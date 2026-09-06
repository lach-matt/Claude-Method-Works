# HANDOFF-40 — The Method 1.6 — chat 87 → chat 88

- Written from **chat 87** for **chat 88**. Live files: **BUILD90 main** (unchanged since chat 62) and
  **BUILD115 compendia** (= BUILD114 + W-125 + chat 87's DEFERRED block + six new members). Register
  **1 to 1792** (unchanged). W-125 IS seated; chat 88 seats nothing at open and writes W-126 at close.
- **Rulings and discipline:** the member `RULINGS-R2.md` (6,041 B · 30 lines, unchanged this chat)
  governs and is append-only; **read it at open, last block first** — the chat-81 block sets the
  cadence, and chats 82–87 have now all run it. **Deferred cross-chapter items:** `DEFERRED.md`
  (**69,014 B · 234 lines**, with chat 87's block) governs; do not re-derive. **Findings carried to
  R3:** the READ-chNN.md members (READ-ch13t is chat 87's) and W-101…W-125 in WORKING-REGISTER.md;
  nothing is restated here.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4" Löwdin/three-body
  plan is executed carried state (MEASURED in W-107, re-confirmed in chats 75–87); do not re-open it
  or put it to M. Its **residue** is live: 13p-04's second site was confirmed at main L5192 this chat,
  and every extent-like count still owes a post-absorption sweep before R3 closes. Project knowledge
  holds BUILD12/BUILD53 only — list it, never read those bundles. Retired handoffs are gone from
  Drive; never fetch or cite one. Never add HANDOFF-NN.md as a member.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 87. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD115_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths (the gate cost ≈ 13 % of chat 87, MEASURED).
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'7cbc33157f4d5b895626de71446fe337'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD115_compendia_papers_audits.md'}
SPILL={'main':'/mnt/user-data/tool_results/<main-id>.json','comp':'/mnt/user-data/tool_results/<comp-id>.json'}
for tag in ('main','comp'):
    b=base64.b64decode(json.loads(json.load(open(SPILL[tag]))[0]['text'])['content'], validate=True)
    m=hashlib.md5(b).hexdigest(); print(tag, f'{len(b):,} B', m, b.count(b'\n'), 'lines', 'OK' if m==EXP[tag] else 'FAIL'); assert m==EXP[tag]
    assert not os.path.exists(NAME[tag]); open(NAME[tag],'wb').write(b)
os.makedirs('/home/claude/members'); n=0
for tag in NAME:
    for m in re.finditer(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', open(NAME[tag],'rb').read(), re.S|re.M):
        p='/home/claude/members/'+m.group(1).decode(); assert not os.path.exists(p); open(p,'wb').write(m.group(2)); n+=1
print('members extracted', n)
EOF
```

   Expected: main 1,983,081 B · 49065309b0c4fe8e055f693aed295cca · 18,470 lines; compendia
   **4,240,326 B · 7cbc33157f4d5b895626de71446fe337 · 50,510 lines**; **348 members extracted (2 + 346)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`.
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/
   199,130, kinds 1565 · 1356 · 499 · 149, minmax, r2-tools-constants, extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK: 347 members listed, 348 files
   extracted`; MANIFEST.tsv **23,285 B · d9d7679fea024a733166e48848ac8f25 · 348 lines**;
   WORKING-REGISTER.md **627,622 B · 11b13caab480bcaf6a08dce57ad53c11 · 5,313 lines**, ends W-125;
   DEFERRED.md **69,014 B · dd52c437 · 234 lines**; RULINGS-R2.md 6,041 B · 4cce8039;
   **r2lib.py 18,486 B · 3344ca87 · 396 lines** (unchanged this chat); gate.py 9,377 B · a01ef15a…;
   close.py 6,456 B · 98acae67…; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5;
   minmax.py 26da1d78; r2-tools.py 4702f5f9. If two `BUILD*_compendia` files are present after a
   close, pass `--comp <path>`.
7. `python3 /home/claude/members/gate.py run r2-ch13t r2-ch13u` (chat 87's instruments: ≈ 81 s and
   ≈ 1 s — one call). r2-ch13r ≈ 9 s, r2-ch13s ≈ 1 s, r2-ch13p ≈ 116 s, r2-ch13q ≈ 1 s,
   r2-ch13n ≈ 8 s, r2-ch13o ≈ 1 s, r2-ch13l ≈ 7 s, r2-ch13j ≈ 60 s, r2-ch13k ≈ 2 s, r2-ch13h ≈ 38 s,
   r2-ch13e ≈ 30 s, r2-ch12t ≈ 44 s, r2-ch12r ≈ 25 s, r2-ch12y ≈ 30 s, r2-ch12n ≈ 60 s,
   r2-ch12m ≈ 150 s — run these only when their figures are in question. `run --all` exceeds one 280 s call.
8. `python3 /home/claude/members/gate.py cert 88` → `GATE-ch88 … verdict PASS`. Shell is dash: text
   through python heredocs or create_file; no `<(…)`; one heredoc per bash call; non-ASCII grep output
   through python. Remove `members/__pycache__` in a **delete-only** call (G0e) after every instrument run.

## Next work — Phase R2, the section read: Chapter 19 whole

**The cadence holds for a sixth chat.** Chat 87 read Chapter 18 whole (459 lines, sixteen sections)
in four `lines` calls after a heading scan, censused eighteen computable and fourteen prose claims,
ran exactly two batches, and closed eleven deviations, fourteen verified findings, eight incidentals
and sixteen census rows. Keep the shape: verify the boundaries by a heading scan, read the whole
section in one or a few `lines` calls, census the claims in two kinds, write one instrument for each,
bank both, write one READ file and one CENSUS-CLOSURES file.

**The section read is Chapter 19 whole, main L5381 onward** — sections MEASURED by heading scan in
chat 87 only as far as **§19.1 The formalisation (L5386)** and **§19.5.1 (L5443, *ρ is a property of
(document, route), and this chapter collapsed the second index*)**. The chapter's end was **not**
measured; **scan for Chapter 20's opening before reading, and verify every boundary, every time.**
HANDOFF-34's L4157, HANDOFF-36's L4477, HANDOFF-38's L4899 and HANDOFF-39's eight-section Chapter 18
were all wrong — chat 87's scan found **eight sections HANDOFF-39 had not listed**, and the chapter
ran 459 lines rather than the ~80 implied. Four consecutive handoffs have mis-stated a chapter's
extent; assume nothing about this one.

**What chat 88's batches already have waiting.** Chapter 18 sends **depth** to Chapter 19 twice —
L4977–4978, *"The number of measured members in a channel is not a function of the coordinates at
all. It is a property of the literature, and Chapter 19 makes that precise"* — and §18.6.1's
bibliography row indexes on **retrieval redundancy ρ**, which §19.5.1 says this chapter *collapsed*.
Read §19.5.1 against §18.6.1's L5325 (twenty-two sources over seven cells, admitting six, E falling
6 → 2 under 5,184 relabellings) and against §16.7.1. The **bibliography catalogue is owed to r2lib**
and Chapter 19 is where it becomes unavoidable — three chats have now deferred it.

**Patterns chats 77–87 established, to watch for:** a running self-count printed several ways in one
chapter (13j-11, 13p-03, 13p-09, **13t-03**, **13t-10**); a class minimum or a sample printed as a
population (13j-01, 13p-01) and its inverse, a population-shaped figure printed as a sample (13r-01)
— check every pair count against C(N, 2), this volume's convention, now verified exact at five sites;
a figure left stale by an earlier absorption (13p-04, confirmed at its second site **13t-11**); a
section attributing a proof, table, count, rule or constraint form to a neighbour that does not
contain it (13d-01, 13h-01, 13i-04, 13j-08, 13l-03, 13l-05, 13o-01, 13p-06, 13r-05, 13r-06,
**13t-08**); a claim true while the statement printed for it is false (13g-01, 13h-04, 13j-01,
13l-01, 13n-01, 13p-02, 13r-03, **13t-04**); a figure printed with its population or its defining
term unstated (13j-07, 13l-06, 13l-09, 13n-02, 13o-03, 13p-11, 13p-13, 13r-08, 13r-09, **13t-05**,
**13t-07**); a section contradicting its own adjacent table (13p-10, 13r-01, **13t-02**); a promise
with no referent (13r-04); and **new this chat, a label pointing at nothing** — a theorem, object or
section number cited by name that occurs nowhere in the six volumes (**13t-01**, **13t-06**). Resolve
every pointer to the claim, never to the heading; check the arithmetic of every ratio, percentage and
pair count as well as every count; measure a claim and its stated witness separately; and where the
text prints a sample, measure the population. **Chat 85's C9 is the standing warning against letting
a display artefact become a finding** — 13t-06 stops short of an impossibility claim for exactly that
reason. Measure from the file (G0aa, G0c).

**Per section read (close it — files written, md5s measured, both goldens banked — before the next
opens):** `python3 members/r2-tools.py lines|pointers|figures|census|layout A B` over the whole
section (its pointer regex is case-sensitive and does not know Appendix A's item numbers or Chapter
4's protocol rows — a bare `§4.6` or `A.2` reported UNRESOLVED is usually one of those, not a defect,
and L5011 is now its third site; and a `§N` inside a quoted external citation is an artefact, not a
pointer). **Its heading resolver reads the front-matter contents list**, so a chapter pointer
resolves to L120–L172 rather than the body; take the later match — chat 87's r2-ch13u carries the
two-line fix. Read every line; census the claims into the two kinds, writing the census into the READ
file; then the two batches in `members/r2-chNN.py` (next names **r2-ch13v** computable, **r2-ch13w**
prose), importing r2lib by path:

```
import importlib.util, os; H=os.path.dirname(os.path.abspath(__file__))
s=importlib.util.spec_from_file_location('r2lib', os.path.join(H,'r2lib.py')); r2lib=importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T=r2lib.load_tower()
```

**`load_tower()` returns the tower-2 MODULE — call `T.L8()`, `T.L9()`, `T.L10()`, not `T[8]`.** r2lib
carries build9/tarjan/analyse, is_tree, closure/factor_q/ci/components/separates, support/direct/
composed, mi/ci_sets/gG_index, lam9p, read_member, md5, the Λ₉/Λ₉′ and (g, G) constants, `Rset`,
`cover_model`, `cover_reduce`, `exact_seed`, `enum_min_covers`, `closure_mask`, `staircase`, and
**`L8_at(caps)`** — the tower at arbitrary caps, caps = (n_max, e_max, l_max, k_max, f_max);
(3,3,1,3,1) → 976, (3,3,1,4,1) → 1,636, (4,3,1,4,1) → 2,394. Still owed, to be lifted verbatim with
provenance when a batch next needs them (DEFERRED lists them): r2-ch12c/e/g/h's functions; chat 75's
`closure_chunked`, `fixed_point`, `length`, `fibre_check`, `criterion`; chat 76's `terms`,
`new_terms`, `jc_values`, `TERMS`, `phi_at`; chat 77's stage-composability sets; chat 78's
`first_fail` / `failing_pairs` (r2lib.closure counts **ordered** pairs including self, so halve for
the unordered counts the book prints); chat 79's `sections(X, w)` and `R(X)` / `failing(X, op)`;
chat 80's `Rn(X)` and r2-ch13f's interval Box/binding measure; chat 84's numeric-Jacobian + pivoted
`rank` pair, the Slater-determinant term engine and the alphabet sweep; chat 85's `therm`/`untherm`,
`lat_closure`, `Rtree` and `pushback`; and **new, chat 87's `viol`, `failcount` and `parts`**.

**The two tools chat 87 adds.** **`viol(X, h, axes)`** reports a function's non-monotonicity under
five readings at once — comparable pairs, covering pairs, unit steps, join-homomorphism failures, and
the projection over realised value tuples — which is what let 13t-04 be stated as *no reading
reproduces the printed figure* rather than *one reading does not*. Use it for every "N violations"
figure in the volume. **`parts(n, N)`** enumerates partitions of s ≤ N into at most n parts, which is
the cell set behind §18.4.2's whole table; the printed reading of an unstated cell set is usually
findable by sweeping two or three natural readings and taking the one that reproduces every row, as
it did for §18.4.1's cap table (6 of 6 at side 4, 0-based) and §18.4.1's fibre table (5 of 5 on the
364 non-increasing triples over 1…12).

**Chat 86's reduction still holds and is still the cheapest tool in the box.** For any h that is a
function of coordinates (i, j), the (i, j) part of a join is (max, max) and of a meet is (min, min),
so quantifying over the **realised value pairs of the projection of Λ onto (i, j)** is exhaustive
over all cell pairs at ≤ 256 tests instead of 475,800. Chat 87 extended it to a closure proof: Λ₁₁'s
13,585 cells were shown closed by testing that all **110** φ̂ bounds are monotone on their realised
values, where the direct pairwise measure needs 92.3 M pairs. **A prefix of a lattice is not a
sublattice** — chat 87's first draft used one as a control and it was meaningless; control a reduction
against an object whose answer is independently known (Λ₁₀ served).

The tower's sides, for any width: A = (n, ℓ, k, 2S, 2J_c, 2K, 2J) at indices 0,1,2,7,10,11,12;
B = (e, f, g, 2S′, v) at 4,5,6,8,9; the base q at 3. At Λ₈ the eight coordinates are
(n, ℓ, k, q, e, f, g, 2S) in that order, with min (1,0,1,0,1,0,0,0) and max (3,1,3,3,3,1,3,3) —
MEASURED, chat 82. Λ₈'s alphabet sizes are (3,2,3,4,3,2,4,4), product **6,912**, so **5,936** cells
of the ambient box lie outside it, and none may be added while keeping closure (MEASURED, chat 86).
Its undirected constraint graph is the tree n–ℓ–k–q–g–f–e with 2S hanging off k; its directed
dependency graph is not a tree — g has two parents, q and f — and the descendants counts the book
uses are the directed ones (0, 0, 0, 1, 1, 3, 4). Λ₈ is a sublattice of its box, distributive, and has
exactly 18 join-irreducible and 18 meet-irreducible cells with empty intersection. Its seven
constraints, split as the Index of Indices lists them: ℓ ≤ n−1, k ≤ 4ℓ+2, q ≤ k, 2S ≤ k, f ≤ e−1,
g ≤ 4f+2, g ≤ q. **§7.1 L1750–L1763 is the table of them; §7.2 L1764–1766 is the section that says
every one is single-argument** (13t-08).

Write READ-chNN.md (the claim census first, then A deviations with both texts, B verified, C
incidental) and CENSUS-CLOSURES-chNN.tsv (id, verdict, reason; A vocabulary; header only when no row
is in range — chat 87 closed rows 701 and 1106–1121, none a defect; row **1122** is the next in range
and falls beyond L5380). Instruments print no wall-clock time (time a run in the shell with
`date +%s` if needed). **A batch over ~200 s is split into two instruments, never trimmed of
coverage** — and a re-encoding or a projection reduction is usually cheaper than a split. Never build
a set inside a per-cell comprehension; never allocate a lookup table indexed by a 32-bit code (it
needs 31.9 GiB — use the mixed-radix index of size 16,384); prefer the box sweep (`Rset`) over the
pairwise fixed point (`Rn`) above ~2,000 cells; and the exact set-cover solver is cheap after
reduction but does **not** close on 4⁵, 4⁶ or 3⁶.

## Close of chat 88

1. `rm -rf /home/claude/members/__pycache__` (delete-only call); `python3 members/gate.py bank r2-ch13v`
   … for each new instrument (writes NAME.out; refuses to overwrite), then a **separate** delete-only
   pycache call.
2. Write /home/claude/W-126.md: begins `### W-126 —`, ends with a blank line; records the gate, the
   section read, findings, what was not done, the close estimate.
3. `python3 members/close.py --old /home/claude/The_Method_1_6_BUILD115_compendia_papers_audits.md --new
   /home/claude/The_Method_1_6_BUILD116_compendia_papers_audits.md --w /home/claude/W-126.md
   [--append DEFERRED.md /home/claude/deferred-add.md] --members members/READ-ch13v.md
   members/CENSUS-CLOSURES-ch13v.tsv members/r2-ch13v.py members/r2-ch13v.out members/r2-ch13w.py
   members/r2-ch13w.out` — every `--append` must precede `--members` (which consumes every later
   argument); `--append` may be given more than once. It must print `reverse recovers md5
   7cbc33157f4d5b895626de71446fe337  == old: True` before writing. Never edit a seated member in place.
   close.py rewrites the bundle only — the extracted `/home/claude/members/` copies stay at their
   pre-close state, so `gate.py manifest` reports FAIL on exactly the changed members after a close;
   verify appends by reading the new bundle, and **print only the fields you need**.
4. HANDOFF-41 in this form (update: build numbers, md5s, MANIFEST.tsv, WORKING-REGISTER.md, DEFERRED.md,
   the member count, the run list, next work, the prompt). `ls -la /mnt/user-data/outputs` before
   copying; never copy over an existing file; present HANDOFF-41.md first, then BUILD116 and the READ file.
5. Handoff at 90–95 % of context or on a closed section read — never earlier, never mid-section. Begin
   the close when the remaining context would not fit a section read plus the close (a section read
   ≈ 30–45 %, the close ≈ 12 %, MEASURED in chats 82–87). No corrections, no Register entries,
   no TASK 1 until the review closes.

## M's Drive actions

- **UPLOAD** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-40.md` and
  `The_Method_1_6_BUILD115_compendia_papers_audits.md` (7cbc3315…).
- **RETIRE:** HANDOFF-39 and BUILD114 once BUILD115 gates in chat 88; HANDOFF-38 and BUILD113 if still
  present; HANDOFF-37, HANDOFF-36, HANDOFF-35, BUILD112, BUILD111, BUILD110 and any earlier compendia builds.
- **KEEP:** BUILD90 main, tower-2.py, chat65/66/67-instruments.tar.gz, SWEEP-B-C-chat67.md, convert.py,
  the certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 88

"Chat 88. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD115 compendia (4,240,326 B, md5
7cbc33157f4d5b895626de71446fe337, 50,510 lines, 346 members). List uploads, outputs and /home/claude
first. Run HANDOFF-40's §0 gate in full and in order — fetch both bundles by title, bootstrap (decode,
md5, extract, expect 348 files), then gate.py census, run --core, manifest, run r2-ch13t r2-ch13u, cert
88; any FAIL stops the chat with a report. Read RULINGS-R2.md and DEFERRED.md from the members; chat
87's DEFERRED block is the last one. The standing block's Phase 0–4 (Löwdin/three-body) plan is
executed carried state; discard it per Ruling 41, but its residue in the reader-facing figures is live.
Then continue Phase R2 under the chat-81 cadence: the section read is Chapter 19 whole, main L5381
onward, with §19.1 at L5386 and §19.5.1 at L5443 — those are the only two boundaries measured, so scan
the whole chapter's headings and find Chapter 20's opening before reading a line, because four
handoffs in a row have mis-stated a chapter's extent and chat 87 found eight sections HANDOFF-39 had
not listed. Read it all, census its claims into computable and prose, then run exactly two instrument
batches, r2-ch13v computable and r2-ch13w prose. Read §19.5.1's collapse of the second index against
§18.6.1's bibliography row at L5325 — twenty-two sources over seven cells, admitting six, E falling
6 → 2 under 5,184 relabellings — and against §16.7.1; the bibliography catalogue is owed to r2lib and
Chapter 19 is where it becomes unavoidable. Use chat 87's viol() for any 'N violations' figure: five
readings at once, which is how §18.2's 86 was shown to reproduce under none of them. Use chat 86's
projection reduction — for h a function of coordinates (i, j) the join's (i, j) part is (max, max) and
the meet's is (min, min) — and remember a prefix of a lattice is not a sublattice, so control a
reduction against an object whose answer is independently known. Check every printed pair count
against C(N, 2), this volume's convention, verified exact at five sites. Resolve every pointer to the
claim and not the heading, and note that r2-tools' resolver reads the front-matter contents list, so
take the later match. Measure a claim and its stated witness separately, check the arithmetic of every
ratio and percentage as well as every count, where the text prints a sample measure the population,
and where a theorem or object is cited by name, check it exists. Close the section read before the
next opens. At close: bank both goldens with gate.py bank, write W-126, build BUILD116 with close.py
(reverse must recover 7cbc3315…), write HANDOFF-41. No corrections, no Register entries, no TASK 1
until the review closes. Handoff at 90–95 % of context or on a closed section read — never earlier,
never mid-section. Timeout on every call. Delete-only calls for pycache, never chained to gate.py
bank. Never copy over an existing file."
