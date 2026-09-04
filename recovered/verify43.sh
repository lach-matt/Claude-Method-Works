#!/bin/bash
# verify43.sh -- HANDOFF-43. TWO HALVES, because s43's F43.1 proved one is not enough.
#
# HALF A (integrity, as every prior verifyN.sh): every file the manifest LISTS is present
#         and hashes correctly.
# HALF B (completeness, NEW -- gate 81): every file in the TREE appears in the manifest.
#
# F43.1: an unsealed pack43 sat in the tree through a full session-open. verify42.sh
# reported ok=909 bad=0 and was RIGHT -- sha256sum -c reports on what the manifest admits.
# An unlisted file does not fail the check; it fails to be a file. That is R 1671's fault
# class reaching the verifier itself. Half B is the repair.
#
# Can-fail test: `touch pack43/PLANTED && bash verify43.sh` must report EXTRA=1 and exit 1.
cd "$(dirname "$0")"
M=MANIFEST-HANDOFF-43.txt

OK=$(sha256sum -c "$M" 2>/dev/null | grep -c ': OK$')
BAD=$(sha256sum -c "$M" 2>/dev/null | grep -c ': FAILED$')

# Half B: tree minus manifest. rt/ and __pycache__ are BUILD ARTEFACTS, excluded by
# construction (the archive ships packs, not a runtime) -- named here so the exclusion is
# a stated choice and not a silent default (§2.9).
find . -type f ! -name "$M" ! -path './rt/*' ! -path '*/__pycache__/*' \
  | sed 's|^\./||' | sort > /tmp/_tree43
awk '{sub(/^[^ ]+  /,""); print}' "$M" | sort > /tmp/_man43
EXTRA=$(comm -23 /tmp/_tree43 /tmp/_man43 | tee /tmp/_extra43 | wc -l)

echo "HANDOFF-43: ok=$OK bad=$BAD extra=$EXTRA"
if [ "$EXTRA" -ne 0 ]; then
  echo "--- UNSEALED FILES IN TREE (F43.1 class) ---"
  cat /tmp/_extra43
fi
[ "$BAD" -eq 0 ] && [ "$EXTRA" -eq 0 ]
