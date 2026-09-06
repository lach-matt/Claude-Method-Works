#!/bin/sh
# snapshot: scripts + completed per-Z files + log + manifest -> outputs (overwrites)
cd /home/claude/pack/code
D=/home/claude/snap; rm -rf $D; mkdir -p $D/out
cp step2_run.py step3.py ground.py snap.sh step2.log $D/ 2>/dev/null
cp out/*.tsv $D/out/ 2>/dev/null
N=$(ls $D/out | wc -l); LAST=$(ls $D/out | tail -1)
CELLS=$(cat $D/out/*.tsv | grep -vc '^Z')
{ echo "STEP2 SNAPSHOT $(date -u +%FT%TZ)  Z-files $N  last $LAST  cells $CELLS  (bank 2_13 unchanged; nothing written to index)";
  echo "resume: put out/ beside step2_run.py; python3 step2_run.py 5 120  (skips complete Z)";
  (cd $D && find . -type f | sort | while read f; do printf "%s %s\n" "$(sha256sum "$f" | cut -c1-16)" "$f"; done); } > $D/MANIFEST-STEP2.txt
tar czf /mnt/user-data/outputs/LOWDIN-STEP2-partial.tar.gz -C /home/claude snap
cp $D/MANIFEST-STEP2.txt /mnt/user-data/outputs/
head -1 $D/MANIFEST-STEP2.txt