# Part III.G$'''$. The $\iota^+$-normal operator on partially polyhomogeneous spaces at n = 4 ([Hin26] section 9.1.3)

*Status.* Verified (D245: the hundred-and-second verifier; four minor findings and fourteen nits seated, to be read).
This part proves, at spatial dimension $n = 4$, [Hin26] Lemmas 9.13-9.14, Proposition 9.15, Definition 9.16 with (9.49),
Remark 9.17, Corollary 9.18, Definition 9.19, Remark 9.20, Lemma 9.21, (9.54)-(9.55), Proposition 9.22 and Remarks
9.23-9.24 (pp. 180-186). The source uses this material only in its section 12. Parts are cited as before; the source is
[Hin26] = P. Hintz, arXiv:2606.28253v2 (printed page numbers).

*What n = 4 changes.* (a) The source's (9.44), $1<\ell_I<1+(1-e_C)(1-v_C)\gamma_C$, becomes
$\frac32<\ell_I<\frac32+s_C$, with $s_C := \gamma_C(1-e_C)(1-v_C)$ (and $\ell_I$ off the real parts of
$\mathcal E^{\mathrm{tot}}_I$). (b) The source's sources carry two exceptional exponents in their $(dx^1)^2$-component,
at $1+1$ and $1+1+(1-e_\Upsilon)\gamma_\Upsilon$. At $n = 4$ they carry one, at $1+\lambda_\sharp$, with
$$\lambda_\sharp := \tfrac32+(1-e_\Upsilon)\gamma_\Upsilon,\tag{0.1}$$
since $\pi_{11}h$ carries no radiation field (III.C (C3)). So the incoming pole the source has at $\lambda = 1$ has no
counterpart, and the least pole is $\lambda_\sharp$ (Corollary 2.6). (c) The pure $\iota^+$ resonances have real part at
least 2 (III.G$'$ Lemma 4.2 (a)), where the source's exceed 1. (d) III.G$'$ Theorem 3.1 (2) loses $d$ derivatives with
$d$ depending on $\mathrm{Re}\,\lambda$, so the finite-regularity statements here hold on strips. (e) The expansion at
$K^+$ is III.G$''$'s, below $\ell_K^{\max} = \min(3,2+2\gamma_Cv_C)$. The harmonic degrees there are at most 4 (the
source's 5).

## 1. Setting

We use III.G$'$ section 1: $\iota^+ = [0,\infty]_v\times\mathbb S^3$ with the faces
$\{v = 0\} = \mathscr I^+\cap\iota^+$ and $\{R = 0\} = K^+\cap\iota^+$, $R = v^{-1}$; the defining functions
$\rho_I = \frac v{1+v}$, $\rho_K = \frac R{1+R}$; the operator
$$N_{\iota^+}(\lambda) = -2v(v\partial_v-\lambda)\big(v\partial_v-\tfrac32-\bar S\big)+v^2\tilde L(0)(\omega,v\partial_v,
\partial_\omega),\qquad2\bar L(t_*^{-\lambda}w) = t_*^{-\lambda-2}N_{\iota^+}(\lambda)w\tag{1.1}$$
(III.G$'$ (1.1); III.G Lemma 1.2 (c)); the index set $\mathcal E_K$ at $K^+\cap\iota^+$ (III.G$'$ Definition 1.2 (3),
Lemma 1.3); the sets $\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}$, $\mathcal E^C_{\iota^+,\mathscr I}$ and
$\mathcal E_s$, $s\in\sigma_\Upsilon$, of III.G$'$ (1.5); and $\mathrm{spec}_{\iota^+}(\bar L)$,
$\mathrm{Spec}_{\iota^+}(\bar L)$ (III.G$'$ Definition 4.1). From III.G$''$ we use $\ell_K^{\max}$, the roots
$\mathcal W(\ell_K)$, the formal solutions of Lemma 2.4 and Theorem 3.1 with their s1 and v1 conventions, and Corollary
3.2. The parameters are those of III.G$'$ Theorem 3.1, with $\gamma_\Upsilon<\min(\frac12s_C,\frac14)$ (III.C (1.1)).
Let $\mathcal E^C_I$ be an index set as in III.C Definition 3.1, with its sets (3.2) and $\mathcal F_{I,11}$ (III.C
(5.1)). Fix
$$\tfrac32<\ell_I<\tfrac32+s_C,\qquad\ell_I\notin\mathrm{Re}\,\pi_1\mathcal E^{\mathrm{tot}}_I,\tag{1.2}$$
the $n = 4$ form of the source's (9.44); it includes
$\ell_I\notin\mathrm{Re}\,\pi_1\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}$, as
$\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}\subset\mathcal E^{\mathrm{tot}}_I$. And $\ell_K\in(-1,\ell_K^{\max})$,
with $\ell_K\notin\mathrm{Re}\,\pi_1\mathcal E_K$ and $\ell_K\ne-\mathrm{Re}\,\mu$ for every root $\mu$ of III.F$'$
Proposition 2.3.

*Slots on $\iota^+$.* Near $v = 0$, $\iota^+$ lies in $\{|x|\ge3R_1\}$, where the rescaled null frame of III.C (1.6) is
a smooth frame of $S^2T^*$. Its slots, with the slot coordinates III.C (1.7) and projections
$\pi_C,\pi_{01}, \pi_{1/},\slashed\pi_0,\pi_{11}$ (III.C Definition 1.2), are used on $\iota^+$ near $v = 0$. The null
frames of $\eta$, $g_\mu$ and $\bar g$ agree on $\iota^+$. III.C Lemma 1.3 is stated on its region $U$, which $\iota^+$
does not meet, but its proof uses only $|x|\ge4R_1$ and shows that the frames differ by $F_0(\omega)(I+E)$ with
$E\in|x|^{-2}C^\infty$; near $\iota^+\cap\mathscr I^+$, $|x|^{-1} = v/t_*$ vanishes at $\iota^+$. So the frames restrict
to $\iota^+$ identically, and there $\bar S$ has the constant matrix $\bar A$ of III.C Lemma 4.2 (constant in $\bar g$'s
frame). Let $e_7$ be the basis section of $\langle(dx^1)^2\rangle$.

**Definition 1.1 ([Hin26] (9.45) at n = 4).**
$H^{k,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_K,\ell_K)}_{\mathrm b}(\iota^+;S^2T^*)$ is the space of $h$ with
$h\in H^{k,(\mathcal E_K,\ell_K)}_{\mathrm b}$ near $R = 0$ and, near $v = 0$, $\pi_Ch\in(\mathcal E^C_I,\ell_I)$,
$\pi_{01}h\in(\mathcal E_{I,01},\ell_I)$, $\pi_{1/}h\in(\mathcal E_{I,1/},\ell_I)$,
$\slashed\pi_0h\in(\slashed{\mathcal E}_{I,0},\ell_I)$, $\pi_{11}h\in(\mathcal E_{I,11},\ell_I)$, each with regularity
$k$. $H^{k,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),\ell_K-2}_{\mathrm b}(\iota^+;S^2T^*)$ is the space of $f$ with
$f\in H^{k,\ell_K-2}_{\mathrm b}$ near $R = 0$ and, near $v = 0$,
$\pi_Cf,\pi_{01}f,\pi_{1/}f, \slashed\pi_0f\in(\mathcal E^C_I+1,\ell_I+1)$ and
$\pi_{11}f\in(\mathcal F_{I,11},\ell_I+1)$. The same names without the second order denote the spaces on
$[0,1)_v\times\mathbb S^3$ defined by the conditions at $v = 0$.

**Lemma 1.2 (III.G$'$'s spaces lie in these).** (1) The eigenvectors of $\bar A$ for $2\gamma_\Upsilon$,
$\gamma_\Upsilon$, $0$ and $(1-e_\Upsilon)\gamma_\Upsilon$ are supported in the slots $\{7\}$, $\{5\}$, $\{6\}$ and
$\{4,7\}$, and those for $\sigma_C$ have no component in slot 6. (2) $H^{k,(\langle\mathcal E^C_{\iota^+,\mathscr
I}\rangle,\ell_I),(\mathcal E_K,\ell_K)}_{\mathrm b}(\iota^+)$ of III.G$'$ Definition 1.2 is contained in
$H^{k,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_K,\ell_K)}_{\mathrm b}(\iota^+)$.

*Proof.* (1) $\bar A$ is lower triangular (III.C Lemma 4.2), so an eigenvector for a diagonal entry $a_{jj}$ distinct
from every other diagonal entry (all seven are distinct, as $2\gamma_\Upsilon<s_C$) has $x_i = 0$ for $i<j$, $x_j = 1$,
and $x_i$ for $i>j$ determined by $(a_{ii}-a_{jj})x_i = -\sum_{j\le m<i}a_{im}x_m$. With the support of III.C Lemma 4.2,
rows 5, 6 have no entry in column 4, rows 6, 7 none in column 5, row 7 none in column 6, and $a_{74}\ne0$; this gives
the supports. For $c\in\sigma_C$, slot 6 gives $(0-c)x_6 = 0$ (row 6 has only its diagonal). (`ext5.py` E6 checks the
supports at sample parameters, and fails with a $(7,6)$ entry; it reads $\bar A$ from `scri5.py`'s table, computed by
`scri5.py --only 1`, and does not test the claim for $\sigma_C$, which is proved here by hand.) (2) $\mathcal
E^C_{\iota^+,\mathscr I} = \mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}+1\subset \mathcal
E^{\mathrm{tot}}_I+1\subset\mathcal E^C_I$ (III.C Lemma 3.2 (a)). By (1), slot 4 of $h$ is the slot-4 part of
$\Pi_{(1-e_\Upsilon)\gamma_\Upsilon}h$ and of $\Pi_Ch$, in $\mathcal E_{(1-e_\Upsilon)\gamma_\Upsilon}\cup\mathcal
E^C_{\iota^+,\mathscr I}\subset\mathcal E_{I,01}$. In the same way slot 5 lies in
$\mathcal E_{\gamma_\Upsilon}\cup \mathcal E^C_{\iota^+,\mathscr I}\subset\mathcal E_{I,1/}$, slot 6 in
$\mathcal E_0\subset\slashed{\mathcal E}_{I,0}$, slot 7 in $\mathcal E_{2\gamma_\Upsilon}\cup\mathcal
E_{(1-e_\Upsilon)\gamma_\Upsilon}\cup\mathcal E^C_{\iota^+, \mathscr I}\subset\mathcal E_{I,11}$, and slots 1-3, which
only $\Pi_C$ reaches, in $\mathcal E^C_{\iota^+,\mathscr I} \subset\mathcal E^C_I$. $\square$

## 2. Partially polyhomogeneous inputs ([Hin26] Lemmas 9.13-9.14, Proposition 9.15, Definition 9.16, Remark 9.17)

**Lemma 2.1 ([Hin26] Lemma 9.13; no dimension enters).** Let $\mathcal E\subset\mathbb C\times\mathbb N_0$ be an index
set, $\alpha\in\mathbb R$, and $(R(\lambda)f)(x) := x^\lambda\int_0^xt^{-\lambda}f(t)\frac{dt}t$ for
$f\in\dot C^\infty([0,1])$, a right inverse of $x\partial_x-\lambda$. Then $R(\lambda)$ extends from
$\mathrm{Re}\,\lambda< \min(\alpha,\min\mathrm{Re}\,\mathcal E)$ to a finite-meromorphic family $R(\lambda):\bar
H^{k,(\mathcal E,\alpha)}_{ \mathrm b}([0,1))\to\bar H^{k+1,(\mathcal E,\alpha)}_{\mathrm b}([0,1))$ on
$\{\mathrm{Re}\,\lambda<\alpha\}$, with divisor $\{(z,k(\mathcal E,z)):z\in\pi_1\mathcal E,\ \mathrm{Re}\,z<\alpha\}$.
The same holds with values in a Hilbert space $\mathcal H$ (e.g. $H^m(\mathbb S^3)$), except that the residues are then
not of finite rank.

*Proof.* (i) $\mathcal E = \emptyset$. With $s := t/x$,
$x^{-\alpha}R(\lambda)f(x) = \int_0^1s^{\alpha-\lambda} (x s)^{-\alpha}f(xs)\frac{ds}s$, a multiplicative convolution of
$t^{-\alpha}f$ with $s^{\alpha-\lambda}1_{(0,1)}(s)$, whose $L^1(\frac{ds}s)$-norm is
$(\alpha-\mathrm{Re}\,\lambda)^{-1}$. By Young's inequality on the group $((0,\infty),\cdot)$,
$\|R(\lambda)f\|_{x^\alpha L^2(\frac{dx}x)}\le(\alpha-\mathrm{Re}\,\lambda)^{-1}\|f\|_{x^\alpha L^2(\frac{dx}x)}$, with
$f$ extended by 0 to $(1,\infty)$ and $R(\lambda)f$ restricted to $(0,1)$. From
$x\partial_xR(\lambda)f = \lambda R(\lambda)f+f$, by induction $(x\partial_x)^jR(\lambda)f$ is bounded in $x^\alpha L^2$
by $\|f\|_{\bar H^{j-1,\alpha}_{\mathrm b}}$ for $j\le k+1$. The family is holomorphic in $\lambda$, and $\dot C^\infty$
is dense. (ii) General $\mathcal E$. Write $f = \chi\sum x^z(\log x)^jf_{(z,j)}+f'$ (the source's Definition 2.8),
$f'\in\bar H^{k,\alpha}_{\mathrm b}$, and treat $f'$ by (i). For $\mathrm{Re}\,\lambda<\mathrm{Re}\,z$,
$R(\lambda)x^z = (z-\lambda)^{-1}x^z$, and differentiating in $z$,
$R(\lambda)(x^z(\log x)^j) = \partial_z^j((z- \lambda)^{-1}x^z)$ (the source's (9.46)). This is meromorphic in
$\lambda\in\mathbb C$, with a pole of order $j+1$ at $\lambda = z$, and lies in
$\bar H^{\infty,((z,j),\alpha)}_{\mathrm b}$. And $R(\lambda)((1-\chi)x^z(\log x)^j)$ vanishes near $x = 0$ and is
entire in $\lambda$. The residue at $\lambda = z$ depends only on the coefficients $f_{(z,i)}$, so it has finite rank in
the scalar case. $\square$

**Lemma 2.2 ([Hin26] Lemma 9.14 at n = 4).** Let $\ell_I$ satisfy (1.2), $l := 2\lceil\ell_I\rceil+10$, and $f\in
H^{k+l,(\langle\mathcal E^C_I+1\rangle',\ell_I+1)}_{\mathrm b}([0,1)_v\times\mathbb S^3;S^2T^*)$. There is
$u(\lambda)\in H^{k+2,(\langle\mathcal E^C_I\rangle,\ell_I)}_{\mathrm b}([0,1)_v\times\mathbb S^3)$, linear and
continuous in $f$, a finite sum $\chi_I\sum v^z(\log v)^jc_{z,j}(\lambda,\omega)$ supported in $\{v<1\}$, such that:

(1) $u$ is meromorphic in $\lambda\in\mathbb C$, with divisor contained in
$\{(z,k(\mathcal E^C_{I,\sharp},z)):z\in\pi_1 \mathcal E^C_{I,\sharp},\ \mathrm{Re}\,z<\ell_I\}$, where
$$\mathcal E^C_{I,\sharp} := (\lambda_\sharp,0)\cup\mathcal E^C_I\subset\mathcal E^{\mathrm{tot}}_I;\tag{2.1}$$

(2) away from the poles, $f-N_{\iota^+}(\lambda)u(\lambda)\in H^{k,\ell_I+1}_{\mathrm b}([0,1)_v\times\mathbb S^3)$.

Here $\chi_I\in C^\infty_c([0,1)_v)$ equals 1 on $[0,\frac12]$.

*Proof.* By (1.1), $N_{\iota^+}(\lambda)u = f$ is $(v\partial_v-\lambda)(v\partial_v-\frac32-\bar A)u+\tilde Nu = g$,
with $g := -\frac1{2v}f$ and $\tilde N := -\frac v2\tilde L(0)\in v\mathrm{Diff}^2_{\mathrm b}$. Near $v = 0$, $g$ has,
at weight $\ell_I$, the index set $\mathcal E^C_I$ in slots 1-6 and $\mathcal E^C_I\cup(\lambda_\sharp,0)$ in slot 7
(III.C Definition 5.1). Of the latter, only the term $v^{\lambda_\sharp}$ itself lies outside $\mathcal E^C_I$, since
$\lambda_\sharp+j\in\mathcal E^C_I$ for $j\ge1$ (III.C Lemma 3.2 (d)). If $f$ has no expansion at $v = 0$, take $u = 0$.

*The exceptional term.* Let $g_{\mathrm{exc}} := \chi_Iv^{\lambda_\sharp}g_\sharp(\omega)e_7$. As $e_7$ is an
eigenvector of $\bar A$ for $2\gamma_\Upsilon$ (Lemma 1.2 (1)), $w^\flat_{\mathrm{exc}} :=
(\lambda_\sharp-\frac32-2\gamma_\Upsilon)^{ -1}v^{\lambda_\sharp}g_\sharp e_7 =
-((1+e_\Upsilon)\gamma_\Upsilon)^{-1}v^{\lambda_\sharp}g_\sharp e_7$ solves
$(v\partial_v-\frac32-\bar A)w^\flat_{\mathrm{exc}} = v^{\lambda_\sharp}g_\sharp e_7$. (On all of $S^2T^*$,
$\lambda_\sharp-\frac32-\bar A$ is not invertible, as
$\lambda_\sharp-\frac32 = (1-e_\Upsilon)\gamma_\Upsilon\in \mathrm{spec}\,\bar A$; only its restriction to the line of
$e_7$ is used.) Let $w_{\mathrm{exc}}(\lambda) := (\lambda_\sharp-\lambda)^{-1}w^\flat_{\mathrm{exc}}$ (Lemma 2.1), with
a simple pole at $\lambda_\sharp$.

*The terms of $\mathcal E^C_I$.* For $(z,j)\in\mathcal E^C_I$ with $\mathrm{Re}\,z<\ell_I$:
$\mathrm{Re}\,z-\frac32\in (2\gamma_\Upsilon,s_C)$ (III.C Definition 3.1 (2) and (1.2)), and
$\mathrm{spec}\,\bar A\subset[0,2\gamma_\Upsilon]\cup [s_C,\infty)$ (III.F (3.1)). So $z-\frac32-\bar A$ is invertible,
and $w^\flat := \partial_z^j(v^z(z-\frac32-\bar A)^{-1}) c$ solves
$(v\partial_v-\frac32-\bar A)w^\flat = v^z(\log v)^jc$ for a coefficient $c(\omega)$ held fixed. Let
$w(\lambda) := (v\partial_v-\lambda)^{-1}w^\flat$, computed term by term by Lemma 2.1 (ii): meromorphic, with poles only
at $\lambda = z$, of order at most $j+1$.

*Iteration.* Solving away a term $T$ at exponent $z$ by $\chi_Iw$ leaves $-\tilde N(\chi_Iw)$ and terms supported in
$\{\frac12\le v<1\}$. As $\tilde L(0)$ is a b-operator in $(v\partial_v, \partial_\omega)$ with smooth coefficients,
$\tilde N(\chi_Iw)$ has the exponents $z+1$, with the same logarithmic orders and coefficients with the same poles in
$\lambda$, and two fewer derivatives in $\omega$. Treat the exponents in order of increasing real part. Each new
exponent lies in $\mathcal E^C_{I,\sharp}+\mathbb N\subset\mathcal E^C_I$ and has real part in
$(\frac32+2\gamma_\Upsilon,\ell_I)$ while it is to be solved away, so the invertibility above applies. There are
finitely many such exponents, since $\mathcal E^C_{I,\sharp}$ is an index set, and none has real part $\ell_I$, by
(1.2). A chain from the least exponent to $\ell_I$ has at most $\lceil\ell_I\rceil$ steps, losing at most
$2\lceil\ell_I\rceil<l-2$ derivatives. The remaining terms have real part above $\ell_I$ and lie in
$H^{k,\ell_I}_{\mathrm b}$ at the level of $g$, so in $H^{k,\ell_I+1}_{\mathrm b}$ at that of $f$. (`ext5.py` E7,
bookkeeping: it generates the exponents from $\mathcal E^C_I$ and $(\lambda_\sharp,0)$ by the $+1$-closure, so that they
lie in $\mathcal E^C_{I,\sharp}$ holds by construction; what it checks, for four samples, is that $z-\frac32$ avoids
$\mathrm{spec}\,\bar A$ off $\lambda_\sharp$ and that $\lambda_\sharp$ is the least.) The poles: at each $z$, the
solving step contributes order at most $j+1\le k(\mathcal E^C_{I,\sharp},z)+1$, and the coefficients carried from lower
exponents $z'$ have poles only at those $z'$. So the divisor is as stated. $u$ lies in $\langle\mathcal E^C_I\rangle$:
the exceptional term sits in slot 7 at $\lambda_\sharp\in\mathcal E_{I,11}$, and all other exponents are in
$\mathcal E^C_I$. $\square$

**Lemma 2.3 (uniqueness below the least exponent).** Let
$h\in H^{k,(\langle\mathcal E^C_I\rangle,\ell_I),\beta}_{ \mathrm b}(\iota^+)$ with $\beta\in(-1,0)$ and
$k\ge k_0(\mathrm{Re}\,z)$, the regularity III.G$'$ Theorem 3.1 (2) needs at $z$ (it depends on $\mathrm{Re}\,z$ through
III.G$'$'s loss $d$). Then $N_{\iota^+}(z)h\in H^{k-2,(\langle\mathcal E^C_I+1\rangle', \ell_I+1),\beta-2}_{\mathrm b}$
for every $z$. Let $w_0$ be a lower bound for the real parts of the exponents of $h$ at $v = 0$, let
$\mathrm{Re}\,z<\ell'\le w_0$, let $z$ not be a pole of III.G$'$'s inverse (all uses below have $\mathrm{Re}\,z<2$,
where it has none, III.G$'$ Lemma 4.2 (a)), and suppose $N_{\iota^+}(z)h$ lies in the domain
$H^{k-2,\ell'+1,\beta-2}_{\mathrm b}$ of III.G$'$ Theorem 3.1 (2) with $\ell'$ for its $\ell_I$. Then
$N_{\iota^+}(z)^{-1}N_{\iota^+}(z)h = h$, with III.G$'$'s inverse. For $h$ as above, $w_0 = \frac32$ and any
$\ell'\in(\mathrm{Re}\,z,\frac32)$ serve when $\mathrm{Re}\,z<\frac32$, the exponents of $N_{\iota^+}(z)h$ being at
least $\lambda_\sharp+1>\frac52$.

*Proof.* The mapping property near $v = 0$ is the leading-part computation of III.C Proposition 5.2, with $v\partial_v$
for $X_I$ and the factor $(v\partial_v-z)$ preserving index sets, together with $v^2\tilde L(0)$ mapping
$\mathcal E^{\mathrm{tot}}_I$ into $\mathcal E^{\mathrm{tot}}_I+2\subset\mathcal E^C_I+1$ (III.C Lemma 3.2 (c)). Near
$R = 0$, $N_{\iota^+}(z)\in R^{-2}\mathrm{Diff}^2_{\mathrm b}$ (III.G$'$ (1.3)). For the identity: every exponent $w$ of
$h$ at $v = 0$ has $\mathrm{Re}\,w\ge w_0>\mathrm{Re}\,z$. So $R^zh = v^{-z}h$, extended by 0 to $\{v<0\}$, is a sum of
terms $v_+^{w-z}c(\omega)$ ($\log$ powers allowed), $\mathrm{Re}(w-z)>0$, and a remainder of positive order; these lie
in $H^{s}$ near $v = 0$ for every $s<\frac12+\mathrm{Re}(w-z)$, and are b-regular there. With III.G$'$'s admissible
choice $s = \min(\frac12,2-\mathrm{Re}\,z)-\delta$ and $\mu$ (Step 5 (ii) of its proof, with $\ell_K = \beta>-1$),
$R^zh$ lies in the space on which $N_{\mathrm{sf}}(z)$ is invertible (III.G Theorem 5.1). Since $v_+^{w-z}$ is
continuous at $v = 0$, the derivative across $v = 0$ creates no term supported there, so $N_{\mathrm{sf}}(z)(R^zh)$ is
the extension by 0 of $R^{2+z}N_{\iota^+}(z)h$. By (3.1) of III.G$'$,
$N_{\iota^+}(z)^{-1}N_{\iota^+}(z)h = R^{-z}N_{\mathrm{sf}}(z)^{-1} N_{\mathrm{sf}}(z)R^zh = h$. $\square$

**Proposition 2.4 ([Hin26] Proposition 9.15 at n = 4).** Let $\ell_I$, $\ell_K$ be as in section 1. The map
$N_{\iota^+}(\lambda)^{-1}$ of III.G$'$ Theorem 3.1, on the space of Definition 1.1, extends from
$\{\mathrm{Re}\,\lambda<\lambda_\sharp\}$ to a meromorphic family
$$N_{\iota^+}(\lambda)^{-1}:H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),\ell_K-2}_{\mathrm b}(\iota^+)\to
H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_K,\ell_K)}_{\mathrm b}(\iota^+),\qquad\mathrm{Re}\,\lambda<
\ell_I,\tag{2.2}$$
which inverts $N_{\iota^+}(\lambda)$ ($N_{\iota^+}(\lambda)N_{\iota^+}(\lambda)^{-1}f = f$). Its poles lie in
$\mathrm{spec}_{\iota^+}(\bar L)\cup\pi_1\mathcal E^C_{I,\sharp}$, and the order of a pole $\lambda_0$ is at most
$m_\iota(\lambda_0)+m_\sharp(\lambda_0)$, where $m_\iota$ is the order of the pole of III.G$'$'s (3.3) at $\lambda_0$ (0
if none) and $m_\sharp(\lambda_0) := k(\mathcal E^C_{I,\sharp},\lambda_0)+1$ (0 if
$\lambda_0\notin\pi_1\mathcal E^C_{I,\sharp}$). At finite regularity: for every $\epsilon>0$ and
$\lambda_-<\ell_I-\epsilon$ there is $l'$ such that (2.2) holds from $H^{k+l'}$ to $H^k$ on
$\{\lambda_-<\mathrm{Re}\,\lambda<\ell_I-\epsilon\}$ for every $k$.

*Proof.* Given $f$, let $u(\lambda)$ be as in Lemma 2.2 for $f$ near $v = 0$ (it already carries the cut-off $\chi_I$;
the second cut-off below changes nothing, $\chi_I^2$ having the same properties), and set
$f'(\lambda) := f-N_{\iota^+}(\lambda)(\chi_Iu(\lambda))$. Near $v = 0$ this is Lemma 2.2 (2), up to terms supported in
$\{\frac12\le v<1\}$; for $v\ge1$ it equals $f$. So $f'(\lambda)\in H^{\infty,\ell_I+1,\ell_K-2}_{\mathrm b}(\iota^+)$,
meromorphic with the poles of $u$. Let $u'(\lambda) := N_{\iota^+}(\lambda)^{-1}f'(\lambda)$ by III.G$'$ Theorem 3.1
(2), finite-meromorphic on $\{\mathrm{Re}\,\lambda<\ell_I\}$, in $H^{\infty,(\langle\mathcal E^C_{\iota^+,\mathscr
I}\rangle,\ell_I),(\mathcal E_K,\ell_K)}_{\mathrm b}$, which lies in the target by Lemma 1.2 (2). Then
$N_{\iota^+}(\lambda)(\chi_Iu+u') = f$, and $\chi_Iu+u'$ is in the target space. The poles: those of $u$ (Lemma 2.2
(1)), and those of $u'$, which come from $f'$ and from III.G$'$'s inverse; at $\lambda_0$ the Laurent orders add, giving
the bound. *Agreement below $\lambda_\sharp$.* For $\mathrm{Re}\,\lambda<\lambda_\sharp$ all exponents of $f$ at $v = 0$
are at least $\lambda_\sharp+1$, so $f$ lies in III.G$'$'s domain with $\ell' := \lambda_\sharp-\delta$, and
$u(\lambda)$ is holomorphic there. By Lemma 2.3 with $w_0 = \lambda_\sharp$, the least exponent of $\chi_Iu$, and
$\ell'\in(\mathrm{Re}\,\lambda,\lambda_\sharp)$, $N^{-1}N(\chi_Iu) = \chi_Iu$, so
$\chi_Iu+u' = N^{-1}(N\chi_Iu+f') = N^{-1}f$. *Finite regularity.* III.G$'$'s loss $d$ depends on $\lambda$ only through
$\mathrm{Re}\,\lambda$: through the regularity $s$ and the number of steps, at most
$\lceil\ell_I-\mathrm{Re}\,\lambda\rceil+2$, each losing two derivatives (Step 5 (ii)-(iii) of its proof). Near each
value of $\mathrm{Re}\,\lambda$ one $s$ serves, its condition $s<\min(\frac12,2-\mathrm{Re}\,\lambda)$ being open; so
$d$ is locally bounded in $\mathrm{Re}\,\lambda$, hence bounded on $[\lambda_-,\ell_I-\epsilon]$, and $l' := l+\sup d$
serves. $\square$

**Definition 2.5 ([Hin26] Definition 9.16).**
$\mathrm{spec}^{<\ell_I}_{\iota^+}(\bar L,\mathcal E^C_I)\subset\{\mathrm{Re} \,\lambda<\ell_I\}$ is the set of poles of
(2.2), and $\mathrm{Spec}^{<\ell_I}_{\iota^+}(\bar L,\mathcal E^C_I)$ the set of $(\lambda,k)$ with $\lambda$ a pole of
order $k+1$.

**Corollary 2.6 ([Hin26] (9.49) at n = 4).** If $\lambda_\sharp<\ell_I$, then
$(\lambda_\sharp,0)\in\mathrm{Spec}^{< \ell_I}_{\iota^+}(\bar L,\mathcal E^C_I)$. Every other element of
$\mathrm{spec}^{<\ell_I}_{\iota^+}(\bar L,\mathcal E^C_I)$ has real part greater than $\frac32+2\gamma_\Upsilon$, and
none has real part below $\lambda_\sharp$.

*Proof.* $\mathrm{spec}_{\iota^+}(\bar L)\subset\{\mathrm{Re}\ge2\}$ (III.G$'$ Lemma 4.2 (a)), and
$\pi_1\mathcal E^C_{I,\sharp}\subset\{\lambda_\sharp\}\cup\{\mathrm{Re}>\frac32+2\gamma_\Upsilon\}$, with
$\lambda_\sharp<\frac32+2 \gamma_\Upsilon<2$. The order at $\lambda_\sharp$ is at most $0+1$, as
$\lambda_\sharp\notin\pi_1\mathcal E^C_I$. It is a pole: take $f$ with only the exceptional term, $g_\sharp\ne0$. The
residue of $\chi_Iu$ at $\lambda_\sharp$ has the term $-\chi_Iw^\flat_{\mathrm{exc}}$, a non-zero multiple of
$v^{\lambda_\sharp}g_\sharp e_7$, and its other terms have exponents $\lambda_\sharp+j$, $j\ge1$. The residue of $u'$ is
$N_{\iota^+}(\lambda_\sharp)^{-1}$ of the residue of $f'$ (III.G$'$'s inverse is holomorphic at $\lambda_\sharp<2$), so
it lies in III.G$'$'s space, where its $\Pi_{2\gamma_\Upsilon}$-component has index set
$\mathcal E_{2\gamma_\Upsilon} = \mathcal E^C_{\iota^+,\mathscr I}\cup(\frac32+2\gamma_\Upsilon,0)$, which does not
contain $\lambda_\sharp$ ($\mathcal E^C_{\iota^+,\mathscr I}$ starts at $\frac52$). As
$\Pi_{2\gamma_\Upsilon}e_7 = e_7$, the $\Pi_{2\gamma_\Upsilon}$-component of the residue of $\chi_Iu+u'$ has a non-zero
$v^{\lambda_\sharp}$-term. (Slot 7 alone would not do: it also receives the
$(1-e_\Upsilon)\gamma_\Upsilon$-eigenvector's component, Lemma 1.2 (1).) $\square$

At the exponent itself the agreement of Proposition 2.4 stops for a reason worth recording:
$R^{\lambda_\sharp} (v^{\lambda_\sharp}e_7)$ extended by 0 is $v_+^0e_7$, and
$N_{\mathrm{sf}}(\lambda_\sharp) = -2\partial_v(v\partial_v+ \lambda_\sharp-\frac32-\bar S)+\ldots$ applied to it
produces $-2\delta(v)(\lambda_\sharp-\frac32-2\gamma_\Upsilon)e_7\ne0$ at the light cone. So $v^{\lambda_\sharp}e_7$ is
not the image of III.G$'$'s inverse, whose outputs carry no incoming term (III.G$'$ Theorem 3.1 (1)).

**Remark 2.7 ([Hin26] Remark 9.17 at n = 4).** Let $(\alpha,0)\in\mathcal E^C_I$ with
$\frac32+2\gamma_\Upsilon<\alpha< \ell_I$, $\alpha\notin\mathrm{spec}_{\iota^+}(\bar L)$ and
$\alpha\notin\pi_1\mathcal E^C_{\iota^+,\mathscr I}\cup(\frac32+\sigma_\Upsilon+\mathbb N_0)$, and
$f := \chi_Iv^{\alpha+1}f_0(\omega)$, $f_0\ne0$. Then $N_{\iota^+} (\lambda)^{-1}f$ has a simple pole at
$\lambda = \alpha$: as in Corollary 2.6, the residue's $v^\alpha$-term, a non-zero multiple of
$(\alpha-\frac32-\bar A)^{-1}f_0$, cannot be cancelled by the residue of $u'$, whose exponents lie in
$\pi_1\mathcal E^C_{\iota^+,\mathscr I}\cup(\frac32+\sigma_\Upsilon+\mathbb N_0)$. In the language of scattering, the
residue solves the problem at frequency $\alpha$ with incoming data $v^\alpha u_0$,
$u_0 = (\alpha-\frac32-\bar A)^{-1}(\frac12f_0)$ (the residue of $(\alpha-\lambda)^{-1}w^\flat$ is $-w^\flat$, and
$g = -\frac1{2v}f$), and its outgoing data are its radiation fields at $\frac32+\mathrm{spec}\,\bar A$. So
$\mathcal E^C_I$ specifies the frequencies at which incoming data are allowed.

## 3. Quasi-homogeneous solutions and resonant states ([Hin26] Corollary 9.18 to Remark 9.24)

**Corollary 3.1 ([Hin26] Corollary 9.18 at n = 4).** Let $\mathrm{Re}\,\lambda_0<\ell_I$, $J\in\mathbb N_0$, and
$$f = \sum_{j=0}^Jt_*^{-\lambda_0-2}(\log t_*)^jf^{(\lambda_0+2,j)}(R,\omega),\qquad f^{(\lambda_0+2,j)}\in
H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),\ell_K-2}_{\mathrm b}(\iota^+).\tag{3.1}$$
Let $K$ be the order of the pole of (2.2) at $\lambda_0$ (0 if none). Then:

(1) (*Existence.*) There is a solution of $2\bar Lu = f$, linear in $f$, of the form
$$u = \sum_{j=0}^{J+K}t_*^{-\lambda_0}(\log t_*)^ju^{(\lambda_0,j)}(R,\omega),\qquad u^{(\lambda_0,j)}\in H^{\infty,
(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_K,\ell_K)}_{\mathrm b}(\iota^+).\tag{3.2}$$

(2) (*Expansion at $R = 0$.*) $u = \chi_Ku_0+\tilde u$, with $\chi_K$ the cut-off of III.G$''$ section 4 restricted to
$\iota^+$ (the formal solutions grow as $R\to\infty$), $u_0$ a sum of III.G$''$'s formal solutions (its (3.1) and Lemma
2.4 (b), with the s1 and v1 conventions) with $t_*^{-\lambda}$ replaced by $t_*^{-\lambda_0}(\log t_*)^j$, $j\le J+K$,
and $\tilde u$ a sum of terms $t_*^{-\lambda_0}(\log t_*)^jH^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),
\ell_K}_{\mathrm b}(\iota^+)$. This holds for every solution of the form (3.2) of $2\bar Lu = f$ with $f$ as in (3.1)
(with $J+K$ for $J$).

*Proof.* (1) After scalar factors, $f = \frac1{2\pi i}\oint t_*^{-\lambda-2}\sum_j(\lambda-\lambda_0)^{-j-1}
f^{(\lambda_0+2,j)}\,d\lambda$ over a small circle around $\lambda_0$, and $u := \frac1{2\pi i}\oint t_*^{-\lambda}
\sum_j(\lambda-\lambda_0)^{-j-1}N_{\iota^+}(\lambda)^{-1}f^{(\lambda_0+2,j)}\,d\lambda$ is defined by Proposition 2.4,
with a pole of the integrand of order at most $J+1+K$ at $\lambda_0$. By (1.1),
$2\bar L(t_*^{-\lambda}w) = t_*^{-\lambda-2}N_{\iota^+}(\lambda)w$, so $2\bar Lu = f$, and the residue expands into
(3.2). (2) As the source. Near $R = 0$ the top term satisfies
$N_{\iota^+}(\lambda_0)u^{(\lambda_0,J)}\in H^{\infty,\ell_K-2}_{\mathrm b}$, so by III.G$''$ Theorem 3.1 it is a sum of
formal solutions modulo $H^{\infty,\ell_K}_{\mathrm b}$. Each such term is removed by subtracting its
$(\log t_*)^J$-version, the formal solution of III.G$''$ with argument $t_*^{-\lambda_0+\mu}(\log t_*)^JY$. Since
$t_*^{-\lambda}(\log t_*)^J = (-\partial_\lambda)^J t_*^{-\lambda}$ and the errors of III.G$''$'s formal solutions,
$t_*^{-\lambda-2}R^{-\mu+k_\mu-1}C^\infty$ (its Theorem 3.1's proof), depend holomorphically on $\lambda$, the
subtracted term's error lies in $\sum_{j\le J}t_*^{-\lambda_0-2} (\log t_*)^jH^{\infty,\ell_K-2}_{\mathrm b}$ near
$R = 0$, as $-\mu+k_\mu-1\ge1>\ell_K-2$. Then induct downwards on $j$: if
$u^{(\lambda_0,j)}\in H^{\infty,\ell_K}_{\mathrm b}$ for $j>j_0$, the coefficient of
$t_*^{-\lambda_0-2} (\log t_*)^{j_0}$ in $2\bar Lu$ gives
$N_{\iota^+}(\lambda_0)u^{(\lambda_0,j_0)}-(j_0+1)\partial_\lambda N_{\iota^+} (\lambda_0)u^{(\lambda_0,j_0+1)}\in
H^{\infty,\ell_K-2}_{\mathrm b}$, as $N_{\iota^+}$ is linear in $\lambda$. Here $\partial_\lambda N_{\iota^+} =
2v(v\partial_v-\frac32-\bar S)\in R^{-1}\mathrm{Diff}^1_{\mathrm b}$, so the second term lies in
$H^{\infty,\ell_K-1}_{\mathrm b}$, and the first step applies to $u^{(\lambda_0,j_0)}$. $\square$

**Definition 3.2 ([Hin26] Definition 9.19 at n = 4).** For $\mathrm{Re}\,\lambda<\ell_I$ and
$k\in\mathbb N_0\cup \{\infty\}$,
$$\mathrm{Res}^k_{\iota^+}(\bar L,\mathcal E^C_I,\lambda) := \Big\{u = \sum_{j=0}^Kt_*^{-\lambda}(\log t_*)^ju^{(\lambda,
j)}(v,\omega):\bar Lu = 0,\ u^{(\lambda,j)}\in H^{k,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_K,\ell_K)}_{\mathrm
b}(\iota^+),\ K\in\mathbb N_0\Big\}.\tag{3.3}$$
So the solution of Corollary 3.1 is unique modulo $\mathrm{Res}^\infty_{\iota^+}(\bar L,\mathcal E^C_I,\lambda_0)$.

**Remark 3.3 ([Hin26] Remark 9.20 at n = 4).** The proof of Corollary 3.1 (2) applies to the elements of (3.3), for
every $\ell_K<\ell_K^{\max}$ allowed in section 1: it describes their asymptotics as $R\to0$ modulo $O(R^{\ell_K})$. By
Remark 2.7, (3.3) depends on $\mathcal E^C_I$, and it is infinite-dimensional, the incoming data being sections over
$\mathbb S^3$ (Definition 3.6 and Proposition 3.7).

**Lemma 3.4 (left inverse).** Let $\beta\in(-1,0)$. For
$h\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta}_{\mathrm b}(\iota^+)$,
$N_{\iota^+}(z)^{-1}N_{\iota^+}(z)h = h$ as meromorphic functions on $\{\mathrm{Re}\,z< \ell_I\}$, with (2.2) for
$\ell_K = \beta$. For finite $k$ the same holds on every strip $\{\lambda_-<\mathrm{Re}\,z<\ell_I-\epsilon\}$,
$\lambda_-<\frac32$, when $h$ has b-regularity $k\ge l'(\lambda_-,\epsilon)+2$, with $l'$ of Proposition 2.4.

*Proof.* $\beta$ is admissible in section 1: $\mathcal E_K\subset\{\mathrm{Re}\ge0\}$, and no root of III.F$'$
Proposition 2.3 has real part in $(0,1)$. So $(\mathcal E_K,\beta)$ is the weight $\beta$ alone, and $N_{\iota^+}(z)h$
lies in the domain of (2.2) by Lemma 2.3's mapping property. Both sides are meromorphic in $z$. For
$\mathrm{Re}\,z<\frac32$ they agree by Lemma 2.3, as $N(z)h$ then has exponents above $\frac52$ at $v = 0$, so it lies
in III.G$'$'s domain with some $\ell'\in(\mathrm{Re}\,z,\frac32)$, and (2.2) agrees there with III.G$'$'s inverse
(Proposition 2.4). By the identity theorem they agree on the connected set $\{\mathrm{Re}\,z<\ell_I\}$ off the poles; at
finite $k$, on the strip, which off the poles is connected and meets $\{\mathrm{Re}\,z<\frac32\}$. $\square$

**Lemma 3.5 ([Hin26] Lemma 9.21 at n = 4).** $\mathrm{Res}^k_{\iota^+}(\bar L,\mathcal E^C_I,\lambda)$ does not depend
on the choice of $\ell_K$. For $k = \infty$ it is the space of the tensors
$$\mathrm{res}_{z=\lambda}\big(t_*^{-z}N_{\iota^+}(z)^{-1}f(z)\big),\tag{3.4}$$
$f$ a polynomial in $z$ with values in
$H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),\beta-2}_{\mathrm b}(\iota^+)$, $\beta\in(-1,0)$ arbitrary. For
finite $k$ it is contained in (resp. contains) the space of such tensors with $f$ of b-regularity $k-l'$ (resp. $k+l'$),
$l'$ as in Proposition 2.4 on a strip containing $\lambda$.

*Proof.* Independence of $\ell_K$: by Remark 3.3 the elements have the expansion of Corollary 3.1 (2) at $R = 0$ for
every allowed $\ell_K$. The tensor (3.4) is annihilated by $2t_*^2\bar L$: writing the residue as
$\frac1{2\pi i} \oint$, this gives $\frac1{2\pi i}\oint t_*^{-z}f(z)\,dz = 0$, $f$ being holomorphic; and by (2.2) it
has the form (3.3). Conversely let $u = \sum_{j\le K}t_*^{-\lambda}(\log t_*)^ju^{(\lambda,j)}$ be in (3.3). After
scalar factors, $u = \frac1{2\pi i}\oint t_*^{-z}\tilde u(z)\,dz$ with
$\tilde u(z) := \sum_j(z-\lambda)^{-j-1}u^{(\lambda,j)}$, and $\bar Lu = 0$ says that
$\mathrm{res}_{z=\lambda}(t_*^{-z-2}N_{\iota^+}(z)\tilde u(z)) = 0$ for all $t_*$, so $N_{\iota^+}(z)\tilde u(z)$ is
holomorphic at $\lambda$. Let $f(z)$ be its Taylor polynomial at $\lambda$ of degree $K(\lambda)$, the order of the pole
of (2.2) at $\lambda$. By the independence just shown, take $\ell_K\in(0,\ell_K^{\max})$. Then near $R = 0$,
$u^{(\lambda,j)}\in H^{k,-\epsilon}_{\mathrm b}$ for every $\epsilon>0$
($\mathcal E_K\cap\{\mathrm{Re} = 0\} = \{(0,0)\}$, III.G$'$ Lemma 1.3 (b)), so with $\beta := -\epsilon$ and Lemma
2.3's mapping property, $f$ takes values in $H^{k-2,(\langle\mathcal E^C_I+1\rangle',\ell_I+1), \beta-2}_{\mathrm b}$.
By Lemma 3.4 (for finite $k$, on a strip containing $\lambda$), $N(z)^{-1}N(z)\tilde u(z) = \tilde u(z)$, and
$N(z)^{-1}(N(z)\tilde u(z)-f(z))$ is holomorphic at $\lambda$, its argument vanishing to order $K(\lambda)+1$ there. So
$u = \mathrm{res}_{z=\lambda}(t_*^{-z} \tilde u(z)) = \mathrm{res}_{z=\lambda}(t_*^{-z}N(z)^{-1}f(z))$. $\square$

**Definition 3.6 ([Hin26] (9.54)-(9.55) at n = 4).** For $\mathrm{Re}\,\lambda<\ell_I$,
$\mathrm{Res}_{\iota^+}(\bar L,\lambda)$ is the space of tensors (3.4) with $f$ a polynomial with values in
$H^{k,\ell_I+1,\beta-2}_{\mathrm b}$. By the finite-meromorphy of III.G$'$ Theorem 3.1 (2) it is finite-dimensional,
consists of tensors of infinite b-regularity, and does not depend on $k$; it lies in
$\mathrm{Res}^\infty_{\iota^+}(\bar L,\mathcal E^C_I,\lambda)$. The quotient $H^{k,(\langle\mathcal
E^C_I+1\rangle',\ell_I+1),\beta-2}_{\mathrm b}/H^{k,\ell_I+1,\beta-2}_{\mathrm b}$ is identified with
$$H^{k,(\langle\mathcal E^C_I+1\rangle',\le\ell_I+1)}_{\mathrm b} := \Big\{\chi_I\Big(f^{(\lambda_\sharp+1,0)}_{11}
v^{\lambda_\sharp+1}e_7+\sum_{(\nu,j)\in\mathcal E^C_I+1,\ \mathrm{Re}\,\nu\le\ell_I+1}v^\nu(\log v)^jf^{(\nu,j)}(\omega)
\Big)\Big\},\tag{3.5}$$
$f^{(\lambda_\sharp+1,0)}_{11}\in H^k(\mathbb S^3)$, $f^{(\nu,j)}\in H^k(\mathbb S^3;S^2T^*)$: finitely many copies of
$H^k(\mathbb S^3)$. The first term is present only if $\lambda_\sharp<\ell_I$; otherwise $v^{\lambda_\sharp+1}e_7$ lies
in $H^{k,\ell_I+1}_{\mathrm b}$. The source's (9.55) has two exceptional terms, $v^2$ and
$v^{2+(1-e_\Upsilon)\gamma_\Upsilon}$ in the $(dx^1)^2$-component; here there is one.

**Proposition 3.7 ([Hin26] Proposition 9.22 at n = 4).** Let $\mathrm{Re}\,\lambda<\ell_I$, $K(\lambda)$ the order of
the pole of (2.2) at $\lambda$, and $\mathrm{Poly}^K(\mathbb C_z;X)$ the polynomials of degree at most $K$ with
coefficients in $X$. There is $l = l(\ell_I,\lambda)$ such that for $k\ge l$ the map
$$\mathrm{Res}_{\iota^+}(\bar L,\lambda)\oplus\mathrm{Poly}^{K(\lambda)}\big(\mathbb C_z;H^{k,(\langle\mathcal E^C_I+1
\rangle',\le\ell_I+1)}_{\mathrm b}\big)\to\mathrm{Res}^{k-l}_{\iota^+}(\bar L,\mathcal E^C_I,\lambda),\quad(u_0,f)\mapsto
u_0+\mathrm{res}_{z=\lambda}\big(t_*^{-z}N_{\iota^+}(z)^{-1}f(z)\big),\tag{3.6}$$
defined independently of $k$, is well defined and continuous, and
$\mathrm{Res}^k_{\iota^+}(\bar L,\mathcal E^C_I,\lambda)$ lies in the range of the map for $k-l$ in place of $k$. There
is a right inverse for $k = \infty$ which is continuous from $\mathrm{Res}^k$ to the domain with $k-l$ for every $k$.

*Proof.* Well-definedness and continuity: Proposition 2.4 on a strip containing $\lambda$, and (3.5) as a subspace of
the domain of (2.2). The proof of Lemma 3.5 gives a map $u\mapsto f\in\mathrm{Poly}^{K(\lambda)}(\mathbb
C;H^{k-l,(\langle \mathcal E^C_I+1\rangle',\ell_I+1),\beta-2}_{\mathrm b})$ with $u = \mathrm{res}(t_*^{-z}N^{-1}f)$,
$\beta\in(-1,0)$ fixed, defined independently of $k$. Split $f = f_1+f_2$ uniquely, $f_1$ with values in
$H^{k-l,\ell_I+1,\beta-2}_{\mathrm b}$ and $f_2$ in (3.5): $f_2$ is the finite expansion of $f$ at $v = 0$ cut off by
$\chi_I$. The right inverse is $u\mapsto(\mathrm{res}(t_*^{-z}N^{-1}f_1),f_2)$, the first component in
$\mathrm{Res}_{\iota^+}(\bar L,\lambda)$ by Definition 3.6. $\square$

So (3.6) parametrises the quasi-homogeneous nullspace by a finite-dimensional piece of pure resonant states (no incoming
data) and an infinite-dimensional piece of finite description that encodes incoming data through the sources.

**Remark 3.8 ([Hin26] Remark 9.23 at n = 4).** (3.6) over-parametrises. At $\lambda = \lambda_\sharp$ (when
$\lambda_\sharp<\ell_I$), the $n = 4$ counterpart of the source's $\lambda = 1$:
$\mathrm{Res}_{\iota^+}(\bar L,\lambda_\sharp) = \{0\}$, as $\lambda_\sharp<2$ (III.G$'$ Lemma 4.2 (a)), and
$N_{\iota^+}(z)^{-1}f$ has no pole at $z = \lambda_\sharp$ unless $f^{(\lambda_\sharp+1,0)}_{11}\ne0$ in (3.5): the
other terms of (3.5) have exponents in $\mathcal E^C_I+1$, whose poles lie in $\pi_1\mathcal E^C_I$ (Lemma 2.2), and
$\lambda_\sharp\notin\pi_1\mathcal E^C_I$.

**Remark 3.9 ([Hin26] Remark 9.24 at n = 4).** Let $\lambda\in\mathrm{spec}^{<\ell_I}_{\iota^+}(\bar L,\mathcal E^C_I)
\setminus\mathrm{spec}_{\iota^+}(\bar L)$ (e.g. $\lambda = \lambda_\sharp$) and $u := (3.6)(0,f)\ne0$. $N_{\iota^+}$ is
$SO(4)$-equivariant, so it preserves the components of each harmonic degree (III.A$'$ section 1). The formal solutions
at $R = 0$ below $\ell_K^{\max}$ occur only at the roots of Table 1.1 of III.G$''$, whose types have degree at most 4
(s4 at $-2$). So if $f$ has only harmonic components of degree $\ge5$, the expansion of $u$ at $R = 0$ is trivial modulo
$O(R^{\ell_K})$ for every $\ell_K<\ell_K^{\max}$. Even an arbitrarily high finite order of vanishing at $R = 0$ thus
leaves an infinite-dimensional space of non-pure resonant states. (The source: degree $\le5$, $l\ge6$.)

## 4. Findings, labels and sources

### 4.1 Findings

(G$'''$1) *The least incoming pole at $n = 4$ is $\lambda_\sharp = \frac32+(1-e_\Upsilon)\gamma_\Upsilon$, simple*
(Corollary 2.6). The source's (9.49) puts $(1,0)$ in the boundary spectrum, from the radiation field's coupling into the
$(dx^1)^2$-component and from the mass term; at $n = 4$ both land in $\mathcal E^C_I$ (III.C (C3)) and give no pole.
Every other pole of (2.2) has real part above $\frac32+2\gamma_\Upsilon$. The pole at $\lambda_\sharp<2$ is excited only
by sources with an exceptional term $v^{1+\lambda_\sharp}e_7$ at $\mathscr I^+\cap\iota^+$. Such a term arises exactly
when $\Pi_{2\gamma_\Upsilon}h$ carries a $v^{\lambda_\sharp}$ term, that is, when the $v^{\lambda_\sharp}$ parts of
slots 4 and 7 of $h$ are not in the ratio of the $(1-e_\Upsilon)\gamma_\Upsilon$-eigenvector (Lemma 1.2 (1)): by III.C
Proposition 5.2's proof, slot 7 of $(X_I-\frac32-\bar A)h$ at $v^{\lambda_\sharp}$ is
$-(1+e_\Upsilon)\gamma_\Upsilon c_7-\bar A_{74}c_4$, which vanishes along that eigenvector. $\mathcal E_{I,11}$ allows
such a term, and III.G$'$'s space does not. The record treats incoming terms below 2 (N1STAR-PROOF.md 10.38 (d)): on its
readings (quadratic sources, data with no incoming term below 2, forced terms entering at 2, nothing below 2 fed from
$K^+$) the channel is closed, since the pole needs a source at frequency exactly $\lambda_\sharp$. What remains open is
a reading: the source's section 12 also has linear grafting errors, at $\iota^+$-index set
$\lambda_0+2+\mathcal E_{\mathrm{ind}}$ (III.G$''$ (4.4)-(4.5)), and whether any of them reaches frequency
$\lambda_\sharp$ with an exceptional $\mathscr I^+$-term is for Part III.J. III.G$''$'s conditional window ((G$''$1))
asks the least grafted order to exceed $1+\max(\epsilon_K,\epsilon_{\mathrm{ind}})$; $\lambda_\sharp>\frac32$ satisfies
it when $\epsilon_K,\epsilon_{\mathrm{ind}}\le\frac12$ (at the record's parameters
$\epsilon_{\mathrm{ind}}<3\times10^{-6}$, III.F$'$ Proposition 2.3 (f)).

(G$'''$2) *The identification below $\lambda_\sharp$ is proved* (Proposition 2.4, Lemma 2.3), by uniqueness in III.G's
admissible spaces: the extension by zero of $v_+^{w-\lambda}$, $\mathrm{Re}(w-\lambda)>0$, lies in them and creates no
term at the light cone. The source states only that (9.48) "extends from $\mathrm{Re}\,\lambda<1$". At the incoming
exponent itself the extension by zero creates $\delta(v)$, which is why $\lambda_\sharp$ is a pole.

(G$'''$3) *The left inverse* (Lemma 3.4), used without statement in the source's proof of Lemma 9.21, is proved by
continuation from $\{\mathrm{Re}\,z<\frac32\}$.

(G$'''$4) *Regularity.* III.G$'$'s loss $d$ grows as $\mathrm{Re}\,\lambda$ decreases, so the finite-regularity forms of
(2.2) and (3.6) hold on bounded strips $\{\lambda_-<\mathrm{Re}\,\lambda<\ell_I-\epsilon\}$; at infinite regularity they
hold on the whole half plane. The local boundedness of $d$ is read from III.G$'$'s proof.

(G$'''$5) *The conditions on $\ell_I$ and $\ell_K$.* $\ell_I$ also avoids
$\mathrm{Re}\,\pi_1\mathcal E^{\mathrm{tot}}_I$ (III.G$'$ Theorem 3.1 (2), and the termination of Lemma 2.2), and
$\ell_K\in(-1,\ell_K^{\max})$ in place of the source's $(-\epsilon_{\mathrm{ind}},3+\epsilon_{\mathrm{ind}})$. Remark
3.9's degree bound is 4 (the source's 5).

### 4.2 Labels

Proved: Lemmas 1.2, 2.1-2.3, 3.4-3.5, Proposition 2.4, Corollaries 2.6 and 3.1, Proposition 3.7, Remarks 2.7, 3.3,
3.8-3.9, given the parts cited. Computed (exact): `ext5.py` E6, with a control (reading `scri5.py`'s table, computed by
`scri5.py --only 1`), and E3 for $\bar A$'s support; `ext5.py` E7 is bookkeeping (Lemma 2.2's proof). READ: the source's
statements quoted from pp. 180-186. Inputs: III.C (Definitions 1.2, 3.1, 5.1, Lemmas 3.2, 4.2, Proposition 5.2); III.G
(Theorem 5.1, the admissible spaces); III.G$'$ ((1.1)-(1.5), Lemma 1.1, Definition 1.2, Lemma 1.3, Theorem 3.1 with its
proof's Step 5, Definition 4.1, Lemma 4.2); III.G$''$ (Table 1.1, Lemma 2.4, Theorem 3.1, Corollary 3.2); III.F (3.1);
III.F$'$ Proposition 2.3; III.A$'$ section 1.

### 4.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 9.1.3, pp. 180-186
((9.44)-(9.56), Lemmas 9.13-9.14, Proposition 9.15, Definition 9.16, Remark 9.17, Corollary 9.18, Definition 9.19,
Remark 9.20, Lemma 9.21, Proposition 9.22, Remarks 9.23-9.24). N1STAR-PROOF.md 10.35 and 10.38. `ext5.py` E6-E7.

### 4.4 The hundred-and-second verifier (D245)

The hundred-and-second verifier (Opus) read this part in full: no major finding, four minor, eleven nits, all seated;
the two claims asked (the least incoming pole $\lambda_\sharp$, simple; the agreement with III.G$'$'s inverse below it)
are proved. (m1) The frames' agreement on $\iota^+$ cited III.C Lemma 1.3, which is stated on $U$: now from its proof,
with $|x|^{-1} = v/t_*$. (m2) Lemma 3.4 and Lemma 2.3 were stated at finite $k$ on the half plane, where (2.2) exists at
finite regularity only on strips: restated, with Lemma 3.5's use. (m3) (G$'''$1) misplaced the source of the exceptional
term: it is a $v^{\lambda_\sharp}$ term of $\Pi_{2\gamma_\Upsilon}h$, not the $(7,4)$ entry alone. (m4) (G$'''$1) said
the record did not consider this channel; it does (N1STAR-PROOF.md 10.38 (d)), and what is open is a reading, about
section 12's linear grafting errors: restated, and the D243 wording withdrawn in the LOG and ROUTES. Nits: two
cross-references; Lemma 1.2's eigenvector argument (all diagonal entries distinct); Lemma 2.3's pole condition; Remark
2.7's sign; (3.5) and Remark 3.8 need $\lambda_\sharp<\ell_I$; "at least" for "exceed" and the double cut-off in
Proposition 2.4; $\ell_K>0$ in Lemma 3.5; the cut-off $\chi_K$ in Corollary 3.1 (2); the mass term and
$\epsilon\le\frac12$ in (G$'''$1); `ext5.py` E6's source table and E7's label. The verifier ran `ext5.py --only 6`,
`--only 7` and E5 with its third control.