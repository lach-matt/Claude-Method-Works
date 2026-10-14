#!/usr/bin/env python3
"""DOCKET 67 -- audit stage: asplund-2009-hybrid-column-recommendation.

The tree (stockgate.py:61-75, :499-510) uses a HYBRID solar column -- A09 photospheric
where determined, A09 CI-meteoritic otherwise -- attributes it to A09 ('A09's own advice',
:500), and calls it 'the defensible cosmic column'.  This script checks what is finite:

  H1  the 12 payload elements lacking a photospheric value are exactly Table 1's dashes
  H2  photospheric-only -> infinity; hybrid -> finite (the tree's Finding B)
  H3  the fill is on the photospheric scale (A09 sec 4.1: meteoritic pegged to Si)
  H4  ROBUSTNESS: how far (dex) would any of the 12 filled values have to fall before
      it, rather than the tree's binder, binds?  i.e. does the choice of fill matter?
  H5  alternative fills READ in later compilations (AAG21 CI column, AG26 'CI-Tc'):
      does the binder or its factor move?
  H6  the tree's hybrid rule applied to Li: photospheric 1.05 is used (Li is determined)
  H7  normalisation effect of the 12 filled elements

Table 1 values are those READ at alphaXiv by the sibling audit (0909.0948), parsed from
rederive/0909.0948.py -- not re-typed here.  stockgate.py is imported READ-ONLY.
"""
import ast, math, sys
sys.dont_write_bytecode = True
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
SIB = ("/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/"
       "scratchpad/d67/rederive/0909.0948.py")
sys.path.insert(0, TREE)
import stockgate as sg  # read-only

src = open(SIB).read()
tree = ast.parse(src)
DATA = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and \
            isinstance(node.targets[0], ast.Name) and node.targets[0].id in ("T1", "AAG21", "AG26"):
        DATA[node.targets[0].id] = ast.literal_eval(node.value)
T1, AAG21, AG26 = DATA["T1"], DATA["AAG21"], DATA["AG26"]

fails = []
def chk(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  -- " + detail if detail else ""))
    if not ok:
        fails.append(label)

AM = sg.ATOMIC_MASS
P59 = sg.payload("as-composed")          # the 59-element ICRP payload (mass fractions)

def column(logeps):
    n = {e: 10.0 ** (v - 12.0) for e, v in logeps.items() if v is not None}
    m = {e: n[e] * AM[e] for e in n if e in AM}
    t = sum(m.values())
    return {e: v / t for e, v in m.items()}

def bind(p, s):
    f = {e: (math.inf if s.get(e, 0) <= 0 else p[e] / s[e]) for e in p}
    e = max(f, key=lambda k: f[k])
    return e, f[e], f

# ---------------------------------------------------------------- H1
dash_all = sorted(e for e, (ph, me) in T1.items() if ph is None)
dash_payload = sorted(e for e in P59 if e in T1 and T1[e][0] is None)
tree_missing = sg.missing_photospheric()
print("Table 1 photospheric dashes (all):", dash_all)
print("payload elements with a Table 1 dash:", dash_payload)
chk("H1 tree's 12 missing == Table 1 dashes within the payload",
    tree_missing == dash_payload and len(dash_payload) == 12, str(tree_missing))
chk("H1 every one of the 12 HAS a Table 1 meteoritic value",
    all(T1[e][1] is not None for e in dash_payload))
chk("H1 payload elements absent from Table 1 altogether", all(e in T1 for e in P59),
    str([e for e in P59 if e not in T1]))

# ---------------------------------------------------------------- H2
ph_only = column({e: v[0] for e, v in T1.items()})
hyb = column({e: (v[0] if v[0] is not None else v[1]) for e, v in T1.items()})
e0, f0, _ = bind(P59, ph_only)
e1, f1, F1 = bind(P59, hyb)
chk("H2 photospheric-only returns infinity", math.isinf(f0), "binds on %s" % e0)
chk("H2 hybrid is finite", math.isfinite(f1), "binds on %s at %.2f" % (e1, f1))
tg = sg.binding_under("as-composed 59", "stellar photosphere")
chk("H2 tree's own hybrid reproduces from READ Table 1", tg[0] == e1 and abs(tg[1] - f1) / f1 < 1e-3,
    "tree %s %.2f vs here %s %.2f" % (tg[0], tg[1], e1, f1))

# ---------------------------------------------------------------- H3
chk("H3 Si photospheric == meteoritic (the A09 sec 4.1 peg)", T1["Si"][0] == T1["Si"][1] == 7.51)
VOL = {"H", "He", "C", "N", "O", "Ne", "Ar", "Kr", "Xe", "Li"}
diffs = sorted(v[1] - v[0] for e, v in T1.items()
               if v[0] is not None and v[1] is not None and e not in VOL)
med = diffs[len(diffs) // 2]
mean = sum(diffs) / len(diffs)
sd = (sum((d - mean) ** 2 for d in diffs) / (len(diffs) - 1)) ** 0.5
print("met - phot over %d non-volatile elements: median %+.3f, mean %+.3f, sd %.3f dex"
      % (len(diffs), med, mean, sd))
chk("H3 fill is on the photospheric scale to within 0.05 dex (median)", abs(med) <= 0.05)

# ---------------------------------------------------------------- H4
print("\nH4  the 12 filled elements in the hybrid, and the fall each needs to bind:")
need = {}
for e in dash_payload:
    need[e] = math.log10(f1 / F1[e])
    print("   %-2s  factor %11.4f   must fall %.2f dex (x%.3g) to overtake %s"
          % (e, F1[e], need[e], 10 ** need[e], e1))
emin = min(need, key=need.get)
print("   closest: %s at %.2f dex" % (emin, need[emin]))
chk("H4 no filled element binds, nor is within 1 dex of binding", need[emin] > 1.0,
    "%s %.2f dex" % (emin, need[emin]))
# the largest fill-to-photosphere offset A09's own data show for a non-volatile element
maxoff = max(abs(d) for d in diffs)
chk("H4 the smallest margin exceeds the largest |met-phot| offset seen for any "
    "non-volatile element in Table 1", need[emin] > maxoff, "margin %.2f vs max offset %.2f"
    % (need[emin], maxoff))

# ---------------------------------------------------------------- H5
alt = {}
for name, fill in (("AAG21 CI column", {e: AAG21[e][1] for e in dash_payload}),
                   ("AG26 Table 3 (CI-Tc) values", {e: AG26[e] for e in dash_payload})):
    le = {e: (v[0] if v[0] is not None else v[1]) for e, v in T1.items()}
    le.update(fill)
    ea, fa, Fa = bind(P59, column(le))
    alt[name] = (ea, fa)
    dmax = max(abs(fill[e] - T1[e][1]) for e in dash_payload)
    chk("H5 fill from %s: binder unchanged" % name, ea == e1,
        "%s %.2f (A09-fill %.2f); max fill change %.2f dex" % (ea, fa, f1, dmax))

# ---------------------------------------------------------------- H6
chk("H6 hybrid rule takes Li photospheric (determined) = 1.05", T1["Li"][0] == 1.05 and
    sg.solar_hybrid()["Li"] == column({"Li": 1.05, **{e: (v[0] if v[0] is not None else v[1])
                                                      for e, v in T1.items() if e != "Li"}})["Li"])
li_met = {e: (v[0] if v[0] is not None else v[1]) for e, v in T1.items()}
li_met["Li"] = T1["Li"][1]
_, _, Fm = bind(P59, column(li_met))
print("   Li factor: hybrid (photospheric Li) %.2f ; with meteoritic Li %.4f" % (F1["Li"], Fm["Li"]))

# ---------------------------------------------------------------- H7
n = {e: 10.0 ** ((v[0] if v[0] is not None else v[1]) - 12.0) * AM[e]
     for e, v in T1.items() if e in AM}
share = sum(n[e] for e in dash_payload) / sum(n.values())
print("H7  mass share of the 12 filled elements in the hybrid column: %.3e" % share)
chk("H7 filling changes the normalisation by < 1e-6", share < 1e-6)

print("\nRESULT:", "ALL CHECKS PASS" if not fails else "FAILURES: %s" % fails)
sys.exit(1 if fails else 0)
