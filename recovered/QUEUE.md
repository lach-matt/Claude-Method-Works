# THE QUEUE

*Reorganised 2026-08-10 by topic. The stratigraphic original — thirteen session
snapshots, each laid on the last — is preserved verbatim at `QUEUE-ARCHIVE.md`.
Nothing was discarded; repeated items were merged and the live ones grouped.*

---

# THE SPINE — what leads to what

The session of 2026-08-10 found that these are one chain, not separate tasks:

    Λ_ladder vacuous at 2 axes  (K.three: an index needs 3)
      └→ needs MORE LADDERS, not another axis  (E=0 forced at 4 cells)
          └→ six species ladders, forced by TWO relations   R 1374
              Z = Nₑ + c − 1  ·  A = Z + N
          └→ + the state family (Rydberg, ℓ, term, j, parent-term, isomeric)
              └→ E = 1, defect at the SUBVALENCE seat
                  └→ Λ_xray, the inner-shell index          R 1378
                      ├→ Moseley recovered, slope derived   R 1380
                      ├→ the isotopic rung, traced          R 1381
                      └→ SIX FIELD-SHIFT ANCHORS
                          └→ |ψ(0)|² fixed at the K shell
                              └→ B.coll ν⁻³ propagates it
                                  └→ δ PER CHANNEL
                                      └→ Λ_spectra populated
                                          └→ **LÖWDIN COMPLETE**

**The Löwdin work is PARTIAL, not finished** (person's ruling, 2026-08-10). It
answers the ORDERING. It completes when it populates Λ_spectra with δ per
channel, verifiable against measured channels. Everything above is the route.

---

# A · THE CRITICAL PATH

## ★★★ A1 · The field shift anchor — the next move

R 1376 put |ψ(0)|² **open by operator**. The KL3 capture supplies **six anchors**:
U, Pu, Cm, Am, Bk, Cf each at two mass numbers, lighter isotope HIGHER — the
field shift's sign, not the mass shift's.

    B.coll   |ψ(0)|² ∝ ν⁻³, same cell as the level spacing
    B.rank1  that family factorises EXACTLY, 2nd singular value 1.8e−14

**One measured constant + a derived scaling = δ per channel.** If it holds it is
the first time an operator-side cell in this work has been crossed rather than
described. HELD: `XRAY-KL3.tsv`, `XRAY-KL2.tsv`.

## ★★ A2 · Λ_spectra's closure — it lacks n

R 1341 names the cause. Λ_ryd holds the n-dependence Λ_spectra discards
(δ₀, δ₂, δ₄). The merged index **(Z, c, n, ℓ, 2S+1)** supplies it. This is the
index A1's output must populate.

## ★★ A3 · a is a(period, block, c) — every bracket is the c = 1 slice

At Nₑ = 20 the ordering reverses across three charges with E(3d²) − E(4s²)
swinging 17 eV. Λ_var said so before the brackets were built.
**Now feedable**: `LADDER-H-Ar-I-III.tsv` holds c = 0,1,2 for Z 1–18. The K–Kr
block is the one that matters (see D2) — Z 1–18 has no ns/(n−1)d competition.

---

# B · THE INDEXES

## ★★ B1 · Λ_xray — new, closed, partially valued

33 dipole lines → **9 cells** on Δn × Δℓ × jtype_hole, E = 0. `xray_index.py`.
Built from Λ's own transition alphabet + EM.map + T.a12, no new data.

**Language profile settled** (R 1379): unlike Λ_cross it has BOTH a statistics
language (pairwise marginals recover all 9) and an analysis language (Moseley,
R² = 0.998). Λ_cross remains the only integer object.

**Open — the coupling rung does not reduce.** The Kα doublet is measured across
85 unblended elements and no two-parameter form in Λ's vocabulary fits it:
(Z − σ)⁴ leaves 20% scatter and a ratio drifting 0.71 → 1.16 across the table.
Report the measurement, not a fit. NOT yet written to any artefact.

**Wanted**: L1M2, L1M3, L2M1, L2M4, L3M1, L3M4, L3M5 — the L-shell lines, which
test whether the nine types hold at a second depth.

## ★★ B2 · Λ_ladder — six species + the state family

`ladder_index2.py`. E = 1 on seat × kind × Zcross, 7 cells, defect at
**subvalence**, two candidates (counting-across-elements = Moseley;
coupling-within = the doublet). **Recompute with both X-ray ladders in** — that
is what resolves the E = 1 or makes it a genuine singleton.

Still open: whether isoelectronic/the walk and isotonic/isobaric sharing cells
is a fault or a finding (one object seen twice).

## ★ B3 · Λ_t — three empty cells, and two may be unreachable

7p, 6d, 7d. **ASD stops at Ds (Z = 110)**, and 7p needs Z ≥ 113. So 6d is
reachable (Ac, Th, Rf–Ds) and 7p/7d probably are not — which would make them
REAL ABSENCES rather than collection gaps, the R 1180 distinction.

## ★ B4 · Λ_ladder's own arithmetic — settled, recorded

Z = Nₑ + c − 1 leaves two of three independent; no ladder varies Z alone.
A = Z + N does the same on the nuclear side. R 1374.

---

# C · THE NUCLEAR CORRIDOR — refuted, and the screen it leaves

## ★★ C1 · The textbook family is REFUTED, structurally

    E = (N + 3/2) + β·ℓ(ℓ+1) − α·⟨L·S⟩

The ratio 4 is an **identity, not a coincidence** (R 1371, correcting 1368). For
two levels of one oscillator shell with Δℓ = 2, higher spin-antiparallel and
lower spin-parallel: Δ[ℓ(ℓ+1)] = 4ℓ+6, Δ⟨L·S⟩ = ℓ+3/2, ratio 4 for EVERY ℓ. The
constraint collapses to (ℓ+3/2)(4β + α) < 0 — it fixes the SIGN of one
combination. **SIX such pairs, three each way.** `corridor_identity.py`.

## ★★ C2 · The screen for replacements

R 1372: a candidate γ·T is admissible only if **ΔT is non-degenerate across those
six pairs**. A function of ℓ(ℓ+1) alone is the β slot; of ⟨L·S⟩ alone, the α
slot. **Six numbers screen a candidate before any fit.**

**NOT YET RUN** on the three named candidates: Woods–Saxon radial shape, a tensor
term, an ℓ-dependent effective mass. Also test the near-degenerate swaps both
ways — (2f7/2, 1h9/2) and (3p3/2, 2f5/2) — a form surviving either is robust.

---

# D · CAPTURE — the route now works

## ★★ D1 · The route

**The person pastes a URL; Claude fetches it live.** Established 2026-08-10 after
three rounds of generated tables failed verification. Nothing is transcribed by
anyone. Generated data failed on: ragged row counts, absent Ground-Shells column,
0.2–11% energy errors, and smoothed-away shell closures.

## ★★ D2 · The ionisation ladders — 15 of 108, +H,He,Li complete

    isoelectronic  11/11    the walk  106/106
    ionisation     ~15/108  ← this      isotopic  1 rung traced (R 1381)

    ie.pl?spectra=K-Kr+I-III&units=0&format=1&at_num_out=on&sp_name_out=on
      &ion_charge_out=on&seq_out=on&shells_out=on&level_out=on&e_out=0&unc_out=on

**K–Kr is the one that matters** — the whole 3d block, where ns/(n−1)d
competition lives, and it carries Ca I/II/III for A3. Then Rb–Xe, Cs–Rn, Fr–Ds.
Charge > 10 is IMPROBABLE (S.status) so I–XI suffices: ~1,170 rows not 6,027.

## ★ D3 · Theodosiou, Inokuti & Manson 1986 — the wholesale test

At. Data Nucl. Data Tables **35**, 473 (1986). Asymptotic quantum defects for s,
p, d, f across ALL ionisation stages of ALL ions with Z ≤ 50 — ~5,100
Hartree–Slater values against the compendium's 4,200. **Would replace R 1202's
standing weakness** (four of seven far anchors are theoretical) with thousands of
reference points.

## ★ D4 · AME2020 — CITED AND NOT HELD

`mathreg.py` and `indices.py` both cite it; no mass data in the restore point, so
**E.nuclide = 9 cannot be reproduced**. REPRODUCTION checks that the build runs,
not that its inputs are present. Same class of fault as R 1373.

## ★ D5 · Collection, what remains

**1,419 extractable cells** not yet measured — not 101,000. The Z × charge face is
the largest source of looseness at 1,935 admitted cells; the index holds 70 of
182 element–charge pairs. Of 112 missing pairs, closed-shell cores are genuine
gaps; **open-shell cores are not gaps at all** — levels published, no defect
extractable (R 1180).

---

# E · THE CHANNEL EQUATION — what it still gets wrong

    δ = a·p^e(Nₑ)·Nₑ^k·ln(c+1)/c        p > 0
    δ = h·C(Z)·((Nₑ−1)/Nₑ)·Nₑ^k·ln(c+1)/c   p = 0
    a = 0.3772 · e(Nₑ) = 0.8297 − 0.0900 ln Nₑ · k = 0.4942 · h = 0.5415
    284 channels, Z 2–90 · rms 0.1610 · R² 0.9741 · Pauli bound 328/328

## ★ E1 · The hydrogenic zero is ALGEBRAIC, not a prediction

At Nₑ = 1 the (Nₑ−1)/Nₑ factor vanishes for every charge and every C(Z). No
parameter can move it, so it is a tautology of the form rather than a test the
data passes. `hydrogenic_test.py`.

## ★ E2 · The relativistic wall, now on THREE objects

    hydrogenic ionisation, Z=92   +14.5% above Z²R
    Moseley KL3, Z=92             +14.2% above the linear law
    Kα doublet, Z≥70              +16% above C(Z−σ)⁴

Same electron, same shell, three independent measurements. **The equation is
non-relativistic — this is a DOMAIN statement, not a failure.**

## ★ E3 · Sr II and Ti IV share a signature

Low at s, p, d and high at f, growing with Nₑ — 0.33 at Nₑ=19, 0.70 at Nₑ=37.
The ℓ-dependence is not a linear coefficient: nearly flat across s, p, d, then a
cliff at f.

## ★ E4 · The polarisation floor is gone

The Janet term replaced it, so both f channels of the held-out species come out
at exactly zero where they measure 0.062 and 0.077. *Collapse dominates above the
boundary and polarisation below it; the equation has only one.*

## ★ E5 · The residual bow

0.93 at Nₑ 2–6, 1.10 at 6–15, 1.02 at 15–32, 0.89 at 32–60. Survived every form
tried. **Carcassés & González flag the same domain**, Phys. Rev. A 80 (2009)
024502 — E_ioniz = Z²N^(−2/3)g(N/Z), failing for neutrals.

---

# F · THE ARTEFACT PASS — see ARTEFACT-PASS.md

## ★★ F1 · Registers 1249–1381 · what has and has not landed

**Landed 2026-08-10**: the corridor identity and six-pair screen; Λ_xray and the
isotopic null in the Mathematical Compendium's authored tail; four new lines in
*what this work introduces*; the Löwdin reclassification in HANDOFF.

**Not landed**: the Kα doublet non-reduction (B1); the Index of Indices has no
Λ_xray entry and its §IX still reads *thirteen of fourteen close*; the Spectra
Compendium still wants the session's captures folded into `COORDINATES.tsv`.

## ★ F2 · The book owes two chapters

The Löwdin solution, and the three-body problem. **Nothing is written until both
a target and a solution exist** — R 1359 records the chapter that was written,
audited and CUT for claiming the problem factorises because there is no third
pair, which is false.

## ★ F3 · The compendium tail is AUTHORED, not generated

R 1373. `COMPENDIUM-TAIL.md` now holds it and `compendium.py` appends it; the
rebuild is verified idempotent. **Any future authored region must go the same
way** or the next rebuild eats it.

---

# G · UNFINISHED OBJECTS — two, both diagnosed

## ★ G1 · M.C2 — half-sided modular inclusion on a non-expanding horizon

OPEN on the GEOMETRIC route only — Sorce 2024 closes it by construction, since a
geometric modular flow needs a conformal Killing field. **The algebraic route is
not blocked.** The obstruction is in the corner edge modes, and it bottoms out at
POSITIVITY of the null translation generator, which Hadamard does not imply —
microlocal vs global spectral. R 1018–1022, 1038–1042.

## ★ G2 · Q.exch — the exchange factor, WITHDRAWN

The fitted sign is opposite to the measured one (R 1168). A uniform s can only
give 0/66 or 66/66 and the data says 55/66. **Needs an ℓ-dependent exchange
term** — Q.bound already carries the orbital count p the overlap should follow.

---

# H · THE CYPHER AUDIT — open items

**Three standing order/analysis contradictions on Λ_spectra**, named and not
adjudicated (R 1171): δ falls with ℓ (194/205 vs 102/205); triplet exceeds
singlet (55/66 vs 33/66); δ falls along a sequence (89/143 vs 135/143).

**Five language/index pairs never run**: Λ_spectra in geometry, algebra,
information and statistics; Λ_α in analysis. *The cypher's agreement is
established on Λ's 976 cells and asserted everywhere else.*

**Two operators still missing**: algebra's Gröbner basis needs a proper
Buchberger–Möller construction rather than the regularity proxy; information's
E_bits exists for Λ only.

---

# I · THE METHOD — protocols, rules, principles

## The protocols are CODE. Run them.

    domain_protocol.py   four questions before any fit. BLOCKS POOLING.
    chem_index.py        routes a residual to its property and class
    t_index.py           Λ_t, the corridor position on (ℓ, n)
    ladder_index.py      superseded by ladder_index2.py — still carries the
                         WITHDRAWN `state` axis (R 1356). NEEDS CORRECTING.
    distinguished_n.py   the magic sequences of four many-body systems
    nuclear_corridor.py  the refutation · corridor_identity.py the identity
    xray_index.py        Λ_xray · isotopic_null.py the null computation
    ground.py            108 observed neutral ground configurations

## The one microscope

**ℛ is the only lens.** When a piece verifies, ask WHERE ELSE THIS EXACT OBJECT
APPEARS. ℓ(ℓ+1) is one object seen six times. **Read orderings from a source;
never compute or recall them.**

## The rules, accumulated

Lock what is measured · one thing at a time · per element, not pooled · charge is
one symbol in three positions · evidence is not an object axis · calibrate on one
atom · **the neutral is not the table** · never fit across a language boundary ·
a law holding atom-by-atom need not hold as a walk · compendia answer, they do
not argue · figures removed must have their data represented another way ·
**do not invent a cell or a column — reshuffle until it fits or one cell remains**
(2026-08-10) · **an index needs THREE axes, never two** (K.three, R 1175) ·
**E = 0 is informative only where refusal was possible.**

## The seventeen mechanisms

Carried in `MECHANISMS.md` and cross-checked against `mathreg.py` by
`mech_audit`. Not repeated here.