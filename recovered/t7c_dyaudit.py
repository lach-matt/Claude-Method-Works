"""T7c-DYAUDIT s22: F^k from neutral / ion / TS 4f orbital; stab per configuration with its own orbital. No constant."""
import json,sys,numpy as np
from t7c_mult import Fk,ci,C0
from t7c_pol import scf_pol_sr,numerov_wf_sr
from t5_scf import ground_occ,minus
HOLES={66:(4,5),68:(2,3),69:(1,2),70:(0,1)}
def orb(Z,k):
    probe,Es,h=scf_pol_sr(Z,1,occ=minus(ground_occ(Z),4,3,k),c=C0)
    cells={n:c.cell_contents for n,c in zip(probe.__code__.co_freevars,probe.__closure__)}
    Vf=cells['Vf']; s='d' if k<7 else 'u'
    rr,drr,u,E,nd=numerov_wf_sr(Vf[s][0],3,4,1.0,Z,C0,Vp=Vf[s][1],Vpp=Vf[s][2])
    u=u/np.sqrt(np.sum(u*u*drr)); return Fk(u,rr,drr),E
M={json.loads(l)['Z']:json.loads(l) for l in open('t7c_mult.jsonl')}
for Z in map(int,sys.argv[1:]):
    F={}; 
    for tag,k in (('ts',0.5),('neu',0.0),('ion',1.0)): F[tag],_=orb(Z,k)
    kn,ki=HOLES[Z]; m=M[Z]
    sn_ts,si_ts=ci(kn,F['ts']),ci(ki,F['ts']); sn,si=ci(kn,F['neu']),ci(ki,F['ion'])
    corr_ts=m['t7c_pol']+sn_ts-si_ts; corr=m['t7c_pol']+sn-si
    row=dict(Z=Z,el=m['el'],F2=dict((t,round(F[t][2],4)) for t in F),stab_n_ts=round(sn_ts,4),stab_i_ts=round(si_ts,4),
        stab_n_own=round(sn,4),stab_i_own=round(si,4),corr_banked=m['corr'],corr_ts=round(corr_ts,4),corr_own=round(corr,4),
        delta=round(corr-corr_ts,4),meas=m['meas'])
    open('t7c_dyaudit.jsonl','a').write(json.dumps(row)+'\n'); print(row,flush=True)