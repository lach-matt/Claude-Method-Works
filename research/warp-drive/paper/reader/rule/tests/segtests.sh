#!/bin/bash
# segments, hand-offs, resume and thread-count independence (P-APPC2). usage: segtests.sh BUILD CFGDIR (from a scratch dir)
B=$1; C=$2
rm -rf s_all s_seq s_t2 r_ref r_kill
$B/rule run $C/tB2.cfg out=s_all 2>/dev/null && $B/rule assemble $C/tB2.cfg out=s_all 2>/dev/null
for s in 0 1 2; do $B/rule run $C/tB2.cfg $s out=s_seq 2>/dev/null; done; $B/rule assemble $C/tB2.cfg out=s_seq 2>/dev/null
cmp s_all/case.txt s_seq/case.txt && diff -q s_all/digests.txt s_seq/digests.txt && echo "PASS segments run one at a time in separate processes == one run"
$B/rule run $C/tB2.cfg out=s_t2 threads=2 batch=3 2>/dev/null && $B/rule assemble $C/tB2.cfg out=s_t2 threads=2 2>/dev/null
cmp s_all/case.txt s_t2/case.txt && diff -q s_all/digests.txt s_t2/digests.txt && echo "PASS tB2: 2 threads, batch 3 == 1 thread, batch 4"
$B/rule run $C/tR2.cfg out=r_ref 2>/dev/null && $B/rule assemble $C/tR2.cfg out=r_ref 2>/dev/null
( $B/rule run $C/tR2.cfg out=r_kill ckpt_minutes=0 2>r_kill.err & P=$!; sleep 6; kill -9 $P; wait $P 2>/dev/null )
echo "killed after 6 s: $(ls r_kill/seg_*/cell_*.bin 2>/dev/null | wc -l) cell files, batch checkpoint present: $(ls r_kill/seg_*/batch.ckpt 2>/dev/null | wc -l)"
$B/rule run $C/tR2.cfg out=r_kill threads=2 2>&1 | grep -m3 "resumed" ; $B/rule assemble $C/tR2.cfg out=r_kill 2>/dev/null
cmp r_ref/case.txt r_kill/case.txt && diff -q r_ref/digests.txt r_kill/digests.txt && echo "PASS tR2: killed mid-batch, resumed with 2 threads == uninterrupted"
