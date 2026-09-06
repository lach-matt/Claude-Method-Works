# BRIDGE — THE LÖWDIN SESSION 37 (2026-08-17)
Successor to BRIDGE-LOWDIN-SESSION-36.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store. HANDOFF-36 verified 786/786;
runtime layered in strict order 18..36 (F36.1 checks pass); gates 1-67 PASSED at open (GATES-37-OPEN.log = GATES-36-OPEN on all 65 comparable gates; 61 SKIP);
gates 1, 61-71 at close (GATES-37-CLOSE.log; 68-71 SKIP). Census (latest-pack rule, census37.sh) ok=255 bad=0 open; ok=267 bad=3 close (the 3 = gate-1-regenerated
derive_P*.json, as s36). §H.10: handoff begun at ~73 %.
## 1 · Rulings (M, s37)
(1) do (a) Stage 2 HF frontier pairs AND (b) Stage 3 SR local walk; comparison decides. (2) read bridge-35 §3(3), reweigh -> RULED: HF (frozen HF + DSCF, SR)
IS THE WALK'S FIELD; the SR-local kernel is the comparison column. (3) item 3 (record read + correlation on the HF field): proceed. (4)(5) held unless needed
(not needed: all HF SCFs converged; Ac 5f untouched). (6) "B then A if the handoff can be produced before 100 %": B done; A NOT run (reserve) — its prediction
is filed (PREDICTION-TERMS) so the design precedes the result. GENERAL carried: SUBCELL=1; predictions before runs; R 1449 flags; comparison decides; no scans; no
constant; residue is not closure; T4 LAST; the n+l walk is the solution format.
## 2 · Findings (pack37; no constant beyond c; Cs/Y RECALLED-NOT-ENTERED; record first-ionised subshells RECALLED, comparison column only)
(1) FINDING-STAGE23: HF (SR, no corr) separates the record's d/s classes at THRESHOLD ZERO on 12/13 rows (Th +0.008 the exception; Gd a 0.2 mHa tie); local
    Stage 1 7/13. SR-local(pe) 9/13 at zero BUT separates completely at ~0.044 (six s-first rows are the six smallest gaps): SR-local minus HF = +0.034 +- 0.007
    class-flat on n>=4, 0 at Sc. SR lifts the (n-2)f channel by 0.14-0.33 (indirect expansion): Stage 1's f collapse was a NON-REL artefact; SR-local reproduces
    the record's f onset (4f at Ce not La; 5f at Pa not Ac/Th) on all 12 f-frontier rows and agrees with HF there. f_orb SIC retired by comparison (7/13 vs 9/13).
(2) FINDING-HFCORR: S-form correlation on the HF pair: the s REMOVAL correlates MORE than the d removal on all 13 (ns^2 pair term): shift +0.004..+0.020,
    class-flat, growing with Z; HF+corr 10/13 at zero, still separated, boundary (0.027,0.035). Three fields, one class ordering, class-flat offsets
    (+0.014, +0.020). THE RESIDUAL IS ROW-DIFFERENTIAL: Th s-first at +0.008 vs Ac d-first at +0.024 (HF); no additive term measured reaches it. La/Ce 5d
    removal identical to 0.0000 (R 1436 handshake as a pair-energy identity; Th/Pa is not). beta_nl: DEc_s grows with sibling count (untested bound).
(3) FINDING-XSEAM-S: s-member frozen exchange seam -0.020..-0.030 class-flat (sd 0.003); pair frozen difference NEGATIVE (-0.002..-0.013) vs relaxed pair offset
    POSITIVE -> the pair offset is RELAXATION difference (B2's object), not frozen exchange; removed from the residual's candidate list. F37.1 (shadowing) closed.
Failed predictions s37: PH2(Th) PH4(Rf) PS1(period-7 windows) PS2(threshold clause) PS3(La 4f) PC1(sign, all 13) PC2 PC3(half) PXS-1(Sc size) PXS-2 — reasons in
the findings. Timing flags: none. Faults: F37.1 (closed).
## 3 · Next chat, in order (rulings first; predictions before runs) — under (7): CLOSE, do not state
(1) RULING NEEDED: run item (a) as filed in PREDICTION-TERMS: term energies (Hund-I d^2/f^n, Hund-II d-s/f-d) on the SR HF orbitals of nlwalk_hf, applied
    D_x(term) = D_x(avg) + [T(neu) - T(ion_x)] on the 13 rows — the ONLY row-differential candidate found; PT-1..5 stated. Design decisions (i)-(iii) in the file
    must be taken before the run. Machinery: t7c_mult / t7c_3dhund / hfterm.py (read first).
(2) then: correlation x terms interaction (comparison decides; PT-5). (3) La 4f with correlation (hf_chan lacks a CORR hook: add one, or nlwalk_hfc on an
    empty channel). (4) Hf/Th/Rf d-member frozen exchange (k=2 intra-shell term) — low priority, the seam is closed as a bound. (5) The physical law statement:
    after (1) — the walk's field is ruled, the f frontier is closed on both fields, the d/s frontier is closed to one row-differential term.
(6) Deferred by ruling: A/PN-3, 4f via Yb, Fe/Ni, seam nd/5d SR reference (Stage 3 IS an SR local reference now: bridge-35 §3(4) may close on it — read).
(7) T4 writing chat LAST: R 1701-1966.
## 4 · Figures (§H.6): MEASURED none entered. RECALLED-NOT-ENTERED: Cs 0.14310, Y 0.2285 (scripts' dicts, inherited); record first-ionised subshells (13 rows).
CHOSEN: grid/tolerance (4000 pts, 2e-5), qtail 1/2, SIC per electron on P^2 (now also DECIDED BY COMPARISON vs f_orb), HF maxit 100, channel rule. DERIVED: rest.
## 5 · Files (pack37): PREDICTION-STAGE23 · PREDICTION-HFCORR · PREDICTION-XSEAM-S · PREDICTION-TERMS · FINDING-STAGE23 · FINDING-HFCORR · FINDING-XSEAM-S ·
TABLE-STAGE2-HF · TABLE-STAGE3-SR · TABLE-HFCORR · TABLE-XSEAM-S · nlwalk_hf.py/.jsonl · nlwalk_hfc.py/.jsonl · nlwalk_sr.py/.jsonl/nlwalk_sr_gate.jsonl ·
xseam_s.py/.jsonl · gates_run.sh (68-71) · GATES-37-{OPEN,CLOSE}.log · CENSUS-SESSION-37-{OPEN,POSTGATE,CLOSE}.txt · census37.sh · README-37 · this bridge.
## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Gruneis-Kresse 2009 / Ren 2013). Owed: T4 (R 1701-1966); PR3; Z-walk (SPEC-WALK-32);
PN-3; item (a) TERMS; La 4f+corr; PN4 s' channels. Container: rt/ beside the packs; rt/ holds nothing outside the packs except __pycache__, .so, gate-regenerated
derive_P*.json, out/. Census loop: census37.sh (latest-pack rule, now a script).