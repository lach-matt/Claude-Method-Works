# Verifier for Deliverable 1's numeric claims. CAN-FAIL: flip any expectation -> FAIL.
import sys, os
sys.path.insert(0, '/home/claude/s52/LOWDIN-HANDOFF-51/rt')
os.chdir('/home/claude/s52/LOWDIN-HANDOFF-51/rt')
import nlcfg, nlchain as NC
rows = NC.load(); col = nlcfg.column(rows); s = nlcfg.scores(col)
mis = set(s['cfg_fail']); okf = list(s['ok_fail'])
C = []
def c(name, got, exp): C.append((name, got == exp, got, exp))
c('cfg_score', s['cfg_score'], (73, 107))
c('ok_score',  s['ok_score'],  (96, 107))
c('cfg_first', s['cfg_first'], 24)
c('ok_first',  s['ok_first'],  25)
c('str_mismatch', s['str_mismatch'], [])
c('n_cfg_fail', len(mis), 34)
c('n_ok_fail',  len(okf), 11)
c('overlap',    sorted(mis & set(okf)), [47, 96, 103])
c('n_disagree', len(s['disagree']), 39)
c('cfg_only',   len(mis - set(okf)), 31)
c('ok_only',    len(set(okf) - mis), 8)
c('every_okfail_preceded_by_cfgfail', all((z-1) in mis for z in okf), True)
c('converse_fails', len([z for z in mis if (z+1) not in okf]), 23)
c('Gd64_cfg_ok', 64 not in mis, True)
c('Gd64_ok_fail', 64 in okf, True)
c('4f_run_split', sorted(z for z in mis if 57 <= z <= 71),
  [59,60,61,62,63,65,66,67,68,69,70])
c('5f_run', sorted(z for z in mis if 89 <= z <= 103), list(range(91,104)))
c('rows_119', len(rows), 119)
c('derivation_107', len([z for z in col if z <= 108]), 107)
bad = [x for x in C if not x[1]]
for n, ok, got, exp in C:
    if not ok: print('  FAIL %-34s got=%r exp=%r' % (n, got, exp))
print('DELIVERABLE-1 CHECK: %s -- %d/%d clauses' %
      ('PASS' if not bad else 'FAIL', len(C)-len(bad), len(C)))
sys.exit(1 if bad else 0)