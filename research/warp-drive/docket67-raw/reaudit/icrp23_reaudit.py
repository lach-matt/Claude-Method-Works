"""DOCKET 67 re-audit: ICRP Publication 23 (1975) from M's Drive copy
(fileId 1BZAg4Dncc5sTu00aTRPr7uBUvtT5awH-).  The Drive text extraction
returned front matter, contents (pp.v-xix), Introduction pp.1-7 and Chapter 1
pp.8-61 only.  Chapter 2 (Gross and Elemental Content, pp.273-334) was NOT
returned, so no elemental mass below is checked against ICRP 23.  What is
checked: the body mass (p.13), and the tree's own arithmetic.
Imports the tree READ-ONLY.
"""
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import stockgate as sg
import stock as st

FAIL = []
def chk(label, ok):
    print(("  PASS " if ok else "  FAIL ") + label)
    if not ok: FAIL.append(label)

# READ at source (ICRP 23 p.13): "Weight of total body for reference adult
# male: 70 kg  female: 58 kg".  p.4: "Reference Man is defined as being between
# 20-30 years of age, weighing 70 kg, is 170 cm in height ..."
ICRP23_MALE_KG, ICRP23_FEMALE_KG = 70.0, 58.0
# READ at source (ICRP 23 p.24, adult gross composition, % of W):
ICRP23_ADULT_GROSS = {"water": 60, "fat": 19, "protein": "15-20", "ash": "4.8-5.8",
                      "mineral": 5.8, "carbohydrate": 0.6, "blood": 7.9}

g = {}
for t in (sg.HUMAN_G_BULK, sg.HUMAN_G_ESSENTIAL_TRACE, sg.HUMAN_G_INCIDENTAL):
    g.update(t)
tot = sum(g.values())
print("=== 1. tree payload table")
print("  59-row total %.1f g (%d rows); ICRP 23 reference male %.0f kg" % (tot, len(g), ICRP23_MALE_KG * 1000 / 1000))
chk("the tree's 70 kg equals ICRP 23's reference adult MALE body mass (p.13)",
    abs(tot / 1000 - ICRP23_MALE_KG) / ICRP23_MALE_KG < 0.002)
print("  female reference adult (p.13) = 58 kg: feedstock at the CI factor would be %.1f kg (not a tree figure)"
      % (58 * sg.binding_under("as-composed 59", "CI chondrite")[1]))
p = sg.payload("as-composed")
print("  N frac %.6f  P frac %.6f  K g at 70 kg %.2f" % (p["N"], p["P"], p["K"] * 70000))
chk("stock.HUMAN equals the 59-row fractions to 6 dp",
    all(abs(st.HUMAN[e] - round(p[e], 6)) < 2e-6 for e in st.HUMAN if e != "Li"))

print("\n=== 2. tree binders (reproduced)")
for d in ("CI chondrite", "stellar photosphere"):
    r = sg.ranked(p, sg.DESTS[d](), 3)
    print("  %-20s %s" % (d, ", ".join("%s %.5g" % kv for kv in r)))
ec, fc = sg.binding_under("as-composed 59", "CI chondrite")
ep, fp = sg.binding_under("as-composed 59", "stellar photosphere")
chk("CI P 10.70, photosphere P 1910.9", ec == "P" and ep == "P" and abs(fp - 1910.87) < 0.1)

print("\n=== 3. flip thresholds by bisection (renormalised)")
def factor_with(e, grams, dest):
    gg = dict(g); gg[e] = grams
    pp = sg.mass_fractions(gg)
    return sg.processing_factor(pp, sg.DESTS[dest]())
def bisect(e, lo, hi, dest, target_binder_changes_from="P"):
    for _ in range(80):
        mid = (lo + hi) / 2
        b, _ = factor_with(e, mid, dest)
        if (b == target_binder_changes_from) == (factor_with(e, lo, dest)[0] == target_binder_changes_from):
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2
li = bisect("Li", 0.007, 0.010, "stellar photosphere")
pp_ = bisect("P", 500.0, 780.0, "stellar photosphere")
pc = bisect("P", 400.0, 780.0, "CI chondrite")
print("  photosphere: Li binds above %.4f mg (x%.4f of 7 mg)" % (li * 1000, li / 0.007))
print("  photosphere: P hands binder to Li below %.1f g (x%.4f of 780 g)" % (pp_, pp_ / 780))
print("  CI chondrite: P hands binder to N below %.1f g (x%.4f)" % (pc, pc / 780))
chk("thresholds reproduce the first audit (7.629 mg, 715.7 g, 588.7 g)",
    abs(li * 1000 - 7.629) < 0.01 and abs(pp_ - 715.7) < 0.2 and abs(pc - 588.7) < 0.2)
print("\nFAILS:", FAIL)
sys.exit(1 if FAIL else 0)
