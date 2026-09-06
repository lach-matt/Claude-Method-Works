#!/usr/bin/env python3
"""semi87.py -- s87 · ITEM 1 · CLAUSE 1 · THE KINETIC CAP ON S''.

Prediction pack87/PREDICTION-S87-ITEM1-KINETIC-CAP.md, hashed BEFORE this file existed.

S''(u) = r^2 rho_r(r), rho_r = sum occ P^2.  sup P^2 <= ||P'||_2 = sqrt(2 T_i^rad).
Caps: M_u1 = r_out^2 sqrt(2 N T)   M_u2 = r_out^2 sum occ sqrt(2 T_i)   M_u3 = sup_orbit r^2 rho_r.
Normalised (t in [0,1], S~ = 2(S-chord)/(L^2 a^2)):  S~'' <= M~ = 2 M_u / L^2,  mass K,
ramp width tau = K/M~ centred at t = b1/K.  J_max = (1/pi) int dt / sqrt(t(1-t) + S~).

usage: python3 semi87.py canfail | run Z [Z..] | score
"""
import json, os, sys, math, time, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
for p in ('pack86', 'pack85', 'pack84', 'pack83', 'pack81', 'rt'):
    sys.path.insert(0, os.path.join(ROOT, p))
import numpy as np
import semi85 as S85
import semi84 as S84

PRED = os.path.join(HERE, 'PREDICTION-S87-ITEM1-KINETIC-CAP.md')
PSHA = os.path.join(HERE, 'PREDICTION-S87-ITEM1-KINETIC-CAP.sha256')
OUT = os.path.join(HERE, 'semi87-out.json')
LMAX = 3


def gate_sha():
    want = open(PSHA).read().split()[0]
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        print(f"HALT rc=3: prediction sha mismatch {want} vs {got}"); sys.exit(3)
    return got


# ------------------------------------------------------------- the ramp profile
def Stilde_ramp(t, b0, b1, tau):
    """S~(t) for sigma = M~ on [tk, tk+tau], tk = b1/K - tau/2.  M~ = K/tau."""
    K = b0 + b1
    if K <= 0:
        return np.zeros_like(t)
    tk = b1 / K - 0.5 * tau
    if tau <= 0:                                   # the tent
        return -b0 * t + K * np.clip(t - tk, 0, None)
    M = K / tau
    x = np.clip(t - tk, 0.0, tau)
    return -b0 * t + M * (x * x / 2.0) + M * tau * np.clip(t - tk - tau, 0, None)


def J_profile(Sfun, n=400001):
    """J = (1/pi) int_0^pi dth |sin th/2| / sqrt(sin^2 th/4 + S~(t)).  inf if radicand <= 0."""
    th = np.linspace(0.0, math.pi, n)
    t = 0.5 * (1.0 - np.cos(th))
    s2 = 0.25 * np.sin(th) ** 2
    rad = s2 + Sfun(t)
    if np.any(rad[1:-1] <= 0):
        return float('inf')
    f = np.sqrt(s2) / np.sqrt(rad)
    f[0] = f[-1] = 1.0
    return float(np.trapz(f, th) / math.pi)


def J_ramp(b0, b1, tau):
    b0, b1 = max(b0, 0.0), max(b1, 0.0)
    K = b0 + b1
    if K <= 0:
        return 1.0
    if tau > 0 and (b1 / K - 0.5 * tau < 0 or b0 / K - 0.5 * tau < 0):
        return None                                   # infeasible: cap inconsistent with slopes
    return J_profile(lambda t: Stilde_ramp(t, b0, b1, tau))


def J_bang(b0, b1, tau, ivs):
    """S~ for sigma = M~ on a union of intervals ivs (total length tau, mean b1/K)."""
    K = b0 + b1; M = K / tau
    def S(t):
        out = -b0 * t
        for (lo, hi) in ivs:
            x = np.clip(t - lo, 0.0, hi - lo)
            out = out + M * (x * x / 2.0) + M * (hi - lo) * np.clip(t - hi, 0, None)
        return out
    return J_profile(S)


# ------------------------------------------------------------- the core numbers
def core_numbers(h):
    r = np.asarray(h.r, float)
    T, rho_r, N, norms = {}, np.zeros_like(r), 0.0, {}
    for (n, l), P in h.cP.items():
        P = np.asarray(P, float); occ = h.cQ[(n, l)]
        dP = np.gradient(P, r)
        Trad = 0.5 * np.trapz(dP * dP, r)
        Tcen = 0.5 * l * (l + 1) * np.trapz(P * P / (r * r), r)
        T[(n, l)] = (Trad, Tcen)
        norms[(n, l)] = float(np.trapz(P * P, r))
        rho_r += occ * P * P; N += occ
    Tcore = sum(h.cQ[k] * (a + b) for k, (a, b) in T.items())
    Mr2 = sum(h.cQ[k] * math.sqrt(2.0 * (a + b)) for k, (a, b) in T.items())
    Mr1 = math.sqrt(2.0 * N * Tcore)
    return dict(r=r, rho_r=rho_r, N=N, Tcore=Tcore, Mr1=Mr1, Mr2=Mr2, norms=norms,
                sup_rho=float(rho_r.max()))


def channel_caps(G, core, q, l, E):
    """Caps in u-space and the J_max ladder for one channel."""
    r, rho_r = core['r'], core['rho_r']
    L = l + 0.5; a = G['a']; r_in, r_out = G['r_in'], G['r_out']
    orb = (r >= r_in) & (r <= r_out)
    Mu1 = r_out ** 2 * core['Mr1']; Mu2 = r_out ** 2 * core['Mr2']
    Mu3 = float((r * r * rho_r)[orb].max()) if orb.any() else float('nan')
    # S1: S'' = r^3 q'' from the q grid itself, independent of the identity
    qp = np.gradient(q, r); qpp = np.gradient(qp, r)
    Spp = float((r ** 3 * qpp)[orb].max()) if orb.any() else float('nan')
    b0, b1, K = G['b0'], G['b1'], G['K']
    out = dict(Mu1=Mu1, Mu2=Mu2, Mu3=Mu3, Spp_orbit=Spp)
    for tag, Mu in (('1', Mu1), ('2', Mu2), ('3', Mu3)):
        tau = K * L * L / (2.0 * Mu) if Mu > 0 else float('inf')
        out['tau' + tag] = tau
        out['Jmax' + tag] = J_ramp(b0, b1, tau)
    out['Jtent'] = J_ramp(b0, b1, 0.0)
    out['Jhalf2'] = J_ramp(b0, b1, 2.0 * out['tau2'])    # lever, second direction
    return out


# ------------------------------------------------------------- can-fails
def canfail():
    gate_sha(); ok = True
    def rep(name, g, msg):
        nonlocal ok; ok = ok and bool(g); print(f"  {name} {msg}  {'PASS' if g else '**FAIL**'}")
    r = np.exp(np.linspace(math.log(1e-5), math.log(40.0), 8000))
    Z = 10.0
    P1 = 2 * Z ** 1.5 * r * np.exp(-Z * r)
    P2 = (Z ** 1.5 / math.sqrt(8)) * r * (2 - Z * r) * np.exp(-Z * r / 2) / 1.0
    P2 /= math.sqrt(np.trapz(P2 * P2, r))
    P3 = (Z ** 2.5 / math.sqrt(24)) * r * r * np.exp(-Z * r / 2); P3 /= math.sqrt(np.trapz(P3 * P3, r))
    class H: pass
    h = H(); h.r = r; h.cP = {(1, 0): P1, (2, 0): P2, (2, 1): P3}; h.cQ = {(1, 0): 2.0, (2, 0): 2.0, (2, 1): 5.0}
    c = core_numbers(h)
    rep('CF0', all(abs(v - 1) < 1e-4 for v in c['norms'].values()), f"hydrogenic norms {[round(v,6) for v in c['norms'].values()]}")
    rep('CF1', c['sup_rho'] <= c['Mr2'] <= c['Mr1'], f"smooth core: sup rho_r {c['sup_rho']:.3f} <= M_r2 {c['Mr2']:.3f} <= M_r1 {c['Mr1']:.3f} -- ADMITTED")
    # CF2 step orbital: ||P'||^2 diverges with refinement
    def stepnorm(npt):
        rr = np.linspace(1e-4, 4.0, npt); P = np.where(rr < 1.0, 1.0, 0.0) * np.sqrt(1.0)
        return np.trapz(np.gradient(P, rr) ** 2, rr)
    g2 = stepnorm(8000) / stepnorm(2000)
    rep('CF2', g2 >= 3.5, f"step P: ||P'||^2 grows x{g2:.2f} under x4 refinement -- no finite M, EXCLUDED")
    # CF3 delta shell vs smooth of same mass
    eps = 0.01; Ps = np.exp(-(r - 1.0) ** 2 / (2 * eps ** 2)); Ps /= math.sqrt(np.trapz(Ps * Ps, r))
    sup_shell = 7.0 * Ps.max() ** 2
    rep('CF3', sup_shell > 10 * c['Mr2'], f"delta-shell sup rho_r {sup_shell:.1f} vs smooth M_r2 {c['Mr2']:.1f} (x{sup_shell/c['Mr2']:.0f}) -- the shell is what the cap excludes")
    # CF4 limits
    b0 = b1 = 0.45
    jt = S85.J_tent(b0, b1); jr = J_ramp(b0, b1, 0.0); jbig = J_ramp(b0, b1, 1e-9)
    j0 = J_ramp(1e-12, 1e-12, 1e-13)
    rep('CF4', abs(jr - jt) < 1e-5 and abs(jbig - jt) < 1e-5 and abs(j0 - 1) < 1e-6,
        f"ramp->tent: quadrature {jr:.6f} closed-form {jt:.6f} (M=1e9: {jbig:.6f}); V+->0: {j0:.6f}")
    # CF5 extremality against random bang-bang, K = 1.1, tau = 0.05
    b0 = b1 = 0.55; tau = 0.05; K = 1.1; mean = b1 / K
    jr = J_ramp(b0, b1, tau); rng = np.random.default_rng(87); worst, ntry = -1.0, 0
    for _ in range(200):
        k = rng.integers(1, 4); w = rng.dirichlet(np.ones(k)) * tau
        pos = np.sort(rng.uniform(0, 1 - tau, k)); ivs = []
        cur = 0.0
        for i in range(k):
            lo = max(pos[i], cur); ivs.append([lo, lo + w[i]]); cur = lo + w[i]
        m = sum((hi - lo) * (lo + hi) / 2 for lo, hi in ivs) / tau
        sh = mean - m; ivs = [[lo + sh, hi + sh] for lo, hi in ivs]
        if ivs[0][0] < 0 or ivs[-1][1] > 1: continue
        ntry += 1; j = J_bang(b0, b1, tau, ivs); worst = max(worst, j if math.isfinite(j) else 1e9)
    rep('CF5', worst <= jr + 1e-6, f"ramp J {jr:.5f} vs max of {ntry} random bang-bang {worst:.5f}")
    # CF6 lever
    ja, jb, jc = J_ramp(b0, b1, tau), J_ramp(b0, b1, 2 * tau), J_ramp(b0, b1, 0.0)
    rep('CF6', (jc == float('inf') or jc > ja) and ja > jb, f"K=1.1: tent {jc}  M {ja:.5f}  M/2 {jb:.5f} -- the cap moves J")
    print(f"\n  CAN-FAIL GATE: {'PASS' if ok else '**FAIL**'}")
    return ok


# ------------------------------------------------------------- run
def run(zs):
    gate_sha()
    import gtest83 as G
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    for Z in zs:
        t0 = time.time()
        h, cfg, ent, eps, row, Etot = S84.field_of(Z)
        core = core_numbers(h)
        if any(abs(v - 1) > 1e-5 for v in core['norms'].values()) or abs(core['N'] - (Z - 1)) > 1e-9:
            print(f"  Z={Z}: CF0 FAIL norms/N -- HALT rc=4"); return 4
        chs = sorted(G.channels(row, lmax=LMAX), key=lambda c: c['nu'])
        rows = []
        for rank, c in enumerate(chs[:5]):
            n, l, E = c['n'], c['l'], float(c['D'])
            r, q = S85.q_native(h, n, l)
            R = S85.channel_row(E, l, r, q)
            if R is None:
                rows.append(dict(tag=c['tag'], n=n, l=l, nu_rank=rank, J=None)); continue
            C = channel_caps(R, core, q, l, E)
            C.update(tag=c['tag'], n=n, l=l, nu_rank=rank, E=E, J=R['J'], K=R['K'], b0=R['b0'], b1=R['b1'],
                     a=R['a'], r_in=R['r_in'], r_out=R['r_out'], conv=R['conv_frac'])
            rows.append({k: (round(v, 10) if isinstance(v, float) and math.isfinite(v) else
                             ('inf' if v == float('inf') else v)) for k, v in C.items()})
        live = [x for x in rows if x.get('J') is not None]
        if not live: print(f"  Z={Z}: no live channel HALT rc=4"); return 4
        lv = sorted(live, key=lambda x: x['l'])[0]
        jt, j2, jh = lv['Jtent'], lv['Jmax2'], lv['Jhalf2']
        fin = lambda v: isinstance(v, float)
        moved = (fin(jt) and fin(j2) and jt - j2 > 1e-12) or (jt == 'inf' and fin(j2))
        moved2 = fin(j2) and fin(jh) and j2 - jh > 1e-12
        if not (moved and moved2):
            print(f"  Z={Z}: **LEVER DEAD** at {lv['tag']}: tent {jt} cap {j2} half {jh}"); return 4
        print(f"  Z={Z} {row['ent']:>3} N={core['N']:.0f} T={core['Tcore']:.1f} Mr1={core['Mr1']:.1f} Mr2={core['Mr2']:.1f} "
              f"lever LIVE {lv['tag']}: {jt}->{j2}->{jh}  ({int(time.time()-t0)}s)")
        for x in rows:
            if x.get('J') is None: print(f"    {x['tag']:>3} rank{x['nu_rank']} --"); continue
            print(f"    {x['tag']:>3} r{x['nu_rank']} l={x['l']} K={x['K']:.4f} J={x['J']:.4f} Spp={x['Spp_orbit']:.3g} "
                  f"Mu1={x['Mu1']:.3g} Mu2={x['Mu2']:.3g} Mu3={x['Mu3']:.3g} tau3={x['tau3']:.2e} "
                  f"Jmax1={x['Jmax1']} Jmax2={x['Jmax2']} Jmax3={x['Jmax3']}")
        out[str(Z)] = dict(Z=Z, ent=row['ent'], N=core['N'], Tcore=core['Tcore'], Mr1=core['Mr1'], Mr2=core['Mr2'],
                           sup_rho=core['sup_rho'], rows=rows, sec=int(time.time() - t0))
        json.dump(out, open(OUT, 'w'), indent=1)
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'canfail': sys.exit(0 if canfail() else 4)
    if a[0] == 'run': sys.exit(run([int(x) for x in a[1:]]))
    if a[0] == 'score':
        import score87; sys.exit(score87.score())
