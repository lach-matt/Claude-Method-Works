import time
from rop import *
t0=time.time(); U=box((2,2,2,2)); C=moore(U)
print('(2,2,2,2) |U| 16 closed incl ∅',len(C),'excl ∅',len([c for c in C if c]),'E=2^16-|Cl|',2**16-len(C),'time %.0fs'%(time.time()-t0))
print('rates incl ∅ (∩,∪): %.1f %.1f'%rates(C,False)[2:],'| excl ∅: %.1f %.1f'%rates(C,True)[2:])
import pickle; pickle.dump(C,open('cl16.pkl','wb'))