# RESULT S95 V5 (stages a-c, ROW 89 ONLY) -- SECOND-ORDER DIFFERENTIAL CORRELATION OF THE TIGHTEST MARGIN: dm2(89) = +0.041 Ha (V^{N-1}, frozen core,
# E_cut 20 Ha, l_max 6). SIGN AS PREDICTED (P1 HELD); MAGNITUDE 1.3x THE SEALED MARGIN 0.0323 (P2, P3-as-written FALSIFIED); ORDERING UNCHANGED (6d widens).
# prediction pack95/PREDICTION-S95-V5.md sha256 959072be (hashed before v5a/v5b existed). ruling: Go (M). Rows 38 56 72 105 NOT RUN.
# instruments pack95/v5a.py (spectra; checks), pack95/v5b.py (E2; brute-force Gaunt angular sums); data v5a-*.npz (spectra), *.e2ck-*.json (per-pair E2).
## SEVERITY LINE: an ESTIMATE, not a bound (spec §5). No sealed row, gate, D1-D5 touched. Criterion 3 stays OPEN; its status moves from "not bounded"
##   to "estimated to second order at the tightest row, with the literature envelope". One row only.
## Can-fails (external numbers, outside the instrument): CF-A lever-dead (E_cut -> no virtuals: E2 = 0) rc=4 PASS. CF-B He E2 = -0.03687 Ha vs external
##   MP2 limit -0.0374 (-1.3%; l_max 4) PASS. CF-E Ne E2 = -0.3499 vs external -0.388 (-9.8%; l_max 4, E_cut 100 truncates the 1s^2 pair) PASS at the
##   estimate level. The first He run FAILED (-0.0956): F95.5 caught by it. E_cut lever (V^N, 6d pairs): -0.0266/-0.0921/-0.1055 at 1/5/20 Ha, monotone (P5 HELD).
## Verification of the spectrum operator against the sealed kernel (v5a, row 89): kinetic+SR block 5e-5 rel (floor); exchange matrix = sealed X to 4e-15;
##   shooter self-consistent 4e-7; deep-shell mass term reproduced only with the shell's OWN Vloc (sealed kernel property, Z/2c^2); valence eps
##   reproduced to ~1e-3 rel in the exchange part, residual at r<1e-3 unexplained (F95.4, open).
## Table (Ha). Entrant-core pair sums E2(c) for c = 6d (entrant) and 7p (runner-up), core = sealed cfg(88). dm2 = E2(7p) - E2(6d).
   virtual space   E_cut  E2(6d)     E2(7p)     dm2       dm2/m   5d-6d pair   5d-7p pair
   V^N (spec §2)     1   -0.02664   -0.01216   +0.0145   0.45    --           --
   V^N               5   -0.09208   -0.01623   +0.0759   2.35    -0.05374     --
   V^N              20   -0.10552   -0.01755   +0.0880   2.72    -0.06244     -0.00246
   V^{N-1} (core)   20   -0.06531   -0.02410   +0.0412   1.27    -0.00920     -0.00260   <- FILED
## Scoring
P1 SIGN HELD (89): dm2 > 0 -- the 6d entrant is stabilised more than the 7p runner-up; the margin GROWS. (Mechanism as stated; one row; the 72/105 rows unrun.)
P2 VALUE FALSIFIED: |dm2| = 0.041 > 0.03 (ledger J4c envelope). Consistent with J2: second order overshoots the all-order answer by up to 40%.
P3 FALSIFIED AS WRITTEN (|dm2| < m fails: 0.041 vs 0.032) -- but the clause's purpose (a FLIP) does not occur: the correction has the sign that widens the
   decided margin. T4's scope sentence does NOT change on this row; it gains a number.
P4 SHAPE: not scorable (one d row). Core-core relaxation column (spec 1a) NOT computed (cost; frozen core filed). P5 HELD on the V^N lever; the filed
   V^{N-1} number is at ONE E_cut (20): truncation uncertainty ~10-15% by the V^N increments (5->20: 13%).
## What is derived (estimate)
 At the chain's tightest row, second-order correlation in the field's own orbitals moves the 6d-vs-7p margin by +0.04 Ha (frozen core, V^{N-1}
 virtuals): the direction confirms the sealed ordering and the magnitude is the literature's scale (J1/J2: 0.01-0.03 all-order, second order higher).
## What is NOT derived
 A bound (spec §5). Core-core relaxation (both sides). Singles (valence singles in V^{N-1} non-zero: the AOC 6d is not an eigenfunction of the core
 operator; unquantified). E_cut/l_max completeness. Rows 38 56 72 105. The F95.4 residual.
## Faults
F95.5 SEVERITY instrument (caught by external can-fail before any row): angular m-sum omitted the m-conservation constraint and the (-1)^q phase of the
   multipole expansion; He E2 2.6x too large. Fixed from the expansion; He/Ne then pass.
F95.6 SEVERITY spec design (the main finding of the build): the spec's V^N virtual space (the field's own operator) inflates the open-shell channel's
   5d-6d pair 7x (the d virtuals carry the valence electron's own potential; model-space rearrangements also entered until the open shell's own radial
   orbital was removed from the virtual slots -- amended s95). The standard valence-MBPT V^{N-1} space (Dzuba/Johnson-Sapirstein, ledger J1b) is the
   declared V5 virtual space from here. COMPARISON DECIDED, as ruled.
## Residue after this item: none NAMED new. Criterion 3: estimate filed at one row; the estimate route is now built and costs ~5 min/row (entrant pairs).