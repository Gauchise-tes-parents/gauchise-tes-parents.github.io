// Illustrations originales en SVG, générées par code (personnages fictifs, aucune personne réelle).
// Style : contours d'encre épais, aplats francs, expressions exagérées mais bienveillantes.

const INK = '#241E2E';
const C = {
  night: '#2B1A5C', lemon: '#FFE11A', orange: '#FF7A2F', cream: '#FFF7E6', white: '#FFFFFF',
  pink: '#FF9E9E', sky: '#BFE9FF', teal: '#138A6E', raspberry: '#D7263D', lilac: '#9B7BEA', grey: '#8C84A6',
};
const SKIN = ['#F6C9A0', '#E5AE84', '#C68A5E', '#8F5B3A', '#F3D7BF'];
const sw = 'stroke="' + INK + '" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"';

// ---------- Visage ----------
function eyes(expr) {
  const L = 47, R = 73, Y = 60;
  const dot = (x, y = Y, r = 3.6) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${INK}"/>`;
  const brow = (x1, y1, x2, y2) => `<path d="M${x1} ${y1} L${x2} ${y2}" fill="none" ${sw} stroke-width="4"/>`;
  switch (expr) {
    case 'happy':
      return `<path d="M41 61 Q47 53 53 61 M67 61 Q73 53 79 61" fill="none" ${sw}/>`;
    case 'sure': // paupières mi-closes, sûr de lui
      return `${dot(L, 61)}${dot(R, 61)}<path d="M40 58 H54 M66 58 H80" fill="none" ${sw} stroke-width="4.5"/>${brow(40, 50, 53, 52)}${brow(67, 52, 80, 50)}`;
    case 'surprised':
      return `<circle cx="${L}" cy="${Y}" r="7" fill="#fff" ${sw} stroke-width="3"/><circle cx="${R}" cy="${Y}" r="7" fill="#fff" ${sw} stroke-width="3"/>${dot(L, Y, 3)}${dot(R, Y, 3)}${brow(40, 46, 53, 44)}${brow(67, 44, 80, 46)}`;
    case 'angry':
      return `${dot(L, 62)}${dot(R, 62)}${brow(39, 50, 54, 56)}${brow(66, 56, 81, 50)}`;
    case 'worried':
      return `${dot(L, 62)}${dot(R, 62)}${brow(40, 54, 53, 49)}${brow(67, 49, 80, 54)}`;
    case 'skeptic':
      return `${dot(L, 61)}<path d="M66 61 H80" fill="none" ${sw}/>${brow(40, 53, 53, 53)}<path d="M66 50 Q73 43 80 48" fill="none" ${sw} stroke-width="4"/>`;
    case 'wink':
      return `${dot(L)}<path d="M66 61 Q73 56 80 61" fill="none" ${sw}/>${brow(40, 50, 53, 49)}`;
    case 'stars':
      return `${star(L, Y, 7)}${star(R, Y, 7)}`;
    case 'closed':
      return `<path d="M41 60 Q47 65 53 60 M67 60 Q73 65 79 60" fill="none" ${sw}/>`;
    default:
      return `${dot(L)}${dot(R)}`;
  }
}
function star(x, y, r) {
  const pts = [];
  for (let i = 0; i < 10; i += 1) {
    const a = (Math.PI / 5) * i - Math.PI / 2;
    const rr = i % 2 ? r * 0.45 : r;
    pts.push(`${(x + rr * Math.cos(a)).toFixed(1)},${(y + rr * Math.sin(a)).toFixed(1)}`);
  }
  return `<polygon points="${pts.join(' ')}" fill="${C.lemon}" ${sw} stroke-width="2"/>`;
}
function mouth(expr) {
  switch (expr) {
    case 'shout':
      return `<path d="M48 76 Q60 72 72 76 Q70 92 60 92 Q50 92 48 76 Z" fill="${INK}"/><path d="M53 87 Q60 83 67 87 Q64 91 60 91 Q56 91 53 87Z" fill="${C.pink}"/>`;
    case 'smile':
      return `<path d="M49 76 Q60 86 71 76" fill="none" ${sw}/>`;
    case 'grin':
      return `<path d="M46 74 H74 Q72 90 60 90 Q48 90 46 74 Z" fill="#fff" ${sw} stroke-width="3"/><path d="M47 79 H73" ${sw} stroke-width="2"/>`;
    case 'o':
      return `<ellipse cx="60" cy="81" rx="5" ry="6.5" fill="${INK}"/>`;
    case 'frown':
      return `<path d="M50 84 Q60 75 70 84" fill="none" ${sw}/>`;
    case 'wavy':
      return `<path d="M48 81 Q52 77 56 81 Q60 85 64 81 Q68 77 72 81" fill="none" ${sw}/>`;
    case 'smirk':
      return `<path d="M50 80 Q62 82 72 74" fill="none" ${sw}/>`;
    case 'teeth':
      return `<rect x="49" y="75" width="22" height="10" rx="3" fill="#fff" ${sw} stroke-width="3"/><path d="M56 75 V85 M64 75 V85" ${sw} stroke-width="2"/>`;
    default:
      return `<path d="M52 80 H68" fill="none" ${sw}/>`;
  }
}
function hair(style, color) {
  const f = `fill="${color}" ${sw}`;
  switch (style) {
    case 'bald':
      return `<path d="M24 58 Q22 44 30 40 Q28 54 32 60 Z" ${f}/><path d="M96 58 Q98 44 90 40 Q92 54 88 60 Z" ${f}/><path d="M44 30 Q52 25 60 26" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".7"/>`;
    case 'bun':
      return `<circle cx="60" cy="14" r="12" ${f}/><path d="M23 62 Q18 22 60 20 Q102 22 97 62 Q94 40 80 34 Q62 42 36 36 Q26 44 23 62 Z" ${f}/>`;
    case 'cap':
      return `<path d="M24 50 Q24 18 60 18 Q96 18 96 50 Z" ${f}/><path d="M60 44 Q90 40 112 48 Q108 54 92 52 L60 50 Z" ${f}/><circle cx="60" cy="19" r="3.5" fill="${INK}"/>`;
    case 'curly':
      return [[30, 40], [40, 28], [54, 22], [68, 22], [82, 28], [92, 40], [26, 54], [96, 54]]
        .map(([x, y]) => `<circle cx="${x}" cy="${y}" r="11" ${f}/>`).join('');
    case 'long':
      return `<path d="M20 100 Q14 30 60 20 Q106 30 100 100 L88 100 Q94 56 80 40 Q60 46 38 40 Q26 56 32 100 Z" ${f}/>`;
    case 'spiky':
      return `<path d="M24 52 L28 30 L38 38 L44 18 L54 32 L62 14 L70 32 L80 18 L84 38 L94 30 L96 52 Q80 40 60 40 Q40 40 24 52 Z" ${f}/>`;
    case 'side':
      return `<path d="M24 56 Q20 24 58 20 Q98 20 96 54 Q90 36 70 32 Q50 40 30 38 Z" ${f}/>`;
    default:
      return '';
  }
}

/**
 * Buste d'un personnage, dessiné dans une boîte 120 x 140.
 * opts : skin, hair, hairColor, shirt, eyes, mouth, mustache, glasses, blush, sweat, steam, earrings
 */
export function person(o = {}) {
  const skin = o.skin || SKIN[0];
  const shirt = o.shirt || C.orange;
  const longBack = o.hair === 'long' ? hair('long', o.hairColor || '#5B3A29') : '';
  return `<g class="person">
    ${longBack}
    <path d="M8 140 Q10 104 60 100 Q110 104 112 140 Z" fill="${shirt}" ${sw}/>
    <path d="M48 102 L60 116 L72 102" fill="none" ${sw}/>
    <rect x="52" y="88" width="16" height="14" fill="${skin}" ${sw} stroke-width="3"/>
    <ellipse cx="24" cy="64" rx="7" ry="9" fill="${skin}" ${sw}/>
    <ellipse cx="96" cy="64" rx="7" ry="9" fill="${skin}" ${sw}/>
    <ellipse cx="60" cy="60" rx="35" ry="38" fill="${skin}" ${sw}/>
    ${o.hair !== 'long' ? hair(o.hair, o.hairColor || '#5B3A29') : `<path d="M28 50 Q34 28 60 28 Q86 28 92 50 Q80 36 60 38 Q40 36 28 50Z" fill="${o.hairColor || '#5B3A29'}" ${sw}/>`}
    ${o.blush ? `<ellipse cx="38" cy="74" rx="7" ry="4" fill="${C.pink}" opacity=".8"/><ellipse cx="82" cy="74" rx="7" ry="4" fill="${C.pink}" opacity=".8"/>` : ''}
    ${o.red ? `<ellipse cx="60" cy="58" rx="33" ry="36" fill="${C.raspberry}" opacity=".18"/>` : ''}
    ${eyes(o.eyes)}
    ${o.glasses ? `<circle cx="47" cy="60" r="10" fill="${C.sky}" fill-opacity=".35" ${sw} stroke-width="3"/><circle cx="73" cy="60" r="10" fill="${C.sky}" fill-opacity=".35" ${sw} stroke-width="3"/><path d="M57 60 H63" ${sw} stroke-width="3"/>` : ''}
    <path d="M58 64 Q54 72 60 73" fill="none" ${sw} stroke-width="3"/>
    ${o.mustache ? `<path d="M44 74 Q52 66 60 72 Q68 66 76 74 Q68 78 60 75 Q52 78 44 74 Z" fill="${o.hairColor || '#5B3A29'}" ${sw} stroke-width="3"/>` : ''}
    ${mouth(o.mouth)}
    ${o.sweat ? `<path d="M93 38 Q99 48 93 52 Q87 48 93 38 Z" fill="${C.sky}" ${sw} stroke-width="2.5"/>` : ''}
    ${o.steam ? `<path d="M20 22 Q14 14 20 6 M100 22 Q106 14 100 6 M60 6 Q54 0 60 -6" fill="none" stroke="${C.grey}" stroke-width="4" stroke-linecap="round"/>` : ''}
    ${o.earrings ? `<circle cx="24" cy="76" r="3.5" fill="${C.lemon}" ${sw} stroke-width="2"/><circle cx="96" cy="76" r="3.5" fill="${C.lemon}" ${sw} stroke-width="2"/>` : ''}
  </g>`;
}

// ---------- Mascotte IA « Doc Source » ----------
const MASCOT_FACES = {
  idle: { eyes: 'default', mouth: 'smile' },
  search: { eyes: 'default', mouth: 'o' },
  confirme: { eyes: 'happy', mouth: 'grin' },
  plutot_exact: { eyes: 'default', mouth: 'smirk' },
  trompeur: { eyes: 'skeptic', mouth: 'wavy' },
  contredit: { eyes: 'surprised', mouth: 'o' },
  inverifiable: { eyes: 'worried', mouth: 'wavy' },
  opinion: { eyes: 'closed', mouth: 'smile' },
  demo: { eyes: 'wink', mouth: 'smile' },
};

/** Mascotte : tête-bulle citron, grosses lunettes, antenne, loupe. Boîte 160 x 170. */
export function mascot(state = 'idle', { withLoupe = true } = {}) {
  const f = MASCOT_FACES[state] || MASCOT_FACES.idle;
  const extra = {
    confirme: `<g transform="translate(118 18)"><path d="M0 22 L8 22 L8 4 Q8 -2 13 0 L14 8 L24 8 Q30 9 28 15 L25 28 Q24 32 19 32 L0 32 Z" fill="${C.lemon}" ${sw} stroke-width="3"/></g>`,
    contredit: `<text x="126" y="40" font-family="Poppins, sans-serif" font-weight="700" font-size="34" fill="${C.raspberry}" stroke="${INK}" stroke-width="1.5">!</text>`,
    inverifiable: `<text x="124" y="40" font-family="Poppins, sans-serif" font-weight="700" font-size="34" fill="${C.night}">?</text>`,
    trompeur: `<path d="M120 20 Q130 10 140 20 Q130 30 120 20 Z M126 38 Q136 28 146 38" fill="none" stroke="${C.orange}" stroke-width="4" stroke-linecap="round"/>`,
    opinion: `<g transform="translate(116 8)"><path d="M18 4 V34 M4 12 H32" ${sw} stroke-width="3"/><path d="M0 24 L4 12 L8 24 Z M28 24 L32 12 L36 24 Z" fill="${C.lilac}" ${sw} stroke-width="2.5"/><path d="M10 34 H26" ${sw} stroke-width="3"/></g>`,
    plutot_exact: `<path d="M122 30 L146 30" stroke="${C.lemon}" stroke-width="6" stroke-linecap="round"/><path d="M122 30 L146 30" ${sw} stroke-width="2" fill="none"/>`,
    demo: `<text x="118" y="34" font-family="Poppins, sans-serif" font-weight="700" font-size="16" fill="${C.night}">démo</text>`,
  }[state] || '';
  return `<g class="mascot mascot--${state}">
    <path d="M80 18 V2" ${sw}/><circle cx="80" cy="0" r="6" fill="${C.orange}" ${sw} stroke-width="3" class="mascot-antenna"/>
    <path d="M40 160 Q42 128 80 124 Q118 128 120 160 Z" fill="${C.night}" ${sw}/>
    <path d="M70 128 L80 140 L90 128" fill="none" stroke="${C.lemon}" stroke-width="4" stroke-linecap="round"/>
    <rect x="24" y="16" width="112" height="110" rx="46" fill="${C.lemon}" ${sw}/>
    <path d="M40 44 Q46 30 62 26" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".8"/>
    <g transform="translate(20 2)">${eyes(f.eyes)}${mouth(f.mouth)}</g>
    <circle cx="67" cy="62" r="15" fill="${C.sky}" fill-opacity=".3" ${sw}/>
    <circle cx="93" cy="62" r="15" fill="${C.sky}" fill-opacity=".3" ${sw}/>
    <path d="M82 62 H78 M52 60 L34 54 M108 60 L126 54" ${sw}/>
    ${withLoupe ? `<g transform="translate(118 112) rotate(-30)"><g class="mascot-loupe">
      <rect x="-6" y="22" width="12" height="32" rx="6" fill="${C.orange}" ${sw} stroke-width="3"/>
      <circle cx="0" cy="0" r="22" fill="${C.sky}" fill-opacity=".7" ${sw} stroke-width="5"/>
      <path d="M-10 -8 Q-6 -15 3 -15" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
    </g></g>` : ''}
    ${extra}
  </g>`;
}

export function mascotSvg(state, label, size = 160) {
  return `<svg class="mascot-svg" viewBox="-6 -12 190 184" width="${size}" height="${Math.round(size * 184 / 190)}" role="img" aria-label="${label}">${mascot(state)}</svg>`;
}

// ---------- Personnages de la famille ----------
export const CAST = {
  tonton: { skin: SKIN[1], hair: 'bald', hairColor: '#7A5A44', shirt: '#4C7BD9', eyes: 'sure', mouth: 'shout', mustache: true, red: true },
  tata: { skin: SKIN[2], hair: 'bun', hairColor: '#2F2230', shirt: C.lilac, eyes: 'happy', mouth: 'smile', earrings: true },
  cousin: { skin: SKIN[0], hair: 'cap', hairColor: C.raspberry, shirt: '#2FB58A', eyes: 'default', mouth: 'o' },
  cousine: { skin: SKIN[3], hair: 'curly', hairColor: '#1E1620', shirt: C.orange, eyes: 'surprised', mouth: 'smile', glasses: false },
  converti: { skin: SKIN[4], hair: 'side', hairColor: '#B9B2A8', shirt: '#E2C044', eyes: 'surprised', mouth: 'o', glasses: true },
  tetu: { skin: SKIN[1], hair: 'spiky', hairColor: '#8B8B8B', shirt: '#8C84A6', eyes: 'closed', mouth: 'frown' },
};

export function personSvg(opts, label, w = 120) {
  return `<svg viewBox="-4 -10 128 154" width="${w}" height="${Math.round(w * 154 / 128)}" role="img" aria-label="${label}">${person(opts)}</svg>`;
}

// Profils de communication (étape 3)
export const PROFILE_ART = {
  convaincu: { skin: SKIN[1], hair: 'bald', hairColor: '#6B4B36', shirt: '#4C7BD9', eyes: 'sure', mouth: 'smirk', mustache: true },
  sceptique: { skin: SKIN[4], hair: 'side', hairColor: '#3A2A20', shirt: '#2FB58A', eyes: 'skeptic', mouth: 'default', glasses: true },
  colerique: { skin: SKIN[0], hair: 'spiky', hairColor: '#7A2F1E', shirt: C.raspberry, eyes: 'angry', mouth: 'teeth', red: true, steam: true },
  pragmatique: { skin: SKIN[2], hair: 'cap', hairColor: C.orange, shirt: '#E2C044', eyes: 'default', mouth: 'smile' },
  preoccupe: { skin: SKIN[3], hair: 'curly', hairColor: '#1E1620', shirt: C.lilac, eyes: 'worried', mouth: 'wavy', sweat: true },
  provocateur: { skin: SKIN[0], hair: 'side', hairColor: '#D8A33A', shirt: C.orange, eyes: 'wink', mouth: 'smirk' },
  curieux: { skin: SKIN[2], hair: 'bun', hairColor: '#5B3A29', shirt: C.sky, eyes: 'stars', mouth: 'o', blush: true },
  mystere: null,
};

export function profileSvg(id, label) {
  if (!PROFILE_ART[id]) {
    return `<svg viewBox="-4 -10 128 154" width="96" height="116" role="img" aria-label="${label}">
      <path d="M8 140 Q10 104 60 100 Q110 104 112 140 Z" fill="${C.night}" ${sw}/>
      <ellipse cx="60" cy="60" rx="35" ry="38" fill="${C.night}" ${sw}/>
      <text x="60" y="78" text-anchor="middle" font-family="Poppins, sans-serif" font-weight="700" font-size="48" fill="${C.lemon}">?</text>
    </svg>`;
  }
  return personSvg(PROFILE_ART[id], label, 96);
}

// ---------- Scène principale : le repas de famille ----------
export function heroScene() {
  const p = (opts, x, y, s = 1, flip = false) => `<g transform="translate(${x} ${y}) scale(${flip ? -s : s} ${s})${flip ? ' translate(-120 0)' : ''}">${person(opts)}</g>`;
  return `<svg class="hero-scene" viewBox="0 0 640 430" role="img" aria-labelledby="heroTitle heroDesc">
  <title id="heroTitle">Le repas de famille</title>
  <desc id="heroDesc">Illustration : à table, un oncle très sûr de lui lance une affirmation sans source. Sa nièce sort une loupe, la tante montre un graphique sur son téléphone et un cousin cherche sur Internet. La mascotte Doc Source examine les chiffres.</desc>
  <!-- mur et fenêtre -->
  <rect x="0" y="0" width="640" height="430" rx="28" fill="#FFE9B8"/>
  <path d="M0 300 H640 V402 Q640 430 612 430 H28 Q0 430 0 402 Z" fill="#F4CE86"/>
  <g transform="translate(250 30)"><rect width="140" height="96" rx="10" fill="${C.sky}" ${sw}/><path d="M70 0 V96 M0 48 H140" ${sw}/><circle cx="34" cy="26" r="12" fill="${C.lemon}"/></g>
  <g transform="translate(412 120)"><rect width="70" height="54" rx="4" fill="#fff" ${sw}/><path d="M10 44 L24 28 L36 36 L50 18 L60 30" fill="none" stroke="${C.orange}" stroke-width="4" stroke-linecap="round"/></g>

  <!-- personnages (derrière la table) -->
  ${p(CAST.tonton, 22, 150, 1.35)}
  ${p(CAST.tata, 190, 172, 1.12)}
  ${p({ ...CAST.cousine, eyes: 'default', mouth: 'smile', glasses: true }, 334, 172, 1.12)}
  ${p(CAST.cousin, 474, 156, 1.25)}

  <!-- tata montre un graphique sur son téléphone -->
  <g class="hero-phone" transform="translate(278 238) rotate(8)">
    <rect width="46" height="78" rx="8" fill="${INK}"/>
    <rect x="5" y="9" width="36" height="58" rx="3" fill="#fff"/>
    <rect x="10" y="44" width="7" height="18" fill="${C.teal}"/><rect x="20" y="34" width="7" height="28" fill="${C.orange}"/><rect x="30" y="22" width="7" height="40" fill="${C.night}"/>
    <circle cx="10" cy="74" r="9" fill="${SKIN[2]}" ${sw} stroke-width="3"/>
  </g>

  <!-- cousine avec la loupe -->
  <g transform="translate(452 250) rotate(-25)"><g class="hero-loupe">
    <rect x="-6" y="22" width="12" height="40" rx="6" fill="${C.orange}" ${sw} stroke-width="3"/>
    <circle cx="0" cy="0" r="26" fill="${C.sky}" fill-opacity=".6" ${sw} stroke-width="5"/>
    <path d="M-12 -9 Q-7 -18 4 -18" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
  </g></g>

  <!-- la table -->
  <path d="M8 330 Q10 312 30 310 H610 Q630 312 632 330 V346 Q632 360 618 360 H22 Q8 360 8 346 Z" fill="#fff" ${sw}/>
  <path d="M40 360 V400 M600 360 V400" ${sw} stroke-width="8"/>
  <path d="M8 336 H632" stroke="${C.raspberry}" stroke-width="4" stroke-dasharray="14 10" opacity=".55"/>
  <!-- poulet rôti -->
  <g transform="translate(108 270)"><ellipse cx="40" cy="44" rx="56" ry="12" fill="#fff" ${sw}/><path d="M6 40 Q4 6 40 6 Q76 6 74 40 Z" fill="#D9893A" ${sw}/><path d="M66 18 L86 6 M84 2 Q92 0 90 10" fill="none" ${sw}/></g>
  <!-- ordinateur portable du cousin -->
  <g transform="translate(520 270)"><path d="M0 0 H78 V48 H0 Z" fill="${C.night}" ${sw}/><path d="M-10 48 H88 L80 58 H-2 Z" fill="#CFC8DD" ${sw}/><text x="39" y="30" text-anchor="middle" font-family="Poppins, sans-serif" font-size="14" font-weight="700" fill="${C.lemon}">www</text></g>
  <!-- carafe d'eau et verres -->
  <g transform="translate(366 272)"><path d="M8 0 H28 V10 Q40 20 38 46 H-2 Q-4 20 8 10 Z" fill="${C.sky}" fill-opacity=".8" ${sw}/></g>
  <g transform="translate(424 290)"><path d="M0 0 H18 L16 28 H2 Z" fill="#fff" ${sw} stroke-width="3"/></g>

  <!-- mascotte au premier plan -->
  <g class="hero-mascot" transform="translate(280 300) scale(.66)">${mascot('search')}</g>

  <!-- bulles -->
  <g class="bubble b1"><path d="M18 18 Q18 6 30 6 H226 Q238 6 238 18 V70 Q238 82 226 82 H110 L82 108 L86 82 H30 Q18 82 18 70 Z" fill="#fff" ${sw}/>
    <text font-family="Poppins, sans-serif" font-weight="700" font-size="17" fill="${INK}"><tspan x="34" y="38">« C'est bien connu,</tspan><tspan x="34" y="62">tout le monde le dit ! »</tspan></text></g>
  <g class="bubble b2"><path d="M440 10 Q440 0 452 0 H618 Q630 0 630 12 V60 Q630 72 618 72 H500 L466 98 L480 72 H452 Q440 72 440 60 Z" fill="${C.lemon}" ${sw}/>
    <text font-family="Poppins, sans-serif" font-weight="700" font-size="17" fill="${INK}"><tspan x="456" y="30">Ah oui ? Selon</tspan><tspan x="456" y="54">quelle source ?</tspan></text></g>
</svg>`;
}

// ---------- Icônes de catégories (40 x 40) ----------
const I = (inner) => `<svg viewBox="0 0 40 40" width="40" height="40" aria-hidden="true">${inner}</svg>`;
const s3 = `stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
export const CATEGORY_ICONS = {
  immigration: I(`<circle cx="20" cy="20" r="14" fill="${C.sky}" ${s3}/><path d="M8 16 Q16 14 18 20 Q20 26 14 30 M24 7 Q22 14 28 16 Q33 18 34 24" fill="none" ${s3}/><path d="M26 28 L34 28 M31 25 L34 28 L31 31" fill="none" ${s3}/>`),
  securite: I(`<path d="M20 5 L33 10 V20 Q33 30 20 36 Q7 30 7 20 V10 Z" fill="#4C7BD9" ${s3}/><path d="M14 20 L18 24 L26 15" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>`),
  rsa: I(`<circle cx="24" cy="12" r="7" fill="${C.lemon}" ${s3}/><text x="24" y="16" text-anchor="middle" font-size="9" font-weight="700" font-family="Poppins,sans-serif" fill="${INK}">€</text><path d="M4 28 H12 Q18 24 24 26 H30 Q33 27 30 30 H22 M12 34 H26 L36 26 Q38 22 34 23 L28 27" fill="${C.cream}" ${s3}/>`),
  travail: I(`<rect x="6" y="13" width="28" height="20" rx="4" fill="${C.orange}" ${s3}/><path d="M15 13 V9 Q15 7 17 7 H23 Q25 7 25 9 V13 M6 21 H34" fill="none" ${s3}/>`),
  'pouvoir-achat': I(`<path d="M4 8 H9 L13 26 H31 L35 13 H11" fill="none" ${s3}/><circle cx="15" cy="32" r="3" fill="${INK}"/><circle cx="29" cy="32" r="3" fill="${INK}"/><path d="M15 17 H31 L29 22 H16 Z" fill="${C.lemon}"/>`),
  impots: I(`<path d="M10 4 H30 V36 L26 33 L22 36 L18 33 L14 36 L10 33 Z" fill="#fff" ${s3}/><path d="M15 12 H25 M15 18 H25 M15 24 H21" fill="none" ${s3}/>`),
  hopital: I(`<rect x="6" y="6" width="28" height="28" rx="8" fill="#fff" ${s3}/><path d="M16 12 H24 V16 H28 V24 H24 V28 H16 V24 H12 V16 H16 Z" fill="${C.raspberry}" ${s3}/>`),
  education: I(`<path d="M20 8 L36 16 L20 24 L4 16 Z" fill="${C.night}" ${s3}/><path d="M10 19 V27 Q20 33 30 27 V19" fill="${C.lilac}" ${s3}/><path d="M34 17 V27" ${s3}/>`),
  retraites: I(`<path d="M12 6 H28 M12 34 H28 M14 6 Q14 16 20 20 Q14 24 14 34 M26 6 Q26 16 20 20 Q26 24 26 34" fill="none" ${s3}/><path d="M16 30 Q20 25 24 30 Z" fill="${C.lemon}" ${s3}/>`),
  ecologie: I(`<path d="M8 32 Q6 10 32 6 Q36 30 12 30" fill="#2FB58A" ${s3}/><path d="M8 32 Q16 20 26 14" fill="none" ${s3}/>`),
  pauvrete: I(`<path d="M20 6 V32 M8 12 H32" ${s3}/><path d="M4 22 L8 12 L12 22 Z M28 26 L32 12 L36 26 Z" fill="${C.lemon}" ${s3}/><path d="M13 34 H27" ${s3}/>`),
  feminisme: I(`<circle cx="20" cy="15" r="9" fill="${C.lilac}" ${s3}/><path d="M20 24 V36 M15 31 H25" ${s3}/>`),
  europe: I(`<circle cx="20" cy="20" r="15" fill="#3355CC" ${s3}/>${Array.from({ length: 12 }, (_, i) => { const a = (i / 12) * Math.PI * 2; return `<circle cx="${(20 + 9.5 * Math.cos(a)).toFixed(1)}" cy="${(20 + 9.5 * Math.sin(a)).toFixed(1)}" r="1.6" fill="${C.lemon}"/>`; }).join('')}`),
  medias: I(`<rect x="5" y="10" width="30" height="21" rx="4" fill="${C.night}" ${s3}/><path d="M15 4 L20 10 L25 4 M12 35 H28" fill="none" ${s3}/><path d="M11 22 Q16 15 20 22 T29 22" fill="none" stroke="${C.lemon}" stroke-width="2.5"/>`),
  institutions: I(`<path d="M5 14 L20 5 L35 14 Z" fill="${C.cream}" ${s3}/><path d="M9 16 V30 M16 16 V30 M24 16 V30 M31 16 V30 M5 33 H35" ${s3}/>`),
  autre: I(`<circle cx="20" cy="20" r="15" fill="${C.lemon}" ${s3}/><text x="20" y="27" text-anchor="middle" font-size="20" font-weight="700" font-family="Poppins,sans-serif" fill="${INK}">?</text>`),
};

// Petites vignettes illustrées pour les trois étapes de la page d'accueil
export function stepArt(n) {
  if (n === 1) return `<svg viewBox="0 0 140 110" width="140" height="110" aria-hidden="true"><g transform="translate(0 6) scale(.7)">${person(CAST.tonton)}</g><g transform="translate(70 6)"><path d="M4 10 Q4 2 12 2 H60 Q68 2 68 10 V36 Q68 44 60 44 H24 L10 58 L14 44 H12 Q4 44 4 36 Z" fill="#fff" ${sw} stroke-width="3"/><text x="36" y="30" text-anchor="middle" font-family="Poppins,sans-serif" font-size="20" font-weight="700" fill="${INK}">!!!</text></g></svg>`;
  if (n === 2) return `<svg viewBox="0 0 140 110" width="140" height="110" aria-hidden="true"><g transform="translate(-4 -4) scale(.68)">${mascot('search')}</g><g transform="translate(92 20)"><rect width="40" height="52" rx="4" fill="#fff" ${sw} stroke-width="3"/><path d="M8 14 H32 M8 24 H32 M8 34 H22" ${sw} stroke-width="2.5"/></g></svg>`;
  return `<svg viewBox="0 0 140 110" width="140" height="110" aria-hidden="true"><g transform="translate(6 6) scale(.7)">${person(CAST.cousine)}</g><g transform="translate(78 14)"><rect width="54" height="40" rx="10" fill="${C.lemon}" ${sw} stroke-width="3"/><path d="M14 20 L24 30 L40 12" fill="none" ${sw} stroke-width="4"/></g></svg>`;
}

// Le personnage qui change d'avis et celui qui campe sur ses positions (page « Comment ça marche »)
export function duoArt() {
  return `<svg viewBox="0 0 320 170" width="320" height="170" role="img" aria-label="Deux personnages : l'un découvre une information et change d'avis, l'autre garde son opinion, bras croisés, avec le sourire.">
    <g transform="translate(10 18)">${person(CAST.converti)}</g>
    <g transform="translate(120 4)"><circle cx="16" cy="16" r="14" fill="${C.lemon}" ${sw} stroke-width="3"/><path d="M10 34 H22 M12 40 H20" ${sw} stroke-width="3"/><path d="M16 -6 V-12 M-2 4 L-8 0 M34 4 L40 0" ${sw} stroke-width="3"/></g>
    <g transform="translate(190 18)">${person(CAST.tetu)}</g>
    <rect x="212" y="128" width="76" height="18" rx="9" fill="#7C7496" ${sw} stroke-width="3" transform="rotate(-8 250 137)"/>
    <rect x="212" y="128" width="76" height="18" rx="9" fill="#9A93B2" ${sw} stroke-width="3" transform="rotate(8 250 137)"/>
  </svg>`;
}

// ---------- Volets thématiques (10) ----------
export const VOLET_ICONS = {
  immigration: CATEGORY_ICONS.immigration,
  securite: CATEGORY_ICONS.securite,
  social: CATEGORY_ICONS.rsa,
  economie: I(`<rect x="6" y="22" width="7" height="12" fill="${C.teal}" ${s3}/><rect x="16" y="15" width="7" height="19" fill="${C.orange}" ${s3}/><rect x="26" y="8" width="7" height="26" fill="${C.lemon}" ${s3}/><path d="M4 36 H36" ${s3}/>`),
  ecologie: CATEGORY_ICONS.ecologie,
  services: CATEGORY_ICONS.hopital,
  droits: CATEGORY_ICONS.pauvrete,
  politique: CATEGORY_ICONS.institutions,
  international: I(`<circle cx="20" cy="20" r="15" fill="${C.sky}" ${s3}/><ellipse cx="20" cy="20" rx="6.5" ry="15" fill="none" ${s3}/><path d="M5 20 H35 M8 12 H32 M8 28 H32" fill="none" ${s3}/>`),
  autre: CATEGORY_ICONS.autre,
};

// ---------- Icônes de la barre d'onglets (24 x 24, couleur héritée) ----------
const T = (inner) => `<svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">${inner}</svg>`;
export const TAB_ICONS = {
  accueil: T('<path d="M3 11 L12 3 L21 11"/><path d="M5 10 V21 H19 V10"/><path d="M10 21 V15 H14 V21"/>'),
  debat: T('<path d="M3 5 H14 V13 H8 L4 16 V13 H3 Z"/><path d="M17 8 H21 V16 H20 V19 L16 16 H10 V15"/>'),
  thematiques: T('<rect x="3" y="3" width="7.5" height="7.5" rx="2"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="2"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="2"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="2"/>'),
  bibliotheque: T('<path d="M4 4 H8 V20 H4 Z"/><path d="M10 4 H14 V20 H10 Z"/><path d="M16 5 L19.5 4 L22 19 L18.5 20 Z"/>'),
  express: T('<path d="M13 2 L4 14 H11 L10 22 L20 9 H13 Z"/>'),
  info: T('<circle cx="12" cy="12" r="9"/><path d="M12 11 V17"/><path d="M12 7.5 V7.6"/>'),
};

// ---------- Cartes des deux modes ----------
/** « Gagner le débat » : une personne présente un graphique, plusieurs personnages écoutent. */
export function modeArtGagner() {
  return `<svg viewBox="0 0 320 170" width="320" height="170" role="img" aria-label="Une personne présente un graphique devant la table ; les autres personnages écoutent attentivement.">
    <rect x="0" y="0" width="320" height="170" rx="18" fill="#FFE9B8"/>
    <g transform="translate(176 14)"><rect width="128" height="86" rx="8" fill="#fff" ${sw}/>
      <rect x="16" y="50" width="18" height="26" fill="${C.teal}" ${sw} stroke-width="2.5"/><rect x="44" y="34" width="18" height="42" fill="${C.orange}" ${sw} stroke-width="2.5"/><rect x="72" y="18" width="18" height="58" fill="${C.night}" ${sw} stroke-width="2.5"/>
      <path d="M100 26 L112 14 M104 14 H112 V22" fill="none" ${sw} stroke-width="3"/>
      <path d="M40 86 L32 112 M88 86 L96 112" ${sw}/></g>
    <g transform="translate(118 30) scale(.95)">${person({ ...CAST.cousine, eyes: 'happy', mouth: 'grin', glasses: true })}</g>
    <path d="M206 74 L232 60" stroke="${INK}" stroke-width="12" stroke-linecap="round"/><path d="M206 74 L232 60" stroke="${C.orange}" stroke-width="6" stroke-linecap="round"/>
    <g transform="translate(-4 70) scale(.72)">${person({ ...CAST.tonton, eyes: 'surprised', mouth: 'o', red: false })}</g>
    <g transform="translate(54 84) scale(.62)">${person({ ...CAST.tata, eyes: 'stars', mouth: 'o' })}</g>
    <path d="M0 150 H320 V152 Q320 170 302 170 H18 Q0 170 0 152 Z" fill="#F4CE86"/>
  </svg>`;
}

/** « Convaincre sans braquer » : deux personnages discutent calmement, une bulle et une loupe. */
export function modeArtConvaincre() {
  return `<svg viewBox="0 0 320 170" width="320" height="170" role="img" aria-label="Deux personnages discutent calmement autour d'une tasse ; une bulle de dialogue et une loupe entre eux.">
    <rect x="0" y="0" width="320" height="170" rx="18" fill="#E6F4FB"/>
    <g transform="translate(14 40)">${person({ ...CAST.tata, eyes: 'happy', mouth: 'smile' })}</g>
    <g transform="translate(186 40)">${person({ ...CAST.converti, eyes: 'default', mouth: 'smile', glasses: true })}</g>
    <g transform="translate(108 8)"><path d="M6 14 Q6 4 16 4 H94 Q104 4 104 14 V44 Q104 54 94 54 H62 L52 68 L50 54 H16 Q6 54 6 44 Z" fill="#fff" ${sw}/>
      <g transform="translate(55 30) rotate(-30)"><rect x="-3.5" y="12" width="7" height="18" rx="3.5" fill="${C.orange}" ${sw} stroke-width="2.5"/><circle r="12" fill="${C.sky}" ${sw} stroke-width="3.5"/></g>
      <circle cx="26" cy="29" r="4" fill="${C.lilac}"/><circle cx="84" cy="29" r="4" fill="${C.teal}"/></g>
    <g transform="translate(140 120)"><path d="M0 0 H34 V20 Q34 32 17 32 Q0 32 0 20 Z" fill="${C.lemon}" ${sw}/><path d="M34 6 Q44 6 44 14 Q44 22 34 20" fill="none" ${sw}/><path d="M10 -8 Q6 -14 10 -20 M22 -8 Q18 -14 22 -20" fill="none" stroke="${C.grey}" stroke-width="3" stroke-linecap="round"/></g>
    <path d="M0 158 H320 Q320 170 304 170 H16 Q0 170 0 158 Z" fill="#BFDDEB"/>
  </svg>`;
}
