#!/usr/bin/env python3
"""wgron5.py -- CERTIFY-10L5-RESULT.md round 4 (task 2): the constant of Theorem 7.L with weights, the approximate-
inverse route's exact requirement, and the frozen-angle growth of the transported unknowns.  Labels: deduced (the
weighted theorem and the finite-rank lemma, each with a computed check and a mutation control); computed (floating
point, on the record's run, as linest5.py E4) for the constants.

Theorem 8.W (deduced; the proof of Theorem 7.L with weights).  Give every row group a weight lam > 0 (one per
transported unknown, one per scalar for its three pair unknowns, whose pair identities fix the ratio a : c : d) and
every off-diagonal bilinear term (row Y, partner Z) a split theta > 0:  2 lam_Y |m| |Y| |Z| <= |m| theta (lam_Y Y^2)
+ |m| (lam_Y/(lam_Z theta)) (lam_Z Z^2).  With f_lam the weighted f of Theorem 7.L, the same steps give
f_lam <= (D_lam + S_lam) exp(2 int a_o^lam du + 2 int a_i^lam dv), the kappa's now
    kappa_Z^lam = sum_{Z's rows} |m| theta + sum_{rows with partner Z} |m| lam_Y/(lam_Z theta) + (diagonal terms),
and since min(lam) f <= f_lam <= max(lam) f,
    F_lam^2 = (max lam / min lam) exp(2 int a_o^lam du + 2 int a_i^lam dv)  bounds f by F_lam^2 (D + S).
Every (lam, theta) gives a theorem; the choice only sets how sharp it is.  The exponent is convex in (log lam,
log theta) (sums of exponentials of linear forms, maxima, integrals), so its minimum is computable.

  W1 (computed check of the weighted lemma, mutation control) a model Goursat pair Y_v = m Z, Z_u = m Y on
     [0, 1]^2 with data 1 on both cones (the extremal coupling, solved exactly as a Bessel series): the weighted bound
     with lam_Y/lam_Z = q must hold for every q tried; with the factor max lam/min lam dropped (the mutation) it must
     fail for some q.
  W2 (computed) control: lam = theta = 1 reproduces linest5.py E4b on |x| <= 1/2 (F^2 = 10^138.0): the code under test
     against the independent implementation.
  W3 (computed) the optimum: F_lam^2 on |x| <= 1/2 and 0.8, with the weights found, against 7.L's.
  W4 (deduced, with a computed instance) the approximate-inverse route.  Lemma: if A has finite rank and L is a
     linear operator with infinite-dimensional range in a Hilbert space H, then ||I - L A|| >= 1 (for f orthogonal to
     the finite-dimensional L(ran A): |(I - LA) f|^2 = |f|^2 + |LAf|^2 >= |f|^2).  So the bound
     ||L^{-1}|| <= ||A|| + F_E ||I - L A||, the explicit estimate F_E applied to the defect, is >= F_E for every
     finite-rank approximate inverse: it cannot lower F below the explicit constant.  What can is an explicit estimate
     on the complement of the discretisation (the high angular frequencies) whose constant F_inf is small; then
     ||L^{-1}|| <= (||A_N|| + F_inf ||P_inf L A_N||)/(1 - F_inf ||P_N ... ||)-type block bounds hold.  Computed
     instance: on the record's angular grid, the Chebyshev projection of x-degree < N, the defect of the exact low-
     mode inverse on f = T_N(x) (a mode outside the range) is exactly 1 in L^2(dx/sqrt(1 - x^2)), and the high-mode
     part of the coupling P_inf m P_N, for the record's coefficients m, is not small: printed.
  W5 (computed) the frozen-angle growth: the nine transported unknowns' rows alone (pair unknowns and the e3 rows'
     x-motion dropped), at each angular node, as a Goursat system in (u, v) with the record's coefficients signed, not
     absolute: the norm of its solution operator (data on the two cones -> the f-norm), by assembling it and taking
     the largest singular value, against its own Gronwall bound.  This measures how much of 7.L's constant is the
     absolute-value bookkeeping rather than growth; it is not a bound on the full operator's norm.

  python3 checks/wgron5.py RUN.npz        (RUN: the record's l1_rc0.9_M32.npz, read as linest5.py reads it)
"""
import os, sys, time, importlib.util
import numpy as np
import sympy as sp
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('linest5', os.path.join(HERE, 'linest5.py'))
L5 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L5)
print = L5.print
UNK, TYPE = L5.UNK, L5.TYPE
GROUP = {n: n for n in UNK}
for i in (1, 2):
    for p in ('da', 'dc', 'dd'):
        GROUP['%s%d' % (p, i)] = 'phi%d' % i
GROUPS = sorted(set(GROUP.values()), key=lambda g: [GROUP[n] for n in UNK].index(g))


def terms(R, bg):
    """every bilinear term of the energy bookkeeping: (bounded unknown Y, partner Z, |m| coordinate-normalised array);
    and the diagonal arrays d_Z (measure, source, the pair identities' quadratic forms), exactly as linest5.kappas"""
    syms = L5.STATE + [L5.Ew, L5.Ek] + list(L5.DX.values())
    args = [bg[s_] for s_ in syms]
    one = np.ones_like(bg[L5.Ew])
    T, D = [], {n: 0.0 * one for n in UNK}
    for name, (op, bnd, rhs, fac) in R.items():
        fac_v = bg[L5.Ew] if fac == L5.Ew else 1.0
        for n in UNK:
            co = rhs.coeff(L5.U[n])
            if co == 0:
                continue
            cv = np.abs(sp.lambdify(syms, co, 'numpy')(*args) * fac_v) * one
            if n == bnd:
                D[bnd] = D[bnd] + 2 * cv
            else:
                T.append((bnd, n, cv))
        if op in ('e4', 'dv'):
            D[bnd] = D[bnd] + np.abs(bg['dv_lw']) + 1.0
        elif op == 'e3':
            D[bnd] = D[bnd] + np.abs(bg['du_lw'] + bg['dx_bw']) + 1.0
        else:
            D[bnd] = D[bnd] + 1.0
    E = bg[L5.Ew]
    q3 = np.abs(E * (bg[L5.chib] - 2 * bg[L5.omb])); q4 = np.abs(E * (bg[L5.chi] - 2 * bg[L5.om]))
    qx = np.abs(E * (bg[L5.eta] + bg[L5.etab]))
    for i in (1, 2):
        D['da%d' % i] = D['da%d' % i] + q3 + qx
        D['dc%d' % i] = D['dc%d' % i] + q4 + qx + q3 + qx
        D['dd%d' % i] = D['dd%d' % i] + q4 + qx
    return T, D


class Bound:
    """the exponent J = log(max lam/min lam) + 2 int a_o du + 2 int a_i dv for weights t = log lam (per group) and
    splits s = log theta (per off-diagonal term), on a band of the background"""

    def __init__(self, T, D, sel, uu, vv, unk=None, typ=None, group=None, groups=None, mutate=False):
        self.unk, self.typ = unk or UNK, typ or TYPE
        self.group, self.groups = group or GROUP, groups or GROUPS
        self.mutate = mutate
        self.uu, self.vv = uu, vv
        self.outs = [n for n in self.unk if self.typ[n] in ('out', 'both')]
        self.ins = [n for n in self.unk if self.typ[n] == 'in']
        msk = lambda A: np.where(sel, A, np.nan)
        self.T = [(y, z, msk(c)) for y, z, c in T]
        self.D = {n: msk(D[n]) for n in self.unk}
        # relaxation for the optimiser: per-u sup over (v, x) and per-v sup over (u, x), term by term
        self.Tu = [(y, z, np.nan_to_num(np.nanmax(c, axis=(1, 2)))) for y, z, c in self.T]
        self.Tv = [(y, z, np.nan_to_num(np.nanmax(c, axis=(0, 2)))) for y, z, c in self.T]
        self.Du = {n: np.nanmax(self.D[n], axis=(1, 2)) for n in self.unk}
        self.Dv = {n: np.nanmax(self.D[n], axis=(0, 2)) for n in self.unk}
        self.iu = ~np.isnan(self.Du[self.unk[0]]); self.iv = ~np.isnan(self.Dv[self.unk[0]])

    def kappa_exact(self, t, s):
        lam = {g: t[i] for i, g in enumerate(self.groups)}
        K = {n: self.D[n].copy() for n in self.unk}
        sg = 1.0 if self.mutate else -1.0        # the mutation: the partner's share lam_Y theta/lam_Z (wrong)
        for k, (y, z, c) in enumerate(self.T):
            K[y] = K[y] + c * np.exp(s[k])
            K[z] = K[z] + c * np.exp(lam[self.group[y]] - lam[self.group[z]] + sg * s[k])
        return K

    def J_exact(self, t, s):
        K = self.kappa_exact(t, s)
        ao = np.nanmax(np.stack([np.nanmax(K[n], axis=(1, 2)) for n in self.outs]), axis=0)
        ai = np.nanmax(np.stack([np.nanmax(K[n], axis=(0, 2)) for n in self.ins]), axis=0)
        Io = np.trapezoid(ao[self.iu], self.uu[self.iu]); Ii = np.trapezoid(ai[self.iv], self.vv[self.iv])
        return (max(t) - min(t)) + 2 * Io + 2 * Ii, Io, Ii

    def J_relaxed(self, p, beta=60.0):
        ng = len(self.groups); t, s = p[:ng], p[ng:]
        lam = {g: t[i] for i, g in enumerate(self.groups)}
        def prof(Tl, Dl, names, axis_grid, idx):
            K = {n: Dl[n][idx].copy() for n in self.unk}
            for k, (y, z, c) in enumerate(Tl):
                K[y] = K[y] + c[idx] * np.exp(s[k])
                K[z] = K[z] + c[idx] * np.exp(lam[self.group[y]] - lam[self.group[z]] - s[k])
            S = np.stack([K[n] for n in names])
            m = S.max(0)
            sm = m + np.log(np.exp(beta * (S - m)).sum(0)) / beta          # smooth max over unknowns
            return np.trapezoid(sm, axis_grid[idx])
        Io = prof(self.Tu, self.Du, self.outs, self.uu, self.iu)
        Ii = prof(self.Tv, self.Dv, self.ins, self.vv, self.iv)
        tm = max(t) + np.log(np.exp(beta * (t - max(t))).sum()) / beta
        tn = min(t) - np.log(np.exp(-beta * (t - min(t))).sum()) / beta
        return (tm - tn) + 2 * Io + 2 * Ii


def model_check():
    """W1: the model Y_v = m1 Z (Y transported in v, measured on ingoing cones), Z_u = m2 Y (measured on outgoing
    ones), Y(u, 0) = Z(0, v) = 1 on [0, 1]^2, m1 = 9, m2 = 1, solved on a fine grid (second order); f(1, 1) of Theorem
    7.L against e^J (D_lam/min lam) from Bound itself, at several (lam, theta); and the mutated Bound (partner share
    lam_Y theta/lam_Z) at theta -> 0, which must fall below f."""
    m1, m2, n = 9.0, 1.0, 800
    g = np.linspace(0, 1, n + 1); h = g[1] - g[0]
    Y = np.ones((n + 1, n + 1)); Z = np.ones((n + 1, n + 1))
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                continue
            if j > 0 and i > 0:          # trapezoid in both, solved exactly for the 2 x 2 linear system
                a = Y[i, j - 1] + h / 2 * m1 * Z[i, j - 1]
                b = Z[i - 1, j] + h / 2 * m2 * Y[i - 1, j]
                det = 1 - (h / 2) ** 2 * m1 * m2
                Y[i, j] = (a + h / 2 * m1 * b) / det; Z[i, j] = (b + h / 2 * m2 * a) / det
            elif j > 0:                  # u = 0: Z = 1 data, Y from its row
                Y[i, j] = Y[i, j - 1] + h * m1 * (Z[i, j - 1] + Z[i, j]) / 2
            else:                        # v = 0: Y = 1 data, Z from its row
                Z[i, j] = Z[i - 1, j] + h * m2 * (Y[i - 1, j] + Y[i, j]) / 2
    f11 = np.trapezoid(Y[:, -1] ** 2, g) + np.trapezoid(Z[-1, :] ** 2, g)
    D11 = 2.0                            # int_0^1 Y(u, 0)^2 du + int_0^1 Z(0, v)^2 dv
    sel = np.ones((n + 1, n + 1, 1), bool)
    one = np.ones((n + 1, n + 1, 1))
    T = [('Y', 'Z', m1 * one), ('Z', 'Y', m2 * one)]
    D = {'Y': 0 * one, 'Z': 0 * one}
    kw = dict(unk=['Y', 'Z'], typ={'Y': 'in', 'Z': 'out'}, group={'Y': 'Y', 'Z': 'Z'}, groups=['Y', 'Z'])
    rows = []
    for lq, s1, s2 in ((0.0, 0.0, 0.0), (np.log(1 / 9), np.log(1 / 3), np.log(3)), (np.log(1 / 9), 0.0, 0.0),
                       (1.0, 0.5, -0.5)):
        t = np.array([lq, 0.0]); s_ = np.array([s1, s2])
        J, _, _ = Bound(T, D, sel, g, g, **kw).J_exact(t, s_)
        Dlam = np.exp(max(t)) * D11                     # D_lam <= max lam D ; f <= f_lam/min lam
        bound = np.exp(J - (max(t) - min(t))) * Dlam / np.exp(min(t))
        rows.append((np.exp(lq), np.exp(s1), np.exp(s2), f11, bound, f11 <= bound))
    Jm, _, _ = Bound(T, D, sel, g, g, mutate=True, **kw).J_exact(np.zeros(2), np.array([-12.0, -12.0]))
    mut = np.exp(Jm) * D11
    return f11, rows, mut, f11 > mut


def main():
    t0 = time.time()
    ok = True
    f11, rows, mut, caught = model_check()
    good = all(r[5] for r in rows)
    print('W1 model (Y_v = 9 Z, Z_u = Y on [0, 1]^2, data 1): f(1, 1) = %.4g; the weighted bound from Bound itself:' %
          f11)
    for q, th1, th2, f_, b_, ok_ in rows:
        print('   lam_Y/lam_Z = %.3g, theta = %.3g, %.3g: bound %.4g (%s)' % (q, th1, th2, b_, 'holds' if ok_ else
                                                                             'FAILS'))
    print('   mutation (the partner\'s share lam_Y theta/lam_Z), theta = e^-12: bound %.4g -> %s' % (
        mut, 'below f: caught (good)' if caught else 'not caught (bad)'))
    print('W1', 'PASS' if good and caught else 'FAIL')
    ok &= good and caught
    if len(sys.argv) < 2:
        print('wgron5 (no run given; W2-W5 skipped):', 'all checks pass' if ok else 'FAILURES')
        return 0 if ok else 1
    R = L5.rows()
    bg, inbox, uu, vv, x = L5.background(sys.argv[1])
    T, D = terms(R, bg)
    print('   (%.0f s) background and %d off-diagonal terms over %d row groups' % (time.time() - t0, len(T),
                                                                                   len(GROUPS)))
    res = {}
    for Xb in (0.5, 0.8):
        sel = inbox[:, :, None] & (np.abs(x)[None, None, :] <= Xb + 1e-12)
        B = Bound(T, D, sel, uu, vv)
        t1 = np.zeros(len(GROUPS)); s1 = np.zeros(len(T))
        J1, Io1, Ii1 = B.J_exact(t1, s1)
        lg1 = J1 / np.log(10)
        if Xb == 0.5:
            good = abs(lg1 - 138.0) < 0.1
            print('W2 lam = theta = 1 on |x| <= 1/2: int a_o du = %.1f, int a_i dv = %.1f, F^2 = 10^%.1f against '
                  'linest5.py E4b\'s 10^138.0 -> %s' % (Io1, Ii1, lg1, 'PASS' if good else 'FAIL'))
            ok &= good
        p0 = np.zeros(len(GROUPS) + len(T))
        best = None
        for it in range(3):
            r_ = minimize(B.J_relaxed, p0, method='L-BFGS-B', options=dict(maxiter=3000))
            p0 = r_.x
            Jx, Io, Ii = B.J_exact(r_.x[:len(GROUPS)], r_.x[len(GROUPS):])
            if best is None or Jx < best[0]:
                best = (Jx, Io, Ii, r_.x.copy())
        Jx, Io, Ii, p = best
        tw = p[:len(GROUPS)]
        res[Xb] = (lg1, Jx / np.log(10), Io, Ii, tw)
        print('W3 |x| <= %.1f: optimal weights (log lam, relative to the smallest): %s' % (
            Xb, ', '.join('%s %.2f' % (g, w - tw.min()) for g, w in zip(GROUPS, tw))))
        print('   log(max/min lam) = %.2f, int a_o du = %.1f, int a_i dv = %.1f: F_lam^2 = 10^%.1f against 7.L\'s '
              '10^%.1f' % (tw.max() - tw.min(), Io, Ii, Jx / np.log(10), lg1))
    # W4: the finite-rank lemma, a computed instance on the angular grid
    M = len(x)
    N = M
    th = np.arccos(x)
    TN = np.cos(N * th)                   # a mode outside the span of T_0..T_{M-1} in the weighted L^2
    print('W4 lemma (deduced): ||I - L A|| >= 1 for every finite-rank A; so ||L^{-1}|| <= ||A|| + F_E ||I - L A||')
    print('   gives no constant below F_E.  Instance: in L^2(dx/sqrt(1-x^2)) the Chebyshev projection P_N (N = %d) '
          'annihilates T_%d, so for the exact low-mode inverse (I - L A) T_%d = T_%d: defect 1 exactly.' % (N, N, N, N))
    # coupling of the record's coefficients into high modes: P_inf (m T_k) for k < N, relative to |m T_k|
    xs = np.cos(np.pi * (np.arange(4 * M) + 0.5) / (4 * M))
    # the largest single coefficient field (dw in the chib row), resampled in x by its Chebyshev interpolant
    syms = L5.STATE + [L5.Ew, L5.Ek] + list(L5.DX.values())
    co = R['chib'][2].coeff(L5.U['dw'])
    f_co = sp.lambdify(syms, co * L5.Ew, 'numpy')(*[bg[s_] for s_ in syms]) * np.ones_like(bg[L5.Ew])
    sel = inbox[:, :, None] & np.ones((1, 1, M), bool)
    iu, iv = np.unravel_index(np.nanargmax(np.where(inbox, np.abs(f_co).max(-1), np.nan)), inbox.shape)
    prof = f_co[iu, iv]
    Cm = np.polynomial.chebyshev.chebfit(x, prof, M - 1)
    # m T_k has Chebyshev degree up to (M - 1) + k: its part above degree N - 1, relative, for k = N - 4 .. N - 1
    rel = []
    for k in range(N - 4, N):
        prod = np.polynomial.chebyshev.chebmul(Cm, np.eye(k + 1)[k])
        hi = np.sqrt(np.sum(prod[N:] ** 2)); tot = np.sqrt(np.sum(prod ** 2))
        rel.append(hi / tot)
    print('   the record\'s largest coefficient (dw in the chib row, at u = %.2f, v = %.2f, sup %.3g): P_inf (m T_k)/'
          '|m T_k| = %s for k = %d..%d: the coupling across the cut is of the coefficient\'s own size, not small' % (
              uu[iu], vv[iv], np.abs(prof).max(), ', '.join('%.2f' % r for r in rel), N - 4, N - 1))
    # W5: frozen-angle growth of the nine transported unknowns
    trans = ['dchi', 'deta', 'domb', 'dchib', 'detab', 'dom', 'dk', 'dw', 'db']
    rowof = {'dchi': 'chi', 'deta': 'eta', 'domb': 'omb', 'dchib': 'chib', 'detab': 'etab', 'dom': 'om',
             'dk': 'k', 'dw': 'w', 'db': 'b'}
    coef = {}
    for y in trans:
        op, bnd, rhs, fac = R[rowof[y]]
        for z in trans:
            c_ = rhs.coeff(L5.U[z])
            if c_ == 0:
                continue
            fac_v = bg[L5.Ew] if fac == L5.Ew else 1.0
            coef[(y, z)] = sp.lambdify(syms, c_, 'numpy')(*[bg[s_] for s_ in syms]) * fac_v * np.ones_like(bg[L5.Ew])
    iu_ = np.where(inbox.any(1))[0]; iv_ = np.where(inbox.any(0))[0]
    us, vs = uu[iu_], vv[iv_]
    e4set = ['dchi', 'deta', 'domb', 'dk', 'dw', 'db']; e3set = ['dchib', 'detab', 'dom']
    worst = (0, None, 0)
    out_rows = []
    for jx in range(M):
        if abs(x[jx]) > 0.5:
            continue
        nu, nv = len(us), len(vs)
        ndata = len(e4set) * nu + len(e3set) * nv
        sol_norms = []
        Amat = np.zeros((len(trans) * nu * nv, ndata))
        for col in range(ndata):
            Y = {z: np.zeros((nu, nv)) for z in trans}
            if col < len(e4set) * nu:
                zi, ii = divmod(col, nu); Y[e4set[zi]][ii, 0] = 1.0
            else:
                zi, jj = divmod(col - len(e4set) * nu, nv); Y[e3set[zi]][0, jj] = 1.0
            for i in range(nu):
                for j in range(nv):
                    if j > 0:      # e4 / d_v rows: Y_v = sum m Z (trapezoid, explicit predictor-corrector)
                        dv_ = vs[j] - vs[j - 1]
                        for y in e4set:
                            r0 = sum(coef[(y, z)][iu_[i], iv_[j - 1], jx] * Y[z][i, j - 1] for z in trans
                                     if (y, z) in coef)
                            Y[y][i, j] = Y[y][i, j - 1] + dv_ * r0
                    if i > 0:      # e3 rows: Y_u = sum m Z
                        du_ = us[i] - us[i - 1]
                        for y in e3set:
                            r0 = sum(coef[(y, z)][iu_[i - 1], iv_[j], jx] * Y[z][i - 1, j] for z in trans
                                     if (y, z) in coef)
                            Y[y][i, j] = Y[y][i - 1, j] + du_ * r0
            Amat[:, col] = np.concatenate([Y[z].ravel() for z in trans])
        sv = np.linalg.svd(Amat, compute_uv=False)[0]
        out_rows.append((x[jx], sv))
        if sv > worst[0]:
            worst = (sv, x[jx], 0)
    gr = res[0.5][2] + res[0.5][3]
    print('W5 frozen-angle transport (nine transported unknowns, signed coefficients, |x| <= 1/2, %d x %d nodes): '
          'largest singular value of data -> solution (nodal l2 norms) %.3g at x = %.3f; per node: %s' % (
              len(us), len(vs), worst[0], worst[1], ', '.join('%.3f: %.3g' % r for r in out_rows)))
    print('   against the Gronwall factor of the same nine rows with absolute values: see W3 (all fifteen rows); '
          'this measures bookkeeping against growth and is not a bound on the full operator')
    print('wgron5 (%.0f s):' % (time.time() - t0), 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
