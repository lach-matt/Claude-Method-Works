"""
Lambda_merged -- (Z, c, n, l, 2S+1), the index register 1341 names and no script
ever built. Queue item A2.

WHY IT EXISTS

Lambda_spectra is the only index of the fourteen that stays open, and 1341 names
the cause: it has no PRINCIPAL QUANTUM NUMBER. Its cells are (Z, charge, l,
multiplicity) -- a channel, with n running inside it. The walk supplies n,
because a is defined per subshell, and a = delta/sqrt(p) makes them one object.

    Lambda_spectra   (Z, c, l, 2S+1)      328 channels     n absent
    the walk         per element          106 steps        n present
    MERGED           (Z, c, n, l, 2S+1)   cells are (species, subshell)

1341 predicts 1,195 cells for the 108 neutrals. That figure is TESTED here, not
assumed -- it is a count over the observed ground configurations, so it can come
out wrong.

WHAT IS AND IS NOT ASKED

E is computed in the SUBJECT'S OWN ORDER, not minimised over permutations. Z has
one order (the nuclear charge), n and l have theirs (the quantum numbers), and
2S+1 has its own. A.erel is explicit that E = 0 is a statement about a
COORDINATISATION, and that any composite cell count has SOME relabelling in which
it vanishes -- so a minimised E here would be meaningless. The coordinates come
from the subject.
"""
import re, sys
from itertools import product

LSYM = "spdfghi"

def read_ground():
    """the 108 observed ground configurations, from ground.py's own table."""
    src = open("ground.py", encoding="utf-8").read()
    rows = re.findall(r'\(\s*(\d+)\s*,\s*"([A-Za-z]+)"\s*,\s*"([^"]+)"', src)
    if not rows:
        rows = re.findall(r'^\s*(\d+)\s*:\s*"([^"]*)"', src, re.M)
        rows = [(z, "", c) for z, c in rows]
    return rows

def subshells(cfg):
    """expand a configuration string into (n, l, occ) triples."""
    NOBLE = {"[He]":"1s2", "[Ne]":"1s2.2s2.2p6",
             "[Ar]":"1s2.2s2.2p6.3s2.3p6",
             "[Kr]":"1s2.2s2.2p6.3s2.3p6.3d10.4s2.4p6",
             "[Xe]":"1s2.2s2.2p6.3s2.3p6.3d10.4s2.4p6.4d10.5s2.5p6",
             "[Rn]":"1s2.2s2.2p6.3s2.3p6.3d10.4s2.4p6.4d10.5s2.5p6.4f14.5d10.6s2.6p6"}
    for k, v in NOBLE.items():
        cfg = cfg.replace(k, v)
    out = []
    for tok in re.findall(r'(\d)([spdfghi])(\d*)', cfg):
        n, l, k = int(tok[0]), LSYM.index(tok[1]), int(tok[2] or 1)
        out.append((n, l, k))
    return out

def opR(X, d):
    X = set(X); vals = [sorted({x[i] for x in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for x in X: m[x[j]] = max(m.get(x[j], -10**9), x[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i != j)}

if __name__ == "__main__":
    rows = read_ground()
    print(f"  ground configurations read: {len(rows)}")
    cells, per_z = set(), {}
    for z, sym, cfg in rows:
        z = int(z)
        ss = subshells(cfg)
        per_z[z] = len(ss)
        for n, l, k in ss:
            # 2S+1 for a subshell holding k of its 2(2l+1): Hund's first rule
            cap = 2*(2*l+1)
            unpaired = min(k, cap - k) if k > cap//2 else min(k, cap//2)
            cells.add((z, 1, n, l, unpaired + 1))
    print(f"  cells (Z, c, n, l, 2S+1) : {len(cells)}")
    print(f"  register 1341 predicts   : 1195   -> "
          f"{'MATCHES' if len(cells)==1195 else 'DIFFERS by %+d' % (len(cells)-1195)}")
    print(f"  subshells per element: min {min(per_z.values())} "
          f"max {max(per_z.values())} mean {sum(per_z.values())/len(per_z):.1f}")

    # c is constant at 1 across the neutrals, so it is a DEFINING LETTER (A.define)
    # and contributes no envelope. Drop it and index on the four that vary.
    X = {(z, n, l, m) for z, c, n, l, m in cells}
    box = 1
    for i in range(4): box *= len({x[i] for x in X})
    print(f"\n  c is constant at 1 over the neutrals — a DEFINING LETTER (A.define),")
    print(f"  contributing no envelope. Indexing on (Z, n, l, 2S+1).")
    print(f"      cells {len(X)} · box {box} · density {len(X)/box:.4f}")
    R = opR(X, 4)
    print(f"      |ℛ(X)| = {len(R)}   E = {len(R)-len(X)}")
