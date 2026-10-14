"""D67 audit: qed-one-loop-beta-coefficients (address.py:518-521, 369-393).

Re-derives, independently of address.py, and then compares with it (read-only import):
 C1  sign: d ln alpha(0)/d ln m = +alpha b/(2 pi)                          (sympy)
 C2  convention: Buttazzo et al. 1307.3536 eq.(96)-(97) write dg^2/dln mu^2 = g^4 b/(4pi)^2;
     that is d(1/alpha)/dln mu = -b/(2 pi), the tree's convention           (sympy)
 C3  READ one-loop b_1 = 41/10 (GUT norm.), b_2 = -19/6  [1307.3536 eqs.(96),(97)]
     -> b_em(all thresholds above) = b_Y + b_2 = 41/6 - 19/6 = 11/3
     tree: 32/3 (twelve charged Dirac fermions x 4/3 N_c Q^2) + (-7) = 11/3 ?
 C4  READ PDG 2024 rev. SM eq.(10.13): Delta alpha_hat(MZ) - Delta alpha(MZ) contains
     (alpha/pi)[ -(7/4) ln(MZ^2/MW^2) ]; the W running between MW and MZ gives
     (alpha/pi)(b_W/4) ln(MZ^2/MW^2)  => b_W = -7
     and 100/27 = (5/9) * SUM N_c Q^2 over (e,mu,tau,u,d,s,c,b) = (5/9)(20/3)
 C5  b per unit N_c Q^2 from READ data only: (b_Y + b_2 - b_W)/SUM_3gen N_c Q^2 = 4/3
 C6  b_Y, b_2 reproduced from the generic one-loop formula (2/3 T per Weyl, 1/3 T per
     complex scalar, -11/3 C_A): the same formula that gives 4/3 per unit-charge Dirac
 C7  43/54 exact from the tree's rows (w = 1 for v-masses, 2/9 for u,d,s)
 C8  alpha datum moved: CODATA 2018 1/137.035999084 -> PDG 2024 eq.(10.11) 1/137.035999178
 C9  leverage of the UNNAMED chiral-limit hypothesis on the u,d,s rows (brackets, not a
     measurement): K coefficient if the light-quark threshold weights differ from 2/9
 C10 compare with address.py constants (read-only import)
"""
import sys, math, importlib.util
from fractions import Fraction as F
import sympy as sp

ok = True
def chk(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  -- " + str(detail) if detail else ""))

# C1
aL, b, Lam, m = sp.symbols("alpha_Lambda b Lambda m", positive=True)
a0 = 1 / (1 / aL + b * sp.log(Lam / m) / (2 * sp.pi))
chk("C1 d ln alpha0/d ln m = +alpha0 b/(2pi)", sp.simplify(sp.diff(sp.log(a0), m) * m - a0 * b / (2 * sp.pi)) == 0)

# C2
g, mu = sp.symbols("g mu", positive=True)
bb = sp.symbols("bb")
dg2_dlnmu = 2 * g**4 * bb / (4 * sp.pi)**2            # d g^2/d ln mu = 2 * d g^2/d ln mu^2
dinvalpha = sp.simplify(-4 * sp.pi / g**4 * dg2_dlnmu)  # alpha = g^2/4pi, d(1/alpha) = -4pi dg^2/g^4
chk("C2 Buttazzo convention == d(1/alpha)/dln mu = -b/(2pi)", sp.simplify(dinvalpha + bb / (2 * sp.pi)) == 0, dinvalpha)

# C3
b1_gut, b2 = F(41, 10), F(-19, 6)                 # READ 1307.3536 eqs.(96),(97)
bY = b1_gut * F(5, 3)                              # g1^2 = 5 gY^2/3 -> 1/gY^2 = (5/3)/g1^2
b_em_unbroken = bY + b2                            # 1/e^2 = 1/gY^2 + 1/g2^2
B_DIRAC, B_W = F(4, 3), F(-22, 3) + F(1, 3)
charged = [(1, 1)] * 3 + [(3, F(4, 9))] * 3 + [(3, F(1, 9))] * 3    # (N_c, Q^2) x 3 gen
S3 = sum(n * q for n, q in charged)
tree_sum = B_DIRAC * S3 + B_W
chk("C3 b_Y = 41/6", bY == F(41, 6), bY)
chk("C3 b_em(READ) = b_Y + b_2 = 11/3", b_em_unbroken == F(11, 3), b_em_unbroken)
chk("C3 tree: 4/3*SUM N_cQ^2 + (-7) == 11/3", tree_sum == b_em_unbroken, f"{B_DIRAC*S3} + {B_W} = {tree_sum}")

# C4
L = sp.symbols("L")                                # L = ln(MZ^2/MW^2)
bW = sp.symbols("b_W")
# 1/alpha(MZ) = 1/alpha(MW) - bW ln(MZ/MW)/(2pi) ; Delta alpha_hat gains alpha*bW/(2pi)*ln(MZ/MW)
dDelta = bW / (2 * sp.pi) * (L / 2)                # in units of alpha
sol = sp.solve(sp.Eq(dDelta, sp.Rational(-7, 4) * L / sp.pi), bW)
chk("C4 PDG eq.(10.13) -7/4 ln(MZ^2/MW^2) => b_W = -7", sol == [-7], sol)
S5 = 3 + 3 * (2 * F(4, 9) + 3 * F(1, 9))
chk("C4 100/27 = (5/9) SUM N_cQ^2 (e,mu,tau,u,d,s,c,b)", F(5, 9) * S5 == F(100, 27), (S5, F(5, 9) * S5))

# C5
b_unit = (b_em_unbroken - F(-7)) / S3
chk("C5 b per unit N_cQ^2 from READ (Buttazzo + PDG) = 4/3", b_unit == F(4, 3), b_unit)

# C6
def weyl(T): return F(2, 3) * T
def cscal(T): return F(1, 3) * T
# per generation hypercharge Y (Q = T3 + Y): Weyl multiplicities
gen_Y = [(6, F(1, 6)), (3, F(2, 3)), (3, F(1, 3)), (2, F(1, 2)), (1, F(1))]
bY_calc = 3 * sum(weyl(n * y * y) for n, y in gen_Y) + cscal(2 * F(1, 4))
b2_calc = F(-11, 3) * 2 + 12 * weyl(F(1, 2)) + cscal(F(1, 2))
chk("C6 b_Y from one-loop formula = 41/6", bY_calc == F(41, 6), bY_calc)
chk("C6 b_2 from one-loop formula = -19/6 (gauge part -22/3)", b2_calc == F(-19, 6), b2_calc)
chk("C6 same formula: unit-charge Dirac = 2 Weyl x 2/3 = 4/3", 2 * weyl(1) == F(4, 3))
chk("C6 same formula: charged complex scalar (Goldstone) = 1/3", cscal(1) == F(1, 3))

# C7
wl = F(2, 27) * 3
rows = [(B_DIRAC, F(1))] * 3 + [(B_DIRAC * 3 * F(4, 9), F(1))] * 2 + [(B_DIRAC * 3 * F(1, 9), F(1))]
rows += [(B_DIRAC * 3 * q, wl) for q in (F(4, 9), F(1, 9), F(1, 9))] + [(B_W, F(1))]
coef = sum(x * w for x, w in rows) / 2
chk("C7 wl = 3 x 2/27 = 2/9", wl == F(2, 9))
chk("C7 K_alpha(H1) coefficient = 43/54", coef == F(43, 54), coef)
light_share = sum(x * w for x, w in rows[6:9]) / 2 / coef
print("     u,d,s share of 43/54:", light_share, "=", float(light_share))
W_share = (B_W / 2) / coef
print("     W row / total:", W_share, "=", float(W_share))

# C8
a18, a24 = 1 / 137.035999084, 1 / 137.035999178
K18, K24 = float(coef) * a18 / math.pi, float(coef) * a24 / math.pi
print(f"C8  K(CODATA2018) = {K18:.9e}  K(PDG2024 avg) = {K24:.9e}  rel. change = {(K24-K18)/K18:.2e}")
chk("C8 K = 1.849653e-3 at 6 s.f. under both alpha values", round(K18, 9) == round(K24, 9) == 1.849653e-3 or (f"{K18:.6e}" == f"{K24:.6e}" == "1.849653e-03"))

# C9 (brackets only)
def coef_with(wlight):
    r = rows[:6] + [(B_DIRAC * 3 * q, w) for q, w in zip((F(4, 9), F(1, 9), F(1, 9)), wlight)] + [rows[-1]]
    return sum(x * w for x, w in r) / 2
cases = {
  "tree (2/9,2/9,2/9)": (wl, wl, wl),
  "s threshold ~ m_s (w_s=1)": (wl, wl, F(1)),
  "pion-like m ~ sqrt(m_q Lambda): w=1/2+1/9": (F(11, 18),) * 3,
  "all ~ v (w=1)": (F(1),) * 3,
  "u,d,s dropped (w=0)": (F(0),) * 3,
}
for k, v in cases.items():
    c = coef_with(v)
    print(f"C9  {k:45s} coef = {str(c):8s} = {float(c):.4f}  ({float(c/coef-1):+.1%})")

# C10
spec = importlib.util.spec_from_file_location("address", "/home/user/Claude-Method-Works/research/warp-drive/address.py")
A = importlib.util.module_from_spec(spec); sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
spec.loader.exec_module(A)
chk("C10 address.B_DIRAC_UNIT_CHARGE == 4/3", A.B_DIRAC_UNIT_CHARGE == F(4, 3))
chk("C10 address.B_W_BOSON == -7", A.B_W_BOSON == -7)
chk("C10 address.dln_lambda_dln_v() == 2/9", A.dln_lambda_dln_v() == F(2, 9), A.dln_lambda_dln_v())
chk("C10 address.K_ALPHA_H1_COEFFICIENT == 43/54 (independent)", A.K_ALPHA_H1_COEFFICIENT == coef)
chk("C10 address.K_ALPHA_H1 == independent K18", abs(A.K_ALPHA_H1 - K18) < 1e-15, A.K_ALPHA_H1)
print("C10 address.RULING_F7_SEATED:", A.RULING_F7_SEATED)
th = {h: A.th229_coefficient("H1", k_alpha=lambda _h, k=k: k) for h, k in (("K18", K18), ("K24", K24))}
print("C10 Th-229 H1 coefficient at K18/K24:", th)
print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
