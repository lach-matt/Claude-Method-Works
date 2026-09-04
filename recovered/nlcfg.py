"""nlcfg.py -- s45 item 1: THE CONFIGURATION COLUMN. BLOCKING per s44 §2(5).

`ok` in nlchain.jsonl compares STEPS (rectag == entrant). The walk produces a STATE.
This driver adds the STATE comparison beside it. Both stay; comparison decides.

    cfg_chain(Z) = seed 1s + entrants of steps 2..Z      (nlchain.cfg_from_chain, unmodified)
    cfg_ok(Z)    = cfg_chain(Z) == ground.expand(Z)      as a NORMALISED MULTISET (F42.2)

nlchain.py is IMPORTED AND NEVER PATCHED (M's ruling (b), s44). No SCF is run: the column is
a pure function of sealed nlchain.jsonl and ground.py.

usage: python3 nlcfg.py show      both columns, both scores, both first divergences
       python3 nlcfg.py gate      standing gate: fixed expectations, exit non-zero on failure
       python3 nlcfg.py --fail    can-fail demonstration (perturbs one chain step in memory)
"""
import sys, os
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
import nlchain as NC
import ground as G

TAG = lambda n, l, k: f"{n}{'spdfg'[l]}{k}"


def norm(cfg):
    """normalised multiset: dict (n,l)->int occ, zero-occupancies dropped. Order-independent."""
    d = {}
    for n, l, k in cfg:
        d[(int(n), int(l))] = d.get((int(n), int(l)), 0) + int(round(k))
    return {k: v for k, v in d.items() if v > 0}


def as_str(cfg):
    return ''.join(TAG(n, l, k) for (n, l), k in sorted(norm(cfg).items()))


def column(rows, perturb=None):
    """returns {Z: dict(cfg_chain, rec_cfg, cfg_ok, ok, str_ok)}"""
    if perturb:
        rows = {z: dict(r) for z, r in rows.items()}
        rows[perturb]['ent_nl'] = [5, 0]          # in-memory only; jsonl untouched
    out = {}
    for Z in sorted(rows):
        if Z < 2: continue
        try:
            chain = NC.cfg_from_chain(Z, rows)
        except KeyError:
            continue
        try:
            rec = G.expand(Z)
        except (KeyError, IndexError):
            out[Z] = dict(cfg_chain=as_str(chain), rec_cfg=None, cfg_ok=None,
                          ok=rows[Z]['ok'], str_ok=None)
            continue
        cfg_ok = norm(chain) == norm(rec)
        # PCC-0a: the string comparison is computed too, and only compared to the multiset.
        str_ok = as_str(chain) == as_str(rec)
        out[Z] = dict(cfg_chain=as_str(chain), rec_cfg=as_str(rec), cfg_ok=cfg_ok,
                      ok=rows[Z]['ok'], str_ok=str_ok)
    return out


def scores(col):
    c = [v for v in col.values() if v['cfg_ok'] is not None]
    o = [v for v in col.values() if v['ok'] is not None]
    cf = sorted(Z for Z, v in col.items() if v['cfg_ok'] is False)
    of = sorted(Z for Z, v in col.items() if v['ok'] is False)
    return dict(cfg_score=(sum(1 for v in c if v['cfg_ok']), len(c)),
                ok_score=(sum(1 for v in o if v['ok']), len(o)),
                cfg_fail=cf, ok_fail=of,
                cfg_first=(cf[0] if cf else None), ok_first=(of[0] if of else None),
                disagree=sorted(Z for Z, v in col.items()
                                if v['cfg_ok'] is not None and v['ok'] is not None
                                and v['cfg_ok'] != v['ok']),
                str_mismatch=sorted(Z for Z, v in col.items()
                                    if v['str_ok'] is not None and v['str_ok'] != v['cfg_ok']))


def show(col, s):
    print(f"  {'Z':>4} {'ent':>4} {'rec':>4} {'ok':>6} {'cfgok':>6}  {'cfg_chain':<26} {'rec_cfg':<26}")
    rows = NC.load()
    for Z in sorted(col):
        v = col[Z]
        if v['cfg_ok'] is True and v['ok'] is True: continue     # print only the informative rows
        print(f"  {Z:>4} {rows[Z]['ent']:>4} {str(rows[Z]['rec_ent']):>4} {str(v['ok']):>6} "
              f"{str(v['cfg_ok']):>6}  {v['cfg_chain']:<26} {str(v['rec_cfg']):<26}")
    print(f"\n  CONFIG score {s['cfg_score'][0]}/{s['cfg_score'][1]}   "
          f"STEP (`ok`) score {s['ok_score'][0]}/{s['ok_score'][1]}")
    print(f"  FIRST CONFIG DIVERGENCE: {s['cfg_first']}   FIRST STEP DIVERGENCE: {s['ok_first']}")
    print(f"  config failures : {s['cfg_fail']}")
    print(f"  step   failures : {s['ok_fail']}")
    print(f"  columns disagree at {len(s['disagree'])}: {s['disagree']}")
    print(f"  nesting: cfg<=ok {set(s['cfg_fail'])<=set(s['ok_fail'])}  "
          f"ok<=cfg {set(s['ok_fail'])<=set(s['cfg_fail'])}")
    print(f"  string-vs-multiset mismatches: {s['str_mismatch']}")


GATE = dict(cfg_score=(39, 47), ok_score=(42, 47), cfg_first=24, ok_first=25,
            cfg_fail=[24, 29, 41, 42, 44, 45, 46, 47], ok_fail=[25, 30, 43, 47, 48],
            disagree=[24, 25, 29, 30, 41, 42, 43, 44, 45, 46, 48], str_mismatch=[])


def gate(s):
    bad = 0
    for k, want in GATE.items():
        got = s[k]
        got = list(got) if isinstance(got, list) else got
        good = (got == want)
        print(f"  [{'PASS' if good else 'FAIL'}] {k:<12} got {got}  want {want}")
        bad += (not good)
    print(f"\nNLCFG GATE: {'PASS -- all clauses' if not bad else f'FAIL -- {bad} clause(s)'}")
    return 1 if bad else 0


if __name__ == '__main__':
    a = sys.argv[1:]
    rows = NC.load()
    p = 30 if '--fail' in a else None
    col = column(rows, perturb=p)
    s = scores(col)
    if a and a[0] == 'gate':
        sys.exit(gate(s))
    show(col, s)
    if p: print("\n  (--fail: step 30's entrant forced to 5s IN MEMORY; nlchain.jsonl untouched)")
