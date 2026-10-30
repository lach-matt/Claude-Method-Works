# Part VIII: linear stability of the Schwarzschild-Tangherlini metric, n = 4 (III.K linearised at Tangherlini)

*Status.* Written (D334); to be read.

This part proves the linear stability of five-dimensional Schwarzschild-Tangherlini $g_{b_0}$, $b_0 = (\mu_0,0)$, in
the gauge of the nonlinear problem. Every solution $(\dot\gamma,\dot k)$ of the linearised constraint equations in
Hintz's data class has a linearised vacuum development $\dot g$ in the generalised wave gauge of III.K. Up to a
linearised boost, $\dot g$ induces $(\dot\gamma,\dot k)$, and where $\chi_K = 1$ it differs from a linearised
Myers-Perry metric $\partial_bg_b(\dot b)$ by terms of $K^+$-order $(\alpha-2)-$: on spatially compact sets
$O(t_*^{-2-\epsilon})$ for every $\epsilon<\epsilon_K$ (Theorem 2.2). In the class of Part VII, $\dot b$ is a change of
mass alone and the boost vanishes (Corollary 2.3). This is the form of Theorem 4 (Part VII Theorem 0.2) one order down,
and the statement the paper's section 8.2 reaches by deduction: there the decay of the metric is deduced in a
Regge-Wheeler gauge from [KI03] and [HKW18], and in the harmonic gauge by Hung's route in five dimensions.

No new linear theory is written. The linear solution is the derivative at zero data of III.K's equation $P_5(\Psi(U)) =
0$, solved directly: the linear Cauchy problem near $\Sigma_{\mathrm{IVP}}$ (Part IV$''$ Theorem 2.4, Part IV$'''$
Theorem 2.1 and III.C$'$ Theorem 3.1's proof, each at $h = 0$), III.K Lemma 2.3's right inverse at $U = 0$, and the
linearised Bianchi identity in place of the nonlinear one. Nash-Moser gives no differentiability of the nonlinear
solution in the data, so the linear solution is not obtained by differentiating Theorem 4.3's solution (finding
(VIII1)). Being linear, nothing here needs smallness.

## 0. Setting

Everything of III.K section 0 is kept: $t_*$, $t_{\mathrm{IVP}}$, $\Sigma_{\mathrm{IVP}}$, $t^\flat_*$ and $C_\flat$,
$\hat T = 2/C_\flat$, $\Omega_*$, $\chi_-$, $\chi_K$ (with $\chi_K = 0$ on $\{t^\flat_*<\hat T+2\}$), $\chi_\iota$,
$E_C$, $E_\Upsilon$, $\mathcal E_0$, $\ell_0$, $\mathcal E^C_I$, $\ell_I$, the cone's weights and $\alpha$; the
parameters are those of VI.C Theorem 2.1 (PART-VI4-PARAMS.md), as in Theorem 4. Also III.K Lemma 1.1 ($\chi^\natural_0$
and $P^\natural$) and Proposition 1.2's region at $S = 0$,
$$\mathcal D = N\cap\{t^\flat_*\le\hat T+3\},\qquad N = \{t_{\mathrm{IVP}}\ge-\nu(r)\},$$
with its cover by $\Omega_{\mathrm{ext},r_1}$, the compact part $\mathcal K$ and the slab $\mathcal S$ (III.K
Proposition 1.2's proof, with $S = 0$ and the same $r_1$, $R_8$, $R_9$, $c$, $T''$ and $\rho'_I$). $\mathcal D$
contains $\Omega_*\cap\{t^\flat_*\le\hat T+3\}$, as $t_{\mathrm{IVP}}\ge t_*\ge t^\flat_*\ge1$ there.

*Linearised operators.* Write $g := g_{b_0}$. For a symmetric 2-tensor $k$ let $D\mathrm{Ric}(k) :=
\frac{d}{ds}\mathrm{Ric}(g+sk)|_{s=0}$, and let $\dot\Upsilon(k)$, $\dot\Upsilon^\natural(k)$, $\dot\Upsilon^0(k)$ be
the derivatives at $(g,g)$ in the first argument of $\Upsilon^{E_\Upsilon}$, $\Upsilon^{\chi^\natural_0E_\Upsilon}$ and
$\Upsilon^0$ (III.B Definition 6.1, III.C$''$ (2.1), III.K Lemma 1.1). As $\delta^*_{g_0,E_C}$ depends on $g_0$ only,
$$L := D_1P(g,g) = D\mathrm{Ric}-\delta^*_{g,E_C}\dot\Upsilon,\qquad L^\natural := D_1P^\natural(g,g) =
D\mathrm{Ric}-\delta^*_{g,E_C}\dot\Upsilon^\natural.\tag{0.1}$$
$L$ is III.C's $L^{g,g}$, and $L^\natural$ is Part IV$'''$'s $L^{\chi^\natural_0}_{g,g}$. On $\Omega_*$,
$\chi^\natural_0 = 1$ (III.K Lemma 1.1 (b)), so $L^\natural = L$ and $\dot\Upsilon^\natural = \dot\Upsilon$ there. Near
$\Sigma_{\mathrm{IVP}}$, $\chi^\natural_0 = 0$ (Lemma 1.1 (d)), so $\dot\Upsilon^\natural = \dot\Upsilon^0$ there. And
$\Upsilon^{E_\Upsilon}(g_0,g_0) = \Upsilon^{\chi^\natural_0E_\Upsilon}(g_0,g_0) = 0$ for every metric $g_0$, since
$\Upsilon^0(g_0,g_0) = 0$ and the $E^\Upsilon$-term is linear in $g-g_0$ (III.C Corollary 5.3's proof, III.C$''$ Lemma
2.1's proof).

*The constraints.* For a metric $\tilde g$ near $\Sigma_{\mathrm{IVP}}$ with future unit normal $\nu_{\tilde g}$,
inducing $(\gamma,k)$, the Gauss and Codazzi equations write $(G_{\tilde g}\mathrm{Ric}(\tilde g))(\nu_{\tilde
g},\cdot)|_{\Sigma_{\mathrm{IVP}}} = \mathcal C(\gamma,k)$, where $\mathcal C$ is the constraint map and does not
depend on $\tilde g$ beyond $(\gamma,k)$. Its vanishing is the constraint equations (as III.K Proposition 1.2 uses
them). Data $(\dot\gamma,\dot k)$ satisfy the *linearised constraint equations* if $D\mathcal
C_{(\gamma_{b_0},k_{b_0})}(\dot\gamma, \dot k) = 0$.

*The boost generator.* $\phi_S = \exp V(S)$, with $V(S)$ linear in $S\in\mathcal S_1$ and supported where
$\chi^\flat_K\ne1$ (PART-III-B-FAMILY.md:340-359, as Part VII Lemma 3.1 records). Put
$$\dot g_{S'} := \frac{d}{ds}\phi_{-sS'}^*g\Big|_{s=0} = -\mathcal L_{V(S')}g,\tag{0.2}$$
a linearised diffeomorphism. $D\mathrm{Ric}(\dot g_{S'}) = \frac{d}{ds}\mathrm{Ric}(\phi_{-sS'}^*g)|_{s=0} = 0$, and
$\dot g_{S'} = 0$ on the interior of $\{\chi^\flat_K = 1\}$, where $V(S') = 0$. Put $\mathcal D' := \mathcal
D\setminus\{t^\flat_*\ge\hat T+\frac74\}$; then $\Omega_*\cup\mathcal D = \Omega_*\cup\mathcal D'$ and
$\Omega_*\cap\mathcal D' = \Omega_*\cap\{t^\flat_*<\hat T+\frac74\}$.

## 1. The linear initial-value problem

**Lemma 1.1 (linearised gauged Cauchy data; III.C$''$ Proposition 4.1 linearised).** Let $\dot\gamma\in
H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}(\Sigma_{\mathrm{IVP}};S^2T^*\Sigma_{\mathrm{IVP}})$ and $\dot k\in
H^{\infty,(\mathcal E_0+1,\ell_0+1)}_{\mathrm b}(\Sigma_{\mathrm{IVP}};S^2T^*\Sigma_{\mathrm{IVP}})$. There are $\dot
h_0,\dot h_1\in H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}(\Sigma_{\mathrm{IVP}};S^2T^*)$, linear in
$(\dot\gamma,\dot k)$, each seminorm bounded by finitely many of $(\dot\gamma,\dot k)$, such that every smooth
symmetric 2-tensor $\dot h$ near $\Sigma_{\mathrm{IVP}}$ with $\dot h|_{\Sigma_{\mathrm{IVP}}} = \dot h_0$ and
$(r\mathcal L_{\partial_{t_{\mathrm{IVP}}}}\dot h)|_{\Sigma_{\mathrm{IVP}}} = \dot h_1$ satisfies:

(1) the first and second fundamental forms of $\Sigma_{\mathrm{IVP}}$ for $g+s\dot h$ have the derivatives
$(\dot\gamma, \dot k)$ at $s = 0$;

(2) $\dot\Upsilon^0(\dot h) = 0$ at $\Sigma_{\mathrm{IVP}}$;

(3) if $(\dot\gamma,\dot k)$ satisfy the linearised constraint equations, then $(G_gD\mathrm{Ric}(\dot h))(\nu,\cdot) =
0$ at $\Sigma_{\mathrm{IVP}}$, $\nu$ the unit normal for $g$.

*Proof.* For $|\epsilon|$ small, III.C$''$ Proposition 4.1 applies to $(\tilde\gamma,\tilde k) :=
\epsilon(\dot\gamma,\dot k)$ ($\tilde\gamma$ small in $H^3_{\mathrm b}$; the constraints are not assumed there). It
gives $h_0(\epsilon) = \epsilon\dot\gamma$, extended by $h_0(\nu_{b_0},\cdot) := 0$, and $h_1(\epsilon) = r\tilde
h_1(\epsilon)$. Its proof determines $\tilde h_1(\epsilon)$ at each point by linear algebraic equations, solved in the
order $(ij)$, $(0j)$, $(00)$, each step dividing by a multiple of $e_0t_{\mathrm{IVP}}$, which is bounded away from 0.
Their other coefficients (the frame, the normal $\nu_0$, the Christoffel symbols of $g_{b_0}+h_0$) are smooth functions
of $h_0$ and its first derivatives. Their right sides are smooth in these and affine in $\tilde k$
(PART-III-C3-BOOSTDATA.md:174-196). So $\epsilon\mapsto h_1(\epsilon)$ is smooth at each point, with $h_1(0) = 0$. Put
$\dot h_0 := \dot\gamma$, extended in the same way, and $\dot h_1 := \partial_\epsilon h_1(0)$. This is the same
construction with the two equations (5.80)-(5.81) of the source linearised at $g_{b_0}$. Their right sides are linear
in $\dot\gamma$, its b-derivatives and $\dot k$, with the coefficients of that proof. So they lie in
$H^{\infty,(\mathcal E_0+1,\ell_0+1)}_{\mathrm b}$ by its count, and $\dot h_1\in H^{\infty,(\mathcal
E_0,\ell_0)}_{\mathrm b}$, linearly and with the stated bounds.

Given $\dot h$, fix $\chi\in C^\infty_c(\mathbb R)$ equal to 1 near 0, and in the coordinates $(t_{\mathrm{IVP}},x)$
put
$$g_\epsilon := g+\epsilon\dot h+t_{\mathrm{IVP}}\chi(t_{\mathrm{IVP}})\,r^{-1}\big(h_1(\epsilon)-\epsilon\dot
h_1\big),$$
the last bracket taken independent of $t_{\mathrm{IVP}}$. Then $(g_\epsilon-g)|_{\Sigma_{\mathrm{IVP}}} =
\epsilon\dot\gamma = h_0(\epsilon)$ and $(r\mathcal
L_{\partial_{t_{\mathrm{IVP}}}}(g_\epsilon-g))|_{\Sigma_{\mathrm{IVP}}} = \epsilon\dot h_1+h_1(\epsilon)-\epsilon\dot
h_1 = h_1(\epsilon)$. The conclusions of III.C$''$ Proposition 4.1 are identities at each point of
$\Sigma_{\mathrm{IVP}}$, derived pointwise in its proof. So they hold for $g_\epsilon$ near any compact piece of
$\Sigma_{\mathrm{IVP}}$, where $g_\epsilon$ is Lorentzian for $|\epsilon|$ small. By its (1)-(2), $g_\epsilon$ induces
$(\gamma_{b_0}+\epsilon\dot\gamma,k_{b_0}+\epsilon\dot k)$ and $\Upsilon^0(g_\epsilon,g) = 0$ at
$\Sigma_{\mathrm{IVP}}$, for every small $\epsilon$. The induced data and $\Upsilon^0$ at $\Sigma_{\mathrm{IVP}}$ are
smooth functions of $g_\epsilon$ and its first derivatives there, and $\partial_\epsilon g_\epsilon|_{\epsilon=0} =
\dot h$, as the correction is $O(\epsilon^2)$ at each point. Differentiating at $\epsilon = 0$ gives (1) and (2).

(3) By the Gauss and Codazzi equations, $(G_{g_\epsilon}\mathrm{Ric}(g_\epsilon))(\nu_{g_\epsilon},\cdot) = \mathcal
C(\gamma_{b_0}+\epsilon\dot\gamma,k_{b_0}+\epsilon\dot k)$ at $\Sigma_{\mathrm{IVP}}$. Differentiate at $\epsilon = 0$.
On the left, the variations of $G_{g_\epsilon}$ and $\nu_{g_\epsilon}$ multiply $\mathrm{Ric}(g) = 0$, leaving
$(G_gD\mathrm{Ric}(\dot h))(\nu,\cdot)$; on the right, $D\mathcal C(\dot\gamma,\dot k) = 0$. $\square$

**Proposition 1.2 (the linear initial solution; III.K Proposition 1.2 linearised at zero data).** Let $(\dot\gamma,\dot
k)$ be as in Lemma 1.1 and satisfy the linearised constraint equations. There is a unique $\dot h$ on $\mathcal D$ with
$$L^\natural\dot h = 0,\qquad\dot h = \dot h_0,\ \ r\mathcal L_{\partial_{t_{\mathrm{IVP}}}}\dot h = \dot h_1\ \text{on
}\Sigma_{\mathrm{IVP}},\tag{1.1}$$
and:

(1) $\dot\Upsilon^\natural(\dot h) = 0$ and $D\mathrm{Ric}(\dot h) = 0$ on $\mathcal D$; on $\mathcal D\cap\Omega_*$,
$\dot\Upsilon(\dot h) = 0$;

(2) on $\mathcal D\cap\Omega_*$, $\dot h\in\bar H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I)}_{\mathrm b}$ (orders
at $\mathscr I^+$; the set is bounded in $t_*$), and for each $k$ there are $k'$ and $C_k$ with $\|\dot h\|_{H^k}\le
C_k\|(\dot\gamma,\dot k)\|_{H^{k+k'}}$, the norms on the right being those of the data classes.

*Proof.* *The solution.* As in III.K Proposition 1.2's proof, $\mathcal D$ is covered by $\Omega_{\mathrm{ext},r_1}$
with its past slab, then $\mathcal K$, then $\mathcal S$, solved in this order. The linear theorems take the place of
the nonlinear ones. The data lie in $H^{\infty,\ell^\flat_0}_{\mathrm b}$, as $\ell^\flat_0<\min\mathrm{Re}\,\mathcal
E_0$ and $\ell^\flat_0<\ell_0$ (III.C$'$ Theorem 3.1's proof, Step 1).

- *Exterior.* On $\Omega_{\mathrm{ext},r_1}$ (Part IV$''$'s $r_0$ being $r_1$), $L^\natural = L^{\chi_0}_{g,g}$ (III.K
  Lemma 1.1 (c)). Part IV$''$ Theorem 2.4 with Corollary 4.1, at $h = 0$ and $\alpha_0 = \ell^\flat_0$, gives the
  unique $\dot h\in H^{k,\ell^\flat_0,(-,\ell^\flat_I)}_{\mathrm b}(\Omega_{\mathrm{ext},r_1})$ with these data,
  bounded by (2.3) there, whose tame term vanishes at $h = 0$. Part IV$''$ Lemma 2.2, which it uses, covers the past
  slab.

- *Compact part.* $\mathcal K$ is compact, and it is the domain of dependence of the past part of its boundary: III.K
  Proposition 1.2's proof shows this for $\phi_S^*g+h_S$ with $|S|$ and the data small, and $g$ is the case $S = 0$,
  $h_S = 0$. $L^\natural$ is a linear operator with smooth coefficients and principal symbol
  $-\frac12g^{-1}(\zeta,\zeta)$ (the normal form of the gauge, as there). Its data on
  $\Sigma_{\mathrm{IVP}}\cap\mathcal K$ are given, and on $\Sigma_{\mathrm{fut},r_1}\cap\partial\mathcal K$ the
  exterior solution gives them. The energy estimates for linear wave equations on a compact domain of dependence then
  give $\dot h$ on $\mathcal K$, forward from $\Sigma_{\mathrm{IVP}}$ and backward to $\{t_{\mathrm{IVP}} = -\nu\}$. It
  is bounded in every $H^k$ by finitely many norms of the data, and unique by II.F Lemma 1.3.

- *Slab.* Part IV$'''$ Theorem 2.1 with $g_0 := g_{b_0}$ and $h = 0$, with the data on $\Sigma_{\mathrm{IVP},r_1}$ and
  the data that $\mathcal K$ gives on $\Sigma_c$, gives $\dot h$ on $\Omega^\natural = \Omega_{\mathrm{ext},r_1}\cup
  \mathcal S$. It equals the exterior solution on $\Omega_{\mathrm{ext},r_1}$, by uniqueness there.

The three solutions agree on overlaps by II.F Lemma 1.3 with $\tau := t_{\mathrm{IVP}}$, as in III.K.

*(2).* On $\Omega_{\mathrm{ext},r_1}$ this is III.C$'$ Theorem 3.1's proof for $L^{\chi_0}$ (III.C$''$ Lemma 2.1).
There $L_{g_{b_0}}\dot h = 0$, so (3.4) of III.C$'$ holds with source 0 and (3.5) without its integral, and every step
is linear in the data. Its (3.2) becomes $\|\dot h\|_{H^{k,(\mathcal E_0,\ell_0),\langle\mathcal E^C_I\rangle,\ell_I}_
{\mathrm b}}\le C_k\|(\dot h_0,\dot h_1)\|_{H^{k_0,(\mathcal E_0,\ell_0)}_{\mathrm b}}$, a linear map continuous at 0
being bounded. On $\mathcal S$, Part IV$'''$ Corollary 2.3's proof (III.C$'$ Theorem 3.1's proof on $\Omega^\natural$)
gives the same, with the data on $\Sigma_c$ bounded by the energy estimate on $\mathcal K$. On $\mathcal K$ there is
nothing at $\mathscr I^+$. Lemma 1.1 bounds $(\dot h_0,\dot h_1)$ by $(\dot\gamma,\dot k)$.

*(1).* This is III.K Proposition 1.2 (2)'s argument, linearised. Put $\dot\eta := \dot\Upsilon^\natural(\dot h)$. By
(0.1) and (1.1), $D\mathrm{Ric}(\dot h) = \delta^*_{g,E_C}\dot\eta$. The second Bianchi identity $\delta_{\tilde
g}G_{\tilde g}\mathrm{Ric}(\tilde g) = 0$ holds for every metric $\tilde g$. Differentiated at the Ricci-flat $g$, the
variation of $\delta_{\tilde g}G_{\tilde g}$ multiplies $\mathrm{Ric}(g) = 0$, so $\delta_gG_gD\mathrm{Ric}(k) = 0$ for
every $k$. Hence $\delta_gG_g\delta^*_{g,E_C}\dot\eta = 0$ on $\mathcal D$. This operator has the principal symbol of
$\delta_gG_g\delta^*_g$, $\frac12g^{-1}(\zeta,\zeta)$ times the identity up to III.B's sign convention
($\delta^*_{g,E_C}-\delta^*_g$ is of order 0; III.K Proposition 4.2). At $\Sigma_{\mathrm{IVP}}$, $\dot\eta =
\dot\Upsilon^0(\dot h) = 0$ by Lemma 1.1 (2). Also $(G_g\delta^*_{g,E_C}\dot\eta)(\nu,\cdot) = (G_gD\mathrm{Ric}(\dot
h))(\nu,\cdot) = 0$ there by Lemma 1.1 (3), so III.K Lemma 4.1, with $g$ for its metric, gives $\partial_\nu\dot\eta =
0$. So the Cauchy data of $\dot\eta$ vanish, and $\dot\eta = 0$ on $\mathcal D$ by II.F Lemma 1.3, forward and backward
of $\Sigma_{\mathrm{IVP}}$, as in III.K. Then $D\mathrm{Ric}(\dot h) = 0$, and $\dot\Upsilon = \dot\Upsilon^\natural$
on $\Omega_*$. $\square$

## 2. The linear solution

**Lemma 2.1 (the source).** Let $\dot h$ be given by Proposition 1.2. $\chi_-(t^\flat_*)\dot h$ is defined on
$\Omega_*\cap\{t^\flat_*\le\hat T+2\}\subset\mathcal D$; extend it by 0 to $\Omega_*$, and put
$$f := -L\big(\chi_-(t^\flat_*)\dot h\big)\quad\text{on }\Omega_*.\tag{2.1}$$
Then $f = -[L,\chi_-(t^\flat_*)]\dot h$ is supported in $\{\hat T+\frac74\le t^\flat_*\le\hat T+2\}$, $f\in\mathcal
F^\infty_{\mathrm{ex}}$, and $\|f\|_{\mathcal F^k_{\mathrm{ex}}}\le C_k\|(\dot\gamma,\dot k)\|_{H^{k+k''}}$.

*Proof.* On $\mathcal D\cap\Omega_*$, $L\dot h = L^\natural\dot h = 0$ by (0.1) and (1.1). So $L(\chi_-\dot h) =
[L,\chi_-]\dot h$, a first-order operator applied to $\dot h$, with coefficients supported in
$\mathrm{supp}\,d\chi_-(t^\flat_*)\subset\{\hat T+\frac74\le t^\flat_*\le\hat T+2\}$. This set is bounded in $t_*$, so
$f$ vanishes near $\iota^+$ and $K^+$. It vanishes on $\{t^\flat_*<\hat T+\frac74\}$, which gives the supported
character of $\mathcal F_{\mathrm{ex}}$. Near $\mathscr I^+$, $\chi_-\dot h$ has the orders $(\langle\mathcal
E^C_I\rangle,\ell_I)$ by Proposition 1.2 (2), as in III.K Lemma 2.2 (c). III.C Proposition 5.2 with $g_1 = g_0 = g$ and
$h = 0$ then puts $L(\chi_-\dot h)$ in the orders $(\langle\mathcal E^C_I+1\rangle',\ell_I+1)$ of $\mathcal
F_{\mathrm{ex}}$ there, continuously, as III.K Lemma 2.2 (c) uses III.C Corollary 5.3. The bound follows from
Proposition 1.2 (2). $\square$

**Theorem 2.2 (linear stability of Schwarzschild-Tangherlini at n = 4).** Let $\dot\gamma\in H^{\infty,(\mathcal
E_0,\ell_0)}_{\mathrm b}(\Sigma_{\mathrm{IVP}})$ and $\dot k\in H^{\infty,(\mathcal E_0+1,\ell_0+1)}_{\mathrm
b}(\Sigma_{\mathrm{IVP}})$ satisfy the linearised constraint equations at $(\gamma_{b_0},k_{b_0})$. Then there are
$U'\in\mathcal D^\infty_{\mathrm{ex}}$ with components $\dot b\in\mathfrak b$, $S'\in\mathcal S_1$ and $S'^{(0)}_1$
(III.J Definition 1.1), and a symmetric 2-tensor $\dot g$ on $\Omega_*\cup\mathcal D$, all linear in $(\dot\gamma,\dot
k)$, with:

(1) $D\mathrm{Ric}(\dot g) = 0$ on $\Omega_*\cup\mathcal D$;

(2) $\dot g = \dot h+\dot g_{S'}$ on $\mathcal D'$ (section 0), with $\dot h$ of Proposition 1.2 and $\dot g_{S'}$ of
(0.2); so $\dot g-\dot g_{S'}$ induces the linearised data $(\dot\gamma,\dot k)$ on $\Sigma_{\mathrm{IVP}}$ (Lemma 1.1
(1)), and $\dot g$ induces them up to the linearised diffeomorphism $-\mathcal L_{V(S')}g$;

(3) on $\Omega_*\cap\{t^\flat_*\ge\hat T+2\}$, $\dot g = D_0G(U')$, the derivative at $U = 0$ of
$$G(U) := g_{b_0,b,-S}+h_{\mathrm{tot}}(\vec p)+h_{\mathrm{rem}}(q)+h,\qquad(h,\vec p,q) = \Phi(U),$$
the metric of III.K Theorem 4.3 (3), and $D_0\Phi(U') = (h',\vec p\,',q')$ with $h'\in\mathcal X^\infty_{J,
\mathrm{ex}}$ and $q'\in\mathcal Q_{\mathrm{ex}}$;

(4) where $\chi_K = 1$,
$$\dot g-\partial_bg_b|_{b=b_0}(\dot b) = h_{b_0,\mathrm{rem}}(q')+h'.\tag{2.2}$$
So for every $R'$, $\epsilon'>0$ and $i,\beta$ there are $C$, $N$ and $T'$ with
$$\big|(t_*\partial_{t_*})^i\partial^\beta_x\big(\dot g-\partial_bg_b|_{b_0}(\dot b)\big)\big|\le C\|(\dot\gamma,\dot
k)\|_{H^N}\,t_*^{-(\alpha-2)+\epsilon'}\quad\text{on }\{r_0\le r\le R',\ t_*\ge T'\},\tag{2.3}$$
and if $\alpha$ is chosen as in Part VII section 4 for a given $\epsilon_t<\epsilon_K$, then $\alpha>4+\epsilon_t$, and
$\epsilon' := \alpha-4-\epsilon_t$ gives $\dot g-\partial_bg_b(\dot b) = O(t_*^{-2-\epsilon_t})$ there;

(5) the linearised gauge 1-form vanishes: on $\Omega_*$,
$$\dot\eta := \dot\Upsilon(\dot g)+D_2\Upsilon^{E_\Upsilon}(g,g)(\dot g_0)-D\vartheta_{\mathrm{tot}}(\vec p\,') =
0,\qquad\dot g_0 := D_0g_{b_0,b,-S}(U'),$$
and on $\mathcal D'$, $\dot\Upsilon^\natural(\dot g)+D_2\Upsilon^{\chi^\natural_0E_\Upsilon}(g,g)(\dot g_{S'}) = 0$.
These are the derivatives of the gauge conditions of III.K Proposition 4.2;

(6) $|\dot b|+|S'|+|S'^{(0)}_1|+\|U'\|_{\mathcal D^k_{\mathrm{ex}}}\le C_k\|(\dot\gamma,\dot k)\|_{H^{k+k'}}$.

*Proof.* *Step 1 (the right inverse at Tangherlini).* At zero data, $h_S = 0$ for every $S$ (III.K Proposition 1.2
(3)), so $\Psi = \Phi$ (III.K (2.1)). III.K Lemma 2.3 at zero data and $U = 0$ gives a linear $\mathcal R:\mathcal
F^\infty_{\mathrm{ex}}\to\mathcal D^\infty_{\mathrm{ex}}$ with $D_0(P_5\circ\Phi)(\mathcal Rf) = f$, bounded by the
tame estimate of III.J$''$ Theorem 4.2 on the exact scales, which at $U = 0$ reads $\|\mathcal Rf\|_{\mathcal
D^k_{\mathrm{ex}}}\le C_k\|f\|_{\mathcal F^{k+d}_{\mathrm{ex}}}$, $d$ its loss. The tail of $U = 0$ vanishes
everywhere, so Lemma 2.3's support clause applies with $c := \hat T+\frac74$: if $f$ vanishes on $\{t^\flat_*<\hat
T+\frac74\}$, so does the tail of $\mathcal Rf$. Put $U' := \mathcal Rf$ with $f$ of Lemma 2.1. Its tail $\tilde h'$
vanishes on $\{t^\flat_*<\hat T+\frac74\}$, and (6) follows from Lemma 2.1.

*Step 2 (the equation in the cone).* For $U$ small and a symmetric 2-tensor $k$ on $\Omega_*$, III.K Proposition 4.2's
"The equation" gives, with zero data,
$$P_5\big(\Phi(U)+(k,0,0)\big) = \mathrm{Ric}(G(U)+k)-\delta^*_{g_0(U),E_C}\Big(\Upsilon^{E_\Upsilon}\big(G(U)+k,
g_0(U)\big)-\vartheta_{\mathrm{tot}}(\vec p)\Big),\qquad g_0(U) := g_{b_0,b,-S},$$
which is III.K's $P_5(\Psi(U))$ for $k = \chi_-h_{-S}$. The right side is smooth in $(U,k)$. $\Phi$ is smooth (III.J
Theorem 2.4, III.J$'''$ Corollary 6.6), $g_{b_0,b,-S}$ is smooth in $(b,S)$ (III.I (1.1), (0.2)), and
$h_{\mathrm{tot}}$, $\vartheta_{\mathrm{tot}}$ and $h_{\mathrm{rem}}$ are smooth in $(\vec p,q)$
(PART-III-I8-UNPARAM.md Definition 2.3, PART-III-I9-COMMOTION.md Definition 2.1, PART-III-I10-CORR4.md Definitions 2.1
and 2.3, PART-III-I15-AUGMENT5.md Definition 1.2). At $(U,k) = (0,0)$ the metric is $g$ and the gauge 1-form vanishes,
so the variation of $\delta^*_{g_0(U),E_C}$ drops out. Differentiating at $(0,0)$ in the direction $(U',\chi_-\dot h)$
gives
$$D\mathrm{Ric}(\dot g)-\delta^*_{g,E_C}\dot\eta = D_0(P_5\circ\Phi)(U')+L(\chi_-\dot h) = f-f = 0\quad\text{on
}\Omega_*,\tag{2.4}$$
with $\dot g := D_0G(U')+\chi_-\dot h$ and $\dot\eta$ as in (5). Here $D_hP_5(0)(k) = Lk$, since at $U = 0$ the right
side is $P(g+k,g)$.

*Step 3 (the initial part of the cone).* On $\Omega_*\cap\{t^\flat_*<\hat T+\frac74\}$, for every $U$: $\chi_K = 0$, so
$g_{b_0,b,-S} = \phi_{-S}^*g$; $h_{\mathrm{tot}}(\vec p)$ and $\vartheta_{\mathrm{tot}}(\vec p)$ vanish, being
supported in $\mathcal C\subset\mathrm{supp}\,\chi_K$, and $h_{\mathrm{rem}}(q)$ vanishes, carrying $\chi_K$; and the
metric component of $\Phi(U)$ is $\tilde h$, as $\chi_\iota = 0$ there (III.K Lemma 2.2's proof). So there $D_0G(U') =
\dot g_{S'}+\tilde h' = \dot g_{S'}$ and $\chi_- = 1$, whence
$$\dot g = \dot g_{S'}+\dot h,\qquad\dot\eta = \dot\Upsilon(\dot h)+\big(D_1+D_2\big)\Upsilon^{E_\Upsilon}(g,g)(\dot
g_{S'}) = 0.$$
The first term vanishes by Proposition 1.2 (1). The second is $\frac{d}{ds}\Upsilon^{E_\Upsilon}(\phi_{-sS'}^*g,
\phi_{-sS'}^*g)|_{s=0} = 0$ (section 0).

*Step 4 (propagation).* By (2.4) and the linearised Bianchi identity (Proposition 1.2's proof),
$\delta_gG_g\delta^*_{g,E_C}\dot\eta = 0$ on $\Omega_*$. $\dot\eta$ vanishes on $\Omega_*\cap\{t^\flat_*<\hat
T+\frac74\}$, which contains $\Omega_*\cap\{t^\flat_*\le2\}$ ($\hat T\ge2$). II.F Lemma 1.3 on $\Omega^\circ_*$ with
$\tau := t^\flat_*$ and $c := \frac32$, as in III.K Proposition 4.2, gives $\dot\eta = 0$. Its compactness hypothesis
is checked in II.F section 7.4 for metrics with $dt^\flat_*$ past timelike, and $g$ is one (II.C Lemma 3.2 (2) at $h =
0$). So $D\mathrm{Ric}(\dot g) = 0$ on $\Omega_*$ by (2.4).

*Step 5 (the initial region).* On $\mathcal D'$ put $\dot g := \dot h+\dot g_{S'}$. $D\mathrm{Ric}(\dot h) = 0$
(Proposition 1.2 (1)) and $D\mathrm{Ric}(\dot g_{S'}) = 0$ (section 0). The gauge 1-form of (5) on $\mathcal D'$ is
$\dot\Upsilon^\natural(\dot h)+(D_1+D_2)\Upsilon^{\chi^\natural_0E_\Upsilon}(g,g)(\dot g_{S'}) = 0+0$, as in Step 3. On
$\Omega_*\cap\mathcal D' = \Omega_*\cap\{t^\flat_*<\hat T+\frac74\}$ the two definitions of $\dot g$ agree (Step 3),
and so do those of the gauge 1-form, $\chi^\natural_0$ being 1 there. As $\Omega_*\cup\mathcal D' =
\Omega_*\cup\mathcal D$, this gives (1), (2) and (5).

*Step 6 ((3) and (4)).* On $\{t^\flat_*\ge\hat T+2\}$, $\chi_- = 0$, so $\dot g = D_0G(U')$; this is (3), with
$D_0\Phi(U')$ in the classes of III.J Theorem 2.4 (2.4) and III.J$'''$ Corollary 6.6. Where $\chi_K = 1$: $g_{b_0,b,-S}
= g_b$ for every $(b,S)$ (III.I (1.1)), so $D_0g_{b_0,b,-S}(U') = \partial_bg_b|_{b_0}(\dot b)$; $h_{\mathrm{tot}}(\vec
p)$ vanishes for every $\vec p$, each of its terms carrying a factor $d\chi_K$ (the four sites of Part VII Theorem 0.2
(i)), so its derivative vanishes; $h_{b,\mathrm{rem}}(q)$ is linear in $q$ for each $b$ (PART-III-I15-AUGMENT5.md
(1.2)), so its derivative at $(b_0,0)$ in the direction $(\dot b,q')$ is $h_{b_0,\mathrm{rem}}(q')$; and the derivative
of $h$ is $h'$. This is (2.2).

*The rate.* This is Part VII section 4's argument for (0.2). On $\{r\le R'\}$ and for $t_*$ large, $\chi_K = 1$, as
$\mathrm{supp}(1-\chi_K)$ is disjoint from a neighbourhood of $K^+$ (PART-III-I15-AUGMENT5.md Lemma 2.2 (c)). $h'$ has
$K^+$-order $\alpha-$, and $h_{b_0,\mathrm{rem}}(q')$ has $K^+$-order $(\alpha-2)-$, each seminorm bounded by one of
$q'$ (PART-III-I15-AUGMENT5.md Lemma 2.2 (a)). Near the interior of $K^+$, $\rho_K = t_0^{-1}$ with $t_0 = t-|x|$
(III.B (2.2), (4.1)), comparable to $t_*$ on $\{r\le R'\}$, and the b-vector fields there are spanned by
$t_*\partial_{t_*}$ and $\partial_x$. By b-Sobolev embedding, $(t_*\partial_{t_*})^i\partial^\beta_x$ of a function of
$K^+$-order $w-$ is $O(t_*^{-w+\epsilon'})$, bounded by a seminorm of it. With $w = \alpha-2$, (6) and III.J Theorem
2.4's bound $\|D_0\Phi (U')\|_k\le C_k\|U'\|_{\mathcal D^{k+d}}$, this is (2.3). The bound on $\alpha$ is VI.C row w2
with Part VII section 4's choice $\alpha>4+\epsilon_t$. $\square$

**Corollary 2.3 (in the class).** Let $G = O(2)\times O(2)$ act as in Part VII section 0, and make the choices of Part
VII Lemma 3.1 equivariant. If $(\dot\gamma,\dot k)$ are $G$-invariant, Theorem 2.2 holds with $U'$ fixed by $G$, $\dot
b = (\dot\mu,0)$, $S' = S'^{(0)}_1 = 0$ and $\dot g$ $G$-invariant. So $\dot g = \dot h$ near $\Sigma_{\mathrm{IVP}}$
induces $(\dot\gamma,\dot k)$, and where $\chi_K = 1$,
$$\dot g-\dot\mu\,\partial_\mu g_{(\mu,0)}|_{\mu=\mu_0} = h_{b_0,\mathrm{rem}}(q')+h',$$
with the rate (2.3): the perturbation settles to a change of mass alone, as $O(t_*^{-2-\epsilon_t})$ on spatially
compact sets.

*Proof.* $G$ acts on $M$ fixing $t$, $t_*$, $t_{\mathrm{IVP}}$, $t^\flat_*$ and $|x|$, so it preserves
$\Sigma_{\mathrm{IVP}}$, $\Omega_*$, $\mathcal D$ and the support classes. It acts on $\mathcal D^k_{\mathrm{ex}}$ and
$\mathcal F^k_{\mathrm{ex}}$ boundedly, isometrically for the norms $\sup_{\sigma\in G}|\sigma\cdot(\cdot)|_k$, and
$\Pi := \int_G\sigma\,d\sigma$ projects onto the fixed elements and preserves every support class (Part VII Proposition
3.2's proof). Lemma 1.1's construction is natural: it sets $\dot h_0 := \dot\gamma$ with $\dot h_0(\nu,\cdot) := 0$ and
solves tensorial linear equations for $\dot h_1$ uniquely, as Part VII Lemma 3.1 records for III.C$''$ Proposition 4.1.
So $\dot h_0$, $\dot h_1$ are $G$-invariant. $L^\natural$ is natural, its cut-offs being functions of
$(t_{\mathrm{IVP}},|x|)$ and $t_*$ and its gauge 1-forms radial (Part VII Lemma 3.1 (C1)-(C2)). So $\sigma_*\dot h$
solves (1.1) for $\sigma\in G$, and $\dot h$ is $G$-invariant by the uniqueness in Proposition 1.2. $\chi_-$ is a
function of $t^\flat_*$, so $f$ is $G$-fixed. Differentiating Part VII Lemma 3.1's $P_5(\Psi(\sigma\cdot U)) =
\sigma_*P_5(\Psi(U))$ at the fixed point $U = 0$, at zero data, gives $D_0(P_5\circ\Phi)\circ\sigma = \sigma_*\circ
D_0(P_5\circ\Phi)$. So $U'' := \Pi\mathcal Rf$ satisfies $D_0(P_5\circ\Phi)(U'') = \Pi f = f$. Its tail vanishes on
$\{t^\flat_*<\hat T+\frac74\}$, and it is bounded as in (6). Run Steps 2-6 with $U''$ in place of $U'$. $U''_0 = (\dot
b,S',S'^{(0)}_1)$ lies in $\mathfrak b^G\times\mathcal S_1^G\times\mathcal S_1^G = (\mathbb
R\times\{0\})\times0\times0$ (Part VII section 0). So $\dot g_{S'} = 0$, and $\dot g$ is $G$-invariant, every
ingredient being equivariant and $U''$ fixed. $\square$

**Remark 2.4 (what is and is not asserted).** (a) Theorem 2.2 has the form of Theorem 4 (Part VII Theorem 0.2): every
linearised data set in the class has a linearised vacuum development, in a fixed gauge, that settles at the stated
rate. It does not assert that a given linearised solution in another gauge differs from $\dot g$ by a linearised
diffeomorphism on $\Omega_*\cup\mathcal D$. That comparison is the linear counterpart of Part VII Remark 4.1: a linear
wave equation for the gauge 1-form, solved on the whole domain. It is not written here, and nothing above uses it. (b)
The rate is that of the slowest term at $K^+$, $h_{b_0,\mathrm{rem}}(q')$, which carries the decaying tails of the
parameter and centre-of-mass motions (PART-III-I15-AUGMENT5.md (1.2)), as in Part VII finding (VII4).

## 3. Findings, labels and sources

(VIII1) *Linearising the equation, not the solution.* III.K's solution comes from II.G's Nash-Moser theorem, which
gives existence and bounds but no differentiability in the data. So the linear solution is built directly. Proposition
1.2 is III.K Proposition 1.2 at zero data with the linear theorems of Parts IV$''$-IV$'''$ in place of the nonlinear
ones. Theorem 2.2's $U'$ is III.K Lemma 2.3's right inverse at $U = 0$ applied to the source (2.1), which carries the
initial solution into the cone. (2.4) is what formal differentiation of $P_5(\Psi(U)) = 0$ in $(U,\text{data})$ at
$(0,0)$ gives, with $\chi_-\dot h$ in place of the derivative of $\chi_-h_{-S}$ in the data, which is not shown to
exist; (2.4) is solved directly instead.

(VIII2) *The boost at the linear level.* The derivative of $\chi_-h_{-S}$ in $S$ vanishes at zero data, so the boost
enters the linear problem only through $g_{b_0,b,-S}$. There it is the linearised diffeomorphism (0.2), supported where
$\chi^\flat_K\ne1$. It is absent where $\chi_K = 1$, and absent in the class.

(VIII3) *Constraint propagation.* The nonlinear propagation (III.K Propositions 1.2 (2) and 4.2) uses the second
Bianchi identity at the solution. Here it is used at $g$, where its derivative is $\delta_gG_gD\mathrm{Ric} = 0$
because $g$ is Ricci flat. The linearised constraints enter through the Gauss-Codazzi identity differentiated along
$g_\epsilon$ (Lemma 1.1 (3)).

(VIII4) *Relation to the paper's section 8.2.* There the decay of the metric is deduced in a Regge-Wheeler-type gauge
from [KI03] and [HKW18] (supplement Proposition 10.1), and in the harmonic gauge by Hung's route in five dimensions
(Propositions 10.2-10.5, sections 10.7-10.11). Theorem 2.2 and Corollary 2.3 prove the linear statement in the gauge of
the nonlinear problem, at the rate of Theorem 4, from the proved Parts III-IV. The deduced routes stay as they are, as
independent routes in other gauges, and Remark 2.4 (a) says what links them to this one: nothing written.

*Labels.* Lemma 1.1 (III.C$''$ Proposition 4.1 linearised), Proposition 1.2 (III.K Proposition 1.2 linearised), Lemma
2.1, Theorem 2.2 (III.K Theorem 4.3 linearised), Corollary 2.3 (Part VII Proposition 3.2 linearised), Remark 2.4.

*Sources.* No source paper is read here: every input is a proved part. II.C Lemma 3.2; II.F Lemma 1.3 and section 7.4;
III.B Definition 6.1, (2.2), (4.1) and section 5 (PART-III-B-FAMILY.md:340-359); III.C Proposition 5.2 and Corollary
5.3's proof; III.C$'$ Theorem 3.1 and its proof; III.C$''$ (2.1), Lemma 2.1, Proposition 4.1; III.I (1.1)-(1.2);
PART-III-I8-UNPARAM.md Definition 2.3; PART-III-I9-COMMOTION.md Definition 2.1; PART-III-I10-CORR4.md Definitions 2.1
and 2.3; PART-III-I15-AUGMENT5.md Definition 1.2 and Lemma 2.2; III.J Definition 1.1 and Theorem 2.4; III.J$''$ Theorem
4.2; III.J$'''$ Corollary 6.6; III.K section 0, Lemma 1.1, Proposition 1.2 and its proof, (2.1), Lemmas 2.2-2.3, 4.1,
Proposition 4.2 and Theorem 4.3; Part IV$''$ Lemma 2.2, Theorem 2.4, Corollary 4.1; Part IV$'''$ Theorem 2.1, Corollary
2.3; VI.C Theorem 2.1; Part VII section 0, Lemma 3.1, Proposition 3.2, Theorem 0.2 and section 4.
