"""e2h1_5.py -- E2-PILOT section 3i (D404): Corollary E2.11, one derivative and the angular derivative, uniformly in l.

From Lemma E2.8's identity (3.4) with Lemma E2.9's split w_l = w_1 + (a - a_1) psi, psi := -phi_* U' >= 0 (zero at the
photon sphere r = sqrt 2, to second order), and w_1 >= 0 on R (certified, e2certify5 C1-C2): for real sigma != 0 and
u = R_l(sigma) f with f in L^2(I), X := ||u'||_I, Y := ||u||_I, Z := int_I psi |u|^2,

    2 m' X^2 + (a - a_1) Z <= ||f|| (2X + (M' + 2|sigma|) Y),     Y <= B_l(sigma) ||f||,

so X <= Xb ||f||, Xb := (1 + (1 + 2 m' (M' + 2|sigma|) B_l)^(1/2)) / (2 m'), and (a - a_1) Z <= K ||f||^2 with
K := 2 Xb + (M' + 2|sigma|) B_l. For Im sigma > 0 the same holds with 4|sigma| for 2|sigma| (Lemma E2.10).

  H1 (exact) the constants at sigma = 3 for every l >= 6 from the certified m' >= 0.005793, M' <= 1.02041 and
     min_I w_6 >= 1.0610 (e2certify5 C3), with exact rationals, every square root rounded up: B_6(3), Xb, K and
     a K/(a - a_1) at l = 6 (the largest over l >= 6, as a/(a - a_1) decreases), pinned to their decimals (D405).
  H3 (exact) every l at sigma = 3, from section 3f's certified B_l(3) (l = 1: 264.5, peak multiplier C5; l = 2-5:
     51.12, 34.39, 26.02, 20.99; l >= 6: B_6): X_l, the angular bound A_l (l(l+2) K_l/(a - a_1) for l >= 2, and
     3 B_1^2 at l = 1, where a = a_1), and C_l^2 := X_l^2 + A_l, so that, summed over the orthogonal harmonics,
     ||d_r* u||_I^2 + sum_l l(l+2) int_I psi |u_l|^2 <= max_l C_l^2 ||f||^2 (the angular part unweighted at l = 1).
  H2 (computed) at l = 6, sigma = 3 + 0.25i, the operator norms f -> u' on I and f -> (a psi)^(1/2) u on I, from the
     finite-difference resolvent of e2cplx5.py, lie below the bounds with 4|sigma| (Lemma E2.10), and u' by a forward
     difference agrees with the central one to 5 % (an independent derivative, D405). Control: centred
     0.3 off the photon sphere, psi takes negative values, so Lemma E2.9's split w_l >= w_1, and with it the bound
     uniform in l, fails.
  H4 (exact, D416) l = 0. Lemma E2.8''s identity has 2 int (phi' - q)|u'|^2 on its left, phi' - q >= 0 on R and
     W_q >= 0 on R (e2lzero5 Z2), so the same algebra gives ||u'||_I <= X_0 ||f|| with section 3g's certified
     m0' >= 0.002580, M0' <= 0.3809 and B_0(3) <= 275.2 (Z4); there is no angular part at l = 0. X_0(3) and the constant
     over every l >= 0, max(C_l, X_0). Computed beside it: at sigma = 3 + 0.25i the norm of f -> u'|_I, against the
     bound with 4|sigma| (Lemma E2.10; Re sigma^2 > 0, so no q-term) and B_0^+.
Labels: H1, H3, H4 computed (exact, outward rounded); H2 and H4's comparison computed (floating point, not certified);
the corollary deduced.

    python3 checks/e2h1_5.py [--selftest]
"""
import math
import os
import sys
from fractions import Fraction as Fr
from math import isqrt

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e2cplx5 as E   # noqa: E402

S = Fr(49, 50)
M1 = Fr(5793, 10**6)     # m' >= (C3)
MM = Fr(102041, 10**5)   # M' <= 1/s (C3)
W6 = Fr(10610, 10**4)    # min_I w_6 >= (C3)
A1 = Fr(15, 4)           # a_1 = 1*3 + 3/4


def sqrt_up(q, digits=12):
    """an upper bound for sqrt(q), q >= 0 rational, at 10^-digits"""
    sc = 10**(2*digits)
    n = q.numerator*sc
    r = isqrt(n // q.denominator)
    while Fr(r*r, sc) < q:
        r += 1
    return Fr(r, 10**digits)


def up(x, nd):
    """x rounded up to nd decimals, as a string (exact: via Fraction)"""
    q = x if isinstance(x, Fr) else Fr(x)
    n = -((-q*10**nd).__floor__())
    s = str(n).rjust(nd + 1, "0")
    return s if nd == 0 else s[:-nd] + "." + s[-nd:]


def constants(sigma=3, l=6):
    a = l*(l + 2) + Fr(3, 4)
    c = MM + 2*sigma
    B = sqrt_up((2/M1 + c*c/W6)/W6)
    Xb = (1 + sqrt_up(1 + 2*M1*c*B))/(2*M1)
    K = 2*Xb + c*B
    return B, Xb, K, a*K/(a - A1)


def psi_of(xg, rg, shift=0.0):
    xs = math.sqrt(2) + 0.5*math.log((math.sqrt(2) - 1)/(math.sqrt(2) + 1)) + shift
    f = 1 - 1/rg**2
    y = 1/rg**2
    return -np.tanh((xg - xs)/float(S))*(2*f/rg**3)*(2*y - 1)


BL3 = {1: Fr(2645, 10), 2: Fr(5112, 100), 3: Fr(3439, 100), 4: Fr(2602, 100), 5: Fr(2099, 100)}
M0 = Fr(2580, 10**6)     # l = 0: min_I (phi' - q) >= (e2lzero5 Z4)
MM0 = Fr(3809, 10**4)    # max_I |phi' - 2q| <=
W0 = Fr(2886, 10**5)     # min_I W_q >=
B03 = Fr(2752, 10)       # B_0(3) <= (certified from the enclosures, Z4)


def lzero(sigma=3):
    """X_0 from Lemma E2.8''s identity: 2 m0' X^2 <= ||f|| (2X + (M0' + 2|sigma|) Y), Y <= B_0 ||f|| (D416)"""
    c = MM0 + 2*sigma
    return (1 + sqrt_up(1 + 2*M0*c*B03))/(2*M0)


def every_l(sigma=3):
    c = MM + 2*sigma
    rows = []
    for l in range(1, 7):
        B = BL3[l] if l in BL3 else constants(sigma, 6)[0]
        Xb = (1 + sqrt_up(1 + 2*M1*c*B))/(2*M1)
        K = 2*Xb + c*B
        a = l*(l + 2) + Fr(3, 4)
        A = 3*B*B if l == 1 else l*(l + 2)*K/(a - A1)
        rows.append((l, B, Xb, A, Xb*Xb + A))
    return rows


def h2(sigma=complex(3.0, 0.25), l=6, h=0.02, L=(-80.0, 120.0)):
    xg = np.arange(L[0], L[1] + h/2, h)
    V, rg = E.potential_on(xg, l)
    n = len(xg)
    A = sps.diags([np.full(n - 1, -1/h**2), 2/h**2 + V - sigma**2, np.full(n - 1, -1/h**2)], [-1, 0, 1],
                  format="csc").astype(complex)
    lu = spla.splu(A)
    I = np.where((rg >= 1.2) & (rg <= 4.0))[0]
    psi = psi_of(xg, rg)
    a = l*(l + 2) + 0.75
    Gd = np.empty((len(I), len(I)), complex)
    Gp = np.empty((len(I), len(I)), complex)
    Gf = np.empty((len(I), len(I)), complex)
    for k, i in enumerate(I):
        rhs = np.zeros(n, complex)
        rhs[i] = 1/h
        sol = lu.solve(rhs)
        du = (sol[I + 1] - sol[I - 1])/(2*h)
        Gd[:, k] = du*h
        Gf[:, k] = (sol[I + 1] - sol[I])/h*h       # a forward difference, an independent derivative (D405)
        Gp[:, k] = np.sqrt(a*np.maximum(psi[I], 0))*sol[I]*h
    nd, npsi, nf = (np.linalg.norm(G, 2) for G in (Gd, Gp, Gf))
    return nd, npsi, float(min(psi[I])), float(max(psi[I])), float(min(psi)), float(min(psi_of(xg, rg, 0.3))), nf


def main():
    ok = {}
    B, Xb, K, aK = constants()
    print("  H1: sigma = 3, l >= 6: B_6 <= %s, ||u'||_I <= %s ||f||, l(l+2) int_I psi|u|^2 <= %s ||f||^2"
          % (up(B, 4), up(Xb, 2), up(aK, 1)))
    ok["H1"] = abs(float(B) - 19.214) < 5e-4 and abs(float(Xb) - 224.49) < 5e-3 and abs(float(aK) - 632.5) < 0.05
    rows = every_l()
    for l, B, Xb, A, C2 in rows:
        print("  H3: l %s %d: B <= %s, ||u'||_I <= %s, angular <= %s, C_l^2 <= %s"
              % (">=" if l == 6 else "=", l, up(B, 2), up(Xb, 1), up(A, 0), up(C2, 0)))
    cmax = max(r[4] for r in rows)
    print("  H3: max_l C_l^2 <= %s (C <= %.1f), at l = %d" % (up(cmax, 0), float(sqrt_up(cmax)),
                                                             max(rows, key=lambda q: q[4])[0]))
    ok["H3"] = abs(float(cmax) - 455800) < 2000 and max(rows, key=lambda q: q[4])[0] == 1
    X0 = lzero()
    call = max(cmax, X0*X0)
    print("  H4: l = 0, sigma = 3: ||u'||_I <= %s ||f||; over every l >= 0, C <= %s, at l = %s"
          % (up(X0, 1), up(sqrt_up(call), 1), 0 if X0*X0 > cmax else 1))
    sg0 = complex(3.0, 0.25)
    c4 = float(MM0) + 4*abs(sg0)
    B0p = math.sqrt((2/float(M0) + c4*c4/float(W0))/float(W0))
    X0p = (1 + math.sqrt(1 + 2*float(M0)*c4*B0p))/(2*float(M0))
    nd0 = h2(sg0, l=0)[0]
    print("  H4: l = 0, sigma = 3 + 0.25i (Re sigma^2 > 0, no q-term): ||f -> u'|_I|| = %.4f <= %.1f" % (nd0, X0p))
    ok["H4"] = 800 < float(X0) < 820 and X0*X0 > cmax and nd0 <= X0p
    sg = complex(3.0, 0.25)
    c = float(MM) + 4*abs(sg)
    Bp = math.sqrt((2/float(M1) + c*c/float(W6))/float(W6))
    Xp = (1 + math.sqrt(1 + 2*float(M1)*c*Bp))/(2*float(M1))
    a6 = 6*8 + 0.75
    Kp = (2*Xp + c*Bp)*a6/(a6 - float(A1))
    nd, npsi, pmin, pmax, pall, pctl, nf = h2(sg)
    print("  H2: l = 6, sigma = 3 + 0.25i: ||f -> u'|_I|| = %.4f <= %.1f; ||f -> (a psi)^(1/2) u|_I|| = %.4f <= %.2f;"
          " psi on I in [%.2e, %.3f], min on the grid %.2e" % (nd, Xp, npsi, math.sqrt(Kp), pmin, pmax, pall))
    print("  H2 control: centred 0.3 off the photon sphere, min psi = %.3e < 0; u' by a forward difference: %.4f"
          " against %.4f (central)" % (pctl, nf, nd))
    ok["H2"] = nd <= Xp and npsi <= math.sqrt(Kp) and pall >= -1e-15 and abs(nf - nd) <= 0.05*nd
    ok["H2 control"] = pctl < 0
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
