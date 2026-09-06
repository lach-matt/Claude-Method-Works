# em36.py — verification instrument for OWED row 36 (§12.11.8 imposition criterion)
# Coordinates: n0 l1 k2 q3 e4 f5 g6 2S7 | 2S'8
import itertools, sys
from collections import Counter

def L8c(N=3, E=3, Lm=1, Km=3, Fm=1):
    out = []
    for n in range(1, N+1):
        for l in range(0, min(Lm, n-1)+1):
            for k in range(1, min(Km, 4*l+2)+1):
                for q in range(0, k+1):
                    for e in range(1, E+1):
                        for f in range(0, min(Fm, e-1)+1):
                            for g in range(0, min(4*f+2, q)+1):
                                for S2 in range(0, k+1):
                                    out.append((n, l, k, q, e, f, g, S2))
    return out

def L9c(caps=(3, 3, 1, 3, 1)):
    return [c+(s,) for c in L8c(*caps) for s in range(0, c[6]+1)]

def join(a, b): return tuple(max(x, y) for x, y in zip(a, b))
def meet(a, b): return tuple(min(x, y) for x, y in zip(a, b))

def sublattice_closure(S):
    """Iterative join/meet closure to a fixed point (the E convention for non-tree sets)."""
    S = set(S); rounds = 0
    while True:
        rounds += 1
        cur = list(S); new = set()
        for i in range(len(cur)):
            a = cur[i]
            for j in range(i+1, len(cur)):
                b = cur[j]
                jn = join(a, b); mt = meet(a, b)
                if jn not in S: new.add(jn)
                if mt not in S: new.add(mt)
        if not new: return S, rounds
        S |= new

def one_pass_closure(S):
    """Single pass: S ∪ {joins, meets of pairs of S} (no iteration) — for comparison only."""
    S = set(S); new = set()
    cur = list(S)
    for i in range(len(cur)):
        for j in range(i+1, len(cur)):
            new.add(join(cur[i], cur[j])); new.add(meet(cur[i], cur[j]))
    return S | new

def dl(c):  return c[5] - c[1]          # Δℓ = f − ℓ
def ds(c):  return c[8] - c[7]          # ΔS (doubled) = 2S′ − 2S
def multipole(c):
    m = abs(dl(c))
    return {0: 'M1', 1: 'E1', 2: 'E2', 3: 'E3'}[m]

if __name__ == '__main__':
    part = sys.argv[1] if len(sys.argv) > 1 else 'A'
    if part == 'A':
        # --- validate builder against the book's cap table (main L3218-3221) ---
        for caps, exp in [((3,3,1,3,1),1654), ((4,4,1,6,1),19433), ((4,4,2,6,2),44153), ((5,5,2,6,2),83543)]:
            n = len(L9c(caps)); print('caps', caps, '|Λ9| =', n, 'expected', exp, 'PASS' if n == exp else 'FAIL')
        L9 = L9c()
        comp = [c for c in L9 if c[6] >= 1]   # target is a legal source ⇔ g ≥ 1 (k ≥ 1 for a source)
        print('composable (target legal source, g≥1):', len(comp), 'expected 1169')
        # --- image table on (multipole, ΔS) ---
        for label, f in [('signed ΔS', ds), ('|ΔS|', lambda c: abs(ds(c)))]:
            ct = Counter((multipole(c), f(c)) for c in L9)
            keys = sorted(set(k[1] for k in ct))
            print(f'--- image on (multipole, {label}) ---   columns:', keys)
            for m in ['E1', 'M1']:
                print(m, [ct.get((m, k), 0) for k in keys], 'row sum', sum(ct.get((m, k), 0) for k in keys))
            print('distinct image cells:', len(ct))
        E1_dS_nonzero = sum(1 for c in L9 if multipole(c) == 'E1' and ds(c) != 0)
        print('E1 with ΔS≠0 (intercombination):', E1_dS_nonzero, 'expected 576')
        # --- range of δ and σ, and the two rule sets ---
        print('range(δ) =', sorted(set(dl(c) for c in L9)), ' range(σ) =', sorted(set(ds(c) for c in L9)))
        spin = [c for c in L9 if ds(c) == 0]
        par  = [c for c in L9 if abs(dl(c)) == 1]
        print('spin rule σ⁻¹({0}):', len(spin), 'expected 526;  parity rule δ⁻¹({−1,+1}):', len(par), 'expected 840')
    elif part == 'B':
        L9 = L9c()
        spin = [c for c in L9 if ds(c) == 0]
        par  = [c for c in L9 if abs(dl(c)) == 1]
        cs, r = sublattice_closure(spin); print('spin rule: E(iterative) =', len(cs)-len(spin), 'rounds', r, 'expected 0')
        cp, r = sublattice_closure(par);  print('parity rule: E(iterative) =', len(cp)-len(par), 'rounds', r, 'expected 750')
        op = one_pass_closure(par);       print('parity rule: E(one-pass)  =', len(op)-len(par))
        # closure stays inside Λ9?
        S9 = set(L9); print('parity-rule closure ⊆ Λ9:', cp <= S9, '; restored cells with Δℓ=0:', sum(1 for c in cp-set(par) if dl(c)==0))
        # interval property check on all pairs of Λ9 (δ and σ)
        viol = 0; pairs = 0
        for i in range(len(L9)):
            a = L9[i]
            for j in range(i+1, len(L9)):
                b = L9[j]; pairs += 1
                for fn in (dl, ds):
                    lo, hi = min(fn(a), fn(b)), max(fn(a), fn(b))
                    if not (lo <= fn(join(a, b)) <= hi and lo <= fn(meet(a, b)) <= hi): viol += 1
        print('interval property: pairs', pairs, '(expected 1,367,031) violations', viol)
    elif part == 'C':
        # scan caps for |Λ9| = 2,664 and 60,164; and image at (5,5,3,10,3)
        hits = []
        for N in range(3, 7):
            for E in range(3, 7):
                for Lm in range(1, 4):
                    for Km in range(3, 13):
                        for Fm in range(1, 4):
                            n = len(L9c((N, E, Lm, Km, Fm)))
                            if n in (2664, 60164): hits.append(((N, E, Lm, Km, Fm), n))
        print('cap hits:', hits)
        L9 = L9c((5, 5, 3, 10, 3))
        ct = Counter((abs(dl(c)), abs(ds(c))) for c in L9)
        print('caps (5,5,3,10,3): |Λ9| =', len(L9), ' image cells', len(ct), ' |Δℓ| values', sorted(set(k[0] for k in ct)), ' |ΔS| values', sorted(set(k[1] for k in ct)))
