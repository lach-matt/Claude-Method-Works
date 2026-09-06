import json
HA=219474.63
K={r[0]:(r[2],r[3]) for r in json.load(open('/home/claude/work/LOWDIN-HANDOFF-11/LOWDIN-HANDOFF-11/pack9/T0b_pairs.json')) if r[1] in('3d','4f')}
rows=[]
for l in open('served.tsv'):
    if l[0]=='#' or l.startswith('Z\t'): continue
    f=l.rstrip('\n').split('\t')
    Z=int(f[0]);
    try: E=-(float(f[3])+float(f[7]))/HA
    except: rows.append((Z,f[1],None)); continue
    rows.append((Z,f[1],E))
print(f"{'el':<4}{'meas':>8}{'TFD':>8}{'SCF':>8}{'geo':>8}{'arith':>8} {'PB1':>4} {'geo%':>6} {'ari%':>6}")
n1=n2=N=0
for Z,el,E in sorted(rows):
    if E is None: print(f"{el:<4}    NULL"); continue
    t,s=K[Z]; g=-(t*s)**.5; a=(t+s)/2
    b= min(t,s)<=E<=max(t,s); ge=abs(g-E)/abs(E)*100; ae=abs(a-E)/abs(E)*100
    N+=1; n1+=b; n2+= ge<=30
    print(f"{el:<4}{E:8.4f}{t:8.4f}{s:8.4f}{g:8.4f}{a:8.4f} {'Y' if b else 'N':>4} {ge:6.1f} {ae:6.1f}")
print(f"\nPB-11.1 between kernels: {n1}/{N}   PB-11.2 geo within 30%: {n2}/{N}")