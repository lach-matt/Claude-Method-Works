"""DOCKET 67 re-audit 2: ICRP Publication 23 (1975) Chapter 2 against the tree.

Source read: OCR text layer of ICRP 23 pp.273-334 (M's .docx, Drive
16DVXUYgP--2YmXOP4VaAguXyIY_rWqM9, 79,841 bytes, md5 09a25adf33de8b2997bf9e355a115746;
the .docx holds word/document.xml and no word/media -- no page images).
Text saved at reaudit/src/icrp23_p273-334_docx.txt.

TABLE 110 'REFERENCE MAN: TOTAL BODY CONTENT FOR SOME ELEMENTS', pp.327-328,
is READ: 36 rows, each with grams and per cent of total body weight.  Its
caption (p.327): 'The values in Table 110 have been transferred from the first
row of Table 108 ... Table 110 includes only those elements for which the
concentration was known in at least 50 % of the total body, including the
skeleton.'  TABLE 108 itself (pp.289-324, landscape, E-notation) is NOT
readable in the OCR layer; no value is taken from it.  Table 106/107 have no
readable heading or body in the layer.

The per-cent column is used as an INDEPENDENT cross-check on every gram value
(g / 70,000 g x 100, compared at the printed precision).

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
    if not ok:
        FAIL.append(label)

# ---------------------------------------------------------------- READ at source
# (element, grams as printed, '<' flag, percent as printed, page, OCR note)
T110 = [
    ("O", 43000, False, "61", 327, ""),
    ("C", 16000, False, "23", 327, ""),
    ("H", 7000, False, "10", 327, "OCR prints '7O0O'; read as 7000 only via the per-cent column '10'"),
    ("N", 1800, False, "2.6", 327, ""),
    ("Ca", 1000, False, "1.4", 327, ""),
    ("P", 780, False, "1.1", 327, ""),
    ("S", 140, False, "0.20", 327, ""),
    ("K", 140, False, "0.20", 327, ""),
    ("Na", 100, False, "0.14", 327, ""),
    ("Cl", 95, False, "0.12", 327, "OCR row label 'I0. Chlorine'"),
    ("Mg", 19, False, "0.027", 327, ""),
    ("Si", 18, False, "0.026", 327, "footnote (a) 'From Chapter 3'"),
    ("Fe", 4.2, False, "0.006", 327, ""),
    ("F", 2.6, False, "0.0037", 327, ""),
    ("Zn", 2.3, False, "0.0033", 327, ""),
    ("Rb", 0.32, False, "0.00046", 327, ""),
    ("Sr", 0.32, False, "0.00046", 328, ""),
    ("Br", 0.20, False, "0.00029", 328, ""),
    ("Pb", 0.12, False, "0.00017", 328, ""),
    ("Cu", 0.072, False, "0.00010", 328, ""),
    ("Al", 0.061, False, "0.00009", 328, ""),
    ("Cd", 0.050, False, "0.00007", 328, ""),
    ("B", 0.048, True, "0.00007", 328, ""),
    ("Ba", 0.022, False, "0.00003", 328, ""),
    ("Sn", 0.017, True, "0.00002", 328, ""),
    ("Mn", 0.012, False, "0.00002", 328, ""),
    ("I", 0.013, False, "0.00002", 328, ""),
    ("Ni", 0.010, False, "0.00001", 328, ""),
    ("Au", 0.010, True, "0.00001", 328, "per cent OCR '0.0000!'"),
    ("Mo", 0.0093, True, "0.00001", 328, ""),
    ("Cr", 0.0018, True, "0.000003", 328, ""),
    ("Cs", 0.0015, False, "0.000002", 328, ""),
    ("Co", 0.0015, False, "0.000002", 328, ""),
    ("U", 0.00009, False, "0.0000001", 328, ""),
    ("Be", 0.000036, False, None, 328, "no per-cent entry printed"),
    ("Ra", 3.1e-11, False, None, 328, "OCR '3.1 . 10 -it'; read as 3.1e-11 -- AMBIGUOUS exponent"),
]
BODY_G = 70000.0   # Table 109, p.327: 'Total body* 70,000* 100'
# Notes for Table 108, pp.287-288 (READ): alternative whole-body estimates
ALT = {
    "Na": [93, 75, 70, 80],   # Edelman & Leibman; Moore et al.; Forbes; neutron activation
    "K": [136, 133, 145],     # Moore et al. incl. bone; Wilde (exchangeable); 40K counting
    "Cl": [98, 84, 94],       # Moore et al.; Cotlove & Hogben range ends
    "Ca": [1014, 1265],       # this report's unrounded value; Widdowson & Dickerson
    # Iodine: 13 mg 'may exceed'; Mg: 7.8 soft + 11 skeleton = 19 g (worked example)
}

print("=== 1. Table 110 internal consistency (grams vs printed per cent of 70 kg)")
bad = []
for e, gr, lt, pct, pg, note in T110:
    if pct is None:
        continue
    calc = gr / BODY_G * 100
    dec = len(pct.split(".")[1]) if "." in pct else 0
    if abs(round(calc, dec) - float(pct)) > 1.01 * 10 ** (-dec) * 0.5 + 1e-15 and \
       abs(calc - float(pct)) > 10 ** (-dec):
        bad.append((e, gr, pct, calc))
print("  rows with a per-cent entry: %d; inconsistent: %s" % (sum(1 for r in T110 if r[3]), bad))
# RECORDED, not repaired: Cl 95 g is 0.136 % of 70 kg; the OCR per-cent reads '0.12'.
# Whether the scan prints 0.12 (a source discrepancy) or 0.14 (an OCR misread) is
# NOT resolvable from the text layer.  It moves nothing: the gram value is used.
chk("the only gram/per-cent disagreement is Cl (95 g vs '0.12')", [b[0] for b in bad] == ["Cl"])
s_bulk = sum(r[1] for r in T110 if r[0] in sg.HUMAN_G_BULK)
print("  sum of the 11 bulk rows %.0f g; sum of all 36 rows (bounds as printed) %.2f g"
      % (s_bulk, sum(r[1] for r in T110)))

print("\n=== 2. owner table (stockgate.py:345-363, 59 rows) against Table 110")
owner = {}
for t in (sg.HUMAN_G_BULK, sg.HUMAN_G_ESSENTIAL_TRACE, sg.HUMAN_G_INCIDENTAL):
    owner.update(t)
icrp = {r[0]: r for r in T110}
agree, differ, absent = [], [], []
for e in owner:
    if e not in icrp:
        absent.append(e)
        continue
    _, gr, lt, pct, pg, note = icrp[e]
    if not lt and abs(owner[e] - gr) <= 1e-12 + 1e-9 * gr:
        agree.append(e)
    else:
        differ.append((e, owner[e], ("<" if lt else "") + repr(gr), owner[e] / gr))
print("  agree exactly (%d): %s" % (len(agree), " ".join(agree)))
print("  differ (%d):" % len(differ))
for e, o, i, r in differ:
    print("    %-3s owner %-9g ICRP %-9s owner/ICRP %.3g" % (e, o, i, r))
print("  not in Table 110 (%d): %s" % (len(absent), " ".join(absent)))
print("  in Table 110, not in owner: %s" % [e for e in icrp if e not in owner])
chk("all 11 bulk elements agree exactly with Table 110",
    all(e in agree for e in sg.HUMAN_G_BULK))
chk("Li is NOT among Table 110's 36 rows", "Li" not in icrp)

print("\n=== 3. owner's comparisons, owner data (reproduce)")
D = {d: sg.DESTS[d]() for d in sg.DESTS}
p0 = sg.mass_fractions(owner)
for d in ("CI chondrite", "stellar photosphere", "Earth cont. crust"):
    print("  %-20s %s" % (d, ", ".join("%s %.5g" % kv for kv in sg.ranked(p0, D[d], 3))))

def swap(base, repl):
    g = dict(base); g.update(repl); return g

print("\n=== 4. substitute every Table 110 value the owner carries ('<' bound taken as printed)")
sub = {e: icrp[e][1] for e in owner if e in icrp}
p1 = sg.mass_fractions(swap(owner, sub))
res1 = {}
for d in ("CI chondrite", "stellar photosphere", "Earth cont. crust"):
    r = sg.ranked(p1, D[d], 3); res1[d] = r
    print("  %-20s %s" % (d, ", ".join("%s %.5g" % kv for kv in r)))
chk("CI binder is P after substitution", res1["CI chondrite"][0][0] == "P")
chk("photosphere binder is P, runner-up Li, after substitution",
    res1["stellar photosphere"][0][0] == "P" and res1["stellar photosphere"][1][0] == "Li")
ci_margin = res1["CI chondrite"][0][1] / res1["CI chondrite"][1][1]
ph_margin = res1["stellar photosphere"][0][1] / res1["stellar photosphere"][1][1]
print("  CI P/N margin %.4f ; photosphere P/Li margin %.4f (owner: 1.3250, 1.0898)"
      % (ci_margin, ph_margin))

print("\n=== 5. Table 110 ALONE as payload (35 rows; Ra 3.1e-11 g dropped -- no A09 row)")
g110 = {r[0]: r[1] for r in T110 if r[0] != "Ra"}
p2 = sg.mass_fractions(g110)
res2 = {}
for d in ("CI chondrite", "stellar photosphere", "Earth cont. crust"):
    r = sg.ranked(p2, D[d], 3); res2[d] = r
    print("  %-20s %s" % (d, ", ".join("%s %.5g" % kv for kv in r)))
print("  photosphere P / runner-up on Table 110 alone: %.3f" %
      (res2["stellar photosphere"][0][1] / res2["stellar photosphere"][1][1]))

print("\n=== 6. flip thresholds against ICRP-substituted payload")
base = swap(owner, sub)
def binder(e, grams, dest):
    return sg.processing_factor(sg.mass_fractions(swap(base, {e: grams})), D[dest])[0]
def bisect(e, lo, hi, dest):
    b_lo = binder(e, lo, dest)
    for _ in range(80):
        mid = (lo + hi) / 2
        if binder(e, mid, dest) == b_lo: lo = mid
        else: hi = mid
    return (lo + hi) / 2
li = bisect("Li", 0.007, 0.010, "stellar photosphere")
pph = bisect("P", 500.0, 780.0, "stellar photosphere")
pci = bisect("P", 400.0, 780.0, "CI chondrite")
nci = bisect("N", 1800.0, 3000.0, "CI chondrite")
print("  photosphere: Li binds above %.4f mg (x%.4f of 7 mg)" % (li * 1000, li / 0.007))
print("  photosphere: P cedes below %.1f g (x%.4f of ICRP 780 g)" % (pph, pph / 780))
print("  CI: P cedes to N below %.1f g (x%.4f of ICRP 780 g)" % (pci, pci / 780))
print("  CI: N takes over above %.0f g (x%.4f of ICRP 1800 g)" % (nci, nci / 1800))
chk("thresholds unchanged from the prior re-audit to 0.1 % (Li 7.629 mg, P 715.7 g, P 588.7 g)",
    abs(li * 1000 - 7.6288) / 7.6288 < 1e-3 and abs(pph - 715.7) / 715.7 < 1e-3
    and abs(pci - 588.7) / 588.7 < 1e-3)

print("\n=== 7. the source's own alternative whole-body values (notes for Table 108)")
for e, vals in ALT.items():
    for v in vals:
        p = sg.mass_fractions(swap(base, {e: float(v)}))
        out = [sg.processing_factor(p, D[d])[0] for d in ("CI chondrite", "stellar photosphere")]
        print("  %-2s %6g g -> CI binder %s, photosphere binder %s" % (e, v, out[0], out[1]))
        chk("%s %g g leaves both binders P" % (e, v), out == ["P", "P"])
fK = sg.factors(sg.mass_fractions(base), D["stellar photosphere"])
print("  photosphere P/K gap on ICRP K 140 g: %.4f (owner :1008 says 2.632x)" % (fK["P"] / fK["K"]))

sp = sg.solar_hybrid()
gap_mixed = (sg.STOCKPY_HUMAN["P"] / sp["P"]) / ((140.0 / 70000.0) / sp["K"])
print("  owner's 2.632 = stock.py's P 0.010 (NOT ICRP) over ICRP K 140/70000: %.4f" % gap_mixed)
chk("owner's 'On the ICRP datum the gap is 2.63x' (stockgate.py:88) uses stock.py's P, not ICRP's;"
    " all-ICRP gap is 2.93", abs(gap_mixed - 2.632) < 1e-3 and abs(fK["P"] / fK["K"] - 2.932) < 1e-3)

print("\n=== 8. two-significant-figure rounding of P, N (p.273 'rounded to two significant figures')")
for e, lo, hi in (("P", 775, 785), ("N", 1750, 1850)):
    for v in (lo, hi):
        p = sg.mass_fractions(swap(base, {e: float(v)}))
        r = sg.ranked(p, D["CI chondrite"], 2); q = sg.ranked(p, D["stellar photosphere"], 2)
        print("  %s %g g -> CI %s %.4g / %s %.4g ; photo %s %.5g / %s %.5g"
              % (e, v, r[0][0], r[0][1], r[1][0], r[1][1], q[0][0], q[0][1], q[1][0], q[1][1]))
chk("P anywhere in [775, 785) g keeps P binding at both", all(
    sg.processing_factor(sg.mass_fractions(swap(base, {"P": v})), D[d])[0] == "P"
    for v in (775.0, 784.99) for d in ("CI chondrite", "stellar photosphere")))

print("\n=== 9. does any element besides Li reach P at the photosphere? (owner :46 '48 added ... none exceeds P')")
r = sg.ranked(sg.mass_fractions(base), D["stellar photosphere"], 5)
print("  top 5:", ", ".join("%s %.4g" % kv for kv in r))
print("  Si on ICRP 18 g vs owner 1.0 g at the photosphere: %.4g vs %.4g"
      % (sg.factors(sg.mass_fractions(base), D["stellar photosphere"])["Si"],
         sg.factors(p0, D["stellar photosphere"])["Si"]))

print("\nFAILS:", FAIL)
sys.exit(1 if FAIL else 0)
