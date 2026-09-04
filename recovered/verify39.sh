#!/bin/bash
# HANDOFF-39 verification: SHA256 manifest over every file except the manifest itself.
cd "$(dirname "$0")"
ok=0; bad=0
while read -r h f; do
  [ -f "$f" ] || { echo "MISSING $f"; bad=$((bad+1)); continue; }
  g=$(sha256sum "$f" | cut -d' ' -f1)
  if [ "$g" = "$h" ]; then ok=$((ok+1)); else echo "BAD $f"; bad=$((bad+1)); fi
done < MANIFEST-HANDOFF-39.txt
echo "HANDOFF-39: ok=$ok bad=$bad"