"""DOCKET 67 audit: potential-exact-linear-cost.
address.py:127-131  'V(v(1+eps))/|V_min| = eps^2 (2+eps)^2 EXACT -> 4 eps^2; sympy residual 0'.
Reads research/warp-drive READ-ONLY (no bytecode written).  Exit 1 on any failed check."""
import sys, re, math
sys.dont_write_bytecode = True
import sympy as sp
WD = "/home/user/Claude-Method-Works/research/warp-drive"
fails = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  | " + str(detail) if detail else ""))
    if not ok: fails.append(name)

e, lam, v, phi, mu2, k3, k4, m = sp.symbols("epsilon lambda v phi mu2 kappa3 kappa4 m", real=True)
# A. Tree-level SM potential, V(0)=0 convention (Buttazzo 1307.3536 eq.6 with |H|^2=phi^2/2, lambda_B=4 lambda_0;
#    Martin 1205.3365 eq.13 with V0 = -lambda v^4/4)
V = -mu2/2*phi**2 + lam/4*phi**4
vmin_sol = sp.solve(sp.diff(V, phi).subs(phi, v), mu2)[0]           # mu2 = lambda v^2
V = V.subs(mu2, vmin_sol)
Vmin = sp.simplify(V.subs(phi, v)); depth = -Vmin                     # lambda v^4/4
chk("A1 V_min = -lambda v^4/4", sp.simplify(Vmin + lam*v**4/4) == 0, Vmin)
dV = sp.expand((V.subs(phi, v*(1+e)) - Vmin)/depth)
chk("A2 [V(v(1+e)) - V_min]/|V_min| - e^2(2+e)^2 == 0 (sympy residual)",
    sp.simplify(dV - e**2*(2+e)**2) == 0, sp.factor(dV))
lit = sp.expand(V.subs(phi, v*(1+e))/depth)
chk("A3 LITERAL V(v(1+e))/|V_min| (V(0)=0 convention) = e^2(2+e)^2 - 1, not e^2(2+e)^2",
    sp.simplify(lit - (e**2*(2+e)**2 - 1)) == 0, sp.factor(lit))
Vm = lam/4*(phi**2 - v**2)**2        # Martin eq.13, V0 = 0: vanishes at the vacuum
chk("A4 Martin form (V0=0): V(v(1+e)) / (lambda v^4/4) = e^2(2+e)^2 exactly",
    sp.simplify(Vm.subs(phi, v*(1+e))/(lam*v**4/4) - e**2*(2+e)**2) == 0)
chk("A5 series: 4e^2 + 4e^3 + e^4 (terminates; leading 4 e^2)",
    sp.expand(e**2*(2+e)**2) == 4*e**2 + 4*e**3 + e**4)
# 8|V_min| = v^2 m_h^2 with m_h^2 = V''(v) = 2 lambda v^2
mh2 = sp.simplify(sp.diff(V, phi, 2).subs(phi, v))
chk("A6 m_h^2 = V''(v) = 2 lambda v^2 and 8|V_min| = m_h^2 v^2", sp.simplify(mh2 - 2*lam*v**2) == 0
    and sp.simplify(8*depth - mh2*v**2) == 0)
# B. leading term is shape-independent: 4 e^2 |V_min| = (1/2) m_h^2 (v e)^2
chk("B1 4 e^2 |V_min| == (1/2) m_h^2 (v e)^2", sp.simplify(4*e**2*depth - mh2*(v*e)**2/2) == 0)
# C. kappa family with same v and m_h: V = m^2 h^2/2 + k3 lambda v h^3 + k4 lambda h^4/4, h = v e
#    (SM: k3 = k4 = 1).  Data fix v and m_h only; kappa_lambda = k3 bounded to (-1.2, 7.5) (CMS, READ via
#    2503.11548 p.2); k4 unmeasured.
h = v*e
Vk = (2*lam*v**2)*h**2/2 + k3*lam*v*h**3 + k4*lam*h**4/4
fk = sp.expand(Vk/depth)
chk("C1 kappa family: dV/|V_min|_SM = 4e^2 + 4 k3 e^3 + k4 e^4", sp.simplify(fk - (4*e**2 + 4*k3*e**3 + k4*e**4)) == 0, fk)
chk("C2 SM point k3=k4=1 recovers e^2(2+e)^2", sp.simplify(fk.subs({k3: 1, k4: 1}) - e**2*(2+e)**2) == 0)
for kk in (-1.2, 7.5):
    val = fk.subs({k3: kk, k4: 1, e: 1})
    print("     C3 at e=1, kappa_lambda=%s, k4=1: dV/|V_min| = %s (SM value 9)" % (kk, float(val)))
chk("C3 at e = 1 the 'exact' value 9 spans [0.2, 35] over the allowed kappa_lambda (k4 = 1)",
    abs(float(fk.subs({k3: -1.2, k4: 1, e: 1})) - 0.2) < 1e-12 and abs(float(fk.subs({k3: 7.5, k4: 1, e: 1})) - 35) < 1e-12)

# D. Numbers at the tree's own eps_det, READ from the owner (import only; no write)
sys.path.insert(0, WD)
import address, higgs
eps_det = address.eps_det_stationary("H1")
cf = address.cost_fraction(eps_det)
print("     D  eps_det(H1) = %.6e ; cost_fraction = %.6e ; energy density = %.6e J/m^3" % (eps_det, cf, address.energy_density(eps_det)))
chk("D1 energy density at eps_det is O(1e16) J/m^3 (address.py:132)", 1e15 < address.energy_density(eps_det) < 1e17, address.energy_density(eps_det))
worst = max(abs(4*(kk-1)*eps_det**3 + 0*eps_det**4)/(4*eps_det**2) for kk in (-1.2, 7.5))
chk("D2 kappa_lambda in (-1.2, 7.5) moves the eps_det cost by < 1e-13 (relative)", worst < 1e-13, worst)
# m_h: tree 125.13 (PDG-2026 capture) vs PDG-2024 125.20(11) (READ via 2401.08811 Table I, cached)
r = (125.20/higgs.M_HIGGS)**2 - 1
chk("D3 m_h 125.13 -> 125.20 moves |V_min| (hence the cost) by +0.11%, same order", abs(r - 0.001119) < 2e-5, r)
# MS-bar lambda(M_t) NNLO 0.12604 vs LO 0.12917 (1307.3536 Table 3, cached): if lambda_MSbar were used
r2 = 0.12604/0.12917 - 1
chk("D4 loop-level lambda (NNLO MS-bar) would move a lambda v^4/4 depth by -2.4%, same order", -0.03 < r2 < -0.02, r2)
chk("D5 |V_min| = m_h^2 v^2/8 in SI at the tree's m_h (2.47e45 J/m^3)",
    abs(address.VMIN_SI - higgs.gev4_to_si(higgs.M_HIGGS**2*higgs.vev()**2/8)) / address.VMIN_SI < 1e-12, address.VMIN_SI)

# E. Owner's 'sympy residual 0' claim: does address.py run sympy on THIS identity?
src = open(WD + "/address.py").read()
sympy_funcs = re.findall(r"def (\w+)\(\):\n(?:    .*\n)*?    import sympy as sp", src)
print("     E  functions in address.py importing sympy:", sympy_funcs)
body_lines = [l for l in src.splitlines() if "cost_fraction" in l]
has_sympy_cost = any(("sp." in l) for l in body_lines)
chk("E1 RECORDED: address.py contains no sympy computation of the cost identity (its selftest checks cost_fraction against its own formula, lines 1359-1368)",
    not has_sympy_cost and "cost" not in " ".join(sympy_funcs))
ex = open(WD + "/excite.py").read()
chk("E2 the identity IS derived elsewhere in the tree: excite.py FIELD_POLY by polynomial composition, matched to endpoint.cost_fraction(-e)",
    "FIELD_POLY" in ex and "endpoint.cost_fraction(-e)" in ex)

# F. Downstream W12 ratio: linear source / nonlinear energy vs nonlinear equilibrium source
#    Equilibrium V'(phi) = -n m0/v * (phi/v)? excite.py: source rest energy = -V'(phi) phi; phi = v(1-d), d>0
d = sp.symbols("d", positive=True)
Vp = sp.diff(V, phi)
src_nl = sp.simplify(-Vp.subs(phi, v*(1-d))*v*(1-d)/depth)
fld = sp.simplify((V.subs(phi, v*(1-d)) - Vmin)/depth)
chk("F1 nonlinear source = 4 d (2-d)(1-d)^2 (excite.py:152)", sp.simplify(src_nl - 4*d*(2-d)*(1-d)**2) == 0, sp.factor(src_nl))
ratio_nl = sp.simplify(src_nl/fld)
ratio_addr = 8/(d*(2-d)**2)          # address.py source_to_field_ratio at eps = -d
diffser = sp.series(ratio_addr - ratio_nl, d, 0, 2).removeO()
print("     F2 address 8/(d(2-d)^2) - nonlinear 4(1-d)^2/(d(2-d)) = %s + O(d^2)" % sp.simplify(diffser))
chk("F2 both ratios -> 2/d; they differ at O(1) absolute, O(d) relative -- 'EXACTLY' holds for the linearised source only",
    sp.limit(ratio_addr*d, d, 0) == 2 and sp.limit(ratio_nl*d, d, 0) == 2)
rel = abs(float(((ratio_addr - ratio_nl)/ratio_nl).subs(d, eps_det)))
chk("F3 at eps_det the difference is < 1e-14 relative (conclusion unmoved)", rel < 1e-14, rel)

print()
print("FAILS:", fails if fails else "none")
sys.exit(1 if fails else 0)
