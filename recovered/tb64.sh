#!/bin/bash
# tb64.sh -- SESSION 64, F63.2 remedy (a): the four tie-break control rows, RE-RUN.
# Sealed instrument, unmodified: rt/nlchain.py restart Z (observed cfg(Z-1) reference).
# Scored later against pack63/PREDICTION-TIEBREAK-CONTROLS.md sha 0b12ef68...
# §2.20: one row at a time, each written before the next begins, resumable, bounded.
# NOTE: output is tbctrl64.jsonl. ctrl64.jsonl is a QUARANTINED name -- never write it.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/tbctrl64.jsonl"
LOG="$HERE/tb64.log"
BUDGET=1800
touch "$OUT"
cd "$HERE/../rt"
for Z in 57 58 89 91; do
  if grep -q "\"Z\": $Z," "$OUT" 2>/dev/null; then
    echo "SKIP Z=$Z (already written)" | tee -a "$LOG"; continue
  fi
  echo "START Z=$Z $(date -u +%FT%TZ) budget=${BUDGET}s" | tee -a "$LOG"
  t0=$(date +%s)
  timeout $BUDGET python3 nlchain.py restart $Z > "$HERE/.row$Z.tmp" 2>>"$LOG"
  rc=$?
  t1=$(date +%s)
  if [ $rc -eq 124 ]; then
    echo "OVERRUN Z=$Z rc=124 after $((t1-t0))s -- NO-DATA, not a fail" | tee -a "$LOG"
    rm -f "$HERE/.row$Z.tmp"; continue
  fi
  if [ $rc -ne 0 ]; then
    echo "ERROR Z=$Z rc=$rc after $((t1-t0))s -- NO-DATA" | tee -a "$LOG"
    rm -f "$HERE/.row$Z.tmp"; continue
  fi
  tail -1 "$HERE/.row$Z.tmp" >> "$OUT"
  rm -f "$HERE/.row$Z.tmp"
  echo "DONE$Z rc=0 $((t1-t0))s $(date -u +%FT%TZ)" | tee -a "$LOG"
done
echo "TB64 COMPLETE $(date -u +%FT%TZ) rows=$(wc -l < "$OUT")" | tee -a "$LOG"
