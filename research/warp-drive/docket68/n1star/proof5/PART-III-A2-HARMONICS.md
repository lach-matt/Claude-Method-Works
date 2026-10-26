# Part III.A$'$. Spherical harmonics on the three-sphere, and the Minkowski operators, at n = 4

*Status.* Verified (D221). Written (D218); read line by line by the ninety-second verifier, whose two minor findings and
six nits are seated (section 3.4). This part proves, at spatial dimension $n = 4$, what [Hin26] section 2.4 (pp. 63-67)
establishes at $n = 3$: the spherical harmonic decomposition of functions, 1-forms and symmetric 2-tensors on the sphere
at infinity, the identities between the geometric operators on each type and the special low degrees ((2.34)-(2.35)),
the Minkowski wave operator, symmetric gradient and divergence in the null bundle splittings near infinity (his Lemma
2.29), the types of tensors those operators preserve ((2.43)-(2.44)), the indicial roots by type (his Definition 2.30
and the example after it), and the indicial families of the symmetric gradient with their kernels ((2.46) and the remark
after it). At $n = 4$ the sphere is $\mathbb S^3$, the constants of his Lemma 2.29 change, and one type is new:
transverse trace-free symmetric 2-tensors, which $\mathbb S^2$ does not carry.

*Method.* Every statement is proved on the unit sphere $\mathbb S^N$ and on $\mathbb R^{1+(N+1)}$ for general $N\ge2$,
from the Ricci identity and the Gauss formula, and then read at $N = 3$. At $N = 2$ each formula is the source's, entry
by entry, which is the control. The source proves his Lemma 2.29 by "explicit computation" with a pointer to [Hin23b]
section 6.2, which is not read here; section 2 below gives the computation. Every formula is also checked by machine in
`harm5.py` (sympy, exact, the degree $l$ symbolic): K5 applies the Cartesian componentwise operators to explicit
harmonics of every type at $N = 2$ and $N = 3$ and compares the result, entry by entry, with the type-wise matrices
obtained from Lemma 2.1 and Lemma 1.5 below; K1-K3 and K6 factor the determinants.

## 1. Harmonics on the sphere

Let $N\ge2$, $\slashed g$ the round metric of the unit sphere $\mathbb S^N\subset\mathbb R^{N+1}$, and use the
conventions of [Hin26] Notation 2.26: $\slashed\Delta := -\mathrm{tr}\,\slashed\nabla^2$ the non-negative rough
Laplacian on tensors, $\slashed\delta\omega := -\omega_{a;}{}^a$, $(\slashed\delta h)_a := -h_{ab;}{}^b$,
$(\slashed\delta^*\omega)_{ab} := \frac12(\omega_{a;b}+\omega_{b;a})$, and
$$\slashed\delta^*_0 := \slashed\delta^*+\tfrac1N\slashed g\slashed\delta,\tag{1.1}$$
the trace-free part of $\slashed\delta^*$ ($\mathrm{tr}\,\slashed\delta^*\omega = -\slashed\delta\omega$); at $N = 2$
this is the source's $\slashed\delta^*+\frac12\slashed g\slashed\delta$. On functions $\slashed\Delta = \slashed\delta
d$. The curvature is $\slashed R(X,Y)Z = \langle Y,Z\rangle X-\langle X,Z\rangle Y$, so that on 1-forms
$\slashed\nabla_a\slashed\nabla_b\omega_c-\slashed\nabla_b\slashed\nabla_a\omega_c = \slashed g_{ac}\omega_b-\slashed
g_{bc}\omega_a$, and $\mathrm{Ric}(\slashed g) = (N-1)\slashed g$.

*Ambient picture.* Write $\hat x$ for the position on $\mathbb S^N$. A 1-form on $\mathbb S^N$ is identified, through
$\slashed g$, with a tangential vector field $V:\mathbb S^N\to\mathbb R^{N+1}$, $V\cdot\hat x = 0$, and a symmetric
2-tensor with a tangential symmetric matrix field $Q$, $Q\hat x = 0$; $\slashed g$ itself is $P := I-\hat x\otimes\hat
x$. Put $\hat x\odot V := \hat x\otimes V+V\otimes\hat x$. $D$ is the flat derivative of $\mathbb R^{N+1}$- or
matrix-valued functions along $\mathbb S^N$, and $\Delta^e$ is $\slashed\Delta$ applied to each Cartesian component as a
function.

**Lemma 1.1 (commutators on the unit sphere).** For every function $S$, 1-form $\omega$ and symmetric 2-tensor $h$ on
$\mathbb S^N$:

(a) $\slashed\Delta\,dS = d\slashed\Delta S-(N-1)\,dS$;

(b) $2\slashed\delta\slashed\delta^*\omega = d\slashed\delta\omega+\slashed\Delta\omega-(N-1)\omega$;

(c) $\slashed\Delta\slashed\delta^*\omega = \slashed\delta^*\slashed\Delta\omega-(N+1)\slashed\delta^*\omega-2\slashed
g\,\slashed\delta\omega$;

(d) $\slashed\delta\slashed\Delta\omega = \slashed\Delta\slashed\delta\omega-(N-1)\slashed\delta\omega$ and
$\slashed\delta\slashed\Delta h = \slashed\Delta\slashed\delta h-(N+1)\slashed\delta h-2\,d\,\mathrm{tr}\,h$.

*Proof.* Contracting the Ricci identity, $\slashed\nabla^d\slashed\nabla_a\omega_d =
\slashed\nabla_a\slashed\nabla^d\omega_d+(N-1)\omega_a$. (a) With $\omega = dS$ and the symmetry of the Hessian,
$-(\slashed\Delta dS)_a = \slashed\nabla^d\slashed\nabla_d\slashed\nabla_aS =
\slashed\nabla^d\slashed\nabla_a\slashed\nabla_dS =
\slashed\nabla_a\slashed\nabla^d\slashed\nabla_dS+(N-1)\slashed\nabla_aS$. (b)
$2(\slashed\delta\slashed\delta^*\omega)_b =
-\slashed\nabla^a\slashed\nabla_a\omega_b-\slashed\nabla^a\slashed\nabla_b\omega_a =
(\slashed\Delta\omega)_b-\slashed\nabla_b\slashed\nabla^a\omega_a-(N-1)\omega_b$. (c) For a 2-tensor $S_{eb}$ the Ricci
identity gives $\slashed\nabla_d\slashed\nabla_aS_{eb}-\slashed\nabla_a\slashed\nabla_dS_{eb} = -\slashed
g_{ae}S_{db}+\slashed g_{de}S_{ab}-\slashed g_{ab}S_{ed}+\slashed g_{db}S_{ea}$; contracting $d$ with $e$ and taking
$S_{db} := \slashed\nabla_d\omega_b$, so that $\slashed\nabla^dS_{db} = -(\slashed\Delta\omega)_b$ and $\mathrm{tr}\,S =
-\slashed\delta\omega$,
$$\slashed\nabla^d\slashed\nabla_a\slashed\nabla_d\omega_b
= -\slashed\nabla_a(\slashed\Delta\omega)_b+(N-1)\slashed\nabla_a\omega_b
+\slashed\nabla_b\omega_a+\slashed g_{ab}\slashed\delta\omega.$$
With $\slashed\nabla_d\slashed\nabla_a\omega_b = \slashed\nabla_a\slashed\nabla_d\omega_b+\slashed
g_{db}\omega_a-\slashed g_{ab}\omega_d$ this yields
$$-(\slashed\Delta\slashed\nabla\omega)_{ab} = \slashed\nabla^d\slashed\nabla_d\slashed\nabla_a\omega_b
= -\slashed\nabla_a(\slashed\Delta\omega)_b+(N-1)\slashed\nabla_a\omega_b
+2\slashed\nabla_b\omega_a+2\slashed g_{ab}\slashed\delta\omega,
$$
and symmetrising in $a,b$ gives (c). (d) are the formal adjoints of (a) and (c): the adjoint of $d$ on functions is
$\slashed\delta$, of $\slashed\delta^*$ is $\slashed\delta$, of $\slashed g\,\cdot$ is $\mathrm{tr}$, $\slashed\Delta$
is formally self-adjoint, and two differential operators agree if and only if their formal adjoints do. $\square$

**Lemma 1.2 (ambient identities).** For a function $f$, a tangential vector field $V$ and a tangential symmetric matrix
field $Q$ on $\mathbb S^N$:
$$\Delta^e(f\hat x) = (\slashed\Delta f+Nf)\hat x-2\slashed\nabla f,\tag{1.2a}$$
$$\Delta^eV = (\slashed\Delta+1)V-2(\slashed\delta V)\hat x,\tag{1.2b}$$
$$\Delta^e(f\hat x\otimes\hat x) = (\slashed\Delta f+2Nf)\hat x\otimes\hat x-2fP
-2\hat x\odot\slashed\nabla f,\tag{1.2c}$$
$$\Delta^e(\hat x\odot V)
= \hat x\odot(\slashed\Delta+N+3)V-4(\slashed\delta V)\hat x\otimes\hat x-4\slashed\delta^*V,\tag{1.2d}$$
$$\Delta^eQ = (\slashed\Delta+2)Q-2\hat x\odot\slashed\delta Q-2(\mathrm{tr}\,Q)\hat x\otimes\hat x.\tag{1.2e}$$

*Proof.* By the Gauss formula of the unit sphere, $D_X\hat x = X$, $D_XV = \slashed\nabla_XV-\langle X,V\rangle\hat x$,
and, writing $Q = \sum q_{bc}e_b\otimes e_c$ in a frame, $D_XQ = \slashed\nabla_XQ-\hat x\odot Q(X)$ with $Q(X) := \sum
q_{bc}X^be_c$. At a point take an orthonormal frame $(e_a)$ with $\slashed\nabla e_a = 0$ there; then $D_{e_a}e_a =
-\hat x$ and $\Delta^e = -\sum_aD_{e_a}D_{e_a}$ there; write $D_a := D_{e_a}$. (1.2b): $e_a\langle e_a,V\rangle =
\langle e_a,\slashed\nabla_aV\rangle$ there, so $\sum_aD_aD_aV = \sum_a(\slashed\nabla_a\slashed\nabla_aV-2\langle
e_a,\slashed\nabla_aV\rangle\hat x-\langle e_a,V\rangle e_a) = -\slashed\Delta V+2(\slashed\delta V)\hat x-V$. (1.2a),
(1.2c): the product rule $\Delta^e(uv) = (\Delta^eu)v+u\Delta^ev-2\sum_a(D_au)(D_av)$ with $\Delta^e\hat x = N\hat x$,
$\sum_a(e_af)e_a = \slashed\nabla f$ and $\sum_ae_a\otimes e_a = P$. (1.2d): by the product rule and (1.2b),
$\Delta^e(\hat x\otimes V) = N\hat x\otimes V+\hat x\otimes((\slashed\Delta+1)V-2(\slashed\delta V)\hat
x)-2\sum_ae_a\otimes(\slashed\nabla_aV-\langle e_a,V\rangle\hat x)$; adding the transpose and using
$\sum_a(e_a\otimes\slashed\nabla_aV+\slashed\nabla_aV\otimes e_a) = 2\slashed\delta^*V$ gives (1.2d). (1.2e):
$\sum_aD_aD_aQ = \sum_a(\slashed\nabla_a\slashed\nabla_aQ-\hat x\odot(\slashed\nabla_aQ)(e_a)-e_a\odot Q(e_a)-\hat
x\odot D_a(Q(e_a)))$ with $D_a(Q(e_a)) = (\slashed\nabla_aQ)(e_a)-Q(e_a,e_a)\hat x$, $\sum_a(\slashed\nabla_aQ)(e_a) =
-\slashed\delta Q$ and $\sum_ae_a\odot Q(e_a) = 2Q$. As a check, (1.2e) at $Q = P$ and (1.2c) at $f = 1$ give $\Delta^eP
= -\Delta^e(\hat x\otimes\hat x) = 2P-2N\hat x\otimes\hat x$. $\square$

**Definition 1.3 (spherical harmonics; [Hin26] Definition 2.27 at n = 4).** For $l\in\mathbb N_0$ let $k_l^2 :=
l(l+N-1)$.

(1) $\mathcal S_l := \ker(\slashed\Delta-k_l^2)\subset C^\infty(\mathbb S^N)$.

(2) For $l\ge1$, $\mathcal V_l := \{V\in C^\infty(\mathbb S^N;T^*\mathbb S^N):\slashed\delta V = 0,\ \slashed\Delta V =
(k_l^2-1)V\}$. A 1-form is of *scalar type* $l$ if it is $dS$, $S\in\mathcal S_l$, and of *vector type* $l$ if it lies
in $\mathcal V_l$.

(3) For $l\ge2$, $\mathcal T_l := \{T\in C^\infty(\mathbb S^N;S^2T^*\mathbb S^N):\mathrm{tr}\,T = 0,\ \slashed\delta T =
0,\ \slashed\Delta T = (k_l^2-2)T\}$. A symmetric 2-tensor is of *scalar type* $l$ if it is
$\slashed\delta^*_0dS+S'\slashed g$ with $S,S'\in\mathcal S_l$; of *vector type* $l$ if it is $\slashed\delta^*V$,
$V\in\mathcal V_l$; of *tensor type* $l$ if it lies in $\mathcal T_l$.

The source states that on $\mathbb S^2$ there are no nonzero trace-free divergence-free symmetric 2-tensors and that
$\mathcal V_l = \{\slashed\star dS:S\in\mathcal S_l\}$ ([Hin26] p. 64, from [Hig87]; READ, used only to compare with the
source). On $\mathbb S^3$ the tensor type is not empty: with $z := x_1+ix_2$, $w := x_3+ix_4$ and $\beta :=
z\,dw-w\,dz$, a tangential 1-form, $T := z^{l-2}\beta\otimes\beta$ restricted to $\mathbb S^3$ lies in $\mathcal
T_l\otimes\mathbb C$ for every $l\ge2$. Indeed, with the Euclidean product extended bilinearly, $dz\cdot dz = dw\cdot
dw = dz\cdot dw = 0$, so $\beta\cdot\beta = 0$, $\beta\cdot dz = \beta\cdot dw = 0$ and $\beta\cdot x = 0$; and
$\partial_i\beta_i = 0$. Hence $T$ is tangential and trace-free, its Euclidean divergence $\beta(\beta\cdot\nabla
z^{l-2})+z^{l-2}((\partial_i\beta_i)\beta+(\beta\cdot\nabla)\beta)$ vanishes, and its components are holomorphic in
$(z,w)$, so harmonic and homogeneous of degree $l$; the argument of Lemma 1.4 (3), by (1.2e), then gives
$\slashed\delta T = 0$ and $\slashed\Delta T = (k_l^2-2)T$. (Also computed: `harm5.py` K5, types t2 and tl, where the
Cartesian computation closes on this tensor alone.)

**Lemma 1.4 (spectra).** (1) $\mathcal S_l$ consists of the restrictions of the harmonic homogeneous polynomials of
degree $l$ on $\mathbb R^{N+1}$, these exhaust the eigenfunctions of $\slashed\Delta$, and $\dim\mathcal S_l = (l+1)^2$
at $N = 3$.

(2) If $\omega\ne0$ is a co-closed 1-form with $\slashed\Delta\omega = \mu\omega$, then $\mu = k_l^2-1$ for some
$l\ge1$, and the Cartesian components of $\omega$ lie in $\mathcal S_l$. $\mathcal V_1$ consists of the duals of the
Killing fields of $\mathbb S^N$, which are the rotation fields $x\mapsto Ax$, $A\in\mathfrak{so}(N+1)$, restricted to
$\mathbb S^N$; $\dim\mathcal V_1 = N(N+1)/2$.

(3) If $h\ne0$ is trace-free, divergence-free and $\slashed\Delta h = \mu h$, then $\mu = k_l^2-2$ for some $l\ge2$, and
the Cartesian components of $h$ lie in $\mathcal S_l$.

(4) $\slashed\Delta$ maps co-closed 1-forms to co-closed 1-forms and trace-free divergence-free tensors to such tensors.
Every smooth co-closed 1-form is a sum $\sum_{l\ge1}V_l$, $V_l\in\mathcal V_l$, and every smooth trace-free
divergence-free tensor a sum $\sum_{l\ge2}T_l$, $T_l\in\mathcal T_l$, converging in $C^\infty$.

*Proof.* (1) Classical: on $\mathbb R^{N+1}$, $\Delta_{\mathbb R^{N+1}} = \partial_r^2+\frac
Nr\partial_r-r^{-2}\slashed\Delta$ (in our sign convention for $\slashed\Delta$), so a harmonic homogeneous polynomial
$p$ of degree $l$ restricts to an element of $\mathcal S_l$. Every polynomial restricted to $\mathbb S^N$ is a sum of
restricted harmonic ones (the decomposition $\mathcal P_l = \mathcal H_l\oplus|x|^2\mathcal P_{l-2}$), polynomials are
dense in $C(\mathbb S^N)$, and eigenfunctions with distinct eigenvalues are orthogonal; so an eigenfunction with
eigenvalue $\mu$ is orthogonal to a dense set unless $\mu = k_l^2$ for some $l$, and then it is orthogonal to every
restricted harmonic polynomial of degree $\ne l$, hence lies in the restrictions of $\mathcal H_l$. $\dim\mathcal H_l =
\dim\mathcal P_l-\dim\mathcal P_{l-2} = \binom{l+3}3-\binom{l+1}3 = (l+1)^2$ in four variables. (2) By (1.2b) with
$\slashed\delta V = 0$, $\Delta^eV = (\mu+1)V$: every Cartesian component of $V$ is an eigenfunction with eigenvalue
$\mu+1$, which by (1) is $k_l^2$ for some $l\ge0$, the components lying in $\mathcal S_l$. If $l = 0$ the components are
constant, and $V\cdot\hat x = 0$ for every $\hat x$ forces $V = 0$; so $l\ge1$. For $V\in\mathcal V_1$, Lemma 1.1 (b)
gives $2\slashed\delta\slashed\delta^*V = (k_1^2-1-(N-1))V = 0$, as $k_1^2 = N$, so $\|\slashed\delta^*V\|^2 = 0$ and
$V$ is Killing. Conversely a Killing $V$ has $\slashed\delta V = -\mathrm{tr}\,\slashed\delta^*V = 0$ and, by Lemma 1.1
(b), $\slashed\Delta V = (N-1)V = (k_1^2-1)V$. The rotation fields restrict to Killing fields, $A\mapsto(Ax)|_{\mathbb
S^N}$ is injective, and the Killing fields of a connected Riemannian $N$-manifold form a space of dimension at most
$N(N+1)/2$ (a Killing field is determined by its value and covariant derivative at one point); so they are all. (3) By
(1.2e) with $\mathrm{tr}\,Q = 0$ and $\slashed\delta Q = 0$, every Cartesian component is an eigenfunction with
eigenvalue $\mu+2 = k_l^2$, the components lying in $\mathcal S_l$. If $l = 0$, $Q$ is constant with $Q\hat x = 0$ for
every $\hat x$, so $Q = 0$. If $l = 1$, $Q_{ij} = \sum_kc_{ijk}\hat x_k$ with $c$ symmetric in $i,j$, and $Q(\hat x)\hat
x = 0$ for every $\hat x$ makes $c$ antisymmetric in $j,k$; a 3-tensor symmetric in its first two indices and
antisymmetric in its last two vanishes ($c_{ijk} = -c_{ikj} = -c_{kij} = c_{kji} = c_{jki} = -c_{jik} = -c_{ijk}$). So
$l\ge2$. (4) The first sentence is Lemma 1.1 (d), with $\mathrm{tr}\,\slashed\Delta h = \slashed\Delta\,\mathrm{tr}\,h$
as $\slashed g$ is parallel. $\slashed\Delta$ is elliptic and self-adjoint on the compact $\mathbb S^N$, so $L^2$ is the
orthogonal sum of its finite-dimensional eigenspaces $E_\mu$ of smooth sections, and a smooth section's expansion
converges in $C^\infty$. For a co-closed $\omega = \sum_\mu\omega_\mu$, Lemma 1.1 (d) makes $\slashed\delta\omega_\mu$
an eigenfunction with eigenvalue $\mu+N-1$; these are mutually orthogonal for distinct $\mu$ and sum to
$\slashed\delta\omega = 0$, so each $\omega_\mu$ is co-closed and, by (2), lies in $\mathcal V_l$ with $\mu = k_l^2-1$.
For a trace-free divergence-free $h = \sum_\mu h_\mu$ the same argument applies to $\mathrm{tr}\,h_\mu$ (eigenvalue
$\mu$) and then to $\slashed\delta h_\mu$ (eigenvalue $\mu+N+1$ by Lemma 1.1 (d)), and (3) concludes. $\square$

**Lemma 1.5 (the identities; [Hin26] (2.34)-(2.35) at n = 4).** For $S\in\mathcal S_l$, $V\in\mathcal V_l$ ($l\ge1$),
$T\in\mathcal T_l$ ($l\ge2$) and $k^2 := k_l^2$:
$$\slashed\delta dS = k^2S,\qquad\slashed\Delta dS = (k^2-N+1)\,dS,\qquad\slashed\delta^*dS
= \slashed\delta^*_0dS-\tfrac{k^2}N\slashed gS,\qquad
\slashed\Delta(\slashed gS) = k^2\slashed gS,$$
$$\slashed\delta(\slashed gS) = -dS,\qquad\mathrm{tr}(\slashed gS) = NS,\qquad\mathrm{tr}\,\slashed\delta^*_0dS = 0,$$
$$\slashed\delta(\slashed\delta^*_0dS) = \tfrac{N-1}N(k^2-N)\,dS,\qquad\slashed\Delta(\slashed\delta^*_0dS)
= (k^2-2N)\,\slashed\delta^*_0dS,$$
$$\slashed\Delta V = (k^2-1)V,\qquad\slashed\delta\slashed\delta^*V = \tfrac12(k^2-N)V,
\qquad\mathrm{tr}\,\slashed\delta^*V = 0,\qquad
\slashed\Delta\slashed\delta^*V = (k^2-N-2)\,\slashed\delta^*V,$$
$$\mathrm{tr}\,T = 0,\qquad\slashed\delta T = 0,\qquad\slashed\Delta T = (k^2-2)T;\tag{1.2}$$
and
$$\slashed\delta^*_0dS = 0\ \ (S\in\mathcal S_1),\qquad\slashed\delta^*V = 0\ \ (V\in\mathcal V_1).\tag{1.3}$$
At $N = 3$: $\slashed\Delta dS = (k^2-2)dS$, $\slashed\delta^*dS = \slashed\delta^*_0dS-\frac{k^2}3\slashed gS$,
$\slashed\delta(\slashed\delta^*_0dS) = \frac23(k^2-3)dS$, $\slashed\Delta(\slashed\delta^*_0dS) =
(k^2-6)\slashed\delta^*_0dS$, $\slashed\delta\slashed\delta^*V = \frac12(k^2-3)V$, $\slashed\Delta\slashed\delta^*V =
(k^2-5)\slashed\delta^*V$, $k^2 = l(l+2)$. At $N = 2$ the list is the source's (2.35).

*Proof.* $\slashed\delta dS = \slashed\Delta S$; $\slashed\Delta dS$ is Lemma 1.1 (a). $\slashed\delta^*dS =
\slashed\nabla^2S$ has trace $-k^2S$, which with (1.1) is the third identity; the next three hold as $\slashed g$ is
parallel. By Lemma 1.1 (b), $2\slashed\delta\slashed\delta^*dS = k^2dS+(k^2-N+1)dS-(N-1)dS$, so
$\slashed\delta\slashed\delta^*dS = (k^2-N+1)dS$, and $\slashed\delta(\slashed\delta^*_0dS) = (k^2-N+1-\frac{k^2}N)dS =
\frac{N-1}N(k^2-N)dS$. By Lemma 1.1 (c) with $\omega = dS$, $\slashed\Delta\slashed\delta^*dS =
(k^2-2N)\slashed\delta^*dS-2k^2\slashed gS$, and adding $\frac{k^2}N\slashed\Delta(\slashed gS) = \frac{k^4}N\slashed
gS$ gives $\slashed\Delta\slashed\delta^*_0dS = (k^2-2N)\slashed\delta^*_0dS$, the $\slashed gS$ terms cancelling. For
$V$: the first identity is the definition; Lemma 1.1 (b) gives $\slashed\delta\slashed\delta^*V = \frac12(k^2-1-N+1)V$;
$\mathrm{tr}\,\slashed\delta^*V = -\slashed\delta V = 0$; Lemma 1.1 (c) gives $(k^2-1-N-1)\slashed\delta^*V$. The $T$
line is the definition. (1.3): $S\in\mathcal S_1$ is the restriction of a linear function $L$, and by the Gauss formula
$\slashed\nabla^2S(X,Y) = D^2L(X,Y)-\langle X,Y\rangle dL(\hat x) = -\langle X,Y\rangle S$, so $\slashed\delta^*_0dS =
-S\slashed g+\frac1N\slashed g\,NS = 0$; and $V\in\mathcal V_1$ is Killing by Lemma 1.4 (2). $\square$

**Lemma 1.6 (decomposition; [Hin26] p. 64 at n = 4).** (1) Every $S\in C^\infty(\mathbb S^N)$ is a sum
$\sum_{l\ge0}S_l$, $S_l\in\mathcal S_l$. (2) Every smooth 1-form is a sum of scalar type $l\ge1$ and vector type $l\ge1$
1-forms. (3) Every smooth symmetric 2-tensor is a sum of scalar type $l\ge0$, vector type $l\ge2$ and tensor type
$l\ge2$ tensors; in the scalar type, $\slashed\delta^*_0dS$ is absent for $l\le1$ by (1.3). All sums converge in
$C^\infty$.

*Proof.* (1) is Lemma 1.4 (1) with the spectral decomposition of $\slashed\Delta$. (2) $\slashed\delta\omega$ has mean
zero; let $S$ be the mean-zero solution of $\slashed\Delta S = \slashed\delta\omega$, so that $V := \omega-dS$ is
co-closed, and expand $S$ by (1) and $V$ by Lemma 1.4 (4). (3) Write $h = \frac1N(\mathrm{tr}\,h)\slashed g+h_0$ with
$h_0$ trace-free. On trace-free tensors the adjoint of $\slashed\delta^*_0$ is $\slashed\delta$, and
$\slashed\delta^*_0$ has injective principal symbol ($\xi\otimes_s\omega-\frac1N\slashed g\langle\xi,\omega\rangle = 0$
forces $\omega = 0$ for $\xi\ne0$ as $N\ge2$), so $\slashed\delta\slashed\delta^*_0$ is elliptic and self-adjoint;
solving $\slashed\delta\slashed\delta^*_0\omega = \slashed\delta h_0$, which is possible as $\slashed\delta h_0$ is
orthogonal to $\ker\slashed\delta\slashed\delta^*_0 = \ker\slashed\delta^*_0$, gives $h_0 = \slashed\delta^*_0\omega+T$
with $\omega$ smooth and $T$ trace-free and divergence-free. Expand $\omega$ by (2), using $\slashed\delta^*_0V =
\slashed\delta^*V$ for co-closed $V$ and (1.3) for $l = 1$, $T$ by Lemma 1.4 (4), and $\mathrm{tr}\,h$ by (1). $\square$

**Definition 1.7 ([Hin26] Definition 2.28 at n = 4).** For $a\in\mathbb R^4$, $S(a) := a\cdot\frac x{|x|}\in\mathcal
S_1$; for $A\in\mathfrak{so}(4)$, $V(A) := (Ax)\cdot dx$, which restricted to $\mathbb S^3$ lies in $\mathcal V_1$ (the
dual of the rotation field $Ax\cdot\partial_x$), and $A\mapsto V(A)$ is an isomorphism $\mathfrak{so}(4)\to\mathcal V_1$
by Lemma 1.4 (2) (both are six-dimensional). Conversely, for $S\in\mathcal S_1$ and $V\in\mathcal V_1$ (or their
complexifications) $a(S)$ and $A(V)$ denote the unique $a$ and $A$ with $S = S(a)$, $V = V(A)$. As in the source, $S(a)$
is homogeneous of degree 0 and $V(A)$ is dual, with respect to the Euclidean metric, to a rotation field. The source's
$V(a) = (a\times x)\cdot dx$, $a\in\mathbb R^3$, is the case $\mathfrak{so}(3)\cong\mathbb R^3$.

## 2. The Minkowski operators at n = 4 ([Hin26] section 2.4.1)

### 2.1 Coordinates, splittings, and the metric

On $\mathbb R^{1+4}$ use $t\in\mathbb R$, $r = |x|>0$, $\omega = \frac x{|x|}\in\mathbb S^3$ for $0\ne x\in\mathbb R^4$,
and
$$t_* := t-r,\qquad\rho := r^{-1},\qquad\bar x^0 := t+r,\qquad\bar x^1 := t-r.\tag{2.1}$$
The level sets of $\bar x^0$, $\bar x^1$ are null. The bundle splittings are those of the source's (2.37b) with $\mathbb
S^3$ in place of $\mathbb S^2$:
$$T^*\mathbb R^{1+4} = \langle d\bar x^0\rangle\oplus\langle d\bar x^1\rangle\oplus rT^*\mathbb S^3,$$
$$S^2T^*\mathbb R^{1+4} = \langle(d\bar x^0)^2\rangle\oplus\langle2\,d\bar x^0d\bar x^1\rangle\oplus\big(2\,
d\bar x^0\otimes_srT^*\mathbb S^3\big)
\oplus\langle(d\bar x^1)^2\rangle\oplus\big(2\,
d\bar x^1\otimes_srT^*\mathbb S^3\big)\oplus r^2S^2T^*\mathbb S^3;\tag{2.2}$$
that is, $(\omega_0,\omega_1,\slashed\omega)$ is the covector $\omega_0\,d\bar x^0+\omega_1\,d\bar x^1+r\slashed\omega$,
and $(a,b,c,e,f,q)$ the symmetric tensor $a(d\bar x^0)^2+2b\,d\bar x^0d\bar x^1+2\,d\bar x^0\otimes_src+e(d\bar
x^1)^2+2\,d\bar x^1\otimes_srf+r^2q$, with $2\alpha\otimes_s\beta := \alpha\otimes\beta+\beta\otimes\alpha$ and
$\alpha\beta := \alpha\otimes_s\beta$. In Cartesian terms, $r\slashed\omega$ is the tangential field $V$ with
$V^\flat|_{\mathbb S^3} = \slashed\omega$ of the ambient picture, extended homogeneously of degree 0, and $r^2q$ is
likewise the tangential matrix field of $q$: $dx^i$ pulls back to $r\,\partial_a\hat x^i\,dy^a$ on the sphere of radius
$r$. Neither identification depends on $(t,r)$. The Minkowski metric and its dual are
$$\bar g = -dt^2+dr^2+r^2\slashed g = -d\bar x^0d\bar x^1+r^2\slashed g,\qquad
\bar g^{-1} = -4\partial_0\otimes_s\partial_1+r^{-2}\slashed g^{-1}
= 2\rho\partial_{t_*}\otimes_s\rho\partial_\rho+\rho^2\big((\rho\partial_\rho)^2+\slashed g^{-1}\big),\tag{2.3}$$
with $\partial_0 := \partial_{\bar x^0}$, $\partial_1 := \partial_{\bar x^1}$ in the coordinates $(\bar x^0,\bar
x^1,\omega)$; $\partial_0 = -\frac12\rho^2\partial_\rho$, $\partial_1 = \partial_{t_*}+\frac12\rho^2\partial_\rho$,
$\partial_0r = -\partial_1r = \frac12$. In the splitting (2.2), $\bar g = (0,-\frac12,0,0,0,\slashed g)$, $\mathrm{tr}
:= \mathrm{tr}_{\bar g} = (0,-4,0,0,0,\mathrm{tr})$, and $G := I-\frac12\bar g\,\mathrm{tr}$ (the operator $G_g =
I-\frac12g\,\mathrm{tr}_g$ of [Hin26], defined the same way in every dimension, and the one `lin5.py` uses at $n = 4$)
is
$$G = \begin{pmatrix}1&0&0&0&0&0\\0&0&0&0&0&\frac14\mathrm{tr}\\0&0&1&0&0&0\\0&0&0&1&0&0\\0&0&0&0&1&0\\
0&2\slashed g&0&0&0&\slashed G\end{pmatrix},
\qquad\slashed G := I-\tfrac12\slashed g\,\mathrm{tr},\tag{2.4}$$
as in the source's (2.39b): $\mathrm{tr}\,h = -4b+\mathrm{tr}\,q$, so $Gh = (a,\frac14\mathrm{tr}\,q,c,e,f,q+2b\slashed
g-\frac12\slashed g\,\mathrm{tr}\,q)$. The Christoffel symbols of $\bar g$ in the coordinates $\bar x^0,\bar x^1$ and
coordinates $y^a$ on $\mathbb S^3$ vanish except for
$$\bar\Gamma^c_{0b} = \bar\Gamma^c_{b0} = \tfrac12r^{-1}\delta^c_b,\quad\bar\Gamma^c_{1b} = \bar\Gamma^c_{b1}
= -\tfrac12r^{-1}\delta^c_b,\quad
\bar\Gamma^0_{ab} = -r\slashed g_{ab},\quad\bar\Gamma^1_{ab} = r\slashed g_{ab},\quad\bar\Gamma^c_{ab}
= \slashed\Gamma^c_{ab},\tag{2.5}$$
as in the source's (2.40): $\bar g_{01} = -\frac12$, $\bar g^{01} = -2$, $\bar g_{ab} = r^2\slashed g_{ab}$, and for
example $\bar\Gamma^0_{ab} = \frac12\bar g^{01}(-\partial_1\bar g_{ab}) = -r\slashed g_{ab}$, $\bar\Gamma^c_{0b} =
\frac12r^{-2}\slashed g^{cd}\partial_0(r^2)\slashed g_{bd}$. The scalar wave operator $\bar\Box u = -\bar
g^{\mu\nu}u_{;\mu\nu}$ is
$$\bar\Box = 4\partial_0\partial_1+\tfrac3r(\partial_1-\partial_0)+r^{-2}\slashed\Delta
= -2\partial_{t_*}\rho(\rho\partial_\rho-\tfrac32)
+\rho^2\big(-(\rho\partial_\rho)^2+2\rho\partial_\rho+\slashed\Delta\big).\tag{2.6}$$
Indeed $\bar g^{ab}\bar\Gamma^0_{ab} = -\frac Nr$ and $\bar g^{ab}\bar\Gamma^1_{ab} = \frac Nr$ at $N = 3$; and with $D
:= \rho\partial_\rho$, $\rho^2\partial_\rho\,\rho^2\partial_\rho = \rho^2(D+1)D$, so $4\partial_0\partial_1 = -2\rho
D\partial_{t_*}-\rho^2(D^2+D)$ and $\frac Nr(\partial_1-\partial_0) = N\rho\partial_{t_*}+N\rho^2D$. For general $N$,
(2.6) reads $-2\partial_{t_*}\rho(D-\frac N2)+\rho^2(-D^2+(N-1)D+\slashed\Delta)$; at $N = 2$ it is the source's.
Equivalently $\bar\Box = \partial_t^2-\partial_r^2-\frac Nr\partial_r+r^{-2}\slashed\Delta$.

### 2.2 The operators in the splittings

**Lemma 2.1 ([Hin26] Lemma 2.29 at n = 4).** In the coordinates $t_*,\rho,\omega$ and the splittings (2.2), with
$\slashed\Delta$ the tensor Laplacian acting componentwise on the summands and $D := \rho\partial_\rho$:

(1) (1-forms.) $\bar\Box = -2\partial_{t_*}\rho(D-\frac32)+{}^b\bar\Box(0)$, where
$${}^b\bar\Box(0) = \rho^2\Big(-D^2+2D+\slashed\Delta+\begin{pmatrix}\frac32&-\frac32&-\slashed\delta\\
-\frac32&\frac32&\slashed\delta\\-2d&2d&1\end{pmatrix}\Big);$$
and
$$\bar\delta^* = \begin{pmatrix}0&0&0\\\frac12&0&0\\0&0&0\\0&1&0\\0&0&\frac12\\
0&0&0\end{pmatrix}\partial_{t_*}+{}^b\bar\delta^*(0),\qquad
{}^b\bar\delta^*(0) = \rho\begin{pmatrix}-\frac12D&0&0\\\frac14D&-\frac14D&0\\\frac12d&0&-\frac14(D+1)\\0&\frac12D&0\\
0&\frac12d&\frac14(D+1)\\
\slashed g&-\slashed g&\slashed\delta^*\end{pmatrix}.$$

(2) (Symmetric 2-tensors.) $\bar\Box = -2\partial_{t_*}\rho(D-\frac32)+{}^b\bar\Box(0)$, where
$${}^b\bar\Box(0) = \rho^2\Big(-D^2+2D+\slashed\Delta+\begin{pmatrix}3&-3&-2\slashed\delta&0&0&-\frac12\mathrm{tr}\\
-\frac32&3&\slashed\delta&-\frac32&-\slashed\delta&\frac12\mathrm{tr}\\
-2d&2d&\frac72&0&-\frac52&-\slashed\delta\\
0&-3&0&3&2\slashed\delta&-\frac12\mathrm{tr}\\
0&-2d&-\frac52&2d&\frac72&\slashed\delta\\
-2\slashed g&4\slashed g&-4\slashed\delta^*&-2\slashed g&4\slashed\delta^*&2\end{pmatrix}\Big);\tag{2.7}$$
and
$$\bar\delta = \begin{pmatrix}2&0&0&0&0&0\\0&2&0&0&0&0\\0&0&2&0&0&0\end{pmatrix}\partial_{t_*}+{}^b\bar\delta(0),\qquad
{}^b\bar\delta(0) = \rho\begin{pmatrix}D-3&-D+3&\slashed\delta&0&0&\frac12\mathrm{tr}\\
0&D-3&0&-D+3&\slashed\delta&-\frac12\mathrm{tr}\\
0&0&D-4&0&-D+4&\slashed\delta\end{pmatrix}.\tag{2.8}$$

For general $N$ the same holds with $\frac32$ and $2D$ in the scalar part replaced by $\frac N2$ and $(N-1)D$; with the
1-form matrix entries $\pm\frac32$ replaced by $\pm\frac N2$; with the entries $3,-3,-\frac32,\frac72,-\frac52$ of (2.7)
replaced by $N,-N,-\frac N2,\frac{N+4}2,-\frac{N+2}2$; and with $3,4$ in (2.8) replaced by $N,N+1$; $\bar\delta^*$ does
not depend on $N$. At $N = 2$ this is [Hin26] Lemma 2.29, entry by entry.

*Proof.* We prove the general-$N$ statement.

*The wave operator.* In Cartesian coordinates the Christoffel symbols of $\bar g$ vanish, so $\bar\Box$ acts on each
Cartesian component of a tensor as the scalar operator $\partial_t^2-\partial_r^2-\frac
Nr\partial_r+r^{-2}\slashed\Delta$, which on a Cartesian component, regarded as a function of $(t,r)$ with values in
functions on $\mathbb S^N$, is $L_0+r^{-2}\Delta^e$, $L_0 := \partial_t^2-\partial_r^2-\frac Nr\partial_r$. Write
$\Box_c := L_0+r^{-2}\slashed\Delta$ acting componentwise in the splitting; by the computation of (2.6), $\Box_c =
-2\partial_{t_*}\rho(D-\frac N2)+\rho^2(-D^2+(N-1)D+\slashed\Delta)$. Write $\alpha := dt = \frac12(d\bar x^0+d\bar
x^1)$ and $\beta := dr = \frac12(d\bar x^0-d\bar x^1) = \hat x\cdot dx$.

1-forms: $\omega_0\,d\bar x^0+\omega_1\,d\bar x^1+r\slashed\omega = (\omega_0+\omega_1)\alpha+(\omega_0-\omega_1)\hat
x\cdot dx+V\cdot dx$ with $V$ the field of $\slashed\omega$. By (1.2a) and (1.2b),
$$\bar\Box\omega = A\,\alpha+B\,\beta+W\cdot dx,\quad A = \Box_c(\omega_0+\omega_1),\quad B
= \Box_c(\omega_0-\omega_1)+Nr^{-2}(\omega_0-\omega_1)-2r^{-2}\slashed\delta\slashed\omega,$$
$$W = \big(\Box_c+r^{-2}\big)\slashed\omega-2r^{-2}d(\omega_0-\omega_1),$$
and $A\alpha+B\beta = \frac12(A+B)d\bar x^0+\frac12(A-B)d\bar x^1$, which is (1).

2-tensors: in terms of $\alpha$ and $\beta$, $h = (a,b,c,e,f,q)$ is $h = \mathsf A\alpha^2+2\mathsf X\alpha\beta+\mathsf
B\beta^2+2\alpha\otimes_s\mathsf W+2\beta\otimes_s\mathsf U+\mathsf Q$, where $\mathsf A = a+2b+e$, $\mathsf X = a-e$,
$\mathsf B = a-2b+e$, $\mathsf W = c+f$, $\mathsf U = c-f$ (as tangential fields) and $\mathsf Q$ the field of $q$; in
Cartesian components, $h_{tt} = \mathsf A$, $(h_{ti}) = \mathsf X\hat x+\mathsf W$, $(h_{ij}) = \mathsf B\hat
x\otimes\hat x+\hat x\odot\mathsf U+\mathsf Q$. By Lemma 1.2,
$$(\bar\Box h)_{tt} = \Box_c\mathsf A,\qquad(\bar\Box h)_{t\cdot} = T_X\hat x+T_W,\qquad(\bar\Box h)_{\cdot\cdot}
= T_B\hat x\otimes\hat x+\hat x\odot T_U+T_Q,$$
$$T_X = \Box_c\mathsf X+Nr^{-2}\mathsf X-2r^{-2}\slashed\delta\mathsf W,\qquad T_W
= (\Box_c+r^{-2})\mathsf W-2r^{-2}d\mathsf X,$$
$$T_B = \Box_c\mathsf B+2Nr^{-2}\mathsf B-4r^{-2}\slashed\delta\mathsf U-2r^{-2}\mathrm{tr}\,q,\qquad
T_U = (\Box_c+(N+3)r^{-2})\mathsf U-2r^{-2}d\mathsf B-2r^{-2}\slashed\delta q,$$
$$T_Q = (\Box_c+2r^{-2})q-2r^{-2}\mathsf B\slashed g-4r^{-2}\slashed\delta^*\mathsf U.$$
Inverting, the components of $\bar\Box h$ in (2.2) are $a' = \frac14(\Box_c\mathsf A+T_B)+\frac12T_X$, $b' =
\frac14(\Box_c\mathsf A-T_B)$, $e' = \frac14(\Box_c\mathsf A+T_B)-\frac12T_X$, $c' = \frac12(T_W+T_U)$, $f' =
\frac12(T_W-T_U)$, $q' = T_Q$. Substituting:
$$a' = \Box_ca+r^{-2}(Na-Nb-2\slashed\delta c-\tfrac12\mathrm{tr}\,q),\qquad
b' = \Box_cb+r^{-2}(-\tfrac N2a+Nb-\tfrac N2e+\slashed\delta c-\slashed\delta f+\tfrac12\mathrm{tr}\,q),$$
$$e' = \Box_ce+r^{-2}(-Nb+Ne+2\slashed\delta f-\tfrac12\mathrm{tr}\,q),\qquad
c' = \Box_cc+r^{-2}(-2da+2db+\tfrac{N+4}2c-\tfrac{N+2}2f-\slashed\delta q),$$
$$f' = \Box_cf+r^{-2}(-2db+2de-\tfrac{N+2}2c+\tfrac{N+4}2f+\slashed\delta q),\qquad
q' = \Box_cq+r^{-2}(-2\slashed ga+4\slashed gb-4\slashed\delta^*c-2\slashed ge+4\slashed\delta^*f+2q),$$
which is (2) for $\bar\Box$. (For instance, in $c'$ the coefficient of $c$ is $\frac12+\frac{N+3}2$, from
$\frac12(\Box_c+r^{-2})\mathsf W$ and $\frac12(\Box_c+(N+3)r^{-2})\mathsf U$; the coefficient of $da$ is $-1-1$, from
$-r^{-2}d\mathsf X$ and $-r^{-2}d\mathsf B$.)

*The symmetric gradient.* From (2.5), for a 1-form with coordinate components $\omega_0,\omega_1$, $\omega_b =
r\slashed\omega_b$: $\bar\nabla_0\omega_0 = \partial_0\omega_0$, $\bar\nabla_1\omega_1 = \partial_1\omega_1$,
$\bar\nabla_0\omega_1 = \partial_0\omega_1$, $\bar\nabla_1\omega_0 = \partial_1\omega_0$, $\bar\nabla_0\omega_b =
r\partial_0\slashed\omega_b$, $\bar\nabla_1\omega_b = r\partial_1\slashed\omega_b$, $\bar\nabla_b\omega_0 =
\partial_b\omega_0-\frac12\slashed\omega_b$, $\bar\nabla_b\omega_1 = \partial_b\omega_1+\frac12\slashed\omega_b$,
$\bar\nabla_a\omega_b = r\slashed\nabla_a\slashed\omega_b+r\slashed g_{ab}(\omega_0-\omega_1)$. Symmetrising and reading
off the components of (2.2): $a = \partial_0\omega_0$, $b = \frac12(\partial_0\omega_1+\partial_1\omega_0)$, $c =
\frac12\partial_0\slashed\omega+\frac\rho2(d\omega_0-\frac12\slashed\omega)$, $e = \partial_1\omega_1$, $f =
\frac12\partial_1\slashed\omega+\frac\rho2(d\omega_1+\frac12\slashed\omega)$, $q =
\rho(\slashed\delta^*\slashed\omega+\slashed g(\omega_0-\omega_1))$; with $\partial_0 = -\frac12\rho D$, $\partial_1 =
\partial_{t_*}+\frac12\rho D$ this is the stated $\bar\delta^*$. No trace over the sphere occurs, so $N$ does not enter.

*The divergence.* $(\bar\delta h)_\nu = -\bar g^{\mu\kappa}\bar\nabla_\mu h_{\kappa\nu} =
2(\bar\nabla_0h_{1\nu}+\bar\nabla_1h_{0\nu})-r^{-2}\slashed g^{ab}\bar\nabla_ah_{b\nu}$, with $h_{00} = a$, $h_{01} =
b$, $h_{0b} = rc_b$, $h_{11} = e$, $h_{1b} = rf_b$, $h_{ab} = r^2q_{ab}$. From (2.5): $\bar\nabla_0h_{10} =
\partial_0b$, $\bar\nabla_1h_{00} = \partial_1a$, $\slashed g^{ab}\bar\nabla_ah_{b0} = -r\slashed\delta c+rN(a-b)-\frac
r2\mathrm{tr}\,q$; $\bar\nabla_0h_{11} = \partial_0e$, $\bar\nabla_1h_{01} = \partial_1b$, $\slashed
g^{ab}\bar\nabla_ah_{b1} = -r\slashed\delta f+rN(b-e)+\frac r2\mathrm{tr}\,q$; $\bar\nabla_0h_{1c} = r\partial_0f_c$,
$\bar\nabla_1h_{0c} = r\partial_1c_c$, $\slashed g^{ab}\bar\nabla_ah_{bc} = r^2(-\slashed\delta q+(N+1)(c-f))_c$, the
$N+1$ being $\slashed g^{ab}\slashed g_{ab}+1$. Hence $(\bar\delta h)_0 =
2\partial_{t_*}a+\rho((D-N)a+(-D+N)b+\slashed\delta c+\frac12\mathrm{tr}\,q)$, $(\bar\delta h)_1 =
2\partial_{t_*}b+\rho((D-N)b+(-D+N)e+\slashed\delta f-\frac12\mathrm{tr}\,q)$, and the $rT^*\mathbb S^N$ component is
$2\partial_{t_*}c+\rho((D-N-1)c+(-D+N+1)f+\slashed\delta q)$.

Setting $N = 2$ reproduces every entry of the source's Lemma 2.29 ((2.41), (2.42), and the 1-form statements); setting
$N = 3$ gives (1)-(2). Checked by machine: `harm5.py` K5 (section 2.3). $\square$

### 2.3 Types, and the indicial roots by type

Applying Lemma 1.6 to each component of a tensor in the splittings (2.2) at each sphere of constant $(t_*,\rho)$ gives
the types of the source's (2.43)-(2.44), with $\mathbb S^3$ harmonics, and one more:
$$\text{s0 1-forms: }(aS,bS,0),\ S\in\mathcal S_0;\quad\text{sl 1-forms, }l\ge1\text{: }(aS,bS,c\,
dS),\ S\in\mathcal S_l;\quad
\text{vl 1-forms, }l\ge1\text{: }(0,0,cV),\ V\in\mathcal V_l;\tag{2.9}$$
and, writing the last component of (2.2) as $pS\slashed g+q\slashed\delta^*_0dS$, $q\slashed\delta^*V$ or $\tau T$,
$$\begin{aligned}&\text{s0: }(aS,bS,0,eS,0,pS\slashed g),\ S\in\mathcal S_0;\qquad
\text{s1: }(aS,bS,c\,dS,eS,f\,dS,pS\slashed g),\ S\in\mathcal S_1;\\
&\text{sl, }l\ge2\text{: }(aS,bS,c\,dS,eS,f\,dS,pS\slashed g+q\slashed\delta^*_0dS),\ S\in\mathcal S_l;\qquad
\text{v1: }(0,0,cV,0,fV,0),\ V\in\mathcal V_1;\\
&\text{vl, }l\ge2\text{: }(0,0,cV,0,fV,q\slashed\delta^*V),\ V\in\mathcal V_l;\qquad
\text{tl, }l\ge2\text{: }(0,0,0,0,0,\tau T),\ T\in\mathcal T_l,\end{aligned}\tag{2.10}$$
with $a,b,c,e,f,p,q,\tau$ functions of $(t_*,\rho)$. The tensor type tl is new at $n = 4$. The operators of Lemma 2.1
are built from $d$, $\slashed\delta$, $\slashed\delta^*$, $\mathrm{tr}$, $\slashed g\,\cdot$, $\slashed\Delta$ and
constants, and by (1.2)-(1.3) each of these maps the components of a type to components of the same type, degree and
harmonic; so the operators of Lemma 2.1 preserve the type, the degree $l$ and the particular $S$, $V$ or $T$, and act on
each type by a matrix of operators in $(t_*,\rho)$. For example, on sl 1-forms, $l\ge1$, ${}^b\bar\Box(0)$ is $\rho^2$
times
$$-D^2+2D+\begin{pmatrix}k^2&0&0\\0&k^2&0\\0&0&k^2-2\end{pmatrix}+\begin{pmatrix}\frac32&-\frac32&-k^2\\
-\frac32&\frac32&k^2\\-2&2&1\end{pmatrix},
\qquad k^2 = l(l+2),\tag{2.11}$$
the analogue of the source's (2.45).

**Definition 2.2 ([Hin26] Definition 2.30 at n = 4).** On $X := [0,\infty)_\rho\times\mathbb S^3$, for
$A\in\rho^\alpha\mathrm{Diff}^m_{\mathrm b}(X)$ acting on one of the bundles above, $\lambda\in\mathbb C$ is a *scalar*,
*vector* or *tensor type $l$ indicial root* of $A$ if there is a nonzero $u$ of that type and degree with
$N(A)(\rho^\lambda u) = 0$.

Replacing $D$ by $\lambda$ in (2.11), the determinant is a constant times
$(\lambda+l+1)(\lambda+l)(\lambda+l-1)(\lambda-l-1)(\lambda-l-2)(\lambda-l-3)$, so $-l-1,-l,-l+1,l+1,l+2,l+3$ are the
scalar type $l$ indicial roots of ${}^b\bar\Box(0)$ on 1-forms (at $n = 3$ the source's six numbers are
$-l-1,-l,-l+1,l,l+1,l+2$).

**Lemma 2.3 (indicial roots of ${}^b\bar\Box(0)$ by type at n = 4).** For a finite list $\mathcal D$ of integers write
$R(\mathcal D)$ for the list of $-d$ and $d+2$, $d\in\mathcal D$, with multiplicity. The indicial roots of
${}^b\bar\Box(0)$, as the zeros of the determinant of its type-wise indicial matrix with multiplicity, are $R(\mathcal
D)$ with: on functions of degree $l$, $\mathcal D = (l)$; on 1-forms, s0: $(0,1)$; sl, $l\ge1$: $(l-1,l,l+1)$; vl:
$(l)$; on symmetric 2-tensors, s0: $(0,0,1,2)$; s1: $(0,1,1,1,2,3)$; sl, $l\ge2$: $(l-2,l-1,l,l,l,l+1,l+2)$; v1:
$(1,2)$; vl, $l\ge2$: $(l-1,l,l+1)$; tl, $l\ge2$: $(l)$. In particular every indicial root is an integer, the scalar
functions' roots are $-l$ and $l+2$ (at $n = 3$, $-l$ and $l+1$), and none lies in the open interval $(0,2)$.

*Proof.* The type-wise matrices are read off from Lemma 2.1 with the identities (1.2)-(1.3) (for the 2-tensor types they
are $7\times7$ for sl, $l\ge2$, and smaller for the others), and their determinants, with $l$ symbolic, factor exactly
as stated (computed, exact: `harm5.py` K6). On the Cartesian side `harm5.py` K1-K3 compute the
determinants and assert them against the lists (with $l$ symbolic for functions and for the 1-form types sl, vl, and at
$l\le2$ for 2-tensors); K5 shows that the two matrices agree entry by entry with $l$ symbolic, which carries K6 to the
Cartesian side. $\square$

*Remark.* The pattern has a structural reason: $\bar\Box$ acts on Cartesian components as the scalar operator, whose
indicial roots on a degree-$d$ harmonic are $-d$ and $d+N-1$ by (2.6); $\mathcal D$ lists the harmonic degrees of the
Cartesian components of a tensor of the given type (the time component has degree $l$, and the spatial factors $\hat x$
and $dS$ shift the degree by one each way).

### 2.4 The symmetric gradient's indicial families

Reading off Lemma 2.1 (1) on the types s0, s1 and v1 (for s1 the entry $-1$ in the last row comes from
$\slashed\delta^*dS = -S\slashed g$ at $l = 1$, which holds at every $N$ by (1.2)-(1.3), as $k_1^2 = N$):
$$N_{s0}\big({}^b\bar\delta^*(0),\lambda\big) = \begin{pmatrix}-\frac\lambda2&0\\\frac\lambda4&-\frac\lambda4\\
0&\frac\lambda2\\1&-1\end{pmatrix},\qquad
N_{s1}\big({}^b\bar\delta^*(0),\lambda\big) = \begin{pmatrix}-\frac\lambda2&0&0\\\frac\lambda4&-\frac\lambda4&0\\
\frac12&0&-\frac14(\lambda+1)\\
0&\frac\lambda2&0\\0&\frac12&\frac14(\lambda+1)\\1&-1&-1\end{pmatrix},\qquad
N_{v1}\big({}^b\bar\delta^*(0),\lambda\big) = \begin{pmatrix}-\frac14(\lambda+1)\\
\frac14(\lambda+1)\end{pmatrix}.\tag{2.12}$$
These are the source's (2.46a)-(2.46c) unchanged.

**Lemma 2.4 (injectivity; the remark after [Hin26] (2.46) at n = 4).** For every type other than s0, s1, v1 and every
$\lambda\in\mathbb C$, $N_\bullet({}^b\bar\delta^*(0),\lambda)$ is injective; $N_{s0}$ and $N_{s1}$ are injective for
$\lambda\ne0$, and $N_{v1}$ for $\lambda\ne-1$. At the exceptional values the kernels are spanned by $(1,1)$ (from
$dt$), by $(1,-1,2)$ (from $dx^i$, with $S = \hat x_i$), and by the rotations $V\in\mathcal V_1$.

*Proof.* By Lemma 2.1 (1), ${}^b\bar\delta^*(0)$ is $\rho$ times an operator with coefficients polynomial in $D$ and
independent of $\rho$, so for $u$ of one type ${}^b\bar\delta^*(0)(\rho^\lambda u) =
\rho^{\lambda+1}N_\bullet({}^b\bar\delta^*(0),\lambda)u$, and $\rho^\lambda u$ does not depend on $t_*$. So if
$N_\bullet(\lambda)u = 0$ then $\omega := \rho^\lambda u$ satisfies $\bar\delta^*\omega = 0$ on $\mathbb
R_t\times(\mathbb R^4\setminus0)$, and so do its real and imaginary parts, as $\bar\delta^*$ is real. In Cartesian
coordinates a 1-form with $\partial_\mu\omega_\nu+\partial_\nu\omega_\mu = 0$ satisfies
$\partial_\lambda\partial_\mu\omega_\nu = 0$ (the identity $\partial_\lambda\partial_\mu\omega_\nu = \partial_\lambda
s_{\mu\nu}+\partial_\mu s_{\lambda\nu}-\partial_\nu s_{\lambda\mu}$, $s := \bar\delta^*\omega$), so on the connected set
$\mathbb R_t\times(\mathbb R^4\setminus0)$ it is affine, $\omega_\mu = a_\mu+B_{\mu\nu}x^\nu$ with $B$ antisymmetric.
The splitting (2.2) does not depend on $t$, so $\omega$ is independent of $t$, which forces $B_{\mu0} = 0$: $\omega$ is
a combination of $dt$, the $dx^i$ and the rotation forms $B_{ij}x^jdx^i$. These are homogeneous of degree 0, 0 and 1 in
$x$ and, in (2.2), of the types s0 ($dt = \frac12(d\bar x^0+d\bar x^1)$), s1 ($dx^i = \hat x_i\,dr+r\,d\hat x_i =
\frac12\hat x_i(d\bar x^0-d\bar x^1)+r\,d\hat x_i$) and v1 (by Definition 1.7). A nonzero $\rho^\lambda u$ of a single
type and degree is therefore one of these, with $\lambda = 0$, $0$ and $-1$ respectively. $\square$

(Checked by machine: `harm5.py` K4 computes the greatest common divisor of the maximal minors of
$N_\bullet({}^b\bar\delta^*(0),\lambda)$ from the Cartesian computation for s0, s1, s2, v1, v2: $\lambda$, $\lambda$,
$1$, $\lambda+1$, $1$.)

## 3. Findings, sources and labels

### 3.1 Findings

(H1) *The tensor type.* At $n = 4$ symmetric 2-tensors carry a third type, tl ($l\ge2$), absent on $\mathbb S^2$. It
enters every type-by-type statement downstream; [Hin26] Lemma 8.4's list at $n = 4$ already carries it (`lin5.py` E2,
tl: $\det N_L = c(\lambda+l)(\lambda-l-2)$), and Lemma 2.3 gives its free roots $-l$, $l+2$.

(H2) *The constants of Lemma 2.29.* The source's constants depend on $N$:
$\rho\partial_\rho-1\to\rho\partial_\rho-\frac32$ and $\rho\partial_\rho\to2\rho\partial_\rho$ in the scalar part;
$\pm1\to\pm\frac32$ in the 1-form matrix; $2,-2,-1,3,-2\to3,-3,-\frac32,\frac72,-\frac52$ in (2.7); $2,3\to3,4$ in
(2.8). $\bar g^{-1}$, $G$, the Christoffel symbols and $\bar\delta^*$ are unchanged. A proof at $n = 4$ that carried the
source's constants over would get every indicial root by type wrong.

(H3) *The identities.* (2.35) at $N = 3$: $\slashed\Delta dS = (k^2-2)dS$, $\slashed\delta(\slashed\delta^*_0dS) =
\frac23(k^2-3)dS$, $\slashed\Delta(\slashed\delta^*_0dS) = (k^2-6)\slashed\delta^*_0dS$,
$\slashed\delta\slashed\delta^*V = \frac12(k^2-3)V$, $\slashed\Delta\slashed\delta^*V = (k^2-5)\slashed\delta^*V$, $k^2
= l(l+2)$; and $\slashed\delta^*_0 = \slashed\delta^*+\frac13\slashed g\slashed\delta$. The special low degrees (2.34)
are unchanged in form: $\slashed\delta^*_0dS = 0$ at $l = 1$, $\slashed\delta^*V = 0$ at $l = 1$, with $\mathcal
V_1\cong\mathfrak{so}(4)$ six-dimensional.

(H4) *Indicial roots.* The free roots on a degree-$d$ Cartesian component are $-d$ and $d+2$ (source: $-d$, $d+1$);
Lemma 2.3 lists them by type. The interval $(0,2)$ free of roots is the free operator's indicial gap at $n = 4$ (source:
$(0,1)$).

(H5) *The symmetric gradient.* (2.46) and its injectivity remark hold at $n = 4$ unchanged, with the rotation algebra
$\mathfrak{so}(4)$ in place of $\mathfrak{so}(3)$; the proof given here (Lemma 2.4) replaces the source's "explicit
computation, or the geometric fact" by the second argument written out.

(H6) *What the source cites and this part proves.* The source cites [Hin23b] section 6.2 for Lemma 2.29 and [Hig87] for
the harmonics on $\mathbb S^2$. Here Lemma 2.1 is proved by the Cartesian route (componentwise action plus the ambient
identities of Lemma 1.2), Lemma 1.4 proves the spectra on co-closed 1-forms and on trace-free divergence-free tensors
from the same identities, and Lemma 1.1 proves the commutation used for (2.35) from the Ricci identity, so no result on
the harmonics of $\mathbb S^2$ ([Hig87]) is used at $N = 3$; what is quoted is the classical theory of harmonic
polynomials (Lemma 1.4 (1)) and the spectral theorem for elliptic operators (Lemma 1.4 (4), Lemma 1.6 (3)). The $N = 2$
control of K5 takes the vector-type basis $x\times\nabla S$ to be $\mathcal V_l$, which is the READ fact after
Definition 1.3.

### 3.2 Sources

READ: [Hin26] pp. 63-67 (section 2.4: Notation 2.26, Definitions 2.27-2.28, (2.34)-(2.46), Lemma 2.29, Definition 2.30
and the remarks after (2.45) and (2.46)), arXiv:2606.28253v2, full text. Not read, and not relied on: [Hin23b] section
6.2, [Hig87].

### 3.3 Labels

Every statement of sections 1-2 is proved here at general $N$ and read at $N = 3$, from classical facts quoted without
proof: the decomposition $\mathcal P_l = \mathcal H_l\oplus|x|^2\mathcal P_{l-2}$ of the homogeneous polynomials and
the density of polynomials in $C(\mathbb S^N)$ (Lemma 1.4 (1), with the dimension count $\dim\mathcal S_l = (l+1)^2$
given there), and the spectral theorem and elliptic regularity for self-adjoint elliptic operators on a compact manifold
(Lemma 1.4 (4), Lemma 1.6 (3)). The comparison statements about $\mathbb S^2$ are READ. Lemma 2.3's factorizations are
exact computations (K6), and Lemma 2.1 and (1.2) are also checked by machine at $N = 2$ and $N = 3$ with $l$ symbolic
(K5, at two points for $N = 3$). `harm5.py --selftest` runs K1-K8 and their controls; K1-K3 assert the determinants of
the Cartesian side against the degree lists of Lemma 2.3 (with $l$ symbolic for functions and for the 1-form types sl,
vl, and at $l\le2$ for 2-tensors).

### 3.4 The ninety-second verifier (D221)

The ninety-second verifier read this part line by line, rederived every proof step, checked Lemma 1.2 by machine at
$N = 2$ on generic fields (with a failing control), recomputed every K5 matrix at lin5.py's second point, and traced
each Cartesian basis element against (2.2). No major finding. *Minor 1* (labels): section 3.3 and (H6) said that no
outside result on harmonics is used; Lemma 1.4 (1) quotes the classical decomposition of harmonic polynomials and the
density of polynomials, and Lemma 1.4 (4) and Lemma 1.6 (3) the spectral theorem and elliptic regularity. Repaired: both
now name what is quoted; no statement changes. *Minor 2* (harm5.py): K2 and K3 asserted only closure, and the proof of
Lemma 2.3 attributed the symbolic determinants to K1-K3. Repaired: the selftest asserts the K2 and K3 determinants
against the degree lists, the docstring says which side carries which assertion, and the proof of Lemma 2.3 says that K5
carries K6 to the Cartesian side. *Nits:* K5 now also runs at the second point (all operators at $N = 3$, the 1-form
operators at $N = 2$); a 2-tensor control (s1, box on 2-tensors) is added to the 1-form one; the vestigial `sign`
parameter is removed; Lemma 1.5 repeats $l\ge1$ and $l\ge2$; the tensor $z^{l-2}\beta\otimes\beta$ is now proved to lie
in $\mathcal T_l\otimes\mathbb C$; (H6) says that the $N = 2$ control rests on the READ description of $\mathcal V_l$.
The verifier also confirmed every repair of D217 to Part III.B.