# FINDING — T7C TAIL CONVENTION (candidate (c) of bridge-19 s6) — session 20, 2026-08-16
Object: scf_pol_sr TS system (entrant at 0.5, Z-0.5 electrons), floor changed from -q/r to -(q-1/2)/r (q=1). One line, source-patched (t7c_tail.py). No constant, no measured input.
Prediction (stated before run; threshold 0.005 CHOSEN): PC1 |dE_5d| < 0.005 at La/Gd/Lu; PC2 SR and nonrel move by the same amount; (c) does not close the edge.
Result (t7c_tail.jsonl):        d_sr        d_nr       banked SR   meas
  La 57 5d                    +0.0043     +0.0043      -0.2079   -0.2386
  Gd 64 5d                    +0.0048     +0.0046      -0.2097   -0.2417
  Lu 71 5d                    +0.0057     +0.0050      -0.1693   -0.1994
PC1: HELD La/Gd, FAILED Lu (0.0057 > 0.005) — recorded as a fail on magnitude. PC2: HELD (SR-nr split <= 0.0007 at all three).
Sign: the softer floor makes the 5d LESS bound (+), i.e. moves the object AWAY from measurement; the edge (object shallow by +0.026/+0.025/+0.022) would grow to ~+0.03.
Conclusion: (c) RULED OUT as a closure of the 5d edge — wrong sign, and not SR-specific (nonrel moves equally, so it is not the quantity that enters at the SR step).
Bound stated: the tail convention is worth ~0.005 Ha on the 5d TS rows, growing La->Lu; it is a convention of the object, not of the residue.
Gates: none moved (no banked file touched; t7c_pol.jsonl untouched).