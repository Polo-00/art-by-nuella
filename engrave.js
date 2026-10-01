/* Art by Nuella — "see your name engraved" live preview.
   Type text, pick a piece and a style; a laser bar sweeps across and the text burns in.
   Preview only: the final layout is always confirmed with the customer. */
(function () {
  'use strict';
  var svg = document.getElementById('d-svg');
  if (!svg) return;
  var NS = 'http://www.w3.org/2000/svg';
  var $ = function (id) { return document.getElementById(id); };
  var in1 = $('d-line1'), in2 = $('d-line2');
  var itemG = $('d-item'), textEngr = $('d-text-engr'), textGlow = $('d-text-glow');
  var clipEngr = $('d-clip-engr'), clipGlow = $('d-clip-glow');
  var laser = $('d-laser'), spark = $('d-spark');

  var ITEMS = {
    tumbler: { cx: 210, cy: 250, maxW: 158, color: '#3b2c1e', op: 0.92, glow: '#ff9a4d', quoteType: 'Engraved cup or bottle', label: 'Tumbler' },
    board:   { cx: 210, cy: 250, maxW: 250, color: '#24120a', op: 0.86, glow: '#ffb36b', quoteType: 'Chopping board', label: 'Cutting board' },
    crystal: { cx: 210, cy: 214, maxW: 176, color: '#fff6e6', op: 0.95, glow: '#ffd39a', quoteType: 'Photo crystal', label: 'Crystal' }
  };
  var FONTS = {
    script: { family: '"Great Vibes", cursive', weight: 400, size: 86, spacing: 0, upper: false },
    serif:  { family: 'Georgia, "Times New Roman", serif', weight: 400, size: 58, spacing: 1, upper: false },
    bold:   { family: '"Bricolage Grotesque", sans-serif', weight: 800, size: 52, spacing: 1.5, upper: true }
  };

  var state = { item: 'tumbler', font: 'script' };
  var progress = 1, raf = null, box = { x: 0, y: 0, w: 1, h: 1 };
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function el(name, attrs, html) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (html) n.innerHTML = html;
    return n;
  }

  /* ---------- the three pieces ---------- */
  function drawItem() {
    var g = '';
    if (state.item === 'tumbler') {
      g += '<ellipse cx="210" cy="430" rx="104" ry="12" fill="#3a2a18" opacity=".18"/>';
      g += '<rect x="118" y="38" width="184" height="30" rx="12" fill="#2b241d"/>';
      g += '<rect x="196" y="18" width="28" height="26" rx="10" fill="#3a3027"/>';
      g += '<path d="M112 74 L308 74 L292 408 Q210 426 128 408 Z" fill="url(#g-tumbler)" stroke="#cbbba0" stroke-width="1.5"/>';
      g += '<rect x="132" y="80" width="14" height="318" rx="7" fill="#fff" opacity=".38"/>';
      g += '<rect x="284" y="80" width="8" height="318" rx="4" fill="#000" opacity=".06"/>';
    } else if (state.item === 'board') {
      g += '<ellipse cx="210" cy="392" rx="160" ry="14" fill="#3a2a18" opacity=".2"/>';
      g += '<rect x="52" y="116" width="316" height="252" rx="26" fill="url(#g-board)"/>';
      g += '<rect x="168" y="58" width="84" height="98" rx="42" fill="url(#g-board)"/>';
      g += '<circle cx="210" cy="96" r="13" fill="#f3e9d6"/>';
      for (var i = 0; i < 9; i++) {
        var y = 132 + i * 27;
        g += '<path d="M60 ' + y + ' C 130 ' + (y - 7) + ', 250 ' + (y + 8) + ', 360 ' + (y - 2) + '" stroke="#5d3413" stroke-width="1.6" fill="none" opacity=".16"/>';
      }
      g += '<rect x="52" y="116" width="316" height="252" rx="26" fill="none" stroke="#5d3413" stroke-opacity=".35" stroke-width="2"/>';
    } else {
      g += '<ellipse cx="210" cy="428" rx="140" ry="12" fill="#000" opacity=".22"/>';
      g += '<rect x="66" y="372" width="288" height="40" rx="10" fill="#17120d"/>';
      g += '<rect x="80" y="372" width="260" height="5" rx="2.5" fill="#e67a30"/>';
      g += '<rect x="80" y="368" width="260" height="14" rx="7" fill="#e67a30" opacity=".35" filter="url(#f-blur)"/>';
      g += '<rect x="102" y="66" width="216" height="306" rx="10" fill="url(#g-crystal)" stroke="#f2e2c4" stroke-opacity=".45" stroke-width="1.5"/>';
      g += '<rect x="110" y="74" width="10" height="290" rx="5" fill="#fff" opacity=".2"/>';
      g += '<rect x="112" y="356" width="196" height="16" fill="#e67a30" opacity=".18"/>';
    }
    itemG.innerHTML = g;
  }

  /* ---------- text ---------- */
  function layoutText() {
    var it = ITEMS[state.item], f = FONTS[state.font];
    var t1 = (in1.value || '').trim(), t2 = (in2.value || '').trim();
    if (f.upper) { t1 = t1.toUpperCase(); t2 = t2.toUpperCase(); }
    [textEngr, textGlow].forEach(function (grp) {
      grp.innerHTML = '';
      var color = grp === textEngr ? it.color : it.glow;
      var ops = grp === textEngr ? it.op : 1;
      var line1 = el('text', { 'text-anchor': 'middle', x: it.cx, y: it.cy, fill: color, 'fill-opacity': ops });
      var line2 = el('text', { 'text-anchor': 'middle', x: it.cx, y: it.cy + 34, fill: color, 'fill-opacity': ops });
      [line1, line2].forEach(function (ln, idx) {
        ln.style.fontFamily = idx === 0 ? f.family : (state.font === 'script' ? 'Georgia, serif' : f.family);
        ln.style.fontWeight = idx === 0 ? f.weight : (state.font === 'bold' ? 600 : 400);
        ln.style.letterSpacing = f.spacing + 'px';
        if (idx === 1 && state.font === 'script') ln.style.fontStyle = 'italic';
        if (idx === 1) ln.style.letterSpacing = (state.font === 'bold' ? 2 : 1) + 'px';
      });
      line1.textContent = t1; line2.textContent = t2;
      grp.appendChild(line1); grp.appendChild(line2);
      if (grp === textEngr) grp.setAttribute('data-ready', '1');
    });
    /* fit each line to the piece */
    var l1 = textEngr.children[0], l2 = textEngr.children[1];
    var fs1 = f.size; l1.style.fontSize = fs1 + 'px';
    var w1 = l1.getComputedTextLength() || 1;
    if (w1 > it.maxW) fs1 = fs1 * it.maxW / w1;
    fs1 = Math.max(fs1, 16);
    var fs2 = Math.min(Math.max(fs1 * 0.42, 12), 22);
    l2.style.fontSize = fs2 + 'px';
    var w2 = l2.getComputedTextLength() || 1;
    if (w2 > it.maxW) fs2 = Math.max(9, fs2 * it.maxW / w2);
    [textGlow, textEngr].forEach(function (grp) {
      grp.children[0].style.fontSize = fs1 + 'px';
      grp.children[1].style.fontSize = fs2 + 'px';
      grp.children[0].setAttribute('y', it.cy - (t2 ? 6 : -10));
      grp.children[1].setAttribute('y', it.cy - (t2 ? 6 : -10) + fs1 * 0.5 + fs2 * 0.9 + 6);
    });
    var bb = textEngr.getBBox();
    box = { x: bb.x - 6, y: bb.y - 8, w: bb.width + 12, h: bb.height + 16 };
    if (!bb.width) box = { x: it.cx - 40, y: it.cy - 30, w: 80, h: 60 };
  }

  /* ---------- sweep animation ---------- */
  function setProgress(p) {
    progress = p;
    var it = ITEMS[state.item];
    var x = box.x + box.w * p;
    var done = p >= 1;
    clipEngr.setAttribute('x', box.x); clipEngr.setAttribute('y', box.y - 4);
    clipEngr.setAttribute('width', done ? box.w + 12 : Math.max(0, box.w * p - 26)); clipEngr.setAttribute('height', box.h + 8);
    var gw = done ? 0 : Math.min(46, box.w * p);
    clipGlow.setAttribute('x', Math.max(box.x, x - gw)); clipGlow.setAttribute('y', box.y - 4);
    clipGlow.setAttribute('width', gw); clipGlow.setAttribute('height', box.h + 8);
    var live = p > 0 && p < 1;
    laser.style.opacity = live ? 1 : 0; spark.style.opacity = live ? 1 : 0;
    laser.setAttribute('x', x - 1.5); laser.setAttribute('y', box.y - 6); laser.setAttribute('height', box.h + 12);
    spark.setAttribute('cx', x);
    spark.setAttribute('cy', box.y + box.h / 2 + Math.sin(p * 46) * (box.h / 2 - 4));
    spark.setAttribute('fill', it.glow);
  }
  function ease(t) { return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
  function play() {
    cancelAnimationFrame(raf);
    layoutText();
    if (reduce) { setProgress(1); return; }
    var chars = (in1.value + in2.value).length;
    var dur = Math.min(3200, 1300 + chars * 55), t0 = null;
    setProgress(0);
    (function step(ts) {
      if (t0 === null) t0 = ts;
      var t = Math.min(1, (ts - t0) / dur);
      setProgress(ease(t));
      if (t < 1) raf = requestAnimationFrame(step);
    })(performance.now());
  }
  function showNow() { cancelAnimationFrame(raf); layoutText(); setProgress(1); }

  /* ---------- controls ---------- */
  var debounce = null;
  function onType() { showNow(); clearTimeout(debounce); debounce = setTimeout(play, 650); }
  in1.addEventListener('input', onType); in2.addEventListener('input', onType);

  function bindSeg(attr, key) {
    var btns = document.querySelectorAll('.seg button[' + attr + ']');
    btns.forEach(function (b) {
      b.addEventListener('click', function () {
        btns.forEach(function (x) { x.classList.remove('on'); });
        b.classList.add('on');
        state[key] = b.getAttribute(attr);
        if (key === 'item') drawItem();
        play();
      });
    });
  }
  bindSeg('data-item', 'item'); bindSeg('data-font', 'font');
  $('d-replay').addEventListener('click', play);

  /* hand the design to the quote form */
  $('d-quote').addEventListener('click', function () {
    var it = ITEMS[state.item];
    var msg = 'Engraving preview: ' + it.label + ', "' + (in1.value || '').trim() + '"' +
      ((in2.value || '').trim() ? ' / "' + in2.value.trim() + '"' : '') + ', ' + state.font + ' style.';
    var d = document.getElementById('f-details'), t = document.getElementById('f-type');
    if (d && d.value.indexOf('Engraving preview:') !== 0) d.value = msg + (d.value ? '\n' + d.value : '');
    else if (d) d.value = d.value.replace(/^Engraving preview:.*$/m, msg);
    if (t) t.value = it.quoteType;
  });

  /* debug/verification hook: ?engrave=0.5 freezes the sweep at that progress */
  var m = /[?&]engrave=([\d.]+)/.exec(location.search);
  var mi = /[?&]item=(tumbler|board|crystal)/.exec(location.search);
  var mf = /[?&]font=(script|serif|bold)/.exec(location.search);
  if (mi) { state.item = mi[1]; document.querySelectorAll('.seg button[data-item]').forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-item') === state.item); }); }
  if (mf) { state.font = mf[1]; document.querySelectorAll('.seg button[data-font]').forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-font') === state.font); }); }

  function boot() {
    drawItem(); layoutText();
    if (m) { setProgress(parseFloat(m[1])); return; }
    setProgress(1);
    /* first time it scrolls into view, engrave it */
    var seen = false;
    new IntersectionObserver(function (es, o) {
      es.forEach(function (e) { if (e.isIntersecting && !seen) { seen = true; play(); o.disconnect(); } });
    }, { threshold: 0.45 }).observe(svg);
  }
  var f = document.fonts && document.fonts.load ? Promise.all([
    document.fonts.load('80px "Great Vibes"'), document.fonts.load('800 40px "Bricolage Grotesque"')
  ]).catch(function () {}) : Promise.resolve();
  f.then(function () { document.fonts.ready.then(boot); });
})();
