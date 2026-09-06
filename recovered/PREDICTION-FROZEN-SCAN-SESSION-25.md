# PREDICTION — item (2), s25: frozen-orbital f-scan (relaxation off), reference f=1/2. Written before the run.
Design: SCF at FOCC=FENT=0.5 (mode all, corr Z, SIC_NOCLAMP=1) exactly as t7c_cuaudit; freeze all dens[c]; for f in the s24 grid
rebuild V_H, V_x, V_c(Z) and the entrant's own PZ SIC from frozen densities with entrant weight f; one numerov solve of the entrant. No SCF at f != 1/2.
PF0 (gate) eps_fr(1/2) == banked eps(1/2) to 1e-4 on Cs, Sc, Yb.
PF1 |DE_J^fr - eps(1/2)| < |DE_J - eps(1/2)| on every row run.
PF2 relaxation part DE_J - DE_J^fr:  Sc -0.006 +- 0.004 ; Yb -0.032 +- 0.008 ; Cs |.| < 0.002.
PF3 eps_fr(f) monotone increasing in f on all three; eps_fr(1) > eps_fr(1/2). (Relaxed Sc, Yb deepen at f=1; that deepening is relaxation.)
Thresholds are CHOSEN for the test only; nothing enters the law.