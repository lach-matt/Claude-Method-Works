import lam8
from itertools import product as prod
L8=lam8.L8(); S=set(L8)
def leq(a,b): return all(a[i]<=b[i] for i in range(8))
def isbox(x,y):
    for z in prod(*[range(x[i],y[i]+1) for i in range(8)]):
        if z not in S: return False
    return True
# EXACT over all comparable pairs (x<y): rate of box intervals
Ll=L8
allpairs=0; boxes=0
# this is O(976^2)=~950k pairs, each isbox check bounded -> fine
for a in Ll:
    for b in Ll:
        if a is b: continue
        if leq(a,b) and a!=b:
            allpairs+=1
            if isbox(a,b): boxes+=1
print(f"EXACT interval-is-box: {boxes}/{allpairs} = {100*boxes/allpairs:.1f}%")
# binding rates: for the constraints q<=k (idx3<=idx2), g<=q (idx6<=idx3), g<=4f+2 (idx6<=4*idx5+2)
# a constraint "binds across [x,y]" when the box-condition y_i<=f(x_j) fails, i.e. that constraint
# is the reason the interval isn't a box. Compute over comparable non-box intervals.
# constraint check per HANDOFF §12.9: for constraint i<=f(j): binds if NOT (y_i<=f(x_j))
def binds_qk(x,y):  return not (y[3] <= x[2])       # q<=k
def binds_gq(x,y):  return not (y[6] <= x[3])       # g<=q
def binds_gf(x,y):  return not (y[6] <= 4*x[5]+2)   # g<=4f+2
cqk=cgq=cgf=0
for a in Ll:
    for b in Ll:
        if a is b: continue
        if leq(a,b) and a!=b:
            if binds_qk(a,b): cqk+=1
            if binds_gq(a,b): cgq+=1
            if binds_gf(a,b): cgf+=1
print(f"binds g<=q : {100*cgq/allpairs:.1f}%  (claim 35.6%)")
print(f"binds q<=k : {100*cqk/allpairs:.1f}%  (claim 33.0%)")
print(f"binds g<=4f+2 : {100*cgf/allpairs:.1f}%  (claim 4.9%)")