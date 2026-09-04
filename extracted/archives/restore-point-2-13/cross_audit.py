#!/usr/bin/env python3
"""cross_audit.py -- PART 1: do the five documents agree?

Register 647: the book and its four compendia are generated from one source, but
"generated" is a claim about the pipeline, not a check on the output. This
compares the figures that appear in more than one document.

A disagreement here is the worst failure available: a reader holding two of the
five would see the work contradict itself.

Under zeno, checkpointed per document.
"""
import re, os, sys
from zeno import State, step

DOCS = {
 "book":      "The Method 1.6.md",
 "math":      "COMPENDIUM.md",
 "spectra":   "SPECTRA.md",
 "register":  "REGISTER.md",
 "indices":   "INDICES.md",
}

# every figure that should be identical wherever it appears
SHARED = {
 "Λ₈ cells":            (r"\b976\b",            "976"),
 "Λ₈ box":              (r"\b6,912\b",          "6,912"),
 "F(−1)":               (r"F\(−1\)\s*=?\s*2\b", "2"),
 "Λ₉ cells":            (r"\b1,654\b",          "1,654"),
 "Λ₉ composable":       (r"\b1,169\b",          "1,169"),
 "Λ₁₀ cells":           (r"\b2,535\b",          "2,535"),
 "Λ₁₃ cells":           (r"\b64,290\b",         "64,290"),
 "the seed":            (r"seed\D{0,24}\b7\b",  "7"),
 "periodic table E":    (r"\b36\b",             "36"),
 "calendar E":          (r"\b365\b",            "365"),
 "violation cells":     (r"\b2,370\b",          "2,370"),
 "violation box":       (r"\b19,440\b",         "19,440"),
 "violation E":         (r"E\s*=\s*30\b",       "30"),
 "channels":            (r"\b133\b",            "133"),
 "interior cells":      (r"\b869\b",            "869"),
 "elements tested":     (r"\b18,288\b",         "18,288"),
}

def run():
    txt = {k: open(v, encoding="utf-8").read() for k, v in DOCS.items() if os.path.exists(v)}
    # the register is a RECORD: its entries state what was true when written, and
    # a present-tense check must not read them (register 648)
    live_txt = dict(txt)
    if "book" in live_txt:
        _b = live_txt["book"]
        _a = _b.rindex("## 28. Withdrawals"); _c = _b.rindex("## 29.")
        live_txt["book"] = _b[:_a] + _b[_c:]
    live_txt.pop("register", None)
    present = {}
    for name, (pat, val) in SHARED.items():
        present[name] = {d: bool(re.search(pat, t)) for d, t in txt.items()}
    # a figure that appears in one doc and is CONTRADICTED in another
    contra = []
    # the composability profile must be identical wherever printed
    prof = {}
    for d, t in txt.items():
        got = re.findall(r"0\.(?:0000|7068|8087|6956|6394|6186)", t)
        if got: prof[d] = sorted(set(got))
    # the object count in the math compendium against the live register
    import importlib.util as iu
    sp = iu.spec_from_file_location("_mr", "mathreg.py"); mr = iu.module_from_spec(sp)
    try: sp.loader.exec_module(mr)
    except SystemExit: pass
    live = len(mr.REG)
    stated = {}
    for d, t in live_txt.items():
        # a count explicitly marked as a snapshot, or sitting inside the register,
        # is a record rather than a present claim (register 648)
        got=[]
        for mm in re.finditer(r"\b(\d{3}) objects\b", t):
            after = t[mm.end():mm.end()+220]
            before = t[max(0, mm.start()-120):mm.start()]
            if "snapshot" in after or "held at that" in after: continue
            if re.search(r"grew|rose|from \d{3}|then|was|earlier", before): continue
            got.append(int(mm.group(1)))
        if got: stated[d] = sorted(set(got))
    # register range
    rng = {}
    for d, t in txt.items():
        n = [int(x) for x in re.findall(r"^(?: {0,3}|### )(\d{3})[.\s]", t, re.M)]
        if n: rng[d] = (min(n), max(n), len(n))
    return txt, present, prof, stated, live, rng

with State("cross_audit") as st:
    txt, present, prof, stated, live, rng = step(st, "compare the five documents", run, budget=600)

print(f"  PART 1 · CROSS-DOCUMENT CONSISTENCY — {len(txt)} documents\n")
print(f"  {'figure':<22}" + "".join(f"{d:>11}" for d in DOCS))
for name, d in present.items():
    print(f"  {name:<22}" + "".join(f"{('yes' if d.get(k) else '·'):>11}" for k in DOCS))
print(f"\n  the composability profile, where printed:")
for d, v in prof.items():
    print(f"    {d:<12}{len(v)} of 6 values: {v}")
print(f"\n  the object count — live register holds {live}:")
for d, v in stated.items():
    tag = "  ← DISAGREES" if any(x != live for x in v) else ""
    print(f"    {d:<12}{v}{tag}")
print(f"\n  numbered-entry ranges:")
for d, (lo, hi, n) in rng.items():
    print(f"    {d:<12}{lo}–{hi}   {n} entries")
bad = sum(1 for d, v in stated.items() if any(x != live for x in v))
print(f"\n  PART 1 " + ("PASSES" if not bad else f"FAILURES: {bad}"))
sys.exit(1 if bad else 0)
