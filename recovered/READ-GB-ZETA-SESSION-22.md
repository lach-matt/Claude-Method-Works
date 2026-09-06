# READ — zeta-dependence of the high-density correlation limit (bridge-21 s3(3), ruled s22 "do", READ ONLY). Sources: Loos & Gill PRB 84,
033103 (2011) (arXiv 1104.0498, fetched, read in full); Hoffman PRB 45, 8730 (1992) NOT fetched (paywalled; content known only through
Loos-Gill's citation of it). Nothing run.
## What is derived (closed form or exact-numeric, no fitting) -- the high-density series eps_c(r_s,zeta) = lam0(zeta) ln r_s + eps0(zeta) + lam1(zeta) r_s ln r_s + O(r_s):
(a) lam0(zeta): GB 1957 resummation, closed-form spin scaling Lambda0(zeta) = 1/2 + [k_dn k_up (k_dn+k_up) - k_dn^3 ln(1+k_up/k_dn) - k_up^3 ln(1+k_dn/k_up)]
    /(4(1-ln2)), k_s = (1 +/- zeta)^{1/3}  (Wang & Perdew 1991, Loos-Gill Eq. 5). lam0(0) = (1-ln2)/pi^2, lam0(1) = lam0(0)/2. DERIVED for all zeta.
(b) eps0(zeta) = eps0^a(zeta) + eps0^b:  eps0^b = ln2/6 - 3 zeta(3)/(4 pi^2) = +0.02419 (Onsager-Mittag-Stephen 1966), zeta-INDEPENDENT, closed form.
    eps0^a(zeta) (RPA constant): NOT closed form; exact-numeric integral (Hoffman 1992 Eq. 20; Loos-Gill Table I): eps0^a(0) = -0.0710995,
    eps0^a(1) = -0.0499167; a "Hoffman minimum" near zeta = 0.9956. The zeta = 1 endpoint follows from zeta = 0 by Misawa's exact scaling
    E^a(r_s,1) = E^a(2^{-4/3} r_s,0)/2 -> eps0^a(1) = [eps0^a(0) - (4/3) ln2 lam0(0)]/2 = -0.0499 (checked). Intermediate zeta: Hoffman's integral only.
(c) lam1(zeta): CLOSED FORM (Loos-Gill 2011 Eqs. 16-19), lam1(0) = 0.0092292, lam1(1) = 0.0047923 (corrects Perdew-Wang's 0.003125; a limit and an
    integral that do not commute). This is the NEXT term of the series -- exact, attributed, extends the series' reach toward r_s ~ 1-2.
## Bearing on the standing (bridge-21 s2, FINDING-T7C-CORR)
1. CONSTANTS: the banked B_U = -0.048 / B_P = -0.0269 are PZ-81's quoted GB values (GB rounded, -0.096 Ry). The exact values are B_U = eps0^a(0)+eps0^b
   = -0.0469, B_P = -0.0257 (Loos-Gill Table I / Onsager). Difference +0.0011/+0.0012 in eps_c -> the U/P shifts move ~+0.001 shallower each.
   ATTRIBUTION REFINEMENT to record (not a fault: quoted-exact stands, but the more exact figure has an owner).
2. THE BRACKET CAN BECOME A NUMBER on an attributed path: lam0(zeta) is closed form (a) and eps0^b is constant, so the ONLY piece missing for a
   pointwise eps_c(r_s(r), zeta(r)) on the spin-polarised object is eps0^a(zeta) between its endpoints -- Hoffman's exact integral, unread here.
   No interpolation choice would remain: local zeta(r) = (n_up - n_dn)/n is a property of the banked object.
3. REACH: adding lam1(zeta) r_s ln r_s (closed form) is the derived way to push the series toward the 5d r_s ~ 1-3 -- the stated limitation of s21.
   The O(r_s) term is not closed (needs QMC-anchored info per Sun-Perdew-Seidl DPI); reach past r_s ~ 2 stays a stated limitation.
## Candidates for ruling (not opened): (i) evaluate eps0^a(zeta) in-project from the GB ring integrand at fixed zeta (derivation build; needs the
Hoffman/GB integrand -- fetch Hoffman via a non-paywalled route or derive from GB 1957 R0(u,zeta)); (ii) replace U/P bracket by pointwise
eps_c(r_s(r),zeta(r)) using (a),(b),(c) -- a number, no constant chosen; (iii) update B_U/B_P to the exact values (attribution refinement, ~0.001).
Attributions added: Wang & Perdew PRB 43, 8911 (1991); Onsager, Mittag & Stephen Ann. Phys. 18, 71 (1966); Misawa PR 140, A1645 (1965);
Hoffman PRB 45, 8730 (1992); Loos & Gill PRB 84, 033103 (2011); Sun, Perdew & Seidl PRB 81, 085123 (2010) (DPI, no-QMC interpolation).
No constant, no measured input.