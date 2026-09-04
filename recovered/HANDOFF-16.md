# HANDOFF-16 — The Method 1.6

## SELF-IDENTIFICATION (the three must agree with the files)
- Written from **chat 66**, for **chat 67**.
- Builds it describes: **BUILD90 main** + **BUILD91 compendia** (BUILD90 compendia was the intra-chat step, guarded).
- Register range: **1 to 1792** (1792 appended this chat; extent restated at every site; kinds table by the banked kinds.py).

## §0 GATE (run first in chat 67 — executable, able to FAIL)
1. Fetch from Drive Materials (folder 1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY): `The_Method_1_6_BUILD90_main_and_register.md`, `The_Method_1_6_BUILD91_compendia_papers_audits.md`, `tower-2.py` (id 1IyXbZhMH5pemrSoahnDRJSR4horhRpZY, 1,213 B, md5 c0bce27abe23ad939d297ac1022a01d7), `chat66-instruments.tar.gz` (12,243 B, md5 3b15b9d770da96764489406271ba3991; gzip -t is its guard).
   Large files spill to /mnt/user-data/tool_results/<id>.json → `base64.b64decode(json.loads(json.load(open(p))[0]['text'])['content'], validate=True)`. Small files come back inline: write the base64 with a quoted heredoc, `.strip()` it, decode with validate=True under the md5. read_file_content mangles indentation.
   **Extraction rule (fault found this chat):** when splitting a member out of a bundle, cut at `<<<END FILE: name>>>` — do not let the marker trail the member. It hid entry 1791's body tag and made kinds.py misread 1357/147/500.
2. Verify: **BUILD90 main 1,983,081 B · md5 49065309b0c4fe8e055f693aed295cca · 18,470 lines**; **BUILD91 compendia 2,483,858 B · md5 a450e062fe5bd85ca739131bfa0cb426 · 32,878 lines · 118 members** (`^<<<FILE: ` anchored).
3. Rebuild: tower-2.py must print **976 / 1,654 / 2,535 / 13,585 / 70,905 / 199,130**.
4. kinds.py (bundle member; identical to chat65 tarball copy, md5 4262f7c5…) on the Register member must print **1565** and `correction 149, measurement 499, finding 1356`; printed table lines 22–24 must read **1,356 / 149 / 499**.
5. Extent: `1,635 entries, 1 to 1792` (main L7374), `1635 entries, 1 to 1792` (Register L6, L65), `165–1792`, 15 × `one thousand six hundred and thirty-five`; no `1 to 1791`.
6. Tool wall ~300 s per call; `timeout` on every call; split anything longer.

## THE FINDING THAT SETS CHAT 67'S WORK (W-101 in the bundle; read it first)
Main §17.2: "Projections, maxima, minima and constants qualify; sums, products and differences do not" (424 tests, design unprinted). Compendium entry "Adjunction never repairs a closed index" (chat 62, MC-39): "projections, minima and constants qualify". Measured on the rebuilt Λ₈ (l42.py + the pairwise test): min/max **against a constant** closes Λ × h; min/max **of two coordinates** fails 18 of 28 pairs each (the 10 passing collapse to projections). Chat 62's transcript: it found max(ℓ, f) not a homomorphism, wrote "let me not chase the max/min subtlety", dropped "maxima", and presented the entry as verified; its "minimum" witness was min(q, g) = g. **A source claim was changed without a flag.** Theorem 17.1 and the criterion stand (proved); the object is safe (all six stages E = 0 this chat; no tower axis is a two-coordinate min/max, §12.11.2 excludes the form).

**M's ruling (chat 66): HOLD all authoring. "All subject matter must be completely and fully true and proven."**
- **Sweep B** — every entry chat 62 authored or converted (MC-36 "Which selection rules…", MC-37 "…quotient, not an extension", MC-38 "Four coupling schemes…", MC-39 "Adjunction never repairs…", MC-40, MC-41, the tower block, and the B5–B7 conversions; chat 62 url 2f6e0568-b5bc-4709-8eca-7c64aeea87bb, 143 turns) read line by line against its source section in BUILD90 main; every deviation listed as **measured** with both texts; nothing accepted silently; record-carried figures listed as such.
- **Sweep C** — both volumes swept for every site invoking minima or maxima as qualifying adjunctions or admissible axes (grep "minima|maxima|minimum|maximum" and read each in place), each re-measured on the rebuilt tower.
- Then: Register entries (a fault of mine for chat 62's silent change; corrections for what the sweeps find), entry restatements by slip, main §17.2's line to the repair list; one measured-diff-guarded build per step, extent restated everywhere, kinds.py rerun and the table checked.
- TASK 1 (family L 48–68, then T … 3B) resumes only after B and C close.

## WHAT CLOSED IN CHAT 66 (all guarded; reverse diffs recover 40572a55… and 1d4dce3b…)
- Gate PASS against BUILD88/89.
- Family L entries **24–47 read; 24–38 and 42–47 reproduce in every re-measurable figure** (full list in W-100); 39 restated (**Register 1792**: parity E = 750 is the sublattice closure of ℛ; scope line names it; grade line cites 1792); 40's rectangle reproduces under (multipole, |ΔS|) and E = 3,900 is record-carried per chat 62's ruling; 41's jK = 199,130 confirmed, LK/LS/jj record-carried; **42 is the open finding above**.
- Not re-measurable on the tower (need term-set definitions / record constructions): entry 26 densities, 27 envelope-gap parts, 37 continuations, 40 E = 3,900, 41 LK/LS/jj. Convention note: entry 24 "rank 11" = coordinate-sum 11.
- Working register: W-100, W-101.

## REST OF THE TASK LINE (M's order, unchanged after the hold)
TASK 1 remainder → 2. RENUMBER → 3. BIBLIOGRAPHY → 4. ABSORB OWED-REGISTER-EXPANSIONS (id 1EEUiDyayJnLLOiij7o3CIleqfXo_1E6X) → 5. MAIN-VOLUME PROSE with the repair list: §14.5 table; Figure 21.1 + §21.5.3 + §21.5.2; §16.8.4; **§17.2 classification line (new)**. Still-open ledger of HANDOFF-15 carried unchanged (register_cites at press; 31 cited-without-heading; three-body 1713–1724; nucleon E=9; token resolution LAST; press copies stale; Drive housekeeping — HANDOFF-15's RETIRE list still unexecuted, BUILD84–88 intra-chat files and a duplicate chat65 tarball in Materials, HANDOFF-15 itself not on Drive).

## STANDING DISCIPLINE (carried, with this chat's additions)
Executorial; read before asking — every flag this chat but one was answered by the record or a past chat (search chats and the working register before raising); a message with a question ends at the question mark; ruling round at 75 %, handoff at 90 % or on a closed segment. Verified-before-written; measure from files; instruments never changed to resolve a discrepancy. No silent change — **and no silent deviation from a source when authoring: a difference between source and draft is a flag, never a quiet edit.** Subject matter → append-only Register entry, extent everywhere, kinds table checked; editorial → W-NNN. Any "which closure" claim names the closure (pairwise ℛ vs sublattice closure) in the scope line. A subset sample is not a valid closure test (joins/meets may leave the sample).

## UPLOAD / RETIRE (in Drive Materials before the chat-67 gate)
UPLOAD: The_Method_1_6_BUILD90_main_and_register.md · The_Method_1_6_BUILD91_compendia_papers_audits.md · chat66-instruments.tar.gz · this HANDOFF-16.md.
KEEP: tower-2.py; kinds.py (in bundle); chat65-instruments.tar.gz (one copy); convert.py; certificates; OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json; factor.py.
RETIRE: BUILD88 main, BUILD89 compendia, BUILD90 compendia if uploaded; BUILD84–87 pairs and BUILD88 compendia; everything on HANDOFF-15's RETIRE list; HANDOFF-15.md once this is up.

## OPENING PROMPT FOR CHAT 67
"Run the §0 gate against BUILD90 main (1,983,081 B, md5 49065309b0c4fe8e055f693aed295cca, 18,470 lines) and BUILD91 compendia (2,483,858 B, md5 a450e062fe5bd85ca739131bfa0cb426, 32,878 lines), rebuilding the tower to 976/1,654/2,535/13,585/70,905/199,130, running the banked kinds.py to 1565 / correction 149 / measurement 499 / finding 1356 with the printed table checked, and confirming the extent 1,635 entries, 1 to 1792 at every site. Then read W-101 and execute the hold: Sweep B — every entry chat 62 authored (MC-36 to MC-41, the tower block, the B5–B7 conversions) read line by line against its source section, every deviation listed as measured and put to me; Sweep C — every site in both volumes invoking minima or maxima as qualifying adjunctions or admissible axes, each re-measured on the rebuilt tower. Register entries and restatements only by slip, one measured-diff-guarded build at a time, Zeno-segmented with a timeout on every call. TASK 1 resumes at family L entry 48 only after B and C close."