#!/bin/bash
# tests of the review fixes (from a scratch dir): BUILD CFGDIR REFPY RHS
B=$1; C=$2; PY=$3; export RULE_RHS=$4; ok=0; bad=0
pass() { echo "PASS $*"; ok=$((ok+1)); }; fail() { echo "FAIL $*"; bad=$((bad+1)); }
rm -rf f_*
# 1. batch=0 is rejected at once (it used to loop forever)
timeout 20 $B/rule run $C/tA2.cfg out=f_b0 batch=0 >/dev/null 2>&1; r=$?; [ $r -ne 0 ] && [ $r -ne 124 ] && pass "batch=0 rejected (exit $r)" || fail "batch=0 (exit $r)"
# 2. an exact zero defect: N_o entries of max|r| (= 0), C++ = Python
$B/rule cells $C/tZ.cfg out=f_z 2>/dev/null; python3 $PY $C/tZ.cfg f_zpy 2>/dev/null
diff -q f_z/cells.dump f_zpy.dump >/dev/null && [ $(grep -c "max|r| cell (0,0) outer" f_z/cells.dump) -eq 4 ] && pass "zero defect: 4 zero entries, C++ = Python" || fail "zero defect: C++ and Python differ"
# 3. resume at a zero defect: stop after outer step 2 of the first batch, resume with 2 threads
RULE_STOP_AFTER_OUTER=2 $B/rule cells $C/tZ.cfg out=f_zr ckpt_minutes=0 >/dev/null 2>&1; s=$?
$B/rule cells $C/tZ.cfg out=f_zr threads=2 2>/dev/null
[ $s -eq 9 ] && diff -q f_zr/cells.dump f_z/cells.dump >/dev/null && pass "zero defect: stopped after step 2 and resumed == uninterrupted" || fail "zero-defect resume (stop exit $s)"
# 4. resume on ordinary data: stop after outer step 2, resume with 2 threads; C++ = Python
RULE_STOP_AFTER_OUTER=2 $B/rule cells $C/tA2.cfg out=f_ar ckpt_minutes=0 >/dev/null 2>&1; s=$?
$B/rule cells $C/tA2.cfg out=f_ar threads=2 2>/dev/null; python3 $PY $C/tA2.cfg f_apy 2>/dev/null
[ $s -eq 9 ] && diff -q f_ar/cells.dump f_apy.dump >/dev/null && pass "tA2: stopped after step 2, resumed with 2 threads == Python (uninterrupted)" || fail "tA2 resume (stop exit $s)"
# 5. the element lines' order does not matter: blocks in increasing (i, j)
for t in tB2 tB2rev; do $B/rule run $C/$t.cfg out=f_$t 2>/dev/null; $B/rule assemble $C/$t.cfg out=f_$t 2>/dev/null; done
cmp -s f_tB2/case.txt f_tB2rev/case.txt && diff -q <(grep -v "^#" f_tB2/digests.txt) <(grep -v "^#" f_tB2rev/digests.txt) >/dev/null && pass "element lines in reverse order give the same canonical string and digests" || fail "element order"
echo "fixtests: $ok passed, $bad failed"
