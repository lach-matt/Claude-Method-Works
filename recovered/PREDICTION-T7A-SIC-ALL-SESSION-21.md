# PREDICTION — T7a-SIC on the full row set (session 21). Closes the s21 (1) gap: SIC on 5d was never run. Ruled by M ("Continue").
Object: t7a_sic.scf_sic_orb (orbital-resolved PZ-81 SIC, spin-polarised TS, nonrel, tail -1/r), sic=False vs sic=True in the same call
chain; shift = eps_sic - eps_pol on the half-hole entrant. Rows: all 13 t5 rows + Y 4d + Cs 6s. No constant, no measured input.
Gate (before reading): Fe reproduces t6 ts_pol -0.378 (sic=False) and banked t7a -0.3854 (sic=True); Dy/Er/Tm/Yb reproduce t7a.jsonl.
PS1  On every 5d row (La/Gd/Lu) the SIC shift is DEEPENING and small: -0.012 <= shift <= -0.002 Ha. It does not exceed half of the
     5d shallowness (~0.022-0.026 after SO, bridge-20): SIC does not close 5d.
PS2  3d/4d rows deepen more than 5d (compactness): Sc/Ti/Cr/Y shifts -0.005..-0.015; |shift 3d| > |shift 5d| row-class-wise.
PS3  Cs 6s: |shift| <= 0.003 (s17 mechanism: self-Hartree ~ f, self-exchange ~ f^4/3 nearly cancel at f=1/2; diffuse s adds nothing).
PS4  No row anywhere reaches shift <= -0.015: SIC is not the owner of the shell-ordered under-binding on ANY shell (structural, s17).
Reading rule: PS4 held -> kernel self-interaction (as PZ defines it) is excluded as owner; the shallowness is in the exchange kernel
itself (local vs exact) -> (3) SR-HF entrant object is the remaining derivable candidate. PS4 failed on d rows -> SIC re-opens as a
partial owner and its magnitude ordering becomes the next audit.