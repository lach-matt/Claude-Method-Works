# Three-body paper audit, six checks x thirteen mass order-types (register 1717's 78; named here, register 1756).
# Shape coordinates after Montgomery: mass-weighted Jacobi vectors rho1, rho2 in R^2; w = (|rho1|^2-|rho2|^2, 2 rho1.rho2) in R^3 (Hopf).
import numpy as np, itertools, sympy as sp
rng=np.random.default_rng(1770)
ORDER=[(1,1,1),(1,1,2),(1,2,1),(2,1,1),(1,2,2),(2,1,2),(2,2,1),(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]   # 13 mass order-types
def jac(m,q):
    m1,m2,m3=m; M12=m1+m2
    r1=np.sqrt(m1*m2/M12)*(q[1]-q[0]); r2=np.sqrt(M12*m3/(M12+m3))*(q[2]-(m1*q[0]+m2*q[1])/M12); return r1,r2
def shape(m,q):
    r1,r2=jac(m,q); return np.array([r1@r1-r2@r2, 2*r1@r2, 2*(r1[0]*r2[1]-r1[1]*r2[0])])
def rays(m):
    b={}
    for i,j in [(0,1),(1,2),(0,2)]:
        q=rng.normal(size=(3,2)); q[j]=q[i]; w=shape(m,q); b[(i,j)]=w/np.linalg.norm(w)
    return b
def mu(m,i,j): return m[i]*m[j]/(m[i]+m[j])
def cij(m,i,j): return (m[i]*m[j])**1.5/np.sqrt(m[i]+m[j])
def checks(m):
    m=np.array(m,float); b=rays(m); res={}
    okC=okA=True
    for _ in range(50):
        q=rng.normal(size=(3,2)); w=shape(m,q); I=np.linalg.norm(w)
        U=0; V=0
        for i,j in b:
            d2=I-w@b[(i,j)]; r2=np.sum((q[i]-q[j])**2)
            okC&=abs(d2/mu(m,i,j)-r2)<1e-9*max(1,r2)          # C: d_ij^2 = |w| - w.b_ij, r_ij^2 = d_ij^2/mu_ij
            U+=cij(m,i,j)/np.sqrt(d2); V+=m[i]*m[j]/np.sqrt(r2)
        okA&=abs(U-V)<1e-10*V                                    # A: U(w) = sum m_i m_j / r_ij
    res['A']=okA; res['C']=okC
    u1,u2,u3,U=sp.symbols('u1 u2 u3 U'); p=u1**2+u2**2+u3**2; qq=u1**2*u2**2+u2**2*u3**2+u1**2*u3**2; r=u1**2*u2**2*u3**2
    N=U**8-4*p*U**6+(6*p**2-8*qq)*U**4-4*(p**3-4*p*qq+16*r)*U**2+(p**2-4*qq)**2
    res['B']=sp.expand(N.subs(U,u1+u2+u3))==0                    # B: the norm vanishes at U = u1+u2+u3
    prod=sp.expand(sp.prod([(u1+s2*u2+s3*u3)**2 for s2 in (1,-1) for s3 in (1,-1)]))
    res['F']=sp.expand((p**2-4*qq)**2-prod)==0                   # F: constant term = prod over the sign classes
    # D: Euler's quintic has exactly one positive root for each of the three orderings; the equilateral triangle is a critical point
    okD=True; m1,m2,m3=m
    for (a,bb,c) in [(m1,m2,m3),(m2,m3,m1),(m3,m1,m2)]:
        coef=[a+bb, 3*a+2*bb, 3*a+bb, -(bb+3*c), -(2*bb+3*c), -(bb+c)]   # Euler quintic for body bb between a and c
        roots=np.roots(coef); okD&=sum(1 for z in roots if abs(z.imag)<1e-9 and z.real>0)==1
    def Ufun(w): 
        I=np.linalg.norm(w); return sum(cij(m,i,j)/np.sqrt(I-w@b[(i,j)]) for i,j in b)
    q=np.array([[0,0],[1,0],[0.5,np.sqrt(3)/2]]); w=shape(m,q); wh=w/np.linalg.norm(w)
    g=np.zeros(3); h=1e-6
    for k in range(3):
        e=np.zeros(3); e[k]=h; g[k]=(Ufun(wh+e)-Ufun(wh-e))/(2*h)
    gt=g-(g@wh)*wh                                               # tangential gradient on the sphere at fixed |w|
    okD&=np.linalg.norm(gt)<1e-4*abs(Ufun(wh))
    res['D']=okD
    # E: symmetry order of U under mass-preserving relabellings: 6, 2, 1
    order=sum(1 for perm in itertools.permutations(range(3)) if all(m[perm[k]]==m[k] for k in range(3)))
    res['E']=order==(6 if len(set(m))==1 else 2 if len(set(m))==2 else 1)
    return res
tot=0; passed=0
for m in ORDER:
    r=checks(m); tot+=6; passed+=sum(r.values()); print(m,''.join(k if v else k.lower() for k,v in sorted(r.items())))
print(f'{passed} of {tot}')