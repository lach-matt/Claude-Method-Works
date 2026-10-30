# Part IV$'''$. Exterior estimates IV: the slab near null infinity, n = 4 (III.K (K2) (b))

*Status.* Written (D306). This part delivers the continuation that III.K (K2) (b) asks of Part IV: the solution on
the slab $\mathcal S$ of III.K Proposition 1.2's proof (as re-posed in D304), near the interior of $\mathscr I^+$ up to
$\{t_* = \hat T+3\}$, with its orders at $\mathscr I^+$. The slab's past boundary contains the part of
$\Sigma_{\mathrm{fut},r_1}$ near $\mathscr I^+$, which reaches $\mathscr I^+$ and is asymptotically null there; Cauchy
data on it are avoided. The solution is instead posed on $\Omega^\natural := \Omega_{\mathrm{ext},r_1}\cup\mathcal S$,
from $\Sigma_{\mathrm{IVP},r_1}$ and from the compact surface $\Sigma_c$ where $\mathcal S$ meets the compact part
$\mathcal K$, neither of which reaches $\mathscr I^+$. Part IV$''$'s argument then applies on $\Omega^\natural$, in
III.C's chart translated in $t$ (which $g_{b_0}$ allows, being stationary), and its solution restricts to the exterior
solution on $\Omega_{\mathrm{ext},r_1}$. The source covers the slab in one sentence ([Hin26] p. 321, quoted in III.K
(K2)). No source text beyond Part IV$''$'s is used.

## 0. Setting

$\hat T = 2/C'$, $T'' = \hat T+5$, $r_1 = 2r_0$, $R_8\ge\max(2r_1,8)$, $c$, the region $\mathcal D$, the compact part
$\mathcal K$, the slab $\mathcal S := \mathcal D\cap\{\rho'_I<c\}\setminus\Omega_{\mathrm{ext},r_1}$ and $\rho'_I :=
(T''-x^1)/|x|$ are those of III.K section 0 and Proposition 1.2's proof. Put
$$\rho'_0 := (T''-x^1)^{-1},\qquad x'_I := (\rho'_I)^{1/2},\qquad U'' := \mathrm{cl}_M\{t_*\le T_0+T''-2\}\cap\{|x|\ge
4R_1\},$$
III.C's (1.2)-(1.3) with $2$ replaced by $T''$: on $U''$, $x^1\le T''-1$ (as in III.C after (1.3)), so $\rho'_0\le1$, and
$(\rho'_0,\rho'_I,\omega)$ are coordinates near $I_0\cup\mathscr I^+$. On $U$ the ratios $\rho'_0/\rho_0 = (2-x^1)/(T''-
x^1)$ and $\rho'_I/\rho_I$ are smooth and positive up to $I_0$ and $\mathscr I^+$, tending to 1 at $I_0$; so the
weighted b- and edge-b spaces of the two charts coincide on $U$, with equivalent norms (the fibration of $\mathscr I^+$
by $\omega$ is the same). Let
$$\Sigma_c := \{\rho'_I = c\}\cap\partial\mathcal S,\qquad\Omega^\natural := \Omega_{\mathrm{ext},r_1}\cup\mathcal S.$$
$\Sigma_c$ is compact: on it $x^1\ge C''-r_1-2$ (III.K Proposition 1.2's proof), so $|x|\le(T''+r_1+2-C'')/c$. $\mathcal
G''$ denotes the class of III.C Definition 3.4 on $U''$ in the coordinates $(\rho'_0,\rho'_I)$.

*Translation.* $t\mapsto t-(T''-2)$ is an isometry of $g_{b_0}$ ($g_{b_0}$ is stationary in III.B's coordinates) and of
$\eta$, and it maps III.C's coordinates (1.2) and frame (1.6) to those above. III.C sections 1 and 4 (Lemmas 1.1, 1.3,
4.1-4.3, Proposition 4.4), Part IV, Part IV$'$ and Part IV$''$ sections 0-2 use the chart only through $\eta$'s form in
it and through the bounds of III.C Lemma 1.3 for $g_{b_0}-\eta$, which are invariant under this map; so they hold on
$U''$ in the translated chart, for $g_1,g_0\in\mathcal G''$, with the same proofs.

**Lemma 0.1 (the background on the slab).** Let $S\in\mathcal S_1$ be small as in III.B Lemma 5.2. On a neighbourhood of
$\bar{\mathcal S}$ in $U''$, $\phi_S^*g_{b_0}$ agrees with an element of $\mathcal G''$; on $\Omega_{\mathrm{ext},r_1}$
it is III.C$''$'s background.

*Proof.* On $\mathcal S$, $\chi_{\mathrm{IVP}} = 1$, as $t_{\mathrm{IVP}}\ge0>-|x|/10$ (III.B section 5), and $\chi_K =
0$, as $\mathrm{supp}\,\chi_K\subset\{|x|<t/2\}$ (III.B section 5: $\mathrm{supp}\,\chi_K$ lies in the interior of
$\{\chi^\sharp_K = 1\}\subset\mathrm{supp}\,\chi^\sharp_K\subset\{|x|<t/2\}$), while on $\mathcal S$, $t_*\le\hat T+3$
gives $x^1\le T''-1$, so $t\le|x|+T''<2|x|$ near infinity; and $\mathcal S$ lies near infinity. So III.B Lemma 5.2's
(5.3) holds near $\bar{\mathcal S}$:
$$\phi_S^*g_{b_0}-g_{b_0}-|x|^{-2}h_S(\omega)(dx^1)^2\in\rho_0^2\rho_I^3\rho_+^2C^\infty(M;S^2T^*),$$
and $g_{b_0}-\eta = \mu_0|x|^{-2}(dx^1)^2+|x|^{-3}C^\infty$ on $\{|x|\ge3R_1\}$ (III.C Lemma 3.5 (1)'s proof). On
$\mathcal S$, $\rho_0$, $\rho'_0$ and $\rho_+$ are bounded below and $\rho_I/\rho'_I$ is smooth and positive, so
$\phi_S^*g_{b_0}-\eta\in(\rho'_0)^2(\rho'_I)^2C^\infty$ with only the slot $\pi_{11}$ at that order, $(dx^1)^2$ being of
type $\pi_{11}$, and the other slots in $(\rho'_0)^2(\rho'_I)^3C^\infty$: this is III.C (3.4) in the translated chart,
and $\phi_S^*g_{b_0}$ is smooth on $M$. On $\Omega_{\mathrm{ext},r_1}$ the statement is III.C$''$'s (its section 3).
$\square$

## 1. The curves on $\Omega^\natural$

**Lemma 1.1.** Let $c_1\in(0,\frac c4]$ and $r_0$ large. (a) $\{\rho'_I = c_1\} = \{t = (1-c_1)|x|+T''\}$ is spacelike
near infinity, with $\{\rho'_I<c_1\}$ to its future. (b) For $p\in\Omega^\natural$ with $\rho'_I(p)<c_1$, the integral
curves of $X'_I := \rho'_I\partial_{\rho'_I}$ and of $X'_0-X'_I$ through $p$ (the outgoing ray at fixed $x^1$, and the
curve of fixed $|x|$), followed in the direction of increasing $\rho'_I$, stay in $\Omega^\natural$ until they reach
$\{\rho'_I = c_1\}$, which they do. (c) $\Omega^\natural\cap\{\rho'_I<c_1\}$ does not meet $\mathcal K$, and $\Sigma_c$
lies in $\{\rho'_I = c\}$.

*Proof.* (a) is Part IV$''$ Lemma 1.1 (a) in the translated chart. (b) Near infinity, $\Omega^\natural\cap\{\rho'_I<c\}$
is the set $\{\rho'_I<c,\ t_{\mathrm{IVP}}\ge0,\ t_*\le\hat T+3\}$: below $\Sigma_{\mathrm{fut},r_1}$ it is
$\Omega_{\mathrm{ext},r_1}$, above it $\mathcal S$. So it suffices that along the segment $\rho'_I$ stays below $c$ and
$t_{\mathrm{IVP}}\ge0$ and $t_*\le\hat T+3$ persist. *The ray.* Along it $x^1 = x^1_p$, and $|x|$ decreases to $r_c :=
(T''-x^1_p)/c_1$, where $\rho'_I = c_1<c$. $t_* = x^1+C'-8\mu_0|x|^{-1}$ decreases along it. $t_{\mathrm{IVP}} =
x^1+|x|-C''$ decreases too, and at $r_c$ it is $x^1_p(1-c_1^{-1})+T''c_1^{-1}-C''$, which is
$\ge|x^1_p|(c_1^{-1}-1)+T''c_1^{-1}-C''>0$ if $x^1_p<0$, and $\ge T''-1+c_1^{-1}-C''>0$ if $x^1_p\in[0,T''-1]$, for
$c_1$ small; and $r_c\ge r_0$. *The curve of fixed $|x|$.* $t$ decreases to $t_c := (1-c_1)|x|+T''$; $t_*$ decreases; it
may cross $\Sigma_{\mathrm{fut},r_1}$ into $\Omega_{\mathrm{ext},r_1}$; $t_{\mathrm{IVP}}(t_c)\ge\frac12|x|+T''-C''>0$;
and $\rho'_I<c_1$ along it, so it avoids $\mathcal K$. (c) is the definition of $\mathcal S$ and $\mathcal
K\subset\mathcal D\setminus\mathcal S$. $\square$

So Part IV$''$ Lemma 1.2 holds on $\Omega^\natural_{c_1} := \Omega^\natural\cap\{\rho'_I<c_1\}$, in the translated chart,
with the same proof.

## 2. The solution on $\Omega^\natural$

**Theorem 2.1 (the linear estimate on $\Omega^\natural$).** Let $g_0 := \phi_S^*g_{b_0}$ with $|S|$ small, or $g_0 :=
g_{b_0}$; $h$ small in $H^{8,\ell^\flat_0,(-,\ell^\flat_I)}_{\mathrm b}(\Omega^\natural)$ (weights at $\mathscr I^+$ in
$\rho'_I$); $L := L^{\chi^\natural_0}_{g_0+h,g_0}$ (III.K Lemma 1.1, $P^\natural$'s linearisation);
$\alpha_0>\ell^\flat_I$, $k\in\mathbb N_0$, $d = 4$. For $f\in H^{k+d,\alpha_0+2,(-',\ell^\flat_I+1)}_{\mathrm
b}(\Omega^\natural)$, data $\dot g_0,\dot g_1\in H^{k+d,\alpha_0}_{\mathrm b}(\Sigma_{\mathrm{IVP},r_1})$ and data $\dot
k_0,\dot k_1\in H^{k+d}(\Sigma_c)$, there is a unique $\dot g\in H^{k,\alpha_0,(-,\ell^\flat_I)}_{\mathrm
b}(\Omega^\natural)$ with $L\dot g = f$ and these data, and Part IV$''$ (2.3) holds with $\|\dot k_0\|_{H^{k+d}}+\|\dot
k_1\|_{H^{k+d}}$ added to $N(f,\dot g_0,\dot g_1;k+d)$ and their $H^8$-norms to $N(\cdot;8)$.

*Proof.* As Part IV$''$ Theorem 2.4, with three changes. *The gauge.* On $\Omega_{\mathrm{ext},r_1}$,
$\chi^\natural_0 = \chi_0$ (III.K Lemma 1.1 (c)); on $\mathcal S$, $\chi^\natural_0 = 1$ (III.K Proposition 1.2's
proof); so $L = L^{\chi_0}$ on $\Omega^\natural$, and Part IV$''$ Corollary 4.1 applies, $\chi_0 = 1$ on
$\Omega^\natural_{c_1}$ ($\rho'_I<c_1$ gives $t_{\mathrm{IVP}}\ge\frac r4$). *The background.* $g_0\in\mathcal G''$ near
$\bar{\mathcal S}$ by Lemma 0.1, and in III.C$''$'s class on $\Omega_{\mathrm{ext},r_1}$; it is Ricci flat. *The
regions.* Fix $c_1\le\frac c4$ so small that Part IV$'$ Proposition 2.2 holds on $\Omega^\natural_{c_1}$ with
$\Sigma_{\mathrm{in}} := \{\rho'_I = c_1\}\cap\Omega^\natural$, $\Sigma_{\mathrm{fin}} := \{t_* = \hat T+3\}\cap
\Omega^\natural_{c_1}$, spacelike as $t_*$ is a time function (III.B Lemma 3.7 (a)); every $X'_I$-curve there begins on
$\Sigma_{\mathrm{in}}$ (Lemma 1.1 (b)). Then:

(i) On $\Omega_N$ (near the interior of $I_0$, with the past slab) Part IV$''$ Lemma 2.2 with the data on
$\Sigma_{\mathrm{IVP},r_1}$, unchanged.

(ii) On $\Omega^\natural\cap\{\rho'_I\ge\frac{c_1}4\}\cap\{\tau'\ge\frac1{16}\}$, away from $\mathscr I^+$: its part in
$\Omega_{\mathrm{ext},r_1}$ by Part IV$''$ Lemma 2.3's first step (Part IV Proposition 4.1 for the system, near the
interior of $I_0$; standard energy estimates on the compact part with $|x|\le R$); then its part in $\mathcal S$, which
is compact ($|x|\le4(T''-x^1)/c_1$, $x^1$ bounded), by the standard energy estimate for the Cauchy problem of a linear
wave equation on a compact domain of dependence, with data on $\Sigma_c$ (given) and on $\Sigma_{\mathrm{fut},r_1}\cap
\{\frac{c_1}4\le\rho'_I<c\}$ (from the part in $\Omega_{\mathrm{ext},r_1}$), both spacelike and compact. Its boundary to
the future, $\{\rho'_I = \frac{c_1}4\}$, $\{t_* = \hat T+3\}$ and $\Sigma_{\mathrm{fut},r_1}\cap\{\rho'_I\ge c\}$ (where
$\Omega^\natural$ borders $\mathcal K$), is spacelike, so the region is closed under past causal curves within
$\Omega^\natural$ (II.F Lemma 1.3 for uniqueness).

(iii) On $\Omega^\natural_{c_1}$, Part IV$''$ Lemma 2.3's second step and Theorem 2.4's Steps 4-6, with $c_1$ for $c$:
the cut-off $\hat\chi_{c_1}(\rho'_I)$, Part IV$'$ Proposition 2.2, and the two rounds of integration by Lemma 1.2 along
the curves of Lemma 1.1. Nothing in these steps uses $\rho'_0$ beyond its role as a coordinate; on $\mathcal S$ it is
bounded below, where the weight at $I_0$ is immaterial.

The forcing of each step vanishes near its initial surface after the cut-offs of Part IV$''$ Theorem 2.4's Step 2 and
Lemma 2.3, and the estimates compose as there; the data on $\Sigma_c$ enter through (ii) only, at the order of
$H^{k+4}$. Uniqueness: II.F Lemma 1.3 on each region. $\square$

**Theorem 2.2 (the nonlinear solution on $\Omega^\natural$; III.K (K2) (b)).** Let $g_0$ be as in Theorem 2.1,
$(h_0,h_1)$ data on $\Sigma_{\mathrm{IVP},r_1}$ as in Part IV$''$ Theorem 3.1, and $(k_0,k_1)$ the Cauchy data on
$\Sigma_c$ of a solution of $P^\natural(g_0+h,g_0) = 0$ on a neighbourhood of $\Sigma_c$ in $\mathcal
K\cup\Omega_{\mathrm{ext},r_1}$ that agrees on $\Omega_{\mathrm{ext},r_1}$ with Part IV$''$ Theorem 3.1's solution. If
$\|h_j\|_{H^{2d,\ell^\flat_0}_{\mathrm b}}+\|k_j\|_{H^{2d}(\Sigma_c)}<\epsilon_0$, there is a unique $h\in
H^{\infty,\ell^\flat_0,(-,\ell^\flat_I)}_{\mathrm b} (\Omega^\natural)$, small in $H^{3d}$, with $P^\natural(g_0+h,g_0)
= 0$ and these data; it equals Part IV$''$ Theorem 3.1's solution on $\Omega_{\mathrm{ext},r_1}$, and the higher norms
are bounded as there.

*Proof.* Part IV$''$ Theorem 3.1's proof on $\Omega^\natural$, with $F^k$ enlarged by $H^k(\Sigma_c)^2$ and $\Phi$ by the
traces on $\Sigma_c$ minus $(k_0,k_1)$; the right inverses are Theorem 2.1's, the smoothing and the map are as there
($P^\natural = P^{\chi_0}$ on $\Omega^\natural$, and III.C Corollary 5.3 holds for it by III.C$''$ Lemma 2.1, near
$\mathcal S$ in the translated chart). On $\Omega_{\mathrm{ext},r_1}$, which is closed under past causal curves within
$\Omega^\natural$ and whose past boundary is $\Sigma_{\mathrm{IVP},r_1}\cup\Sigma_{\mathrm{past},r_1}$, the solution
depends on $(h_0,h_1)$ only, so it is Part IV$''$ Theorem 3.1's by uniqueness there. $\square$

So the solution of III.K Proposition 1.2 on $\mathcal S$ is the restriction of Theorem 2.2's, with $(k_0,k_1)$ from the
compact part (whose data on $\Sigma_{\mathrm{fut},r_1}\cap\{\rho'_I\ge c\}$ come from the exterior), and the three
solutions agree on overlaps by II.F Lemma 1.3.

**Corollary 2.3 (the orders on the slab).** Under the hypotheses of III.C$'$ Theorem 3.1 on the data, the solution of
Theorem 2.2 lies in $H^{\infty,(\mathcal E_0,\ell_0),\langle\mathcal E^C_I\rangle,\ell_I}_{\mathrm b}(\Omega^\natural)$,
with the bound (3.2) there; in particular $h_S$ has the orders $(\langle\mathcal E^C_I\rangle,\ell_I)$ at $\mathscr I^+$
on $\mathcal S$, as III.K Proposition 1.2 (3) states.

*Proof.* III.C$'$ Theorem 3.1's proof on $\Omega^\natural$, with Theorem 2.1 in place of III.C$'$ (2.2). Its Step 1 works
at $I_0$, which $\Omega^\natural$ meets only within $\Omega_{\mathrm{ext},r_1}$; its Step 2 integrates, slot by slot,
along $X_I$ and $X_0-X_I$ near $\mathscr I^+$ (III.A Lemmas 1.2 and 3.2), and on $\Omega^\natural_{c_1}$ the curves
followed backward reach $\{\rho'_I = c_1\}$, where the solution is smooth (Lemma 1.1 (b)); away from $\mathscr I^+$ there
is nothing to show. The structure (4.4) of III.C used there holds near $\mathcal S$ by Lemma 0.1 and the translation.
$\square$

## 3. Findings and sources

(IV$'''$1) *The slab is posed with the exterior.* Cauchy data on $\Sigma_{\mathrm{fut},r_1}$ near $\mathscr I^+$ would
sit on a surface that reaches $\mathscr I^+$ and is asymptotically null there, where neither Part IV's estimates (whose
initial surfaces do not reach $\mathscr I^+$) nor a non-characteristic Cauchy problem in the edge-b sense is available.
Solving on $\Omega^\natural$ from $\Sigma_{\mathrm{IVP},r_1}\cup\Sigma_c$ avoids this; the exterior solution is
recovered by uniqueness.

(IV$'''$2) *The chart.* III.C's chart (1.2) has $x^1\le1$ on $U$ by the choice of $T_0$ (III.C after (1.3)); the slab
reaches $x^1$ up to $\hat T+3-C'$, so the chart is translated in $t$, which the stationarity of $g_{b_0}$ permits, and
the background $\phi_S^*g_{b_0}$ is checked in the translated class by III.B Lemma 5.2 directly (Lemma 0.1).

*Labels.* Theorem 2.2 is the source's sentence on p. 321 of [Hin26] ("for globally small initial data, $h_S$ thus
exists ... on $\phi_S(\{t_{\mathrm{IVP}}\ge0\})\cap\{t_*\le2\}$", quoted in III.K (K2)), for the part near $\mathscr
I^+$.

*Sources.* Inputs: Part IV$''$ (all of it); Part IV$'$ Proposition 2.2; Part IV Proposition 4.1; III.B section 5 (Lemma
5.2, the cut-offs), Lemma 3.7; III.C (1.2)-(1.3), (3.4), Definition 3.4, Lemma 3.5, Lemma 1.3, Proposition 4.4, Corollary
5.3; III.C$'$ Theorem 3.1; III.C$''$ section 3, Lemma 2.1; III.K section 0, Lemma 1.1, Proposition 1.2 and its proof;
II.F Lemma 1.3.
