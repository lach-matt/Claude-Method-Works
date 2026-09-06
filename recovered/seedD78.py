"""seedD78.py -- s78 ITEM 2. SEED D and its PHASE-A can-fail.
SEED D: shell-wise screened hydrogenic. Each orbital (n,l) is solved in a PURE COULOMB
potential -Zeff(n)/r with Zeff(n) = Z - (number of electrons in shells of lower principal
quantum number), floored at 1. NO TFD, NO Latter tail, NO exchange, NO statistical model,
and NO fitted constant -- Zeff is an INTEGER COUNT read off the occupancy. c is still the
only number entered anywhere.
  Physically unlike A: A is a Thomas-Fermi-Dirac statistical potential with a Latter tail.
  Constructible at high Z, unlike C, whose SCF (not whose constructor -- F78.1) dies at 89.
usage:  python3 pack78/seedD78.py A          PHASE-A can-fail, no SCF   rc=0 PASS, rc=4 VOID
        python3 pack78/seedD78.py S Z        first-sweep survival probe at Z
"""
import sys, os, json, time
import numpy as np
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
sys.path.insert(0, os.getcwd())
import t7b_hf
from hfs import numerov_wf
import nlchain as NC
import hfc2 as H
from t7c_kernel import C0
H.CORR = False
BASE = t7b_hf.HF.seed
L = "spdfg"

def zeff_map(Z, occ):
    """Zeff(n) = Z - (electrons in shells with smaller n). Integers only."""
    ns = sorted({n for n, l, q in occ})
    inner = {}
    for n in ns:
        inner[n] = sum(q for (a, b, q) in occ if a < n)
    return {n: max(1.0, float(Z) - float(inner[n])) for n in ns}

def seed_A(self, qtail=1):
    return BASE(self, 1)

def seed_D(self, qtail=1):
    Z = self.Z
    ze = zeff_map(Z, self.occ)
    P = {}; eps = {}
    for n, l, q in self.occ:
        Vf = (lambda zz: (lambda rr: -zz / np.asarray(rr, float)))(ze[n])
        rr, drr, u, E, nd = numerov_wf(Vf, l, n, 1.0, Z)
        if nd != n - l - 1:
            raise RuntimeError(f"seed_D Z={Z} {n}{L[l]} nodes {nd}")
        ui = np.interp(self.r, rr, u, left=0.0, right=0.0)
        ui /= np.sqrt(np.sum(ui * ui * self.dr))
        P[(n, l)] = ui; eps[(n, l)] = E
    return P, eps

SEEDS = {"A": seed_A, "D": seed_D}
def install(tag): t7b_hf.HF.seed = SEEDS[tag]
def chain_cfg(Z):
    rows = NC.load(); return [tuple(x) for x in NC.cfg_from_chain(Z - 1, rows)], rows

# thresholds, declared before the run
T_MAX = 10.0      # max|d_eps| over all orbitals, Ha.  seed C scored 51.9 at Z=19.
T_VAL = 0.05      # valence |d_eps|, Ha.  the same bar phase_A applies to seed C.

def phase_A(Zs=(19, 89)):
    """CAN-FAIL: seed D must MOVE the start, at BOTH a light and the tightest row.
    rc=4 and the word VOID if it does not.  Reachable by the driver: the driver calls
    this and refuses to run when rc != 0."""
    print("PHASE A -- can-fail the seed D switch (no SCF)")
    out = {}; verdict = "PASS"
    for Z in Zs:
        cfg, rows = chain_cfg(Z)
        got = {}
        for tag in ("A", "D"):
            install(tag)
            h = H.HFC(Z, cfg, c=C0)
            try:
                P, eps = h.seed(1)
            except Exception as e:
                print(f"  Z={Z} seed {tag}: CONSTRUCTOR FAILED {type(e).__name__}: {e}")
                verdict = "VOID"; got[tag] = None; continue
            got[tag] = {f"{n}{L[l]}": float(e) for (n, l), e in eps.items()}
        if got.get("A") is None or got.get("D") is None:
            continue
        d = {k: got["D"][k] - got["A"][k] for k in got["A"]}
        mx = max(abs(v) for v in d.values())
        kmx = max(d, key=lambda k: abs(d[k]))
        val = max(got["A"], key=lambda k: (int(k[:-1]), L.index(k[-1])))
        print(f"  Z={Z:3d}  A->D  max|d_eps| = {mx:10.6f} Ha at {kmx}"
              f"   valence {val} d = {d[val]:+.5f} Ha")
        out[str(Z)] = dict(maxd=mx, at=kmx, val=val, dval=d[val], A=got["A"], D=got["D"])
        if mx <= T_MAX:
            print(f"  *** VOID Z={Z}: max|d_eps| {mx:.6f} <= {T_MAX} Ha. Seed D is not a"
                  f" comparable displacement to seed C's 51.9 Ha."); verdict = "VOID"
        if abs(d[val]) <= T_VAL:
            print(f"  *** VOID Z={Z}: valence differs by only {abs(d[val]):.5f} <= {T_VAL} Ha.")
            verdict = "VOID"
    print(f"PHASE A: {verdict}")
    json.dump(dict(verdict=verdict, T_MAX=T_MAX, T_VAL=T_VAL, rows=out),
              open("../pack78/seedD78_phaseA.json", "w"), indent=1)
    return 0 if verdict == "PASS" else 4

def survive(Z, maxit=2):
    """first-sweep survival: does the SCF track every node count from seed D?"""
    cfg, rows = chain_cfg(Z)
    install("D")
    t0 = time.time()
    try:
        E, Ec, it, eps = H.HFC(Z, cfg, c=C0).run2(maxit=maxit)
        print(f"  Z={Z} seed D: {maxit} SWEEP(S) SURVIVED  E={E:.6f} it={it} {time.time()-t0:.0f}s")
        return 0
    except Exception as e:
        print(f"  Z={Z} seed D: SWEEP FAILED {type(e).__name__}: {e}  ({time.time()-t0:.0f}s)")
        return 4

if __name__ == "__main__":
    m = sys.argv[1]
    if m == "A": sys.exit(phase_A())
    if m == "S": sys.exit(survive(int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 2))