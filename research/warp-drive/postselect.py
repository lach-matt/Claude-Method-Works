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
CAN A COEFFICIENT BUY A DISCOUNT?  FOUR ANSWERS, AND THE ONE YES IS NOT FREE
===============================================================================

The cap is delta_max ~ 0.81/S and the opening goes like delta^2, so anything
that multiplies the admissible delta is worth two of itself.  Four ways to try
it were priced.  THREE ARE NO, AND THE NO IS ALGEBRAIC RATHER THAN NUMERICAL.

(1) A UNIFORM COEFFICIENT BUYS NOTHING.  The admissibility bracket

        |u|^2 + 4|v|^2 + 4|Im(conj(v)u)|

is HOMOGENEOUS OF DEGREE 2: scaling both columns by c multiplies it by exactly
c^2, which is the same as scaling lam by c.  A uniform coefficient IS the
deformation strength; it cannot discount it.  Verified to twelve digits.

(2) THE COLUMNS ARE PRICED 1:4, AND THE CONTENT CANNOT MOVE.  At fixed total
column weight and in phase, an all-`u` deformation costs 1 and an all-`v` one
costs 4, so moving content from the same-side column to the cross column would
buy a factor 4 in budget and 2 in headroom.  It is not available: the Janus
family lies on the HYPERBOLA

        |u|^2 - |v|^2 = 1        (cosh^2 d - sinh^2 d)

exactly, at every d.  |v| = sinh d IS the deformation.  Reducing it is not
reweighting the deformation, it is not deforming.

(3) THE BILL IS NOT THE COLUMNS ANYWAY -- IT IS THE PHASE BETWEEN THEM.  Of
the three terms, only two depend on d, and at the delta that matters the split
is not close:

        d = 0.001     4|v|^2 = 4.0e-06     4|Im| = 4.0e-03     phase = 99.9 %
        d = 0.01      4|v|^2 = 4.0e-04     4|Im| = 4.0e-02     phase = 99.0 %
        d = 0.1       4|v|^2 = 4.0e-02     4|Im| = 4.0e-01     phase = 90.9 %

A coefficient that reweights the columns is attacking a tenth of a percent of
the bill.  THE THING TO ATTACK IS THE PHASE, and the way to attack it is not a
coefficient -- it is to bring the columns into phase, which is the branch
reslice.py derives and which relaxes 1/S to 1/sqrt(S).

(4) A MODE-DEPENDENT DELTA IS A REAL GAIN, AND THE NAIVE VERSION OF IT IS A
TRUNCATION ARTEFACT.  The uniform cap is set by the SOFTEST mode; every other
mode could take more.  Averaging the per-mode caps flat gives a large factor
that MOVES WITH THE TRUNCATION and is therefore not a number:

        gap = 0.15    tol 1e-8   122 modes   naive x109.8   weighted x5.109127
                      tol 1e-18  276 modes   naive x259.2   weighted x5.109128
                      tol 1e-30  460 modes   naive x438.0   weighted x5.109128
                      tol 1e-60  921 modes   naive x886.2   weighted x5.109128

The flat average is dominated by thermally dead modes whose cap grows like
-ln(lam) and whose occupation is zero; it tracks the MODE COUNT almost exactly,
which is the signature of an artefact and not of a discount.  WEIGHTED BY
OCCUPATION it is stable to SEVEN digits over four decades of truncation.  That
is the real one, and it is 5.109128 at this gap.

The bisection ceiling is derived from lam rather than passed in, for the same
reason: a fixed ceiling clamps exactly those dead modes, so the flat average
would depend on the ceiling too and the truncation dependence would be partly
hidden by a second artefact.

ITS GROWTH IS NOT A POWER LAW, AND AN EARLIER PASS HERE RECORDED ONE.  Fitted
over a decade it looks like S^0.75; the local slope drifts monotonically --
0.57, 0.61, 0.64, 0.68, 0.71, 0.74, 0.76, 0.79, 0.81, 0.83 -- and a drifting
slope is not an exponent.  Against S/ln(S) the ratio is flat to about 13 %
over two decades of S (0.79 down to 0.69), which is the shape the tower
predicts: per mode the small-d cap is (lam^-2 - 1)/4 and the occupation is
1/(lam^-2 - 1), so their product is 1/4 for EVERY mode below the thermal
scale, the numerator counts modes and the denominator is the partition sum.

So the effective deformation goes from ~0.81/S uniform to ~1/ln(S) weighted --
which would be an enormous change, and this file does not claim it as one:

**A BUDGET GAIN IS NOT AN OPENING GAIN, AND THIS FILE WILL NOT CONVERT ONE
INTO THE OTHER.**  The opening is a function of the BULK parameter gamma, and
the identification gamma <-> delta is the paper's, for a SINGLE marginal
Janus parameter common to every mode.  A per-mode delta_n is a normalizable
Gaussian state and is NOT that deformation; no dictionary in this tree sends
it to a single gamma.  What is measured here is how much deformation the
normalizability bound allows.  What it opens is not measured, and saying it
is 1/ln(S) instead of 1/S^2 would be exactly the unearned step.

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

**It does not report a flat average over modes as a discount.**  That number
moves with the truncation and the census prints all four truncations beside
each other so it cannot be quoted alone.

**It does not fit a power law to a drifting slope.**  The mode-dependent gain
had an exponent recorded for it here and the exponent was an artefact of the
fitting range; the census now prints the local slope at every step so the
drift is visible in the output rather than hidden in a fit.
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


def dets_general(lam, d1, d2):
    """det(I - A B) for <TFD(i d1) | TFD(i d2)>, the two-parameter overlap.

    `dets` above is the d1 = 0 slice of this.  With A = B(d1)* and B = B(d2),

        A B = lam^2 [[ K, -2i Sig ], [ 2i Sig, K ]]
              K   = cosh d1 cosh d2 + 4 sinh d1 sinh d2
              Sig = sinh(d1 + d2)

    so det(I - A B) = (1 - lam^2 K)^2 - 4 lam^4 Sig^2.  Needed for a path that
    post-selects at intermediate deformations: after the first step the state is
    no longer the undeformed TFD, and using `dets` there would price every step
    against the wrong bra.  The selftest asserts it reproduces all three of
    `dets`, which is what ties it to the already-checked arithmetic."""
    s1, c1 = math.sinh(d1), math.cosh(d1)
    s2, c2 = math.sinh(d2), math.cosh(d2)
    K = c1 * c2 + 4 * s1 * s2
    return (1 - lam * lam * K) ** 2 - 4 * lam ** 4 * math.sinh(d1 + d2) ** 2


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


# ------------------------------------------- can a coefficient buy a discount

def bracket(u, v):
    """The admissibility bracket, homogeneous of degree 2 in (u, v)."""
    return abs(u) ** 2 + 4 * abs(v) ** 2 + 4 * abs((v.conjugate() * u).imag)


def janus_columns(d):
    """The Janus line: the two columns at deformation d.  On the hyperbola."""
    return math.cosh(d) + 0j, 1j * math.sinh(d)


def budget_split(d):
    """(|u|^2, 4|v|^2, 4|Im|, phase share of the d-DEPENDENT bill).

    The first term is the undeformed TFD and does not depend on d, so the
    share is taken over the other two -- quoting it over all three would
    flatter the phase term at small d and understate it at large.
    """
    u, v = janus_columns(d)
    U, V, I = abs(u) ** 2, 4 * abs(v) ** 2, 4 * abs((v.conjugate() * u).imag)
    return U, V, I, I / (V + I)


def mode_delta_max(lam, iters=100):
    """Largest d this single mode admits.  The uniform cap is the min of these.

    The bisection ceiling is DERIVED, not passed in.  At large d the bracket
    goes like 2.25 e^{2d}, so the cap sits near -ln(lam) - ln(1.5); starting
    two above that brackets it for every lam.  A fixed ceiling would silently
    clamp the thermally dead modes and make the flat average below depend on
    the ceiling as well as on the truncation -- one artefact hiding another.
    """
    hi = -math.log(lam) + 2.0
    lo = 0.0
    for _ in range(iters):
        m = (lo + hi) / 2
        if admissible(lam, m):
            lo = m
        else:
            hi = m
    return lo


def discount(gap, tol=1e-18):
    """(naive, weighted, n_modes) -- the flat and occupation-weighted ratios of
    the mode-dependent cap to the uniform one.  The naive one is reported so it
    can be seen moving with `tol`; it is not a discount."""
    ms = modes(gap, tol=tol)
    ds = [mode_delta_max(l) for _, l in ms]
    du = min(ds)
    w = [l * l / (1 - l * l) for _, l in ms]
    naive = (sum(ds) / len(ds)) / du
    wtd = (sum(wi * di for wi, di in zip(w, ds)) / sum(w)) / du
    return naive, wtd, len(ms)


def gain_scaling(gaps=(0.3, 0.2, 0.15, 0.1, 0.07, 0.05, 0.03, 0.02, 0.01, 0.006, 0.004)):
    """[(S, gain, gain/(S/lnS), local log-log slope)] -- the evidence that the
    growth is NOT a power law.  A drifting slope is the finding."""
    out, prev = [], None
    for g in gaps:
        S = entropy(g)
        _, wtd, _ = discount(g)
        slope = ((math.log(wtd) - math.log(prev[1])) / (math.log(S) - math.log(prev[0]))
                 if prev else None)
        out.append((S, wtd, wtd / (S / math.log(S)), slope))
        prev = (S, wtd)
    return out


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
    print()

    print("5. CAN A COEFFICIENT BUY A DISCOUNT?  THREE NO AND ONE QUALIFIED YES.")
    print()
    print("   (1) A UNIFORM COEFFICIENT: nothing.  The bracket is homogeneous")
    print("       of degree 2, so scaling the columns IS scaling lam.")
    u0, v0 = janus_columns(0.3)
    for c in (0.5, 2.0, 3.7):
        print("       c = %-5.2f  bracket ratio %.12f  (c^2 = %.4f)"
              % (c, bracket(c * u0, c * v0) / bracket(u0, v0), c * c))
    print()
    print("   (2) THE COLUMNS ARE PRICED 1:4 AND THE CONTENT CANNOT MOVE.")
    for f in (0.0, 0.5, 1.0):
        uu, vv = complex(math.sqrt(1 - f)), complex(math.sqrt(f))
        print("       |v|^2 share %.2f  bracket %.4f  lam headroom %.4f"
              % (f, bracket(uu, vv), 1 / math.sqrt(bracket(uu, vv))))
    print("       but the Janus family is the HYPERBOLA |u|^2 - |v|^2 = 1:")
    for dd in (0.0, 0.8, 1.5):
        uu, vv = janus_columns(dd)
        print("         d = %.1f   |u|^2 - |v|^2 = %.12f" % (dd, abs(uu) ** 2 - abs(vv) ** 2))
    print("       |v| = sinh d IS the deformation. Reducing it is not deforming.")
    print()
    print("   (3) THE BILL IS THE PHASE, NOT THE COLUMNS.")
    for dd in (0.001, 0.01, 0.1):
        U, V, I, sh = budget_split(dd)
        print("       d = %-6g 4|v|^2 = %.2e  4|Im| = %.2e   phase share %.1f%%"
              % (dd, V, I, 100 * sh))
    print("       A coefficient on the columns attacks a tenth of a percent.")
    print("       The phase is attacked by bringing the columns INTO PHASE,")
    print("       which is not a coefficient. See reslice.py.")
    print()
    print("   (4) A MODE-DEPENDENT DELTA IS REAL, AND ITS NAIVE FORM IS AN")
    print("       ARTEFACT.  gap = 0.15, four truncations:")
    for tol in (1e-8, 1e-18, 1e-30, 1e-60):
        nv, wt, nm = discount(0.15, tol=tol)
        print("       tol %-8.0e %3d modes   naive x%-7.1f  weighted x%.6f"
              % (tol, nm, nv, wt))
    print("       The naive one tracks the MODE COUNT. The weighted one is")
    print("       stable to seven digits. Only the second is a number.")
    print()
    print("       AND ITS GROWTH IS NOT A POWER LAW:")
    print("       %-10s %-10s %-12s %s" % ("S", "gain", "gain/(S/lnS)", "local slope"))
    for S, gn, rat, sl in gain_scaling():
        print("       %-10.2f %-10.3f %-12.4f %s"
              % (S, gn, rat, "-" if sl is None else "%.4f" % sl))
    print("       The slope DRIFTS from 0.57 to 0.83 and is still climbing, so")
    print("       there is no exponent. Against S/ln(S) the ratio is flat to")
    print("       about 13% over two decades. An earlier pass here recorded a")
    print("       power law; it was the fitting range, not the physics.")
    print()
    print("   A BUDGET GAIN IS NOT AN OPENING GAIN. The opening is a function of")
    print("   the BULK gamma, identified with a SINGLE marginal delta common to")
    print("   every mode. A per-mode delta_n is a normalizable Gaussian state and")
    print("   is not that deformation. This file prices the budget and stops.")
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

    # The two-parameter overlap must reproduce all three of `dets`.
    for lam, dd in ((0.6, 0.3), (0.3, 0.9), (0.45, 0.05)):
        dc, d00, ddd = dets(lam, dd)
        chk("dets_general reproduces dets at lam=%.2f d=%.2f" % (lam, dd),
            max(abs(dets_general(lam, 0.0, dd) - dc),
                abs(dets_general(lam, 0.0, 0.0) - d00),
                abs(dets_general(lam, dd, dd) - ddd)) < 1e-14, True)
    chk("and it is symmetric in its two arguments",
        abs(dets_general(0.6, 0.2, 0.5) - dets_general(0.6, 0.5, 0.2)) < 1e-15, True)

    # The coefficient question: three no's and one qualified yes.
    u0, v0 = janus_columns(0.3)
    chk("the bracket is homogeneous of degree 2 (a uniform coefficient buys 0)",
        max(abs(bracket(c * u0, c * v0) / bracket(u0, v0) - c * c)
            for c in (0.5, 2.0, 3.7)) < 1e-12, True)
    chk("the columns are priced 1:4",
        (bracket(complex(1), 0j), bracket(0j, complex(1))), (1.0, 4.0))
    chk("the Janus family sits on the hyperbola |u|^2 - |v|^2 = 1",
        max(abs(abs(janus_columns(d)[0]) ** 2 - abs(janus_columns(d)[1]) ** 2 - 1)
            for d in (0.0, 0.3, 0.8, 1.5)) < 1e-12, True)
    chk("at d = 0.001 the phase carries 99.9% of the d-dependent bill",
        budget_split(0.001)[3], 0.999, 1e-3)
    chk("the phase share stays above 90% out to d = 0.1",
        budget_split(0.1)[3] > 0.90, True)

    n8, w8, _ = discount(0.15, tol=1e-8)
    n60, w60, _ = discount(0.15, tol=1e-60)
    chk("the naive discount MOVES with the truncation", n60 / n8 > 5, True)
    chk("the occupation-weighted one does not, to six digits",
        abs(w60 - w8) < 1e-6, True)
    chk("and it is the value the report prints", w8, 5.109128, 1e-5)
    chk("the naive figure tracks the MODE COUNT, which is what makes it an "
        "artefact", abs((n60 / n8) / (921 / 122) - 1) < 0.10, True)

    sc = gain_scaling()
    slopes = [r[3] for r in sc if r[3] is not None]
    chk("the log-log slope DRIFTS, so there is no exponent",
        all(slopes[i] < slopes[i + 1] for i in range(len(slopes) - 1)), True)
    chk("it drifts across the range an earlier pass fitted a power law to",
        (round(min(slopes), 2), round(max(slopes), 2)), (0.57, 0.83))
    rat = [r[2] for r in sc]
    chk("against S/ln(S) the ratio is flat to 13% over two decades",
        max(rat) / min(rat) < 1.16, True)

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
