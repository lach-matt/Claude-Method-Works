// jets.cpp: the development's v-jets on N0 by the transport hierarchy (independent of the cell solver).
// F = F_seed(u, 1/2 + e) + sum_{k >= 4} a_k(u, x) e^k for F = R, m, n, W (s: sum_{k >= 5} s_k e^k).  At each order k:
//   s_k = [Phi]_{k-2} / (k (k - 1))            (the shift equation s_vv = Phi, algebraic in lower orders)
//   d_u a_k = A(u, x) a_k + f_k / k            (A = dX/dF_v on the seed, f_k = [X - X_seed]_{k-1} with a_k = 0)
// with a_k(-10, x) the Taylor coefficients of the data on N1 at v = 1/2; X = (R, m, n, W)_uv of the axis-regular
// system, evaluated in truncated Taylor arithmetic in e, in difference form about the seed's series.
// usage: jets config K out.bin    (the config of a solver run: its xi-columns, p_xi, M; orders 4..K-1)
#define BSOLV_NO_MAIN
#include "solver.cpp"

static const int KT = 12;              // series length (orders 0..11)
struct Tay { Real c[KT]; Tay() { for (auto& q : c) q = Real(0.0); } Tay(double a) { for (auto& q : c) q = Real(0.0); c[0] = Real(a); }
             Tay(const Real& a) { for (auto& q : c) q = Real(0.0); c[0] = a; } };
static int KTRUNC = KT;
static Tay operator+(const Tay& a, const Tay& b) { Tay r; for (int i = 0; i < KTRUNC; i++) r.c[i] = a.c[i] + b.c[i]; return r; }
static Tay operator-(const Tay& a, const Tay& b) { Tay r; for (int i = 0; i < KTRUNC; i++) r.c[i] = a.c[i] - b.c[i]; return r; }
static Tay operator-(const Tay& a) { Tay r; for (int i = 0; i < KTRUNC; i++) r.c[i] = -a.c[i]; return r; }
static Tay operator*(const Tay& a, const Tay& b) { Tay r; for (int i = 0; i < KTRUNC; i++) { Real s(0.0); for (int j = 0; j <= i; j++) s += a.c[j] * b.c[i - j]; r.c[i] = s; } return r; }
static Tay operator*(const Real& k, const Tay& a) { Tay r; for (int i = 0; i < KTRUNC; i++) r.c[i] = k * a.c[i]; return r; }
static Tay operator*(const Tay& a, const Real& k) { return k * a; }
static Tay operator+(const Real& k, const Tay& a) { Tay r = a; r.c[0] = r.c[0] + k; return r; }
static Tay operator+(const Tay& a, const Real& k) { return k + a; }
static Tay operator-(const Real& k, const Tay& a) { return k + (-a); }
static Tay operator-(const Tay& a, const Real& k) { return a + (-k); }
static Tay& operator+=(Tay& a, const Tay& b) { a = a + b; return a; }
static Tay tinv(const Tay& a) { Tay r; r.c[0] = Real(1.0) / a.c[0];
  for (int i = 1; i < KTRUNC; i++) { Real s(0.0); for (int j = 1; j <= i; j++) s += a.c[j] * r.c[i - j]; r.c[i] = -s * r.c[0]; } return r; }
static Tay texp(const Tay& a) { Tay r; r.c[0] = exp(a.c[0]);   // r' = a' r
  for (int i = 1; i < KTRUNC; i++) { Real s(0.0); for (int j = 1; j <= i; j++) s += Real((double)j) * a.c[j] * r.c[i - j]; r.c[i] = s / Real((double)i); } return r; }
static Tay tlog(const Tay& a) { Tay r; r.c[0] = log(a.c[0]);   // r' = a'/a
  for (int i = 1; i < KTRUNC; i++) { Real s = Real((double)i) * a.c[i]; for (int j = 1; j < i; j++) s -= Real((double)j) * r.c[j] * a.c[i - j]; r.c[i] = s / (Real((double)i) * a.c[0]); } return r; }
static Tay tder(const Tay& a) { Tay r; for (int i = 0; i + 1 < KTRUNC; i++) r.c[i] = Real((double)(i + 1)) * a.c[i + 1]; return r; }
static Tay tsin(const Tay& a, Tay& co) { // sin and cos of a series
  Tay s, c; Real s0 = sin(a.c[0]), c0 = cos(a.c[0]); s.c[0] = s0; c.c[0] = c0;
  for (int i = 1; i < KTRUNC; i++) { Real ss(0.0), cc(0.0); for (int j = 1; j <= i; j++) { ss += Real((double)j) * a.c[j] * c.c[i - j]; cc += Real((double)j) * a.c[j] * s.c[i - j]; }
    s.c[i] = ss / Real((double)i); c.c[i] = -cc / Real((double)i); }
  co = c; return s; }

typedef Diff<Tay> DTy;
static DTy operator*(const Real& c, const DTy& a) { return DTy(c * a.s, c * a.d); }
static DTy operator*(const DTy& a, const Real& c) { return DTy(c * a.s, c * a.d); }
static DTy operator+(const Real& c, const DTy& a) { return DTy(c + a.s, a.d); }
static DTy operator+(const DTy& a, const Real& c) { return DTy(a.s + c, a.d); }
static DTy operator-(const Real& c, const DTy& a) { return DTy(c - a.s, -a.d); }
static DTy operator-(const DTy& a, const Real& c) { return DTy(a.s - c, a.d); }

// the seed's series in e at (u, 1/2): R, R_u, R_v, W_v, OM2
struct SeedS { Tay R, Ru, Rv, Wv, OM2, Ruv, Wuv; };
static SeedS seed_series(const Real& xi) {
  Seed s0 = seed_at(xi, V_N0); Real up1 = A_CH * sinh(xi), u = up1 - Real(1.0); Real g = Real(1.0) - Real(1.0) / (u * u);
  SeedS S; Tay R(s0.R);
  for (int it = 0; it < KTRUNC + 1; it++) {     // R_v = (1 - R^-2)/2, by Picard on the series
    Tay iR = tinv(R); Tay f = Real(1.0) - iR * iR; Tay Rn(s0.R);
    for (int i = 1; i < KTRUNC; i++) Rn.c[i] = Real(0.5) * f.c[i - 1] / Real((double)i);
    R = Rn;
  }
  Tay iR = tinv(R), f = Real(1.0) - iR * iR;
  S.R = R; S.Rv = Real(0.5) * f; S.Ru = (-Real(1.0) / g) * f; S.Wv = Real(0.5) * (iR * iR * iR); S.OM2 = (Real(1.0) / (Real(2.0) * g)) * f;
  S.Ruv = iR * iR * iR * S.Ru; S.Wuv = Real(-1.5) * (iR * iR * iR * iR) * S.Ru;
  return S;
}
// data on N1 as series: (m, n) and D_R (R - R_seed) at (-10, 1/2 + e)
static void n1_series(const Real& x, Tay& m, Tay& n, Tay& DR) {
  SeedS S = seed_series(XI_N1);
  Tay e; e.c[1] = Real(1.0);
  Tay co; Tay sn = tsin((R_PI / Real(3.0)) * e, co);
  Tay env = sn * sn * sn * sn;
  Tay th = (V_N0 / CF.lam) + (Real(1.0) / CF.lam) * e; Tay cth; Tay sth = tsin(th, cth);
  Tay r32 = texp(Real(-1.5) * tlog(S.R));
  Real h = sqrt(Real(2.0) / (Real(1.0) + x * x));
  Tay pre = (h * CF.lam * Real(0.5) * CF.amp) * (r32 * env);
  m = pre * cth; n = pre * sth;
  Tay mv = tder(m), nv = tder(n);
  Tay Pv = (Real(2.0) * (Real(1.0) + x) / Real(3.0)) * mv - ((Real(1.0) - x) / Real(3.0)) * nv;
  Tay Qv = (Real(2.0) * (Real(1.0) - x) / Real(3.0)) * nv - ((Real(1.0) + x) / Real(3.0)) * mv;
  Tay sh = Pv * Pv + Qv * Qv + (Pv + Qv) * (Pv + Qv);
  DR = Tay(0.0);
  for (int it = 0; it < KTRUNC + 1; it++) {     // D'' = 2 W_v D' - (R_s + D) shear/3, D = D' = 0 at e = 0
    Tay rhs = Real(2.0) * S.Wv * tder(DR) - (Real(1.0) / Real(3.0)) * (S.R + DR) * sh;
    Tay Dn; for (int i = 2; i < KTRUNC; i++) Dn.c[i] = rhs.c[i - 2] / Real((double)(i * (i - 1)));
    DR = Dn;
  }
}

int main(int argc, char** argv) {
  read_config(argv[1]); int K = atoi(argv[2]); if (K > KT) K = KT;
  omp_set_num_threads(CF.threads); load_consts(CF.consts);
  A_CH = Real(1.0) / Real(500.0); XI_N1 = asinh(Real(-9.0) / A_CH); V_N0 = Real(0.5);
  std::string X = "X" + std::to_string(CF.M); const Mat& xn = C_(X + "_x"); NX = CF.M + 1; XN.assign(xn.a.begin(), xn.a.end());
  D1x = &C_(X + "_D1"); D2x = &C_(X + "_D2");
  for (int i = 0; i < jEND; i++) JI[i] = jidx(JN[i]);
  for (int i = 0; i < RHS_NK; i++) KC.push_back(Real((double)RHS_KNUM[i]) / Real((double)RHS_KDEN[i]));
  std::vector<Real> xb[2] = {breaks(XI_N1, CF.xi_hi, CF.ncol[0], CF.xib[0]), breaks(XI_N1, CF.xi_lo, CF.ncol[1], CF.xib[1])};
  const Mat& Q = C_("L" + std::to_string(CF.pxi) + "_Q"); const Mat& tx = C_("L" + std::to_string(CF.pxi) + "_t");
  int nA = CF.pxi + 1;
  // nodes: per side, per column, nA xi-nodes (the solver's)
  struct Node { Real xi; SeedS S; Real dudxi; };
  std::vector<Node> nodes; std::vector<int> side_of, col_of;
  for (int sd = 0; sd < 2; sd++) for (size_t c = 0; c + 1 < xb[sd].size(); c++) for (int a = 0; a < nA; a++) {
    Real h = (xb[sd][c + 1] - xb[sd][c]) * Real(0.5); Node nd; nd.xi = xb[sd][c] + h * (tx.a[a] + Real(1.0));
    nd.S = seed_series(nd.xi); nd.dudxi = A_CH * cosh(nd.xi); nodes.push_back(nd); side_of.push_back(sd); col_of.push_back(c); }
  size_t NNd = nodes.size();
  // a[k][f][node][x] for f = R, m, n, W; s[k][node][x]; du[k][f][node][x] = d_u a_k
  std::vector<std::vector<Real>> a(KT, std::vector<Real>(4 * NNd * NX, Real(0.0))), du(KT, std::vector<Real>(4 * NNd * NX, Real(0.0)));
  std::vector<std::vector<Real>> s(KT + 1, std::vector<Real>(NNd * NX, Real(0.0)));
  std::vector<Real> Am(16 * NNd * NX, Real(0.0));     // A[node][x][f][f']
  // initial data on N1
  std::vector<Real> a0(KT * 4 * NX, Real(0.0));
  for (int k = 0; k < NX; k++) { Tay m, n, DR; n1_series(XN[k], m, n, DR);
    for (int q = 4; q < K; q++) { a0[(q * 4 + FR) * NX + k] = DR.c[q]; a0[(q * 4 + FM) * NX + k] = m.c[q]; a0[(q * 4 + FN) * NX + k] = n.c[q]; } }
  auto IXN = [&](int f, size_t nd, int k) { return ((size_t)f * NNd + nd) * NX + k; };
  // series evaluation at (node, x): returns delta X (4 series: R, m, n, W) and Phi (series), with a_q (q <= qmax), s_q (q <= smax)
  auto evaluate = [&](size_t nd, int k, int qmax, int smax, const Real* probe, Tay dX[4], Tay& dPhi) {
    const Node& N = nodes[nd]; const Real& x = XN[k];
    // x-derivatives of the a_q and s_q at this node: spectral
    auto xd = [&](const std::vector<Real>& v, int f, const Mat& D) { Real r(0.0); for (int l = 0; l < NX; l++) r += D(k, l) * v[IXN(f, nd, l)]; return r; };
    Tay D[4], Dx[4], Dxx[4], Du[4], Ds, Dsx;
    for (int f = 0; f < 4; f++) for (int q = 4; q <= qmax; q++) {
      D[f].c[q] = a[q][IXN(f, nd, k)]; Dx[f].c[q] = xd(a[q], f, *D1x); Dxx[f].c[q] = xd(a[q], f, *D2x); Du[f].c[q] = du[q][IXN(f, nd, k)]; }
    if (probe) for (int f = 0; f < 4; f++) D[f].c[qmax + 1] = probe[f];
    for (int q = 5; q <= smax; q++) { Ds.c[q] = s[q][nd * NX + k]; Real r(0.0); for (int l = 0; l < NX; l++) r += (*D1x)(k, l) * s[q][nd * NX + l]; Dsx.c[q] = r; }
    typedef Diff<Tay> DT; DT J[jEND];
    Tay zero;
    Tay Rt = N.S.R + D[FR]; Tay iRs = tinv(N.S.R), iRt = tinv(Rt);
    J[jR] = DT(N.S.R, D[FR]); J[jiR] = DT(iRs, iRt - iRs);
    Tay Sd = ((Real(1.0) + x) / Real(3.0)) * D[FM] + ((Real(1.0) - x) / Real(3.0)) * D[FN];
    Tay one(1.0); J[jES] = DT(one, texp(Sd) - one); J[jiES] = DT(one, texp(-Sd) - one);
    Tay e2 = texp(Real(2.0) * D[FW]) - one, em2 = texp(Real(-2.0) * D[FW]) - one, iO = tinv(N.S.OM2);
    J[jOM2] = DT(N.S.OM2, N.S.OM2 * e2); J[jiOM2] = DT(iO, iO * em2);
    J[jRu] = DT(N.S.Ru, Du[FR]); J[jRv] = DT(N.S.Rv, tder(D[FR])); J[jRx] = DT(zero, Dx[FR]); J[jRxx] = DT(zero, Dxx[FR]); J[jRvx] = DT(zero, tder(Dx[FR]));
    J[jWv] = DT(N.S.Wv, tder(D[FW])); J[jWx] = DT(zero, Dx[FW]); J[jWxx] = DT(zero, Dxx[FW]); J[jWvx] = DT(zero, tder(Dx[FW]));
    for (int qq = 0; qq < 2; qq++) { int f = qq ? FN : FM; int o = qq ? jn_ : jm_;
      J[o] = DT(zero, D[f]); J[o + 1] = DT(zero, Du[f]); J[o + 2] = DT(zero, tder(D[f])); J[o + 3] = DT(zero, Dx[f]); J[o + 4] = DT(zero, Dxx[f]); J[o + 5] = DT(zero, tder(Dx[f])); }
    J[js_] = DT(zero, Ds); J[jsv] = DT(zero, tder(Ds)); J[jsx] = DT(zero, Dsx); J[jsvx] = DT(zero, tder(Dsx));
    DT Jp[RHS_NJ]; for (int i = 0; i < jEND; i++) Jp[JI[i]] = J[i];
    DT o[5]; rhs_eval(Jp, KC.data(), x, o);
    dX[FR] = o[2].d; dX[FM] = o[0].d; dX[FN] = o[1].d; dX[FW] = o[3].d; dPhi = o[4].d;
  };
  // the seed coefficient matrix A = dX/dF_v (probe with a_4 = unit vector: [dX]_3 = 4 A e)
  KTRUNC = 5;
  #pragma omp parallel for schedule(dynamic)
  for (size_t nd = 0; nd < NNd; nd++) for (int k = 0; k < NX; k++) for (int fp = 0; fp < 4; fp++) {
    Real pr[4] = {Real(0.0), Real(0.0), Real(0.0), Real(0.0)}; pr[fp] = Real(1.0);
    Tay dX[4], dP; evaluate(nd, k, 3, 4, pr, dX, dP);
    for (int f = 0; f < 4; f++) Am[((nd * NX + k) * 4 + f) * 4 + fp] = dX[f].c[3] / Real(4.0);
  }
  FILE* lg = fopen((std::string(argv[3]) + ".log").c_str(), "w");
  for (int q = 4; q < K; q++) {
    KTRUNC = q + 1;
    // s_q from [Phi]_{q-2} (a up to q-1, s up to q-1)
    #pragma omp parallel for schedule(dynamic)
    for (size_t nd = 0; nd < NNd; nd++) for (int k = 0; k < NX; k++) {
      Tay dX[4], dP; evaluate(nd, k, q - 1, q - 1, nullptr, dX, dP);
      s[q][nd * NX + k] = dP.c[q - 2] / Real((double)(q * (q - 1)));
    }
    // forcing f_q = [dX]_{q-1} with a_q = 0, s up to q
    std::vector<Real> fq(4 * NNd * NX);
    #pragma omp parallel for schedule(dynamic)
    for (size_t nd = 0; nd < NNd; nd++) for (int k = 0; k < NX; k++) {
      Tay dX[4], dP; evaluate(nd, k, q - 1, q, nullptr, dX, dP);
      for (int f = 0; f < 4; f++) fq[IXN(f, nd, k)] = dX[f].c[q - 1];
    }
    // transport along each side, column by column: a(xi_i) = a(xi_0) + h sum_j Q_ij dudxi_j (A_j a_j + f_j/q)
    #pragma omp parallel for schedule(dynamic)
    for (int k = 0; k < NX; k++) for (int sd = 0; sd < 2; sd++) {
      Real start[4]; for (int f = 0; f < 4; f++) start[f] = a0[(q * 4 + f) * NX + k];
      for (size_t c = 0; c + 1 < xb[sd].size(); c++) {
        size_t base = 0; while (base < NNd && !(side_of[base] == sd && col_of[base] == (int)c)) base++;
        Real h = (xb[sd][c + 1] - xb[sd][c]) * Real(0.5);
        int n = 4 * nA; std::vector<Real> Mm((size_t)n * n, Real(0.0)), rhs(n);
        for (int i = 0; i < nA; i++) for (int f = 0; f < 4; f++) {
          int r = i * 4 + f; Mm[(size_t)r * n + r] = Real(1.0); Real b = start[f];
          for (int j = 0; j < nA; j++) { size_t nd = base + j; Real w = h * Q(i, j) * nodes[nd].dudxi;
            for (int fp = 0; fp < 4; fp++) Mm[(size_t)r * n + j * 4 + fp] -= w * Am[((nd * NX + k) * 4 + f) * 4 + fp];
            b += w * fq[IXN(f, nd, k)] / Real((double)q); }
          rhs[r] = b;
        }
        for (int p = 0; p < n; p++) {           // Gaussian elimination, partial pivoting
          int piv = p; for (int r = p + 1; r < n; r++) if (std::fabs(Mm[(size_t)r * n + p].hi) > std::fabs(Mm[(size_t)piv * n + p].hi)) piv = r;
          if (piv != p) { for (int cc = 0; cc < n; cc++) std::swap(Mm[(size_t)p * n + cc], Mm[(size_t)piv * n + cc]); std::swap(rhs[p], rhs[piv]); }
          for (int r = p + 1; r < n; r++) { Real fct = Mm[(size_t)r * n + p] / Mm[(size_t)p * n + p]; if (fct.hi == 0) continue;
            for (int cc = p; cc < n; cc++) Mm[(size_t)r * n + cc] -= fct * Mm[(size_t)p * n + cc]; rhs[r] -= fct * rhs[p]; }
        }
        std::vector<Real> sol(n);
        for (int r = n - 1; r >= 0; r--) { Real sm = rhs[r]; for (int cc = r + 1; cc < n; cc++) sm -= Mm[(size_t)r * n + cc] * sol[cc]; sol[r] = sm / Mm[(size_t)r * n + r]; }
        for (int j = 0; j < nA; j++) for (int f = 0; f < 4; f++) {
          size_t nd = base + j; a[q][IXN(f, nd, k)] = sol[j * 4 + f];
          Real d(0.0); for (int fp = 0; fp < 4; fp++) d += Am[((nd * NX + k) * 4 + f) * 4 + fp] * sol[j * 4 + fp];
          du[q][IXN(f, nd, k)] = d + fq[IXN(f, nd, k)] / Real((double)q);
        }
        for (int f = 0; f < 4; f++) start[f] = sol[(nA - 1) * 4 + f];
      }
    }
    fprintf(lg, "order %d done\n", q); fflush(lg);
  }
  // output: per side, per column: [order q = 4..K-1][a][field R m n W s][x]
  std::ofstream o(argv[3], std::ios::binary); o.write("BSOLH1", 6); o.write((char*)&nA, 4); o.write((char*)&NX, 4); o.write((char*)&NW, 4); o.write((char*)&K, 4);
  int nn = NNd; o.write((char*)&nn, 4);
  for (size_t nd = 0; nd < NNd; nd++) { int sd = side_of[nd], c = col_of[nd]; o.write((char*)&sd, 4); o.write((char*)&c, 4); o.write((char*)&nodes[nd].xi, sizeof(Real));
    for (int q = 4; q < K; q++) { for (int f = 0; f < 4; f++) o.write((char*)&a[q][IXN(f, nd, 0)], NX * sizeof(Real)); o.write((char*)&s[q][nd * NX], NX * sizeof(Real)); } }
  fprintf(lg, "written\n"); fclose(lg);
  return 0;
}
