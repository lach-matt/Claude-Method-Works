#!/usr/bin/env python3
"""emit.py -- build project-knowledge files from restore-point-2_13.

Every emitted file carries a header stating the bank, its sha256, and the exact
source files concatenated, so a stale snapshot cannot masquerade as current.
Contents are COPIED VERBATIM. Nothing here is summarised.
"""
import hashlib, os, pathlib

BANK = "/home/claude/bank"
OUT = "/home/claude/out"
BANKSHA = "8057709403ed2c795cc753f74e68b2cbfc3aeb9c67f45e7c0e38b3129fd857a5"
os.makedirs(OUT, exist_ok=True)

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(65536), b""):
            h.update(b)
    return h.hexdigest()

def header(title, srcs):
    L = [f"# {title}",
         f"# BANK: restore-point-2_13.tar.gz  sha256 {BANKSHA}",
         f"# 694 files, register max R 1700, certificate 1.8.3",
         f"# Extracted verbatim. Not a summary. Stale if the bank advances past 2_13.",
         "# SOURCE FILES:"]
    for s in srcs:
        p = os.path.join(BANK, s)
        L.append(f"#   {s}  ({os.path.getsize(p)} bytes)  sha256 {sha(p)[:16]}")
    return "\n".join(L) + "\n\n"

def concat(outname, title, srcs):
    srcs = [s for s in srcs if os.path.exists(os.path.join(BANK, s))]
    body = [header(title, srcs)]
    for s in srcs:
        body.append("\n" + "=" * 78 + f"\n=== FILE: {s}\n" + "=" * 78 + "\n")
        body.append(pathlib.Path(os.path.join(BANK, s)).read_text(
            encoding="utf-8", errors="replace"))
    t = "".join(body)
    pathlib.Path(os.path.join(OUT, outname)).write_text(t, encoding="utf-8")
    return outname, len(t), len(srcs)

results = []

# 1 · manifest
lines = [header("BANK-2_13 MANIFEST — every file, size, hash", [])]
lines.append(f"{'size':>10}  {'sha256(16)':<18}  path\n")
allf = sorted(pathlib.Path(BANK).rglob("*"))
nf = 0
for p in allf:
    if p.is_file():
        nf += 1
        lines.append(f"{p.stat().st_size:>10}  {sha(p)[:16]:<18}  {p.relative_to(BANK)}\n")
lines.append(f"\nTOTAL FILES: {nf}\n")
pathlib.Path(f"{OUT}/BANK-2_13-MANIFEST.txt").write_text("".join(lines), encoding="utf-8")
results.append(("BANK-2_13-MANIFEST.txt", sum(len(x) for x in lines), nf))

# 2 · code, the Lowdin line
results.append(concat("CODE-LOWDIN-2_13.txt",
    "LOWDIN CODE — the corridor line, verbatim",
    ["ground.py", "brack.py", "bracket.py", "madelung.py", "madelung2.py",
     "aufbau.py", "null_madelung.py", "lowdin_gate.py", "lowdin_outer.py",
     "lowdin_dich.py", "lowdin_tight.py", "lowdin_rule.py", "nuclear_corridor.py"]))

# 3 · register
results.append(concat("REGISTER-2_13.txt",
    "THE REGISTER — R 165 to R 1700, complete", ["REGISTER-DATA.md"]))

# 4 · governance
results.append(concat("DIGEST-BOARD-2_13.txt",
    "DIGEST, BOARD, HANDOFF PROTOCOL, CERTIFICATE",
    ["DIGEST.md", "BOARD.md", "HANDOFF-PROTOCOL.md",
     "HANDOFF-CERTIFICATE-1_8_3.md"]))

# 5 · Lowdin findings
results.append(concat("FINDINGS-LOWDIN-2_13.txt",
    "LOWDIN — chapter and literature, verbatim",
    ["CHAPTER-LOWDIN.md", "LOWDIN-LITERATURE.md"]))

# 6 · spectra
results.append(concat("SPECTRA-2_13.txt",
    "SPECTRA.md — the index's own statement", ["SPECTRA.md"]))

for n, sz, c in results:
    print(f"{n:<32} {sz:>9,} chars  ({c} sources)")
