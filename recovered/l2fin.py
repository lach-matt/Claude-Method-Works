"""l2fin.py -- SESSION 64. THE L2 MEASUREMENT: what the point nucleus costs the answer.
Scored against pack64/PREDICTION-L2-FINITE-NUCLEUS.md
sha 5765c6d00d2d4325c210c3fb5f330806c5db6a3ffab74a1d216da3b3035ee0e5 (filed 20:53:46Z).

EDITS NOTHING. It converges a configuration on the ruling path exactly as
nlguard.run_guarded does -- same LADDER, same rung order, same c -- then evaluates
first-order perturbation theory on the CONVERGED orbitals:

    dE = sum_a q_a INT P_a(r)^2 [V_fin(r) - V_pt(r)] dr

V_fin is the uniformly charged sphere of radius R = 1.2 A^(1/3) fm. The integral form
is used, not |psi(0)|^2, because the scalar-relativistic P diverges mildly at the
origin at high Z and a density-at-a-point is undefined there.

usage: python3 l2fin.py Z A cfgspec [cfgspec ...]
       cfgspec is 'ref' or a channel tag like '6d'. Results cached per (Z,cfg) so a
       killed call costs only what has not succeeded (F64.2 / §2.20).
"""
import os, sys, json, time
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
import numpy as np
import hfc2 as H
from t7c_kernel import C0
import ground as G
import nlguard as NG
import nlchain as C
H.CORR = False

HERE = os.path.dirname(os.path.abspath(__file__))
FM = 1.8897261246e-5           # 1 femtometre in bohr


def R_nuc(A):
    return 1.2 * A ** (1.0 / 3.0) * FM


def dV(r, Z, A):
    """V_finite - V_point on the mesh. Zero outside R by construction."""
    R = R_nuc(A)
    out = np.zeros_like(r)
    i = r < R
    out[i] = -(Z / (2 * R)) * (3.0 - (r[i] / R) ** 2) + Z / r[i]
    return out


def converge(Z, cfg):
    """The ruling path, rung by rung, returning the HFC object that converged."""
    for rung, (beta, maxit) in enumerate(NG.LADDER):
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C0)
        E, _, it, eps = h.run2(beta=beta, maxit=maxit)
        if it < maxit:
            return h, float(E), it, rung
    raise RuntimeError(f"Z={Z}: cycled at every rung")


def shift(h, Z, A):
    """dE and the per-orbital breakdown, on the converged orbitals."""
    r, dr = h.r, h.dr
    d = dV(r, Z, A)
    tot, per = 0.0, {}
    occ = {(n, l): q for n, l, q in h.occ}
    for a, P in h.P.items():
        q = occ[a]
        e = float(q * np.sum(P * P * d * dr))
        per[f"{a[0]}{'spdfg'[a[1]]}"] = e
        tot += e
    return tot, per


def main():
    Z, A = int(sys.argv[1]), int(sys.argv[2])
    specs = sys.argv[3:]
    cache_p = os.path.join(HERE, f".l2_Z{Z}.json")
    cache = json.load(open(cache_p)) if os.path.exists(cache_p) else {}

    cfg_ref = G.expand(Z - 1)
    for spec in specs:
        if spec in cache:
            continue
        if spec == 'ref':
            cfg = cfg_ref
        else:
            n = int(spec[0]); l = 'spdfg'.index(spec[1])
            cfg = C.add(cfg_ref, (n, l))
        t0 = time.time()
        h, E, it, rung = converge(Z, cfg)
        tot, per = shift(h, Z, A)
        cache[spec] = dict(E=E, it=it, rung=rung, dE=tot, per=per,
                           sec=int(time.time() - t0),
                           cfg=''.join(f"{n}{'spdfg'[l]}{q:g}" for n, l, q in cfg))
        json.dump(cache, open(cache_p + '.tmp', 'w')); os.replace(cache_p + '.tmp', cache_p)
        print(f"  Z={Z} {spec:>4}  E={E:.6f} rung={rung}  dE={tot:.6e} Ha  ({cache[spec]['sec']}s)",
              flush=True)

    if all(s in cache for s in specs) and 'ref' in cache:
        print(f"\n  R_nuc(A={A}) = {R_nuc(A):.6e} bohr;  mesh r_min = {converge.__name__ and ''}")
        print(f"  {'chan':>5} {'dE(cfg+c)':>14} {'dD from L2':>14} {'|dD| mHa':>12} {'|dD|/dE':>10}")
        base = cache['ref']['dE']
        for s in specs:
            if s == 'ref':
                continue
            dD = cache[s]['dE'] - base
            print(f"  {s:>5} {cache[s]['dE']:>14.6e} {dD:>14.6e} {abs(dD)*1000:>12.5f} "
                  f"{abs(dD)/abs(base):>10.2e}")
        print(f"\n  dE(ref) = {base:.6e} Ha   per-orbital top 4: "
              f"{sorted(cache['ref']['per'].items(), key=lambda kv: kv[1])[:4]}")


if __name__ == '__main__':
    main()
