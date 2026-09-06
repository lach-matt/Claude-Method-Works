# T7 BUILD SPEC (session 16) — how the next session opens the three candidates without re-deriving anything
Runtime: as README-HANDOFF-16 (rt/). Baseline columns: t5.jsonl (hfs_ts spin-averaged, dscf), t6.jsonl (ts_pol, ts_sic).
Order (Zeno; each closes before the next opens): T7c FIRST (smallest build, one kernel swap, gate is c→∞), then T7a (extend
hfs_sic: per-orbital channels for the entrant shell), then T7b (Fock builder; largest; two-value gate from Fischer 1977).
Files to write: t7c_kernel.py + t7c_run.py → t7c.jsonl; t7a_sic.py + t7a_run.py → t7a.jsonl; t7b_hf.py + t7b_run.py → t7b.jsonl;
one RUN-T7-SESSION-N.txt table with columns meas | TS_pol | T7c | T7a | T7b per species; score against PREDICTION-T7 clause by clause.
Species: Dy Er Tm Yb (4f), Fe (3d control), La Gd Lu (5d control), Sc Cu (3d control) — controls are the "must not break" clause.
Compute pattern: timeout 200 per call, ≤ 3 species per call, jsonl append with done-tracking, snapshot after each call.
Nothing to register/index/store; findings only. Bank 2_13 (R 1700).