"""tbstep.py -- SESSION 64. A RESUMABLE restart-mode step. §2.20 at channel granularity.

WHY THIS EXISTS. `nlchain.py restart Z` is one indivisible process per row. At Z=89 and
Z=91 it exceeds the wall-clock a single call in this container gets, and is killed
part-way with every converged channel thrown away (F64.2). This driver divides the row
into its channels, writes each channel's result before the next begins, and on a rerun
costs only what has not succeeded. That is the prime directive applied one level down.

WHAT IT DOES NOT DO. It does not touch the instrument. It calls the SAME sealed
functions -- nlchain.candidates, nlchain.add, nlchain.tagof, nlguard.run_guarded,
ground.expand -- with the same arguments in the same order, and assembles the record
with the same expressions as nlchain.step. `nlchain.py` is not edited or sed-ed (rule 4).

CAN-FAIL / CONTROL. It is not used on a row until it has REPRODUCED `nlchain.py restart`
bit-for-bit on a row that instrument already returned (Z=57, Z=58), every field but the
two named below. If it cannot reproduce those, it is not an instrument and is discarded.

TWO FIELDS DIFFER BY CONSTRUCTION AND ARE EXCLUDED FROM THAT COMPARISON:
  sec     -- in nlchain.step this is the wall time of one process. Here it is the SUM of
             compute seconds over the channels, which may be spread across several calls.
  driver  -- present here, absent there. Provenance (§2.11); a resumed row must say so.

usage: python3 tbstep.py Z [--budget SECONDS]
       Runs missing channels until the budget is spent, writing the cache as it goes.
       Prints the assembled row to stdout ONLY when every channel is resolved.
       Otherwise prints PARTIAL and the count remaining, and exits 3.
"""
import sys, os, json, time

os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import hfc2 as H
import ground as G
import nlguard as NG
import nlchain as C
H.CORR = False

HERE = os.path.dirname(os.path.abspath(__file__))


def cache_path(Z):
    return os.path.join(HERE, f".cache_Z{Z}.json")


def load_cache(Z):
    p = cache_path(Z)
    return json.load(open(p)) if os.path.exists(p) else {}


def save_cache(Z, c):
    p = cache_path(Z)
    json.dump(c, open(p + '.tmp', 'w'))
    os.replace(p + '.tmp', p)          # atomic: a killed write cannot corrupt the cache


def main():
    Z = int(sys.argv[1])
    budget = 1800
    if '--budget' in sys.argv:
        budget = int(sys.argv[sys.argv.index('--budget') + 1])
    t_start = time.time()

    cfg_prev = G.expand(Z - 1)                       # restart mode: OBSERVED cfg(Z-1)
    cands = C.candidates(cfg_prev)
    cache = load_cache(Z)

    # --- the reference: cation of element Z carrying Z-1 electrons (F40.1) ---
    if 'ref' not in cache:
        t1 = time.time()
        gr = NG.run_guarded(Z, cfg_prev, 'ref')
        if not gr['conv']:
            print(f"NO-DATA Z={Z}: reference did not converge -- {gr['err']}")
            sys.exit(4)
        cache['ref'] = dict(E=gr['E'], it=gr['it'], rung=gr['rung'], sec=int(time.time() - t1))
        save_cache(Z, cache)
        print(f"    {Z} ref E={gr['E']} it={gr['it']} rung={gr['rung']}", flush=True)
    Eref = cache['ref']['E']

    # --- the channels, one at a time, written before the next begins ---
    for c in cands:
        tag = C.tagof(c)
        if tag in cache:
            continue
        if time.time() - t_start > budget:
            break
        t1 = time.time()
        g = NG.run_guarded(Z, C.add(cfg_prev, c), tag)
        if g['conv']:
            cache[tag] = dict(nl=list(c), D=round(g['E'] - Eref, 5), it=g['it'],
                              rung=g['rung'], sec=int(time.time() - t1))
        else:
            cache[tag] = dict(nl=list(c), D=None, err=g['err'], rung=g['rung'],
                              sec=int(time.time() - t1))
        save_cache(Z, cache)
        print(f"    {Z} {tag:>3} {cache[tag].get('D')} rung {cache[tag].get('rung')}", flush=True)

    missing = [C.tagof(c) for c in cands if C.tagof(c) not in cache]
    if missing:
        print(f"PARTIAL Z={Z} remaining={len(missing)} {missing}")
        sys.exit(3)

    # --- assembly, expression for expression as nlchain.step ---
    D = {C.tagof(c): cache[C.tagof(c)] for c in cands}
    ok = {k: v for k, v in D.items() if v.get('D') is not None}
    if not ok:
        print(f"NO-DATA Z={Z}: no channel converged")
        sys.exit(4)
    win = min(ok, key=lambda k: ok[k]['D'])
    srt = sorted(ok, key=lambda k: ok[k]['D'])
    marg = round(ok[srt[1]]['D'] - ok[srt[0]]['D'], 5) if len(srt) > 1 else None
    try:
        rec = ''.join(f"{n}{'spdfg'[l]}{k}" for n, l, k in G.expand(Z))
        cz = {(n, l): k for n, l, k in G.expand(Z)}
        cz1 = {(n, l): k for n, l, k in G.expand(Z - 1)}
        recent = [nl for nl in cz if cz[nl] > cz1.get(nl, 0) + 1e-9] if Z > 1 else []
        rectag = C.tagof(recent[0]) if len(recent) == 1 else None
        prov = 'OBSERVED'
    except (KeyError, IndexError):
        rec, rectag, prov = None, None, ('SYNTHESISED-UNMEASURED' if Z <= 118 else 'PREDICTED-UNSYNTHESISED')
    total_sec = cache['ref']['sec'] + sum(v['sec'] for v in D.values())
    o = dict(Z=Z, mode='restart', ent=win, ent_nl=ok[win]['nl'], D_ent=ok[win]['D'], margin=marg,
             order=[[k, ok[k]['D']] for k in srt], nfail=len(D) - len(ok),
             fail={k: v['err'] for k, v in D.items() if v.get('D') is None},
             ref_cfg=''.join(f"{n}{'spdfg'[l]}{k}" for n, l, k in cfg_prev),
             rec_ent=rectag, rec_cfg=rec, prov=prov,
             label=('PREDICTED-BY-FIELD' if prov != 'OBSERVED' else 'CHAIN'),
             ok=(rectag == win) if rectag else None, it_ref=cache['ref']['it'], sec=total_sec,
             rung_ref=cache['ref']['rung'],
             chan={k: dict(it=v.get('it'), rung=v.get('rung')) for k, v in D.items()},
             rungs=sorted({v.get('rung') for v in D.values()} | {cache['ref']['rung']}),
             guard='nlguard LADDER=' + repr(NG.LADDER),
             driver='pack64/tbstep.py resumable per-channel; sec is summed compute time')
    print(json.dumps(o))


if __name__ == '__main__':
    main()
