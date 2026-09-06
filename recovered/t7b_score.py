"""t7b_score.py -- score T7b against PREDICTION-T7-SESSION-16 PB1-PB4; write RUN-T7B-SESSION-18.txt"""
import json
R={json.loads(l)['Z']:json.loads(l) for l in open('t7b.jsonl')}
order=[66,68,69,70,26,57,64,71,21,29]
out=[]; p=out.append
p("RUN-T7B-SESSION-18  HF (Fock, av-config) TS = eps(N-1/2)+J~/2 and dSCF vs T5 HFS and T7c SR; all Ha; % = (calc-meas)/|meas|")
p(f"{'el':<3}{'sh':>3}{'meas':>8}{'hfs_ts':>8}{'ts_pol':>8}{'t7c_ts':>8}{'hf_ts':>8}{'hf_dscf':>8}{'%hfts':>7}{'%hfdscf':>8}{'sh_ts':>7}{'ts/dscf':>8}")
pb1=pb2=pb3=0
for Z in order:
    r=R[Z]; m=r['meas']; ts=r['hf_ts']; ds=r['hf_dscf']
    pts=100*(ts-m)/abs(m); pds=100*(ds-m)/abs(m); rat=abs(ts-ds)/abs(ds)*100
    tp=r['ts_pol'] if r['ts_pol'] is not None else float('nan')
    p(f"{r['el']:<3}{r['sh']:>3}{m:8.4f}{r['hfs_ts']:8.4f}{tp:8.4f}{r['t7c_ts']:8.4f}{ts:8.4f}{ds:8.4f}{pts:7.1f}{pds:8.1f}{r['shift_ts']:7.4f}{rat:8.1f}")
    if r['sh']=='4f' and abs(pds)<=30: pb1+=1
    if rat<=10: pb2+=1
    if r['sh'] in('3d','5d') and abs(pts)<=15: pb3+=1
p("")
p(f"PB1  HF-dSCF 4f within 30% for >=3 of Dy/Er/Tm/Yb : {pb1}/4  -> {'HOLDS' if pb1>=3 else 'FAILS'}")
p(f"PB2  HF-TS agrees with HF-dSCF within 10%         : {pb2}/10 -> {'HOLDS' if pb2==10 else 'FAILS'}")
p(f"PB3  3d/5d HF-TS within 15%                       : {pb3}/6  -> {'HOLDS' if pb3==6 else 'FAILS'}")
p("PB4  cannot fire (PC1 gave the whole offset, session 17); exact-exchange branch not the direction.")
open('RUN-T7B-SESSION-18.txt','w').write("\n".join(out)+"\n"); print("\n".join(out))