# The base-point ledger: III.I16 Theorem 3.1 by reading

*Status.* Being read (D328 onward): the five batches are with verifiers 145-149.

## What this file is

PART-III-I16-BASEPOINTS.md Theorem 3.1 states that the linear theory of III.I$'$-III.I$''''''''''''''$ and
III.J-III.J$'''$ holds at every base point whose black hole parameter is $b\in\bar{\mathcal B}_*$, with constants
uniform in $b$. Those parts are written at $b_0 = (\mu_0,0)$, five-dimensional Tangherlini. Its proof found the uses of
$b_0$ by a token search. Its finding (I$'''''''''''''''$5) says that a use the search does not see would be a gap, for
instance an argument at $b_0$ that does not name $b_0$.

This ledger replaces the search with a reading. Each batch of parts is read line by line by an independent reader. The
reader records every step whose justification uses a property of the base point that a general $b\in\bar{\mathcal B}_*$
need not have, or uses an object built at $b_0$. Implicit uses count. For each use the reader names what supplies it at
$b$:

- (P1)-(P6) of III.I16 Lemma 1.1;

- Lemma 1.2 (joint injectivity by perturbation);

- section 2 (Proposition 2.2, Lemma 2.4, Proposition 2.5: the v1 terms);

- or an item (i)-(viii) of Theorem 3.1's proof.

The reader also says whether that supply is uniform in $b$. A use that nothing supplies is a gap. Each gap is repaired
in the part it concerns, and the repair is read by the next reader.

The categories are:

- (a) staticity beyond $\partial_{t_*}$ being Killing;

- (b) the SO(4) symmetry: harmonics, types, isotypic components, Killing rotations;

- (c) explicit Tangherlini quantities, and numbers computed at $b_0$;

- (d) objects built at $b_0$: $L_{b_0}$, $g_{b_0}$, the states, towers, companions, physical states, index sets,
  corrections #1-#4 and counterterms;

- (e) derivatives in $b$ taken at $b_0$;

- (f) the joint injectivity of the states;

- (g) the v1 and rotation states;

- (h) anything else that holds at $b_0$ but not at $b$.

## Batches

| batch | parts | lines | reader | status |
|---|---|---|---|---|
| 1 | III.I$'$-III.I$'''''$ (PART-III-I2 to I6) | 1,806 | verifier 145 | read (D329); one gap, repaired, to be read |
| 2 | III.I$''''''$-III.I$'''''''''$ (PART-III-I7 to I10) | 1,814 | verifier 146 | reading |
| 3 | III.I$''''''''''$-III.I$'''''''''''''$ (PART-III-I11 to I14) | 1,718 | verifier 147 | reading |
| 4 | III.I$''''''''''''''$, III.J, III.J$'$ (PART-III-I15, J, J2) | 1,122 | verifier 148 | reading |
| 5 | III.J$''$, III.J$'''$ (PART-III-J3, J4) | 1,117 | verifier 149 | read (D329); one gap, repaired, to be read |

Theorem 3.1 is proved when every batch is read, every gap is repaired, and the repairs are read.

## Batch 1: III.I$'$-III.I$'''''$

Verifier 145 read every line (68 rows; by category a 1, b 3, c 14, d 47, e 4, f 3, g 1, h 9). One gap, major:
III.I$''''$ Lemma 2.4's boost identity is exact only at $b_0$, as it uses that $g_{b_0}$ is Ricci flat in $\mathcal C$,
so III.I$''''$ Proposition 4.1 (2), Corollary 4.3 and III.I$'''''$ Corollary 2.2 did not carry to $b$. Repaired in
III.I16 section 2.6, by Lemma 2.7 (the identity at $b$ with an error $E^S_b$, supported in $\mathcal C$ and
$O(|b-b_0|)$) and Proposition 2.8 (a direct bound). Four minor findings, seated in III.I16: Theorem 3.1's backgrounds
named correctly; the class $k_S$ at $b$; the injectivity of $S\mapsto h(S)$ by Lemma 1.2; (P4) widened, with its loss
$\delta$. Five nits seated. Report: the scratchpad file d327/ledger145.md.

| part | line | cat | property used | supplied by | uniform | note |
|---|---|---|---|---|---|---|
| I2 | 24-25 | d | L = L^{g,g0}, g0 = g_{b0,b,-S} | already at b; (P1) (III.I Props 3.3-3.4) | yes | written for general b |
| I2 | 37-41 | h | structure of L_b at scri via III.I Lemma 3.2, frame III.C Lemma 1.3; Abar constant | III.I Lemma 3.2 is stated for L_b at any b (I-CONE:148-159); Sbar, Abar b-independent ((P2); III.H'':331) | yes | (P1) does not list III.I Lemma 3.2 (n4) |
| I2 | 59, 165, 112-114, 211 | c | index sets E^C_I, E_+, E^tot_I (III.I Def 1.1, III.C) | gauge data, b-independent; T3.1 (iii) | yes | |
| I2 | 30-31, 253 | - | gauge constants e_C, v_C, gamma_C | not a base-point property | - | candidate list hit; no entry needed |
| I3 | 18-19 | d | "everything at b = b0" | T3.1 bullet 1, (P1)-(P4) | yes | |
| I3 | 24 | h | X = {r >= r0}, r0 inside the horizon | III.H'' Thm 2.1 runs III.H' on the same X for b in B1-bar ((P4)) | yes | |
| I3 | 52 | d | L_b := L_{b0}; g0 := g_{b0,b0,-S} | T3.1 bullet 1 and (i) | yes | bullet 1 names "III.I'''", see m1 |
| I3 | 54-55, 234-235 | d | Lhat_b(sigma) invertible, sigma != 0 (III.H Cor 4.4); Ltilde_b (Def 3.1, Cor 4.2) | (P4); III.H'' Thm 2.1 (iii) | yes | |
| I3 | 58-60, 455-457 | c | no indicial root of Lhat_b(0) in (0,1] (III.F' Prop 2.3 (a)) | (P2) | yes | |
| I3 | 193-195 | d | c <= c_k' (III.H Cor 4.2), c_{j,k'} (III.H Thm 4.1 (3)) | (P4) via III.H'' Thm 2.1 (i) + compactness para | yes | (P4) does not name Thm 4.1 (3) (m4) |
| I3 | 199-201 | a | Fourier transform in t_*: L_b commutes with d_{t*} | g_b stationary ((P5)'s proof, I16:71) | yes | only stationarity; no time reflection anywhere in batch |
| I3 | 199-209 | d,e | u = u_hi+u_reg+u_sing; III.H' Lemma 2.1, (4.1)-(5.2); u_sing = gdot + h_s1; G1, G2, Psi | (P4) (III.H'' Thm 2.1 reruns III.H' sections 2-7 at b); (P3) for gdot_b, h_{b,s1} | yes | gdot = d_b g at b0 not in T3.1 (iv) (n1) |
| I3 | 209-210 | d | forward map continuous (III.I Thm 5.3, h = 0, S = 0) | (P1) | yes | |
| I3 | 222-224, 259-260 | d,h | II.G' Cor 4.5 "with I.B's hypotheses for 2L_{b0}"; Sbar = 0 | (P4) (III.H'' Thm 2.1 (i)-(ii), I.B sec. 9); Sbar b-independent (III.H'' Lemma 3.2 = (P2)) | yes | |
| I3 | 254-263 | d | Lemma 4.2: III.H Cor 4.2, Thm 4.1 (3) for Ltilde_b | (P4) | yes | |
| I3 | 281-288 | c,e | gdot(bdot) in A^2 (mu-dot) / A^3 (A-dot), h(S) in A^3, hbreve in A^2 (III.H sec. 1); Psi (III.H Lemma 2.5) | (P3) (leading terms b-independent); uniformly III.H Remark 2.6 gives A^{q-delta}, absorbed by the epsilon of (4.3) (delta < epsilon) | yes | |
| I3 | 309, 329-330 | d | Prop 5.1 "at b0"; start by III.I Thm 5.3 | T3.1 bullet 1; (P1) | yes | |
| I3 | 346-352 | d | (L-L_b)u gains a_K at K+ (III.I Prop 4.1 (4.2)) | (i): L_b is the base point's operator, g0 = g_b near K+ (III.I Lemma 3.6, (P1)) | yes | |
| I3 | 354-361 | - | III.I' Prop 3.1 for L_b; II.E Prop 3.4 | general b | yes | |
| I3 | 397-402 | d | F(v) holomorphic with at most a pole at 0 (III.H' sec. 5) | (P4) (III.H'' Thm 2.1 (v)) | yes | |
| I3 | 428-437 | d | continuity in (S,h): III.I Prop 3.4, Thm 5.3 | (P1) (continuity in (b,S,h)) | yes | at fixed b only claimed |
| I4 | 20 | d | everything at b0 | T3.1 bullet 1 | yes | |
| I4 | 67-70, 81-96 | d | columns fhat_bdot, fhat_S (III.H Def 2.1, Lemmas 2.3-2.4): fhat(0) in A^3, G entire with <zeta>^{-N} bounds | III.H Remark 2.6 (uniform with delta-loss: beta_tf < 3-delta), reached via (P4) | yes (delta < epsilon) | not named in (P4) (m4) |
| I4 | 74, 178-180 | d | rows f*_j sigma-independent, compactly supported in {r<=2}; k-independent bound on c | rows are fixed tensors (normalised at b0, III.H (3.1)); B(b) invertible near b0 (H-AUGMENT:290-291), (P4) | yes | |
| I4 | 76-77 | h | Lhat_b(sigma)-Lhat_b(0) = -i sigma L1 - sigma^2 L2, L1 in rho Diff^1, L2 in rho^2 C^inf | III.F (2.2)-(2.3) normal form at any b (as in III.I Lemma 3.2); (P2) | yes | |
| I4 | 98-113 | c,e | Lemma 1.3: gdot(bdot0) in A^2, h in A^3, hbreve; Phi(0) = 1 | (P3); III.H Remark 2.6 | yes (delta < epsilon) | |
| I4 | 117-118 | b,d | h(S) = h_{b0,s1}(S); h^{<=1} = t_* h + hbreve, the s1 generalised state | (P3) (companions at b) | yes | "s1" is a continued label at rotating b |
| I4 | 128-129 | f | S -> h(S) injective (III.F''' Prop 4.1 (1), proved at b0 by symmetry) | Lemma 1.2 (tau = s1 alone; c > 0 independent of b) | yes | absent from T3.1 (v) (m3) |
| I4 | 135-137 | d | (L-L_b)u gains a_K | (i), (P1) | yes | |
| I4 | 172-177 | c,d | Ltilde_b(0)^{-1} (III.H Prop 3.2) at weight alpha#-3 in the gap | (P4): III.H'' Thm 2.1 compactness para (Prop 3.2 invertible, uniform inverse); (P2) gap | yes | (P4) does not name Prop 3.2 (m4) |
| I4 | 209-218 | d,e | III.I'' (4.1), Lemma 4.3; zf-coefficients gdot(bdot0), h(S0) | (P3), (P4) | yes | |
| I4 | 242-256 | d | u_{K+} = h(S0); h^aug(S) = chi_K h^{<=1}(S) (III.H Def 2.1); G2(0) = h | (P3), (P4) | yes | |
| I5 | 20 | d | everything at b0 | T3.1 bullet 1 | yes | |
| I5 | 36-45 | d | Theta, V(S), w(S) := g_{b0}(X_S,.) | by design b0 at b: outside part of g_{b0,b,-S} is phi*_{-S} g_{b0} (III.I (1.1)); (P6) | yes | |
| I5 | 40-41 | d | g_S := g_{b0,b0,-S} | T3.1 bullet 1 | yes | bullet says "III.I'''": it is here (m1) |
| I5 | 58-61 | h | (iii) Ric(g) = 0 => D_g Ric o delta*_g = 0, for g_{b0} | at b holds on U_I (outside part Ricci flat); fails in C for G := g_{b0,b,0} | - | feeds Lemma 2.4, see M1 |
| I5 | 63-75 | b,c,d | omega_{b0,s1}, omegabreve at b0 (III.D'' Prop 3.1); E_ind; tbar = t+C'-8 mu0 |x|^{-1}; g_{b0}-eta in |x|^{-2}C^inf | (P6) (correction #1 is built at b0); (P3) (E_ind b-independent) | yes | |
| I5 | 77-78 | d | re-centred state h^{<=1}_nat at b0 | as correction ingredient (P6); as the leading term of Prop 4.1 (1) at b: h^{<=1}_{b,nat} (P3), any constant (Lemma 1.2 (b) is constant-agnostic) | yes | statement at b should say which (M1 repair) |
| I5 | 80-90 | c | Lemma 1.2 (a): explicit -8 mu0 |x|^{-1} | b0 object, used only for correction #1 ((P6)) | yes | |
| I5 | 92-102 | c | Lemma 1.2 (b): h^{<=1} in A^{(2,0) u (2+E_ind)} | (P3) | yes | |
| I5 | 106-115 | d | corrections h^(-1), theta^(-1), theta_# built from g_{b0}, omega_{b0} | (P6) (I16:93 names III.I'''') | yes | (P6)'s citation omits this Def 2.1 (n3) |
| I5 | 117-143 | d | Lemma 2.2: holds for every g0 with g0-eta in rho_+ C^inf | g_{b0,b,-S} qualifies (III.I Lemma 3.6, (P1)) | yes | |
| I5 | 149-154 | d,h | L_{h,S} := D_h P1(.,S,b0); P1(0,0,b0) = 0 | at b: D_h P1(.,S,b); P1(0,0,b) != 0 (G not Ricci flat in C), unused by the linear theory | yes | n5 |
| I5 | 158-182 | d,h | Lemma 2.4: D_S P1(0,S,b0)|_{S=0} = L_{b0}(chi_K h^{<=1}_nat) EXACTLY: Ric(g_{b0}) = 0 in C; h^{<=1}_nat in ker D_{g_b0}Ric and ker delta G at b0; same b0-object in correction and leading term | only the remark I16:93-95 (no lemma); (P6)'s E^nu is for rows nu, not the S-column; not in the census | **GAP** | M1 |
| I5 | 188-202 | c,d | (2.4) with E_ind "at b0, fixed once"; L_{h,S} = L^{g',g0} = III.I Thm 5.3's operator | (P3); (P1) | yes | |
| I5 | 209-213, 223-236 | d | k_S := g_S - g_{b0} in K; L^{g,g0}-L_{b0} via differences from g_{b0}; Ldot = 0 near K+ "as g_S = g_{b0} there" | at b: k_S := g_{b0,b,-S} - g_b in K (III.I Lemma 3.6 at b, (P1)); differences from g_b ((i)); k' and Ldot unchanged, vanish near K+ (g_{b0,b,-S} = g_b there) | yes | g_{b0,b,-S}-g_{b0} itself is NOT in K at b (m2) |
| I5 | 230-232 | d | scri leading part + "C^inf error of L_{b0}" | (i); III.I Lemma 3.2 at b | yes | |
| I5 | 248, 383 | d | f_{0,0}(S') = L_{b0}(chi_K h^{<=1}_nat(S')), supported in C | support in C holds at b (f = 0 on U_K and on U_I at h = 0); the identity does not | GAP | M1 |
| I5 | 261-264 | d,h | U_K: g0 = g_{b0}; U_I: phi*g_{b0} Ricci flat | U_K: g0 = g_b, S-independent, f = 0; U_I: outside part phi*_{-S}g_{b0} (III.I (1.1)) | yes | |
| I5 | 273-299 | d | U_iota count: g0-eta in rho_+^2; differences g'-g_{b0}, g0-g_{b0} in H^{k,(E_+,a_+)} | g0-g_{b0} = chi_K(g_b-g_{b0}) in rho_+^2 C^inf in A^{(2,0)}, (2,0) in E_+ (III.I Lemma 3.6, (P1)) | yes | |
| I5 | 340-345 | f | Prop 4.1 (1): S -> h(S) injective | Lemma 1.2 | yes | m3 |
| I5 | 352-381 | d | Lemma 4.2: Pi "depends on L_{b0} only"; f' = f-(L-L_{b0})u; III.I' Prop 3.1 for L_{b0}; Ltilde_{b0}(0)^{-1} | at b: Pi_b from L_b ((i)), III.H Prop 3.2 at b ((P4)); (a) uniform; (b) continuity at fixed b only | (a) yes; (b) fixed b | (b) is not in I16:399-400's list of fixed-b continuity statements |
| I5 | 383-391 | d,h | Prop 4.1 (2): S^(-1)_{0,0} = id (Lemma 2.4), smallness by Lemma 4.2 (b) continuity | nothing at b: S^(-1)_{0,0;b} = id + Sdot_b(E^S_b); continuity across b not available | **GAP** (not uniform as written) | M1 |
| I5 | 393-401 | d | Cor 4.3: (S^(-1))^{-1} | inherits M1 | GAP | |
| I5 | 412-416, 438-441 | c,d | findings: mu0, C', "Pi fixed by L_{b0}" | commentary | - | |
| I6 | 17, 22-26 | d | everything at b0; L := D P1 at (h,S,b0); h^{<=1}_nat of III.I'''' | T3.1 bullet 1; (P6) | yes | |
| I6 | 24 | c | E_ind in (1.1) | (P3) | yes | |
| I6 | 12-14, 131, 252 | c | spec_iota+(Lbar) in {Re >= 2} (III.G' Lemma 4.2 (a)); no indicial root in (0,1] | (P2) | yes | |
| I6 | 37-51 | c | eigencomponents Pi_s of Sbar, Abar lower triangular | Sbar b-independent ((P2), III.H'' Lemma 3.2) | yes | |
| I6 | 81-83 | d | start: III.I'''' Prop 4.1 (1) with Sdot(f) = 0 | III.I'''' Prop 4.1 (1) at b (Sdot_b) | yes | |
| I6 | 85-101 | d | (L-L_b)u gains a_K | (i), (P1) | yes | |
| I6 | 92-97, 118-125 | c | E^iota_ind (III.G'' (4.4)); roots mu of III.G'' sec. 1; Re pi_1 E_K exclusions; l_K^max | (P2) (roots, index sets b-independent): the finite exclusion set, hence c_K, is the same for all b | yes | |
| I6 | 129-131 | d | III.G'' Cor 4.3 | (P2) (stated for general b, K+ towers of L_b) | yes | |
| I6 | 146-151 | b,g | E^gr_K(lambda0): a_s1 ~ t^{-lambda0+1}, a_v1 ~ t^{-lambda0}; S^(-1)_1 = 0 | absence by (P2) (u_+ and W b-independent); if present, the v1 term has bottom a_nu h_{b,v1}, K+-weight Re lambda0 - epsilon (Lemma 2.1) >= Re lambda0 - 1, so the bound used survives | yes | not in T3.1 (vi) (n2) |
| I6 | 179-203 | d | Step 3 = III.I''' Steps 2-3 at b; III.H Prop 3.2 | (P4) | yes | |
| I6 | 209-212 | f | S0 = 0 from injectivity (III.F''' Prop 4.1 (1)) | Lemma 1.2 | yes | m3 |
| I6 | 69-75 | d | Cor 2.2 uses (S^(-1))^{-1} of III.I'''' Cor 4.3 | inherits M1 | GAP | |
| I6 | 225-227 | d | continuity: III.G'' Cor 4.3 | (P2) | yes | |

## Batch 5: III.J$''$, III.J$'''$

Verifier 149 read every line (51 rows; by category a 1, b 1, c 9, d 27, e 4, f 7, g 12, h 18). One gap, minor:
III.J$'''$ Theorem 5.3, on which Corollary 6.6 rests, was not stated at $b$. Repaired in III.I16: Theorem 3.1 lists
III.J$'''$ Propositions 3.4, 4.3, 4.6, 5.2, 5.4 and Theorems 5.3, 5.5, Theorem 5.3 in the form of Proposition 2.5 at the
exact weights, and (viii) gives the reasons ($E^\nu$ exact by room and (E1), $A_b$ independent of the loss, room for the
rotation rows' errors). Minor: the loss at every order at $b$ is III.H$''$ Proposition 1.1, now cited in (P4) and
(viii), and (J$''$2) is marked superseded. Five nits seated. Report: the scratchpad file d327/ledger149.md.

| part | line | cat | property used | supplied by | uniform | note |
|---|---|---|---|---|---|---|
| J'' | 5-6, 29 | h | "at b_0" / "Throughout b = b_0" sets the whole part | (viii) | yes | scope line only |
| J'' | 12-13, 340 | h | "(J'3) open" | I16 status line 12 | - | stale; see n3 |
| J'' | 21-23 | h | strong trapping admissibility at b_0 (III.F Prop 4.1) gives (k+1)δ_Γ≤1 for every k | not named in I16; actually supplied by III.H'' Prop 1.1 and H3:158-170 (and (P4) via III.H'' Thm 2.1) | yes (H3:82 "C independent of η and b"; β_0, Q, ν_min continuous and positive on the compact B̄_1, H3:164) | m1 |
| J'' | 30-31 | d | P enlarged by the rotation rows (III.I^14 §1) | §2 (Def 2.3, Lemma 2.1) | yes | |
| J'' | 102-107 | d | L_{h,S}, L_{h,p}: background g_S = g_{b0,b0,-S}; ϑ_tot built from b_0 corrections | Thm 3.1 bullet 1 (g_{b0,b,-S}); (P6) | yes | |
| J'' | 108-113 | d | g_0 (g_S, g_p) smooth in p; III.I Thm 5.3 proof | (P1) | yes | |
| J'' | 115 | d | (L^{g,g0} − L_{b_0})u as BG family | (i): L_{h,p} − L_b, same K^+ gain | yes | |
| J'' | 115-118 | e | f^b_{h,p} (b-column), f^S, f^{s1}, f^ν, r^ν, L_b h_rem(q) | (iv) \dot g_b; (P6) (1.1); Lemma 2.1 | yes | E^ν(W) is a new BG/FIN term at b; (viii) adds it |
| J'' | 124-125 | d,e | (S^(-1)_{h,S})^{-1}, (S^(-1)_{h,p})^{-1} (III.I^7 Cor 4.6, derivative at b_0) | Thm 3.1 bullet 1; (iv) | yes | |
| J'' | 126-127 | d,g | (−id+A_k)^{-1} and inverse of C^rot in W'^rot (Steps 3, 4') | Prop 2.5 Step 3 (direct bound); (v): Step 4' not used at b; A_b finite rank (Def 2.3) | yes | |
| J'' | 128-130 | f | coefficient functionals S_ν, C^{k+1}_ν, dual functionals of Step 4' | Lemma 1.2 (Cor 2.3 at b); Lemma 2.4; Def 2.3 | yes | |
| J'' | 131-133 | d | rows m_ν, towers T_{ρ,b_0}, states: "fixed smooth sections" | (P3), (P6): T_{ρ,b} smooth in b, so bounded at each order uniformly on B̄_* | yes | under Lemma 1.2(c), "fixed" becomes "uniformly bounded", which suffices |
| J'' | 134-137 | g | conormal components incl. Y_{v1} | §2, Prop 2.2(c) | yes | |
| J'' | 145 | d | III.H Prop 3.2 (\widetilde{L_b}(0)^{-1}) | III.H Prop 3.2 is stated for b near b_0 (PART-III-H-AUGMENT.md:304); uniform by H3 §2 uniformity paragraph | yes | not in (P1)-(P6); n2 |
| J'' | 146 | h | III.H Cor 4.2 radius c_k | (P4); c_k uniform on B̄_1 (H3 §2) | yes | |
| J'' | 149-155 | h | II.G' Cor 4.5 loss ⌈kδ⌉+ℓ, bounded through strong trapping admissibility "at b_0" | III.H'' Prop 1.1 + H3:158-170 | yes | m1 |
| J'' | 160-165 | d | N_{ι+}(λ)^{-1}; III.G'' Thm 4.2/Cor 4.3 "with the towers at b_0" and L_b; III.G''' | (P2) (b-independent N_{ι+}, III.G'' stated for general b), (P3) towers at b | yes | |
| J'' | 167-171 | d | N_tf(\widehat{L_b},±1)^{-1}, III.G'''' Props 4.4, 5.1 | (P2) tf-normal operator b-independent; (P4) | yes | |
| J'' | 173-176 | d | III.I' Props 2.1, 3.1; (z−3/2−\bar A)^{-1} | (P2) (\bar L), Thm 3.1 bullet 1 | yes | |
| J'' | 178-179 | d | III.I'' Lemma 4.3: fixed sections built from the states | (P3) states at b | yes | |
| J'' | 184-191 | h | f(0)<ε from III.F Prop 4.1; β_0, ν_min, q^Γ "do not depend on" trapping data | H3:158-170 performs exactly this computation at every b ∈ B̄_1 | yes | m1 |
| J'' | 204-229 | h | Lemma 2.3: smallness and continuity "at the background 0" | at fixed b: Lemma 2.4 continuity with L_{0,p_b}; across b: Prop 2.5 Step 3 direct bound; "The constants" (I16:397-403) | yes (direct bound) | the proof at 224-228 fails at b (L_j − L_{b_0} does not tend to 0); n1 |
| J'' | 226-227 | d,f | S^{0,0}_ν, R_j := G_j − G − (L_j − L_{b_0})u_j | Lemma 2.4 (I16:205-222) with L_{0,p_b}; Lemma 1.2 | yes at fixed b | n1 |
| J'' | 256 | d | III.I Remark 5.5 rewriting with L_b | (i) | yes | already at b |
| J'' | 265 | d | "FWD of L_{b_0}" in the III.I^9 row | (i), (P6) | yes | |
| J'' | 267 | d | \widetilde{L_{b_0}}(0)^{-1} in the III.I^11 row | III.H Prop 3.2 at b; Prop 2.2(b) for v1 | yes | n2 |
| J'' | 268-269 | g | III.I^12, III.I^13 rows | Thm 3.1 list; Lemma 2.4 | yes | |
| J'' | 270 | d,g | III.I^14 Thm 3.1 row (incl. Step 4') | Prop 2.5; (viii) adds A_b, E^ν to the inventory | yes | row not updated; n4 |
| J'' | 271 | d | III.J' Thm 2.1 at Φ(U); III.G''' Prop 3.7 | (viii); (P2) | yes | |
| J'' | 277-278 | h | Thm 4.1 "for b = b_0" | (viii); \|p\|<δ_0 bounds \|b−b_0\| | yes | δ_0 must also put b in B_*; n5 |
| J'' | 296 | h | Thm 4.2 "b = b_0" | (viii); I16 Cor 3.2 | yes | |
| J'' | 315, 321-331 | h | Prop 4.3 already "for b near b_0"; III.J (2.5) at every b (D285) | Thm 3.1 list (III.J'' Prop 4.3); III.J | yes | |
| J'' | 349-352 | h | (J''2): the tame form at b≠b_0 is part of (J'3) because (H'3) shrinks with k | superseded by III.H'' (H3:222) | yes | stale; m1 |
| J''' | 5, 10-11, 667 | h | "b = b_0"; "(J'3) stays open" | (viii) | - | n3 |
| J''' | 35-37 | c | roots μ of \widehat{L_{b_0}}(0); non-real roots Re < −101 or > 1 | (P2) indicial roots b-independent | yes | |
| J''' | 41-42 | h,c | "Throughout b = b_0"; admissible α, (A_J) | (viii): (P2)-(P3) | yes | |
| J''' | 78-99, 101-113 | c | (E1)-(E5), (A_K): Λ, roots, tf-exponents α_0, E_ind, λ_♯, exponents at hand | (viii) (P2)-(P3) | yes | (E3) at b: the rotation rows add exponents λ+N_0 with Re λ ≤ 2, none at α−2, α−1, α (all > 2), so the set of excluded values is unchanged |
| J''' | 162-201 | d | Cor 3.2: III.G'' Thm 4.2 at b, spec_{ι+}(\bar L), circle choice | (P2) | yes | already written with L_b, u_{b,0} |
| J''' | 211-234 | c | III.G' Thm 3.1(2); A_0 = \tilde L(0), boundary spectrum {−μ} | (P2) | yes | |
| J''' | 236-247 | d | r(λ) via III.G'' Lemma 4.1 at b; u_0 from roots; L_b ∈ Diff_b near K^+ | (P2), (P3) | yes, by continuity in b on the compact B̄_* | not stated; covered by (viii) |
| J''' | 272-297 | d,g | Prop 3.4: graft at b; rows identified up to Re λ_0+1−ε > 5/2 > α−2 | Prop 2.2(a) (rotation rows, same identification order) | yes | |
| J''' | 289 | d | f^♭ = f − L_{b_0}(u_I+u_ι) | (i), (P2) | yes | |
| J''' | 331-400 | g,c | Prop 4.3: levels 1-3; v1 at level 1 has rate α_0 at b | Prop 2.2(b); (G) (no rate in (2, 2+ε_K]) gives room at α−2 | yes | rotation-row coefficient Y' assigned; not mentioned in J'''; m2 |
| J''' | 349-350, 363, 371-372, 399 | c | root facts (d(Re μ, Z) ≥ ε_ind; no root with Re in (0,1]) | (P2) | yes | |
| J''' | 362, 396-397 | d | III.H Prop 3.2 at interior weights | III.H Prop 3.2 (b near b_0) | yes | n2 |
| J''' | 416 | c | \|h\| ≲ r^{-3}, \|\breve h\| ≲ r^{-2} (states' decay) | (P3) leading terms b-independent | yes | |
| J''' | 436-438 | d,c | (L − L_{b_0})u_0; L_{b_0}m_ν of order > 9/2 | (i); Lemma 2.1 (rotation rows κ = Re λ+4, so order > 9/2 for Re λ > 1/2+ε) | yes | |
| J''' | 444-445 | f | coefficient sections below α−2 vanish "as before" | Lemma 1.2 (Cor 2.3 at b); §2 for v1 | yes | |
| J''' | 451-458 | b,g | tower types, d_ρ ∈ {μ,0,1}, d_{v1} = 0; Y^c_ρ | (P3); I13:56-62 (v1 rate z+1 only at b_0) | yes | at b the v1 bottom is in A^3, lower order at ι^+; no change |
| J''' | 462, 468-470 | d,c | profiles "homogeneous of degree d_ρ − j" (towers built at b_0, I13:48) | (P3): leading terms b-independent, corrections smaller by min Re E_ind > 0 (I13:53-54) | yes | Lemma 4.7(a) needs only \|(r∂_r)^a∂^β p_j\| ≲ r^{j−d}, which (P3) gives |
| J''' | 472-473 | f | coefficient sections below α are exactly sums of states (III.I^12 Lemma 2.3(a)) | Lemma 1.2; states at b (P3) | yes | |
| J''' | 531-549 | g,d | Lemma 5.1: δ_1 = min over κ_ν−ε; III.J's rows remove formal solutions of rate < α | Lemma 2.1 (κ at b); (viii), III.J Thm 2.4 at b | yes | |
| J''' | 551-568 | e,g | Prop 5.2: h_{b,rem}(q), L_b \dot g(b), ∂_b h_{b,rem}(q)b'; q's v1 rates > 2+ε_K | (iv); I16 Def 1.1 rates at b | yes | already written at b |
| J''' | 570-590 | d,f,g | Thm 5.3: III.I^14 Thm 3.1 at exact weights; G' lists f^S, f^b, f^{s1}, r^ν only; "Step 3 and its uniqueness"; "Step 4'"; "rate ≤ 2" coefficients killed | Prop 2.5, Remark 2.6 (third bullet), (v); E^ν exact at α by its own (P6) bounds (κ_ν−ε > α; ι^+ exponents in E^♮+2 with π_1E^♮ ⊂ Λ, III.I^13 Lemma 1.3(a), so (E1) applies) | yes | **GAP (minor): the statement at b, "Prop 2.5 at exact weights", is written nowhere; m2** |
| J''' | 584 | a | f^S, f^b, f^{s1} have "stationary coefficients" | (P5) | yes | |
| J''' | 592-617 | d,g | Prop 5.4: ϑ_{ν,♯} at κ_ν−ε; rotation rows at Re λ+4; L_b stationary | (P6), Lemma 2.1, (P5) | yes | |
| J''' | 619-635 | h | Thm 5.5 "b = b_0" | (viii); I16 Cor 3.2 | yes | |
| J''' | 645-665 | h | Cor 6.6: forward solutions exact; model inverses incl. II.G' Cor 4.5 | (P1); III.H'' Prop 1.1 for the trapping loss | yes | m1 applies |
