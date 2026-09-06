# RESULT S102 ITEM 2 -- ROWS 90-A, 91-A SAME CHAIN (d101.py, prediction 56c319fc gated). Receipts
# d101-90.json, d101-91.json (pack101 receipts dir, new files; nothing sealed touched).
## SEVERITY LINE: one instrument/bookkeeping fault, latent since S101, found at first trigger (F102.5).
##   The chain itself ran clean at both rows; measurements below are fresh and internally consistent.
## F102.5 SEVERITY instrument/bookkeeping (wrong-object species, latent): d101.py SEALED[90] = -5.90e-5
##   and SEALED[91] = -4.10e-5 are ts93 T1 values -- the GAUSS-INTEGRATED defect (quad - D over the full
##   occupation interval q in [0,1]) -- while d101's R1 measures the MIDPOINT POINTWISE defect
##   (dE/dq - g at q = 0.5). Incommensurate objects; the in-window test at 90/91 is void as written.
##   Row 58's SEALED entry (+8.0e-5) is the pointwise object and reproduced (+9.01e-5, s101).
## MEASURED (fresh, valid): pointwise defect is POSITIVE at all three rows --
##   row 58 +9.01e-5 | row 90-A +3.329e-5 | row 91-A +5.774e-5; R2 - R1 = +1.6e-5 / +1.6e-5 / +2.2e-5
##   (uniform internal consistency). THE SIGN FLIP IS A PROPERTY OF THE INTEGRATED OBJECT ONLY: the
##   sealed negative values live in the [0,1] Gauss defect, not the midpoint derivative. The S102 order's
##   premise "sign flip exhibited in this chain" transfers to the integrated gauge; ruling needed on
##   which object T4 cites (both are derived quantities; comparison decides is not applicable -- they are
##   different laws, not competing conventions).
## d-SELECTIVITY (per-shell parts, additive to 2-4%): d-channel sums dominate: 90-A d=+3.71e-5 vs
##   f=+1.54e-5; 91-A d=+4.65e-5 vs f=+1.64e-5. Largest single shells are s-channel: 2s -5.6e-5 and
##   7s +2.5/+2.9e-5 -- same-l valence-pair rotation signature as row 58 (5s/6s), consistent with the
##   Item 1 overlap-Pulay finding.
## OBSERVATION (filed, not chased): 2s part = -5.6e-5 at rows 58, 90, 91 identically -- Z-insensitive
##   core term; candidate universal piece for the analytic law.
## R3 projection remains falsified at 90/91 (F101.4 confirmed out-of-row): -3.51e-4 / -4.10e-4.
