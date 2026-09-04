import csv
rows=[r for r in csv.DictReader((l for l in open("LADDER-H-Ar-I-III.tsv") if not l.startswith("#")),delimiter="\t")]
print(f"rows: {len(rows)}")

# --- ragged-count check: bare nuclei have no row ---
from collections import Counter
cnt=Counter(int(r["Z"]) for r in rows)
exp={1:1,2:2}; exp.update({z:3 for z in range(3,19)})
print("row count per Z matches the no-bare-nucleus rule:", dict(cnt)==exp)

# --- cross-check against the INDEPENDENT screenshot capture (sequence-ordered) ---
shot={("H I"):109678.77174307,("He I"):198310.66637,("He II"):438908.878840,
      ("Li III"):987661.0139,("Be III"):1241256.601,("Li II"):610078.5260}
print("\ncross-check vs the earlier independent capture:")
for r in rows:
    if r["spectrum"] in shot:
        d=abs(float(r["IE_cm1"])-shot[r["spectrum"]])
        print(f"   {r['spectrum']:<8} {float(r['IE_cm1']):>16.6f}  diff {d:.2e}")

# --- monotone in charge at fixed Z (a physical must) ---
bad=[]
for z in sorted(cnt):
    seq=[float(r["IE_cm1"]) for r in rows if int(r["Z"])==z]
    if seq!=sorted(seq): bad.append(z)
print("\nIE rises monotonically with charge at every Z:", not bad, bad or "")

# --- electron count consistency: Ne = Z - c, and seq must be the element at Ne ---
EL="H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar".split()
bad=[(r["spectrum"],r["seq"]) for r in rows if EL[int(r["Z"])-int(r["c"])-1]!=r["seq"]]
print("isoelectronic sequence == element at Ne = Z - c:", not bad, bad or "")

# --- electrons in the shells string == Ne ---
def nel(s):
    s=s.replace("[Ne]","1s2.2s2.2p6")
    t=0
    for p in s.split("."):
        t+= int(p[2:]) if len(p)>2 else 1
    return t
bad=[(r["spectrum"],r["shells"],nel(r["shells"]),int(r["Z"])-int(r["c"])) for r in rows
     if nel(r["shells"])!=int(r["Z"])-int(r["c"])]
print("electrons in ground shells == Z - c:", not bad, bad or "")

# --- Pauli: no subshell over 2(2l+1) ---
L={"s":0,"p":1,"d":2,"f":3}
bad=[]
for r in rows:
    for p in r["shells"].replace("[Ne]","1s2.2s2.2p6").split("."):
        l=L[p[1]]; k=int(p[2:]) if len(p)>2 else 1
        if k>2*(2*l+1): bad.append((r["spectrum"],p))
print("Pauli k <= 2(2l+1) on every subshell:", not bad, bad or "")
print(f"\ngrades: " + str(Counter(r["grade"] for r in rows)))