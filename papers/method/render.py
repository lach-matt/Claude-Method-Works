#!/usr/bin/env python3
"""render.py -- a paper's PAPER.md to HTML and a paged PDF, for review.

    python3 papers/method/render.py papers/method/01-closure-law
    python3 papers/method/render.py --all

Writes papers/method/out/<dir>.html and .pdf. pandoc + WeasyPrint; the paper template is paper.html
beside this script. The PDF is generated; never hand-edit it.
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")


def render(d):
    d = os.path.abspath(d)
    name = os.path.basename(d.rstrip("/"))
    src = os.path.join(d, "PAPER.md")
    os.makedirs(OUT, exist_ok=True)
    html = os.path.join(OUT, name + ".html")
    pdf = os.path.join(OUT, name + ".pdf")
    text = open(src, encoding="utf-8").read()
    title = text.split("\n", 1)[0].lstrip("# ").strip()
    subprocess.run(["pandoc", src, "-o", html, "--standalone", "--embed-resources",
                    "--from", "markdown+pipe_tables+smart+implicit_figures", "--resource-path", d,
                    "--template", os.path.join(HERE, "paper.html"), "--metadata", "title=" + title], check=True)
    import weasyprint
    weasyprint.HTML(filename=html, base_url=d + "/").write_pdf(pdf)
    data = open(pdf, "rb").read()
    try:
        import pypdf
        pages = len(pypdf.PdfReader(pdf).pages)
    except Exception:  # noqa: BLE001 -- a count, not a verdict
        pages = len(re.findall(rb"/Type\s*/Page\b(?!s)", data))
    print("  %s  %.2f MB  %d pages" % (os.path.relpath(pdf, HERE), len(data) / 1048576, pages))
    return pdf


if __name__ == "__main__":
    if "--all" in sys.argv:
        dirs = sorted(os.path.join(HERE, x) for x in os.listdir(HERE) if re.match(r"\d\d-", x))
    else:
        dirs = [a for a in sys.argv[1:] if not a.startswith("--")]
    for d in dirs:
        render(d)
