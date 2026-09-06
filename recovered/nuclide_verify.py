# §6.2.1 prints the method and the named cells. Verify E=9 by reconstructing the
# PARTICLE-BOUND nuclide set at low Z and running the A.R closure.
# The book prints: the nine absent cells are He-5,He-7,Li-10,Be-8,Be-13,B-9,B-16,B-18,C-21.
# (Z,N): He=2, Li=3, Be=4, B=5, C=6.  N = A - Z.
# He-5=(2,3) He-7=(2,5) Li-10=(3,7) Be-8=(4,4) Be-13=(4,9) B-9=(5,4) B-16=(5,11) B-18=(5,13) C-21=(6,15)
named_absent = {(2,3),(2,5),(3,7),(4,4),(4,9),(5,4),(5,11),(5,13),(6,15)}

# The particle-bound nuclides at low Z (the chart "as nature draws it").
# Build the known particle-bound (stable OR particle-stable, i.e. not neutron/proton-unbound) set
# for Z=1..6, from standard nuclear data. Particle-bound = does not immediately emit a nucleon.
# H(1): 1,2,3(H-3 beta but particle-bound). n up to: H-1(0),H-2(1),H-3(2). H-4+ neutron-unbound.
# He(2): He-3(1),He-4(2),He-6(4),He-8(6) bound; He-5(3),He-7(5) UNBOUND (named); He-9,He-10 unbound.
# Li(3): Li-6(3),Li-7(4),Li-8(5),Li-9(6),Li-11(8) bound; Li-10(7) UNBOUND (named); Li-5 (2) p-unbound.
# Be(4): Be-7(3),Be-9(5),Be-10(6),Be-11(7),Be-12(8),Be-14(10) bound; Be-8(4) UNBOUND(alpha), Be-13(9) UNBOUND (named); Be-6(2) unbound.
# B(5): B-8(3),B-10(5),B-11(6),B-12(7),B-13(8),B-14(9),B-15(10),B-17(12),B-19(14) bound;
#        B-9(4) UNBOUND, B-16(11) UNBOUND, B-18(13) UNBOUND (named); B-7(2) unbound.
# C(6): C-9(3)..C-22(16) mostly bound; C-21(15) is the named unbound interior cell.
# I build, per the book's method, the MEASURED (particle-bound) cell set over Z<=7 window minus the named,
# then close and check the closure re-adds exactly the named nine.

# Particle-bound cells (Z,N) for Z=1..6 (interior of each isotope chain, bound members):
bound = set()
bound |= {(1,0),(1,1),(1,2)}                                  # H-1,2,3
bound |= {(2,1),(2,2),(2,4),(2,6)}                            # He-3,4,6,8
bound |= {(3,3),(3,4),(3,5),(3,6),(3,8)}                      # Li-6,7,8,9,11
bound |= {(4,3),(4,5),(4,6),(4,7),(4,8),(4,10)}              # Be-7,9,10,11,12,14
bound |= {(5,3),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,12),(5,14)}  # B-8,10..15,17,19
bound |= {(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9),(6,10),(6,11),(6,12),(6,13),(6,14),(6,16)} # C-9..22 bound (C-21 absent)

def closure(X):
    S=set(X); changed=True
    while changed:
        changed=False; new=set()
        L=list(S)
        for a in L:
            for b in L:
                jn=(max(a[0],b[0]),max(a[1],b[1])); mt=(min(a[0],b[0]),min(a[1],b[1]))
                if jn not in S: new.add(jn)
                if mt not in S: new.add(mt)
        if new: S|=new; changed=True
    return S

# The book's count is over the (Z,N) chart; the closure is the (<=,<=) staircase fill.
# NOTE: the book's operator fills the band between drip lines. The join/meet closure here
# approximates that fill; the KEY CHECK is directional: does E>0 and are the named cells inside R(X)\X?
X = bound
R = closure(X)
added = R - X
print("input cells |X| =", len(X))
print("|R(X)| =", len(R), "  E = |R|-|X| =", len(R)-len(X))
print("named-absent nine all inside R(X)\\X ?", named_absent.issubset(added))
print("of the nine, how many the closure re-adds:", len(named_absent & added), "/ 9")
missing = named_absent - added
if missing: print("  named cells NOT re-added by this closure:", sorted(missing))
extra = added - named_absent
print("cells the closure adds beyond the named nine:", len(extra))
if extra: print("  extras (first 20):", sorted(extra)[:20])