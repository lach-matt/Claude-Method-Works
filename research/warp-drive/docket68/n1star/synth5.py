#!/usr/bin/env python3
"""synth5.py -- the harmonic sum in sections 10.27 (a) and 10.33 (a): the gauge 1-forms of the scalar and vector types
on five-dimensional Tangherlini have coefficients bounded uniformly in the harmonic degree, which Lemma 10.54
(N1STAR-PROOF.md section 10.73; D143) turns into convergence of the sum.  Labels: computed (exact, sympy).

Sections 10.27 (a) and 10.33 (a) write h, harmonic by harmonic, as delta* of a gauge 1-form, and say that the gauge
1-forms' coefficients are "bounded by polynomial multiples in l" of h's, so that the sum converges with h's.  Here the
coefficients are computed with gmodes5.py's harmonics ([KI03] H. Kodama and A. Ishibashi, arXiv:hep-th/0305147v3, n =
3, K = 1), the harmonic entering through its jets at a point of S^3 as there.

  S1 (computed, exact) Scalar type, harmonic S with (Delta + k^2) S = 0: the 1-form omega = A_t S dt + A_r S dr + r^2 B
     (-D_i S/k) dz^i that removes f_a and H_T from h has B = -2 H_T/k and A_a = -(2 r/k)(f_a + (r/k) d_a H_T), every
     coefficient c(r) k^-p with p >= 1; with it h - delta* omega has [KI03] (2.7)'s F and F_ab (gmodes5.py's check).
     Mutant: H_T's harmonic taken without its 1/k^2, where B carries k.
  S2 (computed, exact) Vector type, harmonic V with D^i V_i = 0, (Delta + k_V^2) V = 0: delta*(r^2 B V_i dz^i) shifts
     f_a by (r/2) d_a B and H_T by -k_V B/2, so the gauge 1-form is B = -2 H_T/k_V, coefficient k_V^-1.  Mutant: as S1.
  S3 (computed, exact) The scalar floor: the restriction to S^3 of Re (x_1 + i x_2)^l, harmonic and homogeneous of
     degree l on R^4, has Delta_(S^3) = -l(l + 2) for l = 1, ..., 6 (gmodes5.py's coordinates), and l(l - 1) + 3 l =
     l(l + 2) for every l (the radial part of Delta_(R^4) on rho^l); so k^2 = l(l + 2) >= 8 for l >= 2.  Control: S^2,
     where -l(l + 1).  Mutant: the S^2 count claimed for S^3.

sympy; imports gmodes5.py.  python3 synth5.py [--selftest | --mutants | --only N]   (about a minute)
"""
import sys
import time
import sympy as sp
from damping5 import Checklist
import gmodes5 as G

t, r = G.t, G.r


def kpow(e, k):
    """the exponent p if e = c * k^p with c free of k, else None"""
    e = sp.simplify(e)
    if e == 0:
        return 0
    c, kp = e.as_independent(k, as_Mul=True)
    if kp == 1:
        return 0
    if kp == k:
        return 1
    if kp.is_Pow and kp.base == k and kp.exp.is_Integer:
        return int(kp.exp)
    return None


def coeffs(e, basis):
    e = sp.expand(e)
    out = [e.coeff(b) for b in basis]
    rest = sp.simplify(e - sum(c * b for c, b in zip(out, basis)))
    return out, rest


def s1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    k = G.K[2]
    cs, ok, gs, okg, parts = G.scalar_E(k)
    c = dict((p[0].name, p[0]) for p in parts)
    At, Ar, B = [sp.Function(nm)(t, r) for nm in ("A_t", "A_r", "B")]
    fa = [sp.Function(nm)(t, r) for nm in ("f_t", "f_r")]
    HT = sp.Function("H_T")(t, r)
    HTn = HT if control != 1 else HT * k**2                 # mutant: H_T's harmonic without its 1/k^2
    Bs = sp.solve(sp.Eq(gs[c["c_T"]], HTn), B)[0]
    As = sp.solve([sp.Eq(gs[c["c_t"]].subs(B, Bs).doit(), fa[0]), sp.Eq(gs[c["c_r"]].subs(B, Bs).doit(), fa[1])],
                  [At, Ar], dict=True)[0]
    basis = [fa[0], fa[1], HT, sp.diff(HT, t), sp.diff(HT, r)]
    exact = control == 1 or (sp.simplify(Bs + 2 * HT / k) == 0 and all(
        sp.simplify(As[A_] + 2 * r / k * (fa[i] + r / k * sp.diff(HT, [t, r][i]))) == 0
        for i, A_ in enumerate((At, Ar))))
    chk("scalar type: B = -2 H_T/k and A_a = -(2 r/k)(f_a + (r/k) d_a H_T) remove f_a and H_T", okg and exact)
    pows = []
    for e in (Bs, As[At], As[Ar]):
        cf, rest = coeffs(e, basis)
        pows += [kpow(q, k) for q in cf if q != 0] + ([None] if rest != 0 else [])
    chk(f"scalar type: every coefficient is c(r) k^-p with p >= 1 (exponents {sorted(set(pows), key=str)})",
        all(p is not None and p <= -1 for p in pows))
    chk("scalar type: h - delta* omega has [KI03] (2.7)'s F and F_ab with (2.8)'s X_a (gmodes5.py's check)",
        G.scalar_gauge_check(k, gs, parts))
    return chk.ok


def s2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    kV = G.K[1]
    cs, ok, gs, okg, (Ft, Fr, B), parts = G.vector_E(kV)
    ct, cr, cT = [p[0] for p in parts]
    shifts = okg and all(sp.simplify(gs[cc] - w) == 0 for cc, w in ((ct, r * sp.diff(B, t) / 2),
                                                                  (cr, r * sp.diff(B, r) / 2), (cT, -kV * B / 2)))
    chk("vector type: delta*(r^2 B V_i dz^i) shifts f_a by (r/2) d_a B and H_T by -k_V B/2", shifts)
    HT = sp.Function("H_T")(t, r)
    Bs = sp.solve(sp.Eq(gs[cT], HT if control != 1 else HT * kV**2), B)[0]
    p = kpow(sp.simplify(Bs / HT), kV)
    chk(f"vector type: the gauge 1-form removing H_T is B = -2 H_T/k_V, coefficient k_V^{p}",
        p is not None and p <= -1 and (control == 1 or sp.simplify(Bs + 2 * HT / kV) == 0))
    return chk.ok


def s3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ch, th, ph, rho, l = sp.symbols("chi theta phi rho l", positive=True)
    # R^4 in hyperspherical coordinates: x1 = cos chi, x2 = sin chi cos theta (gmodes5.py's chi, theta, phi on S^3)
    x1, x2 = sp.cos(ch), sp.sin(ch) * sp.cos(th)
    lap = lambda Y: (sp.diff(sp.sin(ch)**2 * sp.diff(Y, ch), ch) / sp.sin(ch)**2
                     + sp.diff(sp.sin(th) * sp.diff(Y, th), th) / (sp.sin(ch)**2 * sp.sin(th))
                     + sp.diff(Y, ph, 2) / (sp.sin(ch)**2 * sp.sin(th)**2))
    sc, cc, st, ctt = sp.symbols("s c st ct")
    trig = {sp.sin(ch): sc, sp.cos(ch): cc, sp.sin(th): st, sp.cos(th): ctt}

    def vanishes(e):
        """e = 0 on S^3: numerator reduced modulo sin^2 + cos^2 = 1 in chi and theta"""
        num = sp.numer(sp.together(sp.expand(e).subs(trig)))
        return sp.reduced(sp.expand(num), [sc**2 + cc**2 - 1, st**2 + ctt**2 - 1], sc, st, cc, ctt)[1] == 0
    good = True
    for deg in range(1, 7):
        Y = sp.re(sp.expand((x1 + sp.I * x2)**deg))
        ev = -deg * (deg + 2) if control != 1 else -deg * (deg + 1)
        good &= vanishes(lap(Y) - ev * Y)
    chk("S^3: Re (x_1 + i x_2)^l restricted has Delta = -l(l + 2) Y, l = 1, ..., 6", good)
    rad = sp.simplify(sp.diff(rho**l, rho, 2) + 3 / rho * sp.diff(rho**l, rho) - l * (l + 2) * rho**(l - 2))
    chk("every l: the radial part of Delta_(R^4) on rho^l is l(l + 2) rho^(l - 2), so k^2 = l(l + 2), >= 8 at l >= 2",
        rad == 0 and all(m * (m + 2) >= 8 for m in range(2, 50)))
    # control: S^2, Re (x_1 + i x_2)^l with x1 = cos theta, x2 = sin theta cos phi
    y1, y2 = sp.cos(th), sp.sin(th) * sp.cos(ph)
    lap2 = lambda Y: sp.diff(sp.sin(th) * sp.diff(Y, th), th) / sp.sin(th) + sp.diff(Y, ph, 2) / sp.sin(th)**2
    Y2 = sp.re(sp.expand((y1 + sp.I * y2)**3))
    chk("control S^2: Re (x_1 + i x_2)^3 has Delta = -12 = -l(l + 1)", sp.simplify(lap2(Y2) + 12 * Y2) == 0)
    return chk.ok


CHECKS = [("S1 scalar type: the gauge 1-form's coefficients are c(r) k^-p, p >= 1", s1),
          ("S2 vector type: the gauge 1-form is B = -2 H_T/k_V", s2),
          ("S3 the scalar floor on S^3: k^2 = l(l + 2) >= 8 at l >= 2; control S^2", s3)]


def run(only=None, verbose=False):
    ok = True
    for k, (name, f) in enumerate(CHECKS, 1):
        if only and k != only:
            continue
        t0 = time.time()
        res = f(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    n = 1 if only else len(CHECKS)
    print(f"synth5.py: {n if ok else 'not all'}/{n}")
    return ok


def mutants():
    caught = total = 0
    for name, f in CHECKS:
        total += 1
        res = f(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"synth5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    vb = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=vb) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), vb) else 1)
    print(__doc__)
