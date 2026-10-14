#!/usr/bin/env python3
"""DOCKET 67 audit 0708.2450-conclusion -- re-derivation / machine checks.

The audited result is an EXTRAPOLATION (FO 0708.2450 Sec. 6: an absolute QEI for the
non-minimally coupled (NMC) field is 'expected', not derived) plus a literature-search
NOT-FOUND recorded in qeihps.py:89-92, 511-512.  Neither an expectation nor a search is
a theorem, so what is checkable here is:

 (A) the quote: the tree's paraphrase against the cached full text of 0708.2450v2
     (and the later-literature sentences the grade rests on, against their cached texts);
 (B) the root cause the later literature names for why no absolute NMC QEI exists
     (Kontou-Sanders 2003.01815 p.~32: 'the operator T^split_ab is not of positive type';
     Kontou 2405.05963: same) -- machine-checked on the Minkowski massless NMC energy
     density: the point-split kernel acting on one-particle wavefunctions h is
         K(k,k') = [w w' + k.k' + m^2 + 2 xi |k-k'|^2] / (2 sqrt(w w')),
     from :rho: = |dF/dt|^2 + |grad F|^2 + m^2|F|^2 - 2 xi Lap|F|^2, rho = rho_min - xi Lap phi^2
     (signature (+,-,-,-), Birrell-Davies/FO convention).  FS's absolute method needs K
     of positive type; we show it is not, for EVERY xi > 0 (s-wave 2x2 minor, closed form),
     and positive semidefinite at xi = 0.
 (C) a numeric cross-check on random 3-vectors (no angular averaging) for small xi.

What this does NOT do: it does not prove that no absolute NMC QEI exists (a failure of
one method's hypothesis is not a non-existence proof), and it does not re-run the
literature search (alphaXiv quota exhausted this session; arxiv.org 403 at the proxy).
"""
import hashlib, os, sys
import sympy as sp
import numpy as np

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src")
ok = True

def check(label, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + label)
    ok = ok and bool(cond)

def flat(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return " ".join(fh.read().split())

# ---------------- (A) quotes at source ----------------
SRC = {
    "0708.2450v2": ("0708.2450.txt", "5ef2edeec5aa48e27368f476cb65da2a", [
        "our general QEI is of the so-called ‘difference’ type: it constrains the normal ordered energy density rather than the (Hadamard) renormalised version.",
        "This restriction has recently been removed for the minimally coupled field in [31] to obtain an ‘absolute’ QEI; one would expect that this can also be adapted to the non-minimally coupled field.",
        "[31] C.J. Fewster and C.J. Smith, gr-qc/0702056 (2007).",
    ]),
    "2003.01815v2 (Kontou-Sanders review)": ("casmag/all/2003.01815v2.txt", "a647c534717b5b5b6ef5e7c0a9c54b2c", [
        "To date no absolute QEIs have been derived for the non-minimally coupled scalar field.",
        "The root cause is that the operator T split ab (see (50)) is not of positive type or symmetric.",
        "We will call such QEIs absolute",
        "this only yields an absolute QEI when the lower bound is local and covariant.",
    ]),
    "2309.10848 (FFKP)": ("2309.10848.txt", "4f31876842f625e48506444afd216ee0", [
        "We note that the derivation is for a difference QEIs unlike the absolute one that was possible for the minimally coupled field.",
    ]),
    "2405.05963v2 (Kontou 2024)": ("casmag/all/2405.05963v2.txt", "7b8e441a1e90121782aafa8501188592", [
        "This is not true, for example, for the T split operator of nonminimally coupled fields, so these inequalities cannot be used in this case. State-dependent bounds have been derived for the nonminimally coupled field [17,29,30].",
    ]),
    "1809.05047v2 (Fewster-Kontou) -- the CONTRARY sentence": ("casmag/all/1809.05047v2.txt", "aa6f78fe875ce6b25d9233db9a745ae6", [
        "However, as shown in Ref. [28], nonminimally coupled fields obey state dependent QWEIs of both absolute and difference types.",
        "[28] C. J. Fewster, Gen. Rel. Grav. 39, 1855 (2007), arXiv:math-ph/0611058 [math-ph].",
    ]),
    "math-ph/0611058v2 (partial cache: pp.1-2,6-9,22,24-27)": ("casmag/all/math-ph_0611058v2.txt", "bdc1fee5f1b0529ace9e334e52961c2f", [
        "Our purpose in this Appendix is to illustrate the discussion of state-dependent QEIs with an example to show the type of state-dependence that enters in the difference QEI obtained in [22] by the present author and Osterbrink for the case 0 ≤ ξ ≤ 1/4.",
    ]),
}
for name, (rel, md5, quotes) in SRC.items():
    p = os.path.join(D, rel)
    if not os.path.exists(p):
        check("%s: cached text present" % name, False); continue
    h = hashlib.md5(open(p, "rb").read()).hexdigest()
    check("%s: md5 %s" % (name, md5), h == md5)
    t = flat(p)
    for q in quotes:
        check("%s: quote found: %.70s..." % (name, q), " ".join(q.split()) in t)

# The tree's paraphrase vs FO: 'can also be adapted' is FO's phrase verbatim; 'expected' is
# FO's 'one would expect'; 'NOT DONE' -- FO derive only the difference type (the sentence before).
check("tree phrase 'can also be adapted' is verbatim FO", "can also be adapted" in flat(os.path.join(D, "0708.2450.txt")))

# ---------------- (B) closed form: s-wave minor of the NMC kernel ----------------
xi, k1, k2, r = sp.symbols("xi k1 k2 r", positive=True)
xir = sp.symbols("xi_r", real=True)
def Ks(a, b, x):
    # massless, angular average over directions: <k.k'> = 0, <|k-k'|^2> = a^2 + b^2
    return (a*b + 2*x*(a**2 + b**2)) / (2*sp.sqrt(a*b))
M = sp.Matrix([[Ks(k1, k1, xir), Ks(k1, k2, xir)], [Ks(k2, k1, xir), Ks(k2, k2, xir)]])
det = sp.simplify(M.det())
target = -xir*(k1 - k2)**2 * (k1*k2 + xir*(k1 + k2)**2) / (k1*k2)
check("s-wave det == -xi (k1-k2)^2 (k1 k2 + xi (k1+k2)^2)/(k1 k2)", sp.simplify(det - target) == 0)
print("   det =", sp.factor(det))
# sign: xi > 0, k1 != k2  =>  det < 0  => a negative eigenvalue => not of positive type
detpos = target.subs(xir, xi)
# det = -[xi (k1-k2)^2] * [(k1 k2 + xi (k1+k2)^2)/(k1 k2)]: first bracket > 0 for xi > 0, k1 != k2
check("det/(-xi (k1-k2)^2) is the positive factor", sp.simplify(detpos / (-xi*(k1-k2)**2) - (k1*k2 + xi*(k1+k2)**2)/(k1*k2)) == 0)
check("factor (k1 k2 + xi (k1+k2)^2)/(k1 k2) > 0 for xi > 0", sp.ask(sp.Q.positive((k1*k2 + xi*(k1+k2)**2)/(k1*k2))) is True)
check("at xi = 0 the minor vanishes (rank one, positive semidefinite)", sp.simplify(target.subs(xir, 0)) == 0)
for xv in [sp.Rational(1, 1000), sp.Rational(1, 6), sp.Rational(1, 4), 1]:
    val = target.subs({xir: xv, k1: 1, k2: 2})
    check("xi = %s, (k1,k2)=(1,2): det = %s < 0" % (xv, sp.nsimplify(val)), val < 0)

# ---------------- (C) numeric, no angular averaging ----------------
rng = np.random.default_rng(67)
def kern(ks, x, m=0.0):
    w = np.sqrt((ks**2).sum(1) + m*m)
    kk = ks @ ks.T
    d2 = ((ks[:, None, :] - ks[None, :, :])**2).sum(-1)
    return (np.outer(w, w) + kk + m*m + 2*x*d2) / (2*np.sqrt(np.outer(w, w)))
ks = rng.normal(size=(40, 3))
for x in [0.0, 1e-3, 1/6, 1/4]:
    ev = np.linalg.eigvalsh(kern(ks, x))
    if x == 0.0:
        check("xi = 0: min eigenvalue %.3e >= -1e-12 (positive type)" % ev.min(), ev.min() > -1e-12)
    else:
        check("xi = %.4g: min eigenvalue %.3e < 0 (not positive type)" % (x, ev.min()), ev.min() < 0)
ev = np.linalg.eigvalsh(kern(ks, 1/6, m=1.0))
check("massive m=1, xi = 1/6: min eigenvalue %.3e < 0" % ev.min(), ev.min() < 0)

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
