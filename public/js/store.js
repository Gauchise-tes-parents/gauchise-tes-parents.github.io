// Données locales de l'utilisateur, stockées UNIQUEMENT sur cet appareil (localStorage) :
// réglages, argumentaires que l'utilisateur a choisi d'enregistrer, profils d'interlocuteur facultatifs.
// Rien n'est envoyé au serveur. Tout est modifiable et supprimable depuis « Mes données ».
// Confidentialité (v13) : AUCUN historique automatique — les fiches consultées ne sont plus notées.
const ST_KEY = 'gtp-donnees-v1';
const ST_LIMITS = { argumentaires: 100, profils: 12 };

const stEmpty = () => ({ reglages: { mode: 'autonome', majAuto: true }, argumentaires: [], profils: [] });
let stMemory = null;

function stRead() {
  if (stMemory) return stMemory;
  try { stMemory = { ...stEmpty(), ...JSON.parse(localStorage.getItem(ST_KEY) || 'null') }; } catch { stMemory = stEmpty(); }
  stMemory.reglages = { ...stEmpty().reglages, ...(stMemory.reglages || {}) };
  // purge de l'historique de consultation laissé par les versions précédentes
  if ('historique' in stMemory) { delete stMemory.historique; stWrite(); }
  return stMemory;
}
function stWrite() {
  try { localStorage.setItem(ST_KEY, JSON.stringify(stMemory)); return true; } catch { return false; }
}
const stUid = () => `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 8)}`;
const stNow = () => new Date().toISOString();

export const store = {
  /** false si le navigateur refuse le stockage : l'application fonctionne, mais rien n'est conservé. */
  persistant() { try { localStorage.setItem('gtp-test', '1'); localStorage.removeItem('gtp-test'); return true; } catch { return false; } },

  reglages: () => stRead().reglages,
  setReglage(k, v) { stRead().reglages[k] = v; return stWrite(); },


  argumentaires: () => stRead().argumentaires,
  enregistrerArgumentaire(a) {
    const d = stRead();
    const item = { ...a, id: stUid(), date: stNow() };
    d.argumentaires = [item, ...d.argumentaires].slice(0, ST_LIMITS.argumentaires);
    return stWrite() ? item : null;
  },
  supprimerArgumentaire(id) { const d = stRead(); d.argumentaires = d.argumentaires.filter((x) => x.id !== id); return stWrite(); },

  profils: () => stRead().profils,
  enregistrerProfil(p) {
    const d = stRead();
    const item = { ...p, id: p.id || stUid(), date: stNow() };
    d.profils = [item, ...d.profils.filter((x) => x.id !== item.id)].slice(0, ST_LIMITS.profils);
    return stWrite() ? item : null;
  },
  supprimerProfil(id) { const d = stRead(); d.profils = d.profils.filter((x) => x.id !== id); return stWrite(); },

  effacer(quoi) {
    const d = stRead();
    if (quoi === 'tout') stMemory = { ...stEmpty(), reglages: d.reglages };
    else d[quoi] = [];
    return stWrite();
  },
};
