"""cellcut.py -- s28 ruling D. Finite-volume fraction of each log-mesh cell where eps_c(x) < 0, eps_c piecewise linear between nodes.
Replaces the nodal theta(-eps_c) in v_gbz when SUBCELL=1. Exact for piecewise-linear eps; continuous in every node value; no constant.
frac_j = [ f_half(eps_j, eps_{j-1}) + f_half(eps_j, eps_{j+1}) ] / 2, where f_half(a,b) = measure of s in [0,1] with (a + s*(b-a)/2) < 0
(the half-cell from node j toward its neighbour, along which eps runs linearly from a to the midpoint value (a+b)/2). Endpoints: one-sided."""
import os
import numpy as np
SUBCELL = os.environ.get("SUBCELL", "0") == "1"

def _half(a, b):
    m = 0.5*(a+b)                                  # eps at the cell face
    out = np.zeros_like(a)
    both_neg = (a < 0) & (m < 0); out[both_neg] = 1.0
    cross = (a < 0) != (m < 0)                     # root inside the half-cell
    with np.errstate(divide='ignore', invalid='ignore'):
        s = np.where(cross, a/(a-m), 0.0)          # s in (0,1): eps=0 at s
    out = np.where(cross & (a < 0), s, out)         # negative near the node, positive at the face
    out = np.where(cross & (a >= 0), 1.0-s, out)    # positive near the node, negative at the face
    return out

def frac_neg(eps):
    """in-cell fraction of eps<0 for a 1-D array on a uniform mesh."""
    eps = np.asarray(eps, float)
    left = np.empty_like(eps); right = np.empty_like(eps)
    right[:-1] = _half(eps[:-1], eps[1:]); right[-1] = (eps[-1] < 0)
    left[1:] = _half(eps[1:], eps[:-1]);   left[0] = (eps[0] < 0)
    return 0.5*(left+right)
