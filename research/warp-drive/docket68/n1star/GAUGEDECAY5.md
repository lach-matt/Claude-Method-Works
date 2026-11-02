# GAUGEDECAY5: the gauge vector of Part IX, and decay in the Regge-Wheeler-type and harmonic gauges

*Status.* Written (this note). Not verified by a second reader. Labels as in the supplement: *computed* (a program in
`checks/` with its `.out`, exact unless said otherwise, each with a negative control that fails), *deduced* (argument
written out here), *READ* (verbatim, with identifier and page, read at source).

*The item.* Part VIII (`proof5/PART-VIII-LINEAR.md`, Theorem 2.2, Corollary 2.3) proves that in the class every
linearised data set has a development $\dot g$ in the gauge of the nonlinear problem which settles to a change of mass,
$\dot g-\dot\mu K = O(t_*^{-(\alpha-2)+\epsilon'})$ on $\{r_0\le r\le R',\ t_*\ge T'\}$ with all derivatives. Part IX
(`proof5/PART-IX-GAUGE.md`, Corollary 2.3) shows that a solution in another gauge with the same data up to a linearised
diffeomorphism is $\dot g+\mathcal L_Xg$, and asserts nothing about $X$ (Remark 2.4). This note determines $X$ for the
two gauges of the paper's section 8.2.

*The result, in one paragraph.*
- **Regge-Wheeler-type gauge: closed.** The gauge vector is explicit and local in $(t,r)$: on each sphere it is built
  from $\dot g$'s components and their first derivatives by inverting the Laplacian and $\frac23\Delta(\Delta+3)$ on
  $S^3$; mode by mode it is [KI03]'s $X_a = \frac rk(f_a+\frac rkD_aH_T)$ (READ, and computed). Its $l = 0$ part is a
  time integral. So $\dot g$ in that gauge settles to $\dot\mu K$ at Part VIII's rate, on every $\{r_0<r\le R'\}$ (the
  horizon included), with a loss of two derivatives, uniformly in $l$ with no mode sum (Theorem 1.5). $X$ itself decays
  one power slower in its $l = 0$ time component and at the full rate otherwise. Proved from Part VIII (proved) and
  the lemmas here; the uniqueness of the gauge representative also uses Part IX (verified).
- **Harmonic gauge: not closed; what is proved is the obstruction and its exact form.** The harmonic-gauge solutions
  are $\dot g_{RW}+\dot\mu\,\mathcal L_{W^{**}}g+\mathcal L_{Z'}g$ with $\Box Z' = J$, $J$ supported in $l\ge2$ and
  decaying, and the $l = 0$ part of $Z'$ free ($\Box Z'_0 = 0$) (Proposition 2.1). A conserved horizon charge
  (Lemma 2.2, an exact identity) shows that when $\dot\mu\ne0$ **no** harmonic-gauge solution settles to $\dot\mu K$:
  the linear growth $\frac{\dot\mu}2\,v\,\mathcal L_{W^*}g$ is forced, with the explicit horizon-regular $W^{**}$
  (Theorem 2.3). Part III gives the frequency-domain counterpart (Proposition 2.5: a simple, rank-one pole of the
  unmodified 1-form resolvent at zero, range $W^*$, co-range the horizon functional). The time-domain decay of $Z'$
  modulo $W^*$ is **not** proved: the obstruction is stated in section 2.6.

## 0. Setting

- *The metric and charts.* $g := g_{b_0} = \Phi^*_{\mu_0}g^{\mathrm{KS}}_{\mu_0}$ (III.B (3.3), Proposition 3.4), with
  $\Phi_\mu(t,x) = (t-T_\mu(|x|),x)$ and $g^{\mathrm{KS}}_\mu = \eta+\mu|x|^{-2}(dt_{\mathrm{KS}}+d|x|)^2$. So $r :=
  |x|$ is the area radius of the spheres $\{t = c,\ |x| = r\}$ and $SO(4)$, acting on $x$, acts by isometries. With
  $v := t-T_{\mu_0}(r)+r$ (that is $t_{\mathrm{KS}}+r$), on $\{r\ge r_0\}$, $g = -f\,dv^2+2\,dv\,dr+r^2\gamma$, $f =
  1-\mu_0/r^2$, $r_h = \mu_0^{1/2}>r_0$ (the chart of III.D$'$ section 1). $t_*-v = r-\psi(r)-T_{\mu_0}(r)$ is a function
  of $r$ alone (III.B (3.3), (3.6)); on $\{r\le R'\}$, $|t_*-v|\le C_{R'}$, and $\partial_v = \partial_t =
  \partial_{t_*}$ at fixed $x$.
- *The class.* $G = O(2)\times O(2)$ (Part VII section 0). In Hopf coordinates, $x/r = (\cos\theta\cos\phi_1,
  \cos\theta\sin\phi_1,\sin\theta\cos\phi_2,\sin\theta\sin\phi_2)$, $\gamma = d\theta^2+\cos^2\theta\,d\phi_1^2+
  \sin^2\theta\,d\phi_2^2$. A $G$-invariant symmetric 2-tensor has components depending on $(v,r,\theta)$, and the
  reflections $\phi_i\mapsto-\phi_i$ kill every component with an odd number of $\phi_i$ indices: eight components
  $h_{ab}$, $h_{a\theta}$, $h_{\theta\theta}$, $h_{\phi_1\phi_1}$, $h_{\phi_2\phi_2}$ ($a,b\in\{v,r\}$). A $G$-invariant
  1-form has $X_v,X_r,X_\theta$ (deduced; the ansatz of supplement Proposition 10.2).
- *The mass change.* $K := \partial_\mu g_{(\mu,0)}|_{\mu_0}$ (Part VIII Corollary 2.3). At fixed $(t_{\mathrm{KS}},x)$,
  $\partial_\mu g^{\mathrm{KS}}_\mu = r^{-2}dv^2$, and $\frac d{d\epsilon}\Phi^*_{\mu+\epsilon}$ is the Lie derivative
  along $V := -(\partial_\mu T_\mu)|_{\mu_0}(r)\,\partial_t$. So (deduced)
  $$K = r^{-2}\,dv^2+\mathcal L_Vg,\qquad\mathcal L_Vg = 0\ \text{on}\ \{r\le2R_1\},\tag{0.1}$$
  since $T_\mu(\rho) = T_\mu(2R_1)$ for $\rho\le2R_1$ ($\chi_\infty = 0$ there, III.B (3.3)), so $V$ is a constant
  multiple of the Killing field $\partial_t$ there. $V$ is smooth and stationary.
- *Part VIII in the class.* $\dot g$ is $G$-invariant and smooth on $N = \Omega_*\cup\mathcal D$ (Part IX (IX1)), with
  $D\mathrm{Ric}(\dot g) = 0$. $N = \{t_{\mathrm{IVP}}\ge-\nu(r)\}$ is a union of spheres, $t_{\mathrm{IVP}} =
  t-\psi_{\mathrm{IVP}}(r)$ (III.B Lemma 3.7 (b)). Put $h := \dot g-\dot\mu K$ and $w := \alpha-2$; with Part VII
  section 4's $\alpha$, $w>2+\epsilon_t$ (Part VIII (2.3)). For a function or chart component $u$ put
  $|u|_k(v,r) := \sum_{j\le k}\sup_{S^3_{v,r}}|D^ju|$, $D$ ranging over $\partial_v$, $\partial_r$ and the rotation
  fields $\Omega_{ij} = x^i\partial_j-x^j\partial_i$. On $\{r_0\le r\le R'\}$ these and $\partial_t,\partial_x$ span the
  same module with bounded coefficients, and $\partial_t$ costs a factor $t_*^{-1}$ against $t_*\partial_{t_*}$. So
  Part VIII (2.3) reads (deduced): for every $k$, $R'$, $\epsilon'>0$ there are $C$, $N_k$, $T'$ with
  $$|h|_k\le C\,\|(\dot\gamma,\dot k)\|_{H^{N_k}}\,t_*^{-w+\epsilon'}\quad\text{on}\ \{r_0\le r\le R',\ t_*\ge T'\}.
  \tag{0.2}$$
- *Operators.* As in Part IX section 0: $\delta$, $G$, $\delta^*$, $\Theta(k) := \delta G k$, $\mathcal L_Xg =
  2\delta^*X$, and $\Box := 2\delta G\delta^*$ on 1-forms (III.D (1.1)), so that $\Theta(\mathcal L_Xg) = \Box X$. The
  harmonic gauge is $\Theta = 0$ (the paper's $\Gamma = -\Theta$, supplement Proposition 10.2).

## 1. The Regge-Wheeler-type gauge

### 1.1 The decomposition on the spheres

For a class tensor $h$ at a point $(v,r)$ of the orbit space (all operators below act on $S^3$, in $\theta$, with $(v,r)$
as parameters; $\langle u\rangle := |S^3|^{-1}\int_{S^3}u\,d\omega$, $|S^3| = 2\pi^2$):

- the *$l = 0$ part* $h_0 := \langle h_{ab}\rangle dy^ady^b+2r^2\langle H\rangle\gamma$, $H := \gamma^{ij}h_{ij}/(6r^2)$
  (the $SO(4)$-average; [KI03]'s $H_L$ normalisation);
- the *1-form potentials* $\beta_a := \hat\Delta^{-1}\hat D^ih_{ai}$, $\langle\beta_a\rangle = 0$; in the class
  $h_{ai}dz^i = d\beta_a$ exactly (Lemma 1.2 (c));
- the *scalar potential* $\tau := \mathcal G\,\hat D^i\hat D^jh^{\mathrm{TF}}_{ij}$, $\mathcal G :=
  [\frac23\hat\Delta(\hat\Delta+3)]^{-1}$ on mean-zero functions, $h^{\mathrm{TF}}$ the $\gamma$-traceless part;
- the *tensor part* $h^{\mathrm{TT}} := h^{\mathrm{TF}}-(\hat D\hat D-\frac13\gamma\hat\Delta)\tau$.

**Definition 1.1 (the Regge-Wheeler-type gauge in the class).** A $G$-invariant $h$ is in the RW-type gauge if
$\beta_v = \beta_r = 0$, $\tau = 0$ and $h_0 = cK$ for a constant $c$. By Lemma 1.3 (b) this is supplement Proposition
10.1's gauge: [KI03]'s $f_a = 0 = H_T$ for every scalar mode $l\ge2$, with the $l = 0$ part fixed to the mass change.

**Lemma 1.2 (the sphere; computed `checks/rwgauge5.py` R3, deduced).** (a) The $T^2$-invariant harmonics on $S^3$ are
$P_j(\cos2\theta)$, eigenvalue $-l(l+2)$, $l = 2j$ (R3 (a)); they are complete in the $T^2$-invariant $L^2$, since
$d\omega = \pi^2\,du$ on $u = \cos2\theta\in[-1,1]$ after the $\phi$ integrals. So class functions carry only even $l$,
and $\frac23k^2(k^2-3)\ge\frac{80}3$ on their mean-zero part ($k^2 = l(l+2)\ge8$): $\mathcal G$ is defined.
(b) $\hat D^i\hat D^j(\hat D_i\hat D_j-\frac13\gamma_{ij}\hat\Delta)\tau = \frac23\hat\Delta(\hat\Delta+3)\tau$ (R3 (b)),
so $\hat D^i\hat D^jh^{\mathrm{TT}}_{ij} = 0$.
(c) A class 1-form $a(\theta)d\theta$ with zero divergence is $C_1/\sin2\theta\,d\theta$, smooth only if $C_1 = 0$ (R3
(c)). With the Hodge decomposition, class 1-forms on $S^3$ are exact (no vector type), and, as the divergence of a class
symmetric 2-tensor is a class 1-form (R3 (d)), $\hat D^ih^{\mathrm{TT}}_{ij}$ is a class 1-form with zero divergence,
hence 0: $h^{\mathrm{TT}}$ is transverse traceless (the tensor type).
(d) *Bounds, uniform in $l$.* For $j = 1,\dots,4$, $\|\hat DP_j\|^2 = k^2\|P_j\|^2$ and $\|(\hat D\hat D-\frac13\gamma
\hat\Delta)P_j\|^2 = \frac23k^2(k^2-3)\|P_j\|^2$ (R3 (e), quadrature to 40 digits; the identities are integration by
parts with (b)). Hence, with the spectral norms $\|u\|^2_{H^s} := \sum_l(1+k^2)^s\|u_l\|^2$ and the projection being
orthogonal ($\langle(\hat D\hat D-\frac13\gamma\hat\Delta)\tau,h^{\mathrm{TT}}\rangle = \langle\tau,\hat D^i\hat D^j
h^{\mathrm{TT}}_{ij}\rangle = 0$):
$$\|\beta_a\|_{H^1}\le(\tfrac98)^{1/2}\|h_{a\cdot}\|_{L^2},\qquad\|\tau\|_{H^2}\le(\tfrac{243}{80})^{1/2}
\|h^{\mathrm{TF}}\|_{L^2},$$
the constants being $\sup_{l\ge2}(1+k^2)/k^2$ and $\sup_{l\ge2}(1+k^2)^2/(\frac23k^2(k^2-3))$, attained at $l = 2$ (R3
(f): both functions decrease in $k^2\ge8$). The rotation fields $\Omega_{ij}$ are Killing fields of $(S^3,\gamma)$, so
they commute with $\hat D$, $\hat\Delta$, $\mathcal G$ and the decomposition, and preserve $l$ and exactness; applying
the bounds to $\Omega^Jh$ and using $\sum\Omega_{ij}^2 = \hat\Delta$ and $H^2(S^3)\subset C^0$:
$$\sup|\beta_a|\le C\|\beta_a\|_{H^2}\le C'|h_{a\cdot}|_1,\quad\sup|\tau|\le C\|\tau\|_{H^2}\le C'|h^{\mathrm{TF}}|_0,
\quad\sup|\hat D\tau|\le C\|\tau\|_{H^3}\le C'|h^{\mathrm{TF}}|_1,$$
and the same with $D^j$ applied to both sides, since $\partial_v,\partial_r$ commute with the sphere operators ($\gamma$
does not depend on $(v,r)$). No harmonic sum is formed, and no constant depends on $l$.

**Lemma 1.3 (the gauge vector; computed R1, R2; READ [KI03]).** For a class tensor $h$ put
$$\xi[h] := \Big(-\beta_a+\frac{r^2}2\partial_a\big(\tau/r^2\big)\Big)dy^a-\frac12\hat D\tau.\tag{1.1}$$
(a) $\mathcal L_{\xi[h]}g$ has $a\theta$ components $-\partial_\theta\beta_a$, no $\phi$ components, and traceless angular
part $-(\hat D\hat D-\frac13\gamma\hat\Delta)\tau$ (R1, for arbitrary functions $\beta_a,\tau$ of $(v,r,\theta)$; the
control, with the weight $r^2\partial_a(\tau/r^2)$ replaced by $\partial_a\tau$, fails). So $h+\mathcal L_{\xi[h]}g$
has $\beta = 0$, $\tau = 0$, the same $h^{\mathrm{TT}}$ and the same $l = 0$ part ($\xi$ has none).
(b) For a scalar mode, $h_{ab} = f_{ab}S$, $h_{ai} = rf_aS_i$, $h_{ij} = 2r^2(H_L\gamma_{ij}S+H_TS_{ij})$ ([KI03] (2.4)-
(2.6)), $\beta_a = -\frac rkf_aS$, $\tau = 2r^2H_TS/k^2$, the orbit part of $\xi$ is $X_aS$ with [KI03]'s
$X_a = \frac rk(f_a+\frac rkD_aH_T)$ ((2.8)), and $h+\mathcal L_\xi g = F_{ab}S\,dy^ady^b+2r^2FS\gamma$ with [KI03]'s
invariants $F,F_{ab}$ ((2.7a)-(2.7b)) (R2, at $l = 2$ and $l = 4$, exact; control: $(r/k)^2$ replaced by $r/k^2$ in
$X_a$ fails). So the RW-type components are the gauge invariants, as supplement Proposition 10.1 (ii) states.
(c) *Uniqueness.* For a class 1-form $Z$ with no $l = 0$ part, $\xi[\mathcal L_Zg] = -Z$ (deduced from (a): with $Z_\theta
d\theta = d\eta$, $\langle\eta\rangle = 0$, $\mathcal L_Zg$ has $\beta_a = Z_a+r^2\partial_a(\eta/r^2)$, as $\partial_aZ_\theta
-\frac2r(\partial_ar)Z_\theta = \partial_\theta(r^2\partial_a(\eta/r^2))$, and $\tau = 2\eta$; insert in (1.1)). In
particular $\mathcal L_Zg$ has $\beta = \tau = 0$ only if $Z = 0$.

**Lemma 1.4 ($l = 0$: the linearised mass and Birkhoff; computed R4).** Let $h_0 = A\,dv^2+2B\,dv\,dr+C\,dr^2+2r^2H\gamma$,
functions of $(v,r)$, on a simply connected open subset $U$ of the orbit space.
(a) The linearisation of the five-dimensional Misner-Sharp mass $m = R^2(1-|dR|^2)$ ($m(g) = \mu_0$) is
$$\delta\mu[h_0] = 2\mu_0H+r^2(A+2fB+f^2C)-2r^2(\partial_v+f\partial_r)(rH).$$
It vanishes on $\mathcal L_Yg$ for every spherically symmetric $Y$, $\delta\mu[r^{-2}dv^2] = 1$, so $\delta\mu[K] = 1$ by
(0.1), and $\partial_v\delta\mu$, $\partial_r\delta\mu$ are combinations, with coefficients in $r$, of the components of
$D\mathrm{Ric}(h_0)$ (R4 (a)-(d); control: without its term $2\mu_0H$ it is not gauge invariant).
(b) If $D\mathrm{Ric}(h_0) = 0$ on $U$: $\delta\mu[h_0] =: c$ is constant, and with $h' := h_0-c\,r^{-2}dv^2+\mathcal
L_{Y_1}g$, $Y_1 := -rH\partial_r$ (which removes $H$, R4 (e)), the 1-form $\omega := (B'+\frac f2C')dv+\frac12C'dr$ of
$h'$'s components is closed, and for $d\zeta = \omega$, $\mathcal L_{\zeta\partial_v}g = h'$ (R4 (f); control: $\omega$
without $\frac f2C'$ is not closed modulo $D\mathrm{Ric}$). So
$$h_0 = c\,r^{-2}dv^2+\mathcal L_{Y[h_0]}g,\qquad Y[h_0] := \zeta\,\partial_v+rH\,\partial_r.\tag{1.2}$$
(c) A spherically symmetric Killing field is $c'\partial_v$ (R4 (g)); so $Y[h_0]$ is unique up to $c'\partial_v$, the
choice of $\zeta$'s constant. $D\mathrm{Ric}$ is validated on $\mathcal L_Yg$ and on $r^{-2}dv^2$ (R4 (h); control:
$D\mathrm{Ric}(r^{-3}dv^2)\ne0$).

### 1.2 The theorem

**Theorem 1.5 (Part VIII in the Regge-Wheeler-type gauge).** Let $\dot g$ be Part VIII's solution in the class
(Corollary 2.3), $\dot\mu$ its mass change, $h = \dot g-\dot\mu K$, $h_0$ its $l = 0$ part, $N^\circ := N\cap\{r>r_0\}$.
(a) $\delta\mu[h_0] = 0$, and with $Y[h_0]$ of (1.2), $\zeta$ normalised by $\zeta(v,r)\to0$ as $v\to\infty$ (possible by
(c)),
$$X_{\mathrm{RW}} := \xi[h]-Y[h_0]^\flat,\qquad\dot g_{\mathrm{RW}} := \dot g+\mathcal L_{X_{\mathrm{RW}}}g =
\dot\mu K+(h-h_0)+\mathcal L_{\xi[h]}g$$
is a smooth $G$-invariant linearised vacuum solution on $N^\circ$, in the RW-type gauge with $l = 0$ part exactly
$\dot\mu K$, inducing $(\dot\gamma,\dot k)$ plus the data of the linearised diffeomorphism $\mathcal L_{X_{\mathrm{RW}}}g$.
(b) *Decay.* For every $k$, $R'$, $\epsilon'>0$, on $\{r_0<r\le R',\ t_*\ge T'\}$,
$$|\dot g_{\mathrm{RW}}-\dot\mu K|_k\le C\,\|(\dot\gamma,\dot k)\|_{H^{N_{k+2}}}\,t_*^{-w+\epsilon'}:$$
Part VIII's rate, with a loss of two derivatives, the horizon included, uniformly in $l$ (no mode sum is formed); the
constant depends on $R'$, as Part VIII's does, and nothing is claimed uniformly in $r$.
(c) *The gauge vector.* On the same set: $|\xi[h]|_k\le Ct_*^{-w+\epsilon'}$ (with $N_{k+1}$); $rH_0$ and $d\zeta$, with
all derivatives, are $O(t_*^{-w+\epsilon'})$; and $|\zeta|\le Ct_*^{-w+1+\epsilon'}$. So $X_{\mathrm{RW}} =
O(t_*^{-(w-1)+\epsilon'})$, and its $l\ge2$ part, its $l = 0$ radial part and every derivative are
$O(t_*^{-w+\epsilon'})$. $X_{\mathrm{RW}}$ is unique up to $c'\partial_t^\flat$, the only $G$-invariant Killing fields.
(d) *Uniqueness of the representative* (uses Part IX, labelled verified). If $U\subset N^\circ$ is open and
$SO(4)$-invariant, $\Omega' := D_U(\Sigma_U)$, and $\dot g'$ is a $G$-invariant linearised vacuum solution on $\Omega'$
in the RW-type gauge inducing $(\dot\gamma,\dot k)$ plus the data of some $\mathcal L_Zg$, then $\dot g' =
\dot g_{\mathrm{RW}}$ on $\Omega'$.

*Proof.* *(a)* $\beta$ and $\tau$ depend smoothly on $(v,r,\theta)$ (elliptic inverses on $S^3$ with smooth
parameters), so $\xi[h]$ is smooth; its $\beta,\tau$ are $\dot g$'s, $K$ being $l = 0$. $D\mathrm{Ric}$ commutes with
the $SO(4)$-average, so $D\mathrm{Ric}(h_0) = (D\mathrm{Ric}\,\dot g)_0-\dot\mu D\mathrm{Ric}(K) = 0$. The orbit space of
$N^\circ$, $\{t>\psi_{\mathrm{IVP}}(r)-\nu(r),\ r>r_0\}$, is the region above a graph, hence simply connected; Lemma 1.4
(b) applies, and $\delta\mu[h_0]$ is a constant which, being an expression in $h_0$ and its first derivatives, tends to
0 along $\{r = r_1\}$ by (0.2): it vanishes. So $h_0 = \mathcal L_{Y[h_0]}g$ and $\dot g_0+\mathcal L_{-Y[h_0]}g =
\dot\mu K$; with Lemma 1.3 (a), $\dot g_{\mathrm{RW}}$ is in the RW-type gauge. $D\mathrm{Ric}(\mathcal L_Xg) = 0$ (Part
IX Lemma 2.1 (b)), and $\mathcal L_Xg$ changes the induced data by those of a linearised diffeomorphism. $G$-invariance:
every step is $O(4)$-equivariant and $\dot g$ is $G$-invariant.
*(b)* $\dot g_{\mathrm{RW}}-\dot\mu K = (h-h_0)+\mathcal L_{\xi[h]}g$. Averaging does not increase $|\cdot|_k$, and
$\mathcal L_{\xi}g$ is first order in $\xi$, which by Lemma 1.2 (d) and (1.1) costs one derivative of $h$ ($\beta_a$ one
angular, $\partial_a\tau$ one orbit, $\hat D\tau$ one angular): $|\mathcal L_\xi g|_k\le C|h|_{k+2}$. Apply (0.2).
*(c)* The bounds on $\xi$ and $rH_0$ are Lemma 1.2 (d) and (0.2). $\omega$ is algebraic in $h_0$ and the first
derivatives of $H_0$, so $|\omega|_k\le C|h|_{k+1}\le Ct_*^{-w+\epsilon'}$, and $w-\epsilon'>1$. Put $\zeta(v,r) :=
-\int_v^\infty\omega_v(v',r)\,dv'$; then $\partial_v\zeta = \omega_v$ and, by $d\omega = 0$, $\partial_r\zeta =
-\int_v^\infty\partial_{v'}\omega_r\,dv' = \omega_r$; so $\zeta$ is the normalised potential, and $|\zeta|\le
C\int_v^\infty v'^{-w+\epsilon'}dv'\le C'v^{-w+1+\epsilon'}$, with $|t_*-v|\le C_{R'}$. Killing fields: a $G$-invariant
Killing field $Z$ has $\xi[\mathcal L_Zg] = -Z_{\ge2} = 0$ (Lemma 1.3 (c)) and $Z_0 = c'\partial_v$ (Lemma 1.4 (c)).
*(d)* By Part IX Corollary 2.3 and Remark 2.4 (c), $\dot g' = \dot g+\mathcal L_{X'}g$ on $\Omega'$ with $X'$
$G$-invariant ($\Omega'$ is $SO(4)$-stable, so the decomposition applies on it). So $\dot g'-\dot g_{\mathrm{RW}} =
\mathcal L_Zg$, $Z := X'-X_{\mathrm{RW}}$, is in the RW-type gauge: by Lemma 1.3 (c), $Z_{\ge2} = 0$; its $l = 0$ part
$\mathcal L_{Z_0}g$ is $c''K$, and $c'' = \delta\mu[\mathcal L_{Z_0}g] = 0$ (Lemma 1.4 (a)). So $\mathcal L_Zg = 0$.
$\square$

*The loss of one power in $\zeta$.* It comes from the time integral and is attained by the implication "$\mathcal L_Yg$
decays $\Rightarrow$ $Y$ decays": $Y = (1+v)^{-q}\partial_v$ has $\mathcal L_Yg = O(v^{-q-1})$ with every derivative
(R5). Whether Part VIII's own $h_0$ makes $\zeta$ decay faster is not determined here.

*What this changes in supplement Proposition 10.1.* (10.1)'s reconstruction from the master fields, and the growth
$r^{3/2}$, $r^3$ of its coefficients in the fields [HKW18] bound (`checks/kirecon5.py` P2), are not used: the decay is
passed from Part VIII's $\dot g$ to $\dot g_{\mathrm{RW}}$ directly, on each $\{r\le R'\}$, with Part VIII's rate in
place of [HKW18]'s energy rate $\tau^{-2}$, and pointwise. For data in Part VIII's class (Hintz's, not [HKW18]'s), the
deduction of Proposition 10.1 (iv) is replaced by Theorem 1.5, a proof from Part VIII.

## 2. The harmonic gauge

### 2.1 The solutions

On the Ricci-flat $g$, $\Theta(\mathcal L_Xg) = \Box X = (d\delta+\delta d)X = -\nabla^a\nabla_aX$ for every class
1-form (computed, `checks/hgauge5.py` H1, with general coefficients; control: on the non-vacuum metric $f = 1-\mu/r$
the first equality fails; III.D (1.1) states it).

Let $N^{\mathcal D} := D_{N^\circ}(\Sigma^\circ)$ (Part IX Lemma 1.2: open, globally hyperbolic, $\supset N^\circ\cap\{
t_{\mathrm{IVP}}\ge0\}$). Write $e := \dot g_{\mathrm{RW}}-\dot\mu K$ (Theorem 1.5), so $e_0 = 0$, and let
$$W^* := r^{-2}dv-\frac{dr}{r(r+r_h)},\qquad W^{**} := \frac v2W^*+A\,dv+B\,dr,$$
$$A = \frac{s^2+2r^2\log\frac{r+s}r}{4sr^2},\qquad B = \frac{r^2s-3rs^2+2s^3+2r^3\log r+2(s^3-r^3)\log(r+s)-2s^3\log
s}{4rs(r^2-s^2)},\qquad s := r_h,$$
($W^*$ is III.D$'$ (2.1), supplement (10.2)), and $W^{**}_H := W^{**}-V^\flat$ with $V$ of (0.1).

**Proposition 2.1 (the harmonic-gauge solutions; deduced, (b) from Part IX).** (a) For every smooth 1-form $Z'$ on
$N^{\mathcal D}$ with $\Box Z' = -\Theta(e)$,
$$\dot g_H := \dot g_{\mathrm{RW}}+\dot\mu\,\mathcal L_{W^{**}_H}g+\mathcal L_{Z'}g$$
is a linearised vacuum solution in harmonic gauge inducing $(\dot\gamma,\dot k)$ up to the data of a linearised
diffeomorphism. Such $Z'$ exist for all smooth Cauchy data on $\Sigma^\circ$ (Part IX Lemma 1.1), $G$-invariant for
$G$-invariant data.
(b) Every harmonic-gauge linearised vacuum solution on $\Omega' = D_U(\Sigma_U)$ inducing $(\dot\gamma,\dot k)$ up to the
data of a linearised diffeomorphism is of this form on $\Omega'$ (Part IX Corollary 2.3 gives $\dot g'-\dot
g_{\mathrm{RW}} = \mathcal L_Yg$, and $\Theta(\dot g') = 0$ is $\Box(Y-\dot\mu W^{**}_H) = -\Theta(e)$).
(c) *The source has no $l = 0$ part.* $\Theta$ is $SO(4)$-equivariant and $e_0 = 0$, so $\Theta(e)_0 = 0$: the $l = 0$
part $Z'_0$ solves the homogeneous equation $\Box Z'_0 = 0$, and $Z'_{\ge2}$ solves $\Box Z'_{\ge2} = J := -\Theta(e)$,
with $|J|_k\le Ct_*^{-w+\epsilon'}$ on $\{r_0<r\le R',\ t_*\ge T'\}$ (Theorem 1.5 (b), loss of three derivatives).
(d) *The linearly growing part.* $\Box W^{**} = -\Theta(r^{-2}dv^2) = r^{-3}dv$, $A$ and $B$ are analytic on $\{r>0\}$,
across the horizon ($B$'s numerator vanishes at $r = s$), and $rA$, $rB$ are bounded at infinity (computed, H4; H3 gives
$\Theta(r^{-2}dv^2) = -r^{-3}dv$). With (0.1) and $\Theta(\mathcal L_Vg) = \Box V^\flat$, $\Box W^{**}_H = -\Theta(K)$.
So $K^* := K+\mathcal L_{W^{**}_H}g$ is the mass change in harmonic gauge, and $K^*-\frac v2\mathcal L_{W^*}g$ is
stationary (H4), with $\mathcal L_{W^*}g\ne0$ (H3): the harmonic-gauge mass change grows linearly in $v$.
(e) *Non-uniqueness.* $\Box W^* = 0$ (H3), so $Z'\mapsto Z'+cW^*$ preserves (a): $\dot g_H+c\,\mathcal L_{W^*}g$ is again
a harmonic-gauge solution with the same data up to a linearised diffeomorphism. A decay statement in the harmonic gauge
is therefore a statement modulo $\mathcal L_{W^*}g$, or for a chosen $Z'$.

*Proof.* (a) $D\mathrm{Ric}$ annihilates $\mathcal L_Xg$, and $\Theta(\dot g_H) = \Theta(\dot\mu K+e)+\dot\mu\Box
W^{**}_H+\Box Z' = 0$ by (d). Part IX Lemma 1.1 applies with $P = \Box$ (principal symbol $g^{-1}(\zeta,\zeta)$, Part IX
Lemma 2.1 (a)) on the globally hyperbolic $N^{\mathcal D}$; uniqueness there and the equivariance of $\Box$ give the
$G$-invariance. (b), (c), (e) are as stated. (d): $A$, $B$ involve $\log r$, $\log(r+s)$, $\log s$ and the
denominators $r$, $r+s$, $r^2-s^2$; the numerator of $B$ is analytic near $r = s$ and vanishes there (H4), so $B$ is
analytic there. $\square$

### 2.2 The horizon charge

For a 1-form $X$ near the horizon put
$$Q[X](v) := r_h^3\int_{S^3}\big(\delta X+(dX)_{vr}\big)\Big|_{r = r_h}d\omega,\qquad\ell(J)(v) := r_h^3\int_{S^3}
J(\partial_v)\big|_{r = r_h}d\omega,$$
$\ell$ being III.D$'$ (1.1)'s horizon functional (there on stationary forms).

**Lemma 2.2 (computed H2, H3).** (a) For every class 1-form $X$, at $r = r_h$,
$$r^3(\Box X)_v = \partial_v\big[r^3(\delta X+(dX)_{vr})\big]-\frac r{\sin\theta\cos\theta}\partial_\theta\big(
\sin\theta\cos\theta\,(dX)_{\theta v}\big)$$
(H2, exact with general coefficients; control: at $r = 2r_h$ it fails). Integrating over $S^3$:
$$\frac d{dv}Q[X] = \ell(\Box X).\tag{2.1}$$
(Deduced for every 1-form, not only the class: $(\Box X)_v = \partial_v(\delta X)+(\delta F)_v$, $F := dX$; at $r_h$,
where $g_{vv} = -f = 0$ and $g_{vr} = 1$, $(\delta F)_v = -\nabla_\mu F^{\mu r} = -(r^3\sqrt\gamma)^{-1}\partial_\mu(r^3
\sqrt\gamma F^{\mu r})$, with $F^{rr} = 0$ and $F^{vr} = F_{rv}$ ($g^{vv} = 0$), so $(\delta F)_v = \partial_vF_{vr}$
plus a divergence on $S^3$. H2 is this computation in the class.) $Q[X]$ depends only on the $l = 0$ part of $X$ (H2:
it vanishes on an $l = 2$ class 1-form; in general the $S^3$-integral sees only the average).
(b) $\delta W^* = 0$, $(dW^*)_{vr} = 2r^{-3}$, $Q[W^*] = 4\pi^2$; the Killing 1-form $(\partial_v)^\flat = -f\,dv+dr$ has
$Q = 4\pi^2\mu_0$ and $(\partial_v)^\flat-\mu_0W^*$ is closed; $\ell([\Box,v]W^*) = 4\pi^2$, III.D$'$ Lemma 3.1 (1)'s value;
$\ell(\Theta(r^{-2}dv^2)) = -2\pi^2$, and by (0.1) $\ell(\Theta(K)) = -2\pi^2$ (H3; control: $W^*$ with its $dr$ term
reversed is not in the kernel of $\Box$). And $\frac d{dv}Q[W^{**}] = 2\pi^2$ (H4).

(2.1) is the time-domain form of III.D$'$ Lemma 2.1 (1)-(3): $\ell$ annihilates $\Box$ of every stationary form smooth at
the horizon (the case $\partial_v = 0$ of (2.1)) and spans the annihilator of the range at zero energy.

### 2.3 The forced linear growth

**Theorem 2.3 (deduced from Part VIII, Theorem 1.5, Lemmas 1.4 and 2.2).** Let $\dot g_H = \dot g+\mathcal L_Zg$ be a
harmonic-gauge solution of Proposition 2.1 ($Z = X_{\mathrm{RW}}+\dot\mu W^{**}_H+Z'$, $G$-invariant). Then on the
horizon, for $v\ge v_0$ ($t_*\ge T'$),
$$Q[Z](v) = Q[Z](v_0)+2\pi^2\dot\mu\,(v-v_0)-\int_{v_0}^v\ell(\Theta(h))\,dv',\qquad|\ell(\Theta(h))|\le Cv^{-w+\epsilon'},$$
and $Q[Z-\dot\mu W^{**}_H](v)$ converges as $v\to\infty$. Consequently, if $\dot\mu\ne0$, no harmonic-gauge solution
settles to $\dot\mu K$ near the horizon at any integrable rate: there are no $\delta,\epsilon>0$ for which $(\dot
g_H-\dot\mu K)_0$ and its first derivatives are $O(t_*^{-1-\delta})$ on $\{|r-r_h|\le\epsilon\}$.

*Proof.* $\Box Z = \Theta(\mathcal L_Zg) = -\Theta(\dot g) = -\dot\mu\Theta(K)-\Theta(h)$, and $\ell(\Theta(K)) = -2\pi^2$
(Lemma 2.2 (b)); $\ell(\Theta(h))$ involves $h$ and its first derivatives at $r_h$, bounded by (0.2). Integrate (2.1).
$\dot\mu W^{**}_H$ has $\frac d{dv}Q = 2\pi^2\dot\mu$ ($V = $ const$\cdot\partial_t$ near $r_h$, $Q[V^\flat]$ constant), so
$Q[Z-\dot\mu W^{**}_H]$ has an integrable derivative. Now suppose $\dot\mu\ne0$ and $(\dot g_H-\dot\mu K)_0 =
O(t_*^{-1-\delta})$ with first derivatives near $r_h$. Then $\mathcal L_{Z_0}g = (\dot g_H-\dot\mu K)_0-h_0$ is
$O(t_*^{-\min(1+\delta,w-\epsilon')})$ there with first derivatives, and $\delta\mu$ of it vanishes (Lemma 1.4 (a)). By
Lemma 1.4 (b)-(c) (on a simply connected neighbourhood of the horizon's orbit), $Z_0 = (\zeta\partial_v+rH\partial_r)^\flat
+c'(\partial_v)^\flat$ with $d\zeta$, $H$, $dH$ integrable in $v$, so $\zeta\to\zeta_\infty$. Since $(\zeta\partial_v)^\flat
= \zeta(\partial_v)^\flat$ has $\delta = -\partial_v\zeta$ and $(d\,\cdot)_{vr} = \partial_v\zeta+f\partial_r\zeta+\zeta f'$,
$Q[(\zeta\partial_v)^\flat] = 4\pi^2\mu_0\zeta$ at $r_h$; and $Q[(rH\partial_r)^\flat] = Q[rH\,dv]\to0$. So $Q[Z] =
Q[Z_0]$ converges, against the growth $2\pi^2\dot\mu v$. $\square$

*Remark 2.4 (the coefficient $\frac12$, and supplement Proposition 10.2 (iv)).* Horizon regularity fixes the coefficient:
if $cvW^*+U$, $U$ stationary and smooth at the horizon, solves $\Box(cvW^*+U) = -\Theta(r^{-2}dv^2)$, applying $\ell$
(which kills $\Box U$ and $v\Box W^*$) gives $4\pi^2c = 2\pi^2$, so $c = \frac12$ (deduced from Lemma 2.2 (b)).
Proposition 10.2 (iv)'s $W^{**} = tW^*+A\,dt+B\,dr$ has the coefficient 1 in the static time, but is built on the static
chart's mass change and has $A = (\log f+\mu/r^2)/(2\sqrt\mu)$ (READ, N1STAR-PROOF.md section 10.4), singular at the
horizon; the cokernel argument does not constrain it, and the two statements concern different representatives. The
horizon-regular one is $W^{**}$ above: the mass change in harmonic gauge grows as $\frac{\dot\mu}2v\,\mathcal L_{W^*}g$.

### 2.4 What Part III gives: the frequency domain

**Proposition 2.5 (deduced from III.D Propositions 6.1-6.2 and III.D$'$ Lemma 2.1 and Proposition 4.1, Step 1).** Let
$\hat P(\sigma)$ be the spectral family of the unmodified 1-form wave operator $\Box$ at $b_0$ (III.D$'$'s $\hat P$,
the parameter $\mathsf p_0$), on III.D$'$'s spaces $\mathcal X_\sigma\to\mathcal Y_\sigma$, $\mathcal X_0\to\mathcal Y_0$.
(i) $\hat P(\sigma)$ is invertible for every $\sigma\ne0$ with $\mathrm{Im}\,\sigma\ge0$ (III.D Proposition 6.2, "mode
stability of $\Box$ on Tangherlini away from zero", READ at the supplement's proof5/PART-III-D-GAUGEPOT.md section 6).
(ii) $\hat P(0)$ has index 0, kernel $\mathrm{span}\{W^*\}$, and the annihilator of its range is spanned by $\ell$
(III.D$'$ Lemma 2.1 (2)-(3)).
(iii) Near $\sigma = 0$, with the augmented operator $\mathcal P_0(\sigma)$ of III.D$'$ Proposition 4.1, Step 1
(invertible for $|\sigma|\le c_0$, $\mathrm{Im}\,\sigma\ge0$, with a uniform bound) and $(u_\sigma,c_\sigma) :=
\mathcal P_0(\sigma)^{-1}(0,1)$, $(w_\sigma,d_\sigma) := \mathcal P_0(\sigma)^{-1}(f,0)$:
$$\hat P(\sigma)^{-1}f = w_\sigma-\frac{d_\sigma}{c_\sigma}u_\sigma,\qquad c_\sigma\ell(\psi) = 4\pi^2i\sigma+o(|\sigma|),
\quad u_\sigma\to W^*,\quad d_\sigma\ell(\psi)\to\ell(f),$$
the first two from III.D$'$ ((4.1) at $\gamma = 0$, with $\ell(TW^*) = -i\ell([\Box,t_*]W^*) = -4\pi^2i$), the third from
its Claim, and the fourth by applying $\ell$ to $\hat P(\sigma)w_\sigma+d_\sigma\psi = f$ and using $\ell\circ\hat P(0) =
0$ with $\hat P(\sigma)-\hat P(0) = \sigma T+\sigma^2P_2$, the $w_\sigma$ being bounded. So the resolvent has at
$\sigma = 0$ a simple pole of rank one, $\hat P(\sigma)^{-1} = \frac i{4\pi^2\sigma}W^*\otimes\ell+o(|\sigma|^{-1})$
(applied to a fixed $f$, in $H^{s'}$ on compact sets).
(iv) On the $l\ge2$ part of the class the pole is absent: $\ell$ vanishes there and $W^*$ is $l = 0$, so $\hat P(0)$,
which commutes with the $SO(4)$-projections (these act boundedly on $\mathcal X_0$, $\mathcal Y_0$, the weights being
functions of $|x|$), is invertible on the $l\ge2$ subspace.

So the frequency domain predicts exactly what Theorem 2.3 finds in time: the residue's coefficient
$\frac1{4\pi^2}\int\ell(J)\,dv$ is the charge's increment divided by $Q[W^*] = 4\pi^2$; the stationary source
$\dot\mu\Theta(K)$ meets the simple pole and produces the linear growth $\frac{\dot\mu}2vW^*$; and a decaying source
produces $cW^*$ plus decay.

### 2.5 What is not proved, and the exact obstruction

*Not proved:* that $Z'$ of Proposition 2.1 equals $cW^*+c'(\partial_t)^\flat+o(1)$ on compact sets, with a rate, for
$G$-invariant data, which with Theorem 1.5 would give: every harmonic-gauge solution in the class equals
$\dot\mu K^*+c\,\mathcal L_{W^*}g+O(t_*^{-\kappa})$ on $\{r\le R'\}$ (the counterpart of [Hun19] Theorems 1.3-1.4,
supplement Proposition 10.2 (iv)). This is a time-domain statement for $\Box$, and:

1. *No time-domain theorem in Parts I-III covers $\Box$.* Part II.F$'$ Theorem 1.1 (forward solutions, `proof5/
   PART-II-F2-TAME.md`) needs $P_0$ $\aleph$-admissible (II.C Definition 2.7), whose item (3) is itself a stationary
   time-domain estimate; for the linearised gauge-fixed Einstein operator it is proved in III.H$'$ (2-admissibility,
   with the zero energy contributions integrated in $t_*$). Nothing analogous is written for $\Box$, whose zero energy
   pole (Proposition 2.5 (iii)) is of the same kind as those III.H-III.H$'$ handle for $L_b$ by augmentation. Even on the
   $l\ge2$ sector, where (Z) holds (Proposition 2.5 (iv)), Theorem 1.1 gives $K^+$-weight $-\aleph$ (growth allowed);
   decay at $K^+$ needs the analogue of III.H-III.I for $\Box$, and the framework is stated on full bundles, not on the
   $SO(4)$-isotypic subspaces.
2. *The source class.* $J = -\Theta(e)$ is controlled by Theorem 1.5 on compact $r$-sets only, not in the weighted
   spaces of II.F$'$ (1.4) at $\mathscr I^+$: the behaviour of $\dot g_{\mathrm{RW}}$ at null infinity is not
   established here (the growth in $r$ of `checks/kirecon5.py` P2 is the master-field form of this). Using
   $-\Theta(\dot g)$ directly (Part VIII's $\dot g$ lies in III.J$'''$'s classes) avoids the RW step but leaves item 1.
3. *The $l = 0$ sector* is homogeneous ($\Box Z'_0 = 0$, Proposition 2.1 (c)); its decay modulo $W^*$ is the radial
   1-form problem the supplement's section 10.11 takes by another route (deduced there, not proved).

So the paper's harmonic-gauge route (supplement Propositions 10.2-10.5, sections 10.7-10.11) keeps its status as a
deduction; what is now proved is its non-decaying part: the linear growth $\frac{\dot\mu}2v\,\mathcal L_{W^*}g$ is
forced (Theorem 2.3), with the explicit horizon-regular $W^{**}$, and the stationary freedom is exactly
$\mathcal L_{W^*}g$ (Proposition 2.1 (e), Proposition 2.5 (ii)).

## 3. Findings, labels, sources and files

*Findings.*
- (GD1) In the class the Regge-Wheeler-type gauge vector is $\xi[h]$ of (1.1) at $l\ge2$ (angular inverses of order
  $-1$ and $-2$, so bounded uniformly in $l$ with no mode sum) and a time integral at $l = 0$. Part VIII's decay passes
  to the RW-type gauge at the same rate with a loss of two derivatives, on every $\{r_0<r\le R'\}$ (Theorem 1.5).
  For data in Part VIII's class, Proposition 10.1 (iv)'s deduction from [HKW18] is replaced by a proof from Part VIII.
- (GD2) The RW-type gauge vector decays: $O(t_*^{-(w-1)+\epsilon'})$ after removing $c'\partial_t$, the full rate in
  every component but the $l = 0$ time component and in every derivative (Theorem 1.5 (c)).
- (GD3) A conserved horizon charge for the 1-form wave equation, $\frac d{dv}Q[X] = \ell(\Box X)$ (Lemma 2.2), the
  time-domain form of III.D$'$ Lemma 2.1. With $\ell(\Theta(K)) = -2\pi^2$ and $Q[W^*] = 4\pi^2$ it forces the linear
  growth $\frac{\dot\mu}2v\,\mathcal L_{W^*}g$ in the harmonic gauge (Theorem 2.3); the horizon-regular gauge-fixed mass
  change $K^*$ is explicit (Proposition 2.1 (d)). Supplement Proposition 10.2 (iv)'s coefficient 1 belongs to a
  representative singular at the horizon (Remark 2.4).
- (GD4) Part III gives the unmodified 1-form resolvent on the closed upper half plane: invertible off 0, a simple rank-one
  pole at 0 with range $W^*$ and co-range $\ell$ (Proposition 2.5). It does not give the time-domain decay of $Z'$
  modulo $W^*$; the obstruction is section 2.5.

*Labels.* Computed: `checks/rwgauge5.py` R1-R5, `checks/hgauge5.py` H1-H4 (exact, with H4's second component also at 40
digits, R3 (e) by quadrature at 40 digits; every check with a failing control). Deduced: Lemmas 1.2 (d), 1.3 (c),
Theorem 1.5, Proposition 2.1, Theorem 2.3, Remark 2.4, Proposition 2.5. READ: [KI03] below. Theorem 1.5 (a)-(c) and
Theorem 2.3 rest on Part VIII (proved) and on this note; Theorem 1.5 (d) and Proposition 2.1 (b) also on Part IX
(verified).

*Sources.* READ: [KI03] H. Kodama and A. Ishibashi, arXiv:hep-th/0305147v3: p. 4, (2.4)-(2.6), "Each harmonic mode of
the metric perturbation δg_MN can be written δg_ab = f_ab S, δg_ai = r f_a S_i, δg_ij = 2r^2 (H_L γ_ij S + H_T S_ij)",
with "S_i = −(1/k) D̂_i S" and "S_ij = (1/k^2) D̂_i D̂_j S + (1/n) γ_ij S"; p. 4-5, "Note that the modes with k = 0 and
k^2 = nK require special treatment"; p. 5, "For modes with k^2(k^2 − nK) ≠ 0, the following combinations provide a basis
for gauge-invariant variables for metric perturbations of the scalar type: F = H_L + (1/n) H_T + (1/r) D^a r X_a (2.7a),
F_ab = f_ab + D_a X_b + D_b X_a (2.7b)", "X_a is given by X_a = (r/k)(f_a + (r/k) D_a H_T) (2.8)"; p. 13, section 5.1,
"H_T is gauge-invariant by itself". (Read 2026-11-02 through alphaXiv; the PDF text was extracted with broken spacing and
is quoted normalised.) The supplement: Part VIII (Theorem 2.2 (2.3), Corollary 2.3), Part IX (Lemmas 1.1-1.2, 2.1,
Corollary 2.3, Remark 2.4), III.B ((3.3), (3.6), Proposition 3.4, Lemma 3.7), III.D ((1.1), Propositions 6.1-6.2),
III.D$'$ ((1.1), (2.1), Lemmas 2.1, 3.1, Proposition 4.1 Step 1), II.C Definition 2.7, II.F$'$ Theorem 1.1, III.H$'$;
N1STAR-PROOF.md sections 10.3-10.4 (Propositions 10.1-10.2).

*Files.* `GAUGEDECAY5.md` (this note); `checks/rwgauge5.py` with `checks/rwgauge5.out`; `checks/hgauge5.py` with
`checks/hgauge5.out`.
