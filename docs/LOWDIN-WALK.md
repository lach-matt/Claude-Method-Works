# The walk, reconstructed — `tools/lowdin_walk.py` and `LOWDIN-WALK.tsv`

*The Löwdin solution's entrant walk, rebuilt from the record's own statement of it and run
at both settings of c. Everything it returns is **RECONSTRUCTED**, and the record's own tables
stay unheld and READ. Neither is repaired against the other.*

## Why it exists

The record states the construction that derives the periodic table and its results —
`THE-LOWDIN-SOLUTION-2.md` §II, the Mathematical Compendium's family LS, registers 1701–1712 —
but not the construction itself. Its SCF chain code, Λ_chain (119 rows) and Λ_cinf (107 rows)
were sealed in `LOWDIN-HANDOFF-103.tgz`, which the Löwdin delivery README records as pending
bank and which never arrived; session 104, which produced the paper and its figures, was never
sealed (`LW1-README.md`). The site's seventh solver mode therefore read the record's result and
refused to recompute it, and the Löwdin project's reply of 2026-09-18
(`drive/The Method Materials/LOWDIN-DELIVERY-1/LW1-ADDENDUM-REPLY.md`) measured the same thing
from its side: the one code store it held contains thirteen corridor-line instruments, not one an
SCF solver, not one taking c. It committed a single-Z wrapper on bank receipt. The Löwdin project
has since concluded, and the author's ruling was that anything still needed is this
repository's to build.

This instrument is that build. It is not the record's code and it does not use the record's
field; it runs the record's algorithm in a field it can construct here, and it places what
comes out beside the record with its status on every value.

## What it does

The record's algorithm, verbatim (`THE-LOWDIN-SOLUTION-2.md` §II.2):

```
cfg(1) := 1s¹
for Z = 2 … 120:
    F := converged self-consistent field of the ion with nuclear charge Z
         and electron configuration cfg(Z−1)                  (the V^{N−1} field)
    for each unfilled frontier channel (n, ℓ):
        D(n,ℓ) := binding depth of one electron placed in channel (n, ℓ) of the frozen field F
    entrant(Z) := the channel of greatest depth
    cfg(Z)     := cfg(Z−1) + one electron in entrant(Z)
```

run twice: at c = 137.035999, register 1701's one entered constant, and at c → ∞, register 1706's
twin. The frontier is every (n, ℓ) up to 8s and 8g that is not full in cfg(Z−1) and that binds in
the frozen field. The chain builds on its own derived configuration at every step, never on the
observed one, and never moves an electron already placed — as the record's does (§II.2, §VI.2).

**The radial equation is the record's.** Koelling–Harmon's scalar-relativistic reduction of the
Dirac equation, with c entering once:

```
P'' − (M'/M)(P' − P/r) = [ℓ(ℓ+1)/r² + 2M(V − ε)] P ,   M = 1 + (ε − V)/(2c²)
```

At ℓ = 0 this *is* the Dirac κ = −1 equation, so the hydrogenic 1s at every Z is an exact
fixture, ε = c²(√(1 − (Z/c)²) − 1); at c → ∞ it is Schrödinger's, and every hydrogenic level is,
ε = −Z²/(2n²). The selftest asserts both to 2 × 10⁻⁷ relative, at Z up to 120, and asserts that
the relativistic term with the wrong sign **fails** the Dirac fixture — the record's own demand
(§III) that every instrument carry a demonstrable failure mode.

**Two fields, and the second is the record's.** The instrument runs the chain in two mean
fields, chosen by `--field`, and the table carries both under a `field` column.

*`lx`, local exchange.* The self-consistent field of Herman and Skillman (1963): Hartree
potential of the density plus Kohn–Sham exchange V_x = −(3ρ/π)^{1/3}, with Latter's tail so that
an occupied orbital sees −(Z − N + 1)/r asymptotically. The added electron of the frontier scan
sees the unmodified field, asymptote −(Z − N)/r = −1/r. Local exchange is known to bind compact
d and f channels more strongly than Hartree–Fock does, and its divergences from the record sit
exactly where that bias acts. It is also the start every Hartree–Fock field is converged from.

*`hf`, Hartree–Fock.* The average-of-configuration Hartree–Fock field with non-local exchange —
the object Bach, Lieb, Loss and Solovej's theorem is about, which the record names as its
well-posedness condition (§X, Law C) — under the same Koelling–Harmon kinetic operator. For a
shell a of occupation q_a:

```
(T + V_a) P_a − X_a = ε_a P_a + Σ_b ε_ab P_b
V_a = −Z/r + (q_a−1)[Y⁰(aa) − (2ℓ+1)/(4ℓ+1) Σ_{k>0} a_k(ℓ,ℓ) Y^k(aa)]/r + Σ_{b≠a} q_b Y⁰(bb)/r
X_a = Σ_{b≠a} ½ q_b Σ_k a_k(ℓ_a,ℓ_b) Y^k(ab)/r · P_b ,     a_k(ℓ,ℓ') = (ℓ k ℓ'; 0 0 0)²
```

Each equation is solved as an inhomogeneous shooting problem: homogeneous and particular
solutions integrated out and in with a shared coefficient pass, matched at the turning point,
the eigenvalue fixed by the norm condition ∫P² = 1 on the branch below the local eigenvalue
(the exchange operator is positive, so the Hartree–Fock root lies below it, where the norm falls
from its pole and crosses one exactly once). The inward integration starts where the WKB decay
from the turning point reaches e⁻¹², not further: the homogeneous solution grows by that same
factor and the matching subtracts it from the particular branch, so a longer span costs digits.
Orbitals of one ℓ are coupled by off-diagonal multipliers ε_ab. Each equation carries its own
and, at the root, one exact Newton step (one particular solution per partner, the problem being
linear in its source) moves them to the values that make the solution orthogonal, so every
equation holds exactly with an orthonormal set. What that leaves free is the rotation angle of
each coupled pair within its own span, and the variational condition q_a ε_ab = q_b ε_ba fixes it
(Froese Fischer's rotation analysis): after every sweep each pair takes a Newton step toward the
angle at which the energy is stationary, with the exact gradient 2(q_a⟨b|F_a|a⟩ − q_b⟨a|F_b|b⟩)
from the state's orbitals and the curvature from the energy at three angles. Nothing is
Schmidt-orthogonalised — a Schmidt step after mixing admits fixed points at which the solved
orbital differs from the stored one by a multiple of its partner, and the equations then hold
only up to that residual; two such fixed points, at 3 × 10⁻⁵ and 10⁻³ hartree from the exact
values, were found and discarded on the way to this scheme. A pair of closed shells carries no
multiplier and no rotation: the energy is invariant under their rotation, every rotated pair
solves the coupled equations, and only the canonical pair carries the orbital energies the
record compares. The added electron of the scan sees the same operator at the full occupation,
its own exchange with every occupied orbital and its multipliers against the occupied orbitals of
its ℓ iterated until the overlaps vanish. One approximation is stated and is the field's only
one: the one-electron part of the rotation energy is non-relativistic; the operators solved are
Koelling–Harmon throughout, and the angle is a correction.

The fixtures are the exact numerical Hartree–Fock orbital energies of Froese Fischer and of
Clementi and Roetti, at c → ∞, reproduced to 2 × 10⁻⁴ or better (most to 10⁻⁶): He 1s
−0.917956, Li 2s −0.196323, Be 2s −0.309270, B 2p −0.309856, Ne 2p −0.850410, Na 3s −0.182103,
Ar 3p −0.591017 — closed shells, single open shells, and open shells coupled to one and to two
closed shells of the same ℓ, which is where a multiplier scheme fails if it is going to.

Neither field reproduces the record's collapse criterion (register 1703), its correlation clause
(1705) or its Z = 91 two-branch diagnostic; and the `hf` field is a rebuild from the record's
statement, not the record's code, which never arrived.

**Numerics.** Logarithmic grid r = e^x from 10⁻⁷ to 300 bohr, step 0.005 in x, 4,365 points.
The equation is integrated as a first-order pair in x by fourth-order Runge–Kutta, outward from
the r^γ series at the nucleus (γ² = ℓ(ℓ+1) + 1 − (Z/c)²) and inward from the WKB tail, matched at
the outer classical turning point; the eigenvalue is bracketed by node count and refined by the
Hartree matching correction to 10⁻⁹ relative. The error against the exact hydrogenic levels
scales as the fourth power of the step (measured: 3 × 10⁻⁵ at 0.02, 2 × 10⁻⁶ at 0.01, 1 × 10⁻⁷ at
0.005). The local-exchange field is mixed to a residual below 10⁻⁷ in r·V and every one of its 238 rows
converged; the Hartree–Fock field to 10⁻⁷ in the orbitals, 10⁻⁶ in every overlap and angle, and
three of its 238 rows did not reach it, which the table says on the row (below).
Stdlib only; runs on the default `python3` (3.11).

## What it returns

`LOWDIN-WALK.tsv` at the repository root: one row per (field, c, Z), Z = 2 to 120, 119 rows per
(field, setting). Columns: `field` (`lx` or `hf`), `c`, `Z`, `symbol`, `cfg_prev` (the chain's own
cfg(Z−1)), `entrant`, `D_ent`, `runner_up`, `D_runner`, `margin` (|D(entrant)| − |D(runner-up)|),
`observed_gain` (the channel that gained an electron from Z−1 to Z in `LW1-ground.py`, or `-`
above 108), `agree`, `spectrum` (every bound candidate, deepest first), `scf_iterations`,
`converged`, `status`, `note` (empty, or what went wrong: a field that did not converge says so
with its residuals, and a Hartree–Fock step that failed twice says the row carries the
local-exchange result). Every status is `RECONSTRUCTED`. Regenerate it, never hand-edit it;
`--verify` recomputes one row per (field, setting) and compares.

## What it measured

Read the Hartree–Fock field first — it is the record's own — then the local-exchange field
beside it, then the comparisons. The record's figures are quoted beside each so the reader sees
both; nothing was adjusted to bring them together. Every figure below is `--report`'s, and
`tools/docfigures.py` pins the counts.

**Hartree–Fock at c = 137.035999.** The entrant equals the observed gain at **94 of 107** scored
rows. The thirteen disagreements are Mn, Zn, Tc, Ag, Cd, Ce, Gd, Lu, Hf, Hg, Cm, Lr and Rf — the
six of the chromium class (Mn, Zn, Tc, Ag, Cd, Hg), where nature rearranges an already-open block
and the chain, never moving an electron, cannot follow (the record makes the same scope statement,
register 1701), and seven in the f blocks — at their edges and half-filled points — and the
actinide openings. The chain's own configuration is
identical to the observed one at 70 of 107. The derived opening sequence is the observed one in
the same order — 5d at 57, 4f at 59, 6p at 81, 7s at 87, 6d at 89, 5f at 91, 7p at 113, 8s at
119 — differing in Z only at 4f (59 against 58) and 7p (113 against 103, lawrencium). Clause 1,
smaller n+ℓ opens first, holds without exception. Clause 2 has **two** exceptions, 5d at 57 before
4f at 59 and 6d at 89 before 5f at 91 — **lanthanum and actinium**, which are two of the record's
three (La, Ac, Th); at thorium the entrant is **6d**, as the record has it, with 5f uncollapsed.
Every g channel is offered at all 119 elements and sits within **2.5 × 10⁻⁶** Ha of −1/(2n²) —
the record's "−1/(2n²) to storage precision", which the local field missed by 4 × 10⁻⁴,
reproduced once the exchange is non-local (the record offers 5g at 65 elements, 6g at 70, 7g at
57 and 8g at 28). The five smallest margins are Ce (5d over 4f by 0.0014 Ha), Pa (5f over 6d by
0.0053), Y (4d over 5p by 0.0199), Ac (6d over 7p by 0.0204) and Db (6d over 7p by 0.0292).

Three rows did not converge, and the table records them as such: **Ts, Og and Ubn**, at 7p⁴, 7p⁵
and 8s¹, with residuals of 6.4 × 10⁻⁷, 6.1 × 10⁻⁶ and 1.5 × 10⁻⁶ against a tolerance of 10⁻⁷.
At each the eigenvalues are still to 10⁻⁸ and every overlap is below 2 × 10⁻⁷; the residual sits
in one deep closed shell's equation — at Ts the 2p, whose multiplier against the open 7p is
−575 Ha — and repeats sweep after sweep. The mechanism is the one the rotation release names:
under the Koelling–Harmon operator each orbital's kinetic term is taken at its own energy, so the
coupled equations of one ℓ are not a single Hermitian problem and the orthogonal solution and
the energy-stationary one disagree by a residual that no mixing removes (at Ubn the rotation was
released at sweep 21 with the two 2.0 × 10⁻² rad apart). The same three configurations converge
in 17, 17 and 18 sweeps at c → ∞, where the operator is one. The entrant margins at the three
rows are 0.158, 0.280 and 0.236 Ha, four to five orders above the residual; the rows stand, marked
`converged = no` with the residuals in `note`, and they are not repaired.

**Hartree–Fock at c → ∞.** **96 of 107**, with eleven disagreements — the chromium six, Gd, Lu,
Th (5f against 6d), Cm and Lr; identical configuration at 76 of 107. The openings are the
observed ones in the observed order, differing only at 5f (90 against 91) and 7p; clause 2 has
the same two exceptions, La and Ac. The g channels sit within 7.1 × 10⁻⁶ of −1/(2n²). At Z = 120
the entrant is **7d** over 8s by 0.0034 Ha, the smallest margin at this setting, and 8s wins 7d at
119 by 0.0200; the others of the five are Ra (7s over 6d by 0.0175), Ba (6s over 5d by 0.0273)
and Fr (7s over 7p by 0.0308).

**The two settings against each other, in the record's field.** The entrants differ at **5**
elements: Ce (5d | 4f), Hf (4f | 5d), Th (6d | 5f), Rf (5f | 6d) and Ubn (8s | 7d). Register
1706's eleven are Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf. **One** is displaced here too,
**Rf**; ten are not; four are displaced here and not in the record. At Th the entrant is **6d at
c = 137.035999 and 5f at c → ∞**: the record's own c = 137 entrant, and the record's own
statement that the competition inverts at c → ∞ — what this field lacks is the path clause by
which the record's entrant survives the inversion (register 1703's collapse criterion, which no
field here has), so here the entrant follows the competition. The record's Mn, Zn, Ag, Cd and Hg
displacements cannot occur in this chain at either setting: the s channel wins at Ca by 0.058
and 0.057 Ha, at Sr by 0.072 and 0.051 and at Ba by 0.047 and 0.027, so 4s, 5s and 6s are full
by the time each d block opens (in the local field the same holds at Ca and Sr, by 0.027 and
0.022 and by 0.062 and 0.048, while barium takes 5d at c → ∞ by 0.0037). For the record's twin to file silver under 5s, its non-relativistic chain must have taken
4d before 5s at rubidium or strontium; Λ_cinf is not held, so which it did is not decidable here.

**Local exchange at c = 137.035999.** **96 of 107**, with eleven disagreements — Mn, Zn, Tc, Ag,
Cd, La, Gd, Hg, Th, Cm and Lr; identical configuration at 84 of 107. Clause 1 holds; clause 2
has **one** exception, 6d at 89 before 5f at 90: the local field opens 4f at 57 with no lanthanum
exception and 5d only at 71, and takes 5f at thorium where the record takes 6d. The g channels
sit within 4.2 × 10⁻⁴ of −1/(2n²), the residual being penetration of the ion's outer shells by
the g orbital's inner lobe in a local field. The five smallest margins are Ba (6s over 5d by
0.0248 Ha), Ca (0.0272), Cs (0.0488), Ac (0.0555) and Th (0.0614).

**Local exchange at c → ∞.** **92 of 107**, fifteen disagreements, identical configuration at 61
of 107; clause 2 has two exceptions, 5d at 56 and 6d at 88, barium and radium taking d by 0.0037
and 0.0067 Ha. At Z = 120 the entrant is 6f, and the 5g channel departs from −1/(2n²) by 0.21 Ha
at the top of the range: the g collapse beginning in a local field.

**The two settings against each other, in the local field.** The entrants differ at **7**: Ba
(6s | 5d), Lu (5d | 6s), Ra (7s | 6d), Ac (6d | 5f), Lr (5f | 6d), Cn (6d | 7s) and Ubn (8s | 6f);
**two** of the record's eleven, Lu and Lr; five displaced here and not in the record. At Th the
entrant is 5f at both settings — the null-difference control holds, but by a route the record
does not have, 5f collapsed at both.

**The two fields against each other at c = 137.035999.** The entrants differ at **6** elements —
La, Ce, Lu, Hf, Th and Rf — every one at an f-block boundary or an actinide opening, which is
where local exchange's stronger binding of compact d and f channels acts. Going from the local
field to the record's moves the lanthanum exception into place, moves thorium to 6d, restores
the g channels to −1/(2n²), moves the displaced set from Lu and Lr to Rf, and costs two rows at
Ce and Hf.

None of this is a finding against the record. The record's construction scored 107 of 107 with a
derived collapse criterion; this one scores 94 and 96 in the record's own field without one, and
its disagreements are the chromium class the record itself excludes plus the f-block edges where
the criterion decides. What the reconstruction establishes is narrower and worth having: the
record's algorithm, as stated, run with the record's equation, the record's field and one
constant, reproduces the ordering clause, the period structure, the lanthanum and actinium
exceptions, the thorium entrant and the g-channel storage precision, and every disagreement with
the record is named row by row with the margin at each.

**How the Hartree–Fock rows were assembled.** Each Hartree–Fock setting ran as two chain
segments on separate cores: one from Z = 2 and one seeded at Z = 60 with the local-exchange
chain's configuration there. A chain step depends on cfg(Z − 1) alone, so a segment's rows are the
chain's own from the first Z at which its configuration equals the chain's: at c = 137.035999
the two coincide from Z = 73, at c → ∞ from Z = 62, and the table holds the first segment to 72
and 61 and the second from there. The seed rows themselves were dropped. About three hours per
setting.

## How to run it

```
python3 tools/lowdin_walk.py --selftest                      # 39 checks, about 25 s
python3 tools/lowdin_walk.py --z 47 --c 137.035999 --from observed              # lx, 4 s
python3 tools/lowdin_walk.py --z 90 --c inf --field hf --from observed          # hf, minutes
python3 tools/lowdin_walk.py --goldens [--field hf]           # Ag, Hg, Th at both settings
python3 tools/lowdin_walk.py --chain --c 137.035999 --out lx-c137.tsv           # 119 rows, ~8 min
python3 tools/lowdin_walk.py --chain --c inf --out lx-cinf.tsv                  # ~6 min
python3 tools/lowdin_walk.py --chain --c 137.035999 --field hf --out hf-c137.tsv  # hours
python3 tools/lowdin_walk.py --chain --c inf --field hf --out hf-cinf.tsv
python3 tools/lowdin_walk.py --merge lx-c137.tsv lx-cinf.tsv hf-c137.tsv hf-cinf.tsv --out LOWDIN-WALK.tsv
python3 tools/lowdin_walk.py --report LOWDIN-WALK.tsv [--json]
python3 tools/lowdin_walk.py --verify LOWDIN-WALK.tsv
```

`--z` with `--from observed` takes cfg(Z−1) from `LW1-ground.py` (register 1306), so a single
step runs standalone from the measured table, as the Löwdin reply's single-Z wrapper was to; with
`--from chain --chain-file LOWDIN-WALK.tsv` it takes the chain's own cfg(Z−1). `--chain` resumes
from an existing output file unless `--no-resume`; `--fields DIR` stores every converged field as
JSON. `--report --json` is what `tools/webindex.py` and `tools/docfigures.py` read.

## Where it goes

`tools/webindex.py` reads `LOWDIN-WALK.tsv` into `public/data/index.js` as
`relativistic.walk` — the table's md5, the summary above as data, one entrant per Z per setting —
and puts each element's four rows, spectra included, into its element file; the ten functions of
the instrument travel verbatim in `instruments` as `walk_*`, RECONSTRUCTED. The Hartree–Fock
field is the primary — the record's own — and the local-exchange field stands beside it, both
carried whole. The page draws the
Hartree–Fock reconstruction's displaced elements with a hollow corner mark apart from the record's
filled one,
the element plate carries "The walk, reconstructed" beside "Relativistic limit", the console
answers `walk <El>`, and the seventh solver mode gains `walk` and `compare` operations while its
`recompute` still refuses the record's table and names the reconstruction beside it. See
`docs/WEB-INDEX.md`.

## What it is not

It is not Λ_chain, Λ_cinf, or any object of the Löwdin delivery, and it is not a member. It writes
to none of `method/`, `drive/`, `extracted/` or `recovered/`. Its output is generated —
regenerate, never hand-edit — and its statuses are never flattened: a reader who quotes a
figure from `LOWDIN-WALK.tsv` quotes a RECONSTRUCTED figure. The Hartree–Fock field is a
rebuild from the record's statement of its equations, not the record's code, and its three
unconverged rows are recorded as such rather than repaired or relaxed into `converged = yes`.
