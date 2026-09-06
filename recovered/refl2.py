import eldata as ed
occ=set(ed.E[z] for z in ed.E)
CAP={0:2,1:6,2:10,3:14,4:18}
print("="*76); print("STEP 3: WHY n + n' = 9?  WHICH SHELLS ARE INTERCHANGEABLE?"); print("="*76)
# occupied (l,k) profile of each shell
prof={}
for n in range(1,8):
    cells=sorted((l,k) for (nn,l,k) in occ if nn==n)
    cols=sorted(set(l for l,k in cells))
    prof[n]=(cols, {l:max([k for ll,k in cells if ll==l], default=0) for l in cols})
print(f"  {'n':>3} {'ℓ present':<16} {'column heights':<28} {'ℓ_max allowed':>14}")
for n in range(1,8):
    cols,h=prof[n]
    print(f"  {n:>3} {str(cols):<16} {str([h[l] for l in cols]):<28} {min(n-1,4):>14}")
print()
print("  Pairs that swap: (2,7), (3,6), (4,5).  Note 2+7 = 3+6 = 4+5 = 9.")
print("  Shell 1 is fixed. 1+8=9 would need a shell 8, which does not exist.")
print()
print("="*76); print("STEP 4: IS IT ABOUT COLUMN COUNTS?"); print("="*76)
for n in range(1,8):
    cols,h=prof[n]
    filled=len(cols)
    allowed=min(n,5)
    print(f"  n={n}: {filled} occupied columns of {allowed} admissible")
print()
print("  Occupied-column counts by shell: ", [len(prof[n][0]) for n in range(1,8)])
print("  Reversed:                         ", [len(prof[n][0]) for n in range(7,0,-1)])