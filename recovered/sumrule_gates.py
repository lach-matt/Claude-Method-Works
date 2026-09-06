"""sumrule_gates.py -- s32 gates G-S4 (f-sum) and G-S5 (compressibility / Thomas-Fermi) on ring_zeta.g, the chain's Lindhard function
(Maxwell's eps of the medium, SPEC-SOSEX-SESSION-32 §A1-§A2). Closed-form limits derived BEFORE evaluation; both must hold or the spec's screening
line is wrong. Usage: python3 sumrule_gates.py [rs] [lam]   (rs default 2, lam default 1: Pi is lam-linear, so both limits scale by lam)"""
import numpy as np, sys, ring_zeta as R
rs=float(sys.argv[1]) if len(sys.argv)>1 else 2.0; lam=float(sys.argv[2]) if len(sys.argv)>2 else 1.0; al=R.al
def Pi(K,X,z): xp,xm=R.xs(z); return lam*(al*rs/(np.pi*K*K))*sum(s*R.g(K/s,K*X/(s*s)) for s in (xp,xm) if s>0)
ok=True
p4=lam*4*al*rs/(3*np.pi); print(f"G-S4 f-sum  rs {rs} lam {lam}: K^2 X^2 Pi -> {p4:.6f} (zeta-independent)")
for z in (0.0,0.5,1.0):
    for K in (0.5,1.0,2.0):
        v=K*K*1e6*Pi(K,1e3,z); r=v/p4-1; ok&=abs(r)<1e-3; print(f"  zeta {z} K {K}: {v:.6f} rel {r:+.1e}")
print(f"G-S5 compressibility rs {rs} lam {lam}: K^2 Pi(K,0) -> 2 lam al rs (x_up+x_dn)/pi")
for z in (0.0,0.5,1.0):
    xp,xm=R.xs(z); p5=lam*2*al*rs*(xp+xm)/np.pi; v=1e-6*Pi(1e-3,1e-12,z); r=v/p5-1; ok&=abs(r)<1e-4; print(f"  zeta {z}: {v:.6f} pred {p5:.6f} rel {r:+.1e}")
print("G-S4/G-S5:", "PASS" if ok else "FAIL")