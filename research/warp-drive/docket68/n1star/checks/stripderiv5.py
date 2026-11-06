#!/usr/bin/env python3
"""stripderiv5.py -- BEYOND5 3(b) (D508): the derivatives at I_0 of the degree -3 regular solutions, against (1 + kappa)^(k/2).

The strip's term on {t = 0} is, harmonic by harmonic, r^-3 times the integral of sigma(v) F(1 - v rho) over the strip
(time-translation invariance, D491), F the regular degree -3 solution; its k-th rho-derivative involves F^(k) on [1 -
d rho, 1]. Uniform5's induction (U5), run from the s1 = 1 energy bound that uniform3_5 holds at degree -3, gives
|F^(k)| <= K_k (1 + kappa)^(k/2) |F(0)| on [1/2, 1] with K_k independent of l. Computed here (series at 30 digits, 400
terms, stripfull5's degree -3 reductions at the record's point): the norm of F(0) -> F^(k)(1) in uniform5's normalised
basis W, divided by (1 + kappa)^(k/2), k = 0 ... 4, scalar and vector types, l = 2, 4, 6, 8, 12, 16, 20.

Measured (D508): scalar type, k = 0 from 4.88 (l = 2) to 31.6 (l = 20), about 1.5 l; k = 1 about 3.0, flat; k = 2, 3, 4
falling with l (0.25, 0.026, 0.0059 at l = 20). Vector type: k = 0 about 1.6, flat; k >= 1 falling. All polynomial in l
and far below the induction's l-independent K_k (the k = 0 growth continues to 61.5 at l = 40, verifier 219, far below
K0_3 = e^(6e13)): a pre-asymptotic consistency check, at s = 1 only, which does not probe uniformity in l (x^2/2
dominates M0's lower terms only from x ~ 5e6 on the scalar type; D510). Labels: computed (a consistency check of the
deduction in BEYOND5 3(b), not a bound). About 2 minutes.

    python3 checks/stripderiv5.py
"""
import sys, time
sys.argv = ['x']
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import numpy as np
import sympy as sp
import mpmath as mp
import stripfull5 as SF
import harmonics5 as H
import coulombL5 as C

t0 = time.time()
es, _ = SF.reduce_scalar_p(3)
ev_, _ = SF.reduce_vector_p(3)
Ms, _ = H.matrices_n(es, H.FS)
Mv, _ = H.matrices_n(ev_, H.FV)
print('reduced %.0f s' % (time.time() - t0), flush=True)
KMAX = 4
for typ, Mx, par in (("scalar", Ms, H.kap), ("vector", Mv, H.lam)):
    for l in (2, 4, 6, 8, 12, 16, 20):
        n = 7 if typ == "scalar" else 3
        val = l*(l + 2) if typ == "scalar" else l*(l + 2) - 1
        Ml = [sp.Matrix(n, n, lambda i, j: Mx[o][i, j].subs(par, val)) for o in range(3)]
        T, last, Td = H.series_transfer_n(Ml, dict(C.POINT), 400, nder=KMAX)
        x = (l*(l + 2))**0.5
        W = np.diag([1, 1, 1, 1, x, x, x**2]) if typ == "scalar" else np.diag([1, 1, x])
        Wi = np.linalg.inv(W)
        row = []
        for k in range(KMAX + 1):
            A = np.array([[float(Td[k][i, j]) for j in range(n)] for i in range(n)])
            row.append(np.linalg.norm(W @ A @ Wi, 2)/(1 + x*x)**(k/2))
        print(typ, l, ' '.join('%.4g' % v for v in row), 'last %.1e' % float(last), flush=True)
print('%.0f s' % (time.time() - t0))
