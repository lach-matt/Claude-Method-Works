#!/usr/bin/env python3
"""linest5.py -- CERTIFY-10L5-RESULT.md round 3, F5: the linear estimate of Theorem 7.L at the curvature level, in the
reduced (2+1) variables, with an explicit constant; its value on the record's computed solution; and the demand it puts
on the residual.  Labels: deduced (exact, sympy) for E1-E3 and the coefficient table; computed (floating point, on the
record's run) for E4-E6; deduced and computed for the lemma check E7.

The reduced system (reduce5.py R2-R4), in the Einstein frame of the class, double-null gauge, one-dimensional sections
(null3.py): unknowns the Ricci coefficients psi = (chi, eta, omegab | chib, etab, omega), the metric (k = log sqrt gt,
w = log Omt, b), and the frame derivatives of the two scalars (a_i, c_i, d_i) = (e4, ex, e3) Phi_i.  The hierarchy:
    e4 chi = -chi^2 - 2 omega chi - sum a_i^2,      e3 chib = -chib^2 - 2 omegab chib - sum d_i^2,
    e4 eta = -chi (eta - etab) - sum c_i a_i,       e3 etab = -chib (etab - eta) - sum c_i d_i,
    e4 omegab = eta^2/2 - eta etab + 2 omega omegab + (1/4) sum (a_i d_i + c_i^2),
    e3 omega  = etab^2/2 - eta etab + 2 omega omegab + (1/4) sum (a_i d_i + c_i^2),
    d_v k = e^w chi,  d_v w = -2 e^w omega,  d_v b = -2 e^{2w - k} (eta - etab),
and for each scalar the two Bianchi-type pairs (P1, P2) = (e3 a - ex c, e4 c - ex a), (P3, P4) = (e3 c - ex d,
e4 d - ex c), each equal to an explicit bilinear form G_P in (psi; a, c, d) when Box Phi = 0 (E1).

  E1 (exact) the four pair identities  P_j = G_Pj - [j odd] Box f  for any f, from null3.py's N4-N5:
         G_P1 = -chi d/2 - chib a/2 + 2 eta c + 2 omegab a,   G_P2 = -chi c + (eta + etab) a/2,
         G_P3 = -chib c + (eta + etab) d/2,                   G_P4 = -chi d/2 - chib a/2 + 2 etab c + 2 omega d.
  E2 (exact) the linearisation about a background, in the frame-difference unknowns Z (15 of them): every row reads
         X(dY) = sum_Z m_Z Z + S,   X in {e4, e3, d_v} (transport) or the pair operators,
     with coefficients m_Z that are polynomials in the background's state (psi, a, c, d, e^{+-w}, e^{-k}) and its first
     x-derivatives only (the frame derivatives of the background along X are replaced by its own equations, the
     residual going into S).  No derivative of any unknown appears on any right side: the level-0 hierarchy closes.
     The table (which unknowns enter which row) is printed.
  E3 control: replacing the e3-transport of chib by the e4 equation of null3.py N7 puts ex(d etab) on a right side --
     a derivative of an unknown -- and the check must flag it (the angular loss of the unused equations).
  E4 (computed) the constant: on a truncated domain of dependence D (|x| <= X at the initial cones, shrinking at the
     rates c_u = sup |b| + lam, c_v = sup(Omt^2/gt)/lam), every unknown's coefficient sum kappa_Z (coordinate-
     normalised, including the measure's own derivative and the split of each bilinear term) is evaluated on the
     record's computed solution (dnsolve5 --run 1 0.9 32 800 360, ld 3; D432) on rcert5's box u in [-4, -1.1],
     v in [0.55, 1.6]; a = max_Z sup_D kappa_Z, and Theorem 7.L's constant F^2 = 2 exp(4 a (Delta u + Delta v)).
  E5 (computed) the domain: the x-extent of D left at the box's far corner, for each X and lam -- how much of the late
     region a truncated domain reaches.
  E6 (computed) the demand on the residual: CERTIFY-10L5.md 2(d)'s  delta + int eps < 1/(4 G T F^2)  at that F.
  E7 (deduced; computed check) the two-variable Gronwall lemma: if f(u, v) <= A + a int_0^u f(u', v) du'
     + a int_0^v f(u, v') dv' on [0, U] x [0, V], then f <= 2 A exp(4 a (u + v)).  The extremal solution is computed
     and must lie below; control: the bound A exp(a (u + v)) must fail for it.

  python3 checks/linest5.py RUN.npz        (RUN: the record's l1_rc0.9_M32.npz)
"""
import os, sys, time, importlib.util
import numpy as np
import sympy as sp


def print(*a, **k):
    """print, every line wrapped at 121 characters (the record's line limit)"""
    import builtins, textwrap
    s = (k.pop('sep', ' ')).join(str(q) for q in a)
    lines = []
    for ln in s.split('\n'):
        if len(ln) <= 121:
            lines.append(ln)
        else:
            ind = len(ln) - len(ln.lstrip()) + 4
            lines.extend(textwrap.wrap(ln, 121, subsequent_indent=' ' * ind, break_on_hyphens=False))
    builtins.print('\n'.join(lines), **k)


HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('null3', os.path.join(HERE, 'null3.py'))
N3 = importlib.util.module_from_spec(_s); _s.loader.exec_module(N3)
_s = importlib.util.spec_from_file_location('dnsolve5', os.path.join(os.path.dirname(HERE), 'dnsolve5.py'))
D5 = importlib.util.module_from_spec(_s); _s.loader.exec_module(D5)

# state symbols of the background (frame values)
chi, chib, eta, etab, om, omb = sp.symbols('chi chib eta etab om omb')
a1, c1, d1, a2, c2, d2 = sp.symbols('a1 c1 d1 a2 c2 d2')
Ew, Ek = sp.symbols('Ew Ek', positive=True)          # e^w, e^k
PSI = [chi, eta, omb, chib, etab, om]
SC = [(a1, c1, d1), (a2, c2, d2)]
STATE = PSI + [a1, c1, d1, a2, c2, d2]
sa = lambda f: sum(f(*t) for t in SC)
G = {'chi': -chi ** 2 - 2 * om * chi - sa(lambda a, c, d: a ** 2),
     'eta': -chi * (eta - etab) - sa(lambda a, c, d: c * a),
     'omb': eta ** 2 / 2 - eta * etab + 2 * om * omb + sa(lambda a, c, d: a * d + c ** 2) / 4,
     'chib': -chib ** 2 - 2 * omb * chib - sa(lambda a, c, d: d ** 2),
     'etab': -chib * (etab - eta) - sa(lambda a, c, d: c * d),
     'om': etab ** 2 / 2 - eta * etab + 2 * om * omb + sa(lambda a, c, d: a * d + c ** 2) / 4}
DIR = {'chi': 'e4', 'eta': 'e4', 'omb': 'e4', 'chib': 'e3', 'etab': 'e3', 'om': 'e3'}
GP = lambda a, c, d: {'P1': -chi * d / 2 - chib * a / 2 + 2 * eta * c + 2 * omb * a,
                      'P2': -chi * c + (eta + etab) * a / 2,
                      'P3': -chib * c + (eta + etab) * d / 2,
                      'P4': -chi * d / 2 - chib * a / 2 + 2 * etab * c + 2 * om * d}
# metric rows, coordinate derivative d_v (k = log sqrt gt, w = log Omt)
w_, k_ = sp.symbols('w k')
GM = {'k': Ew * chi, 'w': -2 * Ew * om, 'b': -2 * Ew ** 2 / Ek * (eta - etab)}
# the unknowns
UNK = ['dchi', 'deta', 'domb', 'dchib', 'detab', 'dom', 'dk', 'dw', 'db',
       'da1', 'dc1', 'dd1', 'da2', 'dc2', 'dd2']
U = {n: sp.Symbol(n) for n in UNK}
TYPE = {'dchi': 'in', 'deta': 'in', 'domb': 'in', 'dk': 'in', 'dw': 'in', 'db': 'in',     # e4/d_v: L2 in u
        'dchib': 'out', 'detab': 'out', 'dom': 'out',                                    # e3: L2 in v
        'da1': 'out', 'da2': 'out', 'dd1': 'in', 'dd2': 'in', 'dc1': 'both', 'dc2': 'both'}
SMAP = {chi: 'dchi', eta: 'deta', omb: 'domb', chib: 'dchib', etab: 'detab', om: 'dom',
        a1: 'da1', c1: 'dc1', d1: 'dd1', a2: 'da2', c2: 'dc2', d2: 'dd2'}
# x-derivatives of the background state (spectral on the run), as symbols
DX = {s_: sp.Symbol('dx_' + str(s_)) for s_ in STATE}


def lin(Gexpr):
    """sum_s dG/ds ds, s over the state"""
    return sum(sp.diff(Gexpr, s_) * U[SMAP[s_]] for s_ in STATE)


def rows():
    """the linearised rows: name -> (LHS operator, unknown it bounds, RHS linear in the unknowns, coordinate factor)"""
    R = {}
    exw = 1 / Ek                                            # e^{-k}: ex = e^{-k} d_x
    for y in ('chi', 'eta', 'omb', 'chib', 'etab', 'om'):
        Y = sp.Symbol(y if y not in ('om', 'omb') else y)
        Ysym = {'chi': chi, 'eta': eta, 'omb': omb, 'chib': chib, 'etab': etab, 'om': om}[y]
        rhs = lin(G[y])
        # - (delta X) Y0: X = e4: + dw e4 Y0 = dw G_y; X = e3: + dw G_y - e^{-w} db d_x Y0
        rhs += U['dw'] * G[y]
        if DIR[y] == 'e3':
            rhs += -U['db'] / Ew * DX[Ysym]
        R[y] = (DIR[y], 'd' + y, sp.expand(rhs), Ew)     # coordinate: d_v = e^w e4, D_u = e^w e3
    for mrow in ('k', 'w', 'b'):
        g = GM[mrow]
        rhs = lin(g) + sp.diff(g, Ew) * Ew * U['dw'] + sp.diff(g, Ek) * Ek * U['dk']
        R[mrow] = ('dv', 'd' + mrow, sp.expand(rhs), 1)
    for i, (a, c, d) in enumerate(SC, 1):
        gp = GP(a, c, d)
        # e3 a - ex c: + dw e3 a0 - e^{-w} db d_x a0 - dk ex c0 ; e3 a0 = ex c0 + G_P1
        exc, exa, exd = DX[c] / Ek, DX[a] / Ek, DX[d] / Ek
        R['P1_%d' % i] = ('pair', 'da%d' % i, sp.expand(lin(gp['P1']) + U['dw'] * (exc + gp['P1'])
                                                       - U['db'] / Ew * DX[a] - U['dk'] * exc), Ew)
        R['P2_%d' % i] = ('pair', 'dc%d' % i, sp.expand(lin(gp['P2']) + U['dw'] * (exa + gp['P2'])
                                                       - U['dk'] * exa), Ew)
        R['P3_%d' % i] = ('pair', 'dc%d' % i, sp.expand(lin(gp['P3']) + U['dw'] * (exd + gp['P3'])
                                                       - U['db'] / Ew * DX[c] - U['dk'] * exd), Ew)
        R['P4_%d' % i] = ('pair', 'dd%d' % i, sp.expand(lin(gp['P4']) + U['dw'] * (exc + gp['P4'])
                                                       - U['dk'] * exc), Ew)
    return R


def e1():
    """the pair identities, exact, on the general (2+1)-metric of null3.py"""
    w, c, b, f = N3.w, N3.c, N3.b, N3.f
    u, v, x = N3.u, N3.v, N3.x
    g = N3.metric(); gi = g.inv(); sq = 2 * sp.exp(2 * w + c)
    e4 = lambda F_: sp.exp(-w) * sp.diff(F_, v)
    e3 = lambda F_: sp.exp(-w) * (sp.diff(F_, u) + b * sp.diff(F_, x))
    ex = lambda F_: sp.exp(-c) * sp.diff(F_, x)
    X3 = [u, v, x]
    box = sum(sp.diff(sq * gi[i, j] * sp.diff(f, X3[j]), X3[i]) for i in range(3) for j in range(3)) / sq
    fm = {'chi': sp.exp(-w) * sp.diff(c, v), 'chib': sp.exp(-w) * (sp.diff(c, u) + b * sp.diff(c, x) + sp.diff(b, x)),
          'om': -sp.exp(-w) * sp.diff(w, v) / 2, 'omb': -sp.exp(-w) * (sp.diff(w, u) + b * sp.diff(w, x)) / 2,
          'eta': -sp.exp(c - 2 * w) * sp.diff(b, v) / 4 + sp.exp(-c) * sp.diff(w, x),
          'etab': sp.exp(c - 2 * w) * sp.diff(b, v) / 4 + sp.exp(-c) * sp.diff(w, x)}
    a, cc, d = e4(f), ex(f), e3(f)
    sub = {chi: fm['chi'], chib: fm['chib'], om: fm['om'], omb: fm['omb'], eta: fm['eta'], etab: fm['etab']}
    gp = {k_: e.subs(sub) for k_, e in GP(a, cc, d).items()}
    lhs = {'P1': e3(a) - ex(cc), 'P2': e4(cc) - ex(a), 'P3': e3(cc) - ex(d), 'P4': e4(d) - ex(cc)}
    boxc = {'P1': -1, 'P2': 0, 'P3': 0, 'P4': -1}
    res = {k_: N3.zero(lhs[k_] - gp[k_] - boxc[k_] * box) for k_ in lhs}
    ctl = N3.zero(lhs['P4'] - gp['P4'].subs({}) - 0 * box)
    return res, ctl


def table(R):
    out = {}
    for name, (op, bnd, rhs, fac) in R.items():
        out[name] = sorted({str(q) for q in rhs.free_symbols if str(q) in U}, key=UNK.index)
    return out


def derivs_of_unknowns(rhs):
    return sorted(str(q) for q in rhs.free_symbols if str(q).startswith('dx_d'))


def gronwall_check():
    """extremal f = A + a int f du + a int f dv on [0, T]^2 by the trapezoid rule; compare with 2 A e^{4a(u+v)}"""
    out = []
    for a, T, n in ((1.0, 2.0, 400), (0.5, 4.0, 400), (3.0, 1.0, 400)):
        h = T / n; f = np.zeros((n + 1, n + 1)); A = 1.0
        Iu = np.zeros((n + 1, n + 1)); Iv = np.zeros((n + 1, n + 1))
        for t in range(2 * n + 1):
            for i in range(max(0, t - n), min(n, t) + 1):
                j = t - i
                iu = Iu[i - 1, j] + h / 2 * f[i - 1, j] if i > 0 else 0.0
                iv = Iv[i, j - 1] + h / 2 * f[i, j - 1] if j > 0 else 0.0
                # f = A + a (iu + h/2 f) + a (iv + h/2 f)  (implicit trapezoid in the last cell)
                kk = (h / 2 if i > 0 else 0) + (h / 2 if j > 0 else 0)
                f[i, j] = (A + a * iu + a * iv) / (1 - a * kk)
                Iu[i, j] = iu + (h / 2 * f[i, j] if i > 0 else 0)
                Iv[i, j] = iv + (h / 2 * f[i, j] if j > 0 else 0)
        uu = np.linspace(0, T, n + 1)
        bound = 2 * A * np.exp(4 * a * (uu[:, None] + uu[None, :]))
        weak = A * np.exp(a * (uu[:, None] + uu[None, :]))
        out.append((a, T, f[-1, -1], bound[-1, -1], bool(np.all(f <= bound)), bool(np.any(f > weak)),
                    float(np.log(f[-1, -1]) / (2 * T))))
    return out


def lam_np(exprs):
    syms = STATE + [Ew, Ek] + list(DX.values())
    return syms, [sp.lambdify(syms, e, 'numpy') for e in exprs]


def background(path, box=(-4.0, -1.1, 0.55, 1.6), step=2):
    """the Einstein-frame state of the computed solution on the box, subsampled; x-derivatives spectral"""
    Z = np.load(path)
    u, v, x, mask = Z['u'], Z['v'], Z['x'], Z['mask']
    iu = np.where((u >= box[0] - 0.05) & (u <= box[1] + 0.05))[0]
    iv = np.where((v >= box[2] - 0.05) & (v <= box[3] + 0.05))[0]
    sl = (slice(iu[0], iu[-1] + 1), slice(iv[0], iv[-1] + 1))
    F = {k: Z[k][sl] for k in ('R', 'm', 'n', 'W', 's')}
    u, v = u[sl[0]], v[sl[1]]
    M = len(x)
    _, D1, _ = D5.cheb_gauss(M)
    assert np.allclose(_, x)
    X = x[None, None, :]
    P = (2 * (1 + X) * F['m'] - (1 - X) * F['n']) / 3
    Q = (2 * (1 - X) * F['n'] - (1 + X) * F['m']) / 3
    lR = np.log(F['R'])
    fld = {'w': F['W'] + 2 * lR + P + Q + 0.5 * np.log((1 - X ** 2) / 4),
           'k': 3 * lR - np.log(4.0), 'b': (1 - X ** 2) * F['s'],
           'F1': np.sqrt(1.5) * (2 * lR + P + Q + 0.5 * np.log(1 - X ** 2) - np.log(2.0)),
           'F2': np.sqrt(2.0) * ((P - Q) / 2 + 0.25 * np.log((1 + X) / (1 - X)))}
    du = lambda A: np.gradient(A, u, axis=0)
    dv = lambda A: np.gradient(A, v, axis=1)
    dx = lambda A: np.einsum('ij,abj->abi', D1, A)
    d = {k: (du(f), dv(f), dx(f)) for k, f in fld.items()}
    w, k, b = fld['w'], fld['k'], fld['b']
    Ewv, Ekv = np.exp(w), np.exp(k)
    st = {}
    st[chi] = d['k'][1] / Ewv
    st[chib] = (d['k'][0] + b * d['k'][2] + d['b'][2]) / Ewv
    st[om] = -d['w'][1] / (2 * Ewv)
    st[omb] = -(d['w'][0] + b * d['w'][2]) / (2 * Ewv)
    z = -Ekv / Ewv ** 2 * d['b'][1] / 4
    st[eta] = z + d['w'][2] / Ekv
    st[etab] = -z + d['w'][2] / Ekv
    for (a, c, dd), Fk in zip(SC, ('F1', 'F2')):
        st[a] = d[Fk][1] / Ewv
        st[c] = d[Fk][2] / Ekv
        st[dd] = (d[Fk][0] + b * d[Fk][2]) / Ewv
    dxs = {DX[s_]: dx(st[s_]) for s_ in STATE}
    sub = (slice(None, None, step), slice(None, None, step))
    keep = mask[sl][sub]
    uu, vv = u[sub[0]], v[sub[1]]
    inbox = ((uu >= box[0]) & (uu <= box[1]))[:, None] & ((vv >= box[2]) & (vv <= box[3]))[None, :] & keep
    out = {s_: st[s_][sub] for s_ in STATE}
    out.update({k_: v_[sub] for k_, v_ in dxs.items()})
    out[Ew] = Ewv[sub]; out[Ek] = Ekv[sub]
    lw = np.log(2 * Ewv * Ekv)                                  # varpi = 2 Omt sqrt(gt) = 2 e^{w + k}
    out['dv_lw'] = dv(lw)[sub]; out['du_lw'] = du(lw)[sub]
    out['dx_bw'] = (dx(b * np.exp(lw)) / np.exp(lw))[sub]
    out['b'] = b[sub]; out['Om2_gt'] = (Ewv ** 2 / Ekv ** 2)[sub]
    return out, inbox, uu, vv, x


def kappas(R, bg, vals_needed=True):
    """kappa_Z for every unknown: sum over rows of |coefficient| (bilinear terms split in halves), coordinate-normalised,
    plus each row's measure term and 1 for its source; arrays over the background grid"""
    syms = STATE + [Ew, Ek] + list(DX.values())
    args = [bg[s_] for s_ in syms]
    kap = {n: 0.0 for n in UNK}
    for name, (op, bnd, rhs, fac) in R.items():
        fac_v = bg[Ew] if fac == Ew else 1.0
        for n in UNK:
            co = rhs.coeff(U[n])
            if co == 0:
                continue
            cv = np.abs(sp.lambdify(syms, co, 'numpy')(*args) * fac_v) * np.ones_like(bg[Ew])
            if name.startswith('P'):
                # pair rows enter the energy identity as 2 * (bounded unknown) * rhs
                kap[bnd] = kap[bnd] + cv; kap[n] = kap[n] + cv
            else:
                kap[bnd] = kap[bnd] + cv; kap[n] = kap[n] + cv
        # the measure's own derivative, and the source (2 |Z| |S| <= Z^2 + S^2)
        if op == 'e4' or op == 'dv':
            kap[bnd] = kap[bnd] + np.abs(bg['dv_lw']) + 1.0
        elif op == 'e3':
            kap[bnd] = kap[bnd] + np.abs(bg['du_lw'] + bg['dx_bw']) + 1.0
        else:
            kap[bnd] = kap[bnd] + 1.0
    # the energy identities' own quadratic forms (null3.py N6: div e3 = chib - 2 omegab, div e4 = chi - 2 omega,
    # div ex = eta + etab), times e^w
    E = bg[Ew]
    q3 = np.abs(E * (bg[chib] - 2 * bg[omb])); q4 = np.abs(E * (bg[chi] - 2 * bg[om]))
    qx = np.abs(E * (bg[eta] + bg[etab]))
    for i in (1, 2):
        kap['da%d' % i] = kap['da%d' % i] + q3 + qx
        kap['dc%d' % i] = kap['dc%d' % i] + q4 + qx + q3 + qx
        kap['dd%d' % i] = kap['dd%d' % i] + q4 + qx
    return kap


def main():
    t0 = time.time(); ok = True
    res, _ = e1()
    good = all(res.values())
    print('E1 pair identities P1-P4 (exact, Box f included where it enters):', res, '->', 'PASS' if good else 'FAIL')
    ok &= good
    R = rows()
    tab = table(R)
    bad = {nm: derivs_of_unknowns(r[2]) for nm, r in R.items() if derivs_of_unknowns(r[2])}
    print('E2 the linearised rows (%d), the unknowns on each right side:' % len(R))
    for nm, lst in tab.items():
        print('   %-7s (%s, bounds %s): %s' % (nm, R[nm][0], R[nm][1], ' '.join(lst)))
    allsyms = set().union(*[r[2].free_symbols for r in R.values()])
    bgsyms = {str(q) for q in allsyms} - set(UNK)
    good = not bad and all(s_.startswith('dx_') or s_ in {str(q) for q in STATE} | {'Ew', 'Ek'} for s_ in bgsyms)
    print('   no derivative of an unknown on any right side: %s; background enters through its state and first '
          'x-derivatives only: %s ->' % (not bad, good), 'PASS' if good else 'FAIL')
    ok &= good
    # E3 control: chib from null3.py N7's e4 equation, which carries 2 ex(etab): its linearisation has ex(d etab)
    ctl_rhs = sp.expand(lin(-chi * chib) + 2 * sp.Symbol('dx_detab') / Ek)
    hit = derivs_of_unknowns(ctl_rhs)
    print('E3 control: chib by null3.py N7\'s e4 equation: derivatives of unknowns on the right side: %s ->' % hit,
          'fails (good)' if hit else 'passes (bad)')
    ok &= bool(hit)
    # E7
    gr = gronwall_check()
    good = all(r[4] and r[5] for r in gr)
    for a, T, fT, bT, below, exceeds, rate in gr:
        print('E7 a = %.1f, T = %.1f: extremal f(T, T) = %.4g, bound 2 e^{8aT} = %.4g, below everywhere: %s; '
              'exceeds e^{a(u+v)} (control, must): %s; growth rate log f/(2T) = %.3f a' % (
                  a, T, fT, bT, below, exceeds, rate / a))
    print('E7', 'PASS' if good else 'FAIL'); ok &= good
    if len(sys.argv) < 2:
        print('linest5 (no run given; E4-E6 skipped):', 'all checks pass' if ok else 'FAILURES')
        return 0 if ok else 1
    bg, inbox, uu, vv, x = background(sys.argv[1])
    print('   (%.0f s) background on rcert5\'s box: %d x %d x %d nodes (every second row and column)' % (
        time.time() - t0, len(uu), len(vv), len(x)))
    kap = kappas(R, bg)
    Du, Dv = -1.1 - (-4.0), 1.6 - 0.55
    bsup = float(np.nanmax(np.abs(bg['b'][inbox])))
    print('E4 the coefficient sums kappa_Z on the box (sup over the cells kept), by angular band |x| <= X:')
    hdr = '   %-7s' % 'X' + ''.join('%10s' % n for n in UNK)
    print(hdr)
    results = []
    for Xb in (0.5, 0.8, 0.95, float(x[0])):
        sel = inbox[:, :, None] & (np.abs(x)[None, None, :] <= Xb + 1e-12)
        row = []
        for n in UNK:
            kz = kap[n]
            row.append(float(np.nanmax(np.where(sel, kz, np.nan))))
        a_ = max(row)
        cv_sup = float(np.nanmax(np.where(sel, bg['Om2_gt'], np.nan)))
        F2 = 2 * np.exp(4 * a_ * (Du + Dv))
        results.append((Xb, a_, F2, cv_sup, row))
        print('   %-7.4f' % Xb + ''.join('%10.3g' % r for r in row))
    print('   (rows: X; columns: kappa_Z sup.  a = the largest.)')
    for Xb, a_, F2, cv_sup, row in results:
        lg = 4 * a_ * (Du + Dv) / np.log(10) + np.log10(2)
        print('E4 X = %.4f: a = %.3g, worst unknown %s; F^2 = 2 exp(4 a (Du + Dv)) = 10^%.1f, F = 10^%.1f' % (
            Xb, a_, UNK[int(np.argmax(row))], lg, lg / 2))
    # E5: the domain
    print('E5 the truncated domain on the box (sup |b| = %.3g): x-extent left at the far corner, '
          'X - c_u Du - c_v Dv with c_u = sup|b| + lam, c_v = sup(Omt^2/gt)/lam, lam optimal:' % bsup)
    for Xb, a_, F2, cv_sup, row in results:
        lam = np.sqrt(cv_sup * Dv / Du)
        shrink = (bsup + lam) * Du + cv_sup / lam * Dv
        print('   X = %.4f: sup(Omt^2/gt) = %.3g, shrink = %.3g -> half-width left %.3g (%s)' % (
            Xb, cv_sup, shrink, Xb - shrink, 'empty' if Xb - shrink <= 0 else 'nonempty'))
    # E6: the demand
    print('E6 the closing condition delta + int eps < 1/(4 G T F^2), T = Du + Dv = %.2f, at G = 10 and G = 382:' % (
        Du + Dv))
    for Xb, a_, F2, cv_sup, row in results:
        lg = 4 * a_ * (Du + Dv) / np.log(10) + np.log10(2)
        for Gq in (10.0, 382.0):
            dem = -(np.log10(4 * Gq * (Du + Dv)) + lg)
            print('   X = %.4f, G = %g: demand 10^%.1f' % (Xb, Gq, dem))
    print('linest5 (%.0f s):' % (time.time() - t0), 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
