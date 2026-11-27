// rule.cpp: the production implementation of the rule of S-RULE §3 (the approximant defined by an exactly specified
// computation), with segments as the unit of work (Zeno segmentation), exact hand-offs between segments, checkpoint
// and resume, the element sampling and coefficients (§3.8), and the canonical output with SHA-256 digests (§3.9).
// See README.md.  Every interpretive choice is marked [Qn] and listed in README.md.
#include "scheme.h"
#include "sha256.h"
#include <fstream>
#include <sstream>
#include <iostream>
#include <chrono>
#include <set>
#include <sys/stat.h>
#include <cstdio>
#include <cmath>   // diagnostics only (printed norms); no value of the rule passes through floating point

Consts CS;
static double now_s() { return std::chrono::duration<double>(std::chrono::steady_clock::now().time_since_epoch()).count(); }

// ---------------------------------------------------------------------------------------------- configuration
struct Rat { long n = 0, d = 1; std::string s; };
static Rat parse_rat(const std::string& s) {
  Rat r; r.s = s; size_t p = s.find('/');
  if (p == std::string::npos) { r.n = std::stol(s); r.d = 1; } else { r.n = std::stol(s.substr(0, p)); r.d = std::stol(s.substr(p + 1)); }
  if (r.d <= 0) { fprintf(stderr, "bad rational %s\n", s.c_str()); exit(1); }
  return r;
}
struct SegCfg { int c0, c1, pxi, M; };
struct ElemCfg { int i, j; Rat xlo, xhi, vlo, vhi; int Nt, Ns; };
struct Cfg {
  int seed = 2; Rat xi_e, v_e; int nc = 0, nr = 0, pxi = 0, pv = 0, M = 0, NP = 64, NRay = 40, p = 56, Me = -1;
  std::vector<SegCfg> segs; std::vector<Rat> xibreaks; std::vector<ElemCfg> el;
  int run_cols = -1, run_rows = -1, threads = 1, batch = 4; double ckpt_min = 30; std::string out = "out";
  std::string canon;                 // canonical text of the parameters that define the output (for the digest)
  std::string digest;
};
static Cfg CF;
static void read_cfg(const std::string& fn) {
  std::ifstream f(fn); if (!f) { fprintf(stderr, "cannot open %s\n", fn.c_str()); exit(1); }
  std::string line;
  while (std::getline(f, line)) {
    size_t h = line.find('#'); if (h != std::string::npos) line = line.substr(0, h);
    std::istringstream is(line); std::string k; if (!(is >> k)) continue;
    std::string a, b, c, d;
    if (k == "seed") is >> CF.seed;
    else if (k == "xi_e") { is >> a; CF.xi_e = parse_rat(a); }
    else if (k == "v_e") { is >> a; CF.v_e = parse_rat(a); }
    else if (k == "ncol") is >> CF.nc; else if (k == "nrow") is >> CF.nr;
    else if (k == "pxi") is >> CF.pxi; else if (k == "pv") is >> CF.pv; else if (k == "M") is >> CF.M;
    else if (k == "NP") is >> CF.NP; else if (k == "NRay") is >> CF.NRay; else if (k == "p") is >> CF.p;
    else if (k == "Me") is >> CF.Me;
    else if (k == "segment") { SegCfg s; is >> s.c0 >> s.c1 >> s.pxi >> s.M; CF.segs.push_back(s); }
    else if (k == "xibreaks") { while (is >> a) CF.xibreaks.push_back(parse_rat(a)); }
    else if (k == "elem") { ElemCfg e; is >> e.i >> e.j >> a >> b >> c >> d >> e.Nt >> e.Ns;
      e.xlo = parse_rat(a); e.xhi = parse_rat(b); e.vlo = parse_rat(c); e.vhi = parse_rat(d); CF.el.push_back(e); }
    else if (k == "run_cols") is >> CF.run_cols; else if (k == "run_rows") is >> CF.run_rows;
    else if (k == "threads") is >> CF.threads; else if (k == "batch") is >> CF.batch;
    else if (k == "ckpt_minutes") is >> CF.ckpt_min; else if (k == "out") is >> CF.out;
    else { fprintf(stderr, "unknown key %s\n", k.c_str()); exit(1); }
  }
  if (CF.segs.empty()) CF.segs.push_back({0, CF.nc, CF.pxi, CF.M});
  if (CF.run_cols < 0) CF.run_cols = CF.nc;
  if (CF.run_rows < 0) CF.run_rows = CF.nr;
  if (CF.Me < 0) { CF.Me = 0; for (auto& s : CF.segs) CF.Me = std::max(CF.Me, s.M); }
  int c = 0; for (auto& s : CF.segs) { if (s.c0 != c || s.c1 <= s.c0) { fprintf(stderr, "segments must tile the columns\n"); exit(1); } c = s.c1; }
  if (c != CF.nc) { fprintf(stderr, "segments must tile the columns\n"); exit(1); }
  std::ostringstream o;
  o << "rule S-RULE-3 B 320\nseed " << CF.seed << "\nxi_e " << CF.xi_e.n << "/" << CF.xi_e.d << "\nv_e " << CF.v_e.n << "/" << CF.v_e.d
    << "\nncol " << CF.nc << "\nnrow " << CF.nr << "\npv " << CF.pv << "\nNP " << CF.NP << "\nNRay " << CF.NRay << "\n";
  for (auto& s : CF.segs) o << "segment " << s.c0 << " " << s.c1 << " " << s.pxi << " " << s.M << "\n";
  if (!CF.xibreaks.empty()) { o << "xibreaks"; for (auto& r : CF.xibreaks) o << " " << r.n << "/" << r.d; o << "\n"; }
  o << "Me " << CF.Me << "\np " << CF.p << "\n";
  for (auto& e : CF.el) o << "elem " << e.i << " " << e.j << " " << e.xlo.n << "/" << e.xlo.d << " " << e.xhi.n << "/" << e.xhi.d << " "
                          << e.vlo.n << "/" << e.vlo.d << " " << e.vhi.n << "/" << e.vhi.d << " " << e.Nt << " " << e.Ns << "\n";
  CF.canon = o.str(); CF.digest = sha256_hex(CF.canon);
}
static int seg_of_col(int c) { for (size_t s = 0; s < CF.segs.size(); s++) if (c >= CF.segs[s].c0 && c < CF.segs[s].c1) return s; return -1; }

// ---------------------------------------------------------------------------------------------- global geometry
static Vec XB, VB;                                   // breakpoints (§3.6)
static std::map<std::tuple<int, int, int>, std::unique_ptr<Grid>> GRIDS;
static const Grid* grid_for(int pxi, int M) {
  auto key = std::make_tuple(pxi, CF.pv, M);
  auto it = GRIDS.find(key); if (it != GRIDS.end()) return it->second.get();
  double t0 = now_s(); auto g = make_grid(pxi, CF.pv, M); const Grid* r = g.get(); GRIDS[key] = std::move(g);
  fprintf(stderr, "grid (p_xi %d, p_v %d, M %d) built in %.1f s\n", pxi, CF.pv, M, now_s() - t0);
  return r;
}
static const Grid* grid_col(int c) { const SegCfg& s = CF.segs[seg_of_col(c)]; return grid_for(s.pxi, s.M); }
static void setup_geometry() {
  F xe = fl_rat<F>(CF.xi_e.n, CF.xi_e.d), ve = fl_rat<F>(CF.v_e.n, CF.v_e.d);
  XB.resize(CF.nc + 1); VB.resize(CF.nr + 1);
  if (CF.xibreaks.empty()) { for (int i = 0; i <= CF.nc; i++) XB[i] = CS.xi0 + divi(mul_int(xe - CS.xi0, i), CF.nc); }
  else {                                             // explicit interior breakpoints (an extension for graded grids)
    if ((int)CF.xibreaks.size() != CF.nc - 1) { fprintf(stderr, "xibreaks needs ncol - 1 values\n"); exit(1); }
    XB[0] = CS.xi0; XB[CF.nc] = xe; for (int i = 1; i < CF.nc; i++) XB[i] = fl_rat<F>(CF.xibreaks[i - 1].n, CF.xibreaks[i - 1].d);
  }
  for (int j = 0; j <= CF.nr; j++) VB[j] = CS.half + divi(mul_int(ve - CS.half, j), CF.nr);
}

// ---------------------------------------------------------------------------------------------- §3.5 data on N1
struct N1Row { LeftEdge e; std::vector<F> topGR, topRv; };
static void mn_data(const F& v, const F& x, const F& r, F& gm, F& gn, F& mv3, F& nv3) {
  const F o = one<F>(), eps = v - CS.half;
  F z = divi(CS.pi * eps, 3), sz, cz; sincosF(z, sz, cz);
  F sc = divi(CS.pi, 3) * fdiv(sz, z);
  F h = fsqrt(fdiv(fx_int<6, 5>(2), o + x * x));
  F st, ct; sincosF(fdiv(v, CS.lam), st, ct);
  F r32 = fdiv(o, r * fsqrt(r));
  F pre = ((h * CS.lam) * CS.half) * r32;                               // h ⊙ λ̂ ⊙ ½ ⊙ (1 ⊘ (r ⊙ √r))
  F sc2 = sc * sc, sc3 = sc2 * sc, sc4 = sc2 * sc2;                    // as mn_data [Q1]
  F f = o - fdiv(o, r * r);
  gm = (pre * sc4) * ct; gn = (pre * sc4) * st;
  F a1 = ((fdiv(fl_rat<F>(-3, 4) * f, r)) * eps) * sc4;
  F a2 = (divi(mul_int(CS.pi, 4), 3) * sc3) * cz;
  F a3 = fdiv(eps * sc4, CS.lam);
  mv3 = pre * ((a1 + a2) * ct - a3 * st);
  nv3 = pre * ((a1 + a2) * st + a3 * ct);
}
static void n1_row(const Grid* g, int j, const N1Row* below, N1Row& out) {
  const int nB = g->nB, NX = g->NX; const bool first = (j == 0);
  const Mat& Dv = first ? g->DvR : g->DvL; const Mat& Qv = first ? g->QvR : g->QvL;
  const F o = one<F>(), v0 = VB[j], hv = divi(VB[j + 1] - VB[j], 2);
  Vec vs(nB), E(nB), E4(nB); const Vec& tv = first ? g->TR : g->TV;
  for (int b = 0; b < nB; b++) { vs[b] = v0 + hv * (tv[b] + o); E[b] = vs[b] - CS.half; E4[b] = ((E[b] * E[b]) * E[b]) * E[b]; }
  std::vector<SeedV> sd(nB);
  #pragma omp parallel for schedule(dynamic)
  for (int b = 0; b < nB; b++) sd[b] = seed_at(CS.xi0, vs[b]);
  const F eb = v0 - CS.half, eb4 = ((eb * eb) * eb) * eb;
  out.e.nB = nB; out.e.NX = NX; out.e.G.assign((size_t)4 * nB * NX, fx_zero<6, 5>());
  std::vector<F> sh6((size_t)nB * NX), GR((size_t)nB * NX, fx_zero<6, 5>()), rhs((size_t)nB * NX), GRn((size_t)nB * NX);
  #pragma omp parallel for schedule(dynamic)
  for (int bk = 0; bk < nB * NX; bk++) {
    int b = bk / NX, k = bk % NX; const F& x = g->X[k];
    F gm, gn, mv3, nv3; mn_data(vs[b], x, sd[b].R, gm, gn, mv3, nv3);
    out.e.G[((size_t)FM * nB + b) * NX + k] = gm; out.e.G[((size_t)FN * nB + b) * NX + k] = gn;
    F Pv = divi(mul_int(o + x, 2) * mv3 - (o - x) * nv3, 3), Qv_ = divi(mul_int(o - x, 2) * nv3 - (o + x) * mv3, 3);
    sh6[bk] = Pv * Pv + Qv_ * Qv_ + (Pv + Qv_) * (Pv + Qv_);
    if (!first) GR[bk] = fdiv(eb4 * below->topGR[k] + (vs[b] - v0) * below->topRv[k], E4[b]);
  }
  for (int it = 0; it < CF.NRay; it++) {
    std::vector<S> GRS((size_t)nB * NX); for (size_t q = 0; q < GRS.size(); q++) GRS[q] = to_sm(GR[q]);
    #pragma omp parallel for schedule(static)
    for (int bk = 0; bk < nB * NX; bk++) {
      int b = bk / NX, k = bk % NX;
      F gv = fdiv(dot<6, 5>(&Dv.s[(size_t)b * nB], 1, &GRS[k], NX, nB), hv);           // as n1_row: ⊘ h_v
      F DRv = (((mul_int(E[b], 4) * E[b]) * E[b]) * GR[bk]) + E4[b] * gv;
      F Rt = sd[b].R + E4[b] * GR[bk];
      rhs[bk] = mul_int(sd[b].Wv, 2) * DRv - divi(((((Rt * sh6[bk]) * E4[b]) * E[b]) * E[b]), 3);
    }
    std::vector<S> RS((size_t)nB * NX);
    for (int bk = 0; bk < nB * NX; bk++) { int b = bk / NX; RS[bk] = to_sm(first ? fdiv(rhs[bk], E[b] * E[b]) : rhs[bk]); }
    #pragma omp parallel for schedule(static)
    for (int bk = 0; bk < nB * NX; bk++) {
      int b = bk / NX, k = bk % NX;
      if (first) GRn[bk] = dot<6, 5>(&g->V4.s[(size_t)b * nB], 1, &RS[k], NX, nB);
      else {
        F s1 = dot<6, 5>(&g->QQ.s[(size_t)b * nB], 1, &RS[k], NX, nB);
        GRn[bk] = fdiv(eb4 * below->topGR[k] + (vs[b] - v0) * below->topRv[k] + (hv * hv) * s1, E4[b]);
      }
    }
    GR.swap(GRn);
  }
  for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) out.e.G[((size_t)FR * nB + b) * NX + k] = GR[(size_t)b * NX + k];
  out.topGR.resize(NX); out.topRv.resize(NX);
  std::vector<S> RS((size_t)nB * NX); for (size_t q = 0; q < RS.size(); q++) RS[q] = to_sm(rhs[q]);
  for (int k = 0; k < NX; k++) {                       // R_v at the top from the last sweep's right-hand side [Q16]
    out.topGR[k] = GR[(size_t)(nB - 1) * NX + k];
    out.topRv[k] = (first ? fx_zero<6, 5>() : below->topRv[k]) + hv * dot<6, 5>(&Qv.s[(size_t)(nB - 1) * nB], 1, &RS[k], NX, nB);
  }
}

// ---------------------------------------------------------------------------------------------- canonical integers
// compact canonical binary for an integer X: one byte (bit 7 the sign, bits 0-6 the number n of magnitude bytes),
// then the n magnitude bytes, least significant first; n is minimal (zero: one byte 0)
static void put_int(std::string& o, const F& a) {
  uint64_t m[6]; bool n = fx_abs(a, m); unsigned char by[48]; for (int i = 0; i < 48; i++) by[i] = (unsigned char)(m[i / 8] >> (8 * (i % 8)));
  int len = 48; while (len > 0 && by[len - 1] == 0) len--;
  o.push_back((char)((n && len ? 0x80 : 0) | len)); o.append((const char*)by, len);
}
static F get_int(const std::string& s, size_t& pos) {
  unsigned char h = (unsigned char)s.at(pos++); int len = h & 0x7f; bool n = h & 0x80; uint64_t m[6] = {0};
  for (int i = 0; i < len; i++) m[i / 8] |= (uint64_t)(unsigned char)s.at(pos++) << (8 * (i % 8));
  return fx_from_mag<6, 5>(m, n, false);
}
static void put_raw(std::string& o, const std::vector<F>& v) { o.append((const char*)v.data(), v.size() * sizeof(F)); }
static void get_raw(const std::string& s, size_t& pos, std::vector<F>& v, size_t n) {
  v.resize(n); memcpy((void*)v.data(), s.data() + pos, n * sizeof(F)); pos += n * sizeof(F);
}
static std::string read_file(const std::string& fn) { std::ifstream f(fn, std::ios::binary); std::ostringstream o; o << f.rdbuf(); return o.str(); }
static bool file_exists(const std::string& fn) { struct stat st; return stat(fn.c_str(), &st) == 0; }
static void write_atomic(const std::string& fn, const std::string& data) {
  std::string tmp = fn + ".tmp"; { std::ofstream f(tmp, std::ios::binary); f.write(data.data(), data.size()); if (!f) { fprintf(stderr, "write failed %s\n", tmp.c_str()); exit(1); } }
  std::rename(tmp.c_str(), fn.c_str());
}
static std::string segdir(int s) { char b[64]; snprintf(b, 64, "/seg_%02d", s); return CF.out + b; }
static std::string cellfile(int s, int i, int j) { char b[64]; snprintf(b, 64, "/cell_%04d_%04d.bin", i, j); return segdir(s) + b; }
static std::string handofffile(int s) { char b[64]; snprintf(b, 64, "/handoff_%02d.bin", s); return CF.out + b; }
static std::string elemfile(int s) { char b[64]; snprintf(b, 64, "/elem_%02d.bin", s); return CF.out + b; }
static std::string gtext(const Cell& c) {            // the cell's final G as text "f a b k X" (for comparisons)
  std::string t; const Grid* g = c.g; const size_t NN = c.NN();
  for (int f = 0; f < NF; f++) for (int a = 0; a < g->nA; a++) for (int b = 0; b < g->nB; b++) for (int k = 0; k < g->NX; k++) {
    t += std::to_string(f) + " " + std::to_string(a) + " " + std::to_string(b) + " " + std::to_string(k) + " " + fx_dec(c.G[f * NN + c.IX(a, b, k)]) + "\n"; }
  return t;
}

// ---------------------------------------------------------------------------------------------- elements (§3.8)
struct ElemGeo { Vec xn, vn; std::vector<int> col, row; };
static std::vector<ElemGeo> EG;
static void setup_elements() {
  EG.resize(CF.el.size());
  for (size_t e = 0; e < CF.el.size(); e++) {
    const ElemCfg& c = CF.el[e]; ElemGeo& g = EG[e];
    F XL = fl_rat<F>(c.xlo.n, c.xlo.d), XH = fl_rat<F>(c.xhi.n, c.xhi.d), VL = fl_rat<F>(c.vlo.n, c.vlo.d), VH = fl_rat<F>(c.vhi.n, c.vhi.d);
    g.xn.resize(c.Nt + 1); g.vn.resize(c.Ns + 1); g.col.resize(c.Nt + 1); g.row.resize(c.Ns + 1);
    for (int a = 0; a <= c.Nt; a++) g.xn[a] = divi(XL + XH, 2) - divi(XH - XL, 2) * chat(a, c.Nt);
    for (int b = 0; b <= c.Ns; b++) g.vn[b] = divi(VL + VH, 2) - divi(VH - VL, 2) * chat(b, c.Ns);
    for (int a = 0; a <= c.Nt; a++) { int o = CF.nc - 1; for (int i = 0; i < CF.nc; i++) if (XB[i + 1] >= g.xn[a]) { o = i; break; } g.col[a] = o; }  // [Q17]
    for (int b = 0; b <= c.Ns; b++) { int o = CF.nr - 1; for (int j = 0; j < CF.nr; j++) if (VB[j + 1] >= g.vn[b]) { o = j; break; } g.row[b] = o; }
  }
}
static std::map<std::pair<int, int>, std::unique_ptr<Mat>> RESAMP;
static const Mat* resampler(int M1, int M2) {
  auto key = std::make_pair(M1, M2); auto it = RESAMP.find(key); if (it != RESAMP.end()) return it->second.get();
  auto m = std::make_unique<Mat>(resample_mat(xnodes(M1), xnodes(M2))); const Mat* r = m.get(); RESAMP[key] = std::move(m); return r;
}
// resample an edge [rows][f][b][k] in x from M1 to M2 nodes (per-segment M) [Q27]
static void resample_edge(LeftEdge& e, int M2) {
  int M1 = e.NX - 1; if (M1 == M2) return;
  const Mat* R = resampler(M1, M2); std::vector<F> G((size_t)4 * e.nB * (M2 + 1));
  std::vector<S> in((size_t)e.NX);
  for (int f = 0; f < 4; f++) for (int b = 0; b < e.nB; b++) {
    for (int k = 0; k < e.NX; k++) in[k] = to_sm(e.G[((size_t)f * e.nB + b) * e.NX + k]);
    for (int k2 = 0; k2 <= M2; k2++) G[((size_t)f * e.nB + b) * (M2 + 1) + k2] = dot<6, 5>(&R->s[(size_t)k2 * e.NX], 1, in.data(), 1, e.NX);
  }
  e.G.swap(G); e.NX = M2 + 1;
}
// the element-node values a finished cell owns: ⟨ℓ(ξ_a), ⟨ℓ(v_b), G⟩⟩ (then ⟨R, ·⟩ in x if the cell's M ≠ Me)
static void sample_cell(Cell& c, std::string& rec, long& nrec) {
  const Grid* g = c.g; const int nA = g->nA, nB = g->nB, NX = g->NX, NXe = CF.Me + 1; const size_t NN = c.NN();
  std::vector<Z> Xi = to_ints(c.xis), Vi = to_ints(c.vs), dX = denoms(Xi), dV = denoms(Vi);
  for (size_t q = 0; q < c.G.size(); q++) c.GS[q] = to_sm(c.G[q]);
  const Mat* R = (g->M != CF.Me) ? resampler(g->M, CF.Me) : nullptr;
  for (size_t e = 0; e < EG.size(); e++) {
    const ElemGeo& eg = EG[e]; std::vector<int> as, bs;
    for (size_t a = 0; a < eg.xn.size(); a++) if (eg.col[a] == c.i) as.push_back(a);
    for (size_t b = 0; b < eg.vn.size(); b++) if (eg.row[b] == c.j) bs.push_back(b);
    if (as.empty() || bs.empty()) continue;
    std::vector<std::vector<S>> lx(as.size());
    for (size_t q = 0; q < as.size(); q++) lagr_values(Xi, dX, eg.xn[as[q]], lx[q]);
    std::vector<F> vals(as.size() * bs.size() * NF * NXe);
    for (size_t qb = 0; qb < bs.size(); qb++) {
      std::vector<S> lv; lagr_values(Vi, dV, eg.vn[bs[qb]], lv);
      std::vector<S> inner((size_t)NF * nA * NX);
      #pragma omp parallel for schedule(static)
      for (int fak = 0; fak < NF * nA * NX; fak++) {
        int f = fak / (nA * NX), a = (fak / NX) % nA, k = fak % NX;
        inner[fak] = to_sm(dot<6, 5>(lv.data(), 1, &c.GS[f * NN + c.IX(a, 0, k)], NX, nB));
      }
      #pragma omp parallel for schedule(static)
      for (int qa = 0; qa < (int)as.size(); qa++) for (int f = 0; f < NF; f++) {
        std::vector<S> v1(NX);
        for (int k = 0; k < NX; k++) v1[k] = to_sm(dot<6, 5>(lx[qa].data(), 1, &inner[(size_t)f * nA * NX + k], NX, nA));
        F* o = &vals[(((size_t)qa * bs.size() + qb) * NF + f) * NXe];
        if (!R) for (int k = 0; k < NX; k++) o[k] = from_sm<6, 5>(v1[k]);
        else for (int k2 = 0; k2 < NXe; k2++) o[k2] = dot<6, 5>(&R->s[(size_t)k2 * NX], 1, v1.data(), 1, NX);
      }
    }
    for (size_t qa = 0; qa < as.size(); qa++) for (size_t qb = 0; qb < bs.size(); qb++) {
      int32_t hd[3] = {(int32_t)e, as[qa], bs[qb]}; rec.append((const char*)hd, 12);
      rec.append((const char*)&vals[(((size_t)qa * bs.size() + qb) * NF) * NXe], (size_t)NF * NXe * sizeof(F)); nrec++;
    }
  }
}

// ---------------------------------------------------------------------------------------------- the march of a segment
struct CellResult { LeftEdge right; TopEdge top; std::string gsha, svsha; std::vector<F> last; std::string rec; long nrec = 0; };
static std::map<std::pair<int, int>, CellResult> DONE;          // finished cells of the current segment (edges)

static std::string cell_bytes(const CellResult& r, int i, int j) {
  std::string o = "RULECL1\n" + CF.digest + "\n"; int32_t h[2] = {i, j}; o.append((const char*)h, 8);
  int32_t d[4] = {r.right.nB, r.right.NX, r.top.nA, r.top.NX}; o.append((const char*)d, 16);
  put_raw(o, r.right.G); put_raw(o, r.top.G); put_raw(o, r.top.sv);
  o += r.gsha + r.svsha; int32_t nl = r.last.size(); o.append((const char*)&nl, 4); put_raw(o, r.last);
  int64_t nr = r.nrec; o.append((const char*)&nr, 8); int64_t rl = r.rec.size(); o.append((const char*)&rl, 8); o += r.rec;
  return o;
}
static bool load_cell(int s, int i, int j, CellResult& r) {
  std::string fn = cellfile(s, i, j); if (!file_exists(fn)) return false;
  std::string b = read_file(fn); std::string hd = "RULECL1\n" + CF.digest + "\n";
  if (b.compare(0, hd.size(), hd)) return false;
  size_t pos = hd.size() + 8; int32_t d[4]; memcpy(d, b.data() + pos, 16); pos += 16;
  r.right.nB = d[0]; r.right.NX = d[1]; r.top.nA = d[2]; r.top.NX = d[3];
  get_raw(b, pos, r.right.G, (size_t)4 * d[0] * d[1]); get_raw(b, pos, r.top.G, (size_t)NF * d[2] * d[3]); get_raw(b, pos, r.top.sv, (size_t)d[2] * d[3]);
  r.gsha = b.substr(pos, 64); r.svsha = b.substr(pos + 64, 64); pos += 128;
  int32_t nl; memcpy(&nl, b.data() + pos, 4); pos += 4; get_raw(b, pos, r.last, nl);
  int64_t nr, rl; memcpy(&nr, b.data() + pos, 8); pos += 8; memcpy(&rl, b.data() + pos, 8); pos += 8;
  r.nrec = nr; r.rec = b.substr(pos, rl); return true;
}

static std::vector<N1Row> N1;
static LeftEdge SEG_LEFT;                                       // left edge of the segment's first column, all rows

static void ensure_n1(const Grid* g) {
  if (!N1.empty()) return;
  double t0 = now_s(); N1.resize(CF.run_rows);
  for (int j = 0; j < CF.run_rows; j++) n1_row(g, j, j ? &N1[j - 1] : nullptr, N1[j]);
  fprintf(stderr, "N1 data: %d rows in %.1f s\n", CF.run_rows, now_s() - t0);
}
static LeftEdge left_of(int s, int i, int j) {
  if (i == CF.segs[s].c0) {
    LeftEdge e; int nB = SEG_LEFT.nB, NX = SEG_LEFT.NX; e.nB = nB; e.NX = NX; e.G.resize((size_t)4 * nB * NX);
    for (int f = 0; f < 4; f++) for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++)
      e.G[((size_t)f * nB + b) * NX + k] = SEG_LEFT.G[(((size_t)j * 4 + f) * nB + b) * NX + k];
    return e;
  }
  return DONE.at({i - 1, j}).right;
}

static void write_handoff(int s) {
  const SegCfg& sg = CF.segs[s]; int c = sg.c1 - 1; const Grid* g = grid_col(c);
  std::string o = "RULEHO1\n";
  char hd[512]; snprintf(hd, sizeof hd, "case %s seg %d col %d nr %d pv %d M %d fields R m n W\n", CF.digest.c_str(), s, sg.c1, CF.run_rows, CF.pv, g->M);
  o += hd;
  for (int j = 0; j < CF.run_rows; j++) { const LeftEdge& e = DONE.at({c, j}).right; for (const F& v : e.G) put_int(o, v); }
  write_atomic(handofffile(s), o);
  std::string sha = sha256_hex(o);
  write_atomic(handofffile(s) + ".sha256", sha + "  " + handofffile(s).substr(CF.out.size() + 1) + "\n");
  fprintf(stderr, "hand-off %s: %zu bytes, sha256 %s\n", handofffile(s).c_str(), o.size(), sha.c_str());
}
static void read_handoff(int s, LeftEdge& all) {        // the hand-off of segment s, as the next segment's left edge
  std::string b = read_file(handofffile(s)); std::string sha = sha256_hex(b);
  std::string want = read_file(handofffile(s) + ".sha256").substr(0, 64);
  if (sha != want) { fprintf(stderr, "hand-off %d: sha256 mismatch\n", s); exit(1); }
  size_t nl = b.find('\n', 8); std::istringstream is(b.substr(8, nl - 8)); std::string k, dig; int seg, col, nr, pv, M;
  is >> k >> dig >> k >> seg >> k >> col >> k >> nr >> k >> pv >> k >> M;
  if (dig != CF.digest || seg != s || nr != CF.run_rows || pv != CF.pv) { fprintf(stderr, "hand-off %d does not belong to this case\n", s); exit(1); }
  size_t pos = nl + 1; int nB = CF.pv + 1, NX = M + 1; all.nB = nB; all.NX = NX; all.G.resize((size_t)nr * 4 * nB * NX);
  for (auto& v : all.G) v = get_int(b, pos);
  if (pos != b.size()) { fprintf(stderr, "hand-off %d: trailing bytes\n", s); exit(1); }
}

static void save_batch_ckpt(int s, const std::vector<Cell*>& cells, int n) {
  std::string o = "RULEBC1\n" + CF.digest + "\n"; int32_t h[2] = {(int32_t)cells.size(), n}; o.append((const char*)h, 8);
  for (Cell* c : cells) { int32_t ij[2] = {c->i, c->j}; o.append((const char*)ij, 8); put_raw(o, c->G); }
  write_atomic(segdir(s) + "/batch.ckpt", o);
}
static int load_batch_ckpt(int s, const std::vector<Cell*>& cells) {
  std::string fn = segdir(s) + "/batch.ckpt"; if (!file_exists(fn)) return 0;
  std::string b = read_file(fn); std::string hd = "RULEBC1\n" + CF.digest + "\n"; if (b.compare(0, hd.size(), hd)) return 0;
  size_t pos = hd.size(); int32_t h[2]; memcpy(h, b.data() + pos, 8); pos += 8;
  if (h[0] != (int)cells.size()) return 0;
  size_t p2 = pos;
  for (Cell* c : cells) { int32_t ij[2]; memcpy(ij, b.data() + p2, 8); p2 += 8; if (ij[0] != c->i || ij[1] != c->j) return 0; p2 += c->G.size() * sizeof(F); }
  for (Cell* c : cells) { pos += 8; get_raw(b, pos, c->G, c->G.size()); }
  fprintf(stderr, "  resumed batch from its checkpoint at sweep %d\n", h[1]);
  return h[1];
}

static void run_segment(int s, bool dump) {
  const SegCfg& sg = CF.segs[s]; const Grid* g = grid_for(sg.pxi, sg.M);
  mkdir(CF.out.c_str(), 0755); mkdir(segdir(s).c_str(), 0755);
  // the segment's left edge: N1 data, or the previous segment's hand-off resampled to this segment's M
  if (s == 0) {
    ensure_n1(g); SEG_LEFT.nB = g->nB; SEG_LEFT.NX = g->NX; SEG_LEFT.G.clear();
    for (int j = 0; j < CF.run_rows; j++) SEG_LEFT.G.insert(SEG_LEFT.G.end(), N1[j].e.G.begin(), N1[j].e.G.end());
  } else {
    LeftEdge all; read_handoff(s - 1, all);
    if (all.NX != g->NX) {                    // per-segment M: resample each row's edge
      LeftEdge out; out.nB = all.nB; out.NX = g->NX;
      for (int j = 0; j < CF.run_rows; j++) {
        LeftEdge e; e.nB = all.nB; e.NX = all.NX;
        e.G.assign(all.G.begin() + (size_t)j * 4 * all.nB * all.NX, all.G.begin() + (size_t)(j + 1) * 4 * all.nB * all.NX);
        resample_edge(e, g->M); out.G.insert(out.G.end(), e.G.begin(), e.G.end());
      }
      SEG_LEFT = out;
    } else SEG_LEFT = all;
  }
  DONE.clear();
  const int c0 = sg.c0, c1 = std::min(sg.c1, CF.run_cols), nr = CF.run_rows;
  if (c1 <= c0) return;
  double tseg = now_s(); long ncell = 0;
  for (int d = 0; d <= (c1 - 1 - c0) + (nr - 1); d++) {
    std::vector<std::pair<int, int>> diag;
    for (int t = 0; t <= d; t++) { int i = c0 + t, j = d - t; if (i < c1 && j >= 0 && j < nr) diag.push_back({i, j}); }
    std::vector<std::pair<int, int>> todo;
    for (auto& ij : diag) { CellResult r; if (load_cell(s, ij.first, ij.second, r)) DONE[ij] = r; else todo.push_back(ij); }
    for (size_t q0 = 0; q0 < todo.size(); q0 += CF.batch) {
      size_t q1 = std::min(todo.size(), q0 + (size_t)CF.batch);
      std::vector<std::unique_ptr<Cell>> own; Batch bt;
      double t0 = now_s();
      for (size_t q = q0; q < q1; q++) {
        int i = todo[q].first, j = todo[q].second;
        own.push_back(std::make_unique<Cell>());
        LeftEdge le = left_of(s, i, j);
        const TopEdge* bot = j ? &DONE.at({i, j - 1}).top : nullptr;
        cell_setup(*own.back(), g, i, j, XB[i], XB[i + 1], VB[j], VB[j + 1], le, bot);
        bt.cells.push_back(own.back().get());
      }
      int start = load_batch_ckpt(s, bt.cells);
      double tlast = now_s();
      double tsetup = now_s() - t0;
      scheme_picard(bt, CF.NP, start, [&](int n) {
        if (now_s() - tlast > 60 * CF.ckpt_min && n < CF.NP) { save_batch_ckpt(s, bt.cells, n); tlast = now_s(); }
      });
      // finish each cell: s_v on the top edge, edges, element samples, its file
      for (Cell* c : bt.cells) {
        const int nA = g->nA, nB = g->nB, NX = g->NX; const size_t NN = c->NN();
        CellResult r;
        r.right.nB = nB; r.right.NX = NX; r.right.G.resize((size_t)4 * nB * NX);
        for (int f = 0; f < 4; f++) for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) r.right.G[((size_t)f * nB + b) * NX + k] = c->G[f * NN + c->IX(nA - 1, b, k)];
        r.top.nA = nA; r.top.NX = NX; r.top.G.resize((size_t)NF * nA * NX); r.top.sv.resize((size_t)nA * NX);
        for (int f = 0; f < NF; f++) for (int a = 0; a < nA; a++) for (int k = 0; k < NX; k++) r.top.G[((size_t)f * nA + a) * NX + k] = c->G[f * NN + c->IX(a, nB - 1, k)];
        const Mat& Qv = c->first ? g->QvR : g->QvL;
        for (int a = 0; a < nA; a++) {
          std::vector<S> ph(nB);
          for (int k = 0; k < NX; k++) {
            for (int b = 0; b < nB; b++) ph[b] = to_sm(c->Psi[FS * NN + c->IX(a, b, k)]);
            F base = c->first ? fx_zero<6, 5>() : DONE.at({c->i, c->j - 1}).top.sv[(size_t)a * NX + k];
            r.top.sv[(size_t)a * NX + k] = base + c->hv * dot<6, 5>(&Qv.s[(size_t)(nB - 1) * nB], 1, ph.data(), 1, nB);
          }
        }
        std::string gt = gtext(*c); r.gsha = sha256_hex(gt);
        std::string st; for (auto& v : r.top.sv) st += fx_dec(v) + "\n"; r.svsha = sha256_hex(st);
        for (int f = 0; f < NF; f++) r.last.push_back(c->G[f * NN + c->IX(nA - 1, nB - 1, NX - 1)]);
        sample_cell(*c, r.rec, r.nrec);
        write_atomic(cellfile(s, c->i, c->j), cell_bytes(r, c->i, c->j));
        if (dump) write_atomic(segdir(s) + "/G_" + std::to_string(c->i) + "_" + std::to_string(c->j) + ".txt", gt);
        DONE[{c->i, c->j}] = std::move(r); ncell++;
      }
      std::remove((segdir(s) + "/batch.ckpt").c_str());
      double dt = now_s() - t0; size_t nodes = (size_t)g->nA * g->nB * g->NX * bt.cells.size();
      int msw = 0; for (Cell* c : bt.cells) msw = std::max(msw, c->sweeps);
      fprintf(stderr, "seg %d diag %d cells %zu: setup %.1f s, total %.1f s, sweeps %d, %.1f us/node/sweep (wall, %d threads)\n",
              s, d, bt.cells.size(), tsetup, dt, msw, 1e6 * (dt - tsetup) / (double)nodes / (msw + 1), omp_get_max_threads());
    }
  }
  if (c1 == sg.c1 && nr == CF.nr) {
    write_handoff(s);
    // the segment's element samples, in canonical order (e, a, b), compact integers
    std::vector<std::tuple<int, int, int, const F*>> all;
    for (auto& kv : DONE) { const std::string& rc = kv.second.rec; size_t per = 12 + (size_t)NF * (CF.Me + 1) * sizeof(F);
      for (long q = 0; q < kv.second.nrec; q++) { const char* p = rc.data() + q * per; int32_t hd[3]; memcpy(hd, p, 12); all.push_back({hd[0], hd[1], hd[2], (const F*)(p + 12)}); } }
    std::sort(all.begin(), all.end(), [](auto& x, auto& y) { return std::make_tuple(std::get<0>(x), std::get<1>(x), std::get<2>(x)) < std::make_tuple(std::get<0>(y), std::get<1>(y), std::get<2>(y)); });
    std::string o = "RULEEL1\n"; char hd[256]; snprintf(hd, sizeof hd, "case %s seg %d Me %d records %zu\n", CF.digest.c_str(), s, CF.Me, all.size()); o += hd;
    for (auto& t : all) { int32_t h3[3] = {std::get<0>(t), std::get<1>(t), std::get<2>(t)}; o.append((const char*)h3, 12);
      const F* v = std::get<3>(t); for (int q = 0; q < NF * (CF.Me + 1); q++) put_int(o, v[q]); }
    write_atomic(elemfile(s), o);
    write_atomic(elemfile(s) + ".sha256", sha256_hex(o) + "  " + elemfile(s).substr(CF.out.size() + 1) + "\n");
    fprintf(stderr, "segment %d done: %ld cells in %.1f s; element file %zu bytes\n", s, ncell, now_s() - tseg, o.size());
  }
}

// ---------------------------------------------------------------------------------------------- assembly (§3.8-3.9)
static void assemble() {
  const int NXe = CF.Me + 1; const char* FNM[5] = {"R", "m", "n", "W", "s"};
  std::vector<std::vector<F>> V(CF.el.size()); std::vector<std::vector<char>> got(CF.el.size());
  for (size_t e = 0; e < CF.el.size(); e++) { V[e].assign((size_t)NF * (CF.el[e].Nt + 1) * (CF.el[e].Ns + 1) * NXe, fx_zero<6, 5>()); got[e].assign((size_t)(CF.el[e].Nt + 1) * (CF.el[e].Ns + 1), 0); }
  for (size_t s = 0; s < CF.segs.size(); s++) {
    std::string b = read_file(elemfile(s)); std::string want = read_file(elemfile(s) + ".sha256").substr(0, 64);
    if (sha256_hex(b) != want) { fprintf(stderr, "element file %zu: sha256 mismatch\n", s); exit(1); }
    size_t nl = b.find('\n', 8); std::istringstream is(b.substr(8, nl - 8)); std::string k, dig; int seg, me; size_t nrec;
    is >> k >> dig >> k >> seg >> k >> me >> k >> nrec;
    if (dig != CF.digest || me != CF.Me) { fprintf(stderr, "element file %zu does not belong to this case\n", s); exit(1); }
    size_t pos = nl + 1;
    for (size_t q = 0; q < nrec; q++) {
      int32_t h3[3]; memcpy(h3, b.data() + pos, 12); pos += 12; int e = h3[0], a = h3[1], bb = h3[2]; const ElemCfg& c = CF.el[e];
      for (int f = 0; f < NF; f++) for (int kk = 0; kk < NXe; kk++) V[e][(((size_t)f * (c.Nt + 1) + a) * (c.Ns + 1) + bb) * NXe + kk] = get_int(b, pos);
      got[e][(size_t)a * (c.Ns + 1) + bb] = 1;
    }
  }
  for (size_t e = 0; e < CF.el.size(); e++) for (char q : got[e]) if (!q) { fprintf(stderr, "element %zu: node values missing\n", e); exit(1); }
  const Mat Cx = dctmat(CF.Me);
  Sha256 hcase; std::ofstream txt(CF.out + "/case.txt", std::ios::binary); std::ostringstream dg;
  Z ten, X, half; mpz_ui_pow_ui(ten.v, 10, CF.p); mpz_set_ui(half.v, 1); mpz_mul_2exp(half.v, half.v, BITS - 1);
  for (size_t e = 0; e < CF.el.size(); e++) {
    const ElemCfg& c = CF.el[e]; const int A = c.Nt + 1, Bn = c.Ns + 1; const Mat Ct = dctmat(c.Nt), Cs = dctmat(c.Ns);
    std::vector<S> Ctr((size_t)A * A), Csr((size_t)Bn * Bn);           // node a ascending pairs with column N - a [Q18]
    for (int n = 0; n < A; n++) for (int a = 0; a < A; a++) Ctr[(size_t)n * A + a] = Ct.s[(size_t)n * A + (c.Nt - a)];
    for (int m = 0; m < Bn; m++) for (int b = 0; b < Bn; b++) Csr[(size_t)m * Bn + b] = Cs.s[(size_t)m * Bn + (c.Ns - b)];
    for (int f = 0; f < NF; f++) {
      std::vector<S> vs((size_t)A * Bn * NXe), c1s((size_t)A * Bn * NXe), c2s((size_t)A * Bn * NXe); std::vector<F> c3((size_t)A * Bn * NXe);
      for (size_t q = 0; q < vs.size(); q++) vs[q] = to_sm(V[e][(size_t)f * A * Bn * NXe + q]);
      #pragma omp parallel for schedule(static)
      for (int nbk = 0; nbk < A * Bn * NXe; nbk++) { int n = nbk / (Bn * NXe), bk = nbk % (Bn * NXe);
        c1s[nbk] = to_sm(dot<6, 5>(&Ctr[(size_t)n * A], 1, &vs[bk], (long)Bn * NXe, A)); }
      #pragma omp parallel for schedule(static)
      for (int nmk = 0; nmk < A * Bn * NXe; nmk++) { int n = nmk / (Bn * NXe), m = (nmk / NXe) % Bn, k = nmk % NXe;
        c2s[nmk] = to_sm(dot<6, 5>(&Csr[(size_t)m * Bn], 1, &c1s[(size_t)n * Bn * NXe + k], NXe, Bn)); }
      #pragma omp parallel for schedule(static)
      for (int nml = 0; nml < A * Bn * NXe; nml++) { int nm = nml / NXe, l = nml % NXe;
        c3[nml] = dot<6, 5>(&Cx.s[(size_t)l * NXe], 1, &c2s[(size_t)nm * NXe], 1, NXe); }
      // z = ⌊10^p C + ½⌋ and the block's text
      std::vector<std::string> zs(c3.size());
      #pragma omp parallel for schedule(static)
      for (long q = 0; q < (long)c3.size(); q++) { Z t; fx_to_mpz(c3[q], t.v); mpz_mul(t.v, t.v, ten.v); mpz_add(t.v, t.v, half.v); mpz_fdiv_q_2exp(t.v, t.v, BITS);
        if (mpz_sgn(t.v)) { char* sp = mpz_get_str(nullptr, 10, t.v); zs[q] = sp; free(sp); } }
      std::string blk = "block " + std::to_string(c.i) + " " + std::to_string(c.j) + " " + FNM[f] + " " + std::to_string(CF.p) + " " +
                        std::to_string(c.Nt) + " " + std::to_string(c.Ns) + " " + std::to_string(CF.Me) + "\n";
      Z S1(0), S2(0), S0(0), zz; long nnz = 0;
      for (int a = 0; a < A; a++) for (int b = 0; b < Bn; b++) {
        int K = -1; for (int k = 0; k < NXe; k++) if (!zs[((size_t)a * Bn + b) * NXe + k].empty()) K = k;
        if (K < 0) continue;
        blk += std::to_string(a) + " " + std::to_string(b);
        for (int k = 0; k <= K; k++) { const std::string& v = zs[((size_t)a * Bn + b) * NXe + k]; blk += " "; blk += v.empty() ? "0" : v;
          if (!v.empty()) { nnz++; mpz_set_str(zz.v, v.c_str(), 10); mpz_add(S1.v, S1.v, zz.v);
            if ((a + b + k) % 2) mpz_sub(S2.v, S2.v, zz.v); else mpz_add(S2.v, S2.v, zz.v);
            if (a % 2 == 0 && b % 2 == 0 && k % 2 == 0) { if (((a + b + k) / 2) % 2) mpz_sub(S0.v, S0.v, zz.v); else mpz_add(S0.v, S0.v, zz.v); } } }
        blk += "\n";
      }
      txt.write(blk.data(), blk.size()); hcase.update(blk);
      auto zat = [&](int a, int b, int k) { if (a >= A || b >= Bn || k >= NXe) return std::string("0"); const std::string& v = zs[((size_t)a * Bn + b) * NXe + k]; return v.empty() ? std::string("0") : v; };
      auto zstr = [](const Z& q) { char* sp = mpz_get_str(nullptr, 10, q.v); std::string r(sp); free(sp); return r; };
      dg << "block " << c.i << " " << c.j << " " << FNM[f] << " sha256 " << sha256_hex(blk) << " S1 " << zstr(S1) << " S2 " << zstr(S2) << " S0 " << zstr(S0)
         << " nonzero " << nnz << " z000 " << zat(0, 0, 0) << " z100 " << zat(1, 0, 0) << " z010 " << zat(0, 1, 0) << " z001 " << zat(0, 0, 1) << "\n";
    }
  }
  std::ostringstream full; full << "case sha256 " << hcase.hex() << "\n" << dg.str();
  // spot values
  full << "spot pi " << fx_dec(CS.pi) << "\nspot log2 " << fx_dec(CS.l2) << "\nspot xi0 " << fx_dec(CS.xi0) << "\nspot lambda " << fx_dec(CS.lam)
       << "\nspot Rs(xi0,1/2) " << fx_dec(seed_at(CS.xi0, CS.half).R) << "\n";
  { const Grid* g = grid_col(0); ensure_n1(g); full << "spot Gm(N1, row 0, first node) " << fx_dec(N1[0].e.G[((size_t)FM * g->nB + 0) * g->NX + 0]) << "\n"; }
  { CellResult r; if (load_cell(0, 0, 0, r)) for (int f = 0; f < NF; f++) full << "spot G00 last node field " << f << " " << fx_dec(r.last[f]) << "\n"; }
  for (int f = 0; f < NF; f++) full << "spot first element node value field " << f << " " << fx_dec(V[0][(size_t)f * (CF.el[0].Nt + 1) * (CF.el[0].Ns + 1) * NXe]) << "\n";
  write_atomic(CF.out + "/digests.txt", full.str());
  fprintf(stderr, "case sha256 %s\n", hcase.hex().c_str());
}

// ---------------------------------------------------------------------------------------------- verify
static int verify(const std::string& txtfn, const std::string& dgfn) {
  std::string t = read_file(txtfn), d = read_file(dgfn);
  std::istringstream ds(d); std::string line; std::map<std::string, std::string> want; std::string casesha;
  while (std::getline(ds, line)) { std::istringstream is(line); std::string a, b, c, f, k, h; is >> a;
    if (a == "case") { is >> k >> casesha; } else if (a == "block") { is >> b >> c >> f >> k >> h; want[b + " " + c + " " + f] = h; } }
  int bad = 0; size_t pos = 0, nb = 0;
  while (pos < t.size()) {
    size_t e = t.find("\nblock ", pos); size_t end = e == std::string::npos ? t.size() : e + 1;
    std::string blk = t.substr(pos, end - pos); std::istringstream hs(blk); std::string w, i, j, f; hs >> w >> i >> j >> f;
    std::string h = sha256_hex(blk); if (want[i + " " + j + " " + f] != h) { bad++; fprintf(stderr, "block %s %s %s: digest mismatch\n", i.c_str(), j.c_str(), f.c_str()); }
    nb++; pos = end;
  }
  std::string hc = sha256_hex(t); if (hc != casesha) { bad++; fprintf(stderr, "case digest mismatch\n"); }
  printf("%zu blocks, case sha256 %s: %s\n", nb, hc.c_str(), bad ? "MISMATCH" : "all digests agree");
  return bad ? 1 : 0;
}


// ---------------------------------------------------------------------------------------------- the pilot's cell
// rule pilotcell FILE NP [compat] [ownK]: the sweep engine on the pilot's inputs (tests/pilotin.cpp); with compat the
// pilot's two formula readings and its D2 (the solver's second-derivative matrix) instead of §3.3's dot-product square
static double tod(const F& a) { Z z; fx_to_mpz(a, z.v); double s = 0; size_t nb = mpz_sizeinbase(z.v, 2); (void)nb;
  char* str = mpz_get_str(nullptr, 10, z.v); s = atof(str); free(str); return s / 2.1359870359209100823950217061696e96; }
static int pilotcell(const std::string& fn, int NP, bool compat) {
  compat_pilot() = compat;
  std::string b = read_file(fn); if (b.compare(0, 8, "RULEPI1\n")) { fprintf(stderr, "bad pilot input file\n"); return 1; }
  size_t pos = 8; int32_t d[3]; memcpy(d, b.data() + pos, 12); pos += 12;
  std::map<std::string, std::vector<F>> A;
  while (pos < b.size()) { size_t nl = b.find('\n', pos); std::string nm = b.substr(pos, nl - pos); pos = nl + 1; uint64_t n; memcpy(&n, b.data() + pos, 8); pos += 8;
    std::vector<F> v; get_raw(b, pos, v, n); A[nm] = v; }
  Grid gp; gp.nA = d[0]; gp.nB = d[1]; gp.NX = d[2]; gp.pxi = d[0] - 1; gp.pv = d[1] - 1; gp.M = d[2] - 1;
  auto mat = [&](const char* nm, int n) { Mat m; m.r = m.c = n; m.a = A.at(nm); m.finish(); return m; };
  gp.DvR = mat("Dv", gp.nB); gp.Dxi = mat("Dxi", gp.nA); gp.D1x = mat("D1x", gp.NX); gp.W4 = mat("W4", gp.nB); gp.V4 = mat("V4", gp.nB);
  gp.Qxi = mat("Qxi", gp.nA); gp.QvR = mat("Qv", gp.nB); gp.D2x = compat ? mat("D2x", gp.NX) : dotsq(gp.D1x); gp.X = A.at("x");
  CS.K = A.at("K");
  Cell c; c.g = &gp; c.first = true; const F o = one<F>(); const int nA = gp.nA, nB = gp.nB, NX = gp.NX; const size_t NN = c.NN();
  c.hxi = A.at("h")[0]; c.hv = A.at("h")[1]; c.ihxi = fdiv(o, c.hxi); c.ihv = fdiv(o, c.hv);
  c.eps = A.at("eps"); c.e2.resize(nB); c.e3.resize(nB); c.e4.resize(nB); c.e3x4.resize(nB); c.ie2.resize(nB); c.ie3.resize(nB);
  for (int q = 0; q < nB; q++) { c.e2[q] = c.eps[q] * c.eps[q]; c.e3[q] = c.e2[q] * c.eps[q]; c.e4[q] = c.e3[q] * c.eps[q];
    c.e3x4[q] = mul_int(c.e3[q], 4); c.ie2[q] = fdiv(o, c.e2[q]); c.ie3[q] = fdiv(o, c.e3[q]); }
  c.sd.resize((size_t)nA * nB);
  for (int ab = 0; ab < nA * nB; ab++) { SeedV& s = c.sd[ab]; s.R = A.at("sR")[ab]; s.Ru = A.at("sRu")[ab]; s.Rv = A.at("sRv")[ab]; s.Wv = A.at("sWv")[ab];
    s.OM2 = A.at("sOM2")[ab]; s.du = A.at("sdu")[ab]; s.iOM2 = fdiv(o, s.OM2); s.idu = fdiv(o, s.du); }
  c.Bt.assign(NF * NN, fx_zero<6, 5>());
  for (int f = 0; f < 4; f++) for (int a = 0; a < nA; a++) for (int q = 0; q < nB; q++) for (int k = 0; k < NX; k++)
    c.Bt[f * NN + c.IX(a, q, k)] = A.at("left")[((size_t)f * nB + q) * NX + k];
  cell_seed_rhs(c);
  c.G = c.Bt; c.Gn.resize(NF * NN); c.Psi.resize(NF * NN); c.GS.resize(NF * NN); c.TS.resize(NF * NN);
  Batch bt; bt.cells.push_back(&c);
  double tcpu = 0;
  for (int n = 0; n < NP; n++) {
    double t0 = now_s(); bt.evaluate(); bt.integrate(); tcpu += now_s() - t0;
    double dm = 0, gm = 1e-300; for (size_t i = 0; i < c.G.size(); i++) { dm = std::max(dm, std::fabs(tod(c.Gn[i] - c.G[i]))); }
    for (size_t i = 0; i < c.G.size(); i += 1) gm = std::max(gm, std::fabs(tod(c.Gn[i])));
    c.G.swap(c.Gn);
    printf("sweep %3d: |G_new - G|/|G| = %.3e\n", n + 1, dm / gm); fflush(stdout);
  }
  unsigned long long h = 1469598103934665603ULL;
  for (auto& q : c.G) for (int i = 0; i < 6; i++) { h ^= q.w[i]; h *= 1099511628211ULL; }
  printf("FNV-1a of the fixed-point state: %016llx  (%s, %d sweeps, %.2f s per sweep)\n", h, compat ? "pilot readings and D2" : "the rule's readings", NP, tcpu / NP);
  if (A.count("Gref")) {
    const auto& R = A.at("Gref");
    for (int f = 0; f < NF; f++) { double em = 0, gm = 0; for (size_t i = 0; i < NN; i++) { em = std::max(em, std::fabs(tod(c.G[f * NN + i] - R[f * NN + i]))); gm = std::max(gm, std::fabs(tod(R[f * NN + i]))); }
      printf("field %d: max|G - G_qd| = %.3e, max|G_qd| = %.3e, relative %.3e\n", f, em, gm, em / gm); }
  }
  std::string gt = gtext(c); write_atomic(fn + (compat ? ".G_compat.txt" : ".G_rule.txt"), gt);
  printf("sha256 of G (text) %s\n", sha256_hex(gt).c_str());
  return 0;
}

// ---------------------------------------------------------------------------------------------- main
static void init_all() {
  omp_set_num_threads(CF.threads);
  init_consts(CF.seed);
  CS.K.resize(RHS_NK); for (int i = 0; i < RHS_NK; i++) CS.K[i] = fl_rat<F>(RHS_KNUM[i], RHS_KDEN[i]);   // ⌊q⌋_B
  setup_geometry(); setup_elements();
}
int main(int argc, char** argv) {
  if (argc < 3) {
    fprintf(stderr, "usage: rule run CFG [SEG]     run every segment in order, or only segment SEG (from the previous hand-off)\n"
                    "       rule assemble CFG      coefficients, canonical text (OUT/case.txt) and digests (OUT/digests.txt)\n"
                    "       rule cells CFG         run the run_cols x run_rows cells of segment 0 and dump their G (tests)\n"
                    "       rule verify TEXT DIGESTS\n"
                    "       rule params CFG        print the canonical parameters and their digest\n");
    return 1;
  }
  std::string cmd = argv[1];
  if (cmd == "verify") return verify(argv[2], argv[3]);
  if (cmd == "pilotcell") {             // rule pilotcell FILE NP [compat] [threads=N]
    bool compat = false; int thr = 1; for (int a = 4; a < argc; a++) { std::string t = argv[a]; if (t == "compat") compat = true; else if (!t.compare(0, 8, "threads=")) thr = atoi(t.c_str() + 8); }
    omp_set_num_threads(thr); init_consts(2); return pilotcell(argv[2], atoi(argv[3]), compat);
  }
  // options after CFG: out=DIR threads=N batch=N ckpt_minutes=X; a bare number is the segment for 'run'
  std::vector<std::string> pos; std::vector<std::pair<std::string, std::string>> opts;
  for (int a = 3; a < argc; a++) { std::string t = argv[a]; size_t e = t.find('='); if (e == std::string::npos) pos.push_back(t); else opts.push_back({t.substr(0, e), t.substr(e + 1)}); }
  read_cfg(argv[2]);
  for (auto& o : opts) { if (o.first == "out") CF.out = o.second; else if (o.first == "threads") CF.threads = atoi(o.second.c_str());
    else if (o.first == "batch") CF.batch = atoi(o.second.c_str()); else if (o.first == "ckpt_minutes") CF.ckpt_min = atof(o.second.c_str());
    else { fprintf(stderr, "unknown option %s\n", o.first.c_str()); return 1; } }
  init_all();
  if (cmd == "params") { printf("%s---\nparameter digest %s\n", CF.canon.c_str(), CF.digest.c_str()); return 0; }
  if (cmd == "run") {
    if (!pos.empty()) { int s = atoi(pos[0].c_str()); run_segment(s, false); }
    else for (size_t s = 0; s < CF.segs.size(); s++) run_segment(s, false);
    return 0;
  }
  if (cmd == "cells") {
    run_segment(0, true);
    // a dump in the reference's format
    std::ostringstream o;
    o << "spot pi " << fx_dec(CS.pi) << "\nspot log2 " << fx_dec(CS.l2) << "\nspot xi0 " << fx_dec(CS.xi0) << "\nspot lambda " << fx_dec(CS.lam)
      << "\nspot Rs(xi0,1/2) " << fx_dec(seed_at(CS.xi0, CS.half).R) << "\n";
    const Grid* g = grid_col(0);
    o << "spot Gm(N1, row 0, first node) " << fx_dec(N1[0].e.G[((size_t)FM * g->nB) * g->NX]) << "\n";
    for (int f = 0; f < NF; f++) o << "spot G00 last node field " << f << " " << fx_dec(DONE.at({0, 0}).last[f]) << "\n";
    for (auto& kv : DONE) o << "cell " << kv.first.first << " " << kv.first.second << " sha256 " << kv.second.gsha << "\nsv " << kv.first.first << " " << kv.first.second << " " << kv.second.svsha << "\n";
    write_atomic(CF.out + "/cells.dump", o.str());
    return 0;
  }
  if (cmd == "assemble") { assemble(); return 0; }
  fprintf(stderr, "unknown command %s\n", cmd.c_str()); return 1;
}
