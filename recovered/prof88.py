#!/usr/bin/env python3
"""prof88.py -- s88 · ITEM 1 · CLAUSE 1 · THE DERIVED LOWER PROFILE phi(t).
Prediction pack88/PREDICTION-S88-ITEM1-PROFILE.md hashed BEFORE this file existed.

Sub-core c (a subset of the frozen N-1 core's shells): q_c(r) = -sum_c occ Y0_c  (walk's own
Y0; no nucleus, no exchange).  Phi = the sub-core's normalised S~ on the channel's ruling
orbit, by the SAME geometry() the measurement uses.  Remainder R = S~ - Phi must be convex
(conv_frac >= 0.999) else REFUSED.  Extreme point S~_max = Phi + tent(b0-beta0, b1-beta1).
J_max by quadrature.  Profiles: P1 innermost shell; P2 core minus outermost shell; ladder P_k.
usage: canfail | run Z.. | score | wells Z..
"""
import json, os, sys, math, time, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
for p in ('pack88', 'pack87', 'pack86', 'pack85', 'pack84', 'pack83', 'pack81', 'rt'):
    sys.path.insert(0, os.path.join(ROOT, p))
import numpy as np
import semi87 as S87, semi85 as S85, semi84 as S84
import floor87 as F87
PRED = os.path.join(HERE, 'PREDICTION-S88-ITEM1-PROFILE.md'); PSHA = PRED.replace('.md', '.sha256')
OUT = os.path.join(HERE, 'prof88-out.json')
CONV = 0.999


def gate_sha():
    want = open(PSHA).read().split()[0]; got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got: print("HALT rc=3 sha"); sys.exit(3)


def shells_by_r(h):
    r = np.asarray(h.r, float); out = []
    for k, P in h.cP.items():
        P = np.asarray(P, float); nrm = float(np.trapezoid(P * P, r))
        out.append((float(np.trapezoid(r * P * P, r) / nrm), k))
    return [k for _, k in sorted(out)]


def q_sub(h, shells):
    """-(direct screening charge function) of the named shells: q_c = -sum occ Y0."""
    q = np.zeros(h.npts)
    for k in shells: q = q - h.cQ[k] * np.asarray(h.cY0[k], float)
    return q


def profile_J(E, l, r, q_full, q_c, R, scale=1.0, want_rc=False):
    """J_max for S~ = scale*Phi + tent(remainder).  Returns dict or a refusal."""
    L = l + 0.5; r_out, r_in = R['r_out'], R['r_in']; a = R['a']
    qc = scale * q_c
    Gc = S85.geometry(E, l, r, qc, r_out, r_in)
    Gr = S85.geometry(E, l, r, q_full - qc, r_out, r_in)
    b0p, b1p = Gr['b0'], Gr['b1']
    if Gr['conv_frac'] < CONV or b0p < -1e-9 or b1p < -1e-9:
        return dict(refused=True, conv_rem=Gr['conv_frac'], b0p=b0p, b1p=b1p, Kc=Gc['K'])
    b0p, b1p = max(b0p, 0.0), max(b1p, 0.0); Kp = b0p + b1p
    tc = b1p / Kp if Kp > 0 else 0.5
    u1, u2 = 1.0 / r_out, 1.0 / r_in; lr = np.log(r)
    S1, S2 = float(np.interp(math.log(r_out), lr, qc)) / r_out, float(np.interp(math.log(r_in), lr, qc)) / r_in
    def Phi(t):
        t = np.atleast_1d(np.asarray(t, float)); u = u1 + a * t
        Su = np.interp(np.log(np.clip(1.0 / u, r[0], r[-1])), lr, qc) * u
        return 2.0 * (Su - (S1 + (S2 - S1) * t)) / (L * L * a * a)
    Sfun = lambda t: Phi(t) + S87.Stilde_ramp(t, b0p, b1p, 0.0)
    rc = float(tc * (1 - tc) + Sfun(np.array([tc]))[0])
    if want_rc: return rc
    Jm = S87.J_profile(Sfun, ramp=(tc - 1e-4, tc + 1e-4))
    return dict(refused=False, Kc=Gc['K'], conv_c=Gc['conv_frac'], Kp=Kp, b0p=b0p, b1p=b1p, tc=tc,
                Jtent_rem=S85.J_tent(b0p, b1p), Jmax=Jm, rc=rc, conv_rem=Gr['conv_frac'])


def row_channels(Z):
    import gtest83 as G
    h, cfg, ent, eps, row, Etot = S84.field_of(Z); r = np.asarray(h.r, float)
    chans = []
    for rank, c in enumerate(sorted(G.channels(row, lmax=3), key=lambda c: c['nu'])[:5]):
        n, l, E = c['n'], c['l'], float(c['D'])
        rr, q = S85.q_native(h, n, l); R = S85.channel_row(E, l, rr, q)
        chans.append((c['tag'], n, l, E, q, R, rank))
    return h, row, r, chans


def canfail():
    gate_sha(); ok = True
    def rep(n, g, msg):
        nonlocal ok; ok = ok and bool(g); print(f"  {n} {msg}  {'PASS' if g else '**FAIL**'}")
    h, row, r, chans = row_channels(24)
    tag, n, l, E, q, R, rank = next(c for c in chans if c[0] == '3d')
    order = shells_by_r(h); qc2 = q_sub(h, order[:-1]); qc1 = q_sub(h, order[:1])
    z = profile_J(E, l, r, q, qc2, R, scale=0.0); Jt = S85.J_tent(max(R['b0'], 0), max(R['b1'], 0))
    rep('CF1', (not z['refused']) and abs(z['Jmax'] - Jt) < 1e-6 and abs(z['rc'] - F87.rc_floor(R['b0'], R['b1'], 0.0)) < 1e-9,
        f"s=0 returns the tent: Jmax={z['Jmax']:.6f} Jtent={Jt:.6f} rc={z['rc']:.3e}")
    x = profile_J(E, l, r, q, qc2, R, scale=1.3)
    rep('CF2', x['refused'], f"phi=1.3*P2 REFUSED: refused={x['refused']} conv_rem={x['conv_rem']:.3f}")
    # CF3/CF4 synthetic constant profile vs floor87 closed form
    def J_const(b0, b1, m):
        b0p, b1p = b0 - m / 2, b1 - m / 2; tc = b1p / (b0p + b1p)
        S = lambda t: -0.5 * m * t * (1 - t) + S87.Stilde_ramp(t, b0p, b1p, 0.0)
        return S87.J_profile(S, ramp=(tc - 1e-4, tc + 1e-4))
    a3, f3 = J_const(0.55, 0.55, 0.30), F87.J_floor_closed(0.55, 0.55, 0.30)
    rep('CF3', math.isfinite(a3) and a3 < 2 and abs(a3 - f3) < 1e-5, f"K=1.10 const phi=0.30: Jmax={a3:.6f} floor87={f3:.6f} (<2, NON-VACUOUS)")
    a4 = J_const(0.70, 0.70, 0.30)
    rep('CF4', not (math.isfinite(a4) and a4 < 2), f"K=1.40 const phi=0.30: Jmax={a4} NOT certified")
    y = profile_J(E, l, r, q, qc2, R)
    rep('CF5', (not y['refused']) and y['Jmax'] > y['Jtent_rem'] + 1e-6,
        f"prefactor real at Z=24 3d P2: Jmax={y['Jmax']:.5f} > Jtent(rem)={y['Jtent_rem']:.5f}; K'={y['Kp']:.4f} J={R['J']:.5f}")
    print(f"\n  CAN-FAIL GATE: {'PASS' if ok else '**FAIL**'}"); return ok


def run(zs):
    gate_sha(); out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    for Z in zs:
        t0 = time.time(); h, row, r, chans = row_channels(Z); order = shells_by_r(h); nsh = len(order); rows = []
        for tag, n, l, E, q, R, rank in chans:
            if R is None: rows.append(dict(tag=tag, l=l, nu_rank=rank, J=None)); continue
            b0, b1 = max(R['b0'], 0), max(R['b1'], 0)
            d = dict(tag=tag, l=l, nu_rank=rank, K=R['K'], J=R['J'], b0=b0, b1=b1, Jtent=S85.J_tent(b0, b1), nshell=nsh)
            lad = []
            for k in range(1, nsh):
                lad.append(profile_J(E, l, r, q, q_sub(h, order[:k]), R))
            d['ladder'] = lad; d['P1'] = lad[0]; d['P2'] = lad[-1]
            rows.append(d)
        live = [x for x in rows if x.get('J') is not None]; lv = sorted(live, key=lambda x: x['l'])[0]
        tag, n, l, E, q, R, rank = next(c for c in chans if c[0] == lv['tag']); qc = q_sub(h, order[:-1])
        r0 = profile_J(E, l, r, q, qc, R, scale=0.0, want_rc=True); r1 = profile_J(E, l, r, q, qc, R, scale=1.0, want_rc=True)
        rh = profile_J(E, l, r, q, qc, R, scale=0.5, want_rc=True)
        if not (r1 != r0 and min(r0, r1) < rh < max(r0, r1)):
            print(f"  Z={Z}: **LEVER DEAD** at {lv['tag']} rc0={r0:.3e} rc1={r1:.3e} rch={rh:.3e}"); return 4
        cert = [x for x in live if x['nu_rank'] <= 1 and x['K'] >= 1 and not x['P2']['refused'] and x['P2']['Jmax'] < 2]
        print(f"  Z={Z} {row['ent']:>3} shells={nsh} lever LIVE {lv['tag']} rc {r0:.3e}->{r1:.3e}  P2 cert: "
              + ", ".join(f"{x['tag']} K={x['K']:.3f} K'={x['P2']['Kp']:.3f} Jm={x['P2']['Jmax']:.3f} J={x['J']:.3f}" for x in cert)
              + f"  ({int(time.time()-t0)}s)")
        fix = lambda v: 'inf' if v == float('inf') else v
        out[str(Z)] = dict(Z=Z, ent=row['ent'], rows=json.loads(json.dumps(rows, default=fix).replace('Infinity', '"inf"')))
        json.dump(out, open(OUT, 'w'), indent=1)
    return 0


def score():
    d = json.load(open(OUT)); fin = lambda v: isinstance(v, (int, float)) and math.isfinite(v)
    A = [dict(x, Z=int(z)) for z, row in d.items() for x in row['rows'] if x.get('J') is not None and x['nu_rank'] <= 1]
    Kge = [x for x in A if x['K'] >= 1]; print(f"rows {len(d)} A {len(A)} K>=1 {len(Kge)}")
    for P in ('P1', 'P2'):
        ref = [x for x in A if x[P]['refused']]
        t1 = [x for x in A if not x[P]['refused'] and fin(x[P]['Jmax']) and x[P]['Jmax'] < x['J'] - 1e-6]
        print(f"\n== {P} ==  T1 Jmax>=J violations {len(t1)} -> {'CORRECT' if not t1 else 'FALSIFIED'};  T3 refused {len(ref)} of {len(A)}: "
              + " ".join(f"{x['Z']}{x['tag']}" for x in ref))
        cert = [x for x in Kge if not x[P]['refused'] and fin(x[P]['Jmax']) and x[P]['Jmax'] < 2]
        print(f"  certified {len(cert)} of {len(Kge)}")
        for l in (1, 2, 3):
            g = [x for x in Kge if x['l'] == l]; c = [x for x in cert if x['l'] == l]
            print(f"    l={l}: {len(c)} of {len(g)}")
        five = [x for x in Kge if x['J'] >= 2]
        print(f"  T7 J>=2 certified: {sum(1 for x in five if not x[P]['refused'] and fin(x[P]['Jmax']) and x[P]['Jmax']<2)} of {len(five)}")
        kp = [x[P]['Kp'] for x in A if not x[P]['refused']]; print(f"  T9 median K' = {np.median(kp):.4f}")
        pf = [x[P]['Jmax'] - x['J'] for x in A if not x[P]['refused'] and fin(x[P]['Jmax'])]
        print(f"  T10 median Jmax-J = {np.median(pf):.4f}   median Jmax-Jtent(rem) = {np.median([x[P]['Jmax']-x[P]['Jtent_rem'] for x in A if not x[P]['refused'] and fin(x[P]['Jmax'])]):.4f}")
    mono = 0
    for x in Kge:
        js = [y['Jmax'] if (not y['refused'] and fin(y['Jmax'])) else float('inf') for y in x['ladder']]
        mono += all(js[i + 1] <= js[i] + 1e-9 for i in range(len(js) - 1))
    print(f"\nT8 ladder monotone: {mono} of {len(Kge)}")
    print("\nuncertified K>=1 under P2 (Z tag l K K' Jmax J refused):")
    for x in Kge:
        p = x['P2']
        if p['refused'] or not (fin(p['Jmax']) and p['Jmax'] < 2):
            print(f"  {x['Z']} {x['tag']} {x['l']} {x['K']:.3f} {p.get('Kp', float('nan')):.3f} {p.get('Jmax')} {x['J']:.3f} {p['refused']}")
    print("\nP1 certified:"); [print(f"  {x['Z']} {x['tag']} K={x['K']:.3f} Kc={x['P1']['Kc']:.3f} Jmax={x['P1']['Jmax']:.3f} J={x['J']:.3f}")
                             for x in Kge if not x['P1']['refused'] and fin(x['P1']['Jmax']) and x['P1']['Jmax'] < 2]
    return 0


def wells(zs):
    """ITEM 1b probe: J of BOTH wells of 5d/4d at the named rows."""
    gate_sha()
    for Z in zs:
        h, row, r, chans = row_channels(Z)
        for tag, n, l, E, q, R, rank in chans:
            if l != 2: continue
            L = l + 0.5
            qfun = lambda rr: np.interp(np.log(np.clip(np.atleast_1d(np.asarray(rr, float)), r[0], r[-1])), np.log(r), q)
            J, meta = S84.J_of(E, l, qfun, detail=True)
            if J is None: print(f"  Z={Z} {tag}: no allowed region"); continue
            Ji = (L / math.pi) * meta['I_inner'] if meta['I_inner'] else None
            print(f"  Z={Z} {row['ent']:>3} {tag} n_regions={meta['n_regions']} outer r[{meta['r_inner']:.3f},{meta['r_outer']:.3f}] J_outer={J:.4f}"
                  + (f" J_inner={Ji:.4f}" if Ji else "") + f"  K={R['K'] if R else None}")
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'canfail': sys.exit(0 if canfail() else 4)
    if a[0] == 'run': sys.exit(run([int(x) for x in a[1:]]))
    if a[0] == 'score': sys.exit(score())
    if a[0] == 'wells': sys.exit(wells([int(x) for x in a[1:]]))
