#!/usr/bin/env python3
"""DOCKET 67 audit re-derivation: sm-tree-vev-from-gf.
Tree-level SM relation v = (sqrt2 G_F)^(-1/2) and the tree-level quantities
built from it in higgs.py / massform.py (y_f = sqrt2 m_f / v; g = 2 m_W / v).
Reads the tree read-only (no bytecode written). Every source number is quoted
with its locator; nothing here is fitted."""
import sys, math
sys.dont_write_bytecode = True
import sympy as sp

FAIL = 0
def chk(name, ok, detail=""):
    global FAIL
    print(("PASS " if ok else "FAIL ") + name + ("   " + detail if detail else ""))
    if not ok: FAIL += 1
def rel(a, b): return abs(a / b - 1.0)

print("== A. sympy: the tree-level relation (PDG 2024 EW review eq.10.5b and p.2)")
g, v, MW, GF = sp.symbols("g v M_W G_F", positive=True)
# PDG: G_F/sqrt2 = 1/(2v^2) = g^2/(8 M_W^2), with M_W = g v / 2 (tree level)
e1 = sp.Eq(GF / sp.sqrt(2), g**2 / (8 * MW**2))
sol = sp.solve(e1.subs(MW, g * v / 2), GF)[0]
chk("A1 G_F/sqrt2 = g^2/(8M_W^2), M_W = gv/2  =>  G_F = 1/(sqrt2 v^2)",
    sp.simplify(sol - 1 / (sp.sqrt(2) * v**2)) == 0, str(sol))
vsol = [s for s in sp.solve(sp.Eq(GF, 1 / (sp.sqrt(2) * v**2)), v) if s.is_positive]
chk("A2 positive root v = (sqrt2 G_F)^(-1/2)",
    len(vsol) == 1 and sp.simplify(vsol[0] - (sp.sqrt(2) * GF) ** sp.Rational(-1, 2)) == 0, str(vsol))
# g drops out: the relation v(G_F) is independent of g at tree level
chk("A3 g cancels (v depends on G_F only at tree level)", sp.diff(sol, g) == 0)
# Buttazzo eq.(18): g2_OS = 2 (sqrt2 G_mu)^(1/2) M_W  ==  2 M_W / v  (massform alpha_w form)
chk("A4 Buttazzo eq.18 g2 = 2(sqrt2 G)^(1/2) M_W  ==  2 M_W / v(G)",
    sp.simplify(2 * sp.sqrt(sp.sqrt(2) * GF) * MW - 2 * MW / vsol[0]) == 0)
Mt = sp.symbols("M_t", positive=True)
chk("A5 Buttazzo eq.18 y_t = 2(G/sqrt2 M_t^2)^(1/2) == sqrt2 M_t / v(G)",
    sp.simplify(2 * sp.sqrt(GF / sp.sqrt(2) * Mt**2) - sp.sqrt(2) * Mt / vsol[0]) == 0)

print("\n== B. numeric: v from every READ G_F")
vev = lambda G: 1.0 / math.sqrt(math.sqrt(2.0) * G)
G_TREE = 1.1663788e-5          # higgs.py:209 ; PDG 2024 EW review eq.(10.8) 1.1663788(6)
v_tree = vev(G_TREE)
print("   v(tree pin) = %.6f GeV" % v_tree)
chk("B1 higgs.py selftest fixture 246.2196 at 1e-5", rel(v_tree, 246.2196) < 1e-5, "rel %.2e" % rel(v_tree, 246.2196))
chk("B2 PDG 2024 EW review p.2 'v = 246.22 GeV' (5 s.f.)", round(v_tree, 2) == 246.22)
chk("B3 Buttazzo Table 2 V = 246.21971(6) reproduced from Buttazzo's OWN eq.27 G_mu = 1.1663781e-5",
    abs(vev(1.1663781e-5) - 246.21971) < 5e-6, "%.6f" % vev(1.1663781e-5))
print("   RECORDED: Table 2 cites MuLan [91], but MuLan's 1.1663787 gives %.6f; the printed V matches"
      " the propagator-stripped G_mu (6e-8 relative apart; moves nothing)" % vev(1.1663787e-5))
Gs = {"MuLan 2013 1.1663787(6)": 1.1663787e-5, "Eberhart 2026 1.16637859(59)": 1.16637859e-5,
      "Buttazzo w/o W-propagator 1.1663781(6)": 1.1663781e-5,
      "G_F^EW 1.16716(39) (2102.02825)": 1.16716e-5, "G_F^CKM 1.16550(29) (2102.02825)": 1.16550e-5}
for k, G in Gs.items():
    print("   %-40s v = %.5f  dv/v = %+.2e" % (k, vev(G), vev(G) / v_tree - 1))
chk("B4 every muon-decay G_F moves v by < 5e-7", all(abs(vev(G) / v_tree - 1) < 5e-7 for k, G in Gs.items() if "2102" not in k))

print("\n== C. what 'tree level' drops: PDG 2024 on-shell Delta r (eq.10.22b)")
alpha0 = 1 / 137.035999178       # PDG 2024 EW eq.(10.11)
A0 = math.sqrt(math.pi * alpha0 / (math.sqrt(2) * G_TREE))
chk("C1 A0 = (pi alpha/(sqrt2 G_F))^(1/2) = 37.28038 GeV (PDG)", abs(A0 - 37.28038) < 2e-5, "%.6f" % A0)
sW2, dr = 0.22348, 0.03685        # PDG Table 10.2, and p.8
MW_pred = A0 / math.sqrt(sW2 * (1 - dr))
MW_treeOS = A0 / math.sqrt(sW2)
print("   M_W from A0, s_W^2, Delta r = 0.03685: %.4f GeV ; with Delta r = 0 (tree): %.4f GeV" % (MW_pred, MW_treeOS))
chk("C2 PDG numbers self-consistent: M_W(Delta r) within 20 MeV of fit/measured 80.3692",
    abs(MW_pred - 80.3692) < 0.02, "%.4f" % MW_pred)
chk("C3 tree-level (Delta r=0) misses M_W by ~1.9%: the dropped correction is O(%)",
    0.015 < 1 - MW_treeOS / 80.3692 < 0.025, "%.4f" % (1 - MW_treeOS / 80.3692))
# Martin-Robertson 1907.02500 eq.(1.11),(4.1): tadpole-free MS-bar v(173.1) = 246.60109
vMS = 246.60109
v_G19 = vev(1.1663787e-5)
drt = (vMS / v_G19) ** 2 - 1
print("   Martin-Robertson MS-bar v(Q0=173.1) = %.5f ; v_G = %.5f ; Delta r~ = %.5f ; dv/v = %+.4f" % (vMS, v_G19, drt, vMS / v_G19 - 1))
chk("C4 v = (sqrt2 G_F)^(-1/2) differs from the MS-bar vev by 0.15%: scheme, not error",
    0.001 < vMS / v_G19 - 1 < 0.002)

print("\n== D. massform.py consumers, re-computed (capture values read from the tree)")
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
try:
    import massform, higgs
    MW_cap = massform.M_W_GEV; mt_cap = massform.MASS_MEV["t"] / 1000; me_cap = massform.MASS_MEV["e"] / 1000
    chk("D0 tree's higgs.vev() equals this script's v(G_F)", rel(higgs.vev(), v_tree) < 1e-15)
except Exception as ex:   # fall back to the capture values the tree prints
    print("   (import failed: %r) using printed capture values" % ex)
    MW_cap, mt_cap, me_cap = 80.362, 172.6, 0.000510998951
y_t = math.sqrt(2) * mt_cap / v_tree; y_e = math.sqrt(2) * me_cap / v_tree
chk("D1 y_t = 0.9914 (massform.py:217)", round(y_t, 4) == 0.9914, "%.6f" % y_t)
chk("D2 y_e = 2.935e-6 (massform.py:217)", round(y_e * 1e9) == 2935, "%.5e" % y_e)
gW = 2 * MW_cap / v_tree; aW = gW**2 / (4 * math.pi)
chk("D3 1/alpha_W = 29.49 (massform.py:528)", round(1 / aW, 2) == 29.49, "%.4f" % (1 / aW))
L = lambda a: -(4 * math.pi / a) / math.log(10)
chk("D4 log10 exp(-4pi/alpha_W) = -160.95 (massform.py:530-531)", round(L(aW), 2) == -160.95, "%.4f" % L(aW))

print("\n== E. the size of the dropped hypothesis on the consumers (scheme spread, READ inputs)")
# Buttazzo Table 3 LO vs NNLO at mu = M_t (inputs M_t=173.34, M_W=80.384)
chk("E1 Buttazzo LO y_t 0.99561 = sqrt2*173.34/246.21971", abs(math.sqrt(2) * 173.34 / 246.21971 - 0.99561) < 5e-6)
g2lo = 2 * 80.384 / 246.21971
chk("E2 Buttazzo LO g2 0.65294 vs 2*80.384/246.21971 (agree to 3e-5)", abs(g2lo - 0.65294) < 3e-5, "%.6f" % g2lo)
print("   NOTE: recomputed LO g2 = %.6f vs printed 0.65294 (%.1e relative),"
      " a half-unit in the 5th decimal: consistent with rounding, not a discrepancy" % (g2lo, g2lo/0.65294-1))
yt_ratio = 0.93690 / 0.99561   # eq.(57) NNLO+3loopQCD vs LO
g2_ratio = 0.64779 / 0.65294
print("   Buttazzo: y_t(M_t) MS-bar / tree = %.4f ; g2(M_t) MS-bar / tree = %.4f" % (yt_ratio, g2_ratio))
# Martin-Robertson reference point (M_t=173.1, M_e = 0.000510998946)
yt_MR_tree = math.sqrt(2) * 173.1 / v_G19; ye_MR_tree = math.sqrt(2) * 0.000510998946 / v_G19
print("   Martin-Robertson: y_t(173.1) %.5f vs tree %.5f (ratio %.4f); y_e %.4e vs tree %.4e (ratio %.4f)"
      % (0.93480082, yt_MR_tree, 0.93480082 / yt_MR_tree, 2.7929820e-6, ye_MR_tree, 2.7929820e-6 / ye_MR_tree))
chk("E3 MS-bar Yukawas at M_t are 5-6% below tree for both t and e (scheme/scale, not error)",
    0.93 < 0.93480082 / yt_MR_tree < 0.95 and 0.94 < 2.7929820e-6 / ye_MR_tree < 0.96)
# alpha_W across schemes -- the instanton exponent is the only consumer that amplifies it
schemes = {
  "tree G_mu-scheme 2M_W/v (massform)": aW,
  "Buttazzo MS-bar g2(M_t)=0.64779": 0.64779**2 / (4 * math.pi),
  "Martin MS-bar g2(173.1)=0.64766": 0.64765961**2 / (4 * math.pi),
  "alpha-hat(M_Z)/s-hat^2_Z = 1/(127.930*0.23129)": 1 / (127.930 * 0.23129),
  "alpha(0)/s_W^2 on-shell = 1/(137.036*0.22348)": alpha0 / 0.22348,
}
ex = {}
for k, a in schemes.items():
    ex[k] = L(a)
    print("   %-48s 1/alpha_W = %7.3f  log10 exp(-4pi/aW) = %8.2f" % (k, 1 / a, ex[k]))
spread = max(ex.values()) - min(ex.values())
print("   spread of the exponent across schemes: %.2f decades" % spread)
chk("E4 scheme spread of the exponent is several decades but < 10", 2 < spread < 10, "%.2f" % spread)
lt = math.log10(1.4036e28)   # massform.py:532 transitions (1.4036e28)
need = [lt - e for e in ex.values()]
chk("E5 tree's 'attempts x prefactor must reach 10^189.10' reproduced in its own scheme",
    abs(lt - ex["tree G_mu-scheme 2M_W/v (massform)"] - 189.10) < 0.01)
print("   => needed = 10^%.2f .. 10^%.2f across the five schemes" % (min(need), max(need)))

print("\n== F. moved data")
for lab, mw in [("capture (PDG-2026) 80.362", 80.362), ("PDG2024 no-CDF avg 80.3692", 80.3692),
                ("PDG2024 all avg 80.3946", 80.3946), ("CDF II 80.432", 80.432),
                ("pole (BW - 27.1 MeV, Martin eq.1.9)", 80.362 - 0.0271)]:
    a = (2 * mw / v_tree) ** 2 / (4 * math.pi)
    print("   m_W %-38s 1/alpha_W %.4f  exponent %.3f  (shift %+.3f)" % (lab, 1 / a, L(a), L(a) - L(aW)))
chk("F1 every READ m_W moves the exponent by < 0.5 decade", all(
    abs(L((2 * mw / v_tree) ** 2 / (4 * math.pi)) - L(aW)) < 0.5 for mw in (80.3692, 80.3946, 80.432, 80.3349)))
for lab, mt in [("capture 172.6", 172.6), ("PDG2024 listings 172.57", 172.57), ("PDG2024 EW combination 172.61", 172.61)]:
    print("   m_t %-30s y_t(tree) %.5f" % (lab, math.sqrt(2) * mt / v_tree))
print("\n%d FAIL" % FAIL)
sys.exit(1 if FAIL else 0)
