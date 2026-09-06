#!/usr/bin/env python3
"""v5d.py -- S96: assemble the V^{N-1} object for v5b.py. DECLARED construction (F96.1 remedy; tested by reproducing the filed row-89 E2):
  virtual spectra (w_l, F_l) = the CORE (cfg(Z-1)) V^N operator's roots (pack96/v5c-Z-core-lL.npz, L=0..lmax);
  occupied P, eps = the SIDE's own sealed solve (pack96/v5c-Z-SIDE-occ.npz). Writes pack96/v5d-Z-SIDE.npz in the v5a npz layout.
usage: v5d.py Z SIDE [--lmax 6]"""
import sys,os,numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); Z=int(sys.argv[1]); side=sys.argv[2]
lmax=int(sys.argv[sys.argv.index('--lmax')+1]) if '--lmax' in sys.argv else 6
O=np.load(os.path.join(HERE,'v5c-%d-%s-occ.npz'%(Z,side))); out={k:O[k] for k in O.files}
for l in range(lmax+1):
    S=np.load(os.path.join(HERE,'v5c-%d-core-l%d.npz'%(Z,l))); out['w%d'%l]=S['w']; out['F%d'%l]=S['F']
out['Eref']=0.0
np.savez(os.path.join(HERE,'v5d-%d-%s.npz'%(Z,side)),**out); print("wrote v5d-%d-%s.npz"%(Z,side))