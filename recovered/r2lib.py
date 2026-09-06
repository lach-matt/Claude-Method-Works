# r2lib.py — shared instrument library for Phase R2 (chat 74). Ruling 2 of chat 74.
# Every function below is lifted VERBATIM (by AST source segment) from the instrument named in its
# provenance comment, except two marked parameterisations: mi() takes N = len(xs) instead of the module
# constant, and ci_sets() takes the index X as its first argument. Instruments import this module by path:
#   import importlib.util, os; H=os.path.dirname(os.path.abspath(__file__))
#   s=importlib.util.spec_from_file_location('r2lib', os.path.join(H,'r2lib.py')); r2lib=importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
# and load the tower with r2lib.load_tower() (tower-2.py by path; never copied).
import os, sys, math, itertools, importlib.util, collections, hashlib
from collections import Counter, defaultdict
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))

def load_tower():
    s = importlib.util.spec_from_file_location('tower2', os.path.join(H, 'tower-2.py')); T = importlib.util.module_from_spec(s); s.loader.exec_module(T); return T

def read_member(name, binary=False):
    return open(os.path.join(H, name), 'rb').read() if binary else open(os.path.join(H, name), encoding='utf-8').read()

def md5(b):
    return hashlib.md5(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()

def lam9p(L9):
    """Λ₉′ = Λ₉ ∩ {2S′ ≤ 2f+1} (r2-ch12i.py)."""
    return [c for c in L9 if c[8] <= 2 * c[5] + 1]

def gG_index(T):
    """The 13,775-cell (g, G) index of MC L1306 (r2-ch12k.py): Λ₈ cells extended by G ∈ [g, 4f+2] and 2S′ ∈ [0, G]."""
    n_, l_, k_, q_, e_, f_, g_, S_, G_, Sp_ = range(10)
    X = [c + (G, S2p) for c in T.L8() for G in range(c[g_], 4 * c[f_] + 2 + 1) for S2p in range(0, G + 1)]
    return X

# ---- Λ₉ / Λ₉′ constants (r2-ch12i.py) ----
NAMES = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S', '2S′']
SRC, TGT, Q = [0, 1, 2, 7], [4, 5, 6, 8], 3
EDGES9 = [(0, 1), (1, 2), (2, 3), (2, 7), (4, 5), (5, 6), (3, 6), (6, 8)]
EDGES9P = EDGES9 + [(5, 8)]

# ---- (g, G) index constants (r2-ch12k.py) ----
n_, l_, k_, q_, e_, f_, g_, S_, G_, Sp_ = range(10)
NAMES10 = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S', 'G', '2S′']
ARROWS = {'shell': (n_, e_), 'subshell': (l_, f_), 'occupancy': (k_, G_), 'spin': (S_, Sp_)}
DIST = {('shell', 'subshell'): 1, ('subshell', 'occupancy'): 1, ('occupancy', 'spin'): 1, ('subshell', 'spin'): 2, ('shell', 'occupancy'): 2, ('shell', 'spin'): 3}
EDGES10 = [(n_, l_), (l_, k_), (k_, q_), (k_, S_), (e_, f_), (f_, g_), (q_, g_), (g_, G_), (f_, G_), (G_, Sp_)]

# lifted verbatim from r2-ch12f.py (chat 73)
def build9(caps):
    N,E,LM,KM,FM = caps
    out=[]
    for n in range(1,N+1):
      for l in range(0,min(LM,n-1)+1):
        for k in range(1,min(KM,4*l+2)+1):
          for q in range(0,k+1):
            for e in range(1,E+1):
              for f in range(0,min(FM,e-1)+1):
                for g in range(0,min(4*f+2,q)+1):
                  for S2 in range(0,k+1):
                    for S2p in range(0,g+1):
                      out.append((n,l,k,q,e,f,g,S2,S2p))
    return out

# lifted verbatim from r2-ch12f.py (chat 73)
def src(c): return (c[0],c[1],c[2],c[7])

# lifted verbatim from r2-ch12f.py (chat 73)
def tgt(c): return (c[4],c[5],c[6],c[8])

# lifted verbatim from r2-ch12f.py (chat 73)
def leq(x,y): return all(a<=b for a,b in zip(x,y))

# lifted verbatim from r2-ch12f.py (chat 73)
