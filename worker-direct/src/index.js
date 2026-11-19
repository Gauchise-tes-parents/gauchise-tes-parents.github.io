import { createHandler } from './handler.js';
const handle = createHandler();
export default { fetch: (request, env, ctx) => handle(request, env, ctx) };
