# FINDING-SUMRULES (s32 open) — the two owed gates on the chain's Lindhard function, stated, derived, and certified
Ruling (M, s31 close, executed s32 open): name eps_L as Maxwell's eps in the medium in SPEC-SOSEX; add the f-sum and compressibility sum rules as gates.
Order kept: closed-form limits DERIVED into pack32/SPEC-SOSEX-SESSION-32.md §A2 first; then evaluated (sumrule_gates.py). No timing flag.
Object: ring_zeta.g(q,nu) (BRM 2024 Eqs 12-14, imaginary axis); Pi(K,X;zeta) = (al rs/(pi K^2)) sum_sigma s g(K/s, K X/s^2) = -v chi_0; eps_L = 1 + lam Pi.
Derived (this session, from g's closed form): g(q,nu->inf) -> (2/3) q^2/nu^2 (q^4 terms cancel between log and arctan pieces); g(q->0,0) -> 2.
 G-S4 (f-sum, imaginary-axis form; zeta- and K-independent): K^2 X^2 Pi -> (2/3)(al rs/pi) sum s^3 = 4 al rs/(3 pi) = 0.442291 at rs 2, lam 1.
   Certified: nine points (K 0.5,1,2 x zeta 0,0.5,1) at X = 1e3: max |rel| 1.2e-4 (float cancellation in g at large nu; tolerance 1e-3). PASS.
 G-S5 (compressibility / Thomas-Fermi; two Fermi spheres): K^2 Pi(K,0) -> 2 al rs (x_up+x_dn)/pi = k_TF^2/k_F^2; zeta 0: 1.326873, zeta 1: 0.835878,
   ratio 2^(1/3)/2 = 0.62996 exactly. Certified to 1e-7 relative at K = 1e-3. PASS.
 Both scale linearly in lam (PASS at lam 1/2) and hold at rs 5 (PASS). Cost: < 1 s. Nothing banked; nothing in the chain changed.
What this fixes: the ring's screening object is now certified against two constant-free consequences of causality (Kramers-Kronig) BEFORE any SOSEX
line is built on it — the failure mode it closes is a mis-weighted spin split or a wrong frequency scaling in the reduction entering G-S1..3 silently.
Not gated (recorded in the spec): the INTERACTING compressibility from the ring energy vs the dressed eps's q->0 limit — RPA's known violation; to be
reported as a column of the SOSEX table under R and S, a finding not a gate.
Prior art: Maxwell 1865/1873 (D = eps E); Lindhard 1954; Kronig 1926, Kramers 1927; Thomas-Reiche-Kuhn 1925; Nozieres-Pines 1958 (both rules for eps);
Thomas 1927, Fermi 1927, Mott 1936 (TF screening); Pines-Nozieres 1966 / Mahan (RPA compressibility inconsistency). Nothing here is this work's.