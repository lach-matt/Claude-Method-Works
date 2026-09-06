#!/usr/bin/env python3
"""swing91.py -- S91 ITEM 1. Decompose the one-proton collapse swing at Z*.
   D(c;Z)     = E[Z; cfg(Z-1)+c] - E[Z; cfg(Z-1)]        (sealed chain instrument)
   D_fr(c;Z*) = E[Z*; R_fr + c] - E[Z*; R_fr],  R_fr = cfg(Z*-1) with entrant shell at its cfg(Z*-2) value
   swing = D(Z*) - D(Z*-1) = P + S ;  P = D_fr - D(Z*-1) ; S = D(Z*) - D_fr
usage: swing91.py ROW [--canfail A|B]   ROW in 38 56 58 90 91
Every solve goes through nlguard.run_guarded (rung ladder). Lever: entrant occupancy. rc=4 if dead.
"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG

ROWS = {38: ['4d', '5s'], 56: ['5d', '6s'], 58: ['4f', '5d'], 90: ['6d', '5f'], 91: ['5f', '6d']}
LEV = dict(s=0, p=1, d=2, f=3)
def ch(tag): return (int(tag[0]), LEV[tag[1]])

def setocc(cfg, c, k):
    d = {(n, l): q for n, l, q in cfg}
    d[c] = k
    return [(n, l, q) for (n, l), q in sorted(d.items()) if q > 1e-9]

def Dof(Z, ref, tags):
    g = NG.run_guarded(Z, ref, 'ref')
    if not g['conv']: raise RuntimeError(f"ref Z={Z} {g['err']}")
    out = {}
    for t in tags:
        h = NG.run_guarded(Z, NC.add(ref, ch(t)), t)
        out[t] = None if not h['conv'] else round(h['E'] - g['E'], 5)
    return out, g['rung']

def main():
    Zs = int(sys.argv[1]); canfail = sys.argv[3] if len(sys.argv) > 3 else None
    rows = NC.load()
    tags = ROWS[Zs]
    cfg1 = NC.cfg_from_chain(Zs - 1, rows)          # cfg(Z*-1): the sealed reference at Z*
    ent = tuple(rows[Zs - 1]['ent_nl'])             # entrant shell at Z*-1
    k1 = dict(((n, l), q) for n, l, q in cfg1)[ent]
    cfg2 = NC.cfg_from_chain(Zs - 2, rows)
    k0 = dict(((n, l), q) for n, l, q in cfg2).get(ent, 0)
    if canfail == 'B': ent = (4, 1)                 # wrong shell: freeze 4p instead
    if canfail == 'A': k0 = k1                      # lever dead: frozen == sealed
    sealed = {t: dict(rows[Zs]['order']).get(t) for t in tags}
    prev = {t: dict(rows[Zs - 1]['order']).get(t) for t in tags}
    print(f"Z*={Zs} tags={tags} entrant={NC.tagof(ent)} occ sealed={k1} frozen={k0}", flush=True)
    t0 = time.time()
    Dfr, r0 = Dof(Zs, setocc(cfg1, ent, k0), tags)
    # lever check: frozen must differ from sealed D for the collapsing channel
    t = tags[0]
    if Dfr[t] is None or abs(Dfr[t] - sealed[t]) < 1e-4:
        print(f"LEVER DEAD: D_fr={Dfr[t]} sealed={sealed[t]}  rc=4", flush=True); sys.exit(4)
    Dh, r1 = Dof(Zs, setocc(cfg1, ent, 0.5 * (k0 + k1)), tags)   # half-occupancy lever point
    Dre, r2 = Dof(Zs, cfg1, tags)                                 # sealed reproduction (rung 0 check)
    res = dict(Z=Zs, entrant=NC.tagof(ent), occ=[k0, k1], rungs=[r0, r1, r2], canfail=canfail, rows={})
    for t in tags:
        sw = None if None in (sealed[t], prev[t]) else round(sealed[t] - prev[t], 5)
        P = None if None in (Dfr[t], prev[t]) else round(Dfr[t] - prev[t], 5)
        S = None if None in (Dfr[t], sealed[t]) else round(sealed[t] - Dfr[t], 5)
        Sh = None if None in (Dfr[t], Dh[t]) else round(Dh[t] - Dfr[t], 5)
        res['rows'][t] = dict(D_prev=prev[t], D_fr=Dfr[t], D_half=Dh[t], D_sealed=sealed[t], D_repro=Dre[t],
                              swing=sw, P=P, S=S, S_half=Sh,
                              ident=None if None in (P, S, sw) else round(P + S - sw, 5),
                              repro=None if None in (Dre[t], sealed[t]) else round(Dre[t] - sealed[t], 5))
        print(f"  {t}: prev {prev[t]} fr {Dfr[t]} half {Dh[t]} sealed {sealed[t]} repro {Dre[t]} | "
              f"swing {sw} P {P} S {S} S_half {Sh} ident {res['rows'][t]['ident']}", flush=True)
    res['sec'] = int(time.time() - t0)
    with open(f'../pack91/swing91-{Zs}{"-cf"+canfail if canfail else ""}.json', 'w') as f: json.dump(res, f, indent=1)
    print("sec", res['sec'])

if __name__ == '__main__': main()
