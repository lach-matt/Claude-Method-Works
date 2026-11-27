// dd.h: double-double arithmetic (about 32 significant digits), error-free transformations with FMA.
// Compile without -ffast-math.  Functions accurate to a few units of 2^-104 relative unless noted.
#pragma once
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>

struct dd {
  double hi, lo;
  dd() : hi(0), lo(0) {}
  dd(double h) : hi(h), lo(0) {}
  dd(int h) : hi((double)h), lo(0) {}
  dd(long h) : hi((double)h), lo(0) {}
  dd(double h, double l) : hi(h), lo(l) {}
};

static inline dd qtwo_sum(double a, double b) { double s = a + b; return dd(s, b - (s - a)); }
static inline dd two_sum(double a, double b) {
  double s = a + b, bb = s - a; return dd(s, (a - (s - bb)) + (b - bb));
}
static inline dd two_prod(double a, double b) { double p = a * b; return dd(p, std::fma(a, b, -p)); }

static inline dd operator+(const dd& a, const dd& b) {
  dd s = two_sum(a.hi, b.hi), t = two_sum(a.lo, b.lo);
  s.lo += t.hi; s = qtwo_sum(s.hi, s.lo); s.lo += t.lo; return qtwo_sum(s.hi, s.lo);
}
static inline dd operator-(const dd& a) { return dd(-a.hi, -a.lo); }
static inline dd operator-(const dd& a, const dd& b) { return a + (-b); }
static inline dd operator*(const dd& a, const dd& b) {
  dd p = two_prod(a.hi, b.hi); p.lo += a.hi * b.lo + a.lo * b.hi; return qtwo_sum(p.hi, p.lo);
}
static inline dd operator*(const dd& a, double b) {
  dd p = two_prod(a.hi, b); p.lo += a.lo * b; return qtwo_sum(p.hi, p.lo);
}
static inline dd operator*(double b, const dd& a) { return a * b; }
static inline dd operator/(const dd& a, const dd& b) {
  double q1 = a.hi / b.hi; dd r = a - b * q1;
  double q2 = r.hi / b.hi; r = r - b * q2;
  double q3 = r.hi / b.hi;
  dd q = qtwo_sum(q1, q2); return q + dd(q3);
}
static inline dd& operator+=(dd& a, const dd& b) { a = a + b; return a; }
static inline dd& operator-=(dd& a, const dd& b) { a = a - b; return a; }
static inline dd& operator*=(dd& a, const dd& b) { a = a * b; return a; }
static inline dd& operator/=(dd& a, const dd& b) { a = a / b; return a; }
static inline bool operator<(const dd& a, const dd& b) { return a.hi < b.hi || (a.hi == b.hi && a.lo < b.lo); }
static inline bool operator>(const dd& a, const dd& b) { return b < a; }
static inline double to_double(const dd& a) { return a.hi + a.lo; }
static inline dd ddabs(const dd& a) { return a.hi < 0 ? -a : a; }
static inline dd ldexp(const dd& a, int e) { return dd(std::ldexp(a.hi, e), std::ldexp(a.lo, e)); }

static const dd DD_PI(3.141592653589793116e+00, 1.224646799147353207e-16);
static const dd DD_LN2(6.931471805599452862e-01, 2.319046813846299558e-17);

static inline dd sqrt(const dd& a) {
  if (a.hi <= 0) return dd(0.0);
  double x = 1.0 / std::sqrt(a.hi); double ax = a.hi * x;
  dd d = a - two_prod(ax, ax);
  return two_sum(ax, d.hi * (x * 0.5));
}
// exp(r) - 1 for |r| <= 1/512 by Taylor series
static inline dd expm1_small(const dd& r) {
  dd s = r, t = r; double eps = 1e-34 * std::fabs(r.hi);
  for (int k = 2; k < 40; k++) { t = t * r / dd((double)k); s = s + t; if (std::fabs(t.hi) < eps) break; }
  return s;
}
static inline dd exp(const dd& a) {
  if (a.hi > 709) return dd(INFINITY);
  if (a.hi < -745) return dd(0.0);
  double k = std::floor(a.hi / DD_LN2.hi + 0.5);
  dd r = a - DD_LN2 * k;
  r = ldexp(r, -10);                       // |r| <= ln2/2^11
  dd e = expm1_small(r);                   // e^r - 1
  for (int i = 0; i < 10; i++) e = e * (e + dd(2.0));   // (1+e)^2 - 1 = e(e+2)
  e = e + dd(1.0);
  return ldexp(e, (int)k);
}
static inline dd expm1(const dd& a) {
  if (std::fabs(a.hi) > 0.5) return exp(a) - dd(1.0);
  dd r = ldexp(a, -10);
  dd e = expm1_small(r);
  for (int i = 0; i < 10; i++) e = e * (e + dd(2.0));
  return e;
}
static inline dd log(const dd& a) {
  if (a.hi <= 0) return dd(NAN);
  dd x(std::log(a.hi));
  for (int i = 0; i < 2; i++) x = x + a * exp(-x) - dd(1.0);   // Newton
  return x;
}
// log1p for |a| small, by Newton on expm1
static inline dd log1p(const dd& a) {
  dd x(std::log1p(a.hi));
  for (int i = 0; i < 2; i++) { dd e = expm1(x); x = x - (e - a) / (e + dd(1.0)); }
  return x;
}
static inline void sincos_small(const dd& r, dd& s, dd& c) {   // |r| <= pi/4
  dd r2 = r * r, t = r; s = r; double eps = 1e-34;
  for (int k = 3; k < 60; k += 2) { t = -t * r2 / dd((double)((k - 1) * k)); s = s + t; if (std::fabs(t.hi) < eps * std::fabs(s.hi)) break; }
  t = dd(1.0); c = dd(1.0);
  for (int k = 2; k < 60; k += 2) { t = -t * r2 / dd((double)((k - 1) * k)); c = c + t; if (std::fabs(t.hi) < eps) break; }
}
static inline void sincos(const dd& a, dd& s, dd& c) {
  dd hp = ldexp(DD_PI, -1);
  double k = std::floor(a.hi / hp.hi + 0.5);
  dd r = a - hp * k;                        // adequate for |a| < 1e6 (argument reduction in dd)
  dd ss, cc; sincos_small(r, ss, cc);
  int q = ((long)k % 4 + 4) % 4;
  if (q == 0) { s = ss; c = cc; } else if (q == 1) { s = cc; c = -ss; } else if (q == 2) { s = -ss; c = -cc; } else { s = -cc; c = ss; }
}
static inline dd sin(const dd& a) { dd s, c; sincos(a, s, c); return s; }
static inline dd cos(const dd& a) { dd s, c; sincos(a, s, c); return c; }
static inline dd sinh(const dd& a) {
  if (std::fabs(a.hi) < 0.5) { dd e = expm1(a); return ldexp(e * (e + dd(2.0)) / (e + dd(1.0)), -1); }
  dd e = exp(a); return ldexp(e - dd(1.0) / e, -1);
}
static inline dd cosh(const dd& a) { dd e = exp(a); return ldexp(e + dd(1.0) / e, -1); }
static inline dd asinh(const dd& a) {        // Newton on sinh
  dd x(std::asinh(a.hi));
  for (int i = 0; i < 2; i++) x = x - (sinh(x) - a) / cosh(x);
  return x;
}
static inline dd dd_from_string(const char* s) {   // decimal string -> dd (exact to rounding of the digits)
  bool neg = false; const char* p = s; while (*p == ' ') p++;
  if (*p == '-') { neg = true; p++; } else if (*p == '+') p++;
  dd r(0.0); int e10 = 0; bool frac = false;
  for (; *p; p++) {
    if (*p == '.') { frac = true; continue; }
    if (*p == 'e' || *p == 'E') { e10 += atoi(p + 1); break; }
    if (*p < '0' || *p > '9') break;
    r = r * dd(10.0) + dd((double)(*p - '0')); if (frac) e10--;
  }
  dd ten(10.0), pw(1.0); int ae = e10 < 0 ? -e10 : e10;
  for (int i = 0; i < ae; i++) pw = pw * ten;
  r = e10 < 0 ? r / pw : r * pw;
  return neg ? -r : r;
}
static inline std::string dd_to_string(const dd& a, int digits = 32) {   // decimal, digits significant
  if (a.hi == 0) return "0";
  dd x = ddabs(a); int e = (int)std::floor(std::log10(x.hi));
  dd pw(1.0), ten(10.0); for (int i = 0; i < std::abs(e); i++) pw = pw * ten;
  x = e >= 0 ? x / pw : x * pw;
  while (x.hi >= 10) { x = x / ten; e++; } while (x.hi < 1) { x = x * ten; e--; }
  std::string s = a.hi < 0 ? "-" : "";
  for (int i = 0; i < digits; i++) {
    int d = (int)std::floor(x.hi); if (d > 9) d = 9; if (d < 0) d = 0;
    s += char('0' + d); if (i == 0) s += '.';
    x = (x - dd((double)d)) * ten;
  }
  char buf[16]; snprintf(buf, sizeof buf, "e%+d", e); return s + buf;
}
