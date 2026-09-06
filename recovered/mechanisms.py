"""
THE TWO MECHANISMS, WORKED INTO THE LAW.  Queue item A2 / the Loewdin solution.

WHAT ITEM 7 ESTABLISHED

With the limit set at the last available species, Lambda_spectra's defect is
E = 11, every cell named, and the eleven are TWO MECHANISMS:

    six  · half or full shell — Hund exchange
           3d4->3d5, 3d9->3d10, 4d9->4d10, 4f8->4f7, 5f8->5f7, 5d8->5d9
    five · block opening, d preferred over f
           4d3, 4d6, 4f2, 5f1, 5f5

THE LAW AS IT STANDS

    nu(n,l,q) = n - a*sqrt( n-l-1 + q/(2(2l+1)) )
    the incoming electron takes the Pauli-admissible subshell of least nu

It reproduces 106 of 106 INCLUDING every anomaly -- but it does so by
RECALIBRATING a, eighteen times, at Z = 3, 19, 37, 42, 43, 45, 55, 58, 64, 65,
80, 81, 87, 91, 96, 97, 103, 104. The law ADMITS the anomalies; it does not
PREDICT them.

THE TEST

If the two mechanisms are real physics rather than labels, adding them to nu
should produce the anomalies directly, and the resets that exist only to absorb
an anomaly should become unnecessary. So:

    measure the resets needed WITHOUT the mechanisms, and WITH them.

A reduction is the result. No reduction means the mechanisms are re-describing
what a's freedom already covers, which by A.derived cannot repair anything.

The mechanism terms carry ONE parameter each and both are gated by a COUNT, not
fitted per element:

    exchange   fires when entering makes k = 2l+1 (half) or 4l+2 (full)
    opening    fires at the first element of a block, where Q.collapse puts the
               threshold: Z = 21 (3d), 57 (4f), 89 (5f)
"""
import sys, math
sys.path.insert(0, "/home/claude/work")
import ground as G

CAP = lambda l: 2*(2*l+1)
MAD = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
       (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]

def observed(Z):
    return {(n,l):o for n,l,o in G.expand(Z) if o > 0}

def nu(n, l, q, a):
    return n - a*math.sqrt(max(0.0, (n-l-1) + q/CAP(l)))

def bonus(n, l, q, Z, gx, go):
    """the two mechanisms. q is the occupancy BEFORE the electron enters, so
    entering makes it q+1. Both are gated by counts, not fitted per element."""
    b = 0.0
    if q+1 == 2*l+1 or q+1 == CAP(l):      # half-filled or filled
        b -= gx
    if l >= 2 and Z in (21, 57, 89):        # Q.collapse's block openings
        b -= go * (1 if l == 2 else -1)     # d preferred over f at an opening
    return b

def walk(gx=0.0, go=0.0, a0=0.0):
    """walk Z = 1..108 taking least nu among Pauli-admissible subshells.
    a is held until the observed choice is impossible, then moved minimally to
    the nearest value that makes it possible. Count the moves."""
    occ = {}; a = a0; resets = []; ok = 0
    for Z in range(1, 109):
        obs = observed(Z); prev = observed(Z-1) if Z > 1 else {}
        entered = [k for k in obs if obs[k] > prev.get(k, 0)]
        if len(entered) != 1:
            entered = entered[:1]
        if not entered: continue
        tgt = entered[0]
        cands = [(n,l) for n,l in MAD if occ.get((n,l),0) < CAP(l)]
        score = lambda k: nu(k[0], k[1], occ.get(k,0), a) + bonus(k[0],k[1],occ.get(k,0),Z,gx,go)
        best = min(cands, key=score)
        if best != tgt:
            # move a to the smallest value making tgt the minimum
            lo, hi, found = 0.0, 3.0, None
            for t in range(3001):
                aa = t/1000.0
                s = lambda k: nu(k[0],k[1],occ.get(k,0),aa) + bonus(k[0],k[1],occ.get(k,0),Z,gx,go)
                if min(cands, key=s) == tgt:
                    if found is None or abs(aa-a) < abs(found-a): found = aa
            if found is not None:
                resets.append((Z, round(a,3), round(found,3))); a = found
        if min(cands, key=score) == tgt: ok += 1
        occ[tgt] = occ.get(tgt,0) + 1
    return ok, resets

if __name__ == "__main__":
    print("  THE TWO MECHANISMS WORKED INTO nu — do they reduce the resets?\n")
    print(f"  {'gx (exchange)':<16}{'go (opening)':<15}{'steps right':>12}{'resets':>9}")
    for gx, go in ((0.00,0.00),(0.05,0.00),(0.10,0.00),(0.20,0.00),
                   (0.00,0.10),(0.10,0.10),(0.20,0.20),(0.30,0.10)):
        ok, r = walk(gx, go)
        print(f"  {gx:<16.2f}{go:<15.2f}{ok:>12}{len(r):>9}")
    print("\n  baseline recorded in resets.py: 18 recalibrations of a")
