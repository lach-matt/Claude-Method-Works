#!/usr/bin/env python3
"""pointwise.py -- item 320: "The matter condition was misattributed. - prove the pointwise condition."  B5a's matter
condition (b5a_residue A2) -- each universe's matter on its sheet with rho >= 0 above its vacuum and rho + p >= 0 at
every point -- was named the row's own; M orders it proved.  It is proved here from what matter is built of.  Worked
in the conversation (computed with sympy, exact where marked; READ where marked; deduced where marked; not verified by
a separate session; not seated); 2026-10-12.

  P0 (read) The words the proof rests on, verbatim in the rulings file: M's item-320 order; M's 202, "any plane has its
     own structure in the same fashions that we do, the same definitions as we do, perhaps different values though";
     M's 284 (1) option, "The N bits reconstitute under position 2's own laws"; M's 120, "the NEC only ever appears to
     break, but never does"; and M's 201, "our universe is defined by" the plane's tension and its dark-energy offset.
  P1 (computed, exact) Particles.  Matter as particles -- a distribution f >= 0 over future causal momenta, in any
     number of species, of any masses, as kinetic theory writes it -- has T^ab = sum_i w_i p_i^a p_i^b, w_i >= 0, so
     T(t, t) = sum_i w_i (p_i . t)^2 >= 0 for every vector t and in particular every timelike t (the weak condition)
     and every null k (the null condition) (computed: the contraction is the sum of squares, exactly).  A distribution
     is the limit of such sums.
  P2 (computed, exact) Scalar fields.  A field with its kinetic term of the positive sign and any potential V,
     T_ab = d_a phi d_b phi - g_ab ((1/2)(d phi)^2 + V), has T(k, k) = (k . d phi)^2 >= 0 for every null k and every V
     (computed), and in the rest frame of any observer u, T(u, u) = (1/2)(u . d phi)^2 + (1/2)|d_perp phi|^2 + V
     (computed), which is >= 0 above the potential's least value -- the vacuum, whose energy is the plane's offset
     (201: the universe defined by its tension and its offset), not matter.  Several fields add; their couplings sit
     in V and in the masses, which enter no sign.
  P3 (computed, exact) Gauge fields.  T_ab = F_ac F_b^c - (1/4) g_ab F_cd F^cd gives T(u, u) = (1/2)(E^2 + B^2) in
     the frame of u, and on every null k = (1, n), |n| = 1, T(k, k) = |E_perp + n x B|^2 (computed, exact): both
     sums of squares.  A Yang-Mills field is the sum over its colour components of this form (deduced).
  P4 (deduced) What matter is built of.  The record's matter is atoms, molecules and solids of electrons and nuclei
     (p2_matter; no_madelung's electron configurations), bound electromagnetically -- particles (P1) and a gauge field
     (P3), the nuclei's own binding a Yang-Mills field and particles again, the masses a scalar field gives (P2) inside
     P1's masses and P2's V; degenerate and thermal gases are P1 with their own f >= 0.  An interaction's energy is the
     field's (the Coulomb energy is P3's E^2/2), so the total stress is the sum of P1-P3, and the weak and null
     conditions, being linear in T and holding for each term, hold for the sum at every point.  For a perfect fluid of
     such matter rho = T(u, u) >= 0 and rho + p = T(k, k)/(k . u)^2 >= 0 for k = u + e, e a unit spatial vector
     (computed).
  P5 (deduced) Ours.  Our sheet's matter is the record's: P4 holds for it at every point.  Our vacuum's energy is the
     offset, 5.25e-10 J/m^3 (201), plane structure entering B5a with the tension (b5a_residue A2).
  P6 (deduced; computed where marked; corrected at item 321) Position 2's.  202 gives every plane "the same
     definitions as we do, perhaps different values", and the README reconstitutes "under position 2's own laws" (284
     (1)).  P1-P3 use no value: masses, charges, couplings, the number of species and the potential's shape are left
     general and enter no sign (computed: every symbol general).  What would break them is a kinetic term of the other
     sign (the mutants ghost_scalar and ghost_gauge).  [M, item 321: "don't we already have such a defined term?"  The
     board had written that such a term is "a ghost, a different definition, not a different value".  The record
     holds one whose sign is a value -- position 2's plane's displacement, whose inertia is the plane's tension (P10)
     -- and that sentence is withdrawn.]  So it turns on which kinetic coefficients are values.  A fundamental field's
     is not: rescaling the field folds its size into the potential and the couplings, which P1-P3 leave general, and
     leaves its sign (computed) -- a gauge field's size is 1/e^2, positive for every real charge -- so its size is no
     value of its own, the measured values being the couplings it is folded into, and no value carries its sign: the
     sign is the definition, which 202 gives position 2 as ours.  A derived one is: the inertia of what moves is its
     energy.  For matter -- nuclei, atoms, molecules -- that is a bound system's rest energy (von Laue's theorem,
     standard, not READ), its constituents' energy, >= 0 by P1-P3, so its momentum is future causal as P1 takes it.
     For a plane it is the tension, a value, negative for 139 (1)'s; that ghost is plane structure, not matter, and the
     record holds it at zero (P10).  So P4 holds for every position 2, the README's rebuilt matter included.
  P7 (READ; deduced) Quantum states.  A quantum state can show negative local energy; M's 120: "the NEC only ever
     appears to break, but never does" -- such a show is an appearance, and what is is P4's.  The negative 183's pairs
     concern lies in the quantum region inside the hole (pair_math P2, P4), not on the sheets.
  P8 (deduced) The condition, proved.  At every point of each sheet the matter's stress satisfies the weak and null
     conditions; so its share on a bulk null ray crossing the sheet, S_matter(k_par, k_par)/|k_y| with k_par timelike
     (or null on a grazing ray), is >= 0: rho >= 0 and rho + p >= 0 at every point, B5a's condition, for every universe.
     b5a_residue A2's bound rho > -sigma/6 is then never approached: rho >= 0.
     [Item 339 (the B5a verifier's (Q4), seated at its source): P2's "above the potential's least value" is rho >= 0
     relative to the plane's offset only inside the offset vacuum's basin -- our vacuum is metastable, with a deeper
     region at or below -2.0e108 J/m^3 beyond the barrier (p2_offset, item 322), a change of vacuum and not matter; "any
     potential" needs V bounded below; and P8's "at every point ... for every universe" is the classical statement,
     quantum states being read under M's 120 (P7). The null condition, rho + p >= 0, holds for every V.]
  P9 (the cypher NOT-RUN, stated) The condition is an identity of each kind of matter, not a choice among
     configurations: an index of (kind, condition) rows would carry the answer as its own column, a key (211), as
     tau_share T6 found for tau.  Not run, and said.
  P10 (READ via multiplane.py and STATIC.md; computed; DERIVED in b5_positive B5c; item 321) The ghost the record
     defines, and its hold.  Position 2's plane displaced from ours by r carries the radion; in the Lykken-Randall
     background the board uses (H-LR-PAIR) its kinetic coefficient at r = 0 is C_r = (24 M^3)^2/tau2
     (Pilo-Rattazzi-Zaffaroni eq. 2.16, READ via multiplane.py; g_coincide G2): with 139 (1)'s quarter, tau2 = -tau1/4
     and C_r = -96 (M = k_L = 1), the ghost POSITIVITY.md Q1 records at the coinciding planes (verified once).  PRZ p.2
     say why (READ in STATIC.md): "the kinetic coefficient of the radion is proportional to the brane tension, which is
     negative".  The flat form computes it: a sheet of tension tau displaced by f has the Nambu-Goto Lagrangian -tau
     sqrt(1 + (d f)^2) (the action standard, not READ), to second order -tau - (tau/2)(d f)^2 -- P2's form with the
     sign tau -- so its displacement's T(k, k) = tau (k . d f)^2: a sheet's inertia is its tension, its sign a value's.
     Two sheets of 4/3 and -1/3 of the one-plane value have the velocity terms (tau1 + tau2)/2 = +1/2 moved together
     and tau1 tau2/(2 (tau1 + tau2)) = -2/9 for their separation (computed; the flat form, an illustration: in the
     Lykken-Randall bulk ours sits at the mirror plane and only position 2's sheet moves).  It is not matter: it is the
     planes' separation, in no sheet's T_ab of P1-P3 and not in B5a's surface stress, which carries the tension and
     not its motion (b5a_residue A2).  And the record holds it -- not by a restoring force, which would not cure a
     ghost (STATIC.md S3, PRZ p.9 READ there), but by identity of position: the planes coincide in the extra dimension
     everywhere and not only while the corridor exists (127, 275) and are static, not moving relative to each other
     (141, the form of 140's entangled pin).  So the separation is no degree of freedom and there is no radion, no
     field for the ghost to live in (b5_positive B5c, DERIVED from 127 and 141; static and face to face the pair is one
     Randall-Sundrum plane at long range, STATIC.md S2); 275 removes the forming and dissolving through r > 0 that
     POSITIVITY.md left live.  What remains in the flat form, the pair moved together, has +1/2 (computed).  The marks
     on g_coincide (276, 277) and b5_positive (281) concern how the two tensions enter the junction one-way; the hold
     acts on the separation however they enter.  The record's other value-set sign, Newton's constant on a plane of
     negative tension (Shiromizu-Maeda-Sasaki, "the wrong sign of G_N if lambda < 0": G2 = -G/4, g2_between G1, the
     one-plane law superseded there by the per-sheet count), is a coupling, not a kinetic term, and enters no T_ab.
What this does not prove.
  - The sign of a plane's offset: it is the vacuum's energy, plane structure (201), not matter; b5a_residue A2 carries
    it with the tension.
  - Anything of a matter that is not built of particles, scalar fields and gauge fields: none is in the record, and
    202 gives position 2 our definitions.
  - That position 2's plane's displacement is healthy: it is a ghost (P10).  What is shown is that the record holds
    it at zero (127, 141, 275), so it is no degree of freedom; a configuration with the planes apart is not M's.

Stdlib + sympy.  python3 pointwise.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ("The matter condition was misattributed. - prove the pointwise condition.",
         "any plane has its own structure in the same fashions that we do, the same definitions as we do, perhaps "
         "different values though", "The N bits reconstitute under position 2's own laws",
         "the NEC only ever appears to break, but never does", "Our universe is defined by its plane's tension and its "
         "dark-energy offset")
W321 = ("don't we already have such a defined term?", "Which is position 2's plane? - entangled",
        "I suggest the planes are static", "Coincident everywhere")
CITED = {os.path.join(HERE, "b5_positive.py"):
         "A separation held at zero is not a degree of freedom, so there is no radion",
         os.path.join(D68, "bulk", "POSITIVITY.md"): "It is a ghost at the coinciding planes too",
         os.path.join(D68, "bulk", "STATIC.md"):
         "the kinetic coefficient of the radion is proportional to the brane tension, which is negative",
         os.path.join(HERE, "b1_matter.py"): "the wrong sign of G_N if lambda < 0"}
ETA = sp.diag(-1, 1, 1, 1)


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def p1():
    """particles: T^ab = sum w p^a p^b; T(t, t) = sum w (p . t)^2"""
    n = 3
    ws = sp.symbols("w0:%d" % n, nonnegative=True)
    if MUT.get("negative_weight"):
        ws = (-ws[0],) + ws[1:]                             # the mutant: a species of negative number
    ps = [sp.Matrix(sp.symbols("p%d_0:4" % i, real=True)) for i in range(n)]
    T = sum((w * p * p.T for w, p in zip(ws, ps)), sp.zeros(4))  # T^ab
    t = sp.Matrix(sp.symbols("t0:4", real=True))
    tl = ETA * t                                            # t_a
    val = sp.expand((tl.T * T * tl)[0])
    sq = sp.expand(sum(w * ((ETA * p).T * t)[0] ** 2 for w, p in zip(ws, ps)))
    nonneg = all(w.is_nonnegative for w in ws)
    return dict(identity=sp.simplify(val - sq) == 0, weights_nonneg=bool(nonneg))


def p2():
    """scalar fields: T(k, k) = (k . d phi)^2 for any V; T(u, u) = (1/2) phidot^2 + (1/2)|grad phi|^2 + V"""
    d = sp.Matrix(sp.symbols("d0:4", real=True))           # d_a phi
    V, Vmin = sp.symbols("V V_min", real=True)
    s = -1 if MUT.get("ghost_scalar") else 1                # the mutant: the kinetic term of the other sign
    gi = ETA.inv()
    kin = (d.T * gi * d)[0]
    T = s * (d * d.T - ETA * kin / 2) - ETA * V             # T_ab
    kx, ky, kz = sp.symbols("k_x k_y k_z", real=True)
    k = sp.Matrix([sp.sqrt(kx ** 2 + ky ** 2 + kz ** 2), kx, ky, kz])
    Tkk = sp.simplify((k.T * T * k)[0])
    nec = sp.simplify(Tkk - (k.T * d)[0] ** 2) == 0
    u = sp.Matrix([1, 0, 0, 0])
    Tuu = sp.simplify((u.T * T * u)[0])
    wec_form = sp.simplify(Tuu - (d[0] ** 2 / 2 + (d[1] ** 2 + d[2] ** 2 + d[3] ** 2) / 2 + V)) == 0
    above = sp.simplify((Tuu - V).subs(V, 0))               # the kinetic and gradient part, V measured from V_min
    above_nonneg = all(c >= 0 for c in sp.Poly(above, *d).coeffs())
    return dict(nec=nec, wec_form=wec_form, above_nonneg=above_nonneg)


def p3():
    """gauge fields: T(u, u) = (E^2 + B^2)/2, T(k, k) = |E_perp + n x B|^2"""
    E = sp.Matrix(sp.symbols("E_x E_y E_z", real=True))
    B = sp.Matrix(sp.symbols("B_x B_y B_z", real=True))
    F = sp.zeros(4)                                          # F_ab, signature -+++: F_0i = -E_i, F_ij = eps_ijk B_k
    for i in range(3):
        F[0, i + 1], F[i + 1, 0] = -E[i], E[i]
    F[1, 2], F[2, 1] = B[2], -B[2]
    F[2, 3], F[3, 2] = B[0], -B[0]
    F[3, 1], F[1, 3] = B[1], -B[1]
    gi = ETA.inv()
    Fup = gi * F * gi
    F2 = sum(F[a, b] * Fup[a, b] for a in range(4) for b in range(4))
    s = -1 if MUT.get("ghost_gauge") else 1                 # the mutant: the gauge field's sign reversed
    T = s * (F * gi * F.T - ETA * F2 / 4)                   # T_ab = F_ac F_b^c - g_ab F^2/4
    u = sp.Matrix([1, 0, 0, 0])
    Tuu = sp.simplify((u.T * T * u)[0])
    wec = sp.simplify(Tuu - (E.dot(E) + B.dot(B)) / 2) == 0
    th, ph = sp.symbols("theta phi", real=True)
    nvec = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
    k = sp.Matrix([1, nvec[0], nvec[1], nvec[2]])
    Tkk = sp.simplify((k.T * T * k)[0])
    Eperp = E - E.dot(nvec) * nvec
    sq = (Eperp + nvec.cross(B)).dot(Eperp + nvec.cross(B))
    nec = sp.simplify(sp.expand(Tkk - sq)) == 0
    return dict(wec=wec, nec=nec)


def p6():
    """a fundamental field's kinetic coefficient Z: phi = chi/sqrt|Z| takes its size into V and leaves its sign"""
    d = sp.Matrix(sp.symbols("c0:4", real=True))           # d_a chi
    z = sp.Symbol("z", positive=True)
    chi = sp.Symbol("chi", real=True)
    V = sp.Function("V")
    kin = (d.T * ETA.inv() * d)[0]
    out = {}
    for sgn in (1, -1):
        Z = sgn * z
        L = -(Z / 2) * kin / z - V(chi / sp.sqrt(z))       # -(Z/2)(d phi)^2 - V(phi) at phi = chi/sqrt(z)
        if MUT.get("rescale_flips"):
            L = -(z / 2) * kin / z - V(chi / sp.sqrt(z))    # the mutant: the rescaling read as taking the sign too
        kin_coeff = sp.simplify(sp.diff(L, d[0], 2) / 2)   # chidot^2's coefficient: sgn/2 if the sign stays
        out[sgn] = kin_coeff
    return dict(size_gone=all(z not in v.free_symbols for v in out.values()),
                sign_kept=out[1] == sp.Rational(1, 2) and out[-1] == sp.Rational(-1, 2))


def p10():
    """the record's ghost: a sheet's displacement carries its tension as inertia; PRZ's C_r at r = 0; the hold"""
    tau, eps = sp.Symbol("tau", real=True), sp.Symbol("epsilon", positive=True)
    fd = sp.Matrix(sp.symbols("f0:4", real=True))          # d_a f
    gi = ETA.inv()
    kin = (fd.T * gi * fd)[0]
    sheet = sp.Abs(tau) if MUT.get("inertia_abs") else tau  # the mutant: a sheet's inertia read as |tension|
    lag = -sheet * sp.sqrt(1 + eps ** 2 * kin)             # Nambu-Goto on the induced metric eta + eps^2 d f d f
    L2 = sp.expand(sp.series(lag, eps, 0, 3).removeO().coeff(eps, 2))
    s_ = sp.simplify(-2 * L2 / kin)                        # L2 = -(s/2)(d f)^2: P2's form with the sign s
    G = sp.Matrix(4, 4, sp.symbols("G0:16", real=True))    # g^ab, varied
    Lg = -(s_ / 2) * (fd.T * G * fd)[0]
    T = sp.Matrix(4, 4, lambda a, b: -2 * sp.diff(Lg, G[a, b]) + ETA[a, b] * Lg).subs(
        {G[a, b]: gi[a, b] for a in range(4) for b in range(4)})
    kx, ky, kz = sp.symbols("k_x k_y k_z", real=True)
    k = sp.Matrix([sp.sqrt(kx ** 2 + ky ** 2 + kz ** 2), kx, ky, kz])
    Tkk = sp.simplify((k.T * T * k)[0])
    nambu = sp.simplify(Tkk - tau * (k.T * fd)[0] ** 2) == 0  # T(k, k) = tau (k . d f)^2, its sign the tension's
    t1, t2 = sp.Rational(4, 3), sp.Rational(-1, 3)         # 139 (1): ours and position 2's, one-plane units
    v1, v2, vF, vr = sp.symbols("v1 v2 vF vr", real=True)
    K = t1 * v1 ** 2 / 2 + t2 * v2 ** 2 / 2
    Ks = sp.expand(K.subs({v1: vF - t2 * vr / (t1 + t2), v2: vF + t1 * vr / (t1 + t2)}))
    together, apart = Ks.coeff(vF, 2), Ks.coeff(vr, 2)
    cross = Ks.coeff(vF, 1).coeff(vr, 1)
    MP = _load(os.path.join(D68, "bulk", "multiplane.py"), "pw_mp")
    d = MP.lr()
    tau2 = -d["tau2"] if MUT.get("prz_tau_sign") else d["tau2"]  # the mutant: position 2's tension read reversed
    Cr0 = sp.simplify(d["Cr"].subs(MP.r, 0))
    rel = sp.simplify(Cr0 * tau2 - (24 * MP.M ** 3) ** 2)
    q = {MP.kR: sp.Rational(3, 4) * MP.kL}
    quarter = sp.simplify(Cr0.subs(q).subs({MP.M: 1, MP.kL: 1}))
    t2q = sp.simplify((tau2 / d["tau1"]).subs(q))
    modes = {"together": together, "apart": apart}          # 127, 275: coincident; 141: static, the separation held
    held = {m: c for m, c in modes.items() if m != "apart" or MUT.get("radion_free")}  # the mutant: the separation free
    return dict(nambu=nambu, s=s_, together=together, apart=apart, cross=cross, rel=rel, Cr_quarter=quarter,
                tau2_over_tau1=t2q, held=held)


def fluid():
    """a perfect fluid: rho + p = T(k, k)/(k . u)^2 for k = u + e"""
    rho, p = sp.symbols("rho p", real=True)
    u = sp.Matrix([1, 0, 0, 0])
    ul = ETA * u
    T = (rho + p) * ul * ul.T + p * ETA
    k = sp.Matrix([1, 1, 0, 0])
    return sp.simplify((k.T * T * k)[0] / ((ETA * k).T * u)[0] ** 2 - (rho + p)) == 0


def compute():
    return dict(p1=p1(), p2=p2(), p3=p3(), fluid=fluid(), p6=p6(), p10=p10())


def report(o):
    print("pointwise.py -- the pointwise matter condition proved (item 320)\n")
    print("P1 particles: T(t, t) = sum w (p . t)^2 exactly %s; weights non-negative %s" % (
        o["p1"]["identity"], o["p1"]["weights_nonneg"]))
    print("P2 scalars: T(k, k) = (k . d phi)^2 for every V %s; T(u, u) = phidot^2/2 + |grad phi|^2/2 + V %s; above the "
          "vacuum a sum of squares %s" % (o["p2"]["nec"], o["p2"]["wec_form"], o["p2"]["above_nonneg"]))
    print("P3 gauge: T(u, u) = (E^2 + B^2)/2 %s; T(k, k) = |E_perp + n x B|^2 %s" % (o["p3"]["wec"], o["p3"]["nec"]))
    print("P4 a perfect fluid's rho + p = T(k, k)/(k . u)^2: %s" % o["fluid"])
    print("P6 a fundamental field rescaled: its size gone %s, its sign kept %s" % (o["p6"]["size_gone"],
          o["p6"]["sign_kept"]))
    t = o["p10"]
    print("P10 a sheet displaced: L2 = -(s/2)(d f)^2 with s = %s; T(k, k) = tau (k . d f)^2 %s" % (t["s"], t["nambu"]))
    print("    two sheets (4/3, -1/3): together %s, apart %s, cross %s; PRZ C_r tau2 - (24 M^3)^2 = %s; "
          "quarter: C_r = %s, tau2/tau1 = %s" % (t["together"], t["apart"], t["cross"], t["rel"], t["Cr_quarter"],
                                                 t["tau2_over_tau1"]))
    print("    held (127, 141, 275): the modes that remain %s" % t["held"])


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("P0 item 320's order, 202, 284 (1), 120 and 201 verbatim in the rulings file", all(w in rul for w in WORDS))
    add("P1 particles: T(t, t) is the sum of w (p . t)^2 with w >= 0, for every t (weak and null conditions)",
        o["p1"]["identity"] and o["p1"]["weights_nonneg"])
    add("P2 scalar fields: T(k, k) = (k . d phi)^2 for every potential; T(u, u) a sum of squares above the vacuum",
        o["p2"]["nec"] and o["p2"]["wec_form"] and o["p2"]["above_nonneg"])
    add("P3 gauge fields: T(u, u) = (E^2 + B^2)/2 and T(k, k) = |E_perp + n x B|^2", o["p3"]["wec"] and o["p3"]["nec"])
    add("P4 a perfect fluid's rho + p is T(k, k)/(k . u)^2, so P1-P3 give rho >= 0 and rho + p >= 0", o["fluid"])
    add("P6 a fundamental field's kinetic coefficient: rescaling takes its size and keeps its sign",
        o["p6"]["size_gone"] and o["p6"]["sign_kept"])
    t = o["p10"]
    cited = all(" ".join(c.split()) in " ".join(open(f, encoding="utf-8").read().split()) for f, c in CITED.items())
    add("P10 the record's ghost: 321, 140, 141, 275 verbatim; B5c, POSITIVITY Q1, PRZ p.2 and SMS's sign cited verbatim",
        all(w in rul for w in W321) and cited)
    add("P10 a sheet's inertia is its tension: s = tau, T(k, k) = tau (k . d f)^2; the separation -2/9, together +1/2",
        t["nambu"] and t["s"] == sp.Symbol("tau", real=True) and t["apart"] == sp.Rational(-2, 9)
        and t["together"] == sp.Rational(1, 2) and t["cross"] == 0)
    add("P10 PRZ: C_r tau2 = (24 M^3)^2 at r = 0; 139 (1)'s quarter gives tau2 = -tau1/4 and C_r = -96",
        t["rel"] == 0 and t["Cr_quarter"] == -96 and t["tau2_over_tau1"] == sp.Rational(-1, 4))
    add("P10 held (127, 141, 275): the separation is no degree of freedom; every mode that remains has positive inertia",
        "apart" not in t["held"] and len(t["held"]) > 0 and all(c > 0 for c in t["held"].values()))
    return res


MUTANTS = {"negative_weight": "a species of negative number (P1)",
           "ghost_scalar": "a scalar's kinetic term of the other sign (P2)",
           "ghost_gauge": "a gauge field's sign reversed (P3)",
           "rescale_flips": "a rescaling read as taking a field's sign too (P6)",
           "inertia_abs": "a sheet's inertia read as its tension's size (P10)",
           "prz_tau_sign": "position 2's tension read with its sign reversed (P10)",
           "radion_free": "the separation read as a free degree of freedom (P10)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-16s %-56s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
