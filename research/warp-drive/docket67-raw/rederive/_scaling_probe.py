# probe: far-zone plane wave with phi = A e^{ikl} (O(1), not A/l), rho = B e^{ikl}
import sympy as sp, importlib.util, sys, io, contextlib
src = open('gr-qc_9701064_omega.py').read().split('# ---------------------------------------------------------------- T2 far zone')[0]
src = src.replace('# ---------------------------------------------------------------- T0', 'if False:')
# T0 and T1 blocks are indented under if False only for first line; simpler: exec pieces
g = {}
code = open('gr-qc_9701064_omega.py').read()
pre = code.split('# ---------------------------------------------------------------- T0')[0]
lin = code.split('# ---------------------------------------------------------------- linearisation')[1].split('# ---------------------------------------------------------------- T2 far zone')[0]
exec(pre, g)
g['f0'] = sp.Symbol('f0', positive=True); g['L0'] = sp.Symbol('L0', real=True)
exec(lin, g)
l, x, A, B, k = g['l'], sp.Symbol('x', positive=True), g['A'], g['B'], g['k']
rd = g['READINGS']['conserved(116,r^2)']
for e in g['lin_for'](rd):
    ee = g['sub_modes'](e, A*sp.exp(sp.I*k*l), B*sp.exp(sp.I*k*l))
    ee = sp.expand(sp.simplify(ee*sp.exp(-sp.I*k*l))).subs(l, 1/x)
    pl = sp.Poly(sp.expand(ee), x)
    lo = min(m[0] for m in pl.monoms())
    print('leading power x^%d:' % lo, sp.factor(pl.coeff_monomial(x**lo)))
    print('   next x^%d:' % (lo+1), sp.factor(pl.coeff_monomial(x**(lo+1))))
