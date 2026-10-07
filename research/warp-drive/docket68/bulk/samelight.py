#!/usr/bin/env python3
"""samelight.py -- M's answers to walls A and B (M-RULINGS item 143), followed through.

M: "A - the only thing that can cross is that which can cross the horizon of a black hole.  B - light likely doesn't
vary".  The board's reading of B for the Löwdin walk (H-ALPHA-IS-LIGHT): its one entered constant c = 137.035999 = 1/alpha
in atomic units (method/members/THE-LOWDIN-SOLUTION-2.md l.35: "with c = 137.035999 the only entered constant") is the
same in every universe.  The walk's nucleus is a point charge of infinite mass ("their attraction -Z/r to the nucleus",
l.72), so the walk is silent on the nucleus.

First written with three faults the verifier found: a float-cancellation value (1.97 for an exact 2.000), "a different
nuclear mass scales every line by the same factor ... no spectrum can tell", and "chemistry is the same"; corrected
(SAMELIGHT.md History).

  L1  what alpha does to a spectrum (50-digit arithmetic): hydrogen-like Dirac levels E(n, j) = m c^2 [1 + (Z alpha/
      (n - d_j))^2]^(-1/2).  Change alpha by eps and fs(2p)/Lyman-alpha moves by 2.000 eps; H-alpha/Lyman-alpha by
      -2.4e-9 at eps = 1e-4 -- line to line, so a different alpha is visible against a redshift.  Alpha held: identical
      (STRUCTURAL)
  L2  what a uniform scaling does -- a redshift, the electron's mass with alpha held, the nucleus's mass at leading
      order: every ratio unchanged (STRUCTURAL)
  L3  BEYOND leading order the nucleus IS visible: the hydrogen 21 cm hyperfine line scales as g_p (m_e/m_p) alpha^2 Ry
      (standard, not READ here), so its ratio to Lyman-alpha moves by -eps when m_p changes by +eps, where every
      electronic ratio stays put.  Isotope shifts (mass and field) and molecular lines do the same -- the route by which
      m_p/m_e is measured against redshift
  L4  item 143 A: a horizon is crossed inward by every causal signal -- A restricts the direction, not the kind; the
      corridor's horizon is crossed one way, 1 -> 2 (plane.py P1, seated)
Stdlib only.  python3 samelight.py [--selftest]
"""
import sys
from decimal import Decimal, getcontext

getcontext().prec = 50
ALPHA = Decimal(1) / Decimal("137.035999")
ME_MP = Decimal("5.44617021487E-4")          # m_e/m_p, CODATA 2018 (standard, not READ here)
GP = Decimal("5.5856946893")                 # proton g-factor, CODATA 2018 (standard, not READ here)


def dirac(n, j, alpha, Z=1):
    k = Decimal(j) + Decimal("0.5")
    za = Z * alpha
    dj = k - (k * k - za * za).sqrt()
    return 1 / (1 + (za / (n - dj)) ** 2).sqrt()                   # in units of m c^2


def lines(alpha, scale=Decimal(1), me_mp=ME_MP):
    e = lambda n, j: dirac(n, j, alpha)
    lya = e(2, 1.5) - e(1, 0.5)
    ha = e(3, 2.5) - e(2, 1.5)
    fs = e(2, 1.5) - e(2, 0.5)
    hfs = Decimal(8) / 3 * GP * me_mp * alpha**2 * (alpha**2 / 2)  # 21 cm, leading order, in m c^2 (Ry = alpha^2/2)
    return {"lya": lya * scale, "ha": ha * scale, "fs2p": fs * scale, "hfs": hfs * scale}


def ratios(L):
    return {"fs/lya": L["fs2p"] / L["lya"], "ha/lya": L["ha"] / L["lya"], "hfs/lya": L["hfs"] / L["lya"]}


def rel(a, b):
    return {k: float(a[k] / b[k] - 1) for k in b}


def compute(eps=Decimal("1e-4")):
    base = ratios(lines(ALPHA))
    return {"eps": float(eps),
            "alpha": rel(ratios(lines(ALPHA * (1 + eps))), base),
            "same": rel(ratios(lines(ALPHA)), base),
            "redshift": rel(ratios(lines(ALPHA, scale=Decimal(1) / Decimal(1090))), base),
            "electron_mass": rel(ratios(lines(ALPHA, scale=1 + eps)), base),
            "proton_mass": rel(ratios(lines(ALPHA, me_mp=ME_MP / (1 + eps))), base)}


def report(d):
    print("samelight.py -- walls A and B, followed through (item 143)\n")
    print("L1 alpha changed by %.0e: fs(2p)/Ly-a %+.4e (%.4f eps); H-a/Ly-a %+.3e; 21cm/Ly-a %+.4e"
          % (d["eps"], d["alpha"]["fs/lya"], d["alpha"]["fs/lya"] / d["eps"], d["alpha"]["ha/lya"], d["alpha"]["hfs/lya"]))
    print("   alpha held: %s" % d["same"])
    print("L2 uniform scalings (redshift; electron mass with alpha held): %s; %s" % (d["redshift"], d["electron_mass"]))
    print("L3 proton mass changed by %.0e: electronic ratios %s and %s; 21cm/Ly-a %+.4e"
          % (d["eps"], "%+.1e" % d["proton_mass"]["fs/lya"], "%+.1e" % d["proton_mass"]["ha/lya"],
             d["proton_mass"]["hfs/lya"]))
    print("L4 (plane.py P1, seated) the corridor's horizon is crossed one way, 1 -> 2; A restricts direction, not kind")


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    r = d["alpha"]["fs/lya"] / d["eps"]
    chk("L1: a change of alpha by eps moves fs(2p)/Ly-a by 2 eps, |r - 2| < 1e-3 (50-digit arithmetic)", abs(r - 2) < 1e-3)
    chk("L1: H-a/Ly-a moves by about -2.4e-9 at eps = 1e-4 -- line to line, not uniform",
        -2.5e-9 < d["alpha"]["ha/lya"] < -2.3e-9)
    chk("L1 (STRUCTURAL): alpha held, every ratio identical", all(v == 0 for v in d["same"].values()))
    chk("L2 (STRUCTURAL): a redshift, or the electron's mass with alpha held, leaves every ratio unchanged",
        all(abs(v) < 1e-40 for v in list(d["redshift"].values()) + list(d["electron_mass"].values())))
    chk("L3: a proton mass changed by eps leaves the electronic ratios unchanged and moves 21cm/Ly-a by -eps",
        abs(d["proton_mass"]["fs/lya"]) < 1e-40 and abs(d["proton_mass"]["hfs/lya"] / d["eps"] + 1) < 1e-3)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
