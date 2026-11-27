import sys, numpy as np
sys.path.insert(0, '/home/user/Claude-Method-Works/research/warp-drive/paper/reader/solver')
import bsio
SP='/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/bsolv/s2A_dd/'
J = bsio.read_jets(SP+'s2A.jets')
xs, A = J[0]          # side 0 (u >= -10): per column (9, nA, 5, NX, 2)
print('columns', len(xs), 'array', A.shape)
NX = A.shape[4]; M = NX-1
# x-Chebyshev transform (DCT-I) of values at x_k = cos(pi k/M)
k = np.arange(NX); C = np.cos(np.pi*np.outer(k,k)/M)*2.0/M; C[:,0]*=0.5; C[:,-1]*=0.5; C[0,:]*=0.5; C[-1,:]*=0.5
FN='RmnWs'
for col in [0, 9, 19, 29]:
    xi = xs[col][:,0]; a = 0
    u = -1 + np.sinh(xi[a])/500
    for f in [1,2,0,4]:
        v = A[col,:,a,f,:,0] + A[col,:,a,f,:,1]     # (9 orders j=0..8 of G, i.e. F order 4+j) x NX
        c = v @ C.T                                   # Chebyshev coefficients in x
        mx = np.abs(c).max(axis=1)
        low = np.abs(c[:, :4]).max(axis=1)
        rat = [mx[j+1]/mx[j] if mx[j] > 0 else 0 for j in range(8)]
        print('col %2d u=%7.3f field %s  max_k|a_j| j=0..8: %s' % (col, u, FN[f], ' '.join('%.1e' % q for q in mx)))
        print('                       ratios |a_(j+1)|/|a_j|: %s ; apparent r = %.2f' % (' '.join('%.2f' % q for q in rat), (mx[2]/mx[8])**(1/6) if mx[8] > 0 else 0))
