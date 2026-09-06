# BRIDGE — THE LÖWDIN SESSION 38 (2026-08-18)
Successor to BRIDGE-LOWDIN-SESSION-37.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store. HANDOFF-37 verified
819/819. Runtime layered in strict order 5 -> 18 -> 19..37 (F38.1: the .json data files must be layered too). Gates 1-71 at open: 70/71 BYTE-IDENTICAL
to the s37 reference; the single difference is gate 6's wall-clock field ('sec' 9 vs 8), every physics value identical. Census (census37.sh, latest-pack
rule): open ok=259 bad=0; post-gate ok=267 bad=3, the 3 being gate-1-regenerated derive_P{,2,3}.json exactly as s37. §H.10: handoff begun at ~85%.

## 1 · Rulings (M, s38)
(1) "State plainly" — the three design decisions were restated in plain terms. (2) RULING: "These can be determined by studying the other rows. Each row
has its own definable characteristics." The decisions were therefore DETERMINED BY MEASUREMENT, not chosen: (i) the arrangement is COMPUTED (Slater
diagonal-sum), the record label is a comparison column; (ii) FROZEN avg-of-config, with the frozen-relaxed bound to be measured (untested, see §3);
(iii) LS terms now, zeta per row as a separate column, because SO is itself row-differential and a live competitor. (3) "Go" — prediction filed, then run.
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 flags; comparison decides; no scans; no constant; residue is not closure; T4 LAST;
the n+l walk is the solution format.

## 2 · Findings (pack38)
(1) FINDING-TERMS. Machinery validated first: PT0 inherited, PT8 NEW (diagonal-sum closure to 1e-17; lowest terms COMPUTED d^2 3F, f^2 3H, f^3 4I,
    f^7 8S — the record's Hund terms, reproduced not assumed). PV-1, PV-2 HELD. D_d/D_s reproduce nlwalk_hf to 5 dp: the term column sits on the walk's
    own field.
(2) STRUCTURAL: gap_term - gap_avg = dE_s - dE_d. THE NEUTRAL'S TERM CANCELS OUT OF THE GAP. The s37 mechanism (neutral's Hund-I d^2) cannot
    differentiate the pair; what differentiates is the two IONS' term energies, and the s-removed ion always keeps the open shell -> every row shifts
    toward s-first, by class: A -0.0077 mean, B -0.0438, C -0.0389.
(3) THE FIRST ROW-DIFFERENTIAL OBJECT ON THE PAIR (PV-7 HELD): range 0.0052..0.0504, against class-flat exchange (+0.034+-0.007) and class-flat
    S-correlation (+0.014). Th shift -0.0387 vs Ac -0.0091 -> 0.0296 Ha differential against the 0.016 Ha residual. Th RESOLVED (+0.0083 d-first WRONG
    -> -0.0304 s-first RIGHT); Ac stays d-first (+0.0149).
(4) AND THE COMPARISON DECIDES AGAINST ADOPTING IT: HF 12/13, HF+LS-terms 9/13. Fixed Th; broke Hf, Pa, U, Cm. NOT adopted into the walk field.
    The four failures are exactly the rows where LS coupling is least valid (Hf 5d; Pa U Cm 5f) — the LS term energy is an UPPER BOUND that SO quenches.
Failed predictions s38: PV-4 (class-A direction; the neutral cancels), PV-6 (9/13 not >=12/13), PT-2 (Cm), PT-3 (Hf, and the Pa/U clause). HELD: PT-1
(Th), PV-1, PV-2, PV-7. Untested: PV-3, PV-5. Timing flags: none. Faults: F38.1 (rebuild; caught at open gates; repaired; all 71 gates re-run clean).

## 3 · Next chat, in order (rulings first; predictions before runs) — under (6): CLOSE, do not state
(1) RULING NEEDED: SO / intermediate coupling as the companion to terms — the leading candidate and the untested half of decision (iii). PV-5's
    separation test is unrun. Design: zeta per row (t7c_so; t7c_3dhund for the d column), applied against the four broken rows. The question the run
    must answer: does SO quenching restore Hf Pa U Cm to d-first WHILE LEAVING Th s-first? If yes the d/s frontier closes on terms+SO; if no, terms are
    not the residual's home and the attribution reopens. Write the prediction before touching the machinery.
(2) PV-3 frozen-vs-relaxed (decision (ii)) — untested; the frozen convention was USED but its bound is not measured. Class A gives the exact-zero test;
    the flatness test is defined in PREDICTION-TERMS-VALIDATION §2.
(3) correlation x terms (s37 item 2), now on terms+SO rather than terms alone. (4) La 4f with correlation (hf_chan lacks a CORR hook). (5) Hf/Th/Rf
    d-member frozen exchange — low priority, the seam is closed as a bound. (6) The physical law statement: after (1)-(2).
(7) Deferred by ruling: A/PN-3, 4f via Yb, Fe/Ni, seam nd/5d SR reference (Stage 3 IS an SR local reference: bridge-35 §3(4) may close on it — read).
(8) T4 writing chat LAST: R 1701-1966.

## 4 · Figures (§H.6): MEASURED none entered. RECALLED-NOT-ENTERED: record first-ionised subshells (13 rows); record ground-term labels (comparison
column, agreed with computation on every row); Cs 0.14310, Y 0.2285 (scripts' dicts, inherited). CHOSEN: grid/tolerance (4000 pts, 2e-5), qtail 1/2,
HF maxit 100, channel rule, frozen avg-of-config convention (USED, bound NOT yet measured — see §3(2)). DERIVED: rest.

## 5 · Files (pack38): PREDICTION-TERMS-VALIDATION-SESSION-38.md · FINDING-TERMS-SESSION-38.md · TABLE-TERMS-SESSION-38.txt · nlterm.py · nlterm.jsonl ·
GATES-38-OPEN.log · CENSUS-SESSION-38-{OPEN,POSTGATE}.txt · this bridge. New gate: PT8 (`python3 nlterm.py gate`) — expect lowest 3F / 3H / 4I and
dsum <= 3e-17. Gate 72 proposed: `python3 nlterm.py 21` -> SKIP (if deleted: Sc gap_avg -0.06372 gap_term -0.06891, ~15 s).

## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Gruneis-Kresse 2009 / Ren 2013). Owed: T4 (R 1701-1966); PR3; Z-walk
(SPEC-WALK-32); PN-3; La 4f+corr; PN4 s' channels; PV-3; PV-5. Container: rt/ beside the packs; rt/ holds nothing outside the packs except __pycache__,
.so, gate-regenerated derive_P*.json, out/, nlterm.jsonl (banked in pack38).
