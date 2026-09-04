#!/usr/bin/env python3
"""mech_audit.py -- the mechanism lists must agree across all three places they appear.

Register 778. MECHANISMS.md, mathreg.py and QUEUE.md each name the P family. They
drifted: mathreg held 15, MECHANISMS 14, QUEUE 10. A list kept by hand in three
files will drift again; this makes the disagreement a failure rather than a fact
nobody checks.
"""
import re, importlib.util as iu, sys
sp = iu.spec_from_file_location("_m", "mathreg.py"); m = iu.module_from_spec(sp)
try: sp.loader.exec_module(m)
except SystemExit: pass
reg = {k for k in m.REG if k.startswith("P.")}
mec = set(re.findall(r"^## (P\.\w+)", open("MECHANISMS.md", encoding="utf-8").read(), re.M))
que = set(re.findall(r"P\.\w+", open("QUEUE.md", encoding="utf-8").read()))
fail = 0
for a, b, an, bn in [(reg, mec, "mathreg.py", "MECHANISMS.md"),
                     (reg, que, "mathreg.py", "QUEUE.md")]:
    if a != b:
        fail += 1
        print(f"  MISMATCH {an} ({len(a)}) vs {bn} ({len(b)})")
        if a - b: print(f"      only in {an}: {sorted(x[2:] for x in a-b)}")
        if b - a: print(f"      only in {bn}: {sorted(x[2:] for x in b-a)}")
print("  MECHANISM LISTS AGREE" if not fail else f"  {fail} MISMATCH(ES)")
sys.exit(fail)
