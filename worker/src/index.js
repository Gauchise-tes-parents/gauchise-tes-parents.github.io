// Point d'entrée Cloudflare Worker. La bibliothèque est intégrée au déploiement (kb.json, produit par
// « npm run worker:kb ») : le serveur choisit lui-même les extraits envoyés à Gemini.
// Secret obligatoire : GEMINI_API_KEY (wrangler secret put GEMINI_API_KEY). Réglages : wrangler.toml.
import KB from './kb.json' with { type: 'json' };
import { createHandler } from './handler.js';

const handle = createHandler({ fiches: KB.fiches || [] });

export default {
  fetch: (request, env, ctx) => handle(request, env, ctx),
};
