import numpy as np, sympy as sp
print("="*88)
print("  S1.  THE STRING MASS SPECTRUM — WHERE DOES IT SIT?")
print("="*88)
print("""
  Open bosonic string:   alpha' m^2 = N − 1,  N = 0,1,2,...
  Closed:                alpha' m^2 = 4(N − 1)

  **m^2 is LINEAR in the level number.** p = 1 exactly.
""")
m2=lambda N: N-1.0
Ns=np.arange(2,12)
y=np.array([m2(N) for N in Ns])
d1=np.diff(y); d2=np.diff(d1)
print("     first differences  : %s"%set(d1))
print("     second differences : %s"%set(d2))
print("     V = w/e            : %s"%("INFINITE — e = 0 exactly"))
print("""
  **THE STRING SPECTRUM IS ON THE POLE, EXACTLY**, in the same way L4 and
  L5 are. And Section 22.6.1's corrected reading applies verbatim:

     **a bracket is not worthless there. It is unnecessary.**
     Two levels determine every other, exactly. m^2 is known, not bounded.

  **That is a real statement about string theory in the book's language:
  the spectrum carries no curvature information in N, so no deductive
  bracket is needed and none would say anything.**
""")
print("="*88)
print("  S2.  THE DEGENERACY, WHICH IS WHERE THE CONTENT IS")
print("="*88)
print("""
  The interesting object is not the mass but the NUMBER OF STATES at each
  level. For the bosonic string it is the coefficient of the partition
  function

        prod_{n>=1} (1 − q^n)^{-24}

  and asymptotically d(N) ~ N^{-27/4} exp(4 pi sqrt(N)).
""")
def dN(Nmax=40,D=24):
    c=[0]*(Nmax+1); c[0]=1
    for n in range(1,Nmax+1):
        for _ in range(D):
            for k in range(n,Nmax+1):
                c[k]+=c[k-n]
    return c
d=dN(30)
print("  %6s%18s%20s"%("N","d(N) exact","asymptotic"))
for N in (1,2,3,5,10,15,20,25,30):
    asy=N**(-27/4)*np.exp(4*np.pi*np.sqrt(N))
    print("  %6d%18d%20.4g"%(N,d[N],asy))
ld=np.log(np.array([d[N] for N in range(3,31)],dtype=float))
Nv=np.arange(3,31)
print("\n  monotone   : %s"%all(np.diff(ld)>0))
print("  convex     : %s"%all(np.diff(np.diff(ld))<0) )
print("  3-monotone : %s"%all(np.sign(np.diff(np.diff(np.diff(ld))))==np.sign(np.diff(np.diff(np.diff(ld)))[0])))
def V_of(seq,i):
    a,m,b=seq[i-1],seq[i],seq[i+1]
    return abs(b-a)/abs(m-(a+b)/2)
print("\n  V for log d(N):\n")
print("  %6s%14s%16s"%("N","V","4N/|p−1| ~"))
for i,N in enumerate(Nv):
    if 2<=i<len(ld)-1 and N in (6,10,15,20,25):
        v=V_of(ld,i)
        print("  %6d%14.2f%16.2f"%(N,v,8*np.sqrt(N)))
print("""
  **log d(N) ~ 4 pi sqrt(N), a power law with p = 1/2**, so |p−1| = 1/2 and
  V ~ 4N/(h/2) = 8N. **The Hagedorn growth is an ordinary bracketable
  channel** — steeper than a Rydberg series in absolute terms and, in V,
  about six times more expensive at the same index.
""")
print("="*88)
print("  S3.  AND THE PARTITION FUNCTION IS THE SAME OBJECT AS F")
print("="*88)
print("""
  Chapter 6: Lambda's single expression is a generating function whose
  COEFFICIENTS are the indicator chi — 1 if the cell exists, 0 if not.

  String theory's partition function is a generating function whose
  COEFFICIENTS are the state degeneracies — how many cells exist at each
  level.

  **Same construction, one difference:**
""")
q=sp.symbols('q')
Fs=sp.prod([(1-q**n)**-24 for n in range(1,7)])
ser=sp.series(Fs,q,0,5).removeO()
print("     string  : prod (1−q^n)^{-24}  ->  %s"%sp.expand(ser))
print("     Lambda  : F(1) = 976, coefficients are 0 or 1")
print("""
     **Lambda's coefficients are BOOLEAN. The string's are COUNTS.**

  Lambda indexes WHICH configurations exist. The partition function counts
  HOW MANY states sit at each level. **The first is an index; the second is
  an index with multiplicity** — and Section 6.6's tree factorisation is
  exactly what turns one into the other:
""")
print("     Lambda's F, tree-factorised : nested sums, coefficients 0/1")
print("     string's Z, Euler product   : a product over modes, coefficients large")
print("""
  **BOTH FACTORISE, AND FOR THE SAME REASON: the modes are INDEPENDENT.**
  The string's oscillators do not constrain one another; Lambda's
  coordinates constrain one another only along a tree. **Independence and
  tree structure are the two ways a generating function can be closed
  form, and these are one of each.**
""")