#!/bin/bash
ok=0; bad=0
while read h f; do g=$(sha256sum "$f" 2>/dev/null | cut -c1-16); if [ "$g" = "$h" ]; then ok=$((ok+1)); else bad=$((bad+1)); echo "BAD $f"; fi; done < MANIFEST-HANDOFF-18.txt
echo "HANDOFF-18: ok=$ok bad=$bad"