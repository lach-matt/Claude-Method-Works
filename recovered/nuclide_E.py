# E(X) for a 2-coordinate index (Z,N) under the recovery operator A.R:
#   Ahat_Z = values of Z present; Ahat_N = values of N present
#   phi recovers monotone staircase: for the (<=,<=) corner, N <= maxN_present_at_or_below... 
#   but the operator is: keep x in box with x_i <= phi_ij(x_j) for the recovered envelope.
# For a down-set-style staircase the recovered bound is the monotone upper envelope.
# Implement E as |R(X)| - |X| where R(X) = closure to the (<=,<=) staircase corner
# (Deville connected-row-convex closure), which is the operator the compendium uses (A.staircls).

def env_upper(X):
    # X: set of (Z,N). Recover the monotone staircase upper envelope in BOTH directions,
    # take R(X) = { (z,n) in box : n <= maxN(z') for the envelope, z <= maxZ(n') } 
    # Concretely the (<=,<=) closure: (z,n) in R(X) iff exists (z1,n1),(z2,n2) in X with
    # z<=z1, n<=n1 ... -> simplest faithful form: R(X) = down-closure-then-fill under the
    # componentwise max staircase. Use: for each z, Nmax[z]; R = {(z,n): n<=max over z'>=? } 
    # The correct A.R for connected row-convex: (z,n) in R iff n <= f(z) and z <= g(n) where
    # f(z)=max{n' : (z,n') in X or implied}. We use the join/meet closure to fixpoint instead,
    # which is the operator used elsewhere this session (iterative, exact).
    S=set(X)
    changed=True
    while changed:
        changed=False
        new=set()
        L=list(S)
        for i in range(len(L)):
            for j in range(len(L)):
                a=L[i]; b=L[j]
                jn=(max(a[0],b[0]), max(a[1],b[1]))  # join
                mt=(min(a[0],b[0]), min(a[1],b[1]))  # meet
                if jn not in S: new.add(jn)
                if mt not in S: new.add(mt)
        if new:
            S|=new; changed=True
    return S

# Sanity: a full rectangle closes to itself (E=0). A chart missing interior/corner cells gains them.
# Test on a tiny synthetic "chart": a staircase with one hole.
test={(0,0),(1,0),(1,1),(0,1)}  # full 2x2 box -> E=0
R=env_upper(test); print("2x2 box: |X|=%d |R|=%d E=%d"%(len(test),len(R),len(R)-len(test)))
# L-shape missing corner (1,1): join of (1,0),(0,1) = (1,1) -> restored, E=1
Lsh={(0,0),(1,0),(0,1)}
R=env_upper(Lsh); print("L missing (1,1): |X|=%d |R|=%d E=%d added=%s"%(len(Lsh),len(R),len(R)-len(Lsh),R-Lsh))