# LOWDIN-HANDOFF-29 — single superset archive (session 29, 2026-08-17). Supersedes HANDOFF-28 + PACK-29.
Bank restore-point-2_13 (R 1700) unchanged; nothing written to register/index/store since. Findings only, pack5 … pack29.
Verify:  bash verify29.sh                      (expect ok=N bad=0)
Runtime: as README-HANDOFF-28.md (which chains 27 -> ... -> 18), then: cp pack29/*.py pack29/*.jsonl rt/   (pack29/frachf.jsonl supersedes pack28's: six rows)
Gates (all before ANY new work; run in rt/): gates (1)-(35) of README-HANDOFF-28.md (SUBCELL=1 is now the standing convention; gates reproduce), plus
 (36) python3 frachf.py 55 21 57 71   -> must SKIP all four; if a row is deleted it reprints (Cs I -0.130128 · Sc -0.292356 · La -0.223687 · Lu -0.178789; 90-234 s each, ONE per tool call)
 (37) python3 cutfrac.py              -> must SKIP all six; if cutfrac.jsonl deleted reprints Cs F_out 0.8689, Sc 0.0201, Y 0.0762 (~30 s/row)
 (38) python3 corepol.py gate         -> "H 1s alpha 4.5001", "He HFS alpha 2.5036"
 (39) python3 corepol.py 55           -> must SKIP; if row deleted reprints Cs alpha_closed 29.237 E_A_closed -0.02985
 (40) python3 corepol.py 21           -> must SKIP; if row deleted reprints Sc alpha_closed 3.723 E_A_closed -0.217 A_ns -0.13953
Read first: pack29/BRIDGE-LOWDIN-SESSION-29.md, then SPEC-DROW-EXCESS-SESSION-30.md (the ruled plan: BOTH routes, comparison decides), then FINDING-CUTFRAC, FINDING-COREPOL, FINDING-FRACHF-CLASS.
Known: bash egress denies network. Known (F18.1): list rt/ for files not in any pack. Known: tool call limit ~300 s — one frachf row per call.
Known: corepol is uncoupled Sternheimer in the HFS local potential — absolute alphas inflated ~1.8x (He gate); orderings/ratios only. gate-13 'hfs' is Hartree-Fock-Slater.
Handoff: M's ruling -- trigger 90 %, finish the running task, then full handoff; next archive = LOWDIN-HANDOFF-30 superset.