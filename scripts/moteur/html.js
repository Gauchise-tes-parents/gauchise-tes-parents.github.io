// Lecture minimale de HTML, sans dépendance : suffisante pour des pages de programme bien structurées.
const ENTITES = { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ', rsquo: '’', lsquo: '‘', laquo: '«', raquo: '»', ldquo: '“', rdquo: '”', hellip: '…', ndash: '–', mdash: '—', eacute: 'é', egrave: 'è', agrave: 'à', ecirc: 'ê', ccedil: 'ç', ocirc: 'ô', icirc: 'î', ucirc: 'û', euro: '€', oelig: 'œ' };

export function decoder(s) {
  return String(s || '')
    .replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(Number(n)))
    .replace(/&#x([0-9a-f]+);/gi, (_, n) => String.fromCodePoint(parseInt(n, 16)))
    .replace(/&([a-z]+);/gi, (m, n) => ENTITES[n.toLowerCase()] ?? m);
}

/** Texte brut d'un fragment HTML (balises retirées, entités décodées, espaces normalisés). */
export function texte(html) {
  return decoder(String(html || '').replace(/<br\s*\/?>/gi, ' ').replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ').trim();
}

/** Blocs de titre, paragraphe et puce, dans l'ordre du document : [{ balise, texte }]. */
export function blocs(html) {
  const propre = String(html || '').replace(/<(script|style|noscript|svg|nav|header|form)\b[\s\S]*?<\/\1>/gi, ' ');
  const out = [];
  const re = /<(h[1-6]|p|li)\b[^>]*>([\s\S]*?)<\/\1>/gi;
  let m;
  while ((m = re.exec(propre))) {
    const t = texte(m[2]);
    if (t) out.push({ balise: m[1].toLowerCase(), texte: t });
  }
  return out;
}

/** Liens absolus d'une page. */
export function liens(html, base) {
  const out = new Set();
  for (const m of String(html || '').matchAll(/href\s*=\s*["']([^"'#]+)["']/gi)) {
    try { out.add(new URL(decoder(m[1]), base).href); } catch { /* lien invalide */ }
  }
  return [...out];
}
