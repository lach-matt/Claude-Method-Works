# Part III.I$'''''''$. Undoing the parameter changes, n = 4 ([Hin26] section 11.6.2)

*Status.* Proved (D269: verifier 114 read the repairs, correct; status synchronised with the README at D325). Verified
(D268: the hundred-and-thirteenth verifier; no major finding, two minor ones and seven nits seated, to be read). Written
(D265). This part proves, at spatial dimension $n = 4$, [Hin26] section 11.6.2 (pp. 256-262): the correction terms that
let a source generate the change of the black hole parameters and the centre-of-mass shift of Part III.I$''''''$ (the
source's (11.134a)-(11.135b), Definition 11.37, Lemma 11.38), the gauge-fixed Einstein operator with all modification
parameters (Definition 11.40), its linearisation in them (Lemma 11.41), and their elimination (Definitions 11.42, 11.44,
Lemmas 11.43, 11.45, Corollary 11.46): for a source with a little more than $t_*^{-2}$-decay at $K^+$ there is a unique
choice of the parameters for which the forward solution decays at $K^+$.

*What n = 4 changes.* The scheme is the source's. Three things differ. There is no logarithmic centre-of-mass term (Part
III.I$''''''$ (I$''''''$1)), so there are three parameters, not four, and the source's (11.136)-(11.138b),
$h^{(0,1)}_{\mathrm s1}$, $\vartheta^{(0,1)}_{\mathrm s1}$ and its Remark 11.39 are not needed. The corrections have no
logarithm, so the cancellation of a $(3,1)$-coefficient behind (11.140) is not needed. And the centre-of-mass shift
cannot be undone by a correction alone: the source's metric term $-d\chi_K\otimes_s\omega^{(0)}_{b_0,\mathrm s1}$ has
$\iota^+$-order 1, outside the class $\mathcal X$ at $n = 4$ ($\min\mathrm{Re}\,\mathcal E_+>1$, III.I (1.3)), for the
reason that made Part III.I$''''$ re-centre the boost ((I$''''$1)). The exterior background is translated instead, as it
is boosted (Lemmas 1.1-1.2), and the correction becomes $-d\chi_K\otimes_s(\omega_{\mathrm s1}-\Theta w^0)$, of
$\iota^+$-order 3 ((I$'''''''$1)). Everything is at $b = b_0$, as in III.I Theorem 5.3 and Remark 5.4. Notation: Parts
II.E, III.B, III.D$''$, III.F$'''$, III.H and III.I-III.I$''''''$; no instrument is used.

## 1. Setting

*Notation.* The cut-offs $\chi_K,\chi^\flat_K,\chi_r,\chi_{\mathrm{IVP}},\chi^\sharp_{\mathrm{IVP}}$, the set $\mathcal
C$ (on which every derivative of $\chi_K$ is supported), the factor $\Theta =
\chi_r(|x|)\chi^\sharp_{\mathrm{IVP}}(1-\chi^\flat_K)$, the boosts $\phi_S$ and $w(S)$, the conventions III.I$''''$
(1.2) and the identities (i)-(iii) of III.I$''''$ section 1, the states $\omega_{\mathrm s1}(S) =
\omega^{(0)}_{b_0,\mathrm s1}(S)$, $h(S) = \delta^*_{g_{b_0}}\omega_{\mathrm s1}(S)$ and $h^{\le1}_\natural(S)$, and the
corrections $h^{(-1)}$, $\vartheta^{(-1)}$, $\vartheta_\sharp$ are Part III.I$''''$'s (sections 1-2). $\mathfrak b =
\mathbb R\times\mathfrak{so}(4)$ is the parameter space of III.F$'''$ Proposition 2.2. For $\dot b\in\mathfrak b$ put
$\dot g_{b_0}(\dot b) := \partial_bg_b|_{b=b_0}(\dot b)$, $\dot\omega(\dot b) := \dot\omega_{b_0}(\dot b)$ and $\dot
g(\dot b) := \dot g^\Upsilon_{b_0}(\dot b) = \dot g_{b_0}(\dot b)+\delta^*_{g_{b_0}}\dot\omega(\dot b)$ (III.F$'''$
(2.1)), which is III.H section 1's state $\dot\mu\,\dot g^\Upsilon_{b_0}(1,0)+\dot g^\Upsilon_{b_0}(0,\dot A)$
(linearity, III.F$'''$ Proposition 2.2 (3)). In this part $\mathcal E_{\mathrm{ind}}$ is the union of the index sets of
III.D$''$ Proposition 3.1 and III.F$'''$ Proposition 2.2 at $b_0$. By III.F$'''$ Proposition 2.2 (1)-(2) and III.D$''$
Proposition 3.1 (as quoted in III.I$''''$ section 1), on $\bar X$ near infinity
$$\dot\omega(\dot b)\in\mathcal A^{(1,0)\cup(1+\mathcal E_{\mathrm{ind}})},\quad\dot g(\dot b)\in\mathcal A^{\mathcal
G},\quad\omega_{\mathrm s1}(S)-\bar\omega_{\mathrm s1}(S)\in\mathcal A^{\mathcal G},\quad h(S)\in\mathcal A^{\mathcal
G+1},\qquad\mathcal G := (2,0)\cup(2+\mathcal E_{\mathrm{ind}}),\tag{1.1}$$
with $\bar\omega_{\mathrm s1}(S_w) = d(|x|S_w) = w\cdot dx$ for $S_w(\omega) = w\cdot\omega$, $w\in\mathbb R^4$. $\dot
g(\dot b)$ and $h(S)$ lie in $\ker D_{g_{b_0}}\mathrm{Ric}\cap\ker\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}$ (III.F$'''$
Proposition 2.2 (2); III.I$''''$ section 1), and $(\dot b,S)\mapsto\dot g(\dot b)+h(S)$ is injective, by the rows of
III.H (3.1). Assume
$$2+\mathcal E_{\mathrm{ind}}\subset\mathcal E_+,\tag{1.2}$$
III.I$''''$ (2.4) for this union, so $\mathcal G\subset\mathcal E_+$ by III.I (1.3). $\ell_I$ is fixed as in
III.I$'''''$ (1.2), and, as in III.I$''''$ section 4, $\ell_I\le a_I$ (so $a_I\ge2$).
$\alpha_K\in(2,\min(a_K,2+\epsilon_{\mathrm{ind}},\frac52))$ is as in III.I$''''''$ Proposition 2.1
($\epsilon_{\mathrm{ind}}$ III.G$''''$ Proposition 5.1's), and
$$\mathcal Y := \bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),4-\epsilon,\alpha_K}_{\mathrm
b}(\Omega_*;S^2T^*)^{\bullet,-},$$
real sections, is the source's class (11.116). A fixed large $d$ is used throughout, and "$h$ small" means $h\in\mathcal
X^\infty$ vanishing near $\{t^\flat_* = 1\}$ with small $\mathcal X^d$-norm.

*Translations.* For $S = S_w\in\mathcal S_1$ put $Y_S := w\cdot\partial_x = \eta^{-1}\bar\omega_{\mathrm s1}(S)$,
$V^0(S) := \frac12\Theta Y_S$, $\psi_S := \exp V^0(S)$ and $w^0(S) := g_{b_0}(Y_S,\cdot)$, so that
$g_{b_0}(V^0(S),\cdot) = \frac12\Theta w^0(S)$ and, by $\mathcal L_Xg = 2\delta^*_g(g(X,\cdot))$,
$\partial_S\psi^*_{-S}g_{b_0}|_{S=0}(\dot S) = -\delta^*_{g_{b_0}}(\Theta w^0(\dot S))$.

**Lemma 1.1 (translations; III.B Lemmas 5.1-5.2 for translations).** (a) $V^0(S)$ lifts to a b-vector field on $M$,
vanishing near $\Sigma^{\mathrm{past}}\cup K^+\cup\Sigma^{\mathrm{int}}$ and on $\{|x|\le5R_1\}$ and tangent to every
boundary hypersurface; so $\psi_S$ is a diffeomorphism of $M$ with the properties stated for $\phi_{S_w}$ in III.B Lemma
5.1, depending smoothly on $S$.

(b) There are $w_0>0$ and a neighbourhood $\mathcal N$ of $\mathrm{supp}(\chi_{\mathrm{IVP}}(1-\chi_K))$ such that for
$|w|<w_0$ every integral curve of $V^0(S_w)$ starting in $\mathcal N$ stays, for times in $[0,1]$, either in $\{\Theta =
1\}$, where $\psi_{S_w}$ is the translation $\tau_{w/2}:(t,x)\mapsto(t,x+\frac w2)$, or in a fixed compact subset of $M$
disjoint from $I_0\cup\mathscr I^+\cup\iota^+\cup K^+$.

(c) For $b$ near $b_0$ and $a\in\mathbb R^4$ small, $\tau_a^*g_b-g_b$ has Cartesian components in $|x|^{-3}C^\infty(\bar
X)$ on $\{|x|\ge4R_1\}$; it is stationary, smooth in $a$ and $O(|a|)$.

*Proof.* (a) $Y_S$ has constant Cartesian coefficients, so on the radial compactification of $\mathbb R^{1+4}$ it is a
boundary defining function times a b-vector field; it is tangent to every submanifold of the boundary, $Y_+$ included,
and lifts to a b-vector field on $M$ tangent to every boundary hypersurface. The factor $\Theta$ is the one of III.B
Lemma 5.1, with its vanishing properties, and the rest is that lemma's proof. (b) As in III.B Lemma 5.2: the strict
nesting of the cut-offs gives $\{\Theta = 1\}$ a neighbourhood margin around
$\mathrm{supp}(\chi_{\mathrm{IVP}}(1-\chi_K))$ near $I_0\cup\mathscr I^+\cup\iota^+$, so a slightly larger neighbourhood
$\mathcal N$ still has one; $M$ is compact and the time-$[0,1]$ flow of $V^0(S_w)$, linear in $w$, tends to the identity
uniformly as $w\to0$; on $\{\Theta = 1\}$, $V^0(S_w) = \frac12w\cdot\partial_x$, whose time-1 flow is $\tau_{w/2}$. (c)
$g_b$ is stationary with $g_b-\eta\in|x|^{-2}C^\infty(\bar X)$ on $\{|x|\ge3R_1\}$ (III.B (3.5), Proposition 3.6), and
$\tau^*_a$ acts on Cartesian components by $x\mapsto x+a$. For $F\in|x|^{-2}C^\infty(\bar X)$, $F(x+a)-F(x) =
\int_0^1a\cdot(\nabla F)(x+sa)\,ds$, with $\nabla F\in|x|^{-3}C^\infty(\bar X)$; $x\mapsto x+sa$ extends to a
diffeomorphism of $\bar X$ near infinity that is the identity on $\partial\bar X$, so composition with it preserves
$|x|^{-3}C^\infty(\bar X)$, uniformly in $s$ and smoothly in $a$. $\square$

**Definition 1.2 (the translated background).** For $\vec p = (S,b-b_0,S^{(0)}_1)$ with $S,S^{(0)}_1\in\mathcal S_1$
small and $b$ near $b_0$,
$$g_{\vec p} := (1-\chi_K)(\psi_{-S^{(0)}_1}\circ\phi_{-S})^*g_{b_0}+\chi_Kg_b,\tag{1.3}$$
so that $g_{(S,b-b_0,0)} = g_{b_0,b,-S}$ (III.I (1.1)).

**Lemma 1.3 (properties of the translated background).** For $|S|$, $|S^{(0)}_1|$ and $|b-b_0|$ small:

(a) III.B (5.3) holds with $(\psi_{-S^{(0)}_1}\circ\phi_{-S})^*g_b$ in place of $\phi^*_{S_w}g_b$ ($S_w = -S$), with the
same leading term; hence III.I Lemma 3.6 holds for $g_{\vec p}$ (in particular (3.5) of III.I and $g_{\vec p}\in\mathcal
G^+$), with seminorms $O(|b-b_0|+|S|+|S^{(0)}_1|)$, $\vec p\mapsto g_{\vec p}-g_b$ smooth into that class, and
$\partial_{S^{(0)}_1}g_{\vec p}$, $\partial_Sg_{\vec p}$ in the class $\mathcal K$ of III.I$''''$ section 3; and III.I
Lemma 4.3 holds for $g_{\vec p}$.

(b) III.I Propositions 3.3, 3.4, 4.1, Corollaries 4.2, 5.2 and Theorem 5.3 hold for $g_0 := g_{\vec p}$ ($b = b_0$ in
Theorem 5.3), with $|S|$ replaced by $|S|+|S^{(0)}_1|$, and Theorem 5.3's continuity holds in $(S,S^{(0)}_1,h)$.

(c) On $\{\Theta = 1\}\cap\mathrm{supp}(1-\chi_K)$ near $(\iota^+)^\circ$, $\psi_{-S^{(0)}_1}\circ\phi_{-S}$ is a
Poincaré motion (a Lorentz boost followed by a translation), and $g_{\vec p}-\eta$, $\partial_Sg_{\vec p}$,
$\partial_{S^{(0)}_1}g_{\vec p}$ lie in $\rho_+^2C^\infty$ near $(\iota^+)^\circ$ (with $b = b_0$). On
$\mathrm{int}\,\chi_K^{-1}(0)$, $g_{\vec p}$ is Ricci flat.

*Proof.* (a) Let $p\in\mathrm{supp}(\chi_{\mathrm{IVP}}(1-\chi_K))$. On III.B Lemma 5.2's first alternative $\phi_{-S}$
is the exact boost near $p$, and $\phi_{-S}(p)\in\mathcal N$ for $|S|$ small (the flow tends to the identity), so by
Lemma 1.1 (b) $\psi_{-S^{(0)}_1}$ is the translation $\tau := \tau_{-w/2}$ ($S^{(0)}_1 = S_w$) near $\phi_{-S}(p)$, or
$p$ lies in a fixed compact set away from the faces at infinity, where everything is smooth. On the former,
$$(\psi_{-S^{(0)}_1}\circ\phi_{-S})^*g_b = \phi^*_{-S}g_b+\phi^*_{-S}(\tau^*g_b-g_b).$$
By Lemma 1.1 (c), $\tau^*g_b-g_b\in|x|^{-3}C^\infty(\bar X)$ there, and on that region $|x|^{-3}C^\infty(\bar
X)\subset\rho_0^3\rho_I^3\rho_+^3C^\infty$ ($C^\infty(\bar X)$ lifts to $C^\infty(M)$ there, III.B section 2; as in
III.B Lemma 5.2's proof), a class which $\phi^*_{-S}$ preserves (III.B Lemma 5.1) and which lies in (5.3)'s remainder
class $\rho_0^2\rho_I^3\rho_+^2C^\infty$. This is (5.3) for the composite. III.I Lemma 3.6's proof uses (5.3) on the
first alternative, smoothness on the second and III.B Proposition 3.6, so it applies verbatim; the dependence on
$(S,S^{(0)}_1)$ is smooth as the flows and $h_{S_w}$ are, and the parameter derivatives vanish near $K^+$ (where
$g_{\vec p} = g_b$), so they lie in $\mathcal K$, as III.I$''''$ section 3 states for $S$. III.I Lemma 4.3's proof uses
that the exterior metric is Ricci flat (it is a pullback of $g_{b_0}$), Lemma 3.6, and that the exterior metric minus
$\eta$ lies in $\rho_+^2C^\infty$ near $(\iota^+)^\circ$, which is (c).

(b) III.I Propositions 3.3, 3.4 and 4.1 and Corollary 5.2 are stated for $g_0\in\mathcal G^+$ with III.I (3.5)
(Proposition 3.4: "or more generally"), which (a) gives; Corollary 4.2 rests on Proposition 4.1 and Lemma 4.3; Theorem
5.3's proof uses $g_0$ only through Corollary 5.2 and III.I (3.7), whose bound is linear in the seminorms of
$g_0-g_{b_0}$, now $O(|S|+|S^{(0)}_1|)$ at $b = b_0$; the continuity follows as $g_{\vec p}$ depends smoothly on $\vec
p$.

(c) On $\{\Theta = 1\}$ both flows are exact (III.B Lemma 5.2, Lemma 1.1 (b)), so the composite is a Lorentz boost
followed by a translation, which preserves $\eta$; with $g_{b_0}-\eta\in|x|^{-2}C^\infty$ and $|x|\ge t/20$ there,
$g_{\vec p}-\eta\in\rho_+^2C^\infty$ near $(\iota^+)^\circ$, the part $\chi_Kg_{b_0}$ included. $\partial_S$ and
$\partial_{S^{(0)}_1}$ of $(\psi\circ\phi)^*g_{b_0}$ are Lie derivatives of the pulled-back metric along a generator of
the Poincaré group (a linear or a constant vector field, which is a b-vector field and Killing for $\eta$), so they map
$\eta+\rho_+^2C^\infty$ into $\rho_+^2C^\infty$. On $\mathrm{int}\,\chi_K^{-1}(0)$, $g_{\vec p}$ is a pullback of
$g_{b_0}$ by a diffeomorphism. $\square$

## 2. The correction terms and the operator ([Hin26] (11.134a)-(11.143))

**Definition 2.1 ([Hin26] Definition 11.37 at n = 4).** For $\dot b\in\mathfrak b$ and $S\in\mathcal S_1$,
$$h^{(0)}(\dot b) := -[\delta^*_{g_{b_0}},\chi_K]\dot\omega(\dot b) = -d\chi_K\otimes_s\dot\omega(\dot
b),\qquad\vartheta^{(0)}(\dot b) := [\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}},\chi_K]\dot g(\dot b),$$
$$h^{(0)}_{\mathrm s1}(S) := -d\chi_K\otimes_s\big(\omega_{\mathrm s1}(S)-\Theta
w^0(S)\big),\qquad\vartheta^{(0)}_{\mathrm s1}(S) := [\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}},\chi_K]h(S),$$
and, with the counterterms of the source's Remark 11.27 as in III.I$''''$ Definition 2.1, $\vartheta^{(0)}_\sharp :=
\vartheta^{(0)}-\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}h^{(0)}$ and $\vartheta^{(0)}_{\mathrm s1,\sharp} :=
\vartheta^{(0)}_{\mathrm s1}-\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}h^{(0)}_{\mathrm s1}$. All are linear. By III.I$''''$
(1.2), $[\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}},\chi_K]k = -\iota_{g_{b_0}^{-1}d\chi_K}G_{g_{b_0}}k$.

The source's $h^{(0)}_{\mathrm s1}$ has $\omega^{(0)}_{b_0,\mathrm s1}$ alone; $\Theta w^0(S)$ is the translation of
(1.3), as $\Theta w(S)$ is the boost's in III.I$''''$ Definition 2.1. The source's $h^{(0,1)}_{\mathrm s1}$,
$\vartheta^{(0,1)}_{\mathrm s1}$ have no counterpart.

**Lemma 2.2 ([Hin26] Lemma 11.38 at n = 4).** The tensors of Definition 2.1 are smooth, supported in $\mathcal C$ (so
disjoint from $\mathscr I^+$ and $K^+$ and from $\{t^\flat_*<10\}$), with seminorms $O(|\dot b|)$, resp. $O(|S|)$, and
near $(\iota^+)^\circ$
$$h^{(0)}(\dot b)\in\mathcal A^{\mathcal G},\quad h^{(0)}_{\mathrm s1}(S)\in\mathcal A^{\mathcal G+1},\quad
D_{g_0}\mathrm{Ric}\big(h^{(0)}(\dot b)\big)\in\mathcal A^{\mathcal G+2},\quad D_{g_0}\mathrm{Ric}\big(h^{(0)}_{\mathrm
s1}(S)\big)\in\mathcal A^{\mathcal G+3},$$
$$\vartheta^{(0)}(\dot b),\ \vartheta^{(0)}_\sharp(\dot b)\in\mathcal A^{\mathcal G+1},\qquad\vartheta^{(0)}_{\mathrm
s1}(S),\ \vartheta^{(0)}_{\mathrm s1,\sharp}(S)\in\mathcal A^{\mathcal G+2},\tag{2.1}$$
for every metric $g_0$ smooth on $M$ near $(\iota^+)^\circ$ with $g_0-\eta\in\rho_+C^\infty$ there.

*Proof.* Each has a factor $d\chi_K$, so it is supported in $\mathcal
C\subset\mathrm{supp}\,\chi_K\subset\{t^\flat_*\ge10\}$; it is smooth as $\dot\omega$, $\dot g$, $\omega_{\mathrm s1}$,
$w^0$, $\Theta$ and $h$ are. Near $(\iota^+)^\circ$, on $\mathcal C\cap\{t\ge T_1\}$, $\Theta = 1$ and $|x|\ge t/10$, so
$\mathcal A^{\mathcal E}(\bar X)$ lies in $\mathcal A^{\mathcal E}$ at $\iota^+$ (III.I$''''$ Lemma 1.2 (b)'s proof).
There, by (1.1), $\dot\omega\in\mathcal A^{(1,0)\cup(1+\mathcal E_{\mathrm{ind}})}$, $\dot g\in\mathcal A^{\mathcal G}$,
$h(S)\in\mathcal A^{\mathcal G+1}$, and
$$\omega_{\mathrm s1}(S)-w^0(S) = \big(\omega_{\mathrm s1}(S)-\bar\omega_{\mathrm
s1}(S)\big)+(\eta-g_{b_0})\eta^{-1}\bar\omega_{\mathrm s1}(S)\in\mathcal A^{\mathcal G},$$
the second term because $\bar\omega_{\mathrm s1}(S)$ has constant Cartesian components and
$g_{b_0}-\eta\in|x|^{-2}C^\infty$. With $d\chi_K\in\rho_+C^\infty$, $\iota_{g_{b_0}^{-1}d\chi_K}$ with coefficients in
$\rho_+C^\infty$, $D_{g_0}\mathrm{Ric}\in\rho_+^2\mathrm{Diff}^2_{\mathrm b}$ and
$\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}\in\rho_+\mathrm{Diff}^1_{\mathrm b}$ there (III.I$''''$ Lemma 2.2's proof),
(2.1) follows. $\square$

The source's Lemma 11.38 has $(1,1)\cup(1+\mathcal E_{\mathrm{ind}})$, $(1,0)\cup(1+\mathcal E_{\mathrm{ind}})$ for the
metric terms, and its (11.140) needs the vanishing of a $(3,1)$-coefficient ((11.82)); at $n = 4$ there is no logarithm,
and the translation raises $h^{(0)}_{\mathrm s1}$ from order 1 to order 3 ((I$'''''''$1)).

**Definition 2.3 ([Hin26] Definition 11.40 at n = 4, in the form of its Remark 11.27).** For $\vec p =
(S,b-b_0,S^{(0)}_1)$ small and $h\in\mathcal X^\infty$ with small $\mathcal X^d$-norm, with $g_0 := g_{\vec p}$,
$$h_{\mathrm{tot}}(\vec p) := h^{(-1)}(S)+h^{(0)}(b-b_0)+h^{(0)}_{\mathrm
s1}(S^{(0)}_1),\qquad\vartheta_{\mathrm{tot}}(\vec p) :=
\vartheta_\sharp(S)+\vartheta^{(0)}_\sharp(b-b_0)+\vartheta^{(0)}_{\mathrm s1,\sharp}(S^{(0)}_1),$$
$g' := g_0+h_{\mathrm{tot}}(\vec p)+h$, and
$$P_2(h,\vec p) := \mathrm{Ric}(g')-\delta^*_{g_0,E_C}\Big(\Upsilon^{E_\Upsilon}(g',g_0)-\vartheta_{\mathrm{tot}}(\vec
p)\Big),\qquad L_{h,\vec p} := D_hP_2(\cdot,\vec p)\text{ at }h.\tag{2.2}$$
$P_2(h,(S,0,0)) = P_1(h,S,b_0)$ (III.I$''''$ (2.2)) and $P_2(0,0) = 0$.

*Sizes.* The source's Remark 11.36 accepts metric terms of size $O(\rho_+)$ and gauge terms of size $O(\rho_+^2)$; at $n
= 4$ the metric terms lie in $\mathcal A^{\mathcal G}\subset\mathcal X$ (by (1.2)) and the gauge terms in $\mathcal
A^{\mathcal G+1}$, which $\delta^*_{g_0,E_C}\in\rho_+\mathrm{Diff}^1_{\mathrm b}$ maps to $\iota^+$-order 4, the order
of the sources from III.I$''''$ section 3 on.

**Lemma 2.4 (the parameter identities; [Hin26] (11.78b), (11.134b), (11.135b) at n = 4).** For $\dot S,\dot
S^{(0)}\in\mathcal S_1$ and $\dot b\in\mathfrak b$,
$$D_{\vec p}P_2(0,0)(\dot S,0,0) = L_{b_0}\big(\chi_Kh^{\le1}_\natural(\dot S)\big),\quad D_{\vec p}P_2(0,0)(0,\dot b,0)
= L_{b_0}\big(\chi_K\dot g(\dot b)\big),\quad D_{\vec p}P_2(0,0)(0,0,\dot S^{(0)}) = L_{b_0}\big(\chi_Kh(\dot
S^{(0)})\big).\tag{2.3}$$
All three are supported in $\mathcal C$, and $\chi_Kh^{\le1}_\natural(\dot S)$, $\chi_K\dot g(\dot b)$ and $\chi_Kh(\dot
S^{(0)})$, which vanish for $t^\flat_*<10$, are their forward solutions (II.E Proposition 3.4).

*Proof.* The first is III.I$''''$ Lemma 2.4 (with its support statement in III.I$''''$ Lemma 3.2), as $P_2 =
P_1(\cdot,\cdot,b_0)$ where $b = b_0$ and $S^{(0)}_1 = 0$. For the others: at $\vec p = 0$, $g' = g_0 = g_{b_0}$ and
$\Upsilon^{E_\Upsilon}(g_{b_0},g_{b_0})-\vartheta_{\mathrm{tot}}(0) = 0$, so for a parameter direction with $\dot g_0 :=
\partial g_0$, $\dot g' := \partial g'$, $\dot\vartheta := \partial\vartheta_{\mathrm{tot}}$, the derivative of
$\delta^*_{g_0,E_C}$ multiplies zero and, by (i),
$$DP_2 = D_{g_{b_0}}\mathrm{Ric}(\dot g')-\delta^*_{g_{b_0},E_C}\big(D_1\Upsilon(\dot g'-\dot
g_0)-\dot\vartheta\big),\qquad D_1\Upsilon := D_1\Upsilon^{E_\Upsilon}(g_{b_0},g_{b_0}) =
-\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}$$
(the last by (ii)). *The parameter $b$.* $\dot g_0 = \chi_K\dot g_{b_0}(\dot b)$, as only $\chi_Kg_b$ depends on $b$;
$\dot g'-\dot g_0 = h^{(0)}(\dot b)$ and $\dot\vartheta = \vartheta^{(0)}_\sharp(\dot b)$. By III.I$''''$ (1.2),
$h^{(0)}(\dot b) = \chi_K\delta^*\dot\omega-\delta^*(\chi_K\dot\omega)$, so $\dot g' = \chi_K\dot g(\dot
b)-\delta^*_{g_{b_0}}(\chi_K\dot\omega(\dot b))$ and $D\mathrm{Ric}(\dot g') = D\mathrm{Ric}(\chi_K\dot g(\dot b))$ by
(iii). And $D_1\Upsilon h^{(0)}-\vartheta^{(0)}_\sharp = -\delta Gh^{(0)}-\vartheta^{(0)}+\delta Gh^{(0)} =
-\vartheta^{(0)}(\dot b)$. So $DP_2 = D\mathrm{Ric}(\chi_K\dot g)+\delta^*_{E_C}\vartheta^{(0)}(\dot b)$; and as
$\delta_{E_\Upsilon}G\dot g = 0$, $L_{b_0}(\chi_K\dot g) = D\mathrm{Ric}(\chi_K\dot
g)+\delta^*_{E_C}[\delta_{E_\Upsilon}G,\chi_K]\dot g$, the same. *The parameter $S^{(0)}_1$.* $\dot g_0 =
-(1-\chi_K)\delta^*_{g_{b_0}}(\Theta w^0(\dot S^{(0)}))$ (Translations, above), $\dot g'-\dot g_0 = h^{(0)}_{\mathrm
s1}(\dot S^{(0)})$ and $\dot\vartheta = \vartheta^{(0)}_{\mathrm s1,\sharp}(\dot S^{(0)})$. With III.I$''''$ (1.2),
$-(1-\chi_K)\delta^*(\Theta w^0) = -\delta^*((1-\chi_K)\Theta w^0)-d\chi_K\otimes_s\Theta w^0$ and
$-d\chi_K\otimes_s\omega_{\mathrm s1} = \chi_Kh(\dot S^{(0)})-\delta^*(\chi_K\omega_{\mathrm s1})$, so
$$\dot g' = \chi_Kh(\dot S^{(0)})-\delta^*_{g_{b_0}}\big((1-\chi_K)\Theta w^0(\dot S^{(0)})+\chi_K\omega_{\mathrm
s1}(\dot S^{(0)})\big),$$
and $D\mathrm{Ric}(\dot g') = D\mathrm{Ric}(\chi_Kh(\dot S^{(0)}))$ by (iii). The gauge term is
$\delta^*_{E_C}\vartheta^{(0)}_{\mathrm s1}(\dot S^{(0)})$ as before, and $\delta_{E_\Upsilon}Gh = 0$ gives
$L_{b_0}(\chi_Kh)$. *Supports.* For $k\in\ker D_{g_{b_0}}\mathrm{Ric}$, $D\mathrm{Ric}(\chi_Kk) =
[D\mathrm{Ric},\chi_K]k$ is supported in $\mathcal C$, as are the $\vartheta$'s. $\square$

As in the source, (2.3) reads the late-time terms of Part III.I$''''''$ (2.1) as generated by changes of the parameters
of the final black hole and of its centre, with no change of the initial state.

**Lemma 2.5 (the linearisation in $h$; [Hin26] Definition 11.40's last paragraph at n = 4).** Let $\vec p =
(S,0,S^{(0)}_1)$ ($b = b_0$) and $h$ be small.

(a) $h_{\mathrm{tot}}(\vec p)\in\mathcal X^\infty$, $\|h_{\mathrm{tot}}(\vec p)\|_{\mathcal X^k}\le C_k|\vec p|$, and
$L_{h,\vec p} = L^{g',g_0}$ with $g_0 = g_{\vec p}$, $g' = g_0+h'$, $h' := h_{\mathrm{tot}}(\vec p)+h$.

(b) Every result of Parts III.I-III.I$''''''$ stated for $L_{h,S}$ (or $L^{g_S+h',g_S}$) holds for $L_{h,\vec p}$, with
$f^S_{h,\vec p}$ of Lemma 3.1 in place of III.I$''''$'s $f_{h,S}$.

(c) The bounds of III.I$''''$ Proposition 4.1 (1) and III.I$''''''$ Proposition 2.1 (of $\dot S$, $\tilde u$, resp.
$\dot b$, $\dot S^{(0)}_1$, $\tilde u$ by $f$, at each finite regularity) hold with constants uniform for $(h,\vec p)$
small.

*Proof.* (a) $\vartheta_{\mathrm{tot}}(\vec p)$ does not depend on $h$, so $D_hP_2 =
D_{g'}\mathrm{Ric}-\delta^*_{g_0,E_C}D_1\Upsilon^{E_\Upsilon}(g',g_0) = L^{g',g_0}$. By Lemma 2.2 and III.I$''''$ Lemma
2.2, $h_{\mathrm{tot}}(\vec p)$ ($= h^{(-1)}(S)+h^{(0)}_{\mathrm s1}(S^{(0)}_1)$ at $b = b_0$) is smooth, supported in
$\mathcal C$ and in $\mathcal A^{\mathcal G}$ near $(\iota^+)^\circ$, and $\mathcal G\subset\mathcal E_+$ by (1.2); so
it lies in $H^{\infty,(\mathcal E_+,a_+)}_{\mathrm b}$ at $\iota^+$ for every $a_+$, with norms $O(|\vec p|)$, as in
III.I$''''$ Lemma 2.5. (b) The proofs of those parts use the background $g_S$ only through III.I's results listed in
Lemma 1.3 (b), III.I Lemma 3.6's class and its smooth dependence on the parameter (III.I$''''$ Lemma 3.1), and, in
III.I$''''$ Lemma 3.2, through the two properties of Lemma 1.3 (c); and they use $h'$ only through $h'\in\mathcal X$
with small norm. Lemma 1.3 and (a) provide these for $g_{\vec p}$ and $h'$, and Lemma 3.1 (a) below is III.I$''''$ Lemma
3.2 for $P_2$. (c) In the proofs of these propositions every map is fixed by $L_{b_0}$, or is $L-L_{b_0}$, bounded by
III.I Proposition 4.1 (4.2) with the coefficient bounds of III.I Proposition 3.4, uniform for small $(h',\vec p)$ (Lemma
1.3 (b)), or is the solution map of III.I$''$ Proposition 5.1, or III.I$'$ Proposition 2.1 applied to $L$ itself
(III.I$'''$ Step 4, III.I$''''''$ Step 6), whose bounds are locally uniform: III.I$''$ Proposition 5.1's continuity
paragraph shows this for both, III.I$'$ Proposition 2.1's proof being constructive with bounds depending on $L$ only
through coefficient norms, locally uniform by III.I Proposition 3.4; III.I$''''$ Lemma 4.2 (a) is this argument for
$\dot S$. $\square$

## 3. The linearisation in the parameters ([Hin26] Lemma 11.41 at n = 4)

**Lemma 3.1 ([Hin26] Lemma 11.41 at n = 4).** Let $\vec p = (S,0,S^{(0)}_1)$ be small, $h\in\mathcal X^k$, $k\ge5$, with
small $\mathcal X^5$-norm, $\tilde{\mathcal E}_+ := \mathcal G\cup(\mathcal E_++\mathcal G)$ (III.I$''''$ (3.2) with
this part's $\mathcal G$), and
$$f^S_{h,\vec p}(S') := D_{\vec p}P_2(h,\vec p)(S',0,0),\quad f^b_{h,\vec p}(b') := D_{\vec p}P_2(h,\vec
p)(0,b',0),\quad f^{\mathrm s1}_{h,\vec p}(S'') := D_{\vec p}P_2(h,\vec p)(0,0,S'').$$

(a) $f^S_{h,\vec p}(S')$ and $f^{\mathrm s1}_{h,\vec p}(S'')$ satisfy III.I$''''$ (3.3) and the other statements of
III.I$''''$ Lemma 3.2: they vanish on $\mathrm{int}\,\chi_K^{-1}(1)$, and for $t^\flat_*<c$, $c\le10$, if $h$ does.

(b) $f^b_{h,\vec p}(b')$ is supported in $\mathrm{supp}\,\chi_K$ (so it vanishes near $\mathscr I^+$ and for
$t^\flat_*<10$), and for every $\epsilon>0$
$$f^b_{h,\vec p}(b')\in H^{k-2,\infty,(\tilde{\mathcal E}_++2,a_++4-\epsilon),a_K}_{\mathrm b}(\Omega_*);\tag{3.1}$$
if $h$ has $K^+$-weight $\ell_K>0$ in place of $a_K$, the $K^+$-weight of $f^b_{h,\vec p}(b')$ is $\ell_K$.

(c) All three are linear in the direction, with norms $O(|S'|)$, $O(|b'|)$, $O(|S''|)$, continuous in $(h,\vec p)$ with
$h\in\mathcal X^k$, and at $(h,\vec p) = (0,0)$ given by (2.3), supported in $\mathcal C$.

*Proof.* (a) *For $S$:* III.I$''''$ Lemma 3.2's proof, with $g_{\vec p}$, $h_{\mathrm{tot}}(\vec p)$,
$\vartheta_{\mathrm{tot}}(\vec p)$ for $g_S$, $h^{(-1)}(S)$, $\vartheta_\sharp(S)$: the $S$-derivative falls on $g_0$,
$h^{(-1)}(S)$ and $\vartheta_\sharp(S)$ only. On $U_K := \mathrm{int}\,\chi_K^{-1}(1)$, $P_2$ does not depend on $S$. On
$U_I := \mathrm{int}\,\chi_K^{-1}(0)$, $g_{\vec p}$ is Ricci flat (Lemma 1.3 (c)) and $h_{\mathrm{tot}}$,
$\vartheta_{\mathrm{tot}}$ vanish, so $f = \int_0^1\dot L_sh\,ds$ with $\dot L_s := \partial_S[L^{g_{\vec p}+sh,g_{\vec
p}}](S')$, and III.I$''''$ Lemma 3.1 applies, its proof needing $\partial_Sg_{\vec p}\in\mathcal K$ (Lemma 1.3 (a)). On
$U_\iota$, Lemma 1.3 (c) gives $g_0-\eta$, $k_0 := \partial_Sg_{\vec p}(S')\in\rho_+^2C^\infty$, and
$h_{\mathrm{tot}}\in\mathcal A^{\mathcal G}$, $\vartheta_{\mathrm{tot}}\in\mathcal A^{\mathcal G+1}$ (Lemma 2.2,
III.I$''''$ Lemma 2.2), so the three counts there apply unchanged. *For $S^{(0)}_1$:* the same, with $k_0 :=
\partial_{S^{(0)}_1}g_{\vec p}(S'')\in\rho_+^2C^\infty$ near $(\iota^+)^\circ$ and in $\mathcal K$ (Lemma 1.3),
$h^{(0)}_{\mathrm s1}(S'')\in\mathcal A^{\mathcal G+1}\subset\mathcal A^{\mathcal G}$ for $h^{(-1)\prime}$,
$\vartheta^{(0)}_{\mathrm s1,\sharp}(S'')\in\mathcal A^{\mathcal G+2}\subset\mathcal A^{\mathcal G+1}$ for $\vartheta'$,
and in count (3) the definition of $\vartheta^{(0)}_{\mathrm s1,\sharp}$ for that of $\vartheta_\sharp$:
$D_1\Upsilon(g',g_0)h^{(0)}_{\mathrm s1}(S'')-\vartheta^{(0)}_{\mathrm s1,\sharp}(S'') =
[D_1\Upsilon(g',g_0)-D_1\Upsilon(g_{b_0},g_{b_0})]h^{(0)}_{\mathrm s1}(S'')-\vartheta^{(0)}_{\mathrm s1}(S'')$. On
$U_K$, $P_2$ does not depend on $S^{(0)}_1$, and on $U_I$, $\dot L_s := \partial_{S^{(0)}_1}[L^{g_{\vec p}+sh,g_{\vec
p}}](S'')$ with III.I$''''$ Lemma 3.1.

(b) Outside $\mathrm{supp}\,\chi_K$, $P_2$ does not depend on $b$ near each point: $g_0$ is the exterior metric there,
and $h^{(0)}$, $\vartheta^{(0)}_\sharp$ are supported in $\mathcal C\subset\mathrm{supp}\,\chi_K$. *On $U_K$:* near each
point $g_0 = g_b$ and $h_{\mathrm{tot}} = 0$, $\vartheta_{\mathrm{tot}} = 0$, so $P_2(h,\vec p) = P(g_b+h,g_b)$ and $f^b
= (D_1P+D_2P)(g_{b_0}+h,g_{b_0})\dot g_{b_0}(b')$. At $h = 0$ this is $\frac d{db}\mathrm{Ric}(g_b)(b') = 0$, by (i)
($P(g,g) = \mathrm{Ric}(g)$) and as $g_b$ is Ricci flat; so
$$f^b = \int_0^1\partial_s\big[(D_1P+D_2P)(g_{b_0}+sh,g_{b_0})\big]\dot g_{b_0}(b')\,ds,$$
a sum of terms bilinear in $(h,\partial h,\partial^2h)$ and $(\dot g_{b_0},\partial\dot g_{b_0},\partial^2\dot g_{b_0})$
(Cartesian derivatives), with coefficients smooth in $g_{b_0}+sh$, $g_{b_0}$ and their first two derivatives. $\dot
g_{b_0}(b')$ is stationary and in $|x|^{-2}C^\infty(\bar X)$ near infinity (III.B Proposition 3.6), so of
$\iota^+$-order 2 and smooth and bounded with all b-derivatives at $K^+$, and Cartesian derivatives lie in
$\rho_+\mathcal V_{\mathrm b}$ near $(\iota^+)^\circ$; with $h\in H^{k,(\mathcal E_+,a_+)}_{\mathrm b}$ at $\iota^+$ and
of $K^+$-weight $a_K$ (or $\ell_K$), the terms have $\iota^+$-data $(\mathcal E_++4,a_++4)$, $\mathcal
E_++4\subset\tilde{\mathcal E}_++2$ (as $(2,0)\in\mathcal G$), and $K^+$-weight $a_K$ (or $\ell_K$). *On $U_\iota$:* the
$b$-derivative of (2.2) is III.I$''''$ (3.4) with $k_b := \partial_bg_{\vec p}(b') = \chi_K\dot
g_{b_0}(b')\in\rho_+^2C^\infty$ for $k_0$, $h^{(0)}(b')\in\mathcal A^{\mathcal G}$ for $h^{(-1)\prime}$ and
$\vartheta^{(0)}_\sharp(b')\in\mathcal A^{\mathcal G+1}$ for $\vartheta'$ (Lemma 2.2), and III.I$''''$ Lemma 3.2's three
counts give $\iota^+$-index set $\tilde{\mathcal E}_++2$ at weight $a_++4$. On the compact part it is in $H^{k-2}$.
Together, (3.1).

(c) Linearity and the bounds are clear from (a)-(b); continuity in $(h,\vec p)$ as in III.I$''''$ Lemma 3.2 (each term
is linear in the direction and a product of factors continuous in $(h,\vec p)$, with the bounds of III.C Lemma 2.1;
$g_{\vec p}$ is smooth in $\vec p$ by Lemma 1.3 (a)); at $(0,0)$, (2.3). $\square$

The source's (11.144) splits $f^S$ as in its (11.86), and its (11.145)-(11.146) have $\iota^+$-index set
$\tilde{\mathcal E}_++2\ni(3,0)$ and the $K^+$-order 5 of $\vartheta^{(0,1)}_{\mathrm s1}$; at $n = 4$ no splitting is
made (III.I$''''$ (I$''''$3)), the least $\iota^+$-order is 4 (Lemma 2.2), and $f^{\mathrm s1}$ vanishes near $K^+$.

## 4. Elimination of the parameters ([Hin26] Definitions 11.42, 11.44, Lemmas 11.43, 11.45, Corollary 11.46 at n = 4)

For $(h,\vec p)$ as in Lemma 2.5 and $f\in\mathcal Y$, write $\dot S_{h,\vec p}(f)$ for the boost parameter of
III.I$''''$ Proposition 4.1 (1) for $L_{h,\vec p}$ ($\mathcal Y$ lies in its source space for every
$\alpha\in(1,\min(a_K-1,\frac32))$ and $\alpha_+\in(\alpha,2)$, and $\dot S$ is determined by the forward solution, as
the coefficient of $t_*$ at $K^+$), and, if $\dot S_{h,\vec p}(f) = 0$, $Q_{h,\vec p}(f) := (\dot b,\dot
S^{(0)}_1)\in\mathfrak b\oplus\mathcal S_1$ for its parameters in III.I$''''''$ (2.1), which are determined by the
forward solution (a stationary tensor of positive $K^+$-weight vanishes, and $(\dot b,S)\mapsto\dot g(\dot b)+h(S)$ is
injective). Sources converge in the finite-regularity spaces on which Lemma 2.5 (c)'s bounds hold, which, $d$ being
large, is what Lemma 3.1 (c) gives for $h\to0$ in $\mathcal X^d$.

**Lemma 4.1 (the parameters near the base point).** Let $(h_j,\vec p_j)\to(0,0)$, with $(h_j,\vec p_j)$ as in Lemma 2.5,
and $F_j\to F$ in $\mathcal Y$.

(a) $\dot S_{h_j,\vec p_j}(F_j)\to\dot S_{0,0}(F)$.

(b) If $\dot S_{h_j,\vec p_j}(F_j) = 0$ for every $j$ (so $\dot S_{0,0}(F) = 0$ by (a)), then $Q_{h_j,\vec p_j}(F_j)\to
Q_{0,0}(F)$.

*Proof.* Let $L_j := L_{h_j,\vec p_j}$, $u_j$ the forward solution of $L_ju_j = F_j$ and $u$ that of $L_{b_0}u = F$.
Then $u_j-u$ is the forward solution of
$$L_{b_0}(u_j-u) = R_j := F_j-F-(L_j-L_{b_0})u_j.\tag{4.1}$$
(a) Fix $\alpha\in(1,\min(a_K-1,\frac32))$, $\alpha_+\in(\alpha,2)$ and
$\beta_+\in(1,\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+))$. By III.I$''''$ Proposition 4.1 (1) for $L_j$
(Lemma 2.5 (b)), $u_j = \chi_Kh^{\le1}_\natural(\dot S_j)+\tilde u_j$, bounded uniformly in $j$ (Lemma 2.5 (c));
$\chi_Kh^{\le1}_\natural(\dot S_j)$ vanishes near $\mathscr I^+$, has $K^+$-weight $-1-\epsilon$ and is of
$\iota^+$-order 2 ($h^{\le1}_\natural\in\mathcal A^{\mathcal G}$ near $(\iota^+)^\circ$, III.I$''''$ Lemma 1.2's proof),
and $\tilde u_j\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta_+,\alpha-2}_{\mathrm b}$. $L_j-L_{b_0}$ has
coefficients of class III.I (3.6) with norms $O(\|h_j\|_{\mathcal X^d}+|\vec p_j|)$ (Lemma 2.5 (a), Lemma 1.3 (b)), so
by III.I Proposition 4.1 (4.2) ($\frac32<\ell_I<a_I+\frac12$) $(L_j-L_{b_0})u_j\to0$ in III.I$''''$ Proposition 4.1
(1)'s source space for $(\alpha,\alpha_+)$: the $K^+$-weights $-1-\epsilon+a_K$ and $\alpha-2+a_K$ exceed $\alpha$
($\alpha<a_K-1$), the $\iota^+$-weights $\ell_++2+m_+-\epsilon$ and $\beta_++2+m_+-\epsilon$ exceed $\alpha_++2$, the
order-2 term being counted at $\ell_+ := \min(2-\epsilon,\max(a_+,\min\mathrm{Re}\,\mathcal E_+))>1$ to meet (4.2)'s
hypothesis $\ell_+\le\max(a_+,\min\mathrm{Re}\,\mathcal E_+)$ ($m_+>1$, $\beta_+>1$, $\alpha_+<2$), and the $\mathscr
I^+$-data are $(\langle\mathcal E^C_I+1\rangle',\ell_I+1)$. So $R_j\to0$ there. By III.I$''''$ Proposition 4.1 (1) for
$L_{b_0}$, $u_j-u = \chi_Kh^{\le1}_\natural(\dot S_{0,0}(R_j))+\tilde u_{R_j}$ with $\tilde u_{R_j}$ of $K^+$-weight
$\alpha-2>-1$; also $u_j-u =
\chi_Kh^{\le1}_\natural(\dot S_j-\dot S_{0,0}(F))+(\tilde u_j-\tilde u)$. A $K^+$-weight above $-1$ forces the
coefficient of $t_*$ to vanish, and $S\mapsto h(S)$ is injective (III.F$'''$ Proposition 4.1 (1)), so $\dot S_j-\dot
S_{0,0}(F) = \dot S_{0,0}(R_j)\to0$.

(b) Now III.I$''''''$ Proposition 2.1 for $L_j$ gives $u_j = \chi_K\dot g(\dot b_j)+\chi_Kh(\dot S^{(0)}_j)+\tilde u_j$,
bounded uniformly (Lemma 2.5 (c)), with $K^+$-weight $-\epsilon$, $\iota^+$-order 2 for the first two terms ((1.1)) and
$\tilde u_j\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta_+,\alpha_K-2}_{\mathrm b}$,
$\beta_+\in(1,\min(\frac32,\min\mathrm{Re}\,\mathcal E_+))$. As in (a), $(L_j-L_{b_0})u_j\to0$ in $\mathcal Y$:
$K^+$-weight $a_K-\epsilon\ge\alpha_K$ for $\epsilon\le a_K-\alpha_K$, $\iota^+$-weights $\ell_++2+m_+-\epsilon$
($\ell_+$ as in (a)) and $\beta_++2+m_+-\epsilon$, both above $4-\epsilon$ as $\ell_++m_+>2$. So $R_j\to0$ in $\mathcal
Y$, and $R_j$ is real. $u_j-u$ has $K^+$-weight $-\epsilon>-1$, so $\dot S_{0,0}(R_j) = 0$ (by the uniqueness used in
(a)), and III.I$''''''$ Proposition 2.1 for $L_{b_0}$ gives $u_j-u = \chi_K\dot g(\dot b_{R_j})+\chi_Kh(\dot
S_{R_j})+\tilde u_{R_j}$ with $(\dot b_{R_j},\dot S_{R_j}) = Q_{0,0}(R_j)\to0$. Comparing with $u_j-u = \chi_K\dot
g(\dot b_j-\dot b)+\chi_Kh(\dot S^{(0)}_j-\dot S^{(0)})+(\tilde u_j-\tilde u)$: the stationary tensor $\dot g(\dot
b_j-\dot b-\dot b_{R_j})+h(\dot S^{(0)}_j-\dot S^{(0)}-\dot S_{R_j})$ times $\chi_K$ has $K^+$-weight $\alpha_K-2>0$, so
it vanishes on $X^\circ$, and by injectivity $Q_{h_j,\vec p_j}(F_j)-Q_{0,0}(F) = Q_{0,0}(R_j)\to0$. $\square$

**Definition 4.2 ([Hin26] Definition 11.42 at n = 4).** For $\vec p\,' = (S',b',S'')$ write $\vec p\,'^{,<0} := S'$ and
$\vec p\,'^{,=0} := (b',S'')\in\mathfrak b\oplus\mathcal S_1$. The first eliminates the asymptotic term of $K^+$-order
$(-1,0)$ (the boost), the second the two of order $(0,0)$ ($\dot b$ and $\dot S^{(0)}_1$); the source's third, of order
$(0,1)$, is absent.

**Lemma 4.3 ([Hin26] Lemma 11.43 at n = 4).** For $(h,\vec p)$ small as in Lemma 2.5, $f\in\mathcal Y$ and $\vec
p\,'^{,=0}\in\mathfrak b\oplus\mathcal S_1$ there is a unique $S' =: \vec p\,'^{,<0}_{h,\vec p}(f,\vec
p\,'^{,=0})\in\mathcal S_1$ such that the forward solution of
$$L_{h,\vec p}u = f-D_{\vec p}P_2(h,\vec p)\big(S',\vec p\,'^{,=0}\big)\tag{4.2}$$
has vanishing boost parameter. It is linear in $(f,\vec p\,'^{,=0})$, the source of (4.2) lies in $\mathcal Y$, and
$\vec p\,'^{,<0}_{h,\vec p}(f,\vec p\,'^{,=0}) = \vec p\,'^{,<0}_{h,\vec p}(f,0)+o(1)\vec p\,'^{,=0}$ with $o(1)\to0$ in
$\mathcal L(\mathfrak b\oplus\mathcal S_1,\mathcal S_1)$ as $(h,\vec p)\to0$.

*Proof.* By Lemma 3.1 and $\ell_I\le a_I$, $f^S_{h,\vec p}(S')$ and $f^{\mathrm s1}_{h,\vec p}(S'')$ lie in $\mathcal Y$
($\mathscr I^+$-data $(\langle\mathcal E^C_I+1\rangle',a_I+1)$, $\iota^+$-weight
$a_++2+\min(2,m_+)-\epsilon>4-\epsilon$, zero near $K^+$), and so does $f^b_{h,\vec p}(b')$ (zero near $\mathscr I^+$,
$\iota^+$-weight $a_++4-\epsilon$, $K^+$-weight $a_K>\alpha_K$); all are real. With $S^{(-1)}_{h,\vec p}(S') := \dot
S_{h,\vec p}(f^S_{h,\vec p}(S'))$ and $f^{=0}_{h,\vec p}(b',S'') := f^b_{h,\vec p}(b')+f^{\mathrm s1}_{h,\vec p}(S'')$,
linearity gives the boost parameter of (4.2) as $\dot S_{h,\vec p}(f)-S^{(-1)}_{h,\vec p}(S')-\dot S_{h,\vec
p}(f^{=0}_{h,\vec p}(\vec p\,'^{,=0}))$. By Lemma 3.1 (c), $f^S_{h,\vec p}(S')\to f^S_{0,0}(S')$ as $(h,\vec p)\to0$, so
Lemma 4.1 (a) gives $S^{(-1)}_{h,\vec p}(S')\to S^{(-1)}_{0,0}(S') = S'$, the last because the forward solution
$\chi_Kh^{\le1}_\natural(S')$ of $L_{b_0}u = f^S_{0,0}(S')$ (Lemma 2.4) has the form of III.I$''''$ (4.1) with $\tilde u
= 0$. On $\mathcal S_1\cong\mathbb R^4$, $S^{(-1)}_{h,\vec p}$ is therefore invertible for small $(h,\vec p)$, and
$$\vec p\,'^{,<0}_{h,\vec p}(f,\vec p\,'^{,=0}) := (S^{(-1)}_{h,\vec p})^{-1}\Big(\dot S_{h,\vec p}(f)-\dot S_{h,\vec
p}\big(f^{=0}_{h,\vec p}(\vec p\,'^{,=0})\big)\Big)$$
is the unique choice. For the last claim, $\dot S_{h,\vec p}(f^{=0}_{h,\vec p}(\vec p\,'^{,=0}))\to\dot
S_{0,0}(f^{=0}_{0,0}(\vec p\,'^{,=0})) = 0$ by Lemma 4.1 (a): the forward solution of $L_{b_0}u = f^{=0}_{0,0}(b',S'')$
is $\chi_K(\dot g(b')+h(S''))$ (Lemma 2.4), of $K^+$-weight $-\epsilon>-1$, so it has no boost term; the map is linear
on the finite-dimensional $\mathfrak b\oplus\mathcal S_1$, so the convergence is uniform on bounded sets. $\square$

**Definition 4.4 ([Hin26] Definition 11.44 at n = 4).** For $f\in\mathcal Y$ and $\vec p\,'^{,=0}$, let $\dot{\vec
p}^{,=0}_{h,\vec p}(f,\vec p\,'^{,=0}) := Q_{h,\vec p}(F)$, $F$ the source of (4.2) with $S' = \vec p\,'^{,<0}_{h,\vec
p}(f,\vec p\,'^{,=0})$: the parameters $(\dot b,\dot S^{(0)}_1)$ of III.I$''''''$ (2.1) for the forward solution of
(4.2). Both $\vec p\,'^{,<0}_{h,\vec p}$ and $\dot{\vec p}^{,=0}_{h,\vec p}$ are linear in $(f,\vec p\,'^{,=0})$.

**Lemma 4.5 ([Hin26] Lemma 11.45 at n = 4).** For $(h,\vec p)$ small, $\vec p\,'^{,=0}\mapsto\dot{\vec p}^{,=0}_{h,\vec
p}(0,\vec p\,'^{,=0})$ is close to $-\mathrm{id}$ on $\mathfrak b\oplus\mathcal S_1$, hence invertible.

*Proof.* At $(h,\vec p) = (0,0)$, Lemma 4.3's proof gives $\vec p\,'^{,<0}_{0,0}(0,\vec p\,'^{,=0}) = 0$, and the
forward solution of $L_{b_0}u = -f^{=0}_{0,0}(b',S'')$ is $-\chi_K(\dot g(b')+h(S''))$ (Lemma 2.4), which has the form
of III.I$''''''$ (2.1) with $\tilde u = 0$; so $\dot{\vec p}^{,=0}_{0,0}(0,\vec p\,'^{,=0}) = -\vec p\,'^{,=0}$. For
$(h,\vec p)\to0$, the source $F_{h,\vec p} := -D_{\vec p}P_2(h,\vec p)(\vec p\,'^{,<0}_{h,\vec p}(0,\vec
p\,'^{,=0}),\vec p\,'^{,=0})$ tends to $F_{0,0}$ in $\mathcal Y$ (Lemma 3.1 (c), and $\vec p\,'^{,<0}_{h,\vec p}(0,\vec
p\,'^{,=0}) = o(1)\vec p\,'^{,=0}\to0$ by Lemma 4.3), and $\dot S_{h,\vec p}(F_{h,\vec p}) = 0$ by Lemma 4.3. Lemma 4.1
(b) gives $\dot{\vec p}^{,=0}_{h,\vec p}(0,\vec p\,'^{,=0})\to-\vec p\,'^{,=0}$, uniformly on bounded sets by linearity
on the finite-dimensional space. $\square$

The source's Lemma 11.45 says "close to the identity": its proof solves with $+D_{(h,\vec p)}P(0,0,\vec p\,'^{,=0})$,
while its Definition 11.44 has the source $f-D_{(h,\vec p)}P(0,\vec p\,')$, for which the map is close to
$-\mathrm{id}$, as here; either is invertible.

**Corollary 4.6 ([Hin26] Corollary 11.46 at n = 4).** For $(h,\vec p)$ small (as in Lemma 2.5, $b = b_0$) and
$f\in\mathcal Y$ there is a unique $\vec p\,'_{h,\vec p}(f)\in\mathcal S_1\oplus\mathfrak b\oplus\mathcal S_1$ such that
the forward solution of
$$L_{h,\vec p}u = f-D_{\vec p}P_2(h,\vec p)\big(\vec p\,'_{h,\vec p}(f)\big)\tag{4.3}$$
has neither a boost term nor the parameters of III.I$''''''$ (2.1); therefore
$$u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta_+,\alpha_K-2}_{\mathrm
b}(\Omega_*;S^2T^*)^{\bullet,-}\quad\text{for every }\beta_+<\min(\tfrac32,\min\mathrm{Re}\,\mathcal E_+),\tag{4.4}$$
and $u$ decays at $K^+$ ($\alpha_K>2$). $\vec p\,'_{h,\vec p}(f)$ and $u$ are linear and continuous in $f$.

*Proof.* By linearity, $\dot{\vec p}^{,=0}_{h,\vec p}(f,\vec p\,'^{,=0}) = \dot{\vec p}^{,=0}_{h,\vec p}(f,0)+\dot{\vec
p}^{,=0}_{h,\vec p}(0,\vec p\,'^{,=0})$, and by Lemma 4.5 there is a unique $\vec p\,'^{,=0} =: \vec p\,'^{,=0}_{h,\vec
p}(f)$ for which it vanishes; put $\vec p\,'_{h,\vec p}(f) := (\vec p\,'^{,<0}_{h,\vec p}(f,\vec p\,'^{,=0}_{h,\vec
p}(f)),\vec p\,'^{,=0}_{h,\vec p}(f))$. The forward solution of (4.3) has no boost term (Lemma 4.3) and $(\dot b,\dot
S^{(0)}_1) = 0$, so III.I$''''''$ (2.1) gives $u = \tilde u$, which is (4.4). Uniqueness: a $\vec p\,'$ with these
properties has vanishing boost parameter, which fixes $\vec p\,'^{,<0}$ given $\vec p\,'^{,=0}$ (Lemma 4.3), and then
$\dot{\vec p}^{,=0}_{h,\vec p}(f,\vec p\,'^{,=0}) = 0$ fixes $\vec p\,'^{,=0}$ (Lemma 4.5). Continuity: every map
involved is linear and continuous (III.I$''''$ Proposition 4.1 (1), III.I$''''''$ Proposition 2.1, Lemma 3.1,
finite-dimensional inverses). $\square$

The source's conclusion is $u\in H^{\infty,(\langle\mathcal E^C_I\rangle,3+\epsilon_I),1-\epsilon,\alpha_K-2}_{\mathrm
b}$ with $\alpha_K\in(2,2+\epsilon_K)$; at $n = 4$ the $\iota^+$-weight is $\min(\frac32,\min\mathrm{Re}\,\mathcal
E_+)-\epsilon$ (III.I$''''''$ (I$''''''$1)), and the base points have $b = b_0$ ((I$'''''''$4)).

## 5. Findings, labels and sources

### 5.1 Findings

(I$'''''''$1) *The centre of mass needs a translated exterior.* The source undoes the centre-of-mass shift by the metric
term $-d\chi_K\otimes_s\omega^{(0)}_{b_0,\mathrm s1}$ in the transition region, of size $O(\rho_+)$, acceptable at $n =
3$ (its Remark 11.36). At $n = 4$ that term has $\iota^+$-order 1 and lies outside $\mathcal X$
($\min\mathrm{Re}\,\mathcal E_+>1$, III.I (1.3)), and with it the analysis of Parts III.I-III.I$''''''$ would not apply
as stated (it needs $m_+>1$); it cannot be moved into the solution either, which must vanish at early times. The
exterior background is translated instead ((1.3), Lemmas 1.1-1.3), as the source already boosts it: the correction
becomes $-d\chi_K\otimes_s(\omega_{\mathrm s1}-\Theta w^0)$, of order 3 (Lemma 2.2), the identity (2.3) stays exact, and
the translated background satisfies everything Parts III.I-III.I$''''''$ use (Lemma 1.3, Lemma 2.5). The parts that
write the source's (11.90), Definition 11.63 and Corollary 11.66 must carry the translation in the initial data as they
carry the boost.

(I$'''''''$2) *Three parameters, no logarithm.* As there is no logarithmic centre-of-mass term (III.I$''''''$
(I$''''''$1)), the parameters are $(S,b-b_0,S^{(0)}_1)$; the source's $h^{(0,1)}_{\mathrm s1}$,
$\vartheta^{(0,1)}_{\mathrm s1}$ (with their $K^+$-order 5), (11.136)-(11.138b) and Remark 11.39 are not needed, and the
corrections have no logarithm, so (11.140)'s $(3,1)$-cancellation is not needed.

(I$'''''''$3) *Continuity at the base point.* Where the source cites "the continuous dependence of forward solutions on
$(h,\vec p)$" (Lemma 11.45's proof), Lemma 4.1 compares the forward solutions through $L_{b_0}(u_j-u) =
F_j-F-(L_j-L_{b_0})u_j$ and the uniqueness of the asymptotic parameters; this needs only uniform bounds (Lemma 2.5 (c))
and gives the invertibility of $S^{(-1)}_{h,\vec p}$ and of Lemma 4.5's map at once.

(I$'''''''$4) *Base points at $b_0$.* The linearisation is taken at base points with $b = b_0$, as in all of Part III
(III.I Remark 5.4: the admissibility of $2L_b$ for all $k$ and the uniform version of II.F$'$ Theorem 1.1 are open for
$b\ne b_0$); the derivative in $b$ at $b_0$ is used. The source's Corollary 11.46 at base points with $b\ne b_0$ waits
on those inputs.

### 5.2 Labels

Proved: Lemmas 1.1, 1.3, 2.2, 2.4, 2.5, 3.1, 4.1, 4.3, 4.5 and Corollary 4.6, given the parts cited. Comparisons with
the source are commentary. READ: the source's statements quoted from pp. 256-262. Inputs: II.E Proposition 3.4; III.B
section 2, (3.5), Proposition 3.6, Lemmas 5.1-5.2, (5.3); III.C Lemma 2.1; III.D$''$ Proposition 3.1; III.F$'''$
Propositions 2.2, 4.1 (1); III.G$''''$ Proposition 5.1 (through III.I$''''''$); III.H section 1, (3.1); III.I (1.1),
(1.3), (3.5)-(3.7), Lemmas 3.6, 4.3, Propositions 3.3, 3.4, 4.1, Corollaries 4.2, 5.2, Theorem 5.3, Remark 5.4;
III.I$''$ Proposition 5.1; III.I$''''$ sections 1-3 ((1.2), (i)-(iii), Definition 2.1, Lemmas 1.2, 2.2, 2.4, 2.5, 3.1,
3.2, (2.4), (3.2)-(3.4)), section 4 (Proposition 4.1, Lemma 4.2 (a)); III.I$'''''$ (1.2); III.I$''''''$ Proposition 2.1.

### 5.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 11.6.2 (pp. 256-262:
(11.134a)-(11.147), Remarks 11.36, 11.39, Definitions 11.37, 11.40, 11.42, 11.44, Lemmas 11.38, 11.41, 11.43, 11.45,
Corollary 11.46). N1STAR-PROOF.md 10.45 (b) and 10.61 (b) (the deductions this part replaces).
