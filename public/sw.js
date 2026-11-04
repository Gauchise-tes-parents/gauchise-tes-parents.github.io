// Service worker du mode autonome : l'interface et la base de connaissances restent disponibles sans Internet
// après une première visite. Les appels /api/ (recherche web, stratégie IA) ne sont JAMAIS mis en cache.
// Version du service worker : la changer force les navigateurs à installer le nouveau (v13.1 : réseau d'abord).
const SW_VERSION = '13.2';
const SHELL = 'gtp-shell-';
const KB_CACHE = 'gtp-kb';

async function assetList() {
  const res = await fetch('asset-manifest.json', { cache: 'no-store' });
  if (!res.ok) throw new Error('asset-manifest indisponible');
  return res.json();
}

// Remplacement d'une version déjà installée ? (noté à l'installation, relu à l'activation)
const META = 'gtp-meta';
self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    if (self.registration.active) await (await caches.open(META)).put('remplacement', new Response('1'));
    const { version, fichiers } = await assetList();
    const cache = await caches.open(SHELL + version);
    await cache.addAll(fichiers);
    // Première installation : la base de connaissances est copiée dans son propre cache.
    const kb = await caches.open(KB_CACHE);
    if (!(await kb.match('kb/base.json'))) {
      const [base, manifest] = await Promise.all([fetch('kb/base.json', { cache: 'no-store' }), fetch('kb/manifest.json', { cache: 'no-store' })]);
      if (base.ok && manifest.ok) { await kb.put('kb/base.json', base); await kb.put('kb/manifest.json', manifest); }
    }
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const { version } = await assetList().catch(() => ({ version: null }));
    const meta = await caches.open(META);
    let ancienne = Boolean(await meta.match('remplacement'));
    await meta.delete('remplacement');
    if (version) {
      for (const key of await caches.keys()) if (key.startsWith(SHELL) && key !== SHELL + version) { ancienne = true; await caches.delete(key); }
    }
    await self.clients.claim();
    // Mise à jour d'une version déjà installée : les pages encore ouvertes sur l'ancienne version sont rechargées
    // d'office (elles ne savent pas forcément se mettre à jour seules). Rien ne se passe à la première installation.
    if (ancienne) {
      for (const client of await self.clients.matchAll({ type: 'window' })) client.navigate(client.url).catch(() => {});
    }
  })());
});

self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  if (event.request.method !== 'GET' || url.origin !== self.location.origin) return;
  const scope = new URL(self.registration.scope);
  const path = url.pathname.slice(scope.pathname.length);
  if (path.startsWith('api/')) return; // réseau uniquement
  if (path === 'kb/base.json' && !url.searchParams.has('v')) {
    // La base est remplacée par l'application, seulement après vérification de son empreinte.
    event.respondWith(caches.open(KB_CACHE).then((c) => c.match('kb/base.json')).then((r) => r || fetch(event.request)));
    return;
  }
  if (path === 'version.json') return; // toujours le réseau : sert à détecter une nouvelle publication
  if (path === 'kb/manifest.json' || path === 'asset-manifest.json') {
    event.respondWith(fetch(event.request).catch(() => caches.open(KB_CACHE).then((c) => c.match('kb/manifest.json')).then((r) => r || new Response('{}', { headers: { 'content-type': 'application/json' } }))));
    return;
  }
  // Réseau d'abord : en ligne, on reçoit toujours la dernière version du site (page, configuration, scripts) ;
  // la copie locale ne sert qu'hors ligne. Chaque réponse fraîche met à jour la copie locale.
  event.respondWith((async () => {
    try {
      const res = await fetch(event.request, { cache: 'no-cache' });
      if (res.ok && res.type === 'basic') {
        const copie = res.clone();
        caches.keys().then((keys) => keys.filter((k) => k.startsWith(SHELL)).sort().pop())
          .then((nom) => nom && caches.open(nom)).then((c) => c && c.put(event.request, copie)).catch(() => {});
      }
      return res;
    } catch {
      const cached = await caches.match(event.request, { ignoreSearch: true });
      if (cached) return cached;
      // Navigation hors ligne : on renvoie l'application (routage par #).
      if (event.request.mode === 'navigate') return (await caches.match('index.html')) || (await caches.match('./'));
      throw new Error('hors ligne');
    }
  })());
});
