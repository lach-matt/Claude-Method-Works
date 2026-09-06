# FINDING-NLWALK (s36) — the FULL-TABLE n+l walk, Stage 1 (t5 non-rel local field: frozen HFS + relaxed E path) on 25 rows, 79 channel/swap
entries (nlwalk.py/.jsonl; TABLE-NLWALK-SESSION-36.txt), plus HF (SR, no corr) DSCF on EMPTY channels of La/Ce/Ac (hf_chan.py/.jsonl, owed from s35).
Internal gate: Sc 3d D_rel -0.34175, swap4s -0.26903, Y 4d -0.25611, La 5d -0.27408, Lu 5d -0.24611 = s35 lwalk values (same code path). Al 13 dropped by rule ((N-2)d invalid).
Convention stated: SIC per electron on P^2 (s35); f_orb partition comparison NOT run (Stage 3, owed). Nothing entered; no constant; no measured input; channels enumerated.
SCORING (PREDICTION-NLWALK):
PN1 TIE (<0.08 relaxed, entrant vs nearest frontier partner): HELD 13/17 s/d rows — Sc 0.073 Y 0.0004 Cs 0.056 Ba 0.069 La 0.048 Lu 0.016 Hf 0.025 Fr 0.048
  Ra 0.059 Ac 0.043 Th 0.076 Rf 0.062 (Ce/Gd d/s: 0.039/0.020); FAILED K 0.093 Ca 0.135 Rb 0.083 Sr 0.126: the ns/(n-1)d gap is > 0.08 on the period-4/5 s rows and
  the near-tie is a property of the d rows and of periods 6-7 (Cs/Ba/Fr/Ra hold). p controls: no EMPTY partner exists (all closed) -> control VACUOUS as stated;
  measured instead: the entrant p is the shallowest removal by > 0.20 on Ga/In/Tl (4p -0.223 vs 4s -0.491), the record ionisation.
PN2 f-COLLAPSE GENERAL on the local frozen field: HELD 8 (57 58 64 89 90 91 92 96: f deepest, and by 0.05-0.66), FAILED 4 (55 56 87 88: f is the SHALLOWEST channel,
  4f -0.032 at Cs vs 6s -0.142). THE COLLAPSE BEGINS EXACTLY AT THE d ONSET (La, Ac), NOT BEFORE: with the (n-1)d electron present the local field drops (n-2)f
  below everything; without it f is a Rydberg-like channel. The magnitude grows with f occupancy: Ce 4f -0.90 frz/-0.66 rel, Gd -1.0, U -0.82, Cm -1.03.
PN3 RELAXATION DECIDES: local frozen d/s misorder against the record: Lu (5d deeper frozen; relaxed restores, s35). At Hf/Ac/Rf/Th the frozen field ALSO puts d
  deeper (Hf 5d -0.398 vs 6s -0.312) and relaxed KEEPS d deeper (-0.307 vs -0.282) -> see PN5. f-frontier: relaxed local point still prefers f on every f row
  (57 58 64 89-92 96): HELD — the local 4f/5f fault survives relaxation (relax on f channels 0.01-0.24 but never enough).
PN4 STEPS: UNTESTED BY DESIGN — channel rule has no (N+1)s; not scored (stated, no timing flag: the rule was written before the run).
PN5 REVERSAL ON IONISATION (shallower of the relaxed pair leaves first vs record, RECALLED not entered): HELD 16/22 — the 8 s rows trivially, Sc Y La Lu Ce Gd Th Lr;
  FAILED 6: Hf Ac Rf Pa U Cm. THE PATTERN IS ONE-SIDED: on the local relaxed point the outer s is the SHALLOWER member of the s/d pair on EVERY d row except Lu
  (D_rel s -0.216..-0.282 vs d -0.258..-0.324), so the walk predicts "s leaves first" everywhere; it is right wherever the record removes s (Sc Y La Ce Gd Th) and
  wrong wherever the record removes d (Hf Ac Rf; Pa U Cm remove 6d) — Lu the sole d-first row it gets, by relaxation. The named risk row Th HELD (record 6d2 7s:
  s leaves; local gives 7s shallower by 0.076). So the LOCAL FIELD HAS NO MECHANISM FOR d-FIRST IONISATION: this is the reversal M named, measured, and it is
  the same one-sidedness as the s34 exchange seam / R 1578 object seam — a bound, not closure.
HF ON EMPTY CHANNELS (SR HF DSCF, entrant added to the ion; 24-53 s each):
  La: 4f -0.106 · 6p -0.138 · (record 5d -0.206 · 6s -0.172): EXACT EXCHANGE PUTS 4f SHALLOWEST — the local 4f collapse (-0.375 rel, deepest) is REVERSED by
  0.10 in favour of 5d; the record's La 5d entrant is what HF fills. Ce: 4f -0.367 vs 5d -0.246: HF fills 4f at Ce (record: 4f entrant), by 0.12.
  So HF reproduces the 5d/4f INVERSION at the La->Ce step (R 1307's observed opening) where the local field collapses to 4f already at La.
  Ac: 6d -0.158; 5f -0.018 UNCONVERGED (it 100, maxit) — a bound only: HF 5f at Ac is shallow (Rydberg-like), 6d fills, as the record. Not entered as a value.
READING (bound): (i) the n+l tie is a d-row / period-6-7 property on the local relaxed point (13/17), not universal on the s rows of periods 4-5; (ii) the local
(n-2)f collapse switches on at the d onset and is a filling-order fault of the local kernel, absent in HF at La and correctly reversed at Ce; (iii) the local
kernel cannot ionise d before s except at Lu — the ionisation reversal is where the walk's "other mechanism" (bridge §3(3)) must be READ against the record, not here.
Failed predictions: PN1 (K Ca Rb Sr), PN2 (55 56 87 88), PN5 (Hf Ac Rf Pa U Cm). Timing flags: none (all designs pre-run). Faults: F36.1 (build order; repaired).
Owed: Stage 2 HF frontier pairs on the new rows (Hf Ac Th Rf Pa U Cm Gd: 25-50 s each); Ac 5f HF convergence; Stage 3 SR local walk + SIC-convention comparison;
PN4 s' channels. Owed to T4: R 1944 nlwalk built · R 1945 PN1 13/17, tie is d-row/period-6-7 · R 1946 f-collapse switches on at the d onset · R 1947 local
kernel one-sided on d/s ionisation (16/22, Lu sole d-first) · R 1948 HF La 4f shallowest / Ce 4f deepest: 5d/4f inversion in HF · R 1949 F36.1 census-latest rule.
Files (pack36): PREDICTION-NLWALK · nlwalk.py/.jsonl · hf_chan.py/.jsonl · TABLE-NLWALK · FAULT-F36.1 · this finding.