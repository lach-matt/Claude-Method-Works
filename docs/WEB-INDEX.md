# `public/` — the index as an interactive website

The Method 1.6, read as a zoomable index in the manner of OneZoom: the drawn periodic layout at
the top, each element opening into its ions, each ion into its ℓ channels, each channel into its
cells, and **every value carrying the status the corpus gives it.** Built for scientists,
researchers and students as a research tool, not a brochure.

```sh
python3 tools/webindex.py             # write public/data/ from the instruments
python3 tools/webindex.py --selftest  # 76 fixtures, nothing written
python3 tools/webindex.py --verify    # public/data/ against its own manifest and the sources
cd public && python3 -m http.server   # then open http://localhost:8000/ — or open public/index.html directly
```

Stdlib only on the Python side; no build step, no package manager, no framework on the web side.
`public/index.html`, `public/style.css` and `public/script.js` are hand-written; everything under
`public/data/` is generated and never hand-edited.

## What it shows

| level | node | drawn from |
| --- | --- | --- |
| the index | the drawn layout of section 6 (period × group), Janet's (n+ℓ, ℓ), or Λ_spectra as a lattice in three dimensions | `index.js` → `layout`, `closure`, `lattice` |
| element | Z, symbol, ground shells and level, configuration table, layout cell, closure, Λ₈ ladder; drawn as its slab of the lattice, or as nested circles | `elements/<Z>.js` (populate.py's record) |
| ion | spectroscopic stage, Nₑ, core, the eight channels, the Λ₈ step at that stage | the element record's `channels` and `lambda8` |
| channel | ℓ, p, n₀, B, C(Z, ℓ), δ by equation, and its cells | one entry of `channels` |
| cell | δ, grade, witness, source, bound note, B in the csv against B computed, residual | one row of COORDINATES-2.13 |

Two layouts of the same elements, because the corpus reads the two indexes differently: on the
period × group layout ℛ admits 126 cells against 90 held, **E = 36**, and the 36 are drawn as
ghosts, each a node with its own explanation; on Janet's coordinate **E = 0** and there are no
ghosts to draw. The layout toggle is the closure figure made visible.

**Each of the thirty-six carries the definition section 6.1.1 gives it.** The book names every one:
a subshell of the row it sits in, ℓ read off the group (s at 1–2, d at 3–12, p at 13–18,
`Transitions.md` L368), and the hydrogenic bound ℓ ≤ n−1 of section 7.1 splits them — **25
forbidden** (1d at period 1 groups 3–12, 1p at groups 13–17, 2d at period 2 groups 3–12: orbitals
that cannot exist) and **11 deferred** (3d at period 3 groups 3–12, real but filled after 4s and
drawn in period 4, and period 1 group 2, the slot helium vacates, which ℓ = 0 satisfies the bound
in). Register 448 rules the split 25 + 11, not 26 + 10, and the discrepancy is helium. `webindex.py`
derives each cell's class from the bound (`closure.denied_cells`), asserts the derivation against
the book's own totals in its selftest, and carries the totals as `closure.decomposition` READ; the
canvas labels each ghost with its subshell, dashed for forbidden and dotted with a faint fill for
deferred, and the ghost's plate states the definition in words with the status on each row. The
corpus also rules what the thirty-six are **not**: the void is `L.void`, chapter 10's
box-minus-lattice remainder, and PROSE-ONLY rows PO-0014 and PO-0410 refuse the conflation, so the
plate says so. Register 448 adds that **E is placement-sensitive** — 36 with helium at group 18,
**20** with helium at group 2, E pricing the choice at sixteen cells — and `webindex.py` computes
both closures with cypher's own ℛ, helium moved and nothing else (`closure.placement`, READ against
the register, the recomputation DERIVED). The root plate and every ghost's plate offer *Draw helium
at group 2*: the frames are rebuilt from the build's two closures, twenty ghosts remain, and the
closure solver's browser selftest reproduces E = 20 from the ninety cells with helium moved.

**The lattice, in three dimensions.** An element opens as its slab of Λ_spectra, drawn the way
the record draws the index — the Index of Indices' Figure 6 ("element across, ℓ into the page,
ionisation stage up"), the Löwdin paper's Figure 1(b), and the record's own archived renderer
(`extracted/archives/restore-point-2-13/spectra-lattice.html`, x = Z, y = stage, z = ℓ, a known
cell a cube of edge 0.86 and an unmeasured one of 0.30): ionisation stage up, ℓ into the page, one
node per cell, the cells of a site side by side along the third axis where it holds two
multiplicities. A node carries the nested view's own mark — a filled sphere for a measured cell, a
paper disc ringed in green for an exact one, a small grey dot for a computed one, the witnessed ring
outside a measured node, the limit colours when that facet is on — so the two readings of an element
share one vocabulary; unmeasured nodes are the faint body of the slab; the Λ₈ ladder climbs the front edge, one
rung per recorded step; the stage axis carries every ion as a tappable roman numeral and the ℓ axis
its letters. Drag rotates, wheel or pinch zooms, arrow keys rotate, a tap on a node selects the cell
and on a numeral the ion, and the plate follows as on the plane. The third layout, **Lattice**, is
the whole solid: every element a slab at its Z (charge 1..Z by ℓ 0..7 — `webindex.py` asserts the
58,080 sites are exactly that), the 1,287 known cells as nodes, one per site, from a compact block
`index.js` → `lattice` carries (`[Z, charge, ℓ, mult, grade]` for every measured or exact row; the
axes READ from the record's caption, the drawing DERIVED, nothing computed); the measured wedge at
low Z and low ℓ is the record's own remark made visible, and a tap on a slab opens the element. The
**Nest** toggle shows an element as the nested circles instead — ions, channels, cells — which is
the reading the plane used alone before. The renderer is hand-written on the same canvas: a yaw and
pitch about the scene's centre, a mild perspective, faces sorted far to near and shaded by a fixed
light, no library, so the page still opens from a plain file on a phone. The scene is fitted to the
viewport by the projected extent of its corners at the home angle (the focal length and centring are
kept on the orbit so the scene does not swim as it turns, and refitted on resize), and **every scene
fits its canvas whole at the home view** — a heavy element is a needle by the record's own geometry,
and its ions come apart under the reader's zoom, when the scene scrolls under a vertical drag with
a chip at the clipped edge counting the hidden stages (an earlier reading kept the ions 13 px
apart and let the slab overrun the canvas; it was withdrawn because a rendering must fit the window
it occupies). A node's radius on screen is capped at 22 px at the fitted zoom, growing with the
zoom, so a scene a few cells wide does not fill the canvas with a handful of spheres; the hit test
uses the same radius. The slab stands on a base plane ruled
by ℓ inside a hairline silhouette, unmeasured cells are small faint dots, the ladder carries a dot
on each rung's ion, the numerals and letters are set in the sans, and the whole-index view labels
the slabs with their symbols where there is room and rules its base every ten Z. The element plate's
"The lattice" section names the axes with their source and counts the cubes drawn, and the console
answers `lattice`.

**Particles and binders (built only with `--with-particles`; see *The public build* below).** The lattice is electrons-only by construction — its coordinates carry
configuration and not scale, so a muonic atom occupies the same cell as its electronic twin
(`Muon_Catalysed_Fusion_v1.1.md` §2.1) and the lattice produces pure numbers and no rate (Register
L421, the dimensional obstruction). What the corpus states of the particles beyond the electron is
therefore not a set of cells but a set of passages, and the *Particles* dialog carries them with
their statuses, each figure parsed at build out of the passage that states it (`webindex.py`
`particles_block`; a passage the corpus no longer states fails the build rather than defaulting):
the binder window [119, 918] mₑ with its occupants, the muon (207 mₑ printed, 206.7683 PDG in fault
14f-04) and the pion (273), the muon interior by 1.74× and 4.44×, and the molecular bound-state
counts 60.6, 4.21 and 1.03 for electron, muon and tau; the paper's exclusion table (the pion, kaon,
antiproton and Σ⁻ by nuclear absorption, the tau by index degeneracy); the energy balance's own
header table of inputs and statuses, read from `tools/mucf.py` (MEASURED, PINNED, PROJECTED,
EXTRAPOLATED, PROSE-ONLY), with v1.1's reclassification of the 5 GeV figure as aspirational and the
collection budget's machine figures from `tools/collector.py` (MuSIC, Mu2e, COMET, each with its
arXiv identifier); PART K of `recovered/structural-results.md` — Λ CPT-invariant, antimatter cell for
cell, ALPHA's antihydrogen at 2 × 10⁻¹², and the reduced-mass table of positronium, hydrogen and
antihydrogen, muonic hydrogen and antiprotonic helium — RECOVERED, unbundled, with no instrument;
antiprotonic helium's worked cell (35, 33) with its two disjoint routes agreeing at 0.09σ and the
prose-only ruling that it enters as a scope statement, not as cells; the photon's single restored
cell, E = 1, the one checkable claim of that index, and false; the 27 constants of Λ_phys, the
withdrawn one struck through; ten PROSE-ONLY rows; and the terms counted absent from the corpus at
build (neutrino, gluon, Higgs, muonium, protonium, kaon by name, positronium outside `recovered/`),
so that "absent" is measured and never assumed. **The eighth solver mode runs the muon energy
balance** — N = φλ_c/(λ₀ + ω_s φλ_c), Q, the production cost at which Q reaches a target under the
heat and the work conventions, Q across the transfer-rate band, the breakeven sticking by bisection
and the muon rate a fusion power needs — ported term for term from `tools/mucf.py`, whose seven
functions travel as `mucf_*` instruments; every input carries the paper's status and the result the
weakest of them, and below the 0.30 GeV kinematic floor the mode refuses. Its selftest reproduces
the paper's Table 5.1 (the 0.234 % row at the unrounded transfer rate, the instrument's own recorded
finding, NOTED and not repaired), the section 5.1 breakeven thresholds, the composed lever, the
sticking ceiling and the status rules, from fixtures the build read out of the instrument. The
console answers `particles`, `particle <term>` and `references [term]`.

**References, linked by construction.** The corpus links one data source itself — NIST ASD ver.
5.12 at `physics.nist.gov/asd`, DOI 10.18434/T4W30F, cited for the ground configurations of
`LW1-ground.py` and for the dated retrieval 25 measured cells name — and prints identifiers for the
rest: `webindex.py` finds every arXiv and DOI identifier over `method/members` and `papers/` at
build (53 arXiv, 7 DOI), and the *References* dialog links them (`arxiv.org/abs/<id>`,
`doi.org/<doi>`); the citing line is quoted beside an identifier only where the citing file is
one of the released papers, and never with a file name or line number of the books. Section B.1 of the Spectra
Compendium is parsed into a species → compilation table (26 species), so a measured cell's plate
resolves its `source` column: a dated NIST retrieval or a B.1 species drawn from NIST ASD links to
the database and its DOI; Kaufman & Martin, Kramida & Martin and Sansonetti are cited as strings,
because the corpus prints no identifier for them and a target would be invented; a computed cell
links nowhere. The element plate's References section carries the NIST link for the ground
configuration and the sources of the element's measured cells. The query itself is not held
(`LW1-README.md`), so the database is linked and the query is not.

Elements 109 to 120 are drawn apart, dashed, because `LW1-ground.py` stops at 108 and
COORDINATES-2.13 does not. Their rows are shown `READ` from the csv with no configuration,
equation or derived value behind them, and the panel says so.

## The table as a lattice

**The drawn periodic layout is also a rotatable lattice.** The *Table (3D)* layout draws the same
layout with a third axis — group across, period up with period 1 at the top, ℓ into the page — so
the s, p, d and f blocks stand as layers. Every element is a node at its drawn cell in its block's
layer, coloured by block and carrying its symbol; the thirty-six ghosts are hollow nodes in the
layer the ℓ-by-group rule gives them, the deferred ones fuller, each with its subshell written in;
helium moves to group 2 and the ghosts to the twenty of that placement when the toggle is on. The
set-aside lanthanides and actinides, which the layout gives no group, are drawn in their period
rows at the long-form table's columns 3 to 16 (x = 3 + Z − 58, and Z − 90), a **DERIVED**
placement the caption states each time; elements 119 and 120 sit in period 8 in the s layer with
the spectra-rows tint. The nodes are the plane view's own nodes, so a tap opens the element's slab
or the ghost's definition, Esc returns to the table, and the caption names what is drawn.
`buildTableScene` builds it from `layout` and `state.ghosts`, `drawTableAxes` draws the base, the
four layer frames and the three axes, and the camera, fit, orbit and hit test are the lattice's.

## Set like a reference work

The page is set the way a reference work is read, and the choices are recorded here so a later
hand keeps them. **Type:** IBM Plex Sans for prose and the interface, IBM Plex Serif for the title,
node titles and section heads, IBM Plex Mono only for numbers, symbols, identifiers and code — the
canvas draws element symbols in the serif, labels in the sans and numerals in the mono, all read
from the stylesheet's tokens through one helper, so no face is named in the script. **Palette:**
light by default (warm paper, near-black ink, one deep-blue accent), dark by explicit choice through
the toggle or a host's `data-theme="dark"`; the grade colours (measured, exact, computed) are
desaturated so they still read without glowing, the block tints are pale, and the thirty-six ghosts
are tints rather than dashes. **Statuses are labels, not badges:** every value still carries one,
as small capitals in the muted grey at the row's end, coloured only where it warns (RECOVERED and
PROJECTED amber, RECONSTRUCTED and PROSE-ONLY purple, EXTRAPOLATED and REFUSED red). **The frame:**
a masthead with the title, a one-line statement and the edition (the data's commit and build date,
from `index.js`'s own meta), the path and the caption in a bar above the canvas rather than painted
into it, a compact key, a footer that names the generator and the edition, and a print stylesheet
that prints the plates and dialogs in full width with outward links spelled out. The Λ₈ ladder is
one quiet line per rung and the lattice's nodes are lit by a soft highlight. **The index's cells** are drawn
inset from their frames so the gutters make the grid, with soft corners, the block tint as the fill
and the same tint one tone deeper as the edge; a spectra-only element carries its colour on the edge
instead of a dash; the record's displaced elements and the walk's are dot markers at the top right,
filled and hollow; a mouse hover rings the cell; the key folds by default (a reader's choice is
kept) as a chip at the bottom left, with the zoom controls at the bottom right, so the table and
the lattice stand clear. None of this changes a value or a
status; `tools/webindex.py` is untouched by it except for the site's subtitle.

## The data format

The site must open from a plain `file://` URL on a phone — someone handed `public/` as a folder,
with no server — and there a page may not `fetch()` a file beside itself, while a `<script src>`
is loaded without complaint. So the data ships as script files, each a JSON payload inside a
one-line wrapper:

```
data/index.js          window.__mi = window.__mi || {}; window.__mi.index = {…};
data/elements/<Z>.js   window.__mi = window.__mi || {}; (window.__mi.el = window.__mi.el || {})[<Z>] = {…};
```

`index.html` loads `data/index.js` with a static `<script>` tag before `script.js`; an element is
loaded on demand by injecting `<script src="data/elements/<Z>.js">` and reading
`window.__mi.el[Z]` in the tag's `onload`. The solver module publishes `window.MI.solvers` and
`window.MI.solverLib` from inside its own function scope; nothing else is global. The payload inside the wrapper
is exactly the object `json.dumps` would have written to a `.json` file — compact for an element,
indented for the index — and the manifest records both the `.js` file's bytes and md5 and the
payload's (`payload_bytes`, `payload_md5`), so a reader can strip the wrapper and confirm the
object. Files are UTF-8 and the page declares UTF-8; the corpus's own glyphs (ℓ, Λ₈, ℛ) travel
unescaped. `index.js` → `protocol` states the two forms and the reason.

## The status travels with the value

`index.js` carries `populate.py`'s own axis table — every axis with its status and source — and
the page looks the status up by axis rather than inventing one. The five statuses are `READ`,
`PINNED`, `DERIVED`, `RECOVERED` and `RECONSTRUCTED`, with the meanings `docs/POPULATE.md` gives
them; a value the corpus does not carry (an IUPAC element name, say) is badged as carrying no
status, and so is a value the record does not carry at all — a dash above Z = 108 takes no axis
status, because the axis table describes the value, not its absence. Nothing on the page is
computed by the page: a residual shown is the one `populate.py` wrote, and where the solvers below
do compute, they compute with the instruments' own forms and hold themselves against fixtures the
exporter measured.

Three rules keep one status per quantity across the plates, the console and the solvers:
C(Z, ℓ) is `RECOVERED` everywhere — the axis table row in `populate.AXES` now carries the status
`collapse_C`'s own docstring, `docs/POPULATE.md` and the instruments block always gave it, and
`webindex.py --selftest` holds the two together; E = admitted − held is `PINNED` wherever the
corpus's own figure is quoted (root plate, ghost plate, console, closure solver), as
`docs/POPULATE.md` pins the structural half; and a δ read from COORDINATES-2.13 is `READ` at every
grade, with the grade in the tip — a computed δ is the csv's computed column, read, not a pinned
figure. A `READ` δ is printed with the digits the csv carries (`0.09803`, not `0.0980`), and a
residual below 10⁻³ is printed in exponent form on the plates as it is in the solver, so
`6.0329e-7` never reads as `0.0000`.

Six caveats travel with the data and are shown where they bite (`index.js` → `caveats`): the
Z > 108 boundary; the B column built on the withdrawn aufbau table (register 1306); the 25 measured
rows whose B is a dispersion, not a bound; the Λ₈ mapping being one reconstruction; the equation's
validated domain; and n₀'s reading. Each is drawn from `docs/POPULATE.md`'s "Known gaps" and
"Two findings", and a cell where B disagrees between the csv and the observed configurations
shows **both** values with the disagreement marked — recorded, never repaired.

## What `index.js` carries beyond the layout

Three blocks exist so that a browser can compute without inventing:

- **`equation`** — register 1205's final form: `A`, `K`, `H`, and now `E0 = 0.8297` and
  `E1 = 0.0900` (`populate.E0`, `populate.E1`), the exponent `e(Nₑ) = E0 − E1 ln Nₑ`, and `form`,
  the two branches read out of `populate.channel_delta`'s docstring rather than retyped:
  `delta = a p^e(Ne) Ne^k ln(c+1)/c` where p > 0, `delta = h C(Z) ((Ne-1)/Ne) Ne^k ln(c+1)/c`
  where p = 0.
- **`instruments`** — the verbatim Python of nine functions, by `inspect.getsource`, each with its
  file, line, status and source sentence: `channel_delta` (`PINNED`), `collapse_C` (`RECOVERED`),
  `pauli_bound`, `core_p` (`PINNED`), `n0_of` (`RECONSTRUCTED`), `lambda_constraints`,
  `caps_needed`, `within_caps` (`PINNED`) and `cypher.op_order` — ℛ, `PINNED`. A solver in the
  browser mirrors one of these; the page shows the Python beside the result so the two can be
  diffed by eye.
- **`fixtures`** — numbers the browser-side selftests must reproduce, every one computed at build
  with `populate.py`'s own functions and none typed in: `equation_report`, what
  `populate.equation_report` computes over the measured rows (358 channels, rms 0.1809, R² 0.9656,
  median |error| 0.0587, and the per-ℓ breakdown — the exporter's selftest holds this against the
  instrument's own printed line); `closure`, ℛ over the periodic layout (90 held, 126 admitted,
  E = 36) and over Janet's — where two figures are kept apart on purpose: the **elements' own**
  distinct Janet cells give **19 held, 19 admitted, E = 0 over a box of 32**, and `cypher.py`'s own
  Janet fixture (n = 1 to 7, ℓ < min(n, 4)) gives the 22 cells over a box of 40 with E = 0 that its
  selftest records; the two are not the same index and neither is quoted as the other;
  `collapse_table`, C(Z, ℓ) for ℓ = 1..3 at Z₀ − 4 … Z₀ + 4; `hydrogenic_zero`,
  `channel_delta(1, 1, 0) == 0.0` (register 5193); `pauli`, B at He I ns = 1 and Be I ns = 2, the
  pair `populate.selftest` asserts; and `coefficient_roundtrip_sample`, the first twelve measured
  rows of COORDINATES-2.13 in (Z, charge, ℓ, mult) order — He I ns first, since hydrogen has no
  measured row — each with δ, p, Nₑ, C and δ by equation and a status per column.

## The solvers

Twelve modes sit beside the index, each a browser-side mirror of one instrument and each carrying that
instrument's headline status and its own selftest against the fixtures above: the **channel
equation** (register 1205, `PINNED`), δ for a channel from (Z, charge, ℓ) with its two branches
shown; the **Pauli bound** (register 1141, `PINNED`, with n₀'s reading `RECONSTRUCTED`),
B = min(p, n₀ − ℓ − 1) from the observed core; the **collapse ramp** (`RECOVERED`), C(Z, ℓ) across
the Janet boundary; **closure by ℛ** (§32.4.1, `PINNED`), `op_order` over a set of cells, with the
periodic and Janet figures as its fixtures; **Λ₈ constraints** (§7.1 and §7.4, `PINNED` on a
`RECONSTRUCTED` cell), the seven rules and the caps a cell needs; and the **coefficient
calculator**, which runs the equation backwards — for one coefficient at a measured channel,
solving the branch's form for that coefficient with the others held at their pinned values, or for
an atom's whole coefficient set jointly by least squares over its measured channels — and reports
the gap between what it solved and the pinned values, never replacing them. A solved coefficient
is a measurement of one atom against the equation and carries a status the page states; the pinned
figures stay register 1205's. Every row that carries a number carries a status, and a mode that
cannot reproduce its fixtures says so rather than printing a result. The joint solve goes through
the modified Gram–Schmidt basis (x = R⁻¹Qᵀy), not the normal equations; the closed forms `A only`
and `H only` are linear in δ and keep a δ ≤ 0 row, noting a solved value that leaves the pinned
sign; and the selftests are never vacuous — Λ₈ loads Fe when nothing is loaded and asserts steps
were checked, Fe's four-row `all` solve is asserted as the interpolation it is (rank 4, dof 0) and
an overdetermined element is held on the log-form residual it minimises, and the Pauli mode's
typed-p case asserts n₀ read from the record keeps `RECONSTRUCTED`. The assistant's run button is
labelled by what answers — `Query` for the console alone, `Query console + Claude` only once the
artifact runtime has granted the second answerer.

**The eleventh mode, relative gravity** (`MODE_GRAVITY`), is the gravity instrument's member
arithmetic over `data/nuclides.js`: a body written as a formula with its isotopes and charge
(`^56Fe2+`, `U-238`, `D2O`, `^1H2^16O`) or as a particle of the indexes by name; its mass from
the table (A·u + mass excess − q·mₑ + the level's energy, electron binding neglected and
bounded), Schwarzschild radius, χ = J ħ c / (G M²) and Q̃ = q e / (M √(4π ε₀ G)) with their
decades and ranks in the index's alphabet, χ² + Q̃² against 1, F by the parity of A + Ne, F = 0
by the pairing rule where it applies, the horizon-bound class at every dimension from the exact
solutions, the body's cell in the index where it is a charted member, and every quantity as a
ratio against a reference body (the field at equal distance scales as M). The angular momentum is
the banked lowest level of a single species (READ), typed (no status) or refused — a molecule's is
never inferred — and a mass with no isotope is refused, because no atomic-weight table is held.
Its selftest recomputes the index's own figures from the rows: the member count, the decade
alphabets, the forced and vanishing counts, the 914 cells and the cells per dimension, the 684
relieved, the 294 Schwarzschild nuclides, the two bounds, a sample of members against their
exported χ, Q̃ and cells, and the mass of ¹H₂¹⁶O against the generator's own arithmetic.

**The twelfth mode, the builder** (`MODE_BUILDER`), reads an atom, ion or molecule with the same
reader into its atoms, electrons, protons and nucleons, its exact mass where every isotope is
given, each atom's record (the neutral ground configuration and level, the channels and ions the
index holds, the banked lowest level of the species where one is held) as chips into the explorer,
the Λ₈ cell of a single ion from its element's ladder (RECONSTRUCTED), and the same gravitational
quantities, with a button into the gravity mode. **It draws no bond and defines none**: the finding
on the site is that a bond cannot be indexed, and the row that would carry a bond order carries
that refusal instead. Everything not derivable from what is held is refused by name.

## The relativistic limit and the bounds facet

Two facets put the solution range and its limit on the same node, in the author's framing —
quantum mechanics as the range, relativity as the limit on it, observation at the base — and
both are grounded the only honest way the corpus allows.

**The relativistic limit (the seventh solver mode) computes nothing of the record's.** `THE-LOWDIN-SOLUTION-2.md`
derives the table in the scalar-relativistic (Koelling–Harmon) Hartree–Fock reduction with one
admitted constant, c = 137, and reports that the same construction at c → ∞ misplaces eleven
elements — Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf — and inverts the channel competition at
thorium. The construction itself is **not held**: `LW1-README.md` records the delivery's objects
1, 2, 4–8 and 10 as pending bank and object 11 as not held, because session 104 was never
sealed, and `r2-scf.out` grades every figure of that family UNREPRODUCIBLE with a stated budget,
record-carried and never withdrawn. So `webindex.py` **reads** the eleven from the paper's own
sentence, cross-checks them against register 1706 and the SCF audit's table of configurations and
entrant channels (the selftest asserts all three agree, in order), copies Figure 5 from
`extracted/` with the md5 `extracted/LEDGER.tsv` records, and exports the block as `READ`. The page
marks the eleven on the table, the element plate shows the result with the figure, the console
answers `relativistic`, and the mode's `recompute` operation refuses with the reason rather than
printing a table no instrument produced. `instruments.lowdin_construction` carries the passages,
not Python, and the "Instrument source" toggle shows them as such.

**The request and its answer.** The site asked the Löwdin project for items 5, 2, 1, 11 and 12 of
the standing REQUEST-LOWDIN and for one new object, a single-Z walk switchable between c = 137.035999
and c → ∞. The reply of 2026-09-18 (`drive/The Method Materials/LOWDIN-DELIVERY-1/LW1-ADDENDUM-REPLY.md`, 4,276 B, md5
`8df39014bb91387d79f358c63982a930`, the md5 the delivery's reissued `MANIFEST.tsv` records for it; both
files were fetched byte-exact through the connector and seated with `drive_sync.py --adopt`, so their
rows read `ok-adopted`, and the reissued manifest sits under its id-suffixed name beside the 2026-09-01
one until a full sync pass applies the newest-keeps-the-plain-name rule) measures rather than assumes: the one code store in that session
holds the thirteen corridor-line instruments and not one takes c; the c → ∞ path exists only inside
`LOWDIN-HANDOFF-103.tgz`; no `--c` switch was ever written. The project commits, on bank receipt, to a
thin wrapper over the sealed solver with goldens at Ag, Hg and Th at both settings. Its one remark is
taken up here: Th is not among the eleven but a collapse-criterion row (register 1703), which makes it
the **null-difference control** — a broken c switch that displaced everything would pass a
displacement-only test — so the seventh mode's selftest now asserts both directions, displacement at
Hg and identity at Th. The bank did not arrive, the Löwdin project has concluded, and the author's
ruling was that anything still needed is this repository's to build.

**The walk, recovered.** The record's own instrument is now held: `tools/lowdin_recover.py` reads
it out of the Löwdin project's hundred conversations into `lowdin/rt` (28 files, 23 RECOVERED, 3
RECOVERED-REPLAYED, 1 RECOVERED-PARTIAL, 1 STORE; 154 of 157 printed windows reproduced; `cinf.py`
and `rt/t7b_hf.py` at the sessions' own sealed digests — `docs/LOWDIN-RECOVERED.md`), and run here it
returns four tables in `lowdin/chain/` that `record_walk_block` carries into `index.js` as
`relativistic.record`, with each element's rows under every setting in its own file: the chain at
c = 137.035999 to Z = 120 (**Λ_chain re-derived**: every sealed step the sessions printed reproduces
to the decimal except the margins of rows below Z = 57 that the record's own F61.1 identifies as
pre-guard, and the record's scorer `nlcfg.py` passes its own gate over it, 73 of 107 configurations
and 96 of 107 steps); the table the paper compared against, re-derived as sealed (restart rows from
the observed configuration at c = 137.035999 — the record's F59.3 found its driver's c never reached
the field); restart rows at a genuine c → ∞ by the record's own remedy `cinf2.py` (the record ran 13
of them, the other 94 are run here); and the chain at a genuine c → ∞, which the paper describes and
the record never ran. The paper's eleven reproduce exactly from the first two (Mn, Zn, Ag, Cd, Nd,
Pm, Sm, Lu, Hg, Lr, Rf), and at eight of them the comparison table's entrant is the observed one; at
a genuine c → ∞ the chain moves at **Th, Rf and Ubn** only, and the restart rows at Nd, Pm, Sm, Th and Lr;
thorium takes 6d at c = 137.035999 and 5f at c → ∞ in both modes. Every value is **RECOVERED** —
computed here by the record's instrument — and never READ; the element plate gains *The walk,
recovered* above the reconstruction, the relativistic-limit mode prints the recovered summary first,
the tables are downloads (`data/lowdin/`), and two caveats say what changed: the construction is no
longer "not held", and the eleven carry the finding above (`record-eleven`) in the site's own words.
The reconstruction below stays as the site's second measurement.

**The walk, reconstructed.** `tools/lowdin_walk.py` runs the record's own algorithm — the V^{N−1}
chain of §II.2 with the Koelling–Harmon equation and one constant — in two fields it can build here:
the record's own average-of-configuration Hartree–Fock field with non-local exchange, and a
local-exchange (Hartree–Fock–Slater) field beside it, at both c = 137.035999 and c → ∞, into
`LOWDIN-WALK.tsv` (476 rows, 119 per field and setting; every local-exchange row converged, and three
Hartree–Fock rows at c = 137.035999 — Ts, Og, Ubn — carry `converged = no` with their residuals in
`note`, at margins four orders above them). `webindex.py` reads that table into `index.js` as
`relativistic.walk` — its md5, the instrument's own summary as data, one entrant per Z per field and
setting, the Hartree–Fock field primary — and puts each element's four rows, candidate spectra
included, into its element file; the ten functions of the instrument travel in `instruments` as
`walk_*`. **Every value is RECONSTRUCTED and the record's Λ_chain and Λ_cinf stay READ and unheld**;
the caveat `walk-reconstructed` travels with the block. What it measured, in the record's field: at
c = 137.035999 the entrant equals the observed gain at 94 of 107 rows, clause 1 holds without
exception, clause 2 has the record's La and Ac exceptions and Th takes 6d as the record has it, and
the g channels sit at −1/(2n²) to 2.5 × 10⁻⁶; at c → ∞ 96 of 107; the entrants differ between the
settings at 5 elements (Ce, Hf, Th, Rf, Ubn), of which 1 — Rf — is the record's eleven, and at Th
the entrant is 6d at c = 137.035999 and 5f at c → ∞, the record's inversion without the record's
path clause. In the local field: 96 and 92 of 107, 7 displaced of which Lu and Lr are the eleven,
and Th 5f at both settings. The page draws the Hartree–Fock reconstruction's displaced elements with
a hollow corner mark apart from the record's filled one, the element plate carries "The walk,
reconstructed" beside "Relativistic limit" with both fields (Z = 2 to 120, so the twelve unpopulated
elements carry it too), the console answers `walk <El>` and appends the reconstruction to
`relativistic`, the "Instrument source" toggle shows the ten functions after the record's passages,
and the mode gains `walk` (this element, both fields, both settings) and `compare` (the
reconstruction against the record) while `recompute` still refuses the record's table and names the
reconstruction beside it. The mode's selftest checks the block is carried, that the element files
and `index.js` agree at Ag, that Th's entrants stand as the summary states in each field, that
Z = 120 carries rows, and that `compare` prints no row without a status. See `docs/LOWDIN-WALK.md`
for the instrument, its fixtures and the full comparison.

**The bounds facet** reads the `bound` column of COORDINATES-2.13 — 22 distinct notes over the
104,832 cells — and classifies each into one of eight kinds by a regex rule that travels in
`index.js` → `limits.rules`, applied identically by the exporter and the page: a series limit
printed for the channel, a series unresolved above the stated n, a nuclear limit (no long-lived or
primordial isotope, no nuclide synthesised), no single 2S+1 keying the channel, an open-shell core,
no analysis located (which the note itself says is not a bound on existence), δ = 0 by symmetry,
and no note. The note is `READ`, the kind `DERIVED`, and the rule is shown on the cell plate
beside them; a printed series limit is shown as printed, with no unit added. The legend's
"Cells by" control colours cells by grade or by limit kind, each element plate counts its cells
by kind, and the console answers `limits <El>`. The exporter's selftest asserts every note is
classified and every count sums to the rows.

## The particle indexes

**The particles that are not periodic atoms come from the other session's tree.** Under
`research/warp-drive/` (the warp-drive branch, merged to `main` as PR #34 on 2026-09-19) DOCKET 27
seats three indexes over the PDG 2026 table — `fundamental.py` (the 30 Standard Model particles on
2J, Q3, colour dimension, generation), `mesons.py` (250 mesons on 2J, P, 2I, Q3; 8 set aside for
want of a printed parity) and `baryons.py` (292 baryons on 2J, P, 2I, Q3, S, C, B; 14 set aside) —
read from `captures/PDG-2026.tsv`, which `pdgcapture.py` wrote once from the scikit-hep `particle`
package with the md5 of what it read, and `docket27.py` accounts for the whole table:
6,506 = 5,880 composite nuclei (the periodic elements, this site's subject) + 54 PDG status-4
(the fourth generation and the diquarks, on PDG's own flag) + 572 kept, every one a member of one
of the three; 550 land on a cell and the 22 that do not are named. DOCKET 28, `quasiparticle.py`,
is the one gap closed with two measured refusals — there is no particle table for quasiparticles
because the labels are the host crystal's (230 space groups, 32 point groups, 73 arithmetic classes,
from `sgcapture.py`), and the one exactly specified family, the anyons of SU(2)_k, charts to a
channel that never moves with the box and is refused as a theorem — and is carried marked *in
progress*, because the other session is still working on it. DOCKET 29, `particlesweep.py`,
reopens the census over the three new member sets — every sub-chart of their declared columns,
142 charts (11 + 11 + 120) — and finds one seating and two refusals: `baryons (2I, Q3)`, isospin
against charge with flavour dropped, 16 cells at cell (5, 7, 4), **the tree's only K5**, on all four
of the overlap ruling's grounds and at every mass cut; refused, `baryons (P, 2I, Q3)` at K1 because
K1 is held, and `fundamental (Q3, GEN)` at K4 because at arity 2 the statistics language closes
every chart for free (105 of 105 at the time, 106 of 106 once the band index, itself arity 2, was seated) and what it shows is join-closure. Seven of the eight channels were
occupied then; the spin-4 index later took the eighth. `docket27.py` also counts antimatter rather than implying it — 231 of the 550 charted
members, 42 % — and resolves the photon, the muon and the antimuon by name with their cells.
DOCKET 30, `fqh.py`, re-examines DOCKET 28 and finds it refused the wrong object: the anyon chart
was a union over theories (SU(2)_k for every k), not a reach over data. Rebuilt as a reach — the
quasiparticles of the Laughlin states at filling 1/m, indexed by a measured filling fraction — the
channel moves with the box (K2 then K0) and the box-invariance test returns SEAT: **168
quasiparticles of twelve states, 30 cells, cell (0, 15, 4)**, three states observed (1/3, 1/5,
1/7), the e/3 charge measured by shot noise in 1997, and not one member a fermion, which is forced.
Both verdicts stay on the record; the non-abelian states are named as not here. The site carries
the seated index with every member (m, j, Q, θ/π as exact fractions, the four coordinates with
their statuses), a figure of j against the filling, the sweep and its verdict, and the earlier
refusal after it; the quasiparticle work is still in progress on the other session. DOCKET 31,
`bosonqp.py`, seats the composite bosonic excitations of a solid — Cooper pair, exciton and
biexciton composed from the electron and the hole, six collective modes from the symmetry each
breaks, two hybrids — with every number computed by three stated rules and none written down
(15 members, 5 cells, K7, the trion excluding itself as a fermion), as a sublattice beside the
tree's own bosons: not a subset, one cell outside, the union still a sublattice. DOCKET 32,
`readrezayi.py`, seats the non-abelian Hall quasiparticles, the Z_k parafermion primaries of the
Read–Rezayi series with Moore–Read as k = 2: 363 members over eleven levels, 78 cells, K0, the
weights validated against the Ising category at k = 2 and the Fibonacci τ at k = 3, six fermions
where the abelian index has none, and neither Hall index nesting in the other. The site carries
both as their instruments report them, every value DERIVED from the stated rules or closed form,
the plateaux READ.

**Two things the page does for a browser it has never met.** If drawing ever throws, the error
is written on the canvas with the line that threw, so a blank canvas can be reported rather than
described; and if the `index.js` a browser cached is older than the page (no `lattice` block), the
page fetches a fresh one past the cache and boots again, while element, papers and particle files
are requested with the edition as a query string so they match the index. Dialogs size to the
visible viewport (`dvh`) and scroll inside a flex column, and every figure image opens at full
size on a tap.

**`webindex.py` imports those instruments by path and retypes nothing.** `particle_index_block`
puts the warp tree's directory on `sys.path` (its modules import each other by bare name and reach
`tools/cypher.py` two levels up), calls `rows()`, `index()`, `cell()`, `closers()`, the refusal
measurements and `docket27.census()`, and writes `data/particles.js` (loaded on demand) with every
member's coordinates, each coordinate carrying a status — READ where the capture prints it, PINNED
for the colour assignment the Standard Model's definition fixes, DERIVED for generation from the
PDG id and for the flavour numbers read off the quark content by the pinned case convention —
beside the mass and width (READ), the cells, the closure channel, the collisions, the conjugation
measurement (antimatter, measured rather than seated), and every refused coordinate with the
measurement that refuses it. The block also carries the antimatter count, the three named particles, and the
whole of the sweep: the census, the occupancy before and after, the hits, the seating with its
grounds, reach sweep, cells and corners, the two refusals, and the arity-2 freeness table. The
sweep's occupancy is measured over the whole registry, so the instruments need the warp tree's own
`tools/populate.py` beside them (its Madelung list runs further than the earlier one; the merge
brought it to `main`); a build takes about two minutes with it, and the block is computed once per
process. `index.particle_index` carries the summary; the Particles dialog draws
each index by charge and spin, lists every member with its badges, and appends the muon material
after it where a `--with-particles` build carries that block. The public-build guard runs over
`particles.js` as it does over the index. The tree is located by `--warp-root` (default
`research/warp-drive`, now in the repository, so a plain build carries the indexes and records the
repository's own commit); when it is absent the site carries no particle indexes and says so, and
the selftest checks that too. The channel closures take about thirty seconds per build.

**Incorporating the next index the other session seats** is the same contract: an instrument in
the tree with `rows()`, `index()` and `cell()`, coordinates declared before the chart is run, a
`SOURCE` beside the code, and a status for every value. Add its coordinates to `PARTICLE_COORDS`,
its block to `particle_index_block`, and its figures to the selftest — and, for the explorer, a
row in `PAXES` naming which of its coordinates go on the axes, or it draws the first three.

### The spin-4 mesons and the member sub-population sweep

Two more of the other session's instruments are read at build when the tree carries them.
**`spin4.py`** seats **the spin-4 mesons** as a fourth index: the ten mesons of the table with
2J = 8, a sub-population of the meson index with the spin held constant (so it carries no
information and is not a coordinate; the effective arity is 3), charted on (P, 2I, Q3) — 10
members on 9 cells, cell (4, 5, 3), closed by information and statistics, **K4**, the tree's only
K4 and the last of the eight closure channels to be occupied. It is seated on the table's own
**status** flag as its reach, which is total where mass is not (two members, K(4)(2500)±, have no
printed mass and are charted anyway): the channel moves with the reach — K5 on the established
states alone, K4 once the status-2 states are admitted — so the box-invariance test seats it, and
**both readings are carried** (`reach.established`), the K4 always quoted with its condition. The
overlap rule's reach gate would read the same movement as a late arrival; the block records that
the two tests disagree rather than choosing. `_spin4` writes it in the shape of the other three
indexes plus `parent`, `held_constant`, `massless`, `reach`, `arity`, `tests` and `channels`, so
the Particles dialog and the explorer carry it with no special case beyond a `PAXES` row (charge
across, isospin up, parity into the page, coloured by the PDG status) and a plate section; a
member's plate links the same row in the meson index.

**`subpop.py`** is **the member sub-population sweep**: every earlier sweep varied a chart's
columns, this one varies its members — one coordinate held to one value over every index with
declared coordinates — and asks whether the sub-population is closed and which channel it reaches.
`_subpop` carries its census (143 closed sets when it first ran, 203 once the nuclear band index was
seated, since the sweep is over the seated indexes and a new index extends it by construction; 2
reaching a channel no index occupied either way, both at K4:
one at effective arity 2 where statistics is free, and the spin-4 mesons at arity 3), the spin-4
population under the parent's mass reach (K5 at every cut, never K4 — the refusal the seating
answered on a different reach; both statements stand), which indexes are lattices at all (three of
twenty-three, nineteen not and one too large to test; for the rest the sweep tests closure in the
ambient box, and the block says so), the recursion
determination (within the family, chain 2 over 14 containments; the three lattices peeled one
element at a time with every intermediate re-checked, two exact and one a verified lower bound;
exhaustively over every subset of the five indexes small enough, chains 5, 7, 6, 8 and 14, the corepresentation index the fifth at 27dd39c), the
indexes too large to determine, named, and the candidates run and not seated — the chiral
Goldstones (a full box, so free), the electroweak eaten Goldstones (a relabelling), and the
nuclear rotational bands, whose five routes are listed with their states and whose two sources,
reached by a join over a paper database after four meets failed, are linked by arXiv identifier
and distinguished (one the candidate, one a different object). Occupancy in the census is measured
as it stood before the sweep's own finding was seated, or the finding would erase itself; the
block carries that note. The sweep costs a few minutes at build and is memoised with the rest.

**The nuclear band index, the deformed-paper capture and the bond question** followed on the
same branch and are read the same way (`_nuclear`, `_bonds`). `nucbands.py` seats the nuclear
excited states of the magnetic and antimagnetic rotational bands, the candidate the sub-population
sweep first declared unreachable and then reached by a join: `nbcapture.py` parses the published
data table (arXiv:2303.13849) seated in the tree, reproduces the paper's own census exactly (252
MR bands in 123 nuclei, 38 AMR in 27) and its selection rule (213 of 213 AMR steps at ΔI = 2),
and records the source's one fault as printed, the parser's own fault found by audit and fixed,
and the anomaly run down and found not a fault. The index is 2,152 members of 2,245 captured
levels on (2I, parity), 121 cells, cell (2, 63, 2), K2 — and the plate says the K2 is the free
one, since statistics is vacuous at arity 2, and tables every superset of the two coordinates,
all seven K0. Three refusals are counted apart (27 bands with no spin-parity column, 93 levels
with no parity, 6 level rows with none inside a band that has them, each closing its gamma
arithmetic), the bands themselves are a 67-cell sub-population measured and not seated, and the
two mechanisms are charted apart. The explorer opens it as a fifth index (`#/p/nucbands`; spin
across, parity up, coloured by mechanism, one node per level, fanned at its cell) and a member's
plate carries its nucleus, mechanism, band and energy. The second paper (arXiv:2508.05447, the
deformed rotor's tower) is carried as **captured, not seated**: the document's own delimiter is
absent from the extraction (0 of 210), an earlier refusal that concluded no parse could recover
the entries is recorded as retracted, a sequence-with-reset rule recovers 233 of 234 with the 61
bandhead states exact, and the two entries with a falling spin sequence are named rather than
split. `bonds.py` answers whether a bond can be indexed, three readings and three refusals on
three grounds, with the decidable parts re-derived (σ_v's action, the π² microstates, the
fourteen nucleon–nucleon partial waves at J ≤ 3) and the finding that outlives the question: every
closure channel is now occupied, so the overlap rule's novel-channel ground can never be
satisfied again. The Particles dialog carries both; the captures' md5s join the provenance list.

**What the indexes predict, and the ghosts in every particle lattice.** `predict.py` measures E per
seated index, the cells an index's own join-closure demands and no member occupies: 3,206 over
twenty-two indexes, sixteen predicting and six complete, the partition exact (E = 0 exactly where
the index closes under information, near definitional and said so), E reported as an upper bound
because a demanded cell is one of three things and only one is a prediction: FORBIDDEN, UNPLACED
or OPEN, the worked case being the D_s slot in the mesons, empty because the source prints no
spin-parity for a particle that exists. `ghosts.py` does the adjudication: seven laws (a
join-closure never invents a coordinate value; a monotone bound forbids nothing, so every atomic
and nuclear bound in the tree, real theorems all, forbids nothing by theorem; only an antitone,
congruential or non-monotone bound can forbid; a hidden variable free to range forbids nothing,
so the quark model forbids no meson cell; E is relative to the operator, the element table's 36
being an order deficit with a join deficit of zero on the same ninety cells; forbidding power is
the chart's), one bound that forbids, Gell-Mann–Nishijima on the baryons, re-derived from the
capture's own quark strings (292 of 292 clean, and a capture fault on the mesons found by its
isospin leg, recorded and not repaired, its consequence measured as nil), and the separation of
UNPLACED from OPEN by a rule with a strength condition: 593 forbidden, 36 unplaced, 2,479 open,
98 undecided. `_predictions` carries all of it, and for the site's own eight indexes it classifies
**every demanded cell** with the instrument's own bound and source gaps (nine seconds at build),
naming the source row that pins an UNPLACED one; the selftest asserts the cell-by-cell counts
against the instrument's recorded table and that every demanded cell sits on coordinate values
its members carry, which the projection law guarantees. The explorer draws them: **every
demanded cell of a particle index is a ghost in its lattice**, hollow, tinted by its bin
(forbidden faint and dashed, unplaced amber, open in the accent), fanned with the members at its
position, counted in the caption and the canvas key, listed by bin on the index's plate, and each
opening to a plate of its own (`#/p/mesons/ghost/2,-1,0,3`) with its coordinates read back, its
bin and what decides it, and the members that would be its cell mates (none, by definition). The
baryons' 1,012 draw beside their 278 members. The Particles dialog carries the E table, the laws,
the adjudication table, the rule, the undecided index, the bound and the fault.

**The deformed-paper capture is closed.** The missing entry was a band-number line printed with a
full stop, admitted narrowly (exactly one such line exists), and the capture is total against
three of the paper's own figures, 234 entries, 173 bands, 61 bandhead states; the remaining
falling spin sequence is one entry the paper prints as one, acquitted; on the band index's
coordinates the levels give 96 cells at K2, cell (2, 49, 2), measured and not seated, because a
capture is not an index and seating is a ruling of the other session. The block carries the
closure with its numbers, and the pin reads "234 of 234 entries, total, not seated".

That join-over-meet correction is also the retrieval law the released three-body paper's closure
measurement gives, and the Ask prompt now carries it as clause (g) of the retrieval method: a
failed narrow search is a meet, and its retry is a join over a larger index, never the same meet
again.

None of these instruments is on `main` yet: a plain build from the repository tree carries three
indexes and no sweep, and the fixtures and pins are conditional on their presence; the shipped
data was built with `--warp-root` on the warp branch at d264df1.

### Each particle index as an index of the explorer

Every particle index the build carries is also a first-class index of the explorer, beside the
elements, and not only a table in the Particles dialog. `script.js` reads `particles.js` into
descriptors (`particleIndexes()`): the three PDG indexes and, as they land, the Hall
quasiparticles (`fqh`), the bosonic excitations (`bosonqp`) and the Read–Rezayi primaries
(`readrezayi`), each with its rows as `{name, key, coords, extra}`, the key unique within the
index (a duplicated name in the bosonic index, the Cooper pair at two spins, is keyed by its 2J).
An index opens as a lattice (`buildParticleScene`): three of its declared coordinates on the axes
and a fourth as colour (a coordinate, or as `extra:<field>` a field the row carries beside them,
such as the PDG status), by the `PAXES` table — charge across, spin up, generation or isospin into
the page for the PDG indexes; the inverse filling or the level across and the two orders on the
other axes for the Hall indexes — with **one node per charted member at the rank of its values**,
so a charge of −1, 0, +1 and a spin of 0, ½, 1, 3/2 draw at even spacing. A drawn position can
hold several cells where the index has more coordinates than the drawing (the baryons' seven), and
the members sharing one are fanned out in a small grid inside it, smaller the more there are; the
caption counts the drawn positions and the shared ones. **Which coordinate goes on which axis is a
choice of this page**, badged DERIVED on the plate with the coordinate table saying what is drawn
where; every value, the cell count and the closure channel are the instrument's, and the scene
computes nothing. The axes tick in the coordinate's own units (Q, J, I read back from Q3, 2J, 2I),
and a colour key sits in the canvas's corner. A member's name is drawn under its node once the
reader has zoomed past 1.6× and always under the selected one.

The nodes are `{kind: 'pindex', id}` (parent: the root) and `{kind: 'particle', id, i, row}`
(parent: its index), so the crumbs, `Esc`, the `↑ up` button and the hash all work as they do for
an element: an index is `#/p/mesons`, a member `#/p/mesons/pi0` (the key URI-encoded, so
`#/p/mesons/J%2Fpsi(1S)`), resolved by `goToParticle` after `ensureParticleIndex()`. A member's
plate carries its coordinates each with the coordinate's status and read back in its units, its
cell (the full tuple) with the cell's other members as chips, what the table prints of it — the
PDG id, whether it is an antiparticle (DERIVED: a negative id), family, quark content, mass and
width (READ), C and G where printed, the table's own antiparticle-naming flag and status flags —
or for a Hall quasiparticle its state, j, charge and exchange phase, for a primary its level,
(l, m), weight and quasihole charge, for a bosonic excitation how it is made; then the previous
and next member and the usual Copy JSON, Copy link and Raw record. The index's plate carries the
member definition, the counts, the coordinate table with statuses and the drawn axis, the members
set aside by name, the refused coordinates with their measurements, the source, and every member
as a chip. `citation()` cites a particle node to the capture and the instruments, not to the
element sources.

The particle indexes load when the page is idle after boot (`ensureParticleIndex`, ~218 KB), and
then the **index picker** at the top left (`#index-pick`, hidden when the build carries no
particle indexes) lists the elements and each index, search suggests members by name and indexes
by title (`pi0`, `lambda`, `mesons`, an exact particle name outranking an element whose symbol
starts the same way), and the Particles dialog's headings carry *Open as an index*. Choosing a
layout button while a particle index is open returns to the elements. A smoke test opens every
index and a member of each by hash, taps a node, follows a chip, climbs with `Esc`, searches,
uses the picker and the dialog's button, and drags to rotate, on desktop and phone viewports.

### The register, the deformed levels seated, and the gravity index

The toolbar button that opens this dialog is labelled **Indexes** (it was *Particles* while the
dialog held the particle indexes alone); the dialog's element id and the build's block names are
unchanged.

**The register** (`_register`) is asked of the research tree's registry at build: every seated
first-order index — **27** at the build this page describes, on **all eight** closure channels —
with its label, what a member is, the quantum numbers charted, the cells and the admissible cell
(channel, height, width) measured over the live members (about 35 s, the gravity index's 914 cells
the slowest), the languages that close it by the channel law, whether the overlap rule seated it as
a coarsening, and the sources it reads with their hashes (a path into the store is withheld and
its kind named instead). Beside them the tree's own `STATE.json`, which its instruments regenerate
and which may lag the registry by a row or two (it held 24 rows when the registry held 27), supplies
the channel map, the tree's retractions of its earlier claims (`retractions`, its instrument section
marks written out as "part n" because they are not the books'), what is not claimed, and its commit;
the block records which it read live. The Indexes dialog opens with it as a table, each row the site carries in
full with an *open →* button. The register's completeness flag is false and is shown false.

**The deformed two-quasiparticle band levels are seated** (`_deformed_index`, from the
`deformedbands` instrument over the closed `deformed` capture): **1,907** levels carrying both
spin and parity, on the band index's own two coordinates, **96 cells at K2, cell (2, 49, 2)**, the
K2 said to be the free one; **56** levels with a spin and no parity refused apart and named on the
ghost plates they pin; the band number (234 distinct over 234, a row label), the energy (a
magnitude against an unknown offset) and the host's Z and N (charted anyway: 853 cells at K0, and
still refused) each refused against a number; and the seating's ground measured — the cell held by
nobody else, **zero nuclides shared** with the band index (23 here, 123 there) although the band
index's mass range 58–205 contains this one's 156–174 entirely, so the earlier "disjoint ranges"
ground is replaced by the weaker true one; the source's title overclaims (132 levels above A =
168, up to 174). The site walks the capture itself in the instrument's order and asserts its count
equals the instrument's. It is the sixth index of the explorer (`deformedbands`, spin across,
parity up, coloured by nuclide) and the capture block's verdict reads `CAPTURED IN FULL, SEATED`.

**The gravity index** (`_gravity`, from the `gravity` instrument with `overlaprule`, `ghosts`,
`mi` and `hlaw`): a nuclide in a charge state, read at the lowest level its NIST ASD level table
banks with a readable J, in a spacetime dimension 4 to 11 — `(Z, N, A, q, Ne, 2Je, L, D)`, every
slot a quantum number, a count of them, or the status of the level the rest were read at. The
build reads every number: **3,558** nuclides of AME2020 Table I (carbon 12 reconstructing to
exactly 12 u from the table's own zero, a fixture), **126** species (93 at the table's ground
level, 33 at an excited level, members with L = 1 rather than exclusions), **3,663** members,
**29,304** charted rows on **914** cells in a box of 3,840, **K0, cell (0, 19, 112)**; the two
angular-momentum facts (F forced non-zero on 1,831 members by the parity of A + Ne, established
zero on 423 by the pairing rule carried as `EMPIRICAL-RULE`, 1,409 neither; 294 neutral nuclides
exactly Schwarzschild); the horizon-bound table of exact solutions (Kerr–Newman at D = 4,
Tangherlini and singly-rotating Myers–Perry above, no bound on rotation from D = 6, charge bound in
every dimension, no exact charged rotating solution above four so `B = 2`); the two findings (the
dimension invisible to the chart and visible in the cell count, 109 cells at D = 4 and 115 from
D = 5 at the same cell; **684** members relieved of their bound at D = 6 with the cell unmoved);
the coarsening (B, F, X) the overlap rule seated at **K1, 26 cells**, with its channel by the
dimensions admitted (K7 at D ≤ 5, K1 from D ≤ 6) and per single dimension (K7, K1, then K0);
the **image bound** that empties most of its demand (E = **1,550**: 1,080 forbidden because the
coordinate map's image, exhausted over every nuclide, stage and 2Je to saturation at 1,416 cells,
does not reach them; 470 open; 0 unplaced, the index being gapless), the withdrawn pair of bounds
it replaced (1,228 forbidden, 148 of them reachable, Zr-113 at q = 1 among them); the encoding
sensitivity; the instrument's refusals in the site's words; and **the instrument's own selftest,
run at build and recorded as it ran** — it pins the figures from before its reader was widened
(118 species, 3,394 members) and this tree measures 126 and 3,663, twelve fixtures disagreeing,
every one named with both figures, recorded and not repaired on either side. In the explorer it is
the seventh index (`gravity`): every member drawn once at D = 4 on its spin-decade rank, its
charge-decade rank and F, coloured by the bound class, with the bound class at every dimension,
the mass, χ, Q̃, the level read and a button into the gravity mode on the member's plate; of its
1,550 demanded cells the ones at D = 4 are drawn as ghosts and all are counted.

**The gravity instrument's selftest was re-pinned by the research branch itself.** It pinned the
figures from before its own reader was widened (118 species, 3,394 members) while the tree measured
126 and 3,663; this branch carried a repair for one commit, and the research branch then re-pinned
the instrument at its own head (sections 3a and 3b of the file name the eight species the widened
reader reached and the nine not read at their lowest level), so the copy here is withdrawn in favour
of theirs and the site records the selftest as it ran: it passes.

**A nuclear-spin table, measured and not seated** (`_nuclear_spin`, from the `nspin` instrument's
index half): the gravity index refuses to call the electronic angular momentum the member's spin
because the nuclear part is not banked, and a ground-state nuclear-spin table is exactly that
datum. The instrument sweeps the coordinate map under a model of it (parity fixed by A) and finds
the image shrinks from 1,416 to 1,088 cells with nothing gained, so seating the table could only
forbid — 1,208 of the 1,550 demanded cells against 1,080 now, 128 moved from open — and 755 of the
1,178 members reading no electronic spin would leave the zero decade; the 168 seated cells outside
the new image all read that zero decade, the signature of a re-chart and not a refutation. Carried
on the gravity index's plate and in the dialog with its two refusals; the instrument's other half,
a propulsion estimate, is not carried, being the field's question.

**The phonon index** (`_phonons`, from the `phonondex` instrument, registry row 25): a member is a
site-symmetry type of a space group up to conjugacy — the Γ-point phonon symmetry content every
atom on such a site contributes, from which any material's content follows by addition over its
occupied sites — **1,120** members over all **230** space groups on **90** cells, **K0, cell
(0, 12, 16)**, every number computed (the operations from spglib in the primitive basis, the
character tables by Burnside's class-algebra method, the decomposition by orthogonality) and none
read from a table; **115** distinct decompositions; the guards (modes exactly three times the
multiplicity, orbit-stabiliser on every row); the coarsening the over-representation rule forces
(the triclinic centrosymmetric group's eight inversion centres are one member); six known crystals
composed and matched six for six; the four defects the arithmetic caught; multiplicity and
point-group order refused as the host's; the k ≠ Γ refusal recorded as discharged by the index
beside it. The eighth index of the explorer (`phonons`: site order across, distinct species up,
maximum degeneracy into the page, coloured by crystal system).

**The k-point index** (`_kpoints`, from the `kpointdex` instrument, registry row 26): a member is
an isolated high-symmetry k-star of a space group, the reciprocal-space analogue of a site type —
**870** members over the **162** space groups that have any (the **68** without are exactly the
ten polar crystal classes, measured) on **21** cells, **K0, cell (0, 7, 5)**; the points enumerated
exactly by Hermite normal form and the 1/12 and 1/24 grids agreeing with the enumeration on all 14
Bravais lattices because every coordinate's denominator is 1, 2, 3 or 4; the small representations
computed through the little group's projective factor system, **305** members (35.1 %) carrying a
non-trivial one with their bands stuck together; a published table (Setyawan and Curtarolo 2010)
used only to check, 12 of 14 named points found and the two misses one star on a symmetry line; a
second implementation agreeing on 314 of 314 dimension buckets with the multiplier's order differing
in four space groups as a gauge choice, its eighteen once-unresolved members closed; the star and
point-group order refused as the host's, a merge by symmetry content refused (485 members it would
lose) and two over-representations refused with their counts. The ninth index of the explorer
(`kpoints`: little-group order across, small representations up, maximum degeneracy into the page,
coloured by Bravais lattice). Both were measured into the prediction instrument's table at 27dd39c with a bound each.

**A finding the research tree then repaired.** Its sub-chart sweep (`overlaprule.arity2_freeness`)
walks every registered module and, by its own design, raises rather than skipping when one declares
neither a coordinate entry nor coordinate names to it; at 40ad1e4 the two newest indexes declared
neither and the sweep stopped on the phonon index. The site carried that as
`arity2_freeness.absent` with the sweep's own message (`_freeness`), and keeps the path: a build
on a tree where the sweep raises records the finding on the spin-4 index's plate and in the sweep
block, and the fixtures check whichever the tree gives. At 27dd39c both instruments declare their
names and the sweep runs.

**The time-reversal extension** (`_coreps`, from the `corepdex` instrument, registry row 27): a
member is a corepresentation at an isolated high-symmetry k-star, a single degenerate level where
the k-point index's member is the star — **3,529** on the k-point index's own 870 stars (proved
identical as sets on all 230 space groups by the derivation, compared label-free here), on **13**
cells, **K0, cell (0, 6, 3)**; the degeneracy, the small-representation dimension and the number of
species fusing as coordinates, which determine Herring's case with no exception (3,138 real, 12
pseudoreal, 297 complex pairs, 82 across conjugate stars); the accounting 3,908 − 297 − 82; **309**
levels doubled at k by time reversal over 86 space groups; which obstruction touches which of the
seated stars; the over-representation an adversarial review caught (3,611 members on 37 cells at
arity 4, withdrawn: a conjugate-star level seated twice and the little-group order carried as a
coordinate) and the repair; the star's properties refused as the k-point index's. The tenth index
of the explorer (`coreps`: degeneracy across, small-representation dimension up, species fusing into
the page, coloured by case). The k-point index's third coordinate loses its gloss with it: it is the
largest small-representation dimension and not the degeneracy, which time reversal exceeds at 118
of its groups.

**The isotope index** (`_isotopes`, from **`tools/isotopes.py`**, this repository's own instrument
and not one of the research tree's — it is **not a row of the register**, the register's count of 27
does not include it, and the block and the page both say so): a member is a nuclide of AME2020
Table I, the one nuclear table the repository holds, the neutron included, on **Z and N, both READ**
— **3,558 members on 3,558 cells**, an injective chart, at **K4, cell (4, 295, 18)**, closed by
information and statistics, **E = 0**: the chart of nuclides is join-closed, so the index demands
nothing and draws no ghost. The cell is measured twice: the instrument measures height and width
exactly on two coordinates (a chain is a non-decreasing run of N over the members sorted by (Z, N),
an antichain a strictly decreasing one, both by patience sorting, both witnessed — the chain runs
from (1, 0) to (118, 177) and the antichain is the eighteen nuclides from (63, 107) to (80, 90)),
and the build measures the same chart with the hierarchy law's five closure operators (order and
algebra 3,560, geometry 3,962, information and statistics 3,558) and asserts the two agree; the
meet-closure asks for two cells, the empty nucleus (0, 0) and the diproton (2, 0), which is exactly
what the order and algebra closures add. Each member carries its mass excess with its uncertainty
and quality flag (2,550 measured, 1,008 estimated, at the status the table gives it), its mass in u
(A + Δ/(u c²), the one constant CODATA 2018's and marked EMPIRICAL), its binding energy from three of
the table's own entries (B = Z Δ(¹H) + N Δ(n) − Δ, the electrons cancelling exactly; ⁶²Ni the most
bound at 8,794.555 keV per nucleon on the rounded table's rows) and its one- and two-nucleon
separation energies where the neighbour is in the table (S_n undefined on 119, S_p on 179). Seven
candidate coordinates are refused, each against a measurement: A (a function of the two, the chart
on (Z, N, A) at the same cell), T_z (charted anyway, at height 178 and width 31, and refused as a
relabelling that separates nothing new), the mass excess (a magnitude, 3,481 distinct values on
3,558 rows), the quality flag (provenance of the value, not a property of the nuclide; charted
anyway at (295, 22)), B and B/A, the separation energies (magnitudes, and not total), and spin,
parity and half-life, which are **NOT HELD**: the repository holds no NUBASE table, and the
instrument invents none. The eleventh index of the explorer (`isotopes`: N across, Z up, coloured
by the quality flag); a member's plate opens the same nuclide in the gravity index and in the
gravity mode. `python3 tools/isotopes.py --selftest` pins the table's census, its ledger md5 and
the exact cell; `--charts` runs the three refused charts (about 25 s). See `docs/ISOTOPES.md`.

**The predictions block** at 27dd39c spans 27 indexes: **4,919** demanded, **2,045** forbidden by
five non-monotone bounds (the three-quark flavour bound, the gravity image, and one each for the
phonon chain: a mode budget antitone in the site-symmetry order forbidding 29 of 111, a sum-of-squares
rule forbidding 38 of 45, and Herring's criterion forbidding all 4 of the corepresentation index's
demand, the first index in the register to close at zero open), 36 unplaced, 2,740 open, 98
undecided; law L4 now names the non-monotone bounds from the instrument's own table.

**`data/nuclides.js`** (`nuclides_block`) carries what the two new solver modes compute over: the
3,558 nuclides with mass excess and quality flag (the file's md5 against the ledger's), the
constants with their statuses, the 126 species with the level each was read at, the bound table,
the decade alphabets and the fixtures the browser recomputes.

**The predictions block** now spans 24 indexes: **4,759** demanded cells, **1,974** forbidden by
the two non-monotone bounds (894 baryon cells by the three-quark flavour bound that replaced the
Gell-Mann–Nishijima reading, 1,080 gravity cells by the image), 36 unplaced, 2,651 open, 98
undecided; law L4 now names both bounds; nothing is too large to close, the earlier exclusion of
the gravity index having been withdrawn by the instrument.

## Ask a model, with a machine check

**The page never answers a question itself, and it never trusts the model that does.** The
console answers deterministically from the loaded data. With an API key saved in the browser
(`Ask a model` under the console; the key is kept in `localStorage` and sent only to the API
address given, `api.anthropic.com` by default or a proxy the reader names), the same *Ask* button
also sends the question to Claude with the web search tool on. The system prompt fixes the method:
search first for context and method, then apply it to the DATA lines the page hands over — every
figure of the loaded data the question names, as `path = value [STATUS]` lines built by
`contextLines` (the closure and equation figures, every channel and measured row of the elements
the question mentions, the particle rows it names) — and mark the work with three markers:
`⟦path⟧` after every figure taken from the data, `⟪function(args) = value⟫` for every calculation
the page's own library can repeat (the channel equation, the Pauli bound, the collapse ramp, the
core's p and n₀, E), and `⦃equation⦄` around every chemical equation. It is told never to claim
the page verified anything, and not to write laboratory procedures.

**It searches the way the index retrieves.** The system prompt carries the retrieval procedure the
work states for itself, in the site's own words: enumerate the target facts before searching; for
each target list the routes that could carry it by type — primary, preprint, review, compilation,
citing paper, deposit, database — and try the open ones first, since a paywall blocks a route and
not a fact and a compilation can carry a better figure than the primary; read every retrieved source
for the sources it names before searching afresh; move along the route set when a route is
blocked rather than re-attempting it; a fact on two independent routes closes, a fact on one is
fragile and marked so, and a fact not retrieved is a stated gap with the routes tried; and ask for
a source as a catalogue entry (DOI, arXiv number, archive identifier, database record), not only as
a text string. Two more markers carry the attribution: `⟨⟨url⟩⟩` after every figure taken from the
web, one per route that carried it, and a `RETRIEVAL` table at the end, one line per (target,
route) with its type, source, result and value. `checkRetrieval` parses the table, reads the route
type from the words, resolves each source to an identifier (DOI, arXiv, ark, URL), counts the open
routes per target as its redundancy ρ (two close, one is fragile, none is a stated gap), and checks
every source — inline or in the table — against the URLs the search tool actually returned in the
API response, so a source the searches never produced is flagged rather than trusted. Fixtures in
the ninth mode cover the parser, the identifiers, the redundancy verdicts and the flag.

**The machine check is the solver module's `checkAnswer`, selftested.** It resolves every cited
path back to the loaded value (`askResolve`) and compares the figure the model wrote beside it
(matches, DIFFERS with the index's value shown, not in the index); repeats every computation with
the library (`askCompute`: agrees, DIFFERS with the page's value, not computable, unknown
function); tallies every equation for conservation of every element and of charge with each
element linked to its Z (`checkEquation`: balanced, NOT balanced with the unbalanced tallies,
unreadable); and counts the numbers the model stated with no marker within reach as *unverified,
the model's own*. Marks are drawn inline beside the model's words and a summary line follows; a
mismatch is never corrected. Web sources the API reports are listed under the answer. The console
command `check <text>` runs the same checker over any pasted text, so the check can be exercised
without a key, and the ninth solver mode, *Chemical equation check*, runs the equation part on its
own with a selftest over eleven fixtures (brackets, hydrates, ionic charges in three notations,
phase labels, an unknown symbol refused, no arrow refused). **The tenth mode balances.** `balanceEquation` is the algebraic method made exact: conservation
of every element and of charge as a homogeneous linear system over the species given, its
nullspace computed over the rationals in BigInt fractions, the one-dimensional case scaled to the
smallest whole numbers. Redox in water is a choice of medium — acidic adds H⁺ and H₂O, basic adds
OH⁻ and H₂O — and a half-reaction allows e⁻; an added species is used only where the arithmetic
needs it, lands on whichever side its sign puts it, and the electrons transferred are reported.
The mode refuses rather than guesses: species that admit no balance are said to, species that admit
more than one reaction get the basis and not a choice, and a given species whose coefficient comes
out negative is reported as belonging on the other side, not moved. Every result is tallied by
`checkEquation` before it is shown, so the balancer is checked by an instrument that is not itself.
Charges are read in any usual notation (`Fe3+`, `Fe^3+`, `Fe{3+}`, `Fe(3+)`, `Fe+3`, `Fe³⁺`,
`Fe(III)`; `MnO4-`, `SO4^2-`, `SO4-2`, `SO4(2-)`, `SO₄²⁻`), and the one form the text cannot
decide — a plain digit and sign after a single element symbol, where Fe3+ is iron(III) but N3-
is azide and I3- triiodide — is kept with both readings: the parser reads it as a charge and
records the alternative, both chemistry modes show how every species was read, and the balancer
and the check try the other reading where the default cannot balance and say which reading they
used. Results are also typeset (MnO₄⁻ + 5 Fe²⁺ + 8 H⁺ → Mn²⁺ + 5 Fe³⁺ + 4 H₂O). Twenty-one
fixtures: combustion, permanganate in acid and in base, dichromate, two half-reactions with their
electron counts, a disproportionation, triiodide read the way that balances, the notations, the
refusals. The page still writes no
chemistry of its own: the species are the reader's or the model's.

## The public build

**The label, and the field that is not named.** The site is titled "The Method Research" (`SITE_TITLE`,
which the page, the cite line and the console footer read from `meta`), by the author's decision of
2026-09-20: the website and its indexes exist to carry the work forward, and nothing in the field the
research tree is named for is published. So the tree's own name is a private pattern in the guard
(`(?i)\bwarp\b`, `warp-drive`), every path the site prints from that tree is rewritten by
`public_path()` to `research/…`, its root is printed as "the research tree", and the selftest walks
every paper's non-body fields as well as the index and the particle file for it.


The books the index is drawn from are unpublished and not peer reviewed, and the author's ruling
(2026-09-19) is that **the public site references none of them**: no register numbers, section
numbers, member file names, line references or quoted passages, and no search over the corpus.
The data, the statuses and the instruments stay; provenance outward is the public sources (NIST
ASD, arXiv, DOI) and the papers the author has released to the site — `PUBLIC_PAPERS` in
`webindex.py`, at present the Löwdin paper and the three-body paper, each named on the site by
title. The rule is enforced, not remembered: `PRIVATE_PATTERNS` lists what may not appear in any
string the site ships, `private_strings` walks every string (keys included) of `index.js` and of
every element file, and the selftest fails on the first hit. Where a data string needed rewording
to pass — the coordinates table's own `source` column names a register, and the observed
configurations table is named by file — `public_text` carries the narrow rewrite and the value
beside it is untouched; a status is never changed by this pass. Shipped instrument sources go
through `redact_source`, which keeps the code entire and withholds only a docstring or comment
that cites the books. `LOWDIN-WALK.tsv` is allowed by name (`PUBLIC_NAMES`): it is this
repository's own reconstruction, not one of the books.

**What the flag withholds.** The Particles dialog and the muon energy balance (solver mode 8,
the seven `mucf_*` instruments) read `Muon_Catalysed_Fusion_v1.1.md`, which is not released, so
they build only under `python3 tools/webindex.py --with-particles`; the public build writes
`"particles": null`, the page hides the button, and the solver registry drops any mode whose
`requires` names an absent block. `docfigures.py` still pins the block's figures by building it
on demand, so the numbers stay measured while the site does not carry them. The reference
identifiers found in the unreleased files are still listed — an arXiv or DOI identifier is a
public object — with no citing line.

## Papers, figures, glossary

**Papers.** The four released papers are read on the site, not linked out of it: `papers_block`
renders each from its seated text at build with a small stdlib Markdown renderer (headings,
paragraphs, lists, blockquotes, fenced code, pipe tables, rules, images; arXiv and DOI identifiers
linked by pattern), records its md5 against the store's, copies every figure it cites out of the
extracted tree by the ledger row of the paper's own archive (`PAPER_FIGURE_ARCHIVES`, because two
archives hold a `fig1_shape_sphere.png` and only one is the paper's) with the ledger md5 beside the
measured one, and writes the lot to `data/papers.js`, loaded on demand (`ensurePapers`). The reader
carries a table of contents, the figures inline, a cite line per paper and the md5. The text is the
author's own and is shipped as written — the public-build guard is not run over `papers.js`, and
the three-body paper's own citations of the books stay its own. **The hierarchy law paper is the third**, and
it comes from the research tree rather than the store (`RESEARCH_PAPERS`:
`research/warp-drive/paper/THE-HIERARCHY-LAW.md`, "The Hierarchy Law of Mathematical Languages",
11,350 words by the generator's count, no figures, a provenance ledger and a verification record of its own). No ledger row
records its md5, so the md5 is measured at build and the file's last commit is recorded beside it
(`tree.commit`), the paper card and the reader say so, and the PDF beside it in the tree is copied
to `data/papers/languages/` and offered as a download with its md5, on the card, in the reader and
in Provenance. The guard is run over its text as a measurement (`book_citations`, with the two section-number
patterns excluded and recorded apart as `own_section_marks`, because the paper numbers its own
sections with § and "Section n"), and the selftest asserts that it cites nothing from the books; the slot mechanism (`PAPER_SLOTS`) stays
for a paper named before its file arrives. The selftest asserts the three papers in order, every
store paper's md5 against the store, every figure's md5 against the ledger, the research paper's
commit and PDF, and that the render carries every heading of the Löwdin paper and of this one.
**The index of first-order indexes paper is the fourth** (`RESEARCH_PAPERS`:
`research/warp-drive/paper/THE-INDEX-OF-FIRST-ORDER-INDEXES.md`, read from the tree at
`--warp-root` when one is given, `research_path`), the paper on the indexes this site carries. Its
text cites unpublished material at four sites — three citations of one register entry and the
research tree's own directory in the reproduction appendix — and the site cites nothing from the
books, so `mask` replaces each at build with a visible mark, the count is recorded (`masked`) and
shown on the card and in the reader, and the guard measures zero book citations afterwards; the
PDF beside it is the paper as written and is **withheld** (`pdf_withheld`, `pdf_note`) until the
author reissues it without them. Its last commit is the tree's commit (`--warp-commit`) where the
file is not in this checkout.

**Figures from the data.** The *Figures* dialog draws five figures in the browser, as SVG, from
`index.js` when it opens — no image, no typed number, each caption naming its block and status,
each downloadable as SVG stamped with the edition: the channel equation against every measured
channel (δ READ against δ PINNED, by ℓ, with the rms, R² and median |error| the fixture records),
the residual distribution, where the measurements are (measured cells per Z), the reconstructed
walk's entrant margin at both settings with the displaced ringed (RECONSTRUCTED), and closure
across the layouts (E = 36 split 25 + 11, 20 with helium at group 2, 0 on Janet). The points
behind the first two are `figure_data.equation`, written by `equation_points` over exactly the
rows `equation_figures` scores, so the figure and the fixture cannot disagree.

**Glossary and keys.** A hand-written dialog in `index.html` defines every term and mark the site
uses in the site's own words — the statuses, cells and channels, the channel equation's terms,
layouts and closure, the lattice, the relativistic limit and the walk, the site's own conventions —
42 terms in seven groups. It cites no source and carries no figure; a value keeps its own status
wherever it appears.

**Cite, downloads, editions.** `meta.cite` carries the site's cite line and a BibTeX entry
(author from the released papers, title, year, edition = commit, URL); every paper has its own
under Papers; every node's plate already offered one. `downloads` lists the data as files with the
md5 recorded at build where the file is one blob (`papers.js`, the walk table copied to
`data/LOWDIN-WALK.tsv`, the Löwdin figure), and `--verify` checks each against the index.
`meta.history` is the edition history — every commit that changed `public/` or the generator,
oldest first, with a note written for the site (`EDITION_NOTES`; the commit subjects are git's
record and are not shipped) and a link to the commit. The Provenance panel shows all three, and
the console answers `papers`, `figures`, `cite`, `history` and `glossary`.

## Provenance

The Provenance panel lists every file a number came from with the md5 the store records for it
(from `method/MEMBER-INDEX.tsv` and `drive/MANIFEST.tsv`) against the md5 measured at build; the
git commit; the build time; the totals; the equation's coefficients and the recovered collapse
form; the whole axis table; and the status vocabulary. Every node offers a citation line that
names its path, the commit, the source md5s and its own link, so a figure quoted from the site
can be traced to the byte.

`python3 tools/webindex.py --verify` reads the manifest back out of `data/index.js`, checks every
element `.js` file's md5 against it, strips each wrapper and checks the payload's md5 against
`payload_md5`, and checks every source's md5 against its record. A build removes any `index.json`
or `elements/<Z>.json` of the earlier format so two copies of the index never sit side by side,
and `--verify` reports any that reappear.

## Navigation

Scroll or pinch to zoom, drag to pan, click a node to fly to it. The canvas is focusable
(`tabindex="0"`), and its shortcuts act only while it — or nothing — has focus: `Esc` goes up one
level, `H` the whole index, `+`/`−` zoom, arrows pan; `/` focuses search from anywhere outside a
text field. A table row in the detail plate is a `role="link"` with `tabindex="0"` and opens on
`Enter`. Search takes a symbol, Z or name, or a path — `Fe II`, `Fe II d`, `Fe II d 3`; the ℓ token
is one letter of `spdfgh` or a number (`Fe II 6`), never a substring match, and ℓ = 6, 7 are
labelled by number as the record's `subshell_letter` is; once the particle indexes have loaded it
also suggests a particle by name or an index by title. The address bar carries the path
(`#/Fe/II/d/3`, `#/p/mesons/pi0`), so every node is a link. Copy JSON copies the node's record; Copy link its
address; Raw record shows the record inline; the element file is linked directly.

**If a view does not draw.** The draw loop pauses only its animation frames while `#canvas-wrap`
is scrolled out of view; an explicit draw always paints, because a resize clears the canvas and a
browser whose IntersectionObserver never fires on the way back would otherwise show it blank (the
first report of "3D not rendering" came from the DuckDuckGo Android browser, which has no console).
A debounced scroll listener marks the canvas visible again as a fallback, a `visibilitychange`
handler repaints on return, a drawing error is written on the canvas and kept as
`state.lastDrawError`, and Help carries **Copy diagnostics** — the browser, viewport, canvas
buffer, feature support, view, scene, orbit, loaded data, last draw, last error, and a small
off-screen test draw with the same calls the view uses — the same text as the console command
`diag`, so a phone can report what went wrong.

The home view fits the layout above the legend overlay, so the set-aside actinide row is never
under it at any viewport; the legend can still be collapsed. The Λ₈ ladder's glow is two strokes,
a wide translucent one under a thin bright one, not `shadowBlur`; the ion and channel nodes carry
their measured counts from `buildTree` rather than re-counting each frame; the draw loop pauses
while `#canvas-wrap` is scrolled out of view; and on a phone a selection reveals the plate at once
rather than animating a fly the reader would not see.

The ions inside an element are packed on an Archimedean spiral so consecutive stages are adjacent
and the ladder traces the spiral. The arc length is inverted by Newton's method from the closed
form s(θ) = (b/2)(θ√(1+θ²) + asinh θ), bounded at thirty steps, because a stepwise march on the
residue underflowed to a denormal and never terminated at n = 51, 60, 67, 70, 79, 90, 91, 93, 94,
95, 106 and 111 ions; the spiral starts one full turn out, at ρ = 2r·1.12, so the neutral ion at
the centre and stage II do not overlap and the first ladder step (I → II) has positive length and
is drawn. A node harness over n = 1 … 120 at the three nesting radii returns for every call.

## Verifier notes

**A first-selection freeze in headless Chromium 1194 did not reproduce here.** A file:// review
reported that, in a non-mobile context with default motion, the first `location.hash = '#/Fe'`
stopped the page's own `setInterval` and CDP `evaluate` never returned (nine times; never under
`prefers-reduced-motion: reduce` or mobile emulation). Re-run on the same Chromium build over both
file:// and http, nine fresh-page trials at 1400×860 on `#/Fe` and `#/Fe/II/d/4` all answered
within 3 s with the interval still ticking. The two mechanisms that could have produced it are
removed anyway: the frame loop no longer re-enters `ensureElement` for an element whose load is
already pending, and the ladder no longer uses `shadowBlur`. If it is seen again, record the
Chromium build and whether a headed browser shows it before treating it as the site's.

**Monospace throughout.** `--font-display` resolves to the same IBM Plex Mono stack as the body, so the site title, node titles and dialog headings are monospace like everything else, as the author's criterion asks; the canvas labels use it too.

**The drift operation and the coefficient selftest load every element file** — the count and size
are read from the manifest and printed beside the mode and on its selftest button, never typed. The
load is settled rather than all-or-nothing: an element whose file cannot be loaded is named in the
result and the drift runs over the rest.

## Deploying

The site is static. `.github/workflows/pages.yml` deploys `public/` to GitHub Pages on every push
to `main` that touches it, and on demand, once the Pages site exists with source "GitHub Actions".
**The workflow cannot create that site itself on this repository.** It carries
`enablement: true` on `actions/configure-pages`, and run 35385180002 (2026-09-18, on the branch)
failed at that step with *Resource not accessible by integration*, as did the two earlier runs on
`main` before that option was set. The repository was then made public (2026-09-19) and runs
35416927668 and 35416992727 failed identically: the job's `GITHUB_TOKEN` may not create a Pages
site on a public repository either — that endpoint needs administration rights, which the
workflow token never carries, and visibility was not the cause. So the one-time step is a
person's, and only that: Settings → Pages → Build and deployment → Source: GitHub Actions. After
that the next push to `main` under `public/**` deploys (or run the workflow by hand), and the run's
`page_url` is the address. Any static host serves it unchanged, and because the data ships as script files it needs no server at
all: `public/` copied to a phone and `index.html` opened from the file system is the same site.

## What it is not

It is not a member, a Register entry, or mirrored content, and it writes to none of them.
`public/data/` is derived from `method/members/LW1-ground.py`, `method/members/tower-2.py`,
`tools/cypher.py`'s ℛ and `drive/The Method Materials/COORDINATES-2_13.csv`, through
`tools/populate.py` alone. It replaces an earlier `public/index.html` and
`tools/export_web_index.py` whose figures were invented rather than read; that pair is gone.
