#!/usr/bin/env python3
"""em_open.py -- item 495: item 494's question asked of an electromagnetic field, the electric part included.  Can an
electromagnetic field open and hold, by itself and with no README, a corridor that information or matter can pass?
Run on the board and prior art, not answered from memory.

M, 495: "EM?" -- read as 494 ("Can we possibly conceive a condition where a magnetic or non electric field can open and
hold a corridor ... opened by the field itself?") with the electric field admitted.  Uses field_open (494), mag2m (493),
mmp_corridor (MMP and MM).  Labels: computed (exact unless marked), deduced, READ, M's.

  E0 (read) M's words, verbatim in the rulings file: 495, with 494.
  E1 (computed, exact) Gravity cannot tell electric from magnetic.
     - The Maxwell stress tensor is unchanged by the duality rotation (E, B) -> (E cos a + B sin a, -E sin a + B cos a):
       energy density, Poynting vector and stresses alike.
     - So the hole, the throat and the classical hold see only E^2 + B^2.  For a radial field of any mix,
       rho + p_r = 0: the marginal throat of 494's F1, no more.
     - The pair-creation action is the same with the electric charge in place of the magnetic one.
     - Classically an electromagnetic field does exactly what 494's magnetic field does, and nothing more.
  E2 (computed, exact) What does differ is frame-invariant.
     - B^2 - E^2 and E.B are the same in every frame.  A field is a magnetic field seen from some frame iff E.B = 0
       and |E| < |B| (c = 1): the boost v = E x B/B^2 removes E exactly, and |v| < 1 iff |E| < |B|.
     - A magnetic force does no work, v.(v x B) = 0, so in that frame the field cannot supply a pair's rest energy.
       Such a field is stable against pair creation (deduced).
  E3 (computed; READ) The electric part discharges in our matter, because the light charges are electric.
     - Schwinger's field is E_S = m_e^2 c^3/(e hbar) = 1.32e18 V/m.
     - The field a 1 m mouth needs, as electric, is c B_h = 1.04e27 V/m: 7.9e8 E_S (mag2m's ratio).
     - There Schwinger's rate (eE)^2/(4 pi^3 hbar^2 c) e^(-pi E_S/E) is 6.8e73 pairs per m^3 per s.  It neutralizes
       the mouth's 7.2e35 charges in 2.6e-39 s, against the light-crossing time of 3.3e-9 s (order of magnitude:
       constant field, no back-reaction).
     - An extremal electric mouth's horizon field falls to E_S only at r = 7.9e8 m, 5.3e5 solar masses.  Any smaller
       mouth discharges.  Gibbons (READ): for large holes the loss of charge "is shown to be governed by a Schwinger
       type formula".
     - The opening fails the same way.  Where the field would make a pair of electric mouths at the universe's rate
       (S_E = 563, 494's F2), the electron's exponent pi E_S/E is 4.0e-9 at 1 m and 2.2e-42 at one Dirac charge.  The
       field makes electrons first, by e^563 and more.
     - A magnetic mouth does not discharge: the 26 hold no light magnetic charge (magnetic_chain K5).
  E4 (READ; computed) The hold needs magnetic flux through the mouth.
     - MMP: "This Landau level has degeneracy q, where q is an integer specifying the quantized magnetic flux through
       the sphere": the zero modes that carry the negative energy number q N_f.
     - A purely electric mouth has no flux through its sphere for electric charges.  So it has no zero modes and
       c2 = 0, and then E(l) = r^3/(G l^2) falls for every l: no minimum, no hold (exact).
     - An electric field along the magnetic field lines (E.B != 0, the dyonic mouth) is screened by the very fermions
       that hold the throat.  MMP App. G (READ): "the leading order electric field is screened by the charged
       fermions".  The anomaly d(n_R - n_L)/dt = (e^2/2 pi^2) E.B (READ, 0908.4466) pumps the massless lowest Landau
       level with no exponential suppression, and the field's energy becomes excitations in the throat, which MMP
       6.1.3 says end in a horizon.
     - So E.B must be 0 to within an energy small against the throat's destroying energy.  At 1 m that is
       E_par < 3.5e19 V/m, 3.4e-8 of c B_h (deduced, order of magnitude: the field's energy over the throat's volume
       4 pi r^2 l).
  E5 (deduced) So an electromagnetic field adds no condition and opens no new route.
     - Crossed fields (E.B = 0, |E| < c|B|) are 494's magnetic corridor seen from a moving frame.
     - Any other electric part discharges the mouths (E3) or fills the throat (E4).
     - The electric version would work by duality if the light charged fermions were magnetic monopoles.  The 26 hold
       none, and none is seen.
     - 494 stands: the corridor is magnetic in its own frame, E.B = 0 and |E| < c|B|.  It is not the theorem's.
Imports mmp_corridor.py and mag2m.py by path.  Stdlib + sympy.
python3 em_open.py [--selftest | --mutants]
"""
import os, sys, math, re, io, contextlib, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((495, '"EM?"'),
         (494, "Can we possibly conceive a condition where a magnetic or non electric field can open and hold"))
E_CH, M_E_KG, EPS0, M_SUN = 1.602176634e-19, 9.1093837015e-31, 8.8541878128e-12, 1.98847e30   # CODATA / IAU; standard
S_STAR = 563                                                         # 494 F2: once in the observable universe's history


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    ok = True
    for n, w in WORDS:
        m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
        ok = ok and bool(m) and w in " ".join(m.group(0).split())
    return ok


# ------------------------------------------------------------------ E1, E2
def e1():
    a = sp.symbols("a", real=True)
    E = sp.Matrix(sp.symbols("E1:4", real=True)); B = sp.Matrix(sp.symbols("B1:4", real=True))
    def T(E, B):
        s = -1 if "duality_broken" in MUT else 1                     # the mutant: the electric stress sign flipped
        u = (E.dot(E) + B.dot(B)) / 2
        S = E.cross(B)
        sig = sp.Matrix(3, 3, lambda i, j: -s * E[i] * E[j] - B[i] * B[j] + (1 if i == j else 0) * u)
        return u, S, sig
    E2, B2 = E * sp.cos(a) + B * sp.sin(a), -E * sp.sin(a) + B * sp.cos(a)
    (u0, S0, s0), (u1, S1, s1) = T(E, B), T(E2, B2)
    dual = (sp.simplify(u1 - u0) == 0 and sp.simplify(S1 - S0) == sp.zeros(3, 1)
            and sp.simplify(s1 - s0) == sp.zeros(3, 3))
    # radial E and B of any mix: rho = (E^2+B^2)/2, p_r = sigma_rr = -(E^2+B^2)/2 (Gaussian x 1/4pi dropped)
    Er, Br = sp.symbols("E_r B_r", real=True)
    u, _, sig = T(sp.Matrix([Er, 0, 0]), sp.Matrix([Br, 0, 0]))
    marginal = sp.simplify(u + sig[0, 0]) == 0
    return dict(dual=dual, marginal=marginal)


def e2():
    b = sp.symbols("beta", real=True)
    g = 1 / sp.sqrt(1 - b ** 2)
    Ex, Ey, Ez, Bx, By, Bz = sp.symbols("E_x E_y E_z B_x B_y B_z", real=True)
    # a boost along x (c = 1)
    Ep = sp.Matrix([Ex, g * (Ey - b * Bz), g * (Ez + b * By)])
    Bp = sp.Matrix([Bx, g * (By + b * Ez), g * (Bz - b * Ey)])
    E, B = sp.Matrix([Ex, Ey, Ez]), sp.Matrix([Bx, By, Bz])
    inv1 = sp.simplify((Bp.dot(Bp) - Ep.dot(Ep)) - (B.dot(B) - E.dot(E))) == 0
    inv2 = sp.simplify(Ep.dot(Bp) - E.dot(B)) == 0
    # crossed fields E = (0, e, 0), B = (0, 0, bb), e < bb: the boost v = E x B / B^2 = (e/bb) x removes E
    e, bb = sp.symbols("e bb", positive=True)
    Ec = Ep.subs({Ex: 0, Ey: e, Ez: 0, Bx: 0, By: 0, Bz: bb}).subs(b, e / bb)
    removes = sp.simplify(Ec) == sp.zeros(3, 1)
    v = sp.Matrix(sp.symbols("v1:4", real=True))
    no_work = sp.simplify(v.dot(v.cross(B))) == 0
    return dict(inv1=inv1, inv2=inv2, removes=removes, no_work=no_work)


# ------------------------------------------------------------------ E3
def e3():
    MP = _load("mmp_corridor.py", "em_mp"); M2 = _load("mag2m.py", "em_m2"); MC = _load("magnetic_chain.py", "em_mc")
    HB, C, G = MP.HBAR, MP.C, MP.G
    ES = M_E_KG ** 2 * C ** 3 / (E_CH * HB)
    out = {}
    for r in (1.0, 2.0):
        Q = r * C ** 2 * math.sqrt(4 * math.pi * EPS0 / G)                # extremal electric hole of radius r
        Eh = Q / (4 * math.pi * EPS0 * r ** 2)
        rate = (E_CH * Eh) ** 2 / (4 * math.pi ** 3 * HB ** 2 * C) * math.exp(-math.pi * ES / Eh)
        V = 4 / 3 * math.pi * r ** 3
        out[r] = dict(Q=Q, n=Q / E_CH, Eh=Eh, ratio=Eh / ES, rate=rate, tau=(Q / E_CH) / (rate * V), cross=r / C,
                      mag2m=M2.mouth(r, MC, MP)["B_T"] * C / ES)
    r_min = C ** 2 / (ES * math.sqrt(4 * math.pi * EPS0 * G))
    # the opening field of 494 (S_E = 563), as electric, against the electron's exponent pi E_S / E
    FO = _load("field_open.py", "em_fo")
    rows = FO.f2()["rows"]
    expo = {k: math.pi * ES / (rows[k]["B_T"] * C) for k in ("1 m", "one Dirac charge")}
    light_monopole = "monopoles_light" in MUT                            # the mutant: a light magnetic charge in the 26
    mag_tau = 1e-30 if light_monopole else float("inf")
    return dict(ES=ES, at=out, r_min=r_min, M_min=r_min * C ** 2 / G / M_SUN, expo=expo, mag_tau=mag_tau)


# ------------------------------------------------------------------ E4
def e4():
    l, R, Gs = sp.symbols("l r G", positive=True)
    q_mag = 0                                                            # a purely electric mouth: no magnetic flux
    zero_modes = sp.Symbol("q_e") if "zero_modes_electric" in MUT else q_mag   # the mutant: electric flux counted
    c2 = zero_modes
    E = R ** 3 / (Gs * l ** 2) - c2 / (8 * l)
    no_hold = sp.simplify(sp.diff(E, l) + 2 * R ** 3 / (Gs * l ** 3)) == 0
    # the stray E along B tolerated at 1 m: its energy over the throat's volume against the destroying energy
    MP = _load("mmp_corridor.py", "em_mp4")
    p = MP.point(1.0, MP.ell())
    Ed = 16 * p["Eb_J"]
    V = 4 * math.pi * 1.0 ** 2 * p["l"]
    Emax = math.sqrt(2 * Ed / (EPS0 * V))
    Eh = 1.0 * MP.C ** 2 * math.sqrt(4 * math.pi * EPS0 / MP.G) / (4 * math.pi * EPS0)
    return dict(no_hold=no_hold, Emax=Emax, frac=Emax / Eh)


def compute():
    return dict(words=words(), e1=e1(), e2=e2(), e3=e3(), e4=e4())


def checks(o):
    a, b, c, d = o["e1"], o["e2"], o["e3"], o["e4"]
    one = c["at"][1.0]
    return [("E0: M's 495 and 494 verbatim in the rulings", o["words"]),
            ("E1: the Maxwell stress tensor unchanged by the duality rotation; a radial field of any electric-magnetic "
             "mix gives rho + p_r = 0", a["dual"] and a["marginal"]),
            ("E2: B^2 - E^2 and E.B invariant; crossed fields with |E| < |B| made purely magnetic by v = E x B/B^2; a "
             "magnetic force does no work", b["inv1"] and b["inv2"] and b["removes"] and b["no_work"]),
            ("E3: E_S = 1.32e18 V/m; a 1 m mouth's field 1.04e27 V/m = 7.9e8 E_S (mag2m's ratio), 6.8e73 pairs/m^3/s, "
             "7.2e35 charges gone in 2.6e-39 s against 3.3e-9 s; electric mouths hold only from 7.9e8 m (5.3e5 solar "
             "masses); at 494's opening field pi E_S/E = 4.0e-9 (1 m), 2.2e-42 (one Dirac charge); magnetic mouths "
             "never discharge",
             "%.3g" % c["ES"] == "1.32e+18" and "%.3g" % one["Eh"] == "1.04e+27" and "%.2g" % one["ratio"] == "7.9e+08"
             and abs(one["ratio"] / one["mag2m"] - 1) < 1e-3 and "%.2g" % one["rate"] == "6.8e+73"
             and "%.2g" % one["n"] == "7.2e+35" and "%.2g" % one["tau"] == "2.6e-39"
             and "%.2g" % one["cross"] == "3.3e-09"
             and "%.2g" % c["r_min"] == "7.9e+08" and "%.2g" % c["M_min"] == "5.3e+05"
             and "%.2g" % c["expo"]["1 m"] == "4e-09" and "%.2g" % c["expo"]["one Dirac charge"] == "2.2e-42"
             and c["mag_tau"] == float("inf")),
            ("E4: a purely electric mouth has no zero modes, c2 = 0, and dE/dl = -2 r^3/(G l^3): no hold; the stray "
             "E along B tolerated at 1 m is 3.5e19 V/m, 3.4e-8 of the mouth's field",
             d["no_hold"] and "%.2g" % d["Emax"] == "3.5e+19" and "%.2g" % d["frac"] == "3.4e-08")]


def report(o=None):
    o = o or compute()
    c, d = o["e3"], o["e4"]
    print("E3 E_S %.4g V/m; r_min %.4g m (%.3g solar masses); exponents %s; magnetic tau %s"
          % (c["ES"], c["r_min"], c["M_min"], {k: "%.3g" % v for k, v in c["expo"].items()}, c["mag_tau"]))
    for r, v in c["at"].items():
        print("   r %.0f m: Q %.3g C (%.3g e), E_h %.4g V/m = %.3g E_S (mag2m %.3g), rate %.3g /m^3/s, tau %.3g s, "
              "r/c %.3g s"
              % (r, v["Q"], v["n"], v["Eh"], v["ratio"], v["mag2m"], v["rate"], v["tau"], v["cross"]))
    print("E4 stray E along B at 1 m below %.3g V/m (%.3g of E_h)" % (d["Emax"], d["frac"]))
    for n_, ok in checks(o):
        print("  [%s] %s" % ("ok" if ok else "FAIL", n_))


MUTANTS = {"duality_broken": "the electric stress with its sign flipped, breaking duality (E1)",
           "monopoles_light": "a light magnetic charge admitted to the 26 (E3)",
           "zero_modes_electric": "zero modes counted from electric flux (E4)"}


def selftest(quiet=False):
    r_ = checks(compute())
    if not quiet:
        for n_, ok in r_:
            print("  [%s] %s" % ("ok" if ok else "FAIL", n_))
    k = sum(ok for _, ok in r_)
    if not quiet:
        print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            failed = [n_.split(":")[0] for n_, ok in checks(compute()) if not ok]
        except Exception as ex:                                          # a mutant that breaks the run is caught
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  [%s] %s -> %s" % ("caught" if failed else "MISSED", desc, ", ".join(failed) or "nothing"))
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
