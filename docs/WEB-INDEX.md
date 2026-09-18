# `public/` — the index as an interactive website

The Method 1.6, read as a zoomable index in the manner of OneZoom: the drawn periodic layout at
the top, each element opening into its ions, each ion into its ℓ channels, each channel into its
cells, and **every value carrying the status the corpus gives it.** Built for scientists,
researchers and students as a research tool, not a brochure.

```sh
python3 tools/webindex.py             # write public/data/ from the instruments
python3 tools/webindex.py --selftest  # 19 fixtures, nothing written
python3 tools/webindex.py --verify    # public/data/ against its own manifest and the sources
cd public && python3 -m http.server   # then open http://localhost:8000/
```

Stdlib only on the Python side; no build step, no package manager, no framework on the web side.
`public/index.html`, `public/style.css` and `public/app.js` are hand-written; everything under
`public/data/` is generated and never hand-edited.

## What it shows

| level | node | drawn from |
| --- | --- | --- |
| the index | the drawn layout of section 6 (period × group), or Janet's (n+ℓ, ℓ) | `index.json` → `layout`, `closure` |
| element | Z, symbol, ground shells and level, configuration table, layout cell, closure, Λ₈ ladder | `elements/<Z>.json` (populate.py's record) |
| ion | spectroscopic stage, Nₑ, core, the eight channels, the Λ₈ step at that stage | the element record's `channels` and `lambda8` |
| channel | ℓ, p, n₀, B, C(Z, ℓ), δ by equation, and its cells | one entry of `channels` |
| cell | δ, grade, witness, source, bound note, B in the csv against B computed, residual | one row of COORDINATES-2.13 |

Two layouts of the same elements, because the corpus reads the two indexes differently: on the
period × group layout ℛ admits 126 cells against 90 held, **E = 36**, and the 36 are drawn as
dashed ghosts, each a node with its own explanation; on Janet's coordinate **E = 0** and there are
no ghosts to draw. The layout toggle is the closure figure made visible.

Elements 109 to 120 are drawn apart, dashed, because `LW1-ground.py` stops at 108 and
COORDINATES-2.13 does not. Their rows are shown `READ` from the csv with no configuration,
equation or derived value behind them, and the panel says so.

## The status travels with the value

`index.json` carries `populate.py`'s own axis table — every axis with its status and source —
and the page looks the status up by axis rather than inventing one. The five statuses are
`READ`, `PINNED`, `DERIVED`, `RECOVERED` and `RECONSTRUCTED`, with the meanings `docs/POPULATE.md`
gives them; a value the corpus does not carry (an IUPAC element name, say) is badged as carrying
no status. Nothing on the page is computed by the page: `app.js` does no arithmetic, and a residual
shown is the one `populate.py` wrote.

Six caveats travel with the data and are shown where they bite (`index.json` → `caveats`): the
Z > 108 boundary; the B column built on the withdrawn aufbau table (register 1306); the 25 measured
rows whose B is a dispersion, not a bound; the Λ₈ mapping being one reconstruction; the equation's
validated domain; and n₀'s reading. Each is drawn from `docs/POPULATE.md`'s "Known gaps" and
"Two findings", and a cell where B disagrees between the csv and the observed configurations
shows **both** values with the disagreement marked — recorded, never repaired.

## Provenance

The Provenance panel lists every file a number came from with the md5 the store records for it
(from `method/MEMBER-INDEX.tsv` and `drive/MANIFEST.tsv`) against the md5 measured at build; the
git commit; the build time; the totals; the equation's coefficients and the recovered collapse
form; the whole axis table; and the status vocabulary. Every node offers a citation line that
names its path, the commit, the source md5s and its own link, so a figure quoted from the site
can be traced to the byte.

`python3 tools/webindex.py --verify` checks every element file's md5 against the manifest in
`index.json` and every source's md5 against its record.

## Navigation

Scroll or pinch to zoom, drag to pan, click a node to fly to it. `Esc` goes up one level, `H` the
whole index, `/` focuses search, `+`/`−` zoom, arrows pan. Search takes a symbol, Z or name, or a
path — `Fe II`, `Fe II d`, `Fe II d 3`. The address bar carries the path (`#/Fe/II/d/3`), so every
node is a link. Copy JSON copies the node's record; Copy link its address; Raw record shows the
record inline; the element file is linked directly.

## Deploying

The site is static. `.github/workflows/pages.yml` deploys `public/` to GitHub Pages on every push
to `main` once Pages is set to "GitHub Actions" under the repository's Settings → Pages. Any
static host serves it unchanged; only same-origin `fetch` of `data/` is needed.

## What it is not

It is not a member, a Register entry, or mirrored content, and it writes to none of them.
`public/data/` is derived from `method/members/LW1-ground.py`, `method/members/tower-2.py`,
`tools/cypher.py`'s ℛ and `drive/The Method Materials/COORDINATES-2_13.csv`, through
`tools/populate.py` alone. It replaces an earlier `public/index.html` and
`tools/export_web_index.py` whose figures were invented rather than read; that pair is gone.
