exec(open('red.py').read().split("I1=[")[0])
rho=sp.exp(U1+U2); om=U1+U2
h=rho**2*g3
gih,Gh,Rh=ricci(h,X3); print('Rh',time.time()-t0)
def d(f,a): return sp.diff(f,X3[a])
I3=[]
for a in range(3):
    for c in range(a,3):
        rhs=R5[a,c]+sum(d(Ui,a)*d(Ui,c) for Ui in (U1,U2))+d(om,a)*d(om,c)+g3[a,c]*(sp.exp(-2*U1)*R5[3,3]+sp.exp(-2*U2)*R5[4,4])
        I3.append(sp.simplify(Rh[a,c]-rhs))
print('I3',I3,time.time()-t0)
F=sp.Function('F')(v,r,th)
sh=sp.sqrt(sp.simplify(-h.det()))
boxh=sum(sp.diff(sh*gih[a,c]*d(F,c),X3[a]) for a in range(3) for c in range(3))/sh
I4=sp.simplify(boxh-box5(F)/rho**2); print('I4',I4,time.time()-t0)
# energy identity: X base vector, J5^a = g3^{ab} T5_bc X^c, div5 = (1/(rho sqrt g3)) d_a(rho sqrt g3 J^a)
Xv=[sp.Function('X%d'%i)(v,r,th) for i in range(3)]
grad2_g=sum(gi3[a,c]*d(F,a)*d(F,c) for a in range(3) for c in range(3))
T5=lambda a,c: d(F,a)*d(F,c)-sp.Rational(1,2)*g3[a,c]*grad2_g
J5=[sum(gi3[a,b_]*T5(b_,c)*Xv[c] for b_ in range(3) for c in range(3)) for a in range(3)]
div5=sum(sp.diff(rho*s3*J5[a],X3[a]) for a in range(3))/(rho*s3)
grad2_h=sum(gih[a,c]*d(F,a)*d(F,c) for a in range(3) for c in range(3))
Th=lambda a,c: d(F,a)*d(F,c)-sp.Rational(1,2)*h[a,c]*grad2_h
LXh=lambda a,c: sum(Xv[e]*sp.diff(h[a,c],X3[e])+h[e,c]*sp.diff(Xv[e],X3[a])+h[a,e]*sp.diff(Xv[e],X3[c]) for e in range(3))
Thup=lambda a,c: sum(gih[a,p]*gih[c,q]*Th(p,q) for p in range(3) for q in range(3))
XF=sum(Xv[e]*d(F,e) for e in range(3))
rhs=rho**2*(sp.Rational(1,2)*sum(Thup(a,c)*LXh(a,c) for a in range(3) for c in range(3))+XF*boxh)
I5=sp.simplify(sp.expand(div5-rhs)); print('I5',I5,time.time()-t0)
