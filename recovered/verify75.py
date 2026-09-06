import sys, os, hashlib, importlib.util
spec = importlib.util.spec_from_file_location("cond", "pack58/condense.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
paths = c.tree()
new = [p for p in paths if p.startswith('pack76/') or p == 'SESSION-76-COMBINED.md']
sub = {p:h for p,h in paths.items() if p not in new}
print("current files:", len(paths), " s76-new:", len(new), " subset:", len(sub))
print("subset root :", c.root_hash(sub))
print("s75 sealed  : ff11fa8d3aba377426a42c2ff67b597a2a61317631b7980b0c8c0015fcbbd62e (1215)")
print("VERDICT     :", "MATCH" if c.root_hash(sub)=="ff11fa8d3aba377426a42c2ff67b597a2a61317631b7980b0c8c0015fcbbd62e" and len(sub)==1215 else "MISMATCH")
for p in sorted(new): print("   NEW  ", p)