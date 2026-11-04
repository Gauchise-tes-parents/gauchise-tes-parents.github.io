// Configuration de déploiement (lue avant l'application).
// apiBase : null = même origine que l'interface (serveur Node). Une URL (https://…) = serveur séparé.
// Sur un hébergement statique sans serveur, laisser null : le mode connecté sera indiqué « non configuré ».
// iaBase : URL https du backend IA (Cloudflare Worker Gemini) ; null = pas d'IA. Aucune clé ici : elle reste dans le Worker.
window.GTP_CONFIG = { apiBase: null, iaBase: null };
