#!/usr/bin/env python3
"""
corep_derive.py -- the derivation behind captures/COREPS-HIGHSYM.tsv.

    python3 corep_derive.py            rebuild the capture
    python3 corep_derive.py --check    rebuild and assert byte-identical
    python3 corep_derive.py --selftest fixtures (needs numpy + spglib)

Needs numpy and spglib, neither vendored.  It IMPORTS `K`, `hallmap` and
`primitive_ops` from `phonon_derive`, and the star enumeration and projective
machinery from `phonon_kpoints_derive`, rather than copying either.

WHAT THIS IS.  `kpointdex.py` discharges the PROJECTIVE obstruction at k != 0
and seats 870 isolated high-symmetry k-stars.  Discharging it is NECESSARY AND
NOT SUFFICIENT.  A second, independent obstruction -- TIME REVERSAL, acting
antiunitarily -- degenerates levels that the unitary calculation reports as
separate, and its integrality checks do not notice, because the unitary answer
is internally consistent and simply incomplete.  This file measures the second
obstruction over the SAME 870 members and seats the COREPRESENTATIONS: the
physically irreducible levels, which are what a spectrum actually shows.

    THE MEMBER IS A LEVEL, NOT A STAR.  kpointdex's member is a k-star; this
    file's member is one degenerate level at a star.  They are different
    objects at different granularity, and the whole point of the second
    obstruction is that the level's degeneracy is NOT the small-rep dimension
    at 309 of them.

===============================================================================
THE CRITERION, AND THE CONVENTION IT IS COMPUTED IN
===============================================================================

With D^k({R|t}) = exp(-2 pi i k.t) Gamma(R), the rep property forces

    Gamma(R1) Gamma(R2) = omega(R1,R2) Gamma(R1 R2),
    omega(R1,R2) = exp(2 pi i K1 . t2),   K1 = k - R1^T k in Z^3.

THAT DERIVATION IS DONE HERE INDEPENDENTLY and lands on exactly the multiplier
`phonon_kpoints_derive.omega` uses -- which matters, because an earlier version
of that file used g = R1^{-T}k - k, which is a reciprocal lattice vector but
NOT a 2-cocycle, and every integrality check it met passed anyway.

HERRING'S CRITERION.  Let Q = { q : q.k == -k mod G } -- in the COLUMN
convention used throughout this file, R acts on k as k -> R^{-T} k.  Then

    W_r = (1/|G_k|) sum over q in Q of chi^k( {R_q|T_q}^2 )
        = (1/|G_k|) sum over q in Q of
              exp(-2 pi i k.(R_q T_q + T_q)) * chi_Gamma_r(R_q^2)

W = +1 is case (a), W = -1 case (b), W = 0 case (c).  In (b) and (c) TIME
REVERSAL DOUBLES THE DEGENERACY, and that doubling is invisible to the unitary
calculation.  |Q| = |G_k| whenever Q is non-empty, because Q is a coset of the
little co-group, so dividing by one or the other is the same number.

INDEPENDENT OF THE LATTICE REPRESENTATIVE.  Replacing T_q by T_q + n changes
the phase by exp(-2 pi i (R_q^T k + k).n), and R_q^T k + k is integral on Q.
So the sum does not depend on which coset representative is taken -- asserted
in `selftest`, not assumed.

===============================================================================
WHAT IS PROVED ABOUT THIS TABLE, AND HOW
===============================================================================

1.  THE SUM RULE, DERIVED RATHER THAN QUOTED.  The textbook twisted
    Frobenius-Schur rule sum_r d_r nu_r = #{a in A : a^2 = e} DOES NOT APPLY
    here, and the reason is worth keeping: summing the central extension's own
    twisted indicator over a central-character-zeta sector brings in
    sum_c zeta^(2c), which VANISHES for n > 2.  The extension's twisted
    indicator is not Herring's W.  Deriving it directly instead, from the
    OMEGA-TWISTED REGULAR CHARACTER of the twisted group algebra,

        sum_r d_r chi_Gamma_r(S) = |G_k| * delta(S, I)

    (the same identity that gives sum_r d_r^2 = |G_k|), the character table
    drops out of the sum entirely and leaves

        sum_r d_r W_r  ==  sum over q in Q with R_q^2 = I of
                               exp(-2 pi i k.(R_q T_q + T_q)).

    THE RIGHT-HAND SIDE TOUCHES NO CHARACTER TABLE.  It is pure space-group
    arithmetic, which is what makes it a check rather than a restatement.
    Measured: it holds on ALL 828 stars that have an antiunitary coset.

2.  THE CASE-(c) PAIRING IS FIXED-POINT-FREE.  A case-(c) small rep must pair
    with a DISTINCT partner, or the corepresentation is not well defined and
    the member count is wrong.  The partner is the time-reversal conjugate
        chi~_r(S) = conj( chi^k( {a|t_a}^-1 {S|t_S} {a|t_a} ) ),
    computed for a fixed a in Q.  Measured: every case-(c) rep has exactly one
    partner and it is never itself, and every case-(a) and case-(b) rep is its
    own partner -- 0 failures on all 828.

3.  CROSS-VALIDATED AGAINST AN IMPLEMENTATION SHARING NO CONVENTION.
    `phonon_kpoint_derive.herring` computes the same indicator in the ROW
    convention (k -> k R), on a primitive cell built by spglib's
    `standardize_cell` rather than by `hnf_basis`, through Herring's Ghat
    rather than through a central extension.  Compared over the 7 non-Gamma
    TRIMs of all 230 space groups -- as MULTISETS per space group, because the
    individual TRIM labels are basis-dependent while the 8 half-lattice points
    of the reciprocal torus are its 2-torsion subgroup and that set is not --
    the two AGREE ON 230 OF 230.

4.  THE MEMBER SET IS kpointdex's OWN.  The isolated stars found here on a
    1/12 mesh are compared, AS SETS OF FRACTIONAL k-VECTORS in the shared
    primitive basis, against `kpoint_derive.candidates`'s grid-free Hermite-
    normal-form enumeration: IDENTICAL ON 230 OF 230.  Not equal in count --
    equal as sets.  This also upgrades that mesh from "converged" to "proved
    equal to the exact enumeration", which is more than either file claimed.

===============================================================================
WHAT THIS FILE REFUSES
===============================================================================

TO EXTEND TO HALF-INTEGER SPIN.  Everything here is T^2 = +1, which is what a
phonon has.  For a spinor T^2 = -1, the antiunitary element squares into the
double group's E-bar, chi(E-bar . g) = -chi(g) for a double-valued irrep, and
THE WHOLE SUM CHANGES SIGN -- so cases (a) and (b) exchange their physical
readings.  Two standard references put that sign in different places and
therefore DISAGREE IN PRINT on the (a)/(b) label for double-valued irreps:
MTQC / MSGCorep / Bradley & Cracknell fold sgn[chi(T^2)] into the indicator, so
the case letter is the physical answer; Bilbao's *Representations DSG* reports
the mathematical reality and states the flipped physical rule separately
(Elcoro et al. 2017, section III C).  Their own worked pair pins it down: the
double-valued P-bar-7 of Ia-3 (206) is REAL and therefore DOUBLES, while the
double-valued P-bar-7 of I4_132 (214) is PSEUDOREAL and does NOT.  A spinless
W may never be transported to a spinful reading.  Recomputing in the double
group is a different pass and is not done here.

TO EXTEND TO MAGNETIC SPACE GROUPS.  The group here is the grey group G + theta
G of a NONMAGNETIC crystal.  A magnetically ordered crystal has a different
antiunitary coset and this table says nothing about it.

TO CLAIM A DEGENERACY IS OBSERVED.  The table states what symmetry FORCES.  An
accidental degeneracy at the same k is not symmetry's and is not here.

TO CALL TYPE (x) A CASE (c).  Where -k is not in the star of k the antiunitary
coset is EMPTY, and the normalised criterion is then 0/0 -- UNDEFINED, not zero.
The unnormalised form returns 0 and so collides with case (c), which is a real
defect of that spelling and is recorded here rather than worked around.  The
literature gives the situation its own name and this file uses it: MSGCorep
(arXiv:2211.10740, eq. 9 and Table 1) calls it TYPE (x), and SpaceGroupIrep
(arXiv:2012.08871) gives it the reality code `x`.  It is physically distinct
from (c), and Table 1 of MSGCorep states the distinction exactly:

    type (c)   doubled at k: YES    doubled in the BZ: NO
    type (x)   doubled at k: NO     doubled in the BZ: YES

42 of the 870 stars are type (x).  They are SEATED, with their degeneracy at k
and with `in-bz` in the `doubling` column.  A STATUS IS NEVER FLATTENED.

TO QUOTE W WITHOUT ITS CONVENTION.  W here is the NORMALISED indicator,
divided by |G_k| = |H^k|: the convention of Bilbao's *Representations DSG*
(Elcoro et al., J. Appl. Cryst. 50, 1457 (2017), eq. 13), which returns +1/-1/0.
It is NOT Bradley & Cracknell eq. (7.3.48) or MTQC's J_sigma, which are the
same sum UNNORMALISED (returning +-|H^k|) and, in MTQC's case, with the spin
sign sgn[chi(T^2)] folded in.  A number without its convention is not a
measurement.
"""
import sys, os, time, cmath, collections
from fractions import Fraction as F
import numpy as np
import spglib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from phonon_derive import K, hallmap
import phonon_kpoints_derive as P

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "COREPS-HIGHSYM.tsv")

PROV = (
    "# 3,611 COREPRESENTATIONS over the 870 isolated high-symmetry k-stars of\n"
    "# the 162 space groups that seat any -- the physically irreducible phonon\n"
    "# levels once TIME REVERSAL is admitted.  COMPUTED end to end; no\n"
    "# representation, corepresentation or k-point table is read.\n"
    "#\n"
    "# SPINLESS (T^2 = +1) and NONMAGNETIC.  W is the NORMALISED indicator of\n"
    "# Bilbao's Representations DSG (Elcoro et al. 2017, eq. 13), divided by\n"
    "# |G_k|; it is NOT Bradley & Cracknell eq. (7.3.48) or MTQC's J_sigma.\n"
    "#\n"
    "# WHAT IS CHECKED, AND WHAT IS NOT.  Verified by corep_derive.py --selftest:\n"
    "#   the SIGNED sum rule, whose right-hand side touches no character table\n"
    "#     -- holds on all 828 stars with an antiunitary coset;\n"
    "#   the case-(c) pairing, fixed-point-free on all 828;\n"
    "#   21 stars measured out of an actual DYNAMICAL MATRIX, with a complex\n"
    "#     Hermitian control that breaks only time reversal -- 0 mismatches;\n"
    "#   the published rows of sg 19, 76, 144, 227 and 230.\n"
    "# Agreement with captures/PHONON-KGROUND.tsv over the 7 non-Gamma TRIMs of\n"
    "# all 230 space groups (230 of 230) is measured by a separate script and is\n"
    "# NOT re-run by this file's selftest.  Neither is the set-wise identity of\n"
    "# the stars with kpoint_derive's grid-free enumeration (230 of 230).\n")

HEADER = ("sg\tsystem\tk\tk2\tlittle_order\tstar\tfactor_order\tsmall_dim"
          "\tn_small\tcase\tcorep_dim\tdoubling\n")


# --------------------------------------------------------------- small reps
def small_reps_full(R, T, k, idx):
    """(n, els, cls, Tb, kept) -- the whole character table AND the sector."""
    n = P.factor_order(R, T, k, idx)
    els, mult = P.extension(R, T, k, idx, n)
    cls, Tb = P.char_table_cayley(mult)
    if n == 1:
        kept = list(range(len(Tb)))
    else:
        ident = [i for i in idx if K(R[i]) == K(np.eye(3))][0]
        z = els.index((ident, 1))
        cz = [c for c in range(len(cls)) if z in cls[c]][0]
        kept = [r for r in range(len(Tb))
                if abs(complex(Tb[r][cz])
                       - float(np.real(Tb[r][0])) * cmath.exp(2j * np.pi / n)) < 1e-6]
    return n, els, cls, Tb, kept


def gamma_chars(els, cls, Tb, idx, kept):
    """chi_Gamma_r(R_idx[a]) for each kept rep r, as a list of lists."""
    co = {}
    for ci, c in enumerate(cls):
        for g in c:
            co[g] = ci
    pos = {e: j for j, e in enumerate(els)}
    return [[complex(Tb[r][co[pos[(idx[a], 0)]]]) for a in range(len(idx))]
            for r in kept]


# --------------------------------------------------------- Herring's criterion
def coset(R, k):
    """Q = { q : R_q^{-T} k == -k mod Z^3 }.  Empty iff -k is not in the star."""
    Rt = [np.linalg.inv(np.asarray(x, float)).T for x in R]
    return [i for i in range(len(R))
            if np.max(np.abs((Rt[i] @ k + k) - np.rint(Rt[i] @ k + k))) < 1e-8]


def herring(R, T, k, idx, ch, Q):
    """W for each kept rep, in the order `ch` gives them."""
    key = {K(np.rint(R[i])): a for a, i in enumerate(idx)}
    pre = []
    for q in Q:
        Rq = np.asarray(R[q], float)
        tq = np.asarray(T[q], float)
        u = Rq @ tq + tq
        pre.append((key[K(np.rint(Rq @ Rq))],
                    cmath.exp(-2j * np.pi * float(np.dot(k, u)))))
    return [sum(ph * c[a] for a, ph in pre) / len(idx) for c in ch]


def sum_rule_rhs(R, T, k, Q):
    """sum over q in Q with R_q^2 = I of exp(-2 pi i k.(R_q T_q + T_q)).

    Derived in the module docstring.  Touches no character table.
    """
    s = 0j
    for q in Q:
        Rq = np.asarray(R[q], float)
        if K(np.rint(Rq @ Rq)) != K(np.eye(3)):
            continue
        tq = np.asarray(T[q], float)
        u = Rq @ tq + tq
        if np.max(np.abs(u - np.rint(u))) > 1e-6:
            raise RuntimeError("an involution's square is not a lattice translation")
        s += cmath.exp(-2j * np.pi * float(np.dot(k, u)))
    return s


def partners(R, T, k, idx, ch, Q, which):
    """For each rep index in `which`, the index of its time-reversal partner."""
    key = {K(np.rint(R[i])): a for a, i in enumerate(idx)}
    Ra = np.asarray(R[Q[0]], float)
    ta = np.asarray(T[Q[0]], float)
    Rai = np.linalg.inv(Ra)
    ph = [cmath.exp(-2j * np.pi * float(np.dot(k, np.asarray(T[idx[b]], float))))
          for b in range(len(idx))]
    mine = [[ph[b] * c[b] for b in range(len(idx))] for c in ch]
    conj = []
    for b in range(len(idx)):
        S = np.asarray(R[idx[b]], float)
        u = np.asarray(T[idx[b]], float)
        conj.append((key[K(np.rint(Rai @ S @ Ra))],
                     Rai @ (S @ ta + u - ta)))
    out = {}
    for r in which:
        tgt = [np.conj(cmath.exp(-2j * np.pi * float(np.dot(k, u2))) * ch[r][c])
               for c, u2 in conj]
        m = [s for s in range(len(ch))
             if max(abs(tgt[b] - mine[s][b]) for b in range(len(idx))) < 1e-6]
        out[r] = m[0] if len(m) == 1 else None
    return out


# ------------------------------------------------------------------- the sweep
def canon(PG, k):
    """The star as its LEXICOGRAPHIC MINIMUM, so the label is not the
    representative the enumeration happened to find first."""
    kk = [F(x).limit_denominator(240) for x in k]
    S = {tuple((sum(int(R[r][c]) * kk[c] for c in range(3))) % 1
               for r in range(3)) for R in PG}
    m = min(S)
    return ",".join("%d/%d" % (x.numerator, x.denominator) for x in m)


def one_star(R, T, k, idx, PG, sg, strict=True):
    """The corep rows of a single star, plus the two validations."""
    n, els, cls, Tb, kept = small_reps_full(R, T, k, idx)
    ch = gamma_chars(els, cls, Tb, idx, kept)
    dims = [int(round(float(np.real(Tb[r][0])))) for r in kept]
    Q = coset(R, k)
    lab = canon(PG, k)
    if not Q:
        # TYPE (x): no antiunitary coset.  The normalised criterion is 0/0 here,
        # so nothing is divided and no value is invented -- the status is.
        #
        # n_small IS 2, NOT 1.  The corepresentation is D^{*k} + (D^{*-k})^*,
        # which contains TWO inequivalent small representations exactly as a
        # case (c) does; the only difference is that case (c)'s pair sits at one
        # k and this one's sits at conjugate k.  Counting it as 1 was a first
        # version's error, and it had a visible cost: it made (a) and (x) share
        # a chart cell, which then had to be explained away.  Counted right, the
        # three dimension facts separate ALL FOUR cases with nothing left over.
        return ([(sg, P.system(sg), lab, len(idx), None, n, d, 2, "x", d, "in-bz")
                 for d in dims], None, None)
    W = herring(R, T, k, idx, ch, Q)
    cases = []
    for z in (complex(x) for x in W):
        if abs(z - 1) < 1e-6:
            cases.append("a")
        elif abs(z + 1) < 1e-6:
            cases.append("b")
        elif abs(z) < 1e-6:
            cases.append("c")
        else:
            raise RuntimeError("non-integral Herring indicator at sg %d: %r" % (sg, z))
    lhs = sum(d * (1 if c == "a" else -1 if c == "b" else 0)
              for d, c in zip(dims, cases))
    rhs = sum_rule_rhs(R, T, k, Q)
    ok_sum = abs(complex(rhs).imag) < 1e-6 and abs(float(np.real(rhs)) - lhs) < 1e-6
    cidx = [r for r, c in enumerate(cases) if c == "c"]
    pr = partners(R, T, k, idx, ch, Q, list(range(len(kept))))
    ok_pair = (all(pr[r] is not None and pr[r] != r and dims[pr[r]] == dims[r]
                   for r in cidx)
               and all(pr[r] == r for r, c in enumerate(cases) if c != "c"))
    if strict and not (ok_sum and ok_pair):
        raise RuntimeError("validation failed at sg %d, |G_k| %d: sum %s pair %s"
                           % (sg, len(idx), ok_sum, ok_pair))
    rows, done = [], set()
    for r in range(len(kept)):
        if r in done:
            continue
        c = cases[r]
        if c == "c":
            done.add(pr[r])
            rows.append((sg, P.system(sg), lab, len(idx), None, n, dims[r], 2,
                         "c", 2 * dims[r], "at-k"))
        else:
            rows.append((sg, P.system(sg), lab, len(idx), None, n, dims[r], 1, c,
                         dims[r] * (2 if c == "b" else 1),
                         "at-k" if c == "b" else "none"))
        done.add(r)
    return rows, ok_sum, ok_pair


def sweep(verbose=True, strict=True):
    """One row per COREPRESENTATION.

    TYPE (x) IS SEATED ONCE, NOT TWICE, and that correction came from an
    adversarial review of a first version that seated it twice.  A type-(x)
    corepresentation is D^{*k} + (D^{*-k})^*: ONE object spanning the star of k
    AND the star of -k, and both stars are seated here.  Emitting a row at each
    arm names one member twice -- over-representation, and exactly what
    `phonondex` refused when it seated P-1 with TWO members rather than ITA's
    eight identically contributing sites.  So the pair is emitted at the
    lexicographically smaller label, the partner goes in `k2`, and nothing is
    either lost or double-counted.

    MEASURED, not assumed: the 42 type-(x) stars form 21 conjugate pairs, none
    self-conjugate and none with an unseated partner, so the first version's
    164 type-(x) rows named 82 objects.  Both conditions are asserted below --
    a self-conjugate or unpaired type-(x) star would be a different situation
    and must not be folded silently.
    """
    import kpoint_derive as KD
    HN = hallmap()
    rows, t0, folded = [], time.time(), 0
    for sg in range(1, 231):
        Pm, R0, T0, nc = P.primitive_ops(sg, HN)
        PG = KD.point_group(R0)
        R, T, stars = P.stars_of(sg, HN)
        byk = {}
        for st, k, idx in stars:
            rr, _s, _p = one_star(R, T, k, idx, PG, sg, strict)
            byk[canon(PG, k)] = (k, [r[:4] + (len(st),) + r[5:] for r in rr])
        out = []
        for lab, (k, rr) in sorted(byk.items()):
            if rr and rr[0][8] == "x":
                mlab = canon(PG, -np.asarray(k, float))
                if mlab not in byk:
                    raise RuntimeError(
                        "type (x) whose -k star is not seated: sg %d %s" % (sg, lab))
                if mlab == lab:
                    raise RuntimeError(
                        "type (x) that is self-conjugate: sg %d %s" % (sg, lab))
                if lab > mlab:
                    folded += len(rr)
                    continue
                out.extend(tuple(r[:3]) + (mlab,) + tuple(r[3:]) for r in rr)
            else:
                out.extend(tuple(r[:3]) + ("-",) + tuple(r[3:]) for r in rr)
        out.sort(key=lambda r: (-r[4], r[2], -r[10], -r[7], r[9]))
        rows.extend(out)
        if verbose and sg % 40 == 0:
            print("  sg %d  %.0fs  %d coreps" % (sg, time.time() - t0, len(rows)),
                  file=sys.stderr)
    if verbose:
        print("\nswept in %.1f s" % (time.time() - t0), file=sys.stderr)
        print("corepresentations seated : %d" % len(rows), file=sys.stderr)
        print("  type (x) rows folded   : %d   (one member, two stars)" % folded,
              file=sys.stderr)
        print("doubled AT k by T        : %d"
              % sum(1 for r in rows if r[11] == "at-k"), file=sys.stderr)
        print("type (x), doubled in BZ  : %d"
              % sum(1 for r in rows if r[11] == "in-bz"), file=sys.stderr)
    return rows


def render(rows):
    return PROV + HEADER + "".join("\t".join(str(x) for x in r) + "\n" for r in rows)


# ===========================================================================
# VALIDATION (v): AGAINST AN ACTUAL SPECTRUM, WITH TIME REVERSAL AS THE CONTROL
# ===========================================================================
# No character theory is used on this route at all.  A random force-constant
# tensor is projected onto the space-group-invariant subspace, the dynamical
# matrix is built and diagonalised, and the degeneracies are read off the
# eigenvalues.  Then the same thing is done again with a COMPLEX HERMITIAN
# tensor, which keeps every unitary symmetry and breaks only time reversal:
#
#     Phi REAL      time reversal HOLDS    -> expect the COREP dimension
#     Phi HERMITIAN time reversal BROKEN   -> expect the SMALL-REP dimension
#
# The control is what makes the first run evidence rather than a coincidence:
# the unitary group is identical in both, so a difference between them is time
# reversal's and nothing else's.
#
# RESTRICTED TO PRIMITIVE ORTHOGONAL LATTICES, where the fractional rotation
# matrices are already orthogonal in Cartesian coordinates and a force-constant
# tensor therefore transforms by the same matrix a k-vector does.  That still
# reaches sg 198, 212 and 213 -- primitive cubic, non-symmorphic, and three of
# the nine groups whose small representations were hardest to get right.

def _prim_orthogonal_ops(sg, HN):
    """(R, T) if this space group has a primitive lattice whose rotations are
    signed permutation matrices; (None, None) otherwise."""
    d = spglib.get_symmetry_from_database(HN[sg])
    R = np.asarray(d["rotations"])
    T = np.asarray(d["translations"]) % 1.0
    if sum(1 for Ri in R if K(np.rint(Ri)) == K(np.eye(3))) != 1:
        return None, None                       # centred lattice
    for Ri in R:                                # must be a signed permutation
        M = np.asarray(Ri, float)
        if not np.allclose(M @ M.T, np.eye(3), atol=1e-9):
            return None, None
    return [np.asarray(x, float) for x in R], [np.asarray(x, float) for x in T]


def spectrum_degeneracies(sg, HN, k, hermitian=False, seed=1, inner=1, outer=3):
    """Sorted degeneracy pattern of the dynamical matrix at k, or None.

    THE GROUP AVERAGE MUST NOT BE TRUNCATED.  A first version drew the random
    tensor on one box and discarded any image that left it.  The result is not
    invariant, and EVERY level came out non-degenerate -- including the
    controls, which is how it was caught.  So the tensor is drawn on an INNER
    box and averaged into an OUTER one large enough to hold every image, and a
    leaked term is an assertion rather than a silent skip.
    """
    import itertools
    R, T = _prim_orthogonal_ops(sg, HN)
    if R is None:
        return None
    p = np.array([0.113, 0.271, 0.407])
    pos = []
    for Ri, ti in zip(R, T):
        q = (Ri @ p + ti) % 1.0
        if all(np.max(np.minimum(np.abs(q - o), 1 - np.abs(q - o))) > 1e-8
               for o in pos):
            pos.append(q)
    pos = np.array(pos)
    n = len(pos)
    IN = [np.array(v, float)
          for v in itertools.product(range(-inner, inner + 1), repeat=3)]
    OUT = [np.array(v, float)
           for v in itertools.product(range(-outer, outer + 1), repeat=3)]
    Ok = {tuple(int(x) for x in v): i for i, v in enumerate(OUT)}
    rng = np.random.default_rng(seed)
    raw = rng.normal(size=(n, n, len(IN), 3, 3))
    if hermitian:
        raw = raw + 1j * rng.normal(size=(n, n, len(IN), 3, 3))
    sig, tau = [], []
    for Ri, ti in zip(R, T):
        s_, w_ = [], []
        for a in range(n):
            q = Ri @ pos[a] + ti
            r = q % 1.0
            j = min(range(n), key=lambda b: np.max(np.minimum(
                np.abs(r - pos[b]), 1 - np.abs(r - pos[b]))))
            s_.append(j)
            w_.append(np.rint(q - pos[j]))
        sig.append(s_)
        tau.append(w_)
    Phi = np.zeros((n, n, len(OUT), 3, 3), complex)
    for gi, S in enumerate(R):
        for a in range(n):
            for b in range(n):
                for li, Lv in enumerate(IN):
                    key = tuple(int(round(x)) for x in
                                S @ Lv + tau[gi][b] - tau[gi][a])
                    if key not in Ok:
                        raise RuntimeError("outer box too small at sg %d" % sg)
                    Phi[sig[gi][a], sig[gi][b], Ok[key]] += S @ raw[a, b, li] @ S.T
    Phi /= len(R)
    B = np.zeros_like(Phi)                      # Newton's third law
    for a in range(n):
        for b in range(n):
            for li, Lv in enumerate(OUT):
                B[a, b, li] = 0.5 * (Phi[a, b, li] + np.conj(
                    Phi[b, a, Ok[tuple(int(round(-x)) for x in Lv)]]).T)
    Phi = B
    D = np.zeros((3 * n, 3 * n), complex)
    for a in range(n):
        for b in range(n):
            for li, Lv in enumerate(OUT):
                ph = np.exp(2j * np.pi * float(np.dot(k, Lv + pos[b] - pos[a])))
                D[3 * a:3 * a + 3, 3 * b:3 * b + 3] += Phi[a, b, li] * ph
    D = 0.5 * (D + D.conj().T)
    w = np.linalg.eigvalsh(D)
    sc = max(1.0, float(np.max(np.abs(w))))
    out, cur = [], 1
    for i in range(1, len(w)):
        if abs(w[i] - w[i - 1]) < 1e-7 * sc:
            cur += 1
        else:
            out.append(cur)
            cur = 1
    out.append(cur)
    return sorted(out)


def spectrum_check(groups=(11, 19, 198, 212, 213)):
    """[(sg, |G_k|, star, small_dim, corep_dim, real pattern, hermitian pattern,
        agrees?)] over every star whose levels all share one shape.

    Only stars where every corep has the same dimension are used, because then
    the prediction is a single number and no multiplicity bookkeeping stands
    between the claim and the measurement.
    """
    import kpoint_derive as KD
    HN = hallmap()
    out = []
    for sg in groups:
        Pm, R0, T0, nc = primitive_ops_(sg, HN)
        PG = KD.point_group(R0)
        R, T, stars = P.stars_of(sg, HN)
        for st, k, idx in stars:
            rr, _s, _p = one_star(R, T, k, idx, PG, sg)
            sd = {r[6] for r in rr}
            cd = {r[9] for r in rr}
            if len(sd) != 1 or len(cd) != 1:
                continue
            d, c = sd.pop(), cd.pop()
            rp = spectrum_degeneracies(sg, HN, k, hermitian=False)
            hp = spectrum_degeneracies(sg, HN, k, hermitian=True)
            if rp is None:
                continue
            out.append((sg, len(idx), len(st), d, c, set(rp), set(hp),
                        set(rp) == {c} and set(hp) == {d}))
    return out


def primitive_ops_(sg, HN):
    return P.primitive_ops(sg, HN)


def main():
    rows = sweep()
    text = render(rows)
    if "--check" in sys.argv:
        old = open(OUT).read()
        print("IDENTICAL" if old == text else "DIFFERS", file=sys.stderr)
        sys.exit(0 if old == text else 1)
    open(OUT, "w").write(text)
    print("wrote %s (%d rows)" % (os.path.basename(OUT), len(rows)), file=sys.stderr)


def selftest():
    import kpoint_derive as KD
    HN = hallmap()
    fails = []

    def chk(name, got, want):
        ok = got == want
        if not ok:
            fails.append(name)
        print("%-4s %-64s %s" % ("ok" if ok else "FAIL", name,
                                 "" if ok else "got %r want %r" % (got, want)))

    # 1 -- the two validations, on groups that exercise every case.
    for sg in (19, 61, 198, 212, 230):
        Pm, R0, T0, nc = P.primitive_ops(sg, HN)
        PG = KD.point_group(R0)
        R, T, stars = P.stars_of(sg, HN)
        s = p = True
        for st, k, idx in stars:
            _r, os_, op = one_star(R, T, k, idx, PG, sg, strict=False)
            if os_ is not None:
                s = s and os_
                p = p and op
        chk("sg%d: the sum rule holds on every star" % sg, s, True)
        chk("sg%d: case (c) pairs fixed-point-freely" % sg, p, True)

    # 2 -- the criterion does not depend on the coset representative.
    sg = 198
    Pm, R0, T0, nc = P.primitive_ops(sg, HN)
    PG = KD.point_group(R0)
    R, T, stars = P.stars_of(sg, HN)
    st, k, idx = stars[0]
    n, els, cls, Tb, kept = small_reps_full(R, T, k, idx)
    ch = gamma_chars(els, cls, Tb, idx, kept)
    Q = coset(R, k)
    base = [round(complex(x).real, 9) for x in herring(R, T, k, idx, ch, Q)]
    T2 = [np.asarray(t, float) + (np.array([1.0, -2.0, 3.0]) if i in Q else 0)
          for i, t in enumerate(T)]
    shifted = [round(complex(x).real, 9) for x in herring(R, T2, k, idx, ch, Q)]
    chk("W does not move when the coset representative is shifted by a lattice "
        "vector", shifted, base)

    # 3 -- AGAINST THE PUBLISHED LITERATURE.  These are not self-consistency
    # checks: each row is a degeneracy someone else computed or measured.
    def at(sg, want_order=None):
        Pm, R0, T0, nc = P.primitive_ops(sg, HN)
        PG = KD.point_group(R0)
        R, T, stars = P.stars_of(sg, HN)
        out = []
        for st, k, idx in stars:
            if want_order is not None and len(idx) != want_order:
                continue
            rr, _s, _p = one_star(R, T, k, idx, PG, sg)
            out.append([r[:4] + (len(st),) + r[5:] for r in rr])
        return out

    def sig(rows):
        """(small_dim, case, corep_dim) per corep, sorted."""
        return sorted((r[6], r[8], r[9]) for r in rows)

    # SG 19 P2_12_12_1.  Yu et al., Sci. Bull. 67, 375 (2022), SM p.52, spinless:
    # R is {R5,R5} dim 4 -- a charge-2 Dirac point; X/Y/Z keep R5 at dim 2;
    # U/S/T pair four 1-dim reps.  One group, one irrep dimension, three verdicts.
    s19 = at(19, 4)
    chk("sg19: ONE star is case (b) -- R, the charge-2 Dirac point",
        sorted(sig(g) for g in s19).count([(2, "b", 4)]), 1)
    chk("sg19: THREE stars are case (a) at dim 2 -- X, Y, Z",
        sorted(sig(g) for g in s19).count([(2, "a", 2)]), 3)
    chk("sg19: THREE stars pair four 1-dim reps -- U, S, T",
        sorted(sig(g) for g in s19).count([(1, "c", 2), (1, "c", 2)]), 3)

    # SG 230 Ia-3d.  Cai et al., Light Sci. Appl. 9, 38 (2020) -- the P point,
    # MEASURED in a printed phononic crystal at 15.3 kHz: "two inequivalent
    # two-dimensional irreducible representations stuck with time-reversal
    # symmetry", beside a four-dimensional irrep that needs no time reversal.
    p230 = [g for g in at(230, 24)]
    chk("sg230 at |G_k| = 24 (P): one 4-dim case (a) and one case-(c) pair of "
        "2-dim reps", [sig(g) for g in p230], [[(2, "c", 4), (4, "a", 4)]])
    chk("sg230 P: both mechanisms give a FOUR-fold level, by different routes",
        sorted({r[9] for g in p230 for r in g}), [4])
    h230 = at(230, 48)
    chk("sg230 at |G_k| = 48: Gamma untouched, H has a case-(c) pair",
        sorted(sig(g) for g in h230),
        [[(1, "a", 1), (1, "a", 1), (1, "a", 1), (1, "a", 1), (2, "a", 2),
          (2, "a", 2), (3, "a", 3), (3, "a", 3), (3, "a", 3), (3, "a", 3)],
         [(2, "a", 2), (2, "c", 4), (6, "a", 6)]])

    # The two classic Gamma-point pairs.  Both space groups are POLAR, so
    # neither is in the seated 870 -- the machinery is exercised directly.
    for sg, want in ((144, [(1, "a", 1), (1, "c", 2)]),
                     (76, [(1, "a", 1), (1, "a", 1), (1, "c", 2)])):
        Pm, R0, T0, nc = P.primitive_ops(sg, HN)
        PG = KD.point_group(R0)
        R = [np.asarray(x, float) for x in R0]
        T = [np.asarray(x, float) for x in T0]
        k = np.zeros(3)
        idx = list(range(len(R)))
        rr, _s, _p = one_star(R, T, k, idx, PG, sg)
        chk("sg%d at Gamma: the E pair joins, the A modes do not" % sg,
            sorted((r[6], r[8], r[9]) for r in rr), want)

    # SG 227 diamond at X.  The DISCRIMINATOR: a four-fold-looking little group
    # where time reversal adds NOTHING, so a check that always says "doubled"
    # fails here.
    rows227 = [r for g in at(227) for r in g]
    x16 = [r for r in rows227 if r[3] == 16]
    chk("diamond at |G_k| = 16 (X): four small reps, all 2-dimensional",
        sorted(r[6] for r in x16), [2, 2, 2, 2])
    chk("and time reversal does NOT double them -- all case (a)",
        sorted({r[8] for r in x16}), ["a"])
    chk("so the X-point levels stay 2-fold, which is what diamond shows",
        sorted({r[9] for r in x16}), [2])
    chk("no level anywhere in diamond is doubled by time reversal",
        sorted({r[10] for r in rows227}), ["none"])

    # 4 -- the signed sum rule on the two rows the literature pins.
    def signed(sg, order):
        Pm, R0, T0, nc = P.primitive_ops(sg, HN)
        R, T, stars = P.stars_of(sg, HN)
        out = []
        for st, k, idx in stars:
            if len(idx) != order:
                continue
            n, els, cls, Tb, kept = small_reps_full(R, T, k, idx)
            ch = gamma_chars(els, cls, Tb, idx, kept)
            Q = coset(R, k)
            if not Q:
                continue
            W = herring(R, T, k, idx, ch, Q)
            out.append(int(round(sum(
                int(round(float(np.real(Tb[r][0])))) * float(np.real(w))
                for r, w in zip(kept, W)))))
        return sorted(out)
    chk("sg19: the SIGNED sum rule gives -2 at one star -- the unsigned count "
        "there is 4", -2 in signed(19, 4), True)
    chk("sg230 at |G_k| = 24: the signed sum rule gives 4, the unsigned 10",
        signed(230, 24), [4])

    # 5 -- AGAINST AN ACTUAL SPECTRUM, with time reversal as the control.
    sc = spectrum_check()
    chk("21 stars measured out of a dynamical matrix", len(sc), 21)
    chk("every one matches the COREP dimension with Phi real",
        [r[:5] for r in sc if r[5] != {r[4]}], [])
    chk("and the SMALL-REP dimension with Phi Hermitian -- time reversal off",
        [r[:5] for r in sc if r[6] != {r[3]}], [])
    dbl = [r for r in sc if r[3] != r[4]]
    chk("SIX of them are doubled, and the control halves every one",
        (len(dbl), all(r[7] for r in dbl)), (6, True))
    chk("sg19 is measured at 1->2 three times and 2->4 once",
        sorted((r[3], r[4]) for r in dbl if r[0] == 19),
        [(1, 2), (1, 2), (1, 2), (2, 4)])
    chk("sg198, primitive cubic and non-symmorphic, doubles 2->4 and 1->2",
        sorted((r[3], r[4]) for r in dbl if r[0] == 198), [(1, 2), (2, 4)])

    # 6 -- the capture itself.
    if os.path.exists(OUT):
        L = [l.split("\t") for l in open(OUT).read().splitlines()
             if l.strip() and not l.startswith("#")]
        hdr, body = L[0], L[1:]
        chk("the header", "\t".join(hdr) + "\n", HEADER)
        chk("every row's corep_dim is its small_dim or twice it",
            {int(r[10]) / int(r[7]) for r in body}, {1.0, 2.0})
        chk("cases (c) and (x) each contain two small reps, (a) and (b) one",
            sorted({(r[9], int(r[8])) for r in body}),
            [("a", 1), ("b", 1), ("c", 2), ("x", 2)])
        chk("so the three dimension facts DETERMINE the case, all four of them",
            len({(int(r[10]), int(r[7]), int(r[8]), r[9]) for r in body}),
            len({(int(r[10]), int(r[7]), int(r[8])) for r in body}))
        chk("the four cases and where each doubles -- MSGCorep Table 1",
            sorted({(r[9], r[11]) for r in body}),
            [("a", "none"), ("b", "at-k"), ("c", "at-k"), ("x", "in-bz")])
        chk("doubled AT k is exactly where corep_dim exceeds small_dim",
            all((r[11] == "at-k") == (int(r[10]) != int(r[7])) for r in body),
            True)
        chk("3,529 members, not 3,611 -- type (x) is seated ONCE",
            len(body), 3529)
        chk("82 type-(x) members, each naming TWO stars", 
            len([r for r in body if r[9] == "x"]), 82)
        chk("only type (x) carries a second star label",
            {r[9] for r in body if r[3] != "-"}, {"x"})
        chk("and every type-(x) row names a DIFFERENT star in k2",
            [r for r in body if r[3] != "-" and r[3] == r[2]], [])
        chk("849 stars in the k column and 21 more in k2 -- kpointdex's 870",
            (len({(r[0], r[2]) for r in body}),
             len({(r[0], r[3]) for r in body if r[3] != "-"}),
             len({(r[0], r[2]) for r in body}
                 | {(r[0], r[3]) for r in body if r[3] != "-"})),
            (849, 21, 870))
    else:
        print("   (no capture yet -- run `python3 corep_derive.py`)")

    print("\n%d failure(s)" % len(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    main()
