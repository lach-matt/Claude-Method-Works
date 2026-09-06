#!/bin/bash
# verify LOWDIN-HANDOFF-34: run inside the extracted directory
ok=0; bad=0
while read -r h f; do if [ "$(sha256sum "$f" | cut -d' ' -f1)" = "$h" ]; then ok=$((ok+1)); else bad=$((bad+1)); echo "BAD $f"; fi; done < MANIFEST-HANDOFF-34.txt
echo "HANDOFF-34: ok=$ok bad=$bad"