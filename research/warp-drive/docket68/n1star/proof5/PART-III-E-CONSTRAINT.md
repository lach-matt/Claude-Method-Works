# Part III.E. The constraint propagation operator and its dual states, at n = 4 ([Hin26] section 7 to Proposition 7.3)

*Status.* Written (D225). This part proves, at spatial dimension $n = 4$ and for the Myers-Perry metrics $g_b$, $b$ near
$b_0 = (\mu_0,0)$, what [Hin26] section 7 establishes up to and including Proposition 7.3 (pp. 134-139): the
invertibility of the adjoint of the constraint propagation operator at zero energy and its indicial roots (his Lemma
7.2), and the large zero energy states of the adjoint built from the time translation, the translations and the
rotations, whose trace-reversed symmetric gradients decay (Proposition 7.3). Its input is [Hin26] Theorem 7.1 at $n =
4$, the summary of [Hin26a]; it is stated in section 1 and is proved in Part IV, which writes out [Hin26a] at $n = 4$.
Section 7.2.1 (Proposition 7.4, Lemma 7.5) is Part III.E$'$. Parts are cited as in III.D$'$.

*What n = 4 changes.* The weights: the zero energy invertibility of the constraint propagation operator holds for
weights $\alpha+2\in[-C_0,2)$ (Euclidean density), its top the Coulomb root 2 where the source's is 1, so the adjoint is
invertible for b-weights in $(0,C_0+2]$, and its indicial roots are $2-\bar\lambda$. The dual states then carry one more
order of decay: the translations' and rotations' corrections begin at $\rho^2$ and their trace-reversed symmetric
gradients at $\rho^3$, and the remainders lie at the weight $C_0+2$. Findings are in section 4.

## 1. Setting and the input

$\mathcal B$, $g_b$, $t_*$, $\rho$, $E$ (the trivialisation by $dt_*,dx^i$) and $\bar g$ are as in III.D$''$. With III.B
Definition 6.1 (6.2), for $v_C\in(0,1)$, $e_C$, $\gamma_C$ and a stationary $c_C\in|x|^{-1}C^\infty$ equal to
$|x|^{-1}(dt-v_C\,d|x|)$ for large $|x|$,

$$\delta^*_{g,E_C} := \delta^*_g+E^C_g,\quad E^C_g\omega = \gamma_C\big(2c_C\otimes_s\omega-\tfrac23(1-e_C)\,
g\,\iota_{g^{-1}c_C}\omega\big),\qquad\Box^C_b := 2\delta_{g_b}G_{g_b}\delta^*_{g_b,E_C},\tag{1.1}$$

the constraint propagation operator; $P^C_b := \widehat{\Box^C_b}(0)$ is its zero energy operator. The formal adjoint of
$\Box^C_b$ for the fibre pairing $g_b^{-1}$ and the volume density $|dg_b|$ is

$$(\Box^C_b)^* = 2(\delta^*_{g_b,E_C})^*G_{g_b}\delta^*_{g_b}\tag{1.2}$$

([Hin26] (7.11)), as $\delta_g = (\delta^*_g)^*$ and $G_g$ is symmetric. On stationary sections the spectral family of
$(\Box^C_b)^*$ at zero energy is the formal adjoint of $P^C_b$ for the pairing $B(u,w) := \int_Xg_b^{-1}(u,\bar
w)\,|dg_b|_X|$, $|dg_b| = |dt_*|\otimes|dg_b|_X|$, by the argument of III.D$'$ Lemma 2.1 (1) (a cut-off $\theta(t_*)$
with $\int\theta = 1$; the terms with $\theta'$, $\theta''$ integrate to zero); we write $(P^C_b)^*$ for it.

**Theorem 1.1 ([Hin26] Theorem 7.1 at n = 4; proved in Part IV).** Fix $v_C\in(0,1)$ and $C_0>0$. There are
$e_C\in(0,1)$ and a stationary past timelike $c_C\in\rho C^\infty(\bar X;T^*X)$ with $c_C = |x|^{-1}(dt-v_C\,d|x|)$ for
large $|x|$ such that for all sufficiently large $\gamma_C$ and all $b$ near $b_0$:

(1) (*Mode stability, $\sigma\ne0$.*) For $\sigma\ne0$, $\mathrm{Im}\,\sigma\ge0$, $\widehat{\Box^C_b}(\sigma)$ has
trivial nullspace on $\mathcal A^\gamma(\bar X;E)$ for every $\gamma\in\mathbb R$.

(2) (*Enhanced mode stability, $\sigma = 0$.*) $\Box^C_b$ satisfies the hypotheses (H1)-(H4) of I.A with a horizon
threshold $\frac12+\vartheta_{\mathcal H}<-C_0$, and for every $\alpha$ with $\alpha+2\in[-C_0,2)$ and every $s\ge-C_0$,
$P^C_b:\{\omega\in\bar H^{s,\alpha}_{\mathrm b}:P^C_b\omega\in\bar H^{s-1,\alpha+2}_{\mathrm b}\}\to\bar
H^{s-1,\alpha+2}_{\mathrm b}$ is invertible, with the Euclidean density (I.C (3.1)).

(3) (*Indicial roots.*) The indicial roots of $P^C_b$ satisfy $\mathrm{Re}\,\lambda\ge2$ or $\mathrm{Re}\,\lambda<-C_0$;
the only root with real part 2 is $\lambda = 2$, a simple root of scalar type 0 and of scalar type 1.

(4) (*tf-admissibility.*) $\Box^C_b$ is tf-admissible (I.C Definition 5.1) with every weight in $[-C_0,2)$.

The structure near infinity is that of the source's (7.3)-(7.6) with the shift $\frac32$: $\Box^C_b =
-2\partial_{t_*}\rho(\rho\partial_\rho-\frac32-\bar S^C)+P^C_b+Q\partial_{t_*}+R\partial_{t_*}^2$, with $\bar S^C$ of
spectrum $\gamma_C\{2(1-v_C),(1-e_C)(1-v_C),1-v_C\ (\text{three times})\}$ (computed: `cpmodes5.py` K1; supplement 10.21
(i)), and $P^C_b-\bar P^C\in\rho^4\mathrm{Diff}^2_{\mathrm b}$ against the Minkowski model $\bar\Box^C :=
2\bar\delta\bar G\bar\delta^*_{\bar E_C}$, as in III.D$''$ Lemma 2.1 (the modification $E^C$ has coefficients in $\rho
C^\infty$, and $c_C$ differs from the model's $|x|^{-1}(d\bar t-v_C\,d|x|)$ by $\rho^3C^\infty$). The record's computed
inputs for Part IV are its supplement 10.12-10.14, 10.21-10.23, 10.54 and 10.79.

Below, $C_0$, $v_C$, $e_C$, $c_C$ and $\gamma_C$ are fixed as in Theorem 1.1, and $b$ is near $b_0$. *An unweighted
b-density is used near $\partial X$*, as in the source's section 7.2, unless the Euclidean density is named; for it,
$\bar H^{k,\beta}_{\mathrm b}(|dx|) = \bar H^{k,\beta+2}_{\mathrm b}(\mu_{\mathrm b})$ (I.C Remark (a) after section
1.2). $\chi\in C^\infty(\bar X)$ equals 1 near $\partial X$ and 0 near $\{|x|\le r_h\}$.

## 2. The adjoint at zero energy ([Hin26] Lemma 7.2 at n = 4)

**Lemma 2.1.** (1) (*Invertibility.*) For $\alpha\in(0,C_0+2]$ and $s\le C_0+1$, $(P^C_b)^*:\{\omega\in\dot
H^{s,\alpha}_{\mathrm b}:(P^C_b)^*\omega\in\dot H^{s-1,\alpha+2}_{\mathrm b}\}\to\dot H^{s-1,\alpha+2}_{\mathrm b}$ is
invertible. (2) (*Indicial roots.*) The indicial roots of $(P^C_b)^*$ are $2-\bar\lambda$, $\lambda$ running over those
of $P^C_b$. So they are $0$ (scalar type 0 or 1), have negative real part, or have real part $>C_0+2$.

*Proof.* (1) First for the adjoint $(P^C_b)^{*h}$ of I.C, taken for the fibre inner products $h$ and the Euclidean
density. By Theorem 1.1 (2) and I.C Theorem 3.1 (1) and (4), for $\alpha'$ with $\alpha'+2\in[-C_0,2)$ and $s'\ge-C_0$,
(3.3) of I.C holds without its last term: $(P^C_b)^{*h}$ is injective with closed range on $\mathcal X^*_0 = \{v\in\dot
H^{1-s',-\alpha'-2}_{\mathrm b}(|dx|):(P^C_b)^{*h}v\in\dot H^{-s',-\alpha'}_{\mathrm b}(|dx|)\}$, and the annihilator of
its range is the kernel of $P^C_b$ on $\mathcal X_0$, which is trivial; so it is onto $\dot H^{-s',-\alpha'}_{\mathrm
b}(|dx|)$, and invertible. In b-densities these spaces are $\dot H^{1-s',-\alpha'}_{\mathrm b}$ and $\dot
H^{-s',-\alpha'+2}_{\mathrm b}$; with $s := 1-s'\le C_0+1$ and $\alpha := -\alpha'\in(0,C_0+2]$ this is the claim for
$(P^C_b)^{*h}$. The pairing $B$ differs from the $h$-weighted $L^2(|dx|)$ pairing by a bundle map $M$, smooth and
invertible on $\bar X$ ($g_b^{-1}$ and $h$ are nondegenerate, smooth up to $\partial X$, and $|dg_b|_X|/|dx|$ is smooth
and positive there), so $(P^C_b)^* = M^{-1}(P^C_b)^{*h}M$ with $M$ preserving every $\dot H^{s,\alpha}_{\mathrm b}$; the
claim follows.

(2) Let $N := N(\rho^{-2}P^C_b)$ and write $*$ for adjoints for the Euclidean density near $\partial X$,
$\rho^{-4}|\frac{d\rho}\rho d\slashed g|$, and $*_{\mathrm b}$ for the unweighted b-density, so $A^{*_{\mathrm b}} =
\rho^{-4}A^*\rho^4$. As $(\rho^{-2}P)^* = \rho^{-2}(\rho^2P^*\rho^{-2})$ and $N(\rho^2P^*\rho^{-2}) = N(P^*)$ up to the
conjugation, the source's computation (7.10) reads at $n = 4$

$$N(\rho^{-2}P,\lambda)^* = \rho^{\bar\lambda}N^{*_{\mathrm b}}\rho^{-\bar\lambda}
= \rho^{\bar\lambda}\rho^{-4}N^*\rho^4\rho^{-\bar\lambda} = \rho^{\bar\lambda-2}N(\rho^{-2}P^*)\rho^{2-\bar\lambda}
= N(\rho^{-2}P^*,2-\bar\lambda),$$

the adjoint on the left being on $\mathbb S^3$ for $d\slashed g$; so $\lambda$ is a root of $P^C_b$ iff $2-\bar\lambda$
is one of the adjoint. The rest is Theorem 1.1 (3). (*Computed:* `dual5.py` A1 checks $\det N^*(\lambda) = \det
N(2-\lambda)$ type by type for s0, sl ($l\le3$), vl ($l\le3$), and the four-dimensional $1-\bar\lambda$ as a control.)
$\square$

Two consequences used below. (a) For $f\in\dot H^{s-1,\alpha+2}_{\mathrm b}$ with $f$ polyhomogeneous near $\partial X$
with index set $\mathcal F$, $\min\mathrm{Re}\,\mathcal F>2$, the solution $u = ((P^C_b)^*)^{-1}f$ with $\alpha = C_0+2$
lies in $\dot H^{s,(\mathcal E,C_0+2)}_{\mathrm b}$ (partial polyhomogeneity, III.A Definition 2.8), where $\mathcal E$
is the index set of III.A Lemma 1.5 for $\rho^{-2}f$: solve $\rho^{-2}f$ away near $\partial X$ to order
$\rho^{C_0+4+\epsilon}$ by Lemma 1.5 for the elliptic b-operator $\rho^{-2}(P^C_b)^*$ (on the bundle), and the
remainder, compactly supported away from $\partial X$ modulo $\dot H^{s-1,C_0+4}_{\mathrm b}$, by (1). Since the adjoint
has no root with real part in $(0,C_0+2]$, the exponents of $\mathcal E$ below $C_0+2$ are those of $\mathcal F$ less 2
plus $\mathbb N_0$, without logarithms. (b) *Vanishing inside the horizon.* On $\{r_0<|x|<r_h\}$ the Killing field
$\partial_{t_*}$ is spacelike, so the quotient metric is Lorentzian with $|x|$ timelike, and on stationary sections
$(P^C_b)^*$ is a wave operator in the time $-|x|$ there; an element of its kernel, or a solution with a source supported
in $\{|x|>r_h\}$, that lies in a $\dot H$ space vanishes near $\{|x| = r_0\}$, and so on $\{r_0<|x|<r_h\}$ by uniqueness
for the Cauchy problem on the spacelike hypersurfaces $\{|x| = c\}$, $c<r_h$.

## 3. The dual states ([Hin26] Proposition 7.3 at n = 4)

With $\bar\omega_{\mathrm s0}$, $\bar\omega_{\mathrm s1}(S)$, $V$ as in III.D$''$ (1.2):

**Proposition 3.1.** Assume (Dyn). (1) (*States.*) There are stationary 1-forms

$$\omega^{*(0)}_{b,\mathrm s0},\ \omega^{*(0)}_{b,\mathrm s1}(S)\in\dot H^{1,((0,0),C_0+2)}_{\mathrm b},
\qquad\omega^{*(-1)}_{b,\mathrm v1}(V)\in\dot H^{1,((-1,0),C_0+2)}_{\mathrm b},\tag{3.1}$$

linear in $S\in\mathcal S_1$ and $V\in\mathcal V_1$, of class $C^k$ in $b$ with values in $\dot
H^{1-k,((0,0),C_0+2)}_{\mathrm b}$, resp. $\dot H^{1-k,((-1,0),C_0+2)}_{\mathrm b}$, with leading terms
$\bar\omega_{\mathrm s0}$, $\bar\omega_{\mathrm s1}(S)$, $V$, and $\omega^{*(0)}_{b,\mathrm s0}-\chi
g_b(\partial_{t_*},\cdot)\in\dot H^{1,C_0+2}_{\mathrm b}$, which lie in $\ker(\Box^C_b)^*$. The corrections to the
translations and rotations, $\omega^{*(0)}_{b,\mathrm s1}(S)-\chi\bar\omega_{\mathrm s1}(S)$ and
$\omega^{*(-1)}_{b,\mathrm v1}(V)-\chi V$, lie in $\dot H^{1,((2,0),C_0+2)}_{\mathrm b}$. If $R_V$ is a Killing field of
$g_b$ (at $A = 0$, every $V$), then $\omega^{*(-1)}_{b,\mathrm v1}(V)-\chi g_b(R_V,\cdot)\in\dot H^{1,C_0+2}_{\mathrm
b}$.

(2) (*Dual pure gauge states.*)

$$h^*_{b,\mathrm s0} := G_{g_b}\delta^*_{g_b}\omega^{*(0)}_{b,\mathrm s0}\in\dot H^{0,C_0+3}_{\mathrm b},
\qquad h^*_{b,\mathrm s1}(S),\ h^*_{b,\mathrm v1}(V)\in\dot H^{0,((3,0),C_0+3)}_{\mathrm b},\tag{3.2}$$

with $h^*_{b,\mathrm s1}(S) := G_{g_b}\delta^*_{g_b}\omega^{*(0)}_{b,\mathrm s1}(S)$ and likewise for $V$, of class
$C^k$ in $b$ in $\dot H^{-k,C_0+3}_{\mathrm b}$, resp. $\dot H^{-k,((3,0),C_0+3)}_{\mathrm b}$; and $h^*_{b,\mathrm
v1}(V)\in\dot H^{0,C_0+3}_{\mathrm b}$ when $R_V$ is Killing for $g_b$. All these 1-forms and tensors vanish on
$\{r_0<|x|<r_h\}$ (section 2, (b)).

*Proof. Time translation.* $\partial_{t_*}$ is Killing, so $\delta^*_{g_b}(\chi g_b(\partial_{t_*},\cdot)) =
d\chi\otimes_sg_b(\partial_{t_*},\cdot)\in C_c^\infty(X^\circ)$, and by (1.2) $f_b := (\Box^C_b)^*(\chi
g_b(\partial_{t_*},\cdot)) = 2(\delta^*_{g_b,E_C})^*G_{g_b}(d\chi\otimes_sg_b(\partial_{t_*},\cdot))\in
C_c^\infty(X^\circ)$, stationary. Lemma 2.1 (1) with $\alpha = C_0+2$, $s = 1$, gives a unique $\omega'_b\in\dot
H^{1,C_0+2}_{\mathrm b}$ with $(P^C_b)^*\omega'_b = -f_b$; put $\omega^{*(0)}_{b,\mathrm s0} := \chi
g_b(\partial_{t_*},\cdot)+\omega'_b$. Its expansion is that of $g_b(\partial_{t_*},\cdot)$, smooth on $\bar X$ with
leading term $\bar\omega_{\mathrm s0}$ (III.D$''$ Proposition 3.1). $h^*_{b,\mathrm s0} =
G_{g_b}(d\chi\otimes_sg_b(\partial_{t_*},\cdot)+\widehat{\delta^*_{g_b}}(0)\omega'_b)\in
C_c^\infty+\rho\,\mathrm{Diff}^1_{\mathrm b}\dot H^{1,C_0+2}_{\mathrm b}\subset\dot H^{0,C_0+3}_{\mathrm b}$.

*Translations.* $\delta^*_{g_b}(\chi\bar\omega_{\mathrm s1}) = d\chi\otimes_s\bar\omega_{\mathrm
s1}+\chi(\widehat{\delta^*_{g_b}}(0)-\widehat{\bar\delta^*}(0))\bar\omega_{\mathrm s1}\in C_c^\infty+\rho^3C^\infty$
(III.D$''$ (2.1); $\bar\delta^*\bar\omega_{\mathrm s1} = 0$), and $(\delta^*_{g_b,E_C})^*G_{g_b}$ lies in
$\rho\,\mathrm{Diff}^1_{\mathrm b}$ near $\partial X$ (the adjoint of $\delta^*_{g_b}$ is $\delta_{g_b}$, and $(E^C)^*$
has coefficients in $\rho C^\infty$), so $f_b := (\Box^C_b)^*(\chi\bar\omega_{\mathrm s1})\in
C_c^\infty+\rho^4C^\infty$. (*Computed:* on Tangherlini $(\Box^C)^*dx$ vanishes to order $\rho^3$ with a nonzero
$\rho^4$ term, `dual5.py` A2.) By consequence (a) of Lemma 2.1, with $\mathcal F = (4,0)$: $\omega'_b :=
-((P^C_b)^*)^{-1}f_b\in\dot H^{1,((2,0),C_0+2)}_{\mathrm b}$, the coefficient of $\rho^2$ being
$N(\rho^{-2}(P^C_b)^*,2)^{-1}$ of that of $\rho^{-2}f_b$ (2 is no root of the adjoint). Put $\omega^{*(0)}_{b,\mathrm
s1}(S) := \chi\bar\omega_{\mathrm s1}(S)+\omega'_b$. Then $h^*_{b,\mathrm s1}(S) =
G_{g_b}(d\chi\otimes_s\bar\omega_{\mathrm
s1}+\chi(\widehat{\delta^*_{g_b}}(0)-\widehat{\bar\delta^*}(0))\bar\omega_{\mathrm
s1}+\widehat{\delta^*_{g_b}}(0)\omega'_b)\in C_c^\infty+\rho^3C^\infty+\dot H^{0,((3,0),C_0+3)}_{\mathrm b}$.
(*Computed:* its $\rho^3$ term is nonzero on Tangherlini, A2.)

*Rotations.* $g_\mu(R_V,\cdot) = V$ and $\delta^*_{g_\mu}V = 0$ (III.D$''$, proof of Proposition 3.1), so
$\delta^*_{g_b}(\chi V) = d\chi\otimes_sV+\chi(\widehat{\delta^*_{g_b}}(0)-\widehat{\delta^*_{g_\mu}}(0))V\in
C_c^\infty+\rho^4\mathrm{Diff}^0_{\mathrm b}(\rho^{-1}C^\infty)\subset C_c^\infty+\rho^3C^\infty$, and $f_b :=
(\Box^C_b)^*(\chi V)\in C_c^\infty+\rho^4C^\infty$. As for the translations, $\omega'_b := -((P^C_b)^*)^{-1}f_b\in\dot
H^{1,((2,0),C_0+2)}_{\mathrm b}$, $\omega^{*(-1)}_{b,\mathrm v1}(V) := \chi V+\omega'_b$, and $h^*_{b,\mathrm v1}(V) =
G_{g_b}(d\chi\otimes_sV+\chi(\widehat{\delta^*_{g_b}}(0)-\widehat{\delta^*_{g_\mu}}(0))V+\widehat{\delta^*_{g_b}}(0)
\omega'_b)\in\dot
H^{0,((3,0),C_0+3)}_{\mathrm b}$. *Killing rotations.* If $R_V$ is Killing for $g_b$, $K := g_b(R_V,\cdot)$ has
$\delta^*_{g_b}(\chi K) = d\chi\otimes_sK$, so $(\Box^C_b)^*(\chi K)\in C_c^\infty$ and $\omega'' :=
-((P^C_b)^*)^{-1}(\Box^C_b)^*(\chi K)\in\dot H^{1,C_0+2}_{\mathrm b}$. The difference $(\chi V+\omega'_b)-(\chi
K+\omega'')$ lies in $\ker(P^C_b)^*$, and in $\dot H^{1,\alpha}_{\mathrm b}$ for $\alpha<1$, as $K-V = (g_b-\bar
g)(R_V,\cdot)\in\rho C^\infty$ (III.D$''$ (2.3)) and $\omega'_b$ begins at $\rho^2$; by Lemma 2.1 (1) with such an
$\alpha\in(0,1)$ it vanishes. So $\omega^{*(-1)}_{b,\mathrm v1}(V)-\chi K = \omega''\in\dot H^{1,C_0+2}_{\mathrm b}$ and
$h^*_{b,\mathrm v1}(V) = G_{g_b}(d\chi\otimes_sK+\widehat{\delta^*_{g_b}}(0)\omega'')\in\dot H^{0,C_0+3}_{\mathrm b}$.

*Regularity in b.* For a smooth curve $b(\tau)$ with $b(0) = b$, the formal derivative $\dot\omega'$ of
$\omega'_{b(\tau)}$ solves $(P^C_b)^*\dot\omega' = -(\partial_\tau(P^C_{b(\tau)})^*)\omega'_b-\partial_\tau
f_{b(\tau)}$. $\partial_\tau(P^C_{b(\tau)})^*$ is a second-order b-operator with coefficients in $\rho^4C^\infty$ near
$\partial X$ (the mass and rotation enter at $\rho^2$ and $\rho^3$, counted as in III.D$''$ Lemma 2.1), so the first
term lies in $\dot H^{-1,C_0+6}_{\mathrm b}$, and $\partial_\tau f$ lies in $C_c^\infty+\rho^4C^\infty$; Lemma 2.1 (1)
with $s = 0$ bounds $\dot\omega'$ in $\dot H^{0,C_0+2}_{\mathrm b}$, with the loss of one derivative, and difference
quotients converge to it as in III.D$''$ Lemma 2.2. Iterating gives $C^k$ into $\dot H^{1-k,C_0+2}_{\mathrm b}$; the
expansion terms, from III.A Lemma 1.5, depend smoothly on $b$. The statements for $h^*$ follow. *Vanishing inside the
horizon* is section 2, (b), as $(P^C_b)^*\omega = 0$ there. $\square$

*Remarks.* (a) *Counting.* At $A = 0$ the dual states are one for the time translation, four for the translations and
six for the rotations: eleven, against the source's seven ($1+3+3$). The time translation's and the six rotations' $h^*$
decay to the weight $C_0+3$, and the four translations' begin at $\rho^3$. (b) The memberships can be improved to full
polyhomogeneity near $\partial X$, as the source remarks; only the remainder weight $C_0+2$, with $C_0$ large, is used
later.

## 4. Findings, labels and sources

### 4.1 Findings

(E1) *The weights at n = 4.* The source's Lemma 7.2 holds for $\alpha\in(0,C_0+1]$; at $n = 4$ the range is $(0,C_0+2]$,
because the enhanced mode stability holds up to the Coulomb root 2 (Theorem 1.1 (2)-(3)), and the passage from the
Euclidean to the b-density shifts by $\frac n2 = 2$. The adjoint's roots are $2-\bar\lambda$ (source: $1-\bar\lambda$).

(E2) *One order faster.* The translations' and rotations' corrections begin at $\rho^2$ and their trace-reversed
symmetric gradients at $\rho^3$ (source: $\rho^1$, $\rho^2$), from III.D$''$ Lemma 2.1; the time translation's and
Killing rotations' gradients decay to $C_0+3$ (source $C_0+2$).

(E3) *Eleven dual states at zero rotation* (Remark (a)), as against seven; the six rotations are Killing on Tangherlini.

(E4) *The input.* Everything here rests on Theorem 1.1, the source's Theorem 7.1, which it states as a summary of
[Hin26a] and proves there, including the hypotheses of the low-energy theory with a horizon threshold below $-C_0$; it
is proved at $n = 4$ in Part IV. The proof of Lemma 2.1 (1) is the source's "dual statement", made precise through I.C
Theorem 3.1 (3.3) and the change of pairing.

### 4.2 Labels

Proved here, assuming (Dyn) (Part VI) and Theorem 1.1 (Part IV): Lemma 2.1 and Proposition 3.1. Computed (exact; rerun
D225): `dual5.py` A1-A2, `cpmodes5.py` K1. Standard facts used: the Banach-space adjoint of an invertible operator, the
formal adjoint identity (1.2), and uniqueness for the Cauchy problem of a linear wave equation on spacelike
hypersurfaces.

### 4.3 Sources

READ: [Hin26] pp. 134-139 (section 7 to the end of the proof of Proposition 7.3: (7.1)-(7.8), Theorem 7.1 and its proof,
Lemma 7.2 with (7.9)-(7.10), (7.11), Proposition 7.3 with (7.12)-(7.15) and its proof), arXiv:2606.28253v2, full text.
The record's supplement 10.21 and 10.31 (N1STAR-PROOF.md) for the computed statements.
