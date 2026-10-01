/* Art by Nuella — shared interactions */
(function () {
  'use strict';

  /* mobile nav */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      toggle.classList.toggle('open');
      nav.classList.toggle('open');
    });
  }

  /* scroll reveal */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) en.target.classList.add('visible'); });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

  /* footer year */
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  /* lightbox for galleries */
  var items = Array.prototype.slice.call(document.querySelectorAll('.pg-item:not(.g-link)'));
  if (items.length) {
    var lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.innerHTML =
      '<button class="lb-close" aria-label="Close">&times;</button>' +
      '<button class="lb-nav lb-prev" aria-label="Previous">&#8249;</button>' +
      '<img alt="">' +
      '<button class="lb-nav lb-next" aria-label="Next">&#8250;</button>' +
      '<div class="lb-cap"></div>';
    document.body.appendChild(lb);
    var lbImg = lb.querySelector('img');
    var lbCap = lb.querySelector('.lb-cap');
    var idx = 0;
    function show(i) {
      idx = (i + items.length) % items.length;
      var it = items[idx];
      lbImg.src = it.getAttribute('data-full') || it.querySelector('img').src;
      var c = it.querySelector('.pg-cap');
      lbCap.textContent = c ? c.textContent.replace(/\s+/g, ' ').trim() : '';
    }
    function open(i) { show(i); lb.classList.add('open'); document.body.style.overflow = 'hidden'; }
    function close() { lb.classList.remove('open'); document.body.style.overflow = ''; }
    items.forEach(function (it, i) { it.addEventListener('click', function (e) { e.preventDefault(); open(i); }); });
    lb.querySelector('.lb-close').addEventListener('click', close);
    lb.querySelector('.lb-prev').addEventListener('click', function (e) { e.stopPropagation(); show(idx - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function (e) { e.stopPropagation(); show(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft') show(idx - 1);
      else if (e.key === 'ArrowRight') show(idx + 1);
    });
  }

  /* quote form
     FORM_ENDPOINT: paste the Google Apps Script "web app" URL here (see _setup/README-forms.md).
     While it is empty the form just shows the thank-you message (demo mode) and sends nothing. */
  var FORM_ENDPOINT = '';
  var PHONE_TEXT = '+1 (587) 664-7416';

  document.querySelectorAll('form.quote-form').forEach(function (form) {
    var btn = form.querySelector('button[type=submit]');
    var err = form.querySelector('.form-error');

    function thanks() {
      var wrap = form.closest('.quote-wrap');
      form.style.display = 'none';
      wrap.querySelectorAll(':scope > h2, :scope > p').forEach(function (n) { n.style.display = 'none'; });
      var ok = wrap.querySelector('.form-success');
      if (ok) ok.classList.add('show');
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = new URLSearchParams(new FormData(form));
      if (data.get('website')) { thanks(); return; }            /* honeypot: bots fill this, people never see it */
      data.delete('website');
      data.append('page', (location.pathname.split('/').pop() || 'index.html'));
      if (err) err.classList.remove('show');
      if (!FORM_ENDPOINT) { thanks(); return; }                 /* demo mode */

      var label = btn.textContent;
      btn.disabled = true; btn.textContent = 'Sending...';
      fetch(FORM_ENDPOINT, { method: 'POST', mode: 'no-cors', body: data })
        .then(thanks)
        .catch(function () {
          btn.disabled = false; btn.textContent = label;
          if (err) { err.textContent = 'Sorry, that did not go through. Please call ' + PHONE_TEXT + ' or try again.'; err.classList.add('show'); }
        });
    });
  });
})();
