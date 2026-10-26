# Part III.F$'$. Indicial roots and tf-admissibility of the linearised operator, at n = 4 ([Hin26] sections 8.2-8.3)

*Status.* Written (D230). This part proves, at spatial dimension $n = 4$, what [Hin26] sections 8.2-8.3 establish (pp.
149-153): the indicial roots of the zero energy operator of the linearised gauge-fixed Einstein operator $L_b$ (his
Lemma 8.4, with (8.13)), that the indicial solutions at $\lambda = 0$ satisfy the linearised gauge condition (his Lemma
8.5), the tf-admissibility of $L_b$ (his Proposition 8.6) and the inversion of its transition face normal operator on
b-Sobolev spaces (his Corollary 8.7). Notation is that of Part III.F; the types and degrees are those of III.A$'$
(2.9)-(2.10), indicial roots by type are those of III.A$'$ Definition 2.2, and $\mathrm{spec}_{\mathrm b}$ is the set of
all indicial roots. The facts about the constraint propagation operator that Part IV must deliver are collected in
section 1; where the source computes with Mathematica, the computation is `lin5.py`'s, with $l$ and every parameter
symbolic, and the facts proved here by hand are checked by `linroots5.py` R1-R3.

## 1. The setting

$L_b = D_{g_b}\mathrm{Ric}+\delta^*_{g_b,E^C}\delta_{g_b,E^\Upsilon}G_{g_b}$ (III.F section 1), with
$\delta_E := \delta+E$, $\delta^*_E := \delta^*+E$, and on Minkowski space its model $\bar L$, with
$2\bar L = \bar\Box+2\bar E^C\bar\delta\bar G+2\bar\delta^*_{\bar E^C}\bar E^\Upsilon\bar G$;
$\bar\Box^\Upsilon := 2\bar\delta_{\bar E^\Upsilon}\bar G\bar\delta^*$ and
$\bar\Box^C := 2\bar\delta\bar G\bar\delta^*_{\bar E^C}$ are the models of III.D and III.E. With the trace weight
$m = \frac23$, $\bar E^\Upsilon h = -\gamma_\Upsilon(2\iota_{\bar c_\Upsilon^\sharp}h-m(1-e_\Upsilon)\bar
c_\Upsilon\mathrm{tr}\,h)$, $\bar c_\Upsilon = r^{-1}d\bar t$, and
$\bar E^C\omega = \gamma_C(2\bar c_C\otimes_s\omega-m(1-e_C)\bar g\langle\bar c_C,\omega\rangle)$,
$\bar c_C = r^{-1}(d\bar t-v_C\,dr)$ (III.B (6.5), III.E Theorem 1.1); so $\bar E^\Upsilon\bar Gh =
-\gamma_\Upsilon(2\iota_{\bar c_\Upsilon^\sharp}h-e_\Upsilon\bar c_\Upsilon\mathrm{tr}\,h)$. By III.F Lemma 2.1 (3) the
indicial roots of $\widehat{L_b}(0)$ are those of $\widehat{\bar L}(0)$, which is dilation homogeneous and equal to
$\rho^2$ times its normal operator; likewise for $\Box^\Upsilon_b$ (III.D Lemma 2.1 (3)) and $\Box^C_b$ (III.E section
1). All three models commute with the rotations $\mathrm{SO}(4)$ of the spatial factor.

*Parameters.* $e_\Upsilon>0$ and $\gamma_\Upsilon>0$ are small, with $z := 4e_\Upsilon\gamma_\Upsilon^2\in(0,\frac12]$,
the parameter of III.D Lemma 4.1; $v_C$, $e_C$, $c_C$ and $\gamma_C$ are those of III.E Theorem 1.1, with $C_0 = 100$
(III.F section 1). Part IV fixes the constraint damping parameters first; $\gamma_\Upsilon$ is then taken small, as in
the source ("keeping the other parameters and all 1-forms fixed").

*The constraint propagation operator.* The facts about $\Box^C_b$ used below are:

(C1) (III.E Theorem 1.1 (3), with its count by type; it needs $\gamma_C$ large relative to $e_C^{-1}$, the theorem's
parenthesis recording that the finite scalar roots fall below 2 when $\gamma_C^{-1}>e_C$.) Every indicial root of
$\Box^C_b$ has real part $\ge2$ or $<-C_0$; the only one with real part 2 is $\lambda = 2$, a simple root of scalar
types 0 and 1. At scalar type 0 two roots lie on each side, written $\lambda^C_{\mathrm s0,\ll,1}$,
$\lambda^C_{\mathrm s0,\ll,2}$ (real parts $<-C_0$) and $2$, $\lambda^C_{\mathrm s0,+}$; at scalar type 1 three,
$\lambda^C_{\mathrm s1,\ll,j}$ ($j = 1,2,3$) and $2$, $\lambda^C_{\mathrm s1,+,1}$, $\lambda^C_{\mathrm s1,+,2}$; at
scalar type $l\ge2$ three, $\lambda^C_{\mathrm sl,\ll,j}$ and $\lambda^C_{\mathrm sl,+,j}$; at vector type $l\ge1$ one,
$\lambda^C_{\mathrm vl,\ll}$ and $\lambda^C_{\mathrm vl,+}$.

(C2) The indicial roots of $\Box^C_b$ are simple.

(C3) At scalar type $l$ no indicial root of $\Box^C_b$ lies in $\{1-l,3-l,l+3,l+5\}\setminus\{2\}$; at vector type
$l\ge2$ none lies in $\{1-l,2-l,l+3,l+4\}$.

(C4) Every indicial root of $\Box^C_b$ whose real part is an integer in $[3,51]$ is real.

(C1)-(C4) are III.E Theorem 1.1 (3) as amended in D231: (C1) with the count by type that the source's Lemma 8.4 reads
from his (7.8), and (C2)-(C4), which the theorem did not state before (finding (F$'$2)). Part IV must deliver all four.
At the record's parameter point $(v_C,e_C,\gamma_C) = (\frac12,\frac1{102400},10^6)$ they are computed: (C1) by
`damping5.py` U4 (the lower scalar roots below $-100$ at every $l$) and `lin5.py` E5 ($l\le12$); (C2) and (C3) for every
$l\ge2$ exactly, by Sturm sequences (`eind5.py` E1), and for $l\le12$ numerically (`lin5.py` E5); (C4) by `eind5.py` E2,
a numerical scan over $l<10^4$ with an exact certificate beyond.

## 2. The indicial roots ([Hin26] Lemmas 8.4-8.5 at n = 4)

For a type and degree let $N_L(\lambda)$, $N_\Upsilon(\lambda)$ and $N_C(\lambda)$ be the type's indicial matrices of
$\rho^{-2}\widehat{2\bar L}(0)$, $\rho^{-2}\widehat{\bar\Box^\Upsilon}(0)$ and $\rho^{-2}\widehat{\bar\Box^C}(0)$, in
the bases of III.A$'$ (2.9)-(2.10): of sizes $k = 4,6,7,2,3,1$ for $N_L$ at s0, s1, sl ($l\ge2$), v1, vl ($l\ge2$), tl
($l\ge2$), and $2,3,3,1,1$ for $N_\Upsilon$ and $N_C$ at s0, s1, sl, v1, vl. Each is $-\lambda^2\mathrm{Id}$ plus lower
powers of $\lambda$, so its determinant has degree $2k$.

**Lemma 2.1 (the factorisation).** For each type and degree, with $c\ne0$ a number,
$$\det N_L(\lambda) = c\,(\lambda+l)(\lambda-l-2)\,
\frac{\det N_\Upsilon(\lambda-1)\,\det N_C(\lambda+1)}{D(\lambda)},\qquad
D(\lambda) = \begin{cases}(\lambda-1)^2&\mathrm{s0},\ \mathrm{s1},\\ \lambda(\lambda-2)&\mathrm{v1},\\
1&\mathrm{sl},\ \mathrm{vl},\ l\ge2,\end{cases}\tag{2.1}$$
and at tensor type $l\ge2$, $\det N_L(\lambda) = c\,(\lambda+l)(\lambda-l-2)$.

*Proof.* Computed, exact (`lin5.py` E2, with $l$, $\gamma_\Upsilon$, $e_\Upsilon$, $\gamma_C$, $e_C$, $v_C$ symbolic; E1
checks that the type spaces are invariant and that the operator is [Hin26] (8.5); the control, the four-dimensional
factor $(\lambda+l)(\lambda-l-1)$, fails). $\square$

The factors have a structural reason, which is the source's discussion and is not used as a proof. On Minkowski space
$D\mathrm{Ric}\circ\bar\delta^* = 0$, so $\bar L\bar\delta^* = \frac12\bar\delta^*_{\bar E^C}\bar\Box^\Upsilon$: the
symmetric gradient of an indicial solution of $\bar\Box^\Upsilon$ at $\lambda-1$ is one of $\bar L$ at $\lambda$, unless
it vanishes, which happens exactly for the Killing 1-forms (translations at $\lambda-1 = 0$, rotations at
$\lambda-1 = -1$). The linearised second Bianchi identity $\bar\delta\bar GD\mathrm{Ric} = 0$ gives
$\bar\delta\bar G(2\bar L) = \bar\Box^C\bar\delta_{\bar E^\Upsilon}\bar G$, the dual relation, which shifts the roots of
$\bar\Box^C$ by $-1$. The factor $(\lambda+l)(\lambda-l-2)$ carries the gauge-invariant roots $-l$ and $l+N-2$, $N = 4$;
and $D$ removes the roots that the two relations give twice: $\bar\Box^\Upsilon$'s Killing root and $\bar\Box^C$'s root
2 at s0 and s1, and at v1 the rotations ($\lambda-1 = -1$) and $\bar\Box^C$'s root 3 ($\lambda+1 = 3$, Lemma 2.2).

**Lemma 2.2 (vector type 1 of $\Box^C$).** $N_C(\lambda) = -(\lambda-3)(\lambda+1+2\gamma_Cv_C)$ at vector type 1. So
the roots are $3$ and $-1-2\gamma_Cv_C$.

*Proof.* A vector type 1 1-form of degree 0 is $\rho V$, $V = (Wx)\cdot dx$ with $W\in\mathfrak{so}(4)$, a Killing
1-form ($\bar\delta^*V = 0$), tangential and divergence free, with $V(\partial_r) = 0$. For $f = r^{-\lambda-1}$,
$\langle\bar c_C,V\rangle = 0$ and $\mathrm{tr}(k\otimes_sV) = \langle k,V\rangle = 0$ for
$k\in\mathrm{span}(d\bar t,dr)$, so $\bar\delta^*_{\bar E^C}(fV) = (df+2\gamma_Cf\bar c_C)\otimes_sV =
(F_r\,dr+F_t\,d\bar t)\otimes_sV$, with $F_r = f'-2\gamma_Cv_Cf/r = -(\lambda+1+2\gamma_Cv_C)r^{-\lambda-2}$, and
$\bar G$ is the identity on it. For a function $F(r)$ one computes in Cartesian coordinates
$\bar\delta(F\,d\bar t\otimes_sV) = 0$ and $\bar\delta(F\,dr\otimes_sV) = -\frac12(F'+5F/r)V$ (from
$\partial_i(Fx_i/r) = F'+3F/r$, $(x_i/r)\partial_iV_j = V_j/r$, $x\cdot V = 0$ and
$\mathrm{div}\,V = \mathrm{tr}\,W = 0$). So
$\bar\Box^C(fV) = -(F_r'+5F_r/r)V = -(\lambda+1+2\gamma_Cv_C)(\lambda-3)r^{-2}fV$. (*Computed:* `linroots5.py` R1,
$\lambda$ symbolic; control: $\lambda-2$ in place of $\lambda-3$.) $\square$

**Proposition 2.3 ([Hin26] Lemma 8.4 at n = 4).** Assume $z\in(0,\frac12]$ and (C1). The indicial roots of
$\widehat{L_b}(0)$, in the notation of III.D Lemma 4.1 and (C1), are:

s0: $\lambda^C_{\mathrm s0,\ll,1}-1$, $\lambda^C_{\mathrm s0,\ll,2}-1$, $2-\lambda^\Upsilon_{\mathrm s0,2}$, $0$; $2$,
$1+\lambda^\Upsilon_{\mathrm s0,2}$, $\lambda^C_{\mathrm s0,+}-1$, $4$;

s1: $\lambda^C_{\mathrm s1,\ll,j}-1$ ($j = 1,2,3$), $2-\lambda^\Upsilon_{\mathrm s1,3}$,
$2-\lambda^\Upsilon_{\mathrm s1,2}$, $-1$; $3$, $1+\lambda^\Upsilon_{\mathrm s1,2}$,
$1+\lambda^\Upsilon_{\mathrm s1,3}$, $5$, $\lambda^C_{\mathrm s1,+,1}-1$, $\lambda^C_{\mathrm s1,+,2}-1$;

sl, $l\ge2$: $\lambda^C_{\mathrm sl,\ll,j}-1$ ($j = 1,2,3$), $-l$, $2-\lambda^\Upsilon_{\mathrm sl,l+2}$,
$2-\lambda^\Upsilon_{\mathrm sl,l+1}$, $2-l$; $l+2$, $1+\lambda^\Upsilon_{\mathrm sl,l+1}$,
$1+\lambda^\Upsilon_{\mathrm sl,l+2}$, $l+4$, $\lambda^C_{\mathrm sl,+,j}-1$ ($j = 1,2,3$);

v1: $-2-2\gamma_Cv_C$, $-1$; $3$, $4$;

vl, $l\ge2$: $\lambda^C_{\mathrm vl,\ll}-1$, $-l$, $1-l$; $l+2$, $l+3$, $\lambda^C_{\mathrm vl,+}-1$;

tl, $l\ge2$: $-l$; $l+2$.

(a) No root has real part in $(0,1]$. (b) At each type and degree, $k$ roots (with multiplicity) have real part $\le0$
and $k$ have real part $>1$: those before and after the semicolon. (c) $0$ is a root only at scalar types 0 and 2,
simple there, with the indicial solutions of Lemma 2.5. (d) The roots with real part $\le0$ that come from $\Box^C$,
written with superscript $C$, have real part $<-C_0-1 = -101$. (e) If (C2)-(C3) hold, there is a countable set
$Z_{\mathrm{exc}}\subset(0,\frac12]$, determined by the roots of $\Box^C_b$, such that for $z\notin Z_{\mathrm{exc}}$
every root is simple. (f) If (C4) holds, then for every $R$ only finitely many roots have $|\lambda|\le R$, and no
non-integer root with $|\lambda|\le50$ has integer real part; so there is $\epsilon_{\mathrm{ind}}\in(0,1]$ with
$$d(\mathrm{Re}\,\lambda,\mathbb Z)\ge\epsilon_{\mathrm{ind}}\quad
\text{for every non-integer root }\lambda\text{ with }|\lambda|\le50,\tag{2.2}$$
the source's (8.13), and $(0,\epsilon_{\mathrm{ind}}]\subset(0,1]$ lies in the indicial gap. The number is small at the
record's parameter point: the roots $\lambda^C_{\cdot,+}-1$ lie just above 1 there, the lowest at scalar type 2,
$1+2.93\times10^{-6}$ (`../N1STAR-PROOF.md` 10.34 (iv)), so $\epsilon_{\mathrm{ind}}<3\times10^{-6}$ there. The gap
$(0,1]$ of (a) is exact, and no later part may read $\epsilon_{\mathrm{ind}}$ as a number of order one.

*Proof.* *The list.* By Lemma 2.1 the roots of each type are, with multiplicity, $-l$ and $l+2$, the roots of
$\Box^\Upsilon$ plus 1, the roots of $\Box^C$ minus 1, less the roots of $D$. III.D Lemma 4.1 gives those of
$\Box^\Upsilon$: s0: $1-\lambda^\Upsilon_{\mathrm s0,2}$, $0$, $\lambda^\Upsilon_{\mathrm s0,2}$, $3$; sl ($l\ge1$):
$1-\lambda^\Upsilon_{\mathrm sl,l+2}$, $1-\lambda^\Upsilon_{\mathrm sl,l+1}$, $1-l$,
$\lambda^\Upsilon_{\mathrm sl,l+1}$, $\lambda^\Upsilon_{\mathrm sl,l+2}$, $l+3$; vl: $-l$, $l+2$. (C1) and Lemma 2.2
give those of $\Box^C$. At s0 and s1, $(\lambda-1)^2$ divides the numerator of (2.1) exactly: $\lambda = 1$ is the
simple root $0$ of $\Box^\Upsilon$ plus 1 (at s0 the entry $0$ of the list, at s1 the entry $1-l$) (simple by III.D
Lemma 4.1) and the simple root $2$ of $\Box^C$ minus 1 (C1), and no other factor vanishes at 1 ($\lambda(\lambda-2)$ and
$(\lambda+1)(\lambda-3)$ do not, nor do the roots of either operator other than these two, by the bounds below). At v1,
$\lambda(\lambda-2)$ divides it exactly: $0$ is $\Box^\Upsilon$'s root $-1$ plus 1, and $2$ is $\Box^C$'s root $3$ minus
1 (Lemma 2.2), each simple, and $(\lambda+1)(\lambda-3)$, $\Box^\Upsilon$'s other root $3$ plus 1 and $\Box^C$'s other
root $-1-2\gamma_Cv_C$ minus 1 avoid $0$ and $2$. What remains is the list.

*Bounds.* By III.D (4.2), for $0<z\le\frac12$: $\lambda^\Upsilon_{\mathrm s0,2}\in(2,2+\frac z3]$,
$\lambda^\Upsilon_{\mathrm sl,l+j}\in(l+j,l+j+\frac14)$; so $2-\lambda^\Upsilon_{\mathrm s0,2}\in[-\frac z3,0)$,
$2-\lambda^\Upsilon_{\mathrm sl,l+j}\in(2-l-j-\frac14,2-l-j)$, $1+\lambda^\Upsilon_{\mathrm s0,2}\in(3,3+\frac z3]$ and
$1+\lambda^\Upsilon_{\mathrm sl,l+j}\in(l+j+1,l+j+\frac54)$. By (C1) the roots $\lambda^C_{\cdot,\ll}-1$ have real part
$<-C_0-1$ and the roots $\lambda^C_{\cdot,+}-1$ real part $>1$. *(a), (b), (d)* are read off: before the semicolon every
real part is $\le0$, after it every real part is $>1$ (the integers are $\ge2$), and the counts are $4,6,7,2,3,1$. *(c)*
Before the semicolon, $0$ occurs only as the root $0$ at s0 and as $2-l$ at $l = 2$; every other entry there is $<0$ (as
$z>0$, $2-\lambda^\Upsilon_{\mathrm s0,2}<0$ and $2-\lambda^\Upsilon_{\mathrm s1,2}<0$). So $0$ is a simple root at s0
and at s2, and at no other type.

*(e) Simplicity.* Within the roots that do not come from $\Box^C$ the entries of each type are distinct by the bounds:
they lie in pairwise disjoint intervals, for instance at sl, $-l-\frac14<2-\lambda^\Upsilon_{\mathrm
sl,l+2}<-l<1-l-\frac14<2-\lambda^\Upsilon_{\mathrm sl,l+1}<1-l<2-l$, and on the other side
$l+2<1+\lambda^\Upsilon_{\mathrm sl,l+1}<l+\frac94<l+3<1+\lambda^\Upsilon_{\mathrm sl,l+2}<l+\frac{13}4<l+4$ (at $z = 0$
the first and third pairs would meet, which is why $z>0$ is assumed). The roots from $\Box^C$ are distinct among
themselves by (C2), and at v1 the four are distinct as $\gamma_Cv_C>0$. A root from $\Box^C$ equals an integer entry of
its type exactly when $\Box^C$ has a root at that integer plus 1: at scalar type $l$ the integer entries are $-l$,
$2-l$, $l+2$, $l+4$ (with $0$, $2$, $4$ at s0 and $-1$, $3$, $5$ at s1), so these coincidences are the points of (C3)
(the root $2$ of $\Box^C$ at s0 and s1 being the one $D$ removes); at vector type $l\ge2$ they are $-l$, $1-l$, $l+2$,
$l+3$, and (C3) excludes them likewise. The remaining coincidences are between a real root $\mu$ of $\Box^C$ and
$\lambda^\Upsilon+2$ or $3-\lambda^\Upsilon$, for a root $\lambda^\Upsilon = \lambda^\Upsilon_{\mathrm s0,2}$ or
$\lambda^\Upsilon_{\mathrm sl,l+j}$ of the same type and degree. Each $\lambda^\Upsilon_{\cdot}$ is a strictly
increasing function of $z$: $\lambda^\Upsilon_{\mathrm s0,2} = \frac12+(\frac94+z)^{1/2}$; and
$\lambda^\Upsilon_{\mathrm sl,l+j} = \frac12+(\frac14+s_{l,j})^{1/2}$ with $s_{l,1}<s_{l,2}$ the roots of
$Q_l(s) = s^2-(2+2\kappa+z)s+\kappa(\kappa+1)+z\kappa$, $\kappa = l(l+2)$ (III.D Lemma 4.1), where
$Q_l(\kappa) = -\kappa<0$ puts $\kappa$ strictly between the two roots, so that
$\partial_zs_{l,j} = (s_{l,j}-\kappa)/\partial_sQ_l(s_{l,j})>0$ for both (numerator and denominator have the same sign).
The roots of $\Box^C_b$ do not depend on $z$ (its parameters are fixed first), and there are countably many of them, by
type and degree; so each coincidence happens at at most one $z$, and $Z_{\mathrm{exc}}$, the set of those $z$, is
countable.

*(f)* By Lemma 2.4 below, with the strip $|\mathrm{Re}\,\lambda|\le R$, only finitely many isotypic components carry
roots with $|\lambda|\le R$, each finitely many. The non-integer roots with $|\lambda|\le50$ are those from
$\Box^\Upsilon$, which are real and lie in the open intervals of the bounds above, so their real parts are not integers,
and those $\lambda^C_{\cdot,+}-1$ that are not integers (by (d) the roots $\lambda^C_{\cdot,\ll}-1$ have
$|\lambda|>101$); a non-integer one with integer real part $n$, $2\le n\le50$, would make $\lambda^C_{\cdot,+}$ non-real
with real part $n+1\in[3,51]$, against (C4). The minimum of $d(\mathrm{Re}\,\lambda,\mathbb Z)$ over this finite set is
positive, and $\epsilon_{\mathrm{ind}}$ is any number in $(0,1]$ not exceeding it. $\square$

**Lemma 2.4 (roots in a strip, uniformly).** Let $\mathcal T$ be a compact parameter space and
$I_\tau(\lambda) = -\lambda^2+a_\tau\lambda+\Delta_{\mathbb S^3}+V_\tau+b_\tau$, $\tau\in\mathcal T$, indicial families
of the form of I.C Lemma 2.4 on $\mathbb C^N$-valued functions on $\mathbb S^3$ (the Cartesian frame of $T^*$ or
$S^2T^*$ of $\mathbb R^{1+4}$), with coefficients continuous in $\tau$ and commuting with the action of $\mathrm{SO}(4)$
that rotates both the base and the Cartesian components. For an irreducible representation $\pi$ let $W_\pi$ be the
$\pi$-isotypic subspace, finite dimensional, and $d(\pi)$ the least $d$ with
$W_\pi\cap(\mathcal H_d\otimes\mathbb C^N)\ne0$. Then for every $X>0$ there is $d_0$ such that for all
$\tau\in\mathcal T$, all $\pi$ with $d(\pi)\ge d_0$ and all $\lambda$ with $|\mathrm{Re}\,\lambda|\le X$,
$I_\tau(\lambda)$ is invertible on $W_\pi$. On each $W_\pi$, $\det(I_\tau(\lambda)|_{W_\pi})$ is a polynomial of degree
$2\dim W_\pi$ with leading coefficient $(-1)^{\dim W_\pi}$, so its roots, with multiplicity, depend continuously on
$\tau$.

*Proof.* $\mathcal H_d\otimes\mathbb C^N$ is invariant under the action (the rotation of components is by constant
matrices), and $\Delta = \kappa_d := d(d+2)$ on it. The representation on $\mathbb C^N$ has irreducible constituents of
highest weights $(a,b)$ with $a+b\le2$ (for $S^2(\mathbb R\oplus\mathbb R^4)$, $\mathbb R^4 = (\frac12,\frac12)$), and
$\mathcal H_d = (\frac d2,\frac d2)$; by the Clebsch-Gordan rule for $\mathrm{SU}(2)\times\mathrm{SU}(2)$,
$\pi = (j_1,j_2)$ occurs in $\mathcal H_d\otimes\mathbb C^N$ only if $|j_1+j_2-d|\le2$, so
$W_\pi\subset\bigoplus_{|d-d(\pi)|\le4}\mathcal H_d\otimes\mathbb C^N$, a finite-dimensional space preserved by
$I_\tau(\lambda)$, on which $\kappa_{d(\pi)}\le\Delta\le\kappa_{d(\pi)+4}$. By I.C Lemma 2.4 (a), whose constants depend
on finitely many seminorms of the coefficients and so are uniform in $\tau$, there is $\mu_0$ with $I_\tau(\lambda)$
invertible on all of $H^2$ for $|\mathrm{Re}\,\lambda|\le X$, $|\mathrm{Im}\,\lambda|\ge\mu_0$. For
$|\lambda|\le X+\mu_0$ and $u\in W_\pi$ write $I_\tau(\lambda) = (1+\Delta)+R$,
$R := -1-\lambda^2+a_\tau\lambda+V_\tau+b_\tau$; then
$\|Ru\|\le C(\|u\|+\|u\|_{H^1})\le C(1+\kappa_{d(\pi)+4})^{1/2}\|u\|$ and $\|(1+\Delta)u\|\ge(1+\kappa_{d(\pi)})\|u\|$,
with $C$ uniform in $\tau$; as $(1+\kappa_{d+4})^{1/2}/(1+\kappa_d)\to0$, $I_\tau(\lambda)u\ne0$ for $u\ne0$ once
$d(\pi)\ge d_0$. The last statement: on $W_\pi$, $I_\tau(\lambda) = -\lambda^2\mathrm{Id}+\lambda A_\tau+B_\tau$ with
matrices continuous in $\tau$. $\square$

Each irreducible representation occurs in exactly one type and degree: the scalar, vector and tensor harmonics of degree
$l$ are the representations of highest weights $(\frac l2,\frac l2)$, $(\frac{l\pm1}2,\frac{l\mp1}2)$ and
$(\frac{l\pm2}2,\frac{l\mp2}2)$ (as recalled in the proof of III.D$''$ Proposition 3.1), whose two weights are equal,
differ by one and differ by two respectively, and whose sum is $l$. So $W_\pi$ is $\mathbb C^k\otimes\pi$ for the type
and degree of $\pi$, $I(\lambda)|_{W_\pi} = N(\lambda)\otimes\mathrm{Id}_\pi$ by Schur's lemma, and
$\det(I(\lambda)|_{W_\pi}) = \det N(\lambda)^{\dim\pi}$: the roots on $W_\pi$ are those of the type, each with
multiplicity multiplied by $\dim\pi$, and Proposition 2.3 (b) holds on every $W_\pi$, with $k\dim\pi = \dim W_\pi$.

**Lemma 2.5 ([Hin26] Lemma 8.5 at n = 4).** $\ker N(\widehat{\bar L}(0),0)\subset\ker
N(\rho^{-1}\widehat{\bar\delta_{\bar E^\Upsilon}}(0)\bar G,0)$. More precisely, at scalar type 0 the kernel is spanned
by the constant tensor
$$\bar h_{\mathrm s0} := -d\bar t^2+B_\Upsilon\,dx^2,\qquad B_\Upsilon := \frac{2-e_\Upsilon}{4e_\Upsilon},\tag{2.3}$$
and at scalar type 2, for each $S\in\mathcal S_2$, by $\bar h_{\mathrm s2}(S) := \bar\delta^*(\rho^{-1}w_S)$, $w_S$
spanning $\ker N_{\mathrm s2}(\widehat{\bar\Box^\Upsilon}(0),-1)$; both satisfy
$\bar\delta_{\bar E^\Upsilon}\bar G\bar h = 0$ and $\bar L\bar h = 0$ exactly.

*Proof.* By Proposition 2.3 (c) the kernel is that of scalar types 0 and 2, one-dimensional for each $S$; so it suffices
that the stated tensors are nonzero, stationary, homogeneous of degree 0 and of the stated types, and satisfy the two
equations: for a stationary homogeneous $\bar h$ of degree 0, $\widehat{\bar L}(0)\bar h = \rho^2N(\cdot,0)\bar h$ and
likewise for the gauge operator, both models being dilation homogeneous.

*Scalar type 0.* $\bar h_{\mathrm s0} = \bar\delta^*\Omega$ with $\Omega := d(-\frac12\bar t^2+\frac12B_\Upsilon r^2)$,
as $\bar\delta^*d$ is the Hessian. It is constant (so stationary and homogeneous of degree 0),
$\mathrm{SO}(4)$-invariant, and nonzero. $D\mathrm{Ric}(\bar\delta^*\Omega) = 0$ on Minkowski space. For the gauge
condition, $\bar\delta\bar G\bar h_{\mathrm s0} = 0$ (constant coefficients), and with
$\bar c_\Upsilon^\sharp = -r^{-1}\partial_{\bar t}$, $\iota_{\bar c_\Upsilon^\sharp}\bar h_{\mathrm s0} = r^{-1}d\bar t$
and $\mathrm{tr}\,\bar h_{\mathrm s0} = 1+4B_\Upsilon$, so $\bar E^\Upsilon\bar G\bar h_{\mathrm s0} = -\gamma_\Upsilon
r^{-1}d\bar t\,(2-e_\Upsilon(1+4B_\Upsilon)) = 0$ exactly when $1+4B_\Upsilon = 2/e_\Upsilon$, which is (2.3). Then
$\bar L\bar h_{\mathrm s0} = D\mathrm{Ric}\,\bar h_{\mathrm s0}+\bar\delta^*_{\bar E^C}(\bar\delta_{\bar E^\Upsilon}\bar
G\bar h_{\mathrm s0}) = 0$. (In the source's terms, $\Omega = t\,\bar\omega^{(0)}_{\mathrm s0}+\bar W$ with
$\bar\omega^{(0)}_{\mathrm s0} = -d\bar t$ Killing and $\bar W = B_\Upsilon r\,dr$ solving
$\bar\Box^\Upsilon\bar W = -[\bar\Box^\Upsilon,\bar t]\bar\omega^{(0)}_{\mathrm s0}$; that $-1$ is not an s0 root of
$\Box^\Upsilon$ for $z>0$, III.D Lemma 4.1, is what makes $\bar W$ unique, and $B_\Upsilon\to\infty$ as
$e_\Upsilon\to0$, where $1-\lambda^\Upsilon_{\mathrm s0,2}\to-1$.)

*Scalar type 2.* $1-l = -1$ is a simple root of $\Box^\Upsilon$ at scalar type 2 (III.D Lemma 4.1), so $w_S$ exists and
is unique up to scaling, and $\Omega_S := \rho^{-1}w_S$ is stationary, homogeneous of degree 1 and annihilated by
$\bar\Box^\Upsilon$. So $\bar h_{\mathrm s2}(S) = \bar\delta^*\Omega_S$ is stationary, homogeneous of degree 0, of
scalar type 2, satisfies $\bar\delta_{\bar E^\Upsilon}\bar G\bar h_{\mathrm s2} = \frac12\bar\Box^\Upsilon\Omega_S = 0$
and $\bar L\bar h_{\mathrm s2} = D\mathrm{Ric}(\bar\delta^*\Omega_S)+\bar\delta^*_{\bar E^C}(0) = 0$. It is nonzero:
otherwise $\Omega_S$ would be a stationary Killing 1-form homogeneous of degree 1, and those are the spatial rotations,
of vector type 1.

(*Computed:* `linroots5.py` R2-R3, with every parameter symbolic: $\Box^\Upsilon\Omega = 0$, the two equations,
stationarity, homogeneity and $\bar h\ne0$; R2 solves for $\bar W$ and finds $B_\Upsilon$; R3 finds the kernel at scalar
type 2 one-dimensional, and zero at scalar type 3, the control.) $\square$

## 3. tf-admissibility ([Hin26] Proposition 8.6 and Corollary 8.7 at n = 4)

For an operator $\hat P$ satisfying (H1)-(H2), I.C (4.1) defines $N_{\mathrm{tf}}(\hat P,\hat\sigma)$ from its data at
$\rho = 0$ only: $S_0$, $N(P^{(0)})$ and $H_0$ (I.C section 4.1 (a)); and I.C Theorem 4.3 and Definition 5.1 use only
these data. For $\hat P = \widehat{2L_b}$, $S_0 = \bar S$ and $N(P^{(0)})$ is $\widehat{2\bar L}(0)$ (III.F Lemma 2.1
(2)-(3)); since $2\bar L = -2\partial_{t_*}\rho(\rho\partial_\rho-\frac32-\bar S)+\widehat{2\bar L}(0)$ exactly, with no
$\partial_{t_*}^2$ term ($dt_*$ is null), $N_{\mathrm{tf}}(\widehat{2L_b},\hat\sigma)$ is the spectral family
$\widehat{2\bar L}(\hat\sigma)$ written in $\hat x$ (I.C (4.1)-(4.2) with $\varsigma = 1$). The same holds for
$\Box^C_b$ with its model $\bar\Box^C$: the $\partial_{t_*}$ coefficient of $\bar\Box^C$ is
$-2\rho(\rho\partial_\rho-\frac32-\bar S^C)$ exactly ($\bar\Box$ gives $-2\rho(\rho\partial_\rho-\frac32)$, and
$2\bar\delta\bar G\bar E^C$ gives $\rho\bar S^C$ as in III.F Lemma 3.1), and the rest is stationary and dilation
homogeneous. And it holds for the operators of III.F Lemma 2.1 with the parameters $(\gamma_C,\gamma_\Upsilon)$ replaced
by $(\tau\gamma_C,\tau\gamma_\Upsilon)$, $\tau\in[0,1]$, or by $(0,\gamma_\Upsilon)$, which satisfy (H1)-(H2) by the
proof of III.F Lemma 2.1, which does not use the values of the parameters; at $\tau = 0$ the model is $\bar\Box$ on
$S^2T^*$, componentwise in the Cartesian frame. For all of them $\mathrm{spec}\,\bar S\subset[0,\infty)$ (III.F (3.1),
the $\gamma$'s being $\ge0$), and $\mathrm{spec}\,\bar S^C\subset(0,\infty)$ (III.E section 1).

*Weights.* In I.C Theorem 4.3 the b-weight of $\mathcal X_{\mathrm{tf},\theta}$ at ztf is $q-2$, and the tf-admissible
weight is $\beta := 2-q$; for brevity $\mathcal X(\beta)$, $\mathcal Y(\beta)$ and $\mathrm{ind}(\beta)$ denote the
spaces and the index of $N_{\mathrm{tf}}(e^{i\theta}):\mathcal X_{\mathrm{tf},\theta}\to\mathcal Y_{\mathrm{tf},\theta}$
at $q = 2-\beta$ ($\theta$, $s$, $\alpha_+$ and the orders fixed, in the settings of I.C Theorem 4.3 (1)-(2)), defined
when $\beta$ is not the real part of an indicial root. Near ztf $N_{\mathrm{tf}} = \hat r^{-2}L$, with $L$ as in I.C
section 2.5 at the end at 0 ($\varrho = \hat r$) and Mellin symbol $J(\lambda) = I(-\lambda)$ (I.C section 4.1 (c)); so
a root $\mu$ of $J$ is $-\mu_{\mathrm b}$, $\mu_{\mathrm b}\in\mathrm{spec}_{\mathrm b}$, and $\mathcal X(\beta)$ is
$H^s_{\mathrm b,-\beta}$ there.

**Lemma 3.1 (relative index).** Let $\beta_1<\beta_2<\beta_1+1$, neither the real part of a point of
$\mathrm{spec}_{\mathrm b}$, and $s\in\mathbb Z$. Then $\mathrm{ind}(\beta_2)-\mathrm{ind}(\beta_1) = \dim F$, where
$F := \bigoplus_\mu F_\mu$ over the roots $\mu$ of $J$ with $-\beta_2<\mathrm{Re}\,\mu<-\beta_1$ and
$$F_\mu := \big\{
\mathrm{Res}_{\lambda = \mu}\big(\varrho^\lambda J(\lambda)^{-1}g(\lambda)\big):
 g\ \text{holomorphic near }\mu,\ C^\infty(\mathbb S^3;\mathbb C^N)\text{-valued}\big\}.\tag{3.1}$$
$\dim F_\mu$ is the sum over the finitely many $W_\pi$ on which $\mu$ is a root of $\mathrm{ord}_\mu\det(J|_{W_\pi})$,
the algebraic multiplicity; when $J$ is an indicial family as in Lemma 2.4, it is the multiplicity of $-\mu$ as a root
of $I$ on those components.

*Proof.* Put $c_i := -\beta_i$, so $c_2<c_1<c_2+1$, $\mathcal X(\beta_1)\subset\mathcal X(\beta_2)$ and
$\mathcal Y(\beta_1)\subset\mathcal Y(\beta_2)$, and write $\mathcal X_i$, $\mathcal Y_i$,
$N := N_{\mathrm{tf}}(e^{i\theta})$, $N_i := N|_{\mathcal X_i}$. Every $\Phi\in F_\mu$ is a finite sum
$\varrho^\mu\sum_j(\log\varrho)^ja_j$, $a_j$ smooth, and
$N(L)\Phi = \mathrm{Res}(\varrho^\lambda J(\lambda)J(\lambda)^{-1}g(\lambda)) = 0$, as
$N(L)\varrho^\lambda a = \varrho^\lambda J(\lambda)a$. Let $\chi\in C^\infty_c([0,1))$ be a function of $\hat r$ equal
to 1 near 0.

*Step 1: the expansion.* Let $\mathcal Z := \{w\in\mathcal X_2:Nw\in\mathcal Y_1\}$ and $w\in\mathcal Z$. By I.C Lemma
2.5, $v := \chi w\in H^s_{\mathrm b,c_2}$, and $f := N(L)v = \chi\hat r^2Nw+[L,\chi]w-(L-N(L))\chi w$ lies in
$H^{s-2}_{\mathrm b,c_1}$: the first term as $Nw\in\mathcal Y_1$, whose weight at ztf is $c_1-2$; the second has compact
support in $\mathrm{tf}^\circ$; the third as $L-N(L)\in\varrho\,\mathrm{Diff}^2_{\mathrm b}$ maps $H^s_{\mathrm b,c_2}$
to $H^{s-2}_{\mathrm b,c_2+1}\subset H^{s-2}_{\mathrm b,c_1}$. So $\mathcal Mf$ is holomorphic on
$\{\mathrm{Re}\,\lambda<c_1\}$ with the line bounds (2.1) of I.C up to $\mathrm{Re}\,\lambda = c_1$, and
$J\mathcal Mv = \mathcal Mf$ on $\{\mathrm{Re}\,\lambda<c_2\}$. Hence $J^{-1}\mathcal Mf$ continues $\mathcal Mv$
meromorphically to $\{\mathrm{Re}\,\lambda<c_1\}$, with poles only at roots $\mu$ with $c_2<\mathrm{Re}\,\mu<c_1$ (none
on $\mathrm{Re}\,\lambda = c_2$, by hypothesis), finitely many by I.C Lemma 2.4 (b). Let $\Phi :=
-\sum_\mu\mathrm{Res}_{\lambda = \mu}(\varrho^\lambda J(\lambda)^{-1}\mathcal Mf(\lambda))\in F$. As
$\mathcal M(\chi\varrho^\mu(\log\varrho)^ja)$ continues meromorphically with a single pole, at $\mu$, of principal part
$-j!(\lambda-\mu)^{-j-1}a$ (differentiate
$\int_0^{\varrho_0}\varrho^{\mu-\lambda-1}d\varrho = \varrho_0^{\mu-\lambda}/(\mu-\lambda)$ $j$ times in $\mu$), and
$\mathrm{Res}_{\lambda = \mu}(\varrho^\lambda(\lambda-\mu)^{-j-1}a) = \varrho^\mu(\log\varrho)^ja/j!$, the transform of
$\chi\,\mathrm{Res}(\varrho^\lambda q)$ has principal part $-q$ at $\mu$ for every principal part $q$; so
$\mathcal M(v-\chi\Phi) = J^{-1}\mathcal Mf-\mathcal M(\chi\Phi)$ is holomorphic on $\{\mathrm{Re}\,\lambda<c_1\}$. Its
$L^2$ norms on the lines $\mathrm{Re}\,\lambda = x$, $c_2-\epsilon\le x<c_1$, are bounded uniformly: for
$|\mathrm{Im}\,\lambda|\ge\mu_0$ by I.C Lemma 2.4 (a) and (2.1), with $\mathcal M(\chi\Phi)$ minus its principal parts
rapidly decreasing there; on the remaining compact set by holomorphy. I.C Lemma 2.3 gives
$v-\chi\Phi\in H^0_{\mathrm b,c_1}$; and $L(v-\chi\Phi)\in H^{s-2}_{\mathrm b,c_1}$ near ztf, because
$L(\chi\Phi) = [N(L),\chi]\Phi+(L-N(L))\chi\Phi$ with $\mathrm{Re}\,\mu+1>c_2+1>c_1$; so I.C Lemma 2.5 at the weight
$c_1$ gives $w-\chi\Phi\in H^s_{\mathrm b,c_1}$ near ztf. Away from ztf, $w-\chi\Phi$ and $w$ agree near sctf and are
smooth in between, and $N(\chi\Phi)\in\mathcal Y_1$ by the same computation; so $w-\chi\Phi\in\mathcal X_1$. If
$\chi\Phi\in\mathcal X_1$ for some $\Phi\in F$, then $\mathcal M(\chi\Phi)$ is holomorphic on
$\{\mathrm{Re}\,\lambda<c_1\}$, so its principal parts vanish and $\Phi = 0$ (the functions
$\varrho^\mu(\log\varrho)^ja$ with distinct $(\mu,j)$ are independent). So $\mathcal Z = \mathcal X_1\oplus\chi F$, with
$\chi F\subset\mathcal Z$ by the same computation.

*Step 2: the target.* $\mathcal Y_2 = \mathcal Y_1+N(\mathcal X_2)$. Let $y\in\mathcal Y_2$, $\chi'$ a cut-off with
$\chi'\chi = \chi$, and $f := \chi'\hat r^2y\in H^{s-2}_{\mathrm b,c_2}$. Define $u$ on all of
$(0,\infty)\times\mathbb S^3$ by $\mathcal Mu := J^{-1}\mathcal Mf$ on the line $\mathrm{Re}\,\lambda = c_2$; by
Plancherel in $t = -\log\varrho$ (as in I.C (2.2), $s$ being an integer) and I.C Lemma 2.4 (c), $e^{c_2t}u\in H^s$ and
$N(L)u = f$, so $\chi u\in H^s_{\mathrm b,c_2}$. Then
$y-N(\chi u) = (1-\chi)y-\hat r^{-2}[N(L),\chi]u-\hat r^{-2}(L-N(L))\chi u$: the first term vanishes near ztf, where
alone $\mathcal Y_1$ and $\mathcal Y_2$ differ; the second has compact support in $\mathrm{tf}^\circ$; the third lies in
$\hat r^{-2}H^{s-2}_{\mathrm b,c_2+1}\subset H^{s-2}_{\mathrm b,c_1-2}$ near ztf. So $y-N(\chi u)\in\mathcal Y_1$, and
$\chi u\in\mathcal X_2$.

*Step 3: the indices.* $N_2$ and $N_1$ are Fredholm (I.C Theorem 4.3 (3)). $\ker N_2 = \ker(N|_{\mathcal Z})$, as kernel
elements lie in $\mathcal Z$. The map $\mathcal Y_1/N(\mathcal Z)\to\mathcal Y_2/N(\mathcal X_2)$ is injective (if
$y = Nw$ with $w\in\mathcal X_2$ and $y\in\mathcal Y_1$, then $w\in\mathcal Z$) and surjective by Step 2. So
$N|_{\mathcal Z}:\mathcal Z\to\mathcal Y_1$, with $\mathcal Z$ normed as $\mathcal X_1\oplus\chi F$, is Fredholm with
the index of $N_2$; and it is $N_1$ extended by the finite-dimensional space $\chi F$, so its index is
$\mathrm{ind}\,N_1+\dim F$. *Multiplicity.* By Lemma 2.4 and the discreteness of I.C Lemma 2.4 (b), $\mu$ is a root on
finitely many $W_\pi$, and $J^{-1}g$ splits accordingly. On a finite-dimensional block, the ring of germs of holomorphic
functions at $\mu$ being a principal ideal domain, $J = E\,\mathrm{diag}((\lambda-\mu)^{k_i})\,F'$ with $E$, $F'$
holomorphic and invertible near $\mu$ (Smith form) and $\sum_ik_i = \mathrm{ord}_\mu\det J$. As $g$ ranges over
holomorphic germs so does $E^{-1}g$; the principal parts of $\mathrm{diag}((\lambda-\mu)^{-k_i})h$ form a space of
dimension $\sum k_i$; multiplication by $F'^{-1}$ is a bijection of principal-part spaces (with inverse multiplication
by $F'$); and $q\mapsto\mathrm{Res}(\varrho^\lambda q)$ is injective on principal parts, as
$\mathrm{Res}(\varrho^\lambda(\lambda-\mu)^{-j-1}a) = \varrho^\mu(\log\varrho)^ja/j!$. So $\dim F_\mu = \sum k_i$.
$\square$

**Lemma 3.2 (common orders).** Let $\hat P_1,\dots,\hat P_k$ satisfy (H1)-(H2) with principal symbols positive multiples
of one another, and let $\alpha_+\in\mathbb R$. There are orders $\mathsf r_\pm$ admissible with weight $\alpha_+$ for
every $\sigma_0\in J_\pm$, in the sense of I.C section 4.3, for all of them at once; for a family continuous in a
parameter in a compact set, the same holds uniformly.

*Proof.* The characteristic set at the boundary face, the radial sets and the direction of the flow depend only on the
principal symbol, up to positive multiples (I.A section 4). Take $\mathsf r_{\mathrm{in}}$ above the largest of the
incoming thresholds $\frac12(-1+\vartheta^{(i)}_{\mathrm{in}})-\alpha_+$ (bounded over a compact parameter set, as they
depend continuously on the coefficients) and $\mathsf r_{\mathrm{out}}$ below the smallest of
$-\frac12+\bar S^{(i)}-\alpha_+$, with $\mathsf r_{\mathrm{in}}\ge\mathsf r_{\mathrm{out}}$; I.A Lemma 7.1 gives an
order pair with these values, which satisfies (O1)-(O3) of I.A (1.5) for each operator. On compact subsets of $(0,\pi)$
the constant order $\mathsf r_{\mathrm{out}}$ is allowed for each (I.C Theorem 4.3 (2)). $\square$

**Proposition 3.3 ([Hin26] Proposition 8.6 at n = 4).** Assume $e_\Upsilon>0$, (C1), and fix all parameters but
$\gamma_\Upsilon$. There is $\gamma_1>0$ such that for $\gamma_\Upsilon\in(0,\gamma_1)$ (so that
$z = 4e_\Upsilon\gamma_\Upsilon^2\in(0,\frac12]$) and every $b$ near $b_0$, $\widehat{L_b}$ is tf-admissible (I.C
Definition 5.1) with every weight $\beta\in(0,1]$.

*Proof.* (i) of I.C Definition 5.1: $(0,1]$ lies in an indicial gap, by Proposition 2.3 (a), and the gap contains
$(0,\beta_+)$ with $\beta_+>1$. As $N_{\mathrm{tf}}$ depends only on the model, $b$ plays no role. Fix $\alpha_+$,
$s\in\mathbb Z$ large, and by Lemma 3.2 orders admissible at once for $\widehat{2L_b}$, $\widehat{\Box^C_b}$, the
operator $\hat P'$ with parameters $(0,\gamma_\Upsilon)$, and the operators $\hat P_\tau$ with parameters
$(\tau\gamma_C,\tau\gamma_\Upsilon)$, uniformly for $\gamma_\Upsilon\in[0,1]$ and $\tau\in[0,1]$; by I.C Theorem 4.3 (3)
kernels, annihilators and indices do not depend on these choices or on $q$ with $2-q$ in the gap.

*(ii) The kernel.* Let $\theta\in[0,\pi]$, $\hat\sigma := e^{i\theta}$, $\beta\in(0,\frac12)$ (by Theorem 4.3 (3) this
covers every weight in the gap), and $u_0\in\mathcal X(\beta)$ with $N_{\mathrm{tf}}(\widehat{2L_b},\hat\sigma)u_0 = 0$.

*Step 1.* By I.C Theorem 4.3 (5), with the gap $(0,\beta_+)$, $u_0\in\rho_{\mathrm{ztf}}^{-\beta'}C^\infty_{\mathrm b}$
near ztf for every $\beta'>0$; and $\widehat{2\bar L}(\hat\sigma)u_0 = 0$ on $\mathbb R^4\setminus0$ (the description
above).

*Step 2: the gauge 1-form.* The linearised second Bianchi identity on Minkowski space,
$\bar\delta\bar GD\mathrm{Ric} = 0$, gives $\bar\delta\bar G(2\bar L) = 2\bar\delta\bar G\bar\delta^*_{\bar
E^C}\bar\delta_{\bar E^\Upsilon}\bar G = \bar\Box^C\bar\delta_{\bar E^\Upsilon}\bar G$; the operators are stationary, so
their spectral families compose, and $\eta_0 := \widehat{\bar\delta_{\bar E^\Upsilon}\bar G}(\hat\sigma)u_0$ satisfies
$\widehat{\bar\Box^C}(\hat\sigma)\eta_0 = \widehat{\bar\delta\bar G}(\hat\sigma)\widehat{2\bar L}(\hat\sigma)u_0 = 0$,
that is, $N_{\mathrm{tf}}(\widehat{\Box^C_b},\hat\sigma)\eta_0 = 0$.

*Step 3: $\eta_0\in\mathcal X_{\Box^C}(\beta_C)$, $\beta_C := 1+2\beta\in(1,2)$.*
$\widehat{\bar\delta_{\bar E^\Upsilon}\bar G}(\hat\sigma) = \hat\rho A_1+\hat\sigma A_0$ with
$A_1 := \rho^{-1}\widehat{\bar\delta_{\bar E^\Upsilon}}(0)\bar G\in\mathrm{Diff}^1_{\mathrm b}$ and $A_0$ a bundle map,
both homogeneous of degree 0. Near ztf, $\hat\rho = \hat r^{-1}$, so
$\eta_0\in\rho_{\mathrm{ztf}}^{-1-\beta'}C^\infty_{\mathrm b}$ for every $\beta'>0$, hence
$\eta_0\in H^\infty_{\mathrm b,-1-2\beta}$ there (I.C Lemma 2.2 (f)), which is the ztf part of $\mathcal X(\beta_C)$.
Near sctf, $\hat\rho A_1\in\mathrm{Diff}^1_{\mathrm{sc}}$ and $A_0$ has order $(0,0)$, so
$\eta_0\in H^{s-1,\mathsf r+\alpha_+}_{\mathrm{sc}}$ there, with the common orders; in between $\eta_0$ is smooth. With
$N_{\mathrm{tf}}\eta_0 = 0$, $\eta_0\in\mathcal X_{\mathrm{tf},\theta}$ for $\widehat{\Box^C_b}$ at the regularity $s-1$
and the weight $\beta_C$, which lies in the gap $(-C_0,2)$ of $\Box^C_b$ (C1).

*Step 4.* By III.E Theorem 1.1 (4), $\widehat{\Box^C_b}$ is tf-admissible with the weight $\beta_C\in[-C_0,2)$, so
$\eta_0 = 0$.

*Step 5: the unmodified gauge.* With $\eta_0 = 0$, $\widehat{2\bar L}(\hat\sigma)u_0 =
2\widehat{D\mathrm{Ric}}(\hat\sigma)u_0 = \widehat{2\bar L'}(\hat\sigma)u_0$,
$\bar L' := D\mathrm{Ric}+\bar\delta^*\bar\delta_{\bar E^\Upsilon}\bar G$, the model of $\hat P'$ (parameters
$(0,\gamma_\Upsilon)$). So $N_{\mathrm{tf}}(\hat P',\hat\sigma)u_0 = 0$.
$2\bar L' = \bar\Box+2\bar\delta^*\bar E^\Upsilon\bar G$ does not involve $\gamma_C$.

*Step 6: small $\gamma_\Upsilon$.* $u_0\in\mathcal X_{\hat P'}(1)$: near ztf $u_0\in H^s_{\mathrm b,-1}$, as
$u_0 = O(\hat r^{-\beta'})$ with b-regularity and $\beta'<1$; near sctf it is as before. At $\gamma_\Upsilon = 0$,
$\hat P' = \widehat{\Box}$ on $S^2T^*$, componentwise in the Cartesian frame, tf-admissible with every weight in $(0,2)$
(I.C Proposition 5.3), so by I.C Corollary 5.2 (b) at the weight 1, uniformly in $\theta$ over the three sectors,
$\|w\|\le C\|N^0_{\mathrm{tf}}w\|$. The difference $N_{\mathrm{tf}}(\hat P',e^{i\theta})-N^0_{\mathrm{tf}}(e^{i\theta})
= -2ie^{i\theta}\hat\rho\bar S'+\hat\rho^2M'$, with $\bar S'$ and $M'\in\mathrm{Diff}^1_{\mathrm b}$ homogeneous and
$O(\gamma_\Upsilon)$, is bounded from the space of $\mathcal X$ into that of $\mathcal Y$ with norm $C'\gamma_\Upsilon$,
uniformly in $\theta$, exactly as in III.D Lemma 7.1; so
$\|u_0\|\le C\|N_{\mathrm{tf}}(\hat P',e^{i\theta})u_0\|+CC'\gamma_\Upsilon\|u_0\|$, and $u_0 = 0$ once
$CC'\gamma_\Upsilon\le\frac12$. This fixes $\gamma_1$; it depends on the orders, hence on $\gamma_C$, which is fixed
first. The weight 1 lies in the indicial gap of $\hat P'(0)$ for small $\gamma_\Upsilon$: its roots are within
$O(\gamma_\Upsilon)$ of the integer roots of $\bar\Box$ on $S^2T^*$ (III.A$'$ Lemma 2.3), none in $(0,2)$, on the
finitely many components that meet the strip $|\mathrm{Re}\,\lambda-1|\le\frac12$ (Lemma 2.4), and on no other.

*(iii) The adjoint.* By I.C Theorem 4.3 (3) the annihilator of the range of
$N_{\mathrm{tf}}(\widehat{2L_b},1):\mathcal X(\beta)\to\mathcal Y(\beta)$ is
$\ker_{\mathcal X^*}N_{\mathrm{tf}}(1)^{*h}$; by (ii) the operator is injective, so it suffices that its index is 0.
Consider the family $\hat P_\tau$, $\tau\in[0,1]$, at $\theta = 0$ with the common orders. $\hat P_1 = \widehat{2L_b}$
and $\hat P_0 = \widehat{\Box}$ on $S^2T^*$. $\mathcal X$ does not depend on $\tau$, and
$\tau\mapsto N_{\mathrm{tf}}(\hat P_\tau,1)$ is continuous in the norm of bounded maps $\mathcal X\to\mathcal Y$ (the
differences are as in Step 6). Let $I_\tau$ be the indicial family of $\hat P_\tau(0)$, apply Lemma 2.4 with $X := 2$
and $\mathcal T = [0,1]$, and for $\beta''$ not the real part of a root of $I_\tau$, $|\beta''-\beta|<1$, put
$$G(\tau) := \mathrm{ind}_\tau(\beta'')-\sum_\pi\big(n_\pi(\tau,\beta'')-\dim W_\pi\big),$$
$n_\pi(\tau,\beta'')$ the number of roots of $I_\tau$ on $W_\pi$ with real part $<\beta''$, with multiplicity. The sum
is finite: for $d(\pi)\ge d_0$ no root on $W_\pi$ has $|\mathrm{Re}\,\lambda|\le2$ for any $\tau$, so by continuity
$n_\pi(\tau,\beta'')$ is its value at $\tau = 0$, where the roots on $W_\pi$ are those of $\bar\Box$, $\dim W_\pi$ of
them $\le0$ and $\dim W_\pi$ of them $\ge2$ (III.A$'$ Lemma 2.3: $-d$ and $d+2$), so the term is 0. $G$ does not depend
on $\beta''$: by Lemma 3.1 (through intermediate weights, finitely many roots lying between),
$\mathrm{ind}_\tau(\beta_2)-\mathrm{ind}_\tau(\beta_1)$ is the number of roots with real part in $(\beta_1,\beta_2)$,
which is the change of the sum. $G$ is locally constant: near $\tau_0$ choose $\beta''$ that no root of the finitely
many components meeting the strip has as real part for $\tau$ near $\tau_0$ (the roots move continuously); then
$\mathrm{ind}_\tau(\beta'')$ is locally constant (a norm-continuous family of Fredholm operators on fixed spaces) and so
is the sum. So $G(1) = G(0)$. At $\tau = 0$ and $\beta'' = \beta$, $\mathrm{ind} = 0$ ($\widehat{\Box}$ is invertible,
I.C Proposition 5.3 and Corollary 5.2 (a)) and the sum is 0 (the roots of $\bar\Box$ split evenly about $(0,2)$). At
$\tau = 1$ and $\beta'' = \beta$ the sum is 0 by Proposition 2.3 (b) on every $W_\pi$ (no root has real part in $(0,1]$,
so $n_\pi(1,\beta)$ counts the roots with real part $\le0$, $\dim W_\pi$ of them). Hence $\mathrm{ind}_1(\beta) = 0$.
$\square$

As in the source, the quantitative estimates of I.C Corollary 5.2 now hold for
$N_{\mathrm{tf}}(\widehat{L_b},\hat\sigma)$. On b-Sobolev spaces they read:

**Corollary 3.4 ([Hin26] Corollary 8.7 at n = 4).** On tf use the b-density $|\frac{d\hat r}{\hat r}d\slashed g|$ and
$H^{k,a,c}_{\mathrm b}(\mathrm{tf}) := \rho_{\mathrm{sctf}}^a\rho_{\mathrm{ztf}}^cH^k_{\mathrm b}(\mathrm{tf})$. Fix
$$\beta_{\mathrm{sctf}}<\tfrac32 = \tfrac32+\min\mathrm{Re}\,\mathrm{spec}\,\bar S,
\qquad\beta_{\mathrm{ztf}}\in[-1,0).\tag{3.2}$$
Then there is $\ell\in\mathbb N_0$ such that for all $k\in\mathbb N_0$ and $\epsilon>0$
$$N_{\mathrm{tf}}(\widehat{L_b},\pm1)^{-1}:
H^{k+\ell,\beta_{\mathrm{sctf}}+1,\beta_{\mathrm{ztf}}-2}_{\mathrm b}(\mathrm{tf})\to
H^{k,\beta_{\mathrm{sctf}}-\epsilon,\beta_{\mathrm{ztf}}}_{\mathrm b}(\mathrm{tf})\ \text{is bounded}.\tag{3.3}$$

*Proof.* *The threshold at $R_{\mathrm{out}}$.* I.A (1.5) asks $\mathsf r+\alpha_+<-\frac12+\bar S_L$ there,
$\bar S_L := \frac12\inf_{\partial X}\lambda_{\min}(\bar S+\bar S^{*h})$ for a fibre inner product $h$ of our choice
(I.A Proposition 4.9). For every $\delta>0$ some smooth $h$ gives $\bar S_L\ge-\delta$, as
$\min\mathrm{Re}\,\mathrm{spec}\,\bar S = 0$ (III.F (3.1)): at each $\omega$, a Jordan basis of $\bar S(\omega)$
rescaled so that the off-diagonal entries are at most $\delta/2$ defines $h_\omega$ with
$\mathrm{Re}\,h_\omega((\bar S+\delta)u,u)\ge\frac\delta2h_\omega(u,u)$, a strict inequality, which persists for
$\bar S(\omega')$, $\omega'$ near $\omega$; the condition is convex in $h$, so a partition of unity on $\mathbb S^3$
glues these. *The orders.* Take $\beta := -\beta_{\mathrm{ztf}}\in(0,1]$, $q := 2-\beta$, $\alpha_+ := 0$,
$\delta := \frac14(\frac32-\beta_{\mathrm{sctf}})$, $\epsilon<\delta$ (it suffices to prove (3.3) for small $\epsilon$),
$\mathsf r_{\mathrm{out}} := \beta_{\mathrm{sctf}}-2-\frac\epsilon2<-\frac12-\delta$, and the orders $\mathsf r_\pm$ of
I.A Lemma 7.1 at $\sigma_* = \pm1$ with that outgoing value, constant near $R_{\mathrm{out}}$. By Proposition 3.3 and
I.C Corollary 5.2 (a)-(b), with Theorem 4.3 (4) for $k$ further b-derivatives, $N_{\mathrm{tf}}(\pm1)^{-1}$ is bounded
from $H^{(s-2;k),(\mathsf r+1,q-2)}_{\mathrm{sc},b;b}$ to $H^{(s;k),(\mathsf r,q)}_{\mathrm{sc},b;b}$. Near ztf these
are $H^{s-2+k}_{\mathrm b,\beta_{\mathrm{ztf}}-2}$ and $H^{s+k}_{\mathrm b,\beta_{\mathrm{ztf}}}$ for the b-density (I.C
Definition 4.1). Near sctf, on the end of $\mathbb R^4_{\hat x}$, II.G$'$ Lemma 4.1 ((4.1a)-(4.1b), on $\mathbb R^4$
without the artificial boundary) gives
$H^{k+\ell,\beta_{\mathrm{sctf}}+1}_{\mathrm b}\hookrightarrow H^{(s-1;k),\mathsf r+1}$ and
$H^{(s;k),\mathsf r}\hookrightarrow H^{k-\tilde\ell,\beta_{\mathrm{sctf}}-\epsilon}_{\mathrm b}$ with the losses $\ell$,
$\tilde\ell$ of that lemma ($\mathsf r_{\mathrm{out}}+3+\frac\epsilon2 = \beta_{\mathrm{sctf}}+1$ and
$\mathsf r_{\mathrm{out}}+2-\frac\epsilon2 = \beta_{\mathrm{sctf}}-\epsilon$). Replacing $k$ by $k+\tilde\ell$ and
enlarging $\ell$ gives (3.3), with $\ell$ independent of $\epsilon$ as in II.G$'$ Corollary 4.2. $\square$

## 4. Findings

(F$'$1) *The roots at n = 4.* The gauge-invariant roots are $-l$ and $l+2$ (his $-l$, $l+1$); at v1 the cancelled factor
is $\lambda(\lambda-2)$, because $\Box^C$'s vector type 1 root is $3$, exactly and for every parameter (Lemma 2.2, by
hand), where his is 2; and the s0 indicial solution at $\lambda = 0$ is the gauge-fixed rescaling of time (2.3), not the
leading term of the change of mass, which at $n = 4$ enters at the root 2. The gap is at least $(0,1]$, against his
$(0,\epsilon_{\mathrm{ind}})$.

(F$'$2) *Simplicity and (8.13).* The source asserts that all roots are simple and that (8.13) can be arranged, with the
roots read from Mathematica. The list shows what this rests on: $z = 4e_\Upsilon\gamma_\Upsilon^2>0$ (at $z = 0$, $-l$
and $2-\lambda^\Upsilon_{\mathrm sl,l+2}$ meet, and $0$ and $2-\lambda^\Upsilon_{\mathrm s0,2}$), the simplicity of the
constraint operator's roots (C2), their avoiding finitely many integers per type (C3), and $z$ off a countable set
(proved here); (8.13) needs, beyond the finiteness of Lemma 2.4, that a constraint root with integer real part be real
(C4). (C2)-(C4) are added to the obligations of Part IV, written into III.E Theorem 1.1 (3) in D231.

(F$'$3) *Lemma 8.5 is not needed for tf-admissibility at n = 4.* In the source the gauge 1-form $\eta_0$ has a
$\hat r^{-1}$ term at ztf, outside the tf-admissible range of $\Box^C$, which ends at 1 in four dimensions, and Lemma
8.5 removes it. Here that range is $[-C_0,2)$ and $\eta_0 = O(\hat r^{-1-\epsilon})$ is inside it (Proposition 3.3, Step
3). Lemma 8.5 is proved for later use, as in the source.

(F$'$4) *The index.* The source restricts to one type and degree and moves the weight across the roots, citing the
example after his Definition 2.30. Here the relative index theorem is proved on I.C's spaces (Lemma 3.1), and the
restriction to a type is replaced by Lemma 2.4: only finitely many isotypic components meet a strip, uniformly along the
deformation. The even split of Proposition 2.3 (b) at both ends of the deformation is what makes the index 0, as in the
source.

(F$'$5) *Spaces.* The source's tf-admissibility is the triviality of kernels on $\mathcal A^{\alpha,-\beta}$ for every
$\alpha$, and his proof improves the sctf decay of $u_0$ before using the Fredholm spaces. Here (I.C Definition 5.1) it
is injectivity on the Fredholm spaces, and $u_0$ passes to $\eta_0$ and to $\hat P'$ within them, by orders admissible
for all the operators at once (Lemma 3.2).

(F$'$6) *Corollary 8.7's weights at n = 4* are $\beta_{\mathrm{sctf}}<\frac32$ (his 1, the shift $\frac{n-1}2$) and
$\beta_{\mathrm{ztf}}\in[-1,0)$.