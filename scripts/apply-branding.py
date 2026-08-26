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
    @media(max-width:720px){footer{display:block;padding:28px 7%;}footer span{display:flex;align-items:center;margin-top:10px}.psi-membership{white-space:normal;gap:10px}.psi-mark{width:44px;height:44px;margin-right:0;}}
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
