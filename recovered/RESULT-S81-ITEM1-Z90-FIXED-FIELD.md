# RESULT S81 — ITEM 1. THE FIXED-FIELD COMPARISON AT Z=90, WITH THE THREE REPAIRS.
# THE FIXED-FIELD ORDERING HOLDS BY 79.2 mHa. **AND THE RELAXATION TERM IS 89.9 mHa —
# LARGER THAN THE GAP IT WOULD HAVE TO ERASE.** s79's 10.1 mHa TARGET DOES NOT GENERALISE.
# Prediction sha256 ce8baedbef899a668ee30a7dd7c77989a55be3ef4dfaebf37a758dcd0b1d811a, filed first.
# Instrument pack81/fixed81.py — E1-E5 from fixed79, E6-E9 new and declared.

## THE THREE CAN-FAILS, RUN FIRST, ALL PASSED
**MACHINERY (E7's test).** The l=2 probe in the frozen field returns
**eps(6d) = -0.217248225 against the SCF's own -0.217248225 — identical to nine digits,
diff = 0.0 mHa.** At Z=89 the analogous check agreed to 1e-6 Ha; here it is exact,
because E6+E7 reproduce run2's field for shell a exactly: `_ceff(a,Q) = Q[a]-1` IS the
reduced core occupancy of E6, so the converged orbital is a FIXED POINT of the frozen
probe map. **This is the first time the same-shell exchange path has been exercised in a
frozen-core probe in this project, and it is exact.**
**SCORER.** Control 4f against 6d returns **-11185.877 mHa, ORDERING FAILS.** Both
verdicts reachable on the identical path; the verdict space is not one-sided.
**SELECTION (E8, F80.1).** Both branches run. **The fallback never fired at Z=90** —
`fine_used = 0` on every probe, so no zero set was consulted and both branches returned
**bit-identical** results. F80.1's hazard is absent at this row, and that is now measured
rather than assumed.

## THE MEASUREMENT — THREE CURRENCIES, AND THEY DO NOT AGREE IN SIGN
| currency | object | value | ordering |
|---|---|---|---|
| **TOTAL ENERGY** (the row's own) | E(cfg89+5f) − E(cfg89+6d) | **+54.009 mHa** | **6d WINS** |
| **ONE FIELD** (clause 1's object) | eps(5f in Φ_d\*) − eps(6d in Φ_d\*) | **+79.244 mHa** | **HOLDS** |
| **TWO FIELDS** (eigenvalue, each relaxed) | eps(5f in Φ_f\*) − eps(6d in Φ_d\*) | **−10.657 mHa** | **REVERSED** |
eps(6d in Φ_d\*) = **-0.217248225** · eps(5f in Φ_d\*) = **-0.138004359** ·
eps(5f in Φ_f\*) = **-0.227905042**.
E(Φ_d\*) = -26437.969287891 · E(Φ_f\*) = -26437.915278631, both restarted to stationarity.
The total-energy figure reproduces the sealed m(90) = 54.05 mHa to **0.04 mHa**, and that
difference is fully accounted for by the two E9 ladders (−0.0255 and −0.0602 mHa).
**THE ROW IS UNTOUCHED. THE ENTRANT AT Z=90 IS 6d.**

## THE RELAXATION TERM AT Z=90 — 89.901 mHa, AND IT EXCEEDS THE GAP
s79's definition, applied at a second Z: **relaxation = one-field gap − two-field gap =
79.244 − (−10.657) = 89.901 mHa**, acting to CLOSE the gap.
| Z | pair | one-field gap | relaxation | relaxation as % of gap |
|---|---|---|---|---|
| 89 | 6f vs 6d | 155.369 mHa | 10.072 mHa | **6.5%** |
| 90 | **5f vs 6d** | 79.244 mHa | **89.901 mHa** | **113%** |
**THE TERM IS 8.9 TIMES LARGER AT Z=90 THAN AT Z=89 AND THE GAP IS HALF THE SIZE.**
s79 wrote: *"a property proving the fixed-field inequality with more than 10.1 mHa to
spare would carry the full claim at this Z"* — and flagged it, correctly, as **"a
MEASUREMENT AT ONE Z, not a bound."** That flag is now discharged, and it was load-bearing:
**at Z=90 the equivalent requirement is 89.9 mHa to spare, and the measured fixed-field
gap of 79.2 mHa DOES NOT MEET IT.**
**CONSEQUENCE FOR CLAUSE 1, STATED PLAINLY: a proof of the fixed-field inequality alone
does not carry the row at Z=90.** Whatever cross-channel property of F_core is derived
must either come with a bound on the relaxation term, or be proved at the relaxed field.
**The 10.1 mHa target in ORDER-FOR-S81 item 4 is a Z=89 figure and must not be carried to
any other row.**

## WHY THE TWO-FIELD SIGN FLIP IS NOT A COUNTEREXAMPLE, AND WHAT IT IS
The ranking currency of this project is and always has been **dE, a difference of TOTAL
ENERGIES** — F79.2 is the fault that exists because the two currencies were once mixed.
The two-field eigenvalue comparison is **not the row's criterion**, and at Z=90 it
disagrees with the criterion in sign. Under CLOSE-S78 §1's splitting the residual sits in
the core term: the total-energy result and the two-field eigenvalues together place
**E_core[Φ_f\*] − E_core[Φ_d\*] ≈ +64.7 mHa** — the 5f solution's core pays 64.7 mHa for
letting 5f contract, and recovers 10.7 mHa of it in the eigenvalue.
**THAT INFERENCE IS FLAGGED, NOT ASSERTED:** this scheme's total energy is
E = ½Σq(eps + I) with a correlation potential, so E = E_core + eps holds only in the exact
closed-core RHF identity, and the Z=90 core is OPEN (6d¹). The 64.7 mHa is an
order-of-magnitude decomposition, not a measured quantity, and is not to be quoted as one.
**What IS measured is that the relaxation of the f channel at Z=90 is worth ~90 mHa in
eigenvalue currency. That is the actinide collapse appearing as a number, at the row
adjacent to the flip, and it is the largest such term the project has measured.**

## PREDICTION SCORED — V1 V2 V4 V5 V7 V8 CORRECT, V6 SPLIT, **V3 FALSIFIED**
  V1 ordering holds at fixed field, above floor . . **CORRECT**, +79.244 mHa.
  V2 gap smaller than 155.4, between 40 and 110 mHa . . **CORRECT**, 79.244. The filed
     reasoning (dE separation plus an offset of the Z=89 size) gave ~72 against 79.2.
  V3 the relaxation term is SMALLER than the gap and closes it . . **FALSIFIED ON THE
     CLAUSE THAT MATTERED.** It closes the gap — correct — and it is **89.901 mHa, 13%
     LARGER than the gap**, not smaller. **The filed rationale, "the mechanism is not
     Z-specific", IS WRONG.** It is strongly Z-specific: 10.07 at Z=89, 89.90 at Z=90.
     **This is the most consequential clause in the file and I lost it.**
  V4 fine_used = 0 for 5f . . **CORRECT** — and it was filed as *"the clause I most
     expect to lose"*. It held. **For the second session running, the clause I trusted
     least survived and the one I reasoned confidently about broke.**
  V5 both branches agree, n_zeros = 1 . . **CORRECT IN SUBSTANCE, WRONG IN MECHANISM.**
     The branches agree bit-for-bit, but not because the zero set had one member — the
     fallback never fired at all, so n_zeros was never evaluated. Scored correct on the
     verdict, and the reason is recorded as different from the one filed.
  V6 restart drop 0.01-0.10 mHa, monotone, under 12 passes . . **SPLIT.** −0.025471 mHa
     and monotone — both correct, and consistent with F80.2's 0.034493 at Z=89. **But it
     did NOT terminate under 12 passes: it exhausted the cap** at ~1e-12 Ha per pass.
     The ESTAT test of 1e-10 Ha was not met by the break condition as written.
  V7 machinery within 1 mHa . . **CORRECT, AND BY FAR MORE THAN PREDICTED** — exact to
     nine digits, diff = 0.0 mHa.
  V8 control fails by more than 5 Ha . . **CORRECT** — 11.186 Ha.

## RECORDED AGAINST THIS RESULT, NOT BURIED
1. **ONE Z, ONE PAIR, ONE FIELD, ONE RUNG, ONE SEED.** A measurement of clause 1's
   fixed-field special case at Z=90. **IT DERIVES NO PROPERTY OF F_core.**
2. **E6 IS A CHANGE OF CONSTRUCTION, NOT A PORT.** fixed79 deleted the entrant's whole
   shell; at Z=90 that would have run a 90-electron atom with 89 electrons. The
   occupancy is reduced by one instead. **At Z=89 the two are bit-identical**, so no s79
   number is disturbed. This was decided before any Z=90 run and is declared in the source.
3. **THE SAME-SHELL ASYMMETRY IS REAL AND DECLARED (E7).** The l=2 probe has a partner in
   its own shell; the l=3 probe does not. That is the scheme's convention, present in the
   sealed dE currency too. It is a candidate contributor to the gap and is not corrected.
4. **Vc = 0 FOR THE PROBE (E2)** is carried from s79 unchanged and applied identically to
   both channels. No figure here is to be compared to a sealed dE without naming it.
5. **THE E9 BREAK CONDITION IS LOOSE** (V6). The ladders are converged to ~1e-12 Ha per
   pass, so the frozen field is stationary in fact; the test simply never fired. Cosmetic,
   recorded, not repaired here.
