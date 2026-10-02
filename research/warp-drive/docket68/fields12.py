# PRE-DOCKET 68 COMPUTATION (2026-10-02), not seated.  Linear QM: twelve local fields on Alice's side leave Bob's
# reduced state unchanged.  See CHARTER.md.
import numpy as np
rng=np.random.default_rng(7)
I2=np.eye(2); Z=np.diag([1.,-1]); X=np.array([[0,1.],[1,0]]); Y=np.array([[0,-1j],[1j,0]])
def herm(n):
    A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); return (A+A.conj().T)/2
def expmH(H,t=1.0):
    w,V=np.linalg.eigh(H); return V@np.diag(np.exp(-1j*w*t))@V.conj().T
# Systems: Alice's qubit A, Alice's local apparatus/ancilla C (2 qubits), Bob's qubit B.  Order: A, C1, C2, B
singlet=np.array([0,1,-1,0])/np.sqrt(2)              # A,B
# build |s>_{AB} (x) |00>_{C} in order A,C1,C2,B
s=np.zeros(16,complex)
for a in range(2):
  for b in range(2):
    s[a*8+0*4+0*2+b]=singlet[a*2+b]
O=[herm(8) for _ in range(12)]                       # 12 independent "fields" coupling A and its local apparatus C
def bob_rho(g, t=1.0):
    H=sum(gk*Ok for gk,Ok in zip(g,O))               # H acts on A(x)C only
    U=np.kron(expmH(H,t),I2)
    v=U@s; M=v.reshape(8,2)                           # (A C) x B
    return M.T@M.conj()                               # Bob's reduced state
base=bob_rho(np.zeros(12))
worst=0.0
for k in range(12):                                   # vary each field alone, over a wide range
    for gk in np.linspace(-50,50,41):
        g=np.zeros(12); g[k]=gk
        worst=max(worst,np.abs(bob_rho(g)-base).max())
for _ in range(500):                                  # and all twelve together, random
    worst=max(worst,np.abs(bob_rho(rng.normal(scale=20,size=12),t=rng.uniform(0,10))-base).max())
print("LINEAR QM, 12 fields on Alice's side (each alone over [-50,50], and 500 random joint settings):")
print("  max change in Bob's state =", worst)

# CONTROL AS FIRST WRITTEN -- IT IS VACUOUS, KEPT AS A RECORDED FAULT.  H = eps<Z>Z + X is mapped to itself by
# conjugation with X, which swaps |0> and |1>, so the z-ensemble average of P(+z) is exactly 1/2 for every eps and
# the control can show nothing.  The working control is nlcontrol.py (H = eps<X>Z, Bob measuring sigma_y).
def nl_evolve(psi, eps, T=3.0, n=3000):
    dt=T/n; p=psi.astype(complex)
    for _ in range(n):
        ez=np.real(p.conj()@Z@p)                      # <sigma_z> of the state itself
        H=eps*ez*Z + 1.0*X                            # nonlinear term eps*<Z>Z plus an ordinary field
        p=expmH(H,dt)@p; p/=np.linalg.norm(p)
    return p
def bob_p_plus(alice_basis, eps):
    # Alice measures the singlet in basis z or x; Bob's qubit is left in the opposite eigenstate, each w.p. 1/2
    if alice_basis=='z': ens=[np.array([1,0]),np.array([0,1])]
    else: ens=[np.array([1,1])/np.sqrt(2),np.array([1,-1])/np.sqrt(2)]
    return np.mean([abs(nl_evolve(e,eps)[0])**2 for e in ens])   # Bob then measures sigma_z
print("CONTROL, Bob's P(+z) after evolution, by Alice's choice of basis:")
for eps in (0.0, 1e-3, 1e-2, 1e-1):
    pz,px=bob_p_plus('z',eps),bob_p_plus('x',eps)
    print(f"  eps={eps:<6} Alice z: {pz:.6f}   Alice x: {px:.6f}   difference: {abs(pz-px):.2e}")
