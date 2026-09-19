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
kept on the orbit so the scene does not swim as it turns, and refitted on resize); a heavy element
is a needle by the record's own geometry, so its ions are kept at least 13 px apart with the base
anchored near the bottom, the lower stages where the known cells sit coming up first and the rest
reached by zoom or pan (Shift-drag, or a two-finger drag). The slab stands on a base plane ruled
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

Six modes sit beside the index, each a browser-side mirror of one instrument and each carrying that
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
every chart for free (105 of 105) and what it shows is join-closure. Seven of the eight channels are
now occupied. `docket27.py` also counts antimatter rather than implying it — 231 of the 550 charted
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
refusal after it; the quasiparticle work is still in progress on the other session.

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
its block to `particle_index_block`, and its figures to the selftest.

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
phase labels, an unknown symbol refused, no arrow refused). The page writes no chemistry and no
procedure: it checks what another author wrote.

## The public build

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

**Papers.** The two released papers are read on the site, not linked out of it: `papers_block`
renders each from its seated text at build with a small stdlib Markdown renderer (headings,
paragraphs, lists, blockquotes, fenced code, pipe tables, rules, images; arXiv and DOI identifiers
linked by pattern), records its md5 against the store's, copies every figure it cites out of the
extracted tree by the ledger row of the paper's own archive (`PAPER_FIGURE_ARCHIVES`, because two
archives hold a `fig1_shape_sphere.png` and only one is the paper's) with the ledger md5 beside the
measured one, and writes the lot to `data/papers.js`, loaded on demand (`ensurePapers`). The reader
carries a table of contents, the figures inline, a cite line per paper and the md5. The text is the
author's own and is shipped as written — the public-build guard is not run over `papers.js`, and
the three-body paper's own citations of the books stay its own. **The hierarchy of mathematical
languages paper is a slot** (`PAPER_SLOTS`, `held: false`): the author named it as released, its
file is not in the repository, and the site lists it and shows nothing in its place. The selftest
asserts the two papers and the slot, every held paper's md5 against the store, every figure's md5
against the ledger, and that the render carries every heading of the Löwdin paper.

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
labelled by number as the record's `subshell_letter` is. The address bar carries the path
(`#/Fe/II/d/3`), so every node is a link. Copy JSON copies the node's record; Copy link its
address; Raw record shows the record inline; the element file is linked directly.

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
