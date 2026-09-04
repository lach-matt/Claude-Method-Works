"""
Lach Cylinder method applied to genomic indices.
E(X) = |R(X)| - |X|, R = closure under coordinatewise join and meet.
"""

# ---- PROVENANCE NOTE (B.2.11) --------------------------------------------
# GRCh38 chromInfo lengths below are RECALLED, not retrieved this session.
# The fetch of the Piovesan et al. 2019 Table 2 returned the article body
# without the table. This is a STATED GAP in the B.2.10 sense, not a silent
# default. Every STRUCTURAL result below is tested for dependence on the
# exact values (see test_stability).
# --------------------------------------------------------------------------

L = {  # GRCh38 primary assembly, bp
 1:248956422, 2:242193529, 3:198295559, 4:190214555, 5:181538259,
 6:170805979, 7:159345973, 8:145138636, 9:138394717, 10:133797422,
 11:135086622,12:133275309,13:114364328,14:107043718,15:101991189,
 16:90338345, 17:83257441, 18:80373285, 19:58617616, 20:64444167,
 21:46709983, 22:50818468, 23:156040895, 24:57227415}   # 23=X, 24=Y
NAME = {23:'X',24:'Y'}
def nm(c): return NAME.get(c,str(c))

order = sorted(L)                     # the conventional labelling 1..22,X,Y
lens  = [L[c] for c in order]
N_occ = sum(lens)

# ---- 1. R(X) for the (chromosome, position) index -------------------------
# Cells: (c, p) with 1 <= p <= L(c).  Join = (max c, max p), meet = (min,min).
# By the running-maxima characterisation (B.2.15.2 / sec 23.3):
#   R(X) = {(c,p) : p <= M(c)},  M(c) = max_{c' <= c} L(c')
def closure_size(lengths):
    M, run = [], 0
    for x in lengths:
        run = max(run, x); M.append(run)
    return sum(M), M

R_size, M = closure_size(lens)
E_pos = R_size - N_occ

print("=== 1. THE (chromosome, position) INDEX ===")
print(f"|X|      = {N_occ:,}   (occupied cells = assembled bases)")
print(f"|R(X)|   = {R_size:,}")
print(f"E(X)     = {E_pos:,}")
print(f"E/|X|    = {E_pos/N_occ:.4f}")
print(f"running max is constant at chr1 length: {len(set(M))==1}")

# ---- 2. Direct verification that closure fails (show the test can fail, B.2.19.6)
def is_closed(lengths):
    """brute-force join/meet closure test over all pairs of extreme cells"""
    n = len(lengths); bad = []
    for i in range(n):
        for j in range(n):
            # extreme cell of i joined with extreme cell of j
            c, p = max(i,j), max(lengths[i], lengths[j])
            if p > lengths[c]:
                bad.append((i,j,c,p,lengths[c]))
    return bad

bad = is_closed(lens)
print(f"\njoin-closure violations over {len(lens)**2} ordered pairs: {len(bad)}")
print("first three witnesses (0-indexed chrom slots):")
for w in bad[:3]:
    i,j,c,p,cap = w
    print(f"   chr{nm(order[i])} v chr{nm(order[j])} -> (chr{nm(order[c])}, {p:,}) but L=({cap:,})")

# --- the test must be shown capable of returning clean:
sorted_lens = sorted(lens)
print(f"violations after sorting by length: {len(is_closed(sorted_lens))}  <-- test can return 0")

# ---- 3. E after the relabelling ------------------------------------------
R2, _ = closure_size(sorted_lens)
print(f"\n=== 2. AFTER SORTING CHROMOSOMES BY LENGTH ===")
print(f"|X| = {sum(sorted_lens):,}   |R(X)| = {R2:,}   E = {R2-sum(sorted_lens):,}")

# ---- 4. cost of the repair: inversions in the conventional labelling ------
inv = [(order[i],order[j]) for i in range(len(lens)) for j in range(i+1,len(lens))
       if lens[i] < lens[j]]
aut = [p for p in inv if p[0]<=22 and p[1]<=22]
print(f"\n=== 3. REORDERABILITY (sec 23.3) ===")
print(f"total inversions in the conventional order: {len(inv)}")
print(f"inversions among the 22 autosomes only:     {len(aut)}")
print(f"autosome inversions: {[(nm(a),nm(b)) for a,b in aut]}")

# ---- 5. stability of the structural claim under perturbed lengths --------
import random
def test_stability(trials=2000):
    random.seed(11); fails=0
    for _ in range(trials):
        pert = [int(x*random.uniform(0.90,1.10)) for x in lens]
        if len(is_closed(pert))==0: fails+=1
    return fails
print(f"\nstability: closed under +-10% length perturbation in "
      f"{test_stability()} of 2000 trials  (structural claim independent of exact bp)")