#!/usr/bin/env python3
"""t7c_mv.py -- session 20, candidate (a) of bridge-19 s6: relativistic correction to LOCAL EXCHANGE.
MacDonald & Vosko 1979 (J. Phys. C 12, 2977): V_x^R = V_x^NR * Phi_V(beta), Phi_V = -1/2 + (3/2) ln(beta+eta)/(beta eta), eta = sqrt(1+beta^2),
beta = k_F/c.  Spin-polarised local exchange used here: Vx_s = -(6 rho_s/pi)^(1/3) = -k_F,s/pi with k_F,s = (6 pi^2 rho_s)^(1/3).
Phi_V(0) = 1, so c = 1e6 reproduces the nonrel object. One line of scf_pol_sr patched by source; c passed through as before.
PREDICTION PA1 (before run; 0.005 CHOSEN): |dE_5d(La)| < 0.005, negative.  PA2: 4f gate row (Dy 66) moves < 0.005.
usage: python3 t7c_mv.py 57 66      (appends to t7c_mv.jsonl)
"""
import sys, json, numpy as np
import t7c_pol
from t5_scf import ground_occ, minus
def PHI(rho, c):
    kf = (6.0*np.pi**2*np.maximum(rho, 1e-300))**(1.0/3.0); b = kf/c; eta = np.sqrt(1.0+b*b)
    with np.errstate(divide='ignore', invalid='ignore'):
        f = -0.5 + 1.5*np.log(b+eta)/(b*eta)
    return np.where(b < 1e-4, 1.0 - 2.0*b*b/3.0, f)   # small-beta series to avoid 0/0
src = open('t7c_pol.py').read()
old = "Vx=-(6.0*rho/np.pi)**(1.0/3.0)"
assert src.count(old) == 1
new = "Vx=-(6.0*rho/np.pi)**(1.0/3.0)*PHI(rho,c)"
g = dict(t7c_pol.__dict__); g['PHI'] = PHI
exec(compile(src.replace(old, new).split('if __name__')[0], 't7c_pol_mv', 'exec'), g)
scf = g['scf_pol_sr']
C0 = t7c_pol.C0
T5 = {json.loads(l)['Z']: json.loads(l) for l in open('t5.jsonl')}
T7P = {json.loads(l)['Z']: json.loads(l) for l in open('t7c_pol.jsonl')}
for Z in map(int, sys.argv[1:]):
    r = T5[Z]; n, l = int(r['sh'][0]), "spdf".index(r['sh'][1]); occ = minus(ground_occ(Z), n, l, 0.5)
    s = "d" if dict(((a, b), k) for a, b, k in occ)[(n, l)] >= 2*l+1 else "u"
    _, Es, h = scf(Z, 1, occ=occ, c=C0); e = round(float(Es[(n, l, s)]), 4); b = T7P.get(Z, {})
    out = dict(Z=Z, el=r['el'], sh=r['sh'], meas=r['meas'], mv=e, sr_banked=b.get('t7c_pol'), d_mv=round(e-b['t7c_pol'], 4), it=len(h))
    open('t7c_mv.jsonl', 'a').write(json.dumps(out)+'\n'); print(out, flush=True)
