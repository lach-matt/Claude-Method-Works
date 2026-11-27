// scheme.h: the iteration scheme (S-RULE §3.7), kept apart from the cell operator so that it can be replaced (for
// example by the mixed-precision defect correction under evaluation) without touching anything else.
//
// Interface: a Batch of cells, each holding B (Bt) and its current iterate G.  A scheme leaves in each cell its final
// G and, in Psi, Ψ and Φ evaluated at that final G (needed for the top edge's s_v).  It may call `ckpt(n)` between
// sweeps to let the driver save the batch's state; resuming from that state at sweep n must give the same result.
#pragma once
#include "cell.h"
#include <functional>

// Plain Picard (§3.7): G^0 := B, G^(n+1) := B + I(G^n), the cell's value G^(N_P).  A cell whose sweep leaves every
// integer unchanged is frozen: its remaining sweeps would change nothing, so the output is identical.
inline void scheme_picard(Batch& bt, int NP, int start_sweep, const std::function<void(int)>& ckpt) {
  for (int n = start_sweep; n < NP; n++) {
    bt.evaluate();                                   // Ψ(G^n), Φ(G^n)
    bt.integrate();                                  // Gn = B + I
    for (Cell* c : bt.cells) {
      if (c->frozen) continue;
      bool same = true;
      for (size_t i = 0; i < c->G.size() && same; i++) same = (c->G[i] == c->Gn[i]);
      c->G.swap(c->Gn); c->sweeps = n + 1;
      if (same) { c->frozen = true; c->psi_is_final = true; }   // Psi holds Ψ(G^n) = Ψ(G^(n+1))
    }
    ckpt(n + 1);
  }
  // Φ at the final iterate, for every cell that did not freeze [Q15]
  for (Cell* c : bt.cells) { if (c->psi_is_final) c->frozen = true; else c->frozen = false; }
  std::vector<Cell*> keep = bt.cells; Batch rest;
  for (Cell* c : keep) if (!c->psi_is_final) rest.cells.push_back(c);
  if (!rest.cells.empty()) rest.evaluate();
  for (Cell* c : keep) { c->psi_is_final = true; c->frozen = true; }
}
