# quick numeric exploration of the k=1 conditional branch (ell_s = 1)
import mpmath as mp
mp.mp.dps = 40
def ours(u, L):
    A = 1 + u/L**2; s = mp.sqrt(1 + 8*A + 16*A*u)
    return u*((4*A-1)+s)/(8*A), ((4*A-1)+s)/(4*mp.sqrt(A*u))
def p2(u, L):
    A = 1 + u/L**2; s = mp.sqrt(1 + 8*A + 16*A*u)
    return u*((4*A-1)-s)/(8*A), -((4*A-1)-s)/(4*mp.sqrt(A*u))
# check balance residuals
def fs(u, mu): return 1 + u - mu/u
for L1 in [1.5, 2, 3, 10]:
    u1 = mp.findroot(lambda u: ours(u, L1)[1] - 2, 1.0)
    mu, lam1 = ours(u1, L1)
    # residual of balance: (2mu/u-1)^2 (1+u/L^2) - fs
    res = (2*mu/u1 - 1)**2*(1+u1/L1**2) - fs(u1, mu)
    rh2 = (mp.sqrt(1+4*mu)-1)/2
    print("L1", L1, "u1", mp.nstr(u1,12), "mu", mp.nstr(mu,12), "lam1", mp.nstr(lam1,6), "res", mp.nstr(res,3), "rh", mp.nstr(mp.sqrt(rh2),10), "R1", mp.nstr(mp.sqrt(u1),10))
    for ratio in [mp.mpf(1)/4, mp.mpf(1)/8]:
        target = -ratio*lam1
        # unknowns u2, L2: p2(u2,L2) = (mu, target)
        try:
            sol = mp.findroot(lambda u, L: [p2(u, L)[0]-mu, p2(u, L)[1]-target], (u1*3, 0.9))
            u2, L2 = sol
            print("   ratio", ratio, "u2", mp.nstr(u2,12), "L2", mp.nstr(L2,12), "check", mp.nstr(p2(u2,L2)[0]-mu,3), mp.nstr(p2(u2,L2)[1]-target,3), "R2", mp.nstr(mp.sqrt(u2),10))
        except Exception as e:
            print("   ratio", ratio, "fail", e)
