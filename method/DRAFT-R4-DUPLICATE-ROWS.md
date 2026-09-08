# DRAFT — WITHDRAWN AS A FINDING. The volume states the reason in its own first line.

**NOTHING IN THIS FILE IS IN THE STORE.** The measurement below stands; **the reading I put on it
does not**, and the correction is at the top rather than in place of it, because a withdrawal that
leaves no trace is not a record.

## The correction

I reported the channel table as printing "the same channel twice" in three shapes and asked M whether
to repair it. **I had not read what a row of that table is.** Part II opens:

> **Every captured series, with its fit.** These are the measured rows of the coordinate table.

**A row is a CAPTURE, not a channel.** Two captures of one series are two rows *by construction*, and
every one of the three shapes is the table doing what it says it does:

- **Ar II's four pairs** — one series reached by two capture files, which register 815 names in those
  words. Two captures, two rows.
- **Ba III's two n-windows** — two captures covering different n. And the δ drift across the join is
  not a discrepancy either: the volume's own curve is δ(n) = δ₀ + δ₂/(n − δ₀)², so a low-n window and
  a high-n window of one series **must** give different means. +2.3061 → +2.1273 and +3.2585 →
  +3.2018 are that curve, measured.
- **Ca II, Li I and Zn I's two limits** — each capture carries the limit its own source quoted.
  Register 863 rules on this directly: *"the literature disagrees with itself here … the compendium
  should not adjudicate."* Register 6524 rules the general case: *"the n-extent differences that
  remain are the artifacts of independent captures, and **no table row changes**."*

The count is consistent with the reading: the element table sums to **exactly 596** and the volume
calls the rows *channels* throughout while its count line says *channel rows*. Nothing is
double-counted and nothing is claimed twice.

**There was a reason, it is stated, and I called a pattern an error.** No repair is proposed and none
is owed.

## What survives, and it is small

**One thing the capture reading does not explain.** In all four Ar II pairs **δ agrees to four
decimals while σ(δ) differs by a factor of 2.26–2.45** — 0.1695/0.0749, 0.1507/0.0615, 0.0663/0.0283,
0.0477/0.0203. Two independent captures of the same levels would agree in both or differ in both.
This is recorded as unexplained, **not** asserted as a fault: it may be a spread taken over a
different member set, and nothing printed says which.

## And one disagreement between two seated volumes, which does not dissolve

**Register 862 states Ca II `nd` δ = +0.6338 over n = 3–16. The Spectra Compendium's L525 prints
+0.6341** for that channel and that n-range. This is not about rows or captures. The entry's argument
— that a low-n average must exceed the published δ₀ = 0.626888 — survives either figure, so **the
claim holds and only its quoted number differs**. The direction is not explained by the limit each
was taken against: register 863 says *"Ours 95,751.88"* while L525 carries 95,751.870, and a lower
limit gives a smaller δ, not a larger one.

## The measurement, which stands

Four Ar II rows print one series under two notations (L326/L369, L327/L368, L328/L367, L331/L366),
identical in n-range, levels, interior, n\* range, δ, fits and limit. Two Ba III channels are fitted
in adjacent n-windows (L410/L419 at 5–7 and 8–22†, L415/L420 at 6–8 and 9–23). Ca II prints
95,751.870 on six rows and 95,751.880 on one; Li I 43,487.114 on three and 43,487.150 on five; Zn I
75,769.310 on two and 75,769.330 on three. `method/proofs/compendia4.py` measures all of it and
refuses to repair any of it.
