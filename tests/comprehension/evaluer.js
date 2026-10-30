// Évaluation d'une phrase de test contre l'analyse produite par le moteur (partagé par le test et le rapport).
const liste = (v) => (Array.isArray(v) ? v : [v]);
export function evaluer(item, an) {
  const erreurs = [];
  const pid = an.principal ? an.principal.id : null;
  const pf = an.principal ? (an.principal.fiche?.id || null) : null;
  const okP = liste(item.p).includes(pid);
  if (!okP) erreurs.push(`argument principal : attendu ${liste(item.p).map(String).join(' ou ')}, obtenu ${pid}`);
  if (item.f !== undefined && !liste(item.f).includes(pf)) erreurs.push(`fiche : attendue ${liste(item.f).map(String).join(' ou ')}, obtenue ${pf}`);
  for (const s of item.sec || []) if (!an.arguments.some((a) => a.id === s)) erreurs.push(`argument secondaire manquant : ${s}`);
  const retenues = an.arguments.map((a) => a.fiche?.id).filter(Boolean);
  for (const x of item.x || []) if (retenues.includes(x)) erreurs.push(`fiche à exclure retenue : ${x}`);
  for (const e of item.emo || []) if (!an.emotions.some((y) => y.id === e)) erreurs.push(`émotion non repérée : ${e}`);
  for (const p of item.proc || []) if (!an.procedes.some((y) => y.id === p)) erreurs.push(`procédé non repéré : ${p}`);
  return { ok: !erreurs.length, erreurs, pid, pf };
}
