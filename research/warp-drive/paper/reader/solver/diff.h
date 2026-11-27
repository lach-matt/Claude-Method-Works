// diff.h: difference arithmetic around a reference state.  A Diff holds (s, d): the reference value s and the
// perturbation d, the represented value being s + d.  Operations propagate d without forming (s + d) - s, so the
// perturbation of a result is obtained with a relative error of a few units of the working precision even where it
// is many orders below the reference values (no cancellation).  The plain type C (constants, x) has d = 0.
#pragma once
template<class C> struct Diff {
  C s, d;
  Diff() {}
  Diff(const C& a) : s(a), d(0.0) {}
  Diff(const C& a, const C& b) : s(a), d(b) {}
};
template<class C> inline Diff<C> operator+(const Diff<C>& a, const Diff<C>& b) { return Diff<C>(a.s + b.s, a.d + b.d); }
template<class C> inline Diff<C> operator-(const Diff<C>& a, const Diff<C>& b) { return Diff<C>(a.s - b.s, a.d - b.d); }
template<class C> inline Diff<C> operator-(const Diff<C>& a) { return Diff<C>(-a.s, -a.d); }
inline bool dz_(double a) { return a == 0; }
template<class C> inline bool dz_(const C& a) { return a.hi == 0; }   // normalized: leading part 0 means 0
template<class C> inline Diff<C> operator*(const Diff<C>& a, const Diff<C>& b) {
  // the reference parts of the fields without a seed value (m, n, s and the x-derivatives) are exactly zero:
  // skip the products that vanish
  const bool za = dz_(a.s), zb = dz_(b.s);
  if (za && zb) return Diff<C>(a.s, a.d * b.d);
  if (za) return Diff<C>(a.s, a.d * (b.s + b.d));
  if (zb) return Diff<C>(b.s, a.s * b.d + a.d * b.d);
  return Diff<C>(a.s * b.s, a.s * b.d + a.d * (b.s + b.d));
}

template<class C> inline Diff<C> operator+(const Diff<C>& a, const C& c) { return Diff<C>(a.s + c, a.d); }
template<class C> inline Diff<C> operator+(const C& c, const Diff<C>& a) { return Diff<C>(c + a.s, a.d); }
template<class C> inline Diff<C> operator-(const Diff<C>& a, const C& c) { return Diff<C>(a.s - c, a.d); }
template<class C> inline Diff<C> operator-(const C& c, const Diff<C>& a) { return Diff<C>(c - a.s, -a.d); }
template<class C> inline Diff<C> operator*(const Diff<C>& a, const C& c) { return Diff<C>(a.s * c, a.d * c); }
template<class C> inline Diff<C> operator*(const C& c, const Diff<C>& a) { return Diff<C>(c * a.s, c * a.d); }
