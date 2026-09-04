# PREDICTION — lift F26.2 and build the self-consistent fractional exact-exchange path (M, s28: "Option i"). Written BEFORE any change/run.
## F26.2 as mathematics: average-of-configuration HF gives a shell of Q electrons Q(Q-1)/2 pairs, so each electron feels (Q-1)[Y^0 - w sum c_k Y^k]
from its own shell; at Q = 1/2 this is -1/2 Y^0: a NEGATIVE self-pair. Physically the entrant is ONE spin-orbital at weight f, not a shell smeared to f.
## The lift (derived, no constant): shell a = q_c integer electrons + entrant weight f (Q = q_c + f). Pairs: q_c(q_c-1)/2 among the core + f q_c
entrant-core; a single spin-orbital has NO self-pair (HF direct = exchange for one orbital). Same average pair-exchange w c_k (a distinct-spin-orbital
pair average). With one radial function per shell, E_pair = N_pair G[P_a] and stationarity gives c_eff = 2 N_pair/Q = [q_c(q_c-1) + 2 f q_c]/(q_c+f)
in place of (Q-1), in BOTH the Fock operator and the energy. c_eff -> Q-1 at f = 0 and f = 1 (banked integer runs untouched); c_eff = 0 at q_c = 0.
Janak dE/df = eps_a holds exactly iff q_c = 0 or f = 1 (shared radial function): TRUE for every class row (Y La Lu Sc Gd Cs: entrant alone in its shell)
— so the class rows get an exact fractional path; 3d/4f rows (q_c >= 1) would need a second radial function (stated, not built here).
Correlation on the path: entrant SIC = f E_c[f n_e] and v_c^SIC[f n_e] (PZ at fractional weight), all other shells as hfc2.
## Predictions
PF0 (gate) f = 1 and f = 0 reproduce hfc2's E_HF_neu/E_HF_ion and Ec_neu/Ec_ion to 1e-5 (Y, Gd, Cs), and CORR=0 f=1/2 no longer gives the -0.553-type
    eps (Sc TS eps between the HF neutral and ion HOMO-like values, i.e. in [-0.5, -0.2]).
PF1 Janak on the self-consistent correlated path: [E(1)-E(0)] - Simpson[eps(0), eps(1/2), eps(1)] within 5e-4 on each class row run.
PF2 On this ONE path the midpoint-vs-integer gap of the CORRELATION part, [Ec(1)-Ec(0)] - Delta_c^sc(1/2) with Delta_c^sc(1/2) := eps^corr(1/2) - eps^HF(1/2)
    (two SCFs at f=1/2, with and without v_c), is <= 0.0015 (curvature order, as on the frozen path): the 0.008 lives BETWEEN the paths (orbital set),
    not within either.
PF3 -eps^corr(1/2) is within 0.002 of hfc2's obj_2 (the sc integer removal energy) on Y and Gd.
Stop rule: rows Y, Gd, Cs (hfc2 rows) first, then Sc La Lu if budget; no scan; failed predictions reported with mechanism.
