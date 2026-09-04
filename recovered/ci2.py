"""ci2.py -- s73, R-C(a). THE RADIAL HALF: the MAGNITUDE of V. Scores CI-6.

Object: V = <A|H|B> for two determinants on ONE common orbital set differing by exactly
one spin-orbital, a -> b, same spin (pack73/DERIVATION-CI6-SECTOR.md fixes which two).
Slater-Condon single replacement:

    V = <a|h|b>  +  SUM_{k in common} [ <ak|g|bk> - delta(ms_a,ms_k) <ak|g|kb> ]

    <ak|g|bk> = SUM_kap c^kap(la ma; lb mb) c^kap(lk mk; lk mk) R^kap(a k; b k)
    <ak|g|kb> = SUM_kap c^kap(la ma; lk mk) c^kap(lk mk; lb mb) R^kap(a k; k b)

    R^kap(a b; c d) = int P_a P_c Y^kap(P_b,P_d)/r dr        (h.Yk, SEALED)

c^kap is hfterm.ck (SEALED). No CG recoupling: this is (a), not (b).
No constant beyond c. Nothing empirical enters V.

DESIGN DECISION, MADE BEFORE ANY NUMBER IS READ: the common orbital set is the HFSR
average-of-configuration solution of configuration A (the observed configuration) at that Z.
The B-configuration field is run as a SENSITIVITY check, not as the ruling number.
"""
import sys, json, math, numpy as np
from t7c_hfsr import HFSR
from t7c_kernel import C0
from hfterm import ck

FLOOR = 5e-5   # 0.05 mHa, PREDICTION-CI2x2 CI-6 working floor, in Ha

# ---------------------------------------------------------------- radial
def R(h, a, b, c, d, kap):
    """R^kap(ab;cd) = int P_a P_c Y^kap(P_b,P_d)/r dr. a,b,c,d are (n,l) keys."""
    return float(np.sum(h.P[a] * h.P[c] * h.Yk(h.P[b], h.P[d], kap) / h.r * h.dr))

# ---------------------------------------------------------------- V
def Vdet(h, common, A, B, KMAX=8, radial=True):
    """common: list of (n,l,m,ms) spin-orbitals shared by both determinants.
    A,B: the one spin-orbital by which the determinants differ, each (n,l,m,ms).
    radial=False -> unit radial integrals (ANGULAR ONLY, for the can-fail)."""
    (na, la, ma, sa), (nb, lb, mb, sb) = A, B
    if sa != sb:
        return 0.0                       # spin-orthogonal: exactly zero
    V = 0.0
    for (nk, lk, mk, sk) in common:
        for kap in range(0, KMAX + 1):
            cD = ck(la, ma, lb, mb, kap) * ck(lk, mk, lk, mk, kap)
            if cD != 0.0:
                V += cD * (R(h, (na, la), (nk, lk), (nb, lb), (nk, lk), kap) if radial else 1.0)
            if sk == sa:
                cX = ck(la, ma, lk, mk, kap) * ck(lk, mk, lb, mb, kap)
                if cX != 0.0:
                    V -= cX * (R(h, (na, la), (nk, lk), (nk, lk), (nb, lb), kap) if radial else 1.0)
    return V

# ---------------------------------------------------------------- determinants
def spinorbs(occ):
    """Closed/partly-filled shells -> explicit spin-orbitals, max-S then max-L order."""
    so = []
    for (n, l, q) in occ:
        q = int(round(q)); ml = list(range(l, -l - 1, -1))
        up = min(q, 2 * l + 1); dn = q - up
        so += [(n, l, m, +1) for m in ml[:up]] + [(n, l, m, -1) for m in ml[:dn]]
    return so

def closed(occ):
    return [(n, l, q) for (n, l, q) in occ if int(round(q)) == 2 * (2 * l + 1)]

# ---------------------------------------------------------------- can-fail
def canfail(h):
    print("=== CAN-FAIL, BEFORE ANY SCORED ROW ===")
    # A. ANGULAR, BOTH DIRECTIONS. Unit radial integrals. One open d spectator.
    spec = [(3, 2, 1, +1)]
    allowed  = Vdet(h, spec, (3, 2, 0, -1), (4, 0, 0, -1), radial=False)   # l_a+l_b = 2 EVEN
    forbid   = Vdet(h, spec, (4, 1, 0, -1), (4, 0, 0, -1), radial=False)   # l_a+l_b = 1 ODD
    print(f"  A1 allowed  d->s , angular only : {allowed: .6f}   (must be NONZERO)")
    print(f"  A2 forbidden p->s , angular only : {forbid: .6f}   (must be ZERO)")
    assert abs(allowed) > 1e-9, "CAN-FAIL A1 FAILED: allowed case returned zero"
    assert abs(forbid) < 1e-12, "CAN-FAIL A2 FAILED: forbidden case returned nonzero"
    # B. SPIN ORTHOGONALITY
    assert Vdet(h, spec, (3, 2, 0, -1), (4, 0, 0, +1)) == 0.0, "CAN-FAIL B FAILED"
    print("  B  opposite-spin replacement     :  0.000000   (must be ZERO)")
    # C. CLOSED-SHELL CANCELLATION (spec 2iii), WITH THE REAL RADIAL INTEGRALS
    c3p = [so for so in spinorbs([(3, 1, 6)])]
    vc = Vdet(h, c3p, (3, 2, 0, -1), (4, 0, 0, -1))
    print(f"  C  closed 3p6 spectator, radial  : {vc: .3e} Ha  (must be ZERO)")
    assert abs(vc) < 1e-10, f"CAN-FAIL C FAILED: closed shell contributed {vc}"
    # D. LEVER (F54.2 law): the spectator occupation MUST move V.
    v1 = Vdet(h, [(3, 2, 1, +1)], (3, 2, 0, -1), (4, 0, 0, -1))
    v2 = Vdet(h, [(3, 2, 1, +1), (3, 2, 2, +1)], (3, 2, 0, -1), (4, 0, 0, -1))
    print(f"  D  lever  1 open d : {v1: .6e} Ha")
    print(f"     lever  2 open d : {v2: .6e} Ha   shift {abs(v2-v1):.3e}")
    assert abs(v2 - v1) > 1e-9, "CAN-FAIL D FAILED: lever dead, V does not move"
    print("CAN-FAIL: PASS -- all four, both directions demonstrated.\n")

# ---------------------------------------------------------------- rows
CORE = {24: [(1,0,2),(2,0,2),(2,1,6),(3,0,2),(3,1,6)],
        29: [(1,0,2),(2,0,2),(2,1,6),(3,0,2),(3,1,6)]}
# (occA, occB, commonVALENCE, A_extra, B_extra) -- from DERIVATION-CI6-SECTOR.md §2
ROWS = {
 24: dict(el='Cr',
          occA=[(3,2,5),(4,0,1)], occB=[(3,2,4),(4,0,2)],
          val=[(3,2,2,+1),(3,2,1,+1),(3,2,0,+1),(3,2,-1,+1),(4,0,0,+1)],
          Aex=(3,2,0,-1), Bex=(4,0,0,-1), ML=2, MS=2.0),
 29: dict(el='Cu',
          occA=[(3,2,10),(4,0,1)], occB=[(3,2,9),(4,0,2)],
          val=[(3,2,m,s) for m in (2,1,0,-1,-2) for s in (+1,-1) if not (m==0 and s==-1)]
              + [(4,0,0,+1)],
          Aex=(3,2,0,-1), Bex=(4,0,0,-1), ML=0, MS=0.5),
}

def mlms(so):
    return sum(m for (_,_,m,_) in so), sum(s for (_,_,_,s) in so)/2.0

def run(Z, field='A'):
    r = ROWS[Z]
    occ = CORE[Z] + (r['occA'] if field == 'A' else r['occB'])
    h = HFSR(Z, occ, c=C0); h.run('hf', qtail=1)
    common = spinorbs(CORE[Z]) + r['val']
    A = common + [r['Aex']]; B = common + [r['Bex']]
    mlA, msA = mlms(A); mlB, msB = mlms(B)
    assert (mlA, msA) == (mlB, msB) == (r['ML'], r['MS']), f"sector mismatch {mlA,msA} {mlB,msB}"
    V = Vdet(h, common, r['Aex'], r['Bex'])
    return h, dict(Z=Z, el=r['el'], field=field, ML=mlA, MS=msA, nA=len(A), nB=len(B),
                   V=V, absV=abs(V), mHa=abs(V)*1e3, clears=bool(abs(V) > FLOOR))

if __name__ == "__main__":
    Zs = [int(a) for a in sys.argv[1:]] or [24, 29]
    h0 = HFSR(24, CORE[24] + ROWS[24]['occA'], c=C0); h0.run('hf', qtail=1)
    canfail(h0)
    out = []
    for Z in Zs:
        for field in ('A', 'B'):
            _, o = run(Z, field)
            print(f"{o['el']:>3} Z={Z}  field={field}  (M_L,M_S)=({o['ML']},{o['MS']})  "
                  f"V = {o['V']: .6e} Ha = {o['mHa']:.4f} mHa   "
                  f"{'CLEARS' if o['clears'] else 'BELOW'} floor 0.05 mHa", flush=True)
            out.append(o)
    json.dump(out, open('ci2.json', 'w'), indent=1)
    print("\nwrote ci2.json")
