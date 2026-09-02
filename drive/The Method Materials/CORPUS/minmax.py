# Sweep C instrument (chat 67): is Λ8 × h closed, i.e. is h a lattice homomorphism on the rebuilt Λ8?
# Tests projections, constants, min/max against constants, min/max/sum/product/difference of two coordinates,
# over ALL 976² ordered pairs; and φ̂ against realised max 2Jc per k on Λ11. Requires tower-2.py beside it.
import numpy as np, itertools, importlib.util
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
X=np.array(tw.L8(),dtype=np.int16); n=len(X); J=np.maximum(X[:,None,:],X[None,:,:]); M=np.minimum(X[:,None,:],X[None,:,:])
S=set(map(tuple,X.tolist())); print('|Λ8|',n,'E(Λ8)=0:',len(set(map(tuple,J.reshape(-1,8).tolist()))|S)==len(S) and len(set(map(tuple,M.reshape(-1,8).tolist()))|S)==len(S))
names='n l k q e f g S'.split()
def hom(h):
    hx=h(X); hJ=h(J.reshape(-1,8)).reshape(n,n); hM=h(M.reshape(-1,8)).reshape(n,n)
    return np.array_equal(hJ,np.maximum(hx[:,None],hx[None,:])) and np.array_equal(hM,np.minimum(hx[:,None],hx[None,:]))
print('projections',[hom(lambda A,i=i:A[:,i]) for i in range(8)]); print('constants',[hom(lambda A,c=c:np.full(len(A),c)) for c in (0,1,2)])
print('min(x,c)',sum(hom(lambda A,i=i,c=c:np.minimum(A[:,i],c)) for i in range(8) for c in (1,2)),'of 16; max(x,c)',sum(hom(lambda A,i=i,c=c:np.maximum(A[:,i],c)) for i in range(8) for c in (1,2)),'of 16')
for lab,f in [('min',np.minimum),('max',np.maximum),('sum',lambda a,b:a+b),('product',lambda a,b:a*b),('difference',lambda a,b:a-b)]:
    ok=[(names[i],names[j]) for i,j in itertools.combinations(range(8),2) if hom(lambda A,i=i,j=j:f(A[:,i],A[:,j]))]
    print(lab,'closed',len(ok),'of 28',ok)
L11=np.array(tw.L11(),dtype=np.int16); print('φ̂',tw.PHI,'realised',{k:int(L11[L11[:,2]==k][:,10].max()) for k in (1,2,3)})
