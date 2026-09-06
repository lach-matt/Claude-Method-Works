"""sox_table.py -- s32: coupling-averaged statically-screened second-order exchange eps_2x^scr(r_s,zeta) [Ha] on the ring grid.
eps_2x^scr = sum_sigma (s^3/2) int dq~ g_2b(q~) S(Pi(s q~, 0; r_s, zeta)),   S(Pi) = int_0^1 2 lam dlam/(1+lam Pi) = 2[Pi - ln(1+Pi)]/Pi^2,
Pi = -v chi_0 = (al rs/(pi K^2)) sum_sigma' s' g(K/s', 0) (ring_zeta.g, Maxwell's eps of the medium, SPEC-SOSEX §A1), K = s q~ (spin sigma's own k_F).
g_2b from sox_qres.jsonl (r_s-, zeta-independent, k_F units, Ry). Screening off (S=1) -> E0B for every zeta (G-S1). r_s -> 0 -> E0B (G-S2).
Writes sox_table.json {rs, z, eps2x (nz x nrs, Ha)}. usage: python3 sox_table.py [gates|table]"""
import numpy as np, json, sys, ring_zeta as R
al=R.al; E0B=0.0241792
_rows=sorted([json.loads(l) for l in open('sox_qres.jsonl')],key=lambda r:r['q'])
Q=np.array([r['q'] for r in _rows]); G=np.array([r['g2b_Ry'] for r in _rows]); LQ=np.log(Q)
def _int(f):  # int dq g f(q) with the two tails (g ~ q below, ~ q^-4 above)
    return np.trapezoid(G*Q*f,LQ)+G[0]*Q[0]/2*f[0]+G[-1]*Q[-1]/3*f[-1]
def Pi(K,rs,z):
    xp,xm=R.xs(z)
    return (al*rs/(np.pi*K*K))*sum(s*R.g(K/s,1e-12*np.ones_like(K)) for s in (xp,xm) if s>0)
def S(P):
    with np.errstate(invalid='ignore',divide='ignore'):
        v=2*(P-np.log1p(P))/(P*P)
    return np.where(P<1e-6,1-2*P/3,v)
def eps2x(rs,z,screen=True):
    xp,xm=R.xs(z); tot=0.0
    for s in (xp,xm):
        if s<=0: continue
        w=S(Pi(s*Q,rs,z)) if screen else np.ones_like(Q)
        tot+=(s**3/2)*_int(w)
    return tot/2.0   # Ry -> Ha
if __name__=="__main__":
    mode=sys.argv[1] if len(sys.argv)>1 else "gates"
    if mode=="gates":
        for z in (0.0,1.0):
            e=eps2x(2.0,z,screen=False); print(f"G-S1 zeta {z}: bare {e:.7f} Ha  E0B {E0B}  diff {e-E0B:+.1e}  {'PASS' if abs(e-E0B)<1e-4 else 'FAIL'}")
        for z in (0.0,1.0):
            for rs in (1e-3,3e-4,1e-4):
                e=eps2x(rs,z); print(f"G-S2 zeta {z} rs {rs}: {e:.7f} Ha  E0B-e {E0B-e:+.1e}")
        for z in (0.0,1.0): print(f"PS-1 point rs 2 zeta {z}: eps2x^scr {eps2x(2.0,z):.6f} Ha ratio {eps2x(2.0,z)/E0B:.4f}")
    else:
        t=json.load(open('ring_table.json')); RS=np.array(t['rs']); ZS=np.array(t['z'])
        E=[[eps2x(rs,z) for rs in RS] for z in ZS]
        json.dump({"rs":list(map(float,RS)),"z":list(map(float,ZS)),"eps2x":E,"E0B":E0B},open('sox_table.json','w'))
        E=np.array(E); print("sox_table.json written", E.shape)
        for iz in (0,5,10): print(f"zeta {ZS[iz]}: ratio at rs 0.1/1/2/5/10:",[round(float(E[iz,i]/E0B),4) for i in (16,24,27,30,32)])