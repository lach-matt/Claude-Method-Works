import numpy as np, eldata as ed
MN={21:19,22:51,23:54,24:57,26:61,27:64,28:67,29:72,39:20,40:49,41:53,42:56,
44:62,45:65,46:69,47:71,57:33,58:32,59:31,60:30,62:28,63:18,64:27,65:26,66:25,
67:24,68:23,69:22,70:17,71:21,72:50,73:52,74:55,75:58,77:63,78:66,79:70,90:47,92:45,
1:92,3:1,4:77,5:86,6:95,7:100,8:101,9:102,11:11,12:73,13:80,14:85,15:90,16:94,17:99,
19:10,20:16,30:76,31:81,32:84,33:89,34:93,35:98,37:9,38:15,48:75,49:79,50:83,51:88,
52:92,53:97,55:8,56:14,80:74,81:78,82:82,83:87,84:91,85:96}
com=sorted(z for z in MN if z in ed.E)
mn=np.array([MN[z] for z in com],float)
n=np.array([ed.E[z][0] for z in com],float)
l=np.array([ed.E[z][1] for z in com],float)
k=np.array([ed.E[z][2] for z in com],float)
def onehot(v):
    u=sorted(set(v)); return np.column_stack([(v==x).astype(float) for x in u[1:]])
Xa=np.column_stack([np.ones(len(mn)),onehot(n),onehot(l),onehot(k)])
ba,*_=np.linalg.lstsq(Xa,mn,rcond=None); pa=Xa@ba

print("="*80); print("IS THE ADDITIVE FIT REAL? — inspect the f-block predictions"); print("="*80)
print("  Additive model f(n)+g(ℓ)+h(k) has ∂/∂k = h'(k), independent of ℓ,")
print("  so it CANNOT reproduce a sign flip. Check what it does to lanthanides:\n")
print(f"  {'sym':>4} {'(n,ℓ,k)':>12} {'MN obs':>8} {'MN pred':>9} {'resid':>8}")
lan=[(i,z) for i,z in enumerate(com) if ed.E[z][1]==3 and ed.E[z][0]==4]
for i,z in sorted(lan,key=lambda t:ed.E[t[1]][2]):
    print(f"  {ed.SYM[z]:>4} {str(ed.E[z]):>12} {mn[i]:>8.0f} {pa[i]:>9.1f} {mn[i]-pa[i]:>8.1f}")
resid_lan=np.array([mn[i]-pa[i] for i,z in lan])
print(f"\n  lanthanide residual SD = {resid_lan.std():.1f}   mean |resid| = {np.abs(resid_lan).mean():.1f}")
other=[i for i in range(len(com)) if not (ed.E[com[i]][1]==3 and ed.E[com[i]][0]==4)]
ro=mn[other]-pa[other]
print(f"  all-other residual SD  = {ro.std():.1f}   mean |resid| = {np.abs(ro).mean():.1f}")
print(f"  ratio: lanthanide errors are {np.abs(resid_lan).mean()/np.abs(ro).mean():.1f}× larger")
print()
print("""  So the additive model's R²=0.69 is achieved by fitting the s/p/d blocks
  well and the f-block badly. The high overall R² masks systematic failure
  exactly where the sign flip lives. My earlier statement that additive
  models are 'capped' was right in substance but the number 0.69 overstates
  how well they work.""")
print()
print("="*80); print("HOW MANY PARAMETERS IS THE ADDITIVE MODEL SPENDING?"); print("="*80)
print(f"  additive: {Xa.shape[1]} parameters for {len(mn)} data points")
print(f"  ratio {Xa.shape[1]/len(mn):.2f} — one parameter per {len(mn)/Xa.shape[1]:.1f} elements")
print(f"  the quadratic model used 6 parameters for LOO 0.554")
print(f"  the additive model uses {Xa.shape[1]} for LOO 0.690")
print(f"  → additive buys +0.14 LOO for +{Xa.shape[1]-6} parameters. Poor trade.")