-- The limit's null dust has nonnegative energy for every polarization: the averaged R_vv is
-- 2 <P1v^2 + P1v P2v + P2v^2>, and 4 (a^2 + a b + b^2) = (2 a + b)^2 + 3 b^2 >= 0, zero only at a = b = 0.
theorem target_identity (a b : Int) : 4 * (a*a + a*b + b*b) = (2*a + b)*(2*a + b) + 3*(b*b) := by
  grind

theorem sq_nonneg' (x : Int) : 0 ≤ x * x := by
  rcases Int.le_total 0 x with h | h
  · exact Int.mul_nonneg h h
  · have : 0 ≤ -x := by omega
    have := Int.mul_nonneg this this
    simpa [Int.neg_mul_neg] using this

theorem target_nonneg (a b : Int) : 0 ≤ 4 * (a*a + a*b + b*b) := by
  rw [target_identity]
  have h1 := sq_nonneg' (2*a + b)
  have h2 := sq_nonneg' b
  omega

theorem target_zero (a b : Int) (h : a*a + a*b + b*b = 0) : a = 0 ∧ b = 0 := by
  have e := target_identity a b
  have h1 := sq_nonneg' (2*a + b)
  have h2 := sq_nonneg' b
  have hb : b * b = 0 := by omega
  have hb0 : b = 0 := by
    rcases Int.lt_trichotomy b 0 with hl | he | hg
    · have := Int.mul_pos_of_neg_of_neg hl hl; omega
    · exact he
    · have := Int.mul_pos hg hg; omega
  subst hb0
  have ha : a * a = 0 := by simpa using h
  refine ⟨?_, rfl⟩
  rcases Int.lt_trichotomy a 0 with hl | he | hg
  · have := Int.mul_pos_of_neg_of_neg hl hl; omega
  · exact he
  · have := Int.mul_pos hg hg; omega
