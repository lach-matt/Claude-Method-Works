# Part III.F$''''$. Zero energy pairings and physical zero energy states at n = 4 ([Hin26] 8.12, 8.14, 8.15)

*Status.* Proved (D238: verifier 98 read the repairs, correct; two nits seated; status synchronised with the README at
D325). Written (D234). This part proves, at spatial dimension $n = 4$, the pairings of [Hin26] Lemma 8.12 (p. 157) and
Lemma 8.15 (pp. 158-159) and the physical large zero energy states of Proposition 8.14 (pp. 158-163) that the expansion
at low energies needs. The source proves Lemma 8.12 by "The proof of [Hin24b, Lemma 3.17] applies verbatim", that is, by
reducing each pairing to a pairing at infinity of leading terms ([Hin23b] Theorem 9.6); here the reduction is written
out (Lemma 2.2), and the pairings at infinity are the record's exact computations (`pairing5.py` P2-P5). Lemma 8.15's
vector type pairing is obtained on all of $\mathfrak{so}(4)$ from Remark 8.10 (III.F$'''$ Remark 2.3) and the
spin-independence of its leading terms (Lemma 4.1 (2)), without a separate computation. Proposition 8.14 is proved at
the root $-2$ for scalar, vector and tensor type 2, the last absent in four dimensions; its Step 2 is modified, because
in five dimensions the vanishing of the centre-of-mass pairings against the rotations' dual states, which the source's
Step 2 uses, is not available away from $b_0$. Notation is that of Parts III.F$'$-III.F$'''$; computations cited as
*computed* are exact (sympy) and rerun by `pairing5.py`.

## 1. Setting

The parameters, the unweighted b-density $\mu_{\mathrm b}$, $\epsilon_{\mathrm{ind}}$, $\mathcal E_{\mathrm{ind}}$,
$|dg_b| = |dt_*||dx|$ and the pairing $\langle u,v\rangle := \int_X\langle u,v\rangle_{g_b}|dx|$ (real, bilinear) are
those of III.F$'''$ section 1; adjoints and transposes on $X$ are taken with respect to it. $\chi_R(x) := \chi_1(|x|/R)$
with $\chi_1\in C^\infty_c([0,2))$ equal to 1 on $[0,1]$; it is 1 near the black hole and 0 near infinity, and
$|d\chi_R|\le CR^{-1}$ is supported in $\{R\le|x|\le2R\}$.

*Spins.* For $A\in\mathfrak{so}(4)$ let $V(A) := (Ax)\cdot dx$, the Euclidean dual of the rotation field
$R_A = (Ax)\cdot\partial_x$, and for $V\in\mathcal V_1$ let $A_V$ be the element with $V(A_V) = V$ (III.F$'''$ section
1). $\langle A,B\rangle_F := \frac12\mathrm{tr}(A^TB)$, so that the $E_{ij} := e_ie_j^T-e_je_i^T$, $i<j$, are
orthonormal; $\mathrm{ad}_A$ is skew for it, $\langle[A,X],Y\rangle_F = -\langle X,[A,Y]\rangle_F$. For
$S\in\mathcal S_1$, $\xi_S\in\mathbb R^4$ is given by $|x|S = \xi_S\cdot x$. The dual states are
$h^*_{b,\bullet} = G_{g_b}\delta^*_{g_b}\omega^*_{b,\bullet}$ (III.E Proposition 3.1), with leading terms
$\bar\omega_{\mathrm s0} = -d\bar t$, $\bar\omega_{\mathrm s1}(S) = \xi_S\cdot dx$ and $V$; and
$h^*_{b,\mathrm v1}(V) = h^\sharp_{b,\mathrm v1}([A(b),A_V])+h^\flat_{b,\mathrm v1}(V)$ (III.E$'$ Proposition 3.1).

*Weights.* Each 1-form and tensor below is stationary, smooth on $X$ (or, for the dual states, in
$\dot H^{1}_{\mathrm b}$, resp. $\dot H^0_{\mathrm b}$, and zero on $\{r_0<|x|<r_h\}$), and conormal near $\partial X$;
its *weight* is the largest $a$ with the object in $\mathcal A^a$ up to the leading terms named. The weights used are:
$\dot g^\Upsilon_b(1,0)$ 2, $\dot g^\Upsilon_b(0,\dot A)$ 3, $h_{b,\mathrm s1}(S)$ and $h_{b,\mathrm v1}(V)$ 3,
$\breve h^1_{b,\mathrm s1}(S)$ 2, $\breve h^1_{b,\mathrm v1}(V)$ and $\breve h^2_{b,\mathrm s1}(S)$ $-1$ (III.F$'''$
(4.2), III.D$''$ (3.4), III.D$'''$ Proposition 3.1); $\omega^*_{b,\mathrm s0}$, $\omega^*_{b,\mathrm s1}(S)$ 0 and
$\omega^*_{b,\mathrm v1}(V)$ $-1$; $h^*_{b,\mathrm s1}$, $h^*_{b,\mathrm v1}$ and $h^\sharp_{b,\mathrm v1}$ 3, and
$h^*_{b,\mathrm s0}$, $h^\flat_{b,\mathrm v1}$ in $\dot H^{0,C_0+3}_{\mathrm b}$ (III.E (3.2), III.E$'$ (3.3)).

## 2. The pairings at infinity

A stationary operator on $M$ is $P = P_0+P_1\partial_{t_*}+P_2\partial_{t_*}^2$ with $P_j$ operators on $X$; on
stationary sections $\widehat P(0) = P_0$, $[P,t_*] = P_1$ and $\frac12[[P,t_*],t_*] = P_2$, and
$P(\frac12t_*^2v+t_*\breve v) = \frac12t_*^2P_0v+t_*(P_1v+P_0\breve v)+(P_2v+P_1\breve v)$ for stationary $v$,
$\breve v$.

**Lemma 2.1.** Let $P := D_{g_b}\mathrm{Ric}$, $G := G_{g_b}$, and $k(\omega) := dt_*\otimes_s\omega$.

(1) $GP_0$ and $GP_2$ are symmetric and $GP_1$ is antisymmetric on $X$ (as differential operators).

(2) For every stationary 1-form $\omega$: $P_0\delta^*\omega = 0$, $P_1\delta^*\omega = -P_0k(\omega)$ and
$P_2\delta^*\omega = -P_1k(\omega)$.

*Proof.* (1) $G\circ P$ is formally self-adjoint on $M$ (III.F$'''$ (4.4)), and $|dg_b| = |dt_*||dx|$, so
$GP = \sum_jGP_j\partial_{t_*}^j$ has adjoint $\sum_j(-\partial_{t_*})^j(GP_j)^T$; comparing coefficients,
$(GP_j)^T = (-1)^jGP_j$. (2) $P\circ\delta^* = 0$ (III.F$'''$ Proposition 2.2 (2)), and
$\delta^*(f\omega) = f\delta^*\omega+df\otimes_s\omega$. Apply $P$ to
$\delta^*(t_*\omega) = t_*\delta^*\omega+k(\omega)$ and to
$\delta^*(\frac12t_*^2\omega) = \frac12t_*^2\delta^*\omega+t_*k(\omega)$, expand by the formula above, and read off the
coefficients of $t_*^0$. $\square$

**Lemma 2.2 (reduction to infinity).** Let $L := L_b$, $L_j$ its coefficients as above, $\omega^*$ one of the dual
1-forms of section 1, of weight $c$, and $h^* := G\delta^*\omega^*$, of weight $c^*\ge3$. Write $k := k(\omega^*)$.

(1) (*First order.*) If $u\in\ker D_{g_b}\mathrm{Ric}(0)\cap\ker\delta_{g_b,E_\Upsilon}G$ has weight $a\ge2$, then
$$\langle L_1u,h^*\rangle = \lim_{R\to\infty}\big\langle[P_0,\chi_R]u,\,Gk\big\rangle.\tag{2.1}$$

(2) (*Second order.*) If $h$, $\breve h$ have weights $a\ge3$, $\breve a\ge2$, and $h$, $t_*h+\breve h$ lie in
$\ker D_{g_b}\mathrm{Ric}\cap\ker\delta_{g_b,E_\Upsilon}G$, then $L_2h+L_1\breve h = L(\frac12t_*^2h+t_*\breve h)$ is
stationary and
$$\langle L_2h+L_1\breve h,h^*\rangle
 = \lim_{R\to\infty}\big\langle[P_1,\chi_R]h+[P_0,\chi_R]\breve h,\,Gk\big\rangle.\tag{2.2}$$

(3) (*What the limits see.*) Let $R_1(u)$, $R_2(h,\breve h)$ denote the right sides of (2.1), (2.2), for $u$ with
$P_0u = 0$ of weight $a\ge2$, resp. pairs with $P_0h = 0 = P_1h+P_0\breve h$ of weights $a\ge3$, $\breve a\ge2$, and put
$e_1 := a+c-2$, $e_2 := \min(a-3,\breve a-2)+c$. The limits exist and equal $\langle P_1u,h^*\rangle$, resp.
$\langle P_2h+P_1\breve h,h^*\rangle$. If $e_i>0$ they vanish; if $e_i = 0$ they are the same integrals computed with
the leading terms of the arguments, of $\omega^*$, of $P_j$, $G$ and $t_*$ alone, which do not depend on $R$; if $e_i<0$
the leading terms do not determine them. $R_1$ vanishes on $\delta^*\zeta$ and $R_2$ on
$(\delta^*\zeta,\delta^*\breve\zeta+k(\zeta))$, for stationary $\zeta\in\mathcal A^{a-1}$,
$\breve\zeta\in\mathcal A^{\breve a-1}$ smooth on $X$; and $R_1(u)$, $R_2(h,\breve h)$ do not change when $t_*$ is
replaced by $t_*+\phi$, $\phi$ smooth on $X$ and in $|x|C^\infty(\bar X)$ near $\partial X$, the pair being rewritten as
$(h,\breve h-\phi h)$.

*Proof.* In every pairing below one factor is smooth and supported in $\{|x|\le2R\}$ and the other vanishes on
$\{r_0<|x|<r_h\}$, so integrations by parts on $X$ produce no boundary terms; the dual states have finite regularity,
and the pairings are distributional. Near $\partial X$, $\chi_R$ is a function of $\rho R$, so
$[P_0,\chi_R]\in\rho^2\mathrm{Diff}^1_{\mathrm b}$, $[P_1,\chi_R]\in\rho\,\mathrm{Diff}^0_{\mathrm b}$ and
$[P_0^T,\chi_R]\in\rho^2\mathrm{Diff}^1_{\mathrm b}$, with coefficients bounded uniformly in $R$ and supported in
$\{R\le|x|\le2R\}$ ($P_1\in\rho\,\mathrm{Diff}^1_{\mathrm b}$, III.F Lemma 2.1); and $|dx| = \rho^{-4}\mu_{\mathrm b}$.
So a pairing over that annulus of $[P_0,\chi_R]$ or $[P_0^T,\chi_R]$ applied to weight $w$ against weight $w'$ is
$O(R^{2-w-w'})$, and of $[P_1,\chi_R]$ is $O(R^{3-w-w'})$. Also $P_0^Th^* = GP_0G^{-1}h^* = GP_0\delta^*\omega^* = 0$
and $(\delta^*_{E_C})^*h^* = \frac12(\Box^C_b)^*\omega^* = 0$ (III.F$'''$ Proposition 4.1, Step 1).

(1) $L = P+\delta^*_{E_C}\delta_{E_\Upsilon}G$, and
$[\delta^*_{E_C}\delta_{E_\Upsilon}G,t_*]u = \delta^*_{E_C}\vartheta$ with $\vartheta := [\delta_{E_\Upsilon}G,t_*]u$ of
weight $a$, since $\delta_{E_\Upsilon}Gu = 0$; and $\langle\delta^*_{E_C}\vartheta,h^*\rangle =
\lim_R\langle\vartheta,[(\delta^*_{E_C})^*,\chi_R]h^*\rangle = O(R^{3-a-c^*})\to0$. The pairing
$\langle P_1u,h^*\rangle$ converges absolutely and equals $\lim_R\langle P_1(\chi_Ru),h^*\rangle$ (the commutator term
is $O(R^{3-a-c^*})$), and by Lemma 2.1,
$$\langle P_1(\chi_Ru),G\delta^*\omega^*\rangle = -\langle\chi_Ru,GP_1\delta^*\omega^*\rangle
 = \langle\chi_Ru,GP_0k\rangle = \langle GP_0(\chi_Ru),k\rangle = \langle[P_0,\chi_R]u,Gk\rangle,$$
the last as $P_0u = 0$.

(2) The expansion formula and $Lh = 0$, $L(t_*h+\breve h) = 0$ give $L(\frac12t_*^2h+t_*\breve h) = L_2h+L_1\breve h$.
As $\delta_{E_\Upsilon}G$ is of first order, $\delta_{E_\Upsilon}G(\frac12t_*^2h+t_*\breve h) =
t_*\delta_{E_\Upsilon}G(t_*h+\breve h)+[\delta_{E_\Upsilon}G,t_*]\breve h = [\delta_{E_\Upsilon}G,t_*]\breve h =:
\vartheta$, of weight $\breve a$; so $L(\frac12t_*^2h+t_*\breve h) = P_2h+P_1\breve h+\delta^*_{E_C}\vartheta$, and the
last term pairs to $O(R^{3-\breve a-c^*})\to0$ with $h^*$ as in (1). By Lemma 2.1, with commutator terms
$O(R^{3-\breve a-c^*})$,
$$\langle P_2(\chi_Rh)+P_1(\chi_R\breve h),G\delta^*\omega^*\rangle
 = \langle\chi_Rh,GP_2\delta^*\omega^*\rangle-\langle\chi_R\breve h,GP_1\delta^*\omega^*\rangle
 = -\langle\chi_Rh,GP_1k\rangle+\langle\chi_R\breve h,GP_0k\rangle$$
$$= \langle G(P_1(\chi_Rh)+P_0(\chi_R\breve h)),k\rangle = \langle[P_1,\chi_R]h+[P_0,\chi_R]\breve h,Gk\rangle,$$
using $P_1h+P_0\breve h = 0$, the $t_*^0$ coefficient of $P(t_*h+\breve h) = 0$.

(3) The identity chains of (1)-(2) used only $P_0u = 0$, resp. $P_0h = 0 = P_1h+P_0\breve h$, so
$R_1(u) = \langle P_1u,h^*\rangle$ and $R_2(h,\breve h) = \langle P_2h+P_1\breve h,h^*\rangle$, absolutely convergent.
The leading terms: by the counting above the terms of $R_1$ are $O(R^{-e_1})$ and those of $R_2$ are $O(R^{-(a+c-3)})$
and $O(R^{-(\breve a+c-2)})$; every correction to a leading term (of the arguments, of $\omega^*$, of $P_j$ and $G$ by
$\rho^2$; $dt_*$ is exact) raises a weight, and the model operators are homogeneous under dilations, so at $e_i = 0$ the
leading integral does not depend on $R$. *Gauge.* $P_1\delta^*\zeta = -P_0k(\zeta)$ (Lemma 2.1), and $\langle
P_0k(\zeta),h^*\rangle = \lim_R\langle k(\zeta),[P_0^T,\chi_R]h^*\rangle = O(R^{3-a-c^*})\to0$. For the pair,
$P_2\delta^*\zeta+P_1(\delta^*\breve\zeta+k(\zeta)) = -P_1k(\zeta)-P_0k(\breve\zeta)+P_1k(\zeta) = -P_0k(\breve\zeta)$,
which pairs to $O(R^{3-\breve a-c^*})\to0$. *Time function.* $|dg_b| = |d(t_*+\phi)||dx|$ and Lemma 2.1 holds for
$t_*+\phi$. With $\bar t := t_*+\phi$, $\bar t\,u = t_*u+\phi u$, so the first-order coefficient changes by
$[P_0,\phi]u = P_0(\phi u)$, and $\langle P_0(\phi u),h^*\rangle = \lim_R\langle\phi u,[P_0^T,\chi_R]h^*\rangle =
O(R^{3-a-c^*})\to0$. And $\frac12\bar t^2h+\bar t(\breve h-\phi h) = \frac12t_*^2h+t_*\breve h+(\phi\breve
h-\frac12\phi^2h)$, so the second-order quantity changes by $P_0(\phi\breve h-\frac12\phi^2h)$, of weight
$\ge\min(\breve a-1,a-2)\ge1$ before $P_0$, which pairs to $O(R^{1-c^*})\to0$. $\square$

The computations of `pairing5.py` evaluate exactly these limits, on Minkowski space in Cartesian coordinates, as
$-I_A+I_B$ with $I_A$, $I_B$ the sphere integrals of the coefficients of $\chi_1'$ and $\chi_1''$, classifying each
entry by its excess before computing it.

## 3. [Hin26] Lemma 8.12 at n = 4

**Lemma 3.1 ([Hin26] Lemma 8.12 at n = 4).** For $b = (\mu,A)$ near $b_0$, $\dot\mu\in\mathbb R$,
$\dot A,A'\in\mathfrak{so}(4)$, $S,S'\in\mathcal S_1$:

(1) (*Mass.*) $\langle L_1\dot g^\Upsilon_b(\dot\mu,0),h^*_{b,\mathrm s0}\rangle = 3\pi^2\dot\mu$ and
$\langle L_1\dot g^\Upsilon_b(\dot\mu,0),h^*_{b,\mathrm s1}(S')\rangle = 0$.

(2) (*Angular momenta.*) $\langle L_1\dot g^\Upsilon_b(0,\dot A),h^*_{b,\mathrm s0}\rangle = \langle L_1\dot
g^\Upsilon_b(0,\dot A),h^*_{b,\mathrm s1}(S')\rangle = 0$ and $\langle L_1\dot g^\Upsilon_b(0,\dot A),h^*_{b,\mathrm
v1}(V(A'))\rangle = 2\pi^2\mu\,\langle\dot A,A'\rangle_F$.

(3) (*Centres of mass.*) With $h := h_{b,\mathrm s1}(S)$, $\breve h := \breve h^1_{b,\mathrm s1}(S)$:
$\langle L_2h+L_1\breve h,h^*_{b,\mathrm s0}\rangle = 0$ and
$\langle L_2h+L_1\breve h,h^*_{b,\mathrm s1}(S')\rangle = \frac{3\pi^2}2\mu\,\xi_S\cdot\xi_{S'}$.

(4) (*The rest.*) The pairings of $L_1\dot g^\Upsilon_b(\dot\mu,0)$ and of $L_2h+L_1\breve h$ with
$h^*_{b,\mathrm v1}(V')$ are not determined by the leading terms; they are linear in their arguments and continuous in
$b$. With them as unknowns, the $11\times11$ matrix of (1)-(4) (rows $\dot\mu$, $S$, $\dot A$; columns
$h^*_{\mathrm s0}$, $h^*_{\mathrm s1}$, $h^*_{\mathrm v1}$) is block upper triangular with determinant
$3\pi^2(\frac{3\pi^2}2\mu)^4(2\pi^2\mu)^6\ne0$.

*Proof.* Lemma 2.2 applies: the states lie in $\ker D\mathrm{Ric}\cap\ker\delta_{E_\Upsilon}G$ (III.F$'''$ Proposition
2.2 (2), III.D$''$ Proposition 3.1 (2)), with the weights of section 1, and $c^*\ge3$ throughout. The excesses
($e_1 = a+c-2$, $e_2 = \min(a-3,\breve a-2)+c$): mass ($a = 2$) against s0 and s1 ($c = 0$), 0; against v1 ($c = -1$),
$-1$; angular momenta ($a = 3$) against s0 and s1, 1; against v1, 0; centres of mass ($a = 3$, $\breve a = 2$) against
s0 and s1, 0; against v1, $-1$. The entries of excess $>0$ vanish, those of excess $<0$ are (4)'s, and the continuity
there is that of the states and dual states in $b$ (III.F$'''$ Proposition 2.2 (3), III.D$''$ Proposition 3.1, III.E
Proposition 3.1, III.E$'$ Proposition 3.1) with the absolute convergence of the pairings on the left of (2.1)-(2.2),
uniformly near $b_0$. The entries of excess 0 are, by Lemma 2.2 (3), leading-term integrals on Minkowski space, which by
Lemma 2.2 (3) may be computed with any representatives with $P_0u = 0$ (resp. $P_0h = 0 = P_1h+P_0\breve h$) differing
by decaying gauge terms, and with any time function $t_*+\phi$ as there. *Computed* (`pairing5.py`): (P2) with the mass
perturbation $\dot\mu|x|^{-2}(dt^2+dr^2)$ and the rotation $-2\mu|x|^{-4}dt\otimes_sw_{ij}$,
$w_{ij} = x^i\,dx^j-x^j\,dx^i$, against $\omega^* = dt$, the rotations and the translations: $-3\pi^2\dot\mu$ against
$dt$, 0 against the translations; $-2\pi^2\mu$ for a rotation against its own plane, 0 across planes and against $dt$
and the translations; (P3) the centres of mass, with $h_{b,c} = \delta^*_{g_b}(c\cdot\partial_x)^\flat$ and $\breve
h_{b,c} = [\delta^*_{g_b},t](c\cdot\partial_x)^\flat+\delta^*_{g_b}((c\cdot x)\partial_t^\flat)$ at first order in
$\mu$: $\frac{3\pi^2}2\mu\,(q\cdot c)$ against $q\cdot dx$, 0 against $dt$; (P5) the Kerr-Schild mass perturbation
$|x|^{-2}(dt+dr)^2$, which differs by $\delta^*(d\log|x|)$, and $t-r$ in place of $t$ give the same values. These
representatives differ from ours by decaying gauge terms: $\dot g^\Upsilon_b(\dot\mu,0)$ is
$\dot\mu|x|^{-2}(dt+d|x|)^2+\delta^*\dot\omega_b$ with $\dot\omega_b\in\mathcal A^{(1,0)\cup\dots}$ (III.F$'''$ Lemma
1.1, Proposition 2.2), the static and Kerr-Schild forms differ by $\delta^*$ of a 1-form in $\rho C^\infty$ (III.F$'''$
Theorem 3.1, Step 4), $\dot g^\Upsilon_b(0,\dot A)$ is $2\mu|x|^{-4}(dt+d|x|)\otimes_sV(\dot A)$ plus gauge and the
$d|x|$ part is $\delta^*$ of a vector type 1 form in $\rho C^\infty$, $h_{b,\mathrm s1}(S)-h_{b,\xi_S}$ and the boosts'
stationary parts differ by $\delta^*$ of 1-forms in $\mathcal A^{2}$, resp. $\mathcal A^{1}$ (III.D$''$ (3.2)) up to a
multiple of $h_{b,\mathrm s1}(S)$ (the choice of the time origin), which changes (3) by a first-order pairing of
$h_{b,\mathrm s1}$, of excess $\ge1$ against s0 and s1; the static time $t$ is $t_*+|x|+C^\infty+\rho C^\infty$ near
$\partial X$ (III.F$''$ section 2); and the dual states' leading terms are $-d\bar t = -dt+O(\rho^2)dr$,
$\xi_S\cdot dx$, $V$, with the remainders of higher weight. The signs: the s0 dual state has leading term $-dt$ against
`pairing5.py`'s $dt$, which gives $3\pi^2\dot\mu$; and for $\dot A = E_{ij}$, $V(\dot A) = -w_{ij}$, so the rotation
$-2\mu|x|^{-4}dt\otimes_sw_{ij}$ is $\dot g_b(0,E_{ij})$ up to gauge and $w_{ij} = V(-E_{ij})$, which gives
$2\pi^2\mu\langle\dot A,A'\rangle_F$ by bilinearity. (P4) the determinant, with the undetermined entries as symbols.
$\square$

The source's values ([Hin24b]'s normalisation $2L$, and $dt$ for the s0 dual state) are $-16\pi\dot m$,
$-16\pi m(q\cdot\dot a)$ and $8\pi m(q\cdot c)$; in each dimension the three are $\mp8\pi$ times the ADM mass and
angular momentum and $4\pi$ times the mass times the centre of mass, in the normalisation of the record's supplement
10.32 (a).

## 4. [Hin26] Lemma 8.15 at n = 4

For a stationary $v$ of weight $\ge-2$, smooth on $X$, with $\widehat{L_b}(0)v$ of weight $>1$, and
$W\in\mathfrak{so}(4)$, put
$$\lambda^\sharp_v(W) := \langle\widehat{L_b}(0)v,h^\sharp_{b,\mathrm v1}(W)\rangle
-\langle v,\widehat{L_b}(0)^*h^\sharp_{b,\mathrm v1}(W)\rangle.\tag{4.1}$$
Both pairings converge absolutely: $h^\sharp$ has weight 3, and
$\widehat{L_b}(0)^*h^\sharp_{b,\mathrm v1}(W)\in\rho^{\lfloor C_0\rfloor+6}C^\infty+C^\infty_c$ by III.E$'$ (3.4) and
(4.4) of III.F$'''$. If moreover $\widehat{L_b}(0)v$ pairs absolutely with $h^*_{b,\mathrm v1}(V')$, then
$$\langle\widehat{L_b}(0)v,h^*_{b,\mathrm v1}(V')\rangle = \lambda^\sharp_v([A(b),A_{V'}]),\tag{4.2}$$
since $\langle\widehat{L_b}(0)v,h^\flat\rangle = \langle v,\widehat{L_b}(0)^*h^\flat\rangle$
($h^\flat\in\dot H^{0,C_0+3}_{\mathrm b}$, $C_0>1$, so the boundary terms vanish) and
$\widehat{L_b}(0)^*h^\flat = -\widehat{L_b}(0)^*h^\sharp$, the dual state lying in $\ker\widehat{L_b}(0)^*$.
$\lambda^\sharp_v$ is defined on all of $\mathfrak{so}(4)$, while the right side of (4.2) sees only
$\mathrm{im}\,\mathrm{ad}_{A(b)}$, which is $0$ at $b_0$; this is the source's device (8.33) for smoothness in $b$.

**Lemma 4.1 ([Hin26] Lemma 8.15 at n = 4).** For $b = (\mu,A)$ near $b_0$:

(1) (*Scalar type 1.*) $\widehat{L_b}(0)\breve h^2_{b,\mathrm s1}(S) = -L_2h_{b,\mathrm s1}(S)-L_1\breve h^1_{b,\mathrm
s1}(S)$; so $\langle\widehat{L_b}(0)\breve h^2_{b,\mathrm s1}(S),h^*_{b,\mathrm s0}\rangle = 0$, and
$S\mapsto\langle\widehat{L_b}(0)\breve h^2_{b,\mathrm s1}(S),h^*_{b,\mathrm s1}(\cdot)\rangle =
-\frac{3\pi^2}2\mu\,\xi_S\cdot\xi_{(\cdot)}$ is an isomorphism $\mathcal S_1\to\mathcal S_1^*$, smooth in $b$.

(2) (*Vector type 1.*) $\widehat{L_b}(0)\breve h^1_{b,\mathrm v1}(V) = -L_1h_{b,\mathrm v1}(V)$, which pairs to 0 with
$h^*_{b,\mathrm s0}$ and $h^*_{b,\mathrm s1}(S')$, and
$$\langle\widehat{L_b}(0)\breve h^1_{b,\mathrm v1}(V),h^*_{b,\mathrm v1}(V')\rangle
 = \pi^2\mu\,\langle A_V,[A(b),A_{V'}]\rangle_F,\qquad\lambda^\sharp_{\breve h^1_{b,\mathrm v1}(V)}(W)
 = \pi^2\mu\,\langle A_V,W\rangle_F\ \ \forall W\in\mathfrak{so}(4).\tag{4.3}$$

*Proof.* (1) $h^{\le2}_{b,\mathrm s1}(S) = t_*^2h+2t_*\breve h^1+2\breve h^2$, $h := h_{b,\mathrm s1}(S)$, lies in
$\ker L_b$ (III.D$'''$ Proposition 3.1 (2), with its normalisation: the constant coefficient of $h^{\le k}$ is
$k!\breve h^k$); expanding as in section 2 with $Lh = 0$ and $L(t_*h+\breve h^1) = 0$ gives
$2(L_2h+L_1\breve h^1)+2\widehat{L_b}(0)\breve h^2 = 0$. Lemma 3.1 (3) gives the pairings.

(2) $t_*h_{b,\mathrm v1}(V)+\breve h^1_{b,\mathrm v1}(V)\in\ker L_b$ (III.D$'''$ Proposition 3.1 (3)), so
$\widehat{L_b}(0)\breve h^1 = -L_1h_{b,\mathrm v1}(V)$, and by III.F$'''$ Remark 2.3,
$h_{b,\mathrm v1}(V) = \frac12\dot g^\Upsilon_b(0,[A,A_V])$. Lemma 3.1 (2) then gives 0 against $h^*_{\mathrm s0}$,
$h^*_{\mathrm s1}$, and $-\frac12\cdot2\pi^2\mu\langle[A,A_V],A_{V'}\rangle_F = \pi^2\mu\langle A_V,[A,A_{V'}]\rangle_F$
against $h^*_{\mathrm v1}(V')$. By (4.2),
$\lambda^\sharp_{\breve h^1_{b,\mathrm v1}(V)}(W) = \pi^2\mu\langle A_V,W\rangle_F$ for
$W\in\mathrm{im}\,\mathrm{ad}_{A(b)}$. Now $\lambda^\sharp_{\breve h^1_{b,\mathrm v1}(V)}(W) =
-\lim_R\langle[\widehat{L_b}(0),\chi_R]\breve h^1_{b,\mathrm v1}(V),h^\sharp_{b,\mathrm v1}(W)\rangle$ (insert $\chi_R$
into (4.1): $\widehat{L_b}(0)^*$ of the compactly supported side is exact, and the limit of
$\langle\chi_R\widehat{L_b}(0)v,h^\sharp\rangle-\langle\chi_Rv,\widehat{L_b}(0)^*h^\sharp\rangle$ is (4.1)). Its weights
are $-1$ and $3$ with $[\widehat{L_b}(0),\chi_R]\in\rho^2\mathrm{Diff}^1_{\mathrm b}$, excess 0, so as in Lemma 2.2 (3)
it is the integral of the leading terms: $\bar h^1_{\mathrm v1}(V)$ of III.D$'''$ (3.3), independent of $b$;
$\bar h^\sharp(W) = \mu\rho^3(dt_*+\kappa_C\,d|x|)\otimes_s\rho V(W)$ of III.E$'$ (3.3), which depends on $b$ only
through $\mu$; and the model operator. So $\lambda^\sharp_{\breve h^1_{b,\mathrm v1}(V)}(W) = \mu\,c(V,W)$ with $c$ a
bilinear form independent of $b$. For $b = (\mu,A)$ in the parameter neighbourhood,
$c(V,W) = \pi^2\langle A_V,W\rangle_F$ on $\mathrm{im}\,\mathrm{ad}_A$ (Lemma 3.1 (2) holds at every such $b$, spinning
or not, with the same value, as the leading term $2\mu\rho^3(dt_*+2\,d|x|)\otimes_s\rho V(\dot A)$ (corrected at D238)
of $\dot g^\Upsilon_b(0,\dot A)$, III.E$'$ (2.2), does not depend on $A$); and these images, for $A$ small, span
$\mathfrak{so}(4)$ ($\mathrm{im}\,\mathrm{ad}_{\epsilon E_{12}} = \mathrm{span}\{E_{13},E_{14},E_{23},E_{24}\}$,
$\mathrm{im}\,\mathrm{ad}_{\epsilon E_{13}}\ni E_{12},E_{34}$). So $c(V,\cdot) = \pi^2\langle A_V,\cdot\rangle_F$ on
$\mathfrak{so}(4)$. $\square$

## 5. The physical large zero energy states ([Hin26] Proposition 8.14 at n = 4)

Let $\tau$ be one of the types s2, v2, t2, and $Y$ a harmonic of that type and degree 2 ($S\in\mathcal S_2$,
$V\in\mathcal V_2$, or a trace-free divergence-free tensor harmonic of degree 2). By III.F$'$ Proposition 2.3, $-2$ is a
simple indicial root of $\widehat{L_b}(0)$ at $\tau$ (the root $-l$ at $l = 2$), so
$\ker N_\tau(\widehat{\bar L}(0),-2)$ is one-dimensional for each $Y$; let $\bar h_\tau(Y) = \rho^{-2}\bar u_\tau(Y)$
span it, linearly in $Y$. Since $\bar L$ is homogeneous under dilations, $\widehat{\bar L}(0)\bar h_\tau(Y) = 0$ near
$\partial X$.

**Proposition 5.1 ([Hin26] Proposition 8.14 (1) at n = 4).** There is an index set $\mathcal E_{\mathrm{ind}}$ such that
for all $b$ near $b_0$ there are
$$h^{(-2)}_{b,\tau}(Y)\in\mathcal A^{(-2,0)\cup(-2+\mathcal E_{\mathrm{ind}})}(\bar X;S^2T^*X),
\qquad\tau\in\{\mathrm s2,\mathrm v2,\mathrm t2\},\tag{5.1}$$
linear in $Y$ and smooth in $b$, with $\rho^{-2}$ leading term $\bar h_\tau(Y)$, in
$\ker D_{g_b}\mathrm{Ric}\cap\ker\delta_{g_b,E_\Upsilon}G_{g_b}$, hence in $\ker\widehat{L_b}(0)$. Their leading terms
span $\ker N_\tau(\widehat{\bar L}(0),-2)$ for each $\tau$.

*Proof.* It suffices to treat $Y$ in a basis; we suppress $Y$ and $\tau$.

*Step 1: formal solution.* $f_b := \widehat{L_b}(0)(\chi\bar h)\in\rho^2C^\infty+C^\infty_c$, since
$\widehat{L_b}(0)-\widehat{\bar L}(0)\in\rho^4\mathrm{Diff}^2_{\mathrm b}$ (III.F Lemma 2.1). Near $\partial X$,
$\widehat{L_b}(0) = \rho^2A$ with $A$ an elliptic b-operator whose normal operator does not depend on $b$ (I.C
(1.1)-(1.3); III.F Lemma 2.1). III.A Lemma 1.5 gives $h'_{b,1}\in\mathcal A^{\mathcal F}$, $\mathcal F$ built from
$(0,0)$ and the roots (with logarithms at the integer roots $\ge0$), smooth in $b$, with
$\widehat{L_b}(0)h^{\approx}_b\in\mathcal A^{N}$ for a fixed large $N$, $h^\approx_b := \chi\bar h+h'_{b,1}$;
$\mathcal F\subset-2+\mathcal E_{\mathrm{ind}}$ as $\min\mathrm{Re}\,\mathcal F\ge0$.

*Step 2: the obstructions.* By III.F$'''$ Proposition 4.1 (2) and Corollary 4.2 (2), $\widehat{L_b}(0)h = f$ is
solvable, smoothly in $b$, for $f\in\mathcal A^{\alpha+2}$ orthogonal to the eleven dual states. (a)
$\langle\widehat{L_b}(0)h^\approx_b,h^*_{b,\mathrm s0}\rangle = \langle h^\approx_b,\widehat{L_b}(0)^*h^*_{b,\mathrm
s0}\rangle = 0$: $h^*_{b,\mathrm s0}\in\dot H^{0,C_0+3}_{\mathrm b}$, $C_0>1$, so the boundary terms, $O(R^{1-C_0})$,
vanish. (b) $\lambda_{\mathrm s1}(S') := \langle\widehat{L_b}(0)h^\approx_b,h^*_{b,\mathrm s1}(S')\rangle$, a linear
form on $\mathcal S_1$, smooth in $b$. (c) By (4.2), $\langle\widehat{L_b}(0)h^\approx_b,h^*_{b,\mathrm v1}(V')\rangle =
\lambda^\sharp_{h^\approx_b}([A(b),A_{V'}])$, with $\lambda^\sharp_{h^\approx_b}$ a linear form on $\mathfrak{so}(4)$,
smooth in $b$. Let $S_1\in\mathcal S_1$ solve
$\lambda_{\mathrm s1}(\cdot)-\frac{3\pi^2}2\mu\,\xi_{S_1}\cdot\xi_{(\cdot)} = 0$ (Lemma 4.1 (1)), and
$V_1\in\mathcal V_1$ solve
$$\lambda^\sharp_{h^\approx_b}+\lambda^\sharp_{\breve h^2_{b,\mathrm s1}(S_1)}+\pi^2\mu\,\langle A_{V_1},\cdot\rangle_F
 = 0\quad\text{on }\mathfrak{so}(4)\tag{5.2}$$
(Lemma 4.1 (2); $\lambda^\sharp_{\breve h^2_{b,\mathrm s1}(S_1)}$ is defined since $\breve h^2_{b,\mathrm s1}$ has
weight $-1$ and $\widehat{L_b}(0)\breve h^2_{b,\mathrm s1}$, by Lemma 4.1 (1), weight $\ge2$). Both are smooth in $b$.
Put $h^{\approx,2}_b := h^\approx_b+\breve h^2_{b,\mathrm s1}(S_1)+\breve h^1_{b,\mathrm v1}(V_1)$. Then
$\widehat{L_b}(0)h^{\approx,2}_b$ pairs to 0 with all eleven dual states: with $h^*_{\mathrm s0}$ by (a) and Lemma 4.1;
with $h^*_{\mathrm s1}$ by the choice of $S_1$ and Lemma 4.1 (2) ($\breve h^1_{\mathrm v1}$ pairs to 0); with
$h^*_{\mathrm v1}(V')$ by (4.2) for each summand and (5.2) at $W = [A(b),A_{V'}]$.

*Step 3: the state.* $\widehat{L_b}(0)$ maps $\breve h^2_{b,\mathrm s1}(S_1)$ and $\breve h^1_{b,\mathrm v1}(V_1)$, of
weight $-1$ with leading terms annihilated by $N(\widehat{\bar L}(0),-1)$ (III.D$'''$ Proposition 3.1 (2)-(3)), into
$\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$, so
$\widehat{L_b}(0)h^{\approx,2}_b\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$, smoothly in $b$. III.A Lemma
1.5, applied to its $\rho^2$ terms, gives $h_{b,(0)}\in\mathcal A^{(0,k)}$ for some $k$, smooth in $b$, with
$f_b := -\widehat{L_b}(0)(h^{\approx,2}_b+h_{b,(0)})\in\mathcal A^{2+\epsilon_{\mathrm{ind}}}$; and
$\langle\widehat{L_b}(0)h_{b,(0)},h^*\rangle = \langle h_{b,(0)},\widehat{L_b}(0)^*h^*\rangle = 0$ for the dual states
(weight $\ge3$: boundary terms $O(R^{-1}\log^kR)$), so $f_b$ is orthogonal to all of them. III.F$'''$ Corollary 4.2 (2)
with $\alpha\in(0,\epsilon_{\mathrm{ind}})$ gives $u_b\in\mathcal A^{\alpha-\epsilon}$, smooth in $b$, with
$\widehat{L_b}(0)u_b = f_b$. Every term of $f_b$ is polyhomogeneous: $h^\approx_b$ by its construction (III.A Lemma
1.5), $\breve h^2_{b,\mathrm s1}(S_1)$ and $\breve h^1_{b,\mathrm v1}(V_1)$ in
$\mathcal A^{(-1,0)\cup(-1+\mathcal E_{\mathrm{ind}})}$ by III.D$'''$ Proposition 3.1 (2)-(3), and $h_{b,(0)}$; and
$\widehat{L_b}(0)$ has smooth coefficients. So $u_b$, which solves $\rho^2Au_b = f_b$ near $\partial X$ with $A$
b-elliptic, is polyhomogeneous by III.A Lemma 1.4, as in III.D$'$ Lemma 5.1 (2), with an index set built from the
indicial roots of $\widehat{L_b}(0)$ with real part $>\alpha-\epsilon$ and from that of $f_b$, both independent of $b$
(the roots are the model's, III.F$'$ Lemma 2.1). (This index set contains the roots $\lambda^C_{\cdot,+}-1$ just above
1, harmless here, which the low-energy parts must carry; the ninety-seventh verifier.) Then
$$h^{(-2)}_b := h^{\approx,2}_b+h_{b,(0)}+u_b\in\ker\widehat{L_b}(0),\tag{5.3}$$
with leading term $\bar h$ and $h^{(-2)}_b-\chi\bar h\in\mathcal A^{(-1,0)\cup(-1+\mathcal E_{\mathrm{ind}})}+\mathcal
A^{\mathcal F}+\mathcal A^{(0,k)}+\mathcal A^{\mathcal E'}\subset\mathcal A^{-2+\mathcal E_{\mathrm{ind}}}$,
$\mathcal E'$ the index set of $u_b$ just found; its index set is that of (5.1), independent of $b$. (Before D235 this
step placed $u_b$ in the conormal space $\mathcal A^{\alpha-\epsilon}$ only, which no polyhomogeneous space contains;
the ninety-seventh verifier.)

*Step 4 (the source's generalized companions)* is not needed here; see (F$''''$3).

*Step 5: the gauge.* $\eta := \delta_{g_b,E_\Upsilon}G_{g_b}h^{(-2)}_b$ has weight $-1$, and the second Bianchi identity
gives $\widehat{\Box^C_b}(0)\eta = 2\delta_{g_b}G_{g_b}\widehat{L_b}(0)h^{(-2)}_b = 0$. In the Euclidean weight of
III.E, $\eta\in\bar H^{s,\alpha_C}_{\mathrm b}$ for every $s$ and every $\alpha_C<-3$; taking $\alpha_C+2\in[-C_0,-1)$
(possible as $C_0>1$), III.E Theorem 1.1 (2) gives $\eta = 0$; then
$D_{g_b}\mathrm{Ric}(h^{(-2)}_b) = \widehat{L_b}(0)h^{(-2)}_b = 0$. $\square$

## 6. Findings

(F$''''$1) *The reduction of Lemma 8.12 written out.* The source's "applies verbatim" covers an integration by parts of
three kinds (the gauge term, the self-adjointness of $G\circ D\mathrm{Ric}$ with $|dg_b| = |dt_*||dx|$, and
$D\mathrm{Ric}\circ\delta^* = 0$), here Lemma 2.1 and Lemma 2.2, with the conditions under which each boundary term
vanishes, and the invariance under decaying gauge terms and changes of time function that lets the record's Minkowski
computations be used. At $n = 4$ the boundary terms are weighted by $|dx| = \rho^{-4}\mu_{\mathrm b}$, and the critical
weight is $a+c = 2$.

(F$''''$2) *Lemma 8.15 (2) without a direct computation.* The source evaluates the vector type pairing twice, by Remark
8.10 and directly ((8.30)). Here Remark 8.10 gives it on $\mathrm{im}\,\mathrm{ad}_{A(b)}$, and the functional
$\lambda^\sharp$ of (4.1) depends on $b$ only through $\mu$, so the union of these images over small spins, which spans
$\mathfrak{so}(4)$, gives it everywhere:
$\lambda^\sharp_{\breve h^1_{\mathrm v1}(V)} = \pi^2\mu\langle A_V,\cdot\rangle_F$, the source's
$-8\pi m\langle a(V),\cdot\rangle$ with $\mathfrak{so}(4)$'s trace form for the dot product (and the normalisations of
(F$''''$4)).

(F$''''$3) *Which states.* The source constructs physical states at $-2$ (s2, v2) with generalized companions and at
$-3$ (s3, v3). Proposition 5.1 constructs those at $-2$, the tensor type t2 included, which four dimensions lacks,
without companions. Which states the low-energy expansion needs is decided by the slowest term at $\iota^+$, the subject
of the part on [Hin26] sections 9-11; the record's bookkeeping (`window5.py` W2, exact) shows that for every order in
$(1,2]$ only the states at $-2$ without companions enter, the window being $[-2,0]$ or $[-\frac52,0]$. The source's Step
4 would need $-3$ not to be a root at s2, v2 and t2, which holds at the record's point (`physical5.py` Y3).

(F$''''$4) *Step 2 modified.* The source's Step 2 uses that the centre-of-mass pairings vanish against the rotations'
dual states ("By Lemma 8.15, the left-hand side of (8.34) is independent of the choice of $V_1$", p. 161). At $n = 4$
these entries are of negative excess, not determined by the leading terms, and not shown to vanish away from $b_0$; here
they are absorbed: the s1 equation is solved first (the vector type states pair to 0 with the s1 dual states), and the
v1 equation (5.2) is solved on all of $\mathfrak{so}(4)$ with the centre-of-mass contribution included. The source's
printed "$-8\pi m\,a(V_1) = v_b$" has the sign reversed against its (8.33), and its (8.35) prints
$\lambda_{b,\mathrm s1}$ for $\lambda_{b,\mathrm v1}$ (the record's supplement 10.34 (b)).

(F$''''$5) *Values.* At $n = 4$: $3\pi^2\dot\mu$, $2\pi^2\mu\langle\dot A,A'\rangle_F$ and
$\frac{3\pi^2}2\mu\,\xi_S\cdot\xi_{S'}$ for $L_b$ of III.F (1.1), with the dual states of III.E; the source's are for
$2L_b$, with $dt$ in place of $-d\bar t$ for the s0 dual state, which changes that entry's sign.
