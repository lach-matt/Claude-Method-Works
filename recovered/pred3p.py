import csv, numpy as np
def load(p): return {(r["El"],r["A"]):r for r in csv.DictReader((l for l in open(p) if not l.startswith("#")),delimiter="\t")}
A3,A2=load("XRAY-KL3.tsv"),load("XRAY-KL2.tsv")
K=[k for k in A3 if k in A2]
Z=np.array([int(A3[k]["Z"]) for k in K])
D2=np.array([float(A3[k]["E_theory_eV"])-float(A2[k]["E_theory_eV"]) for k in K])
g=np.array([A3[k]["grade"] for k in K]); el=[k[0] for k in K]
al=7.2973525693e-3; mc2=510998.95
# shared parameterisation: dE = (Z-s)^4 a^4 mc^2 / (2 n^3 l(l+1)),  l=1
C=lambda n: al**4*mc2/(2*n**3*2)
print(f"  shared form  dE = (Z-s)^4 · a^4·mc^2 / (2 n^3 l(l+1))")
print(f"     n=2 coefficient {C(2):.4e} eV   n=3 {C(3):.4e} eV")
print(f"     ratio 3p/2p at equal (Z-s) = (2/3)^3 = {8/27:.4f}  — NO free parameter\n")
ok=(g=='M')&(Z>=12)
print("  THE 2p BASELINE, and the 3p value it predicts:\n")
print(f"  {'el':>3}{'Z':>4}{'2p obs eV':>12}{'sigma_2p':>10}{'3p PREDICTED':>14}")
for z in (20,26,30,36,42,47,54,60,70,74,79,82,92):
    i=int(np.argmin(np.abs(Z-z)))
    if not ok[i]: continue
    s = Z[i] - (D2[i]/C(2))**0.25          # sigma implied by the 2p splitting
    p3 = C(3)*(Z[i]-s)**4                  # same sigma, n=3
    print(f"  {el[i]:>3}{Z[i]:>4}{D2[i]:>12.2f}{s:>10.3f}{p3:>14.2f}")
print("\n  TEST: L1M3 − L1M2 should equal the last column, to within the")
print("  screening difference between 2p and 3p. If instead it needs a")
print("  DIFFERENT n-power, they are not one object.")