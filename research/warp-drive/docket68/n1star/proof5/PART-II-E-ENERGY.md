# Part II.E. Energy estimates, and the global estimate at high frequencies, at n = 4

*Status.* Repairs read (D326: verifier 142 found the D207 repairs correct but one; that minor finding, Lemma 3.3 (b)'s
kernel, and one nit are seated, to be read). Verified. Written out in full (D205). Read line by line by the eighty-sixth
verifier, which re-derived Lemma 2.4 at $n = 4$ by machine (and at $n = 3$, reproducing the source's (8.10)), Lemma 2.5,
Propositions 3.2 and 3.4 and sections 4-6, and confirmed (E1)-(E13) at source. Its six minor findings (the order on the
extension region, the domain of the collar flow, the slab bookkeeping in the tame inductions, the support of $E_+$, the
definition of the extended $t^\flat$, and a hypothesis of Proposition 3.2) and its nits are seated (D207). The part is
labelled proved once the next reader has confirmed them. (E14) was narrowed on the eighty-eighth verifier's reading
(D212): the tame bounds (4.4), (5.6) and (6.2) are proved, and now stated, for orders constant and in $\mathbb N_0$ near
the face across which the source term is extended. This part proves, at spatial dimension $n = 4$, [Hin26c] section 8
(pp. 141-157): solvability of forward problems on bounded time slabs, with energy estimates, on edge-Sobolev spaces with
and without b-regularity and tame in it (the source's Lemma 8.1 and Propositions 8.3, 8.6, 8.9); the same in the black
hole interior with $r$ as the time function (Lemma 8.10, Propositions 8.11-8.13); and the global estimate (Theorem
8.14), which joins these to the microlocal estimate of Part II.D$'$. The source is [Hin26c] = P. Hintz,
arXiv:2606.28008v1 (printed page numbers). Parts II.A, II.A$'$, II.B, II.C, II.C$'$, II.D and II.D$'$ are cited as in
Part II.D$'$.

*Method.* The energy estimates are proved with a vector field multiplier, as in the source, at $n = 4$. Near $\mathscr
I^+$ the multiplier is a weighted edge vector field whose deformation tensor is positive in the time derivative only
through the weight's threshold; the other derivatives come from an exponential weight in time. Every first-order term of
the operator is kept as a pointwise quadratic form in the first derivatives, and every zeroth-order term is absorbed by a
Poincaré inequality with the exponential weight. So the fibre inner product need only make $\mathrm{Re}\,p_1$ large, and
not also make $\mathrm{Im}\,p_1$ and $p_0$ small as in the source. Solvability at all orders is proved from the energy
estimates for $P$ and for its adjoint by duality, and from microlocal regularity on slabs. That regularity needs the
radial estimates at the outgoing radial set over $\mathscr I^+$ localised in time, for $P$ and for $P^*$. The source
quotes the first from its Proposition 7.9 with a finite final time, which Part II.D found to rest on a sign that fails
off the characteristic set, and leaves the second to the reader. Section 3 proves both, with a time cut-off in the
function $t_*-\kappa x_I^{2\ell_I}$, which is monotone along the flow on a full neighbourhood of the radial set up to a
multiple of the principal symbol.

*Organisation.* Section 1: slabs and spaces, the operator near $\mathscr I^+$, extensions of the operator, duality.
Section 2: the energy estimates. Section 3: the localised radial estimates, regularity on slabs, solvability. Section 4:
b-regularity and the tame estimates. Section 5: the black hole interior. Section 6: the global estimate. Section 7:
findings.

## 1. Setting

### 1.1 Slabs and spaces

$\Omega$, $\Omega_* = \mathrm{cl}_M\{t^\flat_*\ge1\}$ and the time function $t^\flat_*$ are those of II.C (II.C Lemma
3.2); below $t^\flat := t^\flat_*$, and $t_* = t-r$ is the coordinate of II.A Definition 1.3. $P$ is weakly admissible of
class $((d_0;k),(2\ell_I,\ell_+,\ell_K))$ relative to $P_0$ (II.C Definition 3.3), with $\epsilon_P :=
\|P-P_0\|_{(d_0;0),(2\ell_I,\ell_+,\ell_K)}$ small, so that the metric $g$ of $P$ satisfies the hypotheses of II.C Lemma
3.2: $dt^\flat$ is past timelike on $\Omega^\circ$, and $dr$ is future timelike on $\{r_0\le r\le r^\natural\}$, where
$r^\natural = \frac12(r_0+r_2)$. For $1\le T_0<T_1<\infty$ the *slab* is
$$\Omega_{T_0,T_1} := \Omega_*\cap\{T_0\le t^\flat\le T_1\}.$$
For $1-\eta_0\le T_0<1$ the slab is defined in the same way in the region $\Omega^-_*$ of Lemma 1.2 (iv), with
$P^{\mathrm{ext}}$ in place of $P$. In $M^\circ$ its boundary consists of the *initial face* $\{t^\flat = T_0\}$ and the
*final faces* $\{t^\flat = T_1\}$ and $\{r = r_0\}$, which are spacelike: their conormals $dt^\flat$, $dr$ are timelike,
and future directed causal vectors point out of the slab at the final faces and into it at the initial face. Its closure
meets $\partial M$ only in $\mathscr I^+\cap\{T_0\le t_*\le T_1\}$, as $t^\flat = t_*$ on $\mathscr I^+$ (II.C Lemma 3.2
(a)).

Near $\mathscr I^+$ at finite times we use $(t_*,x_I,\omega)$ with $x_I := r^{-1/2}$ (II.A Definition 1.3 (B)); it
differs from the $x_I = (t_*/r)^{1/2}$ of II.B section 7 by the factor $t_*^{1/2}$, which is smooth and positive at
finite times. The edge vector fields are spanned by $\partial_{t_*}$, $x_I\partial_{x_I}$ and $x_I\partial_\omega$, and
the b-vector fields by $\partial_{t_*}$, $x_I\partial_{x_I}$ and $\partial_\omega$; at finite times the e3b- and
eb-structures are the edge structure, and $\rho_+$, $\rho_K$ are smooth and positive. We write $H^{\mathsf s,2\alpha}_e
:= H^{\mathsf s,(2\alpha,0,0)}_{e3b}$ and $H^{(\mathsf s;k),2\alpha}_{e;b} := H^{(\mathsf s;k),(2\alpha,0,0)}_{e3b;b}$
(II.A section 4 and (8.1)), with the $L^2$-density $|dg|$. Near $\mathscr I^+$, $|dg|$ is a smooth positive multiple of
$r^3|dt_*\,dr\,d\omega| = 2x_I^{-8}|dt_*\,\frac{dx_I}{x_I}\,d\omega|$.

For a slab $\Omega' = \Omega_{T_0,T_1}$ put $U' := \Omega^\circ\cap\{t^\flat<T_1,r>r_0\}$, $V' :=
\Omega^\circ\cap\{t^\flat>T_0\}$ and $F' := \Omega\cap\{t^\flat\le T_1,r\ge r_0\}$, and define, with quotient norms,
$$H^{\mathsf s,2\alpha}(\Omega')^{\bullet,-} :=
\{u|_{U'}:u\in H^{\mathsf s,2\alpha}_e,\ \mathrm{supp}\,u\subset\{t^\flat\ge T_0\}\},
\qquad H^{\mathsf s,2\alpha}(\Omega')^{-,\bullet} :=
\{v|_{V'}:v\in H^{\mathsf s,2\alpha}_e,\ \mathrm{supp}\,v\subset F'\},$$
and $H^{(\mathsf s;k),2\alpha}(\Omega')^{\bullet,-}$, $H^{(\mathsf s;k),2\alpha}(\Omega')^{-,\bullet}$ likewise. The
first are distributions supported at the initial face and extendible at the final ones, the spaces of forward problems;
the second the reverse, the spaces of backward problems. We call $D(\Omega')$ the restrictions to $U'$ of functions in
$C^\infty_c(M^\circ)$ supported in $\{t^\flat>T_0\}$, and $D_*(\Omega')$ the restrictions to $V'$ of functions in
$C^\infty_c(M^\circ)$ supported in $\{t^\flat<T_1,r>r_0\}$.

### 1.2 The operator near $\mathscr I^+$

**Lemma 1.1 ([Hin26c] (8.3) at $n = 4$).** Near $\mathscr I^+$ at finite times, in $(t_*,x_I = r^{-1/2},\omega)$,
$$P-\tfrac12x_I^2\Big[-2\big(x_I\partial_{x_I}-3-2p_1\big)\partial_{t_*}+2x_I^2\Delta_{\mathbb S^3}+
t_*^{-1}p_0\Big]\in x_I^2C^{(d_0;k),2\ell_I}_{e;b}\mathrm{Diff}^2_e,\tag{1.1}$$
with $p_0$, $p_1$ of II.C Definition 3.3 and $\Delta_{\mathbb S^3}\ge0$ the Laplacian of the round sphere. Hence, for
covectors $\zeta = \zeta_{t_*}dt_*+\xi\frac{dx_I}{x_I}+\eta$, $G(\zeta)\equiv x_I^2(\xi\zeta_{t_*}+x_I^2|\eta|^2)$ modulo
$x_I^{2+2\ell_I}$ times a quadratic form in $(\zeta_{t_*},\xi,x_I\eta)$; that is, $g^{-1}\equiv
x_I^2(x_I\partial_{x_I}\otimes_s\partial_{t_*}+x_I^2\slashed g^{-1})$ with $a\otimes_sb := \frac12(a\otimes b+b\otimes
a)$, $\slashed g$ the round metric.

*Proof.* In the coordinates $\rho_+ = t_*^{-1}$, $x'_I := (t_*/r)^{1/2} = t_*^{1/2}x_I$ of II.C Lemma 3.4,
$x'_I\partial_{x'_I}$ at fixed $\rho_+$ is $-2r\partial_r = x_I\partial_{x_I}$ at fixed $t_*$, and
$x'_I\partial_{x'_I}-2\rho_+\partial_{\rho_+} = 2t_*\partial_{t_*}$ at fixed $r$. As $x_I'^{-2}\rho_+^{-2} = t_*x_I^{-2}$
and $x_I'^2 = t_*x_I^2$, II.C (3.3) reads
$2t_*x_I^{-2}P\equiv-2t_*(x_I\partial_{x_I}-3-2p_1)\partial_{t_*}+2t_*x_I^2\Delta_{\mathbb S^3}+p_0$, as $t_*$ commutes
with $x_I\partial_{x_I}$ and with multiplication by $p_1$. Multiply by $x_I^2/(2t_*)$; the remainder class becomes
$x_I^2C^{(d_0;k),2\ell_I}_{e;b}\mathrm{Diff}^2_e$, $t_*$ being bounded above and below. For the principal symbol,
$\sigma(x_I\partial_{x_I}) = i\xi$ and $\sigma(\partial_{t_*}) = i\zeta_{t_*}$. As a check of the signs: for Minkowski
space, with $\Box = -\partial_t^2+\partial_r^2+\frac3r\partial_r+r^{-2}\Delta_{\mathrm{lap}}$ and $\partial_r|_t =
\partial_r|_{t_*}-\partial_{t_*}$, $\partial_r|_{t_*} = -\frac12x_I^2\,x_I\partial_{x_I}$, one finds $-\Box =
x_I^2\big(-(x_I\partial_{x_I}-3)\partial_{t_*}-x_I^2\Delta_{\mathrm{lap}}\big)+O(x_I^4)\mathrm{Diff}^2_e$, which is (1.1)
with $p_0 = p_1 = 0$ and $\Delta_{\mathbb S^3} = -\Delta_{\mathrm{lap}}$. $\square$

At $n = 3$ the source prints the bracket of (1.1) as
$-2(x_I\partial_{x_I}-2(1+p_1))\partial_{t_*}+2x_I^2\slashed\Delta+p_0$ ([Hin26c] (8.3)): the constant $2 = n-1$ is $3$
here, and $p_0$ stands where the normal form gives $t_*^{-1}p_0$; section 7, (E1).

### 1.3 The fibre inner product

Let $\delta' > 0$. As in the proof of II.D Proposition 3.6 there is a smooth fibre inner product $h_I = \langle
A_I^{-1}\cdot,A_I^{-1}\cdot\rangle$ on $\mathbb C^N$ over a neighbourhood of $\mathrm{cl}(\mathscr I^+\cap\Omega)$,
extended independently of $x_I$, with
$$\mathrm{Re}_{h_I}p_1\ge\bar p_1-\delta'\quad\text{on }\mathrm{cl}(\mathscr I^+\cap\Omega).\tag{1.2}$$
The source asks also $|\mathrm{Im}_hp_1|<\epsilon$ and $\|p_0\|_h<\epsilon$ ([Hin26c] (8.4)); that is not needed below
(section 7, (E2)).

### 1.4 Extensions of the operator

The microlocal estimates of section 3 are applied on a neighbourhood of a slab, beyond its final faces, and, for $T_0 =
1$, below its initial face, where $P$ is not given.

**Lemma 1.2 (extension; [Hin26c] Lemma 8.5 and the paragraph after it).** There are $r^\sharp\in(r_0-\delta_0,r_0)$ and
an operator $P^{\mathrm{ext}}$ on $\{r\ge r^\sharp\}\cap\{t_*\ge\frac12\}$ such that: (i) $P^{\mathrm{ext}} = P$ on
$\Omega$; (ii) $P^{\mathrm{ext}}-P_0$ has coefficients bounded in the norms of $P-P_0$, in $C^{(d_0;k)}$ with the weights
of II.C Definition 3.3, by a constant times those of $P-P_0$; (iii) near $\mathscr I^+$, $P^{\mathrm{ext}}$ has the form
(1.1) with the data $p_0$, $\tilde p_1$ extended to $t_*\in[\frac12,1]$, and (1.2) holds for $t_*\in[1-\eta_0,1]$ with
$2\delta'$ in place of $\delta'$, for some $\eta_0>0$; (iv) $t^\flat$ extends to $\{r\ge r^\sharp,\ t_*\ge\frac12\}$, and
for $\epsilon_P$ small there is $\delta_0>0$ such that, after shrinking $\eta_0$: $dt^\flat$ is past timelike for the
metric of $P^{\mathrm{ext}}$ on the region $\Omega^-_*$, the union of $\{t^\flat\ge1,\ r\ge r^\sharp\}$ and of the collar
$\{1-\eta_0\le t^\flat\le1\}$ below its face $\{t^\flat = 1\}$ (in the collar coordinates of section 1.5), which lies in
$\{t_*>\frac12\}$; and $dr$ is future timelike on $\Omega^-_*\cap\{r^\sharp\le r\le r^\natural+\delta_0\}$.

*Proof.* Write $P_0$ and $P-P_0$ in a fixed frame as sums of coefficients times fixed operators $\mathrm{Id}$,
$\partial_{z^\mu}$, $\partial_{z^\mu}\partial_{z^\nu}$, $z = (t_*,x)$, as in the paragraph after [Hin26c] Lemma 8.5;
those of $P_0$ are independent of $t_*$. Extend each coefficient across $\{r = r_0\}$ by $E_0$ in the variable $r-r_0$
(with $(t_*,\omega)$ as parameters), and across $\{t_* = 1\}$ by $E_0$ in $t_*$ (with $(r,\omega)$, resp. $(x_I,\omega)$
near $\mathscr I^+$, as parameters). Seeley's operator preserves $C^{(d_0;k)}$-regularity and weights in the parameters,
which gives (ii), and acts on the data $p_0$, $\tilde p_1$ of (3.1)-(3.2) of II.C Definition 3.3 in the same way, which
gives the form in (iii). The extended $p_1$ is continuous in $t_*$ and equals $p_1$ at $t_* = 1$, so (1.2) persists with
$2\delta'$ on $[1-\eta_0,1]$. The extension of $P_0$ in $r$ keeps it stationary. (iv) $t^\flat$ is not extended by $E_0$
(Seeley's extension of a function is not given by the function's own formula, which is what is used below). On
$\{t_*\ge\frac12\}$ it is defined by the gluing formulae of the proof of II.C Lemma 3.2, with the constant $C$ there
taken $\ge4(r'_0+1)$, so that the overlap $\{r'_0+1\le r\le\frac12Ct_*\}$ of the regions being glued is non-empty for
every $t_*\ge\frac12$; the formulae make sense for $t_*>0$. In particular $t^\flat = t_*(1-(t_*/r)^{\ell_I})$ near
$\mathscr I^+$ (II.C Lemma 3.2 (a)) and $t^\flat = C'(t_*+r'_0)$ for $r\le r'_0-1$ (II.C Lemma 3.2 (c)), on all of
$\{t_*\ge\frac12\}$. *$dr$.* By II.C Lemma 3.2 (1) with $h = 0$, $dr$ is future timelike for $g_0$ on $\{r_0\le r\le
r^\natural\}$; $g_0$ is stationary and the range of $x$ is compact, so by continuity this holds on $\{r^\sharp\le r\le
r^\natural+\delta_0\}$ for $r^\sharp$ close to $r_0$ and $\delta_0$ small, and for the extended metric, which differs
from $g_0$ by $O(\epsilon_P)$ there. *$dt^\flat$.* For $r\le r'_0-1$, $dt^\flat = C'dt_*$, and $dt_*$ is past timelike
for $g_0$ there (II.C Lemma 3.2's proof, by (H6)), hence for the extended metric, by stationarity and continuity down to
$r^\sharp$. Near $\mathscr I^+$ the proof of II.C Lemma 3.2 bounds $g^{-1}-\bar g^{-1}$ in the basis used there by
$C(\epsilon_P+\rho_I^{1-\ell_I})\rho_I^{\ell_I}$, using $\rho_+\le1$ only to bound powers of $\rho_+$; for
$t_*\ge\frac12$, $\rho_+\le2$, and the argument applies with larger constants. On the rest of $\{t^\flat\le T\}$,
$\{x_I\ge c,\ r\ge r'_0-1\}$, which is compact at bounded $t_*$ (and $t_*\le T/C'$ on $\{t^\flat\le T\}\cap\Omega$ by
II.C Lemma 3.2 (b)), $dt^\flat$ is past timelike on $\Omega_*$ with a margin, hence on a neighbourhood, by continuity.
*The collar.* Near the face $\{t^\flat = 1\}$, which lies in $\{t_*\ge1\}$ by II.C Lemma 3.2 (b), $dt^\flat$ is past
timelike, so the field $Z/(-Zt^\flat)$ of section 1.5 is defined there; its flow from the face for times at most
$\eta_0$ sweeps the collar, which for $\eta_0$ small lies in the neighbourhood just found and in $\{t_*>\frac12\}$: near
$\mathscr I^+$ the flow is translation in $t_*$ by at most $2\eta_0$, and elsewhere at bounded times by compactness.
$\square$

### 1.5 Duality

*A collar.* There is a vector field $Z$ on a neighbourhood of $\Omega^-_*\cap\{t^\flat\le T_1+2\}$, an edge vector
field, equal to $-\partial_{t_*}$ near $\mathscr I^+$, with $Zt^\flat\le-c<0$ and, near $\{r = r_0\}$, $Zr\ge c$. Take
$Z := -\chi_I\partial_{t_*}+(1-\chi_I)\nabla t^\flat$ with $\chi_I = \chi_I(r)$ equal to 1 for $r\ge R$ and 0 for $r\le
R-1$, $R$ large. Near $\mathscr I^+$, $\partial_{t_*}t^\flat = 1-(1+\ell_I)(t_*/r)^{\ell_I}\ge\frac12$ by II.C Lemma 3.2
(a). On $\{r\le R\}$, $\nabla t^\flat$ is past timelike (II.C Lemma 3.2 (2) and Lemma 1.2 (iv)), so $Zt^\flat =
g^{-1}(dt^\flat,dt^\flat)<0$ there, with a negative bound on the compact part at bounded times, and $\nabla t^\flat\,r =
g^{-1}(dt^\flat,dr)>0$ near $r = r_0$, $dr$ being future timelike. Near $\mathscr I^+$ the flow $\Phi_\tau$ of $Z$ is
translation in $t_*$, which preserves the edge structure, the weight and the density; elsewhere it is a smooth flow on a
compact set. So $(\Phi_\tau)_*$ is bounded on $H^{m,2\alpha}_e$, $m\in\mathbb N_0$, uniformly for $|\tau|\le\tau_0$, and
strongly continuous at $\tau = 0$, by the chain rule and the density of $C^\infty_c$. As $Z$ and $\Phi_\tau$ are defined
only near $\Omega^-_*\cap\{t^\flat\le T_1+2\}$, in Lemma 1.3 below $(\Phi_{\pm\tau})_*$ is applied only after
multiplication by a cut-off $\chi_Z$, a function of $t^\flat$ equal to 1 on $\{T_0-\frac14\eta_0\le t^\flat\le T_1+1\}$
and supported in $\{T_0-\frac12\eta_0\le t^\flat\le T_1+2\}$ (there $T_0\ge1-\frac12\eta_0$). This changes neither the
pairings, the supports of the two factors meeting only where $\chi_Z = 1$ (D326), nor the restrictions to $U'$ and $V'$.
The level sets of $t^\flat$ near $\{t^\flat = T\}$, with the flow lines of $Z/(-Zt^\flat)$, give collar coordinates
$(t^\flat,y)$ in which $Z/(-Zt^\flat) = -\partial_{t^\flat}$; near $\mathscr I^+$, $y = (x_I,\omega)$, and in
$(t^\flat,x_I,\omega)$ the edge vector fields are spanned by $\partial_{t^\flat}$, $x_I\partial_{x_I}$,
$x_I\partial_\omega$, as $t^\flat-t_* = -t_*^{1+\ell_I}x_I^{2\ell_I}$ has bounded edge derivatives.

**Lemma 1.3 (pairing, duality and density).** Let $\Omega' = \Omega_{T_0,T_1}$ with $T_0\ge1-\frac12\eta_0$,
$\alpha\in\mathbb R$ and $m\in\mathbb Z$; weights are $2\alpha$ on $u$ and $-2\alpha$ on $v$.

(a) (*Separation.*) Let $u\in H^{m,2\alpha}_e$ and $v\in H^{-m,-2\alpha}_e$ with $\mathrm{supp}\,u\subset\{t^\flat\ge
T_0\}$. If $\mathrm{supp}\,v\subset\{t^\flat\le T_0\}$, or if $\mathrm{supp}\,v\subset F'$ and $u|_{U'} = 0$, then
$\langle u,v\rangle = 0$. Hence the pairing of $u|_{U'}\in H^{m,2\alpha}(\Omega')^{\bullet,-}$ with $v|_{V'}\in
H^{-m,-2\alpha}(\Omega')^{-,\bullet}$, computed with extensions supported in $\{t^\flat\ge T_0\}$, resp. $F'$, is well
defined, and bounded by $C$ times the product of the quotient norms.

(b) (*Duality.*) If $m\ge0$, every bounded functional $\lambda$ on $H^{m,2\alpha}(\Omega')^{-,\bullet}$ is $\lambda =
\langle\cdot,u\rangle$ for some $u\in H^{-m,-2\alpha}(\Omega')^{\bullet,-}$ with $\|u\|\le C\|\lambda\|$.

(c) (*Density.*) If $m\ge0$, $D(\Omega')$ is dense in $H^{m,2\alpha}(\Omega')^{\bullet,-}$ and $D_*(\Omega')$ is dense in
$H^{m,2\alpha}(\Omega')^{-,\bullet}$; likewise for the mixed spaces of order $(m;k)$.

*Proof.* (a) The pairing is that of II.A Lemma 7.1, bounded on $H^{m}\times H^{-m}$. In the first case,
$(\Phi_{-\tau})_*u$ is supported in $\{t^\flat\ge T_0+c\tau\}$ for $\tau>0$ small, as $-Z$ increases $t^\flat$, so
$\langle(\Phi_{-\tau})_*u,v\rangle = 0$, and $(\Phi_{-\tau})_*u\to u$ in $H^{m,2\alpha}_e$ as $\tau\downarrow0$ (for
$m<0$, $(\Phi_\tau)_*$ is the transpose of $(\Phi_{-\tau})_*$ on $H^{-m}$, bounded uniformly, and converges on the dense
set $C^\infty_c$). In the second case, $(\Phi_\tau)_*v$ is supported, within $\{t^\flat\ge T_0-\frac12\eta_0\}$, in $U'$,
as $Z$ points into $F'$ across $\{t^\flat = T_1\}$ and $\{r = r_0\}$ there; $u$ vanishes on $U'$ and on
$\{t^\flat<T_0\}$, so $\langle u,(\Phi_\tau)_*v\rangle = 0$, and $\tau\downarrow0$ gives the claim. For the pairing, two
extensions of $u|_{U'}$ supported in $\{t^\flat\ge T_0\}$ differ by an element vanishing on $U'$, and two extensions of
$v|_{V'}$ supported in $F'$ by an element supported in $\{t^\flat\le T_0\}$; the bound follows by taking minimal
extensions.

(b) Let $E_0$ be Seeley's extension operator ([Hin26c] Lemma 8.5, whose proof is reproduced) across $\{t^\flat = T_0\}$
in the collar coordinates: $E_0w := w$ on $\{t^\flat>T_0\}$ and $(E_0w)(T_0-\tau,y) := \sum_{l\ge0}c_l(\chi
w)(T_0+\tau/\epsilon_l,y)$ for $\tau>0$, where $\epsilon_l = 3^{-l}$, $\sin(\frac\pi2s) = \sum_lc_ls^l$ (so that
$\sum_l|c_l|\epsilon_l^{-j}<\infty$ and $\sum_lc_l\epsilon_l^{-j} = (-1)^j$ for all $j\in\mathbb N_0$), and $\chi =
\chi(t^\flat-T_0)$ is a cut-off equal to 1 near 0 and supported in $[0,\frac12\eta_0)$. It maps $\bar H^{m,2\alpha}(V')$
boundedly into $H^{m,2\alpha}_e$: the reflection acts in $t^\flat$ only, commutes with $x_I\partial_{x_I}$ and
$x_I\partial_\omega$ in the collar coordinates near $\mathscr I^+$, matches all $t^\flat$-derivatives at $t^\flat = T_0$,
and after $j$ derivatives in $t^\flat$ is bounded on $L^2$ by $\sum_l|c_l|\epsilon_l^{\frac12-j}$. $E_0w$ is supported in
$\{t^\flat>T_0-\frac12\eta_0\}$, within $\Omega^-_*$. It preserves support in $F'$: on a collar line $r$ increases as
$t^\flat$ decreases (near $\{r = r_0\}$, as $Zr>0$ there), so if $(T_0-\tau,y)$ has $r<r_0$, so has
$(T_0+\tau/\epsilon_l,y)$. Hence on $H^{m,2\alpha}(\Omega')^{-,\bullet}$ the quotient norm and the norm of $\bar
H^{m,2\alpha}(V')$ are equivalent. Given $\lambda$, extend it by Hahn-Banach to $\bar H^{m,2\alpha}(V')$ with comparable
norm. By II.A Lemma 7.3 and its proof (the case of functionals on extendible spaces), there is $\tilde u\in\dot
H^{-m,-2\alpha}(\bar V')$, $\|\tilde u\|\le C\|\lambda\|$, with $\lambda(y) = \langle\tilde y,\tilde u\rangle$ for every
extension $\tilde y\in H^{m,2\alpha}_e$ of $y$. Take $\tilde y$ supported in $F'$; then $u := \tilde u|_{U'}$ represents
$\lambda$ in the pairing of (a).

(c) Given $v$ supported in $F'$, $(\Phi_\tau)_*v\to v$ as $\tau\downarrow0$, and for small $\tau>0$ its part in
$\{t^\flat>T_0-\frac12\eta_0\}$ is supported in $\{t^\flat<T_1,r>r_0\}$; the part in $\{t^\flat\le T_0-\frac12\eta_0\}$
does not affect the restriction to $V'$. Then multiply by $1-\chi_0(x_I/\delta)$, $\chi_0$ a cut-off equal to 1 near 0,
which converges strongly to the identity as $\delta\to0$ (dominated convergence;
$(x_I\partial_{x_I})^j(x_I\partial_\omega)^\beta\partial_{t_*}^i$ of $\chi_0(x_I/\delta)$ are bounded uniformly in
$\delta$), and mollify on the resulting compact set. For $D(\Omega')$ use $\Phi_{-\tau}$, which moves supports into
$\{t^\flat>T_0\}$. For the mixed spaces the same, as the operations commute with b-vector fields up to terms bounded on
these spaces. $\square$

## 2. Energy estimates

### 2.1 Three identities

For a $C^1$ Lorentzian metric $g$, a real $C^1$ vector field $X$ and real covectors $\zeta$ put
$$K_X(\zeta) := \tfrac12\big(H_G(\zeta(X))-(\mathrm{div}_gX)G(\zeta)\big),\qquad T(V,W)(\zeta) :=
\zeta(V)\zeta(W)-\tfrac12g(V,W)G(\zeta),$$
with $G(\zeta) = g^{-1}(\zeta,\zeta)$; for $\mathbb C^N$-valued $u$, $K_X(du)$ and $T(V,W)(du)$ are the corresponding
Hermitian forms in $du$ (sums over the real and imaginary parts of the components). In coordinates $K_X(\zeta) =
(\nabla_\mu X_\nu)\zeta^\mu\zeta^\nu-\frac12(\mathrm{div}_gX)G(\zeta)$, as $H_G(X^\nu\zeta_\nu) =
2g^{\mu\lambda}\zeta_\lambda\partial_\mu X^\nu\zeta_\nu-(\partial_\kappa g^{\mu\nu})X^\kappa\zeta_\mu\zeta_\nu$ and
$2\zeta^\mu\zeta_\nu\Gamma^\nu_{\mu\kappa} = \zeta^\mu\zeta^\lambda\partial_\kappa g_{\lambda\mu} = -(\partial_\kappa
g^{\mu\nu})\zeta_\mu\zeta_\nu$. $P_\Box := -\Box_g$ acts componentwise; $\sigma_2(P_\Box) = G$.

**Lemma 2.1 (energy identity).** Let $O$ be a region whose boundary in $M^\circ$ consists of finitely many $C^1$
hypersurfaces $\{\varphi_j = 0\}$ meeting transversally, $O = \{\varphi_j>0\ \forall j\}$ near them, and let $X$ be a
real $C^1$ vector field. For $u\in C^2(\bar O;\mathbb C^N)$ with compact support in $\bar O$,
$$2\,\mathrm{Re}\int_O\langle P_\Box u,Xu\rangle\,|dg| = \int_O2K_X(du)\,|dg|+\sum_j\int2T(X,\nabla\varphi_j)(du)\,
\delta(\varphi_j)\,|dg|.\tag{2.1}$$
For $f\in C^1$ real, $K_{fX} = fK_X+2T(X,\frac12\nabla f)$, that is, $K_{fX}(\zeta) =
fK_X(\zeta)+\zeta(X)g^{-1}(df,\zeta)-\frac12(Xf)G(\zeta)$.

*Proof.* For a real component $a$ of $u$, with $J := -(Xa)\nabla a+\frac12G(da)X$: $\mathrm{div}J = -(Xa)\Box
a-(\nabla_\mu X_\nu)\nabla^\mu a\nabla^\nu a-\frac12X(G(da))+\frac12X(G(da))+\frac12(\mathrm{div}X)G(da)$, using
$\nabla^\mu a\nabla_\mu(X^\nu\nabla_\nu a) = (\nabla_\mu X_\nu)\nabla^\mu a\nabla^\nu a+\frac12X(G(da))$. So $(-\Box
a)(Xa) = \mathrm{div}J+K_X(da)$. Integrate over $O$: $\int\mathrm{div}(1_OJ)|dg| = 0$ and $\mathrm{div}(1_OJ) =
1_O\mathrm{div}J+\sum_j\delta(\varphi_j)J(d\varphi_j)$ (the divergence theorem on the Lipschitz domain $O$), and
$-J(d\varphi_j) = (Xa)\,da(\nabla\varphi_j)-\frac12(X\varphi_j)G(da) = T(X,\nabla\varphi_j)(da)$. Sum over the real and
imaginary parts of all components. The formula for $K_{fX}$ follows from $H_G(f\zeta(X)) = fH_G(\zeta(X))+\zeta(X)H_Gf$,
$H_Gf = 2g^{-1}(df,\zeta)$ and $\mathrm{div}(fX) = f\,\mathrm{div}X+Xf$. $\square$

**Lemma 2.2 (dominant energy).** If $V,W$ are both future causal, or both past causal, then $T(V,W)(\zeta)\ge0$ for all
real $\zeta$. If $V$ is timelike, $T(V,V)(\zeta)\ge c|\zeta|^2$ with $c>0$ depending continuously on $V$ and on a
Riemannian norm.

*Proof.* $T$ is bilinear in $(V,W)$, so the past case follows from the future one. Let $Z := \zeta^\sharp$ and $Y :=
g(Z,V)Z-\frac12g(Z,Z)V$. Then $T(V,W)(\zeta) = g(Y,W)$, $g(Y,Y) = \frac14g(Z,Z)^2g(V,V)\le0$, and $g(Y,V) =
T(V,V)(\zeta)$. In an orthonormal frame with $V$ a positive multiple of $e_0$ (if $V$ is timelike), $T(V,V)(\zeta) =
\frac12|V|^2(Z_0^2+|Z_\perp|^2)$, which is the second claim; if $V$ is null, $T(V,V)(\zeta) = g(Z,V)^2\ge0$. So $Y$ is
causal or zero, with $g(Y,V)\ge0$, hence past causal or zero, and $g(Y,W)\ge0$ for $W$ future causal. In the remaining
case, $g(Y,V) = 0$ with $V$ null, $g(Z,V)^2 = T(V,V)(\zeta) = 0$, so $Y = -\frac12g(Z,Z)V$; and $Z\perp V$ with $V$ null
forces $Z$ spacelike or parallel to $V$, so $g(Z,Z)\ge0$ and $Y$ is a non-positive multiple of $V$, again past causal or
zero. $\square$

**Lemma 2.3 (Poincaré inequality with an exponential weight).** Let $O$ be as in Lemma 2.1, $N$ a $C^1$ vector field and
$\tau$ a $C^1$ function with $N\tau = 1$, $|\mathrm{div}_gN|\le C_0$ on $O$, $w>0$ a $C^1$ weight with $|N\log w|\le
C_1$, and $\Phi\ge C_0+C_1$. Let $u\in C^1(\bar O)$ have compact support in $\bar O$ and vanish near the part of every
boundary face $\{\varphi_j = 0\}$ where $N\varphi_j>0$. Then
$$\int_Oe^{-2\Phi\tau}w|u|^2|dg|\le4\Phi^{-2}\int_Oe^{-2\Phi\tau}w|Nu|^2|dg|.\tag{2.2}$$

*Proof.* With $Y := e^{-2\Phi\tau}wN$, $\mathrm{div}(|u|^2Y) = Y|u|^2+e^{-2\Phi\tau}w(\mathrm{div}N+N\log w-2\Phi)|u|^2$.
Integrating as in Lemma 2.1, the boundary terms are $-\int\delta(\varphi_j)|u|^2Y\varphi_j\ge0$, as $u = 0$ near the
faces with $N\varphi_j>0$. So $(2\Phi-C_0-C_1)\int e^{-2\Phi\tau}w|u|^2\le2(\int e^{-2\Phi\tau}w|u|^2)^{1/2}(\int
e^{-2\Phi\tau}w|Nu|^2)^{1/2}$, which gives (2.2), as $2\Phi-C_0-C_1\ge\Phi$. $\square$

With $N$ replaced by $-N$ and $\tau$ by $-\tau$ this is the inequality for the reverse direction: $\int
e^{2\Phi\tau}w|u|^2\le4\Phi^{-2}\int e^{2\Phi\tau}w|Nu|^2$ when $u$ vanishes near the faces with $N\varphi_j<0$.

### 2.2 The multiplier near $\mathscr I^+$ at $n = 4$

Near $\mathscr I^+$ at finite times put, for $\beta\in\mathbb R$,
$$X_0^{(\beta)} := x_I^{-4\beta-2}\big(\partial_{t_*}-x_I\partial_{x_I}\big) = r^{2\beta+1}\big(\partial_{t_*}+
2r\partial_r\big).$$
For covectors write $\zeta = \zeta_{t_*}dt_*+\xi\frac{dx_I}{x_I}+\eta$ and $\hat\eta := x_I\eta$, so that
$\zeta(\partial_{t_*})$, $\zeta(x_I\partial_{x_I})$, $\hat\eta$ are the components of $\zeta$ on the edge frame and
$|\hat\eta|^2 = x_I^2|\eta|^2_{\slashed g}$.

**Lemma 2.4 ([Hin26c] (8.10) at $n = 4$).** For the Minkowski metric $\bar g = -dt_*^2-2dt_*dr+r^2\slashed g$,
$$K_{X_0^{(\beta)}}(\zeta) = x_I^{-4\beta}\Big[-(2\beta+1)\zeta_{t_*}^2-3\zeta_{t_*}\xi-(2\beta+3)|\hat\eta|^2+
x_I^2\big(\tfrac{2\beta-1}4\xi^2-\tfrac{2\beta+1}2\zeta_{t_*}\xi\big)\Big],$$
$$T\big(X_0^{(\beta)},-\nabla t_*\big)(\zeta) = \tfrac12x_I^{-4\beta}\big(\xi^2+|\hat\eta|^2+\tfrac14x_I^2\xi^2\big).$$
For the metric $g$ of $P$, the two sides change by $x_I^{-4\beta}O(x_I^{2\ell_I})(\zeta_{t_*}^2+\xi^2+|\hat\eta|^2)$,
uniformly for $\epsilon_P\le1$, with $d_0\ge2$.

*Proof.* $\bar g^{-1} = -2\partial_{t_*}\otimes_s\partial_r+\partial_r\otimes\partial_r+r^{-2}\slashed g^{-1}$ (with
$\otimes_s$ as in Lemma 1.1, times 2), so $G(\zeta) = -2\zeta_{t_*}\zeta_r+\zeta_r^2+r^{-2}|\eta|^2$ in $(t_*,r,\omega)$,
and $\mathrm{div}_{\bar g}Y = r^{-3}\partial_\mu(r^3Y^\mu)$ for $Y = Y^{t_*}\partial_{t_*}+Y^r\partial_r$. With $X =
r^c(\partial_{t_*}+2r\partial_r)$, $c := 2\beta+1$: $\zeta(X) = r^c(\zeta_{t_*}+2r\zeta_r)$; $H_G(\zeta(X)) =
\partial_{\zeta_r}G\,\partial_r(\zeta(X))-\partial_rG\,\partial_{\zeta_r}(\zeta(X))$, with $\partial_{\zeta_r}G =
-2\zeta_{t_*}+2\zeta_r$, $\partial_rG = -2r^{-3}|\eta|^2$, $\partial_r(\zeta(X)) = r^{c-1}(c\zeta_{t_*}+2(c+1)r\zeta_r)$,
$\partial_{\zeta_r}(\zeta(X)) = 2r^{c+1}$; and $\mathrm{div}X = r^{-3}\partial_r(2r^{c+4}) = 2(c+4)r^c$. So
$$2K_X = r^{c-1}\big[(-2\zeta_{t_*}+2\zeta_r)(c\zeta_{t_*}+2(c+1)r\zeta_r)+4r^{-1}|\eta|^2\big]-2(c+
4)r^c\big(-2\zeta_{t_*}\zeta_r+\zeta_r^2+r^{-2}|\eta|^2\big).$$
Insert $\zeta_r = -\xi/(2r)$ (as $dr = -2r\frac{dx_I}{x_I}$) and $|\eta|^2 = r|\hat\eta|^2$, and $r^{c-1} =
x_I^{-4\beta}$, $r^{-1} = x_I^2$: the $\zeta_{t_*}^2$ coefficient is $-2c$, the $\zeta_{t_*}\xi$ coefficient $-6-cx_I^2$,
the $|\hat\eta|^2$ coefficient $4-2(c+4) = -2c-4$, and the $\xi^2$ coefficient
$\frac12(c+1)x_I^2-\frac12(c+4)x_I^2+\ldots$, which is $\frac{c-2}2x_I^2$. Halving gives $K$. For $T$: $\zeta(X_0) =
r^c(\zeta_{t_*}+2r\zeta_r) = r^c(\zeta_{t_*}-\xi)$, $\zeta(-\nabla t_*) = -\bar g^{-1}(dt_*,\zeta) = \zeta_r =
-\xi/(2r)$, and $\bar g(X_0,-\nabla t_*) = -dt_*(X_0) = -r^c$; so $T =
r^c(\zeta_{t_*}-\xi)(-\frac\xi{2r})+\frac12r^c(-2\zeta_{t_*}\zeta_r+\zeta_r^2+r^{-2}|\eta|^2)$, which is
$\frac12r^{c-1}(\xi^2+|\hat\eta|^2+\frac14r^{-1}\xi^2)$, the $\zeta_{t_*}\xi$ terms cancelling. (These identities were
also checked symbolically.) For $g$: by Lemma 1.1 and II.C (5.1), $g^{-1}-\bar g^{-1}$ is $x_I^{2+2\ell_I}$ times a
quadratic form in $(\zeta_{t_*},\xi,\hat\eta)$ with coefficients bounded in $C^{d_0-1}_e$, and $|dg|/|d\bar g|-1\in
x_I^{2\ell_I}C^{d_0-1}_e$; $K$ and $T$ involve these and one edge derivative of them. $\square$

The cross term $-3\zeta_{t_*}\xi$ and the angular coefficient $-(2\beta+3)$ are $-2$ and $-2(\beta+1)$ at $n = 3$
([Hin26c] (8.10)); the $\zeta_{t_*}^2$ coefficient, which carries the threshold, is the same in both dimensions.

**Lemma 2.5 (energy estimate near $\mathscr I^+$; [Hin26c] Lemma 8.1 at $n = 4$).** Let $\alpha<-\frac12+\bar p_1$ and
$\Omega' = \Omega_{T_0,T_1}$, $T_0\ge1$; put $t' := t_*+r^{\ell_I/2}$. There are $\delta_0>0$ and $T_2$, with
$\Omega'\cap\{t'\ge T_2\}\subset\{x_I\le\delta_0\}$, and $C$, such that:

(i) for $u\in D(\Omega')$ supported in $\{x_I\le\delta_0\}$, $\|u\|_{H^{1,2\alpha}(\Omega')}\le
C\|Pu\|_{H^{0,2\alpha+2}(\Omega')}$;

(ii) for $v\in C^\infty(\bar\Omega'\cap\{t'\ge T_2\})$ vanishing near $\{t^\flat = T_1\}$ and near $\mathscr I^+$,
$\|v\|_{H^{1,-2\alpha-2}(\Omega'\cap\{t'\ge T_2\})}\le C\|P^*v\|_{H^{0,-2\alpha}(\Omega'\cap\{t'\ge T_2\})}$.

Here $H^{1,2\beta}(O)$ and $H^{0,2\beta}(O)$ denote the norms
$\big(\int_Ox_I^{-4\beta}(|u|^2+|\partial_{t_*}u|^2+|x_I\partial_{x_I}u|^2+|x_I\partial_\omega u|^2)|dg|\big)^{1/2}$ and
$\big(\int_Ox_I^{-4\beta}|u|^2|dg|\big)^{1/2}$, and $P^*$ is the adjoint for $|dg|$ and the fibre inner product $h_I$ of
(1.2). $C$ is uniform for $\epsilon_P$ small, with $d_0 = 2$.

*Proof.* *The level sets of $t'$.* With $\alpha' := \ell_I/2$, $dt' = dt_*+\alpha'r^{\alpha'-1}dr$ has $\bar
g^{-1}(dt',dt') = -2\alpha'r^{\alpha'-1}+\alpha'^2r^{2\alpha'-2}$. The proof of II.C Lemma 3.2 bounds the coefficients of
$g^{-1}-\bar g^{-1}$ in its basis by $C(\epsilon_P+\rho_I^{1-\ell_I})\rho_I^{\ell_I}$, $\rho_I = t_*/r$; the basis
evaluated on $(dt')^{\otimes2}$ gives $\rho_I$, $O(r^{\alpha'-1})$, $0$, $\rho_I^{-1}\alpha'^2r^{2\alpha'-2}$, $0$, $0$,
all at most $Cr^{\alpha'-1}\cdot r^{\alpha'}$ at bounded $t_*$. So $g^{-1}(dt',dt')\le-\alpha'r^{\alpha'-1}$ for $r\ge
R_0$, as $\rho_I^{\ell_I}r^{\alpha'} = O(r^{-\ell_I/2})$. Moreover $dt'(V) = t_*+\alpha'r^{\alpha'}>0$ for the future
timelike $V = t\partial_t+r\partial_r$ of II.C Lemma 3.2's proof, so $dt'$ is past timelike there, and $t'$ increases
along future causal curves. As $t_*$ is bounded on $\Omega'$, $\Omega'\cap\{t'\ge T_2\}\subset\{x_I\le\delta_0\}$ for
$T_2$ large.

*Conjugation.* Put $v_\flat := A_I^{-1}u$ and $\tilde P := A_I^{-1}PA_I$. As $A_I$ is independent of $x_I$, $\tilde P-P$
is of first order: $[x_I^2x_I\partial_{x_I}\partial_{t_*},A_I] = x_I^2(\partial_{t_*}A_I)x_I\partial_{x_I}$, the
commutator with $x_I^4\Delta_{\mathbb S^3}$ is $x_I^3$ times a first-order edge operator, and the rest is of order 0 with
coefficient $O(x_I^2)$. By Lemma 1.1, with $P_\Box$ for $g$ satisfying (1.1) with $p_0 = p_1 = 0$ (its difference from
$-\Box_{\bar g}$ comes from $g-\bar g$), near $\mathscr I^+$
$$\tilde P = P_\Box+2x_I^2\tilde p_1\partial_{t_*}+x_I^2b\,x_I\partial_{x_I}+R_1+R_0,\qquad\tilde p_1 := A_I^{-1}p_1A_I,
\tag{2.3}$$
with $b$ bounded, $R_1$ a first-order edge operator with coefficients $O(x_I^{2+2\ell_I})$ (of class $C^{d_0-1}_e$), and
$R_0$ of order 0 with coefficient $O(x_I^2)$. By (1.2), $\mathrm{Re}\,\tilde p_1 = A_I^{-1}(\mathrm{Re}_{h_I}p_1)A_I$, so
$\langle\mathrm{Re}\,\tilde p_1w,w\rangle = h_I(\mathrm{Re}_{h_I}p_1A_Iw,A_Iw)\ge(\bar p_1-\delta')|w|^2$; take $\delta'
:= \frac14(\bar p_1-\frac12-\alpha)$.

*(i).* Let $X := e^{-2\Phi t_*}X_0^{(\alpha)}$, future timelike near $\mathscr I^+$: $\bar g(X_0,X_0) = r^{2c}(-1-4r)$,
which dominates the change $O(x_I^{2\ell_I})r^{2c+1}$ from $g-\bar g$. By Lemma 2.1 on $O := \Omega'$, whose faces near
$\mathrm{supp}\,u$ are $\{t^\flat = T_0\}$, where $v_\flat = 0$, and $\{t^\flat = T_1\}$, with $\varphi = T_1-t^\flat$
and $\nabla\varphi = -\nabla t^\flat$ future timelike, the boundary term is $\ge0$ by Lemma 2.2. So
$$2\,\mathrm{Re}\int\langle\tilde Pv_\flat,Xv_\flat\rangle\ge\int2K_X(dv_\flat)+2\,
\mathrm{Re}\int\langle(\tilde P-P_\Box)v_\flat,Xv_\flat\rangle.$$
By Lemmas 2.1 and 2.4, $K_X = e^{-2\Phi t_*}(K_{X_0}+2\Phi T(X_0,-\nabla t_*))$. Write $\tau_0
:= |\partial_{t_*}v_\flat|$, $\tau_1 := |x_I\partial_{x_I}v_\flat|$, $\tau_2 := |x_I\partial_\omega v_\flat|$. Pointwise,
after dividing by $e^{-2\Phi t_*}x_I^{-4\alpha}$, the integrand on the right is at least
$$\big(-2(2\alpha+1)+4(\bar p_1-\delta')\big)\tau_0^2-C_1\tau_0\tau_1-C_1\tau_1^2+2\Phi(\tau_1^2+\tau_2^2)-2(2\alpha+3)_+
\tau_2^2-C_2(1+\Phi)(\delta^{2\ell_I}+\delta^2)(\tau_0^2+\tau_1^2+\tau_2^2)-C_2|v_\flat|(\tau_0+\tau_1+\tau_2)$$
on $\{x_I\le\delta\}$: the first term is $4\langle\mathrm{Re}\,\tilde
p_1\partial_{t_*}v_\flat,\partial_{t_*}v_\flat\rangle$ plus the $\zeta_{t_*}^2$ part of $2K_{X_0}$; $C_1$ bounds the
cross terms $-6\,\mathrm{Re}\langle\partial_{t_*}v_\flat,x_I\partial_{x_I}v_\flat\rangle$, $-4\,\mathrm{Re}\langle\tilde
p_1\partial_{t_*}v_\flat,x_I\partial_{x_I}v_\flat\rangle$ and those of $b$; $C_2$ bounds the $x_I^2$-terms of Lemma 2.4,
the change from $g$ to $\bar g$, and $R_1$, $R_0$. The first coefficient is $a := 12\delta'>0$. With
$C_1\tau_0\tau_1\le\frac a4\tau_0^2+\frac{C_1^2}a\tau_1^2$ and $C_2|v_\flat|\tau_j\le\frac
a{16}\tau_j^2+\frac{4C_2^2}a|v_\flat|^2$, and Lemma 2.3 with $N = \partial_{t_*}$, $\tau = t_*$, $w = x_I^{-4\alpha}$ (as
$\partial_{t_*}\varphi>0$ only at the initial face, where $v_\flat = 0$, and $|\mathrm{div}_g\partial_{t_*}|\le C_0$),
which gives $\int e^{-2\Phi t_*}x_I^{-4\alpha}|v_\flat|^2\le4\Phi^{-2}\int e^{-2\Phi t_*}x_I^{-4\alpha}\tau_0^2$: choose
$\Phi$ large, then $\delta\le\delta_0$ small depending on $\Phi$, to get
$$2\,\mathrm{Re}\int\langle\tilde Pv_\flat,Xv_\flat\rangle\ge\int e^{-2\Phi t_*}x_I^{-4\alpha}\big(\tfrac a4\tau_0^2+
\tfrac\Phi4(\tau_1^2+\tau_2^2)\big)|dg|\ge c\,\|e^{-\Phi t_*}v_\flat\|^2_{H^{1,2\alpha}}.$$
The left side is at most $2\int e^{-2\Phi t_*}x_I^{-4\alpha-2}|\tilde Pv_\flat|(\tau_0+\tau_1)\le\frac c2\|e^{-\Phi
t_*}v_\flat\|^2_{H^{1,2\alpha}}+C\|e^{-\Phi t_*}\tilde Pv_\flat\|^2_{H^{0,2\alpha+2}}$. As $t_*$ is bounded on $\Omega'$
and $A_I$, $A_I^{-1}$ are bounded with bounded derivatives, (i) follows.

*(ii).* Let $\beta := -\alpha-1$, $O := \Omega'\cap\{t'\ge T_2\}$, $w_\flat := A_I^{-1}v$ and $Y := -e^{2\Phi
t_*}X_0^{(\beta)}$, past timelike. $\tilde P^*$ is the standard adjoint of $\tilde P$, and $A_I^{-1}P^*A_I = \tilde P^*$
(II.D Lemma 1.1, proof). $P_\Box$ is symmetric for $|dg|$. So $\tilde P^* = P_\Box-2x_I^2\tilde
p_1^*\partial_{t_*}-x_I^2b^*x_I\partial_{x_I}+R_1'+R_0'$, with $R_1'$, $R_0'$ as before ($(x_I\partial_{x_I})^* =
-x_I\partial_{x_I}+8+O(x_I^{2\ell_I})$ for $|dg|$). Lemma 2.1 on $O$: the faces with $w_\flat\ne0$ nearby are $\{t^\flat
= T_0\}$ and $\{t' = T_2\}$, with $\nabla\varphi = \nabla t^\flat$, resp. $\nabla t'$, past timelike, so the boundary
terms $2T(Y,\nabla\varphi)(dw_\flat)$ are $\ge0$ by Lemma 2.2 (both vectors past causal). By Lemma 2.1, $K_Y = e^{2\Phi
t_*}(-K_{X_0^{(\beta)}}+2\Phi T(X_0^{(\beta)},-\nabla t_*))$. The $\zeta_{t_*}^2$ coefficient of $-2K_{X_0^{(\beta)}}$ is
$2(2\beta+1) = -2(2\alpha+1)$, and the term $2\,\mathrm{Re}\langle-2x_I^2\tilde
p_1^*\partial_{t_*}w_\flat,Yw_\flat\rangle$ contributes $4\langle\mathrm{Re}\,\tilde
p_1\partial_{t_*}w_\flat,\partial_{t_*}w_\flat\rangle$, so the coefficient is again $a$. The rest is as in (i), with
Lemma 2.3 in the reverse direction ($w_\flat = 0$ near $\{t^\flat = T_1\}$, the only face of $O$ with
$\partial_{t_*}\varphi<0$). $\square$

**Lemma 2.6 (energy estimate on a compact region).** Let $\Omega'$, $t'$ be as in Lemma 2.5 and $T\ge T_2$, $O_T :=
\Omega'\cap\{t'\le T\}$, which is compact. There is $C$ such that $\|u\|_{H^1(O_T)}\le C\|Pu\|_{L^2(O_T)}$ for $u\in
C^\infty(\bar O_T)$ vanishing near $\{t^\flat = T_0\}$, and $\|v\|_{H^1(O_T)}\le C\|P^*v\|_{L^2(O_T)}$ for $v\in
C^\infty(\bar O_T)$ vanishing near $\{t^\flat = T_1\}$, $\{r = r_0\}$ and $\{t' = T\}$; uniformly for $\epsilon_P$ small,
$d_0 = 2$.

*Proof.* Let $N := -\nabla t^\flat$, future timelike and $C^{d_0-1}$, $\hat N := N/(Nt^\flat)$, and $X := e^{-2\Phi
t^\flat}N$. By Lemma 2.1, $K_X = e^{-2\Phi t^\flat}(K_N+2\Phi T(N,N))$, and by Lemma 2.2 and compactness,
$T(N,N)(\zeta)\ge c|\zeta|^2$ on $\bar O_T$. The faces with $u\ne0$ nearby are $\{t^\flat = T_1\}$, $\{r = r_0\}$, $\{t'
= T\}$, with $\nabla\varphi$ equal to $-\nabla t^\flat$, $\nabla r$, $-\nabla t'$, all future timelike (II.C Lemma 3.2
and Lemma 2.5); the boundary terms are $\ge0$ by Lemma 2.2. The first- and zeroth-order terms of $P-P_\Box$ contribute at
most $Ce^{-2\Phi t^\flat}(|du|^2+|u||du|)$, and Lemma 2.3 with $N = \hat N$, $\tau = t^\flat$, bounds $\int e^{-2\Phi
t^\flat}|u|^2$ by $4\Phi^{-2}\int e^{-2\Phi t^\flat}|\hat Nu|^2$, the only face with $\hat N\varphi>0$ being the initial
one. For $\Phi$ large this gives the first estimate, as in Lemma 2.5. For $P^*$ use $-e^{2\Phi t^\flat}N$ and the reverse
inequality of Lemma 2.3. $\square$

**Proposition 2.7 ([Hin26c] Lemma 8.1 and (8.23) at $n = 4$).** Let $\alpha<-\frac12+\bar p_1$ and $\Omega' =
\Omega_{T_0,T_1}$, $T_0\ge1$. There is $C$, uniform for $\epsilon_P$ small with $d_0 = 2$, such that for $u\in
D(\Omega')$ and $v\in D_*(\Omega')$
$$\|u\|_{H^{1,2\alpha}(\Omega')}\le C\|Pu\|_{H^{0,2\alpha+2}(\Omega')},\qquad\|v\|_{H^{1,-2\alpha-2}(\Omega')}
\le C\|P^*v\|_{H^{0,-2\alpha}(\Omega')}.\tag{2.4}$$
The same holds on $\Omega'\cap\{t'\le T\}$ for $T\ge T_2$, with $\{t' = T\}$ a further final face, and for
$P^{\mathrm{ext}}$ on the slabs $\{T_0\le t^\flat\le T_1,r\ge r^\sharp\}$ of Lemma 1.2, $T_0\ge1-\eta_0$.

*Proof.* Let $\chi = \chi(t')$ equal 1 for $t'\le T_2$ and 0 for $t'\ge T_2+1$. For $u$: $\|\chi u\|_{H^1}\le
C\|u\|_{H^1(O_{T_2+1})}\le C\|Pu\|$ by Lemma 2.6, the weights being bounded on $O_{T_2+1}$. $(1-\chi)u\in D(\Omega')$ is
supported in $\{x_I\le\delta_0\}$, so by Lemma 2.5 (i) $\|(1-\chi)u\|_{H^{1,2\alpha}}\le
C(\|Pu\|+\|[P,\chi]u\|_{H^{0,2\alpha+2}})$, and $[P,\chi]u$ is supported in $O_{T_2+1}$ with norm at most
$C\|u\|_{H^1(O_{T_2+1})}$. For $v$, in the reverse order: Lemma 2.5 (ii) bounds $v$ on $\Omega'\cap\{t'\ge T_2\}$, which
contains the support of $[P^*,\chi]v$; then Lemma 2.6 applied to $\chi v$, which vanishes near $\{t' = T_2+1\}$, bounds
$\chi v$. On the extended slabs the proofs apply verbatim, by Lemma 1.2 (iii)-(iv), with (1.2) holding at $2\delta'$, so
that the coefficient of Lemma 2.5 is $a = 8\delta'$ in place of $12\delta'$. $\square$

## 3. Solvability on slabs

Throughout, $\alpha<-\frac12+\bar p_1$, and $h$ is a fibre inner product on $\mathbb C^N$ equal to $h_I$ of (1.2) near
$\mathscr I^+$ (patched with the standard one by a partition of unity; the conditions are convex in the Gram matrix).
$P^*$ is the adjoint of $P$ (or $P^{\mathrm{ext}}$) for $|dg|$ and $h$. Changing the density from $|dt\,dx|$ (II.C
section 1.1) to $|dg| = \mu|dt\,dx|$ adds to $\sigma_1(\mathrm{Im}_hP)$ the term $\frac12H_G\log\mu$, which vanishes at
the radial sets, where $\mathsf H = 0$; so the thresholds below are those of II.D. $R := \partial R_{\mathscr
I^+,\mathrm{out}}$, and $R_{[a,b]} := R\cap\{a\le t_*\le b\}$.

### 3.1 Radial estimates at $\partial R_{\mathscr I^+,\mathrm{out}}$ localised in time

We use the eb-coordinates of II.B section 7 near $\mathscr I^+$: $\rho_+ = t_*^{-1}$, $x'_I = (t_*/r)^{1/2}$, $\rho :=
\sigma_{eb}^{-1}$, $\hat\xi$, $\hat\eta$, $\ell := G_{eb} = x_I'^{-2}\rho_+^{-2}G$ and $\mathsf H := \rho H_\ell$ (II.B
(7.3)), as in II.D Propositions 3.5-3.6. For $\kappa>0$ put
$$F := t_*-\kappa x_I'^{2\ell_I}.$$
$x_I'^{2\ell_I}$ has bounded eb-derivatives of every order, so functions of $F$ are admissible factors of a commutant.

**Lemma 3.1 (a time function adapted to $R$).** Let $\bar t>1$. There are $\kappa$, $x_0>0$ and $C$, depending on $\bar
t$, such that on $U_F := \{|\hat\xi|\le\frac12,\ x'_I\le x_0,\ \frac12\le t_*\le\bar t\}$ in ${}^{eb}S^*M$, for $P$ with
$\epsilon_P\le1$,
$$\mathsf HF = h_F-t_*\rho^2\ell,\qquad h_F = t_*\big(\tfrac12\hat\xi^2+|\hat\eta|^2+\tfrac14x_I'^2\hat\xi^2\big)+
x_I'^{2\ell_I}\tilde h_F,\qquad\tilde h_F\ge\tfrac12\kappa\ell_I,\tag{3.1}$$
with $\tilde h_F$ of class $C^{d_0-2}$ with bounded eb-derivatives.

*Proof.* In eb-coordinates $\sigma_{eb}$ is dual to $\rho_+\partial_{\rho_+}$, so $H_\ell\rho_+ =
\rho_+\partial_{\sigma_{eb}}\ell$ and $\mathsf Ht_* = -t_*\rho\,\partial_{\sigma_{eb}}\ell$. For $\bar G_{eb} =
\frac12\xi(\xi-2\sigma)+|\eta|^2+\frac14x_I'^2\xi^2$ (II.B (7.1)), $-\partial_\sigma\bar G_{eb} = \xi$, and $\rho^2\bar
G_{eb} = \frac12\hat\xi(\hat\xi-2)+|\hat\eta|^2+\frac14x_I'^2\hat\xi^2$, so
$$\hat\xi = \tfrac12\hat\xi^2+|\hat\eta|^2+\tfrac14x_I'^2\hat\xi^2-\rho^2\bar G_{eb}.$$
Put $d := \ell-\bar G_{eb}$; by II.C (5.1) and II.C Lemma 4.1 (a), $d\in x_I'^{2\ell_I}C^{d_0-1}P^{[2]}$, with norm
bounded for $\epsilon_P\le1$. Hence $\mathsf Ht_* =
t_*(\frac12\hat\xi^2+|\hat\eta|^2+\frac14x_I'^2\hat\xi^2)-t_*\rho^2\ell+t_*(\rho^2d-\rho\,\partial_\sigma d)$, and the
last term is $x_I'^{2\ell_I}$ times a function bounded by $C_dt_*$ on the cosphere bundle. By II.B (7.4) and II.C (5.1),
$x_I'^{-1}\mathsf Hx'_I = \hat\xi-1+O(x_I'^{2\ell_I})$, so $\mathsf H(x_I'^{2\ell_I}) =
2\ell_Ix_I'^{2\ell_I}(\hat\xi-1+O(x_I'^{2\ell_I}))$. Therefore (3.1) holds with $\tilde h_F =
2\kappa\ell_I(1-\hat\xi)+t_*x_I'^{-2\ell_I}(\rho^2d-\rho\,\partial_\sigma d)+\kappa\,O(x_I'^{2\ell_I})$, and $\tilde
h_F\ge\kappa\ell_I-C_d\bar t-C\kappa x_0^{2\ell_I}\ge\frac12\kappa\ell_I$ on $U_F$ for $\kappa := 4C_d\bar t/\ell_I$ and
$x_0$ small. $\square$

So $\mathsf HF$ is, up to a multiple of $\ell$, a sum of squares of symbols on a full neighbourhood of $R$ at bounded
times, on and off the characteristic set: $h_F = \sum_ic_i^2$ with $c_i$ among $(t_*/2)^{1/2}\hat\xi$,
$t_*^{1/2}\hat\eta_j$, $\frac12t_*^{1/2}x'_I\hat\xi$, $x_I'^{\ell_I}\tilde h_F^{1/2}$. For $t^\flat$ in place of $F$ this
fails: at $x_I = 0$, $\mathsf Ht^\flat = t_*\hat\xi$, which is negative off the characteristic set near $R$ (II.D, the
paragraph after Proposition 3.6).

**Proposition 3.2 (localised radial estimates at $R$).** Let $t_-<t_+$ and $\omega_0\in(0,1]$ with
$t_--\omega_0\ge\frac12$, constants $s>s_0$,
and suppose (1.2) holds with $2\delta'$ in place of $\delta'$ on $R_{[t_--\omega_0,t_++\omega_0]}$ (for
$P^{\mathrm{ext}}$ below $t_* = 1$, Lemma 1.2 (iii)). There are $B,E,E_\pm,G\in C^\infty_b\Psi^0_{e3b}$ such that (1)
their operator wave front sets lie in any given neighbourhood of $R_{[t_--\omega_0,t_++\omega_0]}$; (2) their Schwartz
kernels lie in $K\times K$ for any given compact neighbourhood $K$ of $\mathscr I^+\cap\{t_--\omega_0\le t_*\le
t_++\omega_0\}$; (3) $B$ is elliptic at $R_{[t_-,t_+]}$; (4) $\mathrm{WF}'(E_-)\subset\{t_*\le t_-\}$,
$\mathrm{WF}'(E_+)\subset\{t_*\ge t_+\}$, and $\mathrm{WF}'(E)\cap R = \emptyset$; and such that, in the strong sense and
uniformly for $\epsilon_P$ small,
$$\|Bu\|_{s,2\alpha}\le C\big(\|GPu\|_{s-1,2\alpha+2}+\|E_-u\|_{s,2\alpha}+\|Eu\|_{s,2\alpha}+
\|\tilde\chi u\|_{s_0,2\alpha}\big),\tag{3.2}$$
$$\|Bv\|_{s,-2\alpha-2}\le C\big(\|GP^*v\|_{s-1,-2\alpha}+\|E_+v\|_{s,-2\alpha-2}+\|\tilde\chi v\|_{s_0,-2\alpha-2}\big),
\tag{3.3}$$
with $\tilde\chi$ as in II.D Proposition 3.6 and the norms of $H^{\cdot,(2\beta,0)}_{e3b}$ near $\mathscr I^+$ at finite
times.

(3.2) is the sink estimate of II.D Proposition 3.6 localised to $t_*\le t_+$ with no error term at late times; (3.3) is
the estimate at $R$ as a source for the adjoint, propagating backward in time, which [Hin26c] leaves to the reader
(section 7, (E3)).

*Proof.* The pattern of II.D section 3 at $R$, with $W' := x_I'^2\rho_+^2$, $\rho$, $\mathsf H$ as above, $A := A_I$ the
frame of $h_I$, and the weight $w := x_I'^{2\alpha}$ for (3.2), $w^* := x_I'^{2\alpha^*}$ with $\alpha^* := -\alpha-1$
for (3.3). The commutant is $\check a = \rho^{-s+\frac12}\Psi\chi_\infty$ with
$$\Psi := \psi(\mathfrak M_\Sigma\rho^2\ell)\,\psi(\mathfrak M_Rq)\,\psi(\mathfrak Mx'_I)\,\psi_-(F)\,\psi_+(F),
\quad q := \hat\xi^2+|\hat\eta|^2,\quad\psi_-(F) := \eta_t\big(\tfrac{F-t_-}{\omega_0}\big),\quad\psi_+(F) :=
\eta_t\big(\tfrac{t_+-F}{\omega_0}\big),$$
$\eta_t$ as in II.D Proposition 3.6, and $\bar t := t_++2$ in Lemma 3.1. On $\mathrm{supp}\,\psi(\mathfrak
M_Rq)\psi(\mathfrak Mx'_I)$, $|\hat\xi|\le\frac12$ and $x'_I\le x_0$ for $\mathfrak M_R$, $\mathfrak M$ large, and $0\le
t_*-F\le\kappa\mathfrak M^{-2\ell_I}\le\frac14\omega_0$. As $\eta_t = 0$ on $(-\infty,-\frac12]$, $\eta_t = 1$ on
$[-\frac14,\infty)$ and $\eta_t'\ne0$ only on $(-\frac12,-\frac14)$, on $\mathrm{supp}\,\Psi$ we have
$t_--\frac12\omega_0\le F\le t_++\frac12\omega_0$; so $\mathrm{supp}\,\Psi\subset U_F\cap\{t_--\frac12\omega_0\le t_*\le
t_++\frac34\omega_0\}$, compact, and $\Psi = 1$ at $R_{[t_-,t_+]}$, where $F = t_*$.

*(3.2)*, with $\varsigma = 1$. II.D (3.1) gives $H_\ell(\check a_\epsilon^2)+2\check a_\epsilon^2\ell_I =
\rho^{-2s}\varphi_\epsilon^2(-\Psi^2Q_\epsilon+\mathsf H(\Psi^2))$, and at $R$, as in II.D Proposition 3.6, $Q_\epsilon =
4A^{-1}(\mathrm{Re}_{h_I}p_1)A-2-4\alpha\ge4(\bar p_1-2\delta')-2-4\alpha = 8\delta'$, by (1.2) with $2\delta'$, as
$4(\bar p_1-\frac12-\alpha) = 16\delta'$. The factors $\psi(\mathfrak M_\Sigma\rho^2\ell)$, $\psi(\mathfrak M_Rq)$,
$\psi(\mathfrak Mx'_I)$ contribute as in II.D Proposition 3.6: $j_\epsilon\ell$, and $+e^*e$ terms supported in
$\{q\ge(2\mathfrak M_R)^{-1}\}\cup\{x'_I\ge(2\mathfrak M)^{-1}\}$, which give $E$. For the time factors, by (3.1),
$$\mathsf H(\psi_\pm(F)^2) = \pm\tfrac2{\omega_0}\psi_\pm\eta_t'\big(\cdots\big)\big(h_F-t_*\rho^2\ell\big),$$
the argument of $\eta'_t$ being that of $\psi_\pm$. The part with $t_*\rho^2\ell$ is of the form $j_\epsilon\ell$ (Lemma
2.1 of II.D). The part with $h_F = \sum_ic_i^2$ is $\pm\sum_i\big(\sqrt{2/\omega_0}(\psi_\pm\eta'_t)^{1/2}c_i\big)^2$, a
finite sum of squares of symbols, since $(\eta_t\eta'_t)^{1/2}$ is smooth. For $\psi_+$ it enters with the sign $-$: a
term $-b'^*b'$, so no error term arises at late times. For $\psi_-$ it enters with $+$: a term $+e_-^*e_-$, supported
where $\eta'_t((F-t_-)/\omega_0)\ne0$, so where $F<t_--\frac14\omega_0$ and hence $t_*<t_-$ on $\mathrm{supp}\,\Psi$;
this gives $E_-$. Then II.D Lemmas 2.1-2.3 give (3.2).

*(3.3)*, with $\varsigma = -1$. For $P^*$ the conjugated operator has $\mathfrak p'_{P^*} = -\mathfrak p'$ (II.D Lemma
1.1, as $\mathrm{Im}_hP^* = -\mathrm{Im}_hP$), so II.D (3.1) gives
$$-\big(H_\ell(\check a_\epsilon^2)+2\check a_\epsilon^2\ell_{I,P^*}\big) =
\rho^{-2s}\varphi_\epsilon^2\big(-\Psi^2Q^*_\epsilon-\mathsf H(\Psi^2)\big),\qquad Q^*_\epsilon :=
-(2s_\epsilon-1)\rho^{-1}\mathsf H\rho-2A^{-1}\big(\mathfrak p'+\tfrac12\mathsf H\log W'+\mathsf H\log w^*\big)A.$$
At $R$, $\rho^{-1}\mathsf H\rho = 0$, $\mathfrak p' = -2\,\mathrm{Re}_{h_I}p_1$ (II.D Lemma 3.4), $\mathsf H\log W' =
2x_I'^{-1}\mathsf Hx'_I+2\rho_+^{-1}\mathsf H\rho_+ = -2$ and $\mathsf H\log w^* = -2\alpha^* = 2\alpha+2$ (II.B (7.4)).
So $Q^*_\epsilon = 4A^{-1}(\mathrm{Re}_{h_I}p_1)A+2-4\alpha-4$, the same quantity as $Q_\epsilon$ in (3.2), positive;
near $R$ the term with $\rho^{-1}\mathsf H\rho$ is small as in II.D. Now the localisers enter with the opposite sign. As
$\mathsf Hq\le-q$ and $\mathsf Hx'_I\le-\frac12x'_I$ near $R$ (II.D Proposition 3.6), the factors $\psi(\mathfrak M_Rq)$,
$\psi(\mathfrak Mx'_I)$ give $-b'^*b'$ terms: $R$ is a source for $-\mathsf H$, and no error term arises from them.
$\psi(\mathfrak M_\Sigma\rho^2\ell)$ gives $j_\epsilon\ell$. Of the time factors, $\psi_-$ gives $-b'^*b'$ and $\psi_+$
gives $+e_+^*e_+$, supported where $F>t_++\frac14\omega_0$, hence in $\{t_*>t_+\}$, which is $E_+$. II.D Lemmas 2.1-2.3
hold with $\varsigma = -1$, as II.A$'$ Lemma 4.1, on which they rest, allows either sign; they give (3.3).

Both estimates use the operator only through the pattern, so they hold for $P^{\mathrm{ext}}$ near $\{t_*\le1\}$, and for
systems $P\otimes\mathrm{Id}-Q$ with $Q$ of first order whose principal symbol vanishes at $R$, as in II.D$'$ Lemma 2.5.
The constants depend on $P$ through finitely many coefficient norms and the margins, which are uniform for $\epsilon_P$
small. $\square$

### 3.2 Regularity on slabs

Below, $\mathsf s$ is a *slab order*: $\mathsf s\in C^\infty({}^{e3b}S^*M)$ with $\pm\mathsf H\mathsf s\le0$ on
$\partial\Sigma^\pm$ over the region considered, and constant near $R$. Admissible order functions (II.C Definition 5.2)
are slab orders over $\Omega_*$, by II.C Proposition 5.1 (2) and (5); so are constants.

*The order on the extension region.* II.C Proposition 5.1 (2) concerns $\Omega_*$ only, while Lemma 3.3 (a) at $T_0 = 1$
propagates through the collar $\{1-\frac12\eta_0<t^\flat<1\}$, part of which lies in $\{t_*<1\}$, and over
$\{r^\sharp\le r\le r_0\}$. There the admissible order is extended by its own formula, II.C (5.3): $\mathsf s =
s_{\mathrm{in}}-(s_{\mathrm{in}}-s_{\mathrm{out}})\chi$, $\chi = \psi_0(x_I)\chi_I+(1-\psi_0(x_I))\chi_\iota$. The
second term is supported in $\Omega_\iota\cap\{\varrho<\epsilon_\iota\delta\}\subset\{r>(\epsilon_\iota\delta)^{-1},\
t_*\ge r/C_\iota\}$ (II.C section 5.2, $\varrho = r^{-1}$, $\rho_K = r/t_*\le C_\iota$ on $\Omega_\iota$), which, after
decreasing $\epsilon_\iota$ so that $(C_\iota\epsilon_\iota\delta)^{-1}>1$, meets neither $\{t_*\le1\}$ nor $\{r\le
r_0\}$ (as $(\epsilon_\iota\delta)^{-1}>r_h+1$). The factor $\chi_I$ is a function of the eb-fibre variables $\hat\xi$,
$|\hat\eta|^2$, $\sigma_{eb}^2/|\nu|^2_{eb}$ alone, defined and $t_*$-translation invariant for $t_*\ge\frac12$. So on
$\{t_*\ge\frac12\}$ outside $\Omega_*$, $\mathsf s = s_{\mathrm{in}}-(s_{\mathrm{in}}-
s_{\mathrm{out}})\psi_0(x_I)\chi_I$, which is $s_{\mathrm{in}}$ where $x_I\ge\epsilon_I$ (in particular over
$\{r^\sharp\le r\le r_0\}$ at these times). It is a slab order there: where it is constant, trivially; near $\mathscr
I^+$, $\pm\mathsf H(\psi_0(x_I)\chi_I)\ge0$ on $\partial\Sigma^\pm$ by the computation of II.C section 5.2,
*Monotonicity* ($\psi_0'\le0$ with $\mathsf Hx_I\le-\frac14x_I$, and $\phi'(\hat\xi)\mathsf H\hat\xi\ge0$), which uses
only II.C Lemmas 5.3-5.4 near $\mathscr I^+$; their proofs use only the bound $\mathsf H^{eb}-\mathsf H^0 =
O(x_I^{2\ell_I})$ on $\hat\xi$ and $O(x_I^{1+2\ell_I})$ on $x_I$, uniformly in $t_*$, which Lemma 1.2 (ii) provides for
$P^{\mathrm{ext}}$ on $\{t_*\ge\frac12\}$, the coefficients of $P^{\mathrm{ext}}-P_0$ being small there in the norms of
II.C Definition 3.3. "Slab order" in Propositions 3.4, 4.3, 4.4 and Theorem 6.1 (A) refers to this extension. Two slabs
$\Omega_1\subset\Omega_2$ are *nested with room $\delta>0$* if they have the same initial face and each final face of
$\Omega_1$ lies at distance at least $\delta$ (in $t^\flat$, resp. $r$) inside $\Omega_2$. Typical choices: $\Omega_1 =
\Omega_{T_0,T_1}$ and $\Omega_2 = \Omega^\sharp_{T_0,T_1} := \{T_0\le t^\flat\le T_1+1,\ r\ge r^\sharp\}$ with
$P^{\mathrm{ext}}$; or $\Omega_1 = \Omega_{T_0,T_1-\delta}\cap\{r\ge r_0+\delta\}$ and $\Omega_2 = \Omega_{T_0,T_1}$.
The spaces and Lemmas 1.3 and 2.5-2.7 hold for these domains with the same proofs, $\{r = r_0+\delta\}$ and $\{r =
r^\sharp\}$ being spacelike final faces (Lemma 1.2 (iv)).

**Lemma 3.3 (regularity on slabs).** (a) Let $\Omega_1\subset\Omega_2$ be nested with room $\delta$, with initial face
$\{t^\flat = T_0\}$, $T_0\ge1-\frac12\eta_0$, $\mathsf s_0<\mathsf
s$ slab orders, and $u\in H^{\mathsf s_0,2\alpha}(\Omega_2)^{\bullet,-}$ with $Pu\in H^{\mathsf
s-1,2\alpha+2}(\Omega_2)^{\bullet,-}$ ($P^{\mathrm{ext}}$ where defined). Then $u|_{\Omega_1}\in H^{\mathsf
s,2\alpha}(\Omega_1)^{\bullet,-}$ and
$$\|u\|_{H^{\mathsf s,2\alpha}(\Omega_1)^{\bullet,-}}\le C\big(\|Pu\|_{H^{\mathsf s-1,2\alpha+2}(\Omega_2)^{\bullet,-}}+
\|u\|_{H^{\mathsf s_0,2\alpha}(\Omega_2)^{\bullet,-}}\big).$$
(b) Let $\Omega_1 = \Omega_{T_0,T_1}\subset\Omega_3 := \Omega_{T_0-\delta,T_1}$ (same final faces;
$T_0-\delta\ge1-\eta_0$), $s_0<s$ constants, and $v\in H^{s_0,-2\alpha-2}(\Omega_3)^{-,\bullet}$ with $P^*v\in
H^{s-1,-2\alpha}(\Omega_3)^{-,\bullet}$. Then $v|_{\Omega_1}\in H^{s,-2\alpha-2}(\Omega_1)^{-,\bullet}$ with the
corresponding estimate.
The constants are uniform for $\epsilon_P$ small, with $d_0$ depending only on the orders.

*Proof.* (a) Let $\tilde u$ be an extension of $u$ supported in $\{t^\flat\ge T_0\}$, and $f\in H^{\mathsf
s-1,2\alpha+2}_e$ the minimal extension of $Pu$. Let $N_2$ be the union of the interior of $\Omega_2$ relative to its
final faces and of $\{t^\flat<T_0\}$, near the slab. On $N_2$, $P\tilde u = f$: $N_2$ is the open set to which the spaces
of $\Omega_2$ restrict, and this is what $Pu\in H^{\mathsf s-1,2\alpha+2}(\Omega_2)^{\bullet,-}$ means. So for operators
with Schwartz kernels in $N_2\times N_2$ the microlocal estimates below see $P\tilde u$ only through $f$. Fix a cut-off
$\chi_1$ equal to 1 near $\Omega_1$, supported in $N_2\cap\{t^\flat>T_0-\frac12\omega_0\}$, and let all operators be
carried by such cut-offs. We control $\tilde u$ microlocally at order $\mathsf s$ at every point of ${}^{e3b}S^*M$ over
$\mathrm{supp}\,\chi_1$ (a compact set in the compactified bundle).

Off the characteristic set: the elliptic estimate (II.A$'$ Theorem 3.1). On it over $M^\circ$: by II.C Proposition 4.2
and Lemma 1.2 (iv), the backward curve reaches $\{t^\flat<T_0\}$, where $\tilde u = 0$, in finite time, and stays in
$\{r>r_0-\delta\}$, as $dr$ is future timelike near $\{r = r_0\}$, so that $r$ cannot decrease along a backward curve
there. Propagation (II.A$'$ Theorem 5.4, at order $\mathsf s$, with $\mathsf H\mathsf s\le0$) controls $\tilde u$ there.
Over $\mathscr I^+$ off $R$: the curves of II.B Lemma 7.2 (1) (i), (iii) reach $\{t_*<T_0\}$ backward (below $t_* = 1$
the flow over $\mathscr I^+$ is still given by II.B (7.5), the normal form of $P^{\mathrm{ext}}$ being that of $P_0$
there); propagation as before. At $R_{[T_0,T_1+\delta/2]}$: Proposition 3.2, (3.2), with $t_- := T_0-\frac12\omega_0$,
$t_+ := T_1+\frac12\delta$, $\omega_0 := \min(\frac12\delta,\frac14\eta_0)$, at the constant value of $\mathsf s$ near
$R$. Its $E_-$ is microsupported in $\{t_*\le t_-\}$, where $\tilde u = 0$ (kernels in $\{t^\flat<T_0\}^2$), and its $E$
in a punctured neighbourhood of $R$ at times in $[t_--\omega_0,t_++\omega_0]$, from whose points the backward curves
reach $\{t^\flat<T_0\}$ (as above); by compactness of $\mathrm{WF}'(E)$ and the local boundedness of the entrance times
(II.A section 9.1, (O)), propagation bounds $\|E\tilde u\|_{\mathsf s}$. The finitely many operators so obtained are
jointly elliptic over $\mathrm{supp}\,\chi_1$, and II.A Lemma 8.4 (c) gives $\|\chi_1\tilde u\|_{\mathsf s,2\alpha}\le
C(\|\chi_1'f\|_{\mathsf s-1,2\alpha+2}+\|\chi_1'\tilde u\|_{\mathsf s_0,2\alpha})$. $\chi_1\tilde u$ is an extension of
$u|_{\Omega_1}$ supported in $\{t^\flat\ge T_0\}$, and $\chi'_1f$, $\chi_1'\tilde u$ depend only on $Pu$, $u$ (the
cut-off $\chi'_1$ being supported in $N_2$), with norms at most $C$ times the quotient norms. This is (a), in the strong
sense, since each estimate used is.

(b) The same with $-\mathsf H$: let $\tilde v$ be an extension supported in $F_3 := \Omega\cap\{t^\flat\le T_1,r\ge
r_0\}$; $P^*\tilde v$ is controlled on $N_3 :=$ the interior of $\Omega_3$ relative to its initial face, together with
$\{t^\flat>T_1\}\cup\{r<r_0\}$, where $\tilde v = 0$. Propagation for the backward problem is propagation for $-P^*$,
whose rescaled Hamilton field is $-\mathsf H$; it applies to constant orders. Every forward curve from a point of the
characteristic set over $\Omega_1$ either reaches $\{t^\flat>T_1\}\cup\{r<r_0\}$ in finite time, or enters any given
neighbourhood of $R_{[T_0,T_1]}$. Indeed $t^\flat$ increases along it; if it stays in the slab, its $\omega$-limit set
is non-empty, compact and invariant; a point of it over $M^\circ$ would have its orbit in the limit set with $t^\flat$
strictly increasing there, against $t^\flat$ being constant ($=\lim t^\flat$) on the limit set; so the limit set lies
over $\mathscr I^+$ at the time $t_\infty := \lim t^\flat\in[T_0,T_1]$, where $\mathsf Ht_* = t_*\hat\xi = 0$, so
$\hat\xi = 0$ and $|\hat\eta|^2 = \frac12\hat\xi(2-\hat\xi) = 0$: it lies in $R$. Over $\mathscr I^+$ the curves (iii)
of II.B Lemma 7.2 reach $\{t_*>T_1\}$ and the curves (i) tend to $R$. At $R_{[T_0-\delta/2,T_1]}$ use (3.3) with $t_- :=
T_0-\frac12\delta$, $t_+ := T_1+\frac12\omega_0$ ($\omega_0$ as in (a)); its $E_+$ quantises $e_+$, whose symbol is
supported in $\{t_*>t_+\}$ (proof of Proposition 3.2), and its Schwartz kernel lies in $K\times K$. Neither places the
kernel in $\{t^\flat>T_1\}$: the operator wave front set does not locate a kernel, and $K$ covers $\mathscr
I^+\cap\{t_--\omega_0\le t_*\le t_++\omega_0\}$ (D326; the D207 repair inferred $E_+\tilde v = 0$ from these two). So
quantise $e_+$ with Schwartz kernel within $\frac18\omega_0$ of the diagonal in $t_*$, as II.D does for $E$ after
Proposition 3.6; this changes $E_+$ by an operator of order $-\infty$ with kernel in $K\times K$, which the low-order
term of (3.3) absorbs, and the kernel now lies in $(K\cap\{t_*>t_+-\frac18\omega_0\})^2$. $K$ is any compact
neighbourhood of a compact part of $\mathscr I^+$, where $x_I = 0$, so we take it so small that
$t_*^{1+\ell_I}x_I^{2\ell_I}<\frac14\omega_0$ on $K$. Then on $K\cap\{t_*>t_+-\frac18\omega_0\}$, $t^\flat =
t_*-t_*^{1+\ell_I}x_I^{2\ell_I}>T_1+\frac18\omega_0$, where $\tilde v = 0$, so $E_+\tilde v = 0$. Conclude as in (a).
$\square$

### 3.3 Solvability

**Proposition 3.4 ([Hin26c] Corollary 8.2 and Proposition 8.3 at $n = 4$).** Let $\alpha<-\frac12+\bar p_1$, $\Omega' =
\Omega_{T_0,T_1}$ with $T_0\ge1$ ($P^{\mathrm{ext}}$ below $t^\flat = 1$), and $\mathsf s$ a slab order. There are
$d_0$, depending only on $\mathsf s$ (and, in (i), on $s'$), and $C$, uniform for $\epsilon_P$ small, such that: (i)
(*uniqueness*) if $u\in H^{s',2\alpha}(\Omega')^{\bullet,-}$ for some $s'\in\mathbb R$ and $Pu = 0$, then $u = 0$; (ii)
(*existence*) for every $f\in H^{\mathsf s-1,2\alpha+2}(\Omega')^{\bullet,-}$ there is $u\in H^{\mathsf
s,2\alpha}(\Omega')^{\bullet,-}$ with $Pu = f$ and
$$\|u\|_{H^{\mathsf s,2\alpha}(\Omega')^{\bullet,-}}
\le C\|f\|_{H^{\mathsf s-1,2\alpha+2}(\Omega')^{\bullet,-}}.\tag{3.4}$$
The same holds for $P^*$ and backward problems on $H^{s,-2\alpha-2}(\Omega')^{-,\bullet}$, $s$ constant, and for the
systems of section 4 and of Proposition 3.2.

*Proof.* (i) For $\delta>0$ small let $\Omega_\delta := \Omega_{T_0,T_1-\delta}\cap\{r\ge r_0+\delta\}$, nested in
$\Omega'$ with room $\delta$. By Lemma 3.3 (a) at the constant orders $s'<N$, $u|_{\Omega_\delta}\in
H^{N,2\alpha}(\Omega_\delta)^{\bullet,-}$ for every $N$, in particular for $N = 2$. By Lemma 1.3 (c), $D(\Omega_\delta)$
is dense in $H^{2,2\alpha}(\Omega_\delta)^{\bullet,-}$; both sides of the first estimate (2.4) on $\Omega_\delta$ are
continuous in that norm ($P$ maps it to $H^{0,2\alpha+2}$, whose quotient norm is the $L^2$-norm on the slab). So
$\|u\|_{H^{1,2\alpha}(\Omega_\delta)}\le C\|Pu\| = 0$, and $u = 0$ on $\Omega_\delta$ for every $\delta$.

(ii) *Step 1: weak solutions in $L^2$.* Let $\Omega^\sharp := \Omega^\sharp_{T_0,T_1}$ and $f^\sharp$ the restriction to
$\Omega^\sharp$ of the minimal extension of $f$ in $H^{\mathsf s-1,2\alpha+2}_e$; assume first $\inf\mathsf s\ge0$, so
that $f^\sharp\in H^{-1,2\alpha+2}(\Omega^\sharp)^{\bullet,-}$ with norm $\le C\|f\|$. For $v\in D_*(\Omega^\sharp)$, by
Lemma 1.3 (a),
$$|\langle f^\sharp,v\rangle|\le C\|f\|\,\|v\|_{H^{1,-2\alpha-2}(\Omega^\sharp)^{-,\bullet}}\le C'\|f\|\,
\|v\|_{H^{1,-2\alpha-2}(\Omega^\sharp)}\le C''\|f\|\,\|P^*v\|_{H^{0,-2\alpha}(\Omega^\sharp)},$$
the second inequality by Seeley's extension $E_0$ of Lemma 1.3 (b), which is bounded from the slab norm, and the third by
(2.4) for $P^{\mathrm{ext},*}$ on $\Omega^\sharp$. So $P^*v\mapsto\langle f^\sharp,v\rangle$ is a bounded functional on
$P^*D_*(\Omega^\sharp)$ in the $L^2$-norm. By Hahn-Banach and the Riesz theorem there is $u^\sharp\in
H^{0,2\alpha}(\Omega^\sharp)$, with $\|u^\sharp\|\le C\|f\|$ and $\langle u^\sharp,P^*v\rangle = \langle
f^\sharp,v\rangle$ for $v\in D_*(\Omega^\sharp)$. Extended by zero, $u^\sharp$ is supported in $\{t^\flat\ge T_0\}$, and
for $v\in D_*$ (a test function on $M$) $\langle Pu^\sharp,v\rangle = \langle u^\sharp,P^*v\rangle$. So $Pu^\sharp$ and
$f^\sharp$ agree on $D_*(\Omega^\sharp)$, which contains the $C^\infty_c$-functions supported in
$\{t^\flat<T_1+1,r>r^\sharp\}$: $Pu^\sharp = f^\sharp$ on $\Omega^\sharp$.

*Step 2: regularity.* Lemma 3.3 (a) with $\Omega' \subset\Omega^\sharp$ (room 1, resp. $r_0-r^\sharp$) and $\mathsf s_0
:= \min(0,\inf\mathsf s)-1$ gives $u := u^\sharp|_{\Omega'}\in H^{\mathsf s,2\alpha}(\Omega')^{\bullet,-}$ and (3.4). By
(i) it is the solution.

*Step 3: the backward problem at nonnegative orders.* The same argument with the roles exchanged: for $g\in
H^{\sigma-1,-2\alpha}(\Omega')^{-,\bullet}$, $\sigma\ge1$ an integer, let $\Omega_3 := \Omega_{T_0-\delta,T_1}$ (with
$P^{\mathrm{ext}}$ if $T_0-\delta<1$; $\delta := \frac12\eta_0$) and $g_3$ the restriction of the minimal extension, in
$L^2$. For $u\in D(\Omega_3)$, $|\langle u,g_3\rangle|\le\|u\|_{H^{0,2\alpha}}\|g_3\|\le C\|Pu\|_{H^{0,2\alpha+2}}\|g\|$
by (2.4) on $\Omega_3$, the $H^0$ quotient norm being the $L^2$ norm, so no extension operator is needed. Hahn-Banach
gives $v_3\in H^{0,-2\alpha-2}(\Omega_3)$ with $P^*v_3 = g_3$ (by the density of $D(\Omega_3)$, Lemma 1.3 (c)), and Lemma
3.3 (b) gives $S_*g := v_3|_{\Omega'}\in H^{\sigma,-2\alpha-2}(\Omega')^{-,\bullet}$ with $\|S_*g\|\le C\|g\|$.
Uniqueness for the backward problem is (i) with the roles exchanged. So $S_*$ is the solution operator, and $S_*P^*v = v$
for $v\in D_*(\Omega')$.

*Step 4: negative orders.* Let $\inf\mathsf s<0$ and $m\in\mathbb N$ with $-m<\inf\mathsf s-1$. Work on $\Omega^\sharp$
with $f^\sharp\in H^{-m-1,2\alpha+2}(\Omega^\sharp)^{\bullet,-}$. For $g\in H^{m,-2\alpha}(\Omega^\sharp)^{-,\bullet}$
put $\lambda(g) := \langle f^\sharp,S_*g\rangle$, with $S_*$ of Step 3 on $\Omega^\sharp$ (at order $\sigma = m+1$);
$|\lambda(g)|\le C\|f\|\,\|g\|$. By Lemma 1.3 (b) (at $m$, on $\Omega^\sharp$) there is $u^\sharp\in
H^{-m,2\alpha}(\Omega^\sharp)^{\bullet,-}$, $\|u^\sharp\|\le C\|f\|$, with $\langle u^\sharp,g\rangle = \lambda(g)$. For
$v\in D_*(\Omega^\sharp)$, $\langle Pu^\sharp,v\rangle = \langle u^\sharp,P^*v\rangle = \langle f^\sharp,S_*P^*v\rangle =
\langle f^\sharp,v\rangle$, so $Pu^\sharp = f^\sharp$ as in Step 1. Step 2 with $\mathsf s_0 := -m$ concludes.

The constants depend on $P$ through finitely many coefficient norms and the structural margins (timelike conditions,
threshold, dynamics), uniform for $\epsilon_P$ small; for the systems of section 4 the same margins hold, the coupling
being of first order with principal symbol vanishing at $R$ and not entering the threshold of Lemma 2.5 (it decays at
$\mathscr I^+$). $\square$

The source proves the step $\mathsf s\ge1$ with its Proposition 7.9 for a finite final time, a case Part II.D found to
fail (its finding (D2)); Proposition 3.2 replaces it. The source's Corollary 8.2 constructs the $H^1$-solution by
smoothing the coefficients and quoting finite-time solvability for smooth wave equations; Steps 1-3 construct it by
duality from the energy estimates instead (section 7, (E3)-(E4)).

## 4. b-regularity on slabs, and the tame estimates

### 4.1 Operators on slab spaces

**Lemma 4.1 ([Hin26c] Lemmas 8.7-8.8 at $n = 4$).** Let $\Omega'$ be a slab of section 3 (or of section 5), $\mathsf s$
an order function and $k\in\mathbb N_0$; the spaces are those of section 1.1 with any weight.

(a) A differential operator $Q$ of order $m$ whose coefficients, in a fixed frame (products of $\partial_{t_*}$,
$x_I\partial_{x_I}$, $x_I\partial_\omega$ near $\mathscr I^+$, of coordinate fields elsewhere), lie in
$C^{(d_0;k)}_{e;b}$ on a neighbourhood of $\Omega'$ maps $H^{(\mathsf s;k)}(\Omega')^{\bullet,-}$ to $H^{(\mathsf
s-m;k)}(\Omega')^{\bullet,-}$, and $H^{(\mathsf s;k)}(\Omega')^{-,\bullet}$ to $H^{(\mathsf
s-m;k)}(\Omega')^{-,\bullet}$, with norm at most $C_k$ times the coefficient norms; $d_0$ depends only on $\mathsf s$ and
$m$.

(b) (*Tame products, with room.*) Let $\Omega'\subset\Omega''$ be nested with room $\delta$. There are $d_0,\tilde d$,
depending only on $\mathsf s$, such that for all $k$, $0\le j\le k$, $\ell\in C^{(d_0;k)}_{e;b}$ near $\Omega''$ and
$w\in H^{(\mathsf s;k)}(\Omega'')^{\bullet,-}$,
$$\|(D^j_{[b]}\ell)(D^{k-j}_{[b]}w)\|_{H^{\mathsf s}(\Omega')^{\bullet,-}}
\le C_k\big(\|\ell\|_{(d_0;\tilde d)}\|w\|_{H^{(\mathsf s;k)}(\Omega'')^{\bullet,-}}+
\|\ell\|_{(d_0;k)}\|w\|_{H^{(\mathsf s;\tilde d)}(\Omega'')^{\bullet,-}}\big),$$
with $D_{[b]}$ as in II.A Notation 9.4 and $C_k$ depending also on $\delta$.

(c) (*Norms through words, with room.*) Let $\mathcal X = (X_1,\dots,X_J)$, $X_J = I$, be b-differential operators of
order 1 spanning $\mathcal V_b$ over a neighbourhood of $\Omega''$. Then $\|X^\alpha w\|_{H^{\mathsf
s}(\Omega'')^{\bullet,-}}\le C\|w\|_{H^{(\mathsf s;|\alpha|)}(\Omega'')^{\bullet,-}}$, and, for $\Omega'\subset\Omega''$
nested with room,
$$\|w\|_{H^{(\mathsf s;k)}(\Omega')^{\bullet,-}}
\le C_k\sum_{|\alpha|\le k}\|X^\alpha w\|_{H^{\mathsf s}(\Omega'')^{\bullet,-}}.$$

*Proof.* (a) Extend the coefficients by Seeley's operator across the final faces of $\Omega'$ (in $t^\flat$, resp. $r$,
with the other coordinates as parameters, and successively near the corner, where $dt^\flat$ and $dr$ are independent),
as in Lemma 1.2. The extension is bounded on $C^{(d_0;k)}_{e;b}$ for all $d_0,k$ ([Hin26c] Lemma 8.5 (2), whose proof is
that of Lemma 1.3 (b) with suprema in place of $L^2$-norms: the reflection commutes with the tangential fields, and $j$
derivatives in the normal variable cost $\sum_l|c_l|\epsilon_l^{-j}$). Call the extended operator $Q^\sharp$. If $\tilde
w$ extends $w$ and is supported in $\{t^\flat\ge T_0\}$, then $\chi Q^\sharp\tilde w$ extends $Qw$, for a cut-off $\chi$
equal to 1 near $\Omega'$, and is supported there; II.A Lemma 8.6 (a) bounds it. Take the infimum over $\tilde w$. The
case $-,\bullet$ is the same with the initial face.

(b) Let $\chi_3$ be a cut-off equal to 1 near $\Omega'$, supported in the union of $\{t^\flat<T_0\}$ and of the interior
of $\Omega''$ relative to its final faces, with bounded b-derivatives. For $w\in H^{(\mathsf s;k)}(\Omega'')^{\bullet,-}$
the distribution $z := \chi_3\tilde w$ does not depend on the extension $\tilde w$ supported in $\{t^\flat\ge T_0\}$, as
all such agree where $\chi_3\ne0$. So, taking $\tilde w$ minimal for the norm of order $(\mathsf s;i)$, $\|z\|_{(\mathsf
s;i)}\le C_i\|w\|_{H^{(\mathsf s;i)}(\Omega'')^{\bullet,-}}$ for every $i$, with the same $z$ (II.A Lemma 8.4 (a) for
multiplication by $\chi_3$). $z$ extends $w|_{\Omega'}$. Let $\ell^\sharp$ be the Seeley extension of $\ell$ and
$\chi_1$, $\chi_2$ cut-offs equal to 1 near $\Omega'$ with $\chi_2 = 1$ near $\mathrm{supp}\,\chi_1$ and $\chi_3 = 1$
near $\mathrm{supp}\,\chi_2$. Then $\chi_1(D^j_{[b]}\ell^\sharp)(D^{k-j}_{[b]}z)$ extends
$(D^j_{[b]}\ell)(D^{k-j}_{[b]}w)$, and II.A Proposition 9.6 with $B = \chi_1$, $B^\sharp = \chi_2$ bounds its $H^{\mathsf
s}$-norm by the right side, the terms with $\|\chi z\|_{(\mathsf s_0;\cdot)}$ being bounded by those with $\mathsf s$.

(c) The first bound: $X^\alpha\tilde w$ extends $X^\alpha w$. For the second, with $z$ as in (b), $\|z\|_{(\mathsf s;k)}$
is equivalent to $\sum_{|\alpha|\le k}\|X^\alpha z\|_{\mathsf s}$ (II.A (8.1) and Notation 9.4: two spanning sets give
equivalent norms), and by the Leibniz rule for words $X^\alpha z$ is a sum of terms $\chi'\,X^\beta\tilde w$ with
$|\beta|\le|\alpha|$ and $\chi'$ a b-derivative of $\chi_3$, supported where $\chi_3$ is; each such term is independent
of the extension, and its $H^{\mathsf s}$-norm is at most $C\|X^\beta w\|_{H^{\mathsf s}(\Omega'')^{\bullet,-}}$.
$\square$

The source proves (b) on $\Omega'$ itself, with a crude bound in the middle range of $j$ through an extension operator on
integer b-Sobolev spaces; it notes that no single extension operator respects all variable orders ([Hin26c] footnote 64).
With room, the cut-off $\chi_3$ is such an operator. Room is always available below, as every slab sits inside a larger
one on which $P$ (or $P^{\mathrm{ext}}$) is given.

### 4.2 The commuted system on slabs

On $\{r\ge r^\sharp\}\cap\{\frac12\le t_*\le\bar t\}$ let $\mathcal X_{\mathrm{sl}} :=
(V_1,V_2,\Omega_{12},\dots,\Omega_{34},I)$ with $V_1 := 2t_*\partial_{t_*}$, $V_2 := x_I\partial_{x_I} = -2r\partial_r$
and $\Omega_{ab}$ the rotation fields of $\mathbb S^3$, as in II.D$'$ section 3. It spans $\mathcal V_b$ there: near
$\mathscr I^+$ the b-vector fields are spanned by $\partial_{t_*}$, $x_I\partial_{x_I}$, $\partial_\omega$; elsewhere, as
$r\ge r^\sharp>0$ and $t_*\ge\frac12$, $\partial_{t_*} = (2t_*)^{-1}V_1$, $\partial_r = -(2r)^{-1}V_2$ and the
$\Omega_{ab}$ span all vector fields. Put $W := x_I^2t_*^{-1}$, which near $\mathscr I^+$ is $x_I'^2\rho_+^2$ of II.D$'$,
and $L := W^{-1}P$.

**Lemma 4.2 ([Hin26c] Lemma 7.12 on slabs).** For $P$ of class $((d_0;k),(2\ell_I,\ell_+,\ell_K))$, the family $\mathcal
X_{\mathrm{sl}}$ satisfies (C) of II.D$'$ section 2 on the region above with $R_i = 0$: $[L,X_i] = \sum_jQ_{ij}X_j$,
where $Q_{ij}$ is the sum of an operator of order 0 with bounded coefficients and a first-order edge operator whose
coefficients lie in $C^{(d_0;k-1)}_{e;b}$ and, near $\mathscr I^+$, in $x_IC^\infty+x_I^{2\ell_I}C^{(d_0;k-1)}_{e;b}$.

*Proof.* Near $\mathscr I^+$ this is II.D$'$ Lemma 3.1 (b), whose proof uses only II.C Lemma 3.4 near $\mathscr
I^+\cap\Omega$, which holds at finite times. Away from $\mathscr I^+$, $[L,X_i]$ is a second-order operator with
coefficients in $C^{(d_0;k-1)}$, as $X_i$ differentiates the coefficients once; writing each coordinate field as
$\sum_jc_jX_j$ with smooth $c_j$ gives the form $\sum_jQ_{ij}X_j$, the first-order part of $[L,X_i]$ going into
$Q_{iJ}X_J$. Patch the two representations with a partition of unity in $x_I$. $\square$

Consequently, by II.D$'$ Lemma 2.1 with $\lambda = 0$ and $R_i = 0$, for $u$ on a slab and $f := Pu$, the words $u^{(j)}
:= (X^\alpha u)_{\alpha\in\mathcal W_j}$ satisfy
$$P^{(j)}u^{(j)} = W\big(X^\alpha(W^{-1}f)\big)_\alpha+W\tilde f^{(j)},\qquad P^{(j)} := WL^{(j)} =
P\otimes\mathrm{Id}-WQ^{(j)},\tag{4.1}$$
with $Q^{(j)}$ the coupling of II.D$'$ (2.2) and $\tilde f^{(j)}_\alpha =
-\sum_{|S|\ge2}(\mathrm{ad}_{X_S}L)X^{\alpha\setminus S}u$. $P^{(j)}$ acts on $\mathbb C^{N|\mathcal W_j|}$. It has the
principal symbol of $P$; its first-order coupling $WQ^{(j)}$ has coefficients $O(x_I^{2+\min(1,2\ell_I)})$ near $\mathscr
I^+$, so its normal form at $\mathscr I^+$, (1.1), has the same $p_1$ as $P\otimes\mathrm{Id}$ (its zeroth-order part, of
size $O(x_I^2)$, changes $p_0$, which is never used), and its
principal symbol of order 1 vanishes at $R$. So $P^{(j)}$ satisfies everything sections 2-3 use, with the same margins,
and Proposition 3.4 holds for it (its last paragraph), with constants depending on finitely many coefficient norms of
$WQ^{(j)}$, which carry at most one b-derivative of those of $P$ (II.D$'$ Lemma 2.1). As $X^\alpha(W^{-1}f) =
W^{-1}\prod(X_{\alpha_i}+c_{\alpha_i})f$ with constants $c_i = -X_i\log W\in\{2,-2,0\}$, the first term on the right of
(4.1) is a word in shifted fields applied to $f$.

**Proposition 4.3 ([Hin26c] Proposition 8.6 at $n = 4$).** Let $\alpha<-\frac12+\bar p_1$, $\Omega' = \Omega_{T_0,T_1}$
with $T_0\ge1$, $\mathsf s$ a slab order and $k\in\mathbb N_0$. There is $d_0$, depending only on $\mathsf s$, such that
for $P$ of class $((d_0;k),(2\ell_I,\ell_+,\ell_K))$ with $\|P-P_0\|_{(d_0;k),(2\ell_I,\ell_+,\ell_K)}$ small, the
forward solution of $Pu = f$ satisfies
$$\|u\|_{H^{(\mathsf s;k),2\alpha}(\Omega')^{\bullet,-}}
\le C_k\|f\|_{H^{(\mathsf s-1;k),2\alpha+2}(\Omega')^{\bullet,-}},\tag{4.2}$$
uniformly for such $P$.

*Proof.* Let $\Omega'' := \Omega^\sharp_{T_0,T_1}$, nested around $\Omega'$ with room; $f''$ the restriction to
$\Omega''$ of the minimal extension of $f$ in $H^{(\mathsf s-1;k),2\alpha+2}_e$; $u''$ the forward solution on $\Omega''$
of $P^{\mathrm{ext}}u'' = f''$ (Proposition 3.4). By uniqueness $u''|_{\Omega'} = u$. We show by induction on $j\le k$:
$$\textstyle\sum_{|\alpha|\le j}\|X^\alpha u''\|_{H^{\mathsf s,2\alpha}(\Omega'')^{\bullet,-}}
\le C_j\|f''\|_{H^{(\mathsf s-1;j),2\alpha+2}(\Omega'')^{\bullet,-}}.\tag{4.3}$$
$j = 0$ is (3.4). Let $j\ge1$. Each b-vector field maps $H^{\mathsf t,2\beta}_e$ into $H^{\mathsf t-1,2\beta-1}_e$ (as
$\partial_\omega = x_I^{-1}x_I\partial_\omega$), so a priori $u''^{(j)}\in H^{\mathsf
s-j,2\alpha-j}(\Omega'')^{\bullet,-}$. The threshold holds also for the weight $\alpha-\frac j2$, so by Proposition 3.4
(i) for $P^{(j)}$ at that weight, $u''^{(j)}$ is the forward solution of (4.1), which by Proposition 3.4 (ii) at the
weight $\alpha$ lies in $H^{\mathsf s,2\alpha}(\Omega'')^{\bullet,-}$ with norm at most $C$ times that of the right side
of (4.1) in $H^{\mathsf s-1,2\alpha+2}(\Omega'')^{\bullet,-}$. The first term of the right side has norm at most
$C\|f''\|_{(\mathsf s-1;j)}$, by Lemma 4.1 (c). For $\tilde f^{(j)}$, let $|S| = q\ge2$. $W\mathrm{ad}_{X_S}L$ is a
second-order edge operator with coefficients in $C^{(d_0;j-q)}_{e;b}$, as each commutator with an element of $\mathcal
X_{\mathrm{sl}}$ preserves $\mathrm{Diff}^2_e$ (II.A Lemma 2.6 near $\mathscr I^+$) and differentiates the coefficients
once, and $W(\mathrm{ad}_{X_S}L)W^{-1}$ differs from it by lower order. Every edge vector field is a combination of the
$X_i$ with bounded coefficients ($x_I\partial_\omega = x_I\cdot\partial_\omega$), so $W\mathrm{ad}_{X_S}L = \sum_iA_iX_i$
with $A_i$ first-order edge operators with $C^{(d_0;j-q)}$ coefficients, and by Lemma 4.1 (a)
$$\|W(\mathrm{ad}_{X_S}L)X^{\alpha\setminus S}u''\|_{H^{\mathsf s-1,2\alpha+2}}
\le C\sum_i\|X_iX^{\alpha\setminus S}u''\|_{H^{\mathsf s,2\alpha}},$$
a sum over words of length $j-q+1\le j-1$, bounded by (4.3) at $j-1$. This proves (4.3) at $j$, the order staying
$\mathsf s$, so that $d_0$ depends only on $\mathsf s$. Finally, by Lemma 4.1 (c) with room, $\|u\|_{H^{(\mathsf
s;k)}(\Omega')}\le C_k\sum_{|\alpha|\le k}\|X^\alpha u''\|_{H^{\mathsf s}(\Omega'')}\le C_k\|f''\|\le C_k\|f\|$.
$\square$

**Proposition 4.4 ([Hin26c] Proposition 8.9 at $n = 4$; tame).** In the setting of Proposition 4.3, with $\mathsf s$
constant and in $\mathbb N_0$ near $\{r\le r_0\}$ ((E14)), there is $d\in\mathbb
N$, depending only on $\mathsf s$, such that for all $k$ and $P$ of class $((d_0;k),(2\ell_I,\ell_+,\ell_K))$ with
$\|P-P_0\|_{(d_0;d),\ldots}$ small,
$$\|u\|_{H^{(\mathsf s;k),2\alpha}(\Omega')^{\bullet,-}}
\le C_k\Big(\|f\|_{H^{(\mathsf s-1;k),2\alpha+2}(\Omega')^{\bullet,-}}+
\epsilon_{P,k}\|f\|_{H^{(\mathsf s-1;d),2\alpha+2}(\Omega')^{\bullet,-}}\Big),\tag{4.4}$$
with $\epsilon_{P,k} := \|P-P_0\|_{(d_0;k),(2\ell_I,\ell_+,\ell_K)}$, which may be taken over a neighbourhood of
$\Omega'$, and $C_k$ depending on $P$ only through a bound for $\epsilon_{P,d}$.

*Proof.* Let $\tilde d$ and the regularity of II.A Proposition 9.6 be those of Lemma 4.1 (b) at the orders $\mathsf s+1$
and $\mathsf s-1$, and $d := \tilde d+3$. For $k\le d$, (4.4) is (4.2), whose constant depends on
$\epsilon_{P,k}\le\epsilon_{P,d}$. For $k>d$ run the induction of Proposition 4.3 on nested slabs
$\Omega'\subset\Omega_{(2k)}\subset\Omega_{(2k-1)}\subset\dots\subset\Omega_{(0)} = \Omega''$, with room
$2^{-i-2}\min(1,r_0-r^\sharp)$ between $\Omega_{(i)}$ and $\Omega_{(i-1)}$, two slabs per step: step $j$ proves the
bound (4.3) on $\Omega_{(2j)}$ in the tame form $C_j(\|f''\|_{(\mathsf s-1;j)}+\epsilon_{P,j}\|f''\|_{(\mathsf
s-1;d)})$. The coefficients of $P^{(j)}$ carry at most one b-derivative of those of $P$, so the constant of Proposition
3.4 for $P^{(j)}$ depends on $\epsilon_{P,d}$ only. In $\tilde f^{(j)}$ write $L = L_0+(L-L_0)$, $L_0$ the operator of
$P_0$. The terms of $L_0$, and those of $L-L_0$ in which at most $2$ b-derivatives fall on the coefficients, are bounded
as in Proposition 4.3 by norms of $u''$ with at most $j-1$ words, on $\Omega_{(2j-2)}$, with constants depending on
$\epsilon_{P,2}$; by the induction hypothesis they are tame. In the others, $q'\ge3$ b-derivatives fall on a coefficient
$p$ of $P-P_0$. As in II.D$'$ Lemma 2.4 (b) and [Hin26c] (7.55)-(7.56), commute the second-order factor to the front; it
remains to bound $\|(D^{q'}_{[b]}D^{\le2}_ep)(D^{j-q}_{[b]}u'')\|_{H^{\mathsf s+1}(\Omega_{(2j)})}$, $q'\le q$. Lemma
4.1 (b) on $\Omega_{(2j)}\subset\Omega_{(2j-1)}$ with $D^{2}_{[b]}D^{\le2}_ep$ for $\ell$ and $(q'-2,j-q+q'-2)$ for
$(j,k)$ bounds it by
$$C_j\Big(\|p\|_{(d_1+2;\tilde d+2)}\|u''\|_{(\mathsf s+1;j-2)}+\|p\|_{(d_1+2;j)}\|u''\|_{(\mathsf s+1;\tilde d)}\Big)$$
on $\Omega_{(2j-1)}$, $d_1$ the regularity of Lemma 4.1 (b) and $d_0\ge d_1+2$. Here $\|u''\|_{(\mathsf s+1;j-2)}\le
C\|u''\|_{(\mathsf s;j-1)}$ on $\Omega_{(2j-1)}$ (II.A Lemma 8.4 (d), on slab spaces by taking extensions), which Lemma
4.1 (c) bounds by the words of length at most $j-1$ on the larger slab $\Omega_{(2j-2)}$, tame by step $j-1$;
$\|u''\|_{(\mathsf s+1;\tilde d)}\le C\|u''\|_{(\mathsf s;\tilde d+1)}\le C\|f''\|_{(\mathsf s-1;\tilde d+1)}$ by (4.2)
at $\tilde d+1<d$; $\|p\|_{(d_1+2;\tilde d+2)}\le C\epsilon_{P,d}$ and $\|p\|_{(d_1+2;j)}\le C\epsilon_{P,j}$. The
finitely many nested slabs used for a given $k$ make $C_k$ depend on $k$ only. Conclude with Lemma 4.1 (c). $\square$

The source states Proposition 8.9 for "$s\in\mathbb N$ an admissible order function"; the proof uses only what
Proposition 8.6 uses, and (4.4) holds for slab orders.

## 5. The black hole interior

The region $\{r_0\le r\le r^\natural\}$ at late times is unbounded in time: its closure meets $K^+$. There $dr$ is
timelike, and $-r$ serves as a time function. The estimates of sections 2-4 hold there with $-r$ in place of $t^\flat$,
with no radial set and no threshold ([Hin26c] section 8.2).

### 5.1 r-slabs

By Lemma 1.2 (iv) there is $\delta_0>0$ such that $dr$ is future timelike for the metric of $P^{\mathrm{ext}}$ on
$\{r^\sharp\le r\le r^\natural+\delta_0\}\cap\{t^\flat\ge1-\eta_0\}$. For $T_0\ge1-\frac12\eta_0$ and $r^\sharp\le a<b\le
r^\natural+\delta_0$ the *r-slab* is
$$\Omega^K_{[a,b]} := \{t^\flat\ge T_0,\ a\le r\le b\},$$
with $T_0$ understood and $P^{\mathrm{ext}}$ in place of $P$ where $P$ is not given. Its faces in $M^\circ$ are
$\{t^\flat = T_0\}$ and $\{r = b\}$, initial, and $\{r = a\}$, final: future causal vectors point into it across the
first two and out of it across the last, as $\nabla t^\flat$ is past and $\nabla r$ future timelike, and $dt^\flat$, $dr$
are independent where the faces meet. Its closure meets $\partial M$ only in $K^+\cap\{a\le r\le b\}$. There, in the
coordinates $(\rho_K = t_*^{-1},x)$, the e3b-vector fields are spanned by $\partial_{t_*} = -\rho_K^2\partial_{\rho_K}$
and $\partial_x$, and the b-vector fields by $t_*\partial_{t_*}$ and $\partial_x$ (II.A section 1, the spanning sets;
[Hin26c] calls these spaces cusp spaces). Only the weight at $K^+$ matters, and near the r-slabs we write $H^{\mathsf
s,\alpha_K}_K := H^{\mathsf s,(0,0,\alpha_K)}_{e3b}$ and $H^{(\mathsf s;k),\alpha_K}_K := H^{(\mathsf
s;k),(0,0,\alpha_K)}_{e3b;b}$, with the density $|dg|$, a smooth positive multiple of $|dt_*\,dx|$ there. So
$\|u\|_{H^{1,\alpha_K}_K}$ is equivalent to the $L^2$-norm of $t_*^{\alpha_K}(|u|+|\partial_{t_*}u|+|\partial_xu|)$. The
source glosses its norm as controlling $t_*^{-\alpha_K}u$ (section 7, (E12)).

Let $U^K := M^\circ\cap\{r>a\}$, $V^K := M^\circ\cap\{t^\flat>T_0,\ r<b\}$ and $U^K_0 := M^\circ\cap\{a<r<b\}$, and
define, with quotient norms,
$$H^{\mathsf s,\alpha_K}(\Omega^K_{[a,b]})^{\bullet,-} :=
\{u|_{U^K}:u\in H^{\mathsf s,\alpha_K}_K,\ \mathrm{supp}\,u\subset\{t^\flat\ge T_0,\ r\le b\}\},
\qquad H^{\mathsf s,\alpha_K}(\Omega^K_{[a,b]})^{-,\bullet} :=
\{v|_{V^K}:v\in H^{\mathsf s,\alpha_K}_K,\ \mathrm{supp}\,v\subset\{r\ge a\}\},$$
$$H^{\mathsf s,\alpha_K}(\Omega^K_{[a,b]})^{\bullet} :=
\{u|_{U^K_0}:u\in H^{\mathsf s,\alpha_K}_K,\ \mathrm{supp}\,u\subset\{t^\flat\ge T_0\}\},$$
and the mixed spaces of order $(\mathsf s;k)$ likewise. The first are the spaces of forward problems, the second those of
backward problems; the third is supported at $\{t^\flat = T_0\}$ only and extendible at both $r$-faces, the space of the
continuation estimates. $D(\Omega^K_{[a,b]})$ is the set of restrictions to $U^K$ of functions in $C^\infty_c(M^\circ)$
supported in $\{t^\flat>T_0,\ r<b\}$, and $D_*(\Omega^K_{[a,b]})$ that of restrictions to $V^K$ of functions in
$C^\infty_c(M^\circ)$ supported in $\{r>a\}$. Both consist of functions vanishing near $K^+$.

Lemma 1.3 holds for r-slabs, with these changes in its proof. The collar field is $Z := \nabla t^\flat$: $Zt^\flat =
G(dt^\flat)<0$, and $Zr = g^{-1}(dt^\flat,dr)>0$, as $\nabla t^\flat$ is past and $\nabla r$ future timelike. Near $K^+$,
$Z$ is a stationary vector field in $(t_*,x)$ plus one with coefficients $O(\rho_K^{\ell_K})$, so its flow changes $t_*$
by a bounded amount in bounded time and is bounded on $H^{m,\alpha_K}_K$, uniformly for bounded times and strongly
continuous. $-Z$ moves supports in $\{t^\flat\ge T_0,\ r\le b\}$ into $\{t^\flat>T_0,\ r<b\}$, and $Z$ moves supports in
$\{r\ge a\}$ into $\{r>a\}$. Seeley's operator is applied first across $\{r = b\}$ in the variable $r$, with
$(t_*,\omega)$ as parameters, and then across $\{t^\flat = T_0\}$ in the collar coordinates of $Z$, with collar width
$\frac12\eta_0$; along a collar line $r$ increases as $t^\flat$ decreases, so the extension of a function vanishing on
$\{r<a\}$ vanishes there. For density, one cuts off also at large times by $1-\chi_0(t_*/T)$, $T\to\infty$, whose
derivative along $\partial_{t_*}$ is $O(T^{-1})$ and along $\partial_x$ zero.

### 5.2 Energy estimates

**Lemma 5.1 ([Hin26c] Lemma 8.10 at $n = 4$).** Let $\alpha_K\in\mathbb R$ and $\Omega^K := \Omega^K_{[a,b]}$. There is
$C$, uniform for $\epsilon_P$ small with $d_0 = 2$ (the norm of $P-P_0$ with the weights $(0,0,\ell_K)$ suffices), such
that
$$\|u\|_{H^{1,\alpha_K}(\Omega^K)}\le C\|Pu\|_{H^{0,\alpha_K}(\Omega^K)},\quad u\in D(\Omega^K),
\qquad\|v\|_{H^{1,-\alpha_K}(\Omega^K)}\le C\|P^*v\|_{H^{0,-\alpha_K}(\Omega^K)},\quad v\in D_*(\Omega^K).\tag{5.1}$$
Here $H^{1,\beta}(\Omega^K)$ and $H^{0,\beta}(\Omega^K)$ are the $L^2(\Omega^K,|dg|)$-norms of
$t_*^\beta(|u|+|\partial_{t_*}u|+|\partial_xu|)$ and of $t_*^\beta u$, and $P^*$ is the adjoint for $|dg|$ and a fixed
smooth fibre inner product $h_K$. The same holds on $\Omega^K\cap\{t^\flat\le T_1\}$, with $\{t^\flat = T_1\}$ a further
final face.

*Proof.* Let $w := t_*^{2\alpha_K} = \rho_K^{-2\alpha_K}$, $N := \nabla r/|G(dr)|$, which is future timelike with $N(-r)
= 1$, and $|\zeta|^2 := \zeta_{t_*}^2+|\zeta_x|^2$ for covectors $\zeta = \zeta_{t_*}dt_*+\zeta_xdx$. On the r-slab, by
stationarity of $g_0$, compactness in $x$ and the decay of $g-g_0$, there are constants, uniform for $\epsilon_P$ small
with $d_0 = 2$, with: $|\mathrm{div}_gN|\le C_0$ and $|N\log w| = 2|\alpha_K||Nt_*|/t_*\le C_1$; $T(\nabla r,\nabla
r)(\zeta)\ge c_r|\zeta|^2$, by Lemma 2.2; and $|K_{w^{\pm1}\nabla r}(\zeta)|\le C_3w^{\pm1}|\zeta|^2$, by the formula for
$K_{fX}$ in Lemma 2.1, as $|\nabla w|\le Cw$ and $\nabla r$ has bounded first derivatives. $P-P_\Box$ is of first order
with bounded coefficients in the frame $\partial_{t_*},\partial_x$, so for any vector field $X$ with $|X|\le C_Xf$,
$|2\,\mathrm{Re}\langle(P-P_\Box)u,Xu\rangle|\le C_4f(|du|^2+|u||du|)$, with $C_4$ depending on $C_X$ and $h_K$ only.

*Forward.* Let $X := e^{2\Phi r}w\nabla r$, future timelike. By Lemma 2.1, $K_X = e^{2\Phi r}(K_{w\nabla
r}+2\Phi\,wT(\nabla r,\nabla r))\ge e^{2\Phi r}w(2\Phi c_r-C_3)|\zeta|^2$. Apply (2.1) on $O := \Omega^K$ to $u\in
D(\Omega^K)$, which has compact support in $\bar O$. The only face near which $u\ne0$ is $\{r = a\}$ (and $\{t^\flat =
T_1\}$), where $\nabla\varphi = \nabla r$ (resp. $-\nabla t^\flat$) is future timelike; with $X$ future timelike the
boundary term is $\ge0$ by Lemma 2.2. So
$$\int e^{2\Phi r}w(4\Phi c_r-2C_3-C_4)|du|^2\le2\,\mathrm{Re}\int\langle Pu,Xu\rangle+C_4\int e^{2\Phi r}w|u||du|
\le C_5\int e^{2\Phi r}w|Pu||du|+C_4\int e^{2\Phi r}w|u||du|.$$
Lemma 2.3 with $\tau := -r$, the weight $w$ and $\Phi\ge C_0+C_1$, where $u$ vanishes near the faces with $N\varphi>0$,
namely $\{t^\flat = T_0\}$ ($N\varphi = dt^\flat(N)>0$) and $\{r = b\}$ ($N\varphi = -dr(N) = 1$), gives $\int e^{2\Phi
r}w|u|^2\le4\Phi^{-2}\int e^{2\Phi r}w|Nu|^2\le C_6\Phi^{-2}\int e^{2\Phi r}w|du|^2$. With Cauchy-Schwarz the last term
above is at most $C_4C_6^{1/2}\Phi^{-1}\int e^{2\Phi r}w|du|^2$, and $C_5|Pu||du|\le\Phi c_r|du|^2+C_5^2(4\Phi
c_r)^{-1}|Pu|^2$. Fix $\Phi$ large: $\int e^{2\Phi r}w|du|^2\le C\int e^{2\Phi r}w|Pu|^2$. As $e^{2\Phi r}$ lies between
$e^{2\Phi a}$ and $e^{2\Phi b}$, this and the Poincaré inequality give the first estimate (5.1).

*Backward.* Let $Y := -e^{-2\Phi r}w^{-1}\nabla r$, past timelike. By Lemma 2.1, $K_Y = e^{-2\Phi r}(-K_{w^{-1}\nabla
r}+2\Phi\,w^{-1}T(\nabla r,\nabla r))\ge e^{-2\Phi r}w^{-1}(2\Phi c_r-C_3)|\zeta|^2$. For $v\in D_*(\Omega^K)$ the faces
near which $v\ne0$ are $\{t^\flat = T_0\}$ and $\{r = b\}$, with $\nabla\varphi = \nabla t^\flat$, resp. $-\nabla r$,
past timelike, so the boundary terms $2T(Y,\nabla\varphi)(dv)$ are $\ge0$ by Lemma 2.2. $P^* = P_\Box+(P^*-P_\Box)$ with
$P^*-P_\Box$ of first order with bounded coefficients. Lemma 2.3 in the reverse direction, with the weight $w^{-1}$,
applies, as $v$ vanishes near $\{r = a\}$ (and $\{t^\flat = T_1\}$), the only faces with $N\varphi<0$. The rest is as
before. $\square$

### 5.3 Solvability, uniqueness and continuation

A *slab order on an r-slab* is $\mathsf s\in C^\infty({}^{e3b}S^*M)$ with $\pm\mathsf H\mathsf s\le0$ on
$\partial\Sigma^\pm$ over it. Admissible order functions are slab orders on the r-slabs inside $\Omega_*$, by II.C
Proposition 5.1 (2); so are constants.

**Lemma 5.2 (the flow in the interior).** There is $c>0$ such that, over $\{r^\sharp\le r\le
r^\natural+\delta_0\}\cap\{t^\flat\ge1-\eta_0\}$, up to $K^+$ and for $\epsilon_P$ small, $\mathsf Hr\le-c$ on
$\partial\Sigma^+$ and $\mathsf Hr\ge c$ on $\partial\Sigma^-$. So $r$ decreases strictly along the future field, at a
rate bounded below, and there is no radial set and no trapping there.

*Proof.* $\mathsf H = \rho H_G$ with $\rho$ a positive defining function of fibre infinity, homogeneous of degree $-1$,
and $H_Gr = 2g^{-1}(\zeta,dr)$. On $\partial\Sigma^+$ the future field is $\mathsf H$ (II.C section 2.3): the projection
of $H_G$ there, $2g^{-1}(\zeta,\cdot)$, is future null, so $g^{-1}(\zeta,dr) = g(\zeta^\sharp,\nabla r)<0$, $\nabla r$
being future timelike. On $\partial\Sigma^-$ the signs reverse. $\rho\,g^{-1}(\zeta,dr)$ is homogeneous of degree 0 and
continuous on the compactified cosphere bundle over the closure of the region, up to $K^+$, where it is that of the
stationary metric $g_0$; it does not vanish on the characteristic set, which is compact. $\square$

**Lemma 5.3 (regularity on r-slabs).** (a) Let $r^\sharp\le a'<a<b<r^\natural+\delta_0$, $\Omega_1 :=
\Omega^K_{[a,b]}\subset\Omega_2 := \Omega^K_{[a',b]}$, $\mathsf s_0<\mathsf s$ slab orders, and $u\in H^{\mathsf
s_0,\alpha_K}(\Omega_2)^{\bullet,-}$ with $Pu\in H^{\mathsf s-1,\alpha_K}(\Omega_2)^{\bullet,-}$. Then $u|_{\Omega_1}\in
H^{\mathsf s,\alpha_K}(\Omega_1)^{\bullet,-}$ and
$$\|u\|_{H^{\mathsf s,\alpha_K}(\Omega_1)^{\bullet,-}}\le C\big(\|Pu\|_{H^{\mathsf s-1,\alpha_K}(\Omega_2)^{\bullet,-}}+
\|u\|_{H^{\mathsf s_0,\alpha_K}(\Omega_2)^{\bullet,-}}\big).$$
(b) Let $\delta>0$ with $T_0-\delta\ge1-\eta_0$ and $b+\delta\le r^\natural+\delta_0$, let $\Omega_3$ be the r-slab
$\{t^\flat\ge T_0-\delta,\ a\le r\le b+\delta\}$, $s_0<s$ constants, and $v\in H^{s_0,-\alpha_K}(\Omega_3)^{-,\bullet}$
with $P^*v\in H^{s-1,-\alpha_K}(\Omega_3)^{-,\bullet}$. Then $v|_{\Omega_1}\in H^{s,-\alpha_K}(\Omega_1)^{-,\bullet}$,
with the corresponding estimate.
Both hold for systems $P\otimes\mathrm{Id}-Q$, $Q$ of first order, with constants depending on finitely many coefficient
norms; they are uniform for $\epsilon_P$ small, with $d_0$ depending only on the orders.

*Proof.* (a) Let $\tilde u$ be an extension of $u$ supported in $\{t^\flat\ge T_0,\ r\le b\}$ and $f$ one of $Pu$; that
$Pu$ lies in $H^{\mathsf s-1,\alpha_K}(\Omega_2)^{\bullet,-}$ means $P\tilde u = f$ on $U_2 := M^\circ\cap\{r>a'\}$,
which contains the region outside the initial faces. Let $\chi_1$ be a cut-off equal to 1 near $\Omega_1$ and supported
in $\{r>\frac12(a+a')\}$, and carry all operators by such cut-offs. Off the characteristic set use the elliptic estimate
(II.A$'$ Theorem 3.1). On it, by Lemma 5.2, the backward curve from any point over $\mathrm{supp}\,\chi_1$ has $r$
increasing at a rate at least $c$, so within parameter time $(b-a'+1)/c$ it reaches $\{r>b\}$ or, earlier,
$\{t^\flat<T_0\}$, where $\tilde u = 0$, staying in $\{r>\frac12(a+a')\}$; this holds also over $K^+$. Propagation
(II.A$'$ Theorem 5.4, at the order $\mathsf s$, with $\mathsf H\mathsf s\le0$ along the future field) controls $\tilde u$
at every such point. Finitely many of these operators are jointly elliptic over $\mathrm{supp}\,\chi_1$, and II.A Lemma
8.4 (c) gives $\|\chi_1\tilde u\|_{\mathsf s}\le C(\|\chi_1'f\|_{\mathsf s-1}+\|\chi'_1\tilde u\|_{\mathsf s_0})$ with
$\chi'_1$ supported in $U_2$, which is (a) after taking infima over the extensions. (b) The same with the future field:
let $\tilde v$ extend $v$ with support in $\{r\ge a\}$; $P^*\tilde v$ is controlled on $V_3 :=
M^\circ\cap\{t^\flat>T_0-\delta,\ r<b+\delta\}$; forward curves from points over $\Omega_1$ reach $\{r<a\}$, where
$\tilde v = 0$, within bounded time, staying in $V_3$ as $t^\flat$ increases and $r$ decreases along them. Propagation
for $-P^*$ applies to constant orders. For systems the principal symbol is scalar and the coupling of lower order, which
the elliptic and real principal type estimates allow. $\square$

**Proposition 5.4 ([Hin26c] Proposition 8.11 and (8.40) at $n = 4$).** Let $\alpha_K\in\mathbb R$,
$T_0\ge1-\frac12\eta_0$, $r^\sharp<a<b\le r^\natural$ and $\mathsf s$ a slab order. There are $d_0$, depending only on
$\mathsf s$, and $C$, uniform for $\epsilon_P$ small, such that:

(i) (*uniqueness*) if $u\in H^{s',\alpha_K}(\Omega^K_{[a,b]})^{\bullet,-}$ for some $s'\in\mathbb R$ and $Pu = 0$, then
$u = 0$;

(ii) (*existence*) for every $f\in H^{\mathsf s-1,\alpha_K}(\Omega^K_{[a,b]})^{\bullet,-}$ there is $u\in H^{\mathsf
s,\alpha_K}(\Omega^K_{[a,b]})^{\bullet,-}$ with $Pu = f$ and
$$\|u\|_{H^{\mathsf s,\alpha_K}(\Omega^K_{[a,b]})^{\bullet,-}}
\le C\|f\|_{H^{\mathsf s-1,\alpha_K}(\Omega^K_{[a,b]})^{\bullet,-}};\tag{5.2}$$

(iii) (*continuation*) for $a<a^+<b$, every $u\in H^{s',\alpha_K}(\Omega^K_{[a,b]})^{\bullet}$, $s'\in\mathbb R$, with
$Pu\in H^{\mathsf s-1,\alpha_K}(\Omega^K_{[a,b]})^\bullet$ satisfies, in the strong sense,
$$\|u\|_{H^{\mathsf s,\alpha_K}(\Omega^K_{[a,b]})^{\bullet}}
\le C\big(\|Pu\|_{H^{\mathsf s-1,\alpha_K}(\Omega^K_{[a,b]})^{\bullet}}+
\|u\|_{H^{\mathsf s,\alpha_K}(\Omega^K_{[a^+,b]})^{\bullet}}\big).\tag{5.3}$$
The same holds for $P^*$ and backward problems at constant orders, and for systems $P\otimes\mathrm{Id}-Q$ with $Q$ of
first order.

*Proof.* (i) and (ii) are proved as Proposition 3.4, with Lemma 5.1 for (2.4), Lemma 5.3 for Lemma 3.3 and the r-slab
form of Lemma 1.3. For (i), $\Omega_\delta := \Omega^K_{[a+\delta,b]}$, and $D(\Omega_\delta)$ is dense in
$H^{2,\alpha_K}(\Omega_\delta)^{\bullet,-}$. For Step 1 of (ii), $\Omega^\sharp := \Omega^K_{[a-\delta_1,b]}$, $\delta_1
:= \min(1,a-r^\sharp)$, with $P^{\mathrm{ext}}$; for Step 3, $\Omega_3 := \{t^\flat\ge T_0-\delta,\ a\le r\le b+\delta\}$
with $\delta := \min(\frac12\eta_0,\delta_0)$, so $b+\delta\le r^\natural+\delta_0$, and the backward estimate (5.1) on
$\Omega_3$. There is no threshold, so the weight is any $\alpha_K$, and $P$ does not shift it.

(iii) Let $\delta_2 := \frac14(b-a^+)$ and $\chi = \chi(r)$ equal to 1 for $r\le a^++\delta_2$ and 0 for $r\ge
b-\delta_2$. If $\tilde u$ extends $u$ with support in $\{t^\flat\ge T_0\}$, then $\chi\tilde u$ is supported in
$\{t^\flat\ge T_0,\ r\le b-\delta_2\}$, so $v := \chi u\in H^{s',\alpha_K}(\Omega^K_{[a,b]})^{\bullet,-}$, and $Pv = g :=
\chi Pu+[P,\chi]u$. $[P,\chi]$ is a first-order operator with coefficients supported in $\{a^++\delta_2\le r\le
b-\delta_2\}$, so by Lemma 4.1 (a), with a cut-off, $\|g\|_{H^{\mathsf s-1,\alpha_K}(\Omega^K_{[a,b]})^{\bullet,-}}\le
C\big(\|Pu\|_{H^{\mathsf s-1,\alpha_K}(\Omega^K_{[a,b]})^\bullet}+\|u\|_{H^{\mathsf
s,\alpha_K}(\Omega^K_{[a^+,b]})^\bullet}\big)$. By (i), $v$ is the solution of (ii) with $f := g$, so $\|v\|_{\mathsf
s}\le C\|g\|_{\mathsf s-1}$, and in the strong sense, as (ii) produces a solution in $H^{\mathsf s}$ whenever $g\in
H^{\mathsf s-1}$. As $u = v$ on $\{r\le a^++\delta_2\}$, a partition of unity in $r$ gives (5.3). $\square$

### 5.4 b-regularity and the tame estimates

On $\{r^\sharp\le r\le r^\natural+\delta_0\}\cap\{t_*\ge\frac12\}$, with $x = (x^1,\dots,x^4)$ the Cartesian coordinates
of II.A Definition 1.3 (A), let
$$\mathcal X_K := (V_1,\dots,V_5,I),\qquad V_1 := t_*\partial_{t_*},\quad V_{1+j} := \partial_{x^j}\ (j = 1,\dots,4),$$
acting componentwise in a fixed trivialisation of the bundle. The $V_i$ commute. They span $\mathcal V_b$ near the
closures of the r-slabs, as near $(K^+)^\circ$ the b-vector fields are spanned by $t_*\partial_{t_*}$ and $\partial_x$
and in $M^\circ$ by all vector fields; and every e3b-vector field there is a combination of the $V_i$ with bounded
coefficients, as $\partial_{t_*} = t_*^{-1}V_1$ with $t_*\ge\frac12$.

**Lemma 5.5 ([Hin26c] (8.41)-(8.42) at $n = 4$).** For $P$ of class $((d_0;k),(2\ell_I,\ell_+,\ell_K))$, $\mathcal X_K$
satisfies (C) of II.D$'$ section 2 there, with $W = 1$ and $R_i = 0$: $[P,X_i] = \sum_jQ_{ij}X_j$, with $Q_{ij}$
first-order e3b-operators whose coefficients lie in $C^{(d_0;k-1)}_{e3b;b}$ (a stationary part plus a part
$O(\rho_K^{\ell_K})$).

*Proof.* In $(t_*,x)$ write $P = \sum a^{\mu\nu}\partial_\mu\partial_\nu+\sum b^\mu\partial_\mu+c$, the coefficients of
$P_0$ independent of $t_*$ and smooth, those of $P-P_0$ in $\rho_K^{\ell_K}C^{(d_0;k)}_{e3b;b}$ near $K^+$ (II.C
Definition 3.3). $[P,\partial_{x^j}]$ has the coefficients differentiated by $-\partial_{x^j}$; $[P,t_*\partial_{t_*}] =
[P,t_*]\partial_{t_*}-(t_*\partial_{t_*}\text{ applied to the coefficients})$, with $[P,t_*] = 2\sum_\nu
a^{t_*\nu}\partial_\nu+b^{t_*}$. In both cases a second-order operator in $\partial_{t_*},\partial_x$ results, with
coefficients in $C^{(d_0;k-1)}_{e3b;b}$, as $V_i$ is a b-vector field. Write each second-order term
$\partial_\mu\partial_\nu$ as $\partial_\mu\circ\sum_jc_{\nu j}V_j$ with $c_{\nu j}\in\{0,1,t_*^{-1}\}$; this is
$\sum_jQ_{ij}V_j$ with $Q_{ij}$ of first order. $[P,I] = 0$. $\square$

By II.D$'$ Lemma 2.1 with $\lambda = 0$ and $R_i = 0$, as in (4.1), for $u$ on an r-slab and $f := Pu$ the words $u^{(j)}
:= (X^\alpha u)_{\alpha\in\mathcal W_j}$ satisfy
$$P^{(j)}u^{(j)} = (X^\alpha f)_\alpha+\tilde f^{(j)},\qquad P^{(j)} := P\otimes\mathrm{Id}-Q^{(j)},
\qquad\tilde f^{(j)}_\alpha = -\sum_{|S|\ge2}(\mathrm{ad}_{X_S}P)X^{\alpha\setminus S}u.\tag{5.4}$$
$P^{(j)}$ is a system with scalar principal part and first-order coupling, whose coefficients carry at most one
b-derivative of those of $P$; Lemmas 5.1-5.3 and Proposition 5.4 hold for it, with no condition on the coupling, as on
r-slabs every first-order term is absorbed by the factor $\Phi$ in Lemma 5.1.

**Proposition 5.6 ([Hin26c] Propositions 8.12 and 8.13 at $n = 4$).** Let $\alpha_K$, $T_0$ and $r^\sharp<a<a^+<b\le
r^\natural$ be as in Proposition 5.4, and $\mathsf s$ a slab order.

(a) There is $d_0$, depending only on $\mathsf s$, such that for all $k\in\mathbb N_0$ and $P$ of class
$((d_0;k),(2\ell_I,\ell_+,\ell_K))$ with $\epsilon_{P,k}$ small, every $u\in
H^{(s';k),\alpha_K}(\Omega^K_{[a,b]})^\bullet$, $s'\in\mathbb R$, with $f := Pu$ satisfies, in the strong sense,
$$\|u\|_{H^{(\mathsf s;k),\alpha_K}(\Omega^K_{[a,b]})^\bullet}
\le C_k\big(\|f\|_{H^{(\mathsf s-1;k),\alpha_K}(\Omega^K_{[a,b]})^\bullet}+
\|u\|_{H^{(\mathsf s;k),\alpha_K}(\Omega^K_{[a^+,b]})^\bullet}\big).\tag{5.5}$$

(b) If $\mathsf s$ is constant and in $\mathbb N_0$ near $\{r = a\}$ ((E14)), there is $d\in\mathbb N$, depending
only on $\mathsf s$, such that for all $k$ and $P$ of that class with $\epsilon_{P,d}$ small,
$$\|u\|_{(\mathsf s;k)}\le C_k\Big(\|f\|_{(\mathsf s-1;k)}+\|u\|^{[a^+,b]}_{(\mathsf s;k)}+
\epsilon_{P,k}\big(\|f\|_{(\mathsf s-1;d)}+\|u\|^{[a^+,b]}_{(\mathsf s;d)}\big)\Big),\tag{5.6}$$
with the spaces of (5.5), the superscript marking the norm on $\Omega^K_{[a^+,b]}$, and $C_k$ depending on $P$ only
through a bound for $\epsilon_{P,d}$. Here $\epsilon_{P,k}$ may be the norm of $P-P_0$ over $\Omega^K_{[a,b]}$ alone: on
the room below $\{r = a\}$ used in the proof, $P$ is replaced by the operator whose coefficients are the Seeley
extensions across $\{r = a\}$ of those on $\Omega^K_{[a,b]}$ (as in Lemma 1.2), which agrees with $P$ on the r-slab.

*Proof.* (a) *Reduction to a forward problem.* With $\chi$ and $\delta_2$ as in the proof of Proposition 5.4 (iii), $v :=
\chi u$ lies in $H^{(s';k),\alpha_K}(\Omega^K_{[a,b]})^{\bullet,-}$ and solves $Pv = g := \chi f+[P,\chi]u$, and by Lemma
4.1 (a)
$$\|g\|_{H^{(\mathsf s-1;k),\alpha_K}(\Omega^K_{[a,b]})^{\bullet,-}}
\le C_k\big(\|f\|_{H^{(\mathsf s-1;k),\alpha_K}(\Omega^K_{[a,b]})^\bullet}+
\|u\|_{H^{(\mathsf s;k),\alpha_K}(\Omega^K_{[a^+,b]})^\bullet}\big).\tag{5.7}$$
As $u = v$ on $\{r\le a^++\delta_2\}$, it suffices to bound $\|v\|_{(\mathsf s;k)}$ by $C_k\|g\|_{(\mathsf s-1;k)}$.

*Induction.* Let $\Omega'' := \Omega^K_{[a-\delta_1,b]}$, $\delta_1 := \frac12\min(1,a-r^\sharp)$, $g''$ the restriction
to $\Omega''$ of the minimal extension of $g$, and $v''$ the forward solution of $Pv'' = g''$ on $\Omega''$ (Proposition
5.4 (ii)); by uniqueness $v''|_{\Omega^K_{[a,b]}} = v$. We show by induction on $j\le k$
$$\textstyle\sum_{|\alpha|\le j}\|X^\alpha v''\|_{H^{\mathsf s,\alpha_K}(\Omega'')^{\bullet,-}}
\le C_j\|g''\|_{H^{(\mathsf s-1;j),\alpha_K}(\Omega'')^{\bullet,-}}.\tag{5.8}$$
$j = 0$ is (5.2). Let $j\ge1$. A b-vector field maps $H^{\mathsf t,\beta}_K$ into $H^{\mathsf t-1,\beta-1}_K$, as
$t_*\partial_{t_*} = \rho_K^{-1}\partial_{t_*}$, so a priori $v''^{(j)}\in H^{\mathsf
s_-,\alpha_K-j}(\Omega'')^{\bullet,-}$ for some $\mathsf s_-$. By Proposition 5.4 (i) for $P^{(j)}$ at the weight
$\alpha_K-j$, $v''^{(j)}$ is the forward solution of (5.4), which by Proposition 5.4 (ii) at the weight $\alpha_K$ lies
in $H^{\mathsf s,\alpha_K}(\Omega'')^{\bullet,-}$, with norm at most $C$ times that of the right side of (5.4) in
$H^{\mathsf s-1,\alpha_K}(\Omega'')^{\bullet,-}$. By Lemma 4.1 (c), $\|X^\alpha g''\|_{\mathsf s-1}\le C\|g''\|_{(\mathsf
s-1;j)}$. For $|S| = q\ge2$, $\mathrm{ad}_{X_S}P$ is a second-order e3b-operator with coefficients in
$C^{(d_0;k-q)}_{e3b;b}$, as each commutator with a $V_i$ differentiates the coefficients once (Lemma 5.5); so it is
$\sum_iA_iX_i$ with $A_i$ first-order e3b-operators, and by Lemma 4.1 (a) $\|(\mathrm{ad}_{X_S}P)X^{\alpha\setminus
S}v''\|_{\mathsf s-1}\le C\sum_i\|X_iX^{\alpha\setminus S}v''\|_{\mathsf s}$, a sum over words of length $j-q+1\le j-1$,
bounded by (5.8) at $j-1$. This proves (5.8). By Lemma 4.1 (c) with room, $\|v\|_{(\mathsf s;k)}\le C_k\sum_{|\alpha|\le
k}\|X^\alpha v''\|_{\mathsf s}\le C_k\|g\|_{(\mathsf s-1;k)}$. Each step holds in the strong sense, so (5.5) does.

(b) As in Proposition 4.4, with $\mathcal X_K$, $W = 1$, nested r-slabs
$\Omega^K_{[a,b]}\subset\Omega_{(2k)}\subset\dots\subset\Omega_{(0)} = \Omega''$ with room $2^{-i-2}\delta_1$ at the
final face, two per step as there, and $d := \tilde d+3$. The one new term is $[P,\chi]u$ in (5.7). Its coefficients are
$\chi'$ times those of $P$, which are stationary smooth ones plus $O(\epsilon_{P,k})$ in $C^{(d_0;k)}$; by Lemma 4.1
(b), whose proof applies verbatim to the spaces $H(\cdot)^\bullet$ with room at both $r$-faces, here $\{a^++\delta_2\le
r\le b-\delta_2\}$ inside $\Omega^K_{[a^+,b]}$, $\|[P,\chi]u\|_{(\mathsf s-1;k)}\le C_k(\|u\|^{[a^+,b]}_{(\mathsf
s;k)}+\epsilon_{P,k}\|u\|^{[a^+,b]}_{(\mathsf s;\tilde d)})$, the stationary part contributing $\|u\|_{(\mathsf s;\tilde
d)}\le\|u\|_{(\mathsf s;k)}$ for $k\ge\tilde d$. The induction then gives (5.6), the norms of $g$ at order $(\mathsf
s-1;d)$ being bounded by (5.7) at $k = d$. $\square$

[Hin26c] states Propositions 8.11-8.13 for constant orders ("We do not need variable orders in this part", its footnote
66), and Theorem 8.14 applies them with the admissible order functions; here they hold for slab orders, which admissible
ones are (section 7, (E10)).

## 6. The global estimate

**Theorem 6.1 ([Hin26c] Theorem 8.14 at $n = 4$).** Let the weights $\alpha_I,\alpha_+,\alpha_K$ satisfy II.D (1.3), and
let $\mathsf s_0<\mathsf s$ be order functions admissible for $P_0$ with weights $\alpha_+$, $\alpha_K$ and margin 0
(II.C Definition 5.2). For every $k\in\mathbb N_0$ there is $C_k$ such that
$$\|u\|_{H^{(\mathsf s;k),(2\alpha_I,\alpha_+,\alpha_K)}_{e3b;b}(\Omega_*)^{\bullet,-}}
\le C_k\Big(\|Pu\|_{H^{(\mathsf s;k),(2\alpha_I+2,\alpha_++2,\alpha_K)}_{e3b;b}(\Omega_*)^{\bullet,-}}+
\|u\|_{H^{(\mathsf s_0;k),(2\alpha_I,\alpha_+,\alpha_K)}_{e3b;b}(\Omega_*)^{\bullet,-}}\Big)\tag{6.1}$$
for $P = P_0$, in the strong sense, and for every weakly admissible $P$ of class $((d_0;k),(2\ell_I,\ell_+,\ell_K))$ with
$\epsilon_{P,k}$ small, with $C_k$ uniform; $d_0$ depends only on $\mathsf s_0$ and $\mathsf s$. Moreover, if $\mathsf s$
and $\mathsf s_0$ are constant and in $\mathbb N_0$ near $\{r\le r_0\}$ ((E14)), there is $d\in\mathbb N$ such that for
every $k$ and every $P$ of that class with $\epsilon_{P,d}$ small,
$$\|u\|_{(\mathsf s;k)}\le C_k\Big(\|Pu\|_{(\mathsf s;k)}+\|u\|_{(\mathsf s_0;k)}+
\epsilon_{P,k}\big(\|Pu\|_{(\mathsf s;d)}+\|u\|_{(\mathsf s_0;d)}\big)\Big),\tag{6.2}$$
with the spaces and weights of (6.1), $\epsilon_{P,k} := \|P-P_0\|_{(d_0;k),(2\ell_I,\ell_+,\ell_K)}$ over $\Omega_*$,
and $C_k$ depending on $P$ only through a bound for $\epsilon_{P,d}$. Both hold uniformly when $P_0$ is replaced by the
stationary models of nearby parameters, or perturbed within the stationary wave-type operators.

The source assumes only the first condition of (1.3) (section 7, (E13)), and prints (8.46) with the weights
$(2\alpha_I,\alpha_+,\alpha_K)$ on $Pu$ (section 7, (E6)).

*Proof.* Let $f := Pu$, and assume the right side of (6.1) finite; then $u\in H^{(\mathsf s_0;k)}$, and $u$ is the
forward solution of $Pu = f$ on every slab and r-slab below, by Propositions 3.4 (i) and 5.4 (i).

*A partition of unity.* Let $\psi_t\in C^\infty(\mathbb R)$ equal 1 on $(-\infty,\frac72]$ and 0 on $[4,\infty)$, and
$\psi_r\in C^\infty(\mathbb R)$ equal 1 on $(-\infty,r_1^++\delta_3]$ and 0 on $[r^\natural-\delta_3,\infty)$, $\delta_3
:= \frac14(r^\natural-r_1^+)$. Put $\phi_A := \psi_t(t^\flat)$, $\phi_C := (1-\psi_t(t^\flat))\psi_r(r)$ and $\phi_B :=
(1-\psi_t(t^\flat))(1-\psi_r(r))$. They are smooth on $M$ with bounded b-derivatives ($\psi_r(r) = 0$ near $\iota^+$ and
$\mathscr I^+$, and $r$ is smooth near $(K^+)^\circ$), and $\phi_A+\phi_B+\phi_C = 1$. $\phi_A$ is supported in
$\{t^\flat\le4\}$; $\phi_B$ in $\{t^\flat\ge\frac72,\ r\ge r_1^++\delta_3\}$, where $\chi = 1$ by II.D (1.2); $\phi_C$ in
$\{t^\flat\ge\frac72,\ r\le r^\natural-\delta_3\}$. Let $\Omega_{1,5}$ be the slab of section 1.1 and $\Omega^K :=
\Omega^K_{[r_0,r^\natural]}$ the r-slab with $T_0 = 1$, which is $\Omega_*\cap\{r\le r^\natural\}$. On $\Omega_{1,5}$,
$\rho_+$ and $\rho_K$ are bounded above and below, and the spaces of (6.1) restrict to those of section 1.1 with the
weight $2\alpha_I$; on $\Omega^K$, $\rho_I$ and $\rho_+$ are, and they restrict to those of section 5.1 with the weight
$\alpha_K$. An extension of $u|_{\Omega_{1,5}}$ supported in $\{t^\flat\ge1\}$, multiplied by $\phi_A$, extends
$\phi_Au$; likewise for $\Omega^K$ and $\phi_C$. As multiplication by the $\phi$'s is bounded (II.A Lemma 8.4 (a)),
$$\|u\|_{(\mathsf s;k)}\le C\big(\|u\|_{H^{(\mathsf s;k),2\alpha_I}(\Omega_{1,5})^{\bullet,-}}+
\|\chi u\|_{(\mathsf s;k)}+\|u\|_{H^{(\mathsf s;k),\alpha_K}(\Omega^K)^\bullet}\big).\tag{6.3}$$

*(A) Finite times.* $\mathsf s$ is a slab order (section 3.2). By Proposition 4.3 on $\Omega_{1,5}$, with
$P^{\mathrm{ext}}$ below $t^\flat = 1$, $\|u\|_{H^{(\mathsf s;k),2\alpha_I}(\Omega_{1,5})^{\bullet,-}}\le
C_k\|f\|_{H^{(\mathsf s-1;k),2\alpha_I+2}(\Omega_{1,5})^{\bullet,-}}\le C_k\|f\|_{(\mathsf s;k)}$. The source applies its
Propositions 8.6 and 8.9 at $T_0 = 1$, below the range $T_0\ge\inf_\Omega t_*+1 = 2$ in which they are stated (section 7,
(E5)); Lemma 1.2 provides that case.

*(B) Away from the initial surface and the interior.* II.D$'$ Theorem 1.1, (1.1): $\|\chi u\|_{(\mathsf s;k)}\le
C_k(\|f\|_{(\mathsf s;k)}+\|u\|_{(\mathsf s_0;k)})$.

*(C) The interior.* $\mathsf s$ is a slab order on $\Omega^K$ (section 5.3). Proposition 5.6 (a) with $a := r_0$, $a^+ :=
r_1^+$, $b := r^\natural$ gives $\|u\|_{H^{(\mathsf s;k),\alpha_K}(\Omega^K)^\bullet}\le C_k(\|f\|_{(\mathsf
s-1;k)}+\|u\|^{[r_1^+,r^\natural]}_{(\mathsf s;k)})$. On $\Omega^K_{[r_1^+,r^\natural]}$, $u =
\psi_t(t^\flat)u+(1-\psi_t(t^\flat))\chi u$, as $\chi = 1$ on $\{t^\flat\ge\frac72,\ r\ge r_1^+\}$; so the last norm is
at most $C$ times the sum of the first two norms on the right of (6.3), which (A) and (B) bound.

Inserting (A)-(C) in (6.3) gives (6.1), and in the strong sense, as each of (A)-(C) holds in it. For (6.2) use
Proposition 4.4, II.D$'$ (1.2) and Proposition 5.6 (b) instead; the term
$\epsilon_{P,k}\|u\|^{[r_1^+,r^\natural]}_{(\mathsf s;d)}$ of (5.6) is bounded by (A) and (B) at $k = d$, with constants
depending on $\epsilon_{P,d}$ only. $d_0$ and $d$ are the largest of those of the three pieces. Uniformity in $P_0$: the
constants of sections 2-5 depend on $P_0$ through finitely many coefficient norms and the margins of II.C Lemma 3.2, of
(1.2) and of the dynamics of II.B, which are uniform as in II.D Remark 1.3; so are those of (B). $\square$

## 7. What this part found

(E1) *The normal form (8.3).* At $n = 3$ the source writes
$P\equiv\frac12x_I^2[-2(x_I\partial_{x_I}-2(1+p_1))\partial_{t_*}+2x_I^2\slashed\Delta+p_0]$. From its normal form at
$\mathscr I^+$ (II.C (3.3) at $n = 4$), with $x'_I = t_*^{1/2}x_I$ and $\rho_+ = t_*^{-1}$, the zeroth-order term is
$t_*^{-1}p_0$ (Lemma 1.1). At bounded times this is a bounded positive factor, and zeroth-order terms are absorbed by the
Poincaré inequality, so nothing below depends on it. At $n = 4$ the constant $2 = n-1$ of the bracket is $3$.

(E2) *The smallness in (8.4) is not needed.* The source chooses the fibre inner product with $\mathrm{Re}\,p_1$ close to
its infimum and also $|\mathrm{Im}\,p_1|<\epsilon$, $\|p_0\|<\epsilon$. In Lemma 2.5 every first-order term other than
$2x_I^2\tilde p_1\partial_{t_*}$ is kept as a quadratic form in the edge derivatives, absorbed by the exponential weight
in time, and $p_0$ by the Poincaré inequality (Lemma 2.3); only $\mathrm{Re}_{h_I}p_1\ge\bar p_1-\delta'$, (1.2), is
used. The source's justification of (8.4) (a block-diagonal inner product, its Definition 5.18 (3)) is therefore not
needed and not checked here.

(E3) *The localised radial estimates on slabs.* The proof of [Hin26c] Proposition 8.3 uses "the localized radial sink
estimate, Proposition 7.9" on a slab with a final time, which is Proposition 7.9 with finite $t_{*,+}$; Part II.D found
that case to rest on $H_Gt_*\ge0$ on the support of the commutant, which fails off the characteristic set (II.D (D2)
(c)). For the adjoint it uses "a localized estimate at the radial source $\partial R^+_{\mathscr I^+,\mathrm{out}}$ for
$P^*$-propagation analogous to Proposition 7.7, whose proof we leave to the reader". Proposition 3.2 proves both, with
the time function $F = t_*-\kappa x_I'^{2\ell_I}$ of Lemma 3.1, whose derivative along the flow is a sum of squares
modulo the principal symbol on a full neighbourhood of the radial set at bounded times.

(E4) *Solvability in $H^1$.* [Hin26c] Corollary 8.2 constructs the forward solution by smoothing the coefficients,
quoting finite-time solvability of wave equations with smooth coefficients and passing to a weak limit, and asserts its
uniqueness, which (8.5), proved for $u\in H^2$, gives for solutions in $H^1$ only after a density argument. Proposition
3.4 constructs the solution by duality from the energy estimates for $P$ and $P^*$, and proves uniqueness in every
$H^{s'}$ by regularity on nested slabs (Lemma 3.3) and the energy estimate on the dense class (Lemma 1.3 (c)).

(E5) *The initial time in Theorem 8.14.* Theorem 8.14 applies Propositions 8.6 and 8.9 "on a $t_*$-interval $[1,4]$",
while Proposition 8.3, on which they rest, assumes $\inf_\Omega t_*+1\le T_0$, that is $T_0\ge2$, the margin giving room
below the initial face for its extension argument. Lemma 1.2 extends $P$ below $t^\flat = 1$, and Lemma 1.3 uses a collar
of width $\frac12\eta_0$, so the slabs with $T_0\ge1$ are covered (Propositions 3.4 and 4.3).

(E6) *The weights in (8.46).* The tame estimate (8.46) carries the weights $(2\alpha_I,\alpha_+,\alpha_K)$ on $Pu$, where
(8.45) and Proposition 7.11 have $(2\alpha_I+2,\alpha_++2,\alpha_K)$. As printed it would bound $u$ by a weaker norm of
$Pu$ than (8.45) does, which is not what the proof gives. (6.2) carries the weights of (6.1).

(E7) *Tame products on slabs.* [Hin26c] Lemma 8.8 (3) proves the tame product estimate on the slab itself, through the
extension operator of its Lemma 8.7 on integer b-Sobolev spaces, and its footnote 64 notes that no single extension
operator respects all variable orders. With room, the cut-off $\chi_3$ of Lemma 4.1 (b) does this for every order, and
Propositions 4.4 and 5.6 (b) run on nested slabs; room is always available, as every slab sits inside a larger one on
which $P$ or $P^{\mathrm{ext}}$ is given.

(E8) *Quotient norms on slabs.* The source passes between the quotient norms of $H(\Omega')^{-,\bullet}$ and norms on the
slab without comment, for instance in the duality step of Proposition 8.3. Lemma 1.3 (b) proves the equivalence, with
Seeley's extension across the initial face, which preserves support at the final faces.

(E9) *The K-current at $n = 4$.* (8.10) holds at $n = 3$. At $n = 4$ (Lemma 2.4) the cross term $-2\zeta_{t_*}\xi$
becomes $-3\zeta_{t_*}\xi$ and the angular coefficient $-2(\beta+1)$ becomes $-(2\beta+3)$; the coefficient of
$\zeta_{t_*}^2$, $-(2\beta+1)$, which carries the threshold, is the same, so the threshold $\alpha_I<-\frac12+\bar p_1$
is unchanged. The cross term is absorbed whatever its size.

(E10) *Constant and variable orders in the interior.* [Hin26c] Propositions 8.11-8.13 are stated for constant $s$ ("We do
not need variable orders in this part", its footnote 66), and Theorem 8.14 applies them with the admissible order
functions, which need not be constant on $r^{-1}([m,r^\natural])$. Here they are proved for slab orders (Lemma 5.3 at the
variable order, Proposition 5.4 (ii) by the scheme of Proposition 3.4), and admissible orders are slab orders by II.C
Proposition 5.1 (2).

(E11) *"$s\in\mathbb N$".* Proposition 8.9 is stated for "$s\in\mathbb N$ an admissible order function"; the proof uses
only what Proposition 8.6 uses, and (4.4) holds for every slab order.

(E12) *The gloss after (8.38).* The source says the left side of (8.38) "controls $t_*^{-\alpha_K}u$ and its
derivatives". With its multiplier $X_0 = \rho_K^{-2\alpha_K}\nabla r$ and (8.39) the norm is that of
$\rho_K^{\alpha_K}L^2$, which controls $t_*^{\alpha_K}u = \rho_K^{-\alpha_K}u$ (section 5.1).

(E13) *A weight condition omitted in Theorem 8.14.* Theorem 8.14 assumes $\alpha_I<-\frac12+\bar p_1$ and the
admissibility of the orders, but not $\alpha_+<\alpha_I-\frac12$, the second condition of [Hin26c] (7.3), which
Proposition 7.11, invoked in its proof, assumes: it is the threshold at the incoming radial set over $\mathscr
I^+\cap\iota^+$, where the quantity $4(\alpha_I-\alpha_+-\frac12)$ must be positive (II.D Proposition 3.5, the source's
(7.19)), and it does not involve the orders. Theorem 6.1 assumes all of II.D (1.3).

(E14) *The extension in the tame estimates (D209).* Propositions 4.4 and 5.6 (b), and through them the tame bound (6.2),
extend the source term across the final face $\{r = r_0\}$, resp. $\{r = a\}$, by the minimal extension, which is
minimal for one norm only, while a tame bound needs control at the low and the high b-regularity at once. They are
therefore proved here only for orders that are constant and in $\mathbb N_0$ near $\{r\le r_0\}$ (for (5.6), near $\{r =
a\}$), and are so stated (D212: the eighty-eighth verifier's Minor 3); where they are applied (Part II.F$'$ sections
3-4, with the orders of its Lemma 2.3) the orders are such, and the extension $E$ of Part II.F$'$ Lemma 2.5, a Seeley
extension in $r$ at fixed $(t^\flat,\omega)$ glued to any extension away from $\{r = r_0\}$, is bounded at every order
of b-regularity at once; the proofs go through with it in place of the minimal extension. Across the time-final face of
a slab the source term is, wherever the propositions are applied, the restriction of one given on a larger slab.
Recorded from Part II.F$'$ section 8.2 (b).

## Sources

[Hin26c] P. Hintz, arXiv:2606.28008v1. READ: pp. 141-157 (section 8: (8.1)-(8.4), Lemma 8.1 with (8.5)-(8.23), Corollary
8.2, Proposition 8.3 with (8.24), Definition 8.4 with (8.25)-(8.26), Lemma 8.5, Proposition 8.6 with (8.27)-(8.30),
Lemmas 8.7-8.8 with (8.31)-(8.35) and footnote 64, Proposition 8.9 with (8.36), (8.37), Lemma 8.10 with (8.38)-(8.39) and
footnote 66, Proposition 8.11 with (8.40), Proposition 8.12 with (8.41)-(8.42), Proposition 8.13 with (8.43)-(8.44),
Theorem 8.14 with (8.45)-(8.46)); p. 116 ((7.3)) and the statements of Propositions 7.7, 7.9 and 7.11, through Parts II.D
and II.D$'$.

Part II.A: Definition 1.3, section 1 (spanning sets), Lemma 2.6, sections 4 and 7 (Lemmas 7.1, 7.3), section 8 ((8.1),
Lemmas 8.4, 8.6), section 9 (Notation 9.4, Proposition 9.6). Part II.A$'$: Theorems 3.1, 5.4. Part II.B: (7.1)-(7.5),
Lemma 7.2, Remark 8.3. Part II.C: section 1.1, Lemma 3.2, Definitions 3.3, 3.5, 5.2, Lemmas 3.4, 4.1, section 2.3, (3.3),
(5.1), Propositions 4.2, 5.1. Part II.D: (1.2)-(1.3), Lemma 1.1, Remark 1.3, Propositions 3.5-3.6 and the paragraph after
it, Lemmas 2.1-2.3, Lemma 3.4, (3.1), findings (D2)-(D3). Part II.D$'$: section 2 (Lemmas 2.1, 2.4, 2.5, condition (C)),
Lemma 3.1, Theorem 1.1 with (1.1)-(1.2).
