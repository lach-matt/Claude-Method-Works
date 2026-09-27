#!/usr/bin/env python3
"""DOCKET 67 -- audit of gr-qc/9607003 Sec. 4, the curved-spacetime / boundary scope remark.

The result is an ARGUED EXTRAPOLATION, not a theorem, so what is checkable is:
  T  the tree's quotation (achievable.py:226-230) against the source page text;
  C  the boundary clause the tree drops is load-bearing: exact Casimir cases where the flat
     QI holds only for t0 below a multiple of the plate separation / identification length;
  K  Kontou & Olum arXiv:1410.0665 Eq. (130), the later PROOF (first order in curvature):
     its leading Gaussian term re-derived, and its small-curvature condition evaluated on the
     corridor numbers noise.py uses (b/l_G)^2 = 6 (M/b)/(a/b)^3;
  G  guards: each check is shown able to fail (a perturbed input flips it).
Exit 0 iff every check passes.  sympy + stdlib only.
"""
import hashlib, os, re, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src", "gr-qc_9607003.alphaxiv_pages.txt")
fails = []

def chk(tag, cond, msg):
    print(("PASS " if cond else "FAIL ") + tag + ": " + msg)
    if not cond:
        fails.append(tag)

# ---------------------------------------------------------------- T: the quotation
TREE_QUOTE = ("we recently argued that such bounds should also hold in a curved spacetime "
              "and/or one with boundaries, IF the sampling time is restricted to be much "
              "smaller than the smallest local radius of curvature.")
if os.path.exists(SRC):
    raw = open(SRC, encoding="utf-8").read()
    print("source text md5", hashlib.md5(raw.encode()).hexdigest(), "(alphaXiv page text, gr-qc/9607003v2)")
    pages = dict(re.findall(r'<page num="(\d+)">(.*?)</page>', raw, re.S))
    flat = lambda s: re.sub(r"\s+", " ", s).strip()
    p11, p2 = flat(pages["11"]), flat(pages["2"])
    SRC_SENT = ("Recently we argued that such bounds should also hold in a curved spacetime "
                "and/or one with boundaries, if the sampling time is restricted to be much "
                "smaller than the smallest local radius of curvature and/or the distance to "
                "any boundaries in the spacetime [23].")
    chk("T1", SRC_SENT in p11, "p.11 prints the full sentence (with the boundary clause and ref [23])")
    chk("T2", flat(TREE_QUOTE).lower() not in p11.lower(),
        "the tree's quoted string is NOT a verbatim substring of p.11 (case-folded)")
    chk("T3", "we recently argued that such bounds" not in p11.lower() and "Recently we argued" in p11,
        "word order: source 'Recently we argued', tree 'we recently argued'")
    chk("T4", "we recently argued [23]" in p2,
        "the tree's word order is p.2's ('we recently argued [23] that if one is willing to restrict ...')")
    dropped = "and/or the distance to any boundaries in the spacetime"
    chk("T5", dropped in p11 and dropped not in TREE_QUOTE,
        "DROPPED CLAUSE: '" + dropped + "' -- tree closes the quote with a period, no ellipsis")
    chk("T6", "An explicit example of the validity of this assumption has been given in Ref. [24]" in p11,
        "source calls it an 'assumption' and cites one worked case [24] (static RW); tree omits it")
    chk("T7", "we proved that the inequality Eq. (1) holds in the" in p2,
        "p.2-3 also cites a proved Casimir case (sampling times << plate distance); tree omits it")
    chk("T8", "argued" in p11 and "argued" in p2,
        "the tree's load-bearing word 'argued' is the source's own, in both places")
    # guard: the substring test can fail
    chk("G-T", SRC_SENT.replace("[23]", "[22]") not in p11, "guard: a one-character edit is detected")
else:
    print("SKIP T*: source text not present at", SRC)

# ---------------------------------------------------------------- C: boundary clause is load-bearing
t0, a, L = sp.symbols("t0 a L", positive=True)
# EM field between perfectly conducting plates, separation a: constant rho = -pi^2/(720 a^4)
# (gauge invariant, position independent); source Eq. (48) EM QI: rho_hat >= -3/(16 pi^2 t0^4).
# A constant density's Lorentzian average is itself, so the flat EM QI holds iff t0 <= cap_EM.
rho_EM = -sp.pi**2 / (720 * a**4)
cap_EM = sp.solve(sp.Eq(rho_EM, -sp.Rational(3, 16) / (sp.pi**2 * t0**4)), t0)[0]
cap_EM_s = sp.nsimplify(sp.simplify(cap_EM / a))
chk("C1", sp.simplify(cap_EM / a - (sp.Rational(135) / sp.pi**4) ** sp.Rational(1, 4)) == 0,
    "EM plates: flat QI (Eq.48) holds iff t0 <= (135/pi^4)^(1/4) a = %.6f a" % float(cap_EM / a))
# for t0 = 2 a the flat bound is VIOLATED by a static observer between plates
lhs = rho_EM.subs(a, 1); rhs = (-sp.Rational(3, 16) / (sp.pi**2 * t0**4)).subs(t0, 2)
chk("C2", bool(lhs < rhs), "t0 = 2a: rho = %.5f < bound %.5f -> flat QI fails without the boundary clause"
    % (float(lhs), float(rhs)))
# periodic identification (no boundary, no curvature): one real massless scalar, rho = -pi^2/(90 L^4);
# source Eq. (1): rho_hat >= -3/(32 pi^2 t0^4)
rho_P = -sp.pi**2 / (90 * L**4)
cap_P = sp.solve(sp.Eq(rho_P, -sp.Rational(3, 32) / (sp.pi**2 * t0**4)), t0)[0]
chk("C3", abs(float(cap_P / L) - (270 / (32 * float(sp.pi)**4)) ** 0.25) < 1e-12,
    "periodic scalar: flat QI holds iff t0 <= %.6f L -- a TOPOLOGY scale, named in neither of the source's"
    " two clauses (curvature radius, boundary distance)" % float(cap_P / L))
chk("G-C", not bool((rho_EM.subs(a, 1)) < (-sp.Rational(3, 16) / (sp.pi**2 * t0**4)).subs(t0, sp.Rational(1, 2))),
    "guard: at t0 = a/2 the EM plate density SATISFIES the flat bound (check can go either way)")

# ---------------------------------------------------------------- K: Kontou-Olum 1410.0665 Eq. (130)
t = sp.symbols("t", real=True)
g = sp.exp(-t**2 / t0**2)
I1 = sp.simplify(sp.integrate(sp.diff(g, t, 2)**2, (t, -sp.oo, sp.oo)))
chk("K1", sp.simplify(I1 - 3 * sp.sqrt(sp.pi / 2) / t0**3) == 0,
    "INT (g'')^2 dt = 3 sqrt(pi/2)/t0^3 = %.4f/t0^3 -- K-O Eq.(130)'s leading 3.76 (flat Fewster-Eveson term)"
    % float(3 * sp.sqrt(sp.pi / 2)))
chk("K1b", abs(float(3 * sp.sqrt(sp.pi / 2)) - 3.76) < 0.005, "matches the printed 3.76 to its 3 figures")
# corridor numbers (achievable.py window; noise.py's l_G): (b/l_G)^2 = 6 (M/b)/(a/b)^3
m, ab, G, c, b = sp.symbols("m ab G c b", positive=True)
M = m * b * c**2 / G
V = sp.Rational(4, 3) * sp.pi * (ab * b)**3
D = M * c**2 / V                               # achievable.required_density
lG_m2 = 8 * sp.pi * G * D / c**4               # G_00 = 8 pi G D / c^4 = l_G^-2
ratio2 = sp.simplify(b**2 * lG_m2)
chk("K2", sp.simplify(ratio2 - 6 * m / ab**3) == 0, "(b/l_G)^2 = 6 (M/b)/(a/b)^3 symbolically (noise.py:182)")
r2 = ratio2.subs({m: sp.Rational(5, 1000), ab: sp.Rational(2, 100)})
chk("K3", r2 == 3750, "at M/b = 5e-3, a/b = 0.02: (b/l_G)^2 = %s, b/l_G = %.3f" % (r2, float(sp.sqrt(r2))))
# K-O Eq.(3) bounds EVERY Fermi-frame Ricci component by R_max.  |G_00| <= |R_00| + |R|/2 and
# |R| <= 4 R_max in an orthonormal frame, so R_max >= G_00/3 = 1/(3 l_G^2).  Ratio of K-O's first
# curvature term to the flat term at sampling width t0:  2.63 R_max t0^2 / 3.76.
def ko_ratio_lower(t0_over_lG):
    return 2.63 * (t0_over_lG**2 / 3.0) / 3.76
rb = ko_ratio_lower(float(sp.sqrt(r2)))
chk("K4", rb > 100, "t0 = b: K-O first-order curvature term >= %.0f x the flat term -- first-order expansion"
    " invalid; sampling at b is outside the PROVED small-curvature regime (supports noise.py:185-187)" % rb)
chk("K5", 0.2 < ko_ratio_lower(1.0) < 0.3 and ko_ratio_lower(0.1) < 0.003,
    "t0 = l_G: ratio >= %.3f (not small); t0 = 0.1 l_G: >= %.5f (small)" % (ko_ratio_lower(1.0), ko_ratio_lower(0.1)))
chk("G-K", not (ko_ratio_lower(0.01) > 100), "guard: at t0 = 0.01 l_G the lower bound is small (K4 can fail)")

print()
print("RESULT:", "ALL PASS" if not fails else "FAILED " + ",".join(fails))
sys.exit(1 if fails else 0)
