/* TITAN Prism shell — panels only */
(function () {
'use strict';
const T = window.T, ST = T.ST, $ = T.$, $$ = T.$$;

function shellPanels() {
  // Classic bottom-nav panels layout (default)
  document.body.classList.add('shell-panels');
}

function applyShell(name) {
  document.body.className = document.body.className.replace(/shell-\w+/g, '');
  const n = (name || 'panels').toLowerCase();
  document.body.classList.add('shell-' + n);
  if (n === 'panels') shellPanels();
  try { ST.set('shell', n); } catch (e) {}
}

T.shell = { apply: applyShell };

// init
try {
  applyShell(ST.get('shell') || 'panels');
} catch (e) {
  applyShell('panels');
}
})();
