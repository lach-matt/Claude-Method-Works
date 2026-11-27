// unit test of fx.h against exact integer arithmetic done in Python (values printed as integers X = x 2^B)
#include "fx.h"
#include <cstdio>
#include <random>
template<int L> void pr(const char* tag, const fx<L>& a) {
  // print as signed big integer in hex limbs (python reconstructs)
  printf("%s", tag); for (int i = L - 1; i >= 0; i--) printf(" %016llx", (unsigned long long)a.w[i]); printf("\n");
}
int main() {
  const int L = 6;
  std::mt19937_64 g(7); std::uniform_real_distribution<double> U(-20, 20);
  for (int t = 0; t < 200; t++) {
    double a = U(g), b = U(g), c = U(g);
    fx<L> A = from_double<L>(a), B = from_double<L>(b), C = from_double<L>(std::fabs(c) + 0.5);
    A = A * from_double<L>(1.0 / 3.0) + from_double<L>(1e-30 * U(g));      // fill low limbs
    B = B * from_double<L>(1.0 / 7.0) - from_double<L>(1e-40 * U(g));
    pr("A", A); pr("B", B); pr("C", C);
    pr("M", A * B); pr("S", A - B); pr("R", recip(C));
    acc<L> ac; ac.add(A, B); ac.add(B, C); ac.add(C, A); pr("D", ac.get());
    pr("V", divi(A, 7)); pr("E", fexp<L, 45>(divi(A, 400)));
  }
}
