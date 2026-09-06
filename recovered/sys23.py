import numpy as np, eldata as ed
from scipy import stats
from collections import Counter
zs=sorted(ed.E)
print("="*80); print("SYSTEM 2 — STRUCTURAL SORTING"); print("="*80)
print("""  Measurement basis: observed crystal structures and compound formation.
  Canonical orderings:
    S1  Pettifor Mendeleev number MN   [Pettifor 1984] — empirical, from
        binary AB structure maps; optimised so similar elements are adjacent
    S2  Villars Periodic Number PN     [Villars 2000s] — rows = principal
        quantum number, emphasises valence-electron count
    S3  modified/data-mined Pettifor   [Glawe 2016; Allahyari & Oganov 2020]
  Observable anchors: ICSD structure types, substitution probability
  matrices, structure-map separation quality.""")
MN={21:19,22:51,23:54,24:57,26:61,27:64,28:67,29:72,39:20,40:49,41:53,42:56,
44:62,45:65,46:69,47:71,57:33,58:32,59:31,60:30,62:28,63:18,64:27,65:26,66:25,
67:24,68:23,69:22,70:17,71:21,72:50,73:52,74:55,75:58,77:63,78:66,79:70,90:47,92:45,
1:92,3:1,4:77,5:86,6:95,7:100,8:101,9:102,11:11,12:73,13:80,14:85,15:90,16:94,17:99,
19:10,20:16,30:76,31:81,32:84,33:89,34:93,35:98,37:9,38:15,48:75,49:79,50:83,51:88,
52:92,53:97,55:8,56:14,80:74,81:78,82:82,83:87,84:91,85:96}
common=[z for z in zs if z in MN]
print(f"\n  elements with Pettifor MN available: {len(common)}")
n=np.array([ed.E[z][0] for z in common],float)
l=np.array([ed.E[z][1] for z in common],float)
k=np.array([ed.E[z][2] for z in common],float)
mn=np.array([MN[z] for z in common],float)
Z=np.array(common,float)
print(f"\n  {'quantity':<20}{'Pearson r vs MN':>18}{'Spearman ρ':>14}")
print("  "+"-"*52)
for nm,x in [('Z',Z),('n',n),('ℓ',l),('k',k),('n+ℓ',n+l),('n+ℓ+k',n+l+k),
             ('|Q₀|',np.sqrt(n*n+l*l+k*k))]:
    r,_=stats.pearsonr(x,mn); rho,_=stats.spearmanr(x,mn)
    print(f"  {nm:<20}{r:>18.4f}{rho:>14.4f}")
def loo(cols):
    X=np.column_stack([np.ones(len(mn))]+cols); pr=np.zeros(len(mn))
    for i in range(len(mn)):
        m=np.ones(len(mn),bool); m[i]=False
        b,*_=np.linalg.lstsq(X[m],mn[m],rcond=None); pr[i]=X[i]@b
    return 1-np.sum((mn-pr)**2)/np.sum((mn-np.mean(mn))**2)
print(f"\n  predicting MN (cross-validated R²):")
for nm,c in [('Z',[Z]),('n',[n]),('ℓ',[l]),('k',[k]),('n,ℓ',[n,l]),
             ('n,ℓ,k  = Λ coords',[n,l,k]),('n,ℓ,k,ℓ²,k²',[n,l,k,l*l,k*k])]:
    print(f"    {nm:<22} {loo(c):+.4f}")
print("""
  VILLARS' CLAIM (Villars et al. 2001): 'the atomic number, the group number
  and the main quantum numbers THEMSELVES lose this information and therefore
  are not able to describe former/nonformer behaviours', whereas MN scales
  retain 'periodicity within the group and its sequence depending on the
  main quantum number'.  Test it directly above: Z alone vs (n,ℓ,k).""")

print()
print("="*80); print("SYSTEM 3 — INTEGRAL SORTING"); print("="*80)
print("""  Measurement basis: integer counts of nucleons.
    I1  atomic number Z          — Moseley 1913, nuclear charge
    I2  mass number A            — Mendeleev's original atomic-weight order
    I3  neutron number N = A − Z
  Observable anchors: X-ray spectra (Moseley's law √ν ∝ Z−1), mass
  spectrometry, nuclear binding energy, magic numbers 2,8,20,28,50,82,126.""")
A={1:1,2:4,3:7,4:9,5:11,6:12,7:14,8:16,9:19,10:20,11:23,12:24,13:27,14:28,15:31,
16:32,17:35,18:40,19:39,20:40,21:45,22:48,23:51,24:52,25:55,26:56,27:59,28:58,
29:63,30:64,31:69,32:74,33:75,34:80,35:79,36:84,37:85,38:88,39:89,40:90,41:93,
42:98,43:98,44:102,45:103,46:106,47:107,48:114,49:115,50:120,51:121,52:130,53:127,
54:132,55:133,56:138,57:139,58:140,59:141,60:142,61:145,62:152,63:153,64:158,
65:159,66:164,67:165,68:166,69:169,70:174,71:175,72:180,73:181,74:184,75:187,
76:192,77:193,78:195,79:197,80:202,81:205,82:208,83:209}
cm=[z for z in zs if z in A]
Zc=np.array(cm,float); Ac=np.array([A[z] for z in cm],float); Nc=Ac-Zc
print(f"\n  elements with mass data: {len(cm)}")
tau,_=stats.kendalltau(Zc,Ac)
print(f"  Kendall τ(Z, A) = {tau:.4f}   (Mendeleev's weight order vs Moseley's Z)")
inv=[(cm[i],cm[j]) for i in range(len(cm)) for j in range(i+1,len(cm)) if Ac[i]>Ac[j]]
print(f"  Z/A inversions: {len(inv)} -> {[(ed.SYM[a],ed.SYM[b]) for a,b in inv]}")
print("  These are exactly the pairs Mendeleev had to transpose against weight.")
print()
MAGIC={2,8,20,28,50,82,126}
print("  Do NUCLEAR magic numbers appear anywhere in Λ?")
for m in sorted(MAGIC):
    if m in ed.E:
        print(f"    Z={m:3d} {ed.SYM[m]:>3}: Λ coord {ed.E[m]}, rank {sum(ed.E[m])}")
mr=[sum(ed.E[m]) for m in MAGIC if m in ed.E]
allr=[sum(ed.E[z]) for z in zs]
print(f"  magic-Z lattice ranks: {sorted(mr)}")
print(f"  mean rank of magic-Z {np.mean(mr):.2f} vs all elements {np.mean(allr):.2f}")
t,p=stats.ttest_1samp(mr,np.mean(allr))
print(f"  t-test: t={t:+.2f}, p={p:.3f}  → {'DIFFERENT' if p<0.05 else 'no difference'}")