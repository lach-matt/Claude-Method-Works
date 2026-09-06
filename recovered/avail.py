"""avail.py -- SESSION 65. Read-only census: is a TRANSFER test even supplied with data?
Counts the 42 q=1 ratio measurements by the l-pair they span, and reports the Z set
for each, so a proposed replacement test is not proposed into an empty cell."""
import json, os, statistics as st
HERE = os.path.dirname(os.path.abspath(__file__))
rows = {json.loads(l)['Z']: json.loads(l) for l in open(os.path.join(HERE,'..','rt','nlchain.jsonl'))}
T = lambda n, l: f"{n}{'spdfg'[l]}"
by = {}
for Z in sorted(rows):
    if Z < 3: continue
    D = dict(rows[Z]['order'])
    for n in range(2, 8):
        for l in range(0, 3):
            a, A, B = T(n, l), T(n, l+1), T(n+1, l)
            if a in D and A in D and B in D and abs(D[B]-D[a]) > 1e-4:
                by.setdefault(l, []).append((Z, n, (D[A]-D[a])/(D[B]-D[a])))
print("  l-pair      n   median a    min      max     Z range")
for l in sorted(by):
    v = [x[2] for x in by[l]]; zs = [x[0] for x in by[l]]
    print(f"  {'spdf'[l]}->{'spdf'[l+1]}    {len(v):>4}   {st.median(v):7.3f} {min(v):8.3f} {max(v):8.3f}"
          f"   {min(zs)}-{max(zs)}")
print("\n  d->f measurements in detail (the pair that decides blocks 7 and 8):")
for Z, n, a in by.get(2, []): print(f"    Z={Z:>4}  {n}d->{n}f   a={a:7.3f}")