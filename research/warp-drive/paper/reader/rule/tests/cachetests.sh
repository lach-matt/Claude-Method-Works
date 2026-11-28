#!/bin/bash
# damaged caches (from an empty scratch dir): BUILD CFGDIR.  A truncated or corrupted cell file must be rejected and the
# cell recomputed; a damaged batch checkpoint ignored; a damaged hand-off or element file a clean error, not a crash.
B=$1; C=$2; CF=$C/tB2.cfg; ok=0; bad=0
pass() { echo "PASS $*"; ok=$((ok+1)); }; fail() { echo "FAIL $*"; bad=$((bad+1)); }
$B/rule run $CF out=ref >/dev/null 2>&1 && $B/rule assemble $CF out=ref >/dev/null 2>&1 || { echo "reference run failed"; exit 1; }
cellf=seg_00/cell_0001_0001.bin; n=$(stat -c %s ref/$cellf)
k=0
for off in 0 1 8 73 100 1000 $((n / 2)) $((n - 65)) $((n - 64)) $((n - 1)) flip; do
  k=$((k+1)); d=t$k; cp -r ref $d
  if [ $off = flip ]; then python3 -c "import sys; f=open(sys.argv[1],'r+b'); f.seek($n//2); c=f.read(1); f.seek($n//2); f.write(bytes([c[0]^1])); f.close()" $d/$cellf
  else truncate -s $off $d/$cellf; fi
  $B/rule run $CF out=$d > $d.log 2>&1; r=$?; $B/rule assemble $CF out=$d >> $d.log 2>&1; r2=$?
  if [ $r -eq 0 ] && [ $r2 -eq 0 ] && cmp -s ref/case.txt $d/case.txt && diff -q ref/digests.txt $d/digests.txt >/dev/null && grep -q "rejected" $d.log; then
    pass "cell file cut at $off of $n bytes: rejected, recomputed, output identical"
  else fail "cell file cut at $off of $n bytes (run exit $r, assemble exit $r2)"; fi
done
# a damaged batch checkpoint: stop after outer step 1 of the first batch, then cut its checkpoint
RULE_STOP_AFTER_OUTER=1 $B/rule run $CF out=ck ckpt_minutes=0 >/dev/null 2>&1
ck=ck/seg_00/batch.ckpt; m=$(stat -c %s $ck 2>/dev/null || echo 0)
for off in 0 5 80 $((m / 2)) $((m - 1)) whole; do
  d=ck_$off; cp -r ck $d; [ $off = whole ] || truncate -s $off $d/seg_00/batch.ckpt
  $B/rule run $CF out=$d > $d.log 2>&1; r=$?; $B/rule assemble $CF out=$d >> $d.log 2>&1
  want=ignored; [ $off = whole ] && want=resumed
  if [ $r -eq 0 ] && cmp -s ref/case.txt $d/case.txt && grep -q "$want" $d.log; then pass "batch checkpoint ($off of $m bytes): $want, output identical"
  else fail "batch checkpoint ($off of $m bytes): run exit $r"; fi
done
# a damaged hand-off and element file: a clean exit 1 with a message
cp -r ref h; truncate -s 1000 h/handoff_00.bin; $B/rule run $CF 1 out=h > h.log 2>&1; r=$?
[ $r -eq 1 ] && grep -q "hand-off 0" h.log && pass "hand-off cut short: clean error (exit 1)" || fail "hand-off cut short: exit $r"
cp -r ref e; truncate -s 2000 e/elem_01.bin; $B/rule assemble $CF out=e > e.log 2>&1; r=$?
[ $r -eq 1 ] && grep -q "element file 1" e.log && pass "element file cut short: clean error (exit 1)" || fail "element file cut short: exit $r"
echo "cachetests: $ok passed, $bad failed"
