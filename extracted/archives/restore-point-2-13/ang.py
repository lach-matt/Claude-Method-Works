import math
from math import factorial as f
L="spdfg"
def tj2(l1,k,l2):
    J=l1+k+l2
    if J%2 or l2<abs(l1-k) or l2>l1+k: return 0.0
    g=J//2
    v=((-1)**g)*math.sqrt(f(J-2*l1)*f(J-2*k)*f(J-2*l2)/f(J+1))*\
      f(g)/(f(g-l1)*f(g-k)*f(g-l2))
    return v*v
print("  THE ANGULAR PART OF G^k — IS IT PURE ENUMERATION?\n")
print("      the exchange integral's angular factor is (l₁ k l₂; 0 0 0)².")
print("      F⁰'s angular factor is 1. so the ratio G^k/F⁰ carries this")
print("      number times a radial ratio.\n")
print(f"      {'pair':>7}{'k':>4}{'(l₁ k l₂;000)²':>18}{'as a fraction':>16}")
for l1,l2 in ((0,0),(0,1),(0,2),(0,3),(1,1),(2,2),(3,3),(1,2),(2,3)):
    ks=list(range(abs(l1-l2),l1+l2+1,2))
    for k in ks:
        v=tj2(l1,k,l2)
        fr=""
        for d in range(1,200):
            if abs(v*d-round(v*d))<1e-9 and round(v*d)>0:
                fr=f"{round(v*d)}/{d}"; break
        print(f"      {L[l1]+'/'+L[l2]:>7}{k:>4}{v:>18.8f}{fr:>16}")
print()
print("  THE s/ℓ CASE — the one every ladder uses\n")
print(f"      {'pair':>7}{'k':>4}{'value':>14}{'  1/(2ℓ+1)?'}")
for l2 in (0,1,2,3):
    v=tj2(0,l2,l2)
    print(f"      {'s/'+L[l2]:>7}{l2:>4}{v:>14.8f}   1/{2*l2+1} = {1/(2*l2+1):.8f}"
          f"   {'YES' if abs(v-1/(2*l2+1))<1e-12 else 'no'}")
print()
print("  THE RESULT\n")
print("      for an s electron against an ℓ electron, the ONLY exchange")
print("      integral is G^ℓ, and its angular factor is exactly 1/(2ℓ+1).")
print()
print("      1/(2ℓ+1) is the reciprocal of the subshell's ORBITAL degeneracy —")
print("      a count, and one Λ already holds.")
print()
print("      → the angular half of G/F IS enumerable from Λ. what is not is")
print("        the RADIAL ratio R^ℓ(ns,n'ℓ)/R^0(ns,n'ℓ).")
print()
print("  AND WHAT THAT LEAVES\n")
print("      a(c) = [angular: 1/(2ℓ+1), from Λ] × [radial: an integral]")
print()
print("      the person's claim is that the enumeration carries the value.")
print("      half of it demonstrably does — exactly, as a degeneracy count.")
print("      the radial half depends on the wavefunctions, and Λ holds")
print("      occupancies, not wavefunctions.")
print()
print("      unless the radial ratio is ALSO fixed by counting — which is")
print("      the remaining question and is not settled here.")
