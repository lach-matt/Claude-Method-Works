# PREDICTION-NLWALK (s36) — the FULL-TABLE n+l walk (bridge-35 §3(1), ruled). Written BEFORE any run.
STAGING (Zeno): Stage 1 = the s35 machinery generalised (nlwalk.py: t5 NON-REL local field; frozen HFS point + relaxed E path, xseam_relax functional,
SIC per electron on P^2 — convention STATED, s35 precedent) on every frontier row; Stage 2 = HF frozen (lwalk_hf, SR Koopmans, 25 s/channel) on the
frontier pairs; Stage 3 = SR local (KH kernel) — OWED if budget ends; the SIC-convention comparison (per-electron vs f_orb partition) belongs to Stage 3.
ROWS (enumerated, not searched): s/d 19 20 21 · 37 38 39 · 55 56 57 · 87 88 89; s/f,d/f 57 58 · 64 · 71 72 · 89 90 91 92 · 96 · 103 104; p controls 13 31 49 81 (13 dropped
if 3d channel not enumerable at N=3: rule below). CHANNEL RULE per row Z with valence N = max n of ground(Z): (N,0) (N,1) (N-1,2) and (N-2,3) if N-2>=4; entrant =
the subshell where ground(Z)-ground(Z-1) = +1 (derived from ground.expand); ion = ground minus entrant; each channel c: D_frz(c), D_rel(c) as lwalk.py.
SWAP rows: every OCCUPIED frontier partner of the entrant (s,d,f among the channels) removed from the ground neutral: D_frz, D_rel.
PREDICTIONS (each can fail; bounds from s35 measured spread):
PN1 TIE: on the relaxed point, |D_rel(entrant) - D_rel(nearest frontier partner)| < 0.08 Ha on EVERY s/d frontier row (s35 max Sc 0.073); on p rows the entrant
    p is deeper than every empty partner by > 0.10 (no tie: control).
PN2 f-COLLAPSE IS GENERAL: on the local frozen field the (N-2)f channel is the DEEPEST channel on La 57 (s35), and ALSO on 56, 58, 64, 71(? — 4f full: channel is
    the 5f? no: rule gives (N-2,3)=4f, full at Lu -> add is refused/flagged) — stated: on every row where 4f/5f is EMPTY or PART-FILLED and N>=6, the local frozen
    field puts the f channel deepest (57 58 64 89 90 91 92 96 predicted; 55 56 87 88 predicted deepest as well). Named failure: any of these where s or d is deeper.
PN3 RELAXATION DECIDES (PL4 generalised): where the local frozen field misorders the entrant against a partner, the relaxed point restores the recorded entrant
    on d/s frontiers (71-type; predict also 72 104), but NOT on f frontiers (58 64 90-92 96): there the relaxed local point still prefers f — the local 4f/5f fault.
PN4 STEPS: at fixed l, s->s' 0.12-0.18 Ha on d rows; at fixed n, d->d' 0.15-0.30 — class-flat across periods 4-7 (s35 values as the bound).
PN5 REVERSAL ON IONISATION (swap rows vs entrant): the shallower of the frontier pair on the RELAXED point is the one the record removes first (recalled, not
    entered): predict this holds on Sc Y La Lu (s35) and extends to Hf(d) Ac(d) Rf(d) Ce(s) Gd(s) Ca/Sr/Ba/Ra/K/Rb/Cs/Fr(s trivially); NAMED RISK ROWS: Th (record
    Th+ = 6d2 7s: s leaves though d expected shallower on local), Lr (7p vs 7s), Pa/U (5f vs 6d/7s). Score >= 15 of ~20 predicted; a failure at Th/Lr/Pa/U is a
    finding about the local field, a failure on a d/s row is a fault in the walk.
PN6 (post-hoc slot, empty by design): the "other mechanism" is NOT to be read from these numbers until bridge §3(3)'s record read is done. R 1449: any design
    change after seeing a result gets a timing flag.
No constant; no measured input; channels enumerated; batches <= 3 rows; JSONL resume (nlwalk.jsonl key Z,tag).