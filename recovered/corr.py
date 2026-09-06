import numpy as np, eldata as ed
from scipy import stats

# Independently measured dimensional quantities.
# Hydride formation enthalpy, kJ/mol H (negative = exothermic/stable hydride).
# Standard literature values, binary metal hydrides.
dHf = {
 21:-100.0, 22:-72.0, 23:-32.0, 24: 10.0, 26: 20.0, 27: 15.0, 28: 20.0,
 29: 40.0, 39:-114.0, 40:-82.0, 41:-40.0, 42: 25.0, 44: 30.0, 45: 20.0,
 46:-19.0, 47: 60.0, 57:-104.0, 58:-100.0, 59:-104.0, 60:-100.0,
 62:-96.0, 63:-88.0, 64:-92.0, 65:-92.0, 66:-92.0, 67:-90.0, 68:-90.0,
 69:-88.0, 70:-84.0, 71:-84.0, 72:-66.0, 73:-38.0, 74: 30.0, 75: 25.0,
 77: 30.0, 78: 25.0, 79: 50.0, 90:-72.0, 92:-42.0,
}
# Metal-metal nearest-neighbour distance, Angstrom (structural, measured)
dMM = {
 21:3.256,22:2.896,23:2.622,24:2.498,26:2.482,27:2.506,28:2.492,29:2.556,
 39:3.550,40:3.179,41:2.858,42:2.725,44:2.650,45:2.689,46:2.751,47:2.889,
 57:3.740,58:3.650,59:3.640,60:3.628,62:3.590,63:3.960,64:3.578,65:3.525,
 66:3.503,67:3.486,68:3.468,69:3.447,70:3.880,71:3.435,72:3.127,73:2.860,
 74:2.741,75:2.741,77:2.714,78:2.775,79:2.884,90:3.596,92:2.754,
}

def report(name, data, unit):
    zs = sorted(data)
    y  = np.array([data[z] for z in zs], float)
    print(f"\n{'='*66}\n{name}  ({unit}),  n = {len(zs)}\n{'='*66}")
    preds = {
        '|Q0| = sqrt(n^2+l^2+k^2)': np.array([ed.Q0mag(z) for z in zs]),
        'H_cp (heuristic index)'  : np.array([ed.hcp(z)   for z in zs]),
        'n  (shell)'              : np.array([ed.E[z][0]  for z in zs], float),
        'l  (subshell)'           : np.array([ed.E[z][1]  for z in zs], float),
        'k  (occupancy)'          : np.array([ed.E[z][2]  for z in zs], float),
        'k / k_max (filling)'     : np.array([ed.E[z][2]/ed.maxk(ed.E[z][1]) for z in zs]),
        'Z  (atomic number)'      : np.array(zs, float),
    }
    print(f"{'predictor':<28}{'Pearson r':>11}{'p':>11}{'Spearman':>11}{'R^2':>8}")
    print('-'*66)
    for lab, x in preds.items():
        r,pv = stats.pearsonr(x,y); rho,_ = stats.spearmanr(x,y)
        star = '  <<<' if (pv<0.01 and abs(r)>0.6) else ''
        print(f"{lab:<28}{r:>11.3f}{pv:>11.2ე}{rho:>11.3f}{r*r:>8.3f}{star}".replace('ე','e'))
    # class comparison
    print('\nBy DeltaQ direction class:')
    for c in ['B','C']:
        v=[data[z] for z in zs if ed.dclass(z)==c]
        if v: print(f"  Class {c}: n={len(v):2d}  mean={np.mean(v):8.2f}  sd={np.std(v):7.2f}")
    b=[data[z] for z in zs if ed.dclass(z)=='B']; cc=[data[z] for z in zs if ed.dclass(z)=='C']
    if len(b)>2 and len(cc)>2:
        tt,pp = stats.ttest_ind(b,cc,equal_var=False)
        print(f"  Welch t-test B vs C:  t={tt:.2f}  p={pp:.4f}")

report('Hydride formation enthalpy', dHf, 'kJ/mol H')
report('Metal-metal nearest-neighbour distance', dMM, 'Angstrom')