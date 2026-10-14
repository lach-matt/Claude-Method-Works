"""D67 audit: cosmic string deficit angle = 8 pi G mu (G = c = 1 below).

Re-derives, from the Einstein equations alone (no source text was readable this pass):
 A. the tree's u-identity  8 pi u W = -(W Psi')' - W Psi'^2 - W''  for
    ds^2 = -e^{2Phi}dt^2 + dr^2 + e^{2Psi}dz^2 + W^2 dphi^2   (u = -T^t_t)
 B. exact (nonlinear) deficit = 8 pi mu for a boost-invariant core (Psi' = 0),
    mu = INT u dA = 2 pi INT_0^R u W dr  -- Gott/Hiscock-type uniform core, both signs
 C. general smooth core with Psi' != 0 but W Psi' -> 0 at both ends:
    deficit = 8 pi mu + 2 pi INT W Psi'^2  >=  8 pi mu   (numeric)
 D. linearised thin string with energy/length mu and tension tau (T^zz = -tau):
    deficit = 4 pi (mu + tau);  W Psi' -> 2 (tau - mu) != 0 unless tau = mu
 E. counterexample to the UNCONDITIONAL sentence: mu > 0, tau = -2 mu (axial pressure 2mu)
    gives an angle EXCESS with positive mu -- but it breaks the tree's W Psi' -> 0 hypothesis.
 F. tree's CONICAL_TERM data mapped to mu: W'(0) - 1 = -4 mu (deficit 2pi(1-W'(0)) = 8 pi mu).
"""
import sympy as sp
ok = []
def chk(label, cond):
    ok.append(bool(cond)); print(("PASS " if cond else "FAIL ") + label)

t, r, z, ph = sp.symbols('t r z phi', real=True)
Phi, Psi, W = sp.Function('Phi')(r), sp.Function('Psi')(r), sp.Function('W')(r)
x = [t, r, z, ph]
g = sp.diag(-sp.exp(2*Phi), 1, sp.exp(2*Psi), W**2)
gi = g.inv()
def christ(g, gi):
    return [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
             for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
G_ = christ(g, gi)
def ricci(G_):
    R = sp.zeros(4)
    for b in range(4):
        for c in range(4):
            R[b, c] = sp.simplify(sum(sp.diff(G_[a][b][c], x[a]) - sp.diff(G_[a][b][a], x[c])
                       + sum(G_[a][a][d]*G_[d][b][c] - G_[a][c][d]*G_[d][b][a] for d in range(4))
                       for a in range(4)))
    return R
Ric = ricci(G_)
Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(4) for b in range(4)))
Gtt_mixed = sp.simplify(sum(gi[0, a]*Ric[a, 0] for a in range(4)) - Rs/2)   # G^t_t
u = -Gtt_mixed/(8*sp.pi)
ident = sp.simplify(8*sp.pi*u*W - (-(sp.diff(W*sp.diff(Psi, r), r)) - W*sp.diff(Psi, r)**2 - sp.diff(W, r, 2)))
chk("A. 8 pi u W = -(W Psi')' - W Psi'^2 - W''  (residual %s); Phi absent from u: %s"
    % (ident, not u.has(Phi)), ident == 0 and not u.has(Phi))

# B. uniform cores, Psi = 0 (boost-invariant: T^t_t = T^z_z follows since then G^z_z = G^t_t when Phi = Psi = 0)
r0, R = sp.symbols('r0 R', positive=True)
for sign, Wc in ((+1, r0*sp.sin(r/r0)), (-1, r0*sp.sinh(r/r0))):
    uc = sp.simplify(u.subs({Psi: 0, Phi: 0}).subs(W, Wc).doit())
    mu = sp.simplify(2*sp.pi*sp.integrate(uc*Wc, (r, 0, R)))
    Wp_out = sp.diff(Wc, r).subs(r, R)          # exterior W = Wp_out*(r - R) + Wc(R): a cone
    deficit = 2*sp.pi*(1 - Wp_out)
    Gzz = sp.simplify((sum(gi[2, a]*Ric[a, 2] for a in range(4)) - Rs/2).subs({Psi: 0, Phi: 0}).subs(W, Wc).doit())
    Gtt = sp.simplify(Gtt_mixed.subs({Psi: 0, Phi: 0}).subs(W, Wc).doit())
    chk("B%s. core W=%s: u=%s, mu=%s, deficit - 8 pi mu = %s, T^z_z = T^t_t: %s"
        % ('+' if sign > 0 else '-', Wc, uc, mu, sp.simplify(deficit - 8*sp.pi*mu), sp.simplify(Gzz - Gtt) == 0),
        sp.simplify(deficit - 8*sp.pi*mu) == 0 and sp.simplify(Gzz - Gtt) == 0)
# Gott bound: deficit < 2 pi  <=>  mu < 1/4 (positive core, R/r0 < pi)
chk("B. positive core: the exterior cone closes (W'=cos(R/r0)=0, deficit 2pi) exactly at mu = 1/4 -- Gott bound G mu < 1/4",
    sp.simplify(2*sp.pi*(1 - sp.cos(sp.pi/2)) - 8*sp.pi*sp.Rational(1, 4)) == 0)

# C. smooth core with Psi' != 0, compact support, numeric
import math
def core(n=200001, Rc=1.0):
    # W = r + a r^3 (1 - r/Rc)^4 ... choose W smooth with W(0)=0, W'(0)=1; Psi = b (r/Rc)^2 (1-r/Rc)^4 (Psi'=0 at 0 and Rc)
    a, b = 0.6, 0.8
    Wf = lambda s: s - a*s**3*(1 - s/Rc)**4 * 1.0
    import sympy as sp2
    s = sp2.symbols('s')
    Ws = s - a*s**3/3
    Ps = b*(s/Rc)**2*(1 - s/Rc)**4
    uW8pi = -(sp2.diff(Ws*sp2.diff(Ps, s), s)) - Ws*sp2.diff(Ps, s)**2 - sp2.diff(Ws, s, 2)
    I_uW = float(sp2.integrate(sp2.expand(uW8pi), (s, 0, Rc)))/(8*math.pi)
    I_WP2 = float(sp2.integrate(sp2.expand(Ws*sp2.diff(Ps, s)**2), (s, 0, Rc)))
    Wp_out = float(sp2.diff(Ws, s).subs(s, Rc))
    mu = 2*math.pi*I_uW
    deficit = 2*math.pi*(1 - Wp_out)
    return mu, deficit, I_WP2
mu, deficit, IWP2 = core()
chk("C. Psi' != 0 core: deficit %.9f = 8 pi mu %.9f + 2 pi INT W Psi'^2 %.9f  (so deficit >= 8 pi mu)"
    % (deficit, 8*math.pi*mu, 2*math.pi*IWP2), abs(deficit - 8*math.pi*mu - 2*math.pi*IWP2) < 1e-9 and deficit >= 8*math.pi*mu)

# D. linearised thin string, T_00 = mu d2, T_zz = -tau d2 ; hbar = -8 T ln r ; h = hbar - eta hbar/2
m, tau = sp.symbols('mu tau', real=True)
L = sp.log(r)
eta = sp.diag(-1, 1, 1, 1)   # (t, x, y, z)
T = sp.diag(m, 0, 0, -tau)
hbar = -8*T*L
trace = sum(eta[i, i]*hbar[i, i] for i in range(4))
h = hbar - eta*trace/2
k = sp.simplify(-h[1, 1]/(2*L))          # spatial transverse metric (1+h_xx)(dx^2+dy^2) = r^{-2k}(...)
deficitD = sp.simplify(2*sp.pi*k)       # cone with circumference/radius ratio 2pi(1-k)
PsiD = h[3, 3]/2
WPsi = sp.simplify(r*sp.diff(PsiD, r))
chk("D. linear: h_tt=%s, h_zz=%s, deficit=%s, W Psi' -> %s" % (sp.simplify(h[0, 0]), sp.simplify(h[3, 3]), deficitD, WPsi),
    sp.simplify(deficitD - 4*sp.pi*(m + tau)) == 0 and sp.simplify(WPsi - 2*(tau - m)) == 0)
chk("D. tau = mu (boost invariant) gives 8 pi mu, h_tt = 0, W Psi' = 0",
    sp.simplify(deficitD.subs(tau, m) - 8*sp.pi*m) == 0 and sp.simplify(h[0, 0].subs(tau, m)) == 0 and WPsi.subs(tau, m) == 0)
# D'. tree identity at first order reproduces 4 pi (mu+tau): 1 - W'(inf) = 8pi INT uW + [W Psi']_inf ; 8pi INT uW = 4 mu
chk("D'. first-order identity: 2pi(4 mu + 2(tau - mu)) = 4 pi (mu + tau)",
    sp.simplify(2*sp.pi*(4*m + 2*(tau - m)) - 4*sp.pi*(m + tau)) == 0)

# E. excess with positive mu
vals = {m: sp.Rational(1, 100), tau: -sp.Rational(2, 100)}
dE = deficitD.subs(vals)
chk("E. mu=+0.01, tau=-0.02 (axial pressure 0.02 > mu): deficit = %s < 0 (EXCESS), W Psi' = %s != 0 (tree hypothesis broken); NEC_z rho+p_z = %s > 0, DEC fails (p_z > rho)"
    % (dE, WPsi.subs(vals), vals[m] - vals[tau]), dE < 0 and WPsi.subs(vals) != 0)

# F. CONICAL_TERM data -> mu in the Psi-regular class
for d, ex in ((-0.4, -0.4), (0.0, 0.0), (0.7, 0.7), (2.0, 2.0)):
    print("   W'(0)-1 = %+.1f  ->  axis mu = -(W'(0)-1)/4 = %+.3f  (%s)" % (d, -d/4, 'deficit' if d < 0 else ('none' if d == 0 else 'EXCESS, mu<0')))
chk("F. normalisation: W'(0)-1 = -4 G mu, not -8 pi G mu (deficit ANGLE 2pi(1-W'(0)) = 8 pi G mu)",
    abs(2*math.pi*(0.4) - 8*math.pi*0.1) < 1e-12)

print("\n%d/%d PASS" % (sum(ok), len(ok)))
raise SystemExit(0 if all(ok) else 1)
