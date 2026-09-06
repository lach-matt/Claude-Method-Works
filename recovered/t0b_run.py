"""t0b_run.py -- T0(b) Scott/Englert-Schwinger K-shell replacement, six-ion probe.
rho_new = rho_K(Z) for r<r_s, rho_TFD outside.  Two variants, comparison decides:
 (u) unscaled: outer TFD untouched, N' = N + dN, tail -(Z-N')/r
 (c) conserved: outer TFD scaled by (N-Nin_K)/(N-Nin_TFD) so N is exact
V_T0b = V_base(tfd.potential) + [V_recon(rho_new) - V_recon(rho_TFD)]  (baseline is RUN-12 exactly)."""
import numpy as np, io, contextlib
with contextlib.redirect_stdout(io.StringIO()): import tfd
from t0b_rs import rho_tfd, rho_K, rs
from t0b_pot import V_from_rho, IONS, probe
MEAS={"Ca II":("4s<3d hold",None),"Sr II":("5s<4d",-0.07),"Ra II":("7s<6d",-0.055),"Ce IV":("4f<5d",-0.227),"Pr V":("4f<5d",-0.524),"Th IV":("5f<6d hold",None)}
print(f"{'ion':<7}{'meas d':>8} | {'TFD d':>8} | {'(u) e1':>9}{'e2':>9}{'d':>8}{'N_u':>8} | {'(c) e1':>9}{'e2':>9}{'d':>8}")
for lab,Z,N,pairs in IONS:
    q=Z-N; Vb,_=tfd.potential(Z,q); eb=probe(Vb,Z,pairs)
    rt,r0=rho_tfd(Z,N); rk=rho_K(Z); r_s,_,_,Nit,Nik=rs(Z,N)
    Vr,_=V_from_rho(Z,N,rt,r0)
    def mk(scale):
        return lambda r: np.where(np.asarray(r)<r_s, rk(r), scale*rt(r))
    out=[]
    for scale in (1.0,(N-Nik)/(N-Nit)):
        Vn,Nn=V_from_rho(Z,N,mk(scale),r0)
        qn=Z-Nn
        def V(rr,Vn=Vn,qn=qn):
            rr=np.asarray(rr,float); v=Vb(rr)+(Vn(rr)-Vr(rr))
            return np.where(rr<r0,np.minimum(v,-qn/rr),-qn/rr)
        e=probe(V,Z,pairs); out.append((e,Nn))
    (eu,Nu),(ec,Nc)=out
    md=MEAS[lab][1]; ms=f"{md:+.3f}" if md is not None else "hold"
    print(f"{lab:<7}{ms:>8} | {eb[1]-eb[0]:+8.4f} | {eu[0]:9.4f}{eu[1]:9.4f}{eu[1]-eu[0]:+8.4f}{Nu:8.3f} | {ec[0]:9.4f}{ec[1]:9.4f}{ec[1]-ec[0]:+8.4f}")