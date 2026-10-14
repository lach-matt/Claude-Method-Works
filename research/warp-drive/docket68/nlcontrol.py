# PRE-DOCKET 68 COMPUTATION (2026-10-02), not seated.  A deterministic Weinberg-type non-linearity makes Bob's
# <sigma_y> depend on Alice's basis (signal ~ eps); the linear control gives 0.  See CHARTER.md.
import numpy as np
Z=np.diag([1.,-1]); X=np.array([[0,1.],[1,0]]); Y=np.array([[0,-1j],[1j,0]])
def U(H,dt):
    w,V=np.linalg.eigh(H); return V@np.diag(np.exp(-1j*w*dt))@V.conj().T
def evolve(p, eps, lin=False, T=3.0, n=3000):
    p=p.astype(complex); dt=T/n
    for _ in range(n):
        ex=np.real(p.conj()@X@p)
        H=(eps*Z if lin else eps*ex*Z)              # nonlinear: rotation rate set by the state's own <X>
        p=U(H,dt)@p; p/=np.linalg.norm(p)
    return p
ENS={'z':[np.array([1,0]),np.array([0,1])],'x':[np.array([1,1])/np.sqrt(2),np.array([1,-1])/np.sqrt(2)]}
def bob(basis_alice, eps, obs, lin=False):
    return np.mean([np.real(e.conj()@obs@e) for e in (evolve(s,eps,lin) for s in ENS[basis_alice])])
print("Bob's <sigma> after evolution, by Alice's choice of measurement basis (z or x):")
for lin in (True, False):
    print(" LINEAR control (H = eps Z):" if lin else " NON-LINEAR (H = eps <X> Z, Weinberg-type):")
    for eps in (1e-3,1e-2,1e-1):
        row=[]
        for nm,obs in (('X',X),('Y',Y),('Z',Z)):
            dz,dx=bob('z',eps,obs,lin),bob('x',eps,obs,lin); row.append(f"<{nm}> z:{dz:+.5f} x:{dx:+.5f}")
        print(f"   eps={eps:<6}", " | ".join(row))
