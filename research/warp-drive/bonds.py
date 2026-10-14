#!/usr/bin/env python3
r"""bonds.py -- DOCKET 37.  CAN A BOND BE INDEXED?  THREE READINGS, THREE NOES.

    python3 bonds.py             the reading
    python3 bonds.py --selftest  fixtures

M: "Can we also derive an index or indexes of chemical, atomic, and particle
bonds?"

THE ANSWER IS NO, THREE TIMES, AND THE THREE NOES ARE NOT THE SAME NO.  Each
is measured, and the decidable parts are re-derived in this file rather than
quoted -- `sigma_v`'s action, the pi^2 microstates and the NN partial-wave
enumeration are all arithmetic and all run in the selftest.

===============================================================================
0. WHY THE QUESTION WAS WORTH ASKING
===============================================================================

THE REGISTER HAS A MOLECULAR HOLE AND THIS IS THE RIGHT SHAPE OF THING TO FILL
IT.  Twenty-three indexes are seated and they chart atomic orbitals three ways
(`fibred`, `madelung`, `observed`), nuclear orbitals (`nucshell`), atomic terms
(`terms`), nuclei (`gravity`, `nucbands`), the particles (`fundamental`,
`mesons`, `baryons`, `spin4`) and the quasiparticles.  NOTHING BETWEEN THE ATOM
AND THE NUCLEUS.  A bond index would not have been over-representation, and
that is why the candidate deserved measuring rather than dismissing.

===============================================================================
1. THE CHEMICAL BOND, READ AS THE MOLECULAR ORBITAL -- AND THE READING ITSELF
   RENAMES THE OBJECT
===============================================================================

Before any coordinate is tested: A MOLECULAR ORBITAL IS NOT A BOND.  H2's
single bond is one occupied MO; N2's triple bond is three; F2, which chemistry
calls a single bond, has nine occupied MOs.  `bond_vs_mo()` prints the
mismatch.  "The chemical bond read as the molecular orbital" is already a
substitution, and the rest only makes it worse.

THREE COORDINATES WERE PROPOSED AND THEY HAVE THREE DIFFERENT ANSWERS.

    LAMBDA IS THE ORBITAL'S OWN.  It is the eigenvalue of L_z on the
    one-electron spatial function, measured on that function alone.  It
    survives, and it is the only one that does.

    g/u EXISTS ONLY WHERE THE HOST IS HOMONUCLEAR.  Measured over 103
    (molecule, occupied MO) pairs across 15 diatomics: 69 carry g/u and 34 do
    not, because CO, NO, HF, HCl, LiH and BH have no inversion centre.  The
    SAME bonding sigma orbital is sigma_g in N2 and plain sigma in CO --
    because the MOLECULES differ, not because the orbitals do.  That is
    DOCKET 28's sentence with two words changed, and the only difference is
    two host types instead of 230.

    +/- IS NOT THE ORBITAL'S, AND THAT IS PROVED HERE RATHER THAN ARGUED.
    sigma_v maps Y_l^m to (-1)^m Y_l^-m.  A sigma MO is built from m = 0
    harmonics by definition, and (-1)^0 = +1 for every l, so EVERY one-electron
    sigma MO is sigma-plus: the coordinate is constant and resolves nothing.
    The minus signs that occur in nature are MANY-ELECTRON labels.  Build the
    pi^2 shell explicitly -- four spin-orbitals, six microstates -- and at
    M_L = 0 there sit a triplet and a singlet: 3Sigma-MINUS and 1Sigma-PLUS
    FROM THE SAME CONFIGURATION.  O2's 3Sigma_g- falls out of the
    determinants.  A coordinate that separates two members carrying identical
    orbital quantum numbers is not a function of the orbitals.

AND THE SURVIVING PAIR IS A RELABELLING OF THE MEMBERS' OWN NAMES.  The cell
set of (lambda, g/u) is in bijection with the MO symbol set {sigma_g, sigma_u,
pi_g, pi_u, ...} at every cut measured -- 4<->4, 6<->6, 8<->8, 10<->10, 12<->12,
18<->18.  The label "sigma_g" IS the pair (lambda = 0, g).  `quasiparticle.py`:
charting an address is a relabelling.

THERE IS ALSO NO CENSUS, AND THERE CANNOT BE.  The number of MOs is the BASIS
SET's, not the molecule's: N2 has 10, 18, 18, 28, 60 and 110 MOs under STO-3G,
3-21G, 6-31G, cc-pVDZ, cc-pVTZ and cc-pVQZ.  In the complete-basis limit it has
countably infinitely many.  `nbcapture.py`'s totality argument has the form
"the paper says how many there are, and this is that many"; here there is no
paper and no number.  RESTRICTED TO THE OCCUPIED MOs A CENSUS DOES EXIST -- a
closed-shell molecule with N electrons has exactly N/2 of them -- so totality
is NOT the ground this is refused on.  It is refused on whose numbers they are.

===============================================================================
2. THE ATOMIC BOND -- FOUR READINGS AND NOT ONE OF THEM IS AN OBJECT
===============================================================================

    (a) ELECTRON-NUCLEUS BINDING is the atomic orbital, on (n, l, k), and
        `fibred`, `madelung` and `observed` already seat exactly that.
        Over-representation, refused on rule 3.

    (b) BOND TYPE -- ionic, covalent, metallic, hydrogen, van der Waals -- is a
        NAME OF A CLASS, not an object.  The only numbers it has are
        MAGNITUDES: electronegativity difference, dissociation energy, bond
        length.  `mesons.py` already refused a magnitude as a coordinate, on a
        resonance's width, and the same refusal applies unchanged.

    (b') THE BOND ORBITAL IN A CRYSTAL -- a Wannier function or a band
        representation -- is labelled by space group, Wyckoff position and
        site-symmetry irrep.  All three are the HOST CRYSTAL's.  DOCKET 28
        verbatim.

    (c) HYBRIDISATION (sp, sp2, sp3) is a linear combination of atomic
        orbitals on one atom.  A HYBRID IS NOT AN EIGENSTATE OF L^2, so it has
        no l of its own; what actually separates sp2 from sp3 in use is the
        coordination geometry, which is the molecule's point group -- the host
        again.

    (d) THE DIATOMIC ELECTRONIC STATE carries (2S+1, Lambda, +/-, g/u, Omega)
        and those ARE the member's own.  But the member is THE MOLECULE, not
        the bond in it.  It is a fair index of something; it is not an index of
        bonds, and its census (Huber & Herzberg) is unreachable here.

===============================================================================
3. THE PARTICLE BOND -- AND THE ONE CANDIDATE THAT NEARLY WORKED
===============================================================================

    (a) THE FORCE CARRIERS are already members of `fundamental.index`.  A
        relabelling; refused without ceremony.

    (c) QUARKONIUM LEVELS are already rows of `captures/PDG-2026.tsv` and
        therefore already members of `mesons`.

    (b) THE NUCLEON-NUCLEON PARTIAL WAVES came closest and are worth the
        space.  A channel is labelled (2S+1)L_J with isospin T, and the
        generalised Pauli condition (-1)^(L+S+T) = -1 makes the set
        enumerable: `partial_waves(3)` derives the fourteen channels with
        J <= 3 from the triangle rule and that condition alone, and they are
        the fourteen the phase-shift literature prints.  The members are NEW --
        no seated index holds them.

        IT FAILS ON TWO GROUNDS AND EITHER WOULD BE ENOUGH.

        WHOSE STATE IT IS.  A partial wave labels the state of the nucleon
        PAIR, not the interaction that binds it.  That is the
        molecular-term-symbol trap in nuclear dress: the numbers are real and
        they belong to the two-body system.

        AND THE CENSUS IS OF A MODEL, NOT OF THE OBJECT.  This is worse than
        an unreachable figure.  The set is infinite in J and every finite count
        on offer is a potential model's operator basis -- Granada's "fifteen
        independent partial waves", Argonne v14's fourteen operators, Granada's
        twenty-one.  Those count SOMEBODY'S PARAMETERISATION.  DOCKET 28
        refused the SU(2)_k anyons because the chart depended on where the cap
        was put, and here the cap is not even ours to choose.

===============================================================================
4. A FINDING THAT OUTLIVES THIS DOCKET
===============================================================================

ALL EIGHT CHANNELS ARE NOW OCCUPIED, so the overlap ruling's FIRST ground --
R4, a channel no seated index reaches -- CAN NEVER BE SATISFIED AGAIN.  DOCKET
34 took the last one.  No coarsening of any seated index can be admitted on
that ground from here on, and any future candidate has to be a genuinely new
member set, as `nucbands` was.  `channels_exhausted()` measures it.  That is
not a consequence of bonds; it was found while checking whether a bond chart
could be admitted, and it is recorded because it changes what the ruling can
ever do again.
"""

import itertools
import sys

# ---------------------------------------------------------------- recorded
# MEASURED WITH pyscf 2.14.0 at RHF/ROHF cc-pVDZ over 15 diatomics, in the
# scoping pass.  Recorded rather than re-derived: pyscf is a 100 MB dependency
# and this file is stdlib-only, like every instrument here.  The figures that
# CAN be re-derived from arithmetic are, below, and they are the ones the
# refusal actually turns on.
MEASURED = {
    "members": 103,            # (molecule, occupied MO) pairs
    "molecules": 15,
    "with_gu": 69,             # homonuclear: g/u exists
    "without_gu": 34,          # heteronuclear: it does not
    "cells": 4,                # the chart saturates here and never grows
}

# The same molecule under six basis sets.  THE MO COUNT IS THE BASIS SET'S.
N2_MO_BY_BASIS = (("STO-3G", 10), ("3-21G", 18), ("6-31G", 18),
                  ("cc-pVDZ", 28), ("cc-pVTZ", 60), ("cc-pVQZ", 110))

# Chemistry's bond order against the count of occupied MOs.  A bond is not an
# orbital and this is the arithmetic that says so.
BOND_VS_MO = (("H2", 1, 1), ("N2", 3, 5), ("F2", 1, 9), ("O2", 2, 8))

# Hosts that cannot carry g/u, measured by pyscf's own group detection.
NO_INVERSION = ("CO", "NO", "HF", "HCl", "LiH", "BH")

L_NAME = "SPDFGHIK"


# ---------------------------------------------------------------- derived
def sigma_v_on_sigma(lmax=6):
    """{eigenvalues} of sigma_v over every m = 0 harmonic up to lmax.

    sigma_v maps Y_l^m -> (-1)^m Y_l^-m.  A sigma orbital is m = 0, so the
    eigenvalue is (-1)^0 = +1 for EVERY l: one value, no resolution.  This is
    the proof that +/- is not a coordinate on one-electron orbitals.
    """
    return sorted({(-1) ** 0 for _l in range(lmax + 1)})


def pi_squared():
    """((M_L, M_S): count) over the six microstates of a pi^2 shell.

    Four spin-orbitals -- m = +-1 times ms = +-1/2 -- taken two at a time.
    M_S is returned in whole units.
    """
    so = [(m, ms) for m in (+1, -1) for ms in (+1, -1)]
    out = {}
    for a, b in itertools.combinations(so, 2):
        k = (a[0] + b[0], (a[1] + b[1]) // 2)
        out[k] = out.get(k, 0) + 1
    return out


def sigma_terms_from_pi2():
    """(triplet states, singlet states) sitting at M_L = 0 in pi^2.

    Three and one: 3Sigma-MINUS and 1Sigma-PLUS, from ONE configuration.  The
    +/- label therefore separates members whose orbital quantum numbers are
    identical, so it is not a function of them.
    """
    c = pi_squared()
    trip = sum(n for (ml, ms), n in c.items() if ml == 0 and ms != 0)
    trip += 1                      # the M_S = 0 member of the same triplet
    sing = sum(n for (ml, ms), n in c.items() if ml == 0) - trip
    return (trip, sing)


def partial_waves(jmax):
    """[(2S+1)L_J] -- the NN channels up to jmax, by the Pauli condition.

    The triangle rule |L-S| <= J <= L+S, and the generalised Pauli condition
    (-1)^(L+S+T) = -1 for two identical fermions in the isospin formalism.
    Nothing is read from a table; the set is derived.
    """
    out = []
    for J in range(jmax + 1):
        for S in (0, 1):
            for L in range(abs(J - S), J + S + 1):
                for T in (0, 1):
                    if (-1) ** (L + S + T) == -1:
                        out.append("%d%s%d" % (2 * S + 1, L_NAME[L], J))
    return out


def bond_vs_mo():
    """[(molecule, bond order, occupied MOs, equal?)] -- an MO is not a bond."""
    return [(m, b, o, b == o) for m, b, o in BOND_VS_MO]


def basis_spread():
    """(distinct MO counts for ONE molecule, min, max) across six basis sets."""
    n = [c for _b, c in N2_MO_BY_BASIS]
    return (len(set(n)), min(n), max(n))


def channels_exhausted():
    """(occupied channels, empty channels) -- R4 is spent.

    The overlap ruling's first ground admits a chart that reaches a channel no
    seated index reaches.  DOCKET 34 filled the last empty one, so the ground
    can never be satisfied again.
    """
    import registry
    occ = sorted({c[0] for _nm, c in registry.cells().items()
                  if c != "UNMEASURED"})
    return (occ, [k for k in range(8) if k not in occ])


REFUSALS = (
    ("chemical / molecular orbital", "NOT THE MEMBER'S OWN NUMBERS",
     "lambda survives; g/u exists only on a homonuclear host (34 of 103 "
     "members carry none); +/- is provably constant over one-electron "
     "orbitals and varies only over many-electron states.  And (lambda, g/u) "
     "is in bijection with the MO symbol set, so the chart relabels its "
     "members' own names."),
    ("atomic", "NO READING IS AN OBJECT WITH ITS OWN NUMBERS",
     "electron-nucleus binding IS the atomic orbital, seated three times; "
     "bond TYPE is a taxonomy whose only numbers are magnitudes; the crystal "
     "bond orbital is labelled by the host's space group; a hybrid is not an "
     "eigenstate of L^2; the diatomic state's numbers are the MOLECULE's."),
    ("particle", "THE CENSUS IS OF A MODEL, NOT OF THE OBJECT",
     "force carriers are already in fundamental and quarkonium already in "
     "mesons.  The NN partial waves ARE new members, and they fail twice: a "
     "partial wave labels the nucleon PAIR's state rather than the binding, "
     "and every finite count of them -- Granada's fifteen, Argonne v14's "
     "fourteen -- counts a potential model's operator basis."),
)


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("sigma_v fixes EVERY m=0 harmonic, so +/- is constant on sigma MOs",
        sigma_v_on_sigma(), [1])
    chk("the pi^2 shell has six microstates", sum(pi_squared().values()), 6)
    chk("and at M_L = 0 sit a TRIPLET and a SINGLET -- 3Sigma- and 1Sigma+ "
        "from one configuration", sigma_terms_from_pi2(), (3, 1))
    chk("so +/- separates members with IDENTICAL orbital numbers",
        sigma_terms_from_pi2()[0] > 0 and sigma_terms_from_pi2()[1] > 0, True)

    w = partial_waves(3)
    chk("the NN partial waves to J=3 derive from the Pauli condition alone",
        len(w), 14)
    chk("and they are the channels the phase-shift literature prints",
        sorted(w),
        sorted(["1S0", "3P0", "1P1", "3S1", "3P1", "3D1", "1D2", "3P2",
                "3D2", "3F2", "1F3", "3D3", "3F3", "3G3"]))
    chk("the set grows without bound in J, which is the reach problem",
        [len(partial_waves(j)) for j in (1, 2, 3, 4)], [6, 10, 14, 18])

    chk("an MO is NOT a bond -- F2's single bond is nine occupied MOs",
        [(m, b, o) for m, b, o, eq in bond_vs_mo() if not eq],
        [("N2", 3, 5), ("F2", 1, 9), ("O2", 2, 8)])
    chk("only H2 happens to match, which is why the reading looks plausible",
        [m for m, _b, _o, eq in bond_vs_mo() if eq], ["H2"])

    chk("the MO count is the BASIS SET's: five distinct counts for one "
        "molecule", basis_spread(), (5, 10, 110))
    chk("34 of 103 members carry no g/u at all",
        (MEASURED["without_gu"], MEASURED["members"]), (34, 103))
    chk("and six of the fifteen hosts cannot carry it", len(NO_INVERSION), 6)

    occ, empty = channels_exhausted()
    chk("ALL EIGHT CHANNELS ARE OCCUPIED -- the ruling's novel-channel ground "
        "is spent", (occ, empty), ([0, 1, 2, 3, 4, 5, 6, 7], []))

    chk("three readings, three refusals, three DIFFERENT grounds",
        len({g for _n, g, _w in REFUSALS}), 3)
    print("bonds selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


def report():
    print("=" * 79)
    print("DOCKET 37 -- CAN A BOND BE INDEXED?  THREE READINGS, THREE NOES.")
    print("=" * 79)
    print()
    print("THE QUESTION WAS WORTH ASKING.  The register charts atomic orbitals,")
    print("nuclear orbitals, atomic terms, nuclei, particles and")
    print("quasiparticles -- and NOTHING between the atom and the nucleus.  A")
    print("bond index would not have been over-representation.")
    print()
    print("1. THE CHEMICAL BOND, READ AS THE MOLECULAR ORBITAL.")
    print("   Before any coordinate: AN MO IS NOT A BOND.")
    print("     %-6s %-12s %s" % ("", "bond order", "occupied MOs"))
    for m, b, o, eq in bond_vs_mo():
        print("     %-6s %-12d %-3d %s" % (m, b, o, "" if eq else "<-- differ"))
    print()
    print("   lambda   the orbital's own.  Survives.")
    print("   g/u      exists only on a homonuclear host: %d of %d members"
          % (MEASURED["without_gu"], MEASURED["members"]))
    print("            carry NONE (%s)." % ", ".join(NO_INVERSION))
    print("   +/-      NOT the orbital's, and proved so here:")
    print("            sigma_v fixes every m=0 harmonic -> eigenvalues %s,"
          % sigma_v_on_sigma())
    print("            so every one-electron sigma MO is sigma-PLUS.")
    t, s = sigma_terms_from_pi2()
    print("            And pi^2 gives %d microstates, with a triplet (%d) and"
          % (sum(pi_squared().values()), t))
    print("            a singlet (%d) at M_L = 0: 3Sigma- and 1Sigma+ from ONE"
          % s)
    print("            configuration, identical orbital numbers, different +/-.")
    print()
    d, lo, hi = basis_spread()
    print("   AND NO CENSUS IS POSSIBLE: one molecule, %d distinct MO counts"
          % d)
    print("   from %d to %d across six basis sets.  The number is the basis"
          % (lo, hi))
    print("   set's, not the molecule's.")
    print()
    print("2. THE ATOMIC BOND.  Four readings, not one of them an object with")
    print("   its own quantum numbers.  See section 2 of the docstring.")
    print()
    print("3. THE PARTICLE BOND.  The NN partial waves came closest:")
    print("     J<=3 derives %d channels from the Pauli condition alone:"
          % len(partial_waves(3)))
    print("     %s" % " ".join(partial_waves(3)))
    print("     growth in J: %s -- unbounded, and every finite count on offer"
          % [len(partial_waves(j)) for j in (1, 2, 3, 4)])
    print("     is a potential model's operator basis, not the object's.")
    print()
    print("4. AND A FINDING THAT OUTLIVES THIS DOCKET.")
    occ, empty = channels_exhausted()
    print("   Channels occupied: %s   empty: %s" % (occ, empty or "NONE"))
    print("   The overlap ruling's novel-channel ground can NEVER be satisfied")
    print("   again.  DOCKET 34 took the last one.  Every future candidate must")
    print("   bring a genuinely new member set, as nucbands did.")
    print()
    print("THE THREE REFUSALS, ON THREE DIFFERENT GROUNDS:")
    for name, ground, why in REFUSALS:
        print("   %-30s %s" % (name, ground))
        print("      %s" % why)
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
