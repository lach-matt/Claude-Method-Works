# BRIDGE — THE LÖWDIN SESSION 19 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-18.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified: HANDOFF-18 297/297 (manifest sha 688112282b43c9a7). Gates 1-5 PASSED at open (derive_P3 byte-identical; probe13 exact;
t5_scf Sc/La banked; t7c H 1s -0.5000064, Z=70 -2634.8449, pol 26 -0.378; t7b He -0.91796 Ne -0.85041, hfs-switch Sc/Fe). Container clean
at open (no F18.1 artefacts; no transcripts mounted). Project knowledge read first (§H, R 1697).
## 1 · Rulings in force
M (this session): bridge-18 s3(1')(2)(3) ALL to be done, prioritised by writability -> order (1') (3) (2), all three CLOSED. T4 writing chat LAST.
Chapter 34 gated on closure. Standing preference: both objects. Handoff = single superset archive; §H.10 at 90 %.
## 2 · Findings (all no constant, no measured input; c = 137.035999 only)
(1') FINDING-T7C-SCPOL-SESSION-19.md. PP0 DERIVED then gated: bare-probe pol == SC-SR on a closed core (Vx_pol(rho/2)==Vx_unpol(rho); Ce IV -0.42268
   both). Non-vacuous object = TS on the ion (probe shell at 0.5, pol, SCF, SR): Ce IV -0.423->-0.252 (meas -0.227), Pr V -0.745->-0.553 (meas -0.524),
   Ra II +0.041->+0.070 (meas +0.055), Sr II +0.022->+0.079 (meas +0.070; nr TS alone +0.067), Th IV hold, Lr I +0.068->+0.010. PP1 HOLDS; PP2/PP3 FAIL
   (TS effect UNDER-predicted on s/d pairs; recorded as fails). All four measured residues within 0.03 Ha on one object. Sr II was an OBJECT fault
   (bare probe), not a residue; sessions 12-16 closed-negative was right for its object, wrong about the residue. R 1449: TS specification made in-session.
(3) FINDING-T7C-MULT-SESSION-19.md. meas = -(IP+E_hole) is level-to-level; t7c_pol is the max-S manifold average. Hund-II stab from OUR 4f orbital's F^k
   (F4/F2 .62, F6/F2 .45 = Racah ratios) by exact CI: dev Dy +8.6->-6.1, Er -15.1->+1.9, Tm -9.8->+2.0, Yb 0->0 %. PM1 4/4, PM2 HOLDS. The mixed-sign
   scatter IS the multiplet coordinate (R 1665 YES). (3b) SO level term on 4f NOT run (PM1 held). Flag: f3 4F/4S degeneracy structural, unverified vs tables.
(2) FINDING-T7C-SO-SESSION-19.md. First-order SO from the SR-pol TS potential (hydrogenic gate 1.00007): Lr I 7p1/2 (-0.035) / 6d3/2 (-0.017): d
   +0.010 -> -0.008, 7p<6d REACHED (PL1 HOLDS; Eliav/Sato order derived). 5d edge La/Gd/Lu shifts -.005/-.007/-.008, dev +13/13/15 -> +11/10/11 %:
   PL2 HOLDS (La borderline on magnitude), NOT closed.
STANDING AFTER SESSION 19: every corridor residue except the 5d edge has a derived owner and is within 0.03 Ha (Ce IV, Pr V, Ra II, Sr II) or in
correct order (Th IV, Lr I). 4f scatter is the multiplet coordinate. THE ONE OPEN SHELL-SYSTEMATIC: 5d edge ~0.025 Ha shallow, uniform La->Lu,
sign unchanged by exchange, SIC, relativity, TS, SO. Faults this session: none new. Predictions failed: PP2, PP3 (both under-predictions).
## 3 · Next chat, in order (candidates; each needs a ruling)
(1) 5d edge — the single obstruction to a corridor closure statement. Candidates: (a) 6s2 relaxation absent from the neutral TS (T7b dSCF within 1.2 %
    argues against); (b) tail convention -q/r at charge 1 for the TS system (test: -(q-1/2)/r, derivable, one line); (c) apply the SC-SR TS-pol object
    of (1') to the 5d NEUTRALS as ions of charge 1 with the entrant at 0.5 -- is the 5d edge an object fault like Sr II? Prediction first. Smallest first.
(2) (3b) first-order SO level term on the 4f rows for the Dy 0.017 Ha; and F^k scale (local orbital vs HF) as a uniform check. Small.
(3) Write-up candidate: "corridor residues" is now a WRITABLE unit -- one object (SC-SR-TS-pol + Hund-II + first-order SO), no constant, every
    measured residue within 0.03 Ha, both boundaries (Lr order, 4f coordinate) derived. M rules whether it goes to the writing chat before or after (1).
(4) T4 writing chat LAST: R 1701-1800 (bridge-18) + R 1801 PP0 derivation · R 1802 TS object closes Ce IV/Pr V/Ra II/Sr II · R 1803 Sr II object fault,
    s12-16 reclassified · R 1804 PP2/PP3 fails · R 1805 4f scatter = multiplet coordinate (R 1665 answered) · R 1806 Lr I order derived (SO) ·
    R 1807 5d edge sole open systematic · R 1808 f3 4F/4S degeneracy flag.
## 4 · Figures (§H.6)
MEASURED: none new entered. RECALLED-NOT-ENTERED: Racah F^k ratios (comparison only); Lr I 7p<6d order (Eliav 1995 / Sato 2015) as ORDER only;
hydrogenic zeta formula as gate. CHOSEN: none. c = 137.035999 CODATA. Prediction thresholds (0.10/0.02/0.03 Ha; 5 %; [-0.030,-0.005]; 0.005-0.015)
were stated before each run and are CHOSEN.
## 5 · Files (PACK-19): t7c_scpol.py t7c_scpol.jsonl RUN-T7C-SCPOL-SESSION-19.txt FINDING-T7C-SCPOL-SESSION-19.md t7c_mult.py t7c_mult.jsonl
RUN-T7C-MULT-SESSION-19.txt FINDING-T7C-MULT-SESSION-19.md t7c_so.py t7c_so.jsonl RUN-T7C-SO-SESSION-19.txt FINDING-T7C-SO-SESSION-19.md
BRIDGE-LOWDIN-SESSION-19.md MANIFEST-PACK-19.txt. Runtime: README-HANDOFF-19 (adds cp pack19/*.py pack19/*.jsonl rt/; sympy required for t7c_mult).
Bring next: LOWDIN-HANDOFF-19 (single superset: HANDOFF-18 + PACK-19 + README + verify19.sh) + project files.
