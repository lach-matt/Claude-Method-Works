#!/usr/bin/env python3
"""The Method 1.6 numbers-index.py -- reconstructed from §F.2 and §F.3.

The file named in the manifest was never supplied. It is rebuilt from the
coordinates §F.2 prints and the assignment rules §F.3 states, not from the E(G)
it must reproduce.

  quantity      count · density · defect · bound · measurement · rate   FIBRE
  definition    asserted < stated < stated with inputs                  ordered
  inputs        named < enumerated < printed                            ordered
  verification  asserted < recomputed < recomputed under variation      ordered

§F.3: "the quantity's kind from its units and vocabulary, the definition from
whether a method and an input set are both named, the inputs from whether they
are named, enumerated or printed, and the verification from whether the
paragraph records a recomputation and whether that recomputation varied the
caps. The rules are stated so the assignment can be rerun; they are coarse, and
being coarse and rerunnable is the point."

CONSTRAINT (register 367): definition = stated ⟹ inputs ≠ enumerated. The two
cannot hold together, because *stated* is assigned exactly when a method is
named and an input set is NOT, while *enumerated* is assigned exactly when one
IS. The press applies it as `not (x[0]==1 and x[1]==1)`.

INTERFACE, fixed by the press: this module exports NUM and classify(paragraph),
where classify returns (fibre, (definition, inputs, verification)).
"""
import re

# a claim-bearing number: a bare integer with a separator, a decimal, a
# percentage, or a scientific figure. bare small integers are excluded because
# they are overwhelmingly section and chapter numbers.
NUM = re.compile(r"\b\d{1,3}(?:,\d{3})+\b|\b\d+\.\d+\b|\b\d+(?:\.\d+)?\s?%|"
                 r"\b\d+\s?×\s?10[⁻\-]?\d+|\b\d{4,}\b")

# ---- the fibre: the quantity's kind, from its units and vocabulary ----------
_FIB = [
 ("density",     r"\bdensit|\bfill\b|\bshare\b|\bfraction\b|% of (?:its|the) (?:own )?box"),
 ("defect",      r"\bE\(|\bdefect\b|\badmitted and absent\b|\bclosure defect\b|\bslack\b"),
 ("rate",        r"\brate\b|\bper (?:cell|entry|session|claim)\b|\bratio\b|\bwithdrawal ratio\b"),
 ("bound",       r"\bbound\b|\bfloor\b|\bceiling\b|\bat most\b|\bat least\b|\bno more than\b|"
                 r"\bcannot exceed\b|\bpole\b"),
 ("measurement", r"\bcm⁻¹|\bmeasured\b|\bMHz\b|\beV\b|\bσ\b|\bobserved\b|\bspectro"),
 ("count",       r""),          # the default: a count of things
]
def _fibre(p):
    for name, pat in _FIB:
        if pat and re.search(pat, p, re.I):
            return name
    return "count"

# ---- definition: is a METHOD named, and is an INPUT SET named? --------------
_METHOD = re.compile(r"\bcomputed\b|\brecomputed\b|\benumerat|\bverified\b|\bsweep|\bby (?:direct )?"
                     r"computation\b|\bthe method\b|\bthe procedure\b|\bexhaustiv|\bcounted\b", re.I)
_INPUTSET = re.compile(r"\bthe input set\b|\binputs? (?:are|is) printed\b|\bat caps\b|\bcaps \(|"
                       r"\bover (?:all|every) \d|\bthe input set is\b|\bprinted below\b|"
                       r"\bfrom the (?:table|list|construction)\b", re.I)
_PRINTED = re.compile(r"\bprinted (?:here|below|beside)\b|\bevery (?:input|value) (?:used )?is printed\b|"
                      r"\bthe inputs are printed\b", re.I)
_ENUM = re.compile(r"\benumerat|\ball \d[\d,]* \b|\bevery cell\b|\bevery pair\b|\bexhaustively\b", re.I)
_RECOMP = re.compile(r"\brecomputed\b|\breproduc|\bre-?run\b|\bverified (?:here|against)\b", re.I)
_VARIED = re.compile(r"\bunder variation\b|\bat (?:four|three|two) cap|\bcap settings\b|"
                     r"\bacross (?:four|three) \b|\bat every cap\b", re.I)

def classify(par):
    """§F.3's rules, run mechanically. returns (fibre, (definition, inputs, verification))."""
    method = bool(_METHOD.search(par))
    inputset = bool(_INPUTSET.search(par))
    printed = bool(_PRINTED.search(par))
    enum = bool(_ENUM.search(par))

    # definition: asserted 0 < stated 1 < stated with inputs 2
    if method and inputset:  d = 2
    elif method:             d = 1            # a method named and no input set
    else:                    d = 0

    # inputs: named 0 < enumerated 1 < printed 2
    if printed:              i = 2
    elif enum:               i = 1
    else:                    i = 0

    # register 367: 'stated' is assigned exactly when no input set is named, so
    # it cannot coexist with 'enumerated'. the assignment rules already forbid
    # it; this makes the exclusion explicit rather than emergent.
    if d == 1 and i == 1:    i = 0

    # verification: asserted 0 < recomputed 1 < recomputed under variation 2
    if _VARIED.search(par):  v = 2
    elif _RECOMP.search(par): v = 1
    else:                    v = 0

    return _fibre(par), (d, i, v)

if __name__ == "__main__":
    import sys
    from collections import defaultdict
    from itertools import product
    S = open("The Method 1.6.md", encoding="utf-8").read()
    pop = defaultdict(set); occ = defaultdict(int)
    for par in re.split(r"\n\s*\n", S):
        if not NUM.findall(par): continue
        q, c = classify(par); pop[q].add(c); occ[q] += len(NUM.findall(par))
    def R(X):
        v = [sorted({c[i] for c in X}) for i in range(3)]
        def e(a, b):
            m = {}
            for c in X: m[c[b]] = max(m.get(c[b], -99), c[a])
            z, o = -99, {}
            for t in sorted(m): z = max(z, m[t]); o[t] = z
            return o
        ph = {(a, b): e(a, b) for a in range(3) for b in range(3) if a != b}
        return {x for x in product(*v)
                if all(x[a] <= ph[(a, b)][x[b]] for a in range(3) for b in range(3) if a != b)}
    ok = lambda x: not (x[0] == 1 and x[1] == 1)
    print(f"  {'fibre':<14}{'occurrences':>12}{'cells':>7}{'admitted':>10}{'E':>5}")
    tot = 0
    for q in sorted(pop, key=lambda k: -occ[k]):
        adm = {x for x in R(pop[q]) if ok(x)}
        e = len(adm) - len(pop[q]); tot += e
        print(f"  {q:<14}{occ[q]:>12,}{len(pop[q]):>7}{len(adm):>10}{e:>5}")
    print(f"  {'all':<14}{sum(occ.values()):>12,}{'—':>7}{'—':>10}{tot:>5}")
    print(f"\n  E(G) = {tot} over {len(pop)} fibres")
