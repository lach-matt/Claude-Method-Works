import csv, numpy as np
def load(p):
    return {(r["El"],r["A"]):r for r in csv.DictReader(
        (l for l in open(p) if not l.startswith("#")),delimiter="\t")}
A3,A2=load("XRAY-KL3.tsv"),load("XRAY-KL2.tsv")
keys=[k for k in A3 if k in A2]
Z=[];D=[];g=[]
for k in keys:
    Z.append(int(A3[k]["Z"]))
    D.append(float(A3[k]["E_theory_eV"])-float(A2[k]["E_theory_eV"]))
    g.append(A3[k]["grade"])
Z=np.array(Z);D=np.array(D);g=np.array(g)
print(f"paired rows: {len(keys)}   (Ka1 - Ka2, theory, eV)")
print(f"{'Z':>4}{'splitting eV':>14}{'/ Z^4 x1e8':>13}")
for z in (10,20,30,40,50,60,70,80,92,100):
    i=int(np.argmin(abs(Z-z)))
    print(f"{Z[i]:>4}{D[i]:>14.2f}{1e8*D[i]/Z[i]**4:>13.3f}")

# the 2p spin-orbit splitting: DIRAC gives dE ~ Z_eff^4 alpha^2 Ry / 24 for n=2
m=(g=='M')
lz,ld=np.log(Z[m]),np.log(D[m])
sl,ic=np.polyfit(lz,ld,1)
ss=1-((ld-(sl*lz+ic))**2).sum()/((ld-ld.mean())**2).sum()
print(f"\nPOWER LAW  splitting ~ Z^p   on {m.sum()} measured rows")
print(f"   p = {sl:.4f}     R^2 = {ss:.6f}")
print(f"   DERIVED: the 2p fine structure is a spin-orbit term, dE = Z^4 a^2 Ry/24")
print(f"   -> p = 4 exactly.   measured/derived = {sl/4:.4f}")
lo=m&(Z<=30); s2,i2=np.polyfit(np.log(Z[lo]),np.log(D[lo]),1)
print(f"   fitted on Z<=30 only: p = {s2:.4f}   ({100*(s2/4-1):+.1f}% from 4)")
al=7.2973525693e-3; Ry=13.605693
pred=lambda z: z**4*al**2*Ry/24
print(f"\n{'Z':>4}{'observed':>12}{'Z^4 a^2 Ry/24':>16}{'ratio':>9}")
for z in (10,20,30,40,60,80,92):
    i=int(np.argmin(abs(Z-z)))
    print(f"{Z[i]:>4}{D[i]:>12.2f}{pred(Z[i]):>16.2f}{D[i]/pred(Z[i]):>9.4f}")