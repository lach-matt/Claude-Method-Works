#!/usr/bin/env python3
"""blocks5.py -- CERTIFY-10L5-RESULT.md round 5, item 2: the block (Schur) route to a small constant, and why no
explicit high-mode estimate can meet its condition on rcert5's box.  Labels: deduced (exact, sympy rationals) for H1;
computed (floating point, on the record's coefficient table as linest5.py and wgron5.py read it) for H2.

Round 4 (8.3) left as the single missing input of task 2 an explicit estimate on the high angular modes whose constant
F_inf meets the block condition  ||A_N|| ||L_Ninf|| F_inf ||L_infN|| < 1,  A_N the low-mode inverse, L_Ninf = P_N L P_inf
and L_infN = P_inf L P_N the couplings across the cut, P_N the projection on Chebyshev degree <= N in x.  Here the norms
are fixed: Theorem 8.W's space-time structure (fluxes on the cones for the unknowns, the space-time L^2 integral for
the sources, the data's fluxes as data), with the section norm L^2(dx/sqrt(1 - x^2)), in which the Galerkin split is
orthogonal (the round-4 instance's norm).

  H1 (exact) the cut coupling of a multiplication by m = sum_{j <= d} m_j T_j does not depend on N >= d.  By
     T_j T_k = (T_{j+k} + T_{|j-k|})/2, the T_i-coefficient of m T_k for i <= N < k is m_{k-i}/2 when k - i <= d and 0
     otherwise; all modes involved have index >= 1, whose norms are equal, so in the orthonormal basis P_N m P_inf is
     the d x d Toeplitz block H_m[a, b] = m_{b-a+d}/2 (zero where b - a + d is outside 1..d; a, b = 1..d), the same for
     every N >= d.  Its norm sigma(m) is therefore N-independent, and sigma(m) >= ||(m_1, ..., m_d)||/2 (the column
     of T_{N+1}).  Checked exactly: for random rational m of degree 6, the coupling matrices at N = 6, 9, 17 coincide
     after the index shift, and the T_{N+1} column is (m_d, ..., m_1)/2 in modes N+1-d .. N.  The same holds for
     P_inf m P_N (the transpose block).
     Control (k1, the code under test mutated): with T_j T_k = T_{j+k} (the |j - k| term dropped) the identity fails.
  H2 (computed) the record's couplings.  For each of the largest coefficient fields of linest5.py's table (coordinate
     normalised, as wgron5.py's W4 takes them), sigma(u, v) of its degree-31 interpolant in x, at every second node of
     the box; then the space-time norm of the coupling restricted to that (row, unknown) pair, which bounds the block's
     norm from below:  ||L_Ninf||^2 >= sup_R (int int_R sigma^2 du dv) / |R_u|  for an 'in' unknown (fluxes in u on
     incoming cones; for 'out' unknowns u and v exchange), R over u- (v-) slabs of the box with the full other range.
     The inverse blocks have norm >= 1 (their data part is the identity on the initial cones' fluxes, deduced), so
     the block condition needs ||L_Ninf|| ||L_infN|| < 1; it fails for every N >= 31 if the computed product exceeds 1.
     Also printed: the coupling for N = 8, 16, 24 at the worst point (full product matrix, T_0 weighted).
     Two settings: the full angular range (where the (2+1) frame's coefficients grow toward the axes, 7.4), and the
     band |x| <= 1/2 on which Theorem 8.W's F^2 = 10^66.9 is computed, with the record's interpolant restricted to it
     and expanded in the band's own Chebyshev basis (so the split is the band's Galerkin split).
     Control (k2): the coefficient replaced by its x-mean has zero coupling (the cut decouples), as it must.

  python3 checks/blocks5.py RUN.npz      (RUN: the record's l1_rc0.9_M32.npz, as linest5.py and wgron5.py read it)
"""
import os, sys, time, importlib.util, random
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('linest5', os.path.join(HERE, 'linest5.py'))
L5 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L5)
print = L5.print


def cheb_mul(a, b, mutate=False):
    """exact product of Chebyshev series (lists of rationals)"""
    out = [sp.Integer(0)] * (len(a) + len(b) - 1)
    for j, aj in enumerate(a):
        for k, bk in enumerate(b):
            if aj == 0 or bk == 0:
                continue
            out[j + k] += (aj * bk if mutate else aj * bk / 2)
            if not mutate:
                out[abs(j - k)] += aj * bk / 2
    return out


def coupling(m, N, width, mutate=False):
    """matrix C[i, k] = T_i-coefficient of m T_k, i = N+1-width .. N, k = N+1 .. N+width"""
    C = sp.zeros(width, width)
    for kk in range(width):
        k = N + 1 + kk
        prod = cheb_mul(m, [0] * k + [1], mutate)
        for ii in range(width):
            i = N + 1 - width + ii
            C[ii, kk] = prod[i] if i < len(prod) else 0
    return C


def h1():
    rnd = random.Random(5)
    d = 6
    m = [sp.Rational(rnd.randint(-99, 99), rnd.randint(1, 37)) for _ in range(d + 1)]
    mats = [coupling(m, N, d) for N in (6, 9, 17)]
    same = all(M_ == mats[0] for M_ in mats[1:])
    col = mats[0][:, 0]
    want = sp.Matrix([m[d - ii] / 2 for ii in range(d)])     # rows N+1-d .. N  <->  j = d .. 1
    colok = col == want
    # nothing outside the d x d block: modes below N+1-d receive nothing from k > N
    big = coupling(m, 17, 2 * d)
    outside = all(big[ii, kk] == 0 for ii in range(d) for kk in range(2 * d))      # rows N+1-2d .. N-d
    tr = [coupling(m, N, d).T for N in (6, 9)]
    mut = [coupling(m, N, d, mutate=True) for N in (6, 9)]
    k1 = not (mut[0][:, 0] == want)
    return same, colok, outside, k1, m


def h2(path, band=None, cache={}):
    R = L5.rows()
    if path not in cache:
        cache[path] = L5.background(path)
    bg, inbox, uu, vv, x = cache[path]
    M0 = len(x)
    # on a band: the record's own degree-(M0 - 1) interpolant restricted to |x| <= band, re-expanded in the band's
    # Chebyshev basis (t = x/band) from its values at 2 M0 Chebyshev points of the band: exact for that polynomial
    tq = np.cos(np.pi * (np.arange(2 * M0) + 0.5) / (2 * M0))
    xq = tq * (band if band is not None else 1.0)
    syms = L5.STATE + [L5.Ew, L5.Ek] + list(L5.DX.values())
    args = [bg[s_] for s_ in syms]
    one = np.ones_like(bg[L5.Ew])
    fields = []
    for name, (op, bnd, rhs, fac) in R.items():
        fac_v = bg[L5.Ew] if fac == L5.Ew else 1.0
        for n in L5.UNK:
            co = rhs.coeff(L5.U[n])
            if co == 0 or n == bnd:
                continue
            cv = sp.lambdify(syms, co, 'numpy')(*args) * fac_v * one
            Cf = np.polynomial.chebyshev.chebfit(x, cv.reshape(-1, M0).T, M0 - 1)           # (M0, nu*nv)
            cv = np.polynomial.chebyshev.chebval(xq, Cf).reshape(cv.shape[0], cv.shape[1], len(xq))
            sup = float(np.nanmax(np.where(inbox[:, :, None], np.abs(cv), np.nan)))
            fields.append((sup, name, bnd, n, cv))
    fields.sort(key=lambda t: -t[0])
    M = M0
    out = []
    for sup, name, bnd, n, cv in fields[:6]:
        # Chebyshev coefficients of the degree-(M-1) interpolant at every (u, v)
        nq = len(tq)
        C = np.polynomial.chebyshev.chebfit(tq, cv.reshape(-1, nq).T, M - 1).T.reshape(cv.shape[0], cv.shape[1], M)
        d = M - 1
        sig = np.zeros(cv.shape[:2])
        for i in range(cv.shape[0]):
            for j in range(cv.shape[1]):
                if not inbox[i, j]:
                    continue
                c = C[i, j]
                H = np.zeros((d, d))
                for a in range(d):
                    for b_ in range(d):
                        q = b_ - a + d
                        if 1 <= q <= d:
                            H[a, b_] = c[q] / 2
                sig[i, j] = np.linalg.svd(H, compute_uv=False)[0]
        typ = L5.TYPE[n]
        best = slab_bound(sig, inbox, uu, vv, typ)
        iu, iv = np.unravel_index(np.argmax(np.where(inbox, sig, -1)), sig.shape)
        # direct couplings for small N at the worst point (orthonormal basis: T_0 row scaled by sqrt 2)
        c = C[iu, iv]
        small = {}
        for N in (8, 16, 24):
            A = np.zeros((N + 1, d))
            for kk in range(d):
                k = N + 1 + kk
                prod = np.polynomial.chebyshev.chebmul(c, np.eye(k + 1)[k])
                A[:, kk] = prod[:N + 1]
            A[0, :] *= np.sqrt(2.0)
            small[N] = np.linalg.svd(A, compute_uv=False)[0]
        # control k2: the x-mean has no coupling
        cm = np.zeros(M); cm[0] = c[0]
        Hm = np.zeros((d, d))
        for a in range(d):
            for b_ in range(d):
                q = b_ - a + d
                if 1 <= q <= d:
                    Hm[a, b_] = cm[q] / 2
        k2 = np.linalg.svd(Hm, compute_uv=False)[0]
        out.append(dict(deg=d, sup=sup, row=name, bnd=bnd, unk=n, typ=typ, sigmax=float(sig[iu, iv]),
                        at=(uu[iu], vv[iv]), lower=float(np.sqrt(best)), small=small, k2=k2,
                        lb=float(np.linalg.norm(c[1:]) / 2), C=C))
    # every N below the degree, for the field with the largest space-time coupling: the full product matrix
    top = max(out, key=lambda r: r['lower'])
    d = M - 1
    lowN = {}
    for N in range(0, d):
        sg = np.zeros(inbox.shape)
        for i in range(inbox.shape[0]):
            for j in range(inbox.shape[1]):
                if not inbox[i, j]:
                    continue
                A = np.zeros((N + 1, d + 1))
                for kk in range(d + 1):
                    prod = np.polynomial.chebyshev.chebmul(top['C'][i, j], np.eye(N + 2 + kk)[N + 1 + kk])
                    A[:, kk] = prod[:N + 1]
                A[0, :] *= np.sqrt(2.0)
                sg[i, j] = np.linalg.svd(A, compute_uv=False)[0]
        lowN[N] = float(np.sqrt(slab_bound(sg, inbox, uu, vv, top['typ'])))
    return out, top, lowN


def slab_bound(sig, inbox, uu, vv, typ):
    """sup over slabs R of int int_R sigma^2 / |R| in the unknown's flux variable (u for 'in', v for 'out')"""
    s2 = np.where(inbox, sig ** 2, 0.0)
    best = 0.0
    if typ in ('in', 'both'):           # the unknown's norm: sup_v int du; slabs in u, full v
        for a in range(len(uu)):
            for b_ in range(a + 1, len(uu)):
                num = np.trapezoid(np.trapezoid(s2[a:b_ + 1], vv, axis=1), uu[a:b_ + 1])
                best = max(best, num / (uu[b_] - uu[a]))
    if typ in ('out', 'both'):
        for a in range(len(vv)):
            for b_ in range(a + 1, len(vv)):
                num = np.trapezoid(np.trapezoid(s2[:, a:b_ + 1], uu, axis=0), vv[a:b_ + 1])
                best = max(best, num / (vv[b_] - vv[a]))
    return best


def main():
    t0 = time.time(); ok = True
    same, colok, outside, k1, m = h1()
    g1 = same and colok and outside
    print('H1 (exact) random rational m of degree 6: the coupling blocks at N = 6, 9, 17 coincide after the shift: %s; '
          'the T_{N+1} column is (m_6, ..., m_1)/2: %s; nothing outside the 6 x 6 block: %s -> %s'
          % (same, colok, outside, 'PASS' if g1 else 'FAIL'))
    print('   so sigma(m) = ||P_N m P_inf|| is the same for every N >= deg m, and >= ||(m_1..m_d)||/2')
    print('   control (k1) product rule T_j T_k = T_{j+k}: the column identity %s' % (
        'fails (good)' if k1 else 'still holds (bad)'))
    ok &= g1 and k1
    if len(sys.argv) < 2:
        print('blocks5 (no run given; H2 skipped): %s' % ('all checks pass' if ok else 'FAILURES'))
        return 0 if ok else 1
    for band in (None, 0.5):
        ok &= report(h2(sys.argv[1], band), band, t0)
    print('blocks5 (%.0f s): %s' % (time.time() - t0, 'all checks pass' if ok else 'FAILURES'))
    return 0 if ok else 1


def report(rr, band, t0):
    res, top, lowN = rr
    ok = True
    d = ('the full angular range (the record\'s degree-31 interpolant in x)' if band is None else
         '|x| <= %.1f (the record\'s interpolant restricted, in the band\'s own Chebyshev basis)' % band)
    print('H2 (computed) on %s: the six largest off-diagonal coefficient fields of the linearised table on rcert5\'s '
          'box (%.0f s):' % (d, time.time() - t0))
    for r in res:
        print('   %s row (bounds %s) <- %s [%s]: sup|m| %.3g; sigma at N >= d = %d up to %.3g (u %.2f, v %.2f), its '
              'lower bound ||m_{1..d}||/2 there %.3g; for N = 8, 16, 24 at that point %s; space-time coupling '
              '>= %.3g; control k2 (x-mean) %.1e' % (
                  r['row'], r['bnd'], r['unk'], r['typ'], r['sup'], r['deg'], r['sigmax'], r['at'][0], r['at'][1],
                  r['lb'],
                  ', '.join('%.3g' % r['small'][N] for N in (8, 16, 24)), r['lower'], r['k2']))
        ok &= r['k2'] == 0.0 and r['sigmax'] >= r['lb'] * (1 - 1e-12)
    dg = top['deg']
    lowest = min([top['lower']] + list(lowN.values()))
    prod = lowest ** 2
    print('H2 the largest space-time coupling (%s row <- %s): >= %.3g for every N >= %d (N-independent, H1), and for '
          'N = 0..%d at least %.3g (N = %d smallest); the transpose block has the same norms.  With ||A_N||, F_inf >= 1 '
          '(deduced) the block product is >= %.3g for EVERY N -> the block condition %s' % (
              top['row'], top['unk'], top['lower'], dg, dg - 1, min(lowN.values()), min(lowN, key=lowN.get), prod,
              'FAILS for every N' if prod > 1 else 'is not excluded'))
    ok &= prod > 1
    return ok


if __name__ == '__main__':
    sys.exit(main())
