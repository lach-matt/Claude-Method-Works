# Part III.C. The exterior region at n = 4: perturbations and the operator at null infinity ([Hin26] 5.1-5.3)

*Status.* Verified (D244: the hundred-and-first verifier; no major finding, four minor and six nits seated, to be read).
This part proves, at spatial dimension $n = 4$, [Hin26] Definitions 5.1-5.4 and 5.13, Remark 5.5, Proposition 5.11 with
(5.40)-(5.41a), Proposition 5.14 and Corollary 5.15 (pp. 84-99), and the parts of Lemmas 5.6-5.8 and Corollaries
5.9-5.10 that these use. Sections 5.4-5.7 of the source (Lemma 5.16, Theorems 5.17, 5.21 and 5.23, Proposition 5.25) and
the edge-b form (5.26b) that their energy estimates use are Part III.C$'$. Parts are cited as before; the source is
[Hin26] = P. Hintz, arXiv:2606.28253v2 (printed page numbers).

*What n = 4 changes.* Three things, and together they make the structure simpler than the source's.

(a) Radiation fields at null infinity decay like $r^{-3/2}$, so the index sets at $\mathscr I^+$ start at $\frac32$
where the source's start at 1 (as at $\iota^+\cap\mathscr I^+$, III.G$'$ Definition 1.2).

(b) The mass of Myers-Perry enters at $|x|^{-2}$ (III.B Proposition 3.6). At the corner $I_0\cap\mathscr I^+$ it lies in
the error class $\rho_0^2\rho_I^2C^\infty$, so the leading part there is Minkowski's, where the source carries the
Schwarzschild terms.

(c) The perturbation's contributions to the operator, the source's $A^h-A_0$ and $B^h$ of (5.28), carry at least
$\rho_I^{1/2}$ relative to the constant matrix $A_0$, where the source's are of the same order. They join the error, at
the cost of the index set $\mathcal E^{\mathrm{tot}}_I$ in place of $\mathcal E^C_I$ in its perturbation part. So the
structure theorem (Proposition 4.3) has a constant lower-triangular matrix $\bar A$ and no $h$-dependent leading part.
The source's (7,6) coupling of $\slashed\pi_0h$'s radiation field into $\pi_{11}h$ is half an order lower and lands in
$\mathcal E^C_I$, so $\pi_{11}h$ carries no radiation field (Definition 3.1, finding (C3)). The source's last index
condition is strengthened to $\mathcal E^{\mathrm{tot}}_I+(\mathcal E^{\mathrm{tot}}_I-1)\subset\mathcal E^C_I$, which
needs $\gamma_\Upsilon<\frac14$.

## 1. Hypotheses, the exterior region, and its coordinates

Throughout: $n = 4$, $D = 5$; the family $g_b$, $b = (\mu,A)\in\mathcal B$, of III.B, with $\mu_0$, $R_1 = \mu_0^{1/2}$,
the compactification $M$ and its faces $I_0$, $\mathscr I^+$, $\iota^+$, $K^+$ (III.B Definition 2.1); the time
functions $t_* = t-\psi(|x|)$ and $t_{\mathrm{IVP}}$ (III.B (3.6), Lemma 3.7), with $t_* = t-|x|+C'-8\mu_0|x|^{-1}$ on
$\{|x|\ge3R_1\}$; and the gauge parameters of III.F section 1, with, in addition,
$$0<\gamma_\Upsilon<\tfrac14,\qquad0<e_\Upsilon<1.\tag{1.1}$$
(The source's conditions (5.42), $v_C<1$, $0<e_C<1$, $\gamma_C>0$, $0<e_\Upsilon<1$, $\gamma_\Upsilon>0$, hold under
III.F's choices.) Let $\eta := -dt^2+dx^2$ in the coordinates of III.B, and
$$x^0 := t+|x|,\qquad x^1 := t-|x|,\qquad\rho_0 := \frac1{2-x^1},\qquad\rho_I := \frac{2-x^1}{|x|},\tag{1.2}$$
the last two being III.B (2.2)'s coordinates near $I_0\cap\mathscr I^+$. ($x^0$ here is Minkowski's; III.B (4.1)'s $x^0$
for $g_\mu$ is $t+|x|-T_\mu(|x|)$, and the two null frames differ by $I+\rho^2C^\infty$, Lemma 1.3.) Fix
$T_0 := C'+1-2R_1$ and set
$$\Omega_{\mathrm{ext}} := \mathrm{cl}_M\{t_*\le T_0\},\qquad U := \Omega_{\mathrm{ext}}\cap\{|x|\ge4R_1\}.\tag{1.3}$$
(The source fixes $T$ and shifts it to 1, (5.1); the choice of $T_0$ only makes (1.2) global on $U$.) On $U$,
$x^1 = t_*-C'+8\mu_0|x|^{-1}\le T_0-C'+2R_1 = 1$, since $\mu_0 = R_1^2$.

**Lemma 1.1 (the corner coordinates).** (1) $(\rho_0,\rho_I,\omega)$, $\omega = x/|x|$, are coordinates on all of $U$,
smooth up to $I_0$ and $\mathscr I^+$: $\rho_0\in[0,1]$, $\rho_0 = 0$ exactly at $I_0$, $\rho_I = 0$ exactly at
$\mathscr I^+$, and $\rho_0\rho_I = |x|^{-1}$. (2) With $X_0 := \rho_0\partial_{\rho_0}$,
$X_I := \rho_I\partial_{\rho_I}$ (at fixed $\omega$ and the other coordinate), exactly on $U$,
$$\partial_{t_*}|_{\rho,\omega} = \rho_0(X_0-X_I),\qquad
\rho\partial_\rho|_{t_*,\omega} = X_I+8\mu_0\rho_0^2\rho_I(X_0-X_I),\qquad\rho := |x|^{-1},\tag{1.4}$$
$$\partial_0 = -\tfrac12\rho_0\rho_IX_I,\qquad\partial_1 = \rho_0\big(X_0-X_I+\tfrac12\rho_IX_I\big),\tag{1.5}$$
with $\partial_0,\partial_1$ the coordinate fields of $(x^0,x^1,\omega)$. In particular $\partial_t$, $\partial_{x^i}$,
$\partial_0$, $\partial_1$ and $|x|^{-1}\partial_\omega$ lie in $\rho_0\mathcal V_{\mathrm b}(U)$, and
$\partial_0,|x|^{-1}\partial_\omega\in\rho_0\rho_I\mathcal V_{\mathrm b}(U)$.

*Proof.* (1) $(x^1,|x|)\mapsto(\rho_0,\rho_I)$ is a diffeomorphism of $\{x^1<2,|x|>0\}$ onto $(0,\infty)^2$, with
inverse $x^1 = 2-\rho_0^{-1}$, $|x| = (\rho_0\rho_I)^{-1}$. Near $I_0\cap\mathscr I^+$ these are III.B (2.2)'s
coordinates. Near the interior of $I_0$, III.B uses $(\tau,\rho) = (t/|x|,|x|^{-1})$ with $\tau\in[-\frac12,1-\delta]$;
there $\rho_I = 1-\tau+2\rho$ and $\rho_0 = \rho/\rho_I$, smooth with smooth inverse $\rho = \rho_0\rho_I$,
$\tau = 1-\rho_I+2\rho_0\rho_I$, as $\rho_I\ge\delta$. Near the interior of $\mathscr I^+$, III.B uses
$(t_0,\rho) = (x^1, |x|^{-1})$; there $\rho_0 = (2-t_0)^{-1}$ and $\rho_I = (2-t_0)\rho$, smooth with smooth inverse for
$t_0\le1$. These charts cover a neighbourhood of $(I_0\cup\mathscr I^+)\cap\Omega_{\mathrm{ext}}$, and $U$ meets no
other face at infinity (it meets $\Sigma^{\mathrm{past}}$ and $\{t_* = T_0\}$, where the spaces are extendible). (2) A
vector field $aX_0+bX_I$ is determined by its action on two functions of $(\rho_0,\rho_I)$. With
$t_* = 2-\rho_0^{-1}+C' -8\mu_0\rho_0\rho_I$ and $\rho = \rho_0\rho_I$: $X_0t_* = \rho_0^{-1}-8\mu_0\rho$,
$X_It_* = -8\mu_0\rho$, $X_0\rho = X_I\rho = \rho$. So $\rho_0(X_0-X_I)$ maps $t_*\mapsto1$, $\rho\mapsto0$; and
$X_I+\alpha(X_0-X_I)$ with $\alpha := 8\mu_0\rho_0^2\rho_I$ maps $\rho\mapsto\rho$ and
$t_*\mapsto-8\mu_0\rho+\alpha\rho_0^{-1} = 0$. For (1.5): $\partial_0|x| = \frac12$, $\partial_1|x| = -\frac12$,
$\partial_0x^1 = 0$, $\partial_1x^1 = 1$; so $\partial_0\rho_0 = 0$, $\partial_0\rho_I = -\frac12\rho_0\rho_I^2$,
$\partial_1\rho_0 = \rho_0^2$, $\partial_1\rho_I = -\rho_0\rho_I+\frac12\rho_0\rho_I^2$, which is (1.5). (`ext5.py` E1
checks (1.4), and (1.5) for Tangherlini's null coordinates with $f = 1-\mu|x|^{-2}$ for $\frac12$, of which (1.5) is
$f = 1$.) The memberships: $\partial_t = \partial_0+ \partial_1$, $\partial_{|x|} = \partial_0-\partial_1$,
$\partial_{x^i} = \omega^i\partial_{|x|}+|x|^{-1}(\ldots) \partial_\omega$, and
$|x|^{-1}\partial_\omega = \rho_0\rho_I\partial_\omega$ with $\partial_\omega$ (at fixed $\rho_0,\rho_I$) a b-vector
field. $\square$

*The splitting.* On $U$, in the rescaled frame $(dx^0,dx^1,|x|e^a)$, $e^a$ a local orthonormal coframe of $\mathbb S^3$,
the source's (5.27) reads
$$S^2T^* = \langle(dx^0)^2\rangle\oplus(2dx^0\otimes_s|x|T^*\mathbb S^3)\oplus\langle|x|^2\slashed g\rangle\oplus
\langle2dx^0dx^1\rangle\oplus(2dx^1\otimes_s|x|T^*\mathbb S^3)\oplus|x|^2\ker\slashed{\mathrm{tr}}\oplus
\langle(dx^1)^2\rangle,\tag{1.6}$$
of ranks $1+3+1+1+3+5+1 = 15$: III.B (4.4) for $\eta$, reordered. A symmetric 2-tensor $h$ has rescaled components
$h_{00},h_{0\bar a},h_{01},h_{1\bar a},h_{11},h_{\bar a\bar b}$ (III.B Definition after (4.4)), and its *slot
coordinates* are, in the order of (1.6),
$$(h_{00},\ h_{0\bar a},\ \tfrac13\slashed{\mathrm{tr}}h,\ h_{01},\ h_{1\bar a},\ \slashed\pi_0h,\ h_{11}),\qquad
\slashed{\mathrm{tr}}h := \slashed g^{ab}h_{\bar a\bar b}\tag{1.7}$$
(the third the coefficient of $|x|^2\slashed g$; `scri5.py`'s normalisation).

**Definition 1.2 ([Hin26] Definition 5.2 at n = 4).** $\pi_Ch := (h_{00},h_{0\bar a},\slashed{\mathrm{tr}}h)$,
$\pi_{01}h := h_{01}$, $\pi_{1/}h := h_{1\bar a}$,
$\slashed\pi_0h := h_{\bar a\bar b}-\frac13(\slashed{\mathrm{tr}}h) \slashed g_{ab}$, $\pi_{11}h := h_{11}$. ($\frac13$
for the source's $\frac12$: the trace-free part on $\mathbb S^3$.)

**Lemma 1.3 (frames).** Three smooth frames of $S^2T^*$ on $U$ are used: the products of the Cartesian $dt,dx^i$; those
of III.F's $dt_*,dx^i$; and the rescaled null frame of (1.6). Each is related to the next by a smooth bundle map with
smooth inverse, of the form $F_0(\omega)(I+\rho^2C^\infty(U))$ with $F_0$ depending on $\omega$ alone.

*Proof.* $dt_* = dt-\psi'(|x|)d|x|$ with $\psi' = 1-8\mu_0|x|^{-2}$ on $U$, so $dt_* = dx^1+8\mu_0|x|^{-2}d|x|$, and
$d|x| = \omega_idx^i$, $|x|e^a = $ the orthonormal tangential projection of $dx$, both depending on $\omega$ alone, and
$dx^0 = dt+d|x|$, $dx^1 = dt-d|x|$. $\square$

So the spaces below, which are defined slot by slot in (1.6), do not depend on which of the null frames of $\eta$,
$g_\mu$ (III.B (4.2)) or $\bar g$ (III.F) is used: these differ by $I+\rho^2C^\infty$, and $\rho^2 = \rho_0^2\rho_I^2$
moves a component's index sets by 2 at both faces, into $\mathcal E^C_I$ (Lemma 3.2 (c)).

## 2. Function spaces, products

We use III.A's notions without change: index sets, $(z,k)$ for the smallest index set containing $(z,k)$, sums
$\mathcal E+\mathcal F$, and the partially polyhomogeneous spaces
$H^{k,(\mathcal E_0,\alpha_0),(\mathcal E_I, \alpha_I)}_{\mathrm b}$ of [Hin26] Definition 2.8 and Notation 2.9, with
the faces listed as $I_0$, $\mathscr I^+$ (III.A section 1). On $\Omega_{\mathrm{ext}}$ these are spaces of restrictions
(extendible at $\{t_* = T_0\}$, $\Sigma^{\mathrm{past}}$ and $\Sigma^{\mathrm{int}}$), as the source's (5.2) is;
$\dim\Omega_{\mathrm{ext}} = 5$. Sections of the summands of (1.6) are taken in local trivialisations by $e^a$.

**Lemma 2.1 (products).** Let $Z$ be a manifold with corners of dimension $d$, compact or a relatively compact domain in
one, with boundary hypersurfaces $H$; let $k>\frac d2$, $k'\ge k$,
$u\in H^{k,(\vec{\mathcal E},\vec\alpha)}_{\mathrm b}(Z)$, $v\in H^{k',(\vec{\mathcal F},\vec\beta)}_{\mathrm b}(Z)$.
Let $\gamma_H\le\alpha_H+\beta_H$, $\gamma_H<\alpha_H+\min\mathrm{Re}\,\mathcal F_H$ and
$\gamma_H<\beta_H+\min\mathrm{Re}\,\mathcal E_H$ for every $H$ ($\min\mathrm{Re}\,\emptyset := +\infty$). Then
$uv\in H^{k,(\vec{\mathcal E}+\vec{\mathcal F},\vec\gamma)}_{\mathrm b}(Z)$, and $(u,v)\mapsto uv$ is continuous.

*Proof.* (i) *No expansions.* $H^k_{\mathrm b}$ is $H^k$ for a b-metric, which in logarithmic coordinates
$s_i = -\log x_i$ near a corner is uniformly equivalent to the Euclidean metric on a cover by unit cubes $Q_m$ of
bounded overlap. On one cube $\|fg\|_{H^k(Q)}\le C\|f\|_{H^k(Q)}\|g\|_{H^{k'}(Q)}$ for $k>\frac d2$, $k'\ge k$ (Sobolev
embedding and the Leibniz rule), with $C$ the same for every cube. Summing, $\|fg\|^2_{H^k}\le
C^2\sum_m\|f\|^2_{H^k(Q_m)}\|g\|^2_{H^{k'}(Q_m)}\le C'\|f\|^2_{H^k}\|g\|^2_{H^{k'}}$. Weights multiply: $\rho^\alpha
H^k_{\mathrm b}\cdot\rho^\beta H^{k'}_{\mathrm b}\subset\rho^{\alpha+\beta}H^k_{\mathrm b}$. (ii) *Expansions.* Induct
on the number of pairs (face, factor) at which a factor carries an expansion. Pick such a face $H$ and write, in a
collar, $u = \chi\sum\rho_H^z(\log\rho_H)^lu_{(z,l)}+u'$ ((2.3) of the source's Definition 2.8), and the same for $v$
(with no sum if $v$ has none at $H$). The products of the sums give
$\chi^2\rho_H^{z+w}(\log\rho_H)^{l+m}u_{(z,l)}v_{(w,m)}$ ($\chi^2-\chi$ is supported where $\rho_H\ge\frac\epsilon2$ and
goes to the remainder) with $(z+w,l+m)\in\mathcal E_H+\mathcal F_H$. The coefficient $u_{(z,l)}v_{(w,m)}$ lies in the
space of $H$ required by Definition 2.8, by the lemma on $H$ (dimension $d-1$, $k>\frac{d-1}2$). Terms with
$\mathrm{Re}(z+w)\le\gamma_H$ are kept; the others are $\rho_H^{\gamma_H}$ times $\rho_H^{\epsilon}(\log\rho_H)^{l+m}$,
$\epsilon>0$, and go to the remainder. A cross term $\chi\rho_H^z(\log \rho_H)^lu_{(z,l)}v'$ has weight
$\mathrm{Re}\,z+\beta_H-\epsilon'$ at $H$ for every $\epsilon'>0$, which exceeds $\gamma_H$ by hypothesis, and fewer
expansions, so the induction applies to it. The same holds for $u'v$ and $u'v'$, the last of weight
$\alpha_H+\beta_H\ge\gamma_H$. Continuity follows from the same bounds. $\square$

We use with it (F1) of III.A: a b-vector field maps $H^{k,(\vec{\mathcal E},\vec\alpha)}_{\mathrm b}$ to
$H^{k-1,(\vec{\mathcal E},\vec\alpha)}_{\mathrm b}$. Multiplication by $C^\infty$ preserves the spaces, as index sets
are closed under $+\mathbb N_0$, and by $\rho_H^c$ it shifts $\mathcal E_H$ and $\alpha_H$ by $c$.

## 3. Metric perturbations ([Hin26] Definitions 5.3-5.4, Remark 5.5 at n = 4)

Write $\sigma_\Upsilon := \{0,(1-e_\Upsilon)\gamma_\Upsilon,\gamma_\Upsilon,2\gamma_\Upsilon\}\subset[0,\frac12)$, the
eigenvalues of $\bar S$ on the slots 4-7 (III.F Lemma 3.1, Lemma 4.2 below).

**Definition 3.1 ([Hin26] Definition 5.3 at n = 4).** Let $\mathcal E_0,\mathcal E^C_I\subset\mathbb C\times\mathbb N_0$
be index sets such that

(1) $\min\mathrm{Re}\,\mathcal E_0>0$ and $j\mathcal E_0\subset\mathcal E_0$ for all $j\in\mathbb N$;

(2) $\min\mathrm{Re}\,\mathcal E^C_I>\frac32+2\gamma_\Upsilon$;

(3) with
$$\mathcal E^{\mathrm{tot}}_I := \mathcal E^C_I\cup\bigcup_{s\in\sigma_\Upsilon}(\tfrac32+s,0),\tag{3.1}$$
$\mathcal E^{\mathrm{tot}}_I+(\mathcal E^{\mathrm{tot}}_I-1)\subset\mathcal E^C_I$.

This strengthens the source's $\mathcal E^C_I+(\mathcal E^{\mathrm{tot}}_I-1)\subset\mathcal E^C_I$, and it implies the
source's $j\mathcal E^{\mathrm{tot}}_I\subset\mathcal E^C_I$, $j\ge2$ (Lemma 3.2 (b)). It is needed for Proposition 5.2:
built under the $n = 4$ analogue of the source's conditions instead, $\mathcal E^C_I$ misses $(2,0)$ and
$2\mathcal E^{\mathrm{tot}}_I\not\subset\mathcal E^C_I+1$ (`ext5.py` E5, third control).

Set
$$\mathcal E_{I,01} := \mathcal E^C_I\cup(\tfrac32+(1-e_\Upsilon)\gamma_\Upsilon,0),\quad
\mathcal E_{I,1/} := \mathcal E^C_I\cup(\tfrac32+\gamma_\Upsilon,0),\quad
\slashed{\mathcal E}_{I,0} := \mathcal E^C_I\cup(\tfrac32,0),$$
$$\mathcal E_{I,11} := \mathcal E^C_I\cup(\tfrac32+(1-e_\Upsilon)\gamma_\Upsilon,0)\cup(\tfrac32+2\gamma_\Upsilon,0).
\tag{3.2}$$
Let $k\ge5$, $\ell_0>0$ and $\ell_I>\frac32$. Then $H^{k,(\mathcal E_0,\ell_0),\langle\mathcal
E^C_I\rangle,\ell_I}_{\mathrm b}(\Omega_{\mathrm{ext}})\subset H^{k,0,0}_{\mathrm b}(\Omega_{\mathrm{ext}};S^2T^*)$ is
the space of real symmetric 2-tensors $h$ whose restriction to $U$ satisfies
$$\pi_Ch\in H^{k,(\mathcal E_0,\ell_0),(\mathcal E^C_I,\ell_I)}_{\mathrm b},\ \ \pi_{01}h\in H^{k,(\mathcal E_0,\ell_0),
(\mathcal E_{I,01},\ell_I)}_{\mathrm b},\ \ \pi_{1/}h\in H^{k,(\mathcal E_0,\ell_0),(\mathcal E_{I,1/},\ell_I)}_{\mathrm
b},$$
$$\slashed\pi_0h\in H^{k,(\mathcal E_0,\ell_0),(\slashed{\mathcal E}_{I,0},\ell_I)}_{\mathrm b},\ \ \pi_{11}h\in
H^{k,(\mathcal E_0,\ell_0),(\mathcal E_{I,11},\ell_I)}_{\mathrm b}.\tag{3.3}$$
If $0<\ell_0<\min\mathrm{Re}\,\mathcal E_0$ we write $\ell_0$ for $(\mathcal E_0,\ell_0)$, and if
$\frac32<\ell_I<\min \mathrm{Re}\,\mathcal E^C_I$ we write $(-,\ell_I)$ for $(\langle\mathcal E^C_I\rangle,\ell_I)$.

So $\pi_Ch$ decays strongly at $\mathscr I^+$; $\pi_{01}h$ and $\pi_{1/}h$ like
$|x|^{-3/2-(1-e_\Upsilon) \gamma_\Upsilon}$ and $|x|^{-3/2-\gamma_\Upsilon}$; $\slashed\pi_0h$ has a radiation field at
$|x|^{-3/2}$; and $\pi_{11}h$ carries the exponents $\frac32+2\gamma_\Upsilon$ (its own) and
$\frac32+(1-e_\Upsilon)\gamma_\Upsilon$ (from $\pi_{01}h$ through $\bar A$'s (7,4) entry), but no radiation field,
unlike the source's $(1,0)$ (finding (C3)). The condition $k\ge5$ gives
$k-2>\frac52 = \frac12\dim\Omega_{\mathrm{ext}}$, so Lemma 2.1 applies to $H^{k-2}$ factors.

**Lemma 3.2 (consequences of Definition 3.1).** Under (1.1) and Definition 3.1:

(a) $\mathcal E^C_I+\frac12\subset\mathcal E^C_I$ and $\mathcal E^{\mathrm{tot}}_I+\frac12\subset\mathcal E^C_I$; so
$\mathcal E^C_I+1$, $\mathcal E^{\mathrm{tot}}_I+1\subset\mathcal E^C_I$, and $(2,0),(3,0)\subset\mathcal E^C_I$.

(b) $j\mathcal E^{\mathrm{tot}}_I\subset\mathcal E^C_I+(j-1)$ for $j\ge2$; in particular
$2\mathcal E^{\mathrm{tot}}_I \subset\mathcal E^C_I+1$.

(c) $\mathcal E^{\mathrm{tot}}_I+2\subset\mathcal E^C_I+1$, and every component index set of (3.3) lies in
$\mathcal E^{\mathrm{tot}}_I$.

(d) The intersections of $\mathcal E_{I,01}$, $\mathcal E_{I,1/}$, $\slashed{\mathcal E}_{I,0}$, $\mathcal E_{I,11}$
with $\{\mathrm{Re}\,z>\frac32+2\gamma_\Upsilon\}$ equal that of $\mathcal E^C_I$ (the source's remark (iii)).

(e) For every index set $\tilde{\mathcal E}$ with $\min\mathrm{Re}\,\tilde{\mathcal E}>\frac32+2\gamma_\Upsilon$ there
is a smallest $\mathcal E^C_I\supseteq\tilde{\mathcal E}$ satisfying (2)-(3) (the source's remark (ii)).

*Proof.* (a) $(\frac32,0)\subset\mathcal E^{\mathrm{tot}}_I$, so $\frac12\in\mathcal E^{\mathrm{tot}}_I-1$, and (3)
gives $\mathcal E^C_I+\frac12\subset\mathcal E^{\mathrm{tot}}_I+(\mathcal E^{\mathrm{tot}}_I-1)\subset\mathcal E^C_I$,
and likewise $\mathcal E^{\mathrm{tot}}_I+\frac12\subset\mathcal E^C_I$. Iterating, $+1$.
$(2,0) = (\frac32,0)+ (\frac12,0)$ and $(3,0) = 2(\frac32,0)$. (b) $2\mathcal E^{\mathrm{tot}}_I = (\mathcal
E^{\mathrm{tot}}_I+(\mathcal E^{\mathrm{tot}}_I-1))+1\subset\mathcal E^C_I+1$, using only (3); and $(j+1)\mathcal
E^{\mathrm{tot}}_I\subset\mathcal E^C_I+(j-1)+ \mathcal E^{\mathrm{tot}}_I = (\mathcal E^C_I+(\mathcal
E^{\mathrm{tot}}_I-1))+j\subset\mathcal E^C_I+j$. (c) From (a): $\mathcal E^{\mathrm{tot}}_I+1\subset\mathcal E^C_I$;
the component sets are unions of $\mathcal E^C_I$ with some $(\frac32+s,0)$. (d) The added sets are $\{\frac32+s+j\}$;
for $j = 0$, $\frac32+s\le\frac32+2\gamma_\Upsilon$; for $j\ge1$,
$\frac32+s+j\in\mathcal E^{\mathrm{tot}}_I+1\subset\mathcal E^C_I$ by (a). (e) Put $\Sigma := \bigcup_s(\frac32+s,0)$,
$\mathcal E_{(0)} := \tilde{\mathcal E}$, and $\mathcal E_{(m+1)}$ the smallest index set containing $\mathcal E_{(m)}$
and $\mathcal E'_m+(\mathcal E'_m-1)$, $\mathcal E'_m := \mathcal E_{(m)}\cup\Sigma$. Each new element has real part at
least $\frac12$ more than an element it is built from, and the generators in $\{\mathrm{Re}\,z<C\}$ are finitely many;
so in each half plane $\{\mathrm{Re}\,z<C\}$ only finitely many elements arise, after at most $2C$ steps, with bounded
logarithmic orders. The union $\mathcal E^C_I$ is an index set; it satisfies (3) by construction, and (2) since new
elements have real part at least $\frac32+\frac12 = 2> \frac32+2\gamma_\Upsilon$ by (1.1). Every set satisfying (2)-(3)
and containing $\tilde{\mathcal E}$ contains each $\mathcal E_{(m)}$. $\square$

(`ext5.py` E4 builds the smallest $\mathcal E^C_I$ for four samples, with exact arithmetic up to real part 9, and checks
(a)-(d); with $\gamma_\Upsilon = \frac3{10}$ the minimality fails (2), as (1.1) predicts.)

**Definition 3.3 ([Hin26] Definition 5.4 at n = 4).** For $\mathcal E_0$ as in Definition 3.1 (1), $k\ge5$, $\ell_0>0$,
$\ell_I>\frac32$, $H^{k,(\mathcal E_0,\ell_0),\langle(3,0)\rangle_0,\ell_I}_{\mathrm b}(\Omega_{\mathrm{ext}})$ is the
space of $h$ with $\pi_Ch,\pi_{01}h,\pi_{1/}h,\slashed\pi_0h\in H^{k,(\mathcal E_0,\ell_0),((3,0),\ell_I)}_{\mathrm b}$
and $\pi_{11}h\in H^{k,(\mathcal E_0,\ell_0),((2,0),\ell_I)}_{\mathrm b}$ on $U$. By Lemma 3.2 (a) it lies in
$H^{k,(\mathcal E_0,\ell_0),\langle\mathcal E^C_I\rangle,\ell_I}_{\mathrm b}$ for every $\mathcal E^C_I$ of Definition
3.1. (The source's $\langle(2,0)\rangle_0$ has $(1,0)$ for $\slashed\pi_0$ and $\pi_{11}$. For $\pi_{11}$ that is the
mass order, $(2,0)$ here. For $\slashed\pi_0$ it is the radiation order; this class contains no radiation field of
$\slashed\pi_0$, and with $(\frac32,0)$ in slot 6, (5.3) below would fail. The source uses $\langle(2,0)\rangle_0$ to
subtract the radiation fields in its Theorem 5.21, Step 2 ((5.64), p. 104). III.C$'$ must either show the subtraction
unnecessary at $n = 4$, by (C1), or use a class with $(\frac32,0)$ in slot 6 and a weaker target: an obligation, (C7).)

**Definition 3.4 (the background class).** $\mathcal G$ is the set of Lorentzian metrics $g_0$ on
$\Omega_{\mathrm{ext}}$, smooth on $M$, with
$$g_0-\eta\in\rho_0^2\rho_I^2C^\infty(U;S^2T^*),\qquad\pi(g_0-\eta)\in\rho_0^2\rho_I^3C^\infty(U)\quad(\pi\in\{\pi_C,
\pi_{01},\pi_{1/},\slashed\pi_0\}),\tag{3.4}$$
equivalently $g_0-\eta\in H^{\infty,(2,0),\langle(3,0)\rangle_0,\infty}_{\mathrm b}(U)$ (the source's footnote 55, at
$n = 4$ and with $\eta$ for $g_m$). Proposition 4.4 uses only the first condition; the second matters for perturbations
measured from $g_b$ ((C5)).

**Lemma 3.5 ([Hin26] Remark 5.5 at n = 4).** (1) $g_b\in\mathcal G$ for every $b\in\mathcal B$. (2) For
$S\in\mathcal S_1$ small as in III.B Lemma 5.2,
$\phi_S^*g_b-g_b\in H^{\infty,(2,0),\langle(3,0)\rangle_0,\infty}_{\mathrm b}$ on
$U\cap\{\chi_{\mathrm{IVP}}(1-\chi_K) = 1\}$, so $\phi_S^*g_b$ agrees there with an element of $\mathcal G$.

*Proof.* (1) By III.B Proposition 3.6, $g_b-g_\mu\in|x|^{-3}C^\infty = \rho_0^3\rho_I^3C^\infty$, and on
$\{|x|\ge3R_1\}$, $g_\mu-\eta = \mu|x|^{-2}(dt-d|x|)^2 = \mu\rho_0^2\rho_I^2(dx^1)^2$, which has only the slot
$\pi_{11}$. (2) III.B Lemma 5.2: there $\phi_S^*g_b-g_b = |x|^{-2}h_S(\omega)(dx^1)^2+\rho_0^2\rho_I^3C^\infty$, with
$h_S\in C^\infty(\mathbb S^3)$. $\square$

Outside $\{\chi_{\mathrm{IVP}}(1-\chi_K) = 1\}$ near $I_0$, $\phi_S$ is the flow of a cut-off boost, and
$\phi_S^*\eta-\eta$ is of size $O(1)$ there: $\mathcal L_{V(S)}\eta = d\chi\otimes_sX_w^\flat$, with $d\chi$ of size
$|x|^{-1}$ and $X_w^\flat$ of size $|x|$. This is why the source modifies the gauge in its section 5.6 by $\chi_0$; it
is taken up in III.C$'$ (finding (C4)).

## 4. The structure at null infinity ([Hin26] Proposition 5.11, (5.40)-(5.41a) at n = 4)

The operator is that of III.B (6.8): for metrics $g,g_0$,
$$L^{g,g_0} := L_{g,g_0} = \tfrac12\Box_g+E^C_{g_0}\delta_gG_g+(\delta^*_{g_0}-\delta^*_g)\delta_gG_g+R_g+
\delta^*_{g_0,E_C}\big(C_{g,g_0}-Y_{g,g_0}+E^\Upsilon_{g_0}G_{g_0}\big),\tag{4.1}$$
the source's $D_1|_{(g,g_0)}P$, with $L^{g_b,g_b} = L_b$ of III.F (1.1).

**Lemma 4.1 (the background at the corner).** On $U$, in the frame of products of $dt_*,dx^i$,
$$L_b = -\rho_0^2\rho_I\big(X_I-\tfrac32-\bar S\big)(X_0-X_I)+\tilde R_b,\qquad\tilde R_b\in\rho_0^2\rho_I^2
\mathrm{Diff}^2_{\mathrm b}(U;S^2T^*),\tag{4.2}$$
with $\bar S$ the endomorphism of III.F Lemma 2.1 (2), and $\tilde R_b$ with coefficients in $C^\infty(U)$.

*Proof.* By III.F (2.2)-(2.3), on $\{|x|>3R_1\}$, $2L_b = -2\partial_{t_*}\rho(\rho\partial_\rho-\frac32-\bar S)+
\widehat{2\bar L}(0)-g_b^{00}\partial_{t_*}^2+Q_b\partial_{t_*}+R_b$, with
$\widehat{2\bar L}(0)\in\rho^2\mathrm{Diff}^2_{ \mathrm b}$, $g_b^{00}\in\rho^2C^\infty(\bar X)$,
$Q_b\in\rho^3\mathrm{Diff}^1_{\mathrm b}$, $R_b\in\rho^4\mathrm{Diff}^2_{ \mathrm b}$, all stationary b-operators on
$\bar X$: polynomials in $\rho\partial_\rho|_{t_*}$ and $\partial_\omega$ with coefficients in $C^\infty(\bar X)$. By
(1.4) these vector fields are b-vector fields on $U$ ($\partial_\omega$ at fixed $t_*,\rho$ is $\partial_\omega$ at
fixed $\rho_0,\rho_I$, as $t_*$ and $\rho$ do not depend on $\omega$), and $\rho = \rho_0\rho_I$,
$\partial_{t_*} = \rho_0(X_0-X_I)$. So the last four terms lie in $\rho_0^2\rho_I^2\mathrm{Diff}^2_{ \mathrm b}(U)$;
e.g. $g_b^{00}\partial_{t_*}^2\in\rho_0^4\rho_I^2\mathrm{Diff}^2_{\mathrm b}$. For the first, $(X_0-X_I) \rho = 0$, so
$$-2\partial_{t_*}\rho(\rho\partial_\rho-\tfrac32-\bar S) = -2\rho_0^2\rho_I(X_0-X_I)\big(X_I-\tfrac32-\bar S\big)-2
\rho_0^2\rho_I(X_0-X_I)\,8\mu_0\rho_0^2\rho_I(X_0-X_I),$$
and the second term lies in $\rho_0^4\rho_I^2\mathrm{Diff}^2_{\mathrm b}$. $\bar S$ is homogeneous of degree 0, a
function of $\omega$ in this frame, so it commutes with $X_0-X_I$. Halving gives (4.2). $\square$

As a check independent of III.F: for radial functions on $4+1$ Minkowski,
$\frac12\Box = 2\partial_u\partial_v+\frac32|x|^{-1}(\partial_u-\partial_v)$ ($u = x^1$, $v = x^0$) equals
$-\rho_0^2\rho_I(X_I-\frac32)(X_0-X_I)$ modulo $\rho_0^2\rho_I^2\mathrm{Diff}^2_{\mathrm b}$ with polynomial
coefficients (`ext5.py` E2; with $|x|^{-1}$ for $\frac32|x|^{-1}$ and 1 for $\frac32$, the source's (5.40), as its
four-dimensional control).

**Lemma 4.2 (the matrix $\bar A$).** In $\bar g$'s rescaled null frame $(dt_*+2d|x|,dt_*,|x|e^a)$, the image of the
products of $(dt_*,dx^i)$ under $F_0(\omega)$, $\bar S$ has a constant matrix $\bar A$; in $\eta$'s frame of (1.6) its
matrix is $\bar A$ modulo $\rho_0^2\rho_I^2C^\infty$ (Lemma 1.3). It is lower triangular, with diagonal
$$2(1-v_C)\gamma_C,\ (1-v_C)\gamma_C,\ (1-e_C)(1-v_C)\gamma_C,\ (1-e_\Upsilon)\gamma_\Upsilon,\ \gamma_\Upsilon,\ 0,\
2\gamma_\Upsilon,\tag{4.3}$$
and off-diagonal entries exactly at $(3,1)$, $(4,1)$, $(4,3)$, $(5,2)$, $(7,3)$, $(7,4)$, with
$\bar A_{74} = 2(1-e_\Upsilon)\gamma_\Upsilon$ and $\bar A_{76} = 0$. Each summand of (1.6) is mapped to summands of its
own type.

*Proof.* $\bar S$ commutes with the rotations of $\mathbb R^4$, which preserve $\bar g$, $t_*$, $c_C$ and $c_\Upsilon$
near infinity (III.B Definition 6.1), and (1.6) is rotation-equivariant. The stabiliser $SO(3)$ of $\omega$ acts on the
rank-1 summands trivially, on the two rank-3 summands by its standard representation, and on
$|x|^2\ker\slashed{\mathrm{tr}}$ by the irreducible 5-dimensional one. By Schur's lemma, $\bar S$ maps each summand to
the summands of the same type by scalars, and the scalars do not depend on $\omega$, as $SO(4)$ acts transitively on
$\mathbb S^3$. They are computed by `scri5.py` C1, which applies $\bar S$ (`sbar5.py`'s, built from (2.2) of III.F on
$4+1$ Minkowski) to an element of each summand at two points, finds the same matrix at both, lower triangular, each
summand mapped to its own type; its four-dimensional control reproduces the source's (5.28) at $h = 0$, all 49 entries.
`ext5.py` E3 reads off the support and the diagonal from `scri5.py`'s table, which C1 checks against the computation;
`scri5.py --only 1` is the check to run for the matrix itself. The diagonal is (3.1) of III.F, as the triangular
structure requires. $\square$

The trace couplings $(3,1)$, $(4,1)$, $(4,3)$, $(7,3)$ differ from the source's four-dimensional values (N1STAR-PROOF.md
10.38 (i)); only the support enters below.

**Lemma 4.3 (counting coefficients).** Let $g,g',g_0,g_0'$ be Lorentzian metrics on $U$ whose Cartesian components are
bounded with bounded inverses. In the Cartesian frame, $L^{g,g_0}-L^{g',g_0'}$ is a second-order operator
$\sum a^{\mu\nu}\partial_\mu\partial_\nu+\sum b^\mu\partial_\mu+c$ whose coefficients are sums of products of:
polynomials in the components of $g,g',g_0,g_0'$ and their inverses; at most two factors from
$\{\partial g,\partial g', \partial g_0,\partial g_0',c_C,c_\Upsilon,c_{\Upsilon,H}\}$, or one second derivative of one
of the metrics or one derivative of a $c$; and at least one factor $\delta$ from $\{g-g',g_0-g_0'\}$ or a Cartesian
derivative of it of order at most 2. Second-order coefficients contain no derivative; first-order ones at most one
derivative of order one or one $c$; and the $\delta$ factor counts towards these limits.

*Proof.* Each term of (4.1) is, in Cartesian coordinates, of the stated form for a single pair $(g,g_0)$: $\Box_g$ has
principal part $-g^{\mu\nu}\partial_\mu\partial_\nu$, first-order part with one Christoffel symbol and zeroth-order part
with one derivative of a Christoffel symbol or two of them; $E^C_{g_0}$ and $E^\Upsilon_{g_0}$ contain one $c$ and no
derivative (III.B (6.1)-(6.2)); $\delta_g$, $\delta^*_g$, $\delta^*_{g_0}$ are first order with one Christoffel symbol
in the zeroth-order part; $C_{g,g_0}$ and $Y_{g,g_0}$ are zeroth order with one first derivative of $g$ or $g_0$ (III.B
Lemma 6.3); $R_g$ is zeroth order with one second derivative or two first derivatives. Each coefficient of (4.1) is a
polynomial in $g$, $g^{-1}$, $g_0$, $g_0^{-1}$, their derivatives and the $c$'s. The difference of a polynomial
expression at two arguments is a sum of terms each with one difference factor, by $ab-a'b' = (a-a')b+a'(b-b')$ and
$g^{-1}-g'^{-1} = -g^{-1}(g-g')g'^{-1}$. $\square$

**Proposition 4.4 ([Hin26] Proposition 5.11 and (5.41a) at n = 4).** Let $k\ge5$, $\mathcal E_0$ as in Definition 3.1
(1), $\ell_0>0$, $\ell_I>0$, and let $\mathcal F$ be an index set with $\min\mathrm{Re}\,\mathcal F>0$ and
$2\mathcal F\subset \mathcal F$. Let $g_1,g_0\in\mathcal G$ and
$h\in H^{k,(\mathcal E_0,\ell_0),(\mathcal F,\ell_I)}_{\mathrm b}(U;S^2T^*)$ (every component), with
$\|h\|_{H^{k,a_0,a_I}_{\mathrm b}}<\epsilon_0$ for some $a_0,a_I>0$ with $h\in H^{k,a_0, a_I}_{\mathrm b}$,
$\epsilon_0>0$ small depending on $k,a_0,a_I$ and on $g_1$. Then $g := g_1+h$ satisfies, on $U$, in the splitting (1.6),
$$L^{g,g_0}\equiv-\rho_0^2\rho_I\big(X_I-\tfrac32-\bar A\big)(X_0-X_I)\bmod\big(\rho_0^2\rho_I^2C^\infty+H^{k-2,(\mathcal
E_0+2,\ell_0+2),(\mathcal F,\ell_I)}_{\mathrm b}\big)\mathrm{Diff}^2_{\mathrm b}(U;S^2T^*).\tag{4.4}$$
In particular this holds with $\mathcal F = \mathcal E^{\mathrm{tot}}_I$ for
$h\in H^{k,(\mathcal E_0,\ell_0), \langle\mathcal E^C_I\rangle,\ell_I}_{\mathrm b}$ (Lemma 3.2 (b)-(c)), and with
$\mathcal F = (2,0)$ for $h\in H^{k,(\mathcal E_0,\ell_0),\langle(3,0)\rangle_0,\ell_I}_{\mathrm b}$.

*Proof.* *The background.* By Lemma 4.1 and Lemma 1.3, conjugating by the frame change $F = F_0(\omega)(I+E)$,
$E\in \rho_0^2\rho_I^2C^\infty$: $F_0$ commutes with $X_0,X_I$, so $F_0^{-1}L_bF_0$ has leading part with
$F_0^{-1}\bar SF_0 = \bar A$ (Lemma 4.2); and $(I+E)^{-1}P(I+E)-P = (I+E)^{-1}[P,E]$, which for
$P\in\rho_0^2\rho_I\mathrm{Diff}^2_{\mathrm b}$ lies in $\rho_0^4\rho_I^3\mathrm{Diff}^1_{\mathrm b}$, as
$\mathcal V_{\mathrm b}$ preserves $\rho_0^2\rho_I^2 C^\infty$. So (4.4) holds for $(g,g_0) = (g_b,g_b)$ with remainder
in $\rho_0^2\rho_I^2C^\infty\mathrm{Diff}^2_{ \mathrm b}$.

*Counting.* Apply Lemma 4.3 to the difference of $L^{g,g_0}$ and $L_b$, with the conversion to b-operators: every
Cartesian derivative lies in $\rho_0\mathcal V_{\mathrm b}(U)$ (Lemma 1.1);
$c_C,c_\Upsilon\in|x|^{-1}C^\infty = \rho_0\rho_IC^\infty$ on $U$ (III.B Definition 6.1), and $c_{\Upsilon,H}$ is
supported in $\{|x|<5R_1\}$, a compact subset of $U$ away from $I_0\cup\mathscr I^+$; the Cartesian components of
$g_b,g_1,g_0$ and their inverses are smooth on $U$, and their Cartesian derivatives lie in $\rho_0C^\infty$. A term with
second-order derivatives is $a\,\partial_\mu\partial_\nu\in a\rho_0^2\mathrm{Diff}^2_{\mathrm b}$; a first-order term
has its $b^\mu$ containing one first derivative or one $c$, both in $\rho_0(\cdot)$, times
$\partial_\mu\in\rho_0\mathcal V_{\mathrm b}$; a zeroth-order term contains two such factors or one second derivative.
So each term is $\rho_0^2$ times a product of the $\delta$ factor, or of $\mathcal V_{\mathrm b}$-derivatives of it of
order at most 2, with smooth bounded functions and with other $\delta$ factors, applied through
$\mathrm{Diff}^2_{\mathrm b}$.

*The backgrounds.* For $(g_1,g_0)$ against $(g_b,g_b)$: $\delta\in\{g_1-g_b,g_0-g_b\}\subset\rho_0^2\rho_I^2C^\infty$
(Definition 3.4, Lemma 3.5 (1)), preserved by $\mathcal V_{\mathrm b}$; the terms lie in $\rho_0^4\rho_I^2C^\infty
\mathrm{Diff}^2_{\mathrm b}\subset\rho_0^2\rho_I^2C^\infty\mathrm{Diff}^2_{\mathrm b}$.

*The perturbation.* For $(g_1+h,g_0)$ against $(g_1,g_0)$: $\delta = h$, and
$(g_1+h)^{-1}-g_1^{-1} = \sum_{j\ge1}(-1)^j g_1^{-1}(hg_1^{-1})^j$. By Lemma 2.1 with $\gamma = (\ell_0,\ell_I)$ (the
strict inequalities hold, as $\min\mathrm{Re}\, \mathcal E_0,\min\mathrm{Re}\,\mathcal F,\ell_0,\ell_I>0$), the $j$-th
term lies in $H^{k,(j\mathcal E_0,\ell_0), (j\mathcal F,\ell_I)}_{\mathrm b}\subset H^{k,(\mathcal E_0,\ell_0),(\mathcal
F,\ell_I)}_{\mathrm b}$. For $j$ so large that $ja_0\ge\ell_0$ and $ja_I\ge\ell_I$, it lies in
$H^{k,\ell_0,\ell_I}_{\mathrm b}$ with norm at most $C(C\epsilon_0)^j$ (part (i) of Lemma 2.1's proof); so the series
converges for $C\epsilon_0<1$. Every coefficient of the difference is then $\rho_0^2$ times an element of
$H^{k-2,(\mathcal E_0,\ell_0),(\mathcal F,\ell_I)}_{\mathrm b}$ (Lemma 2.1 with $k-2>\frac52$, and (F1)); that is,
$H^{k-2,(\mathcal E_0+2,\ell_0+2),(\mathcal F,\ell_I)}_{\mathrm b}$. The frame change $F$ preserves both classes.
$\square$

The source's form (5.26a) at $n = 4$ is $L^{g,g_0}\equiv(2|x|^{-3/2}\partial_0|x|^{3/2}+|x|^{-1}\bar A)\partial_1$
modulo the same class, by (1.5):
$2\partial_0\partial_1+\frac32|x|^{-1}\partial_1\equiv-\rho_0^2\rho_I(X_I-\frac32)(X_0- X_I)$ and
$|x|^{-1}\bar A\partial_1\equiv\rho_0^2\rho_I\bar A(X_0-X_I)$.

**Remark 4.5 (the source's $A^h$, $B^h$, and Lemmas 5.6-5.8 at n = 4).** The source keeps $A^h-A_0\in
C^\infty+H^{k-1,(\mathcal E_0,\ell_0),(\mathcal E^{\mathrm{tot}}_I-1,\ell_I-1)}_{\mathrm b}$ and $B^h$ in the leading
part because at $n = 3$, $\min\mathrm{Re}(\mathcal E^{\mathrm{tot}}_I-1) = 0$: they are of the same order as $A_0$. At
$n = 4$ the same classes have $\min\mathrm{Re} = \frac12$, and Proposition 4.4 places them in the error, in the form
$\rho_0^2\rho_I\cdot\rho_I^{\mathcal E^{\mathrm{tot}}_I-1} = \rho_0^2\rho_I^{\mathcal E^{\mathrm{tot}}_I}$. The source's
Lemmas 5.6-5.8 and Corollaries 5.9-5.10 compute the entries of $A^h$, $B^h$ and the edge-b form; at $n = 4$ the b-form
needs only the memberships used in the proof above, which are their counterparts:
$g^{-1}-g_1^{-1}\equiv-g_1^{-1}hg_1^{-1}$ modulo $H^{k,(2\mathcal E_0,\ell_0),(2\mathcal F,\ell_I)}_{\mathrm b}$ (the
source's (5.11)); Cartesian Christoffel symbols
$\Gamma(g)-\Gamma(g_1)\in\rho_0H^{k-1,(\mathcal E_0,\ell_0),(\mathcal F,\ell_I)}_{\mathrm b}$ (its (5.12)); and
$\mathrm{Riem}(g)-\mathrm{Riem}(g_1)\in\rho_0^2H^{k-2,(\mathcal E_0,\ell_0), (\mathcal F,\ell_I)}_{\mathrm b}$ (its
Lemma 5.8). The edge-b form (5.26b) is in III.C$'$. Taking $\mathcal F = \mathcal E^{\mathrm{tot}}_I$ for every
component discards the component structure (e.g. the $\partial_1^2$ coefficient $g^{11}$ is tied to $h_{00}$, of index
$\mathcal E^C_I$); the b-form does not need it, but (5.26b) and III.C$'$'s energy estimates will. At tensor level the
half-order drop is consistent with `exterior5.py` X7 (N1STAR-PROOF.md 10.64), which computes the $h$-dependent entries
of [Hin23a]'s closely related operator at $n = 3$ and $n = 4$ and finds them $r^{-1/2}$ times the four-dimensional ones;
that operator omits the $\gamma_\Upsilon$ term, which carries one $c$ and obeys the same counting.

## 5. Forward mapping ([Hin26] Definition 5.13, Proposition 5.14, Corollary 5.15 at n = 4)

**Definition 5.1 ([Hin26] Definition 5.13 at n = 4).** Let $\mathcal E_0,\mathcal E^C_I$ be as in Definition 3.1,
$k\ge3$, $\ell_0>0$, $\ell_I>\frac32$.

(1) Set
$$\mathcal F_{I,11} := 1+\big(\mathcal E^C_I\cup(\tfrac32+(1-e_\Upsilon)\gamma_\Upsilon,0)\big).\tag{5.1}$$
$H^{k,(\mathcal E_0+2,\ell_0+2),\langle\mathcal E^C_I+1\rangle',\ell_I+1}_{\mathrm b}(\Omega_{\mathrm{ext}})$ is the
space of real symmetric 2-tensors $f$ with, on $U$, $\pi_Cf,\pi_{01}f,\pi_{1/}f,\slashed\pi_0f\in H^{k,(\mathcal E_0+2,
\ell_0+2),(\mathcal E^C_I+1,\ell_I+1)}_{\mathrm b}$ and
$\pi_{11}f\in H^{k,(\mathcal E_0+2,\ell_0+2),(\mathcal F_{I,11}, \ell_I+1)}_{\mathrm b}$.

(2) If $\ell_0<\min\mathrm{Re}\,\mathcal E_0$ we write $\ell_0+2$ for $(\mathcal E_0+2,\ell_0+2)$, and if
$\ell_I< \min\mathrm{Re}\,\mathcal E^C_I$ we write $(-',\ell_I+1)$ for $(\langle\mathcal E^C_I+1\rangle',\ell_I+1)$.

(3) $H^{k,(\mathcal E_0+2,\ell_0+2),\langle(4,0)\rangle',\ell_I+1}_{\mathrm b}(\Omega_{\mathrm{ext}})$:
$\pi_Cf,\pi_{01}f, \pi_{1/}f,\slashed\pi_0f$ in $((4,0),\ell_I+1)$ and $\pi_{11}f$ in $((3,0),\ell_I+1)$ at
$\mathscr I^+$, and $(\mathcal E_0+2,\ell_0+2)$ at $I_0$.

The source's $\mathcal F_{I,11}$ (5.43) also contains $1+(1,0)$, from the radiation field of $\slashed\pi_0$ through the
$h$-dependent (7,6) entry of $A^h$. At $n = 4$ that entry is part of the error of (4.4), and what it produces lies in
$\mathcal E^C_I+1$ (finding (C3)).

**Proposition 5.2 ([Hin26] Proposition 5.14 at n = 4).** Let $g = g_1+h$, $g_1,g_0\in\mathcal G$, with $h\in
H^{k,(\mathcal E_0,\ell_0),\langle\mathcal E^C_I\rangle,\ell_I}_{\mathrm b}(\Omega_{\mathrm{ext}})$ small as in
Proposition 4.4, $k\ge5$. Then
$$L^{g,g_0}:H^{k,(\mathcal E_0,\ell_0),\langle\mathcal E^C_I\rangle,\ell_I}_{\mathrm b}(\Omega_{\mathrm{ext}})\to
H^{k-2,(\mathcal E_0+2,\ell_0+2),\langle\mathcal E^C_I+1\rangle',\ell_I+1}_{\mathrm b}(\Omega_{\mathrm{ext}}),\tag{5.2}$$
continuously. If $h\in H^{k,(\mathcal E_0,\ell_0),\langle(3,0)\rangle_0,\ell_I}_{\mathrm b}$ (small), then
$$L^{g,g_0}:H^{k,(\mathcal E_0,\ell_0),\langle(3,0)\rangle_0,\ell_I}_{\mathrm b}(\Omega_{\mathrm{ext}})\to H^{k-2,
(\mathcal E_0+2,\ell_0+2),\langle(4,0)\rangle',\ell_I+1}_{\mathrm b}(\Omega_{\mathrm{ext}}).\tag{5.3}$$

*Proof.* Away from $U$ the spaces impose nothing beyond $H^k$ and $H^{k-2}$, and $L^{g,g_0}$ is a second-order operator
with coefficients in $H^{k-2}$; by (F2) of III.A it suffices to work on $U$. Let $\dot g$ be in the domain of (5.2).
Every slot of $\dot g$ lies in $H^{k,(\mathcal E_0,\ell_0),(\mathcal E^{\mathrm{tot}}_I,\ell_I)}_{\mathrm b}$ (Lemma 3.2
(c)). Split $L^{g,g_0}$ by (4.4) with $\mathcal F = \mathcal E^{\mathrm{tot}}_I$.

*The $C^\infty$ error.* $\rho_0^2\rho_I^2C^\infty\mathrm{Diff}^2_{\mathrm b}$ maps $\dot g$ into
$H^{k-2,(\mathcal E_0+2, \ell_0+2),(\mathcal E^{\mathrm{tot}}_I+2,\ell_I+2)}_{\mathrm b}$ in every slot, and
$\mathcal E^{\mathrm{tot}}_I+2\subset \mathcal E^C_I+1\subset\mathcal F_{I,11}$ (Lemma 3.2 (c)).

*The perturbation.* $H^{k-2,(\mathcal E_0+2,\ell_0+2),(\mathcal E^{\mathrm{tot}}_I,\ell_I)}_{\mathrm b}\mathrm{Diff}^2_{
\mathrm b}$ maps $\dot g$, by Lemma 2.1 and (F1), into
$H^{k-2,(2\mathcal E_0+2,\gamma_0),(2\mathcal E^{\mathrm{tot}}_I, \gamma_I)}_{\mathrm b}$ with $\gamma_0 = \ell_0+2$ and
$\gamma_I = \ell_I+1$. The strict inequalities of Lemma 2.1 hold: $\ell_0+2<\ell_0+2+\min\mathrm{Re}\,\mathcal E_0$, and
$\ell_I+1<\ell_I+\frac32 = \ell_I+\min\mathrm{Re}\,\mathcal E^{\mathrm{tot}}_I$, $\ell_I+1<2\ell_I$ as $\ell_I>\frac32$.
And $2\mathcal E_0+2\subset\mathcal E_0+2$, $2\mathcal E^{\mathrm{tot}}_I\subset\mathcal E^C_I+1$ (Lemma 3.2 (b)).

*The leading part.* $u := (X_0-X_I)\dot g$ has the slot index sets of $\dot g$ (F1). Then $w := (X_I-\frac32-\bar A)u$
has, in slot $j$, $(X_I-\frac32-\bar A_{jj})u_j-\sum_{i<j}\bar A_{ji}u_i$. In a slot with index set
$\mathcal E^C_I\cup(\frac32+s,0)$ and $\bar A_{jj} = s$, the term $\rho_I^{3/2+s}a(\rho_0,\omega)$ is annihilated:
$X_I-\frac32-s$ kills it, and the terms $\rho_I^{3/2+s+j}$, $j\ge1$, lie in $\mathcal E^C_I$ (Lemma 3.2 (d)). This holds
in slot 4 ($s = (1-e_\Upsilon)\gamma_\Upsilon$), slot 5 ($s = \gamma_\Upsilon$) and slot 6 ($s = 0$), and for the
$\frac32+2\gamma_\Upsilon$ term of slot 7. By Lemma 4.2 the couplings are $(3,1)$, $(4,1)$, $(4,3)$, $(5,2)$ and
$(7,3)$, from $\pi_C$ slots with index set $\mathcal E^C_I$, and $(7,4)$, which brings $\mathcal E_{I,01}$ into slot 7.
So $w_j\in(\mathcal E^C_I,\ell_I)$ at $\mathscr I^+$ for $j\le6$, and
$w_7\in(\mathcal E^C_I\cup(\frac32+(1-e_\Upsilon) \gamma_\Upsilon,0),\ell_I)$: the
$\frac32+(1-e_\Upsilon)\gamma_\Upsilon$ term of slot 7 itself is not annihilated, nor is that of slot 4 brought by
$(7,4)$. Multiplying by $-\rho_0^2\rho_I$ gives $\mathcal E^C_I+1$, resp. $\mathcal F_{I,11}$, at weight $\ell_I+1$, and
$\mathcal E_0+2$ at weight $\ell_0+2$ at $I_0$. Regularity: $H^{k-2}$.

(5.3): the slots of $\dot g$ have index sets $(3,0)$ (slots 1-6) and $(2,0)$ (slot 7). The leading part does not
annihilate $\rho_I^2$ in slot 7 ($2\ne\frac32+2\gamma_\Upsilon$) and gives $(2,0)$ there, $(3,0)$ elsewhere; the
couplings into slot 7 come from slots with $(3,0)$; after the factor $\rho_I$: $(3,0)$, $(4,0)$. The error gives
$(2,0)+2 = (4,0)$, and the perturbation, with $\mathcal F = (2,0)$, gives $(2,0)+(2,0) = (4,0)$.

`ext5.py` E5 repeats this bookkeeping slot by slot for four parameter samples, with exact arithmetic; it fails, as it
should, if $\bar A_{76}\ne0$ or if $\mathcal F_{I,11}$ omits $(\frac32+(1-e_\Upsilon)\gamma_\Upsilon,0)$. Continuity
follows from Lemma 2.1's. $\square$

**Corollary 5.3 ([Hin26] Corollary 5.15 at n = 4).** Let $g_0\in\mathcal G$ with $\mathrm{Ric}(g_0) = 0$, and $h\in
H^{k,(\mathcal E_0,\ell_0),\langle\mathcal E^C_I\rangle,\ell_I}_{\mathrm b}(\Omega_{\mathrm{ext}})$ small as in
Proposition 4.4, $k\ge5$. Then
$$P(g_0+h,g_0)\in H^{k-2,(\mathcal E_0+2,\ell_0+2),\langle\mathcal E^C_I+1\rangle',\ell_I+1}_{\mathrm b}(\Omega_{
\mathrm{ext}}),\tag{5.4}$$
and for $h\in H^{k,(\mathcal E_0,\ell_0),\langle(3,0)\rangle_0,\ell_I}_{\mathrm b}$ small,
$P(g_0+h,g_0)\in H^{k-2,(\mathcal E_0+2,\ell_0+2),\langle(4,0)\rangle',\ell_I+1}_{\mathrm b}$.

*Proof.* $P(g_0,g_0) = \mathrm{Ric}(g_0)-\delta^*_{g_0,E_C}\Upsilon^{E_\Upsilon}(g_0,g_0) = 0$, since
$\Upsilon^0(g_0,g_0) = 0$ and $E^\Upsilon_{g_0}G_{g_0}(g_0-g_0) = 0$ (III.B (6.3)-(6.4)). So
$$P(g_0+h,g_0) = \int_0^1L^{g_0+sh,g_0}h\,ds,\tag{5.5}$$
and Proposition 5.2 with $g_1 = g_0$ and the perturbation $sh$ applies for each $s\in[0,1]$, with bounds uniform in $s$.
The integrand is continuous in $s$ with values in the target space (the coefficients are polynomial in $s$ and in the
Neumann series of $(g_0+sh)^{-1}$), so the integral converges there. $\square$

The source states its Corollary 5.15 with $g = g_b+h$ and writes $P(g_b+h,g_0)$ through $\tilde h = h-(g_0-g_b)$
((5.48)). When $g_0\ne g_b$, $L(g_0-g_b)$ has $I_0$-index set $(2,0)+2$ at $n = 4$, which lies in $\mathcal E_0+2$ only
if $(2,0) \subset\mathcal E_0$. The statement is used with the perturbation measured from $g_0$ ((5.77a) of the source),
which is the form above (finding (C5)).

## 6. Findings, labels and sources

### 6.1 Findings

(C1) *The structure at $n = 4$ is simpler than the source's.* The perturbation's entries of (5.28), $A^h-A_0$ and $B^h$,
carry at least $\rho_I^{1/2}$ relative to $A_0$, and the Myers-Perry mass carries $\rho_0^2\rho_I^2$ at the corner. So
(4.4) has the constant lower-triangular $\bar A$ (Lemma 4.2), and its error has index set $\mathcal E^{\mathrm{tot}}_I$
in the perturbation part. The source's Lemmas 5.6-5.8 and Corollaries 5.9-5.10, which compute the $h$-entries, reduce to
the memberships of Remark 4.5. The structure is proved here from III.F Lemma 2.1 by the exact coordinate identities
(1.4), not by recomputing the Christoffel symbols. N1STAR-PROOF.md 10.38 (a) deduced the half-order drop by a scaling
argument; it is proved here.

(C2) *The source's last index condition is strengthened* to
$\mathcal E^{\mathrm{tot}}_I+(\mathcal E^{\mathrm{tot}}_I-1)\subset\mathcal E^C_I$, which implies its
$j\mathcal E^{\mathrm{tot}}_I$ condition. It absorbs the perturbation part of (4.4) acting on the radiation fields,
$\frac32+\frac12 = 2$. It forces $(2,0)\subset\mathcal E^C_I$ (the source's (5.9) has $(2,0)$ from $2(1,0)$) and needs
$\gamma_\Upsilon<\frac14$, so that $2>\frac32+2\gamma_\Upsilon$. At $n = 3$ the same condition would put $(1,0)$ into
$\mathcal E^C_I$, which is why the source carries $A^h$ instead. The smallness (1.1) joins III.G$'$'s
$\gamma_\Upsilon<\min(\frac12s_C,\frac38)$ as an obligation for Part VI: $\gamma_\Upsilon<\min(\frac12s_C,\frac14)$.

(C3) *$\pi_{11}h$ carries no radiation field at $n = 4$.* The source's $\mathcal E_{I,11}$ and $\mathcal F_{I,11}$
contain $(1,0)$, from the coupling of $\slashed\pi_0h$'s radiation field into the 11-component by the $h$-dependent
(7,6) entry of $A^h$ (his p. 98, and p. 169: "this coupling is absent when $h = 0$"), and from the mass term. At
$n = 4$, $\bar A_{76} = 0$ (Lemma 4.2), the $h$-dependent coupling is part of the error and lands at
$\frac32+\frac12 = 2\in\mathcal E^C_I$, and the mass term $\mu|x|^{-2}(dx^1)^2$ has index $(2,0)$. This proves, for the
exterior region, the reading of N1STAR-PROOF.md 10.38 (c), that the coupling reaches the 11-component at the Coulombic
order 2. It matches III.G$'$, where $\mathcal E_{\iota^+,\mathscr I,11}$ is the union of the sets for $2\gamma_\Upsilon$
and $(1-e_\Upsilon)\gamma_\Upsilon$.

(C4) *The source's Remark 5.5 holds where $\phi_S$ is the boost* (Lemma 3.5 (2)). Near $I_0$, where
$\chi_{\mathrm{IVP}} <1$, the cut-off flow changes $\eta$ at $O(1)$. The source's section 5.6 handles this by the
cut-off $\chi_0$ in the gauge (5.76), in III.C$'$.

(C5) *Corollary 5.15 is stated with the perturbation measured from $g_0$.* Measured from $g_b$ with $g_0\ne g_b$, the
conclusion needs $(2,0)\subset\mathcal E_0$ at $n = 4$ ($(1,0)$ at $n = 3$). The source's use, (5.77a), measures from
$g_0$.

(C6) *Products.* The source uses the Sobolev algebra property of $H^{k-2}_{\mathrm b}$,
$k-2>\frac12\dim\Omega_{\mathrm {ext}}$, without proof (its remark (vii)), and with it the products of partially
polyhomogeneous functions. Lemma 2.1 proves the form used, with its strict inequalities on the weights; every use here
has room to spare.

### 6.2 Labels

Proved: Lemmas 1.1, 1.3, 2.1, 3.2, 3.5, 4.1-4.3, Proposition 4.4, Proposition 5.2, Corollary 5.3, given the parts cited.
Computed (exact): `ext5.py` E1-E5 and `scri5.py` C1, each with controls. READ: the source's statements and remarks
quoted from pp. 84-99 and 169. Inputs from other parts: III.A (F1)-(F2) and the spaces of [Hin26] Definition 2.8; III.B
(2.2), (3.6), Proposition 3.6, Lemma 4.1, (4.4), Lemma 5.2, Definition 6.1, Lemma 6.3; III.F (1.1), Lemma 2.1, Lemma
3.1.

### 6.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 5 (pp. 84-113), here
pp. 84-99 (Definitions 5.1-5.4, Remark 5.5, Lemmas 5.6-5.8, Corollaries 5.9-5.10, Proposition 5.11 with (5.25)-(5.28)
and (5.40)-(5.42), Definition 5.13 with (5.43), Proposition 5.14, Corollary 5.15 with (5.48)) and p. 169.
N1STAR-PROOF.md 10.38 and 10.64. `ext5.py` (this part), `scri5.py` C1, `sbar5.py`.

(C7) *An obligation for III.C$'$* (Definition 3.3): the source's Theorem 5.21, Step 2, subtracts the radiation fields of
$\slashed\pi_0h$ and $\pi_{11}h$ through $g_0' = g_b+h_0$, $h_0\in\langle(2,0)\rangle_0$, and uses Corollary 5.15 (2)
for $P(g_0',g_b)$. At $n = 4$ the class $\langle(3,0)\rangle_0$ carries no radiation field of $\slashed\pi_0$. III.C$'$
must either show the subtraction unnecessary, as (C1) suggests, or use a class with $(\frac32,0)$ in slot 6.

### 6.4 The hundred-and-first verifier (D244)

The hundred-and-first verifier (Opus) read this part in full: no major finding, four minor, six nits, all seated. (m1)
Definition 3.3 dropped the radiation allowance of the source's $\langle(2,0)\rangle_0$ for $\slashed\pi_0$ silently: now
stated, with the obligation (C7). (m2) $\bar A$ is exactly constant in $\bar g$'s null frame, and in $\eta$'s only
modulo $\rho_0^2\rho_I^2C^\infty$: Lemma 4.2 restated (Proposition 4.4's proof already handled it). (m3) `ext5.py` E3
reads `scri5.py`'s table: said so, with `scri5.py --only 1` as the check; a third control of E5 shows the strengthened
index condition is needed; the tensor-level half-order drop is cross-checked against `exterior5.py` X7 (Remark 4.5).
(m4) The index condition strengthens the source's and implies its $j\mathcal E^{\mathrm{tot}}_I$ condition: Definition
3.1 (3), Lemma 3.2 (b), (e) and (C2) say so. Nits: $U$ meets $\Sigma^{\mathrm{past}}$; $\rho_0\in[0,1]$; $x^0$ against
III.B (4.1); polynomials, not smooth functions, in Lemma 4.3; $\chi^2-\chi$ in Lemma 2.1; the discarded component
structure (Remark 4.5); the second condition of Definition 3.4. The verifier found the counting of Proposition 4.4
right, including the terms the source puts in $A^h$, so N1STAR-PROOF.md 10.38 (a)'s scaling deduction is proved.