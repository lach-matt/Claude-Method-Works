# diagnostic: non-symmetric exchange sqrt(M_i/M_j) kept; l=0, 1s and 7s only
import sys,os,numpy as np,scipy.linalg as sla
sys.argv=['v5a.py','ent','--lmax','-1']; exec(open('v5a.py').read().split("out={}")[0])
S=exch_S(0)
for a in [(1,0),(7,0)]:
    Eref=eps[a]; M=1+(Eref-Vdir)/(2*c*c); Mp=-Vp/(2*c*c); Mpp=-Vpp/(2*c*c); Dref=-Mp/(r*M)-Mpp/(2*M)+3*Mp*Mp/(4*M*M)
    A=-FD2+np.diag((0.5)**2+r*r*(2*M*Vdir+Dref)); Bd=2*r*r*M; Bi=1/np.sqrt(Bd)
    C=A*Bi[:,None]*Bi[None,:]; C-=np.sqrt(M)[:,None]*np.sqrt(r)[:,None]*S*np.sqrt(r)[None,:]*h/np.sqrt(M)[None,:]
    w=sla.eigvals(C); w=w.real; j=np.argmin(abs(w-eps[a])); print("ASYM",a,"sealed %.6f asym-lin %.6f dE %+.2e"%(eps[a],w[j],w[j]-eps[a]),flush=True)