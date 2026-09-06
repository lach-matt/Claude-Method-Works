import sys,os,numpy as np
sys.argv=['v5a.py','ent','--lmax','-1']; exec(open('v5a.py').read().split("out={}")[0])
sys.path.insert(0,HERE); import so94
a=(7,0); Vl,Xs=so94.pot(g,a)
S=np.zeros((N,N)); l=0
for b in keys:
    if b==a: continue
    nb,lb=b
    for k in range(abs(l-lb),l+lb+1,2):
        coef=0.5*Q[b]*_c3j0sq(l,k,lb)
        if coef>1e-14: S+=coef*(P[b][:,None]*Gk(k)*P[b][None,:])
Xm=S@(P[a]*dr)
print("X check: max|Xm-Xs| %.3e  max|Xs| %.3e  <P|Xs> %.8f <P|Xm> %.8f"%(np.max(abs(Xm-Xs)),np.max(abs(Xs)),np.sum(P[a]*Xs*dr),np.sum(P[a]*Xm*dr)))
i=np.argmax(abs(Xm-Xs)); print("worst at r=%.3e: Xs %.4e Xm %.4e"%(r[i],Xs[i],Xm[i]))