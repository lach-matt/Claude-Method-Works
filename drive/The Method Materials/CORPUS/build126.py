#!/usr/bin/env python3
"""
build126.py — reconstruct the members of the 126 `untested` channel rows.

Ruling: author, chat 33 ("yes to the build").
Method: RESPONSE-TO-METHOD-1_6.md §1, the verbatim `bracket.py` constructor,
        with the per-row limit taken from our OWN channel table's last column
        (§3 of that document) instead of the one-limit `LIM` dict.

Reads   : /home/claude/work/spectra_raw/*.tsv   (restore pack A, originals)
          /home/claude/build/The_Method_1_6___Spectra_Compendium-2.md
Writes  : nothing. Prints a report.
"""
import re, os, glob, sys
from collections import defaultdict

SPECTRA = "/home/claude/build/The_Method_1_6___Spectra_Compendium-2.md"
RAW     = "/home/claude/work/spectra_raw"

# ---------------------------------------------------------------- 1 · the rows
def num(s):
    return float(s.replace(",", "").strip())

ROWS = []
for line in open(SPECTRA, encoding="utf-8"):
    if not line.startswith("|") or "untested" not in line:
        continue
    p = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(p) < 11:
        continue
    species_raw = p[0]
    star = species_raw.endswith("*")
    species = species_raw.rstrip(" *")
    desig   = p[1]
    nrange  = p[2].replace("\u2013", "-").replace("\u2014", "-")
    members = int(p[3])
    lim     = num(p[10])
    # designation is  n<l> <term> J=<J>
    m = re.match(r"^(.*?)n([spdfghik])\s+(\S+)\s+J=(\S+)$", desig)
    if not m:
        print("UNPARSED DESIGNATION:", repr(desig)); continue
    tprefix, ell, term, J = m.group(1), m.group(2), m.group(3), m.group(4)
    gap = "\u2020" in nrange
    nums = re.findall(r"\d+", nrange)
    lo, hi = int(nums[0]), int(nums[-1])
    ROWS.append(dict(species=species, star=star, desig=desig, ell=ell,
                     term=term, J=J, lo=lo, hi=hi, members=members, lim=lim,
                     tprefix=tprefix, gap=gap))

print("rows parsed:", len(ROWS))

# ------------------------------------------------------- 2 · species -> files
# stem prefix match: SiI matches SiI.tsv, SiI_ryd.tsv ... but NOT SiII*.
def stems_for(species):
    key = species.replace(" ", "")          # "Si I" -> "SiI"
    out = []
    for f in sorted(glob.glob(os.path.join(RAW, "*.tsv"))):
        st = os.path.basename(f)[:-4]
        if st == key or st.startswith(key + "_"):
            out.append(f)
    return out

SPECIES = sorted({r["species"] for r in ROWS})
FILES = {s: stems_for(s) for s in SPECIES}
for s in SPECIES:
    print(f"  {s:8s} {len(FILES[s])} files: {[os.path.basename(x) for x in FILES[s]]}")

# --------------------------------------------------- 3 · the constructor (§1)
CONF = re.compile(r"^(.*?)(\d+)([spdfghik])$")

def levels(paths):
    """Yield (prefix, n, ell, term, J, E) for every admissible line."""
    for f in paths:
        for line in open(f, encoding="utf-8"):
            if line.startswith("#") or line.startswith("config") or not line.strip():
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) < 4:
                continue
            mm = CONF.match(p[0].strip())
            if not mm:
                continue
            try:
                E = float(p[3])
            except ValueError:
                continue
            yield mm.group(1), int(mm.group(2)), mm.group(3), p[1].strip(), p[2].strip(), E

CACHE = {s: list(levels(FILES[s])) for s in SPECIES}
for s in SPECIES:
    print(f"  {s:8s} {len(CACHE[s])} admissible levels")

def series_for(species, lim):
    """Full constructor at one limit. Returns {(prefix,ell,term,J): [(n,E)...]}"""
    ser = defaultdict(list)
    for prefix, n, ell, term, J, E in CACHE[species]:
        if E >= lim:
            continue
        ser[(prefix, ell, term, J)].append((n, E))
    out = {}
    for k, v in ser.items():
        v = sorted(set(v))
        if len(v) < 3:
            continue
        out[k] = v
    return out

# ------------------------------------------------------------- 4 · match rows
def norm(t):
    """Term as printed in the table vs as written in the TSV."""
    return t.replace("*", "").replace(" ", "")

hit = miss = 0
report = []
for r in ROWS:
    cand = series_for(r["species"], r["lim"])
    matches = []
    for (prefix, ell, term, J), v in cand.items():
        if ell != r["ell"]:
            continue
        if norm(term) != norm(r["term"]):
            continue
        if J != r["J"]:
            continue
        matches.append((prefix, v))
    if matches:
        hit += 1
        best = matches[0]
        ns = [n for n, _ in best[1]]
        ok = (min(ns) == r["lo"] and max(ns) == r["hi"] and len(ns) == r["members"])
        if ok is False and r["gap"]:
            ok = (min(ns) == r["lo"] and max(ns) == r["hi"] and len(ns) == r["members"])
        report.append((r, len(matches), best[0], ns, ok))
    else:
        miss += 1
        report.append((r, 0, None, None, False))

print("\n=== RESULT ===")
print("rows with a constructed series :", hit)
print("rows with none                 :", miss)
exact = sum(1 for x in report if x[4])
print("rows whose n-range AND member count reproduce EXACTLY :", exact)

print("\n=== per species ===")
bys = defaultdict(lambda: [0, 0, 0])
for r, nm, pre, ns, ok in report:
    bys[r["species"]][0] += 1
    if nm: bys[r["species"]][1] += 1
    if ok: bys[r["species"]][2] += 1
for s in sorted(bys):
    t, h, e = bys[s]
    print(f"  {s:8s} rows {t:3d} · constructed {h:3d} · exact {e:3d}")

print("\n=== first 15 rows in detail ===")
for r, nm, pre, ns, ok in report[:15]:
    print(f"{'OK ' if ok else '   '} {r['species']:7s} {r['desig']:22s} "
          f"table {r['lo']}-{r['hi']} ({r['members']}) "
          f"built {ns if ns else '—'} matches={nm} prefix={pre!r}")

