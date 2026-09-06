# PREDICTION — item (2)(ii): pointwise eps_c(r_s(r), zeta(r)) replaces the U/P bracket, s23. Written BEFORE the run.
Object t7c_corrz.py = t7c_corr2 (SIC_NOCLAMP=1) + corr="Z": eps_c = lam0(zeta) ln r_s + eps0a(zeta) + eps0b, lam0 = c_L/2 (Wang-Perdew closed
form), eps0a from eps0a_table.json (in-project ring integral, interpolated in x_- = (1-zeta)^{1/3}), eps0b = ln2/6 - 3 zeta(3)/(4 pi^2). Spin potential
v^sigma = eps - (r_s/3) d eps/d r_s + (1 - sigma zeta) d eps/d zeta (sigma=+1 up); d/dzeta numerical on the table (numerics stated). eps_c<=0
constraint kept as in the banked object. One-orbital SIC self-term at zeta=1 with the exact endpoint constants (same form as banked P).
Z0 = without lam1 term. 15 rows, one SCF each. Comparison against t7c_regen.jsonl (NOCLAMP base, U, P).
PZ6  On every row E_Z lies inside the regenerated bracket: E_U <= E_Z <= E_P (E_U deeper). Threshold: 15/15.
PZ7  On every row E_Z is closer to E_P than to E_U (the entrant region is strongly polarised; closed cores contribute little because eps_c<=0 cuts
     the high-density core... stated as the guess it is). Threshold: 15/15.
PZ8  resid_Z = (regenerated chain resid) + (E_Z - E_base) has smaller rms over the 15 rows than the chain resid itself; the sign is mixed
     (some rows over, some short) -- Z is a NUMBER, so containment is replaced by a signed residual. Pre-named alternative: rms does not fall.
No constant chosen; no measured input.