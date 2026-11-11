// Jauge de soutien affichée discrètement sous l'en-tête (lien vers Tipeee).
// Chiffres recopiés à la main depuis la page publique Tipeee du projet, lors de la mise à jour quotidienne des fiches :
// aucune requête vers Tipeee n'est faite depuis le site (zéro site tiers contacté pendant une visite).
export const SOUTIEN = {
  montant: 45,          // euros par mois affichés par Tipeee (champ « tipperAmount », campagne « par mois »)
  tipeurs: 11,          // nombre de tipeurs affiché par Tipeee
  objectif: 1000,       // objectif mensuel fixé par Marty Ducanda
  maj: '2026-11-11',    // date du relevé
};

/** Part de l'objectif atteinte, bornée entre 0 et 100 (au moins 2 % pour que la jauge reste visible). */
export function soutienPourcentage(s = SOUTIEN) {
  const p = (Number(s.montant) / Number(s.objectif)) * 100;
  if (!Number.isFinite(p) || p <= 0) return 0;
  return Math.min(100, Math.max(2, Math.round(p * 10) / 10));
}

/** Montant en euros au format français (« 1 000 € »). */
export function euros(n) {
  return `${new Intl.NumberFormat('fr-FR', { maximumFractionDigits: 0 }).format(Number(n) || 0).replace(/ /g, ' ')} €`;
}
