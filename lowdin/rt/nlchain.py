"""nlchain.py -- s40: THE SELF-DRIVING WALK. SPEC-CHAIN-SESSION-40 §2.
config(Z+1) = config(Z) + one electron in the channel c minimising E_HF(config(Z)+c), on the ruling field
(hfc2, SR, CORR=False). Reference is the PREVIOUS NEUTRAL. Nothing is read from ground.py except the seed
and the comparison column. Works above Z=108 where ground.py raises KeyError.
D_chain(c) = E_HF(config(Z)+c) - E_HF(config(Z)); negative = bound; entrant = argmin.
Candidate rule (SPEC §4, CHOSEN): occ(c) < 2(2l+1), n <= N+1, 0 <= l <= min(n-1,4), N = max n occupied.
usage: python3 nlchain.py Zstart Zstop      appends nlchain.jsonl (key Z). No constant.
       python3 nlchain.py restart Z         one step from OBSERVED config(Z-1) (per-element test, not chained)
       python3 nlchain.py show              print the chain table so far
"""
import sys, os, json, time
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
import hfc2 as H
from t7c_kernel import C0
import ground as G
import nlguard as NG          # s48: F47.2 repair wired into the chain itself
H.CORR = False

OUT = 'nlchain.jsonl'
CAP = lambda l: 2 * (2 * l + 1)
def tagof(c): return f"{c[0]}{'spdfg'[c[1]]}"


def load():
    if not os.path.exists(OUT): return {}
    return {d['Z']: d for d in map(json.loads, open(OUT))}


def cfg_from_chain(Z, rows):
    """configuration at Z as list of (n,l,occ), built from the chain's own choices"""
    d = {(1, 0): 1}                      # seed: config(1) = 1s  (SPEC §3, CHOSEN)
    for z in range(2, Z + 1):
        if z not in rows: raise KeyError(f"chain has no step at Z={z}")
        n, l = rows[z]['ent_nl']
        d[(n, l)] = d.get((n, l), 0) + 1
    return [(n, l, k) for (n, l), k in sorted(d.items())]


def candidates(cfg):
    d = {(n, l): k for n, l, k in cfg}
    N = max(n for n, l, k in cfg)
    out = []
    for n in range(1, N + 2):
        for l in range(0, min(n - 1, 4) + 1):
            if d.get((n, l), 0) < CAP(l) - 1e-9:
                out.append((n, l))
    return out


def add(cfg, c):
    d = {(n, l): k for n, l, k in cfg}
    d[c] = d.get(c, 0) + 1
    return [(n, l, k) for (n, l), k in sorted(d.items())]


def step(Z, cfg_prev, rows, label):
    """one chain step: cfg_prev has Z-1 electrons; choose the Zth"""
    cands = candidates(cfg_prev)
    t0 = time.time()
    # F40.1: the reference is the CATION of element Z carrying config(Z-1) -- nuclear charge Z, Z-1 electrons.
    # Building it at nuclear charge Z-1 makes D a difference between two different atoms, not a binding energy.
    # s48: EVERY solve goes through the guard (F47.2). Rung 0 IS the ruling field and is
    # tried first, so a converging channel returns exactly the unguarded number. A channel
    # converging at NO rung returns no number and joins `fail`, beside the node-count ones.
    gr = NG.run_guarded(Z, cfg_prev, 'ref')
    if not gr['conv']:
        raise RuntimeError(f"Z={Z}: reference did not converge -- {gr['err']}")
    Eref, itref, rung_ref = gr['E'], gr['it'], gr['rung']
    D = {}
    for c in cands:
        t1 = time.time()
        g = NG.run_guarded(Z, add(cfg_prev, c), tagof(c))
        if g['conv']:
            D[tagof(c)] = dict(nl=list(c), D=round(g['E'] - Eref, 5), it=g['it'],
                               rung=g['rung'], sec=int(time.time() - t1))
        else:
            D[tagof(c)] = dict(nl=list(c), D=None, err=g['err'], rung=g['rung'],
                               sec=int(time.time() - t1))
        print(f"    {Z} {tagof(c):>3} {D[tagof(c)].get('D')} rung {D[tagof(c)].get('rung')}", flush=True)
    ok = {k: v for k, v in D.items() if v.get('D') is not None}
    if not ok: raise RuntimeError(f"Z={Z}: no channel converged")
    win = min(ok, key=lambda k: ok[k]['D'])
    srt = sorted(ok, key=lambda k: ok[k]['D'])
    marg = round(ok[srt[1]]['D'] - ok[srt[0]]['D'], 5) if len(srt) > 1 else None
    try:
        rec = ''.join(f"{n}{'spdfg'[l]}{k}" for n, l, k in G.expand(Z))
        recent = [nl for nl in {(n, l): k for n, l, k in G.expand(Z)}
                  if {(n, l): k for n, l, k in G.expand(Z)}[nl] >
                     {(n, l): k for n, l, k in G.expand(Z - 1)}.get(nl, 0) + 1e-9] if Z > 1 else []
        rectag = tagof(recent[0]) if len(recent) == 1 else None
        prov = 'OBSERVED'
    except (KeyError, IndexError):
        rec, rectag, prov = None, None, ('SYNTHESISED-UNMEASURED' if Z <= 118 else 'PREDICTED-UNSYNTHESISED')
    o = dict(Z=Z, mode=label, ent=win, ent_nl=ok[win]['nl'], D_ent=ok[win]['D'], margin=marg,
             order=[[k, ok[k]['D']] for k in srt], nfail=len(D) - len(ok),
             fail={k: v['err'] for k, v in D.items() if v.get('D') is None},
             ref_cfg=''.join(f"{n}{'spdfg'[l]}{k}" for n, l, k in cfg_prev),
             rec_ent=rectag, rec_cfg=rec, prov=prov, label=('PREDICTED-BY-FIELD' if prov != 'OBSERVED' else 'CHAIN'),
             ok=(rectag == win) if rectag else None, it_ref=itref, sec=int(time.time() - t0),
             rung_ref=rung_ref,
             chan={k: dict(it=v.get('it'), rung=v.get('rung')) for k, v in D.items()},
             rungs=sorted({v.get('rung') for v in D.values()} | {rung_ref}),
             guard='nlguard LADDER=' + repr(NG.LADDER))
    return o


def main():
    a = sys.argv[1:]
    rows = load()
    if a and a[0] == 'show':
        print(f"  {'Z':>4} {'ent':>4} {'rec':>4} {'ok':>3} {'D_ent':>10} {'margin':>9}  prov")
        for Z in sorted(rows):
            r = rows[Z]
            print(f"  {Z:>4} {r['ent']:>4} {str(r['rec_ent']):>4} {str(r['ok']):>3} "
                  f"{r['D_ent']:>10} {str(r['margin']):>9}  {r['prov']}")
        n = [r for r in rows.values() if r['ok'] is not None]
        print(f"\n  chained score {sum(1 for r in n if r['ok'])}/{len(n)}")
        bad = [r['Z'] for r in sorted(rows.values(), key=lambda x: x['Z']) if r['ok'] is False]
        print(f"  FIRST DIVERGENCE: {bad[0] if bad else 'none'}")
        return
    if a and a[0] == 'restart':
        Z = int(a[1])
        cfg = G.expand(Z - 1)
        o = step(Z, cfg, rows, 'restart')
        print(json.dumps(o)); return
    z0, z1 = int(a[0]), int(a[1])
    for Z in range(z0, z1 + 1):
        if Z in rows: print("SKIP", Z, rows[Z]['ent'], flush=True); continue
        cfg = cfg_from_chain(Z - 1, rows)
        o = step(Z, cfg, rows, 'chain')
        open(OUT, 'a').write(json.dumps(o) + '\n')
        rows[Z] = o
        print(f"  -> Z={Z} entrant {o['ent']} D {o['D_ent']} margin {o['margin']} "
              f"rec {o['rec_ent']} ok {o['ok']} ({o['sec']}s)", flush=True)


if __name__ == '__main__':
    main()
