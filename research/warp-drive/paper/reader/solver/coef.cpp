// coef.cpp: element-node values (.elem, from the solver) -> Chebyshev coefficients in (t, sigma, x), double-double.
// usage: coef run.elem out.coef  ; writes binary: "BSOLC1", ne, NX, then per element Nt, Ns and (5, Nt+1, Ns+1, NX)
// Real pairs: C[f][i][j][l] with G = sum C T_i(t) T_j(sigma) T_l(x) on the element's box.
#include "real.h"
#include <vector>
#include <fstream>
#include <cstring>
#include <omp.h>
static void dct_mat(int N, bool ascending, std::vector<Real>& D) {   // D[i][a]: coefficient i from value at node a
  D.assign((size_t)(N + 1) * (N + 1), Real(0.0));
  for (int i = 0; i <= N; i++) for (int a = 0; a <= N; a++) {
    int aa = ascending ? N - a : a;                  // node a is cos(pi aa / N)
    long m = ((long)i * aa) % (2 * N);
    Real c = cos(R_PI * Real((double)m) / Real((double)N));
    Real w = (a == 0 || a == N) ? Real(0.5) : Real(1.0);
    Real s = Real(2.0) / Real((double)N) * w * c;
    if (i == 0 || i == N) s = s * Real(0.5);
    D[(size_t)i * (N + 1) + a] = s;
  }
}
int main(int argc, char** argv) {
  std::ifstream f(argv[1], std::ios::binary); char mg[6]; f.read(mg, 6);
  int ne, NX; f.read((char*)&ne, 4); f.read((char*)&NX, 4);
  std::ofstream o(argv[2], std::ios::binary); o.write("BSOLC1", 6); o.write((char*)&ne, 4); o.write((char*)&NX, 4);
  int M = NX - 1; std::vector<Real> Dx; dct_mat(M, false, Dx);
  for (int e = 0; e < ne; e++) {
    int nt, ns; long nd; size_t n; f.read((char*)&nt, 4); f.read((char*)&ns, 4); f.read((char*)&nd, 8); f.read((char*)&n, 8);
    std::vector<Real> V(n); f.read((char*)V.data(), n * 16);
    std::vector<Real> Dt, Ds; dct_mat(nt, true, Dt); dct_mat(ns, true, Ds);
    std::vector<Real> C(n), T1(n);
    size_t A = nt + 1, B = ns + 1;
    for (int fl = 0; fl < 5; fl++) {
      Real* v = &V[fl * A * B * NX]; Real* c = &C[fl * A * B * NX]; Real* t1 = &T1[fl * A * B * NX];
      #pragma omp parallel for
      for (size_t ab = 0; ab < A * B; ab++) for (int l = 0; l < NX; l++) { Real s(0.0); for (int k = 0; k < NX; k++) s += Dx[(size_t)l * NX + k] * v[ab * NX + k]; t1[ab * NX + l] = s; }
      #pragma omp parallel for
      for (size_t a = 0; a < A; a++) for (size_t j = 0; j < B; j++) for (int l = 0; l < NX; l++) { Real s(0.0); for (size_t b = 0; b < B; b++) s += Ds[j * B + b] * t1[(a * B + b) * NX + l]; c[(a * B + j) * NX + l] = s; }
      #pragma omp parallel for
      for (size_t i = 0; i < A; i++) for (size_t j = 0; j < B; j++) for (int l = 0; l < NX; l++) { Real s(0.0); for (size_t a = 0; a < A; a++) s += Dt[i * A + a] * c[(a * B + j) * NX + l]; t1[(i * B + j) * NX + l] = s; }
      memcpy(c, t1, A * B * NX * 16);
    }
    o.write((char*)&nt, 4); o.write((char*)&ns, 4); o.write((char*)C.data(), n * 16);
  }
}
