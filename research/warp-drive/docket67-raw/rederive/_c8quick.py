import mpmath as mp, importlib.util, sys
mp.mp.dps=15
spec=importlib.util.spec_from_file_location("x","/dev/null")
# minimal copy of J
def T(p,al,be):
    if al==0: return mp.gamma(-p-1)*be**(p+1)
    return 2*(be/al)**((p+1)/2)*mp.besselk(p+1,2*mp.sqrt(al*be))
def J(b2,A):
    a=1-b2
    f=lambda u:((9*u*u-2*u-11)*T(mp.mpf(-7)/2,u*A,(u+a)/(1+u))+5*u*b2*T(mp.mpf(-9)/2,u*A,(u+a)/(1+u)))/(1+u)**6
    pts=sorted(set([0]+[s*mp.mpf(10)**k for s in (a,1/A,mp.mpf(1)) for k in (-3,-1,0,1,3)]))+[mp.inf]
    return mp.quad(f,pts)
M=mp.pi*mp.mpf('0.51099895e-3')*mp.mpf('38.6e-6')/mp.mpf('1.973269804e-16')
for lg in (12,13,13.5,14,15):
    g=mp.mpf(10)**lg; a=1/g**2; b2=1-a
    I=sum(J(b2,(M*w)**2)/w**3 for w in range(1,5))/(6*mp.sqrt(mp.pi))
    print(lg, mp.nstr(I,6), mp.nstr(I/(-(mp.zeta(3)/2)*g**3),6))
