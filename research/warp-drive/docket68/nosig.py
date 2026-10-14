# PRE-DOCKET 68 COMPUTATION (2026-10-02), not seated.  Singlet: CHSH = 2*sqrt2, and Alice's choice of angle
# carries 0 bits to Bob.  See CHARTER.md.
import numpy as np
# Singlet; Alice measures along angle a, Bob along b (spin in x-z plane).
s = np.array([0,1,-1,0])/np.sqrt(2)
Z=np.diag([1,-1]); X=np.array([[0,1],[1,0]])
P=lambda t,o: (np.eye(2)+o*(np.cos(t)*Z+np.sin(t)*X))/2   # projector, outcome o=+-1
def joint(a,b):
    return {(oa,ob): float(s@np.kron(P(a,oa),P(b,ob))@s) for oa in (1,-1) for ob in (1,-1)}
E=lambda a,b: sum(oa*ob*p for (oa,ob),p in joint(a,b).items())
a0,a1,b0,b1=0,np.pi/2,np.pi/4,-np.pi/4
print("CHSH |S| =", abs(E(a0,b0)+E(a0,b1)+E(a1,b0)-E(a1,b1)), "(local-hidden-variable max 2, Tsirelson 2*sqrt2 =", 2*np.sqrt(2),")")
# Bob's outcome statistics for each of Alice's choices: identical => Alice's choice carries 0 bits to Bob
for b in (b0,b1):
    margs=[ (round(joint(a,b)[(1,1)]+joint(a,b)[(-1,1)],15)) for a in np.linspace(0,np.pi,7)]
    print("P(Bob=+1 | Alice angle a) over 7 choices of a:", margs)
# Mutual information between Alice's setting X (uniform over 7) and Bob's outcome R
import math
for b in (b0,):
    A=np.linspace(0,np.pi,7); pr=[joint(a,b)[(1,1)]+joint(a,b)[(-1,1)] for a in A]
    pbar=np.mean(pr); H=lambda p: -sum(q*math.log2(q) for q in (p,1-p) if q>0)
    print("I(Alice's choice ; Bob's outcome) =", H(pbar)-np.mean([H(p) for p in pr]), "bits")
