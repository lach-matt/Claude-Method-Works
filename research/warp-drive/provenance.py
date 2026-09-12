#!/usr/bin/env python3.12
"""provenance.py -- who found what, and what is left that is ours.

M: "Search for attributions outside for provenance."

Done, and IT COST THE SERIES ITS HEADLINE, which is the right outcome of a
provenance pass rather than a failure of one.

  THE BIG ONE.  corridor.py's central result -- that the two mouths of a
  rotating wormhole are related by a reflection that flips the angular
  momentum, so each mouth sees the opposite handedness -- IS PUBLISHED.
  Volkov, arXiv:2605.27600, states it twice and in the plainest terms:

      "+J is the angular momentum measured from the x -> +inf region, while
       -J is the angular momentum measured at x -> -inf.  The angular
       momentum therefore flips sign when seen from different asymptotic
       regions, as it should be.  Indeed, if the observer as x -> inf sees
       the wormhole spin clockwise, say, then the observer at x -> -inf will
       see it spin in the opposite direction."

  and as an equation, his (8.9):  V(-x,y) = V(x,y),  W(-x,y) = -W(x,y)
  -- "symmetric under x -> -x, UP TO A FLIP IN THE SIGN OF THE ROTATION
  FIELD".  That is corridor.py's P, in the same words, before us.

  He also settles the case corridor.py considered and rejected: his (8.10)
  records that for KERR the reflection x -> -x must be accompanied by
  M -> -M, which is why Kerr is NOT reflection-symmetric.  That is the
  candidate this project tested and discarded, discarded for his reason.

  AND HE CORRECTS TWO PAPERS THAT HAD IT BACKWARDS -- Kleihaus & Kunz (2014)
  and Chew, Kleihaus & Kunz (2016) state J is symmetric under x -> -x, and
  Volkov records that it is antisymmetric.  So the point is not only known,
  it has a correction history.  A claim of novelty here would have been
  wrong against a literature that had already argued the question out.

  WHAT SURVIVES AS OURS is narrower and worth stating exactly: not that the
  mouths are opposite, but THE IDENTIFICATION OF THAT FACT WITH THE FIBRE OF
  THE INVERSION PROBLEM -- that the two-point fibre of the even metric
  sector IS the pair of mouths, that its deck group is the mouth exchange,
  and that the missing bit of the parity theorem is therefore a MOUTH LABEL
  rather than a datum about one object.  No source found says that.  It is a
  connection between two known things, which is a smaller claim than the one
  the series was carrying, and it is the honest size.

  EVERY ROW BELOW CARRIES ITS READING STATUS.  A citation read from source
  in this session is VERIFIED; one named from memory is NAMED-NOT-READ and
  MAY NOT BE QUOTED AS IF READ.  currency.py established that discipline
  after this session produced four faults of the recalled-number shape, and
  five rows here are still NAMED-NOT-READ.

    python3.12 provenance.py            the full attribution ledger
    python3.12 provenance.py --selftest
"""

import sys

VERIFIED = "VERIFIED"           # read from source in this session
NAMED = "NAMED-NOT-READ"        # cited from memory; not quoted

# (key, reference, what it establishes, reading status)
SOURCES = [
    ("kerr63", "R. P. Kerr, Phys. Rev. Lett. 11 (1963) 237-238",
     "the rotating vacuum metric itself", VERIFIED),
    ("nj65", "E. T. Newman and A. Janis, J. Math. Phys. 6 (1965) 915-917",
     "the complex shift r -> r + i a cos(theta) taking Schwarzschild to Kerr, "
     "motivated by the spin coefficient rho = -1/(r - i a cos theta)", VERIFIED),
    ("ncc65", "E. T. Newman, R. Couch, K. Chinnapared, A. Exton, A. Prakash "
     "et al., J. Math. Phys. 6 (1965) 918-919",
     "the Kerr-Newman metric", VERIFIED),
    ("bl67", "R. H. Boyer and R. W. Lindquist, J. Math. Phys. 8 (1967) 265",
     "the coordinates every component in this series is written in", VERIFIED),
    ("carter68", "B. Carter, Phys. Rev. 174 (1968) 1559-1571",
     "mu = Q a and the gyromagnetic ratio g = 2, the Dirac value; and Kerr's "
     "two asymptotic regions r -> +/- infinity", VERIFIED),
    ("sams73", "M. M. Schiffer, R. J. Adler, J. Mark and C. Sheffield, "
     "J. Math. Phys. 14 (1973) 52-56",
     "'Kerr geometry as complexified Schwarzschild geometry' -- the complex "
     "radius read as the whole content of the spin", VERIFIED),
    ("ernst68", "F. J. Ernst, Phys. Rev. 167 (1968) 1175",
     "the potential formulation the wormhole solutions are built in", VERIFIED),
    ("an14", "T. Adamo and E. T. Newman, Scholarpedia 9(10):31791, "
     "arXiv:1410.6626",
     "review: Psi2 = -M/(r - i a cos theta)^3 + Q^2/(...) at eq. (2.28), and "
     "Carter's g = 2 with mu = Qa in section 4", VERIFIED),
    ("gv17", "G. W. Gibbons and M. S. Volkov, Phys. Rev. D 96 (2017) 024053",
     "the zero-mass limit of Kerr is a wormhole", VERIFIED),
    ("volkov26", "M. S. Volkov, arXiv:2605.27600",
     "THE MOUTH-FLIP.  Reflection-symmetric spinning ring wormholes; J is "
     "ANTISYMMETRIC under x -> -x, so the two mouths see opposite rotation; "
     "eq. (8.9) W(-x,y) = -W(x,y); eq. (8.10) Kerr needs M -> -M as well; "
     "Appendix D: the reflection is possible for wormholes, not black holes",
     VERIFIED),
    ("kk14", "B. Kleihaus and J. Kunz, Phys. Rev. D 90 (2014) 121503",
     "rotating Ellis wormholes -- and states J SYMMETRIC under x -> -x, which "
     "volkov26 records as wrong", VERIFIED),
    ("ckk16", "X. Y. Chew, B. Kleihaus and J. Kunz, Phys. Rev. D 94 (2016) "
     "104031",
     "spinning Ellis wormhole geometry; carries the same sign error, "
     "corrected by volkov26", VERIFIED),
    ("sv19", "A. Simpson and M. Visser, JCAP 02 (2019) 042, arXiv:1812.07114",
     "the black bounce r^2 -> r^2 + l^2", NAMED),
    ("mfl21", "J. Mazza, E. Franzin and S. Liberati, JCAP 04 (2021) 082, "
     "arXiv:2102.01105",
     "the rotating black bounce used as corridor.py's testbed", NAMED),
    ("teo98", "E. Teo, Phys. Rev. D 58 (1998) 024014",
     "the rotating traversable wormhole ansatz", NAMED),
    ("bpt72", "J. M. Bardeen, W. H. Press and S. A. Teukolsky, "
     "Astrophys. J. 178 (1972) 347",
     "equatorial photon and ISCO radii of Kerr", NAMED),
    ("mt88", "M. S. Morris and K. S. Thorne, Am. J. Phys. 56 (1988) 395",
     "the traversable wormhole conditions", NAMED),
]

# (claim, verdict, source, note)
PRIOR = "PRIOR-ART"             # published before us; we re-derived it
OURS = "OURS"                   # no source found; ours to claim, carefully
FOLK = "ELEMENTARY"             # too standard to attribute, too small to claim
COMBO = "OURS-AS-A-CONNECTION"  # both halves known; the link is ours

ATTRIB = [
    ("H74b  g_tphi^2 = r^2(1+g_tt)^2(1/g_rr+g_tt)", FOLK, "kerr63",
     "a two-line rearrangement of the Kerr components; no source needed and "
     "none claimed"),
    ("H75b  four even, one odd under a -> -a", FOLK, "kerr63",
     "visible in the components as written; standard"),
    ("H75b  the no-go corollary: no even function gives an odd one", COMBO,
     "-", "the parity is elementary; USING it as a no-go on recovering "
     "sgn(a) is the step, and no source found states it that way"),
    ("H75d  I^3 = 27 J^2 for type D", PRIOR, "an14",
     "the Petrov type D condition; entirely standard"),
    ("H76a  Kerr is Schwarzschild at complex radius", PRIOR, "nj65",
     "Newman-Janis 1965.  sams73 makes it the title of a paper"),
    ("H76a  48 M^2/z^6 = K - (i/2)*RR", COMBO, "an14",
     "Psi2 = -M/z^3 is an14 eq. (2.28) and K, *RR from Psi2 is standard; "
     "packaging the two real invariants as ONE complex scalar equal to "
     "Schwarzschild's at complex radius is the framing, not the physics"),
    ("H76b  equatorial K equals Schwarzschild's, a-independent", COMBO,
     "an14", "an immediate corollary of Psi2 real at theta = pi/2.  No "
     "source found states it; it is also two lines, so it is claimed as an "
     "OBSERVATION rather than a result"),
    ("H76c  arg z from K and *RR, branch limit pi/6", COMBO, "an14",
     "inverting a known pair; the branch limit is ours and is small"),
    ("H76d  psi = pi/3 -/+ (2/3) arcsin(a/M)", FOLK, "bpt72",
     "the trigonometric solution of the photon-orbit cubic is standard; "
     "writing it about its achiral centre is a rearrangement"),
    ("H77a  |z|^2 = g_thetatheta", FOLK, "bl67", "one line"),
    ("H77b  conj(z(a)) = z(-a): the modulus pairs chiralities", COMBO, "-",
     "the algebra is trivial; reading it as the MECHANISM of the sign loss "
     "is the contribution and it is an interpretation, not a theorem"),
    ("H78d  mu = Q a, g = 2", PRIOR, "carter68",
     "CARTER 1968.  Verified here, not derived here, and never ours"),
    ("H78e  the signed inversion a = A_phi Sigma/(Q r sin^2)", FOLK, "ncc65",
     "a rearrangement of the Kerr-Newman potential"),
    ("H78f  Phi injective iff Q != 0 or a = 0", COMBO, "-",
     "assembled from standard parts; stating it as an iff on the charge is "
     "the step.  No source found -- and no thorough search for one either, "
     "since it is the kind of remark that lives in a textbook exercise"),
    ("H78g  the two odd channels cover the sphere", OURS, "-",
     "cos and sin have disjoint zeros: elementary arithmetic, but the "
     "PAIRING of the curvature channel with the electromagnetic one as "
     "complementary probes of the same bit is not something we found stated"),
    ("H79a  P : (r,phi) -> (-r,-phi) flips g_tphi", PRIOR, "volkov26",
     "VOLKOV eq. (8.9), and in words in his section V.  THE HEADLINE IS HIS"),
    ("H79b  the two mouths see opposite angular momentum", PRIOR, "volkov26",
     "quoted verbatim in this file's docstring.  Also the subject of his "
     "correction to kk14 and ckk16, so the literature has argued it out"),
    ("H79b  Kerr's r -> -r requires M -> -M", PRIOR, "volkov26",
     "his eq. (8.10).  corridor.py reached and rejected this candidate; the "
     "rejection was right and is his"),
    ("H79a  the index-counting proof for ANY even-in-r metric", FOLK, "-",
     "tensor transformation under a coordinate reflection; textbook.  Stated "
     "generally here because the sources state it per-solution, which is a "
     "presentation choice and not a discovery"),
    ("H79c  the two sheets of the fibre ARE the two mouths", COMBO, "-",
     "THE ONE THING THE SERIES CAN STILL CLAIM.  Both halves are known -- "
     "the fibre from the parity, the mouth flip from volkov26 -- and no "
     "source found connects them, i.e. reads the unrecoverable sign as a "
     "MOUTH LABEL and the deck group as the mouth exchange"),
    ("H79e  sgn(a_+) sgn(a_-) = -1 is the invariant", COMBO, "volkov26",
     "follows from his antisymmetry; saying that the PRODUCT is the only "
     "chart-independent chirality fact is the framing"),
    ("H79 note  the rotating black bounce", PRIOR, "mfl21",
     "a testbed, cited, NAMED-NOT-READ -- so it is used for its functional "
     "form only and no numerical claim of theirs is quoted"),
]


def status_of(key):
    for k, ref, what, st in SOURCES:
        if k == key:
            return st
    return None


BAR = "=" * 79


def report():
    print(__doc__.split("    python3.12")[0].rstrip())
    print()
    print(BAR)
    print("SOURCES")
    print(BAR)
    print()
    for k, ref, what, st in SOURCES:
        print("  [%s]  %s" % (k, ref))
        print("        %s" % what)
        print("        reading status: %s" % st)
        print()
    nv = sum(1 for s in SOURCES if s[3] == VERIFIED)
    nn = len(SOURCES) - nv
    print("  %d SOURCES: %d read from source in this session, %d NAMED AND NOT"
          % (len(SOURCES), nv, nn))
    print("  READ.  The five unread are used for functional form or for a name,")
    print("  never for a number, and none of them is quoted.")
    print()

    print(BAR)
    print("ATTRIBUTION")
    print(BAR)
    print()
    print("  %-48s %-22s %s" % ("claim", "verdict", "source"))
    print("  " + "-" * 76)
    counts = {}
    for claim, verdict, src, note in ATTRIB:
        counts[verdict] = counts.get(verdict, 0) + 1
        print("  %-48s %-22s %s" % (claim, verdict, src))
        print("  %-48s   %s" % ("", note))
    print()
    for v in (PRIOR, COMBO, OURS, FOLK):
        print("      %-22s %2d of %d" % (v, counts.get(v, 0), len(ATTRIB)))
    print()

    print(BAR)
    print("WHAT THE PASS COST, AND WHAT IT LEFT")
    print(BAR)
    print()
    print("  IT COST THE HEADLINE.  corridor.py was the strongest-sounding")
    print("  result of the series and %d of its rows are PRIOR-ART, one of them" %
          sum(1 for c, v, s, n in ATTRIB if v == PRIOR and c.startswith("H79")))
    print("  quoted here word for word from a paper that also CORRECTS TWO")
    print("  EARLIER PAPERS on the same point.  The physics was right and it")
    print("  was right in 2026 before us, and in the slow-rotation case before")
    print("  that.  A novelty claim would have been false against a literature")
    print("  that had already had the argument.")
    print()
    print("  WHAT IS LEFT IS ONE CONNECTION AND IT IS WORTH STATING SMALL:")
    print()
    print("      the two-point fibre of the even metric sector IS the pair of")
    print("      mouths; its deck group IS the mouth exchange; and the")
    print("      unrecoverable sign is therefore A MOUTH LABEL rather than a")
    print("      missing property of one object.")
    print()
    print("  Both halves are published.  The link is not, so far as this")
    print("  search reached -- AND THE SEARCH IS A FLOOR, NOT A PROOF OF")
    print("  ABSENCE.  Two queries against one database is not a literature")
    print("  review, and 'no source found' is exactly as weak as coverage.py's")
    print("  ABSENT: not reachable from here, which is not the same as not")
    print("  existing.")
    print()
    print("  AND THE ENERGY BILL IS UNTOUCHED BY EVERY ROW ABOVE.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = (got == want)
        print("  %-4s %-58s %s" % ("ok" if ok else "FAIL", label, got))
        if not ok:
            fails.append((label, got, want))

    print("provenance.py --selftest")
    print()
    chk("sources", len(SOURCES), 17)
    chk("read from source this session", sum(1 for s in SOURCES if s[3] == VERIFIED), 12)
    chk("named but not read", sum(1 for s in SOURCES if s[3] == NAMED), 5)
    chk("attribution rows", len(ATTRIB), 22)
    chk("prior art", sum(1 for a in ATTRIB if a[1] == PRIOR), 7)
    chk("ours as a connection", sum(1 for a in ATTRIB if a[1] == COMBO), 8)
    chk("ours outright", sum(1 for a in ATTRIB if a[1] == OURS), 1)
    chk("elementary", sum(1 for a in ATTRIB if a[1] == FOLK), 6)
    # the invariant a typed tally cannot give: the verdicts PARTITION the rows,
    # and every verdict is one of the four declared.  This catches a real error
    # (a mistyped or invented verdict); a count only catches transcription, and
    # transcription is the fault this session keeps committing.
    chk("the four verdicts partition every row",
        sum(sum(1 for a in ATTRIB if a[1] == v) for v in (PRIOR, COMBO, OURS, FOLK)),
        len(ATTRIB))
    chk("no row carries an undeclared verdict",
        sorted({a[1] for a in ATTRIB}), sorted([PRIOR, COMBO, OURS, FOLK]))

    chk("Carter is prior art, not ours",
        [a[1] for a in ATTRIB if a[0].startswith("H78d")], [PRIOR])
    chk("the mouth flip is prior art, not ours",
        [a[1] for a in ATTRIB if "opposite angular momentum" in a[0]], [PRIOR])
    chk("and it is attributed to Volkov",
        [a[2] for a in ATTRIB if "opposite angular momentum" in a[0]], ["volkov26"])
    chk("Newman-Janis is prior art",
        [a[1] for a in ATTRIB if "complex radius" in a[0]], [PRIOR])
    chk("the fibre-mouth link is the surviving claim",
        [a[1] for a in ATTRIB if "two sheets of the fibre" in a[0]], [COMBO])

    chk("every attribution names a real source or none",
        all(s == "-" or status_of(s) is not None for _, _, s, _ in ATTRIB), True)
    chk("Volkov was read from source", status_of("volkov26"), VERIFIED)
    chk("Adamo-Newman was read from source", status_of("an14"), VERIFIED)
    chk("Simpson-Visser was NOT read", status_of("sv19"), NAMED)
    chk("Mazza-Franzin-Liberati was NOT read", status_of("mfl21"), NAMED)
    chk("no source is both read and unread",
        len({k for k, _, _, _ in SOURCES}), len(SOURCES))

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
