import sympy as sp
t,x,y,z,M=sp.symbols('t x y z M',real=True)
Y=[t,x,y,z]; r=sp.sqrt(x**2+y**2+z**2); Phi=-M/r
g=sp.diag(-(1+2*Phi),1-2*Phi,1-2*Phi,1-2*Phi); gi=g.inv()
G=[[[sum(gi[a,e]*(sp.diff(g[e,b],Y[c])+sp.diff(g[e,c],Y[b])-sp.diff(g[b,c],Y[e])) for e in range(4))/2 for c in range(4)] for b in range(4)] for a in range(4)]
def Rup(a,b,c,d):
    return sp.diff(G[a][b][d],Y[c])-sp.diff(G[a][b][c],Y[d])+sum(G[a][c][e]*G[e][b][d]-G[a][d][e]*G[e][b][c] for e in range(4))
Mv=-2e-3; p={x:0,y:0.3,z:0,M:Mv}
Rl=[[[[float(sum(g[a,e]*Rup(e,b,c,d) for e in range(4)).subs(p)) for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
def T(k,ei,ej): return -sum(Rl[m][a][n][b]*k[m]*ei[a]*k[n]*ej[b] for m in range(4) for a in range(4) for n in range(4) for b in range(4))
e1=[0,0,1,0]; e2=[0,0,0,1]
ph=-Mv/0.3; s=((1+2*ph)/(1-2*ph))**0.5
for lab,k in (("k=(1,1,0,0) [composite static check]",[1,1,0,0]),("k=(1,s,0,0) true null",[1,s,0,0])):
    a,b=T(k,e1,e1),T(k,e2,e2)
    print("%-40s T11=%.6e T22=%.6e |tr|/max=%.3e" % (lab,a,b,abs(a+b)/max(abs(a),abs(b))))
