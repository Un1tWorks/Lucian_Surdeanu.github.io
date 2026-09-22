/*! mini-coi v0.3.0 - MIT */
// Registers a Service Worker to inject COOP/COEP security headers into page responses.
// This enables SharedArrayBuffer so PyScript can handle blocking Python input() calls in a worker thread.
if (typeof document !== 'undefined') {
  const script = document.currentScript;
  if (!window.crossOriginIsolated && !navigator.serviceWorker.controller) {
    navigator.serviceWorker.register(script.src).then((reg) => {
      reg.active && window.location.reload();
      reg.addEventListener('updatefound', () => {
        const sw = reg.installing;
        sw.addEventListener('statechange', () => {
          if (sw.state === 'activated') window.location.reload();
        });
      });
    });
  }
} else {
  self.addEventListener('install', () => self.skipWaiting());
  self.addEventListener('activate', (e) => e.waitUntil(self.clients.claim()));
  self.addEventListener('fetch', (e) => {
    if (e.request.cache === 'only-if-cached' && e.request.mode !== 'same-origin') return;
    e.respondWith(
      fetch(e.request).then((res) => {
        if (res.status === 0) return res;
        const headers = new Headers(res.headers);
        headers.set('Cross-Origin-Embedder-Policy', 'require-corp');
        headers.set('Cross-Origin-Opener-Policy', 'same-origin');
        return new Response(res.body, { status: res.status, statusText: res.statusText, headers });
      })
    );
  });
}