#!/usr/bin/env python3
# r2-ch14z.py -- computable batch for the chat-103 section read: main L6991-L7116,
# Chapter 25 sections 25.6 through 25.6.6 (the Sc VI deduction), which closes Chapter 25.
# Reads MEMBERS only, never a BUILDnnn bundle path. Imports r2lib by path; copies nothing.
# Rounding: Decimal.quantize with ROUND_HALF_UP throughout, named at each site.
# Rewritten once: the first version compared the volume's "verified" and "tested" claims
# against interior cells, which is not their base. Both bases are now measured and printed.
import importlib.util, re, sys
from decimal import Decimal, ROUND_HALF_UP

spec = importlib.util.spec_from_file_location("r2lib", "/home/claude/members/r2lib.py")
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
read_member = r2lib.read_member

MAIN = read_member("The_Method_1_6-2.md").split("\n")
SPEC = read_member("The_Method_1_6___Spectra_Compendium-2.md").split("\n")

R = 109737.31568          # the volumes' own Rydberg, gated by r2-tools-constants
Z = 6                     # Sc VI: Sc(5+) core charge, stated at main L7075
LIMIT = 892700.0          # MEASURED at main L6914: "a limit measured at 892,700 +/- 400"
LIMSIG = 400.0
D4, D5 = 1.0057, 0.9812   # main L7004, the two measured defects

def q(x, places):
    return Decimal(repr(x)).quantize(Decimal("1." + "0" * places), rounding=ROUND_HALF_UP)

def E(delta, n):
    nu = n - delta
    return LIMIT - R * Z * Z / (nu * nu)

def dEdd(delta, n):           # dE/d(delta) = 2 R Z^2 / nu^3, the local full spacing scale
    nu = n - delta
    return 2.0 * R * Z * Z / (nu ** 3)

def band(printed, places):    # the interval a printed decimal admits, half-up convention
    h = 0.5 * 10 ** (-places)
    return printed - h, printed + h

out = []
P = out.append
P("r2-ch14z  computable batch  main L6991-L7116 (25.6 - 25.6.6)")
P("inputs: R=%.5f Z_eff=%d limit=%.1f +/-%.0f  d(4s)=%.4f d(5s)=%.4f" % (R, Z, LIMIT, LIMSIG, D4, D5))
P("")

# ---- 1. the two-point Ritz solve, main L7008-L7010 --------------------------------
P("1. TWO-POINT RITZ SOLVE (L7010 prints d2=1.0889, dinf=0.9376, d(6s)=0.9679)")
d2 = (D4 - D5) / (1.0 / 16 - 1.0 / 25)
dinf = D4 - d2 / 16.0
d6 = dinf + d2 / 36.0
d7 = dinf + d2 / 49.0
P("   consistency d(4s)-d(5s) = %.6f -> printed 'consistent to 0.025' : %s  [q3 half-up]"
  % (D4 - D5, q(D4 - D5, 3)))
for name, val, printed in (("d2", d2, 1.0889), ("dinf", dinf, 0.9376), ("d(6s)", d6, 0.9679)):
    P("   %-6s computed %.6f  printed %.4f  q4 %s  %s"
      % (name, val, printed, q(val, 4), "EXACT" if float(q(val, 4)) == printed else "DEVIATION"))
P("   d(7s) computed %.6f (nowhere printed as a defect; the 7s figures below depend on it)" % d7)
P("")

# ---- 2. every printed energy, reproduced from its own defect ----------------------
P("2. ENERGIES  E(delta,n) = limit - R Z^2 / (n-delta)^2")
CASES = [
    ("L7018 monotone lower  d=d(5s)", D5,   6, 735860),
    ("L7018 monotone upper  d=dinf",  dinf, 6, 738547),
    ("L7033 convex   upper  d=0.9567", 2 * D5 - D4, 6, 737380),
    ("L7045 Ritz point      d=d(6s)", d6,   6, 736688),
    ("L7064 Rule 4 constant d=0.9934", 0.9934, 6, 735091),
    ("L7050 7s point        d=d(7s)", d7,   7, 784416),
    ("L7050 7s upper        d=dinf",  dinf, 7, 785209),
    ("L7050 7s lower        d=d(6s)", d6,   7, 784128),
    ("L7053 7s convex upper d=2d6-d5", 2 * d6 - D5, 7, 784605),
]
for tag, d, n, printed in CASES:
    e = E(d, n)
    lo, hi = band(round(d, 4), 4)
    elo, ehi = E(hi, n), E(lo, n)          # E decreasing in delta
    inband = min(elo, ehi) - 0.5 <= printed <= max(elo, ehi) + 0.5
    P("   %-34s d=%.6f  E=%10.1f  printed %7d  resid %+6.1f  band[%.0f,%.0f] %s"
      % (tag, d, e, printed, e - printed, min(elo, ehi), max(elo, ehi),
         "IN" if inband else "OUT"))
P("   the 7s lower edge, solved back: E=784128 at n=7 requires delta =")
lo_d = 7 - (R * Z * Z / (LIMIT - 784128)) ** 0.5
P("        %.6f ; d(6s) ESTIMATE = %.6f ; dinf = %.6f ; d(5s) MEASURED = %.6f"
  % (lo_d, d6, dinf, D5))
P("        E at n=7 from the last MEASURED defect d(5s) would be %.1f, not 784128" % E(D5, 7))
P("")

# ---- 3. widths, the factor, and containment --------------------------------------
P("3. WIDTHS AND CONTAINMENT")
w_mono6 = E(dinf, 6) - E(D5, 6)
w_conv6 = E(2 * D5 - D4, 6) - E(D5, 6)
w_mono7 = E(dinf, 7) - E(d6, 7)
w_conv7 = E(2 * d6 - D5, 7) - E(d6, 7)
for tag, w, printed in (("6s monotone", w_mono6, 2687), ("6s +convexity", w_conv6, 1520),
                        ("7s monotone", w_mono7, 1081), ("7s convex", w_conv7, 478)):
    P("   %-14s computed %8.2f  printed %5d  resid %+7.2f" % (tag, w, printed, w - printed))
P("   printed-figure arithmetic: 737380-735860 = %d ; 738547-735860 = %d ; 785209-784128 = %d ; 784605-784128 = %d"
  % (737380 - 735860, 738547 - 735860, 785209 - 784128, 784605 - 784128))
P("   L7035 'a factor of 1.8 tighter': 2687/1520 = %.4f  q1 %s" % (2687 / 1520, q(2687 / 1520, 1)))
P("   containment [735860,737380] inside [735860,738547]: %s (shares the lower edge)"
  % (735860 >= 735860 and 737380 <= 738547))
P("   L7051 'tighter than 6s because the spacing has fallen as nu^-3' -- both factors:")
P("      slope ratio  dE/dd(6s)/dE/dd(7s) = %.3f   delta-range ratio %.4f/%.4f = %.3f   product %.3f"
  % (dEdd(d6, 6) / dEdd(d7, 7), dinf and (D5 - dinf), (d6 - dinf), (D5 - dinf) / (d6 - dinf),
     (dEdd(d6, 6) / dEdd(d7, 7)) * ((D5 - dinf) / (d6 - dinf))))
P("      observed width ratio 2687/1081 = %.3f" % (2687 / 1081))
P("")

# ---- 4. convexity tangents --------------------------------------------------------
P("4. CONVEX TANGENTS")
P("   L7025 2*d(5s)-d(4s) = %.6f  printed 0.9567  q4 %s" % (2 * D5 - D4, q(2 * D5 - D4, 4)))
P("   L7053 2*d(6s)-d(5s) = %.6f  (the 7s tangent; d(6s) is the ESTIMATE, not a measured defect)"
  % (2 * d6 - D5))
P("   L7066 dbar=0.9934 exceeds d(5s)=%.4f : %s" % (D5, 0.9934 > D5))
P("")

# ---- 5. the wavelength window and the electronvolt -------------------------------
P("5. WAVELENGTH AND ENERGY UNITS (L7045-L7046)")
EV = 1.239841984e-4          # eV per cm^-1 (CODATA hc)
for tag, wn, printed in (("point 736,688", 736688, 13.5743),
                         ("window lower edge from 737,380", 737380, 13.5615),
                         ("window upper edge from 735,860", 735860, 13.5895)):
    nm = 1e7 / wn
    P("   %-32s 1e7/E = %.6f nm  printed %.4f  q4 %s  trunc4 %.4f"
      % (tag, nm, printed, q(nm, 4), int(nm * 1e4) / 1e4))
ev = 736688 * EV
P("   91.338 eV: 736688 * %.9e = %.5f  q3 %s" % (EV, ev, q(ev, 3)))
P("")

# ---- 6. the two spreads of the second route, L7105-L7106 -------------------------
P("6. THE TWO SPREADS (printed +/-1,594 and +/-2,169; neither input is printed)")
slopes = [("slope at nu(6s)", dEdd(d6, 6)), ("slope at nu(5s) n=5", dEdd(D5, 5)),
          ("slope at nu(7s)", dEdd(d7, 7)), ("slope at nu(4s) n=4", dEdd(D4, 4))]
for n_, s_ in slopes:
    P("   %-22s = %10.1f cm-1 per unit defect" % (n_, s_))
cands = []
for dn, dv in (("d(4s)-d(5s)", D4 - D5), ("d(5s)-dinf", D5 - dinf), ("d(6s)-dinf", d6 - dinf),
               ("0.025 stated", 0.025), ("0.035*d(6s)", 0.035 * d6), ("0.035*d(5s)", 0.035 * D5),
               ("0.035*d(4s)", 0.035 * D4), ("0.035*dbar", 0.035 * 0.9934),
               ("0.035*dinf", 0.035 * dinf), ("0.17*d(6s)", 0.17 * d6)):
    for sn, s in slopes:
        cands.append(("%s x %s" % (dn, sn), dv * s))
        cands.append(("half of %s x %s" % (dn, sn), 0.5 * dv * s))
for tag, w in (("6s monotone", w_mono6), ("6s convex", w_conv6), ("7s monotone", w_mono7)):
    cands.append(("half the %s width" % tag, w / 2))
cands.append(("the limit's own +/-400, x4", 1600.0))
for target in (1594.0, 2169.0):
    P("   candidates within 60 of %.0f, out of %d bases swept:" % (target, len(cands)))
    hit = [(n, v) for n, v in cands if abs(v - target) <= 60]
    if not hit:
        P("      NONE")
    for n, v in sorted(hit, key=lambda t: abs(t[1] - target)):
        P("      %-44s %8.1f  resid %+6.1f" % (n, v, v - target))
P("")

# ---- 7. the channel table, parsed on three bases ---------------------------------
P("7. THE CHANNEL TABLE (spectra II, L293-L934; its own totals line is L900)")
rows = []
for ln in range(293, 935):
    t = SPEC[ln - 1]
    if not t.startswith("|") or t.startswith("|---"):
        continue
    c = [x.strip() for x in t.strip().strip("|").split("|")]
    if len(c) != 11 or c[0] == "species":
        continue
    sp = c[0].replace("*", "").replace("\u2020", "").strip()
    try:
        interior = int(c[4])
    except ValueError:
        continue
    try:
        stage = int(c[9])
    except ValueError:
        stage = None
    br = c[5]
    m = re.match(r"^(\d+)/(\d+)$", br)
    tested = int(m.group(1)) if m else 0        # bracketed cells: the verified population
    rows.append((ln, sp, interior, stage, br, tested))
elements = sorted(set(s.split()[0] for _, s, _, _, _, _ in rows))
species = sorted(set(s for _, s, _, _, _, _ in rows))
tot_int = sum(r[2] for r in rows)
tot_tested = sum(r[5] for r in rows)
n_brk = sum(1 for r in rows if r[4].count("/") == 1)
P("   parsed %d rows, %d elements, %d interior cells | L900 states 596 / 28 / 2,269 -> %s"
  % (len(rows), len(elements), tot_int, "AGREES" if (len(rows), len(elements), tot_int) == (596, 28, 2269) else "DISAGREES"))
P("   bracket column: %d rows m/k, %d untested, %d no-triple ; bracketed (verified) cells = %d"
  % (n_brk, sum(1 for r in rows if r[4] == "untested"),
     sum(1 for r in rows if r[4] == "no-triple"), tot_tested))
P("   distinct species (element + stage): all rows %d ; bracket-tested rows %d"
  % (len(species), len(set(r[1] for r in rows if r[5] > 0))))
P("   [L7005 claims the monotonicity fact is established on 'thirty-five other species']")


def dist(sel, label):
    d = {}
    for _, sp, interior, st, br, tested in rows:
        if not sel(br, tested):
            continue
        e = d.setdefault(st, [0, 0, 0, set()])
        e[0] += 1; e[1] += interior; e[2] += tested; e[3].add(sp)
    P("   %s -- stage: rows / interior / bracketed / species" % label)
    for st in sorted(d, key=lambda x: (x is None, x)):
        r_, i_, t_, s_ = d[st]
        P("      %-3s %4d rows %5d interior %5d bracketed %3d species%s"
          % (st, r_, i_, t_, len(s_), ("  " + ", ".join(sorted(s_))) if st is not None and st > 3 else ""))
    return d

all_d = dist(lambda br, t: True, "ALL 596 ROWS")
tst_d = dist(lambda br, t: t > 0, "BRACKET-TESTED ROWS ONLY (the verified population)")
P("   L7075 'Every verified cell in this book lies at Z_eff between 1 and 3':")
for label, d in (("all rows", all_d), ("bracket-tested only", tst_d)):
    hi = [s for s in d if s is not None and s > 3]
    P("      %-20s stages above 3: %-28s rows %3d  interior %4d  bracketed %4d"
      % (label, str(sorted(hi)), sum(d[s][0] for s in hi), sum(d[s][1] for s in hi),
         sum(d[s][2] for s in hi)))
    P("      %-20s highest stage present = %s" % ("", max([s for s in d if s is not None])))
P("      L7075 'Z_eff = 6 -- double the highest charge state tested' requires a tested maximum of 3")
P("")

# ---- 8. Sc, and the sulphur-like sequence ---------------------------------------
P("8. THE SPECIES OF THIS SECTION, AGAINST THE COLLECTION")
sc = sorted(set((sp, st) for _, sp, _, st, _, _ in rows if sp.split()[0] == "Sc"))
P("   Sc in the channel table: %s (%d rows)"
  % (sc, sum(1 for r in rows if r[1].split()[0] == "Sc")))
seq = ["S I", "Cl II", "Ar III", "K IV", "Ca V", "Sc VI"]
P("   L7097's sulphur-like sequence against the table (L7099: 'both tabulated for all five'):")
for sp in seq:
    n = [ln for ln, s, _, _, _, _ in rows if s == sp]
    P("      %-7s %s" % (sp, ("%d row(s) at spectra %s" % (len(n), n)) if n else "NO ROW IN THE CHANNEL TABLE"))
ZN = {"S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20, "Sc": 21}
ROM = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6}
bad = [sp for sp in seq if ZN[sp.split()[0]] - ROM[sp.split()[1]] + 1 != 16]
P("   electron counts: all six give 16 electrons (sulphur-like): %s" % (not bad))
P("   L7097 prints six members and calls Sc VI 'a fifth member'; Sc VI is member %d of the six"
  % len(seq))
P("")

# ---- 9. Sc VI across the six volumes ---------------------------------------------
P("9. 'Sc VI' ACROSS THE SIX VOLUMES (raw lines, word-bounded)")
VOLS = [("main", MAIN), ("register", read_member("The_Method_1_6___The_Register-2.md").split("\n")),
        ("math", read_member("The_Method_1_6___Mathematical_Compendium-2.md").split("\n")),
        ("physics", read_member("The_Method_1_6___The_Physics_Compendium-2.md").split("\n")),
        ("ioi", read_member("The_Method_1_6___The_Index_of_Indices-2.md").split("\n")),
        ("spectra", SPEC)]
pat = re.compile(r"\bSc VI\b")
for name, V in VOLS:
    n = [i for i, l in enumerate(V, 1) if pat.search(l)]
    P("   %-9s %d line(s)%s" % (name, len(n), "" if len(n) > 8 else " %s" % n))
P("")
P("end r2-ch14z")
print("\n".join(out))
