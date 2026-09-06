#!/bin/bash
# verify53.sh -- BOTH HALVES (F43.1). Half one: every manifest line still hashes.
# Half two: COMPLETENESS -- no file present in the tree is missing from the manifest.
cd "$(dirname "$0")"
ok=0; bad=0
while read -r h p; do
  [ -f "$p" ] || { echo "MISSING $p"; bad=$((bad+1)); continue; }
  a=$(sha256sum "$p" | cut -d' ' -f1)
  if [ "$a" = "$h" ]; then ok=$((ok+1)); else echo "HASH $p"; bad=$((bad+1)); fi
done < <(sed 's/  /\t/' MANIFEST-HANDOFF-53.txt | awk -F'\t' '{print $1" "$2}')
extra=$(comm -13 <(awk '{ $1=""; sub(/^ /,""); print }' MANIFEST-HANDOFF-53.txt | sort) \
                 <(find . -type f ! -path './rt/*' ! -name 'MANIFEST-HANDOFF-53.txt' | sort) | wc -l)
echo "HANDOFF-53: ok=$ok bad=$bad extra=$extra"
[ $bad -eq 0 ] && [ "$extra" -eq 0 ]