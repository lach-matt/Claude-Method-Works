#!/bin/bash
cd "$1"; man="$2"; bad=0; n=0
grep -v "$man" "$man" | while read h f; do
  if [ ! -f "$f" ]; then echo "MISSING $f"; continue; fi
  a=$(sha256sum "$f" | cut -c1-16); [ "$a" = "$h" ] || echo "MISMATCH $f"
done
echo "$(grep -vc "$man" "$man") entries checked in $1"