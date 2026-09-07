import json
T = json.load(open("tower.json"))
stages = {8: [tuple(c) for c in json.load(open("L8.json"))]}
for d in (9,10,11,12,13): stages[d] = [tuple(c) for c in T[str(d)]]

print("rank-value counts per stage:", {d: len(set(sum(c) for c in stages[d])) for d in stages})
out = []
for d in (9,10,11,12,13):
    up, lo = stages[d], stages[d-1]
    fib = {}
    for c in up:
        r = sum(c); rlo = r - c[-1]        # rank below = total - new coordinate
        fib.setdefault(r, set()).add(rlo)
    rs = sorted(fib)
    strict = all(len(fib[r])==1 for r in rs)
    branch = max(len(fib[r]) for r in rs)
    mins = [min(fib[r]) for r in rs]; maxs = [max(fib[r]) for r in rs]
    mono = all(a<=b for a,b in zip(mins,mins[1:])) and all(a<=b for a,b in zip(maxs,maxs[1:]))
    gaps = any(sorted(fib[r]) != list(range(min(fib[r]), max(fib[r])+1)) for r in rs)
    out.append((d, strict, branch, mono, not gaps))
    print(f"Λ{d}→Λ{d-1}: strict map: {strict} | max branching: {branch} | bracket endpoints monotone: {mono} | fibres gap-free intervals: {not gaps}")

# composite bracket Λ13 -> Λ8 : composed per-stage vs direct
direct = {}
for c in stages[13]:
    r13 = sum(c); r8 = sum(c[:8])
    direct.setdefault(r13, []).append(r8)
# compose stage brackets
def stage_bracket(d):
    fib = {}
    for c in stages[d]:
        r = sum(c); fib.setdefault(r, []).append(r - c[-1])
    return {r: (min(v), max(v)) for r,v in fib.items()}
B = {d: stage_bracket(d) for d in (9,10,11,12,13)}
ok = True; slack = 0
for r13 in sorted(direct):
    lo, hi = r13, r13
    for d in (13,12,11,10,9):
        los = [B[d][r][0] for r in range(lo,hi+1) if r in B[d]]
        his = [B[d][r][1] for r in range(lo,hi+1) if r in B[d]]
        lo, hi = min(los), max(his)
    dl, dh = min(direct[r13]), max(direct[r13])
    if (lo,hi) != (dl,dh): ok = False; slack = max(slack, (dl-lo)+(hi-dh))
print("composite bracket χ(Λ13)→χ(Λ8): equals direct bracket:", ok, "| max slack:", slack)
r8vals = sorted(set(sum(c[:8]) for c in stages[13]))
print("image of Λ13 under projection to Λ8 ranks:", f"{min(r8vals)}..{max(r8vals)}",
      "| covers all of χ(Λ8):", r8vals == list(range(3,21)))
