# FILL-LIMIT FROM OUTSIDE — THE TOWER HAS NO LIMIT TO TAKE; IT HAS A LAST STAGE

Computed by `fill_outside.py` over `tower-1.py`. Companion to `FILL-LIMIT-FINDING.md`, which proved the
bracket of R 333 unimprovable from INSIDE (the morphism criterion leaves L anywhere in [0, 0.4168%)).
M's question, 2026-08-29: *can we prove from outside?* Outside means what chapter 18's envelope clause
means — a law independent of the index. **Yes: one outside premise excludes L = 0, which inside admitted;
one named rung lowers the upper end by a factor of at least 3.2; what remains is a ruling, not a proof.**

## 1 · The premise, and where it comes from

An axis that lowers fill is a **measurement**: a label not determined by the coordinates already present.
This is the book's own doctrine, not physics — Theorem 11.1 (every lattice quantity is a function of the
coordinates; the escape is a further measurement, which is by definition a new coordinate), §32.1.4
(ℛ never produces a coordinate), and the four admitted operations, of which RELABEL adds none. A function
of existing coordinates adjoined as a coordinate would lower fill (multiplicity 1 against a value-count
above 1) while measuring nothing; the doctrine refuses it as an axis.

The premise from outside is then a single sentence of prior-art physics: **a bound atomic transition under
the §7.4 caps has finitely many independent labels.** Two states, each a finite-dimensional multiplet
(configuration, coupling, J), one nucleus (I), one projection each — a finite complete set (Condon &
Shortley 1935; Cowan 1981). The ladder of §12.11.1 is a walk up this set, and the set ends.

## 2 · Theorem (from outside)

Under the premise, only finitely many axes have ratio below one. Σ(1 − ratio) is a **finite sum**, the
product is a finite product of positive terms, and

    L = fill(D_last) > 0.

**L = 0 is excluded from outside, though it was admissible from inside.** The question the request posed —
does Σ(1 − ratio) diverge over axes 14, 15, … — dissolves: there is no infinite sequence to sum. Closure
could not see this because closure never gives reference: it cannot tell a measurement from a repetition
of one, and every route to L = 0 (continuation Q of the inside finding) repeats.

## 3 · The exhibit: the rung prior art names

After the outer electron's spin bit (axis 13, 2J) the physics supplies the hyperfine coupling
**F = J ⊗ I** (Casimir 1936), then the projection **M_F**. In the tower's own one-parent envelope style —
f_max not the cell's f (§12.11.1); every coupling axis hung off one side of the tree (§12.11.5) —

    axis 14   2F     max(0, 2J − 2I_max) ≤ 2F ≤ 2J + 2I_max     window on the single parent 2J
    axis 15   m_F    0 ≤ m_F ≤ 2F,  m_F = F + M_F               cap by the single parent 2F

with **2I_max a declared cap — a declaration about the world, of the kind Z = 120 is.** Both bounds are
monotone functions of one parent, hence morphisms, hence closed: *E = 0 on all six exhaustive tests
(bases Λ₈–Λ₁₀, caps I = ½ and 3/2, boxes to 5.4 million).* The exact triangle |2J − 2I| ≤ 2F ≤ 2J + 2I is a
sum bound with a parity congruence; *E = 2,515 · 11,712 · 3,970 · 19,848 · 6,565 · 30,420 on the same six* —
it does not close, exactly as E3 (sums fail) and §12.11.6 (the congruence breaks joins) say. Its density
against the envelope, 2I adjoined free, is *50.00% at I = ½ falling to 17.94% at I = 7* — inside the
17.0–67.5% range of §12.11.1's own column.

The fills, over the 2J distribution of Λ₁₃ (*27,170 · 40,755 · 38,220 · 33,150 · 25,545 · 17,940 · 10,585 ·
4,605 · 1,160 cells at 2J = 0 … 8*):

    I      vc    fill14%    ratio14   fill15%     ratio15   fill15 / fill13
    0       9   0.046311    0.1111    0.018416    0.3977    0.0442   ← 2F = 2J: a RELABEL, not an axis
    ½      10   0.119353    0.2864    0.044752    0.3750    0.1074
    1      11   0.171360    0.4111    0.062111    0.3625    0.1490
    2      13   0.233726    0.5608    0.083447    0.3570    0.2002
    4      17   0.283890    0.6811    0.107586    0.3790    0.2581
    7      23   0.318563    0.7643    0.130061    0.4083    0.3120

**Under any cap up to I = 7 — the largest ground-state spin among primordial nuclides — the two rungs take
the upper end of the bracket from 0.4168% to at most 0.1301%, and to 0.0448% at I = ½.** fill(15) is the
value of L if the ladder ends there and an upper bound on L if it does not, since every further rung lowers
fill. As I_max → ∞ the ratio of the F-rung tends to one (the translated-cap behaviour of the inside
finding's T) and fill15/fill13 tends to ½: the rung improves the bracket by a factor above two under every
cap, and above 3.2 under every physical one.

At I = 0 the rung is 2F = 2J, multiplicity one on every cell: a relabel. **The hyperfine axis exists only for
I ≥ ½ — the doctrine of §1 and the physics agree on where the rung begins.**

## 4 · What outside does not give, and why it is a ruling

- **The value of L** needs the ladder named and capped. The cap is a declaration about the world; the names
  are prior art up to the nucleus, and the count is finite whatever they are — so L > 0 does not wait on them.
- **The parent side of the cylinder.** §12.11.1 couples only the target: multiplicity, seniority, core J_c,
  K, J. Whether the parent is owed its own rungs, and whether J_c already carries the parent's J, is new
  subject-matter (the request's own words) — **M's ruling.** Each rung the ruling adds lowers fill(D_last)
  by a known factor; none can make it zero.
- **The two-parent rungs.** The selection rule on (2J, 2J′) of §12.11.6 bridges the cylinder's ends and, like
  the tight K of §12.11.5, spends the tree. Outside can name it; whether the tower carries it is a ruling.

## 5 · The verdict, split

- **Proved from outside:** L > 0; L = fill(D_last); Σ(1 − ratio) is finite. Premise: finitely many labels.
- **Computed, cap-conditional:** L ≤ fill(15)(I_max); at most 0.1301% for I ≤ 7. Instrument `fill_outside.py`.
- **Refused:** a value for L, and a lower bound on it, until the remaining rungs are ruled. A lower bound
  from inside the ruling is a finite computation, fill(13) divided by the product of the remaining
  value-counts at worst, and is not written here because the count of rungs is not yet M's.

Together with the inside finding: **the existence of the limit is the law's, its value is the world's, and
the world has now been asked the one question that was answerable without a ruling — is it finite —
and has answered yes.**

## 6 · Files

`fill_outside.py` · `FILL-OUTSIDE-RESULTS.txt` (57 lines) · `tower-1.py` · slip `02-fill-outside.md`.
