# CORRECTIONS — Session 27 (2026-08-16). Ruling (M, s27): "record corrections first, then proceed with the list in order."
Bank restore-point-2_13 (R 1700) UNCHANGED. Nothing written to register/index/store. These are DRAFT entries for the T4 writing chat.
Each correction names: the record as it stands (verbatim source), what supersedes it, and the evidence file. Withdrawn wording is kept, not deleted.

## C27.1  s24 record (a): "SIC-relaxation part" is a MISNOMER  [bridge-25 §2(2), owed to s24 §2(2b)]
STANDS (bridge-24 §2(2b)): "gap = universal no-SIC LSD curvature (-0.011 Sc AND Yb) + SIC-relaxation part growing with compactness (Sc -0.006, Yb -0.032)".
SUPERSEDED BY: s25 frozen-orbital f-scan (PF2 FAILED, PF6 HELD): the term is PRESENT WITH EVERY ORBITAL FROZEN — relaxation |.|<=0.0095 on all 15 rows.
  Correct name: fixed-orbital functional f-nonlinearity at the TS reference. The split is REFERENCE-DEPENDENT (PF4: Sc at ref f=1 -> +0.0656), so
  the s24 numbers are not "wrong values" but values of a misnamed quantity; the admissible statement is "at the TS reference the mask is what the
  functional does at fixed orbitals". s26 then resolves the fixed-orbital part further (C27.3).
EVIDENCE: pack25/FINDING-FROZEN-SCAN-SESSION-25.md (PF2, PF4, PF6); pack25/frozen_scan*.jsonl.  Draft entry: R 1851 (already slotted, bridge-25 §3).

## C27.2  s24 record (b): 3d class range under J with SO/Hund column  [bridge-25 §2, owed to s24 §2 test D]
STANDS (bridge-24 §2 test D): "Sc Ti Cr Fe Ni -0.036..-0.044 · Cu -0.019 (SO in)" -> class range "-0.019..-0.044".
SUPERSEDED BY: s25 3d SO/Hund column: -0.0537 (Ti) .. -0.0194 (Cu), spread 0.034 (was 0.025). NO tightening; range is "-0.019..-0.054".
EVIDENCE: pack25/TABLE-3D-SOHUND / FINDING-3D-SOHUND-SESSION-25.md; t7c_3dhund.jsonl (gate 23 Ni row).  Draft entry: R 1854 (slotted).

## C27.3  s25 record: PF8 composition of the frozen mask is MIS-ATTRIBUTED  [bridge-26 §2(1) "CORRECTION OWED"]
STANDS (pack25/FINDING-FROZEN-SCAN Result 4): "exchange-SIC f^(4/3) law 1.00 + LSD total-density exchange curvature ~+0.07-0.09 + correlation ~+0.05-0.08".
SUPERSEDED BY: s26 frozen split on 15 rows (P26.0-P26.4 HELD): M_xtot ~ 0 and M_ctot ~ 0 (|r| <= 0.013 on every row);
  the "+0.07-0.09" is M_resp = the entrant orbital's own second-order response to dV_f (r_resp +0.067..+0.117, negative in Ha on all 30 rows), NOT
  total-density exchange curvature; the "correlation +0.05-0.08" is almost purely M_csic = SIC-correlation midpoint defect (r_csic +0.050..+0.080),
  the total-density correlation part being ~0. So the s25 "1.15" = 1 + r_csic + r_resp, both derived, row-dependent, not a constant.
  Sc: r_xtot -0.001 r_ctot -0.007 r_csic +0.080 r_resp +0.100 (total 1.173).  Yb: +0.004 -0.000 +0.050 +0.067 (total 1.122; corr=None 1.071).
EVIDENCE: pack26/TABLE-FROZEN-SPLIT-SESSION-26.txt; FINDING-FROZEN-SPLIT-SESSION-26.md; frozen_split.jsonl, frozen_resp.jsonl.  Draft: R 1857 (slotted).

## C27.4  gate-13 naming: "HF-TS" entrants Sc -0.2686 / La -0.2017 are HARTREE-FOCK-SLATER, not HF  [bridge-26 §2(2)(a')]
STANDS (README-22 gate 13; pack26/FINDING-XFOCK carried them as "HF-TS"): t7c_hfsr.py mode 'hfs' = local X-alpha, unpolarised.
SUPERSEDED BY: the naming only. Values unchanged, gate 13 unchanged (rerun s27: -0.2686/-0.2017 PASS). Any comparison of an exact-exchange
  quantity against these two numbers is a comparison against HFS and must say so.  Draft: R 1860 (with F26.2 latent).

## C27.5  Older attribution corrections still owed to the writing chat (not re-derived here; carried from earlier bridges)
  - Kitagawara & Barut (1983) predates Belokolos (2017) by 34 years on period-two structure -> correction to R 1450.
  - Spectra Compendium collapse coordinate -> attribute to Schwarz 2010, J. Chem. Educ. 87, 444, Fig. 1.
  Status: owed to T4, unchanged; listed so the omission is not silent (§H.0).

## Not corrected (checked, stands): the s26 STANDING statement "not a closure"; F26.1 (design), F26.2 (latent); s26 timing flag on the DSCF switch.
