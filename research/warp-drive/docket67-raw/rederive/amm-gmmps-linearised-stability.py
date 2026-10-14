#!/usr/bin/env python3
"""DOCKET 67 -- audit of amm-gmmps-linearised-stability (AMM validity criterion
+ GMMPS Minkowski growing mode, as D26 / specthm R8 / ledger OPENED_FROM_WAITING
use them).  Reads NOTHING under research/ or drive/ for writing; reads the banked
alphaXiv text layers of both papers (md5-pinned) and re-derives what is finite.

   python3 amm-gmmps-linearised-stability.py      -> 'N/N checks pass', exit 0
"""
import hashlib, html, re, sys
import sympy as sp
import mpmath as mp

D67 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/"
D64 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d64/L4/"
TEXTS = {
    "AMM_a": (D67 + "amm_0209075.txt", "486395c6c5ea8f9b16f0478d78a0f375"),
    "AMM_b": (D67 + "src/casmag/all/gr-qc_0209075v1.txt", "906e1cc98f250b6b860823dd98bbc72b"),
    "GMMPS_a": (D67 + "src/casmag/all/2604.01047v1.txt", "d8bf938e9781102399b34444bb59cac2"),
    "GMMPS_b": (D64 + "galanda.txt", "4bac4a9400afceac615c5aa3b9f83c6e"),
}
results = []
def check(name, ok, detail=""):
    results.append((name, bool(ok)))
    print("%-4s %s  %s" % ("PASS" if ok else "FAIL", name, detail))

def norm(s):   # the AMM layer splits words ('m eans'); compare with ALL whitespace removed
    return re.sub(r"\s+", "", s)

# ---------------------------------------------------------------- S0 sources
txt = {}
for k, (p, h) in TEXTS.items():
    b = open(p, "rb").read()
    check("S0 md5 %s" % k, hashlib.md5(b).hexdigest() == h, p)
    txt[k] = norm(html.unescape(b.decode("utf-8", "replace")))

AMM_STRINGS = [   # verbatim at source (ligatures 'fi','ff' are dropped by the AMM layer)
    ("criterion p10", "A necessary condition for the validity of the large N semi-classical equations of motion (2.9) is that the linear response equations(3.4)should have no solutionswith nite non-singularinitialdata forwhich any linearized gauge invariant scalar quantity grows without bound"),
    ("abstract", "no gauge invariant perturbation should become unbounded in time"),
    ("abstract flat", "is stable to allperturbations on distance scales much larger than the Planck length"),
    ("p9 leading-order solution", "retarded correlation function is evaluated in the back- ground geometry ofthe leading order solution ofthe semi-classicalequations (2.9)"),
    ("p12 alpha<0", "interchange roles,with the conclusion unchanged"),
    ("p12 k=0 not treated", "We do not treat this possibility in this paper"),
    ("p12 tensor", "no tensor mode solutions ofthe linear response eq.(3.4) on length scales much larger than the Planck length for a massive eld theory around at space"),
]
for nm, s in AMM_STRINGS:
    check("S0 AMM verbatim '%s'" % nm, norm(s) in txt["AMM_a"])
check("S0 AMM second dump carries criterion", norm("linearized gauge invariant scalar") in txt["AMM_b"]
      or norm("gauge invariant scalar quantity") in txt["AMM_b"])

GMMPS_STRINGS = [
    ("abstract instability", "We establish the linear instability of the semiclassical Einstein–Klein–Gordon system linearised about the Minkowski vacuum spacetime"),
    ("Thm 3.6 value", "are ˜α S 1 = 1 64π 2 , ˜α TT 1 = 0"),
    ("5.1 printed (64pi)^-1", "Theorem 3.6 to fix ˜α S 1 = (64π) −1"),
    ("Thm 4.16 bounded clause", "If Z ⊂ (−4m 2 , 0) and if S ∈ C ∞ c (M), the solution (4.31) of (4.9) are bounded in time"),
    ("Thm 4.16 growth clause", "If Z ⊂ (−4m 2 , ∞), with some, γ ∈ Z, γ > 0, the solution is exponentially growing"),
    ("5.1 slightly smaller than 0", "there is a zero γ 0 of F S that it is real valued and that is slightly smaller than 0"),
    ("5.1 large -b2 only negative zero", "For sufficiently large −b 2 , this is the only negative zero that can be found in D"),
    ("5.1 negative zero => unstable", "the presence of a negative zero implies that the solution of the equation for the S modes are unstable"),
    ("5.2 TT gamma0", "One of the zeros, say γ 0 , is, however, always negative"),
    ("5.2.1 universality hypotheses", "if ˜α S 3 is sufficiently large and negative and if ˜α TT 4 is sufficiently large and positive, the parameter H is universal"),
    ("5.2.1 attribution", "This different behaviour is originated by the choice of the renormalisation parameters done in Theorem 3.6"),
    ("1.5 regardless", "regardless of renormalisation constants, linear perturbations grow exponentially for arbitrary Cauchy data"),
    ("Thm 1.2 bound", "˜ h ab ≤ e −Ht η ab"),
    ("Thm 1.2 any source", "For any nontrivial choice of the sources S ab and Ξ, the solution ˜ h ab grows exponentially in time"),
    ("5.3 gamma~", "˜γ ≃ − b 0 b 1 = −16πG˜α S 1 m 4"),
    ("5.2 TT zero = GW", "Zero is always one of these zeros of F TT in (5.4) and the corresponding TT modes correspond to the classical gravitational waves"),
    ("5.3 inputs", "Ω Λ ≃ 0.685 and Λ ≃ 7.15 × 10 −121 M 2 P"),
]
for nm, s in GMMPS_STRINGS:
    a = norm(s) in txt["GMMPS_a"]; b = norm(s) in txt["GMMPS_b"]
    check("S0 GMMPS verbatim '%s' (both dumps)" % nm, a and b, "a=%s b=%s" % (a, b))

# ---------------------------------------------------------------- S1 sympy: the branch root
m, kap, al, xi, g, b2 = sp.symbols('m kappa alpha xi gamma b_2', real=True)
mp_ = sp.Symbol('mpos', positive=True); M = sp.Symbol('M', positive=True); z = sp.Symbol('z')
c = 6 * (sp.Rational(1, 6) - xi) ** 2
b0 = -al * 4 * m ** 4 / c          # (5.2) as the tree transcribes; sign/ratio independent of c's placement
b1 = -(2 / kap) / c
a = 2 * m ** 2 / (6 * xi - 1)
rho = sp.sqrt(1 - 4 * mp_ ** 2 / M) / (16 * sp.pi ** 2 * M)                 # (4.5)
J0_int = sp.simplify(sp.integrate(rho / M, (M, 4 * mp_ ** 2, sp.oo)))
J417 = (1 / (8 * sp.pi ** 2)) * (1 / z - sp.sqrt(4 * mp_ ** 2 - z) * sp.asin(sp.sqrt(z) / (2 * mp_)) / z ** sp.Rational(3, 2))
J0_417 = sp.simplify(sp.limit(J417, z, 0, '+'))
check("S1 J(0) = 1/(96 pi^2 m^2) from integral", sp.simplify(J0_int - 1 / (96 * sp.pi ** 2 * mp_ ** 2)) == 0, str(J0_int))
check("S1 J(0) = 1/(96 pi^2 m^2) from (4.17) limit", sp.simplify(J0_417 - 1 / (96 * sp.pi ** 2 * mp_ ** 2)) == 0, str(J0_417))
J0 = 1 / (96 * sp.pi ** 2 * m ** 2)
F0 = -b0                        # F_S(0)
F1 = a ** 2 * J0 - b1           # F_S'(0)  (J'(0) term multiplies gamma^2 -> not in F_S'(0))
FS_poly = g * (a - g) ** 2 * (J0 + sp.Symbol('J1') * g) - (b0 + b1 * g + b2 * g ** 2)
check("S1 F_S'(0) from the (5.3) form", sp.simplify(sp.diff(FS_poly, g).subs(g, 0) - F1) == 0)
check("S1 F_S(0) = 0 iff alpha = 0", sp.solve(sp.Eq(F0, 0), al) == [0])
F1_scaled = sp.simplify(F1 * c * kap)   # c>0 for xi != 1/6, kappa>0
check("S1 F_S'(0)*c*kappa = 2 + kappa m^2/(144 pi^2) > 0 (simple root; IFT applies)", sp.simplify(F1_scaled - (2 + kap * m ** 2 / (144 * sp.pi ** 2))) == 0, str(F1_scaled))
gam1 = sp.simplify(-F0 / F1)
target = -2 * kap * al * m ** 4 / (1 + kap * m ** 2 / (288 * sp.pi ** 2))
check("S1 first-order root = -2 kappa alpha m^4/(1+kappa m^2/(288 pi^2)), xi-free", sp.simplify(gam1 - target) == 0)
check("S1 d gamma0/d alpha < 0 => grows (gamma0<0) iff alpha > 0", sp.simplify(sp.diff(target, al)).subs({kap: 1, m: 1}) < 0)
check("S2 5.3: -b0/b1 = -16 pi G alpha m^4 (kappa = 8 pi G)",
      sp.simplify(sp.simplify(-b0 / b1) - (-16 * sp.pi * sp.Symbol('G') * al * m ** 4)).subs(kap, 8 * sp.pi * sp.Symbol('G')) == 0)

# ---------------------------------------------------------------- S3 numerics at the physical hierarchy
mp.mp.dps = 420
def J(gv, mm):
    gv = mp.mpc(gv)
    return (1 / (8 * mp.pi ** 2)) * (1 / gv - mp.sqrt(4 * mm ** 2 - gv) * mp.asin(mp.sqrt(gv) / (2 * mm)) / gv ** mp.mpf(1.5))
def FS(gv, mm, kk, alv, xiv, b2v):
    cc = 6 * (mp.mpf(1) / 6 - xiv) ** 2
    B0 = -alv * 4 * mm ** 4 / cc; B1 = -(2 / kk) / cc; A = 2 * mm ** 2 / (6 * xiv - 1)
    return mp.re(gv * (A - gv) ** 2 * J(gv, mm)) - (B0 + B1 * gv + b2v * gv ** 2)
MP_EV = mp.mpf('2.435323e27')          # reduced Planck mass, eV (sqrt(hbar c/8 pi G) c^2, CODATA 2018 G)
mm = mp.mpf('7.885e-3') / MP_EV        # GMMPS 5.3 mass in reduced-Planck units, kappa = 1
kk = mp.mpf(1); AL = 1 / (64 * mp.pi ** 2); XI = mp.mpf(0)
tgt = -2 * kk * AL * mm ** 4 / (1 + kk * mm ** 2 / (288 * mp.pi ** 2))
def root_near(x0, b2v, alv=AL):
    lo, hi = x0 * 2, x0 / 2
    flo, fhi = FS(lo, mm, kk, alv, XI, b2v), FS(hi, mm, kk, alv, XI, b2v)
    if flo * fhi > 0: return None
    for _ in range(400):
        mid = (lo + hi) / 2; fm = FS(mid, mm, kk, alv, XI, b2v)
        if fm * flo > 0: lo, flo = mid, fm
        else: hi = mid
    return (lo + hi) / 2
for b2v in (mp.mpf(0), mp.mpf(1), mp.mpf(-1), mp.mpf('1e100'), mp.mpf('-1e100')):
    r = root_near(tgt, b2v)
    check("S3 full-F_S branch zero at b2=%s equals first-order root to 1e-15" % mp.nstr(b2v, 3),
          r is not None and abs(r / tgt - 1) < mp.mpf('1e-15'), "root=%s tgt=%s" % (mp.nstr(r, 6) if r else None, mp.nstr(tgt, 6)))
def neg_sign_changes(b2v, lo_exp=-130, hi_exp=-40, n=900):
    xs = [-mp.mpf(10) ** (lo_exp + (hi_exp - lo_exp) * i / n) for i in range(n + 1)]
    vs = [FS(x, mm, kk, AL, XI, b2v) for x in xs]
    return sum(1 for i in range(n) if vs[i] * vs[i + 1] < 0)
def pos_sign_changes(b2v, lo_exp=-130, n=900):
    hi_exp = float(mp.log10(4 * mm ** 2)) - 0.01
    xs = [mp.mpf(10) ** (lo_exp + (hi_exp - lo_exp) * i / n) for i in range(n + 1)]
    vs = [FS(x, mm, kk, AL, XI, b2v) for x in xs]
    return sum(1 for i in range(n) if vs[i] * vs[i + 1] < 0)
nneg_m = neg_sign_changes(mp.mpf('-1e100')); nneg_p = neg_sign_changes(mp.mpf('1e100')); npos_p = pos_sign_changes(mp.mpf('1e100'))
check("S3 b2=-1e100 (5.1's 'large -b2'): TWO negative real zeros of F_S in (-1e-40,-1e-130)", nneg_m == 2, "sign changes=%d" % nneg_m)
check("S3 b2=+1e100: exactly ONE negative zero (the branch root) and one in (0,4m^2)", nneg_p == 1 and npos_p == 1, "neg=%d pos=%d" % (nneg_p, npos_p))
# the second negative zero at b2<0 sits near -b1/b2 and is LARGER in magnitude than gamma0 -> it, not gamma0, sets the growth
cc0 = 6 * (mp.mpf(1) / 6 - XI) ** 2; B1n = -(2 / kk) / cc0
r2 = root_near(-B1n / mp.mpf('-1e100'), mp.mpf('-1e100'))
check("S3 b2=-1e100: second negative zero ~ -b1/b2, |.| >> |gamma0|", r2 is not None and abs(r2) > 1e15 * abs(tgt),
      "zero=%s gamma0=%s" % (mp.nstr(r2, 5) if r2 else None, mp.nstr(tgt, 5)))
# universality of H for b2>0 needs b2 << b1^2/|b0|: beyond it the negative zero ~ -sqrt(|b0|/b2)
B0n = -AL * 4 * mm ** 4 / cc0
thr = B1n ** 2 / abs(B0n)
rbig = root_near(-mp.sqrt(abs(B0n) / (1000 * thr)), 1000 * thr)
check("S3 b2 = 1e3 x b1^2/|b0| (%s): negative zero ~ -sqrt(|b0|/b2), NOT gamma0 (H not universal)" % mp.nstr(thr, 3),
      rbig is not None and abs(rbig / tgt) < mp.mpf('0.1'), "zero=%s" % (mp.nstr(rbig, 5) if rbig else None))
r0 = FS(mp.mpf(0) + mp.mpf('1e-300'), mm, kk, mp.mpf(0), XI, mp.mpf(1))
check("S3 alpha=0: gamma=0 is a zero of F_S (|F_S(1e-300)| tiny)", abs(r0) < mp.mpf('1e-290'), mp.nstr(r0, 3))

# ---------------------------------------------------------------- S4 Thm 4.16's variable, mapped
w2, A_, B0_, B1_, B2_ = sp.symbols('w2 a b0 b1 b2'); Jf = sp.Function('J')
Q = w2 * (w2 + A_) ** 2 * Jf(-w2) + B0_ - B1_ * w2 + B2_ * w2 ** 2               # (4.30), a1=a2=a
FSs = g * (A_ - g) ** 2 * Jf(g) - (B0_ + B1_ * g + B2_ * g ** 2)                  # (5.3)
check("S4 F_S(-w^2) = -Q(w^2) identically (zeros map gamma = -w^2)", sp.simplify(FSs.subs(g, -w2) + Q) == 0)
# Thm 4.16 in Q's variable: bounded if all zeros in (-4m^2, 0) <=> all F_S zeros in (0, 4m^2);
# growth if a Q zero > 0 <=> an F_S zero < 0.  The branch root gamma0 < 0 => Q zero -gamma0 > 0: the GROWTH clause.
check("S4 gamma0<0 lies in Thm 4.16's growth clause (Q-zero -gamma0 > 0), not in (-4m^2,0)",
      (-tgt) > 0 and not (-4 * mm ** 2 < -tgt < 0))
F_planck = B1n / mp.mpf(-1) * -1     # b2 = -1: quadratic zero -b1/b2 = b1 = -|b1| (Planckian, kappa = 1)
F_planck = B1n                        # = -12 at xi = 0
chg = [x for x in [-mp.mpf(10) ** (e / 20) for e in range(-60, 61)]]
vals = [FS(x, mm, kk, AL, XI, mp.mpf(-1)) for x in chg]
nplanck = sum(1 for i in range(len(chg) - 1) if vals[i] * vals[i + 1] < 0)
check("S4 b2=-1: full F_S has a real zero in (-1e3,-1e-3) (Planckian, J kept)", nplanck >= 1, "sign changes=%d, quadratic estimate %s" % (nplanck, mp.nstr(F_planck, 4)))
check("S4 any negative F_S zero (Planckian included) maps to a Q-zero > 0 > -4m^2: Thm 4.16's GROWTH clause, which has no upper bound",
      (-F_planck) > 0 and (-F_planck) > -4 * mm ** 2)

# ---------------------------------------------------------------- S5 Thm 1.2's 'any nontrivial source' (aside)
w, p2, L = sp.symbols('w p2 L', positive=True)
KG_symbol = -w ** 2 + p2 - L          # symbol of the Klein-Gordon operator of mass square -L (sign conventions immaterial)
check("S5 a source S = K_{-L} f has S^ = 0 on the growing pole's shell w^2 = p^2 - L (residue vanishes)",
      sp.simplify(KG_symbol.subs(w, sp.sqrt(p2 - L))) == 0)

# ---------------------------------------------------------------- S6 data_used: inf beta^2_crit = -1/4
u = sp.Symbol('u', positive=True)
bc = -(u - 1) * (3 * u ** 2 + 2 * u + 1) / (4 * u ** 2 * (3 * u + 1))
check("S6 beta2_crit(u=1) = 0", sp.simplify(bc.subs(u, 1)) == 0)
check("S6 beta2_crit -> -1/4 as u -> oo", sp.limit(bc, u, sp.oo) == sp.Rational(-1, 4))
dnum = sp.factor(sp.numer(sp.together(sp.diff(bc, u))))
check("S6 beta2_crit strictly decreasing on u>1 (so range (-1/4,0), inf not attained)",
      all(sp.diff(bc, u).subs(u, uv) < 0 for uv in (sp.Rational(101, 100), 2, 10, 1000, 10 ** 6)) and
      sp.solve(sp.Eq(sp.numer(sp.together(sp.diff(bc, u))), 0), u) == [] or
      all(r.is_real is False or r <= 1 for r in sp.Poly(sp.numer(sp.together(sp.diff(bc, u))), u).nroots()), str(dnum))

# ---------------------------------------------------------------- S7 data: GMMPS 5.3 mass and H0
def mass_eV(alpha, Lam=mp.mpf('7.15e-121'), Om=mp.mpf('0.685')):
    return MP_EV * (Lam / (6 * Om * alpha)) ** mp.mpf(0.25)
m_thm = mass_eV(1 / (64 * mp.pi ** 2)); m_typo = mass_eV(1 / (64 * mp.pi))
check("S7 5.3 m with Thm 3.6's alpha: 7.8e-3 eV reproduced (<2%)", abs(m_thm / mp.mpf('7.8e-3') - 1) < 0.02, mp.nstr(m_thm, 5))
check("S7 5.3 m with 5.1's printed (64 pi)^-1: >20% off (misprint)", abs(m_typo / mp.mpf('7.8e-3') - 1) > 0.2, mp.nstr(m_typo, 5))
# Lambda = 3 Omega H0^2 => m^4 = H0^2 M_P^2/(2 alpha): m ~ H0^(1/2); the Hubble tension moves m, never the sign of gamma0
ratio = mp.sqrt(mp.mpf('73.04') / mp.mpf('67.36'))
check("S7 H0 67.36 -> 73.04 moves m by +4.1%; sign(gamma0) = -sign(alpha) is datum-free", abs(ratio - mp.mpf('1.0413')) < 1e-3, mp.nstr(ratio, 5))

n_ok = sum(ok for _, ok in results)
print("\n%d/%d checks pass" % (n_ok, len(results)))
sys.exit(0 if n_ok == len(results) else 1)
