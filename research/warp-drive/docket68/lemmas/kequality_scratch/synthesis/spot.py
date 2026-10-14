# Synthesis spot-check (independent of all six scripts): the ell_s-free k=1 two-exterior bridge.
# Units ell_1 = 1. Static plane at r=R: lam*R = sum eps_j sqrt(f_j), balance sum eps_j (k-2mu_j/R^2)/sqrt(f_j) = 0,
# lam = kappa^2 sigma/3; RS(ell_1) => lam1 = 2. Bridge side eps=+1 (toward horizon); ours' outer side eps=+1 (decaying),
# position 2's outer side eps=-1 (growing). f_s = 1 + r^2/ls^2 - mu/r^2; f_o = 1 + r^2/lo^2.
from mpmath import mp, mpf, sqrt, findroot, matrix
mp.dps = 50
def system(ratio, l2):
    lam1 = mpf(2); lam2 = ratio*lam1
    def F(mu, R1, R2, ls):
        fs = lambda r: 1 + r**2/ls**2 - mu/r**2
        f1 = lambda r: 1 + r**2
        f2 = lambda r: 1 + r**2/l2**2
        return [lam1*R1 - (sqrt(fs(R1)) + sqrt(f1(R1))),
                (1-2*mu/R1**2)/sqrt(fs(R1)) + 1/sqrt(f1(R1)),
                lam2*R2 - (sqrt(fs(R2)) - sqrt(f2(R2))),
                (1-2*mu/R2**2)/sqrt(fs(R2)) - 1/sqrt(f2(R2))]
    return F
def horizon(mu, ls):
    # r^4/ls^2 + r^2 - mu = 0
    x = (-1 + sqrt(1 + 4*mu/ls**2))*ls**2/2
    return sqrt(x)
cases = {
 "(a) -1/8, ell_2=4ell_1/3 (per-sheet M4)": (mpf(-1)/8, mpf(4)/3, [0.922223, 1.113372, 2.503799, 2.114734]),
 "(b) -1/4, ell_2=ell_1": (mpf(-1)/4, mpf(1), [0.161459732/0.4314318826**2, 1.0, 2.0, 1/0.4314318826]),
 "(c) -1/8, ell_2=ell_1": (mpf(-1)/8, mpf(1), [1.015147613/0.744474335**2, 1.0, 2.0, 1/0.744474335]),
}
for name,(ratio,l2,x0) in cases.items():
    F = system(ratio,l2)
    best=None
    for R1g in [0.8,1.0,1.113,1.3,1.6]:
        for R2g in [1.5,2.0,2.5,3.0,4.0]:
            try:
                s = findroot(F, [mpf(x0[0]), mpf(R1g), mpf(R2g), mpf(x0[3])])
                mu,R1,R2,ls = s
                res = max(abs(v) for v in F(mu,R1,R2,ls))
                if res < mpf('1e-40') and mu>0 and R1>0 and R2>0 and ls>0:
                    rh = horizon(mu,ls)
                    if R1>rh and R2>rh and (1+R1**2/ls**2-mu/R1**2)>0:
                        best=(mu,R1,R2,ls,rh,res); break
            except Exception as e:
                pass
        if best: break
    if best:
        mu,R1,R2,ls,rh,res=best
        print(name)
        print("  ell_s/ell_1 =", mp.nstr(ls,15), " ell_1/ell_s =", mp.nstr(1/ls,15))
        print("  mu =", mp.nstr(mu,12), "ell_1^2 =", mp.nstr(mu/ls**2,12), "ell_s^2")
        print("  r_h =", mp.nstr(rh,12), "ell_1   R1 =", mp.nstr(R1,12), "ell_1   R2 =", mp.nstr(R2,12), "ell_1 =", mp.nstr(R2/ls,10),"ell_s")
        print("  max residual =", mp.nstr(res,3))
    else:
        print(name, ": no admissible root found from these starts")
# flat (k=0) control: B per bridge side = -2mu/(R^2 sqrt f_s) never zero for mu>0; mu=0 -> B=0 identically
import sympy as sp
R,mu,l=sp.symbols('R mu ell',positive=True)
fs=R**2/l**2-mu/R**2
B=(0-2*mu/R**2)/sp.sqrt(fs)
print("k=0 B per bridge side:", sp.simplify(B), "; at mu=0:", sp.simplify(B.subs(mu,0)))
# mirrored flat at RS: kappa^2(rho_m+p_m) = 2B/R
print("mirrored flat kappa^2(rho+p) =", sp.simplify(2*B/R))
