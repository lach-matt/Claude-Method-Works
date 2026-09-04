#!/bin/bash
# seal58.sh -- SEAL TIME.  The expensive proofs live HERE, once, not at every open.
set -u
N=${1:?usage: seal58.sh N}
FAIL(){ echo "!!! SEAL HALTED: $1"; exit 1; }
echo "=== A · FULL GATE REPLAY (proves what is being handed over) ==="
( cd rt && bash run.sh SEAL${N} 'bash ../pack55/gates_run55.sh 1 71' ) || FAIL "replay launch"
echo "  poll: cd rt && timeout 200 bash run.sh --wait SEAL${N} 180   # repeat until DONE"
echo "  then: diff pack55/GATES-55-OPEN.log /tmp/GATES-55-OPEN.log   # expect ZERO lines"
echo "=== B · CANARY REFERENCE ==="
python3 pack58/canary.py --emit || FAIL "canary emit"
echo "=== C · CONDENSE + SEAL ==="
python3 pack58/condense.py ${N} --seal || FAIL "condense halted (declare retirements)"
echo "=== D · FRESH-EXTRACT PROOF ==="
echo "  tar czf LOWDIN-HANDOFF-${N}.tar.gz --exclude=rt --exclude=LOWDIN-HANDOFF-\*.tar.gz ."
echo "  extract elsewhere, then: bash pack58/open58.sh"