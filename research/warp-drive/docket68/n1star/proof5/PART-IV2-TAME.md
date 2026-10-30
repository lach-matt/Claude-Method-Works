# Part IV$'$. Exterior estimates II: the tensor operator in edge-b form and the tame energy estimate, n = 4 ([Hin23a]
sections 3.4-3.5)

*Status.* Written (D303). This part carries [Hin23a] sections 3.4-3.5 (Proposition 3.29, Lemmas 3.33-3.34, Proposition
3.32) to [Hin26]'s gauge-fixed operator at $n = 4$ on III.C's exterior region. Section 1 puts the conjugated operator in
edge-b form; at $n = 4$ its first-order matrix is the constant $\bar A$ of III.C Lemma 4.2, free of the perturbation $h$
(N1STAR-PROOF.md 10.64 (e), III.C Remark 4.5). Section 2 proves the energy estimate for the system, with the tame
estimate and the sharp weights. The source's section 3.3 (metric perturbations, Lemmas 3.23-3.28) is III.C sections 2-5
at $n = 4$, which this part uses as it stands. Source: [Hin23a] pp. 18-30, read at source. Amended D309: verifier 133's
findings seated (C-m1: the norms of $h$ are the polyhomogeneous ones; C-n1 to C-n3).

## 0. Setting

$U$, $M_\sharp$, $x_I = \rho_I^{1/2}$, $X_0$, $X_I$, $\mathcal V_{\mathrm{e,b}}$ and the spaces are those of Part IV
(PART-IV-EB.md) section 0, and the splitting (1.6), the slots and $\bar A$ are III.C's (Lemma 4.2). The weights at
$\mathscr I^+$ are listed in powers of $\rho_I$, as in III.C, unless they are written with $x_I$. Let
$g_1,g_0\in\mathcal G$ (III.C Definition 3.4), $k\ge5$, and $h\in H^{k,(\mathcal E_0,\ell_0),(\mathcal
F,\ell_I)}_{\mathrm b}(U;S^2T^*)$ as in III.C Proposition 4.4. That is: $\min\mathrm{Re}\,\mathcal E_0>0$,
$\min\mathrm{Re}\,\mathcal F>0$, $2\mathcal F\subset\mathcal F$, $\ell_0,\ell_I>0$, and $h$ small in $H^{k,(\mathcal
E_0,\ell_0),(\mathcal F,\ell_I)}_{\mathrm b}$, the polyhomogeneous norm. (The coefficients $\tilde a$ below lie in
$\rho_I^{-1}$ times terms in $h$, whose size near $\mathscr I^+$ the conormal norm $H^{k,a_0,a_I}_{\mathrm b}$ does not
control when $a_I<1$; verifier 133's C-m1, amended D309.) Assume moreover
$$\min\mathrm{Re}\,\mathcal F>1,\qquad\ell_I>1,\tag{0.1}$$
which holds for $\mathcal F = \mathcal E^{\mathrm{tot}}_I$ ($\min\mathrm{Re} = \frac32$, III.C Remark 4.5) and
$\ell_I>\frac32$ (III.C$'$ Theorem 3.1), and for $\mathcal F = (2,0)$. Put $g := g_1+h$ and
$$L_g := 2\rho_I\rho^{-7/2}\,L^{g,g_0}\,\rho^{3/2},\tag{0.2}$$
with $L^{g,g_0}$ the linearised gauge-fixed operator of III.C (4.1), whose principal part is
$\frac12\Box_g\otimes\mathrm{Id}$. For the scalar operator this is Part IV's $L$, up to the factor 2: $2L^{g,g_0}$ has
principal part $\Box_g$.

## 1. The operator in edge-b form ([Hin23a] Proposition 3.29 for [Hin26]'s operator at n = 4)

**Lemma 1.1 (Cartesian derivatives are $\rho_0$ times eb-vector fields).** On $U$, $\partial_t$, $\partial_{x^i}$,
$\partial_0$, $\partial_1$ lie in $\rho_0\mathcal V_{\mathrm{e,b}}(M_\sharp)$, and
$|x|^{-1}\partial_\omega\in\rho_0x_I\mathcal V_{\mathrm{e,b}}(M_\sharp)$.

*Proof.* By III.C (1.5), $\partial_0 = -\frac12\rho_0\rho_IX_I$ and $\partial_1 = \rho_0(X_0-X_I+\frac12\rho_IX_I)$;
$X_0,X_I\in\mathcal V_{\mathrm{e,b}}$. And $|x|^{-1}\partial_\omega = \rho_0x_I\cdot x_I\partial_\omega$, with
$x_I\partial_\omega\in\mathcal V_{\mathrm{e,b}}$. $\partial_t = \partial_0+\partial_1$ and $\partial_{x^i} =
\omega^i(\partial_0-\partial_1)+|x|^{-1}(\ldots)\partial_\omega$, the dots smooth functions of $\omega$. $\square$

This refines III.C Lemma 1.1, which places the same fields in $\rho_0\mathcal V_{\mathrm b}$. The refinement is what the
edge-b form needs: angular second derivatives come with $|x|^{-2}$, hence with $\rho_0^2x_I^2$ times eb-derivatives.

**Proposition 1.2 (the edge-b form).** Under section 0's hypotheses, on $U$, in the splitting (1.6),
$$L_g = -2\big(X_I-\bar A\big)(X_0-X_I)+x_I^2\slashed\Delta+\tilde L_g,\qquad\tilde
L_g\in\Big(x_IC^\infty(M_\sharp)+H^{k-2,(\mathcal E_0,\ell_0),(\mathcal F-1,\ell_I-1)}_{\mathrm
b}\Big)\mathrm{Diff}^2_{\mathrm{e,b}}(M_\sharp;S^2T^*),\tag{1.1}$$
where $\slashed\Delta = -\slashed g^{ab}\partial_a\partial_b$ acts on each slot, in local coordinates $\omega^a$ of
$\mathbb S^3$. By (0.1) the coefficients of the second class decay at $\mathscr I^+$ at least like
$\rho_I^{\min(\min\mathrm{Re}\,\mathcal F-1,\ell_I-1)-}$ and are small in $L^\infty$ near $\mathscr I^+$ for $h$ small.
So $\tilde L_g$ is small relative to the leading part near $\mathscr I^+$, as the source's (3.29b) is.

*Proof.* *The conjugation.* By III.C Proposition 4.4,
$$L^{g,g_0} = -\rho_0^2\rho_I\big(X_I-\tfrac32-\bar A\big)(X_0-X_I)+R,\qquad
R\in\big(\rho_0^2\rho_I^2C^\infty+H^{k-2,(\mathcal E_0+2,\ell_0+2),(\mathcal F,\ell_I)}_{\mathrm
b}\big)\mathrm{Diff}^2_{\mathrm b}.$$
As $(X_0-X_I)\rho = 0$ and $X_I\rho^{3/2} = \frac32\rho^{3/2}$, we have $\rho^{-3/2}(X_I-\frac32-\bar
A)(X_0-X_I)\rho^{3/2} = (X_I-\bar A)(X_0-X_I)$. And $2\rho_I\rho^{-7/2}\cdot\rho_0^2\rho_I\cdot\rho^{3/2} = 2$. So the
leading part of (1.1) is the image of (4.4)'s, and $L_g-(-2(X_I-\bar A)(X_0-X_I)) =
2\rho_0^{-2}\rho_I^{-1}\rho^{-3/2}R\rho^{3/2}$. Conjugation by $\rho^{3/2}$ preserves $\mathrm{Diff}_{\mathrm b}$ and
$\mathrm{Diff}_{\mathrm{e,b}}$, as $\rho^{-3/2}V\rho^{3/2} = V+\frac32V(\log\rho)$ with $V\log\rho$ smooth for
$V\in\mathcal V_{\mathrm b}$.

*The b-form remainder is not enough.* $\rho_0^{-2}\rho_I^{-1}R$ lies in $(\rho_IC^\infty+H^{k-2,(\mathcal
E_0,\ell_0),(\mathcal F-1,\ell_I-1)}_{\mathrm b})\mathrm{Diff}^2_{\mathrm b}$. But $\mathrm{Diff}^2_{\mathrm b}\subset
x_I^{-2}\mathrm{Diff}^2_{\mathrm{e,b}}$ only, $\partial_\omega$ being $x_I^{-1}$ times an eb-vector field. So we redo
the count of III.C Proposition 4.4's proof with Lemma 1.1 in place of III.C Lemma 1.1.

*The background part.* $L^{g_1,g_0}$ differs from $L_{b_0} := L^{g_{b_0},g_{b_0}}$ by terms with a factor $g_1-g_{b_0}$
or $g_0-g_{b_0}$ in $\rho_0^2\rho_I^2C^\infty$ (III.C Definition 3.4, Lemma 3.5). By Lemma 4.3 of III.C and Lemma 1.1,
these lie in $\rho_0^2\cdot\rho_0^2\rho_I^2C^\infty\mathrm{Diff}^2_{\mathrm{e,b}}$. After the prefactor
$2\rho_0^{-2}\rho_I^{-1}$ this is $\rho_0^2\rho_IC^\infty\mathrm{Diff}^2_{\mathrm{e,b}}\subset
x_I^2\mathrm{Diff}^2_{\mathrm{e,b}}$. For $L_{b_0}$ itself: - Its second-order part is $\frac12\Box_{g_{b_0}}$ on each
component in the frame, the principal symbol being scalar. - Its first-order part consists of the connection terms of
the frame and the terms of $E_C$, $E_\Upsilon$. These are Cartesian derivatives (in $\rho_0\mathcal V_{\mathrm{e,b}}$,
Lemma 1.1) times coefficients in $\rho C^\infty = \rho_0\rho_IC^\infty$ ($c_C$, $c_\Upsilon$ and the Christoffel symbols
of $\eta$ in the frame are $O(|x|^{-1})$, III.B Definition 6.1, III.C Lemma 1.3), so they lie in
$\rho_0^2\rho_IC^\infty\mathrm{Diff}^1_{\mathrm{e,b}}$. - Its zeroth-order part lies in $\rho^2C^\infty$.

III.C Lemma 4.1's computation identifies the part of the first-order terms that is not $O(\rho_I)$ relative: it is
$\rho_0^2\rho_I\bar A(X_0-X_I)$ (with the $-\frac32$ of the scalar conjugation). So, after conjugation and the prefactor,
$$L_{b_0,\mathrm{conj}} = \big(2\rho_I\rho^{-7/2}\tfrac12\Box_{g_{b_0}}\rho^{3/2}\big)\otimes\mathrm{Id}+2\bar
A(X_0-X_I)+x_IC^\infty\mathrm{Diff}^1_{\mathrm{e,b}}+x_I^2C^\infty.$$
The scalar term is Part IV Lemma 2.2's $L$: $-2X_I(X_0-X_I)+x_I^2(\slashed\Delta+\frac34)$ modulo
$x_I\mathrm{Diff}^2_{\mathrm{e,b}}$. Its first-order part in Lemma 2.2 is that of the scalar wave operator, and it
differs from the frame's by the connection terms just counted. $x_I^2\cdot\frac34$ and
$x_IC^\infty\mathrm{Diff}^1_{\mathrm{e,b}}$ (the angular connection terms) lie in $x_I\mathrm{Diff}^1_{\mathrm{e,b}}$.
So the background part of (1.1) holds with $\tilde L$ in $x_IC^\infty\mathrm{Diff}^2_{\mathrm{e,b}}$.

*The perturbation.* For $(g_1+h,g_0)$ against $(g_1,g_0)$ the factor is $\delta = h$. By III.C Lemma 4.3 and Lemma 1.1,
each term is $\rho_0^2$ times a product of $h$ or $\mathcal V_{\mathrm b}$-derivatives of $h$ of order at most 2 with
smooth bounded functions, applied through $\mathrm{Diff}^2_{\mathrm{e,b}}$ (Lemma 1.1 replaces $\rho_0\mathcal
V_{\mathrm b}$ by $\rho_0\mathcal V_{\mathrm{e,b}}$ for the derivatives acting on $u$). By III.C Proposition 4.4's proof
(the Neumann series and Lemma 2.1 there), the coefficients lie in $\rho_0^2H^{k-2,(\mathcal E_0,\ell_0),(\mathcal
F,\ell_I)}_{\mathrm b} = H^{k-2,(\mathcal E_0+2,\ell_0+2),(\mathcal F,\ell_I)}_{\mathrm b}$. After the prefactor they
are in $H^{k-2,(\mathcal E_0,\ell_0),(\mathcal F-1,\ell_I-1)}_{\mathrm b}$, multiplying
$\mathrm{Diff}^2_{\mathrm{e,b}}$. The frame change of III.C Lemma 1.3 preserves the classes, as in III.C Proposition
4.4's proof.

*Smallness.* By (0.1) and the Sobolev embedding (0.1) of Part IV ($k-2\ge3$), elements of $H^{k-2,(\mathcal
E_0,\ell_0),(\mathcal F-1,\ell_I-1)}_{\mathrm b}$ are bounded by $C\rho_0^{\min(\min\mathrm{Re}\,\mathcal
E_0,\ell_0)}\rho_I^{\min(\min\mathrm{Re}\,\mathcal F-1,\ell_I-1)-}$ times their norm, which is $O(\|h\|_{H^{k}})$.
$\square$

*Remark 1.3 (the source's $A_g$ and $B_g$).* In [Hin23a] (3.29a) the $h$-dependent entries of $A_g$ and the term $B_g$
are of the size of the leading part at $\mathscr I^+$; at $n = 3$ they are bounded there. At $n = 4$ they carry an extra
$\rho_I^{1/2}$ (10.64 X7, III.C Remark 4.5) and lie in $\tilde L_g$. So the first-order matrix of (1.1) is $\bar A$,
constant, lower triangular with diagonal (4.3) of III.C, all entries $\ge0$:
$$2(1-v_C)\gamma_C,\ (1-v_C)\gamma_C,\ (1-e_C)(1-v_C)\gamma_C,\ (1-e_\Upsilon)\gamma_\Upsilon,\ \gamma_\Upsilon,\ 0,\
2\gamma_\Upsilon.$$
The source's term $A^0_h$, for which its proof uses Lemma 3.33, does not arise (10.64 (g)).

## 2. The energy estimate for the system ([Hin23a] Proposition 3.32 at n = 4)

**Lemma 2.1 (a fibre inner product; the source's "sharp weights").** For every $\epsilon>0$ there is a constant positive
definite inner product $\langle\cdot,\cdot\rangle_\epsilon$ on the fibres of $S^2T^*$, in the frame (1.6), such that
$$\bar A = D+N_\epsilon,\qquad D =
\mathrm{diag}(d_1,\dots,d_7)\otimes\mathrm{Id}_{\mathrm{slot}},\qquad|N_\epsilon|_\epsilon\le\epsilon,$$
with the diagonal of III.C (4.3), $d_j\ge0$, and $D$ self-adjoint for $\langle\cdot,\cdot\rangle_\epsilon$.

*Proof.* Take the slots of (1.6) orthogonal, each with its standard inner product scaled by $\epsilon^{-2j}$ on slot
$j$. $\bar A$ maps each slot to slots of the same type by scalars and is lower triangular (III.C Lemma 4.2). An entry
$\bar A_{ji}$, $i<j$, then has norm $\epsilon^{j-i}|\bar A_{ji}|$ in the scaled norms. For $\epsilon$ small this is at
most $\epsilon\max|\bar A_{ji}|$; rename $\epsilon$. $\square$

**Proposition 2.2 (the energy estimate and its tame form; [Hin23a] Proposition 3.32 at n = 4).** Let $\Omega$,
$\Sigma_{\mathrm{in}}$, $\Sigma_{\mathrm{fin}}$ be as in Part IV section 3, and $\alpha_0,\alpha_I\in\mathbb R$ with
$\alpha_I<\min(\alpha_0,0)$. Let $k\ge8$ and $3\le m\le k-3$, and let $h$ be as in section 0, small in
$H^{8,(\mathcal E_0,\ell_0),(\mathcal F,\ell_I)}_{\mathrm b}$. For $f\in H^{m,(\alpha_0,2\alpha_I)}_{\mathrm
b}(\Omega;S^2T^*)$ vanishing near $\Sigma_{\mathrm{in}}$, the forward solution $u$ of $L_gu = f$ lies in
$H^{(1;m),(\alpha_0,2\alpha_I)}_{\mathrm{e,b;b}}(\Omega;S^2T^*)$, and
$$\|u\|_{H^{(1;m),(\alpha_0,2\alpha_I)}_{\mathrm{e,b;b}}}\le C\Big(\|f\|_{H^{m,(\alpha_0,2\alpha_I)}_{\mathrm
b}}+\|h\|_{H^{m+3,(\mathcal E_0,\ell_0),(\mathcal F,\ell_I)}_{\mathrm b}}\|f\|_{H^{3,(\alpha_0,2\alpha_I)}_{\mathrm
b}}\Big),\tag{2.1}$$
with $C$ depending on $m$, $k$, $\alpha_0$, $\alpha_I$ and the classes, not on $f$ or $h$.

*Proof.* *The basic estimate.* Use the multiplier $W = w^2V$ of Part IV Proposition 3.1, $V = X_0-(1+\kappa)X_I$, with
$\kappa>0$ to be fixed, the density $\bar\mu_{\mathrm b}$, and the fibre inner product of Lemma 2.1. Then
$$2\,\mathrm{Re}\langle wL_gu,wVu\rangle = \langle Qu,u\rangle+\mathcal B_{\mathrm{fin}}(u),\qquad Q =
[L_g,W]-(\mathrm{div}W)L_g+(L_g^*-L_g)W,$$
with $\mathcal B_{\mathrm{fin}}\ge0$, as in Part IV. The scalar part $-2X_I(X_0-X_I)+x_I^2\slashed\Delta$ gives $\bar Q$
of Part IV (3.3); the constant $\frac34$ is absent here, and only increased $\bar Q$ there. Write
$$Y := w(X_0-X_I)u,\qquad Z := wX_Iu,\qquad Vu = w^{-1}(Y-\kappa Z).$$
The first-order term $2\bar A(X_0-X_I)$ of (1.1) contributes, up to terms of order 0 in $u$ and terms with a factor
$x_I$,
$$4\,\mathrm{Re}\langle\bar AY,Y-\kappa Z\rangle = 4\langle DY,Y\rangle-4\kappa\,\mathrm{Re}\langle
DY,Z\rangle+O(\epsilon)(|Y|^2+|Z|^2).$$
On each slot, the quadratic form in $(Y_j,Z_j)$ from $\bar Q$ and this term is
$$4(d_j-\alpha_I)|Y_j|^2-4\kappa d_j\,\mathrm{Re}(Y_j\bar Z_j)+4\kappa(\alpha_0-\alpha_I)|Z_j|^2.$$
It is positive definite if $4(d_j-\alpha_I)(\alpha_0-\alpha_I)>\kappa d_j^2$. As $d_j\ge0$, $\alpha_I<0$ and
$\alpha_0>\alpha_I$, this holds for $\kappa>0$ small. Fix such $\kappa$, then $\epsilon$ small. The angular term of
$\bar Q$, $(1+2(\alpha_0-\alpha_I)+\kappa(1-2\alpha_I))x_I^2|\slashed\nabla u|^2$, is positive, so $\langle Qu,u\rangle$
controls $\|wu\|^2_{H^1_{\mathrm{e,b}}}$ modulo: - $\|wu\|^2_{L^2_{\mathrm b}}$, removed by Part IV's Poincaré
inequality; - the contribution of $\tilde L_g$, whose coefficients are $O(c^{\min(2\min\mathrm{Re}\,\mathcal
F-2,2\ell_I-2)-})$ on $\{x_I<c\}$ by Proposition 1.2's smallness and are absorbed for $c$ small, as in Part IV.

The term $(L_g^*-L_g)W$ is that of the first-order part, already counted, plus that of $\tilde L_g$. This gives
$$\|u\|_{H^{1,(\alpha_0,2\alpha_I)}_{\mathrm{e,b}}}\le C_0\|L_gu\|_{H^{0,(\alpha_0,2\alpha_I)}_{\mathrm b}},\tag{2.2}$$
with $C_0$ uniform for $h$ small in $H^{5,(\mathcal E_0,\ell_0),(\mathcal F,\ell_I)}_{\mathrm b}$ (the source's (3.53);
the skew part needs $\tilde a\in W^{1,\infty}$, so $h\in H^6$, which the $H^8$ hypothesis gives). Away from $\mathscr
I^+$, Part IV Proposition 4.1's argument applies to the system: the principal part is scalar, and the first-order terms
are bounded b-operators, absorbed by the exponential weight. Remark 4.2 there glues the pieces.

*Commuting.* With $X_0$, $X_1 := X_I$, the rotation fields $X_2,\dots,X_7$ of $\mathbb S^3$ (acting on the slots in the
frame (1.6), which they preserve: III.C Lemma 4.2's equivariance) and $X_8 := 1$, apply (2.2) to $X_{j_1}\cdots
X_{j_l}u$, $l\le m$. Lemma 2.4 below (the source's Lemma 3.34) gives
$$\|u\|_{H^{(1;m)}_{\mathrm{e,b;b}}}\le C_0\Big(\|L_gu\|_{H^m_{\mathrm b}}+\sum_{q\le l\le m}\|(\mathrm{ad}^q_{\mathcal
X}L_g)\mathcal X^{l-q}u\|_{H^0_{\mathrm b}}\Big)\tag{2.3}$$
(the source's (3.55); weights $(\alpha_0,2\alpha_I)$ throughout). The commutators of the $X_j$ with the leading part of
(1.1) lie in $x_I\mathrm{Diff}^{1,1}_{\mathrm{e,b;b}}$: for the scalar part by Part IV Lemma 2.2, and $\bar A$ is
constant and commutes with the $X_j$ ($X_0$, $X_I$ act on the slot coordinates, and the rotations commute with $\bar A$
by III.C Lemma 4.2's equivariance). These terms are absorbed for $x_I$ small. For $\tilde L_g = \sum_i(x_Ia_i+\tilde
a_i)P_i$, with $a_i\in C^\infty$, $\tilde a_i\in H^{k-2,(\mathcal E_0,\ell_0),(\mathcal F-1,\ell_I-1)}_{\mathrm b}$ and
$P_i$ spanning $\mathrm{Diff}^2_{\mathrm{e,b}}$, the source's (3.56)-(3.58) apply verbatim: - the $x_Ia_i$-terms are
absorbed; - the $\tilde a_i$-terms are bounded by the Moser estimate (Lemma 2.3), with
$$\|(\mathcal L^q_{\mathrm b}\tilde a)\mathcal L^1_{\mathrm{e,b}}\mathcal L^{m-q+1}_{\mathrm b}u\|\le C\big(\|\tilde
a\|_{H^4}\|u\|_{H^{(1;m)}}+\|\tilde a\|_{H^{m+1}}\|u\|_{H^{(1;3)}}\big).$$

The first term is absorbed near $\mathscr I^+$, the coefficients decaying at $\mathscr I^+$; the second is bounded by
$\|h\|_{H^{m+3}}$ times (2.2) at $m = 3$, by $\|\tilde a_i\|_{H^{m+1}}\le C\|h\|_{H^{m+3}}$ (the coefficients are
rational in at most two b-derivatives of $h$). Commutators of the $X_j$ preserve $\mathrm{Diff}^k_{\mathrm{e,b}}$: for
$X_0$, $X_I$ as eb-vector fields, and for the rotations by Part IV (2.3)'s argument, the source's (3.19a)-(3.19b). This
proves (2.1). At $m = 3$ the constant depends on $\|h\|_{H^{8}}$, the source's (3.54). $\square$

**Lemma 2.3 (Moser estimates on $M_\sharp$).** For $s\ge3>\frac52 = \frac12\dim M_\sharp$ and $a,b$ in the weighted
b-Sobolev spaces,
$$\|ab\|_{H^{s,(\beta_0+\gamma_0,\beta_1+\gamma_1)}_{\mathrm b}}\le
C\big(\|a\|_{\rho_0^{\beta_0}x_I^{\beta_1}L^\infty}\|b\|_{H^{s,(\gamma_0,\gamma_1)}_{\mathrm
b}}+\|a\|_{H^{s,(\beta_0,\beta_1)}_{\mathrm b}}\|b\|_{\rho_0^{\gamma_0}x_I^{\gamma_1}L^\infty}\big),$$
and $H^{s}_{\mathrm b}$ embeds in $L^\infty$ (Part IV (0.1)).

*Proof.* In the coordinates $z_0 = \log\rho_0$, $z_1 = \log x_I$, b-Sobolev spaces are uniformly local Sobolev spaces on
$\mathbb R^2\times\mathbb S^3$ (dimension 5), and weights become exponentials. The estimate is the standard Moser
estimate there ([Tay11], chapter 13, Propositions 3.6-3.7, as the source cites them), applied to the products after
dividing out the weights. $\square$

**Lemma 2.4 (the source's Lemma 3.34, the commutator identity).** In any algebra, for $L,X_1,\dots,X_N$,
$$[L,X_1\cdots X_N] =
\sum_{q=1}^N(-1)^{q-1}\sum_{i_1<\dots<i_q}\big(\mathrm{ad}_{X_{i_1}}\cdots\mathrm{ad}_{X_{i_q}}L\big)\prod_{j\ne
i_1,\dots,i_q}X_j,\qquad\mathrm{ad}_X := [-,X].$$

*Proof.* Induction on $N$: $[L,X_1\cdots X_{N+1}] = [L,X_1\cdots X_N]X_{N+1}+[L,X_{N+1}]X_1\cdots
X_N-[\mathrm{ad}_{X_{N+1}}L,X_1\cdots X_N]$. $\square$

*Remark 2.5 (Lemma 3.33 of the source).* The source's tame product estimate, with $d_{\dim M-1}$, is used only for
$A^0_h$, which does not arise at $n = 4$ (Remark 1.3). For the record, its dimension count at $n = 4$ is $d_4 = 3$
(10.64 X6).

## 3. Findings and sources

(IV$'$1) *The edge-b form needs the refined count.* III.C's b-form (4.4) places the perturbation in
$H^{k-2}\mathrm{Diff}^2_{\mathrm b}$, which loses $x_I^{-2}$ against $\mathrm{Diff}^2_{\mathrm{e,b}}$ in the angular
directions. Redone with Lemma 1.1, the count gives (1.1). III.C's sentence "the edge-b form (5.26b) is in III.C$'$" is
not borne out by III.C$'$, which works in the b-form only; (1.1) is that form.

(IV$'$2) *h-free first-order matrix.* At $n = 4$ the first-order matrix is the constant $\bar A$ (Remark 1.3). Its
diagonal is $\ge0$, so the source's sharp-weight condition $\alpha_I<\min(\alpha_0,0)$ suffices, with $\kappa$ small
depending on the diagonal (Proposition 2.2's proof). The source takes $\kappa = 1$ and $\alpha_I$ large and negative for
the basic estimate, then argues the sharp weights separately; here both are one argument.

*Labels.* Lemma 1.1 refines III.C Lemma 1.1. Proposition 1.2 is the source's Proposition 3.29 for [Hin26]'s operator
(its (5.26b)), Lemma 2.1 the fibre inner product of the source's sharp-weight step, Proposition 2.2 its Proposition
3.32, Lemma 2.3 its use of [Tay11], Lemma 2.4 its Lemma 3.34, and Remark 2.5 its Lemma 3.33.

*Sources.* [Hin23a] pp. 18-30 (Definition 3.27, Lemma 3.28, Proposition 3.29 with (3.30)-(3.46), Definition 3.30,
Corollary 3.31, Proposition 3.32 with (3.50)-(3.58), Lemmas 3.33-3.34), read at source. Inputs: Part IV (PART-IV-EB.md)
sections 0-4; III.B Definition 6.1; III.C Lemmas 1.1, 1.3, 2.1, 3.5, 4.1-4.3, Definition 3.4, Proposition 4.4, Remark
4.5; III.C$'$ Theorem 3.1; N1STAR-PROOF.md 10.64 (X6, X7, (e), (g)).
