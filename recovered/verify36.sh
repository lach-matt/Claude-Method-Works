#!/bin/bash
# verify LOWDIN-HANDOFF-36 against MANIFEST-HANDOFF-36.txt
cd "$(dirname "$0")"; ok=0; bad=0
while read h f; do if [ "$(sha256sum "$f" | cut -d' ' -f1)" = "$h" ]; then ok=$((ok+1)); else bad=$((bad+1)); echo "BAD $f"; fi; done < MANIFEST-HANDOFF-36.txt
echo "HANDOFF-36: ok=$ok bad=$bad"