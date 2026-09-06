#!/bin/bash
# open58.sh -- THE OPEN, CONDENSED.  s58, on M's ruling.
#
# THE RULE THIS ENCODES:
#   ACCEPT THE HANDOFF AS SEALED.  PICK UP WHERE THE LAST SESSION ENDED.
#   DO NOT RE-PROVE THE CHAIN AT EVERY OPEN.
#
# What s57's open did, and what it cost, every session:
#     manifest verify        1140 files, both halves
#     smoke gates            13 serial, incl. nlguard 94s + gate7980 23s
#     full replay 1..71      ~3 min detached + poll cycles
#   The replay and the manifest are REDUNDANT WITH EACH OTHER.  Identical bytes
#   plus deterministic code give identical output; the hash already proved the
#   bytes.  The replay's only unique job -- catching compiler/interpreter drift --
#   is done by ONE canary in ~1 s.
#
# What this does instead:
#     STEP 1  seal      current manifest only.  History lives in LINEAGE.txt.
#     STEP 2  runtime   rebuild rt/ from sealed packs.
#     STEP 3  canary    environment drift, ~1 s.
#   Total: seconds, not minutes.  The full replay runs ONCE, at SEAL time
#   (pack58/seal58.sh), where it belongs -- proving what is being handed over,
#   not re-proving what was already handed over.
#
# ESCALATION: if the canary reports DRIFT, and only then, run the full replay.
set -u
FAIL(){ echo; echo "!!! OPEN HALTED: $1"; echo "Fix before any work."; exit 1; }
N=$(ls -d pack* 2>/dev/null | sed 's/pack//' | sort -n | tail -1)

echo "=== STEP 1 · SEAL (current only) ================================="
python3 pack58/condense.py ${N} --check || FAIL "seal check failed"

echo "=== STEP 2 · RUNTIME ============================================="
if [ ! -f rt/nlchain.jsonl ]; then
  mkdir -p rt && cp -r pack5/. rt/ && cp pack7/pack5/*.py rt/ && cp -r pack8/pack5fix/. rt/
  cp pack9/*.py pack9/*.jsonl rt/ && cp pack10/* rt/ && cp pack12/*.py pack13/*.py rt/
  cp pack16/*.py pack16/*.jsonl rt/ && cp pack17/*.py pack17/*.jsonl pack17/*.c rt/
  cp pack18/*.py pack18/*.jsonl pack18/*.c rt/
  for n in $(seq 19 $N); do for e in py jsonl c json sh; do ls pack$n/*.$e >/dev/null 2>&1 && cp pack$n/*.$e rt/; done; done
  ( cd rt && for k in shoot shoot_sr shoot_x; do gcc -O2 -shared -fPIC -o lib$k.so $k.c || exit 1; done ) \
    || FAIL "kernel compile failed"
fi
[ -f rt/prime.py ] && [ -f rt/run.sh ] || FAIL "prime.py / run.sh missing"
( cd rt && python3 prime.py 2>&1 | tail -3 )

echo "=== STEP 3 · CANARY (environment drift) =========================="
python3 pack58/canary.py || FAIL "environment drift -- NOW run pack55/gates_run55.sh 1 71"

echo
echo "=== OPEN COMPLETE ================================================"
echo "  The chain is sealed and the environment reproduces it."
echo "  Do NOT re-verify history. Work list is §6 of the s58 bridge."
echo
echo "  STANDING (s58):"
echo "    * Seal:     python3 pack58/condense.py N --seal   (never sed a verify script)"
echo "    * Retire:   undeclared removals HALT the seal. Declare in pack<N>/RETIRE.txt."
echo "    * Surveys:  counts, sets, diffs -- pack57/rd.py. Never a row dump."
echo "    * Replay:   at SEAL time only, or when the canary reports DRIFT."
