# PREDICTION S94 ITEM 4 (route i-a) -- CORRELATION AS A LEVER ON THE FIVE TIGHTEST DECIDED MARGINS. Written before corr94.py exists.
## Object. Rows 38 (5s over 4d), 56 (6s over 5d), 72 (5d), 89 (6d over 7p, m=0.0323), 105 (6d over 7p, m=0.0544): the sealed entrant and the
##   sealed runner-up (rt/nlchain.jsonl order[0], order[1]). For each row and each correlation form F in {Z (GB high-density, hfc2 default),
##   R (ring, corr_ring.v_R), S (ring+screened SOX, corr_sosex.v_S)} -- all in-project, no constant, PZ-SIC as in hfc2.corr_pot -- solve the
##   three systems (ref = cfg(Z-1) at nucleus Z; ref+entrant; ref+runner) self-consistently with CORR on, and form
##   m_F = D_F(run) - D_F(ent);  Delta_m_F = m_F - m_sealed.   CORR=False reproduces the sealed row (gate C1).
## This is NOT a bound on the correlation error (position S93 §4 route (i) misnamed the SOSEX spec: it is a gas-derived functional, not a
##   second-order expansion in the field's own orbitals). It is the standing-law lever: does any in-project correlation form change a decided
##   ordering, and what is the SHAPE of its effect across the five rows. A true second-order-in-orbitals bound remains a separate build (V5).
## Rule B declarations:
C1 HYGIENE, value-exact: CORR=False reproduces sealed D_ent, D_run, m to 5e-5 Ha, 5/5.
C2 VALUE: no ordering flips: m_F > 0 for all 15 (row, form) pairs.
C3 VALUE, bound-direction UP: |Delta_m_F| <= 0.5 m_sealed on every (row, form) (correlation a minority of every margin), 15/15.
C4 SIGN: Delta_m_F > 0 at the d-entrant rows 72, 89, 105 (correlation favours the d entrant over its s/p runner: margin widens) 9/9;
   Delta_m_F < 0 at the s-entrant rows 38, 56 (correlation favours the d runner: margin narrows) 6/6.
C5 VALUE (shape/form-spread): |Delta_m_S - Delta_m_R| <= 0.3 |Delta_m_R| on every row 5/5 -- the effect is a field property, its size
   form-independent to 30%. Mechanism if C5 fails: the form dependence is as large as the effect and NO gas-derived functional can speak to
   criterion 3; only V5 (second order in orbitals) can.
C6 SHAPE (recorded, scored loosely): |Delta_m_F|/m_sealed is LARGEST at 89 (smallest margin) and the three d rows share sign and order of
   magnitude (a smooth field property, not a collapse-row jump). If instead 89 or 105 differs from 72 by >3x in |Delta_m|, correlation is
   carrying a mechanism tied to the collapse rows -- a residue pointing at an unnamed law.
## Can-fails (both at row 89, form Z, before any row is scored): A lever-dead: correlation potential and energy patched to zero on the corr
##   path -> Delta_m = 0 to 1e-6 -> rc=4.  B non-vacuity: correlation potential x10 -> |Delta_m| grows by > 3x -> rc=4.
## Bars: 5e-5 Ha floor; rung 0 required on every solve (nlguard ladder); Drep 5/5.