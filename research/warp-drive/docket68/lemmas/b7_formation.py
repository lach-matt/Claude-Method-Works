#!/usr/bin/env python3
"""b7_formation.py -- Warp Theorem lemma B7: the corridor's opening and closing between static planes (derived).

Your rulings: "likely made" (86 answer 3); "a corridor can be made under the same conditions used to make one larger"
(101 answer 1, H-MADE-AS-WIDENED); everything everywhere always entangled (100, 140); the ER = EPR restriction applies to
physical matter (122 (4)); one mouth cannot be made without the other, opening position 1 opens position 2 (136 A);
the formation is the synchronization (136 answer 7); the planes static, the throat forming as facing sides match (141).
READ: Maldacena-Susskind PDF p.17 (residue/OUTSIDE.md): "there does not seem to be any way to create a bridge between
them without preexisting bridges".

  B7a THE MAKING IS A WIDENING (DERIVED from your rulings and one READ source).  Every link is yours or READ:
        (i)   everything everywhere is always entangled (100, 140: H-UNIVERSAL-ENTANGLEMENT), so the matter at position 1
              and at position 2 is entangled;
        (ii)  for physical matter, ER = EPR applies (122 (4), "The er=epr only apply to physical matter":
              H-ER=EPR-MATTER-ONLY): entangled matter is joined by a bridge, so a bridge joins the two positions now;
        (iii) "there does not seem to be any way to create a bridge between them without preexisting bridges"
              (Maldacena-Susskind PDF p.17, READ in residue/OUTSIDE.md, re-read at source), so the corridor is not a
              new bridge;
        (iv)  "a corridor can be made under the same conditions used to make one larger" (101 answer 1): made is
              widened, and your "likely made" (86 answer 3) is that widening -- the two answers are one.
      First written as the board's reading H-BRIDGE-PREEXISTS; each step is a ruling or READ, so it is a derivation.
      What stays outside it: the bridge's five-dimensional widening as a dynamical evolution (B4d)
  B7b NO CHANGE OF TOPOLOGY, CONSISTENT AND SAFE (computed, z3, chain.py's seated encoding, imported): as a widening of
      a preexisting bridge that is never pinched (H-NO-PINCH), keyed to the cosmic beat (97, frame.py's lemma), the
      corridor is consistent with Geroch-Borde, Tipler and well-posedness as chain.py encodes them, causal safety is
      entailed, and no singularity is forced.  Controls: the same corridor made at the joining instant with no prior
      bridge is inconsistent; pinched, it is a change of topology
  B7c THE OPENING AND CLOSING ON THE PLANE are opening.py's (seated): the inflow is the README (115 (c)), position 1's
      horizon ends at the closing (115 (a)), position 2's arises when fully realized (115 (b)).  Their FIVE-dimensional
      evolution -- the bulk widening and closing in time -- is lemma B4d, and is not computed here
Imports copy/chain.py by path.  Stdlib + z3.  python3 b7_formation.py [--selftest]
"""
import contextlib
import importlib.util
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def compute():
    ch = _load(os.path.join(D68, "copy", "chain.py"), "b7_chain")
    routes = {
        "widening a preexisting bridge (101.1, H-BRIDGE-PREEXISTS)": {"Made": False, "Found": True, "Widen": True,
                                                                        "NoPinch": True},
        "CONTROL made at the instant, no prior bridge": {"Made": True, "PriorSetup": False},
        "CONTROL widened but pinched": {"Made": False, "Found": True, "Widen": True, "NoPinch": False},
    }
    res, _ = ch.z3_chain(routes)
    return {"res": res}


def report(d):
    print("b7_formation.py -- Warp Theorem lemma B7\n")
    for k, v in d["res"].items():
        print("  %-62s %s" % (k, v))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    w = d["res"]["widening a preexisting bridge (101.1, H-BRIDGE-PREEXISTS)"]
    chk("B7b: the widening of a preexisting bridge is consistent, causally safe, and forces no singularity",
        w["consistent"] and w["safety_entailed"] and not w.get("singularity_forced", True))
    chk("B7b control: made at the instant with no prior bridge is inconsistent",
        not d["res"]["CONTROL made at the instant, no prior bridge"]["consistent"])
    p = d["res"]["CONTROL widened but pinched"]
    chk("B7b control: a pinched widening is a change of topology, and inconsistent", not p["consistent"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
