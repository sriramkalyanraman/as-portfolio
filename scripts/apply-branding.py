from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBTITLE = "Member of the Psychological Society of Ireland (PSI)"

for name in ("index.html", "contact.html"):
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    text = text.replace("Graduate Member of the PSI", SUBTITLE)
    text = text.replace("Graduate Member of the Psychological Society of Ireland", SUBTITLE)
    text = text.replace("<footer>", '<footer>')
    if 'class="psi-mark"' not in text and "<footer>" in text:
        text = text.replace("</footer>", '  <img class="psi-mark" src="psi-logo.svg" alt="The Psychological Society of Ireland logo">\n  </footer>')
    if ".psi-mark{" not in text:
        text = text.replace("footer{", "footer{flex-direction:column;align-items:center;text-align:center;")
        text = text.replace("footer span{", ".psi-mark{width:76px;height:76px;object-fit:contain;display:block;margin:12px auto 0}\n    footer span{")
    path.write_text(text, encoding="utf-8")

# Remove the mistaken bitmap placeholder logo from the repository.
old_logo = ROOT / "psi-logo-footer.png"
if old_logo.exists():
    old_logo.unlink()
