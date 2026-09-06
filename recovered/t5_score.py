import json
K={(r[0],r[1]):(r[2],r[3]) for r in json.load(open('/home/claude/work/LOWDIN-HANDOFF-14/LOWDIN-HANDOFF-14/pack9/T0b_pairs.json'))}
R=sorted((json.loads(l) for l in open('t5.jsonl')),key=lambda r:r['Z'])
print(f"{'el':<3}{'sh':>3}{'meas':>8}{'TFD_K':>8}{'TFD_TS':>8}{'SCF_K':>8}{'HFS_TS':>8}{'DSCF':>8} {'TS%':>6}{'DS%':>6}{'TS/DS':>7}")
n30=0; pc1t=pc1h=0; early={'Sc','Ti','La','Gd'}; late={'Fe','Ni','Cu','Dy','Er','Tm','Yb'}
gap={}
for r in R:
    tk,sk=K[(r['Z'],r['sh'])]; m=r['meas']
    ts=100*(r['hfs_ts']-m)/abs(m); ds=100*(r['dscf']-m)/abs(m); rat=r['hfs_ts']/r['dscf']
    if abs(ds)<=30: n30+=1
    if r['tfd_ts']>tk: pc1t+=1
    if r['hfs_ts']>sk: pc1h+=1
    gap[r['el']]=(sk-m, r['hfs_ts']-m)
    print(f"{r['el']:<3}{r['sh']:>3}{m:8.4f}{tk:8.4f}{r['tfd_ts']:8.4f}{sk:8.4f}{r['hfs_ts']:8.4f}{r['dscf']:8.4f} {ts:6.0f}{ds:6.0f}{rat:7.3f}")
print(f"\nPC1 shallower vs Koopmans: TFD {pc1t}/13  HFS {pc1h}/13")
for lab,S in (('early',early),('late',late)):
    ks=[gap[e] for e in S if e in gap]; print(f"PC3 {lab}: mean|K-m| {sum(abs(a) for a,b in ks)/len(ks):.3f} -> mean|TS-m| {sum(abs(b) for a,b in ks)/len(ks):.3f}")
print(f"PC5 DSCF within 30%: {n30}/13")