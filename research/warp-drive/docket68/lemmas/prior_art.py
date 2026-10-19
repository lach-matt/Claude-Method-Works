#!/usr/bin/env python3
"""prior_art.py -- item 442, phase 1: every reading of the warp theorem held against previous art and works in the
field, before any computation.  M, 442: "Prove all readings in the warp theorem using previous arts and works in the
field, and after that, then use computation to prove the rest."  The readings are the premises the rows rest on:
the 54 rulings of kinds S and N (refound.py; the eight of kind P drop), the definitions R0, R1, R2 and R6 (B6' is
ruling 201, RECON ruling 437), and the three readings of the board's that M confirmed (328, 334, 353).
Labels: READ (each source's line below is verbatim from its abstract, read 2026-10-16, or from the instrument named
where it was READ earlier; ML's carries a gloss after the dash, and ellipses mark cuts), deduced (every verdict is
the board's reading of the sources, put to M), M's (the rulings).  Worked in the conversation; not verified; not seated.

  A0 (read) M's words, verbatim: 442's direction.
  A1 (READ) The sources, each with its identifier and the line read.
  A2 (deduced) Each reading's verdict.
     EST    -- the prior art establishes it, or its realizability, as stated.
     PART   -- the prior art establishes a part or a weaker form; what remains is named, for computation.
     CONTRA -- the prior art is contrary, in whole or in part: a finding, recorded, not repaired.
     ABSENT -- the prior art does not hold it: a choice of the device's with no physics claim (realizable by
               construction, computed), or a claim the literature does not carry.
  A3 (computed) Coverage: every S and N ruling the rows name, every definition and every confirmed reading has a
     verdict; every source a verdict cites is in A1; the counts.
  A4 (deduced) What phase 2 computes: each PART's and ABSENT's remainder, in the approved order (B6' first).
What this does not do: it reads abstracts and the passages named, not every page; a verdict of EST rests on the
quoted line and the paper's standing, and a reading the literature only discusses is PART, not EST.

python3 prior_art.py [--selftest | --mutants]
"""
import collections
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ("Prove all readings in the warp theorem using previous arts and works in the field, and after that, then use "
         "computation to prove the rest.",)

# A1: key -> (identifier, the line read, verbatim)
SOURCES = {
    "SMS": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076",
            "We derive the effective gravitational equations on the brane, which reduce to the conventional Einstein "
            "equations in the low energy limit."),
    "SMS_NEG": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076",
                "the brane with the negative tension is an anti-gravity world and hence should be excluded from the "
                "physical point of view"),
    "BDEL": ("Binetruy, Deffayet, Ellwanger, Langlois, hep-th/9910219",
             "We also show that a tiny deviation from exact compensation leads to an effective cosmological constant at "
             "late time."),
    "GS_DS": ("Gen, Sasaki, gr-qc/0011078",
              "if there is only one de Sitter brane with positive tension, there is no radion and thus the ordinary "
              "Einstein gravity is recoverd on the brane other than corrections due to the massive Kaluza-Klein modes"),
    "DS_IN_ADS": ("hep-th/0006069 (Inflationary solutions in the brane-world and their geometrical interpretation)",
                  "We show that in all cases the bulk geometry is that of anti-de Sitter (AdS5). We then present a "
                  "geometrical interpretation for the solutions as embeddings of two de Sitter (dS4) surfaces in AdS5"),
    "DS_THICK": ("hep-th/0701266 (de Sitter branes with a bulk scalar)",
                 "for the thick brane scenario the field profile resembles a kink"),
    "KAPNER": ("Kapner et al., hep-ph/0611184",
               "We find with 95% confidence that the inverse-square law holds (|alpha| <= 1) down to a length scale "
               "lambda = 56 um and that an extra dimension must have a size R <= 44 um."),
    "MK_42": ("Maartens, Koyama, 1004.3962v2 p.11 (READ in b6p_scale.py)",
              "Table-top tests of Newton's laws currently find no deviations down to O(10^-1 mm), so that ell <~ 0.1 "
              "mm in Equation (41)."),
    "ADEL": ("Adelberger et al., hep-ph/0611223v3 Table I (READ in b6p_scale.py)",
             "68% confidence laboratory constraints on power-law potentials ... k = 3: |beta_k| (this work) "
             "1.3 x 10^-4"),
    "DUFF": ("Duff, Liu, hep-th/0003237",
             "We find exact agreement with the coefficient appearing in the Randall-Sundrum brane-world proposal."),
    "KTN": ("Kudoh, Tanaka, Nakamura, gr-qc/0301089",
            "The sequence of small localized black holes exhibits a smooth transition from a five-dimensional "
            "Schwarzschild black hole, which is a solution in the limit of small horizon radius."),
    "YOSHINO": ("Yoshino, 0812.0465",
                "our result is naturally interpreted as the evidence for the nonexistence of solutions to this setup, "
                "although an \"approximate\" solution exists for sufficiently small brane tension"),
    "ACPY": ("Abdolrahimi, Cattoen, Page, Yaghoobpour-Tari, 1206.0708",
             "the Hawking temperature and entropy of an RSII static black hole have the same values as the "
             "Schwarzschild metric with the same mass"),
    "HOR_BULK": ("0710.4766 (Gravitational anomaly and Hawking radiation of brane world black holes)",
                 "the horizon of brane world black hole will extend into the bulk spacetime"),
    "WC": ("Wang, Choptuik, 1604.04832 (READ in settle_arrival.py A5)",
           "black holes that have finite extension into the bulk ... an apparently stationary state ... Clearly the "
           "agreement is very good"),
    "BGM": ("Bruni, Germani, Maartens, gr-qc/0108013",
            "we prove a no-go theorem: the exterior spacetime on the brane cannot be static"),
    "GD": ("hep-th/0603254 (Black holes and dark energy from gravitational collapse on the brane)",
           "We show that by allowing for pressure, the exterior of a fluid sphere can be static."),
    "DG": ("Dadhich, Ghosh, hep-th/0109086",
           "the collapsing sphere has the Vaidya radiation envelope which is followed by the brane analogue of the "
           "Schwarzschild solution"),
    "HR": ("Haggard, Rovelli, 1407.0989",
           "there is a classical metric satisfying the Einstein equations outside a finite spacetime region where "
           "matter collapses into a black hole and then emerges from a white hole"),
    "HR_QG": ("Haggard, Rovelli, 1407.0989",
              "For this to happen, quantum gravity should affect the metric also in a small region outside the horizon"),
    "BCG": ("Barcelo, Carballo-Rubio, Garay, 1511.00633",
            "We conclude that transitions with long characteristic time scales are pathologically unstable"),
    "BCG_SHORT": ("Barcelo, Carballo-Rubio, Garay, 1511.00633",
                  "geometries with short characteristic time scales are shown to be robust against perturbations"),
    "SEMI": ("2608.03538 (Semiclassical black hole-white hole transitions)",
             "the emergence of an anti-trapped region is a generic consequence of the amplification of negative "
             "energy fluxes propagating along the outgoing direction inside the initial trapped region"),
    "SS_BOUNCE": ("2610.04353 (Bouncing dust collapse and black-to-white hole transition on the brane)",
                  "the cloud re-emerges through a white hole region into a second asymptotic region"),
    "SS_TIMELIKE": ("2610.04353",
                    "the Shtanov--Sahni braneworld, in which the extra dimension is timelike"),
    "FMW": ("Flanagan, Marolf, Wald, hep-th/9908070",
            "We show that Bousso's entropy bound can be derived from either of two sets of hypotheses."),
    "BOUSSO_SAT": ("Bousso, Freivogel, Leichenauer, 1003.3012",
                   "The gravitational entropy of black holes saturates this inequality."),
    "GJW_HD": ("2011.13807 (Holographic teleportation in higher dimensions)",
               "this wormhole can be made traversable by a double trace deformation that violates the average null "
               "energy condition (ANEC) in the bulk"),
    "GJW_SHOCK": ("1906.10715 (Information transfer via traversable BTZ wormholes)",
                  "the negative energy shock wave is dual to the infinite boost limit of a specific double trace "
                  "deformation which couples the left and right CFTs"),
    "QNEC": ("Ceyhan, Faulkner, 1706.09432",
             "We prove a conjectured lower bound on < T--(x) >psi in any state psi of a relativistic QFT dubbed the "
             "Quantum Null Energy Condition (QNEC)."),
    "FR_NULL": ("Fewster, Roman, gr-qc/0209036",
                "weighted averages of the null-contracted stress-energy tensor along null geodesics are unbounded from "
                "below on the class of Hadamard states"),
    "RS_ENT": ("2302.13742 (How ubiquitous is entanglement in quantum field theory?)",
               "every Reeh-Schlieder state contains entanglement between any two spatially separated regions"),
    "RS_FINITE": ("2302.13742",
                  "We find that entanglement between finite-dimensional subsystems is not common at all"),
    "LP": ("Lehner, Pretorius, 1106.5184",
           "Since no fine-tuning is required to excite the instability, this constitutes a generic violation of cosmic "
           "censorship."),
    "GL_REV": ("2210.13501 (The endpoint of the Gregory-Laflamme instability of black strings revisited)",
               "The endpoint of the instability is the pinch off of the horizon in finite asymptotic time, thus "
               "confirming the violation of the weak cosmic censorship conjecture around black string spacetimes."),
    "CTH": ("1804.03912 (Closed trapping horizons without singularity)",
            "they necessarily violate the null energy condition up to I-, i.e. in a non-compact region of spacetime."),
    "AK": ("Ashtekar, Krishnan, Living Rev. Rel. 7 (2004) 10",
           "evolving black holes are modelled by dynamical horizons and black holes in equilibrium by isolated "
           "horizons"),
    "KOLM": ("Vitanyi, 2002.07674",
             "Formally, it is the length of a shortest program from which the file can be reconstructed. We discuss "
             "the incomputabilty of Kolmogorov complexity"),
    "ADAMS": ("Adams, 1902.03928",
              "For all of these issues, viable universes exist over a range of parameter space, which is delineated "
              "herein."),
    "ADAMS_AG": ("Adams, 1511.06958",
                 "viable universes --- with working stars and habitable planets --- can exist within a parameter space "
                 "where the structure constants alpha and alphaG vary by several orders of magnitude"),
    "BBCJPW": ("Bennett et al., Phys. Rev. Lett. 70, 1895 (1993)",
               "An unknown quantum state can be disassembled into, then later reconstructed from, purely classical "
               "information and purely nonclassical Einstein-Podolsky-Rosen (EPR) correlations."),
    "BOSCHI": ("Boschi et al., quant-ph/9710013",
               "We report on a quantum optical experimental implementation of teleportation of unknown pure quantum "
               "states."),
    "HARRIS": ("Harris, Kanti, hep-ph/0309054",
               "We demonstrate that this quantity varies considerably with n but always remains smaller than unity -- "
               "this provides firm support to earlier arguments made by Emparan, Horowitz and Myers."),
    "GW170817": ("LIGO-Virgo, Fermi, INTEGRAL, 1710.05834",
                 "constrain the difference between the speed of gravity and the speed of light to be between -3x10^-15 "
                 "and +7x10^-16 times the speed of light"),
    "EFT": ("Bjerrum-Bohr, Donoghue, Holstein et al., 0708.1701",
            "general relativity and its combination with scalar quantum electrodynamics (QED) as an effective quantum "
            "field theory at energies well below the Planck scale"),
    "LANDSCAPE": ("2303.17723 (The cosmological constant is probably still zero)",
                  "Four-form flux, quantised in units of the membrane charges, generically generates a landscape of "
                  "vacua with a range of values for the cosmological constant"),
    "WH_NATURAL": ("astro-ph/9409051 (Natural wormholes as gravitational lenses)",
                   "Visser has suggested traversable 3-dimensional wormholes that could plausibly form naturally "
                   "during Big Bang inflation."),
    "WH_UNSTABLE": ("Hayward, gr-qc/0306051",
                    "a numerical study of dynamical perturbations of the first Morris-Thorne wormhole showed it to be "
                    "unstable"),
    "ML": ("Margolus, Levitin, quant-ph/9710043 eq. 4 (READ in encode_read.py E5)",
           "an orthogonal state takes tau >= h/(4E) -- the least time of a change, set by its energy"),
    "HAYWARD": ("Hayward, gr-qc/9303006v3 Theorem 3 (READ in close_small.py K2)",
                "If the null energy condition holds, the area form of a future outer or past inner trapping horizon "
                "is non-decreasing"),
}

# A2: key -> (kind, the reading, sources, verdict, what remains or the finding)
READINGS = {
    "201": ("S", "B6': our universe defined by its plane's tension and its dark-energy offset",
            ["SMS", "BDEL", "GS_DS", "DS_IN_ADS", "DS_THICK", "MK_42", "ADEL", "KAPNER", "DUFF"], "EST",
            "as a consistent, realizable model agreeing with measurement (not derivable as true, flag (b)); remains: "
            "our sigma, offset and ell = 13.96 um meet SMS's relation with the measured G and Lambda (computed)"),
    "R0": ("S", "the read: the README the corridor's inflow at the opening; N read from the README",
           ["DG", "BBCJPW", "KOLM"], "PART",
           "a null radiation envelope forms the brane hole (DG); remains: the shell of E(N) forming the face "
           "(settle_arrival A2, A4) and N a computable function of the README (encode_labels)"),
    "R1": ("S", "exact reconstruction, no tolerance", ["BBCJPW", "BOSCHI"], "PART",
           "exact in principle from classical information and entanglement, the original destroyed (no-cloning "
           "kept); experiments fall short of exact; remains: the labels decode exactly (encode_labels)"),
    "R2": ("S", "position 2 builds an exact copy from its own bulk under its laws", ["ADAMS", "ADAMS_AG"], "PART",
           "structures exist over a range of the constants; remains: the copy's structures computed under each "
           "position 2's laws (p2_matter)"),
    "R6": ("S", "the room by displacement; the copy stays as the new whole", [], "ABSENT",
           "no physics claim beyond conservation; remains: the work of displacement inside the build's energy (E3)"),
    "437": ("S", "RECON: any information reconstructed to obey any position 2's 26", ["ADAMS", "ADAMS_AG"], "CONTRA",
            "finding: viable structure only over a bounded range of the constants (alphaG/alpha < 1e-34); RECON is "
            "provable inside the reconstructible region (433), not for every position 2"),
    "101": ("S", "a corridor at any size; the device sizes it to the README", ["KTN", "ACPY", "YOSHINO", "WC"], "EST",
            "holes on the plane exist from 5D Schwarzschild (small) to large static ones, and collapse forms them; "
            "Yoshino's non-existence reading is answered by the later constructions"),
    "110": ("S", "the closing energy goes into position 2", ["HR"], "PART",
            "the mass that collapses re-emerges from the white hole (HR); remains: the ledger across the passage "
            "(E3)"),
    "111": ("S", "the build uses exactly the closing energy", [], "ABSENT", "the ledger, computed (E3)"),
    "127": ("S", "the planes coincide in the extra dimension", ["GS_DS"], "PART",
            "coincident planes act as one plane of summed tension, with no radion (GS_DS for one positive plane); "
            "remains: the summed-tension junction (computed, STATIC S2)"),
    "275": ("S", "the planes coincident everywhere", ["GS_DS"], "PART", "as 127"),
    "131": ("S", "the throat sized by the README's shortest exact binary form", ["BOUSSO_SAT", "FMW", "KOLM"],
            "PART", "finding: the horizon holds A/4 (BOUSSO_SAT), but the shortest form is Kolmogorov's and "
            "uncomputable (KOLM); with ENCODE's fixed code, N is computable and the size follows"),
    "132": ("S", "the horizons hold the README; one way by nature", ["BOUSSO_SAT", "HR"], "PART",
            "a horizon saturates the entropy bound; one-way by its causal structure; remains: the README's N against "
            "the area (G1, computed)"),
    "133": ("S", "one exact energy for any given README", ["KTN", "ACPY"], "EST",
            "the hole's mass fixes its entropy one-to-one at both ends"),
    "136": ("S", "released at position 2 at the closing; one fixed exact encoding", ["HR"], "PART",
            "re-emergence from the white hole (HR); remains: the encoding fixed and exact (encode_labels)"),
    "137": ("S", "the passage's exact entanglement is N bits", ["BBCJPW", "BOUSSO_SAT"], "PART",
            "teleporting N qubits uses N EPR pairs; a horizon holds A/4; remains: N bits against the throat's area "
            "(I1, computed)"),
    "139": ("S", "position 2's plane negative, ours positive; the energy positive", ["SMS_NEG", "SMS"], "CONTRA",
            "finding: a negative-tension plane is an anti-gravity world (SMS_NEG) -- 139 (1)'s plane; 226, 229 and "
            "the destination's own values already moved off it; the positivity is computed (pointwise, b5b_wall)"),
    "146": ("S", "no tolerance; the encoding in what every universe shares", ["BBCJPW"], "PART", "as R1"),
    "147": ("S", "the copy's motion not in the README; labels and values", [], "ABSENT",
            "a choice of the device's, realizable by construction (encode_labels)"),
    "148": ("S", "position 2's matter rearranges to the README, then its laws govern", ["ADAMS"], "PART", "as R2"),
    "158": ("S", "the hold lasts as long as the write needs", ["ML"], "EST", "the least time exists (ML)"),
    "160": ("S", "the corridor and the opening one object", ["DG"], "PART",
            "a null shell forms the hole as it arrives; remains: the face from the opening (settle_arrival)"),
    "162": ("S", "one black-hole-like object of the README's size, at once", ["DG", "AK", "BGM", "GD", "WC"], "PART",
            "null-shell formation (DG); finding: a dust collapse on the plane has no static exterior (BGM), pressure "
            "allows one (GD), and the numerical collapse settles to the static hole (WC); remains: the size fixed "
            "through the write (computed)"),
    "163": ("S", "'at once' is all together, one whole", [], "ABSENT", "definitional"),
    "166": ("S", "the corridor spans both planes", ["HOR_BULK"], "PART",
            "the horizon extends into the bulk; remains: across both planes (computed)"),
    "179": ("S", "the corridor exclusive to the bulk", ["HOR_BULK"], "PART", "as 166"),
    "282": ("S", "re-posed one-way; B7's join through the bulk with no horizons", ["HOR_BULK"], "PART",
            "remains: B7 by the bulk's geometry (approved, 442 (3))"),
    "198": ("S", "the README forms the corridor", ["DG", "AK"], "PART", "as 160"),
    "340": ("S", "the README forms the face as it arrives", ["DG"], "PART", "as 160"),
    "200": ("S", "position 2's plane counted once", [], "ABSENT", "a counting choice; computed (b6_once)"),
    "226": ("S", "each position 2 carries its own values", ["SMS", "ADAMS"], "PART",
            "planes of any positive tension carry Einstein gravity; remains: per destination (computed)"),
    "229": ("S", "the destination a position 2 like 2a-2P", ["SMS"], "EST",
            "tension and offset not negative: within SMS's admissible planes"),
    "427": ("S", "a destination of any tension reachable", ["SMS_NEG"], "CONTRA",
            "finding: negative tension is an anti-gravity world (SMS_NEG); provable for sigma > 0"),
    "230": ("S", "the bulk does all the work; position 2 absorbs the energy read at position 1", [], "ABSENT",
            "the ledger (E3)"),
    "239": ("S", "the build's need is what the closing energy activates", [], "ABSENT", "the ledger (E3)"),
    "240": ("S", "the copy built under position 2's laws; its mass position 2's", ["ADAMS"], "PART", "as R2"),
    "285": ("S", "an exact copy obeying position 2's laws; the room the new whole", ["ADAMS"], "PART", "as R2, R6"),
    "284": ("S", "the room: the rebuilt content, displacing, staying", [], "ABSENT", "as R6"),
    "270": ("S", "the passage one-way only", ["HR", "SS_BOUNCE"], "PART",
            "black hole in, white hole out (HR); re-emergence into a second asymptotic region (SS_BOUNCE)"),
    "276": ("S", "the passage one-way in all aspects", ["HR"], "PART", "as 270"),
    "277": ("S", "the passage one-way only, again", ["HR"], "PART", "as 270"),
    "273": ("S", "the continuation a quantum bounce to position 2",
            ["HR", "HR_QG", "BCG", "BCG_SHORT", "SEMI", "SS_BOUNCE", "SS_TIMELIKE"], "PART",
            "flag (a): the exterior exact (HR), the transition quantum gravity (HR_QG); finding: long time scales "
            "pathologically unstable (BCG), short ones robust; a semiclassical route in 2D models (SEMI); a "
            "classical bounce on a brane whose extra dimension is timelike (SS_BOUNCE), not Randall-Sundrum's"),
    "336": ("S", "the energy stays in our universe; our face closes by Hawking emission", ["HARRIS", "HAYWARD"],
            "EST", "bulk-to-brane emissivity below one: the hole radiates mainly on the plane; the face can shrink "
                   "only where the null condition fails, as Hawking emission's does (HAYWARD)"),
    "386": ("S", "what crosses is information, not matter", ["BBCJPW", "BOSCHI"], "EST",
            "a state taken apart into classical information and entanglement and rebuilt, demonstrated"),
    "390": ("S", "position 2's face closes when the corridor holds nothing", ["HR", "BCG", "CTH"], "PART",
            "the white hole ends once it has emitted (HR); finding: closing a trapped region formed by null shells "
            "needs negative null energy out to infinity (CTH); remains: the face's end computed"),
    "426": ("S", "the write long; the object standing from the opening", ["ML", "DG"], "PART",
            "the least time (ML) and the face from the shell (DG); remains: computed (encode_read E5)"),
    "432": ("S", "the energy is the README, there at the opening; exact on a navigational lattice", [], "ABSENT",
            "a specification; its 'information is energy' part is not in the literature (101's answers 3-4 too)"),
    "438": ("S", "the geometry as labels; the isotope out, the last state in", [], "ABSENT",
            "a choice of the device's, realizable by construction (encode_labels)"),
    "86": ("N", "natural throats common and regular occurrences", ["WH_NATURAL", "WH_UNSTABLE"], "ABSENT",
           "speculated (WH_NATURAL), not observed; the Morris-Thorne throat unstable (WH_UNSTABLE)"),
    "100": ("N", "everything entangled with everything", ["RS_ENT", "RS_FINITE"], "PART",
            "established for regions of a field (Reeh-Schlieder); finding: not for finitely many modes (RS_FINITE)"),
    "109": ("N", "a horizon cannot exist without its object", ["AK", "CTH"], "PART",
            "trapping horizons evolve with their matter (AK); remains: the face's end with its content (computed)"),
    "122": ("N", "censorship binds the bulk; the two sides time-reversed images", ["LP", "GL_REV", "HR"], "CONTRA",
            "finding: five-dimensional black strings pinch to naked singularities, generically (LP, GL_REV); the "
            "time-reversed images hold (HR)"),
    "140": ("N", "k dependent on the work; position 2's plane entangled", [], "ABSENT", "not in the literature"),
    "155": ("N", "the rest of E absorbed by position 2's expansion", [], "ABSENT", "not in the literature"),
    "177": ("N", "negative null energy from coupling the entangled ends is the appearance", ["GJW_HD", "GJW_SHOCK"],
            "PART", "established in anti-de Sitter holography: a boundary coupling yields the bulk's negative null "
                    "energy; 'appearance' is the reading"),
    "183": ("N", "the null condition never violated, as a pair along each ray", ["QNEC", "FR_NULL"], "PART",
            "the averaged condition proved; finding: the local null energy is unbounded below (FR_NULL)"),
    "202": ("N", "every plane with our structure, perhaps different values", ["LANDSCAPE"], "PART",
            "landscapes of vacua with other values are proposed (LANDSCAPE), not established"),
    "320": ("N", "no bulk is ever empty", ["RS_ENT"], "PART",
            "the vacuum carries entanglement between regions (RS_ENT); a vacuum bulk carries no matter"),
    "328": ("C", "M-ONE-LIGHT-CONE: everything keeps the one light cone", ["GW170817"], "PART",
            "observed for gravity against light to 3e-15; beyond observation, relativity.py's computation"),
    "334": ("C", "H-HOLD-IS-THE-FACE: the hold is the face standing", [], "ABSENT", "a reading of the device's"),
    "353": ("C", "H-PLANCK-ENDS: regularity asked below the Planck curvature", ["EFT"], "EST",
            "general relativity an effective theory well below the Planck scale"),
}
VERDICTS = ("EST", "PART", "CONTRA", "ABSENT")


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def readings():
    r = dict(READINGS)
    if "drop" in MUT:
        r.pop("273")
    if "promote" in MUT:
        r["437"] = r["437"][:3] + ("EST",) + r["437"][4:]
    return r


def needed():
    """every S and N ruling the rows name (refound), the four definitions and the three confirmations"""
    rf = _load(os.path.join(HERE, "refound.py"), "pa_rf")
    R = rf.ruled()
    used = {n for ns in R.values() for n in ns if rf.KIND[n][0] in "SN"}
    return {str(n) for n in used} | {"R0", "R1", "R2", "R6", "328", "334", "353"}


def report():
    rd = readings()
    print("A0 M's words:", words())
    print("A1 %d sources READ" % len(SOURCES))
    cnt = collections.Counter(v[3] for v in rd.values())
    print("A2 %d readings: %s" % (len(rd), ", ".join("%s %d" % (k, cnt[k]) for k in VERDICTS)))
    for v in VERDICTS:
        print("  %s:" % v)
        for k, (kind, text, src, vd, rem) in rd.items():
            if vd == v:
                print("    %-5s %s  [%s]" % (k, text, ", ".join(src) or "-"))
                print("          %s" % rem)


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    rd = readings()
    r = words(); ok.append(r); say("A0 words: %s" % r)
    r = all(len(v) == 2 and v[0] and len(v[1]) > 30 for v in SOURCES.values()); ok.append(r)
    say("A1 every source with its identifier and a line read: %s" % r)
    need = needed()
    r = need <= set(rd); ok.append(r); say("A3 every needed reading has a verdict (%d needed): %s" % (len(need), r))
    cited = {s for v in rd.values() for s in v[2]}
    r = cited <= set(SOURCES); ok.append(r); say("A3 every cited source in A1: %s" % r)
    r = set(SOURCES) <= cited or "drop" in MUT; ok.append(r); say("A3 every source in A1 cited: %s" % r)
    r = all(v[3] in VERDICTS for v in rd.values()) and all(v[2] for v in rd.values() if v[3] in ("EST", "CONTRA"))
    ok.append(r); say("A3 every verdict valid, every EST and CONTRA cites a source: %s" % r)
    r = rd.get("437", ("",) * 4)[3] == "CONTRA" and rd["122"][3] == "CONTRA" and "flag (a)" in rd["273"][4]
    ok.append(r); say("A3 the findings stand: RECON and 122 contrary, 273 flagged: %s" % r)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    for m in ("drop", "promote"):
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-8s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/2 caught" % caught)
    return caught == 2


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
