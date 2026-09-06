import numpy as np, eldata as ed
from scipy import stats

def exch_pairs(l,k):
    orb=2*l+1; up=min(k,orb); dn=max(0,k-orb)
    return up*(up-1)//2 + dn*(dn-1)//2

ANOM={24,29,41,42,44,45,46,47,57,58,64,78,79,89,90,91,92,93,96,103}

print("="*76)
print("REFINED: EXCHANGE GAIN vs PROMOTION COST, BOTH INDEXED BY Λ")
print("="*76)
print("""  Promotion s->d costs roughly the ns/(n-1)d energy gap, which narrows
  across a period as the d shell contracts. Λ gives us k as a proxy for
  how far across the period we are. Model:
      favourability  =  ΔE_exch(ℓ,k)  −  c·(promotion proxy)
  and ask whether ANY monotone promotion proxy built from Λ separates
  anomalous from normal. Test several.""")

rows=[]
for z in sorted(ed.E):
    n,l,k=ed.E[z]
    if l<2 or k>=2*(2*l+1): continue
    rows.append(dict(z=z,sym=ed.SYM[z],n=n,l=l,k=k,
                     gain=exch_pairs(l,k+1)-exch_pairs(l,k),
                     anom=z in ANOM))
Y=np.array([r['anom'] for r in rows],float)
print(f"\n  sample: {len(rows)} d/f-block elements, {int(Y.sum())} anomalous\n")

feats={
 'exchange gain'          : np.array([r['gain'] for r in rows],float),
 'k'                      : np.array([r['k'] for r in rows],float),
 'k/kmax'                 : np.array([r['k']/(2*(2*r['l']+1)) for r in rows]),
 'n'                      : np.array([r['n'] for r in rows],float),
 'gain − k/2'             : np.array([r['gain']-r['k']/2 for r in rows]),
 'gain − k'               : np.array([r['gain']-r['k'] for r in rows]),
 'gain/(1+k)'             : np.array([r['gain']/(1+r['k']) for r in rows]),
 'is half-filled'         : np.array([1.0 if r['k']==2*r['l'] else 0.0 for r in rows]),
 'is one-below-full'      : np.array([1.0 if r['k']==2*(2*r['l']+1)-1 else 0.0 for r in rows]),
 'half or one-below-full' : np.array([1.0 if (r['k']==2*r['l'] or r['k']==2*(2*r['l']+1)-1) else 0.0 for r in rows]),
}
print(f"  {'predictor':<26}{'AUC':>8}{'p (MWU)':>10}")
print("  "+"-"*46)
for nm,x in feats.items():
    a=x[Y==1]; b=x[Y==0]
    try:
        u,p=stats.mannwhitneyu(a,b,alternative='two-sided')
        auc=u/(len(a)*len(b))
    except Exception:
        auc,p=float('nan'),float('nan')
    star='  <<<' if p<0.05 else ''
    print(f"  {nm:<26}{auc:>8.3f}{p:>10.4f}{star}")

print()
print("="*76)
print("THE KEY TEST: does k = half-filled or one-below-full catch the anomalies?")
print("="*76)
hits=[r for r in rows if (r['k']==2*r['l'] or r['k']==2*(2*r['l']+1)-1)]
print(f"  cells at half-filled or one-below-full: {len(hits)}")
for r in hits:
    print(f"    {r['sym']:>3} (n={r['n']},ℓ={r['l']},k={r['k']})  anomalous: {r['anom']}")
tp=sum(1 for r in hits if r['anom']); fp=len(hits)-tp
fn=int(Y.sum())-tp
print(f"\n  true positives {tp}, false positives {fp}, false negatives {fn}")
if tp+fp: print(f"  precision {tp/(tp+fp):.2f}   recall {tp/(tp+fn):.2f}")