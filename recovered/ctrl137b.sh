#!/bin/bash
# s59 NR-1 CONTROL. Same invocation as the sealed pack53/ctrl137.sh, different Z set
# and a per-row checkpoint file (Zeno). Sealed nlchain.py, restart mode, c default.
cd "$(dirname "$0")/../rt"
OUT=../pack59/ctrl137b.jsonl
: > $OUT
for Z in "$@"; do
  python3 nlchain.py restart $Z 2>&1 | tail -1 >> $OUT
  echo "CTRL DONE Z=$Z $(date -u +%H:%M:%SZ)" >> ../pack59/ctrl137b.progress
done
echo "ALL DONE" >> ../pack59/ctrl137b.progress