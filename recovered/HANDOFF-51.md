# HANDOFF-51 — The Method 1.6 — chat 98 → chat 99

- Written from **chat 98** for **chat 99**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD127 compendia** (= BUILD126 + W-137 + DEF-98 + six new members). Register **1 to 1792**
  (unchanged — no Register entry since the chat-67 hold). W-137 IS seated; chat 99 seats nothing at
  open and writes W-138 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked**, not after. Only a choice no file can settle reaches M. The chat-81 block below it sets the
  cadence and is unchanged.
- **Chapter 23 is closed.** Four reads, chats 95–98, main L6178–L6622. Chat 99 opens **Chapter 24**.
- **The chat-97 gate fault does not recur and must not be re-introduced.** Chat 98's `r2-ch14p` and
  `r2-ch14q` read the six volume **members** by name and reproduced at their own bank. **Never write
  an instrument that opens a `BUILDnnn` path** — the name changes every chat and the bundle comes to
  contain the instrument's own banked output.
- **Correcting a banked golden works, and chat 98 did it.** Two faults landed after `r2-ch14p` was
  banked; `r2-ch14p.out` was removed in a **delete-only** call and re-banked. `gate.py bank` refuses
  to overwrite, so that is the only route. The golden in BUILD127 is the corrected one
  (15,920 B · `fee8fd64`).
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based); the bundle numbers each line one higher because of its `<<<FILE:` header. Chat 98
  re-scanned §23.12–§23.15 and found HANDOFF-50's boundaries exact — which is not a reason to carry
  the next set. Re-scan.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard is
  **W-118 (chat 81)**, not W-107. The absorption is W-009 / W-059 / W-063 and Registers 1701–1724;
  three-body count claims resolve to Registers 489 and 507. Project knowledge holds BUILD12/BUILD53
  only — list it, never read those bundles. Retired handoffs are gone from Drive; never fetch or cite
  one. **Never add HANDOFF-NN.md as a member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–127. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch14p is chat 98's) and W-101…W-137 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**136,458 B · `1ad0d7c5` · 27 blocks**, chat 98's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 98. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD127_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. MEASURED cost of the gate in chat 98:
   ≈ 17 % of context, against chat 97's ≈ 25 % (which carried a third fetch).
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'4dceeceede860686704b4f07f793f5db'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD127_compendia_papers_audits.md'}
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
   **5,125,193 B · 4dceeceede860686704b4f07f793f5db · 63,510 lines**; **414 members extracted
   (2 + 412)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **27,710 B ·
   390c77236c459eda38ef94fc945c257c · 414 lines**; WORKING-REGISTER.md **696,698 B ·
   71f9745af1a6dc40c0f1f5c9152a7dd2 · 6,123 lines**, ends **W-137**; DEFERRED.md **136,458 B ·
   1ad0d7c5 · 27 blocks**; RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged); r2lib.py
   21,022 B · 580d2ea2 · 453 lines (unchanged); gate.py 9,377 B · a01ef15a; close.py 6,456 B ·
   98acae67; r2-tools.py 6,529 B · 4702f5f9; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py
   4262f7c5; minmax.py 26da1d78. If two `BUILD*_compendia` files are present after a close, pass
   `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch14p r2-ch14q` → two `OK` (chat 98's goldens:
   r2-ch14p.out 15,920 B · fee8fd64 · 167 lines; r2-ch14q.out 12,769 B · 88b2d69d · 115 lines). Both
   import the lifted r2lib and read members only; an AttributeError means the extraction seated a
   pre-lift r2lib and the chat stops.
8. `python3 /home/claude/members/gate.py cert 99` → writes `/home/claude/GATE-ch99.txt`, verdict PASS
   only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 98 did (do not repeat)

**§23.12–§23.15 is closed, and with it Chapter 23** — main **L6549–L6622, 74 lines, five headings**,
boundaries re-scanned and confirmed. **Eleven deviations, twenty verified, seven incidentals, one
census row closed** (row 1138, a C9 artefact — "never creates an interior peak" is §23.12's own
scoped rule). All of it is in `READ-ch14p.md` and `CENSUS-CLOSURES-ch14p.tsv`; **do not re-measure
any of it.**

**The four findings that carry furthest:**

- **14p-19 — the main volume and the Spectra Compendium disagree about the compendium's own rows.**
  §23.15's "ν reached" column: Al I *n*f 55.0 is exact; **Na I *n*s** is printed at 20.0 where its row
  reaches **18.7** (20.0 belongs to *n*d, *n*f, *n*g); **K I *n*d** is printed at **45.7** where the
  nd row reaches 12.7 and no K I channel passes 15.8. The K I row cannot be a sibling-channel slip,
  so at least one figure points outside the six volumes. **The first main-volume/compendium
  contradiction of the phase**; DEFERRED's chat-98 block sets the sweep.
- **14q-03 / 14q-04 — the ν_V docket closes.** No site in the six volumes gives Ga I a ν_V. §25.5
  L6976's 51.7 is a **ν**, read from its header at L6972 — the number sits beside Ga I and reads like
  a ceiling until the header is read. L6270 hands Ga I one of Al I's own failing cells: §23.15 lists
  **51 and 53 both** for Al I *n*f. L6270 and L6923 retarget from §23.11 to §23.15.
- **14p-03b — a reproducing column with an unprinted convention.** All four §23.12 Δ^(k+1)T rows come
  out of R/n² with the volumes' own R and no quantum defect, on **the m+1 levels nearest ν, ties
  broken downward**. The window is never stated. Tenth member of the unprinted-input class and the
  cheapest to repair; 14p-11 (the +0.86 Hill slope) and 14p-12 (the Kirkwood floor) are the eleventh
  and twelfth and are not cheap.
- **14p-17 — two figures that looked unsourced are sourced.** The 94 is Al I's usable cells over its
  four channels (50+30+11+3); the 55 is Li I's over its three undivided ones (39+8+8). **Grep the
  Spectra Compendium's channel table before recording any cell count as unsourced.**

**Eleven instrument faults, all self-caught and rewritten, none trimmed.** The three to carry are in
DEFERRED's chat-98 block; the shortest form is: **a negative result from a sweep is a statement about
the sweep** (a two-anchor sweep called a reproducing column unreproducible); **ν is not n** (41.8 is
the ν a series reaches, not its last principal quantum number); and **read the header, never the
neighbourhood**. Chat 97's note still bites: two of the eleven were verdicts contradicting numbers
the instrument printed **below** them.

## Chat 99's section read — Chapter 24, the collection

MEASURED by heading scan on the member: **Chapter 24 opens L6623 and runs to L6883; §25 opens
L6884.** Headings: 24 (6623), 24.1 (6634), 24.2 (6653), 24.3 (6668), 24.4 (6688), 24.5 (6699), 24.6
(6710), 24.7 (6725), 24.8 (6741), 24.9 (6752), 24.10 (6817), 24.11 (6826), 24.12 (6844), 24.13
(6857). **261 lines, fourteen headings — too large for one read.** **Re-scan before reading a line.**

**Proposed split, three reads** (chat 99 decides its own unit before reading, and may re-cut):

- **Chat 99: L6623–L6740 — §24 through §24.7**, 118 lines, eight headings, closing before the
  independence argument. Inside the 141-line ceiling.
- Chat 100: §24.8–§24.9, L6741–L6816 (76 lines) — §24.9 alone is 65 lines and is the chapter's
  longest.
- Chat 101: §24.10–§24.13, L6817–L6883 (67 lines), closing the chapter.

**What this unit owes, beyond the read itself:**

- **The census claim.** §24.12 is titled *The census, computed rather than searched* — outside chat
  99's proposed unit, but §24.1 *What it spans* and §24.2 *The largest contributors* will state spans
  and counts that the **Spectra Compendium's 477 channel rows** can settle exactly. After 14p-19,
  **every count and every ν attributed to a named species must be measured against that species'
  compendium rows**, not merely checked for internal consistency.
- **He I, He II and Bi I get their own sections** (§24.3–§24.5) and each will carry species-specific
  figures. The compendium's row format is
  `| species | channel | n range | members | usable | fit | ν range | δ̄ | spread | Z | limit |` —
  columns 4 and 5 are members and usable, column 7 is the ν range. Chat 98's 14p-17 and 14p-19 both
  came out of those columns.
- **§24.7 "Hydrogen, and a floor on interpretation"** will make a claim about the δ = 0 case that the
  tower can test directly.
- **L6634 is one of the four heading-runs-into-body sites** (14q-06) and sits at the head of this
  unit; it is a table header rather than a sentence, so read it before assuming it is the same defect
  as §23.14's.

Instruments: **r2-ch14r** (computable) and **r2-ch14s** (prose). Import `heading_line`,
`section_span`, `has_token` and `enclosing` from r2lib by path; **copy nothing**; **read members,
never a bundle**. Six functions are still owed to r2lib and DEFERRED lists them; note that
`heading_line` requires a trailing space after the number, so the Register's bare `### 96` headings
return None — locate Register entries with an explicit `^#{1,4}\s*N\s*$` match.

**Standing method, unchanged and all of it earned:** use the exact-token heading resolver, never
prefix matching; never span a section by heading rank; **r2lib's resolvers take the LINE LIST, not
the member text** (chat 98's first fault). Grep lowercase `register NNN` by hand. Check every printed
pair count against C(N, 2). Resolve every pointer to the claim and not the heading, and before
recording any pointer as unresolved **read the target section and test for the claim as that section
words it**, case-exact and word-bounded — and if it fails there, grep the whole volume before
recording it. Give every negative claim its own witness. **State what a sweep covered before
recording a negative from it.** Check the arithmetic of every ratio and percentage; **never round
with `round()`** — use `Decimal.quantize` and name the convention; convert exact Fractions
numerator/denominator. A formula numerator is not a value; a citation is not a declaration; a heading
is not a statement; a bound is not a measurement; a boundary case is not a violation; **a number
beside a species is not that species' ceiling** — read the header. Where the text prints a sample,
measure the population — the Spectra Compendium usually holds it. Grep the Register for a later entry
naming the section before recording any figure as unreproducible. **When an instrument disagrees with
a hand reading already taken from the file, the instrument is wrong until proved otherwise** — chat
94 hit that twice, chat 95 four times, chat 96 three, chat 97 twice, chat 98 twice.

## The repair docket

Carried forward until R3 executes it. **None of these goes to M.** Chat 98's additions are in
DEFERRED's chat-98 block in full; the docket below is the standing list.

1. **§14.5.2–§14.5.7 — six heading-only sections, forty citations. R3's largest single item.**
   MEASURED against the Prints & Proofs original (738,550 B · md5 49900cf41f818ab789bb90fc596ac977):
   **authoring gap, not production loss.** Citations: §14.5.2 → 4, §14.5.3 → 1, §14.5.4 → 4,
   §14.5.5 → 4, §14.5.6 → 3, **§14.5.7 → 24**. **Order:** read the Register's nine §14.5.7 citations
   first and author to what they already say, then §21.5.4, then the Mathematical Compendium's
   twelve. Chat 90's **seed(Λ₈) = 7** is the settled material §14.5.7 owes.
2. **The §18.4.1 one-dimensional refinement — a missing Register entry** (main L5977–L5980).
   Register 319, which the passage cites, states a different claim.
3. **The Register has no entry for the correction §23.10.2 cites** (14n-A3) — a second missing entry,
   written when the chat-67 hold lifts, and interacting with 5 below.
4. **The σ collision — flagged for correction.** Rule 4 (main L6047) defines σ = 2R Z_eff² ·
   SE_pred / ν³; §22.5 (L6168) uses σ as the levels' measured uncertainty, and substituting Rule 4's
   σ into §22.5's r = 2Z²R/(ν³σ) cancels ν³ identically — MEASURED r = 100.000000 at ν = 10, 20, 40,
   80.
5. **The Ruling 45 class inside Chapter 23** (14n-A12) — L6453 *An earlier draft claimed…* and the
   Figure 23.3 caption at L6483–L6484 *withdrawn at correction 97*. Captions state facts only.
6. **§23.8.3's affine-invariance reason** (chat 96's 14l-16) — the docket's only *reason* item. R3
   must decide which invariance the chapter claims before rewriting, and check §29.2 L7881, §29.7
   L8052 and App D.4.1 L10377 for the same reasoning.
7. **The §25.6 pointer with no target** (chat 96's 14m-01) — author the explanation or drop the
   clause; the clause is load-bearing for the novelty claim beside it.
8. **The pointer-off-by-one class, now eight members and never yet swept as a class** — 14n-A1,
   14n-A2, 14n-A7, chat 95's 14k-01, chat 96's 14m-01, and chat 98's 14q-02, 14q-03, 14q-04. R3
   sweeps **every §-pointer in the six volumes against the claim rather than the heading**;
   `enclosing` makes the test cheap.
9. **The unprinted-input class, now twelve members** — §22.1.2's δ = 0.35; §22.4.1's δ₂ = 0.06;
   L6060's 446×, L6068's 1,577, L6093's 3.47 %, L6104's *factor of 17*; §23.1 L6189's *agreement
   under 1 %*; §23.9.3's two columns; §23.10.3's displacement row; and chat 98's **§23.12 window**
   (a convention, cheap), **+0.86 Hill slope** and **Kirkwood detection floor** (both absent data).
   R3 should split the class into *conventions unstated* and *inputs absent*.
10. **The 32/11 scope docket** (14j-01), with six measured main-volume sites — L6193, L6213, L6233,
    L6237, L6381, L10245 — plus 2.909 at four. L6381 claims the floor as an original result and must
    be repaired **after** the scope decision, not with it.
11. **The truncation-printed-as-equality class** (14l-02, 14l-03, 14n-A10) — sweep every display
    equation whose own table disagrees with it, and every site printing 4ν/3.
12. **The two unsourced counts of L6517** (14n-A6, 14n-A7) — *619 refusals* and *§25.5's 1,061
    order-1 bounds*. Neither can be repaired without **recomputing the collection at matched order**;
    the phase's first item needing a recomputation rather than a corrected figure. **Note chat 98's
    14p-17**: two counts that looked unsourced were recovered from the Spectra Compendium's channel
    table, so try that table before scheduling the recomputation.
13. **The main-volume/Spectra contradiction class** (14p-19) — new, and the sweep is stated in
    DEFERRED's chat-98 block: every figure the main volume attributes to a named channel, against
    that channel's compendium row. Resolve **K I *n*d 45.7** first; it decides whether the class is a
    table defect or a short compendium.
14. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one substantive (L8052
    credits Nesterov alone for a result §23.8.1 credits to both).
15. **The single-witness class** — six of twelve distinctive figures in chat 98's 74 lines, fourteen
    in chat 97's 115, seventeen in chat 96's 131, thirteen in chat 95's 125. R4 should state which
    figures are unverifiable rather than leaving them looking checked, and distinguish *unverifiable*
    from *uncorroborated*.
16. **Heading sentences finishing in the body** (14q-06) — L4407, L6582, L6634, L8659. Read all four
    before repairing any; L6634 is a table header, not a sentence.

## Close (chat 99)

`gate.py bank r2-ch14r r2-ch14s`; delete pycache in its own delete-only call; write `W-138.md`
(begins `### W-`, **ends with a blank line** — close.py asserts this); append a DEFERRED block as
`DEF-99.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD127_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD128_compendia_papers_audits.md --w W-138.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-99.md \
  --members members/READ-ch14r.md members/CENSUS-CLOSURES-ch14r.tsv members/r2-ch14r.py \
  members/r2-ch14r.out members/r2-ch14s.py members/r2-ch14s.out
```

It must print **reverse recovers md5 4dceeceede860686704b4f07f793f5db == old: True** before writing;
if it does not, nothing is written and the failure is reported. `--append` arguments must precede
`--members`, and `--members` may be omitted entirely if nothing new is seated. **A changed
append-only member is grown with `--append <member> <delta-file>`, never passed to `--members`** —
close.py refuses a name collision, and a member needing *replacement* rather than growth has no
mechanism at all. After a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state; **verify appends by reading the new bundle directly** —
and note the Register member lives in the **main** bundle, not the compendia bundle. `gate.py bank`
refuses to overwrite an existing `.out`; correcting an instrument after banking needs a
**delete-only** call to remove the golden, then bank again (chat 98 did this and it works). Then copy
BUILD128, HANDOFF-52 and the READ file to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-51.md` and
  `The_Method_1_6_BUILD127_compendia_papers_audits.md`.
- **Retire** once BUILD127 gates PASS in chat 99: HANDOFF-50 and BUILD126, plus any earlier compendia
  builds still present (BUILD107–BUILD125).
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Chat 98 read those values out
  of the **member** rather than re-running the instrument, which is the pattern R3 should adopt
  before BUILD124 is retired.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 — the
  certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 99

"Chat 99. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD127 compendia (5,125,193 B, md5
4dceeceede860686704b4f07f793f5db, 63,510 lines, 412 members). List uploads, outputs and /home/claude
first. Run HANDOFF-51's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 414 files), then gate.py census, run --core, manifest, run r2-ch14p
r2-ch14q, cert 99; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 98's block is the last of
twenty-seven. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state;
discard it per Ruling 41 — its discard is W-118, not W-107. Line numbers are MEMBER line numbers and
are never carried between chats, and neither is any count: re-scan every heading on
The_Method_1_6-2.md before reading a line. Chapter 23 closed in chat 98. Then continue Phase R2 under
the chat-81 cadence: Chapter 24 runs L6623–L6883, fourteen headings, too large for one read — take
§24 through §24.7, main L6623–L6740, 118 lines, eight headings, and decide the cut before reading.
Read it all, census its claims into computable and prose, then run exactly two instrument batches,
r2-ch14r computable and r2-ch14s prose, importing heading_line, section_span, has_token and enclosing
from r2lib — copy nothing, pass them the LINE LIST and not the member text, and read the six volume
MEMBERS, never a BUILDnnn bundle path. Chat 98 measured that the Spectra Compendium's channel table
(477 rows: species, channel, n range, members, usable, fit, ν range, δ̄, spread, Z, limit) settles
cell counts and ν ranges exactly, and that §23.15's ν-reached column disagrees with it in two of
three rows — so measure every count and every ν this chapter attributes to a named species against
that species' compendium rows, and resolve K I nd 45.7 if the chapter touches it. Where the text
prints a sample, measure the population. Use the exact-token heading resolver, never prefix matching,
and never span a section by heading rank. Grep lowercase 'register NNN' by hand. Resolve every
pointer to the claim and not the heading, and if it fails at the named target grep the whole volume
before recording it. Give every negative claim its own witness, and state what a sweep covered before
recording a negative from it. A number beside a species is not that species' ceiling — read the
header. ν is not n. Never round with Python's round() — use Decimal.quantize and name the convention.
A heading is not a statement, a bound is not a measurement, a boundary case is not a violation.
Re-read every verdict against the numbers printed above it AND below it. When an instrument disagrees
with a hand reading, suspect the instrument first. Close the section read before the next opens. At
close: bank both goldens with gate.py bank, write W-138 ending with a blank line, build BUILD128 with
close.py (reverse must recover 4dceecee…), write HANDOFF-52. A changed append-only member is grown
with --append, never --members; correcting a banked golden needs a delete-only call first. No
corrections, no Register entries, no TASK 1 until the review closes. Handoff at 90–95 % of context or
on a closed section read — never earlier, never mid-section. Timeout on every call. Delete-only calls
for pycache, never chained to gate.py bank. Never copy over an existing file."
