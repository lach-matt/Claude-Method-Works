#!/usr/bin/env python3
"""DOCKET 67 -- composite audit: ICRP reference adult x CI chondrite x stellar photosphere.

Re-derives D25's two figures (ledger.py:674-677) independently from the cited
tables, then asks which of them move with data READ or CARRIED here.
Statuses of every input are printed.  Nothing in research/ is written.
"""
import csv, math, os, sys
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import stockgate as sg
import sympy as sp

D67 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
PYPI = os.path.join(D67, "pypi")
fails = []
def chk(name, got, want, tol=None):
    ok = (got == want) if tol is None else abs(got - want) <= tol * max(1.0, abs(want))
    print(("PASS " if ok else "FAIL ") + name + " :: got %r want %r" % (got, want))
    if not ok: fails.append(name)

A = sg.ATOMIC_MASS
# ------------------------------------------------------------------ 1. tree figures, by import
e1, f1 = sg.binding_under("as-composed 59", "CI chondrite")
e2, f2 = sg.binding_under("as-composed 59", "stellar photosphere")
chk("tree CI binder", e1, "P"); chk("tree CI factor 10.70", round(f1, 2), 10.70)
chk("tree photosphere binder", e2, "P"); chk("tree photosphere factor 1910.9", round(f2, 1), 1910.9)

# ------------------------------------------------------------------ 2. independent recompute from raw tables
grams = {}
for d in (sg.HUMAN_G_BULK, sg.HUMAN_G_ESSENTIAL_TRACE, sg.HUMAN_G_INCIDENTAL):
    grams.update(d)
chk("payload has 59 elements", len(grams), 59)
tot = sum(grams.values())
pay = {e: g / tot for e, g in grams.items()}
def hybrid(tab):  # tab: e -> (phot, met); phot where determined else meteoritic
    n = {}
    for e, (ph, me) in tab.items():
        v = ph if ph is not None else me
        if v is not None and e in A: n[e] = 10 ** (v - 12)
    m = {e: n[e] * A[e] for e in n}; t = sum(m.values())
    return {e: v / t for e, v in m.items()}
def M(p, s):
    f = {e: (p[e] / s[e] if s.get(e, 0) > 0 else float("inf")) for e in p}
    r = sorted(f.items(), key=lambda kv: -kv[1])
    return r[0], r[1]
ph09 = hybrid(sg.A09)
(b, fb), (r, fr) = M(pay, ph09)
chk("recomputed photosphere binder P", b, "P"); chk("recomputed 1910.87", round(fb, 2), 1910.87)
chk("runner-up Li", r, "Li"); print("   Li/P ratio = %.5f" % (fr / fb))
(b, fb), (r, fr) = M(pay, sg.CHONDRITE)
chk("recomputed CI binder P", b, "P"); chk("recomputed CI 10.701", round(fb, 3), 10.701)
chk("CI runner-up N", r, "N"); print("   N/P ratio at CI = %.4f" % (fr / fb))

# ------------------------------------------------------------------ 3. sympy closed forms for the two flips
gLi, gP, gN, ALi, AP, dE, NCI, PCI = sp.symbols("g_Li g_P g_N A_Li A_P dE N_CI P_CI", positive=True)
# photosphere: f_Li/f_P = (gLi/gP) * (nP AP)/(nLi ALi) = (gLi/gP)*(AP/ALi)*10^(-dE), dE = eps_Li - eps_P
ratio = (gLi / gP) * (AP / ALi) * 10 ** (-dE)
crit = sp.solve(sp.Eq(ratio, 1), dE)[0]
critv = float(crit.subs({gLi: grams["Li"], gP: grams["P"], ALi: A["Li"], AP: A["P"]}))
chk("Li-over-P criterion eps_Li - eps_P < -4.3974", round(critv, 4), -4.3974)
# CI: f_N/f_P = (gN/gP)*(PCI/NCI); N binds iff NCI < PCI*gN/gP (mass fractions; stock normalisation cancels)
ncrit = sp.solve(sp.Eq((gN / gP) * (PCI / NCI), 1), NCI)[0]
chk("N-over-P CI crossover at tree P = 2400 ppm", round(float(ncrit.subs({gN: 1800, gP: 780, PCI: 1040}))), 2400)

# ------------------------------------------------------------------ 4. alternative data
# 4a AAG21 (Asplund, Amarsi & Grevesse 2021) Table 2, READ as the package data file exojax 2.6.0
aag = {}
with open(os.path.join(PYPI, "exojax/data/abundance/AAG2021.dat")) as fh:
    for line in fh:
        if line.startswith("#") or line.startswith("Number"): continue
        c = [x.strip() for x in line.split(",")]
        if len(c) < 5: continue
        def fl(x):
            try:
                v = float(x); return None if math.isnan(v) else v
            except ValueError: return None
        aag[c[1]] = (fl(c[2]), fl(c[4]))
chk("AAG21 Li phot 0.96", aag["Li"][0], 0.96); chk("AAG21 P phot 5.41", aag["P"][0], 5.41)
ph21 = hybrid(aag)
missing = sorted(e for e in pay if e not in ph21); print("   AAG21 hybrid lacks:", missing)
(b21, f21), (r21, fr21) = M(pay, ph21)
print("   AAG21 photosphere (full substitution): binder %s at %.1f, runner-up %s at %.1f (ratio %.4f)" % (b21, f21, r21, fr21, fr21 / f21))
chk("AAG21 hands the photosphere to Li", b21, "Li")
# only Li changed in A09:
t = dict(sg.A09); t["Li"] = (0.96, t["Li"][1])
(bL, fL), (rL, frL) = M(pay, hybrid(t))
print("   A09 with only Li -> 0.96: binder %s %.1f, %s %.1f" % (bL, fL, rL, frL))

# 4b CI compilations: PON14 and MS95 READ from pyrolite 0.3.7 data files; LBP25 N,P CARRIED from sibling audit
def pyro(fn):
    out = {}
    for row in csv.reader(open(os.path.join(PYPI, "pyrolite/data/geochem/refcomp", fn))):
        if len(row) < 3 or row[2] not in ("%", "ppm", "ppb"): continue
        try: v = float(row[1])
        except ValueError: continue
        out[row[0]] = v * {"%": 1e-2, "ppm": 1e-6, "ppb": 1e-9}[row[2]]
    return out
pon = pyro("CH_PalmeONeill2014.csv")
chk("PON14 N 2950 ppm", round(pon["N"] * 1e6), 2950); chk("PON14 P 985 ppm", round(pon["P"] * 1e6), 985)
def swapped(base, **kw):
    s = dict(base); s.update(kw); return s
cases = {
    "tree table (attrib. L03)": sg.CHONDRITE,
    "tree + L03 N,P (2940, 920; CARRIED)": swapped(sg.CHONDRITE, N=2940e-6, P=920e-6),
    "tree + PON14 N,P (READ pyrolite)": swapped(sg.CHONDRITE, N=pon["N"], P=pon["P"]),
    "tree + MS95 N,P (3180,1080 READ pyrolite, units flagged)": swapped(sg.CHONDRITE, N=3180e-6, P=1080e-6),
    "tree + LBP25 N,P (1965, 989; CARRIED)": swapped(sg.CHONDRITE, N=1965e-6, P=989e-6),
    "PON14 full table (READ pyrolite)": pon,
}
ci = {}
for k, s in cases.items():
    (bb, ff), (rr, fr_) = M(pay, s); ci[k] = (bb, ff)
    print("   CI %-58s binder %s %.3f  runner-up %s %.3f" % (k, bb, ff, rr, fr_))
chk("LBP25 N flips CI binder to N", ci["tree + LBP25 N,P (1965, 989; CARRIED)"][0], "N")
chk("PON14 keeps P", ci["tree + PON14 N,P (READ pyrolite)"][0], "P")
# PON14 2-sigma N band vs crossover at PON14 P
xo = 985 * 1800 / 780
print("   PON14 crossover %.0f ppm; PON14 N 2-sigma band %.0f-%.0f ppm" % (xo, 2950 - 885, 2950 + 885))
chk("PON14 2-sigma band spans the crossover", 2950 - 885 < xo < 2950 + 885, True)

# 4c payload: ICRP 110 whole-body bulk (CARRIED from sibling audit, computed there from Kanematsu arXiv:1508.00226)
icrp110 = {"H": 0.102, "C": 0.316, "N": 0.0240, "O": 0.528, "P": 0.00813, "Ca": 0.0153}
held = {e: v for e, v in pay.items() if e not in icrp110}
t_ = sum(held.values()) + sum(icrp110.values())
p110 = {e: v / t_ for e, v in list(held.items()) + list(icrp110.items())}
(bx, fx), (rx, frx) = M(p110, ph09); print("   ICRP110 bulk vs A09 photosphere: %s %.0f, %s %.0f" % (bx, fx, rx, frx))
(by, fy), (ry, fry) = M(p110, sg.CHONDRITE); print("   ICRP110 bulk vs tree CI: %s %.2f, %s %.2f" % (by, fy, ry, fry))
chk("ICRP110 bulk hands photosphere to Li", bx, "Li"); chk("ICRP110 bulk hands CI to C", by, "C")

# ------------------------------------------------------------------ 5. sensitivity of the payload's Li and P
def flip_scale(el, dest):
    lo, hi = 0.2, 5.0
    base = M(pay, dest)[0][0]
    for _ in range(80):
        mid = math.sqrt(lo * hi); g = dict(grams); g[el] *= mid; t = sum(g.values())
        b_ = M({e: v / t for e, v in g.items()}, dest)[0][0]
        if el == "Li":
            lo, hi = (mid, hi) if b_ == base else (lo, mid)
        else:
            lo, hi = (lo, mid) if b_ == base else (mid, hi)
    return mid
sLi = flip_scale("Li", ph09); sP = flip_scale("P", ph09); sPc = flip_scale("P", sg.CHONDRITE)
print("   payload Li flips photosphere above %.3f mg (x%.4f)" % (7 * sLi, sLi))
print("   payload P flips photosphere below %.1f g (x%.4f); flips CI below %.1f g (x%.4f)" % (780 * sP, sP, 780 * sPc, sPc))

# ------------------------------------------------------------------ 6. magnitude envelope over every case run
mags_ph = [fb for fb in (f2, f21, fL, fx)]
mags_ci = [v[1] for v in ci.values()] + [fy]
print("   photosphere factor envelope %.0f - %.0f; CI factor envelope %.2f - %.2f" % (min(mags_ph), max(mags_ph), min(mags_ci), max(mags_ci)))
chk("photosphere magnitude within 1.25x of 1910.9", max(mags_ph) / min(mags_ph) < 1.25, True)
chk("CI magnitude stays order 10 kg/kg", 5 < min(mags_ci) and max(mags_ci) < 20, True)

# ------------------------------------------------------------------ 7. z3: the gate is a principal ideal (tree hypothesis, checked here)
try:
    import z3
    n = 3
    m = [z3.Real("m%d" % i) for i in range(n)]; mm = [z3.Real("mm%d" % i) for i in range(n)]
    s = [z3.Real("s%d" % i) for i in range(n)]; B = z3.Real("B")
    ok = lambda v: z3.And(*[z3.And(v[i] >= 0, v[i] <= B * s[i]) for i in range(n)])
    sol = z3.Solver(); sol.add(B > 0, *[si > 0 for si in s])
    # down-set and join-closed, negated
    sol.add(z3.Or(z3.And(ok(m), z3.And(*[z3.And(mm[i] >= 0, mm[i] <= m[i]) for i in range(n)]), z3.Not(ok(mm))),
                  z3.And(ok(m), ok(mm), z3.Not(ok([z3.If(m[i] >= mm[i], m[i], mm[i]) for i in range(n)])))))
    r = sol.check(); chk("z3: assemblable set down-set and join-closed (UNSAT of negation)", str(r), "unsat")
except ImportError:
    print("SKIP z3 not installed")

print("\nRESULT: %d failure(s)" % len(fails)); sys.exit(1 if fails else 0)
