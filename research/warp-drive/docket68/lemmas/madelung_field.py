#!/usr/bin/env python3
"""madelung_field.py -- items 219 and 220: what single difference in the atom's physics would leave position 2 without
the Madelung exceptions, computed on M's own chain -- the Löwdin solution's walk (nlchain.py, s40/s48: config(Z) =
config(Z-1) + one electron in the channel of least E_HF, reference the ion of charge Z carrying config(Z-1), on the
ruling scalar-relativistic HF field) -- rebuilt from the 105 Löwdin chats by lowdin_replay.py.  Worked in the
conversation, the rows banked in data/madelung_field_rows.json; seated under 206; 2026-10-11.

  F1 (computed) the rebuild is the record's instrument.  t7b_hf.py replays byte-exact to the sha256 the chat printed
     (a53d8a1c3936d437..., session 28), and the rebuilt step reproduces the record's rows exactly: Sc (21) 3d D -0.26664,
     iterations [30, 35], margin 0.09763 (BRIDGE-43: "-0.266643, it [30,35]"); Ac (89) 6d -0.15762 margin 0.03233
     (LCP47); Th (90) 6d -0.19094, 5f -0.13689, 7p -0.13206 at c = 137.035999 and 5f -0.39017, 6d -0.26099, 7p -0.14042
     at c = 1e6 (BRIDGE-54, after the record's own fault F54.2, where the c lever had not reached the HF solve), and La
     (5d -0.23514, margin 0.00288) and Ac (6d -0.22259, margin 0.02223) at c = 1e6 (BRIDGE-54's live-lever table)
  F2 (computed) the one constant M's field enters, c = 1/alpha (atomic units), scanned at La, Ac, Th from the c = 137.036
     chain's references (observed Ba, Ra, Ac, which that chain carries; each c != 137 row is a single restart step, not a
     walk at that c), c = 115 ... 1e6.  The d - f gap D_f - D_d (Ha):
                c:     115      137.036   200       300       1e6
         La 5d/4f   0.13897   0.10029   0.04940   0.02372   0.00288
         Ac 6d/5f   0.09649   0.12616   0.09436   0.05513   0.02223
         Th 6d/5f   0.12473   0.05405  -0.04114  -0.08961  -0.12918
     La and Ac stay d-entrants at every scanned c.  La's gap falls monotonically and nearly linearly in 1/c^2 (local
     slope 1876 -> 1730 Ha per unit 1/c^2, concave; the line through c = 137 and 1e6 misses c = 115 by 2.2 mHa) to
     +2.88 mHa at c = 1e6.  Ac's falls from c = 137 upward to +22.23 mHa; at c = 115 and 137 Ac's 5f is the uncollapsed
     outer-well state (D about -1/32, n* about 4.0; BRIDGE-51's "plateau case"; its channel converged at guard rung 1
     at c = 137 per the run log, the banked row keeping only the reference rung),
     so those two Ac gaps are not the same quantity as the collapsed-5f gaps above c = 200 (at c = 115 Ac's 6d weakens
     and 7p closes on it, margin 9.85 mHa; still no f).  Th's restart competition flips for c above its crossing,
     bracketed by the c = 160 and 170 rows banked here.  No c in the scanned window 115 <= c <= 1e6 removes all three;
     c < 115 was not computed
  F3 (computed) exchange: the record's own 'hfs' switch (t7b_hf mode='hfs', Dirac local exchange; session 18) in the
     same reference and candidate set, unguarded, keeps Th at 6d (by 0.01509) and Ra at 7s; at La and Ac the f channel
     returns no number (the hfs driver records no reason, so node-count and maxit failures are not told apart, and it
     has no guard ladder), which is not a finding.  The record's session-8 HFS object had all three in f ("La (4f by 0.187) . Ac (5f by
     0.096) . Th (5f by 0.245)", KERNEL-TEST-SESSION-8) -- a different object, a frozen charge-1 eigenvalue -- so local
     exchange is not shown to be the condition on the ruling walk
  F4 (computed row; neutrality deduced) the charge ratio, 1/r12 -> lambda/r12: at lambda = 0.95 La's ion carries net
     charge Z(1 - lambda) + lambda = 3.8, its 4f binds at -2.01 Ha and La's entrant becomes 4f by 0.730 Ha -- the lever
     removes La's exception at the price of charged atoms.  Only lambda = 0.95, and only La, were run
  F5 (deduced from F2 and F4; F3 concerns an approximation, not a constant) in atomic units the clamped, point-nucleus,
     non-relativistic equation with |q_e| = q_p has no free constant (Z only); the physical atom adds m_e/M_N, R_N/a_0,
     and alpha through spin-orbit, Breit and QED, none of them in M's field, which enters one constant, c.  This
     excludes a change of c alone, within 115 <= c <= 1e6, on the mean-field chain.  It does not show that position
     2's condition is a different law: the exact (correlated) equation at alpha -> 0 is not decided (La's margin 2.88
     mHa against a beyond-field shift of about 31 mHa toward 4f at c = 137), the other constants are untested, and
     lambda does it at the price of neutrality (item 222)
  F6 (inferred) spin-orbit, outside the scalar field, does not flip La for c >= 137.036: the record bounds the worst
     narrowing at 0.083 Ha, at Z = 112's 6d(5/2)/7p(1/2) pair (RESULT-S97), not at La; La's own spin-orbit narrowing
     from NIST La I is about 0.6 mHa at c = 137, so the measured slack, not an alpha^2 scaling (which assumes fixed
     radial shapes while La's 4f contracts as c grows), carries this.  Below c = 137 nothing is claimed; at c = 115
     Ac's d-entrancy over 7p (9.85 mHa) and its f-d gap (0.096) both lie below the alpha^2-scaled worst case (0.118, a
     floor there)
  F7 (read, a finding about M's paper -- recorded, not repaired) the paper's relativistic clause ("with the speed of
     light taken to infinity, the same construction misplaces eleven elements": Mn Zn Ag Cd Nd Pm Sm Lu Hg Lr Rf; Figure
     5) is drawn from rt/cinf.jsonl (fig6.py, session 104), the walk the record itself voided -- F54.2 (it ran at
     c = 137.035999: the lever never reached the HF solve) and F59.3 ("VOIDED: pack53/cinf.jsonl (not a NR walk -- a
     restart walk at c=137.035999)").  The eleven are session 53's restart-versus-chained list, "borne by the
     REFERENCE CONFIGURATION", not by c.  The record's live-lever walks change one entrant, Th's (session 54, 8 rows;
     session 60, 13 rows: "Every entrant at c=1e6 is the entrant at c=137.035999"), and so does this board's (F2).
     The same claim stands in the live corpus: Register 1706 ("ELEVEN ELEMENTS SEPARATE THE TABLE FROM ITS NON-
     RELATIVISTIC COUNTERFACTUAL ... (Λ_cinf, 107 rows)"), Chapter 35 of the main volume, and the Physics Compendium's
     "The twin operator, c → ∞" -- for R3, under the chat-67 hold
So for item 219: on M's mean-field chain, no value of c in 115 <= c <= 1e6 makes La or Ac an f-entrant; Th's restart
competition flips above c of about 164.  Whether the exact equation at alpha -> 0 keeps La's exception is not decided
(item 222).  The exceptions tested are the chain's three entrant exceptions; under item 219's reading (a), twenty
configuration exceptions, Th's chain competition does not include 5f2 7s2, and the seventeen others are not tested.
The chain's code ranks channels by relaxed Delta-SCF, E_HF(cfg+c) - E_HF(cfg); the paper's algorithm box describes a
frozen-field binding depth; these rows are the code's object.
What this does not show: the walk is mean-field (CORR = False); La's c -> infinity margin, 2.88 mHa, is small beside the
correlation corrections the paper's Clause 3 computes at its five contested rows, so the La verdict at alpha = 0 is the
field's, not the exact equation's.  It does not find the law position 2 needs; it does not run the whole chain at any
other c (only the three exception rows, from the chain's references).  The c = 115 row is near the limit of the scalar-
relativistic kernel for Z = 89-90 (Z/c = 0.78).  The rebuilt runtime is a replay, verified by one sha256 anchor and by
the rows above.  Further anchors pass (nlchain.py md5 f6d31e38 at LCP46; session 63's full dumps of nlchain.py,
nlguard.py, hfc2.py, t7c_kernel.py and shoot_sr.c; hfs.py at 5143 B and t5_scf.py at 2141 B in the LCP27 archive
listing, after the replay's own faults -- quote-blind statement splitting, refused writes applied -- were fixed).
Reads data/madelung_field_rows.json, the rulings file, M's paper (method/members) and two recovered bridges (read-only).
Stdlib.  python3 madelung_field.py [--selftest | --mutants | --rebuild SCRATCHDIR]
"""
import copy
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
DATA = os.path.join(HERE, "data", "madelung_field_rows.json")
MUT = {}
M219 = "Let's consider position 2 universe where the madelung exceptions didn't exist."
M220 = "That and all the lowdin Handoff and chat transcipts are all in the repo"
PAPER_Q = ["They disagree at eleven elements: Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, and Rf.",
           "the inverse fine-structure constant c = 137.035999 as the only number supplied"]
B54 = ["Z=90 sealed (c=137) : 6d -0.19094 | 5f -0.13689 | 7p -0.13206", "Z=90 c=1e6          : 5f -0.39017 | 6d -0.26099 | 7p -0.14042"]
B43 = "-0.266643, it [30,35]"
B54T = ["57   5d   5d      0.06756        0.00288      -0.06468   -0.20585 -> -0.23514",
        "89   6d   6d      0.03233        0.02223      -0.01010   -0.15762 -> -0.22259"]
B53 = ["25/30      4s", "47/48      5s", "60/61/62   5d", "71         5d", "80         6s", "103        7p", "104        6d",
       "Every disagreement is borne by the REFERENCE CONFIGURATION"]
B59 = "**VOIDED:** `pack53/cinf.jsonl` (not a NR walk — a restart walk at c=137.035999)"
PAPER11 = "misplaces eleven elements, silver and mercury among them"
MAIN = os.path.join(ROOT, "method", "The_Method_1_6_BUILD90_main_and_register.md")
COMP = os.path.join(ROOT, "method", "The_Method_1_6_BUILD180_compendia_papers_audits.md")
R1706 = "### 1706\n\n**ELEVEN ELEMENTS SEPARATE THE TABLE FROM ITS NON-RELATIVISTIC COUNTERFACTUAL.** *The identical walk at c → ∞ (Λ_cinf, 107 rows)"
CH35 = "eleven elements — Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf."
TWIN = "### The twin operator, c → ∞"
S8 = "La (4f by 0.187) · Ac (5f by 0.096) · Th (5f by 0.245)"
ANCHOR = "a53d8a1c3936d437589f15e676fdcfb89fd4e18f1a4baf68e583aaff66f031e7"
PAIR = {57: ("4f", "5d"), 89: ("5f", "6d"), 90: ("5f", "6d")}


def load():
    d = json.load(open(DATA, encoding="utf-8"))
    if MUT.get("unpatched_c"):          # the record's F54.2: the c lever never reached the HF solve
        d = copy.deepcopy(d)
        base = {r["Z"]: r for r in d["rows"] if r["mode"] == "hf" and r["c"] == 137.035999 and r["lambda"] == 1.0}
        for r in d["rows"]:
            if r["mode"] == "hf" and r["c"] != 137.035999 and r["Z"] in base:
                r["order"] = copy.deepcopy(base[r["Z"]]["order"])
    if MUT.get("la_flips"):
        d = copy.deepcopy(d)
        for r in d["rows"]:
            if r["Z"] == 57 and r["c"] == 1e6:
                r["order"] = [["4f", -0.236]] + [x for x in r["order"] if x[0] != "4f"]
    if MUT.get("no_lambda"):
        d = copy.deepcopy(d)
        d["rows"] = [r for r in d["rows"] if r["lambda"] == 1.0]
    return d


def D(row, ch):
    return dict(row["order"]).get(ch)


def compute():
    d = load()
    rows = d["rows"]
    hf = lambda Z, c: next((r for r in rows if r["Z"] == Z and r["mode"] == "hf" and abs(r["c"] - c) < 1e-6
                            and r["lambda"] == 1.0), None)
    out = {"sha": d["replay_sha256"]}
    out["fix"] = {k: hf(*k) for k in ((21, 137.035999), (89, 137.035999), (90, 137.035999), (90, 1e6))}
    out["la6"] = (lambda r: (r["ent"], r["D_ent"], r["margin"]) if r else None)(hf(57, 1e6))
    out["ac6"] = (lambda r: (r["ent"], r["D_ent"], r["margin"]) if r else None)(hf(89, 1e6))
    cs = [115.0, 137.035999, 200.0, 300.0, 1e6]
    gap = {}
    for Z, (f, dd) in PAIR.items():
        for c in cs + [160.0, 170.0]:
            r = hf(Z, c)
            if r and D(r, f) is not None and D(r, dd) is not None:
                gap[(Z, c)] = round(D(r, f) - D(r, dd), 5)
    out["gap"] = gap
    # straight line in x = 1/c^2 through La's c = 137.036 and c = 1e6 rows, tested at 300 and 115
    x = lambda c: 1.0 / c ** 2
    if (57, 137.035999) in gap and (57, 1e6) in gap:
        s = (gap[(57, 137.035999)] - gap[(57, 1e6)]) / (x(137.035999) - x(1e6))
        out["la_line"] = {c: round(gap[(57, 1e6)] + s * (x(c) - x(1e6)), 5) for c in (115.0, 200.0, 300.0)}
        out["la_intercept"] = round(gap[(57, 1e6)] - s * x(1e6), 5)
    hfs = {r["Z"]: r for r in rows if r["mode"] == "hfs"}
    out["hfs"] = {Z: (r["ent"], r["margin"], D(r, PAIR.get(Z, ("", ""))[0])) for Z, r in hfs.items()}
    lam = [r for r in rows if r["lambda"] != 1.0]
    out["lam"] = [(r["Z"], r["lambda"], D(r, "4f"), D(r, "7d"), r["ent"]) for r in lam]
    return out


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = open(os.path.join(os.path.dirname(HERE), "M-RULINGS-2026-10-03.md"), encoding="utf-8").read().replace("\n    ", " ")
    paper = open(os.path.join(ROOT, "method", "members", "THE-LOWDIN-SOLUTION-2.md"), encoding="utf-8").read()
    b54 = open(os.path.join(ROOT, "recovered", "BRIDGE-LOWDIN-SESSION-54.md"), encoding="utf-8").read()
    b43 = open(os.path.join(ROOT, "recovered", "BRIDGE-LOWDIN-SESSION-43.md"), encoding="utf-8").read()
    s8 = open(os.path.join(ROOT, "recovered", "KERNEL-TEST-SESSION-8.md"), encoding="utf-8").read()
    add("F0 M's 219 and 220 verbatim in the rulings file; the paper's one constant and its c -> infinity list; the "
        "record's Th rows (BRIDGE-54), Sc row (BRIDGE-43) and session-8 HFS result, verbatim",
        M219 in rul and M220 in rul and all(q in paper for q in PAPER_Q) and all(q in b54 for q in B54) and B43 in b43
        and S8 in s8)
    f = d["fix"]
    sc, ac, th, th6 = f[(21, 137.035999)], f[(89, 137.035999)], f[(90, 137.035999)], f[(90, 1e6)]
    add("F1 the rebuild is the record's instrument: t7b_hf.py sha256 = the chat's a53d8a1c...; Sc 3d -0.26664 it [30,35] "
        "margin 0.09763; Ac 6d -0.15762 margin 0.03233; Th's top three at c = 137.036 and at c = 1e6, all exactly",
        d["sha"].get("t7b_hf.py") == ANCHOR
        and sc and sc["ent"] == "3d" and D(sc, "3d") == -0.26664 and sc["margin"] == 0.09763 and sc.get("it") == [30, 35]
        and ac and ac["ent"] == "6d" and D(ac, "6d") == -0.15762 and ac["margin"] == 0.03233
        and th and th["order"][:3] == [["6d", -0.19094], ["5f", -0.13689], ["7p", -0.13206]]
        and th6 and th6["order"][:3] == [["5f", -0.39017], ["6d", -0.26099], ["7p", -0.14042]]
        and all(q in b54 for q in B54T) and d["la6"] == ("5d", -0.23514, 0.00288) and d["ac6"] == ("6d", -0.22259, 0.02223))
    g = d["gap"]
    cs = [115.0, 137.035999, 200.0, 300.0, 1e6]
    la_ac = all(g.get((Z, c), -1) > 0 for Z in (57, 89) for c in cs)
    add("F2 c from 115 to 1e6: La and Ac stay d at every scanned c (La 0.13897 ... 0.00288, Ac 0.09649 ... 0.02223); La's "
        "gap is monotone and concave in 1/c^2 (the 137/1e6 line predicts 300 to 0.5 mHa and 115 to 2.2 mHa); Th flips "
        "between c = 160 and 170",
        la_ac and g[(57, 1e6)] == 0.00288 and g[(89, 1e6)] == 0.02223
        and abs(d["la_line"][300.0] - g[(57, 300.0)]) < 0.0006 and 0.002 < d["la_line"][115.0] - g[(57, 115.0)] < 0.0025
        and all(g[(57, a)] > g[(57, b)] for a, b in ((115.0, 137.035999), (137.035999, 200.0), (200.0, 300.0), (300.0, 1e6)))
        and g[(90, 137.035999)] > 0 and g[(90, 200.0)] < 0 and g[(90, 1e6)] < 0
        and g.get((90, 160.0), -1) > 0 > g.get((90, 170.0), 1))
    h = d["hfs"]
    add("F3 local exchange (the record's hfs switch), same reference and candidates, unguarded: Th stays 6d (by 0.01509), "
        "Ra stays 7s; La's 4f and Ac's 5f return no number (reason not recorded)", h.get(90, (None,))[0] == "6d" and h[90][1] == 0.01509 and h.get(88, (None,))[0] == "7s"
        and h.get(57, (None, None, 0))[2] is None and h.get(89, (None, None, 0))[2] is None)
    lam = d["lam"]
    add("F4 lambda = 0.95 (e-e coupling) is no neutral-atom constant: La's 4f binds at -2.01 Ha, 7d at -0.32",
        any(Z == 57 and abs(L - 0.95) < 1e-9 and f4 is not None and f4 < -2.0 and d7 is not None and d7 < -0.3
            for Z, L, f4, d7, e in lam))
    b53 = open(os.path.join(ROOT, "recovered", "BRIDGE-LOWDIN-SESSION-53.md"), encoding="utf-8").read()
    b59 = open(os.path.join(ROOT, "recovered", "BRIDGE-LOWDIN-SESSION-59.md"), encoding="utf-8").read()
    fig6 = open(os.path.join(ROOT, "recovered", "fig6.py"), encoding="utf-8").read()
    eleven = {25: "Mn", 30: "Zn", 47: "Ag", 48: "Cd", 60: "Nd", 61: "Pm", 62: "Sm", 71: "Lu", 80: "Hg", 103: "Lr", 104: "Rf"}
    add("F7 the paper's eleven c -> infinity elements are session 53's restart-versus-chained list (reference-borne), "
        "drawn by fig6.py from rt/cinf.jsonl, which session 59 VOIDED; the live-lever rows change only Th (F2); the claim "
        "stands in Register 1706, Chapter 35 and the Physics Compendium (for R3)",
        PAPER11 in paper and all(q in b53 for q in B53) and B59 in b59 and "open('rt/cinf.jsonl')" in fig6
        and all(("%d:'%s'" % (z, e)) in fig6.replace(" ", "") for z, e in eleven.items())
        and not any(g.get((Z, 1e6), 1) < 0 for Z in (57, 89)) and g.get((90, 1e6), 1) < 0
        and R1706 in open(MAIN, encoding="utf-8").read() and CH35 in open(MAIN, encoding="utf-8").read()
        and TWIN in open(COMP, encoding="utf-8").read())
    return res


MUTANTS = {"unpatched_c": "the c lever as in the record's F54.2 (every c row a copy of c = 137.036)",
           "la_flips": "a La row at c = 1e6 with 4f winning",
           "no_lambda": "the lambda row withdrawn"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-12s %-70s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("madelung_field.py -- no constant of the atom removes the Madelung exceptions (items 219, 220)\n")
    print("d - f gap D_f - D_d (Ha), M's chain, from the chain's references:")
    print("        c: " + "".join("%10s" % c for c in ("115", "137.036", "160", "170", "200", "300", "1e6")))
    for Z, nm in ((57, "La 5d/4f"), (89, "Ac 6d/5f"), (90, "Th 6d/5f")):
        print("  %s" % nm + "".join("%10s" % (d["gap"].get((Z, c), "-")) for c in (115.0, 137.035999, 160.0, 170.0, 200.0, 300.0, 1e6)))
    print("La's line in 1/c^2: intercept %+.5f; predicted at 115/200/300: %s" % (d["la_intercept"], d["la_line"]))
    print("local exchange (hfs) step:", d["hfs"])
    print("e-e coupling rows:", d["lam"])


def rebuild(scratch):
    """rebuild the runtime and rerun the three fixture steps (slow: minutes)"""
    sys.path.insert(0, HERE)
    import lowdin_replay as LR
    sha, _ = LR.replay(scratch)
    print("t7b_hf.py sha256 %s anchor" % ("MATCHES" if sha.get("t7b_hf.py") == ANCHOR else "DOES NOT MATCH"))
    open(os.path.join(scratch, "cstep.py"), "w").write(CSTEP)
    for Z, c in ((21, "C0"), (90, "C0"), (90, "1e6")):
        r = subprocess.run([sys.executable, "-W", "ignore", "cstep.py", str(Z), c, "observed"], cwd=scratch,
                           capture_output=True, text=True)
        line = [l for l in r.stdout.splitlines() if l.startswith("RESULT ")]
        o = json.loads(line[0][7:]) if line else {}
        print("  Z=%d c=%s -> %s" % (Z, c, o.get("order", [])[:3] or r.stderr[-300:]))


CSTEP = '''import sys, json, os
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
Z = int(sys.argv[1]); cs = sys.argv[2]
import t7c_kernel as K
if cs != "C0":
    cval = float(cs)
    for name in ("eigen_sr", "numerov_wf_sr", "scf_occ_sr"):
        f = getattr(K, name); d = list(f.__defaults__); co = f.__code__
        names = co.co_varnames[:co.co_argcount]; off = co.co_argcount - len(d)
        for i, nm in enumerate(names[off:]):
            if nm == "c": d[i] = cval
        f.__defaults__ = tuple(d)
import nlchain as NC, nlguard as NG, ground as G
if cs != "C0":
    NC.C0 = cval; NG.C0 = cval          # nlguard passes c=C0 to hfc2.HFC: the lever the record's F54.2 missed
o = NC.step(Z, [tuple(t) for t in G.expand(Z - 1)], {}, "c=" + cs)
print("RESULT " + json.dumps(o), flush=True)
'''

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    if "--rebuild" in sys.argv:
        rebuild(sys.argv[sys.argv.index("--rebuild") + 1])
        sys.exit(0)
    report(compute())
