# The base-point ledger: III.I16 Theorem 3.1 by reading

*Status.* Read (D328-D330): all five batches read, by verifiers 145-149. Three gaps and one unstated theorem were
found and are repaired in III.I16 (D329-D330); the repairs are to be read.

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

- or an item (i)-(viii) of Theorem 3.1's proof (now (i)-(xi)).

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
| 2 | III.I$''''''$-III.I$'''''''''$ (PART-III-I7 to I10) | 1,814 | verifier 146 | read (D330); one gap, repaired, to be read |
| 3 | III.I$''''''''''$-III.I$'''''''''''''$ (PART-III-I11 to I14) | 1,718 | verifier 147 | read (D330); one gap, repaired, to be read |
| 4 | III.I$''''''''''''''$, III.J, III.J$'$ (PART-III-I15, J, J2) | 1,122 | verifier 148 | read (D330); no major gap, one minor gap (reality), repaired, to be read |
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

## Batch 2: III.I$''''''$-III.I$'''''''''$

Verifier 146 read every line (69 rows; by category a 6, b 3, c 10, d 43, e 8, f 8, g 3, h 6, and i 3, the reader's own,
for maps fixed by $L_{b_0}$ as a reference). One gap, major: III.I$'''''''$ Lemma 2.4's parameter identities are exact
only at $(0,0)$, as the background at $(0,\vec p_b)$ mixes $g_{b_0}$ and $g_b$ in $\mathcal C$ and the corrections #2
are built at $b_0$; so III.I$'''''''$ Lemmas 4.3, 4.5, Corollary 4.6 and III.I$''''''''$ Proposition 4.1's base step,
which invert their maps by continuity from $(0,0)$, and III.I16 Proposition 2.5's base level did not carry to $b$.
Repaired in III.I16 section 2.8, by Lemma 2.11 (the identities at $b$ with an error $E^{\mathrm{mot}}_b$, supported in
$\mathcal C$ and $O(|b-b_0|)$) and Proposition 2.12 (a direct bound), and in Proposition 2.5's Step 3. Two minor
findings, seated in Theorem 3.1's list: the statements of III.I$'''''''$ used at $b$, and the fixed-$b$ qualification of
the continuity statements. Five nits seated, among them the naming of the corrections #1-#4 and the stale pointers in
III.I$'''''''$-III.I$'''''''''$. Report: the scratchpad file d327/ledger146.md.

| part | line | cat | property used | supplied by | uniform | note |
|---|---|---|---|---|---|---|
| I7 | 18 | h | "Everything is at b = b_0" | Thm bullet 1 | yes | |
| I7 | 23-27 | a | Lhat_b(sigma)=L0-i sigma L1-sigma^2 L2, L1,L2 stationary | (P5) | yes | only d_t Killing used |
| I7 | 28-36 | d | augmented operator, rows f*_j with III.H (3.1), columns, states gdot,h,hbreve of III.H s.1 | (P3); III.H Prop 3.2 (stated near b_0, B(b) invertible) | yes | III.H Prop 3.2 not in (P4) (n3) |
| I7 | 49-73 | d | Lemma 1.1: L1 on u0; source terms f of III.H Lemma 2.2/2.4 | (P5), III.H at b | yes | |
| I7 | 82-99 | d | Lemma 1.2: Fredholm, kernel trivial for small sigma (III.F'' mode stability, III.H Thm 4.1) | (P4): III.H Cors 4.3-4.4 at b | yes | |
| I7 | 101-117 | d,f | Lemma 1.3: gdot(e1)+h(e2) in A^2, ker L0; r(w_e)=e | (P3); III.H B(b) | yes | |
| I7 | 120-139 | d | Lemma 1.4: h^{<=3}_{b0,s1}, III.G'''' Prop 5.1, Lemma 4.3 index set (0,0)+E_ind | (P4),(P3) | yes | Lemma 4.3 is a lemma, (P4) says "propositions" (n3) |
| I7 | 143-152 | h | Prop 2.1 "at b_0" | Thm bullet 1 | yes | |
| I7 | 144,174,227-228 | c | eps_ind; set of -mu real, discrete | (P2) | yes | constants |
| I7 | 160-168 | d | Step 0: L-L_b gains a_K at K+ | (i), III.I Lemma 3.6 | yes | |
| I7 | 170-188 | c | lambda_sharp, III.G'' Cor 4.3, a_s1 a power, E^iota_ind | (P2) | yes | |
| I7 | 202-208 | d,f | Step 3.1: III.H Prop 3.2; h(S0)=0 => S0=0 (III.F''' Prop 4.1(1)) | III.H Prop 3.2 at b; L1.2 | yes | |
| I7 | 225-242 | d,g | Step 3.2: (5.2) at b; only s1 term below zf-weight alpha-2 | (P4): III.G'''' (5.2) is written at b; its v1 term carries abs(sigma)^{alpha-2} even with h_{b,v1}!=0 | yes | checked G5-TF:636-639 |
| I7 | 244-276 | d | Steps 3.3-3.5: Ltilde_b(sigma)^{-1}, III.I'' Lemma 4.2, injectivity | (P1),(P4) | yes | |
| I7 | 291-319 | d,f | Step 5: G1,G2 at b; S4+=S4- (h injective); (0,0)-coefficient | (P3), L1.2 | yes | |
| I7 | 326-330 | a,f | Step 6: stationary tensor of positive K+-weight vanishes; Im bdot=0 by rows | (P5); III.H B(b) | yes | |
| I8 | 20,454,481-484 | h | base points at b_0; (I'''''''4) "waits on those inputs" | Thm bullet 2, (iv) | yes | text superseded, no pointer (n5) |
| I8 | 28-30 | d | omega_s1=omega^{(0)}_{b0,s1}, h(S), h^{<=1}_nat; h^{(-1)},theta at b_0 | (P3) states; (P6) corrections | yes | |
| I8 | 31 | b | b-space R x so(4) (III.F''' Prop 2.2) | III.F''' Prop 2.2 near b_0 | yes | |
| I8 | 32-35 | e | gdot_{b0}=d_b g_b at b_0, omegadot_{b0}, gdot^Ups_{b0} | (iv),(P3) | yes | |
| I8 | 35-41,46,48 | c | E_ind at b_0; (1.1) class G; eps_ind | (P3),(P2) | yes | |
| I8 | 42-44 | f | (bdot,S)->gdot+h injective by rows | III.H B(b) / L1.2 | yes | |
| I8 | 55-58 | d | w^0=g_{b0}(Y_S,.) | none needed: exterior is g_{b0} at every b (Def 1.2) | yes | |
| I8 | 100-101,125-127 | d | Lemma 1.3(b): III.I Thm 5.3 for g_p "b=b_0" | (P1) + III.H'' Cor 5.1's proof with Lemma 1.3(a) | yes | (P1) names g_{b0,b,-S} only (n3) |
| I8 | 103-106,129-135 | c | Lemma 1.3(c) "with b=b_0": g_p-eta in rho^2 | g_b-eta in abs(x)^{-2}C^inf at every b (III.B (3.5)) | yes | |
| I8 | 139-151 | d | Def 2.1: corrections #2 at b_0 | (P6) | yes | |
| I8 | 153-175 | d | Lemma 2.2 (b_0-built, any g_0) | b-independent | yes | not in Thm list though used at b (m1) |
| I8 | 196-229 | d,e | Lemma 2.4 (2.3) exact at (0,0) with L_{b0}; at (0,p_b) false: g_{p_b}=g_{b0,b,0}, corrections at b_0 | NONE (I16:93-95 is commentary, f^S,f^s1 only) | - | GAP G1 |
| I8 | 234-262 | d,i | Lemma 2.5: results for L_{h,p}; maps fixed by L_{b0} | Thm bullet 1, (i), (P1) | yes | |
| I8 | 266-318 | d,e | Lemma 3.1 (p=(S,0,S1)): on U_K g_{b0} Ricci flat, gdot_{b0}; U_iota k_b=chi_K gdot_{b0} | proof transfers: g_b Ricci flat for all b, gdot_b (P3) | yes | not in Thm list (m1) |
| I8 | 281,322 | d | Lemma 3.1(c): value at (0,0) is (2.3) | - | - | GAP G1 |
| I8 | 330-337 | a,f | Sdot, Q determined by forward solution | (P5); III.H B(b) | yes | |
| I8 | 339-380 | e | Lemma 4.1: continuity at (0,0) against L_{b0} | at b fixed-b only, reference L_{0,p_b} | no | fixed b only; not listed (m1,m2) |
| I8 | 395-410 | d | Lemma 4.3: S^{(-1)}_{0,0}=id by Lemma 2.4; invertible by continuity | - | - | GAP G1 |
| I8 | 417-427 | d | Lemma 4.5: map = -id at (0,0) by Lemma 2.4 | - | - | GAP G1 |
| I8 | 433-450 | d | Cor 4.6 (b=b_0) | rests on 4.3, 4.5 | - | GAP G1 (Thm lists it as uniform) |
| I9 | 12,25,30 | h,d | motions with h_{b0,s1}; everything at b_0 | (P3),(P6), Thm | yes | |
| I9 | 15-16,425-426 | c | Lhat_b(0) no indicial root in (0,1] | (P2) | yes | |
| I9 | 32-37,55-58,302-303 | c | E_ind (III.D''' at b_0), E^iota_ind, lambda_sharp, roots mu real/discrete, class roots non-integer | (P2),(P3) | yes | |
| I9 | 70-77 | d | omegabreve^i_{b0,s1}, omega^{<=k} in ker Box_{b0} | (P3): III.D''' Prop 3.1 is smooth in b (D4:109-112) | yes | |
| I9 | 79-87 | d | row m_{lambda,k} with delta*_{g_b0}; h^{(lambda-1,k)}_{s1}, theta (#3) | (P6): row at b, corrections at b_0 (= CORR4 rows (s1,lambda,k)) | yes | |
| I9 | 89-123 | a,d | Lemma 2.2: Box stationary (2.1); (2.2) deltahat*(0)omegabreve^0=h(S) | (P5),(P3) | yes | |
| I9 | 137-153 | d | Lemma 2.4 exact motion identity, L_{b0} | (P6) (1.1) with E^nu | yes | "in the form (1.1)" not said (n4) |
| I9 | 155-193 | d,e | Lemmas 2.5-2.6 (b=b_0); 2.6(a) via III.I''''''' Lemma 3.1 | UNPARAM 2.5 at b; Lemma 3.1 at b | yes | m1 |
| I9 | 201-237 | d,i | Lemma 3.1 base level: L_b, UNPARAM 4.1,4.3,4.5, Cor 4.6 | (i); base level -> G1 | - | GAP G1 |
| I9 | 262-274 | g,d | s1 row h^{<=3}_{b0,s1}; v1 row gives lambda_0 | (P2),(P3); I16 Lemma 2.1 and Lemma 2.4 last sentence (rate Re lambda-eps > alpha-2) | yes | |
| I9 | 276-327 | d | Step 3: III.I'''''' at b; III.G'''' Prop 5.1 iterated | Thm bullet 1, (P4) | yes | |
| I9 | 331-337 | f | bdot0=0, S4=0; h injective | III.H B(b), L1.2 | yes | |
| I9 | 339-342 | i | maps fixed by L_{b0} / L-L_{b0} | (i) | yes | |
| I9 | 344-353 | e | Lemma 3.3 continuity at (0,0) | fixed b only (I16:397-401) | no | fixed b |
| I9 | 378-382 | d | base step: Cor 4.6, 4.3, 4.5 close to +-id | - | - | GAP G1 |
| I9 | 394-403 | d,e | T_{0,0}=id by Lemma 2.4; near (0,0) by Lemma 3.3 | I16 Prop 2.5 Step 3 direct bound with (1.1) for rows (s1,lambda,k) | yes | Thm list does not say so (m2) |
| I10 | 22-23,89-96,418-425 | g,b | V_K, V'=0 because every rotation Killing at b_0 | (vi), S2 (rotation rows), I16 Lemma 2.1 | yes | |
| I10 | 27,32 | h | everything at b_0 | Thm | yes | |
| I10 | 33,44-47 | c | lambda_sharp, delta_sharp, eps_ind, w_+ | (P2); delta_sharp gauge-only | yes | |
| I10 | 37-40,85-87 | c | E_ind enlarged (III.D''' at b_0); (H3) | (P3) | yes | |
| I10 | 18-21,67-83 | b,c | six SO(4) types, roots -1,0 of Lhat_{b0}(0), class roots mu_c0, mu_c1, d_tau | (P2) roots; (P3) states; types by the b-independent iota+ decomposition | yes | |
| I10 | 126-150 | d | towers omegabreve^i_tau at b_0, lengths K_tau, ker Box_{b0} | (P3) (III.D''' Prop 3.1 in b), (P6) | yes | |
| I10 | 151-164 | a,c,d | (2.1); omega^{(0)}_{b0,s0}=g_{b0}(d_t,.) Killing; states h_tau | (P5),(P3) | yes | |
| I10 | 166-185 | d | Def 2.1 rows and corrections #4 | (P6) | yes | |
| I10 | 187-247 | a,d | Lemma 2.2(a),(d),(e): Box stationary; theta=1/2 Box omega near K+ | (P5),(P3),(P6) | yes | |
| I10 | 249-253 | f | Lemma 2.2(f) h_tau injective | L1.2; leading terms b-independent (P3) | yes | |
| I10 | 269-280 | d | Lemma 2.4 exact row identity | (P6) (1.1) | yes | |
| I10 | 271,279-280 | d | "identities III.I''''''' (2.3) hold for P_4" | - | - | GAP G1 |
| I10 | 287-293 | h | Lemma 2.5 b=b_0 | UNPARAM 2.5 at b | yes | |
| I10 | 298-343 | d,e | Lemma 2.6(a): d_b g_0=chi_K gdot_{b0}; f^b by UNPARAM 3.1 | (iv),(P3); Lemma 3.1 at b | yes | m1 |
| I10 | 345-361 | d | Lemma 2.6(b): near K+ g_0=g_{b0} | at b g_0=g_b near K+; weight kappa_nu unchanged | yes | |
| I10 | 311-392 | d | Lemma 2.6(c): r^nu w.r.t. L_{b0}, r_{0,0}=0, 2nd term in C at b=b_0 | (P6) f^nu_b; I16 Prop 2.5 Step 3 (r+E = O(abs(b-b0)) at (0,p_b)) | yes | |
| I10 | 427-433 | d | (I'''''''''3) u=v-sum m_nu, Lv=F-sum r^nu | (1.1): add E^nu | yes | |

## Batch 3: III.I$''''''''''$-III.I$'''''''''''''$

Verifier 147 read every line (57 rows; by category a 2, b 5, c 16, d 22, e 1, f 4, g 13, h 4). One gap, major:
III.I$''''''''''''$ Lemmas 2.3-2.4 use $h_{b_0,\mathrm v1} = 0$ without naming it, to put $\breve h^1_{b_0,\mathrm
v1}(V)$ in $\ker L_0$ and to remove the v1 content through an antiderivative; at a rotating $b$, Lemma 2.3 (b) fails
when $\dot b_V\ne0$, and III.I$''''''''''''$ Theorem 3.1, which III.I16 Propositions 2.2 and 2.5 use at $b$, was not
supplied. Repaired in III.I16 section 2.7, by Lemma 2.9 (the lemmas at $b$, with $\kappa_b$ of (2.6) and the rotation
rows $T_{\mathrm v1,b}$ in place of the antiderivative, no map inverted) and Corollary 2.10. Two minor findings: the
level-3 conormal rotation tower at $b$ (in Corollary 2.10), and the collision set $\mathcal E_{\mathrm{col}}$, read as a
$b$-independent set (Theorem 3.1 (iii)). Three nits seated: III.I$''''''''''$'s definitions in the list, the conjugation
symmetry of $A_b$, and $\dot g_b$'s leading terms in (P3). Report: the scratchpad file d327/ledger147.md.

| part | line | cat | property used | supplied by | uniform | note |
|---|---|---|---|---|---|---|
| I11 | 30-36 | d | b = b_0; III.I^(9) s.1-2 objects (states, m_nu, P_4, L_{h,p}) | statement-at-b, P3, P6 | yes | |
| I11 | 33 | g | W_v1 = 0 at b_0 | T(vi), S2 (rotation rows N_rot) | yes | |
| I11 | 66-72 | c | Lambda contains 2+pi_1 E_col, E_col "the column terms at b_0" | P3 + III.I''' L1.1 at b (T-list b.1), implicitly | yes | not named in T(iii): finding m1 |
| I11 | 73-76 | c | pole orders of N_iota+(Lbar)^-1, multiplicities of roots of \hat L_{b_0}(0) | P2 | yes | |
| I11 | 83-85 | c | 3 in Lambda: boost row from mass root 2 | P2 | yes | |
| I11 | 152-161 | c | (G), admissibility: roots of \hat L_{b_0}(0), E_K (III.G' L1.3, from N_iota+) | P2 | yes | b-independent exclusion set |
| I11 | 163-165 | g | rates listed by type, v1 absent | S2 (L2.1: rot rate Re lambda; L2.4 N_rot^{<beta}) | yes | |
| I11 | 169-200, 207-212 | d | Lemma 2.1 (a),(b),(d): towers via delta^*_{g_{b_0}} | P3; (a) uses only stationarity | yes | |
| I11 | 203-205 | a | \breve omega^0_s0 Killing | P5 | yes | |
| I11 | 187-225 | d | Lemma 2.1(c): u_{b_0,0}, k_tau of Table 1.1 | P2, P3; used at b in Prop 2.2(a) proof (I16:180-181) | yes | absent from T-list: n1 |
| I11 | 222 | g | h_{b_0,v1}(V) = 0, V Killing | Prop 2.2(a) | yes | |
| I11 | 223-224 | c | rows outside T have Re mu <= -1 | P2 | yes | |
| I11 | 229-243 | f | Lemma 2.2 joint injectivity | L1.2 (K_0, c independent of b) | yes | |
| I11 | 232-236 | b,a | static, spherical, isotypic components, degrees l_tau | L1.2 (replaces proof) | yes | |
| I11 | 238-243 | c | h_s0 in A^{(0,0)+F}, h_s1 in A^{(3,0)...}, mu_c0, mu_c1 < 0 | inside L2.2's proof only; L1.2 | yes | |
| I11 | 245-258 | f | Cor 2.3 | L1.2 | yes | |
| I11 | 322-327 | g | v1 rows of N_sigma carry no parameter | S2 (N_{sigma,rot}) | yes | |
| I11 | 340-406 | d | L_{b_0}, III.G'' Cor 4.3, III.I' at b_0, chi_K u_{b_0,0} | T(i), P1, P2, Prop 2.2(a) | yes | |
| I11 | 373 | c | spec_iota+(Lbar) in Re >= 2 | P2 | yes | |
| I11 | 399-401 | h | reality: L_{b_0} real, conjugation lambda0 -> bar lambda0 | L_b real | yes | A_b symmetry unstated: n2 |
| I11 | 440-442 | b | rows told apart by spherical degree | L1.2 | yes | |
| I12 | 11, 19-45 | d | \hat L_{b_0}(sigma), \tilde L_{b_0}, injective on X'_sigma | T-list b.1 (III.I''''''), P4 | yes | |
| I12 | 73-106 | d,c | Lemma 1.1: L_{b_0}\dot g = 0, L_{b_0}(t h+\breve h) = 0, \dot g^Y_{b_0} index sets, E_col | P3, P4, III.I''' L1.1 at b | yes | E_col at b: m1 |
| I12 | 112-129 | c,b | roots of \hat L_{b_0}(0) by type; only root < 3 is 2 | P2 | yes | |
| I12 | 135-161 | d | L_0, L_1 in rho Diff^1_b, L_2 | T-list b.1 | yes | |
| I12 | 172-188 | d,b | Lemma 2.3: towers h_{b_0,tau}, Table 1.1 types, beta_mu | P2, P3, P4 | yes | |
| I12 | 179 | g | v1 tower carries sigma at least once | Prop 2.2(b) | yes | |
| I12 | 224-234 | d | Lemma 2.5 | T-list b.1, P4 | yes | |
| I12 | 260-261 | d | S_0 = 0 (III.I'''''' Step 3.1) | T-list b.1 | yes | |
| I12 | 329, 373-374 | h | S_o = 0; \dot b_0 = S_1 = 0 (III.H (3.1)) | P4 (B(b) invertible) | yes | |
| I12 | 375-381 | g | v1 rate >= alpha_0+1 at level 1, alpha_0+2 at level 2 | Prop 2.2(b) | yes | |
| I12 | 382-384 | d | towers = m_nu via I11 L2.1 | P3 | yes | |
| I12 | 403-427 | d,f | Lemma 3.2 (b = b_0); L - L_{b_0}; determination by Cor 2.3 | T(i), I16 L2.4, L1.2 | yes | |
| I12 | 429-435 | d | Lemma 3.3 continuity at (0,0) | I16 L2.4 at fixed b only | fixed b | by design |
| I12 | 446-520 | d | Theorem 4.1 (b = b_0); T_{h,p} -> id by continuity | Prop 2.5 (direct bound) | yes | |
| I12 | 538-546 | c,d | mass root 2 -> boost row lambda = 3; \hat g^aug exact | P2, P4 | yes | |
| I12 | 555-560 | c | "at b_0 cut-off, operator, states polyhomogeneous" | P3 + T-list b.1, implicitly | yes | m1 |
| I13 | 47-61 | d,b | towers T_rho at b_0, harmonics Y_rho, d_rho | P3, III.I^(14) L2.1 | yes | |
| I13 | 54 | h | "Myers-Perry corrections smaller by min Re E_ind" | P3 | yes | |
| I13 | 59-65 | g | v1 K+-rate z+1 (h_{b_0,v1} = 0); "rho != v1" | III.I^(14) Def 1.1, Prop 2.2(c) | yes | |
| I13 | 67-77 | c | E_sharp built from Lambda, M | T(iii) | yes | inherits m1 |
| I13 | 164-169 | g | \breve h^1_{b_0,v1}(V) in ker L_0 because h_{b_0,v1} = 0 | none | -- | GAP, M1 |
| I13 | 171-214 | g | Lemma 2.3 (a) kernel list; (b) \dot b = 0 | none (Prop 2.2(c) uses it as input) | -- | GAP, M1: (b) false at rotating b |
| I13 | 191-193, 211-213 | c,d | simple roots; \bar h_tau leading; ker = span(\dot g, h(S)), 11-dim | P2, P3, P4 | yes | |
| I13 | 241-269 | g | Lemma 2.4: "\dot b = 0" step; subtraction T_v1(\tilde a V); mu_v1 = -1 | none | -- | GAP, M1 |
| I13 | 298-322 | d | Step 0-1(ii): L_{b_0}, tower relations, graft u_{b_0,0} | T(i), P2, P3, I16 L2.1, Prop 2.2(a) | yes | |
| I13 | 366-373 | g | level-3 rotation tower rate alpha_tau+3 > alpha | none (at b rate alpha_tau+2 < alpha) | -- | GAP, m2 |
| I13 | 388-406 | g,d | C omits a v1 conormal tower; Lemma 2.4 applied with L_{b_0} | depends on M1, m2 | -- | GAP |
| I13 | 437 | c | h_s1 in A^3, \breve h^1, \dot g in A^2 | P3 | yes | |
| I13 | 459-463 | h | (I''''''''''''3) "no early \dot g": L_1\dot g(\dot b) in L_0(G) only for \dot b = 0 | none | -- | false at rotating b, M1 |
| I14 | 31-32, 49-50 | g | v1 rate lambda; N_beta | S2 (L2.4 N_rot^{<beta}) | yes | Def 1.1(a) already counts v1 |
| I14 | 35-46 | c | admissible beta: roots of \hat L_{b_0}(0), E_K | P2 | yes | |
| I14 | 52-58 | c | E^natural from E_sharp, E_ind, E^iota_ind | T(iii) | yes | inherits m1 |
| I14 | 93-150 | d | Prop 2.1: L_{b_0}, levels | T-list, Prop 2.2(b) | yes | |
| I14 | 152-176 | d,f | Lemmas 2.2-2.3 (b = b_0) | I16 L2.4, L1.2 | yes/fixed b | |
| I14 | 178-186 | d | Prop 2.4: I13 Thm 3.1 with Y^natural | inside Prop 2.5 | -- | inherits M1 |
| I14 | 21-22, 200-203 | e | b-derivative of towers, exponents E_sharp + increments | T(iv), III.I^(14) L2.1 | yes | |

## Batch 4: III.I$''''''''''''''$, III.J, III.J$'$

Verifier 148 read every line (79 rows; by category a 3, b 4, c 7, d 45, e 8, f 4, g 15, h 3). No major gap. One minor
gap: the reality of the objects at $b$, used for conjugation-symmetric coordinates and by (2.2), was supplied by
nothing; (P3) now says real, with the reason in Lemma 1.1's proof, and Definition 2.3 says that $A_b$ commutes with
conjugation. Two minor findings, seated in Theorem 3.1: III.J holds as written at $b$, with its rows built at $b_0$,
(P6)'s rule of rows at $b$ not being applied there; and III.J$'$ Lemma 1.1 is listed, for Proposition 2.5's output.
Seven nits seated, among them the stale statuses in III.J and III.J$'$. Report: the scratchpad file d327/ledger148.md.

| part | line | cat | property used | supplied by | uniform | note |
|---|---|---|---|---|---|---|
| I15 | 23-29 | b | at b_0 every rotation is Killing, so no v1 row and the v1 terms go to q | sec. 2 (Prop 2.2, Lemma 2.4, Prop 2.5) | Y | motivation only |
| I15 | 39-40 | d | "theorems at b = b_0, derivatives at b_0" | Thm 3.1 rule (I16:10-14), (iv) | Y | global |
| I15 | 39 | c | eta_E = min Re E_ind > 0 | (P3), (iii): E_ind is independent of b | Y | |
| I15 | 41-44 | d | E_+ contains (E_sharp u E^nat) below 3+eps_+ | (iii), (P3) | Y | (iii) does not name E^nat (n7) |
| I15 | 52-56 | d | E^alpha_rho, M_rot taken from E_sharp | (iii) | Y | |
| I15 | 63-65 | g | v1 rate Re z+1 at b_0 (h_{b0,v1}=0), Re z at a rotating b, > 2+eps_K by (G) | in text; (P3); (G) does not depend on b | Y | "Re z" holds only off ker h_{b,v1} (n4) |
| I15 | 67-72 | d | h_{b,rem}, T_{rho,b}, h^{<=2}_{b,v1}, gdot_b | defined at b; (P3), (P6) | Y | |
| I15 | 72, 133-135 | d | at b_0, h_rem(q) is III.I^(12)'s chi_K u_exp | III.I^(12) Thm 3.1 at b with the towers T_{rho,b} ((P6)) | Y | |
| I15 | 76-81 | d | (1.4) at b_0 with h_{b0,rem} | (1.3) is defined at every b, so (1.4) holds at b with h_{b,rem} | Y | not named in Thm 3.1 (n2) |
| I15 | 83-98 | g | rotation rows get the rate Re lambda+1 because h_v1 = 0 at b_0 | I16 Lemma 2.1 (rate Re lambda - eps), Prop 2.5 (they become new rows) | Y | |
| I15 | 87-89 | d | h_nu, theta_nu of the rotation rows are III.I^(9) Def 2.1's b_0 corrections | (P6) | Y | |
| I15 | 99-103 | d | III.I^(11) Thm 4.1 used only with the parameter in the non-rotation P | Thm 3.1 (Thm 4.1 only inside Lemma 2.4/Prop 2.5), Lemma 1.2 | Y | |
| I15 | 103-106 | f,g | Lemma 2.2(f) fails for the v1 rows; Cor 2.3 excludes v1 | Lemma 1.2 (v1 excluded at b too, I16:120-127) | Y | |
| I15 | 106-114 | d | exponents of h_nu in (lambda,k)+F; f^nu = L m_nu + r^nu | (P3) (F does not depend on b); (P6) (1.1) adds E^nu; I16 Lemma 2.1 | Y | |
| I15 | 118-143 | e,g | Lemma 2.1: states smooth in b, h_{b,v1} vanishes at b_0 | already at b; it is (P3)'s source | Y | :140-141 conflicts with (P3)'s wording (n1) |
| I15 | 127-131 | c | (R4): no root at mu-k | (P2) | Y | |
| I15 | 147-163 | d | Lemma 2.2(a) at b_0: h_{b0,s1} in A^3, breve h^1 in A^2, gdot weights 2, 3 | Thm 3.1 lists Lemma 2.2; (P3); (P4)'s A^{q-delta} loss absorbed by the "-" orders | Y | |
| I15 | 147 | h | h_rem(q) is real | none: (P3) is silent on reality at b | - | GAP, m3 |
| I15 | 163-168 | a | L_b h^{<=1}_{b,s1}(S) = S''(..)+S'''(..): stationarity plus the tower relations at b | (P5), (P3) | Y | |
| I15 | 173-188 | d | Lemma 2.3 through Lemma 2.2(a) and III.I^(9) Lemma 2.5 | the list (III.I^(9) sec. 2) | Y | |
| I15 | 193-209 | d | Lemma 2.4(a) at b_0: h_nu (b_0-built) supported in C | (P6) | Y | |
| I15 | 211-219 | d | (b): g_0 depends on S only off chi_K; d_S g_p in rho^2 C^inf | Thm 3.1 item 1 (g_{b0,b,-S}); III.I^(7) Lemma 1.3 at b | Y | |
| I15 | 221-238 | e,g | (c): b-derivative at b_0; every q-rate > 2 at every b | (iv) | Y | |
| I15 | 240-242 | e | d_b g_b of weight 2; h^(0)(bdot) in A^G | III.H sec. 1 (the MP family); III.I^(7) Lemma 2.2 (holds for every g_0, PART-III-I8-UNPARAM.md:153-159) | Y | |
| I15 | 243-250 | e | exponents of d_b h_{b,rem}(q): z+d+E_ind, and z+3 for v1 | (P3), I15 Lemma 2.1 | Y | the v1 z+3 exceeds w_+ after L |
| I15 | 253-280 | c,d | Lemma 2.5: thresholds, roots, III.G'''' Props 4.4 and 5.1 | (P2), (P4) | Y | A_b and E^nu not mentioned (n3) |
| I15 | 284-295 | d | Thm 3.1 at b_0 | Prop 2.5 | Y | |
| I15 | 305-321 | d | Step 1: III.I^(8) Prop 4.1 for P_5 | (P1)-(P6); E^nu in Y(alpha_1) (P6), I16:247-249 | Y | |
| I15 | 313-316 | e,g | hat L_{b0}(0) d_b h_{b,v1} = 0 | (iv) | Y | |
| I15 | 330-334 | d | Step 2: orders of r^nu, III.I^(9) Lemma 2.6(c) | (P6) plus E^nu; Prop 2.5 Step 2 | Y | |
| I15 | 348-350 | f | III.I^(10) Cor 2.3 | Lemma 1.2 | Y | |
| I15 | 357-366 | d,e | identity at (0,0) with L_{b0}; continuity as (h,p,q)->0, i.e. b->b_0 | Prop 2.5 Step 3 (direct bound) | Y | |
| I15 | 369-370 | g | a rotation row is a new row at no level (rate Re lambda+1) | Prop 2.5 (new rows at b) | Y | |
| I15 | 375-430 | d,f,g | Step 4': K, l built from b_0 states; h_{b0,v1} = 0; L_{b0}; Thm 4.1's uniqueness | (v): not used at b; Prop 2.5 | Y | |
| I15 | 435-439 | g | v1 coefficient of q' has no M_rot exponent (from Step 4') | Prop 2.5, I16:294-296, with Lemma 2.4's class of u-tilde | Y | |
| I15 | 440-441 | d | chi_K u_exp = h_rem(q') "(Def 1.2 at b_0)" | (P6): the towers of III.I^(12) at b are T_{rho,b} | Y | |
| I15 | 446-457 | d | Remark 3.2(2): the class reproduces | b-free; the new at-b inputs use a_K only through strict inequalities | Y | not named (n2) |
| J | 39 | c | p_<=0 = (S, b-b_0, S_1), g_0 = g_{p<=0} | a coordinate, defined at every b | Y | |
| J | 48-51 | c | (G+): Lambda does not depend on the constants | (P2), (P3)/(iii) | Y | |
| J | 53-57 | c | (A_J): roots of hat L_{b0}(0), E_K | (P2): the indicial roots do not depend on b | Y | |
| J | 76-79 | d | III.G'' Lemma 4.1 for L_b | (P2) (III.G'' sec. 4 is at general b) | Y | |
| J | 81-83 | b | R'_0 = types s0, s2, c0, c1 | (P3) (labels by leading terms that do not depend on b), (P2) roots | Y | |
| J | 131-134, 222-224 | d | G(lambda_0) and T(lambda_0) use the rows m_nu and their corrections | the rows are m^{b0} (J:160, 268-270); (P6) puts rows at b | Y | m1 |
| J | 152-155 | d | L_{0,p<=0} - L_{b0} has iota^+-order 2 | III.I^(7) (1.3), Lemma 2.2 (every g_0); III.I^(9) Lemma 2.5 at b (list) | Y | |
| J | 157-161 | d | D_W P4(0,0) = L_{b0} m_nu (the b_0 identity) | evaluated at (0,0) on b_0 objects, so valid at every b | Y | "bilinear" (n6) |
| J | 166-172 | h | P_4(0,p<=0) supported in supp dchi_K; exponents in G | III.I^(7) (1.3), Lemma 2.2 at general p; F_0 is kept as a source, and no Ricci flatness of g_{b0} in C is used | Y | contrast I16 sec. 2.6 |
| J | 178-185 | b | types, mu_tau, c_tau | (P2), (P3) | Y | |
| J | 192-197 | d | rows through III.I^(10) Lemma 2.1(a) at b_0 | the b_0 rows are valid as b_0 objects | Y | m1 |
| J | 195 | a | breve h^0_{s0} = 0 (d_t Killing) | (P5) | Y | |
| J | 212-214 | g | breve h^0_{v1} = h_{b0,v1} = 0 for the rotation rows | b_0 rows; with rows at b, h_{b,v1} in A^3 enters at u >= lambda_0+3 > 3+eps_+ (J:218-219, (P3)) | Y | |
| J | 214-219 | d | lambda_0-term of T_{rho,b} does not depend on b | (P3), I15 Lemma 2.1 | Y | |
| J | 233-235 | g | v1 rate Re lambda_0 at a rotating b | in text, (P3) | Y | n4 |
| J | 237-249 | b,g | assignment by type; v1 goes to the rotation rows | (P3) labels; I15 Def 1.3 | Y | |
| J | 264-272 | d | L_{b0} m_nu = f^nu_{0,0}, kappa_nu; tower relations of L_b | the b_0 identity on b_0 objects; (P3), and the v1 tower relations at b (I16 Lemma 2.1 proof) | Y | |
| J | 289-291 | d | M + E_ind stays in M below 2 | (iii); the v1 +3 lies above 2 | Y | |
| J | 335-337 | d | III.I (1.4), Cor 4.2 | (P1) | Y | |
| J | 338-339 | d | near K^+ the rows enter only through theta_{nu,sharp} (b_0-built, kappa_nu) | (P6) | Y | |
| J | 340-345 | g | the integral has K^+-order > alpha at every b, its v1 part included | in text; (iv) | Y | |
| J | 346-348 | a | L_b stationary | (P5) | Y | |
| J | 349-356 | e | smooth in U_0 through F_0 and T_{rho,b} | (P3) | Y | |
| J | 361-362 | h | the states are real (conjugation, (4)) | none: (P3) is silent | - | GAP, m3 |
| J | 370-372 | d | the removed row terms are "pure gauge" | with the b_0 rows, pure gauge for g_{b0} only | Y | remark (m1) |
| J | 403-404 | d | (J5)(b) "open" | Thm 3.1, Cor 3.2 | Y | stale (n5) |
| J2 | 4, 8-9, 25-27 | d | "at b_0"; b != b_0 open | Cor 3.2 | Y | stale (n5) |
| J2 | 29-65 | d | Lemma 1.1 (eta_2 -> eps_+) at b_0 | not named in Thm 3.1; supplied by (P2), (P4) and Def 2.3 | Y | m2 |
| J2 | 41-43 | g | at level 2, tf-exponent alpha_0 = u-exponent alpha_0+1 | the thresholds are on tf-exponents and so are unaffected by Prop 2.2(b)'s rate shift | Y | |
| J2 | 44 | d | tilde L_{b0}(0)^{-1} | (P4): III.H Prop 3.2 at b | Y | |
| J2 | 46-47 | c | no indicial root in (0,1) | (P2) | Y | |
| J2 | 69-70, 79 | d | U and p at b_0 | Cor 3.2; (viii), Prop 2.5 | Y | |
| J2 | 76-86 | d | Step 0: III.I^(14) Thm 3.1 | Prop 2.5 (Remark 2.6: only the constructed map is used) | Y | |
| J2 | 78 | d | III.I^(14) Remark 3.2(2) | b-free | Y | n2 |
| J2 | 99-100 | d | h_{b0,rem}(q'); the rows m_nu | h_{b,rem} by the rule ((1.4) at b); III.J's rows are m^{b0}, and only the rows at lambda_0 enter, whose lambda_0-terms do not depend on b | Y | m1 |
| J2 | 101-104 | e | differentiating III.J Lemma 2.1 with p'_<=0 = 0 | III.J is at b | Y | |
| J2 | 107-111 | d | [h']_{lambda_0} = O(R^{l_K}) from K^+-order alpha- | Prop 2.5 (u in Z_alpha) | Y | |
| J2 | 116-118 | d,g | rates of q' < alpha (III.I^(12) Lemma 2.4, III.I^(14) Step 4) | Prop 2.5 / Lemma 2.4; the v1 Re z <= 3 by (G+) | Y | |
| J2 | 122-125 | f | distinct rows have independent, injective leading terms (III.G'' Lemma 1.2) | at the Minkowski model level; (P2), (P3) | Y | |
| J2 | 141-144, 148-149 | d | q' has no polyhomogeneous part; its orders by Lemma 1.1 | m2 | Y | |
| J2 | 154-156 | d | III.I^(14) Thm 3.1 linear and uniform | Prop 2.5, uniform in b | Y | |
| J2 | 179-181 | d | (J'3) "to be verified" | I16 proved (D311) | Y | stale (n5) |

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
