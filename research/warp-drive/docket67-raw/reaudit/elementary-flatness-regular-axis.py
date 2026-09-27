#!/usr/bin/env python3
"""DOCKET 67 re-audit: elementary-flatness-regular-axis against Mars & Senovilla (arXiv gr-qc/0201045v1,
dated 23 October 1992; the preprint of CQG 10 (1993) 1633), READ in full (18 pp.) via Google Drive.

  M1  M&S Property 5, grad(sigma^2).grad(sigma^2)/(4 sigma^2) -> 1 at the axis, for the owner's metric
      (sigma = d/dphi, sigma^2 = W^2, g^rr = e^{-2 Lambda}):  quantity = e^{-2Lambda} W'^2;  Lambda = 0: W'(0)^2.
  M2  M&S Property 3 / 'standard parametrization ... phi goes from 0 to 2 pi ... effective ... a = 1':
      for the flat 2-metric dr^2 + W1^2 r^2 dphi^2 the flow of d/dphi rotates the tangent plane at the
      axis at rate a = W1 (Cartesian Jacobian of x = r cos(W1 phi), y = r sin(W1 phi)); d tau_{2pi} = Id and
      effectiveness force a = 1, i.e. W'(0) = 1 exactly when phi has period 2 pi.  With period 2 pi k the
      condition is k W'(0) = 1.
  M3  M&S end of Sec. 2: orbit length / (2 pi x distance to axis) -> 1 at first order  <=>  W'(0) = 1.
  M4  (COMPUTED here, NOT a statement of M&S) smoothness at a genuine axis makes every axially invariant
      metric function a smooth function of x^2 + y^2 = r^2; for g_zz = e^{2 Psi} = f(r^2) this gives
      Psi'(r) = O(r), hence W Psi' -> 0 at r = 0.  The owner's axis-end boundary term therefore vanishes
      under M&S's hypotheses, but NOT under the owner's HYPOTHESES[0] alone (W(0)=0, W'(0)=1): a
      counterexample Psi = a log(r/(1+r)) keeps W'(0)=1 and has W Psi' -> a.
  M5  M&S Property 2 (axis autoparallel) and Property 4 (sigma^2 >= 0 near the axis) hold for the owner's
      W with W(0) = 0, W'(0) = 1 (sigma^2 = W^2 = r^2 + O(r^3)).
Exit 0 iff all pass.
"""
import sys
import sympy as sp

ok = []
def chk(name, cond, extra=""):
    ok.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name + (("   " + extra) if extra else ""))

r, phi, k, a = sp.symbols('r phi k a', positive=True)
W = sp.Function('W'); Lam = sp.Function('Lambda'); Psi = sp.Function('Psi')

# M1
X = W(r)**2
q = sp.exp(-2*Lam(r))*sp.diff(X, r)**2/(4*X)
chk("M1 grad X.grad X/(4X) = e^{-2Lambda} W'^2", sp.simplify(q - sp.exp(-2*Lam(r))*sp.diff(W(r), r)**2) == 0)
chk("M1 Lambda = 0: quantity -> W'(0)^2, so Property 5 <=> W'(0) = +1 (W > 0 off axis)",
    sp.simplify(q.subs(Lam(r), 0) - sp.diff(W(r), r)**2) == 0)

# M2: rotation rate of the d/dphi flow on the tangent plane at the axis for dr^2 + W1^2 r^2 dphi^2.
W1 = sp.symbols('W1', positive=True)
x = r*sp.cos(W1*phi); y = r*sp.sin(W1*phi)      # local Cartesian chart in which the 2-metric is dx^2+dy^2
# the flow phi -> phi + s acts on (x, y) as rotation by angle W1*s: check
s = sp.symbols('s')
xs = r*sp.cos(W1*(phi+s)); ys = r*sp.sin(W1*(phi+s))
Rot = sp.Matrix([[sp.cos(W1*s), -sp.sin(W1*s)], [sp.sin(W1*s), sp.cos(W1*s)]])
chk("M2 d/dphi flow = rotation by angle W1*s in the local Cartesian chart (rate a = W1)",
    sp.simplify(sp.Matrix([xs, ys]) - Rot*sp.Matrix([x, y])) == sp.zeros(2, 1))
flat = sp.simplify(sp.diff(x, r)**2 + sp.diff(y, r)**2), sp.simplify(sp.diff(x, phi)**2 + sp.diff(y, phi)**2)
chk("M2 chart check: dx^2+dy^2 = dr^2 + W1^2 r^2 dphi^2", flat[0] == 1 and sp.simplify(flat[1] - W1**2*r**2) == 0)
# d tau_{2 pi} = Id  <=> W1 integer; effective (no 0 < s < 2 pi with Rot = Id) <=> W1 = 1
def identity_at(w, s_):
    return sp.simplify(Rot.subs({W1: w, s: s_}) - sp.eye(2)) == sp.zeros(2, 2)
chk("M2 W1 = 1: d tau_{2pi} = Id and effective", identity_at(1, 2*sp.pi) and not identity_at(1, sp.pi))
chk("M2 W1 = 1/2 (period-2pi cone of deficit pi): d tau_{2pi} != Id -> not a smooth axis",
    not identity_at(sp.Rational(1, 2), 2*sp.pi))
chk("M2 W1 = 2: d tau_{2pi} = Id but NOT effective (d tau_pi = Id)", identity_at(2, 2*sp.pi) and identity_at(2, sp.pi))
# with period 2 pi k, the normalised generator is k d/dphi and its rate is k*W1
chk("M2 period 2 pi k: normalised rate k W'(0), condition k W'(0) = 1",
    sp.simplify((k*W1).subs(W1, 1/k) - 1) == 0)

# M3
Wt = r + sp.Symbol('b')*r**2 + sp.Symbol('c')*r**3        # W(0)=0, W'(0)=1
ratio = sp.limit(2*sp.pi*Wt/(2*sp.pi*r), r, 0)
chk("M3 orbit length / (2 pi distance) -> W'(0) = 1", ratio == 1)
Wc = sp.Rational(9, 10)*r
chk("M3 cone W = 0.9 r: ratio -> 0.9 (deficit 0.2 pi)", sp.limit(2*sp.pi*Wc/(2*sp.pi*r), r, 0) == sp.Rational(9, 10))

# M4 (computed, not M&S): g_zz = f(r^2) smooth -> Psi' = O(r)
f = sp.Function('f'); u = sp.symbols('u', positive=True)
PsiS = sp.log(f(r**2))/2
dPsi = sp.diff(PsiS, r)
chk("M4 Psi = (1/2) ln f(r^2): Psi' = r f'(r^2)/f(r^2) = O(r)",
    sp.simplify(dPsi - r*sp.Subs(sp.Derivative(f(u), u), u, r**2).doit()/f(r**2)) == 0)
fex = 1 + 3*u + u**2                                        # a concrete smooth positive f
WPsi_smooth = sp.limit((r*sp.diff(sp.log(fex.subs(u, r**2))/2, r)), r, 0)
chk("M4 example f = 1 + 3 r^2 + r^4, W = r: W Psi' -> 0", WPsi_smooth == 0)
aa = sp.Rational(3, 10)
PsiBad = aa*sp.log(r/(1+r))
WPsi_bad = sp.limit(r*sp.diff(PsiBad, r), r, 0)
chk("M4 owner's HYPOTHESES[0] alone does not give it: Psi = a log(r/(1+r)), W = r -> W Psi' -> a = 0.3",
    WPsi_bad == aa)
chk("M4 and that Psi is not a smooth function of r^2 at the axis (Psi -> -inf)", sp.limit(PsiBad, r, 0) == -sp.oo)

# M5
chk("M5 sigma^2 = W^2 = r^2 + O(r^3) >= 0 near axis, zero only at r = 0 (Property 4)",
    sp.series(Wt**2, r, 0, 3).removeO() == r**2)

n = sum(ok); print("\n%d/%d PASS" % (n, len(ok)))
sys.exit(0 if n == len(ok) else 1)
