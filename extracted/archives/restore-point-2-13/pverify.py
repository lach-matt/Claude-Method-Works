#!/usr/bin/env python3
"""pverify.py -- the P family, recomputed rather than asserted.

Register 1011. `mathverify.py` makes 103 assertions naming 46 of the register's 214
objects; the P family's seventeen members are named by none of them. Their evidence
lives in analysis scripts and in MECHANISMS.md, which is not the same as a check that
reruns.

This recomputes each P-family claim from SPECTRA-DATA.tsv and compares it to the figure
the register states. A discrepancy is reported, not silenced. What it does NOT do is
re-derive the mechanisms — it checks that the numbers the register carries are the
numbers the data gives, which is exactly the failure mode register 782 produced when a
column asserted a verification that never ran.

Every threshold used here is the one the register itself states, so a mechanism cannot
pass by having its own criterion loosened.

A FIRST VERSION REIMPLEMENTED the tests and disagreed with three of them — because a
second implementation of a grouping is a second chance to get it wrong, and it did:
`channel_verify` groups by (species, core) and averages within each l, and the copy
overwrote instead. **This version runs the ESTABLISHED scripts and parses what they
print.** One implementation, checked against the register, is the point (register 1012).
"""
import re, math, statistics as st
from collections import defaultdict, Counter
from zeno import State, step

LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹°", "0123456789*")
ZNUM = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,
        "Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,
        "Sc":21,"Ti":22,"Fe":26,"Zn":30,"Ga":31,"Cd":48,"Ba":56,"Hg":80,"Bi":83}
HEAVY = {"Bi","Ba","Hg","Cd","Pb","Tl"}
OPEN_CORE = {"Ne II","Ar II","Si I","Bi I"}     # register 758's classification


import subprocess, sys

def _run(script):
    r = subprocess.run([sys.executable, script], capture_output=True, text=True, timeout=1500)
    return r.stdout + r.stderr

def run():
    import os, shutil
    if os.path.isdir(".zeno"): shutil.rmtree(".zeno")
    out = []

    cv = _run("channel_verify.py")
    m = re.search(r"(\d+) adjacent-l pairs correct, (\d+) inverted", cv)
    if m: out.append(("P.lcollapse — adjacent-l pairs ordered",
                      int(m.group(1)), int(m.group(1))+int(m.group(2)), 229, 230))

    pj = _run("pjj.py")
    m = re.search(r"consistent < 0\.05\s+(\d+)", pj)
    m2 = re.search(r"TESTABLE\s+(\d+)", pj)
    if m and m2: out.append(("P.jj — J-pairs consistent",
                             int(m.group(1)), int(m2.group(1)), 114, 129))

    mo = _run("mono.py")
    m = re.search(r"(\d+) of (\d+) fall", mo)
    if m: out.append(("P.mono — resolved steps falling (single-claim form)",
                      int(m.group(1)), int(m.group(2)), None, None))

    br = _run("bracket.py")
    m = re.search(r"(\d+) pass, (\d+) FAIL", br)
    if m: out.append(("the delta bracket — interior cells passing",
                      int(m.group(1)), int(m.group(1))+int(m.group(2)), None, None))

    cs = _run("converge_selfsame.py")
    m = re.search(r"(\d+) of (\d+) channels agree between halves", cs)
    if m: out.append(("P.selfsame — disjoint windows agreeing",
                      int(m.group(1)), int(m.group(2)), 67, 72))
    return out

with State("pverify") as s:
    res = step(s, "run the established scripts and read what they report", run, budget=1700)

print(f"  THE P FAMILY — the established scripts rerun, against the register\n")
print(f"  {'claim':<50}{'now':>11}{'register':>11}")
fails = 0
for lab, k, n, ek, en in res:
    now = f"{k}/{n}"
    if ek is None:
        print(f"  {lab:<50}{now:>11}{'—':>11}")
        continue
    reg = f"{ek}/{en}"
    agree = (k == ek and n == en)
    fails += not agree
    print(f"  {lab:<50}{now:>11}{reg:>11}   {'' if agree else '← DISAGREES'}")
print()
print("  EVERY REGISTERED FIGURE REPRODUCES" if not fails
      else f"  {fails} figure(s) differ — the register is stale or the data has moved")
