"""hf_chan.py -- s36: HF (hfc2, SR, no corr) DSCF for the entrant placed in an EMPTY channel (owed from FINDING-LWALK: La 4f). usage: python3 hf_chan.py Z nl ...
D_HF_rel(c) = E_HF(ion+c) - E_HF(ion); ion = ground minus derived entrant. appends hf_chan.jsonl (key Z,tag). No constant."""
import sys,os,json,time
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
import hfc2 as H; from t7c_kernel import C0; from t5_scf import ground_occ,minus; import ground as G
H.CORR=False
OUT='hf_chan.jsonl'; done={(d['Z'],d['tag']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
Z=int(sys.argv[1]); tags=sys.argv[2:]
a={(n,l):k for n,l,k in G.expand(Z)}; b={(n,l):k for n,l,k in G.expand(Z-1)}; g=[nl for nl in a if a[nl]-b.get(nl,0)>1e-9][0]
occ1=minus(ground_occ(Z),g[0],g[1],1.0); E1=None
for tag in tags:
    if (Z,tag) in done: print("SKIP",Z,tag); continue
    c=(int(tag[0]),"spdf".index(tag[1])); t0=time.time()
    if E1 is None: E1,_,it1,_=H.HFC(Z,occ1,c=C0).run2()
    occc=[list(t) for t in occ1]; f=False
    for t in occc:
        if (t[0],t[1])==c: t[2]+=1; f=True
    if not f: occc.append([c[0],c[1],1])
    Ec,_,itc,epsc=H.HFC(Z,[tuple(t) for t in occc],c=C0).run2()
    o=dict(Z=Z,tag=tag,ent=f"{g[0]}{'spdf'[g[1]]}",D_HF_rel=round(Ec-E1,5),eps_c=round(float(epsc[c]),5),E_ion=round(E1,5),it=[it1,itc],sec=int(time.time()-t0))
    open(OUT,'a').write(json.dumps(o)+'\n'); print(o,flush=True)