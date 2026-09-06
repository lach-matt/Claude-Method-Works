import eldata as ed
print("="*74)
print("TEST 1: DOES Λ SAY ANYTHING ABOUT ANOMALOUS GROUND STATES?")
print("="*74)
# Elements whose measured ground state departs from strict Madelung filling
ANOM = {
 24:('Cr','[Ar]3d5 4s1','expected 3d4 4s2'),
 29:('Cu','[Ar]3d10 4s1','expected 3d9 4s2'),
 41:('Nb','[Kr]4d4 5s1','expected 4d3 5s2'),
 42:('Mo','[Kr]4d5 5s1','expected 4d4 5s2'),
 44:('Ru','[Kr]4d7 5s1','expected 4d6 5s2'),
 45:('Rh','[Kr]4d8 5s1','expected 4d7 5s2'),
 46:('Pd','[Kr]4d10','expected 4d8 5s2'),
 47:('Ag','[Kr]4d10 5s1','expected 4d9 5s2'),
 57:('La','[Xe]5d1 6s2','expected 4f1 6s2'),
 58:('Ce','[Xe]4f1 5d1 6s2','expected 4f2 6s2'),
 64:('Gd','[Xe]4f7 5d1 6s2','expected 4f8 6s2'),
 78:('Pt','[Xe]4f14 5d9 6s1','expected 5d8 6s2'),
 79:('Au','[Xe]4f14 5d10 6s1','expected 5d9 6s2'),
 89:('Ac','[Rn]6d1 7s2','expected 5f1 7s2'),
 90:('Th','[Rn]6d2 7s2','expected 5f2 7s2'),
 91:('Pa','[Rn]5f2 6d1 7s2','expected 5f3 7s2'),
 92:('U','[Rn]5f3 6d1 7s2','expected 5f4 7s2'),
 93:('Np','[Rn]5f4 6d1 7s2','expected 5f5 7s2'),
 96:('Cm','[Rn]5f7 6d1 7s2','expected 5f8 7s2'),
 103:('Lr','[Rn]5f14 7s2 7p1','expected 5f14 6d1 7s2'),
}
print(f"  {len(ANOM)} elements with anomalous ground-state configurations\n")

# Where do these sit in Lambda?
print("  Lattice position of the anomalous elements:")
print(f"  {'Z':>4} {'sym':>4} {'(n,l,k)':>12} {'l=n-1?':>8} {'k/kmax':>8} {'rank':>6}")
print("  "+"-"*52)
kain=0; halffull=0; full=0
for z in sorted(ANOM):
    n,l,k = ed.E[z]
    km=2*(2*l+1)
    onbd = (l==n-1)
    frac = k/km
    if onbd: kain+=1
    if abs(frac-0.5)<0.06: halffull+=1
    if frac>0.95: full+=1
    print(f"  {z:>4} {ANOM[z][0]:>4} {str((n,l,k)):>12} {str(onbd):>8} {frac:>8.2f} {n+l+k:>6}")
print()
print(f"  on the kainosymmetric boundary l=n-1: {kain}/{len(ANOM)}")
print(f"  at half-filled subshell (k/kmax≈0.5): {halffull}/{len(ANOM)}")
print(f"  at filled subshell (k/kmax>0.95):     {full}/{len(ANOM)}")
print()
# baseline: what fraction of ALL elements are at half/full?
allh=sum(1 for z in ed.E if abs(ed.E[z][2]/(2*(2*ed.E[z][1]+1))-0.5)<0.06)
allf=sum(1 for z in ed.E if ed.E[z][2]/(2*(2*ed.E[z][1]+1))>0.95)
allb=sum(1 for z in ed.E if ed.E[z][1]==ed.E[z][0]-1)
print(f"  BASELINE across all 118 elements:")
print(f"    half-filled: {allh}/118 = {100*allh/118:.0f}%   anomalous: {100*halffull/len(ANOM):.0f}%")
print(f"    filled:      {allf}/118 = {100*allf/118:.0f}%   anomalous: {100*full/len(ANOM):.0f}%")
print(f"    boundary:    {allb}/118 = {100*allb/118:.0f}%   anomalous: {100*kain/len(ANOM):.0f}%")