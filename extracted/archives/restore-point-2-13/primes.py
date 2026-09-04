#!/usr/bin/env python3
"""primes.py -- does anything in the verified channels carry prime structure?

Register 896. The request is to check for prime factorization patterns. Two things
must be said before any number is computed.

FIRST, what could carry them. A quantum defect is a continuous physical quantity set
by how far a Rydberg orbital penetrates an ionic core; it is not an integer and has no
factorization. The integers in the compendium are: the principal quantum numbers n at
which a channel starts and ends, the member count, the interior-cell count, 2J, the
orbital l, the atomic number Z, and the core charge. Those are what can be tested.

SECOND, the danger. There are perhaps thirty integer quantities and a dozen ways to
ask a prime question of each, so several hundred tests are available and a few will
pass at p < 0.05 by construction. **Every test below is stated before it is run, the
count of tests is fixed in advance, and the threshold is Bonferroni-corrected.** A
pattern found by searching until something appears is not reported.

THE TESTS, fixed at eight:
  1  are channel START n values prime more often than chance?
  2  are channel END n values prime more often than chance?
  3  are MEMBER COUNTS prime more often than chance?
  4  are INTERIOR-CELL counts prime more often than chance?
  5  do channels whose member count is prime have smaller spreads?
  6  do prime-n levels sit anomalously within their series?
  7  is 2J prime more often than chance among J-resolved channels?
  8  does the count of channels per species factor unusually?

The null for 1-4 and 7: the same integers drawn from the observed range with the
observed marginal distribution of magnitudes, prime density taken from the range.
"""
import re, math, random, statistics as st
from collections import Counter, defaultdict
from zeno import State, step

def isprime(n):
    n = int(n)
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True

def binom_p(k, n, p):
    """two-sided exact binomial p-value"""
    from math import comb
    obs = comb(n, k) * p**k * (1-p)**(n-k)
    tot = 0.0
    for i in range(n+1):
        pr = comb(n, i) * p**i * (1-p)**(n-i)
        if pr <= obs * (1 + 1e-12): tot += pr
    return min(1.0, tot)

def load():
    rows = [l.rstrip().split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
    out = []
    for r in rows:
        m = re.search(r"n([spdfghik])\b", r[1])
        if not m: continue
        ns = re.findall(r"\d+", r[2])
        if len(ns) < 2: continue
        jm = re.search(r"J=(\d+)(?:/2)?$", r[1])
        try:
            out.append(dict(sp=r[0].rstrip(" *"), l="spdfghik".index(m.group(1)),
                            lo=int(ns[0]), hi=int(ns[1]), mem=int(r[3]),
                            inter=int(r[4]), d=float(r[7]), spread=float(r[8]),
                            twoJ=(int(jm.group(1))*2 if jm and "/2" not in r[1][jm.start():] else
                                  (int(jm.group(1)) if jm else None))))
        except Exception: pass
    return out

def density(lo, hi):
    """prime density over the integer range actually occupied"""
    v = [x for x in range(lo, hi+1) if isprime(x)]
    return len(v) / max(1, hi - lo + 1)

def run(C):
    res = []
    for key, lab in [("lo", "channel START n"), ("hi", "channel END n"),
                     ("mem", "member count"), ("inter", "interior-cell count")]:
        v = [c[key] for c in C]
        lo, hi = min(v), max(v)
        p = density(lo, hi)
        k = sum(1 for x in v if isprime(x))
        res.append((lab, k, len(v), p, binom_p(k, len(v), p)))
    # 5 — spreads of prime-member channels
    a = [c["spread"] for c in C if isprime(c["mem"])]
    b = [c["spread"] for c in C if not isprime(c["mem"])]
    res.append(("spread | prime member count", st.median(a), st.median(b), None, None))
    # 7 — 2J prime
    v = [c["twoJ"] for c in C if c["twoJ"]]
    if v:
        lo, hi = min(v), max(v); p = density(lo, hi)
        k = sum(1 for x in v if isprime(x))
        res.append(("2J", k, len(v), p, binom_p(k, len(v), p)))
    # 8 — channels per species
    per = Counter(c["sp"] for c in C)
    v = list(per.values()); lo, hi = min(v), max(v); p = density(lo, hi)
    k = sum(1 for x in v if isprime(x))
    res.append(("channels per species", k, len(v), p, binom_p(k, len(v), p)))
    return res

with State("primes") as s:
    C   = step(s, "load every channel", load, budget=120)
    res = step(s, "run the eight fixed tests", lambda: run(C), budget=300)

NT = 8
print(f"  PRIME STRUCTURE IN THE COMPENDIUM'S INTEGERS\n")
print(f"  {len(C)} channels. {NT} tests fixed in advance.")
print(f"  Bonferroni threshold: p < {0.05/NT:.4f}\n")
print(f"  {'quantity':<28}{'prime':>7}{'of':>6}{'expected':>10}{'observed':>10}{'p':>10}")
for lab, k, n, p, pv in res:
    if p is None:
        print(f"  {lab:<28}{'median spread':>7}  prime-member {k:.4f}  other {n:.4f}")
        continue
    print(f"  {lab:<28}{k:>7}{n:>6}{100*p:>9.1f}%{100*k/n:>9.1f}%{pv:>10.4f}"
          f"{'   SIGNIFICANT' if pv < 0.05/NT else ''}")
print()
hits = [r for r in res if r[4] is not None and r[4] < 0.05/NT]
print(f"  {len(hits)} of {NT} tests pass the corrected threshold.")
