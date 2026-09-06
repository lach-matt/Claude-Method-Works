from itertools import combinations

# From paper 6.3: physical iff 2S = k mod 2 and 2S <= min(k, 2(2l+1)-k)
# 6.4 offset: m = (k-2S)/2  =>  2S = k-2m
# Bounds on m:  2S>=0 -> m <= k/2 ;  2S<=k -> m>=0 ;  2S<=2(2l+1)-k -> m >= k-(2l+1)
def flo(k,l): return max(0, k-(2*l+1))
def cei(k):   return k//2

def build(LMAX):
    S=[]
    for l in range(LMAX+1):
        for k in range(1, 2*(2*l+1)+1):
            for m in range(flo(k,l), cei(k)+1):
                S.append((l,k,m))
    return S

def jn(a,b): return tuple(max(x,y) for x,y in zip(a,b))
def mt(a,b): return tuple(min(x,y) for x,y in zip(a,b))

for LMAX in (2,3):
    S=build(LMAX); Sset=set(S)
    jf=mf=0
    jcause={'k_le_2(2l+1)':0,'m_ge_flo':0,'m_le_cei':0,'other':0}
    mcause=dict(jcause)
    def why(c):
        l,k,m=c
        if k>2*(2*l+1): return 'k_le_2(2l+1)'
        if m<flo(k,l):  return 'm_ge_flo'
        if m>cei(k):    return 'm_le_cei'
        return 'other'
    for a,b in combinations(S,2):
        j=jn(a,b); mm=mt(a,b)
        if j not in Sset:  jf+=1; jcause[why(j)]+=1
        if mm not in Sset: mf+=1; mcause[why(mm)]+=1
    print(f"LMAX={LMAX}  |S|={len(S)}  pairs={len(S)*(len(S)-1)//2}")
    print(f"  join failures {jf}   {jcause}")
    print(f"  meet failures {mf}   {mcause}")
    print()