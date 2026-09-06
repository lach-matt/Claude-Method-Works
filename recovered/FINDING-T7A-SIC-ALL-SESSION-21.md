# FINDING — T7a-SIC on the full row set (session 21). Files: t7a_sic_all.py, t7a_all.jsonl, RUN-T7A-SIC-ALL-SESSION-21.txt,
PREDICTION-T7A-SIC-ALL-SESSION-21.md. Object: t7a_sic.scf_sic_orb (PZ-81 orbital-resolved SIC, spin-pol TS, nonrel, tail -1/r).
Gate: Fe -0.378/-0.3854 (shift -0.0074) and Dy/Er/Tm/Yb reproduce t7a.jsonl exactly. Closes s21 (1): SIC on 5d is now RUN.
## Shifts (eps_sic - eps_pol on the half-hole entrant)
Cs 6s -0.0049 · Sc 3d -0.0257 · Ti -0.0220 · Cr -0.0002 · Fe -0.0074 · Ni -0.0013 · Cu +0.0233 · Y 4d -0.0152 ·
La/Gd/Lu 5d -0.0123/-0.0114/-0.0121 · Dy/Er/Tm/Yb 4f -0.0096/-0.0040/-0.0012/+0.0016.
## Score
PS1  Gd/Lu held; La FAILED marginally (-0.0123 vs floor -0.012); "not exceeding half of the 5d shallowness" FAILED at Lu (55 %). 5d SIC is
     UNIFORM ~-0.012 across La/Gd/Lu (spread 0.0009), i.e. it has the same Z-flatness as the 5d edge and is ~half its size.
PS2  FAILED as a class statement: Sc/Ti/Y deepen more than 5d, but Cr/Ni ~0 and Cu REVERSES (+0.023).
PS3  FAILED: Cs -0.0049 (> 0.003).
PS4  FAILED: Sc -0.026, Ti -0.022, Y -0.015 all reach the -0.015 threshold. SIC RE-OPENS as a partial owner.
## Structure read off the run (bound, not fitted): the SIC shift is ordered by CHANNEL FILLING, not by shell: up-channel entrant with
few siblings (d1/d2, 5d1) -> deepening 0.012-0.026; half-filled up-channel (Cr d5) -> 0; down-channel entrant -> small, turning
POSITIVE as the down channel fills (Fe -0.007, Ni -0.001, Cu +0.023; Dy -0.010, Er -0.004, Tm -0.001, Yb +0.002). This is the s17
mechanism (self-Hartree ~ f vs Dirac self-exchange ~ f^4/3 at f = 1/2) plus sibling relaxation, now seen across a full period, and it
is a candidate DERIVABLE structure (function of sibling count in the entrant's spin channel).
## Against the bridge-20 SHELL shallowness (comparison only; SHELL values are the pol object after Hund-II/SO where applicable):
residual = shallow + shift: Cs +0.001 · Sc -0.008 · Y +0.013 · La/Gd/Lu +0.014/+0.014/+0.010 · Fe +0.023 · Cu +0.037 · Er/Tm/Yb
+0.007/+0.015/+0.023 · Dy -0.031. SIC halves the 5d edge, closes Cs and (over-)closes Sc, leaves Y/late-3d/late-4f, and moves Cu and Dy
the WRONG way. It is a partial owner with the wrong filling-dependence to be THE owner: the SHELL shallowness is flat in filling
(La=Gd=Lu; Er<Tm<Yb rising) while SIC falls with filling and changes sign.
Faults: none. Predictions failed: PS1 (La, Lu), PS2, PS3, PS4. No constant, no measured input.