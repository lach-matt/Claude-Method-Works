// evalres.cpp: the residual of an approximant in the printed form of Appendix C (eq:appc-seedform, kappa = 4),
// evaluated in double-double at sample points (floating-point diagnostics, not a certificate).
// usage: evalres approx.txt points.txt out.txt
// approx.txt (text):  a_inv 500 | kappa 4 | pou_xi n c_1..c_{n-1} d | pou_v n c'_1.. d' | then per element
//   "elem i j xi_lo xi_hi v_lo v_hi" and per field "field f p nt ns nx count" followed by count lines "a b k z"
//   (C = z 10^-p; with p = -1 the line holds a decimal value of C instead of an integer).  i, j from 1.
// points.txt: lines "xi v x [own_i own_j]"; with own_i own_j the element's own polynomial approximant is used alone
//   (chi psi replaced by 1, the others by 0), otherwise the blended approximant.
// out.txt: per point xi v x and the eight f_ab (curvature units, f_lx, f_nx divided by sqrt(1 - x^2)).
#include "dd.h"
#include "res_gen.h"
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <map>
#include <cstring>
#include <omp.h>

struct J2 { dd v, u, w, x, uu, uw, ww, ux, wx, xx; };   // w stands for the v-direction
static J2 jc(const dd& c) { J2 a; a.v = c; a.u = a.w = a.x = a.uu = a.uw = a.ww = a.ux = a.wx = a.xx = dd(0.0); return a; }
static J2 operator+(const J2& a, const J2& b) { J2 c; c.v = a.v + b.v; c.u = a.u + b.u; c.w = a.w + b.w; c.x = a.x + b.x; c.uu = a.uu + b.uu;
  c.uw = a.uw + b.uw; c.ww = a.ww + b.ww; c.ux = a.ux + b.ux; c.wx = a.wx + b.wx; c.xx = a.xx + b.xx; return c; }
static J2 operator*(const J2& a, const J2& b) { J2 c; c.v = a.v * b.v; c.u = a.u * b.v + a.v * b.u; c.w = a.w * b.v + a.v * b.w; c.x = a.x * b.v + a.v * b.x;
  c.uu = a.uu * b.v + dd(2.0) * a.u * b.u + a.v * b.uu; c.ww = a.ww * b.v + dd(2.0) * a.w * b.w + a.v * b.ww; c.xx = a.xx * b.v + dd(2.0) * a.x * b.x + a.v * b.xx;
  c.uw = a.uw * b.v + a.u * b.w + a.w * b.u + a.v * b.uw; c.ux = a.ux * b.v + a.u * b.x + a.x * b.u + a.v * b.ux;
  c.wx = a.wx * b.v + a.w * b.x + a.x * b.w + a.v * b.wx; return c; }

struct Block { int p, nt, ns, nx; std::vector<dd> C; };
struct Elem { int i, j; dd xlo, xhi, vlo, vhi; Block F[5]; };
static dd A_CH; static int KAPPA = 4; static std::vector<dd> CX, CV; static dd DX, DV;
static std::vector<Elem> EL;

static void cheb3(const dd& t, int n, std::vector<dd>& T0, std::vector<dd>& T1, std::vector<dd>& T2) {
  T0.assign(n, dd(0.0)); T1.assign(n, dd(0.0)); T2.assign(n, dd(0.0));
  if (n > 0) { T0[0] = dd(1.0); }
  if (n > 1) { T0[1] = t; T1[1] = dd(1.0); }
  for (int k = 1; k + 1 < n; k++) { T0[k + 1] = dd(2.0) * t * T0[k] - T0[k - 1]; T1[k + 1] = dd(2.0) * T0[k] + dd(2.0) * t * T1[k] - T1[k - 1];
    T2[k + 1] = dd(4.0) * T1[k] + dd(2.0) * t * T2[k] - T2[k - 1]; }
}
// derivatives of the block polynomial in (t, s, x): orders (a, b, c) with a + b + c <= 2 -> 10 values
static void block_eval(const Block& B, const dd& t, const dd& s, const dd& x, dd out[10]) {
  std::vector<dd> Ta[3], Sa[3], Xa[3];
  cheb3(t, B.nt + 1, Ta[0], Ta[1], Ta[2]); cheb3(s, B.ns + 1, Sa[0], Sa[1], Sa[2]); cheb3(x, B.nx + 1, Xa[0], Xa[1], Xa[2]);
  static const int ord[10][3] = {{0,0,0},{1,0,0},{0,1,0},{0,0,1},{2,0,0},{1,1,0},{0,2,0},{1,0,1},{0,1,1},{0,0,2}};
  int A = B.nt + 1, Bn = B.ns + 1, K = B.nx + 1;
  // contract x first, for x-orders 0..2
  std::vector<dd> P[3]; for (int q = 0; q < 3; q++) P[q].assign((size_t)A * Bn, dd(0.0));
  for (int a = 0; a < A; a++) for (int b = 0; b < Bn; b++) {
    const dd* c = &B.C[((size_t)a * Bn + b) * K]; dd s0(0.0), s1(0.0), s2(0.0);
    for (int k = 0; k < K; k++) { if (c[k].hi == 0) continue; s0 += c[k] * Xa[0][k]; s1 += c[k] * Xa[1][k]; s2 += c[k] * Xa[2][k]; }
    P[0][a * Bn + b] = s0; P[1][a * Bn + b] = s1; P[2][a * Bn + b] = s2;
  }
  for (int o = 0; o < 10; o++) {
    const std::vector<dd>& Pq = P[ord[o][2]]; dd tot(0.0);
    for (int a = 0; a < A; a++) { dd sb(0.0); for (int b = 0; b < Bn; b++) sb += Pq[a * Bn + b] * Sa[ord[o][1]][b]; tot += sb * Ta[ord[o][0]][a]; }
    out[o] = tot;
  }
}
// Phi(s) and its first two derivatives
static void Phi3(const dd& s, dd& p0, dd& p1, dd& p2) {
  // below s = 1/500 (above 1 - 1/500) Phi and its derivatives are below e^-400 (1 - Phi likewise): their limits
  if (!(s.hi > 0.002)) { p0 = p1 = p2 = dd(0.0); return; }
  if (!(s.hi < 0.998)) { p0 = dd(1.0); p1 = p2 = dd(0.0); return; }
  // f = e^{-1/s}, g = e^{-1/(1-s)}; Phi = f/(f+g) = 1/(1 + e^{1/s - 1/(1-s)}) =: 1/(1+e^h)
  dd h = dd(1.0) / s - dd(1.0) / (dd(1.0) - s);
  dd h1 = -dd(1.0) / (s * s) - dd(1.0) / ((dd(1.0) - s) * (dd(1.0) - s));
  dd h2 = dd(2.0) / (s * s * s) - dd(2.0) / ((dd(1.0) - s) * (dd(1.0) - s) * (dd(1.0) - s));
  dd E = exp(h); dd q = dd(1.0) / (dd(1.0) + E);    // Phi = q, dPhi/dh = -E q^2, d2Phi/dh2 = -E q^2 + 2 E^2 q^3
  dd d1 = -E * q * q, d2 = -E * q * q + dd(2.0) * E * E * q * q * q;
  p0 = q; p1 = d1 * h1; p2 = d2 * h1 * h1 + d1 * h2;
}
static void pou(const std::vector<dd>& cuts, const dd& d, const dd& y, int idx, dd& f0, dd& f1, dd& f2) {  // idx from 1
  int n = cuts.size() + 1; dd a0(1.0), a1(0.0), a2(0.0), b0(0.0), b1(0.0), b2(0.0);
  dd sc = dd(1.0) / (dd(2.0) * d);
  if (idx > 1) { Phi3((y - cuts[idx - 2] + d) * sc, a0, a1, a2); a1 = a1 * sc; a2 = a2 * sc * sc; }
  if (idx < n) { Phi3((y - cuts[idx - 1] + d) * sc, b0, b1, b2); b1 = b1 * sc; b2 = b2 * sc * sc; }
  f0 = a0 - b0; f1 = a1 - b1; f2 = a2 - b2;
}
struct SeedJ { J2 R, W; };
static SeedJ seed(const dd& u, const dd& up1, const dd& v) {
  dd H = v - dd(2.0) * u + log(up1 / (up1 - dd(2.0)));
  double Hd = to_double(H), lo = 1 + 1e-14, hi = Hd / 2 + 3;
  for (int i = 0; i < 200; i++) { double mid = 0.5 * (lo + hi); if (2 * mid + std::log((mid - 1) / (mid + 1)) < Hd) lo = mid; else hi = mid; }
  dd R(0.5 * (lo + hi));
  for (int i = 0; i < 3; i++) { dd g = dd(2.0) * R + log((R - dd(1.0)) / (R + dd(1.0))); R = R - (g - H) / (dd(2.0) + dd(2.0) / (R * R - dd(1.0))); }
  dd f = dd(1.0) - dd(1.0) / (R * R), fp = dd(2.0) / (R * R * R), fpp = dd(-6.0) / (R * R * R * R);
  dd g = dd(1.0) - dd(1.0) / (u * u), gp = dd(2.0) / (u * u * u), gpp = dd(-6.0) / (u * u * u * u);
  dd Rv = f * dd(0.5), Ru = -f / g, Rvv = fp * Rv * dd(0.5), Ruv = fp * Ru * dd(0.5), Ruu = -fp * Ru / g + f * gp / (g * g);
  dd Wv = fp * Rv / (dd(2.0) * f), Wu = (fp * Ru / f - gp / g) * dd(0.5);
  dd Wvv = (fpp * Rv * Rv + fp * Rvv) / (dd(2.0) * f) - (fp * Rv) * (fp * Rv) / (dd(2.0) * f * f);
  dd Wuv = (fpp * Ru * Rv + fp * Ruv) / (dd(2.0) * f) - (fp * Ru) * (fp * Rv) / (dd(2.0) * f * f);
  dd Wuu = ((fpp * Ru * Ru + fp * Ruu) / f - (fp * Ru / f) * (fp * Ru / f) - (gpp / g - (gp / g) * (gp / g))) * dd(0.5);
  SeedJ s; s.R = jc(R); s.R.u = Ru; s.R.w = Rv; s.R.uu = Ruu; s.R.uw = Ruv; s.R.ww = Rvv;
  s.W = jc(dd(0.5) * log(f / (dd(2.0) * g))); s.W.u = Wu; s.W.w = Wv; s.W.uu = Wuu; s.W.uw = Wuv; s.W.ww = Wvv;
  return s;
}
static std::map<std::string, int> RJ;
static void residual(const dd& xi, const dd& v, const dd& x, int own_i, int own_j, dd out[8]) {
  dd sh = sinh(xi), ch = cosh(xi), up1 = A_CH * sh, u = up1 - dd(1.0);
  dd xu = dd(1.0) / (A_CH * ch), xuu = -sh / (A_CH * A_CH * ch * ch * ch);   // dxi/du, d2xi/du2
  SeedJ sd = seed(u, up1, v);
  J2 S[5]; for (int f = 0; f < 5; f++) S[f] = jc(dd(0.0));
  for (auto& e : EL) {
    J2 chi = jc(dd(1.0)), psi = jc(dd(1.0));
    if (own_i) { if (e.i != own_i || e.j != own_j) continue; }
    else {
      dd c0, c1, c2; pou(CX, DX, xi, e.i, c0, c1, c2);
      if (c0.hi == 0 && c1.hi == 0) continue;
      chi = jc(c0); chi.u = c1 * xu; chi.uu = c2 * xu * xu + c1 * xuu;
      dd p0, p1, p2; pou(CV, DV, v, e.j, p0, p1, p2);
      if (p0.hi == 0 && p1.hi == 0) continue;
      psi = jc(p0); psi.w = p1; psi.ww = p2;
    }
    dd hx = (e.xhi - e.xlo) * dd(0.5), mx = (e.xhi + e.xlo) * dd(0.5), hv = (e.vhi - e.vlo) * dd(0.5), mv = (e.vhi + e.vlo) * dd(0.5);
    dd t = (xi - mx) / hx, s = (v - mv) / hv;
    dd tu = xu / hx, tuu = xuu / hx, sv = dd(1.0) / hv;
    for (int f = 0; f < 5; f++) {
      dd g[10]; block_eval(e.F[f], t, s, x, g);
      J2 G; G.v = g[0]; G.u = g[1] * tu; G.w = g[2] * sv; G.x = g[3]; G.uu = g[4] * tu * tu + g[1] * tuu; G.uw = g[5] * tu * sv;
      G.ww = g[6] * sv * sv; G.ux = g[7] * tu; G.wx = g[8] * sv; G.xx = g[9];
      S[f] = S[f] + chi * psi * G;
    }
  }
  J2 ek = jc(dd(1.0)), ev = jc(v - dd(0.5)); ev.w = dd(1.0);
  for (int q = 0; q < KAPPA; q++) ek = ek * ev;
  J2 F[5]; for (int f = 0; f < 5; f++) F[f] = ek * S[f];
  F[0] = F[0] + sd.R; F[3] = F[3] + sd.W;
  static const char* nm[5] = {"R", "m", "n", "W", "s"};
  std::vector<dd> J(RES_NJ, dd(0.0));
  auto put = [&](const std::string& k, const dd& val) { auto it = RJ.find(k); if (it != RJ.end()) J[it->second] = val; };
  for (int f = 0; f < 5; f++) { std::string b = nm[f];
    put(b, F[f].v); put(b + "_u", F[f].u); put(b + "_v", F[f].w); put(b + "_x", F[f].x); put(b + "_uu", F[f].uu); put(b + "_uv", F[f].uw);
    put(b + "_vv", F[f].ww); put(b + "_ux", F[f].ux); put(b + "_vx", F[f].wx); put(b + "_xx", F[f].xx); }
  dd Sx = ((dd(1.0) + x) * F[1].v + (dd(1.0) - x) * F[2].v) / dd(3.0);
  put("ES", exp(Sx)); put("iES", exp(-Sx)); put("iR", dd(1.0) / F[0].v); put("iOM2", exp(dd(-2.0) * F[3].v));
  std::vector<dd> K; for (int i = 0; i < RES_NK; i++) K.push_back(dd((double)RES_KNUM[i]) / dd((double)RES_KDEN[i]));
  dd o[8]; res_eval(J.data(), K.data(), x, o);
  dd R4 = F[0].v * F[0].v * F[0].v * F[0].v, rho = R4 / sqrt(dd(72.0));
  for (int i = 0; i < 8; i++) out[i] = rho * o[i];
}
static dd pow10(int p) { dd r(1.0); for (int i = 0; i < p; i++) r = r * dd(10.0); return r; }
int main(int argc, char** argv) {
  for (int i = 0; i < RES_NJ; i++) RJ[RES_JET[i]] = i;
  std::ifstream f(argv[1]); std::string line; Elem* cur = nullptr;
  A_CH = dd(1.0) / dd(500.0);
  while (std::getline(f, line)) {
    std::istringstream is(line); std::string k; if (!(is >> k)) continue;
    if (k == "kappa") is >> KAPPA;
    else if (k == "pou_xi" || k == "pou_v") { int n; is >> n; std::vector<dd>& c = (k == "pou_xi") ? CX : CV; c.clear();
      std::string s; for (int q = 0; q < n - 1; q++) { is >> s; c.push_back(dd_from_string(s.c_str())); } is >> s; (k == "pou_xi" ? DX : DV) = dd_from_string(s.c_str()); }
    else if (k == "elem") { EL.emplace_back(); cur = &EL.back(); std::string a, b, c, d; is >> cur->i >> cur->j >> a >> b >> c >> d;
      cur->xlo = dd_from_string(a.c_str()); cur->xhi = dd_from_string(b.c_str()); cur->vlo = dd_from_string(c.c_str()); cur->vhi = dd_from_string(d.c_str()); }
    else if (k == "field") { int fl, p, nt, ns, nx; long cnt; is >> fl >> p >> nt >> ns >> nx >> cnt; Block& B = cur->F[fl];
      B.p = p; B.nt = nt; B.ns = ns; B.nx = nx; B.C.assign((size_t)(nt + 1) * (ns + 1) * (nx + 1), dd(0.0));
      dd sc = p >= 0 ? dd(1.0) / pow10(p) : dd(1.0);
      for (long q = 0; q < cnt; q++) { std::getline(f, line); std::istringstream js(line); int a, b, kk; std::string z; js >> a >> b >> kk >> z;
        B.C[((size_t)a * (ns + 1) + b) * (nx + 1) + kk] = dd_from_string(z.c_str()) * sc; } }
  }
  std::vector<std::array<double, 0>> dummy;
  std::ifstream pf(argv[2]); std::vector<std::string> P; while (std::getline(pf, line)) if (!line.empty()) P.push_back(line);
  std::vector<std::string> res(P.size());
  #pragma omp parallel for schedule(dynamic)
  for (size_t q = 0; q < P.size(); q++) {
    std::istringstream is(P[q]); std::string a, b, c; int oi = 0, oj = 0; is >> a >> b >> c >> oi >> oj;
    dd o[8]; residual(dd_from_string(a.c_str()), dd_from_string(b.c_str()), dd_from_string(c.c_str()), oi, oj, o);
    char buf[512]; int n = snprintf(buf, sizeof buf, "%s %s %s", a.c_str(), b.c_str(), c.c_str());
    for (int i = 0; i < 8; i++) n += snprintf(buf + n, sizeof buf - n, " %.6e", to_double(o[i]));
    res[q] = buf;
  }
  std::ofstream o(argv[3]); for (auto& s : res) o << s << "\n";
}
