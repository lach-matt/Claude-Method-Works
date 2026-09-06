"""
Is the ratio 10/2.5 = 14/3.5 = 18/4.5 = 4 an arithmetic accident on three pairs,
or an identity holding on a class of pairs?

Exact rational arithmetic throughout. Ordering READ from the source block
(Krane / Wong, HANDOFF section 3), never recalled.
"""
from fractions import Fraction as F
import sympy as sp

# --- the validated ordering, transcribed from HANDOFF section 3 ------------
ORDER = """1s1/2 1p3/2 1p1/2 1d5/2 2s1/2 1d3/2 1f7/2 2p3/2 1f5/2 2p1/2 1g9/2
1g7/2 2d5/2 2d3/2 3s1/2 1h11/2 1h9/2 2f7/2 1i13/2 3p3/2 2f5/2 3p1/2""".split()

LCODE = {'s': 0, 'p': 1, 'd': 2, 'f': 3, 'g': 4, 'h': 5, 'i': 6}


def parse(tag):
    n_r = int(tag[0])
    ell = LCODE[tag[1]]
    num, den = tag[2:].split('/')
    j = F(int(num), int(den))
    return n_r, ell, j


def levels():
    out = []
    for tag in ORDER:
        n_r, ell, j = parse(tag)
        N = 2 * (n_r - 1) + ell
        A = F(ell * (ell + 1))                      # centrifugal object
        S = (j * (j + 1) - ell * (ell + 1) - F(3, 4)) / 2   # <L.S>
        t = 1 if j == ell + F(1, 2) else -1          # spin-parallel / antiparallel
        out.append(dict(tag=tag, n_r=n_r, ell=ell, j=j, N=N, A=A, S=S, t=t))
    return out


L = levels()

# --- check 1: the closed form <L.S> = l/2  (t=+1)  or  -(l+1)/2  (t=-1) ----
print("CHECK 1  closed form for <L.S>")
bad = [x['tag'] for x in L
       if x['S'] != (F(x['ell'], 2) if x['t'] == 1 else -F(x['ell'] + 1, 2))]
print(f"    deviations: {bad if bad else 'none — closed form holds on all 22'}")

# --- check 2: every consecutive-pair constraint, exact --------------------
# beta*(A1 - A2) + alpha*(S2 - S1) < N2 - N1
print("\nCHECK 2  consecutive-pair constraints, exact rationals")
cons = []
for x, y in zip(L, L[1:]):
    b = x['A'] - y['A']
    a = y['S'] - x['S']
    rhs = y['N'] - x['N']
    ratio = b / a if a != 0 else None
    cons.append(dict(pair=f"{x['tag']}→{y['tag']}", b=b, a=a, rhs=rhs,
                     ratio=ratio, dN=y['N'] - x['N'],
                     dl=y['ell'] - x['ell'], t1=x['t'], t2=y['t']))

four = [c for c in cons if c['ratio'] == 4]
print(f"    pairs with coefficient ratio exactly 4: {len(four)} of {len(cons)}")
for c in four:
    print(f"      {c['pair']:<24} {c['b']:>4}b {c['a']:>+6}a < {c['rhs']:>2}"
          f"   dN={c['dN']}  dl={c['dl']:+d}  t:{c['t1']:+d}→{c['t2']:+d}")

# --- check 3: which of those actually force a sign on (4b + a) -----------
# a ratio-4 pair reads  (S2-S1)*(4b + a) < rhs.  It forces a sign only if rhs = 0.
print("\nCHECK 3  sign forced on the combination (4b + a)")
pos = [c for c in four if c['rhs'] == 0 and c['a'] < 0]
neg = [c for c in four if c['rhs'] == 0 and c['a'] > 0]
for c in pos:
    print(f"      {c['pair']:<24} → 4b + a > 0")
for c in neg:
    print(f"      {c['pair']:<24} → 4b + a < 0")
print(f"\n    {len(pos)} pairs demand 4b + a > 0")
print(f"    {len(neg)} pairs demand 4b + a < 0")
print(f"    both senses strict → {'EMPTY' if pos and neg else 'not empty'}")

# --- check 4: is it an identity?  symbolic, for all l ---------------------
print("\nCHECK 4  symbolic — is ratio 4 an identity in l?")
l2 = sp.symbols('l2', nonnegative=True, integer=True)
l1 = l2 + 2                       # the higher-l partner, two units up
S1 = -(l1 + 1) / sp.Integer(2)    # t = -1, spin-antiparallel
S2 = l2 / sp.Integer(2)           # t = +1, spin-parallel
dA = sp.expand(l1 * (l1 + 1) - l2 * (l2 + 1))
dS = sp.simplify(S2 - S1)
print(f"    dA = {dA}")
print(f"    dS = {sp.nsimplify(dS)}")
print(f"    dA/dS = {sp.simplify(dA / dS)}      (independent of l)")
print(f"    dS > 0 for every l >= 0: {sp.simplify(dS) .subs(l2, 0) > 0}")

# --- check 5: does the same-N condition follow from dl = 2? --------------
print("\nCHECK 5  N = 2(n_r-1)+l, so dl=+/-2 with dN=0 forces dn_r=-/+1")
same = [c for c in cons if abs(c['dl']) == 2 and c['t1'] != c['t2']]
print(f"    dl=+/-2 opposite-t pairs: {len(same)};"
      f" all with dN=0: {all(c['dN'] == 0 for c in same)};"
      f" all ratio 4: {all(c['ratio'] == 4 for c in same)}")
