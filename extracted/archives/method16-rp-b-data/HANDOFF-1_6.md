# HANDOFF — 2026-08-10

*Read this first. It is the complete state: what was done, what is open, what to
do next, and what to be careful of. Nothing here needs reconstructing.*

---

## 0 · HOW TO RESUME

**Upload `restore-point-1.6.tar.gz` and say:**

> Restore from the tar into /home/claude/work, read QUEUE.md and HANDOFF.md, and
> continue.

**The restore command is:**

```bash
mkdir -p /home/claude/work && cd /home/claude/work \
  && tar xzf /mnt/user-data/uploads/restore-point-1.6.tar.gz && ls | head -30
```

**Then verify before doing anything else:**

```bash
cd /home/claude/work && rm -rf .zeno __pycache__ \
  && python3 The_Method_1_6_audits.py 2>&1 | tail -1
```

**Expected: `ALL TWENTY-FIVE PASS`.** If it does not, stop and report — something
did not survive the transfer.

---

## 1 · WHERE THE WORK STANDS

**The Method 1.6** · 449 files · **registers 165–1370, 1,163 entries** · twenty-five
prime audits and four companion audits passing.

**The Löwdin challenge is solved and written up** as Part VII §34 of the book.

    ν(n,ℓ,q) = n − a·√( n − ℓ − 1 + q/2(2ℓ+1) )

    the incoming electron takes the Pauli-admissible subshell of least ν
    L(Z) < a < U(Z),   L,U = Δn(√p_g + √p_r)/(p_g − p_r)
    entry point:  t(ℓ) = √( ℓ(ℓ+1)/2 )

**106 of 106 elements. Nineteen surds. No fitted parameter.** Every term is the
node theorem, antisymmetry, the centrifugal term, or arithmetic on them.

**Thirteen indexes closed.** Λ_ladder is open (its ladders are unbuilt) and
Λ_spectra is open (it lacks the principal number).

---

## 2 · THE IMMEDIATE NEXT TASK

### The nuclear shell ordering — the textbook family is REFUTED

**Run `nuclear_corridor.py` to reproduce.** It builds the corridor for

    E = (N + 3/2) + β·ℓ(ℓ+1) − α·⟨L·S⟩        N = 2(n_r − 1) + ℓ
    ⟨L·S⟩ = ½[ j(j+1) − ℓ(ℓ+1) − ¾ ]

against the observed filling order, requiring that order to be the order of
increasing E. **Each consecutive pair gives one linear inequality:**

    β(ℓ₁(ℓ₁+1) − ℓ₂(ℓ₂+1)) + α(S₂ − S₁) < N₂ − N₁

**Result: the feasible set is EMPTY.** Three constraints land exactly on
`β = −α/4`:

| pair | constraint | gives |
|---|---|---|
| **2p3/2 → 1f5/2** | −10β − 2.5α < 0 | **β > −α/4** |
| **1g7/2 → 2d5/2** | +14β + 3.5α < 0 | **β < −α/4** |
| **1h9/2 → 2f7/2** | +18β + 4.5α < 0 | **β < −α/4** |

**The ratios are exact: 10/2.5 = 14/3.5 = 18/4.5 = 4.** Both senses strict, so no
(β, α) exists.

**Laubscher's `∓sℓ` falls with it — it is the β = 0 slice.**

### What to do next

**Test forms OUTSIDE the family:**

1. **Woods–Saxon radial shape** — its n- and ℓ-dependence is not `βℓ²`. The
   flattened-bottom potential shifts high-ℓ orbitals down independently of L·S.
2. **A tensor term** — spin-dependent and not captured by `α⟨L·S⟩`.
3. **An ℓ-dependent effective mass** — changes the oscillator spacing itself.

**And test the near-degenerate swaps both ways**, because a form surviving EITHER
ordering is the robust one:

- **(2f7/2, 1h9/2)** at the bottom of the 82–126 shell — inverted between neutrons
  (2f7/2 lower, e.g. ¹³³Sn) and protons (1h9/2 lower, e.g. ²⁰⁹Bi).
- **(3p3/2, 2f5/2)** near the top — near-degenerate, swaps with deformation.

---

## 3 · THE VALIDATED NUCLEAR ORDERING

**Source: Krane, *Introductory Nuclear Physics*; Wong, *Introductory Nuclear
Physics*. Supplied by the person 2026-08-10.**

    1s½   1p3/2  1p½                                    → 2, 8
    1d5/2 2s½    1d3/2                                  → 20
    1f7/2                                               → 28
    2p3/2 1f5/2  2p½    1g9/2                           → 50
    1g7/2 2d5/2  2d3/2  3s½    1h11/2                   → 82
    1h9/2 2f7/2  1i13/2 3p3/2  2f5/2  3p½               → 126

**Capacities are 2j+1.** The 82–126 shell is **10 + 8 + 14 + 4 + 6 + 2 = 44**, and
82 + 44 = 126. **`1i13/2` is an intruder from the N = 6 oscillator shell and fills
THIRD, not last** — a model that closes 126 straight after it is missing the
3p–2f5/2 group of 12.

**This ordering reproduces all seven closures from the capacities alone**, which is
what validates it as input.

---

## 4 · LAUBSCHER'S PDL — what was checked and found

**Cédric Laubscher, *Projective Dynamic Logo*.** Four axioms C1–C4 on finite signed
graphs; the minimal admissible closure is **K₄**. One external parameter,
Δm_iso = m_d − m_u. **Corpus D01–D67, MIT-licensed, at
`github.com/laubscher-lab/PDL-framework`.** Programme closed at D55, May 2026.

**D47 claims the magic numbers as a theorem**: the quasi-completeness equation

    3n_u² + (2Δn − 3)n_u + Δn(Δn − 1) − 1860 = 0

has a perfect-square discriminant **22201 = 149²** for Δn = 4 and no other multiple
of 4, forcing n_u = 24, n_d = 28 and **s = Δn/(2n_u) = 1/12**.

**The three checks, run:**

**ONE — the sequence.** His output is **2, 8, 20, 28, 50, 82, 126**, the observed
sequence including the spin-orbit shift. **But `s = 1/d` gives all seven for EVERY
d from 5 to 39 — thirty-five values.** The magic numbers do not determine s.

**TWO — is 149 load-bearing?** Perturbing `r_val` from 930 by ±1, ±2, ±3 leaves no
Δn with a perfect-square discriminant satisfying C2. **The structure crumbles on
one unit** — which is the fragile-coincidence signature and also what genuine
Diophantine uniqueness looks like; the test cannot separate them. **149 appears
only as √22201**, not as a representation dimension or lattice norm, and Laubscher
says so himself.

**THREE — is 1/12 load-bearing?** It is `Δn/(2n_u) = 4/48`. **Not ζ(−1).** No zeta
regularisation, no anomaly cancellation.

**The finding: the spin-orbit FORM is assumed, not derived. Only its magnitude is
claimed, and the magnitude is unconstrained by the data offered to explain it.**
**And §1370 now refutes the form itself.**

---

## 5 · THE OTHER OPEN WINDOWS

### 5.1 · The ionisation ladders — Λ_ladder cannot close without them

    isoelectronic   11 of 11     complete
    the walk        106 of 106   complete
    ionisation      ~15 of 108   PARTIAL  ← this
    isotopic        none         the only route to Λ_chem's nucleus seat

**The query**: `physics.nist.gov/PhysRefData/ASD/ionEnergy.html`, ASCII format,
ordered by sequence, ticking only *atomic number · spectrum name · ion charge ·
isoelectronic sequence · ground-state electronic shells · ground-state level ·
ionization energy*.

**Split by element range if the whole file will not upload:**

    spectra=H-Ar    Z 1–18    ~171 rows   ← Argon and the light elements
    spectra=K-Kr    Z 19–36   ~495 rows   ← the whole 3d block
    spectra=Rb-Xe · spectra=Cs-Rn · spectra=Fr-Ds

**Two uploads of the full 6,027-row file have failed.** The first range alone
covers Argon's full ladder and every occupied cell of Λ_t.

**What it unlocks**: Λ_t at every charge (currently every value is c = 1), the
three empty cells 7p, 6d, 7d, and Λ_ladder's closure.

### 5.2 · The three-body problem — two targets, neither solved

**A chapter was written on it, audited, and CUT.** It claimed the problem
factorises because there is no third pair, **which is false: a Rydberg atom has
all three pairs and the nucleus attracts the outer electron strongly.** What Λ_var
says is that no VARIABLE relates them directly — a fact about coordinates, not
interaction. **Register 1359.**

**Nothing is written until both a target and a solution exist.**

**THE CLASSICAL** — Poincaré 1890. Not an open question: no additional first
integrals exist algebraic (Bruns 1887), uniform analytic (Poincaré), or
meromorphic (Tsygvintsev 2001). **What IS open is enumerative: Smale's sixth
problem — is the number of central configurations finite?** Proven n = 4 (Hampton
& Moeckel 2006), n = 5 planar for generic masses (Albouy & Kaloshin 2012), open
for n ≥ 6. **The equal-mass case is EXPLICITLY EXCLUDED from those proofs**, which
the literature attributes to technique rather than to the objects. **And
Albouy–Kaloshin's method is an index in all but name: bicolored `zw-diagrams`
enumerating the failure modes, with the count exploding past five bodies.**

**THE ATOMIC** — helium. No closed form for any bound state, and no theorem that
none exists. **The open questions are the doubly-excited-state classification
(approximate quantum numbers N, n, K, T, A that no exact symmetry produces) and
Wannier's threshold exponent E^1.127.**

**The sequencing the person named**: solve the classical equal-mass case first,
then adapt. **The hinge is that mass ratios become exchange symmetry** — two
electrons are identical fermions, so the configuration space is quotiented by
exchange and the quotient carries a sign. **And the nucleus is not a third equal
body, so the atomic case is the RESTRICTED problem.**

### 5.3 · The artefact pass

**`ARTEFACT-PASS.md` is the specification.** Stage one is done — the Index of
Indices has section IX (all thirteen new indexes in full), the Physics Compendium
has Λ_chem and Λ_PCA and the Seaton correction, the Mathematical Compendium has
the corridor, the staircase algebra, the Slater triangle, the falsification and
the observability boundary with attributions.

**Still owed**: the Spectra Compendium wants the session's captures folded into
`COORDINATES.tsv`, **which should wait for the ion ladders.**

### 5.4 · Pinned for later

**Whether `2(N+1)/cap(N)` crossing ½ at N = 3 is a known observation.** It is one
line of arithmetic and someone has probably written it. **A simple attribution is
no longer important unless it furthers the work** (the person's instruction).

---

## 6 · THE PROTOCOLS — they are code, run them

| file | what it does |
|---|---|
| **`domain_protocol.py`** | four questions before any fit. **Blocks pooling.** |
| **`chem_index.py`** | routes a residual to its chemical property and class |
| **`t_index.py`** | Λ_t, the corridor position on (ℓ, n) |
| **`ladder_index.py`** | the four ladder directions and what each reaches |
| **`distinguished_n.py`** | the magic sequences of four many-body systems |
| **`nuclear_corridor.py`** | **the test above** |
| **`ground.py`** | 108 observed neutral ground configurations, NIST ASD 5.12 |

### The domain protocol's four questions

1. **DOMAIN** — which single cell of Λ_phys? If the data spans more than one,
   **stop and fit each separately.**
2. **CARRIER** — which carrier does Λ_law assign? Fitting in another is the law-2
   error.
3. **COUNT** — points ≥ 3 × parameters *in this cell*? If not, **report the
   measurement, not a fit.**
4. **POOLING** — combining cells for more points? **Stop.**

**And the reporting rule**: per-cell results are a LIST of measurements with their
own statistics. **A "median across cells" is a pooled fit in disguise.**

---

## 7 · THE METHOD — the concepts that do the work

**ℛ is the only lens.** Every object goes under it — laws, constants, variables,
parameters, series, charge, amplitudes, chemistry, ladders. **Picking up a
different lens per object is the error.**

**When a piece verifies, ask WHERE ELSE THIS EXACT OBJECT APPEARS**, not what
would break it. The breaking test comes after, and only if the connection fails.
**ℓ(ℓ+1) is one object seen six times**: the gate, the collapse switch, the
barrier, Seaton's ratio, the angular factor 1/(2ℓ+1), and the entry point
√(ℓ(ℓ+1)/2).

**The cypher analysis** — ask each of the six languages (order, analysis, algebra,
geometry, information, statistics) whether it can speak of an object. **A language
that falls silent is the finding.** A quantity that is ordinal, algebraic and
geometric but NOT analytic is an integer object: **it cannot be fitted and needs
no fitting.**

**The observability boundary** — an index closes when its cells are enumerable,
and **what it cannot supply is exactly what requires an operator.** Nine of eleven
unfixable cells are expectation values; Λ_cross is the exception and is the only
index with no statistics language.

**The corridor tests a FORM.** If a form is wrong, some element's inequalities are
inconsistent. **Atoms: 106 of 106 non-empty, so the form survives. Nuclei: empty,
so the form is refuted.** That asymmetry is the corridor doing its job.

**An index is closed when its output class is a SINGLETON.** Two outputs mean the
observer is still choosing which to read.

---

## 8 · THE RULES, ACCUMULATED

- Lock what is measured
- One thing at a time
- Per element, not pooled
- Charge is one symbol in three positions
- Evidence is not an object axis (`standing`, `origin`, `kind`, `state` all failed)
- Calibrate on one atom
- The neutral is not the table
- **Never fit across a language boundary**
- A law holding atom-by-atom need not hold as a walk
- **Read orderings from a source; never compute or recall them**
- Compendia answer, they do not argue
- Figures removed must have their data represented another way

---

## 9 · WHAT WENT WRONG TODAY, SO IT DOES NOT REPEAT

**These are recorded as registers, not hidden.**

**1359** — a chapter claimed the three-body problem factorises because there is no
third pair. **False.** Λ_var's statement is about coordinates, not interaction, and
the two were conflated.

**1369** — the nuclear corridor's first run eliminated all six candidate forms,
caused by **three sign errors in one line** rearranging E₁ < E₂. Caught only
because "all six" was too clean. **And the level ordering was written from memory**
with 1i13/2 last when it fills third, and 1h11/2 in the wrong shell.

**1355** — the protocol blocked a fit about to be offered: `ln(gap)` against core
electron count, r² 0.984, e-folding size 16.6 against 16 at 4%. **Four points, two
parameters, and the slope moves 21.6% on dropping one.**

**1331** — the eighteen surd resets of the atomic walk were reported as a result
**before the selection rule was falsified.** Seven of eight rules give 106/106,
random interior points on 200 of 200 seeds. **The trajectory was mine; the corridor
is the physics.**

**Both errors of 1369 surfaced late in a long session.** That is the pattern, and
the fix is a fresh context plus reading inputs from sources.

---

## 10 · THE FILES TO UPLOAD

**`restore-point-1.6.tar.gz`** — 449 files, everything. **This is the only one
strictly required.**

**Optional, if a quick read is wanted before restoring:** `QUEUE.md`,
`HANDOFF.md` (this file), `ARTEFACT-PASS.md`, and the compendium PDFs.

**The container filesystem does not survive between chats. The tar must be
re-uploaded.**

---

## 11 · WHAT THE TAR CARRIES — verified inventory

**444 files, 38.3 MB uncompressed.** Everything needed to rebuild every artefact
from source.

### The six sources, and the PDFs they build

| source | size | builds |
|---|---|---|
| `The Method 1.6.md` | 721 KB, 11,371 lines | **The Method 1.6.pdf** (3.7 MB) |
| `COMPENDIUM.md` | 174 KB, 3,132 lines | **Mathematical Compendium** |
| `SPECTRA.md` | 72 KB, 857 lines | **Spectra Compendium** |
| `INDICES.md` | 82 KB, 1,755 lines | **The Index of Indices** |
| `PHYSICS.md` | 41 KB, 629 lines | **The Physics Compendium** |
| `REGISTER.md` | 566 KB, 4,717 lines | **The Register** |

**`REGISTER-DATA.md`** (7,244 lines) is the register's SOURCE — entries are
appended there, then `register_gen.py` regenerates `REGISTER.md`.

### The build chain

```bash
cd /home/claude/work
python3 register_gen.py > REGISTER.md          # after adding register entries
python3 "The Method 1.6 press.py"              # builds the book PDF
cp "/mnt/user-data/outputs/The Method 1.6.pdf" .   # audits read the built PDF
python3 press_compendia.py                     # builds all five compendia
```

### The audits — all must pass before sealing

```bash
rm -rf .zeno __pycache__
python3 The_Method_1_6_audits.py               # expect ALL TWENTY-FIVE PASS
python3 compendium_audit.py                    # expect PART 2 PASSES
python3 cross_audit.py                         # expect PART 1 PASSES
python3 mech_audit.py                          # expect MECHANISM LISTS AGREE
python3 appendix_audit.py                      # expect ALL APPENDIX CHECKS PASS
```

**`.zeno/` caches audit state — always `rm -rf .zeno` before a rerun**, or a
stale failure will persist after the fix.

**Audit 20 PROJECTION reads the BUILT PDF**, so the book must be rebuilt and
copied back before that audit is meaningful.

### The data

`COORDINATES.tsv` (the graded coordinate supply) · `CHANNELS-NEW.tsv` ·
`SPECTRA-DATA.tsv` · `PAGEMAP.tsv` · plus 91 further `.tsv` and 14 `.json`
including `RITZ.json`, `WALKED.json`, `PROPAGATED.json`, `channels_map.json`.

**268 Python files** — every analysis script from every session, including all the
protocols of §6 and the session scripts each result was computed with.

**45 PNG figures.**

### To reseal after work

```bash
cd /home/claude/work && rm -rf .zeno __pycache__
cd /mnt/user-data/outputs && rm -f restore-point-1.6.tar.gz
cd /home/claude/work && tar czf /mnt/user-data/outputs/restore-point-1.6.tar.gz \
  --exclude=backups --exclude=.zeno --exclude=__pycache__ .
```

**Then present the tar, the queue and the register PDF** so the person has them.
