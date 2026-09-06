"""ring_table.py -- s30 candidate C: tabulate the full RPA ring eps_r(r_s,zeta) [Ry] (ring_zeta.py, nan-masked cancellation cell) on a log r_s x zeta grid."""
import numpy as np, json, sys, ring_zeta as R
np.seterr(all='ignore'); al=R.al
def eps_r(rs,z,nk=1400,nx=1400):
    xp,xm=R.xs(z); k=np.exp(np.linspace(np.log(1e-4),np.log(60.0),nk)); x=np.exp(np.linspace(np.log(1e-4),np.log(1e3),nx))
    K,X=np.meshgrid(k,x,indexing='ij'); Pi=(al*rs/(np.pi*K*K))*sum(s*R.g(K/s,K*X/(s*s)) for s in (xp,xm) if s>0)
    f=K**3*(np.log1p(Pi)-Pi); f=np.where(np.isfinite(f),f,0.0)   # cancellation cell (K~1e-4,X~1e3) masked; s30 stated
    return float(3/(2*np.pi*al*al*rs*rs)*np.trapezoid(np.trapezoid(f,x,axis=1),k))
RS=np.exp(np.linspace(np.log(1e-3),np.log(100.0),41)); ZS=np.linspace(0,1,11)
if __name__=="__main__":
    zi=[int(a) for a in sys.argv[1:]] or range(len(ZS))
    try: tab=json.load(open('ring_table.json'))
    except Exception: tab={'rs':RS.tolist(),'z':ZS.tolist(),'eps':{}}
    for i in zi:
        if str(i) in tab['eps']: print('SKIP z',ZS[i]); continue
        tab['eps'][str(i)]=[eps_r(rs,ZS[i]) for rs in RS]; json.dump(tab,open('ring_table.json','w')); print('z',round(ZS[i],2),'done; eps_r(rs=2)',round(tab['eps'][str(i)][int(np.argmin(abs(RS-2)))],4),flush=True)