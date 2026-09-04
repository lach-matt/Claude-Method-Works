#!/usr/bin/env python3
"""params.py -- Lambda_phys, the index of physical parameters.

Register 1238. The Physics Compendium states the interface between a quantity and
the index that holds it. What it did not hold is the PARAMETERS themselves: the
constants, the read tables, the fitted numbers, and for each one its provenance,
its uncertainty and its domain of validity.

That is an index in its own right. Its coordinates:

    kind        what sort of number it is        0 exact .. 4 fitted
    source      where the value comes from       0 defined .. 3 this work
    domain      how wide its validity is         0 universal .. 3 one species
    depends     how many objects rest on it      binned

A parameter that is EXACT by definition, DEFINED as its own source, UNIVERSAL in
domain and carried by many objects sits at one corner. A number fitted here, from
this work, valid in one region, carried by one object sits at the other. The
question the index answers is whether the work's dependence on measured input is
CONCENTRATED or SPREAD -- and where it would break first.
"""
import math
from itertools import product

# kind: 0 exact by definition, 1 measured constant, 2 read from a table,
#       3 derived here from measurements, 4 fitted here
# src:  0 mathematics, 1 international standard, 2 published literature, 3 this work
# dom:  0 universal, 1 all elements, 2 a region of the index, 3 one species
# fails: where the value stops being right -- stated, not implied
# name, symbol, value, kind, src, dom, nobj, DEFINITION, provenance, where it fails
P = [
 ("Rydberg constant", "R_inf", "109737.31568 cm^-1", 1, 1, 0, 9,
  "the binding energy of a hypothetical one-electron atom with an infinitely heavy "
  "nucleus, expressed as a wavenumber. It sets the scale of every atomic term value.",
  "Rydberg, K. Sven. Vetensk. Akad. Handl. 23 (1890) for the empirical constant; "
  "value CODATA 2018, uncertainty 1.9e-6 cm^-1 -- eleven significant figures",
  "never as a constant; but using it in place of the reduced-mass R_M is wrong for "
  "every species (register 868). The error is 1 part in 1836 A, largest at hydrogen."),
 ("proton-electron mass ratio", "m_p/m_e", "1836.15267343", 1, 1, 0, 9,
  "the ratio of the proton rest mass to the electron rest mass; the quantity that "
  "makes the reduced-mass correction small but not negligible.",
  "CODATA 2018, uncertainty 1.1e-10",
  "never; it enters only through R_M, so an error here is an error there."),
 ("reduced-mass Rydberg", "R_M", "R_inf/(1 + 1/(A m_p))", 3, 1, 1, 9,
  "the Rydberg constant corrected for a nucleus of finite mass A, by replacing the "
  "electron mass with the electron-nucleus reduced mass.",
  "Bohr 1913: after Fowler objected that the Pickering series did not fit, Bohr "
  "replaced the electron mass with the reduced mass and obtained five-digit "
  "agreement, which identified the series as ionised helium. Bohr, Nature 95 (1915) "
  "6-7 for his later comment.",
  "for an ion of unknown isotopic composition: A is the dominant isotope, and a "
  "mixed sample shifts R_M by roughly the isotope shift."),
 ("subshell capacity", "4l+2", "exact integer", 0, 2, 0, 12,
  "the number of electrons a subshell of angular momentum l can hold: 2 spin states "
  "times 2l+1 orbital states.",
  "Stoner, The distribution of electrons among atomic levels, Phil. Mag. 48 (1924) "
  "719-736; made exclusive by Pauli, Z. Phys. 31 (1925) 765-783",
  "for parastatistics of order m the capacity is m(4l+2) -- T.para shows the index "
  "still closes, so the constraint is a cap and not a magic number."),
 ("angular momentum bound", "l <= n-1", "exact integer", 0, 2, 0, 12,
  "the orbital angular momentum of a bound state cannot reach the principal quantum "
  "number; it is the condition for the radial function to have a node structure.",
  "Bohr, Phil. Mag. 26 (1913) 1-25; Schroedinger, Ann. Phys. 79 (1926) 361-376",
  "never within non-relativistic quantum mechanics."),
 ("aufbau ordering", "n+l, then n", "a permutation of subshells", 2, 2, 1, 19,
  "the order in which subshells fill as Z increases: lowest n+l first, and within "
  "one n+l value, lowest n first.",
  "Janet 1928 (Considerations sur la structure du noyau de l'atome, Beauvais 1929), "
  "who recognised it before Madelung 1936; shell lengths by the Klechkovski-Hakala "
  "formulas",
  "at about twenty known exceptions among the elements -- Cr, Cu, Nb, Mo, Ru, Rh, "
  "Pd, Ag, La, Ce, Gd, Pt, Au, Ac, Th, Pa, U, Np, Cm, Lr. The compendium reads the "
  "OBSERVED configuration, so the exceptions are data and not failures. AND the "
  "rule's ORIGIN is unresolved: Loewdin's challenge, Allen & Knight, Int. J. Quantum "
  "Chem. 90 (2003) 80-88."),
 ("Hund's first rule", "max S for the core", "a term selection", 2, 2, 1, 12,
  "of the terms a configuration allows, the one of highest total spin lies lowest in "
  "energy; it fixes which multiplicities a core can present.",
  "Hund, Z. Phys. 33 (1925) 345-371",
  "for a core in an excited term rather than its ground term. The index takes the "
  "ground term, so an excited-core series is outside it."),
 ("Janet block boundary", "Z = 21, 57, 89", "exact integer", 2, 2, 1, 15,
  "the atomic number at which a new n+l block opens -- n+l = 5 at Sc, 7 at La, 8 at "
  "Ac -- which is where the corresponding orbital contracts into the core.",
  "the block structure is Janet 1928; the CONTRACTION is Goeppert-Mayer, Phys. Rev. "
  "60 (1941) 184-187, and Griffin, Andrew & Cowan, Phys. Rev. 177 (1969) 62-71",
  "as a SHARP threshold: collapse is rapid, not instantaneous. Ca I at Z = 20 has "
  "nd = 0.908 against a threshold of 21, and Ba II at 56 has nf = 0.756 against 57."),
 ("ionisation limit", "I", "per species, cm^-1", 2, 2, 3, 25,
  "the energy at which a Rydberg series converges -- the term value of the ion's "
  "ground state relative to the neutral. Every defect is measured against it.",
  "the extrapolation method is Rydberg 1890 and Ritz, Ann. Phys. 12 (1903) 264-310; "
  "values from NIST ASD where published, built by summing two spectra where not "
  "(P.buildlimit), joint-fit where neither",
  "wherever it was CONSTRUCTED rather than published -- such a channel is not a "
  "measurement against an independent standard, and the compendium marks the column."),
 ("core dipole polarisability", "alpha_d", "per core, a0^3", 2, 2, 2, 10,
  "the induced dipole moment of the ionic core per unit applied field; the leading "
  "term in the potential a distant electron feels beyond the Coulomb tail.",
  "Born & Heisenberg, Z. Phys. 23 (1924) 388-410; systematic values Mayer & Mayer, "
  "Phys. Rev. 43 (1933) 605-611; modern e.g. Cs+ 15.696(16) a0^3, arXiv:2502.20961",
  "below l = 4, where penetration dominates and Seaton's formula does not apply. "
  "AND for nf treated as non-penetrating: arXiv:2502.20961 reports alpha_d and "
  "alpha_q that then disagree with the ng energies."),
 ("Seaton polarisation constant", "3 alpha c^2 / K(l)", "derived", 3, 2, 2, 10,
  "the limiting quantum defect of a non-penetrating series, set by the core's "
  "polarisability and the centrifugal factor K(l) = l(l+1)(2l-1)(2l+1)(2l+3).",
  "Seaton, MNRAS 118 (1958) 504-518; Drake & Swainson, Phys. Rev. A 44 (1991) 5448",
  "at l < 4, and wherever the quadrupole term matters. The compendium measures the "
  "ratio delta_2/delta_0 against -l(l+1)/3 at 1.25 rather than 1.00."),
 ("channel equation, a", "0.3772", "fitted", 4, 3, 2, 8,
  "the overall amplitude of the penetrating branch: how much defect one core orbital "
  "of the same l produces at unit electron count and unit charge.",
  "fitted here by least squares on 277 in-region channels plus 7 far anchors; the "
  "FORM it scales is the penetration picture of Hartree, Proc. Camb. Phil. Soc. 24 "
  "(1928) 89-110",
  "outside Z <= 92, charge <= 10, l <= 4, single-parent core."),
 ("channel equation, e0", "0.8297", "fitted", 4, 3, 2, 8,
  "the intercept of the exponent on the core-orbital count p -- how sharply the "
  "defect grows with the number of same-l orbitals in the core, at small Ne.",
  "fitted here; the p-count itself is the Pauli occupancy (Pauli 1925)",
  "as above. Its value moved from 0.583 to 0.830 when the far anchors were added, "
  "so it is sensitive to the high-Z end."),
 ("channel equation, e1", "-0.0900", "fitted", 4, 3, 2, 8,
  "the log-Ne slope of that exponent: the rate at which additional core orbitals "
  "stop mattering as the atom grows.",
  "fitted here; that screening saturates with electron count is the Thomas-Fermi "
  "picture of Fermi, Z. Phys. 48 (1928) 73-79",
  "as above; it was -0.027 before the anchors, a factor of three."),
 ("channel equation, k", "0.4942", "fitted", 4, 3, 2, 8,
  "the Thomas-Fermi exponent: how the defect scales with the number of electrons in "
  "the core, through the screening the statistical model predicts.",
  "fitted here; the scaling is Fermi, Z. Phys. 48 (1928) 73-79, who applied the "
  "statistical model to Rydberg corrections directly",
  "MEASURABLY: k rises with charge, from 0.84 at charge 1 to 1.52 at charge 4 "
  "(register 1214). A single value is a simplification and the register says so."),
 ("channel equation, h", "0.5415", "fitted", 4, 3, 2, 8,
  "the amplitude of the collapse branch: how much defect a collapsed orbital "
  "produces where the core has no orbitals of its own l.",
  "fitted here; the collapse is Goeppert-Mayer 1941 and Griffin, Andrew & Cowan 1969",
  "below the Janet boundary, where the polarisation floor is absent."),
 ("exchange coefficient", "s = -0.0782", "fitted, WITHDRAWN", 4, 3, 3, 1,
  "the fractional difference between a triplet channel's defect and its singlet "
  "partner's, from the exchange interaction between the Rydberg electron and the core.",
  "fitted at register 987, WITHDRAWN at 1168; the physics is Heisenberg, Z. Phys. 38 "
  "(1926) 411-426, with Hund's first rule (1925)",
  "everywhere: the fitted sign is opposite to the measured one, and a uniform s "
  "gives 0 of 66 pairs or 66 of 66."),
 ("isoelectronic ladder, B", "per sequence", "fitted", 4, 3, 2, 3,
  "the single free coefficient of delta(c) = B ln(c+1)/c along a sequence of fixed "
  "electron count, with the constant term fixed at zero by the hydrogenic edge.",
  "fitted here per sequence on the 52 with three or more charge states; the "
  "isoelectronic method is Edlen, Handbuch der Physik XXVII (1964) 80-220",
  "as a CLOSED FORM: no expression of B in the coordinates beats the per-sequence "
  "fit by less than a factor of twenty, and PMC3671562 reports the same for "
  "ionisation energies."),
 ("actinide defects", "5.2, 4.75, 3.8, 2.0", "theoretical", 2, 2, 2, 2,
  "the asymptotic ns, np, nd and nf quantum defects predicted for the actinides, "
  "Z = 89-103; the compendium's only high-Z anchors.",
  "arXiv:2508.06733 (2025), theoretical",
  "as MEASUREMENTS -- they are calculated. Four of the seven far anchors are these, "
  "and the equation's high-Z arm moves if they are revised (register 1202)."),
 ("Cs I np defect", "3.5667", "measured", 1, 2, 3, 2,
  "the limiting quantum defect of the caesium np series, the compendium's only "
  "MEASURED far anchor.",
  "arXiv:1706.06237 (2017), n = 70-100; earlier 3.55925 at n = 9-50 (Lorenzen & "
  "Niemax, Z. Phys. A 315, 1984)",
  "the two values differ by 0.007 because of stray-field shifts; the compendium "
  "uses the field-free one."),
 ("five-sigma admissibility", "r >= 5", "a threshold", 4, 3, 1, 3,
  "the bracket is applied only where the signal exceeds five times the measurement "
  "uncertainty, so that a bracket failure is a fact about the levels and not noise.",
  "the convention is particle physics's; its history and its critics are in Lyons, "
  "Discovering the significance of 5 sigma, arXiv:1310.1284 (2013)",
  "it is a CHOICE. At three sigma more cells enter and more brackets fail; the "
  "compendium states the threshold rather than tuning it."),
 ("bracket yardstick", "2 Z^2 R / nu^3", "derived", 3, 2, 1, 4,
  "the local spacing between adjacent Rydberg levels -- the derivative of the term "
  "formula. A perturbation larger than half of it reorders the levels.",
  "derived from Rydberg's term formula (1890)",
  "for a PERTURBED series, where a level of another channel crosses in. Fano, Phys. "
  "Rev. 124 (1961) 1866-1878; Lu & Fano, Phys. Rev. A 2 (1970) 81-86."),
]

def op_R(X, d):
    X=set(X); vals=[sorted({c[i] for c in X}) for i in range(d)]
    def env(i,j):
        m={}
        for c in X: m[c[j]]=max(m.get(c[j],-10**9), c[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals)
            if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}

def nbin(n):
    return 0 if n<=2 else 1 if n<=5 else 2 if n<=10 else 3

CELLS = {(p[3], p[4], p[5], nbin(p[6])) for p in P}
R = op_R(CELLS, 4)
BOX = 1
for i in range(4):
    BOX *= len({c[i] for c in CELLS})

if __name__ == "__main__":
    print(f"  Lambda_phys: {len(P)} parameters, {len(CELLS)} distinct cells")
    print(f"  |R(X)| = {len(R)}   E = {len(R)-len(CELLS)}   box = {BOX}")
    from collections import Counter
    K=["exact by definition","measured constant","read from a table",
       "derived here","fitted here"]
    S=["mathematics","international standard","published literature","this work"]
    D=["universal","all elements","a region","one species"]
    for lab,idx,names in (("kind",3,K),("source",4,S),("domain",5,D)):
        c=Counter(p[idx] for p in P)
        print(f"  {lab:<8}" + " · ".join(f"{names[k]} {v}" for k,v in sorted(c.items())))
