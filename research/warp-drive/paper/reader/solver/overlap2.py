"""prop:appc-overlap at level 0 for a printed approximant with a quantum per block: N-APP1's overlap.py run on the
exact rationals z 10^-p (its single-quantum loader replaced).  usage: overlap2.py case tables_z.pkl i j [kind] out.json"""
import sys, os, json, pickle, types, numpy as np
from fractions import Fraction as Fr
NAPP1 = os.environ.get('NAPP1', '/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/napp1')
sys.path.insert(0, NAPP1)
import overlap as ov

def main():
    a = sys.argv[1:]
    case, zf, i, j = a[0], a[1], int(a[2]) - 1, int(a[3]) - 1
    kind = a[4] if len(a) > 5 else None
    zs = pickle.load(open(zf, 'rb'))
    Z = {k: np.vectorize(lambda q, p=p: Fr(int(q), 10 ** p), otypes=[object])(z) for k, (p, z) in zs.items()}
    class NP(types.ModuleType):
        def __getattr__(self, n): return getattr(np, n)
    fake_np = NP('np'); fake_np.load = lambda fn: Z
    fake_json = types.SimpleNamespace(load=lambda f: {'p': 0}, dump=json.dump)
    ov.np = fake_np; ov.json = fake_json
    open('_ov_%s.json' % case, 'w').write('{}')
    if kind: ov.ONLY['kind'] = kind
    r = ov.overlap(case, i, j, source='_ov')
    json.dump(r, open(a[-1], 'w'), indent=1)

main()
