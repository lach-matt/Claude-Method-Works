import math
from collections import defaultdict
L="spdfg h i"
LN="s p d f g h i".split()
print("  WHAT HAPPENS AT k = 3  —  the 3D oscillator's shells, enumerated\n")
print("      the isotropic 3D oscillator has E = ħω(2n_r + ℓ + 3/2), so shell N")
print("      holds every (n_r, ℓ) with 2n_r + ℓ = N.  ℓ has the parity of N.\n")
print(f"      {'N':>3}{'subshells':>28}{'capacity':>10}{'cumulative':>12}")
cum=0; SH=[]
for N in range(7):
    ls=list(range(N%2, N+1, 2))
    cap=sum(2*(2*l+1) for l in ls)
    cum+=cap
    s=" ".join(f"{(N-l)//2+1}{LN[l]}" for l in ls)
    print(f"      {N:>3}{s:>28}{cap:>10}{cum:>12}")
    SH.append((N,ls,cap,cum))
print()
print("  THE HIGHEST ℓ IN EACH SHELL, AND WHAT IT COSTS\n")
print("      Mayer's spin-orbit term lowers j = ℓ+½ by an amount ∝ ℓ, so the")
print("      TOP ℓ of shell N drops into shell N−1.  its capacity is 2(ℓ+1)")
print("      because only the j = ℓ+½ half descends.\n")
print(f"      {'N':>3}{'top ℓ':>7}{'orbital':>9}{'2(ℓ+1)':>9}"
      f"{'HO cum':>9}{'− drop + prev drop':>20}{'= magic?':>10}")
MAG=[2,8,20,28,50,82,126]
prev=0
for N,ls,cap,cum in SH:
    top=ls[-1]
    drop=2*(top+1)
    val=cum-drop+prev
    hit="YES" if val in MAG else ""
    print(f"      {N:>3}{LN[top]:>7}{(N-top)//2+1}{LN[top]:<8}{drop:>9}"
          f"{cum:>9}{val:>20}{hit:>10}")
    prev=drop
print()
print("  READING\n")
print("      the rule is: shell N's highest-ℓ orbital, in its j = ℓ+½ half,")
print("      leaves shell N and joins shell N−1.  the closure after shell N is")
print("      then  (HO cumulative) − (what left) + (what arrived from N+1).")
print()
print("      that is a COUNTING statement. no strength enters — only WHICH")
print("      orbital moves, and the capacity 2(ℓ+1) that Pauli fixes.")