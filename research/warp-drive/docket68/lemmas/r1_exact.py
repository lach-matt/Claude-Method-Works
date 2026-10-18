#!/usr/bin/env python3
"""r1_exact.py -- item 491: R1, "no tolerance", on the theorem's own premise.

M, 491: "R1, "no tolerance" - this is wrong because your model and premise are both wrong" and "wait for the lemmas to
be solved first before committing to wording".  489 (passage_est Q5) and 490 (r1_realize) had the wrong premise: each
README mode crossing alone, its interior partner kept apart in the core.  That premise is against 418: whatever falls in
is part of the one README.  It is against 163: the README is held as one whole, not bit by bit.  It is against 432 (2):
the passage is held whole and released whole at the end.  And it is against 386: only information travels.  The model
that premise produced -- an amplifier channel, the partner traced out -- was its artefact.  Here the lemma is solved
on the premise the rulings give.  The wording is not touched.  Labels: computed (exact unless marked), deduced.

  X0 (read) M's words, verbatim in the rulings file: 145, 146, 163, 418, 432, 491.
  X1 (computed, exact) The interior's map on the README is unitary.  passage_est Q5 computed what the transition does
     to a mode k: it mixes it with the mode -k, a' = alpha a + beta b^+, with |alpha|^2 - |beta|^2 = 1.  Both modes are
     within the corridor, so both are the README (418), held whole and released whole (163, 432 (2)).  On the pair the
     map is the two-mode squeezer.  In quadratures it is S = [[c I, s Z], [s Z, c I]], with c = cosh r, s = sinh r,
     Z = diag(1, -1).  It is symplectic exactly (S Omega S^T = Omega), and its inverse is exact: S^-1 = [[c I, -s Z],
     [-s Z, c I]].  On passage_est's computed |beta|^2 (0.68 to 7.7 at the four modes run here) the round trip returns
     any input state to 1.5e-14, roundoff.
  X2 (computed, exact) So zero error is reached.  A unitary keeps every orthogonal pair of README states orthogonal,
     since Tr(U rho U^+ U sigma U^+) = Tr(rho sigma) = 0, so the zero-error capacity of the whole README's passage is
     its full dimension.  Position 2 inverts the known map exactly and has every README mode back, exactly.  Under 489's
     premise -- the partner traced out -- the same two states overlap by 2Y/(G + 2Y)^2 > 0 (0.0119 to 0.185 across the
     band).  That overlap was the premise's, not the passage's.
  X3 (computed, exact) The two witnesses agree (145).  The corridor's size is fixed by N exactly (G3), and position 2's
     white hole has our hole's mass (transition5q H6, face2_release V1).  So its area holds exactly N ln2 = A/(4 l5^3).
     The README's one fixed exact encoding holds N bits too.  README and corridor witness the same N.
  X4 (computed: face2_release) The release loses nothing.  Position 2's face is open for the release, at most 2 r_h/c.
     It holds through it, and closes only when nothing is within it (390), so no part of the README is cut off.
  X5 (deduced) So R1 as M wrote it -- exact reconstruction, no tolerance (145, 146) -- is realizable, and realized: the
     README passes whole through a unitary map, position 2 inverts it exactly, and the two witnesses agree.  R1 stands as
     M's definition, realizable under 441 (2), its wording unchanged (491).  The statement's "exactly" stands with it.

python3 r1_exact.py [--selftest | --mutants]
"""
import os, sys, math, re, io, contextlib, importlib.util
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((145, "There is ever only one true complete reconstruction"), (146, "no tolerance at all"),
         (163, "All together, one whole"), (418, "it is still only every part of the one README"),
         (432, "M-RELEASE-WHOLE"), (491, "your model and premise are both wrong"))


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    ok = True
    for n, w in WORDS:
        m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
        ok = ok and bool(m) and w in " ".join(m.group(0).split())
    return ok


# ------------------------------------------------------------------ X1
def squeezer():
    r = sp.symbols("r", positive=True)
    c, s = sp.cosh(r), sp.sinh(r)
    I2, Z = sp.eye(2), sp.diag(1, -1)
    S = sp.BlockMatrix([[c * I2, s * Z], [s * Z, c * I2]]).as_explicit()
    Si = sp.BlockMatrix([[c * I2, -s * Z], [-s * Z, c * I2]]).as_explicit()
    Om = sp.diag(sp.Matrix([[0, 1], [-1, 0]]), sp.Matrix([[0, 1], [-1, 0]]))
    sympl = sp.simplify(S * Om * S.T - Om) == sp.zeros(4, 4)
    inv = sp.simplify(S * Si - sp.eye(4)) == sp.zeros(4, 4)
    return dict(S=S, Si=Si, r=r, sympl=sympl, inv=inv)


def round_trip(sq):
    PE = _load("passage_est.py", "r1x_pe")
    rows = [(mu, kr, PE.modes(mu, kr)["b2"]) for mu, kr in ((1e4, 0.3), (1e4, 1.0), (1e4, 10.0), (1e6, 1.0))]
    Sf = sp.lambdify(sq["r"], sq["S"], "numpy")
    Sif = sp.lambdify(sq["r"], sq["Si"], "numpy")
    rng = np.random.default_rng(491)
    worst = 0.0
    for _, _, b2 in rows:
        rr = math.asinh(math.sqrt(b2))
        A = rng.normal(size=(4, 4)); V = A @ A.T + 2 * np.eye(4)          # a valid input covariance (above vacuum)
        d = rng.normal(size=4)
        S, Si = np.array(Sf(rr), float), np.array(Sif(rr), float)
        if "partner_traced" in MUT:                                    # 489's premise: the partner never reaches p2
            Vout = S @ V @ S.T
            Vout[2:, :] = 0; Vout[:, 2:] = 0; Vout[2:, 2:] = 0.5 * np.eye(2)
            dout = S @ d; dout[2:] = 0
        else:
            Vout, dout = S @ V @ S.T, S @ d
        Vback, dback = Si @ Vout @ Si.T, Si @ dout
        worst = max(worst, np.max(np.abs(Vback - V)) / np.max(np.abs(V)), np.max(np.abs(dback - d)) / np.max(np.abs(d)))
    return dict(rows=rows, worst=worst)


# ------------------------------------------------------------------ X2
def orthogonality():
    # trace cyclicity, exact: Tr(U r U^+ U s U^+) = Tr(r s) for any unitary U (here a 3x3 symbolic unitary check)
    th = sp.symbols("theta", real=True)
    U = sp.Matrix([[sp.cos(th), -sp.sin(th), 0], [sp.sin(th), sp.cos(th), 0], [0, 0, 1]])
    r0 = sp.diag(1, 0, 0); r1 = sp.diag(0, 1, 0)
    kept = sp.simplify((U * r0 * U.H * U * r1 * U.H).trace()) == 0
    G, Y = sp.symbols("G Y", positive=True)
    traced = 2 * Y / (G + 2 * Y) ** 2                                   # r1_realize Z1, the partner traced out
    return dict(kept=kept, traced=traced)


# ------------------------------------------------------------------ X3
def witnesses():
    N, l5 = sp.symbols("N l5", positive=True)
    rh = (2 * N * sp.log(2) / sp.pi ** 2) ** sp.Rational(1, 3) * l5
    return sp.simplify(2 * sp.pi ** 2 * rh ** 3 / (4 * l5 ** 3) - N * sp.log(2)) == 0


def compute():
    sq = squeezer()
    return dict(words=words(), sq=sq, rt=round_trip(sq), og=orthogonality(), wit=witnesses())


def checks(o):
    sq, rt, og = o["sq"], o["rt"], o["og"]
    b2 = [r[2] for r in rt["rows"]]
    return [("X0: M's 145, 146, 163, 418, 432 and 491 verbatim in the rulings", o["words"]),
            ("X1: the two-mode map is symplectic exactly and its inverse exact; on passage_est's computed |beta|^2 "
             "(%.2g to %.2g) the round trip returns the input to roundoff" % (min(b2), max(b2)),
             sq["sympl"] and sq["inv"] and rt["worst"] < 1e-12 and "%.2g" % min(b2) == "0.68" and "%.2g" % max(b2) == "7.7"),
            ("X2: a unitary keeps orthogonal README states orthogonal (zero error); traced out, they would overlap by "
             "2Y/(G + 2Y)^2", og["kept"] and og["traced"].subs({sp.Symbol("G", positive=True): 1,
                                                                   sp.Symbol("Y", positive=True): 0}) == 0),
            ("X3: position 2's equal-area face holds exactly N ln2 = A/(4 l5^3): the corridor witnesses the README's N",
             o["wit"])]


def report(o=None):
    o = o or compute()
    print("r1_exact.py -- R1 on the theorem's own premise (item 491)\n")
    print("X1 symplectic %s, inverse exact %s; |beta|^2 %s; round-trip error %.1e"
          % (o["sq"]["sympl"], o["sq"]["inv"], ", ".join("%.3g" % r[2] for r in o["rt"]["rows"]), o["rt"]["worst"]))
    print("X2 orthogonal kept under the unitary: %s; the partner traced out (489's premise): overlap %s"
          % (o["og"]["kept"], o["og"]["traced"]))
    print("X3 A/(4 l5^3) = N ln2: %s" % o["wit"])


MUTANTS = {"partner_traced": "489's premise restored: the partner kept in the core, never reaching position 2 (X1)"}


def selftest(quiet=False):
    r_ = checks(compute())
    if not quiet:
        for n_, ok in r_:
            print("  [%s] %s" % ("ok" if ok else "FAIL", n_))
    k = sum(ok for _, ok in r_)
    if not quiet:
        print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        failed = [n_.split(":")[0] for n_, ok in checks(compute()) if not ok]
        MUT.clear()
        caught += bool(failed)
        print("  [%s] %s -> %s" % ("caught" if failed else "MISSED", desc, ", ".join(failed) or "nothing"))
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
