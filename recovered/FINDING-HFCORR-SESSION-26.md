# FINDING — item (2)(a'), s26: like-for-like test of the DE_J residual with EXACT exchange. Ruling: "do the build". Files: hfcorr.py/hfcorr.jsonl (F26.2 record,
1 row), hfdscf.py, hfdscf.jsonl (15), hfdscf_table.py, TABLE-HFCORR-SESSION-26.txt, PREDICTION-HFCORR-SESSION-26.md (PB1–PB5 + amendment, each before its run).
No constant beyond c; meas RECALLED-NOT-ENTERED via TABLE-JANAK-24.
## Two corrections first. (i) Gate 13's banked TS entrant (Sc −0.2686, La −0.2017) is mode 'hfs' = Hartree-Fock-SLATER (local X-alpha, unpolarised),
NOT exact HF — my FINDING-XFOCK carried it as "HF-TS"; corrected here. (ii) F26.2 (LATENT, banked results untouched): HF/HFSR mode 'hf' at fractional
occupation carries the average-of-configuration self term (Q_a−1)Y^0 -> −0.5F^0 at Q_a=1/2 (Sc TS eps −0.553): valid at INTEGER occupation only;
every banked 'hf' use was integer. Timing flag (R 1449): the switch from TS-HF to DSCF-HF was made after seeing that number, and is so registered.
## Object: −D_HF = −[E_HF(entrant removed) − E_HF(neutral)], scalar-relativistic exact-exchange HF, average of configuration, integer occupations,
fully relaxed; plus Delta_c = <n_ent| v_c[n_u,n_d] − v_c^SIC[½ n_ent]> (the chain's own GB-Z correlation with its PZ SIC), first order on the neutral
HF orbitals; plus the chain's so/hund column. Compared with resid_TS / resid_J of TABLE-JANAK-24.
## Result 1 — on the like-for-like class (single entrant, no same-spin siblings, closed core): resid_HFc  Y +0.005 · La +0.002 · Lu +0.005 · Sc −0.008
(mean |.| 0.0050) against resid_J −0.012 · −0.009 · −0.011 · −0.044 (mean 0.019). PB3 HELD (Sc 0.008, La 0.002 <= 0.015), PB4 HELD (s/d 0.0075 vs 0.0169),
PB1 HELD. Gd (open 4f7 core, avg-of-config) +0.018 and Cs +0.012 are worse than the chain: Cs's HF removal energy is +0.012 too shallow — the
diffuse 6s where the chain's SIC-LSD is nearly exact (mask 0.0025) and HF's missing correlation is not recovered by a first-order local term.
## Result 2 — on the multi-electron open shells (Ti..Cu, 4f) avg-of-configuration HF is NOT like-for-like and fails as the caveat said: Cr +0.078,
Fe −0.077, Cu +0.061, Yb +0.093, Fe/Ni/Dy negative — the sign follows the term-average error, not the chain's. The chain's spin-polarised
SIC-LSD + derived so/hund column resolves the Hund ground term; average-of-configuration HF does not. Not evidence for or against (b) on those rows.
## Comparison verdict for item (2): on the class where the comparison is valid, (a') beats (b): the DE_J residual there IS the exchange functional's
over-binding of the entrant — SIC-LSD-Z (relaxed, DE_J) vs exact exchange (relaxed, DSCF), same correlation, no constant — and it closes to <= 0.008 Ha
on Y La Lu Sc. On 3d/4f the question stands and needs a TERM-RESOLVED (Hund ground term) exact-exchange DSCF — a build, not a check. Prediction if
opened: with the ground-term HF the 3d/4f resid_HFc falls below the chain's |resid_J| on >= 7 of 10 rows.
Failed: PB2 (Sc |Delta_c| 0.0361 vs bound 0.035, by 0.001). Held: PB1 PB3 PB4 (PB5 informational). Faults: F26.2 (latent). Not a closure.