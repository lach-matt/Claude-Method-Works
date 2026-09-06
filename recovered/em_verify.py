"""
Batch 7 EM-index verification (MC-36/37/38/39).
Verified-before-written: every figure recomputed on the rebuilt tower.

Coordinate order:
 Λ8:  n0 l1 k2 q3 e4 f5 g6 2S7
 Λ9:  + 2S'8
 ...  + v9 2Jc10 2K11 2J12
"""
from itertools import product as iproduct
from math import log2
import tower  # the validated instrument

# ---------- closure operator R (iterative join/meet sublattice closure) ----------
def R_closure(cells):
    """Iterative sublattice closure: close under componentwise meet(min) and join(max)
    to a fixpoint. This is the ℛ the record uses (MC-31 note: for non-tree sets the
    single double-projection pass can differ; iterate to fixpoint)."""
    S = set(cells)
    if not S:
        return S
    changed = True
    while changed:
        changed = False
        cur = list(S)
        new = set()
        for i in range(len(cur)):
            a = cur[i]
            for j in range(i, len(cur)):
                b = cur[j]
                mn = tuple(min(x,y) for x,y in zip(a,b))
                mx = tuple(max(x,y) for x,y in zip(a,b))
                if mn not in S: new.add(mn)
                if mx not in S: new.add(mx)
        if new:
            S |= new
            changed = True
    return S

def E(cells):
    s=set(cells)
    return len(R_closure(s)) - len(s)

# ---------- sanity: E(Λ_d)=0 at every stage (double check instrument+closure) ----------
def check_stage_closure():
    out={}
    for d in [8,9,10]:  # 8,9,10 are cheap; 11+ are large for O(n^2) closure
        cells=tower.STAGES[d]()
        out[d]=E(cells)
    return out

# ---------- EM maps ----------
# Δℓ = f - l  (target subshell f=index5, source l=index1), defined at Λ8
# ΔS = 2S' - 2S (2S'=index8, 2S=index7), defined at Λ9
def dl(c):  return c[5]-c[1]
def dS(c):  return c[8]-c[7]

# multipole from (Δℓ, parity): Δℓ=0→M1, 1→E1, 2→E2, 3→E3 (lowest whose parity matches)
# parity of the transition = parity of Δℓ; E-type when Δℓ odd, M1 when Δℓ even (for the low orders here)
def multipole(c):
    d=abs(dl(c))
    return {0:'M1',1:'E1',2:'E2',3:'E3'}.get(d, f'>{d}')

if __name__=='__main__':
    print('stage closure E (expect 0):', check_stage_closure())

    L9=tower.L9()
    print('|Λ9| =', len(L9))

    # ---- image rectangle: (multipole, ΔS) ----
    from collections import Counter
    img=Counter()
    for c in L9:
        img[(multipole(c), dS(c))]+=1
    # print E1 and M1 rows across ΔS=0..3
    print('\\nimage (multipole, ΔS):')
    for mp in ['E1','M1','E2','E3']:
        row=[img.get((mp,s),0) for s in range(0,4)]
        if any(row): print(f'  {mp}:', row)
    # E1 cells with ΔS != 0 (intercombination count)
    e1_inter=sum(v for (mp,s),v in img.items() if mp=='E1' and s!=0)
    print('E1 with ΔS!=0 (intercombination):', e1_inter)

    # image cell count + E of the image
    image_cells=set((({'M1':0,'E1':1,'E2':2,'E3':3}[multipole(c)]), dS(c)) for c in L9)
    print('image distinct cells:', len(image_cells), '| E(image)=', E(image_cells))

    # ---- spin imposition σ^{-1}({0}) : keep cells with ΔS=0 ----
    spin0=[c for c in L9 if dS(c)==0]
    print('\\nspin σ^{-1}({0}) on Λ9: kept', len(spin0), '| E=', E(spin0))

    # ---- parity imposition on Λ8: δ^{-1}({-1,+1}) : keep |Δℓ|=1 ----
    L8=tower.L8()
    par=[c for c in L8 if dl(c) in (-1,1)]
    print('parity δ^{-1}({-1,+1}) on Λ8: kept', len(par), '| E=', E(par))
