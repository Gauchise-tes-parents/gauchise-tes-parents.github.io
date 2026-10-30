import { loadConfig } from './config.js';
import { createApp } from './app.js';

const config = loadConfig();
const { server, library } = createApp(config);

server.listen(config.port, config.host, () => {
  console.log(`\n  Gauchise tes parents — http://${config.host}:${config.port}`);
  console.log(`  Moteur : ${config.liveMode ? `RÉEL (recherche + consultation Web, ${config.researchModel} / ${config.strategyModel})` : 'DÉMONSTRATION (aucune clé ANTHROPIC_API_KEY : aucune recherche réelle)'}`);
  console.log(`  Bibliothèque : ${library.length} fiche(s) chargée(s)`);
  if (config.liveMode) console.log(`  Budget : ${config.dailyBudgetUsd} $/jour, ${config.monthlyBudgetUsd} $/mois (0 = sans plafond)`);
  console.log('');
});

const shutdown = () => server.close(() => process.exit(0));
process.on('SIGINT', shutdown);
process.on('SIGTERM', shutdown);
