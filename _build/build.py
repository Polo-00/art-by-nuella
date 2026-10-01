# -*- coding: utf-8 -*-
"""Builds every page of the Art by Nuella site from shared parts.
Run:  python _build/build.py   (from the project folder). Outputs *.html next to styles.css."""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PHONE = "+1 (587) 664-7416"
TEL = "+15876647416"
EMAIL = "artbynuella@gmail.com"
IG_URL = "https://www.instagram.com/artbynuella/"
GOOGLE_URL = "https://share.google/pqAPcqJjy4SCjmEKZ"
AREAS = "Calgary · Chestermere · Airdrie"

NAV = [
    ("events.html", "Events"),
    ("gifts.html", "Gifts &amp; Baskets"),
    ("apparel.html", "Apparel &amp; Merch"),
    ("engraving.html", "Engraving"),
    ("crystals.html", "Crystals &amp; Awards"),
    ("business.html", "Business"),
]

# Real Google reviews (verbatim), from the new and the older Google profiles.
# Names shortened to first name + initial. Owner-family and joke/irrelevant reviews are intentionally left out.
R = {
  "ehi": ("I particularly enjoyed working with ArtbyNuella. Her level of professionalism is top notch. I enjoyed how she carried me along in the various projects she did for me, her timeliness to deliver and prices are very fair and unbeatable. Her work is so neat and impeccable. Thumbs up. I will always recommend her to anyone in Calgary, Canada.", "Ehi E."),
  "joshua": ("It was a well thought out gift set. Thanks", "Joshua E."),
  "sherese": ("We got coasters and a business t-shirt made and Emma did an AMAZING job each time! Looking forward to getting more. Thank you Emma", "Sherese M."),
  "mayowa": ("Art by Nuella gave me some nice designs. My Tshirts were totally transformed. Service delivery was top notch and I was given lots of design to pick from. Can't wait to start rocking my Tshirts!!! Great job!!", "Mayowa J."),
  "stephanie": ("Absolutely love my shirts. Beautiful work and the quality is amazing. The woman who did mine is a very sweet, understanding lady. I highly recommend her.", "Stephanie B."),
  "paul": ("Emma takes the time to explain and offer several options to choose from. I recommend her services for anyone looking for quality, on budget and a timely delivery job.", "Paul T."),
  "ihuoma": ("I had a beautiful experience with my print job. She came through on time and everyone loved their shirts I'll definitely be a repeat customer.", "Ihuoma O."),
  "odunayo": ("Very wonderful customer service I got. Told her what I wanted and she understood the assignment. My daughter's teacher whom I made the gift item for loved it.", "Odunayo A."),
  "amanda": ("Order two shirts, they turned out better then expected and she did them in a pinch! Would definitely order again!", "Amanda P."),
  "festus": ("Excellent artwork and commendable piece of art mastery. Very satisfied customer", "Festus O."),
  "ose": ("Exceptional personalized gift items and great customer service.", "Ose W."),
}
PAGE_REVIEWS = {
  "home": ["ehi", "odunayo", "sherese", "amanda", "mayowa", "joshua", "paul", "stephanie", "ose", "ihuoma", "festus"],
  "events": ["amanda", "ihuoma", "joshua", "ehi"],
  "gifts": ["odunayo", "joshua", "ose", "sherese"],
  "apparel": ["mayowa", "stephanie", "ihuoma", "amanda"],
  "engraving": ["ehi", "festus", "paul"],
  "crystals": ["festus", "ehi", "paul"],
  "business": ["sherese", "ehi", "paul"],
}


def head(title, desc, extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="images/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;600;700;800&family=Work+Sans:wght@400;500;600;700&family=Great+Vibes&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
{extra}</head>
<body>
"""


def header(active):
    links = ""
    for href, label in NAV:
        cls = ' class="active"' if href == active else ""
        links += f'<a href="{href}"{cls}>{label}</a>'
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">
      <img src="images/logo.png" alt="Art by Nuella logo">
      <div><div class="brand-name">ART BY NUELLA</div><div class="brand-tag">Personalized gifts crafted with love</div></div>
    </a>
    <nav class="main-nav">{links}<a class="nav-quote" href="#quote">Get a Quote</a></nav>
    <a class="btn btn-accent header-cta" href="tel:{TEL}">Call now</a>
    <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</header>
"""


def reviews(page="home", tint=True):
    keys = PAGE_REVIEWS.get(page, PAGE_REVIEWS["home"])

    def card(k, reveal):
        cls = "quote reveal" if reveal else "quote"
        return f'<div class="{cls}"><div class="stars">★★★★★</div><p>{html.escape(R[k][0])}</p><div class="who">{R[k][1]} <span>· Google review</span></div></div>'

    if page == "home":
        strip = "".join(card(k, False) for k in keys)
        extra = f'<div class="rev-marquee" aria-label="Customer reviews"><div class="rev-track">{strip}<div class="rev-dup" aria-hidden="true">{strip}</div></div></div>'
        inner = ""
    else:
        extra = ""
        inner = '<div class="quotes">' + "".join(card(k, True) for k in keys) + "</div>"
    return f"""<section class="{'tint' if tint else ''}" id="reviews">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow">Kind words</div>
      <h2>What customers are saying.</h2>
    </div>
    <div class="rating-row reveal">
      <div class="rating-big"><span class="num">5.0</span><div><span class="stars">★★★★★</span><small>Rated on Google</small></div></div>
      <a class="btn btn-outline" href="{GOOGLE_URL}" target="_blank" rel="noopener">Read our Google reviews</a>
    </div>
    {inner}
  </div>
  {extra}
</section>
"""


PROJECT_TYPES = [
    "Event favours or gifts", "Wedding", "Birthday party", "Baby or bridal shower", "Graduation",
    "Corporate or team event", "Gift basket", "Custom apparel", "Engraved cup or bottle",
    "Chopping board", "Notebook or journal", "Photo crystal", "Plaque or award", "Something else",
]


def quote_section(default=None, heading="Tell us what you want made.", sub="Send the item, the name or design, the timing and the story behind it. We will get back to you with a quote."):
    opts = "".join(f'<option{" selected" if p == default else ""}>{p}</option>' for p in PROJECT_TYPES)
    return f"""<section class="fast" id="quote-info">
  <div class="wrap">
    <h2>Fastest way to start</h2>
    <p>Call, email or send a quick request. No cart, just talk to a maker.</p>
    <div class="fast-grid">
      <div><div class="label">Phone</div><div class="value"><a href="tel:{TEL}">{PHONE}</a></div></div>
      <div><div class="label">Email</div><div class="value"><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
      <div><div class="label">Instagram</div><div class="value"><a href="{IG_URL}" target="_blank" rel="noopener">@artbynuella</a></div></div>
      <div><div class="label">Serving</div><div class="value">{AREAS}</div></div>
    </div>
  </div>
</section>
<section id="quote">
  <div class="wrap">
    <div class="quote-wrap">
      <h2>Request a custom quote</h2>
      <p>{sub}</p>
      <form class="quote-form">
        <div class="form-row">
          <div><label for="f-name">Name</label><input id="f-name" name="name" type="text" required></div>
          <div><label for="f-contact">Phone or email</label><input id="f-contact" name="contact" type="text" required></div>
        </div>
        <div class="form-row">
          <div><label for="f-city">City</label><input id="f-city" name="city" type="text" placeholder="Calgary, Chestermere, Airdrie..."></div>
          <div><label for="f-when">Timeline or event date</label><input id="f-when" name="when" type="text" placeholder="e.g. Nov 15, or 'in 2 weeks'"></div>
        </div>
        <div class="form-full"><label for="f-type">Project type</label><select id="f-type" name="type">{opts}</select></div>
        <div class="form-full"><label for="f-details">Project details</label><textarea id="f-details" name="details" placeholder="What is it for, how many, names or wording, colours or theme, photo or logo..."></textarea></div>
        <div style="position:absolute;left:-9999px" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
        <button class="btn btn-accent" type="submit">Send request</button>
        <div class="form-error" role="alert"></div>
        <div class="form-note">Prefer to talk? Call {PHONE} or message @artbynuella on Instagram.</div>
      </form>
      <div class="form-success"><h3>Thank you!</h3><p>We got your request and will be in touch soon. For the fastest reply, call {PHONE}.</p></div>
    </div>
  </div>
</section>
"""


def engrave_demo():
    return """<section class="tint" id="try-it"><div class="wrap">
  <div class="section-head reveal"><div class="eyebrow">Try it</div><h2>See your name engraved.</h2><p>Type a name or a date, pick a piece and a style, and watch it come to life. This is a preview, and we always confirm the final design with you before anything is made.</p></div>
  <div class="demo reveal">
    <div class="demo-controls">
      <label>Pick a piece</label>
      <div class="seg"><button type="button" data-item="tumbler" class="on">Tumbler</button><button type="button" data-item="board">Cutting board</button><button type="button" data-item="crystal">Crystal</button></div>
      <label for="d-line1" style="margin-top:18px">Name or main text</label>
      <input id="d-line1" maxlength="22" value="The Johnsons" autocomplete="off">
      <label for="d-line2" style="margin-top:14px">Date or short message <span style="font-weight:400;color:var(--muted-fg)">(optional)</span></label>
      <input id="d-line2" maxlength="30" value="Est. 2024" autocomplete="off">
      <label style="margin-top:18px">Style</label>
      <div class="seg"><button type="button" data-font="script" class="on">Script</button><button type="button" data-font="serif">Classic</button><button type="button" data-font="bold">Bold</button></div>
      <div class="demo-actions"><button type="button" class="btn btn-outline" id="d-replay">↻ Replay</button><a class="btn btn-accent" href="#quote" id="d-quote">Get a quote for this</a></div>
    </div>
    <div class="demo-stage">
      <svg id="d-svg" viewBox="0 0 420 460" role="img" aria-label="Live engraving preview">
        <defs>
          <linearGradient id="g-tumbler" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#e3d5bc"/><stop offset=".5" stop-color="#fbf3e5"/><stop offset="1" stop-color="#d9c8ab"/></linearGradient>
          <linearGradient id="g-board" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#bb7a40"/><stop offset=".55" stop-color="#9c6130"/><stop offset="1" stop-color="#7c4a22"/></linearGradient>
          <linearGradient id="g-crystal" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2f271e"/><stop offset="1" stop-color="#15100b"/></linearGradient>
          <linearGradient id="g-laser" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#ffb36b" stop-opacity="0"/><stop offset=".5" stop-color="#fff2dc"/><stop offset="1" stop-color="#ffb36b" stop-opacity="0"/></linearGradient>
          <filter id="f-blur" x="-30%" y="-200%" width="160%" height="500%"><feGaussianBlur stdDeviation="6"/></filter>
          <filter id="f-glow" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="2.6"/></filter>
          <clipPath id="d-clipp-engr"><rect id="d-clip-engr" x="0" y="0" width="0" height="0"/></clipPath>
          <clipPath id="d-clipp-glow"><rect id="d-clip-glow" x="0" y="0" width="0" height="0"/></clipPath>
        </defs>
        <g id="d-item"></g>
        <g clip-path="url(#d-clipp-engr)"><g id="d-text-engr"></g></g>
        <g clip-path="url(#d-clipp-glow)" filter="url(#f-glow)"><g id="d-text-glow"></g></g>
        <rect id="d-laser" width="3" x="0" y="0" height="0" rx="1.5" fill="url(#g-laser)" style="opacity:0"/>
        <circle id="d-spark" r="4.5" cx="0" cy="0" fill="#ff9a4d" filter="url(#f-glow)" style="opacity:0"/>
      </svg>
    </div>
  </div>
</div></section>
<script src="engrave.js" defer></script>
"""


def footer():
    ln = "".join(f'<a href="{h}">{l}</a>' for h, l in NAV)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div><div class="brand" style="margin-bottom:12px"><img src="images/logo.png" alt=""><div class="brand-name">ART BY NUELLA</div></div>
        <p>Personalized gifts crafted with love. Family-owned and operated, made locally for {AREAS.replace(' · ', ', ')}.</p></div>
      <div><h5>Explore</h5>{ln}</div>
      <div><h5>Contact</h5><a href="tel:{TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{IG_URL}" target="_blank" rel="noopener">Instagram @artbynuella</a><a href="{GOOGLE_URL}" target="_blank" rel="noopener">Google reviews</a></div>
      <div><h5>Serving</h5><p>Calgary<br>Chestermere<br>Airdrie<br>and nearby areas</p></div>
    </div>
    <div class="foot-base">© <span id="year">2026</span> Art by Nuella · Calgary, Chestermere &amp; Airdrie</div>
  </div>
</footer>
<div class="call-bar"><a class="btn btn-accent" href="tel:{TEL}">Call now</a><a class="btn btn-outline" href="#quote">Get a quote</a></div>
<script src="app.js"></script>
</body>
</html>
"""


def hero(active_crumb, h1, lead, img, cap_title, cap_sub, alt, badge=None, home=False):
    crumb = "" if home else f'<div class="crumbs"><a href="index.html">Home</a> / {active_crumb}</div>'
    bd = f'<div class="badge">{badge}</div>' if badge else ""
    cls = "hero" if home else "hero page-hero"
    return f"""<section class="{cls}" style="padding-bottom:40px">
  <div class="wrap hero-grid">
    <div>
      {crumb}{bd}
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <div class="hero-ctas">
        <a class="btn btn-accent" href="tel:{TEL}">📞 {PHONE}</a>
        <a class="btn btn-outline" href="#quote">Request a quote</a>
      </div>
    </div>
    <div class="hero-media">
      <img src="images/{img}" alt="{alt}">
      <div class="hero-caption"><strong>{cap_title}</strong><span>{cap_sub}</span></div>
    </div>
  </div>
</section>
"""


def pg(img, title, sub="", concept=False, alt=None):
    tag = '<span class="pg-tag">Concept</span>' if concept else ""
    s = f"<small>{sub}</small>" if sub else ""
    return f'<a class="pg-item" href="images/{img}" data-full="images/{img}">{tag}<img src="images/{img}" alt="{alt or title}" loading="lazy"><div class="pg-cap">{title}{s}</div></a>'


def gallery(items, note=True, eyebrow="Recent work", h2="Real pieces, made here.", sub="Tap any photo to see it larger."):
    n = ('<p class="gallery-note">Photos marked <b>Concept</b> are design samples of what we can make for you. Everything else is real work.</p>'
         if note and any("Concept" in i for i in items) else "")
    return f"""<section id="gallery">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">{eyebrow}</div><h2>{h2}</h2><p>{sub}</p></div>
    <div class="page-gallery">{"".join(items)}</div>
    {n}
  </div>
</section>
"""


def detail_grid(items, eyebrow, h2, sub="", tint=False):
    d = "".join(f'<div class="detail reveal"><div class="ck">✓</div><div><h4>{t}</h4><p>{p}</p></div></div>' for t, p in items)
    s = f"<p>{sub}</p>" if sub else ""
    return f"""<section class="{'tint' if tint else ''}">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">{eyebrow}</div><h2>{h2}</h2>{s}</div>
    <div class="detail-grid">{d}</div>
  </div>
</section>
"""


def make_grid(items, eyebrow, h2, sub="", tint=False):
    d = "".join(f'<div class="make-card reveal"><div class="ico">{i}</div><h3>{t}</h3><p>{p}</p></div>' for i, t, p in items)
    s = f"<p>{sub}</p>" if sub else ""
    return f"""<section class="{'tint' if tint else ''}">
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">{eyebrow}</div><h2>{h2}</h2>{s}</div>
    <div class="make-grid">{d}</div>
  </div>
</section>
"""


def steps(items, h2="How it works."):
    d = "".join(f'<div class="step reveal"><div class="n">{i+1:02d}</div><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(items))
    return f"""<section>
  <div class="wrap">
    <div class="section-head reveal"><div class="eyebrow">The process</div><h2>{h2}</h2></div>
    <div class="steps">{d}</div>
  </div>
</section>
"""


STD_STEPS = [
    ("Send the details", "Tell us the item, the name or design, the timing and the story behind it. A phone call, an email or the form all work."),
    ("We confirm the design", "We come back with the design, the details and a quote so you know exactly what you are getting."),
    ("We make it and wrap it", "Your piece is made locally, checked, and ready to give. One-offs and bigger orders are both welcome."),
]


def cta_band(text, sub=""):
    s = f"<p>{sub}</p>" if sub else ""
    return f"""<section style="padding-top:0"><div class="wrap"><div class="cta-band reveal">
  <div><h2>{text}</h2>{s}</div>
  <div class="hero-ctas"><a class="btn btn-dark" href="tel:{TEL}" style="background:#16100a;color:#fefaf1">📞 Call {PHONE}</a><a class="btn btn-outline" href="#quote" style="border-color:#16100a">Request a quote</a></div>
</div></div></section>
"""


def write(name, content):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name, len(content) // 1024, "KB")


# =========================================================== HOME
def page_home():
    ld = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"Art by Nuella","description":"Personalized gifts, custom apparel, engraving, 3D crystals, gift baskets and event favours.","telephone":"+15876647416","email":"artbynuella@gmail.com","areaServed":["Calgary","Chestermere","Airdrie"],"sameAs":["https://www.instagram.com/artbynuella/"]}</script>
"""
    p = head("Art by Nuella | Custom Gifts, Apparel, Engraving & Event Favours in Calgary",
             "Personalized gifts, custom apparel, engraving, 3D crystals, gift baskets and event favours for weddings, birthdays, showers, teams and businesses. Made locally in Calgary, Chestermere and Airdrie.", ld)
    p += header("")
    p += hero("", "Custom gifts that feel personal before they are opened.",
              "Personalized gifts, custom apparel, engraved drinkware, gift baskets, crystals and event favours, designed and made locally. For birthdays, weddings, showers, teachers, teams and businesses.",
              "merch-set.jpg", "Gift shop · print shop · engraving shop",
              "Made for birthdays, weddings, teachers, teams, businesses and keepsakes.",
              "A full Art by Nuella product spread with printed apparel, drinkware, notebooks, tote bags and mugs",
              badge=f"📍 {AREAS}", home=True)
    p += f"""<div class="trust"><div class="wrap">
  <div class="item"><h4><span class="stars">★★★★★</span></h4><span>Rated on Google</span></div>
  <div class="item"><h4>Local</h4><span>Calgary made</span></div>
  <div class="item"><h4>Custom</h4><span>One-offs welcome</span></div>
  <div class="item"><h4>Family-owned</h4><span>Crafted with love</span></div>
</div></div>
"""
    cats = [
        ("events.html", "event-birthday.jpg", "Events", "Weddings, birthdays, showers, graduations, reunions and company events. Favours, gifts and matching pieces made to your date and theme."),
        ("gifts.html", "gift-basket.jpg", "Gifts &amp; Baskets", "Curated gift baskets, teacher gifts, keepsakes and one-off custom orders, wrapped and ready to give."),
        ("apparel.html", "tee-desert.jpg", "Apparel &amp; Merch", "T-shirts, sweatshirts, robes, towels, tote bags, mugs and branded merch for families, crews, events and businesses."),
        ("engraving.html", "engraved-board.jpg", "Engraving", "Wood boards, tumblers, bottles, glassware and journals engraved with names, dates, artwork and logos."),
        ("crystals.html", "crystal-plaque.jpg", "Crystals &amp; Awards", "Photos and designs laser-engraved inside 3D crystal, plus custom plaques and awards."),
        ("business.html", "branded-tumblers.jpg", "Business &amp; Corporate", "Branded drinkware, corporate gifts, staff apparel, event swag and recognition awards."),
    ]
    cards = "".join(
        f'<a class="cat-card reveal" href="{h}"><div class="cat-img"><img src="images/{i}" alt="{t}" loading="lazy"></div><div class="cat-body"><h3>{t}</h3><p>{d}</p><span class="more">Explore</span></div></a>'
        for h, i, t, d in cats)
    p += f"""<section id="services"><div class="wrap">
  <div class="section-head reveal"><div class="eyebrow">What we make</div><h2>Designed, printed, engraved, wrapped and ready to gift.</h2><p>More than engraving. Pick a category to see real pieces, or just tell us what you have in mind.</p></div>
  <div class="cat-grid">{cards}</div>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="event-band reveal">
  <div>
    <div class="eyebrow" style="color:#e67a30">Events</div>
    <h2>Celebrating something? We do events.</h2>
    <p>Weddings, birthdays, baby and bridal showers, graduations, reunions and company events. Favours, gifts for the whole crew, matching apparel and keepsakes, made to your date and your theme.</p>
    <div class="chips" style="margin-bottom:24px"><span class="chip">Weddings</span><span class="chip">Birthdays</span><span class="chip">Baby showers</span><span class="chip">Bridal showers</span><span class="chip">Graduations</span><span class="chip">Reunions</span><span class="chip">Corporate events</span><span class="chip">Memorials</span></div>
    <a class="btn btn-accent" href="events.html">Plan your event</a>
  </div>
  <div class="imgs"><img src="images/event-bridal-party.jpg" alt="Bridal party gift box with personalized tumbler and tote" loading="lazy"><img src="images/event-birthday.jpg" alt="Birthday party favours and custom bottles" loading="lazy"></div>
</div></div></section>
"""
    p += engrave_demo()
    tiles = [
        ("apparel.html", "merch-set.jpg", "Custom merch sets"), ("gifts.html", "gift-basket.jpg", "Gift baskets"),
        ("engraving.html", "engraved-board.jpg", "Wood engraving"), ("engraving.html", "bottles.jpg", "Cups &amp; bottles"),
        ("gifts.html", "teacher-gift.jpg", "Teacher gifts"), ("apparel.html", "ig-robes.jpg", "Robes &amp; towels"),
        ("crystals.html", "couple-rose.jpg", "Photo crystals"), ("business.html", "branded-tumblers.jpg", "Engraved tumblers"),
        ("apparel.html", "tee-desert.jpg", "Custom tees"), ("apparel.html", "tote-desert.jpg", "Printed totes"),
        ("events.html", "ig-70th-tumblers.jpg", "Event tumblers"), ("crystals.html", "crystal-plaque.jpg", "Crystal plaques"),
    ]
    tl = "".join(f'<a class="pg-item g-link" href="{h}"><img src="images/{i}" alt="{t}" loading="lazy"><div class="pg-cap">{t}</div></a>' for h, i, t in tiles)
    p += f"""<section class="tint" id="gallery"><div class="wrap">
  <div class="section-head reveal"><div class="eyebrow">Recent work</div><h2>A gallery built to spark your order.</h2><p>Start with an idea. Tap a photo to see more from that category.</p></div>
  <div class="gallery-grid">{tl}</div>
</div></section>
"""
    p += reviews("home", tint=False)
    p += """<section style="padding-top:0"><div class="wrap"><div class="about reveal">
  <img src="images/logo.png" alt="Art by Nuella logo">
  <div>
    <div class="eyebrow">Meet the maker</div>
    <h2>Family-owned, and personal from the first message.</h2>
    <p>Art by Nuella is a family-owned small business in Calgary, run by Emmanuella, or Emma to her customers. She listens to what you need, offers a few options to choose from, and makes it with care, whether it is one special gift or a table full of favours.</p>
    <div class="hero-ctas" style="margin-top:22px"><a class="btn btn-accent" href="tel:""" + TEL + """">Talk to Emma</a><a class="btn btn-outline" href="#quote">Request a quote</a></div>
  </div>
</div></div></section>
"""
    p += steps(STD_STEPS, "From idea to gift in three steps.")
    p += quote_section()
    p += footer()
    write("index.html", p)


# =========================================================== EVENTS
def page_events():
    p = head("Event Favours, Gifts & Custom Merch | Weddings, Birthdays & More | Art by Nuella",
             "Custom favours, gifts, matching apparel and keepsakes for weddings, birthdays, baby and bridal showers, graduations, reunions and company events in Calgary, Chestermere and Airdrie.")
    p += header("events.html")
    p += hero("Events", "Gifts and keepsakes for every celebration.",
              "Weddings, birthdays, showers, graduations, reunions and company events. We design and make the favours, gifts and matching pieces so your event feels like yours.",
              "event-wedding.jpg", "Made to your date and your theme",
              "One maker for favours, apparel, drinkware, baskets and keepsakes.",
              "Wedding reception table with warm terracotta styling", badge="🎉 Events")
    tiles = [
        ("event-wedding.jpg", "Weddings", "Guest favours, bridal party and groomsmen gifts, engraved keepsakes and welcome gifts."),
        ("ig-70th-tumblers.jpg", "Birthdays &amp; milestones", "Party favours, custom cups and bottles, and matching pieces, like these 70th birthday tumblers."),
        ("event-baby-shower.jpg", "Baby &amp; bridal showers", "Keepsakes, favours, engraved gifts and photo crystals for the guest of honour."),
        ("event-graduation.jpg", "Graduations", "Engraved journals, crystal plaques and custom apparel for the grad."),
        ("event-family-reunion.jpg", "Family reunions", "Matching tees, totes and bottles so the whole family wears it together."),
        ("event-corporate.jpg", "Corporate &amp; team events", "Branded welcome kits, drinkware, apparel and recognition awards."),
        ("event-memorial.jpg", "Memorials &amp; anniversaries", "Photo crystals and engraved keepsakes for the moments worth remembering."),
        ("teacher-gift.jpg", "Teacher &amp; community thanks", "Thank-you gifts for teachers, coaches, volunteers and church or community groups."),
    ]
    tl = "".join(f'<div class="event-tile reveal"><img src="images/{i}" alt="{t}" loading="lazy"><div class="ov"><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in tiles)
    p += f"""<section><div class="wrap">
  <div class="section-head reveal"><div class="eyebrow">Events we cater to</div><h2>If it is worth celebrating, we can make something for it.</h2><p>Do not see your event? Ask. Most of what we make is custom, so we can build around almost any occasion. Event photos on this page are design concepts.</p></div>
  <div class="event-grid">{tl}</div>
</div></section>
"""
    p += make_grid([
        ("🎁", "Party favours &amp; guest keepsakes", "Small personalized gifts for every guest, made in the quantity your event needs."),
        ("💍", "Bridal party &amp; groomsmen gifts", "Engraved drinkware, printed totes, notebooks and gift boxes for your favourite people."),
        ("👕", "Matching apparel for the crew", "T-shirts, sweatshirts and totes in one design for the family, the party or the team."),
        ("🥂", "Custom cups, bottles &amp; glassware", "Names, dates and artwork engraved on cups, tumblers, bottles and glasses."),
        ("🧺", "Gift baskets &amp; welcome bags", "Curated baskets and welcome gifts wrapped and ready to hand out."),
        ("💎", "Crystals, plaques &amp; awards", "Photo crystals for the guest of honour and custom plaques and awards for recognition moments."),
        ("🛁", "Robes, towels &amp; linens", "Monogrammed robes and towels for the bridal party, guests and hosts."),
        ("🚩", "Banners &amp; tablecloths", "Printed banners and table covers for cultural, community and club events."),
        ("🪵", "Serving boards &amp; wood keepsakes", "Engraved boards and wood pieces for hosts, couples and families."),
    ], "What we make for events", "Everything for the day, from one maker.", tint=True)
    p += gallery([
        pg("ig-70th-tumblers.jpg", "70th birthday tumblers", "A matching set for the whole party"),
        pg("engraved-board.jpg", "Engraved wedding &amp; housewarming boards", "Names, dates and even the house itself"),
        pg("ig-robes.jpg", "Monogrammed robes", "Bridal party, guests and hosts"),
        pg("celebration-basket.jpg", "Celebration gift baskets"),
        pg("bottles.jpg", "Custom bottles", "Gold foil design, made in a set"),
        pg("couple-rose.jpg", "Anniversary photo crystals"),
        pg("gift-basket.jpg", "Curated gift baskets"),
        pg("ig-team-tumblers.jpg", "Team &amp; event tumblers"),
        pg("teacher-gift.jpg", "Teacher appreciation gifts"),
        pg("merch-set.jpg", "Matching merch sets", "Apparel, totes, mugs and notebooks in one design"),
        pg("couple-christmas.jpg", "Holiday keepsake crystals"),
        pg("notebooks.jpg", "Journals for the whole party"),
    ], h2="Real gifts made for real celebrations.", eyebrow="Real work", note=False)
    p += detail_grid([
        ("One maker for all of it", "Gifts, apparel, engraving and crystals under one roof, so everything matches."),
        ("Matched sets", "Use the same design across favours, tees, cups and totes so the whole event ties together."),
        ("Your theme and colours", "Tell us the colours, the names and the date. We build around your event."),
        ("Names, dates and photos", "Engrave, print or embed the details that make it personal."),
        ("One-offs and bigger orders", "One special gift or a table full of favours, both are welcome."),
        ("Local and easy to reach", f"Serving {AREAS.replace(' · ', ', ')}. Call, text or message any time."),
    ], "Why it works", "Planning made easier.")
    p += steps([
        ("Tell us the event and the date", "Share what you are celebrating, when it is, and roughly how many people. Earlier is easier."),
        ("Pick the pieces and the theme", "We suggest ideas that fit, then confirm the design and a quote before anything is made."),
        ("We make it and wrap it", "Your favours, gifts and apparel are made locally and ready ahead of your date."),
    ], "Plan your event in three steps.")
    p += reviews("events")
    p += quote_section(default="Event favours or gifts", heading="Plan your event", sub="Tell us the event, the date and roughly how many. We will get back to you with ideas and a quote.")
    p += footer()
    write("events.html", p)


# =========================================================== GIFTS
def page_gifts():
    p = head("Personalized Gifts & Gift Baskets in Calgary | Art by Nuella",
             "Curated gift baskets, teacher gifts, personalized keepsakes, journals and one-off custom gifts, made locally in Calgary, Chestermere and Airdrie.")
    p += header("gifts.html")
    p += hero("Gifts &amp; Baskets", "Personalized gifts, wrapped and ready to give.",
              "Curated gift baskets, teacher gifts, keepsakes, journals and one-off custom orders for birthdays, weddings, thank-yous and just because.",
              "gift-basket.jpg", "Gift baskets · teacher gifts · keepsakes",
              "Built around the person, the occasion and your budget.",
              "A wrapped Art by Nuella gift basket with a gold bow", badge="🎁 Gifts")
    p += gallery([
        pg("gift-basket.jpg", "Gift baskets", "Curated, wrapped and ready"),
        pg("teacher-gift.jpg", "Teacher gifts", "Personalized tumbler and treats"),
        pg("celebration-basket.jpg", "Celebration baskets"),
        pg("notebooks.jpg", "Journals &amp; planners", "Custom artwork on faux leather"),
        pg("bottles.jpg", "Custom bottles"),
        pg("leather-journal.jpg", "Leather journals"),
        pg("ig-robes.jpg", "Monogrammed robes", "A gift they will actually use"),
        pg("ig-towels.jpg", "Monogrammed towels"),
        pg("ig-mugs.jpg", "Custom mugs"),
        pg("engraved-bottle.jpg", "Engraved bottles", "A message and signature in the glass"),
        pg("slate-coasters.jpg", "Slate coaster sets", concept=True),
        pg("keychains.jpg", "Personalized keychains", concept=True),
        pg("wine-glass.jpg", "Etched glassware"),
    ], h2="Gifts we have made.")
    p += detail_grid([
        ("Birthdays", "Personalized cups, apparel, journals and baskets for every age."),
        ("Weddings &amp; anniversaries", "Engraved boards, photo crystals and gifts for the couple and the wedding party."),
        ("Teacher appreciation", "Thank-you gifts and baskets for teachers, coaches and caregivers."),
        ("New homes", "Engraved boards with the family name, a house portrait or the address."),
        ("Holidays &amp; Christmas", "Matching apparel, mugs, baskets and keepsakes for the season."),
        ("Thank-yous &amp; corporate", "Client and staff gifts, wrapped and branded."),
    ], "Gift ideas", "Something for every occasion.", tint=True)
    p += steps(STD_STEPS, "Simple from start to finish.")
    p += reviews("gifts", tint=True)
    p += quote_section(default="Gift basket")
    p += footer()
    write("gifts.html", p)


# =========================================================== APPAREL
def page_apparel():
    p = head("Custom T-Shirts, Totes & Merch in Calgary | Art by Nuella",
             "Custom printed t-shirts, sweatshirts, tote bags, mugs and branded merch for families, events, teams and small businesses in Calgary, Chestermere and Airdrie.")
    p += header("apparel.html")
    p += hero("Apparel &amp; Merch", "Custom apparel and merch, printed your way.",
              "T-shirts, sweatshirts, tote bags, mugs and branded merch for families, crews, events and businesses. Bring the design or we will help you build one.",
              "tee-desert.jpg", "Print shop pieces",
              "Made for events, teams, businesses and everyday gifting.",
              "Custom printed black t-shirt with a desert sun design", badge="👕 Print shop")
    p += gallery([
        pg("merch-set.jpg", "Custom merch sets", "Sweatshirt, tote, mug, bottle and notebook"),
        pg("tee-desert.jpg", "Custom tees"),
        pg("tote-desert.jpg", "Printed totes"),
        pg("ig-robes.jpg", "Monogrammed robes"),
        pg("ig-towels.jpg", "Monogrammed towels"),
        pg("tshirt-monogram.jpg", "Monogram crest tees", concept=True),
        pg("tshirt-logo.jpg", "Business logo tees", concept=True),
        pg("event-family-reunion.jpg", "Family reunion sets", concept=True),
        pg("notebooks.jpg", "Matching notebooks"),
        pg("bottles.jpg", "Matching bottles"),
    ], h2="Made to be worn and used.")
    p += make_grid([
        ("👕", "T-shirts &amp; sweatshirts", "Custom designs, names, photos and logos on comfortable everyday apparel."),
        ("🛍️", "Tote bags", "Printed totes for gifts, events, bridal parties and brands."),
        ("☕", "Mugs &amp; drinkware", "Personalized mugs and bottles that match the rest of your set."),
        ("👨‍👩‍👧", "Family &amp; group matching sets", "One design for the whole family, party or reunion."),
        ("🏢", "Business &amp; team apparel", "Logo apparel for small businesses, realtors, teams and organizations."),
        ("🎄", "Holiday apparel", "Christmas and seasonal designs for family photos and gifting."),
        ("🛁", "Robes &amp; towels", "Monogrammed bathrobes and towels for hotels, guest houses, weddings and gifts."),
        ("🚩", "Banners &amp; tablecloths", "Printed banners and table covers for events, clubs and community groups."),
    ], "What we print", "More than a t-shirt.", tint=True)
    p += steps([
        ("Share your design or idea", "Send a logo, artwork, a photo or just a concept. We can help shape it."),
        ("We confirm the details", "Sizes, colours, quantities and a quote, agreed before we print."),
        ("We print and pack it", "Made locally and packed ready to hand out or wear."),
    ], "From design to doorstep-ready.")
    p += reviews("apparel", tint=True)
    p += quote_section(default="Custom apparel")
    p += footer()
    write("apparel.html", p)


# =========================================================== ENGRAVING
def page_engraving():
    p = head("Custom Engraving in Calgary | Cutting Boards, Tumblers & More | Art by Nuella",
             "Custom engraving on wood boards, tumblers, bottles, glassware and journals with names, dates, artwork and logos. Made locally in Calgary, Chestermere and Airdrie.")
    p += header("engraving.html")
    p += hero("Engraving", "Engraved to be kept.",
              "Wood boards, tumblers, bottles, glassware and journals, engraved with names, dates, artwork and logos. It will not peel, fade or wash off.",
              "board-detail.jpg", "Engraving work",
              "Cups, chopping boards, notebooks, glass and wood pieces finished with personal detail.",
              "Walnut cutting board engraved with a detailed house illustration", badge="✍️ Engraving")
    p += engrave_demo()
    p += gallery([
        pg("engraved-board.jpg", "Engraved chopping boards", "Family names and the house itself"),
        pg("board-detail.jpg", "Engraving detail"),
        pg("branded-tumblers.jpg", "Engraved tumblers", "Custom names and logos, in bulk or one at a time"),
        pg("bottles.jpg", "Engraved bottles"),
        pg("yeti-tumbler.jpg", "Premium tumblers", "Deep, permanent engraving"),
        pg("ig-mugs.jpg", "Engraved mugs", "Logos and monograms"),
        pg("ig-team-tumblers.jpg", "Team tumblers"),
        pg("wine-glass.jpg", "Etched glassware"),
        pg("engraved-bottle.jpg", "Engraved bottles &amp; decanters"),
        pg("cutting-board.jpg", "Engraved boards with logos"),
        pg("leather-journal.jpg", "Leather journals"),
        pg("engraved-knife.jpg", "Engraved keepsakes"),
        pg("slate-coasters.jpg", "Slate coasters", concept=True),
        pg("keychains.jpg", "Wooden keychains", concept=True),
    ], h2="Detail that lasts.")
    p += make_grid([
        ("🪵", "Chopping boards", "Family names, recipes, wedding dates, addresses or a house portrait."),
        ("🥤", "Tumblers &amp; bottles", "Names, monograms and logos on insulated tumblers and water bottles."),
        ("🍷", "Glassware", "Wine glasses, decanters and bottles etched for gifts and events."),
        ("📓", "Notebooks &amp; journals", "Your name, artwork or logo on journals and planners."),
        ("🎁", "Wood keepsakes", "Keychains, coasters, plaques and small pieces for favours and gifts."),
        ("💎", "3D crystals", "Photos and designs engraved inside optical crystal."),
    ], "What we engrave", "If you can name it, we can make it personal.", tint=True)
    p += steps(STD_STEPS, "How engraving orders work.")
    p += reviews("engraving", tint=True)
    p += quote_section(default="Chopping board")
    p += footer()
    write("engraving.html", p)


# =========================================================== CRYSTALS
def page_crystals():
    p = head("3D Photo Crystals, Plaques & Awards in Calgary | Art by Nuella",
             "Photos and designs laser-engraved inside 3D crystal with optional LED bases, plus custom plaques and awards. Anniversaries, babies, memorials and corporate recognition in Calgary, Chestermere and Airdrie.")
    p += header("crystals.html")
    p += hero("Crystals &amp; Awards", "Your photo, held inside crystal.",
              "Photos, logos and artwork laser-engraved inside 3D crystal, with optional light-up bases. Perfect for milestones, memories and recognition.",
              "couple-rose.jpg", "3D photo crystals · plaques · awards",
              "Made from your own photo or design.",
              "A couple's photo engraved inside a crystal on an LED base", badge="💎 Crystals")
    p += gallery([
        pg("crystal-plaque.jpg", "Crystal plaque with LED base"),
        pg("ig-dog-crystal.jpg", "Pet portrait crystal", "Yes, pets too"),
        pg("couple-rose.jpg", "Anniversary portrait"),
        pg("baby-led.jpg", "Baby's first smile", "Glowing on a colour LED base"),
        pg("couple-christmas.jpg", "Holiday keepsake"),
        pg("couple-portrait2.jpg", "Engagement portrait"),
        pg("crystal-led.jpg", "Custom emblem crystal"),
        pg("award-pillar.jpg", "Corporate award", "Logo, event and recipient"),
        pg("medical-award.jpg", "Recognition award", "Custom emblem and message"),
        pg("church-award.jpg", "Appreciation plaque", "Full message of thanks"),
        pg("wood-awards.jpg", "Wood trophy sets"),
        pg("event-memorial.jpg", "Memorial keepsake", concept=True),
    ], h2="Made from real photos and real moments.")
    p += detail_grid([
        ("Anniversaries &amp; weddings", "Turn your favourite couple photo into a keepsake for the mantel."),
        ("New babies", "A first smile, held forever, and lovely for grandparents."),
        ("Memorials", "A gentle, lasting way to keep someone close."),
        ("Corporate &amp; team awards", "Logos, names and dates for milestones and recognition."),
        ("Retirements &amp; service", "Thank someone properly with a piece they will keep."),
        ("Church &amp; community", "Appreciation plaques with a full engraved message."),
    ], "Great for", "The moments worth keeping.", tint=True)
    p += detail_grid([
        ("Photos", "Portraits, couples, families, pets and babies, in black and white or colour tones."),
        ("Logos &amp; artwork", "Company marks, illustrations and custom designs."),
        ("Names, dates &amp; messages", "Add text for awards, plaques and keepsakes."),
        ("Light-up bases", "Optional LED bases make the image glow, including colour-changing options."),
        ("Different sizes", "Ask about the size that suits your photo and your space."),
        ("Gift ready", "Made to be given, and to be displayed."),
    ], "What goes inside", "Make it yours.")
    p += steps([
        ("Send your photo or design", "Share a clear photo, a logo or an idea, plus any names, dates or wording."),
        ("We confirm and quote", "We check the image and details with you and give you a quote before we start."),
        ("We engrave it", "Your crystal is engraved, checked and made ready to gift or display."),
    ], "How crystals work.")
    p += reviews("crystals", tint=True)
    p += quote_section(default="Photo crystal")
    p += footer()
    write("crystals.html", p)


# =========================================================== BUSINESS
def page_business():
    p = head("Corporate Gifts, Branded Merch & Awards in Calgary | Art by Nuella",
             "Branded drinkware, corporate gifts, staff apparel, event swag and recognition awards for businesses and organizations in Calgary, Chestermere and Airdrie.")
    p += header("business.html")
    p += hero("Business", "Branded gifts, merch and awards for your business.",
              "Engraved drinkware, corporate gifts, staff and event apparel, welcome kits, plaques and awards, made locally with your logo and your details.",
              "branded-tumblers.jpg", "Corporate gifts · branded merch · awards",
              "Bulk orders and one-off pieces, made to your brand.",
              "Rows of custom engraved and printed branded tumblers", badge="🏢 Business")
    p += gallery([
        pg("branded-tumblers.jpg", "Branded tumblers", "Company names and logos, made in quantity"),
        pg("ig-team-tumblers.jpg", "Team &amp; club tumblers"),
        pg("ig-mugs.jpg", "Branded mugs", "A logo on every cup"),
        pg("award-pillar.jpg", "Corporate award"),
        pg("event-corporate.jpg", "Welcome kits &amp; event swag", concept=True),
        pg("tshirt-logo.jpg", "Logo apparel", concept=True),
        pg("medical-award.jpg", "Recognition awards"),
        pg("merch-set.jpg", "Branded merch sets"),
        pg("notebooks.jpg", "Branded notebooks"),
        pg("tote-desert.jpg", "Printed tote bags"),
        pg("wood-awards.jpg", "Wood awards &amp; trophies"),
        pg("church-award.jpg", "Appreciation plaques"),
    ], h2="Your brand, on things people keep.")
    p += make_grid([
        ("🥤", "Branded drinkware", "Tumblers, bottles and mugs with your logo or the recipient's name."),
        ("🎁", "Corporate &amp; client gifts", "Curated, wrapped gifts to thank clients, partners and staff."),
        ("🏆", "Awards &amp; plaques", "Crystal and wood recognition pieces with your logo, names and dates."),
        ("👕", "Staff &amp; event apparel", "Logo tees and sweatshirts for teams, booths and events."),
        ("📦", "Event swag &amp; welcome kits", "Bundled gifts for conferences, onboarding and client events."),
        ("📓", "Notebooks &amp; totes", "Useful branded pieces that get used every day."),
    ], "What we make for business", "Made for teams, clients and events.", tint=True)
    p += steps([
        ("Send your logo and quantity", "Share your logo, what you would like made, how many, and when you need it."),
        ("We confirm and quote", "We prepare the design and a quote so you can approve before we produce."),
        ("We produce and hand over", "Everything is made locally and checked before it goes out."),
    ], "Simple for busy teams.")
    p += reviews("business")
    p += quote_section(default="Corporate or team event", sub="Send your logo, the item, how many and when. We will get back to you with a quote.")
    p += footer()
    write("business.html", p)


if __name__ == "__main__":
    page_home(); page_events(); page_gifts(); page_apparel(); page_engraving(); page_crystals(); page_business()
