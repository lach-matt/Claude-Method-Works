#!/usr/bin/env python3
"""DOCKET 67 -- rederive for hep-th/0302039#seciv (Popov Sec. IV).

WHAT CAN BE CHECKED HERE, AND WHAT CANNOT.
  Popov's Sec. IV text was NOT readable in this run (alphaXiv quota exceeded;
  arxiv.org, osti.gov, journals.aps.org EGRESS_BLOCKED).  So Popov's
  high/low-frequency SPLIT and his statement that the high-frequency part is
  state-independent CANNOT be checked against his text here.

  What IS checkable is a NECESSARY condition on the tree's reading:
  the expression the tree calls "the AHS expression" / Popov's (T)^(4) --
  Popov (B1)-(B3) at xi = 1/6, m = 0 as TRANSCRIBED in hpscentre.build()
  (the tree's transcription, not re-read against Popov here) -- must be
    C1  a LOCAL functional of the metric alone: no symbol that could carry a
        state (no temperature, no occupation number, no boundary datum);
        its only free parameter is the additive constant in Popov's log
        ln|4u0^2/(m_DS^2 r^2)| (the arbitrary scale);
    C2  covariantly conserved IDENTICALLY for arbitrary f(l), r(l) -- a part
        that is to stand on its own, independent of the state carried by the
        remainder, must be separately conserved (else the remainder must
        compensate and the split is not state-independent);
    C3  its scale-dependent (log) part separately conserved AND traceless,
        since the additive constant is arbitrary.
  Popov's printed (B3) carries M3 (hpscentre.py:150-153); C2 is run on the
  printed Popov (expected to FAIL) and with M3 restored (expected to PASS).
    C4  ILLUSTRATION ONLY, not Popov's argument: for thermal states in flat
        space the fraction of rho carried by modes above omega_c falls as
        ~ x^3 e^-x (x = omega_c/T); state dependence concentrates at low
        frequency.  This checks the MECHANISM the tree's sentence invokes,
        not Popov's derivation.
Imports hpscentre.py read-only by path; writes nothing into the tree.
"""
import importlib.util, sys, math, time
import sympy as sp

TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)
spec = importlib.util.spec_from_file_location("hpscentre", TREE + "/hpscentre.py")
H = importlib.util.module_from_spec(spec); spec.loader.exec_module(H)

ok = True
def chk(name, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

t0 = time.time()
S = H.build(sp)
l = S['l']; f, f1 = S['F'][0], S['F'][1]; r, r1 = S['R'][0], S['R'][1]
C = sp.Symbol('C_scale')           # the arbitrary additive constant of Popov's log
Lf = sp.log(f)

def div(T):
    tt, ll, th = T
    return sp.simplify(sp.expand(sp.diff(ll, l) + f1/(2*f)*(ll - tt) + 2*r1/r*(ll - th)))

pop = S['popov']                   # ((b1n/d, b1l/d), (b2n/d, b2l/d), (b3n/d, b3l/d))
d = r**8*f**4
M3 = -21*f1**4/f**4                # Popov-sign term dropped from (B3) at xi=1/6 (hpscentre.py:150-153)

def popov_T(fix_m3):
    out = []
    for i, (n, lg) in enumerate(pop):
        if fix_m3 and i == 2:
            lg = lg + M3
        # Popov: n + ln(4 w0^2/(m^2 f)) * lg = n + (C - ln f) * lg
        out.append(n + (C - Lf)*lg)
    return tuple(out)

# C1: free symbols
Tfix = popov_T(True)
fs = set().union(*[e.free_symbols for e in Tfix]) - {l}
funcs = set().union(*[e.atoms(sp.Function) for e in Tfix])
fnames = sorted({type(a).__name__ for a in funcs if isinstance(a, sp.core.function.AppliedUndef)})
print("free symbols besides l:", fs, "; undefined functions:", fnames)
chk("C1 only metric functions f, r and the arbitrary log constant appear", fs == {C} and fnames == ['f', 'r'])

# C2: conservation
dprint = div(popov_T(False))
dfix = div(Tfix)
chk("C2a Popov (B1)-(B3) AS PRINTED (M3) is NOT conserved", dprint != 0)
chk("C2b Popov with M3 restored is conserved identically (arbitrary f, r, C)", dfix == 0)

# C3: log part separately conserved and traceless
Tlog = tuple(lg + (M3 if i == 2 else 0) for i, (n, lg) in enumerate(pop))
chk("C3a scale (log) part conserved on its own", div(Tlog) == 0)
tr = sp.simplify(sp.expand(Tlog[0] + Tlog[1] + 2*Tlog[2]))
chk("C3b scale (log) part traceless (T^t_t + T^l_l + 2 T^th_th = 0)", tr == 0)

# cross-check: Popov (M3 restored) equals HPS conserved reading up to the log sign convention
Th = H.source(sp, S, H.CONSERVED)
same = all(sp.simplify(sp.expand((Tfix[i].subs(C, 0)) - Th[i])) == 0 for i in range(3))
chk("X  Popov(M3 restored, C=0) == HPS conserved reading (independent printing)", same)

# C4: illustration: thermal fraction above cutoff
import math
def frac_above(x):
    # int_x^inf u^3/(e^u-1) du / (pi^4/15), series sum_k e^{-kx}(x^3/k + 3x^2/k^2 + 6x/k^3 + 6/k^4)
    s = sum(math.exp(-k*x)*(x**3/k + 3*x**2/k**2 + 6*x/k**3 + 6/k**4) for k in range(1, 200))
    return s/(math.pi**4/15)
for x in (1, 5, 10, 20, 40):
    print("  thermal rho fraction above omega_c = %2d T : %.3e" % (x, frac_above(x)))
chk("C4 (illustration) thermal fraction above 20 T < 1e-4, above 40 T < 1e-12",
    frac_above(20) < 1e-4 and frac_above(40) < 1e-12)

print("elapsed %.1f s" % (time.time() - t0))
print("RESULT:", "ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
