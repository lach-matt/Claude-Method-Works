"""t7sum.py -- session 18: the SUM candidate T7c + T7b (comparison rule, PREDICTION-T7 s'Comparison rule'; R 1449 timing).
Additive form: SR-TS + (HF-TS - HFS-TS) on the spin-averaged object; SR-pol-TS + same shift on the polarised object.
Additivity of independent shifts validated at <= 0.003 Ha for the pol step (session 17). Prediction (before run): all four 4f
overshoot shallow on both objects; 5d unchanged from T7c; Cu breaks."""
import json
B={json.loads(l)['Z']:json.loads(l) for l in open('t7b.jsonl')}
C={json.loads(l)['Z']:json.loads(l) for l in open('t7c.jsonl')}
P={}
for l in open('t7c_pol.jsonl'):
    j=json.loads(l); P[j['Z']]=j
keys=set(next(iter(P.values())).keys()) if P else set()
out=[f"SUM T7c+T7b (session 18); % vs meas.  pol keys: {sorted(keys)}"]
out.append(f"{'el':<3}{'sh':>3}{'meas':>8}{'t7c_ts':>8}{'hf_sh':>7}{'sum_avg':>8}{'%':>7}{'sr_pol':>8}{'sum_pol':>8}{'%':>7}")
band=0
for Z in [66,68,69,70,26,57,64,71,21,29]:
    b=B[Z]; m=b['meas']; sh=b['shift_ts']; sa=C[Z]['t7c_ts']+sh
    pk=[k for k in keys if 'pol' in k and isinstance(P.get(Z,{}).get(k),(int,float))]
    sp=P[Z][pk[0]] if (Z in P and pk) else None
    spol=(sp+sh) if sp is not None else float('nan'); ppol=100*(spol-m)/abs(m) if sp is not None else float('nan')
    pa=100*(sa-m)/abs(m)
    if b['sh']=='4f' and abs(pa)<=15: band+=1
    out.append(f"{b['el']:<3}{b['sh']:>3}{m:8.4f}{C[Z]['t7c_ts']:8.4f}{sh:7.4f}{sa:8.4f}{pa:7.1f}{(sp if sp is not None else float('nan')):8.4f}{spol:8.4f}{ppol:7.1f}")
out.append(f"4f inside 15% band on the spin-averaged sum: {band}/4")
open('SUM-T7-SESSION-18.txt','w').write("\n".join(out)+"\n"); print("\n".join(out))