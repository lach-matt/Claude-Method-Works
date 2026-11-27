// randomized check of fixp.h against Python's integers (t_fixp.py reads this program's output)
#include "../fixp.h"
#include <random>
#include <vector>
static std::mt19937_64 rng(12345);
static F rnd() {   // magnitudes spread over many scales, both signs
  F a; for (int i = 0; i < 6; i++) a.w[i] = rng();
  int sh = rng() % 380; a = shr(a, sh); a.w[5] &= (1ull << 27) - 1; if (rng() & 1) a = -a; if (rng() % 17 == 0) a = fx_zero<6,5>();
  return a;
}
int main() {
  for (int t = 0; t < 3000; t++) {
    F a = rnd(), b = rnd(); int64_t n = 1 + rng() % 1000; int k = rng() % 300;
    printf("%s %s %ld %d", fx_dec(a).c_str(), fx_dec(b).c_str(), (long)n, k);
    F ab = a * b; printf(" %s", fx_dec(ab).c_str());
    F bd = b; if (!fx_iszero(bd)) { int s2 = 0; F mag = fx_neg(bd) ? -bd : bd; while (mag < fx_int<6,5>(1) && s2 < 20) { bd = mul_int(bd, 1 << 20); mag = mul_int(mag, 1 << 20); s2++; } }
    printf(" %s %s", fx_dec(bd).c_str(), fx_iszero(bd) ? "Z" : fx_dec(fdiv(a, bd)).c_str());
    printf(" %s %s %s", fx_dec(divi(a, n)).c_str(), fx_dec(shr(a, k)).c_str(), fx_dec(a + b).c_str());
    printf(" %s %s", fx_dec(a - b).c_str(), fx_dec(mul_int(a, (rng() & 1) ? -(int64_t)n : (int64_t)n)).c_str());
    F aa = a; if (fx_neg(aa)) aa = -aa; printf(" %s", fx_dec(fsqrt(aa)).c_str());
    int m = 1 + rng() % 40; std::vector<S> x(m), y(m); std::vector<F> xf(m), yf(m);
    for (int i = 0; i < m; i++) { xf[i] = rnd(); yf[i] = rnd(); x[i] = to_sm(xf[i]); y[i] = to_sm(yf[i]); }
    printf(" %d", m); for (int i = 0; i < m; i++) printf(" %s %s", fx_dec(xf[i]).c_str(), fx_dec(yf[i]).c_str());
    printf(" %s\n", fx_dec(dot<6,5>(x.data(), 1, y.data(), 1, m)).c_str());
    if (from_sm<6,5>(x[0]) != xf[0]) { printf("SM roundtrip failed\n"); return 1; }
  }
}
