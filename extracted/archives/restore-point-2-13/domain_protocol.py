#!/usr/bin/env python3
"""domain_protocol.py -- the check that must pass before any fit.

THE ERROR THIS EXISTS TO STOP

Repeatedly in the Loewdin work I pooled data across cells the index says are
separate, fitted one coefficient to the pool, and reported the result. Every
time, the per-cell results were already correct and the pooled one was worse or
meaningless. The occurrences:

  · law 2 fitted on six hand-picked species across periods: r2 0.868.
    On all nineteen, in the right carrier, 0.356. Register 1285.
  · the amplitude Gaussian fitted across the whole table, then refuted by the
    noble-gas calibration. Register 1301.
  · brackets computed for neutrals only and called "the atom's" -- three times.
    Registers 1313, and corrected again at 1315.
  · six occupancy slopes pooled to find "one scaling": cv 1.0, meaningless.
    The four per-subshell slopes were already significant at p < 0.001.

WHY THE INDEX FORBIDS IT

Lambda_phys closes on (source, domain) as a staircase. NO parameter of this work
sits in the universal column. Every one holds on a region. A pooled fit across
regions asserts a universal parameter, which the closed index says does not
exist. This is not a stylistic preference -- it is a structural prohibition that
the compendium's own closure states.

THE PROTOCOL

Before any fit, answer these four in writing. If any answer is wrong, the fit
does not run.

  1 DOMAIN     Which single cell of Lambda_phys does this quantity live in?
               Name it: (source, domain). If the data spans more than one
               domain cell, STOP -- fit each cell separately.

  2 CARRIER    Which carrier does the closed law index assign to this law?
               u, p, l-l_core, Z-T. Fitting in another carrier is the law-2
               error. If the carrier is untested, test it before fitting.

  3 COUNT      How many data points are in THIS cell, and how many free
               parameters does the form have? If points < 3 x parameters,
               report the measurement, not a fit.

  4 POOLING    Am I about to combine cells to get more points? If yes, STOP.
               The index says those cells are separate. More points obtained
               by pooling are not more evidence -- they are a different and
               forbidden claim.

AND THE REPORTING RULE

A per-cell result is reported as a list of measurements with their own
statistics. It is NEVER summarised by a single fitted number across cells, and
a "median across cells" is not a result -- it is a pooled fit in disguise.
"""

CELLS_OF_LAMBDA_PHYS = {
    ("standard",    "universal"),
    ("mathematics", "universal"),
    ("mathematics", "all elements"),
    ("literature",  "all elements"),
    ("literature",  "low"),
    ("this work",   "all elements"),
    ("this work",   "low"),
    ("this work",   "neutral"),
    ("this work",   "hydrogenic"),
}

CARRIERS = {
    "amplitude":       "u",
    "charge exponent": "u",
    "l-spread":        "p",
    "Pauli floor":     "p",
    "regimes":         "p",
    "gate":            "l-l_core",
    "collapse switch": "Z-T",
    "occupancy slope": "the subshell itself",   # measured within (n,l)
}

def check(name, source, domains, carrier, n_points, n_params, pooling):
    """run the protocol. returns (ok, reasons)."""
    bad = []
    if len(domains) > 1:
        bad.append(f"spans {len(domains)} domain cells: {sorted(domains)} "
                   f"-- fit each separately")
    for d in domains:
        if (source, d) not in CELLS_OF_LAMBDA_PHYS:
            bad.append(f"({source}, {d}) is not a cell of Lambda_phys")
    want = CARRIERS.get(name)
    if want and carrier != want:
        bad.append(f"carrier is {carrier!r}, the law index assigns {want!r}")
    if n_points < 3 * n_params:
        bad.append(f"{n_points} points for {n_params} parameters "
                   f"-- report the measurement, not a fit")
    if pooling:
        bad.append("pooling across cells -- forbidden")
    return (not bad), bad

if __name__ == "__main__":
    print("  THE DOMAIN PROTOCOL — run before any fit\n")
    print("      1 DOMAIN   which single cell of Λ_phys?")
    print("      2 CARRIER  which carrier does Λ_law assign?")
    print("      3 COUNT    points ≥ 3 × parameters in THIS cell?")
    print("      4 POOLING  am I combining cells for more points?  → STOP\n")

    print("  REPLAYING TODAY'S FITS THROUGH IT\n")
    TESTS = [
        ("l-spread", "this work", {"all elements"}, "u", 6, 2, True,
         "law 2 on six hand-picked species"),
        ("l-spread", "this work", {"all elements"}, "p", 19, 2, False,
         "law 2 in the right carrier"),
        ("amplitude", "this work", {"neutral", "low", "hydrogenic"}, "u", 41, 3, True,
         "the Gaussian across the whole table"),
        ("occupancy slope", "this work", {"all elements"}, "n²", 6, 2, True,
         "six slopes pooled for one scaling"),
        ("occupancy slope", "this work", {"all elements"},
         "the subshell itself", 7, 2, False,
         "the 4d slope, measured within 4d"),
    ]
    for nm, src, dom, car, npt, npr, pool, label in TESTS:
        ok, why = check(nm, src, dom, car, npt, npr, pool)
        print(f"      {label:<42}{'PASS' if ok else 'BLOCKED'}")
        for w in why:
            print(f"          · {w}")
    print()
    print("  THE REPORTING RULE\n")
    print("      per-cell results are reported as a LIST of measurements with")
    print("      their own statistics. never summarised by one fitted number")
    print("      across cells. a 'median across cells' is a pooled fit in")
    print("      disguise and is not a result.")
