// exactfn.h: P-APPC2 def:appc-functions -- the elementary functions and constants as stated finite computations.
#pragma once
#include "fixp.h"
#include <vector>
#include <algorithm>

// ⌊num/den⌋_B for integers (den > 0 or < 0), exactly, in the type T
template<class T> inline T fl_rat(long num, long den) {
  Z z(num), d(den); mpz_mul_2exp(z.v, z.v, T::FB); mpz_fdiv_q(z.v, z.v, d.v); return fx_from_mpz<T::L, T::FL>(z.v);
}
template<class T> inline T fl_ratz(mpz_srcptr num, mpz_srcptr den) {
  Z z; mpz_mul_2exp(z.v, num, T::FB); mpz_fdiv_q(z.v, z.v, den); return fx_from_mpz<T::L, T::FL>(z.v);
}
template<class T> inline T one() { return fx_int<T::L, T::FL>(1); }
template<class T> inline T pow2(int e) {           // 2^e as a number, e >= -FB
  T r = fx_zero<T::L, T::FL>(); int bit = T::FB + e; r.w[bit / 64] = 1ull << (bit % 64); return r;
}
template<class T> inline int bitlen(const T& a) {  // bit length of the (positive) integer X
  for (int i = T::L - 1; i >= 0; i--) if (a.w[i]) return 64 * i + 64 - __builtin_clzll(a.w[i]);
  return 0;
}

// the least k >= 0 with 8|y| <= 2^k, and z = y ⊘ 2^k
template<class T> inline int kz(const T& y, T& z) {
  T a = fx_neg(y) ? -y : y; int k = 0;
  while (a > pow2<T>(k - 3)) k++;
  z = shr(y, k); return k;
}
// (a) exp y: E_45 := 1, E_(n-1) := 1 + (z ⊙ E_n) ⊘ n, then k squarings
template<class T> inline T expF(const T& y, int deg = 45) {
  T z; int k = kz(y, z); const T o = one<T>(); T E = o;
  for (int n = deg; n >= 1; n--) E = o + divi(z * E, n);
  for (int i = 0; i < k; i++) E = E * E;
  return E;
}

struct Consts {                     // the rule's constants, B = 320
  F pi, l2, xi0, ah, lam, half;
  std::vector<F> logc, sinc, cosc, K;
};
extern Consts CS;

inline void machin(F& pi) {
  auto A = [](long n, int J) {
    Z s(0), num, den, t, nn(n);
    mpz_set_ui(num.v, 1); mpz_mul_2exp(num.v, num.v, BITS);
    for (int j = 0; j <= J; j++) {
      mpz_pow_ui(den.v, nn.v, 2 * j + 1); mpz_mul_si(den.v, den.v, 2 * j + 1);
      mpz_fdiv_q(t.v, num.v, den.v);                       // ⌊1/((2j+1) n^(2j+1))⌋_B, then the sign
      if (j % 2) mpz_sub(s.v, s.v, t.v); else mpz_add(s.v, s.v, t.v);
    }
    return s;
  };
  Z a5 = A(5, 70), a239 = A(239, 20), r;
  mpz_mul_si(a5.v, a5.v, 16); mpz_mul_si(a239.v, a239.v, 4); mpz_sub(r.v, a5.v, a239.v);
  pi = fx_from_mpz<6, 5>(r.v);
}

// (c) log y, y > 0: w := y ⊘ 2^m (exact for m <= 0); if w >= 3/2, w := w ⊘ 2, m := m + 1; t := (w − 1) ⊘ (w + 1)
inline F logF(const F& y) {
  if (fx_neg(y) || fx_iszero(y)) fx_fail("log of a non-positive number");
  int m = bitlen(y) - 1 - BITS;                             // 2^m <= y < 2^(m+1)
  F w = m > 0 ? shr(y, m) : y;
  if (m < 0) { for (int i = 0; i < -m; i++) w = mul_int(w, 2); }
  if (!(w < mul_int(pow2<F>(-1), 3))) { w = shr(w, 1); m++; }
  const F o = one<F>();
  F t = fdiv(w - o, w + o), u = t * t, P = CS.logc[70];
  for (int j = 69; j >= 0; j--) P = CS.logc[j] + u * P;
  return mul_int(CS.l2, m) + mul_int(t * P, 2);
}
// (b) sin y, cos y: u := z ⊙ z; S_22 = C_22 := 1; S_(j-1) := 1 − (u ⊙ S_j) ⊘ (2j(2j+1)), C_(j-1) := 1 − (u ⊙ C_j) ⊘ ((2j−1)2j);
// (s, c) := (z ⊙ S_0, C_0); k times (s, c) := (2 (s ⊙ c), c ⊙ c − s ⊙ s)
inline void sincosF(const F& y, F& s, F& c) {
  F z; int k = kz(y, z); const F o = one<F>(); F u = z * z, S = o, C = o;
  for (int j = 22; j >= 1; j--) { S = o - divi(u * S, (int64_t)2 * j * (2 * j + 1)); C = o - divi(u * C, (int64_t)(2 * j - 1) * 2 * j); }
  s = z * S; c = C;
  for (int i = 0; i < k; i++) { F s2 = mul_int(s * c, 2), c2 = c * c - s * s; s = s2; c = c2; }
}
// (e) ĉ(j, n), standing for cos(π j/n)
inline F chat(long j, long n) {
  j %= 2 * n; if (j < 0) j += 2 * n;
  if (j == 0) return one<F>();
  if (j == n) return -one<F>();
  if (j > n) j = 2 * n - j;
  F s, c; sincosF(divi(mul_int(CS.pi, j), n), s, c); return c;
}
inline void sinhcosh(const F& y, F& sh, F& ch) {
  F e1 = expF(y), e2 = expF(-y); sh = divi(e1 - e2, 2); ch = divi(e1 + e2, 2);
}

inline void init_consts(int seed) {
  machin(CS.pi);
  { Z s(0), num, den, t, three(3); mpz_set_ui(num.v, 1); mpz_mul_2exp(num.v, num.v, BITS);
    for (int j = 0; j <= 110; j++) { mpz_pow_ui(den.v, three.v, 2 * j + 1); mpz_mul_si(den.v, den.v, 2 * j + 1);
      mpz_fdiv_q(t.v, num.v, den.v); mpz_add(s.v, s.v, t.v); }
    mpz_mul_si(s.v, s.v, 2); CS.l2 = fx_from_mpz<6, 5>(s.v); }
  CS.logc.resize(71); for (int j = 0; j <= 70; j++) CS.logc[j] = fl_rat<F>(1, 2 * j + 1);
  CS.half = fl_rat<F>(1, 2);
  F o = one<F>();
  CS.xi0 = -logF(fx_int<6, 5>(4500) + fsqrt(fx_int<6, 5>(20250001)));
  CS.ah = fl_rat<F>(1, 500);
  CS.lam = seed == 1 ? o : fsqrt(fl_rat<F>(1, 10));
}
