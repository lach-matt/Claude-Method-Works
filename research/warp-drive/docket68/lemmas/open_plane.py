#!/usr/bin/env python3
"""open_plane.py -- [WITHDRAWN at 491 as bearing on SOURCE, M: "our plane's matter doesn't travel, just
information ... You worked this question on completely the wrong premise."  The theorem rests only on information
passing through the corridor; a mouth opened by a collision of our plane's matter answers no question it asks.  The
trapped-surface computation stands as computed and bears on no row.]  item 490: SOURCE's opening from our plane (one of the four gaps 489 named).

489 named four gaps on SOURCE's own claim: the device that reads, the structure probe's wavelength (S1C-O1), the opening
shell's emitter, and the corridor's formation from our plane.  The last two rest on emitter E3-E6.  E3-E6 prove that a
round null shell, delivering E(N) all at once, cannot come from our plane: every part of it began in the bulk.  M's 486
reads that as "our plane's matter cannot do it".  This instrument asks whether any opening from the plane exists.  It
finds one: a head-on collision of two pieces of our plane's matter.  Labels: computed (exact unless marked), deduced,
READ, estimate.

  Y1 (READ) Eardley and Giddings, PRD 66, 044011 (2002): two ultrarelativistic particles colliding head-on form a closed
     trapped surface on the union of their shock fronts.  The trapped mass is at least 0.71 sqrt(s) in four dimensions,
     0.66533 sqrt(s) in five, and 0.58105 sqrt(s) at D = 11 (their Table I, for head-on collisions).  They place the
     particles on a brane whose own field is negligible for holes well above the Planck scale, which is our setting.  A trapped surface forms an event horizon outside it and lowers the final mass
     no further (the area theorem).
  Y2 (computed, exact) The head-on trapped surface in D dimensions.  Each shock profile Phi solves lap Phi = -16 pi G E
     delta in the n = D - 2 transverse dimensions.  The surface is the pair of flat n-balls of radius rho_c, with
     |Phi'(rho_c)| = 2, so rho_c^(n-1) = 8 pi G E / Omega_(n-1).  Its area is 2 Omega_(n-1) rho_c^n / n.  Read through
     Tangherlini's area-mass relation, this gives M_AH / sqrt(s) = 1/sqrt(2) = 0.707 in D = 4, (3 pi/4)^(1/3)/2 = 0.665
     in D = 5 and 0.581 in D = 11, Eardley and Giddings' Table I to within 1e-5 (the table truncates).
  Y3 (computed) On our plane.  Both particles are the plane's matter, moving along a line in it.  The configuration is
     symmetric under reflection across the plane, so the orbifold keeps it, and a source on the fixed plane has its
     image coincide with it.  The ratio M_AH / sqrt(s) is therefore the flat five-dimensional 0.665.  The plane's
     tension changes it by O((r_h/ell)^2) = 6.4e-31 at the example (scope C1).  No ray has to leave the plane and return
     (emitter E2): the collision is on the plane.  At the large end, r_h >> ell, the plane's gravity is four-dimensional
     (Randall-Sundrum), and the D = 4 figure 1/sqrt(2) applies, up to the plane's corrections in ell/r_h.
  Y4 (READ; estimate) It settles to the corridor's face.  A head-on collision carries J = 0 and is axisymmetric.  The one
     static, asymptotically flat vacuum end is Tangherlini (Gibbons, Ida and Shiromizu, READ; scope C1), which is
     linearly stable (Ishibashi and Kodama, Prog. Theor. Phys. 110, 901 (2003), READ).  The ringdown estimate, by
     first-order WKB on the l = 2 test-scalar mode of 5D Tangherlini, is omega r_h / c = 1.61 - 0.36 i: the face's
     deformation falls by 1e-10 within 65 face clocks.  The write is 8.63e14 clocks, so the README streams into a round,
     static face (settle_arrival A1's no shear).
  Y5 (computed) The energy: the face of size N needs a collision energy between E5(N) (nothing radiated) and E5(N)/0.665
     = 1.50 E5(N) (the most the area bound lets radiate).  Where in that range is set by the radiated fraction, which
     numerical relativity gives and this instrument does not.
  Y6 (deduced) So our plane's matter can open the face.  E3-E6 stand for the round, all-at-once null shell, and for it
     only.  The trapped surface forms on the shock fronts at the collision, and the face is the static J = 0
     Tangherlini face within 65 clocks.  This conflicts with M's 486 ("an emitter standing in the bulk (our plane's
     matter cannot do it)") for every opening but the round shell.  Whether the theorem requires the round shell (438's
     delivery by a null shell; source_spec U2) is M's (414).  If it does not, SOURCE's third and fourth gaps close on
     this computation, and the reading device and the structure probe remain.

python3 open_plane.py [--selftest | --mutants]
"""
import os, sys, math, cmath
import sympy as sp
import scipy.optimize as so

MUT = set()


def omega(n):
    """area of the unit n-sphere S^n"""
    return 2 * sp.pi ** sp.Rational(n + 1, 2) / sp.gamma(sp.Rational(n + 1, 2))


# ------------------------------------------------------------------ Y2, Y3
def trapped(D):
    G, E = sp.symbols("G E", positive=True)
    n = D - 2                                                        # transverse dimensions
    rho = sp.symbols("rho", positive=True)
    k_ = 2 if "half_flux" not in MUT else 1                          # |Phi'(rho_c)| = 2 (Eardley-Giddings)
    if n == 2:
        Phi = -8 * G * E * sp.log(rho)
    else:
        Phi = 16 * sp.pi * G * E / ((n - 2) * omega(n - 1)) * rho ** (-(n - 2))
    lap_ok = sp.simplify(sp.diff(rho ** (n - 1) * sp.diff(Phi, rho), rho)) == 0      # harmonic off the source
    flux = sp.simplify(-omega(n - 1) * rho ** (n - 1) * sp.diff(Phi, rho))           # = 16 pi G E (Gauss)
    rc = sp.solve(sp.Eq(-sp.diff(Phi, rho), k_), rho)[0]
    area = 2 * omega(n - 1) * rc ** n / n
    # Tangherlini in D: A = Omega_(D-2) r^(D-2), r^(D-3) = 16 pi G M / ((D-2) Omega_(D-2))
    r = (area / omega(D - 2)) ** sp.Rational(1, D - 2)
    M = sp.simplify((D - 2) * omega(D - 2) * r ** (D - 3) / (16 * sp.pi * G))
    frac = sp.nsimplify(sp.simplify(M / (2 * E)))
    return dict(lap_ok=lap_ok, flux=sp.simplify(flux - 16 * sp.pi * G * E) == 0, frac=frac, val=float(frac))


# ------------------------------------------------------------------ Y4
def ringdown(l=2):
    """first-order WKB (Schutz-Will) for the l mode of a massless test scalar on 5D Tangherlini, r_h = 1"""
    r = sp.symbols("r", positive=True)
    f = 1 - 1 / r ** 2
    V = f * (l * (l + 2) / r ** 2 + sp.Rational(3, 4) * f / r ** 2 + sp.Rational(3, 2) * sp.diff(f, r) / r)
    dV = sp.diff(V, r)
    r0 = so.brentq(sp.lambdify(r, dV), 1.05, 4.0, xtol=1e-14)
    # second derivative in the tortoise coordinate at the peak: d/dr* = f d/dr, and V' = 0 there
    d2 = float((f * sp.diff(f * dV, r)).subs(r, r0))
    V0 = float(V.subs(r, r0))
    w = cmath.sqrt(V0 - 1j * 0.5 * math.sqrt(-2 * d2))
    if "undamped" in MUT:
        w = complex(w.real, 0.0)
    t10 = (10 * math.log(10) / abs(w.imag)) if w.imag != 0 else float("inf")
    return dict(r0=float(r0), w=w, t10=t10)


def compute():
    return dict(t4=trapped(4), t5=trapped(5), t11=trapped(11), rd=ringdown())


def checks(o):
    t4, t5, t11, rd = o["t4"], o["t5"], o["t11"], o["rd"]
    return [("Y2: the head-on trapped surface: shock profiles harmonic with flux 16 pi G E; M_AH/sqrt(s) = 1/sqrt(2) "
             "(D = 4), (3 pi/4)^(1/3)/2 = 0.665 (D = 5), 0.581 (D = 11) -- Eardley-Giddings' Table I, 0.66533 and 0.58105",
             all(t["lap_ok"] and t["flux"] for t in (t4, t5, t11))
             and sp.simplify(t4["frac"] - 1 / sp.sqrt(2)) == 0
             and abs(t5["val"] - (3 * math.pi / 4) ** (1 / 3) / 2) < 1e-12 and "%.3f" % t5["val"] == "0.665"
             and abs(t5["val"] - 0.66533) < 1e-5 and abs(t11["val"] - 0.58105) < 1e-5),
            ("Y4: ringdown (WKB, l = 2 test scalar, 5D): omega r_h/c = 1.61 - 0.36i; deformation down by 1e-10 within "
             "65 face clocks", "%.2f" % rd["w"].real == "1.61" and "%.2f" % rd["w"].imag == "-0.36"
             and round(rd["t10"]) == 65),
            ("Y5: collision energy between E5(N) and E5(N)/0.665 = 1.50 E5(N)", "%.2f" % (1 / t5["val"]) == "1.50")]


def report(o=None):
    o = o or compute()
    print("open_plane.py -- the face opened by our plane's matter (item 490)\n")
    for D, t in ((4, o["t4"]), (5, o["t5"]), (11, o["t11"])):
        print("Y2 D = %d: M_AH/sqrt(s) = %s = %.4f" % (D, t["frac"], t["val"]))
    rd = o["rd"]
    print("Y4 WKB peak r = %.3f r_h; omega r_h/c = %.3f %+.3fi; 1e-10 within %.1f clocks" % (rd["r0"], rd["w"].real,
                                                                                          rd["w"].imag, rd["t10"]))
    print("Y5 energy range: E5(N) to %.3f E5(N)" % (1 / o["t5"]["val"]))


MUTANTS = {"half_flux": "the trapped-surface condition |Phi'| = 2 taken as 1 (Y2)",
           "undamped": "the face's deformation taken as never decaying (Y4)"}


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
