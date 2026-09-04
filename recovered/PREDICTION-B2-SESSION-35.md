# PREDICTION-B2 (s35) — candidate (b): the remainder after (a). Written BEFORE any run (R 1449). Ruled by M (bridge-34 §1(3), §3(1)).
Object: on the E path (chain LSD+PZ-SIC), same spin-averaged HFS neutral orbitals as xseam.py, six rows Sc/Y/La/Gd/Lu/Cs.
  (b1) core relaxation at DSCF: relaxed local+SIC exchange-removal of the entrant (ion SCF, same functional) minus the FROZEN Dx_LSD of xseam.jsonl.
  (b2) correlation difference between the O and E paths under ONE form S (frachf_S / janak_S rows of record; no new form).
  Remainder rem := (b1)+(b2). Target of record (FINDING-XSEAM): Delta_x - rem = -(seam O-E), i.e. rem must land at
  Sc -0.010 · Y -0.011 · La -0.011 · Gd -0.014 · Lu -0.006 · Cs +0.005 (Ha) for the seam to CLOSE as (a)+(b).
Predictions (each falsifiable; failure is a finding, not a repair):
  PB2-1  (b1) opposes Delta_x on every d row: relaxation makes the local+SIC removal SHALLOWER by 0.003-0.015 Ha (sign fixed by variational lowering of the ion).
  PB2-2  (b1) on Cs is small, |b1| <= 0.003, so the Cs remainder (+0.005) is carried by (b2), whose sign is POSITIVE on Cs and negative or ~0 on d rows.
  PB2-3  After (a)+(b): |Delta_x - rem + seam| <= 0.005 Ha on Y/La/Gd/Lu/Cs; Sc may sit outside (its T lay outside in FINDING-B) — if Sc alone fails, the seam is
         CLOSED on five rows and Sc's excess is NAMED, not absorbed.
  PB2-4  Class shape: (b1) Sc > mean(nd) by x1.5-3.0 (same ratio as Delta_x), i.e. relaxation scales with the frozen exchange, not with the seam.
Bound stated in advance: rem within x0.5-2.0 of the target row-by-row = HELD; sign wrong on any d row = FAILED on sign (R 1578 seam noted).
No constant; no measured input; frozen/relaxed pair on ONE functional; nothing entered.