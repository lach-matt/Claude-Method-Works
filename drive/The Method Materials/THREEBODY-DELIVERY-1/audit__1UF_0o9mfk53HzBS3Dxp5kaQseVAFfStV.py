# RECONSTRUCTED FROM TRANSCRIPT (chat b778e075, 2026-08-23). Original filename: audit.py
# (the Register's "tb_audit.py" = this file). Corrected state (check A passes).
# Reconstruction seam: the single comment line marked [SEAM] was not recoverable verbatim.
import numpy as np, itertools, sympy as sp
rng=np.random.default_rng(7)
TOL=1e-10
# --- all 13 weak orderings of (x,y,z) realised as mass triples
cases={
 "x=y, y<z":(1,1,2),  "x=y, y=z":(1,1,1),  "x=y, y>z":(2,2,1),
 "x<y, y=z":(1,2,2),  "x>y, y=z":(2,1,1),  "x<y, y<z":(1,2,3),
 "x>y, y>z":(3,2,1),  "x<y, y>z":(1,3,2),  "x>y, y<z":(2,1,3),
 "x=z, x<y":(1,2,1),  "x=z, x>y":(2,1,2),  "x<z, z<y":(1,3,2.5), "x>z, z>y":(3,1,2),
}
def jacobi(q,m):                       # Montgomery eq (26): normalised Jacobi vectors
    m1,m2,m3=m; M=sum(m); mu1=np.sqrt(m1*m2/(m1+m2)); mu2=np.sqrt((m1+m2)*m3/M)
    Z1=mu1*(q[1]-q[0]); Z2=mu2*(q[2]-(m1*q[0]+m2*q[1])/(m1+m2)); return Z1,Z2
def shape(Z1,Z2):                      # Montgomery eq (33)
    return np.array([0.5*(abs(Z1)**2-abs(Z2)**2),(Z1*np.conj(Z2)).real,(Z1*np.conj(Z2)).imag])
def binary_rays(m):                    # unit vectors b_ij: shape of the ij collision (Montgomery §11)
    b={}
    for (i,j,k) in [(0,1,2),(1,2,0),(2,0,1)]:
        q=np.zeros(3,complex); q[i]=q[j]=0; q[k]=1.0
        w=shape(*jacobi(q,m)); b[(i,j)]=w/np.linalg.norm(w)
    return b
def V0_shape(w,m):                     # Σ c_ij/d_ij, c_ij=(m_i m_j)^{3/2}/sqrt(m_i+m_j), d_ij^2=|w|-w·b_ij
    b=binary_rays(m); tot=0
    for (i,j),bij in b.items():
        c=(m[i]*m[j])**1.5/np.sqrt(m[i]+m[j]); d=np.sqrt(np.linalg.norm(w)-w@bij); tot+=c/d
    return tot
def U_newton(q,m):
    return sum(m[i]*m[j]/abs(q[i]-q[j]) for i,j in [(0,1),(1,2),(0,2)])
# --- symbolic: correct degree-8 norm (mass-independent)
V,u1,u2,u3=sp.symbols('V u1 u2 u3')
P8=sp.expand(sp.prod([V-e1*u1-e2*u2-e3*u3 for e1,e2,e3 in itertools.product([1,-1],repeat=3)]))
f8=sp.lambdify((V,u1,u2,u3),P8)
# --- Euler collinear quintic (Euler 1767): count positive real roots for each ordering
def euler_roots(m):
    m1,m2,m3=m; x=sp.symbols('x')
    poly=(m1+m2)*x**5+(3*m1+2*m2)*x**4+(3*m1+m2)*x**3-(m2+3*m3)*x**2-(2*m2+3*m3)*x-(m2+m3)
    return sum(1 for r in sp.Poly(poly,x).nroots() if abs(sp.im(r))<1e-9 and sp.re(r)>0)
# --- book side: K3 triangle region {|a-b|<=c<=a+b} join/meet closure (§12.11.2), and tree analogue
def closure_test(cap):
    cells=[(a,b,c) for a in range(1,cap+1) for b in range(1,cap+1) for c in range(1,cap+1) if abs(a-b)<=c<=a+b]
    S=set(cells); mf=jf=0
    for x,y in itertools.combinations(cells,2):
        if tuple(map(min,x,y)) not in S: mf+=1
        if tuple(map(max,x,y)) not in S: jf+=1
    tree=[(a,b) for a in range(1,cap+1) for b in range(1,cap+1) if b<=a]   # two-body: one edge, chain bound
    T=set(tree); tf=sum(1 for x,y in itertools.combinations(tree,2) if tuple(map(min,x,y)) not in T or tuple(map(max,x,y)) not in T)
    return len(cells),mf,jf,tf
print("case            | A shape=Newton | B norm=0 | C Euler | D Lagrange | E perm-sym | F Saari")
for name,m in cases.items():
    m=np.array(m,float)
    A=B=True; D=True; E=True
    for _ in range(50):
        q=rng.normal(size=3)+1j*rng.normal(size=3); q-=(m@q)/m.sum()
        Z1,Z2=jacobi(q,m); w=shape(Z1,Z2); R=np.sqrt(2*np.linalg.norm(w))   # I=2|w|, R=sqrt(I)
        Vs=V0_shape(w,m)
        A&=abs(Vs-U_newton(q,m))<TOL*max(1,U_newton(q,m))
        # [SEAM] B: degree-8 norm vanishes at the true potential
        b=binary_rays(m); us=[(m[i]*m[j])**1.5/np.sqrt(m[i]+m[j])/np.sqrt(np.linalg.norm(w)-w@b[(i,j)]) for (i,j) in b]
        B&=abs(f8(sum(us),*us))<1e-6*max(1,sum(us))**8
    # D: equilateral triangle is a critical point of U on the sphere I=const for these masses (Lagrange 1772): grad U ∝ grad I
    qe=np.array([1,np.exp(2j*np.pi/3),np.exp(4j*np.pi/3)]); qe-=(m@qe)/m.sum()
    g=np.zeros(3,complex)
    for i in range(3):
        for j in range(3):
            if i!=j: g[i]+=-m[i]*m[j]*(qe[i]-qe[j])/abs(qe[i]-qe[j])**3
    lam=(g@np.conj(m*qe)).real/(np.abs(m*qe)**2).sum()*1  # least-squares multiplier
    D=np.linalg.norm(g-lam*m*qe)<1e-9
    # E: permutation symmetry of V0 under mass-preserving relabellings
    perms=[p for p in itertools.permutations(range(3)) if all(m[p[i]]==m[i] for i in range(3))]
    for _ in range(20):
        q=rng.normal(size=3)+1j*rng.normal(size=3); q-=(m@q)/m.sum()
        for p in perms:
            qp=q[list(p)]; E&=abs(U_newton(q,m)-U_newton(qp,m))<TOL
    C=euler_roots(m)==1
    print(f"{name:15s} |  {A}          |  {B}    | {C} (1 root/ordering) | {D}   | {E} |S|={len(perms)} | theorem (all m)")
n,mf,jf,tf=closure_test(8)
print(f"\nBook §12.11.2 test, cap 8: triangle cells={n}, meet failures={mf}, join failures={jf}; two-body chain: failures={tf}")
