import csv, numpy as np
R=[r for r in csv.DictReader((l for l in open("XRAY-KL3.tsv") if not l.startswith("#")),delimiter="\t")]
Z=np.array([int(r["Z"]) for r in R]); Eth=np.array([float(r["E_theory_eV"]) for r in R])
have=[i for i,r in enumerate(R) if r["E_exp_eV"].strip()]
g=np.array([r["grade"] for r in R])
print(f"rows {len(R)} · with experiment {len(have)} · measured {sum(g=='M')}"
      f" · interpolated {sum(g=='I')} · flagged {sum(g=='X')}")

# --- DOES ANALYSIS SPEAK?  Moseley: sqrt(E) = a(Z - b), a straight line. -----
y=np.sqrt(Eth); m=(g=='M')
A=np.vstack([Z[m],np.ones(m.sum())]).T
(a,b_),*_=np.linalg.lstsq(A,y[m],rcond=None)
pred=A@np.array([a,b_]); res=y[m]-pred
ss=1-(res**2).sum()/((y[m]-y[m].mean())**2).sum()
print(f"\nMOSELEY  sqrt(E) = a(Z - sigma)   on {m.sum()} measured rows, Z {Z[m].min()}-{Z[m].max()}")
print(f"   a = {a:.6f}   sigma = {-b_/a:.4f}   R^2 = {ss:.8f}")
print(f"   max |residual| = {abs(res).max():.4f} sqrt(eV)  at Z = {Z[m][abs(res).argmax()]}")
# Bohr predicts a = sqrt(3/4 * Ry) with Ry = 13.6057 eV
Ry=13.605693
print(f"   DERIVED from Bohr:  a = sqrt(3/4 * Ry) = {np.sqrt(0.75*Ry):.6f}"
      f"   ratio measured/derived = {a/np.sqrt(0.75*Ry):.4f}")
print(f"   Moseley 1913 gives sigma = 1 exactly;  measured {-b_/a:.4f}")

# where does the straight line break?  fit low-Z only, extrapolate up.
lo=m&(Z<=30); A2=np.vstack([Z[lo],np.ones(lo.sum())]).T
(a2,b2),*_=np.linalg.lstsq(A2,y[lo],rcond=None)
dev=y-(a2*Z+b2)
print(f"\n   fit on Z<=30 only: a = {a2:.6f}, sigma = {-b2/a2:.4f}")
print(f"   {'Z':>4}{'sqrt(E) obs':>13}{'linear pred':>13}{'deviation':>11}{'% of E':>9}")
for z in (20,30,40,50,60,70,80,92,100):
    i=int(np.argmin(abs(Z-z)))
    lin=a2*Z[i]+b2
    print(f"   {Z[i]:>4}{y[i]:>13.3f}{lin:>13.3f}{y[i]-lin:>11.3f}"
          f"{100*((y[i]**2)-(lin**2))/y[i]**2:>8.2f}%")