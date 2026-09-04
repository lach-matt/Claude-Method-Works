#!/usr/bin/env python3
"""power.py -- what each mechanism can currently distinguish, and what it would need.

Register 808. "The more spectra channels we can produce, the better we can verify the
math" is right, and this makes it quantitative: for every mechanism, the sample it
rests on, the width of its confidence interval, and the sample that would halve it.

A mechanism resting on 54 observations cannot distinguish 81% from 90%. One resting on
145 can distinguish 100% from 98%. The difference decides whether a claim can be
promoted from tendency to law, and it is arithmetic, not judgement.

Wilson score interval at 95%, which behaves correctly near 0 and 1 where the normal
approximation does not.
"""
import math
from zeno import State, step

def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 1.0)
    p = k / n
    d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d
    h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return (max(0.0, c-h), min(1.0, c+h))

def n_for_width(p, w, z=1.96):
    """the n at which the Wilson half-width falls to w/2"""
    n = 10
    while n < 10_000_000:
        lo, hi = wilson(round(p*n), n, z)
        if hi - lo <= w: return n
        n = int(n * 1.3) + 1
    return None

# (mechanism, what is counted, successes, trials, the register)
CLAIMS = [
    ("P.lcollapse", "adjacent-l pairs correctly ordered",        145, 145, "772"),
    ("P.iso",       "isoelectronic s/p ladders monotone",          8,   9, "773"),
    ("P.iso",       "across-table pairs falling above d=0.3",     15,  15, "717"),
    ("P.jj",        "J-pairs consistent (trivial excluded)",      52,  65, "775"),
    ("P.jsplit",    "open/heavy pairs that split",                19,  19, "758"),
    ("P.jsplit",    "closed/light pairs that do NOT split",       10,  10, "758"),
    ("P.termsplit", "Si I nf terms separating, J-pairs together",   4,   4, "739"),
    ("P.polar",     "elements with high-l defect rising in Z",      6,   7, "731"),
    ("P.dcollapse", "P.iso exceptions that are d and small",       10,  10, "719"),
    ("P.coreblind", "parent-term pairs agreeing",                   2,   2, "743"),
    ("P.buildlimit","constructed limits confirmed by convergence",  1,   1, "712"),
    ("P.trunc",     "species gaining channels when untruncated",    4,   4, "676"),
    ("§22.1",       "interior cells passing the T bracket",      789, 789, "800"),
    ("§25.6.1",     "interior cells passing the delta bracket",  546, 789, "796"),
    ("§25.6.1",     "resolved steps with delta falling",          44,  54, "806"),
    ("P.selfsame",  "disjoint-window pairs agreeing",             46,  48, "811"),
    ("P.converge",  "published limit within 3x the fit error",    38,  58, "813"),
]

with State("power") as s:
    _ = step(s, "compute the interval on every claim", lambda: None, budget=60)

print(f"  {'mechanism':<13}{'what is counted':<40}{'k/n':>9}{'rate':>7}{'95% interval':>16}")
weak = []
for m, w, k, n, r in CLAIMS:
    lo, hi = wilson(k, n)
    width = hi - lo
    print(f"  {m:<13}{w:<40}{f'{k}/{n}':>9}{100*k/n:>6.0f}%{f'{100*lo:.0f}–{100*hi:.0f}%':>16}")
    if width > 0.15: weak.append((m, w, k, n, width))

print()
print(f"  UNDER-POWERED — an interval wider than 15 points:\n")
print(f"  {'mechanism':<13}{'what is counted':<40}{'now':>7}{'to halve it':>13}")
for m, w, k, n, width in weak:
    need = n_for_width(k/n, width/2)
    print(f"  {m:<13}{w:<40}{n:>7}{need if need else '—':>13}")
print()
print("  and the claims already at 100% cannot be strengthened by more of the same —")
print("  only by a sample that could have broken them.")
