// solver.cpp: characteristic cell-marching solver for the 5D Einstein vacuum class in double-null gauge, in
// double-double arithmetic, for the reader's edition's certified approximant (Appendix C).
// See README.md for the formulation, the build, the run, resume and the outputs.
#include "dd.h"
#include "diff.h"
#include "rhs_gen.h"
#include <omp.h>
#include <vector>
#include <map>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <chrono>
#include <cstring>
#include <algorithm>
#include <type_traits>

typedef dd Real;
typedef Diff<Real> DR;
static const int NF = 5;                 // R, m, n, W, s
enum { FR = 0, FM = 1, FN = 2, FW = 3, FS = 4 };

// ------------------------------------------------------------------------------------------------ constants
struct Mat { int r = 0, c = 0; std::vector<Real> a; const Real& operator()(int i, int j) const { return a[i * c + j]; } };
static std::map<std::string, Mat> CONST;
static void load_consts(const std::string& fn) {
  std::ifstream f(fn, std::ios::binary);
  if (!f) { fprintf(stderr, "cannot open %s\n", fn.c_str()); exit(1); }
  while (true) {
    char name[17] = {0}; if (!f.read(name, 16)) break;
    int rc[2]; f.read((char*)rc, 8);
    Mat m; m.r = rc[0]; m.c = rc[1]; m.a.resize((size_t)m.r * m.c);
    for (auto& x : m.a) { double hl[2]; f.read((char*)hl, 16); x = dd(hl[0], hl[1]); }
    CONST[name] = m;
  }
}
static const Mat& C_(const std::string& n) {
  auto it = CONST.find(n); if (it == CONST.end()) { fprintf(stderr, "missing constant %s\n", n.c_str()); exit(1); }
  return it->second;
}

// ------------------------------------------------------------------------------------------------ configuration
struct Elem { Real xlo, xhi, vlo, vhi; int Nt, Ns; std::vector<Real> xin, vin; };
struct Config {
  Real lam = 1.0, amp = 1.0; int pxi = 12, pv = 16, M = 32;
  std::string consts, out; Real xi_lo, xi_hi, v_lo, v_hi;
  int ncol[2] = {10, 1}, nrow[2] = {10, 1};       // [0]: away from the corner in +xi / +v; [1]: the other side
  std::vector<Real> xib[2], vbk[2];                // optional explicit breakpoints (from the corner outward)
  std::vector<Elem> el; int maxit = 80; double tol = 1e-33; double ckpt_min = 20; std::string quads = "1234";
  int threads = 4; int stopcol = -1;
};
static Config CF;
static Real A_CH;                                   // 1/500
static Real XI_N1, V_N0;                            // xi(-10), 1/2

static void read_config(const std::string& fn) {
  std::ifstream f(fn); std::string line;
  while (std::getline(f, line)) {
    std::istringstream is(line); std::string k; if (!(is >> k) || k[0] == '#') continue;
    std::string a, b, c, d;
    if (k == "lam") { is >> a; CF.lam = dd_from_string(a.c_str()); }
    else if (k == "amp") { is >> a; CF.amp = dd_from_string(a.c_str()); }
    else if (k == "pxi") is >> CF.pxi; else if (k == "pv") is >> CF.pv; else if (k == "M") is >> CF.M;
    else if (k == "consts") is >> CF.consts; else if (k == "out") is >> CF.out;
    else if (k == "domain") { is >> a >> b >> c >> d; CF.xi_lo = dd_from_string(a.c_str()); CF.xi_hi = dd_from_string(b.c_str());
      CF.v_lo = dd_from_string(c.c_str()); CF.v_hi = dd_from_string(d.c_str()); }
    else if (k == "cells") is >> CF.ncol[0] >> CF.ncol[1] >> CF.nrow[0] >> CF.nrow[1];
    else if (k == "xibreaks" || k == "vbreaks") { int side, n; is >> side >> n; auto& vv = (k == "xibreaks" ? CF.xib : CF.vbk)[side];
      vv.clear(); for (int i = 0; i < n; i++) { is >> a; vv.push_back(dd_from_string(a.c_str())); } }
    else if (k == "elem") { Elem e; is >> a >> b >> c >> d >> e.Nt >> e.Ns; e.xlo = dd_from_string(a.c_str());
      e.xhi = dd_from_string(b.c_str()); e.vlo = dd_from_string(c.c_str()); e.vhi = dd_from_string(d.c_str()); CF.el.push_back(e); }
    else if (k == "maxit") is >> CF.maxit; else if (k == "tol") is >> CF.tol; else if (k == "ckpt_minutes") is >> CF.ckpt_min;
    else if (k == "quadrants") is >> CF.quads; else if (k == "threads") is >> CF.threads; else if (k == "stopcol") is >> CF.stopcol;
  }
}

// ------------------------------------------------------------------------------------------------ the seed
struct Seed { Real R, Ru, Rv, Wv, OM2, dudxi; };
static Seed seed_at(const Real& xi, const Real& v) {
  Real up1 = A_CH * sinh(xi);              // u + 1 (exact in the chart, no cancellation near the horizon)
  Real u = up1 - dd(1.0);
  Real H = v - dd(2.0) * u + log(up1 / (up1 - dd(2.0)));
  double Hd = to_double(H), lo = 1 + 1e-14, hi = Hd / 2 + 3;
  for (int i = 0; i < 200; i++) { double mid = 0.5 * (lo + hi); double g = 2 * mid + std::log((mid - 1) / (mid + 1)); if (g < Hd) lo = mid; else hi = mid; }
  Real R(0.5 * (lo + hi));
  for (int i = 0; i < 3; i++) { Real g = dd(2.0) * R + log((R - dd(1.0)) / (R + dd(1.0))); R = R - (g - H) / (dd(2.0) + dd(2.0) / (R * R - dd(1.0))); }
  Seed s; s.R = R;
  Real f = dd(1.0) - dd(1.0) / (R * R), g = dd(1.0) - dd(1.0) / (u * u);
  s.Rv = f * dd(0.5); s.Ru = -f / g; s.OM2 = f / (dd(2.0) * g); s.Wv = dd(0.5) / (R * R * R);
  s.dudxi = A_CH * cosh(xi);
  return s;
}

// ------------------------------------------------------------------------------------------------ data on N1
// m = h phi cos(theta), n = h phi sin(theta), phi = (lam/2) amp r^-3/2 env(v), theta = v/lam, r = R_seed(-10, v),
// env = sin^4(pi (v - 1/2)/3) continued analytically (no cut-off).  Returned as G = F/eps^4 and F_v/eps^3.
struct MNdata { Real gm, gn, mv3, nv3; };
static MNdata mn_data(const Real& v, const Real& x, const Real& r) {
  Real eps = v - V_N0, z = DD_PI * eps / dd(3.0);
  Real sz, cz; sincos(z, sz, cz);
  Real sc = (DD_PI / dd(3.0)) * (std::fabs(z.hi) > 0 ? sz / z : dd(1.0));   // sin(pi eps/3)/eps
  Real h = sqrt(dd(2.0) / (dd(1.0) + x * x));
  Real st, ct; sincos(v / CF.lam, st, ct);
  Real r32 = dd(1.0) / (r * sqrt(r));
  Real pre = h * CF.lam * dd(0.5) * CF.amp * r32;
  Real sc2 = sc * sc, sc3 = sc2 * sc, sc4 = sc2 * sc2;
  Real f = dd(1.0) - dd(1.0) / (r * r);
  MNdata o; o.gm = pre * sc4 * ct; o.gn = pre * sc4 * st;
  // d/dv (r^-3/2 env cos) / eps^3 = r^-3/2 [ -(3/4) f/r eps sc^4 cos + (4pi/3) sc^3 cos(z) cos - eps sc^4 sin/lam ]
  Real a1 = -dd(0.75) * f / r * eps * sc4, a2 = dd(4.0) * DD_PI / dd(3.0) * sc3 * cz, a3 = eps * sc4 / CF.lam;
  o.mv3 = pre * ((a1 + a2) * ct - a3 * st);
  o.nv3 = pre * ((a1 + a2) * st + a3 * ct);
  return o;
}

// ------------------------------------------------------------------------------------------------ grids
static std::vector<Real> XN;            // x-nodes
static int NX;                          // M + 1
static const Mat *D1x, *D2x;

static std::vector<Real> breaks(const Real& start, const Real& end, int n, const std::vector<Real>& explicit_) {
  if (!explicit_.empty()) { std::vector<Real> b = explicit_; return b; }
  std::vector<Real> b(n + 1);
  for (int i = 0; i <= n; i++) b[i] = start + (end - start) * dd((double)i) / dd((double)n);
  return b;
}

struct Geom {
  std::vector<Real> xi, v;              // node coordinates, ordered from the start (corner side)
  Real hxi, hv;                         // signed half-widths (end - start)/2
  bool first;                           // adjacent to N0: Radau nodes in v, G-form update
  const Mat *Qx, *Dx, *Qv, *Dv, *W4, *V4, *TT, *wx, *wv;
  int nA, nB;
};
static Geom make_geom(const Real& x0, const Real& x1, const Real& v0, const Real& v1, bool first) {
  Geom g; g.first = first;
  std::string L = "L" + std::to_string(CF.pxi), Lv = "L" + std::to_string(CF.pv), Rv = "R" + std::to_string(CF.pv);
  g.Qx = &C_(L + "_Q"); g.Dx = &C_(L + "_D"); g.wx = &C_(L + "_w");
  const Mat& tx = C_(L + "_t");
  g.nA = CF.pxi + 1; g.hxi = (x1 - x0) * dd(0.5);
  for (int a = 0; a < g.nA; a++) g.xi.push_back(x0 + g.hxi * (tx.a[a] + dd(1.0)));
  std::string vs = first ? Rv : Lv;
  g.Qv = &C_(vs + "_Q"); g.Dv = &C_(vs + "_D"); g.wv = &C_(vs + "_w");
  g.W4 = first ? &C_(Rv + "_W4") : nullptr; g.V4 = first ? &C_(Rv + "_V4") : nullptr; g.TT = first ? &C_(Rv + "_TT") : nullptr;
  const Mat& tv = C_(vs + "_t");
  g.nB = CF.pv + 1; g.hv = (v1 - v0) * dd(0.5);
  for (int b = 0; b < g.nB; b++) g.v.push_back(v0 + g.hv * (tv.a[b] + dd(1.0)));
  return g;
}

// ------------------------------------------------------------------------------------------------ RHS indices
static int JI[RHS_NJ];
static std::vector<Real> KC;
static int jidx(const char* n) { for (int i = 0; i < RHS_NJ; i++) if (!strcmp(RHS_JET[i], n)) return i; fprintf(stderr, "no jet %s\n", n); exit(1); }
enum { jR, jiR, jES, jiES, jOM2, jiOM2, jRu, jRv, jRx, jRxx, jRvx, jWv, jWx, jWxx, jWvx, jm_, jmu, jmv, jmx, jmxx, jmvx,
       jn_, jnu, jnv, jnx, jnxx, jnvx, js_, jsv, jsx, jsvx, jEND };
static const char* JN[] = {"R", "iR", "ES", "iES", "OM2", "iOM2", "R_u", "R_v", "R_x", "R_xx", "R_vx", "W_v", "W_x", "W_xx", "W_vx",
  "m", "m_u", "m_v", "m_x", "m_xx", "m_vx", "n", "n_u", "n_v", "n_x", "n_xx", "n_vx", "s", "s_v", "s_x", "s_vx"};

// ------------------------------------------------------------------------------------------------ x-derivatives
// out[row][k] = sum_l D[k][l] in[row][l]
static void xapply(const Mat& D, const Real* in, Real* out, int rows) {
  #pragma omp parallel for schedule(static)
  for (int r = 0; r < rows; r++) {
    const Real* g = in + (size_t)r * NX; Real* o = out + (size_t)r * NX;
    for (int k = 0; k < NX; k++) {
      const Real* d = &D.a[(size_t)k * NX];
      Real s(0.0); for (int l = 0; l < NX; l++) s += d[l] * g[l];
      o[k] = s;
    }
  }
}

// ------------------------------------------------------------------------------------------------ one cell
// The cell problem is the fixed point G = P(G) := B + I[Psi(G)], B the Goursat boundary terms, I the integration
// operators, Psi the right-hand sides.  Defect correction: r = P(G) - G in double-double (Psi in difference
// arithmetic about the seed), then the correction d = r + I[Psi(G + d) - Psi(G)] by Picard sweeps in double, the
// bracket in difference arithmetic about the current state, and G <- G + d.  Each outer step gains about the
// precision of double; the converged G is a fixed point of the double-double map.
struct Edge { std::vector<Real> G; std::vector<Real> sv; };  // G[f][node][k] (f over NF), sv[node][k]
struct CellOut { int sweeps; int outer; double last; double secs; };

static inline size_t IX(int a, int b, int k, int nB) { return ((size_t)a * nB + b) * NX + k; }
static inline double D_(const Real& a) { return a.hi; }
static inline double D_(double a) { return a; }

template<class T> struct Work { std::vector<T> Gx, Gxx, Gxi, Gv, Gvx, Psi, Phi; };

static std::vector<double> D1d, D2d;   // x-derivative matrices in double
template<class T> static void xapplyT(const T* Dm, const T* in, T* out, int rows) {
  #pragma omp parallel for schedule(static)
  for (int r = 0; r < rows; r++) {
    const T* g = in + (size_t)r * NX; T* o = out + (size_t)r * NX;
    for (int k = 0; k < NX; k++) { const T* d = Dm + (size_t)k * NX; T s(0.0); for (int l = 0; l < NX; l++) s += d[l] * g[l]; o[k] = s; }
  }
}
template<class T> static void derivs(const Geom& g, const std::vector<T>& G, Work<T>& w, const T* D1, const T* D2) {
  const int nA = g.nA, nB = g.nB; const size_t NN = (size_t)nA * nB * NX;
  w.Gv.resize(NF * NN); w.Gxi.resize(3 * NN); w.Gx.resize(NF * NN); w.Gxx.resize(4 * NN); w.Gvx.resize(NF * NN);
  T ihv = T(1.0) / T(g.hv), ihx = T(1.0) / T(g.hxi);
  std::vector<T> Dv(nB * nB), Dx(nA * nA);
  for (int i = 0; i < nB * nB; i++) Dv[i] = T(g.Dv->a[i]);
  for (int i = 0; i < nA * nA; i++) Dx[i] = T(g.Dx->a[i]);
  #pragma omp parallel for collapse(2) schedule(static)
  for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) {
    for (int f = 0; f < NF; f++) for (int k = 0; k < NX; k++) {
      T sv(0.0); for (int bb = 0; bb < nB; bb++) sv += Dv[b * nB + bb] * G[f * NN + IX(a, bb, k, nB)];
      w.Gv[f * NN + IX(a, b, k, nB)] = sv * ihv;
      if (f < 3) { T sx(0.0); for (int aa = 0; aa < nA; aa++) sx += Dx[a * nA + aa] * G[f * NN + IX(aa, b, k, nB)];
                   w.Gxi[f * NN + IX(a, b, k, nB)] = sx * ihx; }
    }
  }
  xapplyT(D1, G.data(), w.Gx.data(), NF * nA * nB);
  xapplyT(D2, G.data(), w.Gxx.data(), 4 * nA * nB);
  xapplyT(D1, w.Gv.data(), w.Gvx.data(), NF * nA * nB);
}
static inline Real Rcast(double a) { return dd(a); }
// the D-jets (perturbation of the fields) at a node from G and its derivative arrays, eps-weights e3 = eps^3, e4 = eps^4
template<class T> struct DJ { T D[NF], Du[3], Dv[NF], Dx[NF], Dxx[4], Dvx[NF]; };
template<class T> static inline void djets(const std::vector<T>& G, const Work<T>& w, size_t NN, size_t idx, const T& e3, const T& e4,
                                           const T& iu, DJ<T>& o) {
  for (int f = 0; f < NF; f++) {
    o.D[f] = e4 * G[f * NN + idx]; o.Dx[f] = e4 * w.Gx[f * NN + idx];
    o.Dv[f] = T(4.0) * e3 * G[f * NN + idx] + e4 * w.Gv[f * NN + idx];
    o.Dvx[f] = T(4.0) * e3 * w.Gx[f * NN + idx] + e4 * w.Gvx[f * NN + idx];
    if (f < 4) o.Dxx[f] = e4 * w.Gxx[f * NN + idx];
    if (f < 3) o.Du[f] = e4 * w.Gxi[f * NN + idx] * iu;
  }
}
// reference (full) state as plain values: R, iR, ES, iES, OM2, iOM2, R_u, R_v, W_v and the field jets
template<class T> static inline void rhs_node(const T ref[jEND], const DJ<T>& d, const T& x, T out[5]) {
  // difference arithmetic about ref: ref holds the full values of every jet at the reference state
  typedef Diff<T> DT; DT J[jEND];
  const T Rt = ref[jR] + d.D[FR];
  J[jR] = DT(ref[jR], d.D[FR]); J[jiR] = DT(ref[jiR], -d.D[FR] * ref[jiR] / Rt);
  T Sd = ((T(1.0) + x) * d.D[FM] + (T(1.0) - x) * d.D[FN]) * T(1.0 / 3.0);
  if constexpr (std::is_same<T, Real>::value) Sd = ((dd(1.0) + x) * d.D[FM] + (dd(1.0) - x) * d.D[FN]) / dd(3.0);
  J[jES] = DT(ref[jES], ref[jES] * expm1(Sd)); J[jiES] = DT(ref[jiES], ref[jiES] * expm1(-Sd));
  J[jOM2] = DT(ref[jOM2], ref[jOM2] * expm1(T(2.0) * d.D[FW])); J[jiOM2] = DT(ref[jiOM2], ref[jiOM2] * expm1(T(-2.0) * d.D[FW]));
  J[jRu] = DT(ref[jRu], d.Du[FR]); J[jRv] = DT(ref[jRv], d.Dv[FR]); J[jRx] = DT(ref[jRx], d.Dx[FR]);
  J[jRxx] = DT(ref[jRxx], d.Dxx[FR]); J[jRvx] = DT(ref[jRvx], d.Dvx[FR]);
  J[jWv] = DT(ref[jWv], d.Dv[FW]); J[jWx] = DT(ref[jWx], d.Dx[FW]); J[jWxx] = DT(ref[jWxx], d.Dxx[FW]); J[jWvx] = DT(ref[jWvx], d.Dvx[FW]);
  for (int q = 0; q < 2; q++) {
    int f = q ? FN : FM; int o = q ? jn_ : jm_;
    J[o] = DT(ref[o], d.D[f]); J[o + 1] = DT(ref[o + 1], d.Du[f]); J[o + 2] = DT(ref[o + 2], d.Dv[f]);
    J[o + 3] = DT(ref[o + 3], d.Dx[f]); J[o + 4] = DT(ref[o + 4], d.Dxx[f]); J[o + 5] = DT(ref[o + 5], d.Dvx[f]);
  }
  J[js_] = DT(ref[js_], d.D[FS]); J[jsv] = DT(ref[jsv], d.Dv[FS]); J[jsx] = DT(ref[jsx], d.Dx[FS]); J[jsvx] = DT(ref[jsvx], d.Dvx[FS]);
  DT Jp[RHS_NJ]; for (int i = 0; i < jEND; i++) Jp[JI[i]] = J[i];
  DT o5[5];
  static thread_local std::vector<T> KT; if (KT.empty()) for (auto& k : KC) KT.push_back(T(D_(k)));
  if constexpr (std::is_same<T, Real>::value) rhs_eval(Jp, KC.data(), x, o5); else rhs_eval(Jp, KT.data(), x, o5);
  for (int i = 0; i < 5; i++) out[i] = o5[i].d;
}
static inline double expm1(double a) { return std::expm1(a); }

// the linear part of P: out = I[Psi, Phi] (no boundary terms)
template<class T> static void integrate(const Geom& g, const std::vector<T>& Psi, const std::vector<T>& Phi,
                                        const std::vector<T>& E, std::vector<T>& out) {
  const int nA = g.nA, nB = g.nB; const size_t NN = (size_t)nA * nB * NX;
  out.assign(NF * NN, T(0.0));
  std::vector<T> Qx(nA * nA), Mv(nB * nB), QQ(nB * nB);
  for (int i = 0; i < nA * nA; i++) Qx[i] = T(g.Qx->a[i]);
  const Mat& Wm = g.first ? *g.W4 : *g.Qv;
  for (int i = 0; i < nB * nB; i++) Mv[i] = T(Wm.a[i]);
  if (g.first) for (int i = 0; i < nB * nB; i++) QQ[i] = T(g.V4->a[i]);
  else for (int i = 0; i < nB; i++) for (int j = 0; j < nB; j++) { Real s(0.0); for (int l = 0; l < nB; l++) s += (*g.Qv)(i, l) * (*g.Qv)(l, j); QQ[i * nB + j] = T(D_(s) == 0 ? 0.0 : 0.0); QQ[i * nB + j] = T(0.0) + (T)(std::is_same<T, Real>::value ? T(0.0) : T(0.0)); }
  // exact QQ in the working type
  if (!g.first) for (int i = 0; i < nB; i++) for (int j = 0; j < nB; j++) { T s(0.0); for (int l = 0; l < nB; l++) s += T(g.Qv->a[i * nB + l]) * T(g.Qv->a[l * nB + j]); QQ[i * nB + j] = s; }
  T hx = T(g.hxi), hv = T(g.hv);
  std::vector<T> E3(nB), E4(nB), E2(nB);
  for (int b = 0; b < nB; b++) { E2[b] = E[b] * E[b]; E3[b] = E2[b] * E[b]; E4[b] = E3[b] * E[b]; }
  #pragma omp parallel for schedule(static)
  for (int f = 0; f < NF; f++) {
    std::vector<T> t1(NN, T(0.0));
    if (f < 4) {
      for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) {
        T s(0.0);
        for (int bb = 0; bb < nB; bb++) { T p = Psi[f * NN + IX(a, bb, k, nB)]; if (g.first) p = p / E3[bb]; s += Mv[b * nB + bb] * p; }
        t1[IX(a, b, k, nB)] = s;
      }
      T fac = g.first ? hx : hx * hv;
      for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) {
        T s(0.0); for (int aa = 0; aa < nA; aa++) s += Qx[a * nA + aa] * t1[IX(aa, b, k, nB)];
        out[f * NN + IX(a, b, k, nB)] = g.first ? fac * s : fac * s / E4[b];
      }
    } else {
      for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) {
        T s(0.0);
        for (int bb = 0; bb < nB; bb++) { T p = Phi[IX(a, bb, k, nB)]; if (g.first) p = p / E2[bb]; s += QQ[b * nB + bb] * p; }
        out[FS * NN + IX(a, b, k, nB)] = g.first ? s : hv * hv * s / E4[b];
      }
    }
  }
}

static CellOut solve_cell(const Geom& g, const Edge& left, const Edge* bottom, const Real& vb_bottom,
                          std::vector<Real>& G, std::vector<Real>& svTop) {
  auto t0 = std::chrono::steady_clock::now();
  const int nA = g.nA, nB = g.nB; const size_t NN = (size_t)nA * nB * NX;
  std::vector<Seed> sd((size_t)nA * nB);
  for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) sd[a * nB + b] = seed_at(g.xi[a], g.v[b]);
  std::vector<Real> E(nB), E3(nB), E4(nB); std::vector<double> Ed(nB), E3d(nB), E4d(nB);
  for (int b = 0; b < nB; b++) { E[b] = g.v[b] - V_N0; E3[b] = E[b] * E[b] * E[b]; E4[b] = E3[b] * E[b];
    Ed[b] = E[b].hi; E3d[b] = Ed[b] * Ed[b] * Ed[b]; E4d[b] = E3d[b] * Ed[b]; }
  Real eb = vb_bottom - V_N0, eb4 = eb * eb * eb * eb;
  // boundary terms B
  std::vector<Real> B(NF * NN, dd(0.0));
  for (int f = 0; f < NF; f++) for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) {
    Real val(0.0);
    if (g.first) { if (f < 4) val = left.G[((size_t)f * nB + b) * NX + k]; }
    else {
      Real Db = eb4 * bottom->G[((size_t)f * nA + a) * NX + k];
      if (f < 4) { Real Dl = E4[b] * left.G[((size_t)f * nB + b) * NX + k], Dc = eb4 * bottom->G[((size_t)f * nA + 0) * NX + k];
                   val = (Db + Dl - Dc) / E4[b]; }
      else val = (Db + (g.v[b] - vb_bottom) * bottom->sv[(size_t)a * NX + k]) / E4[b];
    }
    B[f * NN + IX(a, b, k, nB)] = val;
  }
  G = B;
  Work<Real> w; Work<double> wd;
  std::vector<Real> Psi(4 * NN), Phi(NN), IP;
  std::vector<double> Gd(NF * NN), dlt(NF * NN), r(NF * NN), Psid(4 * NN), Phid(NN), IPd, dn(NF * NN);
  CellOut co{0, 0, 1.0, 0.0};
  static bool verbose = getenv("BSOLV_VERBOSE") != nullptr;
  for (int outer = 0; outer < 12; outer++) {
    // residual in double-double, Psi about the seed
    derivs(g, G, w, D1x->a.data(), D2x->a.data());
    #pragma omp parallel for schedule(static)
    for (size_t idx = 0; idx < NN; idx++) {
      int k = idx % NX; size_t ab = idx / NX; int b = ab % nB;
      const Seed& s = sd[ab];
      Real ref[jEND]; for (int i = 0; i < jEND; i++) ref[i] = dd(0.0);
      ref[jR] = s.R; ref[jiR] = dd(1.0) / s.R; ref[jES] = dd(1.0); ref[jiES] = dd(1.0); ref[jOM2] = s.OM2; ref[jiOM2] = dd(1.0) / s.OM2;
      ref[jRu] = s.Ru; ref[jRv] = s.Rv; ref[jWv] = s.Wv;
      DJ<Real> d; djets(G, w, NN, idx, E3[b], E4[b], dd(1.0) / s.dudxi, d);
      Real o[5]; rhs_node(ref, d, XN[k], o);
      Psi[FR * NN + idx] = s.dudxi * o[2]; Psi[FM * NN + idx] = s.dudxi * o[0]; Psi[FN * NN + idx] = s.dudxi * o[1];
      Psi[FW * NN + idx] = s.dudxi * o[3]; Phi[idx] = o[4];
    }
    integrate(g, Psi, Phi, E, IP);
    double rmax = 0, gmax = 1e-300;
    for (size_t i = 0; i < NF * NN; i++) { Real ri = B[i] + IP[i] - G[i]; r[i] = ri.hi + ri.lo; rmax = std::max(rmax, std::fabs(r[i])); gmax = std::max(gmax, std::fabs(G[i].hi)); }
    co.outer = outer + 1; co.last = rmax / gmax;
    if (verbose) fprintf(stderr, "    outer %d: |P(G) - G|/|G| = %.2e\n", outer, rmax / gmax);
    if (rmax / gmax < CF.tol) { for (size_t i = 0; i < NF * NN; i++) G[i] = G[i] + dd(r[i]); break; }
    // inner: d = r + I[Psi(G + d) - Psi(G)] in double, difference arithmetic about the current state
    for (size_t i = 0; i < NF * NN; i++) Gd[i] = G[i].hi + G[i].lo;
    derivs(g, Gd, wd, D1d.data(), D2d.data());
    std::vector<double> refs((size_t)NN * jEND);
    #pragma omp parallel for schedule(static)
    for (size_t idx = 0; idx < NN; idx++) {
      int k = idx % NX; size_t ab = idx / NX; int b = ab % nB; const Seed& s = sd[ab];
      DJ<double> d; djets(Gd, wd, NN, idx, E3d[b], E4d[b], 1.0 / s.dudxi.hi, d);
      double* rf = &refs[idx * jEND]; double x = XN[k].hi;
      double R = s.R.hi + d.D[FR]; rf[jR] = R; rf[jiR] = 1.0 / R;
      double S = ((1 + x) * d.D[FM] + (1 - x) * d.D[FN]) / 3; rf[jES] = std::exp(S); rf[jiES] = std::exp(-S);
      rf[jOM2] = s.OM2.hi * std::exp(2 * d.D[FW]); rf[jiOM2] = 1.0 / rf[jOM2];
      rf[jRu] = s.Ru.hi + d.Du[FR]; rf[jRv] = s.Rv.hi + d.Dv[FR]; rf[jRx] = d.Dx[FR]; rf[jRxx] = d.Dxx[FR]; rf[jRvx] = d.Dvx[FR];
      rf[jWv] = s.Wv.hi + d.Dv[FW]; rf[jWx] = d.Dx[FW]; rf[jWxx] = d.Dxx[FW]; rf[jWvx] = d.Dvx[FW];
      for (int q = 0; q < 2; q++) { int f = q ? FN : FM; int o = q ? jn_ : jm_;
        rf[o] = d.D[f]; rf[o + 1] = d.Du[f]; rf[o + 2] = d.Dv[f]; rf[o + 3] = d.Dx[f]; rf[o + 4] = d.Dxx[f]; rf[o + 5] = d.Dvx[f]; }
      rf[js_] = d.D[FS]; rf[jsv] = d.Dv[FS]; rf[jsx] = d.Dx[FS]; rf[jsvx] = d.Dvx[FS];
    }
    dlt = r;
    double dprev = 1e300; int inner;
    for (inner = 0; inner < 400; inner++) {
      derivs(g, dlt, wd, D1d.data(), D2d.data());
      #pragma omp parallel for schedule(static)
      for (size_t idx = 0; idx < NN; idx++) {
        int k = idx % NX; size_t ab = idx / NX; int b = ab % nB; const Seed& s = sd[ab];
        DJ<double> d; djets(dlt, wd, NN, idx, E3d[b], E4d[b], 1.0 / s.dudxi.hi, d);
        double o[5]; rhs_node(&refs[idx * jEND], d, XN[k].hi, o);
        double du = s.dudxi.hi;
        Psid[FR * NN + idx] = du * o[2]; Psid[FM * NN + idx] = du * o[0]; Psid[FN * NN + idx] = du * o[1]; Psid[FW * NN + idx] = du * o[3]; Phid[idx] = o[4];
      }
      integrate(g, Psid, Phid, Ed, IPd);
      double dm = 0, dx = 1e-300;
      for (size_t i = 0; i < NF * NN; i++) { dn[i] = r[i] + IPd[i]; dm = std::max(dm, std::fabs(dn[i] - dlt[i])); dx = std::max(dx, std::fabs(dn[i])); }
      dlt.swap(dn);
      co.sweeps++;
      if (dm < 3e-17 * dx || (inner > 6 && dm > 0.7 * dprev && dm < 1e-14 * dx)) break;
      dprev = dm;
    }
    if (verbose) fprintf(stderr, "      inner sweeps %d\n", inner + 1);
    for (size_t i = 0; i < NF * NN; i++) G[i] = G[i] + dd(dlt[i]);
  }
  // s_v at the end v-node: s_v(bottom) + int Phi dv
  svTop.assign((size_t)nA * NX, dd(0.0));
  for (int a = 0; a < nA; a++) for (int k = 0; k < NX; k++) {
    Real s(0.0); for (int bb = 0; bb < nB; bb++) s += (*g.Qv)(nB - 1, bb) * Phi[IX(a, bb, k, nB)];
    svTop[(size_t)a * NX + k] = (g.first ? dd(0.0) : bottom->sv[(size_t)a * NX + k]) + g.hv * s;
  }
  co.secs = std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
  return co;
}

// ------------------------------------------------------------------------------------------------ N1 data
// For each row, G of R, m, n, W at the row's v-nodes on xi = xi(-10) (W: 0; R: Raychaudhuri with D_R = D_R,v = 0 at 1/2)
static void n1_row(const Geom& g, const std::vector<Real>& bottomGR, const std::vector<Real>& bottomRv, const Real& vb,
                   Edge& out, std::vector<Real>& topGR, std::vector<Real>& topRv) {
  const int nB = g.nB; std::vector<Real> E(nB), E4(nB);
  for (int b = 0; b < nB; b++) { E[b] = g.v[b] - V_N0; E4[b] = E[b] * E[b] * E[b] * E[b]; }
  out.G.assign((size_t)4 * nB * NX, dd(0.0));
  std::vector<Seed> sd(nB); for (int b = 0; b < nB; b++) sd[b] = seed_at(XI_N1, g.v[b]);
  Real eb = vb - V_N0, eb4 = eb * eb * eb * eb;
  std::vector<Real> GR((size_t)nB * NX, dd(0.0)), sh6((size_t)nB * NX);
  for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) {
    MNdata d = mn_data(g.v[b], XN[k], sd[b].R);
    out.G[((size_t)FM * nB + b) * NX + k] = d.gm; out.G[((size_t)FN * nB + b) * NX + k] = d.gn;
    const Real& x = XN[k];
    Real Pv = (dd(2.0) * (dd(1.0) + x) * d.mv3 - (dd(1.0) - x) * d.nv3) / dd(3.0);
    Real Qv = (dd(2.0) * (dd(1.0) - x) * d.nv3 - (dd(1.0) + x) * d.mv3) / dd(3.0);
    sh6[(size_t)b * NX + k] = Pv * Pv + Qv * Qv + (Pv + Qv) * (Pv + Qv);   // shear / eps^6
    if (!g.first) GR[(size_t)b * NX + k] = (eb4 * bottomGR[k] + (g.v[b] - vb) * bottomRv[k]) / E4[b];
  }
  std::vector<Real> rhs((size_t)nB * NX), GRn((size_t)nB * NX);
  for (int it = 0; it < 200; it++) {
    for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) {
      Real gv(0.0); for (int bb = 0; bb < nB; bb++) gv += (*g.Dv)(b, bb) * GR[(size_t)bb * NX + k];
      gv = gv / g.hv;
      Real DRv = dd(4.0) * E[b] * E[b] * E[b] * GR[(size_t)b * NX + k] + E4[b] * gv;
      Real Rt = sd[b].R + E4[b] * GR[(size_t)b * NX + k];
      // D_R,vv = 2 W_s,v D_R,v - R shear/3
      rhs[(size_t)b * NX + k] = dd(2.0) * sd[b].Wv * DRv - Rt * sh6[(size_t)b * NX + k] * E4[b] * E[b] * E[b] / dd(3.0);
    }
    double dm = 0, mx = 1e-300;
    for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) {
      Real val;
      if (g.first) { Real s(0.0); for (int bb = 0; bb < nB; bb++) s += (*g.V4)(b, bb) * (rhs[(size_t)bb * NX + k] / (E[bb] * E[bb])); val = s; }
      else {
        Real s1(0.0);   // double integral via Q Q
        for (int b1 = 0; b1 < nB; b1++) { Real s0(0.0); for (int bb = 0; bb < nB; bb++) s0 += (*g.Qv)(b1, bb) * rhs[(size_t)bb * NX + k]; s1 += (*g.Qv)(b, b1) * s0; }
        val = (eb4 * bottomGR[k] + (g.v[b] - vb) * bottomRv[k] + g.hv * g.hv * s1) / E4[b];
      }
      GRn[(size_t)b * NX + k] = val;
      dm = std::max(dm, std::fabs((val - GR[(size_t)b * NX + k]).hi)); mx = std::max(mx, std::fabs(val.hi));
    }
    GR.swap(GRn);
    if (dm < 1e-34 * mx || dm == 0) break;
  }
  for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) out.G[((size_t)FR * nB + b) * NX + k] = GR[(size_t)b * NX + k];
  // top: G_R at the end node and D_R,v there (D_R,v(end) = D_R,v(bottom) + int rhs dv)
  topGR.assign(NX, dd(0.0)); topRv.assign(NX, dd(0.0));
  for (int k = 0; k < NX; k++) {
    topGR[k] = GR[(size_t)(nB - 1) * NX + k];
    Real s(0.0); for (int bb = 0; bb < nB; bb++) s += (*g.Qv)(nB - 1, bb) * rhs[(size_t)bb * NX + k];
    topRv[k] = (g.first ? dd(0.0) : bottomRv[k]) + g.hv * s;
  }
}

// ------------------------------------------------------------------------------------------------ output sampling
static std::vector<std::vector<Real>> EOUT;    // per element: [f][a][b][k]
static std::vector<std::vector<char>> EDONE;    // per element: [a][b]
static void bary_weights(const std::vector<Real>& nodes, const Mat& w, const Real& t, std::vector<Real>& out) {
  int n = nodes.size(); out.assign(n, dd(0.0));
  for (int j = 0; j < n; j++) if (t.hi == nodes[j].hi && t.lo == nodes[j].lo) { out[j] = dd(1.0); return; }
  Real den(0.0);
  for (int j = 0; j < n; j++) { out[j] = w.a[j] / (t - nodes[j]); den += out[j]; }
  for (int j = 0; j < n; j++) out[j] = out[j] / den;
}
static void sample_cell(const Geom& g, const std::vector<Real>& G) {
  const size_t NN = (size_t)g.nA * g.nB * NX;
  Real xmin = std::min(g.xi.front(), g.xi.back(), [](const Real& a, const Real& b) { return a < b; });
  Real xmax = std::max(g.xi.front(), g.xi.back(), [](const Real& a, const Real& b) { return a < b; });
  Real vmin = std::min(g.v.front(), g.v.back(), [](const Real& a, const Real& b) { return a < b; });
  Real vmax = std::max(g.v.front(), g.v.back(), [](const Real& a, const Real& b) { return a < b; });
  if (g.first) { if (g.hv.hi > 0) vmin = V_N0; else vmax = V_N0; }
  for (size_t e = 0; e < CF.el.size(); e++) {
    const Elem& el = CF.el[e]; int nT = el.Nt + 1, nS = el.Ns + 1;
    for (int a = 0; a < nT; a++) {
      const Real& X = el.xin[a]; if (X < xmin || X > xmax) continue;
      std::vector<Real> wa; bary_weights(g.xi, *g.wx, X, wa);
      for (int b = 0; b < nS; b++) {
        const Real& V = el.vin[b]; if (V < vmin || V > vmax) continue;
        if (EDONE[e][(size_t)a * nS + b]) continue;
        std::vector<Real> wb; bary_weights(g.v, *g.wv, V, wb);
        for (int f = 0; f < NF; f++) for (int k = 0; k < NX; k++) {
          Real s(0.0);
          for (int aa = 0; aa < g.nA; aa++) { if (wa[aa].hi == 0) continue; Real s1(0.0);
            for (int bb = 0; bb < g.nB; bb++) s1 += wb[bb] * G[f * NN + IX(aa, bb, k, g.nB)]; s += wa[aa] * s1; }
          EOUT[e][(((size_t)f * nT + a) * nS + b) * NX + k] = s;
        }
        EDONE[e][(size_t)a * nS + b] = 1;
      }
    }
  }
}

// jets on N0 from the first-row cells: Taylor coefficients c_j (j = 0..8) of G in eps at eps = 0, i.e. of F in
// (v - 1/2)^(4 + j); per quadrant side, per column: [col][j][a][f][k]
static std::vector<Real> JETS[2]; static std::vector<std::vector<Real>> JETXI[2];
static void record_jets(int side, int col, const Geom& g, const std::vector<Real>& G) {
  const size_t NN = (size_t)g.nA * g.nB * NX; size_t per = (size_t)9 * g.nA * NF * NX;
  if (JETS[side].size() < (col + 1) * per) JETS[side].resize((col + 1) * per, dd(0.0));
  if ((int)JETXI[side].size() < col + 1) JETXI[side].resize(col + 1);
  JETXI[side][col] = g.xi;
  Real he = g.hv * dd(2.0);                     // eps = he * sigma
  for (int j = 0; j < 9; j++) {
    Real sc(1.0); for (int q = 0; q < j; q++) sc = sc * he;
    for (int a = 0; a < g.nA; a++) for (int f = 0; f < NF; f++) for (int k = 0; k < NX; k++) {
      Real s(0.0); for (int b = 0; b < g.nB; b++) s += (*g.TT)(j, b) * G[f * NN + IX(a, b, k, g.nB)];
      JETS[side][col * per + (((size_t)j * g.nA + a) * NF + f) * NX + k] = s / sc;
    }
  }
}

// ------------------------------------------------------------------------------------------------ checkpoint
template<class T> static void wvec(std::ofstream& f, const std::vector<T>& v) { size_t n = v.size(); f.write((char*)&n, 8); f.write((char*)v.data(), n * sizeof(T)); }
template<class T> static void rvec(std::ifstream& f, std::vector<T>& v) { size_t n; f.read((char*)&n, 8); v.resize(n); f.read((char*)v.data(), n * sizeof(T)); }
struct State { int quad_idx = 0, col = 0; std::vector<Edge> left; double cells = 0, secs = 0, sweeps = 0; };
static void save_ckpt(const State& st) {
  std::string fn = CF.out + ".ckpt", tmpf = fn + ".tmp";
  std::ofstream f(tmpf, std::ios::binary);
  f.write("BSOLV1", 6); f.write((char*)&st.quad_idx, 4); f.write((char*)&st.col, 4);
  f.write((char*)&st.cells, 8); f.write((char*)&st.secs, 8); f.write((char*)&st.sweeps, 8);
  int nl = st.left.size(); f.write((char*)&nl, 4);
  for (auto& e : st.left) { wvec(f, e.G); wvec(f, e.sv); }
  int ne = EOUT.size(); f.write((char*)&ne, 4);
  for (int e = 0; e < ne; e++) { wvec(f, EOUT[e]); wvec(f, EDONE[e]); }
  for (int s = 0; s < 2; s++) { wvec(f, JETS[s]); int n = JETXI[s].size(); f.write((char*)&n, 4); for (auto& v : JETXI[s]) wvec(f, v); }
  f.close(); std::rename(tmpf.c_str(), fn.c_str());
}
static bool load_ckpt(State& st) {
  std::ifstream f(CF.out + ".ckpt", std::ios::binary); if (!f) return false;
  char mg[6]; f.read(mg, 6); if (memcmp(mg, "BSOLV1", 6)) return false;
  f.read((char*)&st.quad_idx, 4); f.read((char*)&st.col, 4);
  f.read((char*)&st.cells, 8); f.read((char*)&st.secs, 8); f.read((char*)&st.sweeps, 8);
  int nl; f.read((char*)&nl, 4); st.left.resize(nl);
  for (auto& e : st.left) { rvec(f, e.G); rvec(f, e.sv); }
  int ne; f.read((char*)&ne, 4);
  for (int e = 0; e < ne; e++) { rvec(f, EOUT[e]); rvec(f, EDONE[e]); }
  for (int s = 0; s < 2; s++) { rvec(f, JETS[s]); int n; f.read((char*)&n, 4); JETXI[s].resize(n); for (auto& v : JETXI[s]) rvec(f, v); }
  return true;
}
static void write_output() {
  std::ofstream f(CF.out + ".elem", std::ios::binary);
  int ne = CF.el.size(); f.write("BSOLE1", 6); f.write((char*)&ne, 4); f.write((char*)&NX, 4);
  for (int e = 0; e < ne; e++) {
    int nt = CF.el[e].Nt, ns = CF.el[e].Ns; f.write((char*)&nt, 4); f.write((char*)&ns, 4);
    long nd = 0; for (char c : EDONE[e]) nd += c; f.write((char*)&nd, 8);
    wvec(f, EOUT[e]);
  }
  std::ofstream g(CF.out + ".jets", std::ios::binary);
  g.write("BSOLJ1", 6); int pa = CF.pxi + 1; g.write((char*)&pa, 4); g.write((char*)&NX, 4);
  for (int s = 0; s < 2; s++) { wvec(g, JETS[s]); int n = JETXI[s].size(); g.write((char*)&n, 4); for (auto& v : JETXI[s]) wvec(g, v); }
}

// ------------------------------------------------------------------------------------------------ the march
int main(int argc, char** argv) {
  if (argc < 2) { fprintf(stderr, "usage: solver config [--fresh]\n"); return 1; }
  read_config(argv[1]); bool fresh = argc > 2 && !strcmp(argv[2], "--fresh");
  omp_set_num_threads(CF.threads);
  load_consts(CF.consts);
  A_CH = dd(1.0) / dd(500.0); XI_N1 = asinh(dd(-9.0) / A_CH); V_N0 = dd(0.5);
  std::string X = "X" + std::to_string(CF.M);
  const Mat& xn = C_(X + "_x"); NX = CF.M + 1; XN.assign(xn.a.begin(), xn.a.end());
  D1x = &C_(X + "_D1"); D2x = &C_(X + "_D2");
  for (auto& q : D1x->a) D1d.push_back(q.hi + q.lo); for (auto& q : D2x->a) D2d.push_back(q.hi + q.lo);
  for (int i = 0; i < RHS_NJ; i++) JI[jidx(JN[i])] = 0;
  for (int i = 0; i < jEND; i++) JI[i] = jidx(JN[i]);
  for (int i = 0; i < RHS_NK; i++) KC.push_back(dd((double)RHS_KNUM[i]) / dd((double)RHS_KDEN[i]));
  for (auto& e : CF.el) {
    for (int a = 0; a <= e.Nt; a++) e.xin.push_back((e.xlo + e.xhi) * dd(0.5) - (e.xhi - e.xlo) * dd(0.5) * cos(DD_PI * dd((double)a) / dd((double)e.Nt)));
    for (int b = 0; b <= e.Ns; b++) e.vin.push_back((e.vlo + e.vhi) * dd(0.5) - (e.vhi - e.vlo) * dd(0.5) * cos(DD_PI * dd((double)b) / dd((double)e.Ns)));
    EOUT.push_back(std::vector<Real>((size_t)NF * (e.Nt + 1) * (e.Ns + 1) * NX, dd(0.0)));
    EDONE.push_back(std::vector<char>((size_t)(e.Nt + 1) * (e.Ns + 1), 0));
  }
  // breakpoints: side 0 = from the corner toward +xi (Q1, Q3) / +v (Q1, Q2); side 1 the other way
  std::vector<Real> xb[2] = {breaks(XI_N1, CF.xi_hi, CF.ncol[0], CF.xib[0]), breaks(XI_N1, CF.xi_lo, CF.ncol[1], CF.xib[1])};
  std::vector<Real> vb[2] = {breaks(V_N0, CF.v_hi, CF.nrow[0], CF.vbk[0]), breaks(V_N0, CF.v_lo, CF.nrow[1], CF.vbk[1])};
  // N1 data for both v sides
  std::vector<Edge> n1[2];
  for (int sv = 0; sv < 2; sv++) {
    int nr = vb[sv].size() - 1; if (nr <= 0) continue;
    std::vector<Real> bG, bRv; n1[sv].resize(nr);
    for (int j = 0; j < nr; j++) {
      Geom g = make_geom(XI_N1, XI_N1 + dd(1e-3), vb[sv][j], vb[sv][j + 1], j == 0);
      std::vector<Real> tG, tR; n1_row(g, bG, bRv, vb[sv][j], n1[sv][j], tG, tR); bG = tG; bRv = tR;
    }
  }
  State st; bool resumed = !fresh && load_ckpt(st);
  FILE* lg = fopen((CF.out + ".log").c_str(), resumed ? "a" : "w");
  fprintf(lg, "%s config %s, M = %d, pxi = %d, pv = %d, threads %d\n", resumed ? "RESUME" : "START", argv[1], CF.M, CF.pxi, CF.pv, CF.threads); fflush(lg);
  auto tlast = std::chrono::steady_clock::now();
  for (int qi = st.quad_idx; qi < (int)CF.quads.size(); qi++) {
    int q = CF.quads[qi] - '1';                     // 0: Q1 (+xi, +v), 1: Q2 (-xi, +v), 2: Q3 (+xi, -v), 3: Q4 (-xi, -v)
    int sx = (q == 1 || q == 3) ? 1 : 0, sv = (q >= 2) ? 1 : 0;
    int ncol = xb[sx].size() - 1, nrow = vb[sv].size() - 1;
    if (ncol <= 0 || nrow <= 0) { st.col = 0; st.left.clear(); continue; }
    if (!(resumed && qi == st.quad_idx)) { st.col = 0; st.left = n1[sv]; }
    resumed = false;
    for (int i = st.col; i < ncol; i++) {
      std::vector<Edge> right(nrow);
      Edge bottom; Real vbot = V_N0;
      double csec = 0, cmax = 0; int smax = 0;
      for (int j = 0; j < nrow; j++) {
        Geom g = make_geom(xb[sx][i], xb[sx][i + 1], vb[sv][j], vb[sv][j + 1], j == 0);
        std::vector<Real> G, svTop;
        CellOut co = solve_cell(g, st.left[j], j ? &bottom : nullptr, vbot, G, svTop);
        sample_cell(g, G);
        if (j == 0 && sv == 0) record_jets(sx, i, g, G);
        // right edge (R, m, n, W at the end xi-node) and top edge (all fields at the end v-node, s_v)
        const size_t NN = (size_t)g.nA * g.nB * NX;
        right[j].G.assign((size_t)4 * g.nB * NX, dd(0.0));
        for (int f = 0; f < 4; f++) for (int b = 0; b < g.nB; b++) for (int k = 0; k < NX; k++)
          right[j].G[((size_t)f * g.nB + b) * NX + k] = G[f * NN + IX(g.nA - 1, b, k, g.nB)];
        bottom.G.assign((size_t)NF * g.nA * NX, dd(0.0));
        for (int f = 0; f < NF; f++) for (int a = 0; a < g.nA; a++) for (int k = 0; k < NX; k++)
          bottom.G[((size_t)f * g.nA + a) * NX + k] = G[f * NN + IX(a, g.nB - 1, k, g.nB)];
        bottom.sv = svTop; vbot = vb[sv][j + 1];
        st.cells += 1; st.secs += co.secs; st.sweeps += co.sweeps;
        if (getenv("BSOLV_VERBOSE")) fprintf(stderr, "cell (%d,%d): outer %d, inner sweeps %d, %.1f s, last %.1e\n", i, j, co.outer, co.sweeps, co.secs, co.last); csec += co.secs; cmax = std::max(cmax, co.last); smax = std::max(smax, co.sweeps);
        if (co.last > 1e3 * CF.tol) fprintf(lg, "  cell Q%d (%d,%d): not converged, last update %.2e after %d sweeps\n", q + 1, i, j, co.last, co.sweeps);
      }
      st.left = right; st.col = i + 1;
      fprintf(lg, "Q%d column %d/%d: %.1f s, max sweeps %d, worst last update %.1e; total %.0f cells, %.0f s\n", q + 1, i + 1, ncol, csec, smax, cmax, st.cells, st.secs);
      fflush(lg);
      double since = std::chrono::duration<double>(std::chrono::steady_clock::now() - tlast).count();
      if (since > 60 * CF.ckpt_min) { st.quad_idx = qi; save_ckpt(st); tlast = std::chrono::steady_clock::now(); fprintf(lg, "  checkpoint written\n"); fflush(lg); }
      if (CF.stopcol >= 0 && i + 1 >= CF.stopcol) { st.quad_idx = qi; save_ckpt(st); write_output(); fprintf(lg, "stopped at column %d\n", i + 1); return 0; }
    }
    st.quad_idx = qi + 1; st.col = 0; st.left.clear();
    save_ckpt(st);
  }
  write_output();
  long tot = 0, done = 0; for (auto& d : EDONE) for (char c : d) { tot++; done += c; }
  fprintf(lg, "DONE: %.0f cells, %.0f s, mean sweeps %.1f; element nodes filled %ld of %ld\n", st.cells, st.secs, st.sweeps / std::max(1.0, st.cells), done, tot);
  fclose(lg);
  return 0;
}
