(() => {
  'use strict';
  const chinese = document.documentElement.lang.startsWith('zh');
  document.querySelectorAll('.language-switch').forEach(link => link.addEventListener('click', () => { const target = new URL(link.href); target.search = location.search; target.hash = location.hash; link.href = target.href; }));
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#site-nav');
  function closeMenu() { toggle?.setAttribute('aria-expanded', 'false'); nav?.classList.remove('open'); }
  toggle?.addEventListener('click', () => { const open = toggle.getAttribute('aria-expanded') !== 'true'; toggle.setAttribute('aria-expanded', String(open)); nav.classList.toggle('open', open); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') { const wasOpen = toggle?.getAttribute('aria-expanded') === 'true'; closeMenu(); if (wasOpen) toggle.focus(); } });
  nav?.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
  document.addEventListener('click', e => { if (!e.target.closest('.site-header')) closeMenu(); });
  matchMedia('(min-width: 821px)').addEventListener('change', e => { if (e.matches) closeMenu(); });

  const form = document.querySelector('.paper-filters');
  if (form) {
    const search = document.querySelector('#paper-search');
    const topic = document.querySelector('#paper-topic');
    const kind = document.querySelector('#paper-kind');
    const year = document.querySelector('#paper-year');
    const rows = [...document.querySelectorAll('.paper-row')];
    const years = [...document.querySelectorAll('.paper-year')];
    const count = document.querySelector('#paper-count');
    const url = new URL(location.href);
    search.value = url.searchParams.get('q') || '';
    for (const [key, select] of [['topic', topic], ['kind', kind], ['year', year]]) {
      const value = url.searchParams.get(key);
      if (value && [...select.options].some(o => o.value === value)) select.value = value;
    }
    const normalize = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    function filter(updateUrl = true) {
      const tokens = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
      let visible = 0;
      for (const row of rows) {
        const data = row.dataset;
        const match = (!topic.value || data.topic === topic.value) && (!kind.value || data.kind === kind.value) && (!year.value || data.year === year.value) && tokens.every(word => normalize(data.search).includes(word));
        row.hidden = !match;
        if (match) visible++;
      }
      for (const group of years) {
        const n = group.querySelectorAll('.paper-row:not([hidden])').length;
        group.hidden = n === 0;
        group.querySelector('h2 span').textContent = chinese ? `${n} 项成果` : `${n} ${n === 1 ? 'publication' : 'publications'}`;
        const link = document.querySelector(`.year-nav a[href="#${group.id}"]`);
        if (link) { link.hidden = n === 0; link.querySelector('span').textContent = n; }
      }
      count.textContent = chinese ? `共 ${rows.length} 项成果，当前显示 ${visible} 项` : `${visible} of ${rows.length} publications`;
      document.querySelector('.no-results').hidden = visible !== 0;
      if (updateUrl) {
        const next = new URL(location.href);
        for (const [key, value] of [['q', search.value.trim()], ['topic', topic.value], ['kind', kind.value], ['year', year.value]]) {
          if (value) next.searchParams.set(key, value); else next.searchParams.delete(key);
        }
        history.replaceState(null, '', next);
      }
    }
    form.addEventListener('input', () => filter());
    form.addEventListener('change', () => filter());
    form.addEventListener('submit', e => { e.preventDefault(); filter(); });
    form.addEventListener('reset', () => { search.value = ''; topic.value = ''; kind.value = ''; year.value = ''; requestAnimationFrame(() => filter()); });
    filter(false);
  }
  let toastTimer;
  function announce(text) { const el = document.querySelector('.toast'); el.textContent = text; el.classList.add('visible'); clearTimeout(toastTimer); toastTimer = setTimeout(() => el.classList.remove('visible'), 3000); }
  document.querySelectorAll('.copy-citation').forEach(button => button.addEventListener('click', async () => {
    const target = document.getElementById(button.dataset.target);
    try { await navigator.clipboard.writeText(target.textContent.trim()); announce(chinese ? '已复制 BibTeX 引用' : 'BibTeX copied to clipboard'); }
    catch { const range = document.createRange(); range.selectNodeContents(target); const selection = getSelection(); selection.removeAllRanges(); selection.addRange(range); announce(chinese ? '已选中引用，请按 Ctrl+C 或 ⌘C 复制。' : 'Citation selected. Press Ctrl+C or ⌘C to copy.'); }
  }));
})();
