#!/bin/bash
# verify31.sh -- HANDOFF-31 integrity: sha256 of every file against MANIFEST-HANDOFF-31.txt
cd "$(dirname "$0")"; ok=0; bad=0
while read h f; do [ -f "$f" ] && [ "$(sha256sum "$f" | cut -d' ' -f1)" = "$h" ] && ok=$((ok+1)) || { bad=$((bad+1)); echo "BAD $f"; }; done < MANIFEST-HANDOFF-31.txt
echo "HANDOFF-31: ok=$ok bad=$bad"