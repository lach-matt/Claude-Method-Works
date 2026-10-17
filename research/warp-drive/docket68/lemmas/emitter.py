#!/usr/bin/env python3
"""emitter.py -- item 486 (2): the emitter of SOURCE's round inflow stands in the bulk, and our plane's matter cannot
be it -- proved.  M, 486: "an emitter standing in the bulk (our plane's matter cannot do it): - prove this please".
Labels: computed (exact unless marked), deduced, READ, M's.  Worked in the conversation; not verified; not seated.

Held against the exclusions first (481, 484): the hole here is the uncharged one (Tangherlini at the small end, the
warped string at the large); no inner or Cauchy horizon enters, and no bounce.

  E0 (read) M's words, verbatim in the rulings file: 486.
  E1 (the record) Our matter is our plane's fields and lives on the plane: B6' (our universe a plane of tension in the
     five-dimensional bulk), 180 (the corridor exclusive to the bulk), settle_arrival A4 (the plane carries its tension
     and nothing else).  The bulk carries gravity (and the bulk U(1), 446), not our matter.
  E2 (computed, exact) Every null ray of the bulk is a straight line.  The record's warped bulk e^(-2y/ell) eta + dy^2
     is (ell/z)^2 (eta + dz^2) with z = ell e^(y/ell) (checked), conformally flat; for g = W^2 eta and k null,
     Gamma^a_bc k^b k^c = 2 (k . d ln W) k^a (checked), so null geodesics are flat-space null lines reparametrized.
     Our plane is z = ell and the bulk z > ell; along a line z is affine in the parameter, so a ray that leaves our
     plane never meets it again, and every ray reaching our plane from the bulk side was in the bulk before.
  E3 (computed) The round shell at the small end.  Its rays are radial onto the hole, centred on our plane.  At a face
     point an angle alpha above the plane the ray traced back has y = (r_h + s) sin alpha, increasing: it began in the
     bulk.  Only alpha = 0 is reachable from the plane, a set of zero area on the face's 3-sphere (the band |alpha| <
     delta holds a fraction 4 delta/pi of it, computed, -> 0).
  E4 (computed) Not even through the hole's own lensing.  A ray of 5D Tangherlini stays in a plane through the centre;
     its angle to capture phi_cap(b) rises strictly from 0 (radial) to infinity at b_c = 2 r_h (computed).  A face point
     at polar angle alpha is seen from an emitter in our plane at gamma, cos gamma = cos alpha cos beta, so the pole
     (alpha = pi/2) is at gamma = pi/2 from every emitter: it takes only rays with phi_cap = pi/2 + n pi, impact
     parameters b_1 = 1.35 r_h and above, never the radial ray the round shell is.  The equator takes b from 0 up.  So
     what our plane can send carries different angular momentum at the pole and at the equator: not round (the face
     would shear, which settle_arrival A1 refuses) and not at once (the b_1 ray arrives 1.14 face clocks after the
     radial one, from the same distance).
  E5 (computed, exact) The large end.  The warped Vaidya shell's generators run at fixed depth (d/dr along v = const,
     dy = 0, is null), weighted e^(2y/ell): each began at its own depth, and the plane's depth y = 0 holds none of the
     shell's measure.  By E2 no ray from our plane reaches depth y > 0 and comes back.
  E6 (READ; deduced) Allowed by established physics.  The round inflow -- the shell that opens the face and the README's
     inflow that writes it (passage_est Q4) -- is in the high-frequency limit a solution of the bulk's own vacuum
     equations ("all solutions to the Einstein-null dust system also arise locally as high-frequency limits of vacuum
     spacetimes", Huneau and Luk, READ), so the theory admits it as data on a slice in the bulk; traced back along its
     rays (E2-E5) every part of it began in the bulk.  So the emitter stands in the bulk, and no matter of our plane can
     be it: proved.  Who or what stands there is no row of the theorem; the theorem names that it must.

python3 emitter.py [--selftest | --mutants]
"""
import os, sys, math, re, importlib.util
import numpy as np
import sympy as sp
import scipy.integrate as si
import scipy.optimize as so

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((486, "an emitter standing in the bulk (our plane's matter cannot do it): - prove this please"),
         (180, "exclusive to the bulk"))


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


# ------------------------------------------------------------------ E2
def conformal():
    y, ell, z = sp.symbols("y ell z", positive=True)
    # e^(-2y/ell) eta + dy^2 with z = ell e^(y/ell): dy = ell dz/z, e^(-2y/ell) = (ell/z)^2
    zz = ell * sp.exp(y / ell)
    dz_dy = sp.diff(zz, y)
    warp_ok = sp.simplify(sp.exp(-2 * y / ell) - (ell / zz) ** 2) == 0
    dy2_ok = sp.simplify(1 - (ell / zz) ** 2 * dz_dy ** 2) == 0               # dy^2 = (ell/z)^2 dz^2
    # Christoffels of g = W(x)^2 eta in 5D, contracted with a null k
    X = sp.symbols("x0:5"); kv = sp.symbols("k0:5")
    W = sp.Function("W")(*X)
    eta = sp.diag(-1, 1, 1, 1, 1)
    g = W ** 2 * eta; gi = eta / W ** 2
    G = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(5)) / 2
           for c in range(5)] for b in range(5)] for a in range(5)]
    kk = sp.Matrix(kv)
    knorm = sum(eta[i, i] * kv[i] ** 2 for i in range(5))
    kdlnW = sum(kv[i] * sp.diff(sp.log(W), X[i]) for i in range(5))
    resid = [sp.simplify(sum(G[a][b][c] * kv[b] * kv[c] for b in range(5) for c in range(5)) - 2 * kdlnW * kv[a]
                         + knorm * sum(eta[a, d] * sp.diff(sp.log(W), X[d]) for d in range(5))) for a in range(5)]
    prop_ok = all(r == 0 for r in resid)                                     # = 2 (k.dlnW) k^a - (k.k) dlnW^a
    # a line from the plane: z(lambda) = ell + lambda k_z, affine; with k_z > 0 it never returns to z = ell
    lam, kz = sp.symbols("lambda k_z", positive=True)
    zl = ell + lam * kz
    returns = sp.solve(sp.Eq(zl, ell), lam)
    return dict(warp=warp_ok and dy2_ok, prop=prop_ok, never=(returns == [] or all(r == 0 for r in returns)))


# ------------------------------------------------------------------ E3
def round_shell():
    s, rh, al = sp.symbols("s r_h alpha", positive=True)
    y = (rh + s) * sp.sin(al)
    increasing = sp.simplify(sp.diff(y, s) - sp.sin(al)) == 0
    # fraction of the half 3-sphere within |alpha| < delta of the plane: the area element of S^3 in (alpha, S^2) is
    # cos^2(alpha) d alpha dOmega_2 measured from the plane's directions: int_0^delta cos^2 / int_0^(pi/2) cos^2
    d = sp.symbols("delta", positive=True)
    t = sp.symbols("t")
    frac = sp.integrate(sp.cos(t) ** 2, (t, 0, d)) / sp.integrate(sp.cos(t) ** 2, (t, 0, sp.pi / 2))
    if "planeband" in MUT:
        frac = sp.Integer(1)
    return dict(increasing=increasing, frac_at=[float(frac.subs(d, x)) for x in (1e-1, 1e-3, 1e-6)],
                frac_zero=sp.limit(frac, d, 0) == 0)


# ------------------------------------------------------------------ E4
def phi_cap(b, rh=1.0):
    """angle swept from infinity to the horizon by a null ray of f = 1 - rh^2/r^2 with impact parameter b < 2 rh:
    phi = int_{rh}^inf b dr / (r^2 sqrt(1 - b^2 f/r^2)), in u = 1/r: int_0^{1/rh} b du / sqrt(1 - b^2 u^2 (1 - rh^2 u^2))"""
    if b == 0:
        return 0.0
    f = lambda u: b / math.sqrt(1 - b * b * u * u * (1 - rh * rh * u * u))
    return si.quad(f, 0, 1 / rh, limit=400, epsabs=1e-13, epsrel=1e-12)[0]


def t_fall(b, R=1e3, rh=1.0):
    """coordinate time from r = R to the face's neighbourhood r = 1.001 rh along the ray: dt/dr = 1/(f sqrt(1 - b^2 f/r^2))"""
    f = lambda r: 1 - rh * rh / (r * r)
    g = lambda r: 1 / (f(r) * math.sqrt(1 - b * b * f(r) / (r * r)))
    return si.quad(g, 1.001 * rh, R, limit=800, epsabs=1e-10, epsrel=1e-11)[0]


def lensing():
    bs = np.linspace(0.0, 1.999, 200)
    ph = [phi_cap(b) for b in bs]
    mono = all(ph[i + 1] > ph[i] for i in range(len(ph) - 1))
    near = phi_cap(1.99999)
    target = math.pi / 2 if "pole_any" not in MUT else 0.0
    b1 = so.brentq(lambda b: phi_cap(b) - math.pi / 2, 1e-6, 1.999999) if target else 0.0
    dt = t_fall(b1) - t_fall(0.0)
    # gamma between an in-plane emitter direction and a face point: cos gamma = cos alpha cos beta
    al, be = sp.symbols("alpha beta", real=True)
    pole_gamma = sp.simplify(sp.acos(sp.cos(sp.pi / 2) * sp.cos(be))) == sp.pi / 2
    return dict(mono=mono, phi0=ph[0], near=near, b1=b1, dt=dt, pole_gamma=pole_gamma)


# ------------------------------------------------------------------ E5
def large_end():
    v, r, y, ell = sp.symbols("v r y ell", positive=True)
    m = sp.Function("m")(v)
    w = sp.exp(-2 * y / ell)
    g = sp.zeros(6, 6)            # coordinates (v, r, theta, phi, y) padded to 6 for clarity; use 5
    gm = sp.Matrix([[-w * (1 - 2 * m / r), w, 0, 0, 0], [w, 0, 0, 0, 0], [0, 0, w * r ** 2, 0, 0],
                    [0, 0, 0, w * r ** 2, 0], [0, 0, 0, 0, 1]])
    kr = sp.Matrix([0, 1, 0, 0, 0])                                          # d/dr along v = const, dy = 0
    null = sp.simplify((kr.T * gm * kr)[0]) == 0
    # the plane's share of the shell's measure: weight e^(2y/ell) on [0, Y]; the slice y in [0, eps] -> 0
    eps, Y = sp.symbols("epsilon Y", positive=True)
    share = sp.integrate(sp.exp(2 * y / ell), (y, 0, eps)) / sp.integrate(sp.exp(2 * y / ell), (y, 0, Y))
    return dict(null=null, plane_share_zero=sp.limit(share, eps, 0) == 0)


def compute():
    return dict(words=words(), conf=conformal(), rs=round_shell(), lens=lensing(), le=large_end())


def checks(o):
    c, rs, L, le = o["conf"], o["rs"], o["lens"], o["le"]
    return dict(E0=o["words"], E2=c["warp"] and c["prop"] and c["never"],
                E3=rs["increasing"] and rs["frac_zero"] and rs["frac_at"][2] < 1e-5,
                E4=(L["mono"] and L["phi0"] == 0.0 and L["near"] > 5 and 1.3 < L["b1"] < 1.4 and L["pole_gamma"]
                    and L["dt"] > 0.1),
                E5=le["null"] and le["plane_share_zero"])


def report(o=None):
    o = o or compute(); ck = checks(o)
    c, rs, L, le = o["conf"], o["rs"], o["lens"], o["le"]
    print("E0 M's words: %s" % o["words"])
    print("E2 the warped bulk is (ell/z)^2 (eta + dz^2): %s; null geodesics straight lines (Gamma k k = 2 (k.dlnW) k): %s; "
          "a ray leaving the plane never returns: %s" % (c["warp"], c["prop"], c["never"]))
    print("E3 traced back, a round-shell ray rises off the plane: %s; the plane's band of the face holds %s of it at "
          "delta = 0.1, 1e-3, 1e-6; -> 0: %s" % (rs["increasing"], ", ".join("%.2g" % x for x in rs["frac_at"]),
                                               rs["frac_zero"]))
    print("E4 phi_cap(b) strictly rising from %.1f: %s (%.2f near b_c); the pole at pi/2 from every emitter: %s; its "
          "first ray b_1 = %.4f r_h, arriving %.3f face clocks after the radial one" % (
              L["phi0"], L["mono"], L["near"], L["pole_gamma"], L["b1"], L["dt"]))
    print("E5 the warped shell's generators null at fixed depth: %s; the plane's share of its measure -> 0: %s" % (
        le["null"], le["plane_share_zero"]))
    for kk, vv in ck.items():
        print("%s %s" % (kk, vv))
    return all(ck.values())


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0; names = ["planeband", "pole_any"]
    for m_ in names:
        MUT.clear(); MUT.add(m_)
        try:
            r_ = selftest(quiet=True)
        except Exception:
            r_ = False
        caught += not r_; print("mutant %-10s %s" % (m_, "caught" if not r_ else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
