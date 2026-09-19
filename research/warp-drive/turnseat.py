#!/usr/bin/env python3
"""
transit.py -- travel > turn > seat, as three gated parts with a failure mode.

M's structure, taken literally and made runnable:

  PART 1  TRAVEL   set the optimal conditions for transition.  Governed by
                   first principles including OBSERVABILITY.
  PART 2  TURN     the turning mechanism -- the change that allows SEATING at
                   the destination.  A CONDITION REQUIREMENT, met iff part 1 is
                   fully defined and stated for input.
  PART 3  SEAT     the seating and closure of the travel.  Also governed by
                   first principles including observability.

  BOTH SETS OF COORDINATES MUST BE KNOWN AT THE ONSET OF PART 1, so that part 2
  can initialize -- and part 2 FAILS if the input data does not provide enough
  for part 3.

And M's prediction, stated before the measurement:

    THE MATHEMATICAL EXPRESSION IS VISIBLE AT BOTH ENDS WITH THE SAME BINARY
    CHAIN.

    IT IS.  Measured, exactly, and proved below.

-- WHAT EACH PART IS, IN THE MATHEMATICS WE ALREADY HAVE ----------------------
The structure is not a metaphor here.  achronal.py reduced achronality to a
Sturm-Liouville problem for the Jacobi field of a null congruence,

        u'' = -q(lambda) u,     q = 4 pi T_kk,

and that problem has exactly M's shape:

  PART 1  u(0) = 0, u'(0) = 1 at the departure event A, plus the DECLARED
          arrival event B.  Both endpoints, at onset.  This is a TWO-POINT
          boundary problem wearing initial-value clothes, which is precisely
          why B cannot be discovered later: without it there is nothing for
          part 2 to test against.
  PART 2  does u TURN and come back to zero?  A conjugate point is that turn.
          It initializes only with a declared interval and it FAILS -- returns
          no length at all -- when the conditions part 1 set do not focus
          enough to reach one.  "Fail if the input data doesn't provide enough
          for part 3" is not an added guard; it is what the equation does.
  PART 3  the turn lands ON the declared B.  u(L_declared) = 0.  Closure.

OBSERVABILITY is met in the way part 1 and part 3 demand: a conjugate LENGTH is
an affine invariant of the congruence, not a coordinate separation.  Two
observers disagree about where B is and agree about L.

-- M'S PREDICTION, PROVED THEN MEASURED ---------------------------------------
    THEOREM (reversal invariance of the turn).  Let u'' + q u = 0 with
    u(0) = u(L) = 0.  Define the path read from the far end, q~(x) = q(L - x).
    Then v(x) := u(L - x) satisfies v'' + q~ v = 0 with v(0) = u(L) = 0 and
    v(L) = u(0) = 0.  The SAME pair is conjugate.  QED

The operator is self-adjoint -- no first-derivative term survives the theta^2
absorption -- so departure and arrival are interchangeable and the turn is one
object seen from two ends.  Measured by bisecting the conjugate length on the
true rays of the bubble, forwards and on the reversed path:

        y0      L (A->B)          L (B->A)         |diff|
        0.8     9.9975835361      9.9975835361     1.1e-14
        0.9     5.3760386939      5.3760386939     5.3e-14
        1.0     5.2600374222      5.2600374222     5.2e-14
        1.1     5.5028056987      5.5028056987     5.7e-14
        1.2     6.4050733902      6.4050733902     9.1e-14

and on a deliberately ASYMMETRIC control potential, |diff| = 0.00e+00 exactly.
The binary chain -- turn / seats / achronal / ANEC sign -- is identical read
from either end on every ray.  THE PREDICTION HOLDS.

-- AND THE STRUCTURE THEN EXCLUDES TWO THINGS, WHICH IS ITS VALUE -------------
Making the parts explicit makes two impossibilities explicit with them, and
neither was visible before the structure was imposed.

  EXCLUSION 1 -- THE TURN LIVES IN THE ENERGY-CONDITION-SATISFYING SECTOR.
  u'' = -4 pi T_kk u turns u back toward zero only where T_kk > 0.  Negative
  T_kk is convex, and convex never returns.  So part 2 succeeds only on rays
  that SATISFY ANEC and fails on every ray that violates it -- which is
  achronal.py's DEFOCUS-PROTECTS read in the other direction.  The exotic
  sector cannot seat.  Whatever a working drive is, part 2 puts it in the
  ORDINARY-MATTER half of the problem.

  EXCLUSION 2 -- AND THAT HALF ARRIVES LATE.  Measured, coordinate time from A
  to the conjugate point against the flat light time between the same endpoints:

        y0    turn        t - |dx|        verdict
        0.6   none        +4.360e-01      late
        0.8   9.990       +8.931e-01      LATE
        0.9   5.370       +7.682e-02      LATE
        1.0   5.250       +1.320e-02      LATE
        1.1   5.490       +2.592e-03      LATE
        1.2   6.390       +7.066e-04      LATE
        1.5   none        -1.243e-04      early -- BUT IT DOES NOT TURN
        2.0   none        -5.044e-08      early -- BUT IT DOES NOT TURN

  Every ray that turns arrives LATE: a positive Shapiro delay, which is what
  positive energy always gives.  The only rays that arrive EARLY are the far
  grazing ones that never turn -- and their lead is real, converged to five
  figures across an 8x refinement, and utterly tiny.

    TURN => LATE.  EARLY => NO TURN.  On this metric there is NO configuration
    where part 2 succeeds and the transit is advantageous.

-- WHAT THIS IS AND IS NOT ----------------------------------------------------
IS:  the three-part structure is coherent, computable, correctly gated, and its
     both-ends prediction is exactly true.  It is a real frame and it produced
     two exclusions the previous frame could not see.

IS NOT: a transport mechanism.  A conjugate point is a LIGHT focus -- a
     congruence of null rays leaving A and reconverging at B.  It says B sits on
     a degenerate boundary of A's causal future.  It does not carry a payload,
     and nothing here claims it does.

AND NOT: a result about all metrics.  Every measurement is on the Alcubierre
     bubble at v_s = 0.5 c.  The exclusions above are properties of THIS object.
     Exclusion 1 is general -- it is the sign of the Jacobi equation.  Exclusion
     2 is MEASURED HERE, and a metric with a different T_kk distribution is
     NOT-RUN, never absent.

stdlib only.  achronal.py supplies the geodesics and T_kk; typefour.py the
metric and the doubly-validated stress tensor.
"""
import math, sys

# part states -- a part is not a boolean, and the reasons are the point
READY, BLOCKED, MET, FAILED, SEATED, MISSED = (
    "READY", "BLOCKED", "MET", "FAILED", "SEATED", "MISSED")


# ---------------------------------------------------------------- part 1

class Conditions:
    """PART 1.  The declared conditions of a transition.  Both endpoints, at
    onset.  An instance with no declared arrival is BLOCKED and part 2 refuses
    to initialize from it -- that refusal is the structure, not a guard."""

    def __init__(self, y0, vs=0.5, arrival_length=None, x0=None, lam=12.0, n=800):
        import achronal
        self.y0, self.vs, self.lam, self.n = y0, vs, lam, n
        self.x0 = achronal.X0 if x0 is None else x0
        self.arrival_length = arrival_length     # the DECLARED L. None => BLOCKED.
        self._q = None

    def state(self):
        return READY if self.arrival_length is not None else BLOCKED

    def potential(self):
        """q(lambda) = 4 pi T_kk along the true null geodesic, as a sampler.
        An affine invariant of the congruence -- this is the observability
        first principle part 1 is held to."""
        if self._q is None:
            import achronal as A
            p0 = (self.x0, self.y0, 0.0)
            k0 = A.null_tangent(p0, (1.0, 0.0, 0.0), self.vs)
            pts, tang, h = A.geodesic(p0, k0, self.vs, self.lam, self.n)
            tk = A.tkk_along(pts, tang, self.vs)
            self._q = ([4.0 * math.pi * t for t in tk], h, pts, tang, tk)
        return self._q

    def sampler(self, reverse_at=None):
        q, h, _p, _t, _tk = self.potential()

        def f(lam):
            x = (reverse_at - lam) if reverse_at is not None else lam
            s = x / h
            i = int(s)
            if i < 0:
                return q[0]
            if i >= len(q) - 1:
                return q[-1]
            w = s - i
            return q[i] * (1.0 - w) + q[i + 1] * w
        return f


# ---------------------------------------------------------------- part 2

def _endvalue(qf, L, n=2000):
    """u'' = -q u on [0, L], u(0)=0, u'(0)=1.  Return u(L)."""
    h = L / n
    u, up = 0.0, 1.0
    for i in range(n):
        a = -qf(i * h) * u
        un = u + h * up + 0.5 * h * h * a
        up += 0.5 * h * (a + (-qf((i + 1) * h) * un))
        u = un
    return u


def turn_length(qf, lo=0.5, hi=11.9, iters=60, n=2000):
    """PART 2.  The conjugate length: the L at which u returns to zero.
    Returns None when the conditions never focus enough -- THE FAILURE MODE."""
    if _endvalue(qf, hi, n) > 0.0:
        return None                       # u never turns back: no turn exists
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if _endvalue(qf, mid, n) > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def part2(cond, iters=60, n=2000):
    """Initializes ONLY from a READY part 1.  Returns (state, length)."""
    if cond.state() is BLOCKED:
        return BLOCKED, None
    L = turn_length(cond.sampler(), iters=iters, n=n)
    return (MET, L) if L is not None else (FAILED, None)


# ---------------------------------------------------------------- part 3

def part3(cond, L_turn, tol=1e-6):
    """PART 3.  Seating: the turn lands on the DECLARED arrival."""
    if L_turn is None:
        return MISSED
    return SEATED if abs(L_turn - cond.arrival_length) <= tol else MISSED


def transit(y0, vs=0.5, arrival_length=None, tol=1e-6):
    """The whole chain, gated.  Nothing downstream runs on a blocked part."""
    c = Conditions(y0, vs, arrival_length)
    s2, L = part2(c)
    s3 = part3(c, L) if (s2 is MET and c.arrival_length is not None) else BLOCKED
    return {"y0": y0, "part1": c.state(), "part2": s2, "turn_length": L,
            "part3": s3, "conditions": c}


# --------------------------------------------- M's prediction, both ends

def binary_chain(cond, L=None):
    """The chain M predicted is visible at both ends.  Four binaries, each one
    a language answering yes or no about this transition -- never a magnitude."""
    q, h, pts, _t, tk = cond.potential()
    L = turn_length(cond.sampler()) if L is None else L
    anec = sum(tk) * h
    return (
        L is not None,                                   # order:   does it turn?
        L is not None and cond.arrival_length is not None
        and abs(L - cond.arrival_length) <= 1e-6,        # closure: does it seat?
        L is None,                                       # order:   achronal?
        anec < 0.0,                                      # analysis, thresholded
    )


def chain_from_far_end(cond, L):
    """The same chain, computed reading the path from the arrival end."""
    if L is None:
        return None
    Lr = turn_length(cond.sampler(reverse_at=L))
    q, h, _p, _t, tk = cond.potential()
    anec = sum(tk) * h
    return (
        Lr is not None,
        Lr is not None and cond.arrival_length is not None
        and abs(Lr - cond.arrival_length) <= 1e-6,
        Lr is None,
        anec < 0.0,
    ), Lr


def shapiro(cond, L):
    """Coordinate time A -> B less the flat light time between the same spatial
    endpoints.  Positive is late."""
    _q, h, pts, _t, _tk = cond.potential()
    i = min(int(round((L if L is not None else (len(pts) - 1) * h) / h)), len(pts) - 1)
    a, b = pts[0], pts[i]
    dx = math.sqrt(sum((b[j] - a[j]) ** 2 for j in (1, 2, 3)))
    return (b[0] - a[0]) - dx


# ---------------------------------------------------------------- selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-60s %16s %16s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got - want) <= tol
        ok &= good
        print("  %-60s %16.6g %16.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("The theorem, on an ASYMMETRIC control -- no bubble, no geometry")
    qc = lambda x: 3.0*math.exp(-((x-0.7)/0.4)**2) + 1.0*math.exp(-((x-2.2)/0.6)**2)
    Lc = turn_length(qc, 0.5, 6.0)
    Lr = turn_length(lambda x: qc(Lc - x), 0.5, 6.0)
    near("a turn exists on the control", Lc, 2.9161741514, 1e-9)
    chk("and reversal recovers it EXACTLY", Lc == Lr, True)
    print("       forward %.10f   reversed %.10f   diff %.2e" % (Lc, Lr, abs(Lc - Lr)))
    # the pinned digits are the n=2000 quadrature's, so the discretisation is
    # checked rather than carried: refining must not move the answer.
    Lc8 = turn_length(qc, 0.5, 6.0, n=8000)
    near("and refining the quadrature 4x does not move it", Lc8, Lc, 1e-6)
    # bit-equality at n=2000 is the bisection landing on identical floats; the
    # theorem guarantees equality of the true values, so at another resolution
    # the right assertion is machine precision, not bit-identity.
    near("reversal holds at the refined resolution, to machine precision",
         turn_length(lambda x: qc(Lc8 - x), 0.5, 6.0, n=8000), Lc8, 1e-13)

    print("\nPart 1 gates part 2 -- an undeclared arrival BLOCKS, it does not guess")
    blocked = Conditions(1.0, arrival_length=None)
    chk("part 1 with no declared arrival", blocked.state(), BLOCKED)
    chk("part 2 refuses to initialize from it", part2(blocked)[0], BLOCKED)
    chk("and returns no length rather than a default", part2(blocked)[1], None)

    print("\nPart 2 FAILS when the conditions cannot reach part 3")
    nofocus = Conditions(0.3, arrival_length=5.0)      # ANEC-violating, defocusing
    s2, L = part2(nofocus)
    chk("a defocusing ray does not turn", s2, FAILED)
    chk("part 3 then MISSES rather than seating", part3(nofocus, L), MISSED)

    print("\nPart 2 is MET, and part 3 seats only on the DECLARED arrival")
    probe = part2(Conditions(1.0, arrival_length=0.0))[1]
    good = Conditions(1.0, arrival_length=probe)
    s2g, Lg = part2(good)
    chk("the turn exists", s2g, MET)
    near("and it is where the bisection puts it", Lg, probe, 1e-9)
    chk("declared correctly -> SEATED", part3(good, Lg), SEATED)
    wrong = Conditions(1.0, arrival_length=probe + 0.5)
    chk("declared wrongly -> MISSED, not nudged", part3(wrong, Lg), MISSED)

    print("\nM's PREDICTION: the same expression, and the same chain, at both ends")
    print("     %5s %18s %18s %10s %s" % ("y0", "L (A->B)", "L (B->A)", "|diff|", "chain"))
    same = 0
    for y0 in (0.8, 0.9, 1.0, 1.1, 1.2):
        c = Conditions(y0, arrival_length=None)
        L = turn_length(c.sampler())
        c.arrival_length = L
        ch_a = binary_chain(c, L)
        ch_b, Lb = chain_from_far_end(c, L)
        agree = (ch_a == ch_b) and abs(L - Lb) < 1e-10
        same += agree
        print("     %5.1f %18.10f %18.10f %10.1e %s"
              % (y0, L, Lb, abs(L - Lb), "SAME" if agree else "DIFFER"))
    chk("rays where both ends agree exactly", same, 5)

    print("\nEXCLUSION 1 -- the turn only happens where ANEC is SATISFIED")
    import achronal
    rows = achronal.survey()
    for r in rows:
        c = Conditions(r["y0"], arrival_length=None)
        turned = turn_length(c.sampler()) is not None
        r["turns"] = turned
    chk("no ANEC-violating ray turns",
        [r["y0"] for r in rows if r["anec_violated"] and r["turns"]], [])
    chk("every turning ray satisfies ANEC",
        all(not r["anec_violated"] for r in rows if r["turns"]), True)
    chk("and turning is exactly the negation of achronal",
        all(r["turns"] != r["achronal"] for r in rows), True)

    print("\nEXCLUSION 2 -- and every ray that turns arrives LATE")
    print("     %5s %10s %14s %s" % ("y0", "turn", "t - |dx|", "verdict"))
    late = []
    for y0 in (0.8, 1.0, 1.2, 1.5):
        c = Conditions(y0, arrival_length=None)
        L = turn_length(c.sampler())
        d = shapiro(c, L)
        late.append((L is not None, d))
        print("     %5.1f %10s %+14.3e %s"
              % (y0, ("%.3f" % L) if L else "none", d,
                 "LATE" if d > 0 else "early"))
    chk("every turning ray is late", all(d > 0 for t, d in late if t), True)
    chk("and every early ray failed to turn", all(not t for t, d in late if d < 0), True)
    print("       TURN => LATE.  EARLY => NO TURN.  No configuration has both.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE CHAIN, RUN")
    print("  %5s %9s %9s %18s %9s %13s"
          % ("y0", "part1", "part2", "turn length", "part3", "t - |dx|"))
    for y0 in (0.3, 0.6, 0.8, 0.9, 1.0, 1.1, 1.2, 1.5):
        c = Conditions(y0, arrival_length=None)
        L = turn_length(c.sampler())
        c.arrival_length = L
        s2 = MET if L is not None else FAILED
        s3 = part3(c, L)
        print("  %5.1f %9s %9s %18s %9s %+13.3e"
              % (y0, c.state(), s2, ("%.10f" % L) if L else "-", s3, shapiro(c, L)))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  The structure is coherent and correctly gated, and its both-ends")
    print("  prediction is EXACTLY true -- conjugacy is reversal-invariant")
    print("  because the Jacobi operator is self-adjoint, and the binary chain")
    print("  is identical read from either end on every ray.")
    print("\n  It then excludes two things.  Part 2 succeeds only where ANEC is")
    print("  SATISFIED, so the turn is in the ordinary-matter half; and every")
    print("  ray that turns arrives LATE.  On this metric no configuration has")
    print("  both a turn and an advantage.  A conjugate point is a light focus,")
    print("  not a payload, and this file does not claim otherwise.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
