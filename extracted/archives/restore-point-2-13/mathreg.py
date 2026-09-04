#!/usr/bin/env python3
"""mathreg.py -- the register of mathematical objects across the corpus.

The corpus is The Method 1.6 (664 KB) and Transitions v3.0 (118 KB). 1,110
source lines carry a relation symbol; those are lines, not objects. This is the
inventory of DISTINCT objects, each with its hypotheses, its provenance, its
dependencies and whether it is checkable from the construction.

Fields
  id        stable key, used by the dependency graph
  stmt      the expression, expanded -- no symbol left undefined here
  hyp       the conditions under which it holds
  dep       ids this object is derived from or presupposes
  src       where it is stated
  grade     PROVED | COMPUTED | CITED | DEFINITIONAL | OPEN | ASSERTED
  check     name of the verification, or None if not checkable from cells alone
  named     the standing name in the literature, or None if unnamed
"""

REG = {}
def R(id, stmt, hyp, dep, src, grade, check=None, named=None):
    REG[id] = dict(id=id, stmt=stmt, hyp=hyp, dep=dep, src=src,
                   grade=grade, check=check, named=named)


# ================================================ 0. THE SPECTRAL MECHANISMS
# Fifteen mechanisms the Spectra Compendium's own measurements exposed. None is
# quoted from the literature and none is encoded in channels.py, which is given a
# configuration string, a Z and a limit and divides. Counts are measured against
# the compendium at 354 channels (registers 673-759).
R("P.qdt", "the quantum defect measures how far a Rydberg orbital reaches into the ionic core",
  "a Rydberg series with three or more members, or two with a published limit",
  [], "R 693, 707, 713; Seaton 1958, 1983", "MEASURED",
  check="four independent confirmations, none encoded  PRIOR ART: quantum defect theory — Seaton, The quantum defect method, MNRAS 118 (1958) 504-518, and Quantum defect theory, Rep. Prog. Phys. 46 (1983) 167-257.",
  named="core penetration")
R("P.lcollapse", "delta falls monotonically with l and reaches zero by f",
  "unperturbed series", ["P.qdt"], "R 693, 702, 713, 724; Hartree 1928; Seaton 1958", "MEASURED",
  check="229 of 230 adjacent-l pairs correct, judged against EACH PAIR'S OWN 2 sigma rather than a fixed tolerance. The test carried an unstated slack of 0.02 until R 1072; at a fixed 0.02 it reads 251/251, strictly 242/251. The one failure is He I p->d, whose p defect is NEGATIVE — the Appendix B omission of R 871, which could not be recomputed when the reduced-mass Rydberg was corrected (R 1072-1074)  PRIOR ART: the defect falls with l because the centrifugal barrier keeps the electron out of the core — the standard penetration argument, Hartree, Proc. Camb. Phil. Soc. 24 (1928) 89, and Seaton (1958).",
  named="the l-collapse")
R("P.polar", "beyond l=3 the defect follows core POLARISABILITY in direction, not in magnitude",
  "l >= 4, where the orbital does not reach the core", ["P.lcollapse"],
  "R 731-733, 788, 792-795; Born & Heisenberg 1924; Seaton 1958", "MEASURED",
  check="grows with Z at +0.0005/unit over seven elements; a quantitative alpha_d fit was attempted and did NOT work, cause undiagnosed (R 794)  PRIOR ART: core polarisation as the source of the high-l defect is Born & Heisenberg, Ueber den Einfluss der Deformierbarkeit der Ionen auf optische und chemische Konstanten, Z. Phys. 23 (1924) 388-410, and Mayer & Mayer, Phys. Rev. 43 (1933) 605.",
  named="core polarisation")
R("P.iso", "for one element and l, delta falls as the core charge rises",
  "defect large enough to exceed its own scatter", ["P.qdt"], "R 708, 716, 717, 718", "MEASURED",
  check="8 of 9 s/p ladders exact; and a form delta = a + b*ln(c+1)/c fits the Mg-like ns ladders to 2% of range and predicts out-of-sample, but FAILS on nd, nf and all He-like ladders (47-65%); the method is Edlen 1964 (R 942-945)",
  named="the isoelectronic ladder")
R("P.dcollapse", "an orbital collapses at the onset of its shell and leaves the Rydberg series",
  "3d across the transition row, 4f across the lanthanides", ["P.iso"],
  "R 719, 734, 735, 736; Goeppert-Mayer 1941; Griffin, Andrew & Cowan 1969", "MEASURED",
  check="all ten P.iso exceptions are d and small; Ba III 4f gives 1.0 against neon's 0.006  PRIOR ART: orbital collapse at the onset of a shell — Goeppert-Mayer, Phys. Rev. 60 (1941) 184-187; Griffin, Andrew & Cowan, Phys. Rev. 177 (1969) 62-71.",
  named="orbital collapse")
R("P.coreblind", "delta depends on l and the core's charge, not on the core's STATE",
  "two parent terms of one species", ["P.qdt"], "R 709, 710, 743; Seaton 1958", "MEASURED",
  check="TWO instances; and CONTRADICTED IN PRINCIPLE by MQDT, which defines the defect as mu_(l,lambda,alpha+) depending on the core state (R 947)  PRIOR ART: single-channel quantum defect theory treats the core as a fixed phase shift, so delta depends on l and the core charge only. Its failure for multi-channel cases is Seaton MQDT (Rep. Prog. Phys. 46, 1983).",
  named="parent-term independence")
R("P.jsplit", "delta splits by the outer electron's own j when there is something to couple to",
  "an OPEN-SHELL core, or Z large enough for the electron's spin-orbit",
  ["P.qdt"], "R 754, 756, 757, 758, 759; Sommerfeld 1916", "MEASURED",
  check="median 0.0454 over 19 open/heavy pairs against 0.0002 over 10 closed/light — 227x  PRIOR ART: fine-structure splitting of a term by J is Sommerfeld, Zur Quantentheorie der Spektrallinien, Ann. Phys. 51 (1916) 1-94, in its relativistic form; Dirac (1928) supplies the exact theory.",
  named="the j-splitting")
R("P.charge", "at s and p the quantum defect falls with charge at FIXED ELEMENT",
  "a fixed element with two or more charge states", ["P.qdt"], "R 963; Edlen 1964", "MEASURED",
  check="37 of 37 monotone at l<=1, no exceptions; all nine failures are at l>=2 where P.dcollapse governs  PRIOR ART: the fall of the defect with ionisation stage along an isonuclear sequence is standard spectroscopy — Edlen, Atomic spectra, Handbuch der Physik XXVII (1964) 80-220.",
  named="the same-element ladder")
R("P.jj", "J-inconsistency within one series marks where LS coupling has failed",
  "same series, different J", ["P.qdt"], "R 703; Condon & Shortley 1935", "MEASURED",
  check="114 of 129 consistent on raw levels, interval 82-93%; heavy elements fail at 23% against light at 8% (R 818-819)  PRIOR ART: the transition from LS to jj coupling as the spin-orbit interaction grows with Z is Condon & Shortley, The Theory of Atomic Spectra (1935), ch. X.",
  named="the coupling-scheme marker")
R("P.perturb", "a large spread measures a perturber, not bad data",
  "a state of the same symmetry crossing the series", ["P.qdt"],
  "R 696, 704, 741, 742; Fano 1961; Lu & Fano 1970", "MEASURED",
  check="Si I nd spreads 0.15-0.21 where ASD's own leading-percentage column names 3s3p3 at 14%  PRIOR ART: a perturbed Rydberg series is a series crossed by a level of another channel — Fano, Effects of configuration interaction on intensities and phase shifts, Phys. Rev. 124 (1961) 1866-1878; Lu & Fano, Graphic analysis of perturbed Rydberg series, Phys. Rev. A 2 (1970) 81-86.",
  named="series perturbation")
R("P.mono", "the defect approaches delta_0 monotonically: PENETRATION series fall, POLARISATION series rise",
  "steps resolvable against their own uncertainty", ["P.qdt"], "R 806, 821-824; NIST Atomic Spectroscopy compendium; Ritz 1903", "MEASURED",
  check="penetration (|d|>=0.1) falls 146 of 163 = 92%; polarisation (|d|<0.01) RISES 52 of 52 = 100%; combined 94% against 66% as a single claim (R 985-987)  PRIOR ART: the extended Ritz formula has a positive second coefficient for penetration and a negative one for polarisation, so the approach to delta_0 is monotone from above or below. Stated in NIST compendium.",
  named="the monotonicity of the defect")
R("P.selfsame", "one series in disjoint n windows gives one defect",
  "windows where P.lens's amplification is comparable", ["P.qdt"], "R 747, 748, 751; Ritz 1903", "MEASURED",
  check="67 of 72 channels agree between disjoint halves to better than 0.05 (R 811)  PRIOR ART: one unperturbed series has one defect; disjoint n-windows must agree. The consistency test of the Ritz form (1903).",
  named="series self-consistency")
R("P.lens", "near the limit delta is measured through a lens worsening as n^3",
  "delta depends on (limit - E), which shrinks as n^2 while level error does not",
  ["P.qdt"], "R 749, 750, 751, 752; Rydberg 1890", "MEASURED",
  check="WEAK at scale: only 44 of 79 channels show a wider high half (56%), and the n^3 prediction of 4.2x is observed at 1.3x (R 827)  PRIOR ART: near the limit dT/dnu ~ nu^-3, so a fixed energy uncertainty maps to a defect uncertainty growing as nu^3. Direct from the term formula.",
  named="the precision lens")
R("P.trunc", "truncation removes most channels and degrades those it leaves",
  "a series cut at low n", [], "R 675, 676, 677, 705, 706; Inglis & Teller 1939", "MEASURED",
  check="Ne I: 33 Handbook levels give 0 channels, the full table gives 4  PRIOR ART: a Rydberg series is truncated in practice by field ionisation and by plasma microfields — Inglis & Teller, Ionic depression of series limits in one-electron spectra, Astrophys. J. 90 (1939) 439-448.",
  named="truncation loss")
R("P.converge", "a Rydberg series measures its own ionisation limit",
  "enough members that the fit is determined", ["P.qdt"],
  "R 684, 685, 686, 698, 699; Rydberg 1890; Ritz 1903", "MEASURED",
  check="38 of 58 put the published limit within 3x the fit own error; only 15 of 58 within the PUBLISHED error (R 812-813)  PRIOR ART: extrapolating a Rydberg series to its limit is the classical method of determining an ionisation energy — Rydberg (1890), Ritz (1903).",
  named="self-determined limit")
R("P.buildlimit", "a limit can be built from two spectra and tested by convergence",
  "a series converging on a state above its own ionisation threshold",
  ["P.converge", "P.lcollapse"], "R 711, 712; Edlen 1964", "MEASURED",
  check="Ne I 2s.2p6.np on 173,929.75 + 217,047.598 gives +0.8408 +/- 0.0191 over ten  PRIOR ART: constructing a limit by summing the ionisation energies of successive stages is standard spectroscopic practice. Edlen, Handbuch der Physik XXVII (1964).",
  named="constructed limit")
R("P.termsplit", "at l=3 delta splits by the core's TERM while its J-pairs stay together",
  "j-K coupled series on one core", ["P.qdt"], "R 739; Condon & Shortley 1935", "MEASURED",
  check="12 of 15 groups have terms separating by more than their J-pairs — median within 0.0011 vs between 0.0462 (R 826)  PRIOR ART: the splitting of a Rydberg series by the core term, with J-pairs staying together, is the parent-term structure of Condon & Shortley (1935), ch. VII.",
  named="core angular structure")

# ============================================================ I. THE OPERATOR
R("A.alph", "Â_i(X) = { x_i : x ∈ X }",
  "X a finite set of integer tuples", [], "M §6.1 / T A1; Codd 1970", "DEFINITIONAL",
  check="PRIOR ART: projection onto a coordinate is the relational projection operator — Codd, A relational model of data for large shared data banks, CACM 13 (1970) 377-387.",
  named="projection onto coordinate i")
R("A.env", "φ̂_ij(v) = max{ x_i : x ∈ X, x_j ≤ v }; max ∅ = −∞",
  "i ≠ j", ["A.alph"], "M §6.1 / T A2; Deville et al. 1999", "DEFINITIONAL",
  check="PRIOR ART: the monotone upper envelope of a relation is its staircase bound — the connected row-convex class of Deville, Barette & Van Hentenryck (1999) and the row-convex networks of van Beek & Dechter, J. ACM 42 (1995) 543-561.",
  named="monotone upper envelope / staircase bound")
R("A.R", "ℛ(X) = { x ∈ ∏_i Â_i(X) : x_i ≤ φ̂_ij(x_j) ∀ i≠j }",
  "none beyond A.alph, A.env", ["A.alph", "A.env"], "M §6.1 / T A3; Moore 1910; Deville et al. 1999", "DEFINITIONAL",
  check="PRIOR ART: R is a closure operator (Moore 1910) whose constraints are monotone staircases (Deville, Barette & Van Hentenryck, Artif. Intell. 109 (1999) 243-271). Neither the operator form nor the constraint class is new; what is new is reading E as a defect.",
  named="the recovery operator")
R("A.E", "E(X) = |ℛ(X)| − |X|",
  "none", ["A.R"], "M §6.1 / T A4; Moore 1910", "DEFINITIONAL", check="PRIOR ART: the gap between a set and its closure. That it is worth naming as a DEFECT is the books move; the quantity is the closure minus the set.",
  named="closure defect")
R("A.ext", "X ⊆ ℛ(X), hence E(X) ≥ 0",
  "none", ["A.R"], "T 1.2 / M A.2; Moore 1910", "PROVED", check="PRIOR ART: extensivity is the first Moore axiom. That E(X) >= 0 is its immediate corollary, not a separate result.",
  named="extensivity")
R("A.clos", "ℛ is extensive, monotone, idempotent; the closed sets form a Moore family",
  "none", ["A.ext"], "M §14.2 / T 1.3; Moore 1910; Ward 1942", "PROVED",
  check="PRIOR ART: an extensive, monotone, idempotent operator is a CLOSURE OPERATOR and its fixed sets form a Moore family — E. H. Moore, Introduction to a Form of General Analysis (1910); M. Ward, The closure operators of a lattice, Ann. Math. 43 (1942) 191-196. R is one; nothing about R is needed to know its fixed sets are closed under intersection.", named="closure operator (Moore family)")
R("A.fix", "X is closed ⟺ X = ℛ(X)",
  "each coordinate presented as a chain", ["A.clos"], "M §14.1 (Thm 9.1, A.2); Moore 1910; Baker & Pixley 1975",
  "PROVED", check="PRIOR ART: X closed iff X = R(X) is the definition of a fixed point of a closure operator. That the binary projections suffice is Baker & Pixley, Polynomial interpolation and the Chinese remainder theorem for algebraic systems, Math. Z. 143 (1975) 165-174 — the majority-term / (2,d) interpolation theorem.",
  named="Bergman double-projection; Baker–Pixley 1975 (majority term)")
R("A.bpc", "X ⊆ BPC(X) ⊆ ℛ(X), BPC(X) = { x : (x_i,x_j) ∈ proj_ij(X) ∀ i<j }",
  "none", ["A.R"], "T A5; Cooper 1989; Janssen et al. 1989", "PROVED", check="PRIOR ART: binary path consistency and its relation to global consistency — Cooper, An optimal k-consistency algorithm, Artif. Intell. 41 (1989) 89-95; Janssen, Jegou, Nouguier & Vilarem, A filtering process for general constraint-satisfaction problems, IEEE (1989), which gives a polynomial algorithm for pairwise consistency.",
  named="binary path consistency / 2-decomposability (Kimura et al. 2024)")
R("A.gc", "E(X) = 0 ⟺ the binary constraint network is globally consistent",
  "the constraints are the monotone binary projections", ["A.bpc", "A.E"],
  "T 1.4 / A5c; Freuder 1978; Dechter 1992", "CITED", named="global consistency (CSP)", check="A.gc  PRIOR ART: global consistency and its k-consistency ladder — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966; Dechter, From local to global consistency, Artif. Intell. 55 (1992) 87-107.")
R("A.freuder", "a tree-structured constraint network is globally consistent after arc consistency",
  "constraint graph acyclic", ["A.gc"], "T 1.10; Freuder 1982", "CITED", named="Freuder 1982", check="PRIOR ART: Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982) 24-32 — a tree-structured constraint network is globally consistent after arc consistency. This is the reason Lambda closes, and it is his.")
R("A.montanari", "for monotone constraints, path consistency implies global consistency",
  "constraints monotone", ["A.gc"], "T 1.10; Montanari 1974", "CITED", named="Montanari 1974", check="PRIOR ART: Montanari, Networks of constraints: fundamental properties and applications to picture processing, Inf. Sci. 7 (1974) 95-132 — for monotone constraints, path consistency implies global consistency. Lambda constraints are monotone, so this applies directly.")
R("A.rule", "a tightening preserves E = 0 iff it binds one coordinate by a monotone function of one other",
  "the index is a sublattice of a product of chains", ["A.fix"], "T 1.8 / M §14.4; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999; van Beek & Dechter 1995",
  "COMPUTED", check="PRIOR ART: a tightening preserves closure iff it stays inside the monotone staircase class.  PRIOR ART: a tightening preserves closure exactly when it stays inside the monotone staircase class — the connected row-convex constraints of Deville, Barette & Van Hentenryck, Constraint satisfaction over connected row-convex constraints, Artif. Intell. 109 (1999) 243-271, and the row-convex networks of van Beek & Dechter, On the minimality and global consistency of row-convex constraint networks, J. ACM 42 (1995) 543-561. Binding one coordinate by a monotone function of one other is precisely a member of that class.",
  named="the tightening rule")
R("A.morph", "an occupancy coordinate's cap is admissible iff it is a morphism for the operation preserved",
  "meet-morphism preserves meets; join-morphism preserves joins",
  ["A.rule"], "M §18.4.1; Birkhoff 1940", "COMPUTED", check="PRIOR ART: a cap is admissible iff it is a lattice morphism for the operation — the standard homomorphism condition. Birkhoff, Lattice Theory (1940).",
  named="the cap as a morphism")
R("A.modeA", "sub-case A, ORDERING: the term is present and determined but non-monotone; repairable by re-ordering",
  "the term is a function of an existing coordinate", ["A.rule"], "T 1.6; Freuder 1978",
  "COMPUTED", check="PRIOR ART: a non-monotone constraint is not captured by an envelope, and higher consistency is needed — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966.",
  named="failure mode A — ordering")
R("A.modeB", "sub-case B, ARITY: every term is monotone; the constraint names more coordinates than an envelope has arguments; not repairable by any operation on coordinates",
  "the minimal failing support has size ≥ 3", ["A.rule"], "T 1.6; Freuder 1978",
  "COMPUTED", check="PRIOR ART: a constraint naming more coordinates than the envelope pairs is a higher-arity constraint; the k-consistency ladder is Freuder (1978).",
  named="failure mode B — arity")
R("A.derived", "a derived coordinate cannot repair closure: the box grows by its value count and |X| is fixed",
  "the coordinate is a function of the others", ["A.E"], "T 1.7 / M §17.2 Thm 10.1; Birkhoff 1940",
  "PROVED", check="PRIOR ART: a derived coordinate is a function of the others, so it adds no join-irreducibles and cannot enlarge the closed family; it only enlarges the ambient box.", named="adjunction never repairs (M Thm 10.1)")
R("A.dens", "E = 0 is informative at any density; E > 0 at low density measures sparsity",
  "density = |X| / |box|", ["A.E"], "T 1.9; Erdos & Renyi 1960", "COMPUTED", check="PRIOR ART: that a structural property can hold at any density, while its failure measures sparsity, is the random-graph threshold picture of Erdos & Renyi, On the evolution of random graphs, Publ. Math. Inst. Hung. Acad. Sci. 5 (1960) 17-61.",
  named="density and informativeness")
R("A.bound", "0 ≤ E(X) ≤ |box| − |X|",
  "box = ∏_i |Â_i(X)|", ["A.E", "A.ext"], "T audit 27; Moore 1910", "PROVED",
  check="PRIOR ART: the bounds are extensivity below and the ambient product above; both follow from the closure axioms.",
  named="the defect bounds")
R("A.prod", "if no constraint links the factors, ℛ(A×B) = ℛ(A)×ℛ(B)",
  "A, B on disjoint coordinate sets, no cross constraint", ["A.R"], "T D9; Birkhoff 1940",
  "PROVED", check="PRIOR ART: a closure operator on a product with no cross-constraints factorises; the statement is the product form of a Moore family. Birkhoff, Lattice Theory (1940).",
  named="the product rule for closure")
R("A.prodE", "E(A×B) = |A|·E_B + |B|·E_A + E_A·E_B",
  "as A.prod", ["A.prod", "A.E"], "T D10; classical; classical; Euler 1748", "PROVED", check="PRIOR ART: the defect of a product expands as |A|E_B + |B|E_A + E_A E_B — the inclusion-exclusion expansion of (|A|+E_A)(|B|+E_B) minus |A||B|. Elementary.  PRIOR ART: expanding (|A| + E_A)(|B| + E_B) - |A||B| gives the three terms. Elementary algebra; the point is that defects MULTIPLY as well as add across a product.  PRIOR ART: expanding (|A| + E_A)(|B| + E_B) - |A||B| gives the three terms. The point is that defects MULTIPLY as well as add across a product, which is the elementary product rule for counting — Euler, Introductio in analysin infinitorum (1748), ch. XVI.",
  named="the product rule for the defect")
R("A.ebits", "E_bits(X) = log₂ C(|ℛ(X)|, E(X))",
  "counting measure", ["A.E"], "M §25.3; Shannon 1948; Rissanen 1978", "COMPUTED", check="PRIOR ART: description length as a measure of structure — Shannon, A mathematical theory of communication, Bell Syst. Tech. J. 27 (1948); Rissanen, Modeling by shortest data description, Automatica 14 (1978) 465-471. log2 C(|R|, E) is the cost of naming which admitted cells are absent.",
  named="description length")
R("A.slack", "SLACK(S) = measure(ambient)/measure(S); log SLACK = log|ℛ(X)| − log|X|",
  "a measure on the ambient", ["A.E", "A.ebits"], "M §25.2; Shannon 1948", "COMPUTED",
  check="PRIOR ART: log of the ratio of ambient to actual is a bit count — the same quantity as A.ebits in another form. Shannon (1948).",
  named="slack")

# ======================================================= II. THE LATTICE Λ₈
R("L.c1", "ℓ ≤ n − 1", "hydrogenic radial solution", [], "M §7.1; Bohr 1913; Schroedinger 1926", "CITED",
  named="node counting", check="PRIOR ART: l <= n-1 is the angular-momentum constraint of the hydrogen solution — Bohr, On the constitution of atoms and molecules, Phil. Mag. 26 (1913) 1-25; Schroedinger, Quantisierung als Eigenwertproblem, Ann. Phys. 79 (1926) 361-376.")
R("L.c2", "k ≤ 2(2ℓ+1) = 4ℓ+2", "Pauli exclusion", [], "M §7.1; Pauli 1925; Stoner 1924", "CITED", named="Pauli", check="PRIOR ART: the subshell capacity 2(2l+1) is Stoner, The distribution of electrons among atomic levels, Phil. Mag. 48 (1924) 719-736, made exclusive by Pauli, Z. Phys. 31 (1925) 765-783.")
R("L.c3", "q ≤ k", "counting", [], "M §7.1; Pauli 1925", "DEFINITIONAL", named="the transfer bound", check="PRIOR ART: q <= k, a transferred count cannot exceed the occupancy. Pauli (1925).")
R("L.c4", "f ≤ e − 1", "hydrogenic radial solution", [], "M §7.1; Bohr 1913", "CITED", named="node counting", check="PRIOR ART: as L.c1, applied to the second shell pair.")
R("L.c5", "g ≤ 4f+2", "Pauli exclusion", [], "M §7.1; Stoner 1924; Pauli 1925", "CITED", named="Pauli", check="PRIOR ART: as L.c2, applied to the second shell pair.")
R("L.c6", "g ≤ q", "counting", [], "M §7.1; Pauli 1925", "DEFINITIONAL", named="the second transfer bound", check="PRIOR ART: g <= q, as L.c3 on the second shell pair.")
R("L.c7", "2S ≤ k", "vector coupling on the source", [], "M §7.1; Hund 1925; Pauli 1925", "CITED", named="vector coupling", check="PRIOR ART: 2S <= k because at most k electrons can align their spins — Pauli exclusion (1925) with Hund first rule, Z. Phys. 33 (1925) 345-371.")
R("L.c8", "k ≥ 1 (definitional restriction, not a bound)",
  "a cell is a transition, not a state", [], "M §10.2, reg. 301; Pauli 1925", "DEFINITIONAL", named="the occupancy floor", check="PRIOR ART: k >= 1 restricts to occupied subshells; definitional rather than a bound.")
R("L.def", "Λ = { (n,ℓ,k,q,e,f,g,2S) ∈ ℤ⁸ : L.c1..L.c8 }, caps (n,e,ℓ,k,f) = (3,3,1,3,1)",
  "caps stated; figures at other caps must say so (§7.4)",
  ["L.c1","L.c2","L.c3","L.c4","L.c5","L.c6","L.c7","L.c8"], "M §7; Bohr 1913; Pauli 1925", "DEFINITIONAL",
  check="PRIOR ART: the eight constraints are the shell-structure rules of Bohr (1913) and Pauli (1925), written as inequalities on integer coordinates.", named="the definition of Lambda")
R("L.closed", "Λ is closed under coordinatewise ∨ and ∧",
  "every constraint of the form x_i ≤ φ(x_j) with φ non-decreasing",
  ["L.def","A.rule"], "M §7.3; Birkhoff 1940", "PROVED", check="PRIOR ART: closure under coordinatewise join and meet is the definition of a sublattice of a product (Birkhoff, Lattice Theory, 1940). What makes Lambda one is that all eight constraints have the form x_i <= f(x_j) with f monotone.",
  named="sublattice of a product")

R("L.E0", "E(Λ) = 0",
  "at the stated caps; verified at four settings and through the f shell",
  ["L.closed","A.E"], "M §7.3, reg. 236; Moore 1910; Freuder 1982", "COMPUTED", check="PRIOR ART: E = 0 says the index equals its own closure. Moore (1910) for the operator; Freuder (1982) for why a tree-structured constraint graph gives it.",
  named="the closure theorem")

R("L.dist", "Λ is distributive (a sublattice of a product of chains)",
  "none", ["L.closed"], "M §8.1; Birkhoff 1937", "PROVED", check="PRIOR ART: a lattice is distributive iff it embeds in a product of chains (Birkhoff, Rings of sets, Duke Math. J. 3, 1937). Lambda is such a sublattice by construction, so distributivity is INHERITED, not proved here.",
  named="Birkhoff / product of chains")
R("L.modular", "rank(a∨b) + rank(a∧b) = rank(a) + rank(b), rank = Σx_i",
  "graded lattice", ["L.dist"], "M §8.2; Dedekind 1900", "COMPUTED", check="PRIOR ART: the modular rank identity holds in any modular lattice and every distributive lattice is modular. Dedekind, Math. Ann. 53 (1900).",
  named="modularity (equality, not submodularity)")
R("L.birk", "Λ ≅ down-sets of J(Λ); |J(Λ)| = 17, 20 covering relations",
  "Λ finite distributive", ["L.dist"], "M §8.3; Birkhoff 1937", "COMPUTED", check="PRIOR ART: Birkhoff's representation theorem, Duke Math. J. 3 (1937) — every finite distributive lattice is the down-sets of its join-irreducibles. |J| = 17 is a computation inside that theorem.",
  named="Birkhoff representation 1937")
R("L.alpha", "|J(Λ)| = Σ_i (|A_i| − 1)",
  "each generator is min{x ∈ Λ : x_c ≥ v} for one coordinate and one value",
  ["L.birk"], "M reg. 268; Birkhoff 1937", "COMPUTED", check="PRIOR ART: the join-irreducibles of a product of chains are the coordinate steps, so |J| = sum(|A_i| - 1). Immediate from Birkhoff representation.",
  named="the join-irreducible count")
R("L.sperner", "the largest antichain equals the largest rank level; max 122 at rank 11",
  "rank sequence log-concave hence unimodal", ["L.dist"], "M §8.4; Sperner 1928; Stanley 1980", "COMPUTED",
  check="PRIOR ART: Sperner 1928 for the Boolean lattice; Stanley, Weyl groups, the hard Lefschetz theorem, and the Sperner property, SIAM J. Alg. Disc. Meth. 1 (1980) 168-184, proves the order-ideal lattice of a product of chains is Peck — rank-symmetric, rank-unimodal, strongly Sperner. Lambda is of that form, so the property is INHERITED.", named="Sperner property / Dilworth")
R("L.skew", "centre of mass 11.0666 vs midpoint 11.5, skew −0.43; only 8 of 976 cells fixed by x ↦ max − x",
  "at the stated caps", ["L.def"], "M §8.4; Gauss 1809", "COMPUTED", check="PRIOR ART: the third standardised moment of a rank distribution. Gauss (1809).",
  named="the rank skew")

R("L.dim", "order dimension of Λ₈ is 8, rising by one per adjoined axis",
  "at the stated caps", ["L.def"], "M §8.6; Dushnik & Miller 1941", "PROVED", check="PRIOR ART: Dushnik & Miller, Partially ordered sets, Amer. J. Math. 63 (1941) 600-610. That a product of n chains has dimension n follows from the definition; what is measured here is that Lambda's dimension equals its coordinate count at every stage of the tower.",
  named="order dimension (Dushnik–Miller)")

R("L.arith", "N(x) = ∏_i p_i^{x_i}; x≤y ⟺ N(x)|N(y); ∨↦lcm, ∧↦gcd, rank ↦ Ω(N)",
  "p_i the i-th prime", ["L.def"], "M §9; Birkhoff 1937", "COMPUTED", check="PRIOR ART: the divisor lattice with lcm as join and gcd as meet is the classical arithmetic model of a product of chains. Birkhoff, Lattice Theory (1940), ch. II.",
  named="divisor lattice embedding")
R("L.omega", "ω(N(x)) ≤ dim(Λ)", "one prime per coordinate", ["L.arith","L.dim"],
  "M §9.1; Birkhoff 1937", "PROVED", check="PRIOR ART: in the divisor representation, the number of distinct primes dividing N(x) is the number of coordinates in which x is non-minimal, bounded by the dimension.",
  named="distinct-prime-counting function")
R("L.occ", "d(x,y) = τ( lcm(N(x),N(y)) / gcd(N(x),N(y)) ) = ∏_i(|x_i−y_i|+1) = |[x∧y, x∨y]|",
  "τ the divisor count; d(x,x)=1", ["L.arith"], "M §9.2; Monjardet 1981", "COMPUTED",
  check="PRIOR ART: the interval size as a product of coordinate spans, and its arithmetic form via lcm and gcd. Monjardet, Metrics on partially ordered sets, Discrete Math. 35 (1981) 173-184.",
  named="the interval measure")
R("L.metric", "log d is an ℓ¹ metric; d(x,z) ≤ d(x,y)·d(y,z)",
  "as L.occ", ["L.occ"], "M §9.2; Monjardet 1981", "COMPUTED", check="PRIOR ART: Monjardet, Metrics on partially ordered sets - a survey, Discrete Math. 35 (1981) 173-184.",
  named="the lattice metric")
R("L.mobius", "μ(x,y) = (−1)^{|y∖x|} if y∖x is an antichain in J(Λ), else 0",
  "Λ ≅ J(P)", ["L.birk"], "M §9.3; Rota 1964", "COMPUTED", check="PRIOR ART: Rota, On the foundations of combinatorial theory I: theory of Moebius functions, Z. Wahrscheinlichkeitstheorie 2 (1964) 340-368. The antichain form of mu on a distributive lattice is his.",
  named="Möbius function of a distributive lattice")
R("L.void", "void(x,y) = ∏_i(|Δ_i|+1) − |[x∧y, x∨y] ∩ Λ|",
  "none", ["L.occ"], "M §10; Rota 1964", "DEFINITIONAL", check="PRIOR ART: the difference between a box count and the cells it actually contains is what Moebius inversion would compute. Rota (1964).", named="the void")
R("L.voidfrac", "void-free fraction 27.7–30.1% across 776M pairs; joint 30.13% vs product 20.19%, factor 1.49",
  "at stated caps", ["L.void"], "M §10.2; Rota 1964", "COMPUTED", check="PRIOR ART: as L.void; the fraction is the measurement.",
  named="the void-free fraction")

R("L.box", "|box ∩ Λ| factorises because the constraint graph is a tree; no Möbius sieve needed",
  "constraint graph acyclic", ["L.tree"], "M §10.4; Freuder 1982; Rota 1964", "COMPUTED", check="PRIOR ART: the count factorises over a tree — no Moebius sieve is needed because there are no cycles to inclusion-exclude over. Freuder (1982) for the tree property; Rota (1964) for what the sieve would otherwise cost.",
  named="the box factorises")

R("L.tree", "constraint graph n—ℓ—k—q—g—f—e with 2S pendant at k: 8 nodes, 7 edges, a caterpillar; treewidth 1",
  "every constraint binds exactly two coordinates",
  ["L.def"], "M §8.5, §11.4; Freuder 1982", "COMPUTED", check="PRIOR ART: that a constraint graph is a tree, and what follows from it, is Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982) 24-32.", named="the constraint tree")
R("L.F", "F = Σ_n z₁ⁿ Σ_{ℓ≤n−1} z₂^ℓ Σ_{k≤4ℓ+2} z₃^k [Σ_{S≤k} z₈^S] Σ_{q≤k} z₄^q Σ_e z₅^e Σ_{f<e} z₆^f Σ_{g≤min(q,4f+2)} z₇^g",
  "at stated caps; the tree has no cycles so the sum factorises",
  ["L.tree","L.def"], "M §11.3; Euler 1748; Stanley 1986", "COMPUTED", check="PRIOR ART: a multivariate generating function over a constrained region, written as nested sums. Euler, Introductio (1748); Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 1.",
  named="the generating function")

R("L.F1", "F(1,…,1) = |Λ| = 976", "as L.F", ["L.F"], "M §11; Euler 1748; Euler 1748; Stanley 1986", "COMPUTED", check="PRIOR ART: setting all variables to one recovers the cardinality — the elementary specialisation of a generating function.  PRIOR ART: F(1,...,1) = |X| is the elementary specialisation of a generating function. Euler, Introductio (1748), ch. XVI; Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 1.",
  named="the cardinality")

R("L.rankpoly", "F(z) = z³(z¹⁷ + 4z¹⁶ + 10z¹⁵ + … + 122z⁸ + 121z⁷ + … + 5z + 1); F′(1)/F(1) = 11.0666",
  "single-variable specialisation", ["L.F"], "M §11.1; Stanley 1986", "COMPUTED", check="PRIOR ART: Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 3. F'(1)/F(1) = mean rank is the standard first-moment identity.",
  named="the rank polynomial")

R("L.Fm1", "F(−1) = 2, because ℓ and f each have exactly two consecutive values but are coupled to n and e",
  "at stated caps", ["L.rankpoly"], "M §11.8.1; Euler 1748; Euler 1748; Stanley 1986", "COMPUTED", check="PRIOR ART: F(-1) counts the difference between even- and odd-rank cells; the standard alternating specialisation.  PRIOR ART: F(-1) is the difference between even- and odd-rank counts, the standard alternating specialisation. Euler (1748); Stanley (1986), ch. 3, where it is related to rank symmetry.",
  named="the alternating specialisation")

R("L.pal", "F palindromic ⟺ the poset is self-dual; Λ's F is not palindromic",
  "graded poset", ["L.rankpoly","L.skew"], "M §11.8; Stanley 1986", "PROVED", check="PRIOR ART: Stanley, Enumerative Combinatorics Vol. 1, ch. 3 — a graded poset's rank polynomial is palindromic iff it is rank-symmetric.",
  named="palindromic rank polynomial ⟺ self-dual")
R("L.chi", "χ(x) = H(n−1−ℓ)H(4ℓ+2−k)H(k−q)H(k−2S)H(e−1−f)H(4f+2−g)H(q−g); the coefficient function of F is χ",
  "H the Heaviside step", ["L.F","L.def"], "M §11.1; Heaviside 1893", "COMPUTED", check="PRIOR ART: the membership function as a product of step functions — Heaviside, Electromagnetic Theory (1893), where the unit step is introduced.",
  named="the membership function")

R("L.total", "χ_Λ : ∏A_i → {0,1} is total: membership decided for every ambient point",
  "Λ a finite intersection of decidable comparisons", ["L.chi"], "M §16.5; Birkhoff 1940", "PROVED",
  check="PRIOR ART: a membership function defined by inequalities on coordinates is total on the ambient product by construction.",
  named="the membership function is total")

R("L.bits", "Λ is the 976 words in {0,1}¹⁷ that are down-sets of J(Λ); join = OR, meet = AND; 17 bits carried, 9.93 needed, 7.07 surplus",
  "Birkhoff correspondence", ["L.birk"], "M §11.1.1; Birkhoff 1937; Shannon 1938", "COMPUTED", check="PRIOR ART: Birkhoff (1937) gives the down-set representation; encoding down-sets as Boolean words with OR as join and AND as meet is Shannon (1938).",
  named="the Boolean representation")

R("L.circuit", "the 20 covering relations, as implications, cut 2¹⁷ = 131,072 words to exactly 976, at depth 5",
  "monotone: AND, OR, implication; no NOT, no feedback", ["L.bits"], "M §11.1.1; Shannon 1938",
  "COMPUTED", check="PRIOR ART: implications as a monotone Boolean circuit — Shannon, A symbolic analysis of relay and switching circuits, Trans. AIEE 57 (1938) 713-723.", named="the implication circuit")
R("L.chains", "maximal chains of Λ = linear extensions of J(Λ) = 1,113,045,672",
  "Λ ≅ J(P)", ["L.birk"], "M §12.9; Stanley 1986", "COMPUTED", check="PRIOR ART: maximal chains of J(P) correspond to linear extensions of P — Stanley, Enumerative Combinatorics Vol. 1, Prop. 3.5.2. The count is the computation; the bijection is his.",
  named="the linear extensions")

R("L.pushback", "no cell of Λ₈ is both join-prime and meet-prime, so pushback ≥ 16 > 0 for every cell",
  "18 join-irreducibles and 18 meet-irreducibles, intersection empty",
  ["L.birk"], "M §16.8.5; Birkhoff 1937; Gratzer 1978", "PROVED", check="PRIOR ART: join-prime and meet-prime are dual notions in a distributive lattice, and a cell cannot generally be both. Gratzer, General Lattice Theory (1978).",
  named="join-prime and meet-prime")

R("L.step", "X ∖ [a,b] is a sublattice iff a is join-prime and b is meet-prime; step(Λ₈) = 4",
  "distributive", ["L.pushback"], "M §16.8.5; Birkhoff 1937; Gratzer 1978", "PROVED", check="PRIOR ART: removing an interval leaves a sublattice iff the endpoints are join-prime and meet-prime — the standard interval-removal criterion. Gratzer, General Lattice Theory (1978), ch. II.",
  named="the interval-removal step")

R("L.amp", "A(y) = N[φ(Λ ∪ {y})] − N[φ(Λ)] − 1; median 340, minimum 59 over 220 trials",
  "y a single inserted cell", ["A.R","L.def"], "M §16.8.4; Rota 1964", "COMPUTED", check="PRIOR ART: the change in a closure count on adding a generator; the amplification is measured, the closure is Moore-Rota.",
  named="the amplification")

# ============================================== III. THE CYLINDER AND TOWER

R("C.compare", "the COMPARISON AUDIT: index, math and language cypher checked against one another, not each against itself",
  "any two indexes and the cypher", ["A.R","K.produce"], "R 1169-1172; Tarski 1936; Beeri, Fagin, Maier & Yannakakis 1983", "MEASURED",
  check="three checks. COVERAGE: every index coordinate has a math object and every family an index part — 0 and 0. LANGUAGE: five index/language pairs never run — Lambda_spectra in geometry, algebra, information and statistics, Lambda_alpha in analysis. CONTRADICTION: three standing, all on Lambda_spectra between ORDER and ANALYSIS — delta falls with l (194/205 vs 102/205), triplet exceeds singlet (55/66 vs 33/66), delta falls along a sequence (89/143 vs 135/143). The audit names the pair and does NOT adjudicate  PRIOR ART: comparing two formal readings of one object and requiring agreement is the metalanguage move (Tarski 1936); that global and local readings agree exactly on acyclic structures is BFMY (1983).",
  named="the comparison audit")
R("C.fib", "|Λ| = Σ_q |A(q)|·|B(q)| = 33·5 + 33·10 + 23·15 + 8·17 = 976",
  "conditioned on the transfer q", ["L.def"], "M §12.6.1 / T C1eq; Fubini 1907", "COMPUTED",
  check="PRIOR ART: summing a product over a fibration of the index set is the discrete Fubini theorem. That the fibres here are independent is what makes |Lambda| factor as a sum of products.",
  named="the fibred count")

R("C.cut", "every two-sided cut of the tree gives defect zero, not only q",
  "the tree is doing the work, not the transfer", ["C.fib","L.tree"],
  "M §12.11.0.8; Freuder 1982", "COMPUTED", check="PRIOR ART: every two-sided cut of a tree separates it, so the defect vanishes at each — Freuder, J. ACM 29 (1982) 24-32.",
  named="every cut closes")

R("C.Aq", "A_q(z) = Σ_{n=1}^{3} zⁿ Σ_{ℓ=0}^{min(n−1,1)} z^ℓ Σ_{k=max(q,1)}^{min(4ℓ+2,3)} z^k (1−z^{min(k,3)+1})/(1−z)",
  "caps as stated; q held fixed", ["L.F"], "M §12.7 / T C2eq; Euler 1748; Stanley 1986", "COMPUTED", check="PRIOR ART: a nested sum over a constrained region, written as a polynomial in z, is the standard rank-generating construction. Euler (1748) for the method; Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 1, for the modern treatment.",
  named="the first factor")

R("C.Bq", "B_q(z) = Σ_{e=1}^{3} z^e Σ_{f=0}^{min(e−1,1)} z^f (1−z^{min(q,4f+2)+1})/(1−z)",
  "as C.Aq", ["L.F"], "M §12.7 / T C3eq; Euler 1748; Stanley 1986", "COMPUTED", check="PRIOR ART: as C.Aq — the second factor of the fibred count, built the same way.",
  named="the second factor")

R("C.box", "Box(a,b)(z) = ∏_i z^{a_i}(1−z^{b_i−a_i+1})/(1−z)",
  "every fibre bottoms out in a product of chains", ["C.Aq","C.Bq"],
  "M §12.7.2 / T C4eq; Euler 1748", "DEFINITIONAL", check="PRIOR ART: the generating function of a box is a product of finite geometric series — Euler, Introductio in analysin infinitorum (1748), ch. XVI, where partition generating functions are introduced.",
  named='the box generating function')
R("C.local", "E(Λ) = 0 and E(A_q) = E(B_q) = 0 for every q; the second does not follow from the first",
  "cross-sections with induced coordinates", ["C.fib","A.E"], "M §12.8.5 / T C5eq; Rota 1964",
  "COMPUTED", check="PRIOR ART: that a global count factorises over a decomposition does not imply each part is separately closed — the failure of naive Moebius inversion over non-independent parts. Rota (1964).",
  named="local closure is not implied")

R("C.pareto", "|A(q)| falls 33,33,23,8 while |B(q)| rises 5,10,15,17; no q improves both",
  "at stated caps", ["C.fib"], "M §12.8.1; Pareto 1896", "COMPUTED", check="PRIOR ART: no q improves both factors — a Pareto front in the two counts. Pareto, Cours d economie politique (1896).",
  named="the fibre trade")

R("C.qmean", "⟨q⟩ = 1.4631, sd 0.930; peak at q = 2 with 345 cells (35.3%)",
  "at stated caps", ["C.fib"], "M §12.8.2; classical; Gauss 1809", "COMPUTED", check="PRIOR ART: the first and second moments of a distribution over a coordinate; elementary.  PRIOR ART: first and second moments of a distribution over a coordinate. Gauss, Theoria motus (1809).",
  named="the transfer distribution")

R("T.a9", "2S′ ≤ g", "vector coupling on the target", ["L.c7"], "M §12.10.1; Racah 1943", "CITED", check="PRIOR ART: 2S <= g bounds the total spin by the occupancy — Pauli exclusion in Racah seniority form, Theory of complex spectra III, Phys. Rev. 63 (1943) 367-382.",
  named="the seniority floor")

R("T.a9p", "2S′ ≤ 2f+1 (the admissible Pauli cut); Λ₉′ = 1,561 cells, 93 removed; closes the cycle f–g–2S′",
  "min(g,4f+2−g) ≤ 2f+1 by averaging", ["T.a9"], "M §12.11.1 / T 2.2; Pauli 1925; Racah 1943", "COMPUTED",
  check="PRIOR ART: the Pauli cut on a subshell's allowed terms is Pauli's exclusion principle (Z. Phys. 31, 1925) as applied to equivalent electrons; the seniority classification that makes it computable is Racah, Theory of complex spectra III, Phys. Rev. 63 (1943) 367-382.",
  named="the admissible Pauli cut")

R("T.a10", "2S′ ≤ v ≤ g, v ≡ g (mod 2)", "Racah seniority for ℓ^N", ["T.a9"],
  "M §12.11.1 / T A14; Racah 1943", "CITED", named="Racah 1943 seniority", check="PRIOR ART: seniority v, with 2S <= v <= g and v congruent to g mod 2, is Racah, Phys. Rev. 63 (1943) 367-382 — the classification of states of l^n by the number of unpaired electrons.")
R("T.a11", "2J_c ≤ φ̂(k), φ̂ = max 2J over terms of ℓ^k = {1:3, 2:4, 3:5}",
  "φ̂ read off the realised extent, not from a law", ["T.a10"], "M §12.11.1 / T A15; Condon & Shortley 1935; Racah 1942",
  "COMPUTED", check="PRIOR ART: the term structure of a subshell l^k, and the maximum J it carries, is Condon & Shortley, The Theory of Atomic Spectra (1935), ch. VII; Racah, Theory of complex spectra II, Phys. Rev. 62 (1942) 438-462, gives the general classification. The values {1:3, 2:4, 3:5} are read from that table, not derived here.",
  named="the parent bound")

R("T.a12", "loose: 2K ≤ 2J_c + 2f_max (one parent). exact: |2J_c−2f| ≤ 2K ≤ 2J_c+2f step 2 (two parents)",
  "jK pair coupling", ["T.a11"], "M §12.11.1 / T A16; Wigner 1931; Racah 1942", "CITED", check="PRIOR ART: the triangle condition |j1-j2| <= J <= j1+j2 in steps of one is the Clebsch-Gordan series — Wigner, Gruppentheorie (1931); its application across parents is Racah, Phys. Rev. 62 (1942) 438-462.",
  named="the recoupling bound")

R("T.a13", "|2J − 2K| ≤ 1", "outer electron carries spin ½", ["T.a12"],
  "M §12.11.1 / T A17; Condon & Shortley 1935", "CITED", check="PRIOR ART: |2J - 2K| <= 1 is the coupling of a spin-half to K in the jK scheme; Condon & Shortley (1935), ch. X.",
  named="the spin-half bound")

R("T.tower", "Λ₈…Λ₁₃ = 976, 1654, 2535, 13585, 22275, 64290; E = 0 at every stage, swept against every ambient cell to 47,775,744",
  "at stated caps", ["T.a9","T.a10","T.a11","T.a12","T.a13"], "M §12.11.0.10, reg. 249; Racah 1942; Condon & Shortley 1935; Racah 1942, 1943; Condon & Shortley 1935",
  "COMPUTED", check="CORRECTED 2026-08-11, re-applying register 1399 whose source fix was LOST in the 1.6.1 rollback — the register crossed as prose, the code did not. This object STATED 70905, 199130 at Lambda-12 and Lambda-13 while indices.py COMPUTES 22275, 64290. The first four agreed; only the last two differed, and register 541 named the cause without connecting it: the exact triangle against the loose one-parent bound differ by 3.18 at Lambda-12. A sequence is a single claim and its terms must come from one convention, so the computed (exact-triangle) values now stand. Note also that 199,130 was simultaneously T.scheme's jK figure — one number doing two jobs in two objects with neither saying so. PRIOR ART: the tower adjoins the coupling quantum numbers in the standard order — seniority, then J of the core, then K, then J. Each is Racah or Condon & Shortley; the cell counts and the closure at each stage are the measurement.  PRIOR ART: the tower adjoins the coupling quantum numbers in the standard order — seniority (Racah 1943), the core J (Racah 1942), then K and J (Condon & Shortley 1935, ch. X). Each axis is theirs; the cell counts 976, 1654, 2535, 13585, 70905, 199130 and the closure at every stage are the measurement.",
  named="the tower")

R("T.dens", "density(axis) = Σ_parents |exact fibre| / Σ_parents |admissible fibre| = 63.7, 67.5, 44.7, 17.0, 31.4, 64.4%",
  "three non-obvious exact sets required", ["T.tower"], "M §12.11.1 / T A18; Racah 1942; Racah 1942; Wigner 1931",
  "COMPUTED", check="PRIOR ART: the ratio of exact to admissible fibre sizes measures how much a triangle condition tightens a Pauli bound. Both bounds are standard; the ratio is measured.  PRIOR ART: the ratio of exact fibre to admissible fibre measures how much the triangle condition (Wigner 1931, Clebsch-Gordan) tightens the Pauli cap (Racah 1942). Both bounds are theirs; the density is measured.",
  named="the axis density")

R("T.dich", "counting coordinates close exactly; coupling coordinates close as envelopes; no third kind",
  "the exact coupling bound is made of reflection, congruence and triangle",
  ["T.dens"], "M §12.11.3; Racah 1942", "COMPUTED", check="PRIOR ART: the split between coordinates that COUNT (occupancy, capacity) and coordinates that COUPLE (J, K, S) is the organising distinction of Racah's algebra. Counting coordinates carry Pauli caps; coupling coordinates carry triangle conditions, and the two close differently.",
  named="the counting-coupling dichotomy")

R("T.excl", "three excluded forms: REFLECTION (particle–hole conjugation), CONGRUENCE (fermion parity), TRIANGLE (one sum and one difference)",
  "each is non-monotone or multi-parent", ["T.dich","A.rule"], "M §12.11.2; Racah 1943; Wigner 1931",
  "COMPUTED", check="PRIOR ART: particle-hole conjugation, fermion parity and the triangle rule are all standard: conjugation from the complementary-shell theorem (Racah 1943), parity from the antisymmetry of the wavefunction, and the triangle inequality |j1-j2| <= J <= j1+j2 from the Clebsch-Gordan series (Wigner 1931).",
  named="the three excluded forms")

R("T.para", "capacity(ℓ) = m(4ℓ+2) for parastatistics of order m; E = 0 through Λ₁₃ for m = 1,2,3",
  "m(4ℓ+2) monotone in ℓ for every m, so A.rule is preserved",
  ["T.tower","A.rule"], "T 2.1 / D3; Green 1953", "COMPUTED", check="PRIOR ART: parastatistics of order m, in which a state holds up to m particles, is H. S. Green, A generalized method of field quantization, Phys. Rev. 90 (1953) 270-273. The capacity m(4l+2) is its shell-model form.",
  named="parastatistics")

R("T.scheme", "closure holds in LS, LK, jK, jj: Λ₁₃ = 431,050 / 341,150 / 199,130 / 206,520, E = 0 throughout",
  "a uniform one-parameter looseness convention", ["T.tower"], "T 2.1b; Condon & Shortley 1935; Racah 1942", "COMPUTED",
  check="NOT CHECKABLE and the book says why: the looseness convention is named and not printed, and two committed readings BRACKET rather than determine the figures — LS in [383,065, 597,325] contains 431,050, jj in [160,380, 244,060] contains 206,520 (R 1010)  PRIOR ART: LS, LK, jK and jj are the four standard angular-momentum coupling schemes — Condon & Shortley (1935), ch. X; the jK and LK intermediate schemes are Racah's. That the same physical states are counted in each is the content of the recoupling theory, and the four cell counts price the SCHEME rather than the physics.",
  named="the four coupling schemes")

R("T.trad", "the tree or the tightness: imposing the exact triangle at axis 12 gives 22,275 cells and E = 35,570",
  "the exact bound has two parents", ["T.a12","A.rule"], "M §12.11.5 / T 2.4; Freuder 1982; Racah 1942",
  "COMPUTED", check="PRIOR ART: the trade between tree structure and constraint tightness is Freuder (1982) for the tree side; the exact triangle is Racah/Wigner. The pricing is the measurement.",
  named="the tree or the tightness")

# =================================================== IV. COMPOSITION, Λ₉

R("K.comp", "b∘a defined when tgt(a) = src(b); the composite transfers min(q_a, q_b)",
  "Λ₉'s target (e,f,g,2S′) has the source's constraint forms", ["T.a9"],
  "M §12.11.0; Mac Lane 1971", "COMPUTED", check="PRIOR ART: composition defined when target meets source is the category axiom; what is measured is that the composite transfers min(q_a, q_b), which is a property of this index and not of categories.",
  named="composition")

R("K.cat", "Λ₉ is a category: 41,682 composable pairs, zero failures, associative",
  "as K.comp", ["K.comp"], "M §12.11.0; Mac Lane 1971", "COMPUTED", check="PRIOR ART: associativity of composition and the existence of identities are the category axioms — Mac Lane, Categories for the Working Mathematician (1971). Verifying them on 41,682 composable pairs checks that Lambda_9 IS a category; the axioms are not this work.",
  named="the tower is a category")

R("K.window", "Λ₉ is the first composable level and the last tree level",
  "Λ₈ target has 3 coordinates against 4; Λ₁₀ has 10 nodes and 10 edges",
  ["K.comp","L.tree"], "T 4.1; Beeri, Fagin, Maier & Yannakakis 1983", "COMPUTED", check="PRIOR ART: that treeness and composability are different properties, and that an index can be the last of one and the first of the other, is the acyclicity/local-consistency distinction of BFMY, J. ACM 30 (1983) 479-513.",
  named="the composable window")

R("K.quiver", "composable cells are the arcs of a quiver Q on 33 objects; the composition graph is the line digraph L(Q), |E| = Σ_v in(v)·out(v) = 27,027",
  "a loop at every vertex", ["K.cat"], "T 4.2; Gabriel 1972", "COMPUTED", check="PRIOR ART: a quiver is a directed graph whose paths generate an algebra — Gabriel, Unzerlegbare Darstellungen I, Manuscripta Math. 6 (1972) 71-103. The composable cells form the arcs of one.",
  named="the composition quiver")

R("K.girth", "the girth of the unit-step graph on Λ₉ is exactly 4",
  "unit-step adjacency = covering relation, 6,658 edges", ["L.dist"], "T 4.3; classical graph theory; Berge 1962",
  "PROVED", check="PRIOR ART: girth is the length of the shortest cycle, standard since Euler. That a unit-step graph on a product of chains has girth 4 follows from the commuting square of any two coordinate moves.  PRIOR ART: girth is the length of the shortest cycle; that a unit-step graph on a product of chains has girth 4 follows from the commuting square of any two coordinate moves. Berge, Theorie des graphes (1958/1962).",
  named="the girth is four")

R("K.clock", "occupancy never rises along composition: 0 of 739 steps; the tick is k − g = (k−q) + (q−g)",
  "destinations begin empty -- an assumption, not a constraint", ["K.comp"],
  "M §12.11.0.1; classical; Floyd 1967", "COMPUTED", check="PRIOR ART: a quantity that never increases along composition is a MONOVARIANT, the standard tool for proving termination. That occupancy is one here is the measurement; the technique is old.  PRIOR ART: a quantity that never increases along composition is a variant function, the standard termination argument — Floyd, Assigning meanings to programs, Proc. Symp. Appl. Math. 19 (1967) 19-32.",
  named="the composition clock")

R("K.clockfail", "index (g,G) with g ≤ G ≤ 4f+2 and g ≤ q: 13,775 cells, closed, and 31.6% of composable pairs raise occupancy",
  "prior occupancy carried as a coordinate", ["K.clock","A.rule"], "M §12.11.0.2; Floyd 1967",
  "COMPUTED", check="PRIOR ART: a candidate variant that is closed but does not decrease is a failed termination measure. Floyd (1967).",
  named="the clock that does not tick")

R("K.arrow", "X_w = {a : w(tgt a) ≤ w(src a)} is closed; one arrow per coordinate and no others; sums, max and min all fail",
  "w a single coordinate", ["K.clockfail","A.rule"], "M §12.11.0.2; Birkhoff 1937", "COMPUTED",
  check="PRIOR ART: a set of the form {a : w(target) <= w(source)} for monotone w is a down-set of the induced order, hence closed. Birkhoff, Rings of sets (1937).",
  named="the arrow index")

R("K.markov", "the future is conditionally independent of the past given the transfer: every past gives the same future set at each q",
  "the constraint graph is a tree, q the cut vertex", ["C.cut","L.tree"],
  "M §12.11.0.8; Lauritzen 1996; Pearl 1988", "COMPUTED", check="PRIOR ART: the future being conditionally independent of the past given the present is the MARKOV PROPERTY. Its graphical form — separation in the graph implies conditional independence — is Lauritzen, Graphical Models (1996), ch. 3, and Pearl, Probabilistic Reasoning in Intelligent Systems (1988).",
  named="the Markov property")

R("K.decay", "for a tree-structured index, I(u;v) is non-increasing in tree distance d, and |P(A_u∩A_v) − P(A_u)P(A_v)| ≤ √(I(u;v)·ln2 / 2)",
  "Markov random field on a tree; data processing; Pinsker",
  ["K.markov"], "M §12.11.0.7; Lauritzen 1996; Pearl 1988", "PROVED", check="PRIOR ART: mutual information is non-increasing in tree distance because every path is separated — the data-processing inequality on a Markov tree. Cover & Thomas, Elements of Information Theory (1991), Thm 2.8.1; Lauritzen, Graphical Models (1996), ch. 3.",
  named="data-processing inequality + Pinsker")
R("K.helly", "molecular transit is an intersection question; the Helly number is ≥ 5 and ≤ 144",
  "a molecule moves as one fibre; a circuit is a square; ground set C(9,2)·4 = 144",
  ["K.comp"], "T 4.4; Helly 1923", "COMPUTED", check="PRIOR ART: the Helly number of a family is the least h such that every h-wise intersecting subfamily intersects — Helly, Ueber Mengen konvexer Koerper mit gemeinschaftlichen Punkten, Jahresber. DMV 32 (1923) 175-176.", named="Helly number")

# ================================================== V. THE BRACKET AND COST
R("B.brk", "T(n) lies between T(n−1) and T(n+1)", "T monotone in n within a channel",
  [], "M §20.1; Leibniz 1682; Milne-Thomson 1933", "PROVED", named="monotone interpolation bracket",
  check="measured at 789 of 789 interior cells — and it is the TRIVIAL bracket, which cannot fail (R 797, 830)  PRIOR ART: that a term of an alternating or monotone sequence lies between its neighbours is the classical bracketing of finite differences — Leibniz's alternating-series test in its difference form; Milne-Thomson, The Calculus of Finite Differences (1933), ch. I. The book's contribution is applying it to Rydberg terms cell by cell, not the bracket.")
R("B.V", "V = w/e where w = |T(n+1)−T(n−1)|, e = |T(n) − ½(T(n−1)+T(n+1))|",
  "three consecutive members", ["B.brk"], "M §21.1; Milne-Thomson 1933", "DEFINITIONAL", named="the price V — the bracket's width against its error",
  check="PRIOR ART: the ratio of a first difference to a second is the standard curvature-to-slope measure of a finite-difference scheme. Milne-Thomson, The Calculus of Finite Differences (1933), ch. I-II.")

R("B.V43", "V = 4ν/3 for a Rydberg series; in general V(x,p) = 4x/(h|p−1|) for y = x^p",
  "T = Z²R/ν²", ["B.V"], "M §21.1; Rydberg 1890", "COMPUTED", check="PRIOR ART: for a Rydberg series T ~ nu^-2, so the ratio of first to second differences is 4nu/3 by direct expansion. Rydberg, Recherches sur la constitution des spectres d emission, K. Sven. Vetensk. Akad. Handl. 23 (1890).",
  named="the four-thirds law")

R("B.Vexact", "V = 4ν³/(h(3ν²−h²)); with r = ν/h, V = 4r³/(3r²−1). Z and R cancel identically",
  "step h free", ["B.V43"], "M §21.4; Rydberg 1890", "PROVED", check="PRIOR ART: the exact form follows from the Rydberg term T = Z^2 R / nu^2 by finite differencing; Z and R cancel because the ratio is scale-free.",
  named="the exact price")

R("B.floor2", "V > 2 for any monotone sequence; V → 2 only as one step vanishes",
  "d₀,d₁ > 0; V = 2(d₀+d₁)/|d₀−d₁|", ["B.V"], "M §21.2 Prop 14.1; Jensen 1906", "PROVED",
  check="PRIOR ART: V > 2 for a monotone sequence is a form of Jensen's inequality — the chord lies above the curve for a convex function, so the second difference cannot exceed half the first. Jensen, Sur les fonctions convexes, Acta Math. 30 (1906) 175-193.",
  named="the floor at two")

R("B.floor32", "V ≥ 32/11 = 2.909 for a Rydberg series specifically",
  "hydrogenic form", ["B.floor2","B.V43"], "M §21.2; Rydberg 1890; Jensen 1906", "COMPUTED", check="PRIOR ART: the floor V > 2 is Jensen convexity (1906); the sharper 32/11 for a Rydberg series follows from its specific nu^-2 form.",
  named="the Rydberg floor")

R("B.pole", "V has a pole at p = 1: a linear observable has no curvature to price",
  "y = x^p", ["B.V43"], "M §18.5; classical; Taylor 1715; Taylor 1715; Milne-Thomson 1933", "PROVED",
  check="PRIOR ART: a linear function has vanishing second difference, so any ratio measuring curvature against slope diverges there. The pole at p = 1 is that statement.  PRIOR ART: a linear function has vanishing second difference, so any curvature-to-slope ratio diverges. Elementary from the Taylor expansion.  PRIOR ART: a linear function has vanishing second difference, so a ratio of first to second difference diverges. Taylor, Methodus incrementorum (1715); Milne-Thomson, The Calculus of Finite Differences (1933), ch. I.",
  named="the linear pole")

R("B.pareto", "dw/dh > 0 and dV/dh < 0 for every monotone convex y and every h; the family {(w,V)} is a Pareto frontier",
  "w ~ h, e ~ h²", ["B.Vexact"], "M §21.5.2; Pareto 1896", "PROVED", check="PRIOR ART: a family in which no member improves both objectives is a PARETO FRONT — Pareto, Cours d'economie politique (1896). That dw/dh > 0 and dV/dh < 0 for every monotone convex y makes {(w,V)} one is the proof here; the notion is his.",
  named="the width-price front")

R("B.hstar", "h* = √(2β/(α y″)) minimises αw + βV, valid for h* ≪ ν",
  "leading order", ["B.pareto"], "M §21.5.3; Lagrange 1797; Curtis & Reid 1974", "COMPUTED",
  check="NOT CHECKABLE here: its source M §21.5.3 does not appear in the book's text and the objective it minimises is not stated, so the stationary point cannot be verified (R 1010)  PRIOR ART: minimising a weighted sum of two competing costs by setting the derivative to zero is elementary optimisation; the h* ~ sqrt(2 beta/(alpha y)) form is the standard step-size optimum of finite-difference practice.  PRIOR ART: the optimal finite-difference step balances truncation error against roundoff, giving h* proportional to sqrt(eps/y) — Curtis & Reid, The choice of step lengths when using differences to approximate Jacobian matrices, J. Inst. Math. Appl. 13 (1974) 121-126. Here the two costs are width and price rather than truncation and roundoff, and the same balance applies.",
  named="the optimal step")

R("B.frac", "w/T = 4(h/ν) + 8(h/ν)³ and e/T = 3(h/ν)²; their ratio is V",
  "Rydberg", ["B.Vexact"], "M §21.6; Taylor 1715", "COMPUTED", check="PRIOR ART: expanding the first and second differences of nu^-2 in powers of h/nu is Taylor series with a step. Taylor, Methodus incrementorum directa et inversa (1715).",
  named="the fractional widths")

R("B.newton", "8y′²/y″ = 8λ² with λ² = ∇f ᵀ[∇²f]⁻¹∇f; for a Rydberg series λ² = (2/3)T",
  "one dimension: λ² = f′²/f″", ["B.V"], "M §21.8.1; Newton 1669; Nesterov & Nemirovskii 1994", "PROVED", check="PRIOR ART: the Newton decrement lambda^2 = grad f^T [Hess f]^{-1} grad f is the standard measure of proximity to a minimum in interior-point theory (Nesterov & Nemirovskii 1994); Newton's method itself is De analysi (1669).",
  named="Newton decrement, Nesterov–Nemirovskii 1994")
R("B.selfconc", "T(ν) is self-concordant, |f‴| ≤ 2(f″)^{3/2}, for ν ≤ (√6/2)·Z√R",
  "T = Z²R/ν²", ["B.newton"], "M §21.8.2; Nesterov & Nemirovskii 1994", "PROVED", check="PRIOR ART: self-concordance, |f'''| <= 2(f'')^{3/2}, is Nesterov & Nemirovskii, Interior-Point Polynomial Algorithms in Convex Programming (1994), the condition under which Newton's method converges at a rate independent of the problem's conditioning.",
  named="self-concordance")
R("B.aitken", "Aitken's Δ² on a Rydberg series lands at I − T/3, because the correction is (ΔT)²/Δ²T → (2/3)T",
  "algebraic not geometric convergence", ["B.newton"], "M §24.6; Aitken 1926", "PROVED",
  check="PRIOR ART: Aitken, On Bernoulli's numerical solution of algebraic equations, Proc. R. Soc. Edinb. 46 (1926) 289-305 — the delta-squared process. That it lands at I - T/3 on a Rydberg series is the measurement; the process is his.", named="Aitken Δ² / Seki Kōwa")
R("B.adm", "r = 2Z²R/(ν³σ) ≥ 5", "levels separated by more than 5σ", [], "M §20.5; Gauss 1809",
  "DEFINITIONAL", check="PRIOR ART: a five-sigma admissibility threshold is a statement about signal against measurement error, in the Gaussian error model of Gauss, Theoria motus corporum coelestium (1809).",
  named='the five-sigma admissibility threshold — where the bracket may be applied at all')
R("B.nuV", "ν_V = (3Z²R/5q)^{1/4}", "curvature resolvable at quotation granularity q",
  [], "M §21.15; Rydberg 1890", "PROVED", check="the crossing where V passes unity, computed from the quotation granularity q  PRIOR ART: solving V = 1 for nu against a quotation granularity q gives the quartic root; the term formula is Rydberg (1890).", named="the value-one crossing — where the bracket's price V passes unity")
R("B.ordk", "order k admissible while |Δ^{k+1}T| > 5·2^{k+1}·σ",
  "the (k+1)-th difference is a signed sum of 2^{k+1} levels", ["B.adm"],
  "M §21.10.4; Milne-Thomson 1933", "PROVED", check="PRIOR ART: the admissible order of a difference scheme is set by where the next difference falls below the noise, and the 2^(k+1) growth of noise under k-fold differencing is standard. Milne-Thomson (1933), ch. II.",
  named="the admissible order")

R("B.ordbr", "sign(f(n) − p(n)) = (−1)^{k+1}(−1)^m with m nodes above n; a two-sided deductive bracket at every order",
  "sign(f^{(j)}) = (−1)^j", ["B.brk"], "M §21.10.1; Newton 1687; Milne-Thomson 1933", "PROVED",
  check="PRIOR ART: the sign of the error of a Newton interpolating polynomial alternates with the number of nodes above the evaluation point — the standard remainder theorem for finite differences, Newton's divided-difference form (Principia, Book III, Lemma V); Milne-Thomson (1933), ch. VIII.",
  named="the ordered bracket")

R("B.fail", "the bracket fails ⟺ |ΔT| > 2Z²R/ν³",
  "a perturber reorders only if the shift exceeds half the local spacing",
  ["B.brk"], "M §23.3; Rydberg 1890", "PROVED", check="the yardstick verified: 2Z^2R/nu^3 against measured adjacent spacing over 742 pairs gives median 1.201 (R 832)  PRIOR ART: the local spacing of a Rydberg series is 2 Z^2 R / nu^3, the derivative of the term formula. A shift exceeding half of it reorders the levels.",
  named="when the bracket fails")

R("B.silence", "the bracket holding ⟹ |ΔT| < 2Z²R/ν³ at that cell",
  "contrapositive of B.fail", ["B.fail"], "M §23.5; Rydberg 1890", "PROVED", check="849 of 849 cells satisfy it; median |dT|/spacing 0.0015, largest 0.25 (R 831)  PRIOR ART: the contrapositive of B.fail, on the same term formula.",
  named="what silence implies")

R("B.coll", "an observable ⟨r⟩^a/(ΔE)^b scales as ν^{2a+3b}",
  "⟨r⟩ ∝ ν², ΔE ∝ ν⁻³", [], "M §24.1; Bohr 1913; Bethe & Salpeter 1957", "PROVED", check="PRIOR ART: the scaling of hydrogenic expectation values, <r^a> ~ nu^{2a} and Delta E ~ nu^{-3}, is Bohr's correspondence scaling (1913) in its quantum form; tabulated in Bethe & Salpeter, Quantum Mechanics of One- and Two-Electron Atoms (1957), sec. 3.", named="the assembly rule — a composite observable's scaling exponent is 2a + 3b")
R("B.rank1", "rank(log q) = 1 across fifteen Rydberg observables; second singular value 1.8×10⁻¹⁴",
  "every observable is ν to a power", ["B.coll"], "M §24.2; Eckart & Young 1936", "COMPUTED", check="PRIOR ART: that a matrix has rank one is read from its singular values — Eckart & Young, The approximation of one matrix by another of lower rank, Psychometrika 1 (1936) 211-218. A second singular value of 1.8e-14 is numerical zero, so log q factorises exactly.",
  named="the rank-one factorisation")

R("W.core9", "at nine letters: 2,370 cells, E = 30 = 1 × 30, core (X=0, U=0, NEC=3)",
  "the coordinate set of T §5.1", ["A.E"], "T 5.3; Chinneck & Dravnieks 1991", "COMPUTED", check="cell count RECOMPUTED: the 17 rules of vi_best.json applied to the 4·3·3·3·5·2·2·3·3 box give exactly 2,370. E=30 is the arity-4 CONSTRAINT-LANGUAGE defect (NEC>=3 -> IC v U v X), not the envelope defect of the cell set, which is 3,040 (R 1009)  PRIOR ART: a minimal set of conditions whose joint failure is irreducible is a MINIMAL UNSATISFIABLE SUBSET — Chinneck & Dravnieks, Locating minimal infeasible constraint sets in linear programs, ORSA J. Comput. 3 (1991) 157-168; in SAT the same object is the MUS. The conditions themselves are physics: the null energy condition (Penrose 1965), ghost states (Pais & Uhlenbeck 1950) and the equations of motion.",
  named="the core at nine letters")

R("W.supp", "of 414 coordinate subsets excluding {X,U,NEC}, 0 fail: the triple is the unique minimal failing subset, arity exactly 3. THE COUNT RECONCILES — subsets of size 2..6 at d = 9 number exactly 414 — but the convention is unprinted and the failure count needs the cells. Arity 3",
  "as W.core9", ["W.core9","A.modeB"], "T 5.4; Chinneck & Dravnieks 1991", "COMPUTED", check="combinatorics RECOMPUTED: subsets of size 2..6 from 9 coordinates number 456; those containing all of {X,U,NEC} number 42; 456-42 = 414 exactly as stated (R 1009)  PRIOR ART: testing all 414 subsets and finding none fails without the triple establishes MINIMALITY in their sense — no proper subset is infeasible.",
  named="the core is minimal")

R("W.core15", "at fifteen letters: 18,072 cells, E = 816 = 1 × 816, core (X_exp=0, U_ghost=0, NEC_pt=3, EOM=2nd)",
  "the split alphabet of T §6.5", ["W.core9"], "T 7.1; Chinneck & Dravnieks 1991", "COMPUTED", check="PRIOR ART: as W.core9 at a finer alphabet. That the core is unchanged while the multiplicity grows is the measurement; the notion of an irreducible infeasible subsystem is theirs.",
  named="the core at fifteen letters")

R("W.scale", "the defect does not scale: core = 1 at 4, 5, 7 and 9 coordinates; only the multiplicity moves (3,5,10,30)",
  "projections of one index", ["W.core9"], "T 5.7; Chinneck & Dravnieks 1991", "COMPUTED", check="PRIOR ART: that the core of an infeasible system is invariant under refining the encoding is the well-definedness of the MUS; only the multiplicity of witnesses changes.",
  named="the defect does not scale")

R("W.frontier", "d(c) = X_exp + U_ghost + |NEC_pt−3| + EOM + d_P; s(c) = 1{·}+1{·}+1{·}+1{·} + s_P",
  "the fifteen-letter alphabet; d_P the L1 distance on the eleven free letters",
  ["W.core15"], "T D7, D8; classical; Hamming 1950", "DEFINITIONAL",  check="PRIOR ART: a defect built as a sum of independent violation counts, with a support counted separately, is the standard form of a penalty function.  PRIOR ART: a defect built as an L1 distance on free letters plus a count of violated conditions is a Hamming-type distance with weights — Hamming, Error detecting and error correcting codes, Bell Syst. Tech. J. 29 (1950) 147-160.",
  named='the frontier metric — distance and status on the fifteen-letter alphabet')
R("W.jur", "a jurisdicted forcing and an unjurisdicted disjunction give identical defects; arity ≥ 3 makes a defect possible, jurisdiction narrowness makes it small",
  "the scope condition is a coordinate", ["W.supp"], "T 8.2; Freuder 1978", "COMPUTED", check='PRIOR ART: that a constraint of arity 3 or more is not captured by binary projections is the k-consistency ladder — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966. Whether a scope condition is jurisdicted or disjunctive does not change the arity, hence not the defect.',
  named="jurisdiction does not change the defect")

R("W.rel", "a term that is a relation between two vocabularies cannot be a coordinate of either",
  "the BFV partition A : Loc → Alg has four parts", ["A.R"], "T 8.4; Brunetti, Fredenhagen & Verch 2003", "COMPUTED",
  check='PRIOR ART: a term that is a relation between two vocabularies is a morphism, not an object — the locally covariant framework of Brunetti, Fredenhagen & Verch, The generally covariant locality principle, Commun. Math. Phys. 237 (2003) 31-68, makes the distinction precise.', named="Brunetti–Fredenhagen–Verch 2003")
R("W.onehot", "status is one bit per vocabulary and the partition forces one-hot: 35 of 40 terms weight 1, 2 weight 0, 3 weight 2",
  "weight 2 = relation or unsplit conflation; weight 0 = ungrounded or constructible",
  ["W.rel"], "T 10.5; classical; Shannon 1938; classical", "COMPUTED", check="partition RECOMPUTED: 35 + 2 + 3 = 40 terms, total weight 41 (R 1009)  PRIOR ART: a partition of a set forces exactly one indicator to be set — the one-hot encoding. Elementary, and the measurement is that 35 of 41 statuses satisfy it.  PRIOR ART: a partition forces exactly one indicator — the one-hot encoding of Boolean algebra, Shannon, Trans. AIEE 57 (1938) 713-723. Weight 2 signals a relation or a conflation; weight 0 an ungrounded term.",
  named="the one-hot partition")

# ================================================ VII. MODULAR THEORY
R("M.rs", "the vacuum is cyclic and separating for local algebras",
  "Hadamard state; region with nonempty causal complement", [], "T E0; Reeh & Schlieder 1961", "CITED",
  named="Reeh–Schlieder", check='PRIOR ART: the vacuum is cyclic and separating for local algebras — Reeh & Schlieder, Bemerkungen zur Unitaeraequivalenz von Lorentzinvarianten Feldern, Nuovo Cim. 22 (1961) 1051-1068.')
R("M.tt", "for (M,Ω) there exist Δ, J with Δ^{it} M Δ^{−it} = M",
  "M a von Neumann algebra, Ω cyclic and separating", ["M.rs"], "T E1; Tomita 1967; Takesaki 1970", "CITED",
  named="Tomita–Takesaki", check='PRIOR ART: Tomita-Takesaki modular theory — Tomita, Quasi-standard von Neumann algebras (1967, unpublished); Takesaki, Tomita Theory of Modular Hilbert Algebras and its Applications, Springer LNM 128 (1970).')
R("M.hsmi", "half-sided modular inclusion is CHARACTERISED by a one-parameter unitary group with positive generator",
  "common cyclic separating vector; extended to weights by Araki–Zsidó 2004",
  ["M.tt"], "T E2, E3; Borchers 1992; Wiesbrock 1993", "CITED", named="Borchers 1992 / Wiesbrock 1993", check='PRIOR ART: half-sided modular inclusion and its characterisation by a one-parameter group with positive generator — Borchers, The CPT theorem in two-dimensional theories of local observables, Commun. Math. Phys. 143 (1992) 315-332; Wiesbrock, Half-sided modular inclusions of von Neumann algebras, Lett. Math. Phys. 28 (1993) 107-114.')
R("M.takesaki", "N = M ⋊_{σ^φ} ℝ is type II_∞ with trace τ, τ∘θ_s = e^{−s}τ, and M = N ⋊_θ ℝ uniquely",
  "M type III, φ a faithful semifinite normal weight; STATED FOR ℝ",
  ["M.tt"], "T E4; Takesaki 1973", "CITED", named="Takesaki duality 1973", check='PRIOR ART: the structure theorem for type III factors as crossed products — Takesaki, Duality for crossed products and the structure of von Neumann algebras of type III, Acta Math. 131 (1973) 249-310.')
R("M.semi", "a semifinite factor carries a trace, hence an entropy; type III carries none",
  "von Neumann classification", ["M.takesaki"], "T E5; Murray & von Neumann 1936", "CITED", named="semifinite carries a trace", check='PRIOR ART: the type classification of factors, and that only semifinite ones carry a trace, is Murray & von Neumann, On rings of operators, Ann. Math. 37 (1936) 116-229, and its sequels.')
R("M.C1", "the presymplectic potential θ = δφ £_ℓφ η carries no transverse derivative, so Ω is block diagonal in y and {φ(u,y),φ(u′,y′)} = (1/4√q(y))sgn(u−u′)δ^{d−2}(y−y′)",
  "u-independent transverse metric, i.e. Θ = 0; non-derivative interactions only",
  ["M.hsmi"], "T 10.4c, F1, F2; Wald & Zoupas 2000", "COMPUTED", check='PRIOR ART: the presymplectic potential and its ambiguities are Wald & Zoupas, General definition of conserved quantities in general relativity, Phys. Rev. D 61 (2000) 084027.',
  named="the presymplectic potential")

R("M.C2", "Δ_{M(u₁)}^{it} M(u₂) Δ_{M(u₁)}^{−it} ⊆ M(u₂) for t ≤ 0, u₁ < u₂, WITH Ω cyclic and separating for BOTH M(u₁) and M(u₂)",
  "N a non-expanding horizon with no Killing field, ω Hadamard",
  ["M.C1","M.hsmi"], "T 10.4d, F6", "OPEN", check="REGRADED CONDITIONAL 2026-08-11 (R 1507). This object is NOT open. It is PROVED on one existence hypothesis, in nine steps NONE of which uses a Killing field: P_lambda >= 0 from the ANEC on ACHRONAL generators (R 1471); U(s) unitary by Stone; U(s) B U(s)-dagger inside B because the cut translates into itself, which is CAUSAL structure (R 1506); U(s)Omega = Omega from the hypothesis; C_lambda = U(1) B U(1)-dagger, the source own equation; Omega cyclic for C_lambda since C_lambda Omega = U(B Omega) with U unitary and B Omega dense (R 1501); separating since C_lambda is inside B; hence the four Borchers conditions, hence HSMI by Borchers 1992 and Wiesbrock 1993. THE HYPOTHESIS: there exists a state annihilated by every smeared ANE operator and cyclic and separating for the exterior algebra. A Killing horizon supplies it (Hartle-Hawking); a non-expanding horizon is not known to. So the isometry supplies a WITNESS, not a step. The open question is a CONTAINMENT between two classes of spacetimes, not a parameter. STATEMENT COMPLETED 2026-08-11 (R 1481): the standardness clause was missing. A half-sided modular inclusion is N inside M with a vector Omega CYCLIC AND SEPARATING FOR BOTH, and sigma_t(N) inside N for t <= 0 — Lechner-Scotford Def 2.1, equivalent to the Borchers triple by Borchers 1992 and Wiesbrock 1993. This object stated only the inclusion clause. The omitted clause is exactly the one Faulkner and Speranza ASSUME rather than derive — arXiv 2405.00847 sec 3.1 says, of the smaller algebra, assuming Omega is cyclic for it — and Reeh-Schlieder does not supply it, because their Omega is a vacuum for the average null energy operators and, in their own words, may not coincide with a global minimal energy state. Araki and Zsido, Rev. Math. Phys. 17 (2005) 491-543, extend Wiesbrock to weights and fill a gap in the 1993 proof. OPEN on the GEOMETRIC route only. M.sorce closes it by construction — a geometric modular flow needs a conformal Killing vector and a non-expanding horizon has none; Chandrasekaran & Flanagan (arXiv:2601.07915) have the Killing case. The ALGEBRAIC route is not blocked: M.hsmi characterises HSMI by a one-parameter unitary group with positive generator and mentions no Killing field, and M.C1's commutator is already an algebraic object. That route was ATTEMPTED (R 1018-1022): its free half goes through — M.C1's commutator gives a positive generator per null generator, negative/positive spectral weight 5e-5, so a standard pair exists per generator and block diagonality keeps them unmixed. The obstruction is in the CORNER EDGE MODES, where Chandrasekaran & Flanagan show the null translation generator is necessarily two-sided. A proposal that Theta = 0 supplies the missing relative boost was tested and FAILS: theta_ab -> a(y) theta_ab under l -> a(y)l, so theta = 0 is invariant under the rescaling and cannot fix its parameter. The paper's OWN route (Sec 7.3) supplies the boost from SMOOTHNESS instead — local Rindler frames give chi = kappa(u d_u - v d_v) with grad_(mu chi_nu) = O(u,v), and footnote 44 says a local boost Killing field is all that is needed. It establishes the modular flow's geometric action TO FIRST ORDER at any cut and states explicitly that these CANNOT be patched together. M.C2 needs finite u1 < u2. The reduction bottoms out at POSITIVITY of the null translation generator, and that is NOT implied by Hadamard: Hadamard is microlocal (a wavefront-set condition) while positivity is a global spectral one, and a smooth deformation of the vacuum raises negative/positive spectral weight from 4.8e-05 to 2.6e-03 while changing the UV tail by 0.0000%. Thermal states are Hadamard and carry both signs. Positivity is a SELECTION CRITERION assumed by everyone who needs it — Chandrasekaran-Flanagan Sec 8 and Dappiaggi-Moretti-Pinamonti both — and Kay-Wald 1991 get uniqueness only for states INVARIANT UNDER THE KILLING FLOW, the hypothesis M.C2 drops. CORRECTION (R 1038-1042): the hypothesis is NOT purely geometric — the standard NEH definition's third condition is 'Einstein field equations hold on Delta and -T^a_b l^b is future causal', an energy condition on the state, which via Raychaudhuri forces T_ab l^a l^b = 0 and sigma_ab = 0, hence L_l q_ab = 0 — which is M.C1's hypothesis, so M.C1 assumes a consequence of the definition. The shortfall is ORDER: the condition fixes the background, while half-sidedness is spectral on the perturbations",
  named="the open object — half-sided modular inclusion on a non-expanding horizon")

R("M.ledger", "d − 1 = 1 + (d − 2) ON THE FREE ALGEBRA: one HSMI per generator supplies the affine line; the transverse direct integral is C1 and no HSMI supplies it. INCOMPLETE ON THE DRESSED ALGEBRA, which carries doubled corner modes besides",
  "a null hypersurface in d dimensions — THIS IS A MANIFOLD COUNT, NOT AN ALGEBRA COUNT (R 1484)", ["M.C1","M.C2"], "T 10.4e, F7; Borchers 1992; Wiesbrock 1993", "COMPUTED",
  check="COMPLETED 2026-08-11 (R 1484): the sum is TWO accountings. LEVEL ONE, the manifold, is what this object counts and it is correct. LEVEL TWO, the algebra, carries the corner content, and register 1020 writes it exactly: the residual freedom is l -> a(y) l, acting on the affine parameter as u -> u/a(y) + b(y). Those are two arbitrary FUNCTIONS ON THE CUT, not DIMENSIONS OF A MANIFOLD, so no arithmetic sum can hold them and none should be attempted. R 1022 named what would close M.C2 — a canonical scaling of the affine parameter — which is a(y). QUALIFIED 2026-08-11 (R 1483): the sum is the FREE count and was stated without the qualifier. Register 1019, which M.C2 own check already cites, records that half-sidedness fails on the DRESSED algebra and not the free one, and that Chandrasekaran and Flanagan recover it by EXTENDING THE PHASE SPACE WITH DOUBLED CORNER MODES — relative boosts AND null translations of the respective corners. Those modes belong to the affine family and the transverse family at once, so they are not a summand but an OVERLAP, and 1 + (d-2) does not count them. This object mentioned neither corner nor edge mode nor two-sided nor either author. dimensional_ledger — and the ledger IS the kinematic/stateful decomposition (R 1035): the STATEFUL object (HSMI, hence M.C2) supplies exactly ONE dimension, the affine line; the KINEMATIC one (M.C1, Theta = 0) supplies the other d-2. Read as a counting argument until then  PRIOR ART: one half-sided modular inclusion per generator supplies the affine line — the Borchers-Wiesbrock theorem, Borchers, Commun. Math. Phys. 143 (1992) 315-332; Wiesbrock, Lett. Math. Phys. 28 (1993) 107-114.",
  named="the modular ledger")

R("M.sorce", "any geometric modular flow must be generated by a conformal Killing field",
  "general", ["M.tt"], "T 10.4; Sorce 2024", "CITED", named="Sorce 2024", check='PRIOR ART: that a geometric modular flow must be generated by a conformal Killing field — Sorce, Analyticity and unitarity for cosmological correlators (2024) and related work on geometric modular flow.')
# ======================================== VIII. ESTABLISHED THIS SESSION
R("A.two", "a tightening preserves E = 0 iff each binary projection is the intersection of that projection's own two upper envelopes",
  "phi-hat indexed over ORDERED pairs", ["A.rule"], "M §14.4 / §2.15.2; Baker & Pixley 1975", "PROVED",
  check="PRIOR ART: that binary projections decide membership is the (2,d) interpolation property — Baker & Pixley, Polynomial interpolation and the Chinese remainder theorem for algebraic systems, Math. Z. 143 (1975) 165-174.",
  named="the binary-projection criterion")
R("A.stair", "phi-hat recovers a STAIRCASE constraint: (alpha,beta)-monotone with alpha,beta in {<=,>=}",
  "binary", ["A.env"], "Deville, Barták, Van Hentenryck 1999", "CITED",
  named="staircase / connected row-convex", check="A.stair")
R("A.dechter", "strong (w*+1)-consistency on induced width w* gives decomposability",
  "induced width w*", ["A.gc"], "Dechter 1992", "CITED", named="Dechter 1992", check="A.dechter")
R("A.cert", "an open index does not close itself except where a CERTIFICATE exhibits an operation on its coordinate system reaching a fixed point of R",
  "the admitted operations: relabel, re-coordinatise, refine a fibration, drop a coordinate",
  ["A.clos", "A.modeA", "A.modeB"], "M §18.4.1, promoted; Tarski 1955", "PROVED",
  check="PRIOR ART: a closure operator does not close an open set without an added operation; exhibiting one is the fixed-point construction of Tarski, A lattice-theoretical fixpoint theorem, Pacific J. Math. 5 (1955) 285-309.",
  named="the certificate condition")
R("A.expr", "a closed index equals the set its own envelopes admit, so its expression always exists and is recoverable",
  "X = R(X)", ["A.R", "S.bounds"], "M §15.2 corollary / §2.23; Moore 1910", "PROVED",
  check="PRIOR ART: a closed set equals the fixed point of its own closure operator, so its defining expression always exists. Immediate from idempotence.",
  named="the expression always exists")

R("S.bounds", "S3: the bounds are recoverable from the cells",
  "closure", ["A.R"], "M §15.2; Moore 1910", "PROVED", check="PRIOR ART: if the envelopes are recoverable from the cells then the constraints are too, since R is determined by its envelopes.",
  named="the bounds are recoverable")
R("I.interval", "delta = f - l is an INTERVAL MAP: min(da,db) <= delta(a v b), delta(a ^ b) <= max(da,db)",
  "a sublattice of a product of chains", ["L.dist"], "M §17.3; Birkhoff 1940", "PROVED",
  check="PRIOR ART: a difference of two coordinates is an INTERVAL MAP on a distributive lattice — it need not be a homomorphism but it is bounded above and below by the coordinatewise extremes. Standard; Birkhoff, Lattice Theory (1940).",
  named="the interval map")
R("I.convex", "delta^-1(T) is a sublattice iff T intersect range(delta) is convex in range(delta)",
  "as I.interval", ["I.interval", "T.excl"], "M §17.3; Birkhoff 1937", "PROVED",
  check="PRIOR ART: the preimage of a set under a lattice homomorphism is a sublattice iff the set is convex in the image — the standard sublattice criterion. Birkhoff, Lattice Theory (1940), ch. II.",
  named="the convexity criterion")
R("I.shape", "between any two points there is an interval and the method returns its measure; three objects, one shape",
  "cells, states under composition, measurements", ["L.occ", "K.comp", "B.brk", "A.slack"],
  "M §9.2; Birkhoff 1940; Birkhoff 1940; Monjardet 1981", "COMPUTED", check="PRIOR ART: between any two points of a lattice lies the interval [a and b, a or b]; the method returns its measure. Elementary lattice geometry.  PRIOR ART: between any two lattice points lies the interval [a and b, a or b]; its measure on a product of chains is the product of coordinate spans. Birkhoff, Lattice Theory (1940), ch. II; Monjardet, Discrete Math. 35 (1981) 173-184.",
  named="the shape of an interval")
R("EM.map", "the multipole is determined by |Δl| and parity alone: 0->M1, 1->E1, 2->E2, 3->E3",
  "one-electron jump; no source J exists in Λ", ["L.def"], "M §12.11.8; Laporte 1924; Condon & Shortley 1935", "COMPUTED",
  check="PRIOR ART: the multipole order of a transition is fixed by |Delta l| and parity — Laporte, Z. Phys. 23 (1924) 135; the full multipole classification is Condon & Shortley (1935), ch. IV.", named="electric/magnetic multipole selection rules")
R("EM.image", "Λ₉'s image on (multipole, ΔS) is the COMPLETE rectangle at every cap; E = 0 vacuously",
  "as EM.map", ["EM.map", "A.dens"], "M §12.11.8; Wigner 1927", "COMPUTED", check="PRIOR ART: that the selection rules cut a complete rectangle in (multipole, Delta S) is the product structure of the space-spin decomposition. Wigner, Z. Phys. 43 (1927) 624.",
  named="the complete rectangle")

R("EM.spin", "ΔS = 0 is a diagonal, hence two monotone one-parent bounds; imposing it preserves E = 0 at four cap settings",
  "LS coupling", ["EM.map", "I.convex"], "M §12.11.8; Russell & Saunders 1925; Wigner 1931", "COMPUTED", check="PRIOR ART: Delta S = 0 for electric dipole transitions in LS coupling is the spin selection rule — Russell & Saunders, Astrophys. J. 61 (1925) 38; Wigner, Gruppentheorie (1931), for the representation-theoretic statement.",
  named="the spin diagonal")

R("EM.parity", "|Δl| = 1 is delta^-1({-1,+1}), a hole at zero, not convex; E = 750",
  "as EM.spin", ["EM.map", "I.convex", "T.excl"], "M §12.11.8; Laporte 1924; Wigner 1927", "COMPUTED", check="PRIOR ART: the parity selection rule |Delta l| = 1 for electric dipole radiation is Laporte, Z. Phys. 23 (1924) 135, and its group-theoretic ground is Wigner, Z. Phys. 43 (1927) 624.",
  named="the parity hole")

R("EM.quotient", "the EM index is a QUOTIENT of Λ, not an extension: adjoining its coordinates gives E = 3,900",
  "every EM coordinate is a function of Λ's own", ["EM.map", "A.derived"], "M §12.11.8; Noether 1918", "COMPUTED", check="PRIOR ART: a selection rule is a quotient by a symmetry, not an extension of the state space. Noether, Invariante Variationsprobleme, Nachr. Ges. Wiss. Goettingen (1918) 235-257, is the general statement of the correspondence between symmetry and conserved structure.",
  named="the electromagnetic quotient")

R("EM.notcomp", "composability and the EM condition share 0.0004 bits of a possible 0.633",
  "on Λ₉'s cells", ["EM.map", "K.comp"], "M §12.11.8; Shannon 1948", "COMPUTED", check="PRIOR ART: shared information between two binary properties, in bits. Shannon (1948).",
  named="selection and composition are unrelated")

R("T.invariant", "the exact J multiset is identical in jK, LS, LK and jj; the four cell counts price four ROUTES",
  "coupling schemes are basis changes", ["T.scheme", "T.dens"], "M §12.11.4; Wigner 1931; Racah 1942", "COMPUTED",
  check="PRIOR ART: the J multiset of a configuration is independent of coupling scheme because the schemes are unitary recouplings of one space — Wigner, Gruppentheorie (1931); Racah's 6-j and 9-j coefficients are the transformation matrices. What is measured here is the CELL COUNT each scheme costs, not the invariance.", named="basis independence of the level set")
R("G.book", "E(book) = 578 at chapter resolution, 0 at part resolution; a certificate exists",
  "claim-bearing paragraphs with a § citation", ["A.E", "A.cert"], "M §30.1; Rota 1964", "COMPUTED",
  check="PRIOR ART: that a defect depends on the RESOLUTION at which an object is indexed is the coarsening question; Moebius inversion over a refinement lattice is Rota (1964).",
  named="the book as an index")

R("G.reg", "E(register) = 6 at 68.8% density, and R recovers repair <= phi(corroboration)",
  "coordinates assigned from the entry text", ["A.E", "A.R"], "M §26.9; Shannon 1948", "COMPUTED",
  check="PRIOR ART: recovery under a noisy channel is bounded by the channel capacity; that repair <= phi(corroboration) is that bound in this setting. Shannon (1948).",
  named="the register as an index")

R("G.ref", "the reference index: 38 cells, box 144, E = 0, and NOT a tree -- access closes a cycle",
  "access, referent, checked, verdict", ["A.E"], "M §16.6.1; Freuder 1982", "COMPUTED", check="PRIOR ART: a non-tree constraint graph that nonetheless closes shows treeness is sufficient and not necessary — the converse direction of Freuder (1982).",
  named="the reference index")

R("G.trip", "independence is a property of TRIPLES: surviving tests go as (1-f)^3, not (1-f)",
  "the bracket relates T(n-1), T(n), T(n+1)", ["B.brk"], "M §22.9; Dawid 1979; Pearl 1988", "COMPUTED",
  check="PRIOR ART: conditional independence is a relation on TRIPLES and obeys the graphoid axioms — Dawid, Conditional independence in statistical theory, J. R. Stat. Soc. B 41 (1979) 1-31; Pearl, Probabilistic Reasoning (1988), ch. 3.",
  named="independence is a triple property")

if __name__ == "__main__":
    import json, collections
    print(f"  registered objects: {len(REG)}")
    g = collections.Counter(v["grade"] for v in REG.values())
    for k, n in g.most_common():
        print(f"    {k:<14} {n}")
    print(f"  checkable from the construction: {sum(1 for v in REG.values() if v['check'])}")
    print(f"  carrying a standing name:        {sum(1 for v in REG.values() if v['named'])}")
    print(f"  UNNAMED:                         {sum(1 for v in REG.values() if not v['named'])}")
    json.dump(REG, open("mathreg.json", "w"), indent=1)

# --- entered from the seed, family, index and real-numbers work -------------

R('S.seed', 'G ⊆ X is a seed of X under ℛ iff φ̂(G) = φ̂(X)',
  'X closed; ℛ depends on G only through φ̂', ['A.env', 'A.R'], 'M §14.5.7; Birkhoff 1937; Moore 1910; Birkhoff 1937', 'PROVED', check='PRIOR ART: a generating set of a closure system is any G with cl(G) = cl(X). That the envelope alone decides it is the specific form here; the notion is Moore-Birkhoff.  PRIOR ART: a generating set of a closure system is any G with cl(G) = cl(X). That the ENVELOPE alone decides it is the specific form here; the notion is Moore-Birkhoff.', named='a seed')
R('S.cover', 'the minimum seed is a MINIMUM SET COVER: elements the envelope steps, sets the cells',
  'S.seed', ['S.seed'], 'M §14.5.9; Karp 1972; Johnson 1974', 'PROVED', check="PRIOR ART: MINIMUM SET COVER is one of the 21 NP-complete problems of Karp, Reducibility among combinatorial problems (1972); the greedy ln n approximation is Johnson, Approximation algorithms for combinatorial problems, JCSS 9 (1974) 256-278. The seed problem IS set cover, which is why five heuristics agree on 7 and the lower bound is 5.",
  named="the seed is a set cover")

R('S.lam', 'seed(Λ₈) = 7 exactly — 976 cells from seven, 139 to 1; LB 5, five heuristics 12/7/7/7/40',
  'branch and bound over 102 elements', ['S.cover'], 'M §14.5.9 / twoheur.py; Karp 1972; Johnson 1974', 'COMPUTED', check='PRIOR ART: the seed problem is minimum set cover, NP-complete (Karp 1972), with a greedy ln n approximation (Johnson 1974). Five heuristics agreeing on 7 against a lower bound of 5 is the measurement.', named="Λ's seed — seven cells")
R('S.down', 'a down-set over c values in d coordinates seeds at d + c − 1',
  'exact: LB = UB at d=4 c=4', ['S.cover'], 'M §14.5.9; Dilworth 1950', 'PROVED', check='PRIOR ART: the minimum generating set of a down-set is its set of maximal elements; the d + c - 1 count follows. Dilworth, A decomposition theorem for partially ordered sets, Ann. Math. 51 (1950) 161-166.', named='the down-set seed law, d + c − 1')
R('S.box', 'a full box c^d seeds at d + c − 2',
  'exact by branch and bound at 3³ and 4³', ['S.cover'], 'M §14.5.9; classical; Dilworth 1950; Dilworth 1950; Birkhoff 1937', 'PROVED', check='PRIOR ART: the corners of a d-dimensional box over c values generate it under coordinatewise max, and d + c - 2 is the count of extreme steps. Elementary.  PRIOR ART: as S.down, for a full box: the extreme steps in each coordinate generate it.  PRIOR ART: the generators of a down-set closed under coordinatewise max are its maximal elements; for a box over c values in d coordinates that count is d + c - 2. Dilworth, A decomposition theorem for partially ordered sets, Ann. Math. 51 (1950) 161-166; Birkhoff (1937) for the representation.', named='the box seed law, d + c − 2')
R('S.car', 'seed ≥ the Carathéodory number = the breadth = d for a product of d chains',
  'semilattice with subsemilattices as convex sets', ['S.cover'], 'Carathéodory / convexity spaces; Caratheodory 1911; Caratheodory 1911', 'CITED', check='PRIOR ART: Caratheodory, Ueber den Variabilitaetsbereich der Fourierschen Konstanten, Rend. Circ. Mat. Palermo 32 (1911) 193-217 — every point of a convex hull in R^d is a combination of at most d+1 points. Its lattice analogue is the breadth, and it bounds the seed below.  PRIOR ART: Caratheodory, Ueber den Variabilitaetsbereich der Fourierschen Konstanten, Rend. Circ. Mat. Palermo 32 (1911) 193-217 — every point of a convex hull in R^d is a combination of at most d+1 points. Its lattice analogue is the breadth, and it bounds the seed below.', named='the Carathéodory lower bound')
R('S.open', 'an open index is recovered as seed(ℛ(X)) plus the E cells ℛ(X) holds and X does not; cost seed + E',
  'exact on four open indexes; compresses only where E ≪ |X|', ['S.seed'], 'M §21.5; Moore 1910', 'PROVED', check='PRIOR ART: an open index needs its closure seed plus the cells the closure adds and it does not hold — the decomposition follows from extensivity.', named='the open-index form, seed + E')
R('A.r4', "ℛ₄, the four-orientation closure over Deville's staircase class",
  'idempotent, hence a closure operator', ['A.stair', 'A.R'], 'M §14.5.5; Deville et al. 1999', 'COMPUTED', check='PRIOR ART: the four orientations of a staircase constraint are the (alpha, beta)-monotone class of Deville, Barette & Van Hentenryck (1999); R uses one corner and R_4 the closure over all four.', named='the four-orientation operator')
R('A.orient', 'E − E₄, the ORIENTATION COST: 0 on eight of ten indexed objects, 2 on the audits, 750 on the parity rule',
  'ℛ₄ defined', ['A.r4'], 'M §14.5.5; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999', 'COMPUTED', check='PRIOR ART: the cost of choosing one orientation over the full class. The class is Devilles; the cost is measured here.  PRIOR ART: the four orientations of a staircase are the (alpha, beta)-monotone constraints of Deville, Barette & Van Hentenryck (1999). R uses one corner and R_4 the closure over all four; the ORIENTATION COST is the difference, measured at 0 on eight of ten indexed objects and 2 on the aufbau index.', named='orientation cost')
R('A.relax', 'ℛ is not a k-wise closure for any k: k-wise defect is 0 at k = d while E(ℛ) can be 750',
  '|Δℓ|=1 at 750 against k-wise 0 for k = 2,3,4', ['A.R'], 'M §14.5.4; Beeri, Fagin, Maier & Yannakakis 1983', 'PROVED', check='PRIOR ART: pairwise (k-wise) consistency implies global consistency exactly for ACYCLIC hypergraphs — BFMY, On the desirability of acyclic database schemes, J. ACM 30 (1983) 479-513. R is the global operator and the k-wise closures are the local ones; the gap between them is their theorem, and this object measures it.', named='ℛ as a relaxation')
R('A.staircls', "E(ℛ) = 0 iff X is an intersection of (≤,≤) staircases — one corner of Deville's class",
  'the anti-diagonal is a staircase with E = 750', ['A.relax', 'A.stair'], 'M §14.5.4; Deville, Barette & Van Hentenryck 1999; van Beek & Dechter 1995', 'PROVED', check='PRIOR ART: connected row-convex and monotone staircase constraint classes — Deville, Barette & Van Hentenryck, Constraint satisfaction over connected row-convex constraints, Artif. Intell. 109 (1999) 243-271; van Beek & Dechter, On the minimality and global consistency of row-convex constraint networks, J. ACM 42 (1995) 543-561.', named='the one-corner characterisation')
R('T.tight', 'the tight-pair count of a base is exactly 2S, S the envelope-step count',
  "van Beek & Dechter's measure", ['A.env'], 'M §14.5.9; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999', 'COMPUTED', check='PRIOR ART: the tight pairs of a staircase constraint are its envelope steps — Deville, Barette & Van Hentenryck, Artif. Intell. 109 (1999) 243-271.  PRIOR ART: the tight pairs of a staircase constraint are the points where its envelope steps — Deville, Barette & Van Hentenryck (1999). That the count is exactly 2S for S the envelope-step count is the measurement.', named='constraint tightness as a count')
R('F.moore', 'the ℛ-closed subsets of a closed index form a Moore family: ∩-closed 100%, ∪-closed 33–68%; 73, 146, 731 members',
  'exhaustive at 8, 9, 16 cells', ['S.seed'], 'M §14.5; Moore 1910; Ward 1942', 'PROVED', check='PRIOR ART: the closed sets of a closure operator form a Moore family — intersection-closed with a top. Moore, Introduction to a Form of General Analysis (1910); Ward, The closure operators of a lattice, Ann. Math. 43 (1942) 191-196. That the R-closed subsets of a closed index form one is that theorem applied at one level up.', named='the family of closed sets')
R('F.open', 'THEOREM: the family of all closed indexes is itself an OPEN index — E = 182, 365, 64,804',
  'every member has E = 0', ['F.moore'], 'M §14.6; Tarski 1955; Ward 1942', 'PROVED', check='PRIOR ART: the lattice of closed sets of a closure operator is complete (Tarski, A lattice-theoretical fixpoint theorem, Pacific J. Math. 5 (1955) 285-309), but completeness is not the same as being CLOSED under the same operator one level up. That the family of closed indexes is itself open is measured here; the setting is Tarski-Ward.', named='the family theorem')
R('F.unstatable', 'and it cannot be stated: a closed index has a seed, an open one costs seed + E, and E is 64,804 at 16 cells',
  'corollary of F.open and S.open', ['F.open', 'S.open'], 'M §14.6.1; Kolmogorov 1965', 'PROVED', check='PRIOR ART: the cost of stating an object is its description length — Kolmogorov, Three approaches to the quantitative definition of information, Probl. Inf. Transm. 1 (1965) 1-7. A closed index has a seed; an open one costs seed plus defect, and the difference is the statement cost.', named='the unstatable family')
R('G.cons', "Λ's seven constraints form a TREE — 8 nodes, 7 edges — with ZERO of 35 triples spanning three nodes",
  'no 3-body among the constraints', ['L.c1'], 'M §21.5.2; Freuder 1982; Dechter & Pearl 1989', 'COMPUTED', check='PRIOR ART: that a tree-structured constraint graph is globally consistent after arc consistency is Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982) 24-32; the width/induced-width machinery is Dechter & Pearl, Tree clustering for constraint networks, Artif. Intell. 38 (1989) 353-366.', named='the constraint index')
R('G.near', 'Λ is one edge from a 3-body in exactly seven places, one per existing edge',
  'every one a bond the physics does not make', ['G.cons'], 'M §21.5.2; Berge 1962', 'COMPUTED', check='PRIOR ART: adding one edge to a tree creates exactly one cycle; the number of places is the number of existing edges. Berge, Theorie des graphes (1958/1962).', named='the seven near-misses')
R('G.tower', "the tower's cycle rank rises by one at each two-parent axis — 0,0,1,1,2,2 — while triangles stay 0",
  'the tree breaks at Λ₁₀', ['G.cons', 'T.tower'], 'M §21.5.2; Berge 1962', 'COMPUTED', check='PRIOR ART: the cycle rank |E| - |V| + c is the first Betti number of a graph — Berge, Theorie des graphes et ses applications (1958/1962). That it rises by one at each two-parent axis is the measurement.',
  named="the cycle rank of the tower")

R('K.transit', 'the transit profile MI/H = 0.51, 0.93, 0.08, 0.13, 0.77 at Λ₉–Λ₁₃: reduced at 10, a label through 11 and 12, re-attaching at 13',
  'Λ₁₂ built with the loose bound', ['T.tower'], 'M §12.11; Shannon 1948', 'COMPUTED', check='PRIOR ART: MI/H is the normalised mutual information, standard since Shannon (1948).', named='the transit profile')
R('L.real', "Λ's eight constraints on 247 real subshells across ALL 118 elements incl. 19 anomalies and 15 predicted superheavies: 18,288 tests, 0 failures",
  'IUPAC ground states', ['L.c1'], 'close_L.py; Madelung 1936; NIST', 'COMPUTED', check='PRIOR ART: the 247 real subshells across 118 elements are the observed ground configurations, tabulated by NIST; the ordering is Janet-Madelung. Testing Lambda constraints against them checks the index, not the table.',
  named="the index against the real subshells")

R('T.real', 'the four coupling bounds on the exact term structure of every subshell: 85,829 tests, 0 failures',
  'ℓ = 0..3, k = 1..4ℓ+2', ['T.a9'], 'microstate enumeration; Condon & Shortley 1935', 'COMPUTED', check="PRIOR ART: the exact term structure of every subshell is tabulated in Condon & Shortley (1935), ch. VII, and in the NIST compendium. The 85,829 tests check the four coupling bounds AGAINST that table; the table is not this work.",
  named="the bounds against real terms")

R('E.table', "the periodic table's 36 decompose 25 + 11, not 26 + 10; E is placement-sensitive, 36 at group 18 and 20 at group 2",
  'all 118 elements', ['A.env'], 'M §6.1.1; Mendeleev 1869; Janet 1929', 'COMPUTED', check='PRIOR ART: the periodic tables arrangement is Mendeleev, Ueber die Beziehungen der Eigenschaften zu den Atomgewichten der Elemente, Z. Chem. 12 (1869) 405-406; the left-step form on n+l is Janet (1929). That E is placement-sensitive is a statement about which arrangement, not about the elements.', named='the thirty-six decomposed')
R('E.layout', "hydrogen's placement is free and helium's costs 16, and they are not additive: −16 and 0 apart, −1 together",
  'E set by the largest group used in period 1', ['E.table'], 'M §6.1.1; Janet 1929', 'COMPUTED', check='PRIOR ART: hydrogen and helium are the classic placement anomalies of the periodic table, and Janets left-step form resolves them differently from the classroom table. The cost measured here is of the CHOICE.', named='the price of a layout')
R('G.prot', 'the 24 protocols occupy 19 cells in four coordinates; §2.8 and §2.24 share one',
  '§2.24 is §2.8 specialised to heuristics', ['G.reg'], 'protindex.py; Freuder 1978', 'COMPUTED', check='PRIOR ART: as G.allcons, applied to the protocol index.', named='the protocol index')

R("F.exact", "ℛ(Cl(U)) = 2^U, so E(Cl(U)) = 2^|U| − |Cl(U)| exactly",
  "Cl(U) holds ∅ and U, and every ordered pair of points is separated by some closed set, "
  "making every envelope constant at 1", ["F.open"], "M §14.6.2; Moore 1910", "PROVED",
  check="PRIOR ART: the closure of a set of generators over an unconstrained alphabet is the full power set, so the defect is the exact complement count. A corollary of extensivity and idempotence.", named="the family's defect, exactly")
R("G.shape", "the constraint graph's shape decides the seed: path 8, star 6, balanced trees 6, forest 5 "
  "on six nodes over one alphabet; neither extreme is cheapest",
  "seed is monotone in S with no exception, all six exact by branch and bound",
  ["S.cover", "G.cons"], "M §21.5.4; Freuder 1982; Dechter & Pearl 1989", "COMPUTED", check="PRIOR ART: that the constraint graph shape decides what a local method achieves is Freuder 1982 for trees and Dechter & Pearl 1989 for the general induced-width bound.", named="shape decides the seed")
R("G.graph", "Λ₁₃'s constraint graph: 12 nodes, 13 edges, girth 5, diameter 6, radius 3, treewidth 2, "
  "hub k at degree 4, cycle rank 2, no triangle at any stage",
  "treewidth 2 at Λ₁₃ keeps Freuder's bound and §21.5.1's one-level shortfall",
  ["G.cons"], "M §21.5.3 / Figure 21.1; Euler 1736; Diestel 2017", "COMPUTED", check="PRIOR ART: girth, diameter, radius and treewidth are standard graph invariants — see Diestel, Graph Theory (5th ed., 2017). Graph theory itself begins with Euler, Solutio problematis ad geometriam situs pertinentis (1736).", named="the constraint graph")

R("G.allcons", "every genuine constraint in the book, indexed over five coordinates: 22 carried by ℛ, "
  "2 by ℛ₄, NONE by neither; E = 21, E₄ = 6, orientation cost 15",
  "eight rows of a first attempt were coordinate systems entered as constraints; the two that no "
  "operator carried were both of those",
  ["A.r4", "G.cons"], "M §21.5.5 / allcons.py; Freuder 1978", "COMPUTED",
  check="PRIOR ART: indexing constraints by the coordinates they name is the constraint-hypergraph view — Freuder, CACM 21 (1978) 958-966.", named="the index of all constraints")
R("E.nuclide", "the measured nuclide chart indexed by (Z, N) closes at E = 9, stable across four "
  "proton-number cutoffs; the nine cells are the mass formula's pairing and clustering terms",
  "cells named at one cutoff persist at every larger one", ["A.env"], "M §6.2; Segre 1945", "COMPUTED",
  check="*** COUNT NOT REPRODUCED 2026-08-11 (R 1550). *** AME2020 Table I was captured from the published paper (Chin. Phys. C 45, 030003, Table I, 3558 rows, Z = 0-118, A = 1-295) and E recomputed with the same operator: E = 2, NOT 9, and stable at 2 across cutoffs Z <= 20, 50, 82, 92 and 118. Six variants of the cell set were tried - axes swapped, neutron excluded, measured-only, Z and N both positive - and none gives 9; measured-only gives 95. WHAT DOES REPRODUCE: the STABILITY across cutoffs, the cells being NAMEABLE PHYSICS, and the reading of them as the mass formula pairing term - the two defect cells are the empty cell (0,0) and Z=2 N=0, THE DIPROTON, which is unbound and is the textbook pairing failure. Three of four claims hold and the number does not. Cause UNDETERMINED: a different source edition, a different inclusion rule, or an arithmetic error in the original. PRIOR ART: the chart of nuclides indexed by (Z, N) is Segres chart, in use since the 1940s.", named="the nuclide chart's defect")
R("E.ioniz", "first ionisation energies given to the bracket as bare numbers refuse at Be→B, N→O, "
  "Mg→Al and P→S — four steps of twelve, 67% admissible",
  "the same two positions in both periods: the s2-p1 subshell opening and the p3-p4 first pairing",
  ["B.brk"], "M §6.2; Mendeleev 1869; NIST", "COMPUTED", check="PRIOR ART: first ionisation energies as a periodic property date to Mendeleev; the values are NISTs. That bare numbers refuse the bracket is a statement about what a bracket needs, not about the data.", named="the refusal map")

R("A.erel", "E = 0 is relative to coordinates: any X with |X| = a·b relabels onto an a × b rectangle, "
  "which is a full box and closed — so every index with a composite cell count has a coordinate "
  "system in which E = 0",
  "the coordinates must be fixed by the subject, not chosen; every coordinate in this book is",
  ["A.R"], "M §21.6; Birkhoff 1940; Birkhoff 1937; Dushnik & Miller 1941", "PROVED", check="PRIOR ART: E = 0 is a statement about a COORDINATISATION, not a set. Any set of size ab relabels onto an a x b grid, which is closed. This is the standard observation that lattice properties are not invariants of the underlying set.  PRIOR ART: a lattice property belongs to a COORDINATISATION and not to the underlying set — the same reason order dimension is not an invariant of cardinality. Birkhoff (1937); Dushnik & Miller, Partially ordered sets, Amer. J. Math. 63 (1941) 600-610.", named="E is coordinate-relative")
R("A.define", "a rung-1 coordinate contributes no envelope: same cells, box, E, envelope-step count "
  "and seed with or without it — it is invisible to ℛ and still counts as a letter",
  "it is the index's own name carried as a coordinate, taking one value because the object is what "
  "does not vary in it", ["A.env"], "M §21.6.1; Birkhoff 1937", "PROVED",
  check="PRIOR ART: a coordinate with a single value contributes no join-irreducible, so it changes neither the lattice nor its envelopes.", named="the defining letter")
R("W.face", "the companion's local null surface is a FACE of the 6-cube, not a parity class: 32 of 64 "
  "with every rung 2, and a parity class gives E = 32 where the printed E is 0",
  "deducible from three printed numbers with no access to any cell; THETA = 0 at 16 and STAT = 0 at 8 "
  "nest Killing horizons inside non-expanding ones", ["A.R"], "T §10.1, §10.4; Coxeter 1948", "COMPUTED",
  check="PRIOR ART: a face of the n-cube is the set fixing some coordinates and freeing the rest — Coxeter, Regular Polytopes (1948), ch. VII. A parity class is not a face, which is what distinguishes them here.", named="the null surface is a face")

R("S.core", "four of the seed's seven cells are NECESSARY: each uniquely covers 12-23 envelope "
  "elements and has ZERO alternatives in Lambda; they cover 87 of 102",
  "a stable attractor of greedy covering, not necessity; §14.5.7 stands unamended (register 600)",
  ["S.lam"], "M §14.5.10; Karp 1972; Chvatal 1979", "COMPUTED", check="PRIOR ART: an element covered by exactly one set forces that set into every cover — the standard reduction rule for set cover.  PRIOR ART: an element covered by exactly one set forces that set into every cover — the ESSENTIAL-SET reduction rule of set-cover preprocessing. Chvatal, A greedy heuristic for the set-covering problem, Math. Oper. Res. 4 (1979) 233-235; Karp (1972) for the problem, Lovasz, On the ratio of optimal integral and fractional covers, Discrete Math. 13 (1975) 383-390 for the LP bound. Four of the seven seed cells are forced this way, and that is the measurement.", named="the seed's necessary core")
R("S.erasure", "the remaining three seed positions admit 519 completing triples over 66 distinct "
  "cells, none in all 519, each appearing in 3 to 157 — a redundancy gradient of fifty to one",
  "heavy-tailed: min 3, median 12, max 157, a ratio of thirteen to one",
  ["S.core"], "M §14.5.11; Karp 1972", "COMPUTED", check="PRIOR ART: the alternative completions of a partial cover; the count is the measurement.", named="the seed is an erasure structure")
R("G.stat", "statistics is a sixth language: max-entropy closure on the pairwise marginals recovers "
  "Lambda at 976, E = 0, restores a deleted cell, and GROWS on an added one, 976 to 1,048",
  "its signature matches the information language, not order/geometry/analysis; the five split "
  "three-two between absorbing and growing",
  ["A.R"], "M §20 / stat_lang.py; Deming & Stephan 1940; Csiszar 1975", "COMPUTED", check="PRIOR ART: the max-entropy distribution matching given marginals is reached by iterative proportional fitting — Deming & Stephan, Ann. Math. Stat. 11 (1940) 427-444; its information-geometric characterisation is Csiszar, I-divergence geometry, Ann. Prob. 3 (1975) 146-158.", named="statistics as a language")

R("S.channel", "six channel conditions hold in all 219 minimum covers of Lambda-8: an s-s, s-p, p-s "
  "and p-p transition, a null transition q = 0, and a full transfer q = k",
  "the constraint is on the CHANNEL, not the cell — which is why every cover looks alike while "
  "nothing is forced", ["S.core"], "M §14.5.12; Condon & Shortley 1935", "COMPUTED",
  check="PRIOR ART: the s-s, s-p and related conditions are statements about which subshell transitions the seed must contain; the subshell structure is Condon & Shortley (1935).", named="the channel conditions")
R("S.unit", "all 219 covers contain a cell matching (3,0,1,1,*,0,1,1) — 3s1 to e-s ending 1, doublet, "
  "e free at 1 or 3; its function is to carry the value ONE where the corners carry extremes",
  "three of the fifteen elements the corners miss are the alphabet values q=1, g=1, 2S=1; e=3 "
  "witnesses the target's ceiling and e=1 the source's",
  ["S.channel"], "M §14.5.13; Karp 1972; Chvatal 1979", "COMPUTED", check="PRIOR ART: a cell present in every minimum cover is forced; the standard set-cover argument.  PRIOR ART: a set present in every minimum cover is forced by an element it uniquely covers — the same reduction rule. Chvatal (1979). That all 219 covers contain this cell is the measurement.", named="the unit cell")
R("S.bits", "the five read as binary: corners 1 and 2 are exact complements (3 of 3), corner 3 and "
  "the unit cell are exact complements (3 of 3), corner 4 is fully specified at 11001100, and every "
  "coordinate receives both a 0 and a 1 with no column one-sided",
  "measured at one cap setting only; whether the pairing survives other caps is untested",
  ["S.unit"], "M §14.5.14; Shannon 1938", "COMPUTED", check="PRIOR ART: reading a structure as binary words with complementation is Boolean algebra — Shannon, Trans. AIEE 57 (1938) 713-723.", named="the seed as binary")

R("K.twocol", "an index has a time column exactly when its cells are moves: Lambda-8 976/0, "
  "Lambda-9 1,654/1,169, the companion's index 2,370/1,410, while the periodic table and the "
  "calendar have no second column and cannot have one",
  "a transition cell has two ends so composability is askable; a state cell has one position and "
  "the question does not arise",
  ["K.cat"], "M §12.11.1.3; Mac Lane 1971", "COMPUTED", check="PRIOR ART: an index has a composition structure exactly when its cells are morphisms rather than objects — the distinction is the category axioms. Mac Lane (1971). CORRECTED 2026-08-11: this statement printed Lambda-8 as 976/491. It is 976/0. The generated table in INDICES.md gives 0 with fraction 0.0000, indices.py says 'Lambda-8 composes not at all — four source coordinates against three target', and K.window states the reason as a dependency: 'Lambda-8 target has 3 coordinates against 4', so tgt(a) = src(b) is not even askable at Lambda-8 and Lambda-9 is the FIRST composable level. The 491 was a hand-authored figure in an object graded COMPUTED, contradicting the computation it depends on.",
  named="space is what an index holds, time is what it composes")
R("K.jump", "the axis that makes the tower a category is worth twenty points: Lambda-8 is 50.3% "
  "composable and Lambda-9, adding 2S' <= g, is 70.7%",
  "the companion's index sits between them at 59.5% — three transition indexes, three fractions, "
  "so this is not a norm",
  ["K.twocol"], "M §12.11.1.3; Mac Lane 1971", "COMPUTED", check="PRIOR ART: the axis that closes composition is the one that supplies identities and associativity — the category axioms. What is priced is the cell cost of adding it.", named="the categorial jump")

R("K.redun", "redundancy under R rises with the number of INDEPENDENT coordinates; a DERIVED coordinate lowers it",
  "a closed index X of dimension d", ["A.R"], "R 1119-1122; Shannon 1948", "MEASURED",
  check="Lambda PROJECTED onto its own first d coordinates, same constraints: d=8 gives 61% removable with exact recovery, d=7,6,5 give 30%, d=4 gives 5%, d=3 gives 0%. And adding the electron count Ne = Z-c+1 to the spectra index — a FUNCTION of two coordinates it already has — drops redundancy from 20% to 0% while doubling the envelopes and raising coupling 17% to 33%  PRIOR ART: redundancy is the excess of a representation over its entropy. That it rises with the number of INDEPENDENT coordinates is the measurement; the notion is Shannon (1948).",
  named="the projection ladder")
R("A.S", "the STEP operator: for each coordinate direction, the ratio between adjacent VALUED cells, its median and its scatter; a direction earns a step when the scatter is tight enough to carry a value",
  "an index whose cells carry values", ["A.R"], "R 1132-1137; Edlen 1964", "MEASURED",
  check="derived unaided from the spectra index it finds iso at s (1.233, scatter 1.13, 43 pairs), iso at p (1.185, 1.16, 25) and l at s (1.416, 1.43, 62). It must be derived from MEASURED cells ONLY: re-deriving from the walked result tightens iso at s to 1.08 on 116 pairs, because the walked values were generated by that step, and the step count goes 3 to 8  PRIOR ART: measuring a step as the ratio between adjacent valued cells is the isoelectronic and isonuclear method of Edlen, Atomic spectra, Handbuch der Physik XXVII (1964) 80-220.",
  named="the step operator")
R("A.W", "the VALUATION closure: every cell reachable from a valued one by steps in S, accumulated error below a threshold, by the least-error route",
  "an index, a step set S, and a tolerance", ["A.S"], "R 1132-1136; Dijkstra 1959", "PROVED",
  check="EXTENSIVE and IDEMPOTENT with exactly zero drift, since the least-error route from the seed leaves nothing tighter to find. MONOTONE except at one cell in 1,345: Mg II ni is measured at +0.0000, the Seaton step is multiplicative, and zero blocks a route a walked positive value would open — so adding a measurement can REMOVE a walked cell  PRIOR ART: the valuation closure is a shortest-path closure over a multiplicative cost. Extensivity, idempotence and monotone-except-at-zero follow from Dijkstra (1959).",
  named="the walk")
R("A.anchor", "REDUNDANCY ANCHORING: keep every route to a cell, not the best one; the spread between independent arrivals MEASURES the error rather than estimating it",
  "a valuation closure with more than one route to a cell", ["A.W"], "R 1136; Gauss 1809", "MEASURED",
  check="956 cells of the spectra index are reached by two or more distinct routes. Observed spread 1.05 against a propagated estimate of 1.14 — ratio 0.92, so the walk's error bars are honest and slightly conservative. The check comes from the index disagreeing with itself, not from an outside formula  PRIOR ART: keeping every route to an estimate and reading their SPREAD as the error, rather than taking the best route, is the method of combining independent determinations — Gauss, Theoria motus corporum coelestium (1809), sec. 3.",
  named="the anchor")
R("A.EW", "E_W(X) = |W(X)| - |X|: the METRIC defect, what the steps reach and the index has not valued; distinct from E(X) = |R(X)| - |X|, the ORDINAL defect",
  "an index whose cells carry values", ["A.W","A.R"], "R 1133; Dijkstra 1959", "DEFINITIONAL",
  check="for Lambda E_W is empty, because a cell of Lambda is an arrangement and carries no number — which is why the book needed only E. For Lambda_spectra the two differ, and the gap between them is the cells that are placed and unvalued  PRIOR ART: the reachable set under a step relation, with accumulated cost and a least-cost route, is single-source shortest paths — Dijkstra, A note on two problems in connexion with graphs, Numer. Math. 1 (1959) 269-271.",
  named="the metric defect")
R("A.logic", "LOGIC is not a language: it is the mechanism binary -> language -> binary by which any language answers a question about a cell",
  "a language with a closure operator", ["A.R"], "R 1173; Boole 1854; Tarski 1936", "DEFINITIONAL",
  check="three levels: BINARY is the type, a cell is admitted or not; a LANGUAGE is a coordinate system with a closure operator; LOGIC is the map. A language earns a row when logic can operate on it and return a binary, which is why documentary has none — it returns a citation. The book's C(5,2) = 10 combinations is then exact: five operator-bearing languages, plus statistics as a sixth and documentary as a seventh  PRIOR ART: that logic is the mechanism by which a language answers a binary question, rather than a language itself, is the object-language/metalanguage distinction — Boole, An Investigation of the Laws of Thought (1854); Tarski, Der Wahrheitsbegriff in den formalisierten Sprachen, Studia Philos. 1 (1936) 261-405.",
  named="the logic level")
R("A.stat2", "the statistics operator is max-entropy on the PAIRWISE marginals, not the first-order ones",
  "an index of dimension d >= 3", ["A.logic"], "R 1174", "MEASURED",
  check="on Lambda, first-order marginals admit all 6,912 ambient cells; pairwise marginals admit exactly 976 and reproduce R cell for cell. IPF converges to the max-entropy distribution matching the SPECIFIED marginals (Deming and Stephan 1940; Ireland and Kullback 1968), so which marginals is the whole question",
  named="the statistics operator")
R("K.three", "an index needs THREE coordinates before its languages can disagree",
  "an index and two languages", ["A.stat2"], "R 1175; Beeri, Fagin, Maier & Yannakakis 1983", "PROVED",
  check="at d = 2 there is one coordinate pair, so pairwise consistency and the cell coincide and every language returns the same answer. The periodic table, Janet and the calendar were all tested at two and all reported agreement; rebuilt at three — with block, l and weekday, each non-monotone in the second coordinate — the periodic table gives order E = 100 against statistics 0, reproducing the book's recorded caveat. All three match the book at 2-D first: 36, 0 and 7  PRIOR ART: pairwise consistency is a statement about PAIRS, so an object with one pair cannot make it. BFMY (1983) for the general local-to-global framework.",
  named="the three-coordinate rule")
R("K.langclose", "E(X) = 0 if and only if the languages agree",
  "an index of dimension >= 3 and two or more operators", ["K.three"], "R 1176; Beeri, Fagin, Maier & Yannakakis 1983", "MEASURED",
  check="six indexes, three operators — order, statistics, geometry. Lambda and a box ordering: E = 0 and every pair agrees, 0 cells differing. The periodic table, Janet, the calendar and Lambda_spectra: E > 0 and every pair differs. No exception. Closure is therefore a language-theoretic property as well as an order-theoretic one, and the language test is cheaper: R enumerates the ambient product, pairwise consistency needs only the marginals  PRIOR ART: global and local closures coincide exactly on acyclic structures — BFMY, J. ACM 30 (1983) 479-513. That E = 0 iff the languages agree is that theorem read as an equivalence.",
  named="closure as agreement")
R("K.corner", "the whole-object defect decomposes into FACES and CORNERS, and the corners are an artefact of loose coordinatisation",
  "an index of dimension d and its d-1 axis slices", ["K.langclose"], "R 1177; Freuder 1978", "MEASURED",
  check="of the 6,195 cells R admits and Lambda_spectra does not hold, 3,993 are admitted by some three-axis slice and 2,202 by none. Statistics admits ONE of the 2,202 and geometry 28%, against 20% and 70% of the faces. And every available fifth coordinate makes the corners worse — by 70% to 652% — because all four candidates are DERIVED (register 1122)  PRIOR ART: cells admitted by the full closure and by no lower-arity projection are exactly the k-consistency gap — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966.",
  named="corners and faces")
R("K.produce", "an axis PRODUCED by another gives a dimension exactly when its production is NOT MONOTONE",
  "a closed index and an axis derived from its coordinates", ["K.axis"], "R 1143; Birkhoff 1937", "MEASURED",
  check="multiplicity is produced by Ne and cycles 2,{1,3},2,{1,3},{2,4} — NOT monotone — and adding it takes redundancy from 20% to 82%. Ne is produced by (Z,charge) and monotone: 0%. n0 is produced by (Z,charge,l) and monotone: 0%. R's envelopes are cumulative maxima, so a monotonically-produced axis is already inside them; a non-monotone one is invisible to them. This resolves the apparent contradiction between R 1122 and R 1123  PRIOR ART: a monotone function of existing coordinates adds no join-irreducibles and so no dimension; a non-monotone one does. Birkhoff (1937).",
  named="the production rule")
R("Q.delta", "delta = [ B - q e^(-a(Ne)l) e^(k/Ne) c^g + P ] (1 + s [triplet]): a closed form for any Rydberg channel from atomic-index quantities alone",
  "a Rydberg channel (Z, charge c, l, multiplicity)", ["Q.bound","Q.pen","Q.pol","Q.exch"], "R 1145-1168; Seaton 1958; Fermi 1928; Pauli 1925", "MEASURED",
  check="311 measured channels: rms 0.2449, R^2 0.924, median |error| 0.090. By l: s 0.283, p 0.276, d 0.280, f 0.119, g 0.0096. Against TWELVE published values never fitted on: median error 0.00155 at l >= 3 and 0.368 below. 50% within 0.090, 90% within 0.414, 99% within 0.826  PRIOR ART: the superseded form of the channel equation. Its terms are the Pauli bound (Pauli 1925), the Thomas-Fermi deficit (Fermi 1928) and Seaton polarisation (1958). Superseded by Q.final at register 1205.",
  named="the channel equation")
R("A.intext", "E is INTERIOR and E_W is EXTERIOR: the order operator is bounded by its sample and the step operator is not",
  "an index with valued cells and a step set", ["A.E","A.EW"], "R 1196-1199; Beeri, Fagin, Maier & Yannakakis 1983; Dijkstra 1959", "MEASURED",
  check="on Lambda_spectra in-region, R places 1,925 from 277 held (E = 1,648) and W values 277 (E_W = 0) at the book's tolerance, because every step's scatter exceeds it — multiplicity 1.664, isoelectronic 1.674, l 2.872. Raising tau does not close the gap: every cell W gains, R mostly refuses, and ALL 218 fail one envelope, charge given Z. The measured set runs Z 2-83 and charge 1-9; the refused cells run Z 1-85 and charge 1-10. The overlap never exceeds 12% of E at any tolerance  PRIOR ART: the order operator is a closure bounded by its sample (BFMY 1983 for what local closure can reach); the step operator is a reachability closure unbounded by it (Dijkstra 1959). That E is interior and E_W exterior follows from the two being different kinds of operator.",
  named="interior and exterior")
R("A.three", "the Method equation partitions an index into three populations: interior captures, the working overlap, and exterior predictions",
  "an index, its order operator and its step set", ["A.intext"], "R 1199-1200; Freuder 1978; Dijkstra 1959", "MEASURED",
  check="at tau = 3.0: INTERIOR 1,503 cells R places and no step values, median l = 2 and charge 4 — these are captures. BOTH 145 placed and valued, median l = 3, the polarisation regime. EXTERIOR 218 the steps reach past the sample edge. The exterior verifies where it reaches: Cs I np walked to 3.659 against a measured 3.5667, an error of 2.6% with a stated error factor of 1.67  PRIOR ART: partitioning by what a closure admits and what a propagation reaches — the k-consistency gap (Freuder 1978) crossed with shortest-path reachability (Dijkstra 1959). The three populations are the measurement.",
  named="the three populations")
R("Q.anchor", "anchoring the equation at BOTH ends of Z fixes the extrapolation at almost no in-region cost",
  "the channel equation and a far-field literature value", ["Q.region","Q.collapse"], "R 1201-1205; Theodosiou, Inokuti & Manson 1986", "MEASURED",
  check="seven far anchors — Cs I np measured at 3.5667, and Th/Ac ns, np, nd, nf from actinide theory at 5.2, 4.75, 3.8, 2.0 — extend the sample from Z <= 83 to Z = 90. Far-anchor median error falls 0.754 to 0.064, a factor of twelve; in-region rises 0.0637 to 0.0665. The saturating exponent returns for real: e(Ne) = 0.8297 - 0.0900 ln Ne against -0.0266 from the in-region sample alone. CAVEAT: four of the seven anchors are THEORETICAL, so the high-Z arm is calibrated against another calculation and moves if that is revised  PRIOR ART: asymptotic quantum defects for all ionisation stages of all ions with Z <= 50 are tabulated in Theodosiou, Inokuti & Manson, At. Data Nucl. Data Tables 35 (1986) 473-486, Hartree-Slater. The far anchors used here are Cs I np (measured) and actinide values from arXiv:2508.06733.",
  named="the two-ended anchor")
R("Q.final", "delta = a p^e(Ne) Ne^k ln(c+1)/c where p > 0, and h C(Z) ((Ne-1)/Ne) Ne^k ln(c+1)/c where p = 0",
  "any Rydberg channel (Z, charge, l, multiplicity)", ["Q.anchor","Q.bound"], "R 1205-1206; Seaton 1958; Fermi 1928; Janet 1929", "MEASURED",
  check="a = 0.3772, e(Ne) = 0.8297 - 0.0900 ln Ne, k = 0.4942, h = 0.5415. 284 channels from Z = 2 to 90 and charge 1 to 10: rms 0.1610, R^2 0.9741, l >= 4 rms 0.0150, hydrogenic output EXACTLY zero, Pauli bound 328/328, one l-ordering violation against a measured zero. Four fitted numbers and every input from the ground state or the periodic table. It values all 1,648 cells R places, where the walk valued none  PRIOR ART: every term of the form has a source. The ln(c+1)/c charge dependence is the isoelectronic behaviour of Edlen 1964; the Ne^k factor is Thomas-Fermi (Fermi 1928); p is the Pauli orbital count (Pauli 1925); C(Z) is orbital collapse (Griffin, Andrew & Cowan 1969) at the Janet boundary (Janet 1929). The equation assembles them; it does not introduce any.",
  named="the channel equation")
R("Q.bound", "B = min( p , n0 - l - 1 ): the integer part's exceptionless upper bound, from aufbau alone",
  "a channel and its core's ground configuration", ["S.ground"], "R 1141; Pauli 1925; Janet 1929", "PROVED",
  check="floor(delta) <= B for 311 of 311 measured channels. As an equality it is right 57%; every error is negative; within two of the bound, 303 of 311. p is the core's orbital count at that l and n0 the first Pauli-allowed n, both from aufbau with no spectrum  PRIOR ART: the bound counts core orbitals of the same l and the first Pauli-allowed principal number, both read from the ground configuration. Paulis exclusion principle, Z. Phys. 31 (1925) 765-783, fixes the occupancies; Janets n+l ordering (1929) fixes which subshells are filled.",
  named="the Pauli bound")
R("Q.pen", "the penetration deficit, -q e^(-a(Ne) l) e^(k/Ne) c^g, with a(Ne) = a0 + a1 Ne^(-1/3)",
  "a channel below the polarisation regime", ["Q.bound"], "R 1147; Hartree 1928; Fermi 1928", "COMPUTED",
  check="the decay a is set by the atom's SIZE: a against ln Ne gives r^2 = 0.437 across 56 species, against electrons-beyond-closure 0.143, against charge nothing (p = 0.34). K I's measured d/s ratio implies a = 1.03, Sr I's implies 0.157 — a factor of seven, and a universal a fits neither  PRIOR ART: the penetration deficit and its Ne^(1/3) scaling are the Thomas-Fermi picture — Fermi, Eine statistische Methode zur Bestimmung einiger Eigenschaften des Atoms, Z. Phys. 48 (1928) 73-79; Hartrees self-consistent field, Proc. Camb. Phil. Soc. 24 (1928) 89-110, gives the orbital form. Fermi 1928 applied it to Rydberg corrections directly.",
  named="the deficit term")
R("Q.pol", "the polarisation term, 3 alpha c^2 / K(l) for l >= 4 with alpha from Lambda_alpha, K(l) = l(l+1)(2l-1)(2l+1)(2l+3)",
  "a non-penetrating channel and a core polarisability", ["A.seaton","Q.alpha"], "R 1165-1168; Seaton 1958; Born & Heisenberg 1924", "CITED",
  check="Seaton's formula. With alpha supplied as a species LABEL from Lambda_alpha rather than a universal constant, the l >= 4 rms falls from 0.01504 to 0.00958 — 36%. Below l = 4 it must be gated OFF: applied at s and p it drives the fit to rms 39.3 because K(l) is small there  PRIOR ART: the polarisation term 3 alpha c^2 / K(l) is Seaton (1958); the physical origin is core polarisability, Born & Heisenberg, Z. Phys. 23 (1924) 388-410. SUBSUMED at register 1204 by the Janet collapse coordinate.",
  named="Seaton's term")
R("Q.exch", "the exchange factor (1 + s [triplet]), s = -0.0782",
  "a channel of a two-valence-electron system", ["Q.bound"], "R 987, withdrawn R 1168", "ASSERTED",
  check="WITHDRAWN (R 1168). The claim was that the fitted s recovers register 987's sign and size. It does not: register 987 measures the triplet defect EXCEEDING the singlet in 22 of 22 ns cases, and the additive fit returned s = -0.0782, the right magnitude and the WRONG SIGN. Cross-checked on 66 singlet/triplet pairs the equation gets 33, exactly chance. The parameter absorbed something else  PRIOR ART: the exchange splitting between singlet and triplet is Heisenberg, Mehrkoerperproblem und Resonanz in der Quantenmechanik, Z. Phys. 38 (1926) 411-426; that the higher multiplicity lies lower is Hund first rule (1925). WITHDRAWN at register 1168: the fitted sign is opposite to the measured one.",
  named="the exchange factor")
R("Q.bridge", "the bridge between the metric and ordinal descriptions is MULTIPLICATIVE with a REGIME factor: every factor positive so each preserves rank by itself, and the regime factor differs between two channels only when they differ in regime",
  "a channel equation required to respect both values and orderings", ["Q.delta","S.regime"], "R 1169-1171; Pareto 1896; Pareto 1896; Spearman 1904", "MEASURED",
  check="an additive fit gets P.lcollapse 102/205 against a measured 194 — chance. A purely multiplicative fit gets 205/205, 143/143, 66/66 where the measurements give 194, 89, 55 — it cannot represent an exception because a product of positives is monotone in each factor. With a regime factor: 204/205, 129/143, 61/66, and ln-R^2 improves 0.8026 to 0.8164  PRIOR ART: that a multiplicative form preserves rank and an additive one does not is elementary; that no single form does both well is a Pareto statement about the two objectives.  PRIOR ART: a product of positive factors is monotone in each and so preserves rank; a sum of signed terms need not. Rank preservation as an objective distinct from least squares is Spearman, The proof and measurement of association between two things, Amer. J. Psychol. 15 (1904) 72-101. That no single form does both well is a Pareto statement (1896).",
  named="the bridge equation")
R("A.blind", "each language is blind in its own way: statistics cannot state a closure defect, analysis cannot state an ordering, a multiplicative algebra cannot state an exception",
  "an index described in more than one language", ["Q.bridge"], "R 1169; Shannon 1948; Freuder 1978", "MEASURED",
  check="register 761 established the first. The second: least squares minimises squared error and has no rank in it — an equation fitting 311 values to R^2 = 0.924 got every ordering wrong. The third: a product of positive factors is monotone in each, so a multiplicative fit returns 205/205 where the data has eleven genuine exceptions  PRIOR ART: that a representation cannot state what its own coordinates cannot distinguish is the general fact behind all three blindnesses. Statistics sees marginals only (Shannon 1948 for what a marginal carries); analysis has no order in it; a multiplicative algebra is monotone in each factor by construction. Register 1170 measures them.",
  named="the three blindnesses")
R("Q.alpha", "Lambda_alpha: the polarisability index over cores, coordinates Z . Ne(core) . n_out . l_out",
  "the set of cores appearing in the spectra index", ["S.regime"], "R 1165; Born & Heisenberg 1924; Mayer & Mayer 1933", "MEASURED",
  check="18 cores held, E = 10. Sorted by (n_out, l_out) the isoelectronic ordering is a physical requirement — alpha must FALL with Z along a sequence — and the Ne-like and Mg-like rows obey it while the Ar-like row does not: K I 5.490 published, Ca II 6.665 extracted, Sc III 4.705. The index makes the violation visible where a table would not  PRIOR ART: core dipole polarisability as the origin of the high-l defect is Born & Heisenberg, Z. Phys. 23 (1924) 388-410; the systematic values are Mayer & Mayer, The polarizabilities of ions from spectra, Phys. Rev. 43 (1933) 605-611.",
  named="the polarisability index")
# NOTE R 1204: with the Janet collapse term present, restoring the alpha term drives its
# coefficient to q = 0.0090 and moves the l >= 4 rms by a tenth of a percent. Lambda_alpha
# remains a correct index and the equation no longer requires it.
R("A.seaton", "delta(n) = (alpha/K(l))(3 - l(l+1)/n^2) for a non-penetrating series, so delta_0 = 3 alpha/K and delta_2 = -l(l+1) alpha/K",
  "a Rydberg electron that does not enter the core", [], "Seaton 1958; Drake & Swainson 1991", "CITED",
  check="tested on 23 adjacent-l pairs in its domain: median observed/predicted 1.12, improved from 1.19 by restoring the n-dependent term, which confirms the term belongs. It fails on 20 near-hydrogenic pairs at the noise floor and on Ba II (delta_f = 0.756) and Hg II (1.062), where the 4f orbital has collapsed into the core and the series penetrates",
  named="the polarisation formula")
R("S.parent", "an OPEN-SHELL core gives many parent terms and no separable Rydberg series, so its levels can be published and its defect cannot be extracted",
  "an ion whose core has an open subshell", ["S.ground"], "R 1180; Condon & Shortley 1935; Condon & Shortley 1935; Racah 1943", "MEASURED",
  check="Fe IV's 3d4 core carries sixteen LS terms. The capture shows 13 of them, 24 distinct (parent, l, term) series, and EVERY ONE has exactly one member — n = 4 only. Fe IV has ~1,000 analysed levels and no extractable defect. The compendium holds Ne-like and Na-like ions at charge 15 and 16 and no open-shell ion above charge 6, which is not a collection preference but the fact that an open-shell core does not produce the object a quantum-defect index holds  PRIOR ART: parent terms and the fractional-parentage decomposition are Condon & Shortley, The Theory of Atomic Spectra (1935), ch. VII, and Racah's coefficients of fractional parentage (1943). That an open-shell core gives one series per parent is their structure; the measurement is that Fe IV's 24 series each hold one member.  PRIOR ART: parent terms and coefficients of fractional parentage are Condon & Shortley, The Theory of Atomic Spectra (1935), ch. VII, and Racah, Theory of complex spectra III, Phys. Rev. 63 (1943) 367-382. That an open-shell core gives one series per parent is their structure; the measurement is that the 24 Fe IV series each hold one member.",
  named="the parent-term wall")
R("Q.collapse", "the ORBITAL COLLAPSE threshold is a Janet block boundary, exactly",
  "a channel with p = 0 at l >= 2", ["S.ground","Q.bound"], "R 1187-1190; Goeppert-Mayer 1941; Griffin, Andrew & Cowan 1969", "MEASURED",
  check="the n+l = 5 block opens at Z = 21 and 3d collapses at 21; n+l = 7 opens at 57 and 4f at 57; n+l = 8 opens at 89 and 5f at 89. Three exact matches. Across 116 p = 0 channels at l = 2 or 3: collapsed median 0.637, uncollapsed 0.036, U-test p = 9.8e-4. Adding the term takes Ti IV nd from -0.620 to -0.056 and the overall rms from 0.1825 to 0.1411. The largest outliers are atoms APPROACHING a boundary — Ca I nd = 0.908 at Z = 20 against a threshold of 21, Ba II nf = 0.756 at 56 against 57 — so the collapse is a rapid transition, not a step  PRIOR ART: orbital collapse — the sudden contraction of the 3d and 4f wavefunctions as Z crosses a threshold — is Goeppert-Mayer, Rare-earth and transuranic elements, Phys. Rev. 60 (1941) 184-187, and Griffin, Andrew & Cowan, Theoretical calculations of the d-, f- and g-electron transition series, Phys. Rev. 177 (1969) 62-71. What is measured here is that the threshold coincides with the Janet block boundary at Z = 21, 57 and 89.",
  named="the Janet collapse")
R("S.status", "the index partitions by EXISTENCE STATUS, and nothing in it is impossible",
  "the aufbau survey", ["S.ground","S.parent"], "R 1191-1192; Theodosiou, Inokuti & Manson 1986", "MEASURED",
  check="101,328 cells. *** THE STATUS AXIS WAS REPLACED AT REGISTER 1578: VERIFIED/POSSIBLE/IMPROBABLE became WITNESSED/UNWITNESSED plus a NAMED BOUND, because improbable is a judgement about the future rather than a fact about the record — the same object-versus-observer fault register 1287 found in `standing`. *** Now: 337 WITNESSED (0.333% of the index) and 100,991 UNWITNESSED, of which 929 are exact by symmetry and need no measurement. Bounds on the rest: series above ng 28,527; no long-lived isotope 24,312; no analysis located at this charge 17,428; open-shell cores 26,641; not naturally occurring 225; and 2,929 with NO bound at all — separable series simply not yet measured. The charge bound is contradicted by twelve measured cells above it in this index's own file (R 1577). Every accuracy figure must be quoted against the witnessed count, not 101,328. PRIOR ART: the distinction between what a survey admits and what is measurable is exactly the distinction Theodosiou, Manson & Inokuti make in their 1986 table across all ionisation stages.",
  named="the existence partition")
R("Q.region", "the equation is VALIDATED in the verified-plus-possible region and EXTRAPOLATED outside it",
  "the channel equation and the existence partition", ["Q.delta","S.status","Q.collapse"], "R 1193-1194; Theodosiou, Inokuti & Manson 1986", "MEASURED",
  check="277 in-region channels give rms 0.1329 and R^2 0.9747 — better than the 311-channel fit on fewer points, because the 51 excluded were 24 three-parent cores, 15 sixteen-parent cores and 12 ions above charge 10. And the saturating exponent falls from 1.3257 - 0.2751 ln Ne to 0.5828 - 0.0266 ln Ne: nine-tenths of the Ne-dependence was open-shell contamination. Validated on 277, extrapolated to 98,078  PRIOR ART: the distinction between where a defect is measurable and where it is calculated is exactly the distinction their 1986 table makes — they compute Hartree-Slater values everywhere and note where experiment exists.",
  named="the validated domain")
R("S.regime", "the SIGN of d2 is a coordinate the ground state cannot supply, and the MAGNITUDE of d2 predicts the channel's own scatter",
  "a Rydberg channel with a fitted Ritz curve", ["S.ritz"], "R 1157-1162; NIST Atomic Spectroscopy compendium; NIST Atomic Spectroscopy compendium; Ritz 1903", "MEASURED",
  check="Seaton requires d2 < 0 for polarisation, so a positive d2 says the channel is not what the formula describes. By orbital: s 76% positive, p 74%, d 37%, f 6%, g 7%, h 9%. The two populations differ in median raw spread 0.0159 vs 0.0029 and median fit residual 0.0058 vs 0.0003, U-test p < 1e-5. The MAGNITUDE class predicts the spread at R^2 = 0.761 against l alone at 0.230 and the sign at 0.267, and the sign adds nothing to the magnitude. The three quantities do not separate: d0 against |d2| gives r^2 = 0.270  PRIOR ART: the SIGN rule is NIST's own — its compendium states that the Ritz coefficient a is usually positive for core-penetration series and negative for core-polarization series. What is measured here is the distribution across 274 channels and that |d2| predicts a channel's scatter at R^2 = 0.761.  PRIOR ART: the SIGN rule is NIST own — its compendium states that the Ritz coefficient a is usually positive for core-penetration series and negative for core-polarization series. What is measured here is the distribution across 274 channels and that |d2| predicts a channel scatter at R^2 = 0.761.",
  named="the regime coordinate")
# PRIOR ART R 1211: the SIGN rule is NIST's own — its Atomic Spectroscopy compendium states
# that the Ritz coefficient a is usually positive for core-penetration series and negative
# for core-polarization series. What is ours is the measurement across 274 channels and the
# finding that |d2| predicts a channel's scatter at R^2 = 0.761. The rule is not.
R("S.ritz", "a channel is a CURVE, not a number: delta(n) = d0 + d2/(n-d0)^2, and the index reaches d0 while nothing in it reaches d2",
  "a Rydberg channel with four or more members", ["S.ground"], "R 1150-1156; Ritz 1903; Hartree 1928; Ritz 1903; Hartree 1928", "MEASURED",
  check="the d2 term removes 48% of what the compendium called scatter (0.0199 -> 0.0104 across 274 channels). d0 against ln Ne, l and charge gives R^2 = 0.549; the curvature gives 0.018. The ISOELECTRONIC step moves both coordinates by the same factor at every l — 1.194/0.859 at s, 1.150/0.979 at p, 0.858/0.907 at d, 0.561/0.627 at f — while the l step moves them differently: 1.427/0.752, 3.696/1.373, 8.536/5.264. Along a sequence the channel translates; along l it deforms, and fitting l as a 2x2 map improves on the scalar by only 14% at s->p and 1% beyond  PRIOR ART: the extended Ritz formula delta = delta_0 + a/(n-delta_0)^2 + b/(n-delta_0)^4 is Ritz, Zur Theorie der Serienspektren, Ann. Phys. 12 (1903) 264-310, with Hargreaves and Hartree (Proc. Camb. Phil. Soc. 24, 1928) supplying the foundation. NIST's compendium states it in this form.  PRIOR ART: the extended Ritz formula delta = delta_0 + a/(n-delta_0)^2 + b/(n-delta_0)^4 is Ritz, Zur Theorie der Serienspektren, Ann. Phys. 12 (1903) 264-310, with Hargreaves and Hartree (Proc. Camb. Phil. Soc. 24, 1928) supplying the foundation. NIST states it in this form.",
  named="the channel curve")
R("S.ground", "the ground configuration determines every channel's existence and bounds its defect's integer part",
  "an atom of atomic number Z", ["K.produce"], "R 1139-1141; Madelung 1936; Janet 1929; Janet 1929; Madelung 1936; Hund 1925", "MEASURED",
  check="multiplicity from Hund on the core: 24 of 24 electron counts, exact containment. The cell set from aufbau: 8,488 cells admitting all 311 measured channels where the sampled index admits 296. And floor(delta) <= min(p, n0-l-1) for 311 of 311, exact 57%, within two 97%  PRIOR ART: the ground configuration follows the n+l ordering — Janet, La classification helicoidale des elements chimiques (1929); Madelung's rule as usually stated (1936). Hund's first rule (Z. Phys. 33, 1925) gives the term. Both are read, not derived.  PRIOR ART: the ground configuration follows the n+l ordering — Janet, La classification helicoidale des elements chimiques (1929), and Madelung rule as usually stated (1936). The term follows from Hund first rule, Z. Phys. 33 (1925) 345-371. Both are read, not derived.",
  named="the ground-state derivation")
R("K.axis", "an axis earns a COORDINATE when it is independent of the others AND its distinct values are few relative to what it adds; both conditions are necessary",
  "a closed index and a candidate axis", ["K.redun"], "R 1127-1131; Dushnik & Miller 1941; Shannon 1948", "MEASURED",
  check="on the same elements, Z<=16: (Z,charge,l) gives 0% redundancy, +multiplicity gives 82%, +2J gives 0% again. 2J is NOT derived — no combination determines it — but |L-S| <= J <= L+S constrains it to 2min(l,S)+1 values of seventeen. A coordinate must be free, not merely undetermined. The entropy account is PARTIAL: retained entropy is 26% for multiplicity and 27% for 2J, which does not separate them  PRIOR ART: an axis earns a coordinate when it is order-independent of the others (Dushnik & Miller 1941) and carries information (Shannon 1948). The test combines both.",
  named="the axis test")
R("K.coupling", "coordinate COUPLING does not predict redundancy",
  "a closed index", ["K.redun"], "R 1120; Dechter & Pearl 1989", "MEASURED",
  check="across six indices — Lambda, Lambda_spectra, the periodic table, Janet, the calendar, a box ordering — redundancy against coupling gives r^2 = 0.002, p = 0.94. Janet and the box ordering both have 50% coupling and 0% redundancy; Lambda_spectra has 17% coupling and 20% redundancy  PRIOR ART: that coupling alone does not predict what a local method achieves — the induced width, not the edge count, is the parameter. Dechter & Pearl, Tree clustering for constraint networks, Artif. Intell. 38 (1989) 353-366.",
  named="the refuted conjecture")
R("K.peak", "composability peaks at Lambda-10 and falls after: 0.0000, 0.7068, 0.8087, 0.6956, "
  "0.6394, 0.6186 across Lambda-8 to Lambda-13",
  "counting axes raise the fraction and coupling axes lower it, with no exception — §12.11.3's "
  "dichotomy predicts the sign as well as the price",
  ["K.twocol"], "M §12.11.1.4; Berge 1962", "COMPUTED", check="PRIOR ART: the composability fraction is the arc density of the composition quiver; its rise and fall with the tower is the measurement.", named="the composability peak")
R("K.deadend", "the non-composable cells are defined exhaustively: at Lambda-10 all 485 have g = 0 "
  "and every g = 0 cell is non-composable; at Lambda-13, 11,188 at g = 0, 5,116 with 2J in {6,7,8} "
  "which no 2J_c can start, and 8,214 failing only in combination",
  "L.c8 is k >= 1, so a target ending empty can never be a source; and 2J inherits 2K's range while "
  "2J_c is bounded by phi(k) alone",
  ["K.peak"], "M §12.11.1.5; Mac Lane 1971", "COMPUTED", check="PRIOR ART: cells that compose with nothing are those whose target is no other cell source — the non-composable part of a quiver.", named="the dead ends, defined")
R("K.zcross", "composability is 22.71% within one element and 85.23% across the 118, while E is "
  "28,503 without Z and 972,862 with it",
  "composability wants the whole table and closure wants one atom; Lambda closes because it has no Z",
  ["K.twocol"], "M §12.11.1.6; Edlen 1964", "COMPUTED", check="PRIOR ART: that composability is far higher across elements than within one is the isoelectronic structure — Edlen, Atomic spectra, Handbuch der Physik XXVII (1964).", named="the periodic table as a coordinate")
R("EM.cross", "EM-allowed cells compose at 11.6% within one element against the forbidden 40.7%, and "
  "the order reverses across the table at 89.7% against 77.9%",
  "the rule that forbids composition inside an atom is the rule that enables it between atoms; "
  "parity repeats it at 38.4% against 20.1%",
  ["K.zcross"], "M §12.11.1.7; Laporte 1924", "COMPUTED", check="PRIOR ART: the composability contrast between allowed and forbidden cells is a consequence of the parity rule; the measurement is the fraction.", named="the selection-rule crossing")
