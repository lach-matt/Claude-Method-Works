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
cube per cell, the cells of a site side by side along the third axis where it holds two
multiplicities. Known cells are full cubes coloured by grade (or by limit, with the legend's
toggle); unmeasured ones are the faint body of the slab; the Λ₈ ladder climbs the front edge, one
rung per recorded step; the stage axis carries every ion as a tappable roman numeral and the ℓ axis
its letters. Drag rotates, wheel or pinch zooms, arrow keys rotate, a tap on a cube selects the cell
and on a numeral the ion, and the plate follows as on the plane. The third layout, **Lattice**, is
the whole solid: every element a slab at its Z (charge 1..Z by ℓ 0..7 — `webindex.py` asserts the
58,080 sites are exactly that), the 1,287 known cells as cubes, one per site, from a compact block
`index.js` → `lattice` carries (`[Z, charge, ℓ, mult, grade]` for every measured or exact row; the
axes READ from the record's caption, the drawing DERIVED, nothing computed); the measured wedge at
low Z and low ℓ is the record's own remark made visible, and a tap on a slab opens the element. The
**Nest** toggle shows an element as the nested circles instead — ions, channels, cells — which is
the reading the plane used alone before. The renderer is hand-written on the same canvas: a yaw and
pitch about the scene's centre, a mild perspective, faces sorted far to near and shaded by a fixed
light, no library, so the page still opens from a plain file on a phone. The element plate's
"The lattice" section names the axes with their source and counts the cubes drawn, and the console
answers `lattice`.

Elements 109 to 120 are drawn apart, dashed, because `LW1-ground.py` stops at 108 and
COORDINATES-2.13 does not. Their rows are shown `READ` from the csv with no configuration,
equation or derived value behind them, and the panel says so.

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
