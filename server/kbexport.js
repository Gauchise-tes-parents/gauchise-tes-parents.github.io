// Export de la base de connaissances pour le mode autonome (hors ligne) et pour l'hébergement statique.
// La même fonction sert au serveur Node (/kb/base.json) et au script de publication statique.
import { createHash } from 'node:crypto';
import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join, relative, sep } from 'node:path';

const LOADER_FIELDS = ['verdict_label', 'volet_label', 'fiabilite_label', 'stabilite_label', 'type_label', 'rubriques_labels'];
export const KB_FORMAT = 3;

/** Fiche telle qu'enregistrée (sans les libellés ajoutés au chargement). */
const raw = (e) => Object.fromEntries(Object.entries(e).filter(([k]) => !LOADER_FIELDS.includes(k)));

/** Construit la base téléchargeable : contenu canonique + manifeste (version, empreinte SHA-256). */
export function buildKb(library, { veille = null } = {}) {
  const fiches = [...library].sort((a, b) => a.id.localeCompare(b.id)).map(raw);
  const body = { format: KB_FORMAT, fiches };
  const json = JSON.stringify(body);
  const sha256 = createHash('sha256').update(json).digest('hex');
  const derniere = fiches.reduce((m, f) => (f.derniere_verification > m ? f.derniere_verification : m), '');
  const version = `${derniere || 'base'}-${sha256.slice(0, 10)}`;
  const manifest = {
    format: KB_FORMAT,
    version,
    sha256,
    taille: Buffer.byteLength(json),
    nb_fiches: fiches.length,
    derniere_verification: derniere,
    genere_le: new Date().toISOString(),
    veille: veille ? { derniere_reussite: veille.derniere_reussite || null, prochaine: veille.prochaine || null } : null,
  };
  return { json, manifest };
}

/** Liste des fichiers de l'interface à garder en cache pour le hors-ligne (+ version). */
export function assetManifest(publicDir) {
  const files = [];
  const walk = (d) => {
    for (const name of readdirSync(d)) {
      const p = join(d, name);
      if (statSync(p).isDirectory()) { if (name !== 'kb') walk(p); continue; }
      if (/\.(html|css|js|woff|svg|png|webmanifest|txt)$/.test(name) && name !== 'sw.js') files.push(relative(publicDir, p).split(sep).join('/'));
    }
  };
  walk(publicDir);
  files.sort();
  const h = createHash('sha256');
  for (const f of files) h.update(f).update(readFileSync(join(publicDir, f)));
  return { version: h.digest('hex').slice(0, 12), fichiers: ['./', ...files.filter((f) => f !== 'index.html'), 'index.html'] };
}
