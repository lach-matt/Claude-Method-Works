#!/bin/bash
# verify29.sh -- HANDOFF-29 integrity: sha256 of every file against MANIFEST-HANDOFF-29.txt
cd "$(dirname "$0")"; ok=0; bad=0
while read h f; do [ -f "$f" ] && [ "$(sha256sum "$f" | cut -d' ' -f1)" = "$h" ] && ok=$((ok+1)) || { bad=$((bad+1)); echo "BAD $f"; }; done < MANIFEST-HANDOFF-29.txt
echo "HANDOFF-29: ok=$ok bad=$bad"