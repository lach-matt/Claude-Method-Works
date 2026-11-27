// exactfn.h: S-RULE §3.2 -- the elementary functions and constants as stated finite computations in the model.
// Every choice the text leaves open is marked [Qn] (rule/README.md, "Questions for the specification").
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

// the least k >= 0 with |y| <= 2^(k-3), and z = y ⊘ 2^k
template<class T> inline int kz(const T& y, T& z) {
  T a = fx_neg(y) ? -y : y; int k = 0;
  while (a > pow2<T>(k - 3)) k++;
  z = shr(y, k); return k;
}
// exp(y): E := 1; for n = deg..1: E := 1 + ((z ⊙ E) ⊘ n); then k squarings
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

// log(y), y > 0
inline F logF(const F& y) {
  if (fx_neg(y) || fx_iszero(y)) fx_fail("log of a non-positive number");
  int m = bitlen(y) - 1 - BITS;                             // 2^m <= y < 2^(m+1)
  if (!(y < mul_int(pow2<F>(m - 1), 3))) m++;               // w >= 3/2: w := w/2, m := m + 1
  F p2 = pow2<F>(m);
  F t = fdiv(y - p2, y + p2);                               // (w - 1) ⊘ (w + 1), w exact [Q3]
  F t2 = t * t, P = CS.logc[70];
  for (int j = 69; j >= 0; j--) P = CS.logc[j] + t2 * P;    // Horner in t ⊙ t [Q5]
  return mul_int(CS.l2, m) + mul_int(t * P, 2);
}
// (sin y, cos y)
inline void sincosF(const F& y, F& S, F& C) {
  F z; int k = kz(y, z);
  S = CS.sinc[45]; for (int n = 44; n >= 0; n--) S = CS.sinc[n] + z * S;     // Horner in z [Q4]
  C = CS.cosc[44]; for (int n = 43; n >= 0; n--) C = CS.cosc[n] + z * C;
  for (int i = 0; i < k; i++) { F S2 = mul_int(S, 2) * C, C2 = C * C - S * S; S = S2; C = C2; }   // [Q2]
}
inline F chat(long num, long den) {                         // ĉ(num/den) = cos(π̂ ⊙ ⌊num/den⌋_B) [Q6]
  F S, C; sincosF(CS.pi * fl_rat<F>(num, den), S, C); return C;
}
inline void sinhcosh(const F& y, F& sh, F& ch) {
  F e1 = expF(y), e2 = expF(-y); sh = divi(e1 - e2, 2); ch = divi(e1 + e2, 2);
}

inline void init_consts(int seed) {
  machin(CS.pi);
  { Z s(0), num, den, t, three(3); mpz_set_ui(num.v, 1); mpz_mul_2exp(num.v, num.v, BITS);
    for (int j = 0; j <= 100; j++) { mpz_pow_ui(den.v, three.v, 2 * j + 1); mpz_mul_si(den.v, den.v, 2 * j + 1);
      mpz_fdiv_q(t.v, num.v, den.v); mpz_add(s.v, s.v, t.v); }
    mpz_mul_si(s.v, s.v, 2); CS.l2 = fx_from_mpz<6, 5>(s.v); }
  CS.logc.resize(71); for (int j = 0; j <= 70; j++) CS.logc[j] = fl_rat<F>(1, 2 * j + 1);
  // Taylor coefficients ⌊±1/n!⌋_B (zero where the polynomial has none)
  CS.sinc.assign(46, fx_zero<6, 5>()); CS.cosc.assign(45, fx_zero<6, 5>());
  { Z fact(1), one_(1), sgnd;
    for (int n = 0; n <= 45; n++) {
      if (n > 0) mpz_mul_si(fact.v, fact.v, n);
      long sg = 0;
      if (n % 2 == 1) sg = ((n - 1) / 2) % 2 ? -1 : 1;
      if (sg) { mpz_set_si(sgnd.v, sg); CS.sinc[n] = fl_ratz<F>(sgnd.v, fact.v); }
      if (n % 2 == 0 && n <= 44) { mpz_set_si(sgnd.v, (n / 2) % 2 ? -1 : 1); CS.cosc[n] = fl_ratz<F>(sgnd.v, fact.v); }
    } }
  CS.half = fl_rat<F>(1, 2);
  F o = one<F>();
  CS.xi0 = -logF(fx_int<6, 5>(4500) + fsqrt(fx_int<6, 5>(20250001)));
  CS.ah = fl_rat<F>(1, 500);
  CS.lam = seed == 1 ? o : fsqrt(fl_rat<F>(1, 10));
}
