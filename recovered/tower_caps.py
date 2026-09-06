# Tower Λ9 at four §7.4 cap settings, to verify the spin-rule four-cap figures.
# Base caps (n,e,l,k,f)=(3,3,1,3,1). The four settings the source names for Λ9
# spin imposition: 1,654 / 2,664 / 44,153 / 60,164.
def build_L9(NMAX,EMAX,LMAX,KMAX,FMAX,PHI=None):
    L8=[]
    for n in range(1,NMAX+1):
        for l in range(0,min(LMAX,n-1)+1):
            for k in range(1,min(KMAX,4*l+2)+1):
                for q in range(0,k+1):
                    for e in range(1,EMAX+1):
                        for f in range(0,min(FMAX,e-1)+1):
                            for g in range(0,min(4*f+2,q)+1):
                                for S2 in range(0,k+1):
                                    L8.append((n,l,k,q,e,f,g,S2))
    L9=[c+(s2p,) for c in L8 for s2p in range(0,c[6]+1)]
    return L8,L9