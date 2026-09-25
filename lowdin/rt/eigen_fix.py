#!/usr/bin/env python3
"""eigen_fix.py -- Session 8 repair of the pack-5 bisection-floor fault (bridge-7 s1.3, DERIVE-P s4).

FAULT: step2_run.eigen brackets E in [-0.6*zeta^2, 0). At charge 1 (zeta=1) deep shells lie below -0.6 Ha
and the bisection returns the bracket edge, -0.6 exactly, silently. 24 of 106 step-3 E_B rows carry it;
Os 5d in the pairing class was SOLVED at the floor, so its u(r), F^k, J_H, P are at a wrong eigenvalue.

REPAIR (adaptive bracket, no new constant): start at the pack-5 floor; if the shoot at Elo says "E too
high" (the same test the bisection uses), Elo is not below the eigenvalue -> deepen x4, capped at the
rigorous bound -Z^2/2 (V(r) >= -Z/r for a screened potential, so no state lies below the bare 1s).
The floor is a BRACKET, and a bracket must contain the root; that is the whole repair.
When the pack-5 floor already brackets, Elo is untouched and the bisection is bit-identical to pack-5.
Deepening is on demand only, so Session 4 fault (ii) (spurious nodes at deep E for zeta >= 9) is not
re-exposed: those cases never asked to deepen.

Import this AFTER step2_run; it patches step2_run.eigen in place so step3/derive_P inherit it unchanged.
"""
import numpy as np, step2_run
_shoot = step2_run._shoot

def eigen(V, l, n, zeta, Z, npts=3000, tol=1e-9):
    rmin, rmax = 1e-5/Z, max(80.0, 4.0*n*n/zeta)
    x = np.linspace(np.log(rmin), np.log(rmax), npts); h = x[1]-x[0]; r = np.exp(x)
    base = (l+0.5)**2 + 2*r*r*V(r); target = n-l-1
    Elo, Ehi = -0.6*zeta*zeta, -1e-9
    cap = -0.5*Z*Z
    too_high = lambda E: (lambda y, nd: nd > target or (nd == target and y[-1]*(-1)**target < 0))(*_shoot(base - 2*r*r*E, h, l))
    deepened = 0
    while too_high(Elo) and Elo > cap:
        Elo = max(4*Elo, cap); deepened += 1
    for _ in range(200):
        E = 0.5*(Elo+Ehi); y, nd = _shoot(base - 2*r*r*E, h, l)
        if nd > target or (nd == target and y[-1]*(-1)**target < 0): Ehi = E
        else: Elo = E
        if Ehi - Elo < tol*abs(E) + 1e-13: break
    E = 0.5*(Elo+Ehi)
    eigen.last_deepened = deepened
    return E
eigen.last_deepened = 0

step2_run.eigen = eigen   # patch in place

if __name__ == "__main__":
    import tfd
    # 1) unchanged where the old floor bracketed: H 1s must still be -0.5, deepened 0
    V, x0 = tfd.potential(1, 1)
    print("H  1s :", round(eigen(V, 0, 1, 1.0, 1), 6), "deepened", eigen.last_deepened)
    # 2) the flagged case: Os 5d at charge 1 (pack-5 gave -0.6 exactly)
    V, x0 = tfd.potential(76, 1)
    print("Os 5d :", round(eigen(V, 2, 5, 1.0, 76), 5), "deepened", eigen.last_deepened)
    print("Os 6p :", round(eigen(V, 1, 6, 1.0, 76), 5), "deepened", eigen.last_deepened)
    print("Os 6s :", round(eigen(V, 0, 6, 1.0, 76), 5), "deepened", eigen.last_deepened)
