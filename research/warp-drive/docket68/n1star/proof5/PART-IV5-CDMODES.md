# Part IV$''''$. Constraint damping I: mode stability and the zero energy operator, n = 4 ([Hin26a] sections 3-4, 5.1,
6, Appendix A)

*Status.* Written (D307); amended D308 (Lemma 1.4's reading of (4)-(5), Theorem 2.1 (1)'s data surface). This part
proves III.E Theorem 1.1 (1)-(3) at $n = 4$: the mode stability of the constraint propagation operator $\Box^C_b$ at
$\sigma\ne0$, the invertibility of its zero energy operator on the stated weights, and its indicial roots. It uses
[Hin26a] Theorem 5.2 at $n = 4$ together with the adjoint estimate (5.81), which Part IV$'''''$ proves (Theorem 7.3,
D308), and rests on (Dyn) (Part VI), as III.E is; III.E Theorem 1.1 (4), the tf-admissibility, rests on [Hin26a] Theorem
B.1, which Part IV$''''''$ writes out. The inputs where $n$ enters are the record's computations, each exact: the fibre
algebra of [Hin26a] section 3 (N1STAR-PROOF.md 10.13), the indicial roots for every $h\in(0,10^{-6}]$ (10.12, 10.54),
the 1-form $c$ on Tangherlini (10.14), the weights at the critical sets (10.22), the structure at infinity (10.18) and
the horizon threshold (10.79). Source: [Hin26a] (arXiv:2606.27658v2) pp. 25-41, 66-69 and Appendix A, read at source.

## 0. Setting

$\mathcal B$, $g_b$, $t_*$, $\rho = |x|^{-1}$, $X$, the bundle $E$ and $\bar g$ are as in III.E section 1, and
$\Box^C_b$, $P^C_b$, $(P^C_b)^*$ are III.E (1.1)-(1.2). Write $h := \gamma_C^{-1}$. Then
$$E^C_g\omega = h^{-1}\big(2c_C\otimes_s\omega-\tfrac23(1-e_C)\,g\,\iota_{g^{-1}c_C}\omega\big)$$
is [Hin26a]'s $C_{g,c,e,h}$ of (3.1) with the trace weight $m = \frac23$ in place of his 1, and $\Box^C_b = \Box^{C_h}_g$
of his (3.2), with $h^2\Box^{C_h}_g = 2h^2\delta_gG_g\delta^*_g-iL_{g,c,e,h}$ and $L_{g,c,e,h} =
4ih\,\delta_g(c\otimes_s\cdot) +2ihe\,d\iota_{c^\sharp}$. The weight $\frac23 = \frac2{D-2}$ is the one for which
$hG_gC\omega$ has his form $2c\otimes_s
\omega-e\,g\langle c,\omega\rangle$ for every $e$ (10.12 (U2), (10.46)); with the weight 1, his literal transcription,
the conclusions below fail (10.12 (U5), 10.13 (W1)).

*The parameters.* As III.K section 0 takes them,
$$v_C := \tfrac12,\qquad e_C := \tfrac1{102400},\qquad C_0 := 100\ (\text{or any }C_0\le100),\qquad h\in\mathsf H,
\tag{0.1}$$
where $\mathsf H := (0,h_*)\setminus\mathsf Z$, $h_* := \min(10^{-6},h_0)$ with $h_0$ the bound of Part IV$'''''$'s
Theorem 5.2 at these $(v_C,e_C,C_0)$ and the weights (2.1) below, and $\mathsf Z$ the countable set of Lemma 1.3 (b).
$c_C$ is 10.14's 1-form (10.49) at $\mu = 1$, $r_0 = 100$, smoothed near $r_0/2$ and $2r_0$ (10.14 (b)) and rescaled to
$\mu_0$ (all conditions depend on $\mu r_0^{-2}$ and $r/r_0$ only, 10.14 (v)); it is stationary and equals
$|x|^{-1}(dt-v_C\,d|x|)$ for large $|x|$ (in the static time up to $O(\mu_0|x|^{-3})\,d|x|$, 10.14 (c)).

## 1. The inputs at n = 4

**Lemma 1.1 (the fibre algebra; [Hin26a] Lemmas 3.3-3.8 at n = 4).** On each fibre, with $G(c)<0$, $B :=
g^{-1}-(1+e)G(c)^{-1}c^\sharp\otimes c^\sharp$ is positive definite for $e>0$, $\ell_{g,c,e}(\zeta)$ of his (3.3) is
$B$-self-adjoint for every $\zeta$, and the characteristic polynomial of $\frac12\ell(\zeta)$ is
$(\lambda-G(c)\zeta_0)^3$ times his quadratic (3.8). His Lemmas 3.3-3.8 hold at $n = 4$ verbatim.

*Proof.* The three statements are computed (10.13 (i), `semiclass5.py` W1, exact). His Lemmas 3.3-3.8 are proved on a
single fibre from these three facts and from the splitting $T^* = \mathbb Rc\oplus c^\perp$, in which $G(\zeta) =
G(c)\zeta_0^2+G(\zeta')$ and $\ell(\zeta)$ has the block form (3.5); at $n = 4$, $c^\perp$ has dimension 4 instead of 3
and the factor $(\lambda-G(c)\zeta_0)$ appears to the third power instead of the second, which no step uses beyond its
eigenvalue. $\square$

**Lemma 1.2 (the structure at infinity; [Hin26a] (6.4) at n = 4).** Near $\partial X$, in $t_*$, $\rho$ and spherical
coordinates,
$$\Box^C_b = -2\partial_{t_*}\rho\big(\rho\partial_\rho-\tfrac32-\bar S^C-\rho\tilde S\big)+P^C_b+Q\partial_{t_*}+R
\partial^2_{t_*},\tag{1.1}$$
with $\tilde S$ smooth, $Q\in\rho^3\mathrm{Diff}^1_{\mathrm b}$, $R\in\rho^2C^\infty$,
$P^C_b\in\rho^2\mathrm{Diff}^2_{\mathrm b}$, and $\bar S^C$ constant with spectrum
$\gamma_C\{2(1-v_C),(1-e_C)(1-v_C),1-v_C\ (\text{three times})\}$, all positive.

*Proof.* On $4+1$ Minkowski with $c = |x|^{-1}(dt-v\,d|x|)$ this is computed (10.18 (i), `cpmodes5.py` K1, exact): the
$\partial_{t_*}\partial_\rho$-coefficient is $2\,\mathrm{Id}$, there is no $\partial_{t_*}$ times a tangential
derivative, and $\bar S^C$ is $\frac r2$ times the $\partial_{t_*}$-coefficient less $\frac{n-1}2 = \frac32$. $g_b$
differs from $\bar g$ by $\rho^2C^\infty$ (III.B Proposition 3.6), and $c_C$ from the model's by $\rho^3C^\infty$; the
differences enter $\tilde S$, $Q$, $R$ and $P^C_b$ as in his proof of (6.4), by the same counting (10.21 (a); III.E
after Theorem 1.1). $\square$

**Lemma 1.3 (the indicial roots; [Hin26a] Theorem 4.9 at n = 4).** Let $h\in(0,10^{-6}]$ and $b$ near $b_0$.

(a) Every indicial root $\lambda$ of $P^C_b$ satisfies $\mathrm{Re}\,\lambda\notin[-100,\frac{19}{10}]$; the only roots
with real part in $[-100,2]$ are $\lambda = 2$ at scalar type 0 and at scalar type 1, each simple. At each type and
degree as many roots have real part $\ge2$ as $<-100$: three each at scalar type $l\ge1$, two each at scalar type 0, one
each at vector type $l\ge1$. The real parts accumulate only at $\pm\infty$.

(b) There is a countable set $\mathsf Z\subset(0,10^{-6}]$ such that for $h\notin\mathsf Z$ the roots are simple, and the
remaining clauses of III.E Theorem 1.1 (3) hold.

*Proof.* The indicial family of $P^C_b$ at $\partial X$ is that of the Minkowski model with $c = |x|^{-1}(dt-v_C\,d|x|)$,
independent of $b$: $g_b-\bar g\in\rho^2C^\infty$ and $c_C$'s deviation are of lower order (Lemma 1.2; his p. 29,
"indicial roots are determined by the leading-order ... part"). (a) is computed (10.54, Proposition 10.44, `uniform5.py`
H1-H2, exact): for each type the roots are those of an explicit polynomial in $(\lambda,\kappa,h)$, $\kappa = l(l+2)$,
whose leading coefficient in $\lambda$ does not vanish for $h>0$; Sturm sequences in $\kappa$ and $h$ and Hurwitz
determinants certify that no root crosses the lines $\mathrm{Re}\,\lambda = -100$, $\frac{19}{10}$, $2$ for
$h\in(0,10^{-6}]$, $\kappa\ge\kappa_0$, and at $l = 0,1$ the factor $\lambda-2$ divides for every $h$, its cofactors
treated alike. The accumulation is the top-weight computation (10.12 (U3)): the roots go as $\pm\kappa^{1/2}$, free of
$h$. (b) For each $l$, simplicity and each clause of III.E Theorem 1.1 (3) (a root not lying in a given finite set; a
root with integer real part in $[3,51]$ being real) is the nonvanishing of finitely many polynomials in $h$ (the
discriminant; the characteristic polynomial at the given points; the Hurwitz determinant of the polynomial shifted to
the line $\mathrm{Re}\,\lambda = k$), each nonzero at $h = 10^{-6}$ (10.52, 10.54 (d); III.E Theorem 1.1 (3), D231). So
each fails for finitely many $h$ at each $l$; only finitely many $l$ have roots with $|\lambda|\le51$, by the top-weight
growth; and the union over $l$ is countable. $\square$

**Lemma 1.4 (the 1-form; [Hin26a] Proposition 5.1 at n = 4).** With the weights
$$\alpha_K := 1,\qquad\alpha_{\mathrm{sf}} := -C_0-\tfrac52,\tag{2.1}$$
$w := \rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}+1}\rho_K^{\alpha_K}$ and $w' :=
\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}+1}$, $c_C$ satisfies his Proposition 5.1 (1)-(6) on Tangherlini $g_{b_0}$, for
some $\delta_r>0$ and with $\delta_{\mathrm{sf}} =
\frac1{100}$; and on $g_b$ for $b$ near $b_0$, with smaller $\delta_r$, $\delta_{\mathrm{sf}}$.

*Proof.* (1)-(3) and (6) off $\mathrm{sf}$: 10.14 Proposition 10.11 (i)-(iii) (`cform5.py` C1-C4, exact; Sturm on each
interval). (4)-(6) at $\mathrm{sf}$: the symbol $T = r^2(-\ell(dw/w)+S)$ depends only on $\rho_K$ and the weights there;
it is positive definite at $\partial K^+$ iff $b_K>b_{\mathrm{sf}}-b^*$ and at the sink iff $b_{\mathrm{sf}}<b^*$, with
$b_K = \alpha_K$, $b_{\mathrm{sf}} = \alpha_{\mathrm{sf}}+1$ and $b^* = 0.99340731\ldots$ (10.14 (iv), `cform5.py` C7);
at (2.1), $b_{\mathrm{sf}} = -C_0-\frac32$ and $b_K = 1$, the characteristic polynomials at $\partial K^+$ and at $R_v$
have positive roots for every $C_0\ge0$, and at $C_0 = 100$ $T$ is positive definite on all of $\mathrm{sf}$ with
$\rho_K\le10$ (10.22 Proposition 10.19 (iv), `solv5.py` Q4, exact). So (4) holds near $\partial K^+$ by continuity, and
(5) holds on $|\frac{r/t}v-1|\le2\delta_{\mathrm{sf}}$ because $T'$ at the sink does not depend on $\rho_K$ (10.22 (c));
this sentence is amended D308, finding (IV$'''''$3), where it read that $T$ is positive definite on $\mathrm{sf}$ for
every $C_0\in[0,100]$. Off $\mathrm{sf}$, for $\rho_{\mathrm{sf}}\le2\delta_r$, by continuity, as Tangherlini differs
from its Minkowski model by $\rho_{\mathrm{sf}} C^\infty$ terms (10.14 (a), his p. 39). His (5.8) holds on an interval
about $v$ of half-width below $0.00166$, which gives the conditions (6) on $\mathrm{sf}$ with $\delta_{\mathrm{sf}} =
\frac1{100}$ (10.14 (iv), C5). For $g_b$: each condition is a strict positivity of a continuous function of the metric
on a compact set, or holds at $\mathrm{sf}$, where $g_b$ and $g_{b_0}$ have the same 3sc model; so it persists for $b$
near $b_0$. $\square$

**Lemma 1.5 (the horizon threshold).** For $b$ near $b_0$ and every $h\in(0,10^{-6}]$, the threshold $\vartheta_{\mathcal
H}$ of I.A (PART-I-SPECTRAL.md after (1.3)) of the spectral family of $\Box^C_b$ satisfies $\frac12+\vartheta_{\mathcal
H}<-C_0$.

*Proof.* $\vartheta_{\mathcal H}$ is the maximum over the compact $\partial\mathcal R_\pm$ of the top eigenvalue of
$\beta_0^{-1}p_{1,\pm}(0)$, self-adjoint for the fibre inner product $B$ of Lemma 1.1. By its definition $p_{1,\pm}(0) =
A_\pm-h^{-1}\ell(\pm\rho_\infty\cdot)$-part, where $A_\pm$ comes from $2\delta G\delta^*$ and is free of $h$, and the
$h^{-1}$-part is $h^{-1}\rho_\infty$ times the damping symbol of $L$ at the conormal covectors of the horizon. These are
future null, so Lemma 1.1 (his Lemma 3.5) makes $\ell$ of them $B$-negative definite with the sign that damps. So, by
Weyl's inequality, $\vartheta_{\mathcal H}\le\vartheta_0(b)-c(b)h^{-1}$ with $\vartheta_0$ and $c>0$ continuous in $b$.
At $b_0$ both are computed (10.79, `hthresh5.py` T3-T5, exact): $\vartheta_0 = \frac{102401}{640}$ and the bound at $h =
10^{-6}$ is $-4839.95\ldots$, with the true value $\vartheta_{\mathcal H} = -4995.83\ldots$. So $\frac12+\vartheta_0(b)-
c(b)h^{-1}<-100$ for $b$ near $b_0$ and $h\le10^{-6}$, the margin at $b_0$ being more than $4700$. $\square$

**Lemma 1.6 (the hypotheses of Part I).** For $b$ near $b_0$ and $h\in(0,10^{-6}]$, the spectral family of $\Box^C_b$
satisfies (H1)-(H4) of I.A (PART-I-SPECTRAL.md (1.2)-(1.3)), and (G) of I.C for every $\alpha$ with $\alpha+2\in
[-C_0,2)$, with the gap $I = (\beta_-,2)$, $\beta_-<-C_0$.

*Proof.* (H1): the principal symbol of $\Box^C_b$ is that of $\Box_{g_b}\otimes\mathrm{Id}$, as $E^C$ is of order 0
and $2\delta G\delta^*$ has the scalar principal symbol $g^{-1}(\zeta,\zeta)$; so $\sigma_2(\hat P(0)) =
G_0\,\mathrm{Id}$, $\sigma_1(T) = \tau_1\mathrm{Id}$ with $\tau_1 = -H_Gt_*$, and $P_2 = g_{00}\mathrm{Id}$. (H2): Lemma
1.2, with $S =
\bar S^C+\rho\tilde S$ and $P^{(0)} := \rho^{-2}P^C_b$, whose principal part at $\partial X$ is that of the Euclidean
Laplacian in b-form, the first-order terms of $E^C$ (coefficients in $\rho C^\infty$) lying in $\mathrm{Diff}^1_{\mathrm
b}$. (H3)-(H4) concern only $G_0$ and $\tau_1$, that is $g_b$ and $t_*$: apart from the threshold in (H3), which is Lemma
1.5, they are part of (Dyn), the dynamical hypotheses on the metric alone, which Part VI checks for $g_b$, $b$ near $b_0$
(III.D's introduction), and they hold for every operator with principal part $\Box_{g_b}\otimes\mathrm{Id}$. (G): by
Lemma 1.3 (a) and I.C Lemma 2.2, the indicial roots relevant to the weight $\alpha+2$ (Euclidean density) are the
$\lambda$ with $\mathrm{Re}\,\lambda = \alpha+2$; none has real part in $[-100,\frac{19}{10}]\cup(\frac{19}{10},2)$, so
$(\beta_-,2)$ with $\beta_- := \max\{\mathrm{Re}\,\lambda<-100\}<-100\le-C_0$ is a gap. $\square$

## 2. Mode stability and the zero energy operator ([Hin26a] Theorem 6.2 at n = 4)

**Theorem 2.1 (III.E Theorem 1.1 (1)-(3) at n = 4).** With (0.1) and $b$ near $b_0$:

(1) for $\sigma\ne0$, $\mathrm{Im}\,\sigma\ge0$, $\widehat{\Box^C_b}(\sigma)$ has trivial nullspace on
$\mathcal A^\gamma(\bar X;E)$ for every $\gamma$;

(2) for every $\alpha$ with $\alpha+2\in[-C_0,2)$ and $s\ge-C_0$, $P^C_b:\{\omega\in\bar H^{s,\alpha}_{\mathrm
b}:P^C_b\omega\in\bar H^{s-1,\alpha+2}_{\mathrm b}\}\to\bar H^{s-1,\alpha+2}_{\mathrm b}$ (Euclidean density) is
invertible, and $\Box^C_b$ satisfies (H1)-(H4) with $\frac12+\vartheta_{\mathcal H}<-C_0$;

(3) the indicial roots are as in Lemma 1.3, with all clauses of III.E Theorem 1.1 (3) for $h\in\mathsf H$.

*Proof.* (3) is Lemma 1.3, and the second half of (2) is Lemmas 1.5-1.6. Theorem 5.2 at $n = 4$ (Part IV$'''''$) is
used with the weights (2.1), which its hypothesis at $n = 4$, $\alpha_{\mathrm{sf}}<b^*-1$ and
$\alpha_K>\alpha_{\mathrm{sf}} +1-b^*$ (Lemma 1.4; 10.22 (c)), allows, and with $C_0+1$ for $C_0$, as in the source (p.
67).

*(1).* Let $\omega'\in\mathcal A^\gamma(\bar X;E)$ with $\widehat{\Box^C_b}(\sigma)\omega' = 0$, and $\omega :=
e^{-i\sigma t_*}\omega'$, a solution of $\Box^C_b\omega = 0$. It is outgoing in the source's sense (Definition 6.1):
$t_* = t-\psi(|x|)$ with $\psi(r) = r-C_\psi+8\mu_0r^{-1}$ for large $r$ (III.B (3.6)), and the tortoise coordinate of
$g_{b_0}$ is $r_* = r-\mu_0r^{-1}+O(r^{-3})$ ($dr_*/dr = (1-\mu_0r^{-2})^{-1}$), so $\omega = e^{-i\sigma t}e^{i\sigma
r_*}\omega_1$ with $\omega_1 = e^{i\sigma(\psi-r_*)}\omega'\in\mathcal A^\gamma$, $\psi-r_*$ being bounded and
conormal. By (1.1),
$$2i\sigma\rho\big(\rho\partial_\rho-\tfrac32-\bar S^C\big)\omega'\in\big(\rho^2\mathrm{Diff}^2_{\mathrm b}+\sigma\rho^3
\mathrm{Diff}^1_{\mathrm b}+\sigma^2\rho^2\mathrm{Diff}^0_{\mathrm b}\big)\omega'\subset\mathcal A^{\gamma+2},$$
the term $\rho\tilde S$ of (1.1) included in the first class. Dividing by $2i\sigma\rho$ and solving the
regular-singular equation in $\rho$ gives $\omega'\in\mathcal A^{\gamma+1}$ as long as
$\gamma+1<\frac32+\min\mathrm{spec}\,\bar S^C$; iterating, $\omega'\in\mathcal A^1$, as $\bar S^C>0$ (Lemma 1.2).
Theorem 5.2 is applied in Part IV$'''''$'s Kerr-Schild coordinates (its Remark 7.4), in which $t =
t_{\mathrm{KS}}+T_\mu(|x|)$ (III.B (3.3)). The data $(\omega,r\mathcal L_{\partial_t}\omega)|_{t_{\mathrm{KS}}=0} =
(e^{i\sigma(\psi-T_\mu)}\omega',-i\sigma re^{i\sigma(\psi-T_\mu)}\omega')$ satisfy $|\omega^{(0)}|\le Cr^{-1}$,
$|\omega^{(1)}|\le C$. Indeed $|e^{i\sigma(\psi-T_\mu)}| = e^{-(\mathrm{Im}\,\sigma)(\psi-T_\mu)}$ is bounded,
$\psi-T_\mu$ being continuous on $[r_\sharp,\infty)$ and tending to $+\infty$ (amended D308; the data were taken at $\{t
= 0\}$ of III.B's $t$, which is not shown to be a time function, finding (IV$'''''$1)); so they lie in
$\rho^{-2-\epsilon}\bar H^{1-j}_{\mathrm b}(X,r^3|dr\,d\slashed g|)$ for every $\epsilon>0$ (10.18 (iii): $\rho^k\in
\rho^aL^2(r^3dr)$ near $\partial X$ iff $a<k-2$), which lies in $\rho^{\alpha_{\mathrm{sf}}+\frac12}\bar
H^{1-j}_{\mathrm b}$, as $\alpha_{\mathrm{sf}}+\frac12 = -C_0-2<-2-\epsilon$. Theorem 5.2's initial value problem (its
(5.16) at $n = 4$) gives $\omega\in\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\rho_K^{\alpha_K}\bar H^1_{3\mathrm
b}(\Omega,|dg|)$. On $[0,\infty)_t\times A$, $A = \{r_1\le r\le r_2\}$ an annulus, $\rho_{\mathrm{sf}}$ is bounded above
and below and $\rho_K = r/t$, so $\int_0^\infty\int_A(t/r)^2|\omega|^2<\infty$ with $|\omega| =
e^{(\mathrm{Im}\,\sigma)t_*}|\omega'|$, which forces $\omega' = 0$ on $A$, for every annulus. So $\omega = 0$.

*(2), injectivity.* Let $u$ be in the kernel. By I.C Theorem 3.1 (2) (Lemmas 1.5-1.6), $u$ is smooth up to the inner
boundary and lies in $\mathcal A^\beta$ near $\partial X$ for every $\beta<2$. So $\omega(t,x) := u(x)$ solves
$\Box^C_b\omega = 0$ with data $(u,0)$ in $\rho^{\alpha_{\mathrm{sf}}+\frac12}\bar H^1_{\mathrm b}\oplus0$, and Theorem
5.2 gives $\omega\in\rho_K^{\alpha_K}L^2$ over $[0,\infty)\times A$ as in (1), which for a stationary $\omega$ forces $u
= 0$. (The source's alternative for $s<1$, the cut-off $\chi(\tau)$, is not needed: by I.C Theorem 3.1 (3) the kernel
does not depend on $s>\frac12+\vartheta_{\mathcal H}$, and $-C_0>\frac12+\vartheta_{\mathcal H}$ by Lemma 1.5.)

*(2), surjectivity.* By I.C Theorem 3.1 (1), $P^C_b:\mathcal X_0\to\mathcal Y_0$ is Fredholm and the annihilator of its
range is $\ker_{\mathcal X^*_0}(P^C_b)^{*}$, $\mathcal X^*_0\subset\dot H^{1-s,-\alpha-2}_{\mathrm b}$ (supported at the
inner boundary). Let $v$ be in that kernel. The indicial roots of $(P^C_b)^*$ are $2-\bar\lambda$ (III.E Lemma 2.1 (2),
which uses only Lemma 1.3), with real part $\le0$ or $>C_0+2$. As $\alpha+2<2$, $v$ has pointwise weight $-\alpha>0$ at
$\partial X$, so the normal operator argument (the expansion of $v$ along the roots of real part above its weight, I.C
Theorem 3.1 (2) for the adjoint) gives $v\in\mathcal A^{C_0+2-\epsilon}$ near $\partial X$ for every $\epsilon>0$, the
roots of real part $\le0$ being below the weight. So $\omega'(t,x) := v(x)$ is a stationary solution of $(\Box^C_b)^*
\omega' = 0$ lying in $\rho_{\mathrm{sf}}^{-\alpha_{\mathrm{sf}}-2}\rho_K^{-\alpha_K}H^{s'}_{3\mathrm
b}(\Omega)^{-,\bullet}$ for $s' = 1-s$ near $\partial X$: $-\alpha_{\mathrm{sf}}-2 = C_0+\frac12$, the decay
$C_0+2-\epsilon$ exceeding it after the shift $\frac32$ between the pointwise and the $L^2$ weight with $|dg|$ (the
source's shift, at $n = 4$ that of $\rho^a L^2(r^3dr)$ plus $\frac12$ from the slab, 10.18 (iii)), and $\rho_K^{-1}$
allowing a stationary function, as $\int^\infty(r/t)^2dt<\infty$. The adjoint estimate (5.81) of Theorem 5.2's proof at
$n = 4$ (Part IV$'''''$) makes $(\Box^C_b)^*$ injective there, so $v = 0$. So $P^C_b$ is surjective, hence invertible,
and by I.C Theorem 3.1 (4) the estimates hold without the error terms. $\square$

The source's other two routes to surjectivity, the index 0 from its Theorem B.1 with [Hin26c] Corollary 9.43 (here I.C
Corollary 6.6) and the radial ordinary differential operators of a static metric with its Theorem 4.9 (3), are not used:
the first needs (TF) and the index at $\sigma\ne0$, the second an index count for operators that are singular at the
horizon. The adjoint route needs only what Theorem 5.2's proof provides.

## 3. Findings, labels and sources

(IV$''''$1) *The range of $\gamma_C$.* III.E Theorem 1.1 is stated "for all sufficiently large $\gamma_C$". At $n = 4$ it
is proved for $\gamma_C = h^{-1}$ with $h\in\mathsf H$: every $h<\min(10^{-6},h_0)$ outside a countable set, the
exceptional set coming from the simplicity of the roots and III.E (3)'s added clauses (Lemma 1.3 (b); 10.54 (d)). Every
use in Part III takes one admissible $\gamma_C$, so the countable exception is harmless; III.E's statement should read
"for all $\gamma_C>1/h_*$ outside a countable set".

(IV$''''$2) *The parameter point.* The record's inputs are computed at $v_C = \frac12$, $e_C = \frac1{102400}$, $C_0\le
100$, which is what III.K section 0 fixes; III.E Theorem 1.1's "Fix $v_C\in(0,1)$ and $C_0>0$" is proved here at that
point, not for every $v_C$ and $C_0$.

(IV$''''$3) *Surjectivity by the adjoint estimate.* The zero energy operator's surjectivity is taken from the adjoint
estimate (5.81) and the indicial roots, the source's third route, which avoids an index count.

(IV$''''$4) *Theorem 5.2 at $n = 4$.* (1) and (2) rest on [Hin26a] Theorem 5.2 at $n = 4$, (5.16) and (5.81), which Part
IV$'''''$ proves (Theorem 7.3, D308); its inputs are Lemmas 1.1, 1.4 and the 3b-geometry of Tangherlini (10.22
Proposition 10.19 (i)-(iii)).

(IV$''''$5) *What is used of Part I.* I.C Theorem 3.1 ([Hin26c] Theorem 9.36) needs (H1)-(H4) and (G) only; (H3)-(H4)
come from (Dyn) except for the threshold, Lemma 1.5, which at $n = 4$ holds with a margin of more than 4700 at the
record's point.

*Labels.* Lemma 1.1 is the source's Lemmas 3.3-3.8, Lemma 1.2 its (6.4), Lemma 1.3 its Theorem 4.9, Lemma 1.4 its
Proposition 5.1, Lemma 1.5 the threshold of [Hin26c] (5.17) for $\Box^C$ (the source's Remark 5.7 mechanism), Theorem
2.1 its Theorem 6.2 and [Hin26] Theorem 7.1 (1)-(3).

*Sources.* [Hin26a] pp. 25-28 (section 3), 29-37 (section 4, Theorem 4.9), 37-41 (Proposition 5.1 with its proof, (5.1)-
(5.6)), 41-42 (Theorem 5.2, (5.14)-(5.16)), 66-69 (section 6: Definition 6.1, Theorem 6.2 and its proof, (6.1)-(6.4),
Remarks 6.3-6.4), read at source. Inputs: N1STAR-PROOF.md 10.12-10.14, 10.18, 10.21-10.22, 10.52, 10.54, 10.79 and the
instruments named there; I.A (H1)-(H4); I.C Theorem 3.1, Lemma 2.2, Corollary 6.6; III.B Proposition 3.6; III.E section
1, Theorem 1.1, Lemma 2.1 (2).
