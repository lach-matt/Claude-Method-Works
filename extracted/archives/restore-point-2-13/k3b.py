import math
LN="s p d f g h i k".split()
print("  THE MAGIC NUMBERS AS A COUNTING STATEMENT\n")
print("      3D oscillator shell N holds every (n_r, ℓ) with 2n_r + ℓ = N.")
print("      its highest ℓ is N, and the j = ℓ+½ half of that orbital holds")
print("      2j+1 = 2(N+1) states.\n")
cum=[]; c=0
for N in range(8):
    ls=list(range(N%2,N+1,2))
    c+=sum(2*(2*l+1) for l in ls); cum.append(c)
MAG=[2,8,20,28,50,82,126,184]
print(f"      {'N':>3}{'HO cum(N)':>11}{'HO cum(N−1)':>13}{'2(N+1)':>9}"
      f"{'sum':>7}{'magic':>8}{'':>4}")
for N in range(8):
    prev = cum[N-1] if N>0 else 0
    val = prev + 2*(N+1)
    m = MAG[N] if N<len(MAG) else None
    hit = "  ✓" if m==val else ("  = HOcum" if m==cum[N] else "")
    print(f"      {N:>3}{cum[N]:>11}{prev:>13}{2*(N+1):>9}{val:>7}"
          f"{(m if m else '—'):>8}{hit:>4}")
print()
print("  THE RULE, IN TWO REGIMES\n")
print(f"      {'N':>3}{'magic':>8}{'HO cum(N)':>12}{'HOcum(N−1)+2(N+1)':>20}{'  which'}")
for N in range(8):
    prev = cum[N-1] if N>0 else 0
    a=cum[N]; b=prev+2*(N+1); m=MAG[N] if N<len(MAG) else None
    w = "HO cum" if m==a else ("descended" if m==b else "neither")
    print(f"      {N:>3}{(m if m else '—'):>8}{a:>12}{b:>20}   {w}")
print()
print("      N ≤ 2 : magic = HO cum(N).  the bare oscillator.")
print("      N ≥ 3 : magic = HO cum(N−1) + 2(N+1).  ALL FOUR EXACT.")
print()
print("  AND WHY N = 3\n")
print("      the descended orbital arrives with 2(N+1) states.  the shell it")
print("      LEAVES then holds HOcum(N) − HOcum(N−1) − 2(N+1) states.")
print(f"      {'N':>3}{'shell cap':>11}{'2(N+1)':>9}{'remainder':>11}{'  ratio'}")
for N in range(8):
    prev = cum[N-1] if N>0 else 0
    capN = cum[N]-prev; d=2*(N+1); rem=capN-d
    print(f"      {N:>3}{capN:>11}{d:>9}{rem:>11}{d/capN:>8.3f}")
print()
print("      the descended fraction 2(N+1)/cap(N) falls: 1.000, 0.667, 0.500,")
print("      0.400, 0.333, 0.286, 0.250.  at N ≤ 2 the WHOLE top orbital is")
print("      more than half the shell; at N ≥ 3 it is less.")
print()
print("      → N = 3 is where the descending orbital stops dominating its own")
print("        shell.  that is a counting threshold, not a strength.")
