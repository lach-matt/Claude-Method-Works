# ATTRIBUTION LEDGER ADDENDUM -- SECTION F: THE MATHEMATICS OF THE SWING (s93). Fetched this session, not recalled.
## F · OCCUPATION DERIVATIVES, KOOPMANS, TRANSITION STATE
F1  Baerends, E.J. (2019/2020). "On derivatives of the energy with respect to total electron number and orbital
    occupation numbers. A critique of Janak's theorem." Mol. Phys.; arXiv:1911.05651. PRIMARY (web search, abstract
    + html read). States: dE/dn_i = eps_i was first introduced by Slater for approximate total-energy expressions
    such as Hartree-Fock; the relation proves Koopmans in HF via fractional numbers; Slater's TS method gives the
    ionization energy incl. relaxation from the half-occupied orbital energy; Janak's extension to exact KS-DFT is
    argued invalid. Our field is HF: the HF statement applies, the DFT dispute does not.
F2  Slater, J.C. (1972). Transition-state method. Adv. Quantum Chem. 6:1. Known via F1. [SECONDARY]
F3  Koopmans, T. (1934). Physica 1:104. Known via F1. [SECONDARY]
F4  Janak, J.F. (1978). Phys. Rev. B 18:7165. Known via F1. [SECONDARY]
F5  Gunnarsson/Abrikosov et al. (2005). Phys. Rev. B 72:134203. Numerical validity of Slater-Janak TS in metals
    (linearity of eps in n assumed, tested). Web search, abstract only. [SECONDARY as to content]
## Term-by-term match to our objects (attribution standard, R-A extended):
##   D(c;Z,core) = E[core+c]-E[core]  <->  Slater: D = int_0^1 (dE/dq_c) dq along the stationary path (exact in HF).
##   Koopmans exact in the field (s93 item 2, K=0)  <->  F3 as proved via F1's route (fractional q).
##   "relaxation energy" Rel (s93 items 1-2)  <->  curvature of dE/dq in q: not a separate object (F1, TS section).
##   swing91 D_half  <->  Slater transition state point, computed at s91 without being named. Named here.
## Code note: rt/t7b_hf.py line 2 already declares "q fractional allowed (Slater TS)". The self-shell pair factor is
##   c_eff = Q-1 (frac=None): eps_c is NOT dE/dQ_c in this functional (the 1/2 Q(Q-1) term differentiates to Q-1/2).
##   So the exact identity must be stated in g(q) := dE/dq|_{orbitals fixed}, not in eps_c(q). Tested in item 3.