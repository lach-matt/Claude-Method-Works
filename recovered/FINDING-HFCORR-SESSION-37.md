# FINDING-HFCORR (s37, item 3) — the standing correlation form (S) added to the HF walk field on the 13 d/s rows (nlwalk_hfc.py/.jsonl; TABLE-HFCORR), and the
record chain read against the three tables (Stage 2 HF, Stage 3 SR-local, HF+corr). Gate: Sc 3d DEc -0.03188 = frachf_S (same code path). All SCFs converged.
Nothing entered; no constant; no measured input; record classes RECALLED-NOT-ENTERED (comparison column). Ruling in force: HF is the walk's field (M, s37).

## Result — HF+corr 10/13; the classes STAY SEPARATED; the boundary moves AWAY from zero by a class-flat amount
DEc on the pair (Ha): d removal -0.022..-0.032 on every row; s removal -0.034..-0.044 on every row. THE s REMOVAL CORRELATES MORE THAN THE d REMOVAL, on all 13:
removing one electron of the ns^2 pair breaks the same-orbital opposite-spin pair (the largest single pair term, He-sized ~0.04); removing the single d entrant
loses only intershell correlation. So dgap = gap(HF+c) - gap(HF) = +0.004 (Sc) +0.008/0.008/0.009 (Y La Ce) +0.011..0.013 (Gd Lu Ac) +0.014/0.015 (Pa U)
+0.018..0.020 (Hf Th Cm Rf): POSITIVE on all 13, class-flat within a period and growing with Z (with the d/f sibling count present: Hf 4f14 5d2, Th 6d2, Cm 5f7, Rf 6d2).
Ordered HF+corr gaps: Sc -0.060 La -0.025 Ce -0.022 Y +0.006 Gd +0.013 Th +0.027 || Ac +0.035 Pa +0.039 U +0.042 Hf +0.046 Lu +0.062 Cm +0.065 Rf +0.112.
Separated (six s-first smallest, seven d-first largest), boundary in (0.027, 0.035); at threshold 0 it scores 10/13 (Y Gd Th wrong).
THE THREE OBJECTS ON ONE LINE: every field separates the record classes with the SAME ordering by class; only the boundary moves — HF (no corr) in (0.008, 0.024],
HF+corr in (0.027, 0.035), SR-local(pe, with S-corr) in (0.036, 0.052). Their pairwise offsets are class-flat: HF+corr - HF = +0.014 +- 0.005; SR-local - HF+corr =
+0.020 +- 0.007 (sd 0.0070, range +0.006..+0.029 on n>=4; Sc -0.004): the latter is the exchange seam PROPER, s34's Delta_x seen on the pair with the correlation
already removed from both sides. What separates the classes is the exchange (HF orbital) structure of the pair; the additive terms move the boundary and none of
them is row-differential — none can fix Th (s-first at +0.008 in HF) without also moving Ac (d-first at +0.024). Th and Ac are 16 mHa apart in HF; the record puts a
boundary between them; every additive term measured here is flat across that pair (dgap Th +0.018, Ac +0.011: it moves them APART the wrong way by 7 mHa).
PC1 FAILED ON SIGN (all 13; mechanism above — the s^2 pair term was not in the prediction; the O-path DEc used for the size, -0.026..-0.032, is the d ENTRANT's, and
the pair's s member had no record number). PC2 FAILED (Th +0.027, Gd +0.013 further from s-first). PC3 HALF: the d-first rows survive (all seven, margins
grow) — but for the wrong reason (correlation moved everything up, not down). PC4 HELD (offset +0.020, sd 0.007, ~0 at Sc — the predicted 0.015-0.025 window and
class-flatness). PC5 HELD where run (Ce 4f -0.405 deepest; Pa/U 6d shallowest, 5f between 6d and 7s; La 4f+corr not rerun — owed, hf_chan has no CORR hook).
Timing flags: none. Faults: none. Design decisions after results: none (all analyses are readings of the filed tables).

## Record read against the tables (bridge-35 §3(3), ruled item 3)
Relaxation-difference (FINDING-B2) and exchange seam (XSEAM/B2): the class-flat SR-local-minus-HF+corr offset (+0.020 +- 0.007, 0 at 3d) IS the exchange seam
on the pair; B2's "seam = -Delta_x + (relax_O - relax_E)" is the same object on the entrant alone. The pair number is smaller than XSEAM's entrant Delta_x
(0.029-0.036 nd rows) because the s member carries part of the same seam (Sc: entrant Delta_x -0.055, pair offset 0.000: at 3d the s and d members carry it
EQUALLY). Stated as a bound, not closure: the s-member Delta_x is not on the record and is the number that would close it (one xseam.py run on the s removal).
R 1436 handshakes on these rows — La/Ce: the 5d removal is IDENTICAL at La and Ce (HF -0.2059/-0.2059; HF+corr -0.2318/-0.2318) and the 6s differs by 0.003:
adding the 4f electron leaves the 5d/6s pair energy unchanged to 3 mHa — a quantitative statement of the handshake in the walk's own object (contact NAMED, not
claimed as the corridor's a_cross: R 1578 seam). Th/Pa: NOT equal (gapHF +0.008 vs +0.024; 6d^2 -> 6d^1 removal): the actinide handshake is not a pair-energy
identity, unlike La/Ce. Lr/Rf: Rf's pair gap is the largest of the table (+0.09..+0.11); Lr is a p row (not a d/s pair) — no test here.
R 1439 surds (a_cross fixed by the pair): no contact claimed; the walk gives pair ENERGIES, the corridor gives a crossing SHAPE parameter; naming both is all this
read supports. beta_nl (SIC sibling law): the growth of DEc_s with Z tracks the d/f sibling count present (Sc/Y/La/Ce ~ -0.035, Gd/Lu -0.038, Th/Cm -0.041,
Hf/Rf -0.043/-0.044) — consistent with a sibling-linear structure, UNTESTED (no fit, no constant; a bound).
Reading (bound): the walk's field question is closed by comparison (HF); the correlation form S is class-flat on the d/s pair and moves the boundary off zero;
the residual is ONE row-differential fact — Th s-first at HF +0.008 against Ac d-first at +0.024 — that no additive class-flat term reaches. The record itself
holds the two candidates for it: the term/multiplet energy of the s-removed ion (Hund-II, t7c_3dhund / t7c_mult: an ion 6d^2 7s vs 6d 7s^2 term difference is
row-specific) and the SO/Hund-II shift already in the chain (t7c_so: -0.005..-0.008 on 5d rows). Neither is designed here; both are reads for the next session.
Owed to T4: R 1957 nlwalk_hfc built, Sc gate exact · R 1958 s removal correlates more than d on all 13 (s^2 pair) · R 1959 three fields, one class ordering,
class-flat offsets +0.014/+0.020; boundary off zero · R 1960 La/Ce 5d removal identical to 0.0000: handshake as pair-energy identity; Th/Pa not · R 1961 the
residual is row-differential (Th/Ac, 16 mHa in HF) and outside every additive term measured · R 1962 PC1 sign failure: the s^2 pair term.
Files (pack37): PREDICTION-HFCORR · nlwalk_hfc.py/.jsonl · TABLE-HFCORR · this finding.
