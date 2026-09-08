#!/usr/bin/env python3
"""explore.py -- the design space, SEARCHED rather than evaluated.

Every other instrument here takes a configuration and returns its balance.
powersource.py inverts that once: it sets the balance to unity and returns
the configuration. Neither of them SEARCHES, and until something does, the
question "how many redesigns does this plant need before it is optimal" has
no answer here at all -- not a hard one, an absent one.

So this varies the configuration across every axis the design actually has,
holding the rest at the design point, and reports three things:

  WHICH AXES MOVE THE ANSWER, ranked, because a design space is not a list of
    knobs -- most of them do nothing and saying which is most of the work;
  WHAT STATUS EACH AXIS CARRIES, because an axis closed by a fact about
    matter, an axis closed by a recorded decision, an axis that is a free
    engineering choice and an axis that is an unmeasured constant are four
    different things and only one of them is a redesign;
  HOW MUCH OF THE MOVEMENT IS DESIGN AND HOW MUCH IS ASSUMPTION.

IT REFUSES TO REPORT AN OPTIMUM, and the refusal is the point. An optimum
over a space whose largest free swing is an unmeasured constant is a
statement about the constant and not about the plant. What it reports
instead is the REDESIGN CEILING -- everything redesign can buy at the
decisions already taken -- and the MEASUREMENT EXPOSURE, which is what the
unmeasured constants can cost if they go the wrong way. Those two numbers
are not the same kind of number, and this file's whole content is that they
are not close.

Stdlib only. python3 tools/explore.py [--selftest]
"""

import argparse
import collections
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import powersource as P                                        # noqa: E402

# ---- THE OBJECTIVE ------------------------------------------------------
# BEAM POWER TO SERVE THE BASELINE, in MW, and lower is better. It is the
# right single objective for this plant and not an arbitrary one:
#   - the households are FIXED by the objective the project was given, so
#     what varies is what it costs to serve them;
#   - the beam is what every criterion runs through -- the accelerator is the
#     capital, the recirculated electricity, the driver count, the standby
#     and the reason for the 8 GeV;
#   - startcost.py's two dominant build items are the driver and its shield,
#     so build energy follows the beam rather than opposing it.
# Where an axis's cost does NOT run through the beam -- the stopping window's
# tritium, the module count's buildability -- that is stated beside its row
# rather than folded into a score. A single number that hides a trade is
# worse than two numbers that show it.
BASELINE_HOUSEHOLDS = P.STATION_HOUSEHOLDS
DESIGN_POINT = {
    "module_mw": P.SPALL_TARGET_MW["ESS, design"],
    "k_eff": P.K_DESIGN,
    "window": P.STATION_WINDOW_MEV,
    "linac_mw": P.LINAC_BEAM_MW,
    "standby_kw": P.REF_STANDBY_KW,
    "eta_acc": 0.30,
    "y_fus": None,
}

# ---- THE STATUSES, AND THEY ARE NOT DEGREES OF THE SAME THING -----------
PHYSICS = "PHYSICS"        # closed by a fact about matter. Not an axis.
DECIDED = "DECIDED"        # open in principle; closed by a recorded decision
DESIGN = "DESIGN"          # a free engineering choice, and the only kind of
                           # axis a REDESIGN can move
ASSUMED = "ASSUMED"        # a constant carrying that status in its own file
UNMEASURED = "UNMEASURED"  # a band nothing in this work has measured
REDESIGNABLE = (DESIGN,)
OWED = (ASSUMED, UNMEASURED)

Axis = collections.namedtuple(
    "Axis", "name key values status owner note")

AXES = (
    Axis("multiplication k", "k_eff",
         (0.80, 0.85, 0.875, 0.89, P.K_DESIGN), DECIDED, "criticality.py",
         "capped at 0.900 by the always-subcritical property; above it the "
         "hazard class comes back"),
    Axis("accelerator efficiency", "eta_acc",
         (0.20, 0.30, 0.40, 0.50), DESIGN, "powersource.py",
         "SOURCED band, wall plug to beam; the high end is the design target "
         "for a superconducting machine"),
    Axis("driver power", "linac_mw",
         (1.40, 4.00, 5.00, 10.00, 15.00, 20.00), ASSUMED, "powersource.py",
         "LINAC_BEAM_MW is ASSUMED at 20; the low end is the largest ever "
         "OPERATED"),
    Axis("driver standby", "standby_kw",
         (P.STANDBY_LO_KW, P.REF_STANDBY_KW, P.STANDBY_HI_KW), UNMEASURED,
         "powersource.py",
         "a band for a machine of unstated size, and its SCALING LAW is "
         "stated nowhere -- see --linac"),
    Axis("stopping window", "window",
         (150.0, 265.0, 400.0), DESIGN, "collector.py",
         "NOT a free lever: --stopping prices it in tritium, 1.93x for 1.11x "
         "in muons"),
    Axis("module power", "module_mw",
         tuple(sorted(P.SPALL_TARGET_MW.values())), DESIGN, "powersource.py",
         "buildability, not energy -- --rescale found the beam is set by the "
         "multiplication"),
    Axis("muon channel", "y_fus",
         (None, 0.0), DECIDED, "environment.py",
         "route C is chosen on the stated criterion; route A is the "
         "project's subject"),
)


def objective(**over):
    """Beam MW to serve the baseline. inf where the plant does not close."""
    cfg = dict(DESIGN_POINT)
    cfg.update(over)
    try:
        return P.station(households=BASELINE_HOUSEHOLDS, **cfg)["beam_mw"]
    except ValueError:
        return float("inf")


def sweep(axis):
    """[(value, objective)] along one axis, everything else at the point."""
    return [(v, objective(**{axis.key: v})) for v in axis.values]


def swing(axis):
    """Worst over best along the axis. inf where some value does not close."""
    vals = [o for _v, o in sweep(axis)]
    lo = min(vals)
    hi = max(vals)
    if lo <= 0:
        raise ValueError(f"axis {axis.name!r} returned a non-positive beam")
    return hi / lo


def closure_floor(key="k_eff", lo=0.50, hi=None, tol=1e-5):
    """The value of an axis below which NO station of any size closes.

    Bisection on a monotone predicate, which is what it is: gain rises with
    k, and a plant that cannot cover its own recirculation cannot be made to
    by building more of it."""
    hi = DESIGN_POINT[key] if hi is None else hi
    if not math.isfinite(objective(**{key: hi})):
        raise ValueError(f"{key} does not close at the design point")
    if math.isfinite(objective(**{key: lo})):
        raise ValueError(f"{key} already closes at {lo}, so there is no floor")
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if math.isfinite(objective(**{key: mid})):
            hi = mid
        else:
            lo = mid
    return hi


def elasticity(key, step=0.01):
    """d ln(beam) / d ln(x) at the design point, one-sided and downward.

    Downward on purpose: what it costs when a term comes in WORSE than
    assumed is the question a design has to answer."""
    x0 = DESIGN_POINT[key]
    b0 = objective()
    b1 = objective(**{key: x0 * (1.0 - step)})
    if not math.isfinite(b1):
        return float("-inf")
    return (b1 / b0 - 1.0) / (-step)


def redesign_ceiling():
    """The best the plant reaches on the axes a REDESIGN may move.

    Every DESIGN axis at its best value at once, with the decisions kept.
    This is an upper bound on redesign and not a proposal: the window's
    tritium cost and the module's buildability are not in the objective."""
    best = {}
    for ax in AXES:
        if ax.status in REDESIGNABLE:
            best[ax.key] = min(ax.values, key=lambda v: objective(
                **{ax.key: v}))
    return objective(**best), best


def measurement_exposure():
    """What the axes nothing has measured can cost if they go the wrong way.

    The worst value of each OWED axis at once. Not a prediction -- a bound on
    the consequence of not having measured."""
    worst = {}
    for ax in AXES:
        if ax.status in OWED:
            worst[ax.key] = max(ax.values, key=lambda v: objective(
                **{ax.key: v}))
    return objective(**worst), worst


def pair_scan():
    """Every pair of axes, worst joint value against the product of singles.

    ONE AT A TIME IS NOT A SEARCH. The ranking holds every other axis at the
    design point, which is exactly the assumption a design space breaks. This
    is the cheapest thing that can catch it, and it is not a full search
    either -- it is pairs, and a triple could be worse still."""
    import itertools
    b0 = objective()
    rows = []
    for a, b in itertools.combinations(AXES, 2):
        sa, sb = swing(a), swing(b)
        worst = 0.0
        for va in a.values:
            for vb in b.values:
                o = objective(**{a.key: va, b.key: vb})
                worst = float("inf") if not math.isfinite(o) else max(
                    worst, o / b0)
                if not math.isfinite(worst):
                    break
            if not math.isfinite(worst):
                break
        ratio = worst / (sa * sb)
        rows.append((ratio, a, b, sa, sb, worst))
    return sorted(rows, key=lambda t: (-t[0], -t[5]))


def _axis(key):
    for ax in AXES:
        if ax.key == key:
            return ax
    raise ValueError(f"no axis named {key!r}")


def _fmt(x):
    return "does not close" if not math.isfinite(x) else f"{x:,.1f}"


def report():
    b0 = objective()
    print()
    print("  THE DESIGN SPACE, SEARCHED")
    print()
    print(f"    OBJECTIVE  beam MW to serve {BASELINE_HOUSEHOLDS:,.0f}"
          " households. Lower is better.")
    print(f"    THE POINT  {b0:,.0f} MW, at the decisions already recorded.")
    print()
    print("    EVERY AXIS THE DESIGN HAS, AND WHAT MOVING IT DOES")
    print()
    ranked = sorted(AXES, key=lambda a: -swing(a))
    print("      axis                    status       swing   range of beam MW")
    for ax in ranked:
        vals = [o for _v, o in sweep(ax)]
        sw = swing(ax)
        sws = "unbounded" if not math.isfinite(sw) else f"{sw:8.2f}x"
        print(f"      {ax.name:<22} {ax.status:<11} {sws:>10}"
              f"   {_fmt(min(vals))} to {_fmt(max(vals))}")
    print()
    print("      and what each one is:")
    for ax in ranked:
        print(f"        {ax.name:<22} {ax.note}")
    print()
    print("    THE FIRST READING IS THE RANKING ITSELF. One axis dominates")
    print("    and it is CLOSED -- not by physics, by a decision the author")
    print("    took and the reason is on the record. The next two are an")
    print("    engineering choice and a constant nobody has measured, and")
    print("    NOTHING ELSE MOVES THE ANSWER BY MORE THAN FIFTEEN PERCENT.")
    print()
    print("    AND THE RANKING'S OWN LIMIT IS THE SECOND READING. One axis")
    print("    at a time cannot see an interaction. Every pair was scanned,")
    print("    and the ranking above is not merely incomplete -- it is")
    print("    optimistic:")
    print()
    print("      pair                                        singles"
          "     both at once   vs product")
    for ratio, a, b, sa, sb, joint in pair_scan()[:5]:
        r = "unbounded" if not math.isfinite(ratio) else f"{ratio:8.2f}x"
        j = "no closure" if not math.isfinite(joint) else f"{joint:8.2f}x"
        print(f"      {a.name} x {b.name}"
              f"{'':<{max(0, 42 - len(a.name) - len(b.name) - 3)}}"
              f" {sa:5.2f},{sb:5.2f} {j:>14} {r:>12}")
    dead = [t for t in pair_scan() if not math.isfinite(t[5])]
    print()
    print(f"    {len(dead)} PAIRS TAKE THE PLANT TO NO CLOSURE AT ALL, each of"
          " them a large")
    print("    axis against another large one. So the design point is not")
    print("    near one cliff, it is near several, and the one-at-a-time")
    print("    table understates every one of them. The worst pair that does")
    lin_sb = [t for t in pair_scan()
              if {t[1].key, t[2].key} == {"linac_mw", "standby_kw"}][0]
    print(f"    still close is the driver's own two axes at"
          f" {lin_sb[5]:.1f}x, against a product")
    print(f"    of {lin_sb[3] * lin_sb[4]:.2f} -- a small driver and a standby"
          " that does not shrink with")
    print("    it are the same question asked twice, and the table hides that")
    print("    by holding one while it moves the other.")
    print()
    floor = closure_floor()
    print("    AND THE DOMINANT AXIS SITS ON A CLIFF, which nothing here had")
    print("    stated.")
    print()
    print(f"      the plant closes only above k = {floor:.3f}")
    print(f"      the design runs at        k = {P.K_DESIGN:.3f}")
    print(f"      the whole design lives in the last"
          f" {P.K_DESIGN - floor:.3f} of multiplication")
    print()
    for k in (0.78, 0.80, 0.85, 0.875, P.K_DESIGN):
        print(f"        k = {k:.3f}   {_fmt(objective(k_eff=k)):>18} MW")
    print()
    print(f"      elasticity at the point   {elasticity('k_eff'):.1f}")
    print("      -- a one percent fall in k costs about seventeen percent")
    print("         more beam, and the curve steepens the whole way down.")
    print()
    print("    SO THE PLANT IS NOT SHORT OF REDESIGNS. It is short of")
    print("    MEASUREMENTS, and those are two different shortages:")
    print()
    ceil_b, ceil_c = redesign_ceiling()
    exp_b, exp_c = measurement_exposure()
    print(f"      REDESIGN CEILING     {_fmt(ceil_b)} MW against"
          f" {b0:,.0f} -- a factor of {b0 / ceil_b:.2f}")
    print("        every DESIGN axis at its best value at once, decisions")
    print("        kept:", ", ".join(f"{k}={v}" for k, v in
                                     sorted(ceil_c.items())))
    print(f"      MEASUREMENT EXPOSURE {_fmt(exp_b)}")
    print("        every UNMEASURED and ASSUMED axis at its worst at once:",
          ", ".join(f"{k}={v}" for k, v in sorted(exp_c.items())))
    print()
    print("    READ THOSE TWO AGAINST EACH OTHER AND THE ANSWER IS NOT A")
    print("    NUMBER, IT IS A KIND. Redesigning everything that is open to")
    print(f"    redesign is worth {b0 / ceil_b:.2f}x. Being wrong about the"
          " constants nobody has")
    print(f"    measured is worth {exp_b / b0:.1f}x --"
          f" {(exp_b / b0) / (b0 / ceil_b):.0f} times as much, in the other"
          " direction.")
    print("    And with the accelerator efficiency at the low end of its own")
    print("    SOURCED band as well, the plant does not close at all:")
    print(f"      {_fmt(objective(eta_acc=0.20, **exp_c))}.")
    print()
    print("    A design space is not explored by iterating over the first")
    print("    while the second is open. That is not a counsel of patience --")
    print("    it is that the iteration would be measuring the assumptions")
    print("    with a plant, which is the most expensive instrument anyone")
    print("    has ever proposed for the job.")
    print()
    print("    THIS FILE THEREFORE REPORTS NO OPTIMUM. An optimum over a")
    print("    space whose largest free swing is an unmeasured constant is a")
    print("    statement about the constant. What it reports is the order to")
    print("    work in, and the order is not the designer's instinct:")
    print()
    print("      1. THE STANDBY SCALING LAW. One number from an operating")
    print("         superconducting proton linac -- its fixed cryogenic and")
    print("         rf load beside its beam power. Decides whether a station")
    print("         of machines that exist is possible at all.")
    print("      2. THE WALL-PLUG-TO-BEAM EFFICIENCY at this power, measured")
    print("         rather than banded. Worth 2.0x on its own and it is the")
    print("         largest genuinely OPEN axis in the table.")
    print("      3. THE TRANSPORT CALCULATION on the fissile fraction, which")
    print("         is what actually places k. The one-group model is worth")
    print("         about fifteen percent on an absolute k, and at an")
    print(f"         elasticity of {elasticity('k_eff'):.0f} that fifteen"
          " percent is the plant.")
    print()
    print("    ONLY AFTER THOSE THREE IS A REDESIGN A DESIGN DECISION RATHER")
    print("    THAN A GUESS ABOUT A MEASUREMENT.")
    print()


def selftest():
    fail = 0

    def check(label, ok):
        nonlocal fail
        if not ok:
            fail += 1
        print(f"  {label:<64} {'PASS' if ok else 'FAIL'}")

    def raises(fn):
        try:
            fn()
        except ValueError:
            return True
        return False

    def out_of(fn):
        import contextlib as _c
        import io as _io
        b = _io.StringIO()
        with _c.redirect_stdout(b):
            fn()
        return b.getvalue()

    print()
    print("  the objective, and that it is the design point")
    b0 = objective()
    check("the design point closes", math.isfinite(b0))
    check("  -- and reproduces powersource's own re-scaled station",
          b0 == P.station(module_mw=P.SPALL_TARGET_MW["ESS, design"],
                          k_eff=P.K_DESIGN)["beam_mw"])
    check("a configuration that cannot close returns inf rather than raising",
          not math.isfinite(objective(k_eff=0.60)))

    print()
    print("  the ranking, and that it is a fact about the plant")
    ranked = sorted(AXES, key=lambda a: -swing(a))
    check("multiplication is the dominant axis", ranked[0].key == "k_eff")
    check("  -- and it is DECIDED, so its swing is not available",
          ranked[0].status == DECIDED)
    small = [a for a in AXES if a.key in ("module_mw", "window", "y_fus")]
    check("module power, window and route are all under 1.2x",
          all(swing(a) < 1.2 for a in small))
    check("  -- so the design space is NARROW, which is the finding",
          sum(1 for a in AXES if swing(a) > 2.0) <= 3)

    print()
    print("  the cliff")
    floor = closure_floor()
    check("there is a multiplication below which nothing closes",
          0.70 < floor < P.K_DESIGN)
    check("  -- and the design sits close above it",
          P.K_DESIGN - floor < 0.15)
    check("  -- with the objective rising without bound as it is approached",
          objective(k_eff=floor + 0.002) > 10.0 * b0)
    check("the elasticity in k is large and negative",
          elasticity("k_eff") < -10.0)
    check("a floor is refused where the axis already closes at the bottom",
          raises(lambda: closure_floor("k_eff", lo=P.K_DESIGN - 1e-9)))

    print()
    print("  redesign against measurement, which is the whole file")
    ceil_b, _c = redesign_ceiling()
    exp_b, _e = measurement_exposure()
    check("redesign improves the plant", ceil_b < b0)
    check("  -- and by less than a factor of two", b0 / ceil_b < 2.0)
    check("the unmeasured axes can cost more than redesign can buy",
          exp_b / b0 > b0 / ceil_b)
    check("  -- by more than an order of magnitude",
          (exp_b / b0) / (b0 / ceil_b) > 10.0)
    # AND WITH ONE DESIGN AXIS AT THE LOW END OF ITS OWN SOURCED BAND, the
    # plant stops existing. Pinned because it is the sentence the report
    # makes, and it is only true with that term included.
    check("  -- and with eta_acc at its band's low end too, nothing closes",
          not math.isfinite(objective(eta_acc=0.20, **_e)))
    d_lin = swing(_axis("linac_mw"))
    d_sb = swing(_axis("standby_kw"))
    joint = objective(linac_mw=1.4, standby_kw=P.STANDBY_HI_KW) / b0
    check("driver power and standby INTERACT, far past their product",
          joint > 5.0 * d_lin * d_sb)
    pairs = pair_scan()
    dead = [t for t in pairs if not math.isfinite(t[5])]
    check("  -- and pairs are scanned rather than asserted about",
          len(pairs) == len(AXES) * (len(AXES) - 1) // 2)
    check("  -- several pairs reach no closure, which one-at-a-time misses",
          len(dead) >= 3)
    check("  -- every one of them pairs two of the three largest axes",
          all({t[1].key, t[2].key} <= {"k_eff", "eta_acc", "linac_mw"}
              for t in dead))
    check("  -- and the report says the ranking is OPTIMISTIC, not just"
          " incomplete",
          "it is" in out_of(report) and "optimistic" in out_of(report))
    check("an unknown axis name is refused", raises(lambda: _axis("nope")))
    check("no OWED axis is counted as redesignable",
          not any(a.status in REDESIGNABLE for a in AXES
                  if a.status in OWED))
    check("every axis carries a status and an owner",
          all(a.status in (PHYSICS, DECIDED, DESIGN, ASSUMED, UNMEASURED)
              and a.owner.endswith(".py") for a in AXES))

    print()
    print("  the refusal")
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("the report renders", len(out) > 2000)
    check("  -- and states that it reports no optimum",
          "REPORTS NO OPTIMUM" in out)
    check("  -- and names the three measurements, in order",
          all(s in out for s in ("STANDBY SCALING LAW",
                                 "WALL-PLUG-TO-BEAM EFFICIENCY",
                                 "TRANSPORT CALCULATION")))
    check("  -- and does not print the word 'optimal' as a verdict",
          "is optimal" not in out.lower())

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    return report()


if __name__ == "__main__":
    sys.exit(main())
