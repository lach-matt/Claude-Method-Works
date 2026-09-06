# PREDICTION — T7a-SICDEC: SIC shift decomposed into DIRECT (entrant's own V_SIC only) and INDIRECT (siblings'/core V_SIC, relaxation).
Session 21, bridge-s21 candidate (B), ruled by M ("Continue"). Object: t7a_sic.scf_sic_orb copied with a `mode` switch
{none, ent, all}; direct = e(ent) - e(none); indirect = e(all) - e(ent). Same 15 rows. No constant, no measured input.
PB1  DIRECT is deepening on every row and ordered by entrant compactness: |direct| 4f (0.03-0.06) > 3d (0.02-0.04) > 4d/5d (0.01-0.03)
     > 6s (<= 0.01). (s17 Yb: <V_SIC> on the entrant -0.054.)
PB2  INDIRECT is positive (destabilising) and grows with the number of integer-occupied siblings in the ENTRANT's spin channel:
     ~0 for d1/5d1 up-channel rows (Sc, Y, La, Gd, Lu: no channel siblings), largest for Cu (d4 down siblings) and Yb (f6 down siblings).
     This is the filling law: shift = direct(shell) + indirect(siblings).
PB3  On 5d the shift is essentially all DIRECT: |indirect| <= 0.003 on La/Gd/Lu. Hence the 5d SIC of -0.012 is the entrant's own
     half-electron self-interaction, a shell property, and it is what the s21-OCC tail-share (0.004-0.005 on 5d) fails to remove.
Reading rule: PB2+PB3 held -> the SIC contribution to the shell finding is DERIVABLE as direct(shell) with the sibling term explaining
the sign changes; remaining flat ~0.013 on 5d/Y is then kernel (local vs exact exchange), not self-interaction -> (3) SR-HF.