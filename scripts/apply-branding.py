from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://aishwaryasreenivasan.site"
SUBTITLE = "Member of the Psychological Society of Ireland (PSI)"

# Keep the footer focused on copyright; PSI membership is already shown in the header.
FOOTER = (
    '<footer>'
    '<span>© 2026 Aishwarya Sreenivasan</span>'
    '</footer>'
)

LOCATION_SECTION = '''
<section class="section soft" id="locations" aria-labelledby="locations-title">
  <div class="section-inner">
    <div class="section-kicker">Ireland</div>
    <h2 id="locations-title">Psychological support in Ireland</h2>
    <p>
      Aishwarya Sreenivasan provides psychological assessment and therapy for young people and adults,
      alongside wellbeing solutions for organisations. This site is relevant to people looking for
      psychological support in Ireland, including Limerick, County Clare and Killaloe.
    </p>
    <div class="grid-3">
      <article class="card">
        <h3>Psychologist in Limerick</h3>
        <p>Information about psychological assessment, therapy and wellbeing support for people searching for a psychologist in Limerick.</p>
      </article>
      <article class="card">
        <h3>Psychologist in County Clare</h3>
        <p>Explore psychological support and evidence-based approaches for people searching for a psychologist in County Clare.</p>
      </article>
      <article class="card">
        <h3>Psychologist in Killaloe</h3>
        <p>Learn more about psychological support for people in and around Killaloe who are looking for a psychologist.</p>
      </article>
    </div>
  </div>
</section>
'''

SEO_SCHEMA = '''
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Aishwarya Sreenivasan",
  "jobTitle": "Psychologist",
  "url": "https://aishwaryasreenivasan.site/",
  "email": "mailto:aishwaryasriram2110@gmail.com",
  "sameAs": [
    "https://www.linkedin.com/in/aishwarya-sreenivasan-62686122/"
  ],
  "memberOf": {
    "@type": "Organization",
    "name": "Psychological Society of Ireland",
    "alternateName": "PSI"
  },
  "knowsAbout": [
    "Psychological assessment",
    "Psychological therapy",
    "Psychological wellbeing",
    "Workplace wellbeing"
  ]
}
</script>
'''

BRANDING_CSS = '''
    footer{display:flex;flex-direction:row;align-items:center;justify-content:space-between;gap:30px;padding:35px 8%;}
    .psi-membership{display:inline-flex;align-items:center;gap:12px;white-space:nowrap;}
    .psi-mark{width:48px;height:48px;object-fit:contain;display:block;flex:0 0 auto;}

    /* Keep the site title/navigation bar permanently visible while scrolling. */
    header{position:fixed !important;top:0 !important;left:0 !important;right:0 !important;width:100% !important;z-index:1000 !important;background:rgba(255,254,250,.97);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);}
    body{padding-top:108px;}
    .mobile-menu{z-index:1001;}
    html{scroll-padding-top:108px;}

    /* Use the repository's full hero-portrait-warm.png asset, scaled only as needed to fit the hero panel bounds. */
    .hero{height:auto !important;min-height:0 !important;}
    .hero-image{height:auto !important;min-height:0 !important;align-self:stretch;aspect-ratio:1 / 1.04;overflow:hidden;padding:0;background:#e8e3d8;display:flex;align-items:center;justify-content:center;box-sizing:border-box;}
    .hero-image img{width:100%;height:100%;max-width:100%;max-height:100%;min-width:0;min-height:0;display:block;object-fit:contain;object-position:center center;image-rendering:auto;-webkit-backface-visibility:hidden;backface-visibility:hidden;}

    /* Responsive safety: prevent horizontal overflow and keep every section inside the viewport. */
    html,body{width:100%;max-width:100%;overflow-x:hidden;}
    header{width:100%;min-width:0;}
    img,svg{max-width:100%;}
    .hero-copy,.hero-image,.values,.value,section,.section-inner,.grid-3,.card,.contact-wrap,.contact-box{min-width:0;}

    @media(max-width:1180px){
      body{padding-top:94px;}
      .mobile-menu{top:94px;}
      .hero-image{aspect-ratio:1 / 1.04;padding:0;}
    }

    @media(max-width:720px){
      header{display:flex;width:100%;height:78px;padding:12px 16px;gap:10px;align-items:center;}
      body{padding-top:78px;}
      .brand{min-width:0;max-width:calc(100% - 54px);flex:1 1 auto;gap:10px;}
      .brand>div{min-width:0;overflow:hidden;}
      .leaf{width:32px;height:44px;flex:0 0 32px;}
      .brand-name{font-size:20px;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
      .brand-sub{font-size:11px;line-height:1.35;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:3px;}
      .menu-toggle{display:flex;flex:0 0 44px;width:44px;height:44px;}
      .mobile-menu{top:78px;left:16px;right:16px;width:auto;max-width:none;}
      .hero-copy,.values,section{width:100%;overflow:hidden;}
      .hero-copy{padding:58px 7% 50px;}
      .hero h1{font-size:clamp(40px,11vw,48px);line-height:1.16;overflow-wrap:anywhere;}
      .eyebrow{overflow-wrap:anywhere;}
      .hero-copy p,.value p,.card p,.section p{overflow-wrap:anywhere;}
      .value h3,.card h3,.section h2{overflow-wrap:anywhere;}
      .actions{max-width:100%;}
      .button{max-width:100%;}
      .hero-image{width:100%;height:auto !important;min-height:0 !important;max-height:none !important;aspect-ratio:4 / 3;padding:0;}
      .grid-3{width:100%;}
      .card{width:100%;}
      .contact-box{min-width:0;width:100%;}
      footer{width:100%;padding:28px 7%;overflow:hidden;}
      footer span{min-width:0;max-width:100%;}
      .psi-membership{white-space:normal;gap:10px;overflow-wrap:anywhere;}
      .psi-mark{width:44px;height:44px;flex:0 0 44px;}
    }
'''

for name in ("index.html", "contact.html"):
    path = ROOT / name
    text = path.read_text(encoding="utf-8")

    text = text.replace("Graduate Member of the PSI", SUBTITLE)
    text = text.replace("Graduate Member of the Psychological Society of Ireland", SUBTITLE)

    if name == "index.html":
        title = "Aishwarya Sreenivasan | Psychologist in Ireland"
        description = (
            "Aishwarya Sreenivasan provides psychological assessment and therapy for young people and adults, "
            "plus psychological wellbeing solutions for organisations in Ireland."
        )
        canonical = SITE_URL + "/"
    else:
        title = "Contact Aishwarya Sreenivasan | Psychologist in Ireland"
        description = (
            "Contact Aishwarya Sreenivasan about psychological assessment, therapy and workplace wellbeing support in Ireland."
        )
        canonical = SITE_URL + "/contact.html"

    text = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", text, count=1, flags=re.DOTALL)
    text = re.sub(
        r'<meta\s+name="description"\s+content="[^"]*">',
        f'<meta name="description" content="{description}">',
        text,
        count=1,
        flags=re.DOTALL,
    )

    text = re.sub(r'\s*<link rel="canonical" href="[^"]*"\s*/?>', "", text)
    text = re.sub(r'\s*<meta property="og:[^"]*" content="[^"]*"\s*/?>', "", text)
    text = re.sub(r'\s*<meta name="twitter:[^"]*" content="[^"]*"\s*/?>', "", text)
    text = re.sub(r'\s*<script type="application/ld\+json">\s*\{.*?\}\s*</script>', "", text, flags=re.DOTALL)

    social = f'''
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Aishwarya Sreenivasan | Psychology">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
'''
    text = text.replace("</head>", social + SEO_SCHEMA + "\n</head>", 1)

    text = text.replace(
        ".hero h1{font:400 clamp(48px,5vw,74px)/1.08 var(--serif);",
        ".hero h1{font:400 clamp(48px,5vw,74px)/1.18 var(--serif);"
    )
    text = text.replace(
        ".eyebrow{letter-spacing:.045em;text-transform:uppercase;color:var(--sage-dark);font-size:15px;margin:0 0 25px}",
        ".eyebrow{letter-spacing:.045em;text-transform:uppercase;color:var(--sage-dark);font-size:15px;margin:0 0 30px}"
    )
    text = text.replace(
        ".rule{width:72px;height:1px;background:var(--sage);margin:38px 0}",
        ".rule{width:72px;height:1px;background:var(--sage);margin:42px 0}"
    )
    text = text.replace(
        ".hero h1{font-size:48px}",
        ".hero h1{font-size:48px;line-height:1.15}"
    )

    # Remove any prior generated location section/footer so repeated workflow runs stay valid.
    text = re.sub(r'\s*<section class="section soft" id="locations".*?</section>\s*', "\n", text, flags=re.DOTALL)
    text = re.sub(r'\s*<footer>.*?</footer>\s*', "\n", text, flags=re.DOTALL)

    if name == "index.html":
        # Put the Ireland/local SEO section immediately before the contact section.
        contact_match = re.search(r'<section\b[^>]*\bid="contact"\b[^>]*\bclass="section contact"', text)
        if not contact_match:
            contact_match = re.search(r'<section\b[^>]*\bclass="section contact"[^>]*\bid="contact"', text)
        if contact_match:
            text = text[:contact_match.start()] + LOCATION_SECTION + "\n" + text[contact_match.start():]
        else:
            text = text.replace("</body>", LOCATION_SECTION + "\n" + FOOTER + "\n</body>", 1)
        text = text.replace("</body>", FOOTER + "\n</body>", 1)
    else:
        text = text.replace("</body>", FOOTER + "\n</body>", 1)

    if "/* Use the repository's full hero-portrait-warm.png asset, scaled only as needed to fit the hero panel bounds. */" not in text:
        text = text.replace("</style>", BRANDING_CSS + "</style>", 1)

    path.write_text(text, encoding="utf-8")

old_logo = ROOT / "psi-logo-footer.png"
if old_logo.exists():
    old_logo.unlink()
