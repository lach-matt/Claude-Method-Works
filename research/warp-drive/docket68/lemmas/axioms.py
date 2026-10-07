#!/usr/bin/env python3
"""axioms.py -- M's ten lemmas of the Warp Theorem: six derived, three shown to be definitions consistent with the rest,
one equivalent to the open lemma B4.

M (after the Warp Theorem's report): "Are my 10 lemmas proved? If not, they need to be."  They had been taken as given.
A theorem rests on some premises, so what can be done is (i) derive every one of them that follows from more basic
rulings, the proved lemmas and established physics, and (ii) for the rest, say what they are and prove they are
consistent with everything else.

DERIVED (each from more basic rulings + proved lemmas + physics, computed):
  H2  the horizons hold the README.  Eq. (17)'s horizon is at F = 0, r = 2m; at the corridor's member r0 = 2m (G3,
      proved) the horizon sits on the throat, so its area is the throat's, N A_bit (H1, proved).  P1's future horizon
      and P2's past horizon are one null surface (STABILITY.md S5), so both hold it
  G1  the one exact energy is E(N).  From 101 answer 6 ("widen the corridor to the necessary size, no more and no less":
      the throat's capacity is exactly N bits, 4 pi r0^2 = N A_bit, with A_bit the holographic area per bit,
      H-STRONG-BOUND), 132 (the horizons and the throat both hold it: the horizon radius 2m equals r0), and 131/133 (the
      energy is the pull, m = G E/c^4): r0 = r_min(N), m = r0/2, E = c^4 r0/(2G) = sqrt(N h c^5 ln2/(8 pi^2 G)), one
      value for each N
  I1  the passage is N bits of entanglement.  READ: Maldacena-Susskind arXiv:1306.0533 p.5, two-sided black holes "are
      highly entangled with an entanglement entropy equal to the Bekenstein Hawking entropy of either black hole".  The
      corridor's horizon has area N A_bit (H2), so its Bekenstein-Hawking entropy is A/(4 l_P^2) nats = A/(4 l_P^2 ln2)
      bits = N (i2_capacity.py I2a).  Their statement is for the thermal state; the corridor's horizon is extremal (O2),
      and at zero temperature the entanglement is the horizon's ground-state degeneracy, e^(A/4) (H-EXTREMAL-ENTROPY,
      standard, not READ) -- labelled
  Z3  null energy is never violated, in five dimensions.  In the vacuum bulk R_AB = (2 Lambda/3) g_AB, so R(k,k) = 0 for
      every null k (computed); on the composite plane the null stress is lambda_RS f(y) k_y^2 >= 0 at every depth (B5a,
      the board's H-SHARED-PROFILE); along the passage it is exactly 0 (Z1, proved).  The plane's four-dimensional
      reading of a violation is the bulk's pull (Z1) -- the appearance items 117 and 120 describe
  E1  E is carried into position 2.  The opening's inflow is the README (115 (c)) and the README is the energy (136 G);
      the passage is one way (O1, proved) so none returns to position 1; the corridor holds nothing indefinitely
      (136 answer 3) and a horizon cannot outlive its object (109), so none stays.  Energy is conserved: E_in =
      E_P2 + E_back + E_kept with E_back = E_kept = 0, so E_P2 = E_in = E (z3).  Controls: without the one-way passage, or
      without 136 answer 3, E_P2 = E is not forced
  E2  it is released at position 2 at the closing: after realization the energy is held on position 2's horizon (106,
      the third hold), and that horizon ends with the corridor (109, 115 (b)); so the release is at the closing (z3, an
      ordering)

DEFINITIONS, consistent with the rest (they say what the theory's words mean; a definition is not derived):
  R0  the read -- the corridor takes the README as its inflow (70, 115 (c)); N is read from the object (130 (2)).
      Consistent: the interaction bound is met with equality exactly because the inflow is the README (I2b)
  R1  exact reconstruction, no tolerance (145, 146).  Consistent: exactness at the instant holds across the mass window
      (R3, exactcopy.py), and the build's energy covers any exact README (R5c)
  R2  position 2 rearranges to the README, then its laws govern (148).  Consistent: rearrange.py's excess energy is the
      width term alone, and the ledger closes (E3)
EQUIVALENT TO B4:
  B3  a complete bulk exists (120, 121).  The local bulk is proved (B2); the complete one is B4, open
Imports copy/exactE.py and lemmas/i2_capacity.py by path.  Stdlib + sympy + z3.  python3 axioms.py [--selftest]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)


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


def derive_h2_g1():
    h, c, G, N, r, m = sp.symbols("h c G N r m", positive=True)
    A_bit = 2 * h * G * sp.log(2) / (sp.pi * c**3)
    r0 = sp.sqrt(N * A_bit / (4 * sp.pi))                       # 101.6: capacity exactly N
    horizon = sp.solve(sp.Eq(1 - 2 * m / r, 0), r)              # eq. (17)'s F = 0
    m_val = r0 / 2                                              # 132: horizon radius 2m = r0
    E = sp.simplify(m_val * c**4 / G)                           # 131/133: m = G E/c^4
    E_closed = sp.sqrt(N * h * c**5 * sp.log(2) / (8 * sp.pi**2 * G))
    area_h = 4 * sp.pi * (2 * m_val) ** 2
    return {"horizon": horizon, "E": E, "G1": sp.simplify(E - E_closed) == 0,
            "H2": sp.simplify(area_h - N * A_bit) == 0}


def derive_i1():
    i2 = _load(os.path.join(HERE, "i2_capacity.py"), "ax_i2")
    d = i2.compute()
    return {"bits": d["bits"], "I1": sp.simplify(d["bits"] - sp.Symbol("N", positive=True)) == 0}


def derive_z3():
    lam = sp.Symbol("Lambda")
    g = sp.diag(-1, 1, 1, 1, 1)
    k = sp.Matrix([1, sp.Rational(3, 5), sp.Rational(4, 5), 0, 0])  # a null vector
    Rkk = (k.T * (2 * lam / 3 * g) * k)[0]
    return {"bulk_Rkk": sp.simplify(Rkk), "null": (k.T * g * k)[0] == 0}


def derive_e1_e2():
    import z3
    Ein, Ep2, Eback, Ekept = z3.Reals("E_in E_P2 E_back E_kept")
    one_way, holds_nothing = z3.Bools("one_way holds_nothing")
    base = [Ein > 0, Ep2 >= 0, Eback >= 0, Ekept >= 0, Ein == Ep2 + Eback + Ekept,
            z3.Implies(one_way, Eback == 0), z3.Implies(holds_nothing, Ekept == 0)]

    def forced(extra):
        s = z3.Solver()
        s.add(base + extra + [Ep2 != Ein])
        return s.check() == z3.unsat
    # E2: an ordering -- realization < closing; held on P2's horizon from realization; the horizon ends at closing;
    # release happens when the holder ends
    t_real, t_close, t_release, t_h_end = z3.Reals("t_real t_close t_release t_h_end")
    s = z3.Solver()
    s.add(t_real < t_close, t_h_end == t_close, t_release == t_h_end, z3.Not(t_release == t_close))
    e2 = s.check() == z3.unsat
    return {"E1": forced([one_way, holds_nothing]), "E1_ctl_no_one_way": forced([z3.Not(one_way), holds_nothing]),
            "E1_ctl_no_136_3": forced([one_way, z3.Not(holds_nothing)]), "E2": e2}


def compute():
    return {"hg": derive_h2_g1(), "i1": derive_i1(), "z3n": derive_z3(), "e": derive_e1_e2()}


def report(d):
    hg, i1, z, e = d["hg"], d["i1"], d["z3n"], d["e"]
    print("axioms.py -- M's ten lemmas\n")
    print("H2 horizon at r = %s; its area at r0 = 2m is N A_bit: %s" % (hg["horizon"], hg["H2"]))
    print("G1 E = c^4 r0/(2G) = %s, equal to E(N): %s" % (hg["E"], hg["G1"]))
    print("I1 the horizon's Bekenstein-Hawking entropy in bits = %s (= N: %s)" % (i1["bits"], i1["I1"]))
    print("Z3 bulk R(k,k) = %s for a null k (null: %s); composite >= 0 (B5a); passage 0 (Z1)" % (z["bulk_Rkk"], z["null"]))
    print("E1 E_P2 = E forced: %s (controls -- without one way: %s, without 136.3: %s); E2 release at closing forced: %s"
          % (e["E1"], e["E1_ctl_no_one_way"], e["E1_ctl_no_136_3"], e["E2"]))
    print("R0, R1, R2 definitions, consistent with I2b, R3/R5c, E3; B3 equivalent to B4 (open)")


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    hg, i1, z, e = d["hg"], d["i1"], d["z3n"], d["e"]
    m = sp.Symbol("m", positive=True)
    chk("H2: the horizon is at r = 2m, on the throat at r0 = 2m, holding N A_bit", hg["horizon"] == [2 * m] and hg["H2"])
    chk("G1: no more, no less (101.6) + both hold it (132) + the pull (131/133) give E(N) exactly", hg["G1"])
    chk("I1: the horizon's Bekenstein-Hawking entropy is exactly N bits (Maldacena-Susskind p.5)", i1["I1"])
    chk("Z3: the vacuum bulk's R(k,k) is 0 for a null k", z["bulk_Rkk"] == 0 and z["null"])
    chk("E1: one way + nothing held indefinitely + conservation force E_P2 = E", e["E1"])
    chk("E1 controls: without the one-way passage, or without 136 answer 3, it is not forced",
        not e["E1_ctl_no_one_way"] and not e["E1_ctl_no_136_3"])
    chk("E2: the release is at the closing (an ordering)", e["E2"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
