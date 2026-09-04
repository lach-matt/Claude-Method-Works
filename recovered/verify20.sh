#!/bin/bash
ok=0; bad=0
while read h f; do g=$(sha256sum "$f" 2>/dev/null | cut -c1-16); if [ "$g" = "$h" ]; then ok=$((ok+1)); else bad=$((bad+1)); echo "BAD $f"; fi; done < MANIFEST-HANDOFF-20.txt
echo "HANDOFF-20: ok=$ok bad=$bad"