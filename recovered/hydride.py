import numpy as np
import eldata as ed
from scipy import stats
import json

# ── Measured hydride formation enthalpies, kJ/mol H ─────────────
# Negative = exothermic (stable hydride). Standard literature values
# for binary metal hydrides at the dilute/dihydride limit.
dHf = {
 21:-100.0, 22:-72.0, 23:-32.0, 24: 10.0, 26: 20.0, 27: 15.0, 28: 20.0,
 29: 40.0, 39:-114.0, 40:-82.0, 41:-40.0, 42: 25.0, 44: 30.0, 45: 20.0,
 46:-19.0, 47: 60.0, 57:-104.0, 58:-100.0, 59:-104.0, 60:-100.0,
 62:-96.0, 63:-88.0, 64:-92.0, 65:-92.0, 66:-92.0, 67:-90.0, 68:-90.0,
 69:-88.0, 70:-84.0, 71:-84.0, 72:-66.0, 73:-38.0, 74: 30.0, 75: 25.0,
 77: 30.0, 78: 25.0, 79: 50.0, 90:-72.0, 92:-42.0,
}

ZS = sorted(dHf)
Y  = np.array([dHf[z] for z in ZS], float)

FEAT = {
    'l'  : np.array([ed.E[z][1] for z in ZS], float),
    'n'  : np.array([ed.E[z][0] for z in ZS], float),
    'k'  : np.array([ed.E[z][2] for z in ZS], float),
    'Q0' : np.array([ed.Q0mag(z) for z in ZS]),
    'Hcp': np.array([ed.hcp(z) for z in ZS]),
    'Z'  : np.array(ZS, float),
}

def design(cols):
    return np.column_stack([np.ones(len(Y))] + [FEAT[c] for c in cols])

def fit(cols):
    X = design(cols)
    b, *_ = np.linalg.lstsq(X, Y, rcond=None)
    pred = X @ b
    ss_res = np.sum((Y-pred)**2); ss_tot = np.sum((Y-np.mean(Y))**2)
    return b, pred, 1 - ss_res/ss_tot

def loo(cols):
    X = design(cols); pr = np.zeros(len(Y))
    for i in range(len(Y)):
        m = np.ones(len(Y), bool); m[i] = False
        b, *_ = np.linalg.lstsq(X[m], Y[m], rcond=None)
        pr[i] = X[i] @ b
    return pr, 1 - np.sum((Y-pr)**2)/np.sum((Y-np.mean(Y))**2)

def rmse(a, b): return float(np.sqrt(np.mean((a-b)**2)))

models = [['l'], ['k'], ['l','k'], ['l','n','k'], ['l','Q0'], ['l','Hcp'],
          ['l','n','k','Q0','Hcp'], ['Z']]

print(f"{'model':<26}{'fit R2':>9}{'LOO R2':>9}{'RMSE':>9}{'LOO RMSE':>10}")
print('-'*63)
rows = []
for cols in models:
    b, pred, r2 = fit(cols)
    lp, lr2 = loo(cols)
    rows.append(dict(model='+'.join(cols), r2=r2, loo=lr2,
                     rmse=rmse(Y,pred), loo_rmse=rmse(Y,lp)))
    print(f"{'+'.join(cols):<26}{r2:>9.3f}{lr2:>9.3f}{rmse(Y,pred):>9.1f}{rmse(Y,lp):>10.1f}")

# ── the preferred model ─────────────────────────────────────────
b, pred, r2 = fit(['l','k'])
lp, lr2 = loo(['l','k'])
print(f"\nPreferred model:  dHf = {b[0]:+.1f} {b[1]:+.1f}·l {b[2]:+.1f}·k   (kJ/mol H)")
print(f"  fit R2 = {r2:.3f}   LOO R2 = {lr2:.3f}   RMSE = {rmse(Y,pred):.1f} kJ/mol H")

# coefficient significance
X = design(['l','k']); nobs, npar = X.shape
resid = Y - pred
s2 = np.sum(resid**2)/(nobs-npar)
cov = s2 * np.linalg.inv(X.T @ X)
se = np.sqrt(np.diag(cov))
tv = b/se
pv = 2*(1-stats.t.cdf(np.abs(tv), nobs-npar))
for nm, bi, si, ti, pi in zip(['intercept','l','k'], b, se, tv, pv):
    print(f"  {nm:<10} beta={bi:+8.2f}  se={si:6.2f}  t={ti:+6.2f}  p={pi:.2e}")

# ── permutation test on the k contribution ──────────────────────
rng = np.random.default_rng(11)
base = fit(['l'])[2]
obs  = r2 - base
null = []
for _ in range(10000):
    kk = rng.permutation(FEAT['k'])
    Xp = np.column_stack([np.ones(len(Y)), FEAT['l'], kk])
    bb, *_ = np.linalg.lstsq(Xp, Y, rcond=None)
    pp = Xp @ bb
    null.append(1 - np.sum((Y-pp)**2)/np.sum((Y-np.mean(Y))**2) - base)
null = np.array(null)
pperm = float((null >= obs).mean())
print(f"\nPermutation test on k (10,000 shuffles):")
print(f"  observed gain in R2 = {obs:.3f}")
print(f"  null 95th pct = {np.percentile(null,95):.3f}   p = {pperm:.4f}")

# ── class comparison ────────────────────────────────────────────
bB = [dHf[z] for z in ZS if ed.dclass(z)=='B']
bC = [dHf[z] for z in ZS if ed.dclass(z)=='C']
tt, pp2 = stats.ttest_ind(bB, bC, equal_var=False)
print(f"\nClass B (n={len(bB)}): mean {np.mean(bB):+.1f} kJ/mol H")
print(f"Class C (n={len(bC)}): mean {np.mean(bC):+.1f} kJ/mol H")
print(f"Welch t = {tt:.2f}, p = {pp2:.4f}")

out = dict(
    coef=dict(intercept=float(b[0]), l=float(b[1]), k=float(b[2])),
    se=[float(x) for x in se], p=[float(x) for x in pv],
    r2=float(r2), loo=float(lr2), rmse=rmse(Y,pred), loo_rmse=rmse(Y,lp),
    perm_p=pperm, obs_gain=float(obs),
    classB=float(np.mean(bB)), classC=float(np.mean(bC)),
    tstat=float(tt), tp=float(pp2), n=len(ZS),
    table=rows,
    zs=ZS, y=[float(v) for v in Y], pred=[float(v) for v in pred],
    loo_pred=[float(v) for v in lp],
)
json.dump(out, open('/home/claude/hydride_fit.json','w'), indent=1)
print('\nsaved hydride_fit.json')
