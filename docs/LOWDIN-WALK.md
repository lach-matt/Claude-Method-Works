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

**The field is not the record's.** The record's mean field is Hartree–Fock. This instrument's is
the **local-exchange** self-consistent field of Herman and Skillman (1963): Hartree potential of
the density plus Kohn–Sham exchange V_x = −(3ρ/π)^{1/3}, with Latter's tail so that an occupied
orbital sees −(Z − N + 1)/r asymptotically. The added electron of the frontier scan sees the
unmodified field, asymptote −(Z − N)/r = −1/r, which is why a far g channel sits near −1/(2n²)
here as in the record. Non-local exchange is **not reproduced**, and nor are the record's collapse
criterion (register 1703), its correlation clause (1705) or its Z = 91 two-branch diagnostic.
Local exchange is known to bind compact d and f channels more strongly than Hartree–Fock does,
and the divergences below sit exactly where that bias acts.

**Numerics.** Logarithmic grid r = e^x from 10⁻⁷ to 300 bohr, step 0.005 in x, 4,365 points.
The equation is integrated as a first-order pair in x by fourth-order Runge–Kutta, outward from
the r^γ series at the nucleus (γ² = ℓ(ℓ+1) + 1 − (Z/c)²) and inward from the WKB tail, matched at
the outer classical turning point; the eigenvalue is bracketed by node count and refined by the
Hartree matching correction to 10⁻⁹ relative. The error against the exact hydrogenic levels
scales as the fourth power of the step (measured: 3 × 10⁻⁵ at 0.02, 2 × 10⁻⁶ at 0.01, 1 × 10⁻⁷ at
0.005). The field is mixed to a residual below 10⁻⁷ in r·V; every one of the 238 rows converged.
Stdlib only; runs on the default `python3` (3.11).

## What it returns

`LOWDIN-WALK.tsv` at the repository root: **238 rows**, 119 per setting, Z = 2 to 120, one row per
(c, Z). Columns: `c`, `Z`, `symbol`, `cfg_prev` (the chain's own cfg(Z−1)), `entrant`, `D_ent`,
`runner_up`, `D_runner`, `margin` (|D(entrant)| − |D(runner-up)|), `observed_gain` (the channel
that gained an electron from Z−1 to Z in `LW1-ground.py`, or `-` above 108), `agree`, `spectrum`
(every bound candidate, deepest first), `scf_iterations`, `converged`, `status`. Every status is
`RECONSTRUCTED`. Regenerate it, never hand-edit it; `--verify` recomputes one row at each setting
and compares.

## What it measured

Read the two settings first, then the comparison. The record's figures are quoted beside each so
the reader sees both; nothing was adjusted to bring them together.

**At c = 137.035999.** The entrant equals the observed gain at **96 of 107** scored rows. The
eleven disagreements are Mn, Zn, Tc, Ag, Cd, La, Gd, Hg, Th, Cm and Lr — every one a row where
nature rearranges an already-open block or takes d over f, which the chain, never moving an
electron, cannot follow (the record makes the same scope statement for the chromium class,
register 1701). The chain's own configuration is identical to the observed one at 84 of 107.
Clause 1 — smaller n+ℓ opens first — holds without exception over the derived openings, as in the
record. Clause 2 has **one** exception here, 6d at 89 before 5f at 90 (the record's set is
exactly La, Ac, Th): the local field opens 4f at Z = 57 with no lanthanum exception and 5d only at
71, and takes 5f at thorium where the record's collapse criterion takes 6d. 7p opens at 113 here
against the observed 103 (Lr): 5f at lawrencium. The five smallest margins are Ba (6s over 5d by
0.0248 Ha), Ca (0.0272), Cs (0.0488), Ac (0.0555) and Th (0.0614) — the alkaline earths and the
actinide openings, which is where the record places its contested rows too (Z = 38, 56, 72, 89,
105; register 1705). Every g channel is offered at all 119 elements and sits within 4.2 × 10⁻⁴
Ha of −1/(2n²); the record offers 5g at 65 elements, 6g at 70, 7g at 57 and 8g at 28, at
−1/(2n²) to storage precision. The residual here is penetration of the ion's outer shells by the
g orbital's inner lobe, real in this field.

**At c → ∞.** **92 of 107**, with fifteen disagreements; identical configuration at 61 of 107.
Clause 1 holds; clause 2 has two exceptions, 5d at 56 before 4f at 57 and 6d at 88 before 5f at
89 — barium and radium take d in the non-relativistic field, by 0.0037 and 0.0067 Ha. At Z = 120
the entrant is **6f**, and at Z = 119 8s wins over 7d by less than 10⁻⁴ Ha; the 5g channel
departs from −1/(2n²) by 0.21 Ha at the top of the range, which is its collapse beginning in the
non-relativistic local field.

**The two settings against each other.** The entrants differ at **7** elements: Ba (6s | 5d),
Lu (5d | 6s), Ra (7s | 6d), Ac (6d | 5f), Lr (5f | 6d), Cn (6d | 7s) and Ubn (8s | 6f). Register
1706's eleven are Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf. **Two** are displaced here too, Lu
and Lr; **nine** are not; **five** are displaced here and not in the record. At Th the entrant is
5f at both settings — the null-difference control the Löwdin reply asked the site to carry holds,
but by a route the record does not have: the record's entrant at Th is 6d, surviving by path
while the competition inverts; here 5f is collapsed at both settings and wins by 0.061 and 0.044
Ha. The record's Mn, Zn, Ag, Cd and Hg displacements cannot occur in this chain: 4s, 5s and 6s are
full by the time the d block opens at both settings, since the s channel wins at Ca by 0.027 and
0.022 Ha and at Sr by 0.062 and 0.048. For the record's twin to file silver under 5s, its
non-relativistic chain must have taken 4d before 5s at rubidium or strontium; Λ_cinf is not held,
so which it did is not decidable here.

None of this is a finding against the record. The record's construction scored 107 of 107 in a
Hartree–Fock field with a derived collapse criterion; this one scores 96 of 107 in a local-exchange
field without one, and the difference is concentrated at the f openings and the s–d competitions,
which is what the exchange bias predicts. What the reconstruction establishes is narrower and
worth having: the record's algorithm, as stated, run with the record's equation and one constant,
reproduces the ordering clause and the period structure in a field one can build in an afternoon,
and its disagreements with the record are named row by row with the margin at each.

## How to run it

```
python3 tools/lowdin_walk.py --selftest                      # 29 checks, about 2 s
python3 tools/lowdin_walk.py --z 47 --c 137.035999 --from observed
python3 tools/lowdin_walk.py --z 90 --c inf --from observed  # one step, 4–9 s each
python3 tools/lowdin_walk.py --goldens                        # Ag, Hg, Th at both settings
python3 tools/lowdin_walk.py --chain --c 137.035999 --out c137.tsv   # 119 rows, ~8 min
python3 tools/lowdin_walk.py --chain --c inf --out cinf.tsv          # ~6 min
python3 tools/lowdin_walk.py --merge c137.tsv cinf.tsv --out LOWDIN-WALK.tsv
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
and puts each element's two rows, spectra included, into its element file; the six functions of
the instrument travel verbatim in `instruments` as `walk_*`, RECONSTRUCTED. The page draws the
reconstruction's displaced elements with a hollow corner mark apart from the record's filled one,
the element plate carries "The walk, reconstructed" beside "Relativistic limit", the console
answers `walk <El>`, and the seventh solver mode gains `walk` and `compare` operations while its
`recompute` still refuses the record's table and names the reconstruction beside it. See
`docs/WEB-INDEX.md`.

## What it is not

It is not Λ_chain, Λ_cinf, or any object of the Löwdin delivery, and it is not a member. It writes
to none of `method/`, `drive/`, `extracted/` or `recovered/`. Its output is generated —
regenerate, never hand-edit — and its statuses are never flattened: a reader who quotes a
figure from `LOWDIN-WALK.tsv` quotes a RECONSTRUCTED figure. A Hartree–Fock field, with the
record's non-local exchange, is the build that would let the comparison be made in the record's
own field; it is not attempted here, and nothing above should be read as if it had been.
