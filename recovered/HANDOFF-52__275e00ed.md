# HANDOFF-52 — The Method 1.6 — chat 99 → chat 100

- Written from **chat 99** for **chat 100**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD128 compendia** (= BUILD127 + W-138 + DEF-99 + six new members). Register **1 to 1792**
  (unchanged — no Register entry since the chat-67 hold). W-138 IS seated; chat 100 seats nothing at
  open and writes W-139 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked.** Only a choice no file can settle reaches M. The chat-81 cadence below it is unchanged.
- **Chapter 23 is closed** (chats 95–98). **Chapter 24 is open**: chat 99 read §24–§24.7, main
  L6623–L6740. Chat 100 takes **§24.8–§24.9, L6741–L6816**.
- **Never write an instrument that opens a `BUILDnnn` path** — the name changes every chat and the
  bundle comes to contain the instrument's own banked output. Chat 99's `r2-ch14r` and `r2-ch14s`
  read the six volume **members** by name and reproduced at their own bank.
- **Correcting a banked golden works**: `gate.py bank` refuses to overwrite, so remove the `.out` in a
  **delete-only** call and bank again (chat 98 exercised it; chat 99 did not need it).
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based); the bundle numbers each line one higher because of its `<<<FILE:` header. Chat 99
  re-scanned Chapter 24 and found HANDOFF-51's boundaries exact — **which is not a reason to carry
  the next set. Re-scan.**
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard is
  **W-118 (chat 81)**, not W-107. The absorption is W-009 / W-059 / W-063 and Registers 1701–1724.
  Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles. Retired handoffs
  are gone from Drive; never fetch or cite one. **Never add HANDOFF-NN.md as a member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–128. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch14r is chat 99's) and W-101…W-138 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**143,252 B · `fadbe4ef` · 28 blocks**, chat 99's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 99. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD128_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. MEASURED gate cost in chat 99: ≈ 17 %.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'f2b9893f2f4483b07e5981ed3159f73e'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD128_compendia_papers_audits.md'}
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
   **5,224,787 B · f2b9893f2f4483b07e5981ed3159f73e · 64,839 lines**; **420 members extracted
   (2 + 418)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **28,116 B ·
   ff9b5a7d882bea02b2c0eea41acb019b · 420 lines**; WORKING-REGISTER.md **702,192 B ·
   e0ff730f88b4c15301ef2dc0d755ef10 · 6,143 lines**, ends **W-138**; DEFERRED.md **143,252 B ·
   fadbe4ef · 28 blocks**; RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged); r2lib.py
   21,022 B · 580d2ea2 · 453 lines (unchanged); gate.py 9,377 B · a01ef15a; close.py 6,456 B ·
   98acae67; r2-tools.py 6,529 B · 4702f5f9; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py
   4262f7c5; minmax.py 26da1d78. If two `BUILD*_compendia` files are present after a close, pass
   `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch14r r2-ch14s` → two `OK` (chat 99's goldens:
   r2-ch14r.out 18,200 B · 1693fbf1 · 232 lines; r2-ch14s.out 11,750 B · 692a7ecb · 126 lines). Both
   import the lifted r2lib and read members only; an AttributeError means the extraction seated a
   pre-lift r2lib and the chat stops.
8. `python3 /home/claude/members/gate.py cert 100` → writes `/home/claude/GATE-ch100.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 99 did (do not repeat)

**§24–§24.7 is closed** — main **L6623–L6740, 118 lines, eight headings**, boundaries re-scanned and
confirmed. **Twenty-five deviations, seventeen verified, seven incidentals, three census rows
closed** (1139 not a defect, 1140 defect, 1141 not a defect — all C9). All of it is in
`READ-ch14r.md` and `CENSUS-CLOSURES-ch14r.tsv`; **do not re-measure any of it.**

**The four findings that carry furthest:**

- **14r-01 — the collection's headline totals are stale, not wrong.** Chapter 24 prints 546 of 789
  interior cells at 69.2 %, 243 failures over 62 channels, and four further counts at L6632. **The
  Register agrees with the chapter** — 673 registers *869 to 930 interior cells*, 797 registers the
  789. **The Spectra Compendium does not**: it states its own totals at spectra-member L900 as **596
  channel rows across 28 elements · 2,269 interior cells**, and its bracket columns sum to **1,577 of
  1,738, 161 failures over 98 channels, 90.7 %**. A sweep of five row-filters, sixteen stage
  thresholds and two ℓ caps returns none of the six printed figures — the sweep is stated in full in
  `r2-ch14r.out`. R3 needs a **recomputation at the current basis**, and must first resolve 14r-19.
- **14r-19 — six channels are tabulated twice in the Spectra Compendium**, 68 interior cells
  double-counted: Ar II L326–L328/L331 repeated at L367–L369/L366, Si I L811/L812/L836 repeated at
  L839/L841/L837, under a second configuration notation, one copy bracket-tested and the other
< truncated lines 104-223 >
    table defect or a short compendium. **14r-19's double-tabulation must be settled before any
    recount.**
15. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one substantive (L8052
    credits Nesterov alone for a result §23.8.1 credits to both). Chat 99 adds **"KI" without its
    space** at L6657 and L6716, **"neon II"** spelled out at L6704, and **the Edlén Handbuch chapter
    dated 1960 at two sites and 1964 at five** (14r-20), which also makes L6683's *sixty-five years
    old* wrong under both.
16. **The single-witness class** — five of twenty-one distinctive figures in chat 99's 118 lines, six
    of twelve in chat 98's 74, fourteen in chat 97's 115, seventeen in chat 96's 131, thirteen in
    chat 95's 125. R4 should state which figures are unverifiable rather than leaving them looking
    checked, and distinguish *unverifiable* from *uncorroborated*.
17. **Heading sentences finishing in the body** (14q-06) — **now three, not four**: L4407
    (+ "routes"), L6582 (+ "one"), L8659 (+ "disanalogy"). **L6634 closes** — chat 99 confirmed it is
    a table header, not a sentence continuation.

## Close (chat 100)

`gate.py bank r2-ch14t r2-ch14u`; delete pycache in its own delete-only call; write `W-139.md`
(begins `### W-`, **ends with a blank line** — close.py asserts this); append a DEFERRED block as
`DEF-100.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD128_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD129_compendia_papers_audits.md --w W-139.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-100.md \
  --members members/READ-ch14t.md members/CENSUS-CLOSURES-ch14t.tsv members/r2-ch14t.py \
  members/r2-ch14t.out members/r2-ch14u.py members/r2-ch14u.out
```

It must print **reverse recovers md5 f2b9893f2f4483b07e5981ed3159f73e == old: True** before writing;
if it does not, nothing is written and the failure is reported. `--append` arguments must precede
`--members`, and `--members` may be omitted entirely if nothing new is seated. **A changed
append-only member is grown with `--append <member> <delta-file>`, never passed to `--members`** —
close.py refuses a name collision, and a member needing *replacement* rather than growth has no
mechanism at all. After a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state; **verify appends by reading the new bundle directly** —
and note the Register member lives in the **main** bundle, not the compendia bundle. `gate.py bank`
refuses to overwrite an existing `.out`; correcting an instrument after banking needs a
**delete-only** call to remove the golden, then bank again. Then copy BUILD129, HANDOFF-53 and the
READ file to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-52.md` and
  `The_Method_1_6_BUILD128_compendia_papers_audits.md`.
- **Retire** once BUILD128 gates PASS in chat 100: HANDOFF-51 and BUILD127, plus any earlier
  compendia builds still present (BUILD107–BUILD126) **except BUILD124**.
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Read those values out of the
  **member** rather than re-running the instrument; that is the pattern R3 should adopt before
  BUILD124 is retired.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 — the
  certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 100

"Chat 100. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD128 compendia (5,224,787 B, md5
f2b9893f2f4483b07e5981ed3159f73e, 64,839 lines, 418 members). List uploads, outputs and /home/claude
first. Run HANDOFF-52's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 420 files), then gate.py census, run --core, manifest, run r2-ch14r
r2-ch14s, cert 100; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 99's block is the last of
twenty-eight. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state;
discard it per Ruling 41 — its discard is W-118, not W-107. Line numbers are MEMBER line numbers and
are never carried between chats, and neither is any count: re-scan every heading on
The_Method_1_6-2.md before reading a line. Chapter 23 closed in chat 98; chat 99 read §24–§24.7. Then
continue Phase R2 under the chat-81 cadence: take §24.8–§24.9, main L6741–L6816, 76 lines, two
headings, and decide the cut before reading. Read it all, census its claims into computable and
prose, then run exactly two instrument batches, r2-ch14t computable and r2-ch14u prose, importing
heading_line, section_span, has_token and enclosing from r2lib — copy nothing, pass them the LINE
LIST and not the member text, and read the six volume MEMBERS, never a BUILDnnn bundle path. Chat 99
measured that the Spectra Compendium's channel table is 596 rows across 28 elements carrying 2,269
interior cells — it states this itself at spectra-member L900 — that interior = levels − 2 on all 477
rows with three or more levels, that the 119 two-member rows print interior 1 by stated convention,
that the column headed 'fits' holds the ionisation stage, and that six channels are tabulated twice
for 68 double-counted cells. Chapter 24's own totals (546/789, 930, 869, 1,105, 1,442) agree with
Registers 673 and 797 and match nothing in the compendium under any of nineteen bases swept, so the
class is staleness rather than error — measure every count this unit attributes to the collection or
to a named species against the compendium's current rows and say which basis you used. Resolve
L6781's '13 of 64 interior cells' against §24.7's 'H I gives 5 cells'; there is no H I channel row
anywhere in the six volumes. Read Register 1625 on independence before judging §24.8. Where the text
prints a sample, measure the population. Compare bases before calling a carried figure wrong. Match a
printed figure at the source's precision, not at yours. A convention stated in the source is not a
defect. Use the exact-token heading resolver, never prefix matching, and never span a section by
heading rank. Grep lowercase 'register NNN' by hand. Resolve every pointer to the claim and not the
heading, and if it fails at the named target grep the whole volume before recording it. Give every
negative claim its own witness, and state what a sweep covered before recording a negative from it. A
number beside a species is not that species' ceiling — read the header. ν is not n. Never round with
Python's round() — use Decimal.quantize and name the convention. A heading is not a statement, a
bound is not a measurement, a boundary case is not a violation. Re-read every verdict against the
numbers printed above it AND below it. When an instrument disagrees with a hand reading, suspect the
instrument first. Close the section read before the next opens. At close: bank both goldens with
gate.py bank, write W-139 ending with a blank line, build BUILD129 with close.py (reverse must
recover f2b9893f…), write HANDOFF-53. A changed append-only member is grown with --append, never
--members; correcting a banked golden needs a delete-only call first. No corrections, no Register
entries, no TASK 1 until the review closes. Handoff at 90–95 % of context or on a closed section read
— never earlier, never mid-section. Timeout on every call. Delete-only calls for pycache, never
chained to gate.py bank. Never copy over an existing file."
