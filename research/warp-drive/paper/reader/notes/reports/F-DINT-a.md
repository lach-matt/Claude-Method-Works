# F-DINT-a: fix round for R-DINT-a

I edited only chapters 00, 01, 25, 46 and 90, starting from bcb6c358. Nothing is committed. The diff is
scratch/f_dint_a/f_dint_a.diff (five files). Line numbers below are post-edit.

## Applied, in the reviewer's words

- **A1** (chapter 46):
  - 1251–1256: the new k″, s_♭ and ω_♭, and the sentence about products at order k + 3.
  - 1337–1344: the e_S display now uses ω_(k+3) of the order k + 3 + k′_(k+3) norm, under the threshold
    min(s_(k+3), s_P), in both places, with the new citation sentence.
  - 1471–1472: the new Smallness clause. Lines 1473–1477 are only rewrapped.
- **e_S check.** I re-derived the display before placing it. Write e_S = A + B, where A is the difference of D_p⃗P_5
  at h̃ + χ_−H and at h̃, and B = D_hP_5(Ψ(U))(χ_−∂_SH). Each is a fixed operator on H or on ∂_SH, plus products of
  coefficients carrying (H, h̃). Lemma ii-g-4-1 (2)–(3) at d = 3, with ‖H‖_(k+5) ≤ ω_(k+3) and ‖H‖_5 ≤ ω_♭, gives
  exactly the reviewer's form.
- **A2** 01:153–156. **A3** 25:29–35, rewrapped. **A4** 00:33–36, rewrapped.
- **Chapter 90:** B2 and B3 at 36–44, B5 at 70–73, B1 at 83–90, B6 at 172–173, B4 at 191–197 and B7 at 219–221. In
  B4 I kept the interval 4.2955 ≤ R ≤ 4.5258 on one line. Each text was checked against the result it cites; for B2,
  γ = 1/10.

## Departures

None in wording. The 71:27 half of B5 is not applied, because chapter 71 is excluded.

## A1: uses checked

- k″, s_♭, ω_♭ and e_S occur only in chapter 46.
- Chapter 71's mentions of e_S (2436, 3892, 3918, 4108 and 4265) count only the loss in U.
- prop:ec-delta-cap uses (d) only at k = 2d, through ω_(2d+3), min(s_(2d+3), s_P) and C_(2d), so it is unaffected.
- d_1 is only a symbol downstream: chapter 46 (thm:iii-k-4-3, cor:s27-rate), 47:820–830, and chapters 60–63.
- 48:240's k′_k is unchanged.
- No chapter other than 46 needs a change.

## Open issue for the coordinator (R1, not applied)

- **Why N_NM + k″ may still be too low.** The right inverse of lem:iii-k-2-3 runs thm:iii-j2-4-1 at Ψ(U), and the
  background of Ψ(U) contains χ_−h_(−S,−S⁰) (proof of lem:iii-k-2-3, "The base point"). Eq. iii-j2-4-1 carries the
  term ‖β‖_(k+d)‖F‖_d. To reach the form of eq. ii-g-2-4, ‖χ_−H‖_(k+d) must go into C_k.
- **What C_k then depends on.** C_k for k ≤ N_NM reads the data at about order N_NM + d − 2 + k′, which exceeds
  N_NM + k″ (d > 5). e_S is likewise needed beyond order k.
- **What is left unproved.** If this is right, two statements are unproved: the first Smallness sentence, which I left
  unchanged, and the reviewer's "the initial family at the orders k ≤ N_NM + 3".
- **Remedy.** The remedy stays inside chapter 46: d_1 at least the finite order at which these constants read the
  data. I added no pending marker, because lint counts one as a hit.

## Checks

- **Lint.** `python3 lint.py --chapters`: 0 hits.
- **Assembly.** `python3 assemble.py --check`: 0 problems.
- **Line rules.** Changed lines are at most 121 characters. No added line starts with a forbidden prefix.
- **Assembled widths.** On a scratch copy, one assembled line is too long, at 123 characters. It comes from 71:3164
  ("Definition 49.76"), was already there before this round, and is in chapter 71.
- **Chapter 71.** Chapter 71 changed in the working tree at 09:07. That change is not mine: another session made it.
  My diff excludes it, and the checks pass with it present.
