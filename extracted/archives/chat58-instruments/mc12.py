"""MC-12 — §11.1.1 binary / circuit.  Verify: J(Λ) and its covers; cell ↦ down-set-of-J
bijection; join = OR, meet = AND over all pairs; the 20 cover-implications cut 2^17 to
exactly 976; the implication circuit's depth; the 17 / 9.93 / 7.07 bit accounting."""
import itertools, math
from lam8 import L8

def leq(x, y): return all(a <= b for a, b in zip(x, y))
def join(x, y): return tuple(max(a, b) for a, b in zip(x, y))
def meet(x, y): return tuple(min(a, b) for a, b in zip(x, y))

cells = L8(); S = set(cells); n = len(cells)
rank = {c: sum(c) for c in cells}
bottom = min(cells, key=lambda c: rank[c])

# covers in Λ
below = {c: [] for c in cells}
for x in cells:
    for y in cells:
        if x != y and leq(x, y) and rank[y] == rank[x] + 1:
            below[y].append(x)
J = [c for c in cells if len(below[c]) == 1]           # join-irreducible: covers exactly one
print("|Λ| =", n, " bottom =", bottom, " |J(Λ)| =", len(J))

Jset = sorted(J, key=lambda c: (rank[c], c))
idx = {g: i for i, g in enumerate(Jset)}
# covers within J (the generator poset A.19)
Jcov = []
for a in Jset:
    for b in Jset:
        if a != b and leq(a, b):
            if not any(a != m != b and leq(a, m) and leq(m, b) for m in Jset):
                Jcov.append((idx[a], idx[b]))     # a < b covering: bit b set forces bit a set
print("covering relations in J(Λ):", len(Jcov))

# cell -> word
def word(x): return tuple(1 if leq(g, x) else 0 for g in Jset)
W = {c: word(c) for c in cells}
print("bijection cell↦word:", "OK" if len(set(W.values())) == n else "FAIL")

# join = OR, meet = AND over all unordered pairs
bad_or = bad_and = 0; npair = 0
for i in range(n):
    for j in range(i + 1, n):
        x, y = cells[i], cells[j]; npair += 1
        if W[join(x, y)] != tuple(a | b for a, b in zip(W[x], W[y])): bad_or += 1
        if W[meet(x, y)] != tuple(a & b for a, b in zip(W[x], W[y])): bad_and += 1
print(f"pairs {npair}: OR failures {bad_or}, AND failures {bad_and}")

# the 20 implications cut 2^17 to exactly 976
accept = 0; k17 = len(Jset)
for bits in itertools.product((0, 1), repeat=k17):
    if all(not (bits[b] and not bits[a]) for a, b in Jcov):
        accept += 1
print(f"words in {{0,1}}^{k17} = {2**k17}; accepted by the {len(Jcov)} implications = {accept}",
      "-> exactly Λ" if accept == n else "-> MISMATCH")
# and the accepted set is exactly the image of Λ
imgs = set(W.values())
sat = set(b for b in itertools.product((0, 1), repeat=k17)
          if all(not (b[y] and not b[x]) for x, y in Jcov))
print("accepted set == image of Λ:", sat == imgs)

# circuit depth: acceptance = AND over the 20 implication gates, each ¬b ∨ a i.e. one gate.
# monotone form: the circuit computes, per bit, forced-closure; depth = longest chain in J
# plus the AND tree.  Measure both: (a) height of the generator poset, (b) depth of the
# balanced AND tree over 20 gates, (c) their sum as the accept-circuit depth.
h = 0
for g in Jset:
    # longest descending chain of generators below g
    memo = {}
    def down(x):
        if x in memo: return memo[x]
        d = 1 + max([down(m) for m in Jset if m != x and leq(m, x)] or [0])
        memo[x] = d; return d
    h = max(h, down(g))
print("height of the generator poset J(Λ) (longest chain, in generators):", h)
and_depth = math.ceil(math.log2(len(Jcov)))
print(f"balanced AND tree over {len(Jcov)} gates: depth {and_depth}; "
      f"implication gate 1; total accept depth {and_depth + 1}")

# bit accounting
print(f"bits carried {k17}; bits needed log2({n}) = {math.log2(n):.2f}; surplus {k17 - math.log2(n):.2f}")
print(f"occupancy {n}/{2**k17} = {100*n/2**k17:.4f}%")
