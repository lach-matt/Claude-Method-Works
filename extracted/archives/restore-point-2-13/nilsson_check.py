#!/usr/bin/env python3
"""nilsson_check.py — verify the supplied transfermium orbitals internally.

A Nilsson label K^pi[N n_z Lambda] is NOT free notation. Four constraints bind
it, and all four are arithmetic:

    (1)  pi = (-1)^N                       parity is fixed by the shell
    (2)  K = Lambda +- 1/2                 K is Lambda plus or minus the spin
    (3)  n_perp = N - n_z >= Lambda        the perpendicular quanta must carry Lambda
    (4)  n_perp - Lambda is EVEN           and carry it with the right parity

Plus the parentage claim: the named spherical parent j-shell must lie in the
SAME oscillator shell N and carry the SAME parity.

Nothing here is a judgement about the physics. These are checks the notation
must satisfy to be notation at all.
"""
L = "spdfghijklm"   # index = orbital angular momentum
PARENT = {"g9/2": (4, 4.5), "d5/2": (2, 2.5), "j15/2": (7, 7.5), "i11/2": (6, 5.5),
          "i13/2": (6, 6.5), "f7/2": (3, 3.5), "h11/2": (5, 5.5), "h9/2": (5, 4.5)}

# (label, 2K, parity, N, n_z, Lambda, parent, species)
ORB = [
    ("1/2+[620]",  1, +1, 6, 2, 0, "g9/2",  "n"),
    ("9/2+[624]",  9, +1, 6, 2, 4, "j15/2", "n"),
    ("7/2+[624]",  7, +1, 6, 2, 4, "i11/2", "n"),
    ("1/2-[750]",  1, -1, 7, 5, 0, "j15/2", "n"),
    ("5/2+[622]",  5, +1, 6, 2, 2, "i11/2", "n"),
    ("11/2-[725]", 11, -1, 7, 2, 5, "j15/2", "n"),
    ("7/2+[633]",  7, +1, 6, 3, 3, "i13/2", "p"),
    ("1/2-[521]",  1, -1, 5, 2, 1, "f7/2",  "p"),
    ("7/2-[514]",  7, -1, 5, 1, 4, "h11/2", "p"),
    ("9/2-[505]",  9, -1, 5, 0, 5, "h9/2",  "p"),
    ("5/2+[642]",  5, +1, 6, 4, 2, "i13/2", "p"),
    ("3/2-[521]",  3, -1, 5, 2, 1, "f7/2",  "p"),
]

print("  THE FOUR INTERNAL CONSTRAINTS ON EVERY SUPPLIED ORBITAL\n")
print(f"    {'orbital':<12}{'sp':<4}{'parity':<9}{'K=L±½':<9}{'n⊥≥Λ':<8}"
      f"{'n⊥−Λ even':<12}{'parent shell':<14}verdict")
bad = []
for lab, K2, pi, N, nz, Lam, par, sp in ORB:
    c1 = pi == (-1) ** N
    c2 = K2 in (2 * Lam + 1, 2 * Lam - 1)
    npr = N - nz
    c3 = npr >= Lam
    c4 = (npr - Lam) % 2 == 0
    pl, pj = PARENT[par]
    c5 = (pl % 2) == (N % 2) and pl <= N
    ok = all((c1, c2, c3, c4))
    if not (ok and c5):
        bad.append((lab, par, c1, c2, c3, c4, c5))
    print(f"    {lab:<12}{sp:<4}{('OK' if c1 else 'FAIL'):<9}"
          f"{('OK' if c2 else 'FAIL'):<9}{('OK' if c3 else 'FAIL'):<8}"
          f"{('OK' if c4 else 'FAIL'):<12}"
          f"{(par + ' ' + ('OK' if c5 else '*** FAIL ***')):<14}"
          f"{'valid' if ok and c5 else 'PROBLEM'}")

print(f"\n  orbitals fully consistent: {len(ORB) - len(bad)} of {len(ORB)}")
for lab, par, *_ , c5 in bad:
    pl, pj = PARENT[par]
    print(f"\n  ** {lab} claims parent {par}: l = {pl}, so it lies in shell N = {pl}")
    print(f"     with parity {'+' if pl % 2 == 0 else '-'}, while the label says "
          f"N = {[o[3] for o in ORB if o[0] == lab][0]} "
          f"with parity {'+' if [o[2] for o in ORB if o[0]==lab][0] > 0 else '-'}.")
    print(f"     A POSITIVE-parity state cannot descend from an ODD-l parent. **")

print("\n  AND THE MASS NUMBERS, CHECKED AS A = Z + N:\n")
ISO = [("251Fm", 251, 100, 151), ("253No", 253, 102, 151), ("255No", 255, 102, 153),
       ("251Md", 251, 101, 150), ("255Lr", 255, 103, 152), ("257Rf", 257, 104, 153),
       ("254No", 254, 102, 152), ("256Rf", 256, 104, 152)]
bm = [i for i in ISO if i[1] != i[2] + i[3]]
for nm, A, Z, N in ISO:
    print(f"    {nm:<7}A = {A}   Z + N = {Z} + {N} = {Z+N}   "
          f"{'OK' if A == Z + N else '*** MISMATCH ***'}")
print(f"\n    mass-number failures: {len(bm)}")
