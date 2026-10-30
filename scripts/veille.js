// Veille en ligne de commande (pour une tâche planifiée externe : cron, GitHub Actions…).
//   node scripts/veille.js              exécute un cycle (code de sortie 1 en cas d'échec, 2 si non configurée)
//   node scripts/veille.js --statut     affiche l'état de la veille
//   node scripts/veille.js --retour <fiche> [horodatage]   restaure la version précédente d'une fiche
import { loadConfig, ROOT } from '../server/config.js';
import { loadLibrary, LIBRARY_DIR } from '../server/library.js';
import { createAnthropicProvider } from '../server/engine/providers/anthropic.js';
import { BudgetLedger } from '../server/engine/cost.js';
import { watchConfig, runWatch, readState, rollbackFiche } from '../server/watch/veille.js';

const args = process.argv.slice(2);
const config = loadConfig();
const wc = watchConfig(process.env, ROOT);

if (args[0] === '--statut') {
  console.log(JSON.stringify(readState(wc), null, 2));
  process.exit(0);
}
if (args[0] === '--retour') {
  if (!args[1]) { console.error('Usage : node scripts/veille.js --retour <id-fiche> [horodatage]'); process.exit(2); }
  const v = rollbackFiche(wc, LIBRARY_DIR, args[1], args[2] || null);
  console.log(`Fiche ${args[1]} restaurée depuis la sauvegarde ${v}.`);
  process.exit(0);
}
if (!config.liveMode) {
  console.error('Veille non exécutée : aucune clé ANTHROPIC_API_KEY configurée. Rien n’est simulé.');
  process.exit(2);
}
const ledger = new BudgetLedger({ file: config.usageFile, dailyUsd: config.dailyBudgetUsd, monthlyUsd: config.monthlyBudgetUsd });
const provider = createAnthropicProvider(config, { fetchImpl: fetch });
const library = loadLibrary(LIBRARY_DIR, console);
const report = await runWatch({ wc, config, provider, library, ledger, libraryDir: LIBRARY_DIR, manual: args.includes('--manuel') });
if (report.statut === 'deja_en_cours') { console.log(report.message); process.exit(0); }
const c = report.compteurs;
console.log(`Veille ${report.statut} — collectées ${c.collectees}, vérifiées ${c.verifiees}, en attente ${c.en_attente}, rejetées ${c.rejetees}, doublons ${c.doublons}, fiches actualisées ${c.fiches_actualisees}, coût ${report.cout_usd} $`);
if (report.erreurs.length) console.log(`Erreurs :\n- ${report.erreurs.join('\n- ')}`);
console.log(`Compte rendu : data/watch/rapports/${report.id}.md`);
process.exit(report.statut === 'echec' ? 1 : 0);
