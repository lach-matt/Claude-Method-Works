// scheme.h: the iteration in a cell (P-APPC2 def:appc-iteration), apart from the cell map (cell.h).
//
// Interface: a Batch of cells, each holding its boundary term B (Bt), its iterate G (initially B) and its counts
// (No, Ni).  A scheme leaves in each cell its final G and, in Psi[FS], the Φ of the last evaluation of P (the top
// values use it, def:appc-cell (e)).  It calls ckpt(o) after outer step o so that the driver can save the batch's G;
// resuming from that G before step o + 1 gives the same result, since an outer step depends on G alone.
#pragma once
#include "cell.h"
#include <functional>
#include <ctime>
// cpu-time accounting of the two parts of an outer step (diagnostics only)
struct SchemeTimes { double tP = 0, tI = 0; long nP = 0, nI = 0; };
inline SchemeTimes& scheme_times() { static SchemeTimes t; return t; }
inline double scheme_cpu() { timespec t; clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &t); return t.tv_sec + 1e-9 * t.tv_nsec; }

// max |r| over all entries of r (the integer of the largest magnitude), and its bit length
inline int fx_bitlen_abs(const F& a) { uint64_t m[6]; fx_abs(a, m); for (int i = 5; i >= 0; i--) if (m[i]) return 64 * i + 64 - __builtin_clzll(m[i]); return 0; }

// def:appc-iteration: N_o outer steps; each forms the defect r := P(G) − G in 𝔽, scales it by 2^ν (2^(−ν) <= max|r| <
// 2^(1−ν)), corrects by N_i sweeps d := r̃ ⊕ I_𝔻(d) in 𝔻, and updates G := G + ⌊2^(−ν) d⌋_B.  r = 0 leaves G unchanged.
inline void scheme_defect(Batch& bt, int start_outer, const std::function<void(int)>& ckpt) {
  int No = 0; for (Cell* c : bt.cells) No = std::max(No, c->No);
  // A cell whose defect was exactly 0 keeps G, and every later step forms the same P(G) and the same r = 0; such a
  // cell is not evaluated again, but each of its later steps still records max |r| = 0, so that the history has N_o
  // entries as in the text, whether or not the run was resumed.  (A checkpoint stores G and the history, not this
  // flag: a resumed run evaluates such a cell once more, finds r = 0 again, and so also recomputes the Φ the top
  // values need.)
  for (Cell* c : bt.cells) c->zero_defect = false;
  for (int o = start_outer; o < No; o++) {
    std::vector<Cell*> act;
    for (Cell* c : bt.cells) {
      if (o >= c->No) continue;
      if (c->zero_defect) { c->rmax.push_back(fx_zero<6, 5>()); c->outer_done = o + 1; } else act.push_back(c);
    }
    if (act.empty()) { ckpt(o + 1); continue; }
    double t0 = scheme_cpu();
    bt.evaluate(act); bt.integrate(act);                         // (i) P(G), and J̄ = rd J(G)
    scheme_times().tP += scheme_cpu() - t0; for (Cell* c : act) scheme_times().nP += c->NN();
    std::vector<Cell*> corr;
    for (Cell* c : act) {
      const size_t n = c->G.size(); int bl = 0; F rm = fx_zero<6, 5>();
      for (size_t q = 0; q < n; q++) { c->Gn[q] = c->Gn[q] - c->G[q]; int b = fx_bitlen_abs(c->Gn[q]); if (b > bl) { bl = b; rm = c->Gn[q]; } }
      if (fx_neg(rm)) rm = -rm;
      // the exact maximum (bl only locates its bit length; scan for the largest magnitude of that length)
      for (size_t q = 0; q < n; q++) { F a = fx_neg(c->Gn[q]) ? -c->Gn[q] : c->Gn[q]; if (rm < a) rm = a; }
      c->rmax.push_back(rm); c->outer_done = o + 1;
      if (bl == 0) { c->zero_defect = true; continue; }          // r = 0: G stays, and so do the later steps
      c->nu = 321 - bl;
      corr.push_back(c);
    }
    for (Cell* c : corr) {                                        // (ii) r̃ := rd(2^ν r), d := r̃
      const size_t n = c->G.size();
      #pragma omp parallel for schedule(static)
      for (size_t q = 0; q < n; q++) { c->rt[q] = rd_fx(c->Gn[q], c->nu); c->d[q] = c->rt[q]; }
    }
    int Ni = 0; for (Cell* c : corr) Ni = std::max(Ni, c->Ni);
    for (int it = 0; it < Ni; it++) {                             // N_i times d := r̃ ⊕ I_𝔻(d), each cell its own N_i
      std::vector<Cell*> run; for (Cell* c : corr) if (it < c->Ni) run.push_back(c);
      double t1 = scheme_cpu(); bt.lin(run); scheme_times().tI += scheme_cpu() - t1; for (Cell* c : run) scheme_times().nI += c->NN();
      for (Cell* c : run) {
        const size_t n = c->G.size();
        #pragma omp parallel for schedule(static)
        for (size_t q = 0; q < n; q++) c->d[q] = c->rt[q] + c->Id[q];
      }
    }
    for (Cell* c : corr) {                                        // (iii) G := G + ⌊2^(−ν) d⌋_B
      const size_t n = c->G.size();
      #pragma omp parallel for schedule(static)
      for (size_t q = 0; q < n; q++) c->G[q] = c->G[q] + floor_scaled(c->d[q], c->nu);
    }
    ckpt(o + 1);
  }
}

// rem:appc-picard, the plain iteration (not the rule): N_P steps G := P(G); used by `rule pilotcell` only
inline void scheme_picard(Batch& bt, int NP) {
  std::vector<Cell*> act = bt.cells;
  for (int n = 0; n < NP; n++) { bt.evaluate(act); bt.integrate(act); for (Cell* c : act) c->G.swap(c->Gn); }
}
