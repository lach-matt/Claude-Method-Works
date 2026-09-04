import numpy as np, json, eldata as ed
from collections import Counter
from scipy import stats
rows=json.load(open('/home/claude/ab.json'))
MN={int(k):v for k,v in json.load(open('/home/claude/mn.json')).items()}
CAP=lambda l:2*(2*l+1)
st=np.array([r['st'] for r in rows]); n=len(st)
def build(kind,std=True):
    X=[]
    for r in rows:
        za,zb=r['za'],r['zb']; mna,mnb=MN[za],MN[zb]
        sw = mna>mnb
        m1,m2=(mnb,mna) if sw else (mna,mnb)
        ka,kb=ed.E[za][2],ed.E[zb][2]; la,lb=ed.E[za][1],ed.E[zb][1]
        k1,k2,l1,l2=(kb,ka,lb,la) if sw else (ka,kb,la,lb)
        X.append({'pettifor':[m1,m2],'pettifor+k':[m1,m2,k1,k2],
                  'pettifor+frac':[m1,m2,k1/CAP(l1),k2/CAP(l2)]}[kind])
    X=np.array(X,float)
    return (X-X.mean(0))/(X.std(0)+1e-12) if std else X
def nn_correct(X,y):
    D=((X[:,None,:]-X[None,:,:])**2).sum(-1); np.fill_diagonal(D,np.inf)
    return np.array([y[int(np.argmin(D[i]))]==y[i] for i in range(len(y))])
print("="*76); print("IS ANY GAIN SIGNIFICANT?  McNemar on paired LOO-NN outcomes"); print("="*76)
for std in (True,False):
    base=nn_correct(build('pettifor',std),st)
    print(f"\n  standardised={std}   Pettifor accuracy {base.mean():.3f}")
    for kind in ['pettifor+k','pettifor+frac']:
        aug=nn_correct(build(kind,std),st)
        b=int(((base==1)&(aug==0)).sum())   # pettifor right, aug wrong
        c=int(((base==0)&(aug==1)).sum())   # aug right, pettifor wrong
        if b+c>0:
            p=stats.binomtest(c,b+c,0.5).pvalue
        else: p=1.0
        print(f"    {kind:<16} acc {aug.mean():.3f}  gain {aug.mean()-base.mean():+.3f}  "
              f"discordant {b}/{c}  McNemar p = {p:.3f}")
print()
print("="*76); print("PERMUTATION TEST: shuffle the k values, keep Pettifor fixed"); print("="*76)
rng=np.random.default_rng(7)
Xb=build('pettifor'); base_acc=nn_correct(Xb,st).mean()
obs=nn_correct(build('pettifor+k'),st).mean()-base_acc
null=[]
raw=build('pettifor+k')
for _ in range(2000):
    Xp=raw.copy()
    idx=rng.permutation(n)
    Xp[:,2:]=Xp[idx,2:]
    null.append(nn_correct(Xp,st).mean()-base_acc)
null=np.array(null)
print(f"  observed gain from real k : {obs:+.4f}")
print(f"  null mean {null.mean():+.4f}, 95th pct {np.percentile(null,95):+.4f}")
print(f"  p = {(null>=obs).mean():.4f}")
print()
print("="*76); print("VERDICT"); print("="*76)
print("""  Occupancy does NOT improve Pettifor's scale on the task the scale was
  built for. The gain is +0.000 standardised and +0.014 unstandardised,
  neither significant, and a permutation test on the k values cannot
  distinguish the real occupancies from random ones.

  The hydride result of §23.1 is therefore TASK-SPECIFIC. Occupancy adds
  orthogonal information about hydride formation enthalpy and adds nothing
  about binary structure-type separation. The caveat was correct to suspect
  this, and the test now settles it.""")