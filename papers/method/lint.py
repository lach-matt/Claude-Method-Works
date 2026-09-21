#!/usr/bin/env python3
"""lint.py -- the published-text guard for papers/method/<dir>/PAPER.md.

Mirrors the site's private patterns (tools/webindex.py PRIVATE_PATTERNS on main, with the paper's
own section marks excluded) and adds the paper contract's own forbidden list (PAPER-SPEC.md §8).
Also checks structure: title, thesis, author line, Abstract, §0, Verification record, References;
that every figure referenced exists; that every "Proof." has a matching ∎.

    python3 papers/method/lint.py papers/method/01-closure-law
    python3 papers/method/lint.py --all
Exit 1 on any hit.
"""
import os, re, sys

SITE = [
    r"\b[Rr]egisters?\s+\d", r"\bchapters?\s+\d", r"[A-Za-z0-9_\-]+\.md\b", r"\bL\d{2,5}\b(?![.\d])",
    r"The Method 1\.6", r"\bcorpus\b", r"\bCompendium\b", r"PROSE-ONLY", r"\bdockets?\b", r"\brulings?\b",
    r"\bseated members?\b", r"\bbundles?\b", r"method/members", r"\brecovered/", r"(?<![\w-])drive/", r"LW1-",
    r"r2-scf", r"tower-2\.py", r"\.tsv\b", r"rclose\.py", r"\bsessions?\s+\d", r"\bchats?\s+\d", r"\bhandoffs?\b",
    r"\bfaults?\s+\d", r"(?i)\bwarp\b", r"warp-drive",
]
OWN = [
    r"\bBUILD\s?\d", r"\bbuilds?\s+\d", r"\bthe books?\b", r"\bthis book\b", r"\bthe volumes?\b", r"\bthe compendi",
    r"(?i)\bthe record\b", r"\bthe store\b", r"\bworking register\b", r"\bseated\b", r"\bM ruled\b", r"\bM's ruling\b",
    r"(?i)earlier draft", r"(?i)previously read", r"(?i)\bwithdrawn\b", r"(?i)corrected here", r"(?i)recorded rather than repaired",
    r"\bPINNED\b", r"\bRECOVERED\b", r"\bRECONSTRUCTED\b", r"\bHELD\b", r"\bBANKED\b", r"\bW-\d{2,4}\b", r"\bFINDING-", r"\bDEF-\d",
    r"\bRUL-\d", r"\bSETTLED-", r"[A-Za-z0-9_\-]+\.(py|csv|json|out)\b", r"\bregister entry\b", r"\bRegister\b",
    r"§\s?\d+\.\d+\.\d+", r"\bAppendix [A-G]\b", r"\bA\.\d{1,2}\b(?! ?[a-z])",
]
RX_SITE = [re.compile(p) for p in SITE]
RX_OWN = [re.compile(p) for p in OWN]


def lint(d):
    p = os.path.join(d, "PAPER.md")
    if not os.path.isfile(p):
        print("%s: no PAPER.md" % d); return 1
    text = open(p, encoding="utf-8").read()
    lines = text.split("\n")
    hits = []
    for i, ln in enumerate(lines, 1):
        for rx in RX_SITE:
            if rx.search(ln):
                hits.append((i, "site:" + rx.pattern, ln.strip()[:100]))
        for rx in RX_OWN:
            if rx.search(ln):
                hits.append((i, "spec:" + rx.pattern, ln.strip()[:100]))
    # structure
    if not lines or not lines[0].startswith("# "):
        hits.append((1, "structure", "first line must be the # title"))
    if not re.search(r"^\*\*Matthew Lach\*\*", text, re.M):
        hits.append((0, "structure", "author line **Matthew Lach** · Independent Researcher · date"))
    for need in ("## Abstract", "## §0", "Verification record", "## References"):
        if need not in text:
            hits.append((0, "structure", "missing " + need))
    proofs = len(re.findall(r"\*\*Proof", text)) + len(re.findall(r"^\s*Proof\.", text, re.M))
    qeds = text.count("∎")
    if proofs > qeds:
        hits.append((0, "structure", "%d proofs but %d ∎" % (proofs, qeds)))
    for m in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text):
        f = os.path.join(d, m.group(1))
        if not os.path.isfile(f):
            hits.append((0, "figure", "missing " + m.group(1)))
    for f in re.findall(r"figures/[\w.\-]+", text):
        if not os.path.isfile(os.path.join(d, f)):
            hits.append((0, "figure", "missing " + f))
    for h in hits:
        print("%s:%s  [%s]  %s" % (p, h[0], h[1], h[2]))
    print("%s: %d hit%s" % (d, len(hits), "" if len(hits) == 1 else "s"))
    return 1 if hits else 0


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    if "--all" in sys.argv:
        dirs = sorted(os.path.join(here, x) for x in os.listdir(here) if re.match(r"\d\d-", x))
    else:
        dirs = [a for a in sys.argv[1:] if not a.startswith("--")]
    sys.exit(max([lint(d) for d in dirs] + [0]))
