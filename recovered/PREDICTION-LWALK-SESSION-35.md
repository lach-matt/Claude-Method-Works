# PREDICTION-LWALK (s35) — the l-walk with n. Written BEFORE any run (R 1449). Ruled by M (s35: pivot from the Z-walk of SPEC-WALK-SESSION-32 to l at fixed n).
Object: row Z, entrant placed in each candidate channel (n,l) of the frontier and its neighbours; removal energy D(n,l) = E_neu(entrant in n,l) - E_ion read three
ways: (i) frozen on the HFS neutral field (t5 orbitals; the s35 frozen reference), (ii) frozen on the HF neutral field (Koopmans, hfc2), (iii) relaxed E path (t5 SCF
per channel, xseam_relax energy functional). Steps: Delta_l := D(n,l+1)-D(n,l) at fixed n; Delta_n := D(n+1,l)-D(n,l) at fixed l. Loewdin/Madelung frontier
statement: (n,l) and (n+1,l-1) near-degenerate, i.e. Delta_l(at n+1... ) ~ Delta_n; tie to the higher-n (lower-l) member. Rows: Sc (4s/3d/4p), Y (5s/4d/5p),
La (6s/5d/4f/6p), Lu (6s/5d/6p), Cs (6s/5d/4f/6p). Enumerated channels, no scan.
Predictions:
 PL1 frontier near-degeneracy: on the relaxed point, |D(n+1,l-1) - D(n,l)| < 0.05 Ha for the frontier pair of every row (Sc 4s/3d, Y 5s/4d, La 6s/5d, Lu 6s/5d,
     Cs 6s/5d), while a non-frontier l step at fixed n (e.g. 3d->4f-side or 4s->4p) exceeds 0.10 Ha.
 PL2 ordering is field-invariant: the deeper member of the frontier pair is the same on (i), (ii) and (iii) on every row, though the values move 0.02-0.07.
 PL3 bracketing holds off the ground state: for every enumerated channel, D(iii) lies between D(i) and D(ii) (the two frozen fields are bounds), sign-fixed
     as on the ground-state channel of FINDING-B2.
 PL4 falsifier: an ordering flip between (i) and (ii) on any row means n+l is not a frozen-field property and the relaxed step is required; the row and the
     pair are then NAMED.
Bound in advance: PL1 measured on (iii) only; PL2/PL3 need (ii); if (ii) is not reached this session, PL2/PL3 are scored on (i) vs (iii) and marked partial.
No constant; no measured input; nothing entered.