#!/bin/bash
cd "$(dirname "$0")"; bad=0; ok=0
while read h f; do a=$(sha256sum "$f" 2>/dev/null|cut -c1-16); if [ "$a" = "$h" ]; then ok=$((ok+1)); else echo MISMATCH $f; bad=$((bad+1)); fi; done < <(grep -v MANIFEST-HANDOFF-16 MANIFEST-HANDOFF-16.txt)
echo "HANDOFF-16: ok=$ok bad=$bad"