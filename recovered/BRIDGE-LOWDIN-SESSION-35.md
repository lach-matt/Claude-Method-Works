# BRIDGE — THE LÖWDIN SESSION 35 (2026-08-17)
Successor to BRIDGE-LOWDIN-SESSION-34.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store. HANDOFF-34 verified 751/751;
gates 1-62 PASSED at open (GATES-34-OPEN.log: 53/53 exact vs pack34's GATES-33 log, 5/5 vs GATES-34-OPEN, gate 6 differs in 'sec' only); byte census clean at
open (CENSUS-SESSION-35-OPEN.txt ok=244 bad=0) and at close (CENSUS-SESSION-35-CLOSE.txt). §H.10: handoff begun at ~82 %.
## 1 · Rulings (M, s35)
(1) "Go" on candidate (b) (PREDICTION-B2). (2) PIVOT: from the Z-walk (SPEC-WALK-SESSION-32) to the l-WALK WITH n; "Go" on PREDICTION-LWALK.
(3) THE n+l-WALK IS THE SOLUTION FORMAT FOR THE LÖWDIN CHALLENGE — pursue it: (a) five rows/one frontier each is a STEP MECHANISM OR TRUNCATION, not a result;
walk the whole table; (b) "there is another rule or mechanism of the rule not yet identified — we have a piece of the answer already"; (c) apply the SR machinery;
(d) T4 still stands, LAST. Derivability comes AFTER the walk solution is finished and its sources attributed, then derived BACKWARDS to Schrödinger.
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 timing flags; comparison decides; no scans; no constant; residue is not closure; T4 LAST.
## 2 · Findings (pack35; no constant beyond c; Cs/Y RECALLED-NOT-ENTERED; record seam/D_tot enter comparison columns only)
(1) FINDING-B2: exchange-only relaxation of the E-path removal REFUSED on size (+0.09..+0.12, x8-12; F35.1 timing flag, redesign post-result). Total-energy
    relaxation on ONE frozen reference (t5 HFS neutral field, non-rel): seam = -Delta_x + (relax_O - relax_E) is an IDENTITY; its test chk (independent E-path
    DSCF vs record E_DSCF) = Sc +0.0016 · Cs -0.0004 (CLOSED <= 2 mHa) · Y -0.008 · La -0.024 · Gd -0.035 · Lu -0.037 (= SR shift of the removal; t5 is non-rel;
    bound). Correlation difference between paths |b2| <= 0.002 on every row: the remainder is RELAXATION. The frozen reference is load-bearing: O relaxes 0.093
    from the HFS field vs 0.069 from its own Koopmans point (Sc). PB2-1 sign held/size failed; PB2-2 failed; PB2-3 held Sc/Cs; PB2-4 failed (relaxation class-flat,
    Sc/nd 1.21); PB2-5 (post-result) failed.
(2) FINDING-LWALK: frontier pair d vs s on Sc/Y/La/Lu(/Cs), (i) frozen HFS, (ii) frozen HF (Koopmans, hfc2 SR no-corr; s partner DSCF), (iii) relaxed E path.
    Tie on (iii): Sc d deeper 0.073 · Y 0.0004 · La 0.048 · Lu s deeper 0.016; HF: 0.064 · 0.003 · 0.034 · s 0.051; frozen HFS Lu FLIPS (d deeper 0.018).
    PL1 held Y/La/Lu, failed Sc; PL2 held Sc/Y/La, failed Lu -> PL4 FIRES: Lu 5d/6s tie is NOT a local-frozen-field property; relaxation (5d 0.064 vs 6s 0.030)
    decides it; HF frozen already right. PL3 bracket held 9/10 frontier channels, failed Cs (relaxes negative on every channel). La 4f channel DEEPEST on both local
    objects (-0.375 vs 5d -0.274): the local 4f collapse as a FILLING-ORDER fault. Steps at fixed l (s->s') 0.14-0.17, at fixed n (d->d') 0.18-0.27 on d rows.
Failed predictions s35: PB2-1 (size), PB2-2, PB2-4, PB2-5, PL1 (Sc), PL2 (Lu). Timing flags: F35.1. Faults closed: none opened besides F35.1 (flag, not fault).
## 3 · Next chat, in order (rulings first; predictions before runs) — under (6): CLOSE, do not state
(1) RULED (M): THE FULL-TABLE n+l WALK. Build the walk in the SR machinery (t7c_cuaudit_S channels or an SR t5: KH kernel libshoot_sr; state the SIC energy
    convention — per-electron on P^2 (this session) vs f_orb partition — and let the comparison decide) on BOTH fields (frozen HFS/local, frozen HF) with the relaxed
    point; every frontier of the table (s/d at Z 19-21, 37-39, 55-57, 87-89; s/f and d/f at 57-58, 64, 71-72, 89-92, 96, 103-104; the p rows as controls), the
    reversal on ionisation (swap rows) included. Prediction file first (PREDICTION-NLWALK): the tie within a stated bound on every frontier on the relaxed
    point; where the local frozen field misorders (Lu-type) name the row; where HF frozen orders right, say so. This is a computation (1-3 s per channel local,
    ~25 s per HF channel): batch <=3 rows per tool call, JSONL resume.
(2) HF (ii) on the EMPTY channels of the five rows first (La 4f above all; the p channels) — owed from FINDING-LWALK; 25 s each.
(3) "The other rule/mechanism" (M): candidates ALREADY IN THE RECORD to be read against the walk, not invented: the relaxation-difference (FINDING-B2), the
    exchange-treatment seam (s34), the R 1436 handshakes and R 1439 surd family (a_cross fixed by the pair), the SIC sibling law beta_nl. Read, then predict.
(4) Seam nd/5d closure: SR frozen reference (same build as (1)) — bound stands until then. (5) A / PN-3, 4f via Yb, Fe/Ni: deferred behind the walk by ruling.
(6) Law statement / derivation backwards to Schrödinger: AFTER the walk solution and attribution. (7) T4 writing chat LAST: R 1701-1943.
## 4 · Figures (§H.6): MEASURED none entered. RECALLED-NOT-ENTERED: Cs 0.14310, Y 0.2285 (in scripts' comparison dicts, inherited). CHOSEN: grid/tolerance
(4000 pts, 1e-6/Z..300, tol 2e-5), qtail 1 neutral / 2 ion (chain precedent), SIC per electron on P^2 (energy convention, stated), channel lists (enumerated). DERIVED: rest.
## 5 · Files (pack35): PREDICTION-{B2,LWALK} · FAULT-F35.1 · FINDING-{B2,LWALK} · TABLE-{B2,LWALK}-SESSION-35.txt · xseam_relax.py/.jsonl · lwalk.py/.jsonl ·
lwalk_hf.py/.jsonl · gates_run.sh (63-65 added) · GATES-34-OPEN.log · CENSUS-SESSION-35-{OPEN,CLOSE}.txt · README-35 · this bridge.
## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Gruneis-Kresse 2009 / Ren 2013). Owed: T4 (R 1701-1943); PR3; the Z-walk test
(SPEC-WALK-32, superseded in priority by the n+l walk, not withdrawn); PN-3; SR frozen reference; HF empty channels. Census loop as bridge-33 §6. Container:
rt/ beside the packs; rt/ holds nothing outside the packs except __pycache__, .so, gate-regenerated derive_P*.json, out/, and GATES-34-OPEN.log (packed).