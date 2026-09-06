# PREDICTION-TERMS (s37, item a) — WRITTEN BEFORE ANY RUN; the run is NOT made this session (handoff reserve, §H.10). Filed so the design precedes the result.
Candidate for the row-differential residual (Th s-first at HF +0.008 vs Ac d-first at +0.024; Gd -0.0002; Y +0.006 in HF+corr): the TERM energy below the
average of configuration of the neutral and of the two ions (Hund-I intra-shell d^2 / f^n, Hund-II inter-shell d-s and f-d exchange), Slater-Condon from the
record's F^k/G^k machinery (t7c_mult / t7c_3dhund; hfterm.py), on the SR HF orbitals of nlwalk_hf. Applied as: D_x(term) = D_x(avg) + [T(neu) - T(ion_x)].
Mechanism stated: where the NEUTRAL has an open d^2 (Hf Th Rf) or an f^n-d coupling (Gd Cm Pa U Ce), removing the d loses that term energy while removing
the s keeps it -> D_d deepens, gap = D_d - D_s DECREASES (toward s-first) on exactly those rows; on d^1 s^2 rows (Sc Y La Lu Ac) the neutral is a doublet
and only the s-removed ion (d^1 s^1 triplet) gains a small term -> gap INCREASES slightly (toward d-first).
PT-1  Th: gap moves from +0.008 to <= -0.010 (s-first, HELD) — the d^2 Hund-I term 0.02-0.04. Ac: gap moves +0.003..+0.008 (stays d-first).
PT-2  Gd: gap moves to <= -0.010 (s-first HELD; f7-d exchange lost on d removal). Cm: stays d-first (gap 0.046 - 0.02..0.03 > 0).
PT-3  Hf is the row at risk: gap +0.028 - (0.02..0.035) -> within +-0.01 of zero; Rf stays d-first (0.091 - 0.03). Pa/U: gap decreases by <= 0.02, stay d-first.
PT-4  Result: on HF+terms (no corr) the boundary sits at 0 within +-0.010 on 12 of 13 rows; the term correction is ROW-DIFFERENTIAL (range 0.00..0.04, not
      class-flat) — the first such term measured on the pair. Y (+0.006 HF+corr / -0.003 HF): unchanged (d^1 s^2, no term); its sign is decided by the correlation
      form question, not by terms.
PT-5  Correlation stays as measured (class-flat +0.014); its interaction with terms is not predicted (comparison decides after PT-1..4).
Design decisions to make BEFORE the run: (i) which ion terms are the ground terms (from the record's term tables, RECALLED-NOT-ENTERED, not measured energies);
(ii) SR HF orbitals of the average-of-configuration SCF (frozen for the term energy) — stated; (iii) no SO (t7c_so is a later comparison column).