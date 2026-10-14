"""DOCKET 67 -- fermion-mass-constancy.  What a MEASURED constancy of a mass
RATIO can and cannot say about P-UNIFORM (massform.py:220-224, 1621-1627).

No measured bound is typed in here: the measurement papers could not be read
in this run (alphaXiv quota exhausted; arXiv refused by the egress proxy), so
every bound B below is a SYMBOL.  What is checked is the map from any bound B
on a ratio to what it says about v, under hypotheses each named:

  H-SM-TREE   m_e = y_e v / sqrt2 (massform's H-TREE)
  H-DIMHOM    m_p = Lambda F(m_q/Lambda), S = sum sigma_q/m_p  (address.py:99-103)
  H-COUPLE    Lambda = mu0 (m_c m_b m_t/mu0^3)^(2/27) exp(-2 pi/(9 alpha_s(mu0)))
              -- Coc et al. 2007 eq. (13), READ in sibling audit
              dlnlambdaqcd-dlnv-2-9.json (not re-read here)
  H-YUK-FIXED Yukawas do not co-vary with v
  H-AS-FIXED  alpha_s at the high scale does not co-vary with v (address H1)

Imports research/warp-drive/address.py and massform.py READ-ONLY
(sys.dont_write_bytecode) for cross-checks; writes nothing there.
Exit 0 iff every check passes.
"""
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import sympy as sp

FAILS = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    if not ok:
        FAILS.append(name)

# ---------------------------------------------------------------- symbols
lv, lye, lyc, lyb, lyt, lylight, ias, S, B = sp.symbols(
    "lnv lny_e lny_c lny_b lny_t lny_light inv_alpha_s S B", real=True)
mu0 = sp.Symbol("mu0", positive=True)

# ln m_e (H-SM-TREE)
ln_me = lye + lv - sp.log(sp.sqrt(2))
# heavy masses m_Q = y_Q v/sqrt2
ln_mc, ln_mb, ln_mt = [y + lv - sp.log(sp.sqrt(2)) for y in (lyc, lyb, lyt)]
# ln Lambda (H-COUPLE, Coc eq. 13)
ln_L = sp.log(mu0) + sp.Rational(2, 27) * (ln_mc + ln_mb + ln_mt - 3 * sp.log(mu0)) \
       - 2 * sp.pi / 9 * ias
# ln m_p to first order (H-DIMHOM): d ln m_p = (1-S) d ln Lambda + S d ln m_q,
# light quark masses m_q = y_light v/sqrt2
def dln_mp(d):   # d: dict of first-order variations of the base variables
    dL = sum(sp.diff(ln_L, x) * d.get(x, 0) for x in (lv, lyc, lyb, lyt, ias))
    dq = d.get(lylight, 0) + d.get(lv, 0)
    return (1 - S) * dL + S * dq
def dln_me(d):
    return d.get(lye, 0) + d.get(lv, 0)
def dln_mu(d):   # mu = m_p/m_e (address.py's convention)
    return sp.simplify(dln_mp(d) - dln_me(d))

# ---- (A) K_mu under H-YUK-FIXED + H-AS-FIXED (address H1)
K_H1 = dln_mu({lv: 1})
chk("A1 d ln Lambda/d ln v = 2/9 from Coc eq.(13)",
    sp.simplify(sp.diff(ln_L, lv) - sp.Rational(2, 9)) == 0)
chk("A2 K_mu(H1) = -7(1-S)/9 exactly",
    sp.simplify(K_H1 + sp.Rational(7, 9) * (1 - S)) == 0, str(sp.factor(K_H1)))
import address
for s in (0.0096, 0.06, 0.0935):
    chk("A3 matches address.K_mu(%.4f,'H1')" % s,
        abs(float(K_H1.subs(S, s)) - address.K_mu(s, "H1")) < 1e-12,
        "%.6f" % float(K_H1.subs(S, s)))
    chk("A4 H2 (Lambda fixed): K = S-1 matches address at S=%.4f" % s,
        abs((s - 1) - address.K_mu(s, "H2")) < 1e-12)

# ---- (B) the measurement map has rank 1: a ratio bound constrains ONE
#          combination of (v, Yukawas, alpha_s).  Null directions with dv != 0.
vars_ = [lv, lye, lylight, lyc, lyb, lyt, ias]
row = sp.Matrix([[sp.simplify(dln_mu({x: 1})) for x in vars_]])
chk("B1 Jacobian of ln mu over 7 inputs has rank 1", row.rank() == 1,
    str(list(row)))
null = row.nullspace()
chk("B2 null space has dimension 6", len(null) == 6)
# explicit null direction 1: v moves, y_e compensates (needs H-YUK-FIXED to exclude)
d1 = {lv: 1, lye: K_H1}
chk("B3 d ln v = 1, d ln y_e = K_mu: mu EXACTLY constant",
    sp.simplify(dln_mu(d1)) == 0)
# explicit null direction 2: Yukawas fixed, v and high-scale alpha_s co-vary
x = sp.Symbol("x")
sol = sp.solve(sp.Eq(dln_mu({lv: 1, ias: x}), 0), x)
chk("B4 Yukawas fixed, d(1/alpha_s) = %s per unit d ln v keeps mu constant"
    % sp.simplify(sol[0]), len(sol) == 1 and sp.simplify(dln_mu({lv: 1, ias: sol[0]})) == 0)
num = float(sol[0].subs(S, 0.06))
chk("B5 that alpha_s co-variation is finite and O(1) (needs H-AS-FIXED to exclude)",
    abs(num) < 10, "d(1/alpha_s)/d ln v = %.4f at S=0.06" % num)

# ---- (C) a common rescaling of every mass scale is invisible to any ratio
lam = sp.Symbol("lnlambda", real=True)
# if Lambda moves one-for-one with v (d ln Lambda/d ln v = 1, Yukawas fixed):
K_common = (1 - S) * 1 + S * 1 - 1
chk("C1 d ln Lambda/d ln v = 1 gives K_mu = 0: mu is BLIND to v", sp.simplify(K_common) == 0)

# ---- (D) converting any ratio bound B into a vev bound
dv_bound_H1 = B / sp.Abs(K_H1)
dv_bound_H2 = B / sp.Abs(S - 1)
f = lambda e, s: float((e / B).subs(S, s))
lo1, hi1 = f(dv_bound_H1, 0.0096), f(dv_bound_H1, 0.0935)
lo2, hi2 = f(dv_bound_H2, 0.0096), f(dv_bound_H2, 0.0935)
chk("D1 |dv/v| <= B/|K_mu|: factor 1/|K| in [%.4f, %.4f] (H1), [%.4f, %.4f] (H2)"
    % (lo1, hi1, lo2, hi2), 1 < lo1 < hi1 < 1.5 and 1 < lo2 < hi2 < 1.11)
chk("D2 so on H-YUK-FIXED + H1/H2 a ratio bound B bounds |dv/v| by < 1.5 B",
    hi1 < 1.5)
# any finite B leaves |eps| < B/|K| unexcluded where measured: P-UNIFORM
# as written (exact uniformity) is stronger than any finite measurement
chk("D3 for every finite B > 0 the allowed |dv/v| interval is nonempty",
    sp.simplify(dv_bound_H1.subs({S: sp.Rational(3, 50), B: sp.Rational(1, 10**7)})) > 0)

# ---- (E) the tree's own flags (read-only)
import massform
chk("E1 massform.P_UNIFORM_STATUS == 'PREMISE'", massform.P_UNIFORM_STATUS == "PREMISE")
chk("E2 VEV_IS_UNIFORM is P_UNIFORM (no measured value enters)",
    massform.VEV_IS_UNIFORM is massform.P_UNIFORM)
chk("E3 CONSIDERATION_HOLDS True and CONSIDERATION_DISCRIMINATES False",
    massform.CONSIDERATION_HOLDS is True and massform.CONSIDERATION_DISCRIMINATES is False)
src = open("/home/user/Claude-Method-Works/research/warp-drive/massform.py").read().splitlines()
chk("E4 massform.py:223 says the constancy 'is not read here'",
    "not read" in src[222] or "not read" in src[221], src[222].strip())

print()
print("RESULT: %s (%d failures)" % ("ALL PASS" if not FAILS else "FAIL", len(FAILS)))
sys.exit(1 if FAILS else 0)
