# RECONSTRUCTED FROM TRANSCRIPT (chat b778e075, 2026-08-23). Three inline python -c calls, joined in order.
# Second-route check (Register 784's mechanism): the inherited degree-8 polynomial vs the Galois norm over (Z/2)^3.
import sympy as sp, itertools
V,u1,u2,u3=sp.symbols('V u1 u2 u3')
P=sp.expand(sp.prod([V-e1*u1-e2*u2-e3*u3 for e1,e2,e3 in itertools.product([1,-1],repeat=3)]))
# --- call 1: the withdrawn polynomial, coefficients exactly as first written (Register 1707 / 1719)
S2=u1**2+u2**2+u3**2; S4=u1**4+u2**4+u3**4; S6=u1**6+u2**6+u3**6
S11=u1**2*u2**2+u2**2*u3**2+u3**2*u1**2   # plausible reading of S_11
claim=V**8-4*S2*V**6+(6*S2**2-4*S4+8*S11)*V**4-4*(S2**3-S2*S4+2*S6)*V**2+(S2**2-S4)**2-64*u1**2*u2**2*u3**2
print('claimed form matches norm:', sp.expand(P-claim)==0)
print(sp.Poly(P,V).all_coeffs())
# --- call 2: factor the true coefficients
c=sp.Poly(P,V).all_coeffs()
for k,co in zip([8,6,4,2,0],[c[0],c[2],c[4],c[6],c[8]]):
    print(k, sp.factor(co))
# --- call 3: the compact correct form N8 in p,q,r and a numeric sanity check
p,q,r=sp.symbols('p q r')
cand=V**8-4*p*V**6+(6*p**2-8*q)*V**4+(-4*p**3+16*p*q-64*r)*V**2+(p**2-4*q)**2
sub={p:u1**2+u2**2+u3**2,q:u1**2*u2**2+u2**2*u3**2+u3**2*u1**2,r:u1**2*u2**2*u3**2}
print('N8 compact form matches norm:', sp.expand(P-cand.subs(sub))==0)
print('N8 at u=(3,5,7), V=15:', sp.expand(P.subs({u1:3,u2:5,u3:7,V:15})))
# --- added for delivery: the two wrong terms, isolated (the finding 1707 states in words)
print('withdrawn U^4 coeff - true U^4 coeff =', sp.factor(sp.expand((6*S2**2-4*S4+8*S11)-(6*p**2-8*q).subs(sub))))
print('withdrawn U^2 coeff - true U^2 coeff =', sp.factor(sp.expand(-4*(S2**3-S2*S4+2*S6)-(-4*p**3+16*p*q-64*r).subs(sub))))
