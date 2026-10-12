#!/usr/bin/env python3
"""tau_share.py -- item 301: "We need to calculate tau before C4 goes to the verifier".  tau is how much of our
stress position 2's sheet receives at the one-way coincidence (j_readings J2; 276 (a): "our sheet's junction carries
our stress alone, position 2's carries ours, received, and its own"), open since j_readings ("The value of tau: J2
shows the conclusion holds for all of it") and item 279 ("if we have the opportunity to do so we should, it may prove
useful elsewhere").  Not P17/P18's tau in c4_oneway, which there names a relative tension.  Worked in the
conversation (computed with sympy, exact where marked; deduced where marked; not verified by a separate session; not
seated); 2026-10-12.

  T0 (read) M's item-301 words, 275's "only the summed stress is fixed" and 139 (1)'s "+4/3 and -1/3", verbatim in the
     rulings file.
  T1 (computed, exact) What the coincidence fixes.  The planes coincide everywhere (275), so at the junction there is
     one surface, and Israel's condition fixes only the summed stress there (275 (b), b5_positive B5a): with each side's
     extrinsic curvature written K^-+ = +-(kappa^2/2)(Sigma^-+ - Sigma^-+ h/3), Sigma^-+ the stress that side carries
     (a lone plane's sides each carrying all of its stress), the jump [K] = -kappa^2 (S - S h/3), S = S1 + S2, holds iff
     Sigma^- + Sigma^+ = 2 (S1 + S2) -- computed for general surface stresses, each a tension part plus a matter part
     (energy density and pressure).  This is the summed stress 275 names, not B5a's composite junction on our side,
     which item 281 marked (W4, position 2's tension in our junction): here our side carries ours alone.
  T2 (computed, exact) tau.  J2's linear junction, our side Sigma^- = S1 + chi S2 and position 2's Sigma^+ = tau S1 +
     S2, meets T1 iff (tau - 1) S1 + (chi - 1) S2 = 0.  Two-way -- one junction both sheets act on, chi = 1 -- gives
     tau = 1.  One-way (chi = 0, 276) gives (tau - 1) S1 = S2: a single number tau exists iff position 2's own stress
     is a tension, and then tau = 1 + lambda_2/lambda_1.  With 139 (1)'s lambda_1 = +4/3 and lambda_2 = -1/3 of the
     Randall-Sundrum value: tau = 3/4, exact.  So tau sigma = lambda_RS: position 2 receives exactly the summed tension
     the coincidence fixes -- the one-plane Randall-Sundrum value, 3/4 of ours.
     [Item 310, the C4 verifier's (7), accepted: this pins J2's split, Sigma+ = tau S1 + S2, position 2's own stress
     counted once; split as tau S1 + 2 S2 -- as T3 itself describes the side, "ours and its own twice" -- the same
     junction gives tau = 1.  For tensions S1 and S2 are proportional, so the split is a convention, and what the
     junction fixes is position 2's side total, Sigma+ = S1 + 2 S2, 2/3 lambda_RS, positive: that and the 2 : 1 bulk are
     the physical content.  tau uses only 139 (1)'s ratio, which is M's; "tau sigma = lambda_RS" and T4's units use its
     sum +4/3 - 1/3 = 1, multiplane M4's normalization (276 (c), a two-way record, the value standing as M's).]
  T3 (computed, exact) With matter on position 2's plane no single number serves: what position 2 receives is the
     summed stress S1 + S2 itself, a tensor, of which tau = 3/4 is the tension part; its side carries S1 + 2 S2 -- ours
     and its own twice, the share of its own that a two-way junction would have put on our side carried on its side.
  T4 (computed, exact; deduced where marked) What tau gives.  Position 2's side carries tau sigma + lambda_2 = sigma/2
     = 2/3 lambda_RS, positive.  For a plane to be flat and static, its side's bulk curvature is kappa^2/6 of the
     tension it carries (computed): our side's 4/3 k and position 2's 2/3 k, k = kappa^2 lambda_RS/6 the composite's
     mean -- the one-way coincidence makes the bulk 2 : 1 across the junction (deduced, if both planes are flat and
     static).  Were both sides at the one curvature k, ours would carry 4/3 of critical and inflate, H^2/c^2 = 7/9 k^2,
     and position 2's 2/3 and sit below flat, -5/9 k^2 (computed): not our universe.  In j_readings' normalization,
     our side at its own k (sigma = 6k/kappa^2), position 2's side needs k/2: the same 2 : 1.
     [Item 310, outside the C4 claim, from its verifier (deduced): one surface carries one induced metric, so the
     coincident sheets share one Hubble rate (Israel's first condition) -- "both sides at the one curvature k: 7/9 and
     -5/9" describes two rates on one surface, which the coincidence forbids -- and that shared induced metric is itself
     a geometric channel between the sheets (for instance 284's displacement where the README lands), which 276's
     one-way junction does not address.  With the bulk 2 : 1 the zero mode gives 1/G4 = (ell_1 + ell_2)/(2 G5): G5 =
     (3/2) G ell over both sides, or G ell/2 over ours alone (if position 2's bulk is not to act on our gravity, 276
     (a)), not G ell -- an O(1) change at flat order in r_h, E and c4_oneway P5's 0.29; M1's clauses are unaffected.]
  T5 (computed) C4's P4 and b5a_oneway's B2 at the value: position 2's share on a ray crossing its plane where the
     README lands, (tau sigma + S2) sin a + (rho + p) cos^2 a / sin a, is positive at tau = 3/4 (it was for every tau
     in [0, 1]; now at the one value).
  T6 (the cypher NOT-RUN, stated) tau is an identity of the junction, not a choice among configurations: an index of
     (chi, tau) rows on the line (tau - 1) lambda_1 + (chi - 1) lambda_2 = 0 would carry the answer as its own column,
     a key (211), as j_readings J5 found for J1-J3.  Not run, and said.

What this does not show.
  - The bulk curvatures themselves: T4's 4/3 k and 2/3 k are what flat, static planes need, not computed from the bulk.
  - tau at the corridor, where the causal structure separates the sheets (J1) and J2's coincidence does not apply.
  - Position 2's matter's received part beyond the tension (T3 states it; nothing here uses it).

Imports b5a_oneway.py by path.  Stdlib + sympy.  python3 tau_share.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M301 = "We need to calculate τ before C4 goes to the verifier"
M275 = "only the summed stress is fixed"
M139 = "+4/3 and -1/3 of the one-plane value"


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def stresses():
    """surface stresses on the induced metric h = diag(-1, 1, 1, 1): a tension part -lambda h plus a perfect-fluid
    matter part diag(rho, p, p, p)"""
    h = sp.diag(-1, 1, 1, 1)
    l1, l2, r1, r2, p1, p2 = sp.symbols("lambda_1 lambda_2 rho_1 rho_2 p_1 p_2", real=True)
    S1 = -l1 * h + sp.diag(r1, p1, p1, p1)
    S2 = -l2 * h + sp.diag(r2, p2, p2, p2)
    return h, S1, S2, (l1, l2, r1, r2, p1, p2)


def trace(h, S):
    return sum(h[i, i] * S[i, i] for i in range(4))          # h is its own inverse here


def junction():
    """T1: one surface, the summed stress fixed; each side's K from the stress it carries"""
    h, S1, S2, syms = stresses()
    k2 = sp.Symbol("kappa2", positive=True)
    # sides carry Sigma^- and Sigma^+; K^- = +(k2/2)(Sigma^- - tr h/3), K^+ = -(k2/2)(Sigma^+ - tr h/3)
    a = sp.symbols("a0:4", real=True)
    b = sp.symbols("b0:4", real=True)
    Sig_m, Sig_p = sp.diag(*a), sp.diag(*b)
    K = lambda Sig, sgn: sgn * k2 / 2 * (Sig - trace(h, Sig) * h / 3)
    S = S1 + S2
    jump = K(Sig_p, -1) - K(Sig_m, +1)
    israel = -k2 * (S - trace(h, S) * h / 3)
    if MUT.get("each_its_own"):
        israel = jump                                       # the mutant: no summed constraint, each sheet its own
    sol = sp.solve([sp.expand(jump[i, i] - israel[i, i]) for i in range(4)], b, dict=True)
    sumrule = None
    if sol and len(sol) == 1 and all(bb in sol[0] for bb in b):
        target = 2 * S
        sumrule = all(sp.simplify(sol[0][b[i]] + a[i] - target[i, i]) == 0 for i in range(4))
    return dict(sumrule=bool(sumrule), h=h, S1=S1, S2=S2, syms=syms)


def tau_value():
    """T2-T3: J2's linear junction against the sum rule; tau for tensions, and the tensor with matter"""
    jn = junction()
    h, S1, S2, (l1, l2, r1, r2, p1, p2) = jn["h"], jn["S1"], jn["S2"], jn["syms"]
    tau, chi = sp.symbols("tau chi", real=True)
    if not jn["sumrule"]:
        return dict(jn=jn, two_way=None, tau_sym=None, tau=None, scalar_with_matter=None, received=None)
    resid = (tau - 1) * S1 + (chi - 1) * S2               # Sigma^- + Sigma^+ - 2 (S1 + S2) for J2's junction
    chi_val = 1 if MUT.get("two_way") else 0
    tensions = {r1: 0, p1: 0, r2: 0, p2: 0}
    two_way = sp.solve([resid.subs(tensions).subs(chi, 1)[0, 0]], tau, dict=True)
    sol = sp.solve([resid.subs(tensions).subs(chi, chi_val)[i, i] for i in range(4)], tau, dict=True)
    tau_sym = sp.simplify(sol[0][tau]) if len(sol) == 1 else None
    l2v = sp.Rational(1, 3) if MUT.get("flipped_139") else -sp.Rational(1, 3)
    vals = {l1: sp.Rational(4, 3), l2: l2v}
    tau_v = tau_sym.subs(vals) if tau_sym is not None else None
    # with matter on position 2's plane (rho_2 != -p_2... any nonzero matter), no scalar tau
    with_matter = sp.solve([resid.subs({r1: 0, p1: 0}).subs(chi, 0)[i, i] for i in range(4)], tau, dict=True)
    rec_tensor = sp.simplify(S1 + S2)                      # what position 2 receives with chi = 0, in general
    carries = sp.simplify(rec_tensor + S2)                  # its side: received + its own
    return dict(jn=jn, two_way=two_way[0][tau] if two_way else None, tau_sym=tau_sym, tau=tau_v, vals=vals,
                scalar_with_matter=bool(with_matter), received=rec_tensor, carries=carries)


def consequences(tv):
    """T4: what position 2's side carries; the curvatures flat, static planes need; one curvature both sides"""
    if tv["tau"] is None:
        return dict(side2=None)
    lam = sp.Symbol("lambda_RS", positive=True)
    k2 = sp.Symbol("kappa2", positive=True)
    l1, l2 = tv["vals"][tv["jn"]["syms"][0]] * lam, tv["vals"][tv["jn"]["syms"][1]] * lam
    side1, side2 = l1, tv["tau"] * l1 + l2
    k = k2 * lam / 6                                        # the composite's mean curvature, Z2 with lambda_RS
    km, kp = sp.simplify(k2 * side1 / 6), sp.simplify(k2 * side2 / 6)
    H1 = sp.simplify((k2 * side1 / 6) ** 2 - k ** 2)        # both sides at k: Randall-Sundrum's brane Friedmann
    H2 = sp.simplify((k2 * side2 / 6) ** 2 - k ** 2)
    return dict(side2=sp.simplify(side2 / lam), km=sp.simplify(km / k), kp=sp.simplify(kp / k),
                mean=sp.simplify((km + kp) / 2 / k), H1=sp.simplify(H1 / k ** 2), H2=sp.simplify(H2 / k ** 2),
                received=sp.simplify(tv["tau"] * l1 / lam))


def p4_at_value(tv):
    """T5: the crossing share at tau = 3/4 (b5a_oneway B2's form)"""
    if tv["tau"] is None:
        return dict(pos=False)
    sig, s = sp.symbols("sigma s", positive=True)
    c2, w = sp.symbols("c2 w", nonnegative=True)
    S2p = sp.Symbol("S2p", positive=True)                   # position 2's own total where the README lands, E7
    share = (tv["tau"] * sig + S2p) * s + w * c2 / s
    B5 = _load("b5a_oneway.py", "ts_b5a")
    b2 = B5.shares()["theirs_pos"]
    return dict(pos=bool(share.is_positive), b2=b2)


def compute():
    tv = tau_value()
    return dict(tv=tv, cq=consequences(tv), p4=p4_at_value(tv))


def report(o):
    tv, cq = o["tv"], o["cq"]
    print("tau_share.py -- tau at the one-way coincidence (item 301)\n")
    print("T1 one surface, the summed stress fixed: Sigma^- + Sigma^+ = 2 (S1 + S2): %s" % tv["jn"]["sumrule"])
    print("T2 two-way tau = %s; one-way tau = %s = %s at 139 (1)'s +4/3, -1/3" % (tv["two_way"], tv["tau_sym"],
                                                                                tv["tau"]))
    print("T3 a single tau with matter on position 2's plane: %s; received in general: S1 + S2" % (
        tv["scalar_with_matter"]))
    print("T4 position 2's side carries %s lambda_RS; tau sigma = %s lambda_RS; flat static planes need our side %s k, "
          "position 2's %s k (mean %s k); both at k: ours H^2/c^2 = %s k^2, position 2's %s k^2" % (
              cq["side2"], cq["received"], cq["km"], cq["kp"], cq["mean"], cq["H1"], cq["H2"]))
    print("T5 the crossing share at tau = 3/4 positive: %s (b5a_oneway B2: %s)" % (o["p4"]["pos"], o["p4"].get("b2")))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("T0 M's item-301 words, 275's and 139 (1)'s, verbatim in the rulings file",
        M301 in rul and M275 in rul and M139 in rul)
    tv, cq = o["tv"], o["cq"]
    add("T1 one surface, the summed stress fixed: the sides carry 2 (S1 + S2) between them", tv["jn"]["sumrule"])
    add("T2 two-way tau = 1; one-way tau = 1 + lambda_2/lambda_1 = 3/4, exact; tau sigma = lambda_RS",
        tv["two_way"] == 1 and tv["tau_sym"] is not None and sp.simplify(tv["tau_sym"] - (1 + tv["jn"]["syms"][1] /
                                                                                         tv["jn"]["syms"][0])) == 0
        and tv["tau"] == sp.Rational(3, 4) and cq.get("received") == 1)
    add("T3 with matter on position 2's plane no single tau; what it receives is S1 + S2",
        tv["received"] is not None and not tv["scalar_with_matter"]
        and sp.simplify(tv["received"] - (tv["jn"]["S1"] + tv["jn"]["S2"])) == sp.zeros(4))
    add("T4 position 2's side carries 2/3 lambda_RS; flat static planes need 4/3 k and 2/3 k, mean k; both at k: 7/9 and "
        "-5/9", cq["side2"] == sp.Rational(2, 3) and cq.get("km") == sp.Rational(4, 3)
        and cq.get("kp") == sp.Rational(2, 3) and cq.get("mean") == 1 and cq.get("H1") == sp.Rational(7, 9)
        and cq.get("H2") == -sp.Rational(5, 9))
    add("T5 C4's P4 / b5a_oneway B2 at tau = 3/4: the crossing share positive", o["p4"]["pos"] and o["p4"].get("b2"))
    return res


MUTANTS = {"two_way": "one junction both sheets act on (chi = 1)",
           "flipped_139": "position 2's tension +1/3 instead of 139 (1)'s -1/3",
           "each_its_own": "no summed constraint, each sheet's junction its own"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-13s %-50s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
