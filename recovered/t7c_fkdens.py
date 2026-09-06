"""t7c_fkdens.py -- s23: F^k on 4f orbitals from the SIC-noclamp / Z chains (t7c_corrz), TS-orbital vs own-orbital Hund-II. usage: DENS Z..."""
import json,sys,os,time,numpy as np
assert os.environ.get("SIC_NOCLAMP")=="1"
from t7c_corrz import scf_sic_corr
from t7c_mult import Fk,ci
from t5_scf import ground_occ,minus
HOLES={66:(4,5),68:(2,3),69:(1,2),70:(0,1)}
dens_mode=sys.argv[1]; corr=None if dens_mode=="SIC" else "Z"
def orb(Z,k):
    if abs(k-0.5)<1e-9:
        Es,h,s=scf_sic_corr(Z,1,occ=minus(ground_occ(Z),4,3,1.0),entrant=(4,3),mode="all",corr=corr); key=[c for c in scf_sic_corr.last['dens'] if c[0]==4 and c[1]==3 and c[5]=='ent'][0]
    else:
        Es,h,s=scf_sic_corr(Z,1,occ=minus(ground_occ(Z),4,3,k),entrant=None,mode="all",corr=corr); key=[c for c in scf_sic_corr.last['dens'] if c[0]==4 and c[1]==3 and c[3]=='d'][0]
    L=scf_sic_corr.last; u=np.sqrt(np.maximum(L['dens'][key],0)); u=u/np.sqrt(np.sum(u*u*L['dr'])); return Fk(u,L['r'],L['dr'])
D={json.loads(l)['Z']:json.loads(l) for l in open('t7c_dyaudit.jsonl')}
out=f't7c_fkdens_{dens_mode}.jsonl'; done={json.loads(l)['Z'] for l in open(out)} if os.path.exists(out) else set()
for Z in map(int,sys.argv[2:]):
    if Z in done: continue
    t0=time.time(); F={}
    for tag,k in (('ts',0.5),('neu',0.0),('ion',1.0)): F[tag]=orb(Z,k)
    kn,ki=HOLES[Z]; d=D[Z]
    hund_ts=ci(kn,F['ts'])-ci(ki,F['ts']); hund_own=ci(kn,F['neu'])-ci(ki,F['ion'])
    row=dict(Z=Z,dens=dens_mode,F2=dict((t,round(F[t][2],4)) for t in F),F2_pol=d['F2'],hund_ts=round(hund_ts,4),hund_own=round(hund_own,4),
             hund_ts_pol=round(d['stab_n_ts']-d['stab_i_ts'],4),hund_own_pol=round(d['stab_n_own']-d['stab_i_own'],4),sec=int(time.time()-t0))
    open(out,'a').write(json.dumps(row)+'\n'); print(row,flush=True)