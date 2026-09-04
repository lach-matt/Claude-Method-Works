import random, math
random.seed(7)

# ---- 4. THE SEQUENCE AS AN INDEX -----------------------------------------
# The (chr,pos) index carries POSITIONS. It does not carry BASES.
# Adjoin the base axis: cells are (p, b), b in {A,C,G,T} -> {0,1,2,3}.
# The genome is the GRAPH OF A FUNCTION p -> b_p : exactly one base per site.

def R_twoaxis(cells, nmax, bmax):
    """closure under coordinatewise join+meet, computed to fixed point"""
    S = set(cells)
    while True:
        new = set()
        for x in S:
            for y in S:
                new.add((max(x[0],y[0]), max(x[1],y[1])))
                new.add((min(x[0],y[0]), min(x[1],y[1])))
        if new <= S: return S
        S |= new

def E_sequence(seq):
    cells = [(i, b) for i, b in enumerate(seq)]
    return len(R_twoaxis(cells, len(seq), 4)) - len(cells)

print("=== 4. E OF THE SEQUENCE CONTENT ===")
for N in (50, 200, 800):
    seq = [random.randrange(4) for _ in range(N)]
    E = E_sequence(seq)
    print(f"  N={N:4d}  E={E:5d}   E/N = {E/N:.4f}   (|S|-1 = 3)")

# monotone (sorted) sequence -- the only closed case
for N in (50, 200, 800):
    seq = sorted(random.randrange(4) for _ in range(N))
    print(f"  N={N:4d}  E={E_sequence(seq):5d}  <-- sorted sequence (AAA..CCC..GGG..TTT)")

# ---- the identity, extrapolated ------------------------------------------
N_gen = 3_088_269_832
E_gen = 3 * N_gen
bits  = N_gen * math.log2(3 + 1)
print(f"\n  human genome: E = 3N = {E_gen:,}")
print(f"  description length = N*log2(E/N + 1) = {bits:,.0f} bits = {bits/8/1e6:,.0f} MB")

# ---- 5. THE TWO BRANCHES, AND WHERE THEY CROSS (sec 16.9.2) ---------------
print("\n=== 5. THE k-MER CROSSING ===")
N = N_gen
print("   k   4^k (alphabet cap)      N-k+1 (length cap)     binding")
kstar = None
for k in range(12, 21):
    a, b = 4**k, N - k + 1
    binding = "alphabet" if a < b else "length"
    if a >= b and kstar is None: kstar = k
    print(f"  {k:3d}   {a:>22,}   {b:>19,}   {binding}")
print(f"\n  branches cross at k* = log_4(N) = {math.log(N,4):.3f}")
print(f"  first integer k where the alphabet cap ceases to bind: {kstar}")

# ---- 6. DOES THE RELABELLED INDEX CARRY ITS OWN BOUNDS? (S3, sec 10.2) ----
print("\n=== 6. S3 -- ARE THE BOUNDS RECOVERABLE FROM THE CELLS? ===")
Ltest = [10, 7, 13, 4]                      # unsorted toy 'chromosomes'
X = {(c,p) for c,l in enumerate(Ltest) for p in range(1, l+1)}
recovered = [max(p for (cc,p) in X if cc==c) for c in range(len(Ltest))]
print(f"  declared bounds : {Ltest}")
print(f"  recovered by max: {recovered}   S3 holds: {recovered==Ltest}")
RX = R_twoaxis(X, None, None)
rec_after = [max(p for (cc,p) in RX if cc==c) for c in range(len(Ltest))]
print(f"  after applying R: {rec_after}   <-- closure OVERWROTE the true bounds")
print(f"  E = {len(RX)-len(X)}")