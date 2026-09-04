#!/usr/bin/env python3
"""bridge_indices_tail.py — apply the section IX prose recovered from the
The Method 1.6.1 transcript to INDICES-TAIL.md.

Two edits in sequence, in the order they were originally made:
  (a) register 1387 — Lambda_xray added, Lambda_ladder rebuilt to twelve ladders
  (b) registers 1427-1429 (delta change 5) — Lambda_ladder CLOSES at fourteen,
      Lambda_spectra restated as closing at the limit

Every anchor is asserted before it is replaced. The script is idempotent by
assertion rather than by guesswork: run twice and the second run fails loudly
rather than double-applying.
"""
import pathlib, sys

P = pathlib.Path("/home/claude/work/INDICES-TAIL.md")
s = P.read_text(encoding="utf-8")


def sub(old, new, label):
    global s
    if old not in s:
        print(f"  ANCHOR MISSING — {label}")
        sys.exit(1)
    s = s.replace(old, new, 1)
    print(f"  applied: {label}")


# ---------------------------------------------------------------- 1387 -----
sub("Registers 1249–1357. Thirteen of the fourteen close.",
    "Registers 1249–1385. **Fifteen indexes: thirteen closed, Λ_ladder open with its\n"
    "requirement named, and Λ_xray NEW (2026-08-10).**",
    "1387 · section IX headline")

i = s.find("## Λ_ladder — the ladders themselves")
j = s.find("## The one-line summary, extended")
assert 0 < i < j
old_l = s[i:j]

new_l = """## Λ_ladder — the ladders themselves

**What it is.** The walks, on (seat, kind, Zcross). **TWELVE ladders in two
families**, E = 1. Registers 1356, 1374, 1375, 1384.

Two relations, three ladders each — **Z = Nₑ + c − 1** on Λ, and **A = Z + N** on
the nuclide chart. Only two of three are independent either side, so no ladder
varies Z alone: forbidden by arithmetic, not by lack of data.

| family | ladder | fixes | reaches | held |
|---|---|---|---|---|
| species | isoelectronic | Nₑ | valence | 11 of 11 |
| species | the walk | c | valence | 106 of 106 |
| species | ionisation | Z | subvalence | 15 of 108 |
| species | isotopic | Z, Nₑ, c | nucleus | **1 rung traced** |
| species | isotonic | N | nucleus | none — NEW |
| species | isobaric | A | nucleus | none — NEW |
| state | the Rydberg series | the species | valence | every δ held |
| state | the ℓ-ladder | species, n | valence | 62 pairs |
| state | the term ladder | species, cfg | valence | 66 pairs |
| state | the outer-j ladder | species, cfg | valence | P.jsplit |
| state | the parent-term | the species | core | 12 of 15 |
| state | the isomeric | Z, N, e⁻ | nucleus | none — NEW |

**What only it contributes.** *That a coordinate individuating the cells is a KEY,
not an axis.* At four ladders `fixes` was injective by construction — a ladder IS
named by what it holds fixed — so one cell per row, and **E = 0 was FORCED: 2% of
admissible arrangements could refuse.** At six, ionisation and isotopic both fix
Z, and the zero becomes earnable. That is the dual of A.define, where a
single-valued coordinate contributes no envelope; this is the other end of the
same degeneracy.

**Why it does not close.** Two reasons, and only the first was known. E = 1, the
defect at **(subvalence, counting, across elements)** — which is Moseley's ladder,
and which is what demanded Λ_xray. And **five cells are shared**: isoelectronic
with the walk, isotonic with isobaric, isotopic with the isomeric, the Rydberg
series with the ℓ-ladder, the term ladder with the outer-j. *Two outputs mean the
observer is still choosing which to read*, so the singleton rule blocks closure
until those five are adjudicated.

## Λ_xray — the inner shell

**What it is.** The dipole-allowed inner-shell transitions, on
(Δn, Δℓ, jtype_hole). **33 lines through the N shell → 9 cells, E = 0.**
Register 1378.

**Where it comes from.** Built with no new data. **Λ's cell IS a transition** —
source subshell into target subshell — and its constraints impose no order between
n and e, so a downward transition was already inside its alphabet; only the caps
excluded it. EM.map gives the dipole rule, T.a12 the j triangle. The six K-shell
lines emerge as the classical set unadjusted: K-L2 and K-L3 are Kα₂ and Kα₁,
K-M2 and K-M3 are Kβ₃ and Kβ₁, K-N2 and K-N3 are Kβ₂. Energies are NIST SRD 128,
Deslattes *et al.*, *Rev. Mod. Phys.* **75** (2003) 35–99.

**What only it contributes.** *That thirty-three named lines are nine transition
types.* Seventy-two of 165 three-coordinate systems reach E = 0 and **every one
collapses to exactly nine cells** — Kα, Lα and Mα are one type read at three
depths, which Siegbahn notation hides.

**And it settles what Λ_cross's silences mean.** The two close on the same shape —
differences plus one endpoint — and the cypher separates them:

| language | Λ_cross | Λ_xray |
|---|---|---|
| order | speaks | speaks, E = 0 |
| geometry | speaks | speaks |
| statistics | **silent** | **speaks** — pairwise marginals recover all 9 |
| analysis | **silent** | **speaks** — Moseley, R² = 0.998 |

*Λ_cross remains the only integer object: cells AND values fixed by arithmetic.
Λ_xray has integer cells and measured values.* Registers 1379, 1380, 1385.

"""
s = s.replace(old_l, new_l, 1)
print("  applied: 1387 · Λ_ladder rebuilt and Λ_xray added in full")

sub("| **Λ_ladder** | the isotopic direction, orthogonal and untraced |",
    "| **Λ_ladder** | that a coordinate individuating the cells is a key, not an axis |\n"
    "| **Λ_xray** | thirty-three named lines are nine transition types |",
    "1387 · one-line summary")

# ------------------------------------------------------- 1427-1429 ---------
sub("Registers 1249–1385. **Fifteen indexes: thirteen closed, Λ_ladder open with its\n"
    "requirement named, and Λ_xray NEW (2026-08-10).**",
    "Registers 1249–1429. **Fifteen indexes: fourteen closed — Λ_ladder now among them\n"
    "— and Λ_spectra closing at the limit with eleven named cells.**",
    "1427 · section IX headline")

sub("""**What it is.** The walks, on (seat, kind, Zcross). **TWELVE ladders in two
families**, E = 1. Registers 1356, 1374, 1375, 1384.""",
    """**What it is.** The walks, on (seat, kind, Zcross). **FOURTEEN ladders in three
families — six species, six state, two X-ray — nine cells, E = 0. IT CLOSES.**
Registers 1356, 1374, 1375, 1384, 1427.""",
    "1427 · Λ_ladder closes")

sub("""**Why it does not close.** Two reasons, and only the first was known. E = 1, the
defect at **(subvalence, counting, across elements)** — which is Moseley's ladder,
and which is what demanded Λ_xray. And **five cells are shared**: isoelectronic
with the walk, isotonic with isobaric, isotopic with the isomeric, the Rydberg
series with the ℓ-ladder, the term ladder with the outer-j. *Two outputs mean the
observer is still choosing which to read*, so the singleton rule blocks closure
until those five are adjudicated.""",
    """**IT CLOSES, and both blocking reasons are resolved.** The E = 1 defect stood at
**(subvalence, counting, across elements)** — Moseley's ladder, in a direction
ionisation does not go. That defect is what demanded Λ_xray, and Λ_xray filled it:
Moseley enters at subvalence as counting/across, the Kα doublet as coupling/within.
**Only the subvalence seat closes** — nucleus gives 1, core 2, valence 1 — and the
seat is settled from OUTSIDE the closure rather than by it, since Λ_PCA excluded
the core independently, on different coordinates, before this was computed. The
physics agrees: a Kα line is not a property of the 1s shell but a transition
*between* shells, so the seat is where the transition spans, not where the hole
sits. **Contingency: 90% of comparable nine-cell sets refuse, so the zero is
earned** (R 1427).

**And the five shared cells are four findings and one separation** (R 1428). Two
pairs are ONE OBJECT and the index is right to merge them — isotonic fixes N and
isobaric fixes A with A = Z + N; isoelectronic fixes Nₑ and the walk fixes c with
Z = Nₑ + c − 1. That is *charge is one symbol in three positions*, one level up.
Two are separated by axes already in the index but not among the three that close:
isotopic is species where the isomeric is state; the Rydberg series fixes the
species where the ℓ-ladder fixes species and n. **The fifth was the real
ambiguity** — the term ladder and the outer-j ladder — and they are five tower
stages apart, nested rather than parallel: the term ladder moves 2S, Λ₈'s own
letter, while the outer-j ladder moves 2J, which arrives only at Λ₁₃. Adding the
tower stage as a fourth axis separates that pair and only that pair, but costs
closure, E going 0 → 1. **So the stage is the discriminator, not an axis** (R 1429).""",
    "1427-1429 · the five shared cells adjudicated")

sub("""**Thirteen close. Λ_ladder does not, and its requirement is named.**
**Λ_spectra does not, and register 1341 names its cause: it lacks the principal
number, which the merged index (Z, c, n, ℓ, 2S+1) supplies.**""",
    """**Fourteen close.** Λ_xray is new and closes at nine transition types. **Λ_ladder
now closes too** — fourteen ladders, nine cells, E = 0, once the X-ray pair is
seated at subvalence (R 1427), its five shared cells resolving as four findings
and one separation (R 1428–1429).

**Λ_spectra closes at the LIMIT** — not for want of the principal number, as
register 1341 supposed. The index runs to the last available species and stops:
98 cells, E = 58, of which 38 need more electrons than any atom has. **The
remaining twenty are within the limit, and eleven of those are the Madelung
exceptions, each nameable** (R 1395, corrected at R 1426).""",
    "1427 · the closing count")

P.write_text(s, encoding="utf-8")
print(f"\nINDICES-TAIL.md written — {len(s)} characters")
