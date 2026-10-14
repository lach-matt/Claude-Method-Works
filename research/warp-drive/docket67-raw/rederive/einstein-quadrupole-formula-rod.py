#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key einstein-quadrupole-formula-rod.

Independent of branelink.py's verify_symbolic: the rod is built from a line
density (not from I = M l^2/12 typed in), the luminosity is evaluated in BOTH
forms of the quadrupole formula as restated in Gerosa's lecture notes L02 p6
(Maggiore eq. 3.75): P = G/5c^5 <Q'''_ij Q'''_ij> = G/5c^5 <M'''_ij M'''_ij - (1/3) M'''_kk^2>,
cross-checked against the binary result P = (32/5) mu^2 R^4 w^6 (L03 p3) and the
binary emission pattern dP/dOmega ~ [((1+cos^2)/2)^2 + cos^2] (L03 p2).
Exit 1 on any failed check.  sympy only.
"""
import sys
import sympy as sp

ok = True
def chk(label, cond, extra=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + label + ((" -- " + extra) if extra else ""))

t, W, M, l, G, c, s, a = sp.symbols('t Omega M ell G c s a', positive=True)
n = sp.Matrix([sp.cos(W*t), sp.sin(W*t), 0])
lam = M / l
# (1) rod from line density: M_ij = int lam s^2 n_i n_j ds
Mij = sp.integrate(lam * s**2, (s, -l/2, l/2)) * (n * n.T)
chk("second moment of a thin uniform rod = M l^2/12", sp.simplify(Mij[0, 0].subs(t, 0) - M*l**2/12) == 0)
Q = Mij - sp.eye(3) * Mij.trace() / 3
d3 = lambda X: X.applyfunc(lambda e: sp.diff(e, t, 3))
Q3, M3 = d3(Q), d3(Mij)
T = 2*sp.pi/W
avg = lambda e: sp.simplify(sp.integrate(sp.expand(sp.expand_trig(e)), (t, 0, T)) / T)
PQ = G/(5*c**5) * avg(sum(Q3[i, j]**2 for i in range(3) for j in range(3)))
PM = G/(5*c**5) * avg(sum(M3[i, j]**2 for i in range(3) for j in range(3)) - M3.trace()**2/3)
unit = G*M**2*l**4*W**6/c**5
chk("traceless form: P / (G M^2 l^4 W^6/c^5) = 2/45", sp.simplify(PQ/unit - sp.Rational(2, 45)) == 0, str(sp.simplify(PQ/unit)))
chk("trace-subtracted form (L02 3.75, 2nd line) agrees", sp.simplify(PM - PQ) == 0)
# (2) binary map: (32/5) G mu^2 R^4 w^6 / c^5 with mu R^2 -> M l^2/12
mu, R = sp.symbols('mu R', positive=True)
Pbin = sp.Rational(32, 5) * G * mu**2 * R**4 * W**6 / c**5
chk("binary (32/5) with mu R^2 = M l^2/12 gives 2/45",
    sp.simplify(Pbin.subs(mu, M*l**2/(12*R**2)) / unit - sp.Rational(2, 45)) == 0)
# (3) omega_GW = 2 Omega: Fourier content of Q_xx
F1 = sp.simplify(sp.integrate(sp.expand(sp.expand_trig(Q[0, 0]*sp.cos(W*t))), (t, 0, T)))
F2 = sp.simplify(sp.integrate(sp.expand(sp.expand_trig(Q[0, 0]*sp.cos(2*W*t))), (t, 0, T)))
chk("Q_xx has zero Fourier weight at Omega", F1 == 0)
chk("Q_xx has non-zero weight at 2 Omega", F2 != 0, str(F2))
# (4) angular pattern: face-on over isotropic
th, ph = sp.symbols('theta phi', real=True)
pat = ((1 + sp.cos(th)**2)/2)**2 + sp.cos(th)**2
mean = sp.simplify(sp.integrate(pat*sp.sin(th), (th, 0, sp.pi))*2*sp.pi / (4*sp.pi))
chk("pattern mean over sphere = 4/5", sp.simplify(mean - sp.Rational(4, 5)) == 0)
face = pat.subs(th, 0) / mean
chk("face-on flux / isotropic L/(4 pi D^2) = 5/2", sp.simplify(face - sp.Rational(5, 2)) == 0)
edge = pat.subs(th, sp.pi/2) / mean
chk("edge-on flux / isotropic = 5/16 (bits range x5/16..x5/2 = -0.505..+0.398 dex)", sp.simplify(edge - sp.Rational(5, 16)) == 0,
    "%.3f..%.3f dex" % (float(sp.log(edge, 10)), float(sp.log(face, 10))))
# normalisation of the READ pattern: 2 mu^2 R^4 w^6/pi * pat integrates to (32/5) mu^2 R^4 w^6 (G=c=1)
tot = sp.simplify(sp.integrate(2*mu**2*R**4*W**6/sp.pi*pat*sp.sin(th), (th, 0, sp.pi))*2*sp.pi)
chk("L03 dP/dOmega integrates to L03 P = (32/5) mu^2 R^4 w^6", sp.simplify(tot - sp.Rational(32, 5)*mu**2*R**4*W**6) == 0)
# (5) the tree's strain relation vs the on-axis amplitude
D, w, h, L = sp.symbols('D omega h L', positive=True)
h_tree = 2/(D*w)*sp.sqrt(G*L/c**3)
A = M*l**2/12
Lrod = sp.Rational(2, 45)*unit
h_tree_rod = sp.simplify(h_tree.subs({L: Lrod, w: 2*W}))
# on-axis: h = (2G/(c^4 D)) * amplitude of Mddot_xx, Mddot_xx = -2 A W^2 cos 2Wt
amp = sp.simplify(sp.Abs(sp.diff(Mij[0, 0], t, 2).subs(t, 0)))
h_axis = 2*G/(c**4*D) * amp
r = sp.simplify(h_axis / h_tree_rod)
chk("on-axis h / tree h = sqrt(5/2)", sp.simplify(r - sp.sqrt(sp.Rational(5, 2))) == 0, str(r))
# circular-polarisation flux identity used by the tree: <hdot+^2 + hdotx^2> = w^2 h^2
flux = c**3/(16*sp.pi*G) * avg((sp.diff(h*sp.cos(w*t), t))**2 + (sp.diff(h*sp.sin(w*t), t))**2).subs(W, w)
chk("flux c^3/(16 pi G)<hd+^2+hdx^2> = c^3 w^2 h^2/(16 pi G) for circular pol.",
    sp.simplify(flux - c**3*w**2*h**2/(16*sp.pi*G)) == 0)
# (6) the 2x / 4x correction: h ~ 1/w, bits ~ 1/w^2
chk("h(w=Omega)/h(w=2 Omega) = 2", sp.simplify(h_tree.subs(w, W)/h_tree.subs(w, 2*W)) == 2)
bits = 4*G/(D**2*c**3*w**2)
chk("bits(w=Omega)/bits(w=2 Omega) = 4", sp.simplify(bits.subs(w, W)/bits.subs(w, 2*W)) == 4)
# (7) thin-rod hypothesis: solid cylinder of radius a -> radiating amplitude (I_xx - I_yy)
Iyy = M*a**2/4
fac = sp.simplify(((M*l**2/12 - Iyy)/(M*l**2/12))**2)
chk("finite radius: L multiplied by (1 - 3 a^2/l^2)^2", sp.simplify(fac - (1 - 3*a**2/l**2)**2) == 0)
# (8) numbers at the design point
Gn, cn = 6.67430e-11, 299792458.0
Mn, ln, Wn = 1.0e6, 100.0, 100.0
Ln = 2/45*Gn*Mn**2*ln**4*Wn**6/cn**5
print("L_GW design point = %.6e W" % Ln)
chk("matches branelink.rod_luminosity 1.2249537481616383e-22", abs(Ln/1.2249537481616383e-22 - 1) < 1e-12)
Dn = 4.017499195181437e16
hn = 2/(Dn*2*Wn)*(Gn*Ln/cn**3)**0.5
print("h (isotropic, tree) = %.6e ; on-axis = %.6e" % (hn, hn*2.5**0.5))
chk("tree h reproduced 4.3359e-48", abs(hn/4.3359e-48 - 1) < 1e-4)
v = Wn*ln/2/cn; lamgw = 2*3.141592653589793*cn/(2*Wn)
print("slow motion v_tip/c = %.3e ; lambda_GW/l = %.3e ; GM/(l c^2) = %.3e" % (v, lamgw/ln, Gn*Mn/(ln*cn**2)))
chk("slow-motion / long-wavelength / weak-field hypotheses satisfied by >1e4", v < 1e-4 and lamgw/ln > 1e4 and Gn*Mn/(ln*cn**2) < 1e-4)
print("rod integrity requires specific tensile strength Omega^2 l^2/8 = %.3e J/kg (hypothesis, not checked against material data)" % (Wn**2*ln**2/8))
# (9) G datum: CODATA 2014 -> 2018/2022 (READ: scipy _codata.py lines 1081, 1430, 1884)
G14, G22 = 6.67408e-11, 6.67430e-11
print("L and h scale linearly in G: CODATA2014->2022 relative move %.2e" % (G22/G14 - 1))
chk("G move < 1e-4 relative (conclusion, 26.6 orders, unmoved)", abs(G22/G14 - 1) < 1e-4)
print("ALL PASS" if ok else "SOME FAILED")
sys.exit(0 if ok else 1)
