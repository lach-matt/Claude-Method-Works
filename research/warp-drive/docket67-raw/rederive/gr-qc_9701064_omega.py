#!/usr/bin/env python3
r"""
DOCKET 67 -- re-derivation of HPS (gr-qc/9701064 v1, p.8):
    omega_1^2 = 1/(16 K^2),  omega_2^2 = 1/(16 K^2 (4 + 3 ln F)),  K^2 = 1/(5760 pi).

INDEPENDENT TRANSCRIPTION.  HPS eqs. (5)-(7) are transcribed here afresh from
the alphaXiv page-text capture of gr-qc/9701064v1 (scratchpad d67/src/hps/
hps_0.xml, pp.4-5), NOT imported from research/warp-drive/hpscentre.py.  The
three disputed slots are parameters:
    a_tt   : tt log bracket, coefficient of f'^2 f''/f^3   (printed 16; conserved 116)
    ll_pow : ll log bracket, -4 f'^2 r'^2/(f^2 r^ll_pow)   (printed 1;  homogeneous 2)
    a_th   : thth log bracket, coefficient of f'^4/f^4      (printed 21)

CHECKS
  T0  transcription guard: the reading (116, 2, 21) is covariantly conserved
      identically for arbitrary f(l), r(l); the printed reading is not.
  T1  flat space f = f0, r = l solves all three equations for every f0.
  T2  FAR-ZONE (HPS's own regime): plane-wave ansatz phi = A e^{ikl}/l,
      rho = B e^{ikl} about f = F0 const, r = l, LEADING ORDER in 1/l
      (short-wavelength / WKB, K << l).  Dispersion in s = 16 K^2 k^2.
  T3  CENTRE (the tree's regime): exact spherical modes phi = A sin(kl)/l,
      rho' = B (sin kl - kl cos kl)/l about flat space; dispersion.
  T4  both of T2, T3 under ALL FOUR readings (a_tt, ll_pow) -- the disputed
      slots are quadratic or higher in the perturbation.
  T5  omega_1 from the TRACE equation alone: -R = 16 K^2 (box R) at linear
      order, log part traceless -> (box + 1/16K^2) R = 0.  A finite R^2
      counterterm rescales the box R coefficient c -> omega_1^2 = 1/(16 K^2 c).
  T6  numbers: K^2 = 8 pi * 1/(46080 pi^2) = 1/(5760 pi); 16 K^2 = 8 pi *
      1/(2880 pi^2) (AHL alpha = beta); pi/omega_1 = 4 pi K; 2 pi/omega_1 = 8 pi K;
      K and 4 pi K in l_P; omega_2/omega_1 at L0 = -2/3 and in the far zone
      on HPS's own fit F = (5.3 ln l - 25.5)^2; adiabaticity |d ln omega_2/dl|/omega_2.
Exit 0 iff every check passes.
"""
import math
import sys
import sympy as sp

FAILS = []


def chk(name, got, want):
    ok = (got == want)
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else "   got=%r want=%r" % (got, want)))
    if not ok:
        FAILS.append(name)


l = sp.Symbol('l', positive=True)
K2 = sp.Symbol('K2', positive=True)
a_tt, ll_pow, a_th = sp.symbols('a_tt ll_pow a_th')


def rhs(f, r):
    f1, f2, f3, f4 = [sp.diff(f, l, n) for n in (1, 2, 3, 4)]
    r1, r2, r3, r4 = [sp.diff(r, l, n) for n in (1, 2, 3, 4)]
    L = sp.log(f)
    tt_n = (32/r**4 + 7*f1**4/f**4 - 24*f1**3*r1/(f**3*r) + 24*f1**2*r1**2/(f**2*r**2)
            - 32*r1**4/r**4 + 4*f1**2*f2/f**3 - 12*f2**2/f**2 + 80*f1**2*r2/(f**2*r)
            - 160*f1*r1*r2/(f*r**2) + 128*r1**2*r2/r**3 - 64*f2*r2/(f*r) + 32*r2**2/r**2
            - 16*f1*f3/f**2 + 64*r1*f3/(f*r) - 96*f1*r3/(f*r) - 64*r1*r3/r**2
            + 16*f4/f - 64*r4/r)
    tt_l = (16/r**4 - 49*f1**4/f**4 + 44*f1**3*r1/(f**3*r) + 20*f1**2*r1**2/(f**2*r**2)
            - 16*r1**4/r**4 + a_tt*f1**2*f2/f**3 - 104*f1*r1*f2/(f**2*r) - 36*f2**2/f**2
            + 8*f1**2*r2/(f**2*r) - 80*f1*r1*r2/(f*r**2) + 64*r1**2*r2/r**3
            + 16*f2*r2/(f*r) + 16*r2**2/r**2 - 48*f1*f3/f**2 + 64*r1*f3/(f*r)
            - 16*f1*r3/(f*r) - 32*r1*r3/r**2 + 16*f4/f - 32*r4/r)
    ll_n = (f1**4/f**4 - 16*f1**3*r1/(f**3*r) + 64*f1*r1**3/(f*r**3) - 4*f1**2*f2/f**3
            + 64*f1*r1*f2/(f**2*r) - 64*r1**2*f2/(f*r**2) - 4*f2**2/f**2
            - 48*f1**2*r2/(f**2*r) + 32*f1*r1*r2/(f*r**2) + 32*f2*r2/(f*r)
            + 8*f1*f3/f**2 - 32*r1*f3/(f*r) - 32*f1*r3/(f*r))
    ll_l = (16/r**4 + 7*f1**4/f**4 - 20*f1**3*r1/(f**3*r) - 4*f1**2*r1**2/(f**2*r**ll_pow)
            + 32*f1*r1**3/(f*r**3) - 16*r1**4/r**4 - 12*f1**2*f2/f**3
            + 48*f1*r1*f2/(f**2*r) - 32*r1**2*f2/(f*r**2) - 4*f2**2/f**2
            - 16*f1**2*r2/(f**2*r) + 16*f1*r1*r2/(f*r**2) + 16*f2*r2/(f*r)
            - 16*r2**2/r**2 + 8*f1*f3/f**2 - 16*r1*f3/(f*r) - 16*f1*r3/(f*r)
            + 32*r1*r3/r**2)
    th_n = (17*f1**4/f**4 - 16*f1**3*r1/(f**3*r) - 32*f1*r1**3/(f*r**3) - 52*f1**2*f2/f**3
            + 32*f1*r1*f2/(f**2*r) + 32*r1**2*f2/(f*r**2) + 28*f2**2/f**2
            + 16*f1**2*r2/(f**2*r) + 64*f1*r1*r2/(f*r**2) - 32*f2*r2/(f*r)
            + 24*f1*f3/f**2 - 48*r1*f3/(f*r) + 32*f1*r3/(f*r) - 16*f4/f)
    th_l = (-16/r**4 + a_th*f1**4/f**4 - 12*f1**3*r1/(f**3*r) - 8*f1**2*r1**2/(f**2*r**2)
            - 16*f1*r1**3/(f*r**3) + 16*r1**4/r**4 - 52*f1**2*f2/f**3
            + 28*f1*r1*f2/(f**2*r) + 16*r1**2*f2/(f*r**2) + 20*f2**2/f**2
            + 4*f1**2*r2/(f**2*r) + 32*f1*r1*r2/(f*r**2) - 32*r1**2*r2/r**3
            - 16*f2*r2/(f*r) + 20*f1*f3/f**2 - 24*r1*f3/(f*r) + 16*f1*r3/(f*r)
            - 8*f4/f + 16*r4/r)
    return (K2*(tt_n + L*tt_l), K2*(ll_n + L*ll_l), K2*(th_n + L*th_l)), \
           ((tt_n, tt_l), (ll_n, ll_l), (th_n, th_l))


def einstein(f, r):
    f1, f2 = sp.diff(f, l), sp.diff(f, l, 2)
    r1, r2 = sp.diff(r, l), sp.diff(r, l, 2)
    return (2*r2/r + r1**2/r**2 - 1/r**2,
            f1*r1/(f*r) + r1**2/r**2 - 1/r**2,
            f2/(2*f) + r2/r + f1*r1/(2*f*r) - f1**2/(4*f**2))


def divergence(T, f, r):
    tt, ll, th = T
    f1, r1 = sp.diff(f, l), sp.diff(r, l)
    return sp.diff(ll, l) + f1/(2*f)*(ll - tt) + 2*r1/r*(ll - th)


READINGS = {"printed(16,r^1)": {a_tt: 16, ll_pow: 1, a_th: 21},
            "M1only(16,r^2)": {a_tt: 16, ll_pow: 2, a_th: 21},
            "M2only(116,r^1)": {a_tt: 116, ll_pow: 1, a_th: 21},
            "conserved(116,r^2)": {a_tt: 116, ll_pow: 2, a_th: 21}}

# ---------------------------------------------------------------- T0
fF, rF = sp.Function('f')(l), sp.Function('r')(l)
T, parts = rhs(fF, rF)
print("T0  transcription guard (conservation of the source, arbitrary f, r)")
for name, rd in READINGS.items():
    parts_r = [(n.subs(rd), g.subs(rd)) for n, g in parts]
    dn = sp.simplify(sp.expand(divergence([p[0] for p in parts_r], fF, rF)))
    dl = sp.simplify(sp.expand(divergence([sp.log(fF)*p[1] for p in parts_r], fF, rF)))
    tot = sp.simplify(sp.expand(dn + dl))
    conserved = (tot == 0)
    chk("  %-20s conserved identically = %s" % (name, name.startswith("conserved")),
        conserved, name.startswith("conserved"))
    if name.startswith("conserved"):
        # the ln f coefficient of the divergence must vanish by itself (mu arbitrary)
        Lsym = sp.Symbol('Lsym')
        dlog = sp.simplify(sp.expand(dl.subs(sp.log(fF), Lsym)).coeff(Lsym))
        chk("    ln f coefficient of the divergence vanishes on its own", dlog, 0)

# ---------------------------------------------------------------- T1
f0 = sp.Symbol('f0', positive=True)
L0 = sp.Symbol('L0', real=True)
Tb, _ = rhs(f0 + 0*l, l)
chk("T1  flat f = f0, r = l solves all three (every reading, every f0)",
    [sp.simplify(Tb[i].subs(a_tt, 116).subs(ll_pow, 2).subs(a_th, 21) - einstein(f0 + 0*l, l)[i])
     for i in range(3)], [0, 0, 0])

# ---------------------------------------------------------------- linearisation
eps = sp.Symbol('eps')
phi, rho = sp.Function('phi')(l), sp.Function('rho')(l)
fP, rP = f0*(1 + eps*phi), l + eps*rho
TP, _ = rhs(fP, rP)
GP = einstein(fP, rP)
lin_raw = [sp.expand(sp.diff(GP[i] - TP[i], eps).subs(eps, 0)) for i in range(3)]
lin_raw = [e.subs(sp.log(f0), L0) for e in lin_raw]


def lin_for(rd):
    return [sp.expand(e.subs(rd)) for e in lin_raw]


s = sp.Symbol('s')          # s = 16 K^2 k^2
k = sp.Symbol('k', positive=True)
A, B = sp.symbols('A B')


def sub_modes(e, ph, rh):
    reps = {}
    for n in (4, 3, 2, 1):
        reps[sp.Derivative(rho, (l, n))] = sp.diff(rh, l, n)
        reps[sp.Derivative(phi, (l, n))] = sp.diff(ph, l, n)
    e = e.subs(reps)
    return e.subs({rho: rh, phi: ph})


def disp_from_rows(rows):
    """rows: list of (cA, cB) linear forms; return the common determinant factor in s."""
    dets = []
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            d = sp.factor(sp.expand(rows[i][0]*rows[j][1] - rows[i][1]*rows[j][0]))
            if d != 0:
                dets.append(d)
    g = dets[0]
    for d in dets[1:]:
        g = sp.gcd(g, d)
    g = sp.factor(g.subs(k, sp.sqrt(s/(16*K2))))
    num = sp.numer(sp.together(g))
    polys = [fa for fa, _m in sp.factor_list(num)[1] if fa.has(s) and fa != s]
    return sp.expand(sp.prod(polys)), dets


# ---------------------------------------------------------------- T2 far zone
print("\nT2  FAR ZONE, plane wave, leading order in 1/l (HPS's regime)")
x = sp.Symbol('x', positive=True)   # x = 1/l
far_disp = {}
for name, rd in READINGS.items():
    rows = []
    for e in lin_for(rd):
        ee = sub_modes(e, A*sp.exp(sp.I*k*l)/l, B*sp.exp(sp.I*k*l))
        ee = sp.expand(sp.simplify(ee*sp.exp(-sp.I*k*l)))
        # leading power in 1/l
        ee = sp.expand(ee.subs(l, 1/x))
        pl = sp.Poly(ee, x)
        lo = min(m[0] for m in pl.monoms())
        lead = sp.expand(pl.coeff_monomial(x**lo))
        rows.append((sp.expand(lead.coeff(A)), sp.expand(lead.coeff(B))))
    D, dets = disp_from_rows(rows)
    far_disp[name] = D
    roots = sp.solve(D, s)
    print("   %-20s leading dispersion: %s = 0   roots s = %s" % (name, sp.factor(D), roots))
target = sp.expand((3*L0 + 4)*s**2 - (3*L0 + 5)*s + 1)
for name, D in far_disp.items():
    ratio = sp.simplify(D/target)
    chk("  %-20s far-zone dispersion prop. to (3L0+4)s^2-(3L0+5)s+1" % name,
        ratio.is_number and ratio != 0, True)
chk("  roots: s = 1 and s = 1/(3L0+4)  (omega_1^2 = 1/16K^2, omega_2^2 = 1/16K^2(4+3 ln F))",
    sorted([sp.simplify(v) for v in sp.solve(target, s)], key=str),
    sorted([sp.Integer(1), 1/(3*L0 + 4)], key=str))

# ---------------------------------------------------------------- T3 centre
print("\nT3  CENTRE, exact spherical modes about flat space (the tree's regime)")
Bs = sp.Symbol('Bs')
cen_disp = {}
for name, rd in READINGS.items():
    rows = []
    bare_rho = []
    for e in lin_for(rd):
        # bare rho must not enter: replace it by a symbol and check
        Rb = sp.Symbol('Rb')
        reps = {}
        uprime = B*(sp.sin(k*l) - k*l*sp.cos(k*l))/l
        for n in (4, 3, 2, 1):
            reps[sp.Derivative(rho, (l, n))] = sp.diff(uprime, l, n - 1)
            reps[sp.Derivative(phi, (l, n))] = sp.diff(A*sp.sin(k*l)/l, l, n)
        ee = e.subs(reps).subs({rho: Rb, phi: A*sp.sin(k*l)/l})
        ee = sp.expand(ee)
        bare_rho.append(sp.simplify(ee.coeff(Rb)))
        ee = sp.expand(sp.expand_trig(sp.expand(ee.subs(Rb, 0)*l**5)))
        cs = sp.collect(ee, [sp.sin(k*l), sp.cos(k*l)], evaluate=False)
        for v in cs.values():
            pv = sp.Poly(sp.expand(v), l)
            for c in pv.coeffs():
                c = sp.expand(c)
                rows.append((c.coeff(A), c.coeff(B)))
    D, dets = disp_from_rows(rows)
    cen_disp[name] = D
    chk("  %-20s bare rho absent from all three linear equations" % name, bare_rho, [0, 0, 0])
    ratio = sp.simplify(D/target)
    chk("  %-20s centre dispersion prop. to (3L0+4)s^2-(3L0+5)s+1" % name,
        ratio.is_number and ratio != 0, True)

# mode ratios at the two roots (conserved reading), exact residuals
rd = READINGS["conserved(116,r^2)"]
for kk2, ratio, lab in ((1/(16*K2), -2, "omega_1 mode, A = -2B"),
                        (1/(16*K2*(3*L0 + 4)), 4, "omega_2 mode, A = 4B")):
    kk = sp.sqrt(kk2)
    res = []
    for e in lin_for(rd):
        reps = {}
        uprime = (sp.sin(kk*l) - kk*l*sp.cos(kk*l))/l
        ph = ratio*sp.sin(kk*l)/l
        for n in (4, 3, 2, 1):
            reps[sp.Derivative(rho, (l, n))] = sp.diff(uprime, l, n - 1)
            reps[sp.Derivative(phi, (l, n))] = sp.diff(ph, l, n)
        res.append(sp.simplify(e.subs(reps).subs(phi, ph)))
    chk("  exact residuals, %s" % lab, res, [0, 0, 0])

# ---------------------------------------------------------------- T5 trace
print("\nT5  omega_1 from the trace equation alone (conserved reading)")
Glin = [sp.expand(sp.diff(g, eps).subs(eps, 0)) for g in GP]
Rlin = -(Glin[0] + Glin[1] + 2*Glin[2])           # G^a_a = -R
Tlin = [sp.expand(sp.diff(t, eps).subs(eps, 0).subs(sp.log(f0), L0).subs(rd)) for t in TP]
trT = sp.expand(Tlin[0] + Tlin[1] + 2*Tlin[2])
boxR = sp.diff(Rlin, l, 2) + 2/l*sp.diff(Rlin, l)
chk("  linear trace of source = 16 K^2 box R_lin  (and no L0: log part traceless)",
    sp.simplify(trT - 16*K2*boxR), 0)
chk("  hence -R = 16 K^2 box R, i.e. (box + 1/(16K^2)) R = 0: static k^2 = 1/(16 K^2)",
    sp.solve(sp.Eq(-1, 16*K2*(-k**2)), k**2), [1/(16*K2)])
c = sp.Symbol('c', real=True, nonzero=True)
chk("  box R coefficient rescaled to c (finite R^2 counterterm): k1^2 = 1/(16 K^2 c)",
    sp.solve(sp.Eq(-1, 16*K2*c*(-k**2)), k**2), [1/(16*K2*c)])
print("   (c < 0 turns the omega_1 ripple into a growing/decaying exponential: the ripple's")
print("    existence rests on the finite R^2 coupling being the one implicit in AHS/HPS)")

# ---------------------------------------------------------------- T6 numbers
print("\nT6  numbers")
chk("  K^2 = 8 pi/(46080 pi^2) = 1/(5760 pi)", sp.simplify(8*sp.pi/(46080*sp.pi**2) - 1/(5760*sp.pi)), 0)
chk("  16 K^2 = 8 pi * 1/(2880 pi^2)  (AHL eq. (6) alpha = beta)",
    sp.simplify(16/(5760*sp.pi) - 8*sp.pi/(2880*sp.pi**2)), 0)
Kp = 1/math.sqrt(5760*math.pi)
w1 = 1/(4*Kp)
print("   K = %.6f l_P;  omega_1 = 1/(4K) = %.4f l_P^-1" % (Kp, w1))
print("   pi/omega_1 = %.6f K = %.5f l_P (extremum spacing);  2 pi/omega_1 = %.6f K = 8 pi K"
      % (math.pi/w1/Kp, math.pi/w1, 2*math.pi/w1/Kp))
chk("  pi/omega_1 = 4 pi K", abs(math.pi/w1/Kp - 4*math.pi) < 1e-12, True)
chk("  RIPPLE_WINDOW_K = 8 pi = 2 pi/omega_1 in K (ONE full omega_1 period = TWO extremum spacings)",
    abs(2*math.pi/w1/Kp - 8*math.pi) < 1e-12, True)
r20 = 1/math.sqrt(3*(-2/3) + 4)
print("   omega_2/omega_1 at L0 = ln f(0) = -2/3: 1/sqrt(2) = %.6f" % r20)
a_fit, b_fit = 5.3, 25.5
for lK in (1e2, 1e3, 1e4, 1e5):
    Fv = (a_fit*math.log(lK) - b_fit)**2
    lnF = math.log(Fv)
    w2 = w1/math.sqrt(3*lnF + 4)            # in l_P^-1
    # adiabaticity: |d omega_2/dl| / omega_2^2, l in K units (HPS unit of l ambiguous)
    dlnF_dl = 2*a_fit/(lK*(a_fit*math.log(lK) - b_fit)) / Kp   # per l_P, taking l in K
    dlnw2 = 1.5*dlnF_dl/(3*lnF + 4)
    print("   l = %.0e K: F = %.1f, ln F = %.3f, omega_2/omega_1 = %.4f, |dln w2/dl|/w2 = %.2e, "
          "|F'/F|/omega_1 = %.2e" % (lK, Fv, lnF, w2/w1, dlnw2/w2, dlnF_dl/w1))
print("   (5.3 ln l - 25.5 > 0 needs l > e^(25.5/5.3) = %.1f in HPS's l unit)" % math.exp(b_fit/a_fit))

print("\nSUMMARY: %d FAIL" % len(FAILS))
sys.exit(1 if FAILS else 0)
