// matrices.h: S-RULE §3.3 -- node sets and the spectral matrices, each entry ⌊e⌋_B of an exact rational e determined
// by the (dyadic) nodes, computed with GMP integers.  The algorithms here are deliberately not the reference's
// (rule_ref.py builds Lagrange polynomials and integrates them; this file uses closed forms), so that agreement of the
// two is a check of both.
#pragma once
#include "exactfn.h"
#include <vector>

typedef std::vector<F> Vec;
struct Mat { int r = 0, c = 0; std::vector<F> a; std::vector<S> s;   // the entries and their sign-magnitude form
  const F& operator()(int i, int j) const { return a[(size_t)i * c + j]; }
  void finish() { s.resize(a.size()); for (size_t i = 0; i < a.size(); i++) s[i] = to_sm(a[i]); } };

inline Vec lobatto(int p) { Vec t(p + 1); for (int j = 0; j <= p; j++) t[j] = -chat(j, p); return t; }
inline Vec radau(int p) {
  Vec t(p + 1); for (int j = 0; j <= p; j++) t[j] = chat(2 * j, 2 * p + 1);
  std::sort(t.begin(), t.end(), [](const F& a, const F& b) { return a < b; }); return t;
}
inline Vec xnodes(int M) { Vec t(M + 1); for (int k = 0; k <= M; k++) t[k] = chat(k, M); return t; }

inline std::vector<Z> to_ints(const Vec& t) { std::vector<Z> T(t.size()); for (size_t i = 0; i < t.size(); i++) fx_to_mpz(t[i], T[i].v); return T; }

// d_j = Π_{k≠j} (T_j − T_k)
inline std::vector<Z> denoms(const std::vector<Z>& T) {
  int n = T.size(); std::vector<Z> d(n); Z df;
  for (int j = 0; j < n; j++) { mpz_set_ui(d[j].v, 1); for (int k = 0; k < n; k++) if (k != j) { mpz_sub(df.v, T[j].v, T[k].v); mpz_mul(d[j].v, d[j].v, df.v); } }
  return d;
}
// coefficients c_m of Ñ_j(T) = Π_{k≠j} (T − T_k), by synthetic division of Π_k (T − T_k) by (T − T_j)
inline std::vector<std::vector<Z>> lagrange_numerators(const std::vector<Z>& T) {
  int n = T.size(); std::vector<Z> P(n + 1); mpz_set_ui(P[0].v, 1);
  for (int k = 0; k < n; k++) {                 // P := P (T − T_k); P has degree k + 1
    for (int m = k + 1; m >= 1; m--) { mpz_set(P[m].v, P[m - 1].v); }
    mpz_set_ui(P[0].v, 0);
    // now P holds T * old; subtract T_k * old (old coefficient m is now at m + 1)
    for (int m = 0; m <= k; m++) { Z t; mpz_mul(t.v, T[k].v, P[m + 1].v); mpz_sub(P[m].v, P[m].v, t.v); }
  }
  std::vector<std::vector<Z>> out(n, std::vector<Z>(n));
  for (int j = 0; j < n; j++) {                 // b_{n-1} = a_n, b_{m-1} = a_m + T_j b_m
    mpz_set(out[j][n - 1].v, P[n].v);
    for (int m = n - 1; m >= 1; m--) { mpz_mul(out[j][m - 1].v, T[j].v, out[j][m].v); mpz_add(out[j][m - 1].v, out[j][m - 1].v, P[m].v); }
  }
  return out;
}

// D_ij = ℓ'_j(τ_i): off the diagonal (d_i/d_j) 2^B/(T_i − T_j); on it Σ_{k≠j} 2^B/(T_j − T_k), summed exactly
inline Mat Dmat(const Vec& t) {
  int n = t.size(); std::vector<Z> T = to_ints(t), d = denoms(T);
  Mat D; D.r = D.c = n; D.a.resize((size_t)n * n);
  Z num, den, df;
  for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
    if (i != j) {
      mpz_mul_2exp(num.v, d[i].v, 2 * BITS); mpz_sub(df.v, T[i].v, T[j].v); mpz_mul(den.v, df.v, d[j].v);
      mpz_fdiv_q(num.v, num.v, den.v); D.a[(size_t)i * n + j] = fx_from_mpz<6, 5>(num.v);
    } else {
      mpz_set_ui(num.v, 0); mpz_set_ui(den.v, 1);
      for (int k = 0; k < n; k++) if (k != j) {      // num/den + 1/δ = (num δ + den)/(den δ)
        mpz_sub(df.v, T[j].v, T[k].v); mpz_mul(num.v, num.v, df.v); mpz_add(num.v, num.v, den.v); mpz_mul(den.v, den.v, df.v); }
      mpz_mul_2exp(num.v, num.v, 2 * BITS); mpz_fdiv_q(num.v, num.v, den.v); D.a[(size_t)i * n + j] = fx_from_mpz<6, 5>(num.v);
    }
  }
  D.finish(); return D;
}
// Q_ij = ∫_{-1}^{τ_i} ℓ_j = 2^-B [A_j(T_i) − A_j(−2^B)] / d_j with A_j the antiderivative of Ñ_j, scaled by
// L = lcm(1..n) to integer coefficients
inline Mat Qmat(const Vec& t) {
  int n = t.size(); std::vector<Z> T = to_ints(t), d = denoms(T); auto c = lagrange_numerators(T);
  Z L(1); for (int m = 1; m <= n; m++) mpz_lcm_ui(L.v, L.v, m);
  Z lo; mpz_set_si(lo.v, -1); mpz_mul_2exp(lo.v, lo.v, BITS);      // −2^B
  Mat Q; Q.r = Q.c = n; Q.a.resize((size_t)n * n);
  Z a, s1, s2, q, den;
  for (int j = 0; j < n; j++) {
    std::vector<Z> A(n);                                             // A_m = c_m L/(m+1), coefficient of T^(m+1)
    for (int m = 0; m < n; m++) { mpz_divexact(q.v, L.v, Z(m + 1).v); mpz_mul(A[m].v, c[j][m].v, q.v); }
    auto ev = [&](mpz_srcptr x, mpz_ptr out) { mpz_set_ui(out, 0); for (int m = n - 1; m >= 0; m--) { mpz_add(out, out, A[m].v); mpz_mul(out, out, x); } };
    ev(lo.v, s2.v);
    mpz_mul(den.v, L.v, d[j].v);
    for (int i = 0; i < n; i++) { ev(T[i].v, s1.v); mpz_sub(s1.v, s1.v, s2.v); mpz_fdiv_q(s1.v, s1.v, den.v); Q.a[(size_t)i * n + j] = fx_from_mpz<6, 5>(s1.v); }
  }
  Q.finish(); return Q;
}
// On σ = (τ + 1)/2, exactly (S_j = T_j + 2^B, σ = S/2^(B+1)) [Q9]:
//   W4_ij = σ_i^-4 ∫_0^σ_i s^3 ℓ_j = Σ_m c_m S_i^m / (m + 4) / d_j,
//   V4_ij = σ_i^-4 ∫_0^σ_i (σ_i − s) s^2 ℓ_j = Σ_m c_m S_i^m / ((m + 3)(m + 4)) / d_j,
// with c_m the coefficients of Π_{k≠j} (S − S_k) and d_j = Π_{k≠j} (S_j − S_k).
inline void W4V4(const Vec& t, Mat& W4, Mat& V4) {
  int n = t.size(); std::vector<Z> T = to_ints(t);
  Z sh; mpz_set_ui(sh.v, 1); mpz_mul_2exp(sh.v, sh.v, BITS);
  for (auto& x : T) mpz_add(x.v, x.v, sh.v);
  std::vector<Z> d = denoms(T); auto c = lagrange_numerators(T);
  Z L4(1), L34(1); for (int m = 0; m < n; m++) { mpz_lcm_ui(L4.v, L4.v, m + 4); mpz_lcm_ui(L34.v, L34.v, (unsigned long)(m + 3) * (m + 4)); }
  W4.r = W4.c = V4.r = V4.c = n; W4.a.resize((size_t)n * n); V4.a.resize((size_t)n * n);
  Z q, s, den, aw;
  for (int j = 0; j < n; j++) {
    std::vector<Z> Aw(n), Av(n);
    for (int m = 0; m < n; m++) { mpz_divexact(q.v, L4.v, Z(m + 4).v); mpz_mul(Aw[m].v, c[j][m].v, q.v);
      mpz_divexact(q.v, L34.v, Z((long)(m + 3) * (m + 4)).v); mpz_mul(Av[m].v, c[j][m].v, q.v); }
    for (int i = 0; i < n; i++) {
      for (int w = 0; w < 2; w++) {
        auto& A = w ? Av : Aw; mpz_set_ui(s.v, 0);
        for (int m = n - 1; m >= 0; m--) { mpz_mul(s.v, s.v, T[i].v); mpz_add(s.v, s.v, A[m].v); }
        mpz_mul_2exp(s.v, s.v, BITS); mpz_mul(den.v, w ? L34.v : L4.v, d[j].v); mpz_fdiv_q(s.v, s.v, den.v);
        (w ? V4 : W4).a[(size_t)i * n + j] = fx_from_mpz<6, 5>(s.v);
      }
    }
  }
  W4.finish(); V4.finish();
}
// the dot-product square: entries <A_i·, A_·j>
inline Mat dotsq(const Mat& A) {
  int n = A.r; Mat R; R.r = R.c = n; R.a.resize((size_t)n * n);
  std::vector<S> col((size_t)n * n);
  for (int l = 0; l < n; l++) for (int j = 0; j < n; j++) col[(size_t)j * n + l] = A.s[(size_t)l * n + j];
  #pragma omp parallel for schedule(dynamic)
  for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) R.a[(size_t)i * n + j] = dot<6, 5>(&A.s[(size_t)i * n], 1, &col[(size_t)j * n], 1, n);
  R.finish(); return R;
}
// C_nm = ⌊(2/N) ε_n ε_m ĉ((nm mod 2N)/N)⌋_B, ε = 1/2 at the two ends
inline Mat dctmat(int N) {
  Mat C; C.r = C.c = N + 1; C.a.resize((size_t)(N + 1) * (N + 1));
  std::vector<F> ch(2 * N); for (int r = 0; r < 2 * N; r++) ch[r] = chat(r, N);
  for (int n = 0; n <= N; n++) for (int m = 0; m <= N; m++) {
    long num = 2, den = N; if (n == 0 || n == N) den *= 2; if (m == 0 || m == N) den *= 2;
    C.a[(size_t)n * (N + 1) + m] = divi(mul_int(ch[((long)n * m) % (2 * N)], num), den);
  }
  C.finish(); return C;
}
// ⌊ℓ_j(t)⌋_B on the given node coordinates, exactly [Q10]; dn: the products Π_{k≠j}(x_j − x_k) (denoms())
inline void lagr_values(const std::vector<Z>& X, const std::vector<Z>& dn, const F& t, std::vector<S>& out) {
  int n = X.size(); out.resize(n); Z T, num, df;
  fx_to_mpz(t, T.v);
  for (int j = 0; j < n; j++) {
    mpz_set_ui(num.v, 1);
    for (int k = 0; k < n; k++) if (k != j) { mpz_sub(df.v, T.v, X[k].v); mpz_mul(num.v, num.v, df.v); }
    mpz_mul_2exp(num.v, num.v, BITS); mpz_fdiv_q(num.v, num.v, dn[j].v);
    out[j] = to_sm(fx_from_mpz<6, 5>(num.v));
  }
}
// The exact Chebyshev resampling in x from M1 to M2 nodes: R_kl = ⌊ℓ^(M1)_l(x^(M2)_k)⌋_B, the M1-interpolant
// evaluated at the M2-nodes with one floor per value (extension; S-RULE §6 "per-column M") [Q27]
inline Mat resample_mat(const Vec& x1, const Vec& x2) {
  std::vector<Z> X = to_ints(x1), d = denoms(X);
  Mat R; R.r = x2.size(); R.c = x1.size(); R.a.resize((size_t)R.r * R.c);
  for (int k = 0; k < R.r; k++) { std::vector<S> lv; lagr_values(X, d, x2[k], lv); for (int l = 0; l < R.c; l++) R.a[(size_t)k * R.c + l] = from_sm<6, 5>(lv[l]); }
  R.finish(); return R;
}
