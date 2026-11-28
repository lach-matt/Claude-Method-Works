// cell.h: P-APPC2 def:appc-rule-seed (the seed), def:appc-grid, def:appc-cell (the cell map P(G) = B + I(G)) and the
// linearised map I_𝔻 of def:appc-iteration (iv) in the short arithmetic 𝔻 (binary64).  The iteration that uses them is
// in scheme.h.
//
// 𝔻 is IEEE binary64 with rounding to nearest, ties to even, each operation rounded once: this file must be compiled
// with -ffp-contract=off (no fused multiply-add), without -ffast-math, with SSE2 doubles (x86-64); every sum in 𝔻 is
// written in the order the text gives (a dot product ⟨a, g⟩_𝔻 from its first index up).
#pragma once
#include "matrices.h"
#include <omp.h>
#include <map>
#include <memory>
#include <tuple>
#include <cmath>
#include "rhs_gen.h"     // eq:appc-rhs (tests/rhs_vs_text.py: identical to the printed sequence, definition by definition)

enum { FR = 0, FM = 1, FN = 2, FW = 3, FS = 4, NF = 5 };
static const int NJ = 31;

// ---------------------------------------------------------------------------------------------- 𝔻 conversions
// rd(2^e X / 2^B) for the integer X of a number of 𝔽: nearest binary64, ties to even (exact integer rounding)
inline double rd_fx(const F& a, int e = 0) {
  uint64_t m[6]; bool n = fx_abs(a, m);
  int nb = 0; for (int i = 5; i >= 0; i--) if (m[i]) { nb = 64 * i + 64 - __builtin_clzll(m[i]); break; }
  if (nb == 0) return 0.0;
  auto bit = [&](int k) -> uint64_t { return (m[k / 64] >> (k % 64)) & 1; };
  uint64_t mant; int ex;
  if (nb <= 53) { mant = m[0]; ex = 0; }
  else {
    int sh = nb - 53; mant = 0;
    for (int k = 0; k < 53; k++) mant |= bit(sh + k) << k;
    uint64_t half = bit(sh - 1), sticky = 0;
    for (int k = 0; k < sh - 1 && !sticky; k++) sticky |= bit(k);
    if (half && (sticky || (mant & 1))) { mant++; if (mant >> 53) { mant >>= 1; sh++; } }
    ex = sh;
  }
  double v = std::ldexp((double)mant, ex + e - BITS);        // exact: mant < 2^53, no subnormal in this range
  return n ? -v : v;
}
inline double rd_rat(long num, long den) { return (double)num / (double)den; }    // rd q for small integers num, den
// ⌊2^(−ν) d⌋_B: the exact rational 2^(−ν) d floored to 𝔽
inline F floor_scaled(double d, int nu) {
  if (d == 0) return fx_zero<6, 5>();
  int e; double f = std::frexp(d, &e); long long M = (long long)std::ldexp(f, 53);   // d = M 2^(e − 53), exactly
  int s = e - 53 - nu + BITS;
  Z z(M); if (s >= 0) mpz_mul_2exp(z.v, z.v, s); else mpz_fdiv_q_2exp(z.v, z.v, -s);
  return fx_from_mpz<6, 5>(z.v);
}

// ---------------------------------------------------------------------------------------------- grids
struct DMat { int r = 0, c = 0; std::vector<double> a, tr;   // rd of the entries, row-major and transposed
  void from(const Mat& m) { r = m.r; c = m.c; a.resize(m.a.size()); tr.resize(m.a.size());
    for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) { a[(size_t)i * c + j] = rd_fx(m.a[(size_t)i * c + j]); tr[(size_t)j * r + i] = a[(size_t)i * c + j]; } } };
struct Grid {                       // node families and matrices for one (p_ξ, p_v, M)
  int pxi, pv, M, nA, nB, NX;
  Vec TL, TV, TR, X;
  Mat Dxi, Qxi, DvL, QvL, QQ, DvR, QvR, W4, V4, D1x, D2x;
  DMat dDxi, dQxi, dDvL, dQvL, dQQ, dDvR, dQvR, dW4, dV4, dD1x, dD2x; std::vector<double> dX;
};
inline std::unique_ptr<Grid> make_grid(int pxi, int pv, int M) {
  auto g = std::make_unique<Grid>();
  g->pxi = pxi; g->pv = pv; g->M = M; g->nA = pxi + 1; g->nB = pv + 1; g->NX = M + 1;
  g->TL = lobatto(pxi); g->TV = lobatto(pv); g->TR = radau(pv); g->X = xnodes(M);
  g->Dxi = Dmat(g->TL); g->Qxi = Qmat(g->TL);
  g->DvL = Dmat(g->TV); g->QvL = Qmat(g->TV); g->QQ = dotsq(g->QvL);
  g->DvR = Dmat(g->TR); g->QvR = Qmat(g->TR); W4V4(g->TR, g->W4, g->V4);
  g->D1x = Dmat(g->X); g->D2x = D2mat(g->X);
  g->dDxi.from(g->Dxi); g->dQxi.from(g->Qxi); g->dDvL.from(g->DvL); g->dQvL.from(g->QvL); g->dQQ.from(g->QQ);
  g->dDvR.from(g->DvR); g->dQvR.from(g->QvR); g->dW4.from(g->W4); g->dV4.from(g->V4); g->dD1x.from(g->D1x); g->dD2x.from(g->D2x);
  g->dX.resize(g->NX); for (int k = 0; k < g->NX; k++) g->dX[k] = rd_fx(g->X[k]);
  return g;
}

// ---------------------------------------------------------------------------------------------- the seed
struct SeedV { F R, Ru, Rv, OM2, iOM2, Wv, du, idu; };
inline SeedV seed_at(const F& xi, const F& v) {
  const F o = one<F>(), two = fx_int<6, 5>(2);
  F sh, ch; sinhcosh(xi, sh, ch);
  F u1 = CS.ah * sh, u = u1 - o, du = CS.ah * ch;
  F H = v - mul_int(u, 2) + logF(fdiv(u1, u1 - two));
  F r0 = o + pow2<F>(-32), r1 = divi(fx_neg(H) ? fx_zero<6, 5>() : H, 2) + fx_int<6, 5>(3);
  for (int i = 0; i < 80; i++) {
    F q = divi(r0 + r1, 2);
    if (mul_int(q, 2) + logF(fdiv(q - o, q + o)) < H) r0 = q; else r1 = q;
  }
  F R = r0;
  for (int i = 0; i < 6; i++) R = R - fdiv(mul_int(R, 2) + logF(fdiv(R - o, R + o)) - H, two + fdiv(two, R * R - o));
  F f = o - fdiv(o, R * R), g = o - fdiv(o, u * u);
  SeedV s; s.R = R; s.Rv = divi(f, 2); s.Ru = -fdiv(f, g); s.OM2 = fdiv(f, mul_int(g, 2));
  s.Wv = fdiv(o, mul_int((R * R) * R, 2)); s.du = du; s.idu = fdiv(o, du); s.iOM2 = fdiv(o, s.OM2);
  return s;
}

// ---------------------------------------------------------------------------------------------- edges
struct LeftEdge { int nB = 0, NX = 0; std::vector<F> G; };          // [f < 4][b][k]
struct TopEdge { int nA = 0, NX = 0; std::vector<F> G, sv; };       // G [f < 5][a][k], top values [a][k]

// ---------------------------------------------------------------------------------------------- one cell
struct Cell {
  int i = 0, j = 0; const Grid* g = nullptr; bool first = false; int No = 1, Ni = 0;
  F hxi, hv, ihxi, ihv, hh, hv2;
  Vec xis, vs, eps, e2, e3, e4, ie2, ie3;
  std::vector<SeedV> sd;              // [a][b]
  std::vector<F> Bt, G, Gn, Xs, Psi;  // [f][a][b][k] (Xs: [a][b][k][5], X(J_s); Psi[FS] is Φ)
  std::vector<S> GS, TS;
  // 𝔻
  double hxid, hvd, ihxid, ihvd; std::vector<double> e2d, e3d, e4d, ie2d, ie3d, uxd, iuxd;
  std::vector<double> Jd, rt, d, Psid, Td, Id;  // J̄ [node][31]; r̃, d, Ψ̇/Φ̇, temporaries, I_𝔻 [f][a][b][k]
  int nu = 0; bool zero_defect = false; int outer_done = 0;
  std::vector<F> rmax;                // max |r| of each outer step (spot values)
  size_t NN() const { return (size_t)g->nA * g->nB * g->NX; }
  size_t IX(int a, int b, int k) const { return ((size_t)a * g->nB + b) * g->NX + k; }
};

inline void rhs_at(const F* J, const F& x, F* out) { rhs_eval<F, F>(J, CS.K.data(), x, out); }

// pairs of 𝔻 (value, tangent): a ⊙ b gives (ā ⊗ b̄, (ȧ ⊗ b̄) ⊕ (ā ⊗ ḃ)); sums and negation componentwise
struct DP { double v, t; };
inline DP operator*(const DP& a, const DP& b) { double p = a.t * b.v, q = a.v * b.t; return DP{a.v * b.v, p + q}; }
inline DP operator+(const DP& a, const DP& b) { return DP{a.v + b.v, a.t + b.t}; }
inline DP operator-(const DP& a, const DP& b) { return DP{a.v - b.v, a.t - b.t}; }
inline DP operator-(const DP& a) { return DP{-a.v, -a.t}; }
struct DConsts { std::vector<DP> K; };
// a function-local static with an initializer is initialized once, thread-safely (C++11), before any thread uses it
inline const DConsts& dconsts() {
  static const DConsts d = [] { DConsts x; for (int i = 0; i < RHS_NK; i++) x.K.push_back(DP{rd_rat(RHS_KNUM[i], RHS_KDEN[i]), 0.0}); return x; }();
  return d;
}

// the right-hand side at the seed (D = 0): J_s
inline void cell_seed_rhs(Cell& c) {
  const Grid* g = c.g; const int nA = g->nA, nB = g->nB, NX = g->NX; const F o = one<F>();
  c.Xs.resize(c.NN() * 5);
  #pragma omp parallel for schedule(static)
  for (int ab = 0; ab < nA * nB; ab++) {
    const SeedV& s = c.sd[ab]; F J[RHS_NJ]; for (auto& q : J) q = fx_zero<6, 5>();
    F e0 = expF(fx_zero<6, 5>());
    J[0] = s.R; J[1] = fdiv(o, s.R); J[2] = e0; J[3] = e0; J[4] = s.OM2 * e0; J[5] = s.iOM2 * e0; J[6] = s.Ru; J[7] = s.Rv; J[11] = s.Wv;
    for (int k = 0; k < NX; k++) rhs_at(J, g->X[k], &c.Xs[(((size_t)ab) * NX + k) * 5]);
  }
}

// set up a cell: geometry, the seed at its nodes, the boundary term B, X(J_s), the numbers in 𝔻 (parallel)
inline void cell_setup(Cell& c, const Grid* g, int i, int j, int No, int Ni, const F& xi0, const F& xi1, const F& v0, const F& v1,
                       const LeftEdge& left, const TopEdge* low) {
  c.g = g; c.i = i; c.j = j; c.first = (j == 0); c.No = No; c.Ni = Ni;
  const int nA = g->nA, nB = g->nB, NX = g->NX; const size_t NN = c.NN();
  const F o = one<F>();
  c.hxi = divi(xi1 - xi0, 2); c.hv = divi(v1 - v0, 2);
  c.ihxi = fdiv(o, c.hxi); c.ihv = fdiv(o, c.hv); c.hh = c.hxi * c.hv; c.hv2 = c.hv * c.hv;
  const Vec& tv = c.first ? g->TR : g->TV;
  c.xis.resize(nA); c.vs.resize(nB);
  for (int a = 0; a < nA; a++) c.xis[a] = xi0 + c.hxi * (g->TL[a] + o);
  for (int b = 0; b < nB; b++) c.vs[b] = v0 + c.hv * (tv[b] + o);
  c.eps.resize(nB); c.e2.resize(nB); c.e3.resize(nB); c.e4.resize(nB); c.ie2.resize(nB); c.ie3.resize(nB);
  for (int b = 0; b < nB; b++) {
    c.eps[b] = c.vs[b] - CS.half; c.e2[b] = c.eps[b] * c.eps[b]; c.e3[b] = c.e2[b] * c.eps[b]; c.e4[b] = c.e3[b] * c.eps[b];
    c.ie2[b] = fdiv(o, c.e2[b]); c.ie3[b] = fdiv(o, c.e3[b]);
  }
  c.sd.resize((size_t)nA * nB);
  #pragma omp parallel for schedule(dynamic)
  for (int ab = 0; ab < nA * nB; ab++) c.sd[ab] = seed_at(c.xis[ab / nB], c.vs[ab % nB]);
  c.Bt.assign(NF * NN, fx_zero<6, 5>());
  F eta4 = fx_zero<6, 5>();
  if (!c.first) { F eta = v0 - CS.half; eta4 = ((eta * eta) * eta) * eta; }
  #pragma omp parallel for schedule(static)
  for (int ab = 0; ab < nA * nB; ab++) {
    int a = ab / nB, b = ab % nB;
    for (int f = 0; f < NF; f++) for (int k = 0; k < NX; k++) {
      F val = fx_zero<6, 5>();
      if (c.first) { if (f < 4) val = left.G[((size_t)f * nB + b) * NX + k]; }
      else if (f < 4) {
        const F& tb = low->G[((size_t)f * nA + a) * NX + k], &t0 = low->G[((size_t)f * nA + 0) * NX + k];
        val = fdiv(eta4 * tb + c.e4[b] * left.G[((size_t)f * nB + b) * NX + k] - eta4 * t0, c.e4[b]);
      } else {
        val = fdiv(eta4 * low->G[((size_t)FS * nA + a) * NX + k] + (c.vs[b] - v0) * low->sv[(size_t)a * NX + k], c.e4[b]);
      }
      c.Bt[f * NN + c.IX(a, b, k)] = val;
    }
  }
  cell_seed_rhs(c);
  c.hxid = rd_fx(c.hxi); c.hvd = rd_fx(c.hv); c.ihxid = rd_fx(c.ihxi); c.ihvd = rd_fx(c.ihv);
  c.e2d.resize(nB); c.e3d.resize(nB); c.e4d.resize(nB); c.ie2d.resize(nB); c.ie3d.resize(nB);
  for (int b = 0; b < nB; b++) { c.e2d[b] = rd_fx(c.e2[b]); c.e3d[b] = rd_fx(c.e3[b]); c.e4d[b] = rd_fx(c.e4[b]); c.ie2d[b] = rd_fx(c.ie2[b]); c.ie3d[b] = rd_fx(c.ie3[b]); }
  c.uxd.resize((size_t)nA * nB); c.iuxd.resize((size_t)nA * nB);
  for (int ab = 0; ab < nA * nB; ab++) { c.uxd[ab] = rd_fx(c.sd[ab].du); c.iuxd[ab] = rd_fx(c.sd[ab].idu); }
  c.G = c.Bt; c.Gn.resize(NF * NN); c.Psi.resize(NF * NN); c.GS.resize(NF * NN); c.TS.resize(NF * NN);
  c.Jd.resize(NN * NJ); c.rt.resize(NF * NN); c.d.resize(NF * NN); c.Psid.resize(NF * NN); c.Td.resize(NF * NN); c.Id.resize(NF * NN);
  c.zero_defect = false; c.outer_done = 0; c.rmax.clear(); c.nu = 0;
}

// Ψ (fields R, m, n, W), Φ and J̄ := rd J(G) at the nodes of line (a, b), from c.GS (the sign-magnitude form of G)
inline void cell_eval_line(Cell& c, int a, int b) {
  const Grid* g = c.g; const int nA = g->nA, nB = g->nB, NX = g->NX; const size_t NN = c.NN();
  const Mat& Dv = c.first ? g->DvR : g->DvL;
  std::vector<F> Gv((size_t)NF * NX), Gxi((size_t)3 * NX); std::vector<S> GvS((size_t)NF * NX);
  for (int f = 0; f < NF; f++) for (int k = 0; k < NX; k++) {
    Gv[(size_t)f * NX + k] = dot<6, 5>(&Dv.s[(size_t)b * nB], 1, &c.GS[f * NN + c.IX(a, 0, k)], NX, nB) * c.ihv;
    GvS[(size_t)f * NX + k] = to_sm(Gv[(size_t)f * NX + k]);
    if (f < 3) Gxi[(size_t)f * NX + k] = dot<6, 5>(&g->Dxi.s[(size_t)a * nA], 1, &c.GS[f * NN + c.IX(0, b, k)], (long)nB * NX, nA) * c.ihxi;
  }
  const SeedV& s = c.sd[(size_t)a * nB + b];
  const F& e4 = c.e4[b], &e3 = c.e3[b]; const F o = one<F>();
  for (int k = 0; k < NX; k++) {
    const size_t ix = c.IX(a, b, k);
    F D[NF], Dx[NF], Dv_[NF], Dvx[NF], Dxx[4], Du[3];
    for (int f = 0; f < NF; f++) {
      const S* gl = &c.GS[f * NN + c.IX(a, b, 0)];
      F gval = c.G[f * NN + ix];
      F gx = dot<6, 5>(&g->D1x.s[(size_t)k * NX], 1, gl, 1, NX);
      F gvx = dot<6, 5>(&g->D1x.s[(size_t)k * NX], 1, &GvS[(size_t)f * NX], 1, NX);
      D[f] = e4 * gval; Dx[f] = e4 * gx;
      Dv_[f] = mul_int(e3 * gval, 4) + e4 * Gv[(size_t)f * NX + k];     // 4 (e₃ ⊙ G) + e₄ ⊙ G_v
      Dvx[f] = mul_int(e3 * gx, 4) + e4 * gvx;                          // 4 (e₃ ⊙ G_x) + e₄ ⊙ G_vx
      if (f < 4) Dxx[f] = e4 * dot<6, 5>(&g->D2x.s[(size_t)k * NX], 1, gl, 1, NX);
      if (f < 3) Du[f] = (e4 * Gxi[(size_t)f * NX + k]) * s.idu;
    }
    const F& x = g->X[k];
    F J[RHS_NJ];
    F R = s.R + D[FR];
    F Sv = divi(D[FM] + x * D[FM] + D[FN] - x * D[FN], 3);              // (D^m + x ⊙ D^m + D^n − x ⊙ D^n) ⊘ 3
    J[0] = R; J[1] = fdiv(o, R); J[2] = expF(Sv); J[3] = expF(-Sv);
    J[4] = s.OM2 * expF(mul_int(D[FW], 2)); J[5] = s.iOM2 * expF(mul_int(D[FW], -2));
    J[6] = s.Ru + Du[FR]; J[7] = s.Rv + Dv_[FR]; J[8] = Dx[FR]; J[9] = Dxx[FR]; J[10] = Dvx[FR];
    J[11] = s.Wv + Dv_[FW]; J[12] = Dx[FW]; J[13] = Dxx[FW]; J[14] = Dvx[FW];
    J[15] = D[FM]; J[16] = Du[FM]; J[17] = Dv_[FM]; J[18] = Dx[FM]; J[19] = Dxx[FM]; J[20] = Dvx[FM];
    J[21] = D[FN]; J[22] = Du[FN]; J[23] = Dv_[FN]; J[24] = Dx[FN]; J[25] = Dxx[FN]; J[26] = Dvx[FN];
    J[27] = D[FS]; J[28] = Dv_[FS]; J[29] = Dx[FS]; J[30] = Dvx[FS];
    double* jd = &c.Jd[ix * NJ]; for (int q = 0; q < NJ; q++) jd[q] = rd_fx(J[q]);
    F out[5]; rhs_at(J, x, out);
    const F* xs = &c.Xs[(((size_t)a * nB + b) * NX + k) * 5];
    c.Psi[FR * NN + ix] = s.du * (out[2] - xs[2]); c.Psi[FM * NN + ix] = s.du * (out[0] - xs[0]);
    c.Psi[FN * NN + ix] = s.du * (out[1] - xs[1]); c.Psi[FW * NN + ix] = s.du * (out[3] - xs[3]);
    c.Psi[FS * NN + ix] = out[4] - xs[4];
  }
}

// ⟨a, g⟩_𝔻 for every row r of a matrix at once: out[r] = ((A_r0 g0 ⊕ A_r1 g1) ⊕ ...) -- each row's sum in the order of
// the index (the loop over r is innermost and independent, so it may be vectorized without changing any sum)
inline void matvec_d(const DMat& A, const double* g, long sg, double* out) {
  const int R = A.r, C = A.c;
  for (int r = 0; r < R; r++) out[r] = A.tr[r] * g[0];
  for (int l = 1; l < C; l++) { const double gl = g[l * sg]; const double* col = &A.tr[(size_t)l * R]; for (int r = 0; r < R; r++) out[r] = out[r] + col[r] * gl; }
}
inline double dot_d(const double* a, const double* g, long sg, int n) {
  double s = a[0] * g[0]; for (int l = 1; l < n; l++) s = s + a[l] * g[l * sg]; return s;
}

// I_𝔻: Ψ̇ and Φ̇ at the nodes of line (a, b) from c.d (def:appc-iteration (iv))
inline void cell_lin_line(Cell& c, int a, int b) {
  const Grid* g = c.g; const int nA = g->nA, nB = g->nB, NX = g->NX; const size_t NN = c.NN();
  const DMat& Dv = c.first ? g->dDvR : g->dDvL;
  std::vector<double> dv((size_t)NF * NX), dxi((size_t)3 * NX), gx((size_t)NF * NX), gxx((size_t)4 * NX), gvx((size_t)NF * NX);
  for (int f = 0; f < NF; f++) for (int k = 0; k < NX; k++) {
    dv[(size_t)f * NX + k] = dot_d(&Dv.a[(size_t)b * nB], &c.d[f * NN + c.IX(a, 0, k)], NX, nB) * c.ihvd;
    if (f < 3) dxi[(size_t)f * NX + k] = dot_d(&g->dDxi.a[(size_t)a * nA], &c.d[f * NN + c.IX(0, b, k)], (long)nB * NX, nA) * c.ihxid;
  }
  for (int f = 0; f < NF; f++) {
    const double* dl = &c.d[f * NN + c.IX(a, b, 0)];
    matvec_d(g->dD1x, dl, 1, &gx[(size_t)f * NX]);
    if (f < 4) matvec_d(g->dD2x, dl, 1, &gxx[(size_t)f * NX]);
    matvec_d(g->dD1x, &dv[(size_t)f * NX], 1, &gvx[(size_t)f * NX]);
  }
  const double e4 = c.e4d[b], e3 = c.e3d[b], ux = c.uxd[(size_t)a * nB + b], iux = c.iuxd[(size_t)a * nB + b];
  const DConsts& DK = dconsts();
  for (int k = 0; k < NX; k++) {
    const size_t ix = c.IX(a, b, k);
    double D[NF], Dx[NF], Dv_[NF], Dvx[NF], Dxx[4], Du[3];
    for (int f = 0; f < NF; f++) {
      const double gd = c.d[f * NN + ix], gxd = gx[(size_t)f * NX + k];
      D[f] = e4 * gd; Dx[f] = e4 * gxd;
      Dv_[f] = 4.0 * (e3 * gd) + e4 * dv[(size_t)f * NX + k];
      Dvx[f] = 4.0 * (e3 * gxd) + e4 * gvx[(size_t)f * NX + k];
      if (f < 4) Dxx[f] = e4 * gxx[(size_t)f * NX + k];
      if (f < 3) Du[f] = (e4 * dxi[(size_t)f * NX + k]) * iux;
    }
    const double* Jv = &c.Jd[ix * NJ]; const double xb = g->dX[k];
    const double Sdot = (((D[FM] + xb * D[FM]) + D[FN]) - xb * D[FN]) / 3.0;
    double Jt[NJ] = {D[FR], -((Jv[1] * Jv[1]) * D[FR]), Jv[2] * Sdot, -(Jv[3] * Sdot), Jv[4] * (2.0 * D[FW]), -(Jv[5] * (2.0 * D[FW])),
                     Du[FR], Dv_[FR], Dx[FR], Dxx[FR], Dvx[FR], Dv_[FW], Dx[FW], Dxx[FW], Dvx[FW],
                     D[FM], Du[FM], Dv_[FM], Dx[FM], Dxx[FM], Dvx[FM], D[FN], Du[FN], Dv_[FN], Dx[FN], Dxx[FN], Dvx[FN],
                     D[FS], Dv_[FS], Dx[FS], Dvx[FS]};
    DP J[NJ]; for (int q = 0; q < NJ; q++) J[q] = DP{Jv[q], Jt[q]};
    DP out[5]; DP xd{xb, 0.0}; rhs_eval<DP, DP>(J, DK.K.data(), xd, out);
    c.Psid[FR * NN + ix] = ux * out[2].t; c.Psid[FM * NN + ix] = ux * out[0].t;
    c.Psid[FN * NN + ix] = ux * out[1].t; c.Psid[FW * NN + ix] = ux * out[3].t; c.Psid[FS * NN + ix] = out[4].t;
  }
}

// ---------------------------------------------------------------------------------------------- batches
// A batch is a set of independent cells (of one anti-diagonal) iterated in lockstep; every parallel loop runs over
// the nodes of all its active cells at once.  The result does not depend on the batch or on the thread count.
struct Batch {
  std::vector<Cell*> cells;
  std::vector<Cell*> active() const { std::vector<Cell*> v; for (Cell* c : cells) if (!c->zero_defect) v.push_back(c); return v; }
  void to_sm_all(const std::vector<Cell*>& act) {
    std::vector<std::pair<Cell*, int>> jobs; for (Cell* c : act) for (int p = 0; p < 64; p++) jobs.push_back({c, p});
    #pragma omp parallel for schedule(static)
    for (size_t q = 0; q < jobs.size(); q++) {
      Cell* c = jobs[q].first; size_t n = c->G.size(), part = jobs[q].second, lo = n * part / 64, hi = n * (part + 1) / 64;
      for (size_t i = lo; i < hi; i++) c->GS[i] = to_sm(c->G[i]);
    }
  }
  void evaluate(const std::vector<Cell*>& act) {          // Ψ, Φ, J̄ from G
    to_sm_all(act);
    std::vector<std::tuple<Cell*, int, int>> jobs;
    for (Cell* c : act) for (int a = 0; a < c->g->nA; a++) for (int b = 0; b < c->g->nB; b++) jobs.push_back({c, a, b});
    #pragma omp parallel for schedule(dynamic, 1)
    for (size_t q = 0; q < jobs.size(); q++) cell_eval_line(*std::get<0>(jobs[q]), std::get<1>(jobs[q]), std::get<2>(jobs[q]));
  }
  void integrate(const std::vector<Cell*>& act) {         // Gn = B + I(Ψ, Φ) (eq:appc-rule-int)
    std::vector<std::tuple<Cell*, int, int, int>> j1, j2;
    for (Cell* c : act) {
      for (int f = 0; f < NF; f++) for (int a = 0; a < c->g->nA; a++) for (int k = 0; k < c->g->NX; k++) j1.push_back({c, f, a, k});
      for (int f = 0; f < 4; f++) for (int b = 0; b < c->g->nB; b++) for (int k = 0; k < c->g->NX; k++) j2.push_back({c, f, b, k});
    }
    #pragma omp parallel for schedule(dynamic, 16)
    for (size_t q = 0; q < j1.size(); q++) {
      Cell& c = *std::get<0>(j1[q]); int f = std::get<1>(j1[q]), a = std::get<2>(j1[q]), k = std::get<3>(j1[q]);
      const Grid* g = c.g; const int nB = g->nB; const size_t NN = c.NN();
      std::vector<S> p(nB);
      for (int b = 0; b < nB; b++) { const F& x = c.Psi[f * NN + c.IX(a, b, k)]; p[b] = to_sm(c.first ? x * (f < 4 ? c.ie3[b] : c.ie2[b]) : x); }
      if (f < 4) {
        const Mat& M = c.first ? g->W4 : g->QvL;
        for (int b = 0; b < nB; b++) c.TS[f * NN + c.IX(a, b, k)] = to_sm(dot<6, 5>(&M.s[(size_t)b * nB], 1, p.data(), 1, nB));
      } else {
        for (int b = 0; b < nB; b++) {
          F I = c.first ? dot<6, 5>(&g->V4.s[(size_t)b * nB], 1, p.data(), 1, nB)
                        : fdiv(c.hv2 * dot<6, 5>(&g->QQ.s[(size_t)b * nB], 1, p.data(), 1, nB), c.e4[b]);
          size_t ix = FS * NN + c.IX(a, b, k); c.Gn[ix] = c.Bt[ix] + I;
        }
      }
    }
    #pragma omp parallel for schedule(dynamic, 16)
    for (size_t q = 0; q < j2.size(); q++) {
      Cell& c = *std::get<0>(j2[q]); int f = std::get<1>(j2[q]), b = std::get<2>(j2[q]), k = std::get<3>(j2[q]);
      const Grid* g = c.g; const int nA = g->nA, nB = g->nB, NX = g->NX; const size_t NN = c.NN();
      for (int a = 0; a < nA; a++) {
        F t = dot<6, 5>(&g->Qxi.s[(size_t)a * nA], 1, &c.TS[f * NN + c.IX(0, b, k)], (long)nB * NX, nA);
        F I = c.first ? c.hxi * t : fdiv(c.hh * t, c.e4[b]);
        size_t ix = f * NN + c.IX(a, b, k); c.Gn[ix] = c.Bt[ix] + I;
      }
    }
  }
  void lin(const std::vector<Cell*>& act) {               // c.Id := I_𝔻(c.d)
    std::vector<std::tuple<Cell*, int, int>> jobs;
    for (Cell* c : act) for (int a = 0; a < c->g->nA; a++) for (int b = 0; b < c->g->nB; b++) jobs.push_back({c, a, b});
    #pragma omp parallel for schedule(dynamic, 1)
    for (size_t q = 0; q < jobs.size(); q++) cell_lin_line(*std::get<0>(jobs[q]), std::get<1>(jobs[q]), std::get<2>(jobs[q]));
    std::vector<std::tuple<Cell*, int, int, int>> j1, j2;
    for (Cell* c : act) {
      for (int f = 0; f < NF; f++) for (int a = 0; a < c->g->nA; a++) for (int k = 0; k < c->g->NX; k++) j1.push_back({c, f, a, k});
      for (int f = 0; f < 4; f++) for (int b = 0; b < c->g->nB; b++) for (int k = 0; k < c->g->NX; k++) j2.push_back({c, f, b, k});
    }
    #pragma omp parallel for schedule(dynamic, 16)
    for (size_t q = 0; q < j1.size(); q++) {
      Cell& c = *std::get<0>(j1[q]); int f = std::get<1>(j1[q]), a = std::get<2>(j1[q]), k = std::get<3>(j1[q]);
      const Grid* g = c.g; const int nB = g->nB; const size_t NN = c.NN();
      std::vector<double> p(nB);
      for (int b = 0; b < nB; b++) { double x = c.Psid[f * NN + c.IX(a, b, k)]; p[b] = c.first ? x * (f < 4 ? c.ie3d[b] : c.ie2d[b]) : x; }
      if (f < 4) {
        const DMat& M = c.first ? g->dW4 : g->dQvL;
        for (int b = 0; b < nB; b++) c.Td[f * NN + c.IX(a, b, k)] = dot_d(&M.a[(size_t)b * nB], p.data(), 1, nB);
      } else {
        for (int b = 0; b < nB; b++)
          c.Id[FS * NN + c.IX(a, b, k)] = c.first ? dot_d(&g->dV4.a[(size_t)b * nB], p.data(), 1, nB)
                                                  : ((c.hvd * c.hvd) * dot_d(&g->dQQ.a[(size_t)b * nB], p.data(), 1, nB)) / c.e4d[b];
      }
    }
    #pragma omp parallel for schedule(dynamic, 16)
    for (size_t q = 0; q < j2.size(); q++) {
      Cell& c = *std::get<0>(j2[q]); int f = std::get<1>(j2[q]), b = std::get<2>(j2[q]), k = std::get<3>(j2[q]);
      const Grid* g = c.g; const int nA = g->nA, nB = g->nB, NX = g->NX; const size_t NN = c.NN();
      for (int a = 0; a < nA; a++) {
        double t = dot_d(&g->dQxi.a[(size_t)a * nA], &c.Td[f * NN + c.IX(0, b, k)], (long)nB * NX, nA);
        c.Id[f * NN + c.IX(a, b, k)] = c.first ? c.hxid * t : ((c.hxid * c.hvd) * t) / c.e4d[b];
      }
    }
  }
};
