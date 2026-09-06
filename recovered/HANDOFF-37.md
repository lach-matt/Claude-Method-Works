# HANDOFF-37 — The Method 1.6 — chat 84 → chat 85

- Written from **chat 84** for **chat 85**. Live files: **BUILD90 main** (unchanged since chat 62) and
  **BUILD112 compendia** (= BUILD111 + W-122 + chat 84's DEFERRED block + six new members). Register
  **1 to 1792** (unchanged). W-122 IS seated; chat 85 seats nothing at open and writes W-123 at close.
- **Rulings and discipline:** the member `RULINGS-R2.md` (6,041 B · 30 lines, unchanged this chat)
  governs and is append-only; **read it at open, last block first** — the chat-81 block sets the
  cadence, and chats 82, 83 and 84 have now all run it. **Deferred cross-chapter items:** `DEFERRED.md`
  (**46,912 B · 131 lines**, with chat 84's block) governs; do not re-derive. **Findings carried to
  R3:** the READ-chNN.md members (READ-ch13n is chat 84's) and W-101…W-122 in WORKING-REGISTER.md;
  nothing is restated here.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4" Löwdin/three-body
  plan is executed carried state (MEASURED in W-107, re-confirmed in chats 75–84); do not re-open it
  or put it to M. Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles.
  Retired handoffs are gone from Drive; never fetch or cite one. Never add HANDOFF-NN.md as a member.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 84. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD112_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths (the gate cost ≈ 13 % of chat 84, MEASURED).
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'89e1b72a60d5f3c2a430460c9b2bc7b4'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD112_compendia_papers_audits.md'}
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
   **3,968,759 B · 89e1b72a60d5f3c2a430460c9b2bc7b4 · 46,604 lines**; **330 members extracted (2 + 328)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`.
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/
   199,130, kinds 1565 · 1356 · 499 · 149, minmax, r2-tools-constants, extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK: 329 members listed, 330 files
   extracted`; MANIFEST.tsv **22,073 B · 5fe6138a73b3600d05f8cfb4f5ac941b · 330 lines**;
   WORKING-REGISTER.md **608,544 B · 1d49ba84122fe8902525982e26de8138 · 5,072 lines**, ends W-122;
   DEFERRED.md **46,912 B · e2d5b56c · 131 lines**; RULINGS-R2.md 6,041 B · 4cce8039;
   **r2lib.py 18,486 B · 3344ca87 · 396 lines** (unchanged this chat); gate.py 9,377 B · a01ef15a…;
   close.py 6,456 B · 98acae67…; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5;
   minmax.py 26da1d78; r2-tools.py 4702f5f9. If two `BUILD*_compendia` files are present after a
   close, pass `--comp <path>`.
7. `python3 /home/claude/members/gate.py run r2-ch13n r2-ch13o` (chat 84's instruments: ≈ 8 s and ≈ 1 s
   — one call). r2-ch13l ≈ 7 s, r2-ch13j ≈ 60 s, r2-ch13k ≈ 2 s, r2-ch13h ≈ 38 s, r2-ch13e ≈ 30 s,
   r2-ch12t ≈ 44 s, r2-ch12r ≈ 25 s, r2-ch12y ≈ 30 s, r2-ch12n ≈ 60 s, r2-ch12m ≈ 150 s — run these
   only when their figures are in question. `run --all` exceeds one 280 s call.
8. `python3 /home/claude/members/gate.py cert 85` → `GATE-ch85 … verdict PASS`. Shell is dash: text
   through python heredocs or create_file; no `<(…)`; one heredoc per bash call; non-ASCII grep output
   through python. Remove `members/__pycache__` in a **delete-only** call (G0e) after every instrument run.

## Next work — Phase R2, the section read: §16.6 through §16.8, then Chapter 17

**The cadence holds for a third chat.** Chat 84 read §16.1–§16.5.1 whole (150 lines) in two calls,
censused thirteen computable and ten prose claims, ran exactly two batches, and closed five
deviations, nine verified findings, five incidentals, five census rows and **two chat-74 DEFERRED
items**. Keep the shape: read the whole section in one or a few `lines` calls, census the claims in
two kinds, write one instrument for each, bank both, write one READ file and one CENSUS-CLOSURES file.

**The section read is §16.6 through §16.8, main L4482 through L4788** (Chapter 17 opens at **L4789** —
MEASURED chat 84 by heading scan; HANDOFF-36's L4477/L4478 was wrong, as HANDOFF-34's L4157 was, so
**verify both boundaries by a heading scan before reading**, every time). Its subsections: §16.6 the
six disjoint defences (L4482), §16.6.1 the vocabulary of reference as an index (L4520), §16.6.2 the
coordinate below the book's own floor (L4555), §16.7 two kinds of absence (L4574) with §16.7.1–§16.7.4
(L4578, L4618, L4636, L4644), §16.8 what self-reference does and does not defend (L4659) with
§16.8.1–§16.8.6 (L4663, L4669, L4683, L4691, L4733, L4772). That is **307 lines over sixteen
subsections** — twice chat 84's read. If the census is heavy, close **§16.6–§16.7** (L4482–L4658) as
the section read and open §16.8 next, rather than splitting a batch.

**What chat 85's batches already have waiting.** DEFERRED's remaining Chapter 16 item: **§16.6 L4482's
`multiverse dimension ⅅ_gro`**, which §14.6.1 L4115–4116 cites as a term with no referent, against
§29.2.2 L7922 — measure the term's referent at all three sites before writing anything. **L4525's
"constraints of §16.4 form"** is one of 13o-01's eight sites and falls in this range: resolve it to
the claim, not to §16.4's heading, and do not re-derive 13o-01 — it is closed and recorded. §16.6's
own headline claim — *"The defences are disjoint, and there are six"* — is a self-count over the
chapter itself: **measure the six against the defences the chapter actually names**, since a running
self-count printed five ways in four subsections is an established pattern here (13j-11). §16.6.2's
"below this book's own floor" and §16.8.4's "the cost of a fabrication is computable" are both
computable claims on the tower; §16.8.5's "the floor is derived rather than measured" and §16.8.6's
"two closure operators, and the book names one" are re-measurable against r2lib's `Rset` / `Rn` pair.

**Patterns chats 77–84 established, to watch for:** a Register entry restating a section may carry
different figures — measure both, withdraw neither; a withdrawn figure may still stand at other sites
— the later line governs, record the residue; a section may attribute a proof, a table, a count or **a
constraint form** to a neighbour that does not contain it (13d-01, 13h-01, 13i-04, 13j-08, 13l-03,
13l-05, and now **13o-01** at eight sites); a claim may be true while the statement printed for it is
not (13g-01, 13h-04, 13j-01, 13l-01, and now **13n-01**, where an inequality is printed as an
equality); a rounded ratio may be printed with the word *exactly*; a figure may be printed with its
population unstated (13j-07, 13l-06, 13l-09, **13n-02**, **13o-03**); a heading may be truncated with
its remainder rendering as body text (**13o-04**, four sites). Resolve every pointer to the claim,
never to the heading; check the arithmetic of every ratio and percentage as well as every count;
measure a claim and its stated witness separately; and where the text prints a sample, measure the
population. **Chat 84's B6 is the standing warning against checking by eye:** d³ at 2S = 3 admits five
2J values only because d³ carries two quartet terms; read from ⁴F alone the printed set looks wrong.

**Per section read (close it — files written, md5s measured, both goldens banked — before the next
opens):** `python3 members/r2-tools.py lines|pointers|figures|census|layout A B` over the whole section
(its pointer regex is case-sensitive and does not know Appendix A's item numbers or Chapter 4's
protocol rows — a bare `§4.6` or `A.2` reported UNRESOLVED is usually one of those, not a defect; and
a `§N` inside a quoted external citation is an artefact, not a pointer — chat 84 confirmed L4440's
`§17` is Edlén's Handbuch §17); read every line; census the claims into the two kinds, writing the
census into the READ file; then the two batches in `members/r2-chNN.py` (next names **r2-ch13p**
computable, **r2-ch13q** prose), importing r2lib by path:

```
import importlib.util, os; H=os.path.dirname(os.path.abspath(__file__))
s=importlib.util.spec_from_file_location('r2lib', os.path.join(H,'r2lib.py')); r2lib=importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T=r2lib.load_tower()
```

**`load_tower()` returns the tower-2 MODULE — call `T.L8()`, `T.L9()`, `T.L10()`, not `T[8]`.** r2lib
carries build9/tarjan/analyse, is_tree, closure/factor_q/ci/components/separates, support/direct/
composed, mi/ci_sets/gG_index, lam9p, read_member, md5, the Λ₉/Λ₉′ and (g, G) constants, `Rset`,
`cover_model`, `cover_reduce`, `exact_seed`, `enum_min_covers`, `closure_mask`, `staircase`, and
**`L8_at(caps)`** — the tower at arbitrary caps, caps = (n_max, e_max, l_max, k_max, f_max);
(3,3,1,3,1) → 976, (3,3,1,4,1) → 1,636, (4,3,1,4,1) → 2,394, and 216 at 32 distinct settings of which
only 4 give all eight axes more than one value. Still owed, to be lifted verbatim with provenance when
a batch next needs them (DEFERRED lists them): r2-ch12c/e/g/h's functions; chat 75's `closure_chunked`,
`fixed_point`, `length`, `fibre_check`, `criterion`; chat 76's `terms`, `new_terms`, `jc_values`,
`TERMS` and **`phi_at`**, the multiplicity-weighted `densities`; chat 77's stage-composability sets;
chat 78's `first_fail` / `failing_pairs` (note r2lib.closure counts **ordered** pairs including self,
so halve for the unordered counts the book prints); chat 79's `sections(X, w)` and `R(X)` /
`failing(X, op)`; chat 80's `Rn(X)` and r2-ch13f's interval Box/binding measure; **and now chat 84's
three: the numeric-Jacobian + pivoted `rank` pair, the Slater-determinant term engine (`dets`,
`allowed_2S`, `terms`, `seniorities`) — the measurement for every LS-coupling claim in Chapters 8–12
and the Spectra Compendium — and the alphabet sweep that measures a printed cell count against every
plausible reading of an unstated alphabet.** The tower's sides, for any width: A = (n, ℓ, k, 2S, 2J_c,
2K, 2J) at indices 0,1,2,7,10,11,12; B = (e, f, g, 2S′, v) at 4,5,6,8,9; the base q at 3. At Λ₈ the
eight coordinates are (n, ℓ, k, q, e, f, g, 2S) in that order, with min (1,0,1,0,1,0,0,0) and max
(3,1,3,3,3,1,3,3) — MEASURED, chat 82. Λ₈'s constraint graph is the tree n–ℓ–k–q–g–f–e with 2S hanging
off k; its alphabet sizes are (3,2,3,4,3,2,4,4), product **6,912**, and it has exactly one path between
each of the 28 coordinate pairs — MEASURED, chats 83 and 84.

Write READ-chNN.md (the claim census first, then A deviations with both texts, B verified, C
incidental) and CENSUS-CLOSURES-chNN.tsv (id, verdict, reason; A vocabulary; header only when no row
is in range — chat 84 closed rows 1085–1089). Instruments print no wall-clock time (time a run in the
shell with `date +%s` if needed). **A batch over ~200 s is split into two instruments, never trimmed of
coverage**; never build a set inside a per-cell comprehension; prefer the box sweep (`Rset`) over the
pairwise fixed point (`Rn`) above ~2,000 cells; and the exact set-cover solver is cheap after reduction
but does **not** close on 4⁵, 4⁶ or 3⁶.

## Close of chat 85

1. `rm -rf /home/claude/members/__pycache__` (delete-only call); `python3 members/gate.py bank r2-ch13p`
   … for each new instrument (writes NAME.out; refuses to overwrite), then a **separate** delete-only
   pycache call.
2. Write /home/claude/W-123.md: begins `### W-123 —`, ends with a blank line; records the gate, the
   section read, findings, what was not done, the close estimate.
3. `python3 members/close.py --old /home/claude/The_Method_1_6_BUILD112_compendia_papers_audits.md --new
   /home/claude/The_Method_1_6_BUILD113_compendia_papers_audits.md --w /home/claude/W-123.md
   [--append DEFERRED.md /home/claude/deferred-add.md] --members members/READ-ch13p.md
   members/CENSUS-CLOSURES-ch13p.tsv members/r2-ch13p.py members/r2-ch13p.out members/r2-ch13q.py
   members/r2-ch13q.out` — every `--append` must precede `--members` (which consumes every later
   argument); `--append` may be given more than once. It must print `reverse recovers md5
   89e1b72a60d5f3c2a430460c9b2bc7b4  == old: True` before writing. Never edit a seated member in place.
   close.py rewrites the bundle only — the extracted `/home/claude/members/` copies stay at their
   pre-close state, so `gate.py manifest` reports FAIL on exactly the changed members after a close;
   verify appends by reading the new bundle, and **print only the fields you need**.
4. HANDOFF-38 in this form (update: build numbers, md5s, MANIFEST.tsv, WORKING-REGISTER.md, DEFERRED.md,
   the member count, the run list, next work, the prompt). `ls -la /mnt/user-data/outputs` before
   copying; never copy over an existing file; present HANDOFF-38.md first, then BUILD113 and the READ file.
5. Handoff at 90–95 % of context or on a closed section read — never earlier, never mid-section. Begin
   the close when the remaining context would not fit a section read plus the close (a section read
   ≈ 30–45 %, the close ≈ 12 %, MEASURED in chats 82, 83 and 84). No corrections, no Register entries,
   no TASK 1 until the review closes.

## M's Drive actions

- **UPLOAD** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-37.md` and
  `The_Method_1_6_BUILD112_compendia_papers_audits.md` (89e1b72a…).
- **RETIRE:** HANDOFF-36 and BUILD111 once BUILD112 gates in chat 85; HANDOFF-35 and BUILD110 if still
  present; HANDOFF-34, HANDOFF-33, HANDOFF-32, BUILD109, BUILD108, BUILD107 and any earlier compendia builds.
- **KEEP:** BUILD90 main, tower-2.py, chat65/66/67-instruments.tar.gz, SWEEP-B-C-chat67.md, convert.py,
  the certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 85

"Chat 85. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD112 compendia (3,968,759 B, md5
89e1b72a60d5f3c2a430460c9b2bc7b4, 46,604 lines, 328 members). List uploads, outputs and /home/claude
first. Run HANDOFF-37's §0 gate in full and in order — fetch both bundles by title, bootstrap (decode,
md5, extract, expect 330 files), then gate.py census, run --core, manifest, run r2-ch13n r2-ch13o, cert
85; any FAIL stops the chat with a report. Read RULINGS-R2.md and DEFERRED.md from the members; chat
84's DEFERRED block is the last one. The standing block's Phase 0–4 (Löwdin/three-body) plan is
executed carried state; discard it per Ruling 41. Then continue Phase R2 under the chat-81 cadence:
the section read is §16.6 through §16.8, main L4482 through L4788, with Chapter 17 opening at L4789 —
verify both boundaries by a heading scan first, because two successive handoffs put Chapter 16's end in
the wrong place. Read it all, census its claims into computable and prose, then run exactly two
instrument batches, r2-ch13p computable and r2-ch13q prose. If the census is heavy, close §16.6–§16.7
(L4482–L4658) as the section read rather than splitting a batch. Measure §16.6's 'there are six'
against the defences the chapter actually names; resolve §16.6 L4482's 'multiverse dimension ⅅ_gro'
against §14.6.1 L4115–4116 and §29.2.2 L7922; and resolve L4525's 'constraints of §16.4 form' to the
claim without re-deriving 13o-01, which is closed. Resolve every pointer to the claim and not the
heading, measure a claim and its stated witness separately, check the arithmetic of every ratio and
percentage as well as every count, and where the text prints a sample measure the population. Close
the section read before the next opens. At close: bank both goldens with gate.py bank, write W-123,
build BUILD113 with close.py (reverse must recover 89e1b72a…), write HANDOFF-38. No corrections, no
Register entries, no TASK 1 until the review closes. Handoff at 90–95 % of context or on a closed
section read — never earlier, never mid-section. Timeout on every call. Delete-only calls for pycache,
never chained to gate.py bank. Never copy over an existing file."
