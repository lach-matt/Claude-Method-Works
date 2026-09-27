#!/usr/bin/env python3
r"""
DOCKET 67 audit -- Kuo & Ford, gr-qc/9304008 v1, Eqs. (3.18), (3.19), (3.22), (3.23).
Independent re-derivation. Does NOT import fluctuation.py and shares no code with it.

Route W (Weyl algebra): <alpha,zeta| a+^m a^n |alpha,zeta> by Heisenberg transform
    D+ S+ a S D = alpha + c a - w s a+,  w = e^{i delta},  s = sinh r, c = cosh r   (KF 3.14-3.17)
then explicit normal ordering of words in {a, a+} with [a,a+] = 1 and vacuum expectation.
Route F (Fock, numeric, 40 digits): the state D(alpha)S(zeta)|0> built in a truncated Fock space
by mpmath matrix exponentials of KF's own (3.10),(3.11), and <psi|:T00^2:|psi> by matrices.
Operator: :T00: = K (2 a+a - z a^2 - zbar a+^2), z = e^{2 i theta}  (KF (3.18) first line with
(2.12)-(2.14)); :T00^2: its full normal-ordered square (KF (3.2)-(3.6): normal ordering w.r.t.
the Minkowski vacuum; the n = 0 diagonal term is removed).

C1  Route W reproduces KF (3.18) and (3.22) symbolically.
C2  Route W <:T^2:> vs KF (3.19) and (3.23): symbolic difference; values at the tree's points.
C3  Route F agrees with Route W at generic points (controls W); KF (3.19) does not.
C4  Squeezed vacuum (any delta): <:T^2:> = 3 rho^2 identically; Delta = 2/3 wherever rho != 0.
C5  Closed form: :T00: = K :Q^2:, Q Hermitian quadrature; rho = K(mu^2+v), <:T^2:> = K^2(mu^4+6mu^2 v+3v^2).
C6  Structural: exact results depend on (theta,gamma,delta) only through theta+gamma, 2theta+delta
    (U(1) phase covariance). KF (3.18) does; KF (3.19) does not -- shown numerically.
C7  Fairness: alternative conventions tried for (3.19)/(3.23): squeeze sign flipped (delta -> delta+pi),
    gamma sign flipped, and <:T::T:> - <0|:T::T:|0> instead of full normal ordering.  Report which, if any,
    reproduce the print.
C8  Cross-key (context for gr-qc/9304008-qualitative-conclusion, NOT graded here): at KF's own Fig.1/2
    parameters (gamma = delta = 0, theta = pi/2) the exact Delta vanishes on the curve 1 - e^{-2r} = 8 s^2
    where rho < 0.  KF p.9: 'By the point that the state is sufficiently squeezed to have rho < 0, we always
    have that Delta is at least of order unity.'
"""
import sys
import sympy as sp
import mpmath as mpm

FAILS = []


def chk(label, ok, info=""):
    print("  [%s] %s %s" % ("ok" if ok else "XX", label, info))
    if not ok:
        FAILS.append(label)


# ------------------------------------------------------------------ Route W: Weyl algebra
def mul(P, Q):
    out = {}
    for w1, c1 in P.items():
        for w2, c2 in Q.items():
            out[w1 + w2] = out.get(w1 + w2, 0) + c1 * c2
    return out


def add(P, Q, k=1):
    out = dict(P)
    for w, c in Q.items():
        out[w] = out.get(w, 0) + k * c
    return out


def normal_order(P):
    """words over 'a' (annihilation) and 'A' (creation); rewrite aA -> Aa + 1."""
    done = {}
    todo = dict(P)
    while todo:
        w, c = todo.popitem()
        i = w.find('aA')
        if i < 0:
            done[w] = done.get(w, 0) + c
            continue
        for nw in (w[:i] + 'Aa' + w[i + 2:], w[:i] + w[i + 2:]):
            todo[nw] = todo.get(nw, 0) + c
    return {w: c for w, c in done.items() if sp.simplify(c) != 0}


def vac(P):
    return sp.expand(normal_order(P).get('', 0))


r, th, gam, dl, S, K = sp.symbols('r theta gamma delta s_alpha K', real=True)
sh, ch = sp.sinh(r), sp.cosh(r)
E = lambda x: sp.exp(sp.I * x)
al, alc = S * E(gam), S * E(-gam)
w, wc = E(dl), E(-dl)
z, zc = E(2 * th), E(-2 * th)

a_t = {'': al, 'a': ch, 'A': -w * sh}            # D+S+ a SD
A_t = {'': alc, 'A': ch, 'a': -wc * sh}          # D+S+ a+ SD


def moment(m, n, at=a_t, At=A_t):
    P = {'': 1}
    for _ in range(m):
        P = mul(P, At)
    for _ in range(n):
        P = mul(P, at)
    return vac(P)


def exact_moments(at=a_t, At=A_t):
    M = {(m, n): moment(m, n, at, At) for (m, n) in
         [(1, 1), (0, 2), (2, 0), (2, 2), (1, 3), (3, 1), (0, 4), (4, 0)]}
    rho = K * (2 * M[1, 1] - z * M[0, 2] - zc * M[2, 0])
    T2 = K**2 * (6 * M[2, 2] - 4 * z * M[1, 3] - 4 * zc * M[3, 1] + z**2 * M[0, 4] + zc**2 * M[4, 0])
    return M, sp.expand(rho), sp.expand(T2)


def trig(e):
    return sp.simplify(sp.expand(sp.expand_complex(sp.expand(e.rewrite(sp.exp)))).rewrite(sp.cos))


def iszero(e):
    e = sp.expand(sp.expand_complex(sp.expand(e)))
    e = sp.simplify(e.rewrite(sp.exp))
    if e == 0:
        return True
    # numeric fallback at random points (exact identity check backup)
    import random
    random.seed(1)
    for _ in range(6):
        pt = {r: random.uniform(0.1, 1.5), th: random.uniform(0, 6), gam: random.uniform(0, 6),
              dl: random.uniform(0, 6), S: random.uniform(0.1, 2), K: 1}
        if abs(complex(sp.N(e.subs(pt), 30))) > 1e-20:
            return False
    return True


# KF's printed equations, transcribed from the v1 text layer (d67/src/casmag/all/gr-qc_9304008v1.txt:1100-1197)
cos = sp.cos
KF318 = 2 * K * (sh * ch * cos(2 * th + dl) + sh**2 + S**2 * (1 - cos(2 * (th + gam))))
KF319 = 2 * K**2 * (S**4 * (cos(4 * (th + gam)) - 4 * cos(2 * (th + gam)) + 3)
                    + 3 * S**2 * (2 * sh * ch * (2 * cos(2 * th + dl + 2 * gam) - cos(4 * th + dl + 2 * gam))
                                  + 4 * sh**2 * (cos(2 * gam) - cos(2 * th)) - cos(dl + 2 * gam))
                    + 3 * sh**2 * (ch**2 * cos(4 * th + 2 * dl) + 3 - 4 * cos(2 * th)))
KF322 = 2 * K * sh * (ch * cos(2 * th) + sh)
KF323 = 2 * K**2 * sh**2 * (2 * ch**2 * cos(4 * th) - 8 * sh * ch * cos(2 * th) + 3 * (sh**2 + ch**2))

print("gr-qc_9304008-eq3.18-3.23.py -- independent re-derivation\n")
M, rho, T2 = exact_moments()
sv = {S: 0, dl: 0}

print("C1  <:T00:>")
chk("KF (3.18) equals the exact squeezed-coherent <:T00:>", iszero(rho - KF318))
chk("KF (3.22) equals the exact squeezed-vacuum <:T00:> (alpha=0, delta=0)", iszero(rho.subs(sv) - KF322))

print("C2  <:T00^2:>")
d319 = iszero(T2 - KF319)
d323 = iszero(T2.subs(sv) - KF323)
chk("KF (3.19) is NOT the exact squeezed-coherent <:T00^2:>", not d319)
chk("KF (3.23) is NOT the exact squeezed-vacuum <:T00^2:>", not d323)
T2sv = trig(T2.subs(sv))
print("      exact squeezed vacuum <:T^2:> =", sp.factor(T2sv))
print("      KF (3.23)                    =", KF323)
print("      exact - KF(3.23)            =", sp.simplify(sp.expand(sp.expand_trig(T2sv - KF323))))
pts = [("tree r=3/10, theta=0.2", sp.Rational(3, 10), sp.Rational(1, 5)),
       ("tree r=3/10, theta=19pi/40", sp.Rational(3, 10), 19 * sp.pi / 40),
       ("tree control r=0.7, theta=1.1", sp.Rational(7, 10), sp.Rational(11, 10))]
for name, rv, tv in pts:
    sub = {r: rv, th: tv, K: 1}
    re_ = lambda e: (lambda c: (c.real if abs(c.imag) < 1e-25 else float('nan')))(complex(sp.N(e, 40)))
    ex = re_(T2sv.subs(sub)); kf = re_(KF323.subs(sub))
    rh = re_(rho.subs(sv).subs(sub))
    print("      %-30s rho=%+.6f  exact<:T^2:>=%.6f  3rho^2=%.6f  KF(3.23)=%.6f  Delta_exact=%.6f  Delta_KF=%.6f"
          % (name, rh, ex, 3 * rh**2, kf, abs(ex - rh**2) / abs(ex), abs(kf - rh**2) / abs(kf)))

print("C3  Route F (Fock numeric) controls Route W")
mpm.mp.dps = 40
NMAX = 90


def fock_check(rv, tv, gv, dv, sv_):
    a = mpm.zeros(NMAX, NMAX)
    for n in range(1, NMAX):
        a[n - 1, n] = mpm.sqrt(n)
    ad = a.T
    alpha = sv_ * mpm.expj(gv); zeta = rv * mpm.expj(dv)
    Sop = mpm.expm((mpm.conj(zeta) * a * a - zeta * ad * ad) / 2)
    Dop = mpm.expm(alpha * ad - mpm.conj(alpha) * a)
    v0 = mpm.zeros(NMAX, 1); v0[0] = 1
    psi = Dop * (Sop * v0)
    zz = mpm.expj(2 * tv)
    T1 = 2 * ad * a - zz * a * a - mpm.conj(zz) * ad * ad
    T2o = (6 * ad * ad * a * a - 4 * zz * ad * a * a * a - 4 * mpm.conj(zz) * ad * ad * ad * a
           + zz**2 * a**4 + mpm.conj(zz)**2 * ad**4)
    ev = lambda O: (psi.H * (O * psi))[0]
    tail = sum(abs(psi[n])**2 for n in range(NMAX - 10, NMAX))
    return ev(T1), ev(T2o), tail


for (rv, tv, gv, dv, s_) in [(0.4, 0.3, 0.9, 1.7, 0.6), (0.7, 1.1, 0.0, 0.0, 0.0), (0.25, 2.0, -0.4, 0.5, 1.1)]:
    f1, f2, tail = fock_check(mpm.mpf(rv), mpm.mpf(tv), mpm.mpf(gv), mpm.mpf(dv), mpm.mpf(s_))
    sub = {r: rv, th: tv, gam: gv, dl: dv, S: s_, K: 1}
    w1 = complex(sp.N(rho.subs(sub), 30)); w2 = complex(sp.N(T2.subs(sub), 30))
    k2 = complex(sp.N(KF319.subs(sub), 30))
    chk("F=W at (r,theta,gamma,delta,s)=%s  (tail %.1e)" % ((rv, tv, gv, dv, s_), float(tail)),
        abs(complex(f1) - w1) < 1e-15 and abs(complex(f2) - w2) < 1e-15 * max(1, abs(w2)),
        "rho=%.10f  <:T^2:>=%.10f  KF(3.19)=%.10f" % (w1.real, w2.real, k2.real))

print("C4  squeezed vacuum identity")
Mv, rho_v, T2_v = exact_moments({'': 0, 'a': ch, 'A': -w * sh}, {'': 0, 'A': ch, 'a': -wc * sh})
chk("<:T^2:> = 3 rho^2 identically, any delta", iszero(T2_v - 3 * rho_v**2))

print("C5  quadrature closed form")
mu, v = sp.symbols('mu v', real=True)
Qmean = sp.expand(-sp.I * (E(th) * al - E(-th) * alc))
vn = sp.expand(-(z * (M[0, 2] - al**2) + zc * (M[2, 0] - alc**2)) + 2 * (M[1, 1] - al * alc))
chk("rho = K(mu^2 + v)", iszero(rho - K * (Qmean**2 + vn)))
chk("<:T^2:> = K^2(mu^4 + 6 mu^2 v + 3 v^2)", iszero(T2 - K**2 * (Qmean**4 + 6 * Qmean**2 * vn + 3 * vn**2)))

print("C6  U(1) phase covariance (theta+phi, gamma-phi, delta-2phi)")
ph = sp.Rational(7, 10)
shift = {th: th + ph, gam: gam - ph, dl: dl - 2 * ph}
base = {r: sp.Rational(1, 2), th: sp.Rational(2, 5), gam: sp.Rational(3, 10), dl: sp.Rational(6, 5), S: sp.Rational(4, 5), K: 1}  # exact rationals: float inputs cap the check at 1e-15


def val(e, sft):
    return complex(sp.N(e.subs(sft, simultaneous=True).subs(base), 30)) if sft else complex(sp.N(e.subs(base), 30))


_dT = abs(val(T2, shift) - val(T2, None)); _dR = abs(val(rho, shift) - val(rho, None))
chk("exact <:T^2:> is covariant (rel. 1e-20)", _dT < 1e-20 * max(1, abs(val(T2, None))), "|diff| = %.3e, |value| = %.6f" % (_dT, abs(val(T2, None))))
chk("exact rho is covariant", _dR < 1e-20, "|diff| = %.3e" % _dR)
chk("KF (3.18) is covariant", abs(val(KF318, shift) - val(KF318, None)) < 1e-20)
cov319 = abs(val(KF319, shift) - val(KF319, None))
chk("KF (3.19) is NOT covariant (structural, independent of algebra)", cov319 > 1e-6, "|shift diff| = %.6f" % cov319)

print("C7  alternative conventions, fairness")
alts = {}
# squeeze sign flipped: S+ a S = a c + w s a+   <=> delta -> delta + pi
alts['squeeze sign flipped'] = T2.subs(dl, dl + sp.pi)
alts['gamma sign flipped'] = T2.subs(gam, -gam)
alts['theta sign flipped'] = T2.subs(th, -th)
# <:T::T:> - vacuum part, not fully normal ordered
Tw = {'Aa': 2, 'aa': -z, 'AA': -zc}
TT = mul(Tw, Tw)


def ev_word_poly(P, at, At):
    tot = 0
    for wd, cf in P.items():
        Q = {'': cf}
        for ch_ in wd:
            Q = mul(Q, At if ch_ == 'A' else at)
        tot += vac(Q)
    return sp.expand(tot)


TTv = ev_word_poly(TT, {'': 0, 'a': 1}, {'': 0, 'A': 1})
alts['<:T::T:> - <0|:T::T:|0>'] = sp.expand(K**2 * (ev_word_poly(TT, a_t, A_t) - TTv))
for name, ex in alts.items():
    m319 = iszero(ex - KF319)
    m323 = iszero(ex.subs(sv) - KF323)
    print("      %-28s reproduces (3.19): %s   reproduces (3.23): %s" % (name, m319, m323))
    chk("  convention '%s' does not rescue the print" % name, not m319 and not m323)
# and (3.18) under the same alternatives, to show convention is pinned by (3.18)
chk("(3.18) itself pins the conventions: squeeze-flip breaks it", not iszero(rho.subs(dl, dl + sp.pi) - KF318))

print("C8  cross-key context: KF Fig.1/2 parameters gamma=delta=0, theta=pi/2")
fig = {gam: 0, dl: 0, th: sp.pi / 2, K: 1}
rv = sp.Rational(1, 2)
s2 = (1 - sp.exp(-1)) / 8
pt = dict(fig); pt.update({r: rv, S: sp.sqrt(s2)})
rho_pt = sp.re(sp.N(rho.subs(pt), 40)); T2_pt = sp.re(sp.N(T2.subs(pt), 40))
kf_pt = sp.re(sp.N(KF319.subs(pt), 40))
D_ex = abs(T2_pt - rho_pt**2) / abs(T2_pt)
D_kf = abs(kf_pt - rho_pt**2) / abs(kf_pt)
chk("rho < 0 at r=1/2, s^2=(1-e^-1)/8", rho_pt < 0, "rho/K = %s" % sp.N(rho_pt, 12))
chk("exact Delta = 0 there (<:T^2:> = rho^2)", abs(D_ex) < 1e-25, "Delta_exact = %s" % sp.N(D_ex, 6))
f1, f2, tail = fock_check(mpm.mpf('0.5'), mpm.pi / 2, mpm.mpf(0), mpm.mpf(0), mpm.sqrt((1 - mpm.e**-1) / 8))
chk("  Fock control agrees: Delta = 0", abs((f2 - f1**2) / f2) < 1e-25, "rho=%s" % mpm.nstr(f1.real, 12))
print("      KF's printed (3.19) gives Delta = %s at the same point" % sp.N(D_kf, 6))
# grid census of exact Delta over the rho<0 region at Fig.1 parameters
import math
cnt = small = 0
dmin = 1e9
for i in range(1, 201):
    for j in range(0, 201):
        rr = 2.0 * i / 200; ss = 2.0 * j / 200
        x = 4 * ss * ss; vv = math.exp(-2 * rr) - 1
        if x + vv < 0:
            den = x * x + 6 * x * vv + 3 * vv * vv
            if den == 0:
                continue
            D = abs(2 * vv * (2 * x + vv)) / abs(den)
            cnt += 1; small += D < 0.1; dmin = min(dmin, D)
print("      grid r in (0,2], s in [0,2]: %d rho<0 points, %d with exact Delta < 0.1, min %.2e" % (cnt, small, dmin))
chk("exact Delta takes values < 0.1 in the rho<0 region at KF's Fig.1 parameters", small > 0)

print("C9  internal consistency of the print: does KF (3.19) at alpha=0, delta=0 give KF (3.23)?")
k319sv = sp.expand(KF319.subs(sv))
print("      KF (3.19) at s_alpha=0, delta=0 =", sp.factor(k319sv))
chk("KF (3.19) and KF (3.23) DISAGREE with each other (v1 print internally inconsistent)", not iszero(k319sv - KF323))
chk("KF (3.19) at alpha=0 is not 3 rho^2 either", not iszero(k319sv - 3 * KF322**2))
chk("both printed <:T^2:> vanish at r=0 ('As required', KF p.8)", iszero(KF323.subs(r, 0)) and iszero(k319sv.subs(r, 0)))

print()
if FAILS:
    print("FAILED: %d -- %s" % (len(FAILS), FAILS))
    sys.exit(1)
print("ALL CHECKS PASS")
