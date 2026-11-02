#!/usr/bin/env python3
"""stage5b.py -- three of the steps stage5.py leaves deduced, computed: paper/RESPONSE-HL-5D.md section 4 ("Higher
stages"), supplement N1STAR-PROOF.md 5.2-5.4 and 9.5. Same gauge, coordinates and background as stage5.py (lead5.py:
Ric^H relative to g0 in ingoing Eddington-Finkelstein coordinates (v, r, th, phi1, phi2), ell = g0^-1 dv = d_r).

Engine. `ricci` below is stage5's `series` reorganised as a series in (lam, tags): every quantity is a dict
{(k, tag): coefficient of lam^k}, tag '' for the background and one tag per new unknown, products of two tagged
factors dropped. The program asserts, rather than assumes, what makes the truncation exact: every factor of a product
has no negative power, every tagged g^-1, D g, Gamma, D^rho starts at lam^kt0, and every dropped product of two tagged
factors lies above the cut. The background is kept only to the order a tagged output can reach. Checked in B2 against
lead5 (R^(-1) = 0, R^(0) = lead5's R^(0)[W] - (1/2) e1 d_s^2 W, stage5 S1 (b)) and against stage5 S1 (c) at lam^1.

  B1 (exact; docstring (b) of stage5) The seven components outside the eight T^2 x Z2 x Z2-invariant ones vanish
     identically. Metric g0 + h, h generic in the eight invariant components (functions of (v, r, th, s)); phase
     u = v + psi(v, r, th) generic; the two-scale derivative D_a = d_a + lam^-1 (d_a u) d_s exactly, lam symbolic and
     not expanded, g^-1 by the block adjugate. Computed: Ric, the gauge term and Ric^H in the seven components
     (v phi_i, r phi_i, th phi_i, phi1 phi2): all zero, to every order in lam at once; and none of the fifteen
     contains phi1 or phi2 (T^2). Control: g0 + f dv dphi1, f generic: a non-invariant component is nonzero (the
     coefficient of d_th^2 f in Ric^H_(v phi1) is simplified and nonzero).
  B2 (exact; (a) and (d)) Lemmas 5.1-5.3 at m = 2. G = g0 + lam (W + m1) + lam^2 (g2 + m2) + lam^3 (g3 + m3)
     + lam^4 g4, u = v + lam phi1 + lam^2 phi2 + lam^3 phi3. Generic: W = lead5's W_TT + chi dv^2 with chi a generic
     function of (v, r, th, s); m1, m2, m3 generic functions of (v, r, th) and g2, g3, g4 of (v, r, th, s), each in
     the eight invariant components (B1 is what makes that restriction exact); phi1, phi2, phi3 generic functions of
     (v, r, th); M(v), E(v), H(th) generic. Restricted: the eight components; terms of degree >= 2 in the stage-2 and
     stage-3 unknowns (exact at lam^2, asserted). No harmonic or angular restriction was needed. Computed in R^(2):
     g4 absent; m3, phi3 only in -(1/2)(2 ell.d phi3 - m3(ell, ell)) d_s^2 W (e3's linear part); g3 only as
     -(ell.d) d_s g3 - (1/2) e1 d_s^2 g3 plus terms with no X-derivative of g3 and at most one d_s (Lemma 5.2), with
     no g2 in its coefficients; second derivatives of m2 only as -(1/2) box~ m2, none higher; second derivatives of
     phi2 only as -(1/2)(box~ phi2) d_s W, none higher. Control: the non-null phase u = v + r/3 + ..., as stage5 S1.
  B3 (exact; (c)) m1 from past null infinity. (i) The linearisation of Ric^H at g0 (the wave operator -1/2 box~ +
     lower order of m1's equation) on the T^2-invariant scalar-type sector of a harmonic Y_k = P_k(cos 2th) of S^3
     (eigenvalue -4k(k+1)): m = Y (f_vv dv^2 + 2 f_vr dv dr + f_rr dr^2) + 2 Y' (f_v dv + f_r dr) dth
     + r^2 (H_L Y gamma + H_T nabla nabla Y), seven functions of (v, r). Computed with Y abstract (Y'' from the
     harmonic equation, k symbolic): the sector is closed, the 1+1 system is printed by its size. sigma^* = (-1)^k on
     the sector (k = 1, 2, 3 with P_k). (ii) S3's source, -4 A^2 E^2 h^2 sin 2th / (9 r^3) dv dth with h(cos^2 2th),
     is d_th Z dv dth with Z odd in x = cos 2th, so it lies in the odd-k sectors only: for constant h, k = 1 alone
     (sin 2th = -(1/2) d_th P_1), for the record's H every odd k (the Legendre coefficients k <= 7 computed, the even
     ones zero). (iii) An exact solution of the reduced 1+1 system with the k = 1 source (constant h) is sought as a
     Laurent polynomial in r with coefficients functions of v; what is found is printed. (iv) The whole m1-linear part
     of <R^(1)[g0 + lam (W + m1)]> (stage5's W, chi with no radiation at past null infinity, S3), coefficients of every
     derivative of the generic m1: sigma-equivariant, coefficient by coefficient. Controls: the k = 2 sector (even)
     and, for (iv), one quadrature (the sin s term of W_TT removed), which must break the equivariance.

Labels: computed (exact, sympy). Run: python3 checks/stage5b.py [B1 B2 B3]   (the record's .out is a full run)
"""
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import lead5 as L                                                               # noqa: E402
import stage5 as S5                                                             # noqa: E402

lam, s, X, v, r, th = L.lam, L.s, L.X, L.v, L.r, L.th
COMP, zero, sym, second = S5.COMP, S5.zero, S5.sym, S5.second
N = 5
PAIRS = [(b, c) for b in range(N) for c in range(b, N)]
NONINV = [k for k in PAIRS if k not in COMP]


# ------------------------------------------------------------------------------------------------- the series engine
class Engine:
    """Ric^H of G in the two-scale form, as series in lam and tags (degree <= 1 in the tags)"""

    def __init__(self, G, UC, k0, kt, kt0, linear=False):
        self.UC, self.k0, self.kt, self.kt0, self.linear = UC, k0, kt, kt0, linear
        self.G = G

    def cut(self, d, k0=None, kt=None):
        k0 = self.k0 if k0 is None else k0
        kt = self.kt if kt is None else kt
        out = {}
        for (k, t), x in d.items():
            if k <= (kt if t else k0):
                x = sp.expand(x)
                if x != 0:
                    out[(k, t)] = x
        return out

    def floor(self, d, what):
        for (k, t) in d:
            assert k >= 0, "%s has lam^%d" % (what, k)
            assert not t or k >= self.kt0, "%s tagged %s at lam^%d" % (what, t, k)

    def pair(self, ka, ta, kb, tb, kt):
        if ta and tb:
            assert self.linear or ka + kb > kt, "a product of two tagged factors below the cut"
            return None
        return ta or tb

    def mul(self, A, B, acc, k0, kt):
        for (ka, ta), ea in A.items():
            for (kb, tb), eb in B.items():
                t = self.pair(ka, ta, kb, tb, kt)
                if t is None or ka + kb > (kt if t else k0):
                    continue
                key = (ka + kb, t)
                acc[key] = acc.get(key, 0) + ea*eb

    def D(self, e, a, k0, kt):
        out = {}
        for (k, t), x in e.items():
            out[(k, t)] = out.get((k, t), 0) + sp.diff(x, X[a])
            xs = sp.diff(x, s)
            if xs == 0:
                continue
            for (j, tj), c in self.UC[a].items():
                tt = self.pair(k, t, j, tj, kt)
                if tt is None:
                    continue
                out[(k + j, tt)] = out.get((k + j, tt), 0) + c*xs
        return self.cut(out, k0, kt)

    def run(self, comps, ok0, okt):
        g0, g0i = L.background()
        G = self.G
        H = [[{key: x for key, x in G[a][b].items() if key != (0, '')} for b in range(N)] for a in range(N)]
        c0 = lambda M: [[{(0, ''): M[a, b]} if M[a, b] != 0 else {} for b in range(N)] for a in range(N)]
        gi, term = c0(g0i), c0(g0i)
        for _ in range(self.kt + 1):
            new = []
            for a in range(N):
                row = []
                for b in range(N):
                    acc = {}
                    for c in range(N):
                        for d in range(N):
                            if g0i[d, b] != 0:
                                self.mul(self.mul_one(term[a][c], H[c][d]), {(0, ''): -g0i[d, b]}, acc, self.k0,
                                         self.kt)
                    row.append(self.cut(acc))
                new.append(row)
            term = new
            gi = [[self.cut({k: gi[a][b].get(k, 0) + term[a][b].get(k, 0) for k in set(gi[a][b]) | set(term[a][b])})
                   for b in range(N)] for a in range(N)]
        for a in range(N):
            for b in range(N):
                self.floor({k: x for k, x in gi[a][b].items()}, "g^-1")
        Dg = {(k, a, b): self.D(G[a][b], k, self.k0, self.kt) for k in range(N) for (a, b) in PAIRS}
        dg = lambda k, a, b: Dg[(k, min(a, b), max(a, b))]
        for x in Dg.values():
            self.floor(x, "D g")
        comb = {}
        for d in range(N):
            for (b, c) in PAIRS:
                e = {}
                for part, sg in ((dg(b, d, c), 1), (dg(c, d, b), 1), (dg(d, b, c), -1)):
                    for key, x in part.items():
                        e[key] = e.get(key, 0) + sg*x/2
                comb[(d, b, c)] = self.cut(e)
        Gam = {}
        for a in range(N):
            for (b, c) in PAIRS:
                acc = {}
                for d in range(N):
                    self.mul(gi[a][d], comb[(d, b, c)], acc, self.k0, self.kt)
                Gam[(a, b, c)] = Gam[(a, c, b)] = self.cut(acc)
                self.floor(Gam[(a, b, c)], "Gamma")
        Gh = L.christoffel(g0, g0i, lambda e, k: sp.diff(e, X[k]))
        Dv = []
        for p in range(N):
            acc = {}
            for a in range(N):
                for b in range(N):
                    diff = dict(Gam[(p, a, b)])
                    if Gh[p][a][b] != 0:
                        diff[(0, '')] = diff.get((0, ''), 0) - Gh[p][a][b]
                    self.mul(gi[a][b], self.cut(diff), acc, self.k0, self.kt)
            Dv.append(self.cut(acc))
            self.floor(Dv[-1], "D^rho")
        T = [self.cut({key: sum(Gam[(a, a, d)].get(key, 0) for a in range(N))
                       for a in range(N) for key in Gam[(a, a, d)]}) for d in range(N)]
        DDv = {(p, c): self.D(Dv[p], c, ok0, okt) for p in range(N) for c in range(N)}
        out = {}
        for (b, c) in comps:
            acc = {}
            add = lambda d, sg: [acc.__setitem__(key, acc.get(key, 0) + sg*x) for key, x in d.items()]
            for a in range(N):
                add(self.D(Gam[(a, b, c)], a, ok0, okt), 1)
            add(self.D(T[b], c, ok0, okt), -1)
            for d in range(N):
                self.mul(T[d], Gam[(d, b, c)], acc, ok0, okt)
                for a in range(N):
                    pr = {}
                    self.mul(Gam[(a, c, d)], Gam[(d, b, a)], pr, ok0, okt)
                    add(pr, -1)
            for (x, y) in ((b, c), (c, b)):
                for p in range(N):
                    inner = dict(DDv[(p, y)])
                    for q in range(N):
                        if Gh[p][y][q] != 0:
                            for key, z in Dv[q].items():
                                inner[key] = inner.get(key, 0) + Gh[p][y][q]*z
                    pr = {}
                    self.mul(G[x][p], inner, pr, ok0, okt)
                    add(pr, -sp.Rational(1, 2))
            out[(b, c)] = self.cut(acc, ok0, okt)
        return out

    def mul_one(self, A, B):
        acc = {}
        self.mul(A, B, acc, self.k0, self.kt)
        return acc


def ucoef(phases):
    """the D-coefficients: phases is [(power j of lam^j phi, tag, phi)], D_a = d_a + sum lam^(j-1) (d_a phi) d_s"""
    return [{(j - 1, t): sp.diff(ph, X[a]) for (j, t, ph) in phases if sp.diff(ph, X[a]) != 0} for a in range(N)]


def put(G, M, k, t):
    for (a, b) in PAIRS:
        if M[a, b] != 0:
            G[a][b][(k, t)] = G[a][b].get((k, t), 0) + M[a, b]
            if a != b:
                G[b][a] = G[a][b]


def empty():
    G = [[None]*N for _ in range(N)]
    for (a, b) in PAIRS:
        G[a][b] = G[b][a] = {}
    return G


# ------------------------------------------------------------------------------------------------------------- B1
def b1_ricci(h, f=None):
    """the seven non-invariant components of Ric, the gauge term and Ric^H for g0 + h (+ f dv dphi1), lam exact"""
    g0, g0i = L.background()
    g = g0 + h
    if f is not None:
        g[0, 3] = g[3, 0] = f
    psi = sp.Function("psi")(v, r, th)
    du = [sp.diff(v + psi, x) for x in X]
    Dd = lambda e, k: sp.diff(e, X[k]) + du[k]/lam*sp.diff(e, s)
    gi = sp.zeros(N)
    blk = [0, 1, 2, 3] if f is not None else [0, 1, 2]
    B = g.extract(blk, blk)
    Bi = B.adjugate()/B.det()
    for i, a in enumerate(blk):
        for j, b in enumerate(blk):
            gi[a, b] = Bi[i, j]
    for a in range(N):
        if a not in blk:
            gi[a, a] = 1/g[a, a]
    Gam = L.christoffel(g, gi, Dd)
    Gh = L.christoffel(g0, g0i, lambda e, k: sp.diff(e, X[k]))
    Dv = [sum(gi[a, b]*(Gam[p][a][b] - Gh[p][a][b]) for a in range(N) for b in range(N)) for p in range(N)]
    out = {}
    for (b, c) in PAIRS:
        ric = 0
        for a in range(N):
            ric += Dd(Gam[a][b][c], a) - Dd(Gam[a][b][a], c)
            for d in range(N):
                ric += Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a]
        hb = sum(g[b, p]*(Dd(Dv[p], c) + sum(Gh[p][c][q]*Dv[q] for q in range(N))) for p in range(N))
        hc = sum(g[c, p]*(Dd(Dv[p], b) + sum(Gh[p][b][q]*Dv[q] for q in range(N))) for p in range(N))
        out[(b, c)] = (ric, (hb + hc)/2)
    return out, f


def b1(control=False):
    t0 = time.time()
    if control:
        f = sp.Function("f")(v, r, th, s)
        out, _ = b1_ricci(sp.zeros(N), f)
        rh = sp.expand(out[(0, 3)][0] - out[(0, 3)][1])
        cth = sp.simplify(rh.coeff(sp.Derivative(f, th, 2)))
        nz = [k for k in NONINV if out[k][0] != 0 or out[k][1] != 0]
        print("  B1 control (g0 + f dv dphi1): non-invariant components not identically zero: %s; coefficient of"
              " d_th^2 f in Ric^H_(v phi1): %s" % (nz, cth), flush=True)
        return cth == 0 and not nz
    h = sym("h", (v, r, th, s))
    out, _ = b1_ricci(h)
    ric = all(zero(out[k][0]) for k in NONINV)
    gauge = all(zero(out[k][1]) for k in NONINV)
    t2 = not any({X[3], X[4]} & (out[k][0].free_symbols | out[k][1].free_symbols) for k in PAIRS)
    print("  B1: g0 + h, h generic in the eight invariant components, phase v + psi generic, lam exact: in the seven"
          " components %s\n      Ric = 0: %s; gauge term = 0: %s; so Ric^H = 0: %s; no component of the fifteen"
          " contains phi1, phi2: %s [%.0fs]" % (NONINV, ric, gauge, ric and gauge, t2, time.time() - t0), flush=True)
    return ric and gauge and t2


# ------------------------------------------------------------------------------------------------------------- B2
TG = ("m2", "p2", "g3", "m3", "p3", "g4")


def b2(control=False):
    t0 = time.time()
    g0, g0i = L.background()
    ell = [g0i[a, 0] for a in range(N)]
    elld = lambda f: sum(ell[a]*sp.diff(f, X[a]) for a in range(N))
    box = lambda f: sum(g0i[a, b]*sp.diff(f, X[a], X[b]) for a in range(N) for b in range(N))
    mll = lambda m: sum(ell[a]*ell[b]*m[a, b] for a in range(N) for b in range(N))
    W = L.wave(with_chi=True)
    Ws, Wss = W.applyfunc(lambda e: sp.diff(e, s)), W.applyfunc(lambda e: sp.diff(e, s, 2))
    m1, m2, m3 = sym("m1", (v, r, th)), sym("m2", (v, r, th)), sym("m3", (v, r, th))
    g2, g3, g4 = sym("g2", (v, r, th, s)), sym("g3", (v, r, th, s)), sym("g4", (v, r, th, s))
    ph1, ph2, ph3 = [sp.Function("ph%d" % i)(v, r, th) for i in (1, 2, 3)]
    G = empty()
    put(G, g0, 0, '')
    put(G, W + m1, 1, '')
    put(G, g2, 2, '')
    for M, k, t in ((m2, 2, "m2"), (g3, 3, "g3"), (m3, 3, "m3"), (g4, 4, "g4")):
        put(G, M, k, t)
    u0 = v + r/3 if control else v
    UC = ucoef([(0, '', u0), (1, '', ph1), (2, "p2", ph2), (3, "p3", ph3)])
    E = Engine(G, UC, k0=1, kt=3, kt0=2)
    R = E.run(COMP, 0, 2)
    t1 = time.time()
    e1 = 2*elld(ph1) - mll(m1)
    R0 = L.reduced_ricci(W)
    g2f, g3f = {g2[a, b] for (a, b) in COMP}, {g3[a, b] for (a, b) in COMP}
    m2f = {m2[a, b] for (a, b) in COMP}
    ok = dict(val=True, s1=True, low=True, g4=True, e3=True, g3=True, g3c=True, m2=True, p2=True)
    for k in COMP:
        c = lambda kk, t: R[k].get((kk, t), 0)
        ok["val"] &= zero(c(-1, '')) and zero(c(0, '') - (R0[k][1] - e1*Wss[k]/2))
        ok["low"] &= not any(t and kk < 1 for (kk, t) in R[k])
        ok["s1"] &= (zero(c(1, "m2") - mll(m2)*Wss[k]/2) and zero(c(1, "p2") + elld(ph2)*Wss[k])
                     and not any(c(1, t) != 0 for t in ("g3", "m3", "p3", "g4")))
        ok["g4"] &= c(2, "g4") == 0
        ok["e3"] &= zero(c(2, "m3") - mll(m3)*Wss[k]/2) and zero(c(2, "p3") + elld(ph3)*Wss[k])
        rest = sp.expand(c(2, "g3") + elld(sp.diff(g3[k], s)) + e1*sp.diff(g3[k], s, 2)/2)
        ok["g3"] &= all(d.variables == (s,) for d in rest.atoms(sp.Derivative) if d.expr in g3f)
        ok["g3c"] &= not any(f.func in {x.func for x in g2f} for f in rest.atoms(sp.Function))
        two, high = second(c(2, "m2"), m2f)
        ok["m2"] &= not high and zero(two + box(m2[k])/2)
        two, high = second(c(2, "p2"), {ph2})
        ok["p2"] &= not high and zero(two + box(ph2)*Ws[k]/2)
    tag = "B2 control (u = v + r/3)" if control else "B2"
    print("  %s: engine against lead5 and stage5 S1 (b): R^(-1) = 0, R^(0) = R_v^(0)[W] - (1/2) e1 d_s^2 W: %s;\n"
          "      no stage-2 or stage-3 unknown below lam^1: %s; at lam^1 (stage5 S1 (c)) m2, phi2 only in -(1/2)(2 ell.d"
          " phi2 - m2(ell, ell)) d_s^2 W, g3, m3, phi3, g4 absent: %s;\n      in R^(2): g4 absent: %s; m3, phi3 only in"
          " -(1/2)(2 ell.d phi3 - m3(ell, ell)) d_s^2 W: %s; g3 only as -(ell.d) d_s g3 - (1/2) e1 d_s^2 g3 + (no"
          " X-derivative, one d_s): %s,\n      with no g2 in its coefficients: %s; second derivatives of m2"
          " only in -(1/2) box~ m2: %s; of phi2 only in -(1/2)(box~ phi2) d_s W: %s [engine %.0fs, checks %.0fs]"
          % (tag, ok["val"], ok["low"], ok["s1"], ok["g4"], ok["e3"], ok["g3"], ok["g3c"], ok["m2"], ok["p2"],
             t1 - t0, time.time() - t1), flush=True)
    return all(ok.values())


# ------------------------------------------------------------------------------------------------------------- B3
kap2 = sp.Symbol("kappa2", positive=True)                       # 4 k (k + 1)
Yf = sp.Function("Y")(th)
C2, S2 = sp.cos(th)**2, sp.sin(th)**2
SC = sp.sin(th)*sp.cos(th)


def yred(e):
    """Y'' -> -2 cot(2 th) Y' - kappa2 Y (the T^2-invariant harmonic equation on S^3), repeatedly"""
    while True:
        ds = [d for d in e.atoms(sp.Derivative) if d.expr == Yf and d.derivative_count >= 2]
        if not ds:
            return sp.expand(e)
        d = max(ds, key=lambda x: x.derivative_count)
        rhs = sp.diff(-2*sp.cos(2*th)/sp.sin(2*th)*sp.diff(Yf, th) - kap2*Yf, th, d.derivative_count - 2)
        e = sp.expand(e.subs(d, rhs))


FN = ("fvv", "fvr", "frr", "fv", "fr", "HL", "HT")


def sector(Y, fs):
    """the scalar-type T^2-invariant perturbation of harmonic Y with the seven functions fs"""
    fvv, fvr, frr, fv, fr, HL, HT = fs
    Yp, Ypp = sp.diff(Y, th), sp.diff(Y, th, 2)
    m = sp.zeros(N)
    m[0, 0], m[1, 1] = fvv*Y, frr*Y
    m[0, 1] = m[1, 0] = fvr*Y
    m[0, 2] = m[2, 0] = fv*Yp
    m[1, 2] = m[2, 1] = fr*Yp
    m[2, 2] = r**2*(HL*Y + HT*Ypp)
    m[3, 3] = r**2*(HL*C2*Y - HT*SC*Yp)
    m[4, 4] = r**2*(HL*S2*Y + HT*SC*Yp)
    return m


def linearise(m, comps):
    """the part of Ric^H(g0 + eps m) linear in eps (the operator of m1's equation from g0)"""
    g0, _ = L.background()
    G = empty()
    put(G, g0, 0, '')
    put(G, m, 1, "m")
    R = Engine(G, [{}]*N, k0=0, kt=1, kt0=1, linear=True).run(comps, -1, 1)
    return {k: R[k].get((1, "m"), 0) for k in comps}


TH = sp.Symbol("t")                                              # tan(th/2)
TRIG = {sp.cos(th): (1 - TH**2)/(1 + TH**2), sp.sin(th): 2*TH/(1 + TH**2)}


def coeffs(e):
    """coefficients of e, linear in the unknown functions and their derivatives, by atom"""
    e = sp.expand(sp.expand_trig(sp.expand(e)))
    at = sorted([d for d in e.atoms(sp.Derivative)], key=lambda d: -d.derivative_count)
    at += [f for f in e.atoms(sp.Function) if not isinstance(f, (sp.sin, sp.cos, sp.tan, sp.cot))]
    dm = [sp.Dummy() for _ in at]
    e = e.subs(list(zip(at, dm)))
    P = sp.Poly(e, *dm) if dm else None
    return [e] if P is None else [x for x in P.coeffs()]


def tzero(e):
    """exact zero test: every coefficient, a rational function of cos th, sin th, through t = tan(th/2)"""
    return all(sp.cancel(sp.together(c.subs(TRIG))) == 0 for c in coeffs(e))


def reduce_sector(Lm):
    """closure of the sector: each component a multiple of its harmonic tensor, multiples free of th"""
    Yp = sp.diff(Yf, th)
    red = {k: yred(Lm[k]) for k in Lm}
    out, ok = {}, True
    for k in ((0, 0), (0, 1), (1, 1)):
        ok &= tzero(red[k].coeff(Yp))
        out[k] = red[k].coeff(Yf)
    for k in ((0, 2), (1, 2)):
        ok &= tzero(red[k].coeff(Yf))
        out[k] = red[k].coeff(Yp)
    b = -red[(3, 3)].coeff(Yp)/SC
    a = red[(3, 3)].coeff(Yf)/C2
    ypp = yred(sp.diff(Yf, th, 2))
    for k, want in (((2, 2), a*Yf + b*ypp), ((3, 3), a*C2*Yf - b*SC*Yp), ((4, 4), a*S2*Yf + b*SC*Yp)):
        d = sp.expand(red[k] - want)
        ok &= tzero(d.coeff(Yf)) and tzero(d.coeff(Yp))
    out["L"], out["T"] = a, b
    ok &= all(tzero(sp.diff(x, th)) for x in out.values())
    out = {k: sp.expand(sp.radsimp(sp.expand(x.subs(th, sp.pi/4)))) for k, x in out.items()}
    return ok, out


def b3(control=False):
    t0 = time.time()
    fs = [sp.Function(n)(v, r) for n in FN]
    if control:
        m = sector(sp.legendre(2, sp.cos(2*th)), fs)
        M, Ms = S5.sigma_star(m)
        odd = all(zero(x) for x in Ms + M)
        Lb, odd_iv = b3_full(control=True)
        print("  B3 control: the k = 2 sector sigma-odd: %s; one quadrature: m1's operator sigma-equivariant: %s"
              % (odd, odd_iv), flush=True)
        return odd or odd_iv
    # (i) the sector, k symbolic
    Lm = linearise(sector(Yf, fs), COMP)
    closed, red = reduce_sector(Lm)
    sizes = {str(k): len(sp.Add.make_args(sp.expand(x))) for k, x in red.items()}
    par = {}
    for k in (1, 2, 3):
        M, Ms = S5.sigma_star(sector(sp.legendre(k, sp.cos(2*th)), fs))
        par[k] = all(zero(x - (-1)**k*y) for x, y in zip(Ms, M))
    print("  B3 (i): the linearisation of Ric^H at g0 on the scalar-type sector of Y (Y'' = -2 cot 2th Y' - kappa2 Y)"
          " closes, every multiple free of th: %s;\n      the reduced 1+1 system's terms per equation: %s;"
          " sigma^* = (-1)^k on the sector, k = 1, 2, 3 (P_k(cos 2th)): %s [%.0fs]"
          % (closed, sizes, par, time.time() - t0), flush=True)
    # (ii) the source's harmonics
    x, y = sp.symbols("x y", real=True)
    hf = sp.Function("h")
    Z = -sp.Integral(hf(y**2)**2, (y, 0, x))/2
    zodd = zero(sp.diff(Z + Z.subs(x, -x), x).doit()) and zero((Z + Z.subs(x, -x)).subs(x, 0).doit())
    src = -4*A2E2*hf(sp.cos(2*th)**2)**2*sp.sin(2*th)/(9*r**3)
    dZ = sp.diff(Z.subs(x, sp.cos(2*th)), th).doit()
    rep = zero(src - 4*A2E2/(9*r**3)*dZ)
    Zrec = -sp.atan(x)
    zrec = zero(sp.diff(Zrec, x) + sp.Rational(1, 2)*(2/(1 + x**2)))
    coef = [sp.simplify(sp.Rational(2*k + 1, 2)*sp.integrate(Zrec*sp.legendre(k, x), (x, -1, 1))) for k in range(8)]
    print("  B3 (ii): S3's source = (4 A^2 E^2/(9 r^3)) d_th Z(cos 2th) dv dth, Z(x) = -(1/2) int_0^x h(y^2)^2: %s; Z odd"
          " for every h: %s;\n      record's H (h^2 = 2/(1 + x^2), Z = -atan x: %s): Legendre coefficients k = 0..7: %s"
          % (rep, zodd, zrec, coef), flush=True)
    ii = rep and zodd and zrec and all(coef[k] == 0 for k in range(0, 8, 2)) and all(coef[k] != 0 for k in (1, 3, 5))
    # (iii) k = 1, constant h: the solution with no radiation at past null infinity, order by order in 1/r
    J = 5
    iii, (ode, fac, zc) = b3_solve(red, J)
    half = all(2*x % 2 == 1 for x in fac.values())
    print("  B3 (iii): k = 1, h constant, L0 m1 = -S, f = sum_j c_(f,j)(v) r^(-j - w), w = 1 for H_L, H_T, 0 else,"
          " j <= %d:\n      each order a linear transport c_j' = A c_j + (lower) in v with factors %s, all"
          " half-odd (never the radiation weight); with zero data before the shell\n      (P = A^2 E^2 h0^2 = 0"
          " there) %d of %d coefficients vanish identically; the first nonzero: c_(fv,2)' = %s, so\n      m1_(v th) ="
          " %s r^-2 + O(r^-3), Q = int_-oo^v P; sigma-odd (k = 1); equations satisfied through each order: %s"
          % (J, sorted(set(fac.values())), len(zc), len(fac), ode[("fv", 2)],
             sp.Rational(-4, 27)*sp.Symbol("Q")*sp.diff(sp.cos(2*th), th), iii),
          flush=True)
    iii &= half and ode[("fv", 2)] == sp.Rational(-4, 27)*sp.Function("P")(v)
    # (iv) the whole m1-linear mean of R^(1) with W: sigma-equivariant
    Lb, iv = b3_full(control=False)
    print("  B3 (iv): the m1-linear part of <R^(1)[g0 + lam (W + m1)]> (W, chi of S3), generic m1 in the eight"
          " components:\n      %d coefficients (target component, m1 component, derivative); sigma-equivariant"
          " coefficient by coefficient: %s [%.0fs]" % (Lb, iv, time.time() - t0), flush=True)
    return closed and par[1] and par[3] and not par[2] and ii and iii and iv


A2E2 = L.A**2*L.Ef**2


def b3_solve(red, J=5):
    """the reduced system at k = 1 with S3's source (constant h0): the formal solution in integer powers of 1/r,
    f = sum_j c_(f,j)(v) r^(-j - w_f), solved order by order; every c' is fixed by one transport equation in v"""
    P = sp.Function("P")(v)                                     # A^2 E^2 h0^2
    q = sp.Symbol("q")
    fs = [sp.Function(n)(v, r) for n in FN]
    w = dict(fvv=0, fvr=0, frr=0, fv=0, fr=0, HL=1, HT=1)
    c = {(F, j): sp.Function("c_%s_%d" % (F, j))(v) for F in FN for j in range(J + 1)}
    ans = {f: sum(c[(F, j)]*r**(-j - w[F]) for j in range(J + 1)) for F, f in zip(FN, fs)}
    eq = {}
    for k, x in red.items():
        e = x.subs(kap2, 8) + (sp.Rational(2, 9)*P/r**3 if k == (0, 2) else 0)    # L0 m1 = -S
        eq[k] = sp.expand(sp.expand(e.subs(ans).doit()).subs(r, 1/q))
    owner = {(0, 0): "fvv", (0, 1): "fvr", (1, 1): "frr", (0, 2): "fv", (1, 2): "fr", "L": "HL", "T": "HT"}
    shift = {k: (0 if k in ("L", "T") else 1) for k in owner}
    ode, zeroc, factors, ok = {}, set(), {}, True
    for j in range(J + 1):
        step, sub = {}, {}
        for (F, i) in zeroc:
            sub[c[(F, i)]] = 0
        for (F, i), rhs in ode.items():
            sub[sp.Derivative(c[(F, i)], v)] = rhs
        for k, F in owner.items():
            e = sp.expand(eq[k].coeff(q, j + shift[k]).subs(sub).doit().subs(sub))
            d = sp.Derivative(c[(F, j)], v)
            fac = e.coeff(d)
            others = [x for x in e.atoms(sp.Derivative) if x.expr in {c[(G, j)] for G in FN} and x != d]
            ok &= fac != 0 and not others and all(x.expr not in c.values() or x.expr in
                                                  {c[(G, i)] for G in FN for i in range(j)} or x == d
                                                  for x in e.atoms(sp.Derivative) if x.expr in c.values())
            step[F] = sp.expand(-(e - fac*d)/fac)
            factors[(F, j)] = fac
        cj = {c[(G, j)]: G for G in FN}
        live = {F for F in FN if step[F].subs({x: 0 for x in cj}) != 0}
        while True:                                 # c_j' = A c_j + b_j: zero data, b_j = 0 off live => zero there
            more = {F for F in FN if F not in live and any(cj[x] in live for x in step[F].atoms(sp.Function)
                                                            if x in cj)}
            if not more:
                break
            live |= more
        dead = {c[(G, j)]: 0 for G in FN if G not in live}
        for F in FN:
            if F in live:
                ode[(F, j)] = sp.expand(step[F].subs(dead))
            else:
                zeroc.add((F, j))
    resid = True
    sub = {c[(F, i)]: 0 for (F, i) in zeroc}
    sub.update({sp.Derivative(c[(F, i)], v): rhs for (F, i), rhs in ode.items()})
    for k in owner:
        for n in range(J + 1 + shift[k]):
            resid &= sp.expand(eq[k].coeff(q, n).subs(sub).doit().subs(sub)) == 0
    return ok and resid and bool(ode), (ode, factors, zeroc)


def b3_full(control):
    """m1-linear part of <R^(1)[g0 + lam (W + m1)]>; equivariance under sigma coefficient by coefficient"""
    _, _, _, W = S5.source(single=control, past=True)
    g0, _ = L.background()
    m1 = sym("m1", (v, r, th))
    G = empty()
    put(G, g0, 0, '')
    put(G, W, 1, '')
    put(G, m1, 1, "m1")
    R = Engine(G, ucoef([(0, '', v)]), k0=1, kt=2, kt0=1, linear=True).run(COMP, -1, 1)
    hh = sp.Function("h")(sp.cos(2*th)**2)
    Lb = {k: S5.mean(R[k].get((1, "m1"), 0)).subs(L.Hf, hh).doit() for k in COMP}
    eps = {0: 1, 1: 1, 2: -1, 3: 1, 4: 1}
    pi_ = {0: 0, 1: 1, 2: 2, 3: 4, 4: 3}
    pk = lambda a, b: (min(pi_[a], pi_[b]), max(pi_[a], pi_[b]))
    atoms = {}
    for k in COMP:
        for d in Lb[k].atoms(sp.Derivative) | Lb[k].atoms(sp.Function):
            f = d.expr if isinstance(d, sp.Derivative) else d
            if f.func.__name__.startswith("m1_"):
                vs = d.variables if isinstance(d, sp.Derivative) else ()
                atoms[d] = (f, tuple(sorted(vs, key=str)))
    syms = {d: sp.Dummy() for d in atoms}
    lin = {k: sp.expand(Lb[k].subs(syms)) for k in COMP}
    fun = {(a, b): m1[a, b] for (a, b) in COMP}
    byname = {(f.func, vs): d for d, (f, vs) in atoms.items()}
    ok, n = True, 0
    sub = {th: sp.pi/2 - th}
    for k in COMP:
        for d, (f, vs) in atoms.items():
            (a, b) = [kk for kk in COMP if fun[kk] == f][0]
            c = lin[k].coeff(syms[d])
            img = byname.get((fun[pk(a, b)].func, vs))
            c2 = lin[pk(*k)].coeff(syms[img]) if img is not None else 0
            lhs = c2.subs(sub, simultaneous=True)*eps[k[0]]*eps[k[1]]
            rhs = c*eps[a]*eps[b]*(-1)**sum(1 for x in vs if x == th)
            if c != 0 or c2 != 0:
                n += 1
                ok &= zero(lhs - rhs)
    return n, ok


CHECKS = [("B1", b1), ("B2", b2), ("B3", b3)]


def main():
    ok = True
    want = sys.argv[1:] or [n for n, _ in CHECKS]
    for name, f in CHECKS:
        if name not in want:
            continue
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
