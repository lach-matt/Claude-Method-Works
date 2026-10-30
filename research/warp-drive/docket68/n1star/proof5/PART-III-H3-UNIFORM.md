# Part III.H$''$. Uniformity near $b_0$, n = 4 ([Hin26] Proposition 8.3 and Theorem 10.1 on a fixed neighbourhood of
$b_0$; [Hin26c] Theorems 10.1 and 11.1 uniformly in the stationary model)

*Status.* Written (D294). This part proves, at spatial dimension $n = 4$, the two inputs that Part III lacked at black
hole parameters $b\ne b_0$ ((I3) of III.I). The first is the 2-admissibility of $2L_b$ for every order $k$ of
b-regularity, on one fixed neighbourhood $\mathcal B_*$ of $b_0$ and with constants uniform in $b$ (Theorem 2.1). The
second is the forward solution theory of II.F Theorem 8.1 and II.F$'$ Theorem 1.1, uniformly over the stationary models
$2L_b$, $b\in\mathcal B_*$ (Theorems 3.1 and 4.1). So III.I Theorem 5.3, the source's Theorem 11.12, holds for
$b\in\mathcal B_*$ with constants uniform in $b$ and with continuity in $b$ (Corollary 5.1). This discharges (H$'$3) of
III.H$'$, (F$'$11) of II.F$'$ for this family, and (I3) of III.I. What (J$'$3) of III.J$'$ needs beyond this is recorded
as (H$''$5).

*What n = 4 changes.* (1) *The trapping bound at every $b$.* III.F Proposition 4.1 proves strong trapping admissibility
at $b_0$ only, from a frame built with Tangherlini's symmetry; near $b_0$ it gives the bound $\epsilon$ only on a
neighbourhood that shrinks with $\epsilon$, which is why III.H$'$ Theorem 1.3 holds on $\mathcal B_K$ only for $k\le K$.
The source proves the bound at every Kerr parameter by a computation in Marck's tetrad ([Hin26] pp. 147-149). Here the
frame comes from the null geometry alone. Along every null bicharacteristic $e_0 := \zeta/\sigma$ is parallel and the
filtration $\mathrm{span}\,e_0\subset e_0^\perp\subset T^*$ is invariant, so in an adapted frame the connection is a
rotation of the screen plus a part that lowers a grading. III.F's computation uses the Tangherlini frame only through
these properties, so it holds at every $b$, with bounds uniform on $\mathcal B_*$ (Proposition 1.1). (2) *The model at
$\iota^+$ does not see $b$.* By III.F Lemma 2.1 (3), $2L_b-2\bar L$ has coefficients of orders $\rho^2,\rho^3,\rho^4$
near infinity, so $N_{\iota^+}(2L_b) = N_{\iota^+}(2\bar L)$ (Lemma 3.2), and II.F sections 1-6, which concern that
operator alone, hold for every $b$ with the same constants. (3) The rest is continuity and compactness, as in I.A
section 8, I.B section 9 and III.H Remark 2.6.

## 0. Setting

The parameters are those of III.H section 1: the gauge modification $E_\Upsilon$ of III.D section 1 and the constraint
damping $(c_C,e_C,\gamma_C)$ of III.F section 1, with $e_C\in(0,1)$, $\gamma_C>0$, and (Dyn) (III.D, introduction).
$\mathcal B$ is the neighbourhood of $b_0$ of III.H Corollary 4.4, on which III.H Corollaries 4.2-4.3 hold uniformly.
$U_\Gamma$ is the fixed neighbourhood of the projections of the trapped sets of III.D section 1, over which $E^\Upsilon
= 0$ for every $b\in\mathcal B$. As in III.F section 4 we take $z_0 = 1$ (the operator has real coefficients, and $z_0 =
-1$ is the conjugate case); then $\sigma = 1$ on $\Gamma_b$ in I.B's normalisation, and $\Gamma_b$ lies in the future
characteristic set over $\{|x|>r_h\}$. Fix an open $\mathcal B_*\ni b_0$ whose closure $\bar{\mathcal B}_*$ is a compact
subset of $\mathcal B$, such that for $b\in\bar{\mathcal B}_*$:

(B1) $\Gamma_b$ lies over a fixed compact subset of $U_\Gamma$ and in a fixed conic neighbourhood $O$ of $\Gamma_{b_0}$
in $T^*M\setminus o$, on which $\sigma>0$ and which meets the characteristic set $\Sigma_b$ of $g_b$ only in its future
component; I.B (Γ.1)-(Γ.3) hold with $\nu_{\min}$, $\beta_0$ and $\sup_\Gamma q^\Gamma$ continuous in $b$ and positive
((Dyn));

(B2) $dt_*$ is $g_b$-timelike over $U_\Gamma$ ($g_b^{00}<0$ on $X^\circ$, III.B Lemma 3.7 (a));

(B3) $c_C$ is past timelike for $g_b$ over $U_\Gamma$ (III.E Theorem 1.1 at $b_0$, and continuity over the compact
closure of $U_\Gamma$);

(B4) $|b-b_0|$ is below the bound that the proof of III.I Theorem 5.3 needs for $\|P-P_0\|_{(0;d)}<\epsilon_0'$ (III.I
Proposition 3.4, (3.7)), and the order $\mathsf s$ of II.C Proposition 5.1, built for $2L_{b_0}$, is admissible for
$2L_b$ with the same weights and margin (II.C Proposition 5.1 (4)); it satisfies (C1)-(C3) of III.H$'$ Definition 1.1
(III.I Lemma 5.1).

Put $f_b := |dg_b|/(|dt_*|\,|dx|)$, a smooth positive stationary function, smooth in $b$.

## 1. Strong trapping admissibility on $\mathcal B_*$ ([Hin26] Proposition 8.3 at n = 4)

**Proposition 1.1.** For $\eta\in(0,1]$ and $b\in\bar{\mathcal B}_*$ there is a stationary fibre inner product
$h_{\eta,b}$ on $\pi^*S^2T^*$ over $O$, homogeneous of degree 0 and smooth in $b$, such that, with $p_1^\Gamma$ of I.B
(Γ.4) for $2L_b$, $h_{\eta,b}$ and the adjoints of I.A (for $|dx|$ and $dt_*$),
$$\sup_{\Gamma_b}\lambda_{\max}(p_1^\Gamma)\le C\eta,\tag{1.1}$$
with $C$ independent of $\eta$ and $b$. In particular $2L_b$ is strongly trapping admissible ([Hin26c] Definition 5.8)
at every $b\in\bar{\mathcal B}_*$.

*Proof.* *Step 1: the subprincipal operator.* Over $U_\Gamma$, $E^\Upsilon = 0$ and $R_{g_b}$ has order 0, so III.F
(4.1) holds at every $b\in\bar{\mathcal B}_*$, on half-densities by $|dg_b|$:
$$iS_{\mathrm{sub}}(2L_b) = \nabla^{\pi^*S^2T^*}_{H_G}+2E^C_{g_b}\sigma_1(i\delta_{g_b})G_{g_b};$$
the identity $iS_{\mathrm{sub}}(\Box_g) = \nabla^{\pi^*S^2T^*}_{H_G}$ is [Hin17] Proposition 4.1, valid in every
dimension and for every metric.

*Step 2: the frame.* On $O$ put $\sigma := -\zeta(\partial_{t_*})$ and $e_0 := \zeta/\sigma$: stationary, homogeneous of
degree 0, null on $\Sigma := \Sigma_b$ and future directed there. As $\partial_{t_*}$ is Killing, $H_G\sigma = 0$; and
$\nabla^{\pi^*T^*}_{H_G}\zeta = 0$, the geodesic equation (the computation of III.D section 5.2 (c), which uses no
property of the metric). So $\nabla_{H_G}e_0 = 0$ on $\Sigma\cap O$. Let $\tau := dt_*$, timelike by (B2). A timelike
covector and a nonzero null covector are never $g^{-1}$-orthogonal, so with
$$e_2 := a\tau+ce_0,\qquad a := -\frac1{g^{-1}(\tau,e_0)},\qquad c := -\frac{a\,g^{-1}(\tau,\tau)}{2g^{-1}(\tau,e_0)},$$
expansion with $g^{-1}(e_0,e_0) = 0$ gives $g^{-1}(e_0,e_2) = -1$ and $g^{-1}(e_2,e_2) =
a^2g^{-1}(\tau,\tau)+2ac\,g^{-1}(\tau,e_0) = 0$ on $\Sigma\cap O$; $e_2$ is stationary and homogeneous of degree 0. Let
$V := \{e_0,e_2\}^\perp$, a rank-3 bundle on which $g^{-1}$ is positive definite (the orthogonal complement of a
Lorentzian plane). Every covector is $\omega = \omega_0e_0+\omega_V+\omega_2e_2$ with $\omega_V\in V$, $\omega_2 =
-g^{-1}(\omega,e_0)$ and $\omega_0 = -g^{-1}(\omega,e_2)$. As $\nabla$ is metric and $\nabla_{H_G}e_0 = 0$,
$$(\nabla_{H_G}e_2)_2 = -H_G\,g^{-1}(e_2,e_0) = 0,\qquad(\nabla_{H_G}e_2)_0 = -\tfrac12H_G\,g^{-1}(e_2,e_2) = 0,$$
so $w := \nabla_{H_G}e_2\in V$; and for a section $v$ of $V$, $(\nabla_{H_G}v)_2 = -H_G\,g^{-1}(v,e_0) = 0$,
$(\nabla_{H_G}v)_0 = g^{-1}(v,w)$, and the $V$-part $\nabla^Vv$ is $g$-skew. In a local frame $(e_0,v_1,v_2,v_3,e_2)$
with $(v_i)$ $g^{-1}$-orthonormal in $V$, therefore,
$$\nabla_{H_G} = H_G+\sigma(N_1+\Omega)\quad\text{componentwise},\qquad N_1e_0 = 0,\ \ N_1v =
\sigma^{-1}g^{-1}(v,w)e_0,\ \ N_1e_2 = \sigma^{-1}w,\tag{1.2}$$
with $\Omega$, the matrix of $\sigma^{-1}\nabla^V$ in $(v_i)$, skew; $\sigma^{-1}w$ and $\Omega$ are homogeneous of
degree 0, as $H_G$ is of degree 1 and the frame of degree 0. At $b_0$ this is the structure of III.D section 5.2 (c):
there $w$ is a multiple of $e_1$, and $\Omega$ is the rotation $\kappa R$ of $V_\perp$.

*Step 3: the grading.* Give $e_0$, $V$, $e_2$ the weights 0, 1, 2 and $S^2T^*$ the induced weight $\mathrm{wt}$, as in
III.F section 4. $N_1$ lowers $\mathrm{wt}$ by 1 and $\Omega$ preserves it. The dual frame vector $E_2$ satisfies
$g^{-1}e_0 = -E_2$ (the pairings of $e_0$ with $e_0$, $V$, $e_2$ are $0$, $0$, $-1$), so $\sigma_1(i\delta)(\zeta) =
\iota_{g^{-1}\zeta} = -\sigma\iota_{E_2}$, and Step 1 reads, on components,
$$iS_{\mathrm{sub}}(2L_b) = H_G+\sigma(A+\Omega),\qquad A := N_1+2\gamma_C\,E^C_{(c)}(-\iota_{E_2})G,\tag{1.3}$$
$N_1$ and $\Omega$ acting as derivations, and $E^C_{(c)}$ the map of III.F (4.2) with $c_C$ in place, divided by
$\gamma_C$. This is III.F (4.2) with $N_1$ for $2N$, $\gamma_C$ for $\gamma$ and $\Omega$ for $\kappa R$. III.F's
grading argument uses the frame through four facts only: $g = -2e_0e_2+\sum_iv_i^2$; the weights; that the part of the
connection not preserving $\mathrm{wt}$ lowers it; and that the $\mathrm{wt}$-preserving part acts on $V$ by skew maps.
All four hold here. So, as there, $A+\Omega = D_0+D_-$, where $D_-$ lowers the refined weight $W = 2\,\mathrm{wt}+s$ and
$D_0$ preserves each of the seven pieces $e_0^2$; $e_0\otimes_sV$; $e_0e_2$; $T := \sum_iv_i^2$; the trace-free part of
$S^2V$; $e_2\otimes_sV$; $e_2^2$. These pieces are $O(V)$-invariant, and on them $D_0$ is $\Omega$ plus the scalars
$0,0,0,-2(1-e_C)\gamma_Cc_2,0,-2\gamma_Cc_2,-4\gamma_Cc_2$. $N_1$ lowers $W$ (by at least 1, as it lowers $\mathrm{wt}$
by 1), so it lies in $D_-$, and $D_0$ is the $W$-preserving part of the constraint damping term plus $\Omega$, exactly
III.F's $D_0$ with $\Omega$ for $\kappa R$ (`lgrade5.py` G1 computes it for every $c$). Here $c_2 = -g^{-1}(c_C,e_0)<0$,
as $c_C$ is past timelike (B3) and $e_0$ future null; so the scalars are $\ge0$, $e_C<1$.

*Step 4: the inner product.* Let $\langle\cdot,\cdot\rangle_0$ be the inner product on $\pi^*S^2T^*$ induced by
declaring $e_0,v_1,v_2,v_3,e_2$ orthonormal. It does not depend on the choice of $(v_i)$, as $O(V)$ acts unitarily, so
it is defined on $O$, stationary, homogeneous of degree 0 and smooth in $b$ (the frame is built from $g_b$, $\zeta$ and
$dt_*$); the seven pieces are orthogonal for it, and $\Omega$ is skew. Put $h^0_{\eta,b} :=
\sum_P\eta^{-2W(P)}\langle\cdot_P,\cdot_P\rangle_0$ on $\Sigma\cap O$, and extend it to a stationary inner product on
$O$, homogeneous of degree 0 and smooth in $b$; $p_1^\Gamma$ involves the inner product only on $\Gamma_b$ and through
its derivative along $H_G$, which is tangent to $\Sigma$, so the extension does not enter. As in III.F, in an
$h^0_{\eta,b}$-orthonormal frame $D_-$ is $O(\eta)$ and $D_0$ is unchanged; $h^0_{\eta,b}$ is constant in the frame, so
$H_G$ is skew; and by (1.3) and I.B (6.0), on $\Gamma_b$,
$$p_1^\Gamma = -\tfrac12(D_0+D_0^*)+O(\eta),\qquad-\tfrac12(D_0+D_0^*)\le0,$$
for the half-densities by $|dg_b|$. The $O(\eta)$ term is bounded by $\eta$ times a polynomial in $|\sigma^{-1}w|$,
$\gamma_C$ and the components $c_\mu$, which are continuous on $O$ and in $b$; as $\Gamma_b\cap\{\sigma = 1\}$ lies in a
fixed compact subset of $O$ modulo time translations (B1), the bound is uniform on $\bar{\mathcal B}_*$.

*Step 5: the density.* I.A's adjoints are for $|dt_*|\,|dx|$, and (1.3) is on half-densities by $|dg_b| =
f_b|dt_*|\,|dx|$. Put $h_{\eta,b} := f_bh^0_{\eta,b}$. Then $\int h_{\eta,b}(u,v)\,|dt_*|\,|dx| = \int
h^0_{\eta,b}(u,v)\,|dg_b|$, so the two pairings agree, and with them the adjoints and $p_1^\Gamma$ ($p_1^\Gamma$ is an
endomorphism, and a scalar factor in the inner product changes neither its self-adjointness nor its eigenvalues). This
replaces the scalar $O(|b-b_0|)$ that III.D Lemma 5.2 and III.F Proposition 4.1 carry for a fixed inner product. With
$C\eta<\epsilon$, (1.1) gives strong trapping admissibility. $\square$

**Corollary 1.2 ($\delta_\Gamma$ uniformly small).** For every $k\in\mathbb N_0$ there are $\eta_k\in(0,1]$ and
$\epsilon_k>0$ such that, with $h_\Gamma := h_{\eta_k,b}$ in I.B (Γ.4), $\delta_\Gamma(0)<\frac1{2(k+1)}$ and
$\delta_\Gamma(-\epsilon)\le\frac1{k+1}$ for $\epsilon\in(0,\epsilon_k]$ and every $b\in\bar{\mathcal B}_*$. So
$\mathcal B^{\mathrm{hi}}_k$ of III.H$'$ section 1 may be taken to contain $\bar{\mathcal B}_*$ for every $k$.

*Proof.* With $f(\eta') := \sup_\Gamma\lambda_{\max}(p_1^\Gamma-\eta'q^\Gamma)$ of I.B (1.4), $q^\Gamma\ge2\beta_0$ and
(1.1) give $f(\eta')\le C\eta-2\beta_0\eta'$ for $\eta'\ge0$, so $\gamma_+\le C\eta/(2\beta_0)$. $f$ is Lipschitz with
constant $Q := \sup_\Gamma q^\Gamma$ and $f(\gamma_-)-f(\gamma_+) = \frac12\nu_{\min}$, so
$\gamma_+-\gamma_-\ge\nu_{\min}/(2Q)$. Hence, by (1.4),
$$\delta_\Gamma(-\epsilon)\le\frac{\gamma_++\epsilon}{\gamma_+-\gamma_-}
\le\frac{2Q}{\nu_{\min}}\Big(\frac{C\eta}{2\beta_0}+\epsilon\Big),$$
and $\beta_0$, $Q$, $\nu_{\min}$ are continuous and positive on the compact $\bar{\mathcal B}_*$ (B1). Choose $\eta_k$
and $\epsilon_k$ accordingly. $\square$

For each $k$ the inner product $h_{\eta_k,b}$ is a different one; I.B Theorem 1.3 is applied at each $k$ separately
(III.H$'$ Lemma 3.1), so this is what it needs.

## 2. 2-admissibility on $\mathcal B_*$ for every $k$ ([Hin26] Theorem 10.1 at n = 4)

**Theorem 2.1.** III.H$'$ Theorem 1.3 holds with $\bar{\mathcal B}_*$ in place of $\mathcal B_k$, for every $k$: for
$k\in\mathbb N_0$, the order $\mathsf s$ of (B4) and $b\in\bar{\mathcal B}_*$, III.H$'$ (1.2) holds with a constant
$C_k$ independent of $b$. So $2L_b$ is 2-admissible with sf-weight $\alpha_{\mathrm{sf}}$, sf-loss 0 and margin 1 (II.C
Definition 2.7, relaxed, for these orders) at every $b\in\bar{\mathcal B}_*$, with constants uniform in $b$.

*Proof.* Run III.H$'$ sections 2-7 at $b\in\bar{\mathcal B}_*$. Each constant is uniform, as follows.

(i) *Section 2.* $c$ is at most the $c_{j,k'}$ of III.H Theorem 4.1 (3) for $j+k'\le k$, uniform near $b_0$ by III.H
Corollary 4.2 (and Lemma 5.2 (b) there). Lemma 2.1 has no constant; its high-energy input, I.B Theorem 1.3 (3), is
uniform in $b$ by I.B section 9.

(ii) *Lemma 3.1, $|\sigma|\ge C_0$.* I.B Theorem 1.3 (5), at the orders of III.H$'$ Lemma 1.2 (b), with $h_\Gamma :=
h_{\eta_k,b}$ of Corollary 1.2. By I.B section 9 its constants are uniform in $b$, given (H5)-(H8) continuously in $b$
((Dyn)) and the inner product continuous in $b$; then the thresholds $\gamma_\pm$ of I.B section 6 and $c_\Gamma$ are
continuous in $b$. The condition $(k+1)\delta\le1$ of the proof holds on $\bar{\mathcal B}_*$ by Corollary 1.2, for
$\epsilon\le\epsilon_k$.

(iii) *Lemma 3.1, $\frac c2\le|\sigma|\le C_0$.* The argument by contradiction there, run with sequences
$(\sigma_n,b_n)\to(\sigma_*,b_*)$, $b_*\in\bar{\mathcal B}_*$. The estimates (7.1) and (7.3) of I.A Theorem 7.2 hold
uniformly in $b$ for these fixed orders (I.A Theorem 8.1); the coefficients of $\widehat{L_{b_n}}(\sigma_n)$ converge in
$C^\infty$ to those of $\widehat{L_{b_*}}(\sigma_*)$; and the limit is a nonzero element of the kernel of
$\widehat{L_{b_*}}(\sigma_*)$ on a space of admissible order. This contradicts III.H Corollary 4.4, as $b_*\in\mathcal
B$. The inverse is then bounded uniformly and continuous in $(\sigma,b)$ (I.A Theorem 8.1), which gives the
$\sigma\partial_\sigma$-derivatives as there.

(iv) *Section 4 (Lemmas 4.1-4.2).* III.H Corollaries 4.2-4.3 and the bound (4.5) of III.H, uniform near $b_0$ (III.H
Remark 2.6 and the uniformity paragraph of the proof of III.H Corollary 4.2).

(v) *Section 5 (Lemma 5.1).* Uniform near $b_0$, by the last paragraph of III.H$'$ section 5 (III.H Remark 2.6).

(vi) *Section 6 (Lemmas 6.1-6.2).* Statements about $t_*$-translation-invariant elliptic operators and integration in
$t_*$, which do not involve $b$.

(vii) *Section 7.* The assembly, linear in the bounds above.

For II.C Definition 2.7: (1) is Proposition 1.1; (2), tf-admissibility with weight $\alpha_{\mathrm{sf}}+2$, is III.F$'$
Proposition 3.3, which holds for every $b$ near $b_0$ as the tf-normal operator does not depend on $b$; (3) is (1.2) of
III.H$'$ at the orders of (B4), which lie in $\mathcal O_c$. $\square$

This supersedes the restriction $k\le K$ of III.H$'$ Theorem 1.3 and (H$'$3).

## 3. II.F Theorem 8.1 uniformly in $b$ ([Hin26c] Theorem 10.1 for the stationary models $2L_b$)

**Lemma 3.2 (the $\iota^+$-normal operator does not depend on $b$).** For $b\in\mathcal B$, in the normal form II.F
(1.4) of $P_0 = 2L_b$ on $\{|x|>3R_1\}$: $S = \bar S$, $Q = Q_b$, $g_{00} = g_b^{00}$, and $\rho^2P^{(0)} =
\widehat{2\bar L}(0)+R_b$, so $P^{(0)}(0,\omega,\rho\partial_\rho,\partial_\omega)$ is that of $2\bar L$. Hence
$N_{\iota^+}(2L_b) = N_{\iota^+}(2\bar L)$, and $N^0(\sigma)$ (II.F (1.6)) does not depend on $b$.

*Proof.* III.F Lemma 2.1 (2)-(3): on $\{|x|>3R_1\}$, $2L_b = 2\bar L-g_b^{00}\partial^2_{t_*}+Q_b\partial_{t_*}+R_b$,
with $g_b^{00}\in\rho^2C^\infty(\bar X)$, $Q_b\in\rho^3\mathrm{Diff}^1_{\mathrm b}$,
$R_b\in\rho^4\mathrm{Diff}^2_{\mathrm b}$; and $2\bar L = -2\partial_{t_*}\rho(\rho\partial_\rho-\frac32-\bar
S)+\widehat{2\bar L}(0)$ with $\widehat{2\bar L}(0)\in\rho^2\mathrm{Diff}^2_{\mathrm b}$. Comparing with II.F (1.4) ($c
= \frac32$) gives the identifications. As $\rho^{-2}R_b\in\rho^2\mathrm{Diff}^2_{\mathrm b}$ vanishes at $\rho = 0$, the
frozen operator $P^{(0)}(0,\cdot)$ is $(\rho^{-2}\widehat{2\bar L}(0))|_{\rho = 0}$. II.F Definition 1.1 uses only $S_0
= S|_{\partial X}$ and $P^{(0)}(0,\cdot)$. $\square$

At $n = 3$ the mass enters $R_b$ at $\rho^3$, and $\rho^{-2}R_b$ is of order $\rho$; at $n = 4$ it is of order $\rho^2$.
Either way it vanishes at $\rho = 0$; the point here is only that the remainder carries all the $b$-dependence.

**Theorem 3.1.** II.F Theorem 8.1, with II.F Remark 8.2 (margin 1), holds for $P_0 = 2L_b$, $b\in\bar{\mathcal B}_*$,
$\aleph = 2$, sf-loss 0, the order $\mathsf s$ of (B4), and a constant $C_k$ independent of $b$.

*Proof.* (a) *Sections 1-6 of II.F.* They concern $N_{\iota^+}(P_0)$: its Mellin family $N^0(\sigma)$ and the
semiclassical rescaling (sections 1.2-1.3), the estimates of Propositions 3.1 and 5.1 and their lemmas, and the forward
problem for $N_{\iota^+}(P_0)$ (Proposition 6.2). By Lemma 3.2 none depends on $b$. Their compactness and contradiction
arguments (II.F sections 3.5, 4.2 and 5.4) concern $N^0$ and $N_{\mathrm{tf}}$, which do not depend on $b$. The
uniqueness of section 1.4 (Lemmas 1.3-1.4) is qualitative and holds for every $g_b$, with $t_*$ a time function (II.B
Lemma 1.1).

(b) *Section 7.* $P_+ = \chi N_{\iota^+}(P_0)+(1-\chi)P_0$ (II.F Definition 7.1), and $P_+-N_{\iota^+}(P_0) =
(1-\chi)(P_0-N_{\iota^+}(P_0))$ lies in $x_I^2\tau^3\rho_{\mathrm{cf}}^{-2}\mathrm{Diff}^2_{\mathrm{ebe}}$ (II.F Lemma
7.2 (b)), with seminorms continuous in $b$ (III.F Lemma 2.1 (3): smooth in $b$). $\tau_1$ of II.F Lemma 7.2 (c) is
uniform, the normalised difference there being $O(\rho_+^2)$ with constants continuous in $b$. By the remark after II.F
Proposition 7.4, $\tau_0$ and the constants depend on $P_0$ only through section 7.6. Its estimates are the radial
estimates at cf (II.F Lemma 7.6, whose quantities at the radial sets are those of $N_{\iota^+}(P_0)$, by (a) independent
of $b$), propagation estimates and II.E's slab estimates. Their constants depend on finitely many seminorms of
$P_+-N_{\iota^+}(P_0)$ and of the orders, and on margins, all continuous in $b$. Its one limit argument
($u^\epsilon\rightharpoonup u$) extracts a solution from an estimate that is already uniform. Strong uniqueness (II.F
section 7.4) is qualitative. Finite-time solvability (II.F section 7.5) uses II.E Propositions 3.4 and 4.3, whose
constants are uniform for $\epsilon_P$ small: on a slab (bounded $t_*$), $2L_b-2L_{b_0}$ is such a perturbation of
$2L_{b_0}$, its coefficients being $O(|b-b_0|)$ times $\rho^2,\rho^3,\rho^4$ near infinity (III.F Lemma 2.1 (3)) and the
weights at $\iota^+$ and $K^+$ being bounded above and below there. So II.F Proposition 7.4 holds with $\tau_0$ and $C$
uniform on $\bar{\mathcal B}_*$.

(c) *Section 8.* Step 0 uses II.E Proposition 4.3 on a slab, uniform as in (b). Steps 1 and 3 use II.F Proposition 7.4,
uniform by (b). Step 2 uses the 2-admissibility estimate (II.F (8.6)), uniform by Theorem 2.1, and Lemmas 1.3-1.4, which
are qualitative. Step 4 sums the bounds. So (8.2) holds with $C_k$ independent of $b$. $\square$

## 4. II.F$'$ Theorem 1.1 uniformly in $b$ ((F$'$11) for the family $2L_b$)

**Theorem 4.1.** Let $\alpha_I$, $\alpha_+$, $\ell_I$, $\ell_+$, $\ell_K$ be as in II.F$'$ Theorem 1.1, with $\aleph =
2$, $\delta = 0$ and the order $\mathsf s$ of (B4). There are $\epsilon_0>0$ and $d\in\mathbb N$ such that for every
$b\in\bar{\mathcal B}_*$ the conclusions of II.F$'$ Theorem 1.1 and Corollary 1.2 hold with $P_0 := 2L_b$ (with II.F$'$
Remark 7.1 for margin 1), with $\epsilon_0$, $d$ and $C_k$ independent of $b$. Moreover, for $k\ge1$: let $b_j\to b$ in
$\bar{\mathcal B}_*$, let $P_j$ be admissible relative to $2L_{b_j}$ of class $((0;k+d),(2\ell_I,\ell_+,\ell_K))$ with
$\|P_j-2L_{b_j}\|_{(0;d)}<\epsilon_0$ and $\|P_j-2L_{b_j}\|_{(0;k+d)}$ bounded, with coefficients converging in $C^2$ on
compact subsets of $M^\circ\cap\{r>r_0\}$ to those of $P$, admissible relative to $2L_b$, and let $f_j\to f$ in (1.4) of
II.F$'$. Then the forward solutions converge in $H^{k-1,(\alpha_I-\varsigma,\alpha_+-\varsigma,-2-\varsigma)}_{\mathrm
b}(\Omega_*;E)^{\bullet,-}$ for every $\varsigma>0$.

*Proof.* II.F$'$'s proof depends on $P_0$ only through the following inputs:

(i) II.E Theorem 6.1 and II.E Propositions 3.4, 4.3 and 4.4 (II.F$'$ section 3.1). Theorem 6.1 is uniform over the
stationary models of nearby parameters (its last sentence). The slab propositions are uniform as in Theorem 3.1 (b).

(ii) The thresholds of II.F$'$ Lemma 2.1 and of II.C Lemmas 3.2 and 3.7, which are continuous in the coefficients.

(iii) The orders (II.F$'$ section 2.3), fixed by (B4).

(iv) II.F Theorem 8.1 with Remark 8.2, uniform by Theorem 3.1.

(v) The 2-admissibility estimate II.C (2.2), uniform by Theorem 2.1.

Every other constant depends on $P$ only through $\epsilon_0$ (II.F$'$ section 3.1, last sentence). So $\epsilon_0$, $d$
and $C_k$ can be chosen independent of $b\in\bar{\mathcal B}_*$. *Continuity.* The proof in II.F$'$ section 6, with
$P^{(j)} := P_j$ relative to $2L_{b_j}$: by the first part the $u_j$ are bounded in
$H^{k,(\alpha_I,\alpha_+,-2)}_{\mathrm b}$ uniformly in $j$. A weak limit point $\tilde u$ satisfies $P\tilde u = f$, by
the $C^2$ convergence of the coefficients on compact sets. II.F$'$ Lemma 2.2 (uniqueness, qualitative) gives $\tilde u =
u$, and II.F$'$ Lemma 6.1 gives norm convergence. $\square$

The source states its Theorem 11.1 for $P_0$ near an admissible $P_1$ among all small stationary perturbations as well.
That wider statement is not proved here and is not used; Part III uses only the family $2L_b$ ((H$''$3)).

## 5. Consequences

**Corollary 5.1 ([Hin26] Theorem 11.12 at n = 4, near $b_0$).** III.I Theorem 5.3 holds for every $b\in\mathcal B_*$ in
place of $b_0$. With $g_0 := g_{b_0,b,-S}$, $g := g_0+h$ and the forward solution $u$ of $L^{g,g_0}u = f$, (5.1)-(5.2)
of III.I hold with $\epsilon_0$, $d$ and $C_k$ independent of $b$. For $k\ge1$, $u$ depends continuously on $(b,S,h)$ in
$H^{k-1,(\beta_I-\varsigma,\beta_+-\varsigma,-\frac32-\varsigma)}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-}$, for every
$\varsigma>0$.

*Proof.* III.I's proof of Theorem 5.3, with $P_0 := 2L_b$ and Theorem 4.1 in place of II.F$'$ Theorem 1.1. Its
hypothesis (i) is Theorem 2.1. (ii) is unchanged, as $\bar S$ and $\bar A$ do not depend on $b$. (iii) is III.I
Corollary 5.2, which is stated for $g_0 = g_{b_0,b,-S}$ and $P_0 = 2L_b$ and whose hypothesis is now Theorem 2.1, with
$\|P-2L_b\|_{(0;d)}\le C(|b-b_0|+|S|+\|h\|_{\mathcal X^{d+5}})$ by III.I Proposition 3.4, (3.7), small by (B4).
*Continuity.* Theorem 4.1, as $2L^{g,g_0}$ depends smoothly on $(b,S)$ and continuously on $h$ in the norm of III.I
(3.7) (III.I Lemma 3.6). $\square$

This removes (I3) of III.I and the restriction of III.I Remark 5.4. The source's continuity is in $(b_0,b,S,h)$; here
$b_0$ is fixed ((H$''$4)).

## 6. Findings, labels and sources

(H$''$1) *Strong trapping admissibility near $b_0$ needs no special frame.* Along null bicharacteristics, $e_0 =
\zeta/\sigma$ is parallel and the null filtration is invariant, so in the frame $(e_0,V,e_2)$ of Proposition 1.1 the
connection is a screen rotation plus a part that lowers the grading. III.F's computation then holds at every $b$ for
which $E^\Upsilon$ vanishes near $\Gamma_b$, $c_C$ is past timelike and $dt_*$ is timelike there. The source computes in
Marck's tetrad ([Hin26] pp. 147-149). Multiplying the inner product by $f_b$ removes the density correction exactly
(Step 5).

(H$''$2) *$N_{\iota^+}(2L_b)$ does not depend on $b$* (Lemma 3.2), so II.F sections 1-6 hold for every $b$ with the same
constants.

(H$''$3) *(F$'$11) is discharged for the family $2L_b$, $b\in\bar{\mathcal B}_*$* (Theorems 3.1 and 4.1). The source's
wider uniformity, over all small stationary perturbations of an admissible $P_1$, is not proved and not used.

(H$''$4) *Continuity in $b$* (Theorem 4.1, Corollary 5.1) follows from the uniform constants by II.F$'$ section 6's
argument.

(H$''$5) *What (J$'$3) still needs.* By Corollary 5.1, III.I Theorem 5.3 holds at every $b\in\mathcal B_*$, uniformly.
The parts III.I$'$-III.I$''''''''''''''$ and III.J-III.J$'''$ were written with $b = b_0$, and use data at $b_0$ in
three ways. (a) At $b_0$ every rotation in $\mathcal V_1$ is Killing, so $h_{b_0,\mathrm v1}(V) = 0$ and $\mathcal
W_{\mathrm v1} = 0$ (III.I$'''''''''$ section 1, which defines $\mathcal W_{\mathrm v1}$ in general as a complement of
the Killing rotations; III.I$''''''''''$ section 1 and Lemma 2.1; III.I$'''''''''''$ Lemma 2.3). At $b\ne b_0$ the
non-Killing rotations give v1-rows, whose dual states are those of III.E$'$, as in the source. (b) The index sets of the
zero energy states are fixed at $b_0$ (III.D$''$ Proposition 3.1, III.D$'''$ Proposition 3.1, III.F$'''$ Proposition
2.2; used in III.I$''''$, III.I$'''''''$, III.I$''''''''$, III.I$'''''''''$). (c) Derivatives in $b$ are taken at $b_0$
(III.I$'''''''$). The $\iota^+$-data of III.G-III.G$''''$ depend only on $N_{\iota^+}$, hence not on $b$ (Lemma 3.2).
Writing that chain at base points $b\in\mathcal B_*$ is the remainder of (J$'$3).

*Labels.* Proposition 1.1 is the source's Proposition 8.3 on $\mathcal B_*$, by a different frame; Theorem 2.1 its
Theorem 10.1 near $b_0$ for every $k$; Theorems 3.1 and 4.1 [Hin26c] Theorems 10.1 and 11.1 uniformly over the family
$2L_b$; Corollary 5.1 the source's Theorem 11.12 near $b_0$. Corollary 1.2 and Lemma 3.2 are new at $n = 4$.

*Sources.* [Hin26] pp. 147-149 (Proposition 8.3 and its proof, with footnote 77) and pp. 225-226 (Theorem 11.12, with
continuity in $(b_0,b,S,h)$), read at source. [Hin17] Proposition 4.1 (as cited in III.F). Inputs: I.A Theorems 7.2 and
8.1; I.B (1.4), Theorem 1.3 and sections 6 and 9; II.B Lemma 1.1; II.C Definition 2.7, Lemmas 3.2 and 3.7, Proposition
5.1; II.E Theorem 6.1, Propositions 3.4, 4.3 and 4.4; II.F (1.4), Definitions 1.1 and 7.1, Lemmas 1.3, 1.4, 7.2 and 7.6,
Propositions 3.1, 5.1, 6.2 and 7.4, Theorem 8.1, Remark 8.2; II.F$'$ Theorem 1.1, Corollary 1.2, Lemmas 2.1, 2.2 and
6.1, sections 2.3 and 3.1, Remark 7.1; III.B Lemma 3.7; III.D section 1, section 5.2, Lemma 5.2; III.E Theorem 1.1;
III.E$'$; III.F section 1, Lemma 2.1, (4.1)-(4.2), Proposition 4.1; III.F$'$ Proposition 3.3; III.H Theorem 4.1,
Corollaries 4.2-4.4, Remark 2.6, Lemma 5.2; III.H$'$ Definition 1.1, Lemma 1.2, sections 2-7, Theorem 1.3; III.I
Proposition 3.4, Lemmas 3.6 and 5.1, Corollary 5.2, Theorem 5.3, Remark 5.4.
