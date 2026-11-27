// fixp.h: the arithmetic model of the rule (S-RULE §3.1) in fixed-width two's-complement integers.
//
// A number x of the model is held as the integer X = 2^(64 FL) x in L little-endian 64-bit limbs (two's complement).
// The rule's own type is Fx<6,5>: 320 fractional bits (B = 320), one limb of integer part.  Every operation is exact
// or floored exactly as §3.1 says; the model has no bound on X, so every result is range-checked (|x| < 2^60 times
// 2^(64 (L - FL - 1))) and the program stops (exit 3) rather than wrap.  A run that finishes therefore computed the
// unbounded model's values.  No floating point is used anywhere in this file.
//
//   a + b, a - b, -a           exact
//   mul_int(a, n)              n a, exact (n an integer)
//   a * b                      a ⊙ b = floor(a b)                         (floor, also for negative products)
//   fdiv(a, b)                 a ⊘ b = floor(a / b)                       (GMP mpn_tdiv_qr on magnitudes, then floor)
//   divi(a, n)                 a ⊘ n = floor(a / n), n a positive integer
//   shr(a, k)                  a ⊘ 2^k = floor(a / 2^k)
//   fsqrt(a)                   floor(sqrt(a)) = isqrt(2^B X) / 2^B
//   DotAcc / dot()             <a, b> = floor(sum a_i b_i): exact products, exact sum, one floor
#pragma once
#include <cstdint>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <unistd.h>
#include <x86intrin.h>
#include "gmpmin.h"

typedef unsigned __int128 u128;
typedef __int128 i128;

[[noreturn]] inline void fx_fail(const char* what) {
  fprintf(stderr, "FATAL (fixed point): %s -- the model's integer exceeded this build's width or a division by zero; "
                  "rebuild with more integer limbs\n", what);
  fflush(stderr);
  _exit(3);
}

template<int L_, int FL_> struct Fx {
  static constexpr int L = L_, FL = FL_, FB = 64 * FL_;
  uint64_t w[L_];
};

template<int L, int FL> inline void fx_check(const Fx<L, FL>& r) {
  int64_t t = (int64_t)r.w[L - 1];
  if ((t >> 60) != 0 && (t >> 60) != -1) fx_fail("overflow");
}
template<int L, int FL> inline bool fx_neg(const Fx<L, FL>& a) { return (int64_t)a.w[L - 1] < 0; }
template<int L, int FL> inline bool fx_iszero(const Fx<L, FL>& a) {
  uint64_t o = 0; for (int i = 0; i < L; i++) o |= a.w[i]; return o == 0;
}
template<int L, int FL> inline bool operator==(const Fx<L, FL>& a, const Fx<L, FL>& b) {
  uint64_t o = 0; for (int i = 0; i < L; i++) o |= a.w[i] ^ b.w[i]; return o == 0;
}
template<int L, int FL> inline bool operator!=(const Fx<L, FL>& a, const Fx<L, FL>& b) { return !(a == b); }
template<int L, int FL> inline int fx_cmp(const Fx<L, FL>& a, const Fx<L, FL>& b) {
  if ((int64_t)a.w[L - 1] != (int64_t)b.w[L - 1]) return (int64_t)a.w[L - 1] < (int64_t)b.w[L - 1] ? -1 : 1;
  for (int i = L - 2; i >= 0; i--) if (a.w[i] != b.w[i]) return a.w[i] < b.w[i] ? -1 : 1;
  return 0;
}
template<int L, int FL> inline bool operator<(const Fx<L, FL>& a, const Fx<L, FL>& b) { return fx_cmp(a, b) < 0; }
template<int L, int FL> inline bool operator>(const Fx<L, FL>& a, const Fx<L, FL>& b) { return fx_cmp(a, b) > 0; }
template<int L, int FL> inline bool operator<=(const Fx<L, FL>& a, const Fx<L, FL>& b) { return fx_cmp(a, b) <= 0; }
template<int L, int FL> inline bool operator>=(const Fx<L, FL>& a, const Fx<L, FL>& b) { return fx_cmp(a, b) >= 0; }

template<int L, int FL> inline Fx<L, FL> fx_zero() { Fx<L, FL> r; memset(r.w, 0, sizeof r.w); return r; }
template<int L, int FL> inline Fx<L, FL> fx_int(int64_t n) {        // the integer n as a number
  Fx<L, FL> r; for (int i = 0; i < L; i++) r.w[i] = 0;
  r.w[FL] = (uint64_t)n; for (int i = FL + 1; i < L; i++) r.w[i] = n < 0 ? ~0ull : 0;
  fx_check(r); return r;
}
template<int L, int FL> inline Fx<L, FL> operator+(const Fx<L, FL>& a, const Fx<L, FL>& b) {
  Fx<L, FL> r; unsigned char c = 0;
  for (int i = 0; i < L; i++) c = _addcarry_u64(c, a.w[i], b.w[i], (unsigned long long*)&r.w[i]);
  fx_check(r); return r;
}
template<int L, int FL> inline Fx<L, FL> operator-(const Fx<L, FL>& a, const Fx<L, FL>& b) {
  Fx<L, FL> r; unsigned char c = 0;
  for (int i = 0; i < L; i++) c = _subborrow_u64(c, a.w[i], b.w[i], (unsigned long long*)&r.w[i]);
  fx_check(r); return r;
}
template<int L, int FL> inline Fx<L, FL> operator-(const Fx<L, FL>& a) { return fx_zero<L, FL>() - a; }

// magnitude of a (two's complement negation when negative); returns the sign
template<int L, int FL> inline bool fx_abs(const Fx<L, FL>& a, uint64_t* m) {
  bool n = fx_neg(a);
  if (!n) { for (int i = 0; i < L; i++) m[i] = a.w[i]; return false; }
  unsigned char c = 0;
  for (int i = 0; i < L; i++) c = _subborrow_u64(c, 0, a.w[i], (unsigned long long*)&m[i]);
  return true;
}
// value from a magnitude q (L limbs, q < 2^(64L-4)) and sign; for a negative value with a nonzero discarded
// remainder (rnz) the floor is -q - 1 = ~q
template<int L, int FL> inline Fx<L, FL> fx_from_mag(const uint64_t* q, bool neg, bool rnz) {
  if (q[L - 1] >> 60) fx_fail("overflow");
  Fx<L, FL> r;
  if (!neg) { for (int i = 0; i < L; i++) r.w[i] = q[i]; }
  else if (rnz) { for (int i = 0; i < L; i++) r.w[i] = ~q[i]; }
  else { unsigned char c = 0; for (int i = 0; i < L; i++) c = _subborrow_u64(c, 0, q[i], (unsigned long long*)&r.w[i]); }
  fx_check(r); return r;
}

// magnitude product, product scanning with a three-word accumulator, fully unrolled for fixed limb counts
template<int LA, int LB> static inline void mulmag(const uint64_t* A, const uint64_t* B, uint64_t* P) {
  unsigned long long c0 = 0, c1 = 0, c2 = 0;
#pragma GCC unroll 16
  for (int k = 0; k < LA + LB - 1; k++) {
#pragma GCC unroll 8
    for (int i = (k < LB ? 0 : k - LB + 1); i <= (k < LA ? k : LA - 1); i++) {
      unsigned long long hi, lo = _mulx_u64(A[i], B[k - i], &hi);
      unsigned char c = _addcarry_u64(0, c0, lo, &c0); c = _addcarry_u64(c, c1, hi, &c1); c2 += c;
    }
    P[k] = c0; c0 = c1; c1 = c2; c2 = 0;
  }
  P[LA + LB - 1] = c0;
}
// every pair of limb counts 1..L to its unrolled kernel (small operands are common: most jets are tiny)
template<int L, int LA, int LB> struct MulTab {
  static inline void run(int la, int lb, const uint64_t* A, const uint64_t* B, uint64_t* P) {
    if (la == LA && lb == LB) { mulmag<LA, LB>(A, B, P); return; }
    if constexpr (LB > 1) MulTab<L, LA, LB - 1>::run(la, lb, A, B, P);
    else if constexpr (LA > 1) MulTab<L, LA - 1, L>::run(la, lb, A, B, P);
  }
};
template<int L> inline void mul_dispatch(int la, int lb, const uint64_t* A, const uint64_t* B, uint64_t* P) { MulTab<L, L, L>::run(la, lb, A, B, P); }
// a ⊙ b
template<int L, int FL> inline Fx<L, FL> operator*(const Fx<L, FL>& a, const Fx<L, FL>& b) {
  uint64_t A[L], Bm[L], P[2 * L];
  bool na = fx_abs(a, A), nb = fx_abs(b, Bm);
  int la = L, lb = L;
  while (la > 0 && A[la - 1] == 0) la--;
  while (lb > 0 && Bm[lb - 1] == 0) lb--;
  for (int i = 0; i < 2 * L; i++) P[i] = 0;
  if (la && lb) mul_dispatch<L>(la, lb, A, Bm, P);
  for (int i = FL + L; i < 2 * L; i++) if (P[i]) fx_fail("overflow in a product");
  uint64_t rnz = 0; for (int i = 0; i < FL; i++) rnz |= P[i];
  return fx_from_mag<L, FL>(P + FL, na != nb, rnz != 0);
}
// n a, exact
template<int L, int FL> inline Fx<L, FL> mul_int(const Fx<L, FL>& a, int64_t n) {
  uint64_t A[L], Q[L]; bool na = fx_abs(a, A); bool nn = n < 0; uint64_t m = nn ? (uint64_t)(-(n + 1)) + 1 : (uint64_t)n;
  u128 c = 0;
  for (int i = 0; i < L; i++) { u128 t = (u128)A[i] * m + (uint64_t)c; Q[i] = (uint64_t)t; c = t >> 64; }
  if ((uint64_t)c) fx_fail("overflow in an integer multiple");
  return fx_from_mag<L, FL>(Q, na != nn, false);
}
// a ⊘ n, n a positive integer: limb-by-limb division with a precomputed reciprocal of the normalized divisor
// (Möller and Granlund, "Improved division by invariant integers", 2011, Algorithm 4)
struct DivInv { uint64_t d, v; int s; };
inline DivInv make_divinv(uint64_t n) {
  DivInv r; r.s = __builtin_clzll(n); r.d = n << r.s; r.v = (uint64_t)(~(u128)0 / r.d - ((u128)1 << 64)); return r;
}
static inline uint64_t udiv_preinv(uint64_t u1, uint64_t u0, uint64_t d, uint64_t v, uint64_t* r) {
  u128 q = (u128)v * u1; q += ((u128)u1 << 64) | u0;
  uint64_t q1 = (uint64_t)(q >> 64) + 1, q0 = (uint64_t)q;
  uint64_t rr = u0 - q1 * d;
  if (rr > q0) { q1--; rr += d; }
  if (rr >= d) { q1++; rr -= d; }
  *r = rr; return q1;
}
struct DivInvTable { DivInv T[128]; DivInvTable() { for (int i = 1; i < 128; i++) T[i] = make_divinv(i); } };
inline const DivInv& divinv_small(int64_t n) { static const DivInvTable t; return t.T[n]; }   // thread-safe initialization
template<int L, int FL> inline Fx<L, FL> divi(const Fx<L, FL>& a, int64_t n) {
  if (n <= 0) fx_fail("divi: the divisor must be a positive integer");
  if (n == 1) return a;
  DivInv di = n < 128 ? divinv_small(n) : make_divinv((uint64_t)n);
  uint64_t A[L], Q[L]; bool na = fx_abs(a, A);
  uint64_t r = di.s ? A[L - 1] >> (64 - di.s) : 0;
  int top = L - 1; while (top >= 0 && A[top] == 0) { Q[top] = 0; top--; }    // leading zero limbs: zero quotient, r stays 0
  if (top < L - 1) r = (di.s && top >= 0) ? A[top] >> (64 - di.s) : 0;   // the shifted dividend's limb top + 1
  for (int i = top; i >= 0; i--) {
    uint64_t u0 = di.s ? (A[i] << di.s) | (i ? A[i - 1] >> (64 - di.s) : 0) : A[i];
    Q[i] = udiv_preinv(r, u0, di.d, di.v, &r);
  }
  return fx_from_mag<L, FL>(Q, na, r != 0);
}
// a ⊘ 2^k (k >= 0): arithmetic shift, which is the floor in two's complement
template<int L, int FL> inline Fx<L, FL> shr(const Fx<L, FL>& a, int k) {
  Fx<L, FL> r; int q = k / 64, s = k % 64; uint64_t ext = fx_neg(a) ? ~0ull : 0;
  for (int i = 0; i < L; i++) {
    uint64_t lo = (i + q < L) ? a.w[i + q] : ext, hi = (i + q + 1 < L) ? a.w[i + q + 1] : ext;
    r.w[i] = s ? (lo >> s) | (hi << (64 - s)) : lo;
  }
  return r;
}
// a ⊘ b
template<int L, int FL> inline Fx<L, FL> fdiv(const Fx<L, FL>& a, const Fx<L, FL>& b) {
  uint64_t A[L], Bm[L]; bool na = fx_abs(a, A), nb = fx_abs(b, Bm);
  int dn = L; while (dn > 0 && Bm[dn - 1] == 0) dn--;
  if (!dn) fx_fail("division by zero");
  uint64_t Num[L + FL]; for (int i = 0; i < FL; i++) Num[i] = 0; for (int i = 0; i < L; i++) Num[FL + i] = A[i];
  int nn = L + FL; while (nn > 0 && Num[nn - 1] == 0) nn--;
  uint64_t Q[L + FL + 1]; for (auto& q : Q) q = 0; bool rnz;
  if (nn < dn) { rnz = nn > 0; }
  else {
    uint64_t R[L];
    mpn_tdiv_qr((mp_limb_t*)Q, (mp_limb_t*)R, 0, (const mp_limb_t*)Num, nn, (const mp_limb_t*)Bm, dn);
    rnz = false; for (int i = 0; i < dn; i++) rnz |= R[i] != 0;
    for (int i = L; i < nn - dn + 1; i++) if (Q[i]) fx_fail("overflow in a quotient");
  }
  return fx_from_mag<L, FL>(Q, na != nb, rnz);
}
// floor(sqrt(a)), a >= 0
template<int L, int FL> inline Fx<L, FL> fsqrt(const Fx<L, FL>& a) {
  if (fx_neg(a)) fx_fail("square root of a negative number");
  uint64_t Num[L + FL]; for (int i = 0; i < FL; i++) Num[i] = 0; for (int i = 0; i < L; i++) Num[FL + i] = a.w[i];
  int nn = L + FL; while (nn > 0 && Num[nn - 1] == 0) nn--;
  uint64_t S[L + FL]; for (auto& s : S) s = 0;
  if (nn) { uint64_t R[L + FL]; mpn_sqrtrem((mp_limb_t*)S, (mp_limb_t*)R, (const mp_limb_t*)Num, nn); }
  return fx_from_mag<L, FL>(S, false, false);
}

// ---------------------------------------------------------------------------------------------- conversions
template<int L, int FL> inline void fx_to_mpz(const Fx<L, FL>& a, mpz_ptr z) {   // the integer X
  uint64_t m[L]; bool n = fx_abs(a, m);
  mpz_import(z, L, -1, 8, 0, 0, m);
  if (n) mpz_neg(z, z);
}
template<int L, int FL> inline Fx<L, FL> fx_from_mpz(mpz_srcptr z) {              // the integer X, exactly
  if (mpz_sizeinbase(z, 2) > (size_t)(64 * L - 4)) fx_fail("integer too large for this build");
  uint64_t m[L]; for (auto& x : m) x = 0; size_t cnt = 0;
  mpz_export(m, &cnt, -1, 8, 0, 0, z);
  return fx_from_mag<L, FL>(m, mpz_sgn(z) < 0, false);
}
template<int L, int FL> inline std::string fx_dec(const Fx<L, FL>& a) {            // X in decimal
  Z z; fx_to_mpz(a, z.v); char* s = mpz_get_str(nullptr, 10, z.v); std::string r(s); free(s); return r;
}
template<int L, int FL> inline std::string fx_hex(const Fx<L, FL>& a) {            // X in hexadecimal, signed
  Z z; fx_to_mpz(a, z.v); bool n = mpz_sgn(z.v) < 0; mpz_abs(z.v, z.v);
  char* s = mpz_get_str(nullptr, 16, z.v); std::string r = (n ? "-0x" : "0x") + std::string(s); free(s); return r;
}

// ---------------------------------------------------------------------------------------------- exact dot products
// Operands in sign-magnitude form (the sign in the top bit of the top limb), so that a vector used in many dot
// products is converted once.  Each product is formed exactly and added to (or subtracted from) an exact
// two's-complement accumulator of 2L + 1 limbs; the total is floored once at the end.  The result is therefore
// independent of the order of the terms and of how the work is divided among threads.
template<int L> struct SM { uint64_t m[L]; };
template<int L, int FL> inline SM<L> to_sm(const Fx<L, FL>& a) {
  SM<L> s; bool n = fx_abs(a, s.m); if (n) s.m[L - 1] |= 1ull << 63; return s;
}
template<int L, int FL> inline Fx<L, FL> from_sm(const SM<L>& s) {
  uint64_t m[L]; for (int i = 0; i < L; i++) m[i] = s.m[i]; bool n = m[L - 1] >> 63; m[L - 1] &= ~(1ull << 63);
  return fx_from_mag<L, FL>(m, n, false);
}

template<int L, int FL> struct DotAcc {
  uint64_t acc[2 * L + 1];                       // the exact running sum, two's complement
  inline void clear() { for (int k = 0; k < 2 * L + 1; k++) acc[k] = 0; }
  inline void mac(const SM<L>& a, const SM<L>& b) {
    const uint64_t sg = (a.m[L - 1] ^ b.m[L - 1]) >> 63, msk = 0 - sg;
    uint64_t A[L], B[L], P[2 * L];
    for (int i = 0; i < L; i++) { A[i] = a.m[i]; B[i] = b.m[i]; }
    A[L - 1] &= ~(1ull << 63); B[L - 1] &= ~(1ull << 63);
    if (A[L - 1]) { if (B[L - 1]) mulmag<L, L>(A, B, P); else { mulmag<L, L - 1>(A, B, P); P[2 * L - 1] = 0; } }
    else { if (B[L - 1]) { mulmag<L - 1, L>(A, B, P); P[2 * L - 1] = 0; } else { mulmag<L - 1, L - 1>(A, B, P); P[2 * L - 2] = P[2 * L - 1] = 0; } }
    unsigned char c = (unsigned char)sg;          // acc += (P xor msk) + sg, i.e. acc -= P for a negative product
    for (int k = 0; k < 2 * L; k++) c = _addcarry_u64(c, acc[k], P[k] ^ msk, (unsigned long long*)&acc[k]);
    acc[2 * L] += msk + c;
  }
  inline Fx<L, FL> result() const {
    constexpr int W = 2 * L + 1;
    const uint64_t ext = (int64_t)acc[W - 1] < 0 ? ~0ull : 0;
    for (int k = FL + L; k < W; k++) if (acc[k] != ext) fx_fail("overflow in a dot product");
    Fx<L, FL> r; for (int k = 0; k < L; k++) r.w[k] = acc[FL + k];   // dropping FL limbs: the floor
    if (((int64_t)r.w[L - 1] < 0) != (ext != 0)) fx_fail("overflow in a dot product");
    fx_check(r); return r;
  }
};
// <a, b> over n terms with strides
template<int L, int FL> inline Fx<L, FL> dot(const SM<L>* a, long sa, const SM<L>* b, long sb, int n) {
  DotAcc<L, FL> acc; acc.clear();
  for (int i = 0; i < n; i++) acc.mac(a[i * sa], b[i * sb]);
  return acc.result();
}

typedef Fx<6, 5> F;      // the rule's numbers: B = 320
typedef SM<6> S;
static const int BITS = 320;
