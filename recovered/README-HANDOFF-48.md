# LOWDIN-HANDOFF-48 — single superset archive (session 48, 2026-08-19). Supersedes HANDOFF-47.

**THIS FILE WAS WRITTEN, NOT COPIED (F47.1).** Check this header against
`pack48/BRIDGE-LOWDIN-SESSION-48.md` before trusting any recipe below. Bank restore-point-2_13
(R 1700) unchanged; nothing written to register/index/store. pack5 … **pack48**.

Verify: `bash verify48.sh` (expect **ok=N bad=0 extra=0**, BOTH halves, F43.1).
HALF A is integrity (every listed file present and hashing). HALF B is completeness (no file in
the tree absent from the manifest). `bad=0` alone does NOT establish the tree is the sealed tree.
Can-fail: `touch pack48/PLANTED && bash verify48.sh` -> extra=1, exit 1. Remove it afterwards.

**The exact ok= count is deliberately NOT written here (F48.1).** SESSION-47-COMBINED.md stated
ok=984 when the true count was 985 — it omitted itself, having been sealed after its own header
was written. A header cannot state the count of a manifest that includes the header. Read the
count off the run.

## Runtime rebuild — rt/ is NOT in the archive and NOT in the manifest

The archive ships packs, not a runtime. Rebuild beside the packs:

    mkdir -p rt && cp -r pack5/. rt/ && cp pack7/pack5/*.py rt/ && cp -r pack8/pack5fix/. rt/
    cp pack9/*.py pack9/*.jsonl rt/ && cp pack10/* rt/ && cp pack12/*.py pack13/*.py rt/
    cp pack16/*.py pack16/*.jsonl rt/ && cp pack17/*.py pack17/*.jsonl pack17/*.c rt/
    cp pack18/*.py pack18/*.jsonl pack18/*.c rt/
    for n in $(seq 19 48); do for e in py jsonl c json; do ls pack$n/*.$e >/dev/null 2>&1 && cp pack$n/*.$e rt/; done; done
    cd rt && for k in shoot shoot_sr shoot_x; do gcc -O2 -shared -fPIC -o lib$k.so $k.c; done

`19..48`, not `19..47` — layering short loses the 5d block. **`.json` is in the extension list
(F38.1); dropping it loses derive_P*.json.** Then CHECK, do not assume:

    wc -l rt/nlchain.jsonl        -> 74     (Z = 2..75)
    md5sum rt/nlchain.jsonl       -> read it off the run and record it in the s49 bridge

## Gates

    cp pack37/census37.sh . && bash census37.sh > CENSUS-SESSION-49-OPEN.txt
    cp pack48/gates_run48.sh gates_run49.sh && sed -i 's/GATES-48-OPEN.log/GATES-49-OPEN.log/g' gates_run49.sh
    bash gates_run49.sh 1 8 ; 9 20 ; 21 30
    cp pack26/TABLE-FROZEN-SPLIT-SESSION-26.txt rt/     # gate 31 needs it; gates 21-30 delete it
    bash gates_run49.sh 31 45 ; 46 52 ; 53 60 ; 61 71
    diff GATES-48-OPEN.log GATES-49-OPEN.log            # expect ONLY gate 6 `sec` drift
    cd rt && python3 nlterm.py gate ; python3 f392_guard.py ; python3 nlchain.py show
    python3 gate7980.py ; python3 nlcfg.py gate ; python3 nlguard.py gate

Run each segment as its own step (Zeno). **Read every exit code UNPIPED (F44.1)** — a pipe
returns the exit of the last command in it, not of the gate.

Expected at open: census **bad=0**; gate 78 **63/70, FIRST DIVERGENCE 25**; gate 83 **PASS 8/8**
against the s48-restated dict (cfg_score (51,70), ok_score (63,70)); gate 84 PASS 6/6. Gate 83's
`cfg_fail` and `disagree` are **PREFIX-invariant, not chain-length-invariant** — s48 amended the
taxonomy after the Pr/Nd extension falsified the stronger claim. Read the gate's own text.

## State

Chain at **74 rows, Z=2..75**. 4f block CLOSED (61..71), 5d block OPEN (72..75), all at rung 0.
Four prediction files filed before their runs and scored; **PB-5 is the first band in the
project to hold**, and it was the only one filed on mechanism grounds. The promotion mechanism
is NAMED — exchange, 92% of the gap at Pr — and NOT BUILT. **The residue is -8.021 mHa at
Z=59. Residue is not closure.**

Work list is §8 of the bridge. **T4 (R 1701 onward) is LAST and is not opened in a working
session.**
