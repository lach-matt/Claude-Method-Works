# Part III.B. The Myers-Perry family on the compactified spacetime, and the gauge-fixed Einstein equation, at n = 4

*Status.* Written out in full (D215). Not yet read by an independent verifier; nothing here is labelled proved. This
part proves, at spatial dimension $n = 4$, what [Hin26] sections 3 and 4 (pp. 68-83) establish for the Kerr family: the
compactified spacetime and its charts, the black hole family as smooth metrics on it with their decay at infinity, the
time functions, the linearised metrics, the initial data and their decay, the null coordinates near null infinity, the
cut-off Lorentz boosts and the pullback of the family by them, and the gauge-fixed Einstein equation with its
linearisation. The source is [Hin26] = P. Hintz, *Nonlinear stability of subextremal Kerr black holes* (printed page
numbers), read in the record's text extraction. Parts II.A (`PART-II-A-SETUP.md`) and II.C (`PART-II-C-OPERATORS.md`)
are cited as II.A and II.C.

*Method.* At $n = 4$ the black hole family is the Myers-Perry family, written for every spin at once in Kerr-Schild form
(supplement section 10.36). One feature of five dimensions simplifies the source's section 3 throughout: the ingoing and
outgoing Eddington-Finkelstein times of the family differ by a function in $|x|^{-1}C^\infty$, where in four dimensions
they differ by $4m\log r$. So the Kerr-Schild coordinates, in which the family is regular across the future event
horizon, are smooth coordinates on the compactification, and a smooth change of time function, the identity near the
horizon, puts the family into the outgoing form the source uses at null infinity. The time functions are then written
down explicitly and their causal character is read off from one algebraic inequality (Lemma 3.3). The boost lemma is
proved with the exact Lorentz boost, which acts on the compactification by maps homogeneous of degree one.

*Organisation.* Section 1: scope and what $n = 4$ changes. Section 2: the compactification. Section 3: the Myers-Perry
family, time functions, linearised metrics and initial data. Section 4: null coordinates near null infinity. Section 5:
cut-off Lorentz boosts. Section 6: the gauge-fixed Einstein equation. Section 7: findings and sources.

## 1. Scope, and what n = 4 changes

Throughout, $n = 4$, spacetime is $\mathbb R^{1+4}$ with coordinates $(t,x)$, $x\in\mathbb R^4$, $|x|$ is the Euclidean
norm, $\hat x := x/|x|\in\mathbb S^3$, $\eta := -dt^2+dx^2$, and $\bar X$ denotes the radial compactification of
$\mathbb R^4_x$; $C^\infty(\bar X)$ near infinity consists of the smooth functions of $(|x|^{-1},\hat x)$. The changes
from [Hin26] sections 3-4 are these.

(a) The sphere at infinity is $\mathbb S^3$, and the angular indices are $2,3,4$.

(b) The family is $g_b$, $b = (\mu,A)$, $\mu>0$, $A\in\mathfrak{so}(4)$: seven parameters where Kerr has four,
$\mathfrak{so}(4)$ being six-dimensional. The mass enters at $|x|^{-2}$ and the spin at $|x|^{-3}$, where for Kerr they
enter at $r^{-1}$ and $r^{-2}$.

(c) No logarithm: the ingoing and outgoing times differ by $2\int^r\mu(s^2-\mu)^{-1}ds\in|x|^{-1}C^\infty$ (Lemma 3.5).

(d) The boosts are four, $S$ ranging over the restrictions to $\mathbb S^3$ of linear functions, and the boosted mass
term has the exponent 4 and the constant $\frac2{\pi^2}$ where the source has 3 and $\frac3{4\pi}$ (Lemma 5.2).

(e) The trace weight of the gauge modifications is $\frac2{D-2} = \frac23$, $D = n+1 = 5$, where the source has 1, so
that the modifications act on trace-reversed tensors exactly as at $D = 4$ (Lemma 6.1).

## 2. The compactification

Fix $\mu_0>0$ and set $R_1 := \mu_0^{1/2}$ and $r_0 := \frac12R_1$.

**Definition 2.1 ([Hin26] Definitions 3.1-3.2, (3.2)-(3.3)).** $\overline{\mathbb R^{1+4}}$ is the radial
compactification, $k_\pm$ the two points at future and past timelike infinity of the closure of $\{|x|\le C\}$, and
$Y_+\subset\partial\overline{\mathbb R^{1+4}}$ the 3-sphere $\{\frac1t = 0,\ \frac{t-|x|}t = 0\}$ in the closure of
$\{t>0\}$. $\tilde M := [\overline{\mathbb R^{1+4}};k_+,Y_+]$, and
$$M := \mathrm{cl}_{\tilde M}\{|x|\ge r_0,\ t\ge-\tfrac12|x|\},\tag{2.1}$$
with boundary hypersurfaces $I_0$ (spacelike infinity), $\mathscr I^+$ (the lift of $Y_+$), $\iota^+$ (future timelike
infinity), $K^+$ (the lift of $k_+$), $\Sigma^{\mathrm{past}} := \{t = -\frac12|x|\}$ and $\Sigma^{\mathrm{int}} :=
\{|x| = r_0\}$. $\tilde M_{1/2}$ and $M_{1/2}$ are obtained by declaring the square root of a defining function of
$\mathscr I^+$ smooth.

Local coordinates, with $\omega\in\mathbb S^3$ and $t_0 := t-|x|$, are those of [Hin26] (3.4a)-(3.4h) with $r$ replaced
by $|x|$ and $\mathbb S^2$ by $\mathbb S^3$:
$$\tau = \tfrac t{|x|},\ \rho = \tfrac1{|x|};\qquad\rho_0 = \tfrac1{|x|-t+2},\ \rho_I = \tfrac{|x|-t+2}{|x|};\qquad
t_0,\ \rho_I = \tfrac1{|x|};\tag{2.2}$$
$$\rho_I = \tfrac{t-|x|+2}{|x|},\ \rho_+ = \tfrac1{t-|x|+2};\qquad\rho_+ = \tfrac1{|x|},\ v = \tfrac{t_0}{|x|};\qquad
\rho_+ = \tfrac1{|x|},\ \rho_K = \tfrac{|x|}{t_0};\qquad\rho_K = t_0^{-1},\ x,$$
near the interior of $I_0$, near $I_0\cap\mathscr I^+$, near the interior of $\mathscr I^+$, near $\mathscr
I^+\cap\iota^+$, near the interior of $\iota^+$, near $\iota^+\cap K^+$ and near the interior of $K^+$. These are the
coordinates of the iterated blow-up of the radial compactification at $k_+$ and at $Y_+$ (II.A section 1 constructs the
same blow-ups, there in $\{t_0\ge1\}$; nothing in the construction depends on the dimension). $\mathscr I^+$ fibres over
$Y_+\cong\mathbb S^3$ with fibres $\mathbb R_{t_0}$. Two facts are used repeatedly: the functions in $C^\infty(\bar X)$
lift to smooth functions on $M$ (they are smooth functions of $\rho = |x|^{-1}$ and $\omega$, and $\rho = \rho_0\rho_I$,
$\rho_I$, $\rho_I\rho_+$, $\rho_+$, $\rho_+$ in the charts listed, a smooth function on each); and $dt$ and $dx^i$, $i =
1,\dots,4$, form a smooth frame of the scattering cotangent bundle $T^* := {}^{\mathrm{sc}}T^*\overline{\mathbb
R^{1+4}}$ pulled back to $M$ ([Hin26] Notation 3.5). So a symmetric 2-tensor $\sum g_{\mu\nu}dx^\mu dx^\nu$ ($x^0 := t$)
lies in $C^\infty(M;S^2T^*)$ when its coefficients are smooth on $M$, and $|x|^{-j}C^\infty(M;S^2T^*)$ means
coefficients in $|x|^{-j}C^\infty(M)$.

**Lemma 2.2 ([Hin26] Lemma 3.4).** Let $X := \mathrm{cl}_{\bar X}\{|x|\ge r_0\}$ and $M' := [\overline{\mathbb
R}_{t_0}\times X;\{\pm\infty\}\times\partial X]$. The identity of $\mathbb R^{1+4}$ extends to a diffeomorphism from
$\mathrm{cl}_{M'}\{t_0\ge1\}$ onto $\mathrm{cl}_M\{t_0\ge1\}$.

*Proof.* Both sides are covered by the charts below, and the transition maps are smooth with smooth inverses. Away from
the front face $\{+\infty\}\times\partial X$ of $M'$: near $\{+\infty\}\times\mathring X$, $(t_0^{-1},x)$, which are
(2.2)'s coordinates near the interior of $K^+$; near $\mathbb R\times\partial X$, $(t_0,|x|^{-1},\omega)$, (2.2)'s
coordinates near the interior of $\mathscr I^+$. Near the front face, $M'$ has the coordinates
$(\frac{t_0+2}{|x|},\frac1{t_0+2},\omega)$ near its intersection with $\mathbb R\times\partial X$, which are (2.2)'s
$(\rho_I,\rho_+,\omega)$ near $\mathscr I^+\cap\iota^+$; $(\frac1{|x|},\frac{t_0}{|x|},\omega)$ in its interior, (2.2)'s
coordinates near the interior of $\iota^+$; and $(\frac1{|x|},\frac{|x|}{t_0},\omega)$ near its intersection with
$\{+\infty\}\times X$, (2.2)'s coordinates near $\iota^+\cap K^+$. $\square$

## 3. The Myers-Perry family

### 3.1 Kerr-Schild form

For $A\in\mathfrak{so}(4)$ let $s := -\frac12\mathrm{tr}(A^2)$, $p := \mathrm{Pf}(A)$, $\|A\|$ the operator norm, and
for $r>0$
$$P(r) := r^4+sr^2+p^2,\qquad\mathsf M(r) := (r^2+s)I+A^2,\qquad Q(r,x) := P(r)-x^T\mathsf M(r)x.\tag{3.1}$$

**Lemma 3.1 (the radial function).** (a) $A^4+sA^2+p^2I = 0$ and $(r^2I-A^2)\mathsf M(r) = P(r)I$. (b) For $|x|^2>s$
(note $s\ge\|A\|^2$), $Q(\cdot,x)$ has exactly one zero $r = r_A(x)$ in $(0,\infty)$, and it is simple; $r_A$ is smooth
in $(x,A)$, $r_0(x) = |x|$, $r_A(x)^2\le|x|^2\le r_A(x)^2+\|A\|^2$, and $r_A\in|x|(1+|x|^{-2}C^\infty(\bar X))$ near
infinity, smoothly in $A$.

*Proof.* (a) Rotating, $A = aJ_{12}+bJ_{34}$ with $J_{ij}$ the elementary rotation generators; then $A^2 =
-\mathrm{diag}(a^2,a^2,b^2,b^2)$, $s = a^2+b^2$, $p^2 = a^2b^2$, and both identities hold entrywise (and were checked
symbolically: `d215/chk3b.py`). Both sides of each identity are conjugation-covariant, so they hold for every $A$. (b)
With $y := r^2$, $Q = y^2+(s-|x|^2)y+p^2-s|x|^2+|Ax|^2$, using $-x^TA^2x = |Ax|^2$. In the rotated frame the constant
term is $c_0 := a^2b^2-(a^2+b^2)|x|^2+a^2(x_1^2+x_2^2)+b^2(x_3^2+x_4^2)\le a^2b^2-\min(a^2,b^2)|x|^2$, which is negative
when $\min(a^2,b^2)>0$ and $|x|^2>\max(a^2,b^2)$, and equals $-a^2(x_3^2+x_4^2)\le0$ (or the same with the roles
exchanged) when $b = 0$. So $c_0\le0$ on $\{|x|^2>s\}$. The discriminant is $(|x|^2-s)^2-4c_0\ge(|x|^2-s)^2>0$, so the
two roots are real and distinct, their product $c_0\le0$ and their sum $|x|^2-s>0$: exactly one is positive, it is
simple, and it is smooth in the coefficients:
$$r_A^2 = \tfrac12\Big(|x|^2-s+\big((|x|^2-s)^2-4(p^2-s|x|^2+|Ax|^2)\big)^{1/2}\Big),$$
With $z := |x|^{-2}$ this is $|x|^2\cdot\frac12\big(1-sz+((1-sz)^2-4z(p^2z-s+|A\hat x|^2))^{1/2}\big)$, a smooth
function of $(z,\hat x,A)$ near $z = 0$ with value 1 at $z = 0$; so $r_A^2\in|x|^2(1+|x|^{-2}C^\infty(\bar X))$ and
likewise $r_A$. At $A = 0$, $Q = y(y-|x|^2)$, so $r_0 = |x|$. Finally $Q = 0$ and (a) give $x^T(r_A^2I-A^2)^{-1}x = 1$;
as $-A^2\ge0$ with largest eigenvalue $\|A\|^2$, the eigenvalues of $(r_A^2I-A^2)^{-1}$ lie in
$[(r_A^2+\|A\|^2)^{-1},r_A^{-2}]$, which gives the two bounds on $|x|^2$. $\square$

**Definition 3.2 (Myers-Perry in Kerr-Schild form; supplement 10.36, from [ER08] (31)-(34)).** For $\mu>0$,
$A\in\mathfrak{so}(4)$ and $|x|^2>s$, with $r := r_A(x)$ and $P,\mathsf M$ evaluated at $r$,
$$\ell_A := \frac{\mathsf M(rI+A)x}{P}\cdot dx,\qquad k_A := dt+\ell_A,\qquad F_A := 1+\frac{x^TA^2\mathsf M^2x}{P^2},
\qquad H_{\mu,A} := \frac{\mu r^2}{PF_A},$$
$$g^{\mathrm{KS}}_{\mu,A} := \eta+H_{\mu,A}\,k_A\otimes k_A.\tag{3.2}$$

**Lemma 3.3 (Kerr-Schild algebra).** On $\{|x|^2>s\}$: (a) $|\ell_A|_{\mathrm{eucl}} = 1$, so $k_A$ is null for $\eta$;
(b) $\ell_A(x\cdot\partial_x) = r_A(x)$, so $\ell_A(\hat x\cdot\partial_x) = r_A/|x|\in(0,1]$; (c) if
$\|A\|^2(r_A^2+\|A\|^2)<r_A^4$, then $F_A\in(0,1]$ and $H_{\mu,A}>0$; (d) $(g^{\mathrm{KS}}_{\mu,A})^{-1} =
\eta^{-1}-H_{\mu,A}k_A^\sharp\otimes k_A^\sharp$, $k_A^\sharp := \eta^{-1}(k_A,\cdot)$; (e) for $\beta\in(-1,1]$,
wherever (c)'s condition holds, $(g^{\mathrm{KS}}_{\mu,A})^{-1}(dt-\beta\,d|x|,dt-\beta\,d|x|)<0$.

*Proof.* (a), (b): $|\ell_A|^2-1$ and $\ell_A(x\cdot\partial_x)-r$ are rational functions of $(r,x,A)$ which vanish on
$\{Q = 0\}$: in the rotated frame they equal $-Q/P$ and $-rQ/P$ (symbolic computation, `d215/chk3b.py`), and both sides
are conjugation-covariant. (c) $\mathsf M$ commutes with $A$, so $A\mathsf M$ is antisymmetric and $x^TA^2\mathsf M^2x =
-|A\mathsf Mx|^2$; so $F_A\le1$. By (a), $\mathsf M/P = (r^2I-A^2)^{-1}$ has norm at most $r^{-2}$, so $|A\mathsf
Mx|/P\le\|A\||x|r^{-2}\le\|A\|(r^2+\|A\|^2)^{1/2}r^{-2}<1$ under (c)'s condition (Lemma 3.1 (b)); so $F_A>0$ and
$H_{\mu,A}>0$, $P>0$ for $r>0$. (d) $\eta^{-1}(k_A,k_A) = 0$ by (a), and then $(\eta+Hk\otimes
k)(\eta^{-1}-Hk^\sharp\otimes k^\sharp) = I+Hk\otimes k^\sharp-Hk\otimes k^\sharp-H^2\eta^{-1}(k,k)k\otimes k^\sharp =
I$. (e) With $\theta := dt-\beta\,d|x|$, $\eta^{-1}(\theta,\theta) = -1+\beta^2$ and $k_A^\sharp(\theta) =
\eta^{-1}(k_A,\theta) = -1-\beta\,\ell_A(\hat x\cdot\partial_x) = -1-\beta r_A/|x|$. So the quantity is
$-(1-\beta^2)-H(1+\beta r_A/|x|)^2$; for $\beta\in(-1,1)$ the first term is negative and the second non-positive; for
$\beta = 1$ the first vanishes and the second is $-H(1+r_A/|x|)^2<0$. $\square$

**Proposition 3.4 (READ).** $g^{\mathrm{KS}}_{\mu,A}$ is Ricci-flat where it is defined and $H_{\mu,A}>0$. At $A = 0$ it
is the five-dimensional Schwarzschild-Tangherlini metric $\eta+\mu|x|^{-2}(dt+d|x|)^2$, whose future event horizon is
$\{|x| = \mu^{1/2}\}$.

This is the Myers-Perry family [MP86] in the Kerr-Schild form of [ER08] (pp. 14-16, (31)-(34) and (42)-(44), READ in
supplement section 10.36); its Ricci-flatness at five rational points with two independent spins, equal spins and one
spin, in exact arithmetic, and the identification with [ER08] (42) at $A = aJ_{12}+bJ_{34}$, are supplement Proposition
10.33 (i), computed. At $A = 0$ the Ricci-flatness is computed here: in coordinates $(t,|x|,\chi,\theta,\phi)$,
$g^{\mathrm{KS}}_{\mu,0} = -f\,dt^2+2(1-f)\,dt\,d|x|+(2-f)\,d|x|^2+|x|^2\slashed g$, $f = 1-\mu|x|^{-2}$, and its Ricci
tensor vanishes identically (`d215/chkric.py`, sympy). The route uses only $b$ near $b_0 = (\mu_0,0)$.

*The parameter set.* Fix $\epsilon_{\mathrm{param}}\in(0,\frac1{10})$ and let $\mathcal B := \{b =
(\mu,A):|\mu-\mu_0|<\frac12\mu_0,\ \|A\|<\epsilon_{\mathrm{param}}R_1\}$. For $b\in\mathcal B$ and $|x|\ge r_0 =
\frac12R_1$: $|x|^2\ge\frac14R_1^2>2\|A\|^2\ge s$, $r_A^2\ge|x|^2-\|A\|^2\ge\frac14R_1^2-\frac1{100}R_1^2$, so Lemma 3.3
(c)'s condition holds, and $g^{\mathrm{KS}}_b$ is defined, smooth, with $H_b>0$, on $\mathbb R_t\times\{|x|\ge r_0\}$,
smoothly in $b$. The horizon of $g^{\mathrm{KS}}_{\mu,0}$ is at $|x| = \mu^{1/2}\in(R_1/\sqrt2,\sqrt{3/2}R_1)$, inside
$\{|x|>r_0\}$.

### 3.2 The outgoing form near infinity

Fix $\chi_\infty\in C^\infty(\mathbb R)$, non-decreasing, equal to 0 on $(-\infty,2R_1]$ and to 1 on $[3R_1,\infty)$.
For $\mu\in(\frac12\mu_0,\frac32\mu_0)$ let
$$T_\mu(\rho) := 2\int_\rho^\infty\chi_\infty(s)\frac{\mu}{s^2-\mu}\,ds,\qquad\Phi_\mu(t,x) := (t-T_\mu(|x|),x),\qquad
g_b := \Phi_\mu^*g^{\mathrm{KS}}_b.\tag{3.3}$$
($s^2-\mu>\frac12\mu_0>0$ on $\mathrm{supp}\,\chi_\infty$.) Write $g_\mu := g_{(\mu,0)}$ and $\bar g := \eta$.

**Lemma 3.5 (no logarithm).** (a) $T_\mu\in|x|^{-1}C^\infty(\bar X)$ near infinity, with $T_\mu(\rho) =
\sqrt\mu\log\frac{\rho+\sqrt\mu}{\rho-\sqrt\mu} = \frac{2\mu}\rho+\frac{2\mu^2}{3\rho^3}+O(\rho^{-5})$ for
$\rho\ge3R_1$, smooth in $\mu$. (b) For $|x|\ge3R_1$,
$$g_\mu = \eta+\frac\mu{|x|^2}(dt-d|x|)^2 = -f\,dt^2-\frac{2\mu}{|x|^2}dt\,d|x|+(2-f)\,d|x|^2+|x|^2\slashed g,\qquad
f := 1-\frac\mu{|x|^2},\tag{3.4}$$
$\slashed g$ the round metric of $\mathbb S^3$. (c) $\Phi_\mu$ is a diffeomorphism of $\mathbb R_t\times\{|x|\ge r_0\}$
which equals a time translation on $\{|x|\le2R_1\}$; it extends to a diffeomorphism of $\tilde M$ near $\{|x|\ge r_0\}$
preserving every boundary hypersurface, and $\Phi_\mu^*$ maps $\rho_0^\alpha\rho_I^\beta\rho_+^\gamma\rho_K^\delta
C^\infty(M;S^2T^*)$ into itself near $I_0\cup\mathscr I^+\cup\iota^+\cup K^+$, for all weights.

*Proof.* (a) For $\rho\ge3R_1$, $T_\mu(\rho) = 2\int_\rho^\infty\frac\mu{s^2-\mu}ds =
2\sqrt\mu\,\mathrm{artanh}\frac{\sqrt\mu}\rho$, an odd power series in $\sqrt\mu/\rho$ convergent for $\rho>\sqrt\mu$.
(b) On $\{|x|\ge3R_1\}$, $\Phi_\mu^*dt = dt-T_\mu'd|x| = dt+\frac{2\mu}{|x|^2-\mu}d|x|$, and $g^{\mathrm{KS}}_{\mu,0} =
\eta+\frac\mu{|x|^2}(dt+d|x|)^2$. Substituting, the $(t,|x|)$ block of $\Phi_\mu^*g^{\mathrm{KS}}_{\mu,0}$ has $g_{tt} =
-f$, $g_{t|x|} = \frac\mu{|x|^2}-(-f)\frac{2\mu}{|x|^2-\mu} = -\frac\mu{|x|^2}$ and $g_{|x||x|} = 1+\frac\mu{|x|^2}$
(symbolic check: `d215/chk3b.py`), which is (3.4). (c) $T_\mu$ is smooth and bounded, so $\Phi_\mu$ is a diffeomorphism
with inverse $(t,x)\mapsto(t+T_\mu(|x|),x)$, a time translation by $-T_\mu(2R_1)$ on $\{|x|\le2R_1\}$. In each chart of
(2.2) the lift is smooth with smooth inverse: $t_0\mapsto t_0-T_\mu$ with $T_\mu\in\rho C^\infty$ near $\mathscr I^+$;
$\rho_0\mapsto\rho_0(1-\rho_0T_\mu)^{-1}$, $\rho_+\mapsto\rho_+(1-\rho_+T_\mu)^{-1}$, $\rho_K =
t_0^{-1}\mapsto\rho_K(1-\rho_KT_\mu)^{-1}$, $\tau\mapsto\tau-\rho T_\mu$, the other coordinates fixed; each factor is
$1+O(\rho)$ or $1+O(\rho_K)$ with $\rho\in\rho_0\rho_I\rho_+C^\infty$. So the defining functions are multiplied by
positive smooth functions and the weighted spaces are preserved. On the bundle, $\Phi_\mu^*dt = dt-T_\mu'(|x|)\hat
x\cdot dx$ and $\Phi_\mu^*dx^i = dx^i$, with $T_\mu'\hat x^i\in C^\infty(\bar X)$: a smooth bundle map of $T^*$.
$\square$

**Proposition 3.6 ([Hin26] Proposition 3.10 at n = 4).** For $b = (\mu,A)\in\mathcal B$: $g_b\in C^\infty(M;S^2T^*)$ and
$g_b^{-1}\in C^\infty(M;S^2T)$, smoothly in $b$; and
$$g_b-g_\mu\in|x|^{-3}C^\infty(M;S^2T^*),\qquad g_\mu-\bar g\in|x|^{-2}C^\infty(M;S^2T^*),\tag{3.5}$$
with $g_\mu-\bar g = \mu|x|^{-2}(dt-d|x|)^2$ on $\{|x|\ge3R_1\}$; the same for the dual metrics, with $g_\mu^{-1}-\bar
g^{-1} = -\mu|x|^{-2}(\partial_t+\partial_{|x|})^{\otimes2}$ there.

*Proof.* By Lemma 3.5 (c) it suffices to prove the statements for $g^{\mathrm{KS}}_b$, with $g^{\mathrm{KS}}_\mu :=
g^{\mathrm{KS}}_{\mu,0}$ in place of $g_\mu$. By Lemma 3.1 (b), $r := r_A\in|x|(1+|x|^{-2}C^\infty(\bar X))$; so $P,\
r^2+s\in|x|^4(1+|x|^{-2}C^\infty)$, resp. $|x|^2(\dots)$, and $\mathsf M/P =
(r^2-A^2)^{-1}\in|x|^{-2}(I+|x|^{-2}C^\infty(\bar X))$. Hence the coefficient vector of $\ell_A$ is $r\,\mathsf
Mx/P+\mathsf MAx/P = \hat x+|x|^{-1}A\hat x+|x|^{-2}C^\infty(\bar X)$; $F_A\in1+|x|^{-2}C^\infty$ and
$H_{\mu,A}\in\mu|x|^{-2}(1+|x|^{-2}C^\infty(\bar X))$, all smooth in $b$. As $dt$, $dx^i$ form a smooth frame of $T^*$
on $M$ and $C^\infty(\bar X)$ lifts into $C^\infty(M)$ (section 2), $g^{\mathrm{KS}}_b = \eta+H(dt+\ell_A)^2\in
C^\infty(M;S^2T^*)$. At $A = 0$, $\ell_0 = \hat x\cdot dx = d|x|$ and $H_{\mu,0} = \mu|x|^{-2}$, so
$g^{\mathrm{KS}}_\mu-\eta = \mu|x|^{-2}(dt+d|x|)^2\in|x|^{-2}C^\infty$; and $H_{\mu,A}-H_{\mu,0}\in|x|^{-4}C^\infty$,
$\ell_A-\ell_0\in|x|^{-1}C^\infty(\bar X;T^*)$, so $g^{\mathrm{KS}}_b-g^{\mathrm{KS}}_\mu\in|x|^{-3}C^\infty$. The dual
metrics are $\eta^{-1}-Hk^\sharp\otimes k^\sharp$ (Lemma 3.3 (d)), and the same argument applies. On $\{|x|\ge3R_1\}$
the formula for $g_\mu$ is (3.4); its inverse is computed from (3.4), or by applying Lemma 3.3 (d) to the outgoing
Kerr-Schild form $\eta+\mu|x|^{-2}(dt-d|x|)^2$, $dt-d|x|$ being $\eta$-null. $\square$

So the mass of $g_b$ appears in $g_b-\bar g$ at $|x|^{-2} = \rho_0^2\rho_I^2\rho_+^2$ (in the charts (2.2), up to smooth
positive factors), its spin at $|x|^{-3}$: one order of $|x|^{-1}$ further than for Kerr in each case.

### 3.3 Time functions

Let
$$\psi(\rho) := \int_{r_0}^\rho\Big(1-\chi_\infty(s)\frac{8\mu_0}{s^2}\Big)ds,\qquad t_* := t-\psi(|x|).\tag{3.6}$$
For $\rho\ge3R_1$, $\psi(\rho) = \rho-C'+\frac{8\mu_0}\rho$ with a constant $C'$; so $t_* = t_0+C'-8\mu_0|x|^{-1}$ near
infinity, the form of [Hin26] (3.13) with $\tilde T = C'-Cr^{-1}$.

**Lemma 3.7 ([Hin26] Lemmas 3.6-3.7 at n = 4).** (a) For every $b\in\mathcal B$, $dt_*$ is timelike for $g_b$ on
$\{|x|\ge r_0\}$, and $t_*\le t$. (b) There is $t_{\mathrm{IVP}} = t-\psi_{\mathrm{IVP}}(|x|)$ with $\psi_{\mathrm{IVP}}
= \psi$ on $[r_0,5R_1]$, $\psi_{\mathrm{IVP}}$ constant on $[R_3,\infty)$ for some $R_3$, such that $dt_{\mathrm{IVP}}$
is timelike for every $g_b$, $b\in\mathcal B$, $t_{\mathrm{IVP}}\le t$, and $t_{\mathrm{IVP}}-t_*$ is a function of
$|x|$ alone.

*Proof.* Pull back by $\Phi_\mu^{-1}$: in the Kerr-Schild coordinates $(t_{\mathrm{KS}},x) = \Phi_\mu(t,x)$, $t =
t_{\mathrm{KS}}+T_\mu(|x|)$, so a function $t-\phi(|x|)$ has differential $dt_{\mathrm{KS}}-\beta\,d|x|$ with $\beta :=
\phi'-T_\mu' = \phi'+2\chi_\infty\frac\mu{|x|^2-\mu}$. By Lemma 3.3 (e) it suffices that $\beta\in(-1,1]$ on
$[r_0,\infty)$.

(a) $\phi = \psi$: $\beta = 1-\chi_\infty\big(\frac{8\mu_0}{\rho^2}-\frac{2\mu}{\rho^2-\mu}\big)$. Off
$\mathrm{supp}\,\chi_\infty$, $\beta = 1$. On it, $\rho\ge2R_1$, i.e. $\rho^2\ge4\mu_0$, and $\mu<\frac32\mu_0$:
$(8\mu_0-2\mu)\rho^2-8\mu_0\mu\ge5\mu_0\cdot4\mu_0-12\mu_0^2>0$, so the bracket is positive and $\beta<1$; and
$\beta\ge1-\frac{8\mu_0}{\rho^2}>1-2 = -1$ for $\rho>2R_1$ (at $\rho = 2R_1$, $\chi_\infty = 0$). For $t_*\le t$:
$\psi(2R_1) = \frac32R_1$, $\psi'\ge-1$ on $[2R_1,3R_1]$ and $\psi'>0$ elsewhere, so $\psi\ge\frac12R_1>0$.

(b) Choose $\psi_{\mathrm{IVP}}'\in C^\infty$ with $\psi_{\mathrm{IVP}}' = \psi'$ on $[r_0,5R_1]$,
$0\le\psi_{\mathrm{IVP}}'\le\psi'$ on $[5R_1,\infty)$, and $\psi_{\mathrm{IVP}}' = 0$ on $[R_3,\infty)$ (possible as
$\psi'>0$ there), and $\psi_{\mathrm{IVP}}(r_0) = 0$. Then $\beta =
\psi_{\mathrm{IVP}}'+2\chi_\infty\frac\mu{\rho^2-\mu}$ lies in $(0,1)$ on $[5R_1,\infty)$ (it is positive, and at most
the value for $\psi$, which is $<1$ by (a)) and equals the value for $\psi$ on $[r_0,5R_1]$. $\psi_{\mathrm{IVP}}\ge0$
as $\psi\ge0$ on $[r_0,5R_1]$ and $\psi_{\mathrm{IVP}}$ is non-decreasing after. $\square$

So $t_{\mathrm{IVP}} = t-C''$ for $|x|\ge R_3$: its level set $\Sigma^{\mathrm{IVP}} := t_{\mathrm{IVP}}^{-1}(0)$ is
asymptotically flat and ends at $I_0$, and $t_*$'s level sets end at $\mathscr I^+$.

### 3.4 Linearised metrics, and initial data

**Definition 3.8 ([Hin26] Definition 3.11).** For $b\in\mathcal B$ and $\dot b = (\dot\mu,\dot A)\in\mathbb
R\times\mathfrak{so}(4)$, $\dot g_b(\dot b) := \frac d{ds}g_{b+s\dot b}|_{s=0}$.

By Proposition 3.6, smoothly in $b$,
$$\dot g_b(\dot b)\in|x|^{-2}C^\infty(M;S^2T^*),\qquad\dot g_b(0,\dot A)\in|x|^{-3}C^\infty(M;S^2T^*).\tag{3.7}$$
(For the first: $\frac d{ds}$ of $g_{\mu+s\dot\mu}-\bar g\in|x|^{-2}C^\infty$, using that $\Phi_\mu$ depends smoothly on
$\mu$ and Lemma 3.5 (c) holds uniformly; for the second: $\frac d{ds}$ of $g_{(\mu,A+s\dot
A)}-g_\mu\in|x|^{-3}C^\infty$.)

**Lemma 3.9 ([Hin26] Lemma 3.13 and Remark 3.14 at n = 4).** Let $\gamma_b$, $k_b$ be the metric and second fundamental
form induced by $g_b$ on $\Sigma^{\mathrm{IVP}}$, identified with $X$ by $(t,x)\mapsto x$ (as [Hin26] Definition 3.12,
with the future unit normal). Then
$$\gamma_\mu = \Big(1+\frac\mu{|x|^2}\Big)d|x|^2+|x|^2\slashed g\quad\text{on }\{|x|\ge R_3\},\qquad
\gamma_b-\gamma_\mu\in|x|^{-3}C^\infty(X;S^2T^*X),\tag{3.8}$$
$$k_\mu,\ \partial_bk_b\in|x|^{-3}C^\infty(X;S^2T^*X),\qquad k_b-k_\mu\in|x|^{-4}C^\infty(X;S^2T^*X).\tag{3.9}$$

*Proof.* On $\{|x|\ge R_3\}$, $\Sigma^{\mathrm{IVP}} = \{t = C''\}$ and $dt = 0$ on it, so by (3.4) the induced metric
of $g_\mu$ is $\eta|_{dt = 0}+\mu|x|^{-2}d|x|^2$, which is (3.8)'s first formula; the second follows from (3.5)
restricted to $\{t = C''\}$ (restriction maps $|x|^{-j}C^\infty(M;S^2T^*)$ near $I_0$ into
$|x|^{-j}C^\infty(X;S^2T^*X)$, as $\{t = C''\}$ meets $M$'s boundary only in $I_0$, transversally). Near infinity
$\Sigma^{\mathrm{IVP}} = \{t = C''\}$, and as $g_b(\nu_b,\partial_j) = 0$, $k_b(\partial_i,\partial_j) =
g_b(\nabla_{\partial_i}\nu_b,\partial_j) = -g_b(\nu_b,\nabla_{\partial_i}\partial_j) =
-\nu_b^\lambda\Gamma(g_b)_{\lambda ij}$, $\Gamma_{\lambda ij} := \frac12(\partial_ig_{\lambda j}+\partial_jg_{\lambda
i}-\partial_\lambda g_{ij})$, $\nu_b$ the future unit normal. Since $g_b-\eta\in|x|^{-2}C^\infty$, the Christoffel
symbols $\Gamma(g_b)_{\lambda ij}$ in the coordinates $(t,x)$ are first derivatives $\partial_x$ of
$|x|^{-2}C^\infty(\bar X)$ (the coefficients are $t$-independent), hence in $|x|^{-3}C^\infty(\bar X)$, and
$\nu_b\in\partial_t+|x|^{-2}C^\infty$; so $k_b\in|x|^{-3}C^\infty$, and the same with $g_b-g_\mu\in|x|^{-3}C^\infty$
gives $k_b-k_\mu\in|x|^{-4}C^\infty$, and smoothness in $b$ gives the derivative. $\square$

The data class for the route's stability statement is then that of [Hin26] Remark 3.14 shifted by one order:
$\gamma_\mu$ modulo $O(|x|^{-2-\epsilon})$, $k_\mu$ modulo $O(|x|^{-3-\epsilon})$. Whether the route's own data lie in
it is a matter for Part VI.

## 4. Null coordinates near null infinity

On $\{|x|\ge3R_1\}$ let $r_* := |x|-\frac12T_\mu(|x|) = |x|+\frac{\sqrt\mu}2\log\frac{|x|-\sqrt\mu}{|x|+\sqrt\mu}$, so
$\frac{dr_*}{d|x|} = f^{-1}$, and ([Hin26] (3.29))
$$x^1 := t-|x| = t_0,\qquad x^0 := t+2r_*-|x| = t+|x|-T_\mu(|x|).\tag{4.1}$$

**Lemma 4.1 ([Hin26] (3.30)-(3.33) and Lemma 3.15 at n = 4).** On $\{|x|\ge3R_1\}$:
$$g_\mu = -f\,dx^0dx^1+|x|^2\slashed g,\qquad dx^0 = dt+\frac{2-f}f\,d|x|,\qquad dx^1 = dt-d|x|,\tag{4.2}$$
with $ab := \frac12(a\otimes b+b\otimes a)$; $dx^0,dx^1\in C^\infty(M;T^*)$ near $I_0\cup\mathscr I^+\cup\iota^+$;
$\partial_0|x| = \frac f2$, $\partial_1|x| = -\frac f2$; and
$$\partial_0 = \tfrac f2(\partial_t+\partial_{|x|})\in\rho_0\rho_I\rho_+\mathcal V_b(M),\qquad\partial_1 =
\tfrac f2\Big(\tfrac{2-f}f\partial_t-\partial_{|x|}\Big)\in\rho_0\rho_+\mathcal V_b(M).\tag{4.3}$$

*Proof.* With $c := \frac{2-f}f = \frac{|x|^2+\mu}{|x|^2-\mu} = 1-T_\mu'$, $dx^0 = dt+c\,d|x|$ by (4.1). Then
$-f(dt+c\,d|x|)(dt-d|x|) = -f\,dt^2-f(c-1)\,dt\,d|x|+fc\,d|x|^2$ with $f(c-1) = \frac{2\mu}{|x|^2}$ and $fc = 2-f$,
which is (3.4). $c-1 = \frac{2\mu}{|x|^2-\mu}\in|x|^{-2}C^\infty(\bar X)$ and $d|x| = \hat x\cdot dx$, so $dx^0,dx^1$
are smooth sections of $T^*$. Inverting $(dx^0,dx^1)$ on the $(t,|x|)$-plane, $d|x| = (1+c)^{-1}(dx^0-dx^1) = \frac
f2(dx^0-dx^1)$ (as $1+c = \frac2f$) and $dt = \frac f2(dx^0+c\,dx^1)$, which give $\partial_0|x|$, $\partial_1|x|$ and
the formulas for $\partial_0,\partial_1$ in (4.3). For the memberships let $u := t-|x|$, $v := t+|x|$, so
$\partial_t+\partial_{|x|} = 2\partial_v$ and $\partial_t-\partial_{|x|} = 2\partial_u$ at fixed $\omega$. Near
$\mathscr I^+\cap\iota^+$, $\rho_+ = (u+2)^{-1}$ and $\rho_I = \frac{2(u+2)}{v-u}$, and $|x|^{-1} = \rho_I\rho_+$; so
$\partial_v\rho_+ = 0$, $\partial_v\rho_I = -\frac{\rho_I}{v-u} = -\frac12\rho_I^2\rho_+$, and $\partial_v =
-\frac12\rho_I\rho_+\,\rho_I\partial_{\rho_I}\in\rho_I\rho_+\mathcal V_b$; $\partial_u\rho_+ = -\rho_+^2$,
$\partial_u\rho_I = \rho_I\rho_++\frac12\rho_I^2\rho_+$, and $\partial_u =
-\rho_+\,\rho_+\partial_{\rho_+}+\rho_+(1+\frac12\rho_I)\rho_I\partial_{\rho_I}\in\rho_+\mathcal V_b$. Near
$I_0\cap\mathscr I^+$, $\rho_0 = (2-u)^{-1}$, $\rho_I = \frac{2(2-u)}{v-u}$, and the same computation gives $\partial_v
= -\frac12\rho_0\rho_I\,\rho_I\partial_{\rho_I}\in\rho_0\rho_I\mathcal V_b$ and $\partial_u\in\rho_0\mathcal V_b$. In
the interiors of $I_0$ and $\iota^+$ both lie in $|x|^{-1}\mathcal V_b$, linear fields with constant coefficients being
$|x|^{-1}$ times b-vector fields there. As $\frac{2-f}f\partial_t-\partial_{|x|} =
2\partial_u+(c-1)(\partial_u+\partial_v)$ with $c-1\in|x|^{-2}C^\infty$, (4.3) follows; the dimension enters nowhere.
$\square$

Correspondingly ([Hin26] (3.34)-(3.37)), on $\{|x|>\mu^{1/2}\}$
$$T^* = \langle dx^0\rangle\oplus\langle dx^1\rangle\oplus|x|T^*\mathbb S^3,\tag{4.4}$$
$$S^2T^* = \langle(dx^0)^2\rangle\oplus\langle2dx^0dx^1\rangle\oplus(2dx^0\otimes_s|x|T^*\mathbb S^3)
\oplus\langle(dx^1)^2\rangle\oplus
(2dx^1\otimes_s|x|T^*\mathbb S^3)\oplus\langle|x|^2\slashed g\rangle\oplus|x|^2\ker\slashed{\mathrm{tr}},$$
and in this splitting $g_\mu = (0,-\frac f2,0,0,0,1,0)$. *Rescaled components* ([Hin26] Definition 3.16): with
$x^2,x^3,x^4$ local coordinates on $\mathbb S^3$ and $s(\mu_1,\dots,\mu_N) := \#\{j:\mu_j\in\{2,3,4\}\}$,
$T^{\bar\nu_1\dots\bar\nu_p}{}_{\bar\mu_1\dots\bar\mu_q} := |x|^{s(\nu)-s(\mu)}T^{\nu_1\dots\nu_p}{}_{\mu_1\dots\mu_q}$.
By Proposition 3.6, $(g_b)_{\bar\mu\bar\nu}-(g_\mu)_{\bar\mu\bar\nu}\in|x|^{-3}C^\infty(M)$, where the source has
$r^{-2}$.

## 5. Cut-off Lorentz boosts

Let $\mathcal S_1 := \{S_w:w\in\mathbb R^4\}$, $S_w(\omega) := w\cdot\omega$ on $\mathbb S^3$, the restrictions of
linear functions (the source's $\mathcal S_1$, three-dimensional there, is four-dimensional here). Let ([Hin26] (3.38))
$$\bar\omega(S_w) := t\,d(|x|S_w)-|x|S_w\,dt = t\,w\cdot dx-(w\cdot x)\,dt,\qquad X_w := \bar g^{-1}(\bar\omega(S_w),
\cdot) = t\,w\cdot\partial_x+(w\cdot x)\partial_t,$$
the generator of the Lorentz boosts in the direction $w$; $X_w$ is Killing for $\bar g$, so $\delta_{\bar
g}^*\bar\omega(S_w) = 0$. The time-$s$ flow of $X_w$ is the boost of rapidity $s|w|$: with $\hat w := w/|w|$, $t\mapsto
t\cosh(s|w|)+(x\cdot\hat w)\sinh(s|w|)$, $x\cdot\hat w\mapsto(x\cdot\hat w)\cosh(s|w|)+t\sinh(s|w|)$, the orthogonal
components fixed. The cut-offs $\chi^\flat_K,\chi_K,\chi^\sharp_K,\chi_{\mathrm{IVP}},\chi^\sharp_{\mathrm{IVP}}\in
C^\infty(M)$ are those of [Hin26] Definition 3.17 with $m_0$ replaced by $R_1$, made consistent (section 7, (K1)):
$\chi^\flat_K,\chi_K,\chi^\sharp_K$ supported in $\{t>50R_1\}$, $\chi^\flat_K = 1$ on $\{|x|<t/10,\ t>60R_1\}$,
$\mathrm{supp}\,\chi^\sharp_K\subset\{|x|<t/2\}$, $\chi_{\mathrm{IVP}} = 1$ on $\{t_{\mathrm{IVP}}>-|x|/10\}$,
$\mathrm{supp}\,\chi^\sharp_{\mathrm{IVP}}\subset\{t_{\mathrm{IVP}}>-|x|/2\}$, each later function equal to 1 on the
support of the earlier. In addition fix $\chi_r\in C^\infty(\mathbb R)$ equal to 0 on $(-\infty,5R_1]$ and to 1 on
$[6R_1,\infty)$.

**Lemma 5.1 ([Hin26] Lemma 3.18 at n = 4).** $V(S_w) := \frac12\chi_r(|x|)\chi^\sharp_{\mathrm{IVP}}(1-\chi^\flat_K)X_w$
is a b-vector field on $\overline{\mathbb R^{1+4}}$ near the support, tangent to $Y_+$; its lift to $M$ is a b-vector
field vanishing near $\Sigma^{\mathrm{past}}\cup K^+\cup\Sigma^{\mathrm{int}}$ and on $\{|x|\le5R_1\}$, tangent to every
boundary hypersurface. Hence $\phi_{S_w} := \exp(V(S_w))$ is a diffeomorphism of $M$ restricting to diffeomorphisms of
$I_0$, $\mathscr I^+$ and $\iota^+$, equal to the identity near $\Sigma^{\mathrm{past}}\cup
K^+\cup\Sigma^{\mathrm{int}}$ and on $\{|x|\le5R_1\}$, and $\phi_{S_w}^*$ maps $\rho_0^\alpha\rho_I^\beta\rho_+^\gamma
C^\infty(M;S^2T^*)$ to itself for all weights.

*Proof.* With $\rho = |x|^{-1}$, $v = t_0/|x|$, $\omega = \hat x$ (coordinates near $Y_+ = \{\rho = v = 0\}$): $X_w|x| =
tS_w$, $X_wt = |x|S_w$, $X_w\omega = \frac t{|x|}(w-(w\cdot\omega)\omega) = (1+v)\slashed\nabla S_w$, so $X_w\rho =
-\rho(1+v)S_w$ and $X_wv = S_w-\frac{t^2}{|x|^2}S_w = -S_wv(2+v)$:
$$X_w = -S_w(1+v)\rho\partial_\rho-S_w(2+v)v\partial_v+(1+v)\slashed\nabla S_w,\tag{5.1}$$
[Hin26] (3.40), a b-vector field tangent to $\{\rho = 0\}$ and $\{v = 0\}$, the dimension entering only through
$\slashed\nabla$ on $\mathbb S^3$. Away from $Y_+$, $X_w$ is linear with constant coefficients, hence a b-vector field
on the radial compactification, tangent to its boundary, and its lift to the blow-up at $Y_+$ is a b-vector field
([Hin26] Lemma 3.18's proof; the blow-up of a submanifold to which a b-vector field is tangent lifts it to a b-vector
field). The cut-off factor is smooth on $M$ and vanishes near $\Sigma^{\mathrm{past}}$ (as $\chi^\sharp_{\mathrm{IVP}} =
0$ for $t_{\mathrm{IVP}}\le-|x|/2$), near $K^+$ (as $1-\chi^\flat_K = 0$ on $\{|x|<t/10,\ t>60R_1\}$, a neighbourhood of
$K^+$ in $M$) and on $\{|x|\le5R_1\}$, which contains $\Sigma^{\mathrm{int}}$ (as $\chi_r = 0$ there). The factor
$\chi_r$ equals 1 near $I_0\cup\mathscr I^+\cup\iota^+$, so it changes nothing at infinity. A complete b-vector field
tangent to all boundary hypersurfaces has a flow by diffeomorphisms preserving each of them, and its pullback preserves
each weighted space, the defining functions being multiplied by smooth positive functions. $\square$

**Lemma 5.2 ([Hin26] Lemma 3.19 at n = 4).** Let $w\in\mathbb R^4$ be so small that every integral curve of $V(S_w)$
starting in $\mathrm{supp}(\chi_{\mathrm{IVP}}(1-\chi_K))$ stays, for times in $[0,1]$, in
$\{\chi_r\chi^\sharp_{\mathrm{IVP}}(1-\chi^\flat_K) = 1\}$ (a subset of $\{|x|\ge6R_1\}$), or in a fixed compact subset
of $M^\circ$; (5.3) concerns the former, the statement on the latter being smoothness only. Let $c := |w|$, so that
$$c^2 = \frac2{\pi^2}\|S_w\|^2_{L^2(\mathbb S^3)},\qquad a(\omega) := \Big(\cosh\frac c2+
\frac{S_w(\omega)}c\sinh\frac c2\Big)^{-1},\qquad h_{S_w} := \mu\big(a^4-1\big)\in C^\infty(\mathbb S^3).\tag{5.2}$$
Then for $b = (\mu,A)\in\mathcal B$,
$$\chi_{\mathrm{IVP}}(1-\chi_K)\Big(\phi_{S_w}^*g_b-\big(g_b+|x|^{-2}h_{S_w}(dx^1)^2\big)\Big)\in
\rho_0^2\rho_I^3\rho_+^2C^\infty(M;S^2T^*).\tag{5.3}$$

The source's (3.43)-(3.44) have $r^{-1}$, $2m(a^3-1)$, $\frac3{4\pi}$ and the remainder class $\rho_0\rho_I^2\rho_+$.

*Proof.* $\|S_w\|^2_{L^2(\mathbb S^3)} = c^2\int_{\mathbb S^3}(\hat w\cdot\omega)^2 = c^2\frac{|\mathbb S^3|}4 =
\frac{\pi^2}2c^2$ (`d215/chkboost.py`). On the set in question the flow of $V(S_w) = \frac12X_w$ for time 1 is the boost
$\Lambda$ of rapidity $\beta := \frac c2$ in the direction $\hat w$; so $\phi_{S_w}^* = \Lambda^*$ there. As
$\Lambda^*\bar g = \bar g$,
$$\Lambda^*g_b-g_b = \Lambda^*(g_b-g_\mu)-(g_b-g_\mu)+\Lambda^*(g_\mu-\bar g)-(g_\mu-\bar g).$$
$\Lambda$ is linear, commutes with dilations and, on the region (where $t\ge-|x|/2$ and $|x|\gtrsim t$), satisfies
$|\Lambda(t,x)|_x\ge c_1|x|$; so $\Lambda^*$ maps $|x|^{-3}C^\infty(M;S^2T^*)$ into itself there, and the first two
terms lie in $|x|^{-3}C^\infty\subset\rho_0^3\rho_I^3\rho_+^3C^\infty$. For the last two, $g_\mu-\bar g =
\mu|x|^{-2}(dt_0)^2$ on $\{|x|\ge3R_1\}$ (Proposition 3.6), $t_0 = x^1$. Write $t = |x|(1+v)$, $x = |x|\omega$. By
homogeneity, $t' := t\circ\Lambda = |x|L(v,\omega)$ and $|x'| := |x\circ\Lambda| = |x|G(v,\omega)$, with $L,G$ smooth
for bounded $v$, $G>0$ on the region, and $L(0,\omega) = G(0,\omega) = a(\omega)^{-1}$: at $v = 0$, $t'
= |x|(\cosh\beta+\cos\theta\sinh\beta)$, $\cos\theta := \omega\cdot\hat w = S_w/c$, and $|x'|^2
= |x|^2((\cos\theta\cosh\beta+\sinh\beta)^2+\sin^2\theta) = |x|^2(\cosh\beta+\cos\theta\sinh\beta)^2$. As $\Lambda$
preserves $t^2-|x|^2$,
$$t_0' := t'-|x'| = \frac{t^2-|x|^2}{t'+|x'|} = |x|K(v,\omega),\qquad K := \frac{v(2+v)}{L+G} = a(\omega)v\,(1+O(v)),$$
$L+G>0$ on the region (no point of it is mapped to the past light cone of the origin by a small boost). Using $|x|\,dv =
dt_0-v\,d|x|$,
$$dt_0' = K\,d|x|+|x|(\partial_vK\,dv+\partial_\omega K\,d\omega) = \partial_vK\,dt_0+(K-v\partial_vK)\,d|x|+
\partial_\omega K\cdot|x|d\omega,$$
with $\partial_vK = a+O(v)$, $K-v\partial_vK = O(v^2)$, $\partial_\omega K = O(v)$, and $d|x|$, $|x|d\omega$ smooth
sections of $T^*$. So $dt_0' = a\,dt_0+v\,\theta$ with $\theta\in C^\infty(T^*)$, and $|x'|^{-2} = |x|^{-2}G^{-2}
= |x|^{-2}(a^2+O(v))$. Hence
$$\Lambda^*\big(\mu|x|^{-2}(dt_0)^2\big)-\mu|x|^{-2}(dt_0)^2 = \mu|x|^{-2}(a^4-1)(dt_0)^2+
\mu|x|^{-2}v\,C^\infty(M;S^2T^*).$$
On the region $v$ is bounded (as $1-\chi_K$ vanishes near $K^+$), and $v\in\rho_IC^\infty$ near $\mathscr I^+$: $v =
\rho_I(1-2\rho_+)$ near $\mathscr I^+\cap\iota^+$, $v = -\rho_I(1-2\rho_0)$ near $I_0\cap\mathscr I^+$, $v = t_0\rho_I$
in the interior of $\mathscr I^+$; and $|x|^{-2}\in\rho_0^2\rho_I^2\rho_+^2C^\infty$. So the last term lies in
$\rho_0^2\rho_I^3\rho_+^2C^\infty$, which is (5.3) (away from $\mathscr I^+$, $\rho_I$ is bounded below and
$|x|^{-2}C^\infty\subset\rho_0^2\rho_+^2C^\infty$). $\square$

## 6. The gauge-fixed Einstein equation ([Hin26] section 4 at D = 5)

Throughout, $D := n+1 = 5$, $G_gh := h-\frac12g\,\mathrm{tr}_gh$, $\delta_g$ the divergence ($(\delta_gh)_\mu =
-\nabla^\kappa h_{\kappa\mu}$) and $\delta_g^*$ the symmetrised covariant derivative, $\iota_Vh := h(V,\cdot)$.

**Definition 6.1 ([Hin26] Definitions 4.1-4.2 at D = 5).** Let $c_\Upsilon\in|x|^{-1}C^\infty(X;T^*)$ be stationary with
$c_\Upsilon = |x|^{-1}dt$ for large $|x|$, $c_{\Upsilon,H}\in C_c^\infty(\{|x|<5R_1\};T^*)$ stationary,
$c_C\in|x|^{-1}C^\infty(X;T^*)$ stationary with $c_C = |x|^{-1}(dt-v_C\,d|x|)$ for large $|x|$, $v_C\in(0,1)$, and
$e_\Upsilon,\gamma_\Upsilon,\gamma_{\Upsilon,H},e_C,\gamma_C\in\mathbb R$. For a metric $g_0$,
$$E^\Upsilon_{g_0,\infty}h := -\gamma_\Upsilon\Big(2\iota_{g_0^{-1}c_\Upsilon}h-\tfrac23(1-
e_\Upsilon)\,c_\Upsilon\,\mathrm{tr}_{g_0}h\Big),\qquad
E^\Upsilon_{g_0,H}h := \gamma_{\Upsilon,H}\Big(2\iota_{g_0^{-1}c_{\Upsilon,H}}h-\tfrac23\,c_{\Upsilon,
H}\,\mathrm{tr}_{g_0}h\Big),\tag{6.1}$$
$E^\Upsilon_{g_0} := E^\Upsilon_{g_0,\infty}+E^\Upsilon_{g_0,H}$, $\delta_{g_0,E_\Upsilon} :=
\delta_{g_0}+E^\Upsilon_{g_0}$;
$$E^C_{g_0}\omega := \gamma_C\Big(2c_C\otimes_s\omega-\tfrac23(1-e_C)\,g_0\,\iota_{g_0^{-1}c_C}\omega\Big),\qquad
\delta^*_{g_0,E_C} := \delta^*_{g_0}+E^C_{g_0};\tag{6.2}$$
$$\Upsilon^0(g,g_0)_\mu :=
g_{\mu\nu}g^{\kappa\lambda}\big(\Gamma(g)^\nu_{\kappa\lambda}-\Gamma(g_0)^\nu_{\kappa\lambda}\big),\qquad
\Upsilon^{E_\Upsilon}(g,g_0) := \Upsilon^0(g,g_0)-E^\Upsilon_{g_0}G_{g_0}(g-g_0),\tag{6.3}$$
$$P(g,g_0) := \mathrm{Ric}(g)-\delta^*_{g_0,E_C}\Upsilon^{E_\Upsilon}(g,g_0),\qquad\Box^\Upsilon_{g,E_\Upsilon} :=
2\delta_{g,E_\Upsilon}G_g\delta_g^*,\qquad\Box^C_{g,E_C} := 2\delta_gG_g\delta^*_{g,E_C},\tag{6.4}$$
and $L_{g,g_0} := D_{(g,g_0)}P(\cdot,0)$, $L_g := L_{g,g}$.

$\Upsilon^0(g,g_0) = g\,g_0^{-1}\delta_gG_gg_0$ ([Hin26] (4.3)-(4.4)): $(\delta_gG_gg_0)^\nu =
-\nabla^\kappa(g_0)_\kappa{}^\nu+\frac12\nabla^\nu\mathrm{tr}_gg_0$, and in $g$-normal coordinates at a point, $\nabla =
\partial$ and both sides equal $g^{\kappa\lambda}(\Gamma(g_0)\dots)$ by the same computation as at $D = 4$; the identity
is the wave-map gauge identity, valid in every dimension.

**Lemma 6.2 (the trace weight).** At $D = 5$: $\mathrm{tr}_gG_gh = -\frac32\mathrm{tr}_gh$; $G_g$ is invertible,
$G_g^{-1}h = h-\frac13g\,\mathrm{tr}_gh$; and
$$E^\Upsilon_{g_0,\infty}G_{g_0}h = -\gamma_\Upsilon\big(2\iota_{g_0^{-1}c_\Upsilon}h-
e_\Upsilon c_\Upsilon\mathrm{tr}_{g_0}h\big),\quad E^\Upsilon_{g_0,H}G_{g_0}h = 2\gamma_{\Upsilon,H}\iota_{g_0^{-
1}c_{\Upsilon,H}}h,\quad
G_{g_0}E^C_{g_0}\omega = \gamma_C\big(2c_C\otimes_s\omega-e_C\,g_0\,\iota_{g_0^{-1}c_C}\omega\big).\tag{6.5}$$
These are the same expressions as the source's (4.1), (4.2) and (4.7) give at $D = 4$ with the trace weight 1.

*Proof.* $\mathrm{tr}_gg = 5$, so $\mathrm{tr}_gG_gh = \mathrm{tr}_gh-\frac52\mathrm{tr}_gh$;
$(I-\frac13g\,\mathrm{tr})(I-\frac12g\,\mathrm{tr}) = I-(\frac12+\frac13-\frac56)g\,\mathrm{tr} = I$. With $\iota_cG_gh
= \iota_ch-\frac12c\,\mathrm{tr}h$: $2\iota_cG_gh-\frac23(1-e)c\,\mathrm{tr}G_gh =
2\iota_ch-c\,\mathrm{tr}h+(1-e)c\,\mathrm{tr}h = 2\iota_ch-e\,c\,\mathrm{tr}h$, and with $e = 0$ in place of $1-e$
removed, $2\iota_ch-c\,\mathrm{tr}h+c\,\mathrm{tr}h = 2\iota_ch$. For $E^C$: $\mathrm{tr}_{g_0}E^C\omega =
\gamma_C\langle c,\omega\rangle(2-\frac{10}3(1-e_C))$, so $G_{g_0}E^C\omega = \gamma_C\big(2c\otimes_s\omega-g_0\langle
c,\omega\rangle(\frac23(1-e_C)+1-\frac53(1-e_C))\big) = \gamma_C(2c\otimes_s\omega-e_Cg_0\langle c,\omega\rangle)$. At
$D = 4$ with weight 1, $\mathrm{tr}G = -\mathrm{tr}$ and the same lines give the same right sides. $\square$

The operators that enter later parts, $\Box^\Upsilon = 2\delta_gG_g\delta^*_g+2E^\Upsilon G_g\delta^*_g$ and $\Box^C =
2\delta_gG_g\delta^*_g+2\delta_gG_gE^C$, contain $E^\Upsilon$ and $E^C$ only through $E^\Upsilon G$ and $GE^C$; so (6.5)
is why the weight is $\frac2{D-2}$: the modifications act as at $D = 4$, and their parameters $e,\gamma$ keep their
roles. This is the choice of the record (supplement 10.12 and 10.15).

**Lemma 6.3 ([Hin26] Lemma 4.4 at D = 5).** With $C(g,g_0)^\lambda_{\mu\nu} :=
\Gamma(g)^\lambda_{\mu\nu}-\Gamma(g_0)^\lambda_{\mu\nu}$, $C_{g,g_0}(\dot g)^\kappa :=
g^{\kappa\lambda}C(g,g_0)_{\lambda\mu\nu}\dot g^{\mu\nu}$ and $Y_{g,g_0}(\dot g)^\kappa := \Upsilon^0(g,g_0)^\lambda\dot
g^\kappa{}_\lambda$ (indices moved with $g$):
$$D^1|_{(g,g_0)}\Upsilon^0 = -\delta_gG_g-C_{g,g_0}+Y_{g,g_0},\qquad
D^1|_{(g,g_0)}\Upsilon^{E_\Upsilon} = -\delta_gG_g-C_{g,g_0}+Y_{g,g_0}-E^\Upsilon_{g_0}G_{g_0};\tag{6.6}$$
$$D_g\mathrm{Ric} = \tfrac12\Box_g-\delta_g^*\delta_gG_g+R_g,\qquad
(\Box_g\dot g)_{\mu\nu} := -g^{\kappa\lambda}\dot g_{\mu\nu;\kappa\lambda},\tag{6.7}$$
with $R_g$ the zeroth order term of [Hin26] (4.12), $(R_g\dot g)_{\lambda\nu} =
\mathrm{Riem}(g)^\rho{}_{\lambda\nu}{}^\kappa\dot g_{\rho\kappa}+\frac12(\mathrm{Ric}(g)^\rho{}_\nu\dot
g_{\lambda\rho}+\mathrm{Ric}(g)^\rho{}_\lambda\dot g_{\nu\rho})$ in the source's curvature convention; and
$$L_{g,g_0} = \tfrac12\Box_g+E^C_{g_0}\delta_gG_g+(\delta^*_{g_0}-\delta^*_g)\delta_gG_g+R_g+
\delta^*_{g_0,E_C}\big(C_{g,g_0}-Y_{g,g_0}+E^\Upsilon_{g_0}G_{g_0}\big),\qquad L_g = D_g\mathrm{Ric}+
\delta^*_{g,E_C}\delta_{g,E_\Upsilon}G_g.\tag{6.8}$$

*Proof.* The source's proof (p. 83) is an index computation in which the dimension does not appear, and it is reproduced
here. (6.6): from (6.3), $D^1\Upsilon^0(\dot g)^\mu = \dot g^{\mu\nu}\Upsilon^0_\nu-g^{\mu\nu}\dot
g^{\kappa\lambda}C_{\nu\kappa\lambda}+\frac12g^{\mu\nu}g^{\kappa\lambda}(\dot g_{\kappa\nu;\lambda}+\dot
g_{\lambda\nu;\kappa}-\dot g_{\kappa\lambda;\nu})$, using $D\Gamma(\dot g)^\nu_{\kappa\lambda} = \frac12(\dot
g^\nu{}_{\kappa;\lambda}+\dot g^\nu{}_{\lambda;\kappa}-\dot g_{\kappa\lambda}{}^{;\nu})$ and $Dg^{\kappa\lambda} = -\dot
g^{\kappa\lambda}$; the first term is $Y$, the second $-C$, and the third is $\dot
g^{\mu\kappa}{}_{;\kappa}-\frac12\nabla^\mu\mathrm{tr}\dot g = -(\delta_gG_g\dot g)^\mu$, the coefficient $\frac12$
being that of $G_g$, the same in every dimension. The last term of (6.3) is linear in $g-g_0$ with $g_0$ fixed, with
linearisation $-E^\Upsilon_{g_0}G_{g_0}$. (6.7): $D\mathrm{Riem}(\dot g)^\kappa{}_{\lambda\mu\nu} = (D\Gamma(\dot
g)^\kappa_{\lambda\nu})_{;\mu}-(D\Gamma(\dot g)^\kappa_{\lambda\mu})_{;\nu}$; contracting, $2D\mathrm{Ric}(\dot
g)_{\lambda\nu} = (\dot g_\lambda{}^\kappa{}_{;\nu\kappa}-\dot g_\lambda{}^\kappa{}_{;\kappa\nu})-\dot
g_{\lambda\nu;\kappa}{}^\kappa+\dot g_\nu{}^\kappa{}_{;\lambda\kappa}-\dot g^\kappa{}_{\kappa;\lambda\nu}+\dot
g_{\lambda\kappa}{}^{;\kappa}{}_\nu$. The commutator term is a curvature term (the source's (4.14)); the second term is
$(\Box_g\dot g)_{\lambda\nu}$; and $-2\delta_g^*\delta_gG_g\dot g$ differs from the remaining terms by another
commutator, a curvature term; the two curvature terms sum to $2R_g\dot g$. Each step is the Ricci identity, valid in
every dimension. (6.8): $L_{g,g_0} = D_g\mathrm{Ric}-\delta^*_{g_0,E_C}D^1\Upsilon^{E_\Upsilon}$, and substituting
(6.6)-(6.7) and $\delta^*_{g_0,E_C}-\delta^*_g = (\delta^*_{g_0}-\delta^*_g)+E^C_{g_0}$ gives the first formula; at $g_0
= g$, $C_{g,g} = 0 = Y_{g,g}$ and the second follows. $\square$

## 7. Findings, and the sources

### 7.1 What is not carried, and findings

The Boyer-Lindquist apparatus of [Hin26] section 3.2 ((3.9)-(3.18), (3.22), (3.25)-(3.26)) is not carried: Kerr-Schild
coordinates and the time change (3.3) replace it, which five dimensions allow and four do not (Lemma 3.5). Where the
source constructs $\tilde T$ with $\tilde T = C'-Cr^{-1}$ by an estimate, (3.6) gives it explicitly with $C = 8\mu_0$,
and Lemma 3.3 (e) reduces every causal statement to one inequality. The proof of Lemma 5.2 uses the exact boost and
homogeneity in place of the source's expansion (3.45)-(3.49) of the cut-off flow; at $n = 4$ the expansion has no
$O(\rho)$ terms, the coordinate $t_0 = t-|x|$ of the compactification being the Minkowski retarded time.

(K1) *Definition 3.17 and Lemma 3.18.* Definition 3.17 asks $\chi^\flat_K$ to be supported in $\{t>50m_0\}$ and equal to
1 on $\{r<t/10\}$; on $\{m_0\le r<t/10,\ 10m_0<t\le50m_0\}$, which meets $M$, the two conflict. And Lemma 3.18 asserts
that the lift of $V(S)$ vanishes for $r\le5m_0$; with the cut-offs of Definition 3.17 this needs
$\chi^\sharp_{\mathrm{IVP}}(1-\chi^\flat_K) = 0$ on $\{r\le5m_0\}$, which fails at $t\le50m_0$ where $\chi^\flat_K = 0$
and $t_{\mathrm{IVP}}>-r/2$. Repaired here by asking $\chi^\flat_K = 1$ only on $\{|x|<t/10,\ t>60R_1\}$ and by the
radial factor $\chi_r$ in $V(S_w)$; both change nothing near $I_0\cup\mathscr I^+\cup\iota^+\cup K^+$, so Lemma 3.19 and
its uses are unaffected.

No other statement of [Hin26] sections 3-4 is found false. Two remarks on the record's reading: the extraction of (4.4)
places the free index as an upper index on both sides, and (6.3) writes $\Upsilon^0$ as a 1-form, which is what (4.3)
defines; and the source's $\mathcal S_1$ is the space of restrictions of linear functions to the sphere (extracted as
"$S\in S^1$").

### 7.2 Sources

[Hin26] P. Hintz, *Nonlinear stability of subextremal Kerr black holes*, sections 3-4 (pp. 68-83), read in the record's
text extraction (digest `d215/sec34.md`; Lemma 4.4 and its proof read at source).

[ER08] R. Emparan and H. S. Reall, *Black holes in higher dimensions*, arXiv:0801.3471v2: pp. 10, 14, 16, 19 ((14)-(16),
(31)-(34), (42)-(44), section 4.3), READ in supplement section 10.36, for the Myers-Perry family in Kerr-Schild form.
[MP86] R. C. Myers and M. J. Perry, *Black holes in higher dimensional space-times*, Ann. Phys. 172 (1986): the family,
as [ER08] presents it; not read.

Supplement sections 10.12, 10.15 (the trace weight), 10.33 and 10.36 (the family computed at points) are cited for the
record's choices and computations; `d215/chk3b.py`, `chkboost.py` and `chkric.py` are the symbolic checks of Lemmas 3.1,
3.3, 3.5, 5.2 and Proposition 3.4 at $A = 0$.
