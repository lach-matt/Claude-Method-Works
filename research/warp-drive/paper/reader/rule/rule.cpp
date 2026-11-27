// rule.cpp: the production implementation of the rule of P-APPC2 (proofs/P-APPC2.md, sec:appc-rule): the march with
// segments as the unit of work, exact hand-offs between segments, checkpoint and resume, the element values and
// coefficients (def:appc-element-values), the canonical strings and SHA-256 digests (sec:appc-digest) and the spot
// values (sec:appc-spot).  See README.md.
#include "scheme.h"
#include "sha256.h"
#include <fstream>
#include <sstream>
#include <iostream>
#include <chrono>
#include <set>
#include <sys/stat.h>
#include <cstdio>
#include <ctime>

Consts CS;
static double cpu_s() { timespec t; clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &t); return t.tv_sec + 1e-9 * t.tv_nsec; }
static double now_s() { return std::chrono::duration<double>(std::chrono::steady_clock::now().time_since_epoch()).count(); }

// ---------------------------------------------------------------------------------------------- configuration
struct Rat { long n = 0, d = 1; };
static Rat parse_rat(const std::string& s) {
  Rat r; size_t p = s.find('/');
  if (p == std::string::npos) { r.n = std::stol(s); r.d = 1; } else { r.n = std::stol(s.substr(0, p)); r.d = std::stol(s.substr(p + 1)); }
  if (r.d <= 0) { fprintf(stderr, "bad rational %s\n", s.c_str()); exit(1); }
  return r;
}
struct SegCfg { int c0, c1, M, No, Ni; };
struct ElemCfg { int i, j; Rat xlo, xhi, vlo, vhi; int Nt, Ns; };
struct Cfg {
  int seed = 2; Rat xi_e, v_e; int nc = 0, nr = 0, pxi = 0, pv = 0, NRay = 40, p = 56;
  std::vector<SegCfg> segs; std::vector<ElemCfg> el;
  int run_cols = -1, run_rows = -1, threads = 1, batch = 4; double ckpt_min = 30; std::string out = "out";
  std::string canon, digest;
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
    else if (k == "pxi") is >> CF.pxi; else if (k == "pv") is >> CF.pv;
    else if (k == "NRay") is >> CF.NRay; else if (k == "p") is >> CF.p;
    else if (k == "segment") { SegCfg s; is >> s.c0 >> s.c1 >> s.M >> s.No >> s.Ni; CF.segs.push_back(s); }
    else if (k == "elem") { ElemCfg e; is >> e.i >> e.j >> a >> b >> c >> d >> e.Nt >> e.Ns;
      e.xlo = parse_rat(a); e.xhi = parse_rat(b); e.vlo = parse_rat(c); e.vhi = parse_rat(d); CF.el.push_back(e); }
    else if (k == "run_cols") is >> CF.run_cols; else if (k == "run_rows") is >> CF.run_rows;
    else if (k == "threads") is >> CF.threads; else if (k == "batch") is >> CF.batch;
    else if (k == "ckpt_minutes") is >> CF.ckpt_min; else if (k == "out") is >> CF.out;
    else { fprintf(stderr, "unknown key %s\n", k.c_str()); exit(1); }
  }
  if (CF.run_cols < 0) CF.run_cols = CF.nc;
  if (CF.run_rows < 0) CF.run_rows = CF.nr;
  int c = 0; for (auto& s : CF.segs) { if (s.c0 != c || s.c1 <= s.c0) { fprintf(stderr, "the segments must tile the columns\n"); exit(1); } c = s.c1; }
  if (c != CF.nc) { fprintf(stderr, "the segments must tile the columns\n"); exit(1); }
  std::ostringstream o;
  o << "rule P-APPC2 B 320\nseed " << CF.seed << "\nxi_e " << CF.xi_e.n << "/" << CF.xi_e.d << "\nv_e " << CF.v_e.n << "/" << CF.v_e.d
    << "\nncol " << CF.nc << "\nnrow " << CF.nr << "\npxi " << CF.pxi << "\npv " << CF.pv << "\nNRay " << CF.NRay << "\np " << CF.p << "\n";
  for (auto& s : CF.segs) o << "segment " << s.c0 << " " << s.c1 << " " << s.M << " " << s.No << " " << s.Ni << "\n";
  for (auto& e : CF.el) o << "elem " << e.i << " " << e.j << " " << e.xlo.n << "/" << e.xlo.d << " " << e.xhi.n << "/" << e.xhi.d << " "
                          << e.vlo.n << "/" << e.vlo.d << " " << e.vhi.n << "/" << e.vhi.d << " " << e.Nt << " " << e.Ns << "\n";
  CF.canon = o.str(); CF.digest = sha256_hex(CF.canon);
}
static int seg_of_col(int c) { for (size_t s = 0; s < CF.segs.size(); s++) if (c >= CF.segs[s].c0 && c < CF.segs[s].c1) return s; return -1; }

// ---------------------------------------------------------------------------------------------- geometry
static Vec XB, VB;
static std::map<int, std::unique_ptr<Grid>> GRIDS;
static const Grid* grid_for(int M) {
  auto it = GRIDS.find(M); if (it != GRIDS.end()) return it->second.get();
  double t0 = now_s(); auto g = make_grid(CF.pxi, CF.pv, M); const Grid* r = g.get(); GRIDS[M] = std::move(g);
  fprintf(stderr, "grid (p_xi %d, p_v %d, M %d) built in %.1f s\n", CF.pxi, CF.pv, M, now_s() - t0);
  return r;
}
static const Grid* grid_col(int c) { return grid_for(CF.segs[seg_of_col(c)].M); }
static void setup_geometry() {                              // def:appc-grid
  F xe = fl_rat<F>(CF.xi_e.n, CF.xi_e.d), ve = fl_rat<F>(CF.v_e.n, CF.v_e.d);
  XB.resize(CF.nc + 1); VB.resize(CF.nr + 1);
  for (int i = 0; i <= CF.nc; i++) XB[i] = CS.xi0 + divi(mul_int(xe - CS.xi0, i), CF.nc);
  for (int j = 0; j <= CF.nr; j++) VB[j] = CS.half + divi(mul_int(ve - CS.half, j), CF.nr);
}

// ---------------------------------------------------------------------------------------------- def:appc-rule-data
struct N1Row { LeftEdge e; std::vector<F> Gam, Ups; };
static void n1_row(const Grid* g, int j, const N1Row* prev, N1Row& out) {
  const int nB = g->nB, NX = g->NX; const bool first = (j == 0);
  const Mat& Dv = first ? g->DvR : g->DvL; const Mat& Qv = first ? g->QvR : g->QvL;
  const F o = one<F>(), v0 = VB[j], hv = divi(VB[j + 1] - VB[j], 2), ihv = fdiv(o, hv);
  Vec vs(nB), E(nB), e2(nB), e3(nB), e4(nB), ie2(nB); const Vec& tv = first ? g->TR : g->TV;
  for (int b = 0; b < nB; b++) { vs[b] = v0 + hv * (tv[b] + o); E[b] = vs[b] - CS.half; e2[b] = E[b] * E[b]; e3[b] = e2[b] * E[b]; e4[b] = e3[b] * E[b]; ie2[b] = fdiv(o, e2[b]); }
  std::vector<SeedV> sd(nB);
  #pragma omp parallel for schedule(dynamic)
  for (int b = 0; b < nB; b++) sd[b] = seed_at(CS.xi0, vs[b]);
  F eta4 = fx_zero<6, 5>(); if (!first) { F eta = v0 - CS.half; eta4 = ((eta * eta) * eta) * eta; }
  out.e.nB = nB; out.e.NX = NX; out.e.G.assign((size_t)4 * nB * NX, fx_zero<6, 5>());
  std::vector<F> sig6((size_t)nB * NX), GR((size_t)nB * NX, fx_zero<6, 5>()), rho((size_t)nB * NX), GRn((size_t)nB * NX);
  #pragma omp parallel for schedule(dynamic)
  for (int b = 0; b < nB; b++) {
    const F& r = sd[b].R, &e = E[b];
    F z = divi(CS.pi * e, 3), sz, cz; sincosF(z, sz, cz);
    F q1 = divi(CS.pi, 3) * fdiv(sz, z), q2 = q1 * q1, q3 = q2 * q1, q4 = q2 * q2;
    F st, ct; sincosF(fdiv(vs[b], CS.lam), st, ct);
    F fr = o - fdiv(o, r * r);
    F a1 = -((fdiv(divi(mul_int(fr, 3), 4), r) * e) * q4);
    F a2 = (divi(mul_int(CS.pi, 4), 3) * q3) * cz;
    F a3 = fdiv(e * q4, CS.lam);
    F ir32 = fdiv(o, r * fsqrt(r));
    for (int k = 0; k < NX; k++) {
      const F& x = g->X[k];
      F h = fsqrt(fdiv(fx_int<6, 5>(2), o + x * x));
      F kap = divi(h * CS.lam, 2) * ir32;
      out.e.G[((size_t)FM * nB + b) * NX + k] = (kap * q4) * ct; out.e.G[((size_t)FN * nB + b) * NX + k] = (kap * q4) * st;
      F m3 = kap * ((a1 + a2) * ct - a3 * st), n3 = kap * ((a1 + a2) * st + a3 * ct);
      F P3 = divi(mul_int(o + x, 2) * m3 - (o - x) * n3, 3), Q3 = divi(mul_int(o - x, 2) * n3 - (o + x) * m3, 3);
      sig6[(size_t)b * NX + k] = P3 * P3 + Q3 * Q3 + (P3 + Q3) * (P3 + Q3);
      if (!first) GR[(size_t)b * NX + k] = fdiv(eta4 * prev->Gam[k] + (vs[b] - v0) * prev->Ups[k], e4[b]);
    }
  }
  for (int it = 0; it < CF.NRay; it++) {
    std::vector<S> GRS((size_t)nB * NX); for (size_t q = 0; q < GRS.size(); q++) GRS[q] = to_sm(GR[q]);
    #pragma omp parallel for schedule(static)
    for (int bk = 0; bk < nB * NX; bk++) {
      int b = bk / NX, k = bk % NX;
      F gv = dot<6, 5>(&Dv.s[(size_t)b * nB], 1, &GRS[k], NX, nB) * ihv;
      F Dl = mul_int(e3[b] * GR[bk], 4) + e4[b] * gv;
      F Rt = sd[b].R + e4[b] * GR[bk];
      rho[bk] = mul_int(sd[b].Wv * Dl, 2) - divi(((Rt * sig6[bk]) * e4[b]) * e2[b], 3);
    }
    std::vector<S> RS((size_t)nB * NX);
    for (int bk = 0; bk < nB * NX; bk++) { int b = bk / NX; RS[bk] = to_sm(first ? rho[bk] * ie2[b] : rho[bk]); }
    #pragma omp parallel for schedule(static)
    for (int bk = 0; bk < nB * NX; bk++) {
      int b = bk / NX, k = bk % NX;
      if (first) GRn[bk] = dot<6, 5>(&g->V4.s[(size_t)b * nB], 1, &RS[k], NX, nB);
      else GRn[bk] = fdiv(eta4 * prev->Gam[k] + (vs[b] - v0) * prev->Ups[k] + (hv * hv) * dot<6, 5>(&g->QQ.s[(size_t)b * nB], 1, &RS[k], NX, nB), e4[b]);
    }
    GR.swap(GRn);
  }
  for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) out.e.G[((size_t)FR * nB + b) * NX + k] = GR[(size_t)b * NX + k];
  out.Gam.resize(NX); out.Ups.resize(NX);
  std::vector<S> RS((size_t)nB * NX); for (size_t q = 0; q < RS.size(); q++) RS[q] = to_sm(rho[q]);
  for (int k = 0; k < NX; k++) {                       // ρ of the last sweep
    out.Gam[k] = GR[(size_t)(nB - 1) * NX + k];
    out.Ups[k] = (first ? fx_zero<6, 5>() : prev->Ups[k]) + hv * dot<6, 5>(&Qv.s[(size_t)(nB - 1) * nB], 1, &RS[k], NX, nB);
  }
}

// ---------------------------------------------------------------------------------------------- files
static void put_int(std::string& o, const F& a) {       // compact storage: sign/length byte, magnitude bytes (LE)
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
static void get_raw(const std::string& s, size_t& pos, std::vector<F>& v, size_t n) { v.resize(n); memcpy((void*)v.data(), s.data() + pos, n * sizeof(F)); pos += n * sizeof(F); }
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
static std::string gtext(const Cell& c) {            // the cell's G as text "f a b k X" (comparisons only)
  std::string t; const Grid* g = c.g; const size_t NN = c.NN();
  for (int f = 0; f < NF; f++) for (int a = 0; a < g->nA; a++) for (int b = 0; b < g->nB; b++) for (int k = 0; k < g->NX; k++)
    t += std::to_string(f) + " " + std::to_string(a) + " " + std::to_string(b) + " " + std::to_string(k) + " " + fx_dec(c.G[f * NN + c.IX(a, b, k)]) + "\n";
  return t;
}

// ---------------------------------------------------------------------------------------------- elements (def:appc-element-values)
struct ElemGeo { Vec xn, vn; std::vector<int> col, row; int Me = 0; };
static std::vector<ElemGeo> EG;
static void setup_elements() {
  EG.resize(CF.el.size());
  for (size_t e = 0; e < CF.el.size(); e++) {
    const ElemCfg& c = CF.el[e]; ElemGeo& g = EG[e];
    F mi = fl_rat<F>(c.xlo.n * c.xhi.d + c.xhi.n * c.xlo.d, 2 * c.xlo.d * c.xhi.d), hi = fl_rat<F>(c.xhi.n * c.xlo.d - c.xlo.n * c.xhi.d, 2 * c.xlo.d * c.xhi.d);
    F mj = fl_rat<F>(c.vlo.n * c.vhi.d + c.vhi.n * c.vlo.d, 2 * c.vlo.d * c.vhi.d), hj = fl_rat<F>(c.vhi.n * c.vlo.d - c.vlo.n * c.vhi.d, 2 * c.vlo.d * c.vhi.d);
    g.xn.resize(c.Nt + 1); g.vn.resize(c.Ns + 1); g.col.resize(c.Nt + 1); g.row.resize(c.Ns + 1);
    for (int a = 0; a <= c.Nt; a++) g.xn[a] = mi - hi * chat(a, c.Nt);
    for (int b = 0; b <= c.Ns; b++) g.vn[b] = mj - hj * chat(b, c.Ns);
    for (int a = 0; a <= c.Nt; a++) { int o = CF.nc - 1; for (int i = 0; i < CF.nc; i++) if (g.xn[a] <= XB[i + 1]) { o = i; break; } g.col[a] = o; }
    for (int b = 0; b <= c.Ns; b++) { int o = CF.nr - 1; for (int j = 0; j < CF.nr; j++) if (g.vn[b] <= VB[j + 1]) { o = j; break; } g.row[b] = o; }
    g.Me = 0; for (int a = 0; a <= c.Nt; a++) g.Me = std::max(g.Me, CF.segs[seg_of_col(g.col[a])].M);
  }
}
static std::map<std::pair<int, int>, std::unique_ptr<Resampler>> RESAMP;
static const Resampler* resampler(int M1, int M2) {
  auto key = std::make_pair(M1, M2); auto it = RESAMP.find(key); if (it != RESAMP.end()) return it->second.get();
  auto r = std::make_unique<Resampler>(make_resampler(M1, M2)); const Resampler* p = r.get(); RESAMP[key] = std::move(r); return p;
}
static void resample_edge(LeftEdge& e, int M2) {        // def:appc-resample, for each field and node v_b
  int M1 = e.NX - 1; if (M1 == M2) return;
  const Resampler* R = resampler(M1, M2); std::vector<F> G((size_t)4 * e.nB * (M2 + 1)); std::vector<S> in(e.NX);
  for (int f = 0; f < 4; f++) for (int b = 0; b < e.nB; b++) {
    for (int k = 0; k < e.NX; k++) in[k] = to_sm(e.G[((size_t)f * e.nB + b) * e.NX + k]);
    resample_vals(*R, in.data(), &G[((size_t)f * e.nB + b) * (M2 + 1)]);
  }
  e.G.swap(G); e.NX = M2 + 1;
}
// Γ^F_abk := ⟨ℓ^ξ(τ*), ⟨ℓ^v(ς*), G⟩⟩ for the element nodes the cell owns, resampled to M_e
static void sample_cell(Cell& c, std::string& rec, long& nrec) {
  const Grid* g = c.g; const int nA = g->nA, nB = g->nB, NX = g->NX; const size_t NN = c.NN(); const F o = one<F>();
  std::vector<Z> TLi = to_ints(g->TL), TVi = to_ints(c.first ? g->TR : g->TV), dL = denoms(TLi), dV = denoms(TVi);
  for (size_t q = 0; q < c.G.size(); q++) c.GS[q] = to_sm(c.G[q]);
  for (size_t e = 0; e < EG.size(); e++) {
    const ElemGeo& eg = EG[e]; std::vector<int> as, bs; const int NXe = eg.Me + 1;
    for (size_t a = 0; a < eg.xn.size(); a++) if (eg.col[a] == c.i) as.push_back(a);
    for (size_t b = 0; b < eg.vn.size(); b++) if (eg.row[b] == c.j) bs.push_back(b);
    if (as.empty() || bs.empty()) continue;
    const Resampler* R = (g->M != eg.Me) ? resampler(g->M, eg.Me) : nullptr;
    std::vector<std::vector<S>> lx(as.size());
    for (size_t q = 0; q < as.size(); q++) lagr_values(TLi, dL, fdiv(eg.xn[as[q]] - XB[c.i], c.hxi) - o, lx[q]);   // τ*
    std::vector<F> vals(as.size() * bs.size() * NF * NXe);
    for (size_t qb = 0; qb < bs.size(); qb++) {
      std::vector<S> lv; lagr_values(TVi, dV, fdiv(eg.vn[bs[qb]] - VB[c.j], c.hv) - o, lv);                          // ς*
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
        F* out = &vals[(((size_t)qa * bs.size() + qb) * NF + f) * NXe];
        if (!R) for (int k = 0; k < NX; k++) out[k] = from_sm<6, 5>(v1[k]); else resample_vals(*R, v1.data(), out);
      }
    }
    for (size_t qa = 0; qa < as.size(); qa++) for (size_t qb = 0; qb < bs.size(); qb++) {
      int32_t hd[4] = {(int32_t)e, as[qa], bs[qb], NXe}; rec.append((const char*)hd, 16);
      rec.append((const char*)&vals[(((size_t)qa * bs.size() + qb) * NF) * NXe], (size_t)NF * NXe * sizeof(F)); nrec++;
    }
  }
}

// ---------------------------------------------------------------------------------------------- the march of a segment
struct CellResult { LeftEdge right; TopEdge top; std::string gsha, svsha; std::vector<F> spot; std::string rec; long nrec = 0; int M = 0; };
static std::map<std::pair<int, int>, CellResult> DONE;
static std::string cell_bytes(const CellResult& r, int i, int j) {
  std::string o = "RULECL2\n" + CF.digest + "\n"; int32_t h[3] = {i, j, r.M}; o.append((const char*)h, 12);
  int32_t d[4] = {r.right.nB, r.right.NX, r.top.nA, r.top.NX}; o.append((const char*)d, 16);
  put_raw(o, r.right.G); put_raw(o, r.top.G); put_raw(o, r.top.sv);
  o += r.gsha + r.svsha; int32_t nl = r.spot.size(); o.append((const char*)&nl, 4); put_raw(o, r.spot);
  int64_t nr = r.nrec; o.append((const char*)&nr, 8); int64_t rl = r.rec.size(); o.append((const char*)&rl, 8); o += r.rec;
  return o;
}
static bool load_cell(int s, int i, int j, CellResult& r) {
  std::string fn = cellfile(s, i, j); if (!file_exists(fn)) return false;
  std::string b = read_file(fn); std::string hd = "RULECL2\n" + CF.digest + "\n"; if (b.compare(0, hd.size(), hd)) return false;
  size_t pos = hd.size(); int32_t h[3]; memcpy(h, b.data() + pos, 12); pos += 12; r.M = h[2];
  int32_t d[4]; memcpy(d, b.data() + pos, 16); pos += 16;
  r.right.nB = d[0]; r.right.NX = d[1]; r.top.nA = d[2]; r.top.NX = d[3];
  get_raw(b, pos, r.right.G, (size_t)4 * d[0] * d[1]); get_raw(b, pos, r.top.G, (size_t)NF * d[2] * d[3]); get_raw(b, pos, r.top.sv, (size_t)d[2] * d[3]);
  r.gsha = b.substr(pos, 64); r.svsha = b.substr(pos + 64, 64); pos += 128;
  int32_t nl; memcpy(&nl, b.data() + pos, 4); pos += 4; get_raw(b, pos, r.spot, nl);
  int64_t nr, rl; memcpy(&nr, b.data() + pos, 8); pos += 8; memcpy(&rl, b.data() + pos, 8); pos += 8;
  r.nrec = nr; r.rec = b.substr(pos, rl); return true;
}
static std::vector<N1Row> N1;
static LeftEdge SEG_LEFT;
static void ensure_n1() {
  if (!N1.empty()) return;
  const Grid* g = grid_for(CF.segs[0].M); double t0 = now_s(); N1.resize(CF.run_rows);
  for (int j = 0; j < CF.run_rows; j++) n1_row(g, j, j ? &N1[j - 1] : nullptr, N1[j]);
  fprintf(stderr, "data on N1: %d rows in %.1f s\n", CF.run_rows, now_s() - t0);
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
// def:appc-handoff: the canonical string "edge j b F" + the M + 1 integers, per row, field, node; its digest
static std::string handoff_canonical(const LeftEdge& all, int nr) {
  std::string t; const char* FL = "RmnW";
  for (int j = 0; j < nr; j++) for (int f = 0; f < 4; f++) for (int b = 0; b < all.nB; b++) {
    t += "edge " + std::to_string(j) + " " + std::to_string(b) + " " + FL[f];
    for (int k = 0; k < all.NX; k++) { t += " "; t += fx_dec(all.G[(((size_t)j * 4 + f) * all.nB + b) * all.NX + k]); }
    t += "\n";
  }
  return t;
}
static void write_handoff(int s) {
  const SegCfg& sg = CF.segs[s]; int c = sg.c1 - 1; const Grid* g = grid_col(c);
  LeftEdge all; all.nB = g->nB; all.NX = g->NX;
  for (int j = 0; j < CF.nr; j++) { const LeftEdge& e = DONE.at({c, j}).right; all.G.insert(all.G.end(), e.G.begin(), e.G.end()); }
  std::string canon = handoff_canonical(all, CF.nr), dig = sha256_hex(canon);
  std::string o = "RULEHO2\n"; char hd[512];
  snprintf(hd, sizeof hd, "case %s seg %d col %d nr %d pv %d M %d digest %s\n", CF.digest.c_str(), s, sg.c1, CF.nr, CF.pv, g->M, dig.c_str()); o += hd;
  for (const F& v : all.G) put_int(o, v);
  write_atomic(handofffile(s), o);
  write_atomic(handofffile(s) + ".sha256", sha256_hex(o) + "  " + handofffile(s).substr(CF.out.size() + 1) + "\n");
  fprintf(stderr, "hand-off of segment %d: digest %s (canonical string %zu bytes; stored %zu bytes)\n", s, dig.c_str(), canon.size(), o.size());
}
static std::string read_handoff(int s, LeftEdge& all) {
  std::string b = read_file(handofffile(s));
  if (sha256_hex(b) != read_file(handofffile(s) + ".sha256").substr(0, 64)) { fprintf(stderr, "hand-off %d: file checksum mismatch\n", s); exit(1); }
  size_t nl = b.find('\n', 8); std::istringstream is(b.substr(8, nl - 8)); std::string k, dig, hdig; int seg, col, nr, pv, M;
  is >> k >> dig >> k >> seg >> k >> col >> k >> nr >> k >> pv >> k >> M >> k >> hdig;
  if (dig != CF.digest || seg != s || nr != CF.nr || pv != CF.pv) { fprintf(stderr, "hand-off %d does not belong to this case\n", s); exit(1); }
  size_t pos = nl + 1; all.nB = CF.pv + 1; all.NX = M + 1; all.G.resize((size_t)nr * 4 * all.nB * all.NX);
  for (auto& v : all.G) v = get_int(b, pos);
  if (sha256_hex(handoff_canonical(all, nr)) != hdig) { fprintf(stderr, "hand-off %d: digest mismatch\n", s); exit(1); }
  return hdig;
}
static void save_batch_ckpt(int s, const std::vector<Cell*>& cells, int o) {
  std::string out = "RULEBC2\n" + CF.digest + "\n"; int32_t h[2] = {(int32_t)cells.size(), o}; out.append((const char*)h, 8);
  for (Cell* c : cells) { int32_t ij[2] = {c->i, c->j}; out.append((const char*)ij, 8); put_raw(out, c->G);
    int32_t nr = c->rmax.size(); out.append((const char*)&nr, 4); put_raw(out, c->rmax); }
  write_atomic(segdir(s) + "/batch.ckpt", out);
}
static int load_batch_ckpt(int s, const std::vector<Cell*>& cells) {
  std::string fn = segdir(s) + "/batch.ckpt"; if (!file_exists(fn)) return 0;
  std::string b = read_file(fn); std::string hd = "RULEBC2\n" + CF.digest + "\n"; if (b.compare(0, hd.size(), hd)) return 0;
  size_t pos = hd.size(); int32_t h[2]; memcpy(h, b.data() + pos, 8); pos += 8;
  if (h[0] != (int)cells.size()) return 0;
  size_t p2 = pos;
  for (Cell* c : cells) { int32_t ij[2]; memcpy(ij, b.data() + p2, 8); p2 += 8; if (ij[0] != c->i || ij[1] != c->j) return 0;
    p2 += c->G.size() * sizeof(F); int32_t nr; memcpy(&nr, b.data() + p2, 4); p2 += 4 + nr * sizeof(F); }
  for (Cell* c : cells) { pos += 8; get_raw(b, pos, c->G, c->G.size()); int32_t nr; memcpy(&nr, b.data() + pos, 4); pos += 4; get_raw(b, pos, c->rmax, nr); }
  fprintf(stderr, "  resumed the batch from its checkpoint after outer step %d\n", h[1]);
  return h[1];
}

static void run_segment(int s, bool dump) {
  const SegCfg& sg = CF.segs[s]; const Grid* g = grid_for(sg.M);
  mkdir(CF.out.c_str(), 0755); mkdir(segdir(s).c_str(), 0755);
  if (s == 0) {
    ensure_n1(); SEG_LEFT.nB = g->nB; SEG_LEFT.NX = g->NX; SEG_LEFT.G.clear();
    for (int j = 0; j < CF.run_rows; j++) SEG_LEFT.G.insert(SEG_LEFT.G.end(), N1[j].e.G.begin(), N1[j].e.G.end());
  } else {
    LeftEdge all; read_handoff(s - 1, all);
    if (all.NX != g->NX) {
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
    std::vector<std::pair<int, int>> diag, todo;
    for (int t = 0; t <= d; t++) { int i = c0 + t, j = d - t; if (i < c1 && j >= 0 && j < nr) diag.push_back({i, j}); }
    for (auto& ij : diag) { CellResult r; if (load_cell(s, ij.first, ij.second, r)) DONE[ij] = r; else todo.push_back(ij); }
    for (size_t q0 = 0; q0 < todo.size(); q0 += CF.batch) {
      size_t q1 = std::min(todo.size(), q0 + (size_t)CF.batch);
      std::vector<std::unique_ptr<Cell>> own; Batch bt; double t0 = now_s(), cc0 = cpu_s();
      for (size_t q = q0; q < q1; q++) {
        int i = todo[q].first, j = todo[q].second; own.push_back(std::make_unique<Cell>());
        LeftEdge le = left_of(s, i, j); const TopEdge* low = j ? &DONE.at({i, j - 1}).top : nullptr;
        cell_setup(*own.back(), g, i, j, sg.No, sg.Ni, XB[i], XB[i + 1], VB[j], VB[j + 1], le, low);
        bt.cells.push_back(own.back().get());
      }
      int start = load_batch_ckpt(s, bt.cells);
      double tsetup = now_s() - t0, csetup = cpu_s() - cc0, tlast = now_s();
      scheme_defect(bt, start, [&](int o) { if (now_s() - tlast > 60 * CF.ckpt_min && o < sg.No) { save_batch_ckpt(s, bt.cells, o); tlast = now_s(); } });
      for (Cell* c : bt.cells) {
        const int nA = g->nA, nB = g->nB, NX = g->NX; const size_t NN = c->NN();
        CellResult r; r.M = g->M;
        r.right.nB = nB; r.right.NX = NX; r.right.G.resize((size_t)4 * nB * NX);
        for (int f = 0; f < 4; f++) for (int b = 0; b < nB; b++) for (int k = 0; k < NX; k++) r.right.G[((size_t)f * nB + b) * NX + k] = c->G[f * NN + c->IX(nA - 1, b, k)];
        r.top.nA = nA; r.top.NX = NX; r.top.G.resize((size_t)NF * nA * NX); r.top.sv.resize((size_t)nA * NX);
        for (int f = 0; f < NF; f++) for (int a = 0; a < nA; a++) for (int k = 0; k < NX; k++) r.top.G[((size_t)f * nA + a) * NX + k] = c->G[f * NN + c->IX(a, nB - 1, k)];
        const Mat& Qv = c->first ? g->QvR : g->QvL; std::vector<S> ph(nB);
        for (int a = 0; a < nA; a++) for (int k = 0; k < NX; k++) {      // s^top from Φ of the last evaluation of P
          for (int b = 0; b < nB; b++) ph[b] = to_sm(c->Psi[FS * NN + c->IX(a, b, k)]);
          F base = c->first ? fx_zero<6, 5>() : DONE.at({c->i, c->j - 1}).top.sv[(size_t)a * NX + k];
          r.top.sv[(size_t)a * NX + k] = base + c->hv * dot<6, 5>(&Qv.s[(size_t)(nB - 1) * nB], 1, ph.data(), 1, nB);
        }
        std::string gt = gtext(*c); r.gsha = sha256_hex(gt);
        std::string st; for (auto& v : r.top.sv) st += fx_dec(v) + "\n"; r.svsha = sha256_hex(st);
        r.spot.push_back(c->G[FM * NN + c->IX(nA - 1, nB - 1, 0)]);      // G^m_(p_ξ p_v 0)
        for (auto& v : c->rmax) r.spot.push_back(v);                       // max |r| per outer step
        sample_cell(*c, r.rec, r.nrec);
        write_atomic(cellfile(s, c->i, c->j), cell_bytes(r, c->i, c->j));
        if (dump) write_atomic(segdir(s) + "/G_" + std::to_string(c->i) + "_" + std::to_string(c->j) + ".txt", gt);
        DONE[{c->i, c->j}] = std::move(r); ncell++;
      }
      std::remove((segdir(s) + "/batch.ckpt").c_str());
      double dt = now_s() - t0, dc = cpu_s() - cc0; size_t nodes = (size_t)g->nA * g->nB * g->NX * bt.cells.size();
      fprintf(stderr, "seg %d diag %d cells %zu: setup %.1f s, total %.1f s wall, %.1f s cpu; per node: %.0f us cpu for (N_o, N_i) = (%d, %d) [%d threads]\n",
              s, d, bt.cells.size(), tsetup, dt, dc, 1e6 * (dc - csetup) / (double)nodes, sg.No, sg.Ni, omp_get_max_threads());
    }
  }
  if (c1 == sg.c1 && nr == CF.nr) {
    write_handoff(s);
    std::vector<std::tuple<int, int, int, int, const F*>> all;
    for (auto& kv : DONE) { const std::string& rc = kv.second.rec; size_t pos = 0;
      for (long q = 0; q < kv.second.nrec; q++) { int32_t hd[4]; memcpy(hd, rc.data() + pos, 16); all.push_back({hd[0], hd[1], hd[2], hd[3], (const F*)(rc.data() + pos + 16)}); pos += 16 + (size_t)NF * hd[3] * sizeof(F); } }
    std::sort(all.begin(), all.end(), [](auto& x, auto& y) { return std::make_tuple(std::get<0>(x), std::get<1>(x), std::get<2>(x)) < std::make_tuple(std::get<0>(y), std::get<1>(y), std::get<2>(y)); });
    std::string o = "RULEEL2\n"; char hd[256]; snprintf(hd, sizeof hd, "case %s seg %d records %zu\n", CF.digest.c_str(), s, all.size()); o += hd;
    for (auto& t : all) { int32_t h4[4] = {std::get<0>(t), std::get<1>(t), std::get<2>(t), std::get<3>(t)}; o.append((const char*)h4, 16);
      const F* v = std::get<4>(t); for (int q = 0; q < NF * h4[3]; q++) put_int(o, v[q]); }
    write_atomic(elemfile(s), o);
    write_atomic(elemfile(s) + ".sha256", sha256_hex(o) + "  " + elemfile(s).substr(CF.out.size() + 1) + "\n");
    fprintf(stderr, "segment %d done: %ld cells in %.1f s; element file %zu bytes\n", s, ncell, now_s() - tseg, o.size());
  }
}

// ---------------------------------------------------------------------------------------------- spot values
static void spot_lines(std::ostringstream& o) {
  o << "spot pi " << fx_dec(CS.pi) << "\nspot log2 " << fx_dec(CS.l2) << "\nspot xi0 " << fx_dec(CS.xi0) << "\nspot a " << fx_dec(CS.ah)
    << "\nspot lambda " << fx_dec(CS.lam) << "\nspot Rs(xi0,1/2) " << fx_dec(seed_at(CS.xi0, CS.half).R)
    << "\nspot exp 1 " << fx_dec(expF(one<F>())) << "\nspot log 3 " << fx_dec(logF(fx_int<6, 5>(3)));
  { F s, c; sincosF(one<F>(), s, c); o << "\nspot sin 1 " << fx_dec(s) << "\n"; }
  const Grid* g = grid_for(CF.segs[0].M); ensure_n1();
  F h0 = divi(XB[1] - XB[0], 2), xi_first = XB[0] + h0 * (g->TL[0] + one<F>()), hv0 = divi(VB[1] - VB[0], 2), v_first = VB[0] + hv0 * (g->TR[0] + one<F>());
  o << "spot Rs(first node of cell (0,0)) " << fx_dec(seed_at(xi_first, v_first).R) << "\n";
  const LeftEdge& e = N1[0].e; const int nB = e.nB, NX = e.NX;
  o << "spot G_m(N1, row 0, v_0, x_0) " << fx_dec(e.G[((size_t)FM * nB + 0) * NX]) << "\nspot G_R(N1, row 0, v_0, x_0) " << fx_dec(e.G[((size_t)FR * nB + 0) * NX])
    << "\nspot G_m(N1, row 0, v_pv, x_0) " << fx_dec(e.G[((size_t)FM * nB + nB - 1) * NX]) << "\nspot G_R(N1, row 0, v_pv, x_0) " << fx_dec(e.G[((size_t)FR * nB + nB - 1) * NX]) << "\n";
}
static void cell_spots(std::ostringstream& o) {
  CellResult r;
  if (load_cell(0, 0, 0, r)) {
    for (size_t q = 1; q < r.spot.size(); q++) o << "spot max|r| cell (0,0) outer " << q << " " << fx_dec(r.spot[q]) << "\n";
    o << "spot G_m(p_xi,p_v,0) cell (0,0) " << fx_dec(r.spot[0]) << "\n";
  }
  CellResult r1; if (CF.run_rows > 1 && load_cell(0, 0, 1, r1)) o << "spot G_m(p_xi,p_v,0) cell (0,1) " << fx_dec(r1.spot[0]) << "\n";
}

// ---------------------------------------------------------------------------------------------- assembly (eq:appc-rule-z)
static void assemble() {
  const char* FNM[5] = {"R", "m", "n", "W", "s"};
  std::vector<std::vector<F>> V(CF.el.size()); std::vector<std::vector<char>> got(CF.el.size());
  for (size_t e = 0; e < CF.el.size(); e++) { int NXe = EG[e].Me + 1; V[e].assign((size_t)NF * (CF.el[e].Nt + 1) * (CF.el[e].Ns + 1) * NXe, fx_zero<6, 5>()); got[e].assign((size_t)(CF.el[e].Nt + 1) * (CF.el[e].Ns + 1), 0); }
  std::vector<std::string> hdigs;
  for (size_t s = 0; s < CF.segs.size(); s++) {
    LeftEdge tmp; hdigs.push_back(read_handoff(s, tmp));
    std::string b = read_file(elemfile(s));
    if (sha256_hex(b) != read_file(elemfile(s) + ".sha256").substr(0, 64)) { fprintf(stderr, "element file %zu: checksum mismatch\n", s); exit(1); }
    size_t nl = b.find('\n', 8); std::istringstream is(b.substr(8, nl - 8)); std::string k, dig; int seg; size_t nrec;
    is >> k >> dig >> k >> seg >> k >> nrec; if (dig != CF.digest) { fprintf(stderr, "element file %zu does not belong to this case\n", s); exit(1); }
    size_t pos = nl + 1;
    for (size_t q = 0; q < nrec; q++) {
      int32_t h4[4]; memcpy(h4, b.data() + pos, 16); pos += 16; int e = h4[0], a = h4[1], bb = h4[2], NXe = h4[3]; const ElemCfg& c = CF.el[e];
      for (int f = 0; f < NF; f++) for (int kk = 0; kk < NXe; kk++) V[e][(((size_t)f * (c.Nt + 1) + a) * (c.Ns + 1) + bb) * NXe + kk] = get_int(b, pos);
      got[e][(size_t)a * (c.Ns + 1) + bb] = 1;
    }
  }
  for (size_t e = 0; e < CF.el.size(); e++) for (char q : got[e]) if (!q) { fprintf(stderr, "element %zu: node values missing\n", e); exit(1); }
  Sha256 hcase; std::ofstream txt(CF.out + "/case.txt", std::ios::binary); std::ostringstream dg;
  Z ten, half; mpz_ui_pow_ui(ten.v, 10, CF.p); mpz_set_ui(half.v, 1); mpz_mul_2exp(half.v, half.v, BITS - 1);
  for (size_t e = 0; e < CF.el.size(); e++) {
    const ElemCfg& c = CF.el[e]; const int A = c.Nt + 1, Bn = c.Ns + 1, NXe = EG[e].Me + 1;
    const Mat Ct = chebmat(c.Nt, false), Cs = chebmat(c.Ns, false), Cx = chebmat(EG[e].Me, true);
    for (int f = 0; f < NF; f++) {
      std::vector<S> vs((size_t)A * Bn * NXe), c1s((size_t)A * Bn * NXe), c2s((size_t)A * Bn * NXe); std::vector<F> c3((size_t)A * Bn * NXe);
      for (size_t q = 0; q < vs.size(); q++) vs[q] = to_sm(V[e][(size_t)f * A * Bn * NXe + q]);
      #pragma omp parallel for schedule(static)
      for (int abn = 0; abn < A * Bn * NXe; abn++) { int ab = abn / NXe, n = abn % NXe;          // x first
        c1s[abn] = to_sm(dot<6, 5>(&Cx.s[(size_t)n * NXe], 1, &vs[(size_t)ab * NXe], 1, NXe)); }
      #pragma omp parallel for schedule(static)
      for (int amn = 0; amn < A * Bn * NXe; amn++) { int a = amn / (Bn * NXe), m = (amn / NXe) % Bn, n = amn % NXe;   // then σ
        c2s[amn] = to_sm(dot<6, 5>(&Cs.s[(size_t)m * Bn], 1, &c1s[(size_t)a * Bn * NXe + n], NXe, Bn)); }
      #pragma omp parallel for schedule(static)
      for (int lmn = 0; lmn < A * Bn * NXe; lmn++) { int l = lmn / (Bn * NXe), mn = lmn % (Bn * NXe);   // then t
        c3[lmn] = dot<6, 5>(&Ct.s[(size_t)l * A], 1, &c2s[mn], (long)Bn * NXe, A); }
      std::vector<std::string> zs(c3.size());
      #pragma omp parallel for schedule(static)
      for (long q = 0; q < (long)c3.size(); q++) { Z t; fx_to_mpz(c3[q], t.v); mpz_mul(t.v, t.v, ten.v); mpz_add(t.v, t.v, half.v); mpz_fdiv_q_2exp(t.v, t.v, BITS);
        if (mpz_sgn(t.v)) { char* sp = mpz_get_str(nullptr, 10, t.v); zs[q] = sp; free(sp); } }
      std::string blk = "block " + std::to_string(c.i) + " " + std::to_string(c.j) + " " + FNM[f] + " " + std::to_string(CF.p) + " " +
                        std::to_string(c.Nt) + " " + std::to_string(c.Ns) + " " + std::to_string(EG[e].Me) + "\n";
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
      dg << "block " << c.i << " " << c.j << " " << FNM[f] << " sha256 " << sha256_hex(blk) << " nonzero " << nnz << " S1 " << zstr(S1) << " S2 " << zstr(S2)
         << " S0 " << zstr(S0) << " z000 " << zat(0, 0, 0) << " z100 " << zat(1, 0, 0) << " z010 " << zat(0, 1, 0) << " z001 " << zat(0, 0, 1) << "\n";
    }
  }
  std::ostringstream full; full << "case sha256 " << hcase.hex() << "\n";
  for (size_t s = 0; s < hdigs.size(); s++) full << "handoff " << s << " sha256 " << hdigs[s] << "\n";
  full << dg.str(); spot_lines(full); cell_spots(full);
  { const ElemCfg& c = CF.el[0]; int NXe = EG[0].Me + 1; full << "spot Gamma^m_000 first element " << fx_dec(V[0][(size_t)FM * (c.Nt + 1) * (c.Ns + 1) * NXe]) << "\n"; }
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
    if (want[i + " " + j + " " + f] != sha256_hex(blk)) { bad++; fprintf(stderr, "block %s %s %s: digest mismatch\n", i.c_str(), j.c_str(), f.c_str()); }
    nb++; pos = end;
  }
  std::string hc = sha256_hex(t); if (hc != casesha) { bad++; fprintf(stderr, "case digest mismatch\n"); }
  printf("%zu blocks, case sha256 %s: %s\n", nb, hc.c_str(), bad ? "MISMATCH" : "all digests agree");
  return bad ? 1 : 0;
}

// ---------------------------------------------------------------------------------------------- main
int main(int argc, char** argv) {
  if (argc < 3) {
    fprintf(stderr, "usage: rule run CFG [SEG] [out=DIR threads=N batch=N ckpt_minutes=X]   every segment in order, or segment SEG\n"
                    "       rule assemble CFG [out=DIR]     coefficients, DIR/case.txt (canonical string) and DIR/digests.txt\n"
                    "       rule cells CFG [out=DIR]        the run_cols x run_rows cells (segments in order) and a dump (tests)\n"
                    "       rule verify TEXT DIGESTS\n"
                    "       rule params CFG                 the canonical parameters and their digest\n"
                    "       rule n1handoff CFG [out=DIR]    the data on N1 as a hand-off state (a size measurement)\n");
    return 1;
  }
  std::string cmd = argv[1];
  if (cmd == "verify") return verify(argv[2], argv[3]);
  std::vector<std::string> pos; std::vector<std::pair<std::string, std::string>> opts;
  for (int a = 3; a < argc; a++) { std::string t = argv[a]; size_t e = t.find('='); if (e == std::string::npos) pos.push_back(t); else opts.push_back({t.substr(0, e), t.substr(e + 1)}); }
  read_cfg(argv[2]);
  for (auto& o : opts) { if (o.first == "out") CF.out = o.second; else if (o.first == "threads") CF.threads = atoi(o.second.c_str());
    else if (o.first == "batch") CF.batch = atoi(o.second.c_str()); else if (o.first == "ckpt_minutes") CF.ckpt_min = atof(o.second.c_str());
    else { fprintf(stderr, "unknown option %s\n", o.first.c_str()); return 1; } }
  omp_set_num_threads(CF.threads);
  init_consts(CF.seed);
  CS.K.resize(RHS_NK); for (int i = 0; i < RHS_NK; i++) CS.K[i] = fl_rat<F>(RHS_KNUM[i], RHS_KDEN[i]);
  setup_geometry(); setup_elements();
  if (cmd == "params") { printf("%s---\nparameter digest %s\n", CF.canon.c_str(), CF.digest.c_str()); return 0; }
  if (cmd == "run") { if (!pos.empty()) run_segment(atoi(pos[0].c_str()), false); else for (size_t s = 0; s < CF.segs.size(); s++) run_segment(s, false); return 0; }
  if (cmd == "cells") {
    std::ostringstream o; std::vector<std::string> hd; std::map<std::pair<int, int>, CellResult> all;
    for (size_t s = 0; s < CF.segs.size() && CF.segs[s].c0 < CF.run_cols; s++) {
      run_segment(s, true); for (auto& kv : DONE) all[kv.first] = kv.second;
      if (CF.segs[s].c1 <= CF.run_cols && CF.run_rows == CF.nr) { LeftEdge t; hd.push_back(read_handoff(s, t)); }
    }
    spot_lines(o); cell_spots(o);
    for (size_t s = 0; s < hd.size(); s++) o << "handoff " << s << " sha256 " << hd[s] << "\n";
    for (auto& kv : all) o << "cell " << kv.first.first << " " << kv.first.second << " sha256 " << kv.second.gsha << " sv " << kv.second.svsha << "\n";
    write_atomic(CF.out + "/cells.dump", o.str());
    return 0;
  }
  if (cmd == "assemble") { assemble(); return 0; }
  if (cmd == "n1handoff") {
    ensure_n1(); mkdir(CF.out.c_str(), 0755);
    LeftEdge all; all.nB = N1[0].e.nB; all.NX = N1[0].e.NX; for (auto& r : N1) all.G.insert(all.G.end(), r.e.G.begin(), r.e.G.end());
    std::string canon = handoff_canonical(all, CF.run_rows), comp, raw;
    for (const F& v : all.G) { put_int(comp, v); raw.append((const char*)&v, 48); }
    write_atomic(CF.out + "/handoff_n1.txt", canon); write_atomic(CF.out + "/handoff_n1.bin", comp);
    printf("data on N1 as a hand-off state: %zu integers; canonical string %zu bytes (digest %s); compact binary %zu bytes; fixed 48-byte %zu bytes\n",
           all.G.size(), canon.size(), sha256_hex(canon).c_str(), comp.size(), raw.size());
    return 0;
  }
  fprintf(stderr, "unknown command %s\n", cmd.c_str()); return 1;
}
