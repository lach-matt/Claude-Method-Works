# Part IV$''$. Exterior estimates III: sharp decay, the Cauchy problem and the exterior solution, n = 4 ([Hin23a]
section 3.6)

*Status.* Written (D305). This part carries [Hin23a] section 3.6 (Theorem 3.35, Corollary 3.36) to [Hin26]'s
gauge-fixed operator at $n = 4$ on III.C$'$'s exterior domain $\Omega_{\mathrm{ext},r_0}$, and delivers III.C$'$
Theorem 2.1: the linear estimate (2.2) with its tame form (Theorem 2.4), the nonlinear solution (Theorem 3.1), the
backward solution on the past slab (Lemma 2.2), and both in the cut-off gauge of III.C$''$ and for the backgrounds of
III.C$'$ Remark 2.2 (2) (Corollary 4.1, finding (C$''$2)). Section 1 integrates the leading part along its two families
of curves; section 2 proves the linear theorem, in three steps: the Cauchy problem near the interior of $I_0$, Part
IV$'$'s energy estimate near $\mathscr I^+$, and the recovery of the sharp weight at $\mathscr I^+$; section 3 runs II.G
Theorem 2.1. At $n = 4$ the recovery needs two rounds and no $h$-dependent leading terms (Part IV$'$ Remark 1.3), and
only slot 6 carries a radiation field. The continuation near $\mathscr I^+$ that III.K (K2) (b) asks for, on the slab
$\mathcal S$ of III.K Proposition 1.2 as re-posed in D304, is the next part's (finding (IV$''$2)); Lemmas 1.1, 1.2 and
2.1 are stated so that it can use them. Source: [Hin23a] pp. 30-32, read at source. Amended D309: verifier 133's
findings seated (D-m1 to D-m3, D-n1 to D-n5).

## 0. Setting

$U$, $M_\sharp$, $x_I = \rho_I^{1/2}$, $X_0$, $X_I$, the edge-b and b-spaces and the weights are those of Part IV
section 0; the splitting (1.6), its slots 1-7 and $\bar A$ are III.C's (Lemma 4.2); $L_g$ is Part IV$'$ (0.2). As in Part
IV, $H^{k,(a_0,2a_I)}_{\mathrm b} = \rho_0^{a_0}\rho_I^{a_I}H^k_{\mathrm b}$, the weight at $\mathscr I^+$ being written
in powers of $x_I$; all other weights at $\mathscr I^+$ below are powers of $\rho_I$.

*Parameters.* $\ell^\flat_0$, $\ell^\flat_I$ are as in III.C$'$ (1.1), and
$$\beta := \ell^\flat_I-\tfrac32\in\big(0,\tfrac12\big),\qquad\beta<d_* := \min_{j\ne6}\bar A_{jj} =
(1-e_\Upsilon)\gamma_\Upsilon.\tag{0.1}$$
The diagonal (4.3) of III.C is $2(1-v_C)\gamma_C$, $(1-v_C)\gamma_C$, $(1-e_C)(1-v_C)\gamma_C$,
$(1-e_\Upsilon)\gamma_\Upsilon$, $\gamma_\Upsilon$, $0$, $2\gamma_\Upsilon$; the first three exceed 100 (III.F section
1: $(1-e_C)(1-v_C)\gamma_C>100$, $0<e_C,v_C<1$), and
$(1-e_\Upsilon)\gamma_\Upsilon\le\gamma_\Upsilon\le2\gamma_\Upsilon$; so $d_* = (1-e_\Upsilon)\gamma_\Upsilon$, and
$\beta<d_*$ is III.C$'$ (1.1)'s $\ell^\flat_I<\frac32+(1-e_\Upsilon)
\gamma_\Upsilon$. By III.C Lemma 4.2 the off-diagonal entries of $\bar A$ are at $(3,1)$, $(4,1)$, $(4,3)$, $(5,2)$,
$(7,3)$, $(7,4)$: no row couples to slot 6, and row 6 has no off-diagonal entry.

*Conjugation.* For a symmetric 2-tensor $\dot g$ on $U$ put $u := \rho^{-3/2}\dot g$. Then
$$L^{g,g_0}\dot g = f\iff L_gu = f_\flat := 2\rho_I\rho^{-7/2}f.\tag{0.2}$$
Multiplication by $\rho^{\pm3/2} = \rho_0^{\pm3/2}\rho_I^{\pm3/2}$ and by $\rho_I$ maps weighted b-Sobolev spaces
isomorphically onto each other with the weights shifted (b-derivatives of these functions are constant multiples of
them). So $\dot g\in H^{k,\alpha_0,\alpha_I}_{\mathrm b}$ iff $u\in H^{k,(\alpha_0-\frac32,2(\alpha_I-\frac32))}_{\mathrm
b}$, and $f\in H^{k,\alpha_0+2,\alpha_I+1}_{\mathrm b}$ iff $f_\flat\in
H^{k,(\alpha_0-\frac32,2(\alpha_I-\frac32))}_{\mathrm b}$. Put $a_0 := \alpha_0-\frac32$.

*The classes of III.C$'$ Theorem 2.1 in these terms.* The forcing class $H^{k,\alpha_0+2,(-',\ell^\flat_I+1)}_{\mathrm
b}$ (III.C Definition 5.1 (2)) has every slot in $H^{k,\alpha_0+2,\ell^\flat_I+1}_{\mathrm b}$ near $\mathscr I^+$: its
index sets $\mathcal E^C_I+1$ and $\mathcal F_{I,11}$ have real parts above $\ell^\flat_I+1$ (III.C$'$ after (1.1), and
$\min\mathrm{Re}\,\mathcal F_{I,11}\ge\frac52+(1-e_\Upsilon)\gamma_\Upsilon$ by (5.1) there). So $f_\flat\in
H^{k,(a_0,2\beta)}_{\mathrm b}$ in every slot. The solution class $H^{k,\alpha_0,(-,\ell^\flat_I)}_{\mathrm b}$
(III.C$'$ after (1.1)) has every slot in $H^{k,\alpha_0,\ell^\flat_I}_{\mathrm b}$ except
$\slashed\pi_0\dot g\in H^{k,\alpha_0,((\frac32,0),\ell^\flat_I)}_{\mathrm b}$. In terms of $u$ it is
$$\mathcal G^k_{a_0}(\Omega) := \Big\{u:\ u_j\in H^{k,(a_0,2\beta)}_{\mathrm b}\ (j\ne6),\ \ u_6 = \chi_Iu^{(0)}+\tilde
u_6,\ \ u^{(0)}\in H^{k,a_0}_{\mathrm b}(\mathscr I^+\cap\bar\Omega),\ \tilde u_6\in H^{k,(a_0,2\beta)}_{\mathrm
b}\Big\},\tag{0.3}$$
with $\chi_I := \hat\chi(\rho_I)$, $\hat\chi\in C^\infty_c([0,\frac c2))$ equal to 1 near 0, $c$ the constant of Lemma
2.1 (so $u^{(0)}$ is used only over $\Omega_c$; another $\hat\chi$ gives an equivalent norm; verifier 133's D-n2),
$u^{(0)}$ extended constant in $\rho_I$, and the norm the sum of the norms; the radiation field of $\slashed\pi_0\dot g$
is $\rho_0^{3/2}u^{(0)}$, the coefficient of $\rho_I^{3/2}$. Away from $U$ the classes impose only $H^k$.

*The operator.* Let $g_0\in\mathcal G$ (III.C Definition 3.4) with $\mathrm{Ric}(g_0) = 0$ and $g_0-g_{b_0}$ small in the
sense of III.C$'$ Lemma 1.1, or $g_0 = g_{b_0}$; let $h\in H^{\infty,\ell^\flat_0,(-,\ell^\flat_I)}_{\mathrm
b}(\Omega_{\mathrm{ext},r_0};S^2T^*)$ and $g := g_0+h$. In Part IV$'$'s terms $h\in H^{k,(\mathcal E_0,\ell_0),(\mathcal
F,\ell_I)}_{\mathrm b}$ for every $k$, with $\mathcal E_0 := \emptyset$, $\ell_0 := \ell^\flat_0$, $\mathcal F :=
\{(\frac{3j}2,0):j\ge1\}$ and $\ell_I := \ell^\flat_I$: $\mathcal F+\mathcal F\subset\mathcal F$, and Part IV$'$ (0.1)
holds, $\min\mathrm{Re}\,\mathcal F = \frac32$ and $\ell^\flat_I>\frac32$. So Part IV$'$ Proposition 1.2 applies to
$L_g$ on $U$: in its coefficient class $H^{k-2,(\mathcal E_0,\ell_0),(\mathcal F-1,\ell_I-1)}_{\mathrm b}$ the exponents
at $\mathscr I^+$ are $\frac{3j}2-1\ge\frac12$ and the weight is $\ell^\flat_I-1>\frac12$, so
$$\tilde L_g = x_I\sum_i\big(a_i+\tilde a_i\big)P_i,\qquad a_i\in C^\infty(M_\sharp),\ \ \tilde a_i\in x_I^{-1}
H^{k-2,(\mathcal E_0,\ell_0),(\mathcal F-1,\ell_I-1)}_{\mathrm b},\ \ P_i\in\mathrm{Diff}^2_{\mathrm{e,b}},\tag{0.4}$$
with $\tilde a_i$ bounded (its expansion starts at $\rho_I^0$) and $\|\tilde a_i\|_{H^{j}}\le C\|h\|_{H^{j+2}}$ in these
classes (Part IV$'$ Proposition 1.2's proof: the coefficients are rational in $h$ and two b-derivatives of it). $L$
denotes $L^{g,g_0}$, or $L^{\chi_0}_{g,g_0}$ in section 4.

*Domains.* $\Omega^+ := \Omega_{\mathrm{ext},r_0}\cap\{t_{\mathrm{IVP}}\ge0\}$ and the past slab $\Omega^- :=
\Omega_{\mathrm{ext},r_0}\cap\{t_{\mathrm{IVP}}\le0\}$. For $|x|$ large $t_{\mathrm{IVP}} = t-C''$ (III.B Lemma 3.7
(b)), and
$$\Omega^+ = \{0\le t_{\mathrm{IVP}}\le F_0(|x|)\},\qquad F_0(r) := r+2r^{1-\ell^\flat_I}-(r_0+2r_0^{1-\ell^\flat_I}),
\tag{0.5}$$
which is empty where $r<r_0$; $\Omega_{\mathrm{ext},r_0}\subset U\cap\{|x|\ge r_0\}$ (III.C$'$ Lemma 1.1's proof). Near
the interior of $I_0$, $\tau := t/|x|$ and $\rho = |x|^{-1}$ are III.B's coordinates, $\rho_I = 1-\tau+2\rho$ (Part IV
section 4), and $\tau' := t_{\mathrm{IVP}}/|x| = \tau-C''\rho$.

## 1. The two families of curves ([Hin23a] Theorem 3.35's integrations)

**Lemma 1.1 (the curves).** Let $c\in(0,\frac12]$ and $r_0\ge\max(R_0,4|C''|+4)$.

(a) $\{\rho_I = c\}\cap U = \{t = (1-c)|x|+2\}$ is spacelike for $g_{b_0}$ near infinity, and $\{\rho_I<c\}$ lies to its
future. $\Omega^-\subset\{\rho_I\ge\frac12\}$.

(b) Let $p\in\Omega^+$ with $\rho_I(p)<c$. The integral curve of $X_I$ through $p$ (fixed $\rho_0$, $\omega$: the
outgoing ray of $\eta$ at fixed $x^1$) and that of $X_0-X_I$ (fixed $|x|$, $\omega$, increasing $t$), followed in the
direction of increasing $\rho_I$, stay in $\Omega^+$ until they reach $\{\rho_I = c\}$, which they do.

*Proof.* (a) $\rho_I = (2-x^1)/|x| = c$ iff $t = (1-c)|x|+2$. For $\eta$, $\zeta := dt-(1-c)d|x|$ has
$\eta^{-1}(\zeta,\zeta) = -1+(1-c)^2<0$; the correction from $g_{b_0}-\eta$, $O(|x|^{-2})$ in the frame (III.C Lemma
1.3), does not change the sign for $|x|$ large. Along $\partial_t$, $\rho_I$ decreases. On $\Omega^-$, $t\le C''$, so
$\rho_I\ge (2-C''+|x|)/|x|\ge\frac12$ for $|x|\ge r_0$.

(b) *The $X_I$-curve.* Along it $x^1 = x^1_p$ is fixed and $|x|$ decreases from $|x|_p$ to $r_c := (2-x^1_p)/c$, where
$\rho_I = c$. The upper condition of (0.5) is $x^1\le C''-r_0-2r_0^{1-\ell^\flat_I}+2|x|^{1-\ell^\flat_I}$, whose right
side decreases in $|x|$ ($\ell^\flat_I>1$); it holds at $p$, so at every smaller $|x|$. It gives $x^1_p\le C''-r_0<0$.
The lower condition is $x^1_p+|x|\ge C''$, decreasing along the curve; at $r_c$,
$x^1_p+r_c = x^1_p(1-c^{-1})+2c^{-1}\ge|x^1_p|\ge r_0-C''>C''$, as $c^{-1}-1\ge1$. And $r_c\ge(2+r_0-C'')/c\ge r_0$.
*The $(X_0-X_I)$-curve.* Along it $|x| = |x|_p$ and $t$ decreases to $t_c := (1-c)|x|_p+2$. The upper condition is
monotone in $t$; the lower one holds at $t_c$, as $t_c-C''\ge\frac12|x|_p+2-C''>0$. In both cases $\rho_I$ increases to
$c$ along the curve. $\square$

Both curves are integral curves of commuting b-vector fields: in the coordinates $(\rho_0,\rho,\omega)$, $X_I =
\rho\partial_\rho|_{\rho_0}$ and $X_0-X_I = \rho_0\partial_{\rho_0}|_\rho$; $X_0$, $X_I$ and the rotation fields of
$\mathbb S^3$ commute with both.

**Lemma 1.2 (integration).** Let $c$, $r_0$ be as in Lemma 1.1, $\Omega_c := \Omega^+\cap\{\rho_I<c\}$, $m\in\mathbb
N_0$, $a_0,\gamma\in\mathbb R$, and $w\in H^{m,(a_0,2\gamma)}_{\mathrm b}(\Omega_c)$ vanishing on $\{\rho_I>\frac c2\}$.
Let $v$ on $\Omega_c$ vanish on $\{\rho_I>\frac c2\}$.

(a) If $(X_I-d)v = w$ with $d>\gamma$, then $\|v\|_{H^{m,(a_0,2\gamma)}_{\mathrm b}}\le(d-\gamma)^{-1}\|w\|_{H^{m,(a_0,
2\gamma)}_{\mathrm b}}$.

(b) If $X_Iv = w$ and $\gamma>0$, then $v = v^{(0)}+\tilde v$ with $v^{(0)}$ a function of $(\rho_0,\omega)$, and
$$\|v^{(0)}\|_{H^{m,a_0}_{\mathrm b}(\mathscr I^+\cap\bar\Omega_c)}\le(2\gamma)^{-1/2}c^{\gamma}\|w\|_{H^{m,(a_0,
2\gamma)}_{\mathrm b}},\qquad\|\tilde v\|_{H^{m,(a_0,2\gamma)}_{\mathrm b}}\le\gamma^{-1}\|w\|_{H^{m,(a_0,2\gamma)}_{
\mathrm b}}.$$

(c) If $(X_0-X_I)v = w$ and $a_0>\gamma$, then $\|v\|_{H^{m,(a_0,2\gamma)}_{\mathrm b}}\le(a_0-\gamma)^{-1}\|w\|_{H^{m,
(a_0,2\gamma)}_{\mathrm b}}$.

The norms are those of the b-density $|\frac{d\rho_0}{\rho_0}\frac{d\rho_I}{\rho_I}d\slashed g|$, equivalent to
$\mu_{\mathrm b}$'s on $\Omega_c$ (Part IV Lemma 2.1).

*Proof.* (a), (b): in the coordinates $(s,\rho_0,\omega)$, $s := \log\rho_I$, $X_I = \partial_s$ and the density is
$ds\,\frac{d\rho_0}{\rho_0}d\slashed g$. By Lemma 1.1 (b), for $p\in\Omega_c$ the segment of its $X_I$-curve from $p$ to
$s_c := \log c$ lies in $\Omega_c$, and $v = 0$ near $s_c$. So $v(s) = -\int_s^{s_c}e^{d(s-s')}w(s')\,ds'$, with $w$
extended by zero along the curve outside $\Omega_c$. Hence
$$e^{-\gamma s}|v(s)|\le\int_s^{s_c}e^{-(d-\gamma)(s'-s)}e^{-\gamma s'}|w(s')|\,ds',$$
a convolution with a kernel of $L^1$-norm $(d-\gamma)^{-1}$; Young's inequality in $s$, then integration in
$(\rho_0,\omega)$ with the weight $\rho_0^{-2a_0}$, gives (a) for $m = 0$. For (b), $d = 0$: $v = v^{(0)}+\tilde v$ with
$v^{(0)} := -\int_{-\infty}^{s_c}w\,ds'$ and $\tilde v(s) := \int_{-\infty}^sw\,ds'$. By Cauchy-Schwarz,
$|v^{(0)}|^2\le\int_{-\infty}^{s_c}e^{2\gamma s'}ds'\int e^{-2\gamma s'}|w|^2ds'$, and
$e^{-\gamma s}|\tilde v(s)|\le\int_{-\infty}^se^{-\gamma(s-s')}e^{-\gamma s'}|w(s')|ds'$, a kernel of $L^1$-norm
$\gamma^{-1}$. (c): in the coordinates $(z,y,\omega)$, $z := \log\rho_0$, $y := \log\rho$, $X_0-X_I = \partial_z$ and
$\log\rho_I = y-z$, so the density is $dz\,dy\,d\slashed g$ and $\{\rho_I = c\}$ is $\{z = z_c(y) := y-\log c\}$. By
Lemma 1.1 (b), $v(z,y) = \int_{z_c(y)}^zw(z',y)\,dz'$. The weight is $\rho_0^{-a_0}\rho_I^{-\gamma} = e^{-\gamma
y}e^{-(a_0-\gamma)z}$, and
$$e^{-(a_0-\gamma)z}|v(z)|\le\int_{z_c}^ze^{-(a_0-\gamma)(z-z')}e^{-(a_0-\gamma)z'}|w(z')|\,dz',$$
a kernel of $L^1$-norm $(a_0-\gamma)^{-1}$; Young's inequality in $z$ gives (c) for $m = 0$.

*Derivatives.* Let $V$ be one of $X_0$, $X_I$ and the rotation fields. $V$ commutes with $X_I$ and with $X_0-X_I$, and
$Vv$ vanishes where $v$ does; so $Vv$ solves the same equation with $Vw$, and the $m = 0$ bounds apply to it. (In (c),
differentiating the integral in $y$ produces the boundary term $w(z_c(y),y)\,\partial_yz_c$, which vanishes as $w = 0$
near $\{\rho_I = c\}$.) Induction on $m$ gives the bounds for $m\ge1$, with the same constants; for $v^{(0)}$ the fields
tangent to $\mathscr I^+$ are $X_0$ and the rotations, and $X_Iv^{(0)} = 0$. $\square$

## 2. The linear theorem ([Hin23a] Theorem 3.35 and III.C$'$ (2.2) at n = 4)

**Lemma 2.1 (the region of the radiation field).** Fix $c\in(0,\frac12]$ so small that Part IV$'$ Proposition 2.2 holds
on $\Omega_c$ with $\Sigma_{\mathrm{in}} := \{\rho_I = c\}\cap\Omega^+$ and $\Sigma_{\mathrm{fin}} :=
\Sigma_{\mathrm{fut},r_0}\cap\{\rho_I<c\}$. These are admissible in Part IV section 3: $\Omega_c\subset\Omega_{\mathrm{
ext},r_0}\subset U$ and $\Omega_c\subset\{x_I<c^{1/2}\}$; $\Sigma_{\mathrm{in}}$ is spacelike with $\Omega_c$ to its
future (Lemma 1.1 (a)); $\Sigma_{\mathrm{fin}}$ is spacelike for $g$ (III.C$'$ Lemma 1.1); and every $X_I$-curve in
$\Omega_c$ begins on $\Sigma_{\mathrm{in}}$ (Lemma 1.1 (b)). $\square$

**Lemma 2.2 (the Cauchy problem near the interior of $I_0$, both directions).** Let $\Omega_N :=
\Omega_{\mathrm{ext},r_0}\cap\{\tau'\le\frac14\}$, which contains $\Omega^-$, and $\alpha\in\mathbb R$, $s\in\mathbb
N_0$. For $h$ small in $H^5$ with $h\in H^{s+2}$ (verifier 133's D-m1: the tame term carries $\|h\|_{H^{s+2}}$), $f\in
H^{s,\alpha+2}_{\mathrm b}(\Omega_N)$ and data $\dot g_j\in H^{s+1-j,\alpha}_{\mathrm b}(\Sigma_{\mathrm{IVP},r_0})$, $j
= 0,1$, there is a unique $\dot g\in H^{s+1,\alpha}_{\mathrm b}(\Omega_N)$ with $L\dot g = f$, $\dot g = \dot g_0$ and
$r\mathcal L_{\partial_{t_{\mathrm{IVP}}}}\dot g = \dot g_1$ on $\Sigma_{\mathrm{IVP},r_0}$, and
$$\|\dot g\|_{H^{s+1,\alpha}_{\mathrm b}(\Omega_N)}\le C\big(\|f\|_{H^{s,\alpha+2}_{\mathrm b}}+\|\dot
g_0\|_{H^{s+1,\alpha}_{\mathrm b}}+\|\dot g_1\|_{H^{s,\alpha}_{\mathrm b}}\big)+C\|h\|_{H^{s+2}}\big(\|f\|_{H^{4,\alpha
+2}_{\mathrm b}}+\|\dot g_0\|_{H^{5,\alpha}_{\mathrm b}}+\|\dot g_1\|_{H^{4,\alpha}_{\mathrm b}}\big).\tag{2.1}$$
Here the weight at $I_0$ is a power of $\rho$; on $\Omega_N$, $\rho_I\ge\frac12$, so it is one of $\rho_0$.

*Proof.* On $\Omega_N$, $\tau'\in[-\frac1{12},\frac14]$ (III.C$'$ Lemma 1.1: $t_{\mathrm{IVP}}\ge-\frac{|x|-r_0}{12}$),
so $\tau\in[-\frac1{12}-\epsilon,\frac14+\epsilon]$ for $r_0$ large, inside Part IV Proposition 4.1's range with
$\delta = \frac12$. That proposition, for the system as in Part IV$'$ Proposition 2.2's proof (the principal part is
scalar, the first-order terms are bounded b-operators, absorbed by the exponential weight), and with $\tau$ replaced by
$\tau'$, applies here: $\tau'$ is a smooth function near the interior of $I_0$ with $G_{\mathrm b}(d\tau',d\tau') =
G_{\mathrm b}(d\tau,d\tau)+O(\rho) = \tau^2-1+O(\rho)<0$, and its proof uses only that $d\tau$ is uniformly timelike in
the b-sense on the $\tau$-range and that $L\in\rho^2\mathrm{Diff}^2_{\mathrm b}$ is a wave operator; the change
$L-L_{b_0}$ lies in $\rho^2(\rho C^\infty+H^{s_0-2})\mathrm{Diff}^2_{\mathrm b}$, small for $h$ and $g_0-g_{b_0}$ small
(III.C Proposition 4.4, near the interior of $I_0$; III.C$''$ Lemma 2.1 for $L^{\chi_0}$). Two changes are needed.

*Data.* Proposition 4.1 has vanishing data and $f$ vanishing near the initial surface. With the data above, the energy
identity of its proof, on $\{0\le\tau'\le\tau'_1\}$, has in addition the flux through $\Sigma_{\mathrm{IVP},r_0} =
\{\tau' = 0\}$ of the energy current of its multiplier, bounded by
$C(\|\dot g_0\|^2_{H^{1,\alpha}_{\mathrm b}}+\|\dot g_1\|^2_{H^{0,\alpha}_{\mathrm b}})$, as
$r\partial_{t_{\mathrm{IVP}}} = \partial_{\tau'}$ modulo b-vector fields tangent to $\{\tau' = 0\}$ (with
$\rho\partial_\rho$ at fixed $\tau'$). The term on the left of the identity coming from $f$ does not need $f$ to vanish
there. This gives the case $s = 0$. For $s\ge1$, commute the b-vector fields tangent to $\{\tau' = 0\}$,
$\rho\partial_\rho|_{\tau'}$ and the rotations: their commutators with $L$ lie in $\rho^2\mathrm{Diff}^2_{\mathrm b}$
(with coefficients in $H^{s_0-3}$ for the perturbation), of first order in the commuted fields, and their data are
tangential derivatives of $\dot g_0$, $\dot g_1$ together with one normal derivative, given at $\{\tau' = 0\}$ by the
data and the equation; the commutator terms enter as sources and are absorbed as in Proposition 4.1's proof. The normal
derivatives $\partial^2_{\tau'}$ are recovered from the equation, which is non-characteristic at the level sets of
$\tau'$. The tame term comes from the Moser estimate (Part IV$'$ Lemma 2.3) for the perturbation's coefficients, which
are rational in $h$ and two of its b-derivatives.

*Both directions.* On $\Omega^+\cap\Omega_N$ the solution is the forward one; on $\Omega^-$ it is the backward one,
given by the same argument run backward in time, which uses only the b-structure of $L$, that $d\tau'$ is timelike, and
that $\Sigma_{\mathrm{past},r_0}$ is spacelike (III.C$'$ Lemma 1.1). ($t\mapsto-t$ is not an isometry of the gauge-fixed
operator, whose $E_C$-term is odd in time; verifier 133's D-n4.) Uniqueness: the estimate applied to the difference of
two solutions, which have vanishing data and source. $\square$

**Lemma 2.3 (the forward problem with growth at $\mathscr I^+$; Part IV Remark 4.2 for the system).** Let $\Omega^+_1
:= \Omega^+\cap\{\tau'\ge\frac1{16}\}$, $a_0\in\mathbb R$, $\alpha_I<\min(a_0,0)$, $3\le m\le k_h-3$, $k_h\ge8$, with
$h\in H^{k_h}$ small in $H^8$ (verifier 133's D-n1), and let $f_\flat\in H^{m,(a_0,2\alpha_I)}_{\mathrm b}(\Omega^+_1)$
vanish on $\{\tau'<\frac18\}$. The forward solution $u$ of $L_gu = f_\flat$ on $\Omega^+_1$, vanishing on
$\{\tau'<\frac18\}$, satisfies
$$\|u\|_{H^{m+1,a_0}_{\mathrm b}(\Omega^+_1\cap\{\rho_I>\frac c2\})}+\|u\|_{H^{(1;m),(a_0,2\alpha_I)}_{\mathrm{e,b;b}}
(\Omega_c)}\le C\big(\|f_\flat\|_{H^{m,(a_0,2\alpha_I)}_{\mathrm b}}+\|h\|_{H^{m+3}}\|f_\flat\|_{H^{4,(a_0,2\alpha_I)}_{
\mathrm b}}\big).\tag{2.2}$$

*Proof.* *Away from $\mathscr I^+$.* $\Omega' := \Omega^+_1\cap\{\rho_I>\frac c4\}$ lies in
$\{\frac1{16}\le\tau'\le1-\frac c8\}$ for $r_0$ large ($\rho_I = 1-\tau+2\rho$). Its interior boundary consists of
$\{\tau' = \frac1{16}\}$, initial, and the piecewise smooth $(\{\rho_I = \frac c4\}\cup\Sigma_{\mathrm{fut},r_0})\cap
\bar\Omega'$, spacelike (Lemma 1.1 (a), III.C$'$ Lemma 1.1) with $\Omega'$ to its past. Part IV Proposition 4.1, for the
system and with $\tau'$, as in Lemma 2.2's proof, gives $u_1$ on $\Omega'$ with $\|u_1\|_{H^{m+1,a_0}_{\mathrm b}}\le
C(\|f_\flat\|_{H^{m,a_0}_{\mathrm b}}+\text{tame})$; on $\Omega'$, $\rho_I>\frac c4$, so the weight at $\mathscr I^+$
is immaterial. Its past closedness (the boundary to its future is spacelike) makes $u_1 = u$ on $\Omega'$ (II.F Lemma
1.3).

*Near $\mathscr I^+$.* Let $\chi_c := \hat\chi_c(\rho_I)$ with $\hat\chi_c = 1$ on $[\frac c2,\infty)$ and $0$ on
$[0,\frac c4]$, and $u_2 := u-\chi_cu_1$ on $\Omega_c$. Then $u_2 = 0$ on $\{\rho_I>\frac c2\}$, and
$$L_gu_2 = f_3 := (1-\chi_c)f_\flat-[L_g,\chi_c]u_1,$$
which vanishes on $\{\rho_I>\frac c2\}$, hence near $\Sigma_{\mathrm{in}} = \{\rho_I = c\}$. The commutator is a
first-order b-operator supported in $\{\frac c4\le\rho_I\le\frac c2\}$, so $\|[L_g,\chi_c]u_1\|_{H^{m,(a_0,2\alpha_I)}_{
\mathrm b}}\le C\|u_1\|_{H^{m+1,a_0}_{\mathrm b}(\Omega')}$. $u_2$ is the forward solution on $\Omega_c$ from
$\Sigma_{\mathrm{in}}$ (uniqueness by II.F Lemma 1.3), and Part IV$'$ Proposition 2.2 on $\Omega_c$ (Lemma 2.1) gives the
second term of (2.2). $\square$

**Theorem 2.4 (the linear exterior estimate; [Hin23a] Theorem 3.35 at n = 4, III.C$'$ (2.2) and (5.52)).** Let
$\alpha_0>\ell^\flat_I$, $a_0 := \alpha_0-\frac32$, $k\in\mathbb N_0$, $d := 4$, and let $h$ be small in
$H^{8,\ell^\flat_0, (-,\ell^\flat_I)}_{\mathrm b}$. For $f\in H^{k+d,\alpha_0+2,(-',\ell^\flat_I+1)}_{\mathrm
b}(\Omega_{\mathrm{ext},r_0})$ and $\dot g_0,\dot g_1\in H^{k+d,\alpha_0}_{\mathrm b}(\Sigma_{\mathrm{IVP},r_0})$ there
is a $\dot g\in H^{k,\alpha_0,(-,\ell^\flat_I)}_{\mathrm b}(\Omega_{\mathrm{ext},r_0})$, unique in
$H^{\max(k,1),\alpha_0,(-,\ell^\flat_I)}_{\mathrm b}$ (the energy estimate needs $H^1$; verifier 133's D-n5), with
$L\dot g = f$, $\dot g|_{\Sigma_{\mathrm{IVP}, r_0}} = \dot g_0$ and $r\mathcal L_{\partial_{t_{\mathrm{IVP}}}}\dot
g|_{\Sigma_{\mathrm{IVP},r_0}} = \dot g_1$; and with $N(f,\dot g_0,\dot g_1;j) :=
\|f\|_{H^{j,\alpha_0+2,(-',\ell^\flat_I+1)}_{\mathrm b}}+\|\dot g_0\|_{H^{j,\alpha_0}_{\mathrm b}}+\|\dot
g_1\|_{H^{j,\alpha_0}_{\mathrm b}}$,
$$\|\dot g\|_{H^{k,\alpha_0,(-,\ell^\flat_I)}_{\mathrm b}}\le C\big(N(f,\dot g_0,\dot g_1;k+d)+\|h\|_{H^{k+d+3,
\ell^\flat_0,(-,\ell^\flat_I)}_{\mathrm b}}N(f,\dot g_0,\dot g_1;8)\big),\tag{2.3}$$
with $C$ depending on $k$, $\alpha_0$, $\ell^\flat_I$, the parameters and the bound on $h$ in $H^8$, not on $h$
otherwise. At $\alpha_0 = \ell^\flat_0$ this is III.C$'$ (2.2) in its tame form, the source's (5.52); (2.2) itself
follows with $C$ depending on $h$.

*Proof.* *Step 1 (near $\Sigma_{\mathrm{IVP}}$).* Lemma 2.2 with $s := k+3$, $\alpha := \alpha_0$ gives $\dot g_N$ on
$\Omega_N$, including the past slab, bounded in $H^{k+4,\alpha_0}_{\mathrm b}$ by (2.1).

*Step 2 (the forcing for the rest).* Let $\chi := \hat\chi_N(\tau')$, $\hat\chi_N = 1$ on $(-\infty,\frac18]$ and 0 on
$[\frac14,\infty)$. On $\Omega^+$, $w := \dot g-\chi\dot g_N$ must satisfy
$$Lw = f_2 := (1-\chi)f-[L,\chi]\dot g_N,\qquad w = 0\ \text{on }\{\tau'<\tfrac18\},$$
as $\dot g = \dot g_N$ on $\Omega_N$ (uniqueness in Lemma 2.2). $f_2$ vanishes on $\{\tau'<\frac18\}$, and
$[L,\chi]\in\rho^2\mathrm{Diff}^1_{\mathrm b}$ is supported in $\{\frac18\le\tau'\le\frac14\}$, where $\rho_I\ge\frac12$,
so $\|[L,\chi]\dot g_N\|_{H^{k+3,\alpha_0+2,(-',\ell^\flat_I+1)}_{\mathrm b}}\le C\|\dot g_N\|_{H^{k+4,\alpha_0}_{\mathrm
b}}$. Put $u := \rho^{-3/2}w$; then $L_gu = f_{2,\flat} := 2\rho_I\rho^{-7/2}f_2\in H^{k+3,(a_0,2\beta)}_{\mathrm b}$ in
every slot (section 0).

*Step 3 (growth).* Fix $\epsilon := \frac14(\frac12-\beta)>0$ and $\gamma_0 := \beta-1+2\epsilon<0$; $\gamma_0<
\min(a_0,0)$, as $a_0>\beta>\gamma_0$. Lemma 2.3 with $m := k+3$, $\alpha_I := \gamma_0$ gives $u$ on $\Omega^+_1$, with
(2.2), and $u = 0$ on $\{\tau'<\frac18\}$, so $u$ is the solution on $\Omega^+$. On $\Omega^+\cap\{\rho_I>\frac c2\}$
this already bounds $u$ in $H^{k+4,a_0}_{\mathrm b}$, which is the claim there.

*Step 4 (the equation near $\mathscr I^+$).* On $\Omega_c$, with $u_2$ of Lemma 2.3's proof, $u_2 = 0$ on
$\{\rho_I>\frac c2\}$ and, by Part IV$'$ (1.1),
$$\big(X_I-\bar A\big)(X_0-X_I)u_2 = F := -\tfrac12\big(f_3-x_I^2\slashed\Delta u_2-\tilde L_gu_2\big).\tag{2.4}$$
*The gain.* For $u_2\in H^{j,(a_0,2\gamma)}_{\mathrm b}$, $x_I^2\slashed\Delta u_2$ and $\tilde L_gu_2$ lie in
$H^{j-2,(a_0,2\gamma+1-2\epsilon)}_{\mathrm b}$: $x_I^2\slashed\Delta$ and $x_Ia_iP_i$ carry the factor $x_I$ and are of
second order; for $x_I\tilde a_iP_i$, Part IV$'$ Lemma 2.3 with $\tilde a_i\in L^\infty$ and $\tilde a_i\in
H^{j-2,(\ell^\flat_0,-2\epsilon)}_{\mathrm b}$ (its expansion at $\mathscr I^+$ starts at $\rho_I^0$, which lies in every
$x_I^{-2\epsilon}L^2_{\mathrm b}$ near $\mathscr I^+$ but not in $L^2_{\mathrm b}$), and $P_iu_2\in
x_I^{2\gamma}L^\infty$ by the embedding (0.1) of Part IV, gives
$$\|x_I\tilde a_iP_iu_2\|_{H^{j-2,(a_0,2\gamma+1-2\epsilon)}_{\mathrm b}}\le C\big(\|u_2\|_{H^{j,(a_0,2\gamma)}_{\mathrm
b}}+\|h\|_{H^{j}}\|u_2\|_{H^{5,(a_0,2\gamma)}_{\mathrm b}}\big).\tag{2.5}$$
With $u_2\in H^{(1;m)}_{\mathrm{e,b;b}}$ in place of $H^{j}$, the loss is one b-derivative instead of two, as
$P_i\in\mathrm{Diff}^1_{\mathrm{e,b}}\mathrm{Diff}^1_{\mathrm b}$ and $x_I^2\slashed\Delta\in
x_I\mathrm{Diff}^1_{\mathrm{e,b}}\mathrm{Diff}^1_{\mathrm b}$. And $f_3\in H^{k+3,(a_0,2\beta)}_{\mathrm b}$:
$f_{2,\flat}$ is, and $[L_g,\chi_c]u_1$ is supported in $\{\rho_I\ge\frac c4\}$.

*Step 5 (the integration, slot by slot).* Write (2.4) by slots. As $\bar A$ is lower triangular with the entries of
section 0, for $j\ne6$
$$(X_I-\bar A_{jj})Y_j = F_j+\sum_{i<j,\,i\ne6}\bar A_{ji}Y_i,\qquad Y_j := (X_0-X_I)u_{2,j},\tag{2.6}$$
and, $X_I$ and $X_0-X_I$ commuting, for slot 6
$$(X_0-X_I)Z_6 = F_6,\qquad Z_6 := X_Iu_{2,6}.\tag{2.7}$$
All of $Y_j$, $Z_6$, $u_2$, $F$ vanish on $\{\rho_I>\frac c2\}$, so Lemma 1.2 applies; the solution of each equation
vanishing there is unique (it is an ordinary differential equation along curves that reach $\{\rho_I = c\}$, Lemma 1.1
(b)).

*Round 1.* $u_2\in H^{(1;k+3),(a_0,2\gamma_0)}_{\mathrm{e,b;b}}$ (Step 3), so by Step 4, $F\in
H^{k+2,(a_0,2\gamma_1)}_{\mathrm b}$ with $\gamma_1 := \min(\beta,\gamma_0+\frac12-\epsilon) = \beta-\frac12+\epsilon<0$.
For $j\ne6$, in the order 1, 2, 3, 4, 5, 7, Lemma 1.2 (a) with $d = \bar A_{jj}\ge d_*>\gamma_1$ gives $Y_j\in
H^{k+2,(a_0,2\gamma_1)}_{\mathrm b}$, the right side of (2.6) lying there by induction; then Lemma 1.2 (c),
$a_0>\gamma_1$, gives $u_{2,j}\in H^{k+2,(a_0,2\gamma_1)}_{\mathrm b}$. For slot 6, Lemma 1.2 (c) gives $Z_6$, and Lemma
1.2 (a) with $d = 0>\gamma_1$ gives $u_{2,6}\in H^{k+2,(a_0,2\gamma_1)}_{\mathrm b}$.

*Round 2.* Now $u_2\in H^{k+2,(a_0,2\gamma_1)}_{\mathrm b}$, so by Step 4 (with two derivatives lost), $F\in
H^{k,(a_0,2\gamma_2)}_{\mathrm b}$, $\gamma_2 := \min(\beta,\gamma_1+\frac12-\epsilon) = \beta$. As in round 1, with
$d_*>\beta$ (0.1) and $a_0>\beta$, $u_{2,j}\in H^{k,(a_0,2\beta)}_{\mathrm b}$ for $j\ne6$. For slot 6, $Z_6\in
H^{k,(a_0,2\beta)}_{\mathrm b}$ by Lemma 1.2 (c), and Lemma 1.2 (b), $\beta>0$, gives $u_{2,6} = u^{(0)}+\tilde u_6$ with
$u^{(0)}\in H^{k,a_0}_{\mathrm b}(\mathscr I^+\cap\bar\Omega_c)$, $\tilde u_6\in H^{k,(a_0,2\beta)}_{\mathrm b}$.

*Step 6 (assembly).* On $\Omega_c$, $u = u_2+\chi_cu_1$, with $\chi_cu_1$ supported in $\{\rho_I\ge\frac c4\}$; on
$\Omega^+\cap\{\rho_I>\frac c2\}$, Step 3; on $\Omega_N$, Step 1. As $\chi_I = \hat\chi(\rho_I)$ vanishes for
$\rho_I\ge\frac c2$, $u_6-\chi_Iu^{(0)} = \tilde u_6+(1-\chi_I)u^{(0)}+\chi_cu_{1,6}$ on $\Omega_c$, and
$(1-\chi_I)u^{(0)}$ is supported in $\{\rho_I\ge\frac c2\cdot\frac12\}$ within $\Omega_c$, where every weight at
$\mathscr I^+$ is equivalent. So $u\in\mathcal G^k_{a_0}(\Omega^+)$, that is, $\dot g = \rho^{3/2}u+\chi\dot g_N\in
H^{k,\alpha_0,(-,\ell^\flat_I)}_{\mathrm b}$ on $\Omega^+$ (section 0), and on $\Omega^-$ by Step 1.

*The estimate.* Each step is bounded by the previous ones: Step 1 by (2.1), Step 3 by (2.2), Step 4 by (2.5), Step 5 by
Lemma 1.2's constants. The tame terms carry $\|h\|$ at most three orders above the order of the norm on the right
((2.1), (2.2), (2.5)), and the lower norms of $f$ and the data are at most of order 8; this gives (2.3). *Uniqueness.*
Two solutions differ by one with vanishing data and source; it vanishes on $\Omega_N$ by Lemma 2.2, and on $\Omega^+$ as
the forward solution with vanishing source (II.F Lemma 1.3). $\square$

The source integrates $\pi_{\mathrm C\Upsilon}u$, then $\slashed\pi_0u$, then $\pi_{11}u$, and repeats, because at $n =
3$ the radiation field of $\slashed\pi_0u$ enters $\pi_{11}u$'s equation through the $h$-dependent $\slashed A_{11}$ and
the second-order error acting on $\slashed\pi_0u$, $\pi_{11}u$ has the size of the leading part. At $n = 4$ both are in
$\tilde L_g$, gaining $x_I^{1-2\epsilon}$, and $\bar A_{76} = 0$: so all slots improve together, two rounds suffice, and
$\pi_{11}\dot g$ has no radiation field (III.C (C3)).

## 3. The nonlinear exterior solution ([Hin23a] Corollary 3.36 at n = 4, III.C$'$ Theorem 2.1)

**Theorem 3.1 (III.C$'$ Theorem 2.1, the nonlinear part).** Let $g_0$ be as in section 0 and $d := 7$. There are
$\epsilon_0>0$ and, for every $k$ and $\epsilon>0$, $\epsilon_1\in(0,\epsilon_0]$ such that for $h_0,h_1\in
H^{\infty,\ell^\flat_0}_{\mathrm b}(\Sigma_{\mathrm{IVP},r_0};S^2T^*)$ with $\|h_j\|_{H^{2d,\ell^\flat_0}_{\mathrm
b}}<\epsilon_0$ the problem
$$P(g_0+h,g_0) = 0\ \text{in }\Omega_{\mathrm{ext},r_0},\qquad h = h_0,\ \ r\mathcal L_{\partial_{t_{\mathrm{IVP}}}}h =
h_1\ \text{on }\Sigma_{\mathrm{IVP},r_0},\tag{3.1}$$
has a solution $h\in H^{\infty,\ell^\flat_0,(-,\ell^\flat_I)}_{\mathrm b}(\Omega_{\mathrm{ext},r_0})$ small in $H^{3d}$
of this class, unique among solutions small in $B^8$ (verifier 133's D-m2), and $\|h_j\|_{H^{2d+k,\ell^\flat_0}_{\mathrm
b}}<\epsilon_1$ gives $\|h\|_{H^{3d+k,\ell^\flat_0, (-,\ell^\flat_I)}_{\mathrm b}}<\epsilon$. This is III.C$'$ Theorem
2.1 with $k_0 := 2d = 14$ and $k_1 := 2d+k$.

*Proof.* Apply II.G Theorem 2.1 with $d = 7$ and:

- $B^k := H^{k,\ell^\flat_0,(-,\ell^\flat_I)}_{\mathrm b}(\Omega_{\mathrm{ext},r_0};S^2T^*)$, with the norm of (0.3)
after conjugation, and $F^k := H^{k,\ell^\flat_0+2,(-',\ell^\flat_I+1)}_{\mathrm b}(\Omega_{\mathrm{ext},r_0})\times
H^{k,\ell^\flat_0}_{\mathrm b}(\Sigma_{\mathrm{IVP},r_0})^2$, the norms made monotone in $k$ by II.G Remark 2.2.

- The support classes trivial: $B^k_\eta := B^k$, $F^\infty_\eta := F^\infty$, and $\eta_0 := 1$.

- $\Phi(h) := \big(P(g_0+h,g_0),\,h|_{\Sigma_{\mathrm{IVP},r_0}}-h_0,\,r\mathcal
L_{\partial_{t_{\mathrm{IVP}}}}h|_{\Sigma_{\mathrm{IVP},r_0}}-h_1\big)$ on $U := \{|h|_{3d}<\delta\}$.

*(i) Smoothing.* Componentwise: for the slots other than 6, and for the remainder $\tilde u_6$ and the radiation field
$u^{(0)}$ of slot 6 separately, II.G's operator $\tilde S_\theta$ on weighted b-Sobolev spaces without support
conditions (II.G section 3, Step 4, as in III.K Lemma 3.1), on $\Omega_{\mathrm{ext},r_0}$ and on $\mathscr
I^+\cap\Omega_{\mathrm{ext},r_0}$ respectively; then reassemble with $\chi_I$. The norm of $B^k$ is the sum of these
norms, so (2.1) holds; the support conditions are vacuous.

*(ii) The map.* By III.C Corollary 5.3 (with $\mathcal E_0 = \emptyset$, $\ell_0 = \ell^\flat_0$, and $\langle\mathcal
E^C_I\rangle$ at the weight $\ell^\flat_I$, which is (III.C after (3.3)) the class $(-,\ell^\flat_I)$ of $B^k$),
$P(g_0+h,g_0)\in H^{k-2,\ell^\flat_0+2,(-',\ell^\flat_I+1)}_{\mathrm b}$ for $h\in B^k$ small in $B^5$, and by (5.5)
there and III.C Proposition 5.2 it is $C^2$ in $h$, with $\Phi'(h)\dot h = (L^{g_0+h,g_0}\dot h,\dot
h|_{\Sigma},r\mathcal L_{\partial_{t_{\mathrm{IVP}}}}\dot h|_{\Sigma})$ and $\Phi''$ bilinear in two b-derivatives with
coefficients rational in $h$ and its first two b-derivatives; (2.2) and (2.3) of II.G follow from the Moser estimates
(Part IV$'$ Lemma 2.3, III.C Lemma 2.1), the loss being 2 and the low norms of order $\le5\le d$. The trace on
$\Sigma_{\mathrm{IVP},r_0}$ is bounded $B^{k+1}\to H^{k,\ell^\flat_0}_{\mathrm b}(\Sigma)$, which lies within the loss
$d$.

*(iii) Right inverses.* For $h\in U$, $\Psi(h)(f,\dot g_0,\dot g_1) := \dot g$ of Theorem 2.4 with $\alpha_0 :=
\ell^\flat_0>\ell^\flat_I$. Then $\Phi'(h)\Psi(h) = \mathrm{id}$ on $F^\infty$, and (2.3) gives II.G (2.4): $|\Psi(h)F|_k
\le C(\|F\|_{k+4}+|h|_{k+7}\|F\|_8)\le C(\|F\|_{k+d}+|h|_{k+d}\|F\|_{2d})$ for $k\ge d$, $3d\ge8$ giving the smallness of
$h$ that Theorem 2.4 asks. The support statement of (iii) is vacuous.

$\Phi(0) = (0,-h_0,-h_1)$, as $P(g_0,g_0) = 0$ (III.C Corollary 5.3's proof). So II.G Theorem 2.1 gives $h$ with
$|h|_{3d}<
\delta$ and $\Phi(h) = 0$ when $\|h_j\|_{2d}<\epsilon_{\mathrm{NM}}(\delta)$. *Higher norms.* For $k\ge0$ the shifted
scales $|v|'_j := |v|_{j+k}$, $\|f\|'_j := \|f\|_{j+k}$ satisfy (i)-(iii) with the same $d$: (2.1) and (2.4) are
invariant under the shift, and (2.3) holds on $U' := \{|h|'_{3d}<\delta\}\subset U$ with constants depending on $k$. So
data small in $H^{2d+k}$ give a solution small in $H^{3d+k}$, with any $\delta = \epsilon$; by uniqueness it is the same
$h$. *Uniqueness.* If $h,h'$ solve (3.1), small in $B^{8}$, then $\bar L(h-h') = 0$ with vanishing data, where $\bar L :=
\int_0^1L^{g_0+h'+s(h-h'),g_0}ds$. Each $L^{g_0+h_s,g_0}$ has the form (1.1) of Part IV$'$ with the same leading part,
which is $h$-free, and a remainder in the class (0.4), uniformly in $s$; so $\bar L$ has it too, and its principal part,
an average of $\frac12\Box_{g_s}$ with $g_s$ close to $g_{b_0}$, is a wave operator with the same causal structure.
Lemma 2.2 and Lemma 2.3 hold for $\bar L$ (their proofs use only these properties), and the difference vanishes.
$\square$

*Remark 3.2 (constraints).* III.C$'$ Remark 2.2 (1), the second Bianchi identity, applies to the solution of Theorem
3.1 as stated there; nothing in this part changes it.

## 4. The cut-off gauge and the backgrounds (III.C$''$ (C$''$2))

**Corollary 4.1.** Theorems 2.4 and 3.1, and Lemmas 2.2-2.3, hold with $L^{\chi_0}_{g,g_0}$ and $P^{\chi_0}$ of
III.C$''$ (2.1) in place of $L^{g,g_0}$ and $P$, for every $g_0$ of section 0.

*Proof.* $\chi_0 = 1-\check\chi_0(t_{\mathrm{IVP}}/r)$ equals 1 on $\{t_{\mathrm{IVP}}\ge\frac r4\}$ (III.C$''$
section 2). On $\Omega_c$, $\rho_I<c\le\frac12$ gives $t>(1-c)|x|+2$, so $t_{\mathrm{IVP}}\ge\frac14|x|$ for $|x|\ge
r_0$ large, which suffices (verifier 133's D-n3); so $L^{\chi_0} = L$ on $\Omega_c$, and the edge-b structure (Part
IV$'$ Proposition 1.2), Part IV$'$ Proposition 2.2 and section 2's integration, which are used only on $\Omega_c$, are
unchanged. Elsewhere only the b-structure enters (Part IV Proposition 4.1 in Lemmas 2.2-2.3), and
$L^{\chi_0}-L\in\rho_0^2\rho_I^2C^\infty
\mathrm{Diff}^1_{\mathrm b}$ (III.C$''$ Lemma 2.1's proof), a first-order term of the class those proofs absorb. In
Theorem 3.1, III.C Proposition 5.2 and Corollary 5.3 hold for $L^{\chi_0}$, $P^{\chi_0}$ by III.C$''$ Lemma 2.1, and
$P^{\chi_0}(g_0,g_0) = 0$ there. For $g_0\ne g_{b_0}$: Part IV$'$ is stated for $g_1,g_0\in\mathcal G$ (its section 0),
the hypersurfaces $\Sigma_{\mathrm{IVP},r_0}$, $\Sigma_{\mathrm{fut},r_0}$, $\Sigma_{\mathrm{past},r_0}$ are spacelike
for $g_0+h$ when $g_0-g_{b_0}$ is small as in III.C$'$ Lemma 1.1 (its proof uses only the size of $g_0+h-\eta$ in the
frame), and Lemma 1.1 (a) persists likewise. $\square$

This is what III.C$''$ (C$''$2) and III.C$'$ Remark 2.2 (2) ask of Part IV: the change of gauge lies where only robust
estimates are used, and the structure at $\mathscr I^+$ is that of the original gauge.

## 5. Findings and sources

(IV$''$1) *Two rounds, and the radiation field in slot 6 only.* At $n = 4$ the leading part of the conjugated operator
is $h$-free, every coupling into slot 6 and out of it vanishes ($\bar A_{6i} = \bar A_{j6} = 0$), and the error gains
$x_I^{1-2\epsilon}$ (0.4). So the decay is recovered in two rounds of integration of all slots at once, from a growth
weight $\gamma_0 = \beta-1+2\epsilon$, with a loss of $d = 4$ derivatives. The source's three-stage scheme and its
second improvement are not needed.

(IV$''$2) *What is not here: the continuation beyond $\Sigma_{\mathrm{fut},r_1}$.* III.K (K2) (b), as written in D300,
asked Part IV for the solution on the slab $\mathcal S_{r_1}$ between $\Sigma_{\mathrm{fut},r_1}$ and a level of
$t^\flat_*$. That slab has the
timelike side $\{r = R_8\}$, and its points near $\mathscr I^+$ at bounded $t_*$ depend on the data on all of
$\Sigma_{\mathrm{IVP}}$, not on $\Sigma_{\mathrm{fut},r_1}$ alone: the domain of dependence of
$\Sigma_{\mathrm{fut},r_1}\cap\{r\ge R_8\}$ is bounded by the outgoing cone through $\Sigma_{\mathrm{fut},r_1}\cap\{r =
R_8\}$, which stays near $\Sigma_{\mathrm{fut},r_1}$. This is verifier 132's A-m2 (ii) seen from the slab. The region
near $\mathscr I^+$ must be posed after the compact part, from the spacelike surface $\{\rho_I = c\}$ (Lemma 1.1 (a)),
whose past within $\{t_*\le T\}$ is compact away from the exterior domain; and verifier 132's A-M3 moved III.K's levels
from $t^\flat_*$ to $t_*$, verifier 133's B-M1 back (D309). III.K poses the slab $\mathcal S$ to the future of
$\{\rho'_I = c\}\cup\Sigma_{\mathrm{fut},r_1}$, $\rho'_I$ being $\rho_I$ in the chart translated in $t$, up to
$\{t^\flat_* = \hat T+3\}$, after the compact part. The continuation there is Part IV$'''$. On that slab the
$X_I$-curves backward need not reach $\{\rho_I = c\}$ before $\Sigma_{\mathrm{fut},r_1}$ (verifier 133's D-m3), so Part
IV$'''$ poses the problem on the exterior domain together with the slab, where its Lemma 1.1 proves that they reach
$\{\rho'_I = c_1\}$, and Part IV$'$ applies near the interior of $\mathscr I^+$ after the chart (1.2) of III.C is
translated in $t$ ($g_{b_0}$ is stationary).

(IV$''$3) *The Cauchy problem near $I_0$.* Part IV's Proposition 4.1 is stated with vanishing data and with the initial
surface a level set of $\tau$. Lemma 2.2 adds the data (the flux through $\Sigma_{\mathrm{IVP}}$, tangential commutation,
normal derivatives from the equation), uses $\tau' = t_{\mathrm{IVP}}/|x|$, and solves backward on the past slab, which
is verifier 132's B-m3.

*Labels.* Lemma 1.2 is the source's use of [HV20, Lemma 7.7 (1)] and of the integration of $\rho_I\partial_{\rho_I}-A$;
Theorem 2.4 is its Theorem 3.35 with data, for [Hin26]'s operator (III.C$'$ (2.2), (5.52)); Theorem 3.1 is its Corollary
3.36 and [Hin26] Theorem 5.17's nonlinear part; Corollary 4.1 is [Hin26]'s remark that the cut-off plays no role in its
Theorems 5.17 and 5.21.

*Sources.* [Hin23a] pp. 30-32 (section 3.6: (3.59a)-(3.59b), Theorem 3.35 with (3.60)-(3.64), Corollary 3.36, Remark
3.37), read at source. Inputs: Part IV sections 0, 3-4 (Propositions 3.1, 4.1, Remark 4.2); Part IV$'$ (0.2), (1.1),
Proposition 1.2, Remark 1.3, Proposition 2.2, Lemma 2.3; III.B Lemma 3.7; III.C (1.3), (4.3), Lemmas 1.3, 2.1, 4.2,
Definitions 3.4, 5.1, Propositions 4.4, 5.2, Corollary 5.3; III.C$'$ (1.1), Lemma 1.1, Theorem 2.1, Remark 2.2; III.C$''$
section 2, Lemma 2.1, (C$''$2); III.F section 1; II.F Lemma 1.3; II.G Theorem 2.1, Remark 2.2, section 3.
