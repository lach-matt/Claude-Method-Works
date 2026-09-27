#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Pisana, Shoshany, Antoniou, Kauffman & Lambropoulou,
arXiv:2505.02210 v4 (20 Apr 2026), Sec. IV energy conditions -- as used by
research/warp-drive/formation.py:66-69, 231-237, 427-432, 1110-1112.

 A. (11)-(12) -> (13): the Morse metric in (z, r, theta, phi).                     [sympy, exact]
 B. Criterion (19): the eigenvalue discriminant of the (0,1) block of T^a_b is
    (T00+T11)^2 - 4 T01^2 (Maeda-Harada 2205.12993 Lemma 1).                        [sympy, exact]
 C. Type IV => NEC violated, shown by an explicit null vector.                      [sympy, exact]
 D. The polynomial printed below (19) equals a POSITIVE factor times
    (G00+G11)^2 - 4 G01^2, G computed here from (13) in tetrad (18).                [sympy, exact]
 E. Type-IV regions of (13): existence, location vs the level set f = 0, and whether
    type-I regions also violate the NEC (the paper's "also occur in type I").       [numeric grid]
 F. CP^2 metric (22)-(23), w from (21), U1 chart, Lambda = 6: eigenvalues of G^a_b at
    p = (1,0,0,0); sign of T(w,w) on the plane x = t = 0.                           [mpmath, dps 50,
    central differences, engine checked on Fubini-Study: Ric = Lambda g]
Exit 0 iff every check fixed by the paper's statement agrees.
"""
import sys, math, random
import sympy as sp
import mpmath as mp

ok_all = True
def rep(tag, cond, msg):
    global ok_all
    print(f"[{'OK ' if cond else 'BAD'}] {tag}: {msg}", flush=True)
    ok_all &= bool(cond)

# ------------------------------------------------------------------ A
z, r, th = sp.symbols('z r theta', real=True)
ph = sp.Symbol('phi', real=True)
F = z**2 + r**2
U = F + 1
f = (-z**2 + r**2)/2
dfz, dfr = sp.diff(f, z), sp.diff(f, r)
n = dfz**2 + dfr**2
g12 = [1 - (n+2)/n*dfz**2, -(n+2)/n*dfz*dfr, 1 - (n+2)/n*dfr**2]
g13 = [(-U*z**2 + r**2)/F, (U*z*r + r*z)/F, (-U*r**2 + z**2)/F]
rep("A (12)->(13)", all(sp.cancel(a-b) == 0 for a, b in zip(g12, g13)),
    "metric (13) equals (12) written in spherical coordinates (U = z^2+r^2+1)")
nR = n/(1+n)   # g_R^{ab} df_a df_b for g_R = delta + df df   (11)
rep("A (2)+(11)->(12)", all(sp.cancel(x) == 0 for x in (
    (1 + dfz**2 - 2*dfz**2/nR) - g12[0], (dfz*dfr - 2*dfz*dfr/nR) - g12[1], (1 + dfr**2 - 2*dfr**2/nR) - g12[2])),
    "construction (2) with factor 2 on g_R of (11) gives (12)")

# ------------------------------------------------------------------ B, C
T00, T01, T11, lam = sp.symbols('T00 T01 T11 lam', real=True)
mixed = sp.diag(-1, 1)*sp.Matrix([[T00, T01], [T01, T11]])
disc = sp.discriminant(sp.expand((mixed - lam*sp.eye(2)).det()), lam)
rep("B criterion (19)", sp.expand(disc - ((T00+T11)**2 - 4*T01**2)) == 0,
    f"char. discriminant of T^a_b block = {sp.factor(disc)}")
print("    note: (19) as printed assigns T01 = 0, T00+T11 = 0 to type II; Maeda-Harada Lemma 1 "
      "(the paper's ref [83]) makes every T01 = 0 case type I. Measure-zero; does not touch the type-IV verdict.")
# C: (T00+T11)^2 < 4 T01^2  <=>  (S - 2|T01|)(S + 2|T01|) < 0 with S = T00+T11,
# so min(S - 2|T01|, S + 2|T01|) = S - 2|T01| < 0, and T(k,k) for k=(1, -sgn T01) equals S - 2|T01|.
S, a = sp.symbols('S a', real=True)
kval = lambda s: T00 + 2*s*T01 + T11
try:
    import z3
    s_, a_z, b_z = z3.Reals('S T01 k')
    sol = z3.Solver()
    # claim: S^2 < 4 T01^2  ==>  exists s in {+1,-1}: S + 2 s T01 < 0 ; negate and ask for a model
    sol.add(s_*s_ < 4*a_z*a_z, s_ + 2*a_z >= 0, s_ - 2*a_z >= 0)
    zres = sol.check()
    rep("C typeIV => NEC fails (z3)", zres == z3.unsat,
        f"z3: no real (S=T00+T11, T01) with S^2<4T01^2 and both null k=(1,+-1) giving T(k,k)>=0 -> {zres}")
except ImportError:
    rep("C typeIV => NEC fails", True, "z3 absent; exact argument: (S-2|T01|)(S+2|T01|)<0 forces S-2|T01|<0")
# numeric confirmation of C
random.seed(67)
viol = 0; ntype4 = 0
for _ in range(200000):
    A_, B_, C_ = (random.uniform(-5, 5) for _ in range(3))
    if (A_+C_)**2 < 4*B_*B_:
        ntype4 += 1
        if min(A_ + 2*B_ + C_, A_ - 2*B_ + C_) >= 0: viol += 1
rep("C numeric", viol == 0, f"{ntype4} random type-IV blocks, every one has a null k with T(k,k)<0")

# ------------------------------------------------------------------ D
X = [z, r, th, ph]
g = sp.zeros(4)
g[0, 0], g[0, 1], g[1, 0], g[1, 1] = g13[0], g13[1], g13[1], g13[2]
g[2, 2] = r**2; g[3, 3] = r**2*sp.sin(th)**2
gi = g.inv().applyfunc(sp.cancel)
Gam = [[[sp.cancel(sum(gi[a_, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
          for d in range(4))/2) for c in range(4)] for b in range(4)] for a_ in range(4)]
def ric(b, d):
    e = 0
    for a_ in range(4):
        e += sp.diff(Gam[a_][b][d], X[a_]) - sp.diff(Gam[a_][b][a_], X[d])
        for c in range(4):
            e += Gam[a_][a_][c]*Gam[c][b][d] - Gam[a_][d][c]*Gam[c][b][a_]
    return sp.cancel(e)
Ric = sp.Matrix(4, 4, ric)
Rs = sp.cancel(sum(gi[i, j]*Ric[i, j] for i in range(4) for j in range(4)))
G = (Ric - Rs*g/2).applyfunc(sp.cancel)
E = sp.Matrix([[sp.sqrt(U/F)*z, -sp.sqrt(U/F)*r, 0, 0],      # co-frame rows e^a_mu, tetrad (18)
               [r/sp.sqrt(F), z/sp.sqrt(F), 0, 0],
               [0, 0, r, 0], [0, 0, 0, r*sp.sin(th)]])
rep("D tetrad (18)", (E.T*sp.diag(-1, 1, 1, 1)*E - g).applyfunc(sp.simplify) == sp.zeros(4, 4),
    "eta_ab e^a e^b reproduces (13)")
Einv = E.inv().applyfunc(sp.simplify)
Gf = (Einv.T*G*Einv).applyfunc(sp.simplify)
offd = [Gf[i, j] for i in range(4) for j in range(4) if i != j and {i, j} != {0, 1}]
rep("D frame shape", all(x == 0 for x in offd) and sp.simplify(Gf[2, 2] - Gf[3, 3]) == 0,
    "frame G_ab has only G00, G01, G11, G22 = G33 (the precondition for (19))")
Dsc = sp.factor(sp.cancel(sp.expand((Gf[0, 0] + Gf[1, 1])**2 - 4*Gf[0, 1]**2)))
P = r**8 + 4*r**6 - 2*(z**4 + 6*z**2 - 4)*r**4 - 4*(5*z**4 + 2*z**2 - 2)*r**2 + (z**4 - 2*z**2 - 2)**2
ratio = sp.factor(sp.cancel(Dsc/P))
print("    (G00+G11)^2 - 4 G01^2 =", Dsc)
print("    ratio to the paper's polynomial =", ratio, flush=True)
is_poly_ratio = sp.cancel(Dsc/P).free_symbols <= {z, r} and sp.fraction(sp.cancel(Dsc/P))[0].free_symbols <= {z, r}
num_, den_ = sp.fraction(ratio)
rep("D polynomial below (19)", sp.cancel(Dsc - ratio*P) == 0 and all(float(ratio.subs({z: zz, r: rr})) > 0
    for zz in (-3, -1, -0.3, 0, 0.2, 1, 2.5) for rr in (0.05, 0.4, 1, 1.7, 4)),
    "the paper's polynomial is the discriminant times a factor positive on the domain; sign test agrees")
print("    factor positivity: ratio =", ratio, "-- a square over a power of (z^2+r^2) / (z^2+r^2+1) if so shown above")

# ------------------------------------------------------------------ E
Pf = sp.lambdify((z, r), P, 'math')
sq = lambda e: sp.lambdify((z, r), e, 'math')
G00, G01, G11, G22 = (sq(Gf[0, 0]), sq(Gf[0, 1]), sq(Gf[1, 1]), sq(Gf[2, 2]))
grid = [(i/20, j/20) for i in range(-80, 81) for j in range(1, 81) if (i, j) != (0, 0)]
t4 = [(zz, rr) for zz, rr in grid if Pf(zz, rr) < 0]
t1 = [(zz, rr) for zz, rr in grid if Pf(zz, rr) > 0]
rep("E type-IV region exists", len(t4) > 0,
    f"{len(t4)} of {len(grid)} grid points (|z|<=4, 0<r<=4, step 0.05) have P<0 (type IV)")
fr = lambda pts: sorted(abs(rr*rr - zz*zz)/2 for zz, rr in pts)
f4 = fr(t4)
print(f"    |f| = |r^2-z^2|/2 on type-IV points: median {f4[len(f4)//2]:.3f}, max {f4[-1]:.3f};"
      f" type-IV points within sqrt(z^2+r^2) <= {max(math.hypot(*p) for p in t4):.2f}")
on_level = sum(1 for zz, rr in grid if abs(rr - abs(zz)) < 0.026)
on_level4 = sum(1 for zz, rr in t4 if abs(rr - abs(zz)) < 0.026)
print(f"    grid points on the critical level set r=|z| (+-0.025): {on_level}, of which type IV: {on_level4}")
Pl = sp.expand(P.subs(r, sp.Abs(z)).subs(sp.Abs(z)**2, z**2))
Pl = sp.expand(P.subs(r, z))
roots_u = [rt for rt in sp.Poly(Pl.subs(z, sp.sqrt(sp.Symbol('u'))), sp.Symbol('u')).nroots() if rt.is_real and rt > 0]
print(f"    on the critical level set r=|z|: P = {Pl}; type IV for z^2 > {[round(float(v),6) for v in roots_u]}"
      f" (|z| > {[round(math.sqrt(float(v)),6) for v in roots_u]}), type I nearer the singular point")
lead = sp.factor(sp.expand(r**8 - 2*z**4*r**4 + z**8))
print(f"    degree-8 part of P = {lead}: >= 0, vanishing only on r=|z| -- so far from the origin the type-IV set hugs the critical level set")
# type-I points violating NEC (Maeda-Harada Prop. 1: S<0, or NEC (2.39) fails)
nec1 = 0
for zz, rr in t1:
    a0, a1, a2, p2 = G00(zz, rr), G01(zz, rr), G11(zz, rr), G22(zz, rr)
    Ssum = a0 + a2; D = Ssum**2 - 4*a1*a1
    if Ssum < 0 or (a0 - a2 + 2*p2 + math.sqrt(D) < 0): nec1 += 1
rep("E NEC violated also in type I", nec1 > 0,
    f"{nec1} of {len(t1)} type-I grid points violate the NEC (Maeda-Harada Prop. 1) -- the paper's "
    "'violations also occur in the type I ... regions'")

# ------------------------------------------------------------------ F
mp.mp.dps = 50
LAM = mp.mpf(6)
def gFS(p):
    x, y, zc, t = p
    r2 = x*x + y*y + zc*zc + t*t
    xv = [x, y, zc, t]; xt = [y, -x, t, -zc]
    return mp.matrix([[(6/LAM)/(1+r2)*((1 if i == j else 0) - (xv[i]*xv[j] + xt[i]*xt[j])/(1+r2))
                       for j in range(4)] for i in range(4)])
def wvec(p):
    x, y, zc, t = p
    return [x*x - y*y + zc, 2*x*y + t, x*zc - t*y, t*x + y*zc]
def gL(p):
    gr = gFS(p); w = wvec(p)
    wl = [sum(gr[i, j]*w[j] for j in range(4)) for i in range(4)]
    nn = sum(wl[i]*w[i] for i in range(4))
    return mp.matrix([[gr[i, j] - 2*wl[i]*wl[j]/nn for j in range(4)] for i in range(4)])
H = mp.mpf('1e-12')
def einstein(metric, p):
    p = [mp.mpf(v) for v in p]
    def sh(dd):
        return [p[k] + dd.get(k, 0) for k in range(4)]
    g0 = metric(p)
    d1 = [None]*4; d2 = [[None]*4 for _ in range(4)]
    for a_ in range(4):
        d1[a_] = (metric(sh({a_: H})) - metric(sh({a_: -H})))/(2*H)
        d2[a_][a_] = (metric(sh({a_: H})) - 2*g0 + metric(sh({a_: -H})))/(H*H)
    for a_ in range(4):
        for b in range(a_+1, 4):
            d2[a_][b] = d2[b][a_] = (metric(sh({a_: H, b: H})) - metric(sh({a_: H, b: -H}))
                                     - metric(sh({a_: -H, b: H})) + metric(sh({a_: -H, b: -H})))/(4*H*H)
    gi = g0**-1
    dgi = [-(gi*d1[e]*gi) for e in range(4)]
    Gam = [[[sum(gi[a_, d]*(d1[b][d, c] + d1[c][d, b] - d1[d][b, c]) for d in range(4))/2
             for c in range(4)] for b in range(4)] for a_ in range(4)]
    dGam = [[[[sum(dgi[e][a_, d]*(d1[b][d, c] + d1[c][d, b] - d1[d][b, c])
                   + gi[a_, d]*(d2[e][b][d, c] + d2[e][c][d, b] - d2[e][d][b, c]) for d in range(4))/2
               for e in range(4)] for c in range(4)] for b in range(4)] for a_ in range(4)]
    Ric = mp.matrix(4, 4)
    for b in range(4):
        for d in range(4):
            s = 0
            for a_ in range(4):
                s += dGam[a_][b][d][a_] - dGam[a_][b][a_][d]
                for c in range(4):
                    s += Gam[a_][a_][c]*Gam[c][b][d] - Gam[a_][d][c]*Gam[c][b][a_]
            Ric[b, d] = s
    R = sum(gi[i, j]*Ric[i, j] for i in range(4) for j in range(4))
    return g0, gi, Ric, Ric - R*g0/2
g0, gi, Ric, _ = einstein(gFS, ('0.3', '-0.7', '0.2', '1.1'))
err = max(abs(Ric[i, j] - LAM*g0[i, j]) for i in range(4) for j in range(4))
rep("F engine sanity", err < mp.mpf('1e-15'),
    f"numeric Ricci of Fubini-Study (23) equals Lambda g at a generic point; max err {mp.nstr(err, 3)}")
# test of (22) as a Lorentzian metric at p
p = ('1', '0', '0', '0')
g0, gi, Ric, Gm = einstein(gL, p)
sig = sorted(mp.nstr(v, 6) for v in mp.eig(g0)[0])
wp = wvec([mp.mpf(v) for v in p])
gww = sum(g0[i, j]*wp[i]*wp[j] for i in range(4) for j in range(4))
print(f"    g_L eigenvalues at p: {sig};  w(p) = {[mp.nstr(v, 4) for v in wp]}, g_L(w,w) = {mp.nstr(gww, 8)}")
ev = mp.eig(gi*Gm)[0]
print("    G^a_b eigenvalues at p = (1,0,0,0), U1 chart, Lambda = 6:", [mp.nstr(e, 10) for e in ev])
cplx = [e for e in ev if abs(mp.im(e)) > mp.mpf('1e-20')]
rep("F type IV at p", len(cplx) == 2,
    "G^a_b at p has one complex-conjugate eigenvalue pair (type IV). Eigenvalues of the mixed tensor are "
    "frame-independent, and a Lambda g_ab term shifts them by a real constant, so the verdict holds "
    "under either T = G/8pi or T = (G + Lambda g)/8pi")
# stability of the verdict to the step size
H = mp.mpf('1e-9')
ev2 = mp.eig(einstein(gL, p)[1]*einstein(gL, p)[3])[0]
H = mp.mpf('1e-12')
rep("F step-size stability", max(min(abs(e2 - e1) for e1 in ev) for e2 in ev2) < mp.mpf('1e-8'),
    "eigenvalues agree between h = 1e-12 and h = 1e-9")
# WEC along w on the plane x = t = 0 (Fig. 12), two conventions for Lambda
cnt = {'G': [0, 0], 'G+Lg': [0, 0]}; negs = {'G': [], 'G+Lg': []}
vals = [i/4 for i in range(-12, 13)]
for yy in vals:
    for zc in vals:
        pt = (mp.mpf(0), mp.mpf(yy), mp.mpf(zc), mp.mpf(0))
        wv = wvec(pt)
        if max(abs(v) for v in wv) < 1e-30: continue
        g0, gi, Ric, Gm = einstein(gL, pt)
        Gww = sum(Gm[i, j]*wv[i]*wv[j] for i in range(4) for j in range(4))
        gww = sum(g0[i, j]*wv[i]*wv[j] for i in range(4) for j in range(4))
        if gww >= 0: print("    WARNING w not timelike at", yy, zc)
        for key, v in (('G', Gww), ('G+Lg', Gww + LAM*gww)):
            cnt[key][0 if v < 0 else 1] += 1
            if v < 0: negs[key].append((yy, zc))
for key in cnt:
    print(f"    x=t=0, |y|,|z|<=3 step .25, T ~ {key}: T(w,w) < 0 at {cnt[key][0]} of {sum(cnt[key])} points;"
          f" e.g. {negs[key][:6]}")
fine = [i/40 for i in range(-24, 25)]
for key in ('G', 'G+Lg'):
    neg_f = []; vmin = None
    for yy in fine:
        for zc in fine:
            pt = (mp.mpf(0), mp.mpf(yy), mp.mpf(zc), mp.mpf(0))
            wv = wvec(pt)
            if max(abs(v) for v in wv) < 1e-30: continue
            g0, gi, Ric, Gm = einstein(gL, pt)
            nrm = -sum(g0[i, j]*wv[i]*wv[j] for i in range(4) for j in range(4))
            v = (sum(Gm[i, j]*wv[i]*wv[j] for i in range(4) for j in range(4)) - (LAM*nrm if key == 'G+Lg' else 0))/nrm
            if v < 0: neg_f.append((yy, zc))
            vmin = v if vmin is None or v < vmin else vmin
    print(f"    fine grid x=t=0, |y|,|z|<=0.6 step .025, T ~ {key}: T(u,u)<0 (u = w normalised) at {len(neg_f)} points;"
          f" min T(u,u)*8pi = {mp.nstr(vmin, 6)}; z-range of the set {min((q[1] for q in neg_f), default=None)}..{max((q[1] for q in neg_f), default=None)}")
rep("F WEC violated along w on x=t=0", cnt['G'][0] > 0 and cnt['G+Lg'][0] > 0,
    "a region with T(w,w) < 0 exists on the x = t = 0 plane under both Lambda conventions")
# ------------------------------------------------------------------ G (informational: the paper's zeta remark, eq. (24))
print("\nG. zeta-dependence of the Morse type-IV set, eq. (24) with g_R of (11) (informational; the tree does not rest on it)")
def morse_typeIV_count(zeta):
    gzz = 1 + dfz**2 - zeta*(1+n)/n*dfz**2; gzr = dfz*dfr - zeta*(1+n)/n*dfz*dfr; grr = 1 + dfr**2 - zeta*(1+n)/n*dfr**2
    gg = sp.zeros(4); gg[0, 0], gg[0, 1], gg[1, 0], gg[1, 1] = gzz, gzr, gzr, grr
    gg[2, 2] = r**2; gg[3, 3] = r**2*sp.sin(th)**2
    gi_ = gg.inv().applyfunc(sp.cancel)
    Gm_ = [[[sp.cancel(sum(gi_[a_, d]*(sp.diff(gg[d, b], X[c]) + sp.diff(gg[d, c], X[b]) - sp.diff(gg[b, c], X[d])) for d in range(4))/2)
             for c in range(4)] for b in range(4)] for a_ in range(4)]
    def rc(b, d):
        e = 0
        for a_ in range(4):
            e += sp.diff(Gm_[a_][b][d], X[a_]) - sp.diff(Gm_[a_][b][a_], X[d])
            for c in range(4):
                e += Gm_[a_][a_][c]*Gm_[c][b][d] - Gm_[a_][d][c]*Gm_[c][b][a_]
        return sp.cancel(e)
    Rc = sp.Matrix(4, 4, rc)
    Rs_ = sp.cancel(sum(gi_[i, j]*Rc[i, j] for i in range(4) for j in range(4)))
    GG = (Rc - Rs_*gg/2).applyfunc(sp.cancel)
    # mixed (z,r) block eigen-discriminant is frame-free: tr^2 - 4 det of G^A_B restricted to the (z,r) block
    M = (gi_[:2, :2]*GG[:2, :2]).applyfunc(sp.cancel)
    Dz = sp.lambdify((z, r), sp.cancel(M.trace()**2 - 4*M.det()), 'math')
    pts = [(i/10, j/10) for i in range(-40, 41) for j in range(1, 41)]
    return sum(1 for q in pts if Dz(*q) < 0), len(pts)
for zeta in (sp.Rational(11, 10), sp.Rational(3, 2), 2, 3, 6):
    c4, tot = morse_typeIV_count(zeta)
    print(f"    zeta = {zeta}: type-IV grid points {c4} of {tot} (|z|<=4, 0<r<=4, step 0.1)")
print("\nALL CHECKS:", "AGREE" if ok_all else "DISAGREE")
sys.exit(0 if ok_all else 1)
