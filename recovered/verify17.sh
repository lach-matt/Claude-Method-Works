#!/bin/sh
# verify17.sh -- run from inside LOWDIN-HANDOFF-17/: checks every file against MANIFEST-HANDOFF-17.txt (sha256 prefix 16)
ok=0; bad=0
while read h f; do
  g=$(sha256sum "$f" 2>/dev/null | cut -c1-16)
  if [ "$g" = "$h" ]; then ok=$((ok+1)); else bad=$((bad+1)); echo "BAD $f"; fi
done < MANIFEST-HANDOFF-17.txt
echo "HANDOFF-17: ok=$ok bad=$bad"