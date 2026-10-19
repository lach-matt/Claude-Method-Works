import sys, time, pickle; sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive/docket68/lemmas")
import sympy as sp, kn_gauge as K
t0 = time.time(); T = lambda m: print(m, round(time.time()-t0, 1), flush=True)
v, r, th, mu = sp.symbols("v r theta mu", positive=True)
a, b, cc, dps, dom = [sp.Function(n)(v, r, th) for n in ("a", "b", "cc", "dps", "dom")]
L = {jk: x[1] for jk, x in pickle.load(open("hlin.pkl", "rb")).items()}
Phi = sp.Function("Phi")(v); p1, p2 = sp.Function("p1")(th), sp.Function("p2")(th)
Kf, Mf = sp.Function("K")(v, th), sp.Function("M")(v, th)
k = sp.Rational(-3, 2); sn, cs = sp.sin(th), sp.cos(th); hvr = r**4*sn**2*cs**2
cpf = sp.Function("cp")(th)
Af = sp.Function("A")(v, r, th)
sub0 = {dps: p1*Phi*r**k, dom: p2*Phi*r**k, b: 2*p1*Phi*r**k*hvr, cc: Phi*cpf*r**sp.Rational(7, 2) + Kf*r**2, a: Af}
E = sp.expand(sp.numer(sp.together(L[(2, 2)].subs(sub0).doit()))); T("E nterms %d" % len(E.args))
cAr = E.coeff(sp.Derivative(Af, r)); E0 = sp.expand(E.subs(sp.Derivative(Af, r), 0))
cA = E0.coeff(Af); rest = sp.expand(E0.subs(Af, 0))
P = sp.simplify(cA/cAr); T("P = %s" % P)
Q = sp.expand(sp.simplify(-rest/cAr)); T("Q ops %d" % sp.count_ops(Q))
d = K._rsplit(Q, r); T("Q powers %s" % sorted(d))
Ip = 0
for e_, cf in d.items():
    m = e_ - 2; Ip += cf*(sp.log(r) if m == -1 else r**(m + 1)/(m + 1))
Apart = sp.expand(r**2*Ip); T("Apart ops %d" % sp.count_ops(Apart))
sub = dict(sub0); sub[a] = Apart + Mf*r**2
sup = {}
for jk in [(0, 2), (0, 1)]:
    Z = sp.expand(sp.numer(sp.together(L[jk].subs(sub).doit()))); T("sup %s nterms %d" % (jk, len(Z.args)))
    sup[jk] = K._rsplit(Z, r); T("split powers %s" % sorted(sup[jk]))
pickle.dump(dict(P=P, Q=Q, Apart=Apart, sup=sup), open("dbg9.pkl", "wb")); T("done")
