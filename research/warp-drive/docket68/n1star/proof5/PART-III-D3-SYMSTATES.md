# Part III.D″. Zero energy states from the symmetries of Minkowski space, at n = 4 ([Hin26] section 6.5.1)

*Status.* Proved (D231: verifier 95 read the repairs, correct; status synchronised with the README at D325). Verified
(D229: read in full by the ninety-fourth verifier, its one minor finding and one nit seated and to be read); written
(D223). This part proves, at spatial dimension $n = 4$ and for the Myers-Perry metrics $g_b$, $b$ near $b_0 =
(\mu_0,0)$, what [Hin26] section 6.5.1 establishes (pp. 125-128): the comparison of the operators of $g_b$ with those of
Minkowski space and of the non-rotating member of the family (his Lemma 6.14), and the stationary solutions of the gauge
potential wave equation whose leading terms are the time translation, the spatial translations, the Lorentz boosts and
the rotations of Minkowski space, with their symmetric gradients (Proposition 6.15 and Remarks 6.16-6.17). Part III.D$'$
is cited as III.D$'$, and the other parts as in III.D$'$. Computations cited as *computed* are exact (sympy) and rerun
by the instruments named (D223).

*What n = 4 changes.* The mass of $g_b$ enters at $|x|^{-2}$ and the rotation at $|x|^{-3}$ (III.B (3.5)), where Kerr's
enter at $|x|^{-1}$ and $|x|^{-2}$, so every comparison of Lemma 6.14 gains one power of $\rho$, and so do the
corrections and the symmetric gradients built from it. The correction to the boost then sits at $\rho^1$, which is no
indicial root, so the source's logarithm (6.31) and its use of the formal solution lemma do not occur; the corrections
to the translations and rotations sit at $\rho^2$, which is an s1 root when $e_\Upsilon\gamma_\Upsilon^2 = 0$, so here
the modification at infinity is used with $e_\Upsilon>0$, $\gamma_\Upsilon\ne0$. Findings are in section 4.

## 1. Setting and notation

$\mathcal B$, $g_b$ ($b = (\mu,A)$, $A\in\mathfrak{so}(4)$), $t_*$, $\rho = |x|^{-1}$ near infinity, the trivialisation
by $dt_*,dx^1,\dots,dx^4$ and the bundle $E$ are as in III.D section 1, and $g_\mu := g_{(\mu,0)}$, the five-dimensional
Schwarzschild-Tangherlini metric of mass parameter $\mu$. The model metric is $\bar g = -d\bar t^2+dx^2$, $\bar t :=
t_*+|x|$ (III.D (D1)), with operators $\bar\delta^*$, $\bar\Box^\Upsilon := \Box^\Upsilon_{\bar g,\bar E_\Upsilon}$
(III.D section 3). Fix $\gamma_{\Upsilon,H}\in(0,\epsilon_0]$ and then $b\in\mathcal B(\gamma_{\Upsilon,H})$,
$e_\Upsilon\in(0,\epsilon_1]$ and $0<|\gamma_\Upsilon|<\epsilon_1$ as in III.D$'$ Proposition 4.1, so that

$$z := 4e_\Upsilon\gamma_\Upsilon^2\in(0,\tfrac12],\tag{1.1}$$

and write $\Box^\Upsilon_b := \Box^\Upsilon_{g_b,E_\Upsilon}$. We take $c_\Upsilon$ and $c_{\Upsilon,H}$ invariant under
the rotations of $x$ ($c_\Upsilon = \zeta(|x|)|x|^{-1}dt$ with $\zeta = 1$ for large $|x|$, and $c_{\Upsilon,H} =
-\frac12\chi(|x|)\,d|x|$), which III.B Definition 6.1 and III.D sections 1 and 5.1 allow. By III.D$'$ Proposition 4.1
and Lemma 5.1, $\widehat{\Box^\Upsilon_b}(0)$ is invertible on the b-spaces with an unweighted b-density, for every
$s>\frac32$ and every weight in the gap $(0,\lambda^\Upsilon_{\mathrm s1,2})$, and maps $\mathcal A^{2+\mathcal E}$,
$\min\mathrm{Re}\,\mathcal E>0$, into polyhomogeneous spaces. *All b-spaces in this part use an unweighted b-density
near $\partial X$*, as the source's section 6.5 does.

*Indicial roots.* By III.D Lemma 4.1 the indicial roots of $\widehat{\Box^\Upsilon_b}(0)$ do not depend on $b$ or on the
horizon modification, and for $0<z\le\frac12$: at s0 they are $0$, $3$, $\lambda^\Upsilon_{\mathrm s0,2} =
\frac12+(\frac94+z)^{1/2}\in(2,3)$ and $1-\lambda^\Upsilon_{\mathrm s0,2}$; at s1 they are $0$, $4$,
$\lambda^\Upsilon_{\mathrm s1,2}\in(2,\lambda^\Upsilon_{\mathrm s0,2})$, a root in $(3,4)$, and their mirror images
$1-\lambda$; at sl, $l\ge2$, and vl, $l\ge1$, every root is $\le0$ or $\ge3$. In particular *neither 1 nor 2 is an
indicial root, of any type* (computed: `genstates5.py` H5, `zstates5.py` Z2, Z3, Z5). Fix $\epsilon_{\mathrm{ind}}>0$
less than $d(\mathrm{Re}\,\lambda,\mathbb Z)$ for every indicial root $\lambda$ with $\mathrm{Re}\,\lambda\notin\mathbb
Z$ and $|\mathrm{Re}\,\lambda|\le10$. As in the source, $\mathcal E_{\mathrm{ind}}$ denotes an index set with
$\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}\ge\epsilon_{\mathrm{ind}}$, which may change from line to line, and $(k,0)$
the index set $\{(k+j,0):j\in\mathbb N_0\}$.

*The model symmetries* ((6.29) at n = 4). For $S\in\mathcal S_1$, so $|x|S = \xi\cdot x$ for some $\xi\in\mathbb R^4$,
and $V\in\mathcal V_1$, so $V = \sum_{i<j}c_{ij}(x^i\,dx^j-x^j\,dx^i)$ with $c\in\mathfrak{so}(4)$ (the Euclidean duals
of the rotation fields; III.A$'$ Definition 2.2),

$$\bar\omega^{(0)}_{\mathrm s0} := \bar g(\partial_{t_*},\cdot) = -d\bar t,\quad\bar\omega^{(0)}_{\mathrm s1}(S) :
= d(|x|S),\quad\breve{\bar\omega}^{(0),1}_{\mathrm s1}(S) := |x|\,d(|x|S)-|x|S\,d\bar t,
\quad\bar\omega^{(-1)}_{\mathrm v1}(V) := V.\tag{1.2}$$

$\bar\omega_{\mathrm s1}(S) = \xi\cdot dx$ is dual to a translation, $\bar B(S) := t_*\bar\omega_{\mathrm
s1}(S)+\breve{\bar\omega}^1_{\mathrm s1}(S) = \bar t\,d(\xi\cdot x)-(\xi\cdot x)\,d\bar t$ to a Lorentz boost, and $V$
to the rotation field $R_V := \bar g^{-1}V = \sum c_{ij}(x^i\partial_j-x^j\partial_i)$ (the same vector field in the
coordinates $(\bar t,x)$ and $(t_*,x)$, as $R_V|x| = 0$). All four are Killing 1-forms of $\bar g$, so $\bar\delta^*$
annihilates them and $\bar\Box^\Upsilon = 2\bar\delta_{\bar E}\bar G\bar\delta^*$ does too. Their components are smooth
on $\bar X$, of orders $\rho^0$, $\rho^0$, $\rho^{-1}$ and $\rho^{-1}$.

## 2. Comparison of operators ([Hin26] Lemma 6.14 at n = 4)

**Lemma 2.1.** For $b = (\mu,A)\in\mathcal B$, near $\partial X$ and on stationary sections,

$$\widehat{\delta^*_{g_b}}(0)\in\rho\,\mathrm{Diff}^1_{\mathrm b},
\qquad\widehat{\delta^*_{g_b}}(0)-\widehat{\bar\delta^*}(0)\in\rho^3\mathrm{Diff}^0_{\mathrm b},
\qquad\widehat{\delta^*_{g_b}}(0)-\widehat{\delta^*_{g_\mu}}(0)\in\rho^4\mathrm{Diff}^0_{\mathrm b},\tag{2.1}$$

$$\widehat{\Box^\Upsilon_b}(0)\in\rho^2\mathrm{Diff}^2_{\mathrm b},
\qquad\widehat{\Box^\Upsilon_b}(0)-\widehat{\bar\Box^\Upsilon}(0)\in\rho^4\mathrm{Diff}^2_{\mathrm b},
\qquad\widehat{\Box^\Upsilon_b}(0)-\widehat{\Box^\Upsilon_{g_\mu,E_\Upsilon}}(0)\in\rho^5\mathrm{Diff}^2_{\mathrm b},
\tag{2.2}$$

and $[\Box^\Upsilon_b,t_*]\in\rho\,\mathrm{Diff}^1_{\mathrm b}$,
$[\Box^\Upsilon_b-\Box^\Upsilon_{g_\mu,E_\Upsilon},t_*]\in\rho^4\mathrm{Diff}^1_{\mathrm b}$ on stationary sections.
(The source has $\rho^2$, $\rho^3$ in (2.1) and $\rho^3$, $\rho^4$ in (2.2).)

*Proof.* Near $\partial X$ the components of $g_b$, $g_b^{-1}$, $\bar g$, $\bar g^{-1}$ in the coordinates $(t_*,x)$ are
smooth functions on $\bar X$ (functions of $(\rho,\hat x)$, $\hat x = x/|x|$), and

$$g_b-\bar g\in\rho^2C^\infty,\qquad g_b-g_\mu\in\rho^3C^\infty,\tag{2.3}$$

and the same for the inverses. Indeed III.B (3.5) gives $g_b-g_\mu\in|x|^{-3}C^\infty$ and
$g_\mu-\eta\in|x|^{-2}C^\infty$, $\eta = -dt^2+dx^2$, with the duals; by III.B (3.6), $\bar t = t+C'-8\mu_0|x|^{-1}$
near infinity, so $\bar g-\eta = -16\mu_0|x|^{-2}\,dt\,d|x|-64\mu_0^2|x|^{-4}d|x|^2\in|x|^{-2}C^\infty$; and the frame
change $dt = dt_*+(1-8\mu_0|x|^{-2})\,d|x|$ has coefficients smooth on $\bar X$, so it preserves $\rho^kC^\infty$. The
Cartesian derivatives $\partial_{x^i}$ lie in $\rho\,\mathrm{Diff}^1_{\mathrm b}$ (they are $\rho$ times b-vector fields
with coefficients smooth on $\bar X$), and $\partial_{t_*}$ annihilates stationary sections. Hence $\Gamma(g)\in\rho
C^\infty$ for $g = g_b,\bar g$, and $g_1-g_2\in\rho^kC^\infty$ (with the inverses) implies
$\Gamma(g_1)-\Gamma(g_2)\in\rho^{k+1}C^\infty$. On stationary 1-forms $\delta^*_g\omega =
\frac12(\partial_\mu\omega_\nu+\partial_\nu\omega_\mu)-\Gamma^\lambda_{\mu\nu}\omega_\lambda$, whose first part does not
depend on $g$: this gives (2.1) with $k = 2$, $3$. For (2.2): $\delta_g = -g^{\mu\nu}\nabla_\mu$ is in
$\rho\,\mathrm{Diff}^1_{\mathrm b}$ with $\delta_{g_1}-\delta_{g_2}\in\rho^{k+1}\mathrm{Diff}^1_{\mathrm b}$;
$G_{g_1}-G_{g_2}\in\rho^k\mathrm{Diff}^0_{\mathrm b}$; and near $\partial X$, $E^\Upsilon_{g}h =
-\gamma_\Upsilon(2\iota_{g^{-1}c_\Upsilon}h-\frac23(1-e_\Upsilon)c_\Upsilon\mathrm{tr}_gh)$ with $c_\Upsilon\in\rho
C^\infty$ (III.B Definition 6.1; the horizon term is supported in $\{|x|<5R_1\}$), so
$E^\Upsilon_g\in\rho\,\mathrm{Diff}^0_{\mathrm b}$ and
$E^\Upsilon_{g_1}-E^\Upsilon_{g_2}\in\rho^{k+1}\mathrm{Diff}^0_{\mathrm b}$; the model's $\bar E_\Upsilon$ uses $c
= |x|^{-1}d\bar t$, which differs from $c_\Upsilon$ by $\rho^3C^\infty$. Expanding
$2(\delta_1+E_1)G_1\delta^*_1-2(\delta_2+E_2)G_2\delta^*_2$ into terms each containing one difference gives
$\rho^{k+2}\mathrm{Diff}^2_{\mathrm b}$, and $\Box^\Upsilon_b(0)\in\rho^2\mathrm{Diff}^2_{\mathrm b}$ in the same way.
For the commutators: on stationary sections $[\Box^\Upsilon_g,t_*]$ is the first-order operator obtained from the terms
of $\Box^\Upsilon_g$ with one $\partial_{t_*}$ (those with $\partial_{t_*}^2$ give $2\partial_{t_*}$, which vanishes on
stationary sections); these are $-2g^{t_*\nu}\partial_\nu$ plus connection and $E$ terms, so the same counting applies,
with $g^{t_*\nu}\in C^\infty$ and its differences in $\rho^kC^\infty$; and III.D Lemma 2.1 (2)-(3) gives
$[\Box^\Upsilon_b,t_*] = -2\rho(\rho\partial_\rho-\frac32-\bar S)+Q_b\in\rho\,\mathrm{Diff}^1_{\mathrm b}$. $\square$

**Lemma 2.2 (smooth dependence on b).** Let $\alpha\in(0,\lambda^\Upsilon_{\mathrm s1,2})$ and let $b\mapsto f_b$ be of
class $C^k$ from $\mathcal B(\gamma_{\Upsilon,H})$ into $\bar H^{s-1,\alpha+2}_{\mathrm b}$ for every $s$. Then
$b\mapsto u_b := \widehat{\Box^\Upsilon_b}(0)^{-1}f_b$ is of class $C^k$ into $\bar H^{s,\alpha}_{\mathrm b}$ for every
$s$, and its derivatives are the inverse images $\partial_bu_b =
\widehat{\Box^\Upsilon_b}(0)^{-1}(\partial_bf_b-(\partial_b\widehat{\Box^\Upsilon_b}(0))u_b)$ and their iterates.

*Proof.* Write $P_b := \widehat{\Box^\Upsilon_b}(0)$. As in the proof of III.D$'$ Lemma 5.1 (2), $u_b\in\bigcap_s\bar
H^{s,\alpha}_{\mathrm b}$. The coefficients of $P_b$ depend smoothly on $b$ in $C^\infty$ (III.B Proposition 3.6), so
$P_{b'}-P_b$ maps $\bar H^{s+1,\alpha}_{\mathrm b}$ to $\bar H^{s-1,\alpha+2}_{\mathrm b}$ with norm $O(|b'-b|)$; and
$\|P_{b'}^{-1}\|_{\bar H^{s-1,\alpha+2}_{\mathrm b}\to\bar H^{s,\alpha}_{\mathrm b}}$ is bounded for $b'$ near $b$, by
I.C Theorem 7.1 (2) (the estimate without error term, uniform near a point where (Z) holds). So $u_{b'}-u_b =
P_{b'}^{-1}\big((f_{b'}-f_b)-(P_{b'}-P_b)u_b\big)\to0$ in $\bar H^{s,\alpha}_{\mathrm b}$; that is, $b\mapsto P_b^{-1}w$
is continuous for every fixed $w$ in $\bigcap_s\bar H^{s-1,\alpha+2}_{\mathrm b}$, uniformly on bounded sets of each
$\bar H^{s-1,\alpha+2}_{\mathrm b}$. With $\dot u := P_b^{-1}(\dot f-\dot Pu_b)$,

$$\frac{u_{b+h}-u_b}h-\dot u
= P_{b+h}^{-1}\Big(\frac{f_{b+h}-f_b}h-\frac{P_{b+h}-P_b}hu_b\Big)-P_b^{-1}\big(\dot f-\dot Pu_b\big)\to0,$$

since the bracket converges in every $\bar H^{s-1,\alpha+2}_{\mathrm b}$ and $P_{b+h}^{-1}\to P_b^{-1}$ strongly there.
Induction gives $C^k$. $\square$

## 3. The states ([Hin26] Proposition 6.15 at n = 4)

**Proposition 3.1.** Assume (Dyn), and let $E_\Upsilon$ and $b$ be as in section 1. There are stationary 1-forms, linear
in $S\in\mathcal S_1$ and $V\in\mathcal V_1$ and smooth in $b$,

$$\omega^{(0)}_{b,\mathrm s0} := g_b(\partial_{t_*},\cdot),\quad\omega^{(0)}_{b,\mathrm s1}(S),
\quad\breve\omega^{(0),1}_{b,\mathrm s1}(S),\quad\omega^{(-1)}_{b,\mathrm v1}(V),\tag{3.1}$$

smooth on $X$, with components in $\rho^{-1}C^\infty(\bar X)$ at most (the source's footnote 72; D229), with

$$\omega^{(0)}_{b,\mathrm s0}-\bar\omega^{(0)}_{\mathrm s0}\in\rho^2C^\infty,
\qquad\omega^{(0)}_{b,\mathrm s1}(S)-\bar\omega^{(0)}_{\mathrm s1}(S)\in\mathcal A^{(2,0)\cup(2+\mathcal E_{
\mathrm{ind}})},$$
$$\breve\omega^{(0),1}_{b,\mathrm s1}(S)-\breve{\bar\omega}^{(0),1}_{\mathrm s1}(S)\in\mathcal A^{(1,0)\cup(1+
\mathcal E_{\mathrm{ind}})},
\qquad\omega^{(-1)}_{b,\mathrm v1}(V)-V\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})},\tag{3.2}$$

such that

$$\Box^\Upsilon_b\omega^{(0)}_{b,\mathrm s0} = 0,\quad\Box^\Upsilon_b\omega^{(0)}_{b,\mathrm s1}(S) = 0,
\quad\Box^\Upsilon_b\big(t_*\omega^{(0)}_{b,\mathrm s1}(S)+\breve\omega^{(0),1}_{b,\mathrm s1}(S)\big) = 0,
\quad\Box^\Upsilon_b\omega^{(-1)}_{b,\mathrm v1}(V) = 0.\tag{3.3}$$

(1) (*No logarithm.*) In place of the source's (6.31): the correction to the boost has no logarithmic term;
$c_{b,\mathrm s1} = 0$.

(2) (*Symmetric gradients.*) $\delta^*_{g_b}\omega^{(0)}_{b,\mathrm s0} = 0$, and

$$h_{b,\mathrm s1}(S) :
= \delta^*_{g_b}\omega^{(0)}_{b,\mathrm s1}(S)\in\mathcal A^{(3,0)\cup(3+\mathcal E_{\mathrm{ind}})},
\qquad\delta^*_{g_b}\big(t_*\omega^{(0)}_{b,\mathrm s1}(S)+\breve\omega^{(0),1}_{b,\mathrm s1}(S)\big)
=: t_*h_{b,\mathrm s1}(S)+\breve h^1_{b,\mathrm s1}(S),$$
$$\breve h^1_{b,\mathrm s1}(S)\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})},\qquad h_{b,\mathrm v1}(V) :
= \delta^*_{g_b}\omega^{(-1)}_{b,\mathrm v1}(V)\in\mathcal A^{(3,0)\cup(3+\mathcal E_{\mathrm{ind}})},\tag{3.4}$$

the $\rho^2$ leading term of $\breve h^1_{b,\mathrm s1}(S)$ is of scalar type 1, given by the same $S$, and
$h_{b,\mathrm s1}(S)$, $t_*h_{b,\mathrm s1}(S)+\breve h^1_{b,\mathrm s1}(S)$ and $h_{b,\mathrm v1}(V)$ lie in the
kernels of $D_{g_b}\mathrm{Ric}$ and of $\delta_{g_b,E_\Upsilon}G_{g_b}$.

(3) (*Killing rotations*, Remark 6.17.) If $R_V$ is a Killing field of $g_b$, then $\omega^{(-1)}_{b,\mathrm v1}(V) =
g_b(R_V,\cdot)$ and $h_{b,\mathrm v1}(V) = 0$. At $b = (\mu,0)$ this holds for every $V\in\mathcal V_1$, six independent
rotations (the source has three).

*Proof.* Throughout, $P_b := \widehat{\Box^\Upsilon_b}(0)$, and we use two facts. (F1) If $f\in\mathcal A^{2+\mathcal
F}$ is smooth on $\bar X$, $\mathcal F$ an index set with $\min\mathrm{Re}\,\mathcal F = k\in\{1,2\}$ and $(k,0)$ its
only element with real part below $k+\epsilon_{\mathrm{ind}}$, then $P_b^{-1}f\in\mathcal A^{(k,0)\cup(k+\mathcal
E_{\mathrm{ind}})}$. Indeed, by III.D$'$ Lemma 5.1, $u := P_b^{-1}f\in\bigcap_s\bar H^{s,\alpha}_{\mathrm b}$ for every
$\alpha<k$ in the gap (as $k\le2<\lambda^\Upsilon_{\mathrm s1,2}$), and III.A Lemma 1.4 with $A = \rho^{-2}P_b$ near
$\partial X$ (I.C (1.1)) and $\alpha\in(k-\epsilon_{\mathrm{ind}},k)$ gives $u\in\mathcal A^{\mathcal E}$ with $\mathcal
E$ generated by $\mathcal F$ and the boundary spectrum above $\alpha$; the latter has no point with real part in
$(k-\epsilon_{\mathrm{ind}},k+\epsilon_{\mathrm{ind}})$ (no root at 1 or 2, section 1), so the only element of $\mathcal
E$ there is $\mathcal F$'s $(k,0)$, without logarithm. (F2) For a Killing 1-form $K$ of $g_b$, $\delta^*_{g_b}K = 0$,
hence $\Box^\Upsilon_bK = 0$; and for any stationary 1-form $\omega$, $h := \delta^*_{g_b}\omega$ satisfies
$D_{g_b}\mathrm{Ric}(h) = \frac12\mathcal L_{\omega^\sharp}\mathrm{Ric}(g_b) = 0$ and $\delta_{g_b,E_\Upsilon}G_{g_b}h =
\frac12\Box^\Upsilon_b\omega$; the same holds for $t_*\omega+\breve\omega$.

*Time translation.* $\partial_{t_*}$ is Killing for $g_b$, so (F2) gives $\Box^\Upsilon_b\omega_{b,\mathrm s0} = 0$ and
$\delta^*\omega_{b,\mathrm s0} = 0$; and $\omega_{b,\mathrm s0}-\bar\omega_{\mathrm s0} = (g_b-\bar
g)(\partial_{t_*},\cdot)\in\rho^2C^\infty$ by (2.3).

*Translations.* $\bar\delta^*\bar\omega_{\mathrm s1} = 0$, so by (2.1) $\delta^*_{g_b}\bar\omega_{\mathrm s1} =
(\widehat{\delta^*_{g_b}}(0)-\widehat{\bar\delta^*}(0))\bar\omega_{\mathrm s1}\in\rho^3C^\infty$, and $f_b :=
\Box^\Upsilon_b\bar\omega_{\mathrm s1} = 2\delta_{g_b,E_\Upsilon}G_{g_b}\delta^*_{g_b}\bar\omega_{\mathrm s1}$ is smooth
on $\bar X$ and in $\rho^4C^\infty$ near $\partial X$
($\delta_{g_b}+E^\Upsilon_{g_b,\infty}\in\rho\,\mathrm{Diff}^1_{\mathrm b}$ there), that is in $\mathcal A^{2+(2,0)}$.
By (F1) with $k = 2$, $\omega'_b := -P_b^{-1}f_b\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$, and
$\omega_{b,\mathrm s1} := \bar\omega_{\mathrm s1}+\omega'_b$ solves $\Box^\Upsilon_b\omega_{b,\mathrm s1} =
f_b+P_b\omega'_b = 0$. Then $h_{b,\mathrm s1} =
\widehat{\delta^*_{g_b}}(0)\omega'_b+(\widehat{\delta^*_{g_b}}(0)-\widehat{\bar\delta^*}(0))\bar\omega_{\mathrm
s1}\in\rho\,\mathrm{Diff}^1_{\mathrm b}\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}+\rho^3C^\infty\subset\mathcal
A^{(3,0)\cup(3+\mathcal E_{\mathrm{ind}})}$. $f_b$ depends smoothly on $b$ in $\rho^4C^\infty$, so Lemma 2.2 gives
smoothness in $b$.

*Boosts.* $\bar B = t_*\bar\omega_{\mathrm s1}+\breve{\bar\omega}^1_{\mathrm s1}$ is Killing for $\bar g$, so
$\bar\Box^\Upsilon\bar B = 0$, and $\bar\Box^\Upsilon\bar\omega_{\mathrm s1} = 0$. Hence

$$\breve f_b := \Box^\Upsilon_b\big(t_*\omega_{b,\mathrm s1}+\breve{\bar\omega}^1_{\mathrm s1}\big)
= [\Box^\Upsilon_b-\bar\Box^\Upsilon,
t_*]\bar\omega_{\mathrm s1}+\big(\widehat{\Box^\Upsilon_b}(0)-\widehat{\bar\Box^\Upsilon}(0)\big)\breve{\bar
\omega}^1_{\mathrm s1}+[\Box^\Upsilon_b,
t_*]\omega'_b,\tag{3.5}$$

as the terms with a factor $t_*$, $t_*(\Box^\Upsilon_b-\bar\Box^\Upsilon)\bar\omega_{\mathrm s1} = t_*f_b$ and
$t_*\Box^\Upsilon_b\omega'_b = -t_*f_b$, cancel. By III.D Lemma 2.1 (3), near $\partial X$,
$\Box^\Upsilon_b-\bar\Box^\Upsilon = -g_b^{00}\partial_{t_*}^2+Q_b\partial_{t_*}+R_b$ with
$Q_b\in\rho^3\mathrm{Diff}^1_{\mathrm b}$ and $R_b =
\widehat{\Box^\Upsilon_b}(0)-\widehat{\bar\Box^\Upsilon}(0)\in\rho^4\mathrm{Diff}^2_{\mathrm b}$ (also (2.2)); on
stationary sections $[\Box^\Upsilon_b-\bar\Box^\Upsilon,t_*] = Q_b$. So the first term of (3.5) is
$Q_b\bar\omega_{\mathrm s1}\in\rho^3C^\infty$, the second $R_b\breve{\bar\omega}^1_{\mathrm
s1}\in\rho^4\mathrm{Diff}^2_{\mathrm b}(\rho^{-1}C^\infty)\subset\rho^3C^\infty$, and the third, by Lemma 2.1, in
$\rho\,\mathrm{Diff}^1_{\mathrm b}\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}\subset\mathcal
A^{(3,0)\cup(3+\mathcal E_{\mathrm{ind}})}$. So $\breve f_b\in\mathcal A^{2+((1,0)\cup(1+\mathcal E_{\mathrm{ind}}))}$,
smooth on $\bar X$, and by (F1) with $k = 1$, $\breve\omega'_b := -P_b^{-1}\breve f_b\in\mathcal A^{(1,0)\cup(1+\mathcal
E_{\mathrm{ind}})}$. Put $\breve\omega_{b,\mathrm s1} := \breve{\bar\omega}^1_{\mathrm s1}+\breve\omega'_b$; then
$\Box^\Upsilon_b(t_*\omega_{b,\mathrm s1}+\breve\omega_{b,\mathrm s1}) = \breve f_b+P_b\breve\omega'_b = 0$. No
logarithm arises, since 1 is not an indicial root; this is (1). Smoothness in $b$: $\breve f_b$ is smooth in $b$ (Lemma
2.2 for $\omega'_b$), and Lemma 2.2 again.

For (2): $[\delta^*_g,t_*] = dt_*\otimes_s(\cdot)$ for every metric, and $\bar\delta^*\bar B = 0$ gives
$dt_*\otimes_s\bar\omega_{\mathrm s1}+\widehat{\bar\delta^*}(0)\breve{\bar\omega}^1_{\mathrm s1} = 0$. So

$$\breve h^1_{b,\mathrm s1}
= dt_*\otimes_s\omega'_b+\big(\widehat{\delta^*_{g_b}}(0)-\widehat{\bar\delta^*}(0)\big)\breve{\bar\omega}^1_{
\mathrm s1}+\widehat{\delta^*_{g_b}}(0)\breve\omega'_b\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}+\rho^3
\mathrm{Diff}^0_{\mathrm b}(\rho^{-1}C^\infty)+\rho\,\mathrm{Diff}^1_{\mathrm b}\mathcal A^{(1,0)\cup(1+\mathcal E_{
\mathrm{ind}})},$$

which lies in $\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$. *Its leading term.* At $b_S := (\mu,0)$ the metric
$g_\mu$, $t_*$ and $E_\Upsilon$ are invariant under the rotations of $x$ (section 1); the construction is linear and, by
the uniqueness of the inverse images, equivariant, so $S\mapsto\breve h^1_{b_S,\mathrm s1}(S)$ is an
$\mathrm{SO}(4)$-equivariant linear map from $\mathcal S_1$, the representation $\mathbb R^4$. The decomposition of
III.A$'$ Lemma 1.6 is into $\mathrm{SO}(4)$-invariant subspaces, and among the types only scalar type 1 contains
$\mathbb R^4$ (at each $l$ the scalar, vector and tensor types are, for $\mathrm{SO}(4)$, the representations of highest
weights $(\frac l2,\frac l2)$, $(\frac{l\pm1}2,\frac{l\mp1}2)$ and $(\frac{l\pm2}2,\frac{l\mp2}2)$, and $\mathbb R^4$ is
$(\frac12,\frac12)$); so $\breve h^1_{b_S,\mathrm s1}(S)$ is of scalar type 1, given by $S$. For general $b$, by (2.2),
$f_b-f_{b_S} = (P_b-P_{b_S})\bar\omega_{\mathrm s1}\in\rho^5C^\infty$, so
$\omega'_b-\omega'_{b_S} = -P_b^{-1}\big((f_b-f_{b_S})+(P_b-P_{b_S})\omega'_{b_S}\big)$, whose argument lies in
$\rho^{2+3}C^\infty+\mathcal A^{2+(5,0)\cup(5+\mathcal E_{\mathrm{ind}})}$, lies in $\bar H^{\infty,\alpha}_{\mathrm b}$
for some $\alpha>2$ (III.D$'$ Lemma 5.1, any $\alpha\in(2,\lambda^\Upsilon_{\mathrm s1,2})$). Then, term by term in
(3.5), $\breve f_b-\breve f_{b_S}\in\rho^4C^\infty+\bar H^{\infty,\alpha+1}_{\mathrm b}+\mathcal A^{(6,0)\cup(6+\mathcal
E_{\mathrm{ind}})}$ by Lemma 2.1 (the commutator bound and $R_b-R_{b_S}\in\rho^5\mathrm{Diff}^2_{\mathrm b}$), and
$\breve\omega'_b-\breve\omega'_{b_S} = -P_b^{-1}\big((\breve f_b-\breve f_{b_S})+(P_b-P_{b_S})\breve\omega'_{b_S}\big)$
lies in $\bar H^{\infty,\alpha''}_{\mathrm b}$ for every $\alpha''<2$ (III.D$'$ Lemma 5.1), so that
$\widehat{\delta^*_{g_b}}(0)$ of it is $O(\rho^{\alpha''+1})$, $\alpha''\in(1,2)$ (D229, the ninety-fourth verifier's
m2). So, in the formula for $\breve h^1$, the differences $dt_*\otimes_s(\omega'_b-\omega'_{b_S})$,
$(\widehat{\delta^*_{g_b}}(0)-\widehat{\delta^*_{g_\mu}}(0))\breve{\bar\omega}^1_{\mathrm s1}\in\rho^3C^\infty$,
$\widehat{\delta^*_{g_b}}(0)(\breve\omega'_b-\breve\omega'_{b_S})$ and
$(\widehat{\delta^*_{g_b}}(0)-\widehat{\delta^*_{g_\mu}}(0))\breve\omega'_{b_S}\in\rho^5C^\infty$ are all
$O(\rho^{2+\epsilon})$ for some $\epsilon>0$, and $\breve h^1_b$ and $\breve h^1_{b_S}$ have the same $\rho^2$ term.

*Rotations.* $g_\mu(R_V,\cdot) = V$, since $g_\mu = \eta+\mu|x|^{-2}(dt-d|x|)^2$ (III.B (3.4)) and $R_V(t) = R_V(|x|) =
0$; and $R_V$ is Killing for the spherically symmetric $g_\mu$, so $\delta^*_{g_\mu}V = 0$ (computed: `zstates5.py` Z4).
By (2.1), $\delta^*_{g_b}V =
(\widehat{\delta^*_{g_b}}(0)-\widehat{\delta^*_{g_\mu}}(0))V\in\rho^4\mathrm{Diff}^0_{\mathrm
b}(\rho^{-1}C^\infty)\subset\rho^3C^\infty$ near $\partial X$, smooth on $\bar X$, so $f_b :=
\Box^\Upsilon_bV\in\mathcal A^{2+(2,0)}$, and (F1) gives $\omega'_b := -P_b^{-1}f_b\in\mathcal A^{(2,0)\cup(2+\mathcal
E_{\mathrm{ind}})}$, smooth in $b$ by Lemma 2.2. $\omega_{b,\mathrm v1}(V) := V+\omega'_b$ solves (3.3), and
$h_{b,\mathrm v1}(V) = \delta^*_{g_b}V+\widehat{\delta^*_{g_b}}(0)\omega'_b\in\rho^3C^\infty+\mathcal
A^{(3,0)\cup(3+\mathcal E_{\mathrm{ind}})}$.

The kernel statements in (2) are (F2).

(3) If $R_V$ is Killing for $g_b$, $K := g_b(R_V,\cdot)$ has $\Box^\Upsilon_bK = 0$ (F2), and $K-V = (g_b-\bar
g)(R_V,\cdot)\in\rho^2C^\infty\cdot\rho^{-1}\subset\rho C^\infty$ by (2.3). So $\omega_{b,\mathrm v1}(V)-K\in\mathcal
A^{(1,0)\cup(1+\mathcal E_{\mathrm{ind}})}$ is in the kernel of $P_b$ on $\bar H^{s,\alpha}_{\mathrm b}$ for
$\alpha\in(0,1)$, which is trivial (III.D$'$ Lemma 5.1 (1)); so $\omega_{b,\mathrm v1}(V) = K$ and $h_{b,\mathrm v1}(V)
= \delta^*K = 0$. At $b = (\mu,0)$, $K = V$ for every $V$ by the above, and $\mathcal V_1\cong\mathfrak{so}(4)$ has
dimension 6 (computed: `zstates5.py` Z4, rank 6). $\square$

*Remarks.* (a) *The decay rates* (the source's Remark 6.16). $h_{b,\mathrm s1}$ gains three powers over
$\omega_{b,\mathrm s1}$, not one, because $g_b$ is translation-invariant to two orders ($g_b-\bar g\in\rho^2C^\infty$);
$h_{b,\mathrm v1}$ gains four powers over $\omega_{b,\mathrm v1}$ because $g_b$ is spherically symmetric to three orders
($g_b-g_\mu\in\rho^3C^\infty$). (b) Which $R_V$ are Killing for $g_b$ depends on the rotation $A$; at $A = 0$ all are,
and (3) is used there.

## 4. Findings, labels and sources

### 4.1 Findings

(D$''$1) *One power everywhere.* At $n = 4$ each comparison of [Hin26] Lemma 6.14 gains one power of $\rho$
((2.1)-(2.2)), because Myers-Perry meets Minkowski at $\mu|x|^{-2}$ and Tangherlini at $|x|^{-3}$; the source's proof of
the lemma, "directly from (3.21) and its consequence (6.8)", becomes the count of section 2 from III.B (3.5).

(D$''$2) *The exponents.* The corrections to the translations and the rotations lie at $\rho^2$ (source: $\rho^1$), the
correction to the boost at $\rho^1$ (source: $\rho^0$, with the logarithm (6.31)). 1 is no indicial root, so the boost
needs neither the source's Lemma 2.15 nor its logarithm, and $c_{b,\mathrm s1} = 0$. 2 is an s1 indicial root when
$e_\Upsilon\gamma_\Upsilon^2 = 0$ (`zstates5.py` Z2), so the translations and rotations need the modification at
infinity with $z>0$; the source's p. 81 introduces $e_\Upsilon$ to remove such coincidences.

(D$''$3) *The symmetric gradients* gain one power: $h_{b,\mathrm s1},h_{b,\mathrm v1}\in\mathcal A^{(3,0)\cup(3+\mathcal
E_{\mathrm{ind}})}$, $\breve h^1_{b,\mathrm s1}\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$. In the source,
(6.32c) states $h_{b,\mathrm v1}(V)\in\mathcal A^{(2,0)\cup(1+\mathcal E_{\mathrm{ind}})}$, while its proof gives
$\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$, which implies it; the proof's "$\rho^3\mathrm{Diff}^1_{\mathrm
b}$" for $\widehat{\delta^*_{g_b}}(0)-\widehat{\delta^*_{g_{b_S}}}(0)$ is $\rho^3\mathrm{Diff}^0_{\mathrm b}$ in its own
Lemma 6.14. Neither changes a statement.

(D$''$4) *Killing rotations.* The source's condition that $V$ and $V(a)$ be linearly dependent becomes that $R_V$ be a
Killing field of $g_b$; the identification $\omega_{b,\mathrm v1}(V) = g_b(R_V,\cdot)$ then follows from the triviality
of the zero energy kernel (III.D$'$), and at $A = 0$ holds for all six rotations.

(D$''$5) *The leading term of $\breve h^1$* is identified by representation theory at $b = (\mu,0)$ and by one more
power of decay in general, which makes precise the source's "follows for general $b$ again by the sub-sub-leading nature
of the departure from spherical symmetry". The record's supplement 10.28 (a) said the proof runs "with every order
raised by one"; that is right except for the boost, which gains one order and loses its logarithm.

### 4.2 Labels

Proved here, assuming (Dyn) (Part VI): Lemmas 2.1, 2.2 and Proposition 3.1. Computed (exact; rerun D223): `zstates5.py`
Z1-Z5, `genstates5.py` H5. Standard facts used: the Lie derivative identity $D\mathrm{Ric}(\mathcal L_Xg) = \mathcal
L_X\mathrm{Ric}(g)$, and the highest weights of the $\mathrm{SO}(4)$-representations on spherical harmonics of each
type.

### 4.3 Sources

READ: [Hin26] pp. 125-128 (section 6.5 to the end of the proof of Proposition 6.15: Lemma 6.13 and its proof, Lemma
6.14, Proposition 6.15 with (6.29)-(6.35), footnotes 72-73, Remarks 6.16-6.17), arXiv:2606.28253v2, full text. The
record's supplement 10.28 (N1STAR-PROOF.md) for the computed statements.
