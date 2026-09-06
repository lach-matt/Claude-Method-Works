import numpy as np, json, os, re
S=open('/mnt/user-data/outputs/spec/appendix-c-provenance.md').read()
i=S.find('## C.2 Channels')
rows=[]
for ln in S[i:].split('\n'):
    p=[x.strip() for x in ln.strip().strip('|').split('|')]
    if len(p)>=11 and p[0] not in ('species','---') and '---' not in p[0]:
        try:
            rows.append(dict(sp=p[0],ch=p[1],mem=int(p[3]),spread=float(p[8]),
                             Z=int(p[9]),lim=float(p[10].replace(',',''))))
        except Exception: pass
print("channels parsed from Appendix C:",len(rows))
FILE={'Al I':'al1','Al II':'al2','Li I':'li1','Na I':'na1','K I':'k1','Ga I':'ga1',
      'He I':'he1','He II':'he2','Li II':'li2','Be II':'be2','Mg II':'mg2',
      'Si II':'si2','C II':'c2','Ca II':'ca2','Cd II':'cd2','Zn II':'zn2','Hg II':'hg2'}
def fd(Tv,nodes,order):
    ys=[Tv[x] for x in nodes]
    for _ in range(order): ys=[ys[i+1]-ys[i] for i in range(len(ys)-1)]
    return ys[0] if ys else None
def status(Tv,n,k,sig):
    span=[n+j for j in range(-(k+1),k+2)]
    if any(x not in Tv for x in span): return 'missing'
    want=1 if (k+1)%2==0 else -1
    floor=5*(2.0**(k+1))*sig
    for s in range(0,len(span)-(k+1)):
        d=fd(Tv,span[s:s+k+2],k+1)
        if d is None: return 'missing'
        if abs(d)<floor: return 'unresolved'
        if np.sign(d)!=want: return 'refused'
    return 'ok'
cache={}
def load(sp):
    if sp in cache: return cache[sp]
    f=FILE.get(sp)
    p='/home/claude/data/%s.json'%f if f else None
    cache[sp]=json.load(open(p)) if p and os.path.exists(p) else {}
    return cache[sp]
out=[]
for r in rows:
    D=load(r['sp'])
    key=None
    for k in D:
        if k.replace(' ','')==r['ch'].replace(' ','') or k.split()[0]==r['ch'].split()[0] and k.split()[-1]==r['ch'].split()[-1]:
            key=k; break
    if key is None: continue
    M={int(a):b for a,b in D[key].items()}
    Tv={n:r['lim']-M[n] for n in M if r['lim']-M[n]>0}
    if len(Tv)<6: continue
    dg=0
    for v in M.values():
        s=("%.6f"%v).rstrip('0')
        if '.' in s: dg=max(dg,len(s.split('.')[1]))
    sig=10.0**(-dg) if dg else 1.0
    ok=rf=0
    for k in (1,2,3):
        for n in sorted(Tv):
            st=status(Tv,n,k,sig)
            if st=='ok': ok+=1
            elif st=='refused': rf+=1
    if ok+rf>=8:
        out.append((r['sp'],r['ch'],r['mem'],r['spread'],ok,rf,100*rf/(ok+rf)))
print("channels matched with >=8 resolved cells:",len(out))
out.sort(key=lambda x:-x[6])
print("\n  %-8s%-16s%6s%10s%8s%8s%11s"%("species","channel","mem","δ spread","adm","ref","refusal %"))
print("  "+"-"*68)
for sp,ch,mem,sd,ok,rf,rate in out:
    print("  %-8s%-16s%6d%10.4f%8d%8d%11.1f"%(sp,ch[:16],mem,sd,ok,rf,rate))
SP=np.array([o[3] for o in out]); RT=np.array([o[6] for o in out])
MM=np.array([o[2] for o in out],float)
print("\n  %-30s%12s%12s"%("","Pearson","Spearman"))
for lab,v in [("δ spread vs refusal rate",SP),("members vs refusal rate",MM)]:
    print("  %-30s%12.3f%12.3f"%(lab,np.corrcoef(v,RT)[0,1],
        np.corrcoef(np.argsort(np.argsort(v)),np.argsort(np.argsort(RT)))[0,1]))
hi=[o for o in out if o[3]>0.20]; lo=[o for o in out if o[3]<=0.05]
print("\n     δ spread > 0.20 : n=%d  median refusal %.1f%%"%(len(hi),np.median([o[6] for o in hi]) if hi else float('nan')))
print("     δ spread ≤ 0.05 : n=%d  median refusal %.1f%%"%(len(lo),np.median([o[6] for o in lo]) if lo else float('nan')))
if hi and lo:
    wins=sum(1 for a in hi for c in lo if a[6]>c[6]); tot=len(hi)*len(lo)
    print("     pairwise: high-spread > low-spread in %d of %d  (%.0f%%)"%(wins,tot,100*wins/tot))