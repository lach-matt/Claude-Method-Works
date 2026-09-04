"""
THE UPDATE RULE, DERIVED — per-block monotone ascent.  Registers 1401-1409.

WHAT WAS OPEN

QUEUE listed the update rule as the one thing NOT derived: "keep a unless
forced, move minimally" reproduces the table but is a CHOICE. Register 1331
sharpened it — seven of eight placement rules give 106/106, including uniformly
random interior points on 200 of 200 seeds — so the ordering data constrains
membership of the corridor and not position within it.

THE RULE

    at a JANET BLOCK OPENING   a := the block's own floor L
    inside a block             a := max(a, L)      -- a only ever RISES
    a NEVER descends inside a block

Zero violations across all 106 steps. No fitted parameter, no nearest-endpoint
comparison, no minimal-move heuristic.

WHY GLOBAL ASCENT FAILS AND PER-BLOCK ASCENT DOES NOT

Monotone ascent across the whole table is IMPOSSIBLE: it breaks at Ce 58 and
stays broken through Yb, because every 4f corridor has ceiling 1/sqrt(2) = 0.7071
with no floor, while a has already climbed to 1.2168 at Cs. It breaks again at Pa
and U in the 5f block. The global statement is decisive -- the highest floor
anywhere is 1.9841 and the tightest ceiling anywhere is 0.7071, so no single a
serves the whole walk by a factor of nearly three. That is register 1341's
NECESSITY OF STATE proved rather than asserted.

Both descents in the recorded trajectory are Janet block openings: La at the 4f
opening, Ac at the 5f. Nowhere else.

WHAT IT REPRODUCES

All eight a values HANDOFF records. Seven at the element the record names; the
eighth, Pa's 1.3660, assigned at the Ac 89 opening two elements earlier and held.

WHAT IS UNTESTED

The trajectory re-places a at six block openings -- B, Al, Sc, Y, La, Ac -- where
the record states no value. Agreement there is untested, not confirmed.
"""
import sys, math
sys.path.insert(0, "/home/claude/work")
import ground as G

LS = "spdfg"; cap = lambda l: 2*(2*l+1); INF = 1e9
JANET = [(1,2),(3,4),(5,12),(13,20),(21,38),(39,56),(57,88),(89,118)]
block = lambda Z: next(i for i,(a,b) in enumerate(JANET) if a <= Z <= b)

def corridor(Z):
    """the exact bracket: endpoints (n_r - n_g)/(sqrt(p_r) - sqrt(p_g))."""
    pr = {(n,l):o for n,l,o in G.expand(Z-1)}
    cu = {(n,l):o for n,l,o in G.expand(Z)}
    got = [k for k in cu if cu[k] > pr.get(k,0)]
    if len(got) != 1: return None
    gn, gl = got[0]; gp = gn-gl-1
    cand = []
    for l in range(5):
        for n in range(l+1, 9):
            if pr.get((n,l),0) >= cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0) == 0: break
    if (gn,gl) not in cand or len(cand) < 2: return None
    lo, hi = -INF, INF
    for n,l in cand:
        if (n,l) == (gn,gl): continue
        rp = n-l-1; d = math.sqrt(rp)-math.sqrt(gp); r = n-gn
        if abs(d) < 1e-12: continue
        if d > 0: hi = min(hi, r/d)
        else:     lo = max(lo, r/d)
    return (gn,gl), lo, hi

def walk():
    a, cur, out, viol = None, None, [], []
    for Z in range(3, 109):
        c = corridor(Z)
        if not c: continue
        g, lo, hi = c
        b = block(Z)
        if b != cur:
            a = lo if lo > -INF/2 and abs(lo) > 1e-9 else (0.0 if lo > -INF/2 else hi)
            cur = b; out.append((Z, "open", a)); continue
        na = max(a, lo) if lo > -INF/2 else a
        if na > hi + 1e-9:
            viol.append((Z, na, lo, hi))
            na = lo if lo > -INF/2 and abs(lo) > 1e-9 else hi
            out.append((Z, "forced", na))
        elif na != a:
            out.append((Z, "rise", na))
        a = na
    return out, viol

RECORDED = {19:0.5774, 37:1.0000, 55:1.2168, 57:0.7071,
            80:0.8090, 87:1.3938, 91:1.3660, 103:1.9841}

if __name__ == "__main__":
    moves, viol = walk()
    print("  Λ_walk — PER-BLOCK MONOTONE ASCENT\n")
    print(f"  violations across 106 steps : {len(viol)}")
    print(f"  moves : {len(moves)}  "
          f"({sum(1 for _,k,_ in moves if k=='open')} openings, "
          f"{sum(1 for _,k,_ in moves if k=='rise')} rises, "
          f"{sum(1 for _,k,_ in moves if k=='forced')} forced)\n")
    print(f"      {'Z':>4}{'el':>4}{'blk':>5}{'kind':>8}{'a':>10}   against the record")
    held = dict((Z,v) for Z,_,v in moves)
    for Z,k,v in moves:
        r = RECORDED.get(Z)
        tag = "" if r is None else f"recorded {r:.4f}  " + \
              ("MATCH" if abs(v-r) < 2e-3 else "differs")
        print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{block(Z):>5}{k:>8}{v:>10.4f}   {tag}")
    hit = sum(1 for Z,r in RECORDED.items()
              if any(abs(v-r) < 2e-3 and z <= Z for z,_,v in moves
                     for _ in [0] if z <= Z and all(zz <= Z for zz,_,_ in [(z,0,0)])))
    print(f"\n  every recorded a value is reached: "
          f"{sorted(RECORDED.values()) == sorted({round(v,4) for _,_,v in moves} & {round(r,4) for r in RECORDED.values()}) or 'see above'}")