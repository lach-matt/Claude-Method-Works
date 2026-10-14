# DOCKET 67 raw audit output — UNVERIFIED, NOT SEATED

This directory preserves the output of DOCKET 67 (M-D65-3, the audit of the external results the warp
board's refusals rest on) so it survives the container. **Nothing here is on the board.** No ledger row,
specthm fact or paper line cites it, and no grade here may be quoted as a finding.

**Why unverified.** Each audit was to be checked by three adversarial verifiers (refute the grade;
re-run the re-derivation; check the data claim). The runs stopped on usage limits: the session limit
on 2026-09-26 16:30 UTC, then the weekly limit, which resets 2026-10-02 06:00 UTC. At that point 412 of
431 results had an audit and only 12 verifier results had returned. Every grade below is a single
auditor's, unchecked.

**Unverified tally:** NARROWED 248, STANDS 120, OPEN 33, DATA-DEPENDENT 7, WRONG 4. Missing audits: 19 (listed in `round2_collected.json` under `missing`).

**Contents**
- `canonical.json` — the 431 external results (from 832 uses across 43 owner instruments; 165 cited-only
  results dropped), each with every owner's statement as used.
- `audits/*.json` — one audit report per result (source read, published statement and hypotheses,
  hypothesis drift against the tree with file:line, data then vs now, re-derivation, later literature,
  grade and evidence). Includes a few duplicates from the stopped earlier passes.
- `rederive/` — the re-derivation scripts (sympy / z3 / numeric) the audits ran.
- `GRADES.tsv` — one row per audited result, worst grade first.
- `round2_collected.json` — the audits as returned in the workflow journals (authoritative over `audits/`).
- `d67_audit.js`, `SHARDS.md` — the workflow script and the run log (run ids for resuming).
- `run1-partial-fable/` — the first, abandoned run's 24 audits (a different model; superseded).

**Resume.** After the reset, the 12 shard runs in `SHARDS.md` resume from their caches if the container
still holds them; otherwise the missing audits and every verifier re-run from `canonical.json`.
