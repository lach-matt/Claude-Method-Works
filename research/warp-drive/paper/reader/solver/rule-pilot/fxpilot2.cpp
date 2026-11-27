// fxpilot.cpp: S-RULE pilot.  The corner cell (first column, first row) of a solver configuration, solved
//   (a) by the solver's own solve_cell (Real = qd with -DUSE_QD, or dd), and
//   (b) by plain Picard sweeps G <- B + I[Psi(G) - Psi(seed)] in fixed point fx<L> (B = 64 (L - 1) bits), every
//       product floored, every matrix-vector product a fused (exact) dot product floored once, the right-hand side the
//       generated straight-line program rhs_eval evaluated on full values (no difference arithmetic).
// The geometry, seed values, boundary data and spectral constants are taken from the solver (converted exactly from
// its Real) -- the rule computes them itself; their cost is a one-off per cell and is not measured here.
// usage: fxpilot config nsweeps [ref]     (ref = 1: also run solve_cell and compare)
#define BSOLV_NO_MAIN
#include "solver.cpp"
#include "fx.h"
#ifndef FXL
#define FXL 6
#endif
typedef fx<FXL> F;
static F toF(const Real& a) {
#ifdef USE_QD
  return from_double<FXL>(a.hi) + from_double<FXL>(a.l1) + from_double<FXL>(a.l2) + from_double<FXL>(a.l3);
#else
  return from_double<FXL>(a.hi) + from_double<FXL>(a.lo);
#endif
}
static double now() { return std::chrono::duration<double>(std::chrono::steady_clock::now().time_since_epoch()).count(); }

int main(int argc, char** argv) {
  read_config(argv[1]); int nsw = atoi(argv[2]); int doref = argc > 3 ? atoi(argv[3]) : 1;
  omp_set_num_threads(1); load_consts(CF.consts);
  A_CH = Real(1.0) / Real(500.0); XI_N1 = asinh(Real(-9.0) / A_CH); V_N0 = Real(0.5);
  std::string X = "X" + std::to_string(CF.M);
  const Mat& xn = C_(X + "_x"); NX = CF.M + 1; XN.assign(xn.a.begin(), xn.a.end());
  D1x = &C_(X + "_D1"); D2x = &C_(X + "_D2");
  for (auto& q : D1x->a) D1d.push_back(lead2(q)); for (auto& q : D2x->a) D2d.push_back(lead2(q));
  for (int i = 0; i < jEND; i++) JI[i] = jidx(JN[i]);
  for (int i = 0; i < RHS_NK; i++) KC.push_back(Real((double)RHS_KNUM[i]) / Real((double)RHS_KDEN[i]));
  for (int i = 0; i < RHS_NK; i++) { KClo.push_back(LowReal((double)RHS_KNUM[i]) / LowReal((double)RHS_KDEN[i])); KCd.push_back((double)RHS_KNUM[i] / (double)RHS_KDEN[i]); }
  for (auto& q : D1x->a) D1lo.push_back(cvt<LowReal>(q)); for (auto& q : D2x->a) D2lo.push_back(cvt<LowReal>(q));
  CF.floor = 1e-300; CF.tol = 1e-300;          // the reference runs to its own stall
  std::vector<Real> xb = breaks(XI_N1, CF.xi_hi, CF.ncol[0], CF.xib[0]);
  std::vector<Real> vb = breaks(V_N0, CF.v_hi, CF.nrow[0], CF.vbk[0]);
  Geom g0 = make_geom(XI_N1, XI_N1 + Real(1e-3), vb[0], vb[1], true);
  Edge left; { std::vector<Real> bG, bRv, tG, tR; n1_row(g0, bG, bRv, vb[0], left, tG, tR); }
  Geom g = make_geom(xb[0], xb[1], vb[0], vb[1], true);
  const int nA = g.nA, nB = g.nB; const size_t NN = (size_t)nA * nB * NX;
  fprintf(stderr, "cell: nA %d nB %d NX %d nodes %zu, fx limbs %d (B = %d bits)\n", nA, nB, NX, NN, FXL, 64 * (FXL - 1));
  std::vector<Real> Gref, svTop; double tref = 0;
  if (doref) { double t0 = now(); CellOut co = solve_cell(g, left, nullptr, V_N0, Gref, svTop); tref = now() - t0;
    fprintf(stderr, "reference solve_cell: %.1f s, outer %d, inner sweeps %d, last %.2e\n", tref, co.outer, co.sweeps, co.last); }
  // ---- fixed point
  double t0 = now();
  std::vector<F> Bf(NF * NN), G(NF * NN), Gn(NF * NN);
  for (int f = 0; f < NF; f++) for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++)
    Bf[f * NN + IX(a, b, k, nB)] = f < 4 ? toF(left.G[((size_t)f * nB + b) * NX + k]) : F(0);
  struct SF { F R, iRs, Ru, Rv, Wv, OM2, iOM2, du, idu; };
  std::vector<SF> sd((size_t)nA * nB);
  for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) { Seed s = seed_at(g.xi[a], g.v[b]); SF& q = sd[a * nB + b];
    q.R = toF(s.R); q.Ru = toF(s.Ru); q.Rv = toF(s.Rv); q.Wv = toF(s.Wv); q.OM2 = toF(s.OM2); q.du = toF(s.dudxi);
    q.iRs = recip(q.R); q.iOM2 = recip(q.OM2); q.idu = recip(q.du); }
  std::vector<F> E3(nB), E4(nB), iE3(nB), iE2(nB), XF(NX), KF(RHS_NK);
  for (int b = 0; b < nB; b++) { Real e = g.v[b] - V_N0; F ef = toF(e); E3[b] = ef * ef * ef; E4[b] = E3[b] * ef; iE3[b] = recip(E3[b]); iE2[b] = recip(ef * ef); }
  for (int k = 0; k < NX; k++) XF[k] = toF(XN[k]);
  for (int i = 0; i < RHS_NK; i++) KF[i] = toF(KC[i]);
  auto conv = [&](const Mat& m) { std::vector<F> o(m.a.size()); for (size_t i = 0; i < o.size(); i++) o[i] = toF(m.a[i]); return o; };
  std::vector<F> Dv = conv(*g.Dv), Dx = conv(*g.Dx), D1 = conv(*D1x), D2 = conv(*D2x), W4 = conv(*g.W4), V4 = conv(*g.V4), Qx = conv(*g.Qx);
  F ihv = recip(toF(g.hv)), ihx = recip(toF(g.hxi)), hx = toF(g.hxi);
  // Psi at the seed (D = 0) per node, for the difference Psi(seed + D) - Psi(seed)
  auto jets_full = [&](const SF& s, const F* D, const F* Du, const F* Dv_, const F* Dx_, const F* Dxx, const F* Dvx, const F& x, F* J) {
    F R = s.R + D[FR]; J[jR] = R; J[jiR] = recip(R);
    F S = divi(muli(D[FM], 1) + x * D[FM] + D[FN] - x * D[FN], 3);
    J[jES] = fexp<FXL, 45>(S); J[jiES] = fexp<FXL, 45>(-S);
    F e2 = fexp<FXL, 45>(muli(D[FW], 2)), em2 = fexp<FXL, 45>(muli(D[FW], -2));
    J[jOM2] = s.OM2 * e2; J[jiOM2] = s.iOM2 * em2;
    J[jRu] = s.Ru + Du[FR]; J[jRv] = s.Rv + Dv_[FR]; J[jRx] = Dx_[FR]; J[jRxx] = Dxx[FR]; J[jRvx] = Dvx[FR];
    J[jWv] = s.Wv + Dv_[FW]; J[jWx] = Dx_[FW]; J[jWxx] = Dxx[FW]; J[jWvx] = Dvx[FW];
    for (int q = 0; q < 2; q++) { int f = q ? FN : FM; int o = q ? jn_ : jm_;
      J[o] = D[f]; J[o + 1] = Du[f]; J[o + 2] = Dv_[f]; J[o + 3] = Dx_[f]; J[o + 4] = Dxx[f]; J[o + 5] = Dvx[f]; }
    J[js_] = D[FS]; J[jsv] = Dv_[FS]; J[jsx] = Dx_[FS]; J[jsvx] = Dvx[FS];
  };
  std::vector<F> Psi0((size_t)5 * NN);
  { F Z[NF]; for (auto& z : Z) z = F(0);
    for (size_t idx = 0; idx < NN; idx++) { int k = idx % NX; size_t ab = idx / NX; F J[jEND], Jp[RHS_NJ], o[5];
      jets_full(sd[ab], Z, Z, Z, Z, Z, Z, XF[k], J); for (int i = 0; i < jEND; i++) Jp[JI[i]] = J[i];
      rhs_eval(Jp, KF.data(), XF[k], o); for (int i = 0; i < 5; i++) Psi0[i * NN + idx] = o[i]; } }
  double tsetup = now() - t0;
  G = Bf;
  std::vector<F> Gv(NF * NN), Gxi(3 * NN), Gx(NF * NN), Gxx(4 * NN), Gvx(NF * NN), Psi(4 * NN), Phi(NN), t1(NN);
  double tsw = 0; std::vector<double> hist;
  for (int sw = 0; sw < nsw; sw++) {
    double ts = now();
    // derivatives (fused dot products)
    for (int f = 0; f < NF; f++) for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) {
      acc<FXL> s; for (int bb = 0; bb < nB; bb++) s.add(Dv[b * nB + bb], G[f * NN + IX(a, bb, k, nB)]);
      Gv[f * NN + IX(a, b, k, nB)] = s.get() * ihv;
      if (f < 3) { acc<FXL> s2; for (int aa = 0; aa < nA; aa++) s2.add(Dx[a * nA + aa], G[f * NN + IX(aa, b, k, nB)]); Gxi[f * NN + IX(a, b, k, nB)] = s2.get() * ihx; }
    }
    auto xap = [&](const std::vector<F>& Dm, const F* in, F* out, int rows) {
      for (int r = 0; r < rows; r++) for (int k = 0; k < NX; k++) { acc<FXL> s; for (int l = 0; l < NX; l++) s.add(Dm[(size_t)k * NX + l], in[(size_t)r * NX + l]); out[(size_t)r * NX + k] = s.get(); } };
    xap(D1, G.data(), Gx.data(), NF * nA * nB); xap(D2, G.data(), Gxx.data(), 4 * nA * nB); xap(D1, Gv.data(), Gvx.data(), NF * nA * nB);
    // right-hand sides
    for (size_t idx = 0; idx < NN; idx++) {
      int k = idx % NX; size_t ab = idx / NX; int b = ab % nB; const SF& s = sd[ab];
      F D[NF], Du[NF], Dvv[NF], Dxx_[NF], Dxx2[NF], Dvx[NF];
      for (int f = 0; f < NF; f++) {
        D[f] = E4[b] * G[f * NN + idx]; Dxx_[f] = E4[b] * Gx[f * NN + idx];
        Dvv[f] = muli(E3[b] * G[f * NN + idx], 4) + E4[b] * Gv[f * NN + idx];
        Dvx[f] = muli(E3[b] * Gx[f * NN + idx], 4) + E4[b] * Gvx[f * NN + idx];
        Dxx2[f] = f < 4 ? E4[b] * Gxx[f * NN + idx] : F(0);
        Du[f] = f < 3 ? (E4[b] * Gxi[f * NN + idx]) * s.idu : F(0);
      }
      F J[jEND], Jp[RHS_NJ], o[5];
      jets_full(s, D, Du, Dvv, Dxx_, Dxx2, Dvx, XF[k], J); for (int i = 0; i < jEND; i++) Jp[JI[i]] = J[i];
      rhs_eval(Jp, KF.data(), XF[k], o);
      Psi[FR * NN + idx] = s.du * (o[2] - Psi0[2 * NN + idx]); Psi[FM * NN + idx] = s.du * (o[0] - Psi0[0 * NN + idx]);
      Psi[FN * NN + idx] = s.du * (o[1] - Psi0[1 * NN + idx]); Psi[FW * NN + idx] = s.du * (o[3] - Psi0[3 * NN + idx]);
      Phi[idx] = o[4] - Psi0[4 * NN + idx];
    }
    // integration (first row: W4, V4 on sigma; Q in xi) and the update G <- B + I[...]
    double dmax = 0, gmax = 1e-300;
    for (int f = 0; f < NF; f++) {
      if (f < 4) {
        for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) {
          acc<FXL> s; for (int bb = 0; bb < nB; bb++) s.add(W4[b * nB + bb], Psi[f * NN + IX(a, bb, k, nB)] * iE3[bb]); t1[IX(a, b, k, nB)] = s.get(); }
        for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) {
          acc<FXL> s; for (int aa = 0; aa < nA; aa++) s.add(Qx[a * nA + aa], t1[IX(aa, b, k, nB)]);
          size_t i = f * NN + IX(a, b, k, nB); Gn[i] = Bf[i] + hx * s.get(); }
      } else {
        for (int a = 0; a < nA; a++) for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) {
          acc<FXL> s; for (int bb = 0; bb < nB; bb++) s.add(V4[b * nB + bb], Phi[IX(a, bb, k, nB)] * iE2[bb]);
          size_t i = FS * NN + IX(a, b, k, nB); Gn[i] = Bf[i] + s.get(); }
      }
    }
    double dfm[NF] = {0}; int kat[NF] = {0};
    for (int f = 0; f < NF; f++) for (size_t j = 0; j < NN; j++) { size_t i = f * NN + j; double dd_ = std::fabs(to_dbl(Gn[i] - G[i]));
      if (dd_ > dfm[f]) { dfm[f] = dd_; kat[f] = j % NX; } dmax = std::max(dmax, dd_); gmax = std::max(gmax, std::fabs(to_dbl(Gn[i]))); }
    // high angular modes of the update: Chebyshev coefficients of the update of m at one (a, b), top quarter of k
    double hi = 0, lo = 0; { int a = nA / 2, b = nB / 2; for (int n = 0; n < NX; n++) { double c = 0;
        for (int k = 0; k < NX; k++) { double w = (k == 0 || k == NX - 1) ? 0.5 : 1.0; c += w * std::cos(M_PI * n * k / (NX - 1)) * to_dbl(Gn[FM * NN + IX(a, b, k, nB)] - G[FM * NN + IX(a, b, k, nB)]); }
        c = std::fabs(c) * 2.0 / (NX - 1); if (n >= 3 * (NX - 1) / 4) hi = std::max(hi, c); else lo = std::max(lo, c); } }
    printf("    per field |dG|: R %.2e m %.2e n %.2e W %.2e s %.2e (x-node of max m: %d); update of m at mid node: low modes %.2e, top quarter %.2e\n",
           dfm[0], dfm[1], dfm[2], dfm[3], dfm[4], kat[1], lo, hi);
    G.swap(Gn);
    double dt = now() - ts; tsw += dt;
    hist.push_back(dmax / gmax);
    printf("sweep %3d: |G_new - G|/|G| = %.3e  (%.2f s)\n", sw + 1, dmax / gmax, dt); fflush(stdout);
    if (dmax == 0) { printf("fixed point reached exactly (no bit changes)\n"); break; }
  }
  printf("setup (fixed point, excl. seed and constants) %.2f s; mean sweep %.2f s\n", tsetup, tsw / std::max<size_t>(1, hist.size()));
  if (doref) {
    double emax[NF] = {0}, gm[NF] = {1e-300, 1e-300, 1e-300, 1e-300, 1e-300};
    for (int f = 0; f < NF; f++) for (size_t i = 0; i < NN; i++) {
      Real gr = Gref[f * NN + i]; F d = G[f * NN + i] - toF(gr);
      emax[f] = std::max(emax[f], std::fabs(to_dbl(d))); gm[f] = std::max(gm[f], std::fabs(to_double(gr))); }
    for (int f = 0; f < NF; f++) printf("field %d: max|G_fx - G_ref| = %.3e, max|G_ref| = %.3e, relative %.3e\n", f, emax[f], gm[f], emax[f] / gm[f]);
    printf("reference time %.1f s\n", tref);
  }
  // dump G (as doubles of the difference to a later run is not needed); write a digest of the fixed-point state
  unsigned long long h = 1469598103934665603ULL;
  for (auto& q : G) for (int i = 0; i < FXL; i++) { h ^= q.w[i]; h *= 1099511628211ULL; }
  printf("FNV-1a of the fixed-point state: %016llx\n", h);
}
