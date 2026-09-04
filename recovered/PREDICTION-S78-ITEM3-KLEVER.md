# PREDICTION S78 — ITEM 3, THE EIGENINDEX LEVER TEST. Filed before the run.
# No probe was run for this item. Nothing below has been computed in any form.

## WHERE THE EIGENINDEX ACTUALLY LIVES — read from source, not run
t7c_hfsr.solve_one does NOT select an eigenvalue by index. With exchange present it
brackets from `eh = eigen_sr(Vf, l, n, 1.0, self.Z, c, ...)` and then BISECTS TO A ZERO OF
log(nrm). The node count nd is computed, RETURNED, and checked by the CALLER (hfc2.py:55).
**So k is implicit and is set by two things: the bracket seeded from (n,l), and which zero
of log(nrm) the bisection lands on.** The only lever on it is `n` in the eigen_sr call,
and **n is passed POSITIONALLY — patching a default would be dead, which is F54.2 exactly.**
The poison therefore wraps the module-level name `t7c_hfsr.eigen_sr`.

## PREDICTIONS
  K1 The wrapper IS REACHED: the call counter is > 0 when a converged solve is run.
     **If it is 0 the lever is dead and item 3 is VOID before it starts.**
  K2 Poisoning n -> n+1 MOVES THE OUTPUT. I predict the move is not a small energy shift
     but a **NODE-COUNT RAISE from hfc2.py:55**: the bracket is displaced to a less bound
     region, the bisection finds a different zero, and the state returned carries the
     wrong node count for the orbital requested.
  K3 Poisoning n -> n-1 also moves the output, and for the SAME reason.
  K4 If any orbital survives the poison with an unchanged converged energy to 1e-6 Ha,
     that orbital's bracket is insensitive to n, and **that is the finding, not a failure.**

## WHAT THE VERDICT MEANS FOR RUNG B
Rung B is an EIGENINDEX SELECTOR: choose eps_k of the radial Fock operator directly, so
that Courant-Fischer's eps_1 < eps_2 < ... applies at a fixed field. **A PASS here does
not build Rung B. It establishes only that the quantity Rung B would vary is a live input
to the converged answer.** A VOID here would mean the walk's energies do not depend on the
eigenindex at all, and Rung B could not be built on this solver.