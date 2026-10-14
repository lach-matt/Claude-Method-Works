#!/usr/bin/env python3
"""DOCKET 67 re-audit 2: icrp-reference-adult-and-ci-chondrite, ICRP 23 Chapter 2 READ.

Source read: ICRP Publication 23 (1975), Chapter 2, pp.273-334, as the OCR text layer of
M's Drive .docx 16DVXUYgP--2YmXOP4VaAguXyIY_rWqM9 (downloaded here, md5
09a25adf33de8b2997bf9e355a115746; word/ holds document.xml only -- no media, no w:tbl, so
no page images to read).  Table 110 (pp.327-328, 'REFERENCE MAN: TOTAL BODY CONTENT FOR
SOME ELEMENTS', transferred per its own preamble 'from the first row of Table 108') is
read below.  Table 108 itself (pp.289-324) is unreadable in this OCR: no element name
survives in the text of those pages.

The owner's tables are imported read-only from research/warp-drive/stockgate.py
(sys.dont_write_bytecode, so nothing is written into the repository).
"""
import sys, math
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import stockgate as sg  # noqa: E402

# ---------------------------------------------------------------- ICRP 23 Table 110, READ
# (value_g, qualifier, page, ocr_note).  qualifier '<' = printed as an upper limit.
# Percent-of-body column printed beside each (READ) is kept to cross-check alignment.
T110 = {
    "O":  (43000, "",  327, 61),      "C":  (16000, "",  327, 23),
    "H":  (7000,  "",  327, 10),      # OCR prints '7O0O'; percent 10 = 7000/70000
    "N":  (1800,  "",  327, 2.6),     "Ca": (1000,  "",  327, 1.4),
    "P":  (780,   "",  327, 1.1),     "S":  (140,   "",  327, 0.20),
    "K":  (140,   "",  327, 0.20),    "Na": (100,   "",  327, 0.14),
    "Cl": (95,    "",  327, 0.12),    # 95/70000 = 0.136 %: printed 0.12 -- see below
    "Mg": (19,    "",  327, 0.027),   "Si": (18,    "",  327, 0.026),  # '(a) From Chapter 3'
    "Fe": (4.2,   "",  327, 0.006),   "F":  (2.6,   "",  327, 0.0037),
    "Zn": (2.3,   "",  327, 0.0033),  "Rb": (0.32,  "",  327, 0.00046),
    "Sr": (0.32,  "",  328, 0.00046), "Br": (0.20,  "",  328, 0.00029),
    "Pb": (0.12,  "",  328, 0.00017), "Cu": (0.072, "",  328, 0.00010),
    "Al": (0.061, "",  328, 0.00009), "Cd": (0.050, "",  328, 0.00007),
    "B":  (0.048, "<", 328, 0.00007), "Ba": (0.022, "",  328, 0.00003),
    "Sn": (0.017, "<", 328, 0.00002), "Mn": (0.012, "",  328, 0.00002),
    "I":  (0.013, "",  328, 0.00002), "Ni": (0.010, "",  328, 0.00001),
    "Au": (0.010, "<", 328, 0.00001), "Mo": (0.0093, "<", 328, 0.00001),
    "Cr": (0.0018, "<", 328, 0.000003), "Cs": (0.0015, "", 328, 0.000002),
    "Co": (0.0015, "", 328, 0.000002), "U":  (0.00009, "", 328, 0.0000001),
    "Be": (0.000036, "", 328, None),  # percent cell not returned by OCR
    "Ra": (3.1e-11, "", 328, None),   # printed '3.1 x 10^-11', OCR '3.1 • 10 -it'
}
ICRP_TOTAL_BODY_G = 70000  # Table 105 row 1 (p.280) and Table 109 'Total body* 70,000* 100' (p.327)

OWNER = {}
OWNER.update(sg.HUMAN_G_BULK); OWNER.update(sg.HUMAN_G_ESSENTIAL_TRACE)
OWNER.update(sg.HUMAN_G_INCIDENTAL)

fails = []
def chk(name, ok):
    print(("  PASS " if ok else "  FAIL ") + name)
    if not ok:
        fails.append(name)

print("=" * 78)
print("1. TABLE 110 INTERNAL CONSISTENCY (amount vs printed percent of 70,000 g)")
for e, (g, q, pg, pct) in T110.items():
    if pct is None:
        continue
    calc = 100 * g / ICRP_TOTAL_BODY_G
    # printed percent is rounded to 2 s.f. (or to 1e-5 / 1e-6 / 1e-7 at the tail)
    ok = abs(calc - pct) <= max(0.06 * pct, 0.5e-5 if pct < 1e-4 else 0) + 1e-12
    if not ok:
        print("   %-2s %10g g -> %.5g %% computed; printed %g %%  <-- MISMATCH" % (e, g, calc, pct))
s110 = sum(v[0] for v in T110.values())
print("   sum of Table 110 amounts = %.4f g against total body 70,000 g (rounding, p.273-274)" % s110)
chk("Cl is the only amount/percent mismatch in Table 110",
    [e for e, (g, q, pg, pct) in T110.items() if pct is not None and
     abs(100*g/ICRP_TOTAL_BODY_G - pct) > max(0.06*pct, 0.5e-5 if pct < 1e-4 else 0) + 1e-12] == ["Cl"])

print("=" * 78)
print("2. OWNER (stockgate.py:345-366, 59 elements) AGAINST ICRP 23 TABLE 110")
same, diff, absent = [], [], []
for e in sorted(OWNER, key=lambda k: -OWNER[k]):
    if e not in T110:
        absent.append(e); continue
    g, q, pg, _ = T110[e]
    r = OWNER[e] / g
    tag = "AGREES" if abs(r - 1) < 1e-9 else ("x%.3g" % r)
    (same if tag == "AGREES" else diff).append(e)
    print("   %-2s owner %-9g ICRP %s%-9g p.%d  %s" % (e, OWNER[e], q, g, pg, tag))
print("   owner elements not in Table 110 (%d): %s" % (len(absent), " ".join(absent)))
print("   Table 110 elements not in owner: %s" % " ".join(e for e in T110 if e not in OWNER))
print("   agree %d, differ %d, absent %d" % (len(same), len(diff), len(absent)))
chk("all 11 bulk elements agree exactly", all(OWNER[e] == T110[e][0] for e in sg.HUMAN_G_BULK))
chk("Li is NOT in Table 110", "Li" not in T110)
s_owner = sum(OWNER.values())
print("   owner sum %.4f g (normalising denominator); ICRP total body %d g" % (s_owner, ICRP_TOTAL_BODY_G))

print("=" * 78)
print("3. BINDERS (owner's processing_factor, max_e p_e/s_e) UNDER EACH PAYLOAD")
CI = sg.DESTS["CI chondrite"](); PH = sg.DESTS["stellar photosphere"]()

def ranked(p, s, n=3):
    f = {e: (math.inf if s.get(e, 0) <= 0 else p[e]/s[e]) for e in p}
    return sorted(f.items(), key=lambda kv: -kv[1])[:n]

def show(label, p):
    out = {}
    for dn, s in (("CI", CI), ("photosphere", PH)):
        r = ranked(p, s)
        out[dn] = r
        print("   %-46s %-11s %s" % (label, dn, "  ".join("%s %.5g" % kv for kv in r)))
    return out

pay_owner = sg.payload("as-composed")
A = show("(a) owner as-composed 59", pay_owner)
chk("(a) reproduces D25: CI P 10.70, photosphere P 1911",
    A["CI"][0][0] == "P" and abs(A["CI"][0][1] - 10.70115) < 1e-4 and
    A["photosphere"][0][0] == "P" and abs(A["photosphere"][0][1] - 1910.87) < 0.01)

# (b) owner 59 with every Table 110 value substituted; '<' taken at the printed limit
b = dict(OWNER)
for e in b:
    if e in T110:
        b[e] = T110[e][0]
B = show("(b) owner 59, Table 110 substituted, renorm", sg._norm(b))
B70 = show("(b') same, per ICRP 70,000 g", {e: v / ICRP_TOTAL_BODY_G for e, v in b.items()})

# (c) Table 110 ALONE.  Ra excluded: neither destination column carries it (inf artefact).
t = {e: v[0] for e, v in T110.items() if e != "Ra"}
C = show("(c) ICRP Table 110 alone (35, '<' at limit)", {e: v / ICRP_TOTAL_BODY_G for e, v in t.items()})
t0 = {e: v[0] for e, v in T110.items() if e != "Ra" and v[1] != "<"}
C0 = show("(c') Table 110 alone, '<' rows dropped", {e: v / ICRP_TOTAL_BODY_G for e, v in t0.items()})

# (d) owner 59 with Li removed (Li is not an ICRP 23 Table 110 value)
d = {e: v for e, v in OWNER.items() if e != "Li"}
D = show("(d) owner 58, Li removed", sg._norm(d))

for lab, res in (("b", B), ("b'", B70), ("c", C), ("c'", C0), ("d", D)):
    chk("(%s) CI binder P, N second" % lab, res["CI"][0][0] == "P" and res["CI"][1][0] == "N")
    chk("(%s) photosphere binder P" % lab, res["photosphere"][0][0] == "P")
chk("(c) photosphere runner-up is K, not Li (Li absent from ICRP)", C["photosphere"][1][0] == "K")

print("=" * 78)
print("4. FLIP MARGINS ON THE ICRP-PRINTED VALUES (owner's destination tables held fixed)")
fP_ph = PH["P"]; fLi_ph = PH["Li"]; fN_ci = CI["N"]; fP_ci = CI["P"]
# photosphere: Li binds iff Li_g/s_Li > P_g/s_P  <=>  Li_g > P_g * s_Li/s_P
li_star = 780 * fLi_ph / fP_ph
P_star_ph = OWNER["Li"] * fP_ph / fLi_ph
P_star_ci = 1800 * fP_ci / fN_ci
N_star_ci = 780 * fN_ci / fP_ci
print("   photosphere: Li binds above %.4f mg at ICRP P 780 g (owner Li 7 mg; ICRP prints none)" % (1e3 * li_star))
print("   photosphere: P loses to owner's 7 mg Li below %.2f g (ICRP 780; 2-s.f. interval 775-785)" % P_star_ph)
print("   CI:          P loses to N below %.2f g at ICRP N 1800 (ICRP P 780)" % P_star_ci)
print("   CI:          N binds above %.1f g at ICRP P 780 (ICRP N 1800; interval 1750-1850)" % N_star_ci)
print("   CI margin N/P factor = %.4f ; ratio needed to flip = x%.4f in N" % (
      (1800/fN_ci)/(780/fP_ci), N_star_ci/1800))
chk("ICRP rounding interval of P (775-785 g) does not reach either P threshold",
    775 > P_star_ph and 775 > P_star_ci)
chk("ICRP rounding interval of N (1750-1850 g) does not reach the CI N threshold", 1850 < N_star_ci)
chk("Li threshold 7.6288 mg", abs(1e3*li_star - 7.6288) < 1e-3)

print("=" * 78)
print("5. stockgate DOCSTRING FIGURES THAT NAME ICRP")
chk("N 1800/70085.9 = 0.02568 (stockgate.py:97)", abs(1800/s_owner - 0.025683) < 1e-6)
chk("P 780/70085.9 = 0.011129 (stockgate.py:97)", abs(780/s_owner - 0.011129) < 1e-6)
chk("ICRP K 140 g = half of stock.py's 280 g (stockgate.py:85)", T110["K"][0] == 140)
chk("lead 120 mg (stockgate.py:47) = Table 110 Pb 0.12 g", T110["Pb"][0] == 0.12)
print("   P as ICRP prints it: 1.1 %% of body; per 70,000 g = %.5f %%; per owner sum = %.5f %%" % (
      100*780/70000, 100*780/s_owner))
print("=" * 78)
print("RESULT:", "ALL PASS" if not fails else "FAILURES: %s" % fails)
sys.exit(1 if fails else 0)
