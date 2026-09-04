#!/bin/bash
# latest-pack census (F36.1 rule): each rt file vs its copy in the highest-numbered pack containing it
ok=0; bad=0; miss=0
for f in rt/*; do b=$(basename "$f"); best=""
  for d in $(ls -d pack*/ | sed 's#/##' | sort -t k -k2 -n) ; do
    for c in "$d/$b" "$d/pack5/$b" "$d/pack5fix/$b"; do [ -f "$c" ] && best="$c"; done
  done
  if [ -z "$best" ]; then miss=$((miss+1)); echo "NOPACK $b"; continue; fi
  if cmp -s "$f" "$best"; then ok=$((ok+1)); else bad=$((bad+1)); echo "BAD $b vs $best"; fi
done
echo "CENSUS-37: ok=$ok bad=$bad nopack=$miss"