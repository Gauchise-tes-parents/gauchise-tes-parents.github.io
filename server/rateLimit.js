// Limitation des requêtes en mémoire (suffisant pour une instance unique).
// Les adresses IP ne sont ni journalisées ni stockées sur disque ; elles sont hachées en mémoire.
import { createHash } from 'node:crypto';

const hash = (s) => createHash('sha256').update(String(s)).digest('base64url').slice(0, 16);

export class SlidingWindowLimiter {
  constructor({ limit, windowMs, now = () => Date.now() }) {
    this.limit = limit;
    this.windowMs = windowMs;
    this.now = now;
    this.hits = new Map();
  }

  /** Renvoie { ok, retryAfterSec }. */
  take(key) {
    const k = hash(key);
    const t = this.now();
    const list = (this.hits.get(k) || []).filter((x) => t - x < this.windowMs);
    if (list.length >= this.limit) {
      this.hits.set(k, list);
      return { ok: false, retryAfterSec: Math.ceil((this.windowMs - (t - list[0])) / 1000) };
    }
    list.push(t);
    this.hits.set(k, list);
    if (this.hits.size > 50000) this.prune();
    return { ok: true, retryAfterSec: 0 };
  }

  prune() {
    const t = this.now();
    for (const [k, list] of this.hits) {
      if (!list.some((x) => t - x < this.windowMs)) this.hits.delete(k);
    }
  }
}

/** Plafond global quotidien des analyses coûteuses (protège le budget API). */
export class DailyBudget {
  constructor({ limit, now = () => new Date() }) {
    this.limit = limit;
    this.now = now;
    this.day = null;
    this.count = 0;
  }

  dayKey() {
    return this.now().toLocaleDateString('sv-SE', { timeZone: 'Europe/Paris' });
  }

  take() {
    const d = this.dayKey();
    if (d !== this.day) { this.day = d; this.count = 0; }
    if (this.limit > 0 && this.count >= this.limit) return false;
    this.count += 1;
    return true;
  }

  remaining() {
    if (this.dayKey() !== this.day) return this.limit;
    return Math.max(0, this.limit - this.count);
  }
}
