import sys,json,os,warnings; warnings.filterwarnings('ignore')
from hfs_sic import scf_sic
from t5_scf import ground_occ, minus
T5={json.loads(l)['Z']:json.loads(l) for l in open('t5.jsonl')}
done=set(json.loads(l)['Z'] for l in open('t6.jsonl')) if os.path.exists('t6.jsonl') else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: continue
    r5=T5[Z]; n,l=int(r5['sh'][0]),"spdf".index(r5['sh'][1]); hole=minus(ground_occ(Z),n,l,1.0)
    Es0,h0,s=scf_sic(Z,1,occ=hole,entrant=(n,l),sic=False); e0=Es0[(n,l,s)]
    Es1,h1,s=scf_sic(Z,1,occ=hole,entrant=(n,l),sic=True); e1=Es1[(n,l,s)]
    r=dict(Z=Z,el=r5['el'],sh=r5['sh'],meas=r5['meas'],ts_avg=r5['hfs_ts'],ts_pol=round(e0,4),ts_sic=round(e1,4),chan=s,it=[len(h0),len(h1)])
    open('t6.jsonl','a').write(json.dumps(r)+'\n'); print(r,flush=True)