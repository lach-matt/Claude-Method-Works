from math import sqrt
# What the capture supplies: two ISOELECTRONIC sequences, Ne = 1 and Ne = 2.
# Spot-check three values read off the image against physics, to confirm the format.
R_H = 109678.77174307      # H I, from the capture
print("FORMAT CHECK")
print(f"  H I   {R_H:>14.2f} cm-1   Rydberg for H")
print(f"  He II  438908.88 cm-1   vs 4x H = {4*R_H:>10.2f}   ratio {438908.87884/R_H:.4f}  (Z^2, reduced-mass shifted)")
print(f"  Li III 987661.01 cm-1   vs 9x H = {9*R_H:>10.2f}   ratio {987661.0139/R_H:.4f}")
print(f"  He I   198310.67 cm-1   = 24.587 eV, the two-electron ground   OK")

# What the corridor gets from these sequences.
# nu(n,l,q) = n - a*sqrt(n-l-1 + q/(2(2l+1)))
def nu(n,l,q,a): return n - a*sqrt((n-l-1) + q/(2*(2*l+1)))

print("\nCORRIDOR CONSTRAINTS THESE SEQUENCES GENERATE")
# Ne=1: electron enters 1s of an empty atom. Rivals: 2s,2p,3s,3p,3d.
print("  Ne=1  ground 1s (q=0). rivals and the a they force:")
for (n,l,nm) in [(2,0,'2s'),(2,1,'2p'),(3,0,'3s'),(3,2,'3d')]:
    # need nu(1s) < nu(rival):  1 - 0 < n - a*sqrt(p)
    p = n-l-1
    if p > 0:
        print(f"    1s < {nm}:  1 < {n} - a*sqrt({p})  ->  a < {(n-1)/sqrt(p):.4f}")
    else:
        print(f"    1s < {nm}:  1 < {n}  ->  no constraint on a (p=0)")

print("  Ne=2  second electron enters 1s (q=1). rivals:")
g = nu(1,0,1,0)  # symbolic handled below
for (n,l,nm) in [(2,0,'2s'),(2,1,'2p')]:
    p = n-l-1
    # 1 - a*sqrt(0.5) < n - a*sqrt(p)   ->  a*(sqrt(p) - sqrt(0.5)) < n-1
    coef = sqrt(p) - sqrt(0.5)
    if abs(coef) < 1e-12:
        print(f"    1s < {nm}:  degenerate")
    elif coef > 0:
        print(f"    1s < {nm}:  a < {(n-1)/coef:.4f}")
    else:
        print(f"    1s < {nm}:  a > {(n-1)/coef:.4f}  (vacuous, a>0)")

print("\nWHAT VARIES ALONG THESE SEQUENCES")
print("  ground shells column is constant: '1s' for all 110 rows, '1s2' for all ~91.")
print("  so the CONFIGURATION never changes -> the corridor sees one constraint set, not 110.")