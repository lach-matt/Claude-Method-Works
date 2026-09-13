#!/usr/bin/env python3
r"""
postselect.py -- WHAT THE JANUS DOOR COSTS.  The traversable wormhole of
Kawamoto-Maeda-Nakamura-Takayanagi (arXiv:2502.03531) is a POST-SELECTION, and
the paper does not quantify the success probability.  This does.

    THE ANSWER IS NOT THE ONE EXPECTED, AND IT IS BETTER AND WORSE THAN THAT.

    The success probability is O(1) and does NOT fall with the entropy.  There
    is no exp(-S) post-selection penalty.  What is catastrophic is the size of
    the deformation you are ALLOWED: normalizability caps it at delta ~ 0.81/S,
    and the causal opening it buys goes like delta^2.  So the throat you may
    open shrinks like 1/S^2 while the odds of getting it stay near nine in ten.

    THAT CAP IS FOR THE JANUS LINE ONLY, WHICH IS ONE LINE THROUGH A TWO-
    PARAMETER SPACE.  The Janus deformation puts its two columns 90 degrees
    apart, which is the worst case: the phase penalty is the splitting of the
    two singular values, and 90 degrees maximises it.  Bring the columns INTO
    PHASE and the penalty vanishes, leaving only the ordinary squeezing bound,
    and the cap relaxes from 1/S to 1/sqrt(S) -- so the opening goes like 1/S
    rather than 1/S^2, which is 77 orders of magnitude at a solar mass.  That
    branch is derived in reslice.py; this file prices the Janus line.

    python3 postselect.py                 the reading
    python3 postselect.py --selftest      fixtures, including the closed forms

===============================================================================
THE SETUP, AND WHAT IS ASSUMED
===============================================================================

Their model A deforms a thermofield double by an EXACTLY MARGINAL Janus
parameter.  At imaginary parameter the AdS3 solution becomes traversable: the
metric stays real, the dilaton goes imaginary, and null geodesics cross.  There
is NO double-trace coupling -- "there are no interactions between the two CFTs
under the time evolutions" -- which is why this evades the past-horizon
regularity obstruction that made Gao-Jafferis-Wall decline a standing coupling.

The price is that initial and final states differ.  The object is a transition
matrix, not a density matrix.  Running it as a protocol therefore means
preparing |Psi> and post-selecting on |phi>, at probability

        P = |<phi|Psi>|^2 / ( <phi|phi> <Psi|Psi> ).

ASSUMED, and stated because it is the load-bearing step: that the two states
are the paper's free-scalar Janus TFDs at deformation 0 and i*delta (their eq.
4.37), and that no interaction acts between them -- which is model A's own
defining property.  The bulk parameter gamma and the boundary parameter delta
are identified, which the paper expects rather than proves ("this is expected
to correspond to the Janus solution with an imaginary value of the bulk scalar
field").  A reader who rejects that identification keeps the probability
result and loses the opening result.

===============================================================================
WHY IT IS COMPUTABLE AT ALL
===============================================================================

Both states are Gaussian, so the overlap is a determinant.  Per mode, with
lam = exp(-beta E / 2), modes a and b on the two sides, and c = (a,b):

        <0| e^{1/2 c A c} e^{1/2 c! B c!} |0>  =  det(I - A B)^{-1/2}

The undeformed TFD is B = [[0,lam],[lam,0]].  The imaginary Janus at delta has
cos(2th) = i sinh(delta), sin(2th) = cosh(delta), giving

        B(delta) = [[2i lam s, lam c], [lam c, -2i lam s]],  s=sinh d, c=cosh d

and the three determinants below are that formula written out.  Everything is
exact; nothing is fitted.

===============================================================================
WHAT IT REFUSES TO REPORT
===============================================================================

**It never returns a probability for a non-normalizable target.**  Past the
bound the determinant <phi|phi>^{-2} goes negative, the norm goes imaginary,
and the ratio above exceeds 1.  That is not a likely event -- it is the
signature that |phi> IS NOT A STATE, so there is nothing to post-select onto.
The functions return None there and the report says NOT NORMALIZABLE.  A
number would be worse than a refusal, because it would look like an answer.

**It does not claim the door is open or shut.**  It prices one deformation.
Whether an opening of order 1/S^2 is useful is not a question arithmetic
settles, and this file does not settle it.
"""

import math
import sys

# --------------------------------------------------------------- the overlaps

def dets(lam, d):
    """The three Gaussian determinants, each as det(I - A B).

    Returns (d_cross, d_00, d_dd) where the overlap is det^{-1/2} in each case:
      d_cross  <TFD(0) | TFD(i delta)>
      d_00     <TFD(0) | TFD(0)>          = (1 - lam^2)^2, so the norm is 1/(1-lam^2)
      d_dd     <TFD(i delta) | TFD(i delta)>
    """
    s, c = math.sinh(d), math.cosh(d)
    d_cross = (1 - lam * lam * c) ** 2 - 4 * lam ** 4 * s * s
    d_00 = (1 - lam * lam) ** 2
    p = 1 - lam * lam * (c * c + 4 * s * s)
    d_dd = p * p - 4 * lam ** 4 * math.sinh(2 * d) ** 2
    return d_cross, d_00, d_dd


def admissible(lam, d, u=None, v=None):
    """THE EXACT CRITERION, corrected.  Normalizability of exp[1/2 c! M c!]|0>
    with M = [[2v,u],[u,-2v]] is that every SINGULAR VALUE of lam*M is below 1:

        lam^2 ( |u|^2 + 4|v|^2 + 4|Im(conj(v)u)| )  <  1

    An earlier version of this file tested the DETERMINANT instead.  That is
    necessary and NOT sufficient -- the determinant is the product of the two
    singular values, so both can exceed 1 while it stays positive.  A
    Fock-truncation convergence check caught it: the entropy wandered with the
    truncation on a state the determinant had passed.  See reslice.py, which
    derives the singular values in closed form and cross-checks them against a
    numerical SVD."""
    if u is None:
        u, v = math.cosh(d) + 0j, 1j * math.sinh(d)      # the Janus line
    P = abs(u) ** 2 + 4 * abs(v) ** 2
    I = abs((v.conjugate() * u).imag)
    return lam * lam * (P + 4 * I) < 1.0


def p_mode(lam, d):
    """Post-selection probability for one mode, or None if the target is not
    a normalizable state.  The None is the point -- see the docstring."""
    if not admissible(lam, d):
        return None
    d_cross, d_00, d_dd = dets(lam, d)
    if d_dd <= 0 or d_00 <= 0:
        return None
    return math.sqrt(d_00 * d_dd) / abs(d_cross)


def normalizable(lam, d):
    return p_mode(lam, d) is not None


# ------------------------------------------------------------------ a spectrum

def modes(gap, tol=1e-18):
    """A tower beta*E_n = gap*n, truncated where the mode is thermally dead.
    The truncation is why no result here depends on the tower being infinite."""
    out = []
    n = 0
    while True:
        n += 1
        be = gap * n
        lam = math.exp(-0.5 * be)
        if lam * lam < tol:
            return out
        out.append((be, lam))


def entropy(gap):
    """Thermal entropy of the tower, in nats."""
    S = 0.0
    for be, lam in modes(gap):
        occ = lam * lam / (1 - lam * lam)
        S += -math.log(1 - lam * lam) + occ * be
    return S


def delta_max(gap, hi=3.0, iters=120):
    """Largest delta keeping EVERY mode normalizable.  The softest mode binds:
    per mode the bound is delta_max ~ beta E / 4, so the lowest energy sets it."""
    ms = modes(gap)
    lo = 0.0
    for _ in range(iters):
        mid = (lo + hi) / 2
        if all(normalizable(lam, mid) for _, lam in ms):
            lo = mid
        else:
            hi = mid
    return lo


def total_probability(gap, d):
    """P over the whole tower, or None if any mode is past its bound."""
    tot = 0.0
    for _, lam in modes(gap):
        p = p_mode(lam, d)
        if p is None:
            return None
        tot += -math.log(p)
    return math.exp(-tot)


# ------------------------------------------------- what the deformation buys

def _K(m, n=20000):
    """Complete elliptic integral of the first kind, parameter m, by Simpson.
    m is negative here (chi > 1), which is the traversable branch."""
    h = (math.pi / 2) / n
    s = 0.0
    for i in range(n + 1):
        t = i * h
        f = 1.0 / math.sqrt(1 - m * math.sin(t) ** 2)
        s += f * (0.5 if i in (0, n) else 1.0)
    return s * h


def mu0(gamma_sq):
    """The paper's eq. (4.4).  Traversable iff mu0 <= pi/2, needing gamma^2 < 0."""
    chi = math.sqrt(1 - 2 * gamma_sq)
    return math.sqrt(2 / (1 + chi)) * _K((1 - chi) / (1 + chi))


def opening(gamma):
    """pi/2 - mu0 at imaginary gamma: how far the boundaries are causally
    connected.  Goes like gamma^2, coefficient about 0.589."""
    return math.pi / 2 - mu0(-gamma * gamma)


# ------------------------------------------------------------------ the report

def report():
    print("=" * 74)
    print("THE JANUS DOOR, PRICED")
    print("=" * 74)
    print("Kawamoto, Maeda, Nakamura & Takayanagi, arXiv:2502.03531, model A.")
    print("A traversable AdS3 wormhole with NO coupling between the two CFTs,")
    print("bought with a post-selection the paper does not price.")
    print()

    print("1. THE NORMALIZABILITY BOUND.  Past it there is no target state.")
    print("   %-10s %-12s %-14s %s" % ("gap", "entropy S", "delta_max", "S * delta_max"))
    rows = []
    for gap in (2.0, 1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625):
        S, dm = entropy(gap), delta_max(gap)
        rows.append((S, dm))
        print("   %-10.6f %-12.4f %-14.8f %.5f" % (gap, S, dm, S * dm))
    print()
    print("   The product converges: the admissible deformation shrinks like 1/S.")
    print("   Per mode the bound is delta < beta*E/4, so the SOFTEST mode binds,")
    print("   and a bigger system has softer modes.  Nothing here is a choice.")
    print()

    print("2. THE SUCCESS PROBABILITY INSIDE THE WINDOW, at half of delta_max.")
    print("   %-12s %-16s %-12s %s" % ("entropy S", "delta", "-ln P", "P"))
    for gap in (1.0, 0.5, 0.25, 0.125):
        S = entropy(gap)
        d = 0.5 * delta_max(gap)
        P = total_probability(gap, d)
        print("   %-12.3f %-16.8f %-12.5f %.6f" % (S, d, -math.log(P), P))
    print()
    print("   FLAT IN S.  This is the result that was not expected: there is no")
    print("   exp(-S) post-selection penalty.  Scale the deformation the way")
    print("   normalizability already forces and the odds stay near nine in ten.")
    print()

    print("3. WHAT THE DEFORMATION BUYS.  Causal opening pi/2 - mu0, eq. (4.4).")
    print("   %-12s %-14s %s" % ("|gamma|", "opening", "opening / gamma^2"))
    for g in (0.2, 0.1, 0.05, 0.02, 0.01):
        o = opening(g)
        print("   %-12.4f %-14.3e %.5f" % (g, o, o / (g * g)))
    print()
    print("   The opening goes like gamma^2, coefficient ~0.589.")
    print()

    print("4. PUT TOGETHER.")
    k = rows[-1][0] * rows[-1][1]
    print("   admissible delta  ~  %.3f / S" % k)
    print("   opening           ~  0.589 * delta^2  ~  %.3f / S^2" % (0.589 * k * k))
    print("   probability       ~  O(1), independent of S")
    print()
    print("   THE COST IS GEOMETRIC, NOT PROBABILISTIC.  The Janus door is not")
    print("   shut by improbability.  It is shut by how little of it opens.")
    print()
    S_sun = 1.05e77                      # Bekenstein-Hawking, one solar mass, in nats
    print("   For a solar-mass black hole, S ~ %.2e:" % S_sun)
    print("       admissible delta ~ %.2e" % (k / S_sun))
    print("       opening          ~ %.2e" % (0.589 * (k / S_sun) ** 2))
    print()
    print("   Recorded, not adjudicated.  Whether an opening of that size is")
    print("   useful is not a question arithmetic settles.")
    return 0


# -------------------------------------------------------------------- checks

def selftest():
    ok = True

    def chk(name, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", name, got))
        if not good:
            print("        expected %r" % (want,))

    print("postselect selftest")

    # The undeformed limit must be exact, both the norm and the probability.
    chk("delta = 0 gives P = 1 exactly", p_mode(0.5, 0.0), 1.0, 1e-15)
    chk("undeformed TFD norm per mode is 1/(1-lam^2)",
        dets(0.3, 0.0)[1] ** -0.5, 1 / (1 - 0.09), 1e-12)

    # Two closed-form values, computed independently when this was derived.
    chk("closed form: lam=0.30 delta=0.50", p_mode(0.30, 0.50), 0.86481120, 1e-8)
    chk("closed form: lam=0.60 delta=0.20", p_mode(0.60, 0.20), 0.81613316, 1e-8)

    # Monotone in delta, and bounded by 1 where the state exists.
    ps = [p_mode(0.4, d) for d in (0.0, 0.1, 0.2, 0.3)]
    chk("P decreases in delta", all(a >= b for a, b in zip(ps, ps[1:])), True)
    chk("P never exceeds 1 where normalizable", all(p <= 1 + 1e-12 for p in ps), True)

    # The refusal. Past the bound the answer is None, never a number.
    chk("lam=0.60 delta=0.50 is NOT normalizable", p_mode(0.60, 0.50), None)
    chk("and the raw determinant there is negative", dets(0.60, 0.50)[2] < 0, True)

    # The soft modes bind first: delta_max falls as lam -> 1.
    dm = [delta_max_mode(l) for l in (0.3, 0.6, 0.9, 0.99)]
    chk("delta_max falls monotonically as lam -> 1",
        all(a > b for a, b in zip(dm, dm[1:])), True)
    chk("and tracks beta*E/4 for soft modes (lam=0.99)",
        abs(dm[-1] / (-2 * math.log(0.99)) - 0.25) < 0.02, True)

    # Law 1: the admissible deformation shrinks like 1/S.
    prods = [entropy(g) * delta_max(g) for g in (0.5, 0.125, 0.03125)]
    chk("S * delta_max increases and converges", all(a < b for a, b in zip(prods, prods[1:])), True)
    chk("S * delta_max is ~0.80 at the finest gap", abs(prods[-1] - 0.80) < 0.03, True)

    # Law 2: at a fixed fraction of the bound, P does not fall with S.
    Ps = [total_probability(g, 0.5 * delta_max(g)) for g in (1.0, 0.5, 0.25, 0.125)]
    chk("P at half the bound is flat in S", max(Ps) - min(Ps) < 0.005, True)
    chk("and sits near 0.884", abs(Ps[-1] - 0.884) < 0.005, True)

    # The bulk side: the opening is quadratic, and zero without the deformation.
    chk("no deformation, no opening", abs(opening(0.0)) < 1e-9, True)
    chk("opening/gamma^2 -> 0.589", abs(opening(0.01) / 1e-4 - 0.589) < 0.002, True)
    chk("mu0 < pi/2 exactly when gamma is imaginary", mu0(-0.01) < math.pi / 2, True)
    chk("and mu0 > pi/2 for real gamma (not traversable)", mu0(0.01) > math.pi / 2, True)

    print("postselect selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def delta_max_mode(lam, dhi=4.0, n=40000):
    """First delta at which ONE mode stops being normalizable.  Scanned rather
    than bisected: the determinant is a difference of squares and dips before
    it recovers, so a bisection assuming monotonicity finds the wrong root."""
    if not normalizable(lam, 0.0):
        return 0.0
    for k in range(1, n + 1):
        d = dhi * k / n
        if not normalizable(lam, d):
            lo, hi = dhi * (k - 1) / n, d
            for _ in range(60):
                mid = (lo + hi) / 2
                if normalizable(lam, mid):
                    lo = mid
                else:
                    hi = mid
            return lo
    return float("inf")


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
