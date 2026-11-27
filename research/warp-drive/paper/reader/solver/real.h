// real.h: the working precision.  Default double-double; -DUSE_QD selects quad-double.
#pragma once
#ifdef USE_QD
#include "dd.h"
#include "qd.h"
typedef qd Real;
static const int NW = 4;                      // doubles per value
static inline Real R_from_string(const char* s) { return qd_from_string(s); }
static inline std::string R_to_string(const Real& a) { return qd_to_string(a); }
static const Real R_PI = QD_PI;
static inline double lead2(const Real& a) { return a.hi + a.l1; }
static inline double lo1(const Real& a) { return a.l1; }
static inline bool req(const Real& a, const Real& b) { return a.hi == b.hi && a.l1 == b.l1 && a.l2 == b.l2 && a.l3 == b.l3; }
static inline Real from_parts(const double* p) { return qd(p[0], p[1], p[2], p[3]); }
static inline void to_parts(const Real& a, double* p) { p[0] = a.hi; p[1] = a.l1; p[2] = a.l2; p[3] = a.l3; }
#else
#include "dd.h"
typedef dd Real;
static const int NW = 2;
static inline Real R_from_string(const char* s) { return dd_from_string(s); }
static inline std::string R_to_string(const Real& a) { return dd_to_string(a); }
static const Real R_PI = DD_PI;
static inline double lead2(const Real& a) { return a.hi + a.lo; }
static inline double lo1(const Real& a) { return a.lo; }
static inline bool req(const Real& a, const Real& b) { return a.hi == b.hi && a.lo == b.lo; }
static inline Real from_parts(const double* p) { return dd(p[0], p[1]); }
static inline void to_parts(const Real& a, double* p) { p[0] = a.hi; p[1] = a.lo; }
#endif
