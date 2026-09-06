# PREDICTION — T7c-OCC: occupation-dependence of the local TS object (session 21). Bridge-20 §3(2). Ruled by M s21.
Object: t5_scf.scf_occ (spin-averaged local HFS, Dirac exchange, HFS total energy). NONREL. Tail FIXED -1/r at every q
(banked convention; (c) ruled the moving tail out in s20). No constant, no measured input; recalled IPs comparison only.
Rows: Sc 3d (Z=21), Y 4d (39), Cs 6s (55). Entrant occupation q on ground(Z-1)+entrant, q = 0, 1/8, ..., 1 (9 points).
Quantities: eps(q) entrant eigenvalue; J = int_0^1 eps dq (Simpson, 9 pts) = Janak removal energy; D = E(q=1) - E(q=0) (dSCF);
            T = eps(1/2) (the banked TS observable). Curvature term kappa = T - J.
P2a  Janak identity holds on the object: |J - D| <= 0.001 Ha on all three rows. (If it fails, the object's Etot is inconsistent
     with its eigenvalues and nothing downstream is readable — fault, register before reading.)
P2b  eps(q) is nearly linear for s and curved for d: |kappa| <= 0.005 Ha for Cs 6s; 0.01 <= |kappa| <= 0.03 Ha for Sc 3d and Y 4d,
     with kappa > 0 (TS eigenvalue shallower than the Janak/dSCF removal energy) -- i.e. the d-class shallowness of bridge-20's
     SHELL finding sits in the half-occupation (TS) APPROXIMATION, not in the local functional.
P2c  kappa(Y 4d) >= kappa(Sc 3d) (ordering matches the SHELL finding Sc +0.011 < Y +0.013 nonrel).
Reading rule: P2b holding -> shallowness is a TS-approximation term and Slater's exact TS (J) is the derivable replacement to test on
5d/4f next; P2b failing with kappa small -> shallowness is in the functional (exchange kernel), and (3) SR-HF or SIC becomes the
target. Either way P2a must hold first.
