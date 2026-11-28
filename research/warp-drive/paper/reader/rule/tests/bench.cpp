// micro-benchmarks of the per-node pieces (not part of the rule)
#include "../cell.h"
#include <chrono>
Consts CS;
static double t() { return std::chrono::duration<double>(std::chrono::steady_clock::now().time_since_epoch()).count(); }
int main() {
  init_consts(2); CS.K.resize(RHS_NK); for (int i = 0; i < RHS_NK; i++) CS.K[i] = fl_rat<F>(RHS_KNUM[i], RHS_KDEN[i]);
  F a = fl_rat<F>(1, 3), b = fl_rat<F>(-22, 23), c = fl_rat<F>(1, 7000);
  int N = 2000000; double t0 = t(); F s = a;
  for (int i = 0; i < N; i++) { s = s * b; s = s * a; } printf("mul: %.1f ns\n", (t() - t0) / (2.0 * N) * 1e9);
  t0 = t(); for (int i = 0; i < N; i++) s = s + c; printf("add: %.1f ns\n", (t() - t0) / N * 1e9);
  t0 = t(); F q = a; for (int i = 0; i < N; i++) q = divi(q + a, 7 + i % 30); printf("divi: %.1f ns\n", (t() - t0) / N * 1e9);
  t0 = t(); for (int i = 0; i < N / 10; i++) q = fdiv(c, q + a); printf("fdiv: %.1f ns\n", (t() - t0) / (N / 10) * 1e9);
  t0 = t(); F e; for (int i = 0; i < 20000; i++) e = expF(c + q); printf("exp: %.2f us\n", (t() - t0) / 20000 * 1e6);
  F J[RHS_NJ]; for (int i = 0; i < RHS_NJ; i++) J[i] = fl_rat<F>(1 + i, 37 + 3 * i); J[0] = fl_rat<F>(10, 1); J[1] = fdiv(one<F>(), J[0]);
  F out[5]; t0 = t(); for (int i = 0; i < 20000; i++) { J[8] = J[8] + c; rhs_at(J, a, out); } printf("rhs: %.2f us\n", (t() - t0) / 20000 * 1e6);
  std::vector<S> x(81), y(81); for (int i = 0; i < 81; i++) { x[i] = to_sm(fl_rat<F>(i + 1, 3)); y[i] = to_sm(fl_rat<F>(1, 1000 + i)); }
  t0 = t(); for (int i = 0; i < 100000; i++) { q = q + dot<6, 5>(x.data(), 1, y.data(), 1, 81); } printf("dot81: %.2f us (%.1f ns/term)\n", (t() - t0) / 100000 * 1e6, (t() - t0) / 100000 / 81 * 1e9);
  printf("%s %s\n", fx_dec(s).substr(0, 5).c_str(), fx_dec(out[0] + e + q).substr(0, 5).c_str());
}
