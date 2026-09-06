# Observed neutral ground configurations, Z=1..118 (NIST). Stored as deltas from Madelung where anomalous.
L={'s':0,'p':1,'d':2,'f':3,'g':4}
CAP=lambda l:2*(2*l+1)
MAD=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),(4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
def madelung(Z):
    c={};left=Z
    for (n,l) in MAD:
        if left<=0:break
        k=min(CAP(l),left);c[(n,l)]=k;left-=k
    return c
def parse(s):
    c={}
    for tok in s.split():
        n=int(tok[0]);l=L[tok[1]];q=int(tok[2:]);c[(n,l)]=q
    return c
# anomalies: full valence given, core assumed Madelung-filled below listed shells
ANOM={24:'3d5 4s1',29:'3d10 4s1',41:'4d4 5s1',42:'4d5 5s1',44:'4d7 5s1',45:'4d8 5s1',46:'4d10 5s0',47:'4d10 5s1',
57:'4f0 5d1 6s2',58:'4f1 5d1 6s2',64:'4f7 5d1 6s2',78:'5d9 6s1',79:'5d10 6s1',
89:'5f0 6d1 7s2',90:'5f0 6d2 7s2',91:'5f2 6d1 7s2',92:'5f3 6d1 7s2',93:'5f4 6d1 7s2',96:'5f7 6d1 7s2',
103:'5f14 6d0 7s2 7p1'}
def config(Z):
    c=madelung(Z)
    if Z in ANOM:
        over=parse(ANOM[Z])
        c.update(over)
        c={k:v for k,v in c.items() if v>0}
        assert sum(c.values())==Z,(Z,c)
    return c
if __name__=='__main__':
    for Z in [24,46,57,58,64,91,103,104]:
        print(Z,sorted(config(Z).items()))