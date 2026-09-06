"""
THE RIVAL PULL — the algebra of the corridor's ceiling, extracted from its
geometry. Registers 1397, 1401-1405; queue A4a.

THE OBJECT

The corridor's upper bound on a is

    U = dn / ( sqrt(rad_r) - sqrt(rad_g) ),    rad = p + occ/2(2l+1)

The RIVAL's occupancy enters only through rad_r, in the DENOMINATOR. So every
electron sitting in the rival grows the denominator and LOWERS the ceiling. The
attraction is arithmetic, not a fitted term:

    dU/d(occ_r) = - dn / [ 2 * cap(l_r) * sqrt(rad_r) * (sqrt(rad_r) - sqrt(rad_g))^2 ]

Two factors govern its size.

  THE CAP sits in the denominator, so the pull scales as 1/cap:
      s = 2, p = 6, d = 10, f = 14.
  An s rival's single electron moves the ceiling MOST. That is the algebra of
  "the charge of two": an s shell divides by two, so each electron carries the
  largest share.

  THE GAP is squared. The pull grows as the two radicands approach, which is
  proximity in the literal sense.

THE DEGENERATE CASE

rad_r = rad_g gives U = dn/0. That rival imposes no bound and the corridor
construction already skips it (|d| < 1e-12). It is not a singularity of the
physics but a rival that cannot be ordered against the entrant at any a.
"""
import math
cap = lambda l: 2*(2*l+1)
LS = "spdfg"

def rad(p, occ, l):
    return p + occ/cap(l)

def ceiling(dn, p_g, occ_g, l_g, p_r, occ_r, l_r):
    """U, or None where the rival is degenerate and imposes no bound."""
    d = math.sqrt(rad(p_r, occ_r, l_r)) - math.sqrt(rad(p_g, occ_g, l_g))
    if abs(d) < 1e-12:
        return None
    return dn/d

def pull(dn, p_g, occ_g, l_g, p_r, occ_r, l_r):
    """dU/d(occ_r) — how far one electron in the rival draws the ceiling down."""
    rr = rad(p_r, occ_r, l_r)
    d = math.sqrt(rr) - math.sqrt(rad(p_g, occ_g, l_g))
    if abs(d) < 1e-12:
        return None
    return -dn/(2*cap(l_r)*math.sqrt(rr)*d*d)

if __name__ == "__main__":
    print("  THE RIVAL PULL — dU/d(occ_r), no fitted parameter\n")
    print(f"  {'rival':>6}{'cap':>5}{'p_r':>5}{'p_g':>5}{'U at occ 0':>12}"
          f"{'U at occ 1':>12}{'pull':>10}")
    for lab, lr, pr, pg in (("s",0,4,1),("s",0,3,1),("s",0,3,0),
                            ("p",1,3,1),("p",1,2,0),
                            ("d",2,2,1),("d",2,1,0),
                            ("f",3,1,0)):
        u0 = ceiling(1,pg,0,2,pr,0,lr); u1 = ceiling(1,pg,0,2,pr,1,lr)
        pl = pull(1,pg,0,2,pr,1,lr)
        if u0 is None or u1 is None:
            print(f"  {lab:>6}{cap(lr):>5}{pr:>5}{pg:>5}"
                  f"{'degenerate — imposes no bound':>34}")
            continue
        print(f"  {lab:>6}{cap(lr):>5}{pr:>5}{pg:>5}{u0:>12.4f}{u1:>12.4f}{pl:>10.4f}")

    print("\n  THE 1/cap LAW — same p_r, same gap, only the rival's l changes:")
    print(f"  {'rival':>6}{'cap':>5}{'pull at occ 1':>16}{'ratio to s':>12}")
    base = None
    for lab, lr in (("s",0),("p",1),("d",2),("f",3)):
        pl = pull(1, 1, 0, 2, 3, 1, lr)
        if base is None: base = pl
        print(f"  {lab:>6}{cap(lr):>5}{pl:>16.4f}{pl/base:>12.4f}")
    print("      the ratios are NOT exactly 1/cap because sqrt(rad_r) and the")
    print("      squared gap also move with cap. The cap is the leading factor.")

    print("\n  MEASURED, for comparison (median margin by rival occupancy):")
    print("      s: occ 0 -> +1.7379   occ 1 -> +0.2529")
    print("      p: occ 0 -> +0.8369   occ 1 -> -0.1356")
    print("      d: occ 0 -> +0.5071   occ 1 -> +0.1520   occ 2 -> -0.0984")
    print("      monotone in occupancy within every l, s falling hardest.")