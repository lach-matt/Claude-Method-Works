#!/usr/bin/env python3
"""DOCKET 67 -- audit of 'no-observed-wormhole' (create.py:119, :249).

A negative observational claim has no derivation to re-run.  What IS finite
and checkable here, and is checked:

 (A) the tree's own internal consistency: create.py states the absence FLAT
     ("nobody has ever observed one"); negmass.py records the echo channel as
     CONTESTED with no confirmed detection; detect.py records OBSERVED = False
     and that the shadow channel cannot discriminate.  Parsed by AST -- the
     tree's files are NOT imported (importing would write __pycache__ into
     research/warp-drive, which this docket may not touch).
 (B) what the published null results actually bound, and whether that bound
     reaches the tree's own search target (detect.py: a 1193 km throat).
     INPUT VALUES ARE NOT READ AT SOURCE: alphaXiv returned 'assistant quota
     exceeded' on every call and arxiv.org / iopscience / osti are refused by
     the egress proxy.  The numbers below are the abstracts as returned by a
     web-search snippet (Takahashi & Asada 2013, arXiv:1303.1301; Yoo, Harada
     & Tsukamoto 2013, arXiv:1302.7170).  Every figure computed from them is
     CONDITIONAL on those snippet values and says so.
"""
import ast, math, os, sys
import sympy as sp

TREE = "/home/user/Claude-Method-Works/research/warp-drive"
ok = True
def chk(label, got, want):
    global ok
    good = got == want
    ok &= good
    print("  [%s] %s: %r (want %r)" % ("OK" if good else "XX", label, got, want))

def consts(fname, names):
    tree = ast.parse(open(os.path.join(TREE, fname)).read())
    out = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in names:
                    try: out[t.id] = ast.literal_eval(node.value)
                    except Exception: out[t.id] = "<non-literal>"
    return out

print("(A) THE TREE'S OWN STATEMENTS, BY AST")
c = consts("create.py", {"ROUTE", "ROUTE_COST"})
d = consts("detect.py", {"OBSERVED", "SOURCE_IS_AN_ESSAY", "CHANNELS"})
n = consts("negmass.py", {"CONFIRMED_DETECTION", "CONTESTED", "ECHO_SEARCHES"})
src_create = open(os.path.join(TREE, "create.py")).read().splitlines()
chk("create.py:119 carries the flat claim",
    "NOBODY HAS EVER OBSERVED ONE" in src_create[118], True)
chk("create.ROUTE_COST", c.get("ROUTE_COST"),
    "nobody has ever observed one -- a search problem, not a build")
chk("create.py:115-122 cites a source for the claim",
    any("arXiv" in l for l in src_create[114:122]), False)
chk("detect.OBSERVED", d.get("OBSERVED"), False)
shadow = [x for x in d.get("CHANNELS", ()) if x[0] == "shadow"]
chk("detect.py: shadow channel discriminates", shadow[0][1] if shadow else None, False)
chk("negmass.CONFIRMED_DETECTION", n.get("CONFIRMED_DETECTION"), False)
chk("negmass.CONTESTED", n.get("CONTESTED"), True)
chk("negmass: echo analyses listed", len(n.get("ECHO_SEARCHES", ())), 6)
tentative = [e for e in n.get("ECHO_SEARCHES", ()) if "tentative" in e[2]]
chk("negmass: a tentative positive claim is on record", len(tentative), 1)
print("  -> create.py's flat 'nobody has ever observed one' drops two hypotheses the")
print("     tree states elsewhere: 'observed' means IDENTIFIED (detect.py: shadows")
print("     mimic, so an imaged compact object is not a non-observation), and the")
print("     echo channel is CONTESTED, not null (negmass.py).  Both files agree with")
print("     create.py that there is NO CONFIRMED detection.")

print("\n(B) WHAT THE PUBLISHED NULLS BOUND (snippet values; NOT READ AT SOURCE)")
h = sp.Symbol("h", positive=True)
nsym, r = sp.symbols("n r", positive=True)
# mean inter-object distance for number density n
dist = (3 / (4 * sp.pi * nsym)) ** sp.Rational(1, 3)
n_TA = sp.Rational(1, 10**4)          # h^3 Mpc^-3, Takahashi & Asada, a = 10..1e4 pc
d_TA = float(dist.subs(nsym, n_TA))   # in Mpc/h
print("  Takahashi-Asada: n < 1e-4 h^3 Mpc^-3 for 10 pc < a < 1e4 pc")
print("   => Wigner-Seitz radius (3/(4 pi n))^(1/3) >= %.2f Mpc/h" % d_TA)
chk("Wigner-Seitz radius at the bound ~ 13.4 Mpc/h", round(d_TA, 1), 13.4)
N100 = float(sp.Rational(4, 3) * sp.pi * 100**3 * n_TA)
print("   => up to %.0f Ellis wormholes of that size within 100 Mpc/h remain allowed" % N100)
chk("allowed count within 100 Mpc/h exceeds zero by hundreds", N100 > 400, True)
PC_M = 3.0856775814913673e16
a_tree_m = 1193e3                         # detect.py:90/103, the tree's search target
a_tree_pc = a_tree_m / PC_M
gap = math.log10(10.0 / a_tree_pc)
print("  detect.py target throat 1193 km = %.3e pc: %.1f orders BELOW the SQLS range" % (a_tree_pc, gap))
chk("SQLS bound reaches the tree's target", 10.0 <= a_tree_pc <= 1e4, False)
AU_M = 1.495978707e11
print("  Yoo-Harada-Tsukamoto femtolensing: n < 2e-9 AU^-3 at a ~ 1 cm")
chk("femtolensing bound reaches the tree's target (a ~ 1 cm only)",
    abs(math.log10(a_tree_m / 0.01)) < 1, False)
d_femto_AU = float(dist.subs(nsym, sp.Rational(2, 10**9)))
print("   => Wigner-Seitz radius (3/(4 pi n))^(1/3) >= %.0f AU at a ~ 1 cm" % d_femto_AU)
print("  Galactic microlensing SENSITIVITY range quoted for a = 100 .. 1e7 km")
chk("tree target inside the microlensing sensitivity window", 100 <= 1193 <= 1e7, True)
print("   (whether that window has produced a published BOUND was not read: OPEN)")

print("\nVERDICT: no confirmed identification (agrees with the tree); the flat")
print("wording drops 'identified' and 'contested'; published nulls bound only")
print("specific model classes and size windows, none covering 1193 km.")
print("\nSELFTEST " + ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
