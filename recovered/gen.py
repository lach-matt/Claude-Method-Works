import itertools
def build(capn, cape, capl, capk, capf, s_floor, s_parity):
    cells=[]
    for n in range(1,capn+1):
     for l in range(0,min(capl,n-1)+1):
      for k in range(1,min(capk,4*l+2)+1):
       for q in range(0,k+1):
        for e in range(1,cape+1):
         for f in range(0,min(capf,e-1)+1):
          for g in range(0,min(q,4*f+2)+1):
           lo = s_floor(k)
           for S2 in range(lo,k+1):
            if s_parity and (S2-k)%2!=0: continue
            cells.append((n,l,k,q,e,f,g,S2))
    return cells
CAPS=(3,3,1,3,1)
variants = {
 "2S in [0..k], no parity": (lambda k:0, False),
 "2S in [1..k], no parity": (lambda k:1, False),
 "2S in [k%2..k], parity":  (lambda k:k%2, True),
}
for name,(fl,par) in variants.items():
    X=build(*CAPS,fl,par)
    print(f"{name}: {len(X)} cells")