# FINDING — T3b' (session 14, 2026-08-16). PARTIAL: 2 of 16 served (Gd, Lu — the 5d entrant class). Nothing written to bank.
Convention fixed BEFORE lookup: entrant shell = shell gained at the observed step (ground.py). Co,Ni 3d; La,Gd,Lu 5d (NOT 4f);
Ce,Nd–Eu,Dy–Tm 4f; Pr,Tb 4f donor steps. Hole state = M II with one entrant electron removed, all else fixed.
PB-13' (stated before lookup): flatness persists; kernels deepen; PB-11.1 keeps failing.
SERVED (Handbook _a pages, physics.nist.gov): Gd 5d E_bind = -(49601.45+3444.235)/219474.63 = -0.2417 Ha (MOW98, MZH78);
Lu 5d E_bind = -43762.50/219474.63 = -0.1994 Ha (CT72/MMMS89; hole = Lu II ground).
Kernels (T0b_pairs.json 5d): Gd TFD -0.1698 SCF -0.3645 -> measured BETWEEN (PB-11.1 Y), geo -0.2488 (2.9%), arith -0.2671 (10.5%);
Lu TFD -0.4245 SCF -0.3500 -> measured SHALLOWER than both (PB-11.1 N), geo -0.3855 (93%), arith -0.3872 (94%).
READING: the 5d entrant binding is flat and shallow (-0.24, -0.20 Ha) as 3d/4f were; SCF kernel is flat across the two (-0.36,-0.35)
while TFD 5d swings 2.5x. Same seam as session 13: eigenvalue vs hole-state difference. PB-13' HOLDS on 2 points (not decisive).
NOT SERVED (budget, §H.10): Co, Ni, La, Ce, Pr, Nd, Pm, Sm, Eu, Tb, Dy, Ho, Er, Tm — 14 species. Co II 3d6 4s2 confirmed absent from
Handbook Co II table (search snippet) -> NULL/gap; Ni likely same. Route that works: web_fetch of physics.nist.gov/PhysRefData/Handbook/
element_name_a.htm then <el>table1_a.htm (IP) + <el>table6_a.htm (levels). Handbook lists persistent levels only; La II 6s2 1S0 and
lanthanide 4f^n 6s2 terms are low and likely present. FAULTS this session: (1) I first tried www.physics.nist.gov formatted pages
(robots-blocked) and ASD energy1.pl (fetcher substituted the seen Co XX page twice) and declared the route blocked; the working route
was in the session-13 transcript — protocol "review all chats and transcripts" was applied late. Register. (2) RUN-T0A-SESSION-13.txt
named in BRIDGE-13 §5 is absent from PACK-13 and its manifest (lost artefact, R 1767 class). (3) bash egress denies physics.nist.gov.