#!/usr/bin/env python3
"""DOCKET 67 audit: o5-pass-literature-tally (throatmass.py SELF_CONSISTENT_FAMILIES).

Re-derives what is finite in the DOCKET 62 O5 tally '6 self-consistent families,
0 with m(r) < 0':
  C1  the counts, re-parsed from the journal's 'SIX FAMILIES RETURNED' block and
      re-derived from throatmass.py's list (READ data: nothing here can move it)
  C2  the Misner-Sharp mass of each family's CLASS / assumed background (sympy):
      is m < 0 even possible in that class?
  C3  KS eq. (61)-(63) and Garattini eqs. (78)-(79) arithmetic, from the banked text
  C4  classification: sign of m forced by class/background vs. decided by dynamics
Reads research/warp-drive only (never writes).  sympy only.
"""
import os, re, sys, json
import sympy as sp

TREE = "/home/user/Claude-Method-Works/research/warp-drive"
SCR = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847"
JOURNAL = SCR + "/tasks/wq1u9n1d8.output"
SRC = SCR + "/scratchpad/d67/src/casmag/all/"
ok = True
def chk(label, cond, got=""):
    global ok
    ok &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "XX", label, got))

# ------------------------------------------------------------------ C1
print("C1  THE COUNTS")
s = open(JOURNAL).read()
i = s.find('"known_self_consistent_solutions"')
line = s[i:s.find("\n", i)].rstrip(",")
block = json.loads("{" + line + "}")["known_self_consistent_solutions"]
entries = re.findall(r"^(\d)\. ([A-Z][^\n]*)", block, re.M)
chk("journal block lists six numbered families", len(entries) == 6, [e[0] for e in entries])
tally = re.findall(r"solutions found with (m\(r\) < 0 anywhere|negative ADM mass)\s*:\s*(\d+)", block)
chk("journal tally: m(r)<0 anywhere = 0, negative ADM = 0",
    tally == [("m(r) < 0 anywhere", "0"), ("negative ADM mass", "0")], tally)
sys.path.insert(0, TREE)
import throatmass as T
chk("throatmass list length 6 == journal", T.SELF_CONSISTENT_FAMILIES_RETURNED == 6)
chk("throatmass FAMILIES_WITH_NEGATIVE_MASS == 0", T.FAMILIES_WITH_NEGATIVE_MASS == 0)
chk("throatmass THROAT_FAMILIES == 3", T.THROAT_FAMILIES == 3)
# which families did the pass READ at source? (field 2)
read_src = [f[0] for f in T.SELF_CONSISTENT_FAMILIES if "read" in f[2].lower() and "not" not in f[2].lower()]
print("     families the pass marks read at source:", read_src)

# ------------------------------------------------------------------ C2
print("\nC2  MISNER-SHARP MASS OF EACH FAMILY'S CLASS (m = (R/2)(1 - g^ab dR dR), G = c = 1)")
t, x, chi, l, a0 = sp.symbols("t x chi l a_0", positive=True)
A = sp.Function("a", positive=True)(t)
# flat FLRW  ds^2 = -dt^2 + a^2 (dx^2 + x^2 dOmega^2), areal R = a x
R = A * x
grad2 = -sp.diff(R, t) ** 2 + sp.diff(R, x) ** 2 / A ** 2
m_flrw = sp.simplify(R / 2 * (1 - grad2))
H = sp.diff(A, t) / A
chk("flat FLRW: m = R^3 H^2 / 2  (>= 0 for EVERY state: m<0 impossible in class)",
    sp.simplify(m_flrw - R ** 3 * H ** 2 / 2) == 0, m_flrw)
# Einstein static universe  ds^2 = -dt^2 + a0^2 (dchi^2 + sin^2 chi dOmega^2)
R = a0 * sp.sin(chi)
m_esu = sp.simplify(R / 2 * (1 - sp.diff(R, chi) ** 2 / a0 ** 2))
chk("ESU R x S^3: m = (a0/2) sin^3 chi  (>= 0 on [0,pi]: m<0 impossible in class)",
    sp.simplify(m_esu - a0 * sp.sin(chi) ** 3 / 2) == 0, m_esu)
# Garattini eq. (16): Ellis background, r^2 = l^2 + r_t^2, proper-distance gauge g^ll = 1
rt = sp.Symbol("r_t", positive=True)
r = sp.sqrt(l ** 2 + rt ** 2)
m_ellis = sp.simplify(r / 2 * (1 - sp.diff(r, l) ** 2))
chk("Garattini (Ellis, ASSUMED not solved): m = r_t^2/(2r) > 0, ADM mass 0",
    sp.simplify(m_ellis - rt ** 2 / (2 * r)) == 0 and sp.limit(m_ellis, l, sp.oo) == 0, m_ellis)
# KS eq. (8): r = |rho| + a, flat on both sides
rho, a = sp.symbols("rho a", positive=True)
r_plus = rho + a
m_ks = sp.simplify(r_plus / 2 * (1 - sp.diff(r_plus, rho) ** 2))
chk("KS short-throat flat-space: m = 0 for rho != 0 (ADM mass 0, not r_0/2 > 0)", m_ks == 0, m_ks)
# KS eq. (61)-(62): E = -(1/2) INT G^t_t r^2 drho, G^t_t = 2r''/r + (r'^2-1)/r^2,
# r' = sgn rho, r'' = 2 delta(rho): the only contribution is the delta term.
rr = sp.Symbol("rr")
E_ks = -sp.Rational(1, 2) * sp.integrate(2 * 2 * sp.DiracDelta(rr) * (sp.Abs(rr) + a), (rr, -sp.oo, sp.oo))
chk("KS eq. (62) reproduced: total energy E = -2a (c^4/G) -- NEGATIVE, printed by KS",
    sp.simplify(E_ks + 2 * a) == 0, E_ks)
# HPS throat (proper-distance gauge): m = r_0/2, m'(0)=0, m''(0)=0 when r''(0)=0
r0, aa, cc = sp.symbols("r_0 aa cc", real=True)
rs = r0 + aa * l ** 2 / 2 + cc * l ** 4 / 24
ms = sp.series(rs * (1 - sp.diff(rs, l) ** 2) / 2, l, 0, 3).removeO()
chk("HPS throat: m(0) = r_0/2 > 0; m''(0) = aa(1-2 r_0 aa)/2 -> 0 at HPS r''(0)=0",
    sp.simplify(ms.coeff(l, 0) - r0 / 2) == 0 and
    sp.simplify(2 * ms.coeff(l, 2) - aa * (1 - 2 * r0 * aa) / 2) == 0)
# flare: oscillating R(l) ~ l + rho(l): |r'| > 1 wherever rho' > 0 on the rising branch
eps, w = sp.symbols("epsilon omega", positive=True)
rf = l + eps * sp.sin(w * l)
mf = sp.simplify(rf / 2 * (1 - sp.diff(rf, l) ** 2))
chk("HPS flare form R ~ l + bounded wiggle (HPS p.8): m < 0 wherever the wiggle's slope > 0",
    sp.simplify(mf.subs(l, 0) ) == 0 and float(mf.subs({l: 2 * sp.pi, eps: sp.Rational(1, 10), w: 1})) < 0,
    "m(2pi; eps=0.1, w=1) = %.4f" % float(mf.subs({l: 2 * sp.pi, eps: sp.Rational(1, 10), w: 1})))

# ------------------------------------------------------------------ C3
print("\nC3  PRINTED ARITHMETIC FROM THE BANKED SOURCE TEXT")
ks = open(SRC + "hep-th_0202068v1.txt").read()
g = open(SRC + "gr-qc_0501105v1.txt").read()
chk("KS text carries 'Note that the total energy is negative.'", "Note that the total energy is negative." in ks)
chk("KS text carries 'if exists' (conditional self-consistency)", "semiclassical wormhole, if exists" in ks)
f = 4e-4
a_lp = (f / 2) ** 0.5
chk("KS eq. (63)-(64): a = l_P sqrt(f/2), f ~ 4e-4 -> 0.01414 l_P (printed 0.0141)", abs(a_lp - 0.0141) < 1e-4, a_lp)
chk("KS eq. (65): m = beta_a/a = 0.16/0.0141 -> %.2f m_P (printed 11.35; rounding of f, beta)" % (0.16 / 0.0141),
    abs(0.16 / 0.0141 - 11.35) / 11.35 < 0.01)
chk("Garattini eq. (40)-(41): classical energy pi r_t/(2G) > 0 set equal to -E_TT (integrated only)",
    "self-consistent equation for TT tensors" in g)
chk("Garattini (78)x(79): 1.158822606 * 0.3860531213 = 0.4473670842 (r_t scales as sqrt(G_0))",
    abs(1.158822606 * 0.3860531213 - 0.4473670842) < 1e-9, 1.158822606 * 0.3860531213)
chk("Garattini title carries a question mark ('Self sustained traversable wormholes?')",
    "Self sustained traversable wormholes?" in g)

# ------------------------------------------------------------------ C4
print("\nC4  WHAT DECIDES THE SIGN OF m IN EACH FAMILY")
forced = {
    "Hochberg-Popov-Sushkov": "DYNAMICAL (f, r solved); flare m not printed; the tree itself later MEASURED m<0 there (hpscentre.py, CONSERVED reading)",
    "Khusnutdinov-Sushkov": "FORCED: flat background assumed -> m = 0 off the shell; KS print E = -2a < 0",
    "Garattini": "FORCED: Ellis background assumed -> m = r_t^2/2r > 0",
    "Abdolrahimi-Page-Tzounis": "FORCED at leading order: Schwarzschild M >> m_P plus O(hbar) linear perturbation",
    "Sanders": "FORCED by class: ESU m = (a/2) sin^3 chi >= 0",
    "Pinamonti": "FORCED by class: flat FLRW m = R^3 H^2/2 >= 0",
}
n_forced = sum(1 for v in forced.values() if v.startswith("FORCED"))
for k, v in forced.items():
    print("     %-26s %s" % (k, v))
chk("families whose 'm >= 0' is fixed by class/assumed background, not by semiclassical dynamics",
    n_forced == 5, "%d of 6" % n_forced)
import hpscentre
chk("tree's own later measurement: m<0 FOUND in HPS's system (conserved reading)",
    hpscentre.M_NEGATIVE_FOUND_IN_HPS_SYSTEM is True, hpscentre.FIRST_NEGATIVE_M_THROAT_LP)

print("\nRESULT:", "ALL PASS" if ok else "FAILURES")
sys.exit(0 if ok else 1)
