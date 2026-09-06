#!/bin/bash
# F53.2 CONTROL. Sealed nlchain.py, restart mode, c at its default 137.035999.
# Same reference (OBSERVED config Z-1) as cinf.py, so c is the only difference.
cd "$(dirname "$0")/../rt"
for Z in "$@"; do
  python3 nlchain.py restart $Z 2>&1 | tail -1 >> /tmp/ctrl137.jsonl
  echo "CTRL DONE Z=$Z"
done