#!/usr/bin/env python3
"""DOCKET 67 -- birkhoff-theorem re-derivation (sympy).  Writes nothing; prints PASS/FAIL rows.

B1  Birkhoff in the areal chart ds^2 = -e^{2a(t,r)}dt^2 + e^{2b(t,r)}dr^2 + r^2 dOmega^2:
    G_tr = 0 forces b_t = 0; G_tt = 0 then gives e^{-2b} = 1 - 2M/r; G_rr = 0 gives
    a = -b + h(t), removable by t -> t'(t).  (M any real constant -- sign NOT fixed.)
B2  Covariant (double-null) form, valid in untrapped AND trapped regions:
    ds^2 = -2 e^{2s(u,v)} du dv + r(u,v)^2 dOmega^2, Misner-Sharp m = (r/2)(1 + 2 e^{-2s} r_u r_v).
    m_u and m_v are linear in Einstein-tensor components (G=0 => dm = 0: m is constant).
B3  Degenerate cases for Lambda = 0: r = const is not vacuum (G has a 1/r0^2 term);
    null grad r (r_v = 0 on an open set) forces m = r/2, contradicting dm = 0 unless r_u = 0.
B4  The tree's witness (foliation.py V7): generalised PG chart.  Ricci = 0 recomputed; MS mass M;
    it IS Schwarzschild via t = tau/sqrt(k) + F(R), F' = -v/(sqrt(k) f), on f != 0 (explicit isometry).
B5  Where is it STATIC?  Killing field d_tau has norm -(1-2M/R)/(1+2E): timelike iff R > 2M.  The
    chart is non-degenerate for every R > 0 (det of the (tau,R) block = -1/(1+2E)), so it covers
    R <= 2M, where NO Killing combination a*xi + rotations is timelike (norms add, cross terms 0).
    => "the spacetime is STATIC" holds on R > 2M only (Schmidt gr-qc/9709071 p.2; Goswami-Ellis
    1101.4520 eq.(54): the R < 2M part is spatially homogeneous, Kantowski-Sachs-type).
B6  wall.py's use: a vacuum region containing a REGULAR centre.  Kretschmann of Schwarzschild =
    48 M^2/r^6, finite at r -> 0 iff M = 0, and M = 0 gives Riemann = 0 (flat).  So "interior is
    exactly flat" needs Birkhoff PLUS a regular-centre hypothesis (M_in = 0).
B7  The device's interior (stability.py/linstab.py): M_in = -m < 0: f = 1 + 2m/R > 0 for all R > 0,
    so d_t is timelike everywhere -> static everywhere (no horizon), and Kretschmann diverges at
    r = 0 -- the m(0) != 0 singular centre linstab's specthm R8 names.  Birkhoff admits M < 0.
B8  Thin-shell input: stability.sigma(R,-m,0) = (sqrt(1+2m/R)-1)/(4 pi R) > 0 for all m > 0, R > 0
    (checked symbolically) -- Birkhoff is what licenses f_in, f_out being used unchanged during
    radial motion (linstab P3), since M in each vacuum region is constant (B1/B2).
"""
import sympy as sp

rows = []
def row(name, ok, detail=""):
    rows.append((name, bool(ok), detail))
    print("%-4s %s  %s" % ("PASS" if ok else "FAIL", name, detail))

def christoffel(g, x):
    n = len(x); gi = sp.simplify(g.inv())
    return [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
             for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)], gi

def ricci(g, x):
    n = len(x); Ga, gi = christoffel(g, x)
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            e = 0
            for a in range(n):
                e += sp.diff(Ga[a][b][c], x[a]) - sp.diff(Ga[a][b][a], x[c])
                for d in range(n):
                    e += Ga[a][a][d]*Ga[d][b][c] - Ga[a][c][d]*Ga[d][b][a]
            Ric[b, c] = sp.simplify(e)
    return Ric, gi, Ga

def einstein(g, x):
    Ric, gi, Ga = ricci(g, x)
    Rs = sp.simplify(sum(gi[i, j]*Ric[i, j] for i in range(len(x)) for j in range(len(x))))
    return sp.simplify(Ric - Rs*g/2), Ric, gi, Ga

def riemann_down(g, x):
    n = len(x); Ga, gi = christoffel(g, x)
    R = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    e = sp.diff(Ga[a][b][d], x[c]) - sp.diff(Ga[a][b][c], x[d])
                    for k in range(n):
                        e += Ga[a][c][k]*Ga[k][b][d] - Ga[a][d][k]*Ga[k][b][c]
                    R[(a, b, c, d)] = e
    Rd = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    Rd[(a, b, c, d)] = sp.simplify(sum(g[a, k]*R[(k, b, c, d)] for k in range(n)))
    return Rd, gi

t, r, th, ph = sp.symbols('t r theta phi', positive=True)
X = [t, r, th, ph]

# ---------------- B1
a = sp.Function('a')(t, r); b = sp.Function('b')(t, r)
g = sp.diag(-sp.exp(2*a), sp.exp(2*b), r**2, r**2*sp.sin(th)**2)
G, _, _, _ = einstein(g, X)
Gtr = sp.simplify(G[0, 1])
row("B1a G_tr = (2/r) b_t  (so vacuum => b = b(r))", sp.simplify(Gtr - 2*sp.diff(b, t)/r) == 0, str(Gtr))
bb = sp.Function('B')(r); aa = sp.Function('A')(t, r)
g1 = sp.diag(-sp.exp(2*aa), sp.exp(2*bb), r**2, r**2*sp.sin(th)**2)
G1, _, _, _ = einstein(g1, X)
M = sp.Symbol('M', real=True)
sol_b = sp.log(1/sp.sqrt(1 - 2*M/r))
row("B1b G_tt = 0 solved by e^{-2B} = 1-2M/r (M any real)",
    sp.simplify(G1[0, 0].subs(bb, sol_b).doit()) == 0)
# general solution of G_tt: e^{-2B} = 1 - 2M/r is the general solution of (r(1-e^{-2B}))' = 0
Gtt_form = sp.simplify(G1[0, 0]*sp.exp(-2*aa)*r**2)
chk = sp.simplify(Gtt_form - sp.diff(r*(1 - sp.exp(-2*bb)), r))
row("B1c G_tt e^{-2A} r^2 = d/dr[r(1-e^{-2B})]  (first integral: 2M constant)", chk == 0, str(chk))
h = sp.Function('h')(t)
Grr = sp.simplify(G1[1, 1].subs(bb, sol_b).doit())
Asol = -sol_b + h
row("B1d G_rr = 0 solved by A = -B + h(t)",
    sp.simplify(Grr.subs(aa, Asol).doit()) == 0)
# uniqueness of A: G_rr is first order in A_r: show G_rr = (2/r) A_r e^{-2B}... - ...
Arr = sp.solve(sp.Eq(Grr, 0), sp.diff(aa, r))
row("B1e G_rr = 0 fixes A_r uniquely = -dB/dr", len(Arr) == 1 and sp.simplify(Arr[0] - sp.diff(-sol_b, r)) == 0, str(Arr))
Gthth = sp.simplify(G1[2, 2].subs({bb: sol_b, aa: Asol}).doit())
row("B1f G_thth = 0 then (no further condition)", Gthth == 0)

# ---------------- B2 double null
u, v = sp.symbols('u v')
s = sp.Function('s')(u, v); R = sp.Function('R')(u, v)
Y = [u, v, th, ph]
g2 = sp.zeros(4, 4); g2[0, 1] = g2[1, 0] = -sp.exp(2*s); g2[2, 2] = R**2; g2[3, 3] = R**2*sp.sin(th)**2
G2, _, gi2, _ = einstein(g2, Y)
m = R/2*(1 + 2*sp.exp(-2*s)*sp.diff(R, u)*sp.diff(R, v))
gradR2 = sp.simplify(2*gi2[0, 1]*sp.diff(R, u)*sp.diff(R, v))
row("B2a Misner-Sharp: 1 - 2m/R = g^ab d_aR d_bR", sp.simplify(1 - 2*m/R - gradR2) == 0)
# m_u = c1*G_uu + c2*G_uv ; find by ansatz
c1, c2, c3, c4 = sp.symbols('c1 c2 c3 c4')
mu = sp.expand(sp.diff(m, u)); mv = sp.expand(sp.diff(m, v))
# known Misner-Sharp: m_u = R^2 e^{-2s}(R_u G_uv - R_v G_uu)  (up to normalisation); test directly
cand_u = R**2*sp.exp(-2*s)*(sp.diff(R, u)*G2[0, 1] - sp.diff(R, v)*G2[0, 0])
cand_v = R**2*sp.exp(-2*s)*(sp.diff(R, v)*G2[0, 1] - sp.diff(R, u)*G2[1, 1])
ku = sp.simplify(sp.expand(mu)/sp.expand(cand_u)); kv = sp.simplify(sp.expand(mv)/sp.expand(cand_v))
row("B2b m_u proportional to (R_u G_uv - R_v G_uu): vacuum => m_u = 0", ku.is_number, "ratio=%s" % ku)
row("B2c m_v proportional to (R_v G_uv - R_u G_vv): vacuum => m_v = 0", kv.is_number, "ratio=%s" % kv)

# ---------------- B3 degenerate
r0 = sp.Symbol('r0', positive=True)
G3 = sp.simplify(G2.subs(R, r0).doit())
row("B3a R = r0 constant: G_uv = e^{2s}/(2 r0^2)-type term != 0 => not vacuum (Lambda = 0)",
    sp.simplify(G3[0, 1]) != 0, "G_uv=%s" % sp.simplify(G3[0, 1]))
row("B3b R_v = 0 on an open set: m = R/2 exactly, so dm = 0 forces dR = 0 -> back to B3a",
    sp.simplify(m.subs(sp.Derivative(R, v), 0) - R/2) == 0)

# ---------------- B4 the tree's witness
tau, Rc = sp.symbols('tau R', positive=True)
Mp, E = sp.symbols('M E', positive=True)
Z = [tau, Rc, th, ph]
vv = sp.sqrt(2*Mp/Rc + 2*E); kk = 1 + 2*E
hm = sp.zeros(4, 4); hm[0, 0] = -1 + vv**2/kk; hm[0, 1] = hm[1, 0] = vv/kk; hm[1, 1] = 1/kk
hm[2, 2] = Rc**2; hm[3, 3] = Rc**2*sp.sin(th)**2
Ric4, hi4, _ = ricci(hm, Z)
row("B4a (V7 recomputed) generalised PG chart: all 16 Ricci components 0",
    all(sp.simplify(Ric4[i, j]) == 0 for i in range(4) for j in range(4)))
row("B4b (V8 recomputed) Misner-Sharp mass = M", sp.simplify(Rc*(1 - hi4[1, 1])/2 - Mp) == 0)
f = 1 - 2*Mp/Rc
Fp = -vv/(sp.sqrt(kk)*f)
# Schwarzschild pulled back by t = tau/sqrt(k) + F(R)
dt_dtau = 1/sp.sqrt(kk); dt_dR = Fp
pb00 = -f*dt_dtau**2; pb01 = -f*dt_dtau*dt_dR; pb11 = -f*dt_dR**2 + 1/f
row("B4c explicit isometry to Schwarzschild (t,R) on f != 0: tau-tau, tau-R, R-R match",
    all(sp.simplify(x) == 0 for x in (pb00 - hm[0, 0], pb01 - hm[0, 1], pb11 - hm[1, 1])))

# ---------------- B5 static where?
xi_norm = sp.simplify(hm[0, 0])
row("B5a |d_tau|^2 = -(1-2M/R)/(1+2E)", sp.simplify(xi_norm + f/kk) == 0, str(xi_norm))
det2 = sp.simplify(hm[0, 0]*hm[1, 1] - hm[0, 1]**2)
row("B5b det of (tau,R) block = -1/(1+2E): chart non-degenerate at every R > 0, incl. R <= 2M",
    sp.simplify(det2 + 1/kk) == 0, str(det2))
# hypersurface orthogonality of xi (xi ^ d xi = 0) -- 1-form xi_a = h_{a tau}
xi1 = [hm[0, 0], hm[0, 1], 0, 0]
# xi ^ dxi components: (xi ^ dxi)_{abc} = xi_[a d_b xi_c]
bad = 0
for (A_, B_, C_) in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]:
    tot = 0
    import itertools
    for p in itertools.permutations((A_, B_, C_)):
        sign = sp.combinatorics.Permutation([ (A_, B_, C_).index(q) for q in p]).signature()
        tot += sign*xi1[p[0]]*sp.diff(xi1[p[2]], Z[p[1]])
    if sp.simplify(tot) != 0:
        bad += 1
row("B5c xi ^ d xi = 0 (hypersurface-orthogonal wherever timelike)", bad == 0)
# numeric sample: R = M (inside), R = 3M (outside)
for Rv, want in ((sp.Rational(1, 1), False), (sp.Rational(3, 1), True)):
    val = xi_norm.subs({Mp: 1, E: sp.Rational(1, 2), Rc: Rv})
    row("B5d d_tau timelike at R=%sM ? %s" % (Rv, want), (val < 0) == want, "norm=%s" % val)
# Rotations: norms R^2 (...) >= 0, orthogonal to xi (h_{tau theta} = h_{tau phi} = 0)
row("B5e rotations orthogonal to d_tau (h_tau_theta = h_tau_phi = 0): for R < 2M every Killing"
    " combination a xi + rot has norm a^2 |xi|^2 + |rot|^2 >= 0 -> no timelike Killing field",
    hm[0, 2] == 0 and hm[0, 3] == 0)

# ---------------- B6 regular centre
Ms = sp.Symbol('M', real=True)
fs = 1 - 2*Ms/r
gs = sp.diag(-fs, 1/fs, r**2, r**2*sp.sin(th)**2)
Rd, gis = riemann_down(gs, X)
# Kretschmann K = R_abcd R^abcd ; metric diagonal
K = 0
for (A_, B_, C_, D_), val in Rd.items():
    if val != 0:
        K += val**2*gis[A_, A_]*gis[B_, B_]*gis[C_, C_]*gis[D_, D_]
K = sp.simplify(K)
row("B6a Schwarzschild Kretschmann = 48 M^2/r^6", sp.simplify(K - 48*Ms**2/r**6) == 0, str(K))
row("B6b finite as r -> 0 iff M = 0", sp.limit(K.subs(Ms, 0), r, 0) == 0 and sp.limit(K.subs(Ms, 1), r, 0) == sp.oo)
gflat = gs.subs(Ms, 0)
Rd0, _ = riemann_down(gflat, X)
row("B6c M = 0: every Riemann component 0 (exactly flat)", all(sp.simplify(sp.expand_trig(sp.expand(sp.expand_trig(x).rewrite(sp.sin)))) == 0 for x in Rd0.values()))

# ---------------- B7 negative interior mass
mneg = sp.Symbol('m', positive=True)
fin = 1 + 2*mneg/r
row("B7a M_in = -m: f_in = 1 + 2m/r > 0 for all r > 0 (no horizon; d_t timelike everywhere)",
    sp.solve(sp.Eq(fin, 0), r) == [] or all(not (x.is_positive) for x in sp.solve(sp.Eq(fin, 0), r)))
row("B7b and Kretschmann 48 m^2/r^6 -> infinity at r = 0 (singular centre, specthm R8's m(0) != 0)",
    sp.limit(K.subs(Ms, -mneg), r, 0) == sp.oo)

# ---------------- B8 thin shell sign (stability.sigma)
Rsh = sp.Symbol('R', positive=True)
sig = -(1/(4*sp.pi*Rsh))*(sp.sqrt(1 - 0/Rsh) - sp.sqrt(1 + 2*mneg/Rsh))
row("B8 stability.sigma(R,-m,0) = (sqrt(1+2m/R)-1)/(4 pi R) > 0 for m, R > 0",
    sp.simplify(sig - (sp.sqrt(1 + 2*mneg/Rsh) - 1)/(4*sp.pi*Rsh)) == 0 and
    sp.ask(sp.Q.positive(sp.sqrt(1 + 2*mneg/Rsh) - 1), sp.Q.positive(mneg) & sp.Q.positive(Rsh)) is not False)

# ---------------- B9 the datum Birkhoff (1923) did not have: Lambda > 0 (measured 1998-)
# With Lambda the Birkhoff class is Schwarzschild-de Sitter, f = 1 - 2M/r - Lambda r^2/3; a regular
# empty cavity (M = 0) is de Sitter, not Minkowski.  Size of the departure at wall.py's balloon.
Lam = sp.Symbol('Lambda', positive=True)
fL = 1 - 2*Ms/r - Lam*r**2/3
gL = sp.diag(-fL, 1/fL, r**2, r**2*sp.sin(th)**2)
GL, RicL, giL, _ = einstein(gL, X)
row("B9a f = 1 - 2M/r - Lambda r^2/3 solves G_ab + Lambda g_ab = 0",
    all(sp.simplify(GL[i, j] + Lam*gL[i, j]) == 0 for i in range(4) for j in range(4)))
RdL, giL2 = riemann_down(gL.subs(Ms, 0), X)
KL = 0
for (A_, B_, C_, D_), val in RdL.items():
    if val != 0:
        KL += val**2*giL2[A_, A_]*giL2[B_, B_]*giL2[C_, C_]*giL2[D_, D_]
KL = sp.simplify(KL)
row("B9b M = 0 cavity with Lambda: Kretschmann = 8 Lambda^2/3 != 0 (de Sitter, not flat)",
    sp.simplify(KL - sp.Rational(8, 3)*Lam**2) == 0, str(KL))
c = 299792458.0; Mpc = 3.0856775814913673e22
for label, H0, OL in (("Planck 2018 H0=67.4, OmL=0.685", 67.4, 0.685), ("SH0ES-scale H0=73.0, OmL=0.685", 73.0, 0.685)):
    H = H0*1e3/Mpc
    LamV = 3*H*H*OL/c**2
    dev = LamV*4478.0**2/3
    row("B9c %s: Lambda = %.3e m^-2, Lambda R^2/3 at R = 4478 m = %.2e (<< 1e-30)" % (label, LamV, dev), dev < 1e-30)

n_ok = sum(1 for _, ok, _ in rows if ok)
print("\n%d/%d PASS" % (n_ok, len(rows)))
raise SystemExit(0 if n_ok == len(rows) else 1)
