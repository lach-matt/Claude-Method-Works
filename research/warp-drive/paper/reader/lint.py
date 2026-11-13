#!/usr/bin/env python3
"""lint.py -- the guard for the reader's edition (STYLE.md section 2-4).

    python3 lint.py chapters/07-foo.md ...     check chapter sources (labels may stay symbolic)
    python3 lint.py --chapters                 check every chapter source, and cross-chapter label references
    python3 lint.py --paper                    check the assembled PAPER.md (no symbolic label may remain)
    python3 lint.py --selftest                 controls: each forbidden pattern must fire on a planted line

Exit 1 on any hit. Stdlib only.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (pattern, reason). Case-sensitive unless (?i) is given.
FORBIDDEN = [
    (r"[A-Za-z0-9_\-]+\.(py|md|tsv|csv|json|out|txt|sh|mjs|html|pdf|tgz|zip)\b", "file name"),
    (r"(?i)\b(checks|proof5|docket\d*|n1star|lemmas)/", "repository path"),
    (r"(?i)\bdockets?\b", "process word: docket"),
    (r"(?i)\bn1star\b|N1\*|\bN1STAR\b", "working name"),
    (r"(?i)\bwarp\b", "research tree name"),
    (r"`", "backtick span"),
    (r"\b[0-9a-f]{32}\b", "md5"),
    (r"(?i)\bverifiers?\b|\bverified by an independent\b|\bindependent readers?\b", "process word: verifier/reader"),
    (r"(?i)\bseat(ed|ing|s)?\b", "process word: seat"),
    (r"(?i)\bfinal[- ]pass\b|\[final-pass\]", "process word: final pass"),
    (r"(?i)\brounds?\s+\d|\bround\s+(one|two|three)\b|\bin round\b", "process word: round"),
    (r"\bR\d{1,2}\.\d{1,2}\b|\[R\d+[-\w]*\]|\bR\d{1,2}-[A-Z]\b", "round label"),
    (r"\bD\d{3}\b", "D-label"),
    (r"(?i)\bnits?\b|\bminors?\b(?! (of|in|axis|order|determinant))|\bMajor\s+\d|\bMajors?\b", "review word"),
    (r"(?i)\bsupersed\w*|\bwithdrawn\b|\bamended\b|\bamendment\b", "process word: amendment"),
    (r"(?i)\bthe record\b|\bthe record's\b|\brecord's own\b", "process word: the record"),
    (r"(?i)\bthe supplement\b|\bsupplement\b", "process word: supplement"),
    (r"(?i)\bcommission\w*|\bthe brief\b|\bworkstreams?\b|\bWS-[A-H]\b", "process word: commission/brief"),
    (r"(?i)\bledgers?\b|\bcensus\b|\bprovenance\b|\bselftest\b|\bmutants?\b|\bpinned?\b", "process word"),
    (r"(?i)\bauthor's words\b|\bthe author's record\b", "process word: author's words"),
    (r"\bREAD\b", "status tag READ"),
    (r"\((computed|deduced)\b|\b(computed|deduced)[;,)]\s|\bcomputed, not certified\b", "status tag"),
    (r"(?i)\bclaude\b|\bAI\b|\bagents?\b|\bLLM\b", "AI word"),
    (r"(?i)\bearlier (version|draft)\b|\bpreviously (read|said|stated)\b|\bwas corrected\b|\bwas found\b",
     "narration of the work"),
    (r"(?i)\bcrucially\b|\bimportantly\b|\bit is worth noting\b|\bdelve\w*|\bleverag\w*|\bseamless\w*|"
     r"\bin essence\b|\blet us now turn\b|\btapestry\b", "filler"),
    (r"(?i)\bSOURCE\b(?= )|\bTheorem E\b", "working name"),
    (r"\[\[C:|\bComputation C\d|(?i:\bcomputations?\b|\bprograms?\b|\bcode\b|\bscripts?\b|\bsympy\b|\bmpmath\b|\binterval arithmetic\b|\bfloating[- ]point\b|\bnumerically\b|\bcomputer\b)", "no-code ruling"),
]
RX = [(re.compile(p), why) for p, why in FORBIDDEN]

RESULT_KINDS = ("thm", "lem", "prop", "cor", "def", "rem", "eq", "ch", "sec", "app", "part")
DEF_RX = re.compile(r"\{#(" + "|".join(RESULT_KINDS) + r"):([a-z0-9][a-z0-9\-]*)\}")
REF_RX = re.compile(r"\[\[(" + "|".join(RESULT_KINDS) + r"|C):([a-z0-9][a-z0-9_\-]*)\]\]")


URL = re.compile(r"https?://\S+|doi:\S+|arXiv:\S+")


def scan_text(name, text, assembled):
    hits = []
    lines = text.split("\n")
    refs = "references" in name
    for i, ln in enumerate(lines, 1):
        if len(ln) > 121:
            hits.append((i, "line longer than 121 characters (%d)" % len(ln), ln[:80]))
        probe = URL.sub("", ln)
        for rx, why in RX:
            if refs and why in ("no-code ruling", "file name", "filler", "process word"):
                continue  # titles of cited works are quoted as published
            m = rx.search(probe)
            if m:
                hits.append((i, why, ln.strip()[:110]))
        if assembled and ("{#" in ln or "[[" in ln):
            hits.append((i, "unresolved symbolic label", ln.strip()[:110]))
        if "[[pending:" in ln:
            hits.append((i, "pending: an open issue the coordinator must resolve", ln.strip()[:110]))
    proofs = len(re.findall(r"^\s*\*?\*?Proof\b", text, re.M))
    qeds = text.count("∎")
    if proofs != qeds:
        hits.append((0, "%d proofs opened but %d closed by ∎" % (proofs, qeds), ""))
    return hits


def report(name, hits):
    for i, why, ln in hits:
        print("%s:%s  [%s]  %s" % (name, i, why, ln))
    return len(hits)


def chapter_files():
    d = os.path.join(HERE, "chapters")
    return sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".md")) if os.path.isdir(d) else []


def run_chapters(files):
    total = 0
    defs, refs = {}, []
    for f in files:
        text = open(f, encoding="utf-8").read()
        name = os.path.relpath(f, HERE)
        total += report(name, scan_text(name, text, assembled=False))
        for m in DEF_RX.finditer(text):
            key = m.group(1) + ":" + m.group(2)
            if key in defs:
                total += report(name, [(0, "label defined twice (also in %s)" % defs[key], key)])
            defs[key] = name
        for m in REF_RX.finditer(text):
            refs.append((name, m.group(1), m.group(2)))
    exported = set()
    op = os.path.join(HERE, "OUTLINE.md")
    if os.path.isfile(op):
        otext = open(op, encoding="utf-8").read()
        exported = {m.group(1) + ":" + m.group(2) for m in DEF_RX.finditer(otext)}
        exported |= set(re.findall(r"\b(?:part|ch|app):[a-z0-9][a-z0-9\-]*", otext))  # the outline's table
    for name, kind, key in refs:
        if kind == "C":
            continue
        k = kind + ":" + key
        if k not in defs and k not in exported:
            total += report(name, [(0, "reference to undefined label", k)])
    print("chapters: %d file(s), %d label(s) defined, %d hit(s)" % (len(files), len(defs), total))
    return total


def selftest():
    planted = [
        "see checks/ix5.py", "the docket", "the verifier found", "as seated in", "round 9 of", "R10.1 states",
        "D612 records", "the record's text", "the supplement's Lemma", "the brief", "a census of", "mutant 3",
        "READ at source", "(computed, exactly)", "Claude", "an earlier version", "crucially", "N1* says", "`x`",
        "warp field", "5c1a186aa2528e503e24c336f9a6dcef", "x" * 130, "Proof. trivial", "see [[C:ix5]]", "Computation C12 verifies",
        "checked numerically", "by interval arithmetic", "the program", "sympy",
    ]
    ok = True
    for p in planted:
        if not scan_text("selftest", p, assembled=False):
            print("CONTROL FAILED to fire:", p); ok = False
    clean = ("**Theorem {#thm:main}** Let λ > 0. Then the metric g_λ satisfies [[eq:energy]].\n"
             "Proof. By Lemma 5.3 and the identity (5.2), expanded term by term. ∎")
    if scan_text("selftest", clean, assembled=False):
        print("FALSE POSITIVE on clean text:", scan_text("selftest", clean, assembled=False)); ok = False
    if not scan_text("selftest", "see [[thm:main]]", assembled=True):
        print("CONTROL FAILED: unresolved label in assembled mode"); ok = False
    print("selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--selftest" in a:
        sys.exit(selftest())
    if "--paper" in a:
        p = os.path.join(HERE, "PAPER.md")
        n = report("PAPER.md", scan_text("PAPER.md", open(p, encoding="utf-8").read(), assembled=True))
        print("PAPER.md: %d hit(s)" % n)
        sys.exit(1 if n else 0)
    files = chapter_files() if "--chapters" in a else [x for x in a if not x.startswith("--")]
    sys.exit(1 if run_chapters(files) else 0)
