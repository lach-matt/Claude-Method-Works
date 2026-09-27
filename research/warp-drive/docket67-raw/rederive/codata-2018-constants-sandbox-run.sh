#!/bin/bash
S=/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/sandbox
v=$1; cd $S/$v/research/warp-drive || exit 9
mkdir -p $S/logs/$v
for f in drivensource tolman candidates nonstatic ledger excite higgs noise branelink achievable spec formation warpfolder hpscentre fewsterteo phase1 seatindex throatmass; do
  timeout 1200 python3 -B $f.py --selftest > $S/logs/$v/$f.log 2>&1; echo "$f $?" >> $S/logs/$v/RC
done
echo DONE >> $S/logs/$v/RC
