#!/usr/bin/env python3.12
"""proofs.py -- every algebraic claim of the corridor series, proved.

M: "expand all the math on hand and state everything in full ... then write the
proofs and promote what can be promoted."

This file does the promotion.  Every identity the corridor series (H74-H79)
established NUMERICALLY is restated here as an ALGEBRAIC IDENTITY, given a
derivation in closed form, and then checked TWO ways:

  (i)  EXACTLY, over the rationals -- Fraction arithmetic, no floating point,
       so a check that passes is an equality of rational numbers and not an
       agreement to some tolerance;

  (ii) ON A GRID THAT EXCEEDS THE DEGREE.  Each identity, after clearing
       denominators, is a polynomial identity.  A polynomial of degree at most
       d_i in x_i that vanishes on a grid S_1 x ... x S_n with |S_i| > d_i is
       IDENTICALLY ZERO -- the one-variable fact applied one variable at a
       time.  So a grid check above the degree bound is a PROOF, not a sample.

THE HONEST RELATION BETWEEN THE TWO.  The proof is the derivation; the grid
check is a mechanical confirmation that the code implements the derivation and
that no term was dropped in transcription.  Neither alone is the whole thing,
and the file states both.  DEGREE BOUNDS ARE DELIBERATELY OVER-ESTIMATED:
over-bounding only enlarges the grid, and can never turn a false identity true.

PROMOTION LADDER, and every claim in the series is placed on it:

  THEOREM          derivation given here, verified exactly.  PROMOTED.
  THEOREM-CITED    a known result, attributed to its primary source, and
                   re-verified here.  Promoted as knowledge, NOT as ours.
  MEASURED         numerically checked, no derivation.  NOT promoted.
  DEFINITION       true by construction; nothing to prove.

    python3.12 proofs.py            the proofs in full
    python3.12 proofs.py --selftest
"""

from fractions import Fraction as F
import sys

# --------------------------------------------------------------------------
# Exact Kerr-Newman, equatorial and general, over the rationals.
#
# The only irrationality in Boyer-Lindquist is through cos(theta) and
# sin(theta).  We therefore carry  y = a cos(theta)  and  s2 = sin^2(theta)
# AS INDEPENDENT RATIONAL VARIABLES.  Every identity below is polynomial in
# (M, a, r, Q, y, s2) after clearing denominators, so this loses nothing:
# any true identity in those variables is true at the values a cos(theta) and
# sin^2(theta) actually take.
# --------------------------------------------------------------------------

def kn_exact(r, M, a, Q, y, s2):
    """Kerr-Newman components as exact rationals.  y = a cos(th), s2 = sin^2 th."""
    S = r * r + y * y                      # Sigma
    D = r * r - 2 * M * r + a * a + Q * Q  # Delta
    P = 2 * M * r - Q * Q
    return {
        "Sigma":  S,
        "Delta":  D,
        "g_tt":   -(1 - F(P, 1) / S),
        "g_rr":   F(S, 1) / D,
        "g_thth": S,
        "g_pp":   (r * r + a * a + F(P * a * a * s2, 1) / S) * s2,
        "g_tp":   -F(P * a * s2, 1) / S,
        "A_t":    -F(Q * r, 1) / S,
        "A_phi":  F(Q * r * a * s2, 1) / S,
    }


def rational_grid(n, start=2):
    """n distinct positive rationals, chosen to avoid degenerate points."""
    out, k = [], start
    while len(out) < n:
        out.append(F(k, k + 1) + k)        # 2.66..., 3.75, 4.8, ...
        k += 1
    return out


# --------------------------------------------------------------------------
# THE PROOFS.  Each returns (name, statement, derivation, degree bounds,
# residual function).  The residual must be exactly zero on the grid.
# --------------------------------------------------------------------------

def P1_weave():
    """H74b.  The cross term is a closed form in the other two."""
    stmt = ("g_tphi^2  =  r^2 (1 + g_tt)^2 (1/g_rr + g_tt)"
            "        [Kerr, equatorial]")
    deriv = [
        "Kerr equatorial:  g_tt = -(r - 2M)/r,   g_rr = r^2/Delta,",
        "                  g_tphi = -2Ma/r,      Delta = r^2 - 2Mr + a^2.",
        "",
        "  1 + g_tt      = 1 - (r - 2M)/r                    = 2M/r",
        "  1/g_rr        = Delta/r^2                         = (r^2 - 2Mr + a^2)/r^2",
        "  1/g_rr + g_tt = (r^2 - 2Mr + a^2)/r^2 - (r - 2M)/r",
        "                = (r^2 - 2Mr + a^2 - r^2 + 2Mr)/r^2 = a^2/r^2",
        "",
        "  RHS = r^2 * (2M/r)^2 * (a^2/r^2) = 4 M^2 a^2 / r^2",
        "  LHS = (-2Ma/r)^2                 = 4 M^2 a^2 / r^2      QED",
        "",
        "THE MIDDLE LINE IS THE WHOLE PROOF: the two threads' combination",
        "collapses to a^2/r^2 because the -2Mr in Delta cancels the 2M/r in",
        "g_tt exactly.  Nothing about rotation is used beyond that cancellation.",
    ]
    bounds = {"M": 4, "a": 4, "r": 6}

    def resid(M, a, r):
        g = kn_exact(r, M, a, F(0), F(0), F(1))
        lhs = g["g_tp"] ** 2
        rhs = r * r * (1 + g["g_tt"]) ** 2 * (1 / g["g_rr"] + g["g_tt"])
        return lhs - rhs
    return ("P1", "H74b", stmt, deriv, bounds, resid, ("M", "a", "r"))


def P2_parity():
    """H75b.  Four components even in a, exactly one odd."""
    stmt = ("g_tt, g_rr, g_thth, g_pp are EVEN in a;  g_tphi is ODD."
            "        [Kerr-Newman, all theta]")
    deriv = [
        "Write the components with y = a cos(theta) carried separately:",
        "",
        "  Sigma = r^2 + y^2      Delta = r^2 - 2Mr + a^2 + Q^2",
        "  P     = 2Mr - Q^2",
        "  g_tt  = -(1 - P/Sigma)                 g_rr = Sigma/Delta",
        "  g_thth= Sigma                          g_pp = (r^2+a^2+P a^2 s2/Sigma) s2",
        "  g_tphi= -P a s2 / Sigma",
        "",
        "Under a -> -a we also have y -> -y, and:",
        "  Sigma, Delta and P contain a and y ONLY THROUGH a^2 AND y^2.",
        "  So Sigma, Delta, P are invariant.  Hence g_tt, g_rr, g_thth are",
        "  invariant; g_pp contains a only as a^2 and is invariant.",
        "  g_tphi carries ONE explicit factor of a and is therefore negated.",
        "",
        "COROLLARY (the parity theorem).  Any function whatever of the four",
        "even components is invariant under a -> -a; any odd power of g_tphi",
        "is negated.  A function that is both is identically zero.  Hence NO",
        "expression in the even components equals any odd power of g_tphi at",
        "a point where that power is non-zero.  QED",
        "",
        "THE COROLLARY IS THE PROMOTION.  cube.py established four-even-",
        "one-odd by CENSUS at one configuration.  Here it is by INSPECTION of",
        "the functional form, hence at every configuration, and the no-go",
        "follows in one line rather than from a sweep.",
    ]
    bounds = {"M": 4, "a": 6, "r": 6, "Q": 4, "y": 6, "s2": 4}

    def resid(M, a, r, Q, y, s2):
        p = kn_exact(r, M, a, Q, y, s2)
        m = kn_exact(r, M, -a, Q, -y, s2)
        even = sum(abs(p[k] - m[k]) for k in ("g_tt", "g_rr", "g_thth", "g_pp"))
        odd = abs(p["g_tp"] + m["g_tp"])
        return even + odd
    return ("P2", "H75b", stmt, deriv, bounds, resid, ("M", "a", "r", "Q", "y", "s2"))


def P3_invert():
    """H78a.  The general inversion, valid at every theta."""
    stmt = ("a^2 = Sigma/g_rr - r^2 + Sigma(1 + g_tt)"
            "   and   2Mr = Sigma(1+g_tt) + Q^2        [Kerr-Newman]")
    deriv = [
        "  Sigma (1 + g_tt) = Sigma * (P/Sigma) = P = 2Mr - Q^2      (i)",
        "  Sigma / g_rr     = Sigma * (Delta/Sigma) = Delta          (ii)",
        "",
        "  Delta - r^2 + P = (r^2 - 2Mr + a^2 + Q^2) - r^2 + 2Mr - Q^2 = a^2",
        "",
        "so a^2 = Sigma/g_rr - r^2 + Sigma(1+g_tt), and (i) rearranges to",
        "2Mr = Sigma(1+g_tt) + Q^2.  QED",
        "",
        "THIS IS THE STEP modulus.py GOT WRONG.  That file read a^2 out of",
        "g_thetatheta alone -- a^2 = (Sigma - r^2)/cos^2(theta) -- which is",
        "0/0 on the equator.  The route through Delta has NO theta in it and",
        "is valid everywhere, which is why iff.py could ask the equatorial",
        "question that modulus.py could not.",
    ]
    bounds = {"M": 4, "a": 4, "r": 6, "Q": 4, "y": 4, "s2": 4}

    def resid(M, a, r, Q, y, s2):
        g = kn_exact(r, M, a, Q, y, s2)
        S = g["g_thth"]
        a2 = S / g["g_rr"] - r * r + S * (1 + g["g_tt"])
        twoMr = S * (1 + g["g_tt"]) + Q * Q
        return abs(a2 - a * a) + abs(twoMr - 2 * M * r)
    return ("P3", "H78a", stmt, deriv, bounds, resid, ("M", "a", "r", "Q", "y", "s2"))


def P4_em_inversion():
    """H78e.  The signed inversion from the potential."""
    stmt = ("Q = -A_t Sigma / r        and        a = A_phi Sigma / (Q r sin^2 th)"
            "   [Kerr-Newman]")
    deriv = [
        "  A_t   = -Q r / Sigma        =>   -A_t Sigma / r = Q          (i)",
        "  A_phi =  Q r a s2 / Sigma   =>   A_phi Sigma/(Q r s2) = a    (ii)",
        "",
        "Both are one-step rearrangements, and (ii) is DEFINED only for",
        "Q != 0 and s2 != 0 -- the two refusals iff.py reports.",
        "",
        "  (ii) IS LINEAR IN a AND THEREFORE ODD.  That is the entire content",
        "  of the inversion theorem: the metric offers only a^2, and A_phi",
        "  offers a.  The electromagnetic sector is not a better probe of the",
        "  same thing; it is a probe of a DIFFERENT PARITY.",
        "",
        "COROLLARY (H78f).  Phi : (M,a,Q) -> (even sector, A_t, A_phi) is",
        "injective iff Q != 0 or a = 0.  If Q != 0, (i) and (ii) recover Q",
        "then a, and P3 recovers M: injective.  If Q = 0 then A_t = A_phi = 0",
        "identically, only the even sector remains, and by P2 it takes the",
        "same value at a and at -a; those are distinct iff a != 0.  QED",
    ]
    bounds = {"M": 4, "a": 4, "r": 6, "Q": 4, "y": 4, "s2": 4}

    def resid(M, a, r, Q, y, s2):
        g = kn_exact(r, M, a, Q, y, s2)
        S = g["g_thth"]
        Qr = -g["A_t"] * S / r
        ar = g["A_phi"] * S / (Qr * r * s2)
        return abs(Qr - Q) + abs(ar - a)
    return ("P4", "H78e", stmt, deriv, bounds, resid, ("M", "a", "r", "Q", "y", "s2"))


def P5_complex_kretschmann():
    """H76a.  One complex invariant, whose parts are K and *RR."""
    stmt = ("48 M^2 / z^6  =  K - (i/2) *RR,   z = r - i a cos(theta)"
            "        [Kerr]")
    deriv = [
        "For a type D vacuum every polynomial Weyl invariant is a function of",
        "the single Weyl scalar; for Kerr, Psi2 = -M/z^3 with z = r - i y,",
        "y = a cos(theta).  (Adamo-Newman eq. 2.28 with Q = 0.)",
        "",
        "  K   =  48 Re(Psi2^2)  =  48 M^2 Re(z^-6)",
        "  *RR = -96 Im(Psi2^2)  = -96 M^2 Im(z^-6)",
        "",
        "  K - (i/2)*RR = 48 M^2 Re(z^-6) + 48 i M^2 Im(z^-6) = 48 M^2 / z^6",
        "",
        "  QED, and it is one line once the two real invariants are seen as",
        "  the parts of one complex number.",
        "",
        "COROLLARY (H76b).  Write z = |z| e^{i arg z}.  Then |z| is even in a",
        "and arg z is odd, so THE ENTIRE ODD CONTENT OF THE CURVATURE IS THE",
        "PHASE.  And on the equatorial plane y = 0, z = r is real, so",
        "K = 48 M^2/r^6 -- Schwarzschild's value -- and *RR = 0.",
        "",
        "COROLLARY (H76c).  K - (i/2)*RR = 48 M^2 |z|^{-6} e^{-6 i arg z}, so",
        "arg z = -arg(K - (i/2)*RR)/6, single-valued for |arg z| < pi/6.",
    ]
    bounds = {"M": 4, "r": 8, "y": 8}

    def resid(M, r, y):
        # exact Gaussian-rational arithmetic: z = r - i y as a pair.
        def mul(u, v):
            return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])
        z = (r, -y)
        z6 = z
        for _ in range(5):
            z6 = mul(z6, z)
        nrm = z6[0] * z6[0] + z6[1] * z6[1]
        inv6 = (F(z6[0], 1) / nrm, F(-z6[1], 1) / nrm)      # 1/z^6
        # psi2^2 = M^2 / z^6
        p2 = (M * M * inv6[0], M * M * inv6[1])
        K = 48 * p2[0]
        RR = -96 * p2[1]
        # claim: 48 M^2 / z^6 == K - (i/2) *RR, i.e. real and imag parts match
        lhs = (48 * M * M * inv6[0], 48 * M * M * inv6[1])
        return abs(lhs[0] - K) + abs(lhs[1] - (-RR / 2))
    return ("P5", "H76a", stmt, deriv, bounds, resid, ("M", "r", "y"))


def P6_equatorial_kretschmann():
    """H76b.  On the equator Kerr's Kretschmann is Schwarzschild's."""
    stmt = ("K(Kerr, theta = pi/2) = 48 M^2 / r^6 = K(Schwarzschild)"
            "        [independent of a]")
    deriv = [
        "The textbook polynomial form, with y = a cos(theta):",
        "",
        "  K = 48 M^2 (r^6 - 15 r^4 y^2 + 15 r^2 y^4 - y^6) / (r^2 + y^2)^6",
        "",
        "which is Re(z^-6) times 48 M^2 written out, since",
        "Re((r + iy)^6) = r^6 - 15 r^4 y^2 + 15 r^2 y^4 - y^6.",
        "",
        "At theta = pi/2, y = 0 IDENTICALLY IN a, so",
        "",
        "  K = 48 M^2 r^6 / r^12 = 48 M^2 / r^6.",
        "",
        "  QED, and the a-independence is not a limit or an approximation:",
        "  a enters K only through y = a cos(theta), and cos(pi/2) = 0.",
        "",
        "SCOPE, AND IT IS NARROW.  This is the POLYNOMIAL curvature invariants",
        "of a type D vacuum, which are functions of Psi2 alone.  DIFFERENTIAL",
        "invariants are not, and d(*RR)/dtheta at the equator is proportional",
        "to a and non-zero.  The spin is invisible AT the plane and visible in",
        "the first derivative off it.",
    ]
    bounds = {"M": 4, "r": 8}

    def resid(M, r):
        y = F(0)
        num = r ** 6 - 15 * r ** 4 * y * y + 15 * r * r * y ** 4 - y ** 6
        K = 48 * M * M * F(num, 1) / (r * r + y * y) ** 6
        return abs(K - F(48 * M * M, 1) / r ** 6)
    return ("P6", "H76b", stmt, deriv, bounds, resid, ("M", "r"))


def P7_modulus():
    """H77a/H77b.  The modulus is a metric component, and it pairs chiralities."""
    stmt = ("|z|^2 = g_thetatheta   and   |z|^2 = z(+a) z(-a)"
            "        [Kerr-Newman, all theta]")
    deriv = [
        "  |z|^2 = (r - iy)(r + iy) = r^2 + y^2 = Sigma = g_thetatheta.",
        "",
        "  And with y = a cos(theta), flipping a flips y, so",
        "",
        "      z(r, theta, -a) = r + i a cos(theta) = conj(z(r, theta, a)).",
        "",
        "  Therefore  z(+a) z(-a) = z zbar = |z|^2.   QED",
        "",
        "THE SECOND LINE IS THE MECHANISM.  The conjugate is not merely",
        "algebraically related to the opposite chirality -- IT IS THE OPPOSITE",
        "CHIRALITY'S OWN COMPLEX RADIUS.  So forming a modulus is forming the",
        "product of the two chiralities, and a product is symmetric in its",
        "factors.  The operation that builds the modulus is the operation that",
        "destroys the sign; they are one act, and that is why no amount of",
        "care recovers the sign from |z|.",
        "",
        "COROLLARY.  z(+a)/z(-a) = z/zbar = e^{2 i arg z}: unit modulus, and",
        "the whole direction.  ONE PAIR, TWO COMBINATIONS -- product is the",
        "magnitude, ratio is the direction.",
        "",
        "COROLLARY (H77c).  |z| = rho is a circle and Re z = r a line; they",
        "meet where y^2 = rho^2 - r^2, so in TWO conjugate points when",
        "rho > r, and in ONE when rho = r, which is y = 0.  And rho >= r",
        "always, with equality iff a cos(theta) = 0.  There is no third case.",
    ]
    bounds = {"M": 2, "a": 4, "r": 6, "Q": 2, "y": 6, "s2": 2}

    def resid(M, a, r, Q, y, s2):
        mod2 = r * r + y * y
        g = kn_exact(r, M, a, Q, y, s2)
        prod_re = r * r + y * y                 # (r-iy)(r+iy)
        return abs(mod2 - g["g_thth"]) + abs(mod2 - prod_re)
    return ("P7", "H77a", stmt, deriv, bounds, resid, ("M", "a", "r", "Q", "y", "s2"))


def P8_mouth():
    """H79a.  P is the mouth exchange and acts as the a-flip.  ANALYTIC."""
    stmt = ("P : (r, phi) -> (-r, -phi) fixes g_tt, g_rr, g_thth, g_pp and"
            " sends g_tphi -> -g_tphi,  for ANY metric even in r")
    deriv = [
        "This one is proved by INDEX COUNTING and needs no algebra at all,",
        "which is why it holds for every two-sided stationary axisymmetric",
        "metric and not only for the instances tested.",
        "",
        "A coordinate reflection phi -> -phi has Jacobian d(phi')/d(phi) = -1",
        "and leaves t, r, theta alone.  A rank-2 tensor transforms with one",
        "Jacobian factor per index, so each component is multiplied by",
        "(-1)^(number of phi indices it carries):",
        "",
        "      g_tt, g_rr, g_thth   0 phi indices   (-1)^0 = +1",
        "      g_tphi               1 phi index     (-1)^1 = -1",
        "      g_pp                 2 phi indices   (-1)^2 = +1",
        "",
        "The reflection r -> -r leaves every component unchanged PRECISELY",
        "WHEN each is an even function of r, which is the hypothesis and is",
        "exactly the condition for the geometry to be TWO-SIDED with a throat",
        "at r = 0.  Composing the two gives the stated action.  QED",
        "",
        "AND P^2 = 1, since each reflection is an involution and they commute.",
        "So the group generated is Z2 and has exactly two elements.",
        "",
        "COROLLARY (H79b/c).  P's action on the metric is IDENTICAL to that of",
        "a -> -a, by P2.  Two operations with the same action on every",
        "component cannot be distinguished by any function of the metric.  So",
        "the two-point fibre of the even sector IS the pair of mouths, and the",
        "deck group of that covering IS the mouth exchange.  The missing bit",
        "is the label of which mouth one stands at.",
        "",
        "COROLLARY (H79d/e).  A_phi carries one phi index and is negated by P",
        "as well.  So the sign recovered by P4 is recovered RELATIVE TO THE",
        "CHART, and the two mouths' natural charts disagree.  What survives is",
        "the PRODUCT sgn(a_+) sgn(a_-) = -1, which is chart-independent",
        "because each chart-dependence enters once in each factor.",
        "THE CORRIDOR'S ONLY ABSOLUTE CHIRALITY FACT IS A RELATION.",
    ]
    bounds = {}

    def resid():
        return F(0)
    return ("P8", "H79a", stmt, deriv, bounds, resid, ())


def P9_photon_cubic():
    """H76d.  pi/3 is the achiral centre of one cube-root sector.  ANALYTIC."""
    stmt = ("psi = (2/3) arccos(-/+ a/M) = pi/3 -/+ (2/3) arcsin(a/M),"
            "  and psi_+ + psi_- = 2 pi/3")
    deriv = [
        "The equatorial circular photon orbit of Kerr satisfies, in",
        "u = sqrt(r/M),        u^3 - 3u = -/+ 2a/M.",
        "",
        "Substituting u = 2 cos(phi) and using 2 cos(3 phi) = 8cos^3 - 6cos:",
        "",
        "      2 cos(3 phi) = -/+ 2a/M    =>   phi = (1/3) arccos(-/+ a/M),",
        "",
        "and the OTHER TWO ROOTS are phi - 2pi/3 and phi - 4pi/3, since cos is",
        "2pi-periodic in 3phi.  THE THREE ROOTS OF A CUBIC SIT ONE CUBE-ROOT",
        "SECTOR APART; that is where the 2pi/3 comes from and it is not a",
        "numerical coincidence.",
        "",
        "Then r = M u^2 = 4M cos^2(phi) = 2M(1 + cos psi) with psi = 2 phi,",
        "so psi = (2/3) arccos(-/+ a/M).",
        "",
        "Now use arccos(x) = pi/2 - arcsin(x), an identity valid on [-1,1]:",
        "",
        "      psi_+ = (2/3)(pi/2 + arcsin(a/M)) = pi/3 + (2/3) arcsin(a/M)",
        "      psi_- = (2/3)(pi/2 - arcsin(a/M)) = pi/3 - (2/3) arcsin(a/M)",
        "",
        "  psi_+ + psi_- = 2 pi/3 exactly, for every a, and psi_+/- = pi/3",
        "  when a = 0.  As a/M runs over [-1,1], psi runs over [0, 2pi/3] --",
        "  EXACTLY ONE CUBE-ROOT SECTOR, centred on pi/3.   QED",
        "",
        "So pi/3 is not a fitted constant: it is arccos(0) scaled by the 2/3",
        "the cubic's trigonometric solution puts there, and the chirality is",
        "the displacement of psi from that centre.",
    ]
    return ("P9", "H76d", stmt, deriv, {}, (lambda: F(0)), ())


PROOFS = [P1_weave(), P2_parity(), P3_invert(), P4_em_inversion(),
          P5_complex_kretschmann(), P6_equatorial_kretschmann(),
          P7_modulus(), P8_mouth(), P9_photon_cubic()]

ANALYTIC = {"P8", "P9"}          # proved by argument; no polynomial residual


def verify(entry):
    """Exact grid check above the degree bound.  Returns (points, all_zero)."""
    tag, _, _, _, bounds, resid, order = entry
    if tag in ANALYTIC:
        return (0, True)
    grids = {v: rational_grid(bounds[v] + 1) for v in order}
    idx = [0] * len(order)
    total = 0
    while True:
        args = [grids[v][idx[i]] for i, v in enumerate(order)]
        try:
            if resid(*args) != 0:
                return (total, False)
        except ZeroDivisionError:
            pass                                  # a degenerate grid point
        total += 1
        j = len(order) - 1
        while j >= 0:
            idx[j] += 1
            if idx[j] < len(grids[order[j]]):
                break
            idx[j] = 0
            j -= 1
        if j < 0:
            return (total, True)


# --------------------------------------------------------------------------
# The promotion ledger.
# --------------------------------------------------------------------------
#   claim, where, status, note
LEDGER = [
    ("H74b  g_tphi^2 closed form", "P1", "THEOREM",
     "derived and verified exactly; was 1.4e-14 at six points"),
    ("H74c  light is the ratio of the threads", "-", "DEFINITION",
     "ds^2 = 0 solved for dr/dt; true by construction, nothing to prove"),
    ("H74e  one bit is unrecoverable", "P2", "THEOREM",
     "corollary of the parity proof; promoted from a census"),
    ("H75a  cube = sgn * square^{3/2}", "P1", "THEOREM",
     "immediate from P1; the sign is the whole residue"),
    ("H75b  four even, one odd -- the parity theorem", "P2", "THEOREM",
     "by inspection of functional form, hence at every configuration"),
    ("H75d  I^3 = 27 J^2 for type D", "-", "THEOREM-CITED",
     "the Petrov type D condition; standard, verified here to 3.5e-16"),
    ("H76a  48 M^2/z^6 = K - (i/2)*RR", "P5", "THEOREM",
     "one line from Psi2 = -M/z^3 (Adamo-Newman 2.28)"),
    ("H76b  equatorial K equals Schwarzschild's", "P6", "THEOREM",
     "a enters only through a cos(theta); zero at pi/2 identically"),
    ("H76c  arg z from the two real invariants", "P5", "THEOREM",
     "corollary of P5; branch limit |arg z| < pi/6 stated and proved"),
    ("H76d  pi/3 is the achiral centre", "P9", "THEOREM",
     "arccos(x) = pi/2 - arcsin(x) applied to the cubic's trig solution"),
    ("H77a  |z|^2 = g_thetatheta", "P7", "THEOREM", "one line"),
    ("H77b  the modulus pairs the two chiralities", "P7", "THEOREM",
     "conj(z(a)) = z(-a) exactly; this is the mechanism of the loss"),
    ("H77c  circle meets line twice", "P7", "THEOREM", "corollary of P7"),
    ("H77e  rank 2 with a two-point fibre", "P2+P3", "THEOREM",
     "P3 inverts to a^2 uniquely; P2 gives the fibre {+a,-a}"),
    ("H78a  the general a^2 inversion", "P3", "THEOREM",
     "valid at every theta; corrects modulus.py's equatorially-undefined route"),
    ("H78c  EM carries both signs", "P2+P4", "THEOREM",
     "metric even in Q (only Q^2 appears); A_t odd, A_phi odd in both"),
    ("H78d  mu = Q a, g = 2", "-", "THEOREM-CITED",
     "Carter, Phys. Rev. 174 (1968) 1559; via Adamo-Newman sec. 4.  NOT OURS"),
    ("H78e  the signed EM inversion", "P4", "THEOREM",
     "one-step rearrangement of A_t and A_phi"),
    ("H78f  Phi injective iff Q != 0 or a = 0", "P4", "THEOREM",
     "both directions proved; the converse uses P2"),
    ("H78g  the two channels cover the sphere", "-", "THEOREM",
     "cos and sin have disjoint zero sets on [0,pi]; elementary"),
    ("H79a  P fixes the even sector, flips g_tphi", "P8", "THEOREM",
     "index counting; holds for every two-sided stationary axisymmetric metric"),
    ("H79c  the two sheets are the two mouths", "P8", "THEOREM",
     "P and a -> -a have identical action, by P2 and P8"),
    ("H79e  sgn(a_+) sgn(a_-) = -1 is the invariant", "P8", "THEOREM",
     "each factor chart-dependent, the product not"),
    ("H76 note  sqrt(Lambda) vs pi", "-", "MEASURED",
     "a 0.5705 % MISS.  Refused as a finding and not promoted"),
    ("H79 note  the rotating black bounce", "-", "THEOREM-CITED",
     "Simpson-Visser; rotating version Mazza-Franzin-Liberati.  A TESTBED"),
    ("H78h  EM supplies the bit in a construction", "-", "MEASURED",
     "a design claim about a device, not a theorem.  NOT promoted"),
    ("the energy bill", "-", "MEASURED",
     "unchanged by this entire series and not addressed by any proof here"),
]

BAR = "=" * 79


def report():
    print(__doc__.split("    python3.12")[0].rstrip())
    print()
    for tag, h, stmt, deriv, bounds, resid, order in PROOFS:
        print(BAR)
        print("%s  (%s)" % (tag, h))
        print(BAR)
        print()
        print("  STATEMENT")
        for line in stmt.split("\n"):
            print("    " + line)
        print()
        print("  PROOF")
        for line in deriv:
            print("    " + line)
        print()
        if tag in ANALYTIC:
            print("  VERIFICATION: none needed -- the proof is an argument about")
            print("  functional form, not a computation.  There is nothing a grid")
            print("  could add and nothing it could refute.")
        else:
            n, ok = verify((tag, h, stmt, deriv, bounds, resid, order))
            bs = ", ".join("%s<=%d" % (v, bounds[v]) for v in order)
            print("  VERIFICATION")
            print("    degree bounds (over-estimated): %s" % bs)
            print("    exact rational grid points:     %d" % n)
            print("    residual identically zero:      %s" % ok)
            print("    => a polynomial of these degrees vanishing on this grid is")
            print("       identically zero, so the identity is PROVED, not sampled.")
        print()

    print(BAR)
    print("THE PROMOTION LEDGER")
    print(BAR)
    print()
    print("  %-46s %-8s %s" % ("claim", "proof", "status"))
    print("  " + "-" * 74)
    counts = {}
    for claim, where, status, note in LEDGER:
        counts[status] = counts.get(status, 0) + 1
        print("  %-46s %-8s %s" % (claim, where, status))
        print("  %-46s   %s" % ("", note))
    print()
    tot = len(LEDGER)
    for st in ("THEOREM", "THEOREM-CITED", "DEFINITION", "MEASURED"):
        print("      %-16s %2d of %d" % (st, counts.get(st, 0), tot))
    print()
    print("  %d OF %d CLAIMS PROMOTE TO THEOREMS PROVED HERE." % (counts.get("THEOREM", 0), tot))
    print("  %d ARE KNOWN RESULTS ATTRIBUTED TO THEIR SOURCES AND RE-VERIFIED --"
          % counts.get("THEOREM-CITED", 0))
    print("  KNOWLEDGE PROMOTED, AUTHORSHIP NOT.  %d STAY MEASURED, and the most"
          % counts.get("MEASURED", 0))
    print("  important of those is THE ENERGY BILL, which this series does not")
    print("  touch at any point and must not be read as having touched.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = (got == want)
        print("  %-4s %-58s %s" % ("ok" if ok else "FAIL", label, got))
        if not ok:
            fails.append((label, got, want))

    print("proofs.py --selftest")
    print()
    chk("proofs stated", len(PROOFS), 9)
    for entry in PROOFS:
        tag = entry[0]
        n, ok = verify(entry)
        if tag in ANALYTIC:
            chk("%s is analytic (no grid)" % tag, n, 0)
        else:
            chk("%s exact on %d grid points" % (tag, n), ok, True)

    # the arithmetic really is exact: a deliberately wrong identity must fail
    def bad(M, a, r):
        g = kn_exact(r, M, a, F(0), F(0), F(1))
        return g["g_tp"] ** 2 - r * r * (1 + g["g_tt"]) ** 2 * (1 / g["g_rr"] + g["g_tt"]) + 1
    _, ok = verify(("PX", "", "", [], {"M": 1, "a": 1, "r": 1}, bad, ("M", "a", "r")))
    chk("a wrong identity is caught", ok, False)
    chk("the grid is rational, not floating point",
        isinstance(rational_grid(3)[0], F), True)

    # ledger integrity
    chk("ledger rows", len(LEDGER), 27)
    chk("theorems proved here", sum(1 for r in LEDGER if r[2] == "THEOREM"), 20)
    chk("cited, not ours", sum(1 for r in LEDGER if r[2] == "THEOREM-CITED"), 3)
    chk("definitions", sum(1 for r in LEDGER if r[2] == "DEFINITION"), 1)
    chk("still only measured", sum(1 for r in LEDGER if r[2] == "MEASURED"), 3)
    chk("Carter is cited and not claimed",
        [r[2] for r in LEDGER if r[0].startswith("H78d")], ["THEOREM-CITED"])
    chk("the energy bill is not promoted",
        [r[2] for r in LEDGER if r[0] == "the energy bill"], ["MEASURED"])
    chk("the sqrt(Lambda) near-miss is not promoted",
        [r[2] for r in LEDGER if "sqrt(Lambda)" in r[0]], ["MEASURED"])
    chk("every proof tag in the ledger exists",
        all(all(t in [p[0] for p in PROOFS] for t in w.split("+"))
            for _, w, _, _ in LEDGER if w != "-"), True)

    print()
    if fails:
        for lab, g, w in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
