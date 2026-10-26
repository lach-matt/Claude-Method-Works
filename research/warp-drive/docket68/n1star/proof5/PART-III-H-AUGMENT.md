# Part III.H. The augmented low-energy resolvent at n = 4 ([Hin26] section 10.1)

*Status.* Verified (D249: the hundred-and-fourth verifier; no major finding, two minor findings and six nits seated,
to be read). Written (D248). This part proves, at spatial dimension $n = 4$, [Hin26] section 10.1 (pp. 200-212): the
augmentation of $\widehat{L_b}(\sigma)$ by the zero energy states cut off near $I^+$, the Fourier transforms of the
resulting source terms (the source's Lemma 10.4 and (10.24)), the invertibility of the augmented zero energy operator
(Proposition 10.6), the uniform low-energy estimates (Proposition 10.7) and the augmentation built on the spectral side
(section 10.1.3). It also proves what III.F$''$ section 5 left open: $\widehat{L_b}(\sigma)$ is invertible for
$0<|\sigma|<c_0$ and $b\ne b_0$ near $b_0$, so that the source's Proposition 8.8 holds at $n = 4$ on a fixed
neighbourhood of $b_0$ (Corollaries 4.3-4.4).

*What n = 4 changes.* At $n = 3$ the mass and boost states decay like $r^{-1}$, the naive columns
$[L_b,t_*]\dot g^\Upsilon_b$ only like $r^{-2}$, which is not in the target space, and the source must first improve its
states at $\iota^+$ (its Lemma 10.3, by its Proposition 9.11). At $n = 4$ the states decay one order faster (III.F$'''$
Proposition 4.1), the columns are $O(r^{-3})$ and lie in the target for every weight $\alpha$ with $\alpha+2\in(0,1)$,
and the states cut off near $I^+$ need no correction: the source's Lemma 10.3 is not needed, no logarithm enters, the
cut-off source terms are supported in a cone inside $\iota^+$ (Lemma 2.2), and the window $(0,\epsilon_{\mathrm{ind}})$
of the source's weights becomes $(0,1)$. The source's Proposition 10.7 rests on [Hin26c] Theorem 9.41 with augmentation
columns that depend on $\sigma$; Part I.C's Theorem 6.4 allows only constant, compactly supported columns, and Theorem
4.1 below extends it ((H1)). The source's Lemma 10.5 (partial polyhomogeneity), used only in its section 11.5, is left
to the part that writes that section. Notation is that of Parts I.C, II.G$'$, III.F$'''$ and III.F$''''$; no
instrument is used, every step being by hand.

## 1. Setting

*Parameters.* Those of III.F$'''$ section 1 and III.F$''''$ section 1: $b = (\mu,A)$ near $b_0$, the modification
parameters with (Dyn), (C1) and $\gamma_\Upsilon$ small, and $s>\frac12+\vartheta_L$ constant; the pairing
$\langle u,v\rangle := \int_X\langle u,v\rangle_{g_b}|dx|$. $r := |x|$ on $X$ (so $r\ge r_0>0$), and $\rho$ is the
boundary defining function of I.C section 6 ($\rho = 1/r$); II.G$'$ section 4.3 uses $\langle x\rangle^{-1}$, which
on $\{r\ge1\}$ differs from $1/r$ by a smooth factor in $[2^{-1/2},1]$.

*Weights.* All weights below are Part I.C's, defined with the density $|dx|$ (the source's $|dg_b|_X|$):
$\bar H^{m,a}_{\mathrm b}$ is I.C's, and the b-weights of III.F$'''$ (density $\mu_{\mathrm b} = |dx|/|x|^4$) are these
plus 2. Thus $\mathcal A^q\subset\bar H^{\infty,a}_{\mathrm b}$ near $\partial X$ for $a<q-2$. $\partial X$ is the
boundary at infinity ($\rho = 0$) of $\bar X$, and "smooth on $X$" below says nothing there, where only conormality is
claimed. Throughout,
$$\alpha\in\mathbb R,\qquad\alpha+2\in(0,1),\tag{1.1}$$
the source's $\alpha_{\mathrm{sf}}$ (at $n = 3$, $\alpha_{\mathrm{sf}}+\frac32\in(0,\epsilon_{\mathrm{ind}})$). Then
III.F$'''$ Proposition 4.1 applies at its b-weight $\alpha+2\in(0,1]$, $\widehat{L_b}$ satisfies (G) of I.C at the
weight $\alpha$ ($\alpha+2$ lies in the gap $(0,\beta^L_+)$, $\beta^L_+>1$, III.F$'$ Proposition 2.3) and (TF) with the
weight $\alpha+2$ (III.F$'$ Proposition 3.3), and (H1)-(H5) of I.A with index 0 at $\sigma\ne0$ (III.F$''$ Corollary
1.2). $\mathcal X_\sigma$, $\mathcal Y_\sigma$ ($\sigma\ne0$), $\mathcal X_0$, $\mathcal Y_0$, the norms
$\|\cdot\|_{(s;k),(\mathsf r,l,q),\varsigma}$ ($\varsigma = |\sigma|$), the orders $\mathsf r$ and $\alpha_+$ and the
cut-offs $\chi_{\mathrm{zf}},\chi_{\mathrm{tf}}$ are those of I.C section 6, for $\widehat P = \widehat{L_b}$ at the
weight $\alpha$. $\Sigma_0 := \{\sigma\in\mathbb C:0<|\sigma|\le1,\ \mathrm{Im}\,\sigma\ge0\}$.

*The operator.* By III.F$''''$ section 2, $L_b = L_0+L_1\partial_{t_*}+L_2\partial_{t_*}^2$ with stationary operators
$L_j$ on $X$: $L_0 = \widehat{L_b}(0)$, $L_1 = [L_b,t_*]$ and $L_2 = \frac12[[L_b,t_*],t_*]$ on stationary sections, and
$\widehat{L_b}(\sigma) = L_0-i\sigma L_1-\sigma^2L_2$ (III.A (2.2): $\partial_{t_*}$ becomes $-i\sigma$). Near
$\partial X$, $L_0\in\rho^2\mathrm{Diff}^2_{\mathrm b}$, $L_1\in\rho\,\mathrm{Diff}^1_{\mathrm b}$ and
$L_2\in\rho^2C^\infty$ (III.G$''''$ (1.2) and the proof of its Lemma 1.2, from III.F Lemma 2.1; I.C (1.1)); on compact
subsets of $X$ they have smooth coefficients.

*The states.* For $\dot b = (\dot\mu,\dot A)\in\mathfrak b := \mathbb R\oplus\mathfrak{so}(4)$ let
$\dot g(\dot b) := \dot\mu\,\dot g^\Upsilon_b(1,0)+\dot g^\Upsilon_b(0,\dot A)$, and for $S\in\mathcal S_1$ let
$h(S) := h_{b,\mathrm s1}(S)$ and $\breve h(S) := \breve h^1_{b,\mathrm s1}(S)$ (III.F$'''$ (4.2); III.D$''$ Proposition
3.1, the source's Proposition 6.15). They are smooth on $X$, conormal at $\partial X$, with weights (largest $q$
with the state in $\mathcal A^q$) $\dot g(1,0)$ 2, $\dot g(0,\dot A)$ 3, $h(S)$ 3, $\breve h(S)$ 2 (III.F$''''$ section
1). The generalised state is $h^{\le1}(S) := t_*h(S)+\breve h(S) = \delta^*_{g_b}(t_*\omega^{(0)}_{b,\mathrm
s1}(S)+\breve\omega^{(0),1}_{b,\mathrm s1}(S))$ (III.D$''$ Proposition 3.1), where the 1-form lies in the kernel of
$\Box^\Upsilon_b$; as $D_{g_b}\mathrm{Ric}\circ\delta^*_{g_b} = 0$ and $2\delta_{g_b,E_\Upsilon}G_{g_b}\delta^*_{g_b} =
\Box^\Upsilon_b$ (III.F$'''$ Proposition 4.1, proof), $L_bh^{\le1}(S) = 0$, that is, $L_0h(S) = 0$ and
$L_1h(S)+L_0\breve h(S) = 0$ (as III.F$''''$ Lemma 3.1 (3) uses). And $L_b\dot g(\dot b) = L_0\dot g(\dot b) = 0$.

*Cut-offs.* Fix $\chi_c\in C^\infty(\mathbb R)$ (named apart from I.C's $\chi_0$) equal to 1 on $(-\infty,\frac14]$ and
to 0 on $[\frac12,\infty)$, and $\chi_+\in C^\infty(\mathbb R)$ equal to 0 on $(-\infty,1]$ and to 1 on $[2,\infty)$,
and put
$$\chi_K(t_*,x) := \chi_+(t_*)\chi_c(|x|/t_*)\quad(t_*>0),\qquad\chi_K := 0\quad(t_*\le0).\tag{1.2}$$
$\chi_K$ is smooth on $\mathbb R\times X$, vanishes for $t_*\le1$ and for $|x|\ge t_*/2$ (so near $I^+$, where
$|x|/t_*\to\infty$), and equals 1 on $\{t_*\ge2,\ |x|\le t_*/4\}$ (so near $K^+$): it has the properties the source asks
of its $\chi_K$ (p. 203). For $|x|\ge1$, $\chi_K(t_*,x) = \chi_c(|x|/t_*)$ for all $t_*>0$, as both vanish for
$t_*\le2|x|$.

## 2. The cut-off states and their Fourier transforms ([Hin26] Lemma 10.4 and (10.24) at n = 4)

**Definition 2.1.** For $\dot b\in\mathfrak b$ and $S\in\mathcal S_1$,
$\dot g^{\mathrm{aug}}(\dot b) := \chi_K\dot g(\dot b)$ and $h^{\mathrm{aug}}(S) := \chi_Kh^{\le1}(S)$, and
$f_{\dot b} := L_b\dot g^{\mathrm{aug}}(\dot b)$, $f_S := L_bh^{\mathrm{aug}}(S)$.

These are the source's (10.10)-(10.11) and (10.24a) without its correction $u_b$; at $n = 4$ none is needed.

**Lemma 2.2 (the source terms).** Let $h$ be $\dot g(\dot b)$ or $h^{\le1}(S)$ and $f := L_b(\chi_Kh)$.

(a) $f = [L_b,\chi_K]h$; $f$ vanishes outside $\{1\le t_*\le2,\ |x|\le t_*/2\}\cup\{t_*\ge2,\ t_*/4\le|x|\le t_*/2\}$.

(b) Fix $\psi\in C^\infty_c([0,2))$ equal to 1 on $[0,1]$, and put $f_c := \psi(r)f$, $f_\infty := (1-\psi(r))f$. Then
$f_c$ is smooth on $\mathbb R\times X$ with support in $\{1\le t_*\le8,\ r\le2\}$, $f_\infty$ is supported in
$\{r\ge1,\ 2r\le t_*\le4r\}$, and for all $j,a\in\mathbb N_0$ and multi-indices $\beta$ on $\mathbb S^3$,
$$|(t_*\partial_{t_*})^j(r\partial_r)^a\partial_\omega^\beta f_\infty|\le C\,r^{-4}.\tag{2.1}$$

In the source's notation, $f\in\mathcal A^{\infty,4,\infty}(\Omega)$ (orders at $I^+$, $\iota^+$, $K^+$), against its
$\mathcal A^{3,3+\epsilon_{\mathrm{ind}}-\epsilon,4+\epsilon_{\mathrm{ind}}-\epsilon}$ at $n = 3$ ((10.12)).

*Proof.* (a) $L_bh = 0$ (section 1), so $f = L_b(\chi_Kh)-\chi_KL_bh = [L_b,\chi_K]h$, and
$$[L_b,\chi_K]h = [L_0,\chi_K]h+L_1\big((\partial_{t_*}\chi_K)h\big)+[L_1,\chi_K]\partial_{t_*}h
+L_2\big((\partial^2_{t_*}\chi_K)h+2(\partial_{t_*}\chi_K)\partial_{t_*}h\big),$$
$L_2$ being a multiplication. Every coefficient contains a derivative of $\chi_K$ of order $\ge1$. For $t_*\ge2$,
$\chi_K = \chi_c(|x|/t_*)$, whose derivatives vanish unless $|x|/t_*\in[\frac14,\frac12]$; for $t_*\in[1,2]$, $\chi_K$
vanishes unless $|x|\le t_*/2\le1$; for $t_*<1$ it vanishes. (b) On $\mathrm{supp}\,f\cap\{r\le2\}$,
$t_*\le\max(2,4r)\le8$. On $\mathrm{supp}\,f\cap\{r\ge1\}$, the first set of (a) meets $\{r\ge1\}$ only where $r = 1$,
$t_* = 2$, so $2r\le t_*\le4r$. There $\chi_K = \chi_c(r/t_*)$, homogeneous of degree 0 in $(t_*,x)$, so
$\partial^p_{t_*}\partial^q_x\chi_K$ is homogeneous of degree $-p-|q|$ and bounded by $Cr^{-p-|q|}$ on the cone
$\{2r\le t_*\le4r\}$, as are its derivatives along $t_*\partial_{t_*}$, $r\partial_r$, $\partial_\omega$, which preserve
homogeneity. On the cone the states satisfy, with these derivatives, $|\dot g|\le Cr^{-2}$, $\partial_{t_*}\dot g = 0$;
$|t_*h(S)|\le4r\cdot Cr^{-3}$, $t_*\partial_{t_*}(t_*h) = t_*h$, $|\partial_{t_*}(t_*h)| = |h|\le Cr^{-3}$;
$|\breve h|\le Cr^{-2}$, $\partial_{t_*}\breve h = 0$. With $L_0\in\rho^2\mathrm{Diff}^2_{\mathrm b}$,
$[L_0,\chi_K]$ is $\rho^2$ times a first-order b-operator in $x$ whose coefficients are bounded, with their b-derivatives
and $t_*\partial_{t_*}$-derivatives, on the cone; so $[L_0,\chi_K]h = O(r^{-2}\cdot r^{-2})$. Likewise
$L_1((\partial_{t_*}\chi_K)h) = O(r^{-1}\cdot r^{-1}r^{-2})$, $[L_1,\chi_K]\partial_{t_*}h = O(r^{-1}\cdot r^{-3})$
($[L_1,\chi_K]$ is $\rho$ times a bounded multiplication), and the $L_2$ terms are $O(r^{-2}(r^{-2}r^{-2}+
r^{-1}r^{-3}))$. The same bounds hold after applying $(t_*\partial_{t_*})^j(r\partial_r)^a\partial_\omega^\beta$, which
commute with the stationary b-operators up to b-operators of the same class. $\square$

**Lemma 2.3 (zero frequency; the source's Lemma 10.4 (1) and (10.24c)).** Let $\hat f(0) := \int f\,dt_*$, pointwise in
$x$ ($f(\cdot,x)$ has compact support). Then $\hat f(0)$ is smooth on $X$ and in $\mathcal A^3$ near $\partial X$,
and
$$\hat f_{\dot b}(0) = L_1\dot g(\dot b)+L_0w_{\dot b},\qquad\hat f_S(0) = L_2h(S)+L_1\breve h(S)+L_0w_S,\tag{2.2}$$
with $w_{\dot b} := -\kappa(r)\dot g(\dot b)$, $w_S := -\kappa'(r)h(S)-(\kappa(r)+\kappa_2)\breve h(S)$, where
$\kappa(r) := \int\chi_+(t)(1-\chi_c(r/t))\,dt$, $\kappa'(r) := \int\chi_+(t)(1-\chi_c(r/t))\,t\,dt$ and
$\kappa_2 := \int t\chi_+'(t)\,dt$. For $r\ge1$, $\kappa(r) = \kappa_0r-\kappa_1$ and $\kappa'(r) =
\kappa'_0r^2-\kappa'_1$, with $\kappa_0 = \int_0^4(1-\chi_c(1/s))\,ds$, $\kappa'_0 = \int_0^4s(1-\chi_c(1/s))\,ds$,
$\kappa_1 = \int_0^2(1-\chi_+)$, $\kappa'_1 = \int_0^2t(1-\chi_+(t))\,dt$. So $w_{\dot b}$, $w_S$ are smooth on $X$,
linear in $\dot b$, $S$, and in $\mathcal A^1$ near $\partial X$.

*Proof.* Write $\chi_K = \chi_++(\chi_K-\chi_+)$, $\chi_+ = \chi_+(t_*)$. For each $x$,
$(\chi_K-\chi_+)(\cdot,x) = \chi_+(t_*)(\chi_c(r/t_*)-1)$ is smooth with support in $[1,\max(2,4r)]$, locally uniformly
in $x$. So for $h' := (\chi_K-\chi_+)h$, differentiating under the integral,
$\int L_bh'\,dt_* = L_0\int h'\,dt_*+L_1\int\partial_{t_*}h'\,dt_*+L_2\int\partial^2_{t_*}h'\,dt_* = L_0\int h'\,dt_*$,
and $\int h'\,dt_* = -\kappa(r)\dot g$, resp. $-\kappa'(r)h-\kappa(r)\breve h$. Next, $L_b(\chi_+\dot g) = \chi_+'L_1\dot
g+\chi_+''L_2\dot g$ has compact support in $t_*$ and integrates to $L_1\dot g$. And, using $L_0h = 0$,
$$L_b\big(\chi_+(t_*h+\breve h)\big) = \chi_+(L_1h+L_0\breve h)+t_*\chi_+'L_1h+(t_*\chi_+)''L_2h+\chi_+'L_1\breve
h+\chi_+''L_2\breve h,$$
whose first term vanishes; the rest has compact support in $t_*$ and integrates to
$\kappa_2L_1h+L_2h+L_1\breve h$ ($\int(t_*\chi_+)'' = 1$, $\int\chi_+' = 1$, $\int\chi_+'' = 0$), and
$\kappa_2L_1h = L_0(-\kappa_2\breve h)$. As $f = L_b(\chi_+h)+L_bh'$, (2.2) follows. For $r\ge1$, $1-\chi_c(r/t) = 1$ for
$t\le2r$, in particular on $\mathrm{supp}(1-\chi_+)\subset(-\infty,2]$; so
$\kappa(r) = \int_0^\infty(1-\chi_c(r/t))\,dt-\int_0^2(1-\chi_+)\,dt = \kappa_0r-\kappa_1$ (substituting $t = rs$;
$1-\chi_c(1/s)$ vanishes for $s\ge4$), and likewise $\kappa'(r)$. Then $w\in\mathcal A^1$ ($r\mathcal A^2$, $r^2\mathcal
A^3$), and $\hat f(0)\in\mathcal A^3$ by (2.2): $L_1\mathcal A^2\subset\mathcal A^3$, $L_0\mathcal A^1\subset\mathcal
A^3$, $L_2\mathcal A^3\subset\mathcal A^5$. $\square$

**Lemma 2.4 (Fourier transforms of the source terms; the source's Lemma 10.4 (2)-(4)).** For $\mathrm{Im}\,\sigma\ge0$
let $\hat f(\sigma,x) := \int e^{i\sigma t_*}f(t_*,x)\,dt_*$.

(a) (*Structure.*) $\hat f = \hat f_c+\hat f_\infty$, with $\hat f_c$ entire in $\sigma$ with values in the smooth
sections supported in $\{r\le2\}$, and, on $\{r\ge1\}$,
$$\hat f_\infty(\sigma,x) = r^{-3}G(\sigma r,x),\qquad G(\zeta,x) := \int_2^4e^{i\zeta s}F(s,x)\,ds,\quad F(s,x) :=
r^4f_\infty(sr,x),\tag{2.3}$$
where for $\mathrm{Im}\,\zeta\ge0$ and all $j,a,\beta,N$,
$|(\zeta\partial_\zeta)^j(r\partial_r)^a\partial_\omega^\beta G(\zeta,x)|\le C\langle\zeta\rangle^{-N}$; $G$ is entire
in $\zeta$.

(b) (*Uniform bounds.*) For $k,j\in\mathbb N_0$, $N\in\mathbb R$ and $\beta_{\mathrm{tf}}<3$,
$\sup_{\sigma\in\Sigma_0}\|(\sigma\partial_\sigma)^j\hat f(\sigma)\|_{H^{k,(N,\beta_{\mathrm{tf}},0)}_{\mathrm
b,|\sigma|}}<\infty$ (II.G$'$ section 4.3's norm, with $\mu_{\mathrm b}$). Hence, by II.G$'$ (4.5a), for every order
pair $(s',\mathsf r')$ as in II.G$'$ Lemma 4.6 and every $l<-1$, with $\varsigma_1$ that of II.G$'$ (4.5a),
$$\sup_{\sigma\in\Sigma_0,\,|\sigma|\le\varsigma_1}\|(\sigma\partial_\sigma)^j\hat f(\sigma)\|_{(s'-1;k),(\mathsf
r'+1,l+2,0),|\sigma|}<\infty.
\tag{2.4}$$

(c) (*Regularity at zero frequency.*) Let $\phi\in C^\infty([0,\infty))$ vanish on $[0,2]$ and be bounded with its
derivatives. For $a\in(0,1)$ and $m\in\mathbb N_0$ there is $C$ with
$$\|\phi(\rho/|\sigma|)(\hat f(\sigma)-\hat f(0))\|_{\bar H^{m,a}_{\mathrm b}}\le C|\sigma|^{1-a},\qquad\sigma\in
\Sigma_0.\tag{2.5}$$

(d) (*Continuity, holomorphy.*) $\sigma\mapsto\hat f(\sigma)$ is continuous on
$\{\mathrm{Im}\,\sigma\ge0,\ |\sigma|\le1\}$ with values in $\bar H^{m,a}_{\mathrm b}$ for every $m$ and $a<1$, and
smooth on $\{\mathrm{Im}\,\sigma\ge0\}\setminus0$ and holomorphic on $\{\mathrm{Im}\,\sigma>0\}$ with values in $\bar
H^{m,M}_{\mathrm b}$ for every $m$ and $M$.

*Proof.* (a) $\hat f_c$: $f_c$ is smooth with compact support. For $r\ge1$, by Lemma 2.2 (b) and $t_* = sr$,
$\hat f_\infty(\sigma,x) = r\int_2^4e^{i\sigma rs}f_\infty(sr,x)\,ds = r^{-3}G(\sigma r,x)$. $F$ is smooth, supported in
$s\in[2,4]$ (so it vanishes with all $s$-derivatives at $s = 2,4$), and bounded with all derivatives along $s\partial_s$,
$r\partial_r$ (at fixed $s$) and $\partial_\omega$: $s\partial_sF = r^4(t_*\partial_{t_*}f_\infty)(sr,x)$ and
$r\partial_rF = r^4((4+t_*\partial_{t_*}+r\partial_r)f_\infty)(sr,x)$, bounded by (2.1). For $\mathrm{Im}\,\zeta\ge0$
and $s>0$, $|e^{i\zeta s}|\le1$; integrating by parts $N$ times with $e^{i\zeta s} = (i\zeta)^{-1}\partial_se^{i\zeta
s}$ gives the decay, and $\zeta\partial_\zeta e^{i\zeta s} = s\partial_se^{i\zeta s}$ gives
$(\zeta\partial_\zeta)^jG = \int e^{i\zeta s}(-\partial_ss)^jF\,ds$, of the same kind. Derivatives in $x$ pass under the
integral.

(b) II.G$'$ section 4.3: with $\varsigma := |\sigma|$ and $\hat\rho := \langle x\rangle^{-1}/\varsigma$,
$\rho_{\mathrm{scf}} = \hat\rho/(1+\hat\rho)$, $\rho_{\mathrm{tf}} = \varsigma(1+\hat\rho)$,
$\rho_{\mathrm{zf}} = (1+\hat\rho)^{-1}$, and $\|u\|_{H^{k,\beta}_{\mathrm b,\varsigma}} =
\|w_\beta(\varsigma)^{-1}u\|_{\bar H^k_{\mathrm b}(\bar X,\mu_{\mathrm b})}$,
$w_\beta = \rho_{\mathrm{scf}}^{\beta_{\mathrm{scf}}}\rho_{\mathrm{tf}}^{\beta_{\mathrm{tf}}}\rho_{\mathrm{zf}}^{\beta_{
\mathrm{zf}}}$. Since $\sigma\partial_\sigma$ acts on (2.3) as $\zeta\partial_\zeta$ on $G$, it suffices to take $j = 0$
with $G$ replaced by $(\zeta\partial_\zeta)^jG$. On $\{r\ge1\}$, $|\zeta| = \varsigma r$ is comparable to
$\hat\rho^{-1}$, and $r^{-3}$ to $\langle x\rangle^{-3} = (\rho_{\mathrm{scf}}\rho_{\mathrm{tf}})^3$; so, for every $M$,
$|w_\beta^{-1}\hat f_\infty|\le C\rho_{\mathrm{scf}}^{3-N}\rho_{\mathrm{tf}}^{3-\beta_{\mathrm{tf}}}
\langle\hat\rho^{-1}\rangle^{-M}$. Where $\hat\rho\ge1$: $\rho_{\mathrm{scf}}\in[\frac12,1]$,
$\rho_{\mathrm{tf}}\in[\langle x\rangle^{-1},2\langle x\rangle^{-1}]$, and the bound is $C\langle
x\rangle^{-(3-\beta_{\mathrm{tf}})}$, square integrable for $\mu_{\mathrm b}$ on $\{\langle x\rangle\ge1\}$ uniformly in
$\varsigma$ as $\beta_{\mathrm{tf}}<3$. Where $\hat\rho\le1$: $\rho_{\mathrm{scf}}\in[\hat\rho/2,\hat\rho]$,
$\rho_{\mathrm{tf}}\in[\varsigma,2\varsigma]$, and the bound is $C\hat\rho^{3-N+M}$, square integrable for
$\mu_{\mathrm b} = |d\hat\rho/\hat\rho|\,d\omega$ for $M>N-3$. The b-derivatives along $r\partial_r$ and
$\partial_\omega$ fall on $r^{-3}$, on $\zeta = \sigma r$ (giving $\zeta\partial_\zeta G$) and on the $x$-dependence of
$G$, with the same bounds, and $w_\beta$ has bounded logarithmic b-derivatives (II.G$'$ section 4.3). $\hat f_c$ is
bounded in $C^\infty$, uniformly for $|\sigma|\le1$, with support in $\{r\le2\}$, where $\hat\rho\ge c/\varsigma\ge c$,
so $w_\beta^{-1}$ is bounded there. Then (2.4) is II.G$'$ (4.5a) with $l+4 = \beta_{\mathrm{tf}}$ and
$N = \mathsf r'_{\mathrm{out}}+3+\epsilon$.

(c) On $\mathrm{supp}\,\phi(\rho/\varsigma)\subset\{\rho\ge2\varsigma\}$, $|\sigma r|\le\frac12$, and by (a) and
Taylor's formula $|(r\partial_r)^a\partial_\omega^\beta(G(\sigma r,x)-G(0,x))|\le C|\sigma|r$ there; the b-derivatives
of $\phi(\rho/\varsigma)$ are bounded uniformly in $\varsigma$. So $|\hat f_\infty(\sigma)-\hat
f_\infty(0)|\le C\varsigma\rho^2$ there, with b-derivatives, and as $\bar H^{m,a}_{\mathrm b} = \rho^{a+2}\bar
H^m_{\mathrm b}(\mu_{\mathrm b})$, the $\{r\ge1\}$ part of the left side of (2.5) is at most
$C\|\varsigma\rho^{-a}\|_{L^2(\{2\varsigma\le\rho\le1\},\mu_{\mathrm b})} =
C\varsigma(\int_{2\varsigma}^1\rho^{-2a-1}d\rho)^{1/2}\le C\varsigma^{1-a}$, as $a>0$. And
$\hat f_c(\sigma)-\hat f_c(0) = O(|\sigma|)$ in $C^\infty$ with support in $\{r\le2\}$.

(d) $\hat f_c$ is entire. For $\sigma\ne0$, by (a), $\hat f_\infty(\sigma)$ and
$\partial^j_\sigma\hat f_\infty(\sigma) = r^{j-3}(\partial^j_\zeta G)(\sigma r,x)$ are $O(r^{j-3}(|\sigma|r)^{-N})$ for
every $N$, locally uniformly in $\sigma$, with their b-derivatives; this gives smoothness (and, $G$ being entire,
holomorphy in $\{\mathrm{Im}\,\sigma>0\}$) in every $\bar H^{m,M}_{\mathrm b}$. At $\sigma = 0$: on
$\{\rho\ge2\varsigma\}$ the difference is bounded as in (c); on $\{\rho\le2\varsigma\}$, $|\hat f(\sigma)|$,
$|\hat f(0)|\le C\rho^3$, whose $\bar H^{m,a}_{\mathrm b}$-norm there is $O(\varsigma^{1-a})$. $\square$

**Lemma 2.5 (the cut-off states on the spectral side).** For $\mathrm{Im}\,\sigma\ge0$, $\sigma\ne0$, let
$\Psi(\sigma,x) := \int e^{i\sigma t_*}\partial_{t_*}\chi_K(t_*,x)\,dt_*$ and
$$\hat g^{\mathrm{aug}}(\sigma)(\dot b) := i\sigma^{-1}\Psi(\sigma,\cdot)\dot g(\dot b),\qquad\hat
h^{\mathrm{aug}}(\sigma)(S) := \partial_\sigma\big(\sigma^{-1}\Psi(\sigma,\cdot)\big)h(S)+i\sigma^{-1}\Psi(\sigma,\cdot)
\breve h(S).\tag{2.6}$$

(a) For $\mathrm{Im}\,\sigma>0$ these are the absolutely convergent Fourier transforms of $\dot g^{\mathrm{aug}}(\dot b)$
and $h^{\mathrm{aug}}(S)$.

(b) For $r\ge1$, $\Psi(\sigma,x) = \Phi(\sigma r)$ with $\Phi(\zeta) := \int_2^4e^{i\zeta s}\partial_s[\chi_c(1/s)]\,ds$,
an entire function with $\Phi(0) = 1$ and $|\partial^j_\zeta\Phi(\zeta)|\le C_{j,N}\langle\zeta\rangle^{-N}$ on
$\{\mathrm{Im}\,\zeta\ge0\}$. Hence (2.6) is smooth on $X$ and lies in $\bar H^{m,M}_{\mathrm b}$ for every $m$ and
$M$, smoothly in $\sigma\in\{\mathrm{Im}\,\sigma\ge0\}\setminus0$, holomorphically in the interior; in particular it lies
in $\mathcal X_\sigma$.

(c) $\widehat{L_b}(\sigma)\hat g^{\mathrm{aug}}(\sigma)(\dot b) = \hat f_{\dot b}(\sigma)$ and
$\widehat{L_b}(\sigma)\hat h^{\mathrm{aug}}(\sigma)(S) = \hat f_S(\sigma)$.

(d) For $R\ge1$ there is $C$ with $|\Psi(\sigma,x)-1|\le C|\sigma|$ and $|\partial_\sigma\Psi(\sigma,x)|\le C$ for
$r\le R$, $\sigma\in\Sigma_0$.

*Proof.* (a) For $\mathrm{Im}\,\sigma>0$, $\int e^{i\sigma t_*}\chi_K\,dt_*$ converges absolutely ($\chi_K$ is bounded
and vanishes for $t_*\le1$), and integrating by parts, the boundary term at $\infty$ vanishing,
$\int e^{i\sigma t_*}\chi_K\,dt_* = -(i\sigma)^{-1}\int e^{i\sigma t_*}\partial_{t_*}\chi_K\,dt_* = i\sigma^{-1}\Psi$;
and $\int e^{i\sigma t_*}t_*\chi_K\,dt_* = -i\partial_\sigma(i\sigma^{-1}\Psi) = \partial_\sigma(\sigma^{-1}\Psi)$. The
states are stationary. (b) For $r\ge1$, $\chi_K(t_*,x) = \chi_c(r/t_*)$ for $t_*>0$ (section 1), so
$\partial_{t_*}\chi_K$ is supported in $2r\le t_*\le4r$ and, with $t_* = rs$,
$\Psi = \int e^{i\sigma rs}\partial_s[\chi_c(1/s)]\,ds = \Phi(\sigma r)$; $\partial_s[\chi_c(1/s)]$ is smooth with
support in $[2,4]$ and integral $\chi_c(\frac14)-\chi_c(\frac12) = 1$, and the bounds follow by integration by parts as
in Lemma 2.4 (a). So for $\sigma\ne0$, $\Psi$, $\partial_\sigma\Psi = r\Phi'(\sigma r)$ and their $\sigma$- and
b-derivatives are $O(r^p(|\sigma|r)^{-N})$ for every $N$, locally uniformly in $\sigma$; with the states' conormal
bounds this gives the memberships. For $r\le1$, $\partial_{t_*}\chi_K(\cdot,x)$ is supported in $[1,4]$, and $\Psi$ is
entire in $\sigma$ and smooth in $x$. A section in $\bar H^{m,M}_{\mathrm b}$ for all $m$, $M$ lies in $\mathcal
X_\sigma$, $\widehat{L_b}(\sigma)$ mapping it into the same class. (c) For $\mathrm{Im}\,\sigma>0$, integrating by
parts in $t_*$ (no boundary terms: $\chi_Kh$ vanishes for $t_*\le1$ and grows at most linearly, $e^{i\sigma t_*}$
decays), $\mathcal F(L_bv)(\sigma) = \widehat{L_b}(\sigma)\mathcal F(v)(\sigma)$ for $v = \chi_Kh$; so (c) holds there by
(a). Both sides are continuous on $\{\mathrm{Im}\,\sigma\ge0\}\setminus0$ pointwise in $x$ (Lemma 2.4 (d) and (b)), so
(c) extends to real $\sigma\ne0$. (d) For $r\le R$, $\partial_{t_*}\chi_K(\cdot,x)$ is supported in $[1,\max(2,4R)]$
and integrates to 1; so $\Psi-1 = \int(e^{i\sigma t_*}-1)\partial_{t_*}\chi_K\,dt_*$ and
$\partial_\sigma\Psi = \int it_*e^{i\sigma t_*}\partial_{t_*}\chi_K\,dt_*$, with $|e^{i\sigma t_*}|\le1$. $\square$

So, as $\sigma\to0$, $\hat g^{\mathrm{aug}}(\sigma)\sim i\sigma^{-1}\dot g$ and $\hat h^{\mathrm{aug}}(\sigma)\sim
-\sigma^{-2}h+i\sigma^{-1}\breve h$ on compact sets: the source's naive columns (10.5), whose spacetime counterparts are
$H(t_*)\dot g$ and $H(t_*)(t_*h+\breve h)$.

**Remark 2.6 (uniformity in $b$).** Lemmas 2.2-2.4 are stated at fixed $b$; near $b_0$ their bounds hold uniformly with
a loss $\delta>0$. The states depend continuously on $b$ with values in $\bar H^{m,a}_{\mathrm b}$ for every $m$ and
every $a$ below their weights minus 2 (III.F$'''$ Proposition 2.2 (3) and Proposition 4.1, Step 5, at every
regularity; III.D$''$ Proposition 3.1), and $\bar H^{\infty,a}_{\mathrm b}\subset\mathcal A^{a+2}$ (b-Sobolev
embedding, as $\bar H^{m,a}_{\mathrm b} = \rho^{a+2}\bar H^m_{\mathrm b}(\mu_{\mathrm b})$). So for every $\delta>0$
the states are bounded in $\mathcal A^{2-\delta}$ ($\dot g(1,0)$, $\breve h(S)$), resp. $\mathcal A^{3-\delta}$
($\dot g(0,\dot A)$, $h(S)$), and in $C^\infty$ on compact subsets of $X$, locally uniformly in $b$; the coefficients
of $L_b$ depend smoothly on $b$. The proofs then give, uniformly for $b$ near $b_0$: (2.1) with $r^{-4+\delta}$;
$\hat f(0)$ bounded in $\mathcal A^{3-\delta}$ and $w$ in $\mathcal A^{1-\delta}$; (2.3) with
$|G|\le Cr^\delta\langle\zeta\rangle^{-N}$ (with its derivatives); Lemma 2.4 (b) for $\beta_{\mathrm{tf}}<3-\delta$;
(2.5) with $|\sigma|^{1-a-\delta}$; and the bounds in the proof of Lemma 5.2 (b) with $\rho^{3-\delta}$. By (2.2),
$\hat f(0)$ depends continuously on $b$ in $\bar H^{\infty,a}_{\mathrm b}$ for every $a<1$. Where uniformity in $b$ is
used (the bound of Proposition 3.2, Corollaries 4.2-4.3, Lemma 5.2) the weights leave room for the loss: with
$\delta := \epsilon_0 := \frac14(1-(\alpha+2))$, $\alpha+2+\epsilon_0<1-\delta$ and
$1-(\alpha+2)-\delta\ge\epsilon_0$.

## 3. The augmented zero energy operator ([Hin26] Proposition 10.6 at n = 4)

*The rows.* Fix real $f^*_1\in C^\infty_c(X^\circ;S^2T^*X)\otimes\mathfrak b^*$ and
$f^*_2\in C^\infty_c(X^\circ;S^2T^*X)\otimes\mathcal S_1^*$ such that, at $b_0$,
$$\langle\dot g(\dot b),f^*_1\rangle = \dot b,\quad\langle h(S),f^*_1\rangle = 0,\quad\langle\dot g(\dot
b),f^*_2\rangle = 0,\quad\langle h(S),f^*_2\rangle = S\tag{3.1}$$
(after fixing bases; $\langle\cdot,f^*_j\rangle$ is taken componentwise). They exist: the eleven states are independent
(III.F$'''$ Proposition 4.1 (1)), smooth on $X^\circ$, and the restriction of
$C^\infty_c(X^\circ)\to W^*$ to a finite-dimensional $W\subset\mathcal D'(X^\circ)$ is onto (III.F$'''$ Corollary 4.2,
proof). By continuity of the states in $b$ (III.F$'''$ Proposition 4.1, Step 5), the matrix
$B(b) := (\langle\cdot,f^*\rangle)$ of the nullspace in these bases is invertible near $b_0$, with $B(b_0) = I$.
(3.1) is the source's (10.6b) and more: the source asks only that the block-diagonal map
$(\dot b,S)\mapsto(\langle\dot g(\dot b),f^*_1\rangle,\langle h(S),f^*_2\rangle)$ be an isomorphism, while its proof of
Proposition 10.6 uses that $u\mapsto(\langle u,f^*_1\rangle,\langle u,f^*_2\rangle)$ is injective on the nullspace,
and under (10.6b) alone the proposition itself can fail ((H2)).

**Definition 3.1 ([Hin26] (10.26) at n = 4).** For $\mathrm{Im}\,\sigma\ge0$, acting on $(u,\dot b,S)$ with $u$ a
section over $X$, $\dot b\in\mathfrak b_{\mathbb C}$, $S\in\mathcal S_{1,\mathbb C}$,
$$\tilde L_b(\sigma)(u,\dot b,S) := \big(\widehat{L_b}(\sigma)u+\hat f_{\dot b}(\sigma)+\hat
f_S(\sigma),\ \langle u,f^*_1\rangle,\ \langle u,f^*_2\rangle\big).\tag{3.2}$$
By Lemma 2.5 (c), for $\sigma\ne0$ the column terms are $\widehat{L_b}(\sigma)\hat g^{\mathrm{aug}}(\sigma)(\dot b)$
and $\widehat{L_b}(\sigma)\hat h^{\mathrm{aug}}(\sigma)(S)$, the source's form.

**Proposition 3.2 ([Hin26] Proposition 10.6 at n = 4).** For $b$ near $b_0$ and $\alpha$ as in (1.1),
$$\tilde L_b(0):\mathcal X_0\oplus\mathfrak b_{\mathbb C}\oplus\mathcal S_{1,\mathbb C}\to\mathcal Y_0\oplus\mathfrak
b_{\mathbb C}\oplus\mathcal S_{1,\mathbb C},\qquad\mathcal X_0 = \{u\in\bar H^{s,\alpha}_{\mathrm b}:\widehat{L_b}(0)u\in
\mathcal Y_0\},\ \mathcal Y_0 = \bar H^{s-1,\alpha+2}_{\mathrm b},$$
is invertible (the column terms lie in $\mathcal Y_0$, so this is the source's domain (10.27)), with inverse bounded
uniformly near $b_0$.

*Proof.* $\hat f(0)\in\mathcal A^3\subset\bar H^{\infty,\alpha+2}_{\mathrm b}$ (Lemma 2.3; $\alpha+2<1$). *Index.* By
III.F$'''$ Proposition 4.1 at the b-weight $\alpha+2\in(0,1]$, $\widehat{L_b}(0):\mathcal X_0\to\mathcal Y_0$ is
Fredholm of index 0, so $\tilde L_b(0)$, a finite rank perturbation of $\widehat{L_b}(0)\oplus0_{\mathbb
C^{11}\to\mathbb C^{11}}$, has index 0. *Injectivity.* Let $\tilde L_b(0)(u,\dot b,S) = 0$. By (2.2),
$L_0(u+w_{\dot b}+w_S)+L_1\dot g(\dot b)+L_2h(S)+L_1\breve h(S) = 0$. Here $w := w_{\dot b}+w_S$ is smooth on $X$
and in $\mathcal A^1\subset\bar H^{\infty,\alpha}_{\mathrm b}$ near $\partial X$ (as $\alpha<-1$), and
$L_0w\in\mathcal A^3\subset\mathcal Y_0$; so $u+w\in\mathcal X_0$ and $L_0(u+w)$ is in the range of (4.1) of III.F$'''$,
which the dual states (4.3) there annihilate (III.F$'''$ Proposition 4.1 (2)). Pairing with them,
$$\langle L_1\dot g(\dot b)+L_2h(S)+L_1\breve h(S),h^*\rangle = 0,\qquad h^*\in\{h^*_{b,\mathrm s0},\ h^*_{b,\mathrm
s1}(S'),\ h^*_{b,\mathrm v1}(V)\}.$$
By III.F$''''$ Lemma 3.1 (1)-(4) this is a linear system in $(\dot\mu,S,\dot A)$ whose $11\times11$ matrix is block upper
triangular with determinant $3\pi^2(\frac{3\pi^2}2\mu)^4(2\pi^2\mu)^6\ne0$; so $\dot b = 0$, $S = 0$, hence $w = 0$, and
$u$ lies in the nullspace, spanned by the states (III.F$'''$ Proposition 4.1 (1)). As $\langle u,f^*\rangle = 0$ and
$B(b)$ is invertible, $u = 0$. *Uniform bound.* As in III.F$'''$ Corollary 4.2 (1): the coefficients of $\tilde L_b(0)$,
including $\hat f(0)$ in $\bar H^{\infty,\alpha+2}_{\mathrm b}$, depend continuously on $b$ (Remark 2.6), and the
estimate of I.C Theorem 3.1 holds uniformly near $b_0$ (I.C Theorem 7.1 (2)); the contradiction argument there applies
verbatim. $\square$

Of $s$ the proof uses only $s>\frac12+\vartheta_L$ (through III.F$'''$ Proposition 4.1 and I.C Theorems 3.1 and
7.1), so Proposition 3.2 holds at every such constant $s$, with $\mathcal X_0$, $\mathcal Y_0$ at that regularity: in
particular at the regularities $s+k$ and $s+i$ at which the proof of Theorem 4.1 inverts $\mathcal P(0)$.


The source pairs with $h^*_{b,\mathrm s0}$, then $h^*_{b,\mathrm v1}$, then $h^*_{b,\mathrm s1}$, and handles its error
term $\widehat{L_b}(0)h'$ by integration by parts against the decay of the dual states. Here the error $L_0w$ lies in the
range of $\widehat{L_b}(0)$ on the domain itself, as $w\in\mathcal A^1$ and $\alpha<-1$, so no integration by parts is
needed; and the order of the pairings is that of III.F$''''$ Lemma 3.1 (4)'s triangular matrix (rows $\dot\mu$, $S$,
$\dot A$), whose undetermined entries drop out.

## 4. Uniform low-energy estimates ([Hin26] Proposition 10.7 at n = 4)

**Theorem 4.1 (I.C Theorem 6.4 with columns depending on $\sigma$).** Assume (H1)-(H4), (G) and (TF) as in I.C Theorem
6.4, with $s>\frac12+\vartheta_{\mathcal H}$ constant, the weight $\alpha$ ($\alpha+2$ in the gap of (G)) and
$\alpha_+\in\mathbb R$, and that $\widehat P(\sigma):\mathcal X_\sigma\to\mathcal Y_\sigma$ has index 0 for
$\sigma\in\Sigma_0$. Let $\Sigma'$ be $\Sigma_0$ or $\Sigma_0\cap\mathbb R$, $m\in\mathbb N$,
$\phi_1,\dots,\phi_m\in C^\infty_c(X^\circ;E)$, $\epsilon_0\in(0,1]$, and let $F_1,\dots,F_m$ be sections over $X$
depending on $\sigma\in\Sigma'\cup\{0\}$ such that, for all $k,j\in\mathbb N_0$, every constant $s'$ and every
$\eta'\in[0,\epsilon_0]$:

(A1) $F_i(0)\in\bar H^{\infty,\alpha+2+\epsilon_0}_{\mathrm b}$;

(A2) $\sup_{\sigma\in\Sigma',\,|\sigma|\le\varsigma_1}\|(\sigma\partial_\sigma)^jF_i(\sigma)\|_{(s';k),(\mathsf
r+\alpha_++1,\alpha+2+\eta',0),|\sigma|}<\infty$, with $\varsigma_1$ that of II.G$'$ (4.5a);

(A3) $\|\chi_{\mathrm{zf}}(F_i(\sigma)-F_i(0))\|_{\bar H^{s'+k,\alpha+2}_{\mathrm b}}\le C|\sigma|^{\epsilon_0}$ for
$\sigma\in\Sigma'$, $\chi_{\mathrm{zf}}$ the cut-off of I.C section 6.4;

(A4) $\sigma\mapsto F_i(\sigma)$ is smooth on $\Sigma'$ (along $\Sigma'$) with values in $\bar H^{(s';j),\mathsf
r_{\varsigma_*}+M}$ near each $\sigma_*\in\Sigma'$, for every $M$.

Put $\mathcal P(\sigma)(u,c) := (\widehat P(\sigma)u+\sum_ic_iF_i(\sigma),(\langle u,\phi_j\rangle_h)_j)$ on
$\mathcal X_\sigma\oplus\mathbb C^m\to\mathcal Y_\sigma\oplus\mathbb C^m$ ($\mathcal X_0\oplus\mathbb C^m\to\mathcal
Y_0\oplus\mathbb C^m$ at $\sigma = 0$), and assume $\mathcal P(0)$ is invertible ((Z$_{\mathcal P}$)). Then:

(1) (*Uniform estimates.*) For every $k$ there are $c_k\in(0,\varsigma_1]$, non-increasing in $k$, and $C_k$ such that
for $\sigma\in\Sigma'$ with $|\sigma|\le c_k$ and $\mathcal P(\sigma)(u,c) = (f,e)$, $(u,c)\in\mathcal
X_\sigma\oplus\mathbb C^m$,
$$\|u\|_{(s;k),(\mathsf r+\alpha_+,\alpha,0),\varsigma}+|c|\le C_k\big(\|f\|_{(s-1;k),(\mathsf
r+\alpha_++1,\alpha+2,0),\varsigma}+|e|\big),\tag{4.1}$$
in the strong sense.

(2) (*Invertibility.*) For $\sigma\in\Sigma'$ with $|\sigma|\le c_0$, $\mathcal P(\sigma)$ is invertible.

(3) (*Derivatives in $\sigma$.*) If moreover $\widehat P(\sigma)$ is invertible for $\sigma\in\Sigma'$, $|\sigma|\le
c_0$, then for $j,k\in\mathbb N_0$ there are $c_{j,k}\in(0,c_0]$ and $C$ with
$$\|(\sigma\partial_\sigma)^j\mathcal P(\sigma)^{-1}(f,e)\|_{(s+j;k),(\mathsf r+\alpha_+,\alpha,0),\varsigma}\le
C\big(\|f\|_{(s-1;k+j),(\mathsf r+\alpha_++1,\alpha+2,0),\varsigma}+|e|\big)\tag{4.2}$$
for $\sigma\in\Sigma'$, $|\sigma|\le c_{j,k}$, the norm on the left being that of the first component plus the modulus of
the second; $(\sigma\partial_\sigma)^j\mathcal P(\sigma)^{-1}$ is the derivative on the spaces of I.A Theorem 7.2 (6),
extended by (4.2).

*Proof.* We use two facts on the norms of I.C Definition 6.1. First, for $l,q\in\mathbb R$ and $\eta\ge0$,
$$\|u\|_{(s;k),(\mathsf r,l,q-\eta),\varsigma} = \varsigma^\eta\|u\|_{(s;k),(\mathsf r,l+\eta,q),\varsigma},\tag{4.3}$$
as both squares equal $\varsigma^{-2(q-\eta)}\|(1-\chi_\partial)u\|^2+\varsigma^{-2(l+2)}\|S_\varsigma(\chi_\partial
u)\|^2_{(\mathsf r,q-\eta-l)}$. Second, for $v\in\bar H^{m,a+\epsilon_0}_{\mathrm b}$ independent of $\sigma$,
$$\|(1-\chi_{\mathrm{zf}})v\|_{\bar H^{m,a}_{\mathrm b}}\le C\varsigma^{\epsilon_0}\|v\|_{\bar
H^{m,a+\epsilon_0}_{\mathrm b}},\tag{4.4}$$
as $1-\chi_{\mathrm{zf}}$ is supported in $\{\rho\le4\varsigma\}$ and $\rho^{\epsilon_0}(1-\chi_{\mathrm{zf}})$ has
b-derivatives bounded by $C\varsigma^{\epsilon_0}$.

(1) The proof of I.C Theorem 6.4 (1) (section 6.4), with these changes. *Finiteness*: $\widehat P(\sigma)u = f-\sum
c_iF_i(\sigma)$, which lies in $\bar H^{(s-1;k),\mathsf r_\varsigma+\alpha_++1}$ by (A2) and I.C Lemma 6.2 (c). *Step
1*: the bounded inverse of $\mathcal P(0)$ at the regularity $s+k$ exists as there ($\mathcal P(0)$ is
$\widehat P(0)\oplus0$ plus a finite rank operator whose columns lie in $\mathcal Y_0$ at every regularity by (A1)), and
the identity becomes
$$\widehat P(0)(\chi_{\mathrm{zf}}u)+\sum c_iF_i(0) = \chi_{\mathrm{zf}}f-\chi_{\mathrm{zf}}(\sigma T+\sigma^2P_2)u+
[\widehat P(0),\chi_{\mathrm{zf}}]u+\sum c_i\big((1-\chi_{\mathrm{zf}})F_i(0)-\chi_{\mathrm{zf}}(F_i(\sigma)-F_i(0))
\big),$$
from $\chi_{\mathrm{zf}}(\widehat P(\sigma)u+\sum c_iF_i(\sigma)) = \chi_{\mathrm{zf}}f$. The two new terms are bounded
in $\bar H^{s+k-1,\alpha+2}_{\mathrm b}$ by $C\varsigma^{\epsilon_0}|c|$, by (4.4) with (A1), and by (A3). So (6.9) of
I.C holds with the extra term $C\varsigma^{\epsilon_0}|c|$ on the right. *Step 2*: fix $\eta$ as there and moreover
$\eta\le\epsilon_0$. Now $\chi_{\mathrm{tf}}\widehat P(\sigma)u = \chi_{\mathrm{tf}}(f-\sum c_iF_i(\sigma))$, so
$\varsigma^2N_{\mathrm{tf}}(\hat\sigma)w$ gains the term $-S_\varsigma(\sum c_i\chi_{\mathrm{tf}}F_i(\sigma))$, which
contributes, after the multiplication by $\varsigma^{-(\alpha+2)}\varsigma^{-2}$, at most
$C|c|\max_i\|\chi_{\mathrm{tf}}F_i(\sigma)\|_{(s-2;k),(\mathsf r+\alpha_++1,\alpha+2,-\eta),\varsigma} =
C\varsigma^\eta|c|\max_i\|\chi_{\mathrm{tf}}F_i(\sigma)\|_{(s-2;k),(\mathsf r+\alpha_++1,\alpha+2+\eta,0),\varsigma}\le
C\varsigma^\eta|c|$, by (4.3), I.C Lemma 6.2 (b), (d) and (A2). The conclusion of Step 2 becomes
$\|u\|_{(\alpha,-\eta)}\le C\|f\|'_{(\alpha+2,0)}+C_{\rho_c}\varsigma^\eta\|u\|_{(\alpha,0)}+C\varsigma^\eta|c|$, and
inserted in the modified (6.9),
$\|u\|_{(\alpha,0)}+|c|\le C(\|f\|'_{(\alpha+2,0)}+|e|)+C'_{\rho_c}\varsigma^\eta(\|u\|_{(\alpha,0)}+|c|)
+C\varsigma^{\epsilon_0}|c|$; the last two terms are absorbed for $\varsigma$ small.

(2) $\mathcal P(\sigma)$ is $\widehat P(\sigma)\oplus0_{\mathbb C^m\to\mathbb C^m}$, of index 0, plus a finite rank
operator (its columns lie in $\mathcal Y_\sigma$ by (A2)); so it has index 0, and by (4.1) at $k = 0$ it is injective.

(3) Let $R(\sigma) := \widehat P(\sigma)^{-1}$. For $\sigma\in\Sigma'$, $|\sigma|\le c_0$, and $(f,e)$,
$$\mathcal P(\sigma)^{-1}(f,e) = \Big(R(\sigma)\big(f-\sum_ic_iF_i(\sigma)\big),c\Big),\qquad c =
M(\sigma)^{-1}\big((\langle R(\sigma)f,\phi_j\rangle_h)_j-e\big),\quad M(\sigma)_{ji} := \langle
R(\sigma)F_i(\sigma),\phi_j\rangle_h,$$
where $M(\sigma)$ is invertible because $\mathcal P(\sigma)$ is (if $M(\sigma)c = 0$, then
$(-R(\sigma)\sum c_iF_i(\sigma),c)$ is in the kernel). Let $D$, $Z$ be as in the proof of I.C Theorem 6.4 (4) (for this
$j$). By I.A Theorem 7.2 (6), $R(\sigma):D\to Z$ is strongly $C^j$ near $\sigma_*$: for $f\in D$, $\sigma\mapsto
R(\sigma)f$ is $j$ times differentiable in $Z$, with derivatives $R^{(i)}(\sigma)f$ continuous in $\sigma$. The columns
enter with a $\sigma$-dependent argument (the point of I.C Remark 6.7 (c)): each $R^{(i)}(\sigma):D\to Z$, $i\le j$,
being strongly continuous, is bounded locally uniformly in $\sigma$ (Banach-Steinhaus), and $\sigma\mapsto F_l(\sigma)$
is $C^j$ in norm into $D$ by (A4) (with $M\ge\epsilon+\alpha_++1$ and $s'\ge s+\epsilon-1$, $\epsilon$ that of $D$).
Splitting difference quotients as
$R(\sigma')\frac{F_l(\sigma')-F_l(\sigma)}{\sigma'-\sigma}+\frac{R(\sigma')-R(\sigma)}{\sigma'-\sigma}F_l(\sigma)$
gives the Leibniz rule, and by induction $\sigma\mapsto R(\sigma)F_l(\sigma)$ is $C^j$ into $Z$. As
$\langle\cdot,\phi_j\rangle_h$ is continuous on $Z$, $M(\sigma)$ is $C^j$, hence so is $M(\sigma)^{-1}$, and
$\sigma\mapsto\mathcal P(\sigma)^{-1}(f,e)$ is $j$ times differentiable near $\sigma_*$ in $Z\oplus\mathbb C^m$ for
$(f,e)\in D\oplus\mathbb C^m$. Applying $(\sigma\partial_\sigma)^i$ to $\mathcal P(\sigma)\mathcal P(\sigma)^{-1} = I$
gives the formula of I.C section 6.6 with $\mathcal P$ for $\widehat P$, and the argument there applies: the entries of
$A_i := (\sigma\partial_\sigma)^i\mathcal P(\sigma)$ are those of I.C Lemma 6.5 in the first column and the columns
$(\sigma\partial_\sigma)^iF_l(\sigma)$, which map $\mathbb C^m$ boundedly into
$\mathcal H^{(s';k),(\mathsf r+\alpha_++1,\alpha+2,0)}_\varsigma$ for every $s'$ by (A2); the rows are constant.
$\square$

Here (Z$_{\mathcal P}$) for the source's operator is Proposition 3.2, and the index 0 at $\sigma\ne0$ replaces I.C's
adjoint estimate (6.7) in the proof of invertibility, as $\mathcal P$ has as many columns as rows (I.C (F6) needed
(6.7) for $m_1\ne m_2$).

**Corollary 4.2 ([Hin26] Proposition 10.7 at n = 4).** Let $b$ be near $b_0$, $\alpha$ as in (1.1), $\alpha_+\in\mathbb
R$, and the orders of I.C section 6 for $\widehat{L_b}$. For every $k$ there are $c_k>0$, non-increasing in $k$, and
$C_k$, uniform for $b$ near $b_0$, such that for $\sigma\in\Sigma_0$ with $|\sigma|\le c_k$:
$\tilde L_b(\sigma):\mathcal X_\sigma\oplus\mathfrak b_{\mathbb C}\oplus\mathcal S_{1,\mathbb C}\to\mathcal
Y_\sigma\oplus\mathfrak b_{\mathbb C}\oplus\mathcal S_{1,\mathbb C}$ is invertible, and
$$\|u\|_{(s;k),(\mathsf r+\alpha_+,\alpha,0),\varsigma}+|\dot b|+|S|\le C_k\|\tilde L_b(\sigma)(u,\dot
b,S)\|_{(s-1;k),(\mathsf r+\alpha_++1,\alpha+2,0),\varsigma},\tag{4.5}$$
the norm on the right being that of the first component plus the moduli of the others (the source's (10.28)).

*Proof.* Theorem 4.1 with $\widehat P = \widehat{L_b}$, $\Sigma' = \Sigma_0$, $m = 11$, the components of $f^*_1$,
$f^*_2$ (converted to $\langle\cdot,\cdot\rangle_h$ by a smooth bundle map) as rows, and as columns $F_i := \hat f_{\dot
b}$, $\hat f_S$ for basis elements, with $\epsilon_0 := \frac14(1-(\alpha+2))$. The hypotheses on $\widehat{L_b}$ are
those of section 1. (A1): $\hat f(0)\in\mathcal A^3\subset\bar H^{\infty,a}_{\mathrm b}$ for $a<1$ (Lemma 2.3), and
$\alpha+2+\epsilon_0<1$. (A2): Lemma 2.4 (b), with $l+2 = \alpha+2+\eta'<1$ and $\varsigma_1$ of (2.4), for the orders
of I.C section 6, which are of the kind of II.G$'$ Lemma 4.6 (constant $s$; $\mathsf r$ equal to a constant near the
zero section over sctf, I.C section 4.3 and I.A Lemma 7.1, as II.G$'$ Proposition 4.7's proof uses them). (A3): Lemma
2.4 (c) with $a = \alpha+2$ and $\phi = \phi_z$ of I.C section 6.4, as
$|\sigma|^{1-(\alpha+2)}\le|\sigma|^{\epsilon_0}$. (A4): Lemma 2.4 (d). (Z$_{\mathcal P}$): Proposition 3.2. *Uniformity
in $b$.* The constants of the proof of I.C Theorem 6.4 (1) are uniform near $b_0$ (I.C Theorem 7.1 (2)); the tf-normal
operator does not depend on $b$ (III.G$''''$ Lemma 1.1); the inverse of $\tilde L_b(0)$ is bounded uniformly
(Proposition 3.2); and (A1)-(A3) hold uniformly by Remark 2.6 with $\delta = \epsilon_0$, as
$\alpha+2+\epsilon_0<1-\delta$ and $|\sigma|^{1-(\alpha+2)-\delta}\le|\sigma|^{\epsilon_0}$. $\square$

**Corollary 4.3 (the low-energy range of [Hin26] Proposition 8.8, and [Hin26] (10.48), at n = 4).** Shrinking $c_0$ of
Corollary 4.2 (uniformly near $b_0$): for $b$ near $b_0$ and $\sigma\in\Sigma_0$ with $|\sigma|\le c_0$,
$\widehat{L_b}(\sigma):\mathcal X_\sigma\to\mathcal Y_\sigma$ is invertible, and for $f\in\mathcal Y_\sigma$, with
$(u,\dot b,S) := \tilde L_b(\sigma)^{-1}(f,0,0)$,
$$\widehat{L_b}(\sigma)^{-1}f = u+\hat g^{\mathrm{aug}}(\sigma)(\dot b)+\hat h^{\mathrm{aug}}(\sigma)(S).\tag{4.6}$$
Theorem 4.1 (3) therefore applies to $\tilde L_b$ on $\Sigma_0$, giving the source's (10.29).

*Proof.* *Injectivity.* Let $\widehat{L_b}(\sigma)v = 0$, $v\in\mathcal X_\sigma$. For $(\dot b,S)$ to be chosen put
$v' := v-\hat g^{\mathrm{aug}}(\sigma)(\dot b)-\hat h^{\mathrm{aug}}(\sigma)(S)\in\mathcal X_\sigma$ (Lemma 2.5 (b)).
By Lemma 2.5 (c), $\tilde L_b(\sigma)(v',\dot b,S) = (0,\langle v,f^*\rangle-M(\sigma)(\dot b,S))$, with
$M(\sigma)(\dot b,S) := \langle\hat g^{\mathrm{aug}}(\sigma)(\dot b)+\hat h^{\mathrm{aug}}(\sigma)(S),f^*\rangle$. Let
$R$ bound $\mathrm{supp}\,f^*\subset\{r\le R\}$. By Lemma 2.5 (d), on $\mathrm{supp}\,f^*$,
$\hat g^{\mathrm{aug}}(\sigma)(\dot b) = i\sigma^{-1}(1+O(\sigma))\dot g(\dot b)$ and
$\hat h^{\mathrm{aug}}(\sigma)(S) = (-\sigma^{-2}(1+O(\sigma))+O(\sigma^{-1}))h(S)+O(\sigma^{-1})\breve h(S)$. So with
$D(\sigma) := \mathrm{diag}(\sigma I_{\mathfrak b},\sigma^2I_{\mathcal S_1})$ and (3.1),
$$M(\sigma)D(\sigma) = \begin{pmatrix}iI&0\\0&-I\end{pmatrix}+O(|\sigma|)+O(|b-b_0|),$$
invertible for $\sigma$ small and $b$ near $b_0$. Choosing $(\dot b,S) := M(\sigma)^{-1}\langle v,f^*\rangle$,
$\tilde L_b(\sigma)(v',\dot b,S) = 0$, so $v' = 0$, $\dot b = 0$, $S = 0$ (Corollary 4.2), and $v = 0$. *Invertibility.*
$\widehat{L_b}(\sigma)$ has index 0 (section 1). *(4.6).* By (3.2) and Lemma 2.5 (c),
$\widehat{L_b}(\sigma)(u+\hat g^{\mathrm{aug}}(\sigma)(\dot b)+\hat h^{\mathrm{aug}}(\sigma)(S)) = f$, and the left side
of (4.6) is the unique solution in $\mathcal X_\sigma$. $\square$

**Corollary 4.4 ([Hin26] Proposition 8.8 at n = 4 near $b_0$).** There is a neighbourhood $\mathcal B$ of $b_0$ such that
for $b\in\mathcal B$ and every $\sigma\ne0$ with $\mathrm{Im}\,\sigma\ge0$, $\widehat{L_b}(\sigma):\mathcal
X_\sigma\to\mathcal Y_\sigma$ is invertible and has trivial kernel on every $\mathcal A^a$.

*Proof.* For $|\sigma|\le c_0$, Corollary 4.3, on a neighbourhood of $b_0$ independent of $\sigma$; for
$|\sigma|\ge c_0$, III.F$''$ Proposition 4.1 with this $c_0$, on its neighbourhood $\mathcal B(c_0)$. Take $\mathcal B$
the intersection. The kernel on $\mathcal A^a$ by III.F$''$ Lemma 1.3. $\square$

This closes III.F$''$ section 5: the range $0<|\sigma|<c_0$, $b\ne b_0$, which the source takes from [AHW24] Theorem 6.1
(1), follows at $n = 4$ from the zero energy structure near $b_0$ (Proposition 3.2) through the uniform low-energy
estimate, the perturbation not degenerating because $c_0$ is uniform in $b$ ((H3)).

## 5. The spectral-side augmentation ([Hin26] section 10.1.3 at n = 4)

Fix $\phi_s\in C^\infty([0,\infty))$ equal to 0 on $[0,1]$ and to 1 on $[2,\infty)$, and for real $\sigma\ne0$ put
$\chi_s := \phi_s(\rho/|\sigma|)$ (1 near zf, 0 near scf).

**Definition 5.1 ([Hin26] (10.38b), (10.39b) at n = 4).** For $0\ne\sigma\in[-1,1]$,
$\dot g^{\mathrm{sing}}(\sigma)(\dot b) := i\sigma^{-1}\chi_s\dot g(\dot b)$ and
$h^{\mathrm{sing}}(\sigma)(S) := \chi_s(-\sigma^{-2}h(S)+i\sigma^{-1}\breve h(S))$; $F'_{\dot b}(\sigma) :=
\widehat{L_b}(\sigma)\dot g^{\mathrm{sing}}(\sigma)(\dot b)$, $F'_S(\sigma) := \widehat{L_b}(\sigma)h^{\mathrm{sing}}(
\sigma)(S)$, $F'_{\dot b}(0) := L_1\dot g(\dot b)$, $F'_S(0) := L_2h(S)+L_1\breve h(S)$; and $\tilde L'_b(\sigma)$ is
(3.2) with $F'$ in place of $\hat f$ (the source's (10.41)).

**Lemma 5.2.** (a) $F'_{\dot b}(\sigma) = \chi_s(L_1\dot g-i\sigma L_2\dot g)+i\sigma^{-1}[\widehat{L_b}(\sigma),
\chi_s]\dot g$ and $F'_S(\sigma) = \chi_s(L_2h+L_1\breve h-i\sigma L_2\breve h)+[\widehat{L_b}(\sigma),\chi_s](-
\sigma^{-2}h+i\sigma^{-1}\breve h)$.

(b) The $F'$ satisfy (A1)-(A4) of Theorem 4.1 on $\Sigma' = \Sigma_0\cap\mathbb R$, with
$\epsilon_0 = \frac14(1-(\alpha+2))$, uniformly near $b_0$ (Remark 2.6).

(c) $\tilde L'_b(0)$ is invertible as in Proposition 3.2. So the conclusions of Corollary 4.2 hold for $\tilde
L'_b(\sigma)$, $0\ne\sigma\in[-c_k,c_k]$, and, $\widehat{L_b}(\sigma)$ being invertible there (Corollary 4.3), those of
Theorem 4.1 (3) too.

*Proof.* (a) $\widehat{L_b}(\sigma)(\chi_sv) = \chi_s\widehat{L_b}(\sigma)v+[\widehat{L_b}(\sigma),\chi_s]v$, with
$\widehat{L_b}(\sigma) = L_0-i\sigma L_1-\sigma^2L_2$, $L_0\dot g = 0$, $L_0h = 0$ and $L_1h+L_0\breve h = 0$:
$\widehat{L_b}(\sigma)(i\sigma^{-1}\dot g) = L_1\dot g-i\sigma L_2\dot g$, and
$\widehat{L_b}(\sigma)(-\sigma^{-2}h+i\sigma^{-1}\breve h) = -\sigma^{-2}L_0h+i\sigma^{-1}(L_1h+L_0\breve
h)+L_2h+L_1\breve h-i\sigma L_2\breve h$. (b) $[\widehat{L_b}(\sigma),\chi_s] = [L_0,\chi_s]-i\sigma[L_1,\chi_s]$ has
coefficients supported in $\{\varsigma\le\rho\le2\varsigma\}$, with $[L_0,\chi_s]\in\rho^2\mathrm{Diff}^1_{\mathrm b}$
and $[L_1,\chi_s]\in\rho\,C^\infty$, their coefficients bounded with their b-derivatives uniformly in $\varsigma$. So, as
$\rho\sim\varsigma$ there, each commutator term is $O(\rho^3)$ with its b-derivatives: $\varsigma^{-1}\rho^2\rho^2$,
$\rho\rho^2$ for $\dot g$ (weight 2; $\rho^3$ for $\dot g(0,\dot A)$), $\varsigma^{-2}\rho^2\rho^3$,
$\varsigma^{-1}\rho\rho^3$, $\varsigma^{-1}\rho^2\rho^2$, $\rho\rho^2$ for $h$ and $\breve h$. The main terms are
$\chi_s$ times $\mathcal A^3$ (the $\sigma$-free ones, (2.2)) and $\varsigma\chi_s\mathcal A^4$. Hence $F'(\sigma)$ is
supported in $\{\rho\ge\varsigma\}$, i.e. $\hat\rho\ge c$, where $\rho_{\mathrm{scf}}\ge c'$ and
$\rho_{\mathrm{tf}}\sim\rho$, and is $O(\rho^3)$ there with b-derivatives and $\sigma\partial_\sigma$-derivatives
($\sigma\partial_\sigma$ falls on $\phi_s(\rho/\varsigma)$, giving a bounded function supported where
$\rho\sim\varsigma$, and on the powers of $\sigma$); as in Lemma 2.4 (b), its $H^{k,(N,\beta_{\mathrm{tf}},0)}_{\mathrm
b,\varsigma}$-norms are bounded for $\beta_{\mathrm{tf}}<3$, and (A2) follows by II.G$'$ (4.5a). (A1): $F'(0)\in\mathcal
A^3$ by (2.2). (A3): on $\mathrm{supp}\,\chi_{\mathrm{zf}}\subset\{\rho\ge2\varsigma\}$, $\chi_s = 1$ and $d\chi_s =
0$, so $\chi_{\mathrm{zf}}(F'(\sigma)-F'(0)) = -i\sigma\chi_{\mathrm{zf}}L_2\dot g$, resp.
$-i\sigma\chi_{\mathrm{zf}}L_2\breve h$, of norm $O(|\sigma|)$ in $\bar H^{m,\alpha+2}_{\mathrm b}$ ($L_2\dot g$,
$L_2\breve h\in\mathcal A^4$). (A4): for $\sigma\ne0$, $F'(\sigma)$ is supported in $\{\rho\ge\varsigma\}$, compact in
$X$ for fixed $\sigma$, and smooth in $\sigma$. (c) $F'(0)$ is (2.2) without the terms $L_0w$, and the proof of
Proposition 3.2 used (2.2) only through them; the index argument is unchanged. $\square$

**Remark 5.3 ([Hin26] Remark 10.8 at n = 4).** $\sigma\dot g^{\mathrm{sing}}(\sigma) = i\chi_s\dot g$ and
$\sigma^2h^{\mathrm{sing}}(\sigma) = \chi_s(-h+i\sigma\breve h)$: no correction terms ((10.38a), (10.39a), which the
source obtains from its Proposition 9.30) and no logarithmic terms $\sigma\log|\sigma|$, as the naive columns are
already of tf-order 3 (they are $O(\rho_{\mathrm{tf}}^3)$), above the target's tf-weight $\alpha+4<3$ for $\mu_{\mathrm
b}$ (Lemma 2.4 (b)). The spacetime counterparts behave alike: by Lemma 2.5 (b),
$\mathcal F(\partial_{t_*}\dot g^{\mathrm{aug}})(\sigma) = -i\sigma\hat g^{\mathrm{aug}}(\sigma) = \Phi(\sigma r)\dot g$
for $r\ge1$, equal to $\dot g$ at $\sigma = 0$, with no logarithm (the source's $t_*^{-1}$- and $\log t_*$-terms of
(10.13) do not arise).

## 6. Findings, labels and sources

### 6.1 Findings

(H1) *σ-dependent columns.* The source's Proposition 10.7 extends [Hin26c] Theorem 9.41 to augmentation columns that
depend on $\sigma$ and are not compactly supported ("merely require a more attentive bookkeeping", p. 209). Part I.C's
Theorem 6.4 is stated for constant, compactly supported columns; Theorem 4.1 is the extension, with hypotheses (A1)-(A4):
the columns' zero-frequency values better than the target by $\epsilon_0$ at tf, uniform bounds, Hölder continuity of
order $\epsilon_0$ at zf, and smoothness in $\sigma$. The invertibility follows from the index, as there are as many
columns as rows; the derivatives in $\sigma$ through a Schur complement.

(H2) *The rows.* The source's (10.6b) asks that the block-diagonal map $(\dot b,\dot S)\mapsto(\langle\dot
g^\Upsilon_b(\dot b),f^*_1\rangle,\langle h_{b,\mathrm s1}(\dot S),f^*_2\rangle)$ be an isomorphism; its proof of
Proposition 10.6 uses that $u\mapsto(\langle u,f^*_1\rangle,\langle u,f^*_2\rangle)$ is injective on the nullspace,
which (10.6b) does not imply (cross terms $\langle h_{b,\mathrm s1}(S'),f^*_1\rangle$, $\langle\dot
g^\Upsilon_b(\dot b'),f^*_2\rangle$). The biorthogonal choice (3.1) gives both. Under
(10.6a)-(10.6b) alone the source's Proposition 10.6 is false, not only its proof. As the restriction
$C^\infty_c(X^\circ)\to W^*$ is onto (section 3), every matrix of pairings of the states with the rows is realised,
among them diagonal blocks $I$ and off-diagonal blocks $\langle h(S),f^*_1\rangle = eS$,
$\langle\dot g(\dot b),f^*_2\rangle = e^T\dot b$, with $e:\mathcal S_1\to\mathfrak b$ isometric in the fixed bases
($\dim\mathcal S_1 = 4\le7 = \dim\mathfrak b$; at $n = 3$, $3\le4$). Then (10.6b) holds, and for $S\ne0$,
$u := \dot g(-eS)+h(S)\ne0$ lies in the nullspace with $\langle u,f^*_1\rangle = -eS+eS = 0$ and
$\langle u,f^*_2\rangle = -e^TeS+S = 0$, so $(u,0,0)$ lies in the kernel of the source's (10.26) at $\sigma = 0$.

(H3) *Mode stability near $b_0$ at low frequency.* III.F$''$ section 5 left $\widehat{L_b}(\sigma)$, $b\ne b_0$,
$0<|\sigma|<c_0$, open. Corollaries 4.3-4.4 close it at $n = 4$, from the augmented estimate, which is uniform in $b$
(Remark 2.6), and the scaling $D(\sigma)$ of the pairing matrix; the source takes this range from [AHW24] Theorem 6.1
(1), which has no five-dimensional counterpart.

(H4) *What n = 4 removes.* No improved states (the source's Lemma 10.3 and its use of Proposition 9.11), no
correction terms in section 10.1.3, no logarithms, and the weight window (1.1) in place of
$(0,\epsilon_{\mathrm{ind}})$: the states' extra order of decay puts the naive columns $\mathcal A^3$ into the target
$\bar H^{\infty,\alpha+2}_{\mathrm b}$ for $\alpha+2<1$. The cut-off source terms are supported in a cone inside
$\iota^+$ (Lemma 2.2), so their Fourier transforms decay rapidly at scf (Lemma 2.4 (a)), and the requirement of the
source's Lemma 10.4 on $\mathsf r$ at the zero section does not arise from them.

(H5) *Proposition 10.6's error term.* The source handles $\widehat{L_b}(0)h'$, $h'\in\mathcal A^{-\epsilon}$, by
integration by parts against the dual states' decay; here $w\in\mathcal A^1$ lies in the domain, as $\alpha<-1$.

### 6.2 Labels

Proved: Lemmas 2.2-2.5, Remark 2.6, Proposition 3.2, Theorem 4.1, Corollaries 4.2-4.4, Lemma 5.2, given the parts cited.
Remark 5.3 and the comparisons with the source are commentary. READ: the source's statements quoted from pp. 200-212.
Inputs: I.A Theorem 7.2 (3), (6); I.C (1.1), Definition 6.1, Lemmas 6.2 and 6.5, Theorems 3.1, 6.4 (its proof) and 7.1
(2); II.G$'$ section 4.3 and Lemma 4.6; III.D$''$ Proposition 3.1; III.F Lemma 2.1; III.F$'$ Propositions 2.3 and 3.3;
III.F$''$ Corollary 1.2, Lemma 1.3 and Proposition 4.1; I.C Remark 6.7 (c); III.F$'''$ Propositions 2.2 (3) and 4.1 and
Corollary 4.2; III.F$''''$ section 2 and Lemma 3.1; III.G$''''$ (1.2) and Lemmas 1.1-1.2.

### 6.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 10.1, pp. 200-212
((10.5)-(10.41), Lemmas 10.3-10.5, Propositions 10.6-10.7, Remark 10.8); Proposition 8.8 for the range of
Corollary 4.4.
