#!/usr/bin/env python3
"""DOCKET 67 audit re-derivation for arXiv:0909.0948 (Asplund, Grevesse, Sauval & Scott 2009, Table 1).

Reads stockgate.py / stock.py READ-ONLY (bytecode writing disabled, nothing under research/ is written).
Checks:
  C1  every A09 value the tree carries against Table 1 as READ at alphaXiv (0909.0948v1 p.42)
  C2  the tree's headline numbers are reproduced from those values
  C3  the P-vs-Li binder identity: exact dex criterion (normalisation cancels), A09 error bars,
      and every later compilation read here (AAG21 2105.01661, C11 via 2608.23155, L25 2502.10575,
      AG26 2608.23155)
  C4  full substitution of AAG21 Table 2 and AG26 Table 3 into the tree's hybrid column
  C5  the 'largest dex gap in the table' claim against the full published Table 1
  C6  the 'protosolar / meteoritic' label, and the gas-giant Li, as computed destinations
  C7  X, Y, Z of the tree's 62-element hybrid against A09 sec 3.12
"""
import sys, math, random
sys.dont_write_bytecode = True
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)
import stockgate as sg   # read-only import
import stock as sp       # read-only import

# ---- A09 Table 1 as READ (photosphere, meteorites); None = dash in the table.  0909.0948v1 p.42
T1 = {
 "H": (12.00, 8.22), "He": (10.93, 1.29), "Li": (1.05, 3.26), "Be": (1.38, 1.30), "B": (2.70, 2.79),
 "C": (8.43, 7.39), "N": (7.83, 6.26), "O": (8.69, 8.40), "F": (4.56, 4.42), "Ne": (7.93, -1.12),
 "Na": (6.24, 6.27), "Mg": (7.60, 7.53), "Al": (6.45, 6.43), "Si": (7.51, 7.51), "P": (5.41, 5.43),
 "S": (7.12, 7.15), "Cl": (5.50, 5.23), "Ar": (6.40, -0.50), "K": (5.03, 5.08), "Ca": (6.34, 6.29),
 "Sc": (3.15, 3.05), "Ti": (4.95, 4.91), "V": (3.93, 3.96), "Cr": (5.64, 5.64), "Mn": (5.43, 5.48),
 "Fe": (7.50, 7.45), "Co": (4.99, 4.87), "Ni": (6.22, 6.20), "Cu": (4.19, 4.25), "Zn": (4.56, 4.63),
 "Ga": (3.04, 3.08), "Ge": (3.65, 3.58), "As": (None, 2.30), "Se": (None, 3.34), "Br": (None, 2.54),
 "Kr": (3.25, -2.27), "Rb": (2.52, 2.36), "Sr": (2.87, 2.88), "Y": (2.21, 2.17), "Zr": (2.58, 2.53),
 "Nb": (1.46, 1.41), "Mo": (1.88, 1.94), "Ru": (1.75, 1.76), "Rh": (0.91, 1.06), "Pd": (1.57, 1.65),
 "Ag": (0.94, 1.20), "Cd": (None, 1.71), "In": (0.80, 0.76), "Sn": (2.04, 2.07), "Sb": (None, 1.01),
 "Te": (None, 2.18), "I": (None, 1.55), "Xe": (2.24, -1.95), "Cs": (None, 1.08), "Ba": (2.18, 2.18),
 "La": (1.10, 1.17), "Ce": (1.58, 1.58), "Pr": (0.72, 0.76), "Nd": (1.42, 1.45), "Sm": (0.96, 0.94),
 "Eu": (0.52, 0.51), "Gd": (1.07, 1.05), "Tb": (0.30, 0.32), "Dy": (1.10, 1.13), "Ho": (0.48, 0.47),
 "Er": (0.92, 0.92), "Tm": (0.10, 0.12), "Yb": (0.84, 0.92), "Lu": (0.10, 0.09), "Hf": (0.85, 0.71),
 "Ta": (None, -0.12), "W": (0.85, 0.65), "Re": (None, 0.26), "Os": (1.40, 1.35), "Ir": (1.38, 1.32),
 "Pt": (None, 1.62), "Au": (0.92, 0.80), "Hg": (None, 1.17), "Tl": (0.90, 0.77), "Pb": (1.75, 2.04),
 "Bi": (None, 0.65), "Th": (0.02, 0.06), "U": (None, -0.54),
}
SIG = {"Li": 0.10, "P": 0.03, "K": 0.09}   # A09 Table 1 quoted 1-sigma

# ---- AAG21 Table 2 (2105.01661v2 p.6): (photosphere, CI) for the tree's 62 elements
AAG21 = {
 "H": (12.00, 8.22), "He": (10.914, 1.29), "Li": (0.96, 3.25), "Be": (1.38, 1.32), "B": (2.70, 2.79),
 "C": (8.46, 7.39), "N": (7.83, 6.26), "O": (8.69, 8.39), "F": (4.40, 4.42), "Ne": (8.06, -1.12),
 "Na": (6.22, 6.27), "Mg": (7.55, 7.53), "Al": (6.43, 6.43), "Si": (7.51, 7.51), "P": (5.41, 5.43),
 "S": (7.12, 7.15), "Cl": (5.31, 5.23), "Ar": (6.38, -0.50), "K": (5.07, 5.08), "Ca": (6.30, 6.29),
 "Sc": (3.14, 3.04), "Ti": (4.97, 4.90), "V": (3.90, 3.96), "Cr": (5.62, 5.63), "Mn": (5.42, 5.47),
 "Fe": (7.46, 7.46), "Co": (4.94, 4.87), "Ni": (6.20, 6.20), "Cu": (4.18, 4.25), "Zn": (4.56, 4.61),
 "Ga": (3.02, 3.07), "Ge": (3.62, 3.58), "As": (None, 2.30), "Se": (None, 3.34), "Br": (None, 2.54),
 "Rb": (2.32, 2.37), "Sr": (2.83, 2.88), "Y": (2.21, 2.15), "Zr": (2.59, 2.53), "Nb": (1.47, 1.42),
 "Mo": (1.88, 1.93), "Ag": (0.96, 1.20), "Cd": (None, 1.71), "In": (0.80, 0.76), "Sn": (2.02, 2.07),
 "Sb": (None, 1.01), "Te": (None, 2.18), "I": (None, 1.55), "Cs": (None, 1.08), "Ba": (2.27, 2.18),
 "La": (1.11, 1.17), "Ce": (1.58, 1.58), "Nd": (1.42, 1.45), "Sm": (0.95, 0.94), "W": (0.79, 0.65),
 "Au": (0.91, 0.81), "Hg": (None, 1.17), "Tl": (0.92, 0.77), "Pb": (1.95, 2.03), "Bi": (None, 0.65),
 "Th": (0.03, 0.04), "U": (None, -0.54), "Ta": (None, -0.15),
}
# ---- AG26 Table 3 (2608.23155v1 p.24): one recommended present-day value (photosphere or CI-Tc)
AG26 = {"H": 12.0, "He": 10.934, "Li": 0.96, "Be": 1.21, "B": 2.70, "C": 8.47, "N": 7.84, "O": 8.70,
 "F": 4.40, "Ne": 8.07, "Na": 6.22, "Mg": 7.56, "Al": 6.43, "Si": 7.55, "P": 5.35, "S": 7.06, "Cl": 5.31,
 "Ar": 6.38, "K": 5.07, "Ca": 6.30, "Sc": 3.13, "Ti": 4.97, "V": 3.90, "Cr": 5.65, "Mn": 5.47, "Fe": 7.46,
 "Co": 4.94, "Ni": 6.20, "Cu": 4.18, "Zn": 4.56, "Ga": 3.02, "Ge": 3.62, "As": 2.29, "Se": 3.32, "Br": 2.55,
 "Rb": 2.34, "Sr": 2.84, "Y": 2.29, "Zr": 2.59, "Nb": 1.47, "Mo": 1.88, "Ag": 1.15, "Cd": 1.66, "In": 0.80,
 "Sn": 2.02, "Sb": 1.01, "Te": 2.14, "I": 1.66, "Cs": 1.03, "Ba": 2.27, "La": 1.12, "Ce": 1.58, "Nd": 1.42,
 "Sm": 0.95, "W": 0.79, "Au": 0.91, "Hg": 1.04, "Tl": 0.92, "Pb": 1.95, "Bi": 0.61, "Th": 0.03, "U": -0.52,
 "Ta": -0.14}
# ---- (Li, P) photospheric pairs from every compilation READ here
PAIRS = {"A09 (0909.0948 Table 1)": (1.05, 5.41),
         "AAG21 (2105.01661 Table 2)": (0.96, 5.41),
         "C11 (as restated in 2608.23155 pp.23,32)": (1.03, 5.46),
         "L25 (2502.10575 Table 2)": (1.04, 5.44),
         "AG26 (2608.23155 Table 3)": (0.96, 5.35)}

AM = sg.ATOMIC_MASS
out = []
def say(s=""):
    print(s); out.append(s)
ok_all = True
def chk(label, cond):
    global ok_all
    ok_all &= bool(cond)
    say("  [%s] %s" % ("ok" if cond else "FAIL", label))

def hybrid(tab, keys):
    n = {}
    for e in keys:
        v = tab[e]
        if isinstance(v, tuple):
            v = v[0] if v[0] is not None else v[1]
        if v is not None:
            n[e] = 10.0 ** (v - 12.0) * AM[e]
    t = sum(n.values())
    return {e: x / t for e, x in n.items()}

def bind(p, s):
    f = {e: (p[e] / s[e]) if s.get(e, 0) > 0 else float("inf") for e in p}
    r = sorted(f.items(), key=lambda kv: -kv[1])
    return r

P59 = sg.payload("as-composed")
KEYS = list(sg.A09.keys())

say("C1  transcription: every tree value vs A09 Table 1 as READ")
mism = []
for e, (ph, me) in sg.A09.items():
    tph, tme = T1[e]
    if ph != tph or me != tme:
        mism.append((e, (ph, me), (tph, tme)))
for e, v in sp.A09.items():
    if v != T1[e][0]:
        mism.append(("stock.py:" + e, v, T1[e][0]))
for m in mism:
    say("    DISCREPANCY %-12s tree=%s  Table1=%s" % m)
chk("stockgate carries %d elements; photospheric column identical to Table 1 for all" % len(sg.A09),
    all(sg.A09[e][0] == T1[e][0] for e in sg.A09))
chk("meteoritic column identical except Ne, Ar (tree None; Table 1 -1.12, -0.50)",
    sorted(m[0] for m in mism) == ["Ar", "Ne"])
chk("stock.py's 18 photospheric values identical to Table 1", all(sp.A09[e] == T1[e][0] for e in sp.A09))
nophot = sorted(e for e in sg.A09 if T1[e][0] is None)
chk("the 12 no-photospheric elements the tree names are exactly Table 1's dashes among its 62: %s" % nophot,
    set(nophot) == {"As", "Se", "Br", "Cd", "Sb", "Te", "I", "Cs", "Hg", "Bi", "U", "Ta"})

say("\nC2  reproduce the tree's headline numbers from the Table 1 values")
s09 = hybrid(T1, KEYS)
r = bind(P59, s09)
say("    human(59) vs A09 hybrid: %s %.2f, %s %.2f (ratio %.5f), %s %.2f (P/3rd %.4f)"
    % (r[0][0], r[0][1], r[1][0], r[1][1], r[1][1] / r[0][1], r[2][0], r[2][1], r[0][1] / r[2][1]))
chk("P binds at 1910.87 (stockgate selftest fixture; ledger D25)", r[0][0] == "P" and abs(r[0][1] - 1910.87) < 0.01)
chk("Li runner-up at 0.91758 of P", r[1][0] == "Li" and abs(r[1][1] / r[0][1] - 0.91758) < 1e-5)
chk("Ne/Ar meteoritic omission does not move it (hybrid uses photospheric Ne, Ar)",
    abs(bind(P59, sg.solar_hybrid())[0][1] - r[0][1]) < 1e-9)
sp_b = sp.binding_element()
chk("stock.py cosmic(): P at %.1f (fixture 1910.5)" % sp_b[1], sp_b[0] == "P" and abs(sp_b[1] - 1910.5) < 0.1)
c = sp.cosmic()
chk("P/Li photospheric mass-fraction ratio %.4g (tree 1.02e5)" % (c["P"] / c["Li"]), abs(c["P"] / c["Li"] / 1.02e5 - 1) < 0.005)
dex = T1["Li"][1] - T1["Li"][0]
chk("Li gap %.2f dex = %.2fx (tree 2.21, 162)" % (dex, 10 ** dex), abs(dex - 2.21) < 1e-9 and abs(10 ** dex - 162.18) < 0.01)

say("\nC3  the binder identity P vs Li -- exact criterion")
# f_Li/f_P = (p_Li/p_P) * 10^(P-Li) * (m_P/m_Li): normalisation of the stock cancels exactly
k = (P59["Li"] / P59["P"]) * (AM["P"] / AM["Li"])
thr = math.log10(1.0 / k)        # Li binds iff (P - Li) > thr, i.e. Li - P < -thr
say("    Li overtakes P iff  log eps(Li) - log eps(P) < %.4f  (A09 value: %.2f)" % (-thr, 1.05 - 5.41))
say("    margin at A09: %.4f dex; A09 quoted sigma(Li)=0.10, sigma(P)=0.03" % ((1.05 - 5.41) + thr))
z = ((1.05 - 5.41) + thr) / math.hypot(SIG["Li"], SIG["P"])
pli = 0.5 * math.erfc(z / math.sqrt(2))
random.seed(67)
N = 200000
mc = sum(1 for _ in range(N) if (random.gauss(1.05, .10) - random.gauss(5.41, .03)) < -thr) / N
say("    P(Li binds | A09's own Gaussian errors) = %.4f analytic, %.4f MC (N=%d)" % (pli, mc, N))
chk("the A09 margin (0.037 dex) is smaller than A09's own sigma(Li) = 0.10", (1.05 - 5.41) + thr < 0.10)
for name, (li, p) in PAIRS.items():
    ratio = k * 10 ** (p - li)
    say("    %-42s Li=%.2f P=%.2f  f_Li/f_P = %.4f  -> binder %s" % (name, li, p, ratio, "Li" if ratio > 1 else "P"))
binders = {n: ("Li" if k * 10 ** (p - li) > 1 else "P") for n, (li, p) in PAIRS.items()}
chk("compilations disagree on the binder (contested datum)", len(set(binders.values())) == 2)

say("\nC4  full-table substitution into the tree's hybrid construction, same 59-element payload")
for name, tab in (("A09", T1), ("AAG21", AAG21), ("AG26", AG26)):
    s = hybrid(tab, KEYS)
    rr = bind(P59, s)
    say("    %-6s X=%.5f  binder %s %.1f  2nd %s %.1f  (2nd/1st %.4f)  70 kg -> %.1f t"
        % (name, s["H"], rr[0][0], rr[0][1], rr[1][0], rr[1][1], rr[1][1] / rr[0][1], 70 * rr[0][1] / 1000))
    craft = bind(sg._norm(sg.CRAFT), s)[0]
    say("           craft binder %s %.4e" % craft)
rr21 = bind(P59, hybrid(AAG21, KEYS)); rr26 = bind(P59, hybrid(AG26, KEYS))
chk("AAG21: binder flips to Li", rr21[0][0] == "Li")
chk("AG26: binder P, Li within 2%", rr26[0][0] == "P" and rr26[1][0] == "Li" and rr26[1][1] / rr26[0][1] > 0.98)
chk("magnitude stays within 1.6e3..2.4e3 kg/kg on every table", all(1.6e3 < x[0][1] < 2.4e3 for x in (r, rr21, rr26)))

say("\nC5  'the largest such gap in the table' against Table 1 as published")
gaps = sorted(((abs(ph - me), e) for e, (ph, me) in T1.items() if ph is not None and me is not None), reverse=True)
say("    top |ph-met|: " + ", ".join("%s %.2f" % (e, g) for g, e in gaps[:9]))
defic = sorted(((ph - me), e) for e, (ph, me) in T1.items() if ph is not None and me is not None)
say("    largest photospheric DEFICIT (ph<met): " + ", ".join("%s %.2f" % (e, d) for d, e in defic[:4]))
chk("literal claim FALSE on the published table (He, Ne, Ar, Kr, Xe, H exceed Li)", gaps[0][1] != "Li")
chk("true as 'largest photospheric deficit' (Li -2.21, next Pb -0.29)", defic[0][1] == "Li" and defic[1][0] > -0.3)
chk("tree's largest_dex_gap() returns Li only because Ne/Ar meteoritic are None and H/He excluded",
    sg.largest_dex_gap()[0] == "Li")

say("\nC6  labels of destinations as computed")
met = sg.solar("meteoritic")
say("    'solar meteoritic' column mass fractions: H %.4f O %.3f Fe %.3f Si %.3f -> a CI-chondrite rock, not protosolar gas"
    % (met["H"], met["O"], met["Fe"], met["Si"]))
chk("meteoritic column is volatile-depleted (H mass fraction < 0.05)", met["H"] < 0.05)
# a protosolar stock per A09 sec 3.11: photospheric H; He +0.05; volatiles C N O Ne Ar +0.04; refractories = meteoritic +0.04
proto = {}
for e in KEYS:
    ph, me = T1[e]
    if e == "H": v = 12.0
    elif e == "He": v = ph + 0.05
    elif e in ("C", "N", "O", "Ne", "Ar"): v = ph + 0.04
    else: v = (me if me is not None else ph) + 0.04
    proto[e] = 10 ** (v - 12) * AM[e]
t = sum(proto.values()); proto = {e: x / t for e, x in proto.items()}
rp = bind(P59, proto)
say("    protosolar (A09 sec 3.11 construction): binder %s %.1f, Li %.2f" % (rp[0][0], rp[0][1], dict(rp)["Li"]))
say("    tree's 'protosolar / meteoritic' Li = %.4f is the CI-rock figure (binder %s %.2f)" % ((dict(bind(P59, met))["Li"],) + bind(P59, met)[0]))
chk("a genuine protosolar stock binds on P with Li far behind (Li not burned)", rp[0][0] == "P" and dict(rp)["Li"] < 50)
jup = bind(P59, sg.jupiter_hybrid())
jl = {}
for e in KEYS:
    ph, me = T1[e]
    v = me if e == "Li" else (ph if ph is not None else me)
    jl[e] = 10 ** (v - 12) * AM[e] * (1 if e in ("H", "He") else 3.0)
t = sum(jl.values()); jl = {e: x / t for e, x in jl.items()}
jr = bind(P59, jl)
say("    Jupiter as the tree builds it (photospheric Li x3): %s %.1f, Li/P %.4f" % (jup[0][0], jup[0][1], dict(jup)["Li"] / jup[0][1]))
say("    Jupiter with unburned (meteoritic) Li x3:          %s %.1f, Li/P %.4f" % (jr[0][0], jr[0][1], dict(jr)["Li"] / jr[0][1]))

say("\nC7  X, Y, Z of the tree's 62-element hybrid vs A09 sec 3.12 (X=0.7381, Y=0.2485, Z=0.0134)")
X, Y = s09["H"], s09["He"]; Z = 1 - X - Y
say("    tree hybrid X=%.4f Y=%.4f Z=%.4f" % (X, Y, Z))
chk("agrees with A09's X, Y, Z to 0.001 absolute", abs(X - .7381) < 1e-3 and abs(Y - .2485) < 1e-3 and abs(Z - .0134) < 1e-3)

say("\nRESULT: %s" % ("ALL CHECKS AS STATED" if ok_all else "SOME CHECK FAILED"))
