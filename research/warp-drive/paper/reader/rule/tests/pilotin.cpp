// pilotin.cpp: the inputs of the pilot's test cell (the corner cell of solver/rule-pilot/p1.cfg) as the quad-double
// solver computes them -- nodes, matrices, seed values, N1 data, constants -- each converted exactly to 2^-320 Z (a
// quad-double is a sum of four doubles, all of whose bits lie above 2^-320 here; the program checks this), written to a
// file for `rule pilotcell`.  With a third argument 1 it also runs the solver's own solve_cell in quad-double to its
// stall (as S-RULE §5.2 did) and writes that G as the reference.  Not part of the rule: a test harness.
// build: g++ -O2 -std=c++17 -fopenmp -DUSE_QD -I../solver -I. -o pilotin tests/pilotin.cpp -l:libgmp.so.10
#define BSOLV_NO_MAIN
#include "solver.cpp"
#include "gmpmin.h"
#include <x86intrin.h>
static long inexact = 0;
static void put(std::string& o, const Real& a) {              // exact 2^320 a as 6 two's-complement limbs
  Z acc(0), t; double p[4]; to_parts(a, p);
  for (int i = 0; i < NW; i++) {
    double d = p[i]; if (d == 0) continue;
    int e; double m = std::frexp(std::fabs(d), &e); long long M = (long long)std::ldexp(m, 53); int sh = e - 53 + 320;
    mpz_set_si(t.v, d < 0 ? -M : M);                         // each part floored to 2^-320 Z (as the pilot's from_double)
    if (sh >= 0) mpz_mul_2exp(t.v, t.v, sh); else { inexact++; mpz_fdiv_q_2exp(t.v, t.v, -sh); }
    mpz_add(acc.v, acc.v, t.v);
  }
  uint64_t w[6] = {0}; Z mag; mpz_abs(mag.v, acc.v); size_t cnt; mpz_export(w, &cnt, -1, 8, 0, 0, mag.v);
  if (mpz_sgn(acc.v) < 0) { unsigned char c = 1; for (int i = 0; i < 6; i++) { unsigned long long r; c = _addcarry_u64(c, ~w[i], 0, &r); w[i] = r; } }
  o.append((const char*)w, 48);
}
static void putv(std::string& o, const char* name, const std::vector<Real>& v) {
  o += name; o.push_back('\n'); uint64_t n = v.size(); o.append((const char*)&n, 8); for (auto& x : v) put(o, x);
}
int main(int argc, char** argv) {
  read_config(argv[1]); omp_set_num_threads(1); load_consts(CF.consts); bool ref = argc > 3 && atoi(argv[3]);
  A_CH = Real(1.0) / Real(500.0); XI_N1 = asinh(Real(-9.0) / A_CH); V_N0 = Real(0.5);
  std::string X = "X" + std::to_string(CF.M); const Mat& xn = C_(X + "_x"); NX = CF.M + 1; XN.assign(xn.a.begin(), xn.a.end());
  D1x = &C_(X + "_D1"); D2x = &C_(X + "_D2");
  for (auto& q : D1x->a) D1d.push_back(lead2(q)); for (auto& q : D2x->a) D2d.push_back(lead2(q));
  for (int i = 0; i < jEND; i++) JI[i] = jidx(JN[i]);
  for (int i = 0; i < RHS_NK; i++) KC.push_back(Real((double)RHS_KNUM[i]) / Real((double)RHS_KDEN[i]));
  for (int i = 0; i < RHS_NK; i++) { KClo.push_back(LowReal((double)RHS_KNUM[i]) / LowReal((double)RHS_KDEN[i])); KCd.push_back((double)RHS_KNUM[i] / (double)RHS_KDEN[i]); }
  for (auto& q : D1x->a) D1lo.push_back(cvt<LowReal>(q)); for (auto& q : D2x->a) D2lo.push_back(cvt<LowReal>(q));
  std::vector<Real> xb = breaks(XI_N1, CF.xi_hi, CF.ncol[0], CF.xib[0]), vb = breaks(V_N0, CF.v_hi, CF.nrow[0], CF.vbk[0]);
  Geom g0 = make_geom(XI_N1, XI_N1 + Real(1e-3), vb[0], vb[1], true);
  Edge left; { std::vector<Real> bG, bRv, tG, tR; n1_row(g0, bG, bRv, vb[0], left, tG, tR); }
  Geom g = make_geom(xb[0], xb[1], vb[0], vb[1], true);
  const int nA = g.nA, nB = g.nB; const size_t NN = (size_t)nA * nB * NX;
  std::string o = "RULEPI1\n"; int32_t d[3] = {nA, nB, NX}; o.append((const char*)d, 12);
  putv(o, "Dv", g.Dv->a); putv(o, "Dxi", g.Dx->a); putv(o, "D1x", D1x->a); putv(o, "D2x", D2x->a);
  putv(o, "W4", g.W4->a); putv(o, "V4", g.V4->a); putv(o, "Qxi", g.Qx->a); putv(o, "Qv", g.Qv->a);
  putv(o, "x", XN); putv(o, "K", KC);
  std::vector<Real> eps(nB); for (int b = 0; b < nB; b++) eps[b] = g.v[b] - V_N0; putv(o, "eps", eps);
  std::vector<Real> sd[6]; for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) { Seed s = seed_at(g.xi[a], g.v[b]);
    sd[0].push_back(s.R); sd[1].push_back(s.Ru); sd[2].push_back(s.Rv); sd[3].push_back(s.Wv); sd[4].push_back(s.OM2); sd[5].push_back(s.dudxi); }
  putv(o, "sR", sd[0]); putv(o, "sRu", sd[1]); putv(o, "sRv", sd[2]); putv(o, "sWv", sd[3]); putv(o, "sOM2", sd[4]); putv(o, "sdu", sd[5]);
  putv(o, "h", {g.hxi, g.hv}); putv(o, "left", left.G);
  if (ref) {
    std::vector<Real> Gref, svTop; CF.floor = 1e-300; CF.tol = 1e-300;
    auto t0 = std::chrono::steady_clock::now(); CellOut co = solve_cell(g, left, nullptr, V_N0, Gref, svTop);
    fprintf(stderr, "reference solve_cell (qd): %.1f s, outer %d, inner sweeps %d, last %.2e\n",
            std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count(), co.outer, co.sweeps, co.last);
    putv(o, "Gref", Gref);
    // the reference cell's node coordinates, for the comparison with the rule's own cell
    putv(o, "xi", g.xi); putv(o, "v", g.v);
  }
  FILE* f = fopen(argv[2], "wb"); fwrite(o.data(), 1, o.size(), f); fclose(f);
  fprintf(stderr, "wrote %s (%zu bytes); inexact conversions %ld\n", argv[2], o.size(), inexact);
}
