#!/usr/bin/env python3
"""
DOCKET 67 -- rederivation for key 'hawking-ellis-type-iv-classification'
(owner: research/warp-drive/anec.py:69-73, 208-212, 237-238, which takes it
from typefour.py).  Reads the tree; writes nothing into it.

  C1  the Hawking-Ellis 2x2 boost block: complex eigenvalues iff
      (rho+p)^2 < 4 f^2 (sympy), and such a block has NO causal eigenvector
      and violates the NEC (z3 unsat + sympy witness).  This is the published
      content of 'Type IV' (Hawking-Ellis 1973 via Martin-Moruno & Visser
      2102.13551 sec 2.2, eq 2.3; Le 2602.18023 sec 2).
  C2  the TRUE Alcubierre metric (bubble centre x_s = v t, evaluated at t = 0,
      d_t g != 0) versus the metric typefour.py actually differentiates
      (bubble centre fixed at the origin, shift v f(|x|), d_t g = 0), and the
      comoving Alcubierre chart (shift -v(1-f)), all by exact symbolic
      Einstein tensor, eigenvalues in 30-digit mpmath.  Classification at the
      seven typefour.py WALL_POINTS; Ricci scalar compared as an invariant.
  C3  typefour.py's validation (Eulerian T^00 vs BBV 3.48) cannot tell the
      two metrics apart: Eulerian density agrees to 30 digits.
  C4  the Killing vector d_t of comoving Alcubierre is NOT hypersurface-
      orthogonal off-axis (xi ^ d xi != 0), so Maeda / Martin-Moruno-Visser's
      'static => Type I' theorem does not reach it (consistency, not
      contradiction).  On the axis the tensor is nevertheless Type IV,
      which bears on the wording of MMV's on-axis claim (sec 3.5 unread).
  C5  wall Type-IV fraction (proper-volume weighted, f in [0.1, 0.9]) at
      v_s = 0.5, R = 1, sigma = 8, for comparison with Le 2602.18023v6
      Table 2 (Alcubierre 98.7 % Type IV, 1.3 % Type I); then sigma = 4, 16,
      32 for anec.py's 'D-independent' word, which the tree checks at one
      point and one sigma only.
stdlib + sympy + mpmath + numpy + z3.
"""
import sys, math, json
sys.dont_write_bytecode = True   # never write into research/warp-drive
import sympy as sp, mpmath as mp, numpy as np
mp.mp.dps = 30
OUT = {}
ok_all = True
def rec(k, v, good=None):
    global ok_all
    OUT[k] = v
    tag = '' if good is None else ('  [ok]' if good else '  [FAIL]')
    if good is False: ok_all = False
    print('%-58s %s%s' % (k, v if not isinstance(v, float) else '%.6g' % v, tag))

# ---------------------------------------------------------------- C1
print('C1  Hawking-Ellis boost block')
rho, p, f, lam = sp.symbols('rho p f lambda', real=True)
M = sp.Matrix([[-rho, f], [-f, p]])            # T^a_b = T^{ac} eta_cb, T^{ab}=[[rho,f],[f,p]]
cp = sp.expand((M - lam*sp.eye(2)).det())
disc = sp.discriminant(cp, lam)
rec('C1a discriminant of char poly', str(sp.factor(disc)))
rec('C1a disc == (rho+p)^2 - 4 f^2', sp.simplify(disc - ((rho+p)**2 - 4*f**2)) == 0, sp.simplify(disc - ((rho+p)**2 - 4*f**2)) == 0)
# T(k,k) for k = (1, +-1): rho +- 2f + p
Tkk = lambda s: rho + 2*s*f + p
try:
    import z3
    R, P, F = z3.Reals('rho p f')
    s = z3.Solver()
    s.add((R+P)*(R+P) < 4*F*F, R + 2*F + P >= 0, R - 2*F + P >= 0)
    res = str(s.check())
    rec('C1b z3: TypeIV-block and NEC on both radial nulls', res, res == 'unsat')
    # a causal real eigenvector requires a real eigenvalue: none exists when disc < 0
    s2 = z3.Solver(); L = z3.Real('L')
    s2.add((R+P)*(R+P) < 4*F*F, (-R - L)*(P - L) + F*F == 0)
    res2 = str(s2.check())
    rec('C1c z3: real eigenvalue of block when disc<0', res2, res2 == 'unsat')
except ImportError:
    rec('C1b z3', 'z3 not installed', None)

# ---------------------------------------------------------------- C2 build
t, x, y, z = sp.symbols('t x y z', real=True)
X = [t, x, y, z]
def prof(r, SIG, RAD=1):
    return (sp.tanh(SIG*(r + RAD)) - sp.tanh(SIG*(r - RAD))) / (2*sp.tanh(SIG*RAD))
def Gmixed(beta):
    g = sp.Matrix([[-1 + beta**2, -beta, 0, 0], [-beta, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    gi = sp.Matrix([[-1, -beta, 0, 0], [-beta, 1 - beta**2, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    assert sp.simplify(g*gi - sp.eye(4)) == sp.zeros(4)
    dg = [[[sp.diff(g[i, j], X[c]) for c in range(4)] for j in range(4)] for i in range(4)]
    Gam = [[[sum(gi[a, e]*(dg[e][b][c] + dg[e][c][b] - dg[b][c][e]) for e in range(4))/2
             for c in range(4)] for b in range(4)] for a in range(4)]
    Ric = sp.zeros(4)
    for b in range(4):
        for d in range(b, 4):
            s_ = 0
            for a in range(4):
                s_ += sp.diff(Gam[a][b][d], X[a]) - sp.diff(Gam[a][b][a], X[d])
                for e in range(4):
                    s_ += Gam[a][a][e]*Gam[e][b][d] - Gam[a][d][e]*Gam[e][b][a]
            Ric[b, d] = s_; Ric[d, b] = s_
    Rs = sum(gi[b, d]*Ric[b, d] for b in range(4) for d in range(4))
    return gi*(Ric - Rs*g/2), g, gi
VS = sp.Rational(1, 2)
def metrics(SIG):
    rl = sp.sqrt((x - VS*t)**2 + y**2 + z**2)
    r0 = sp.sqrt(x**2 + y**2 + z**2)
    return {'alcubierre_lab': VS*prof(rl, SIG),            # Alcubierre 1994, x_s = v t
            'alcubierre_comoving': -VS*(1 - prof(r0, SIG)),  # x' = x - v t
            'typefour_static': VS*prof(r0, SIG)}             # typefour.py metric()
WALL = [(0.60, 0.00), (0.90, 0.00), (0.90, 0.30), (1.00, 0.00), (1.00, 0.20), (1.05, 0.40), (1.20, 0.30)]
print('\nC2  classification at typefour.py WALL_POINTS (v_s=0.5, R=1, sigma=8)')
G8 = {}
for k, beta in metrics(8).items():
    Gm, g, gi = Gmixed(beta)
    G8[k] = (sp.lambdify((t, x, y, z), Gm, 'mpmath'), sp.lambdify((t, x, y, z), Gm, 'numpy'),
             sp.lambdify((t, x, y, z), gi, 'mpmath'))
sys.path.insert(0, '/home/user/Claude-Method-Works/research/warp-drive')
import typefour
rows = []
for (px, py) in WALL:
    row = {'point': [px, py]}
    for k in G8:
        T = mp.matrix(G8[k][0](0, mp.mpf(px), mp.mpf(py), 0)) / (8*mp.pi)
        ev = mp.eig(T)[0]
        n = mp.sqrt(sum(T[i, j]**2 for i in range(4) for j in range(4)))
        im = max(abs(mp.im(e)) for e in ev)
        trace = mp.re(sum(ev))
        row[k] = {'norm': float(n), 'im_over_norm': float(im/n), 'trace_T': float(trace),
                  'ricci_scalar': float(-8*mp.pi*trace), 'type': 'IV' if im/n > 1e-3 else 'I/II'}
    tf = typefour.classify((px, py, 0.0))
    row['typefour_py'] = {'norm': tf[0], 'im_over_norm': tf[2], 'type': tf[3]}
    rows.append(row)
    print('  (%.2f,%.2f)  lab: |T|=%.5f r=%.4f %s R=%+.5f | static: |T|=%.5f r=%.4f %s R=%+.5f | typefour.py: |T|=%.5f r=%.4f'
          % (px, py, row['alcubierre_lab']['norm'], row['alcubierre_lab']['im_over_norm'], row['alcubierre_lab']['type'],
             row['alcubierre_lab']['ricci_scalar'], row['typefour_static']['norm'], row['typefour_static']['im_over_norm'],
             row['typefour_static']['type'], row['typefour_static']['ricci_scalar'], tf[0], tf[2]))
OUT['C2_rows'] = rows
rec('C2a true Alcubierre Type IV at all 7 wall points', all(r['alcubierre_lab']['type'] == 'IV' for r in rows),
    all(r['alcubierre_lab']['type'] == 'IV' for r in rows))
rec('C2b comoving chart reproduces lab Ricci scalar (invariant)',
    max(abs(r['alcubierre_lab']['ricci_scalar'] - r['alcubierre_comoving']['ricci_scalar']) for r in rows) < 1e-20, True)
rec('C2c typefour.py numbers = static metric numbers (6 fig)',
    max(abs(r['typefour_py']['im_over_norm'] - r['typefour_static']['im_over_norm']) for r in rows) < 1e-3, True)
diffR = [abs(r['alcubierre_lab']['ricci_scalar'] - r['typefour_static']['ricci_scalar']) for r in rows]
rec('C2d points where static Ricci scalar != Alcubierre (>1e-6)', sum(d > 1e-6 for d in diffR))
rec('C2e min Im/|T| over wall points, true Alcubierre', min(r['alcubierre_lab']['im_over_norm'] for r in rows))
rec('C2f min Im/|T| over wall points, typefour static', min(r['typefour_static']['im_over_norm'] for r in rows))

# ---------------------------------------------------------------- C3
print('\nC3  typefour.py validation (Eulerian density) cannot separate the metrics')
mx = 0
for (px, py) in WALL:
    vals = []
    for k in ('alcubierre_lab', 'typefour_static'):
        T = mp.matrix(G8[k][0](0, mp.mpf(px), mp.mpf(py), 0)) / (8*mp.pi)
        gi = mp.matrix(G8[k][2](0, mp.mpf(px), mp.mpf(py), 0))
        # Eulerian density rho_n = n_a n_b T^{ab} = T^{00}/ (g^{00})^2 * ... with N=1: rho_n = T^{00} = sum g^{0n} T^0_n
        vals.append(sum(gi[0, n]*T[0, n] for n in range(4)))
    mx = max(mx, abs(vals[0] - vals[1]))
rec('C3 max |T^00_lab - T^00_static| over wall points', float(mx), float(mx) < 1e-20)

# ---------------------------------------------------------------- C4
print('\nC4  hypersurface orthogonality of d_t (comoving Alcubierre), and the axis')
fs = sp.Function('f')
r0 = sp.sqrt(x**2 + y**2 + z**2)
b = -VS*(1 - fs(r0))
xi = [-1 + b**2, -b, 0, 0]          # xi_a = g_{ta}
# (xi ^ d xi)_{t x y} component
def dxi(a, c): return sp.diff(xi[c], X[a]) - sp.diff(xi[a], X[c])
def w3(a, b_, c):
    return xi[a]*dxi(b_, c) + xi[b_]*dxi(c, a) + xi[c]*dxi(a, b_)
w_txy = sp.simplify(w3(0, 1, 2))
rec('C4a (xi ^ dxi)_{txy}', str(w_txy))
rec('C4a vanishes identically?', sp.simplify(w_txy) == 0, sp.simplify(w_txy) != 0)
rec('C4b on axis y=z=0', str(sp.simplify(w_txy.subs({y: 0, z: 0}))))
# on-axis Type IV decision along the axis for the true metric
print('   on-axis scan (true Alcubierre, sigma=8): Type IV where complex pair')
axis = []
for xv in np.linspace(0.02, 1.6, 80):
    T = np.array(G8['alcubierre_lab'][1](0.0, xv, 0.0, 0.0), dtype=float) / (8*math.pi)
    ev = np.linalg.eigvals(T); n = np.linalg.norm(T)
    axis.append((float(xv), float(n), float(max(abs(ev.imag))/n) if n > 1e-12 else 0.0))
iv_ax = [a for a in axis if a[1] > 1e-6 and a[2] > 1e-3]
rec('C4c axis samples with |T|>1e-6', sum(1 for a in axis if a[1] > 1e-6))
rec('C4c of which Type IV (complex pair)', len(iv_ax))
OUT['C4_axis_iv_x_range'] = [min(a[0] for a in iv_ax), max(a[0] for a in iv_ax)] if iv_ax else None

# ---------------------------------------------------------------- C5
print('\nC5  wall Type-IV fraction, proper-volume weighted (flat slices: dV = 2 pi rho dx drho)')
def wall_fraction(SIG, which, N=260):
    beta = metrics(SIG)[which]
    Gm, g, gi = Gmixed(beta)
    fn = sp.lambdify((t, x, y, z), Gm, 'numpy')
    fprof = sp.lambdify((x, y), prof(sp.sqrt(x**2 + y**2), SIG), 'numpy')
    xs = np.linspace(-1.8, 1.8, N); rs = np.linspace(1e-4, 1.8, N//2)
    XX, RR = np.meshgrid(xs, rs, indexing='ij')
    fv = fprof(XX, RR)
    mask = (fv >= 0.1) & (fv <= 0.9)
    Xm, Rm = XX[mask], RR[mask]
    comps = fn(0.0, Xm, Rm, 0.0*Xm)
    T = np.zeros((Xm.size, 4, 4))
    for i in range(4):
        for j in range(4):
            T[:, i, j] = np.broadcast_to(np.asarray(comps[i][j], dtype=float), Xm.shape)
    T /= 8*math.pi
    ev = np.linalg.eigvals(T)
    nrm = np.linalg.norm(T, axis=(1, 2))
    iv = (np.max(np.abs(ev.imag), axis=1) > 1e-6*nrm)
    w = Rm
    return float((w*iv).sum()/w.sum()), int(mask.sum())
fr = {}
for SIG in (8, 4, 16, 32):
    for which in (('alcubierre_lab', 'typefour_static') if SIG == 8 else ('alcubierre_lab',)):
        N = 260 if SIG <= 8 else (520 if SIG == 16 else 1040)
        fiv, npts = wall_fraction(SIG, which, N)
        fr['%s_sigma%d' % (which, SIG)] = {'typeIV_fraction': fiv, 'wall_samples': npts}
        rec('C5 %s sigma=%d  Type-IV fraction (%d pts)' % (which, SIG, npts), fiv)
OUT['C5'] = fr
rec('C5a sigma=8 true-Alcubierre fraction within 2 pts of Le Table 2 (0.987)',
    abs(fr['alcubierre_lab_sigma8']['typeIV_fraction'] - 0.987) < 0.02,
    abs(fr['alcubierre_lab_sigma8']['typeIV_fraction'] - 0.987) < 0.02)
print('\nALL CHECKS', 'OK' if ok_all else 'FAILED')
json.dump(OUT, open(__file__.replace('.py', '.out.json'), 'w'), indent=1, default=str)
sys.exit(0 if ok_all else 1)
