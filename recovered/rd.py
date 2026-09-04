#!/usr/bin/env python3
"""rd.py -- READ DISCIPLINE.  Exploratory reads return REDUCTIONS, never listings.

WHY THIS EXISTS.  s57 spent most of its window printing rows it did not need:
a 200-line archive listing when one directory was wanted, and a 107-row dump
printed twice over because the glob matched pack*/ and rt/ without deduping.
The find that mattered -- pack53/cinf.jsonl -- was a COUNT and a SET, not a listing.

THE RULE, ENFORCED HERE AND NOT NARRATED:
  a survey answers HOW MANY, WHICH SET, and WHAT DIFFERS.
  if a full listing is genuinely needed it goes to a file under pack<N>/ and is
  hashed by seal.py -- it does not go into the context window.

Every function below returns a short string.  None of them prints a row per element.
"""
import glob, json, os

def rows(pattern, dedupe_by=None):
    """Load jsonl matching a glob. Deduped by (file-content, key) so a runtime copy
    of a sealed file is never counted twice -- s57's doubled dump was exactly this."""
    seen_files, out = set(), []
    for f in sorted(glob.glob(pattern)):
        with open(f, "rb") as fh:
            h = hash(fh.read())
        if h in seen_files:            # identical content elsewhere: skip
            continue
        seen_files.add(h)
        for line in open(f):
            try: d = json.loads(line)
            except Exception: continue
            d["_src"] = os.path.basename(f)
            out.append(d)
    if dedupe_by:
        uniq = {}
        for d in out:
            uniq.setdefault(dedupe_by(d), d)
        out = list(uniq.values())
    return out

def span(vals):
    """A set of integers as a compact range string: '2..108' or '2..4,11,19..20'."""
    v = sorted(set(vals))
    if not v: return "(empty)"
    parts, s, p = [], v[0], v[0]
    for x in v[1:]:
        if x == p + 1: p = x; continue
        parts.append(f"{s}" if s == p else f"{s}..{p}"); s = p = x
    parts.append(f"{s}" if s == p else f"{s}..{p}")
    return ",".join(parts)

def survey(name, ds, key="Z"):
    """HOW MANY and WHICH SET. One line."""
    ks = [d[key] for d in ds if key in d]
    return f"{name}: n={len(ds)} distinct {key}={len(set(ks))} span={span(ks)}"

def differs(a, b, key="Z", on="ent"):
    """WHAT DIFFERS between two row sets, as a set of keys. One line, no rows."""
    A = {d[key]: d.get(on) for d in a}
    B = {d[key]: d.get(on) for d in b}
    d = sorted(k for k in A.keys() & B.keys() if A[k] != B[k])
    return f"{on} differs at {len(d)}: {span(d)}" if d else f"{on} differs at 0"

def dump(path, ds, fields):
    """If a full listing IS needed, it goes to a FILE, not the window."""
    with open(path, "w") as fh:
        fh.write("\t".join(fields) + "\n")
        for d in ds:
            fh.write("\t".join(str(d.get(f, "")) for f in fields) + "\n")
    return f"wrote {len(ds)} rows -> {path}  (hash it with seal.py; do not cat it)"

if __name__ == "__main__":
    import sys
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.join(here, ".."))
    ci = rows("pack53/cinf.jsonl")
    ch = rows("pack51/nlchain.jsonl")
    print(survey("cinf  (c=1e6)", ci))
    print(survey("chain (sealed)", ch))
    print(differs(ch, ci))
