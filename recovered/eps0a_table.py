"""eps0a_table.py -- s23: tabulate eps0^a(zeta) [Ha] from ring_zeta at rs=0.01,0.005 with two-point r_s ln r_s extrapolation. Writes eps0a_table.json."""
import numpy as np, json, ring_zeta as R
zs=list(np.round(np.arange(0,0.901,0.05),3))+[0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99,0.995,0.999,1.0]
rho=(0.005*np.log(0.005))/(0.01*np.log(0.01))
out={"zeta":[],"eps0a_Ha":[],"c005":[],"c01":[],"rho":rho,"note":"eps0a=(c(0.005)-rho*c(0.01))/(1-rho); ring_zeta grids 1400x1400"}
for z in zs:
    c1=(R.eps_r(0.01,z)-R.cL(z)*np.log(0.01))/2; c5=(R.eps_r(0.005,z)-R.cL(z)*np.log(0.005))/2
    e=(c5-rho*c1)/(1-rho); out["zeta"].append(float(z)); out["eps0a_Ha"].append(float(e)); out["c005"].append(float(c5)); out["c01"].append(float(c1))
    print(f"{z:6.3f} {c1:.5f} {c5:.5f} -> {e:.5f}",flush=True)
json.dump(out,open("eps0a_table.json","w"))