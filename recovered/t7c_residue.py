"""t7c_residue.py -- session 18: SR re-probe of the relativistic corridor residues (bridge-17 s3(2)b; R 1578 class).
Object = T0b probe: eigen on tfd.potential(Z, Z-N) at zeta=2 for the pair; kinetic language nonrel (eigen_fix) vs SR (t7c_kernel
eigen_sr, c=137.035999, no constant). Gate: SR at c=1e6 regenerates the T0b baseline d to 1e-4.
PREDICTIONS (before run): PR1 Ra II d=E(6d)-E(7s): -0.0018 -> >0, rise >= +0.02, toward meas +0.055.
PR2 Th IV d=E(5f)-E(6d) <0 stays <0 (hold preserved), moves up. PR3 Lr I d=E(7p)-E(6d) moves down by >= 0.03; crossing uncertain."""
import io, contextlib, numpy as np, warnings; warnings.filterwarnings("ignore")
with contextlib.redirect_stdout(io.StringIO()): import tfd
import eigen_fix
from t7c_kernel import eigen_sr, C0
IONS=[("Ra II",88,86,[(7,0),(6,2)],"7s<6d",+0.055),("Th IV",90,86,[(6,2),(5,3)],"5f<6d hold",None),
      ("Lr I",103,102,[(6,2),(7,1)],"7p<6d",None),("Sr II",38,36,[(5,0),(4,2)],"5s<4d (control)",+0.07)]
L="spdf"; out=["SR RE-PROBE (session 18)  d = E(second)-E(first), Ha"]
out.append(f"{'ion':<7}{'pair':>8}{'meas':>8}{'nonrel':>9}{'sr(c=1e6)':>10}{'sr':>9}{'shift':>8}  first/second SR shifts")
for lab,Z,N,pairs,order,meas in IONS:
    V,_=tfd.potential(Z,Z-N)
    e0=[eigen_fix.eigen(V,l,n,2.0,Z) for n,l in pairs]
    ei=[eigen_sr(V,l,n,2.0,Z,c=1e6) for n,l in pairs]
    es=[eigen_sr(V,l,n,2.0,Z) for n,l in pairs]
    d0,di,ds=e0[1]-e0[0],ei[1]-ei[0],es[1]-es[0]
    out.append(f"{lab:<7}{pairs[1][0]}{L[pairs[1][1]]}-{pairs[0][0]}{L[pairs[0][1]]:>3}{(meas if meas is not None else float('nan')):8.3f}{d0:9.4f}{di:10.4f}{ds:9.4f}{ds-d0:8.4f}  {es[0]-e0[0]:+.4f}/{es[1]-e0[1]:+.4f}  [{order}]")
open('RUN-T7C-RESIDUE-SESSION-18.txt','w').write("\n".join(out)+"\n"); print("\n".join(out))