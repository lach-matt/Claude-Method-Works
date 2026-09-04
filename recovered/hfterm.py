"""hfterm.py -- s27 item 3: term-resolved (Hund ground term) exact-exchange DSCF, first order in orbital relaxation, on top of s26 hfdscf.
usage: python3 hfterm.py Z ...   (Z=0 runs the PT0 coefficient gate only). Appends hfterm.jsonl (key Z), resumable. No constant beyond c.
E_det = sum_{i<j open spin-orbitals} [J_ij - delta_spin K_ij]; J,K from Gaunt c^k x radial F^k/G^k of the avg-of-config HF orbitals of that state.
E_avg = within-shell N(N-1)/2*[F^0 - w sum_k c3j0^2 F^k], w=(2l+1)/(4l+1); cross-shell N_a N_b [F^0(ab) - 1/2 sum_k c3j0^2(la,k,lb) G^k]. Closed shells cancel."""
import sys,os,json,time,itertools,math,numpy as np
os.environ.setdefault("SIC_NOCLAMP","1")
from sympy.physics.wigner import gaunt, wigner_3j
from t7c_hfsr import HFSR
from t7c_kernel import C0
from t5_scf import ground_occ,minus
import t7c_cuaudit as T
OUT="hfterm.jsonl"
SH={21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f')}
_ck={}
def ck(l,m,lp,mp,k):
    """Gaunt c^k(lm,l'm') = sqrt(4pi/(2k+1)) int Y*_lm Y_{k,m-m'} Y_{l'm'}."""
    key=(l,m,lp,mp,k)
    if key not in _ck: _ck[key]=float((-1)**m*math.sqrt(4*math.pi/(2*k+1))*gaunt(l,k,lp,-m,m-mp,mp))
    return _ck[key]
def c3j0sq(a,k,b): return float(wigner_3j(a,k,b,0,0,0))**2
def hund_det(shells):
    """shells: list of (l,N). Returns spin-orbitals (shell index, ml, ms) of the highest-weight determinant of the Hund term: max S then max L.
    Each open shell: fill ml = l..-l spin-up first (max S), then spin-down from ml=l downward (max L given max S). All shells' up-spins parallel."""
    so=[]
    for i,(l,N) in enumerate(shells):
        ml=list(range(l,-l-1,-1)); up=min(N,2*l+1); dn=N-up
        so+=[(i,m,+1) for m in ml[:up]]+[(i,m,-1) for m in ml[:dn]]
    return so
def pair(a,b,ma,mb,la,lb,F,G,same_spin,ia,ib):
    """J - delta K for spin-orbitals in shells ia,ib (radial integral dicts keyed by k)."""
    J=sum(ck(la,ma,la,ma,k)*ck(lb,mb,lb,mb,k)*F[k] for k in F)
    K=sum(ck(la,ma,lb,mb,k)**2*G[k] for k in G) if same_spin else 0.0
    return J-K
def E_open(shells,so,Fk,Gk):
    """Energy of the given determinant restricted to pairs among the open-shell spin-orbitals. Fk[(i,j)] dict k->F^k(i,j); Gk[(i,j)] k->G^k."""
    E=0.0
    for (ia,ma,sa),(ib,mb,sb) in itertools.combinations(so,2):
        la,lb=shells[ia][0],shells[ib][0]
        E+=pair(None,None,ma,mb,la,lb,Fk[(ia,ib)],Gk[(ia,ib)],sa==sb,ia,ib)
    return E
def E_avg(shells,Fk,Gk):
    E=0.0
    for i,(l,N) in enumerate(shells):
        w=(2*l+1)/(4*l+1); E+=N*(N-1)/2*(Fk[(i,i)][0]-w*sum(c3j0sq(l,k,l)*Fk[(i,i)][k] for k in Fk[(i,i)] if k>0))
    for i,j in itertools.combinations(range(len(shells)),2):
        li,Ni=shells[i]; lj,Nj=shells[j]
        E+=Ni*Nj*(Fk[(i,j)][0]-0.5*sum(c3j0sq(li,k,lj)*Gk[(i,j)][k] for k in Gk[(i,j)]))
    return E
def radial(h,keys):
    """F^k, G^k between HF shells (n,l) in keys, from h.P and h.Yk. Returns dicts keyed by index pairs (i,j) with i<=j (and (i,i))."""
    r,dr=h.r,h.dr; Fk={};Gk={}
    for i,a in enumerate(keys):
        for j,b in enumerate(keys):
            if j<i: continue
            la,lb=a[1],b[1]
            Fk[(i,j)]={k:float(np.sum(h.P[a]**2*h.Yk(h.P[b],h.P[b],k)/r*dr)) for k in range(0,min(2*la,2*lb)+1,2)}
            Gk[(i,j)]={k:float(np.sum(h.P[a]*h.P[b]*h.Yk(h.P[a],h.P[b],k)/r*dr)) for k in range(abs(la-lb),la+lb+1,2)}
    return Fk,Gk
def gate_PT0():
    """determinant-averaged pair energy over ALL determinants of l^N == Slater average, using unit radial integrals F^k=1 (coefficients only)."""
    out=[]
    for l,N in ((2,2),(3,2),(2,3)):
        so_all=[(0,m,s) for m in range(-l,l+1) for s in (+1,-1)]
        Fk={(0,0):{k:1.0 for k in range(0,2*l+1,2)}}; Gk={(0,0):{k:1.0 for k in range(0,2*l+1,2)}}
        dets=list(itertools.combinations(so_all,N)); Es=[E_open([(l,N)],list(d),Fk,Gk) for d in dets]
        avg=sum(Es)/len(dets); sl=E_avg([(l,N)],Fk,Gk); out.append((l,N,avg,sl,abs(avg-sl)))
    # cross-shell: d^1 s^1 all determinants vs N_a N_b [F0 - 1/2 sum c3j0^2 G^k]
    Fk={(0,0):{0:1.0,2:1.0,4:1.0},(1,1):{0:1.0},(0,1):{0:1.0}}; Gk={(0,0):{0:1.0,2:1.0,4:1.0},(1,1):{0:1.0},(0,1):{2:1.0}}
    dets=[[(0,m,s),(1,0,t)] for m in range(-2,3) for s in (1,-1) for t in (1,-1)]
    avg=sum(E_open([(2,1),(0,1)],d,Fk,Gk) for d in dets)/len(dets); sl=E_avg([(2,1),(0,1)],Fk,Gk); out.append(("d1s1",avg,sl,abs(avg-sl)))
    return out
if __name__=="__main__":
    Zs=list(map(int,sys.argv[1:]))
    if 0 in Zs:
        for row in gate_PT0(): print("PT0",row)
        Zs=[z for z in Zs if z]
    done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
    for Z in Zs:
        if Z in done: print("SKIP",Z); continue
        el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); t0=time.time()
        occ0=ground_occ(Z); occ1=[(a,b,q) for a,b,q in minus(occ0,n,l,1.0) if q>0]
        res={}
        for tag,occ in (("neu",occ0),("ion",occ1)):
            h=HFSR(Z,occ,c=C0); e,E,it,_=h.run('hf',qtail=1)
            openk=[(a,b) for a,b,q in occ if 0<q<2*(2*b+1)]; shells=[(b,int(round(q))) for a,b,q in occ if 0<q<2*(2*b+1)]
            Fk,Gk=radial(h,openk); so=hund_det(shells)
            dE=E_open(shells,so,Fk,Gk)-E_avg(shells,Fk,Gk)
            res[tag]=dict(E=float(E),it=it,open=[(a,b,q) for a,b,q in occ if 0<q<2*(2*b+1)],dE_term=dE,
                          Fk_ent={k:round(v,5) for k,v in Fk[(openk.index((n,l)),openk.index((n,l)))].items()} if (n,l) in openk else {})
            if tag=="neu": h0=h
        D_avg=res["ion"]["E"]-res["neu"]["E"]; D_term=D_avg+res["ion"]["dE_term"]-res["neu"]["dE_term"]
        # Delta_c exactly as s26 hfdscf (neutral HF orbitals, entrant weight 1/2)
        r,dr=h0.r,h0.dr; w=4*np.pi*r*r; P=h0.P; Q={(a,b):q for a,b,q in occ0}; ne=P[(n,l)]**2; f=0.5
        nu=np.zeros_like(r); nd=np.zeros_like(r)
        for (a,b),q in Q.items():
            cap=2*(2*b+1); dens=P[(a,b)]**2; qs=q-(1-f) if (a,b)==(n,l) else q
            up=min(qs,cap/2); nu+=up*dens; nd+=max(qs-cap/2,0)*dens
        vu,vd=T.v_gbz(nu/w,nd/w); vsic=T.v_gbz(f*ne/w,0*ne)[0]; Dc=float(np.sum(ne*(vu-vsic)*dr))
        o=dict(Z=Z,el=el,sh=sh,D_avg=round(D_avg,5),dE_term_neu=round(res["neu"]["dE_term"],5),dE_term_ion=round(res["ion"]["dE_term"],5),
               D_term=round(D_term,5),Delta_c=round(Dc,5),obj_avg=round(-D_avg+Dc,5),obj_term=round(-D_term+Dc,5),
               open_neu=res["neu"]["open"],open_ion=res["ion"]["open"],Fk_ent_neu=res["neu"]["Fk_ent"],it=[res["neu"]["it"],res["ion"]["it"]],
               sec=int(time.time()-t0))
        open(OUT,"a").write(json.dumps(o)+"\n"); print({k:v for k,v in o.items() if k not in ("open_neu","open_ion","Fk_ent_neu")},flush=True)
