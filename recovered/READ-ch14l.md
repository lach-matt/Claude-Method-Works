# READ-ch14l — Chapter 23, second read: §23.6 – §23.9.3 (main member L6303–L6433)

Chat 96. Unit MEASURED by heading scan on `The_Method_1_6-2.md` before a line was read: §23.6 opens
L6303, §23.10 opens L6434, so the unit is **L6303–L6433, 131 lines, eleven headings** — §23.6,
§23.7, §23.8, §23.8.1, §23.8.2, §23.8.3, §23.8.4, §23.9, §23.9.1, §23.9.2, §23.9.3. Identical to
HANDOFF-48's scan; the scan was run anyway, per the standing rule.

Instruments: **r2-ch14l** (computable, 16 OK / 8 deviations, golden 12,977 B · c4803f26 · 124 lines)
and **r2-ch14m** (prose, 14 OK / 5 deviations, golden 13,398 B · fc3fee6a · 97 lines). Both import
`heading_line`, `section_span`, `has_token`, `enclosing` from r2lib by path; nothing copied. Neither
instrument uses `round()`: every printed comparison goes through `Decimal.quantize` with
ROUND_HALF_EVEN named at the call. No corrections made, no Register entry written — the chat-67 hold
stands.

---

## A — Deviations

**14l-13 · The Z = 1 self-concordance row is wrong, and contradicts its own section twelve lines
below.** §23.8.2 L6357 prints *Z = 1 | ν ≤ **406***. MEASURED: the threshold is
(√6/2)·Z·√R = **405.717**, and at ν = 406 the ratio |f‴|/2(f″)^{3/2} is **1.000698 > 1**, so
self-concordance fails there. L6361 states the crossing correctly — *crosses unity between ν = 405
and 406*. The Z = 2 row (811.433 → 811) and the Z = 6 row (2434.300 → 2,434) are floored correctly,
so the defect is the Z = 1 row alone: it rounds up where its siblings round down. Repair is a single
digit, 406 → 405.

**14l-16 · §23.8.3's reason contradicts §23.8.1's formula.** L6368: *Z²R enters T as a multiplicative
constant, a multiplicative constant is an affine map, and under an affine map the decrement cannot
change.* MEASURED at ν = 40: λ² = 45.7239 (Z = 1), 182.8955 (Z = 2), 1646.0597 (Z = 6) — the
decrement scales by Z², ×4 and ×36. This is §23.8.1's own formula λ² = (2/3)Z²R/ν² (L6345) read back.
Affine invariance of the Newton decrement is invariance under affine maps of the **domain** (ν), not
under rescaling the function's values. The cancellation §23.4 observed is real and the section is
right that it is not an accident — V = 4r³/(3r²−1) = 53.344447 at r = 40 for every Z — but the
correct reason is that V is a ratio of two quantities each homogeneous of degree 1 in Z²R, so the
constant divides out. As written, §23.8.3 asserts something §23.8.1 disproves two subsections
earlier. **This is the unit's most serious finding: not a figure, a reason.**

**14l-18 · "A twelfth" is a tenth.** §23.9.1 L6402: *A guarantee on C₆ costs a third of a guarantee
on T, and a twelfth of one on the dipole moment.* MEASURED from the section's own table: V(T)/V(C₆) =
**3.2631** (a third, correct) and V(⟨r⟩)/V(C₆) = **9.7812** — a tenth, and exactly 1/10 in the
asymptotic form (|p−1| = 10 against 1). The twelfth belongs to the **blockade radius**, the row
immediately below, at **11.7362**. Either the sentence names the wrong row or it carries the wrong
fraction.

**14l-11 · 731.5820 does not reproduce under the constant the book itself prints.** §23.8.1 L6347
gives *731.5820 against 731.5820 at ν = 10*. MEASURED with R = 109737.31568 — the only Rydberg
constant printed anywhere in the two bundles, at **17 sites** — (2/3)T = 731.5821045333…, which is
**731.5821** at four decimals (Decimal.quantize, ROUND_HALF_EVEN). The printed fourth decimal is 0
where the computation gives 1. It reproduces only if R is first truncated to 109737.3, which no
volume does. The ν = 100 figure, 7.3158, reproduces under either.

**14m-01 · The §25.6 pointer does not resolve, and no section in the volume carries the claim.**
§23.6 L6319: *It is not in the literature, and §25.6 explains why: the field abandoned the variable.*
MEASURED: §25.6 (L6991–L7116) is *The one deduction, and why it is not a prediction* — Sc VI's ⁴S°
channel — and carries **"abandoned" 0×, "variable" 0×, "literature" 0×, "field" 0×**. Nor is there a
correct target elsewhere: *abandon\** has exactly **three** main-volume sites — L1479 (§5, about
retrieval), L3435 (§12.11.3.1, about the factorisation law), and L6319 itself. Same class as chat
95's 14k-01 (§23.11 cited for a claim it does not carry) but worse: there the claim existed at
§23.15, here it exists nowhere. R3 must either author the explanation or drop the pointer; it cannot
be repaired by redirection.

**14l-07 / 14m-14 · The Figure 23.2 caption states an exclusivity the mathematics denies.** L6331:
*The pole at p = 1 is the method's only hard singularity: a linear observable has no curvature to
price.* MEASURED at x = 20, h = 1: **p = 0 gives w = 0 and e = 0**, so V = 0/0 is undefined there
too, while the asymptotic form 4x/(h|p−1|) returns a finite 80 and hides it. Second site of chat 95's
14j-04. Two things make this site the sharper one: the running prose at L6326 makes no exclusivity
claim, so the caption is stronger than the text it captions; and a caption is held to facts only.
Chapter 23's figures are otherwise sound — four of them, at L6191, L6328, L6479, L6575, numbered 1–4
sequentially.

**14l-02 · The two fractional forms are printed as equalities and are truncations.** §23.6 L6306
prints *w/T = 4(h/ν) + 8(h/ν)³* and *e/T = 3(h/ν)²*. Exact: w/T = 4u/(1−u²)² and
e/T = (3u²−u⁴)/(1−u²)², u = h/ν. On the three printed rows the shortfall is **0.0019 %** worst for
w/T and **0.4164 %** worst for e/T (ν = 20, h = 1); off them it reaches 0.4672 % and **6.5946 %** at
ν = 5. The table's own w/T and e/T columns carry the **exact** values (0.201004, not the equation's
0.201000), so the table does not witness the equalities it sits under, and the reader cannot tell
from the page that the display line is asymptotic.

**14l-03 / 14m-11 · The ratio claim holds only asymptotically, and is later claimed as an original
exact result.** L6317: *their ratio returns V = (4/3)(ν/h)*. MEASURED, the exact ratio of the two
fractional forms is **4r³/(3r²−1)** — identical to chat 95's settled exact V, confirming it
independently — which exceeds (4/3)r at every tested (ν, h): 26.688907 against 26.666667 at ν = 20,
h = 1, and a gap of 0.044593 at ν = 10. §23.8.4 L6381 then lists *the value 4ν/3* among what the book
claims as its own, without saying it is the asymptote of the book's own exact result.

**14m-10 · L6381 claims the 32/11 floor as an original result, inheriting chat 95's 14j-01 scope
defect.** MEASURED: **six** main-volume sites carry 32/11 — L6193 (§23.1), L6213 (§23.2), L6233 and
L6237 (§23.3), **L6381 (§23.8.4)**, L10245 (App C.1). 14j-01 measured that 32/11 is the floor of the
h = 1 series and not of V; §23.9.2 prints V = 2.0000 twelve lines after this sentence. This is the
site that turns the scope defect into a novelty claim, and the one R3 should repair last, after the
scope decision the docket owes.

**14l-24 · §23.9.3 prints three derived figures and none of their inputs.** The *V on T* column
reproduces **exactly** under ν = n − 1.35 with h = 1 — 11.58494, 24.89052, 51.54484 against the
printed 11.58, 24.89, 51.54 — δ = 1.35 being Na I ns; the search over δ ∈ [0, 3) at 0.01 returns
**1.35 uniquely**. Neither δ nor h nor the species is printed anywhere in the section. The *V on ν*
column reproduces from nothing at all: its scaling is n⁴ (ratios 16.2 and 16.0), which is the
Ritz-curvature model V = 2ν⁴/(3hδ₂), but **no single δ₂ fits all three rows** — 0 fits in
δ₂ ∈ [0.0001, 2] at 0.5 % tolerance, the implied value being 0.034 at n = 10 and 0.046 at n = 20.
Eighth member of the unprinted-input class.

**14m-07 · Nesterov is attributed five ways in five places.** MEASURED: L6341 *Nesterov and
Nemirovskii (1994)*, L7881 *Nesterov & Nemirovskii*, L8052 *Nesterov 1994*, L10377
*Nesterov–Nemirovskii*, L11653 *Nesterov, Y.* The year is consistent and the appendix entry is the
full one, so this is an R-ATTR consistency defect in the name form, not a factual error — with one
substantive edge: **L8052 credits Nesterov alone** for the identity λ² = f′²/f″ that §23.8.1 credits
to both authors.

**14m-13 · Two incompatible table conventions inside 131 lines.** MEASURED: **17** markdown-pipe
table lines (§23.8.2, §23.9.2, §23.9.3) against **14** space-aligned pseudo-table lines (§23.6,
§23.9.1). §23.9.1's single ranked list is split across two space-aligned blocks with the column
header repeated at L6395, so one ranked table prints as two. A consistent-formatting defect under the
compendium standard's *consistent formatting* and *visual hierarchy*; the production risk is
INFERRED, not measured — no press was run this chat.

---

## B — Verified findings

1. **14l-01** — all six printed cells of §23.6's table reproduce exactly: w/T 0.201004 / 0.100125 /
   0.201004, e/T 7.531e-3 / 1.877e-3 / 7.531e-3, and both approximation columns.
2. **14l-04** — e/T *is* exactly the relative error of linear interpolation of T across the bracket
   (chord midpoint minus true value), verified on three (ν, h). §23.6's characterisation is exact.
3. **14l-05 / 14l-05b** — §23.7's exponent algebra is sound in all four parts: both maps are
   involutions, x^p·x^(2−p) = x², x^p·x^(−p) = 1, the composition translates by 2, and the orbits are
   the two parity classes. The cost map's name is earned: 4x/(h|p−1|) is invariant under p ↦ 2−p at
   every p ∈ [−30, 30], p ≠ 1.
4. **14l-06** — p = 1 is odd; powers of ⟨r⟩ (p = 2) generate the even orbit only, so none reaches the
   pole.
5. **14l-08** — the ratio 8 holds at p = −2, −3, 2, 11 exactly. Noted: it holds **identically for
   every p with f″ ≠ 0**, so the four values are an instance, not a test.
6. **14l-09** — ½λ² is exactly the decrease in the quadratic model at a full Newton step (p = −2, 3,
   11).
7. **14l-10** — λ² = T′²/T″ = (2/3)T for T = Z²R/ν², exact at Z = 1, 2, 6 and ν = 10, 40, 100.
8. **14l-12** — §23.8.2's stated equivalence 24Z²R/ν⁵ ≤ 2·6^{3/2}(Z²R)^{3/2}/ν⁶ ⟺ ν ≤ (√6/2)Z√R
   holds at all fifteen tested (Z, ν).
9. **14l-14** — all three ratio statements reproduce: 0.0049295 → 0.0049 at ν = 2, 0.1355626 → 0.1356
   at ν = 55, and the crossing is between 405 (0.998) and 406 (1.001).
10. **14l-15** — *sevenfold margin* is the floor of the measured 1/0.1355626 = **7.377**.
11. **14l-17** — all eight V values of §23.9.1 reproduce exactly at ν = 20, h = 1 as the **exact** V:
    8.17899, 13.44420, 20.04170, 26.68891, 26.72220, 40.03333, 80.00000, 95.99055. Noted: the
    sentence introduces them with the asymptotic formula, which reproduces none of them.
12. **14l-20 / 14l-21** — all five rows of §23.9.2 reproduce in both columns; V → 2 strictly from
    above (2.0000018 at p = 300, never at or below 2 at finite p); the branches cross at
    |p−1| = 2x/h, so the asymptotic branch is 2.0513 at p = 40, exactly 2 at p = 41, 1.9512 at p = 42
    — the printed *requires p > 41* is right.
13. **14l-22 / 14l-23** — the V-on-T column reproduces exactly (see 14l-24 for the missing inputs),
    and the ratio column is internally consistent with its own two V columns to two significant
    figures (0.14 %, 0.16 %, 0.19 %).
14. **14m-02, 14m-03, 14m-03b, 14m-05, 14m-06** — five pointers resolve to the **claim**: §23.5's
    asymptotic form (L6287, form at L6280), §23.4's cancellation (L6246, L6259), §23.7's pole
    (2 sites), and 4x/(h|p−1|) as established (5 main-volume sites, first L6187 in §23.1). The
    self-description *and gave no reason* is exact: §23.4 carries no because/why/reason line.
15. **14m-04** — Prop. 23.1's floor is stated in the file's own words at L6201 (*V = w/e > 2, with
    V → 2 only*) and L6204, so §23.9.2's pointer resolves. Noted below as an incidental.
16. **14m-08** — every external anchor §23.8.4 makes reaches a reference section: Moore at App F.4.3,
    IEEE 1788 at App F.4.3, Nesterov at App D.4.1 and F.4.3.
17. **14m-09** — the deepest-channel claim holds. Every main-volume site printing ν above 55 (L6357,
    L6358, L6361) is inside §23.8.2 itself, where the number is a self-concordance bound and not a
    channel.
18. **14m-14** — Chapter 23's four figures are numbered sequentially 1–4.
19. **14m-15** — zero Register citations in the unit (capitalised and lowercase both grepped), the
    unit deriving twenty printed figures and citing the Register for none.
20. **14m-16** — zero Ruling 45/46 violations: no build, script, chat or file reference in 131 lines.
21. **14m-17** — the *C₃, geometric cross-section* label is the book's own convention, not a
    conflation: §26.1 L7129 groups *cross-section, C₃, quadrupole, diamagnetic shift* against p = 4
    and §23.13 L6573 recovers C₃ empirically at 3.999. **Recorded so R3 does not reopen it.**
22. **14m-18** — the table's seven other physics labels carry the standard Rydberg scalings and are
    mutually consistent.

---

## C — Incidentals

- **C1 — the printed 2.0000 rows hide their own margin.** §23.9.2's p = 300 and p = 10,000 rows print
  V = 2.0000 in bold against Prop. 23.1's strict V > 2. Measured, V(300) − 2 = 1.759 × 10⁻⁶, so the
  two are consistent — but the page gives the reader no sign that the bold 2.0000 is a rounding, in a
  table whose whole point is that the floor is never reached.
- **C2 — "two things" is unmarked.** §23.8 L6334 promises *the name explains two things*. Excluding
  the claiming sentence and the headings, §23.8 makes **one** explicit explanatory statement (L6370,
  the cancellation). §23.8.1's *the optimum whose distance it measures is the series limit* is the
  only candidate second, and §23.8.2 and §23.8.4 are a third and fourth movement the count does not
  cover. Defensible, not a deviation; the reader identifies the second explanation unaided.
- **C3 — two unattributed quotations in an attribution section.** §23.8.4 quotes *114% of optimal
  width* (L6375) and a full sentence about paying more for rigorous bounds (L6378–L6379) with no
  source named for either. The section's other three anchors all reach the appendix.
- **C4 — the ratio-8 result is stated as verified at four exponents when it is an identity.** 14l-08:
  8y′²/y″ ÷ λ² = 8 for every p with f″ ≠ 0. Presenting it as *verified symbolically at p = −2, −3, 2,
  11* understates it.
- **C5 — single-witness figures in this unit, seventeen:** 0.201004, 0.100125, 7.531e-3, 1.877e-3,
  26.689 (as 26.69), 8.18, 13.44, 20.04, 26.72, 40.03, 95.99, 2.39, 0.0049, 0.1356, 731.5820,
  11.58/24.89/51.54, 1.09e5/1.77e6/2.84e7. Measured cross-volume: 26.69 appears once, 95.99 once,
  0.1356 once, 731.5820 twice, 8.18 twice. Same standing R4 item as chat 95's C1 and chat 94's C6 —
  and the same distinction applies: nearly all of these are *uncorroborated* yet reproducible; only
  the V-on-ν triple is genuinely *unverifiable*.
- **C6 — §23.9 is a four-line hinge section** (L6383–L6386) whose whole content is that V is a
  property of the observable and the observable is chosen by *the person*. Noted for the reader
  audit: the volume's usual register is *the reader*.
