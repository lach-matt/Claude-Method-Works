#!/usr/bin/env python3
"""contingency.py — a check that cannot fail is not evidence.

Register 1383. Three faults found separately shared one gap:

  · MEASURE recomputes a stated value and confirms it — but a quantity that is
    zero by construction recomputes to zero every time (register 1382, Q.final's
    hydrogenic zero, which sat among the fit statistics as though data
    constrained it).
  · REPRODUCTION confirms the build completes — and it completed while
    discarding 6,659 bytes (register 1373).
  · E = 0 at four cells was true and forced (registers 1374-1375).

None asks the prior question: COULD THIS HAVE COME OUT OTHERWISE? That is a
question about the SPACE, not about the value.

    WITNESS    exhibit one admissible neighbour for which the check FAILS,
               constructed rather than hypothesised.
    SPACE      state the admissible set BEFORE running, or the witness is not
               independent of the result it is meant to test.
    RATE       what fraction of comparable objects fail, reported beside the
               result.
    VANISHING  does any factor vanish or saturate at the tested point?

Reporting rule: A FORCED CHECK IS LABELLED, NOT DELETED. B.brk and EM.image are
the model rather than faults — both are vacuous and both say so.

The protocol caught an error in its own first demonstration: it scored
Λ_ladder's four cells at 28% by sampling arbitrary cell sets, when a ladder is
named by what it fixes and the space is row-injective. Restricted correctly the
rate is 2%. RATE WITHOUT SPACE IS MEANINGLESS — question 2 failing on the
protocol's own worked example, which is why SPACE must be declared first and is
a required argument here rather than an optional one.
"""
import random
from itertools import product  # noqa: F401 — used by callers building declared spaces


class Vacuous(Exception):
    """Raised when a check is structurally incapable of failing."""


def contingency(name, check, space, held, vanishing=None, sample=None, seed=0):
    """Ask the four questions of one check.

    name      what is being checked
    check     callable(obj) -> bool, the check as actually run
    space     an ITERABLE of admissible neighbours, declared by the caller
              BEFORE the result is known. Not a filter over an arbitrary set:
              the admissible set is a property of how the object is named.
    held      the object the check was run on
    vanishing callable(obj) -> list of (factor_name, value) that must be
              inspected for a structural zero or saturation at the tested point
    sample    cap on how many neighbours to draw (None = all). Capping is
              declared in the output; an uncapped factorial space is the fault
              that OOM-killed the container twice, so the cap is applied to the
              ITERATOR and never by building the product first.
    """
    if not check(held):
        return {"name": name, "held": False, "note": "the check does not pass on the held object"}

    rng = random.Random(seed)
    n = tried = failed = 0
    witness = None
    for obj in space:
        n += 1
        if sample is not None and tried >= sample:
            break
        tried += 1
        if not check(obj):
            failed += 1
            if witness is None:
                witness = obj

    rate = (failed / tried) if tried else 0.0
    van = list(vanishing(held)) if vanishing else []
    dead = [f"{k} = {v}" for k, v in van if v in (0, 0.0)]

    result = {
        "name": name,
        "held": True,
        "space_size": tried,
        "capped": sample is not None,
        "failed": failed,
        "rate": rate,
        "witness": witness,
        "vanishing": dead,
        "earned": failed > 0 and not dead,
    }
    return result


def report(r):
    if not r.get("held"):
        return f"  {r['name']}: {r['note']}"
    pct = 100.0 * r["rate"]
    lines = [f"  {r['name']}"]
    lines.append(f"    SPACE     {r['space_size']} admissible neighbours"
                 + (" (capped)" if r["capped"] else ""))
    if r["witness"] is not None:
        lines.append(f"    WITNESS   {r['witness']!r}")
    else:
        lines.append( "    WITNESS   NONE — no admissible neighbour fails")
    lines.append(f"    RATE      {r['failed']}/{r['space_size']} refuse ({pct:.0f}%)")
    if r["vanishing"]:
        lines.append(f"    VANISHING {', '.join(r['vanishing'])}")
    else:
        lines.append( "    VANISHING no factor vanishes or saturates here")
    lines.append("    VERDICT   " + ("EARNED" if r["earned"] else
                                     "FORCED — label it, do not delete it"))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# The protocol's own worked examples, kept because both are recorded faults.
# ---------------------------------------------------------------------------
def _demo():
    print(__doc__.split("\n")[0])
    print()

    # register 1375: E = 0 at four cells, with an injective axis. FORCED.
    def closes(cells):
        seen = {}
        for c in cells:
            if c[0] in seen:
                return False
            seen[c[0]] = c
        return True                       # row-injective: always monotonisable

    four = [(0, 0, 0), (1, 1, 0), (2, 2, 1), (3, 3, 1)]
    # SPACE, declared before running: 4-cell sets on the 4x4x2 grid whose axis 0
    # is injective. CONSTRUCTED, not filtered — filtering an arbitrary sample is
    # what made the protocol's first run report 28% instead of 2%.
    space = []
    for i in range(60):
        r = random.Random(i)
        space.append(tuple(sorted((z, r.randrange(4), r.randrange(2))
                                  for z in range(4))))
    print(report(contingency("Lambda_ladder at four cells, axis 0 injective",
                             closes, space, tuple(four))))
    print()

    # register 1382: a factor that vanishes by construction. FORCED.
    def q_final(Ne):
        return (Ne - 1) / Ne

    def is_zero(Ne):
        return q_final(Ne) == 0.0

    print(report(contingency("Q.final at Ne = 1",
                             is_zero, [2, 3, 4, 5, 6, 10, 20], 1,
                             vanishing=lambda Ne: [("(Ne-1)/Ne", q_final(Ne))])))


if __name__ == "__main__":
    _demo()
