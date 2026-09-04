#!/usr/bin/env python3
# r3-q5c-measure.py — R3 (Q5 pass 3): the chat-56 batch 2 slip B2-C1 re-derived. Chat 56 left no instrument pack; M ruled
# (RUL-153, pass 2) that the re-run is an instrument of R3's, named as a re-derivation. Λ₈ from the seated tower-2.py,
# imported by path; standard library; deterministic.
#
# The two readings of ω(N(x)) in the divisor embedding N(x) = ∏ pᵢ^{xᵢ}: the number of distinct primes dividing N(x) is
# the number of POSITIVE coordinates, |{i : xᵢ > 0}| (B2-C1's corrected gloss); the gloss the object carried read it as
# the number of NON-MINIMAL coordinates, |{i : xᵢ > minᵢ}|, which drops a floored coordinate (n, k, e ≥ 1) sitting at its
# minimum 1 though it still carries its prime. The slip: max ω = 8 at 100 cells under the first, 96 under the second.
import os, sys, importlib.util, io, contextlib
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('tower2', os.path.join(H, 'tower-2.py')); T2 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(T2)
FAIL = []
def check(tag, got, exp):
    ok = got == exp; print('   %-66s %-26s %s' % (tag, repr(got)[:26], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
L8 = T2.L8(); check('|Λ₈|', len(L8), 976)
mins = [min(x[i] for x in L8) for i in range(8)]
check('the floors: coordinates whose minimum over Λ₈ is 1 (n, k, e)', [i for i, m in enumerate(mins) if m == 1], [0, 2, 4])
pos = {x: sum(1 for v in x if v > 0) for x in L8}
nonmin = {x: sum(1 for i, v in enumerate(x) if v > mins[i]) for x in L8}
check('positive-exponent reading: max ω', max(pos.values()), 8)
check('positive-exponent reading: cells attaining 8', sum(1 for v in pos.values() if v == 8), 100)
check('positive-exponent reading: min ω (three primes divide every N(x))', min(pos.values()), 3)
check('non-minimal reading: cells attaining 8', sum(1 for v in nonmin.values() if v == 8), 96)
diff = sorted(x for x in L8 if pos[x] == 8 and nonmin[x] != 8)
check('the discrepancy is exactly four cells', len(diff), 4)
check('each has a floored coordinate at its minimum 1 and every coordinate positive', all(all(v > 0 for v in x) and any(x[i] == 1 for i in (0, 2, 4)) for x in diff), True)
print('   the four cells:', ' '.join(str(x) for x in diff))
check('the tight cell (2,1,3,3,2,1,3,3): ω = 8 by direct factorisation', pos[(2, 1, 3, 3, 2, 1, 3, 3)], 8)
print('\n   integrity checks: %s' % ('ALL OK' if not FAIL else 'FAILED: ' + '; '.join(FAIL)))
sys.exit(1 if FAIL else 0)
