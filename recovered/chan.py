import numpy as np
def V3(nu):
    d0=1/nu**2-1/(nu+1)**2; d1=1/(nu+1)**2-1/(nu+2)**2
    return 2*abs(d0+d1)/abs(d0-d1)
def Vcell(nuc): return V3(nuc-1.0)

def V_block(ns, delta):
    """paper's V: ratio of MEANS over interior cells of a contiguous block"""
    nu = np.array(ns,float)-delta
    T = 1.0/nu**2
    w = np.abs(T[:-2]-T[2:])
    e = np.abs(T[1:-1]-0.5*(T[:-2]+T[2:]))
    return w.sum()/e.sum(), np.median(w/e), nu[1:-1]

print("=== Ba I 6snf, n=17-25 (paper measures V = 27.0 on Curry's levels) ===")
for d in [0.10,0.16,0.20,0.25]:
    Vr,Vm,nui = V_block(range(17,26), d)
    print(f"  delta={d:4.2f}  nu_bar={nui.mean():5.2f}  V(ratio of means)={Vr:6.2f}   "
          f"median per-cell V={Vm:6.2f}   4*nu_bar/3={4*nui.mean()/3:6.2f}")

print("\n=== forward predictions: V for channels already in the paper's dataset ===")
print("   channel                        delta   n-range     nu-range      V pred")
chans = [
 ("Kr I (2P3/2) ns",        3.10, range(5,16)),
 ("Kr I (2P1/2) np",        2.60, range(5,8)),
 ("Sc III nd",              0.63, range(4,15)),
 ("Ca I 4snd",              0.80, range(4,16)),
 ("Ca I 4snf",              0.15, range(4,16)),
 ("Sr I 5snf",              0.07, range(4,16)),
 ("Ba I 6snf (block)",      0.16, range(17,26)),
 ("Sc I 3d4s(1D)np 2P",     2.00, range(9,39)),
 ("Mg I 3snd 1D",           0.50, range(4,16)),
]
for name,d,ns in chans:
    ns=list(ns)
    if len(ns)<3: continue
    Vr,Vm,nui = V_block(ns,d)
    print(f"   {name:28s} {d:5.2f}  {ns[0]:2d}-{ns[-1]:2d}   {nui.min():5.2f}-{nui.max():5.2f}   "
          f"{Vr:7.2f}  (median cell {Vm:6.2f})")

print("\n=== sensitivity of the low-nu cases to delta ===")
for d in [2.4,2.6,2.8,3.0,3.2]:
    Vr,_,nui=V_block([5,6,7],d)
    print(f"  Kr I np, delta={d:4.2f}: nu(6p)={nui[0]:4.2f}  V={Vr:5.2f}")
for d in [2.8,3.0,3.1,3.3]:
    Vr,_,nui=V_block(range(5,10),d)
    print(f"  Kr I ns n=5-9, delta={d:4.2f}: nu range {nui.min():.2f}-{nui.max():.2f}  V={Vr:5.2f}")

print("\n=== absolute floor for a *resolved* Rydberg channel ===")
print("   V(cell) at nu = 2,2.5,3,4 :", [round(Vcell(x),3) for x in [2,2.5,3,4]])