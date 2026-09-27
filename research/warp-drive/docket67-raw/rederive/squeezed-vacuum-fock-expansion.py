#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the Fock-basis expansion of the single-mode squeezed vacuum,
as used at research/warp-drive/fluctuation.py:419-446.  Imports nothing from research/.

Convention (Kuo & Ford gr-qc/9304008 eqs 3.11, 3.16, READ at source):
  S(zeta) = exp[ zeta* a^2/2 - zeta a+^2/2 ],  zeta = r e^{i delta},
  S+ a S = a cosh r - a+ e^{i delta} sinh r.
Claim audited:
  S(zeta)|0> = (cosh r)^{-1/2} sum_k (-e^{i delta} tanh r)^k sqrt((2k)!)/(2^k k!) |2k>.
"""
import itertools, sys
import sympy as sp
import mpmath as mp
import numpy as np
from scipy.linalg import expm

res = []
def chk(name, ok, detail=""):
    res.append(bool(ok)); print(("[PASS] " if ok else "[FAIL] ") + name + ("  -- " + detail if detail else ""))

# ---- A1: coefficients from the annihilation condition (sympy, symbolic)
# b = S a S+ = a cosh r + a+ e^{i d} sinh r annihilates S|0>  (since a|0> = 0).
r, d = sp.symbols('r delta', real=True)
k = sp.symbols('k', integer=True, nonnegative=True)
ch, sh, t = sp.cosh(r), sp.sinh(r), sp.tanh(r)
# recurrence from <n|b|psi> = 0 : cosh r sqrt(n+1) c_{n+1} + e^{id} sinh r sqrt(n) c_{n-1} = 0
def claim(kk):
    return (-sp.exp(sp.I*d)*t)**kk*sp.sqrt(sp.factorial(2*kk))/(2**kk*sp.factorial(kk))
# for GENERAL symbolic k >= 1: divide the n = 2k-1 row by c_{2k-2}; needs c_{2k}/c_{2k-2}
ratio = sp.gammasimp(claim(k) / claim(k - 1))          # -> -e^{id} tanh r (2k-1)^{1/2}... form
row = ch*sp.sqrt(2*k)*ratio + sp.exp(sp.I*d)*sh*sp.sqrt(2*k - 1)
row = sp.simplify(row.subs(t, sh/ch))
kp = sp.symbols('kp', integer=True, positive=True)
# row = (f - 1) * e^{id} sinh r * (positive), with f a product of positive square roots: f^2 == 1 => f == 1
f = sp.sqrt(kp)*sp.sqrt(1/(kp*(2*kp - 1)))*sp.sqrt(2*kp - 1)
ok = (sp.simplify(row.subs(k, kp) - (f - 1)*sp.exp(sp.I*d)*sh/sp.sqrt(1/(2*kp - 1))) == 0
      and sp.simplify(f**2) == 1 and f.is_positive)
print("   symbolic row reduces to (f-1)*e^{id} sinh r*sqrt(2k-1), f^2 =", sp.simplify(f**2), ", f>0:", f.is_positive)
# and, independently of simplification, on 15 concrete k at a rational r, delta to 40 digits
for kk in range(1, 16):
    lhs = ch*sp.sqrt(2*kk)*claim(kk) + sp.exp(sp.I*d)*sh*sp.sqrt(2*kk - 1)*claim(kk - 1)
    ok_n = abs(sp.N(lhs.subs({r: sp.Rational(7, 10), d: sp.Rational(9, 10)}), 40)) < 1e-35
    if not ok_n: print("   numeric row fails at k =", kk)
    ok &= ok_n
print("   ratio c_2k/c_2k-2 =", ratio, "; row residual =", row)
chk("A1 claimed c_2k satisfy the annihilation recurrence b S|0> = 0, general k (symbolic) + k=1..15 at 40 digits", ok)
# odd components: the n=0 row reads cosh r * c_1 = 0, and each even-n row propagates c_1 = 0 upward;
# checked numerically in B1 (odd entries of the matrix-exponential state).

# ---- A2: normalisation closed form: sum_k C(2k,k) (t^2/4)^k = (1-t^2)^{-1/2} = cosh r
x = sp.symbols('x', positive=True)
S = sp.summation(sp.binomial(2*k, k)*(x/4)**k, (k, 0, sp.oo))
S = sp.simplify(S)
norm = sp.simplify((S.subs(x, t**2)/ch).rewrite(sp.exp))
chk("A2 |c_0|^2 sum_k |c_2k/c_0|^2 = (1/cosh r) * (1 - tanh^2 r)^{-1/2} = 1", sp.simplify(norm - 1) == 0,
    "sum = %s" % S)

# ---- B: independent control -- S built as a matrix exponential in a truncated Fock space
def fock_expm(rr, dd, N=260):
    a = np.diag(np.sqrt(np.arange(1, N)), 1).astype(complex)
    ad = a.conj().T
    z = rr*np.exp(1j*dd)
    G = 0.5*(np.conj(z)*a@a - z*ad@ad)
    v = expm(G)[:, 0]
    return v
def formula(rr, dd, N):
    out = np.zeros(N, complex)
    tt = np.tanh(rr)
    for kk in range(N//2):
        out[2*kk] = complex((-mp.e**(1j*dd)*tt)**kk*mp.sqrt(mp.factorial(2*kk))/(2**kk*mp.factorial(kk))/mp.sqrt(mp.cosh(rr)))
    return out
worst = 0; oddmax = 0
for rr, dd in ((0.7, 0.0), (0.7, 0.9), (1.3, -2.0), (0.2, 3.0)):
    v = fock_expm(rr, dd); f = formula(rr, dd, len(v))
    err = np.max(np.abs(v[:120]-f[:120])); worst = max(worst, err)
    oddmax = max(oddmax, np.max(np.abs(v[1:120:2])))
chk("B  matrix-exponential S(zeta)|0> (260 levels) equals the formula on n<120 at 4 (r,delta)", worst < 1e-10,
    "max |diff| = %.2e" % worst)
chk("B1 odd Fock components of S(zeta)|0> vanish", oddmax < 1e-14, "max |c_odd| = %.2e" % oddmax)

# NOTE: C1/C3 floors are the n=160 truncation (D measures it), 17 orders below the tree's 1e-12.
# ---- C: the tree's CONTROL, reproduced with its own data (r=0.7, theta=1.1, nmax=160, dps=50),
#         against Wick/Isserlis moments computed here from scratch (not the tree's generating function)
mp.mp.dps = 50
R, TH, NMAX = mp.mpf('0.7'), mp.mpf('1.1'), 160
def cs_vec(R, dd, nmax, sign=-1):
    tt = mp.tanh(R); v = [mp.mpc(0)]*(nmax+1)
    for kk in range(nmax//2+1):
        v[2*kk] = (sign*mp.e**(1j*dd)*tt)**kk*mp.sqrt(mp.factorial(2*kk))/(2**kk*mp.factorial(kk))/mp.sqrt(mp.cosh(R))
    return v
def low(v): return [mp.sqrt(j+1)*v[j+1] for j in range(len(v)-1)] + [mp.mpc(0)]
def mom(v, m, n):   # <a+^m a^n> = <a^m psi | a^n psi>, WITH conjugation
    am, an = v[:], v[:]
    for _ in range(m): am = low(am)
    for _ in range(n): an = low(an)
    return mp.fsum(mp.conj(p)*q for p, q in zip(am, an))
def T2_fock(v, th):
    z = mp.e**(2j*th)
    return 6*mom(v,2,2) - 4*z*mom(v,1,3) - 4/z*mom(v,3,1) + z**2*mom(v,0,4) + z**-2*mom(v,4,0)
def rho_fock(v, th):
    z = mp.e**(2j*th)
    return 2*mom(v,1,1) - z*mom(v,0,2) - mom(v,2,0)/z
# Isserlis for normal-ordered <a+^m a^n>: contractions a+a -> N, aa -> M, a+a+ -> Mc (a+ left of a)
def wick(m, n, N, M, Mc):
    ops = ['d']*m + ['a']*n
    def pairs(lst):
        if not lst: yield 1; return
        i = lst[0]
        for j in lst[1:]:
            rest = [q for q in lst if q not in (i, j)]
            oi, oj = ops[i], ops[j]
            val = N if oi != oj else (M if oi == 'a' else Mc)
            for p in pairs(rest): yield val*p
    return mp.fsum(pairs(list(range(m+n))))
def T2_wick(R, dd, th):
    s, c = mp.sinh(R), mp.cosh(R)
    N, M = s**2, -mp.e**(1j*dd)*s*c; Mc = mp.conj(M)
    z = mp.e**(2j*th)
    return 6*wick(2,2,N,M,Mc) - 4*z*wick(1,3,N,M,Mc) - 4/z*wick(3,1,N,M,Mc) + z**2*wick(0,4,N,M,Mc) + z**-2*wick(4,0,N,M,Mc)
v = cs_vec(R, 0, NMAX)
tf, tw = T2_fock(v, TH), T2_wick(R, 0, TH)
rel = abs(tf-tw)/abs(tw)
chk("C1 tree data: Fock series (nmax=160, 50 dps) vs Isserlis moments", rel < mp.mpf('1e-25'), "rel diff = %s" % mp.nstr(rel, 3))
s, c = mp.sinh(R), mp.cosh(R)
rho_closed = 2*s*(s + c*mp.cos(2*TH))
chk("C2 rho from series = 2 sinh r (sinh r + cosh r cos 2theta) [KF 3.22 shape]",
    abs(rho_fock(v, TH) - rho_closed) < mp.mpf('1e-30'), "rho = %s" % mp.nstr(rho_closed.real, 15))
chk("C3 <:T^2:> = 3 rho^2 at the tree's point", abs(tf - 3*rho_closed**2)/abs(tf) < mp.mpf('1e-25'),
    "T2 = %s, 3rho^2 = %s" % (mp.nstr(tf.real, 15), mp.nstr(3*rho_closed**2, 15)))
kf323 = 2*s**2*(2*c**2*mp.cos(4*TH) - 8*s*c*mp.cos(2*TH) + 3*(s**2+c**2))
chk("C4 printed KF (3.23) differs from the series by > 1e-3 relative (as the tree records)",
    abs(tf-kf323)/abs(tf) > mp.mpf('1e-3'), "KF3.23 = %s vs %s" % (mp.nstr(kf323, 12), mp.nstr(tf.real, 12)))

# ---- D: truncation at nmax = 160: tail mass and effect on the 4th moment
tt = mp.tanh(R)
tail = mp.fsum(abs(x)**2 for x in cs_vec(R, 0, 2000)[NMAX+1:])
vbig = cs_vec(R, 0, 400)
dT = abs(T2_fock(vbig, TH) - tf)/abs(tf)
chk("D  tail beyond n=160 has norm^2 < 1e-30 and moves <:T^2:> by < 1e-25 relative (truncation, not precision, limits C1)",
    tail < mp.mpf('1e-30') and dT < mp.mpf('1e-25'), "tail = %s, dT = %s" % (mp.nstr(tail, 3), mp.nstr(dT, 3)))

# ---- E: 'phase absorbed into theta' -- with delta != 0 (complex coefficients, conjugated moments)
dd = mp.mpf('0.9')
vd = cs_vec(R, dd, NMAX)
e1 = abs(T2_fock(vd, TH) - T2_fock(v, TH + dd/2))/abs(tf)
e2 = abs(rho_fock(vd, TH) - rho_fock(v, TH + dd/2))
chk("E1 state at (theta, delta) = state at (theta + delta/2, 0) for rho and <:T^2:>", e1 < mp.mpf('1e-30') and e2 < mp.mpf('1e-30'),
    "rel %s, abs %s" % (mp.nstr(e1, 3), mp.nstr(e2, 3)))
# the tree's mom() omits conjugation: harmless only for real coefficients (delta = 0)
def mom_noconj(v, m, n):
    am, an = v[:], v[:]
    for _ in range(m): am = low(am)
    for _ in range(n): an = low(an)
    return mp.fsum(p*q for p, q in zip(am, an))
e3 = abs(mom_noconj(vd, 1, 1) - mom(vd, 1, 1))
chk("E2 (hypothesis check) un-conjugated overlap is wrong once delta != 0, right at delta = 0",
    e3 > mp.mpf('1e-3') and abs(mom_noconj(v, 1, 1) - mom(v, 1, 1)) < mp.mpf('1e-40'), "diff at delta=0.9: %s" % mp.nstr(e3, 4))

# ---- F: negative control -- wrong sign (+tanh r)^k is detected by the tree's check
vw = cs_vec(R, 0, NMAX, sign=+1)
ew = abs(T2_fock(vw, TH) - tw)/abs(tw)
chk("F  negative control: (+tanh r)^k fails the 1e-12 comparison", ew > mp.mpf('1e-3'), "rel = %s" % mp.nstr(ew, 4))

# ---- G: photon statistics as a consistency check: <n> = sinh^2 r, P(2k) sums to 1
nbar = mom(v, 1, 1)
chk("G  <a+a> = sinh^2 r and <a a> = -sinh r cosh r from the series", abs(nbar - s**2) < mp.mpf('1e-30')
    and abs(mom(v, 0, 2) + s*c) < mp.mpf('1e-30'), "<n> err %s, <aa> err %s" % (mp.nstr(abs(nbar - s**2), 3), mp.nstr(abs(mom(v, 0, 2) + s*c), 3)))

# ---- H: the source text actually read (banked alphaXiv full text of gr-qc/9304008v1)
import os, hashlib
KF = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "casmag", "all", "gr-qc_9304008v1.txt")
try:
    txt = open(KF, encoding="utf-8").read()
    quotes = ["a superposition of states containing even numbers of particles",
              "A general squeezed state for a single mode can be expressed as [8]",
              "[8] C. M. Caves, Phys. Rev. D 23, 1693 (1981).",
              "In a squeezed vacuum, α = 0, we may also take δ = 0, as this is simply a choice of phase"]
    flat = " ".join(txt.split())
    miss = [q for q in quotes if " ".join(q.split()) not in flat]
    chk("H  KF gr-qc/9304008v1 quotes string-matched in the banked full text", not miss,
        "md5 %s; missing: %s" % (hashlib.md5(txt.encode()).hexdigest(), miss))
except OSError as e:
    chk("H  KF banked full text readable", False, str(e))

print("\n%d/%d PASS" % (sum(res), len(res)))
sys.exit(0 if all(res) else 1)
