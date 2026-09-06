# HANDOFF-36 — The Method 1.6 — chat 83 → chat 84

- Written from **chat 83** for **chat 84**. Live files: **BUILD90 main** (unchanged since chat 62) and
  **BUILD111 compendia** (= BUILD110 + W-121 + chat 83's DEFERRED block + the `L8_at` lift into r2lib
  + six new members). Register **1 to 1792** (unchanged). W-121 IS seated; chat 84 seats nothing at
  open and writes W-122 at close.
- **Rulings and discipline:** the member `RULINGS-R2.md` (6,041 B · 30 lines, unchanged this chat)
  governs and is append-only; **read it at open, last block first** — the chat-81 block sets the
  cadence, and chats 82 and 83 have now both run it. **Deferred cross-chapter items:** `DEFERRED.md`
  (**41,404 B · 120 lines**, with chat 83's block) governs; do not re-derive. **Findings carried to
  R3:** the READ-chNN.md members (READ-ch13l is chat 83's) and W-101…W-121 in WORKING-REGISTER.md;
  nothing is restated here.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4" Löwdin/three-body
  plan is executed carried state (MEASURED in W-107, re-confirmed in chats 75–83); do not re-open it
  or put it to M. Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles.
  Retired handoffs are gone from Drive; never fetch or cite one. Never add HANDOFF-NN.md as a member.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 83.
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD111_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths (the gate cost ≈ 13 % of chat 83, MEASURED).
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'5e949b9f51950431dc0e69b2fe81d7ae'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD111_compendia_papers_audits.md'}
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
   **3,911,814 B · 5e949b9f51950431dc0e69b2fe81d7ae · 45,809 lines**; **324 members extracted (2 + 322)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`.
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/
   199,130, kinds 1565 · 1356 · 499 · 149, minmax, r2-tools-constants, extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK: 323 members listed, 324 files
   extracted`; MANIFEST.tsv **21,674 B · 2c18ddf06be96e3fd1aecf57e0f67432 · 324 lines**;
   WORKING-REGISTER.md **605,228 B · 959214cb97771b3bc9acf9ca4b56ade2 · 5,029 lines**, ends W-121;
   DEFERRED.md **41,404 B · b5a22be1 · 120 lines**; RULINGS-R2.md 6,041 B; **r2lib.py 18,486 B ·
   3344ca87 · 396 lines** (grown by chat 83's `L8_at` lift); gate.py 9,377 B · a01ef15a…; close.py
   6,456 B · 98acae67…; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5; minmax.py
   26da1d78; r2-tools.py 4702f5f9. If two `BUILD*_compendia` files are present after a close, pass
   `--comp <path>`.
7. `python3 /home/claude/members/gate.py run r2-ch13l r2-ch13m` (chat 83's instruments: ≈ 7 s and ≈ 1 s
   — one call). r2-ch13j ≈ 60 s, r2-ch13k ≈ 2 s, r2-ch13h ≈ 38 s, r2-ch13e ≈ 30 s, r2-ch12t ≈ 44 s,
   r2-ch12r ≈ 25 s, r2-ch12y ≈ 30 s, r2-ch12n ≈ 60 s, r2-ch12m ≈ 150 s — run these only when their
   figures are in question. `run --all` exceeds one 280 s call.
8. `python3 /home/claude/members/gate.py cert 84` → `GATE-ch84 … verdict PASS`. Shell is dash: text
   through python heredocs or create_file; no `<(…)`; one heredoc per bash call; non-ASCII grep output
   through python. Remove `members/__pycache__` in a **delete-only** call (G0e) after every instrument run.

## Next work — Phase R2, the section read: Chapter 16, then Chapter 17

**The cadence holds for a second chat.** Chat 83 read Chapter 15 whole (62 lines) in one call,
censused twelve computable and ten prose claims, ran exactly two batches, and closed nine deviations,
eight verified findings and two census rows. Keep the shape: read the whole section in one or a few
`lines` calls, census the claims in two kinds, write one instrument for each, bank both, write one
READ file and one CENSUS-CLOSURES file.

**Chapter 16 is `## 16.` at L4332 through L4477** (Chapter 17 opens at L4478 — verify with a heading
scan before reading, as chat 82 had to). Its sections: §16.1 the counting argument (L4335), §16.2 the
split (L4351), §16.3 D1 (L4359), §16.3.1 the D1 tripwire (L4379), §16.4 D2 (L4407), then §16.5 and
§16.6. That is ~146 lines, more than twice Chapter 15 — if the census is heavy, take §16.1–§16.4 as
the section read and close it before opening §16.5–§16.6, rather than splitting a batch.

**What chat 84's batches already have waiting.** DEFERRED's Chapter 16 items: §16.4's "form" and the
two-route protection (chat 74), and §16.6 L4482's `multiverse dimension ⅅ_gro`, which §14.6.1
L4115–4116 cites as a term with no referent, against §29.2.2 L7922. **Also seat 13l-03's neighbours:**
Appendix A's index sends A.4 to `§16.1, in full` and A.5 to `§16.5, in full`; chat 83 measured A.7's
row wrong (it points at §16.3, which contains the phrase zero times, while §15.3 contains it three
times), so resolve A.4 and A.5 to the claim while Chapter 16 is open rather than to the heading.
**And use `r2lib.Rset` and the exhaustive-population habit** — chat 83's largest finding is that
§15.3's `criterion is exact` is exact only under a reading the text does not print, found by sweeping
every subset of two small grids instead of trusting the printed `274 of 274`.

**Patterns chats 77–83 established, to watch for:** a Register entry restating a section may carry
different figures — measure both, withdraw neither; a withdrawn figure may still stand at other sites
— the later line governs, record the residue; a section may attribute a proof, a table or a count to
a neighbour that does not contain it (13d-01, 13h-01, 13i-04, 13j-08, and now **13l-03** and
**13l-05**); a claim may be true while the statement printed for it is not (13g-01, 13h-04, 13j-01,
and now **13l-01**, where the claim is true only under a reading the text does not give); a rounded
ratio may be printed with the word *exactly*; a rate may be printed with no denominator (13l-09); and
a running self-count may be printed five ways in four subsections (13j-11). Resolve every pointer to
the claim, never to the heading; check the arithmetic of every ratio and percentage as well as every
count; measure a claim and its stated witness separately; and where the text prints a sample, measure
the population.

**Per section read (close it — files written, md5s measured, both goldens banked — before the next
opens):** `python3 members/r2-tools.py lines|pointers|figures|census|layout A B` over the whole section
(its pointer regex is case-sensitive and does not know Appendix A's item numbers or Chapter 4's
protocol rows — a bare `§4.6` or `A.2` reported UNRESOLVED is usually one of those, not a defect;
chat 82 confirmed §4.6 is Chapter 4's row L1447); read every line; census the claims into the two
kinds, writing the census into the READ file; then the two batches in `members/r2-chNN.py` (next names
**r2-ch13n** computable, **r2-ch13o** prose), importing r2lib by path:

```
import importlib.util, os; H=os.path.dirname(os.path.abspath(__file__))
s=importlib.util.spec_from_file_location('r2lib', os.path.join(H,'r2lib.py')); r2lib=importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T=r2lib.load_tower()
```

**`load_tower()` returns the tower-2 MODULE — call `T.L8()`, `T.L9()`, `T.L10()`, not `T[8]`.** r2lib
now carries, in addition to build9/tarjan/analyse, is_tree, closure/factor_q/ci/components/separates,
support/direct/composed, mi/ci_sets/gG_index, lam9p, read_member, md5, the Λ₉/Λ₉′ and (g, G)
constants, and `Rset`, `cover_model`, `cover_reduce`, `exact_seed`, `enum_min_covers`, `closure_mask`,
`staircase`: **`L8_at(caps)`**, lifted verbatim in chat 83 — the tower at arbitrary caps, with
caps = (n_max, e_max, l_max, k_max, f_max); (3,3,1,3,1) → 976, (3,3,1,4,1) → 1,636, (4,3,1,4,1) →
2,394, and 216 at 32 distinct settings of which only 4 give all eight axes more than one value.
Still owed, to be lifted verbatim with provenance when a batch next needs them (DEFERRED lists them):
r2-ch12c/e/g/h's functions; chat 75's `closure_chunked`, `fixed_point`, `length`, `fibre_check`,
`criterion`; chat 76's `terms`, `new_terms`, `jc_values`, `TERMS` and **`phi_at`** (not lifted with
`L8_at` because it depends on `TERMS`), the multiplicity-weighted `densities`; chat 77's
stage-composability sets; chat 78's `first_fail` / `failing_pairs` (note r2lib.closure counts
**ordered** pairs including self, so halve for the unordered counts the book prints); chat 79's
`sections(X, w)` and `R(X)` / `failing(X, op)`; chat 80's `Rn(X)` and r2-ch13f's interval Box/binding
measure. The tower's sides, for any width: A = (n, ℓ, k, 2S, 2J_c, 2K, 2J) at indices 0,1,2,7,10,11,12;
B = (e, f, g, 2S′, v) at 4,5,6,8,9; the base q at 3. At Λ₈ the eight coordinates are
(n, ℓ, k, q, e, f, g, 2S) in that order, with min (1,0,1,0,1,0,0,0) and max (3,1,3,3,3,1,3,3) —
MEASURED, chat 82. Λ₈'s constraint graph is the tree n–ℓ–k–q–g–f–e with 2S hanging off k, and its
alphabet sizes are (3,2,3,4,3,2,4,4) — MEASURED, chat 83.

Write READ-chNN.md (the claim census first, then A deviations with both texts, B verified, C
incidental) and CENSUS-CLOSURES-chNN.tsv (id, verdict, reason; A vocabulary; header only when no row
is in range — chat 83 closed rows 1083 and 1084). Instruments print no wall-clock time (time a run in
the shell with `date +%s` if needed). **A batch over ~200 s is split into two instruments, never
trimmed of coverage**; never build a set inside a per-cell comprehension; prefer the box sweep
(`Rset`) over the pairwise fixed point (`Rn`) above ~2,000 cells; and the exact set-cover solver is
cheap after reduction but does **not** close on 4⁵, 4⁶ or 3⁶.

## Close of chat 84

1. `rm -rf /home/claude/members/__pycache__` (delete-only call); `python3 members/gate.py bank r2-ch13n`
   … for each new instrument (writes NAME.out; refuses to overwrite), then a **separate** delete-only
   pycache call.
2. Write /home/claude/W-122.md: begins `### W-122 —`, ends with a blank line; records the gate, the
   section read, findings, what was not done, the close estimate.
3. `python3 members/close.py --old /home/claude/The_Method_1_6_BUILD111_compendia_papers_audits.md --new
   /home/claude/The_Method_1_6_BUILD112_compendia_papers_audits.md --w /home/claude/W-122.md
   [--append DEFERRED.md /home/claude/deferred-add.md] --members members/READ-ch13n.md
   members/CENSUS-CLOSURES-ch13n.tsv members/r2-ch13n.py members/r2-ch13n.out members/r2-ch13o.py
   members/r2-ch13o.out` — every `--append` must precede `--members` (which consumes every later
   argument); `--append` may be given more than once (chat 83 appended DEFERRED.md and r2lib.py in one
   call). It must print `reverse recovers md5 5e949b9f51950431dc0e69b2fe81d7ae  == old: True` before
   writing. Never edit a seated member in place. close.py rewrites the bundle only — the extracted
   `/home/claude/members/` copies stay at their pre-close state, so `gate.py manifest` reports FAIL on
   exactly the changed members after a close; verify appends by reading the new bundle, and **print only
   the fields you need**.
4. HANDOFF-37 in this form (update: build numbers, md5s, MANIFEST.tsv, WORKING-REGISTER.md, DEFERRED.md,
   the member count, the run list, next work, the prompt). `ls -la /mnt/user-data/outputs` before
   copying; never copy over an existing file; present HANDOFF-37.md first, then BUILD112 and the READ file.
5. Handoff at 90–95 % of context or on a closed section read — never earlier, never mid-section. Begin
   the close when the remaining context would not fit a section read plus the close (a section read
   ≈ 30–45 %, the close ≈ 12 %, MEASURED in chats 82 and 83). No corrections, no Register entries, no
   TASK 1 until the review closes.

## M's Drive actions

- **UPLOAD** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-36.md` and
  `The_Method_1_6_BUILD111_compendia_papers_audits.md` (5e949b9f…).
- **RETIRE:** HANDOFF-35 and BUILD110 once BUILD111 gates in chat 84; HANDOFF-34 and BUILD109 if still
  present; HANDOFF-33, HANDOFF-32, BUILD108, BUILD107 and any earlier compendia builds.
- **KEEP:** BUILD90 main, tower-2.py, chat65/66/67-instruments.tar.gz, SWEEP-B-C-chat67.md, convert.py,
  the certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 84

"Chat 84. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD111 compendia (3,911,814 B, md5
5e949b9f51950431dc0e69b2fe81d7ae, 45,809 lines, 322 members). List uploads, outputs and /home/claude
first. Run HANDOFF-36's §0 gate in full and in order — fetch both bundles by title, bootstrap (decode,
md5, extract, expect 324 files), then gate.py census, run --core, manifest, run r2-ch13l r2-ch13m, cert
84; any FAIL stops the chat with a report. Read RULINGS-R2.md and DEFERRED.md from the members; chat
83's DEFERRED block is the last one. The standing block's Phase 0–4 (Löwdin/three-body) plan is
executed carried state; discard it per Ruling 41. Then continue Phase R2 under the chat-81 cadence:
the section read is Chapter 16, main L4332 through the line before Chapter 17 — verify both boundaries
by a heading scan first, read it all, census its claims into computable and prose, then run exactly two
instrument batches, r2-ch13n computable and r2-ch13o prose. If the census is heavy, close §16.1–§16.4
as the section read rather than splitting a batch. r2lib now carries L8_at(caps), the tower at
arbitrary caps, lifted in chat 83. Resolve Appendix A's A.4 → §16.1 and A.5 → §16.5 rows to the claim
while the chapter is open, since chat 83 measured A.7's row (→ §16.3) wrong. Resolve every pointer to
the claim and not the heading, measure a claim and its stated witness separately, check the arithmetic
of every ratio and percentage as well as every count, and where the text prints a sample measure the
population. Close the section read before the next opens. At close: bank both goldens with gate.py
bank, write W-122, build BUILD112 with close.py (reverse must recover 5e949b9f…), write HANDOFF-37. No
corrections, no Register entries, no TASK 1 until the review closes. Handoff at 90–95 % of context or
on a closed section read — never earlier, never mid-section. Timeout on every call. Delete-only calls
for pycache, never chained to gate.py bank. Never copy over an existing file."
