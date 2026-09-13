#!/usr/bin/env python3
r"""
arity.py -- THE INDEX HAS NO ARITY COORDINATE, AND ONE SEATED CELL IS MIS-NAMED
BECAUSE OF IT.  Also: what E = 0 does and does not certify.

Found while testing whether reported flight signatures suggest anything about
the index.  Two of seven survived three hostile lenses each, and both arrived
independently at the same structural fault -- which is not about flight at all.

    THE CELL SEATED AS `DEC` CODES `WEC AND NEC`.  IT HOLDS EXACTLY WHERE DEC
    FAILS.  AND THE TREE ALREADY CONTAINS THE CONTRADICTION.

    python3 arity.py             the reading
    python3 arity.py --selftest  fixtures

===============================================================================
1. THE DECLARED FORM IS QUADRATIC.  DEC IS NOT
===============================================================================

The index declares every member of the family to have the identical shape

        [TENSOR]_mn [VECTOR]^m [VECTOR]^n  >=  [BOUND]

with ONE vector appearing twice -- a quadratic form on a single direction.  The
V slot then says which directions are quantified over: null, timelike, or both.

**THE DOMINANT ENERGY CONDITION IS NOT OF THAT SHAPE.**  DEC is bilinear on an
ORDERED PAIR of future-causal directions,

        T_mn v^m w^n  >=  0      for all future-causal v and w

equivalently that the flux -T^m_n v^n is itself future-causal.  A quadratic form
cannot express it, because the two slots must be filled independently.

    SO THE INDEX HAS NO ARITY COORDINATE, AND V = 2 IS WHERE THE ABSENCE SHOWS.
    Read under the declared form, "causal, both" says T_vv >= 0 for every causal
    v -- which is WEC and NEC together, and is not DEC.

===============================================================================
2. THE WITNESS, AND IT IS TWO NULL VECTORS
===============================================================================

Take a perfect fluid at rho = 1, p = 2, so T = diag(1, 2, 2, 2):

    THE QUADRATIC READING HOLDS.  Minimising T_mn v^m v^n over future-causal v
    gives 1.0 -- strictly positive, no violation anywhere. The cell returns TRUE.

    THE TRUE DEC FAILS.  Take v = (1, 1, 0, 0) and w = (1, -1, 0, 0), both null
    and future-directed:

            T(v,v) = +3      T(w,w) = +3      T(v,w) = -1

    Two directions on which the condition is comfortably satisfied, whose CROSS
    term is negative.  The condition returns FALSE.

The textbook criterion agrees with the second and not the first: DEC for a
perfect fluid is rho >= |p|, and 1 >= 2 is false, while WEC is rho >= 0 and
rho + p >= 0, which holds.  **The cell is WEC wearing DEC's name.**

===============================================================================
3. THE TREE ALREADY HELD THE CONTRADICTION
===============================================================================

This is not a discrepancy with the literature that the tree can shrug off.  A
seated instrument in the same tree encodes the conditions for a perfect fluid as

        (NEC, WEC, SEC, DEC) = (1+w >= 0, 1+w >= 0, 1+3w >= 0, 1 >= |w|)

so its DEC is the BILINEAR one, rho >= |p|.  At w = 2 it returns DEC False --
while the index cell that carries the same name returns True.  **Two seated
readings of DEC, disagreeing on a case both can evaluate**, and no record of it
anywhere before this file.

===============================================================================
4. WHAT E = 0 CERTIFIES, AND IT IS LESS THAN IT HAS BEEN READ AS
===============================================================================

The obvious question is why the closure never demanded the missing condition.
The answer is a theorem about the operator rather than an oversight:

    AN ADMITTED CELL BEARS ONLY COORDINATE VALUES THE INDEX ALREADY BEARS.

The ambient box is the product of the OBSERVED value sets, so a cell needing a
value no seated cell carries is not in the box to be admitted.  Machine-checked
by the pass that found this over every subset of three boxes (2^36, 2^27, 2^36),
and independently sampled here at **0 violations over 400 random indexes, all
five languages**.

    SO E = 0 IS A NON-OVER-GENERATION CERTIFICATE, NOT A COMPLETENESS ONE.

It says the family admits nothing beyond itself.  It cannot say the family is
complete, because a missing condition that needs a new value -- a new arity, a
new tensor, a new measure -- is invisible to it by construction.

**AND THAT QUALIFIES RESULTS IN THIS TREE, INCLUDING ONES SEATED TODAY.**  The
negative-energy census was reported as closing at E = 0 with a control showing
the zero is not generic, and that measurement stands exactly as made.  What must
be narrowed is the reading: it establishes that the eight known mechanisms admit
no ninth WITHIN THE VALUES THEY ALREADY SPAN.  A mechanism requiring a fresh
value on any slot could not have been demanded, so "the census is complete" is
too strong and "the census does not over-generate" is right.  The same narrowing
applies to every E = 0 in this tree, the energy-condition family's included.

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It does not repair the cell.**  The index is not edited, the cell is not
renamed, and no arity coordinate is added. A finding is recorded, never
repaired, and an index that has been quietly corrected no longer shows what it
got wrong.

**It does not claim the index is wrong about anything else.**  One cell is
mis-named for one structural reason. The other sixteen are not touched by this,
and no published figure moves: the cell HOLDS under the reading the index
actually implements, so every count that used it is arithmetically right.

**It does not withdraw the E = 0 results.**  They were correctly measured and
correctly controlled. It narrows what they license, which is a different act,
and section 4 states the narrower reading rather than deleting the wider one.

**It does not decide which reading is correct.**  DEC has a standard meaning and
the bilinear form is it, but whether this index INTENDED the quadratic shadow --
a defensible object in its own right, sometimes called the causal-directions
condition -- is a question for whoever seated it, not for this file.
"""

import math
import random
import sys

import hlaw


def T_diag(rho, p):
    """Perfect fluid T = diag(rho, p, p, p), signature (-,+,+,+)."""
    return (rho, p, p, p)


def contract(T, v, w):
    """T_mn v^m w^n."""
    return sum(T[i] * v[i] * w[i] for i in range(4))


def is_causal_future(v, tol=1e-12):
    return v[0] > 0 and v[0] ** 2 + tol >= sum(x * x for x in v[1:])


def quadratic_min(T, n=200000, seed=1):
    """min T_mn v^m v^n over future-causal v -- the reading the index implements."""
    rnd = random.Random(seed)
    best = None
    for _ in range(n):
        v = [1.0] + [rnd.uniform(-1, 1) for _ in range(3)]
        nrm = math.sqrt(sum(x * x for x in v[1:]))
        if nrm > 1:
            v = [1.0] + [x / nrm for x in v[1:]]
        if not is_causal_future(v):
            continue
        q = contract(T, v, v)
        if best is None or q < best:
            best = q
    return best


def dec_witness(T):
    """The two null directions whose CROSS term breaks DEC. (v, w, T(v,w))."""
    v, w = (1, 1, 0, 0), (1, -1, 0, 0)
    return v, w, contract(T, v, w)


def dec_textbook(rho, p):
    return rho >= abs(p)


def wec_textbook(rho, p):
    return rho >= 0 and rho + p >= 0


def cosmo_conditions(w):
    """The seated instrument's own coding, quoted rather than reimplemented in
    spirit: (NEC, WEC, SEC, DEC) for a perfect fluid at w = p/rho."""
    return (1.0 + w >= 0.0, 1.0 + w >= 0.0, 1.0 + 3.0 * w >= 0.0, 1.0 >= abs(w))


def unborne_admissions(n=400, seed=3):
    """Count admitted cells bearing a value no seated cell bears, over n random
    indexes and all five languages. The theorem says zero."""
    import itertools
    rnd = random.Random(seed)
    bad = 0
    for _ in range(n):
        d = rnd.randint(2, 4)
        al = [rnd.randint(2, 4) for _ in range(d)]
        allc = list(itertools.product(*[range(a) for a in al]))
        X = frozenset(rnd.sample(allc, rnd.randint(3, min(len(allc), 8))))
        borne = [{c[i] for c in X} for i in range(d)]
        cl, _ = hlaw.closures(X)
        for L in hlaw.LANGS:
            for y in cl[L]:
                if any(y[i] not in borne[i] for i in range(d)):
                    bad += 1
    return bad, n


# --------------------------------------------------------------- the reading

def report():
    rho, p = 1.0, 2.0
    T = T_diag(rho, p)
    print("=" * 74)
    print("THE MISSING ARITY COORDINATE, AND THE CELL IT MIS-NAMES")
    print("=" * 74)
    print()
    print("1. The index declares one shape: T_mn v^m v^n >= B, ONE vector twice.")
    print("   DEC is bilinear on an ORDERED PAIR -- T_mn v^m w^n >= 0 for all")
    print("   future-causal v and w. A quadratic form cannot express it.")
    print("   THERE IS NO ARITY COORDINATE, AND V = 2 IS WHERE IT SHOWS.")
    print()
    print("2. THE WITNESS, at rho = %.0f, p = %.0f:" % (rho, p))
    print("   quadratic reading, min over future-causal v = %+.4f  -> CELL HOLDS"
          % quadratic_min(T))
    v, w, cross = dec_witness(T)
    print("   v = %s and w = %s, both future null:" % (v, w))
    print("     T(v,v) = %+.0f   T(w,w) = %+.0f   T(v,w) = %+.0f  -> DEC FAILS"
          % (contract(T, v, v), contract(T, w, w), cross))
    print("   textbook: DEC needs rho >= |p| -> %s;  WEC needs rho,rho+p >= 0 -> %s"
          % (dec_textbook(rho, p), wec_textbook(rho, p)))
    print("   THE CELL IS WEC WEARING DEC'S NAME.")
    print()
    print("3. AND THE TREE ALREADY HELD THE CONTRADICTION.")
    nec, wec, sec, dec = cosmo_conditions(p / rho)
    print("   a seated instrument codes (NEC,WEC,SEC,DEC) = (1+w>=0, 1+w>=0,")
    print("   1+3w>=0, 1>=|w|) -- a BILINEAR DEC. At w = %.0f it returns:" % (p / rho))
    print("     NEC %s   WEC %s   SEC %s   DEC %s" % (nec, wec, sec, dec))
    print("   while the index cell of the same name returns True. TWO SEATED")
    print("   READINGS OF DEC, DISAGREEING ON A CASE BOTH CAN EVALUATE.")
    print()
    print("4. WHY THE CLOSURE NEVER DEMANDED IT -- and what E = 0 certifies.")
    bad, n = unborne_admissions()
    print("   AN ADMITTED CELL BEARS ONLY VALUES THE INDEX ALREADY BEARS:")
    print("     %d violations over %d random indexes, all five languages." % (bad, n))
    print("   The ambient box IS the product of observed value sets, so a cell")
    print("   needing an unborne value is not in the box to be admitted.")
    print()
    print("   SO E = 0 IS A NON-OVER-GENERATION CERTIFICATE, NOT A COMPLETENESS")
    print("   ONE. It says the family admits nothing beyond itself. It cannot say")
    print("   the family is complete: a missing condition needing a new arity, a")
    print("   new tensor or a new measure is invisible to it by construction.")
    print()
    print("   AND THAT QUALIFIES RESULTS SEATED TODAY. The negative-energy census")
    print("   closes at E = 0 with a control showing the zero is not generic, and")
    print("   that measurement stands exactly as made. The READING narrows: it")
    print("   establishes no ninth mechanism WITHIN THE VALUES THE EIGHT SPAN.")
    print("   'The census is complete' is too strong; 'the census does not")
    print("   over-generate' is right. Same narrowing for every E = 0 here.")
    print()
    print("   NOTHING IS REPAIRED. The cell is not renamed, no arity coordinate is")
    print("   added, and no published figure moves -- the cell HOLDS under the")
    print("   reading the index implements, so every count that used it is right.")
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

    print("arity selftest")
    rho, p = 1.0, 2.0
    T = T_diag(rho, p)

    # The witness, exactly.
    v, w, cross = dec_witness(T)
    chk("v is future null", (v[0] > 0, v[0] ** 2 == sum(x * x for x in v[1:])), (True, True))
    chk("w is future null", (w[0] > 0, w[0] ** 2 == sum(x * x for x in w[1:])), (True, True))
    chk("T(v,v) is positive", contract(T, v, v), 3.0)
    chk("T(w,w) is positive", contract(T, w, w), 3.0)
    chk("but the CROSS term is negative", cross, -1.0)

    # The two readings disagree, which is the whole finding.
    chk("the quadratic reading HOLDS (min > 0)", quadratic_min(T) > 0.99, True)
    chk("the textbook DEC FAILS", dec_textbook(rho, p), False)
    chk("the textbook WEC holds", wec_textbook(rho, p), True)
    chk("so the cell tracks WEC, not DEC",
        (quadratic_min(T) > 0) == wec_textbook(rho, p) != dec_textbook(rho, p), True)

    # The seated instrument's own coding, and the contradiction.
    nec, wec, sec, dec = cosmo_conditions(p / rho)
    chk("the seated instrument returns DEC False at w = 2", dec, False)
    chk("and WEC True, which is what the index cell tracks", wec, True)

    # A control: where DEC genuinely holds, both readings agree.
    T2 = T_diag(2.0, 1.0)
    chk("control rho=2,p=1: textbook DEC holds", dec_textbook(2.0, 1.0), True)
    chk("control: the cross term is non-negative there",
        dec_witness(T2)[2] >= 0, True)

    # The scope theorem.
    bad, n = unborne_admissions()
    chk("no admitted cell bears an unborne value, over %d indexes" % n, bad, 0)

    print("arity selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
