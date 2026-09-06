#!/usr/bin/env python3
"""gate75 - locks the numeric claims of FORMAL-DERIVATION-STATEMENT.md against
the sealed sources. Ground truth is the SOURCE FILES, not this script's authors
(R 1968 / R-A). Each claim names the file it must be found in."""
import re, sys, os
ROOT = os.path.dirname(os.path.abspath(__file__)) + "/.."
STMT = os.path.join(ROOT, "pack75/FORMAL-DERIVATION-STATEMENT.md")
ASM  = os.path.join(ROOT, "pack63/ASSEMBLY-RUNG-0.md")
AMD  = os.path.join(ROOT, "pack70/AMENDMENT-STALE-LINES-S70.md")

# (label, string that must appear in the statement, source file it must also appear in)
CLAIMS = [
 ("c",              "137.035999",        ASM),
 ("hydrogen E",     "-0.5000080791",     ASM),
 ("2s E",           "-0.1250033510",     ASM),
 ("2p E",           "-0.1250013413",     ASM),
 ("seed margin",    "375 mHa",           ASM),
 ("self-int miss",  "8.08 microhartree", ASM),
 ("num floor",      "0.05 mHa",          ASM),
 ("tight margin",   "32.33 mHa",         ASM),
 ("floor factor",   "650",               ASM),
 ("seed forgotten", "0.005 mHa",         ASM),
 ("truncation",     "87",                ASM),
 ("exceptions n",   "11 of 107",         ASM),
 ("exception rows", "25, 30, 43, 47, 48, 64, 71, 80, 96, 103, 104", ASM),
 ("nuc Z=89",       "0.27480",           AMD),
 ("nuc Z=120",      "11.61091",          AMD),
]
# claims whose source is a different pack (checked for presence in statement only,
# with the source named in the statement's own text)
PRESENT_ONLY = ["253 mHa", "184 mHa", "2, 8, 8, 18, 18, 32", "107 scored",
                "16 of 16", "13 of 13", "49 mHa", "2,8,8,36,32,32"]
# claims that MUST NOT appear (boundary rule, F75.1/F75.2)
FORBIDDEN = ["119 rows", "119 steps", "18, 32, 32", "zero inversions in 119"]

def run(text):
    fails = []
    for label, needle, src in CLAIMS:
        if needle not in text:
            fails.append(f"MISSING IN STATEMENT: {label} = {needle}")
            continue
        s = open(src).read()
        if needle not in s:
            fails.append(f"UNSOURCED: {label} = {needle} not in {os.path.basename(src)}")
    for needle in PRESENT_ONLY:
        if needle not in text:
            fails.append(f"MISSING IN STATEMENT: {needle}")
    for bad in FORBIDDEN:
        if bad in text:
            fails.append(f"BOUNDARY VIOLATION (F75.1/F75.2): '{bad}' present")
    return fails

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        good = open(STMT).read()
        a = run(good)
        b = run(good.replace("-0.5000080791", "-0.5000080792"))   # must fail
        c = run(good + "\nzero inversions in 119 rows\n")          # must fail
        print(f"SELFTEST clean={len(a)} corrupted={len(b)} boundary={len(c)}")
        ok = (len(a) == 0 and len(b) > 0 and len(c) > 0)
        print("CAN-FAIL: " + ("VERIFIED both directions" if ok else "NOT VERIFIED"))
        sys.exit(0 if ok else 4)
    f = run(open(STMT).read())
    print(f"gate75: {len(CLAIMS)+len(PRESENT_ONLY)} claims checked, {len(f)} failures")
    for x in f: print("  " + x)
    sys.exit(0 if not f else 1)