# Part III.F. The linearised gauge-fixed Einstein operator at n = 4: structure, trapped set ([Hin26] 8 to 8.1)

*Status.* Written (D228). This part proves, at spatial dimension $n = 4$ and for the Myers-Perry metrics $g_b$ of Part
III.B with $b$ near $b_0 = (\mu_0,0)$, what [Hin26] section 8 establishes up to the end of section 8.1 (pp. 144-149):
the structure of the linearised gauge-fixed Einstein operator $L_b$ as a stationary wave-type operator (his Lemma 8.1),
its Minkowski model and the spectrum of the model's endomorphism $\bar S$ (his Lemma 8.2 with (8.7)), and the bound at
the trapped set (his Proposition 8.3), in the form Part I.B uses. Parts are cited as in III.D and III.E; (Dyn) is as in
III.D.

*What n = 4 changes.* The structure is that of the source with the shift $\frac32$ in place of $1$ and one more power of
$\rho$ in every deviation from Minkowski space. The spectrum of $\bar S$ is the union of those of the gauge potential
and constraint propagation operators and five zeros (two at $n = 3$); this follows from a factorisation of $\bar S$
through 1-forms, in which one cross term vanishes, and needs no explicit matrix. At the trapped set the angular plane is
two-dimensional and is rotated along the flow; a grading of the symmetric 2-tensors that this rotation preserves gives
the bound for every constraint damping 1-form, angular components included. Findings (F1)-(F5) are in section 5.

## 1. The operator

Fix, as the source's section 8 does: the gauge modification
$E_\Upsilon = (c_\Upsilon,e_\Upsilon,\gamma_\Upsilon;c_{\Upsilon,H},\gamma_{\Upsilon,H})$ of III.D section 1, with
$0<e_\Upsilon\ll1$ and $0<\gamma_\Upsilon\ll1$ as III.D$'$ Proposition 4.1 (his Proposition 6.12) allows, so that the
gauge potential operator $\Box^\Upsilon_b$ is mode stable with the indicial roots of III.D Lemma 4.1; and $v_C\in(0,1)$,
$C_0 = 100$, and $c_C$, $e_C\in(0,1)$, $\gamma_C$ from III.E Theorem 1.1, with $\gamma_C$ so large that
$(1-e_C)(1-v_C)\gamma_C>100$, so that the constraint propagation operator $\Box^C_b$ is mode stable, enhanced at zero
energy. The *linearised gauge-fixed Einstein operator* is
$$L_b := D_{g_b}\mathrm{Ric}+\delta^*_{g_b,E_C}\delta_{g_b,E_\Upsilon}G_{g_b},\tag{1.1}$$
the operator $L_{g_b}$ of III.B (6.8), acting on symmetric 2-tensors. By III.B (6.7)-(6.8),
$$2L_b = \Box_{g_b}+2E^C_{g_b}\delta_{g_b}G_{g_b}+2\delta^*_{g_b,E_C}E^\Upsilon_{g_b}G_{g_b}+2R_{g_b},\tag{1.2}$$
with $\Box_g\dot g = -g^{\kappa\lambda}\dot g_{;\kappa\lambda}$ and $R_g$ the curvature term of III.B (6.7): expand
$2(\delta^*+E^C)(\delta+E^\Upsilon)G$ and use $2D\mathrm{Ric} = \Box-2\delta^*\delta G+2R$. The spectral family is
$\widehat{L_b}(\sigma) := e^{i\sigma t_*}L_be^{-i\sigma t_*}$ on stationary sections of $S^2T^*X$, trivialised by the
products of $dt_*,dx^1,\dots,dx^4$ (the bundle $E$ of I.A with $N = 15$).

## 2. Structure ([Hin26] Lemma 8.1 at n = 4)

The Minkowski model is $\bar g = -(dt_*+d|x|)^2+\sum_i(dx^i)^2$ of III.D section 2, $\bar t = t_*+|x|$, with
$\bar E^\Upsilon$ of III.D section 2, $\bar c_C := |x|^{-1}(d\bar t-v_C\,d|x|)$,
$\bar E^Ch := \gamma_C(2\bar c_C\otimes_s\omega-\frac23(1-e_C)\bar g\,\iota_{\bar g^{-1}\bar c_C}\omega)$ on 1-forms
$\omega$, and
$$2\bar L := \bar\Box+2\bar E^C\bar\delta\bar G+2(\bar\delta^*+\bar E^C)\bar E^\Upsilon\bar G.\tag{2.1}$$

**Lemma 2.1.** (1) $2L_b$ is stationary with principal symbol $g_b^{-1}(\zeta,\zeta)\,\mathrm{Id}$, and
$\widehat{2L_b}(\sigma) = \hat P(0)+\sigma T+\sigma^2P_2$ satisfies (H1) and the operator part of (H6) of I.A-I.B with
$g = g_b$, $t = t_*$: $P_2 = g_b^{00}\mathrm{Id}$, $\sigma_1(T) = -2g_b^{-1}(dt_*,\cdot)\mathrm{Id}$.

(2) On $\{|x|>0\}$, exactly,
$$2\bar L = -2\partial_{t_*}\rho\big(\rho\partial_\rho-\tfrac32-\bar S\big)+\widehat{2\bar L}(0),\qquad
\rho\bar S = -\bar E^C\iota_X\bar G+(dt_*\otimes_s\cdot)\,\bar E^\Upsilon\bar G,\quad X := \bar g^{-1}dt_*,\tag{2.2}$$
with $\bar S$ a bundle endomorphism homogeneous of degree 0 and
$\widehat{2\bar L}(0)\in\rho^2\mathrm{Diff}^2_{\mathrm b}$, and no $\partial_{t_*}^2$ term.

(3) On $\{|x|>3R_1\}$,
$$2L_b = 2\bar L-g_b^{00}\partial_{t_*}^2+Q_b\partial_{t_*}+R_b,\qquad g_b^{00}\in\rho^2C^\infty(\bar X),\quad
Q_b\in\rho^3\mathrm{Diff}^1_{\mathrm b},\quad R_b\in\rho^4\mathrm{Diff}^2_{\mathrm b},\tag{2.3}$$
stationary and smooth in $b$. Hence (H2) holds with $S := \bar S$ near infinity, and
$\widehat{2L_b}(0)-\widehat{2\bar L}(0)\in\rho^4\mathrm{Diff}^2_{\mathrm b}$; the source's (8.2)-(8.4) hold with
$\rho\partial_\rho-1$ replaced by $\rho\partial_\rho-\frac32$, $S-\bar S = 0$ near infinity, and $\rho^3$ by $\rho^4$.

*Proof.* (1) As in III.D Lemma 2.1 (1): the terms of (1.2) other than $\Box_{g_b}$ have order at most 1, and
$\Box_{g_b}$ has principal part $-g_b^{\mu\nu}\partial_\mu\partial_\nu\mathrm{Id}$ in the frame; conjugation by
$e^{-i\sigma t_*}$ gives the rest, $g_b^{00}<0$ on $X^\circ$ by III.B Lemma 3.7 (a).

(2) In Cartesian coordinates $\bar\Box$ acts componentwise as the scalar wave operator, so by III.A$'$ Lemma 2.1 (1)
$\bar\Box = -2\partial_{t_*}\rho(\rho\partial_\rho-\frac32)+{}^{\mathrm b}\bar\Box(0)$, without a $\partial_{t_*}^2$
term ($\bar g^{-1}$ has none, III.A$'$ (2.3)). The other terms of (2.1) have order at most 1. In $(t_*,x)$ a Cartesian
derivative $\partial_\mu$ has $\partial_{t_*}$-coefficient $(dt_*)_\mu$ ($\partial_{\bar t} = \partial_{t_*}$,
$\partial_{x^i} = \partial_{x^i}|_{t_*}-\frac{x^i}{|x|}\partial_{t_*}$), so the $\partial_{t_*}$-coefficient of
$\bar\delta^*\omega = \mathrm{sym}\,\partial\omega$ is $dt_*\otimes_s\omega$ and that of
$\bar\delta h = -\bar g^{\mu\nu}\partial_\mu h_{\nu\cdot}$ is $-\iota_Xh$. Hence the $\partial_{t_*}$-coefficient of
$2\bar L-\bar\Box$ is $2(-\bar E^C\iota_X\bar G+(dt_*\otimes_s\cdot)\bar E^\Upsilon\bar G)$, which is (2.2), and
$\bar E^C$, $\bar E^\Upsilon$ carry the factor $\rho$ through $\bar c_C$, $\bar c_\Upsilon$, so $\bar S$ is homogeneous
of degree 0. The stationary remainder is $\widehat{2\bar L}(0)$, in $\rho^2\mathrm{Diff}^2_{\mathrm b}$ as each
Cartesian derivative lies in $\rho\mathcal V_{\mathrm b}$ on stationary sections and the zeroth-order terms are
$\rho^2$.

(3) As in III.D Lemma 2.1 (3), with the same inputs: $k := g_b-\bar g\in\rho^2C^\infty$,
$g_b^{-1}-\bar g^{-1}\in\rho^2C^\infty$, $\bar g^{00} = 0$, $\Gamma(\bar g)\in\rho C^\infty$,
$\Gamma(g_b)-\Gamma(\bar g)\in\rho^3C^\infty$, $\mathrm{Riem}(g_b)\in\rho^4C^\infty$ (two derivatives of $k$;
$\mathrm{Riem}(\bar g) = 0$), $c_C-\bar c_C\in\rho^3C^\infty$ (III.E section 1) and
$E^\Upsilon_{g_b}-\bar E^\Upsilon\in\rho^3C^\infty$ (III.D Lemma 2.1 (3)). Then $\Box_{g_b}-\bar\Box$ has second-order
coefficients in $\rho^2C^\infty$ (in the $\partial_{t_*}^2$ slot only $g_b^{00}$), first-order ones in $\rho^3C^\infty$,
zeroth-order ones in $\rho^4C^\infty$; $E^C_{g_b}-\bar E^C\in\rho^3C^\infty$, $G_{g_b}-\bar G\in\rho^2C^\infty$,
$\delta_{g_b}-\bar\delta$ has first-order coefficients in $\rho^2$ and zeroth-order ones in $\rho^3$, and
$\delta^*_{g_b}-\bar\delta^*\in\rho^3C^\infty$, so $2E^C\delta G-2\bar E^C\bar\delta\bar G$ and
$2\delta^*_{E_C}E^\Upsilon G-2(\bar\delta^*+\bar E^C)\bar E^\Upsilon\bar G$ are first-order with $\rho^3$ coefficients
and zeroth-order $\rho^4$ terms; and $2R_{g_b}\in\rho^4C^\infty$. Sorting as there: $\rho^2\partial_{t_*}^2$ terms form
$-g_b^{00}\partial_{t_*}^2$; $\rho^2\partial_{t_*}\partial_{x^i}$ and $\rho^3\partial_{t_*}$ form $Q_b\partial_{t_*}$;
$\rho^2\partial_{x^i}\partial_{x^j}$, $\rho^3\partial_{x^i}$ and $\rho^4$ form $R_b$. (H2) follows from (2) as in III.D.
$\square$

## 3. The model's endomorphism ([Hin26] Lemma 8.2 and (8.7) at n = 4)

**Lemma 3.1.** The characteristic polynomial of $\bar S$ on $S^2T^*$ (dimension 15) is $\lambda^5$ times those of
$\bar S^C$ and $\bar S^\Upsilon$ on $T^*$, the endomorphisms of the constraint propagation and gauge potential operators
($\Box^C$'s of III.E section 1 and $\Box^\Upsilon$'s of III.D (2.1)):
$$\mathrm{spec}\,\bar S = \{0\ (5\times)\}\cup\gamma_C\{2(1-v_C),\,(1-e_C)(1-v_C),\,1-v_C\ (3\times)\}
\cup\gamma_\Upsilon\{2,\,1-e_\Upsilon,\,1\ (3\times)\},\tag{3.1}$$
with algebraic multiplicities. In particular every eigenvalue is $\ge0$ and $\min\mathrm{spec}\,\bar S = 0$, the
source's (8.7).

*Proof.* Write (2.2) as $\rho\bar S = U_1V_1+U_2V_2$ with $U_1 := -\bar E^C$ and $U_2 := dt_*\otimes_s\cdot$ from $T^*$
to $S^2T^*$, and $V_1 := \iota_X\bar G$, $V_2 := \bar E^\Upsilon\bar G$ from $S^2T^*$ to $T^*$. With
$U := (U_1\ U_2):T^*\oplus T^*\to S^2T^*$ and $V := (V_1;V_2)$, $\rho\bar S = UV$, so
$\det(\lambda-UV) = \lambda^{15-10}\det(\lambda-VU)$, and
$$VU = \begin{pmatrix}V_1U_1&V_1U_2\\V_2U_1&V_2U_2\end{pmatrix},\qquad
V_1U_2\omega = \iota_X\bar G(dt_*\otimes_s\omega) = 0:$$
indeed $\iota_X(dt_*\otimes_s\omega) = \frac12(dt_*(X)\omega+\omega(X)dt_*) = \frac12\omega(X)dt_*$ as $dt_*$ is null,
$\mathrm{tr}(dt_*\otimes_s\omega) = \omega(X)$, and $\iota_X\bar g = dt_*$, so
$\iota_X\bar G(dt_*\otimes_s\omega) = \frac12\omega(X)dt_*-\frac12\omega(X)dt_* = 0$. So
$\det(\lambda-VU) = \det(\lambda-V_1U_1)\det(\lambda-V_2U_2)$. The same reading of $\partial_{t_*}$-coefficients for
$\Box^C = 2\delta G\delta^*+2\delta GE^C$ and $\Box^\Upsilon = 2\delta G\delta^*+2E^\Upsilon G\delta^*$ gives
$\rho\bar S^C = -\iota_X\bar G\bar E^C = V_1U_1$ and
$\rho\bar S^\Upsilon = \bar E^\Upsilon\bar G(dt_*\otimes_s\cdot) = V_2U_2$. Their spectra, by hand: with the null
covectors $dt_*$ and $k := d\bar t+d|x|$ ($X = -\partial_{\bar t}-\partial_r$, $dt_*(X) = 0$, $k(X) = -2$,
$\bar g^{-1}(k,dt_*) = -2$), and
$\bar G\bar E^C\omega = \gamma_C(2\bar c_C\otimes_s\omega-e_C\bar g\langle\bar c_C,\omega\rangle)$ (III.B (6.5)),
$\bar c_C/\rho = \frac12(1-v_C)k+\frac12(1+v_C)dt_*$:
$$\gamma_C^{-1}\bar S^C\omega = (1-v_C)\omega-\omega(X)\,\bar c_C/\rho+e_C\langle\bar c_C/\rho,\omega\rangle\,dt_*,$$
which is $(1-v_C)\omega$ on angular $\omega$, $(1-e_C)(1-v_C)dt_*$ on $dt_*$, and $2(1-v_C)k+(1+v_C)(1-e_C)dt_*$ on $k$.
With $\bar E^\Upsilon\bar Gh = -\gamma_\Upsilon(2\iota_Yh-e_\Upsilon\bar c_\Upsilon\mathrm{tr}\,h)$,
$Y := \bar g^{-1}d\bar t$, $\bar c_\Upsilon = \rho\,d\bar t$ (III.B (6.5)),
$$\gamma_\Upsilon^{-1}\bar S^\Upsilon\omega = \omega-\omega(Y)\,dt_*+e_\Upsilon\omega(X)\,d\bar t,$$
which is $\omega$ on angular $\omega$, $2dt_*$ on $dt_*$ ($dt_*(Y) = -1$), and $(1-e_\Upsilon)(k+dt_*)$ on $k$. Both are
triangular in the bases (angular, $dt_*$, $k$), with the diagonals of (3.1). (*Computed:* `sbar5.py` S1-S2 build
$2\bar L$ on $4+1$ Minkowski and find (3.1) with the multiplicities; `cpmodes5.py` K1 and `thresh5.py` U2 the two
factors.) $\square$

The explicit form of $\widehat{2\bar L}(0)$ (the source's (8.6)) is needed only for the indicial roots, and at $n = 4$
it is built and used by `lin5.py` in the next part. The source's (8.8), that $\bar S$ is lower triangular in his
splitting (5.27) with the eigenvalues on the diagonal, enters through (3.1) only, in Corollary 8.7's condition
$\beta_{\mathrm{sctf}}<\frac32+\min\mathrm{Re}\,\mathrm{spec}\,\bar S = \frac32$ (his $1$).

## 4. The trapped set ([Hin26] Proposition 8.3 at n = 4, in the form Part I.B uses)

As in III.D section 5.2, Part I.B uses at the trapped set the bound (Γ.4) with $\gamma_-<0$, i.e.
$\sup_\Gamma\lambda_{\max}(p_1^\Gamma)<\frac12\nu_{\min}$, with losses governed by $\delta_\Gamma$, and the inner
product may depend on the covector (I.B Lemma 6.0). The operator has real coefficients, so complex conjugation exchanges
$z_0 = 1$ and $z_0 = -1$, and (1.4) of I.B, with its factors $z_0$, is the same for both; we take $z_0 = 1$,
$\sigma = 1$ on $\Gamma$.

**Proposition 4.1.** Assume (Dyn). For every $\epsilon>0$ there are a stationary fibre inner product $h_\Gamma$ on
$\pi^*S^2T^*$ over a neighbourhood of $\Gamma_{b_0}$ in phase space, homogeneous of degree 0, and a neighbourhood
$\mathcal B_\epsilon$ of $b_0$, such that for $b\in\mathcal B_\epsilon$,
$\sup_{\Gamma_b}\lambda_{\max}(p_1^\Gamma)<\epsilon$ for $2L_b$, $p_1^\Gamma$ being (6.0) of I.B Lemma 6.0. In
particular (Γ.4) holds with $\gamma_-<0$, and $\delta_\Gamma(0)$ is as small as wished. At $b_0$, $2L_{b_0}$ is strongly
trapping admissible ([Hin26c] Definition 5.8): this holds there for every $\epsilon$ with one $b$.

*Proof.* *The subprincipal operator.* Near $\Gamma_{b_0}$, $E^\Upsilon = 0$ (III.D section 1: the supports of
$c_\Upsilon$ and $c_{\Upsilon,H}$ avoid $U_\Gamma$), and $R_{g_b}$ is of order 0. So by (1.2), on half-densities by
$|dg|$,
$$iS_{\mathrm{sub}}(2L_b) = iS_{\mathrm{sub}}(\Box_{g_b})+2E^C_{g_b}\sigma_1(i\delta_{g_b})G_{g_b},\qquad
iS_{\mathrm{sub}}(\Box_{g_b}) = \nabla^{\pi^*S^2T^*}_{H_G},\tag{4.1}$$
the second identity being the source's (6.13) for the tensor wave operator ([Hin17] Proposition 4.1, in every dimension;
III.D section 5.2 (a) on 1-forms), $\nabla^{\pi^*S^2T^*}$ the Leibniz extension of $\nabla^{\pi^*T^*}$, and
$\sigma_1(i\delta_g)(\zeta)h = \iota_{g^{-1}\zeta}h$.

*The frame.* At $b_0$, near $\Gamma_{b_0}$ (where $C>0$), III.D section 5.2 (c) gives $e_0 = \zeta$, $e_1$, $e_2$ with
Gram matrix $CJ$ and $\nabla_{H_G}e_0 = 0$, $\nabla_{H_G}e_1 = -2\sigma e_0$, $\nabla_{H_G}e_2 = -2\sigma e_1$, and the
plane $V_\perp$ of angular covectors orthogonal to them, $g$-positive, $\nabla_{H_G}$-invariant and $g$-skew there
(III.D Lemma 5.2's proof). Normalise $e_0,e_1,e_2$ by $C^{1/2}$ (stationary, homogeneous of degree 0; $H_GC = 0$ keeps
the connection matrix) and let $e_3,e_4$ be a local $g$-orthonormal frame of $V_\perp$, so
$\nabla_{H_G}e_a = \sigma\kappa R(e_a)$, $a = 3,4$, with $R$ the rotation $e_3\mapsto e_4\mapsto-e_3$ and $\kappa$ a
function homogeneous of degree 0 (D231). Write $c_C = \sum_\mu c_\mu e_\mu$; as $c_C$ is past timelike (III.E Theorem
1.1) and $e_0$ future null on the future characteristic set, $c_2 = -g^{-1}(c_C,e_0)<0$, and
$\gamma := C^{1/2}\gamma_C/\sigma>0$ ($\sigma>0$ on $\Gamma_{b_0}$, which lies in the future characteristic set over
$\{|x|>r_h\}$). With $g^{-1}e_0 = -E_2$ ($E_\mu$ the dual frame), $\sigma_1(i\delta)(\zeta) = -C^{1/2}\iota_{E_2}$, and
(4.1) reads
$$iS_{\mathrm{sub}}(2L_{b_0}) = H_G+\sigma(A+\kappa R),\tag{4.2}$$
on components in the frame, where $A = 2N+2\gamma\,E^C_{(c)}(-\iota_{E_2})G$ ($N$ the Leibniz extension of
$e_1\mapsto-e_0$, $e_2\mapsto-e_1$, $e_0,e_3,e_4\mapsto0$, $E^C_{(c)}$ the map of (6.2) of III.B with $c_C$ in place,
divided by $\gamma_C$) and $R$ acts as a derivation.

*The grading.* Give $e_0,e_1,e_2,e_3,e_4$ the weights $0,1,2,1,1$ and a product of two the sum $\mathrm{wt}$;
$g^{-1}(e_\mu,e_\nu)\ne0$ only if the weights add to 2, and $g = -2e_0e_2+e_1^2+e_3^2+e_4^2$ has weight 2. Then: $N$
lowers $\mathrm{wt}$ by 1; $R$ preserves it; $\iota_{E_2}$ removes a factor $e_2$, lowering it by 2;
$G = I-\frac12g\,\mathrm{tr}$ preserves it; and
$E^C_{(c)}\omega = 2c\otimes_s\omega-\frac23(1-e_C)g\langle c,\omega\rangle$ raises it by the weight of the component
$c_\mu e_\mu$ used, at most 2, with equality only for $c_2$. So $A+\kappa R$ does not raise $\mathrm{wt}$, and its
$\mathrm{wt}$-preserving part is $D := 2\gamma c_2\,\Phi+\kappa R$ with
$\Phi h := 2e_2\otimes_s\iota h-\frac23(1-e_C)g\langle e_2,\iota h\rangle$,
$\iota h := -\iota_{E_2}Gh = -\iota_{E_2}h-\frac12(\mathrm{tr}\,h)\,e_0$ (as $\iota_{E_2}g = -e_0$; and
$\langle e_2,\omega\rangle = -\omega_0$, the $e_0$-coefficient). On the monomials: $\Phi = 0$ on weight 0 ($e_0^2$) and
weight 1 ($e_0e_1$, $e_0e_a$); on weight 2, $\Phi(e_0e_2) = 0$ ($\iota(e_0e_2) = -\frac12e_0+\frac12e_0$), $\Phi = 0$ on
the five spatial trace-free monomials (no $e_2$ factor, trace 0, or differences of equal values), and with
$T := e_1^2+e_3^2+e_4^2$, $\Phi(T) = -(1+2e_C)e_0e_2-(1-e_C)T$ ($\iota e_1^2 = -\frac12e_0$,
$\langle e_2,-\frac12e_0\rangle = \frac12$); on weight 3, $\Phi(e_1e_2) = -e_1e_2$, $\Phi(e_2e_a) = -e_2e_a$; on weight
4, $\Phi(e_2^2) = -2e_2^2$. Refine to $W := 2\,\mathrm{wt}+s$ with $s = 1$ on $T$ and on the spatial trace-free part and
$s = 0$ elsewhere: the only $\mathrm{wt}$-preserving map changing $s$ is $T\mapsto e_0e_2$, which lowers $W$; and $R$
preserves each of the pieces $e_0^2$; $\{e_0e_1,e_0e_3,e_0e_4\}$; $e_0e_2$; $T$; the trace-free spatial part;
$\{e_1e_2,e_2e_3,e_2e_4\}$; $e_2^2$ ($T$ and $g$ are $R$-invariant). So $A+\kappa R = D_0+D_-$ with $D_-$ lowering $W$
and $D_0$ preserving each piece, equal there to a scalar plus $\kappa R$: the scalars are
$0,0,0,-2(1-e_C)\gamma c_2,0,-2\gamma c_2,-4\gamma c_2$ in the order above, all $\ge0$ as $c_2<0$, $e_C<1$. (*Computed:*
`lgrade5.py` G1, for every $c$, angular components included, with failing controls; `strap5.py` P2-P3 the characteristic
polynomial $\lambda^{10}(\lambda+2\gamma c_2)^3(\lambda+4\gamma c_2)(\lambda+2(1-e_C)\gamma c_2)$ and the block form at
$c_3 = c_4 = 0$.)

*The inner product.* Let $\langle\cdot,\cdot\rangle_0$ be the inner product on $\pi^*S^2T^*$ induced by the one making
$e_0,\dots,e_4$ orthonormal; it does not depend on the choice of $e_3,e_4$ in $V_\perp$, so it is defined near
$\Gamma_{b_0}$, stationary and homogeneous of degree 0, and the seven pieces are orthogonal for it. $R$ is skew for it.
For $\eta\in(0,1]$ let $h_\Gamma := \sum_P\eta^{-2W(P)}\langle\cdot_P,\cdot_P\rangle_0$, the sum over the pieces. In an
$h_\Gamma$-orthonormal basis a map lowering $W$ by $j\ge1$ has its entries multiplied by $\eta^j$, so $D_-$ is
$O(\eta)$, while $D_0$ is unchanged; $h_\Gamma$ is constant in the frame, so $H_G$, acting componentwise and preserving
the symplectic volume, is skew. By (4.2) and I.B (6.0) (the inner product is constant in the frame, as in III.D Lemma
5.2), $p_1^\Gamma = -\frac12((A+\kappa R)+(A+\kappa R)^*) = -\frac12(D_0+D_0^*)+O(\eta)$, and $-\frac12(D_0+D_0^*)\le0$,
the scalars being $\ge0$ and $\kappa R$ skew. So $\lambda_{\max}(p_1^\Gamma)\le C\eta$ on $\Gamma_{b_0}$, with $C$
independent of $\eta$ ($\gamma$, $c_\mu$ and $\kappa$ are bounded near the compact $\Gamma_{b_0}$); take $\eta$ with
$C\eta<\epsilon/2$. As in the source, this is for fixed modification parameters. The density: (4.1) is on half-densities
by $|dg|$ and I.A's adjoints for $|dx|$ and $dt_*$; they agree at $b_0$, and near $b_0$ the change adds a scalar
$O(|b-b_0|)$ to $p_1$ (III.D Lemma 5.2).

*Near $b_0$.* Extend $h_\Gamma$ to a stationary inner product near $\Gamma_{b_0}$. $p_1^\Gamma$ for $2L_b$ is built from
the subprincipal symbol of $2L_b$ and $h_\Gamma$, continuous in $b$ uniformly near $\Gamma_{b_0}$, and
$\Gamma_b\to\Gamma_{b_0}$ by (Dyn); so $\sup_{\Gamma_b}\lambda_{\max}(p_1^\Gamma)<\epsilon$ for $b$ near $b_0$.
$\nu_{\min}$ and $\beta_0$ are continuous in $b$ by (Dyn) and positive at $b_0$. $\square$

## 5. Findings, labels and sources

### 5.1 Findings

(F1) *The structure at n = 4.*
$2L_b = -2\partial_{t_*}\rho(\rho\partial_\rho-\frac32-\bar S)+\widehat{2L_b}(0)+Q\partial_{t_*}-g^{00}\partial_{t_*}^2$
near infinity with $Q\in\rho^3\mathrm{Diff}^1_{\mathrm b}$ and
$\widehat{2L_b}(0)-\widehat{2\bar L}(0)\in\rho^4\mathrm{Diff}^2_{\mathrm b}$, where the source has
$\rho\partial_\rho-1$, $S-\bar S\in\rho C^\infty$ and $\rho^3$: the mass enters at $|x|^{-2}$.

(F2) *The spectrum of $\bar S$ without a matrix.* The source obtains (8.7) from an explicit $10\times10$ matrix
(8.6)-(8.8). Here $\rho\bar S$ factors through 1-forms as $U_1V_1+U_2V_2$ with $V_1U_2 = 0$, so its spectrum is that of
the constraint propagation and gauge potential operators' endomorphisms with five zeros, at every $n$ (at $n = 3$, two
zeros and his seven values).

(F3) *The angular plane at the trapped set.* At $n = 3$ the angular complement is a line and the source's basis (8.12)
triangularises $A$. At $n = 4$ it is a plane, rotated along the flow by $\nabla_{H_G}$; the grading $W$ is preserved by
the rotation and makes the rest strictly lowering, for every constraint damping 1-form, angular components included,
which the record's supplement 10.26 (b) had left open for non-spherical $c_C$.

(F4) *The inner product depends on the covector*, through the frame; I.B Lemma 6.0 makes this admissible for (Γ.4).

(F5) *Strong trapping admissibility near $b_0$.* As for the gauge potential operator (III.D finding (D4)), the bound
holds at $b_0$ for every $\epsilon$, and for $b$ near $b_0$ for each fixed $\epsilon$ on a neighbourhood depending on
$\epsilon$; Part I.B needs only the latter.

### 5.2 Labels

Proved here: Lemmas 2.1 and 3.1 and Proposition 4.1. Computed, as checks: `sbar5.py` S1-S3, `strap5.py` P1-P3 and
`lgrade5.py` G1 (exact, each with failing controls), and `cpmodes5.py` K1, `thresh5.py` U2 for the factors. Inputs:
III.B (6.5)-(6.8) and Lemma 3.7; III.A$'$ Lemma 2.1 and (2.3); III.D section 1, Lemma 2.1 and section 5.2; III.D$'$
Proposition 4.1; III.E Theorem 1.1 and section 1; I.A-I.B (H1), (H2), (H6), (H7) and I.B Lemma 6.0; (Dyn). Standard
facts used without proof, and named: $\det(\lambda-UV) = \lambda^{p-q}\det(\lambda-VU)$ for $U$ of size $p\times q$, $V$
of size $q\times p$; the subprincipal operator of a tensor wave operator ([Hin17] Proposition 4.1); the identity
$2D\mathrm{Ric} = \Box-2\delta^*\delta G+2R$ (III.B (6.7)).

### 5.3 Sources

READ: [Hin26] pp. 144-149 (section 8's opening: the data fixed, (8.1); Lemma 8.1 with (8.2)-(8.5) and its proof; Lemma
8.2 with (8.6)-(8.8) and its proof; section 8.1: Proposition 8.3, (8.9)-(8.12) and its proof, footnote 77),
arXiv:2606.28253v2, full text in the record's extraction. The record's supplement 10.25 and 10.26 for the computed
values.
