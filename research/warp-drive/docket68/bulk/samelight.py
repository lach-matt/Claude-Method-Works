#!/usr/bin/env python3
"""samelight.py -- M's answers to walls A and B (M-RULINGS item 143), followed through.

M: "A - the only thing that can cross is that which can cross the horizon of a black hole.  B - light likely doesn't
vary".  The board's reading of B for the Löwdin walk: its one entered constant c = 137.035999 = 1/alpha in atomic units
(recovered/BODY2-CHAPTER-35-THE-LOWDIN-SOLUTION.md: "c = 137.035999 as the only entered constant") is the same in every
universe (H-LIGHT-INVARIANT).

  L1  what alpha does to a spectrum: hydrogen-like Dirac levels E(n, j) = m c^2 [1 + (Z alpha/(n - d_j))^2]^(-1/2),
      d_j = j + 1/2 - sqrt((j + 1/2)^2 - (Z alpha)^2).  Change alpha by eps and the ratio of the 2p fine-structure
      interval to Lyman-alpha moves by ~2 eps -- a shift that differs from line to line, so it is NOT degenerate with
      redshift.  Hold alpha fixed (M's B) and every ratio is identical (STRUCTURAL)
  L2  what a uniform scaling does (a redshift, the nucleus's mass at leading order): every ratio unchanged -- the
      control, and the reason those cannot tell universes apart
  L3  the Löwdin walk (READ, deduced): one entered constant, so under H-LIGHT-INVARIANT the walk returns the same
      107 entrants, the same three exceptions and the same twelve unwitnessed rows in every universe.  Item 138's
      "measure exactly as are ours do" then follows for the electrons; what could differ lies outside the walk -- the
      nucleus (its mass, its size, which nuclei are stable)
  L4  item 143 A against the corridor: plane.py P1 (seated) computes that the corridor's horizon is crossed one way,
      1 -> 2, leaving through a white-hole horizon on position 2's side; anything that crosses a horizon inward --
      matter, light, gravitational waves -- is admitted by A
Stdlib only.  python3 samelight.py [--selftest]
"""
import math
import sys

ALPHA = 1 / 137.035999


def dirac(n, j, alpha, Z=1):
    k = j + 0.5
    dj = k - math.sqrt(k * k - (Z * alpha) ** 2)
    return 1 / math.sqrt(1 + (Z * alpha / (n - dj)) ** 2)          # in units of m c^2


def lines(alpha, scale=1.0):
    """Lyman-alpha (2p3/2 -> 1s1/2), H-alpha (3d5/2 -> 2p3/2) and the 2p fine-structure interval, times a uniform scale."""
    e = lambda n, j: dirac(n, j, alpha)
    lya = e(2, 1.5) - e(1, 0.5)
    ha = e(3, 2.5) - e(2, 1.5)
    fs = e(2, 1.5) - e(2, 0.5)
    return {k: v * scale for k, v in (("lya", lya), ("ha", ha), ("fs2p", fs))}


def ratios(L):
    return {"fs/lya": L["fs2p"] / L["lya"], "ha/lya": L["ha"] / L["lya"]}


def compute(eps=1e-4):
    base = ratios(lines(ALPHA))
    var = ratios(lines(ALPHA * (1 + eps)))
    same = ratios(lines(ALPHA))
    scaled = ratios(lines(ALPHA, scale=1 / (1 + 1089.0)))            # a redshift
    mass = ratios(lines(ALPHA, scale=1 / (1 + 5.48579909065e-4 / 1.00728)))   # hydrogen's reduced mass, leading order
    rel = {k: var[k] / base[k] - 1 for k in base}
    return {"eps": eps, "base": base, "rel_alpha": rel,
            "rel_same": {k: same[k] / base[k] - 1 for k in base},
            "rel_redshift": {k: scaled[k] / base[k] - 1 for k in base},
            "rel_mass": {k: mass[k] / base[k] - 1 for k in base}}


def report(d):
    print("samelight.py -- walls A and B, followed through (item 143)\n")
    print("L1 alpha changed by %.0e: fs(2p)/Ly-a moves by %.3e (= %.2f eps); H-a/Ly-a by %.3e -- line to line, not uniform"
          % (d["eps"], d["rel_alpha"]["fs/lya"], d["rel_alpha"]["fs/lya"] / d["eps"], d["rel_alpha"]["ha/lya"]))
    print("   alpha held (M's B): %s" % d["rel_same"])
    print("L2 control, uniform scalings: a redshift z = 1089 %s; hydrogen's reduced mass %s"
          % ({k: "%.1e" % v for k, v in d["rel_redshift"].items()}, {k: "%.1e" % v for k, v in d["rel_mass"].items()}))
    print("L3 (READ, deduced) the walk's one entered constant is alpha: held, the walk's table is the same in every universe")
    print("L4 (plane.py P1, seated) the corridor's horizon is crossed one way, 1 -> 2; A admits whatever crosses a horizon")


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    r = d["rel_alpha"]["fs/lya"] / d["eps"]
    chk("L1: a change of alpha by eps moves fs(2p)/Ly-a by about 2 eps (1.9 to 2.1)", 1.9 < r < 2.1)
    chk("L1: the two ratios move by different amounts -- the shift differs from line to line",
        abs(d["rel_alpha"]["fs/lya"] - d["rel_alpha"]["ha/lya"]) > 1e-5)
    chk("L1 (STRUCTURAL): alpha held, every ratio is identical", all(v == 0 for v in d["rel_same"].values()))
    chk("L2 control (STRUCTURAL): a redshift leaves every ratio unchanged to 1e-14", all(abs(v) < 1e-14 for v in d["rel_redshift"].values()))
    chk("L2 control (STRUCTURAL): the nucleus's mass, at leading order, leaves every ratio unchanged to 1e-14",
        all(abs(v) < 1e-14 for v in d["rel_mass"].values()))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
