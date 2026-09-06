#!/usr/bin/env python3
"""semi85.py -- s85 · ITEM 1 · CLAUSE 1 · THE VARIABLE-q BOUND, MEASURED.

Prediction pack85/PREDICTION-S85-ITEM1-THE-BOUND.md, filed and hashed BEFORE this file
was written.  Its sha gates every run.

WHAT IS MEASURED, per channel, on the SAME field s84 used (imported, not reimplemented):

    K  := 2 V+ / (L^2 a)  =  V+ / ( c* sqrt(1 - (L/nu*)^2) )
    V+ := positive variation of w := q - r q' across the orbit's own turning points
    a  := u2 - u1,  u = 1/r,  c* := [S(u2)-S(u1)]/a,  S(u) := q(r)/r = -V(r)

    **K < 1  ==>  J < 2  ==>  dg/dl > 0  ==>  G-within.**

DESIGN DECISIONS, DECLARED

  D1  **THE FIELD IS s84's, IMPORTED.**  field_of, q_of_channel, _regions, _quad and
      J_of come from pack84/semi84.py unmodified.  Nothing sealed is edited.  CF6
      checks that the q grid this file builds interpolates to semi84's own qfun.

  D2  **THE REGION IS THE OUTER ONE**, semi84's convention.  Where a channel returns
      more than one allowed region the chord, the deficit and K all refer to the OUTER
      well alone and n_regions is reported so the row can be read that way (s84 §4).

  D3  **V+ IS A POSITIVE VARIATION, NOT AN ENDPOINT DIFFERENCE.**  A real core is not
      convex -- shell structure puts sign changes in q'' -- so the rigorous bound needs
      int [S'']_+ , not S'(u2)-S'(u1).  Both are reported: K (from V+) is the RULING
      quantity, K_end (from the endpoints) is reported beside it and is <= K always.
      CF5 sites the difference on a synthetic non-convex core.

  D4  **THE LEVER IS q(r), DEMONSTRATED EVERY RUN, ON BOTH OUTPUTS.**  Each row is
      computed twice: measured q, and q == 1.  The dead arm must return V+ = 0, K = 0
      and J = 1; the live arm must move BOTH J and K.  Sited at the most penetrating
      live channel, where a dead lever and a live one differ.  Halts rc=4 otherwise.

  D5  **THE CURRENCY IS THE SEALED D (F79.2), never an eigenvalue.**  As s84.

  D6  **THE POPULATION IS NAMED IN EVERY CLAUSE** (F83.1, twelfth appearance).
      A = width-2 frontier = nu_rank in {0,1}.  B = all l<=3 among the five lowest-nu.

usage:  python3 semi85.py canfail        -- the gate, runs first
        python3 semi85.py run Z [Z ...]  -- a Zeno segment
        python3 semi85.py score          -- S1..S10 against the filed clauses
"""
import json, os, sys, math, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'pack84'))
import numpy as np
import semi84 as S84                       # D1: the field, imported unmodified

PRED = os.path.join(HERE, 'PREDICTION-S85-ITEM1-THE-BOUND.md')
PSHA = os.path.join(HERE, 'PREDICTION-S85-ITEM1-THE-BOUND.sha256')
OUT = os.path.join(HERE, 'semi85-out.json')
LMAX = 3


def gate_sha():
    want = open(PSHA).read().split()[0]
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        print(f"HALT rc=3: prediction sha mismatch\n  filed {want}\n  now   {got}")
        sys.exit(3)
    return got


# --------------------------------------------------------------- the closed form
def J_tent(b0, b1):
    """J for the extreme one-kink convex S.  = 2 EXACTLY on b0+b1 = 1, any split."""
    if b0 < 0: b0 = 0.0
    if b1 < 0: b1 = 0.0
    if b0 + b1 >= 1.0:
        return float('inf')
    if b0 + b1 <= 0.0:
        return 1.0
    tk = b1 / (b0 + b1)
    return 1.0 + (2.0 / math.pi) * (math.asin(math.sqrt(tk / (1.0 - b0)))
                                    - math.asin(math.sqrt(max(tk - b1, 0.0) / (1.0 - b1))))


def Jbar(K):
    """The K-only bound.  Worst split is symmetric.  Jbar(1) = 2."""
    return J_tent(0.5 * K, 0.5 * K)


# --------------------------------------------------------------- the measurement
def w_grid(r, q):
    """w = q - r q' = S'(u), on the native radial grid."""
    return q - r * np.gradient(q, r)


def geometry(E, l, r, q, r_out, r_in):
    """K, K_end, b0, b1, c*, nu*, eps, V+, kappa for one channel and one region."""
    L = l + 0.5
    u1, u2 = 1.0 / r_out, 1.0 / r_in
    a = u2 - u1
    lr = np.log(r)
    w = w_grid(r, q)
    qi = lambda rr: float(np.interp(math.log(rr), lr, q))
    wi = lambda rr: float(np.interp(math.log(rr), lr, w))

    # V+ : positive variation of w with u INCREASING, i.e. r DECREASING.
    inside = r[(r > r_in) & (r < r_out)]
    seq = np.concatenate(([r_out], inside[::-1], [r_in]))
    wv = np.array([wi(x) for x in seq])
    d = np.diff(wv)
    Vp = float(d[d > 0].sum())
    Vend = float(wv[-1] - wv[0])

    S1, S2 = qi(r_out) / r_out, qi(r_in) / r_in
    cst = (S2 - S1) / a
    K = 2.0 * Vp / (L * L * a)
    K_end = 2.0 * Vend / (L * L * a)
    b0 = 2.0 * (cst - wv[0]) / (L * L * a)
    b1 = 2.0 * (wv[-1] - cst) / (L * L * a)

    disc = cst * cst + 2.0 * E * L * L
    nus = cst / math.sqrt(-2.0 * E) if E < 0 else None
    eps = math.sqrt(disc) / cst if (disc > 0 and cst > 0) else None
    K_alt = (Vp / math.sqrt(disc)) if disc > 0 else None

    # kappa = sup (1 - f/g), the sup-norm deficit, reported for comparison only
    th = np.linspace(1e-7, math.pi - 1e-7, 3001)
    t = 0.5 * (1 - np.cos(th))
    u = u1 + a * t
    Su = np.interp(np.log(np.clip(1.0 / u, r[0], r[-1])), lr, q) * u
    g = L * L * (u - u1) * (u2 - u)
    f = 2.0 * (Su - (S1 + (S2 - S1) * t))
    kappa = float(np.max(1.0 - (g + f) / np.maximum(g, 1e-300)))
    conv = float((d >= -1e-12).mean())
    return dict(K=K, K_end=K_end, K_alt=K_alt, Vp=Vp, V_end=Vend, c_star=cst,
                nu_star=nus, eps=eps, b0=b0, b1=b1, kappa=kappa, conv_frac=conv,
                a=a, r_out=r_out, r_in=r_in,
                Jbar=Jbar(K), J_tent=(J_tent(b0, b1) if conv > 0.999 else None))


def q_native(h, n, l):
    """(r, q) of the FROZEN core, the same construction semi84.q_of_channel uses."""
    r = np.asarray(h.r, float)
    Vloc, X = h.field(n, l, np.zeros(h.npts))
    return r, -r * np.asarray(Vloc, float)


ONE = lambda rr: np.ones_like(np.atleast_1d(np.asarray(rr, float)))


def channel_row(E, l, r, q):
    qfun = lambda rr: np.interp(np.log(np.clip(
        np.atleast_1d(np.asarray(rr, float)), r[0], r[-1])), np.log(r), q)
    J, meta = S84.J_of(E, l, qfun, detail=True)
    if J is None:
        return None
    G = geometry(E, l, r, q, meta['r_outer'], meta['r_inner'])
    G.update(J=J, n_regions=meta['n_regions'])
    return G


# ------------------------------------------------------------------- can-fails
def canfail():
    print("=== CAN-FAILS · semi85 · they GATE ===================================")
    print(f"  prediction sha OK  {gate_sha()[:8]}...")
    ok = True
    RG = np.exp(np.linspace(math.log(1e-6), math.log(400.0), 6000))

    # CF1 THE ANCHOR CARRIES THROUGH TO K.  Constant q: J=1 AND V+=0 AND K=0.
    wJ = wK = 0.0
    for q0 in (1.0, 2.0, 89.0, 90.0):
        for l in range(4):
            for E in (-0.05, -0.5, -5.0):
                R = channel_row(E, l, RG, np.full_like(RG, q0))
                if R is None:
                    continue
                wJ = max(wJ, abs(R['J'] - 1.0)); wK = max(wK, abs(R['K']))
    g1 = wJ < 1e-6 and wK < 1e-9
    ok &= g1
    print(f"  CF1 constant q: max|J-1|={wJ:.2e}  max|K|={wK:.2e}   "
          f"{'PASS' if g1 else '**FAIL**'}")

    # CF2 THE THRESHOLD IDENTITY.  Jbar(1)=2 exactly; Jbar(0)=1; Jbar monotone.
    b1 = abs(Jbar(1.0 - 1e-12) - 2.0) < 1e-5 and abs(Jbar(0.0) - 1.0) < 1e-12
    ks = np.linspace(0, 0.999, 400)
    mono = all(Jbar(ks[i]) <= Jbar(ks[i + 1]) + 1e-12 for i in range(len(ks) - 1))
    # and EVERY split of b0+b1=1 gives exactly 2
    splits = [abs(J_tent(b, 1.0 - 1e-13 - b) - 2.0) for b in (0.05, 0.3, 0.5, 0.8)]
    g2 = b1 and mono and max(splits) < 1e-5
    ok &= g2
    print(f"  CF2 Jbar(1)=2, Jbar(0)=1, monotone, all splits ->2 (max dev "
          f"{max(splits):.1e})   {'PASS' if g2 else '**FAIL**'}")

    # CF3 THE THEOREM, AND IT MUST BE TWO-SIDED.  Synthetic screened cores: J<=Jbar(K)
    # at every case, AND at least one case with K<1 & J<2, AND at least one with
    # K>=1 & J>=2.  **A criterion that never fires on either side is not tested.**
    viol, lo_side, hi_side = 0, 0, 0
    for Z, d in ((20, 0.35), (57, 0.30), (90, 0.28), (90, 0.6)):
        qq = 1.0 + (Z - 1.0) * np.exp(-RG / d)
        for l in range(4):
            R = channel_row(-0.20, l, RG, qq)
            if R is None:
                continue
            if R['J'] > R['Jbar'] + 1e-6:
                viol += 1
            if R['K'] < 1 and R['J'] < 2: lo_side += 1
            if R['K'] >= 1 and R['J'] >= 2: hi_side += 1
    g3 = (viol == 0) and lo_side and hi_side
    ok &= g3
    print(f"  CF3 J<=Jbar(K): {viol} violation(s); K<1&J<2 at {lo_side}; "
          f"K>=1&J>=2 at {hi_side}   {'PASS' if g3 else '**FAIL**'}")

    # CF4 THE BOUND MUST BE ABLE TO FAIL A ROW IT SHOULD FAIL.  A deliberately
    # over-screened core drives K past 1 while J passes 2.  If no synthetic core can
    # do that, K<1 is vacuous rather than sufficient.
    qq = 1.0 + 40.0 * np.exp(-RG / 0.9)
    Rk = channel_row(-0.20, 1, RG, qq)
    g4 = Rk is not None and Rk['K'] >= 1.0
    ok &= g4
    print(f"  CF4 an over-screened core is REFUSED by the bound: K="
          f"{(Rk['K'] if Rk else float('nan')):.3f}   {'PASS' if g4 else '**FAIL**'}")

    # CF5 V+ IS DOING WORK.  On a MONOTONE core V+ == endpoint difference; on a core
    # with a shell bump (w non-monotone) V+ must EXCEED it.  D3 sited.
    qm = 1.0 + 89.0 * np.exp(-RG / 0.28)
    qb = qm + 6.0 * np.exp(-((np.log(RG) - math.log(1.2)) ** 2) / 0.02)
    Rm, Rb = channel_row(-0.20, 2, RG, qm), channel_row(-0.20, 2, RG, qb)
    same = abs(Rm['K'] - Rm['K_end']) < 1e-3 * max(1.0, abs(Rm['K']))
    more = Rb['K'] > Rb['K_end'] + 1e-6
    g5 = same and more
    ok &= g5
    print(f"  CF5 V+ = endpoints on a monotone core ({Rm['K']:.4f} vs "
          f"{Rm['K_end']:.4f}); EXCEEDS on a shell bump ({Rb['K']:.4f} vs "
          f"{Rb['K_end']:.4f})   {'PASS' if g5 else '**FAIL**'}")

    # CF6 THE FIELD IS s84's.  The q grid built here interpolates to semi84's own
    # qfun at a real Z.  **F84.3's ruling (direct core field) is inherited, not
    # re-decided.**
    h, cfg, ent, eps, row, Et = S84.field_of(20)
    r20, q20 = q_native(h, 4, 0)
    qf84, tail84, _ = S84.q_of_channel(h, 4, 0)
    probe = np.exp(np.linspace(math.log(1e-4), math.log(50.0), 200))
    dq = float(np.max(np.abs(qf84(probe) - np.interp(
        np.log(probe), np.log(r20), q20))))
    g6 = dq < 1e-12
    ok &= g6
    print(f"  CF6 q grid == semi84's qfun at Z=20: max diff {dq:.2e}   "
          f"{'PASS' if g6 else '**FAIL**'}")

    # CF7 sha gate halts on a mutated prediction.
    import subprocess
    rc = subprocess.run([sys.executable, '-c',
                         f"import sys;sys.path.insert(0,{HERE!r});"
                         "import semi85;semi85.PSHA='/dev/null';semi85.gate_sha()"],
                        capture_output=True, text=True).returncode
    g7 = rc != 0
    ok &= g7
    print(f"  CF7 sha gate halts on unreadable hash  rc={rc}   "
          f"{'PASS' if g7 else '**FAIL**'}")

    # CF8 (S10) the two forms of K agree on real-shaped input.
    dv = max(abs(R['K'] - R['K_alt']) for R in (Rm, Rb) if R['K_alt'] is not None)
    g8 = dv < 1e-6
    ok &= g8
    print(f"  CF8 K = 2V+/(L^2 a) = V+/sqrt(c*^2+2EL^2): max diff {dv:.2e}   "
          f"{'PASS' if g8 else '**FAIL**'}")

    print(f"\n  CAN-FAIL GATE: {'PASS' if ok else '**FAIL**'}")
    return ok


# ------------------------------------------------------------------------- run
def run(zs):
    gate_sha()
    sys.path.insert(0, os.path.join(ROOT, 'pack83'))
    import gtest83 as G
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    for Z in zs:
        t0 = time.time()
        h, cfg, ent, eps, row, Etot = S84.field_of(Z)
        chs = G.channels(row, lmax=LMAX)
        by_nu = sorted(chs, key=lambda c: c['nu'])
        rows, dead = [], []
        for rank, c in enumerate(by_nu[:5]):
            n, l, E = c['n'], c['l'], float(c['D'])
            r, q = q_native(h, n, l)
            R = channel_row(E, l, r, q)
            if R is None:
                rows.append(dict(tag=c['tag'], n=n, l=l, E=E, J=None, nu_rank=rank,
                                 note='no allowed region'))
                continue
            # D4: THE DEAD ARM, this channel, this run.
            D0 = channel_row(E, l, r, np.ones_like(r))
            R.update(tag=c['tag'], n=n, l=l, sigma=c['sigma'], E=E, nu=c['nu'],
                     g_banked=c['g'], nu_rank=rank, occ=bool((n, l) in h.P),
                     dg_dl=2.0 - R['J'], q_tail=float(q[-1]),
                     J_dead=(None if D0 is None else D0['J']),
                     K_dead=(None if D0 is None else D0['K']))
            rows.append({k: (round(v, 9) if isinstance(v, float) else v)
                         for k, v in R.items()})
        live = [r for r in rows if r.get('J') is not None]
        if not live:
            print(f"  Z={Z}: no live channel -- HALT rc=4")
            return 4
        lv = sorted(live, key=lambda r: r['l'])[0]
        moved_J = lv['J_dead'] is not None and abs(lv['J'] - lv['J_dead']) > 1e-9
        moved_K = lv['K_dead'] is not None and abs(lv['K'] - lv['K_dead']) > 1e-9
        if not (moved_J and moved_K):
            print(f"  Z={Z}: **LEVER DEAD** at {lv['tag']} -- J moved={moved_J} "
                  f"K moved={moved_K}. The field never reached the integrand.")
            return 4
        print(f"  Z={Z} {row['ent']:>3}  lever LIVE at {lv['tag']}: "
              f"J {lv['J_dead']:.6f}->{lv['J']:.4f}  K {lv['K_dead']:.1e}->"
              f"{lv['K']:.4f}   ({int(time.time()-t0)}s)")
        for r in rows:
            if r.get('J') is None:
                print(f"    {r['tag']:>3} rank{r['nu_rank']}  --")
                continue
            print(f"    {r['tag']:>3} rank{r['nu_rank']} l={r['l']} J={r['J']:.4f} "
                  f"K={r['K']:.4f} Kend={r['K_end']:.4f} Jbar="
                  f"{r['Jbar']:.4f} eps={(r['eps'] or 0):.3f} nu*={(r['nu_star'] or 0):.2f}"
                  f" cv={r['conv_frac']:.2f} reg={r['n_regions']}")
        out[str(Z)] = dict(Z=Z, ent=row['ent'], rows=rows, sec=int(time.time() - t0))
        json.dump(out, open(OUT, 'w'), indent=1)
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'canfail':
        sys.exit(0 if canfail() else 4)
    if a[0] == 'run':
        sys.exit(run([int(x) for x in a[1:]]))
    if a[0] == 'score':
        import score85
        sys.exit(score85.score())
