#!/bin/bash
for d in LOWDIN-HANDOFF-6 LOWDIN-PACK-7 LOWDIN-PACK-8 LOWDIN-PACK-9; do
  m=$(ls $d/MANIFEST* 2>/dev/null|head -1)
  [ -z "$m" ] && { echo "$d: no manifest"; ls $d; continue; }
  ok=0; bad=0; tot=0
  while read h f; do
    [ -z "$f" ] && continue; tot=$((tot+1))
    if [ -f "$d/$f" ]; then a=$(sha256sum "$d/$f"|cut -c1-${#h}); [ "$a" = "$h" ] && ok=$((ok+1)) || { bad=$((bad+1)); echo "  MISMATCH $f"; }
    else bad=$((bad+1)); echo "  MISSING $f"; fi
  done < <(grep -E '^[0-9a-f]{8,}' $m)
  echo "$d ($m): $ok/$tot ok, $bad bad"
done