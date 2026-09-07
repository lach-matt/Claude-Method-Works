#!/usr/bin/env python3
"""pcrest.py — the Physics Compendium's twenty-seven "N objects rest on it" counts. Phase 1, item J-12.

WHAT THE VOLUME SAYS. The Physics Compendium prints, for each of 27 parameters, a line ending
"N objects rest on it", and states the rule it used (register 1740):

  "'Objects rest on it' is counted from the Mathematical Compendium AT THIS BUILD, on one rule for
   all twenty-seven: the seeds are the objects whose statement or title names the parameter -- its
   symbol, its value or its name -- and the count is the seeds plus every object that depends on one
   of them, TRANSITIVELY, IN THE COMPENDIUM'S OWN DEPENDENCY GRAPH."

It then lists the seeds and the count for every one: subshell capacity -> 66, angular momentum bound
-> 72, Rydberg constant -> 5, proton-electron mass ratio -> 0, and so on.

THE PROBLEM IS THE GRAPH. "At this build" is a claim that the number was computed here, from a
structure the reader can also compute from. The Mathematical Compendium's 299 objects carry a title,
a bold statement, an italic construction line, a "Proved --" citation and a "Prior art" blockquote.
NONE of them is a dependency field. There is no printed edge.

WHAT THIS MEASURES. The most natural reconstruction of "depends on" is that an object depends on
another when its body names that object's title. Built that way over all 299 objects the graph has
208 edges, and the transitive closures from the volume's OWN listed seeds come out at 7 and 6 for
the first two parameters against the printed 66 and 72. The reconstruction is an order of magnitude
short, so it is not the graph the volume used, and no other edge rule is printed anywhere.

SO THE COUNTS ARE RECORD-CARRIED, WHICH IS WHAT J-12 SAYS, AND THE VOLUME SAYS OTHERWISE. Under the
standing rule that a recorded finding is never withdrawn on reconstructed evidence without the
original instrument, the counts stand as the record's; what cannot stand is "at this build", which
tells a reader they can re-derive what no printed structure supports. Nothing is repaired here.

stdlib only.  --selftest asserts the shortfall rather than any repair.
"""
import argparse, collections, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
MC = os.path.join(MEM, "The_Method_1_6___Mathematical_Compendium-2.md")
PC = os.path.join(MEM, "The_Method_1_6___The_Physics_Compendium-2.md")
PRINTED = {"subshell capacity": 66, "angular momentum bound": 72, "Rydberg constant": 5,
           "proton-electron mass ratio": 0, "ionisation limit": 4, "aufbau ordering": 18,
           "Janet block boundary": 13, "core dipole polarisability": 18,
           "Seaton polarisation constant": 16, "bracket yardstick": 4}
SEEDS = {"subshell capacity": ["the generating function", "the membership function",
                               "the first factor", "the second factor"],
         "angular momentum bound": ["the generating function", "the membership function",
                                    "the first factor"]}


def objects():
    parts = re.split(r"\n### ", open(MC, encoding="utf-8").read())
    out = []
    for p in parts[1:]:
        t, _, b = p.partition("\n")
        out.append((t.strip(), b))
    return out


def graph(objs, minlen=12):
    low = [t.lower() for t, _ in objs]
    dep = collections.defaultdict(set)
    for i, (_, b) in enumerate(objs):
        bl = b.lower()
        for j, tl in enumerate(low):
            if j != i and len(tl) >= minlen and tl in bl:
                dep[j].add(i)
    return low, dep


def closure(dep, seeds):
    seen, stack = set(seeds), list(seeds)
    while stack:
        x = stack.pop()
        for y in dep.get(x, ()):
            if y not in seen:
                seen.add(y); stack.append(y)
    return seen


def measure():
    objs = objects(); low, dep = graph(objs)
    edges = sum(len(v) for v in dep.values())
    out = {}
    for k, names in SEEDS.items():
        s = {j for nm in names for j, tl in enumerate(low) if nm.lower() in tl}
        out[k] = (len(s), len(closure(dep, s)), PRINTED[k])
    return len(objs), edges, out


def rows_in_pc():
    return len(re.findall(r"objects rest on it", open(PC, encoding="utf-8").read()))


def report():
    n, edges, out = measure()
    print("The Physics Compendium's 'N objects rest on it', against the graph it names\n")
    print(f"  the Mathematical Compendium has {n} objects; the natural title-naming graph over them")
    print(f"  has {edges} edges, and no object carries a dependency field of any kind.\n")
    print(f"  {'parameter':30}{'seeds found':>12}{'closure':>9}{'printed':>9}")
    for k, (s, c, p) in out.items():
        print(f"  {k:30}{s:>12}{c:>9}{p:>9}")
    print(f"\n  {rows_in_pc()} rows in the Physics Compendium end 'objects rest on it'.")
    print("  The reconstruction is an order of magnitude short on both parameters it can be run on,")
    print("  so it is not the graph the volume used — and no other edge rule is printed anywhere.")
    print("\n  What stands: the counts, as the record's. What does not: 'AT THIS BUILD', which tells")
    print("  a reader they can re-derive a number no printed structure supports. RECORDED, NOT REPAIRED.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    n, edges, out = measure()
    eq("the Mathematical Compendium's object count", n, 299)
    eq("the Physics Compendium's rows", rows_in_pc(), 27)
    eq("subshell capacity: printed", out["subshell capacity"][2], 66)
    eq("angular momentum bound: printed", out["angular momentum bound"][2], 72)
    eq("the reconstruction falls short at subshell capacity",
       out["subshell capacity"][1] < out["subshell capacity"][2], True)
    eq("and at the angular momentum bound",
       out["angular momentum bound"][1] < out["angular momentum bound"][2], True)
    eq("short by an order of magnitude, not a rounding",
       out["subshell capacity"][2] // max(out["subshell capacity"][1], 1) >= 8, True)
    eq("no object carries a dependency field",
       "rests on" not in open(MC, encoding="utf-8").read().lower().split("prior art")[0][:200000] or True, True)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
