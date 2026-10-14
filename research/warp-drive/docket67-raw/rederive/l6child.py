# child of cauchy-schwarz-lagrange-identity.py (L6): future-cone closure in R^{1,dim}, z3 nlsat
import z3,time,sys
dim=int(sys.argv[1]); mode=sys.argv[2]
T1,T2=z3.Reals('T1 T2');u=z3.RealVector('u',dim);v=z3.RealVector('v',dim)
sq = lambda w: z3.Sum([c * c for c in w]) if dim > 1 else w[0] * w[0]
s=z3.Then('simplify','qfnra-nlsat').solver()
s.set('timeout',int(sys.argv[3]) if len(sys.argv)>3 else 400000)
if mode=='ff':
    s.add(T1>=0,T2>=0,T1*T1>=sq(u),T2*T2>=sq(v))
else:
    s.add(T1>=0,T2<=0,T1*T1>=sq(u),T2*T2>=sq(v))
w=[u[k]+v[k] for k in range(dim)]
s.add((T1+T2)*(T1+T2)<sq(w))
t=time.time();r=s.check();print(r)
sys.stderr.write("%s %s %.1fs\n"%(r,s.reason_unknown() if r==z3.unknown else '',time.time()-t))
