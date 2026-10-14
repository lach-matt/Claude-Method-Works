#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Fewster-Ford-Roman arXiv:1004.0179 note [18].

Checks, each printed PASS/FAIL:
 A  z3: (a) <=> (b) <=> (c) for a 3-level observable in its eigenbasis (every
    normalised psi = weights w on the simplex), with vacuity guards.
 B  numeric (mpmath): random Hermitian matrices, inf sigma = min Rayleigh
    quotient, mu_psi carried by the eigenvalues, Prob(outcome <= -D) = 0 when
    D > -inf sigma.  (finite-dimensional ILLUSTRATION of the spectral theorem)
 C  note [18]'s own caveat: psi orthogonal to the lowest eigenvector ->
    inf supp mu_psi > inf sigma(A).
 D  NARROWING of "decides": a valid but non-sharp bound Q decides
    Prob(outcome <= -D) = 0 only when D > Q; for D < Q it decides nothing.
 E  why (a) must hold on D(A) of the SELF-ADJOINT operator (H3): -d^2/dx^2 on
    (0,oo): form >= 0 on C_c^oo(0,oo), yet the Robin extension psi'(0)=a psi(0),
    a<0, has eigenvalue -a^2 < 0 (sympy, exact).
 F  integrity of the paper's own closed forms (eq. 22, 24, 26, Table I,
    P(negative)=0.89, 0.84, 0.95).
 G  the tree's datum Q = mu_1^4/(16 pi^2) hbar c / b^4 at b = 1 m and
    log10(D/Q) = 71.256 (SI 2019 exact h, c).
"""
import random, sys
import sympy as sp
import mpmath as mp

ok_all = True
def chk(name, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + (("  -- " + detail) if detail else ""))

# ---------------------------------------------------------------- A  z3
try:
    import z3
    l = [z3.Real("l%d" % i) for i in range(3)]
    w = [z3.Real("w%d" % i) for i in range(3)]
    Q = z3.Real("Q")
    simplex = z3.And(*[wi >= 0 for wi in w], z3.Sum(w) == 1)
    expv = z3.Sum([w[i] * l[i] for i in range(3)])
    b_ = z3.And(*[li >= -Q for li in l])                       # (b) spectrum in [-Q,oo)
    c_ = z3.And(*[z3.Implies(w[i] > 0, l[i] >= -Q) for i in range(3)])  # (c) supp mu_psi
    def prove(f):
        s = z3.Solver(); s.add(z3.Not(f)); r = s.check(); return r == z3.unsat
    # (b) => (c) for every psi
    chk("A1 z3 (b)=>(c) for every normalised psi", prove(z3.Implies(z3.And(simplex, b_), c_)))
    # (c) => (a): a random variable with values in [-Q,oo) has mean >= -Q
    chk("A2 z3 (c)=>(a)", prove(z3.Implies(z3.And(simplex, c_), expv >= -Q)))
    # (a) => (b): (a) at the three eigenvectors (unit weights) gives (b)
    at_unit = z3.And(*[l[i] >= -Q for i in range(3)])  # <e_i,A e_i> = l_i
    chk("A3 z3 (a) at eigenvectors => (b)", prove(z3.Implies(at_unit, b_)))
    # (a) for ALL psi => (b): quantified form
    wf = [z3.Real("v%d" % i) for i in range(3)]
    a_all = z3.ForAll(wf, z3.Implies(z3.And(*[x >= 0 for x in wf], z3.Sum(wf) == 1),
                                     z3.Sum([wf[i] * l[i] for i in range(3)]) >= -Q))
    chk("A4 z3 (forall psi: <A> >= -Q) => (b)", prove(z3.Implies(a_all, b_)))
    # vacuity guards: premises satisfiable, and conclusion not trivially true
    s = z3.Solver(); s.add(simplex, b_); chk("A5 guard: (b) & simplex satisfiable", s.check() == z3.sat)
    s = z3.Solver(); s.add(simplex, z3.Not(c_)); chk("A6 guard: (c) can fail", s.check() == z3.sat)
    # the single-psi converse is FALSE (note [18]'s caveat): supp mu_psi in [-Q,oo) for ONE psi does not give (b)
    s = z3.Solver(); s.add(simplex, c_, z3.Not(b_))
    chk("A7 single-psi (c) does NOT imply (b) (counterexample exists)", s.check() == z3.sat,
        str(s.model()) if s.check() == z3.sat else "")
except ImportError:
    chk("A z3 available", False, "pip install z3-solver")

# ---------------------------------------------------------------- B  numeric
mp.mp.dps = 30
random.seed(67)
def rand_herm(n):
    M = mp.matrix(n, n)
    for i in range(n):
        M[i, i] = mp.mpf(random.uniform(-3, 3))
        for j in range(i + 1, n):
            z = mp.mpc(random.uniform(-1, 1), random.uniform(-1, 1))
            M[i, j] = z; M[j, i] = mp.conj(z)
    return M
worst = mp.mpf(0)
for trial in range(40):
    n = random.randint(2, 6)
    A = rand_herm(n)
    E, V = mp.eighe(A)
    lmin = min(E)
    for k in range(20):
        psi = mp.matrix([mp.mpc(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(n)])
        nrm = mp.sqrt(sum(abs(x) ** 2 for x in psi)); psi = psi / nrm
        ray = mp.re(sum(mp.conj(psi[i]) * sum(A[i, j] * psi[j] for j in range(n)) for i in range(n)))
        # spectral measure weights
        wts = [abs(sum(mp.conj(V[i, m]) * psi[i] for i in range(n))) ** 2 for m in range(n)]
        mean = sum(wts[m] * E[m] for m in range(n))
        worst = max(worst, abs(mean - ray), abs(sum(wts) - 1))
        if ray < lmin - mp.mpf(10) ** -25:
            worst = mp.mpf(1)
        D = -lmin + mp.mpf("0.1")
        P = sum(wts[m] for m in range(n) if E[m] <= -D)
        if P != 0:
            worst = mp.mpf(1)
chk("B random Hermitian: <psi,A psi> >= inf sigma, mu_psi on eigenvalues, P(<= -D)=0 for D > -inf sigma",
    worst < mp.mpf(10) ** -20, "max residual %s" % mp.nstr(worst, 3))

# ---------------------------------------------------------------- C  caveat
A = sp.diag(-2, 1, 3)
psi = sp.Matrix([0, 1, 1]) / sp.sqrt(2)
w = [(psi[i]) ** 2 for i in range(3)]
supp = [A[i, i] for i in range(3) if w[i] != 0]
chk("C psi orthogonal to lowest eigenvector: inf supp mu_psi = %s > inf sigma = %s" % (min(supp), -2),
    min(supp) > -2)

# ---------------------------------------------------------------- D  narrowing of "decides"
# A with inf sigma = -1; an ABSOLUTE bound Q = 2 is valid (-1 >= -2) but not sharp.
A = sp.diag(-1, 0, 5); Qb = 2
psi = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
w = [psi[i] ** 2 for i in range(3)]
def prob_le(Dv): return sum(w[i] for i in range(3) if A[i, i] <= -Dv)
decided_zero = lambda Dv: Dv > Qb                        # what note [18] + the bound can conclude
chk("D1 D=3 > Q=2: bound decides P=0, and P=%s" % prob_le(3), decided_zero(3) and prob_le(3) == 0)
chk("D2 D=1.5 < Q: bound silent, true P=%s (zero)" % prob_le(sp.Rational(3, 2)),
    (not decided_zero(sp.Rational(3, 2))) and prob_le(sp.Rational(3, 2)) == 0)
chk("D3 D=0.5 < Q: bound silent, true P=%s (NONZERO)" % prob_le(sp.Rational(1, 2)),
    (not decided_zero(sp.Rational(1, 2))) and prob_le(sp.Rational(1, 2)) > 0)

# ---------------------------------------------------------------- E  self-adjoint extension matters
x = sp.symbols("x", positive=True); a = sp.symbols("a", negative=True)
f = sp.exp(a * x)
chk("E1 Robin eigenvector satisfies psi'(0) = a psi(0)", sp.simplify(sp.diff(f, x).subs(x, 0) - a * f.subs(x, 0)) == 0)
chk("E2 -psi'' = -a^2 psi (eigenvalue -a^2 < 0)", sp.simplify(-sp.diff(f, x, 2) + a ** 2 * f) == 0)
chk("E3 psi in L^2(0,oo): ||psi||^2 = %s" % sp.integrate(f ** 2, (x, 0, sp.oo)),
    sp.integrate(f ** 2, (x, 0, sp.oo)) == -1 / (2 * a))
# form on C_c^oo(0,oo): <psi,-psi''> = INT psi'^2 >= 0 (boundary term vanishes); test on a bump
t = sp.symbols("t")
bump = (x - 1) ** 2 * (x - 2) ** 2  # C^1 compactly supported piece on [1,2] (form domain element)
form = sp.integrate(sp.diff(bump, x) ** 2, (x, 1, 2))
ibp = sp.integrate(-sp.diff(bump, x, 2) * bump, (x, 1, 2))
chk("E4 core form >= 0 and equals <psi,-psi''> (no boundary term): %s = %s" % (form, ibp), form == ibp and form > 0)
# Rayleigh quotient of the Robin eigenvector is the negative eigenvalue
num = sp.integrate(sp.diff(f, x) ** 2, (x, 0, sp.oo)) + a * f.subs(x, 0) ** 2
chk("E5 Robin form <f,Af>/<f,f> = %s = -a^2" % sp.simplify(num / sp.integrate(f ** 2, (x, 0, sp.oo))),
    sp.simplify(num / sp.integrate(f ** 2, (x, 0, sp.oo)) + a ** 2) == 0)

# ---------------------------------------------------------------- F  paper's own closed forms
u, tau, c = sp.symbols("u tau c", positive=True)
fG = sp.exp(-u ** 2 / tau ** 2) / (tau * sp.sqrt(sp.pi))
bound24 = sp.simplify(c / (12 * sp.pi) * sp.integrate(sp.diff(sp.sqrt(fG), u) ** 2, (u, -sp.oo, sp.oo)))
chk("F1 eq.(24): c/(12pi) INT ((sqrt f)')^2 = %s = c/(24 pi tau^2)" % bound24,
    sp.simplify(bound24 - c / (24 * sp.pi * tau ** 2)) == 0)
om = sp.symbols("omega", real=True)
G2 = sp.simplify(c / (48 * sp.pi ** 2) * sp.integrate(om ** 3 * sp.exp(-om ** 2 * tau ** 2 / 2), (om, 0, sp.oo)))
chk("F2 eq.(18): G2[f] = %s = c/(24 pi^2 tau^4)" % G2, sp.simplify(G2 - c / (24 * sp.pi ** 2 * tau ** 4)) == 0)
alpha, beta, om0 = c / 24, sp.pi * tau ** 2, c / (24 * sp.pi * tau ** 2)
chk("F3 eq.(22): shifted-Gamma mean alpha/beta - omega_0 = 0 (vacuum mean zero)",
    sp.simplify(alpha / beta - om0) == 0)
chk("F4 eq.(22): variance alpha/beta^2 = G2[f]", sp.simplify(alpha / beta ** 2 - G2) == 0)
mp.mp.dps = 20
Pneg = lambda al, x0: mp.gammainc(al, 0, x0, regularized=True)
p_flux = Pneg(mp.mpf(1) / 24, mp.mpf(1) / 24)
p_rho = Pneg(mp.mpf(1) / 12, mp.mpf(1) / 12)
p_phi2 = Pneg(mp.mpf(1) / 72, mp.mpf(1) / 72)
chk("F5 P(negative) flux c=1 = %s (paper 0.89)" % mp.nstr(p_flux, 4), abs(p_flux - 0.89) < 0.005)
chk("F6 P(negative) energy density c=1 = %s (paper 0.84)" % mp.nstr(p_rho, 4), abs(p_rho - 0.84) < 0.005)
chk("F7 P(negative) Lorentzian :phi^2: = %s (paper 0.95)" % mp.nstr(p_phi2, 4), abs(p_phi2 - 0.95) < 0.005)
# Table I: Y = (4 pi tau)^2 X, X ~ shifted Gamma(alpha=1/72, rate beta=4 pi^2 tau^2/3) -> Y rate 1/12, mean 0
al, rate = sp.Rational(1, 72), sp.Rational(1, 12)
kap = [0] + [al * sp.factorial(n - 1) / rate ** n for n in range(1, 9)]
kap[1] = 0  # shift removes the mean
# moments from cumulants
mom = [sp.Integer(1)]
for n in range(1, 9):
    mom.append(sum(sp.binomial(n - 1, k - 1) * kap[k] * mom[n - k] for k in range(1, n + 1)))
table = [1, 0, 2, 48, 1740, 83904, 5051640, 364724928, 30707616912]
chk("F8 Table I moments reproduced by eq.(26): %s" % [int(m) for m in mom], [int(m) for m in mom] == table)
chk("F9 eq.(26) consistency: beta*omega_0 = alpha = 1/72",
    sp.simplify(4 * sp.pi ** 2 * tau ** 2 / 3 / (96 * sp.pi ** 2 * tau ** 2) - sp.Rational(1, 72)) == 0)

# ---------------------------------------------------------------- G  tree datum
mp.mp.dps = 30
mu1 = mp.findroot(lambda m: mp.cos(m) * mp.cosh(m) - 1, 4.73)
h = mp.mpf("6.62607015e-34"); cl = mp.mpf(299792458)
hbarc = h / (2 * mp.pi) * cl
Qtree = mu1 ** 4 / (16 * mp.pi ** 2) * hbarc / mp.mpf(1) ** 4
Qtree_hbar = mu1 ** 4 / (16 * mp.pi ** 2) * mp.mpf("1.054571817e-34") * cl   # achievable.py:299 HBAR
chk("G1a with the tree's HBAR = 1.054571817e-34 (achievable.py:299): Q = %s Pa (tree 1.002159073400914e-25)"
    % mp.nstr(Qtree_hbar, 16), abs(Qtree_hbar / mp.mpf("1.002159073400914e-25") - 1) < 1e-14,
    "mu1=%s" % mp.nstr(mu1, 16))
chk("G1b with exact SI-2019 hbar = h/2pi: Q = %s Pa; relative move %s (DISCREPANCY of rounding only)"
    % (mp.nstr(Qtree, 16), mp.nstr(Qtree / Qtree_hbar - 1, 3)), abs(Qtree / Qtree_hbar - 1) < 1e-9)
Dt = mp.mpf("1.8057952075209083e46")
chk("G2 log10(D/Q) = %s (tree 71.256)" % mp.nstr(mp.log10(Dt / Qtree), 8), abs(mp.log10(Dt / Qtree) - 71.256) < 5e-4)
chk("G3 D > Q, so under H1-H6 note [18] gives Prob(outcome <= -D) = 0", Dt > Qtree)

print("ALL PASS" if ok_all else "SOME FAIL")
sys.exit(0 if ok_all else 1)
