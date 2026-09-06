import sympy as sp
print("="*88)
print("  §23.5 RE-RUN — THE RELATION SET IS LARGER THAN WHEN IT WAS AUDITED")
print("="*88)
print("""
  §23.5 closed {V = 4ν/3h, λ² = (2/3)T, w·V = 8λ², T = Z²R/ν²} and found
  three admitted claims the search list omitted. **That was the relation
  set as it stood then.** The book now states considerably more.
""")
V,w,e,T,h,nu,lam,Z,R,r,k,x,p=sp.symbols('V w e T h nu lam Z R r k x p',positive=True)
ORIG=[3*h*V-4*nu, 3*lam**2-2*T, w*V-8*lam**2, T*nu**2-Z**2*R]
NEW=[3*h*V-4*nu, 3*lam**2-2*T, w*V-8*lam**2, T*nu**2-Z**2*R,
     w*nu-4*T*h, e*nu**2-3*T*h**2, V*e-w,
     V*h*(3*nu**2-h**2)-4*nu**3]
print("     relations at the time of the audit : %d"%len(ORIG))
print("     relations stated in the book now   : %d"%len(NEW))
gb0=sp.groebner(ORIG,V,w,e,lam,T,h,nu,Z,R,order='lex')
gb1=sp.groebner(NEW,V,w,e,lam,T,h,nu,Z,R,order='lex')
print("     Gröbner basis then / now          : %d / %d"%(len(gb0.exprs),len(gb1.exprs)))
print("="*88)
print("  WHAT THE ENLARGED SET ADMITS")
print("="*88)
CAND=[("w/T = 4h/ν",              w*nu-4*T*h,            "on the §23.5 list"),
      ("e/T = 3(h/ν)²",           e*nu**2-3*T*h**2,      "on the §23.5 list"),
      ("V·e = w",                 V*e-w,                 "on the §23.5 list"),
      ("V = 4ν³/(h(3ν²−h²))",     V*h*(3*nu**2-h**2)-4*nu**3, "?"),
      ("w·V = (16/3)T",           3*w*V-16*T,            "?"),
      ("λ² = (2/3)T",             3*lam**2-2*T,          "?"),
      ("w² = (16/3)·T·e",         3*w**2-16*T*e,         "?"),
      ("e·V² = w²/e ... i.e. w² = V²e²", w**2-V**2*e**2,  "?"),
      ("λ² = w·e/8 ... i.e. 8λ² = wV and V=w/e", 8*lam**2*e-w**2, "?"),
      ("T·h² = e·ν²/3",           3*T*h**2-e*nu**2,      "?"),
      ("V² = 16ν²/(9h²)",         9*h**2*V**2-16*nu**2,  "?"),
      ("w·e = ... ",              w*e*9*h**2-16*nu**2*e**2, "?")]
print("\n  %-34s%16s%16s"%("relation","reduces (then)","reduces (now)"))
print("  "+"-"*68)
new_admitted=[]
for nm,pol,note in CAND:
    r0=sp.simplify(gb0.reduce(pol)[1])
    r1=sp.simplify(gb1.reduce(pol)[1])
    print("  %-34s%16s%16s"%(nm,"0" if r0==0 else "no","0" if r1==0 else "no"))
    if r1==0 and r0!=0: new_admitted.append(nm)
print("\n     admitted NOW but not THEN : %d  %s"%(len(new_admitted),new_admitted))
print("="*88)
print("  AND THE NON-POLYNOMIAL RELATIONS THE BOOK NOW STATES")
print("="*88)
print("""
  §23.5's closure is over POLYNOMIAL relations. The book has since added
  relations that are not polynomial, and they were never audited at all:
""")
NP=[("A^m(x^p) = (−1)^m x^p/(p−1)^m","rational in p, pole at p = 1"),
    ("exponential V = 2/tanh(kh/2)","transcendental"),
    ("self-concordance ν ≤ (√6/2)Z√R","an inequality, not an identity"),
    ("Aitken(T) = T/3","a limit, provable from A^m at p = −2"),
    ("rank(a∨b)+rank(a∧b) = rank(a)+rank(b)","lattice, not algebraic"),
    ("Σ_q |A_q||B_q| = |Λ|","combinatorial"),
    ("F(−1) = 2 from F_box(−1) = 0","combinatorial"),
    ("E(X) = size of the non-pairwise content","order-theoretic"),
    ("reorderable ⟺ C1P + monotone endpoints","order-theoretic")]
print("  %-46s%s"%("relation","kind"))
print("  "+"-"*74)
for a,b in NP: print("  %-46s%s"%(a,b))
print("""
  **Nine relations outside the polynomial closure, none of them audited
  against a target list.**

  > **E(target list) is not 3. It was 3 for the relation set of that
  > moment, and the audit has not been re-run since.**

  **That is §23.5's own finding, committed a second time by the same
  auditor** — the list was enumerated once and the structure kept growing.
  **C.2.10 says enumerate targets BEFORE searching; it does not say
  enumerate them once.**
""")