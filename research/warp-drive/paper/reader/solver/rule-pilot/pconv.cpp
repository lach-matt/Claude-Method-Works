// pconv.cpp: S-RULE pilot of the cell discretization error.  The corner cell of a configuration solved by the
// solver's solve_cell (quad-double) at several (p_xi, p_v), each compared at the nodes of the coarsest with the
// finest (barycentric interpolation in xi and v; same x-nodes).
// usage: pconv config consts1 pxi1 pv1 consts2 pxi2 pv2 ...   (finest last)
#define BSOLV_NO_MAIN
#include "solver.cpp"
static double now() { return std::chrono::duration<double>(std::chrono::steady_clock::now().time_since_epoch()).count(); }
int main(int argc, char** argv) {
  read_config(argv[1]); omp_set_num_threads(1);
  int nc = (argc - 2) / 3;
  for (int c = 0; c < nc; c++) load_consts(argv[2 + 3 * c]);
  A_CH = Real(1.0) / Real(500.0); XI_N1 = asinh(Real(-9.0) / A_CH); V_N0 = Real(0.5);
  std::string X = "X" + std::to_string(CF.M);
  const Mat& xn = C_(X + "_x"); NX = CF.M + 1; XN.assign(xn.a.begin(), xn.a.end());
  D1x = &C_(X + "_D1"); D2x = &C_(X + "_D2");
  for (auto& q : D1x->a) D1d.push_back(lead2(q)); for (auto& q : D2x->a) D2d.push_back(lead2(q));
  for (int i = 0; i < jEND; i++) JI[i] = jidx(JN[i]);
  for (int i = 0; i < RHS_NK; i++) KC.push_back(Real((double)RHS_KNUM[i]) / Real((double)RHS_KDEN[i]));
  for (int i = 0; i < RHS_NK; i++) { KClo.push_back(LowReal((double)RHS_KNUM[i]) / LowReal((double)RHS_KDEN[i])); KCd.push_back((double)RHS_KNUM[i] / (double)RHS_KDEN[i]); }
  for (auto& q : D1x->a) D1lo.push_back(cvt<LowReal>(q)); for (auto& q : D2x->a) D2lo.push_back(cvt<LowReal>(q));
  CF.floor = 1e-300; CF.tol = 1e-300;
  std::vector<Real> xb = breaks(XI_N1, CF.xi_hi, CF.ncol[0], CF.xib[0]);
  std::vector<Real> vb = breaks(V_N0, CF.v_hi, CF.nrow[0], CF.vbk[0]);
  std::vector<Geom> gs; std::vector<std::vector<Real>> Gs;
  for (int c = 0; c < nc; c++) {
    CF.pxi = atoi(argv[3 + 3 * c]); CF.pv = atoi(argv[4 + 3 * c]);
    Geom g0 = make_geom(XI_N1, XI_N1 + Real(1e-3), vb[0], vb[1], true);
    Edge left; { std::vector<Real> bG, bRv, tG, tR; n1_row(g0, bG, bRv, vb[0], left, tG, tR); }
    Geom g = make_geom(xb[0], xb[1], vb[0], vb[1], true);
    std::vector<Real> G, sv; double t0 = now(); CellOut co = solve_cell(g, left, nullptr, V_N0, G, sv);
    fprintf(stderr, "p %d/%d: %.1f s, outer %d, sweeps %d, last %.2e\n", CF.pxi, CF.pv, now() - t0, co.outer, co.sweeps, co.last);
    gs.push_back(g); Gs.push_back(G);
  }
  // compare every level with the finest at the nodes of that level
  const Geom& gf = gs.back(); const std::vector<Real>& Gf = Gs.back(); size_t NNf = (size_t)gf.nA * gf.nB * NX;
  for (int c = 0; c + 1 < nc; c++) {
    const Geom& g = gs[c]; size_t NN = (size_t)g.nA * g.nB * NX;
    double em[NF] = {0}, gm[NF] = {0};
    for (int a = 0; a < g.nA; a++) { std::vector<Real> wa; bary_weights(gf.xi, *gf.wx, g.xi[a], wa);
      for (int b = 0; b < g.nB; b++) { std::vector<Real> wb; bary_weights(gf.v, *gf.wv, g.v[b], wb);
        for (int f = 0; f < NF; f++) for (int k = 0; k < NX; k++) {
          Real s(0.0); for (int aa = 0; aa < gf.nA; aa++) { Real s1(0.0); for (int bb = 0; bb < gf.nB; bb++) s1 += wb[bb] * Gf[f * NNf + IX(aa, bb, k, gf.nB)]; s += wa[aa] * s1; }
          Real d = s - Gs[c][f * NN + IX(a, b, k, g.nB)];
          em[f] = std::max(em[f], std::fabs(to_double(d))); gm[f] = std::max(gm[f], std::fabs(to_double(s))); } } }
    printf("p %s/%s against the finest: ", argv[3 + 3 * c], argv[4 + 3 * c]);
    for (int f = 0; f < NF; f++) printf(" %c %.2e (rel %.2e)", "RmnWs"[f], em[f], em[f] / gm[f]); printf("\n");
  }
}
