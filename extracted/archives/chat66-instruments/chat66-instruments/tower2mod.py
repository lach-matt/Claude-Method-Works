# The tower Λ₈→Λ₁₃, reconstructed from §12.11.1 axis definitions (BUILD56 main).
# Coordinate order per stage:
#   n0 l1 k2 q3 e4 f5 g6 2S7 | 2S'8 v9 2Jc10 2K11 2J12
PHI = {1:3, 2:4, 3:5}   # φ̂(k) at §7.4 caps
FMAX = 1                # cap on f under §7.4

def L8():
    out=[]
    for n in range(1,4):
      for l in range(0,min(1,n-1)+1):
        for k in range(1,min(3,4*l+2)+1):
          for q in range(0,k+1):
            for e in range(1,4):
              for f in range(0,min(1,e-1)+1):
                for g in range(0,min(4*f+2,q)+1):
                  for S2 in range(0,k+1):
                    out.append((n,l,k,q,e,f,g,S2))
    return out

def L9():  return [c+(s2p,) for c in L8()  for s2p in range(0, c[6]+1)]
def L10(): return [c+(v,)   for c in L9()  for v   in range(c[8], c[6]+1)]
def L11(): return [c+(jc,)  for c in L10() for jc  in range(0, PHI[c[2]]+1)]
def L12(): return [c+(K2,)  for c in L11() for K2  in range(0, c[10]+2*FMAX+1)]
def L13(): return [c+(J2,)  for c in L12() for J2  in range(max(0,c[11]-1), c[11]+2)]

STAGES = {8:L8, 9:L9, 10:L10, 11:L11, 12:L12, 13:L13}

if False:
    for d in range(8,14):
        print(f'|Λ{d}| =', len(STAGES[d]()))
