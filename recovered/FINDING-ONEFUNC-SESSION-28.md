# FINDING — item (2), one function: the two correlation forms ARE one function E_c(f) — but only on the same orbitals; the s26/s27 0.008 gap is
# NOT the f-curvature. It is first-order orbital relaxation of E_c^SIC.   s28. Files: PREDICTION-ONEFUNC-SESSION-28.md (before any run), onefunc.py,
# onefunc.jsonl (six class rows, SUBCELL=1). No constant beyond c; no measured input; RECALLED-NOT-ENTERED unchanged. Not a closure.

## The one function, built and tested (frozen neutral exact-exchange orbitals; f = entrant weight, 0 = ion, 1 = neutral)
E_c(f) = E_c[n_c + f n_e] - f E_c^pol[f n_e]. Five points f = 0, 1/4, 1/2, 3/4, 1; analytic Janak slopes at 0, 1/2, 1.
PQ0 HELD on all six rows: E_c'(1/2) == s26 hfdscf Delta_c to <= 3e-5 (Y -0.028004/-0.02802 · Sc -0.036093/-0.03609 · Gd -0.02513/-0.02513 ·
    La -0.026273/-0.02625 · Cs -0.003163/-0.00316 · Lu -0.026669/-0.02667); the central-difference slope agrees to 2e-4. The midpoint form IS E_c'(1/2).
The integer difference ON THE SAME ORBITALS, E_c(1)-E_c(0):  Y -0.028685 · Sc -0.037161 · Gd -0.025909 · La -0.026770 · Cs -0.003153 · Lu -0.027278.
GAP := [E_c(1)-E_c(0)] - E_c'(1/2) = -0.0007 · -0.0011 · -0.0008 · -0.0005 · +0.00001 · -0.0006 Ha  (|.| < 0.0011 on every d row; ~0 on Cs).
PQ4 HELD: (1/24)E_c'''(1/2) from the five points is 0.90-1.09 of GAP on every d row (Cs 0.79 of 1e-5); the CLOSED-FORM SIC piece
    (lam0(1)/3)(ln 2 - 1/2) N_e^- = 0.00055-0.00080 Ha is 55-95% of it. The gap on one function is curvature, mostly the derived f^2 ln f law of the
    correlation-SIC (the correlation twin of the s25 f^(4/3) exchange law) — sign: the midpoint magnitude is SMALLER than the same-orbital integer,
    not larger.  PQ3 HELD: Simpson on three slopes reproduces E_c(1)-E_c(0) to 1.7e-4 (Sc 2.2e-4): the function is smooth; the integral is its slopes.
PQ2 FAILED as stated (the sign is opposite and the size is 0.001, not 0.008). PQ1 FAILED, and this is the finding:
## What the 0.008 was
hfc2's Ec_ion - Ec_neu (relaxed integer SCF): Y +0.02019 · Gd +0.01721 · Cs +0.00244 vs the SAME quantity on frozen orbitals +0.02869 · +0.02591 ·
+0.00315. Difference 0.0085 · 0.0087 · 0.0007. FINDING-HFC2's "E_HF moves < 0.0005" is true and is the reason: the exact-exchange orbitals are
STATIONARY for E_HF, so relaxation enters E_HF at second order but enters E_c^SIC — evaluated on those orbitals, not stationary there — at FIRST
order. Two evaluations of E_c on two orbital sets are not two forms of one function; they are one function on two arguments. Timing flag (R 1449):
this reading was made after PQ1 failed; the prediction file assumed relaxation <= 0.0005 for E_c and it is 0.0085. My error, on record.
## Consequence for the ruling
"Combine both into one function" is DONE for the midpoint-vs-integer question proper: on one orbital set they are the slope and the integral of
E_c(f), differing by a derived closed-form curvature of ~0.001, mostly (lam0/3)(ln2 - 1/2)N_e^-. The law's correlation term is stated once:
   I_c = E_c'(1/2) + (1/24)E_c'''(1/2) + O(E^(5))  =  E_c(1) - E_c(0)   on the entrant path,   with (1/24)E_c''' >= (lam0(1)/3)(ln2-1/2)N_e^- as its
   closed-form floor. Midpoint is "slightly better" exactly as M read it: it sits within 0.001 of the exact same-orbital integral and needs no relaxed ion.
What is NOT closed and is returned to M: whether the law's E_c is evaluated on the neutral HF orbitals (s26; margins <= 0.009) or on orbitals relaxed
under E_HF + E_c^SIC (hfc2; margins ~0.013). That is the OBJECT/OBSERVER seam of R 1578 in a new dress: the correlation functional evaluated on
orbitals it did not produce. The self-consistent fractional path — which would make BOTH orbital choices one function of f as well — cannot be built
in exact-exchange mode: F26.2, 'hf' valid at integer occupation only. So the fully combined function needs either (i) a fractional-occupation
exact-exchange kernel (a build; F26.2 lifted), or (ii) a ruling that the law's E_c is evaluated at the orbitals of the functional that defines it
(relaxed, hfc2 form) with the frozen form as its first-order approximant. Neither is a constant; both are rulings.
Failed predictions s28 item (2): PQ1, PQ2 (sign, size). Held: PQ0, PQ3, PQ4.
