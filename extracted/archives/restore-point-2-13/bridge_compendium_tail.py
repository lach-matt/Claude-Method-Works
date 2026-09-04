#!/usr/bin/env python3
"""bridge_compendium_tail.py — apply the COMPENDIUM-TAIL prose recovered from
The Method 1.6.1 to this tree.

Registers 1395-1398 (Lambda_spectra's closure, rival = donor) and 1426 (the
limit correction), in the order they were made.

ONE DEVIATION FROM THE ORIGINAL, RECORDED. The original edit anchored the new
section on "## The Janet boundary, seen from the inner shell", a heading added by
register 1392 whose text has NOT been recovered. That anchor does not exist here,
so the section is inserted before "## Attributions" instead, which does. The
prose is otherwise verbatim. The Janet boundary section (R 1392), the Nilsson
narrowing (R 1393) and the C3 falsifier paragraph (R 1430) remain missing, and
the two introduces-list rows the original added alongside them are added here
without the Janet row, which has nothing to attach to.
"""
import pathlib, sys

P = pathlib.Path("/home/claude/work/COMPENDIUM-TAIL.md")
s = P.read_text(encoding="utf-8")


def sub(old, new, label):
    global s
    if old not in s:
        print(f"  ANCHOR MISSING — {label}")
        sys.exit(1)
    s = s.replace(old, new, 1)
    print(f"  applied: {label}")


SECTION = """## Λ_spectra's closure, and what the limit leaves

**The object.** The index runs to the LAST AVAILABLE SPECIES and stops. Λ is
complete at 976 because its coordinates are bounded by the physics; Λ_spectra is
infinite unless capped, and *all cappings are closed when complete*.

Indexing every subshell any atom holds, (n, ℓ, k) over the 108 observed ground
configurations: **98 cells, E = 58**. Of those 58, **47 require more electrons
than any atom has** — 6d⁷ through 6f¹⁴, needing Z beyond 108. Past the limit, not
defects. Applying the limit:

> **E = 11, and every cell is named.**

| absent | Madelung predicts at | observed |
|---|---|---|
| 3d⁴ · 3d⁹ | Cr 24 · Cu 29 | 3d⁵ · 3d¹⁰ |
| 4d³ · 4d⁶ · 4d⁹ | Nb 41 · Ru 44 · Ag 47 | 4d⁴ · 4d⁷ · 4d¹⁰ |
| 4f² · 4f⁸ | Ce 58 · Gd 64 | 4f¹ · 4f⁷ |
| 5d⁸ | Pt 78 | 5d⁹ |
| 5f¹ · 5f⁵ · 5f⁸ | Ac 89 · Np 93 · Cm 96 | 5f⁰ · 5f⁴ · 5f⁷ |

*The Madelung exceptions, recovered as closure defects rather than looked up —
E.nuclide's shape, a defect whose every missing cell can be named.*

**This work — rival = donor iff the donor is not full.** Twelve walk steps have a
subshell empty as another fills. A subshell at capacity has nowhere to put an
electron, so it is not Pauli-admissible and cannot be a rival in anyone's bracket,
including its own. An s shell holds 2 and is full when it donates:

| donor | occupancy before | binding rival |
|---|---|---|
| 4s, 5s, 6s (Cr, Cu, Nb, Ru, Pt) | **2, full** | 4p, 5p, 6p |
| 5s (Pd) | **1, partial** | 5s |
| 5d, 6d, 7p (Pr, Tb, Pa, Pu, Bk, Rf) | partial | itself |

**Holds 12 of 12, with no fitted term.** *Pd is its own control: the only s donor
that is not full, and it sits with the d and f donors. Were the rule about angular
momentum it would sit with Cr.* The anomalous steps differ from ordinary ones in
WHICH RIVALS EXIST, and that is fixed by occupancy — which ν already carries in q.
Registers 1395–1398.

## Attributions"""

sub("## Attributions", SECTION, "1395–1398 · Λ_spectra's closure and rival = donor")

sub("| **the domain prohibition** | no parameter of this work is universal, so no pooled fit across regions is admissible |",
    "| **the domain prohibition** | no parameter of this work is universal, so no pooled fit across regions is admissible |\n"
    "| **the limit** | Λ_spectra closes at the last available species; E = 11, all named |\n"
    "| **rival = donor iff not full** | the twelve anomalous steps, from Pauli alone |",
    "1395–1398 · introduces-list rows")

# ------------------------------------------------------------ 1426 ---------
sub("""Indexing every subshell any atom holds, (n, ℓ, k) over the 108 observed ground
configurations: **98 cells, E = 58**. Of those 58, **47 require more electrons
than any atom has** — 6d⁷ through 6f¹⁴, needing Z beyond 108. Past the limit, not
defects. Applying the limit:""",
    """Indexing every subshell any atom holds, (n, ℓ, k) over the observed ground
configurations: **98 cells, E = 58**. Of those 58, **38 require more electrons
than any atom has** — 6f¹ through 6f¹⁴ and beyond, needing Z past the table.
Past the limit, not defects. Applying the limit:

*Corrected at register 1426: the split was first reported as 47 / 11, using
`ground.py`'s own edge of Z = 108 as the limit while the synthesised table runs
to 118. The nine cells between — 6d⁷–6d¹⁰ and 7p²–7p⁶ — are real elements, not
absences. The eleven named exceptions below are unaffected; only the count of
beyond-limit cells was wrong.*""",
    "1426 · the limit correction, 38 / 20")

P.write_text(s, encoding="utf-8")
print(f"\nCOMPENDIUM-TAIL.md written — {len(s)} characters")
