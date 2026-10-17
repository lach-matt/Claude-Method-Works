#!/usr/bin/env python3
"""magnetic_chain.py -- item 463: the whole warp chain re-evaluated under a magnetic corridor (462) in place of an
electric one.  M (463): "We will need to reevaluate the whole warp chain under a magnetic corridor instead of electric".
Labels: READ (quoted), computed, deduced; each row's class is the board's reading, with its reason, to be overruled by
M at any point.  Worked in the conversation; not verified; not seated.  2026-10-17.

  K0 (read) M's words: 462, 463.
  K1 (deduced) Every row of the register (warptheorem.py LEMMAS_NOW, 80 rows) classed by what the charge's kind does
     to it:
       unchanged  -- the row does not involve the corridor's charge;
       duality    -- the row involves the charged hole only through its stress tensor, which the plane's duality
                     F -> *F leaves as it was (461 W14): electric and magnetic give the same geometry and energy;
       changed    -- the row's statement, or the note beside it, rested on electric physics and moves;
       opened     -- magnetic physics raises a question the row did not face.
     No row moves on the register (446): the classes are notes beside the rows.
  K2 (deduced) The corridor's computed stages classed the same way (sections 11-26).
  K3 (computed; READ) The magnetic numbers at both ends of the family, the charge ratio Q/r+ = 0.42 of P2's member:
     the small end r+ = 1.79 ell at ell = 2^84 l_P (section 25), the large end the Earth cap, r+ = 8.870 mm (372).
     Per end: the geometric charge q = Q/r+ * r+ in Planck lengths; the Dirac integer Q = q e/sqrt(pi) (Maldacena
     2004.06084 (3)); the horizon field |F| = Q/(2 r+^2) over Schwinger's m_e^2 (an electric charge discharges, 461
     W13) and over m_W^2 (the electroweak symmetry restored near the horizon); the plane's dual theory's degrees of
     freedom N^2 = (pi/2)(ell/l_P)^2 against the magnetic hole's 9Q two-dimensional modes (stage 2's quantum stress).
  K4 (READ; deduced; computed) Formation.  Dowker, Gauntlett, Giddings and Horowitz (hep-th/9312172), READ:
     "Pair production of black holes is necessarily a topology changing process"; the Ernst solution "describes two
     oppositely charged black holes undergoing uniform acceleration in a background magnetic field"; Garfinkle and
     Strominger's instanton has "the horizons of the two black holes ... identified to form a wormhole in space";
     the wormhole instanton's action is S_E = 4 pi q^2 (1 - qB)^2/(1 - (1 - qB)^4) (their (A.7)), "the Schwinger
     result" pi m^2/(qB) for weak fields, Gamma = e^(-S_E).  Deduced: the 26 hold no magnetic charge, so on our plane
     dF = 0 everywhere and the flux through any closed surface that bounds is zero; B4 (step 2: the topology is
     preserved) keeps every such surface bounding.  So no classical process -- the README's arrival, the opening, any
     device built of the 26's matter -- gives the corridor's mouth a magnetic charge.  An electric charge, by
     contrast, can be gathered from charged matter (d*F = J).  The quantum route is pair creation: both mouths in one
     universe, opposite charges, a Wheeler wormhole between them.  Computed: S_E at a magnetar's field (1e11 T) is
     ~1e68 at the small end and ~1e75 at the large; S_E falls to order one only as qB -> 1, a background field as
     strong as the hole's own horizon field over a region holding the pair's mass.
  K5 (READ; deduced) The closing.  Maldacena (2004.06084, READ): "Extremal magnetic black holes are more stable than
     their electric counterparts, since unit charge magnetic monopoles are much heavier than electrically charged
     particles"; decay by emitting smaller magnetic holes is suppressed as e^(-S), S > pi Q (M l_p)^2 (his (13)).
     Deduced: a magnetic hole radiates down to extremality and then stops; with no lighter magnetic charge in the 26
     it does not close by Hawking emission.  CLOSE and CLOSEs (the face closing by emission over the hole's life) are
     the uncharged hole's; for the magnetic corridor the face stays open as an extremal hole unless its charge is
     cancelled, which only its pair partner can do.
  K6 (computed; deduced) The bulk carries no field.  Under section 25's W11 the field lives on the plane, its bulk
     share at most ~1e-15, and the plane's magnetic field solves Maxwell exactly there (462): the bulk is vacuum, as
     B2/B2t state, and its field energy outside the neck (E4r, E4rs) is the uncharged hole's to that order.

python3 magnetic_chain.py [--selftest | --mutants | --table]
"""
import importlib.util
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
THEOREM = os.path.join(D68, "warptheorem.py")
WORDS = ("We will need to reevaluate the whole warp chain under a magnetic corridor instead of electric",
         "Yes, a magnetic corridor")
MUT = set()

LP = 1.616255e-35                     # m
MPL_GEV = 1.220890e19
HBARC = 1.973269804e-16               # GeV m
ALPHA0 = 1 / 137.035999
M_E, M_W = 0.51099895e-3, 80.369      # GeV
MU_T = 0.42                           # P2's member's Q/r+
ELL = LP * 2.0**84                    # section 25's placement
ENDS = {"small": 1.79 * ELL, "large": 8.870e-3}
B_MAGNETAR_T = 1e11
GEOM_PER_TESLA = 1e4 * math.sqrt(6.674e-8) / 2.99792458e10**2 * 100   # 1/m per tesla (Gaussian geometrized)

C_UN, C_DU, C_CH, C_OP = "unchanged", "duality", "changed", "opened"
ROWS = {
    "G1": (C_DU, "E(N) is the uncharged hole's; the charged corridor's field energy (447 note) is the same for a magnetic field (W14); the electroweak corona lowers it slightly (Maldacena section 2.3)"),
    "G2": (C_UN, "E(N) computed for the uncharged hole"),
    "G3": (C_UN, "the horizon's size fixed by N"),
    "H1": (C_UN, "the horizon's bit count"),
    "H2": (C_DU, "r+ and r- as our face and position 2's (447 note) are the same for either charge; but section 26's prior art predicts no regular r- for a hole like this (S12)"),
    "H2tu": (C_UN, "the horizon's trace on each plane"),
    "H2txs": (C_UN, "position 2's bit area"),
    "H2tx": (C_UN, "position 2's bit area"),
    "O1a": (C_DU, "the one object read one way; the charge's kind does not enter"),
    "O1bs": (C_DU, "routes through r- (447 note) are the same for either charge; every one assumes an inner horizon the prior art does not expect (section 26)"),
    "O1cs": (C_DU, "as O1bs"),
    "O1b": (C_DU, "as O1bs, at the large end"),
    "O1c": (C_DU, "as O1cs, at the large end"),
    "O2": (C_OP, "the uncharged hole's surface gravity; a magnetic hole is driven toward extremality by its own emission (Maldacena section 4), so the corridor's surface gravity falls over its life"),
    "O3s": (C_CH, "an electric corridor loses its charge at once (461 W13); a magnetic one keeps it through the hold (W14): the charged hold is the magnetic corridor's"),
    "O3": (C_CH, "as O3s, at the large end"),
    "Z1q": (C_UN, "a general identity for the plane"),
    "Z1ts": (C_DU, "a radial magnetic field has T^t_t = T^r_r as a radial electric one does: the null energy along the radial ray stays zero (446 note)"),
    "Z1t": (C_DU, "as Z1ts, at the large end"),
    "Z2rs": (C_DU, "the plane's reading of our leg; the stress tensor is the same"),
    "Z2r": (C_DU, "as Z2rs, at the large end"),
    "Z3a": (C_UN, "null energy away from the corridor"),
    "Z3bs": (C_DU, "the passage's negative energy is quantum; with magnetic flux the two-dimensional modes along the field lines are its carrier (MMP, 445 (2)) -- the row's statement stands"),
    "Z3b": (C_DU, "as Z3bs, at the large end"),
    "Z3c": (C_UN, "the plane's dark energy"),
    "B1": (C_UN, "each plane's matter, Gauss and Codazzi"),
    "B2": (C_UN, "a vacuum bulk beneath the plane"),
    "B2ts": (C_CH, "the bulk beneath the magnetic corridor is vacuum to ~1e-15 (W11, K6): B2's vacuum holds for the charged corridor itself, where the electric bulk U(1) (446) put a field in it"),
    "B2t": (C_CH, "as B2ts, at the large end"),
    "B3s": (C_DU, "a complete bulk; the field lives on the plane"),
    "B3": (C_DU, "as B3s, at the large end"),
    "B4a": (C_CH, "the positions joined through the bulk with no horizons until the opening: with no magnetic charge in the 26 and the topology preserved (B4), no net magnetic flux can appear at our mouth when it opens (K4)"),
    "B4ds": (C_CH, "the opening evolves regularly in five dimensions; a regular classical evolution conserves zero magnetic flux, so the opening cannot make a magnetic corridor (K4)"),
    "B4d": (C_CH, "as B4ds, at the large end"),
    "B5a": (C_UN, "positivity at the coincidence"),
    "B5cs": (C_OP, "position 2's positivity where the README lands; near a magnetic mouth the electroweak and QCD coronae, and baryon number violated as monopoles do (Maldacena; Callan-Rubakov), act on the plane's matter there"),
    "B5c": (C_OP, "as B5cs, at the large end"),
    "B5pu": (C_UN, "position 2's matter, within one universe"),
    "B5px": (C_UN, "position 2's matter, between universes"),
    "B5b": (C_UN, "a smooth wall keeps null energy"),
    "B6": (C_UN, "k's ratio"),
    "B6'": (C_UN, "k's scale, a definition"),
    "B8": (C_UN, "the bulk's law is Einstein's"),
    "B7": (C_CH, "formation: the corridor must acquire its magnetic charge, which no classical process can give it (K4); the quantum route, pair creation, is topology changing and puts both mouths in one universe"),
    "I1": (C_UN, "the passage as N bits"),
    "I2": (C_UN, "the capacity bound"),
    "E1us": (C_CH, "'discharge aside' (447 note) becomes exact: a magnetic hole does not discharge; its emission is the uncharged hole's below m_e and enhanced by its charge above (Maldacena (16)-(17))"),
    "E1u": (C_CH, "as E1us, at the large end"),
    "E2us": (C_UN, "position 2's closing energy"),
    "E2u": (C_UN, "as E2us, at the large end"),
    "E1xs": (C_UN, "nothing of our E crosses; the magnetic flux threads the bridge without carrying energy across"),
    "E1x": (C_UN, "as E1xs, at the large end"),
    "E2xs": (C_UN, "position 2's closing energy"),
    "E2x": (C_UN, "as E2xs, at the large end"),
    "E3": (C_UN, "the ledger"),
    "E4rs": (C_CH, "the field energy outside the neck: the 446 note had the bulk carry the U(1)'s field energy; on the magnetic corridor the field is on the plane and the bulk carries none to ~1e-15 (K6)"),
    "E4r": (C_CH, "as E4rs, at the large end"),
    "R0": (C_UN, "the read"), "R1": (C_UN, "exact reconstruction"), "R2": (C_UN, "the copy under position 2's laws"),
    "R3": (C_UN, "exactness over the mass window"), "R4": (C_UN, "the corridor's length as a trajectory difference"),
    "R5": (C_UN, "the build's mechanism"), "R6": (C_UN, "the room"),
    "RECON": (C_UN, "reconstruction to the 26 of any position 2"), "ENCODE": (C_UN, "the encoding"),
    "M1s": (C_DU, "the plane's reading of the mouth: four-dimensional Reissner-Nordstrom on the plane is the same for a magnetic charge (455 note)"),
    "M1": (C_DU, "as M1s, at the large end"),
    "M1P2xs": (C_DU, "position 2's side; the stress tensor is the same"),
    "M1P2x": (C_DU, "as M1P2xs, at the large end"),
    "FARs": (C_DU, "a far surface around the hole; the magnetic field on the plane falls as the electric one does"),
    "FAR": (C_DU, "as FARs, at the large end"),
    "WRITEs": (C_UN, "the write's least time"), "WRITE": (C_UN, "as WRITEs, at the large end"),
    "ARRIVALs": (C_CH, "the README, energy alone, makes no inner horizon (C1) and needs the hole charged by a device no row places (446 note); for a magnetic charge no device built of the 26's matter can do it (K4)"),
    "ARRIVAL": (C_CH, "as ARRIVALs, at the large end"),
    "CLOSEs": (C_CH, "our face closes by Hawking emission over the hole's life: a magnetic hole radiates to extremality and then stops, stable in the 26 (K5); the face stays open unless its charge is cancelled"),
    "CLOSE": (C_CH, "as CLOSEs, at the large end"),
    "SOURCEs": (C_CH, "the README's source as energy alone cannot carry a magnetic charge; the corridor's charge needs a source of its own (K4)"),
    "SOURCE": (C_CH, "as SOURCEs, at the large end"),
}

STAGES = [
    ("section 14", "the charged hole's chain", C_DU, "Reissner-Nordstrom on the plane is the same for either charge; its five-dimensional realization had a bulk charge, now on the plane (Kaus and Reall's limit)"),
    ("445 (2)", "MMP's wormhole on our plane", C_OP, "already magnetic: two oppositely charged mouths in one universe, the pair a magnetic charge must come in (K4); set aside at 446 as not the corridor"),
    ("446 (1)", "the bulk U(1)", C_CH, "stale under 459 (S1): the U(1) is the 26's, on the plane"),
    ("447", "stage 1: the dictionary", C_DU, "the plane's chain is the same; the five-dimensional exact chain used a bulk charge (W2) and its inner horizon is the one the prior art does not expect"),
    ("448", "stage 2: the inner horizon", C_UN, "its quantum stress is the plane's dual theory's, N^2 ~ 1e50 degrees of freedom against the magnetic hole's 9Q ~ 1e25-1e32 two-dimensional modes (K3)"),
    ("449-452", "stage 3 and V1-V3", C_DU, "the solver's validation stands; its physical model, MM's bulk magnetic U(1), is stale under 459"),
    ("453", "the approach", C_CH, "'no axis under the bulk field's magnetic flux' was a bulk-field statement; the bulk carries none"),
    ("454", "P1: the throat with the plane", C_DU, "Kaus and Reall's throat, the field on the plane, is the same for a magnetic field by duality"),
    ("455", "P2: one charged hole", C_DU, "the lam = 64 electric member; the magnetic field-on-plane hole is P3m's (R4 = 1.810 ell)"),
    ("457, 462", "P3", C_UN, "already magnetic (462)"),
    ("444, 445 (1)", "C1, C2: the neutral delivery", C_UN, "neutral; its consequence sharpens: the charge must come from elsewhere, and a magnetic charge cannot come from matter (K4)"),
]


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def register_ids():
    spec = importlib.util.spec_from_file_location("mc_wt", THEOREM)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return [r[1].split()[0] for r in mod.LEMMAS_NOW]


def classes(ids):
    table = dict(ROWS)
    if "drop_row" in MUT:
        table.pop("CLOSE")
    return {r: table.get(r) for r in ids}


def end_numbers(rplus):
    e = math.sqrt(4 * math.pi * ALPHA0)
    q = MU_T * rplus / LP                               # geometric charge, Planck lengths
    Q = q * e / math.sqrt(math.pi)                      # Dirac integer
    rp = rplus / LP
    F = Q / (2 * rp**2) * MPL_GEV**2                    # GeV^2
    N2 = (math.pi / 2) * (ELL / LP)**2
    qB_mag = (MU_T * rplus) * B_MAGNETAR_T * GEOM_PER_TESLA
    if "weak_field_sign" in MUT:
        qB_mag = -qB_mag
    return dict(q=q, Q=Q, schw=F / M_E**2, ew=F / M_W**2, N2=N2, modes=9 * Q, qB=qB_mag,
                S_mag=pair_action(q, qB_mag), r_w=math.sqrt(Q / 2) / M_W * HBARC)


def pair_action(q, qB):
    """DGGH (A.7), the Einstein-Maxwell wormhole instanton: S_E = 4 pi q^2 (1 - qB)^2 / (1 - (1 - qB)^4)"""
    if qB < 1e-6:                                       # the weak-field series, pi q^2 (1/(qB) - 1/2)
        return math.pi * q**2 * (1 / qB - 0.5) if qB > 0 else float("nan")
    return 4 * math.pi * q**2 * (1 - qB)**2 / (1 - (1 - qB)**4)


def report(table_only=False):
    ids = register_ids()
    cl = classes(ids)
    counts = {}
    for r in ids:
        counts[cl[r][0]] = counts.get(cl[r][0], 0) + 1
    print("K1 the register's %d rows under a magnetic corridor: %s" % (len(ids), ", ".join(
        "%s %d" % (k, counts.get(k, 0)) for k in (C_UN, C_DU, C_CH, C_OP))))
    for k in (C_CH, C_OP, C_DU, C_UN):
        print("  %s:" % k)
        for r in ids:
            if cl[r][0] == k:
                print("    %-8s %s" % (r, cl[r][1]))
    if table_only:
        return
    print("K2 the corridor's stages:")
    for tag, name, k, why in STAGES:
        print("  %-12s %-32s %-9s %s" % (tag, name, k, why))
    print("K3 the magnetic numbers (Q/r+ = %.2f):" % MU_T)
    for end, rp in ENDS.items():
        n = end_numbers(rp)
        print("  %-5s r+ %.3g m: q %.3g l_P, Q %.3g; |F|/m_e^2 %.3g (electric discharges), |F|/m_W^2 %.3g; "
              "corona r_w %.3g m; N^2 %.3g vs 9Q %.3g" % (end, rp, n["q"], n["Q"], n["schw"], n["ew"], n["r_w"], n["N2"],
                                                          n["modes"]))
        print("        pair creation at a magnetar's 1e11 T: qB %.2g, S_E %.3g; S_E at qB = 0.5: %.3g" % (
            n["qB"], n["S_mag"], pair_action(n["q"], 0.5)))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("K0 words: %s" % r)
    ids = register_ids()
    cl = classes(ids)
    missing = [i for i in ids if cl[i] is None]
    extra = [k for k in ROWS if k not in ids]
    r = len(ids) == 80 and not missing and not extra; ok.append(r)
    say("K1 all 80 rows classed, none extra: %s%s" % (r, (" (missing %s, extra %s)" % (missing, extra)) if not r else ""))
    if missing:
        return False
    counts = {}
    for i in ids:
        counts[cl[i][0]] = counts.get(cl[i][0], 0) + 1
    want = {C_UN: 38, C_DU: 21, C_CH: 18, C_OP: 3}
    r = counts == want; ok.append(r); say("K1 the counts %s: %s" % (counts, r))
    r = all(cl[i][0] == C_CH for i in ("B7", "B4a", "ARRIVAL", "ARRIVALs", "CLOSE", "CLOSEs", "SOURCE", "SOURCEs"))
    ok.append(r); say("K1 formation, arrival, closing and source changed: %s" % r)
    r = len(STAGES) == 11 and all(k in (C_UN, C_DU, C_CH, C_OP) for _, _, k, _ in STAGES); ok.append(r)
    say("K2 the corridor's 11 stages classed: %s" % r)
    s, l = end_numbers(ENDS["small"]), end_numbers(ENDS["large"])
    r = 2.4e24 < s["Q"] < 2.6e24 and 5.8e17 < s["schw"] < 6.0e17 and l["schw"] > 1 and s["ew"] > 1; ok.append(r)
    say("K3 small end Q %.3g, |F|/m_e^2 %.3g; large end |F|/m_e^2 %.3g (both discharge if electric): %s" % (
        s["Q"], s["schw"], l["schw"], r))
    r = s["N2"] / s["modes"] > 1e20 and s["N2"] / l["modes"] > 1e15; ok.append(r)
    say("K3 the dual theory outweighs the two-dimensional modes (%.1g, %.1g): %s" % (s["N2"] / s["modes"],
                                                                                    s["N2"] / l["modes"], r))
    # K4: the exact action against DGGH's weak-field series and its leading Schwinger term
    q = 10.0
    ex = 4 * math.pi * q**2 * (1 - 1e-3)**2 / (1 - (1 - 1e-3)**4)
    se = math.pi * q**2 * (1 / 1e-3 - 0.5)
    r = abs(ex / se - 1) < 1e-3 and s["S_mag"] > 1e60 and l["S_mag"] > 1e70 and pair_action(q, 0.999999) < 1
    ok.append(r); say("K4 (A.7) against its series %.6f; S_E at a magnetar %.2g, %.2g; order one only as qB -> 1: %s" % (
        ex / se, s["S_mag"], l["S_mag"], r))
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    names = ["drop_row", "weak_field_sign"]
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:
            bad = True
        caught += bad
        print("mutant %-16s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(table_only="--table" in sys.argv)
