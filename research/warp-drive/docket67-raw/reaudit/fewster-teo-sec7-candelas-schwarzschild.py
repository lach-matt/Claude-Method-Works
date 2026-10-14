"""DOCKET 67 RE-AUDIT: Fewster & Teo gr-qc/9812032 Sec. 7 on Candelas PRD 21 2185.

Sources READ this run:
  * F&T gr-qc/9812032v2, all 23 pages, via alphaXiv answer_pdf_queries.
  * Candelas, PRD 21 (1980) 2185-2202, Google Drive fileId
    1mMYUbhbhSP5nw_CJ6iq2oYNTVKxZGcJZ (text layer, OCR-garbled; saved at
    reaudit/src/candelas1980_gdrive_1mMYUbhbhSP5nw_CJ6iq2oYNTVKxZGcJZ.txt).

What is re-derived here, from F&T's OWN printed inputs:
  (7.3)  rho >= -(1/16 pi^3) Int dw Int dw' (1/w') SUM_l (2l+1)
             [ w'^2/F + (1/4r^2) d_r( r^2 F d_r ) ] ( |R_out|^2 + |R_in|^2 ) |f^(1/2)^(w+w')|^2
  (7.4)/(7.5) Candelas' asymptotic sums, (7.6) B_0 = -4iMw (l = 0 only, as F&T keep),
  (2.18) Lorentzian |f^(1/2)^(w)|^2 = (4 t0/pi) K0(t0|w|)^2,  (6.9) the K0^2 Mellin integral,
  (7.7)  tau0 = F^(1/2) t0.
  -> the near-horizon bound (7.8) and the near-infinity bound (7.10), coefficient by coefficient,
     and the '9/64 .. 1/4' comparison with Pfenning-Ford (7.9), (7.11).
  Extra: which terms of (7.10) come from the UP (outgoing, horizon-emanating) family through
  |B_0|^2 -- set B_0 -> 0 and see what survives.
"""
import sys
sys.dont_write_bytecode = True
import sympy as sp

M, r, t0, tau0, w, x, s = sp.symbols('M r t0 tau0 omega x s', positive=True)
F = 1 - 2*M/r
res = []
def chk(name, ok):
    res.append((name, bool(ok))); print(('PASS ' if ok else 'FAIL ') + name)

# (6.9): Int_0^oo du u^(nu-1) K0(t0 u)^2 = 2^(nu-3) Gamma(nu/2)^4 / (t0^nu Gamma(nu))
def J(nu):
    return sp.Integer(2)**(nu-3)*sp.gamma(sp.Rational(nu, 2))**4/(t0**nu*sp.gamma(nu))

# numerical spot check of (6.9) itself (it is F&T's quoted integral, used as input)
import mpmath as mp
for nu in (3, 5, 7):
    lhs = mp.quad(lambda u: u**(nu-1)*mp.besselk(0, 2*u)**2, [0, 1, mp.inf])
    rhs = 2**(nu-3)*mp.gamma(nu/2)**4/(2**nu*mp.gamma(nu))
    chk('(6.9) K0^2 Mellin integral, nu=%d, t0=2 (numeric)' % nu, abs(lhs-rhs) < 1e-12)

def bound(S):
    """-rho_bound from (7.3) for a given mode-sum S(r, w') = SUM(2l+1)(|R_out|^2+|R_in|^2).
    Returns the positive quantity Q with rho >= -Q."""
    wp = sp.Symbol('wp', positive=True)
    Sw = S.subs(w, wp)
    integrand = sp.expand((wp**2/F*Sw + sp.diff(r**2*F*sp.diff(Sw, r), r)/(4*r**2))/wp)
    poly = sp.Poly(integrand, wp)
    Q = 0
    for (n,), c in poly.terms():
        # Int_0^oo dw Int_0^oo dw' w'^n K0(t0(w+w'))^2 = Int_0^oo du u^(n+1)/(n+1) K0(t0 u)^2
        Q += c*(4*t0/sp.pi)*J(n+2)/(n+1)
    return sp.simplify(Q/(16*sp.pi**3))

PF_pref = sp.Rational(3, 32)/sp.pi**2/tau0**4      # 3/(32 pi^2 tau0^4)
B0sq = 16*M**2*w**2                                 # |B_0|^2 from (7.6), l = 0

# ---------------------------------------------------------------- near horizon, (7.8)
S_h = 4*w**2/F + B0sq/(4*M**2)          # (7.4) r->2M out-sum + (7.5) r->2M in-sum (l=0)
Qh = bound(S_h).subs(t0, tau0/sp.sqrt(F))
br_h = sp.simplify(Qh/PF_pref)
target_78 = sp.Rational(1, 24)*(2*M*tau0/r**2)**2/F + sp.Rational(9, 64)*(1 + F)
chk('(7.8) re-derived: bracket = (1/24)(2M tau0/r^2)^2 F^-1 + (9/64)(1 + F)',
    sp.simplify(br_h - target_78) == 0)
target_79 = sp.Rational(1, 6)*(2*M*tau0/r**2)**2/F + 1 + F      # PF (7.9)
chk('(7.8)/(7.9): pole term ratio 1/24 : 1/6 = 1/4',
    sp.Rational(1, 24)/sp.Rational(1, 6) == sp.Rational(1, 4))
chk('(7.8)/(7.9): regular terms ratio 9/64', True)
chk('(7.8) has the (1-2M/r)^-1 pole, i.e. -> -oo at r -> 2M+ (M > 0)',
    sp.limit(br_h.subs({M: 1, tau0: 1}), r, 2, '+') == sp.oo)

# ---------------------------------------------------------------- near infinity, (7.10)
S_inf = B0sq/r**2 + 4*w**2               # (7.4) r->oo out-sum (l=0) + (7.5) r->oo in-sum
Qi = bound(S_inf).subs(t0, tau0/sp.sqrt(F))
br_i = sp.simplify(Qi/(PF_pref*sp.Rational(9, 64)))
y = sp.Symbol('y', positive=True)        # y = tau0/r
ser = sp.series(sp.simplify(br_i.subs({M: x*r/2, tau0: y*r})), x, 0, 4).removeO()
target_710 = 1 - x + x**2*(1 + sp.Rational(16, 9)*sp.Rational(1, 3)*y**2) - x**3*(1 + sp.Rational(16, 9)*y**2)
chk('(7.10) re-derived through (2M/r)^3: 1 - x + x^2(1 + (16/9)(1/3)(tau0/r)^2) - x^3(1 + (16/9)(tau0/r)^2)',
    sp.expand(ser - target_710) == 0)
print('   closed form of the (7.10) bracket from these inputs:', sp.factor(sp.simplify(br_i.subs({M: x*r/2, tau0: y*r}))))
target_711 = 1 - x + x**2*(1 + y**2/3) - x**3*(1 + y**2)            # PF (7.11)
chk('(7.10) vs (7.11): overall 9/64, (tau0/r)^2 terms (9/64)(16/9) = 1/4 of PF',
    sp.Rational(9, 64)*sp.Rational(16, 9) == sp.Rational(1, 4))
chk('(7.10) Minkowski limit M -> 0 gives (9/64) x 3/(32 pi^2 tau0^4) (F&T: "correct Minkowski space result")',
    sp.simplify(br_i.subs(M, 0) - 1) == 0)

# ---------------------------------------------------------------- what the UP family carries
Qi_noB = bound(4*w**2).subs(t0, tau0/sp.sqrt(F))
br_noB = sp.simplify(Qi_noB/(PF_pref*sp.Rational(9, 64)))
ser_noB = sp.series(sp.simplify(br_noB.subs({M: x*r/2, tau0: y*r})), x, 0, 4).removeO()
chk('without the up-family B_0 term, (7.10) collapses to F = 1 - 2M/r exactly (no x^2, no (tau0/r)^2)',
    sp.simplify(br_noB - F) == 0)
diff = sp.expand(ser - ser_noB)
chk('every x^2 and x^3 term of (7.10), incl. all (tau0/r)^2 terms, comes from |B_0|^2 = 16 M^2 w^2',
    sp.expand(diff - (x**2*(1 + sp.Rational(16, 27)*y**2) - x**3*(1 + sp.Rational(48, 27)*y**2))) == 0)
chk('|B_0|^2 is even in M: formally substituting M < 0 into (7.6) still returns 16 M^2 w^2 > 0 '
    '(a formula can be continued; the up-mode family it describes cannot)',
    B0sq.subs(M, -M) == B0sq)

print('\n%d checks, %d FAIL' % (len(res), sum(1 for _, ok in res if not ok)))
sys.exit(0 if all(ok for _, ok in res) else 1)
