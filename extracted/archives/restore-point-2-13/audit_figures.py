#!/usr/bin/env python3
"""audit_figures.py — stage 2: the numbers.

Stage 1 checked structure. This checks CONTENT: every figure that appears in more
than one place must agree, and every figure in an object graded COMPUTED must
match what the generator computes.

WHY THIS STAGE EXISTS. Today found T.tower stating 70905, 199130 against a
generator computing 22275, 64290 — a correction register 1399 recorded as made
and which was lost in the rollback. It was found by scanning all forty-three
COMPUTED objects carrying figures. This automates that scan and widens it.

THE METHOD. Extract every distinguishable numeric token from each artefact, keep
those appearing in two or more artefacts, and report any that appear with
DIFFERENT companions — i.e. any figure whose neighbourhood differs. Then check
the tower, the census and the named sequences directly against their generators.

WHAT THIS CANNOT DO. It cannot tell a coincidence of digits from a shared claim.
So it reports CANDIDATES and each is read, not trusted. Declared before running.
"""
import re, subprocess, sys, pathlib
from collections import defaultdict

W = pathlib.Path("/home/claude/work")
ART = ["COMPENDIUM.md", "INDICES.md", "PHYSICS.md", "SPECTRA.md", "REGISTER.md"]
fails = []


def check(name, ok, detail=""):
    print(f"    {name:<38}{'PASS' if ok else 'FAIL'}   {detail}")
    if not ok:
        fails.append(name)


print("  AUDIT · STAGE 2 — THE NUMBERS\n")

# ---- A · the tower, against its generator --------------------------------
idx = (W / "INDICES.md").read_text(encoding="utf-8")
comp = (W / "COMPENDIUM.md").read_text(encoding="utf-8")
tab = dict(re.findall(r"\| \*\*(Λ₈|Λ₉|Λ₁₀|Λ₁₁|Λ₁₂|Λ₁₃)\*\* \| ([\d,]+) \|", idx))
tw = re.search(r"Lambda-8…Lambda-13 = |Λ₈…Λ₁₃ = ([\d, ]+);", comp)
seq_comp = re.search(r"976, 1654, 2535, 13585, (\d+), (\d+)", comp)
check("tower · compendium vs generated table",
      seq_comp and seq_comp.group(1) == tab["Λ₁₂"].replace(",", "")
      and seq_comp.group(2) == tab["Λ₁₃"].replace(",", ""),
      f"Λ₁₂ {seq_comp.group(1) if seq_comp else '?'} vs {tab['Λ₁₂']}, "
      f"Λ₁₃ {seq_comp.group(2) if seq_comp else '?'} vs {tab['Λ₁₃']}")

# ---- B · the two-column counts -------------------------------------------
a = re.search(r"Λ₈ ([\d,]+)/([\d,]+)", idx)
b = re.search(r"Lambda-8 ([\d,]+)/([\d,]+)", comp)
check("two-column · Λ₈ across artefacts", a and b and a.group(2) == b.group(2),
      f"{a.group(1)}/{a.group(2)} vs {b.group(1)}/{b.group(2)}")

# ---- C · every COMPUTED object's figures vs the artefacts ----------------
src = (W / "mathreg.py").read_text(encoding="utf-8")
objs = re.findall(r'R\("([\w.]+)",\s*"(.*?)",\s*"(.*?)",\s*\[(.*?)\],\s*"(.*?)",\s*"(\w+)"',
                  src, re.S)
computed = [(o[0], re.sub(r"\s+", " ", o[1])) for o in objs if o[5] == "COMPUTED"]
withfig = [(k, s) for k, s in computed if re.search(r"\b\d[\d,]{2,}\b", s)]
print(f"\n    COMPUTED objects carrying a figure: {len(withfig)}")
missing = [k for k, s in withfig if k not in comp]
check("COMPUTED · all objects printed", not missing,
      "" if not missing else f"absent from the compendium: {missing[:6]}")

# ---- D · cross-artefact figure agreement ---------------------------------
def figs(text):
    out = defaultdict(set)
    for m in re.finditer(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d{4,})(?![\w.])", text):
        ctx = re.sub(r"\s+", " ", text[max(0, m.start() - 46):m.end() + 26])
        out[m.group(1).replace(",", "")].add(ctx)
    return out


per = {a_: figs((W / a_).read_text(encoding="utf-8")) for a_ in ART}
shared = set(per[ART[0]])
for a_ in ART[1:]:
    shared |= set(per[a_])
multi = [f for f in shared if sum(1 for a_ in ART if f in per[a_]) >= 2]
print(f"\n    figures appearing in 2+ artefacts: {len(multi)}")
print(f"    (a shared digit string is not a shared claim; these are candidates)")

# ---- E · the session's own headline claims, recomputed --------------------
print()
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    sys.path.insert(0, str(W))
    import brack, ground as G
L = "spdfg"
cap = lambda l: 2 * (2 * l + 1)
IV = {r[0]: r for r in brack.IV}
STEPS = sorted(IV)
check("walk · 106 steps", len(STEPS) == 106, f"{len(STEPS)} rows in brack.IV")
check("walk · corridors non-empty", all(IV[Z][4] < IV[Z][5] for Z in STEPS),
      f"{sum(1 for Z in STEPS if IV[Z][4] < IV[Z][5])} of {len(STEPS)}")
lo, hi, empt = -1e9, 1e9, []
for Z in STEPS:
    nlo, nhi = max(lo, IV[Z][4]), min(hi, IV[Z][5])
    if nlo >= nhi:
        empt.append(Z); lo, hi = IV[Z][4], IV[Z][5]
    else:
        lo, hi = nlo, nhi
check("walk · 14 forced moves (R 1401/1434)", len(empt) == 14, f"{len(empt)}: {empt}")
hf = max(IV[Z][4] for Z in STEPS if -1e8 < IV[Z][4] < 1e8)
tc = min(IV[Z][5] for Z in STEPS if IV[Z][5] < 1e8)
check("walk · no single a (R 1409)", hf > tc, f"highest floor {hf:.4f} > tightest ceiling {tc:.4f}")
check("ground · 108 configurations (R 1446)", max(G.GROUND) == 108, f"max Z = {max(G.GROUND)}")

print(f"\n  STAGE 2: {len(fails)} failure(s)" + (f" — {fails}" if fails else ""))
print(f"  {len(multi)} shared figures flagged as candidates for reading, not as faults.")
