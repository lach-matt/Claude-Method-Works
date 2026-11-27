// fx.h: fixed-point numbers X / 2^B with B = 64 (L - 1), X a signed two's-complement integer of L 64-bit limbs.
// Rounding: every product and quotient is floored (rounded toward -infinity) to a multiple of 2^-B; sums are exact;
// fused dot products accumulate the exact products and floor once.  This is the arithmetic model of S-RULE.
#pragma once
#include <cstdint>
#include <cstring>
#include <cmath>
#include <cstdio>
typedef unsigned __int128 u128;
typedef __int128 i128;

template<int L> struct fx {
  uint64_t w[L];                                 // little-endian limbs; w[L-1] is the (signed) integer part
  fx() { memset(w, 0, sizeof w); }
  fx(int a) { memset(w, 0, sizeof w); w[L - 1] = (uint64_t)(int64_t)a; }
  bool neg() const { return (int64_t)w[L - 1] < 0; }
  bool zero() const { for (int i = 0; i < L; i++) if (w[i]) return false; return true; }
};
template<int L> inline fx<L> operator+(const fx<L>& a, const fx<L>& b) {
  fx<L> r; u128 c = 0;
  for (int i = 0; i < L; i++) { c += (u128)a.w[i] + b.w[i]; r.w[i] = (uint64_t)c; c >>= 64; }
  return r;
}
template<int L> inline fx<L> operator-(const fx<L>& a) {
  fx<L> r; u128 c = 1;
  for (int i = 0; i < L; i++) { c += (u128)(~a.w[i]); r.w[i] = (uint64_t)c; c >>= 64; }
  return r;
}
template<int L> inline fx<L> operator-(const fx<L>& a, const fx<L>& b) {
  fx<L> r; i128 c = 0;
  for (int i = 0; i < L; i++) { c += (i128)(u128)a.w[i] - (i128)(u128)b.w[i]; r.w[i] = (uint64_t)c; c >>= 64; }
  return r;
}
template<int L> inline fx<L>& operator+=(fx<L>& a, const fx<L>& b) { a = a + b; return a; }
template<int L> inline fx<L>& operator-=(fx<L>& a, const fx<L>& b) { a = a - b; return a; }

// signed full product into 2L limbs (two's complement, mod 2^(128 L))
template<int L> inline void mulfull(const fx<L>& a, const fx<L>& b, uint64_t* P) {
  for (int i = 0; i < 2 * L; i++) P[i] = 0;
  for (int i = 0; i < L; i++) {
    u128 c = 0; uint64_t ai = a.w[i];
    for (int j = 0; j < L; j++) { c += (u128)ai * b.w[j] + P[i + j]; P[i + j] = (uint64_t)c; c >>= 64; }
    P[i + L] = (uint64_t)c;
  }
  if (a.neg()) { i128 c = 0; for (int j = 0; j < L; j++) { c += (i128)(u128)P[L + j] - (i128)(u128)b.w[j]; P[L + j] = (uint64_t)c; c >>= 64; } }
  if (b.neg()) { i128 c = 0; for (int j = 0; j < L; j++) { c += (i128)(u128)P[L + j] - (i128)(u128)a.w[j]; P[L + j] = (uint64_t)c; c >>= 64; } }
}
// floor(a b / 2^B): limbs L-1 .. 2L-2 of the product (arithmetic shift of a two's-complement integer is floor)
template<int L> inline fx<L> operator*(const fx<L>& a, const fx<L>& b) {
  uint64_t P[2 * L]; mulfull(a, b, P); fx<L> r;
  for (int i = 0; i < L; i++) r.w[i] = P[L - 1 + i];
  return r;
}
template<int L> inline fx<L>& operator*=(fx<L>& a, const fx<L>& b) { a = a * b; return a; }
// a * n for a small integer n (exact)
template<int L> inline fx<L> muli(const fx<L>& a, int64_t n) { fx<L> b(0); b.w[L - 1] = (uint64_t)n; uint64_t P[2 * L]; mulfull(a, b, P); fx<L> r; for (int i = 0; i < L; i++) r.w[i] = P[L - 1 + i]; return r; }
// floor(a / n), n > 0 a small integer
template<int L> inline fx<L> divi(const fx<L>& a, uint64_t n) {
  bool ng = a.neg(); fx<L> m = ng ? -a : a; fx<L> q; u128 rem = 0;
  for (int i = L - 1; i >= 0; i--) { u128 cur = (rem << 64) | m.w[i]; q.w[i] = (uint64_t)(cur / n); rem = cur % n; }
  if (ng) { q = -q; if (rem) { fx<L> u; u.w[0] = 1; q = q - u; } }
  return q;
}

// accumulator of exact products (2L + 1 limbs), floored once at the end
template<int L> struct acc {
  uint64_t s[2 * L + 1];
  acc() { memset(s, 0, sizeof s); }
  inline void add(const fx<L>& a, const fx<L>& b) {
    uint64_t P[2 * L]; mulfull(a, b, P);
    uint64_t ext = (int64_t)P[2 * L - 1] < 0 ? ~0ULL : 0;
    u128 c = 0;
    for (int i = 0; i < 2 * L; i++) { c += (u128)s[i] + P[i]; s[i] = (uint64_t)c; c >>= 64; }
    s[2 * L] = (uint64_t)((u128)s[2 * L] + ext + c);
  }
  inline fx<L> get() const { fx<L> r; for (int i = 0; i < L; i++) r.w[i] = s[L - 1 + i]; return r; }
};

template<int L> struct fxu {
  static fx<L> ulp() { fx<L> r; r.w[0] = 1; return r; }
};
// exact floor(d 2^B) of a double
template<int L> inline fx<L> from_double(double d) {
  fx<L> r; if (d == 0) return r;
  bool ng = d < 0; double a = std::fabs(d); int e; double m = std::frexp(a, &e);   // a = m 2^e, m in [1/2, 1)
  uint64_t M = (uint64_t)std::ldexp(m, 53); int sh = e - 53 + 64 * (L - 1);       // a 2^B = M 2^sh
  bool rem = false;
  if (sh >= 0) { int li = sh / 64, bi = sh % 64; if (li < L) r.w[li] |= M << bi; if (bi && li + 1 < L) r.w[li + 1] |= M >> (64 - bi); }
  else { int s = -sh; if (s >= 64) { rem = M != 0; M = 0; } else { rem = (M & ((1ULL << s) - 1)) != 0; M >>= s; } r.w[0] = M; }
  if (ng) { r = -r; if (rem) { fx<L> u; u.w[0] = 1; r = r - u; } }
  return r;
}
template<int L> inline double to_dbl(const fx<L>& a) {
  bool ng = a.neg(); fx<L> m = ng ? -a : a; double s = 0;
  for (int i = L - 1; i >= 0; i--) s += std::ldexp((double)m.w[i], 64 * (i - (L - 1)));
  return ng ? -s : s;
}
template<int L> inline bool lt(const fx<L>& a, const fx<L>& b) { return (a - b).neg(); }
// floor(2^B / y) for y > 0 (Newton reciprocal in fixed point, then exact correction)
template<int L> inline fx<L> recip(const fx<L>& y) {
  fx<L> one(1); fx<L> two(2);
  fx<L> x = from_double<L>(1.0 / to_dbl(y));
  for (int i = 0; i < 8; i++) { x = x * (two - y * x); }
  // correction to the exact floor: want x y <= 1 < (x + ulp) y in exact arithmetic
  fx<L> u; u.w[0] = 1;
  for (int it = 0; it < 64; it++) {
    uint64_t P[2 * L]; mulfull(x, y, P);                  // exact x y 2^(2B)
    // compare with 1 * 2^(2B): limb 2L-2 == 1 and lower all zero  -> equality
    bool gt = false, eq = true;
    // value = P as signed 2L-limb; target T has limb (2L-2) = 1
    for (int i = 2 * L - 1; i >= 0; i--) { uint64_t t = (i == 2 * L - 2) ? 1 : 0; if (P[i] != t) { eq = false; gt = P[i] > t; break; } }
    if (!eq && gt) { x = x - u; continue; }
    fx<L> x1 = x + u; mulfull(x1, y, P); eq = true; gt = false;
    for (int i = 2 * L - 1; i >= 0; i--) { uint64_t t = (i == 2 * L - 2) ? 1 : 0; if (P[i] != t) { eq = false; gt = P[i] > t; break; } }
    if (eq || !gt) { x = x1; continue; }
    break;
  }
  return x;
}
// exp(y) by Horner on the Taylor polynomial of degree NE, every step floored (used for |y| < 1/8)
template<int L, int NE> inline fx<L> fexp(const fx<L>& y) {
  fx<L> s(1);
  for (int n = NE; n >= 1; n--) { s = divi(y * s, (uint64_t)n); s = s + fx<L>(1); if (n == 1) break; }
  return s;
}
