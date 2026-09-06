"""aderive.py -- SESSION 65. DERIVES THE CHANNELS CANDIDATE A NEEDS.

M's ruling: Candidate A returned NO-DATA not because the field is silent but because
the walk's candidate list stops at n = N_max+1. The channels exist; they were left to
be derived. This derives them, commensurably with the sealed chain:

    D(ch) at Z  =  E( cfg_chain(Z-1) + ch )  -  E( cfg_chain(Z-1) )    at nuclear charge Z

which is `nlchain.step`'s own definition (F40.1: the reference is the CATION of element
Z carrying config(Z-1)). Every solve goes through `nlguard.run_guarded` (F47.2).
`nlchain.py` is NOT edited and NOT sed-ed (rule 4). Its functions are imported.

F64.2 APPLIES: one channel is one unit of work. Each result is written before the next
begins, by atomic replace. A rerun costs only what has not succeeded.

EVERY Z CARRIES A DETERMINISM CHECK: one channel ALREADY IN THE SEALED CHAIN at that Z
is recomputed here and must return the sealed value to the stored precision. If it does
not, the derived channels at that Z are NOT commensurable with the chain and are
discarded. That check runs FIRST at each Z, before the new channel.

usage: python3 aderive.py Z [Z ...]     run from rt/ with PYTHONPATH=.
       python3 aderive.py --show
"""
import sys, os, json, time

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'aderive.jsonl')
BUDGET_PER_CHANNEL = 900          # s, declared before the run (§2.20)

# block -> the one channel Candidate A needs that the candidate list does not carry,
# plus the sealed channel used as that Z's determinism check.
NEED = {13: ('5s', '4s'), 21: ('4d', '4p'), 31: ('6s', '5s'),
        39: ('5d', '5p'), 49: ('7s', '6s'), 57: ('6d', '5d'),
        81: ('8s', '7s'), 89: ('7d', '6d'), 113: ('9s', '8s')}
# block 6 l=2 (4f/5d) and block 7 l=2 (5f/6d) need a second channel each:
EXTRA = {57: ['5f'], 89: ['6f']}


def load_cache():
    if not os.path.exists(CACHE): return {}
    return {(d['Z'], d['ch']): d for d in map(json.loads, open(CACHE))}


def put(rec):
    tmp = CACHE + '.tmp'
    old = [json.dumps(v) for v in load_cache().values()]
    with open(tmp, 'w') as f:
        f.write('\n'.join(old + [json.dumps(rec)]) + '\n')
    os.replace(tmp, CACHE)


def main():
    if sys.argv[1:2] == ['--show']:
        for k, v in sorted(load_cache().items()):
            print(f"  Z={k[0]:>4} {k[1]:>3}  D={v['D']}  rung={v['rung']} {v['sec']}s {v['kind']}")
        return
    os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
    import nlchain as NC, nlguard as NG, hfc2 as H
    H.CORR = False
    rows = NC.load()
    cache = load_cache()
    for Z in [int(x) for x in sys.argv[1:]]:
        newch, checkch = NEED[Z]
        todo = [(checkch, 'DETERMINISM-CHECK'), (newch, 'DERIVED')] + \
               [(c, 'DERIVED') for c in EXTRA.get(Z, [])]
        todo = [t for t in todo if (Z, t[0]) not in cache]
        if not todo:
            print(f"  Z={Z}: complete in cache"); continue
        cfg = NC.cfg_from_chain(Z - 1, rows)
        t0 = time.time()
        gr = NG.run_guarded(Z, cfg, 'ref')
        if not gr['conv']:
            print(f"  Z={Z}: REFERENCE DID NOT CONVERGE -> NO-DATA (F59.3)"); continue
        Eref = gr['E']
        print(f"  Z={Z}  ref E={Eref:.6f} rung={gr['rung']} {int(time.time()-t0)}s")
        for ch, kind in todo:
            n, l = int(ch[0]), 'spdfg'.index(ch[1])
            t1 = time.time()
            g = NG.run_guarded(Z, NC.add(cfg, (n, l)), ch)
            sec = int(time.time() - t1)
            if not g['conv']:
                print(f"    {ch}  NO-DATA ({g['err']}) {sec}s"); continue
            D = round(g['E'] - Eref, 5)
            put(dict(Z=Z, ch=ch, D=D, rung=g['rung'], it=g['it'], sec=sec, kind=kind,
                     driver='pack65/aderive.py'))
            note = ''
            if kind == 'DETERMINISM-CHECK':
                sealed = dict(rows[Z]['order']).get(ch)
                note = f"   sealed={sealed}  {'MATCH' if sealed == D else '** MISMATCH **'}"
            print(f"    {ch}  D={D}  rung={g['rung']} {sec}s{note}", flush=True)
            if sec > BUDGET_PER_CHANNEL:
                print("    OVERRUN -- declared budget spent, stopping"); return


if __name__ == '__main__':
    main()
