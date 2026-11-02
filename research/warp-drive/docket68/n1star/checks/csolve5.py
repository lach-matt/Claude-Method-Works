#!/usr/bin/env python3
"""csolve5.py -- C7: the constraint solve's lam^(N-2) scaling (supplement Lemmas 6.3-6.4, Proposition 6.5), computed.

The operator is data5.py's constraint map (rho, J_r, J_th) of Psi(U) = (gamma + a dr dr, K + w Pi + q dr + dr q) at the
data on Sigma of the stage-0 approximant g0 + lam (W_TT + chi dv^2), expanded to second order in U: its linear part L
and its quadratic part Q, each a lam-series whose coefficients are exact sympy expressions in (r, th, v, s).

  C7a (exact) Neither L nor Q has a coefficient of order 1/lam (data5.py S2/S4 showed it for L; Q is new: the 1/lam
      second derivatives of gamma enter only through the trace of W on the spheres at every order in a). So the
      quadratic remainder Nl of Proposition 6.5's proof has coefficients O(1) at this approximant, not merely O(1/lam).
      Control: the trace_W mutant (an oscillating trace in place of W_TT) has a 1/lam coefficient in both.
  C7b (numerical, floating point) The linear solve of Lemma 6.4: concrete mu, E, H (below), A = 1, tau0 = 0; on S^3's
      symmetric class a pseudo-spectral collocation (a, w in cos 2k th, q in sin 2k th, k < M), the system M1 d_r U +
      M0 U = F marched by the implicit midpoint rule from zero data at r = a = 1 to r = 3 with lam/32 steps; F a source
      of size lam^(N-2), N = 6, carrying a phase mean and two harmonics, supported on the shell 1.25 < r < 2.75. The
      measured rates of sup_r ||d_r^j U||_(H^2) over lam = 1/8, ..., 1/64 are lam^(N-2), lam^(N-2), lam^(N-3) for j =
      0, 1, 2: within Proposition 6.5's lam^(N-2-j), the first r-derivative costing nothing, as the absence of a 1/lam
      coefficient implies. Control: the trace_W mutant's 1/lam coefficient (with zero phase mean, so sup ||U|| still
      scales as lam^(N-2)) makes the first r-derivative cost lam^-1. Resolution: M = 12, 16, 20 and lam/32, lam/64 steps.
  C7c (numerical) The nonlinear solve, by Proposition 6.5's scheme: U_(i+1) solves the linear system whose principal
      coefficients (of d_r a, d_r d_th a, d_th^2 a in rho; of d_r w, d_r q, d_th w, d_th q, d_r a, d_r d_th a in J) are
      frozen at U_i, the remaining quadratic terms evaluated at U_i as a source. The iterates converge, and the
      nonlinear correction relative to U, the contraction factor of the scheme, scales as lam^(N-2): the proof's bound C
      lam^(N-3) allows a 1/lam coefficient in Nl, which C7a shows absent here. Control: the trace_W mutant, whose Q has
      a 1/lam coefficient, contracts at the proof's rate lam^(N-3) only.

Not reached: the approximant's higher stages (g_j, j >= 1, the means and the phase corrections; Lemma 6.3(b) gives them
O(1) coefficients) and the O(lam) coefficients (data5.py truncates its series at lam^1, so only the orders -1 and 0
are complete); the norms are the computed ones at one resolution set, not bounds. Equivalent H^2 norm: coefficients in
cos 2k th (sin 2k th for q) weighted by (1 + l (l + 2)), l = 2k.

Run: python3 checks/csolve5.py   (about fifty minutes, most of it the sympy build of L and Q; saved as
     checks/csolve5.out)
"""
import os
import sys
import time

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import data5 as d5                                                               # noqa: E402

NN = 6                                   # the approximant's stage count N; the residual is O(lam^(N-2))
P = NN - 2
LAMS = [1/8, 1/16, 1/32, 1/64]
V0, V1, RA, RB = 1.25, 2.75, 1.0, 3.0
MU0, DMU = sp.Rational(1, 2), sp.Rational(1, 20)
x_ = sp.Symbol("x_")
_u = (x_ - V0)/(V1 - V0)
BUMP = sp.Piecewise((((x_ - V0)*(V1 - x_)/((V1 - V0)/2)**2)**5, (x_ > V0) & (x_ < V1)), (0, True))
FUN = {d5.mu.func: sp.Lambda(x_, MU0 - DMU*sp.Piecewise((0, x_ <= V0), (1, x_ >= V1),
                                                        (_u**3*(10 - 15*_u + 6*_u**2), True))),
       d5.Ef.func: sp.Lambda(x_, BUMP),                            # E = bump on (V0, V1), C^4
       d5.Hf.func: sp.Lambda(x_, 1 + sp.cos(2*x_)/2)}              # H smooth on S^3 (a function of cos 2 th)
_MEMO = {}


# --- the operator: data5.py's constraint map at Psi(eps U), its eps^1 and eps^2 parts ----------------------------

def build(mutant=None):
    d5.MUT.clear()
    if mutant:
        d5.MUT.add(mutant)
    gam, gi, K = d5.slice_data(True, mutant is None)
    eps = d5.eps
    h = sp.zeros(4)
    h[0, 0] = d5.af
    Q = sp.zeros(4)
    for i in (1, 2, 3):
        Q[i, i] = d5.wf*gam[i, i]
    Q[0, 1] = Q[1, 0] = d5.qf
    gpi = sp.zeros(4)
    for i in range(4):
        for j in range(4):
            e1 = sum(gi[i, k]*h[k, l]*gi[l, j] for k in range(4) for l in range(4))
            e2 = sum(gi[i, k]*h[k, l]*gi[l, m]*h[m, n]*gi[n, j] for k in range(4) for l in range(4)
                     for m in range(4) for n in range(4))
            gpi[i, j] = d5.trunc(sp.expand(gi[i, j] - eps*e1 + eps**2*e2), 1)   # (gamma + eps h)^-1 to eps^2
    J, rho = d5.constraints(gam + eps*h, gpi, K + eps*Q)
    out = []
    for x in J + [rho]:
        x = sp.expand(x)
        out.append((sp.expand(sp.diff(x, eps).subs(eps, 0)), sp.expand(sp.diff(x, eps, 2).subs(eps, 0)/2)))
    d5.MUT.clear()
    return out


_, SYM = d5.jet(sp.Integer(0))
JETS = set(SYM.values())


def split(x, deg):
    """{jets: coefficient} of a polynomial of degree deg in the jets of (a, w, q)"""
    x = x.xreplace(SYM)
    if any(dd.expr in (d5.af, d5.wf, d5.qf) for dd in x.atoms(sp.Derivative)) or \
            any(f in (d5.af, d5.wf, d5.qf) for f in x.atoms(sp.Function)):
        raise ValueError("a jet was not replaced")
    out = {}
    for term in sp.Add.make_args(x):
        js, rest = [], []
        for f in sp.Mul.make_args(term):
            b, p = f.as_base_exp()
            if b in JETS:
                js += [b]*int(p)
            else:
                rest.append(f)
        if len(js) != deg:
            raise ValueError("a term of degree %d in U" % len(js))
        key = tuple(sorted(js, key=str))
        out[key] = out.get(key, 0) + sp.Mul(*rest)
    return out


def table(res):
    """T[eq][k] = [linear {jets: c}, quadratic {jets: c}], k the lam order; eq = J_r, J_th, rho"""
    T = []
    for lin, quad in res:
        row = {}
        for part, deg in ((lin, 1), (quad, 2)):
            for k, c in d5.orders(part).items():
                row.setdefault(k, [{}, {}])[deg - 1] = split(sp.expand(c), deg)
        T.append(row)
    return T


def operator(mutant=None):
    """the coefficient table, built once per run (the approximant's takes about twenty minutes)"""
    if mutant not in _MEMO:
        _MEMO[mutant] = table(build(mutant))
    return _MEMO[mutant]


# --- the discretisation --------------------------------------------------------------------------------------------

def concrete(c):
    x = c
    for f_, l_ in FUN.items():
        x = x.subs(f_, l_)
    x = x.doit().subs({d5.v: d5.r, d5.A: 1})                        # on Sigma, tau0 = 0: v = r, s = r/lam
    return sp.lambdify((d5.r, d5.th, d5.s), x, "numpy")


def grid(M):
    th = (np.arange(M) + 0.5)*np.pi/(2*M)
    k = np.arange(M)
    Ce, So = np.cos(2*np.outer(th, k)), np.sin(2*np.outer(th, k + 1))
    Ie, Io = np.linalg.inv(Ce), np.linalg.inv(So)
    return th, dict(Ie=Ie, Io=Io, k=k,
                    De=[np.eye(M), (-2*k*np.sin(2*np.outer(th, k))) @ Ie, (-4*k**2*Ce) @ Ie],
                    Do=[np.eye(M), (2*(k + 1)*np.cos(2*np.outer(th, k + 1))) @ Io, (-4*(k + 1)**2*So) @ Io])


def hnorm(X, G, M):
    k = G["k"]
    we, wo = 1 + 2*k*(2*k + 2), 1 + 2*(k + 1)*(2*(k + 1) + 2)
    return (np.linalg.norm(we*(G["Ie"] @ X[:M])) + np.linalg.norm(we*(G["Ie"] @ X[M:2*M]))
            + np.linalg.norm(wo*(G["Io"] @ X[2*M:])))


FIELD = {"a": (0, "De"), "w": (1, "De"), "q": (2, "Do")}
PRINC = [{"w_r", "w_t", "q_r", "q_t", "a_r", "a_rt"}]*2 + [{"a_r", "a_rt", "a_tt"}]


class System:
    """M1(r) d_r U + M0(r) U (+ the frozen quadratic terms) = F on the collocation grid"""

    def __init__(self, T, M):
        self.M = M
        self.th, self.G = grid(M)
        self.lin, self.quad, self.neg = [], [], 0
        for row in T:
            L, Q = {}, {}
            for k, (ld, qd) in row.items():
                if k > 0:
                    continue                            # orders above 0 are incomplete in data5.py's truncation
                self.neg += (k < 0)*(len(ld) + len(qd))
                for key, c in ld.items():
                    L.setdefault(key, []).append((k, concrete(c)))
                for key, c in qd.items():
                    Q.setdefault(key, []).append((k, concrete(c)))
            self.lin.append({key: (self.op(key[0]), fs) for key, fs in L.items()})
            self.quad.append({key: ([self.op(j) for j in key], fs) for key, fs in Q.items()})

    def op(self, js):
        f, _, der = str(js).partition("_")
        i, D = FIELD[f]
        if der.count("r") > 1:
            raise ValueError("a second r-derivative: %s" % js)
        P_ = np.zeros((self.M, 3*self.M))
        P_[:, i*self.M:(i + 1)*self.M] = self.G[D][der.count("t")]
        return der.count("r"), P_

    def cval(self, fs, r, lam):
        return sum(lam**k*np.broadcast_to(f(r, self.th, r/lam), self.th.shape) for k, f in fs)

    def matrices(self, r, lam, prev=None):
        M = self.M
        M1, M0, src = np.zeros((3*M, 3*M)), np.zeros((3*M, 3*M)), np.zeros(3*M)
        for e in range(3):
            rows = slice(e*M, (e + 1)*M)
            for key, ((on, P_), fs) in self.lin[e].items():
                (M1 if on else M0)[rows] += self.cval(fs, r, lam)[:, None]*P_
            if prev is None:
                continue
            Xi, Xri = prev
            for key, (ops, fs) in self.quad[e].items():
                c = self.cval(fs, r, lam)
                vals = [P_ @ (Xri if on else Xi) for on, P_ in ops]
                pi = [i for i in range(2) if str(key[i]) in PRINC[e]]
                if pi:                                  # a principal factor: frozen coefficient times U_(i+1)
                    on, P_ = ops[pi[0]]
                    (M1 if on else M0)[rows] += (c*vals[1 - pi[0]])[:, None]*P_
                else:                                   # the rest: a source at U_i
                    src[rows] += c*vals[0]*vals[1]
        return M1, M0, src

    def forcing(self, r, lam):
        b = float(FUN[d5.Ef.func](sp.Float(r))) if V0 < r < V1 else 0.0
        osc = 1 + np.cos(r/lam) + 0.5*np.sin(2*r/lam)
        return lam**P*np.concatenate([np.cos(2*self.th), np.sin(2*self.th), 1 + np.cos(2*self.th)/3])*b*osc

    def march(self, lam, per=32, prev=None):
        """implicit midpoint from zero data at r = RA; returns U and d_r U at the step midpoints, and the step"""
        n = int(np.ceil((RB - RA)*per/lam))
        h = (RB - RA)/n
        X = np.zeros(3*self.M)
        Xm, Xrm = [], []
        for i in range(n):
            rm = RA + (i + 0.5)*h
            M1, M0, src = self.matrices(rm, lam, None if prev is None else (prev[0][i], prev[1][i]))
            X1 = np.linalg.solve(M1/h + M0/2, self.forcing(rm, lam) - src + (M1/h - M0/2) @ X)
            Xm.append((X + X1)/2)
            Xrm.append((X1 - X)/h)
            X = X1
        return np.array(Xm), np.array(Xrm), h

    def norms(self, Xm, Xrm, h):
        Xrr = np.diff(Xrm, axis=0)/h
        return tuple(max(hnorm(x, self.G, self.M) for x in Y) for Y in (Xm, Xrm, Xrr))


def slopes(vals, lams=LAMS):
    return [np.log(vals[i + 1]/vals[i])/np.log(lams[i + 1]/lams[i]) for i in range(len(vals) - 1)]


# --- the checks ----------------------------------------------------------------------------------------------------

def c7a(control=False):
    T = operator("trace_W" if control else None)
    neg = {(nm, k, deg): len(row[k][deg]) for nm, row in zip(("J_r", "J_th", "rho"), T)
           for k in row if k < 0 for deg in (0, 1) if row[k][deg]}
    if control:
        return not neg
    print("  C7a: orders of lam in L and Q at the stage-0 approximant's data (W_TT and chi): %s; terms of order < 0:"
          " %s" % (sorted({k for row in T for k in row}), neg or "none"), flush=True)
    return not neg


def sweep(T, M=12, per=32, label=""):
    S = System(T, M)
    rows = []
    for lam in LAMS:
        t0 = time.time()
        Xm, Xrm, h = S.march(lam, per)
        rows.append(S.norms(Xm, Xrm, h))
        print("    %s lam = 1/%d: sup ||U|| %.3e, sup ||d_r U|| %.3e, sup ||d_r^2 U|| %.3e [%.0fs]"
              % (label, round(1/lam), rows[-1][0], rows[-1][1], rows[-1][2], time.time() - t0), flush=True)
    sl = [slopes([r_[j] for r_ in rows]) for j in range(3)]
    print("    %s rates (successive halvings): %s" % (label, "; ".join(
        "j = %d: %s" % (j, " ".join("%.2f" % x for x in sl[j])) for j in range(3))), flush=True)
    return S, rows, sl


def c7b(control=False):
    T = operator("trace_W" if control else None)
    S, rows, sl = sweep(T, label="mutant" if control else "")
    last = [s_[-1] for s_ in sl]                                    # the rate over the last halving, 1/32 -> 1/64
    bound = all(last[j] >= P - j - 0.1 for j in range(3))          # Proposition 6.5: lam^(N-2-j)
    free = abs(last[0] - P) < 0.1 and abs(last[1] - P) < 0.1 and abs(last[2] - (P - 1)) < 0.1
    if control:
        return free
    res = []
    for M, per in ((16, 32), (20, 32), (12, 64)):
        S2 = System(T, M)
        Xm, Xrm, h = S2.march(1/32, per)
        res.append((M, per, S2.norms(Xm, Xrm, h)))
    ref = rows[2]
    dev = max(abs(n_[j]/ref[j] - 1) for _, _, n_ in res for j in range(3))
    print("  C7b: rates over 1/32 -> 1/64 (%.2f, %.2f, %.2f) for j = 0, 1, 2: Proposition 6.5's lam^(N-2-j) = (%d, %d,"
          " %d) holds: %s; the first r-derivative free, rates (N-2, N-2, N-3): %s; at lam = 1/32 the norms move by at"
          " most %.1e between M = 12, 16, 20 and lam/32, lam/64 steps" % (tuple(last) + (P, P - 1, P - 2, bound, free,
                                                                              dev)), flush=True)
    return bound and free and dev < 1e-2


def c7c(control=False):
    S = System(operator("trace_W" if control else None), 12)
    rel, sizes, conv = [], [], []
    for lam in LAMS[:3]:
        Xm, Xrm, h = S.march(lam)
        prev, diffs = (Xm, Xrm), []
        for i in range(8):
            Xm2, Xrm2, h = S.march(lam, prev=prev)
            diffs.append(max(hnorm(a_ - b_, S.G, S.M) for a_, b_ in zip(Xm2, prev[0])))
            prev = (Xm2, Xrm2)
            if diffs[-1] < 1e-13*max(hnorm(x, S.G, S.M) for x in Xm2):
                break
        u = max(hnorm(x, S.G, S.M) for x in prev[0])
        rel.append(diffs[0]/u)
        sizes.append(u)
        conv.append(diffs[1] < 1e-2*diffs[0])
        print("    %slam = 1/%d: sup ||U|| %.3e; ||U_(i+1) - U_i|| %s" % ("mutant " if control else "", round(1/lam), u,
                                                                   " ".join("%.1e" % d for d in diffs)), flush=True)
    sr, su = slopes(rel, LAMS[:3]), slopes(sizes, LAMS[:3])
    sharp = abs(sr[-1] - P) < 0.15                                  # Nl with O(1) coefficients: lam^(N-2)
    print("  C7c%s: the nonlinear correction relative to U (the scheme's contraction factor) %s, rates %s (the proof's"
          " bound: >= N - 3 = %d; with C7a, N - 2 = %d: %s); sup ||U|| rates %s; each iterate's change below 1e-2 of the"
          " last: %s" % (" (control)" if control else "", " ".join("%.1e" % x for x in rel),
                         " ".join("%.2f" % x for x in sr), P - 1, P, sharp, " ".join("%.2f" % x for x in su), all(conv)),
          flush=True)
    if control:
        return sharp
    return all(conv) and sharp and sr[-1] >= P - 1 - 0.1 and abs(su[-1] - P) < 0.1


CHECKS = [("C7a", c7a), ("C7b", c7b), ("C7c", c7c)]


def main():
    ok = True
    for name, f in CHECKS:
        t0 = time.time()
        good = f()
        ctl = f(control=True)
        print("%s %s%s [%.0fs]" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else "",
                                   time.time() - t0), flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
