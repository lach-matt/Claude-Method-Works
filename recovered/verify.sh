#!/bin/bash
dir=$1; man=$2
cd "$dir"; ok=0; bad=0
while read h f; do
  a=$(sha256sum "$f" 2>/dev/null | cut -c1-16)
  if [ "$a" = "$h" ]; then ok=$((ok+1)); else bad=$((bad+1)); echo "MISMATCH $f"; fi
done < <(grep -v "$(basename $man)" "$man")
echo "$(basename $dir): ok=$ok bad=$bad"