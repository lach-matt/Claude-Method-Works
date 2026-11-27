// cell.h: S-RULE §3.4 (the seed), §3.6 (cells, the cell problem) -- the cell operator P(G) = B + I(G).
// The iteration scheme that uses it (plain Picard, §3.7) is in scheme.h, so that a different scheme can replace it.
#pragma once
#include "matrices.h"
#include <omp.h>
#include <map>
#include <memory>
#include <tuple>

// the right-hand side: the solver's generated straight-line program, every product floored (fixp.h's operator*)
#include "rhs_gen.h"

enum { FR = 0, FM = 1, FN = 2, FW = 3, FS = 4, NF = 5 };
// For the comparison with the pilot only (rule pilotcell ... compat): the pilot's readings of two formulas, 4(ε³ ⊙ G)
// for (4ε³) ⊙ G in D_v and D_vx [Q2], and D_m + x ⊙ D_m + D_n − x ⊙ D_n for (1 + x) ⊙ D_m + (1 − x) ⊙ D_n in S [Q12].
inline bool& compat_pilot() { static bool c = false; return c; }

// ---------------------------------------------------------------------------------------------- grids
struct Grid {                       // node sets and matrices for one (p_ξ, p_v, M)
  int pxi, pv, M, nA, nB, NX;
  Vec TL, TV, TR, X;
  Mat Dxi, Qxi, DvL, QvL, QQ, DvR, QvR, W4, V4, D1x, D2x;
};
inline std::unique_ptr<Grid> make_grid(int pxi, int pv, int M) {
  auto g = std::make_unique<Grid>();
  g->pxi = pxi; g->pv = pv; g->M = M; g->nA = pxi + 1; g->nB = pv + 1; g->NX = M + 1;
  g->TL = lobatto(pxi); g->TV = lobatto(pv); g->TR = radau(pv); g->X = xnodes(M);
  g->Dxi = Dmat(g->TL); g->Qxi = Qmat(g->TL);
  g->DvL = Dmat(g->TV); g->QvL = Qmat(g->TV); g->QQ = dotsq(g->QvL);
  g->DvR = Dmat(g->TR); g->QvR = Qmat(g->TR); W4V4(g->TR, g->W4, g->V4);
  g->D1x = Dmat(g->X); g->D2x = dotsq(g->D1x);
  return g;
}

// ---------------------------------------------------------------------------------------------- §3.4 the seed
struct SeedV { F R, Ru, Rv, OM2, iOM2, Wv, du, idu; };
inline SeedV seed_at(const F& xi, const F& v) {
  const F o = one<F>(), two = fx_int<6, 5>(2);
  F sh, ch; sinhcosh(xi, sh, ch);
  F up1 = CS.ah * sh, u = up1 - o, du = CS.ah * ch;
  F H = v - mul_int(u, 2) + logF(fdiv(up1, u - o));
  F r0 = o + pow2<F>(-32), r1 = divi(fx_neg(H) ? fx_zero<6, 5>() : H, 2) + fx_int<6, 5>(3);
  for (int i = 0; i < 80; i++) {
    F mid = divi(r0 + r1, 2);
    if (mul_int(mid, 2) + logF(fdiv(mid - o, mid + o)) < H) r0 = mid; else r1 = mid;
  }
  F R = r0;
  for (int i = 0; i < 6; i++) R = R - fdiv(mul_int(R, 2) + logF(fdiv(R - o, R + o)) - H, two + fdiv(two, R * R - o));
  F f = o - fdiv(o, R * R), g = o - fdiv(o, u * u);
  SeedV s; s.R = R; s.Rv = divi(f, 2); s.Ru = -fdiv(f, g); s.OM2 = fdiv(f, mul_int(g, 2));   // R_u := −(f ⊘ g) [Q24]
  s.Wv = fdiv(o, (mul_int(R, 2) * R) * R); s.du = du; s.idu = fdiv(o, du); s.iOM2 = fdiv(o, s.OM2);
  return s;
}

// ---------------------------------------------------------------------------------------------- edges
struct LeftEdge { int nB = 0, NX = 0; std::vector<F> G; };          // [f < 4][b][k]
struct TopEdge { int nA = 0, NX = 0; std::vector<F> G, sv; };       // G [f < 5][a][k], sv [a][k]

// ---------------------------------------------------------------------------------------------- one cell
struct Cell {
  int i = 0, j = 0; const Grid* g = nullptr; bool first = false;
  F hxi, hv, ihxi, ihv, hh, hv2, vlo;
  Vec xis, vs, eps, e2, e3, e4, e3x4, ie2, ie3;
  std::vector<SeedV> sd;            // [a][b]
  std::vector<F> Bt, G, Gn, Xs, Psi;  // [f][a][b][k] (Xs: [a][b][k][5], the right-hand side at D = 0)
  std::vector<S> GS, TS;
  bool frozen = false; int sweeps = 0; bool psi_is_final = false;
  size_t NN() const { return (size_t)g->nA * g->nB * g->NX; }
  size_t IX(int a, int b, int k) const { return ((size_t)a * g->nB + b) * g->NX + k; }
};

inline void rhs_at(const F* J, const F& x, F* out) { rhs_eval<F, F>(J, CS.K.data(), x, out); }

// the right-hand side at the seed (D = 0): R = R_s, ES = iES = exp(0) = 1, OM2 = Ω²_s ⊙ 1, the rest the seed's
inline void cell_seed_rhs(Cell& c) {
  const Grid* g = c.g; const int nA = g->nA, nB = g->nB, NX = g->NX; const size_t NN = c.NN(); const F o = one<F>();
  c.Xs.resize(NN * 5);
  #pragma omp parallel for schedule(static)
  for (int ab = 0; ab < nA * nB; ab++) {
    const SeedV& s = c.sd[ab]; F J[RHS_NJ]; for (auto& q : J) q = fx_zero<6, 5>();
    J[0] = s.R; J[1] = fdiv(o, s.R); J[2] = expF(fx_zero<6, 5>()); J[3] = J[2];
    J[4] = s.OM2 * J[2]; J[5] = s.iOM2 * J[2]; J[6] = s.Ru; J[7] = s.Rv; J[11] = s.Wv;
    for (int k = 0; k < NX; k++) rhs_at(J, g->X[k], &c.Xs[(((size_t)ab) * NX + k) * 5]);
  }
}

// set up a cell: geometry, the seed at its nodes, the boundary term B, the right-hand side at D = 0 (parallel)
inline void cell_setup(Cell& c, const Grid* g, int i, int j, const F& xi0, const F& xi1, const F& v0, const F& v1,
                       const LeftEdge& left, const TopEdge* bottom) {
  c.g = g; c.i = i; c.j = j; c.first = (j == 0);
  const int nA = g->nA, nB = g->nB, NX = g->NX; const size_t NN = c.NN();
  const F o = one<F>();
  c.hxi = divi(xi1 - xi0, 2); c.hv = divi(v1 - v0, 2); c.vlo = v0;                // [Q8]
  c.ihxi = fdiv(o, c.hxi); c.ihv = fdiv(o, c.hv); c.hh = c.hxi * c.hv; c.hv2 = c.hv * c.hv;
  const Vec& tv = c.first ? g->TR : g->TV;
  c.xis.resize(nA); c.vs.resize(nB);
  for (int a = 0; a < nA; a++) c.xis[a] = xi0 + c.hxi * (g->TL[a] + o);
  for (int b = 0; b < nB; b++) c.vs[b] = v0 + c.hv * (tv[b] + o);
  c.eps.resize(nB); c.e2.resize(nB); c.e3.resize(nB); c.e4.resize(nB); c.e3x4.resize(nB); c.ie2.resize(nB); c.ie3.resize(nB);
  for (int b = 0; b < nB; b++) {
    c.eps[b] = c.vs[b] - CS.half; c.e2[b] = c.eps[b] * c.eps[b]; c.e3[b] = c.e2[b] * c.eps[b]; c.e4[b] = c.e3[b] * c.eps[b];
    c.e3x4[b] = mul_int(c.e3[b], 4); c.ie2[b] = fdiv(o, c.e2[b]); c.ie3[b] = fdiv(o, c.e3[b]);
  }
  c.sd.resize((size_t)nA * nB);
  #pragma omp parallel for schedule(dynamic)
  for (int ab = 0; ab < nA * nB; ab++) c.sd[ab] = seed_at(c.xis[ab / nB], c.vs[ab % nB]);
  // B (§3.6): row 0 B^F = G^F_left, B^s = 0; other rows the Goursat terms
  c.Bt.assign(NF * NN, fx_zero<6, 5>());
  const F elo = v0 - CS.half, elo4 = ((elo * elo) * elo) * elo;
  #pragma omp parallel for schedule(static)
  for (int ab = 0; ab < nA * nB; ab++) {
    int a = ab / nB, b = ab % nB;
    for (int f = 0; f < NF; f++) for (int k = 0; k < NX; k++) {
      F val = fx_zero<6, 5>();
      if (c.first) { if (f < 4) val = left.G[((size_t)f * nB + b) * NX + k]; }
      else if (f < 4) {
        const F& gb = bottom->G[((size_t)f * nA + a) * NX + k], &g0 = bottom->G[((size_t)f * nA + 0) * NX + k];
        val = fdiv(elo4 * gb + c.e4[b] * left.G[((size_t)f * nB + b) * NX + k] - elo4 * g0, c.e4[b]);
      } else {
        val = fdiv(elo4 * bottom->G[((size_t)FS * nA + a) * NX + k] + (c.vs[b] - v0) * bottom->sv[(size_t)a * NX + k], c.e4[b]);
      }
      c.Bt[f * NN + c.IX(a, b, k)] = val;
    }
  }
  cell_seed_rhs(c);
  c.G = c.Bt; c.Gn.resize(NF * NN); c.Psi.resize(NF * NN); c.GS.resize(NF * NN); c.TS.resize(NF * NN);
  c.frozen = false; c.sweeps = 0; c.psi_is_final = false;
}

// Ψ (fields R, m, n, W) and Φ at the nodes of line (a, b) from c.GS (the sign-magnitude form of the current G)
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
  const F& e4 = c.e4[b], &e3x4 = c.e3x4[b]; const F o = one<F>();
  for (int k = 0; k < NX; k++) {
    const size_t ix = c.IX(a, b, k);
    F D[NF], Dx[NF], Dv_[NF], Dvx[NF], Dxx[4], Du[3];
    for (int f = 0; f < NF; f++) {
      const S* gl = &c.GS[f * NN + c.IX(a, b, 0)];
      F gval = c.G[f * NN + ix];
      F gx = dot<6, 5>(&g->D1x.s[(size_t)k * NX], 1, gl, 1, NX);
      F gvx = dot<6, 5>(&g->D1x.s[(size_t)k * NX], 1, &GvS[(size_t)f * NX], 1, NX);
      D[f] = e4 * gval; Dx[f] = e4 * gx;
      if (!compat_pilot()) {
        Dv_[f] = e3x4 * gval + e4 * Gv[(size_t)f * NX + k];              // (4ε³) ⊙ G + ε⁴ ⊙ ∂_v G [Q2]
        Dvx[f] = e3x4 * gx + e4 * gvx;                                    // [Q11]
      } else {
        Dv_[f] = mul_int(c.e3[b] * gval, 4) + e4 * Gv[(size_t)f * NX + k];
        Dvx[f] = mul_int(c.e3[b] * gx, 4) + e4 * gvx;
      }
      if (f < 4) Dxx[f] = e4 * dot<6, 5>(&g->D2x.s[(size_t)k * NX], 1, gl, 1, NX);
      if (f < 3) Du[f] = (e4 * Gxi[(size_t)f * NX + k]) * s.idu;
    }
    const F& x = g->X[k];
    F J[RHS_NJ];
    F R = s.R + D[FR];
    F Sv = !compat_pilot() ? divi((o + x) * D[FM] + (o - x) * D[FN], 3)              // [Q12]
                           : divi(D[FM] + x * D[FM] + D[FN] - x * D[FN], 3);
    J[0] = R; J[1] = fdiv(o, R); J[2] = expF(Sv); J[3] = expF(-Sv);
    J[4] = s.OM2 * expF(mul_int(D[FW], 2)); J[5] = s.iOM2 * expF(mul_int(D[FW], -2));
    J[6] = s.Ru + Du[FR]; J[7] = s.Rv + Dv_[FR]; J[8] = Dx[FR]; J[9] = Dxx[FR]; J[10] = Dvx[FR];
    J[11] = s.Wv + Dv_[FW]; J[12] = Dx[FW]; J[13] = Dxx[FW]; J[14] = Dvx[FW];
    J[15] = D[FM]; J[16] = Du[FM]; J[17] = Dv_[FM]; J[18] = Dx[FM]; J[19] = Dxx[FM]; J[20] = Dvx[FM];
    J[21] = D[FN]; J[22] = Du[FN]; J[23] = Dv_[FN]; J[24] = Dx[FN]; J[25] = Dxx[FN]; J[26] = Dvx[FN];
    J[27] = D[FS]; J[28] = Dv_[FS]; J[29] = Dx[FS]; J[30] = Dvx[FS];
    F out[5]; rhs_at(J, x, out);
    const F* xs = &c.Xs[(((size_t)a * nB + b) * NX + k) * 5];
    c.Psi[FR * NN + ix] = s.du * (out[2] - xs[2]); c.Psi[FM * NN + ix] = s.du * (out[0] - xs[0]);
    c.Psi[FN * NN + ix] = s.du * (out[1] - xs[1]); c.Psi[FW * NN + ix] = s.du * (out[3] - xs[3]);
    c.Psi[FS * NN + ix] = out[4] - xs[4];
  }
}

// ---------------------------------------------------------------------------------------------- batches
// A batch is a set of independent cells (on one anti-diagonal) iterated in lockstep; every parallel loop runs over
// the nodes of all its cells at once.  The result does not depend on the batch or on the thread count.
struct Batch {
  std::vector<Cell*> cells;
  void to_sm_all() {
    std::vector<std::pair<Cell*, size_t>> jobs;
    for (Cell* c : cells) if (!c->frozen) jobs.push_back({c, 0});
    #pragma omp parallel for schedule(static) collapse(1)
    for (size_t q = 0; q < jobs.size() * 64; q++) {
      Cell* c = jobs[q / 64].first; size_t n = c->G.size(), part = q % 64, lo = n * part / 64, hi = n * (part + 1) / 64;
      for (size_t i = lo; i < hi; i++) c->GS[i] = to_sm(c->G[i]);
    }
  }
  void evaluate() {          // Ψ, Φ of every active cell from its current G
    to_sm_all();
    std::vector<std::tuple<Cell*, int, int>> jobs;
    for (Cell* c : cells) if (!c->frozen) for (int a = 0; a < c->g->nA; a++) for (int b = 0; b < c->g->nB; b++) jobs.push_back({c, a, b});
    #pragma omp parallel for schedule(dynamic, 1)
    for (size_t q = 0; q < jobs.size(); q++) cell_eval_line(*std::get<0>(jobs[q]), std::get<1>(jobs[q]), std::get<2>(jobs[q]));
  }
  void integrate() {         // Gn = B + I(Ψ, Φ) for every active cell (§3.6, "the integration I")
    std::vector<std::tuple<Cell*, int, int, int>> j1, j2;
    for (Cell* c : cells) if (!c->frozen) {
      for (int f = 0; f < NF; f++) for (int a = 0; a < c->g->nA; a++) for (int k = 0; k < c->g->NX; k++) j1.push_back({c, f, a, k});
      for (int f = 0; f < 4; f++) for (int b = 0; b < c->g->nB; b++) for (int k = 0; k < c->g->NX; k++) j2.push_back({c, f, b, k});
    }
    // stage 1: along v (W4 / Q_v, and the whole of I^s)
    #pragma omp parallel for schedule(dynamic, 16)
    for (size_t q = 0; q < j1.size(); q++) {
      Cell& c = *std::get<0>(j1[q]); int f = std::get<1>(j1[q]), a = std::get<2>(j1[q]), k = std::get<3>(j1[q]);
      const Grid* g = c.g; const int nB = g->nB; const size_t NN = c.NN();
      S P[64]; std::vector<S> Pv; S* p = P; if (nB > 64) { Pv.resize(nB); p = Pv.data(); }
      for (int b = 0; b < nB; b++) {
        const F& x = c.Psi[f * NN + c.IX(a, b, k)];
        p[b] = to_sm(c.first ? x * (f < 4 ? c.ie3[b] : c.ie2[b]) : x);
      }
      if (f < 4) {
        const Mat& M = c.first ? g->W4 : g->QvL;
        for (int b = 0; b < nB; b++) c.TS[f * NN + c.IX(a, b, k)] = to_sm(dot<6, 5>(&M.s[(size_t)b * nB], 1, p, 1, nB));
      } else {
        for (int b = 0; b < nB; b++) {
          F I = c.first ? dot<6, 5>(&g->V4.s[(size_t)b * nB], 1, p, 1, nB)
                        : fdiv(c.hv2 * dot<6, 5>(&g->QQ.s[(size_t)b * nB], 1, p, 1, nB), c.e4[b]);
          size_t ix = FS * NN + c.IX(a, b, k); c.Gn[ix] = c.Bt[ix] + I;
        }
      }
    }
    // stage 2: along ξ (Q_ξ)
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
};
