#!/usr/bin/env python3
"""stability.py -- wall E (stability), worked as mathematics (M-RULINGS item 149: "work the math now").

[Auditing agent, item 281 (the reverse passage, 270/276): S5/S5b follow side-2 rays along the white-hole surface --
inflow from position 2 (W3), which the one-way object excludes (i_oneway I3); S1 is unaffected.  Kept as written.]

[Item 331 (M-UPDATE-STALE-NOW): S1-S5b are statements about Bronnikov-Kim eq. (17) at r0 = 2m, and they stand as
that.  They are not statements about the corridor: item 251 dropped clause (O)'s "extremal", the corridor's horizon
being the localized five-dimensional hole's at the small end (rows_small O2s: kappa = c^2/r_h) and four-dimensional
Schwarzschild at the large end (item 261, C3 F5: kappa = 1/(4M)); item 271's verifier found O2 false at both ends.
The corridor's own horizon is S6.  Every "the corridor" below in S1-S5b reads "eq. (17) at r0 = 2m".  Kept as written.]

First written quoting Aretakis's extremal-Kerr Theorem 3 (tau^(k-1)) as if general and using an asymptotic bound for
early times; corrected (STABILITY.md History).  The finite-time result now comes from an exact horizon identity.

The corridor: Bronnikov-Kim eq. (17) at r0 = 2m (plane.py), -F dt^2 + dr^2/H + r^2 dOmega^2, F = 1 - 2m/r,
H = (1 - 2m/r)^2 / (1 - 3m/2r).  In Aretakis's form g = -D dv^2 + 2 dv drho + r(rho)^2 dOmega^2, drho = sqrt(F/H) dr.

READ: Aretakis, arXiv:1206.6598v2: abstract ("do not decay along such horizons as advanced time tends to infinity, and
in fact, higher order derivatives blow up"); eqs. (6)-(8) p.10 (extremality D = D' = 0); Prop. 3.2 p.10 (the hierarchy
"provided" D''(r_H) = 2K(r_H), eq. 10; "extremal Reissner-Nordstrom satisfies the condition (10)", p.11); Theorem 1
p.11 (non-decay, under A1-A4 only); Theorem 2 p.12 (blow-up, conditional: "unless psi and the tangential to H+
derivatives of psi do not decay and H[psi] = 0").  Theorem 3 p.15 ("asympotically", sic) is for extremal Kerr.

  S1  the corridor's horizon is extremal: D'(rho_H) = 0.  Control: the r0 = 1.8m member, D' = sqrt(10)/(10m)
  S2  it meets condition (10) exactly: D'' = 1/(2m^2) = 2K.  Control (READ): extremal RN meets it
  S3  the corridor's clock m/c = r_min(N)/(2c): 6.6e-37 s at the example README
  S4  the exact horizon identities for a spherical wave (derived here from the wave operator, generic D(rho), r(rho)):
        d/dv (d psi/d rho) = 0                       -> H0 = d psi/d rho is conserved exactly (beta_0 = 0: the throat
                                                       sits on the horizon, r' = 0)
        d/dv (d^2 psi/d rho^2) = -(D''/2) H0 - (r''/r) d psi/dv,  with D''/2 = 1/(4m^2), r''/r = 1/(2m^2) here
      so over an advanced time v the second derivative changes by -H0 v/(4m^2) - (psi(v) - psi(0))/(2m^2): linear growth
      with an exact coefficient, no unknown constant.  Over one clock (v = m) the linear part is H0/(4m), a quarter of
      the second derivative's natural size H0/m
  S5  the white-hole half of the wall.  READ: Bianchi, Christodoulou, D'Ambrosio, Haggard & Rovelli, arXiv:1802.04264v2
      p.7 (a secondary citation; the primary sources are Eardley 1974 and Barrabes-Brady-Poisson 1993, both about
      non-extremal white holes): "Generically, white holes are known to be unstable under perturbations ... The
      instability arises because modes of short-wavelength are exponentially blue-shifted along the white hole
      horizon."  The exponential rate is the surface gravity kappa = D'(rho_H)/2.  The corridor's is zero (S1), so the
      exponential blueshift is absent.  Control: the r0 = 1.8m member, kappa = sqrt(10)/(20m), e-folds every
      2 sqrt(10) m ~ 6.3 m.  At r0 = 2m the entry's future horizon and the exit's past horizon are ONE null surface
      (P1's two horizons merge), so S4's identities hold on the exit too
  S5b what remains at kappa = 0 is a power law, and it is unbounded.  Rays hugging the white-hole surface (side 2,
      rho~ < 0) obey d rho~/dv = D/2 = rho~^2/(8m^2): rho~(v) = rho~0/(1 - rho~0 v/(8m^2)) -> -8m^2/v, approaching the
      surface without reaching it; their spacing shrinks as (1 - rho~0 v/(8m^2))^-2 ~ v^-2, a blueshift growing as v^2.
      Control: the non-extremal near-horizon law d rho~/dv = kappa rho~ gives spacing e^(kappa v).  So the exponential
      mechanism is absent and a v^2 blueshift remains; whether it destabilises the exit is OPEN
  S6  (item 331) the corridor's own horizon, at both ends: not extremal.  The wave operator on -D dv^2 + 2 dv drho +
      R(rho)^2 dOmega_n^2 (the black-hole face, ingoing) and on -D du^2 - 2 du drho + R^2 dOmega_n^2 (the white-hole
      face, outgoing), at D = 0, D' = 2 kappa, R' free (computed, exact, generic D, R and n):
        black-hole face   d/dv (d psi/d rho) = -kappa (d psi/d rho) - (n R'/(2R)) d psi/dv
        white-hole face   d/du (d psi/d rho) = +kappa (d psi/d rho) - (n R'/(2R)) d psi/du
      and the k-th transverse derivative carries -k kappa (black-hole face) at the top order (computed, k = 2).  At
      kappa = 0 and R' = 0 the first reduces to S4's conserved H0 (computed): Aretakis's hierarchy is the kappa = 0 case
      and nothing else.  On the corridor: the small end is Tangherlini, D = 1 - r_h^2/r^2, rho = r, n = 3, kappa = 1/r_h
      (rows_small O2s, c^2/r_h), n R'/(2R) = 3/(2 r_h); the large end is Schwarzschild, D = 1 - 2M/r, n = 2, kappa =
      1/(4M), n R'/(2R) = 1/(2M) (computed).
      Our face (the black-hole side, where the hold is): every transverse derivative is damped, one e-fold per clock of
      r_h/c at the small end -- e^(-66,980) of its initial size over C6's write floor (write_small S3) -- and with the
      tangential source bounded it is bounded by e^(-kappa v)|H(0)| + (n R'/(2 R kappa)) sup|d psi/dv|, 3/2 at the small
      end and 2 at the large (computed, the ODE solved exactly).  No Aretakis growth: S4's linear growth and S5b's v^2
      law do not occur on the corridor (deduced from the identity).  That the tangential derivative stays bounded is
      READ, for the scalar wave S1-S6 all treat: Schlue, arXiv:1012.5963v1, Theorem 1 (eq. (1.9): E[phi](Sigma_tau) <=
      C D/tau^2 on the exterior of the higher-dimensional Schwarzschild solution, "where n >= 3 is the spatial
      dimension" -- n = 4 is the small end's Tangherlini, 1 - 2m/r^(n-2), n = 3 the large end's Schwarzschild) and
      Proposition 5.2 (section 5.1, "Uniform Boundedness": the nondegenerate energy bounded by its initial value, "a
      consequence of the conservation of the degenerate energy associated to the multiplier T, and the redshift effect
      of Section 3"); pointwise |phi| <= C D'/tau^(3/2 - delta) (abstract).  Schlue's redshift effect is the mechanism
      the identity above computes.  A pointwise bound on d psi/dv itself follows by commuting with T, which commutes
      with the wave operator (standard, not READ).  Gravitational perturbations are not Schlue's: for them the record
      holds Ishibashi-Kodama's mode stability (rows_small O2s), which is not a bound.
      Position 2's face (the white-hole side): the transverse derivative grows as e^(kappa u) -- Eardley's blueshift,
      present (computed: the sign).  It is bounded by the face's open period: position 2's face stays open at most
      ln(1 + (pi/10)(ell/r_h)) = 33.6 clocks (c_junction J1), so at most e^33.6 = 1 + (pi/10)(ell/r_h) = 3.9e14
      (c_junction J5; c7_oneway V12 (Q1), verified), not e^66,980 (item 271 (3), which took the face open through the
      write).  What arrives at the face from position 2 over that period is position 2's to mitigate (240); a
      blackbody bath of it is 27 to 65 orders below Barcelo's 0.28 E (c7_oneway V12 (Q1)).  The face's stability
      against position 2's other ambient fields is not claimed (240).
Imports copy/chain.py's exact throat coefficient and lemmas/c_junction.py, lemmas/write_small.py by path.  Stdlib +
sympy.  python3 stability.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
C = 299792458.0
EXAMPLE_N = 2742570311524972

r, m, s, M = sp.symbols("r m s M", positive=True)
MUT = {}


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def D_derivatives(r0v, rH):
    """D = F as a function of rho, d rho/dr = sqrt(F/H).  Returns D'(rho) and D''(rho) at r -> rH (limits)."""
    F = 1 - 2 * m / r
    H = (1 - 2 * m / r) * (1 - r0v / r) / (1 - sp.Rational(3, 2) * m / r)
    drho_dr = sp.sqrt(F / H)
    D1 = sp.diff(F, r) / drho_dr                                    # dD/drho
    D2 = sp.diff(D1, r) / drho_dr                                   # d2D/drho2
    lim = lambda e: sp.limit(sp.simplify(e.subs(r, rH + s)), s, 0, "+")
    return lim(D1), lim(D2)


def transport():
    """Derive, for generic D(rho), r(rho), the horizon identities of a spherical wave psi(v, rho)."""
    v, rho = sp.symbols("v rho")
    Df, Rf = sp.Function("D")(rho), sp.Function("R")(rho)
    psi = sp.Function("psi")(v, rho)
    box = (sp.diff(Rf**2 * sp.diff(psi, rho), v) + sp.diff(Rf**2 * (sp.diff(psi, v) + Df * sp.diff(psi, rho)), rho)) / Rf**2
    d0, d1, d2, r0_, r1, r2 = sp.symbols("d0 d1 d2 R0 R1 R2")
    sub = {sp.Derivative(Df, (rho, 2)): d2, sp.Derivative(Df, rho): d1, Df: d0,
           sp.Derivative(Rf, (rho, 2)): r2, sp.Derivative(Rf, rho): r1, Rf: r0_}
    hz = {d0: 0, d1: 0, r1: 0}
    first = sp.solve(sp.Eq(sp.expand(box.subs(sub).subs(hz)), 0), sp.Derivative(psi, v, rho))
    second = sp.solve(sp.Eq(sp.expand(sp.diff(box, rho).subs(sub).subs(hz)), 0), sp.Derivative(psi, v, (rho, 2)))
    return {"first": first, "second": second, "syms": (d2, r0_, r2), "psi": psi, "v": v, "rho": rho}


def r_second(rH):
    """r''(rho) at the horizon: r_rho = sqrt(H/F), so r_rhorho = (1/2) d(H/F)/dr there."""
    F = 1 - 2 * m / r
    H = (1 - 2 * m / r) ** 2 / (1 - sp.Rational(3, 2) * m / r)
    return sp.limit(sp.Rational(1, 2) * sp.diff(sp.simplify(H / F), r).subs(r, rH + s), s, 0, "+")


def white_hole():
    """S5b: the side-2 rays hugging the white-hole surface, at kappa = 0 and (control) at kappa > 0."""
    v, kap = sp.symbols("v kappa", positive=True)
    a = sp.Symbol("a", positive=True)
    x0 = -a                                                         # rho~0 < 0: side 2
    xv = x0 / (1 - x0 * v / (8 * m**2))
    ode_ok = sp.simplify(sp.diff(xv, v) - xv**2 / (8 * m**2)) == 0 and sp.simplify(xv.subs(v, 0) - x0) == 0
    spacing = sp.simplify(-sp.diff(xv, a))                          # d rho~ / d rho~0, rho~0 = -a
    blue = sp.limit(1 / (spacing * v**2), v, sp.oo)                 # blueshift / v^2 -> constant
    xc = x0 * sp.exp(kap * v)                                       # control: d rho~/dv = kappa rho~
    ctl_ok = sp.simplify(sp.diff(xc, v) - kap * xc) == 0
    return {"ode_ok": ode_ok, "limit": sp.limit(xv * v, v, sp.oo), "spacing": spacing, "blue_over_v2": blue,
            "spacing_control": sp.simplify(-sp.diff(xc, a)), "control_ok": ctl_ok}


def transport_general(side="bh"):
    """S6 (item 331): the horizon identities at D = 0, D' = 2 kappa, R' free, on the black-hole face (ingoing v) and
    the white-hole face (outgoing u: g^(u rho) = -1), for a spherical wave on an n-sphere"""
    v, rho, n, kap = sp.symbols("v rho n kappa", positive=True)
    Df, Rf = sp.Function("D")(rho), sp.Function("R")(rho)
    psi = sp.Function("psi")(v, rho)
    sgn = 1 if (side == "bh" or MUT.get("wh_damped")) else -1     # the mutant: the white-hole face read as ingoing
    box = (sgn * sp.diff(Rf**n * sp.diff(psi, rho), v)
           + sp.diff(Rf**n * (sgn * sp.diff(psi, v) + Df * sp.diff(psi, rho)), rho)) / Rf**n
    d0, d1, d2, r0_, r1, r2 = sp.symbols("d0 d1 d2 R0 R1 R2")
    sub = [(sp.Derivative(Df, (rho, 2)), d2), (sp.Derivative(Df, rho), d1), (Df, d0),
           (sp.Derivative(Rf, (rho, 2)), r2), (sp.Derivative(Rf, rho), r1), (Rf, r0_)]
    hz = {d0: 0, d1: 0 if MUT.get("extremal_reading") else 2 * kap}  # the mutant: the corridor read as extremal (S1)
    first = sp.solve(sp.Eq(sp.expand(box.subs(sub).subs(hz)), 0), sp.Derivative(psi, v, rho))[0]
    second = sp.solve(sp.Eq(sp.expand(sp.diff(box, rho).subs(sub).subs(hz)), 0), sp.Derivative(psi, v, (rho, 2)))[0]
    H, P, H2 = sp.Derivative(psi, rho), sp.Derivative(psi, v), sp.Derivative(psi, (rho, 2))
    return dict(damp=sp.simplify(sp.expand(first).coeff(H)), source=sp.simplify(sp.expand(first).coeff(P)),
                top2=sp.simplify(sp.expand(second).coeff(H2)), first=first, syms=(kap, n, r0_, r1), H=H, P=P)


def nonextremal():
    """S6 (item 331): the corridor's own horizon at both ends; our face damped, position 2's bounded by its open
    period"""
    bh, wh = transport_general("bh"), transport_general("wh")
    kap, n, r0_, r1 = bh["syms"]
    rh = sp.Symbol("r_h", positive=True)
    reduces = sp.simplify(bh["first"].subs({kap: 0, r1: 0})) == 0      # kappa = 0, R' = 0: S4's conserved H0
    ends = {}
    for name, Dr, nv, rH in (("small", 1 - rh**2 / r**2, 3, rh), ("large", 1 - 2 * M / r, 2, 2 * M)):
        kv = sp.simplify(sp.diff(Dr, r).subs(r, rH) / 2)            # rho = r, R = r: D' = dD/dr, R' = 1
        src = sp.simplify(-bh["source"].subs({n: nv, r1: 1, r0_: rH}))
        ends[name] = dict(kappa=kv, source=src, sup_ratio=sp.simplify(src / kv))
    v, k, c_, s_, H0 = sp.symbols("v kappa c s H0", positive=True)
    sol = sp.exp(-k * v) * H0 - c_ * s_ / k * (1 - sp.exp(-k * v))      # H' = -kappa H - c s, s the source's bound
    ode_ok = sp.simplify(sp.diff(sol, v) + k * sol + c_ * s_) == 0 and sp.simplify(sol.subs(v, 0) - H0) == 0
    CJ = _load(os.path.join(D68, "lemmas", "c_junction.py"), "st_cj")
    ex = CJ.example(CJ.seen())
    open_clocks = ex["floor"] if MUT.get("open_through_write") else ex["t_full"]   # the mutant: open through the write
    return dict(bh=bh, wh=wh, reduces=reduces, ends=ends, ode_ok=ode_ok, sup=sp.limit(sol, v, sp.oo),
                open_clocks=open_clocks, log10_blue=open_clocks / math.log(10), floor=ex["floor"],
                blue_exact=1 + math.pi / 10 * ex["ell_over_rh"], log10_damp_floor=-ex["floor"] / math.log(10))


def compute():
    d1, d2 = D_derivatives(2 * m, 2 * m)                            # the corridor
    K = 1 / (2 * m) ** 2
    c1, _ = D_derivatives(sp.Rational(9, 5) * m, 2 * m)            # control: r0 = 1.8 m, horizon at 2m
    Drn = (1 - M / r) ** 2                                          # extremal RN (READ)
    rn_ok = sp.simplify(sp.diff(Drn, r, 2).subs(r, M) - 2 / M**2) == 0
    ch = _load(os.path.join(D68, "copy", "chain.py"), "st_chain")
    r1 = float(sp.N(sp.sympify(ch.coefficients()["r_min_m_per_sqrt_bit"]["exact"]), 20))
    rN = EXAMPLE_N ** 0.5 * r1
    t_m = rN / (2 * C)
    tr = transport()
    d2s, r0s, r2s = tr["syms"]
    rpp = r_second(2 * m)
    second = tr["second"][0]
    coeff_H0 = sp.simplify(second.coeff(sp.Derivative(tr["psi"], tr["rho"])).subs({d2s: d2}))
    coeff_dv = sp.simplify(second.coeff(sp.Derivative(tr["psi"], tr["v"])).subs({r2s: rpp, r0s: 2 * m}))
    return {"D1": d1, "D2": d2, "K": K, "cond10": sp.simplify(d2 - 2 * K) == 0, "control_D1": c1, "rn_ok": rn_ok,
            "rN": rN, "t_m": t_m, "t_m_per_sqrt_bit": r1 / (2 * C), "first": tr["first"], "rpp": rpp,
            "coeff_H0": coeff_H0, "coeff_dv": coeff_dv,
            "kappa": sp.simplify(d1 / 2), "kappa_control": sp.simplify(c1 / 2), "wh": white_hole(),
            "s6": nonextremal()}


def report(d):
    print("stability.py -- wall E: eq. (17)'s horizon (item 149), S1-S5b; the corridor's own, S6 (item 331)\n")
    print("S1 eq. (17) at r0 = 2m: D'(rho_H) = %s (extremal; not the corridor, S6); control r0 = 1.8m: D'(rho_H) = %s"
          % (d["D1"], d["control_D1"]))
    print("S2 D''(rho_H) = %s, 2K = %s: Aretakis's condition (10) holds: %s; extremal RN meets it: %s"
          % (d["D2"], 2 * d["K"], d["cond10"], d["rn_ok"]))
    print("S3 eq. (17)'s clock m/c = %.3e s at the example README (r_min = %.3e m); %.3e s x sqrt(N)"
          % (d["t_m"], d["rN"], d["t_m_per_sqrt_bit"]))
    print("S4 on the horizon: d/dv(d psi/d rho) = %s (conserved); r''(rho_H) = %s; d/dv(d2 psi/d rho2) = (%s) H0 + (%s) dpsi/dv"
          % (d["first"][0] if d["first"] else 0, d["rpp"], d["coeff_H0"], d["coeff_dv"]))
    print("   over one clock (v = m) the linear part of the change is H0/(4m): a quarter of the natural size H0/m")
    print("S5 white-hole blueshift rate kappa: eq. (17) %s (exponential blueshift absent); control r0 = 1.8m: %s, "
          "e-folding %s" % (d["kappa"], d["kappa_control"], sp.simplify(1 / d["kappa_control"])))
    w = d["wh"]
    print("S5b side-2 rays at kappa = 0: rho~ v -> %s; spacing %s (blueshift ~ v^2 x %s); control kappa > 0: spacing %s"
          % (w["limit"], w["spacing"], w["blue_over_v2"], w["spacing_control"]))
    x = d["s6"]
    print("\nS6 (item 331) the corridor's own horizon, kappa != 0 -- black-hole face: d/dv H = (%s) H + (%s) dpsi/dv; "
          "top order of the second: %s;\n   white-hole face: d/du H = (%s) H + (%s) dpsi/du; "
          "kappa = 0, R' = 0 gives S4: %s"
          % (x["bh"]["damp"], x["bh"]["source"], x["bh"]["top2"], x["wh"]["damp"], x["wh"]["source"], x["reduces"]))
    for name, e in x["ends"].items():
        print("   %s end: kappa = %s, source n R'/(2R) = %s, bound on H's forced part = %s sup|dpsi/dv|"
              % (name, e["kappa"], e["source"], e["sup_ratio"]))
    print("   our face over C6's write floor (%.0f clocks): damped by 10^(%.0f); position 2's face open %.2f clocks: "
          "blueshift at most 10^%.2f = %.3g (1 + (pi/10) ell/r_h = %.3g)"
          % (x["floor"], x["log10_damp_floor"], x["open_clocks"], x["log10_blue"], 10 ** x["log10_blue"],
             x["blue_exact"]))


def checks(d):
    out = []

    def chk(name, cond):
        out.append((name, bool(cond)))

    chk("S1: eq. (17) at r0 = 2m has an extremal horizon, D'(rho_H) = 0 (not the corridor's: S6, item 331)",
        d["D1"] == 0)
    chk("S1 control: the r0 = 1.8m horizon member is not extremal, D'(rho_H) != 0", d["control_D1"] != 0)
    chk("S2: D''(rho_H) = 1/(2 m^2) = 2K -- Aretakis's condition (10) holds exactly", d["cond10"]
        and sp.simplify(d["D2"] - 1 / (2 * m**2)) == 0)
    chk("S2 control (READ): extremal Reissner-Nordstrom meets condition (10)", d["rn_ok"])
    chk("S3: eq. (17)'s clock m/c at the example README is ~6.6e-37 s", 6.0e-37 < d["t_m"] < 7.2e-37)
    chk("S4: on the horizon the first derivative is conserved exactly (d/dv of it is zero)", d["first"] == [0])
    chk("S4: the second derivative changes at -H0/(4 m^2) - (1/(2 m^2)) dpsi/dv, exactly (r'' = 1/m)",
        sp.simplify(d["coeff_H0"] + 1 / (4 * m**2)) == 0 and sp.simplify(d["coeff_dv"] + 1 / (2 * m**2)) == 0)
    chk("S5: eq. (17)'s surface gravity is zero, so its white hole's exponential blueshift is absent; control: "
        "the r0 = 1.8m member e-folds every 2 sqrt(10) m", d["kappa"] == 0
        and sp.simplify(1 / d["kappa_control"] - 2 * sp.sqrt(10) * m) == 0)
    w = d["wh"]
    a, kap, v = sp.Symbol("a", positive=True), sp.Symbol("kappa", positive=True), sp.Symbol("v", positive=True)
    chk("S5b: side-2 rays approach the white-hole surface as -8m^2/v and their spacing shrinks as v^-2 (blueshift ~ v^2, "
        "unbounded); control: at kappa > 0 the spacing grows as e^(kappa v)",
        w["ode_ok"] and sp.simplify(w["limit"] + 8 * m**2) == 0 and w["blue_over_v2"].is_positive
        and w["blue_over_v2"] != sp.oo and w["control_ok"] and sp.simplify(w["spacing_control"] - sp.exp(kap * v)) == 0)
    x = d["s6"]
    kap, n_, r0_, r1 = x["bh"]["syms"]
    rh = sp.Symbol("r_h", positive=True)
    chk("S6 (item 331): at D' = 2 kappa the black-hole face damps H at -kappa, the white-hole face grows it at +kappa, "
        "both with source -(n R'/2R) times the tangential derivative; the second derivative's top order -2 kappa; "
        "kappa = 0 and R' = 0 give S4's conserved H0",
        sp.simplify(x["bh"]["damp"] + kap) == 0 and sp.simplify(x["wh"]["damp"] - kap) == 0
        and sp.simplify(x["bh"]["source"] + n_ * r1 / (2 * r0_)) == 0
        and sp.simplify(x["wh"]["source"] + n_ * r1 / (2 * r0_)) == 0
        and sp.simplify(x["bh"]["top2"] + 2 * kap) == 0 and x["reduces"])
    e = x["ends"]
    chk("S6: the small end (Tangherlini, n = 3) has kappa = 1/r_h, source 3/(2 r_h), forced part <= 3/2 sup|dpsi/dv|; "
        "the large end (Schwarzschild, n = 2) kappa = 1/(4M), source 1/(2M), <= 2 sup|dpsi/dv|; the ODE solved exactly",
        sp.simplify(e["small"]["kappa"] - 1 / rh) == 0 and sp.simplify(e["small"]["source"] - 3 / (2 * rh)) == 0
        and e["small"]["sup_ratio"] == sp.Rational(3, 2) and sp.simplify(e["large"]["kappa"] - 1 / (4 * M)) == 0
        and sp.simplify(e["large"]["source"] - 1 / (2 * M)) == 0 and e["large"]["sup_ratio"] == 2 and x["ode_ok"])
    chk("S6: position 2's face open at most 33.6 clocks (c_junction J1), its blueshift at most e^33.6 = "
        "1 + (pi/10) ell/r_h = 3.9e14 (J5; c7_oneway V12 (Q1)); our face damped by e^-66,980 over C6's write floor",
        "%.1f" % x["open_clocks"] == "33.6" and "%.2g" % 10 ** x["log10_blue"] == "3.9e+14"
        and abs(10 ** x["log10_blue"] / x["blue_exact"] - 1) < 1e-9 and round(x["floor"]) == 66980
        and x["log10_damp_floor"] < -29000)
    return out


MUTANTS = {"extremal_reading": "the corridor's horizon read as extremal, D' = 0, as eq. (17)'s S1 (S6)",
           "wh_damped": "the white-hole face read as damping, as the black-hole face (S6)",
           "open_through_write": "position 2's face held open through C6's write floor (item 271 (3); S6)"}


def selftest():
    r_ = checks(compute())
    for name, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", name))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = sorted({nm.split(":")[0].split()[0] for nm, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-20s %-76s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)




if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
