# Adversarial check: does F_S (5.3) have a negative real zero when b2 < -b1^2/(4|b0|)?
# m=1, kappa=1, xi=0, alpha~S1=1/(64 pi^2)  (the audit's N2 test point)
import mpmath as mp
mp.mp.dps=60
pi=mp.pi
def J(g):  # J(g)=int_4^inf rho(M)/(M-g) dM, rho=(1/16pi^2)(1/M)sqrt(1-4/M); g<0
    s=-g
    f=lambda u: 2*mp.sinh(u)**2/(mp.cosh(u)**2*(4*mp.cosh(u)**2+s))
    uc=mp.acosh(mp.sqrt(max(s,4)/4)) if s>4 else mp.mpf(1)
    return mp.quad(f,[0,uc/2,uc,uc+2,uc+10,uc+60,mp.inf])/(16*pi**2)
print("J(0) check vs 1/(96pi^2):", J(mp.mpf('-1e-30')), 1/(96*pi**2))
c=mp.mpf(1)/6; a=-2; alpha=1/(64*pi**2)
b0=-alpha*4/c; b1=-2/c
print("b0,b1",b0,b1,"disc threshold b2 =",-b1**2/(4*abs(b0)))
def F(g,b2): return g*(a-g)**2*J(g)-b0-b1*g-b2*g**2
for b2 in (-100,-1000):
    print("b2=",b2)
    for X in (1,5,10,50,100,1000,10000,15000,15700,15800,16000,160000,158000,157000):
        g=-mp.e**X
        v=F(g,b2)
        print("  X=%g  sign F(-e^X)=%s  F/g^2=%s"%(X, mp.sign(v), mp.nstr(v/g**2,8)))
