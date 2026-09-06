# BRIDGE — THE LÖWDIN SESSION 36 (2026-08-17)
Successor to BRIDGE-LOWDIN-SESSION-35.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store. HANDOFF-35 verified 768/768;
gates 1-65 PASSED at open (GATES-36-OPEN.log: 53/53 exact vs pack34's GATES-33 log; 61 recomputed once under F36.1, SKIP after repair); gates 1/61/66/67 at close
(GATES-36-CLOSE.log). Census (latest-pack rule) ok=250 bad=0 open, ok=254 bad=0 close. §H.10: handoff begun at ~80 %.
## 1 · Rulings (M, s36)
(1) "Go" on the bridge-35 §3 order: PREDICTION-NLWALK -> full-table walk. GENERAL carried: SUBCELL=1; predictions before runs; R 1449 timing flags; comparison
decides; no scans; no constant; residue is not closure; T4 LAST; the n+l walk is the solution format (s35 §1(3)).
## 2 · Findings (pack36; no constant beyond c; Cs/Y RECALLED-NOT-ENTERED; PN5 record ionisation RECALLED, not entered)
(1) FINDING-NLWALK Stage 1 (t5 non-rel local; frozen HFS + relaxed E path; 25 rows, 79 entries; SIC per electron on P^2 stated):
    PN1 tie <0.08 HELD 13/17 (Sc Y Cs Ba La Lu Hf Fr Ra Ac Th Rf; Y 0.0004 .. Th 0.076), FAILED K Ca Rb Sr (0.08-0.14): the tie is a d-row / period-6-7 property.
    PN2 f-collapse: local frozen field puts (n-2)f DEEPEST on 57 58 64 89-92 96 (by 0.05-0.66) and SHALLOWEST on 55 56 87 88 -> switches on at the d onset.
    PN3 relaxation never repairs the f rows; PN4 untested by design (no s' channel); PN5 reversal on ionisation 16/22: local relaxed point puts s shallower on
    EVERY d row except Lu -> right where the record removes s (Sc Y La Ce Gd Th), wrong where it removes d (Hf Ac Rf; Pa U Cm remove 6d): ONE-SIDED, a bound.
(2) HF (SR, no corr, DSCF) on EMPTY channels (owed s35): La 4f -0.106 vs record 5d -0.206 (6s -0.172, 6p -0.138): EXACT EXCHANGE PUTS 4f SHALLOWEST at La;
    Ce 4f -0.367 vs 5d -0.246: HF fills 4f at Ce. HF reproduces the 5d/4f inversion at La->Ce (R 1307) that the local kernel collapses at La. Ac 6d -0.158;
    5f UNCONVERGED (it 100) -0.018 bound only.
(3) F36.1 (Claude, build): out-of-order pack copy; caught by gate 61 recompute, missed by any-pack census; census rule -> latest-pack. Repaired; recipe fixed.
Failed predictions s36: PN1 (K Ca Rb Sr), PN2 (55 56 87 88), PN5 (Hf Ac Rf Pa U Cm). Timing flags: none. Faults: F36.1 (closed).
## 3 · Next chat, in order (rulings first; predictions before runs) — under (6): CLOSE, do not state
(1) RULING NEEDED: the reversal on ionisation (PN5) is one-sided on the LOCAL relaxed point. Candidates: (a) run Stage 2 HF frontier pairs on Hf Ac Th Rf Pa U Cm Gd
    (25-50 s each; lwalk_hf.py needs SH rows added or hf_chan.py + swap) — comparison decides whether exact exchange ionises d first where the record does;
    (b) Stage 3 SR local walk (KH kernel; SIC per-electron vs f_orb: comparison decides). Recommended: (a) first — it is the same seam as La 4f and Lu.
(2) RULING NEEDED: with HF now reproducing La/Ce 4f onset and Lu d/s, is the walk's field HF (frozen HF + DSCF) with the local kernel demoted to a comparison
    column? (s34 exchange seam / R 1578 object seam; "the other mechanism" of bridge-35 §3(3) may be the exchange treatment itself — READ against the record first.)
(3) bridge-35 §3(3) record read (relaxation-difference, exchange seam, R 1436 handshakes, R 1439 surds, beta_nl) against TABLE-NLWALK — read, then predict.
(4) Ac 5f HF convergence (damping/maxit) before its value is used. (5) PN4 s' channels (rule extension, stated). (6) Law statement: after walk + attribution.
(7) Deferred by ruling: A/PN-3, 4f via Yb, Fe/Ni, seam nd/5d SR reference. (8) T4 writing chat LAST: R 1701-1949.
## 4 · Figures (§H.6): MEASURED none entered. RECALLED-NOT-ENTERED: Cs 0.14310, Y 0.2285 (scripts' dicts, inherited); PN5's first-ionised subshells (record, used
as the comparison target only). CHOSEN: grid/tolerance (4000 pts, tol 2e-5), qtail 1 neutral / 2 ion, SIC per electron on P^2 (stated), channel rule (stated), HF maxit 100. DERIVED: rest.
## 5 · Files (pack36): PREDICTION-NLWALK · FINDING-NLWALK · TABLE-NLWALK · FAULT-F36.1 · nlwalk.py/.jsonl · hf_chan.py/.jsonl · gates_run.sh (66-67) ·
GATES-36-{OPEN,CLOSE}.log · CENSUS-SESSION-36-{OPEN,CLOSE}.txt · README-36 · this bridge.
## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Gruneis-Kresse 2009 / Ren 2013). Owed: T4 (R 1701-1949); PR3; Z-walk (SPEC-WALK-32,
not withdrawn); PN-3; SR frozen reference; Stage 2/3 of the walk; Ac 5f. Census loop: latest-pack rule (README-36). Container: rt/ beside the packs; rt/ holds
nothing outside the packs except __pycache__, .so, gate-regenerated derive_P*.json, out/, GATES-36-*.log (packed).