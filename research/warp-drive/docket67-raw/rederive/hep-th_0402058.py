#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Bousso, 'Flat space physics from holography', hep-th/0402058v2
(JHEP 0405:050, 2004).  Checks every closed-form claim of Sec. 2.1-3 the tree leans on, plus
the one numeric example.  Units: k_B = c = 1 as in the source; hbar and l_Pl kept explicit.
Exit 0 iff every check that the SOURCE makes agrees; discrepancies are PRINTED, not failed."""
import sys, sympy as sp

M, R, G, hb, lP = sp.symbols('M R G hbar l_P', positive=True)
ok = True
def chk(name, cond):
    global ok
    ok &= bool(cond)
    print("  [%s] %s" % ("ok" if cond else "XX", name))

print("hep-th/0402058 re-derivation")
S_bek = 2*sp.pi*M*R/hb                   # eq (2.2)
S_hol = 4*sp.pi*R**2/(4*G*hb)            # eq (2.1) for a sphere, A/4Għ with l_P^2 = Għ
# (a) the quoted claim: no Newton constant in (2.2), in the hbar-form
chk("(a) dS_Bek/dG == 0 in the hbar-form of (2.2)", sp.diff(S_bek, G) == 0)
chk("(a') at G = 0, S_Bek is finite and nonzero for M,R>0 ('remains nontrivial')",
    S_bek.subs(G, 0) == S_bek and S_bek != 0)
# (b) Sec 2.1: covariant bound becomes trivial as G -> 0 (hbar fixed)
chk("(b) lim_{G->0} A/4Għ = oo  ('trivial for G = 0', p.4)", sp.limit(S_hol, G, 0, '+') == sp.oo)
# (c) Sec 2.2: under M << R/G the Bekenstein bound is tighter; ratio = 2GM/R
ratio = sp.simplify(S_bek/S_hol)
chk("(c) S_Bek/S_hol == 2GM/R, hence << 1 exactly when M << R/G (eq 2.3)", sp.simplify(ratio - 2*G*M/R) == 0)
# (d) Schwarzschild: R = 2GM saturates (2.2) exactly -- but sits OUTSIDE (2.3)
S_bh = (4*sp.pi*(2*G*M)**2)/(4*G*hb)
chk("(d) S_BH = A/4Għ at R = 2GM equals 2πMR/ħ exactly", sp.simplify(S_bh - S_bek.subs(R, 2*G*M)) == 0)
w = sp.simplify(M/(R/G)).subs(R, 2*G*M)
print("      weak-gravity parameter M/(R/G) at the horizon = %s  (source's regime needs << 1)" % w)
chk("(d') black hole is NOT weakly gravitating: M/(R/G) = 1/2", w == sp.Rational(1, 2))
# (e) at G -> 0 the Schwarzschild radius of every mass vanishes: no BH exists in the G = 0 regime
chk("(e) lim_{G->0} 2GM = 0: the saturating object disappears where 'nontrivial at G=0' holds",
    sp.limit(2*G*M, G, 0) == 0)
# (f) representation dependence: write hbar = l_P^2/G (the source's own eq (1.4)/(3.2) form)
S_bek_lP = S_bek.subs(hb, lP**2/G)
print("      (2.2) with hbar -> l_P^2/G:", sp.simplify(S_bek_lP))
chk("(f) in the l_P-form (source eq 3.2) G DOES appear: dS/dG != 0", sp.diff(S_bek_lP, G) != 0)
chk("(f') and at fixed l_P, lim_{G->0} = 0, i.e. the bound collapses, not 'nontrivial'",
    sp.limit(S_bek_lP, G, 0) == 0)
# (g) Sec 3 heuristic: deflection 4GM/R over lever arm ~R, annulus 2πR x 4GM, S <= ΔA/4l_P^2
dA = 2*sp.pi*R*(4*G*M/R)*R
S_gceb = sp.simplify((dA/(4*lP**2)).subs(lP**2, G*hb))
print("      heuristic (3.1)-(3.2) with deflection 4GM/R, lever arm R: S <=", S_gceb)
chk("(g) the X-ray heuristic reproduces 2πMR/ħ (source: 'up to factors of order one')",
    sp.simplify(S_gceb - S_bek) == 0)

# (h) the numerical example, CODATA 2022 (hbar exact since 2019 SI; G, m_e from CODATA 2022)
hbar = 1.054571817e-34; c = 299792458.0; Gn = 6.67430e-11; me = 9.1093837139e-31
lp = (hbar*Gn/c**3)**0.5
for lab, Rl in (("reduced Compton hbar/(m c)", hbar/(me*c)), ("Compton h/(m c)", 2*3.141592653589793*hbar/(me*c))):
    print("      electron, R = %-26s pi R^2/l_P^2 = %.3e   (source prints 10^44)" % (lab, 3.141592653589793*Rl**2/lp**2))
Sb_e = 2*3.141592653589793  # 2π M R/ħ with R = ħ/M
print("      electron Bekenstein bound 2πMR/ħ at R=ħ/Mc: %.3f ; spin entropy ln2 = 0.693 -> 'roughly saturated' (order one)" % Sb_e)
print("  DISCREPANCY (recorded, not an error): the electron holographic figure is 1.8e45 (reduced Compton)"
      " to 7.1e46 (Compton), 1.3-2.9 decades above the printed 10^44; the tree does not use it.")
# G-sensitivity: CODATA 2018 and 2022 G identical; the claim is structural so no datum enters
print("  G(CODATA 2018) = G(CODATA 2022) = 6.67430e-11; the G-independence claim uses no numerical datum.")
print("RESULT:", "ALL SOURCE CLAIMS REPRODUCED" if ok else "MISMATCH")
sys.exit(0 if ok else 1)
