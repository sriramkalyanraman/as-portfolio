from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SUBTITLE = "Member of the Psychological Society of Ireland (PSI)"

FOOTER = (
    '<footer>'
    '<span>© 2026 Aishwarya Sreenivasan</span>'
    '<span class="psi-membership">'
    '<img class="psi-mark" src="psi-logo.svg" alt="" aria-hidden="true">'
    f'{SUBTITLE}'
    '</span>'
    '</footer>'
)

BRANDING_CSS = '''
    footer{display:flex;flex-direction:row;align-items:center;justify-content:space-between;gap:30px;padding:35px 8%;}
    .psi-membership{display:inline-flex;align-items:center;gap:12px;white-space:nowrap;}
    .psi-mark{width:48px;height:48px;object-fit:contain;display:block;flex:0 0 auto;}

    /* Responsive safety: prevent horizontal overflow and keep every section inside the viewport. */
    html,body{width:100%;max-width:100%;overflow-x:hidden;}
    header{width:100%;min-width:0;}
    img,svg{max-width:100%;}
    .hero-copy,.hero-image,.values,.value,section,.section-inner,.grid-3,.card,.contact-wrap,.contact-box{min-width:0;}

    @media(max-width:720px){
      header{display:flex;width:100%;height:78px;padding:12px 16px;gap:10px;align-items:center;}
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
      .hero-image{width:100%;height:118vw;min-height:360px;max-height:620px;}
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

    # Give the landing-page hero headline more vertical breathing room.
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

    text = re.sub(r"<footer>.*?</footer>", FOOTER, text, flags=re.DOTALL)
    text = re.sub(r"\s*\.psi-mark\{[^}]*\}", "", text)
    text = re.sub(r"\s*\.psi-membership\{[^}]*\}", "", text)
    text = re.sub(r"\s*footer\{[^}]*\}", "", text)
    text = re.sub(r"\s*@media\(max-width:720px\)\{footer\{display:block[^}]*\}footer span\{[^}]*\}[^}]*\}", "", text)
    if BRANDING_CSS.strip() not in text:
        text = text.replace("</style>", BRANDING_CSS + "</style>", 1)
    path.write_text(text, encoding="utf-8")

old_logo = ROOT / "psi-logo-footer.png"
if old_logo.exists():
    old_logo.unlink()
