# GRAPH-FINDINGS — what the 2026-09-04 graph pass measured

Every number here was measured in this repository on 2026-09-04 and every claim can be re-run from
the commands in the last section. **Nothing recorded here has been repaired.** The chat-67 full hold
governs this file exactly as it governs a section read: a finding is recorded, never repaired.

**Three passes are recorded here, and the `AMBIGUOUS` grade is the starting point of all three.**
§1–§10 come from the first graph (20,463 nodes, 27,601 edges, 2,434 communities over 3,279 files) and
trace the seven edges it put forward: **all seven refusals were correct**, none was an extraction
defect, and four mark a place where a filename or a phrase is shared but the referent is not. §11
answers the seven the 2026-09-04 rebuild proposed (26,364 nodes) — **four of which this file already
answered**, because a rebuild carries no resolutions forward. §12 is the census of **all 120**
`AMBIGUOUS` edges in the rebuilt graph, the other 113 included, and it is where the one edge that
found a real fault in the repository is written up.

**§13 is not a trace but a refusal**, and it is the one section about the tool rather than the corpus:
an incremental `--update` was run on six changed files and stopped before the write, because its
merge would have collapsed 121 provenance distinctions across files that had not changed.

## Status vocabulary

Used as `method/README.md` and `docs/COVERAGE.md` use it, and never flattened:

- **HELD** — the bytes are in this repo and their md5 is recorded.
- **ABSENT** — not reachable from any source here. **Not a finding of loss.** A name in prose, a
  certificate or a handoff is not proof a file ever existed as a file.
- **RECOVERED** — measured out of the corpus's own data.
- **RECONSTRUCTED** — not measured; derived.

---

## 1. The `HANDOFF-13` collision, and a fingerprint for an absent document

`recovered/GATE-CERTIFICATE-chat62.md` opens `# §0 GATE CERTIFICATE — chat 62 (HANDOFF-13)` and
pins the handoff it gated. The `HANDOFF-13` this repo holds is a **different document**:

| | the certificate's HANDOFF-13 | `recovered/HANDOFF-13.md` |
|---|---|---|
| size | 9,463 B | 9,015 B |
| lines | 112 | 54 |
| md5 | `a07ad36d649743186447c3b3a67a33f8` | `54f720751582ed0872bfc7dc3b68cf77` |
| self-ID | chat 62 · BUILD62 compendia · Register 165–present | chat 63 → chat 64 · BUILD76 main + BUILD79 compendia · Register 1–1787 |
| source conversation | — | 63 |
| created | 2026-08-29 16:33 (certificate) | 2026-08-29 22:00 |

**md5 `a07ad36d649743186447c3b3a67a33f8` appears in no row of `recovered/LEDGER.tsv`,
`extracted/LEDGER.tsv` or `drive/MANIFEST.tsv`.** Status: **ABSENT**, and not a loss — the
certificate records it as *"not present in Drive Materials listing (page 1); chat-uploaded copy
used."* It was never in the mirror. What this trace adds is a **byte-exact fingerprint**: if a
9,463 B / 112-line file with that md5 ever surfaces, it verifies in one command.

**Why the collision exists.** The corpus says so itself, in the recovered HANDOFF-13's second line:
*"HANDOFF-11-1.md called this session 'chat 62' — the chat that produced BUILD75/HANDOFF-11 is
titled 62."* Chat numbering was already unstable, so handoff numbers were reused across
generations. The same mechanism produces the `HANDOFF-23`/`24`, `HANDOFF-25`/`26` and
`HANDOFF-3`/`4` pairs.

### An open item this trace closed

The certificate ends with an explicit non-measurement:

> *"Drive holds three tower instruments … Sizes of tower-1-1 and tower-2 agree; **identity not
> measured**."*

It is now measured, four ways, all agreeing on md5 `c0bce27abe23ad939d297ac1022a01d7` at 1,213 B:

- `drive/The Method Materials/tower-1-1.py`
- `drive/The Method Materials/tower-2.py`
- `drive/The Method Materials/CORPUS/tower-2.py`
- `method/members/tower-2.py` (the seated member)

and the recovered HANDOFF-13, written by a different chat, independently states that same md5 for
`tower-2.py`. **`tower-1-1.py` and `tower-2.py` are byte-identical.** `python3
method/members/tower-2.py` prints `976 / 1654 / 2535 / 13585 / 70905 / 199130` — six of six. That
retroactively validates the certificate's own PASS, which checked `tower-1-1.py` behaviourally
rather than by hash.

---

## 2. `Ruling 28` ↔ `Ruling 41` — a dependency, not a contradiction

Ruling 41 exists **because** Ruling 28 was already executed. The project's standing prompt still
carried a "Phase 0–4" plan to *perform* the absorption (Löwdin then three-body merge, renumber
three-body to 1713–1724, Chapter 36, Part VII retitled). Chat 71 measured (W-107) that BUILD90 main
**already** seats Chapter 35 at L9716 and Chapter 36 at L9892 under Part VII, with the Register
carrying Löwdin at 1701–1712 and three-body at 1713–1724.

So the plan described completed work, and Ruling 41 is its closure notice — *"Do not re-open it and
do not put it to M; this handoff's plan governs."* Stated in `recovered/HANDOFF-22.md` and
`recovered/HANDOFF-24.md`. No sentence in the corpus names both rulings, which is why the edge could
only be `AMBIGUOUS`: the link is recoverable only by reading the Phase 0–4 content.

---

## 3. Two instrument faults, same family, opposite polarity

Both are instruments trusted before the instrument itself was checked. They fail in opposite
directions, which is why `semantically_similar_to` was correctly held at `AMBIGUOUS`:

| | hyper-radius normalisation | first-match version picker |
|---|---|---|
| where | `audit_state1_failing.py` L58, `Vs=V0_shape(w,m)/R` | the Contents checker / `index_pages.py` |
| fault | the hyper-radius carried into the shape potential | takes the first page whose *text* contains the heading, so prose occurrences win |
| symptom | check A **False 13/13** — fails loudly | six "mis-paged" Contents lines — **manufactures findings** |
| resolution | delete `/R`, giving `audit.py` L58 | W-088 built the sound checker (require a heading-shaped line, skip Contents lines, search the body): **all six were correct** |
| recorded in | `recovered/README.md` item 4 | `method/members/WORKING-REGISTER.md` W-085, W-088 |

One produces a false negative you cannot miss; the other produces false positives that look like
findings. Same mechanism *class*, not the same mechanism. Both sit under the corpus's own standing
rule from F59.3: **"a control must be proven to vary the thing it controls for."**

---

## 4. `DEF-151d` ↔ `GATE-ch151Bclose4` — co-membership, not citation

Both are artefacts of the same close (chat 151-B) under `incoming/BUILD184-PARTS/`.
`GATE-ch151Bclose4` is the §0 gate certificate that authorised the build — verdict PASS, census
byte-identical, `run --core` 5/5, MANIFEST 358 listed / 359 extracted, 72 of 72 banked goldens
reproducing, §0a empty. `DEF-151d` is the deferred block whose items that build closes. **Neither
document names the other**; `incoming/BUILD184-PARTS/REBUILD-BUILD184.md` names both. A correct
`references` relation that is unprovable from either endpoint alone.

---

## 5. The two three-body questions — the graph's doubt matches a rule the corpus states

Both ask whether the gravitational three-body stratification connects to the nuclear / deuterium
physics. **The corpus answers directly, and the answer is no.** From the Register, the *dimensional
obstruction*:

> *"the dimensional obstruction applies to any scheme reasoning from combinatorial or
> configuration-space quantities to nuclear rates"*

with the reason given as scale separation — bonding energies of order 10⁻¹ eV over 10⁻¹⁰ m against
barrier penetration at 10⁵ eV over 10⁻¹⁵ m, *"a six-order gap in energy and five-order gap in
length."* The master theorem is a phase-space (configuration-space) result. **Upgrading either edge
above `AMBIGUOUS` would reproduce exactly the error the corpus documents as its own worked negative
result.**

A second reason to hold them low: `recovered/README.md` item 6 records the stratification as
**`NOT HELD — never data`** — *"E(𝔉)=0 was a theorem-assembly, not a computation … No data object
was ever built; the Brudno step is a citation."*

---

## 6. The truncation census — 23 files, 3,004 lines, and only one hard boundary

23 files under `recovered/` still carry a `< truncated lines N-M >` marker, totalling **3,004
missing lines**. This is a bounded, enumerated set, not an unknown.

**22 of the 23 have a complete copy in this repo.** `recover.py`'s "completeness outranks recency"
ordering worked: the complete body took the plain name and the truncated one took the `__<md5>`
suffix. The three that had no plain-named sibling — `HANDOFF-74`, `75`, `78` — are marked
`PRESENT-IN-REPO` in `recovered/LEDGER.tsv` with an empty target, because their complete bodies were
already held under `drive/`:

| handoff | complete body | md5 | held at |
|---|---|---|---|
| HANDOFF-74 | 51,439 B | `badd59f900…` | `drive/The Method Materials/{LOWDIN,THREEBODY}-DELIVERY-1/` |
| HANDOFF-75 | 47,460 B | `3e8423fe84…` | same, both folders |
| HANDOFF-78 | 47,710 B | `0b30bba90f…` | same, both folders |

**The single hard boundary is `recovered/HANDOFF-34.md`** — 15,426 B, **lines 34–42 missing (9
lines)**, no complete copy anywhere in the repo, and the gap falls inside its §0 gate step list
(after step 5, before "The computable batch (r2-ch13j.py)").

That truncation is **not a recovery defect**. The marker `< truncated lines 34-42 >` is present
twice in the source shard itself, `drive/chats/2026-08/37aaed26-2634-4eba-8490-9cac72ddc78a.json` —
the chat export rendered the message with the lines already elided. Status: **ABSENT**, hard
boundary of the export, not reachable by re-running `recover.py`.

---

## 7. Duplicate names in `recovered/` — the `__<md5>` convention

**171 filenames in `recovered/` have more than one distinct body**, 25 of them `HANDOFF-*`.

> **The `__<hash>` suffix in `recovered/` is NOT the `__<driveFileId>` convention.** CLAUDE.md's
> rule — *"a `__<driveFileId>` suffix marks an older Drive copy; the newest copy keeps the plain
> name"* — governs `drive/`. In `recovered/` the suffix is `recover.py`'s **md5 prefix**, a
> disambiguator for two distinct bodies claiming one filename. The "older/newer" reading does not
> transfer.

Two distinct shapes hide under that one convention:

**(a) The truncated re-posting.** For `HANDOFF-37` … `HANDOFF-53`, the pattern is regular: a full
body written *from* chat N, and a ~16.2 KB truncated body appearing in chat N+1 — the handoff being
received and re-posted. These are damaged duplicates, not separate documents. All carry exactly one
truncation marker; all their plain-named counterparts carry none.

**(b) The genuine divergence.** `HANDOFF-26.md` (conv 75, 10,675 B) and
`HANDOFF-26__66aa3bd5.md` (conv 74, 10,707 B) are both complete and **disagree on a governance
rule**:

| | plain `HANDOFF-26.md` | `HANDOFF-26__66aa3bd5.md` |
|---|---|---|
| source conversation | 75 | 74 |
| LEDGER `created_at` | 16:14:53Z | 15:22:57Z |
| stated bundle md5 | `893a9826…` | `1f9024af…` |
| stated bundle size | 3,204,034 B | 3,203,041 B |
| how `RULINGS-R2.md` / `DEFERRED.md` grow | `close.py --append DEFERRED.md …` | forbids it — accretion into new `RULINGS-R2-chNN.md` / `DEFERRED-chNN.md` members |

The variant argues itself out of the append flag mid-sentence: *"pass nothing extra — **no:** those
two are old members … (append-only by accretion; never edit the seated member)."* **The direction is
the surprise**: that self-correction is in the *earlier* file (conv 74, 15:22); the *later* one
(conv 75, 16:14) is back to `--append`. The accretion rule was reached and then abandoned within the
hour. Both preserve "never edit a seated member"; they differ on whether `close.py` may append to
one. **Unreconciled — this file records it, it does not settle it.**

---

## 8. The Löwdin bridge series — was 31 of 63 absent, now 3 of 66

**Superseded by the `RECOVERED-BY-WRITE` pass, and kept because the reasoning still stands.**

As first measured, `recovered/` held **32** numbered `BRIDGE-LOWDIN-SESSION-N.md` files, the highest
63, and 31 of the series were absent from the whole repository. Walking the export's tool calls
recovered **28 of those 31**, and found the series runs to **66**, higher than anything then known:

```
now held   63 of 66      still absent   1, 2, 62
```

The original reading was right about the shape and wrong only about reachability. Each surviving
bridge names its predecessor in its header, so the successor spine reconstructs itself and the gaps
are visible from inside the chain — that is how sessions 19, 20, 21, 24 and 27 were known to be
missing, and all five are now held.

Status of the remaining three: **ABSENT — still not a finding of loss.** A bridge naming its
predecessor is not proof that predecessor was ever written to a file. There is also an unnumbered
`BRIDGE-LOWDIN-SESSION.md`.

**The lesson is the general one of this session:** absence measured against the repository is a
statement about reach, not about the world. Nothing was lost between the two measurements; the second
one simply read the export structurally. See `docs/HANDOFF-GAP.md`.

---

## 9. Instrument notes from the AST pass

**Four `.py` files under `recovered/` fail `ast.parse` on Python 3.11 but are valid Python 3.12+.**
They are *not* defects — the failure is "f-string expression part cannot include a backslash", a
restriction lifted by PEP 701. The AST extractor here runs 3.11.

- `recovered/chk.py`, `recovered/mo.py`, `recovered/r2-ch13o.py`, `recovered/readB.py`

**Three are genuinely malformed, and the malformation is the corpus's own** — each construct was
checked byte-for-byte against its source shard and is present there verbatim. `recover.py` did not
introduce them, and none carries a truncation marker:

| file | line | the construct |
|---|---|---|
| `recovered/l-ch1.py` | 5 | `from tower import L8 if False else None` — a conditional expression in an import; never valid Python |
| `recovered/whatisit.py` | 39 | `if (a[i]+b[i])%2==0 for i in range(0) else True:` — malformed comprehension |
| `recovered/caps__163a1d7c.py` | 7–8 | `for n in range(1,NM+1):` with no indented body; the next line dedents to `several=0` |

**The graph's 7,088 dangling-endpoint edges are benign.** Every one is an AST `imports` /
`imports_from` naming a module that is not a file in this repo — `re`, `numpy`, `itertools`,
`sympy`. The semantic layer contributes **zero** dangling edges. Expected for a corpus whose `.py`
files import a stdlib; not corruption.

---

## 10. Re-verification

Every claim above re-runs from these:

```bash
# §1 — the HANDOFF-13 collision and the absent fingerprint
md5sum recovered/HANDOFF-13.md && wc -lc recovered/HANDOFF-13.md
grep -rn 'a07ad36d649743186447c3b3a67a33f8' recovered/LEDGER.tsv extracted/LEDGER.tsv drive/MANIFEST.tsv   # expect: no rows

# §1 — tower-1-1 == tower-2, and the seated member still runs
md5sum "drive/The Method Materials/tower-1-1.py" "drive/The Method Materials/tower-2.py" method/members/tower-2.py
python3 method/members/tower-2.py      # expect 976 / 1654 / 2535 / 13585 / 70905 / 199130

# §6 — the truncation census
grep -rlc 'truncated lines' recovered/*.md | wc -l                      # expect 23
grep -c 'truncated lines' recovered/HANDOFF-34.md                       # expect 1
grep -c 'truncated lines 34-42' drive/chats/2026-08/37aaed26-2634-4eba-8490-9cac72ddc78a.json   # expect 2

# §7 — duplicate names, and the HANDOFF-26 divergence
awk -F'\t' 'NR>1{c[$1]++; if(c[$1]==2) n++} END{print n" duplicated filenames"}' recovered/LEDGER.tsv
grep -c -- '--append' recovered/HANDOFF-26.md recovered/HANDOFF-26__66aa3bd5.md   # expect 1 and 0

# §8 — the Löwdin bridge gaps
ls recovered/ | grep -oP 'BRIDGE-LOWDIN-SESSION-\K[0-9]+' | sort -n | uniq | tr '\n' ' '

# §9 — the three malformed instruments; each must fail to parse on any Python.
# l-ch1 and whatisit raise SyntaxError, caps raises IndentationError (a SyntaxError
# subclass). Four further files fail ONLY on Python < 3.12 and are not defects.
for f in recovered/l-ch1.py recovered/whatisit.py recovered/caps__163a1d7c.py; do
  python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" "$f"; done
```

## 11. The 2026-09-04 rebuild's seven questions — four were already answered here

The rebuilt graph (26,364 nodes) proposed seven Suggested Questions, all from `AMBIGUOUS` edges.
**Four of the seven are questions this document already answers.** That is not a defect in either the
graph or the document: the questions are generated from `AMBIGUOUS` edges, a rebuild starts from the
sources and carries no resolutions forward, and the edges are *correctly* ambiguous — so the same
questions will resurface at every rebuild. **Read this file before tracing them.**

| # | question | verdict |
|---|---|---|
| 1 | `READING-LIST-STAGING.tsv` ↔ `T9 — 1.7 staging fault` | **co-membership** (new) |
| 2 | `LADDER-K-Kr.tsv` ↔ `Kr II URL` | **co-membership + a data dependency** (new) |
| 3 | dimensional obstruction ↔ gravitational three-body stratification | already §5 — **no** |
| 4 | `O3` deuterium overlap ↔ measure-disjoint stratification | already §5 — **no** |
| 5 | `DEF-151d` ↔ `GATE-ch151Bclose4` | already §4 — co-membership |
| 6 | hyper-radius normalisation ↔ first-match version picker | §3, **but a third instrument** (new) |
| 7 | `Lr I 7p < 6d` ↔ tail convention ruled out | **stated, and graded too low** (new) |

### 1 and 2 — two more rows of one owed board

Both pairs are the same species as §4's `DEF-151d` finding: **co-membership on a parent that neither
endpoint names.** `BRIDGE-1_8_3-to-next.md` §4 lists five open threads with owners —

> *"(1) ladder-as-limit ruling — M; (2) T8-J width — M; (3) Kr II URL — M; (4) write the 93 —
> Claude on M's word; (5) T9 quarantine/repair — M."*

— and `recovered/OWED.md` names the set outright: *"**Board rows 1–5** — ladder-as-limit · T8-J
width · Kr II URL · the 93 series · T9's 65."* Question 1 pairs row (4) — the *93 new* series in
`READING-LIST-STAGING.tsv`'s own row — with row (5), T9. Question 2 pairs row (3) with the ladder it
concerns.

**Question 2 carries something question 1 does not: a real data dependency.** `URLS-SUPPLIED.md`
states that *"`sremoval=on` is the parameter that produces the MULTI-CHARGE ladder — it is what gave
`LADDER-K-Kr.tsv` its 495 rows across every ionisation stage."* The Kr II URL is the outstanding
capture for that ladder's Kr II stage, so the two are linked by the data and not only by the board.
`conceptually_related_to` is the right relation; `AMBIGUOUS` understates it slightly and
`references` would overstate it, since neither file cites the other.

### 6 — the first-match fault has a third instrument, and §3 did not have it

§3 pairs the hyper-radius normalisation fault with a first-match picker in **the Contents checker /
`index_pages.py`**. The rebuilt graph points at a *different* one: `recovered/03-seal.md`, where
`regchat.py`'s **version picker** used `re.search` across three directory listings and

> *"took the FIRST match rather than the highest, so it computed the bank name already in force and
> wrote over it — and over the copy already staged in outputs."*

That is a third member of the family, and the file names the family itself — *"an instrument that
reads a population and takes what it happens to reach first rather than what the population says —
R 1578's object-versus-observer fault."* §3's reading stands unchanged; the class is larger than it
recorded. Note the polarity: this one is **destructive** rather than merely wrong, and the same entry
draws the second rule — *"a seal is a fixed point of the record and MUST NOT be silently replaced."*

### 7 — stated, and the only edge here graded too low

Session 19 (`FINDING-T7C-SO-SESSION-19.md`) reaches Lr I's 7p < 6d ground order from the
one-electron object and then names what remains:

> *"The one open shell-systematic is the 5d edge … **the single named obstruction to a closure
> statement on the corridor observables.** Candidates (none opened; M ruling): (a) … (c) …"*

Session 20 (`FINDING-T7C-TAIL-SESSION-20.md`) opens with *"T7C TAIL CONVENTION (**candidate (c) of
bridge-19 s6**)"* and closes it: *"(c) RULED OUT as a closure of the 5d edge — wrong sign, and not
SR-specific."* The softer floor moves the object **away** from measurement.

So the relationship is **stated, directional and eliminative**: session 20 rules out one of the
candidate closures for the obstruction session 19 named. The citation is in session 20's own title.
`AMBIGUOUS` is too low — this is `references` at `EXTRACTED` strength — and it is the one edge of the
seven where the grade, not the reading, is what needs correcting. **Not repaired in the graph**: the
graph is regenerated, never hand-edited, and the finding is recorded here instead.

### What the four repeats mean for reading the graph

A question resurfacing is evidence the edge is genuinely undecidable **from its two endpoints**,
which is what `AMBIGUOUS` means. Three of the seven resolve to *co-membership on a parent document* —
a shape the corpus produces constantly (owed boards, gate certificates, deferral blocks) and one a
pairwise edge cannot express. The graph carries hyperedges for exactly this, and the fact that these
three arrived as ambiguous pairwise edges rather than as hyperedges is the most actionable thing in
this section for a future extraction pass.

---

## 12. The other 113 `AMBIGUOUS` edges — a census, and one of them is a real fault

§11 traced the seven the rebuild put forward as Suggested Questions. **The graph carries 120
`AMBIGUOUS` edges in all**, and this section accounts for the rest of them. The census first:

| | count |
|---|---|
| `AMBIGUOUS` edges in the graph | **120** of 36,150 links (0.33 %) |
| sourced from an image file | **80** |
| sourced from a text file | **40** |
| of those 40, traced in §11 as the rebuild's questions | 7 |
| of those 40, both endpoints in the same document | 5 (two of them §11's Q1 and Q2) |
| cross-document text edges not previously traced | **28** |

Relations, all 120: `conceptually_related_to` 66 · `references` 35 · `rationale_for` 10 ·
`semantically_similar_to` 6 · `shares_data_with` 2 · `cites` 1.

### 12a. All 80 image edges are inside one figure, and the vision pass doubts at 38× the text rate

The 80 image-sourced edges come from **52 distinct figures**, 66 of them under
`extracted/archives/restore-point-2-13/`. **Every one of the 80 has both endpoints in the same
image** — the vision pass never drew an ambiguous edge from a figure to anything outside it. All ten
`rationale_for` edges in the whole graph are here.

The rates are the finding: **4.6 % of the 1,752 edges from image files are `AMBIGUOUS`, against
0.12 % of the 34,398 from text files.** Reading a chart produces relations the reader cannot ground —
a caption's axis label against a plotted series, a legend entry against a fitted line — and the
extractor graded them honestly. **These are not candidates for tracing**: the figure is the whole
evidence, and a reader looking at it has everything the edge has. They are a measurement of the
vision pass, not of the corpus.

**Re-measured on the 2026-09-11 rebuild, which read all 80 figures: the rate holds and the
containment does not.** 29 of 644 image edges are `AMBIGUOUS` — **4.50 %**, against 4.6 % — so the
vision pass doubts at the same rate on a fresh reading, which is the part of this section that
replicates. The text rate is **0.237 % of 41,815**, about twice the 0.12 % recorded here, so the 38×
ratio is now nearer 19×; the ratio was never the finding, the disparity was. What does not replicate
is the containment claim: **9 of the 29 cross a file**, where the 2026-09-04 build had none. All nine
are figure-to-figure — `fig-constraints.png` to `fig-sections.png`, `fig13.png` to `fig11.png`,
`fig09.png` to `fig07.png` and six more — so the narrower statement still holds, that **no image
`AMBIGUOUS` edge reaches out of the figure set into a text document**. The blanket "nothing to trace"
needs that qualification: for those nine the evidence is two figures rather than one, and a reader
wanting to judge the edge has to hold both. Recorded, not repaired.

### 12b. The five handoff-supersession edges: the handoff number space is used twice

The graph drew five `AMBIGUOUS` edges between consecutively numbered handoffs —
`HANDOFF-24 → 23`, `26 → 25`, `32 → 31`, `45 → 44`, and `22 → 15__99520fa7`. Tracing them found
something neither endpoint states and no earlier pass here recorded.

**`recovered/` holds 114 numbered handoff files written under two different numberings, and the
ranges overlap at 3–53.** Classify each file by the chat pair its own body states:

| numbering | rule | earliest | latest | files |
|---|---|---|---|---|
| **pre-restart** | handoff = origin chat **+ 2** | `HANDOFF-3` ← "Rebuild 2" | `HANDOFF-53` ← chat 51 → 52 | **18** |
| **post-restart** | handoff ≈ origin chat **− 48** | `HANDOFF-7` ← chat 55 | `HANDOFF-95` ← chat 142 | **85** |
| header states no chat pair | (early post-restart, "written by chat 60" form) | | | 11 |

The chat lineage itself is continuous — `drive/chats/INDEX.tsv` holds "Rebuild 1"–"Rebuild 12" and
then plain-numbered conversations **13 to 143 with only two gaps, 20 and 109**. So this is *one*
project renumbering its handoffs, not two projects. **The corpus records a fork at the same
moment.** `recovered/HANDOFF-7.md` — the earliest post-restart file, titled *"Lineage merge"* — says:

> *"**LINEAGE MERGE (BUILD55).** Chats 52/53 had forked from BUILD53: chat 52 → BUILD54 … chat 53 →
> BUILD53.REPAIRED … repair set replayed onto BUILD54 by patch, zero rejects → BUILD55, M-ruled."*

The renumbering and the fork coincide. **Nothing states that one caused the other**, and this file
does not assert it.

**Where the post-restart numbering steps, a handoff was retired unused.** The offset moves −49 → −48
between numbers 25 and 26, and −48 → −47 between 33 and 34; both steps are documented:

> `HANDOFF-26`: *"chat 74 → chat 75 (**supersedes HANDOFF-25, retired unused**)"*
> `HANDOFF-34`: *"**HANDOFF-33 and BUILD108 are retired unused** — they were presented before M's
> ruling arrived … **must not be uploaded**"*

`RULINGS-R2.md` states the same event from the other side — chat 74's ruling 4, *"built in chat 74
itself (BUILD101 + HANDOFF-26; HANDOFF-25 and BUILD100 retired unused)"*.

#### The fault, and it is small, exact and worth knowing

**Six numbers hold only the pre-restart document while a post-restart handoff cites that number as
its own predecessor: 23, 25, 32, 33, 43, 44.** At each, a citation resolves to the wrong document:

- `HANDOFF-24.md` (chat 73 → 74) — *"supersedes HANDOFF-23"*, *"Rulings in force (unchanged from
  HANDOFF-23)"*. `recovered/HANDOFF-23.md` is **chat 21 → 22**.
- `HANDOFF-26.md` (chat 74 → 75) — *"supersedes HANDOFF-25"*. `recovered/HANDOFF-25.md` is
  **chat 23 → 24**.
- `HANDOFF-32.md` is itself **pre-restart** (chat 30 → 31) and says *"RETIRE the BUILD-30 bundles and
  HANDOFF-31"*; `recovered/HANDOFF-31.md` is **chat 79 → 80**. This edge points the other way.
- `HANDOFF-45.md` (chat 92 → 93) — *"HANDOFF-44 printed DEFERRED.md as 86,899 B"* and *"HANDOFF-43
  mis-cited that and HANDOFF-44 corrected it"*. `recovered/HANDOFF-44.md` is **chat 42 → 43** and
  contains **zero** occurrences of `DEFERRED` or `86,899`; `HANDOFF-43.md` names neither W-118 nor
  W-107. The citation is checkable and it fails.

**Four numbers hold both documents — 7, 11, 15 and 53** — and that is the `__<md5>` convention §7
describes, doing work §7 did not know it was doing. `HANDOFF-53` is the corroboration: it carries
**four** files, two from chat 100 → 101 and two from chat 51 → 52, and 53 is exactly the top of the
pre-restart range.

The fifth edge, `HANDOFF-22 → HANDOFF-15__99520fa7`, is §2's `Ruling 28 ↔ Ruling 41` pair and it
crosses the same seam: `HANDOFF-15__99520fa7.md` is pre-restart and **names no Ruling 28 at all** —
its own rulings run to 27, and it states the absorption as *"PAPERS ABSORBED"* in prose. §2's reading
stands as written (it already says *"no sentence in the corpus names both rulings"*); what this adds
is why — the two numberings number their rulings differently too, and `RULINGS-R2.md` numbers its
rulings **per chat** ("Chat 74 … 1, 2, 3, 4") rather than globally.

#### The consequence for `HANDOFF-GAP.tsv`

That census resolves a bare-number citation by **filename**, and the filename space is doubly used.
One row is directly affected: `HANDOFF-33` is seated as `recovered/HANDOFF-33.md` with the title line
*"# THE METHOD 1.6 — HANDOFF (chat 31 → chat 32)"* — the **pre-restart** document, against a
post-restart citation. The other five numbers (23, 25, 32, 43, 44) never entered the gap file because
a file of that name already existed, so they count among its 62 *held*. **`HANDOFF-GAP.tsv` is not
wrong about what is on disk; it is wrong about which document answers the citation, at up to six
numbers.** Recorded, not repaired — the file is generated, and the generator would need the lineage
discriminator to do better. **The discriminator is free and already banked**: the chat pair in each
handoff's own first lines, or `recovered/LEDGER.tsv`'s `conversation` column.

### 12c. The six session-series edges — house style, and two shared registers

Six edges pair documents in the Löwdin/atomic-physics session run
(`FINDING-HFCORR-SESSION-37 ↔ FINDING-ONEFUNC-SESSION-28`, `FINDING-SO-SESSION-38 ↔
FINDING-HFTERM-SESSION-27`, `FINDING-T0a-SESSION-10 ↔ FINDING-HFTERM-SESSION-27`,
`PREDICTION-CELLCUT-SESSION-28 ↔ PREDICTION-CHAIN-LIGHT-SESSION-40`, `PREDICTION-S92-ITEM1-SP ↔
PREDICTION-S84-ITEM1-SEMICLASSICAL`, `PREDICTION-S82-ITEM4 ↔ PREDICTION-T-E`). **None of the six
names the other file.**

They resemble each other because the series has a house style. Of the **291** `PREDICTION-*` and
`FINDING-*` files in `recovered/`, **164 carry a pre-registration declaration** — *"FILED BEFORE
THE INSTRUMENT EXISTS"*, *"written BEFORE any code change or run"* — and smaller sets repeat *"no
constant beyond c"* (27), `RECALLED-NOT-ENTERED` (44) and *"Not a closure"* (25). A semantic
extractor reading two of these finds the same frame, the same disclaimers and the same vocabulary,
and cannot tell a relationship from a convention. **`AMBIGUOUS` is the correct grade and the reason
is the corpus's discipline, not the extractor's weakness.**

Two of the six do have a shared anchor, and it is a register neither file cites the other over:
`FINDING-HFCORR-SESSION-37` and `FINDING-ONEFUNC-SESSION-28` both cite **R 1578** (the
object-versus-observer seam); `FINDING-T0a-SESSION-10` and `FINDING-HFTERM-SESSION-27` both cite
**R 1449**. That is the same shape §11 named — *co-membership on a parent neither endpoint names* —
with a **Register entry** as the parent instead of a document. Across all 35 cross-document
`AMBIGUOUS` text edges, **7 share at least one register or ruling identifier and 28 share none**;
four of the seven are the handoff edges sharing the boilerplate `Ruling 41` paragraph, which is why
the handoff edges were drawn in the first place.

### 12d. The three remaining same-document edges

`recovered/BRIDGE-LOWDIN-SESSION-46.md` and `recovered/REQUEST-2-to-original-works-…md` each carry an
edge between two of their own concepts — an internal relation the extractor could see but not ground,
and the whole evidence is one file a reader can open. The third is this document: the graph drew an
`AMBIGUOUS` edge from **§4's `DEF-151d` finding to §7's `HANDOFF-26` divergence**, inside the file
that records both. Neither section claims a link to the other and none is claimed here.

### What the census says about the grade

`AMBIGUOUS` runs at **0.12 %** on text and **4.6 %** on images, and where it fires on text it fires
for four reasons, all of them real: co-membership on an unnamed parent (document or register entry),
a house style that makes unrelated documents read alike, an identifier space used twice, and a
genuine relation graded too low (§11's Q7, the only one). **Only one of the 120 turned out to be a
fault in the repository rather than a limit of a pairwise edge** — and the graph found it by doubting
a citation that a filename lookup accepts.

---

## Re-verification for §12

```bash
# the census: 120 AMBIGUOUS edges, and the image/text split
python3 - <<'EOF'
import json, collections
g=json.load(open('graphify-out/graph.json'))
a=[x for x in g['links'] if x.get('confidence')=='AMBIGUOUS']
img=[x for x in a if x.get('source_file','').lower().endswith(('.png','.jpg','.jpeg','.svg'))]
print(len(a), 'AMBIGUOUS;', len(img), 'from images;', len(a)-len(img), 'from text')
print(collections.Counter(x['relation'] for x in a).most_common())
EOF

# 12b: the two numberings, by each handoff's own chat pair
grep -h -o 'chat [0-9]* → [a-z ]*[0-9]*' recovered/HANDOFF-{23,24,25,26,31,32,43,44,45,53}.md

# 12b: the four files at number 53, two from each numbering
head -1 recovered/HANDOFF-53*.md

# 12b: the citation that fails
grep -c 'DEFERRED\|86,899' recovered/HANDOFF-44.md          # 0
grep -o 'HANDOFF-44[^.]*' recovered/HANDOFF-45.md | head -2

# 12b: the retired-unused steps
grep -o 'retired unused' recovered/HANDOFF-{26,34}.md

# 12b: the gap census row that seats the wrong lineage
awk -F'	' '$1=="HANDOFF-33"{print $1, $13, $14}' HANDOFF-GAP.tsv

# 12c: the house style, 164 of 291
grep -l -iE 'FILED BEFORE|WRITTEN BEFORE|before any (run|solve|number|row|code)'   recovered/PREDICTION-*.md recovered/FINDING-*.md | wc -l
```

---

## 13. `--update` is not usable on this repository, and the reason is provenance

**Deferred, not repaired.** Run on 2026-09-04 after six files changed; **nothing was written** — the
run was stopped before the graph write, `graph.json` came out byte-identical to its pre-run backup,
and `manifest.json` was restored because the merge step had already stamped the six as extracted
while the graph never took them.

The six were `CLAUDE.md`, `docs/DOCFIGURES.md`, `docs/GRAPH-FINDINGS.md`, `docs/HANDOFF-GAP.md`,
`docs/R3-REPAIR-PLAN.md` and `tools/docfigures.py` — 0.15 % of the 4,090 files the index covers, and
**nothing under `drive/`, `extracted/`, `recovered/` or `method/` had moved.** Extraction itself went
cleanly: AST gave 31 nodes and 67 edges for the one `.py`, and one agent gave **117 nodes, 163 edges,
3 hyperedges** for the five documents at 144,489 subagent tokens. The extraction is **in the semantic
cache**, so re-running costs no agent tokens; it is the *merge* that is the problem.

### What the merge does

```
[graphify] Replaced 63 node(s) from re-extracted source file(s).
[graphify] Deduplicated 354 node(s) (285 exact, 69 fuzzy).
old 26364 nodes -> merged 26095 nodes
```

**The merged graph is smaller than the one it merges into**, so graphify's own shrink guard (#479)
refuses the write and directs you to a full rebuild with `--force`. That guard is the second reason
to stop. The first is what the shrink is made of:

| | |
|---|---|
| old node ids absent from the merged graph | **377** |
| …of those, sourced from one of the six changed files | 24 |
| **…sourced from a file that did not change** | **353** |
| …of the 353, a node with an identical label survives elsewhere | 206 |
| **…of those, the survivor is in a different top-level tree** | **121** |

`build_merge` runs a repository-wide dedup as a side effect of an incremental update on six
documents, and it folds trees into each other:

```
extracted/…/transitions/Transitions.md  ->  drive/…/CORPUS/INTEGRATION-transitions.md
recovered/REGISTER_AUDIT.md             ->  method/members/REGISTER_AUDIT.md
drive/…/CORPUS/READ-ch16d.md            ->  method/members/READ-ch16d.md
drive/…/EXPANSION-MC54.md               ->  recovered/EXPANSION-MC54.md
```

### Why that is a defect here and not everywhere

**Those pairs are not duplicates in this repository.** `drive/` is the mirror of record and `method/`
is the store of record; `extracted/` and `recovered/` are generated trees carrying their own ledgers
and their own statuses, and `CLAUDE.md` states outright that **RECOVERED is not mirrored** — no
recovered file is claimed byte-identical to a copy held elsewhere, nor is any of it a member of a
bundle. Which tree a body sits in *is* the finding about it. Collapsing a mirrored copy into a seated
member is the same class of error as flattening `RECOVERED-BY-WRITE` to `RECOVERED`: it destroys a
distinction the corpus is built to keep.

So the trade the merge offers is **121 collapsed provenance distinctions across untouched files, to
seat 148 nodes about six documents.** That is why it was refused. A corpus with one source tree and
no provenance semantics would take this merge happily; this one cannot.

### The standing decision, and its discharge on 2026-09-11

The decision taken on 2026-09-04 was: **leave the graph at 26,364 and let those six documents describe
an earlier state of themselves.** The staleness was exactly known and bounded — five documents, plus
`docs/R3-REPAIR-PLAN.md`, which was in no node at all. The correct route to currency was a **full
rebuild** (`/graphify .`), which builds through `build_from_json` and never runs this merge-time dedup,
worth spending after a pass that moves the corpus rather than after six documents.

**That deferral is discharged.** The R4 leg moved the corpus, and on 2026-09-11 the full rebuild was
spent: **30,892 nodes, 42,459 edges, 3,240 communities** over 4,662 files. `docs/R3-REPAIR-PLAN.md`
now carries **8 nodes**, and the six documents describe their current state. The rebuild cost
**18.8M combined subagent tokens over 131 chunk runs** — far above the ~3.45M this section estimated,
and the estimate was not wrong so much as conditional: the 2026-09-04 figure was a *mostly-cached*
run, replaying 11,583 of its 15,345 semantic nodes from `graphify-out/cache/`, which was gitignored
and so never travelled with the repository. A rebuild in a fresh clone pays the whole semantic pass.
The cache is tracked from 2026-09-11, so the next rebuild resumes instead of starting cold; **that is
the defect this section's estimate concealed, and it is repaired rather than recorded** because it was
a gitignore rule and not a finding about the corpus.

**The prohibition itself is unchanged.** `--update` is still not usable here, for exactly the reason
given above, and **`--force` past the shrink guard is still forbidden**: forcing writes the 121
collapses, which is the thing being avoided. A discharged deferral is not a lifted rule.

Nothing here is a defect in graphify. It is a mismatch between a general-purpose dedup and a corpus
whose whole point is that the same text in two trees means two different things.

### Re-verification for §13

Reads only — it reproduces the merge in memory and writes nothing, so `graph.json` is untouched.
It needs the semantic cache warm; if it reports the cache cold, the extraction agent has to be
re-run first.

```python
# python3 -c with the graphify interpreter: $(cat graphify-out/.graphify_python)
import json, collections
from pathlib import Path
from graphify.detect import detect_incremental
from graphify.extract import extract
from graphify.cache import check_semantic_cache
from graphify.build import build_merge

ROOT = '/home/user/Claude-Method-Works'
SPEC = f'{ROOT}/.claude/skills/graphify/references/extraction-spec.md'

inc = detect_incremental(Path(ROOT))
changed = {f for fl in inc.get('new_files', {}).values() for f in fl}
code = [Path(f) for f in inc['new_files'].get('code', [])]
ast = extract(code, cache_root=Path(ROOT)) if code else {'nodes': [], 'edges': []}
docs = [f for c in ('document', 'paper', 'image') for f in inc['new_files'].get(c, [])]
sn, se, sh, uncached = check_semantic_cache(docs, root=ROOT, prompt_file=SPEC)
if uncached:
    raise SystemExit('semantic cache is cold -- re-run the extraction agent first')

seen = {n['id'] for n in ast['nodes']}
new = {'nodes': list(ast['nodes']) + [n for n in sn if n['id'] not in seen],
       'edges': ast['edges'] + se, 'hyperedges': sh,
       'input_tokens': 0, 'output_tokens': 0}

old = json.loads(Path('graphify-out/graph.json').read_text(encoding='utf-8'))
G = build_merge([new], graph_path='graphify-out/graph.json', prune_sources=None,
                root=ROOT, directed=False)
print(f'old {len(old["nodes"])} -> merged {G.number_of_nodes()}')

rel = {str(Path(f).relative_to(ROOT)) for f in changed}
osrc = {n['id']: (n.get('source_file') or '') for n in old['nodes']}
olab = {n['id']: n.get('label', '') for n in old['nodes']}
nid = set(G.nodes())
nlab = collections.defaultdict(list)
for n, d in G.nodes(data=True):
    nlab[(d.get('label') or '').lower()].append(d.get('source_file') or '')
tree = lambda p: p.split('/')[0]
gone = [g for g in osrc if g not in nid]
elsewhere = [g for g in gone if osrc[g] not in rel]
survives = [g for g in elsewhere if olab[g].lower() in nlab]
cross = [g for g in survives if tree(nlab[olab[g].lower()][0]) != tree(osrc[g])]
print(f'gone {len(gone)}: {len(gone) - len(elsewhere)} from changed files, '
      f'{len(elsewhere)} from unchanged; {len(survives)} have a same-label survivor, '
      f'{len(cross)} of those in a different tree')
```

Expected on the 2026-09-04 state: `old 26364 -> merged 26095` and
`gone 377: 24 from changed files, 353 from unchanged; 206 have a same-label survivor, 121 of those in
a different tree`.

---

## What is still open

- **`HANDOFF-26` governance divergence** (§7b) — two complete bodies, two incompatible rules for
  growing `RULINGS-R2.md` / `DEFERRED.md`. Unreconciled by design; the author's call.
- **`HANDOFF-13`, 9,463 B / md5 `a07ad36d…`** (§1) — ABSENT, fingerprint recorded.
- **`HANDOFF-34.md` lines 34–42** (§6) — ABSENT at the export boundary; not recoverable by re-running
  `recover.py`.
- **31 numbered Löwdin bridges** (§8) — ABSENT repo-wide.
- **Four post-restart handoffs — 23, 32, 43 and 44** (§12b) — ABSENT repo-wide; the files at those
  names are the pre-restart documents. Two more, **25 and 33**, are recorded as *retired unused* by
  the handoffs that superseded them, so they may never have existed as live documents at all.
- **Six documents the graph describes at an earlier state** (§13) — `--update` was run and refused;
  the currency costs a full rebuild, and the deferral is deliberate.

None of these is a defect to fix. Each is a recorded absence or an unresolved authorial question,
and this file exists so the next session starts from the measurement rather than re-deriving it.
