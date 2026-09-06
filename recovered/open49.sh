#!/bin/bash
# open49.sh -- THE ENFORCED SESSION OPEN. Written at s49 close so that s50 and every session
# after it CANNOT repeat s49's four faults. Run it from the archive root, first thing.
#
#   bash open49.sh
#
# It refuses to continue past a failed step. Each step is a bounded Zeno segment and the long
# one is DETACHED, so no tool-call timeout can orphan it (PRIME CONTINUITY clause 3).
set -u
FAIL(){ echo; echo "!!! OPEN HALTED: $1"; echo "Fix this before any work. Do not proceed."; exit 1; }
N=$(ls -d pack* 2>/dev/null | sed 's/pack//' | sort -n | tail -1)
echo "=== STEP 1 · SEALS ==============================================="
bash verify${N}.sh || FAIL "manifest verify failed -- BOTH halves must be clean (F43.1)"

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
[ -f rt/prime.py ] && [ -f rt/run.sh ] || FAIL "prime.py / run.sh missing -- the directives are not enforceable without them"

echo "=== STEP 3 · THE STATE CARD (PRIME CONTINUITY clause 2) =========="
echo "NOTHING may be said about state until this prints. Speak only from it."
( cd rt && python3 prime.py ); RC=$?
[ $RC -eq 1 ] && FAIL "prime.py found a REAL fault -- register it against the object"
[ $RC -eq 2 ] && echo "  NOTE: a job ended without an rc. Read its log; recompute ONLY units with no completion line."

echo "=== STEP 4 · SMOKE GATES (one per kernel + every chain gate) ====="
cd rt || FAIL "no rt"
for g in "python3 nlterm.py gate" "python3 f392_guard.py" "python3 gate7980.py" \
         "python3 nlcfg.py gate" "python3 nlguard.py gate" "python3 continuity.py"; do
  echo "--- $g"; eval "$g" > /tmp/smoke.$$ 2>&1
  [ $? -eq 0 ] || { tail -5 /tmp/smoke.$$; FAIL "smoke gate failed: $g"; }
  tail -1 /tmp/smoke.$$
done
cd ..

echo "=== STEP 5 · FULL GATE REPLAY, DETACHED ==========================="
echo "The full 1..71 replay is NOT held in a tool call. It is launched and polled."
cp pack${N}/gates_run*.sh gates_runNEXT.sh 2>/dev/null
echo "  launch:  cd rt && bash run.sh GATES 'cd .. && bash gates_runNEXT.sh 1 71'"
echo "  poll  :  cd rt && bash run.sh --wait GATES 110"
echo "  then  :  diff pack${N}/GATES-*-OPEN.log <newlog>   # expect zero, gate 6 sec excluded"
echo
echo "=== OPEN COMPLETE. Work list is §8 of the bridge. ==================="
