# Part III.E'. The vector type 1 dual states at n = 4 ([Hin26] section 7.2.1)

*Status.* Written (D227). This part proves, at spatial dimension $n = 4$ and for the Myers-Perry metrics $g_b$ of Part
III.B with $b$ near $b_0 = (\mu_0,0)$, what [Hin26] section 7.2.1 establishes (pp. 140-144): the Lie derivative of $g_b$
along the rotation vector fields (his Lemma 7.5) and the structure of the vector type 1 dual states (his Proposition
7.4), whose leading term depends on the rotation only through its bracket with the spin. Parts are cited as in III.E.

*What n = 4 changes.* The spin is a matrix $A\in\mathfrak{so}(4)$, and the source's $a(b)\times a(V)$ becomes the
bracket $W = [A,A_V]$. Lemma 7.5 becomes an exact identity, $\delta^*_{g_b}V_b = \frac12D_Ag_b(W)$, from the
$O(4)$-equivariance of Part III.B's family; in its coordinates there is no pure gauge term at leading order, and the
leading term sits at $\rho^3$, the order at which the spin enters. The correction of $V_b$ sits at $|x|^{-3}$, its
coefficient $c_0$ fixed by the vector type 1 indicial value $3(1+2v_C\gamma_C)$. The Killing rotations form a space of
dimension 6, 4 or 2. The source's (7.19) holds with more: $D_{g_b}\mathrm{Ric}(0)^*h^\sharp$ vanishes near $\partial X$,
by the self-adjointness of $G\,D\mathrm{Ric}$, as the source's argument uses $G^2 = \mathrm{Id}$, which fails at
$n = 4$. Findings (E$'$1)-(E$'$5) are in section 4.

## 1. Setting

$\mathcal B$, $b = (\mu,A)$, $g_b$, $t_*$, $\rho = |x|^{-1}$ near $\partial X$, $\bar g$, $\bar t = t_*+|x|$, $\chi$,
and the constants $v_C$, $e_C$, $\gamma_C$, $C_0$ are as in III.E; $g_b = \Phi_\mu^*g^{\mathrm{KS}}_{\mu,A}$ with III.B
(3.1)-(3.3). $C^\infty$ means smooth on $\bar X$ in the trivialisation by $dt_*$, $dx^i$, and
$a\otimes_sb := \frac12(a\otimes b+b\otimes a)$. For $W\in\mathfrak{so}(4)$ put
$$R_W := (Wx)\cdot\partial_x,\qquad V(W) := \bar g(R_W,\cdot) = (Wx)\cdot dx,\tag{1.1}$$
so that $\mathcal V_1 = \{V(W):W\in\mathfrak{so}(4)\}$ is the six-dimensional space of rotation 1-forms of III.D$''$
(1.2), and $\rho V(W) = (W\omega)\cdot dx\in C^\infty$, $\omega := x/|x|$. For $V = V(A_V)\in\mathcal V_1$ write
$V_b := g_b(R_{A_V},\cdot) = g_b\bar g^{-1}V$. $P^* := (P^C_b)^*$ is the adjoint of III.E section 1; on stationary
sections $(\Box^C_b)^* = 2(\delta^*_{g_b,E_C})^*G_{g_b}\delta^*_{g_b}$ acts as $P^*$. $\omega^{*(-1)}_{b,\mathrm v1}(V)$
and $h^*_{b,\mathrm v1}(V) = G_{g_b}\delta^*_{g_b}\omega^{*(-1)}_{b,\mathrm v1}(V)$ are the states of III.E Proposition
3.1.

## 2. The rotations ([Hin26] Lemma 7.5 at n = 4)

**Lemma 2.1 (equivariance).** For $O\in O(4)$ let $\varphi_O(t,x) := (t,Ox)$. Then
$\varphi_O^*g_{(\mu,OAO^T)} = g_{(\mu,A)}$, and $t_*$, $|x|$ and $\chi$ are $\varphi_O$-invariant.

*Proof.* In III.B (3.1), $s = -\frac12\mathrm{tr}(A^2)$ and $p^2 = \mathrm{Pf}(A)^2$ do not change under
$A\mapsto OAO^T$ ($\mathrm{Pf}(OAO^T) = \det O\,\mathrm{Pf}(A)$), so neither does $P$, while
$\mathsf M\mapsto O\mathsf MO^T$; hence $Q(r,Ox)$ for $OAO^T$ equals $Q(r,x)$ for $A$, and by the uniqueness of the root
(III.B Lemma 3.1 (b)), $r_{OAO^T}(Ox) = r_A(x)$. The vector $\mathsf M(rI+A)x/P$ becomes $O$ times itself, so the 1-form
$\ell$ of III.B (3.2) satisfies $\varphi_O^*\ell_{OAO^T} = \ell_A$
($v(Ox)\cdot d(Ox) = (Ov(x))\cdot O\,dx = v(x)\cdot dx$); $x^TA^2\mathsf M^2x$, so $F$ and $H$, are invariant; and
$\eta$, $dt$ are $\varphi_O$-invariant. So $\varphi_O^*g^{\mathrm{KS}}_{\mu,OAO^T} = g^{\mathrm{KS}}_{\mu,A}$.
$\Phi_\mu$ and $t_* = t-\psi(|x|)$ depend on $x$ through $|x|$ only, and so commute with, resp. are invariant under,
$\varphi_O$; $\chi$ is a function of $|x|$. $\square$

**Lemma 2.2 ([Hin26] Lemma 7.5 at n = 4).** Let $b = (\mu,A)$, $A_V\in\mathfrak{so}(4)$, $V := V(A_V)$, $R := R_{A_V}$,
and $W := [A,A_V]$. Then exactly
$$\delta^*_{g_b}V_b = \tfrac12D_Ag_{(\mu,A)}(W),\qquad
D_Ag_{(\mu,A)}(W) := \tfrac d{ds}g_{(\mu,A+sW)}\big|_{s=0},\tag{2.1}$$
and near $\partial X$
$$\delta^*_{g_b}V_b = \mu\rho^3(dt_*+2\,d|x|)\otimes_s\rho V(W)+\tilde h_b(W),\tag{2.2}$$
with $\tilde h_b:\mathfrak{so}(4)\to\rho^4C^\infty(\bar X;S^2T^*X)$ linear and smooth in $b$. So $\delta^*_{g_b}V_b$
depends on $V$ only through $W$, and the right side of (2.1) is defined for every $W\in\mathfrak{so}(4)$.

*Proof.* (2.1). $R$ generates $\varphi_{O_s}$, $O_s := e^{sA_V}$, so
$\mathcal L_Rg_b = \frac d{ds}\varphi_{O_s}^*g_b|_{s=0}$. By Lemma 2.1 with $A$ replaced by $O_s^TAO_s$,
$\varphi_{O_s}^*g_{(\mu,A)} = g_{(\mu,O_s^TAO_s)}$, and $\frac d{ds}O_s^TAO_s|_{s=0} = AA_V-A_VA = W$; so
$\mathcal L_Rg_b = D_Ag_{(\mu,A)}(W)$. And $\delta^*_g(g(R,\cdot)) = \frac12\mathcal L_Rg$ for every metric. (2.2).
Write $x = |x|\omega$. In (3.1) of III.B, $r = |x|u$ turns $Q = 0$ into
$u^4-u^2+\rho^2(su^2-s-\omega^TA^2\omega)+\rho^4p^2 = 0$, whose root $u = 1$ at $\rho = 0$ is simple; by the implicit
function theorem $u = U(\rho^2,\omega,A)$ is smooth with $U = 1+O(\rho^2)$, the $O(\rho^2)$ even in $A$ (the equation
is). Then $H = \mu\rho^2(1+\rho^2C^\infty)$, $F = 1+\rho^2C^\infty$, and
$$\ell_A = \frac{(U^2I+\rho^2(s+A^2))(U\omega+\rho A\omega)}{U^4+s\rho^2U^2+p^2\rho^4}\cdot dx
= d|x|+\rho\,\rho V(A)+\rho^2C^\infty,$$
as $\omega\cdot dx = d|x|$ and $(A\omega)\cdot dx = \rho V(A)$, with every coefficient smooth in $(\rho,\omega,A,\mu)$.
Hence $D_AH(W)\in\rho^4C^\infty$ (it differentiates the $\rho^2$-corrections, even in $A$),
$D_A\ell(W) = \rho\,\rho V(W)+\rho^2C^\infty$, and with $k = dt+\ell_A$,
$$D_Ag^{\mathrm{KS}}(W) = D_AH(W)\,k\otimes k+2H\,k\otimes_sD_A\ell(W)
= 2\mu\rho^3(dt+d|x|)\otimes_s\rho V(W)+\rho^4C^\infty,$$
linear in $W$, the $\rho^4$ part smooth in $(\mu,A)$. $\Phi_\mu$ does not depend on $A$, so
$D_Ag_b(W) = \Phi_\mu^*D_Ag^{\mathrm{KS}}(W)$; $\Phi_\mu^*dt = dt-T'_\mu(|x|)\,d|x|$ with $T'_\mu\in\rho^2C^\infty$, and
the coefficients do not depend on $t$, so the expansion holds for $g_b$ in III.B's $(t,x)$. Finally $t = t_*+\psi(|x|)$
with $\psi'(|x|) = 1-8\mu_0\rho^2$ for large $|x|$ (III.B (3.6)), so $dt+d|x| = dt_*+2\,d|x|+\rho^2C^\infty$. With (2.1)
this is (2.2). $\square$

The source's (7.20) has in addition $-\delta^*_{g_b}(\rho S(a)S'dr+\frac12\slashed d(S(a)S'))$ at leading order; that
term comes from its coordinates, built on the Boyer-Lindquist radius, in which the flat part of the Kerr family is not
Cartesian. Here the coordinates are those of III.B, Kerr-Schild up to $\Phi_\mu$, and there is none (finding (E$'$1)).
In three space dimensions the same computation, with $\mathfrak{so}(3)$'s bracket the cross product, gives the source's
structure (supplement 10.36 (e); `mp5.py` M2-M3 check (2.1) and the leading term of (2.2) at sample spins, and the same
structure on Kerr).

**Lemma 2.3 (the Killing rotations).** $R_{A_V}$ is a Killing field of $g_b$ if and only if $[A,A_V] = 0$. If
$A = O(aJ_{12}+bJ_{34})O^T$ with $O\in SO(4)$ and $J_{ij}$ the elementary generators, then $\dim\ker\mathrm{ad}_A$ is
$6$ if $a = b = 0$, $4$ if $a = \pm b\ne0$, and $2$ otherwise.

*Proof.* $R$ is Killing iff $\delta^*_{g_b}V_b = 0$, which holds if $W = 0$ by (2.1). Conversely, if
$\delta^*_{g_b}V_b = 0$, the $\rho^3$ term of (2.2) vanishes; as $\mu>0$ and $\rho V(W)$ is angular,
$(dt_*+2\,d|x|)\otimes_s\rho V(W) = 0$ forces $V(W) = 0$, so $Wx = 0$ for all $x$ and $W = 0$. For the dimension,
$\mathrm{ad}_{OA'O^T} = \mathrm{Ad}_O\,\mathrm{ad}_{A'}\,\mathrm{Ad}_O^{-1}$, so let $O = I$.
$\mathfrak{so}(4) = \Lambda^2_+\oplus\Lambda^2_-$, the self-dual and anti-self-dual 2-forms, two commuting ideals each
isomorphic to $\mathfrak{so}(3)$, and $A = \frac{a+b}2(J_{12}+J_{34})+\frac{a-b}2(J_{12}-J_{34})$ with
$J_{12}\pm J_{34}\in\Lambda^2_\pm$. The centraliser of $A$ is the sum of the centralisers of its two components, each of
dimension 1 for a nonzero element of $\mathfrak{so}(3)$ and 3 for zero; so the dimension is
$(1\text{ or }3)+(1\text{ or }3)$ according as $a+b$ and $a-b$ vanish. (*Computed:* `dualv1_5.py` V4.) $\square$

So the rotations for which the source's (7.16) holds -- here $h^*_{b,\mathrm v1}(V)\in\dot H^{0,C_0+3}_{\mathrm b}$
(III.E Proposition 3.1 (2)) -- form a space of dimension 6 at $A = 0$, 4 on $\{a = \pm b\ne0\}$ and 2 elsewhere
(Proposition 3.1 (3) below gives the converse), where the source has 3 and 1.

## 3. The structure of the vector type 1 dual states ([Hin26] Proposition 7.4 at n = 4)

Let
$$c_0 := \frac{\mu(1+2(1+v_C)\gamma_C)}{3(1+2v_C\gamma_C)},\qquad
\kappa_C := \frac{1+2(v_C-1)\gamma_C}{1+2v_C\gamma_C}.\tag{3.1}$$

**Proposition 3.1.** Assume (Dyn). Write $A(b) := A$ for $b = (\mu,A)$. The dual states of III.E Proposition 3.1 can be
written
$$h^*_{b,\mathrm v1}(V) = h^\sharp_{b,\mathrm v1}([A(b),A_V])+h^\flat_{b,\mathrm v1}(V),\qquad
V = V(A_V)\in\mathcal V_1,\tag{3.2}$$
where:

(1) $h^\sharp_{b,\mathrm v1}(W)\in\rho^3C^\infty(\bar X;S^2T^*X)$ is linear in $W\in\mathfrak{so}(4)$, smooth in $b$,
vanishes where $\chi = 0$, and has the $\rho^3$ leading term
$$\bar h^\sharp(W) = \mu\rho^3\big(dt_*+\kappa_C\,d|x|\big)\otimes_s\rho V(W);\tag{3.3}$$
moreover, for every $W\in\mathfrak{so}(4)$,
$$(\delta^*_{g_b,E_C})^*h^\sharp_{b,\mathrm v1}(W)\in\rho^{\lfloor C_0\rfloor+5}C^\infty(\bar X;T^*X),\qquad
\widehat{D_{g_b}\mathrm{Ric}}(0)^*h^\sharp_{b,\mathrm v1}(W)\in C^\infty_c(X^\circ;S^2T^*X).\tag{3.4}$$

(2) $h^\flat_{b,\mathrm v1}(V)\in\dot H^{0,C_0+3}_{\mathrm b}(X;S^2T^*X)$ is linear in $V$ and of class $C^k$ in $b$
with values in $\dot H^{-k,C_0+3}_{\mathrm b}$.

(3) $h^*_{b,\mathrm v1}(V)\in\dot H^{0,C_0+3}_{\mathrm b}$ if and only if $[A(b),A_V] = 0$, that is (Lemma 2.3), if and
only if $R_{A_V}$ is Killing for $g_b$.

*Proof. Step 1, the leading order.* For $W\in\mathfrak{so}(4)$ put, on $\mathrm{supp}\,\chi$,
$$k_b(W) := G_{g_b}\Big(\tfrac12D_Ag_b(W)+c_0\,\delta^*_{g_b}\big(|x|^{-3}V(W)\big)\Big),\tag{3.5}$$
linear in $W$ and smooth in $b$. If $W = [A,A_V]$, then $k_b(W) = G_{g_b}\delta^*_{g_b}\omega^\sharp(V)$ with
$\omega^\sharp(V) := V_b+c_0|x|^{-3}V(W)$, by (2.1). Near $\partial X$: $g_b-\bar g\in\rho^2C^\infty$, so
$G_{g_b}-\bar G\in\rho^2C^\infty$ and $\delta^*_{g_b}-\bar\delta^*\in\rho^3C^\infty$ (the Christoffel symbols); with
(2.2) and $dt_*+2\,d|x| = d\bar t+d|x|$,
$$k_b(W) = \bar G\big(h_0+c_0\bar\delta^*(|x|^{-3}V)\big)+\rho^4C^\infty,\qquad
h_0 := \mu|x|^{-4}(d\bar t+d|x|)\otimes_sV,
\quad V := V(W).$$
On Minkowski space (Cartesian $(\bar t,x)$, $r := |x|$, $f = f(r)$): $\bar\delta^*V = 0$, $V$ being Killing, so
$\bar\delta^*(fV) = f'\,dr\otimes_sV$; every $\alpha\otimes_sV$ with $\alpha\in\mathrm{span}\{d\bar t,dr\}$ is
trace-free, as $V$ is angular, so $\bar G$ acts as the identity and $e_C$ drops out;
$\bar\delta(f\,d\bar t\otimes_sV) = 0$ and $\bar\delta(f\,dr\otimes_sV) = -\frac12(f'+5f/r)V$, from
$\nabla dr = r^{-1}(dx^2-dr^2)$, $\nabla_{\partial_r}V = r^{-1}V$, $\Delta r = 3/r$ and $\mathrm{div}\,V = 0$ (here
$\bar\delta = -\mathrm{div}$); and with $\bar c_C = r^{-1}(d\bar t-v_C\,dr)$,
$\bar g^{-1}\bar c_C = -r^{-1}(\partial_{\bar t}+v_C\partial_r)$,
$(\bar E_C)^*h = \gamma_C(2\iota_{\bar g^{-1}\bar c_C}h-\frac23(1-e_C)\bar c_C\,\mathrm{tr}\,h)$ gives
$(\bar E_C)^*(f\,d\bar t\otimes_sV) = -\gamma_Cr^{-1}fV$ and $(\bar E_C)^*(f\,dr\otimes_sV) = -\gamma_Cv_Cr^{-1}fV$. So
$$2(\bar\delta+\bar E_C^*)\bar Gh_0 = -\mu(1+2\gamma_C(1+v_C))r^{-5}V,\qquad
2(\bar\delta+\bar E_C^*)\bar G\,\bar\delta^*(c_0r^{-3}V) = 3c_0(1+2\gamma_Cv_C)r^{-5}V,$$
which cancel by (3.1); $3(1+2v_C\gamma_C)$ is the vector type 1 indicial value $N(\rho^{-2}P^*,2)$ (supplement 10.31
(i)). And $(\delta^*_{g_b,E_C})^*-(\bar\delta+\bar E_C^*)\in\rho^3\mathrm{Diff}^1_{\mathrm b}$ near $\partial X$
($g_b-\bar g\in\rho^2C^\infty$, $c_C-\bar c_C\in\rho^3C^\infty$, III.E section 1), while
$\bar\delta+\bar E^*_C\in\rho\,\mathrm{Diff}^1_{\mathrm b}$; hence
$$f_1(W) := 2(\delta^*_{g_b,E_C})^*\big(\chi k_b(W)\big)\in C^\infty_c(X^\circ)+\rho^5C^\infty,\tag{3.6}$$
the commutator with $\chi$ being supported where $d\chi\ne0$. The leading term of $k_b(W)$ is
$h_0-3c_0r^{-4}dr\otimes_sV = \rho^3(\mu\,dt_*+(2\mu-3c_0)\,d|x|)\otimes_s\rho V$, and $2\mu-3c_0 = \mu\kappa_C$: this
is (3.3). (*Computed:* `dualv1_5.py` V1-V3, exact, each with a failing control.)

*Step 2, the formal solution.* Let $J := \lfloor C_0\rfloor+2$. Near $\partial X$, $\rho^{-2}P^*$ is a b-differential
operator with coefficients smooth on $\bar X$ and $b$-independent normal operator (as
$P^C_b-\bar P^C\in\rho^4\mathrm{Diff}^2_{\mathrm b}$), so
$P^*(\rho^jc) = \rho^{j+2}N(\rho^{-2}P^*,j)c+\rho^{j+3}C^\infty$ for $c\in C^\infty(\partial X;T^*X|_{\partial X})$. For
$3\le j\le J$, $N(\rho^{-2}P^*,j)$ is invertible on $C^\infty(\partial X)$, since the indicial roots of $P^*$ are $0$,
have negative real part, or have real part $>C_0+2\ge J$ (III.E Lemma 2.1 (2)), and it is elliptic (III.A (E2)).
Removing in turn, for $j = 3,\dots,J$, the coefficient of $\rho^{j+2}$ of the current remainder by $\rho^jc_j(W)$,
$c_j(W) := -N(\rho^{-2}P^*,j)^{-1}$ of that coefficient, gives $\omega'^\sharp_1(W) := \sum_{j=3}^J\rho^jc_j(W)$, linear
in $W$ and smooth in $b$, with
$$r_b(W) := f_1(W)+P^*\big(\chi\omega'^\sharp_1(W)\big)\in C^\infty_c(X^\circ)+\rho^{J+3}C^\infty.\tag{3.7}$$
(This is III.A Lemma 1.5 with no pole met.)

*Step 3, the solution.* As $J+3 = \lfloor C_0\rfloor+5>C_0+4$, $r_b(W)\in\dot H^{0,C_0+4}_{\mathrm b}$, and III.E Lemma
2.1 (1) ($s = 1$, $\alpha = C_0+2$) gives $\omega'^\flat_1(W) := -(P^*)^{-1}r_b(W)\in\dot H^{1,C_0+2}_{\mathrm b}$. Let
$V = V(A_V)$, $W := [A,A_V]$, and
$f_2(V) := 2(\delta^*_{g_b,E_C})^*G_{g_b}(d\chi\otimes_s\omega^\sharp(V))\in C^\infty_c(X^\circ)$,
$\omega'_2(V) := -(P^*)^{-1}f_2(V)\in\dot H^{1,C_0+2}_{\mathrm b}$. Since
$G_{g_b}\delta^*_{g_b}(\chi\omega^\sharp(V)) = \chi k_b(W)+G_{g_b}(d\chi\otimes_s\omega^\sharp(V))$,
$P^*(\chi\omega^\sharp(V)) = f_1(W)+f_2(V)$, and
$$\tilde\omega := \chi\omega^\sharp(V)+\chi\omega'^\sharp_1(W)+\omega'^\flat_1(W)+\omega'_2(V)$$
satisfies $P^*\tilde\omega = f_1+f_2+(r_b-f_1)-r_b-f_2 = 0$. Moreover
$\tilde\omega-\omega^{*(-1)}_{b,\mathrm v1}(V)\in\dot H^{1,\alpha}_{\mathrm b}$ for $\alpha\in(0,1)$:
$\omega^{*(-1)}_{b,\mathrm v1}(V) = \chi V+\omega'_b$ with $\omega'_b\in\dot H^{1,((2,0),C_0+2)}_{\mathrm b}$,
$\chi(V_b-V) = \chi(g_b-\bar g)(R_{A_V},\cdot)\in\rho C^\infty$, $\chi c_0|x|^{-3}V(W)\in\rho^2C^\infty$ and
$\chi\omega'^\sharp_1\in\rho^3C^\infty$. Both lie in the kernel of $P^*$, so by III.E Lemma 2.1 (1) with such an
$\alpha$ they are equal, as in III.E's argument for the Killing rotations.

*Step 4, the splitting.*
$h^*_{b,\mathrm v1}(V) = G_{g_b}\delta^*_{g_b}\tilde\omega = h^\sharp_{b,\mathrm v1}(W)+h^\flat_{b,\mathrm v1}(V)$ with
$$h^\sharp_{b,\mathrm v1}(W) := \chi k_b(W)+G_{g_b}\delta^*_{g_b}\big(\chi\omega'^\sharp_1(W)\big),$$
$$h^\flat_{b,\mathrm v1}(V) := G_{g_b}\big(d\chi\otimes_s\omega^\sharp(V)\big)
+G_{g_b}\delta^*_{g_b}\big(\omega'^\flat_1([A,A_V])+\omega'_2(V)\big).$$
(1): $h^\sharp(W)$ is defined for every $W$, is linear in $W$ and smooth in $b$, vanishes where $\chi = 0$, and lies in
$\rho^3C^\infty$ with leading term that of $k_b(W)$, (3.3), the second summand being in $\rho^4C^\infty$. As
$2(\delta^*_{g_b,E_C})^*G_{g_b}\delta^*_{g_b} = P^*$ on stationary sections,
$2(\delta^*_{g_b,E_C})^*h^\sharp(W) = f_1(W)+P^*(\chi\omega'^\sharp_1(W)) = r_b(W)$, the first part of (3.4). For the
second, two facts at a Ricci-flat $g$ in every dimension:
$D_g\mathrm{Ric}(\delta^*_g\omega) = \frac12D_g\mathrm{Ric}(\mathcal L_{\omega^\sharp}g)$, which is
$\frac12\mathcal L_{\omega^\sharp}\mathrm{Ric}(g) = 0$;
and $G_gD_g\mathrm{Ric}$, which is the linearised Einstein tensor there, is formally self-adjoint (it is, up to sign,
the second variation of the Einstein-Hilbert action), so with $G_g$ symmetric and invertible,
$D_g\mathrm{Ric}^*G_g = G_gD_g\mathrm{Ric}$. As every $g_{(\mu,A)}$ is Ricci-flat, $D_{g_b}\mathrm{Ric}(D_Ag_b(W)) = 0$.
Hence, writing $\chi\delta^*y = \delta^*(\chi y)-d\chi\otimes_sy$,
$$D_{g_b}\mathrm{Ric}^*h^\sharp(W) = G_{g_b}D_{g_b}\mathrm{Ric}\Big(
\tfrac12\chi D_Ag_b(W)-c_0\,d\chi\otimes_s|x|^{-3}V(W)\Big),$$
and $D_{g_b}\mathrm{Ric}(\frac12\chi D_Ag_b(W)) = \frac12[D_{g_b}\mathrm{Ric},\chi]D_Ag_b(W)$ is supported where
$d\chi\ne0$: so $D_{g_b}\mathrm{Ric}(0)^*h^\sharp(W)\in C^\infty_c(X^\circ)$ (the stationary adjoint being the zero
energy operator's, III.E section 1). (2): $G_{g_b}(d\chi\otimes_s\omega^\sharp)\in C^\infty_c$, and
$\delta^*_{g_b}\in\rho\,\mathrm{Diff}^1_{\mathrm b}$ maps $\dot H^{1,C_0+2}_{\mathrm b}$ to
$\dot H^{0,C_0+3}_{\mathrm b}$; linearity in $V$ is clear, and the regularity in $b$ follows as in III.E Proposition
3.1, the sources $r_b(W)$ and $f_2(V)$ being smooth in $b$ in $C^\infty_c+\rho^{J+3}C^\infty$, resp. $C^\infty_c$. (3):
if $W = [A,A_V]\ne0$, then $\bar h^\sharp(W)\ne0$ ($\mu>0$, $V(W)\ne0$), a $\rho^3$ term not in
$\dot H^{0,C_0+3}_{\mathrm b}$ while $h^\flat$ is; if $W = 0$, $h^\sharp(0) = 0$. $\square$

*Remark.* The source's (7.31) and (7.18) are the four-dimensional counterparts of $c_0|x|^{-3}V(W)$ and (3.3): with
$\mu\leftrightarrow2m$ (the mass enters as $\mu|x|^{-2}$ where Kerr's does as $2m|x|^{-1}$),
$\rho^3\leftrightarrow\rho^2$ and the bracket for the cross product, the same coefficients $1+2(v_C\mp1)\gamma_C$ over
$1+2v_C\gamma_C$ appear, up to the orientation convention of the spin (supplement 10.36 (ii)), and the indicial value
$3(1+2v_C\gamma_C)$ replaces his $2+4\gamma_Cv_C$. In his ansatz the term $\rho S(a)S'dr+\frac12\slashed d(S(a)S')$
cancels his (7.20)'s pure gauge term; here there is none to cancel.

## 4. Findings, labels and sources

### 4.1 Findings

(E$'$1) *Lemma 7.5 is exact at n = 4, without a gauge term.* $\delta^*_{g_b}V_b = \frac12D_Ag_b([A,A_V])$ by
equivariance (Lemma 2.1), so the deformation tensor of a rotation is the derivative of the family along the bracket of
the spin with the rotation; in Part III.B's coordinates it has no pure gauge term at leading order, where the source's
(7.20) has $-\delta^*_{g_b}(\rho S(a)S'dr+\frac12\slashed d(S(a)S'))$, an effect of coordinates built on the
Boyer-Lindquist radius. The leading order is $\rho^3$, one beyond the source's $\rho^2$.

(E$'$2) *The bracket.* $a(b)\times a(V)$ becomes $[A(b),A_V]\in\mathfrak{so}(4)$; $h^\sharp$ is defined on all of
$\mathfrak{so}(4)$, smoothly in $b$, across the jumps 6, 4, 2 of the Killing rotations (Lemma 2.3), where the source's
jump is from 3 to 1 at $a = 0$.

(E$'$3) *The coefficients.* The correction of $V_b$ is $c_0|x|^{-3}V(W)$ with $c_0$ of (3.1), fixed by the vector type 1
indicial value $3(1+2v_C\gamma_C)$; the leading term (3.3) has the source's coefficients $1+2(v_C\mp1)\gamma_C$ over
$1+2v_C\gamma_C$. $e_C$ drops out, the tensors involved being trace-free, as in the source.

(E$'$4) *The adjoint of the linearised Ricci operator.* The source proves
$\widehat{D_{g_b}\mathrm{Ric}}(0)^*h^\sharp\in\rho^{\lfloor C_0\rfloor+2}C^\infty$ from
$\mathrm{ran}\,G\delta^*\subset\ker(D\mathrm{Ric}\circ G)$, which uses $G^2 = \mathrm{Id}$, true in $3+1$ dimensions; in
$4+1$, $G^2h = h+\frac14g\,\mathrm{tr}\,h$. The statement holds at $n = 4$ in the form
$\ker D\mathrm{Ric}^* = G(\ker D\mathrm{Ric})\supset\mathrm{ran}\,G\delta^*$, from the self-adjointness of
$G\,D\mathrm{Ric}$; with the Ricci-flatness of the whole family it gives (3.4), the adjoint vanishing near $\partial X$.

(E$'$5) *The statement of (2).* The source states $h^{*\flat}_{b,\mathrm v1}(V)\in\dot H^{0,C_0+1}_{\mathrm b}(X;T^*X)$;
its proof gives $\dot H^{0,C_0+2}_{\mathrm b}(X;S^2T^*X)$, the bundle being that of symmetric 2-tensors. Harmless. Here
the weight is $C_0+3$.

### 4.2 Labels

Proved here: Lemmas 2.1-2.3 and Proposition 3.1. Computed, as checks: `dualv1_5.py` V1-V4 (exact, with failing controls)
and `mp5.py` M1-M5 (supplement 10.36: the family, (2.1) on the full metric at exact points, the expansion of (2.2) at
sample spins, the Killing rotations, the leading term in the source's coordinates). Inputs: III.B (3.1)-(3.3), (3.6),
Lemma 3.1 and Proposition 3.6; III.E section 1, Lemma 2.1 and Proposition 3.1; III.D$''$ (1.2); III.A (E2) and Lemma
1.5. Standard facts used without proof, and named: the implicit function theorem;
$\mathfrak{so}(4) = \Lambda^2_+\oplus\Lambda^2_-$ as two commuting ideals isomorphic to $\mathfrak{so}(3)$, in which the
centraliser of a nonzero element is one-dimensional; $\delta^*_g(g(R,\cdot)) = \frac12\mathcal L_Rg$; the diffeomorphism
invariance of $\mathrm{Ric}$; the formal self-adjointness of the linearised Einstein tensor at a Ricci-flat metric.

### 4.3 Sources

READ: [Hin26] pp. 140-144 (section 7.2.1: (7.16), Proposition 7.4, (7.17)-(7.19), Lemma 7.5 and its proof,
(7.20)-(7.28), the proof of Proposition 7.4, (7.29)-(7.35)), arXiv:2606.28253v2, full text in the record's extraction.
The record's supplement 10.31 (i), (c) and 10.36 for the computed values, here derived by hand.

