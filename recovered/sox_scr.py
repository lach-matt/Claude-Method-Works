"""sox_scr.py -- s32 candidate S, step 2: the statically-screened, coupling-averaged second-order exchange eps_2x^scr(r_s,zeta) [Ha].
   eps_2x^scr = (3/(32 pi^5)) 4 pi sum_sigma x_sigma^3 INT dq' S(q') F(Pi(x_sigma q'; r_s, zeta)) / 2      (Ry->Ha),   x_sigma = (1 +- zeta)^(1/3)
   S(q') from sox_table.jsonl (bare pair sum, unit sphere; PCHIP split at the q=2 kink; tail S ~ q^-4);  F(Pi) = 2[Pi - ln(1+Pi)]/Pi^2 (PREDICTION-SOSEX D1);
   Pi(K,0;zeta) = (alpha r_s/(pi K^2)) sum_tau s_tau g(K/s_tau, 0) -- ring_zeta.g, the chain's Lindhard function (Maxwell's eps of the medium; G-S4/5 certified).
F -> 1 as r_s -> 0 (G-S2 automatic; G-S1 fixes the bare value E0B). Usage: python3 sox_scr.py -> writes sox_scr_table.json on the ring grid (rs, z of ring_table.json)."""
import numpy as np, json, ring_zeta as R
from scipy.interpolate import PchipInterpolator
al=R.al
_d=sorted([json.loads(l) for l in open('sox_table.jsonl')],key=lambda x:x['q'])
Q=np.array([x['q'] for x in _d]); SQ=np.array([x['S'] for x in _d])
_f1=PchipInterpolator(Q[Q<=2.0],SQ[Q<=2.0]); _f2=PchipInterpolator(Q[Q>=2.0],SQ[Q>=2.0])
def S(q):
    q=np.asarray(q,float); out=np.where(q<=2.0,_f1(np.clip(q,Q[0],2.0)),_f2(np.clip(q,2.0,Q[-1])))
    out=np.where(q<Q[0],SQ[0]*q/Q[0],out); out=np.where(q>Q[-1],SQ[-1]*(Q[-1]/q)**4,out); return out
def F(P):
    P=np.asarray(P,float); small=P<1e-3
    return np.where(small,1-2*P/3+P*P/2,2*(P-np.log1p(np.where(small,1.0,P)))/np.where(small,1.0,P*P))
def Pi(K,rs,z,lam=1.0):
    xp,xm=R.xs(z); return lam*(al*rs/(np.pi*K*K))*sum(s*R.g(K/s,1e-12*np.ones_like(K)) for s in (xp,xm) if s>0)
# fixed q' quadrature (dense, log + linear near the kink); Simpson-free trapezoid on a 1600-point composite grid
_qa=np.exp(np.linspace(np.log(1e-3),np.log(1.0),300)); _qb=np.linspace(1.0,3.5,900)[1:]; _qc=np.exp(np.linspace(np.log(3.5),np.log(60.0),400))[1:]
QQ=np.concatenate([_qa,_qb,_qc]); SQQ=S(QQ)
def eps_2x_bare():
    I=np.trapezoid(SQQ,QQ)+QQ[0]*SQQ[0]/2+SQQ[-1]*QQ[-1]/3
    return 3/(16*np.pi**5)*4*np.pi*I/2
def eps_2x_scr(rs,z,lam=1.0):
    xp,xm=R.xs(z); tot=0.0
    for x in (xp,xm):
        if x<=0: continue
        Fq=F(Pi(x*QQ,rs,z,lam)); I=np.trapezoid(SQQ*Fq,QQ)+QQ[0]*SQQ[0]/2*Fq[0]+SQQ[-1]*QQ[-1]/3*Fq[-1]
        tot+=x**3*I
    return 3/(32*np.pi**5)*4*np.pi*tot/2
if __name__=="__main__":
    E0B=eps_2x_bare(); print(f"bare (quadrature of the table) E0B = {E0B:.7f}")
    tab=json.load(open('ring_table.json')); RS=tab['rs']; ZS=tab['z']
    out={'rs':RS,'z':ZS,'eps2x_scr':{}, 'E0B_table':E0B, 'note':'eps_2x^scr(rs,zeta) Ha; F=2[Pi-ln(1+Pi)]/Pi^2 static Lindhard, AC weight; S(q) from sox_table.jsonl'}
    for iz,z in enumerate(ZS):
        out['eps2x_scr'][str(iz)]=[float(eps_2x_scr(rs,z)) for rs in RS]
        print(f"z {z}: rs {RS[0]} {out['eps2x_scr'][str(iz)][0]:.6f} | rs 2 {eps_2x_scr(2.0,z):.6f} ratio {eps_2x_scr(2.0,z)/E0B:.4f} | rs {RS[-1]} {out['eps2x_scr'][str(iz)][-1]:.6f}",flush=True)
    json.dump(out,open('sox_scr_table.json','w'))
