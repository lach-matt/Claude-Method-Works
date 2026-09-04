# FINDING — T0 closure run, session 12: TFDλW gradient correction (Kirzhnits 1/9, Weizsäcker 1) on the residue set
Solver: tfdw3.py (BVP in S=ln P, ψ>0 by construction — the ground branch; μ R-independent: Ca II −0.8935 at R=10 and R=6).
tfdw.py (BVP in P) converges only to NODEFUL branches (excited TFλW solutions) — its numbers were NOT scored (fault
registered before reading). tfdw2.py (fixed-point) does not converge: 2-cycle at λ=1, spurious Numerov nodes at λ=1/9
(session-4 fault (ii) re-exposed by the 1/λ-scaled effective potential). Both kept as the record of the route.
Probe eigenvalues (Ha), delta = E(higher-ℓ) − E(lower-ℓ); measured sign: s ground at Sr/Ra II, f ground at Ce IV/Pr V.
            TFD      λ=1/9    λ=1      measured
Ca II d-s  +.045    +.050    +.010     4s ground (hold)          -> holds under both
Sr II d-s  −.002    +.008    −.014     5s ground by .07          -> 1/9 flips to measured order; λ=1 wrong way
Ra II d-s  −.002    −.006    −.005     7s ground by .055         -> both wrong way (Ra carries s-relativity, bridge-10)
Ce IV f-d  +.163    +.175    +.111     4f ground by .227         -> 1/9 wrong way; λ=1 right way, does not close
Pr V  f-d  +.003    +.016    −.102     4f ground by .524         -> 1/9 wrong way; λ=1 flips to measured order
Th IV f-d  −.044    −.027    −.064     5f ground (hold)          -> holds under both
Scored: PW1 FALSIFIED at λ=1/9 (both f-onset residues move the wrong way); PW2 half (Sr held, Ra falsified);
PW3 HELD (Ca II, Th IV); PW4 moot for 1/9, λ=1 moves f-onset the right way as stated; PW5 FAILS — no single derived λ
moves all four residues toward measurement: λ=1/9 repairs the d-onset (outer, slowly-varying region, where Kirzhnits'
expansion is valid), λ=1 repairs the f-onset (interior, where the nuclear cusp demands the full Weizsäcker term).
Reading (stated, NOT decided): the two derived λ each act where their derivation holds; the collapse-curve fault is
region-split, not one number. A single constant λ between them is NOT derivable and is excluded. Candidate as tested
(uniform λ) is RETIRED under PW5. Not a closure. Timing flag: none (predictions before solver). Chosen constants: none.
Nothing written to register/index/store. Bank 2_13 unchanged.