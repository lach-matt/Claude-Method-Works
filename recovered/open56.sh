#!/bin/bash
# open56.sh -- s57 open. Byte-for-byte pack55/open55.sh except: gates 94,95,96 join the
# smoke list (an unenforced gate is not a gate, s51 precedent) and step 5 names the
# pack56 reference log. F55.4's unique job tag is retained.
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
[ -f rt/prime.py ] && [ -f rt/run.sh ] || FAIL "prime.py / run.sh missing"
echo "=== STEP 3 · THE STATE CARD (PRIME CONTINUITY clause 2) =========="
( cd rt && python3 prime.py ); RC=$?
[ $RC -eq 1 ] && FAIL "prime.py found a REAL fault -- register it against the object"
[ $RC -eq 2 ] && echo "  NOTE: a job ended without an rc. Read its log; recompute ONLY units with no completion line."
echo "=== STEP 4 · SMOKE GATES ========================================="
cd rt || FAIL "no rt"
for g in "python3 nlterm.py gate" "python3 f392_guard.py" "python3 gate7980.py" \
         "python3 nlcfg.py gate" "python3 nlguard.py gate" "python3 gate85.py" \
         "python3 ../pack53/runsealed.py ../pack52/gate86.py" "python3 continuity.py" \
         "python3 ../pack56/gate94.py" "python3 ../pack56/gate95.py"; do
  echo "--- $g"; eval "$g" > /tmp/smoke.$$ 2>&1
  [ $? -eq 0 ] || { tail -5 /tmp/smoke.$$; FAIL "smoke gate failed: $g"; }
  tail -1 /tmp/smoke.$$
done
cd ..
echo "  NOTE: gate 96 is NOT in the smoke list -- it reads /tmp/c3z57.jsonl, which does not"
echo "        survive a fresh extract. pack56/c3z57.jsonl is the sealed copy; re-point it there."
echo "=== STEP 5 · FULL GATE REPLAY, DETACHED ==========================="
TAG=GATES${N}_$(date +%H%M%S)
echo "  launch:  cd rt && bash run.sh $TAG 'bash ../pack55/gates_run55.sh 1 71'"
echo "  poll  :  cd rt && timeout 200 bash run.sh --wait $TAG 180   # BOUNDED. repeat until DONE"
echo "  then  :  diff pack55/GATES-55-OPEN.log /tmp/GATES-55-OPEN.log  # expect ZERO lines"
echo
echo "=== OPEN COMPLETE. Work list is §7 of BRIDGE-LOWDIN-SESSION-56.md ==="