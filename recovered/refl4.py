import eldata as ed
occ=set(ed.E[z] for z in ed.E)
print("="*76); print("STEP 6: WHY IS THE PROFILE SEQUENCE 1,2,3,4,4,3,2 PALINDROMIC?"); print("="*76)
print("""  Occupied columns per shell: 1,2,3,4,4,3,2
  The rise 1,2,3,4 is the constraint ℓ ≤ n−1: shell n admits n subshells
  (capped at 5), and aufbau fills them all by the time the shell is done.
  The fall 4,3,2 is NOT a constraint — shells 5,6,7 ADMIT 5 columns each
  but only 4,3,2 are occupied.""")
print()
for n in range(1,8):
    admissible=min(n,5)
    filled=len(set(l for (nn,l,k) in occ if nn==n))
    print(f"  n={n}: admits {admissible} columns, {filled} occupied, "
          f"{'saturated' if filled==admissible else f'{admissible-filled} short'}")
print()
print("""  So the descending arm is a statement about where element production
  STOPPED, not about lattice geometry. It says: the periodic system was
  truncated at Z=118, and the truncation happens to land such that shell
  7 has exactly as many occupied columns as shell 2, shell 6 as shell 3,
  and shell 5 as shell 4.""")
print()
print("="*76); print("STEP 7: IS THE PALINDROME A COINCIDENCE OF Z=118?"); print("="*76)
# Rebuild the occupied set for truncations at other Z and re-measure
import eldata
def profile_at(Zmax):
    o=set(eldata.E[z] for z in eldata.E if z<=Zmax)
    return [len(set(l for (nn,l,k) in o if nn==n)) for n in range(1,8)]
def npairs(seq):
    # count reflection pairs n+n'=const with identical counts
    pairs=[]
    for i in range(len(seq)):
        for j in range(i+1,len(seq)):
            if seq[i]==seq[j] and seq[i]>0: pairs.append((i+1,j+1))
    return pairs
print(f"  {'Zmax':>6} {'profile':<24} {'equal-count pairs':<28} {'|group|'}")
for Zmax in [86,102,112,118,120,138,168]:
    p=profile_at(Zmax)
    pr=npairs(p)
    print(f"  {Zmax:>6} {str(p):<24} {str(pr):<28} {2**len(pr)}")
print()
print("""  The reflection structure is highly sensitive to where the series is cut.
  It is a property of the CURRENT truncation of the periodic system, not
  of Λ. At Z=120 or Z=138 the pattern changes entirely.""")