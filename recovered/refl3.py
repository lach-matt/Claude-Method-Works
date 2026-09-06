import eldata as ed, itertools
occ=set(ed.E[z] for z in ed.E)
CAP={0:2,1:6,2:10,3:14,4:18}

print("="*76); print("STEP 5: ARE SWAPPABLE SHELLS PROFILE-IDENTICAL?"); print("="*76)
prof={n: tuple(sorted((l,k) for (nn,l,k) in occ if nn==n)) for n in range(1,8)}
for a,b in [(2,7),(3,6),(4,5),(1,2),(5,6)]:
    same = prof[a]==prof[b]
    print(f"  shells {a},{b}: profiles identical? {same}")
    if not same and (a,b) in [(2,7),(3,6),(4,5)]:
        print(f"     n={a}: {prof[a]}")
        print(f"     n={b}: {prof[b]}")
print()
print("  Profiles by shell:")
for n in range(1,8):
    print(f"    n={n}: {prof[n]}")