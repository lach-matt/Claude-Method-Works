"""t7c_ionts.py -- session 18, bridge-18 s3(1'): (A) inspection check: pol SC-SR on the closed-core corridor object regenerates SC-SR
(structural null); (B) CANDIDATE, change of object (R 1578 flag): TS-with-self on the ion — probe shell at 1/2 occupancy INSIDE the
polarised SR SCF (one SCF per shell, T5 TS convention), d = e(4f) - e(5d). nr = c=1e6, sr = c=137.035999. Prediction (chat, before run):
(A) |d_pol - d_SCSR| < 1e-4; (B) d rises toward meas on Ce IV and Pr V by 0.05-0.15 Ha, not to closure."""
import sys, json, io, contextlib, warnings; warnings.filterwarnings("ignore")
with contextlib.redirect_stdout(io.StringIO()): import tfd
from t5_scf import ground_occ
from t7c_pol import scf_pol_sr
from t7c_kernel import C0
ION={"CeIV":(58,54,4,-0.227),"PrV":(59,54,5,-0.524),"RaII":(88,86,2,0.055)}
lab=sys.argv[1]; Z,N,q,meas=ION[lab]; g=ground_occ(N)
pairs={"CeIV":[(5,2),(4,3)],"PrV":[(5,2),(4,3)],"RaII":[(7,0),(6,2)]}[lab]
out={}
for mode,c in (("nr",1e6),("sr",C0)):
    pr,Es,h=scf_pol_sr(Z,q,occ=g,c=c); eA=[pr(n,l)[0] for n,l in pairs]
    eB=[]
    for n,l in pairs:
        pr2,Es2,h2=scf_pol_sr(Z,q,occ=g+[(n,l,0.5)],c=c); eB.append(Es2[(n,l,"u")] if (n,l,"u") in Es2 else pr2(n,l)[0])
    out[mode]=dict(A=round(eA[1]-eA[0],5),B=round(eB[1]-eB[0],5),eA=[round(e,4) for e in eA],eB=[round(e,4) for e in eB])
row=dict(ion=lab,meas=meas,**out); open('t7c_ionts.jsonl','a').write(json.dumps(row)+'\n'); print(row)