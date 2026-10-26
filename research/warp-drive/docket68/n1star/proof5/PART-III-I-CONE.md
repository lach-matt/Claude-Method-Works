# Part III.I. The dynamical linearised operator at n = 4 ([Hin26] section 11 opening and 11.1)

*Status.* Proved (D258: the hundred-and-eighth verifier read the D256 repairs and found them correct). Verified (D254:
the hundred-and-sixth verifier; one major and two minor findings and eight nits seated. D256: the hundred-and-seventh
verifier read the repairs; one residual minor finding and two nits seated, to be read). Written (D251). This part
proves, at spatial dimension $n = 4$, [Hin26] section 11's setting and section 11.1 (pp. 218-226): the classes of metric
perturbations and source terms (Definition 11.3), the edge-3b membership of the perturbations (Lemma 11.5), the
structure of the linearised gauge-fixed Einstein operator $L^{g,g_0}$ in the forward cone (Proposition 11.6, Remark
11.7), its forward mapping properties (Proposition 11.8, Corollary 11.9), its admissibility relative to $L_b$ (Corollary
11.10), and the regularity of forward solutions (Theorem 11.12, at $b_0$), with the compatibility between Part II.F$'$'s
orders and those of III.H$'$ that the latter left as an obligation.

*What n = 4 changes.* The perturbation's contributions to the operator at null infinity are half an order lower than
the constant matrix $\bar A$ (III.C (C1)); so the dynamical operator is admissible with $p_0 = \tilde p_1 = 0$ in II.C
Definition 3.3, and the source's restriction $\ell_I<2\gamma_\Upsilon$ disappears (Lemma 2.2). At $\iota^+$ the
background differences (mass, rotation, cut-off boost) are of order 2 (III.B Proposition 3.6, Lemma 5.2), the source's 1,
and the curvature of the patched background is of order 4 (Lemma 4.3), the source's 3. The forward solutions of Theorem
5.3 have sf-loss 0 (III.H$'$), and their weights at $\mathscr I^+$ reach $\frac32$, the order of a radiation field.
Theorem 11.12 is proved here at $b_0$; for $b\ne b_0$ two inputs are open ((I3)). Notation: Parts II.A, II.C, II.F$'$,
III.B, III.C, III.F and III.H$'$; no instrument is used.

## 1. Setting ([Hin26] (11.1)-(11.11) at n = 4)

*Background.* For $b$ near $b_0$ and $S\in\mathcal S_1$ small, with the cut-offs and boosts of III.B section 5,
$$g_{b_0,b,-S} := (1-\chi_K)\phi_{-S}^*g_{b_0}+\chi_Kg_b\tag{1.1}$$
(the source's (11.1)). The cut-offs are moreover taken with (the source's (11.5))
$$\mathrm{supp}\,\chi^\flat_K\subset\chi_K^{-1}(1)\subset\mathrm{supp}\,\chi_K\subset(\chi^\sharp_K)^{-1}(1)\subset
\mathrm{supp}\,\chi^\sharp_K\subset\{t^\flat_*\ge10\},\tag{1.2}$$
a further condition of the same kind as III.B's (supports in $\{t>T\}$ with $T$ large), compatible with them.

*Time function and domain.* $t^\flat_*$ is the function of II.C Lemma 3.2 with $\ell = \ell_I = \frac12$, built for
$g_{b_0}$ (the source's (11.3)), and $\Omega_* := \mathrm{cl}_M\{t^\flat_*\ge1\}\subset\Omega = \mathrm{cl}_M\{t_*\ge1\}$
(the source's (11.4)). $L^2$-based spaces on $\Omega_*$ use the unweighted b-density $\mu_{\mathrm b}
= |dt_*\,dx|/(t_*\langle x\rangle^4)$ (II.F$'$ Corollary 1.2; the source's $t_*^{-1}\langle x\rangle^{-3}|dt_*dx|$), and
weights are listed at $(\mathscr I^+,\iota^+,K^+)$ with the defining functions $\rho_I,\rho_+,\rho_K$ of III.B (2.2).

**Definition 1.1 ([Hin26] Definition 11.3 at n = 4).** Let $\mathcal E_+\subset\mathbb C\times\mathbb N_0$ be an index
set with
$$(2,0)\in\mathcal E_+,\qquad\min\mathrm{Re}\,\mathcal E_+>1,\qquad j\mathcal E_+\subset\mathcal E_+\ (j\in\mathbb N),
\tag{1.3}$$
and let $\mathcal E^C_I$ satisfy III.C Definition 3.1 (2)-(3), with $\mathcal E^{\mathrm{tot}}_I$, $\mathcal E_{I,01}$,
$\mathcal E_{I,1/}$, $\slashed{\mathcal E}_{I,0}$, $\mathcal E_{I,11}$ and $\mathcal F_{I,11}$ as there ((3.1)-(3.2),
(5.1)). Let $\ell_I,\ell_+,\ell_K\in\mathbb R$.

(1) For $k\ge5$, $H^{k,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_+,\ell_+),\ell_K}_{\mathrm b}(\Omega_*)$ is the
space of real symmetric 2-tensors $h$ whose slot components (III.C Definition 1.2, near $\mathscr I^+$) lie in
$H^{k,(\mathcal E,\ell_I),(\mathcal E_+,\ell_+),\ell_K}_{\mathrm b}$ with $\mathcal E = \mathcal E^C_I$ for $\pi_C$,
$\mathcal E_{I,01}$ for $\pi_{01}$, $\mathcal E_{I,1/}$ for $\pi_{1/}$, $\slashed{\mathcal E}_{I,0}$ for $\slashed\pi_0$,
$\mathcal E_{I,11}$ for $\pi_{11}$ (III.C (3.3) with $\iota^+$ in place of $I_0$).

(2) For $k\ge3$, $H^{k,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),(\mathcal E_++2,\ell_++2),\ell_K}_{\mathrm
b}(\Omega_*)$ is the space of $f$ with $\pi_Cf,\pi_{01}f,\pi_{1/}f,\slashed\pi_0f$ in $(\mathcal E^C_I+1,\ell_I+1)$ and
$\pi_{11}f$ in $(\mathcal F_{I,11},\ell_I+1)$ at $\mathscr I^+$, all in $(\mathcal E_++2,\ell_++2)$ at $\iota^+$ and of
weight $\ell_K$ at $K^+$ (III.C Definition 5.1).

(3) $H^{k,(\langle(3,0)\rangle_0,\ell_I),(\mathcal E_+,\ell_+),\mathcal E_K}_{\mathrm b}(\Omega_*)$ is III.C Definition
3.3's class at $\mathscr I^+$ ($(3,0)$ for the slots but $\pi_{11}$, $(2,0)$ for $\pi_{11}$), with $(\mathcal
E_+,\ell_+)$ at $\iota^+$ and the index set $\mathcal E_K$ at $K^+$.

The source has $(1,0)\in\mathcal E_+$ and $\min\mathrm{Re}\,\mathcal E_+\ge1$: $(1,0)$ is the $\iota^+$-order of its
background differences, which at $n = 4$ is 2 (Lemma 3.6); $\min\mathrm{Re}\,\mathcal E_+>1$ is what Lemma 2.2 and
Proposition 4.1 use, and later parts may raise it (the radiative $\frac32+(1-e_\Upsilon)\gamma_\Upsilon$ of
N1STAR-PROOF.md 10.44 (e) lies above it).

*The class of perturbations.* With parameters $a_I>\frac32$, $a_+>1$, $a_K>2$, put
$$\mathcal X^k := H^{k,(\langle\mathcal E^C_I\rangle,a_I),(\mathcal E_+,a_+),a_K}_{\mathrm
b}(\Omega_*;S^2T^*).\tag{1.4}$$
The source fixes $(a_I,a_+,a_K) = (3+\epsilon_I,3+\epsilon_+,2+\epsilon_K)$ ((11.9)-(11.10)) for the iteration of its
sections 11.2-11.8; at $n = 4$ that choice belongs to the parts that write those sections, and this part needs only the
inequalities stated ((I5)).

## 2. The edge-3b class ([Hin26] Lemma 11.5 at n = 4)

On $M_{1/2}$ (III.B Definition 2.1) put $x_I := \rho_I^{1/2}$. Near $\mathscr I^+$, with the null coordinates
$x^0 = t+|x|$, $x^1 = t-|x|$ and $r\,d\omega$ the rescaled angular coframe,
$$x_I^2(dx^0)^2,\quad dx^0\otimes_sdx^1,\quad x_I\,dx^0\otimes_sr\,d\omega,\quad x_I^{-2}(dx^1)^2,\quad
x_I^{-1}dx^1\otimes_sr\,d\omega,\quad r\,d\omega\otimes_sr\,d\omega\tag{2.1}$$
span $x_I^{-2}\rho_+^{-2}C^\infty(\Omega_{*,1/2};S^2\,{}^{e3b}T^*M_{1/2})$, and (2.1) with the factors of $x_I$ dropped
away from $\mathscr I^+$ is a global frame (the source's (11.13)).

**Lemma 2.1.** (2.1) is a frame of $x_I^{-2}\rho_+^{-2}C^\infty(S^2\,{}^{e3b}T^*)$ over $\Omega_{*,1/2}$.

*Proof.* By II.A Lemma 2.5 (as used in II.C Lemma 3.2's proof), near $\mathscr I^+$ the covectors $e_1 := x_I^{-1}dt_*$,
$e_2 := x_Idr$ and $r\,d\omega$ span $\rho_+^{-1}x_I^{-1}C^\infty({}^{e3b}T^*)$. With $dt_* = dx^1+O(|x|^{-2})d|x|$
(III.C Lemma 1.3's proof) and $dr = d|x|$: $x_I^{-1}dx^1 = e_1+O(\rho^2x_I^{-2})e_2$ and $x_Idx^0 =
x_I^2e_1+2e_2+O(\rho^2)e_2$, an invertible smooth change of frame ($\rho = |x|^{-1}$, $\rho^2x_I^{-2} =
\rho_+^2\rho_I\le1$). Symmetric products give (2.1). Away from $\mathscr I^+$, $x_I$ is bounded below and the same
products of $dt,dx^i$ span; near $K^+$ they span $x_I^{-2}\rho_+^{-2}S^2\,{}^{e3b}T^*$ themselves, with no rescaling by
$\langle x\rangle$ (II.C section 5.1). $\square$

**Lemma 2.2 ([Hin26] Lemma 11.5 at n = 4).** Let $h\in\mathcal X^k$, $k\ge3$. Then $h\in\tilde{\mathcal
G}^{k-3,(2\ell_I,\ell_+,\ell_K)}_{\mathrm b}$ (II.C Definition 3.1) for every
$$\ell_I\in(0,\tfrac12],\qquad\ell_+\in(0,1],\qquad\ell_K\in(0,a_K],\tag{2.2}$$
with $\|h\|_{\tilde{\mathcal G}^{k-3,(2\ell_I,\ell_+,\ell_K)}_{\mathrm b}}\le C\|h\|_{\mathcal X^k}$. The source needs
$\ell_I<\min(2\gamma_\Upsilon,\frac12)$ and $\ell_+<1$.

*Proof.* b-Sobolev embedding for $\mu_{\mathrm b}$ ($\dim M = 5$, three derivatives) gives, slot by slot, sup bounds with
$k-3$ b-derivatives: at $\mathscr I^+$ by the least real part of the slot's index set (the expansion terms) or by $a_I$,
whichever is smaller; at $\iota^+$ by $\min(a_+,\min\mathrm{Re}\,\mathcal E_+)-\epsilon>1\ge\ell_+$ for $\epsilon$
small; at $K^+$ by $a_K\ge\ell_K$. In powers of $x_I$, the slot components are: $h_{00},h_{0\bar
a},\slashed{\mathrm{tr}}h$ of order $>3+4\gamma_\Upsilon$; $h_{01}$ and $h_{11}$ of order
$\ge3+2(1-e_\Upsilon)\gamma_\Upsilon$; $h_{1\bar a}$ of order $\ge3+2\gamma_\Upsilon$; $\slashed\pi_0h$ of order 3
(Definition 1.1 (1), III.C (3.2)). The coefficients of $h$ in the frame (2.1) are $x_I^{-2}h_{00}$, $h_{01}$,
$x_I^{-1}h_{0\bar a}$, $x_I^2h_{11}$, $x_Ih_{1\bar a}$ and $h_{\bar a\bar b}$, of $x_I$-orders at least
$1+4\gamma_\Upsilon$, 3, $2+4\gamma_\Upsilon$, 5, 4 and 3, all $\ge1\ge2\ell_I$. These are the index sets' orders; where
$a_I$ is smaller, a slot has $x_I$-order $2a_I$ (less $\epsilon$ for logarithms), and the least coefficient order is
then $2a_I-2-\epsilon>1$, so the conclusion stands. Away from $\mathscr I^+$ the coefficients are the Cartesian
components times bounded factors. So the coefficients lie in $C^{k-3,(2\ell_I,\ell_+,\ell_K)}_{\mathrm b}$, which is the
claim. $\square$

At $n = 3$ the coefficient $x_I^{-2}h_{00}$ has order $4\gamma_\Upsilon$, which is the source's
$\ell_I<2\gamma_\Upsilon$; at $n = 4$ the extra $x_I$ of the radiation order $\frac32$ removes it.

As in the source (its footnote 103), $\ell_I$ is an e3b weight in Lemma 2.2, Corollary 5.2 and Theorem 5.3's proof, and
a b-weight at $\mathscr I^+$ in Definition 1.1 and Proposition 4.1; the two are not compared.

*Consequences.* By Lemma 2.2 with $\ell_I = \frac12$ and II.C Lemma 3.2, $dt^\flat_*$ is past timelike for
$g = g_{b_0,b,-S}+h$ when $|b-b_0|$, $|S|$ and $\|h\|_{\mathcal X^4}$ are small: $g-g_{b_0} = (g_{b_0,b,-S}-g_{b_0})+h$,
and $g_{b_0,b,-S}-g_{b_0}$ is small in $\tilde{\mathcal G}^{0,(1,0,0)}_{\mathrm e3b}$ (Lemma 3.6 with Lemma 2.2's
argument; it vanishes at $b = b_0$, $S = 0$ and depends continuously on $(b,S)$). Such $g$ lie in $\mathcal
G^{(0;k-3),(2\ell_I,\ell_+,\ell_K)}_{e3b;b}$ relative to $g_b$ (the source's "asymptotically Kerr", [Hin26c] Definition
5.15). Smallness of $h$ in $H^{3,(1,0,0)}_{\mathrm b}$ makes $x_I^2\rho_+^2g$ non-degenerate Lorentzian (II.C Definition
3.1, Remark (b)): by Lemma 2.2's coefficients, weight 1 at $\mathscr I^+$ suffices (the source's footnote 104).

## 3. The structure in the forward cone ([Hin26] Proposition 11.6, Remark 11.7 at n = 4)

*Coordinates.* On $U^+ := \Omega_*\cap\{|x|\ge4R_1\}$ put
$$\rho_+ := \frac1{t_*+1},\qquad\rho_I := \frac{t_*+1}{|x|},\qquad\rho := |x|^{-1} = \rho_+\rho_I,\qquad X_+ :=
\rho_+\partial_{\rho_+},\ X_I := \rho_I\partial_{\rho_I}.\tag{3.1}$$
These are smooth coordinates with $\omega$ near $\mathscr I^+\cap\iota^+$, positive multiples (smooth, by III.B (2.2) and
$t_* = t-|x|+C'-8\mu_0|x|^{-1}$ on $\{|x|\ge3R_1\}$) of III.B's $\rho_+$, $\rho_I$ there; so they define the same faces
and b-structure.

**Lemma 3.1 (the vector fields).** On $U^+_C := U^+\cap\{\rho_I\le C\}$, $C\ge1$ fixed, exactly,
$$\partial_{t_*}|_{\rho,\omega} = -\rho_+(X_+-X_I),\qquad\rho\partial_\rho|_{t_*,\omega} = X_I.\tag{3.2}$$
Cartesian derivatives $\partial_t$, $\partial_{x^i}$ lie in $\rho_+\mathcal V_{\mathrm b}(U^+_C)$, and
$|x|^{-1}\partial_\omega\in\rho_+\rho_I\mathcal V_{\mathrm b}(U^+_C)$. Near $K^+$ ($\rho_I\to\infty$) (3.1) are not
coordinates, and the weights there are III.B's; Lemma 3.2 and Propositions 3.3-3.4 use Lemma 3.1 near $\mathscr
I^+\cup(\iota^+)^\circ$ only, Proposition 3.4 treating $K^+$ separately (D254).

*Proof.* At fixed $\rho$, $\partial_{t_*}\rho_+ = -\rho_+^2$ and $\partial_{t_*}\rho_I = \rho = \rho_+\rho_I$; at fixed
$t_*$, $\rho_+$ is constant and $\rho_I\propto\rho$. Then $\partial_t|_x = \partial_{t_*}|_x$, and $\partial_{|x|}|_t =
\partial_{|x|}|_{t_*}-\psi'(|x|)\partial_{t_*}$ with $\partial_{|x|}|_{t_*} = -\rho\cdot\rho\partial_\rho =
-\rho_+\rho_IX_I$ and $\psi'$ bounded; $\partial_{x^i} = \omega^i\partial_{|x|}+|x|^{-1}(\cdot)\partial_\omega$ and
$|x|^{-1}\partial_\omega =
\rho_+\rho_I\partial_\omega$. $\square$

**Lemma 3.2 (the background in the cone).** On $U^+\cap\{\rho_I\le1\}$, in the frame of products of $dt_*,dx^i$,
$$L_b = \rho_+^2\rho_I(X_+-X_I)\big(X_I-\tfrac32-\bar S\big)+\tilde R_b,\qquad\tilde R_b\in\rho_+^2\rho_I^2
\mathrm{Diff}^2_{\mathrm b}(U^+;S^2T^*),\tag{3.3}$$
with $\bar S$ of III.F Lemma 2.1 (2) and $\tilde R_b$ with coefficients smooth on $U^+$.

*Proof.* III.C Lemma 4.1's proof with (3.2) in place of III.C (1.4): $2L_b = -2\partial_{t_*}\rho(\rho\partial_\rho-
\frac32-\bar S)+\widehat{2\bar L}(0)-g_b^{00}\partial^2_{t_*}+Q_b\partial_{t_*}+R_b$ (III.F (2.2)-(2.3)), the last four
in $\rho^2\mathrm{Diff}^2_{\mathrm b}$ with $\rho = \rho_+\rho_I$, the vector fields $\rho\partial_\rho|_{t_*}$,
$\partial_\omega$ being b-vector fields on $U^+$, and $\partial_{t_*}\in\rho_+\mathcal V_{\mathrm b}$. The first is
$2\rho_+(X_+-X_I)\rho_+
\rho_I(X_I-\frac32-\bar S) = 2\rho_+^2\rho_I(X_+-X_I)(X_I-\frac32-\bar S)$, as $(X_+-X_I)(\rho_+\rho_I) = 0$ and $\bar S$
depends on $\omega$ only. $\square$

This is III.C (4.2) with $\rho_+$ for $\rho_0$ and $-(X_+-X_I)$ for $X_0-X_I$; the source's (11.17a) has $1$ for
$\frac32$ and the $h$-dependent $A^h$, $B^h$.

*The background class in the cone.* $\mathcal G^+$ is the set of Lorentzian $g_0$ on $\Omega_*$, smooth on $M$, with, on
$U^+\cap\{\rho_I\le1\}$, $g_0-\eta\in\rho_+^2\rho_I^2C^\infty$ and $\pi(g_0-\eta)\in\rho_+^2\rho_I^3C^\infty$ for
$\pi\ne\pi_{11}$ (III.C Definition 3.4 with $\rho_+$ for $\rho_0$).

**Proposition 3.3 ([Hin26] Proposition 11.6 (1) at n = 4).** Let $g_1,g_0\in\mathcal G^+$, $k\ge5$, and
$h\in\mathcal X^k$ with small $H^{3,(1,0,0)}_{\mathrm b}$-norm (the expansion of $g^{-1}$ after Proposition 3.4 replaces
III.C Proposition 4.4's Neumann series). Then $g := g_1+h$ satisfies, on $U^+\cap\{\rho_I\le1\}$, in the splitting III.C
(1.6),
$$L^{g,g_0}\equiv\rho_+^2\rho_I(X_+-X_I)\big(X_I-\tfrac32-\bar A\big)\bmod\big(\rho_+^2\rho_I^2C^\infty+H^{k-2,
(\mathcal E^{\mathrm{tot}}_I,a_I),(\mathcal E_++2,a_++2)}_{\mathrm b}\big)\mathrm{Diff}^2_{\mathrm b}.\tag{3.4}$$
For $h\in H^{k,(\langle(3,0)\rangle_0,a_I),(\mathcal E_+,a_+),\cdot}_{\mathrm b}$ the same holds with $(2,0)$ for
$\mathcal E^{\mathrm{tot}}_I$.

*Proof.* III.C Proposition 4.4's proof on $U^+$, with Lemmas 3.1-3.2 for III.C Lemmas 1.1 and 4.1: the frame change
(III.C Lemma 1.3, with $\rho^2 = \rho_+^2\rho_I^2$) turns $\bar S$ into $\bar A$ (III.C Lemma 4.2); the backgrounds
$(g_1,g_0)$ against $(g_b,g_b)$ differ by $\rho_+^2\rho_I^2C^\infty$, which with two factors $\rho_+$ from the
derivatives gives $\rho_+^4\rho_I^2C^\infty\mathrm{Diff}^2_{\mathrm b}$; and the perturbation, counted by III.C Lemma
4.3 with Cartesian derivatives in $\rho_+\mathcal V_{\mathrm b}$ (Lemma 3.1) and
$c_C,c_\Upsilon\in\rho_+\rho_IC^\infty$, gives $\rho_+^2$ times $H^{k-2}$ functions of the index sets of $h$: $\mathcal
E^{\mathrm{tot}}_I$ at $\mathscr I^+$ (III.C Lemma 3.2 (b)-(c)), $\mathcal E_+$ at $\iota^+$ ($j\mathcal
E_+\subset\mathcal E_+$ for the Taylor terms of $g^{-1}$, III.C Lemma 2.1 with the weights $(a_I,a_+)$). $\square$

So, as at $I_0\cap\mathscr I^+$, the leading part has the constant lower-triangular $\bar A$ and no $h$-dependent term;
the source's $A^h-A_0$ and $B^h$ are part of the error, of $\mathscr I^+$-order $\frac32$ against the leading $1$ (III.C
(C1)). The source's edge-b form (11.17b) is not carried: Corollary 5.2 uses (3.7) instead, as III.C defers (5.26b) to
III.C$'$.

**Proposition 3.4 ([Hin26] Proposition 11.6 (2) at n = 4).** Let $g_0 = g_{b_0,b,-S}$, or more generally $g_0\in\mathcal
G^+$ with (the source's (11.15a)-(11.15b))
$$g_0-g_{\mu_0}\in H^{\infty,(\langle(3,0)\rangle_0,\infty),((2,0),\infty),(0,0)}_{\mathrm b}(\Omega_*),\qquad g_0 = g_b
\text{ near }K^+,\tag{3.5}$$
let $h\in\mathcal X^k$, $k\ge5$, with small $H^{3,(1,0,0)}_{\mathrm b}$-norm, and $g := g_{b_0,b,-S}+h$ (the source's
(11.16)). Then on $\Omega_*$
$$L^{g,g_0}-L_b\in H^{k-2,(\mathcal E^{\mathrm{tot}}_I,a_I),(\mathcal E_++2,a_++2),a_K}_{\mathrm
b}\mathrm{Diff}^2_{\mathrm
b}(\Omega_*;S^2T^*),\tag{3.6}$$
$$2L^{g,g_0}-2L_b\in x_I^2\rho_+^2H^{k-2,(2\ell_I,\ell_+,\ell_K)}_{\mathrm b}\mathrm{Diff}^2_{e3b}(\Omega_*;S^2T^*)
\quad\text{for (2.2)'s }\ell_I,\ell_+,\ell_K,\tag{3.7}$$
the latter with norm bounded by $C(|b-b_0|+|S|+\|h\|_{\mathcal X^k})$, $C$ depending on $k$ and on an upper bound for
$\|h\|_{\mathcal X^k}$.

The source's (11.18a)-(11.18b) carry, in addition, the term
$\chi_I\rho_I\rho_+^2((A^h-A_0)(\rho_I\partial_{\rho_I}-\rho_+
\partial_{\rho_+})+\rho_+^{-1}B^h)$, which contains a leading-order term at $\mathscr I^+$; at $n = 4$ it is part of the
error.

*Proof.* Write $g-g_b = (g_{b_0,b,-S}-g_b)+h$ and $g_0-g_b$. By Lemma 3.6 below, $g_{b_0,b,-S}-g_b$ is supported where
$\chi_K<1$, so away from $K^+$, and lies in $H^{\infty,(\langle(3,0)\rangle_0,\infty),((2,0),\infty),\infty}_{\mathrm
b}\subset\mathcal X^\infty$ (III.C Definition 3.3 and Lemma 3.2 (a); $(2,0)\in\mathcal E_+$); the same holds for
$g_0-g_b$ under (3.5). So both differences are of the class of $h$, and III.C Lemma 4.3 applies to
$L^{g,g_0}-L^{g_b,g_b}$ with $\delta$ in $\mathcal X^k$. Cartesian derivatives lie in $\rho_+\mathcal V_{\mathrm b}$
near $\mathscr I^+\cup\iota^+$ (Lemma 3.1, and in the interior of $\iota^+$ by homogeneity) and in $\rho_+\mathcal
V_{3b}\subset\rho_+\mathcal V_{\mathrm b}$ near $K^+$ (the source's proof); the counting gives $\rho_+^2$ times
$H^{k-2}$ functions of the class of $\mathcal X^k$, which is (3.6) ($\rho_+^2$ shifts the $\iota^+$ data by 2; at $K^+$,
$\rho_+^2$ is bounded and the weight is $a_K$). For (3.7): near $\mathscr I^+$, $\partial_0\in x_I^2\rho_+\mathcal
V_{e3b}$, $\partial_1\in\rho_+\mathcal V_{e3b}$, $|x|^{-1}\partial_\omega\in x_I\rho_+\mathcal V_{e3b}$ (the source's
(11.12), dimension-free), so all Cartesian derivatives lie in $\rho_+\mathcal V_{e3b}$, and a coefficient $c$ of the
counting with a factor $\delta$ of $x_I$-order at least 3 (the least slot order, $\frac32$ in $\rho_I$) gives
$c\,\partial\partial\in x_I^2\rho_+^2\cdot x_I^{1}\cdot(\cdots)
\mathrm{Diff}^2_{e3b}$, and $x_I^1\le x_I^{2\ell_I}$; at $\iota^+$ the factor has order $>1\ge\ell_+$ and at $K^+$ order
$a_K\ge\ell_K$. The b-regularity of the coefficients is $k-2$, and the e3b-fields are b-fields on $M_{1/2}$. The norm
bound is linear in the $\delta$ factors (their sum of norms is at most $C(|b-b_0|+|S|)+\|h\|$), the other factors being
bounded in terms of an upper bound for $\|h\|_{\mathcal X^k}$. $\square$

*The inverse metric (D254).* Smallness enters only through $g^{-1} = (g_b+\delta)^{-1}$, $\delta := g-g_b$. Write
$(g_b+\delta)^{-1} = \sum_{j\le N}(-g_b^{-1}\delta)^jg_b^{-1}+R_N$, $R_N := (-g_b^{-1}\delta)^{N+1}(g_b+\delta)^{-1}$.
$(g_b+\delta)^{-1}$ is a smooth function of $\delta$ for $\delta$ pointwise small, which the $H^{3,(1,0,0)}_{\mathrm
b}$-smallness gives by Sobolev embedding, so by Moser's composition estimate (II.A's tame estimates)
$(g_b+\delta)^{-1}-g_b^{-1}$ is bounded in $H^k_{\mathrm b}$ with weights 0, by a constant depending on an upper bound
for $\|\delta\|_{H^k}$. The factor $(-g_b^{-1}\delta)^{N+1}$ has $N+1$ times $\delta$'s least orders, positive at each
face, so for $N$ large $R_N$ lies in $H^k_{\mathrm b}$ with weights beyond every weight in (3.4), (3.6) and (3.7) and
adds no expansion terms; the Taylor terms are products handled by III.C Lemma 2.1. This replaces III.C Proposition 4.4's
Neumann series, whose convergence needs $H^k$-smallness.

**Remark 3.5 ([Hin26] Remark 11.7 at n = 4).** $g_{b_0}+h$ and $g_{b_0,b,0}+h$ differ near $(\iota^+)^\circ$ by
$\chi_K(g_b-g_{b_0})\in\rho_+^2C^\infty$, which is absorbed into $h$ as $(2,0)\in\mathcal E_+$; the same holds for the
boost, $g_{b_0,b,-S}-g_{b_0,b,0} = (1-\chi_K)(\phi^*_{-S}g_{b_0}-g_{b_0})\in H^{\infty,(\langle(3,0)\rangle_0,\infty),
((2,0),\infty),\infty}_{\mathrm b}$ (Lemma 3.6). This is where (1.3)'s $(2,0)\in\mathcal E_+$ is used.

**Lemma 3.6 (the background differences).** For $|b-b_0|$ and $|S|$ small, $g_{b_0,b,-S}$ satisfies (3.5) and lies in
$\mathcal G^+$; $g_{b_0,b,-S}-g_b$ is supported in $\{\chi_K<1\}$ and lies in
$H^{\infty,(\langle(3,0)\rangle_0,\infty),((2,0),\infty),\infty}_{\mathrm b}(\Omega_*)$, with seminorms $O(|b-b_0|+|S|)$.

*Proof.* $g_{b_0,b,-S}-g_b = (1-\chi_K)(\phi^*_{-S}g_{b_0}-g_{b_0})+(1-\chi_K)(g_{b_0}-g_b)$. On $\mathrm{supp}(1-\chi_K)
\cap\Omega_*$, $\chi_{\mathrm{IVP}} = 1$ and the flow of $V(S)$ is the boost (on III.B Lemma 5.2's first alternative,
with $\mathrm{supp}\,\chi^\flat_K\subset\chi_K^{-1}(1)$; on its second, $\{|x|<6R_1\}$, the difference is smooth and
supported in a compact set away from the faces at infinity, as that alternative of III.B Lemma 5.2 states, hence in the
class), so by III.B (5.3), $\phi^*_{-S}g_{b_0}-g_{b_0} = |x|^{-2}h_{-S}(\omega)
(dx^1)^2+\rho_0^2\rho_I^3\rho_+^2C^\infty$, with $h_{-S} = O(|S|)$; and by III.B Proposition 3.6, $g_{b_0}-g_b =
(\mu_0-\mu)|x|^{-2}(dx^1)^2+O(|b-b_0|)|x|^{-3}C^\infty$ on $\{|x|\ge3R_1\}$. Near $\mathscr I^+$, $|x|^{-2}(dx^1)^2$ is
the slot $\pi_{11}$ at $\rho_I$-order 2 and $\iota^+$-order 2, and $|x|^{-3}$ is of orders 3; in the interior of
$\iota^+$, $|x|^{-2}\in\rho_+^2C^\infty$. This is the class stated, as $1-\chi_K$ is smooth on $M$. For (3.5):
$g_{b_0,b,-S}-g_{\mu_0} = (g_{b_0,b,-S}-g_b)+(g_b-g_{\mu_0})$, the last being $\chi_K$-independent, smooth at $K^+$ and
of the same classes; and $g_{b_0,b,-S} = g_b$ on $\chi_K^{-1}(1)$, a neighbourhood of $K^+$. $\mathcal G^+$: near
$\mathscr I^+\cap\iota^+$, $g_{b_0,b,-S} = \phi^*_{-S}g_{b_0}$ and $g_{\mu_0}-\eta = \mu_0|x|^{-2}(dx^1)^2$, slot
$\pi_{11}$ only. $\square$

## 4. Forward mapping ([Hin26] Proposition 11.8, Corollary 11.9 at n = 4)

**Proposition 4.1 ([Hin26] Proposition 11.8 at n = 4).** Let $g_0\in\mathcal G^+$ satisfy (3.5), $h$ and $g$ be as in
Proposition 3.4, and $\frac32<\ell_I<a_I+\frac12$, $0<\ell_+<a_++\min\mathrm{Re}\,\mathcal E_+$, $\ell_K\in\mathbb R$,
$k\ge5$. Then
$$L^{g,g_0}:H^{k,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_+,\ell_+),\ell_K}_{\mathrm b}(\Omega_*)\to
H^{k-2,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),(\mathcal E_++2,\ell_++2),\ell_K}_{\mathrm b}(\Omega_*),\tag{4.1}$$
and, if moreover $\ell_+\le\max(a_+,\min\mathrm{Re}\,\mathcal E_+)$, for every $\epsilon>0$,
$$L^{g,g_0}-L_b:H^{k,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_+,\ell_+),\ell_K}_{\mathrm b}\to
H^{k-2,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),(2\mathcal E_++2,\ell_++2+m_+-\epsilon),\ell_K+a_K}_{\mathrm b},\qquad
m_+ := \min(a_+,\min\mathrm{Re}\,\mathcal E_+).\tag{4.2}$$
The source's (11.19) has $\ell_++3-\epsilon$ ($m_+ = 1$) and $\ell_K+2+\epsilon_K$ ($a_K = 2+\epsilon_K$). The upper
bounds on $\ell_I$ and $\ell_+$ are those of the products (III.C Lemma 2.1): a coefficient of the error with no
expansion beyond its $\mathscr I^+$-weight $a_I$, acting on the radiation term $\rho_I^{3/2}$ of $\slashed\pi_0u$, gives
$\rho_I^{a_I+\frac32}$ times a function with no expansion, and likewise at $\iota^+$; the source's Proposition 11.8,
stated for all weights, has the same restriction ((I6)).

*Proof.* (4.1). Near $\mathscr I^+$ (on $U^+\cap\{\rho_I\le1\}$) this is III.C Proposition 5.2's proof with Proposition
3.3 for III.C Proposition 4.4, $\iota^+$ in place of $I_0$ and $\mathcal E_+$ in place of $\mathcal E_0$: the leading
part $\rho_+^2\rho_I(X_+-X_I)(X_I-\frac32-\bar A)$ has the slot-by-slot effect computed there ($X_+-X_I$ preserves index
sets, $(X_I-\frac32-\bar A_{jj})$ annihilates the exceptional terms, the couplings of $\bar A$ as there), the factor
$\rho_+^2\rho_I$ shifting by 2 at $\iota^+$ and 1 at $\mathscr I^+$; the $C^\infty$ error gives $\mathcal E^{\mathrm
tot}_I+2\subset\mathcal E^C_I+1$ and $\mathcal E_++2$; the perturbation error gives, by III.C Lemma 2.1,
$2\mathcal E^{\mathrm{tot}}_I\subset\mathcal E^C_I+1$ at weight $\ell_I+1$ and $2\mathcal E_++2\subset\mathcal E_++2$ at
weight $\ell_++2$ (the inequalities: $\ell_I+1<\ell_I+\frac32$, $\ell_I+1<a_I+\frac32$ by the hypothesis
$\ell_I<a_I+\frac12$, $\ell_I+1\le a_I+\ell_I$; $\ell_++2<\ell_++2+\min\mathrm{Re}\,\mathcal E_+$,
$\ell_++2<a_++2+\min\mathrm{Re}\,\mathcal E_+$ by the hypothesis on $\ell_+$, $\ell_++2\le a_++2+\ell_+$). Away from
$\mathscr I^+$, near $\iota^+\cup K^+$: $L_b\in\rho_+^2\mathrm{Diff}^2_{\mathrm b}$ near $(\iota^+)^\circ$ (Cartesian
derivatives in $\rho_+\mathcal V_{\mathrm b}$) and $L_b\in\mathrm{Diff}^2_{\mathrm b}$ near $K^+$, which give (4.1)
there, and $L^{g,g_0}-L_b$ is handled by (3.6) and III.C Lemma 2.1. (4.2): only $\iota^+$ and $K^+$ need an argument, as
at $\mathscr I^+$ (4.2) is (4.1); by (3.6), the coefficients of $L^{g,g_0}-L_b$ have $\iota^+$-data $(\mathcal
E_++2,a_++2)$ and $K^+$-weight $a_K$, and III.C Lemma 2.1 gives the product index set $2\mathcal E_++2$ at the weight
$\ell_++2+m_+-\epsilon$, which is below the least of $\ell_++2+\min\mathrm{Re}\,\mathcal E_+$, $\ell_++2+a_+$ and
$a_++2+\min\mathrm{Re}\,\mathcal E_+$ (the last as $\ell_++m_+\le a_++\min\mathrm{Re}\,\mathcal E_+$ when
$\ell_+\le\max(a_+,\min\mathrm{Re}\,\mathcal E_+)$), and the weight $\ell_K+a_K$ at $K^+$. $\square$

**Lemma 4.3 (the curvature of the patched background).** For $|b-b_0|$, $|S|$ small, $\mathrm{Ric}(g_{b_0,b,-S})$ is
supported in $\mathrm{supp}\,\chi_K\cap\mathrm{supp}(1-\chi_K)$ and lies in $\rho_+^4C^\infty$ near $(\iota^+)^\circ$,
with seminorms $O(|b-b_0|+|S|)$.

*Proof.* $g_1 := \phi^*_{-S}g_{b_0}$ and $g_2 := g_b$ are Ricci flat, so $\mathrm{Ric}(g_{b_0,b,-S})$ vanishes on the
interior of $\chi_K^{-1}(\{0,1\})$; so it is supported in $\mathrm{supp}\,\chi_K\cap\mathrm{supp}(1-\chi_K)$, whose
closure meets $\partial M$ only in a compact subset of $(\iota^+)^\circ$ ($\chi_K = 1$ near $K^+$ and $\chi_K = 0$ near
$\mathscr I^+$: III.B section 5, $\chi^\flat_K = 1$ on $\{|x|<t/10,\ t>60R_1\}$ and
$\mathrm{supp}\,\chi^\sharp_K\subset\{|x|<t/2\}$), and near $(\iota^+)^\circ$ $g_i-\bar g = k_i\in\rho_+^2C^\infty$
(Lemma 3.6, and III.B Lemma 5.1 for the pullback) and Cartesian derivatives lie in $\rho_+\mathcal V_{\mathrm b}$. With
$k := (1-\chi_K)k_1+\chi_Kk_2$, $\mathrm{Ric} (\bar g+k) = D\mathrm{Ric}(k)+Q(k)$, $Q$ at least quadratic:
$Q(k)\in\rho_+^6C^\infty$ (two factors $k$, two derivatives); $D\mathrm{Ric}(k) =
(1-\chi_K)D\mathrm{Ric}(k_1)+\chi_KD\mathrm{Ric}(k_2)+E$, with $D\mathrm{Ric}(k_i) = -Q(k_i)\in\rho_+^6 C^\infty$ and
$E$ the terms with a derivative on $\chi_K$: $\partial\chi_K\in\rho_+C^\infty$, $\partial^2\chi_K\in\rho_+^2 C^\infty$
($\chi_K$ smooth on $M$), times $\partial k_i\in\rho_+^3C^\infty$, resp. $k_i\in\rho_+^2C^\infty$; so $E\in\rho_+^4
C^\infty$. Where $\chi_K$ is locally constant, $E = 0$ and the count gives $\rho_+^6$. The size is linear in $k_1-k_2$
(for $k_1 = k_2$ the patched metric is Ricci flat), and $k_1-k_2 = O(|b-b_0|+|S|)$ by Lemma 3.6. $\square$

At $n = 3$ the same count gives $\rho_+^3$ (the source's $P(g_0,g_0)\in\rho_+^3C^\infty$); N1STAR-PROOF.md 10.39 (iii)
computed the mass case exactly at $n = 4$.

**Corollary 4.2 ([Hin26] Corollary 11.9 at n = 4).** Let $g_0 = g_{b_0,b,-S}$ with $|b-b_0|$, $|S|$ small and $g =
g_0+h$, $h\in\mathcal X^\infty$ with small $H^{3,(1,0,0)}_{\mathrm b}$-norm. Then
$$P_0(h,S,b) := P(g,g_0) = \mathrm{Ric}(g)-\delta^*_{g_0,E_C}\Upsilon^{E_\Upsilon}(g,g_0)\in
H^{\infty,(\langle\mathcal E^C_I+1\rangle',a_I+1),(\mathcal E_++2,a_++2),a_K}_{\mathrm b}(\Omega_*).\tag{4.3}$$

*Proof.* $P(g_0,g_0) = \mathrm{Ric}(g_0)$, as $\Upsilon^{E_\Upsilon}(g_0,g_0) = 0$ (III.C Corollary 5.3's proof); it
lies in $\rho_+^4C^\infty$ with support whose closure meets $\partial M$ in a compact subset of $(\iota^+)^\circ$ (Lemma
4.3), and $(4,0)\subset\mathcal E_++2$ as $(2,0)\in\mathcal E_+$. And $P(g,g_0)-P(g_0,g_0) =
\int_0^1L^{g_0+sh,g_0}h\,ds$, which lies in the space by Proposition 4.1 (with $g_1 = g_0$, uniformly in $s$), as in
III.C Corollary 5.3. $\square$

## 5. Admissibility and forward solutions ([Hin26] Corollary 11.10, Theorem 11.12 at n = 4)

### 5.1 The orders

III.H$'$ Theorem 1.3 holds for orders in its class $\mathcal O_c$: II.C Definition 2.4 with the conditions (C1)-(C3)
there. The orders of Part II.F$'$ are built by II.C Proposition 5.1's construction (its section 5.2,
$\mathsf s = s_{\mathrm{in}}-(s_{\mathrm{in}}-s_{\mathrm{out}})\chi$), shifted by constants (II.F$'$ Lemma 2.3 and Remark
7.1). III.H$'$ (H$'$7) asked that these be checked.

**Lemma 5.1 (the orders lie in $\mathcal O_c$).** The order $\mathsf s$ of
II.C Proposition 5.1, read over $K^+$ as a $t_*$-translation-invariant function (its (1)), satisfies (C1)-(C3) of
III.H$'$ Definition 1.1, with $s_c = s_{\mathrm{in}}$; and so does $\mathsf s+c$ for every constant $c$.

*Proof.* Over $K^+$, $\psi_0(x_I) = 0$ ($x_I\ge\epsilon_I$ there), so $\mathsf s = s_{\mathrm{in}}-(s_{\mathrm{in}}-
s_{\mathrm{out}})\chi_\iota$ with $\chi_\iota = \phi(f_W/\delta)\tilde\psi(\epsilon_\iota\delta
f_T)\psi(|\hat\eta_{3b}|^2/( 2\delta))\Psi(\sigma_{3b}^2/|\nu|^2_{3b})$ on $\Omega_\iota$ and $\chi_\iota = 0$ elsewhere
(the factor $\tilde\psi$ vanishes for $\epsilon_\iota\delta f_T\le4$, which holds near the inner boundary of
$\Omega_\iota$). (C1): $\Psi = 0$ on $(-\infty,0.04]$, so $\chi_\iota = 0$ on
$\{\sigma_{3b}^2\le0.04|\nu|^2_{3b}\}\supset\{\sigma = 0\}$, and $\mathsf s = s_{\mathrm{in}}$ there. (C2): on
$\mathrm{supp}\,\phi(f_W/\delta)$, $|\hat\xi_{3b}|<\frac\delta2$, so $f_T = r(1-\hat\xi_{3b})<2r$, and
$\tilde\psi(\epsilon_\iota\delta f_T) = 0$ for $r\le2/(\epsilon_\iota\delta)$; so $\mathsf s =
s_{\mathrm{in}}$ over $\{r\le2/(\epsilon_\iota\delta)\}\supset\{r\le r_\Gamma\}$, II.C having chosen
$1/(\epsilon_\iota\delta) >r_\Gamma$; (C2) is in any case implied by II.C Definition 2.4 (3) (III.H$'$ Definition 1.1,
D252). (C3): $-\mathsf H\mathsf s = (s_{\mathrm{in}}-s_{\mathrm{out}})\mathsf H\chi_\iota$ for the stationary $G_0$
($\mathsf H = \mathsf H^{3b}$ on $\Sigma^+$, a positive multiple of $\mathsf H_{G_0}$). On $\Sigma^+$ over
$\Omega_\iota$ the factors $\psi$ and $\Psi$ equal 1 (II.C Lemmas 5.3 and 5.5 (b): $\sigma_{3b}^2\ge0.09|\nu|^2$ and
$|\hat\eta_{3b}|^2\le3\delta<4\delta$), and $\mathsf H$ applied to the other two is $\ge0$ (Lemma 5.5 (a), (c) with
$\tilde\psi'\ge0$, and $\phi'(f_W/\delta)\ge0$ where $f_W\in[-\frac\delta2,-\frac\delta4]$, $\phi$ being even with
$\phi'\le0$ on $[0,\infty)$; by Lemma 5.5 (b) the other branch $\hat\xi_{3b}<-\frac\delta8$ does not meet $\Sigma$).
Each of these holds with margin off $\Sigma$. The proof of II.C Lemma 5.3 shows $|G_{3b}|>0.0125|\nu|^2_{3b}$ where
$\sigma_{3b}^2<0.09|\nu|^2_{3b}$, so $\Psi = 1$ on $W_1 := \{|G_{3b}|<0.0125|\nu|^2_{3b}\}$. On $W_2 :=
\{|\sigma_{3b}^{-2}G_{3b}|<\frac\delta{16}\}$ the computation of Lemma 5.5 (b), with the error $\frac\delta{16}+
\frac\delta{16}$, still gives $\hat\xi_{3b}\ge-\frac\delta8$ and
$|\hat\eta_{3b}|^2\le\frac32\delta+\frac\delta8<4\delta$, so $\psi = 1$ there. Lemma 5.5 (a) and (c) are proved there
from II.B (3.4) and (5.2) without using $\Sigma$ ($\bar{\mathsf H}f_T = 2\varrho^{-1}$ and $\bar{\mathsf H}f_W =
2(2-\hat\xi_{3b})\hat\xi_{3b}$ wherever $\sigma_{3b}\ne0$), so they hold on
$W_1\cap\Omega_\iota\cap\{|\hat\xi_{3b}|\le\frac\delta2\}$. Any other positive rescaling of the Hamilton field, or other
defining symbol of $\Sigma$ (as I.B section 1.4's $\mathsf H^\natural$), differs from $\mathsf H^{3b}$ by a positive
factor and by terms vanishing on $\Sigma$, of size $O(|\sigma_{3b}^{-2}G_{3b}|)$ relative to the margins $\frac\delta8$
and $\varrho^{-1}$ of (a), (c); so on a thinner neighbourhood $W\subset W_1\cap W_2$ of $\Sigma$ the monotonicity
$\mathsf H\mathsf s\le0$ holds for it too. On $\Sigma^-$ the same holds by the evenness of II.C section 5.2's
construction under the antipodal map. Outside $\Omega_\iota$ the order is constant. Constants added to $\mathsf s$
change none of this. $\square$

### 5.2 Admissibility

**Corollary 5.2 ([Hin26] Corollary 11.10 at n = 4).** Let $g_0 = g_{b_0,b,-S}$ (or $g_0$ with (3.5)) and $g := g_0+h$,
$h\in\mathcal X^k$, $k\ge5$, with small $\mathcal X^5$-norm. Then $P := 2L^{g,g_0}$ is admissible relative to $P_0 :=
2L_b$ of class $((0;k-5),(2\ell_I,\ell_+,\ell_K))$ (II.C Definition 3.3) for every $\ell_I\in(0,\frac12]$,
$\ell_+\in(0,1]$ and $\ell_K\in(2,a_K]$, with $p_0 = \tilde p_1 = 0$, whenever $P_0$ is 2-admissible with sf-loss 0 in
III.H$'$'s sense (orders in $\mathcal O_c$, margin 1; III.H$'$ Theorem 1.3; at $b = b_0$ for every $k$).

*Proof.* (1) $\sigma_2(P) = G_g$ with $g-g_b = (g_0-g_b)+h\in\tilde{\mathcal G}^{(0;k-3),(2\ell_I,\ell_+,\ell_K)}$ by
Lemmas 2.2 and 3.6. (2) With $p_0 = \tilde p_1 = 0$, $\tilde P = P-P_0$, which by (3.7) and Sobolev embedding
($H^{k-2}_{\mathrm b}\subset C^{k-5}_{\mathrm b}$, three derivatives for $\dim M = 5$) lies in
$x_I^2\rho_+^2C^{k-5,(2\ell_I,
\ell_+,\ell_K)}_{\mathrm b}\mathrm{Diff}^2_{e3b}$. (3) $p_1 = S|_{\partial X}$, which in the splitting III.C (1.6) is
$\bar A$, lower triangular with real diagonal (III.C Lemma 4.2), and $p_0 = 0$ is strictly lower triangular. The
conditions $\ell_+>\delta = 0$ and $\ell_K>\aleph = 2$ of II.C (5.23) hold. $\square$

The source has $\tilde p_1 = (A^h-A_0)|_{\mathscr I^+}$ and $p_0 = 4\rho_+^{-1}B^h|_{\mathscr I^+}$, of class
$\rho_+^{\ell_+}C^{k-4}_{\mathrm b}$, and needs $\ell_+\in(\delta,1)$, $\ell_I<\min(2\gamma_\Upsilon,\frac12)$.

### 5.3 Forward solutions

**Theorem 5.3 ([Hin26] Theorem 11.12 at n = 4, at $b_0$).** Let $\beta_+\in(\frac12,\frac32)$ and $\beta_I\in(\beta_+,
\frac32)$. There are $\epsilon_0>0$ and $d\in\mathbb N$ such that for every $k\in\mathbb N_0$, every $S\in\mathcal S_1$
with $|S|<\epsilon_0$, every $h\in\mathcal X^{k+d}$ with $\|h\|_{\mathcal X^d}<\epsilon_0$, and every
$$f\in H^{k+d,(\beta_I+1,\beta_++2,\frac12)}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-},\tag{5.1}$$
the forward solution $u$ of $L^{g,g_0}u = f$, $g_0 := g_{b_0,b_0,-S}$, $g := g_0+h$, satisfies
$$u\in H^{k,(\beta_I,\beta_+,-\frac32)}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-},\qquad
\|u\|_{H^{k,(\beta_I,\beta_+,-\frac32)}_{\mathrm b}}\le C_k\big(\|f\|_{H^{k+d,(\beta_I+1,\beta_++2,\frac12)}_{\mathrm
b}}+
\|h\|_{\mathcal X^{k+d}}\|f\|_{H^{d,(\beta_I+1,\beta_++2,\frac12)}_{\mathrm b}}\big).\tag{5.2}$$
For $k\ge1$, $u$ depends continuously on $(S,h)$ in
$H^{k-1,(\beta_I-\varsigma,\beta_+-\varsigma,-\frac32-\varsigma)}_{\mathrm b}$ for every $\varsigma>0$. The densities
are $\mu_{\mathrm b}$.

The source has $\beta_+\in(\frac12,\frac12+\epsilon_{\mathrm{ind}})$, $\beta_I\in(\beta_+,1)$, sf-loss
$\delta>\beta_+-\frac12$ (so $u$ at $\beta_+-\delta$), and $b$ near $b_0$; here $\delta = 0$, the window of $\beta_+$ is
$(\frac12,\frac32)$, and $\beta_I$ reaches $\frac32$, the radiation field's order. The source's (11.23) writes the
$K^+$-weights $-2$ for $u$ and $0$ for $f$ where its (11.22) and (11.21) have $-\frac32$ and $\frac12$; with
$\mu_{\mathrm b}$ throughout, (5.2) uses the latter.

*Proof.* Apply II.F$'$ Theorem 1.1, in the form of its Corollary 1.2, with $P_0 := 2L_{b_0}$, $\aleph = 2$, the
sf-weight $\alpha_+ := \beta_+-\frac52$ and $\alpha_I := \beta_I-2$, with its Remark 7.1 for the relaxed admissibility
with margin $d_\aleph = 1$ ($d$ raised by 1). Its hypotheses: (i) $P_0$ is 2-admissible with sf-weight $\alpha_+$,
sf-loss 0 and margin 1 (III.H$'$ Theorem 1.3, at $b_0$ for every $k$, $\alpha_++2 = \beta_+-\frac12\in(0,1)$), for the
orders of II.F$'$, which lie in $\mathcal O_c$ by Lemma 5.1; II.F (8.6), where the admissibility enters (II.F Remark
8.2), uses them over $K^+$ with weights $\alpha_+$, $-2$ and margin 1, as III.H$'$ Definition 1.1 asks. (ii) (1.3) of
II.F$'$: $\alpha_I<-\frac12+\bar S = -\frac12$ ($\bar S = 0$, the least eigenvalue of $\bar A$, III.C (4.3)) is
$\beta_I<\frac32$, and $\alpha_+<\alpha_I-\frac12$ is $\beta_+<\beta_I$. (iii) $P = 2L^{g,g_0}$ is admissible relative
to $P_0$ of class $((0;k+d),(2\ell_I,\ell_+,\ell_K))$ for fixed $\ell_I\in(0,\frac12]$, $\ell_+\in(0,1]$,
$\ell_K\in(2,a_K]$, by Corollary 5.2 with $h\in\mathcal X^{k+d+5}$ ($d$ raised by 5), and $\|P-P_0\|_{(0;d)}\le
C(|S|+\|h\|_{\mathcal X^{d+5}})<\epsilon_0'$ for $\epsilon_0$ small (Proposition 3.4, (3.7)). The tame form:
$\|P-P_0\|_{(0;k+d)}\le C_k(|S|+\|h\|_{\mathcal X^{k+d+5}})$ by (3.7), whose coefficients are polynomial in $h$,
$g^{-1}$ and their derivatives, with tame (Moser) bounds in the b-regularity for $\|h\|_{\mathcal X^{d+5}}$ small
(II.A's tame product estimates); with II.F$'$ (1.5), $C_k|S|\|f\|_{H^d}\le C_k\|f\|_{H^{k+d}}$, which is (5.2). The
weights: Corollary 1.2 of II.F$'$ with $b_I = \alpha_I+2 =
\beta_I$, $b_+ = \alpha_++\frac52 = \beta_+$, sf-loss 0, and $K^+$-weights $\frac12$ for $f$ and $-\aleph+\frac12 =
-\frac32$ for $u$. Continuity: the last statement of II.F$'$ Theorem 1.1, $P$ depending continuously on $(S,h)$ in the
norm of (3.7). $\square$

**Remark 5.4 (b different from $b_0$).** The source states Theorem 11.12 for $|b-b_0|<\epsilon_0$, with constants
uniform in $b$. At $n = 4$ two inputs are not yet available for $b\ne b_0$. (a) III.H$'$ Theorem 1.3 gives the
2-admissibility of $2L_b$ for $k\le K$ on a neighbourhood $\mathcal B_K$ of $b_0$, not for all $k$, as strong trapping
admissibility is proved at $b_0$ only (III.H$'$ (H$'$3)). (b) II.F$'$ Theorem 1.1 is proved for one stationary $P_0$,
with constants depending on it; its uniform version over the stationary models of nearby parameters is open (II.F$'$
section 1.3 (b), (F$'$11)). So for $b\in\mathcal B_K$, $b\ne b_0$, Theorem 5.3 holds with $L_b$ for $L_{b_0}$ at those
$k$ for which II.F$'$'s proof invokes II.C Definition 2.7 (3) only at b-regularities $\le K$, with $b$-dependent
constants; which $k$ these are, and the uniformity in $b$, are recorded as open ((I3)).

**Remark 5.5 ([Hin26] Remark 11.13 at n = 4).** As in the source, rewriting $L_bu = f-(L^{g,g_0}-L_b)u$ and using
(4.2), the tameness of (5.2) propagates through a fixed finite number of such rewritings, with a total loss of
b-regularity independent of $k$; this is for the parts that write the source's sections 11.2-11.8, whose statements
are written with $k = \infty$. Each rewriting uses (4.2), so the weights must lie in Proposition 4.1's range ((I6)).

## 6. Findings, labels and sources

### 6.1 Findings

(I1) *Admissibility with $p_0 = \tilde p_1 = 0$.* At $n = 4$ the perturbation's contributions $A^h-A_0$, $B^h$ at null
infinity are half an order lower than the constant $\bar A$ (III.C (C1)), in the cone as at $I_0\cap\mathscr I^+$
(Proposition 3.3), so the dynamical operator is admissible relative to $L_b$ with $p_0 = \tilde p_1 = 0$ and $p_1 = \bar
A$ (Corollary 5.2); the source's restrictions $\ell_I<2\gamma_\Upsilon$ and $\ell_+<1$ become $\ell_I\le\frac12$ and
$\ell_+\le1$ (Lemma 2.2).

(I2) *Orders.* II.C Proposition 5.1's construction gives orders in III.H$'$'s class $\mathcal O_c$ (Lemma 5.1); with
this, III.H$'$'s obligation (H$'$7) is met for Part II.F$'$'s use, and the relaxed (margin 1) admissibility enters
through II.F$'$ Remark 7.1 and II.F Remark 8.2.

(I3) *$b\ne b_0$ (open).* Theorem 11.12 is proved at $b_0$. For $b\ne b_0$ near $b_0$ it needs (a) 2-admissibility of
$L_b$ for all $k$, which needs strong trapping admissibility near $b_0$ or a finite-$k$ version of the later Nash-Moser
argument, and (b) II.F$'$ Theorem 1.1 uniformly in the stationary model ((F$'$11)). The later parts, where the final
parameters $b$ vary ([Hin26] section 11.6 on), must supply both or work around them.

(I4) *Orders at $\iota^+$.* The background differences are of order 2 at $\iota^+$ (Lemma 3.6), the curvature of the
patched background of order 4 (Lemma 4.3), so $(2,0)\in\mathcal E_+$ replaces the source's $(1,0)$; the forward mapping
(4.2) gains $m_+ = \min(a_+,\min\mathrm{Re}\,\mathcal E_+)>1$ at $\iota^+$, the source's 1.

(I5) *Parameters.* The weights $(a_I,a_+,a_K)$ of $\mathcal X^k$ are left free here ($a_I>\frac32$, $a_+>1$, $a_K>2$);
the source's $(3+\epsilon_I,3+\epsilon_+,2+\epsilon_K)$ and $0<\epsilon_K<\epsilon_+<\min(\epsilon_{\mathrm{ind}},
\epsilon_I)<1$ are fixed at $n = 4$ by the parts that write sections 11.2-11.8 (the Fourier transform's conditions,
III.A, and the iteration).

(I6) *The range of the forward mapping (D254).* [Hin26] Proposition 11.8 is stated for all weights, but its products
(III.C Lemma 2.1) need $\ell_I<a_I+\frac12$ (at $n = 3$, $\ell_I<a_I = 3+\epsilon_I$) and
$\ell_+<a_++\min\mathrm{Re}\,\mathcal E_+$, and (11.19) moreover $\ell_+\le\max(a_+,\min\mathrm{Re}\,\mathcal E_+)$.
Proposition 4.1 carries these, Corollary 4.2 ($\ell = a$) lies inside them, and the parts writing sections 11.2-11.8
must keep their weights there.

### 6.2 Labels

Proved: Lemmas 2.1, 2.2, 3.1, 3.2, 3.6, 4.3, 5.1, Propositions 3.3, 3.4, 4.1, Corollaries 4.2, 5.2 and Theorem 5.3, given
the parts cited; Remarks 3.5, 5.4, 5.5 and the comparisons with the source are commentary. READ: the source's statements
quoted from pp. 218-226. Inputs: II.A Lemma 2.5 and its tame estimates; II.C Definitions 2.4, 3.1, 3.3, Lemma 3.2,
Proposition 5.1 and its section 5.2 (Lemmas 5.3, 5.5); II.F Remark 8.2; II.F$'$ Theorem 1.1, Corollary 1.2, Remark 7.1;
III.B (2.2), Proposition 3.6, section 5 (Lemmas 5.1-5.2); III.C Definitions 1.2, 3.1, 3.3, 3.4, 5.1, Lemmas 1.3, 2.1,
3.2, 4.1-4.3, Propositions 4.4, 5.2, Corollary 5.3; III.F (2.2)-(2.3), Lemma 2.1; III.H$'$ Definition 1.1, Theorem 1.3.

### 6.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 11's opening and
section 11.1 (pp. 218-226: (11.1)-(11.24), Definition 11.3, Remark 11.4, Lemma 11.5, Proposition 11.6, Remark 11.7,
Proposition 11.8, Corollaries 11.9-11.10, Remark 11.11, Theorem 11.12, Remark 11.13). N1STAR-PROOF.md 10.39 and 10.42
(the deductions this part replaces).
