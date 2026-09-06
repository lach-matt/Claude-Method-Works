from itertools import product
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
def L9():
    return [x+(s,) for x in L8() for s in range(0,x[6]+1)]
if __name__=='__main__':
    print('|Λ8|=',len(L8()),' |Λ9|=',len(L9()))