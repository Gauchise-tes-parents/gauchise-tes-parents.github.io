// Onglet « Direct » : chaînes de Marty Ducanda et adresses du lecteur et du chat.
// Le site ne contacte NI Twitch NI YouTube pour savoir s'il y a un live : il interroge seulement le détecteur
// du projet (worker-direct/, GTP_CONFIG.directBase). Le lecteur de la plateforme n'est chargé que pendant un live.

export const CHAINES = {
  twitch: { nom: 'Twitch', login: 'martyducanda', url: 'https://www.twitch.tv/martyducanda' },
  youtube: { nom: 'YouTube', handle: 'Martyducanda', url: 'https://www.youtube.com/@Martyducanda' },
};

// Origines des lecteurs officiels autorisées dans la politique de sécurité (frame-src) quand le direct est activé.
export const ORIGINES_LECTEURS = ['https://player.twitch.tv', 'https://www.youtube-nocookie.com'];

const VIDEO_ID = /^[A-Za-z0-9_-]{11}$/;
const HOTE = /^[a-z0-9.-]{1,253}$/i;

/** Plateformes en direct, dans l'ordre de préférence (Twitch puis YouTube). */
export function plateformesEnDirect(s) {
  if (!s || typeof s !== 'object') return [];
  const out = [];
  if (s.twitch?.enDirect) out.push('twitch');
  if (s.youtube?.enDirect && VIDEO_ID.test(s.youtube.videoId || '')) out.push('youtube');
  return out;
}

/** Adresse du lecteur intégré (lecture automatique, son coupé au départ comme l'exigent les navigateurs). */
export function urlLecteur(plateforme, s, hote) {
  if (plateforme === 'twitch') {
    const parent = HOTE.test(hote || '') ? hote : 'gauchise-tes-parents.github.io';
    return `https://player.twitch.tv/?channel=${encodeURIComponent(CHAINES.twitch.login)}&parent=${encodeURIComponent(parent)}&autoplay=true&muted=true`;
  }
  if (plateforme === 'youtube' && VIDEO_ID.test(s?.youtube?.videoId || '')) {
    return `https://www.youtube-nocookie.com/embed/${s.youtube.videoId}?autoplay=1&mute=1&playsinline=1`;
  }
  return null;
}

/** Adresse du chat sur la plateforme (s'ouvre dans un nouvel onglet). */
export function urlChat(plateforme, s) {
  if (plateforme === 'twitch') return `https://www.twitch.tv/popout/${encodeURIComponent(CHAINES.twitch.login)}/chat`;
  if (plateforme === 'youtube' && VIDEO_ID.test(s?.youtube?.videoId || '')) return `https://www.youtube.com/live_chat?is_popout=1&v=${s.youtube.videoId}`;
  return null;
}

/** Adresse du live sur la plateforme elle-même. */
export function urlLive(plateforme, s) {
  if (plateforme === 'twitch') return CHAINES.twitch.url;
  if (plateforme === 'youtube' && VIDEO_ID.test(s?.youtube?.videoId || '')) return `https://www.youtube.com/watch?v=${s.youtube.videoId}`;
  return CHAINES[plateforme]?.url || null;
}

/** Titre du live (texte brut, à échapper à l'affichage). */
export function titreLive(plateforme, s) {
  const t = s?.[plateforme]?.titre;
  return typeof t === 'string' && t.trim() ? t.trim().slice(0, 300) : null;
}
