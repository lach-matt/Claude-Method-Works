from tower2mod import L8
def ext(spcap=None):
    out=[]
    for c in L8():
        n,l,k,q,e,f,g,S2=c
        for G in range(g,4*f+2+1):
            for sp in range(0,G+1):
                if spcap is None or sp<=spcap: out.append(c+(sp,G))
    return out