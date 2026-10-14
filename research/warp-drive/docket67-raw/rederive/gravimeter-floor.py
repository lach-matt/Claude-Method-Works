#!/usr/bin/env python3
"""DOCKET 67 -- audit of 'gravimeter-floor' (address.py:431 GRAVIMETER_FLOOR = 1e-9 m/s^2 ORDER).

What is checkable here WITHOUT reading a measurement paper (every paper route was
refused this run: alphaXiv quota exceeded on all three tools; arxiv.org,
export.arxiv.org, semanticscholar.org 403 at the egress proxy):

  C1  the unit statement '1e-9 m/s^2 = 0.1 microGal' (Gal := 1 cm/s^2, CGS definition) -- exact
  C2  the tree's reach numbers 1.371597e7 m (H1) / 2.560737e7 m (H2) recomputed
      independently from the tree's threshold masses: r = sqrt(G M / a_floor)
  C3  how the conclusion that rests on the floor moves with the floor:
      r scales as a_floor^(-1/2) exactly (sympy); the floor at which the tree's
      '>1e23' / '>20 orders' / r > d would first fail, computed
  C4  geometry the tree's point-mass magnitude GM/r^2 leaves implicit:
      a gravimeter reads ONE component (local vertical); on a sphere of radius
      R_E the vertical component of a surface source seen at chord s is
      GM/(2 R_E s), and the H1 reach exceeds Earth's diameter
  C5  the floor as a measurement is NOT checked (not READ) -- printed as OPEN

The tree is imported read-only (no bytecode written); nothing under research/ is edited.
"""
import math
import sys

import sympy as sp

sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import address as A  # noqa: E402

NPASS = NFAIL = 0


def rep(ok, msg):
    global NPASS, NFAIL
    if ok:
        NPASS += 1
    else:
        NFAIL += 1
    print(("PASS  " if ok else "FAIL  ") + msg)


# ------------------------------------------------------------------ C1 unit identity
print("C1  unit identity")
Gal = sp.Rational(1, 100)                     # m/s^2, CGS definition 1 Gal = 1 cm/s^2
uGal = Gal / 10**6
floor = sp.Rational(1, 10**9)
rep(sp.simplify(floor / uGal - sp.Rational(1, 10)) == 0,
    "1e-9 m/s^2 = %s microGal exactly (tree: '~0.1 microGal')" % (floor / uGal))
rep(A.GRAVIMETER_FLOOR == 1.0e-9, "tree constant GRAVIMETER_FLOOR = %.1e" % A.GRAVIMETER_FLOOR)
print("      relative to g = 9.80665 m/s^2 the floor is %.3e of g" % (1e-9 / 9.80665))

# ------------------------------------------------------------------ C2 reach numbers
print("\nC2  reach numbers recomputed")
G = A.G
S_mid = A.S_SCAN[1][1]
masses = {}
for hyp, want in (("H1", 1.371597e7), ("H2", 2.560737e7)):
    ed = A.eps_det_stationary(hyp)
    rho_tot, _ = A.source_density(ed, A.higgs_fraction(S_mid, hyp))
    M = rho_tot * 4.0 / 3.0 * math.pi
    masses[hyp] = M
    r_indep = math.sqrt(G * M / 1e-9)
    MH = A.higgs.M_HIGGS / A.higgs.M_HIGGS_PIN_WITHDRAWN
    rep(abs(r_indep - A.gravimetric_radius(M)) <= 1e-12 * r_indep,
        "%s: M = %.6e kg, r = sqrt(GM/1e-9) = %.6e m (tree function agrees)" % (hyp, M, r_indep))
    rep(abs(r_indep / (want * MH) - 1) < 1e-5,
        "%s: matches the tree's selftest pin %.6e m (x m_h rescale %.8f) to 1e-5" % (hyp, want, MH))
    print("      prose 'out to %s m' is the pin to two figures" % ("1.4e7" if hyp == "H1" else "2.6e7"))

# ------------------------------------------------------------------ C3 floor sensitivity
print("\nC3  sensitivity of the dependent conclusion to the floor")
a, Gs, Ms = sp.symbols("a G M", positive=True)
r = sp.sqrt(Gs * Ms / a)
elas = sp.simplify(sp.diff(r, a) * a / r)
rep(elas == sp.Rational(-1, 2), "d ln r / d ln a_floor = %s exactly: a floor 100x worse costs 10x in reach" % elas)

for hyp in ("H1", "H2"):
    ed = A.eps_det_stationary(hyp)
    M = masses[hyp]
    d_best = A.detection_standoff(1.0, 1.0, ed)          # the tree's '2v best case' standoff
    print("      %s: Higgs best-case standoff d = %.4e m" % (hyp, d_best))
    for fl in (1e-12, 1e-11, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 9.8):
        rr = math.sqrt(G * M / fl)
        print("        floor %8.1e m/s^2 -> r = %.3e m, r/d = %.3e" % (fl, rr, rr / d_best))
    # floors at which the tree's statements would first fail
    a_1e23 = G * M / (1e23 * d_best) ** 2
    a_1e20 = G * M / (1e20 * d_best) ** 2
    a_eq = G * M / d_best ** 2
    rep(a_1e23 > 1e-9, "%s: '>1e23' (address.py selftest :1474) holds for any floor below %.3e m/s^2 "
        "(%.1fx the tree's 1e-9)" % (hyp, a_1e23, a_1e23 / 1e-9))
    rep(a_1e20 > 1e-5, "%s: '>20 orders' (address.py:217-218) holds for any floor below %.3e m/s^2 = %.0f mGal "
        "(%.1e x the tree's 1e-9); it FAILS only for a floor ~1e-3 g" % (hyp, a_1e20, a_1e20 / 1e-5, a_1e20 / 1e-9))
    fl_ugal = 1e-8
    rd = math.sqrt(G * M / fl_ugal) / d_best
    print("      FINDING %s: at a 1 microGal (1e-8) floor r/d = %.3e -> log10 = %.2f; the '23 orders' wording "
          "(address.py:209) and the '>1e23' pin %s" % (hyp, rd, math.log10(rd),
          "hold" if rd > 1e23 else "would NOT hold (floor-dependent), '>20 orders' still holds"))
    rep(a_eq > 1e30, "%s: r > d (gravity reads farther at all) for any floor below %.3e m/s^2" % (hyp, a_eq))

# the 1 m 'mass gravity reads at 1 m' line (address.py:1129) scales linearly with the floor
Mg = 1e-9 * 1.0 / G
rep(abs(Mg - 14.98) < 0.01, "address.py:1129 'mass gravity reads at 1 m' = floor/G = %.3f kg (linear in floor)" % Mg)

# ------------------------------------------------------------------ C4 geometry
print("\nC4  geometry left implicit by GM/r^2 (point-mass MAGNITUDE)")
R_E = 6.371e6
th = sp.symbols("theta", positive=True)
Rs = sp.symbols("R", positive=True)
s = 2 * Rs * sp.sin(th / 2)
# unit vector from gravimeter (at angle 0) toward a surface source at central angle theta,
# projected on the local vertical (inward radial): equals sin(theta/2) = s/(2R)
gpos = sp.Matrix([Rs, 0]); spos = sp.Matrix([Rs * sp.cos(th), Rs * sp.sin(th)])
u = (spos - gpos) / s
vert = sp.simplify((-gpos / Rs).dot(u))
rep(sp.simplify(vert - sp.sin(th / 2)) == 0,
    "vertical fraction of a surface source's pull = sin(theta/2) = s/(2R): %s" % vert)
for hyp in ("H1", "H2"):
    M = masses[hyp]
    r_mag = math.sqrt(G * M / 1e-9)
    g_antipode = G * M / (2 * R_E) ** 2
    print("      %s: magnitude reach %.3e m vs Earth diameter %.3e m; vertical g at the antipode %.3e m/s^2"
          % (hyp, r_mag, 2 * R_E, g_antipode))
    rep(r_mag > 2 * R_E, "%s: the magnitude reach exceeds Earth's diameter, so '1.4e7/2.6e7 m' is a field-strength "
        "radius, not a terrestrial baseline" % hyp)
    rep(g_antipode > 1e-9, "%s: the vertical component (= magnitude at the antipode) is >= 1e-9 everywhere on "
        "Earth's surface -- the vertical-only reading does not shorten the claim for a surface source" % hyp)
# a gravimeter NOT at the surface (off-axis, in space) reads only the projection; worst case is
# perpendicular incidence (zero).  The tree's reach assumes the sensitive axis points at the source.

# Newtonian point-mass hypothesis: exterior of a uniform sphere is exact in Newton (shell theorem);
# the post-Newtonian size at the reach radius is GM/(r c^2)
for hyp in ("H1", "H2"):
    M = masses[hyp]
    r_mag = math.sqrt(G * M / 1e-9)
    pn = G * M / (r_mag * A.C ** 2)
    rep(pn < 1e-15, "%s: post-Newtonian parameter GM/(r c^2) at the reach = %.2e -- 'Newtonian point mass' costs nothing" % (hyp, pn))

# ------------------------------------------------------------------ C5 the measurement
print("\nC5  the floor itself as a measurement")
print("OPEN  1e-9 m/s^2 as an achieved instrument figure is NOT READ in this run (every paper route refused).")
print("      Which figure it is (single-shot noise / noise after integration / long-term stability /")
print("      absolute accuracy) is not said at address.py:431 ('~0.1 microGal ORDER').")
print("      C3: '>20 orders' survives any floor below 6.3e-3 (H1) / 2.2e-2 (H2) m/s^2; the '>1e23' pin")
print("      survives only below 6.3e-9 (H1) / 2.2e-8 (H2) m/s^2 -- a factor 6.3 from the tree's ORDER value.")

print("\n%d PASS, %d FAIL" % (NPASS, NFAIL))
sys.exit(1 if NFAIL else 0)
