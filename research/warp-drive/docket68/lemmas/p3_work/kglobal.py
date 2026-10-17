"""K over a whole Across solution (s from smin to 1), axis node excluded"""
import numpy as np, sys
P3 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/p3/"
sys.path.insert(0, P3); sys.path.insert(0, P3[:-3] + "p3e")
from across import Across
from p3curv import slice_K, NAMES, JS
fn, Ns, smin = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
A = Across(Ns, 20, smin); U = np.load(P3 + fn)
jet = {"": "", "_s": "_X", "_x": "_u", "_ss": "_XX", "_sx": "_Xu", "_xx": "_uu"}
n = A.n
Jall = {nm + j: A.D[jet[j]] @ U[m * n:(m + 1) * n] for m, nm in enumerate(NAMES) for j in JS}
xs = A.x
cols = [k for k in range(len(xs)) if xs[k] > 1e-9]
print("x nodes:", np.array2string(xs[cols][[0, 1, 3, 6, 10, -1]], precision=3))
for i in range(0, A.Ns + 1, max(1, A.Ns // 12)):
    sv = A.s[i]
    if abs(sv) < 1e-3 or sv > 0.97:
        continue
    idx = [i * (A.Nx + 1) + k for k in cols]
    J = {k: v[idx] for k, v in Jall.items()}
    K, g = slice_K(sv, xs[cols], J)
    print("s %+.3f  K at x = %s" % (sv, np.array2string(K[[0, 1, 3, 6, 10, -1]], precision=4, max_line_width=200)))
