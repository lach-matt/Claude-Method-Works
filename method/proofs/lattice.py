"""Is the triangle region a lattice, or only not a SUBLATTICE?

Appendix A.18 heads "The triangle region is join-closed and meet-broken"; main SS12.11.2 and the
three-body paper's Law 3 say "not a lattice". Those are different propositions: a set can be a
lattice under its induced order without being closed under the ambient componentwise operations.
This tests the stronger one. The regions are built exactly as the seated instrument r2-ch19a3.py
builds them, and C at cap 8 reproduces Appendix A.15's printed 12,654 meet failures, which is what
identifies the object. Standard library only.
"""
import itertools
def Cr(c): return [(a,b,cc) for a in range(c+1) for b in range(c+1) for cc in range(c+1) if abs(a-b)<=cc]
def Tr(c): return [(a,b,j) for a in range(c+1) for b in range(c+1) for j in range(c+1) if abs(a-b)<=j<=a+b]
def le(x,y): return all(p<=q for p,q in zip(x,y))
def analyse(X, name, cap):
    S=set(X); mfail=jfail=noglb=nolub=0
    for x,y in itertools.combinations(X,2):
        mn=tuple(map(min,x,y)); mx=tuple(map(max,x,y))
        if mn not in S:
            mfail+=1
            LB=[z for z in X if le(z,x) and le(z,y)]
            if len([z for z in LB if not any(z!=w and le(z,w) for w in LB)])!=1: noglb+=1
        if mx not in S:
            jfail+=1
            UB=[z for z in X if le(x,z) and le(y,z)]
            if len([z for z in UB if not any(z!=w and le(w,z) for w in UB)])!=1: nolub+=1
    print(f'{name} cap {cap}: |X|={len(X):,}  componentwise meet fails {mfail:,}  join fails {jfail:,}')
    print(f'    pairs with NO greatest lower bound in the region: {noglb:,}')
    print(f'    pairs with NO least upper bound in the region   : {nolub:,}')
    print(f'    => a LATTICE under the induced order: {noglb==0 and nolub==0}')
if __name__ == '__main__':
    for cap in (4,6,8): analyse(Tr(cap), 'T two-sided |a-b|<=j<=a+b', cap)
    for cap in (4,6,8): analyse(Cr(cap), 'C one-sided |a-b|<=c    ', cap)
    print("\nAppendix A.15 prints 12,654 meet failures for C at cap 8; reproduced above.")
