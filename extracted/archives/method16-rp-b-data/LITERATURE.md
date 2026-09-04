# Literature checks — *The Method 1.6*

Every comparison between a compendium channel and an independently published
measurement. Registers 788, 858–863.

A channel built here averages the defect over the n it holds, which is usually low.
A published δ₀ is the **asymptotic** value from high-n spectroscopy. Where δ₂ > 0 the
defect falls toward δ₀, so **a low-n average must EXCEED a published δ₀** — that is the
direction each comparison is tested in, not equality.

---

## Confirmed

| channel | ours | published | source | verdict |
|---|---|---|---|---|
| **Ca II** ns | +1.8192 (n=4–10) | δ₀ = **1.802995(5)** (n=38–65) | single trapped ⁴⁰Ca⁺ | exceeds δ₀ by 0.016 ✓ |
| **Ca II** nd | +0.6338 (n=3–16) | δ₀ = **0.626888(9)** (n=37–50) | single trapped ⁴⁰Ca⁺ | exceeds δ₀ by 0.007 ✓ |
| **Ca II** limit | 95,751.88 | **95,751.916(32)** | correlated P/F fit | agrees to 0.036, ≈1σ ✓ |
| **Li I** nd | +0.0031 (n=3–12) | δ₀ = **0.00192(17)** | ⁷Li MOT, two-step cw | exceeds δ₀ by 0.0012 ✓ |

**Four independent confirmations, all in the direction the Ritz form requires.**

---

## Corrected by the literature

**P.mono's statement.** Register 802 read "δ falls monotonically with n" as a tendency
because both directions appeared. The extended Ritz formula
**δ(n) = δ₀ + δ₂/(n−δ₀)² + δ₄/(n−δ₀)⁴ + …** is standard, and **caesium's nF series is
measured with δ₂ = −0.2014(16) — negative — and its defects RISE**, 0.03331591 at n = 45
to 0.03333469 at n = 50. *The law is that δ approaches δ₀ monotonically; the direction is
sign(δ₂), a property of the channel.* Registers 858–859.

**P.polar's novelty.** Not first, and by fifty years — Freeman & Kleppner, Phys. Rev. A
**14**, 1614 (1976). Zn⁺ was measured at 18.33 ± 0.95 a₀³ from the same 4snf series this
compendium holds; caesium has been measured to ℓ = 8, beyond our ℓ = 7. Register 788.

---

## Exposed by the literature

**Li I np.** Ours +0.1477 over 41 members against a literature value near 0.047. The
channel spans a perturbation and its mean is not a defect — **P.perturb identified it from
the spread alone at register 704, before any literature was consulted.**

---

## Contested in the literature itself

**Ca II's ionisation energy.** One measurement gives 95,751.916(32) cm⁻¹ "in agreement
with the accepted value"; another reports 2,870,575.582(15) GHz, *"60 times more
accurately … and contradicting it by 7.5 standard deviations."* **The compendium uses
95,751.88 and should not adjudicate between them** — where the literature disagrees with
itself, a channel built on either value carries that disagreement and the compendium
records it rather than choosing.

---

## Where the literature has the same difficulty we do

**High-ℓ defects: theory and measurement disagree beyond their error bars.** Careful
modern measurements of **potassium's f, g, h and i** states report that *the differences
between the predicted and measured values are larger than the uncertainties in the
measurements in all cases.* **Register 794 attempted to fit α_d from our ℓ ≥ 4 defects,
failed, and could not diagnose whether the fault was implementation or data. The field
has the same disagreement with far better data** — which does not excuse our failure but
does place it.

**Scale check.** Rb ng measured at δ(n=30) = **0.00405(6)**. Our Na I ng is **+0.0003** —
smaller, as sodium's smaller core requires, and the two are consistent in ordering.

---

## Exposed by the literature — a systematic in every channel

**The Rydberg constant.** Chasing He I's *negative* high-ℓ defects against NIST's published
limit (198,310.6691, ours 198,310.666) found something larger: **`channels.py` uses R∞ =
109,737.31568 for every species where the reduced-mass value R_M = R∞/(1 + mₑ/M) is
correct.** For helium R_M = 109,722.386 — lower by 14.93 — so every defect is understated
by n*(√(R∞/R_M) − 1), **0.00240 at n* = 35 for helium, scaling linearly with n***.

*He I's nf −0.0010, ng −0.0014, nh −0.0015, ni −0.0016 over n = 4–35 against a
reduced-mass correction of about +0.0014: the size and the sign both match.* **Median
understatement across 403 channels: 0.00006. Largest: 0.00143. Fifty channels have an
error exceeding 20% of their own defect.** Registers 868–870.

**CORRECTED (registers 872–875).** `channels.py` now uses R_M where the levels are
measured and R∞ where the table is a theoretical hydrogenic one computed from R∞ — the
constant must match the data's convention, not the physics in the abstract. **Be IV, a bare
nucleus, now returns +0.0002 to 0.0000 across d, f, g, h, i, k with every spread at
0.0000.** *290 channels shifted; no mechanism's headline figure changed.*

**He I still cannot be corrected** — it came from Appendix B and `spectra_raw/` holds no
levels for it. **Li III is RESOLVED (registers 879–882).** The cause was a limit this work wrote as a
FORMULA rather than took from a source: `spectra_raw/LiIII.tsv` recorded *"limit = Z²R =
9 × 109737.31568 (hydrogenic, Z=3)"*. **Applying P.converge to its 81 levels gives
987,662.29 ± 0.36 — higher by 26.45 cm⁻¹**, which is the QED and relativistic contribution
a bare Coulomb expression omits. *With it, every Li III channel returns +0.0002 to +0.0004
with spreads of 0.0001, against −0.0038 to −0.0082 before.* **Register 679's "QED and
reduced-mass residual" was half right — the QED was real and it was in the LIMIT, not in
the levels.**

---

## K I — three channels and a limit, against an eight-digit source

**Peper, Helmrich, Butscher, Agner, Schmutz, Merkt & Deiglmayr, "Precision measurement
of the ionization energy and quantum defects of 39K I", arXiv:1907.02776 (2019).**
ETH Zurich, frequency-comb-referenced UV and millimetre-wave spectroscopy.

    published        delta_0                  ours (at our n-bar)
    s_1/2            2.18020826(5)            2.1912 +/- 0.0111    AGREES
    d_3/2            0.27698453(19)           0.2460 +/- 0.0380    AGREES
    f_j              0.0094576(6)             0.0112 +/- 0.0030    AGREES
    E_I              35,009.8139710(22)       35,010.6 +/- 0.4     high by 0.79

**Three of three verified.** The derived limit is high by 0.79 cm-1 — twice our stated
error, and inside the **x6 inflation** register 1056 calibrated on Ga II. *That
calibration now holds on a second species.*

**And a prediction is REFUTED.** Our propagated bound on K I nh is 0.0016–0.0112. Seaton
with the published K+ polarisability alpha_d = 5.49(11) a0^3 gives **0.00036**; Seaton
under-predicts ng by 2.3x here (0.00106 against a published 0.0024080) because the dipole
term omits the quadrupole, so scaled up nh is about **0.0008** — still below our lower
bound. **Two independent estimates place K I nh under the deduced lower bound**, which is
register 1082's over-claiming, confirmed from outside.

---

## Two conventions confirmed as standard

**The charge in the formula is the CORE's, not the atom's.** NIST's own compendium states
the Rydberg formula as **E_nl = −Z_c²/(n−δ)²**, *"where Z_c is the charge of the core and
n* = n − δ"*. This confirms register 766, where atomic numbers had been passed for Be III
and B III and had to be corrected from 4 and 5 to **3**.

**The Rydberg constant is the reduced-mass one.** Precision Rb work writes its constant
explicitly as **R\* = R∞/(1 + mₑ/m_₈₇Rb)**, corrected for the reduced electron mass.
**Register 868's correction is standard practice, not an invention** — which makes its
absence from `channels.py` until today a plain omission rather than a judgement call.

---

## A diagnostic the compendium gained

**A defect that deviates from constancy carries the signature of its cause in the POWER of
n\*:**

    n^3    a shift in the ionization limit
    n^7    a magnetic field
    n^10   an electric field

*Published, and the cubic law was derived independently here at register 877 and used to
find Li III's limit fault at 879.* **Any future residual can now be attributed by fitting
its power**, rather than by trying explanations in turn as registers 872–878 had to.

---

## Isoelectronic extrapolation — the method is Edlén 1964

**The activity is sixty years old.** Edlén's *Handbuch der Physik* article (1964) systematised
isoelectronic regularities, and Curtis has carried it on: *"through core polarisation and
core penetration models, quantum defect formulations and charge screening parameterisations,
quantifiable regularities have been discovered."* There is a paper titled *"The combined use
of screening and quantum defect parameters in the study of ionized atoms."*

**The field's standard forms are screening-based** — Z_eff = Z − σ with a penetration
parameter p — **and Edlén's Taylor expansion of δ in 1/n\*².** *The form this work fitted,
δ = a + b·ln(c+1)/c, was not located; but four other "findings" this session turned out to
be published, so an unsuccessful search establishes little.*

**And the form does not generalise** (register 944): it fits the Mg-like ns ladders to 2% of
range and fails on nd, nf and every He-like ladder at 47–65%.

---

## Contradicted by the literature

**P.coreblind.** MQDT defines the quantum defect as **mu_{l,lambda,alpha+}**, depending
explicitly on the internal quantum state alpha+ of the ionic core, and the entire apparatus
of multichannel quantum defect theory exists because different core states give different
channels with different defects. **The mechanism asserts the opposite on two instances.**
*Ne II's agreement across cores 26,000 cm-1 apart and Si I's across 287 are real
measurements; what they are not is a general principle.* Register 947.

## Expressed in the field's own coordinates

**P.jsplit.** *"The angular momentum quantum numbers that matter are the total angular
momentum of the core f_c ... and the total angular momentum of the Rydberg electron j_e."*
That is P.jsplit's decomposition exactly. **The framing is standard; the content — a
227-fold separation between open-or-heavy and closed-and-light cores — the search did not
reach.** Register 948.

---

## Not found

Searched and not located: **Li I nf**, **Ca II nh**, **Al II nh** — the three two-sided
brackets of register 842. **Ar II's quantum defects** — the compendium's largest holding at 44 channels. Its
literature is energy levels and observed spectral lines, which is the ASD compilation
itself. **Three of the four best-collected species — Ar II (44), Si I (39), Ne II (37) —
have no published defects to check against.** *The compendium computes defects for spectra
whose defects nobody has tabulated: that is both its value and the reason it cannot be
checked.* Also not found: **Mg II's quantum defects** — the compendium holds twelve Mg II channels and the
literature on that ion is transition probabilities, lifetimes and photoabsorption, not
quantum defects. Also sought and not obtained: numerical values for **Na I's
f, g and h defects**, which are published (J. Phys. B **30**, 2345, 1997, *Quantum defects
of the sodium atom in f, g and h states*) but behind a paywall; the abstract states the
coefficients reproduce Na Rydberg levels to better than 0.2 MHz for n > 20 without
giving them. **Our Na I nf +0.0014, ng +0.0003, nh +0.0000 remain unverified against
it.** They remain **PREDICTED AND UNVERIFIED**, which is the status
that should attract scrutiny rather than confidence.

---

## Prior art on the coordinates, checked at register 1208

### The noble-gas-centred coordinate is published

**Washburn, Simons & Allahyarov, arXiv:2605.00028, 22 April 2026 — "A Noble-Gas-Centered
Coordinate for Within-Period Atomic Property Trends".**

They introduce **ρ = d/L_p ∈ [0,1)**, the distance from the preceding noble gas normalised
by the period length, and a landscape function **J(ρ) = cosh(ρ ln φ) − 1** with φ the
golden ratio. From it they derive first ionisation energy, electron affinity, Mulliken
electronegativity and Pearson hardness on one axis. Of 34 atoms across periods 2–4, 26
lie on the predicted monotone descent and **the 8 deviations occur exactly at
{p³, d⁵, f⁷, s², d¹⁰}** — the half-filled and filled subshell sites.

**ρ is the compendium's *electrons beyond closure*, normalised.** Register 1122 tested
that quantity as a fifth coordinate of Λ_spectra and rejected it — it is derived, and
adding it multiplied the corner count by 652%. This paper builds a whole construction on
it for a different observable.

**What does NOT collide.** Their observable is a single ground-state quantity per atom;
ours is δ(n, ℓ) across a Rydberg series at every ℓ and charge. Their anomaly sites are
half-filled and filled subshells; ours is the **Janet block boundary at n+ℓ**, which
their coordinate does not see because ρ resets at every noble gas and the collapse
threshold sits at the *opening* of an n+ℓ block. Registers 1187–1190 stand.

**What DOES need saying.** The compendium should not describe a noble-gas-referenced
coordinate as unexamined. It has been examined, published, and made to carry four
observables.

### Isoelectronic sequences need more than one set of constants

**Methods of Calculating Ionization Energies of Multielectron (Five or More)
Isoelectronic Atomic Ions, PMC3671562.**

Their conclusion, in their own terms: **Slater's rules are not appropriate for predicting
trends or screening constants**; ionisation energies are not functions of complete
squares; and **for particular isoelectronic sequences the ionising electrons may occupy
different orbitals, so more than one set of constants is needed.**

**That is the ladder's own finding, published, about a different observable.** The
compendium established at registers 1183–1184 that δ(c) = A + B·ln(c+1)/c fits per
sequence to median rms 0.0083 and that no closed form of its parameters does better than
0.168 — a factor of twenty. **Their reason is ours**: the electron in question changes
orbital along the sequence, so one parameter set cannot serve the whole ladder.

### The regime is NIST's own statement, not ours

**NIST, *Atomic Spectroscopy — Term Series, Quantum Defects*** (the compendium's own data
source) gives the extended Ritz formula δ = δ₀ + a/(n−δ₀)² + b/(n−δ₀)⁴ + … and states:

> **the value of a is usually positive for core-penetration series and negative for
> core-polarization series.**

**That is register 1157.** `S.regime` records *the sign of δ₂ is a coordinate the ground
state cannot supply* and reports s 76% positive, p 74%, d 37%, f 6%. **The sign rule was
already published, in the reference the captures come from.** What the compendium adds is
the MEASUREMENT across 274 channels and the finding that |δ₂| predicts a channel's scatter
at R² = 0.761 — but the rule itself is not ours and must not be presented as new.

### Quantum defects against Z^⅓ across the whole periodic table

**arXiv:physics/0504154, "The Zel'dovich effect and evolution of atomic Rydberg spectra
along the Periodic Table".** They compile **experimental quantum defects for 37 elements**
and plot μ against **Z^⅓**, comparing to a systematic theory and to the numerical μ(Z) of
Fano, Theodosiou & Dehmer.

**Z^⅓ is the compendium's Thomas–Fermi axis** — register 1064's Nₑ^⅓ and the channel
equation's Nₑ^0.494. **The idea of organising defects on that axis across the whole table
is published.** Their compilation of 37 elements is also data the compendium does not hold
and could check against.

### A measured quadrupole polarisability, and the same tension

**arXiv:2502.20961, Cs via terahertz and radio-frequency spectroscopy**, gives true Cs⁺
polarisabilities: **α_d = 15.696(16) a₀³ and α_q = 78.6(12) a₀⁵** (ℓ ≥ 4 fit), against
theory at 15.8–15.9 and 76–118.

**And they report the difficulty the compendium hit at register 1211**: treating nf as
non-penetrating *gave α_d and α_q not in agreement with their ng energies*. Our Si III
g/h ratios of 1.77 and 1.12 are the same disagreement in a less-measured species. **Their
resolution is that nf states need penetration and exchange included** — so the fault is in
treating f as polarisation-only, which is what our own Janet gate does.

### The survey itself is published

**Theodosiou, Inokuti & Manson, "Quantum defect values for positive atomic ions",
*Atomic Data and Nuclear Data Tables* **35**, 473 (1986).**

> The asymptotic quantum defects, at the ionization limit, of s, p, d and f atomic
> orbitals have been calculated in the Hartree–Slater approximation **for all
> ionization stages of all ions with atomic number Z ≤ 50.**

Roughly **5,100 values of δ₀(Z, charge, ℓ)**, against the compendium's
verified-plus-possible 4,200. **The object this compendium supplies has a published
table**, and the bibliography carries it as a reference the coordinates can be checked
against.

**The companion report is open**: Manson, Inokuti & Theodosiou, *Systematics of Energy
Levels and Other Properties of Highly Charged Ions*, OSTI 7104964. It uses the
compendium's three axes by name — **isoelectronic (N constant), isonuclear (Z constant),
isoionic (z = Z − N + 1 constant)** — and states three things the compendium can use:

**One.** The structure in μ is *"due to the delicate balance between three forces: the
nuclear attraction, the interelectron repulsion, and the centrifugal repulsion."*

**Two.** *"For the neutrals, there are slope discontinuities in the curves for N = 2, 10,
18, and 36, the noble gas electron numbers. By the third spectrum (z = 3), these
discontinuities occur for N = 2, 10 and 28"* — **the closed shells move from noble-gas to
hydrogenic as charge rises.** The compendium's Janet collapse threshold is fixed in Z and
does not carry this.

**Three.** *"This structure is considerably diminished for z = 2 and essentially gone for
z = 3 and higher."* The compendium's sample — 20 species at charge 1, 9 at charge 4 —
cannot test this.

---

## The drawn indexes, attributed

### Janet's left-step table, and the open problem underneath it

**Charles Janet, *Considérations sur la structure du noyau de l'atome*, Beauvais (1929)**,
with the left-step table first published in **1928**. Janet **recognised the (n+ℓ) rule
before Madelung**, who reached it around 1926 and did not publish until 1936; Janet's
table correctly placed the actinides years before most were discovered. The shell-length
sequence 2, 8, 8, 18, 18, 32, 32 follows from the rule by the **Klechkovski–Hakala
formulas**.

**And why the ordering holds is unresolved.** *The Löwdin challenge — the origin of the
n+ℓ, n rule — remains open; see Allen & Knight, Int. J. Quantum Chem. **90** (2003)
80–88.* **The compendium uses Janet's ordering and does not explain it.** The
orbital-collapse coincidence at Z = 21, 57 and 89 (registers 1187–1190) is a measurement
against his boundaries, not a derivation of them.

**On the wider literature of periodic systems:** at least a thousand have been published
since Mendeleev; Scerri, *A Tale of Seven Scientists* (Oxford, 2016), and van Spronsen
survey them.

### The other drawn indexes

| index | source |
|---|---|
| the periodic table | Mendeleev, Z. Chem. **12** (1869) 405–406 |
| the nuclide chart | Segrè's chart, in use since the 1940s; values from AME2020 |
| the calendar | the Gregorian reform of 1582, on the Julian arrangement of 46 BC |
| the EM quotient | Laporte (1924); Russell & Saunders (1925); Wigner (1927) |
| the violation index | Penrose (1965); Pais & Uhlenbeck (1950); core as MUS, Chinneck & Dravnieks (1991) |
| Λ_spectra | Seaton (1958, 1983); survey table Theodosiou, Inokuti & Manson (1986) |

---

# THE DATA SOURCES, AND WHAT EACH SUPPLIES

*Gathered in one pass at register 1258. The compendium's coordinates rest on these;
each is listed with what it holds that the others do not.*

## The NIST chain

**Kramida, A., Ralchenko, Yu., Reader, J., and NIST ASD Team, *NIST Atomic Spectra
Database* (ver. 5.12), DOI 10.18434/T4W30F.** The assembled database: levels, lines,
transition probabilities, and — through the Ground States and Ionization Energies
(GSIE) interface — **6,027 spectra with ground-state electronic shells, ground-state
level labels, ionization energies and total binding energies**. Every capture in this
work comes from here. *The GSIE interface is a POST form; a plain GET returns
ionization energies without the shells column.*

**Martin, W. C., Musgrove, A., Kotochigova, S., and Sansonetti, J. E., *Ground Levels
and Ionization Energies for the Neutral Atoms*, NIST SRD, DOI 10.18434/T42P4C.** The
neutrals, Z = 1 to 104, with ground levels in LS-coupling names. *Notes that Pa, U and
Np are better described in jj-coupled 5f^N(L1S1J1) 6d_j 7s2 terms, and that Pb, Bi and
Po ground levels are jj-coupled because of the 6p spin-orbit interaction — which is
exactly the tower's LS→jj transition, in the ground state.*

**Sansonetti, J. E., and Martin, W. C., *Handbook of Basic Atomic Spectroscopic Data*,
NIST SRD 108, J. Phys. Chem. Ref. Data 34 (2005) 1559.** Neutral and singly-ionised
atoms, Z = 1 to 99, per element: wavelengths, intensities, spectrum assignments and
ground levels, with about 12,000 lines. **This is the source that covers charges 1 and
2 — the range where Madelung ordering holds and where the equation's regime assignment
cannot be derived.** Browsable per element rather than through a form.

**Shirai, T., Reader, J., Kramida, A. E., and Sugar, J., *Spectral Data for Highly
Ionized Atoms*, J. Phys. Chem. Ref. Data 36 (2007) 509.** The high-charge range,
where the ordering becomes hydrogenic.

**Kramida, A., J. Res. Natl. Inst. Stand. Tech. 118 (2013) 168.** The LOPT
level-optimisation method behind many of the compiled levels.

## Works built on that chain

**Del Zanna, G., *et al.*, *CHIANTI — an atomic database for emission lines*, Paper
XVI, arXiv:2011.05211.** The astrophysical emission database; carries level and
configuration data derived from ASD, and is the standard downstream consumer.

**Dutta, U., *et al.*, *Compilation of spectroscopic data of Radium (Ra I and Ra II)*,
arXiv:1603.01087.** A single-element compilation in the same style as this work's
captures, crediting Kramida for the ionization-energy calculation.

**Cowley, C. R., *et al.*, *A study of the elements copper through uranium in Sirius
A*, arXiv:1605.08399.** Stellar abundance work resting on ASD levels — an example of
the compendium's data being used where the coordinates matter and the index does not.

## Orbital collapse — the double well

**Connerade, J. P., *Highly Excited Atoms* (Cambridge, 1998), Chapter 5.** The standard
review of orbital collapse.

**Goeppert-Mayer, M., Phys. Rev. 60 (1941) 184.** Rare-earth and transuranic elements —
the first identification of the collapse.

**Griffin, D. C., Andrew, K. L., and Cowan, R. D., Phys. Rev. 177 (1969) 62.**
Theoretical calculations of the d-, f- and g-electron transition series.

**arXiv:2402.02609 (2024).** Orbital collapse for 5g electrons in superheavy elements,
and the statement this work uses directly: *the effective radial potential for 4f and
5f electrons has two wells, a deep narrow inner one and a shallow outer one; the
electron is localised in one or the other; and **in both cases the radial wave
functions are nodeless**.* **That is why the collapse is pure phase and h is the
inner-well defect.**

**arXiv:1208.3768, *Atomic swelling upon compression*.** The same double well produced
artificially by confinement, with the natural case cited to Connerade.

**Moss, A., *Lanthanides & Actinides Notes* (2003).** The quantitative statement used
to fix h(f): *for Ba (Z = 56) 4f is an outer orbital with ⟨r⟩ close to hydrogenic; for
La (Z = 57) 4f is an inner orbital with ⟨r⟩ ≈ 0.7 a₀; only at Ce (Z = 58) is the 4f
electron of sufficiently high binding energy to be occupied.*

## The Löwdin challenge

**Löwdin, P.-O. (1969).** The derivation of the n+ℓ rule named a major unsolved problem
in quantum chemistry.

**Klechkovsky, V. M. (1962).** An early proposed explanation.

**Demkov, Yu. N., and Ostrovsky, V. N., *n+ℓ filling rule in the periodic system and
focusing potentials*, Sov. Phys. JETP 35 (1972) 66.** **The nearest thing to a
derivation** — a potential class whose levels depend only on n+ℓ. The consensus is
that a chosen potential is not what Löwdin intended.

**Wong, D. P., J. Chem. Educ. 56 (1979) 714.** A theoretical justification.

**Ostrovsky, V. N. (2001); Allen, L. C., and Knight, E. T., Int. J. Quantum Chem. 90
(2003) 80.** Claimed solutions; **Scerri's commentary finds the second inadequate.**

**Scerri, E. R., *A Tale of Seven Scientists* (Oxford, 2016); van Spronsen, J. W.,
*The Periodic System of Chemical Elements* (Elsevier, 1969).** The wider literature of
periodic systems — at least a thousand have been published.

## Quantum defects across the table

**Theodosiou, C. E., Inokuti, M., and Manson, S. T., *Quantum defect values for
positive atomic ions*, At. Data Nucl. Data Tables 35 (1986) 473.** **The survey, in
Hartree–Slater, for all ionisation stages of all ions with Z ≤ 50** — roughly 5,100
values of δ₀(Z, charge, ℓ).

**Manson, S. T., Inokuti, M., and Theodosiou, C. E., *Systematics of Energy Levels and
Other Properties of Highly Charged Ions*, OSTI 7104964.** Open access. Uses the
compendium's three axes by name and states that **the closed shells move from noble-gas
numbers at z = 1 to hydrogenic ones at z ≥ 3** — confirmed here at four independent
electron counts.

**arXiv:physics/0504154, *The Zel'dovich effect and evolution of atomic Rydberg spectra
along the Periodic Table*.** Experimental defects for 37 elements plotted against Z^⅓.

**arXiv:1412.1428.** Holmium Rydberg series by MOT depletion spectroscopy — nd defects
0.7 to 0.85 in a mid-lanthanide, a region the compendium holds nothing comparable to.

**arXiv:1706.06237.** Cs I np at n = 70–100, δ = 3.5667 — the compendium's only
measured far anchor.

**arXiv:2502.20961.** Cs⁺ dipole and quadrupole polarisabilities from terahertz and
radio-frequency spectroscopy, and the same nf/ng disagreement this work met.

**arXiv:2508.06733.** Actinide quantum defects, Z = 89–103, theoretical.

**Lyons, L., *Discovering the significance of 5 sigma*, arXiv:1310.1284 (2013).** The
history and the critics of the threshold this work uses for bracket admissibility.

### Thomas–Fermi scaling of ionic spectra — the ⅔

**Carcassés, R., and González, A., *Thomas-Fermi scaling in the energy spectra of
atomic ions*, Phys. Rev. A **80** (2009) 024502; arXiv:0906.4065.**

> E_ioniz = Z² N^(−2/3) g(N/Z), with Z the nuclear charge and N the electron count.
> *"This relation does not hold for neutral atoms, but works extremely well in the
> cationic domain, Z > N."* g is given analytically with two adjustable parameters and
> fitted to more than 380 ions.

**The ⅔ relating electron count to charge in a scaling variable is theirs**, tested on
a body of data comparable to this compendium's. Register 1279 finds the per-element
constants of the channel equation collapse onto u = ln(Nₑ/c^(2/3)) at r² 0.9920, and
1281 records that **the exponent is attributable and the application to the quantum
defect is not** — no such collapse appears in the literature searched.

**And their caveat is this work's.** They flag that the scaling fails for neutrals; the
compendium's residuals bow at 0.93 for Nₑ = 2–6 and 0.89 for Nₑ = 32–60, the same
domain.

**Related:** arXiv:1605.07751 on the large-Z scaling of the kinetic energy density,
which gives the three radial regimes — near-nuclear r < Z^(−2/3), core r ~ Z^(−1/3),
asymptotic r > Z^(7/6) — and states where Thomas–Fermi may and may not be trusted.

### Isoelectronic energy differences — the quadratic in charge

**Krug, S. L., and von Lilienfeld, O. A., *Alchemical insights into approximately
quadratic energies of iso-electronic atoms*, arXiv:2406.18416 (2024).**

> Experimental energy differences ΔE plotted against the final system's nuclear
> charge for iso-electronic atoms with Z from 1 to 86, fitted as approximately
> quadratic, with the fitted parameter tabulated against electron number for each
> series — both with and without the constraint that initial and final
> configurations match.

**This is the form register 1304 uses.** Y(c) = Ac² + Bc + C along an isoelectronic
sequence is theirs, tested on a far larger set than the six species captured here.
**What this work adds is a measured crossing at c = 2.13 for Nₑ = 20**, from
Ca I, Sc II, Ti III and V IV.

**Berengut, J. C., *et al.*, arXiv:1204.0603.** Locates the 6p–5f crossing in the
thallium isoelectronic sequence by Dirac–Fock, plotting orbital energies against Z
and reading the crossing from the curve. *Configuration crossings along
isoelectronic sequences are a computed object; they need not be captured.*

**Standard inorganic statement** (Schaller, *Principles of Chemistry*; Moss,
*Transition Metals Notes*): the 3d orbital lies closer to the nucleus than 4s,
experiences an increase in charge more strongly, and contracts more — so on
ionisation 3d falls below 4s. **This is why register 1304's hydrogenic estimate for
the leading coefficient came out with the wrong sign: the contraction is
differential, and bare hydrogenic energies do not carry it.**

## From M's Gemini inputs, verified at register 1615

**Rosenzweig, N. & Porter, C. E.**, *Repulsion of Energy Levels in Complex
Atomic Spectra*, Phys. Rev. **120**, 1698 (1960).
→ **PRIOR ART for the jK rebuild (R 1602).** Level-spacing statistics for
ATOMIC spectra, and the requirement that states be grouped by good quantum
numbers before the statistics mean anything. Our keyability problem, 1960.

**Allen, L. C. & Knight, E. T.**, *The Löwdin challenge: Origin of the n+ℓ, n
(Madelung) rule*, Int. J. Quantum Chem. **90**, 80–88 (2002).
→ Confirms Löwdin 1969 posed the n+ℓ derivation as a major unsolved problem.
The direct response to the challenge our chapter addresses.

**Scerri, E.**, *Commentary on Allen & Knight's Response to the Löwdin
Challenge*, Int. J. Quantum Chem. **109**, 959–971 (2009).
→ Records **~20 exceptions to the n+ℓ rule** — independent corroboration of
register 1594's La/Ce and Ac/Pa from NIST ground configurations. Also asks
directly *whether it is important to derive the rule at all*, which is the
position `CHAPTER-LOWDIN.md` reaches by computation.

**Montgomery, H. L.** (1973) pair correlation; **Odlyzko, A.** (1987)
numerical; **Berry, M. & Keating, J.** — the zeta-zero / GUE correspondence.
→ POINTER only. Tested on our levels at R 1615 and **refuted by control**: a
pure Rydberg series scores 0.644 on the r-statistic with no chaos in it.

**NOT PURSUED — real physics, no object in any index here:**
Alcubierre and Morris-Thorne metrics · Aharonov-Bohm and Berry phase ·
Landauer's principle · Friston's Free Energy Principle · Tononi's IIT ·
McFadden's CEMI · Hameroff-Penrose Orch-OR · octonions and E8 as a closure
bound. Recorded so a later session need not re-derive the judgement.

### Rosenzweig & Porter 1960 — read in full at register 1620

*Repulsion of Energy Levels in Complex Atomic Spectra*, Phys. Rev. **120**,
1698. DOI 10.1103/PhysRev.120.1698. Companion: *Statistical Properties of
Atomic and Nuclear Spectra*, Ann. Acad. Sci. Fennicae AVI **44** (1960).
Follow-up: R. E. Trees, Phys. Rev. **123**, 1293 (1961).

**The three-way split by spin-dependent force strength:**

| elements | forces | what the key must carry |
|---|---|---|
| Hf Ta W Re Os Ir | strong | **J alone** — odd-parity levels of the same J follow Wigner |
| Sc Ti V Cr Mn Fe Co Ni | weak | **S, L and J** all fixed |
| Y Zr Nb Mo Ru Rh Pd | intermediate | neither key is clean |

**Their own parenthesis is our refusal problem:** *"When the quantum numbers S
and L are disregarded, the same levels give rise to a distribution of spacings
which is approximated by a random superposition of a number of appropriately
weighted Wigner distributions."*

→ **ATTRIBUTE IN THE jK CHAPTER.** The coupling scheme decides the key, and
they published the element ranges in 1960.

⚠ **We cannot test it.** Our eight spectra from those elements are all IONS;
they studied NEUTRALS with complex open shells.

### Demkov & Ostrovskii 1972 — read in full at register 1621

*Filling Rule in the Periodic System and Focusing Potentials*, Zh. Eksp. Teor.
Fiz. **62**, 125–132 (1972); Sov. Phys. JETP **35**, 66.

**The result:** for U(r) ∝ −1/[r(r+R)²] — a *focusing* potential closely
resembling Thomas–Fermi — additional degeneracy occurs for levels of identical
**N = n + ℓ**, and **only at E = 0**. The degeneracy is lifted at E < 0.

**Why it matters here:** Seaton's theorem gives π μ(n→∞) = δ(E=0), so the
index's asymptotic defects are E = 0 quantities. The DO degeneracy and our
measured column sit at the same energy.

**But the test refutes the connection.** Corridor width does not narrow with Z
(R 1621) as the Thomas–Fermi limit would require.

Related, all verified: Demkov & Ostrovsky, *Internal symmetry of the Maxwell
"fish-eye" problem and the Fock group for the hydrogen atom*, Sov. Phys. JETP
**33**, 1083 (1971) · Ostrovsky (2001) review · *On the dynamical symmetry of
the periodic table II: modified Demkov–Ostrovsky atomic model*, J. Phys. B
**17**, 21 (1984) — the ΔN × SU(2) symmetry · Kibler, arXiv:quant-ph/0611287 ·
Meek & Allen list **19 anomalous configurations**, corroborating R 1594 again.

### The exchange factor and MQDT — read at register 1622, closing G2

**The singlet–triplet splitting scales as n\*⁻³** (effective principal quantum
number), so the dependence is on n before ℓ.

**And at high n the channels MIX** — singlet and triplet character is no longer
pure, so a factor keyed on the label multiplies the wrong thing. That is why
`Q.exch` scored exactly chance at register 1168.

- **Aymar, M.**, *Rydberg series of alkaline-earth atoms Ca through Ba: the
  interplay of laser spectroscopy and multichannel quantum defect analysis*,
  Phys. Rep. **110**, 163 (1984)
- **Sun, J.-Q. & Lu, K. T.**, J. Phys. B **21**, 1957 (1988) — msns ¹S₀ and
  ³S₁ series
- **Sun, J.-Q.**, Phys. Rev. A **40**, 7355 (1989) — MQDT of hyperfine
  structure in high Rydberg states
- **Sun, Lu & Beigang**, J. Phys. B **22**, 2887 (1989) — msnd series

→ **MQDT is not an ℓ-dependent correction to a single-channel factor. It is a
different object.** G2 as posed cannot be satisfied.
