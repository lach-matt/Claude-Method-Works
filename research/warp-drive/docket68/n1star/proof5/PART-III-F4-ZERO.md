# Part III.F$'''$. The zero energy kernel and cokernel of the linearised operator at n = 4 ([Hin26] 8.9-8.13)

*Status.* Written (D233). This part proves, at spatial dimension $n = 4$, [Hin26] section 8.4 from Proposition 8.9 to
Corollary 8.13 (pp. 154-158): the linearised Myers-Perry metrics brought into the gauge (Proposition 2.2, the source's
Proposition 8.9), the spin changes that are pure gauge (Remark 2.3, Remark 8.10), the kernel and cokernel of the zero
energy operator $\widehat{L_b}(0)$, eleven-dimensional against the source's seven (Proposition 4.1, Proposition 8.11),
and the linear right inverse built from them (Corollary 4.2, Corollary 8.13). The source takes the kernel bound from
[AHW24] Theorem 6.1 (2), the classification of the stationary decaying solutions of the linearised Einstein equation on
Kerr, which has no five-dimensional counterpart; at the Tangherlini parameter $b_0$ it is proved here harmonic by
harmonic from the Kodama-Ishibashi decomposition at zero frequency (Theorem 3.1), and near $b_0$ the count follows from
the invertibility at $b_0$ of an augmented operator and Part I.C's perturbation theory, so no rigidity statement for
spinning Myers-Perry metrics is needed. The pairings of the source's Lemma 8.12 are not used here (finding (F$'''$4));
they are part of the next part. Notation is that of Parts III.F, III.F$'$ and III.F$''$. Computations cited as
*computed* are exact (sympy) and rerun by `static5.py` S1-S6, `zstates5.py` Z5-Z6 and `mp5.py` M3.

## 1. Setting

The parameters are those of III.F$'$ section 1 and III.F$''$: (Dyn), $z = 4e_\Upsilon\gamma_\Upsilon^2\in(0,\frac12]$,
(C1), $\gamma_\Upsilon$ as in III.F$'$ Proposition 3.3, the horizon modification and
$b\in\mathcal B(\gamma_{\Upsilon,H})$ as in III.D$'$ Proposition 4.1 and III.D$''$ section 1, and
$s>\frac12+\vartheta_L$ (III.F$''$ Lemma 1.1). *All b-spaces use an unweighted b-density $\mu_{\mathrm b} = |dx|/|x|^4$
near $\partial X$*, so that $\bar H^{s,\alpha}_{\mathrm b}$ here is I.C's $\bar H^{s,\alpha-2}_{\mathrm b}$, and
$H^{\infty,a}_{\mathrm b}\subset\mathcal A^a$ near $\partial X$. $\epsilon_{\mathrm{ind}}$ and
$\mathcal E_{\mathrm{ind}}$ are as in III.D$''$ section 1: $\epsilon_{\mathrm{ind}}\in(0,\frac12)$ is less than
$d(\mathrm{Re}\,\lambda,\mathbb Z)$ for every indicial root $\lambda$ of $\widehat{\Box^\Upsilon_b}(0)$ with non-integer
real part of modulus at most 10 (the gauge potential operator's number, not that of III.F$'$ (2.2), which concerns the
roots of $\widehat{L_b}(0)$ and is far smaller at the record's point), and $\mathcal E_{\mathrm{ind}}$ denotes an index
set with $\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}\ge\epsilon_{\mathrm{ind}}$, independent of $b$, which may change
from line to line. Write $\beta^L_+ := \min\{\mathrm{Re}\,\lambda:\lambda$ an indicial root of $\widehat{L_b}(0)$,
$\mathrm{Re}\,\lambda>0\}$; by III.F$'$ Proposition 2.3, $\beta^L_+>1$, so every $\alpha\in(0,1]$ lies in the indicial
gap $(0,\beta^L_+)$.

*Densities and adjoints.* In the Kerr-Schild coordinates $(t,x)$ of III.B Definition 3.2, $g_b = \eta+Hk\otimes k$ with
$k$ null for $\eta$ (III.B Lemma 3.3 (a)), so $\det g_b = \det\eta = -1$; and $t_*-t = -\psi(|x|)$ is a function on $X$
(III.B (3.6)), so the change $(t,x)\mapsto(t_*,x)$ has Jacobian 1 and $|dg_b| = |dt_*|\,|dx|$ for every $b$. Adjoints on
$X$ are taken with respect to $|dx|$ and the fibre inner product induced by $g_b$ (indefinite); for a stationary
operator $P$ on $M$ with formal adjoint $P^*$ with respect to $|dg_b|$ and $g_b$, $\widehat P(0)^* = \widehat{P^*}(0)$
(pair $\phi(t_*)u$ with $\phi(t_*)v$, $\phi\in C^\infty_c(\mathbb R)$, $u,v\in C^\infty_c(X^\circ)$ stationary, and
integrate in $t_*$). The source's spatial density $|dg_b|_X|$ is $|dx|$ here.

*The linearised family at $b_0$.* $t$ denotes the Kerr-Schild time, $v := t+|x|$, and on $\{r>r_h\}$ the static chart
$(t_s,r,z)$ of III.F$''$ section 2 has $v = t_s+r_*$, so $dt+d|x| = dt_s+f^{-1}dr$. For $\dot A\in\mathfrak{so}(4)$ put
$V(\dot A) := (\dot Ax)\cdot dx$; it is $r^2$ times a Killing 1-form $V_i\,dz^i$ of the unit $\mathbb S^3$, of vector
type 1, and $\dot A\mapsto V(\dot A)$ is an isomorphism of $\mathfrak{so}(4)$ onto $\mathcal V_1$ (III.D$''$ (1.2)).

**Lemma 1.1.** $\dot g_{b_0}(1,0) = |x|^{-2}(dt+d|x|)^2$ and
$\dot g_{b_0}(0,\dot A) = 2\mu_0|x|^{-4}(dt+d|x|)\otimes_sV(\dot A)$. So $\dot g_{b_0}(1,0)$ is $O(4)$-invariant (scalar
type 0) and equals $r^{-2}(dt_s+f^{-1}dr)^2$; and $\dot g_{b_0}(0,\dot A)$ is of vector type 1, with Kodama-Ishibashi
coefficients ($h = 2rf_aV_i\,dy^adz^i$) $f_t = \mu_0r^{-3}$ and $f_r = \mu_0r^{-3}f^{-1}$ in the static chart, on the
Killing form $r^{-2}V(\dot A)$.

*Proof.* At $A = 0$ the metric is $\eta+\mu|x|^{-2}(dt+d|x|)^2$ (III.B Proposition 3.4), which gives the first formula.
For the second, $s = -\frac12\mathrm{tr}(A^2)$, $p^2$ and $|Ax|^2$ are of order $|A|^2$, so $r_A = |x|+O(|A|^2)$,
$P = r_A^4+O(|A|^2)$, $F_A = 1+O(|A|^2)$ and $H_{\mu,A} = \mu|x|^{-2}+O(|A|^2)$ (III.B (3.1), Lemma 3.1 (b)); and
$\mathsf M/P = (r^2I-A^2)^{-1} = r^{-2}I+O(|A|^2)$ (Lemma 3.1 (a)), so
$\ell_A = |x|^{-1}x\cdot dx+|x|^{-2}(Ax)\cdot dx+O(|A|^2)$. Differentiating $H_{\mu,A}k_A\otimes k_A$ at $A = 0$ in the
direction $\dot A$ gives $2\mu|x|^{-2}(dt+d|x|)\otimes_s|x|^{-2}(\dot Ax)\cdot dx$. (*Computed*, exactly, by `mp5.py`
M3.) With $a\otimes_sb := \frac12(a\otimes b+b\otimes a)$, the component of $\dot g_{b_0}(0,\dot A)$ on
$(\partial_{t_s},\partial_{z^i})$ is $\mu_0r^{-4}\cdot r^2V_i$, so $rf_t = \mu_0r^{-2}$, and the $dr$ part gives
$f_r = \mu_0r^{-3}f^{-1}$. $\square$

## 2. Gauged linearised Myers-Perry metrics ([Hin26] Proposition 8.9 at n = 4)

**Lemma 2.1 (inverse images).** Let $k\in\{1,2\}$ and let $f$ be a stationary section, smooth on $\bar X$, with
$f\in\rho^{2+k}C^\infty$ near $\partial X$. Then $u := \widehat{\Box^\Upsilon_b}(0)^{-1}f\in\mathcal
A^{(k,0)\cup(k+\mathcal E_{\mathrm{ind}})}(\bar X;E)$, with $\mathcal E_{\mathrm{ind}}$ independent of $b$; its $\rho^k$
coefficient $u_k$ solves $I(k)u_k = f_{2+k}$, where $f = \rho^{2+k}f_{2+k}+O(\rho^{3+k})$ and $I$ is the indicial family
of $A := \rho^{-2}\widehat{\Box^\Upsilon_b}(0)$ near $\partial X$ (I.C (1.3)).

*Proof.* $f\in\mathcal A^{2+(k,0)}$, so III.D$'$ Lemma 5.1 (2) applies with $\mathcal E = (k,0)$ and $\alpha\in(0,k)$,
and its proof gives $u\in\mathcal A^{\mathcal E'}$ with $\mathcal E'$ the index set of III.A Lemma 1.4 built from
$E(\alpha)$ (the boundary spectrum with real part $>\alpha$), $F = (k,0)$ and their shifts by $\mathbb N_0$:
$E_0 = E(\alpha)\bar\cup F$, $E_{j+1} = E(\alpha)\bar\cup(F\bar\cup(E_j+1))$. By III.D Lemma 4.1 and (4.2), every
indicial root with positive real part is at least $\lambda^\Upsilon_{\mathrm s1,2}\in(2,3)$; so $E(\alpha)$ has
$\min\mathrm{Re}\ge\lambda^\Upsilon_{\mathrm s1,2}$, and $\lambda^\Upsilon_{\mathrm s1,2}-2>\epsilon_{\mathrm{ind}}$ by
the choice of $\epsilon_{\mathrm{ind}}$. The exponent $k$ occurs in each $E_j$ only through $F$, with logarithmic order
0: $k\notin E(\alpha)$, and $E_j+1$ has minimal real part at least $k+1$. Every other element of
$\mathcal E' = \bigcup_jE_j$ has real part $\ge k+1$ or $\ge\lambda^\Upsilon_{\mathrm s1,2}$, hence
$\ge k+\epsilon_{\mathrm{ind}}$. So $\mathcal E'\subset(k,0)\cup(k+\mathcal E_{\mathrm{ind}})$; the roots do not depend
on $b$ (III.D Lemma 4.1), nor does this index set. Inserting $u = \rho^ku_k+O(\rho^{k+\epsilon_{\mathrm{ind}}})$ into
$Au = \rho^{-2}f$ and comparing the $\rho^k$ terms gives $I(k)u_k = f_{2+k}$; $I(k)$ is invertible since neither 1 nor 2
is an indicial root (III.D$''$ section 1). $\square$

**Proposition 2.2 ([Hin26] Proposition 8.9 at n = 4).** For $b$ near $b_0$ and
$\dot b = (\dot\mu,\dot A)\in\mathbb R\times\mathfrak{so}(4)$ let
$\eta_b(\dot b) := 2\delta_{g_b,E_\Upsilon}G_{g_b}\dot g_b(\dot b)$ and
$$\dot\omega_b(\dot b) := -\widehat{\Box^\Upsilon_b}(0)^{-1}\eta_b(\dot b),
\qquad\dot g^\Upsilon_b(\dot b) := \dot g_b(\dot b)+\delta^*_{g_b}\dot\omega_b(\dot b).\tag{2.1}$$
(1) $\dot\omega_b(1,0)\in\mathcal A^{(1,0)\cup(1+\mathcal E_{\mathrm{ind}})}$ and
$\dot\omega_b(0,\dot A)\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$; in particular neither has a logarithmic
term (the source's $c_b(\log\rho)\bar\omega^{(0)}_{\mathrm s0}$ is absent).

(2) $\dot g^\Upsilon_b(\dot b)$ lies in $\ker D_{g_b}\mathrm{Ric}\cap\ker\delta_{g_b,E_\Upsilon}G_{g_b}$, hence in
$\ker\widehat{L_b}(0)$, and
$$\dot g^\Upsilon_b(1,0)\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})},
\qquad\dot g^\Upsilon_b(0,\dot A)\in\mathcal A^{(3,0)\cup(3+\mathcal E_{\mathrm{ind}})}.\tag{2.2}$$

(3) $\dot\omega_b(\dot b)$ and $\dot g^\Upsilon_b(\dot b)$ are linear in $\dot b$ and of class $C^k$ in $b$ for every
$k$, with values in $\bar H^{s,\alpha'}_{\mathrm b}$, resp. $\bar H^{s-1,\alpha'+1}_{\mathrm b}$, for every $s$ and
every $\alpha'\in(0,1)$ (for $\dot b = (1,0)$) or $\alpha'\in(0,2)$ (for $\dot b = (0,\dot A)$).

(4) At $b_0$, $\dot\omega_{b_0}(1,0)$ and $\dot g^\Upsilon_{b_0}(1,0)$ are of scalar type 0, and
$\dot\omega_{b_0}(0,\dot A)$, $\dot g^\Upsilon_{b_0}(0,\dot A)$ of vector type 1; and the coefficient $f_t$ of
$\dot g^\Upsilon_{b_0}(0,\dot A)$ is that of $\dot g_{b_0}(0,\dot A)$.

*Proof.* (1) By III.B (3.7), $\dot g_b(1,0)\in\rho^2C^\infty$ and $\dot g_b(0,\dot A)\in\rho^3C^\infty$ near
$\partial X$, smooth on $\bar X$ and stationary. As in the proof of III.D$''$ Lemma 2.1,
$\delta_{g_b}\in\rho\,\mathrm{Diff}^1_{\mathrm b}$, $E^\Upsilon_{g_b}\in\rho\,\mathrm{Diff}^0_{\mathrm b}$ and
$G_{g_b}\in\mathrm{Diff}^0_{\mathrm b}$ near $\partial X$, with coefficients smooth on $\bar X$; so
$\eta_b(1,0)\in\rho^3C^\infty$ and $\eta_b(0,\dot A)\in\rho^4C^\infty$, and Lemma 2.1 with $k = 1$, resp. $k = 2$, gives
(1).

(2) $g_b$ is Ricci-flat for every $b$ (III.B Proposition 3.4), so $D_{g_b}\mathrm{Ric}(\dot g_b(\dot b)) = 0$; and
$D_{g_b}\mathrm{Ric}\circ\delta^*_{g_b} = 0$, since $2\delta^*_{g_b}X^\flat = \mathcal L_Xg_b$ and
$D_{g_b}\mathrm{Ric}(\mathcal L_Xg_b) = \mathcal L_X\mathrm{Ric}(g_b) = 0$. With
$\Box^\Upsilon_b = 2\delta_{g_b,E_\Upsilon}G_{g_b}\delta^*_{g_b}$ (III.D section 1),
$2\delta_{g_b,E_\Upsilon}G_{g_b}\dot g^\Upsilon_b = \eta_b+\Box^\Upsilon_b\dot\omega_b = 0$; and then
$\widehat{L_b}(0)\dot g^\Upsilon_b = D_{g_b}\mathrm{Ric}(\dot
g^\Upsilon_b)+\delta^*_{g_b,E_C}\delta_{g_b,E_\Upsilon}G_{g_b}\dot g^\Upsilon_b = 0$ (III.F (1.1)). Since
$\delta^*_{g_b}\in\rho\,\mathrm{Diff}^1_{\mathrm b}$ (III.D$''$ (2.1)) maps $\mathcal A^{\mathcal F}$ to
$\mathcal A^{1+\mathcal F}$, (1) gives (2.2).

(3) Linearity is clear. $b\mapsto\dot g_b(\dot b)$ is smooth into $C^\infty$ (III.B (3.7) holds smoothly in $b$), so
$b\mapsto\eta_b(\dot b)$ is smooth into $\bar H^{s-1,\alpha'+2}_{\mathrm b}$ for every $s$ and $\alpha'<k$; III.D$''$
Lemma 2.2 gives $\dot\omega_b$, and $\delta^*_{g_b}$ is smooth in $b$.

(4) At $b_0$ the operators $\delta_{g_{b_0},E_\Upsilon}$, $G_{g_{b_0}}$ and $\Box^\Upsilon_{b_0}$ commute with the
rotations of $x$ ($c_\Upsilon$ and $c_{\Upsilon,H}$ are rotation-invariant, III.D$''$ section 1), and so does
$\widehat{\Box^\Upsilon_{b_0}}(0)^{-1}$, being the inverse of an invertible operator that commutes with them. The
projections onto a type and degree (III.A$'$ Lemma 1.6) are averages over $SO(4)$ and commute with all of these; so
$\dot\omega_{b_0}(\dot b)$ and $\dot g^\Upsilon_{b_0}(\dot b)$ have the type of $\dot g_{b_0}(\dot b)$, which Lemma 1.1
gives. A stationary 1-form of vector type 1 is $r^2B(r)V_i\,dz^i$, and $\delta^*$ of it shifts $f_t$ by
$\frac r2\partial_tB = 0$ (*computed*: `static5.py` S5). $\square$

*Cross-check.* `zstates5.py` Z5 computes the leading terms of $\eta_{b_0}$ and of the gauge 1-forms, at $\rho^1$ (scalar
type 0) and $\rho^2$ (vector type 1), and the indicial polynomials there, $2(2+z)$ and $3$, nonzero.

**Remark 2.3 ([Hin26] Remark 8.10 at n = 4).** Let $A_V\in\mathfrak{so}(4)$, $V := V(A_V)$, $V_b := g_b(R_{A_V},\cdot)$
and $W := [A(b),A_V]$. Then
$$\dot g^\Upsilon_b(0,[A(b),A_V]) = 2h_{b,\mathrm v1}(V),
\qquad h_{b,\mathrm v1}(V) = \delta^*_{g_b}\omega^{(-1)}_{b,\mathrm v1}(V)\ \text{(III.D}''\text{ (3.4))}.\tag{2.3}$$
*Proof.* By III.E$'$ Lemma 2.2, $\dot g_b(0,W) = D_Ag_b(W) = 2\delta^*_{g_b}V_b$. Let
$D := 2V_b+\dot\omega_b(0,W)-2\omega^{(-1)}_{b,\mathrm v1}(V)$, a stationary 1-form smooth on $\bar X$. Near
$\partial X$, $V_b-V = (g_b-\bar g)(R_{A_V},\cdot)\in\rho C^\infty$ ($g_b-\bar g\in\rho^2C^\infty$, III.D$''$ (2.3), and
$R_{A_V}$ has Cartesian components in $\rho^{-1}C^\infty$),
$\dot\omega_b(0,W)\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$ and
$\omega^{(-1)}_{b,\mathrm v1}(V)-V\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})}$ (III.D$''$ (3.2)); so
$D\in\mathcal A^{\epsilon}$ for every $\epsilon<1$. And $\widehat{\Box^\Upsilon_b}(0)D =
2\delta_{g_b,E_\Upsilon}G_{g_b}(\dot g_b(0,W)+\delta^*_{g_b}\dot\omega_b(0,W)) = 2\delta_{g_b,E_\Upsilon}G_{g_b}\dot
g^\Upsilon_b(0,W) = 0$ by Proposition 2.2 (2) and III.D$''$ (3.3). By III.D$'$ Proposition 4.1, $D = 0$, and
$\dot g^\Upsilon_b(0,W) = \delta^*_{g_b}(2V_b+\dot\omega_b(0,W)) = 2h_{b,\mathrm v1}(V)$. $\square$

So the spin changes in the image of $\mathrm{ad}_{A(b)}$, of dimension $6-\dim\ker\mathrm{ad}_{A(b)}\in\{0,2,4\}$
(III.E$'$ Lemma 2.3), are pure gauge. But for fixed $\dot A = [A,A_V]\ne0$ and $A\to0$,
$\|A_V\|\ge\|\dot A\|/(2\|A\|)\to\infty$, so the gauge potential $2\omega^{(-1)}_{b,\mathrm v1}(V)$, whose leading term
is $2V$, is unbounded as $b$ approaches the Tangherlini parameters. As in the source, the final angular momentum must
therefore be encoded as an element of $\mathfrak{so}(4)$, all six components, and not modulo the pure gauge changes.

## 3. Stationary solutions on five-dimensional Tangherlini ([AHW24] Theorem 6.1 (2))

On $\{r>r_h\}$ use the static chart $(t_s,r,z)$ of III.F$''$ section 2, $f = 1-\mu_0/r^2$, and III.B's $t_*$. A
stationary symmetric 2-tensor or 1-form on $\{r>r_0\}$ is *in $\mathcal A^\beta$ near infinity* if its components in the
frame $(dt_*,dx)$ are; the frames $(dt_*,dr,r\,dz)$ and $(dt_s,dr,r\,dz)$ differ near infinity by matrices with bounded
conormal entries ($t_* = t_s-r_*+c_0+O(r^{-1})$ with all derivatives, III.D Proposition 6.2), so then the
Kodama-Ishibashi coefficients $f_{ab}$, $f_a$, $H_L$, $H_T$ of each harmonic (III.F$''$ Theorem 2.2), as functions of
$r$, are conormal and $O(r^{-\beta})$, and a 1-form $\zeta = A_aS\,dy^a+r^2BS_i\,dz^i$ (or $r^2BV_i\,dz^i$) is in
$\mathcal A^{\beta-1}$ if $A_a$, $rB$ are conormal and $O(r^{1-\beta})$. The ordinary differential equations below have
regular singular points at $r = \infty$ (analytic in $1/r$) with the stated exponents $p_+>p_-$ in $r$. The solution
behaving like $r^{p_-}$ carries no logarithm (in $1/r$ it belongs to the larger exponent $-p_-$; Frobenius), and every
solution not proportional to it grows like $r^{p_+}$, possibly with a logarithmic factor; so a solution that is
$O(r^{-\beta})$ with $-\beta<p_+$ is a multiple of the decaying one.

**Theorem 3.1 ([AHW24] Theorem 6.1 (2) on five-dimensional Tangherlini).** Let $\beta\in(0,1)$, and let $h$ be a
stationary symmetric 2-tensor on $\{r>r_0\}$, smooth there, in $\mathcal A^\beta$ near infinity, of one type and degree,
with $D_{g_{b_0}}\mathrm{Ric}(h) = 0$ on $\{r>r_h\}$. Then there are $\dot b = (\dot\mu,\dot A)$, with $\dot\mu = 0$
unless the type is scalar type 0 and $\dot A = 0$ unless it is vector type 1, and a stationary 1-form $\omega$ on
$\{r>r_0\}$, smooth, of the same type and degree, in $\mathcal A^{\beta-1}$ near infinity, with
$h = \dot g_{b_0}(\dot b)+\delta^*_{g_{b_0}}\omega$ on $\{r>r_h\}$.

*Proof.* Steps 1-6 find, for each type, a 1-form $\omega$ smooth on $\{r>r_h\}$, in $\mathcal A^{\beta-1}$ near
infinity, with $h = \dot g_{b_0}(\dot b)+\delta^*\omega$ on $\{r>r_h\}$; Step 7 makes it smooth on $\{r>r_0\}$. The
formulas quoted are *computed* by `static5.py` S1-S6, from $D\mathrm{Ric}$ itself on coefficients independent of $t$,
with `gmodes5.py`'s reduced operators (the record's supplement Proposition 10.30). A gauge 1-form $\zeta$ in
$\mathcal A^{\beta-1}$ that is smooth on $\{r>r_0\}$ leaves $h' := h+\delta^*\zeta$ smooth on $\{r>r_0\}$, in
$\mathcal A^\beta$ and in the kernel of $D\mathrm{Ric}$.

*Step 1: tensor type, $l\ge2$.* $h = 2r^2H\,T_{ij}dz^idz^j$; $D\mathrm{Ric}(h)_{ab} = D\mathrm{Ric}(h)_{ai} = 0$ and
$D\mathrm{Ric}(h)_{ij} = -r^2(r^{-3}(r^3fH')'-l(l+2)r^{-2}H)T_{ij}$, and $\Phi := r^{3/2}H$ solves
$f(f\Phi')' = V_T\Phi$, $V_T = \frac f{r^2}(l(l+2)+\frac34+\frac{9\mu_0}{4r^2})$, with $V_T/f$ positive and bounded on
$[r_h,\infty)$; the exponents of $H$ are $l$ and $-(l+2)$ at infinity (S1). $H$ is an angular component, the same in all
charts, so smooth on $\{r>r_0\}$; at infinity $H = O(r^{-\beta})$ excludes the exponent $l$, so $H = O(r^{-l-2})$ and
$H' = O(r^{-l-3})$. On solutions, $f$ and $V_T$ being real, $(f\bar\Phi\Phi')' = f|\Phi'|^2+V_T|\Phi|^2/f$; the boundary
terms vanish at $r_h$ ($f = 0$, $\Phi$, $\Phi'$ bounded) and at infinity ($O(r^{-2l-2})$), so
$\int_{r_h}^\infty(f|\Phi'|^2+V_T|\Phi|^2/f)\,dr = 0$, $\Phi = 0$, and $h = 0$.

*Step 2: vector type, $l\ge2$.* $h = 2rf_aV_i\,dy^adz^i+2r^2H_TV_{ij}dz^idz^j$. With $\zeta_0 := r^2BV_i\,dz^i$,
$B := -2H_T/k_V$ (smooth on $\{r>r_0\}$, $rB = O(r^{1-\beta})$), $h' := h+\delta^*\zeta_0$ has $H'_T = 0$ and
$f'_a = F_a$, the invariants $f_a+\frac r{k_V}D_aH_T$ (III.F$''$ Step 2). With $F_t = ry$: $E_r = (k_V^2-2)F_r/(2r^2)$,
$E_T = -k_V(r^2fF_r)'/(2r^3)$ and $E_t = -(f(r^5y')'-(k_V^2-2)r^3y)/(2r^4)$, $k_V^2-2 = l(l+2)-3\ge5$; the exponents of
$f_t = ry$ at infinity are $l$ and $-(l+2)$; and in the ingoing chart $(v,r,z)$, $h_{vi} = rf_tV_i$ and
$h_{ri} = r(f_r-f_t/f)V_i$ (S2). So $F_r = 0$, i.e. $f'_r = 0$, and $h'_{ri} = -rf'_tV_i/f$ is smooth at $r_h$:
$y = f'_t/r$ is $f$ times a smooth function near $r_h$, so $y\to0$ and $y'$ is bounded there. At infinity
$f'_t = O(r^{-\beta})$, so $y = O(r^{-l-3})$, $y' = O(r^{-l-4})$. On solutions
$(r^5\bar yy')' = r^5|y'|^2+(k_V^2-2)r^3|y|^2/f$, with $|y|^2/f$ integrable at $r_h$ and the boundary terms zero at both
ends; so $y = 0$, $h' = 0$ and $h = \delta^*(-\zeta_0)$.

*Step 3: scalar type, $l\ge2$.* $h = f_{ab}S\,dy^ady^b+2rf_aS_i\,dy^adz^i+2r^2(H_L\gamma_{ij}S+H_TS_{ij})dz^idz^j$. With
[KI03]'s gauge 1-form $\zeta_1 := -2X_aS\,dy^a-\frac{2r^2}kH_TS_i\,dz^i$, $X_a := \frac rk(f_a+\frac rkD_aH_T)$ ((2.8);
built covariantly on the orbit space from $h$, so smooth on $\{r>r_0\}$, and $O(r^{1-\beta})$),
$h' := h+\delta^*\zeta_1$ has $f'_a = H'_T = 0$, its remaining components being the invariants $F_{ab}$, $F$ of [KI03]
(2.7) (III.F$''$ Step 3). Then (S3): $E_{tr} = k^2F_{tr}/(2r^2)$, so $F_{tr} = 0$;
$E_T = -\frac{k^2}{4r^2}(fF_{rr}-F_{tt}/f+2F)$, solved by [KI03]'s $X := r(-F_{tt}/f-2F)$, $Y := r(fF_{rr}-2F)$; $E_r$
and the combination of $E_{tt}$, $E_{rr}$, $E_L$ free of second derivatives give the flow
$$Y' = \frac{\mu_0(X-Y)}{r(r^2-\mu_0)},
\qquad X' = \frac{\mu_0(\mu_0-2r^2)X+(k^2r^2(r^2-\mu_0)+4\mu_0r^2-3r^4)Y}{\mu_0r(r^2-\mu_0)},\tag{3.1}$$
on which all seven equations hold; with $\tilde Z := \frac{fr^2}{k^2}(X'-\frac Xr-(\frac{f'}f-\frac2r)Y)$ and
$H := k^2-3+6\mu_0/r^2$, $\Phi := (3\tilde Z-r(X+Y))/(r^{1/2}H)$ solves $f(f\Phi')' = V_S\Phi$, $V_S = fQ/(16r^2H^2)$,
where on (3.1)
$$3\tilde Z-r(X+Y) = \frac{-\mu_0(k^2r^2+9r^2-6\mu_0)X+(3(k^2-3)r^4-2(2k^2-9)\mu_0r^2-12\mu_0^2)Y}{k^2\mu_0r},\tag{3.2}$$
the determinant of $(r^{1/2}\Phi,r^{1/2}\Phi')$ as linear forms in $(X,Y)$ is $r^3/(k^2\mu_0)\ne0$, and the exponents of
$\Phi$ at infinity are $l+\frac32$ and $-l-\frac12$. At $r_h$: where $F_{tr} = 0$, in ingoing components
$F_{vv} = -fF_{vr}$, $X = r(F_{vr}-2F)$ and $Y = r(fF_{rr}+F_{vr}-2F)$ (S3), smooth since $h'$ is; so by (3.2), whose
coefficients are polynomials in $r$ divided by $k^2\mu_0r$, and $H\ge k^2-3>0$, $\Phi$ is smooth on $[r_h,\infty)$. At
infinity $X,Y = O(r^{1-\beta})$, so $\Phi = O(r^{7/2-\beta})$ by (3.2), which excludes the exponent
$l+\frac32\ge\frac72$: $\Phi = O(r^{-l-1/2})$, $\Phi' = O(r^{-l-3/2})$. As $Q>0$ on $\{r>r_h\}$ for $l\ge2$ (III.F$''$
Theorem 2.2, Step 3; `gmodes5.py` G5), $V_S>0$ and $V_S/f$ is bounded; the identity
$(f\bar\Phi\Phi')' = f|\Phi'|^2+V_S|\Phi|^2/f$ gives $\Phi = 0$ as in Step 1; then $\Phi' = 0$, the determinant gives
$X = Y = 0$, $E_T = 0$ gives $6F = 0$, so $F = F_{tt} = F_{rr} = 0$, $h' = 0$ and $h = \delta^*(-\zeta_1)$.

*Step 4: scalar type 0.* $h = f_{ab}\,dy^ady^b+2r^2H_L\gamma$. $\delta^*(A_t\,dt_s+A_r\,dr)$ shifts $H_L$ by $fA_r/(2r)$
and $f_{tr}$ by $\frac f2(A_t/f)'$ (S4). Put $A_r := -2rH_L/f$ and $A_t := -f\int_{r_1}^r2f_{tr}f^{-1}\,dr'$, smooth on
$(r_h,\infty)$ and $O(r^{1-\beta})$ ($\beta<1$); $h' := h+\delta^*\zeta$, $\zeta := A_t\,dt_s+A_r\,dr$, has
$H'_L = f'_{tr} = 0$, is $O(r^{-\beta})$ and solves the stationary equations, which then give $F_{tt}'' = -3F_{tt}'/r$
with $F_{rr}$ algebraic in $(F_{tt},F_{tt}')$ (S4): $(f'_{tt},f'_{rr}) = c(f,0)+\dot\mu(r^{-2},r^{-2}f^{-2})$. The first
is $cf\,dt_s^2$, not $O(r^{-\beta})$ unless $c = 0$. By Lemma 1.1,
$\dot g_{b_0}(1,0) = r^{-2}dt_s^2+2r^{-2}f^{-1}dt_s\,dr+r^{-2}f^{-2}dr^2$, and
$2r^{-2}f^{-1}dt_s\,dr = \delta^*(A^\mu\,dt_s)$ with $A^\mu := -f\int_r^\infty2s^{-2}f(s)^{-2}\,ds = O(r^{-1})$
($\delta^*(A\,dt_s)$ has only the $tr$ component $\frac f2(A/f)'$). So
$h = \dot\mu\,\dot g_{b_0}(1,0)+\delta^*(-\zeta-\dot\mu A^\mu\,dt_s)$ on $\{r>r_h\}$.

*Step 5: vector type 1.* $h = 2rf_aV_i\,dy^adz^i$, $V_{ij} = 0$. Here $D\mathrm{Ric}(h)_{ab} = 0$, $E_r = 0$,
$D\mathrm{Ric}(h)_{ij} = 0$ and $E_t = -f(r^5y')'/(2r^4)$, $f_t = ry$ (S5); so $f_t = ar+b'r^{-3}$, and $f_r$ is
unconstrained. $\delta^*(r^2BV_i\,dz^i)$ shifts $f_r$ by $\frac r2B'$ and $f_t$ by 0 (S5). Put
$B := 2\int_\infty^rf_r(s)s^{-1}\,ds$, convergent and $O(r^{-\beta})$; then $h' := h-\delta^*(r^2BV_i\,dz^i)$ has
$f'_r = 0$, $f'_t = f_t$, and is $O(r^{-\beta})$, so $a = 0$. Let $\dot A$ with $V(\dot A) = (b'/\mu_0)r^2V_i\,dz^i$; by
Lemma 1.1, $k := h-\dot g_{b_0}(0,\dot A)$ has $f_t = 0$ and $f_r = O(r^{-\beta})$, and with
$\tilde B := 2\int_\infty^rf^{(k)}_r(s)s^{-1}\,ds$, $k-\delta^*(r^2\tilde BV_i\,dz^i)$ has $f_t = f_r = 0$, so vanishes.
Hence $h = \dot g_{b_0}(0,\dot A)+\delta^*(r^2\tilde BV_i\,dz^i)$, with $r\tilde B = O(r^{1-\beta})$.

*Step 6: scalar type 1.* $h = f_{ab}S\,dy^ady^b+2rf_aS_i\,dy^adz^i+2r^2H_L\gamma_{ij}S\,dz^idz^j$,
$D_iD_jS = -\gamma_{ij}S$, $k = 3^{1/2}$. For stationary $\zeta = A_tS\,dt_s+A_rS\,dr+r^2BS_i\,dz^i$, $\delta^*\zeta$
shifts $f_{tt}$, $f_t$, $H_L$ by $-\frac{ff'}2A_r$, $-\frac k{2r}A_t$, $\frac k6B+\frac f{2r}A_r$, free of derivatives,
with determinant $-\mu_0(r^2-\mu_0)/(4r^6)\ne0$ on $(r_h,\infty)$ (rows $f_{tt}$, $f_t$, $H_L$; columns $A_t$, $A_r$,
$B$), and $f_{rr}$, $f_r$ by $A_r'+\frac{\mu_0A_r}{r(r^2-\mu_0)}$ and $\frac{r^2B'-kA_r}{2r}$; and when
$f_{tt} = f_t = H_L = 0$ the stationary equations force $f_{tr} = f_{rr} = f_r = 0$ (S6; the shift formulas are those of
`gmodes5.py` G3 at $\sigma = 0$). Let $\zeta$ solve the algebraic system making $h+\delta^*\zeta$ have
$f_{tt} = f_t = H_L = 0$; then $h+\delta^*\zeta = 0$, and $\omega := -\zeta$ has $h = \delta^*\omega$. Its coefficients
satisfy, from the $f_t$, $f_{rr}$ and $H_L$ components of $h = \delta^*\omega$:
$A^\omega_t = -2rf_t/k = O(r^{1-\beta})$; $(f^{1/2}A^\omega_r)' = f^{1/2}f_{rr}$, so
$A^\omega_r = f^{-1/2}(c+\int_{r_1}^rf^{1/2}f_{rr}) = O(r^{1-\beta})$; and
$B^\omega = \frac6k(H_L-\frac f{2r}A^\omega_r) = O(r^{-\beta})$. So $\omega\in\mathcal A^{\beta-1}$ near infinity.

*Step 7: across the horizon.* By III.A$'$ Lemma 1.6 the sectors of Steps 1-6 are all the types and degrees of symmetric
2-tensors on $\mathbb S^3$. In each, $h = \dot g_{b_0}(\dot b)+\delta^*\omega$ on $\{r>r_h\}$ with $\omega$ smooth there
and in $\mathcal A^{\beta-1}$. III.F$''$ Lemma 2.1 holds at $\sigma = 0$ with the same proof (its formulas are
$\delta^*$'s with $\partial_\tau\mapsto0$). Let $\tilde\omega$ be the solution on $(r_0,\infty)$, in the chart
$(t_*,r,z)$, of the $r$-row system of $\delta^*\tilde\omega = h-\dot g_{b_0}(\dot b)$, whose coefficients and right side
are smooth on $(r_0,\infty)$, with $\tilde\omega = \omega$ at one point $r_1>r_h$. By Lemma 2.1 (a) there,
$\tilde\omega = \omega$ on $(r_h,\infty)$; so $\tilde\omega$ is smooth on $(r_0,\infty)$ and in $\mathcal A^{\beta-1}$
near infinity. $\square$

**Corollary 3.2 (stationary gauge invariants at $b_0$).** On $\{r>r_h\}$, for stationary 1-forms $\omega$: (a) if
$\dot\mu\,\dot g_{b_0}(1,0) = \delta^*\omega$, then $\dot\mu = 0$; (b) if $\dot g_{b_0}(0,\dot A) = \delta^*\omega$,
then $\dot A = 0$; (c) if $\omega$ is of scalar type 1 and $\delta^*\omega = 0$, then $\omega = 0$.

*Proof.* At $b_0$, $\delta^*$ commutes with the projections onto types and degrees, so in (a) and (b) $\omega$ may be
replaced by its scalar type 0, resp. vector type 1, part. (a) For $\omega = A_t\,dt_s+A_r\,dr$, the $H_L$ component
$fA_r/(2r)$ of $\delta^*\omega$ must vanish, so $A_r = 0$, and then the $tt$ component $-\frac{ff'}2A_r$ vanishes, while
that of $\dot g_{b_0}(1,0)$ is $r^{-2}$ (Lemma 1.1). (b) $\delta^*(r^2BV_i\,dz^i)$ has $f_t = 0$ (Proposition 2.2 (4)),
while $\dot g_{b_0}(0,\dot A)$ has $f_t = \mu_0r^{-3}$ on $r^{-2}V(\dot A)$ (Lemma 1.1). (c) Componentwise in a basis of
$\mathcal S_1$, the shifts of $f_{tt}$, $f_t$, $H_L$ vanish, and their determinant is nonzero (Step 6), so
$A_t = A_r = B = 0$. $\square$

## 4. The zero energy kernel and cokernel ([Hin26] Proposition 8.11 and Corollary 8.13 at n = 4)

For $\alpha\in(0,1]$ consider
$$\widehat{L_b}(0):\mathcal X_b := \{u\in\bar H^{s,\alpha}_{\mathrm b}(\bar X;S^2T^*X):\widehat{L_b}(0)u\in\bar
 H^{s-1,\alpha+2}_{\mathrm b}\}\to\bar H^{s-1,\alpha+2}_{\mathrm b}(\bar X;S^2T^*X).\tag{4.1}$$
Under the pairing $\langle u,v\rangle := \int_X\langle u,v\rangle_{g_b}|dx|$, and $|dx| = \rho^{-4}\mu_{\mathrm b}$, the
dual of $\bar H^{s-1,\alpha+2}_{\mathrm b}$ is $\dot H^{1-s,2-\alpha}_{\mathrm b}$ (the source's footnote 79 at
$n = 4$).

**Proposition 4.1 ([Hin26] Proposition 8.11 at n = 4).** For $b$ near $b_0$ and every $\alpha\in(0,1]$, (4.1) is
Fredholm of index 0, and:

(1) (*Kernel.*) Its nullspace is eleven-dimensional, spanned by
$$\dot g^\Upsilon_b(1,0)\in\mathcal A^{(2,0)\cup(2+\mathcal E_{\mathrm{ind}})},
\quad\dot g^\Upsilon_b(0,\dot A)\in\mathcal A^{(3,0)\cup(3+\mathcal E_{\mathrm{ind}})}\ (\dot A\in\mathfrak{so}(4)),
\quad h_{b,\mathrm s1}(S)\in\mathcal A^{(3,0)\cup(3+\mathcal E_{\mathrm{ind}})}\ (S\in\mathcal S_1),\tag{4.2}$$
of Proposition 2.2 and III.D$''$ (3.4); all lie in $\ker\delta_{g_b,E_\Upsilon}G_{g_b}$.

(2) (*Cokernel.*) The annihilator of its range in $\dot H^{1-s,2-\alpha}_{\mathrm b}$ is the kernel there of
$\widehat{L_b}(0)^*$, and is eleven-dimensional, spanned by the dual states of III.E Proposition 3.1 (2),
$$h^*_{b,\mathrm s0},\qquad h^*_{b,\mathrm s1}(S)\ (S\in\mathcal S_1),
\qquad h^*_{b,\mathrm v1}(V)\ (V\in\mathcal V_1).\tag{4.3}$$

*Proof.* *Step 0: the index.* $\widehat{L_b}$ satisfies (H1)-(H5) with index 0 at $\sigma\ne0$ (III.F$''$ Corollary
1.2), (G) with the weight $\alpha-2$ of I.C, since $\alpha\in(0,\beta^L_+)$ (section 1), and (TF) with the weight
$\alpha$ (III.F$'$ Proposition 3.3); so (4.1) has index 0 by I.C Corollary 6.6. By I.C Theorem 3.1 (1)-(2) it is
Fredholm, the annihilator of its range is the kernel of the adjoint on the dual domain, and every element of its
nullspace is smooth up to $\partial_\sharp X$ and lies in $\mathcal A^\beta$ near $\partial X$ for every
$\beta<\beta^L_+$ (the upper end of the gap containing $\alpha$). The pairing with $|dx|$ and $g_b$ in place of I.C's
identifies the adjoints' kernels by an invertible bundle map, smooth on $\bar X$.

*Step 1: the states and the dual states.* By Proposition 2.2 (2) and III.D$''$ Proposition 3.1 (2), the tensors (4.2)
lie in $\ker D_{g_b}\mathrm{Ric}\cap\ker\delta_{g_b,E_\Upsilon}G_{g_b}\subset\ker\widehat{L_b}(0)$, and, being smooth on
$\bar X$ and $O(\rho^2)$, in $\bar H^{s,\alpha}_{\mathrm b}$ for $\alpha<2$. For the adjoint:
$G := G_{g_b} = \mathrm{Id}-\frac12g_b\,\mathrm{tr}_{g_b}$ is self-adjoint and invertible,
$G^{-1} = \mathrm{Id}-\frac13g_b\,\mathrm{tr}_{g_b}$ in five dimensions, and $G\circ D_{g_b}\mathrm{Ric}$ is formally
self-adjoint (the linearised Einstein operator; III.E$'$ (E$'$4)); so
$(D_{g_b}\mathrm{Ric})^* = G\,D_{g_b}\mathrm{Ric}\,G^{-1}$ and
$$L_b^* = G\,D_{g_b}\mathrm{Ric}\,G^{-1}+G(\delta_{g_b,E_\Upsilon})^*(\delta^*_{g_b,E_C})^*.\tag{4.4}$$
For $h^* = G\delta^*_{g_b}\omega^*$ with $\omega^*\in\ker(\Box^C_b)^*$, using
$D_{g_b}\mathrm{Ric}\circ\delta^*_{g_b} = 0$ and $(\Box^C_b)^* = 2(\delta^*_{g_b,E_C})^*G\delta^*_{g_b}$ (from
$\Box^C_b = 2\delta_{g_b}G\delta^*_{g_b,E_C}$, III.E section 1),
$L_b^*h^* = G(\delta_{g_b,E_\Upsilon})^*\frac12(\Box^C_b)^*\omega^* = 0$. The dual states (4.3) are of this form (III.E
Proposition 3.1), stationary, so in the kernel of $\widehat{L_b}(0)^* = \widehat{L_b^*}(0)$ (section 1), and they lie in
$\dot H^{0,((3,0),C_0+3)}_{\mathrm b}\subset\dot H^{1-s,2-\alpha}_{\mathrm b}$ ($2-\alpha<3$, $s\ge1$; they vanish on
$\{r_0<|x|<r_h\}$). By Step 0 they annihilate the range.

*Step 2: the dual states are independent, for every $b$.* Let
$ah^*_{b,\mathrm s0}+h^*_{b,\mathrm s1}(S)+h^*_{b,\mathrm v1}(V) = 0$, and $\omega := a\omega^{*(0)}_{b,\mathrm
s0}+\omega^{*(0)}_{b,\mathrm s1}(S)+\omega^{*(-1)}_{b,\mathrm v1}(V)$. Then $\delta^*_{g_b}\omega = 0$: $\omega$ is a
Killing 1-form of $g_b$ on $X^\circ$, which vanishes on $\{r_0<|x|<r_h\}$ (III.E Proposition 3.1 (2)), hence everywhere
($\nabla\nabla\omega$ is a linear expression in $\omega$ through the curvature, so $\omega$ is determined by
$(\omega,\nabla\omega)$ at one point of the connected $X^\circ$). By III.E (3.1) and III.D$''$ (3.2), near $\partial X$,
$\omega = \chi(-a\,d\bar t+\xi_S\cdot dx+V)+\omega_2$ with $|x|S = \xi_S\cdot x$ and $\omega_2$ partially
polyhomogeneous with index set $(2,0)$; $V$ has Cartesian components homogeneous of degree 1, and $d\bar t = dt_*+d|x|$
and the $dx^i$ are independent on $\partial X$. So $\omega = 0$ forces $V = 0$, then $a = 0$ and $\xi_S = 0$.

*Step 3: the kernel at $b_0$.* Let $u$ be in the nullspace of (4.1) at $b_0$, and fix $\beta\in(0,1)$, so that
$u\in\mathcal A^\beta$ near $\partial X$, smooth up to $\partial_\sharp X$ (Step 0).

(i) *The gauge 1-form.* $\eta := \delta_{g,E_\Upsilon}Gu\in\mathcal A^{1+\beta}$, smooth up to $\partial_\sharp X$. The
linearised second Bianchi identity $\delta_gG_gD_g\mathrm{Ric} = 0$ gives
$\delta_gG_gL_{b_0} = \frac12\Box^C\delta_{g,E_\Upsilon}G_g$, so $\widehat{\Box^C}(0)\eta = 0$. As
$\eta\in\bar H^{s',1}_{\mathrm b}$ for every $s'$, which is the Euclidean weight $-1$, and $-1+2\in[-C_0,2)$, III.E
Theorem 1.1 (2) gives $\eta = 0$. So $D_{g_{b_0}}\mathrm{Ric}(u) = 0$ and $\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}u = 0$.

(ii) *Harmonics.* Both operators commute with the rotations at $b_0$ (section 2, proof of Proposition 2.2 (4)), so each
component $u_\pi$ of a type and degree $\pi$ (III.A$'$ Lemma 1.6) lies in both kernels, is smooth on $\{r>r_0\}$ and in
$\mathcal A^\beta$. By Theorem 3.1, $u_\pi = \dot g_{b_0}(\dot b_\pi)+\delta^*\omega_\pi$ on $\{r>r_h\}$, with
$\omega_\pi$ of type $\pi$, smooth on $\{r>r_0\}$, in $\mathcal A^{\beta-1}$. Let
$\omega'_\pi := \omega_\pi-\dot\omega_{b_0}(\dot b_\pi)$, of type $\pi$ (Proposition 2.2 (4)) and in
$\mathcal A^{\beta-1}$ (Proposition 2.2 (1)). Then $u_\pi = \dot g^\Upsilon_{b_0}(\dot b_\pi)+\delta^*\omega'_\pi$ on
$\{r>r_h\}$, and applying $2\delta_{E_\Upsilon}G$, $\Box^\Upsilon_{b_0}\omega'_\pi = 0$ there.

(iii) *Inside the horizon.* III.F$''$ Lemma 2.3 holds at $\sigma = 0$ with the same proof (the radial equation
$-fU''+AU'+BU = 0$ in the ingoing chart does not use $\sigma\ne0$). With $Q = \Box^\Upsilon_{b_0}$ it gives
$\tilde\omega_\pi$, smooth on $\{r>r_0-\delta_0\}$, so up to $\{r = r_0\}$, equal to $\omega'_\pi$ on $\{r\ge r_h\}$,
with $\widehat{\Box^\Upsilon_{b_0}}(0)\tilde\omega_\pi = 0$ on all of $\bar X$.

(iv) *The expansion at infinity.* Near $\partial X$, $\widehat{\Box^\Upsilon_{b_0}}(0) = \rho^2A$ with $A$ elliptic, and
$\tilde\omega_\pi\in H^{\infty,a}_{\mathrm b}$ for every $a<\beta-1$; take $a\in(-1,\beta-1)$. III.A Lemma 1.4, applied
on $E$ as in the proof of III.D$'$ Lemma 5.1 (2), with $F = \emptyset$ (as $A\tilde\omega_\pi = 0$ there) and a weight
$\epsilon\in(0,\lambda^\Upsilon_{\mathrm s1,2})$, gives $\tilde\omega_\pi\in H^{\infty,(E,\epsilon)}_{\mathrm b}$ with
$E$ built from the roots of real part $>a$. By III.D Lemma 4.1 the only root with real part in
$(a,\epsilon)\subset(-1,\lambda^\Upsilon_{\mathrm s1,2})$ is $0$, at scalar types 0 and 1 only, and it is simple; so
$\tilde\omega_\pi = \chi w_0+w_\epsilon$ with $w_\epsilon\in H^{\infty,\epsilon}_{\mathrm b}\subset\mathcal A^\epsilon$
and $w_0$ an indicial solution for the root 0 of type $\pi$: by III.D Lemma 4.1, $w_0 = c\,d\bar t$ at scalar type 0,
$w_0 = d(|x|S')$ ($S'\in\mathcal S_1$) at scalar type 1, and $w_0 = 0$ otherwise.

(v) *Mode stability.* Let $D_\pi := \tilde\omega_\pi+c\,\omega^{(0)}_{b_0,\mathrm s0}$, resp.
$\tilde\omega_\pi-\omega^{(0)}_{b_0,\mathrm s1}(S')$, resp. $\tilde\omega_\pi$ (recall
$\bar\omega^{(0)}_{\mathrm s0} = -d\bar t$). By III.D$''$ (3.2)-(3.3), $D_\pi\in\mathcal A^{\epsilon'}$ for some
$\epsilon'>0$, smooth on $\bar X$, and $\widehat{\Box^\Upsilon_{b_0}}(0)D_\pi = 0$; III.D$'$ Proposition 4.1 gives
$D_\pi = 0$. As $\delta^*\omega^{(0)}_{b_0,\mathrm s0} = 0$ and
$\delta^*\omega^{(0)}_{b_0,\mathrm s1}(S') = h_{b_0,\mathrm s1}(S')$, on $\{r\ge r_h\}$
$$u_\pi = \dot g^\Upsilon_{b_0}(\dot b_\pi)+h_{b_0,\mathrm s1}(S'_\pi),\tag{4.5}$$
with $\dot b_\pi = 0$ except at scalar type 0 and vector type 1, and $S'_\pi = 0$ except at scalar type 1.

(vi) *The interior.* $k_\pi := u_\pi-\dot g^\Upsilon_{b_0}(\dot b_\pi)-h_{b_0,\mathrm s1}(S'_\pi)$ lies in
$\ker D\mathrm{Ric}\cap\ker\delta_{E_\Upsilon}G$, so $P'k_\pi = 0$ with $2P' = \Box+2\delta^*E^\Upsilon G$ of principal
part $\Box$, and $k_\pi = 0$ on $\{r>r_h\}$; by the system $(r-r_h)Y' = MY$ of III.D Proposition 6.2 (d), as in
III.F$''$ Proposition 3.1 (*The interior*), $k_\pi = 0$ on $\{r>r_0\}$.

So $u_\pi = 0$ except at scalar types 0 and 1 and vector type 1, and $u$, the convergent sum of its components (III.A$'$
Lemma 1.6), lies in the span of (4.2) at $b_0$.

*Step 4: independence at $b_0$.* Suppose $\dot g^\Upsilon_{b_0}(\dot\mu,\dot A)+h_{b_0,\mathrm s1}(S) = 0$. First,
$\omega^{(0)}_{b_0,\mathrm s1}(S)$ is of scalar type 1: with $\Pi$ the projection onto scalar type 1,
$\Pi\omega^{(0)}_{b_0,\mathrm s1}(S)$ lies in $\ker\widehat{\Box^\Upsilon_{b_0}}(0)$ and differs from $d(|x|S)$ by an
element of $\mathcal A^\epsilon$, as $\omega^{(0)}_{b_0,\mathrm s1}(S)$ does, so the two differ by an element of
$\mathcal A^\epsilon\cap\ker\widehat{\Box^\Upsilon_{b_0}}(0) = 0$. So by Proposition 2.2 (4) the three summands are of
scalar type 0, vector type 1 and scalar type 1, and each vanishes. $\dot g^\Upsilon_{b_0}(\dot\mu,0) = 0$ means
$\dot\mu\,\dot g_{b_0}(1,0) = \delta^*(-\dot\omega_{b_0}(\dot\mu,0))$, so $\dot\mu = 0$ (Corollary 3.2 (a)); likewise
$\dot A = 0$ (Corollary 3.2 (b)); and $\delta^*\omega^{(0)}_{b_0,\mathrm s1}(S) = 0$ gives
$\omega^{(0)}_{b_0,\mathrm s1}(S) = 0$ on $\{r>r_h\}$ (Corollary 3.2 (c)), so its leading term $d(|x|S)$ vanishes and
$S = 0$. With Step 3, the nullspace at $b_0$ is eleven-dimensional and spanned by (4.2). By Step 0 the annihilator of
the range has dimension 11, and by Steps 1-2 it is spanned by (4.3).

*Step 5: near $b_0$.* Fix $f^*_j$, $f^\sharp_j$ as in Corollary 4.2. At $b_0$, $\tilde L_{b_0}$ of Corollary 4.2 is
invertible: if $\widehat{L_{b_0}}(0)u+\sum_jc_jf^\sharp_j = 0$ and $\langle u,f^*_j\rangle = 0$ for all $j$, pairing
with the annihilator of the range (Step 4) gives $c = 0$, so $u$ is in the nullspace and $u = 0$; and $\tilde L_{b_0}$
has index 0, being a finite rank perturbation of $\widehat{L_{b_0}}(0)\oplus0_{\mathbb C^{11}\to\mathbb C^{11}}$. This
is (Z$_{\mathcal P}$) of I.C for $\widehat{L_{b_0}}$, with $m_1 = m_2 = 11$ and the compactly supported $f^\sharp_j$,
$f^*_j$; by I.C Theorem 7.1 (1) it holds for $b$ near $b_0$, so $\tilde L_b$ is invertible. Then
$u\mapsto(\langle u,f^*_j\rangle)_j$ is injective on the nullspace of (4.1) at $b$ ($\tilde L_b(u,0) = 0$ otherwise), so
its dimension is at most 11. The eleven states (4.2) depend continuously on $b$ in $\bar H^{s-1,\alpha}_{\mathrm b}$
(Proposition 2.2 (3); III.D$''$ Proposition 3.1, smooth in $b$), so the matrix $(\langle u_i(b),f^*_j\rangle)_{ij}$,
invertible at $b_0$ by Step 4 and the choice of $f^*_j$, stays invertible near $b_0$: the states are independent, hence
a basis. By index 0 the annihilator of the range has dimension 11, and by Steps 1-2 it is spanned by (4.3). $\square$

**Corollary 4.2 ([Hin26] Corollary 8.13 at n = 4).** Fix $f^*_j,f^\sharp_j\in C^\infty_c(X^\circ;S^2T^*X)$,
$j = 1,\dots,11$, real, such that $u\mapsto(\langle u,f^*_j\rangle)_j$ and $u^*\mapsto(\langle f^\sharp_j,u^*\rangle)_j$
restrict to isomorphisms of the nullspace of (4.1) at $b_0$, resp. of the annihilator of its range, onto
$\mathbb C^{11}$. Define
$$\tilde L_b(u,c) := \Big(\widehat{L_b}(0)u+\sum_{j=1}^{11}c_jf^\sharp_j,
\ (\langle u,f^*_j\rangle)_{j=1,\dots,11}\Big).\tag{4.6}$$
(1) (*Invertibility.*) For $b$ near $b_0$, $\tilde L_b:\mathcal X_b\oplus\mathbb C^{11}\to\bar H^{s-1,\alpha+2}_{\mathrm
b}\oplus\mathbb C^{11}$ is invertible, with $\|\tilde L_b^{-1}\|$ bounded near $b_0$; and if $b\mapsto(f_b,c_b)$ is of
class $C^k$ into $\mathcal A^{\alpha+2}(\bar X;S^2T^*X)\oplus\mathbb C^{11}$, then $b\mapsto\tilde L_b^{-1}(f_b,c_b)$ is
of class $C^k$ into $\mathcal A^{\alpha-\epsilon}\oplus\mathbb C^{11}$ for every $\epsilon\in(0,\alpha)$.

(2) (*Inversion of $\widehat{L_b}(0)$.*) If $f\in\mathcal A^{\alpha+2}$ is orthogonal to the dual states (4.3) and
$(u,c) = \tilde L_b^{-1}(f,0)$, then $c = 0$ and $\widehat{L_b}(0)u = f$; if $f$ depends smoothly on $b$ and the
orthogonality holds for all $b$, then $u$ depends smoothly on $b$.

*Proof.* The $f^*_j$, $f^\sharp_j$ exist: the nullspace and the annihilator are finite-dimensional spaces of
distributions on $X^\circ$ (smooth tensors, by Step 0), and the restriction of $C^\infty_c(X^\circ)\to W^*$ to a
finite-dimensional $W\subset\mathcal D'(X^\circ)$ is onto, since otherwise a nonzero element of $W$ would annihilate
every test section; real ones suffice, the spaces being spanned by real tensors.

(1) Invertibility near $b_0$ is Step 5 of the proof of Proposition 4.1. *Uniform bound.* Otherwise there are
$b_j\to b_0$ and $(u_j,c_j)$ with $\|u_j\|_{\bar H^{s,\alpha}_{\mathrm b}}+|c_j| = 1$ and $\tilde L_{b_j}(u_j,c_j)\to0$.
By I.C Theorem 7.1 (2) the estimate (3.2) of I.C Theorem 3.1 holds uniformly near $b_0$: $\|u_j\|_{\bar
H^{s,\alpha}_{\mathrm b}}\le C(\|\widehat{L_{b_j}}(0)u_j\|_{\bar H^{s-1,\alpha+2}_{\mathrm b}}+\|u_j\|_{\bar
H^{-N,-N}_{\mathrm b}})$. Passing to a subsequence, $u_j\to u$ weakly in $\bar H^{s,\alpha}_{\mathrm b}$ and strongly in
$\bar H^{-N,-N}_{\mathrm b}$ (compact inclusion), and $c_j\to c$; since $\widehat{L_{b_j}}(0)-\widehat{L_{b_0}}(0)\to0$
as maps $\bar H^{s,\alpha}_{\mathrm b}\to\bar H^{s-2,\alpha+2}_{\mathrm b}$, $\tilde L_{b_0}(u,c) = 0$, so $(u,c) = 0$;
then $\|\widehat{L_{b_j}}(0)u_j\|\le|c_j|\max_k\|f^\sharp_k\|+o(1)\to0$ and the estimate give
$\|u_j\|_{\bar H^{s,\alpha}_{\mathrm b}}\to0$, contradicting the normalisation. *Smoothness.* As in the proof of
III.D$''$ Lemma 2.2: the coefficients of $\tilde L_b$ depend smoothly on $b$, so $b\mapsto\tilde L_b^{-1}w$ is
continuous for fixed $w$ in $\bigcap_s\bar H^{s-1,\alpha'+2}_{\mathrm b}\oplus\mathbb C^{11}$
($\alpha' := \alpha-\epsilon\in(0,1]$, for which all of the above holds), uniformly on bounded sets, and the difference
quotients converge to $\tilde L_b^{-1}(\dot w-\dot{\tilde L}\tilde L_b^{-1}w)$; induction gives $C^k$. Finally
$\mathcal A^{\alpha+2}\subset\bigcap_s\bar H^{s-1,\alpha'+2}_{\mathrm b}$ near $\partial X$ (with smoothness up to
$\partial_\sharp X$) and $\bigcap_s\bar H^{s,\alpha'}_{\mathrm b}\subset\mathcal A^{\alpha'}$.

(2) Pairing $\widehat{L_b}(0)u+\sum_jc_jf^\sharp_j = f$ with each dual state $h^*_i(b)$ of (4.3), which annihilate the
range (Proposition 4.1 (2)), gives $\sum_jc_j\langle f^\sharp_j,h^*_i(b)\rangle = \langle f,h^*_i(b)\rangle = 0$. The
matrix $(\langle f^\sharp_j,h^*_i(b)\rangle)$ is invertible at $b_0$ by the choice of $f^\sharp_j$, and depends
continuously on $b$ (III.E Proposition 3.1 and III.E$'$ Proposition 3.1: the dual states are continuous in $b$ in
$\dot H^{0,C_0+3}_{\mathrm b}$, resp. $\dot H^{0,((3,0),C_0+3)}_{\mathrm b}$), so it is invertible near $b_0$ and
$c = 0$. Smoothness follows from (1). $\square$

## 5. Findings

(F$'''$1) *No logarithm in Proposition 8.9.* At $n = 4$ the mass enters $g_b$ at $|x|^{-2}$, its gauge correction lies
at $\rho^1$, and 1 is not an indicial root of $\widehat{\Box^\Upsilon_b}(0)$; the source's
$c_b(\log\rho)\bar\omega^{(0)}_{\mathrm s0}$ arises because at $n = 3$ the correction lands on the root 0. The angular
momenta's corrections lie at $\rho^2$, which is not a root for $z>0$ (Lemma 2.1).

(F$'''$2) *Eleven for seven.* The kernel and the cokernel are $1+6+4$ dimensional: the mass, the angular momenta in
$\mathfrak{so}(4)$, the four translations; and the time translation, the six rotations and the four translations. Remark
2.3 is the source's (8.21) with the sign $+2h_{b,\mathrm v1}(V)$ of III.E$'$ Lemma 2.2's normalisation; the pure gauge
spin changes form $\mathrm{im}\,\mathrm{ad}_{A(b)}$, of dimension 0, 2 or 4.

(F$'''$3) *[AHW24] Theorem 6.1 (2) replaced.* At $b_0$ by Theorem 3.1, the Kodama-Ishibashi analysis at zero frequency,
harmonic by harmonic, with energy identities for $l\ge2$ and explicit gauge 1-forms at $l = 0,1$; for $b\ne b_0$ not
needed: the kernel near $b_0$ is counted by the augmented operator of Corollary 4.2, invertible at $b_0$ and hence near
it by I.C Theorem 7.1. No rigidity statement for spinning Myers-Perry metrics is used, and none is proved.

(F$'''$4) *Lemma 8.12 is not needed for Proposition 8.11 or Corollary 8.13.* The independence of the kernel at $b_0$
follows from the types and the stationary gauge invariants of Corollary 3.2, near $b_0$ by continuity; that of the dual
states, at every $b$, from their leading terms and the vanishing of a Killing form that vanishes inside the horizon. The
source counts both with the pairings. Lemma 8.12 at $n = 4$, whose values the record computed (`pairing5.py` P1-P5),
belongs with section 8.5's pairings to the next part, where it is used.

(F$'''$5) *The adjoint.* The source's (8.25), $L^* = G\circ D\mathrm{Ric}\circ G-\dots$, uses $G^2 = \mathrm{Id}$, true
in $3+1$ dimensions only; at $n = 4$ it is (4.4), with $G^{-1} = \mathrm{Id}-\frac13g\,\mathrm{tr}$, and the inclusion
$G\delta^*\ker(\Box^C)^*\subset\ker L^*$ holds as there.

(F$'''$6) *Densities and weights.* $|dg_b| = |dt_*||dx|$ for every $b$ (Kerr-Schild form), so the source's spatial
density is $|dx|$, and the dual of (4.1)'s target is $\dot H^{1-s,2-\alpha}_{\mathrm b}$ (the source's footnote 79 at
$n = 4$). The source's weights $\alpha\in(0,\epsilon_{\mathrm{ind}})$ become $\alpha\in(0,1]$, in the gap of III.F$'$
Proposition 2.3, and the kernel elements decay at least like $\rho^2$, the source's like $\rho^1$.