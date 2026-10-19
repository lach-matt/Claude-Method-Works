#!/usr/bin/env python3
"""mag2m.py -- item 493: can a magnetic corridor with mouths of 1 to 2 m be opened between two different spacetimes,
and be held open, without a README?  The hypothesis run with all the board knows, not answered from memory.

M, 493: "Don't guess, run the hypothesis whit all we know so far. - Can a magnetic warp corridor of be opened between
two different spacetimes, and be held/remain open, without a README? - the mouth size should be assumed to be 1 to 2
meters."  What the board already holds and this run uses: magnetic_chain (463: the charge's numbers, formation K4,
closing K5), mmp_corridor (445 (2): Maldacena-Milekhin-Popov and Maldacena-Milekhin, READ in full), BOUNCE-RESEARCH
section 19's deduction 2 (453: "two universes cannot hold a cold throat"), P3 (464: the magnetic hole's interior), and
M's 109, 162, 390.  Labels: computed (exact unless marked), deduced, READ, M's.

  G0 (read) M's words, verbatim in the rulings file: 493; with 109, 162, 390.
  G1 (computed: magnetic_chain's relations) The mouth.  A magnetic hole that stays radiates to extremality and stops
     (magnetic_chain K5; Maldacena, READ), so the mouth that stays is extremal, Q = M = r+ in geometric units.
     - At r+ = 1 m: 1.35e27 kg (225 Earths), 1.06e34 Dirac charges, a horizon field 3.5e18 T.
     - At 2 m: twice the mass and the charge, the field halved.
     - The field is 7.9e8 times Schwinger's (no electric discharge applies to a magnetic charge) and 0.032 times the
       electroweak scale: the symmetry is not restored at the horizon.
     - Its face would hold N = pi r^2/(ln2 l_P^2): 1.7e70 bits at 1 m, 6.9e70 at 2 m.  That is 1.3e4 to 5.1e4 times the
       theorem's own cap N* = 1.37e66 (372, the 8.87 mm Earth-cap corridor).
  G2 (computed; READ) Opened -- no.
     (a) Classically: the mouth needs 1e34 Dirac charges, and the 26 hold no magnetic charge.  So dF = 0 on our plane,
         and with the topology preserved (B4) no closed surface encloses flux (magnetic_chain K4, deduced).  No process
         built of our matter -- or of the README's energy, were there one -- gives a mouth that charge.
     (b) By quantum pair creation, the one route there is (Dowker-Gauntlett-Giddings-Horowitz; Garfinkle-Strominger,
         READ), the rate is e^(-S_E).  In a magnetar's 1e11 T, S_E = 4.2e77 at 1 m and 8.4e77 at 2 m.  S_E reaches
         order one only as qB -> 1, a background field of 3.5e18 T (1 m) over the pair's region -- the hole's own
         horizon field.
     (c) And the instanton makes both mouths in one universe, "the horizons of the two black holes ... identified to
         form a wormhole in space" (READ).  It never joins two different spacetimes.
  G3 (computed, exact in the relation; READ) Held open as a corridor between two spacetimes -- no.
     - A magnetic throat is held open (traversable) only by the negative energy of the charged fermions' field-line
       circles (MMP; in five dimensions MM's AdS3 energy): E(l) = r^3/(G l^2) - c2/(8 L), L the circle's length.
     - The circle closes through the space outside, so L = l + d, d the return path.  For any finite d, E has a
       minimum: one universe, MM's corridor.  At 1 m on our plane it is l = 3.0e5 m, binding 1.3e33 J, held only below
       7.5e-9 K.  The binding falls as the return path grows: 8.4e22 J at a light-year, 8.4e12 J at 1e10 light-years.
     - Between two different spacetimes there is no return path.  Each field line runs from infinity in one to infinity
       in the other (section 19), so L is infinite, the negative energy is zero, and dE/dl = -2 r^3/(G l^3) < 0 for
       every l: no minimum, and the throat runs out to the extremal hole's infinite throat.
     - The theorems agree: topological censorship (Friedman, Schleich and Witt, READ: under the averaged null energy
       condition "every causal curve from I^- to I^+ is deformable" to one outside) and the achronal ANEC (Graham and
       Olum, READ: it suffices "to rule out ... wormholes connecting different asymptotically flat regions").
     - MMP escape them only because their wormhole is longer than the path outside, which two spacetimes do not have.
       FSW's proof is disputed (Krasnikov, READ); the achronal ANEC is a conjecture.  The flux argument above stands
       without either.
  G4 (computed by the record; deduced) Held open as a hole -- yes, but not as a corridor.
     - The extremal magnetic hole stays, held by its charge and not by any README (K5): a T = 0 hole at 1-2 m.
     - Its passage to another spacetime would run through its degenerate horizon, a Cauchy horizon (excluded, 484).
     - The record computed that passage on the plane (464, p3_double_null): the magnetic corridor's interior has no
       regular inner horizon, and ends in a spacelike singularity that reaches the plane.
     - So it holds as a black hole in one spacetime, with no route to another.
  G5 (M's; deduced) Without a README, on M's own rulings.
     - The corridor opens because of the README and closes when nothing is within it (390).
     - It takes the size that holds the README (162).
     - A horizon cannot exist without its object (109).
     - A README-less corridor is therefore no corridor of the theorem.  What the physics leaves without one (G4) is a
       magnetic hole whose object is its own charge.
  G6 (deduced) So, run on everything the board knows, at 1 to 2 m:
     - It cannot be opened: no magnetic charge exists to give the mouth, and pair creation is e^(-4e77) and in one
       universe only.
     - It cannot be held open as a corridor between two different spacetimes: with no shared space the magnetic support
       vanishes and the throat runs to extremality.
     - What could stay without a README is an extremal magnetic black hole, closed to passage.
     - In one spacetime a magnetic wormhole can be held open (MM), but that is not between two spacetimes, and opening it
       still needs the charge the 26 do not hold.

python3 mag2m.py [--selftest | --mutants]
"""
import os, sys, math, re, io, contextlib, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((493, "Can a magnetic warp corridor of be opened between two different spacetimes"),
         (109, "A horizon cannot exist without the object"), (162, "only the size that is needed to hold the object"),
         (390, "it closes when there is nothing contained within the corridor"))
N_STAR = 1.3651e66
M_EARTH = 5.9722e24                                                  # standard, not READ
B_SCHW_T = 4.414e9                                                   # m_e^2 c^2/(e hbar); standard, not READ


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


# ------------------------------------------------------------------ G1, G2
def mouth(r, MC, MP):
    LP, G, C = MP.LP, MP.G, MP.C
    M = r * C ** 2 / G                                               # extremal: r+ = G M / c^2
    e = math.sqrt(4 * math.pi * MC.ALPHA0)
    q = r / LP                                                       # geometric charge, Planck lengths (Q = r+)
    Qd = q * e / math.sqrt(math.pi)                                  # Dirac integer (Maldacena (3), as magnetic_chain)
    rp = r / LP
    F_GeV2 = Qd / (2 * rp ** 2) * MC.MPL_GEV ** 2                     # magnetic_chain's horizon field, GeV^2
    B_T = 1.0 / (r * MC.GEOM_PER_TESLA)                              # the horizon field Q/r+^2 = 1/r+ in tesla
    N = math.pi * r ** 2 / (math.log(2) * LP ** 2)                   # (H): 4 pi r^2 = N x 4 ln2 l_P^2
    qB = r * MC.B_MAGNETAR_T * MC.GEOM_PER_TESLA * (0.0 if "no_field" in MUT else 1.0)
    S = MC.pair_action(q, qB) if qB > 0 else float("inf")
    B_one = 1.0 / (r * MC.GEOM_PER_TESLA)                            # qB = 1
    return dict(M=M, earths=M / M_EARTH, Qd=Qd, B_T=B_T, schw=F_GeV2 / MC.M_E ** 2, ew=F_GeV2 / MC.M_W ** 2, N=N,
                over_cap=N / N_STAR, S=S, B_one=B_one)


# ------------------------------------------------------------------ G3
def throat(MP, r):
    l, d, R, Gs, c2 = sp.symbols("l d r G c_2", positive=True)
    E = R ** 3 / (Gs * l ** 2) - c2 / (8 * (l + d))
    E_inf = sp.limit(E, d, sp.oo)
    dE_inf = sp.diff(E_inf, l)
    no_min = sp.simplify(dE_inf + 2 * R ** 3 / (Gs * l ** 3)) == 0   # dE/dl = -2 r^3/(G l^3) < 0
    # one universe on our plane, MM's point (mmp_corridor), and the binding as the return path grows
    p = MP.point(r, MP.ell())
    G4, c2v = MP.LP ** 2, p["c2"]
    def binding(dv):
        f = lambda lv: r ** 3 / (G4 * lv ** 2) - c2v / (8 * (lv + dv))
        lo, hi = 1e-3, 1e40
        for _ in range(400):                                          # golden-section on log l
            a = lo * (hi / lo) ** 0.382; b = lo * (hi / lo) ** 0.618
            if f(a) < f(b):
                hi = b
            else:
                lo = a
        return -f(math.sqrt(lo * hi)) * MP.HBAR * MP.C                 # J
    bind = {dv: binding(dv) for dv in (0.0, 1e3, MP.LY, 1e10 * MP.LY)}
    return dict(no_min=no_min, E_inf=E_inf, p=p, bind=bind)


def compute():
    MC = _load("magnetic_chain.py", "m2_mc"); MP = _load("mmp_corridor.py", "m2_mp")
    return dict(words=words(), one=mouth(1.0, MC, MP), two=mouth(2.0, MC, MP), th=throat(MP, 1.0))


def checks(o):
    a, b, th = o["one"], o["two"], o["th"]
    bd = th["bind"]
    ds = sorted(bd)
    return [("G0: M's 493, 109, 162 and 390 verbatim in the rulings", o["words"]),
            ("G1: the extremal mouth at 1 m: 1.35e27 kg (225 Earths), 1.06e34 Dirac charges, 3.5e18 T, 7.9e8 Schwinger, "
             "0.032 of the electroweak scale; its face 1.7e70 bits (6.9e70 at 2 m), 1.3e4-5.1e4 times the theorem's cap",
             "%.3g" % a["M"] == "1.35e+27" and round(a["earths"]) == 225 and "%.3g" % a["Qd"] == "1.06e+34"
             and "%.2g" % a["B_T"] == "3.5e+18" and "%.2g" % a["schw"] == "7.9e+08" and "%.2g" % a["ew"] == "0.032"
             and "%.2g" % a["N"] == "1.7e+70" and "%.2g" % b["N"] == "6.9e+70"
             and "%.2g" % a["over_cap"] == "1.3e+04" and "%.2g" % b["over_cap"] == "5.1e+04"),
            ("G2: pair creation in a magnetar's field: S_E = 4.2e77 (1 m), 8.4e77 (2 m); order one only at qB -> 1, "
             "3.5e18 T, the horizon field itself", "%.2g" % a["S"] == "4.2e+77" and "%.2g" % b["S"] == "8.4e+77"
             and "%.2g" % a["B_one"] == "3.5e+18" and abs(a["B_one"] / a["B_T"] - 1) < 1e-12),
            ("G3: with the return path infinite (two spacetimes) dE/dl = -2 r^3/(G l^3) < 0: no minimum; one universe "
             "at 1 m: l 3.0e5 m, binding 1.3e33 J, below 7.5e-9 K; the binding falls with the return path",
             th["no_min"] and "%.2g" % th["p"]["l"] == "3e+05" and "%.2g" % th["p"]["Eb_J"] == "1.3e+33"
             and "%.2g" % th["p"]["Tmax"] == "7.5e-09" and all(bd[ds[i]] > bd[ds[i + 1]] for i in range(len(ds) - 1))
             and abs(bd[0.0] / th["p"]["Eb_J"] - 1) < 1e-3)]


def report(o=None):
    o = o or compute(); a, b, th = o["one"], o["two"], o["th"]
    print("mag2m.py -- a magnetic corridor of 1-2 m between two spacetimes, without a README (item 493)\n")
    for r, x in ((1, a), (2, b)):
        print("G1 r+ = %d m: M %.3g kg (%.0f Earths), %.3g Dirac charges, B %.2g T (%.2g Schwinger, %.2g EW); face %.2g bits, "
              "%.2g x the cap; G2 S_E(1e11 T) %.2g, qB = 1 at %.2g T" % (r, x["M"], x["earths"], x["Qd"], x["B_T"], x["schw"],
                                                                        x["ew"], x["N"], x["over_cap"], x["S"], x["B_one"]))
    print("G3 E(l) with L -> infinity: %s; dE/dl < 0 everywhere: %s; one universe at 1 m: l %.2g m, binding %.2g J, T_max %.2g K"
          % (th["E_inf"], th["no_min"], th["p"]["l"], th["p"]["Eb_J"], th["p"]["Tmax"]))
    print("   binding against the return path d: %s" % ", ".join("d %.3g m: %.3g J" % kv for kv in sorted(th["bind"].items())))


MUTANTS = {"no_field": "the pair created with no background field (G2)"}


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
        failed = [n_.split(":")[0] for n_, ok in checks(compute()) if not ok]
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
