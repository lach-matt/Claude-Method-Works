#!/usr/bin/env python3
"""DOCKET 67 codata-2018-constants: classify every selftest line that differs between the
baseline sandbox copy of research/warp-drive and a copy whose constant literals were replaced
(gHi = BIPM-01 6.67559e-11, gLo = LENS-14 6.67191e-11, g1s = CODATA +1 sigma 6.67445e-11,
gDL = DerSimonian-Laird consensus 6.67399e-11, em22 = CODATA 2022 mu0/eps0/m_e/a0/E_h and exact
hbar).  A flipped line is BOOLEAN (a verdict: its got/want are True/False, or it has no number)
or NUMERIC (a pinned figure).  Sandbox copies live under ../sandbox; the tree is never touched.
Prints the flips; exit 1 if any BOOLEAN verdict flips."""
import os, re, sys, difflib
S = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sandbox", "logs")
FAILTOK = re.compile(r"(\bFAIL\b|\[XX\]|^\s*XX\b|SELFTEST FAIL)")
def lines(v, f):
    p = os.path.join(S, v, f + ".log")
    return open(p, errors="replace").read().splitlines() if os.path.exists(p) else []
def norm(s):
    return re.sub(r"/tmp/\S+", "<tmp>", s)
TRACED = {  # boolean-typed checks traced, by reading the owner line, to a numeric pin
    "the invariant is kept executable": "spec.py:286-287 abs(seating_invariant()/1.54562e19 - 1) < 1e-4: a 5-s.f. NUMERIC PIN",
    "l_P DERIVED from hbar, G, c agrees": "tolman.py:2771-2772 compares derived l_P with the TYPED CODATA l_P; perturbing G alone makes the typed pair inconsistent (perturbation artefact)",
    "FAILS on one digit of the exchange rate": "ledger.py:3934-3936 negative control mutates the literal '1.348948e+26', absent once G moves: control artefact of a 7-s.f. pin",
    "--check from another cwd finds LEDGER.md": "ledger.py:3949 LEDGER.md on disk was generated at the base constants: document-sync pin",
}
bool_flips = 0
summary = {}
for v in ("g1s", "gDL", "gHi", "gLo", "em22"):
    rc = dict(l.split() for l in open(os.path.join(S, v, "RC")) if l.strip() and l.strip() != "DONE")
    rcb = dict(l.split() for l in open(os.path.join(S, "base", "RC")) if l.strip() and l.strip() != "DONE")
    num = boo = 0
    print("=" * 20, v)
    for f in rc:
        if rc[f] == rcb[f]:
            continue
        base = set(norm(x) for x in lines("base", f) if FAILTOK.search(x))
        for x in lines(v, f):
            if not FAILTOK.search(x) or norm(x) in base or "SELFTEST" in x:
                continue
            if re.search(r"^\s*(FAIL|XX)\s+\S.*: got", x) or "has DRIFTED" in x or "nope.md" in x:
                kind = "NUMERIC" if re.search(r"got [-\d.]", x) or "DRIFTED" in x else "BOOLEAN?"
            elif re.search(r"\b(True|False)\b", x):
                kind = "BOOLEAN"
            elif re.search(r"\d\.\d", x):
                kind = "NUMERIC"
            else:
                kind = "BOOLEAN?"
            for key, why in TRACED.items():
                if key in x and kind.startswith("BOOLEAN"):
                    kind = "PIN-IN-BOOLEAN"
                    x = x + "   <-- " + why
            if kind.startswith("BOOLEAN"):
                boo += 1
            else:
                num += 1
            print("  %-14s %-12s %s" % (kind, f, x.strip()[:260]))
    summary[v] = (num, boo)
    bool_flips += boo
print()
for v, (n, b) in summary.items():
    print("%-5s numeric-pin flips (incl. traced pin-in-boolean) %3d   untraced boolean/verdict flips %d" % (v, n, b))
sys.exit(1 if bool_flips else 0)
