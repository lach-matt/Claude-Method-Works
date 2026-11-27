// qd.h: quad-double arithmetic (about 64 significant digits), after Hida, Li and Bailey's algorithms (accurate
// addition and multiplication, long division), with FMA error-free products.  Same interface as dd.h.  Compile
// without -ffast-math.
#pragma once
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>

struct qd {
  double hi, l1, l2, l3;
  qd() : hi(0), l1(0), l2(0), l3(0) {}
  qd(double h) : hi(h), l1(0), l2(0), l3(0) {}
  qd(int h) : hi((double)h), l1(0), l2(0), l3(0) {}
  qd(long h) : hi((double)h), l1(0), l2(0), l3(0) {}
  qd(double a, double b, double c, double d) : hi(a), l1(b), l2(c), l3(d) {}
  double operator[](int i) const { return i == 0 ? hi : i == 1 ? l1 : i == 2 ? l2 : l3; }
};
namespace qdi {
static inline double qts(double a, double b, double& e) { double s = a + b; e = b - (s - a); return s; }
static inline double ts(double a, double b, double& e) { double s = a + b, bb = s - a; e = (a - (s - bb)) + (b - bb); return s; }
static inline double tp(double a, double b, double& e) { double p = a * b; e = std::fma(a, b, -p); return p; }
static inline void three_sum(double& a, double& b, double& c) { double t1, t2, t3; t1 = ts(a, b, t2); a = ts(c, t1, t3); b = ts(t2, t3, c); }
static inline void renorm4(double& c0, double& c1, double& c2, double& c3) {
  double s0, s1, s2 = 0.0, s3 = 0.0;
  if (std::isinf(c0)) return;
  s0 = qts(c2, c3, c3); s0 = qts(c1, s0, c2); c0 = qts(c0, s0, c1);
  s0 = c0; s1 = c1;
  if (s1 != 0.0) { s1 = qts(s1, c2, s2); if (s2 != 0.0) s2 = qts(s2, c3, s3); else s1 = qts(s1, c3, s2); }
  else { s0 = qts(s0, c2, s1); if (s1 != 0.0) s1 = qts(s1, c3, s2); else s0 = qts(s0, c3, s1); }
  c0 = s0; c1 = s1; c2 = s2; c3 = s3;
}
static inline void renorm5(double& c0, double& c1, double& c2, double& c3, double& c4) {
  double s0, s1, s2 = 0.0, s3 = 0.0;
  if (std::isinf(c0)) return;
  s0 = qts(c3, c4, c4); s0 = qts(c2, s0, c3); s0 = qts(c1, s0, c2); c0 = qts(c0, s0, c1);
  s0 = c0; s1 = c1;
  s0 = qts(c0, c1, s1);
  if (s1 != 0.0) {
    s1 = qts(s1, c2, s2);
    if (s2 != 0.0) { s2 = qts(s2, c3, s3); if (s3 != 0.0) s3 += c4; else s2 = qts(s2, c4, s3); }
    else { s1 = qts(s1, c3, s2); if (s2 != 0.0) s2 = qts(s2, c4, s3); else s1 = qts(s1, c4, s2); }
  } else {
    s0 = qts(s0, c2, s1);
    if (s1 != 0.0) { s1 = qts(s1, c3, s2); if (s2 != 0.0) s2 = qts(s2, c4, s3); else s1 = qts(s1, c4, s2); }
    else { s0 = qts(s0, c3, s1); if (s1 != 0.0) s1 = qts(s1, c4, s2); else s0 = qts(s0, c4, s1); }
  }
  c0 = s0; c1 = s1; c2 = s2; c3 = s3;
}
static inline double quick_three_accum(double& a, double& b, double c) {
  double s; s = ts(b, c, b); s = ts(a, s, a);
  bool za = (a != 0.0), zb = (b != 0.0);
  if (za && zb) return s;
  if (!zb) { b = a; a = s; } else { a = s; }
  return 0.0;
}
}  // namespace qdi

static inline qd operator+(const qd& a, const qd& b) {
  using namespace qdi;
  int i = 0, j = 0, k = 0; double s, t, u, v; double x[4] = {0, 0, 0, 0};
  if (std::fabs(a[i]) > std::fabs(b[j])) u = a[i++]; else u = b[j++];
  if (i == 4) v = b[j++]; else if (j == 4) v = a[i++];
  else if (std::fabs(a[i]) > std::fabs(b[j])) v = a[i++]; else v = b[j++];
  u = qts(u, v, v);
  while (k < 4) {
    if (i >= 4 && j >= 4) { x[k] = u; if (k < 3) x[++k] = v; break; }
    if (i >= 4) t = b[j++]; else if (j >= 4) t = a[i++];
    else if (std::fabs(a[i]) > std::fabs(b[j])) t = a[i++]; else t = b[j++];
    s = quick_three_accum(u, v, t);
    if (s != 0.0) x[k++] = s;
  }
  for (k = i; k < 4; k++) x[3] += a[k];
  for (k = j; k < 4; k++) x[3] += b[k];
  renorm4(x[0], x[1], x[2], x[3]);
  return qd(x[0], x[1], x[2], x[3]);
}
static inline qd operator-(const qd& a) { return qd(-a.hi, -a.l1, -a.l2, -a.l3); }
static inline qd operator-(const qd& a, const qd& b) { return a + (-b); }
static inline qd operator*(const qd& a, const qd& b) {
  using namespace qdi;
  double p0, p1, p2, p3, p4, p5, q0, q1, q2, q3, q4, q5, p6, p7, p8, p9, q6, q7, q8, q9, r0, r1, t0, t1, s0, s1, s2;
  p0 = tp(a.hi, b.hi, q0); p1 = tp(a.hi, b.l1, q1); p2 = tp(a.l1, b.hi, q2);
  p3 = tp(a.hi, b.l2, q3); p4 = tp(a.l1, b.l1, q4); p5 = tp(a.l2, b.hi, q5);
  three_sum(p1, p2, q0);
  three_sum(p2, q1, q2); three_sum(p3, p4, p5);
  s0 = ts(p2, p3, t0); s1 = ts(q1, p4, t1); s2 = q2 + p5; s1 = ts(s1, t0, t0); s2 += (t0 + t1);
  p6 = tp(a.hi, b.l3, q6); p7 = tp(a.l1, b.l2, q7); p8 = tp(a.l2, b.l1, q8); p9 = tp(a.l3, b.hi, q9);
  q0 = ts(q0, q3, q3); q4 = ts(q4, q5, q5); p6 = ts(p6, p7, p7); p8 = ts(p8, p9, p9);
  t0 = ts(q0, q4, t1); t1 += (q3 + q5);
  r0 = ts(p6, p8, r1); r1 += (p7 + p9);
  q3 = ts(t0, r0, q4); q4 += (t1 + r1);
  t0 = ts(q3, s1, t1); t1 += q4;
  t1 += a.l1 * b.l3 + a.l2 * b.l2 + a.l3 * b.l1 + q6 + q7 + q8 + q9 + s2;
  renorm5(p0, p1, s0, t0, t1);
  return qd(p0, p1, s0, t0);
}
static inline qd operator*(const qd& a, double b) { return a * qd(b); }
static inline qd operator*(double b, const qd& a) { return a * qd(b); }
static inline qd operator/(const qd& a, const qd& b) {
  double q0 = a.hi / b.hi; qd r = a - b * q0;
  double q1 = r.hi / b.hi; r = r - b * q1;
  double q2 = r.hi / b.hi; r = r - b * q2;
  double q3 = r.hi / b.hi; r = r - b * q3;
  double q4 = r.hi / b.hi;
  qdi::renorm5(q0, q1, q2, q3, q4);
  return qd(q0, q1, q2, q3);
}
static inline qd& operator+=(qd& a, const qd& b) { a = a + b; return a; }
static inline qd& operator-=(qd& a, const qd& b) { a = a - b; return a; }
static inline qd& operator*=(qd& a, const qd& b) { a = a * b; return a; }
static inline qd& operator/=(qd& a, const qd& b) { a = a / b; return a; }
static inline bool operator<(const qd& a, const qd& b) {
  return a.hi < b.hi || (a.hi == b.hi && (a.l1 < b.l1 || (a.l1 == b.l1 && (a.l2 < b.l2 || (a.l2 == b.l2 && a.l3 < b.l3)))));
}
static inline bool operator>(const qd& a, const qd& b) { return b < a; }
static inline double to_double(const qd& a) { return a.hi + a.l1; }
static inline qd qdabs(const qd& a) { return a.hi < 0 ? -a : a; }
static inline qd ldexp(const qd& a, int e) { return qd(std::ldexp(a.hi, e), std::ldexp(a.l1, e), std::ldexp(a.l2, e), std::ldexp(a.l3, e)); }

static const qd QD_PI(3.14159265358979312e+00, 1.22464679914735321e-16, -2.99476980971833967e-33, 1.11245422086336528e-49);
static const qd QD_LN2(6.93147180559945286e-01, 2.31904681384629956e-17, 5.70770843841621207e-34, -3.58243221060181142e-50);

static inline qd sqrt(const qd& a) {
  if (a.hi <= 0) return qd(0.0);
  qd r(1.0 / std::sqrt(a.hi)), h = ldexp(a, -1);
  for (int i = 0; i < 3; i++) r = r + r * (qd(0.5) - h * r * r);
  return a * r;
}
static inline qd expm1_small(const qd& r) {
  qd s = r, t = r; double eps = 1e-67 * std::fabs(r.hi);
  for (int k = 2; k < 80; k++) { t = t * r / qd((double)k); s = s + t; if (std::fabs(t.hi) < eps) break; }
  return s;
}
static inline qd exp(const qd& a) {
  if (a.hi > 709) return qd(INFINITY);
  if (a.hi < -745) return qd(0.0);
  double k = std::floor(a.hi / QD_LN2.hi + 0.5);
  qd r = ldexp(a - QD_LN2 * k, -12);
  qd e = expm1_small(r);
  for (int i = 0; i < 12; i++) e = e * (e + qd(2.0));
  return ldexp(e + qd(1.0), (int)k);
}
static inline qd expm1(const qd& a) {
  if (std::fabs(a.hi) > 0.5) return exp(a) - qd(1.0);
  qd e = expm1_small(ldexp(a, -12));
  for (int i = 0; i < 12; i++) e = e * (e + qd(2.0));
  return e;
}
static inline qd log(const qd& a) {
  if (a.hi <= 0) return qd(NAN);
  qd x(std::log(a.hi));
  for (int i = 0; i < 3; i++) x = x + a * exp(-x) - qd(1.0);
  return x;
}
static inline qd log1p(const qd& a) {
  qd x(std::log1p(a.hi));
  for (int i = 0; i < 3; i++) { qd e = expm1(x); x = x - (e - a) / (e + qd(1.0)); }
  return x;
}
static inline void sincos_small(const qd& r, qd& s, qd& c) {
  qd r2 = r * r, t = r; s = r; double eps = 1e-67;
  for (int k = 3; k < 100; k += 2) { t = -t * r2 / qd((double)((k - 1) * k)); s = s + t; if (std::fabs(t.hi) < eps * std::fabs(s.hi)) break; }
  t = qd(1.0); c = qd(1.0);
  for (int k = 2; k < 100; k += 2) { t = -t * r2 / qd((double)((k - 1) * k)); c = c + t; if (std::fabs(t.hi) < eps) break; }
}
static inline void sincos(const qd& a, qd& s, qd& c) {
  qd hp = ldexp(QD_PI, -1);
  double k = std::floor(a.hi / hp.hi + 0.5);
  qd r = a - hp * k;
  // halve twice for faster series, then double-angle back
  qd rr = ldexp(r, -2), ss, cc; sincos_small(rr, ss, cc);
  for (int i = 0; i < 2; i++) { qd s2 = qd(2.0) * ss * cc, c2 = cc * cc - ss * ss; ss = s2; cc = c2; }
  int q = ((long)k % 4 + 4) % 4;
  if (q == 0) { s = ss; c = cc; } else if (q == 1) { s = cc; c = -ss; } else if (q == 2) { s = -ss; c = -cc; } else { s = -cc; c = ss; }
}
static inline qd sin(const qd& a) { qd s, c; sincos(a, s, c); return s; }
static inline qd cos(const qd& a) { qd s, c; sincos(a, s, c); return c; }
static inline qd sinh(const qd& a) {
  if (std::fabs(a.hi) < 0.5) { qd e = expm1(a); return ldexp(e * (e + qd(2.0)) / (e + qd(1.0)), -1); }
  qd e = exp(a); return ldexp(e - qd(1.0) / e, -1);
}
static inline qd cosh(const qd& a) { qd e = exp(a); return ldexp(e + qd(1.0) / e, -1); }
static inline qd asinh(const qd& a) { qd x(std::asinh(a.hi)); for (int i = 0; i < 3; i++) x = x - (sinh(x) - a) / cosh(x); return x; }
static inline qd qd_from_string(const char* s) {
  bool neg = false; const char* p = s; while (*p == ' ') p++;
  if (*p == '-') { neg = true; p++; } else if (*p == '+') p++;
  qd r(0.0); int e10 = 0; bool frac = false;
  for (; *p; p++) {
    if (*p == '.') { frac = true; continue; }
    if (*p == 'e' || *p == 'E') { e10 += atoi(p + 1); break; }
    if (*p < '0' || *p > '9') break;
    r = r * qd(10.0) + qd((double)(*p - '0')); if (frac) e10--;
  }
  qd pw(1.0); int ae = e10 < 0 ? -e10 : e10; for (int i = 0; i < ae; i++) pw = pw * qd(10.0);
  r = e10 < 0 ? r / pw : r * pw;
  return neg ? -r : r;
}
static inline std::string qd_to_string(const qd& a, int digits = 64) {
  if (a.hi == 0) return "0";
  qd x = qdabs(a); int e = (int)std::floor(std::log10(x.hi));
  qd pw(1.0); for (int i = 0; i < std::abs(e); i++) pw = pw * qd(10.0);
  x = e >= 0 ? x / pw : x * pw;
  while (x.hi >= 10) { x = x / qd(10.0); e++; } while (x.hi < 1) { x = x * qd(10.0); e--; }
  std::string s = a.hi < 0 ? "-" : "";
  for (int i = 0; i < digits; i++) { int d = (int)std::floor(x.hi); if (d > 9) d = 9; if (d < 0) d = 0; s += char('0' + d); if (i == 0) s += '.'; x = (x - qd((double)d)) * qd(10.0); }
  char buf[16]; snprintf(buf, sizeof buf, "e%+d", e); return s + buf;
}
