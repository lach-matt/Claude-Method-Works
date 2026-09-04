# FINDING S77a — THE RUNG A CAVEAT, SETTLED FROM SOURCE. RUNG A STANDS.
# Owed item 1 of DESIGN-S76 §"ORDER FOR s77". Settled by reading the chain, not by recall.

## THE QUESTION
Is each non-winning `order` row a FULL self-consistent solution at that occupancy, or
a differentiating-electron energy computed in the frozen cfg(Z-1) field? If the latter,
the rows are not critical points and Rung A collapses.

## THE SOURCE — rt/nlchain.py `step()`, lines 56-95
    gr = NG.run_guarded(Z, cfg_prev, 'ref')          # the CATION: charge Z, Z-1 electrons
    for c in cands:
        g = NG.run_guarded(Z, add(cfg_prev, c), tagof(c))
        D[tag] = dict(D=round(g['E'] - Eref, 5), it=g['it'], rung=g['rung'], ...)
and rt/nlguard.py `run_guarded()`, line 64:
    E, _, it, eps = H.HFC(Z, [tuple(x) for x in cfg], c=C0).run2(beta=beta, maxit=maxit)

**EVERY CANDIDATE IS A FRESH, FULL, GUARDED SCF SOLVE AT NUCLEAR CHARGE Z CARRYING ITS
OWN Z-ELECTRON OCCUPANCY `cfg_prev + c`.** Nothing is frozen. `run2` is the self-consistent
loop; the ladder is climbed per candidate; a candidate that converges at no rung returns
no number and joins `fail` beside the node-count failures.

## WHAT `D` IS, EXACTLY
D = E(cfg_prev + c) - E(cfg_prev), a difference of TWO CONVERGED TOTAL ENERGIES at the
same nuclear charge Z. It is a binding energy, not an eigenvalue. **Eref is one common
constant per Z, so argmin over D is identically argmin over E** — which is the same
statement s76 §3 makes about the common mode: a constant added to every candidate leaves
the argmin invariant.

## CORROBORATION IN THE SEALED RECORD, INDEPENDENT OF THE SOURCE
nlchain.jsonl Z=89 carries a per-channel `chan` map: 5f it=320 rung=1, 6d it=44 rung=0,
7p it=36 rung=0, eight channels at it=37 rung=0, and five channels failed on node count
(6f, 7d, 7f, 8d, 8f). **A frozen-field evaluation has no per-channel iteration count, no
per-channel rung, and no per-channel convergence failure.** The record could not have
this shape unless each channel were separately converged.

## VERDICT
**RUNG A DOES NOT COLLAPSE.** The nine converged rows at Z=89 are nine distinct
occupancy sectors, each self-consistently solved: nine constrained critical points of the
same restricted-HF functional at the same Z. The `order` column is already a sample of
Lions' occupancy family, at zero cost, as DESIGN-S76 proposed.
**CONSEQUENCE FOR s76 §3:** D(Z) is NOT narrower than stated. The invariance criterion
2*D(Z) < m(Z) keeps the breadth s76 gave it — still measured at 3 rows and proved nowhere.
**WHAT IS STILL NOT SAMPLED:** the node-excited axis. Rung A varies occupancy only; every
row takes the lowest radial eigenfunction in each channel. Rung B remains the open build.