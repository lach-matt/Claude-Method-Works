# Part III.C$''$. Boosted backgrounds and gauged Cauchy data, n = 4 ([Hin26] sections 5.6-5.7)

*Status.* Written (D289). This part proves, at spatial dimension $n = 4$, [Hin26] Theorem 5.23 with the cut-off gauge
(5.76), Remark 5.24, Proposition 5.25, and the statements of section 5.7.1, Remark 5.26 and Example 5.27 (pp. 108-113).
It settles finding (C4) of III.C. Like III.C$'$, it rests on Part IV for the exterior solution (III.C$'$ Theorem 2.1),
here in the cut-off gauge (finding (C$''$2)).

*What n = 4 changes.* (1) *The boosts are genuine on the whole exterior domain.* III.C (C4) found that where
$\chi_{\mathrm{IVP}}<1$ near $I_0$ the cut-off boost changes $\eta$ at $O(1)$. III.C$'$ Lemma 1.1 takes the past slab of
$\Omega_{\mathrm{ext},r_0}$ with the slope $\frac1{12}$ instead of the source's $\frac14$, so
$\Omega_{\mathrm{ext},r_0}\subset\{t_{\mathrm{IVP}}>-|x|/10\}\subset\{\chi_{\mathrm{IVP}} = 1\}$, and there
$\phi_S^*g_{b_0}$ lies in the background class $\mathcal G$ of III.C (Lemma 1.1). (2) *A misprint.* The source asks
$\phi_S(\Sigma_{\mathrm{IVP}})\subset\{\chi_0 = 1\}$ where its argument needs $\{\chi_0 = 0\}$ (finding (C$''$1)). (3)
*No logarithms from the time function.* At $n = 3$ the source's $t$ differs from Boyer-Lindquist time by $O(\log r)$,
which gives the Cauchy data on $\Sigma_{\mathrm{IVP}}$ the extra index set $\mathcal E_{\log}$ ((5.83b), Remark 5.26).
At $n = 4$ the Kerr-Schild time of III.B differs from Boyer-Lindquist time by $O(r^{-1})$, smooth in $r^{-1}$, and no
logarithm arises (Proposition 4.2).

Notation as in III.C and III.C$'$; $\phi_S$, $S\in\mathcal S_1$, is III.B's cut-off boost (III.B section 5, Lemma 5.2),
and $\chi_{\mathrm{IVP}}$, $\chi_K$ its cut-offs. The gauge 1-form $\Upsilon^0(g,g_0) :=
\mathrm{tr}_g(\nabla^g-\nabla^{g_0})$ and $E^\Upsilon_{g_0}$ are those of III.B section 6 (the source's (4.3)-(4.4) and
Definition 4.1).

## 1. The boosted background

**Lemma 1.1 (the boosted Myers-Perry metric on the exterior domain; [Hin26] section 5.6, first paragraph, at n = 4).**
There is $\epsilon_1>0$ such that for $S\in\mathcal S_1$ with $|S|<\epsilon_1$ and $r_1\ge R_0+1$ (III.C$'$ Lemma 1.1):
$\phi_S^*g_{b_0}$ agrees on $\Omega_{\mathrm{ext},r_1}$ with an element of $\mathcal G$ (III.C Definition 3.4), it is
Ricci flat, and $\phi_S^*g_{b_0}-g_{b_0}$ is small in the sense of III.C$'$ Lemma 1.1. Hence III.C$'$ Theorems 2.1 and
3.1 hold with $g_{b_0}$ replaced by $g_0 = \phi_S^*g_{b_0}$ (III.C$'$ Remark 2.2 (2)).

*Proof.* On $\Omega_{\mathrm{ext},r_1}$, $t_{\mathrm{IVP}}\ge-\frac{r-r_1}{12}>-\frac{|x|}{10}$, so $\chi_{\mathrm{IVP}}
= 1$ there (III.B section 5); and $t_{\mathrm{IVP}}\le r+2r^{1-\ell^\flat_I}$ there, so $t\le|x|+C$ and $\chi_K = 0$, as
$\mathrm{supp}\,\chi_K\subset\{|x|<t/2\}$. So $\Omega_{\mathrm{ext},r_1}\subset\{\chi_{\mathrm{IVP}}(1-\chi_K) = 1\}$,
and III.C Lemma 3.5 (2) gives $\phi_S^*g_{b_0}-g_{b_0} = |x|^{-2}h_S(\omega)(dx^1)^2+\rho_0^2\rho_I^3C^\infty$ there for
$|S|$ small (III.B Lemma 5.2), with $h_S$ smooth and $O(|S|)$. The first term has only the 11-slot and lies in
$\rho_0^2\rho_I^2C^\infty$, and $g_{b_0}\in\mathcal G$ (III.C Lemma 3.5 (1)); so $\phi_S^*g_{b_0}$ satisfies (3.4) of
III.C on $\Omega_{\mathrm{ext},r_1}$. $\mathrm{Ric}(\phi_S^*g_{b_0}) = \phi_S^*\mathrm{Ric}(g_{b_0}) = 0$. The
difference is $O(|S|)$ in every $C^k$ norm of III.C$'$ Lemma 1.1's bounds, so the hypersurfaces of
$\Omega_{\mathrm{ext},r_1}$ stay spacelike for $|S|$ small. $\square$

This settles III.C (C4): the boost need only be genuine where the exterior problem is posed, and the slope $\frac1{12}$
arranges it. The region where $\chi_{\mathrm{IVP}}<1$ lies below $\Sigma_{\mathrm{past},r_1}$ and plays no part.

## 2. The cut-off gauge ([Hin26] (5.75)-(5.76) at n = 4)

Fix $\check\chi_0\in C^\infty_c((-\frac14,\frac14))$ equal to 1 on $[-\frac18,\frac18]$ (the source prints
$[-\frac18,-\frac18]$), and $\chi_0 := 1-\check\chi_0(t_{\mathrm{IVP}}/r)$, extended by 1 where $r$ is small relative to
$t_{\mathrm{IVP}}$. Near $I_0$ and $\mathscr I^+$, $t_{\mathrm{IVP}}/r$ is a smooth function on $M$ ($\tau = t/|x|$ near
the interior of $I_0$, III.C Lemma 1.1), so $\chi_0\in C^\infty(M)$. It equals 0 on $\{|t_{\mathrm{IVP}}|\le
r/8\}\supset\Omega_{\mathrm{ext},r_0}\cap\{t_{\mathrm{IVP}}\le0\}$ and near $\Sigma_{\mathrm{IVP}}$, and 1 on
$\{t_{\mathrm{IVP}}\ge r/4\}$, a neighbourhood of $\mathscr I^+\cap\Omega_{\mathrm{ext}}$ (there
$t_{\mathrm{IVP}}/r\to1$). Let
$$\Upsilon^{\chi_0E_\Upsilon}(g,g_0) := \Upsilon^0(g,g_0)-\chi_0E^\Upsilon_{g_0}G_{g_0}(g-g_0),\qquad P^{\chi_0}(g,g_0)
:= \mathrm{Ric}(g)-\delta^*_{g_0,E_C}\Upsilon^{\chi_0E_\Upsilon}(g,g_0),\tag{2.1}$$
and $L^{\chi_0}_{g,g_0}$ the linearisation of $P^{\chi_0}$ in $g$. $\Upsilon^0$ is natural: for a diffeomorphism $\phi$,
$$\phi^*\Upsilon^0(g,g_0) = \Upsilon^0(\phi^*g,\phi^*g_0),\tag{2.2}$$
the source's (5.75), in any dimension, since $\nabla^{\phi^*g} = \phi^*\nabla^g$ and the trace is natural. The term
$E^\Upsilon_{g_0}G_{g_0}(g-g_0)$ is not natural in this sense when $E^\Upsilon$ is stationary relative to $g_{b_0}$;
this is why the cut-off is introduced.

**Lemma 2.1 (the structure in the cut-off gauge).** For $g_0\in\mathcal G$, III.C Proposition 4.4, Proposition 5.2 and
Corollary 5.3 hold for $L^{\chi_0}$ and $P^{\chi_0}$ in place of $L$ and $P$.

*Proof.* $L^{\chi_0}_{g,g_0}-L_{g,g_0} = \delta^*_{g_0,E_C}\big((1-\chi_0)E^\Upsilon_{g_0}G_{g_0}(\cdot)\big)$, as
$E^\Upsilon_{g_0}G_{g_0}(g-g_0)$ is linear in $g-g_0$. Its coefficients are those of the $E^\Upsilon$-term of III.C
(4.1), which lie in $\rho_0^2C^\infty\mathrm{Diff}^1_{\mathrm b}$ near $I_0$ (III.F section 1: $E^\Upsilon_{g_0}$ is
homogeneous of degree $-1$ and $\delta^*$ of degree $-1$ in $|x|$), times $1-\chi_0$, which is supported in
$\{|t_{\mathrm{IVP}}|<r/4\}$, a set on which $\rho_I$ is bounded below. So the difference lies in
$\rho_0^2\rho_I^2C^\infty\mathrm{Diff}^1_{\mathrm b}$, the error class of III.C (4.4), and the leading part at $\mathscr
I^+$ is unchanged ($\chi_0 = 1$ there). The proofs of Proposition 5.2 and Corollary 5.3 use only (4.4) and
$P^{\chi_0}(g_0,g_0) = 0$, which holds as $G_{g_0}(g_0-g_0) = 0$. $\square$

## 3. Stability with boosted background and data ([Hin26] Theorem 5.23 at n = 4)

For $h$ on $\Omega_{\mathrm{ext},r_0}$ and $r_1 := r_0+1$, put
$$h_{S,0} := (\phi_S^*h)|_{\Sigma_{\mathrm{IVP},r_1}},\qquad h_{S,1} := r\mathcal
L_{\partial_{t_{\mathrm{IVP}}}}(\phi_S^*h)|_{\Sigma_{\mathrm{IVP},r_1}},\tag{3.1}$$
defined for $|S|$ small, as $\phi_S$ maps a neighbourhood of $\Sigma_{\mathrm{IVP},r_1}$ into
$\Omega_{\mathrm{ext},r_0}$ ($\phi_S$ is the time-1 flow of a b-vector field, close to the identity in $C^\infty$ on
compact sets and near $I_0$).

**Theorem 3.1 ([Hin26] Theorem 5.23 at n = 4).** Let $h_0,h_1$ be small data as in III.C$'$ Theorem 3.1, and let $h\in
H^{\infty,(\mathcal E_0,\ell_0),\langle\mathcal E^C_I\rangle,\ell_I}_{\mathrm b}(\Omega_{\mathrm{ext},r_0})$ solve
$$P^{\chi_0}(g_{b_0}+h,g_{b_0}) = 0,\qquad h|_{\Sigma_{\mathrm{IVP},r_0}} = h_0,\quad r\mathcal
L_{\partial_{t_{\mathrm{IVP}}}}h|_{\Sigma_{\mathrm{IVP},r_0}} = h_1\tag{3.2}$$
(III.C$'$ Theorems 2.1 and 3.1 in the cut-off gauge, Lemma 2.1, finding (C$''$2)). For $S\in\mathcal S_1$ small,
depending only on $b_0$, $\ell^\flat_0$ and $\ell^\flat_I$, let $h_S\in H^{\infty,(\mathcal E_0,\ell_0),\langle\mathcal
E^C_I\rangle,\ell_I}_{\mathrm b}(\Omega_{\mathrm{ext},r_1})$ solve
$$P^{\chi_0}(\phi_S^*g_{b_0}+h_S,\phi_S^*g_{b_0}) = 0\ \text{in }\Omega_{\mathrm{ext},r_1},\qquad h_S = h_{S,0},\ \
r\mathcal L_{\partial_{t_{\mathrm{IVP}}}}h_S = h_{S,1}\ \text{on }\Sigma_{\mathrm{IVP},r_1}\tag{3.3}$$
(Lemma 1.1). Then:

(1) $h_S = \phi_S^*h$ near $\Sigma_{\mathrm{IVP},r_1}$, and $h_0 = h$ on $\Omega_{\mathrm{ext},r_1}$;

(2) $h_S$ depends smoothly on $S$, in the sense of the source's footnote 59: $C^l$ in $S$ with values in $H^{k,(\mathcal
E_0,\ell_0),\langle\mathcal E^C_I\rangle,\ell_I}_{\mathrm b}$ for data of regularity depending on $k$ and $l$;

(3) if $h_0,h_1$ induce data satisfying the constraint equations and $\Upsilon^0(g_{b_0}+h,g_{b_0}) = 0$ at
$\Sigma_{\mathrm{IVP},r_0}$, then $\mathrm{Ric}(\phi_S^*g_{b_0}+h_S) = 0$ and
$\Upsilon^{\chi_0E_\Upsilon}(\phi_S^*g_{b_0}+h_S,\phi_S^*g_{b_0}) = 0$.

*Proof.* (1) Take $|S|$ so small that $\phi_S$ maps a neighbourhood $\mathcal U$ of $\Sigma_{\mathrm{IVP},r_1}$ into
$\{|t_{\mathrm{IVP}}|<r/8\}\cap\Omega_{\mathrm{ext},r_0}$, where $\chi_0 = 0$. There $P^{\chi_0}(g_{b_0}+h,g_{b_0}) =
\mathrm{Ric}(g_{b_0}+h)-\delta^*_{g_{b_0},E_C}\Upsilon^0(g_{b_0}+h,g_{b_0}) = 0$. Pull back by $\phi_S$: by (2.2), and
$\phi_S^*\delta^*_{g,E_C} = \delta^*_{\phi_S^*g,\phi_S^*E_C}$ with $E_C$ built from $g_0$ and its derivatives naturally
(III.B section 6),
$$\mathrm{Ric}(\phi_S^*g_{b_0}+\phi_S^*h)-
\delta^*_{\phi_S^*g_{b_0},E_C}\Upsilon^0(\phi_S^*g_{b_0}+\phi_S^*h,\phi_S^*g_{b_0}) = 0$$
on $\mathcal U$, where also $\chi_0 = 0$; so $\phi_S^*h$ solves (3.3) on $\mathcal U$ with the data (3.1). By uniqueness
for the quasilinear wave equation (III.C$'$ Theorem 2.1, and finite speed of propagation), $h_S = \phi_S^*h$ on the
domain of dependence of $\Sigma_{\mathrm{IVP},r_1}$ inside $\mathcal U$. For $S = 0$, $\phi_0 = \mathrm{id}$ and (3.3)
is (3.2) on $\Omega_{\mathrm{ext},r_1}\subset\Omega_{\mathrm{ext},r_0}$. The data (3.1) lie in $H^{\infty,(\mathcal
E_0,\ell_0)}_{\mathrm b}(\Sigma_{\mathrm{IVP},r_1})$: $h$ is of that class near $\Sigma_{\mathrm{IVP},r_1}$ away from
$\mathscr I^+$, and pullback by $\phi_S$ preserves weighted, partially polyhomogeneous b-Sobolev spaces near compact
subsets of $I_0^\circ$ ($\phi_S$ is the flow of a b-vector field; the source's argument after (5.77b)); $\mathcal
L_{\partial_{t_{\mathrm{IVP}}}}$ and $r$ are a b-vector field and a weight there.

(2) The data (3.1) depend smoothly on $S$ (differentiate (3.1)). Formally $\dot h := \frac{d}{ds}h_{S(s)}|_{s = 0}$,
$S(0) = S_0$, $\dot S = S'(0)$, solves
$$L^{\chi_0}_{\phi_{S_0}^*g_{b_0}+h_{S_0},\phi_{S_0}^*g_{b_0}}\dot h =
-\frac{d}{ds}P^{\chi_0}\big(\phi_{S(s)}^*g_{b_0}+h_{S_0},\phi_{S(s)}^*g_{b_0}\big)\Big|_{s = 0},$$
with the differentiated data. The right side is a linear differential expression in $\frac{d}{ds}\phi_{S(s)}^*g_{b_0}$,
which lies in $\rho_0^2\rho_I^2C^\infty$ with the slots of III.C (3.4) on $\Omega_{\mathrm{ext},r_1}$ (differentiate
Lemma 1.1's expansion in $S$), applied with coefficients in the classes of III.C Proposition 4.4; so it lies in the
target space of III.C Proposition 5.2, (5.2). III.C$'$ (2.2) (the linear estimate, for $L^{\chi_0}$ by Lemma 2.1 and
(C$''$2)) and the proof of III.C$'$ Theorem 3.1 give $\dot h$ in the class of $h_S$; difference quotients converge to
$\dot h$ by the same estimate applied to their difference with $\dot h$, and higher derivatives follow likewise, with
the losses of footnote 59.

(3) By (1) and the hypotheses, $\phi_S^*g_{b_0}+h_S = \phi_S^*(g_{b_0}+h)$ near $\Sigma_{\mathrm{IVP},r_1}$, whose data
satisfy the constraints and the gauge condition there (the pullback of data that do); III.C$'$ Remark 2.2 (1) (the
second Bianchi identity) gives the conclusions on $\Omega_{\mathrm{ext},r_1}$. $\square$

**Remark 3.2 ([Hin26] Remark 5.24 at n = 4).** If $h_0 = h_1 = 0$, then $h_S = 0$ by uniqueness, and the metric is
$\phi_S^*g_{b_0}$. On all of $\Sigma_{\mathrm{IVP}}$ such data are compactly supported perturbations of the Myers-Perry
data, as produced by gluing ([CD03]; Part V).

## 4. Gauged Cauchy data ([Hin26] Proposition 5.25 and section 5.7.1 at n = 4)

**Proposition 4.1 ([Hin26] Proposition 5.25 at n = 4).** Let $\mathcal E_0$ be an index set with
$\min\mathrm{Re}\,\mathcal E_0>0$ and $j\mathcal E_0\subset\mathcal E_0$ for $j\in\mathbb N$, and $\ell_0>0$. Let
$\gamma = \gamma_{b_0}+\tilde\gamma$, $k = k_{b_0}+\tilde k$ on $\Sigma_{\mathrm{IVP}}$ with $\tilde\gamma\in
H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}(\Sigma_{\mathrm{IVP}};S^2T^*\Sigma_{\mathrm{IVP}})$, $\tilde k\in
H^{\infty,(\mathcal E_0+1,\ell_0+1)}_{\mathrm b}(\Sigma_{\mathrm{IVP}};S^2T^*\Sigma_{\mathrm{IVP}})$, $\tilde\gamma$
small in $H^3_{\mathrm b}$. There are $h_0,h_1\in H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm
b}(\Sigma_{\mathrm{IVP}};S^2T^*)$, depending continuously on $(\tilde\gamma,\tilde k)$ and 0 at $(0,0)$, such that for
every spacetime metric $g$ with $(g-g_{b_0})|_{\Sigma_{\mathrm{IVP}}} = h_0$ and $(r\mathcal
L_{\partial_{t_{\mathrm{IVP}}}}(g-g_{b_0}))|_{\Sigma_{\mathrm{IVP}}} = h_1$: (1) the first and second fundamental forms
of $\Sigma_{\mathrm{IVP}}$ for $g$ are $\gamma$ and $k$; (2) $\Upsilon^0(g,g_{b_0}) = 0$ at $\Sigma_{\mathrm{IVP}}$.

*Proof.* As in the source, which follows [HV18b, Proposition 3.10] and [HV24, Theorem 4.2]; the dimension enters only
through the size of the frame. Near $\Sigma_{\mathrm{IVP}}$ write $g_{b_0} =
a\,dt_{\mathrm{IVP}}^2+2dt_{\mathrm{IVP}}\otimes_sb+\gamma_{b_0}$ and set $h_0 := \tilde\gamma$, so $g_0 := g_{b_0}+h_0$
induces $\gamma$. Let $\nu_{b_0}$, $\nu_0 = \nu_{b_0}+\tilde\nu$ be the future unit normals; $\tilde\nu\in
H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}$. We seek $h_1 = r\tilde h_1$ such that $g := g_0+t_{\mathrm{IVP}}\tilde
h_1$ (still with unit normal $\nu_0$ at $\Sigma_{\mathrm{IVP}}$) has second fundamental form $k$ and
$\Upsilon^0(g,g_{b_0}) = 0$ there. These are the source's (5.80) and (5.81):
$$g_0\big((\nabla^{g}_X-\nabla^{g_0}_X)Y,\nu_0\big) = \tilde
k(X,Y)-h_0(\nabla^{g_{b_0}}_XY,\nu_{b_0})-g_0(\nabla^{g_{b_0}}_XY,\tilde\nu)-
g_0\big((\nabla^{g_0}_X-\nabla^{g_{b_0}}_X)Y,\nu_0\big),$$
$$\mathrm{tr}_{g_0}(\nabla^{g}-\nabla^{g_0}) = -\mathrm{tr}_{g_0}(\nabla^{g_0}-\nabla^{g_{b_0}}).$$
Each $x$-derivative of $h_0$ gains a factor $r^{-1}$ (b-regularity), the Christoffel symbols of $g_{b_0}$ are
$O(r^{-3})$ with all b-derivatives at $n = 4$ (III.B Proposition 3.6: the mass enters at $|x|^{-2}$), and $\mathcal E_0$
is closed under sums; so both right sides lie in $H^{\infty,(\mathcal E_0+1,\ell_0+1)}_{\mathrm b}$. In a frame $e_0 =
\nu_0$, $e_1,\dots,e_4$ $g_0$-orthonormal and tangent to $\Sigma_{\mathrm{IVP}}$, at $t_{\mathrm{IVP}} = 0$,
$2(\Gamma(g)_{\lambda\mu\nu}-\Gamma(g_0)_{\lambda\mu\nu}) = (t_{\mathrm{IVP}})_{;\mu}(\tilde
h_1)_{\nu\lambda}+(t_{\mathrm{IVP}})_{;\nu}(\tilde h_1)_{\mu\lambda}-(t_{\mathrm{IVP}})_{;\lambda}(\tilde
h_1)_{\mu\nu}$, with $e_it_{\mathrm{IVP}} = 0$ ($i\ge1$) and $e_0t_{\mathrm{IVP}}$ in $C^\infty+H^{\infty,(\mathcal
E_0,\ell_0)}_{\mathrm b}$ and bounded away from 0. The first equation at $(e_i,e_j)$, $i,j = 1,\dots,4$, reads
$-\frac12(e_0t_{\mathrm{IVP}})(\tilde h_1)_{ij} = \cdots$ and determines $(\tilde h_1)_{ij}$; the $e^j$-component of the
second determines $(\tilde h_1)_{0j}$, and its $e^0$-component, $-\frac12(e_0t_{\mathrm{IVP}})(\tilde h_1)_{00} =
f_0+\frac12(e_0t_{\mathrm{IVP}})(g_0)^{ij}(\tilde h_1)_{ij}$, determines $(\tilde h_1)_{00}$; all in
$H^{\infty,(\mathcal E_0+1,\ell_0+1)}_{\mathrm b}$, linearly and continuously in the data. So $h_1 = r\tilde h_1\in
H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}$. $\square$

These data enter III.C$'$ Theorem 3.1 when $\min\mathrm{Re}\,\mathcal E_0>\frac32+2\gamma_\Upsilon$ and
$\ell_0>\frac32$, and then Theorem 3.1 above; if $(\gamma,k)$ satisfy the constraints, the solutions are vacuum
(III.C$'$ Remark 2.2 (1), Theorem 3.1 (3)).

**Proposition 4.2 (data at Boyer-Lindquist time 0; [Hin26] section 5.7.1 and Remark 5.26 at n = 4).** Let
$t_{\mathrm{BL}}$ be the Boyer-Lindquist time of $g_{b_0}$ and suppose data on $\Sigma^{\mathrm{BL}} :=
t_{\mathrm{BL}}^{-1}(0)$ are as in (5.82) of the source, with index set $\mathcal E_0$ and weight $\ell_0$, small, and
satisfying the constraints. Then the solution of the gauge-fixed equation with $\Upsilon^0$ in a conic neighbourhood
$U_\delta := \{|t/r|<\delta,\ r>\delta^{-1}\}$ of spatial infinity induces on $\Sigma_{\mathrm{IVP}}\cap\{r>r_0\}$ data
$(h_0,h_1)$ in $H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}$: the index set is unchanged, with no $\mathcal E_{\log}$.

*Proof.* The solution in $U_\delta$ is the source's (the "boost theorem" [COM81], proved by III.C$'$ Theorem 2.1's
arguments on $[-\delta,\delta]_\tau\times[0,\delta]_\rho\times\mathbb S^3$, $\tau = t/r$); its partial polyhomogeneity
$h\in H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}(U_\delta)$ follows as in III.C$'$ Theorem 3.1, Step 1. On $\{|x|\ge
R_3\}$, $t_{\mathrm{IVP}} = t-C''$ (III.B (3.6)-(3.7)) with $t$ the Kerr-Schild time of III.B; for the Myers-Perry
metric at $n = 4$, $t-t_{\mathrm{BL}} = \int\frac{\mu r^{-2}}{1-\mu r^{-2}}\,dr+O(r^{-2}) = -\mu r^{-1}+O(r^{-2})$, a
smooth function of $\rho = r^{-1}$ near $\rho = 0$ (at $n = 3$ the integral is $2m\log r$). So $\tau_{\mathrm{IVP}} :=
t_{\mathrm{IVP}}/r = \tau_{\mathrm{BL}}+\rho\,c(\rho)$ with $c$ smooth, and Taylor expansion of
$a(\tau_{\mathrm{BL}})\rho^z(\log\rho)^k = a(\tau_{\mathrm{IVP}}-\rho c(\rho))\rho^z(\log\rho)^k$ in $\rho$ gives terms
$\rho^{z+j}(\log\rho)^k$, $j\in\mathbb N_0$: the index set $(z,k)+\mathbb N_0\subset\mathcal E_0$, with no new
logarithm. $\square$

The source's Remark 5.26 (logarithms from $(2,0)+\mathcal E_{\log}$) therefore has no counterpart at $n = 4$ from this
mechanism; the logarithmic index sets the later sections allow arise there for other reasons (the $\iota^+$ and $K^+$
analysis) and are kept.

**Remark 4.3 ([Hin26] Example 5.27 at n = 4).** (1) Data exactly Myers-Perry outside a compact set ([CD03] at $n = 4$,
Part V) satisfy Proposition 4.1 with $\mathcal E_0 = \emptyset$ and every $\ell_0$. (2)-(3) The conformal-method
constructions the source cites are stated at $n = 3$; their $n = 4$ versions are not used here.

## 5. Findings, labels and sources

(C$''$1) *A misprint in the source* (p. 108): "$\phi_S(\Sigma_{\mathrm{IVP}})\subset\{\chi_0 = 1\}$" should read
$\{\chi_0 = 0\}$. The argument needs the gauge to be $\Upsilon^0$ (natural under pullback, (5.75)) near
$\Sigma_{\mathrm{IVP},r_1}$ and near its image, which is where $\chi_0 = 0$. Also "$\check\chi_0|_{[-\frac18,-\frac18]}
= 1$" should read $[-\frac18,\frac18]$.

(C$''$2) *Part IV must deliver III.C$'$ Theorem 2.1 in the cut-off gauge*, for $P^{\chi_0}$ and $g_0\in\mathcal G$. The
source's justification is that the stationarity of $E^\Upsilon$ and the choice of $c_\Upsilon$ away from $\mathscr I^+$
play no role in its Theorems 5.17 and 5.21. At $n = 4$, Lemma 2.1 shows that the change lies in the error class of III.C
(4.4); the energy estimates of [Hin23a] must be checked to tolerate it (they use the structure at $\mathscr I^+$ and
robust estimates elsewhere).

(C$''$3) *III.C (C4) is settled* by the slope $\frac1{12}$ of III.C$'$ Lemma 1.1's past slab (Lemma 1.1).

(C$''$4) *No logarithms from the time function at $n = 4$* (Proposition 4.2).

*Labels.* Lemma 1.1 is the first paragraph of the source's section 5.6; (2.1)-(2.2) its (5.75)-(5.76); Theorem 3.1 its
Theorem 5.23; Remark 3.2 its Remark 5.24; Proposition 4.1 its Proposition 5.25; Proposition 4.2 its section 5.7.1 with
Remark 5.26; Remark 4.3 its Example 5.27; Lemma 2.1 is new at $n = 4$.

*Sources.* [Hin26] pp. 108-113 (sections 5.6-5.7: (5.75)-(5.83b), Theorem 5.23 with footnote 59, Remark 5.24,
Proposition 5.25 with (5.79)-(5.81), section 5.7.1, Remark 5.26, Example 5.27), read at source. Inputs: III.B section 5
(the cut-off boosts, Lemma 5.2, the cut-offs), section 6, Proposition 3.6, (3.6)-(3.7); III.C Definition 3.4, Lemma 3.5,
Proposition 4.4, Proposition 5.2, Corollary 5.3, (C4); III.C$'$ Lemma 1.1, Theorems 2.1 and 3.1, Remark 2.2; III.F
section 1; Part IV; Part V ([CD03]).
