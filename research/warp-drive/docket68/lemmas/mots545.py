#!/usr/bin/env python3
"""mots545.py -- item 545: the inner marginally trapped surface the record's scheme was read as showing at the physical
wavelength, investigated exhaustively.  It does not form.  Labels: computed (exact unless marked), deduced, READ, M's.

  M0 (M's) 545, verbatim: "Does 519 cover this? - no it does not. Please investigate this exhaustively, and report back
     the findings, how it affects the rest of the theorem, and how to mitigate it if it does, or determine if it
     applies at all".
  M1 (deduced; computed exact) The expansion of a cross-section.  On the slice v = const of hf_mirror5's metric (r =
     y^-2, x = cos 2 th, the circles e^{2 Q1}, e^{2 Q2}) the surface y = Y(x) has the null normals l = d_y (the slice's
     ingoing generator) and k, with
         theta_l = -6/y < 0,
         theta_k[Y] = (3/2) Y^2 W + V_x + Y' V_y + 8 E [(1 - x^2)(Y Y'' - 2 Y'^2) - 2 x Y Y']
                      + 8 Y Y' (1 - x^2)(E_x + E_y Y'),
     E = e^{2(beta + S)}, every field at (Y(x), x), no v-derivative.  At Y' = 0 it is hf_mirror5 X10's round-sphere
     expansion (checked on the record's slice to the x-grid's aliasing).  A marginally trapped surface is a closed
     surface with theta_k = 0 at every point.  A sign change of a round sphere's theta_k along a column -- what growth5
     counts -- is not one.
  M2 (deduced) Every closed cross-section is a graph.  The slice is ruled by its null generators d_y, and a spacelike
     surface cannot contain a null direction.  So projecting a closed connected spacelike surface in the domain along
     the generators onto their S^3 is a local diffeomorphism of compact onto connected: a covering, hence (S^3 simply
     connected) one-to-one.  The surface is y = Y(omega), embedded; no fold, self-intersection or torus can occur on a
     null slice, and a T^2-invariant one is a curve y = Y(x).
  M3 (deduced) Ellipticity and comparison.  In the base metric g_yy = g_yx = 0, so the induced metric of y = Y(omega)
     involves no derivative of Y, and theta_k is quasi-linear with a positive multiple of its Laplacian as principal
     part (8 E Y (1 - x^2) Y'' in M1).  If two cross-sections touch at p, the outer one's (smaller y) theta_k at p is at
     most the inner one's.  So a marginally trapped surface's innermost point lies where the round spheres are locally
     untrapped and its outermost where they are trapped (the record's own hf_mirror5 horizon docstring).
  M4 (deduced; computed exact) The control.  With u = 1/Y, Y Lap Y - 2 |grad Y|^2 = -u^-3 Lap u on S^3 (sympy), so on
     Tangherlini theta_k = (3/2) u^-2 (1 - mu u^-4) - 2 u^-3 Lap u.  At the greatest and the least u the maximum
     principle gives u = mu^(1/4): on Tangherlini's ingoing null slices the only marginally trapped surface of any
     shape is r = sqrt(mu), strictly stable.  On its Painleve-Gullstrand slices five-dimensional Schwarzschild holds a
     family of closed self-intersecting interior ones (READ, M11).  Interior marginally trapped surfaces belong to a
     slicing, and a black hole with no inner horizon holds them.
  M5 (deduced; computed, numerical) The exhaustive search among T^2-invariant surfaces.  theta_k[Y] = 0 is a
     second-order ODE on [-1, 1], regular singular at both axes with indicial roots 0, 0.  The solutions regular at
     x = -1 are one family fixed by Y(-1), so the T^2-invariant marginally trapped surfaces are exactly the zeros of one
     function C(Y(-1)), the singular solution's coefficient at x = +1.  Shot by RK4 (mesh graded to both axes) from 600
     values of Y(-1) inside half the least round zero; a shot leaving the domain counts as +-inf on its side.  Each sign
     change is refined, kept only if its shot stays in the domain with |C| < 1e-6, polished by Newton collocation on
     the scheme's own x-grid (kept only if the polish stays on the shot), and given lambda_1 = -max Re eig of theta_k's
     linearisation.
  M6 (deduced; computed, numerical) The sweep, which bounds every surface of any shape.  From the outer marginally
     trapped surface, closed T^2-invariant leaves are continued by Newton collocation.  Inward they solve theta_k = c g,
     c < 0, with g = max(1, -the round expansion at the core boundary) > 0, so each is strictly trapped; they run until
     one lies wholly past the core boundary.  Past it the fields are continued by their boundary values, since only a
     leaf's part in the domain is ever compared, and nesting is required only there.  Outward they solve theta_k = c >
     0 until one lies wholly outside the least round zero.  A marginally trapped surface of any shape in the domain
     would touch, from the wrong side, the deepest inward leaf it reaches or the farthest outward one (M2, M3): so
     where both sweeps complete the outer one is the only one.  Checked between the nodes on 401 points: every inward
     leaf's theta_k < 0 and every outward one's > 0 in the domain, consecutive leaves nested.
  M7 (deduced; READ) A surface not invariant under a rotation of the circles would be carried by it through
     marginally trapped surfaces, giving its stability operator the eigenfunction d_phi Y, which changes sign, so it
     would be unstable (Booth, Cox and Margalef-Bentabol, Theorem 1.6).  Moot wherever M6 completes.
  M8 (computed, numerical; pinned) The slices.  The record's scheme run with growth5's code at the five points where a
     second round zero was reported, the accepted state captured at the step nearest each hundredth of v from where
     the zero first appears; "outflow" is the premise's causal clause, W < 0 at the core boundary:
       point                          v span     slices  outflow  2nd round zero  W 2nd zero  one MOTS  unique  lambda_1
       ---------------------------------------------------------------------------------------------------------
       10 l5, mu0 = 100 l5^2          1.31-1.69      40       21              10           0        21      21    5.89
       10 l5, mu0 = 1000 l5^2         1.40-1.68      29       28               9           0        28      27    5.93
       lam_P, copper (102.4)          1.30-1.80      51       26              10           0        26      26    5.92
       lam_P, the example README (60.9) 1.30-1.73      35       17              10           0        17      17    5.90
       lam_P, r0 = 20 ell (808.5)     1.60-2.30      71       71              47           0        71      71    5.70
     226 slices: on all 163 with the boundary outflow the search finds one marginally trapped surface, the outer
     apparent horizon, strictly stable; 162 are unique of any shape by the sweeps.  The 163rd (10 l5 at mu0 = 1000,
     v = 1.671, two steps before the slice solve fails) sweeps completely, but one leaf's expansion between the nodes
     is +0.0025 against the outer surface's own between-node residual of 0.034 there: unique to the x-grid's
     resolution, not certified.  On the 63 slices past the premise, where the scheme's excision is ill-posed, the
     search still finds exactly one.  The extra round zeros are the angular shift's term (2/3) y^3 d_x((1 - x^2) q):
     W alone has one zero per column on every one of the 86 slices that show them.
  M9 (computed) Resolution.  Copper at Ny = 28 and at Nx = 20 (v = 1.30-1.60, 16 slices each): the outer surface's
     radii agree with Ny = 20 to 1e-4 at Nx 20 (the same steps) and to 3e-3 at Ny 28 (its steps fall up to 0.007
     in v away), lambda_1 to 0.01, and every slice with the boundary
     outflow is unique at both (13 and 13).  The round-zero count itself moves with resolution (13 slices with a second
     zero at Ny = 28, 4 at Nx = 20, 10 at Ny = 20 over the same span): the proxy is noisy, the result is not.  Nx = 24
     makes the scheme itself unstable (it fails at v = 0.39).
  M10 (computed; pinned) Mitigation at the small end.  What stops the scheme at the least seeds is its core boundary
     turning inflow, not an inner surface.  At lam_P on larger seeds (growth5.run, the same envelope, its breakdown
     criterion): a seed of mu0 >= 808.5 l5^2 keeps the core boundary outflow
     through the shell (r0 = 20 ell's own run, both grids, W at the boundary at most -1.50; mu0 = 1000, at most -3.59),
     and every seed up to 750 l5^2 turns it inflow before the shell ends: 300 at v = 1.82, 500 at 2.50 (2.53 at Ny =
     28), 650 at 2.18 (2.19), 750 at 2.13 -- not monotone below the threshold.  So the record's scheme stays valid
     through the shell at the small end on a seed some 8 to 13 times the least (copper 102, the example README 61
     l5^2).  seed_derive D2 lets a seed exceed the least, since escape falls as it grows.
  M11 (READ) Prior art.
     - Booth, Chan, Hennigar, Kunduri and Muth (2210.15685v2, p. 17): "self-intersecting MOTSs may also be found in D =
       5 Schwarzschild and they are qualitatively the same as in D = 4"; p. 49: "a family of closed, self-intersecting
       MOTSs contained in the black hole interior".  Booth, Hennigar and Mondal (2005.05350v3, p. 16): "an (apparently)
       infinite number of self-intersecting MOTS inside r = 2m".
     - Booth, Brits, Gonzalez and Van Den Broeck (gr-qc/0506119v2, p. 4): "large (though not infinite) concentrations
       of matter may force the creation of a dynamical horizon-timelike membrane pair ... Timelike membrane-dynamical
       horizon pairs can annihilate each other"; p. 6: an MTT "is a timelike membrane if and only it is a future inner
       trapping horizon"; p. 23: "all of these intricacies are contained within the outermost isolated horizon ... and
       would not be visible to outside observers".  Pook-Kolb, Birnholtz, Krishnan and Schnetter (1903.05626v3, p. 2),
       in vacuum: "a common horizon is formed, which bifurcates into an inner branch ... and an outer branch".
     - Galloway and Schoen (gr-qc/0509107v2, p. 6), in any dimension: "marginally outer trapped surfaces cannot occur
       outside the event horizon".
     - Booth, Cox and Margalef-Bentabol (2311.02063v2, p. 3, Theorem 1.6): "Suppose S is a MOTS and X is a symmetry of
       (Sigma, g, K) but not of S.  Then 0 is an eigenvalue of L_S ... (2) S is unstable if and only if X is tangent to
       S at some point."
  M12 (deduced) What it decides.
     - It does not apply.  No inner marginally trapped surface forms on the record's slices at any of the five points,
       so there is no inner trapping horizon either.  544's sentence (carried from N1STAR-PROOF section 10.2) is
       withdrawn.
     - 519 is unchanged.  The work has no inner or Cauchy horizon, and the end state is Tangherlini, which has neither
       (SETTLE, SETTLEs S1).  A black hole without an inner horizon may still hold interior marginally trapped surfaces
       on some slicing (M4): their presence on a slicing is not what an inner horizon is.
     - The rest of the theorem: no status moves.  The second round zero was the premise's one-zero clause, the
       record's proxy for one horizon, and on these slices it fails only by the angular shift's term.
       - What stops the scheme at the small end is the causal clause: the core boundary turns inflow (copper from v =
         1.5625, the example README from 1.5125; at 10 l5 from 1.516 and 1.680).  So the passage at the physical
         wavelength through the seed's interior stays named theorized (SOURCE-PROOF Part E).
       - At the large end the boundary stays outflow and one horizon holds throughout; the run past v = 1.833 is not
         converged (derived_go D2).
       - The face forms with one horizon at the physical wavelength too, on every slice the scheme computes with its
         boundary outflow.
     - Mitigation: the surface needs none, since it does not form.  For the small end's inflow boundary see M10; the
       route needing no excision, the characteristic problem in double-null gauge, stays named (N1STAR-PROOF 10.2).

What this does not claim: a theorem about the spacetime (the slices are the scheme's, and a run of a scheme is not a
proof); anything inside the core boundary, which bounds the record's core; anything on other slicings, where the prior
art shows interior marginally trapped surfaces are generic even in Tangherlini.

Usage: python3 mots545.py --selftest | --mutants | --scan NAME v0 v1 dv [Ny [Nx]] | --report
"""
import importlib.util, json, math, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
G5 = os.path.join(HERE, "..", "n1star", "growth5.py")
DATA = os.path.join(HERE, "data", "mots545_scans.json")
SLICE = os.path.join(HERE, "data", "mots545_slice.json")
MITIG = os.path.join(HERE, "data", "mots545_mitigation.json")
LAM_P = (64*math.pi**2/3)**(1/3)
POINTS = {"L100_10l5": (100.0, 1.0), "L1000_10l5": (1000.0, 10/math.sqrt(1000)),
          "copper": (102.4, LAM_P/math.sqrt(102.4)), "example": (60.9, LAM_P/math.sqrt(60.9)),
          "r0=20ell": (808.5, LAM_P/math.sqrt(808.5))}
FIELDS = ("w", "w_y", "w_x", "q", "q_y", "q_x", "b", "b_y", "b_x", "F", "F_y", "F_x", "G", "G_y", "G_x")
NEED = ("w", "q", "q_x", "q_y", "b", "b_y", "b_x", "G", "G_y", "G_x", "F", "F_y", "F_x")
MUT = set()


def words():
    return ("Does 519 cover this? - no it does not. Please investigate this exhaustively, and report back the findings, "
            "how it affects the rest of the theorem, and how to mitigate it if it does, or determine if it applies "
            "at all")


def load_mods():
    spec = importlib.util.spec_from_file_location("m5_growth5", G5)
    g5 = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(G5))
    spec.loader.exec_module(g5)
    return g5, g5.H


# ---------------------------------------------------------------- the slice and theta_k (M1)
class Slice:
    """one null slice: the scheme's fields on its grid, with Chebyshev interpolants in y per column"""
    def __init__(s, yex, Ny, Nx, fields, v=None, mu=None):
        s.yex, s.Ny, s.Nx, s.v, s.mu = yex, Ny, Nx, v, mu
        s.t = np.cos(np.pi*np.arange(Ny + 1)/Ny)                 # y = yex (1 - t)/2
        s.x = np.cos(np.pi*np.arange(Nx + 1)/Nx)
        s.Dx = cheb_D(Nx)
        s.f = {k: np.asarray(fields[k], float) for k in FIELDS}
        s.c = {k: np.polynomial.chebyshev.chebfit(s.t, s.f[k], Ny) for k in FIELDS}   # shape (Ny+1, Nx+1)

    def tt(s, Y):
        return 1 - 2*np.asarray(Y)/s.yex

    def at(s, k, Y):
        """field k at y = Y[j] on column j"""
        tt = s.tt(Y)
        return np.array([np.polynomial.chebyshev.chebval(tt[j], s.c[k][:, j]) for j in range(s.Nx + 1)])

    def theta(s, Y):
        Y = np.asarray(Y, float); x = s.x
        Yp = s.Dx @ Y; Ypp = s.Dx @ Yp
        F = {k: s.at(k, Y) for k in NEED}
        c2, s2 = (1 + x)/2, (1 - x)/2
        W = 1 + Y**3*F["w"]
        Vx = Y**5*(-2*x*F["q"] + (1 - x**2)*F["q_x"])
        Vy = 5*Y**4*(1 - x**2)*F["q"] + Y**5*(1 - x**2)*F["q_y"]
        beta, beta_y, beta_x = Y**6*F["b"], 6*Y**5*F["b"] + Y**6*F["b_y"], Y**6*F["b_x"]
        cs = c2*F["G"] + s2*F["F"]
        S = Y**3*cs/3
        S_y = Y**2*cs + Y**3*(c2*F["G_y"] + s2*F["F_y"])/3
        S_x = Y**3*((F["G"] - F["F"])/2 + c2*F["G_x"] + s2*F["F_x"])/3
        E = np.exp(2*(beta + S))
        E_y, E_x = 2*E*(beta_y + S_y), 2*E*(beta_x + S_x)
        lap = (1 - x**2)*(Y*Ypp - 2*Yp**2) - 2*x*Y*Yp
        if "lap_sign" in MUT:
            lap = -lap
        th = 1.5*Y**2*W + Vx + Yp*Vy + 8*E*lap + 8*Y*Yp*(1 - x**2)*(E_x + E_y*Yp)
        if "drop_shift" in MUT:
            th = th - Vx - Yp*Vy
        return th

    def round_theta(s):
        """the round spheres' expansion on the grid, (3/2) y^2 [W + (2/3) y^3 d_x((1 - x^2) q)] -- X10's form"""
        y = s.yex*(1 - s.t)/2
        Yg = y[:, None]*np.ones((1, s.Nx + 1)); X = s.x[None, :]*np.ones((s.Ny + 1, 1))
        W = 1 + Yg**3*s.f["w"]
        T = W + (2/3)*Yg**3*(((1 - X**2)*s.f["q"]) @ s.Dx.T)
        return 1.5*Yg**2*T


class SliceC(Slice):
    """past the core boundary each field continues by its value there: a test leaf may pass the boundary, and only its
    part in the domain is ever compared with a marginally trapped surface, which lies in the domain (M6)"""
    def tt(s, Y):
        return np.maximum(1 - 2*np.asarray(Y)/s.yex, -1.0)


def cheb_D(N):
    x = np.cos(np.pi*np.arange(N + 1)/N)
    c = np.array([2.0] + [1.0]*(N - 1) + [2.0])*(-1)**np.arange(N + 1)
    X = np.tile(x, (N + 1, 1)).T
    D = np.outer(c, 1/c)/(X - X.T + np.eye(N + 1))
    return D - np.diag(D.sum(axis=1))


def round_profile(S, ny=2000):
    """the round spheres' expansion on a fine y-grid per column: (yy, T[j, i]) and the outer zero per column"""
    T = S.round_theta()
    yy = np.linspace(0.3, S.yex, ny); tt = 1 - 2*yy/S.yex
    Tc = np.array([np.polynomial.chebyshev.chebval(tt, np.polynomial.chebyshev.chebfit(S.t, T[:, j], S.Ny))
                   for j in range(S.Nx + 1)])
    outer = []
    for j in range(S.Nx + 1):
        sg = np.sign(Tc[j]); i = np.nonzero(sg[1:] != sg[:-1])[0]
        outer.append(yy[i[0]] if len(i) else np.nan)
    return yy, Tc, np.array(outer)


def zeros_per_column(S, w_only=False):
    """count of sign changes of the round spheres' expansion along y in each column, on a fine sampling; with w_only,
    of W alone (the expansion without the angular shift's term (2/3) y^3 d_x((1 - x^2) q))"""
    y = S.yex*(1 - S.t)/2
    T = (1 + y[:, None]**3*S.f["w"]) if w_only else S.round_theta()
    tt = np.linspace(-1, 1, 4001)
    out = []
    for j in range(S.Nx + 1):
        f = np.polynomial.chebyshev.chebval(tt, np.polynomial.chebyshev.chebfit(S.t, T[:, j], S.Ny))
        out.append(int((np.sign(f[1:]) != np.sign(f[:-1])).sum()))
    return out


def newton(S, Y0, c=0.0, tol=1e-9, it=60, ymax=None, g=None):
    """collocation Newton for theta_k[Y] = c g on the scheme's x-grid (axes included); g = 1 unless given"""
    ymax = S.yex*1.0000001 if ymax is None else ymax
    c = c*(np.ones(S.Nx + 1) if g is None else np.asarray(g, float))
    Y = np.array(Y0, float)
    for _ in range(it):
        r = S.theta(Y) - c
        if not np.all(np.isfinite(r)):
            return None
        if np.max(np.abs(r)) < tol:
            return Y
        J = np.empty((len(Y), len(Y))); h = 1e-7
        for k in range(len(Y)):
            Yk = Y.copy(); Yk[k] += h
            J[:, k] = (S.theta(Yk) - c - r)/h
        try:
            dY = np.linalg.solve(J, -r)
        except np.linalg.LinAlgError:
            return None
        lam = 1.0
        while lam > 1e-4:
            Yn = Y + lam*dY
            if np.all(Yn > 0) and np.all(Yn < ymax):
                rn = S.theta(Yn) - c
                if np.all(np.isfinite(rn)) and np.max(np.abs(rn)) < np.max(np.abs(r)):
                    break
            lam /= 2
        else:
            return None
        Y = Yn
    return Y if np.max(np.abs(S.theta(Y) - c)) < tol else None


def stability(S, Y):
    """lambda_1 = -max Re eig(d theta_k/dY): > 0 for a strictly stable (outermost-type) surface"""
    h = 1e-7
    r = S.theta(Y)
    J = np.empty((len(Y), len(Y)))
    for k in range(len(Y)):
        Yk = Y.copy(); Yk[k] += h
        J[:, k] = (S.theta(Yk) - r)/h
    return float(-np.max(np.linalg.eigvals(J).real))


# ---------------------------------------------------------------- the exhaustive search by shooting (M5)
class Field2:
    """every needed field as one tensor Chebyshev interpolant in (t, x) -- the scheme's own representation"""
    def __init__(s, S):
        s.S = S
        V = lambda z, N: np.cos(np.outer(np.arccos(np.clip(z, -1, 1)), np.arange(N + 1)))
        It, Ix = np.linalg.inv(V(S.t, S.Ny)), np.linalg.inv(V(S.x, S.Nx))
        s.C = np.array([It @ S.f[k] @ Ix.T for k in NEED])

    def eval(s, Y, x):
        t = 1 - 2*np.asarray(Y)/s.S.yex
        n = np.arange(s.S.Ny + 1)
        Tt = np.cos(np.outer(np.arccos(np.clip(t, -1, 1)), n))
        out = np.abs(t) > 1
        if out.any():
            Tt[out] = np.sign(t[out])[:, None]**n*np.cosh(np.outer(np.arccosh(np.abs(t[out])), n))
        Tx = np.cos(np.arccos(np.clip(x, -1, 1))*np.arange(s.S.Nx + 1))
        return (s.C @ Tx) @ Tt.T


def parts(F2, Y, psi):
    x = -np.cos(psi); sn = np.sin(psi)
    w, q, q_x, q_y, b, b_y, b_x, G, G_y, G_x, Fm, F_y, F_x = F2.eval(Y, x)
    W = 1 + Y**3*w
    Vx = Y**5*(-2*x*q + (1 - x**2)*q_x)
    Vyt = 5*Y**4*q + Y**5*q_y
    c2, s2 = (1 + x)/2, (1 - x)/2
    cs = c2*G + s2*Fm
    Sx = Y**3*cs/3
    S_y = Y**2*cs + Y**3*(c2*G_y + s2*F_y)/3
    S_x = Y**3*((G - Fm)/2 + c2*G_x + s2*F_x)/3
    beta = Y**6*b; beta_y = 6*Y**5*b + Y**6*b_y; beta_x = Y**6*b_x
    E = np.exp(2*(beta + Sx)); E_y = 2*E*(beta_y + S_y); E_x = 2*E*(beta_x + S_x)
    return x, sn, W, Vx, Vyt, E, E_x, E_y


def _rhs(F2, psi, Y, P, c):
    """theta_k = c as Y_psipsi, x = -cos psi: 8 E Y (Y_psipsi + cot psi Y_psi) = c - (3/2) Y^2 W - V_x - ..."""
    x, sn, W, Vx, Vyt, E, E_x, E_y = parts(F2, Y, psi)
    br = c - 1.5*Y**2*W - Vx - P*sn*Vyt + 16*E*P**2 - 8*Y*P*(sn*E_x + E_y*P)
    return br/(8*E*Y) - (np.cos(psi)/sn)*P


def _axis(F2, Y, psi, c):
    x, sn, W, Vx, Vyt, E, E_x, E_y = parts(F2, Y, psi)
    return (c - 1.5*Y**2*W - Vx)/(16*E*Y)


def shoot(F2, Y0, c=0.0, n=3000, eps=2e-3, ymin=0.0, keep=False):
    """the regular solution from the axis x = -1 with Y(-1) = Y0, by RK4 on a mesh graded toward both axes; returns
    C, the singular solution's coefficient at x = +1 (zero exactly for a closed surface), and a status per shot
    (0 in the domain, +1 left into the core, -1 left outward, 2 not finite)"""
    Y0 = np.atleast_1d(np.asarray(Y0, float))
    a = _axis(F2, Y0, 0.0, c)
    Y = Y0 + 0.5*a*eps**2; P = a*eps
    tau = np.linspace(np.arccos(1 - 2*eps/np.pi), np.arccos(-1 + 2*eps/np.pi), n + 1)
    psis = np.pi*(1 - np.cos(tau))/2
    st = np.zeros(len(Y0), int)
    path = [Y.copy()] if keep else None
    for k in range(n):
        p0, p1 = psis[k], psis[k + 1]; h = p1 - p0; pm = 0.5*(p0 + p1)
        ok = st == 0
        if not ok.any():
            break
        y, pp = Y[ok], P[ok]
        k1y, k1p = pp, _rhs(F2, p0, y, pp, c)
        k2y, k2p = pp + 0.5*h*k1p, _rhs(F2, pm, y + 0.5*h*k1y, pp + 0.5*h*k1p, c)
        k3y, k3p = pp + 0.5*h*k2p, _rhs(F2, pm, y + 0.5*h*k2y, pp + 0.5*h*k2p, c)
        k4y, k4p = pp + h*k3p, _rhs(F2, p1, y + h*k3y, pp + h*k3p, c)
        Y[ok] = y + h/6*(k1y + 2*k2y + 2*k3y + k4y)
        P[ok] = pp + h/6*(k1p + 2*k2p + 2*k3p + k4p)
        bad = ~np.isfinite(Y) | ~np.isfinite(P)
        st[ok & (Y > F2.S.yex)] = 1; st[ok & (Y < ymin)] = -1; st[bad & (st == 0)] = 2
        if keep:
            path.append(Y.copy())
    pe = psis[-1]
    C = np.sin(pe)*(P - _axis(F2, Y, np.pi, c)*(pe - np.pi))
    C[st != 0] = np.nan
    return (C, st, psis, np.array(path)) if keep else (C, st)


def roots(F2, lo, hi, c=0.0, n0=600, ymin=0.0, rounds=6, tol=1e-6):
    """every closed surface theta_k = c with axis value in (lo, hi): each sign change of C, a shot that leaves the
    domain counting as +-inf on its side, refined by multisection and kept only if the refined shot stays in the domain
    with |C| < tol"""
    def ext(C, st):
        Ce = C.copy(); Ce[st == 1] = np.inf; Ce[st == -1] = -np.inf; Ce[st == 2] = np.nan
        if "no_exit_inf" in MUT:
            Ce[st != 0] = np.nan
        return Ce
    Y0 = np.linspace(lo, hi, n0)
    Ce = ext(*shoot(F2, Y0, c=c, ymin=ymin))
    br = [(Y0[i], Y0[i + 1], Ce[i], Ce[i + 1]) for i in range(n0 - 1)
          if (np.isfinite(Ce[i]) or np.isfinite(Ce[i + 1])) and not np.isnan(Ce[i]) and not np.isnan(Ce[i + 1])
          and np.sign(Ce[i]) != np.sign(Ce[i + 1])]
    for _ in range(rounds):
        if not br:
            break
        pts = np.concatenate([np.linspace(a, b, 10)[1:-1] for a, b, _, _ in br])
        ce = ext(*shoot(F2, pts, c=c, ymin=ymin))
        nb = []
        for k, (a, b, ca, cb) in enumerate(br):
            ys = np.concatenate([[a], pts[8*k:8*k + 8], [b]])
            cs = np.concatenate([[ca], ce[8*k:8*k + 8], [cb]])
            for j in range(9):
                if not np.isnan(cs[j]) and not np.isnan(cs[j + 1]) and np.sign(cs[j]) != np.sign(cs[j + 1]):
                    nb.append((ys[j], ys[j + 1], cs[j], cs[j + 1])); break
        br = nb
    good = []
    for a, b, _, _ in br:
        m = 0.5*(a + b)
        cm, sm = shoot(F2, [m], c=c, ymin=ymin)
        if sm[0] == 0 and abs(cm[0]) < tol:
            good.append(m)
    return good


def leaf_nodes(S, F2, y0, c=0.0):
    """the shot from Y(-1) = y0 sampled at the scheme's x-nodes (a Newton start)"""
    C, st, psis, path = shoot(F2, [y0], c=c, keep=True)
    return np.interp(S.x, -np.cos(psis), path[:, 0])            # x = -cos psi increases along the shot


# ---------------------------------------------------------------- the sweep (M6)
def sweep(S, Ystar, sign=-1, dc=0.05, cmax=500.0, stop_y=None, beyond=3.0, g=None):
    """closed leaves theta_k = c g continued from the outer MOTS (c = 0): inward (sign -1, c < 0, g > 0) until a leaf
    lies wholly past the core boundary, outward (sign +1) until a leaf lies wholly outside the least round zero
    (stop_y).  Each leaf must lie strictly beyond the last at every node where the last is in the domain; the step
    halves on failure down to dc/64"""
    if "leaf_sign" in MUT:
        sign = -sign
    leaves = [(0.0, Ystar.copy())]
    c, Y, h, why = 0.0, Ystar.copy(), dc, "c limit"
    while abs(c) < cmax:
        cn = c + sign*h
        guess = Y + (Y - leaves[-2][1])*(h/abs(leaves[-1][0] - leaves[-2][0])) if len(leaves) > 1 else Y
        Yn = newton(S, guess, c=cn, ymax=S.yex*beyond, g=g)
        # inward, only the leaf's part in the domain matters: deeper where the last leaf is inside, still past the
        # boundary where it was past it
        ok = Yn is not None and (np.all(np.where(Y < S.yex, Yn > Y, Yn >= S.yex)) if sign < 0 else np.all(Yn < Y))
        if not ok:
            if h > dc/64:
                h /= 2; continue
            why = "no further nested leaf" if Yn is None else "not nested"
            break
        leaves.append((cn, Yn)); c, Y = cn, Yn
        h = min(h*1.5, max(4*dc, 0.05*abs(cn)))       # steps grow with |c| (a deep core needs many units of c)
        if sign > 0 and stop_y is not None and Y.max() < stop_y:
            why = "outside every round zero"; break
        if sign < 0 and Y.min() >= S.yex:
            why = "wholly past the core boundary"; break
    return leaves, why


def fine_theta(S, F2, Yn, nfine=401):
    """theta_k of a leaf (its Chebyshev interpolant through the nodes) on a fine x-grid, the fields from the tensor
    interpolant; nan where the leaf is past the core boundary"""
    cY = np.polynomial.chebyshev.chebfit(S.x, Yn, S.Nx)
    xs = np.cos(np.linspace(0, np.pi, nfine))
    Y = np.polynomial.chebyshev.chebval(xs, cY)
    Yp = np.polynomial.chebyshev.chebval(xs, np.polynomial.chebyshev.chebder(cY))
    Ypp = np.polynomial.chebyshev.chebval(xs, np.polynomial.chebyshev.chebder(cY, 2))
    th = np.full(nfine, np.nan)
    inn = Y <= S.yex
    for i in np.nonzero(inn)[0]:
        x, y, yp, ypp = xs[i], Y[i], Yp[i], Ypp[i]
        _, _, W, Vx, Vyt, E, E_x, E_y = [np.atleast_1d(a)[0] for a in parts(F2, np.array([y]), np.arccos(-x))]
        th[i] = (1.5*y**2*W + Vx + yp*(1 - x**2)*Vyt + 8*E*((1 - x**2)*(y*ypp - 2*yp**2) - 2*x*y*yp)
                 + 8*y*yp*(1 - x**2)*(E_x + E_y*yp))
    return th


def nested_fine(S, Ya, Yb, nfine=401, domain=False):
    """least of Yb - Ya over a fine x-grid (both interpolated through the nodes); with domain, of min(Yb, yex) -
    min(Ya, yex) where Ya is inside the domain, and -inf if Yb comes back inside where Ya was past the boundary"""
    xs = np.cos(np.linspace(0, np.pi, nfine))
    A = np.polynomial.chebyshev.chebval(xs, np.polynomial.chebyshev.chebfit(S.x, Ya, S.Nx))
    B = np.polynomial.chebyshev.chebval(xs, np.polynomial.chebyshev.chebfit(S.x, Yb, S.Nx))
    if not domain:
        return float((B - A).min())
    if np.any((A >= S.yex) & (B < S.yex)):
        return -np.inf
    inn = A < S.yex
    return float((np.minimum(B, S.yex) - A)[inn].min()) if inn.any() else np.inf


def analyse(S):
    """one slice: the round picture, every T^2-invariant MOTS (M5) and the two sweeps (M6)"""
    F2 = Field2(S)
    yy, Tc, outer = round_profile(S)
    T = S.round_theta()
    trapped = yy[(Tc < 0).all(axis=0)]
    ylo = 0.5*np.nanmin(outer)
    mots = []
    for y0 in roots(F2, ylo, S.yex*0.9999, ymin=0.25*ylo):
        Ys = leaf_nodes(S, F2, y0)
        Yn = newton(S, Ys)
        if Yn is None or np.max(np.abs(Yn - Ys)) > 0.05:          # a polish that leaves the shot is not kept
            mots.append(dict(y0=float(y0), polished=False, r_min=float((Ys**-2).min()), r_max=float((Ys**-2).max())))
            continue
        mots.append(dict(y0=float(y0), polished=True, r_min=float((Yn**-2).min()), r_max=float((Yn**-2).max()),
                         lam1=stability(S, Yn), Y=Yn.tolist()))
    sw = None
    good = [m for m in mots if m["polished"]]
    if len(good) == 1:
        Ystar = np.array(good[0]["Y"])
        SC = SliceC(S.yex, S.Ny, S.Nx, S.f, v=S.v, mu=S.mu)
        g = np.maximum(1.0, -T[-1])        # inward leaves theta_k = c g: deepest where the core boundary is most trapped
        Lin, why_in = sweep(SC, Ystar, sign=-1, g=g)
        Lout, why_out = sweep(S, Ystar, sign=+1, stop_y=np.nanmin(outer))
        th_in = [np.nanmax(np.append(fine_theta(S, F2, Y), -np.inf)) for _, Y in Lin[1:]]
        th_out = [np.nanmin(np.append(fine_theta(S, F2, Y), np.inf)) for _, Y in Lout[1:]]
        sw = dict(n_in=len(Lin) - 1, c_in=Lin[-1][0], why_in=why_in,
                  pocket=int((Lin[-1][1] < S.yex).sum()),
                  th_in=float(max(th_in)) if th_in else None,
                  gap_in=min([nested_fine(S, A, B, domain=True) for (_, A), (_, B) in zip(Lin[:-1], Lin[1:])]
                             or [np.nan]),
                  n_out=len(Lout) - 1, c_out=Lout[-1][0], why_out=why_out,
                  th_out=float(min(th_out)) if th_out else None,
                  gap_out=min([nested_fine(S, B, A) for (_, A), (_, B) in zip(Lout[:-1], Lout[1:])] or [np.nan]))
        sw["unique"] = bool(why_in == "wholly past the core boundary" and why_out == "outside every round zero"
                            and sw["th_in"] is not None and sw["th_in"] < 0 and sw["gap_in"] > 0
                            and sw["th_out"] is not None and sw["th_out"] > 0 and sw["gap_out"] > 0)
    for m in mots:
        m.pop("Y", None)
    return dict(v=S.v, mu=S.mu, nz=int(max(zeros_per_column(S))), nzW=int(max(zeros_per_column(S, w_only=True))),
                Wex=float((1 + S.yex**3*S.f["w"][-1]).max()),
                Tex=float(T[-1].max()), band=[float(trapped.max()**-2), float(trapped.min()**-2)] if len(trapped)
                else None, r_core=float(S.yex**-2), mots=mots, sweep=sw)


# ---------------------------------------------------------------- slices from the scheme (M8)
def capture(name, vs, Ny=20, Nx=16):
    """run the record's scheme (growth5.run) at a point and capture the accepted slices at the steps nearest vs"""
    g5, H = load_mods()
    L, lam = POINTS[name]
    targets = sorted(vs); got = {}
    orig = H.rhs
    state = {"i": 0, "n": 0}
    def rhs(g, st, v, data, *a, **k):
        out = orig(g, st, v, data, *a, **k)
        i, n = state["i"], state["n"]
        state["n"] += 1                       # growth5.run calls rhs four times a step; the first is the accepted state
        if n % 4 == 0 and i < len(targets) and v >= targets[i] - 1e-12:
            while state["i"] < len(targets) and v >= targets[state["i"]] - 1e-12:
                state["i"] += 1
            got[round(v, 6)] = dict(fields={f: np.asarray(out[1][f]).tolist() for f in FIELDS}, yex=float(g.yex),
                                    mu=float(data.mu_pred(v)))
            if state["i"] == len(targets):
                raise ValueError("captured")
        return out
    H.rhs = rhs
    try:
        g5.run(L, lam, Ny, Nx, log=lambda *a: None)
    finally:
        H.rhs = orig
    return got


def scan(name, vs, Ny=20, Nx=16):
    got = capture(name, vs, Ny, Nx)
    return [analyse(Slice(rec["yex"], Ny, Nx, rec["fields"], v=v, mu=rec["mu"])) for v, rec in sorted(got.items())]


def summary(rows):
    """per point: slices; those with W_ex < 0 (the scheme's premise, causal clause); of those, with a second round zero,
    with a second zero of W alone, with other than one T^2-invariant MOTS, unique of any shape by the sweeps; the least
    lambda_1 there; and past the premise, the slices and those with one T^2-invariant MOTS"""
    valid = [r for r in rows if r["Wex"] < 0]
    past = [r for r in rows if r["Wex"] >= 0]
    inner = sum(1 for r in valid if len(r["mots"]) != 1) if "count_all" not in MUT else len(valid)
    return dict(n=len(rows), valid=len(valid), nz2=sum(1 for r in valid if r["nz"] > 1),
                nzW2=sum(1 for r in valid if r.get("nzW", 1) > 1), not_one=inner,
                unique_valid=sum(1 for r in valid if r["sweep"] and r["sweep"]["unique"]),
                lam1_min=round(min([m["lam1"] for r in valid for m in r["mots"] if m.get("polished")] or [0.0]), 2),
                past=len(past), past_one=sum(1 for r in past if len(r["mots"]) == 1))


# ---------------------------------------------------------------- checks
def tangherlini_slice(Ny=20, Nx=16, yex=1.3, mu=1.0):
    """Tangherlini of mass mu in the scheme's fields: w = -mu y, everything else zero"""
    t = np.cos(np.pi*np.arange(Ny + 1)/Ny); y = yex*(1 - t)/2
    f = {k: np.zeros((Ny + 1, Nx + 1)) for k in FIELDS}
    f["w"] = -mu*y[:, None]*np.ones((1, Nx + 1)); f["w_y"] = -mu*np.ones((Ny + 1, Nx + 1))
    return Slice(yex, Ny, Nx, f, v=0.0, mu=mu)


def stored_slice():
    d = json.load(open(SLICE))
    return Slice(d["yex"], d["Ny"], d["Nx"], d["fields"], v=d["v"], mu=d["mu"])


def legendre_identity():
    """u = 1/Y: Y (Lap Y) - 2 |grad Y|^2 = -u^-3 Lap u for the S^3 Laplacian on T^2-invariant functions (M4)"""
    import sympy as sp
    x = sp.symbols("x"); u = sp.Function("u")(x); Y = 1/u
    L = lambda f: 4*((1 - x**2)*sp.diff(f, x, 2) - 2*x*sp.diff(f, x))          # Lap_{S^3} on f(x), x = cos 2 th
    g2 = lambda f: 4*(1 - x**2)*sp.diff(f, x)**2                                 # |grad f|^2
    return sp.simplify(Y*L(Y) - 2*g2(Y) + L(u)/u**3) == 0


PINNED = {    # M8, the runs of 2026-10-21 (data/mots545_scans.json)
    'L100_10l5': dict(n=40, valid=21, nz2=10, nzW2=0, not_one=0, unique_valid=21,
                      lam1_min=5.89, past=19, past_one=19),
    'L1000_10l5': dict(n=29, valid=28, nz2=9, nzW2=0, not_one=0, unique_valid=27,
                       lam1_min=5.93, past=1, past_one=1),
    'copper': dict(n=51, valid=26, nz2=10, nzW2=0, not_one=0, unique_valid=26,
                   lam1_min=5.92, past=25, past_one=25),
    'example': dict(n=35, valid=17, nz2=10, nzW2=0, not_one=0, unique_valid=17,
                    lam1_min=5.9, past=18, past_one=18),
    'r0=20ell': dict(n=71, valid=71, nz2=47, nzW2=0, not_one=0, unique_valid=71,
                     lam1_min=5.7, past=0, past_one=0),
}
PIN_RES = {    # M9
    'copper_28x16': dict(n=16, valid=13, nz2=13, nzW2=0, not_one=0, unique_valid=13,
                         lam1_min=5.93, past=3, past_one=3),
    'copper_20x20': dict(n=16, valid=13, nz2=4, nzW2=0, not_one=0, unique_valid=13,
                         lam1_min=5.93, past=3, past_one=3),
}
PIN_MIT = {    # M10: the boundary's first inflow and the run's end
    'L1000_Ny20': dict(wex_first=None,
                       end='complete'),
    'L300_Ny20': dict(wex_first=1.815625,
                      end='scheme failed at v = 1.8969: LinAlgError'),
    'L500_Ny20': dict(wex_first=2.5,
                      end='scheme failed at v = 2.5021: LinAlgError'),
    'L500_Ny28': dict(wex_first=2.525316,
                      end='scheme failed at v = 2.5316: LinAlgError'),
    'L650_Ny20': dict(wex_first=2.181667,
                      end='scheme failed at v = 2.1967: LinAlgError'),
    'L650_Ny28': dict(wex_first=2.193686,
                      end='scheme failed at v = 2.2056: LinAlgError'),
    'L750_Ny20': dict(wex_first=2.13244,
                      end='scheme failed at v = 2.1354: LinAlgError'),
}


def load(path=DATA):
    return json.load(open(path)) if os.path.exists(path) else {}


def checks(fast=False):
    ok = {}
    ok["M0 M's words, 545"] = words().startswith("Does 519 cover this?")
    T = tangherlini_slice()
    sol = analyse(T)
    ok["M4 Tangherlini: the exhaustive search finds one MOTS, r = sqrt(mu) = 1, strictly stable"] = (
        len(sol["mots"]) == 1 and abs(sol["mots"][0]["r_min"] - 1) < 1e-6 and abs(sol["mots"][0]["r_max"] - 1) < 1e-6
        and sol["mots"][0]["lam1"] > 1)
    ok["M4 Tangherlini: the sweeps leave no room for a MOTS of any shape but it"] = bool(
        sol["sweep"] and sol["sweep"]["unique"])
    ok["M4 the identity behind uniqueness on Tangherlini's null slices for every shape (sympy)"] = legendre_identity()
    S = stored_slice()
    jj = 12
    yk = S.yex*(1 - S.t[jj])/2
    rt = S.round_theta()[jj]
    ok["M1 on the record's slice (copper, v = %.3f): theta_k of a round sphere is X10's round expansion in every "
       "column, to the x-grid's aliasing" % S.v] = bool(
        np.max(np.abs(S.theta(np.full(S.Nx + 1, yk)) - rt)) < 1e-4*max(1.0, np.abs(rt).max()))
    if not fast:
        a = analyse(S)
        ok["M5-M6 on the record's slice (copper, v = %.3f, %d round zeros in a column): one MOTS, unique by the "
           "sweeps" % (S.v, a["nz"])] = (len(a["mots"]) == 1 and a["mots"][0]["lam1"] > 1 and a["nz"] >= 2
                                         and bool(a["sweep"] and a["sweep"]["unique"]))
    R = load()
    if PINNED:
        ok["M8 the five points' scans read back as pinned"] = all(
            k in R and summary(R[k]) == pin for k, pin in PINNED.items())
        S5 = [summary(R[k]) for k in PINNED if k in R]
        val = sum(a["valid"] for a in S5)
        ok["M8 on all %d slices with the core boundary outflow: one marginally trapped surface, W alone one zero per "
           "column on all %d that show a second round zero" % (val, sum(a["nz2"] for a in S5))] = (
            len(S5) == 5 and all(a["not_one"] == 0 and a["nzW2"] == 0 for a in S5) and val == 163)
        ok["M8 unique of any shape by the sweeps on 162 of the 163; on the 63 slices past the premise one each"] = (
            sum(a["unique_valid"] for a in S5) == 162 and sum(a["past"] for a in S5) == 63
            and sum(a["past_one"] for a in S5) == 63 and min(a["lam1_min"] for a in S5) > 5)
    if PIN_RES:
        ok["M9 the resolution scans read back as pinned"] = all(
            k in R and summary(R[k]) == pin for k, pin in PIN_RES.items())
        if all(k in R for k in ("copper", "copper_28x16", "copper_20x20")):
            def near(rows, v):
                return min(rows, key=lambda a: abs(a["v"] - v))
            d20 = max(abs(near(R["copper"], a["v"])["mots"][0][f] - a["mots"][0][f])
                      for a in R["copper_20x20"] for f in ("r_min", "r_max"))
            d28 = max(abs(near(R["copper"], a["v"])["mots"][0][f] - a["mots"][0][f])
                      for a in R["copper_28x16"] for f in ("r_min", "r_max"))
            ok["M9 the outer surface's radii: Nx 20 against Nx 16 within 1e-3, Ny 28 against Ny 20 within 5e-3"] = (
                d20 < 1e-3 and d28 < 5e-3)
    if PIN_MIT:
        Mt = load(MITIG)
        ok["M10 the mitigation runs read back as pinned"] = all(
            k in Mt and {kk: Mt[k][kk] for kk in pin} == pin for k, pin in PIN_MIT.items())
        dg = load(os.path.join(HERE, "data", "derived_go_runs.json"))
        r0w = [max(st[5] for st in dg[k]["steps"]) for k in ("r0=20ell_20x16", "r0=20ell_28x16") if k in dg]
        ok["M10 at lam_P: every seed up to 750 l5^2 turns the core boundary inflow inside the shell; 808.5 (both "
           "grids) and 1000 never"] = (
            all(d["wex_first"] is not None and d["wex_first"] < 3.5 for d in Mt.values() if d["L"] <= 750)
            and Mt.get("L1000_Ny20", {}).get("wex_first", 0) is None and len(r0w) == 2 and max(r0w) < 0)
    return ok


def selftest(quiet=False, fast=False):
    ck = checks(fast=fast)
    for k, v in ck.items():
        if not quiet:
            print("[%s] %s" % ("ok" if v else "FAIL", k))
    good = all(ck.values())
    if not quiet:
        print("mots545.py: %d/%d %s" % (sum(ck.values()), len(ck), "pass" if good else "FAIL"))
    return good


def mutants():
    names = ("lap_sign", "drop_shift", "leaf_sign", "count_all")
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        bad = not selftest(quiet=True, fast=(m != "leaf_sign"))
        caught += bad
        print("mutant %-10s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


def report():
    R = load()
    for k, rows in R.items():
        print(k, summary(rows))


if __name__ == "__main__":
    if "--scan" in sys.argv:
        i = sys.argv.index("--scan")
        name = sys.argv[i + 1]; v0, v1, dv = map(float, sys.argv[i + 2:i + 5])
        Ny = int(sys.argv[i + 5]) if len(sys.argv) > i + 5 else 20
        Nx = int(sys.argv[i + 6]) if len(sys.argv) > i + 6 else 16
        rows = scan(name, list(np.round(np.arange(v0, v1 + 1e-9, dv), 6)), Ny, Nx)
        key = name if (Ny, Nx) == (20, 16) else "%s_%dx%d" % (name, Ny, Nx)
        R = load(); R[key] = rows
        json.dump(R, open(DATA, "w"), separators=(",", ":"))
        print(key, summary(rows))
    elif "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    elif "--report" in sys.argv:
        report()
    else:
        sys.exit(0 if selftest() else 1)
