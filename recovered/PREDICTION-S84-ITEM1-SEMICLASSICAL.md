# PREDICTION — s84 · ITEM 1 · CLAUSE 1 · THE SEMICLASSICAL HALF
# FILED BEFORE ANY NUMBER IS COMPUTED FROM THE FIELD. Instrument: pack84/semi84.py.
# Target, from ORDER-FOR-S84 Item 1, unwidened:
#   derive a property of F_core forcing g(rank 1) > g(rank 2) at the WIDTH-2 FRONTIER,
#   and account for Z=90.

## THE OBJECT, AND WHY IT IS THE ONE THE ORDER NAMES

s83 reduced Madelung to G-within: **g(l) = l + delta(n,l) increasing in l**. In a pure
Coulomb field delta == 0 and g = l, so **G-within is satisfied trivially by hydrogen
and is destroyed only by the core**: the defect falls with l, and G-within survives if
and only if it falls by LESS THAN ONE UNIT PER UNIT l. That is the open question the
order names, and it is a statement about one scalar function of the radial potential.

## THE DERIVATION BEING TESTED — STATED IN FULL BEFORE IT IS MEASURED

Semiclassical (Langer) phase integral for a radial potential with enclosed-charge
function q(r) := -r V(r), at the channel's own energy E, with L := l + 1/2:

    p(r) = sqrt( 2E + 2q(r)/r - L^2/r^2 ),    Phi(L) = int_a^b p dr  over p > 0
    pi * delta = Phi - Phi_Coulomb   (same E, same L, q == 1)

Differentiating the phase integral in L^2 (turning-point terms vanish, p = 0 there):

    dPhi/dL^2 = -(1/2) * I,     I(L) := int_a^b dr / ( r^2 p(r) )

**ANCHOR THEOREM (EXACT, NOT SEMICLASSICAL-APPROXIMATE).** Substituting u = 1/r turns
I into the integral of an inverse square root of a QUADRATIC in u, between its own two
roots: I = int du / sqrt(2E + 2q0 u - L^2 u^2) = **pi / L, for ANY constant q0 and ANY
bound E.** The charge cancels identically. Hydrogen and a bare nucleus of charge Z
give the same I.

Hence, with I_C = pi/L,

    **dg/dl = 2 - I/I_C   and   G-within (dg/dl > 0)  <=>  I < 2 * I_C.**

**THIS IS THE PROPERTY OF F_core THE ORDER ASKS FOR, IN CANDIDATE FORM.** Its content:
a field that is Coulombic anywhere — inner charge Z or outer charge 1, it does not
matter — contributes EXACTLY the hydrogenic amount, so **the entire l-dependence of
the defect comes from the region where q(r) is VARYING**, and G-within fails only if
that region alone doubles I. **IT IS NOT YET A PROOF: no bound on the variable-q
contribution is derived here.** What is filed is the identity, the exact anchor, and
the measurement of the gap between them.

## CLAUSES

S1 · **THE ANCHOR IS EXACT.** For a pure Coulomb of charge q0 in {1, 2, 89, 90} at any
     bound E and l in 0..4, the computed I equals pi/L to better than 1e-6 relative.
     Machinery, and it can fail: a quadrature that leaks at the turning points misses it.

S2 · **THE ANCHOR IS CHARGE-BLIND.** I(q0=1) and I(q0=90) agree to the same 1e-6 at
     identical (E, L). Filed separately from S1 because it is the load-bearing half:
     charge-blindness is what makes the variable-q region the whole story.

S3 · **dg/dl > 0 AT EVERY WIDTH-2 FRONTIER CHANNEL TESTED EXCEPT POSSIBLY Z=90.**
     I/I_C < 2 at every tested channel of the width-2 frontier.

S4 · **THE BAND. I/I_C LIES IN 0.6 .. 1.4 AT EVERY TESTED CHANNEL**, i.e. dg/dl in
     0.6 .. 1.4, clustered near 1. Basis: both Coulomb limits give exactly 1 and the
     transition region is a minority of the classically allowed range. **This is the
     clause I most expect to lose** — it is a guess at the SIZE of a term I have not
     bounded, and a single penetrating s channel could sit far outside it.

S5 · **THE DEVIATION |I/I_C - 1| IS LARGER FOR PENETRATING CHANNELS (l <= 1) THAN FOR
     l >= 3**, at every Z tested, by at least a factor of 2 in the median. Basis: a
     high-l orbit is excluded by the centrifugal term from the region where q varies,
     so it must sit nearer the anchor.

S6 · **Z=90 IS THE EXTREME ROW OF THE TESTED SET.** Its width-2 pair carries either
     the smallest dg/dl or the largest |I/I_C - 1| of every row tested. **If Z=90 is
     unremarkable on this instrument, the semiclassical route does NOT account for
     Z=90 and that is reported as a failure of the route, not smoothed over.**

S7 · **SIGN AGREEMENT WITH THE BANKED LADDER.** At each tested Z, the sign of the
     banked g(rank1) - g(rank2) agrees with the sign of the integrated semiclassical
     prediction across the same l interval. **Expected to hold at >= 5 of 6 rows.**
     **DECLARED LIMITATION, IN ADVANCE:** the two frontier channels differ in n as well
     as l, while dg/dl is taken at FIXED E. The comparison therefore mixes the
     l-derivative with an energy shift, and a disagreement at one row is evidence
     about the comparison, not necessarily about the identity. **F82.2's shape,
     declared before the run.**

S8 · **THE EXCHANGE TERM IS A DECLARED APPROXIMATION, NOT A RESULT.** The HF exchange
     is non-local; the instrument localises it as X/P to form q(r). Any claim here is
     conditional on that localisation, and the instrument reports q(r)'s measured tail
     value so the localisation can be checked against s82's q_eff = 1.000000.

## WHAT THIS CANNOT DO

**IT DOES NOT CLOSE CLAUSE 1.** A bound on the variable-q contribution is what would
close it, and no such bound is derived here. If every clause holds, what is earned is
that the target is now a bound on ONE integral over ONE region — and that G-within's
survival is anchored on an EXACT charge cancellation rather than on a fitted trend.
**NOTHING SEALED IS EDITED. c = 137.035999 remains the only number ever entered.**
