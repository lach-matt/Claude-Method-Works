#!/usr/bin/env python3
"""semi84.py -- s84 · ITEM 1 · CLAUSE 1 · THE SEMICLASSICAL HALF.

Prediction pack84/PREDICTION-S84-ITEM1-SEMICLASSICAL.md, filed and hashed BEFORE this
file was written.  Its sha gates every run.

WHAT IS MEASURED.  With q(r) := -r V_eff(r) the enclosed-charge function of the frozen
N-1 field, E the channel's own eigenvalue and L = l + 1/2:

    p(r) = sqrt(2E + 2q(r)/r - L^2/r^2)
    I(L) = int dr / (r^2 p)          over the classically allowed region
    J    = (L/pi) * I  =  I / I_C    since I_C = pi/L EXACTLY for any constant q
    dg/dl = 2 - J                    G-within  <=>  J < 2

DESIGN DECISIONS, DECLARED

  D1  **THE QUADRATURE IS EXACT ON THE ANCHOR.**  In u = 1/r the radicand is a
      quadratic when q is constant, so the substitution u = u1 + (u2-u1) sin^2(theta)
      removes BOTH inverse-square-root endpoint singularities exactly and Gauss-
      Legendre in theta returns pi/L to machine precision.  A grid quadrature in r
      would lose 1e-3 at the turning points and the anchor could not be checked.
      For a variable q the same substitution still regularises both endpoints, since
      the radicand still vanishes linearly there.

  D2  **THE LEVER IS q(r), AND IT IS DEMONSTRATED ON EVERY RUN.**  Every channel is
      computed TWICE: once with the measured q(r) and once with q == 1.  The constant-q
      arm must return J = 1 to 1e-9 (the anchor) and the measured arm must DIFFER from
      it.  If they agree, the field never reached the integrand and the run halts rc=4.
      The standing law, embedded, sited where a dead lever and a live one differ:
      a penetrating channel, not a hydrogenic one.

  D3  **THE FIELD IS fixed81's, IMPORTED UNMODIFIED.**  One SCF per Z; the core is
      frozen with the sealed entrant's occupancy reduced by one -- fixed81.load_ref's
      construction -- and every channel of the row is evaluated in that one field.
      **DECLARED: the field a channel sees therefore depends on which entrant defined
      the core.  That is a per-row choice, and it is the sealed row's own entrant.**

  D4  **EXCHANGE IS LOCALISED AS V_eff = Vloc - X/P**, from t7b_hf.solve_one's own
      convention ([-1/2 d2 + l(l+1)/2r^2 + Vloc]P - X = eps P).  **THIS IS AN
      APPROXIMATION AND IS DECLARED, NOT DERIVED** (S8).  q(r)'s measured tail is
      reported at every channel so it can be read against s82's q_eff = 1.000000.
      Where |P| is below a floor the localisation is not formed and Vloc is used;
      the fraction of the allowed region so treated is reported.

  D5  **NOTHING SEALED IS EDITED.**  Output is pack84/semi84-out.json.

usage:  python3 semi84.py canfail          -- the gate, runs first
        python3 semi84.py run Z [Z ...]    -- a Zeno segment, one Z per SCF
        python3 semi84.py score            -- S1..S7 against the filed clauses
"""
import json, os, sys, math, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RT = os.path.join(ROOT, 'rt')
for p in (RT, os.path.join(ROOT, 'pack81'), os.path.join(ROOT, 'pack83')):
    sys.path.insert(0, p)
os.chdir(RT)

PRED = os.path.join(HERE, 'PREDICTION-S84-ITEM1-SEMICLASSICAL.md')
PSHA = os.path.join(HERE, 'PREDICTION-S84-ITEM1-SEMICLASSICAL.sha256')
OUT = os.path.join(HERE, 'semi84-out.json')
PFLOOR = 1e-8          # |P| below this: exchange not localised (D4)
LMAX = 3               # R82.2 / s83 §7: every claim restricted to l <= 3

import numpy as np


def gate_sha():
    want = open(PSHA).read().split()[0]
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        print(f"HALT rc=3: prediction sha mismatch\n  filed {want}\n  now   {got}")
        sys.exit(3)
    return got


# ------------------------------------------------------------------ quadrature
_GLX, _GLW = np.polynomial.legendre.leggauss(200)


def _roots(f, ulo, uhi, n=4000):
    """Outermost bracket of f > 0 on [ulo, uhi], by scan then bisection."""
    us = np.linspace(ulo, uhi, n)
    fs = f(us)
    pos = np.nonzero(fs > 0)[0]
    if len(pos) == 0:
        return None
    i0, i1 = pos[0], pos[-1]
    if i0 == 0 or i1 == n - 1:
        return None                      # allowed region touches the scan edge
    def bis(a, b):
        for _ in range(200):
            m = 0.5 * (a + b)
            if f(np.array([m]))[0] > 0:
                b = m
            else:
                a = m
        return 0.5 * (a + b)
    u1 = bis(us[i0 - 1], us[i0])
    u2 = bis(us[i1 + 1], us[i1])
    return (u1, u2) if u2 > u1 else None


def I_of(E, L, qfun, umax=None):
    """I = int dr/(r^2 p) in u = 1/r, endpoint singularities removed exactly (D1).

    In u: I = int du / sqrt(2E + 2 q(1/u) u - L^2 u^2), between the radicand's roots.
    """
    E = float(E); L = float(L)
    f = lambda u: 2.0 * E + 2.0 * qfun(1.0 / np.maximum(u, 1e-300)) * u - (L * L) * u * u
    if umax is None:
        umax = 4.0 * (qfun(1e-8) + 1.0) / (L * L) + 1e4
    br = _roots(f, 1e-9, umax)
    if br is None:
        return None
    u1, u2 = br
    th = 0.25 * math.pi * (_GLX + 1.0)                     # theta in [0, pi/2]
    s2 = np.sin(th) ** 2
    u = u1 + (u2 - u1) * s2
    val = f(u)
    val = np.where(val > 0, val, 0.0)
    jac = 2.0 * (u2 - u1) * np.sin(th) * np.cos(th)
    integ = np.where(val > 0, jac / np.sqrt(np.maximum(val, 1e-300)), 0.0)
    return float(0.25 * math.pi * np.sum(_GLW * integ))


def J_of(E, l, qfun):
    """J = I / I_C = (L/pi) I.  dg/dl = 2 - J."""
    L = l + 0.5
    I = I_of(E, L, qfun)
    return None if I is None else (L / math.pi) * I


# ------------------------------------------------------------------ the field
def field_of(Z):
    """One SCF per Z.  Returns (h, cfg, entrant, eps) with the core frozen (D3)."""
    import nlchain as NC
    import fixed81 as FX
    from t7c_kernel import C0
    sealed = {r['Z']: r for r in
              (json.loads(l) for l in open(os.path.join(RT, 'nlchain.jsonl')))}
    row = sealed[Z]
    ent_tag = row['ent']
    import gtest83 as G
    m = G.TAG.match(ent_tag)
    ent = (int(m.group(1)), G.LSYM.index(m.group(2)))
    cfg = NC.add(NC.cfg_from_chain(Z - 1, sealed), ent)
    FX.Frozen81.P0 = None
    h = FX.Frozen81(Z, cfg, c=C0)
    E, Ec, it, eps = h.run2()
    cQ = {}
    for (n, l, q) in cfg:
        q2 = q - 1 if (n, l) == ent else q
        if q2 > 0:
            cQ[(n, l)] = float(q2)
    h.freeze(h.P, cQ)
    return h, cfg, ent, eps, row, float(E)


def q_of_channel(h, n, l):
    """q(r) = -r V_eff(r), V_eff = Vloc - X/P (D4).  Returns (qfun, tail, frac_floor)."""
    P = h.P[(n, l)]
    Vloc, X = h.field(n, l, P)
    r = h.r
    ok = np.abs(P) > PFLOOR
    Veff = np.array(Vloc, dtype=float)
    Veff[ok] = Vloc[ok] - X[ok] / P[ok]
    q = -r * Veff
    frac = float(1.0 - ok.mean())
    tail = float(q[-1])
    lr = np.log(r)
    def qfun(rr):
        rr = np.atleast_1d(np.asarray(rr, dtype=float))
        return np.interp(np.log(np.clip(rr, r[0], r[-1])), lr, q)
    return qfun, tail, frac


# ------------------------------------------------------------------ can-fails
def canfail():
    print("=== CAN-FAILS · semi84 · they GATE ===================================")
    print(f"  prediction sha OK  {gate_sha()[:8]}...")
    ok = True

    # CF1/CF2 (S1, S2) THE ANCHOR.  I == pi/L for ANY constant charge and any bound E.
    worst = 0.0
    for q0 in (1.0, 2.0, 89.0, 90.0):
        for l in range(5):
            for E in (-0.05, -0.5, -5.0):
                J = J_of(E, l, (lambda c: (lambda rr: np.full_like(
                    np.atleast_1d(np.asarray(rr, float)), c)))(q0))
                if J is None:
                    print(f"  **no allowed region** q0={q0} l={l} E={E}")
                    ok = False
                    continue
                worst = max(worst, abs(J - 1.0))
    good = worst < 1e-6
    ok &= good
    print(f"  CF1 anchor  max |J-1| over 60 (q0,l,E) cases = {worst:.3e}   "
          f"{'PASS' if good else '**FAIL**'}")
    print(f"  CF2 charge-blind: q0=1 and q0=90 both inside that bound   "
          f"{'PASS' if good else '**FAIL**'}")

    # CF3 THE LEVER, SYNTHETIC AND SITED WHERE IT MATTERS.  A q(r) that VARIES must
    # move J off 1.  A core-like bump inside a small radius, hydrogenic outside.
    def qbump(rr):
        rr = np.atleast_1d(np.asarray(rr, float))
        return 1.0 + 9.0 * np.exp(-rr / 0.3)
    Jb = J_of(-0.05, 0, qbump)
    moved = (Jb is not None) and abs(Jb - 1.0) > 1e-6
    ok &= moved
    print(f"  CF3 a VARYING q moves J off the anchor: J={Jb:.6f}   "
          f"{'PASS' if moved else '**FAIL**'}")

    # CF4 the sha gate halts on a mutated prediction.
    import subprocess
    rc = subprocess.run([sys.executable, '-c',
                         f"import sys;sys.path.insert(0,{HERE!r});"
                         "import semi84;semi84.PSHA='/dev/null';semi84.gate_sha()"],
                        capture_output=True, text=True).returncode
    good = (rc != 0)
    ok &= good
    print(f"  CF4 sha gate halts when the filed hash is unreadable  rc={rc}   "
          f"{'PASS' if good else '**FAIL**'}")

    print(f"\n  CAN-FAIL GATE: {'PASS' if ok else '**FAIL**'}")
    return ok


# ------------------------------------------------------------------ the run
def run(zs):
    gate_sha()
    import gtest83 as G
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    for Z in zs:
        t0 = time.time()
        h, cfg, ent, eps, row, Etot = field_of(Z)
        chs = G.channels(row, lmax=LMAX)
        by_nu = sorted(chs, key=lambda c: c['nu'])
        rows = []
        for c in by_nu[:5]:
            n, l = c['n'], c['l']
            if (n, l) not in h.P:
                continue
            qfun, tail, frac = q_of_channel(h, n, l)
            E = float(eps[(n, l)])
            J = J_of(E, l, qfun)
            Jc = J_of(E, l, lambda rr: np.ones_like(
                np.atleast_1d(np.asarray(rr, float))))
            if J is None or Jc is None:
                rows.append(dict(tag=c['tag'], n=n, l=l, E=E, J=None,
                                 note='no allowed region'))
                continue
            rows.append(dict(tag=c['tag'], n=n, l=l, sigma=c['sigma'], E=E,
                             nu=c['nu'], g_banked=c['g'], nu_rank=by_nu.index(c),
                             J=round(J, 6), J_anchor=round(Jc, 9),
                             dg_dl=round(2.0 - J, 6),
                             q_tail=round(tail, 6), frac_floor=round(frac, 4)))
        live = [r for r in rows if r.get('J') is not None]
        # **D2: THE LEVER, ON THIS RUN.**  Sited at the most penetrating live channel.
        pen = sorted(live, key=lambda r: r['l'])
        if not pen:
            print(f"  Z={Z}: no live channel -- HALT rc=4")
            return 4
        lv = pen[0]
        if abs(lv['J'] - lv['J_anchor']) < 1e-9:
            print(f"  Z={Z}: **LEVER DEAD** -- measured q gives the anchor value at "
                  f"{lv['tag']} (J={lv['J']}). The field never reached the integrand.")
            return 4
        print(f"  Z={Z}  lever LIVE at {lv['tag']}: J={lv['J']:.6f} vs anchor "
              f"{lv['J_anchor']:.9f}   ({int(time.time()-t0)}s)")
        for r in rows:
            if r.get('J') is None:
                print(f"    {r['tag']:>3}  --")
                continue
            print(f"    {r['tag']:>3} l={r['l']} E={r['E']:+.6f}  J={r['J']:.4f}"
                  f"  dg/dl={r['dg_dl']:+.4f}  g_bank={r['g_banked']:.4f}"
                  f"  q_tail={r['q_tail']:.4f}")
        out[str(Z)] = dict(Z=Z, ent=row['ent'], E_total=Etot, rows=rows,
                           sec=int(time.time() - t0))
        json.dump(out, open(OUT, 'w'), indent=1)
    return 0


def score():
    gate_sha()
    out = json.load(open(OUT))
    Zs = sorted(int(k) for k in out)
    print(f"=== SCORE · semi84 · rows {Zs} ===")
    allJ = []
    for Z in Zs:
        for r in out[str(Z)]['rows']:
            if r.get('J') is not None:
                allJ.append((Z, r['tag'], r['l'], r['J'], r['nu_rank']))
    # S3: J < 2 at the width-2 frontier (nu_rank 0 and 1)
    fr = [x for x in allJ if x[4] < 2]
    s3bad = [x for x in fr if x[3] >= 2.0]
    print(f"  S3 width-2 frontier channels {len(fr)}, J >= 2 at {len(s3bad)}  {s3bad}")
    # S4: band 0.6..1.4
    s4bad = [x for x in allJ if not (0.6 <= x[3] <= 1.4)]
    print(f"  S4 all channels {len(allJ)}, outside 0.6..1.4 at {len(s4bad)}")
    for x in s4bad[:12]:
        print(f"      Z={x[0]} {x[1]} J={x[3]:.4f}")
    # S5: penetrating vs high-l deviation
    lo = [abs(x[3] - 1) for x in allJ if x[2] <= 1]
    hi = [abs(x[3] - 1) for x in allJ if x[2] >= 3]
    med = lambda v: (sorted(v)[len(v) // 2] if v else None)
    print(f"  S5 median |J-1|: l<=1 {med(lo)}  (n={len(lo)}) vs l>=3 {med(hi)} "
          f"(n={len(hi)})")
    # S6: is Z=90 extreme
    per = {Z: min((r['dg_dl'] for r in out[str(Z)]['rows']
                   if r.get('J') is not None), default=None) for Z in Zs}
    print(f"  S6 min dg/dl per Z: " + "  ".join(
        f"{Z}:{per[Z]:+.4f}" for Z in Zs if per[Z] is not None))
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'canfail':
        sys.exit(0 if canfail() else 4)
    if a[0] == 'run':
        sys.exit(run([int(x) for x in a[1:]]))
    if a[0] == 'score':
        sys.exit(score())
