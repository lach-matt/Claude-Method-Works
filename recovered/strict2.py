import eldata as ed
from itertools import combinations
CAP=lambda l:2*(2*l+1)
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP(l)+1)]
def leq(a,b): return all(x<=y for x,y in zip(a,b))
OV={24:(3,2,5),29:(3,2,10),41:(4,2,4),42:(4,2,5),44:(4,2,7),45:(4,2,8),46:(4,2,10),
47:(4,2,10),57:(5,2,1),58:(4,3,1),64:(4,3,7),78:(5,2,9),79:(5,2,10),89:(6,2,1),
90:(6,2,2),91:(5,3,2),92:(5,3,3),93:(5,3,4),96:(5,3,7),103:(7,1,1)}
STRICT=dict(ed.E); STRICT.update(OV)
print("="*82)
print("FULL CONSEQUENCES OF THE STRICTLY MEASURED CONVENTION")
print("="*82)
for nm,cfg in [('idealised / block (used in the paper)',ed.E),('strictly measured',STRICT)]:
    occ=set(cfg.values()); zs=sorted(cfg)
    print(f"\n  {nm}")
    print(f"    distinct occupied cells         : {len(occ)}")
    ideal=not any(leq(y,x) and y not in occ for x in occ for y in L)
    print(f"    order ideal (down-set)          : {ideal}")
    cols=set((n,l) for (n,l,k) in occ)
    part=[]
    for (n,l) in cols:
        ks={k for (a,b,k) in occ if (a,b)==(n,l)}
        if ks!=set(range(1,CAP(l)+1)): part.append(((n,l),len(ks),CAP(l)))
    print(f"    occupied columns                : {len(cols)}")
    print(f"    columns NOT completely filled    : {len(part)}")
    if part:
        for c,h,cap in part: print(f"        {c[0]}{'spdfg'[c[1]]}: {h} of {cap} cells")
    maxel=[x for x in occ if not any(leq(x,y) and x!=y for y in occ)]
    print(f"    maximal occupied cells          : {len(maxel)} -> {sorted(maxel)}")
    pairs=[(a,b) for a in zs for b in zs if a!=b and leq(cfg[a],cfg[b])]
    vz=sum(1 for a,b in pairs if a>b)
    print(f"    comparable pairs                : {len(pairs)}")
    print(f"    Z-order violations              : {vz}  "
          f"{'(Z is a linear extension)' if vz==0 else '(Z is NOT a linear extension)'}")

print()
print("="*82)
print("WHY THE HOLES OCCUR — anomalies that SKIP an occupancy value")
print("="*82)
print("""  My earlier argument was that an anomaly 'relocates an electron but does not
  remove a cell an earlier element already occupied'. That is false when the
  anomaly SKIPS a value. Worked cases:""")
cases=[('3d',(3,2),4,[(23,'V',3),(24,'Cr',5),(25,'Mn',5)]),
       ('3d',(3,2),9,[(28,'Ni',8),(29,'Cu',10),(30,'Zn',10)]),
       ('4d',(4,2),9,[(45,'Rh',8),(46,'Pd',10),(47,'Ag',10)]),
       ('5d',(5,2),8,[(77,'Ir',7),(78,'Pt',9),(79,'Au',10)])]
for nm,col,miss,seq in cases:
    print(f"\n    {nm} k={miss} is never realised:")
    for z,sym,k in seq: print(f"        Z={z:3d} {sym:<3} {nm}^{k}")
    print(f"        → the sequence jumps over {nm}^{miss}")
print("""
  So the accumulated set has genuine holes under measurement. The down-set
  property is a property of the IDEALISED assignment, not of the measured
  periodic system, and the paper must say so.""")