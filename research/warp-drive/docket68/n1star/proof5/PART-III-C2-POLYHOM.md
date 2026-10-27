# Part III.C$'$. The exterior solution and its partial polyhomogeneity, n = 4 ([Hin26] sections 5.4-5.5)

*Status.* Written (D288); verified (D291: verifier 125's findings seated); proved (D292: verifier 126 read the repairs).
This part proves, at spatial dimension $n = 4$, [Hin26] Lemma 5.16, the estimate (5.53) and Theorem 5.17 as consequences
of Part IV, and Theorem 5.21 (pp. 99-108). It settles obligation (C7) of III.C: at $n = 4$ the radiation fields need not
be subtracted. Theorem 5.17 and (5.53) rest on [Hin23a] section 3 at $n = 4$, which Part IV writes out; they are stated
here as that part's output (finding (C$'$1)). Sections 5.6-5.7 of the source (Theorem 5.23, Proposition 5.25) are Part
III.C$''$.

*What n = 4 changes.* (1) *Weights.* The radiation fields decay like $|x|^{-3/2}$ (III.C (a)), so every weight at
$\mathscr I^+$ is shifted by $\frac12$: the source's (5.49),
$1<\ell^\flat_I<\min(\ell^\flat_0,1+(1-e_\Upsilon)\gamma_\Upsilon,\frac32)$, becomes (1.1). (2) *No subtraction.* The
source's Theorem 5.21, Step 2, measures $h$ from $g_{b_0}+h_0$, $h_0$ carrying the radiation fields of $\slashed\pi_0h$
and $\pi_{11}h$, because at $n = 3$ these enter the leading part of the operator at $\mathscr I^+$ (its $A^h$). At $n =
4$ the leading part is the constant $\bar A$ and all of the perturbation lies in the error (III.C Proposition 4.4,
finding (C1)); so the equation is integrated directly, without $h_0$ and without the source term $P(g_0,g_{b_0})$, and
the obligation (C7) does not arise. (3) *Half steps.* The error gains $\frac12$ at $\mathscr I^+$ instead of the
source's $\min(\alpha_I-1,(1-e_\Upsilon)\gamma_\Upsilon)$, so Step 2 raises the weight by any $\eta<\frac12$ per round.
(4) *The index condition at $I_0$* is $\min\mathrm{Re}\,\mathcal E_0>\frac32+2\gamma_\Upsilon$, so that $\mathcal
E_0\subset\mathcal E^C_I$ is compatible with III.C Definition 3.1 (2).

Notation: as in III.C (the faces $I_0$, $\mathscr I^+$, the coordinates (1.2) and $\rho_0$, $\rho_I$, $X_0 =
\rho_0\partial_{\rho_0}$, $X_I = \rho_I\partial_{\rho_I}$, the splitting (1.6) with its slots 1-7, the matrix $\bar A$
of Lemma 4.2, Definition 3.1 and the spaces (3.3)); III.A Lemmas 1.2, 1.3 and 3.2 (the source's Lemmas 2.12, 2.11 and
2.23). The parameters are those of III.C (1.1) and III.F section 1; $b_0 = (\mu_0,0)$. Densities are $\mu_{\mathrm b}$,
so a weight is the pointwise order (b-Sobolev embedding, $k>\frac52$).

## 1. The domain ([Hin26] Lemma 5.16 at n = 4)

Fix weights
$$\ell^\flat_0>\tfrac32,\qquad\tfrac32<\ell^\flat_I<\min\big(\ell^\flat_0,\ \tfrac32+(1-e_\Upsilon)\gamma_\Upsilon,\
2\big).\tag{1.1}$$
So $\ell^\flat_I<\min\mathrm{Re}\,\mathcal E^C_I$ for every $\mathcal E^C_I$ of III.C Definition 3.1, and
$H^{k,\ell^\flat_0,(-,\ell^\flat_I)}_{\mathrm b}$ (III.C after (3.3)) consists of the $h$ with every slot in
$H^{k,\ell^\flat_0,\ell^\flat_I}_{\mathrm b}$ except $\slashed\pi_0h\in
H^{k,\ell^\flat_0,((\frac32,0),\ell^\flat_I)}_{\mathrm b}$, which carries a radiation field (the slot-4, 5 and 7
exponents $\frac32+s$, $s\in\sigma_\Upsilon\setminus\{0\}$, exceed $\ell^\flat_I$ by (1.1) and
$(1-e_\Upsilon)\gamma_\Upsilon\le\gamma_\Upsilon\le2\gamma_\Upsilon$).

**Lemma 1.1 (spacetime domain; [Hin26] Lemma 5.16 at n = 4).** For $r_0$ large let, with $r = |x|$,
$$\Omega_{\mathrm{ext},r_0} := \big\{-\tfrac{r-r_0}{12}\le t_{\mathrm{IVP}}\le0\big\}\cup\big\{0\le t_{\mathrm{IVP}}\le
r+2r^{1-\ell^\flat_I}-(r_0+2r_0^{1-\ell^\flat_I})\big\},$$
with boundary hypersurfaces $\Sigma_{\mathrm{past},r_0}$, $\Sigma_{\mathrm{fut},r_0}$ (the first and last level sets)
and $\Sigma_{\mathrm{IVP},r_0} := \Omega_{\mathrm{ext},r_0}\cap\{t_{\mathrm{IVP}} = 0\}$. There is $R_0>3R_1$ such that
for $r_0\ge R_0$ and every $h\in H^{3,\ell^\flat_0,(-,\ell^\flat_I)}_{\mathrm b}(\Omega_{\mathrm{ext},r_0})$ with norm
below 1 (III.C's spaces (3.3), defined there for $k\ge5$, extend verbatim to $k = 3$), the three hypersurfaces are
spacelike for $g_{b_0}+h$.

*Proof.* For $r$ large, $t_{\mathrm{IVP}} = t-C''$ (III.B Lemma 3.7 (b)), and $r^{1-\ell^\flat_I}\to0$ as
$\ell^\flat_I>1$; so $\Omega_{\mathrm{ext},r_0}\subset U\cap\{|x|\ge r_0\}$ (III.C (1.3)) for $r_0$ large, and on it
$\rho_0\le C/r_0$: on $\Sigma_{\mathrm{fut},r_0}$, $x^1 = t-r = -r_0+2r^{1-\ell^\flat_I}-2r_0^{1-\ell^\flat_I}+O(1)$,
and $x^1$ is smaller below it, so $\rho_0 = (2-x^1)^{-1}\le C/r_0$. By Sobolev embedding ($3>\frac52$) every slot of $h$
is bounded by $C\rho_0^{\ell^\flat_0}\rho_I^{\ell^\flat_I}$, except $\slashed\pi_0h$, bounded by
$C\rho_0^{\ell^\flat_0}\rho_I^{3/2}$; and $g_{b_0}-\eta\in\rho_0^2\rho_I^2C^\infty$ with its $\pi_C$, $\pi_{01}$,
$\pi_{1/}$, $\slashed\pi_0$ parts in $\rho_0^2\rho_I^3C^\infty$ (III.C Lemma 3.5 (1), Definition 3.4). Write $\delta :=
g_{b_0}+h-\eta$, so $|\delta|\le C(\rho_0^2\rho_I^2+\rho_0^{\ell^\flat_0}\rho_I^{3/2})$ in the frame of (1.6), which is
small for $r_0$ large.

*$\Sigma_{\mathrm{IVP},r_0}$ and $\Sigma_{\mathrm{past},r_0}$.* $dt$ is timelike for $\eta$, and so for $\eta+\delta$
when $|\delta|$ is small. In the coordinates $(u,r)$ of Minkowski space ($u := t-r$, not the $t_*$ of III.B (3.6)),
$\eta^{-1} = -2\partial_u\partial_r+\partial_r^2$ on $du,dr$, so $\zeta := d(t_{\mathrm{IVP}}+\frac{r-r_0}{12}) =
du+\frac{13}{12}dr$ has $\eta^{-1}(\zeta,\zeta) = -2\cdot\frac{13}{12}+(\frac{13}{12})^2 = -\frac{143}{144}$ (the
computation is dimension-free; any slope $c\in(0,1)$ in place of $\frac1{12}$ gives $-2(1+c)+(1+c)^2 = (c+1)(c-1)<0$);
so $\zeta$ is timelike for $\eta+\delta$ too.

*$\Sigma_{\mathrm{fut},r_0}$.* With $x^0 = t+r$, $x^1 = t-r$, $\eta = -dx^0dx^1$ (symmetric product), so $\eta^{01} =
-2$, $\eta^{00} = \eta^{11} = 0$, and $dr = \frac12(dx^0-dx^1)$. For $\ell := \ell^\flat_I$,
$$\zeta := d\big(t_{\mathrm{IVP}}-r-2r^{1-\ell}\big) = (\ell-1)r^{-\ell}dx^0+\big(1-(\ell-1)r^{-\ell}\big)dx^1,$$
so $\eta^{-1}(\zeta,\zeta) = -4(\ell-1)r^{-\ell}(1-(\ell-1)r^{-\ell})$, with $r^{-\ell} = \rho_0^\ell\rho_I^\ell$. As
$\zeta$ has no angular part, $(\eta+\delta)^{-1}(\zeta,\zeta)-\eta^{-1}(\zeta,\zeta) =
-\eta^{ia}\eta^{jb}\delta_{ab}\zeta_i\zeta_j+O(|\delta|^2)$, $i,j,a,b\in\{0,1\}$. The coefficient of $\zeta_1^2$ is
$-4\delta_{00}$, of $\pi_C$-type, bounded by $C(\rho_0^2\rho_I^3+\rho_0^{\ell^\flat_0}\rho_I^{\ell^\flat_I})$; that of
$\zeta_0\zeta_1$ involves $\delta_{01}$, bounded likewise; that of $\zeta_0^2$ involves $\delta_{11}$, bounded by
$C(\rho_0^2\rho_I^2+\rho_0^{\ell^\flat_0}\rho_I^{\ell^\flat_I})$ and multiplied by $\zeta_0^2 =
O(\rho_0^{2\ell}\rho_I^{2\ell})$; and $O(|\delta|^2)\le C(\rho_0^4\rho_I^4+\rho_0^{2\ell^\flat_0}\rho_I^3)$. Relative to
$\rho_0^\ell\rho_I^\ell$ these are at most
$C(\rho_0^{2-\ell}\rho_I^{3-\ell}+\rho_0^{\ell^\flat_0-\ell}+\rho_0^{2\ell^\flat_0-\ell}\rho_I^{3-\ell})$, which tends
to 0 as $\rho_0\to0$, as $\ell<2$, $\ell<\ell^\flat_0$ and $\ell<3$ (1.1). As $\rho_0\le C/r_0$ on
$\Omega_{\mathrm{ext},r_0}$, for $r_0$ large $(\eta+\delta)^{-1}(\zeta,\zeta)\le-2(\ell-1)r^{-\ell}<0$. $\square$

The source's past slab has the slope $\frac14$; the slope $\frac1{12}$ keeps $\Omega_{\mathrm{ext},r_0}$ inside
$\{t_{\mathrm{IVP}}>-|x|/10\}$, where $\chi_{\mathrm{IVP}} = 1$ (III.B), so that the boosts of III.C$''$ are genuine
boosts on all of it (finding (C4) of III.C). The source's version uses its Lemma 5.6 for the pointwise bounds; here the
slots of $h$ and of $g_{b_0}-\eta$ give them directly, the mass entering at $\rho_0^2\rho_I^2$ in the 11-slot only
(III.C (b)).

## 2. The exterior solution ([Hin26] (5.52)-(5.53) and Theorem 5.17 at n = 4; Part IV)

**Theorem 2.1 ([Hin26] Theorem 5.17 at n = 4; from Part IV).** There is $k_0\in\mathbb N$ such that the following holds.
Let $\ell^\flat_0$, $\ell^\flat_I$ be as in (1.1) and $r_0\ge R_0$ (Lemma 1.1). There is $\epsilon_0>0$ such that for
$h_0,h_1\in H^{\infty,\ell^\flat_0}_{\mathrm b}(\Sigma_{\mathrm{IVP},r_0};S^2T^*)$ with
$\|h_j\|_{H^{k_0,\ell^\flat_0}_{\mathrm b}}<\epsilon_0$, the problem
$$P(g_{b_0}+h,g_{b_0}) = 0\ \text{in }\Omega_{\mathrm{ext},r_0},\qquad h = h_0,\ \ r\mathcal
L_{\partial_{t_{\mathrm{IVP}}}}h = h_1\ \text{on }\Sigma_{\mathrm{IVP},r_0},\tag{2.1}$$
has a unique solution $h\in H^{\infty,\ell^\flat_0,(-,\ell^\flat_I)}_{\mathrm b}(\Omega_{\mathrm{ext},r_0})$; and for
every $\epsilon>0$ and $k$ there are $k_1\ge k_0$ and $\epsilon_1\in(0,\epsilon_0]$ such that
$\|h_j\|_{H^{k_1,\ell^\flat_0}_{\mathrm b}}<\epsilon_1$ gives $\|h\|_{H^{k,\ell^\flat_0,(-,\ell^\flat_I)}_{\mathrm
b}}<\epsilon$ (the source reuses the letters $k_0$, $\epsilon_0$ here). Moreover, for $h\in
H^{\infty,\ell^\flat_0,(-,\ell^\flat_I)}_{\mathrm b}$ small in a fixed $H^{d}$-norm and every $\alpha_0>\ell^\flat_I$,
the solution of
$$L_{g_{b_0}+h,g_{b_0}}\dot g = f\in H^{k+d,\alpha_0+2,(-',\ell^\flat_I+1)}_{\mathrm b},\qquad\dot
g|_{\Sigma_{\mathrm{IVP},r_0}} = \dot g_0,\quad r\mathcal L_{\partial_{t_{\mathrm{IVP}}}}\dot
g|_{\Sigma_{\mathrm{IVP},r_0}} = \dot g_1,\quad\dot g_0,\dot g_1\in H^{k+d,\alpha_0}_{\mathrm b},$$
satisfies
$$\|\dot g\|_{H^{k,\alpha_0,(-,\ell^\flat_I)}_{\mathrm b}}\le
C\big(\|f\|_{H^{k+d,\alpha_0+2,(-',\ell^\flat_I+1)}_{\mathrm b}}+\|\dot g_0\|_{H^{k+d,\alpha_0}_{\mathrm b}}+\|\dot
g_1\|_{H^{k+d,\alpha_0}_{\mathrm b}}\big),\tag{2.2}$$
with $C$ depending on $k$, $\alpha_0$, $\ell^\flat_I$ and $h$; and the tame form of (2.2) at $\alpha_0 = \ell^\flat_0$,
the source's (5.52).

Here $(-',\ell^\flat_I+1)$ is the class of III.C Definition 5.1 (2) with the index sets left out, as in the
source. The source proves
Theorem 5.17 from [Hin23a] Theorem 3.35 and Corollary 3.36 "with minor, only notational, modifications": the tame
estimate (5.52), a Nash-Moser scheme (the source cites [SR89]; here II.G Theorem 2.1, which is [Hin26c] Theorem 12.4),
and the radiation field of $\pi_{11}\dot g$, $\slashed\pi_0\dot g$ recovered by integrating the leading part. At $n = 4$
the leading part is III.C (4.4), and only $\slashed\pi_0$ carries a radiation field (III.C (C3)). [Hin23a] section 3 is
written out at $n = 4$ in Part IV; N1STAR-PROOF.md 10.64 records the eight places where $n$ enters it. Theorem 2.1 is
that part's output and is used below as stated (finding (C$'$1)).

**Remark 2.2 ([Hin26] Remarks 5.18 and 5.20 at n = 4).** (1) If the data of $\hat g :=
g_{b_0}+h_0+t_{\mathrm{IVP}}r^{-1}h_1$ (the source's Remark 5.18 prints $t_{\mathrm{IVP}}rh_1$; with $h_1 = r\mathcal
L_{\partial_{t_{\mathrm{IVP}}}}h$ of (2.1) the factor is $r^{-1}$, as in its Proposition 5.25 and section 5.7.1; finding
(C$'$5)) satisfy the vacuum constraints on $\Sigma_{\mathrm{IVP},r_0}$ and $\Upsilon^{E_\Upsilon}(\hat g,g_{b_0}) = 0$
there, the second Bianchi identity gives $\Upsilon(g_{b_0}+h,g_{b_0}) = 0$ and $\mathrm{Ric}(g_{b_0}+h) = 0$, in any
dimension (10.57 (d) of the record; III.C$''$ for the gauged data). (2) The structure (4.4) of III.C holds for every
$g_0\in\mathcal G$ (III.C Definition 3.4), and Corollary 5.3 of III.C needs only $\mathrm{Ric}(g_0) = 0$; so Theorem 2.1
holds for $P(g_0+h,g_0) = 0$ with $g_0\in\mathcal G$ Ricci flat and $g_0-g_{b_0}$ small in the sense of Lemma 1.1, in
particular for $g_0 = \phi_S^*g_{b_0}$ where III.C Lemma 3.5 (2) applies (the cut-off region near $I_0$ is III.C$''$,
(C4)).

## 3. Partial polyhomogeneity ([Hin26] Theorem 5.21 at n = 4)

**Theorem 3.1 ([Hin26] Theorem 5.21 at n = 4).** Let $\mathcal E_0$ be an index set with $\min\mathrm{Re}\,\mathcal
E_0>\frac32+2\gamma_\Upsilon$ and $j\mathcal E_0\subset\mathcal E_0$ for $j\in\mathbb N$. Let $\ell_0,\ell_I>\frac32$
with $\ell_0\notin\mathrm{Re}\,\pi_1\mathcal E_0$, $\ell_I<\ell_0$, $\ell_I<\frac32+(1-e_C)(1-v_C)\gamma_C$ and
$\ell_I\notin\frac32+\sigma_\Upsilon$. Let $\ell^\flat_0 := \frac32+\frac12(1-e_\Upsilon)\gamma_\Upsilon$ and
$\ell^\flat_I := \frac32+\frac14(1-e_\Upsilon)\gamma_\Upsilon$, which satisfy (1.1). There is an index set $\mathcal
E^C_I$ satisfying III.C Definition 3.1 and $\mathcal E_0\subset\mathcal E^C_I$ such that: if $h_0,h_1\in
H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}(\Sigma_{\mathrm{IVP},r_0};S^2T^*)$ satisfy the smallness of Theorem 2.1,
the solution $h$ of (2.1) satisfies
$$h\in H^{\infty,(\mathcal E_0,\ell_0),\langle\mathcal E^C_I\rangle,\ell_I}_{\mathrm
b}(\Omega_{\mathrm{ext},r_0}),\tag{3.1}$$
and for every $k$ and $\epsilon>0$ there are $k_0$, $\epsilon_0$ with
$$\|h_j\|_{H^{k_0,(\mathcal E_0,\ell_0)}_{\mathrm b}}<\epsilon_0\ (j = 0,1)\implies\|h\|_{H^{k,(\mathcal
E_0,\ell_0),\langle\mathcal E^C_I\rangle,\ell_I}_{\mathrm b}}<\epsilon.\tag{3.2}$$

As in the source (its Remark 5.22), smallness of $\|h_j\|_{H^{k_0,\ell^\flat_0}_{\mathrm b}}$ does not make the
coefficients of the expansions small, which is why (3.2) is stated separately.

*Proof.* *Step 1 (the expansion at $I_0$).* Suppose $h\in H^{\infty,(\mathcal E_0,\alpha_0),(-,\ell^\flat_I)}_{\mathrm
b}$ for some $\alpha_0\in[\ell^\flat_0,\ell_0)$; for $\alpha_0 = \ell^\flat_0$ this is Theorem 2.1
($\ell^\flat_0<\min\mathrm{Re}\,\mathcal E_0$). As $P(g_{b_0}+h,g_{b_0}) = 0$ and $P(g_{b_0},g_{b_0}) = 0$,
$$L_{g_{b_0}}h = -\int_0^1\big(L_{g_{b_0}+sh,g_{b_0}}-L_{g_{b_0},g_{b_0}}\big)h\,ds.\tag{3.3}$$
By III.C Proposition 4.4, applied with $g_1 = g_0 = g_{b_0}$ to $h$ and to $0$, the two operators have the same
leading part and the same $C^\infty$ error (the paragraph "The perturbation" of its proof), and their difference lies in
$H^{\infty,(\mathcal E_0+2,\alpha_0+2),(\mathcal E^{\mathrm{tot}}_I,\ell^\flat_I)}_{\mathrm b}\mathrm{Diff}^2_{\mathrm
b}$ on $U$ (the perturbation part of (4.4), whose coefficients are polynomial in $sh$ and its first two derivatives,
each term with a factor of $h$; III.C Lemma 4.3), uniformly in $s$. Acting on $h$, whose slots lie in
$H^{\infty,(\mathcal E_0,\alpha_0),(\mathcal E^{\mathrm{tot}}_I,\ell^\flat_I)}_{\mathrm b}$, it gives by III.C Lemma 2.1
an element of $H^{\infty,(\mathcal E_0+2,\alpha_0+3),(2\mathcal E^{\mathrm{tot}}_I,\ell^\flat_I+1)}_{\mathrm b}$: at
$I_0$ the index set is $2\mathcal E_0+2\subset\mathcal E_0+2$ and the weight $\alpha_0+2+\min\mathrm{Re}\,\mathcal
E_0>\alpha_0+3$ (as $\min\mathrm{Re}\,\mathcal E_0>1$); at $\mathscr I^+$, $2\mathcal E^{\mathrm{tot}}_I\subset\mathcal
E^C_I+1$ (III.C Lemma 3.2 (b)), at weight $\ell^\flat_I+\frac32>\ell^\flat_I+1$. Away from $U$ the spaces impose only
regularity. So $h$ solves
$$L_{g_{b_0}}h\in H^{\infty,(\mathcal E_0+2,\alpha_0+3),(-',\ell^\flat_I+1)}_{\mathrm b},\qquad
h|_{\Sigma_{\mathrm{IVP},r_0}} = h_0,\ \ r\mathcal L_{\partial_t}h|_{\Sigma_{\mathrm{IVP},r_0}} = h_1\in
H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}.\tag{3.4}$$
This is one order better at $I_0$ than III.C Proposition 5.2 alone gives. (The source writes $\mathcal E_0+3$; the index
set is $\mathcal E_0+2$, the gain being in the weight, which is what the argument uses.) Lower $\alpha_0$ slightly if
needed so that $\alpha_1 := \min(\alpha_0+1,\ell_0)\notin\mathrm{Re}\,\pi_1\mathcal E_0$. Let $\mathcal E_{0,\le} :=
\{(z,k)\in\mathcal E_0:\mathrm{Re}\,z\le\alpha_1\}$, finite, $N := |\mathcal E_{0,\le}|$, and $R :=
\prod_{(z,k)\in\mathcal E_{0,\le}}(X_0-z)\in\mathrm{Diff}^N_{\mathrm b}$. Then $Rh\in
H^{\infty,\alpha_0,(-,\ell^\flat_I)}_{\mathrm b}$ (III.A Lemma 1.3, converse), and
$$L_{g_{b_0}}(Rh) = \rho_0^2R\big(\rho_0^{-2}L_{g_{b_0}}h\big)+\rho_0^2\big[\rho_0^{-2}L_{g_{b_0}},R\big]h.$$
Index sets are closed under $+\mathbb N_0$ (III.C section 2), so $\mathcal E_0+j\subset\mathcal E_0$. The first term:
$\rho_0^{-2}L_{g_{b_0}}h\in H^{\infty,(\mathcal E_0,\alpha_0+1),(-',\ell^\flat_I+1)}_{\mathrm b}$ by (3.4), and $R$
removes its expansion at $I_0$ up to $\alpha_1\le\alpha_0+1$ (III.A Lemma 1.3, converse), so the first term lies in
$H^{\infty,\alpha_1+2,(-',\ell^\flat_I+1)}_{\mathrm b}$. For the second, by III.C Lemma 4.1 and (3.5)
below, $A := \rho_0^{-2}L_{g_{b_0}} = -\rho_I(X_I-\frac32-\bar A)(X_0-X_I)+\rho_0^{-2}\tilde R_b$ with
$\rho_0^{-2}\tilde R_b\in\rho_I^2C^\infty\mathrm{Diff}^2_{\mathrm b}$, the leading part having coefficients independent
of $\rho_0$. $X_0$ commutes with $X_0$, $X_I$, $\partial_\omega$, $\rho_I$ and the constant $\bar A$, and maps $a\in
C^\infty$ to $X_0a\in\rho_0C^\infty$; so $R$ commutes with the leading part, and $[A,R] = [\rho_0^{-2}\tilde
R_b,R]\in\rho_0\rho_I^2\mathrm{Diff}^{N+1}_{\mathrm b}$. (The cruder $[A,R]\in\rho_0\rho_I\mathrm{Diff}^{N+1}_{\mathrm
b}$ would not do: on the radiation field $\rho_I^{3/2}$ of slot 6 it gives $\rho_I^{5/2}$, below the weight
$\ell^\flat_I+1\in(\frac52,3)$ of the target.) Split $h = h_{\mathrm e}+h_{\mathrm r}$, $h_{\mathrm e}$ the terms of
its expansion at $I_0$ with real part at most $\alpha_0$ (those known) and $h_{\mathrm r}\in H^{\infty,\alpha_0}$ at
$I_0$. Then $Rh_{\mathrm e} = 0$, so $[A,R]h_{\mathrm e} = -RAh_{\mathrm e}$. At $I_0$, $Ah_{\mathrm e}$ has its
expansion in $\mathcal E_0$ (smooth coefficients only add $\mathbb N_0$), and $R$ removes its terms up to $\alpha_1$,
leaving order $>\alpha_1$. At $\mathscr I^+$, $Ah_{\mathrm e}$ lies in $(-',\ell^\flat_I+1)$: the leading part sends
the slots other than 6 from the weight $\ell^\flat_I$ to $\ell^\flat_I+1$ and annihilates the radiation field
$\rho_I^{3/2}a$ of slot 6 ($\bar A_{66} = \bar A_{6i} = \bar A_{76} = 0$, so on it $(X_I-\frac32-\bar A)$ acts as
$X_I-\frac32$, which commutes past $X_0-X_I$), and $\rho_0^{-2}\tilde R_b$ gains $\rho_I^2$. And $[A,R]h_{\mathrm r}\in
H^{\infty,\alpha_0+1}$ at $I_0$, with $\alpha_0+1\ge\alpha_1$, and has the weight at least $\frac32+2>\ell^\flat_I+1$ at
$\mathscr I^+$. So $\rho_0^2[A,R]h\in H^{\infty,\alpha_1+2,(-',\ell^\flat_I+1)}_{\mathrm b}$. The data of $Rh$ lie in
$H^{\infty,\alpha_1}_{\mathrm b}(\Sigma_{\mathrm{IVP},r_0})$. Theorem 2.1 (2.2), with $h = 0$ and $\alpha_0$ replaced by
$\alpha_1>\ell^\flat_I$, gives $Rh\in H^{\infty,\alpha_1,(-,\ell^\flat_I)}_{\mathrm b}$, and III.A Lemma 1.3 gives $h\in
H^{\infty,(\mathcal E_0,\alpha_1),(-,\ell^\flat_I)}_{\mathrm b}$. After finitely many steps, $h\in H^{\infty,(\mathcal
E_0,\ell_0),(-,\ell^\flat_I)}_{\mathrm b}$.

*Step 2 (the expansion at $\mathscr I^+$).* Suppose $h\in H^{\infty,(\mathcal E_0,\ell_0),\langle\mathcal
E^C_I\rangle,\alpha_I}_{\mathrm b}$ for some $\alpha_I\in[\ell^\flat_I,\ell_I)$ and some $\mathcal E^C_I$ of III.C
Definition 3.1 with $\mathcal E_0\subset\mathcal E^C_I$; Step 1 gives this for $\alpha_I = \ell^\flat_I$, with any such
$\mathcal E^C_I$ (one exists: III.C Lemma 3.2 (e) applied to $\mathcal E_0$). By (3.3) and III.C Proposition 4.4 on $U$,
$$\big(X_I-\tfrac32-\bar A\big)(X_0-X_I)h = \tilde f := \rho_0^{-2}\rho_I^{-1}\Big(\tilde
R_bh+\int_0^1\big(L_{g_{b_0}+sh,g_{b_0}}-L_{g_{b_0}}\big)h\,ds\Big),\tag{3.5}$$
with $\tilde R_b\in\rho_0^2\rho_I^2C^\infty\mathrm{Diff}^2_{\mathrm b}$ (III.C (4.4) at $h = 0$). The first term maps
the slots of $h$, in $(\mathcal E^{\mathrm{tot}}_I,\alpha_I)$ at $\mathscr I^+$, to $(\mathcal
E^{\mathrm{tot}}_I+1,\alpha_I+1)\subset(\mathcal E^C_I,\alpha_I+1)$ (III.C Lemma 3.2 (a)). The second is $\rho_I^{-1}$
times a $\mathrm{Diff}^2_{\mathrm b}$-operator with coefficients in $H^{\infty,(\mathcal E_0,\ell_0),(\mathcal
E^{\mathrm{tot}}_I,\alpha_I)}_{\mathrm b}$ acting on $h$; by III.C Lemma 2.1 it lies in $(\mathcal
E^{\mathrm{tot}}_I+\mathcal E^{\mathrm{tot}}_I-1,\alpha_I+\eta)\subset(\mathcal E^C_I,\alpha_I+\eta)$ for every
$\eta<\frac12$ (III.C Definition 3.1 (3); the weight is $\alpha_I+\frac32-1$, with the strict inequality of Lemma 2.1).
At $I_0$ both lie in $(\mathcal E_0,\ell_0)$. Fix $\eta\in(\frac14,\frac12)$ and put $\beta :=
\min(\alpha_I+\eta,\ell_I)$ (as in the source's Step 2.6); lower $\eta$ slightly if needed so that
$\beta\notin\frac32+\sigma_\Upsilon$ and $\beta\notin\mathrm{Re}\,\pi_1\mathcal E_0$ (not needed if $\beta = \ell_I$, by
the hypotheses). So
$$\tilde f\in H^{\infty,(\mathcal E_0,\ell_0),(\mathcal E^C_I,\beta)}_{\mathrm b}(U).\tag{3.6}$$
Write $w := (X_0-X_I)h$; its slots have the index sets of $h$'s (III.A (F1)). By III.C Lemma 4.2, $\bar A$ is lower
triangular with the diagonal (4.3) of III.C and off-diagonal entries at $(3,1)$, $(4,1)$, $(4,3)$, $(5,2)$, $(7,3)$,
$(7,4)$, and $\bar A_{76} = 0$. We integrate slot by slot, in the order 1, 2, 3, 4, 5, 6, 7, putting the off-diagonal
terms on the right.

(i) *Slots 1-3 ($\pi_Ch$).* $(X_I-\frac32-\bar A_{jj})w_j = \tilde f_j+\sum_{i<j}\bar A_{ji}w_i$, with $\frac32+\bar
A_{jj}\ge\frac32+(1-e_C)(1-v_C)\gamma_C>\ell_I\ge\beta$ ($1-e_C<1$). By induction the right side lies in $(\mathcal
E^C_I,\beta)$ at $\mathscr I^+$, and III.A Lemma 1.2 (the source's Lemma 2.12; $\beta\ne\frac32+\bar A_{jj}$, and the
new exponent $\frac32+\bar A_{jj}$ lies above $\beta$, so only the conormal statement is affected) gives $w_j\in
H^{\infty,(\mathcal E_0,\ell_0),(\mathcal E^C_I,\beta)}_{\mathrm b}$. Then $(X_0-X_I)h_j = w_j$, and III.A Lemma 3.2
with $z = 0$ ($\ell_0>\beta$, $\beta\notin\mathrm{Re}\,\pi_1\mathcal E_0$; away from $\mathscr I^+$ there is nothing to
show) gives $h_j\in H^{\infty,(\mathcal E_0,\ell_0),(\mathcal E_0\bar\cup\mathcal E^C_I,\beta)}_{\mathrm b}$.

(ii) *Slots 4-5 ($\pi_{01}h$, $\pi_{1/}h$).* The couplings $(4,1)$, $(4,3)$, $(5,2)$ bring $w_1,w_2,w_3\in(\mathcal
E^C_I,\beta)$. Lemma 1.2 with $z = \frac32+\bar A_{jj}$, $\bar A_{44} = (1-e_\Upsilon)\gamma_\Upsilon$, $\bar A_{55} =
\gamma_\Upsilon$, gives $w_j$ the index set $\mathcal E^C_I\cup(\frac32+\bar A_{jj},0)$, which is $\mathcal E_{I,01}$,
resp. $\mathcal E_{I,1/}$ (III.C (3.2)), at weight $\beta$; Lemma 3.2 then gives $h_j$ the extended union with $\mathcal
E_0$.

(iii) *Slot 6 ($\slashed\pi_0h$).* No coupling ($\bar A_{6i} = 0$ for $i<6$). Lemma 1.2 with $z = \frac32$ gives
$\slashed{\mathcal E}_{I,0} = \mathcal E^C_I\cup(\frac32,0)$: the radiation field.

(iv) *Slot 7 ($\pi_{11}h$).* The couplings $(7,3)$ (from $\mathcal E^C_I$) and $(7,4)$ (from $\mathcal E_{I,01}$) and no
$(7,6)$; Lemma 1.2 with $z = \frac32+2\gamma_\Upsilon$ gives $\mathcal
E^C_I\cup(\frac32+(1-e_\Upsilon)\gamma_\Upsilon,0)\cup(\frac32+2\gamma_\Upsilon,0) = \mathcal E_{I,11}$ (if $\bar A_{77}
= 2\gamma_\Upsilon$ equals $\bar A_{44}$, the two exponents coincide and Lemma 1.2 gives a logarithm; the index set
(3.2) of III.C then needs $(\frac32+2\gamma_\Upsilon,1)$, which happens only for $e_\Upsilon = -1$, excluded by
$0<e_\Upsilon<1$). No radiation field of $\slashed\pi_0h$ reaches slot 7: this is III.C's (C3).

III.A Lemma 3.2 gives the extended union $\mathcal E_0\bar\cup(\cdot)$ at $\mathscr I^+$: where an exponent of the
expansion at $I_0$ meets one at $\mathscr I^+$, the corner produces a logarithm. So, with $\mathcal E'$ the smallest
index set containing $\mathcal E_0\bar\cup\mathcal E^C_I$ and satisfying III.C Definition 3.1 (it exists by III.C Lemma
3.2 (e), as $\min\mathrm{Re}(\mathcal E_0\bar\cup\mathcal E^C_I)>\frac32+2\gamma_\Upsilon$; it contains $\mathcal E_0$),
the slots of $h$ lie in the classes of III.C (3.3) for $\mathcal E'$, at weight $\beta$ (for slots 4, 5
and 7, $\mathcal E_0\bar\cup\mathcal E_{I,j}\subset\mathcal E'_{I,j}$ by III.C Lemma 3.2 (d), as
$\min\mathrm{Re}\,\mathcal E_0>\frac32+2\gamma_\Upsilon$): $h\in H^{\infty,(\mathcal
E_0,\ell_0),\langle\mathcal E'\rangle,\beta}_{\mathrm b}$ on $U$, and off $U$ trivially. This is the source's Step 2.6,
its $\mathcal E^{C,\mathrm{new}}_I$. Repeating with $(\alpha_I,\mathcal E^C_I)$ replaced by $(\beta,\mathcal E')$,
$\eta>\frac14$, reaches $\ell_I$ after $M\le4(\ell_I-\ell^\flat_I)+1$ rounds, with index sets $\mathcal
E^{(0)}\subset\mathcal E^{(1)}\subset\dots\subset\mathcal E^{(M)}$; take $\mathcal E^C_I := \mathcal E^{(M)}$, $\mathcal
E^{(0)}$ the smallest index set of III.C Definition 3.1 containing $\mathcal E_0$. As the number of rounds and every
step depend only on $\mathcal E_0$, $\ell_0$, $\ell_I$ and the parameters, so does $\mathcal E^C_I$. This is (3.1).

*Smallness (3.2).* Each step is linear in the data of the previous one: the coefficients of the expansion at $I_0$ are
obtained from $Rh$, which Theorem 2.1 (2.2) bounds by the data and the source of (3.4); the source of (3.4) is quadratic
in $h$, bounded in $H^{k,\alpha_0+3}$ by the previous step's norms times the small
$\|h\|_{H^{k+2,\ell^\flat_0,(-,\ell^\flat_I)}}$; and III.A Lemmas 1.2, 1.3 and 3.2 are bounded at every order. At
$\mathscr I^+$ the coefficients are obtained by the integrations of (i)-(iv), bounded likewise. Finitely many steps
compose to (3.2), with $k_0$ the sum of the losses plus Theorem 2.1's. $\square$

**Remark 3.2 (the source's Step 2 and (C7)).** At $n = 3$ the entries $A^h-A_0$ and $B^h$ of the source's (5.28) are of
the order of $A_0$ at $\mathscr I^+$, so the radiation fields of $\pi_{11}h$ and $\slashed\pi_0h$ enter the leading part
of the operator; the source removes them by $g_0 = g_{b_0}+h_0$, at the cost of the source term $P(g_0,g_{b_0})$
((5.64), with $\langle(2,0)\rangle_0$). At $n = 4$ they are half an order lower (III.C (C1)) and sit in the error of
(3.5), whose index set $\mathcal E^{\mathrm{tot}}_I+\mathcal E^{\mathrm{tot}}_I-1$ lies in $\mathcal E^C_I$ by III.C
Definition 3.1 (3). So III.C (C7) is settled: the subtraction is not needed, and no class with $(\frac32,0)$ in slot 6
is used.

## 4. Findings, labels and sources

(C$'$1) *Theorem 2.1 rests on Part IV.* [Hin26] Theorem 5.17 is [Hin23a] Corollary 3.36 with notational changes; at $n =
4$ that paper's section 3 is to be written out in Part IV (the record's 10.64 locates the eight places where $n$ enters,
and (5.49)'s weights become (1.1)). Theorem 2.1, with (2.2) and its tame form, is the statement Part IV must deliver;
until it does, Theorem 3.1 is proved relative to it.

(C$'$2) *(C7) of III.C is settled* (Remark 3.2): no subtraction of radiation fields, no source term, a constant leading
matrix.

(C$'$3) *The source's "$\mathcal E_0+3$" in Step 1* is the index set $\mathcal E_0+2$ with weight $\alpha_0+3$; the
argument uses only the weight.

(C$'$4) *A coincidence of exponents in slot 7.* $\frac32+2\gamma_\Upsilon$ and $\frac32+(1-e_\Upsilon)\gamma_\Upsilon$
coincide only at $e_\Upsilon = -1$; under $0<e_\Upsilon<1$ they are distinct, and III.C (3.2) needs no logarithm.

(C$'$5) *A misprint in the source's Remark 5.18* (p. 101): the metric whose data are constrained is
$g_{b_0}+h_0+t_{\mathrm{IVP}}r^{-1}h_1$, not $\ldots+t_{\mathrm{IVP}}rh_1$, by the convention $h_1 =
r\mathcal L_{\partial_{t_{\mathrm{IVP}}}}h$ of the source's Theorem 5.17 ((2.1) here) and as in its Proposition 5.25 and
section 5.7.1.

*Labels.* Lemma 1.1 is the source's Lemma 5.16, Theorem 2.1 its Theorem 5.17 with (5.52)-(5.53), Remark 2.2 its Remarks
5.18 and 5.20, Theorem 3.1 its Theorem 5.21 with Remark 5.22; Remark 3.2 is new at $n = 4$.

*Sources.* [Hin26] pp. 99-108 (section 5.4: (5.49)-(5.53), Lemma 5.16, Theorem 5.17, Remarks 5.18-5.20; section 5.5:
Theorem 5.21, Remark 5.22, (5.54)-(5.74)), read at source. Inputs: III.A (F1), Lemmas 1.2, 1.3, 3.2; III.B Lemma 3.7 (b);
III.C (1.1)-(1.3), (1.6), Definitions 3.1, 3.4, 5.1, Lemmas 2.1, 3.2, 3.5, 4.1-4.3, Proposition 4.4, Proposition 5.2,
Corollary 5.3, findings (C1), (C3), (C4), (C7); II.G Theorem 2.1; Part IV ([Hin23a] section 3 at $n = 4$, to be
written); N1STAR-PROOF.md 10.57, 10.64.
