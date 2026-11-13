### Tables for the resolvent bound on the band {#sec:tb2}

These tables carry the numbers used by [[prop:band-polynomial]], [[thm:band]], [[prop:band-points]] and
[[cor:band-one-derivative]]. The notation is that of [[sec:band]]: y = 1/r², z = 1 − 2y, v := 1/r = y^(1/2),
η = (1 − y)y^(3/2) = (1 − v²)v³, I = {1/4 ≤ v ≤ 5/6} = {−7/18 ≤ z ≤ 7/8}, κ = l(l + 2) and a = κ + 3/4. A "least
Bernstein coefficient" of a polynomial p on a piece [α, β] is min_k b_k in the notation of [[lem:bernstein-lower-bound]],
with n the degree of p; it is rounded down here, and every one listed is positive.

### The polynomial multipliers {#sec:tb2-polynomial-multipliers}

Each multiplier is F(z) := zψ(z), with ψ a polynomial with rational coefficients, and is used for every harmonic
l ≥ l_1. G_(l_1) is the weight polynomial of [[lem:band-weight-z]] for V = V_(a,9/4) at a = κ + 3/4, l = l_1; it is
listed by its coefficients of z⁰, z¹, … . W_0, m_0 and M_0 are the bounds asserted for min_I w, min_I φ′ and max_I φ′.

| name | l_1 | ψ(z) | W_0 | m_0 | M_0 |
|---|---|---|---|---|---|
| M5 | 5 | 1 + (11/20)z − (1/4)z² − (9/40)z³ | 0.87 | 0.0455 | 0.75 |
| M7 | 7 | 1 + (29/50)z − (33/50)z² − (11/25)z³ + (21/50)z⁴ | 1.30 | 0.031 | 0.74 |
| M11 | 11 | 1 + (8/25)z − (137/100)z² − (31/100)z³ + (19/20)z⁴ | 1.80 | 0.0210 | 0.72 |

| name | G_(l_1)(z): coefficients of z⁰, z¹, …, z⁷ |
|---|---|
| M5 | 103/20, 223/40, 4627/160, 829/32, 3469/64, −9, −2169/64 (degree 6) |
| M7 | 77/10, 1013/200, 11073/400, 8331/80, 12481/80, −3873/20, −4999/50, 43113/400 |
| M11 | 559/50, −2573/200, 13051/100, 200819/800, −9349/800, −2357/5, 4651/160, 39007/160 |

Values of F at the ends of ℝ (z = ±1) and of I (z = 7/8, −7/18), and the resulting p_∞ = max(F(1), −F(−1)) and
p_I = max(F(7/8), −F(−7/18)):

| name | F(1) | −F(−1) | F(7/8) | −F(−7/18) | p_∞ | p_I |
|---|---|---|---|---|---|---|
| M5 | 43/40 | 17/40 | 163303/163840 | 138173/466560 | 43/40 | 163303/163840 < 0.99673 |
| M7 | 9/10 | 31/50 | 1367107/1638400 | 1739381/6298560 | 9/10 | 1367107/1638400 < 0.83442 |
| M11 | 59/100 | 57/100 | 1663809/3276800 | 52049963/188956800 | 59/100 | 1663809/3276800 < 0.50776 |

### Bernstein data for the polynomial multipliers {#sec:tb2-bernstein}

For each multiplier, the six polynomials below have, on each listed piece, the least Bernstein coefficient shown. The
first three are in the variable z on [−1, 1]; the last three are in the variable v on [1/4, 5/6], obtained by
substituting z = 1 − 2v².

1. ψ(z), degree 3 or 4.
2. F_z(z) = ψ(z) + zψ′(z), degree 3 or 4.
3. G_(l_1)(z), degree 6 (M5) or 7 (M7, M11).
4. (1 − v²)v³G_(l_1)(1 − 2v²) − W_0, degree 17 (M5) or 19 (M7, M11).
5. 4(1 − v²)v³F_z(1 − 2v²) − m_0, degree 11 (M5) or 13 (M7, M11).
6. M_0 − 4(1 − v²)v³F_z(1 − 2v²), the same degree as item 5.

| name | item | pieces and least Bernstein coefficients |
|---|---|---|
| M5 | 1 | [−1, 1]: 0.424 |
| M5 | 2 | [−1, 0]: 0.0166; [0, 1]: 0.449 |
| M5 | 3 | [−1, 0]: 4.22; [0, 1]: 5.15 |
| M5 | 4 | [1/4, 4/9]: 0.0304; [4/9, 23/36]: 0.267; [23/36, 5/6]: 0.00399 |
| M5 | 5 | [1/4, 5/6]: 0.000516 |
| M5 | 6 | [1/4, 4/9]: 0.414; [4/9, 23/36]: 0.027; [23/36, 5/6]: 0.0113 |
| M7 | 1 | [−1, 1]: 0.07 |
| M7 | 2 | [−1, −1/3]: 0.0444; [−1/3, 1/3]: 0.484; [1/3, 1]: 0.466 |
| M7 | 3 | [−1, 0]: 5.27; [0, 1]: 7.7 |
| M7 | 4 | [1/4, 13/24]: 0.0575; [13/24, 5/6]: 0.025 |
| M7 | 5 | [1/4, 5/6]: 0.00128 |
| M7 | 6 | [1/4, 4/9]: 0.495; [4/9, 23/36]: 0.0376; [23/36, 5/6]: 0.00245 |
| M11 | 1 | [−1, 0]: 0.152; [0, 1]: 0.477 |
| M11 | 2 | [−1, −3/5]: 0.00696; [−3/5, −1/5]: 0.0198; [−1/5, 1/5]: 0.725; [1/5, 3/5]: 0.252; [3/5, 1]: 0.0512 |
| M11 | 3 | [−1, 0]: 11.1; [0, 1]: 9.34 |
| M11 | 4 | [1/4, 19/48]: 0.0773; [19/48, 13/24]: 2.74; [13/24, 11/16]: 0.057; [11/16, 5/6]: 0.0691 |
| M11 | 5 | [1/4, 19/48]: 0.000388; [19/48, 13/24]: 0.0116; [13/24, 11/16]: 0.254; [11/16, 5/6]: 0.199 |
| M11 | 6 | [1/4, 19/48]: 0.687; [19/48, 13/24]: 0.444; [13/24, 11/16]: 0.0191; [11/16, 5/6]: 0.00673 |

### The algebraic multipliers on the band {#sec:tb2-algebraic-rows}

For [[thm:band]], ranges (d)–(f). Each row uses F_ν = Φ(νz) of [[lem:band-algebraic-constants]] on σ ∈ [σ_a, σ_b],
for every l ≥ l_1(σ), with a_* := 4σ_a² − 2σ_a − 4/3 the lower bound for a, A_ν := 6ν⁴ + (17/2)ν³ and α := (a_* − A_ν)/ν.
"Core" is 2ν³ min(η(τ), 1375/7776) and "flank" is 2αν² min(h_ν(τ), h_ν(7/8)); w_I is at least the smaller. Lower bounds
are rounded down and upper bounds up; B♯ is the bound of [[lem:band-sharp]] at σ = σ_b with these constants.

| row | ν | [σ_a, σ_b] | a_* | A_ν | α ≥ | (7/2)ν³ | τ | core ≥ | flank ≥ |
|---|---|---|---|---|---|---|---|---|---|
| (d) | 11/4 | [14, 28] | 2264/3 | 33275/64 | 85.361 | 72.79 | 9/50 | 6.4425 | 5.5568 |
| (e) | 4 | [28, 108] | 9236/3 | 2080 | 249.66 | 224 | 27/200 | 20.661 | 20.68 |
| (f) | 6 | [108, 384] | 139316/3 | 9612 | 6137.7 | 756 | 7/200 | 74.927 | 91.889 |

| row | w_I ≥ | m′ ≥ | M′ ≤ | p_I ≤ | p_∞ ≤ | B♯(σ_b) ≤ |
|---|---|---|---|---|---|---|
| (d) | 5.5568 | 0.009107 | 2.045 | 0.92344 | 0.9398 | 10.297 |
| (e) | 20.661 | 0.0048594 | 2.9745 | 0.96153 | 0.97015 | 10.579 |
| (f) | 74.927 | 0.002303 | 4.4618 | 0.98234 | 0.9864 | 10.381 |

### Data for the sampled frequencies {#sec:tb2-points}

For [[prop:band-points]]. At each row the algebraic multiplier F_ν serves every l ≥ l_1 (a = κ + 3/4 at l = l_1 is
used exactly), and the harmonics l < l_1 are bounded by [[lem:band-barrier]] at the left end σ_- of the range; B♯ is
taken at its right end σ_+. Constants are rounded as in [[sec:tb2-algebraic-rows]].

| [σ_-, σ_+] | l_1 | ν | τ | α ≥ | w_I ≥ | m′ ≥ | M′ ≤ | p_I ≤ | p_∞ ≤ | barrier ≤ | B♯ ≤ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [12, 12] | 23 | 5/2 | 73/400 | 83.424 | 4.8284 | 0.010527 | 1.8591 | 0.90948 | 0.92848 | 3.914 | 5.990 |
| [24, 24] | 47 | 37/10 | 29/200 | 202.35 | 16.211 | 0.0055726 | 2.7514 | 0.95546 | 0.96537 | 3.827 | 4.097 |
| [48, 48] | 94 | 53/10 | 21/200 | 570.75 | 49.246 | 0.0029084 | 3.9412 | 0.97754 | 0.98267 | 1.897 | 3.022 |
| [96, 96] | 190 | 153/20 | 3/40 | 1585.1 | 151.37 | 0.0014458 | 5.6887 | 0.98903 | 0.99157 | 1.885 | 2.252 |
| [128, 128] | 253 | 177/20 | 13/200 | 2465.2 | 235.96 | 0.0010893 | 6.5811 | 0.99177 | 0.99368 | 1.257 | 2.024 |
| [160, 160] | 316 | 99/10 | 23/400 | 3495.4 | 331.94 | 0.00087484 | 7.3619 | 0.99341 | 0.99494 | 0.9422 | 1.869 |
| [192, 192] | 381 | 109/10 | 21/400 | 4607.4 | 444.45 | 0.00072418 | 8.1055 | 0.99455 | 0.99582 | 1.254 | 1.743 |
| [5119/20, 256] | 503 | 12 | 3/80 | 9575.9 | 598.53 | 0.00059921 | 8.9235 | 0.9955 | 0.99655 | 0.4244 | 1.677 |
| [6399/20, 320] | 631 | 12 | 1/40 | 21693 | 602.87 | 0.00059921 | 8.9235 | 0.9955 | 0.99655 | 0.4237 | 1.815 |
| [7679/20, 384] | 759 | 12 | 1/50 | 36541 | 604.55 | 0.00059921 | 8.9235 | 0.9955 | 0.99655 | 0.4232 | 1.963 |
