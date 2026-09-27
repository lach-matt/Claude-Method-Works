"""Re-audit checks: Pendry, J. Phys. A 16 (1983) 2161, read from Drive 1agL2n-mWVdWzk_3vNNbWM5imgH9nmM58.
Checks Pendry's printed forms and numbers against the tree's ceiling (branelink.py:38-39, 350)."""
import sympy as sp, math
P=[]; F=[]
def chk(name, ok):
    (P if ok else F).append(name); print(("PASS " if ok else "FAIL ")+name)
hb,k,T,E,I=sp.symbols('hbar k_B T E I',positive=True)
# (a) Pendry abstract / eq (5),(16): I^2 <= (pi/(3 ln^2 2)) E / hbar   <=>  I <= sqrt(pi E/(3 hbar))/ln 2  (tree)
pendry_I = sp.sqrt(sp.pi*E/(3*sp.log(2)**2*hb))
tree_I = sp.sqrt(sp.pi*E/(3*hb))/sp.log(2)
chk("(a) Pendry eq.(16) I^2<=(pi/3ln^2 2)E/hbar is identical to branelink's sqrt(pi P/3hbar)/ln2", sp.simplify(pendry_I-tree_I)==0)
# (b) Pendry eq (36) at optimum: S=(1/6)pi k^2 Tc/hbar, E=(1/12) pi k^2 Tc^2/hbar  -> S^2/E = pi k^2/(3 hbar)
S36=sp.pi*k**2*T/(6*hb); E36=sp.pi*k**2*T**2/(12*hb)
chk("(b) eq.(36) optimum saturates S^2 = pi k^2 E/(3 hbar) (eq.15 in entropy form)", sp.simplify(S36**2/E36 - sp.pi*k**2/(3*hb))==0)
# (c) the 1D Bose integral that gives eq (36): E = int_0^inf hbar w n(w) dw/2pi, S from Bose entropy
x=sp.symbols('x',positive=True)
import mpmath as _mp
bose=_mp.quad(lambda u: u/(_mp.e**u-1),[0,_mp.inf]); print('   int x/(e^x-1) =',bose,' pi^2/6 =',_mp.pi**2/6)
assert abs(bose-_mp.pi**2/6)<1e-14
Eint = (k*T)**2/(2*sp.pi*hb)*sp.zeta(2)  # Gamma(2)zeta(2), checked by quadrature above
chk("(c) E+ = int hbar w n dw/2pi = pi k^2 T^2/(12 hbar) (eq.36, bosons, massless)", sp.simplify(Eint-E36)==0)
# (d) eq (34)/(35): with S >= Q/T (32) and eq.(15): Q <= pi k^2 T^2/(3 hbar); equality at Tc = 2T (eq.37 'one quarter')
Q=sp.symbols('Q',positive=True)
Qmax=sp.solve(sp.Eq((Q/T)**2, sp.pi*k**2*Q/(3*hb)),Q)[0]
chk("(d) eq.(35) Q <= pi k^2 T^2/(3 hbar)", sp.simplify(Qmax-sp.pi*k**2*T**2/(3*hb))==0)
Tc=sp.symbols('T_c',positive=True)
chk("(d') optimum channel temperature Tc = 2T (E+(Tc)=Qmax)", sp.solve(sp.Eq(E36.subs(T,Tc),Qmax),Tc)==[2*T])
chk("(d'') eq.(37): irreversible contact Tc=T gives one quarter of optimum", sp.simplify(E36/Qmax)==sp.Rational(1,4))
# (e) dE/dT = pi^2 k^2 T/(3h): the thermal conductance quantum -- resolves OCR 'h' as hbar
h=2*sp.pi*hb
chk("(e) dE+/dT = pi^2 k^2 T/(3h), the conductance quantum: the OCR glyph 'h' is hbar", sp.simplify(sp.diff(E36,T)-sp.pi**2*k**2*T/(3*h))==0)
# (f) numbers Pendry prints: eq.(17) 1e9 bit/s needs E+ ~ 1e-16 W ; 'information flow rate of 10^?? Hz would require at least 1 W'
hbar=1.054571817e-34
Emin=lambda Ib: 3*hbar*math.log(2)**2*Ib**2/math.pi
print("   E+ at 1e9 bit/s =", Emin(1e9), "W (hbar);  with h:", Emin(1e9)*2*math.pi, "W")
chk("(f) eq.(17) '10^-16 W' at 1e9 bit/s: right ORDER (4.8e-17 with hbar; not a discriminator between h and hbar)", 1e-17 < Emin(1e9) < 1e-16*1.0001)
I1W=math.sqrt(math.pi*1.0/(3*hbar))/math.log(2)
print("   I at 1 W =", I1W, "bit/s")
chk("(f') 1 W carries 1.44e17 bit/s (Pendry's '10^17 Hz ... at least 1 W', exponent garbled in OCR)", 1e17 < I1W < 2e17)
# (g) Pendry's parallelism argument (eqs 6-7): two channels at total E carry sqrt(2) x one channel: N channels sqrt(N)
N=sp.symbols('N',positive=True)
chk("(g) eq.(7): N channels sharing E carry sqrt(N) x single-channel ceiling", sp.simplify(N*pendry_I.subs(E,E/N)/pendry_I - sp.sqrt(N))==0)
# (h) branelink S5 N(A) is the ceiling
A=sp.symbols('A',positive=True)
chk("(h) branelink.py:350 N(A)=sqrt(A pi/(3 hbar ln^2 2)) is Pendry's bound", sp.simplify(sp.sqrt(A*sp.pi/(3*hb*sp.log(2)**2))-pendry_I.subs(E,A))==0)
# (i) gapped boson (optical fibre cut-off): ratio S^2/E strictly below pi k^2/3hbar at finite T
import mpmath as mp
def ratio(x0):
    Eg=mp.quad(lambda u: u/(mp.e**u-1),[x0,mp.inf]); Sg=mp.quad(lambda u: (u/(mp.e**u-1)) - mp.log(1-mp.e**(-u)),[x0,mp.inf])
    return (Sg**2/Eg)/(mp.pi**2/3*mp.pi/mp.pi)  # S in units k^2T/2pi hbar ; E in k^2T^2/2pi hbar ; ceiling pi k^2/3hbar -> (2pi)(pi/3)=... normalise
# normalisation: S=(kT/2pi hbar) k s, E=(kT)^2/(2 pi hbar) e ; S^2/E = k^2/(2 pi hbar) s^2/e ; ceiling pi k^2/(3hbar) -> s^2/e ceiling = 2pi^2/3
def r2(x0):
    e=mp.quad(lambda u: u/(mp.e**u-1),[x0,mp.inf]); s=mp.quad(lambda u: u/(mp.e**u-1) - mp.log(1-mp.e**(-u)),[x0,mp.inf])
    return s**2/e/(2*mp.pi**2/3)
chk("(i) massless gapless boson saturates (ratio 1)", abs(r2(0)-1)<1e-12)
chk("(i') band edge (Pendry's optical-fibre cut-off) stays strictly below ceiling", all(r2(x0)<1 for x0 in (0.1,1,5)))
print("\n%d PASS, %d FAIL"%(len(P),len(F))); raise SystemExit(1 if F else 0)
