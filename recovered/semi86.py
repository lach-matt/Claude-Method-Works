#!/usr/bin/env python3
"""semi86.py -- s86 · ITEM 1 · CLAUSE 1 · DOES THE GAUSS CONSTRAINT CUT THE TENT?

Prediction pack86/PREDICTION-S86-ITEM1-GAUSS-CUT.md, hashed BEFORE this file existed.
Field and geometry: s85's, imported unmodified (semi85.q_native, semi85.channel_row);
semi85 imports s84's field unmodified. Nothing sealed is edited.

PER CHANNEL (population A = nu_rank 0,1): the tent = the two tangent lines of
S(u) = u Q(u) at u1 = 1/r_out and u2 = 1/r_in. Reported: intercepts alpha1, alpha2
(= -u_i^2 Q'(u_i) = r_i q'(r_i)), monotonicity of Q_tent on 2001 points, its band,
and the same for the SATURATING tent (both b's scaled to b0+b1 = 1).

LEVER (D4 of s85, carried): q == 1 must give alpha1 = alpha2 = 0 and K = 0 on the
dead arm; the live arm must move both. rc=4 otherwise.

usage: python3 semi86.py canfail | run Z [Z...] | score
"""
import json, os, sys, math, hashlib, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'pack85')); sys.path.insert(0, os.path.join(ROOT, 'pack84'))
import numpy as np
import semi85 as S85
import semi84 as S84
PRED = os.path.join(HERE, 'PREDICTION-S86-ITEM1-GAUSS-CUT.md')
PSHA = os.path.join(HERE, 'PREDICTION-S86-ITEM1-GAUSS-CUT.sha256')
OUT = os.path.join(HERE, 'semi86-out.json')
TOL = 1e-9

def gate_sha():
    want = open(PSHA).read().split()[0]
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        print(f"HALT rc=3: prediction sha mismatch {want} != {got}"); sys.exit(3)

def tent_check(r, q, r_out, r_in, L, scale=1.0):
    """Tent from tangents at u1,u2 with slopes scaled about the chord by `scale`
    (scale=1 is the tent; scale=1/(b0+b1) is the saturating tent). Returns dict."""
    lr = np.log(r); w = S85.w_grid(r, q)
    qi = lambda rr: float(np.interp(math.log(rr), lr, q))
    wi = lambda rr: float(np.interp(math.log(rr), lr, w))
    u1, u2 = 1.0 / r_out, 1.0 / r_in; a = u2 - u1
    Q1, Q2 = qi(r_out), qi(r_in); S1, S2 = Q1 * u1, Q2 * u2
    cst = (S2 - S1) / a
    w1 = cst - scale * (cst - wi(r_out)); w2 = cst + scale * (wi(r_in) - cst)
    al1 = S1 - w1 * u1; al2 = S2 - w2 * u2              # intercepts
    # kink
    if abs(w2 - w1) < 1e-300:
        uk = 0.5 * (u1 + u2)
    else:
        uk = (al2 - al1) / (w1 - w2)
    uk_in = (u1 - TOL <= uk <= u2 + TOL)
    u = np.linspace(u1, u2, 2001)
    St = np.where(u <= uk, al1 + w1 * u, al2 + w2 * u)
    Qt = St / u
    d = np.diff(Qt)
    mono = float(d.min()) >= -TOL * abs(Q2)
    band = (Qt.min() >= Q1 - TOL * abs(Q2)) and (Qt.max() <= Q2 + TOL * abs(Q2))
    b0 = 2 * (cst - w1) / (L * L * a); b1 = 2 * (w2 - cst) / (L * L * a)
    return dict(alpha1=al1, alpha2=al2, Q1=Q1, Q2=Q2, Qt_u1=float(Qt[0]), Qt_u2=float(Qt[-1]),
                mono=bool(mono), band=bool(band), kink_in=bool(uk_in), b0=b0, b1=b1,
                K_end=b0 + b1, minQt=float(Qt.min()), maxQt=float(Qt.max()))

def channel(E, l, r, q):
    R = S85.channel_row(E, l, r, q)
    if R is None: return None
    L = l + 0.5
    T = tent_check(r, q, R['r_out'], R['r_in'], L)
    Ke = T['K_end']
    Tsat = tent_check(r, q, R['r_out'], R['r_in'], L, scale=(1.0 / Ke if Ke > 0 else 1.0))
    return dict(K=R['K'], K_end=R['K_end'], J=R['J'], n_regions=R['n_regions'],
                tent=T, sat=Tsat)

def canfail():
    gate_sha(); ok = True
    r = np.exp(np.linspace(math.log(1e-4), math.log(60.0), 2400)); L = 1.5
    # CF1 a q that INCREASES with r on the outer side: intercept > 0, flagged.
    qbad = 1.0 + 0.2 * np.tanh(r)                       # q' > 0 everywhere
    T = tent_check(r, qbad, 3.0, 0.2, L)
    g1 = (T['alpha1'] > 0) and (T['alpha2'] > 0) and (not T['mono'])
    print(f"  CF1 increasing q: alpha1={T['alpha1']:.3e} alpha2={T['alpha2']:.3e} mono={T['mono']}  {'PASS' if g1 else 'FAIL'}"); ok = ok and bool(g1)
    # CF2 constant q: intercepts 0, Q_tent constant, admissible.
    T = tent_check(r, np.full_like(r, 7.0), 3.0, 0.2, L)
    g2 = abs(T['alpha1']) < 1e-9 and abs(T['alpha2']) < 1e-9 and T['mono'] and T['band'] and abs(T['maxQt'] - T['minQt']) < 1e-9
    print(f"  CF2 constant q: alphas {T['alpha1']:.1e},{T['alpha2']:.1e} spread {T['maxQt']-T['minQt']:.1e}  {'PASS' if g2 else 'FAIL'}"); ok = ok and bool(g2)
    # CF3 a screened core (q decreasing): admissible; then flip q' sign at outer end only.
    qg = 1.0 + 9.0 * np.exp(-r / 0.6)
    T = tent_check(r, qg, 3.0, 0.2, L)
    qf = qg.copy(); lr = np.log(r)
    # flip: replace outer tail by a rising one beyond r=2.5 smoothly
    m = r > 2.5; qf[m] = qg[m] + 0.5 * (r[m] - 2.5) ** 2
    Tf = tent_check(r, qf, 3.0, 0.2, L)
    g3 = (T['alpha1'] <= 0 and T['alpha2'] <= 0 and T['mono'] and T['band']) and (Tf['alpha1'] > 0) and (not Tf['mono'])
    print(f"  CF3 screened core admissible ({T['mono']},{T['band']}); outer flip alpha1 {T['alpha1']:.3e}->{Tf['alpha1']:.3e} mono->{Tf['mono']}  {'PASS' if g3 else 'FAIL'}"); ok = ok and bool(g3)
    # CF4 lever on a real row sited below in run(); here the q==1 arm alone.
    T = tent_check(r, np.ones_like(r), 3.0, 0.2, L)
    g4 = abs(T['alpha1']) < 1e-12 and abs(T['alpha2']) < 1e-12 and abs(T['K_end']) < 1e-12
    print(f"  CF4 dead arm alphas=0,K=0  {'PASS' if g4 else 'FAIL'}"); ok = ok and bool(g4)
    # CF5 the sha gate halts on a mutated prediction (subprocess).
    import subprocess, shutil, tempfile
    tmp = tempfile.mkdtemp(); shutil.copy(PRED, tmp); shutil.copy(PSHA, tmp)
    open(os.path.join(tmp, os.path.basename(PSHA)), 'w').write('0' * 64 + '  x\n')
    code = (f"import sys,hashlib;w=open('{tmp}/{os.path.basename(PSHA)}').read().split()[0];"
            f"g=hashlib.sha256(open('{tmp}/{os.path.basename(PRED)}','rb').read()).hexdigest();sys.exit(3 if w!=g else 0)")
    rc = subprocess.run([sys.executable, '-c', code]).returncode
    g5 = rc == 3
    print(f"  CF5 sha gate halts rc={rc}  {'PASS' if g5 else 'FAIL'}"); ok = ok and bool(g5)
    print("CAN-FAIL GATE:", "PASS" if ok else "FAIL")
    return ok

def run(zs):
    gate_sha()
    sys.path.insert(0, os.path.join(ROOT, 'pack83')); import gtest83 as G
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    for Z in zs:
        t0 = time.time()
        h, cfg, ent, eps, row, Etot = S84.field_of(Z)
        chs = sorted(G.channels(row, lmax=3), key=lambda c: c['nu'])
        rows = []
        for rank, c in enumerate(chs[:2]):                     # population A
            n, l, E = c['n'], c['l'], float(c['D'])
            r, q = S85.q_native(h, n, l)
            R = channel(E, l, r, q)
            if R is None:
                rows.append(dict(tag=c['tag'], l=l, nu_rank=rank, note='no region')); continue
            D = channel(E, l, r, np.ones_like(r))
            R.update(tag=c['tag'], n=n, l=l, nu_rank=rank, Z=Z,
                     dead_alpha=(None if D is None else [D['tent']['alpha1'], D['tent']['alpha2']]),
                     dead_K=(None if D is None else D['K']))
            rows.append(R)
        live = [x for x in rows if 'tent' in x]
        if not live: print(f"  Z={Z}: no live channel HALT rc=4"); return 4
        lv = live[0]
        dead_ok = lv['dead_alpha'] is not None and max(abs(v) for v in lv['dead_alpha']) < 1e-12 and abs(lv['dead_K']) < 1e-12
        moved = abs(lv['tent']['alpha1'] - 0) > 1e-9 and abs(lv['K'] - lv['dead_K']) > 1e-9
        if not (dead_ok and moved):
            print(f"  Z={Z}: **LEVER DEAD** dead_ok={dead_ok} moved={moved}"); return 4
        print(f"  Z={Z} {row['ent']:>3} lever LIVE at {lv['tag']} ({int(time.time()-t0)}s)")
        for x in live:
            T, S = x['tent'], x['sat']
            print(f"    {x['tag']:>3} r{x['nu_rank']} l={x['l']} K={x['K']:.4f} J={x['J']:.4f} "
                  f"a1={T['alpha1']:.3e} a2={T['alpha2']:.3e} mono={T['mono']} band={T['band']} "
                  f"Q[{T['Q1']:.3f},{T['Q2']:.3f}] | SAT mono={S['mono']} band={S['band']} kink_in={S['kink_in']}")
        out[str(Z)] = dict(Z=Z, ent=row['ent'], rows=rows)
        json.dump(out, open(OUT, 'w'), indent=1)
    return 0

def score():
    gate_sha(); out = json.load(open(OUT)); A = [x for z in out.values() for x in z['rows'] if 'tent' in x]
    n = len(A); Zof = lambda x: x['Z']
    s1 = sum(1 for x in A if x['tent']['alpha1'] <= TOL and x['tent']['alpha2'] <= TOL)
    s2 = sum(1 for x in A if x['tent']['mono'] and x['tent']['band'])
    s3 = sum(1 for x in A if x['tent']['Q1'] >= 1 - 1e-6 and x['tent']['Q2'] <= Zof(x) + 1e-6)
    s5 = sum(1 for x in A if abs(x['tent']['Qt_u1'] - x['tent']['Q1']) < 1e-9 and abs(x['tent']['Qt_u2'] - x['tent']['Q2']) < 1e-9)
    s6 = sum(1 for x in A if x['sat']['mono'] and x['sat']['band'])
    s6k = sum(1 for x in A if x['sat']['kink_in'])
    changed = n - s6   # channels whose worst case is removed by the constraint
    print(f"A channels: {n}")
    print(f"S1 both intercepts <= 0:        {s1}/{n}  {'CORRECT' if s1==n else 'FALSIFIED'}")
    print(f"S2 tent Q mono & in band:        {s2}/{n}  {'CORRECT' if s2==n else 'FALSIFIED'}")
    print(f"S3 1<=Q1, Q2<=Z:                 {s3}/{n}  {'CORRECT' if s3==n else 'FALSIFIED'}")
    print(f"S4 status changes under cut:     {changed}/{n}  {'CORRECT' if changed==0 else 'FALSIFIED'}")
    print(f"S5 tent endpoints = Q1,Q2:       {s5}/{n}  {'CORRECT' if s5==n else 'FALSIFIED'}")
    print(f"S6 saturating tent admissible:   {s6}/{n} (kink inside [u1,u2]: {s6k}/{n})  {'CORRECT' if s6==n else 'FALSIFIED'}")
    bad = [(x['Z'], x['tag'], x['tent']['alpha1'], x['tent']['alpha2']) for x in A if not (x['tent']['alpha1'] <= TOL and x['tent']['alpha2'] <= TOL)]
    if bad: print("  intercept>0 at:", bad)
    mins = sorted(((x['tent']['alpha1'], x['Z'], x['tag']) for x in A), reverse=True)[:3]
    print("  least-negative alpha1:", [(f'{a:.3e}', z, t) for a, z, t in mins])
    mins = sorted(((x['tent']['alpha2'], x['Z'], x['tag']) for x in A), reverse=True)[:3]
    print("  least-negative alpha2:", [(f'{a:.3e}', z, t) for a, z, t in mins])
    return 0

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'canfail': sys.exit(0 if canfail() else 4)
    if a[0] == 'run': sys.exit(run([int(x) for x in a[1:]]))
    if a[0] == 'score': sys.exit(score())
