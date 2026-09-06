# FINDING — Route N (non-adiabatic entrant-core second order, dipole direct, chain basis) on the class rows.  s30.
# Files: PREDICTION-DROW-SESSION-30.md (adopted), drow_n.py, drow_n.jsonl. Box stated: ion HFS-SR local potential (corepol.orbitals), r in [3e-4, 300],
# regular inner condition, log mesh h 0.00588, all box states eps < 3 Ha, l <= 4 (n_b ~250 per l). Uncoupled-HFS scale inherited (He gate ~1.8x, s29): a reading
# scale, entered nowhere. F30.3/F30.3b build errors on record (box conditioning; eps_e roundoff), both caught by the box_dev / sign gate before any E2 was scored.
## Table (Ha, uncoupled). E2_closed: i over the closed core, ns2 excluded. Adiabatic closure vs s29 corepol (Sternheimer, exact a-sum).
row  eps_e(ion) E2_closed  E2_ns2   | adiab_full  corepol E_A  ratio | E2/adiab | ns2/closed | excess(P)
Cs   -0.1608    -0.0208    —        | -0.02886    -0.02985    0.967 |  0.72    |   —        |  (B)
Sc   -0.4608    -0.0304    -0.0202  | -0.21738    -0.21700    1.002 |  0.14    |  0.66      |  0.0014
Y    -0.3365    -0.0373    -0.0313  | -0.12880    -0.12964    0.994 |  0.29    |  0.84      |  0.0102
La   -0.3477    -0.0553    -0.0193  | -0.14988    -0.15087    0.993 |  0.37    |  0.35      |  0.0072
Lu   -0.3278    -0.0363    -0.0313  | -0.17220    -0.17310    0.995 |  0.21    |  0.86      |  0.0083
Convention comparison (TIMING-FLAGGED, R 1449: run after PN1 was read): eps_e = neutral eigenvalue instead of <e|h_ion|e>: Sc E2_closed -0.0344, Y -0.0421
(ns2 term inflates to -0.095/-0.151, near-degenerate valence pairs — reported, not used). The convention moves E2 by 13-15 %, not by the factor 3-10 needed.
## Predictions scored
PN0 HELD: adiabatic closure reproduces corepol on every row to <= 3.3 % (Cs) and <= 0.8 % (d rows): the box basis is complete and the operator is the chain's.
PN1 FAILED on every d row and marginally on Cs: |E2| Sc 0.030 (<= 0.003 predicted, 10x), Y 0.037, La 0.055, Lu 0.036 ([0.005,0.015] predicted, 2.5-4x),
     Cs 0.0208 ([0.008,0.020], over by 4 %). Under either eps_e convention.
PN2 FAILED: Sc/Y = 0.82 (< 0.3 predicted). The term has NO 3d/nd>=4 discrimination.
PN3 FAILED on order: La is the largest, not <= Y; Y ~ Lu within 3 % (that half held).
PN4 FAILED: E2/adiabatic on Sc 0.14 (< 0.1 predicted); the non-adiabatic denominators cut the adiabatic A by 3-7x on d rows and 1.4x on Cs, not 10x.
PN5 HELD: ns2 term >= 0.3 of closed on Y La Lu (0.84, 0.35, 0.86); reported separately, not added.
## What the numbers say
(1) The dipole entrant-core second-order term in the chain's own basis is 0.02-0.03 Ha coupled-scale on EVERY class row including Sc — the same size as
    the local form's total delivered correlation A (0.02-0.03), not the size of the residual (0.009 / 0.001). It is the object the local form is already
    representing, not the piece it leaves out. Reading it against the excess was the wrong contact; the honest statement is: the local GB form and second-order
    entrant-core correlation are the same physics at the same magnitude, and the 35 % shortfall on nd>=4 is inside that physics, not beside it.
(2) The residual's discriminator — zero at 3d, ~0.009 flat at 4d/5d/5d — is not produced by this term (Sc/Y 0.82), nor by the entrant self-SIC (Route P
    B: Sc/Y 1.81), nor by geometry (P2). Both routes fail -> SPEC rule: NEW OBJECT, stated in COMPARE-DROW.
Failed predictions this item: PN1 PN2 PN3(order) PN4. Timing flags: eps_e convention comparison (after PN1). Gate for HANDOFF-30: python3 drow_n.py 55 21 39 57 71
-> must SKIP all (epse=ion); EPSE=neu python3 drow_n.py 21 39 -> SKIP; if Cs row deleted reprints E2_closed -0.02082 adiab_closed_full -0.02886 (17 s).