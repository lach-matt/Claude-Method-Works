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
  are $\dot g_{RW}+\dot\mu\,\mathcal L_{W^{**}_H}g+\mathcal L_{Z'}g$ with $\Box Z' = J$, $J$ supported in $l\ge2$ and
  decaying, and the $l = 0$ part of $Z'$ free ($\Box Z'_0 = 0$) (Proposition 2.1). A conserved horizon charge
  (Lemma 2.2, an exact identity) shows that when $\dot\mu\ne0$ **no** harmonic-gauge solution settles to $\dot\mu K$:
  the linear growth $\frac{\dot\mu}2\,v\,\mathcal L_{W^*}g$ is forced, with the explicit horizon-regular $W^{**}$
  (Theorem 2.3). Part III gives the frequency-domain counterpart (Proposition 2.5: a simple, rank-one pole of the
  unmodified 1-form resolvent at zero, range $W^*$, co-range the horizon functional). The time-domain decay of $Z'$
  modulo $W^*$ is **not** proved: the obstruction is stated in section 2.5.

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
  $|u|_k(v,r) := \sum_{j\le k}\sup_{S^3_{v,r}}|D^ju|$, $D$ ranging over $\partial_v$, $\partial_r$ and the Lie
  derivatives along the rotation fields $\Omega_{ij} = x^i\partial_j-x^j\partial_i$. On $\{r_0\le r\le R'\}$ these and
  $\partial_t,\partial_x$ span the same module
  with bounded coefficients, and $\partial_t$ costs a factor $t_*^{-1}$ against $t_*\partial_{t_*}$. So
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
(a) $\mathcal L_{\xi[h]}g$ has $a\theta$ components $-\partial_\theta\beta_a$, no $\phi$ components, and traceless
angular part $-(\hat D\hat D-\frac13\gamma\hat\Delta)\tau$ (R1, for arbitrary functions $\beta_a,\tau$ of
$(v,r,\theta)$; the control, with the weight $r^2\partial_a(\tau/r^2)$ replaced by $\partial_a\tau$, fails). So
$h+\mathcal L_{\xi[h]}g$ has $\beta = 0$, $\tau = 0$, the same $h^{\mathrm{TT}}$ and the same $l = 0$ part ($\xi$ has
none).
(b) For a scalar mode, $h_{ab} = f_{ab}S$, $h_{ai} = rf_aS_i$, $h_{ij} = 2r^2(H_L\gamma_{ij}S+H_TS_{ij})$ ([KI03] (2.4)-
(2.6)), $\beta_a = -\frac rkf_aS$, $\tau = 2r^2H_TS/k^2$, the orbit part of $\xi$ is $X_aS$ with [KI03]'s
$X_a = \frac rk(f_a+\frac rkD_aH_T)$ ((2.8)), and $h+\mathcal L_\xi g = F_{ab}S\,dy^ady^b+2r^2FS\gamma$ with [KI03]'s
invariants $F,F_{ab}$ ((2.7a)-(2.7b)) (R2, at $l = 2$ and $l = 4$, exact; control: $(r/k)^2$ replaced by $r/k^2$ in
$X_a$ fails). So the RW-type components are the gauge invariants, as supplement Proposition 10.1 (ii) states.
(c) *Uniqueness.* For a class 1-form $Z$ with no $l = 0$ part, $\xi[\mathcal L_Zg] = -Z$ (deduced from (a): with
$Z_\theta d\theta = d\eta$, $\langle\eta\rangle = 0$, $\mathcal L_Zg$ has $\beta_a = Z_a+r^2\partial_a(\eta/r^2)$, as
$\partial_aZ_\theta -\frac2r(\partial_ar)Z_\theta = \partial_\theta(r^2\partial_a(\eta/r^2))$, and $\tau = 2\eta$;
insert in (1.1)). In particular $\mathcal L_Zg$ has $\beta = \tau = 0$ only if $Z = 0$.

**Lemma 1.4 ($l = 0$: the linearised mass and Birkhoff; computed R4).** Let $h_0 =
A\,dv^2+2B\,dv\,dr+C\,dr^2+2r^2H\gamma$, functions of $(v,r)$, on a simply connected open subset $U$ of the orbit space.
(a) The linearisation of the five-dimensional Misner-Sharp mass $m = R^2(1-|dR|^2)$ ($m(g) = \mu_0$) is
$$\delta\mu[h_0] = 2\mu_0H+r^2(A+2fB+f^2C)-2r^2(\partial_v+f\partial_r)(rH).$$
It vanishes on $\mathcal L_Yg$ for every spherically symmetric $Y$, $\delta\mu[r^{-2}dv^2] = 1$, so $\delta\mu[K] = 1$ by
(0.1), and, with $\dot R := D\mathrm{Ric}(h_0)$,
$$\partial_v\delta\mu = \tfrac23r^3\big(\dot R_{vv}+f\dot R_{vr}\big),\qquad
\partial_r\delta\mu = \tfrac13r^3f\dot R_{rr}+r\dot R_{\theta\theta}$$
(R4 (a)-(d); control: without its term $2\mu_0H$ it is not gauge invariant).
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
$\dot\mu K$, inducing $(\dot\gamma,\dot k)$ plus the data of the linearised diffeomorphism
$\mathcal L_{X_{\mathrm{RW}}}g$.
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
(b) $\delta W^* = 0$, $(dW^*)_{vr} = 2r^{-3}$, $Q[W^*] = 4\pi^2$; the Killing 1-form $(\partial_v)^\flat = -f\,dv+dr$
has $Q = 4\pi^2\mu_0$ and $(\partial_v)^\flat-\mu_0W^*$ is closed; $\ell([\Box,v]W^*) = 4\pi^2$, III.D$'$ Lemma 3.1
(1)'s value; $\ell(\Theta(r^{-2}dv^2)) = -2\pi^2$, and by (0.1) $\ell(\Theta(K)) = -2\pi^2$ (H3; control: $W^*$ with its
$dr$ term reversed is not in the kernel of $\Box$). And $\frac d{dv}Q[W^{**}] = 2\pi^2$ (H4).

(2.1) is the time-domain form of III.D$'$ Lemma 2.1 (1)-(3): $\ell$ annihilates $\Box$ of every stationary form smooth at
the horizon (the case $\partial_v = 0$ of (2.1)) and spans the annihilator of the range at zero energy.

### 2.3 The forced linear growth

**Theorem 2.3 (deduced from Part VIII, Theorem 1.5, Lemmas 1.4 and 2.2).** Let $\dot g_H = \dot g+\mathcal L_Zg$ be a
harmonic-gauge solution of Proposition 2.1 ($Z = X_{\mathrm{RW}}+\dot\mu W^{**}_H+Z'$, $G$-invariant). Then on the
horizon, for $v\ge v_0$ ($t_*\ge T'$),
$$Q[Z](v) = Q[Z](v_0)+2\pi^2\dot\mu\,(v-v_0)-\int_{v_0}^v\ell(\Theta(h))\,dv'\ ,$$
$$|\ell(\Theta(h))|\le Cv^{-w+\epsilon'},$$
and $Q[Z-\dot\mu W^{**}_H](v)$ converges as $v\to\infty$. Consequently, if $\dot\mu\ne0$, no harmonic-gauge solution
settles to $\dot\mu K$ near the horizon at any integrable rate: there are no $\delta,\epsilon>0$ for which $(\dot
g_H-\dot\mu K)_0$ and its first derivatives are $O(t_*^{-1-\delta})$ on $\{|r-r_h|\le\epsilon\}$.

*Proof.* $\Box Z = \Theta(\mathcal L_Zg) = -\Theta(\dot g) = -\dot\mu\Theta(K)-\Theta(h)$, and $\ell(\Theta(K)) =
-2\pi^2$ (Lemma 2.2 (b)); $\ell(\Theta(h))$ involves $h$ and its first derivatives at $r_h$, bounded by (0.2). Integrate
(2.1). $\dot\mu W^{**}_H$ has $\frac d{dv}Q = 2\pi^2\dot\mu$ ($V = $ const$\cdot\partial_t$ near $r_h$, $Q[V^\flat]$
constant), so $Q[Z-\dot\mu W^{**}_H]$ has an integrable derivative. Now suppose $\dot\mu\ne0$ and $(\dot g_H-\dot\mu
K)_0 = O(t_*^{-1-\delta})$ with first derivatives near $r_h$. Then $\mathcal L_{Z_0}g = (\dot g_H-\dot\mu K)_0-h_0$ is
$O(t_*^{-\min(1+\delta,w-\epsilon')})$ there with first derivatives, and $\delta\mu$ of it vanishes (Lemma 1.4 (a)). By
Lemma 1.4 (b)-(c) (on a simply connected neighbourhood of the horizon's orbit), $Z_0 =
(\zeta\partial_v+rH\partial_r)^\flat +c'(\partial_v)^\flat$ with $d\zeta$, $H$, $dH$ integrable in $v$, so
$\zeta\to\zeta_\infty$. Since $(\zeta\partial_v)^\flat = \zeta(\partial_v)^\flat$ has $\delta = -\partial_v\zeta$ and
$(d\,\cdot)_{vr} = \partial_v\zeta+f\partial_r\zeta+\zeta f'$, $Q[(\zeta\partial_v)^\flat] = 4\pi^2\mu_0\zeta$ at $r_h$;
and $Q[(rH\partial_r)^\flat] = Q[rH\,dv]\to0$. So $Q[Z] = Q[Z_0]$ converges, against the growth $2\pi^2\dot\mu v$.
$\square$

*Remark 2.4 (the coefficient $\frac12$, and supplement Proposition 10.2 (iv)).* Horizon regularity fixes the coefficient:
if $cvW^*+U$, $U$ stationary and smooth at the horizon, solves $\Box(cvW^*+U) = -\Theta(r^{-2}dv^2)$, applying $\ell$
(which kills $\Box U$ and $v\Box W^*$) gives $4\pi^2c = 2\pi^2$, so $c = \frac12$ (deduced from Lemma 2.2 (b)).
Proposition 10.2 (iv)'s $W^{**} = tW^*+A\,dt+B\,dr$ has the coefficient 1 in the static time, but is built on the static
chart's mass change and has $A = (\log f+\mu/r^2)/(2\sqrt\mu)$ (READ, N1STAR-PROOF.md section 10.4), singular at the
horizon; the cokernel argument does not constrain it, and the two statements concern different representatives. The
horizon-regular one is $W^{**}$ above: the mass change in harmonic gauge grows as $\frac{\dot\mu}2v\,\mathcal L_{W^*}g$.

### 2.4 What Part III gives: the frequency domain

**Proposition 2.5 (deduced from III.D Propositions 6.1-6.2 and III.D$'$ Lemma 2.1 and Proposition 4.1, Step 1).** Let
$\hat P(\sigma)$ be the spectral family of the unmodified 1-form wave operator $\Box$ at $b_0$ (III.D$'$'s $\hat P$, the
parameter $\mathsf p_0$), on III.D$'$'s spaces $\mathcal X_\sigma\to\mathcal Y_\sigma$, $\mathcal X_0\to\mathcal Y_0$.
(i) $\hat P(\sigma)$ is invertible for every $\sigma\ne0$ with $\mathrm{Im}\,\sigma\ge0$ (III.D Proposition 6.2, "mode
stability of $\Box$ on Tangherlini away from zero", proved in `proof5/PART-III-D-GAUGEPOT.md` section 6, for
$\mathcal X_\sigma\to\mathcal Y_\sigma$; the high energies are its Proposition 6.1 at $\mathsf p_0$).
(ii) $\hat P(0)$ has index 0, kernel $\mathrm{span}\{W^*\}$, and the annihilator of its range is spanned by $\ell$
(III.D$'$ Lemma 2.1 (2)-(3)).
(iii) Near $\sigma = 0$, with the augmented operator $\mathcal P_0(\sigma)$ of III.D$'$ Proposition 4.1, Step 1
(invertible for $|\sigma|\le c_0$, $\mathrm{Im}\,\sigma\ge0$, with a uniform bound) and $(u_\sigma,c_\sigma) :=
\mathcal P_0(\sigma)^{-1}(0,1)$, $(w_\sigma,d_\sigma) := \mathcal P_0(\sigma)^{-1}(f,0)$:
$$\hat P(\sigma)^{-1}f = w_\sigma-\frac{d_\sigma}{c_\sigma}u_\sigma\ ,$$
$$c_\sigma\ell(\psi) = 4\pi^2i\sigma+o(|\sigma|),
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

**Corollary 2.6 (conditional; deduced).** Suppose (Adm$\Box$): every $G$-invariant $Z'$ on $N^{\mathcal D}$ with $\Box Z'
= J$, $J$ $G$-invariant with $J_0 = 0$ and $|J|_k\le Ct_*^{-w+\epsilon'}$ for every $k$ on compact $r$-sets (in whatever
weighted class at $\mathscr I^+$ the theorem needs), satisfies $|Z'-cW^*-c'(\partial_t)^\flat|_k\le C_kt_*^{-\kappa}$ on
each $\{r_0<r\le R'\}$ for some constants $c,c'$ and some $\kappa>0$. Then every harmonic-gauge solution of Proposition
2.1 is $\dot g_H = \dot\mu K^*+c\,\mathcal L_{W^*}g+O(t_*^{-\min(\kappa,w-\epsilon')})$ there, with a loss of
derivatives, and $4\pi^2(c+\mu_0c') = \lim_{v\to\infty}Q[Z-\dot\mu W^{**}_H]$. (Insert $Z'$ in Proposition 2.1 (a);
$\mathcal L_{(\partial_t)^\flat}g = 0$; the charge by Lemma 2.2 (b) and Theorem 2.3.) (Adm$\Box$) is what is open.

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
- (GD4) Part III gives the unmodified 1-form resolvent on the closed upper half plane: invertible off 0, a simple
  rank-one pole at 0 with range $W^*$ and co-range $\ell$ (Proposition 2.5). It does not give the time-domain decay of
  $Z'$ modulo $W^*$; the obstruction is section 2.5.

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

## Round 2

*Status.* Written (round 2, this section). Not verified by a second reader. Round 1 above is left as it stands; where
it is wrong this section says so (R2.0) and states the correction. New programs: `checks/admbox5.py` (B1-B8) and
`checks/gdrepair5.py` (V1-V5), with their `.out` files, every check with a negative control that fails. Section R2.V
folds in the independent verifier's reading of round 1 at commit 40398c5 and says, for each finding, what was wrong.
Labels as in round 1; "standard" marks a textbook fact used without a program.

*The result, in one paragraph.*
- **Round 1's (Adm$\Box$) is false as stated** (R2.0). $d\phi_2$, $d\phi_4$ below are $G$-invariant, smooth across the
  horizon, solve $\Box Z = 0$, and have stationary, nonzero, $\theta$-dependent $\mathcal L_Zg$. So Corollary 2.6's
  hypothesis fails already for $J = 0$, and its conclusion fails for harmonic-gauge solutions of Proposition 2.1 (a).
  Any decay statement must restrict the data of the gauge vector.
- **Obstruction (a) is closed at $b_0$** (R2.1-R2.2). The analogue of III.H-III.H$'$ for $\Box$ has one state ($W^*$),
  one column (from the cut-off state $\chi_KW^*$) and one row. III.H Proposition 3.2's $11\times11$ pairing matrix
  becomes the number $\ell([\Box,t_*]W^*) = 4\pi^2$. $\Box$ is 1-admissible with sf-loss 0, in the form III.H$'$ proves
  for $L_{b_0}$; the forward solution is a part of $K^+$-weight 0 plus $\beta(t_*,r)W^*$.
- **Decay modulo $W^*$, with its coefficient** (R2.3). For sources in the class of II.C Definition 2.7 (3), $u-c_f(t_*)
  W^* = O(t_*^{-1/2})$ on each compact $r$-set, where $c_f$ is the horizon charge $(4\pi^2)^{-1}\int^v\ell(f)$.
  Homogeneous solutions with compactly supported data settle to $(Q/4\pi^2)W^*$ at that rate. The rate $\frac12$ is what
  $L^2$ in time gives; nothing better is claimed.
- **Obstruction (c)** needs no separate argument (Corollary R2.8 covers $l = 0$); the explicit $l = 0$ reduction is Lemma
  R2.9.
- **Obstruction (b) is reduced, not closed** (R2.4). With the source cut off to a cone inside $\{\chi_K = 1\}$, in Part
  VIII's gauge it is $|x|^{-1}$ times an algebraic expression in $h$ plus a gauge-source term, and only $K^+$- and
  $\iota^+$-orders matter. Two inputs are not extracted here: the $\iota^+$-orders of $h'$ and of $D\vartheta_{\mathrm{
  tot}}(\vec p\,')$. Under that hypothesis (S$_K$), Theorem R2.12: a solution in harmonic gauge on
  $\{t_*\ge4,\ r\le t_*/8\}$ equals $\dot\mu K^*+c_\infty\mathcal L_{W^*}g+O(t_*^{-1/2})$ on each $\{r_0<r\le R'\}$,
  with $c_\infty$ a horizon charge; a gauge change by a homogeneous $Y_h$ with compactly supported data shifts
  $c_\infty$ by $Q[Y_h]/4\pi^2$ and changes nothing else.
- **The supplement's gauge-fixed mass change is singular at the horizon** (R2.V (M), the verifier's major finding,
  confirmed in V1). Supplement Proposition 10.2 (iv)'s $K^*$, built with the static time and the coefficient 1, has
  $K^*_{vr}\sim-\frac38(r-r_h)^{-1}$ and $K^*_{rr}\sim\frac38(r-r_h)^{-2}$ at $\mu_0 = 1$. So the paper's "regular at the
  horizon" and the final state of supplement 10.8 and 10.11 are wrong; replacement texts are in R2.S.
- **The spherically symmetric sector in harmonic gauge, corrected** (Proposition R2.13, unconditional given R2.5). It is
  exactly $\dot\mu K^*+\mathcal L_{Z'_0}g$ with $\Box Z'_0 = 0$, where $K^* = r^{-2}dv^2+\mathcal L_{W^{**}}g$ is the
  horizon-regular mass change with the $\frac v2$ term. For $Z'_0$ with compactly supported data it settles to
  $\dot\mu K^*+c\,\mathcal L_{W^*}g$ at the rate $t_*^{-1/2}$, $c = Q[Z'_0]/4\pi^2$. The linear growth is forced only for
  decaying gauge data: a stationary, horizon-regular harmonic-gauge mass change exists, but it is $O(1)$ at infinity
  (V2).

### R2.0 Correction to round 1: (Adm$\Box$) and Corollary 2.6

**Lemma R2.0 (computed B6).** $\phi_2 := (r^2-\frac{\mu_0}2)P_1(\cos2\theta)$ and $\phi_4 := (r^4-\mu_0r^2+
\frac{\mu_0^2}6)P_2(\cos2\theta)$ (the two lower coefficients of $\phi_4$ solved for) satisfy $\Box_0\phi = 0$. They are
polynomials in $r^2$, so smooth across the horizon in the ingoing chart, and $G$-invariant. $Z := d\phi$ has $\Box Z =
d\Box_0\phi = 0$ and $Q[Z] = 0$, and $\mathcal L_Zg = 2\nabla d\phi$ is stationary, nonzero and $\theta$-dependent.
(Control:
$r^2P_1(\cos2\theta)$, the mass term dropped, is not a solution.)

So round 1 is wrong at three places. The text above is not altered, for the verifier reading commit 40398c5.
- *Corollary 2.6's hypothesis (Adm$\Box$) is false.* $Z' = d\phi_2$ is $G$-invariant, solves $\Box Z' = J$ with $J = 0$
  (which meets every bound asked of $J$), and $Z'-cW^*-c'(\partial_t)^\flat$ does not tend to 0 on any $\{r_0<r\le R'\}$:
  its $l = 2$ part is stationary and nonzero, and $W^*$, $(\partial_t)^\flat$ are $l = 0$. Corollary 2.6 is vacuous as
  stated.
- *Its conclusion, and section 2.5's target, fail.* "Every harmonic-gauge solution ... equals $\dot\mu K^*+c\,\mathcal
  L_{W^*}g+O(t_*^{-\kappa})$" is false: by Proposition 2.1 (a) with $Z'+d\phi_2$, $\dot g_H+2\nabla d\phi_2$ is a
  harmonic-gauge solution with the same data up to a linearised diffeomorphism, and it differs from every
  $\dot\mu K^*+c\,\mathcal L_{W^*}g$ by a stationary $l = 2$ tensor.
- *The cause is the data at infinity.* $|d\phi_l|$ grows like $r^{l-1}$. For every even $l\ge2$ the stationary equation
  $(r^3f\phi_l')' = l(l+2)r\phi_l$ has a solution smooth at $r_h$ (indicial roots $0,0$ there); by the energy identity
  of III.D$'$ Lemma 2.1 (2)(c) it cannot decay, so it is the growing Frobenius branch. On III.D$'$'s decaying space
  $\mathcal X_0$ these are excluded, which is why the kernel there is $\mathrm{span}\{W^*\}$.

*The corrected target (Adm$\Box'$).* (i) The forward solution (zero data) of $\Box u = f$, $f$ in a stated weighted
class, is $cW^*+o(1)$ on compact $r$-sets with a rate. (ii) The same for homogeneous solutions with data in a stated
decaying class. $(\partial_t)^\flat$ occurs in neither, its data not decaying; as $\mathcal L_{(\partial_t)^\flat}g =
0$ it does not enter $\dot g_H$ anyway.

### R2.1 The augmented zero-energy operator of $\Box$ (III.H at $\Box$)

*Setting.* $b = b_0$ and the unmodified operator $\Box$, the parameter $\mathsf p_0$ of III.D$'$. III.D$'$ section 1:
$\hat P(\sigma)$ satisfies (H1)-(H5) with $\vartheta_{\mathcal H} = 1$, (G) for $\alpha+2\in(0,2)$, (TF), and has index
0 at $\sigma\ne0$. III.D Lemma 2.1 (1)-(3): $\Box = L_0+L_1\partial_{t_*}+L_2\partial_{t_*}^2$ with $L_0 = \hat P(0)\in
\rho^2\mathrm{Diff}^2_{\mathrm b}$, $L_1\in\rho\,\mathrm{Diff}^1_{\mathrm b}$ (equal to $[\Box,t_*]$ on stationary
sections) and $L_2 = -g^{00}\in\rho^2C^\infty$ near $\partial X$, which is what III.H section 1 asks of $L_b$; and
$\bar S = 0$, as III.D Lemma 3.1 gives $\bar S = \gamma_\Upsilon(\cdots)$ (READ, `PART-III-D-GAUGEPOT.md`:132) and
$\gamma_\Upsilon = 0$ here. Fix $\alpha$ with $\alpha+2\in(0,1)$ (III.H (1.1)), $s>\frac32$, $\chi_K$ of III.H (1.2), an
$SO(4)$-invariant fibre inner product $h$ and an $SO(4)$-invariant $\varphi\in C^\infty_c(X^\circ;E)$ with
$\langle W^*,\varphi\rangle_h = 1$ (average any choice over $SO(4)$). The state is $W^*$ of III.D$'$ (2.1): smooth on
$X$, in $\mathcal A^2$ (weight 2, as $\dot g(1,0)$ in III.H), $\Box W^* = 0$.

**Definition R2.1.** $f_* := \Box(\chi_KW^*) = [\Box,\chi_K]W^*$, $\hat f_*(\sigma) := \int e^{i\sigma t_*}f_*\,dt_*$,
$\hat g_*(\sigma) := i\sigma^{-1}\Psi(\sigma,\cdot)W^*$ with $\Psi$ of III.H Lemma 2.5, and
$$\tilde P(\sigma)(u,c) := \big(\hat P(\sigma)u+c\hat f_*(\sigma),\ \langle u,\varphi\rangle_h\big).$$

**Lemma R2.2 (III.H Lemmas 2.2-2.5 at $\Box$; computed B1-B2, deduced).** (a) $f_*$ is supported as in III.H Lemma 2.2
(a), and its part at $r\ge1$ obeys III.H (2.1): $|(t_*\partial_{t_*})^j(r\partial_r)^a\partial^\beta_\omega f_\infty|\le
Cr^{-4}$. (b) $\hat f_*(0) = L_1W^*+L_0w$, $w := -\kappa(r)W^*$ with $\kappa$ of III.H Lemma 2.3, so $w\in\mathcal A^1$
and $\hat f_*(0)\in\mathcal A^3$. (c) III.H Lemma 2.4 (a)-(d) hold for $\hat f_*$. (d) For $\sigma\ne0$,
$\mathrm{Im}\,\sigma\ge0$: $\hat g_*(\sigma)\in\mathcal X_\sigma$ and $\hat P(\sigma)\hat g_*(\sigma) = \hat
f_*(\sigma)$.

*Proof.* III.H's proofs use of their state only $L_bh = 0$, stationarity, its weight, and the structure of $L_0$,
$L_1$, $L_2$ near $\partial X$; at $\Box$ these are $\Box W^* = 0$, the weight 2 and the setting. The generalised state
$t_*h+\breve h$ does not occur. *Computed:* in the outgoing chart of III.B (3.4), (3.6) ($|x|\ge3R_1$), $\Box W^* = 0$,
$r^3L_1W^*\to-1$, $r^4L_2W^*\to16\mu_0$, $r^3L_0(rW^*)\to1$ in both orbit components, and $r^2g^{TT}\to-16\mu_0$ (B1;
control: in III.B's time $t$, $L_2W^*$ is only $O(r^{-2})$). On the cone $t_* = r/q$, $q\in[\frac14,\frac12]$,
$r^4[\Box,\chi]W^*$ has a finite limit and $r^3[\Box,\chi]W^*\to0$ for $\chi = (r/t_*)^2$ and $e^{r/t_*}$ (B2; control:
for the Killing form $(\partial_{t_*})^\flat$, weight 0, it is not $O(r^{-3})$). $\square$

**Proposition R2.3 (III.H Proposition 3.2 at $\Box$; computed B3, deduced).** $\tilde P(0):\mathcal X_0\oplus\mathbb
C\to\mathcal Y_0\oplus\mathbb C$, the spaces of III.H Proposition 3.2 at the weight $\alpha$, is invertible.

*Proof.* *Index 0.* $\tilde P(0)$ is a finite-rank perturbation of $\hat P(0)\oplus0$, and $\hat P(0):\mathcal
X_0\to\mathcal Y_0$ has index 0 (I.C Corollary 6.6, as in III.D$'$ Lemma 2.1 (3)); $\hat f_*(0)\in\mathcal
A^3\subset\mathcal Y_0$ as $\alpha+2<1$. *Injectivity.* Let $\tilde P(0)(u,c) = 0$. By Lemma R2.2 (b), $\hat
P(0)(u+cw)+cL_1W^* = 0$, and $u+cw\in\mathcal X_0$ ($\mathcal A^1\subset\bar H^{\infty,\alpha}_{\mathrm b}$ as
$\alpha<-1$). Apply $\ell$ of III.D$'$ (1.1). $\ell\circ\hat P(0) = 0$ on $\mathcal X_0$ (III.D$'$ Lemma 2.1 (1) and the
density argument of its (3); B3 checks $(\Box u)_v = 0$ at $r_h$ for stationary $l = 0$ $u$ with general coefficients,
and not at $2r_h$). And $\ell(L_1W^*) = \ell([\Box,t_*]W^*) = 4\pi^2$ (III.D$'$ Lemma 3.1 (1); B3 computes
$\ell([\Box,v+F(r)]W^*) = 4\pi^2$ for a general $F$, so for every $t_*$ with $t_*-v$ a function of $r$ near $r_h$, and
$\ell(L_1W^*+L_0(-\kappa W^*)) = 4\pi^2$ for a general $\kappa$). So $4\pi^2c = 0$, $c = 0$, $u\in\mathrm{span}\{W^*\}$
(III.D$'$ Lemma 2.1 (2)), and $\langle u,\varphi\rangle_h = 0$ gives $u = 0$. $\square$

III.H's block-triangular $11\times11$ matrix is here the $1\times1$ matrix $(4\pi^2)$. The time cut-off is what makes
it nonzero: a stationary column $\hat P(0)(\kappa W^*)$ is annihilated by $\ell$ (B3 control), and an augmentation by
it is not injective at zero energy.

**Theorem R2.4 (III.H Theorem 4.1 and Corollaries 4.2-4.3 at $\Box$; deduced).** There are $c_k>0$ and $C_k$ such that
for $\sigma\in\Sigma_0$, $|\sigma|\le c_k$: $\tilde P(\sigma):\mathcal X_\sigma\oplus\mathbb C\to\mathcal
Y_\sigma\oplus\mathbb C$ is invertible with the estimate III.H (4.5); III.H Theorem 4.1 (3) holds for $\tilde P$ on
$\Sigma_0\cap\mathbb R$; and, with $(u,c) := \tilde P(\sigma)^{-1}(f,0)$ for $0<|\sigma|\le c_0$,
$$\hat P(\sigma)^{-1}f = u+c\,\hat g_*(\sigma).\tag{R2.1}$$

*Proof.* III.H Theorem 4.1 is stated for any $\hat P$ with (H1)-(H4), (G), (TF) and index 0 at $\sigma\ne0$, which the
setting gives, and columns with (A1)-(A4), which Lemma R2.2 (c) gives with $\epsilon_0 = \frac14(1-(\alpha+2))$ exactly
as in III.H Corollary 4.2's proof; (Z$_{\mathcal P}$) is Proposition R2.3. $\hat P(\sigma)$ is invertible for every
$\sigma\ne0$ with $\mathrm{Im}\,\sigma\ge0$ (III.D Propositions 6.1-6.2), so III.H Corollary 4.3's scaling argument is
not
needed, and (R2.1) follows from Lemma R2.2 (d) as III.H (4.6) does. $\square$

### R2.2 The time domain: $\Box$ is 1-admissible (III.H$'$ at $\Box$)

$\mathcal O_c(\Box)$ is III.H$'$ Definition 1.1 with $P_0 = \Box$ and the $K^+$-weight $-1$ in place of $-2$.

**Theorem R2.5 (III.H$'$ Theorem 1.3 at $\Box$; deduced).** Let $\alpha_{\mathrm{sf}}+2\in(0,1)$, $k\in\mathbb N_0$,
$\mathsf s\in\mathcal O_c(\Box)$ and $f\in H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}(\Omega)^{\bullet,-}$. The
forward solution $u$ of $\Box u = f$ satisfies, with $C$ independent of $f$ and $\|f\|$ that norm:

(i) $u = u'+u_{\mathrm{sing}}$ with $\|u'\|_{H^{(\mathsf s;k),(\alpha_{\mathrm{sf}},0)}_{3b;b}(M_0)}\le C\|f\|$;

(ii) $u_{\mathrm{sing}} = \beta(t_*,r)W^*$, where for one function $B$ with $\sum_{j\le
k}\|(t\partial_t)^jB\|_{L^2(\mathbb
R)}\le C\|f\|$, $\partial_{t_*}\beta(\cdot,r) = (\partial_t\chi_K)(\cdot,r)*B$ and $\beta(\cdot,r)-\beta(\cdot,r') =
(\chi_K(\cdot,r)-\chi_K(\cdot,r'))*B$;

(iii) $\|u\|_{H^{(\mathsf s-1;k),(\alpha_{\mathrm{sf}},-1)}_{3b;b}(\Omega)^{\bullet,-}}\le C\|f\|$: $\Box$ is
1-admissible
with sf-weight $\alpha_{\mathrm{sf}}$, sf-loss 0 and margin 1 (II.C Definition 2.7 relaxed, orders in $\mathcal
O_c(\Box)$), at $b_0$ and for every $k$.

*Proof.* III.H$'$ sections 2-7 with $L_{b_0}$ replaced by $\Box$ and $\tilde L_b$ by $\tilde P$ (Theorem R2.4), the
states of III.H$'$ Lemma 5.1 reduced to the one of weight $q = 2$, and the two integrations of its section 7 (iv)-(v)
reduced to one. What III.H$'$ takes from $L_b$, at $\Box$:
- *Lemma 1.2 (orders).* With $\alpha_K = -1$ and margin 1, II.C Definition 2.4 (5)-(6) give $\mathsf
  s+\alpha_{\mathrm{sf}}+1>\frac12(-1+\vartheta_{\mathrm{in}})+1$ at the incoming radial set and $<\frac12(-1+
  \vartheta_{\mathrm{out}})-1\le-\frac32+\bar S$ at the outgoing one: inside the interval Lemma 1.2 (a) needs. (4)
  gives $s_c>\frac32+\vartheta_{\mathcal H} = \frac52$ (III.D Lemma 5.1).
- *Lemma 2.1.* High energies (I.B Theorem 1.3 (3); III.D Proposition 6.1), invertibility at every $\sigma\ne0$ (III.D
  Proposition 6.2), uniqueness of forward solutions (II.E Proposition 3.4).
- *Lemma 3.1.* I.B Theorem 1.3 (5) with $\delta_\Gamma(0)<\frac1{2(k+1)}$: III.D Lemma 5.2 gives $\delta_\Gamma(0)$ as
  small as wished at $b_0$, so $b_0\in\mathcal B^{\mathrm{hi}}_k$ for every $k$, as III.F Proposition 4.1 does for $L_b$.
- *Lemmas 4.1-4.2.* Theorem R2.4.
- *Lemma 5.1* with $q = 2$: $\partial_{t_*}u_{\mathrm{sing}}\in H^{(m;k),(\alpha_{\mathrm{sf}}+1,0)}_{3b;b}(M_0)$, as
  $\beta' = \alpha_{\mathrm{sf}}+1<0$.
- *Section 7.* (i) as there, with $u' := u_{\mathrm{hi}}+u_{\mathrm{reg}}$; (ii) $u_{\mathrm{sing}} = -u'$ on $\Omega_-$;
  then Lemma 6.2 once, for $u_{\mathrm{sing}}$ with the order $\mathsf s-1$, $\beta = \alpha_{\mathrm{sf}}+1$, $\ell =
  1$: the data $(\alpha_{\mathrm{sf}},0)\subset(\beta-1,-1)$ on $\Omega_-$ and $\partial_{t_*}u_{\mathrm{sing}}$ at
  $(\beta,-\ell+1)$ give $u_{\mathrm{sing}}\in H^{(\mathsf s-1;k),(\alpha_{\mathrm{sf}},-1)}_{3b;b}(M_0)$. This is (iii).

For (ii): by III.H$'$ Lemma 5.1's proof, $\mathcal F(\partial_{t_*}u_{\mathrm{sing}}) = \chi\Psi\hat b_1W^*$ on
$\mathbb R$, and $\Psi(\cdot,r)$ is the Fourier transform of $\partial_t\chi_K(\cdot,r)$ (III.H Lemma 2.5); $B :=
\mathcal F^{-1}(\chi\hat b_1)$ is bounded by III.H$'$ Lemma 4.2 and Plancherel, $\mathcal F(t\partial_tB) =
-(1+\sigma\partial_\sigma)\hat B$. Then $\beta(\cdot,r)-\beta(\cdot,r')-\psi*B$, $\psi :=
\chi_K(\cdot,r)-\chi_K(\cdot,r')
\in C^\infty_c([1,\max(2,4r,4r')])$, has zero $t_*$-derivative and is square integrable as $t_*\to-\infty$
($u_{\mathrm{sing}} = -u'$ there), so it vanishes. (i)-(ii) for general $f$ by density, $u'$ and $B$ extended by
continuity. $\square$

So round 1's obstruction (a) is closed in the form it was posed: II.C Definition 2.7 (3) holds for $\Box$ as III.H$'$
Theorem 1.3 proves it for $L_{b_0}$, with $\aleph = 1$ in place of 2. An application of II.F$'$ Theorem 1.1 to $\Box$
inherits III.H$'$'s obligation (H$'$7), orders in $\mathcal O_c$.

### R2.3 Decay modulo $W^*$: the coefficient is the horizon charge

**Lemma R2.6 (standard: Sobolev embedding on an interval, rescaled).** If $w,t\partial_tw\in L^2([\frac T2,4T];H)$ for
a Hilbert space $H$, then $\sup_{[T,2T]}\|w(t)\|_H^2\le C\,T^{-1}\int_{T/2}^{4T}(\|w\|_H^2+\|t\partial_tw\|_H^2)\,dt$,
$C$ absolute.

**Theorem R2.7 (deduced from Theorem R2.5, Lemma 2.2 and B4).** Let $k\ge1$, $j\ge0$, $R'>r_0$, and $\mathsf
s\in\mathcal O_c(\Box)$ with $\mathsf s\ge j+3$ over $\{r\le R'+1\}$ (such orders exist: II.C Definition 2.4 bounds
$\mathsf s$ above only near the outgoing radial set, which lies over sf, and the monotonicity runs toward it). Let $f\in
H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}(\Omega)^{\bullet,-}$, $u$ the forward solution of $\Box u = f$, and
$v_h(t_*)$ the value of $v$ at $(t_*,r_h)$. On $\{r_0<r\le R',\ t_*\ge4\max(R',1)\}$, with $j$ derivatives in $x$ and
$k-1$ of $t_*\partial_{t_*}$,
$$\big|u-c_f(t_*)W^*\big|\le C\,t_*^{-1/2}\|f\|,\qquad c_f(t_*) := \frac1{4\pi^2}\int_{-\infty}^{v_h(t_*)}\ell(f)(v')\,
dv',\tag{R2.2}$$
$\ell(f)(v) = r_h^3\int_{S^3}f(\partial_v)|_{(v,r_h)}d\omega$. In particular: (a) if $f$ has no $l = 0$ part,
$\ell(f) = 0$ and $u = O(t_*^{-1/2})$; (b) if $\int_v^\infty|\ell(f)|\le C'v^{-\kappa}$, then $u = c_\infty
W^*+O(t_*^{-\min(1/2,\kappa)})$, $c_\infty = (4\pi^2)^{-1}\int\ell(f)$.

*Proof.* (1) $Q[u](v) = 4\pi^2c_f$: (2.1) of Lemma 2.2 (deduced there for every 1-form) and $u = 0$ for $t_*<1$. (2)
$Q[u_{\mathrm{sing}}] = 4\pi^2(\beta-r_h\partial_r\beta)|_{r_h}$, $\partial_r$ at fixed $v$ (B4; control: without the
$\partial_r\beta$ term it fails). By Theorem R2.5 (ii), $\partial_r|_v\beta = \partial_r|_{t_*}\beta+(\partial_r
t_*)|_v\partial_{t_*}\beta$ is a convolution of $B$ with a kernel in $C^\infty_c$ ($\partial_r\chi_K$, $\partial_t
\chi_K$ at $r$ near $r_h$), and $|B(t)|\le Ct^{-1/2}\|f\|$ by Lemma R2.6 with $H = \mathbb C$. (3) $Q[u']$ involves
$u'$ and its first derivatives at $r_h$, so $|Q[u'](v)|\le C\|u'(t_*)\|_{H^2(K)}\le Ct_*^{-1/2}\|f\|$, $K$ a compact
neighbourhood of the horizon sphere, by Theorem R2.5 (i) (on compact $r$-sets its norm controls $t\partial_t$ and
$\mathsf
s\ge2$ derivatives in $L^2(dt\,dx)$) and Lemma R2.6. (4) Hence $4\pi^2\beta(t_*,r_h) = Q[u]-Q[u']+4\pi^2r_h\partial_r
\beta = 4\pi^2c_f+O(t_*^{-1/2}\|f\|)$, and for $r\le R'$, $\beta(t_*,r) = \beta(t_*,r_h)+(\psi*B)(t_*) =
c_f+O(t_*^{-1/2}\|f\|)$. (5) $u-c_fW^* = u'+(\beta-c_f)W^*$: the first term by Theorem R2.5 (i) and Lemma R2.6 in
$H^{j+3}\subset C^j$; the second with its derivatives, as $\partial_{t_*}\beta = \partial_t\chi_K*B$ and
$\partial_{t_*}c_f = \ell(f)/4\pi^2$ are $O(t_*^{-1/2})$ by Lemma R2.6, and the $r$-derivatives of $\beta$ are
convolutions of $B$ with $C^\infty_c$ kernels. For general $f$ both sides of (R2.2) depend continuously on $f$ on bounded
time intervals (Theorem R2.5 (iii); $\ell(f)\in L^2_{\mathrm{loc}}$), and $C^\infty_c(\Omega^\circ)$ is dense. (a):
$\ell$
sees only the $l = 0$ part (H2). $\square$

$c_f$ need not converge: $\ell(f)$ is only square integrable, and $c_fW^*$ is then the growth that the $K^+$-weight $-1$
of Theorem R2.5 (iii) allows. All of it is along $W^*$.

**Corollary R2.8 (homogeneous solutions with compactly supported data; deduced).** Let $Y$ be a smooth 1-form on
$\{t_*\ge t_0,\ r\ge r_0\}$ with $\Box Y = 0$ whose Cauchy data on $\{t_* = t_0\}$ have compact support. Then $Q[Y]$ is
constant, and on each $\{r_0<r\le R'\}$, $|Y-(Q[Y]/4\pi^2)W^*|\le Ct_*^{-1/2}$ with the derivatives of (R2.2).

*Proof.* With $\chi\in C^\infty(\mathbb R)$ equal to 0 near $(-\infty,t_0]$ and to 1 on $[t_0+1,\infty)$, $\chi(t_*)Y$ is
the forward solution of $[\Box,\chi(t_*)]Y$, which is smooth with compact support by finite speed of propagation
($\{r = r_0\}$ is spacelike, inside the horizon; the spaces of III.H$'$ are extendible there). So it lies in every class
of Theorem R2.7, and $(4\pi^2)^{-1}\int\ell([\Box,\chi]Y) = (4\pi^2)^{-1}Q[\chi Y]$ at late times $= Q[Y]/4\pi^2$, by
(2.1) and $\Box Y = 0$. Theorem R2.7 (b), $\kappa = \infty$. $\square$

By Lemma R2.0 the compact support, or some decay of the data, cannot be dropped.

**Lemma R2.9 ($l = 0$; computed B5).** For $Y = a\,dv+b\,dr$ ($a,b$ functions of $v,r$) put $\phi := \delta Y$ and $q :=
r^3(dY)_{vr}$. Then
$$(\Box Y)_v = \partial_v\phi+r^{-3}(\partial_vq+f\partial_rq),\qquad(\Box Y)_r = \partial_r\phi-r^{-3}\partial_rq.$$
So $\Box Y = 0$ iff $\partial_rq = r^3\partial_r\phi$ and $\partial_vq = -r^3(\partial_v\phi+f\partial_r\phi)$; their
integrability condition is $-r^3\Box_0\phi = 0$, the $l = 0$ scalar wave equation, and $q$ is then fixed up to a constant
by $\phi$. $Q[Y] = 2\pi^2(r_h^3\phi+q)|_{r_h}$. Stationary solutions smooth at the horizon and bounded: $W^*$ with
$(\phi,q) = (0,2)$, $(\partial_v)^\flat$ with $(0,2\mu_0)$, and $d\psi = \mu_0W^*-(\partial_v)^\flat$, $\psi = v+F$, $F'
=
-\frac{r^2+rr_h+r_h^2}{r(r+r_h)}$, $\Box_0\psi = 0$, with $(0,0)$; only $W^*$ decays (III.D$'$ Lemma 2.1 (2)). (Control:
$q$ with $r^2$ in place of $r^3$ does not reduce the equation.)

So round 1's obstruction (c) is settled for data with compact support by Corollary R2.8, without a separate radial
argument. At zero energy the radial ODE system is solved explicitly (III.D$'$ Lemma 2.1 (2) and B5); in time it reduces
to $l = 0$ scalar waves for $\phi$ and $\psi$ and a quadrature for $q$, and Corollary R2.8 gives what those reductions
would: $\phi\to0$, $q\to Q[Y]/2\pi^2$, $Y\to(Q[Y]/4\pi^2)W^*$.

### R2.4 The source: obstruction (b), reduced

**Lemma R2.10 (the gauge identity; computed B8, READ III.B (6.3)).** III.B Definition 6.1 (`PART-III-B-FAMILY.md`:
430-445) reads "$\Upsilon^0(g,g_0)_\mu := g_{\mu\nu}g^{\kappa\lambda}\big(\Gamma(g)^\nu_{\kappa\lambda}-\Gamma(g_0)^\nu_{
\kappa\lambda}\big)$, $\Upsilon^{E_\Upsilon}(g,g_0) := \Upsilon^0(g,g_0)-E^\Upsilon_{g_0}G_{g_0}(g-g_0)$" (6.3), with
"$c_\Upsilon = |x|^{-1}dt$ for large $|x|$" and "$E^\Upsilon_{g_0,\infty}h := -\gamma_\Upsilon\big(2\iota_{g_0^{-1}
c_\Upsilon}h-\tfrac23(1-e_\Upsilon)\,c_\Upsilon\,\mathrm{tr}_{g_0}h\big)$" (6.1), $E^\Upsilon_{g_0,H}$ compactly
supported.
The derivative of $\Upsilon^0(g+\epsilon k,g)$ at $\epsilon = 0$ is $-\Theta(k)$ (B8, for a general class tensor on
Tangherlini; control: without the $-g^{-1}k\Gamma$ term of $\dot\Gamma$ it fails). Hence $\dot\Upsilon :=
D_1\Upsilon^{E_\Upsilon}(g,g) = -\Theta-E^\Upsilon_gG_g$ and $D_2\Upsilon^{E_\Upsilon}(g,g) = -\dot\Upsilon$. Part VIII
Theorem 2.2 (5), $\dot\eta = 0$, then reads $\Theta(\dot g-\dot g_0) = -E^\Upsilon_gG_g(\dot g-\dot g_0)-D\vartheta_{
\mathrm{tot}}(\vec p\,')$. Where $\chi_K = 1$, $\dot g_0 = \dot\mu K$ (Part VIII Theorem 2.2's proof, Step 6:
"$g_{b_0,b,-S} = g_b$" there), so
$$J_h := -\Theta(h) = E^\Upsilon_gG_gh+D\vartheta_{\mathrm{tot}}(\vec p\,')\quad\text{on}\ \{\chi_K = 1\},\qquad h =
\dot g-\dot\mu K.\tag{R2.3}$$
No derivative of $h$ enters, and $E^\Upsilon_{g,\infty}$ carries the factor $|x|^{-1}$.

**Lemma R2.11 (cone sources; computed B7, deduced).** Let $F$ be supported in $\{t_*\ge2,\ r\le t_*/4\}$, smooth, with
$|(t_*\partial_{t_*})^i(r\partial_r)^a\partial^\beta_\omega F|\le C\,r^{-a_\iota}(r/t_*)^{b_K}$ on $r\ge1$ and $\le
Ct_*^{-b_K}$ on $r\le1$. If $b_K>\frac12$ and $a_\iota>\beta+\frac52$, then $F\in H^{(\mathsf s;k),(\beta,0)}_{3b;b}
(\Omega)^{\bullet,-}$ for every $\mathsf s$ and $k$.

*Proof.* On the cone $r\partial_{t_*} = (r/t_*)\,t_*\partial_{t_*}$ and $r\partial_x$ are b-vector fields with
coefficients bounded with all b-derivatives, so b-regularity gives every 3b-order. $\rho_{\mathrm{sf}} = r^{-1}$ and
$\rho_K\asymp r/t_*$ there, and $\int_1^\infty\int_{2r}^\infty r^{2\beta}r^{-2a_\iota}(r/t)^{2b_K}r^3\,dt\,dr<\infty$ iff
$b_K>\frac12$ and $a_\iota>\beta+\frac52$: after the $t$-integral the $r$-exponent is $2\beta-2a_\iota+4$ (B7; control:
$a_\iota = \beta+\frac52$ diverges). On $r\le1$, $t^{-b_K}$ is square integrable. $\square$

**Hypothesis (S$_K$).** There is $\beta\in(0,1)$ such that on $\{\chi_K = 1,\ t_*\ge T_0\}$, $h$ is conormal (in the
sense of Lemma R2.11) with $\iota^+$-order $>\frac32+\beta$ and $K^+$-order $>\frac12$, and $D\vartheta_{\mathrm{tot}}
(\vec p\,')$ with $\iota^+$-order $>\frac52+\beta$ and $K^+$-order $>\frac12$.

*What is known about (S$_K$).* $K^+$: $h$ has $K^+$-order $(\alpha-2)->2$ (Part VIII Theorem 2.2's proof, "The rate":
"$h'$ has $K^+$-order $\alpha-$, and $h_{b_0,\mathrm{rem}}(q')$ has $K^+$-order $(\alpha-2)-$"). $\iota^+$: III.I15 Lemma
2.2 (a) (`PART-III-I15-AUGMENT5.md`:147-150) says $h_{\mathrm{rem}}(q)$ is "at $\iota^+$ partially polyhomogeneous with
exponents in $\mathcal E_\sharp\cup\mathcal E^\natural$ to the order $(3+\eta_2)-$, of plain weight $\ge\lambda_\sharp$",
and "$\lambda_\sharp := \frac32+(1-e_\Upsilon)\gamma_\Upsilon$" (`PART-III-I6-ALMOSTBDD.md`:31). Read as an
$\iota^+$-order, $h_{\mathrm{rem}}$ meets (S$_K$) for $\beta<(1-e_\Upsilon)\gamma_\Upsilon$: the constraint damping
$\gamma_\Upsilon>0$ makes the room. *Not extracted here:* the $\iota^+$-order of $h'\in\mathcal X^\infty_{J,
\mathrm{ex}}$ (III.J$'''$ Proposition 5.4), and the $\iota^+$- and $K^+$-orders of $D\vartheta_{\mathrm{tot}}(\vec p\,')$
on $\{\chi_K = 1\}$. (S$_K$) is open, and on the cone it is all that obstruction (b) now consists of.

**Theorem R2.12 (the harmonic gauge near $K^+$; deduced, conditional on (S$_K$)).** Put $\chi' :=
\chi_+(t_*/2)\chi_c(2r/t_*)$ ($\chi_+$, $\chi_c$ of III.H (1.2)), so $\mathrm{supp}\,\chi'\subset\{\chi_K = 1\}$ and
$\chi' = 1$ on $\{t_*\ge4,\ r\le t_*/8\}$. Assume (S$_K$), and let $Y$ be the forward solution of $\Box Y = \chi'J_h$,
which lies in the class of Theorem R2.5 with $\alpha_{\mathrm{sf}}+2 = \beta$ by (R2.3) and Lemma R2.11, and
$\dot g_H := \dot g+\mathcal L_{\dot\mu W^{**}_H+Y}g$. Then:

(i) $\dot g_H$ is $G$-invariant, $D\mathrm{Ric}(\dot g_H) = 0$, and it induces $(\dot\gamma,\dot k)$ up to the data of
the
linearised diffeomorphism $\mathcal L_{\dot\mu W^{**}_H}g$ ($Y$ vanishes for $t_*<2$);

(ii) $\Theta(\dot g_H) = (1-\chi')\Theta(h)$, so $\dot g_H$ is in harmonic gauge on $\{t_*\ge4,\ r\le t_*/8\}$;

(iii) on each $\{r_0<r\le R',\ t_*\ge T'\}$, with the derivatives of (R2.2),
$$\big|\dot g_H-\dot\mu K^*-c_\infty\mathcal L_{W^*}g\big|\le Ct_*^{-1/2},\qquad c_\infty =
-\frac1{4\pi^2}\int\ell\big(\chi'\Theta(h)\big)\,dv,$$
where $K^*-\frac v2\mathcal L_{W^*}g$ is stationary and smooth across the horizon (Proposition 2.1 (d)), and $C$ is
bounded by the data norms of Part VIII and the constants of (S$_K$);

(iv) for every 1-form $Y_h$ with $\Box Y_h = 0$ and compactly supported data, $\dot g_H+\mathcal L_{Y_h}g$ has (i)-(ii),
and (iii) with $c_\infty+Q[Y_h]/4\pi^2$;

(v) (iii) fails without a restriction on the data of $Y_h$ (Lemma R2.0), and with non-decaying data the linear growth
itself can be removed at the price of a term that does not decay at infinity (Proposition R2.13 (c)).

*Proof.* (ii): $\Theta(\dot g)+\dot\mu\Box W^{**}_H = \Theta(\dot g)-\dot\mu\Theta(K) = \Theta(h)$ (Proposition 2.1 (d)),
and $\Box Y = -\chi'\Theta(h)$. (iii): $\dot g_H-\dot\mu K^* = h+\mathcal L_Yg$. Theorem R2.7 gives $|Y-c(t_*)W^*|\le
Ct_*^{-1/2}$ with one more derivative, $c(t_*) = -(4\pi^2)^{-1}\int^{v_h(t_*)}\ell(\chi'\Theta(h))$. For $t_*\ge8r_h$,
$\chi' = 1$ near the horizon, and $|\ell(\Theta(h))|\le Cv^{-w+\epsilon'}$ (Theorem 2.3), so $c-c_\infty$ and $\partial
c$ are $O(t_*^{-(w-1)+\epsilon'})$; $\mathcal L_{cW^*}g = c\,\mathcal L_{W^*}g+2\,dc\otimes_sW^*$. With $|h|_k =
O(t_*^{-w+\epsilon'})$ ((0.2)) and $w-1>1$, the slowest term is $t_*^{-1/2}$. (iv): Corollary R2.8, $\mathcal L_{Y_h}g$
being linear in $Y_h$. (i): every ingredient is $G$-equivariant, and the forward solution is unique. $\square$

So the harmonic-gauge statement that is proved, given (S$_K$), is: near $K^+$, on every compact $r$-set at late times,
the solution is the explicit $\dot\mu K^* = \frac{\dot\mu}2v\,\mathcal L_{W^*}g+(\text{stationary})$, plus the stationary
$c_\infty\mathcal L_{W^*}g$ with $c_\infty$ a horizon charge, plus $O(t_*^{-1/2})$; and a gauge change with compactly
supported data only moves $c_\infty$, by $Q[Y_h]/4\pi^2$. Theorem 2.3 forces the growth; Theorem R2.12 settles the rest.

### R2.V The verifier's reading of round 1 (commit 40398c5): what was wrong

An independent verifier read round 1 and confirmed Theorem 1.5, the charge identity of Lemma 2.2, Theorem 2.3, Remark
2.4 and Proposition 2.5 (as a deduction). Its findings follow, each with what was wrong and the repair; the computations
are `checks/gdrepair5.py` V1-V5. Round 1's text is left as the verifier read it.

**(M) Major: the supplement's $K^*$ is singular at the horizon, and round 1 said so too softly.** Supplement Proposition
10.2 (iv) (READ, `N1STAR-PROOF.md`:1780-1782) takes "$K := dg/d\mu$" of the static chart and "$K^* := K+\pi_{W^{**}}$
with $W^{**} = tW^*+A\,dt+B\,dr$, $A = (\log f+\mu/r^2)/(2\sqrt\mu)$": the coefficient of the static time is 1. Written
in
the ingoing chart, its $\Gamma[K^*] = 0$ holds, but at $\mu_0 = 1$, $(r-r_h)K^*_{vr}\to-\frac38$ and $(r-r_h)^2K^*_{rr}
\to\frac38$ as $r\to r_h^+$, the verifier's values (V1). The difference from the horizon-regular $K^* = r^{-2}dv^2+
\mathcal L_{W^{**}}g$ of Proposition 2.1 (d) is $\frac v2\mathcal L_{W^*}g$ plus a stationary tensor with a double pole
at $r_h$ (V1). *What was wrong in round 1:* Remark 2.4 (lines 300-303) called the two "different representatives", and
the close of section 2.5 (lines 365-368) said the paper's route "keeps its status as a deduction". Both understate it.
Plainly:
- the supplement's $K^*$ is not smooth across the horizon, so it is the final state of no perturbation that is;
- the paper's clause "the $l = 0$ sector's two non-decaying solutions are explicit and regular at the horizon" (READ,
  `paper/RESPONSE-HL-5D.md`:797-798) is false for $K^*$ (it holds for $W^*$);
- supplement 10.8 (`N1STAR-PROOF.md`:2436-2440 and 2854-2856) and 10.11 (2919-2920) write $h_0 = cK^*+\pi_{W'}$ with
  $W'$ regular and conclude that $h_0$ settles to $cK^*+c_1(\infty)\pi_{W^*}$. With that $K^*$, $h_0$ smooth and $c\ne0$,
  $\pi_{W'} = h_0-cK^*$ is singular at $r_h$, so $W'$ is not regular: the decomposition fails, and the stated final
  state is wrong.

The corrected final state is Proposition R2.13; replacement texts are in R2.S.

**(m1) The Part IX dependence was understated (round 1 lines 390-392).** The labels said that Theorem 1.5 (a)-(c) rest on
Part VIII and this note, and that only Theorem 1.5 (d) and Proposition 2.1 (b) use Part IX. In fact Theorem 1.5 (a) uses
Part IX (IX1) (the region $N$; line 52) and Part IX Lemma 2.1 (b) ($D\mathrm{Ric}(\mathcal L_Xg) = 0$; lines 177-178),
and Proposition 2.1 (a) uses Part IX Lemmas 1.1-1.2 ($N^{\mathcal D}$, its global hyperbolicity and the Cauchy problem
for
$P = \Box$; lines 213, 224, 242-243). These Part IX inputs are labelled verified. Round 2 inherits them through
Proposition 2.1.

**(m2) "Forced" was claimed at the metric level (round 1 lines 26, 366, 381).** The summary, the close of section 2.5 and
(GD3) say the linear growth $\frac{\dot\mu}2v\,\mathcal L_{W^*}g$ is forced. Theorem 2.3 proves a statement about the
gauge vector: the horizon charge $Q[Z]$ grows like $2\pi^2\dot\mu v$, so no harmonic-gauge solution settles to
$\dot\mu K$ near the horizon at an integrable rate. At the metric level round 1 had the growth only through Corollary
2.6, which is conditional, and vacuous as stated (R2.0). Corrected: Proposition R2.13. At the metric level the growth is
forced in the $l = 0$ sector when the gauge vector's $l = 0$ part has compactly supported data, and it can be removed
when the data do not decay.

**(n1) Proposition 2.5 did not cite (Dyn).** III.D and III.D$'$ assume (Dyn) (Part VI.A). Proposition 2.5, and
everything in round 2 that uses III.D or III.D$'$ (R2.1-R2.5, R2.7-R2.8, R2.12, R2.13 (b)), assume it as those parts do.

**(n2) "Every check with a failing control" was not true (round 1 line 389).** R3 (c)-(f), H2's $l = 2$ item and H3's
values of $Q$ and $\ell$ had no control, and R5's control (`rwgauge5.py`:456-459, "$Y$ decays like $\mathcal L_Yg$"
for the same $Y$) is tautological. Controls are supplied in V4, each a claim that fails:
- R3c: off the class, $\cos^2\theta\,d\phi_1$ is divergence-free and not closed, so "divergence-free implies exact"
  fails;
- R3d: a $(\theta,\phi_1)$ component gives a $\phi_1$ divergence;
- R3e: $(k^2-2)$ in place of $(k^2-3)$ fails at 40 digits;
- R3f: with $k^2(k^2-2)$ the supremum is not $\frac{243}{80}$;
- H2: $Q$ of a general $l = 0$ class 1-form is not 0;
- H3: $Q[W^*+(\partial_v)^\flat] = 4\pi^2(1+\mu_0)$ and $\ell([\Box,v](\partial_v)^\flat) = 4\pi^2\mu_0$, so the values
  discriminate;
- R5: for $Y = (1+v)^{-q}r\partial_r$, $\mathcal L_Yg$ is only $O(v^{-q})$, so the loss of one power is particular to
  $\partial_v$.

**(n3) H4's $r$-component was numerical (`hgauge5.py`:21, 29, 173-178).** It is exact: after
`expand_log(force=True)` every component of $\Box W^{**}-r^{-3}dv$ vanishes identically (V3; control: the coefficient
1). `hgauge5.py` is left as the verifier read it.

**(n4) Definition 1.1 and supplement Proposition 10.1 agree at $l\ge2$ only (round 1 lines 83-84).** Definition 1.1
fixes the $l = 0$ part to $cK$ with $K$ of (0.1), which is smooth across the horizon. Proposition 10.1 uses the static
$K_{\mathrm{st}} = r^{-2}dt^2+r^{-2}f^{-2}dr^2 = r^{-2}dv^2+\mathcal L_{\zeta\partial_v}g$, $\zeta' = (r^2f^2)^{-1}$,
which
has a double pole at $r_h$ (V5). So the two gauges coincide for $l\ge2$; at $l = 0$, Proposition 10.1's is singular at
the horizon. Theorem 1.5's "with $l = 0$ part exactly $\dot\mu K$" refers to (0.1)'s $K$.

**Proposition R2.13 (the spherically symmetric sector in harmonic gauge; deduced; computed H4, B5, V1-V2).** Let $\dot
g_H$ be a harmonic-gauge solution of Proposition 2.1 (a), with gauge vector $Z'$.

(a) *Exact form.* $(\dot g_H)_0 = \dot\mu K^*+\mathcal L_{Z'_0}g$, where $Z'_0$ is the $l = 0$ part of $Z'$, $\Box Z'_0 =
0$, and $K^* := K+\mathcal L_{W^{**}_H}g$, which equals $r^{-2}dv^2+\mathcal L_{W^{**}}g$ (by (0.1)), with
$$W^{**} = \tfrac v2W^*+A\,dv+B\,dr,\qquad A = \frac{r_h^2+2r^2\log\frac{r+r_h}r}{4r_hr^2},\qquad B =
\frac{r^2r_h-3rr_h^2+2r_h^3+2r^3\log r+2(r_h^3-r^3)\log(r+r_h)-2r_h^3\log r_h}{4rr_h(r^2-r_h^2)}.$$
$K^*$ is smooth across the horizon, $\Theta(K^*) = 0$, $\delta\mu[K^*] = 1$, and $K^*-\frac v2\mathcal L_{W^*}g$ is
stationary (H4, V2 (a)). The choice $Z'_0 = 0$ is allowed, and then $(\dot g_H)_0 = \dot\mu K^*$ identically.

(b) *Decaying gauge data.* If $Z'_0$ has compactly supported Cauchy data, then on each $\{r_0<r\le R'\}$, with the
derivatives of (R2.2),
$$(\dot g_H)_0 = \dot\mu K^*+c\,\mathcal L_{W^*}g+O(t_*^{-1/2}),\qquad c = Q[Z'_0]/4\pi^2.$$
When $\dot\mu\ne0$ this grows linearly in $v$ and is not (stationary, smooth at $r_h$) $+\,o(1)$.

(c) *Non-decaying gauge data.* Without decay the growth can be removed. Let $\Psi := (v+F)^2+K_\Psi$ with $F = -r-
r_h\log\frac r{r+r_h}$ and $K_\Psi' = \big(\frac{r^4}2+r^2r_h^2-\frac32r_h^4+2r_h^4\log\frac r{r_h}\big)/(r(r^2-r_h^2))$.
Then $\Box_0\Psi = 0$, $d\Psi$ is smooth across $r_h$, and $S := K^*-(4\mu_0)^{-1}\mathcal L_{d\Psi}g$ is stationary,
smooth across the horizon, $\Theta(S) = 0$, $\delta\mu[S] = 1$; but $S_{vv}\to-1/\mu_0$ as $r\to\infty$ (V2). So
$\dot\mu S$ is the $l = 0$ part of a harmonic-gauge solution, with $Z'_0 = -\frac{\dot\mu}{4\mu_0}d\Psi$, that is
stationary near the horizon, not decaying at infinity, and whose gauge vector grows in $v$ and $r$. The growth of
$Q[Z]$ (Theorem 2.3) is then carried by $\frac{\dot\mu}{2\mu_0}v(\partial_v)^\flat$, a linearly growing time translation,
whose Lie derivative is stationary.

*Proof.* (a): $(\dot g_{\mathrm{RW}})_0 = \dot\mu K$ (Theorem 1.5 (a)), $W^{**}_H$ is radial, and Proposition 2.1 (c)
gives $\Box Z'_0 = 0$; $K = r^{-2}dv^2+\mathcal L_Vg$ (0.1) and $W^{**}_H = W^{**}-V^\flat$ (section 2.1).
$\delta\mu[\mathcal L_Yg] = 0$ for radial $Y$ (Lemma 1.4 (a)). (b): Corollary R2.8 for $Z'_0$, and $\mathcal
L_{Z'_0}g-c\,\mathcal L_{W^*}g = \mathcal L_{Z'_0-cW^*}g$. (c): V2. By B5, $d\psi = \mu_0W^*-(\partial_v)^\flat$ for
$\psi = v+F$, and $d\Psi = 2(v+F)\,d\psi+K_\Psi'\,dr$; so $-\frac{\dot\mu}{4\mu_0}d\Psi$ has the growing part
$-\frac{\dot\mu}2vW^*+\frac{\dot\mu}{2\mu_0}v(\partial_v)^\flat$. The first cancels the growing part of $\dot\mu W^{**}$;
$Q[d\Psi] = 0$ ($\delta d\Psi = \Box_0\Psi = 0$ and $d\,d\Psi = 0$). $\square$

So "the growth is forced" holds for perturbations whose gauge vector decays at infinity, and only for them. A statement
of the final state must carry that class.

### R2.S Replacement texts for the supplement and the paper

These replace the passages named; each is a statement of what is proved or deduced here, with its label.

*(S1) Supplement Proposition 10.2 (iv), from "The mass change" (`N1STAR-PROOF.md`:1780) to "(conditional, D45)." (1786):*

> The mass change. In the ingoing chart ($v = t+r_*$, $g = -f\,dv^2+2\,dv\,dr+r^2\gamma$) the mass derivative is $K :=
> r^{-2}dv^2$, smooth across the horizon, with $\Gamma[K] = r^{-3}dv$. The static chart's $dg/d\mu = r^{-2}dt^2+
> r^{-2}f^{-2}dr^2$ equals $K+\pi_{\zeta\partial_v}$ with $\zeta' = (r^2f^2)^{-1}$, singular at $r_h$. Put $W^{**} :=
> \frac v2W^*+A\,dv+B\,dr$, $r_h = \sqrt\mu$,
> $$A = \frac{r_h^2+2r^2\log\frac{r+r_h}r}{4r_hr^2},\qquad B = \frac{r^2r_h-3rr_h^2+2r_h^3+2r^3\log r+2(r_h^3-r^3)
> \log(r+r_h)-2r_h^3\log r_h}{4rr_h(r^2-r_h^2)},$$
> analytic on $r>0$ including $r = r_h$, where the numerator of $B$ vanishes. Then $K^* := K+\pi_{W^{**}}$ satisfies
> $\Gamma[K^*] = 0$, is smooth across the horizon, has linearised mass 1, and $K^* = \frac v2\pi_{W^*}+(\text{stationary,
> smooth across }r_h)$: the counterparts of [Hun19] (8.1) and (8.39). The
> coefficient $\frac12$ of $v$ is forced by regularity at the horizon among gauge vectors $cvW^*+U$, $U$ stationary and
> smooth at $r_h$: the horizon functional annihilates $\Box U$ and gives $4\pi^2c = 2\pi^2$. The representative $tW^*+
> A_{\mathrm{st}}\,dt+B_{\mathrm{st}}\,dr$ with the coefficient 1 of the static time gives a $K^*$ singular at $r_h$ (at
> $\mu = 1$, $(r-r_h)K^*_{vr}\to-\frac38$ and $(r-r_h)^2K^*_{rr}\to\frac38$). In harmonic gauge the $l = 0$ part of a
> perturbation in the class is $\dot\mu K^*+\pi_Z$ with $\Box Z = 0$. When $Z$ has compactly supported data it settles to
> $\dot\mu K^*+c\,\pi_{W^*}$ on each $\{r\le R\}$ at the rate $t_*^{-1/2}$, with $c$ the conserved horizon charge of $Z$
> divided by that of $W^*$ (deduced, GAUGEDECAY5 Proposition R2.13 (b), assuming (Dyn)); the mass change grows linearly
> in $v$, as in four dimensions. Without decay of $Z$'s data at infinity the growth can be exchanged for a stationary
> term that does not decay at infinity (R2.13 (c)).

*(S2) Supplement 10.8, its first sentence (`N1STAR-PROOF.md`:2436-2438), to "(Proposition 10.2(i), (iv))":*

> The $l = 0$ part of a perturbation in the class is $h_0 = cK+\pi_W$, $K = r^{-2}dv^2$ the horizon-regular mass change
> of Proposition 10.2 (iv) (Proposition 10.1 (i)'s static $K$ differs from it by $\pi_{\zeta\partial_v}$, $\zeta' =
> (r^2f^2)^{-1}$, singular at $r_h$), and in harmonic gauge $h_0 = cK^*+\pi_{W'}$ with $\Box W' = 0$ and $W'$ smooth
> across the horizon, $K^*$ the horizon-regular gauge-fixed mass change of Proposition 10.2 (iv), since $\Gamma[K^*] = 0$
> and $\Gamma[\pi_{W'}] = \Box W'$. With the static-time $K^*$ (coefficient 1) this decomposition fails for $c\ne0$:
> $\pi_{W'} = h_0-cK^*$ would be singular at $r_h$.

*(S3) Supplement 10.8 (iii) (`N1STAR-PROOF.md`:2856) and 10.11 (2919-2920), the final state:*

> ... so $h_0$ settles to $cK^*+c_1(\infty)\pi_{W^*}$, with $K^* = K+\pi_{W^{**}}$, $W^{**} = \frac v2W^*+A\,dv+B\,dr$,
> the horizon-regular gauge-fixed mass change of Proposition 10.2 (iv), and $c_1(\infty) = Q[W']/Q[W^*]$, the conserved
> horizon charges. $cK^*$ grows like $\frac c2v\,\pi_{W^*}$. For $W'$ with compactly supported data this is proved at the
> rate $t_*^{-1/2}$ on each $\{r\le R\}$ (GAUGEDECAY5 Proposition R2.13 (b), deduced, assuming (Dyn)); the rate here
> remains a deduction. Without decay of $W'$'s data at infinity the final state is not unique (R2.13 (c)).

*(S4) The paper, section 8.2 (`paper/RESPONSE-HL-5D.md`:797-798), the clause "and the l = 0 sector's two non-decaying
solutions are explicit and regular at the horizon;":*

> and the $l = 0$ sector's two non-decaying solutions are explicit and regular at the horizon: the stationary one-form
> $W^*$, and the gauge-fixed mass change $K^* = K+\pi_{W^{**}}$ with $W^{**} = \frac v2W^*+A\,dv+B\,dr$, $v$ the
> ingoing time, whose coefficient $\frac12$ is forced by regularity at the horizon (with the static time and the
> coefficient 1, $K^*$ is singular there). In harmonic gauge the spherically symmetric part of a perturbation whose
> gauge vector has compactly supported data settles on each region $r\le R$ to $\dot\mu K^*+c\,\pi_{W^*}$, growing
> linearly in $v$, at the rate $\tau^{-1/2}$ (deduced from the zero-energy structure of the 1-form wave operator,
> supplement GAUGEDECAY5 R2.13); without decay of the gauge vector's data the growth can be traded for a stationary term
> that does not decay at infinity;

### R2.5 What is not proved, and why

1. *(S$_K$).* The $\iota^+$-orders of $h'$ (III.J$'''$'s class) and of $D\vartheta_{\mathrm{tot}}(\vec p\,')$ on
   $\{\chi_K = 1\}$; $h_{\mathrm{rem}}$'s is enough for $\beta<(1-e_\Upsilon)\gamma_\Upsilon$.
2. *The harmonic gauge on all of $N$, not only on the cone.* It needs $J_h$ at $\mathscr I^+$ in II.F$'$ (1.4)'s
   b-class (by (R2.3), $J_h$ is $|x|^{-1}$ times a radiation field there), II.F$'$ Theorem 1.1 for $P = P_0 = \Box$
   (whose hypothesis Theorem R2.5 (iii) supplies, with (H$'$7)), and the cone localisation of the forward solution
   ($\chi_Ku$ solves a problem with cone-supported source $\chi_Kf+[\Box,\chi_K]u$). The $\mathscr I^+$- and
   $\iota^+$-weights of $\dot g$ in III.J$'''$'s classes are not extracted here.
3. *A rate better than $t_*^{-1/2}$.* Theorem R2.5 (i) is $L^2$ in time at $K^+$-weight 0, which is all III.H$'$'s
   argument gives; a faster rate needs the $K^+$ expansion of the resolvent at zero energy, the analogue of III.I for
   $\Box$.
4. *A second reading* of the transposition R2.2-R2.5.

### R2.6 Findings, labels and files (round 2)

*Findings.*
- (GD5) Round 1's (Adm$\Box$) and Corollary 2.6 are false as stated (R2.0): $d\phi_2$, $d\phi_4$ are $G$-invariant
  homogeneous solutions with non-decaying data and stationary $l\ge2$ Lie derivatives. A decay statement must restrict
  the data of the gauge vector.
- (GD6) At $b_0$, $\Box$ has III.H's structure with one state and one column; $\tilde P(0)$ is invertible because
  $\ell([\Box,t_*]W^*) = 4\pi^2\ne0$, and $\Box$ is 1-admissible with sf-loss 0 (R2.3-R2.5). Obstruction (a) is closed as
  posed.
- (GD7) Forward solutions with sources in that class settle modulo $W^*$ at the rate $t_*^{-1/2}$ on compact $r$-sets,
  with the coefficient of $W^*$ the horizon charge $(4\pi^2)^{-1}\int\ell(f)$ (R2.7). Homogeneous solutions with
  compactly
  supported data settle to $(Q/4\pi^2)W^*$ (R2.8), the $l = 0$ sector included (R2.9): obstruction (c).
- (GD9) The supplement's $K^*$ (Proposition 10.2 (iv), static time, coefficient 1) is singular at the horizon (V1);
  the horizon-regular one has the coefficient $\frac12$ of $v$. In harmonic gauge the spherically symmetric sector is
  exactly $\dot\mu K^*+\mathcal L_{Z'_0}g$, $\Box Z'_0 = 0$. It settles to $\dot\mu K^*+c\,\mathcal L_{W^*}g$,
  $c = Q[Z'_0]/4\pi^2$, when $Z'_0$ has compactly supported data. Without decay a stationary horizon-regular
  harmonic-gauge mass change exists that is $O(1)$ at infinity (R2.13). Replacement texts: R2.S.
- (GD10) Round 1's Part IX dependence, its "forced" growth, its control claim, H4's numerical component and its
  identification of Definition 1.1 with Proposition 10.1 at $l = 0$ are corrected in R2.V.
- (GD8) On the cone, obstruction (b) is reduced to (S$_K$). In Part VIII's gauge the source is zeroth order in $h$ with a
  $|x|^{-1}$ coefficient (R2.10), and $h_{\mathrm{rem}}$'s $\iota^+$-weight $\lambda_\sharp$ suffices. Given (S$_K$) the
  harmonic gauge settles near $K^+$ to $\dot\mu K^*+c_\infty\mathcal L_{W^*}g$ at the rate $t_*^{-1/2}$ (R2.12).

*Labels.* Computed: `checks/admbox5.py` B1-B8 and `checks/gdrepair5.py` V1-V5 (exact, sympy; V4's R3e by
quadrature at 40 digits; each with a failing control). Deduced: Lemma R2.2,
Proposition R2.3, Theorems R2.4, R2.5, R2.7, Corollary R2.8, Lemmas R2.10 (with B8) and R2.11 (with B7), and Theorem
R2.12, which is conditional on (S$_K$), and Proposition R2.13 ((b) through Corollary R2.8; all of R2.1-R2.13 that
uses III.D or III.D$'$ assumes (Dyn), as those parts do). READ: III.B (6.1), (6.3) (`PART-III-B-FAMILY.md`:430-445),
III.I15 Lemma 2.2
(a) (`PART-III-I15-AUGMENT5.md`:147-150), $\lambda_\sharp$ (`PART-III-I6-ALMOSTBDD.md`:31), $\bar S$
(`PART-III-D-GAUGEPOT.md`:132), supplement Proposition 10.2 (iv) (`N1STAR-PROOF.md`:1780-1782), 10.8 (2436-2440,
2854-2856), 10.11 (2919-2920), the paper (`paper/RESPONSE-HL-5D.md`:797-798). Standard: Lemma R2.6. Nothing conjectural
is stated as proved; open: section R2.5.

*Files.* `GAUGEDECAY5.md` (this section appended); `checks/admbox5.py` with `checks/admbox5.out`;
`checks/gdrepair5.py` with `checks/gdrepair5.out`.

## Round 3

*Status.* Written 2026-11-02 (round 3, this section). Not verified by a second reader. Rounds 1 and 2 are left as they
stand; where round 3 changes them it says so here, as amendments (A1)-(A8). New programs: `checks/gdix5.py` (P1),
`checks/gdsk5.py` (K1-K5) and `checks/gdscri5.py` (S1-S8), with their `.out` files; every check has a control that
must fail, and fails. Labels as in rounds 1-2. Readings of the supplement's Parts are READ with file:line, every file
under `proof5/` (abbreviated IX, VIII, K for III.K, J for III.J, J4 for III.J$'''$, I8, I9, I10, I15 for
III.I$'''''''$, III.I$''''''''$, III.I$'''''''''$, III.I$''''''''''''''$, F2 for II.F$'$, C for III.C, C3 for
III.C$''$, B for III.B). "Standard" marks b-Sobolev embedding for a b-density, used without a program.

*The result, in one paragraph.*
- **Part IX's repair moves no conclusion here** (R3.1). Round 1's $N^\circ$ and $N^{\mathcal D}$ are replaced by
  $U^\sharp$, $\Omega^\sharp$ and $N^+ = M^\circ\cap\{t_{\mathrm{IVP}}\ge0\}$; Theorem 1.5 and Proposition 2.1 are
  restated on $N^+$, for tensors smooth up to $\Sigma^\circ$. The one new argument: the harmonic-gauge vector's source
  is known on $N^+$ only and is extended across $\Sigma^\circ$, and the solution on $N^+$ does not depend on the
  extension, as $\Sigma^\circ$ is noncharacteristic for $\Box$ with Part IX's leading coefficient (Lemma R3.1, P1).
- **(S$_K$) holds, for every $\beta\in(0,\delta_\sharp)$, $\delta_\sharp = (1-e_\Upsilon)\gamma_\Upsilon$** (R3.2).
  $h'$ has $\iota^+$-order exactly $\lambda_\sharp$ and $K^+$-order $\alpha$; on $\{\chi_K = 1\}$,
  $D\vartheta_{\mathrm{tot}}(\vec p\,')$ is a sum of row terms $\frac12\Box^\Upsilon\omega_\nu$ of joint orders
  $(\mathrm{Re}\,\lambda+1,\kappa_\nu)$, $\mathrm{Re}\,\lambda\ge\lambda_\sharp$, $\kappa_\nu>\lambda_\sharp+3$ (K1-K3).
  Theorem R2.12 is deduced without its hypothesis (Corollary R3.3). The room is the constraint damping: at
  $\gamma_\Upsilon = 0$ there is none (K4).
- **Round 2's cut-off $\chi'$ was built from the wrong $\chi_K$** (A8): III.H (1.2)'s, not Part VIII's, on whose
  $\{\chi_K = 1\}$ alone (R2.3) holds. Repaired with a later, narrower $\chi'$; only constants change.
- **The harmonic gauge beyond the cone: closed on the late region, open down to $\Sigma^\circ$** (R3.3). The source
  lies in II.F$'$ (1.4)'s class: at $\mathscr I^+$, $E^\Upsilon G$ does not see the trace-free angular slot, the only
  one with a radiation field (S1), so the source's order there is $\lambda_\sharp+1$, above the $b_I+1<\frac52$ asked
  (S2-S4); at $\iota^+$ and $K^+$ as on the cone. With II.F$'$ Theorem 1.1 for $\Box$ this gives a solution equal to
  $\dot g$ near $\Sigma^\circ$, in harmonic gauge on all of $N^+\cap\{t^\flat_*\ge3\}$ out to $\mathscr I^+$, settling
  on compact sets to $\dot\mu K^*+c_\infty\mathcal L_{W^*}g$ at the rate $t_*^{-1/2}$ (Theorem R3.4). Down to
  $\Sigma^\circ$ one estimate is missing, (Ext$\Box$): the gauge vector's $\mathscr I^+$-order above $\frac12+\beta$
  on a bounded $t_*$-slab (S5, S7), which needs a weighted Cauchy estimate for $\Box$ near $I_0\cup\mathscr I^+$; the
  write-out's exterior theorems are stated for $L$ only.
- **The rate** $t_*^{-1/2}$ is not improved: task 4 was to be attempted only if the harmonic gauge closed on all of $N$.

### R3.1 Part IX's repair (D610): the amendments

*What Part IX now says* (READ). $\nu\ge0$ with $\nu = 0$ on $[0,R_\nu]$, $R_\nu = \frac12(r_0+R)$ (K:102-107, IX:24-29),
so near $\{r = r_0\}$, $N = \{t_{\mathrm{IVP}}\ge0\}$ and $\Sigma^\circ$ is part of $N$'s boundary. The comparison is
posed on $U^\sharp := M^\circ\cap\{t_{\mathrm{IVP}}>-1\}$ and $\Omega^\sharp := D_{U^\sharp}(\Sigma^\circ)$, open and
globally hyperbolic on each component with Cauchy hypersurface $\Sigma^\circ$, with $\Omega^\sharp_+ = N^+ :=
M^\circ\cap\{t_{\mathrm{IVP}}\ge0\}$ (IX:30-33, 131-134); tensors are compared on future halves $\Omega'_+$, smooth up
to $\Sigma_U$ (IX:35-40, 209-216); a source known on $\Omega'_+$ only is extended across $\Sigma_U$ by Seeley's theorem
and a cut-off (IX:231-234); $\dot g|_{N^+}$ is smooth up to $\Sigma^\circ$ (IX:40-47); $N^\circ$ and $N^{\mathcal D}$
are withdrawn, and a text citing them reads $U^\sharp$, $\Omega^\sharp$, $N^+$ (IX:350-351).

*The uses here, each amended.* These are also the D610 repair verifier's minor finding m1 for this file (relayed
2026-11-02): $N^{\mathcal D} := D_{N^\circ}(\Sigma^\circ)$ and the old Lemma 1.2 at lines 213, 221, 243, 357 and 769,
and $U\subset N^\circ$ in Theorem 1.5 (d) at line 166. A substitution of names is not enough, as $e$ is not defined on
$\Omega^\sharp\cap\{t_{\mathrm{IVP}}<0,\ r\le R_\nu\}$: the source is extended across $\Sigma^\circ$ as IX's Step 1 does,
the problem is solved on $\Omega^\sharp$, and the result is stated on $N^+$ ((A4), Lemma R3.1, computed P1); line 166
is (A2) (d), lines 213, 221 and 243 are (A3)-(A4), line 357 is (A6), line 769 is (A7).

(A1) Section 0, "Part VIII in the class" (round 1, lines 52-54): $\dot g$ is smooth on the interior of $N$, and
$\dot g|_{N^+}$ is smooth up to $\Sigma^\circ$; where $\nu = 0$, $N$ ends at $\Sigma^\circ$.

(A2) Theorem 1.5 (lines 149-169) and its proof (lines 171-193). $N^\circ := N\cap\{r>r_0\}$ is not open where $\nu = 0$,
while the proof (line 174) uses the open set $\{t>\psi_{\mathrm{IVP}}(r)-\nu(r),\ r>r_0\}$, the interior of $N$ in
$M^\circ$. Read (a)-(c) on $N^+$, every object smooth up to $\Sigma^\circ$. Lemma 1.4 (b) is applied on the interior of
$N^+$, whose orbit space $\{t>\psi_{\mathrm{IVP}}(r),\ r>r_0\}$ lies above a graph, so is simply connected, and whose
upward rays $\{(v',r):v'\ge v\}$ stay in it ($t_{\mathrm{IVP}}$ increases with $v$ at fixed $r$). $\xi[h]$, $H_0$ and
$\omega$ are smooth up to $\Sigma^\circ$ (inverses on $S^3$ with parameters $(v,r)$, commuting with
$\partial_v,\partial_r$); $\zeta = -\int_v^\infty\omega_v\,dv'$ has $d\zeta = \omega$, so its derivatives of order $\ge1$
are derivatives of $\omega$ and $\zeta$ is continuous up to $\Sigma^\circ$. So $X_{\mathrm{RW}}$ and
$\dot g_{\mathrm{RW}}$ are smooth up to $\Sigma^\circ$, and (a)'s data clause is read from one side (Part VIII Lemma
1.1, VIII:71-72). (a)-(c) also hold, as proved, on the open set $\mathrm{int}\,N\cap M^\circ$, the data clause aside.
(d) reads: $U\subset U^\sharp$ open and $SO(4)$-invariant, $\Omega'_+ := D_U(\Sigma_U)\cap\{t_{\mathrm{IVP}}\ge0\}$,
$\dot g'$ on $\Omega'_+$ smooth up to $\Sigma_U$, inducing the data plus those of $\mathcal L_Zg$, $Z$ smooth up to
$\Sigma_U$; then $\dot g' = \dot g_{\mathrm{RW}}$ on $\Omega'_+$. Its proof stands with Part IX Corollary 2.3 and Remark
2.4 (c) as repaired (IX:279-293, 312-317): Lemmas 1.3 (c) and 1.4 (a) are sphere-wise and pointwise, and (d) uses no
simple connectivity.

(A3) Section 2.1, "Let $N^{\mathcal D} := D_{N^\circ}(\Sigma^\circ)$" (line 213): read $\Omega^\sharp$ (IX Lemma 1.2),
with $\Omega^\sharp_+ = N^+$.

(A4) Proposition 2.1 (a)-(b) (lines 220-228) and its proof (lines 241-246). Read (a) for 1-forms $Z'$ on $N^+$, smooth up
to $\Sigma^\circ$, with $\Box Z' = -\Theta(e)$ on $N^+$; such $Z'$ exist for all smooth Cauchy data on $\Sigma^\circ$
and are determined on $N^+$ by them (Lemma R3.1). Read (b) on $\Omega'_+$, $U\subset U^\sharp$, for $\dot g'$ smooth
up to $\Sigma_U$. In the proof, $e$ is known on $N^+$ only (A2): extend $-\Theta(e)$ across $\Sigma^\circ$ to $F$ on
$\Omega^\sharp$ as IX Theorem 2.2's Step 1 does (IX:231-234), solve $\Box\tilde Z = F$ on $\Omega^\sharp$ with the data
(IX Lemma 1.1 with $P = \pm\Box$, IX Lemma 2.1 (a)), and restrict to $N^+$.

**Lemma R3.1 (the extension does not reach $N^+$; deduced, computed P1).** Let $F_1,F_2$ be smooth on $\Omega^\sharp$
and equal on $N^+$, and let $\tilde Z_i$ solve $\Box\tilde Z_i = F_i$ with the same Cauchy data on $\Sigma^\circ$. Then
$\tilde Z_1 = \tilde Z_2$ on $N^+$.

*Proof.* $d := \tilde Z_1-\tilde Z_2$ has $\Box d = 0$ on $N^+$ and zero data on $\Sigma^\circ$. IX Theorem 2.2's Step 3
(IX:253-277) uses of $L^0$ only that its principal part is a negative multiple of $g^{\alpha\beta}\partial_\alpha
\partial_\beta$ times the identity, so that $\Sigma^\circ$ is noncharacteristic. $\Box$ has the principal part
$-g^{\alpha\beta}\partial_\alpha\partial_\beta$ (IX Lemma 2.1 (a)); P1 computes the leading coefficient at $\Sigma$: for
$w = f(t)W$ no derivative of $f$ above the second occurs in $\Box w$, and the coefficient of $f''$ is $-g^{tt}W$, so the
coefficient of $t^{m-2}$ in $\Box(t^mW+O(t^{m+1}))$ at $t = 0$ is $-m(m-1)g^{tt}W$ (control: with the trace term of $G$
dropped the coefficient is not $-g^{tt}W$). So $d$ vanishes to infinite order at $\Sigma^\circ$, its extension by 0 is
smooth with $\Box\tilde d = 0$ on $\Omega^\sharp$ and zero data, and [BGP] Corollary 3.2.4, on each component (IX:96-99),
gives $\tilde d = 0$. $\square$

*Consequences.* The extension affects no conclusion on $N^+$. $G$-invariance needs no averaging: for $\sigma\in G$,
$\sigma^*\tilde Z$ solves the problem with $\sigma^*F$, another extension of the $G$-invariant $-\Theta(e)$ ($G$
preserves $t_{\mathrm{IVP}}$ and $|x|$, so $N^+$ and $\Omega^\sharp$: IX:312-314), and the same $G$-invariant data; so
$\sigma^*Z' = Z'$ on $N^+$.

(A5) Lemma 2.2, Theorem 2.3 (lines 275-295) and Remark 2.4: unchanged. They concern the horizon at late times, in the
interior of $N^+$, and Lemma 1.4 is used on a neighbourhood of the horizon's orbit.

(A6) Corollary 2.6 (lines 357-363), withdrawn by R2.0: read $N^+$ for $N^{\mathcal D}$. R2.0's $d\phi_2$ is defined on
all of $M^\circ$, so the withdrawal stands.

(A7) Round 2. R2.V (m1) (lines 766-772): the Part IX inputs of Proposition 2.1 (a) are now IX Lemma 1.1 on
$\Omega^\sharp$, IX Lemma 1.2 ($\Omega^\sharp_+ = N^+$), the extension of IX:35-40 and Lemma R3.1. Part IX's status line
reads verified (D347) and repaired (D610) (IX:3-6); the repair's second reading is not recorded there. Theorem R2.12:
$Y$ lives on $\Omega = \mathrm{cl}_M\{t_*\ge1,\ r\ge r_0\}$ (F2:41) and vanishes for $t_*<2$; as $t_*\le
t_{\mathrm{IVP}}$, it extends by 0 to $N^+$, and near $\Sigma^\circ$ ($t_*\le0$ there) $\dot g_H = \dot g+\dot\mu
\mathcal L_{W^{**}_H}g$. Corollary R2.8 and Proposition R2.13 do not use $N^\circ$ or $N^{\mathcal D}$.

(A8) Theorem R2.12's cut-off (lines 703-707, 729-731); not from Part IX, found while checking (A7). (R2.3) holds on
$\{\chi_K = 1\}$ for Part VIII's $\chi_K$, the cut-off of III.B section 5 and III.I (1.2): supported in
$\{t>50R_1\}\cap\{t^\flat_*\ge10\}$, and equal to 1 on a neighbourhood of $\mathrm{supp}\,\chi^\flat_K\supset\{|x|<t/10,\
t>60R_1\}$ (B:345-352, `PART-III-I-CONE.md`:25-28; thresholds raised as K:35-37 allows). Round 2's $\chi' :=
\chi_+(t_*/2)\chi_c(2r/t_*)$ is built from III.H (1.2)'s $\chi_K = \chi_+(t_*)\chi_c(|x|/t_*)$
(`PART-III-H-AUGMENT.md`:66-71), a different function, and its support $\{t_*\ge2,\ r\le t_*/4\}$ is not in Part
VIII's $\{\chi_K = 1\}$, which misses $\{t^\flat_*<10\}$. Repair: $\chi' := \chi_+(t_*/T_1)\chi_c(10r/t_*)$ with $T_1$
above the threshold $T_\chi$ for which $\chi^\flat_K = 1$ on $\{|x|<t/10,\ t>T_\chi\}$. As $t\ge t_*$ ($\psi\ge0$,
B:243-244), $\mathrm{supp}\,\chi'\subset\{t_*\ge T_1,\ r\le t_*/20\}\subset\{|x|<t/10,\ t>T_\chi\}\subset
\mathrm{int}\{\chi_K = 1\}$; $\chi' = 1$ on $\{t_*\ge2T_1,\ r\le t_*/40\}$, where R2.12 (ii) now holds; in the proof of
(iii), "$t_*\ge8r_h$" reads "$t_*\ge\max(2T_1,40r_h)$"; and $\chi'$ is supported in $\{r\le t_*/4\}$, as Lemma R2.11
asks. Nothing else changes.

*Does a conclusion move?* No. Every decay, charge and growth statement lives at late times in the interior of $N^+$;
the domain statements read $N^+$, with smoothness up to $\Sigma^\circ$, where they read $N^\circ$ or $N^{\mathcal D}$.
Read literally, $N^{\mathcal D}$ also contained points below $\Sigma^\circ$ where $\nu>0$; nothing after round 1 used
them. (A8) changes constants only.

### R3.2 (S$_K$): settled

*Readings* (READ).
1. $h'$. Part VIII Theorem 2.2 (3)-(4): $h'\in\mathcal X^\infty_{J,\mathrm{ex}}$, and (2.2) where $\chi_K = 1$
   (VIII:224-230, 295-301). $\mathcal X^k_{J,\mathrm{ex}} := H^{k,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E_+,
   3+\epsilon_+),\alpha}_{\mathrm b}$ (J4:48-49): a partial expansion at $\iota^+$ with index set $\mathcal E_+$ up to
   the weight $3+\epsilon_+$, and $K^+$-weight $\alpha$. Near the corner $\rho_+ = 1/r$, $\rho_K = r/t_*$ (J4:34-36).
   The expansion is in powers of $\rho_+$ with coefficients carrying the weights of the adjacent faces, $\alpha$ at
   $\iota^+\cap K^+$ (J4:141-147, 170), for a b-density (`PART-III-A-PREREQ.md`:142). $\mathcal E_+\subset
   \{\mathrm{Re}\ge\lambda_\sharp\}$ and contains an exponent of real part $\lambda_\sharp$ ((H1), I10:53-55);
   $\lambda_\sharp = \frac32+(1-e_\Upsilon)\gamma_\Upsilon$ is a simple pole with no resonant state (J:13-15),
   $K_\iota(\lambda_\sharp) = 1$ (J:112-114), so the $\lambda_\sharp$-term carries no logarithm.
2. $h_{b_0,\mathrm{rem}}(q')$: $K^+$-order $(\alpha-2)-$, plain $\iota^+$-weight $\ge\lambda_\sharp$ (I15:147-150); each
   piece is a function of $t_*$ times a stationary tensor (I15:67-72, 157-162).
3. $\vartheta_{\mathrm{tot}}$ is the sum of III.I$'''''''$'s terms (I8:183-185), the motion terms (I9:128-131), which
   are the s1 rows (I10:101-102, 180-182), the rows (I10:258-260) and the rotation rows (I15:92-94). III.I$'''''''$'s
   terms each carry a factor $d\chi_K$ (I8:139-147, 163-164) and vanish on $\{\chi_K = 1\}$, where $d\chi_K = 0$. Where
   $\chi_K = 1$ a row term is $\vartheta_{\nu,\sharp}(W) = \vartheta_\nu(W) = \frac12\Box^\Upsilon_{b_0}\omega_\nu(W)$
   (I10:177-178, 202, 234-235), and by (2.2) there (I10:191-193) it is $\frac12[a^{(K+1)}(A_1\breve\omega^K+A_2\breve
   \omega^{K-1})+a^{(K+2)}A_2\breve\omega^K]$, with $\breve\omega^i\in\mathcal A^{(\sigma_\tau-i,0)+\mathcal F}$
   (I10:152-154), $\mathcal F = (0,0)\cup\mathcal E_{\mathrm{ind}}$, $\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}>0$
   (I15:39), $a^{(j)}$ of rate $e_\nu+j$ (I10:221-225; for s0, $A^{(j)}_\nu$ of rate $\lambda-1+j$), and
   $\mathrm{Re}\,\lambda\ge\lambda_\sharp$ on every row (I10:61-64; I15:103-104 for the rotation rows). Lemma 2.2 (b),
   (d) state the $\iota^+$-index set $(\lambda+1,k)+\mathcal F$ near $(\iota^+)^\circ$ and the $K^+$-weight
   $\kappa_\nu-$, $\kappa_\nu>\lambda_\sharp+3$, near $K^+$, each separately (I10:195-206).

*Computed.* K1: a product $a(t_*)P(x)$, $a$ of rate $c$ (logarithms allowed), $P$ of spatial order $m$, is conormal at
the corner with orders $(c+m,c)$, exactly without logarithms and with a loss "$-$" with them: the pointwise form of J4
Lemma 2.1 (J4:119-122). K3: on Tangherlini at large $r$, with the $E_\Upsilon$-term of $\Box^\Upsilon$ and $c_\Upsilon
= |x|^{-1}dt$, the coefficients $A_1$ of $\partial_{t_*}$ and $A_2$ of $\partial^2_{t_*}$ gain one and two spatial
orders (control: with $c_\Upsilon = dt$, $A_1$ gains none). K2: with these, every row type (s1, v1, s0, s2, c0, c1,
rotation) has joint orders $(\lambda+1,\kappa_\nu)$ at the corner, Lemma 2.2's values (control: $A_1$ without its gain
gives $\iota^+$-order $\lambda$, contradicting Lemma 2.2 (b)).

**Proposition R3.2 ((S$_K$) holds; deduced from the readings and K1-K4).** Let $\delta_\sharp := (1-e_\Upsilon)
\gamma_\Upsilon = \lambda_\sharp-\frac32>0$ (I10:45-46). For every $\beta\in(0,\delta_\sharp)$ and $\eta\in(0,
\delta_\sharp-\beta)$, on $\{\chi_K = 1,\ t_*\ge T_0\}$: $h = h_{b_0,\mathrm{rem}}(q')+h'$ is conormal with
$\iota^+$-order $\lambda_\sharp-\eta>\frac32+\beta$ and $K^+$-order $\alpha-2-\eta>\frac12$;
$D\vartheta_{\mathrm{tot}}(\vec p\,')$ with $\iota^+$-order $\lambda_\sharp+1-\eta>\frac52+\beta$ and $K^+$-order
$>\lambda_\sharp+3$; and $J_h$ of (R2.3) with $\iota^+$-order $\lambda_\sharp+1-\eta>\beta+\frac52$ and $K^+$-order
$\alpha-2-\eta>\frac12$ (the factor $|x|^{-1}$ of $E^\Upsilon_{g,\infty}$ gains one $\iota^+$-order and none at $K^+$).
Each seminorm is bounded by finitely many of $U'$, so of the data (VIII:243, 309-311).

*Proof.* $h'$: by reading 1 and b-Sobolev embedding (standard), $h'$ and its b-derivatives are
$O(\rho_+^{\lambda_\sharp}\rho_K^\alpha)$ near the corner, $O(\rho_+^{\lambda_\sharp})$ on $(\iota^+)^\circ$ and
$O(t_*^{-\alpha})$ near $K^+$; $t_*\partial_{t_*}$, $r\partial_r$ and $\partial_\omega$ span the b-vector fields there
(K1). $h_{\mathrm{rem}}$ and the rows: K1 and K2 applied to the explicit forms; the shifts by $\mathcal F$ only raise
orders. $J_h$: (R2.3). The inequalities: K4, at 75 rational samples of $(\gamma_\Upsilon,e_\Upsilon,\beta)$ (control: at
$\beta = \delta_\sharp$ the condition on $h'$ is an equality, and at $\gamma_\Upsilon = 0$ no $\beta>0$ is admissible).
$\square$

**Corollary R3.3 (Theorem R2.12 without (S$_K$); deduced).** Theorem R2.12, with the cut-off of (A8), holds for every
$\beta\in(0,\delta_\sharp)$, from Part VIII, the readings above, Theorems R2.5 and R2.7 and Lemma R2.11, assuming (Dyn)
and III.H$'$'s obligation (H$'$7) as Theorem R2.5 does; its constant is bounded by the data norms of Part VIII. The room
is $\delta_\sharp$, the constraint damping: at $\gamma_\Upsilon = 0$ the cone source would have $\iota^+$-order
$\frac52$, the edge of Lemma R2.11 for every $\beta>0$.

*The class* (K5; not needed above). $G$ fixes no nonzero element of $\mathcal S_1$ or of $\mathfrak{so}(4)$, a line in
$\mathcal S_0$ and a line in $\mathcal S_2$, spanned by $x_1^2+x_2^2-x_3^2-x_4^2$ (round 1's $P_1(\cos2\theta)$). So in
the class only the rows of types s0, s2 and c0 carry parameters (coefficient spaces: I10:90-97); s1, c1, v1 and the
rotation rows vanish, as $S'$ and $S'^{(0)}_1$ do (VIII:314-316). Control: the torus alone fixes $R_{12}$ and $R_{34}$;
the reflections are what remove the rotation rows.

### R3.3 The harmonic gauge beyond the cone

*Setting.* On $\Omega_*$ (F2:41), in the class, $\dot g_0 = \chi_K\dot\mu K$ (I8 (1.3) at $S = S^{(0)}_1 = 0$,
VIII:239), and Part VIII Theorem 2.2 (5) (VIII:237-240) with R2.10 gives
$$-\Theta(\dot g) = E^\Upsilon G(\dot g-\chi_K\dot\mu K)+D\vartheta_{\mathrm{tot}}(\vec p\,')-\dot\mu\Theta(\chi_KK).
\tag{R3.1}$$
With $\Box W^{**}_H = -\Theta(K)$ (Proposition 2.1 (d)) put
$$F_Y := -\Theta(\dot g)-\dot\mu\Box(\chi_KW^{**}_H) = E^\Upsilon G(\dot g-\chi_K\dot\mu K)+D\vartheta_{\mathrm{tot}}
(\vec p\,')-\dot\mu\big([\Theta,\chi_K]K+[\Box,\chi_K]W^{**}_H\big).\tag{R3.2}$$
So $F_Y = J_h$ on $\{\chi_K = 1\}$ (R2.3); $F_Y = E^\Upsilon G\dot g$ on $\{\chi_K = 0\}$, in particular near
$\mathscr I^+$ ($\mathrm{supp}\,\chi_K\subset\{|x|<t/2\}$, B:347-348); the commutator terms live on $\mathcal C =
\mathrm{supp}\,d\chi_K$, whose closure meets $\partial M$ only in a compact subset of $(\iota^+)^\circ$ (I15:207-208).

**Lemma R3.5 (the source in II.F$'$'s class; deduced, computed S1-S4, S6, S8).** Let $\beta\in(0,\delta_\sharp)$,
$b_+ := \beta+\frac12$, $b_I\in(b_+,\frac32)$, $\alpha_+ := \beta-2$, $\alpha_I := b_I-2$, and $\chi\in C^\infty(\mathbb
R)$ equal to 0 on $(-\infty,2]$ and 1 on $[3,\infty)$. Then (1.3) of II.F$'$ holds for $P_0 = \Box$, and
$\chi(t^\flat_*)F_Y$ lies in (1.4).

*Proof.* *(1.3).* $\bar S = \gamma_\Upsilon\min(1-e_\Upsilon,1)$ for $\Box^\Upsilon$ (`PART-III-D-GAUGEPOT.md`:131-139),
so $\bar S = 0$ for $\Box$ ($\gamma_\Upsilon = 0$), and (1.3) reads $b_I<\frac32$, $b_+<b_I$ (F2:67, 89-92). *Weights.*
(1.4) is $(b_I+1,b_++2,\frac12)$ for the b-density $\mu_{\mathrm b}$ (S3; F2:89-96), and a conormal function lies there
iff its pointwise order exceeds each weight (S4). *$\mathscr I^+$.* There $F_Y = E^\Upsilon G\dot g$ with
$E^\Upsilon_{g,\infty}k = -\gamma_\Upsilon(2\iota_{g^{-1}c_\Upsilon}k-\frac23(1-e_\Upsilon)c_\Upsilon\mathrm{tr}_gk)$,
$c_\Upsilon = |x|^{-1}dt$ (III.B (6.1), read in round 2), which contracts with $g^{-1}c_\Upsilon$, a vector with no
angular component, and takes a trace: it does not see the trace-free angular slot $\slashed\pi_0$ (S1; control: $\Theta$
does). $\dot g$ has on $\Omega_*$ the $\mathscr I^+$-classes of III.C Definition 3.1 slot by slot ($h'$: J4:48;
$\chi_-\dot h$: VIII:135-136; the $\chi_K$-terms vanish there), with exponents (C:154, 166-178, 182-186)
$>\frac32+2\gamma_\Upsilon$ for $\pi_C$, $\frac32+(1-e_\Upsilon)\gamma_\Upsilon$ for $\pi_{01}$,
$\frac32+\gamma_\Upsilon$ for $\pi_{1/}$, $\frac32+(1-e_\Upsilon)\gamma_\Upsilon$ and $\frac32+2\gamma_\Upsilon$ for
$\pi_{11}$, and $\frac32$ for $\slashed\pi_0$, the radiation field. Without $\slashed\pi_0$ the least is
$\lambda_\sharp$ (S2; control: with it, $\frac32$), and $|x|^{-1}$ adds one: $\mathscr I^+$-order
$\lambda_\sharp+1>\frac52>b_I+1$. *$\iota^+$.* On
$\{\chi_K = 1\}$, $(\lambda_\sharp+1)-$ (Proposition R3.2). Elsewhere $\dot g-\chi_K\dot\mu K = h'+h_{\mathrm{rem}}(q')+
Dh_{\mathrm{tot}}(\vec p\,')$ has $\iota^+$-order $\min(\lambda_\sharp,2)- = \lambda_\sharp-$ ($h_{\mathrm{tot}}$'s
terms lie in $\mathcal A^{\mathcal G}$, $\mathcal A^{\mathcal G+1}$, $\mathcal A^{(\lambda,k)+\mathcal F}$: I8:155-158,
I9:94-98, I10:195-196), so $E^\Upsilon G(\cdot)$ has $(\lambda_\sharp+1)-$; $D\vartheta_{\mathrm{tot}}$ has
$\min(3,\lambda_\sharp+1)-$ (I8:159-160, I10:195-196); $[\Theta,\chi_K]K$ has order 3 ($d\chi_K\in\rho_+C^\infty$,
I8:172-173; $K$ stationary in $|x|^{-2}C^\infty(\bar X)$, I8:309-310); $[\Box,\chi_K]$ gains two orders on the cone (S6;
control: a spatial cut-off gains one) and $W^{**}_H$ has order 1 on $(\iota^+)^\circ$ (S8: $r\partial_\mu T_\mu\to2$,
$rA\to\frac12$, $rB\to-\frac14$, and $r\frac v2W^*$ bounded there; control: at fixed $r$, $\frac v2W^*$ grows), so
$[\Box,\chi_K]W^{**}_H$ has order 3. All exceed $b_++2 = \beta+\frac52$ (S4). *$K^+$.* On $\{\chi_K = 1\}$,
$(\alpha-2)->\frac12$; $\mathcal C$ and $\{\chi_K<1\}$ stay away from $K^+$. *Support.* $\chi(t^\flat_*)F_Y$ vanishes on
$\{t^\flat_*<2\}$, as $(\Omega_*)^{\bullet,-}$ asks. $\square$

Without the term $\dot\mu\Box(\chi_KW^{**}_H)$ the source near $K^+$ is $J_h-\dot\mu\Theta(K)$, stationary at leading
order, of $K^+$-order 0, and not in (1.4) (S4's control). That is why the mass change is carried explicitly.

**Theorem R3.4 (the harmonic gauge on the late region; deduced from Lemma R3.5, II.F$'$ Theorem 1.1 at $P = P_0 =
\Box$, Theorems R2.5 and R2.7; assuming (Dyn) and (H$'$7)).** $\Box$ is 1-admissible with sf-weight $\alpha_+ =
\alpha_{\mathrm{sf}}$ and sf-loss 0 (Theorem R2.5 (iii), in the relaxed form II.F$'$ allows, F2:717). Let $Y$ be the
forward solution on $\Omega_*$ of $\Box Y = \chi(t^\flat_*)F_Y$ (II.F$'$ Theorem 1.1, F2:65-80), extended by 0 to $N^+$,
$$Z := \dot\mu\chi_KW^{**}_H+Y,\qquad\dot g_H := \dot g+\mathcal L_Zg\quad\text{on }N^+.$$
(i) $\dot g_H$ is $G$-invariant, $D\mathrm{Ric}(\dot g_H) = 0$, and $\dot g_H = \dot g$ on $N^+\cap\{t^\flat_*<2\}$; so
it induces $(\dot\gamma,\dot k)$ exactly.

(ii) $\Theta(\dot g_H) = -(1-\chi(t^\flat_*))\chi^\natural_0E^\Upsilon G\dot g$. So $\dot g_H$ is in harmonic gauge on
$N^+\cap\{t^\flat_*\ge3\}$, the whole late region out to $\mathscr I^+$, and near $\Sigma^\circ$, where $\chi^\natural_0
= 0$ (K:76-77, 84-86); in general not on $\{t^\flat_*<3,\ \chi^\natural_0\ne0\}$.

(iii) On each $\{r_0<r\le R',\ t_*\ge T'\}$, with the derivatives of (R2.2),
$$\big|\dot g_H-\dot\mu K^*-c_\infty\mathcal L_{W^*}g\big|\le Ct_*^{-1/2},\qquad c_\infty = \frac1{4\pi^2}\int\ell\big(
\chi'J_h+[\Box,\chi']Y\big)\,dv,$$
$\chi'$ of (A8): a horizon charge, as in R2.12 (iii).

(iv) For $Y_h$ on $N^+$ with $\Box Y_h = 0$ and compactly supported Cauchy data on $\Sigma^\circ$, $\dot g_H+\mathcal
L_{Y_h}g$ has (ii), induces $(\dot\gamma,\dot k)$ up to the data of $\mathcal L_{Y_h}g$, and has (iii) with
$c_\infty+Q[Y_h]/4\pi^2$.

*Proof.* (i) $\chi_K = 0$ on $\{t^\flat_*<10\}$ and $Y = 0$ on $\{t^\flat_*<2\}$; $D\mathrm{Ric}(\mathcal L_Zg) = 0$
(IX Lemma 2.1 (b)); $\dot g$ induces the data (VIII:314-317); $G$-invariance as in R2.12 (i). (ii) By (R3.2),
$\Theta(\dot g_H) = \Theta(\dot g)+\dot\mu\Box(\chi_KW^{**}_H)+\chi(t^\flat_*)F_Y = (1-\chi(t^\flat_*))(\Theta(\dot g)+
\dot\mu\Box(\chi_KW^{**}_H))$, and $\chi_K = 0$ where $\chi(t^\flat_*)<1$. There $\dot\Upsilon^\natural(\dot g) = 0$
(VIII:132-133 on $\mathcal D$, (R3.1) with $\chi_K = 0$ and $\chi^\natural_0 = 1$ on $\Omega_*\cap\{t^\flat_*<10\}$),
and $\dot\Upsilon^\natural = -\Theta-\chi^\natural_0E^\Upsilon G$ (R2.10's computation with the cut-off: C3:59-60,
K:93-94, VIII:36-41). (iii) Cone localisation with $\chi'$ of (A8): $\chi'Y$ is the forward solution of
$\Box(\chi'Y) = \chi'J_h+[\Box,\chi']Y$, as $\chi(t^\flat_*) = 1$ and $F_Y = J_h$ on $\mathrm{supp}\,\chi'$. The first
term is in Theorem R2.5's class by Proposition R3.2 and Lemma R2.11. The second is supported in $\mathrm{supp}\,
d\chi'$, a compact set and a cone in $(\iota^+)^\circ$, where $Y\in H^{k,(\alpha_I,\alpha_+,-1)}_{\mathrm b}$ (sf-loss
0) and $[\Box,\chi']\in\rho_+^2\mathrm{Diff}^1_{\mathrm b}$ (S6) give sf-weight $\alpha_++2 = \alpha_{\mathrm{sf}}+2$,
Theorem R2.5's (b-regularity gives every 3b-order on the cone, as in Lemma R2.11's proof). Theorem R2.7 gives
$|\chi'Y-c(t_*)W^*|\le Ct_*^{-1/2}$. For large $t_*$, $\chi' = 1$ on compact $r$-sets and $d\chi' = 0$ near the horizon,
so $\ell$ of the source is $\ell(J_h) = -\ell(\Theta(h)) = O(v^{-w+\epsilon'})$ (Theorem 2.3) and $c(t_*)\to c_\infty$
at the rate $t_*^{-(w-1)+\epsilon'}$. On compact $r$-sets at late times $Y = \chi'Y$ and $\dot g_H-\dot\mu K^* =
h+\mathcal L_Yg$; conclude as in R2.12 (iii). (iv) $Y_h$ has compactly supported data on every later slice (finite
speed of propagation), so Corollary R2.8 applies; $\mathcal L_{Y_h}g$ is linear in $Y_h$. $\square$

So the harmonic gauge holds on everything but a transition region bounded in $t^\flat_*$, where the solution is Part
VIII's own, in its generalised harmonic gauge $\dot\Upsilon^\natural = 0$.

*The obstruction down to $\Sigma^\circ$.*

(Ext$\Box$) Let $Z_1$ be the solution on $N^+$ of $\Box Z_1 = F_Y$ with zero Cauchy data on $\Sigma^\circ$ (IX Lemma 1.1
on $\Omega^\sharp$, with $F_Y|_{N^+}$ extended across $\Sigma^\circ$; unique on $N^+$ by Lemma R3.1). There are
$\beta\in(0,\delta_\sharp)$ and $p>\frac12+\beta$ such that $Z_1$ and its b-derivatives are $O(\rho_I^p)$ near
$\mathscr I^+$ on $N^+\cap\{2\le t^\flat_*\le3\}$.

**Proposition R3.6 (conditional on (Ext$\Box$); deduced, computed S5, S7).** Under (Ext$\Box$), with $Z :=
\dot\mu\chi_KW^{**}_H+Z_1$, $\dot g_H := \dot g+\mathcal L_Zg$ is in harmonic gauge on all of $N^+$, induces
$(\dot\gamma,\dot k)$ exactly, and satisfies Theorem R3.4 (iii)-(iv).

*Proof.* $\Box Z = -\Theta(\dot g)$ on $N^+$. $Z_1 = 0$ and $\nabla_\nu Z_1 = 0$ on $\Sigma^\circ$, so $\mathcal
L_{Z_1}g$ induces zero data (IX Lemma 2.1 (f)). $\chi(t^\flat_*)Z_1$ is the forward solution on $\Omega_*$ of
$\Box(\chi Z_1) = \chi F_Y+[\Box,\chi(t^\flat_*)]Z_1$. The first term is Lemma R3.5's. The second is supported in
$\{2\le t^\flat_*\le3\}$, bounded in $t_*$, and meets $\partial M$ only at $\mathscr I^+$; $t^\flat_*$ is smooth near
$\mathscr I^+$ and equals $t_*$ there (K:34-35), so it is $t_*+\kappa/r+\ldots$, and $[\Box,\chi(t^\flat_*)]$ gains one
order at $\mathscr I^+$ (S5; control: a cut-off in the static time gains none). So the second term has
$\mathscr I^+$-order $p+1$, and lies in (1.4) iff $p>\frac12+\beta$ (S7; control: $p = \frac12+\beta$ fails). The
proof of Theorem R3.4 (iii) then applies to $\chi(t^\flat_*)Z_1$. $\square$

*What (Ext$\Box$) needs, and why it is open.* On $N^+\cap\{t^\flat_*<3\}$, $F_Y = \chi^\natural_0E^\Upsilon G\dot g$,
supported where $\chi^\natural_0\ne0$: near infinity $\{t_{\mathrm{IVP}}>r/8\}\cup\{t_*>\frac12\}$ (K:74; C3:52-55),
a region that reaches the interior of $I_0$ and $\mathscr I^+$. Its $I_0$-weight is one above $\dot h$'s on the exterior
($\ell^\flat_0$, VIII:144-147), its $\mathscr I^+$-order $\lambda_\sharp+1$ (S2). The expected $\mathscr I^+$-order of
$Z_1$ is $\frac32$, the radiation field, against the $\frac12+\beta<1$ asked. But the write-out's exterior theory is
stated and proved for $L$ only: Part IV Proposition 3.1, the b-energy estimate near $I_0\cup\mathscr I^+$
(`PART-IV-EB.md`:196-202, its multiplier built on $L$'s edge-b form, Lemma 2.2 at 114-120), Part IV$''$ Theorem 2.4
(`PART-IV3-NM.md`:229-236) and III.C$'$ Theorem 3.1. II.F$'$ does not reach $I_0$: its domain is $\Omega_*$, and it
leaves even $\mathrm{cl}_M\{t_*\ge1\}$ unproved (F2:110-114). So (Ext$\Box$) asks for a $\Box$-version of Part IV
Proposition 3.1 at $\bar S = 0$, with a weight at $\mathscr I^+$ above $\frac12+\beta$; it is not written. Other Cauchy
data for the gauge vector do not help: the source near $I_0$ is fixed by $\dot g$.

### R3.4 The rate

Not attempted. Task 4 was to be attempted only if (S$_K$) and the harmonic gauge on all of $N$ both closed, and the
latter does not (R3.3). What a better rate needs is unchanged from R2.5 item 3: the $K^+$-expansion of $\Box$'s
resolvent at zero energy beyond the simple pole of Proposition 2.5, the analogue of III.I for $\Box$. The rate in
Theorem R3.4 (iii) and Corollary R3.3 is $t_*^{-1/2}$, what square integrability in time gives.

### R3.5 What is not proved

1. *(Ext$\Box$)*, so the harmonic gauge down to $\Sigma^\circ$ (Proposition R3.6 is conditional on it). Precisely: a
   weighted Cauchy estimate for $\Box$ on $N^+\cap\{t^\flat_*\le3\}$ near $I_0\cup\mathscr I^+$, for sources of
   $I_0$-weight one above $\ell^\flat_0$ and $\mathscr I^+$-order $\lambda_\sharp+1$, giving $\mathscr I^+$-order above
   $\frac12+\beta$ on $\{2\le t^\flat_*\le3\}$.
2. *A rate better than $t_*^{-1/2}$*: the analogue of III.I for $\Box$ (R3.4).
3. *II.F$'$ Theorem 1.1 at $P_0 = \Box$* rests on Theorem R2.5 (iii) and inherits III.H$'$'s obligation (H$'$7), as
   for $L_{b_0}$; (Dyn) is assumed throughout, as III.D does.
4. *A second reading* of R2.1-R2.5, R2.12, (A8) and this round.

### R3.6 Findings, labels and files (round 3)

*Findings.*
- (GD11) Part IX's repair (D610) is absorbed with no conclusion moved: round 1's $N^\circ$, $N^{\mathcal D}$ read
  $U^\sharp$, $\Omega^\sharp$, $N^+$ ((A1)-(A7)); the harmonic-gauge vector's source is extended across $\Sigma^\circ$,
  and the extension does not reach $N^+$ (Lemma R3.1; P1, $\Sigma^\circ$ noncharacteristic for $\Box$ with coefficient
  $-g^{tt}$). $G$-invariance follows from that independence, without averaging.
- (GD12) (S$_K$) holds for every $\beta\in(0,(1-e_\Upsilon)\gamma_\Upsilon)$ (Proposition R3.2): $h'$ has
  $\iota^+$-order $\lambda_\sharp$ exactly, and on $\{\chi_K = 1\}$ $D\vartheta_{\mathrm{tot}}(\vec p\,')$ is a sum of
  row terms of joint orders $(\mathrm{Re}\,\lambda+1,\kappa_\nu)$. Theorem R2.12 is deduced without its hypothesis
  (Corollary R3.3). The room is the constraint damping alone.
- (GD13) Round 2's cut-off $\chi'$ was built from III.H (1.2)'s $\chi_K$, not Part VIII's (A8); repaired, constants only.
- (GD14) $E^\Upsilon G$ does not see the radiation field (S1), so the harmonic-gauge source has $\mathscr I^+$-order
  $\lambda_\sharp+1$ and lies in II.F$'$ (1.4) (Lemma R3.5). The harmonic gauge holds on the whole late region
  $N^+\cap\{t^\flat_*\ge3\}$, out to $\mathscr I^+$, with the solution equal to Part VIII's near $\Sigma^\circ$ and the
  same settling on compact sets (Theorem R3.4).
- (GD15) Down to $\Sigma^\circ$ the obstruction is one estimate, (Ext$\Box$): $\mathscr I^+$-order above $\frac12+\beta$
  for the gauge vector on a bounded $t_*$-slab, which needs an exterior estimate for $\Box$ that the write-out proves
  for $L$ only (Proposition R3.6).
- (GD16) In the class only the rows of types s0, s2, c0 carry parameters (K5).

*Labels.* Computed: `checks/gdix5.py` P1 (identities at random rational points to 60 digits, as `ix5.py`),
`checks/gdsk5.py` K1-K5 and `checks/gdscri5.py` S1-S8 (exact, sympy; K4, S2, S4, S7 at exact rational samples); each
with a control that fails. Deduced: Lemma R3.1, Proposition R3.2, Corollary R3.3, Lemma R3.5, Theorem R3.4, Proposition
R3.6 (conditional on (Ext$\Box$)), the amendments (A1)-(A8). Everything that uses III.D, III.D$'$ or Theorem R2.5
assumes (Dyn), and Theorem R3.4 and Corollary R3.3 also (H$'$7). READ: the file:line citations above. Standard:
b-Sobolev embedding for a b-density.

*Proposed replacement for the paper's sentences on decay in harmonic gauge* (section 8.2, "In harmonic gauge the
spherically symmetric part ... at the rate τ^(−1/2) ..."; section 9, "... and in the harmonic gauge ..., which argue
decay in those gauges, remain deductions"):

> In harmonic gauge every perturbation in the class has a representative that equals the solution of section 8.2 near
> the initial surface and is in harmonic gauge on the whole late region, out to null infinity; on each region r ≤ R it
> settles to μ̇K* + c π_{W*}, c a conserved horizon charge, at the rate τ^(−1/2), and a gauge change with compactly
> supported data moves only c (deduced from the supplement's proved parts, with the horizon and trapping hypotheses its
> Part VI verifies and one order condition it carries; supplement GAUGEDECAY5 R3.4, `checks/gdsk5.py`,
> `checks/gdscri5.py`). The harmonic gauge down to the initial surface needs one estimate more, a weighted energy
> estimate for the 1-form wave operator near spatial infinity, which is not written; τ^(−1/2) is what square
> integrability in time gives.

*Files.* `GAUGEDECAY5.md` (this section appended); `checks/gdix5.py` with `checks/gdix5.out`; `checks/gdsk5.py` with
`checks/gdsk5.out`; `checks/gdscri5.py` with `checks/gdscri5.out`.

## Round 4

*Status.* Written 2026-11-02 (round 4, this section). Not verified by a second reader. Rounds 1-3 are left as they
stand; every change to them is a numbered amendment, (A9)-(A31) in section R4.c. New programs: `checks/gdext5.py`
(E1-E6), `checks/gdrate5.py` (G1-G4) and `checks/gdr3fix5.py` (T1-T5), with their `.out` files; every check has a
control that must fail, and fails.
Labels as in rounds 1-3. Readings use round 3's abbreviations (IX, VIII, K, I10, I15, F2, C, C3, B) and also IV, IV',
IV'', IV''' for `PART-IV-EB.md`, `PART-IV2-TAME.md`, `PART-IV3-NM.md`, `PART-IV4-SLAB.md`, C' for
`PART-III-C2-POLYHOM.md`, H for `PART-III-H-AUGMENT.md`, H' for `PART-III-H2-ADMISS.md`, I for `PART-III-I-CONE.md`,
D for `PART-III-D-GAUGEPOT.md`, VIA for `PART-VI-DYN.md` and IIC for `PART-II-C-OPERATORS.md`, all under `proof5/`.
Section headings of this round are lettered (R4.a-R4.e) so that they do not collide with the numbered statements
(see (A19)).

*The result, in one paragraph.*
- **(Ext$\Box$) holds** (Theorem R4.3), for every $\beta\in(0,\delta_\sharp)$: on the slab $N^+\cap\{2\le
  t^\flat_*\le3\}$ the gauge vector $Z_1$ has $\mathscr I^+$-order every $p<\min(\frac32,q_{\dot h}-1)$, where
  $q_{\dot h}>\frac32+2\gamma_\Upsilon$ is the order of Part VIII's $\dot h$ at $I_0$; the order asked is
  $\frac12+\beta$. The route is the natural one, a modification of Part IV's exterior theory, and it is shorter
  than expected: in III.B's Cartesian components $\Box$ is the scalar wave operator on each component plus a coupling
  of order $|x|^{-3}$, a sum of homogeneous pieces of degrees $-3,-5$ (E1), which after Part IV's conjugation lies in
  $\rho_0^2x_I^4\mathrm{Diff}^1_{\mathrm{e,b}}$ (E2). So the first-order matrix $\bar A$ of Part IV$'$ (1.1) is 0, and
  every estimate of Parts IV-IV$'''$ that does not use $\bar A$'s positivity carries over with the scalar proof.
- **The indicial data** (Lemma R4.1): at $\mathscr I^+$ the roots are $0$ (a radiation field, order $\frac32$, in all
  five components) and $a$ (the $I_0$-weight) (E3); at $I_0$ there is no restriction, $\tau$ being a b-time function
  for every weight (E4); the multiplier is positive iff $\alpha_I<\min(\alpha_0,0)$, Part IV's condition unchanged
  (E5). This sharp-weight condition, not the radiation field, is what sets the order reached on the slab: it ties the
  $\mathscr I^+$-weight to the source's $I_0$-weight, one above $\dot h$'s through the factor $|x|^{-1}$ of
  $c_\Upsilon$ (E6).
- **The harmonic gauge on all of $N^+$** (Corollary R4.4): Proposition R3.6 holds without its hypothesis. Every
  perturbation in the class has a representative in harmonic gauge on all of $N^+$ that induces the given data exactly
  and settles on compact sets to $\dot\mu K^*+c_\infty\mathcal L_{W^*}g$ at the rate $t_*^{-1/2}$. No hypothesis
  remains beyond the write-out's proved parts at $b_0$: (Dyn) is Part VI.A Theorem 6.1, and (H$'$7) is met for $\Box$
  by III.I Lemma 5.1's proof ((A16)).
- **The rate is not improved; the first obstruction is identified** (section R4.b). The resolvent side does not block
  it: at zero energy the first non-smooth term is $\sigma^2\log\sigma$, coefficient $-\frac1{8\pi^2}$ times the
  monopole (G1-G3). The missing step is Theorem R2.5 at positive $K^+$-weight. It is bounded by the gauge source's
  $\iota^+$-order $\lambda_\sharp+1 = \frac52+\delta_\sharp$ (G4): it can give at most $t_*^{-1/2-\kappa}$,
  $\kappa<\delta_\sharp$, and a model computation (formal) suggests that $t_*^{-1/2-\delta_\sharp}$ is the true rate
  of Theorem R3.4's representative when the $l = 0$ time component of that tail does not vanish.
- **Round 3's Theorem R3.4 (iv) and round 2's Corollary R2.8 had a false step** (the round-3 verifier's major finding,
  (A23)): data compactly supported on a slice $\{t_* = t_0\}$ do not stay compactly supported, as the slices reach
  $\mathscr I^+$. The missing input is the $\mathscr I^+$ half of (Ext$\Box$) for homogeneous solutions, and
  Proposition R4.2 gives it: Corollary R4.6 repairs R2.8 for data compactly supported on $\Sigma^\circ$, and with it
  R2.12 (iv), R2.13 (b), Corollary R3.3, Theorem R3.4 (iv) and Proposition R3.6 (iv) hold without condition, in that
  form. R2.8 with data on a later slice $\{t_* = t_0\}$ is not proved and nothing uses it.
- **The verifiers' findings on rounds 2 and 3** (relayed 2026-11-02) are seated as (A9)-(A22) and (A23)-(A31); the
  parts of the round-2 finding M1 that (A1)-(A8) already cover are listed in R4.c.

### R4.a The 1-form wave operator near $I_0\cup\mathscr I^+$

*Setting.* Near infinity ($|x|\ge3R_1$), in III.B's Cartesian coordinates $(t,x)$, $g = g_{b_0} = \eta+\mu_0
|x|^{-2}(dx^1)^2$, $x^1 = t-|x|$ (III.B Lemma 3.5 (b), as IV''':71 reads it): a Kerr-Schild metric with the
$\eta$-null form $dt-d|x|$, so $\det g = -1$. Part IV's chart: $\rho_0 = (2-x^1)^{-1}$, $\rho_I = (2-x^1)/|x|$,
$\rho = \rho_0\rho_I = |x|^{-1}$, $x_I = \rho_I^{1/2}$, $X_0 = \rho_0\partial_{\rho_0}$, $X_I = \rho_I\partial_{\rho_I}$
(IV:15-21). 1-forms are written in the Cartesian frame $dt,dx^1,\dots,dx^4$, the fixed smooth frame of II.C's spaces
(IIC:359); the frames $(dt,dr,r\,d\omega)$ and III.C (1.6) differ from it by smooth bounded functions of $\omega$,
so the weighted b-spaces and the pointwise orders do not depend on which is used. $\Box_0$ is the scalar operator
$-\mathrm{tr}\nabla^2$ of IV:122, and
$$L_\Box := \rho_I\rho^{-7/2}\,\Box\,\rho^{3/2}\quad\text{on Cartesian components,}\tag{R4.1}$$
IV (2.1)'s conjugation applied componentwise; $L$ is IV (2.1)'s scalar operator.

**Lemma R4.1 (the operator and its indicial data; computed E1-E5, deduced).**
(a) For every 1-form $Z$, $(\Box Z)_c = \Box_0Z_c+C_c^{\nu b}\partial_bZ_\nu+D_c^\nu Z_\nu$, with $C$, $D$ stationary,
$C = \sum_{k\ge1}\mu_0^kC_k$ and $D = \sum_{k\ge1}\mu_0^kD_k$, $C_k$ and $D_k$ homogeneous in $x$ of degrees $-1-2k$ and
$-2-2k$ (so $O(|x|^{-3})$ and $O(|x|^{-4})$ with every derivative; at E1's points only $k = 1$ occurs), and
$C_1\ne0$; there is no second-order coupling (E1, exact at integer points; $\Box$ computed as $d\delta+\delta d$ and
checked against $2\delta G\delta^*$, which needs $\mathrm{Ric} = 0$; control: on the non-vacuum metric with
$\mu_0|x|^{-1}$ the two differ).
(b) $L_\Box = L\otimes\mathrm{Id}+E$ with $E\in\rho_0^2x_I^4C^\infty(M_\sharp)\mathrm{Diff}^1_{\mathrm{e,b}}$ (E2:
$\partial_t = \rho_0(X_0-X_I)$, $\partial_r = \rho_0(-X_0+(1-\rho_I)X_I)$, $r^{-1}\partial_\omega = \rho_0x_I\cdot
x_I\partial_\omega$, and every coupling coefficient after the prefactor and the conjugation lies in
$\rho_0^2x_I^4C^\infty$; control: a coefficient of degree $-1$, a connection term of a non-Cartesian frame, gives an
order-0 eb-coefficient). So IV (2.2) holds for $L_\Box$ with $\tilde L_\Box := \tilde L\otimes\mathrm{Id}+E\in
x_I\mathrm{Diff}^2_{\mathrm{e,b}}$; IV' (1.1) holds with $\bar A = 0$ and $h = 0$; and the commutators of $L_\Box$ with
$X_0$, $X_I$ and the rotation fields acting on each Cartesian component lie in $x_I\mathrm{Diff}^{1,1}_{\mathrm{e,b;b}}$
(IV (2.3) for $L$; $[E,X]\in\rho_0^2x_I^4 \mathrm{Diff}^1_{\mathrm{e,b}}$ as $\mathcal V_{\mathrm{e,b}}$ is a Lie
algebra preserving $\rho_0^{\ell_0}x_I^{\ell_I} C^\infty$, IV Remark 1.3).
(c) *At $\mathscr I^+$.* $L_\Box(\rho_0^a\rho_I^\lambda e_\nu) = -2\lambda(a-\lambda)\rho_0^a\rho_I^\lambda
e_\nu+o(\rho_I^\lambda)$ at fixed $\rho_0$, $\omega$, for every Cartesian $e_\nu$ (E3: exact for the radial scalar
operator with $a$, $\lambda$ symbolic, and for the full 1-form operator in the components $dt$, $dx^1$ at one
$(a,\lambda)$, $\mu_0 = 1$ and one direction, the off-diagonal limits 0; control: the conjugation by $\rho$, the $n = 3$
one, leaves a divergent term). The indicial roots are $\lambda = 0$, the radiation field ($Z = \rho^{3/2}u$ of $\mathscr
I^+$-order $\frac32$ in every component), and $\lambda = a$, the functions of $\rho$ alone. For $L$ the roots are the
diagonal entries of $\bar A$, of which only slot 6's is 0 (IV'':24-33); for $\Box$ every component behaves as slot 6.
(d) *At $I_0$.* In $(\tau,\rho) = (t/|x|,|x|^{-1})$, $\rho^{-2-\alpha}\Box_0(\rho^\alpha v(\tau))\to(1-\tau^2)v''+(1-
2\alpha)\tau v'+\alpha(2-\alpha)v$ as $\rho\to0$, the coefficient of $v''$ independent of $\alpha$ (E4); the
coupling of item (a) is $O(\rho^2)$ relative and does not enter. So $\tau$ is a b-time function on $\{|\tau|<1\}$
for every weight: there is no indicial restriction at $I_0$ (control: the polar component of $a\,dr$ carries
$3a|x|^{-2}$, which survives as 3 at $I_0$).
(e) *The multiplier.* With $\bar A = 0$ the slot form of IV' Proposition 2.2's proof is $-4\alpha_I|Y|^2+4\kappa(
\alpha_0-\alpha_I)|Z|^2$, and IV (3.3)'s angular coefficient is $1+2(\alpha_0-\alpha_I)+\kappa(1-2\alpha_I)$; both are
positive for every $\kappa>0$ iff $\alpha_I<\min(\alpha_0,0)$ (E5; control: $\alpha_I = 0$ and $\alpha_I = \alpha_0$
degenerate).

*Proof.* (a) E1. The structure is that of any Kerr-Schild metric whose profile is homogeneous: the Christoffel symbols
of $\eta+\mu_0|x|^{-2}\ell\otimes\ell$, $\ell = dt-d|x|$ homogeneous of degree 0 and stationary, are $\mu_0$ times a
term homogeneous of degree $-3$ plus at most $\mu_0^2$ times one of degree $-5$ ($g^{-1} =
\eta^{-1}-\mu_0|x|^{-2}\ell^\sharp\otimes\ell^\sharp$); on a Ricci-flat metric $\Box = -\nabla^a\nabla_a$ (round 1,
section 2.1), whose coupling is $2g^{ab}\Gamma^\nu_{ac}\partial_b$ in first order and $\partial\Gamma$, $\Gamma\Gamma$
in zeroth order. E1 does not use this formula: it applies $d\delta+\delta d$ to test forms. (b) IV' Lemma 1.1
($\partial_t,\partial_{x^i}\in
\rho_0\mathcal V_{\mathrm{e,b}}$, $|x|^{-1}\partial_\omega\in\rho_0x_I\mathcal V_{\mathrm{e,b}}$), $|x|^{-3} =
\rho_0^3x_I^6$ and the prefactor $\rho_I\rho^{-2} = \rho_0^{-2}x_I^{-2}$; conjugation adds $\frac32\partial_b\log\rho$,
of degree $-1$; E2 computes each product. (c)-(e) as stated. $\square$

**Proposition R4.2 (the exterior estimate for $\Box$; IV Propositions 3.1 and 4.1, IV' Proposition 2.2, IV'' Lemmas
2.2-2.3 and IV''' Theorem 2.1 (i)-(iii) at $\Box$; deduced).** Let $\mathcal D$, $\Omega_{\mathrm{ext},r_1}$, $\mathcal
K$, $\mathcal S$, $\Omega^\natural = \Omega_{\mathrm{ext},r_1}\cup\mathcal S$, $\rho'_0$, $\rho'_I$ and $c_1$ be those of
III.K section 0 and Proposition 1.2's proof and of IV''' sections 0-2, at $S = 0$; $\mathcal D^+ := \mathcal D\cap\{
t_{\mathrm{IVP}}\ge0\}$, $\tau' := t_{\mathrm{IVP}}/|x|$, $\Omega^\natural_{c_1} := \Omega^\natural\cap\{\rho'_I<c_1\}$.
Let $a_0\in\mathbb R$, $\alpha_I<\min(a_0,0)$ and $m\in\mathbb N_0$. Let $F$ be a smooth 1-form on $\mathcal D^+$ with
$f_\flat := \rho_I\rho^{-7/2}F\in H^{m+4,(a_0,2\alpha_I)}_{\mathrm b}$ over $\Omega^\natural$ near infinity (in the
translated chart over $\mathcal S$) and $F\in H^{m+4}(\mathcal K)$. Then the solution $Z$ of $\Box Z = F$ on $\mathcal
D^+$ with zero Cauchy data on $\Sigma_{\mathrm{IVP}}$ is in $H^{m+1}(\mathcal K)$, and $u := \rho^{-3/2}Z$ satisfies
$$\|u\|_{H^{m+1,a_0}_{\mathrm b}(\Omega^\natural\cap\{\rho'_I>c_1/2\})}+\|u\|_{H^{(1;m),(a_0,2\alpha_I)}_{\mathrm{e,b;b}}
(\Omega^\natural_{c_1})}\le C\big(\|f_\flat\|_{H^{m+4,(a_0,2\alpha_I)}_{\mathrm b}}+\|F\|_{H^{m+4}(\mathcal K)}\big).
\tag{R4.2}$$
(The loss of four derivatives is IV'' Theorem 2.4's $d$; it is not optimised. Compactly supported $F$ is allowed.)

*Proof: the modifications, and why each step carries over.*
1. *The operator.* Every use of $L_g$'s form IV' (1.1) in IV'-IV''' is met by Lemma R4.1 (b) with $\bar A = 0$, the
   coefficients $\tilde a_i$ of IV'' (0.4) equal to 0, and so no tame terms (the simplification of VIII:145-147 at
   $h = 0$). The rotations act on each Cartesian component as derivations; IV':166-174 needed III.C Lemma 4.2's
   equivariance to let them act on the slots, and here nothing is needed.
2. *Near $\mathscr I^+$: IV' Proposition 2.2 at $\Box$.* The multiplier is $W = w^2V$, $V = X_0-(1+\kappa)X_I$, with the
   Euclidean fibre inner product on Cartesian components (IV' Lemma 2.1 is not needed: $\bar A = 0$ is diagonal). Write
   $2\,\mathrm{Re}\langle wL_\Box u,wVu\rangle = 2\,\mathrm{Re}\langle w(L\otimes\mathrm{Id})u,wVu\rangle+
   2\,\mathrm{Re}\langle wEu,wVu\rangle$. The first term is IV's identity in each component: $\langle Qu,u\rangle+
   \mathcal B_{\mathrm{fin}}$ with $\mathcal B_{\mathrm{fin}}\ge0$ (the energy current of $\Box_0\otimes\mathrm{Id}$ is
   the sum of the components' currents) and $\langle Qu,u\rangle\ge c_0\|wu\|^2_{H^1_{\mathrm{e,b}}}-Cc\|wu\|^2_{
   H^1_{\mathrm{e,b}}}$, $c_0>0$ by Lemma R4.1 (e) and independent of $c$, after IV's Poincaré inequality (in each
   component). The second is bounded by $Cc^2\|wu\|^2_{H^1_{\mathrm{e,b}}}$ on $\{x_I<c\}$, as $E$ carries
   $\rho_0^2x_I^4$, $\rho_0\le1$, and $V\in\mathcal V_{\mathrm{e,b}}$; it is absorbed for $c$ small, as IV's $Q-\bar Q$
   is. Higher b-regularity: IV's induction with the commutators of Lemma R4.1 (b).
3. *Near the interior of $I_0$: IV Proposition 4.1 and IV'' Lemma 2.2 at $\Box$.* There $\rho_I\ge\delta$, eb- and
   b-structures agree, $L_\Box\in\mathrm{Diff}^2_{\mathrm b}$ with principal symbol $\rho_IG_{\mathrm
   b}\otimes\mathrm{Id}$ up to $O(\rho)$, and $E\in\rho_0^2\mathrm{Diff}^1_{\mathrm b}$ is a bounded first-order
   b-operator, absorbed by the exponential weight in $\tau$ (or $\tau'$) as IV':163-164 and IV'' Lemma 2.2 (IV'':173-175)
   absorb the system's first-order terms. $\tau'$ is a b-time function for every weight (Lemma R4.1 (d)). IV'' Lemma 2.2
   at $\Box$, with zero data and the source $F$ (which it does not ask to vanish near $\Sigma_{\mathrm{IVP}}$), gives
   $Z$ on $\Omega_N$.
4. *The gluing: IV'' Theorem 2.4 Steps 1-3 and Lemma 2.3 at $\Box$*, verbatim with 2 and 3: the cut-off $\hat
   \chi_N(\tau')$ of Step 2, whose commutator lives where $\rho_I\ge\frac12$ (so any $\mathscr I^+$-weight is met);
   then Lemma 2.3, away from $\mathscr I^+$ by step 3, and near it the forward problem for $u_2 = u-\chi_cu_1$, with
   the first-order b-commutator $[L_\Box,\chi_c]$ supported in $\{\frac c4\le\rho_I\le\frac c2\}$, by step 2.
5. *The slab: IV''' Theorem 2.1 (i)-(iii) at $\Box$.* Its three changes are: the gauge cut-off, absent for $\Box$; the
   background, here $g_{b_0}$ itself ($S = 0$), for which IV''' Lemma 0.1 is III.C Lemma 3.5's form of $g_{b_0}-\eta$,
   and Lemma R4.1 holds in the translated chart as $g_{b_0}$ is stationary (IV''':33-37); the regions, whose curves
   (IV''' Lemma 1.1) are statements about $g_{b_0}$, $t^\flat_*$, $t_{\mathrm{IVP}}$ and $\rho'_I$ alone. The compact
   parts ($\mathcal K$, and $\mathcal S\cap\{\rho'_I\ge\frac{c_1}4\}$) use the standard energy estimates for a linear
   wave equation with principal symbol $g^{-1}(\zeta,\zeta)\mathrm{Id}$ (IX Lemma 2.1 (a)) on compact domains of
   dependence; on $\Omega^\natural_{c_1}$, step 2 with $\Sigma_{\mathrm{in}} = \{\rho'_I = c_1\}$ and
   $\Sigma_{\mathrm{fin}} = \{t^\flat_* = \hat T+3\}$, spacelike for $g_{b_0}$ (K:31-33). Uniqueness on each region:
   II.F Lemma 1.3.
6. *What does not carry over, and is not used.* The recovery of the sharp weight at $\mathscr I^+$ (IV'' Theorem 2.4
   Steps 4-6) integrates each slot along $X_I$ and $X_0-X_I$; with $\bar A = 0$ every Cartesian component would be
   integrated as slot 6 is, and Lemma 1.2 (c) there needs $a_0>\gamma$. Theorem R4.3 needs only the estimate (R4.2).
$\square$

**Theorem R4.3 ((Ext$\Box$) holds; deduced from Proposition R4.2 and the readings below; computed E6).** Let $q_{\dot
h} := \min(\min\mathrm{Re}\,\mathcal E_0,\ell_0)$, so that $q_{\dot h}>\frac32+2\gamma_\Upsilon$ ($\min\mathrm{Re}\,
\mathcal E_0>\frac32+2\gamma_\Upsilon$ and $\ell_0>3$, K:54-57). For every $\beta\in(0,\delta_\sharp)$ and every $p$ with
$$\tfrac12+\beta<p<\min\big(\tfrac32,\ q_{\dot h}-1\big),$$
the Cartesian components of $Z_1$ (round 3's (Ext$\Box$)) and all their b-derivatives are $O(\rho_I^p)$ near
$\mathscr I^+$ on $N^+\cap\{2\le t^\flat_*\le3\}$, with constants bounded by finitely many norms of the data. The
interval is not empty: $q_{\dot h}-1>\frac12+2\gamma_\Upsilon\ge\frac12+2\delta_\sharp$. With only the statement-level
exterior weight $\ell^\flat_0 = \frac32+\frac12\delta_\sharp$ of III.C' Theorem 3.1 in place of $q_{\dot h}$ (C':135-137,
VIII:145-147) the same holds for $\beta\in(0,\frac12\delta_\sharp)$.

*Proof.* (1) *The source on the past of the slab.* In the class $S' = 0$ (VIII:314-316), so $\dot g = \dot h$ on
$\mathcal D' = \mathcal D\setminus\{t^\flat_*\ge\hat T+\frac74\}$ (VIII:60-62, 220), and $\dot\Upsilon^\natural(\dot g)
= 0$ there (VIII:240 at $S' = 0$). As $\dot\Upsilon^\natural = -\Theta-\chi^\natural_0E^\Upsilon G$
(R2.10 with the cut-off, as in Theorem R3.4 (ii)'s proof) and $\chi_K = 0$ on $\{t^\flat_*<T_K\}$, $T_K>\hat T+3$
(K:35-37), (R3.2) gives $F_Y = \chi^\natural_0E^\Upsilon G\dot h$ on $N^+\cap\{t^\flat_*<\hat T+\frac74\}$, which
contains $\{t^\flat_*\le\frac72\}$ ($\hat T\ge2$). Let $\chi_3\in C^\infty(\mathbb R)$ equal 1 on $(-\infty,3]$ and 0 on
$[\frac72,\infty)$, and $F' := \chi_3(t^\flat_*)F_Y$, a smooth 1-form on $\mathcal D^+$. As $dt^\flat_*$ is past
timelike (K:31-33), $N^+\cap\{t^\flat_*\le3\}$ is closed under past causal curves in $N^+$; so the solution $Z'$ of
$\Box Z' = F'$ on $\mathcal D^+$ with zero data equals $Z_1$ there (II.F Lemma 1.3; the extension across
$\Sigma^\circ$ is immaterial by Lemma R3.1).
(2) *Support.* Near infinity, on $\{\tau'<\frac18\}$, $t_{\mathrm{IVP}}<\frac r8$ and $t_* = t_{\mathrm{IVP}}-F(r)\le
\frac r8-\frac r4<0$ for $r\ge R_6$ (K:42-47), so $\chi_\natural(t_*) = 0$ and $\chi^\natural_0 = \chi_0 = 0$ (K
Lemma 1.1 (c) and its proof at K:85-86). And $\chi^\natural_0 = 0$ near $\Sigma_{\mathrm{IVP}}$ (K Lemma 1.1 (d)). So
$F'$ vanishes near $\Sigma_{\mathrm{IVP}}$ and, near infinity, on $\{\tau'<\frac18\}$; Proposition R4.2 does not ask
it, but it places the source's $I_0$-tail in $\{\tau'\ge\frac18\}$, the region of IV'' Lemma 2.3.
(3) *Weights* (READ and deduced; E6 for the arithmetic). On $\Omega_{\mathrm{ext},r_1}$ and $\mathcal S$, $\dot h\in
H^{\infty,(\mathcal E_0,\ell_0),\langle\mathcal E^C_I\rangle,\ell_I}_{\mathrm b}$ (VIII:170-178, by III.C' Theorem
3.1's proof and IV''' Corollary 2.3): conormal with joint orders $q_{\dot h}-$ at $I_0$ and, at $\mathscr I^+$, above
$\ell^\flat_I$ in every slot but $\slashed\pi_0$, which has $\frac32$ (C':31-37). $E^\Upsilon_{g,\infty}$ is
$|x|^{-1}$ times coefficients smooth on $M$ (III.B (6.1)), and does not see $\slashed\pi_0$ (S1); $\chi^\natural_0$ and
$\chi_3(t^\flat_*)$ are smooth on $M$ near infinity (K Lemma 1.1 (a); $t^\flat_*$ is smooth near $\mathscr I^+$,
K:34-35). So $F'$ has $I_0$-order $q_{\dot h}+1$ and $\mathscr I^+$-order $\ell^\flat_I+1$, and $f'_\flat :=
\rho_I\rho^{-7/2}F'\in H^{m,(a_0,2\alpha_I)}_{\mathrm b}$ for every $m$, every $a_0<q_{\dot h}-\frac52$ and every
$\alpha_I<\ell^\flat_I-\frac32$ (the shifts of IV'' (0.2): $\rho_I\rho^{-7/2} = \rho_0^{-7/2}\rho_I^{-5/2}$). (Without S1
the $\mathscr I^+$-weight would be $0-$, still above every $\alpha_I<0$.)
(4) *The estimate.* Fix $a_0<q_{\dot h}-\frac52$ with $p-\frac32<\min(a_0,0)$ and put $\alpha_I := p-\frac32$; then
$\alpha_I<\min(a_0,0)$, and Proposition R4.2 gives $u = \rho^{-3/2}Z'\in H^{(1;m),(a_0,2\alpha_I)}_{\mathrm{e,b;b}}(
\Omega^\natural_{c_1})$ for every $m$. By b-Sobolev embedding (IV (0.1)), $V^ju = O(\rho_0^{a_0}\rho_I^{\alpha_I})$ for
b-vector fields $V$ and $j\le m-3$; as $V\rho^{3/2}\in\mathbb C\rho^{3/2}$, $V^jZ' = O(\rho_0^{3/2+a_0}\rho_I^{p})$. On
the slab $\rho_0$ (equivalently $\rho'_0$) is bounded above and below (IV''':24-28), and away from $\mathscr I^+$ there
is nothing to show. The constraints are E6's: $\alpha_I>\beta-1$ is $p>\frac12+\beta$, $\alpha_I<a_0$ is $p<q_{\dot
h}-1$, $\alpha_I<0$ is $p<\frac32$. $\square$

*Why the order is $\min(\frac32,q_{\dot h}-1)$ and not $\frac32$.* The radiation field has order $\frac32$ (Lemma R4.1
(c)), and on the slab, away from $I_0$, that is what $Z_1$ has where the recovery of step 6 applies. The energy
estimate reaches the slab through the corner $I_0\cap\mathscr I^+$, where the multiplier needs $\alpha_I<\alpha_0$
(Lemma R4.1 (e)); the source's $I_0$-weight is one above $\dot h$'s only because $c_\Upsilon$ carries $|x|^{-1}$, and
without that factor the interval of Theorem R4.3 would be empty (E6 control (ii)).

**Corollary R4.4 (the harmonic gauge on all of $N^+$: Proposition R3.6 without its hypothesis; deduced).** With $Z :=
\dot\mu\chi_KW^{**}_H+Z_1$ and $\dot g_H := \dot g+\mathcal L_Zg$ on $N^+$: $\dot g_H$ is $G$-invariant, $D\mathrm{Ric}(
\dot g_H) = 0$, $\Theta(\dot g_H) = 0$ on all of $N^+$, $\dot g_H$ induces $(\dot\gamma,\dot k)$ exactly, and on each
$\{r_0<r\le R',\ t_*\ge T'\}$, with the derivatives of (R2.2) as amended by (A12),
$$\big|\dot g_H-\dot\mu K^*-c_\infty\mathcal L_{W^*}g\big|\le Ct_*^{-1/2},\qquad c_\infty = \frac1{4\pi^2}\int\ell\big(
\chi'J_h+[\Box,\chi']Z_1\big)\,dv,$$
a horizon charge; for $Y_h$ with $\Box Y_h = 0$ and compactly supported data on $\Sigma^\circ$, $\dot g_H+\mathcal
L_{Y_h}g$ has the same properties with $c_\infty+Q[Y_h]/4\pi^2$, the data changed by those of $\mathcal L_{Y_h}g$.

*Proof.* Proposition R3.6, whose hypothesis (Ext$\Box$) is Theorem R4.3, with the slab commutator of S5 as corrected
by (A25) (T1) and the uniqueness sentence of (A29); the last clause (Theorem R3.4 (iv)) by Corollary R4.6 below, not by
round 3's argument ((A23)). $G$-invariance of $Z_1$: Lemma R3.1's consequences. $\square$

**Corollary R4.6 (Corollary R2.8 repaired: homogeneous solutions with data compactly supported on $\Sigma^\circ$;
deduced).** Let $Y$ be a smooth 1-form on $N^+$ with $\Box Y = 0$ whose Cauchy data on $\Sigma^\circ$ have compact
support. Then $Q[Y]$ is constant at late times, and on each $\{r_0<r\le R',\ t_*\ge T'\}$, $|Y-(Q[Y]/4\pi^2)W^*|\le
Ct_*^{-1/2}$ with the derivatives of (R2.2) as amended by (A12). Near $\mathscr I^+$ on $N^+\cap\{t^\flat_*\le\hat T+3\}$
the Cartesian components of $Y$ and all their b-derivatives are $O(\rho_I^p)$ for every $p<\frac32$.

*Proof.* (1) *$\mathscr I^+$.* Let $\Upsilon$ be a smooth compactly supported 1-form on $N^+$ with $Y$'s Cauchy data on
$\Sigma^\circ$. Then $Y-\Upsilon$ has zero data and $\Box(Y-\Upsilon) = -\Box\Upsilon$, compactly supported, so
$\rho_I\rho^{-7/2}\Box\Upsilon$ lies in every weighted space and Proposition R4.2 applies with every $a_0$; with $a_0>0$
and $\alpha_I = p-\frac32<0$, b-Sobolev embedding as in Theorem R4.3's step (4) gives the order $p$; $\Upsilon$ vanishes
near infinity. (2) *The slab.* With $\chi$ of Lemma R3.5, $\chi(t^\flat_*)Y$ solves $\Box(\chi Y) =
[\Box,\chi(t^\flat_*)]Y$, supported in $\{2\le t^\flat_*\le3\}$ and meeting $\partial M$ only at $\mathscr I^+$, of
$\mathscr I^+$-order $p+1$ (S5 as corrected, T1). Fix $\beta\in(0,1)$ and $p\in(\frac12+\beta,\frac32)$: the source lies
in II.F$'$ (1.4) (S7), with (1.3) for $\Box$ ($\bar S = 0$, Lemma R3.5's proof), and II.F$'$ Theorem 1.1 gives its
forward solution, which is $\chi(t^\flat_*)Y$ by (A29). (3) *Late times.* As in Theorem R3.4 (iii)'s proof: $\chi'Y$
solves $\Box(\chi'Y) = [\Box,\chi']Y$, a source supported in $\mathrm{supp}\,d\chi'$ (a compact set and a cone in
$(\iota^+)^\circ$), in Theorem R2.5's class by S6 and II.F$'$'s weights; Theorem R2.7 gives $|\chi'Y-c(t_*)W^*|\le
Ct_*^{-1/2}$, and for large $t_*$, $d\chi' = 0$ near the horizon, so $c$ is constant, equal to $Q[\chi'Y]/4\pi^2 =
Q[Y]/4\pi^2$ there ((2.1) and $\Box Y = 0$). $\square$

*What this repairs* (the round-3 verifier's major finding, (A23)). Round 2's R2.8 took data compactly supported on a
slice $\{t_* = t_0\}$ and asserted that $[\Box,\chi(t_*)]Y$ is compactly supported. It is not: the slab $\{t_0\le t_*\le
t_0+1\}$ reaches $\mathscr I^+$, outgoing null rays from a compact set reach $\mathscr I^+$ after a finite
$t_*$-increment, and in $4+1$ dimensions there is no Huygens principle, so $Y$ does not vanish near $\mathscr I^+$ on
that slab. The source then lies in Theorem R2.7's class only through an $\mathscr I^+$-estimate for $\Box$ on a bounded
slab, which is Proposition R4.2. The status of the items that used R2.8:
- R2.8 with data on a slice $\{t_* = t_0\}$: not proved (its proof fails); not used anywhere, once read as Corollary
  R4.6.
- R2.12 (iv), and Corollary R3.3's (iv): hold, for $Y_h$ with data compactly supported on $\Sigma^\circ$ (Corollary
  R4.6).
- R2.13 (b): its proof is "Corollary R2.8 for $Z'_0$", so it used the failed step; it holds for $Z'_0$ with data
  compactly supported on $\Sigma^\circ$ (Corollary R4.6). That is the form in which the supplement (10.2 (iv), 10.8) and
  the paper (section 8.2) cite it: their rate $t_*^{-1/2}$ stands, with Corollary R4.6 added to the citation.
- Theorem R3.4 (iv): holds, by Corollary R4.6 in place of its proof's last sentence.
- Proposition R3.6, that is Corollary R4.4: holds without condition, (iv) included.

*Hypotheses.* None beyond the write-out's proved parts at $b_0$. (Dyn) is Part VI.A Theorem 6.1 (VIA:303-309, proved
D318), stated for every operator with principal symbol $G\,\mathrm{Id}$. (H$'$7) asks that II.F$'$'s orders lie in
III.H$'$'s class $\mathcal O_c$ (H':509-511, 67); for $L$ this is III.I Lemma 5.1 (I:338-357), whose proof uses the
construction of II.C Proposition 5.1 and the Hamilton flow of $G_0$, and of the operator only the constants $s_{\mathrm
{in}}$, $s_{\mathrm{out}}$, which it does not constrain; so it holds for $\Box$'s orders as well (deduced). II.C
Definition 2.7 (1)-(2) for $\Box$ are III.D Lemma 5.2 and Lemma 7.1 ((A18)). See (A16).

*The indicial data, collected.* $\mathscr I^+$: roots $\{0,a\}$ in every Cartesian component; order $\frac32$ (a
radiation field) in all five components, against $\frac32+\bar A_{jj}$ for $L$'s slots. $I_0$: no root restricts the
weight. Corner: $\alpha_I<\min(\alpha_0,0)$. On the slab: $p<\min(\frac32,q_{\dot h}-1)$, asked $p>\frac12+\beta$. At
zero energy (section R4.b): $L_1r^{-q} = -2(q-\frac32)r^{-q-1}$, $l = 0$ roots $\{0,2\}$, first non-smooth term
$\sigma^2\log\sigma$.

### R4.b The rate: the first obstruction

Not improved. Theorem R3.4 (iii) and Corollary R4.4 keep $t_*^{-1/2}$. What a better rate needs, and where it stops:

**Proposition R4.5 (the rate; computed G1-G4; (a)-(b) deduced, (c) formal).**
(a) *Zero energy is not the obstruction.* Near $\partial X$, with the outgoing time $t_* = t-r$ and on Cartesian
components (Lemma R4.1), $\hat P(\sigma) = \hat P(0)-i\sigma L_1$ at $\mu_0 = 0$ with $L_1 = 2\partial_r+\frac3r$ and no
$\sigma^2$ term ($dt-dr$ is null for $g$; III.B's $t_*$ adds $L_2\in\rho^2C^\infty$, round 2's B1), and $L_1r^{-q} =
-2(q-\frac32)r^{-q-1}$ (G1; control: in the static time the $\sigma$-linear term vanishes). $\hat P(0) = -\Delta$ has the
indicial roots $\{-l,l+2\}$ (G2). For compactly supported $f$ the formal expansion of $\hat P(\sigma)^{-1}f$ is $u_0 =
mr^{-2}$, $u_1 = -imr^{-1}$, and the $\sigma^2$ equation has the source $mr^{-2}$ at the $l = 0$ root 0: no power solves
it, $-\frac m2\log r$ does (G2; control: at $n = 3$ the chain stops, $L_1u_0 = 0$). The free kernel confirms it: its
$\sigma^2\log\sigma$ coefficient is $-\frac1{8\pi^2}$, independent of $r$, which is $-\frac m2$ at $m = \frac1{4\pi^2}$
(G3; control: the $n = 3$ kernel has no logarithm). So the first non-smooth term at zero energy is two orders above the
pole: the resolvent's structure at zero energy does not block a first improvement of $t_*^{-1/2}$.
(b) *What a rate $t_*^{-1/2-\kappa}$ needs.* Theorem R2.5 (i)-(ii) at $K^+$-weight $\kappa>0$ for the source class,
which by Lemma R2.6 gives $t_*^{-1/2-\kappa}$. The source side, computed (G4): a cone source of $\iota^+$-order $a$ and
fast $K^+$-decay lies in the $L^2$-in-time class with $K^+$-weight $\kappa$ and sf-weight $\beta$ iff
$a>\beta+\frac52+\kappa$ (round 2's B7 at $\kappa = 0$); its time-Fourier transform is bounded pointwise in $\sigma$, in
the zero-energy weight, iff $a>\beta+3$ ($|\hat F(\sigma,x)|\le\frac{4^{1-b}}{b-1}r^{1-a}$). The harmonic-gauge source
has $a = \lambda_\sharp+1-\eta = \frac52+\delta_\sharp-\eta$ (Proposition R3.2), so the first holds iff $\kappa<
\delta_\sharp-\beta-\eta$, and the second, which with III.H Theorem 4.1 (3)'s symbol bounds (R2.4) would give
$t_*^{-1}$, fails, as $\delta_\sharp<\frac14$ (I10:45-46). The commutator term $[\Box,\chi']Y$ of Theorem R3.4's
proof lives on a cone in $(\iota^+)^\circ$, where $t^\kappa\sim r^\kappa$ costs $\kappa$ of the same room.
(c) *Formal: the true rate of Theorem R3.4's representative.* The quasi-stationary response at a fixed point to the
cone tail is $\int_1^{t/4}r'^{-2}\,r'^{-a}(r'/t)^br'^3\,dr'\sim\frac{4^{a-b-2}}{b+2-a}t^{2-a}$ for the $l = 0$ kernel
$r'^{-2}$, and $\sim t^{-a}$ for the $l = 2$ kernel $r'^{-4}$ (G4; control: the $l = 0$ exponent is not $-a$). At
$a = \frac52+\delta_\sharp$ the $l = 0$ part is $t^{-1/2-\delta_\sharp}$. It reaches the metric: near compact sets
the response is $\phi(t)(\partial_v)^\flat+\psi(t)W^*$, the two bounded stationary $l = 0$ solutions smooth at the
horizon (round 2's B5), and the charge fixes $\mu_0\phi+\psi = c_f$ ($Q[(\partial_v)^\flat] = 4\pi^2\mu_0$, $Q[W^*] =
4\pi^2$, Lemma 2.2 (b)), so $\psi-c_\infty\approx-\mu_0\phi$ and $\dot g_H-\dot\mu K^*-c_\infty\mathcal L_{W^*}g$ carries
$-\mu_0\phi\,\mathcal L_{W^*}g$. Not proved: that the $l = 0$ time component of the $\lambda_\sharp$-term of $J_h$ is
nonzero, and the model itself.

*The first obstruction, precisely.* Theorem R2.5 at positive $K^+$-weight for $\Box$, that is III.H$'$'s time-domain
argument with $t_*^\kappa$ weights, is not written. Its frequency-side input is in place (R2.4: III.H Theorem 4.1 (3) at
$\Box$, the uniform bounds on $(\sigma\partial_\sigma)^j\tilde P(\sigma)^{-1}$), and (a) shows nothing at zero energy
that would stop it below the source's limit. What it can buy for Theorem R3.4's representative is bounded by the gauge
source's $\iota^+$-order, $\kappa<\delta_\sharp$ ((b)), the constraint damping's margin, and (c) indicates that this
bound is the true rate there. For a representative whose $l = 0$ gauge part has compactly supported data (Proposition
R2.13 (b)) the source has no $l = 0$ part, and the model gives the $l\ge2$ response $t^{-a}$: there the operator side,
not the source, is the first obstruction.

### R4.c Amendments: the verifiers' findings on rounds 2 and 3

*The round-2 verifier's findings.* The independent verifier of round 2 (relayed by the main session on 2026-11-02)
found R2.0-R2.4 and R2.V sound and re-derived R2.13's computations. Its findings are seated below. Its scripts are not
in this repository; nothing here depends on them.

*Already covered by round 3.* Of M1 (the domain, D610):
- solving Proposition 2.1 on $\Omega^\sharp$ with $F$ an extension of $-\Theta(e)|_{N^+}$, and reading $\dot g_H$ on
  $N^+$: (A3)-(A4) and Lemma R3.1;
- "$G$-averaged": not needed; Lemma R3.1's consequences give $G$-invariance on $N^+$ for every extension, an averaged
  one among them;
- "$l = 0$ part removed": on $N^+$, $-\Theta(e)$ has none (Proposition 2.1 (c)), and the extension's $l = 0$ part below
  $\Sigma^\circ$ does not reach $N^+$ (Lemma R3.1);
- Theorem 1.5 (d) on $\Omega'_+$ with $U\subset U^\sharp$ $SO(4)$-invariant: (A2) (d);
- Corollary 2.6: (A6); R2.0's second bullet: (A4) with (A6) ($d\phi_2$ is defined on $M^\circ$, and Proposition 2.1 (a)
  is read on $N^+$);
- R2.13 (a)-(c), "of Proposition 2.1 (a)" (line 811): (A4), which reads Proposition 2.1 (a) on $N^+$.
Not covered, and seated: Proposition 2.1 (b)'s invariant $U$ (A9), the slab of R2.8 and R2.13 (b) (A10), the local
$N^\circ$ (A11).

(A9) *M1, Proposition 2.1 (b) (lines 226-228), as read by (A4).* (A4) reads (b) on $\Omega'_+$, $U\subset U^\sharp$,
but drops the invariance of $U$. Read "$U\subset U^\sharp$ open and $G$-invariant". The gauge vector $Y$ of
$\dot g'-\dot g_{\mathrm{RW}} = \mathcal L_Yg$, and so $Z' = Y-\dot\mu W^{**}_H$, is $G$-invariant on a $G$-invariant
domain (IX Corollary 2.3 and Remark 2.4 (c), now IX:292-306 and 318-331, as (A2) (d) uses them; IX:326: "$G$-invariant
(for instance $U = U^\sharp$ ...)").

(A10) *M1, Corollary R2.8 (lines 632-641) and Proposition R2.13 (b) (lines 820-823).* R2.8 takes $\{t_*\ge t_0,\
r\ge r_0\}$, whose side $\{r = r_0\}$ is not in $M^\circ$, and for $t_0<0$ the slab leaves $N^+$. The verifier proposed
data on $\{t_* = t_0\}\cap\{r\ge r'_0\}$, $t_0\ge0$, $r'_0\in(r_0,r_h)$; that places the slab in $N^+\cap M^\circ$
($t_*\le t_{\mathrm{IVP}}$, K:42-44) with a spacelike side $\{r = r'_0\}$, but it does not save R2.8's proof, which the
round-3 verifier found fails on any such slice ((A23)). Read R2.8 as Corollary R4.6 (data compactly supported on
$\Sigma^\circ$, the solution on $N^+$), and R2.13 (b) with $Z'_0$'s data compactly supported on $\Sigma^\circ$. (A7)
recorded that R2.8 and R2.13 do not use $N^\circ$ or $N^{\mathcal D}$; it did not place the slab.

(A11) *M1, the local $N^\circ$ (line 150).* Theorem 1.5's "$N^\circ := N\cap\{r>r_0\}$" is round 1's own symbol, not
Part IX's withdrawn $N^\circ$. IX:364-365's rule (a text citing $N^\circ$, $N^{\mathcal D}$ reads $U^\sharp$,
$\Omega^\sharp$, $N^+$) does not apply to it: read mechanically it would put $U^\sharp = M^\circ\cap\{t_{\mathrm{IVP}}>
-1\}$, which reaches below $\Sigma^\circ$, into Theorem 1.5. Write it $N_{r_0} := N\cap\{r>r_0\}$; Theorem 1.5 (a)-(c)
are read on $N^+$ and proved on $\mathrm{int}\,N\cap M^\circ$ as (A2) states, and (d) as (A2) (d) states.

(A12) *m1, Theorem R2.7's derivatives (lines 603-605 against step (5), lines 621-624).* The statement claims $k-1$ powers
of $t_*\partial_{t_*}$; step (5) bounds $\partial_{t_*}$. Read "with $j$ derivatives in $x$ and $k-1$ of
$\partial_{t_*}$". That is all R2.12, R2.13, R3.4 and Corollary R4.4 use: $\partial^i_{t_*}(\beta-c_f) = (\partial^i_t
\chi_K)*B-\partial^{i-1}_{t_*}\ell(f)/4\pi^2$, the first bounded by $\sup|B|$ over a bounded window, the second by
Lemma R2.6 applied to $\ell(f)$, whose $(t\partial_t)^j$ are square integrable for $j\le k$. The $t_*\partial_{t_*}$
version also holds for $k\ge2$, by $t\partial_t(\beta-c_f)|_{r_h} = -t\partial_tQ[u']/4\pi^2+r_ht\partial_t\partial_r
\beta$ (the verifier's identity, from step (4)); it is not used.

(A13) *m2, round 1's "modulo $\mathcal L_{W^*}g$" (lines 237-239) and "the stationary freedom is exactly $\mathcal
L_{W^*}g$" (lines 366-368; (GD4), lines 384-386).* Both hold for gauge vectors with decaying data, in III.D$'$'s space
$\mathcal X_0$, and are false without it: $d\phi_l$ (R2.0) gives further stationary harmonic-gauge freedom at every even
$l\ge2$, and $d\Psi$ (R2.13 (c)) exchanges the linear growth for a stationary term that does not decay. Read both with
"for gauge vectors in $\mathcal X_0$ (decaying data)".

(A14) *m3, R2.S (S3) (lines 883-885).* "For $W'$ with compactly supported data this is proved at the rate ... (...,
deduced, assuming (Dyn)); the rate here remains a deduction" contradicts itself. Replace from "For $W'$" to
"deduction." by: "For $W'$ with compactly supported data GAUGEDECAY5 Proposition R2.13 (b) gives the rate $t_*^{-1/2}$ on
each $\{r\le R\}$ (deduced, with (Dyn), which Part VI.A Theorem 6.1 proves at $b_0$)." This is the wording the
supplement now carries (READ, `N1STAR-PROOF.md`:2938-2940).

(A15) *m4, R2.S (S4) (lines 893-895).* "whose gauge vector has compactly supported data" must mean $Z'_0$ in $(\dot
g_H)_0 = \dot\mu K^*+\pi_{Z'_0}$: the gauge vector measured from Part VIII's solution contains $\dot\mu W^{**}_H$, never
compactly supported ($rA\to\frac12$, S8). Replace "the spherically symmetric part of a perturbation whose gauge vector
has compactly supported data settles" by "the spherically symmetric part of a perturbation is $\dot\mu K^*+\pi_Z$ with
$\Box Z = 0$, and when $Z$ has compactly supported data it settles". (The paper's present text at
`paper/RESPONSE-HL-5D.md`:805-807 already has this form; the main session carries m4 there.)

(A16) *m5, (Dyn) and (H$'$7).* Everything in rounds 2-4 is at $b_0$, where (Dyn) is proved (Part VI.A Theorem 6.1,
VIA:303-309; proved D318), for every operator with principal symbol $G\,\mathrm{Id}$, so for $\Box$ and $L_{b_0}$. Read
the following without the assumption, citing that theorem instead: R2.V (n1) (lines 782-783), R2.S (S1) (line 866), (S3)
(line 884, now (A14)), the labels of R2.6 (line 941), Corollary R3.3 (lines 1135-1136), Theorem R3.4's heading (line
1194), R3.5 item 3 (lines 1281-1282), R3.6's labels (lines 1309-1310) and the proposed replacement of round 3
(lines 1320-1322, "with the horizon and trapping hypotheses ... one order condition it carries"). (H$'$7) is not an
extra hypothesis either: for $\Box$ at $b_0$ it is met as for $L$, by III.I Lemma 5.1's proof (Corollary R4.4,
*Hypotheses*). It would be one for $b\ne b_0$, where (H$'$7) also asks III.H$'$ (H$'$3)'s bound $k\le K$ (H':511-513);
nothing here is at $b\ne b_0$. Read Theorem R3.4, Corollary R3.3 and R3.5 item 3 without (H$'$7) at $b_0$.

(A17) *n1, R2.1's regularity (line 486).* Take $s>\frac52$, not $s>\frac32$: R2.3's injectivity uses III.D$'$'s density
step (lines 517-518), which needs $s>\frac52$, the threshold III.D Lemma 5.1 gives ($s_c>\frac32+\vartheta_{\mathcal H}$,
as R2.5's proof itself records, line 567).

(A18) *n2, Theorem R2.5 (iii)'s "1-admissible" (lines 556-559).* R2.5 proves II.C Definition 2.7 (3) (IIC:337-345).
Items (1) and (2) are: (1) trapping admissibility, III.D Lemma 5.2 at $\gamma_\Upsilon = 0$ (D:289-292); (2)
tf-admissibility with the weight $\alpha_{\mathrm{sf}}+2\in(0,1)$, III.D Lemma 7.1 at $\gamma_\Upsilon = 0$, whose gap
is $(0,2)$ when $e_\Upsilon\gamma_\Upsilon^2 = 0$ (READ, D:439-442: "with $(0,2)$ when $e_\Upsilon\gamma_\Upsilon^2 =
0$"). With these, "1-admissible" in R2.5 (iii) is as stated.

(A19) *n3, headings.* The section headings R2.1-R2.6 (lines 478, 541, 593, 660, 899, 913) collide with Definition R2.1,
Lemma R2.2, Proposition R2.3, Theorems R2.4-R2.5 and Lemma R2.6, and round 3's R3.1-R3.6 (lines 986, 1083, 1146, 1267,
1274, 1285) with Lemma R3.1-Proposition R3.6. Read the headings as sections R2.a-R2.f and R3.a-R3.f in order; every
citation "R2.n" or "R3.n" in rounds 2-4 means the numbered statement unless it says "section". Round 4's headings are
lettered.

(A20) *n4, Theorem R2.7's window (lines 603, 614-621).* For $t_*\ge4\max(R',1)$ the convolutions $\psi*B$ and $\partial_t
\chi_K*B$ can reach $B$ near $t = 0$. That is harmless: $B = \mathcal F^{-1}(\chi\hat b_1)$ with $\chi$ compactly
supported is band-limited and bounded, $|B|\le\|\chi\hat b_1\|_{L^1}\le C\|f\|$; on $t_*\ge8\max(R',1)$ the window lies
in $[t_*/2,t_*]$ and Lemma R2.6 gives $t_*^{-1/2}$, and on the bounded range between, $C\|f\|\le C't_*^{-1/2}\|f\|$.

(A21) *n5, V4's claims (`checks/gdrepair5.py`:189-215).* V4 prints True for the claims R3d, R3e, R3f, H2 and R5
without computing them; only their controls are computed there. The claims are computed elsewhere and V4's entries are
records of those: R3 (d) at `checks/rwgauge5.out`:12, R3 (e) at :13-16 (quadrature to 40 digits, $j = 1,\dots,4$),
R3 (f) at :17, R5 at :31, H2's $l = 2$ claim at `checks/hgauge5.out`:5. Read V4's claim column as recorded from those
lines.

(A22) *n7, R2.6's order (lines 915-935).* The findings are printed GD5, GD6, GD7, GD9, GD10, GD8; read them in the order
GD5-GD10.

*The round-3 verifier's findings* (relayed 2026-11-02; its scripts are not in this repository, and nothing here
depends on them).

(A23) *Major: Theorem R3.4 (iv) (lines 1210-1212, proof lines 1229-1230) and Corollary R2.8's proof (lines 636-638).*
"$Y_h$ has compactly supported data on every later slice (finite speed of propagation)" and "$[\Box,\chi(t_*)]Y$ is
smooth with compact support" are false: the slices $\{t_* = t_0\}$ reach $\mathscr I^+$ (F2 (1.1)); outgoing radial null
rays from $\{r\le r_K\}$ reach $\mathscr I^+$ after a $t_*$-increment $O(\mu_0/r_K)$ (in III.B's coordinates near
infinity these rays have $dt = d|x|$, IX:157 giving $g^{-1}$, and $t_* = t-\psi$, $\psi' = 1-8\mu_0|x|^{-2}$, so the
increment is $8\mu_0/r_K$; the verifier's $9\mu_0/r_K$ is the static-time count); and in $4+1$ dimensions there is no
Huygens principle, so $J^+(K)$ meets every such slice out to $\mathscr I^+$ with $Y_h\ne0$ there. Repaired by Corollary
R4.6, which supplies the $\mathscr I^+$-estimate on a bounded slab from Proposition R4.2; the status of R2.8, R2.12 (iv),
R2.13 (b), Corollary R3.3, Theorem R3.4 (iv) and Proposition R3.6 is listed after Corollary R4.6. All hold without
condition in the form with data compactly supported on $\Sigma^\circ$; R2.8 with data on a later slice is not proved.

(A24) *Stale Part IX citations (lines 988-995, 1019-1020, 1030, 1038, 1044, 1049, 1059-1060).* Part IX moved at D611.
Read IX:131-134 as 139-142, 209-216 as 218-225, 231-234 as 240-243, 253-277 as 262-279, 279-293 as 292-306, 312-317 as
318-331, 96-99 as 104-108, 350-351 as 364-365 and 312-314 as 326 (spot-checked: IX:139-142 is Lemma 1.2, IX:326 the
$G$-invariance of $U^\sharp$, IX:364-365 the withdrawal of $N^\circ$, $N^{\mathcal D}$). Line 1060's "the repair's second
reading is not recorded there" is out of date: IX:365 records D611's reading ("The verifier of the repair (D611) found
no major gap").

(A25) *$t^\flat_*$ in Proposition R3.6's proof (lines 1250-1251) and in S5.* $t^\flat_*$ is not $t_*+\kappa/r$: II.C
Lemma 3.2 (a) with $\ell = \frac12$ (I:31) gives $t^\flat_* = t_*(1-(t_*/r)^{1/2})$ near $\mathscr I^+$, smooth in $x_I$
and equal to $t_*$ at $\mathscr I^+$. T1 re-runs S5 with it: $r^{p+1}[\Box,\chi(t^\flat_*)]Z$ is finite at $p = \frac32$
and $p = 1$, so one order is gained at $\mathscr I^+$, exactly one at $p = 1$ ($r^{p+3/2}$ of it is not finite; at $p =
\frac32$ the leading term carries the factor $3-2p = 0$, the verifier's observation); control: the static time gains
nothing. Read lines 1250-1251 as "$t^\flat_* = t_*(1-(t_*/r)^{1/2})$ near $\mathscr I^+$ (II.C Lemma 3.2 (a), $\ell =
\frac12$), and $[\Box,\chi(t^\flat_*)]$ gains one order at $\mathscr I^+$ (S5 as re-run in T1)". The conclusion stands.

(A26) *K3 and K5 (line 1140).* K3 checks $A_1$'s and $A_2$'s gain for class 1-forms at $q\in\{3,\frac72\}$, while K2
applies it at $q = \sigma_\tau-K$ (negative values among them) and to the rows s1, v1 and the rotation rows, which are
not class objects. T2 runs K3 with $q$ a symbol: the gain holds for every $q$ (control: $c_\Upsilon = dt$). For the rows
outside the class K5 is needed, not "not needed above": in the class those rows vanish (K5), and the rows that remain
(s0, s2, c0) are class 1-forms, to which T2 applies. Read line 1140's "(K5; not needed above)" as "(K5; needed for
Proposition R3.2 in the class, as it removes the rows to which K3 does not apply)".

(A27) *$\gamma_\Upsilon = 0$ (lines 971-972, 1137-1138, 1295, and K4's second control).* The write-out's range is $0<
\gamma_\Upsilon<\frac14$ (I10:45-46); the statements "at $\gamma_\Upsilon = 0$ there is none" and "the room is the
constraint damping" at $\gamma_\Upsilon = 0$ are outside it. Label them heuristic: they say what the inequalities give
when $\gamma_\Upsilon$ is set to 0, not what the write-out proves there.

(A28) *"$F_Y = E^\Upsilon G\dot g$ on $\{\chi_K = 0\}$" (line 1155).* Add the citation: the row terms $\vartheta_\nu$,
$\vartheta_{\nu,\sharp}$ are supported in $\mathrm{supp}\,\chi_K$ and vanish for $t^\flat_*<10$ (I10:199-200), and
III.I$'''''''$'s terms carry $d\chi_K$ (I8:139-147).

(A29) *"$\chi(t^\flat_*)Z_1$ is the forward solution" (line 1247).* Add: $\chi(t^\flat_*)Z_1$ and II.F$'$ Theorem 1.1's
solution are both smooth on $\Omega_*$ (the latter lies in II.F$'$'s spaces at every order), vanish on $\{t^\flat_*<2\}$
and solve the same equation; each $\{t^\flat_*\le T\}$ is closed under past causal curves ($dt^\flat_*$ is past timelike,
K:31-33), so they agree there by II.F Lemma 1.3, for every $T$. The same sentence serves Corollary R4.6 (2).

(A30) *Nits.* The b-density reading at line 1091 is I:33 ("$L^2$-based spaces on $\Omega_*$ use the unweighted
b-density $\mu_{\mathrm b}$"), not `PART-III-A-PREREQ.md`:142. (A4) at line 1028 uses Lemma R3.1's proof (the extension
by zero of a solution vanishing to infinite order at $\Sigma^\circ$), not only its statement, for "determined on $N^+$ by
them". K4, S2, S4 and S7 checked linear inequalities at samples; T3 proves them on the whole parameter box (each
difference a positive sum after a rational parametrisation; control: at $\eta = \delta_\sharp-\beta$ the condition on
$h$'s $\iota^+$-order is an equality).

(A31) *Tautological controls.* S8's control was the hand-written limit $\lim(v/2)/r$; T4 evaluates $W^{**}_H$'s
components at $r = 2r_h$: $v^{-1}W^{**}_v\to\frac1{8r_h^2}$, $v^{-1}W^{**}_r\to-\frac1{12r_h^2}$, so $W^{**}_H$ has no
$K^+$-order (control: $W^*$'s components are bounded). S4's second control set the $K^+$-order to 0 by hand, and lines
1190-1191 rely on it; T5 computes $\Theta(r^{-2}dv^2) = -r^{-3}dv$, stationary and nonzero, which is $\Theta(K)$ on
$\{r\le2R_1\}$ by (0.1): without the $W^{**}$ term the source has a stationary part, of $K^+$-order 0, below the
$\frac12$ of (1.4) (control: $\Theta(K^*) = 0$, H4 and V3, so carrying $W^{**}$ removes it).

### R4.d What is not proved

1. *A rate better than $t_*^{-1/2}$*: Theorem R2.5 at positive $K^+$-weight for $\Box$ (section R4.b), with at most
   $\kappa<\delta_\sharp$ to gain for Theorem R3.4's representative.
2. *Proposition R4.5 (c)*: a model computation, not a proof.
3. *Corollary R2.8 with data on a later slice* $\{t_* = t_0\}$ (its proof fails, (A23)); nothing uses that form.
4. *A second reading* of R2.1-R2.5, R2.12, rounds 3 and 4; in particular of Proposition R4.2's transposition and
   Corollary R4.6.

(Ext$\Box$), (Dyn) and (H$'$7) are no longer open (Theorem R4.3, (A16)).

### R4.e Findings, labels and files (round 4)

*Findings.*
- (GD17) In III.B's Cartesian components the 1-form wave operator on Tangherlini is the scalar one on each component
  plus a coupling of order $|x|^{-3}$ (E1); after Part IV's conjugation it lies in $\rho_0^2x_I^4\mathrm{Diff}^1_
  {\mathrm{e,b}}$, so Part IV$'$'s first-order matrix is $\bar A = 0$ (E2). The indicial roots at $\mathscr I^+$ are $0$
  and $a$ in every component, so all five components carry a radiation field of order $\frac32$ (E3); at $I_0$ none
  restricts the weight (E4); the corner condition $\alpha_I<\min(\alpha_0,0)$ is unchanged (E5).
- (GD18) Part IV's exterior estimates carry over to $\Box$ (Proposition R4.2), and (Ext$\Box$) holds for every
  $\beta\in(0,\delta_\sharp)$, with $\mathscr I^+$-order up to $\min(\frac32,q_{\dot h}-1)$ on the slab (Theorem R4.3,
  E6). The source's $I_0$-weight, one above $\dot h$'s through $c_\Upsilon$'s factor $|x|^{-1}$, is what makes the room.
- (GD19) Every perturbation in the class has a representative in harmonic gauge on all of $N^+$, inducing the data
  exactly and settling on compact sets to $\dot\mu K^*+c_\infty\mathcal L_{W^*}g$ at the rate $t_*^{-1/2}$, with no
  hypothesis beyond the write-out's proved parts at $b_0$ (Corollary R4.4, (A16)).
- (GD20) The rate: the zero-energy structure of $\Box$ does not block an improvement (first non-smooth term
  $\sigma^2\log\sigma$, G1-G3); Theorem R2.5 at positive $K^+$-weight is the missing step, and it can gain at most
  $\delta_\sharp$ for Theorem R3.4's representative, the gauge source's $\iota^+$-order being $\frac52+\delta_\sharp$
  (G4; Proposition R4.5).
- (GD21) Round 2's Corollary R2.8 and round 3's Theorem R3.4 (iv) used a false compact-support step; the
  $\mathscr I^+$-estimate of Proposition R4.2 repairs them (Corollary R4.6), and R2.12 (iv), R2.13 (b), Corollary R3.3,
  Theorem R3.4 (iv) and Proposition R3.6 hold without condition for data compactly supported on $\Sigma^\circ$.
- (GD22) The verifiers' findings on rounds 2 and 3 are seated as (A9)-(A31); S5 is re-run with the actual
  $t^\flat_*$ (T1), K3 at every spatial order (T2), K4, S2, S4, S7's inequalities on the whole box (T3), and S8's and
  S4's controls computed (T4, T5).

*Labels.* Computed: `checks/gdext5.py` E1-E6, `checks/gdrate5.py` G1-G4 and `checks/gdr3fix5.py` T1-T5 (exact, sympy; E1
at integer points with integer $r$, E5, E6 and G4 (c) at exact rational samples, G3 by exact series, T2 with $q$
symbolic, T3 on the whole parameter box); each with a control that fails. Deduced: Lemma R4.1 (from E1-E5), Proposition
R4.2, Theorem R4.3, Corollaries R4.4 and R4.6, Proposition R4.5 (a)-(b), and the amendments (A9)-(A31). Formal (a model
computation, not a proof): Proposition R4.5 (c). READ: the file:line citations above. Standard: b-Sobolev embedding (IV
(0.1)), the energy estimates for linear wave equations on compact domains of dependence. Everything is at $b_0$, where
(Dyn) is Part VI.A Theorem 6.1.

*Proposed replacement for the paper's harmonic-gauge sentences.* Section 8.2, the sentence beginning "In harmonic gauge
the spherically symmetric part of a perturbation is" up to "does not decay at infinity;":

> In harmonic gauge every perturbation in the class has a representative that is in harmonic gauge on the whole domain,
> induces the given data, and equals the solution above near the initial surface. On each region r ≤ R it settles to
> μ̇K* + c π_{W*}, growing linearly in v, with c a conserved horizon charge, at the rate τ^(−1/2). A gauge change whose
> gauge vector has compactly supported data on the initial surface moves only c (deduced from the supplement's proved
> parts: GAUGEDECAY5 R3.4, R4.3, R4.4, R4.6; `docket68/n1star/checks/gdscri5.py`, `checks/gdext5.py`). Without decay of
> those data the growth can be traded for a stationary term that does not decay at infinity. τ^(−1/2) is what square
> integrability in time gives. A better rate needs the 1-form wave operator's estimate at positive weight at timelike
> infinity, which is not written, and could gain at most the constraint damping's margin;

Section 9, the sentence "The decay of X is not proved, so the routes in a Regge–Wheeler-type gauge and in the harmonic
gauge (Hung's sections 5–8 in five dimensions), which argue decay in those gauges, remain deductions.":

> The gauge vector X is determined in two gauges (supplement GAUGEDECAY5). In a Regge–Wheeler-type gauge it is explicit,
> and the perturbation settles to the change of mass at the rate of section 8.2, the horizon included. In the harmonic
> gauge a representative exists on the whole domain, induces the given data and settles to μ̇K* + c π_{W*} at τ^(−1/2).
> Both are deduced from the supplement's proved parts; Hung's route in five dimensions (his sections 5–8) is needed for
> neither and remains a deduction.

*Files.* `GAUGEDECAY5.md` (this section appended); `checks/gdext5.py` with `checks/gdext5.out`; `checks/gdrate5.py` with
`checks/gdrate5.out`; `checks/gdr3fix5.py` with `checks/gdr3fix5.out`.

## Round 5

*Status.* Written 2026-11-02 (round 5, this section). Not verified by a second reader. Rounds 1-4 are left as they
stand; every change to them is a numbered amendment, (A32)-(A36) in section R5.c. New program: `checks/gdkplus5.py`
(Q1-Q6) with `checks/gdkplus5.out`; every check has a control that mutates the computed path and must fail, and fails.
Labels as in rounds 1-4. Readings add I3 for `PART-III-I3-ALMOST.md` (III.I$''$), I4 for `PART-III-I4-BOOST.md`
(III.I$'''$), G2 for `PART-II-G2-DECAY.md` (II.G$'$) and G for `PART-II-G-NASHMOSER.md`, all under `proof5/`; F2, D,
H$'$, I10 as before. Section headings are lettered (R5.a-R5.e). No finding of the round-4 verifier had been relayed
when this round was written; none is seated here.

*The result, in one paragraph.*
- **Theorem R2.5 holds at positive $K^+$-weight** (Theorem R5.1). The write-out's template is III.I$''$ Proposition
  5.1 ([Hin26] Proposition 11.17), which improves III.H$'$'s forward solutions at $K^+$ with II.G$'$'s Fourier tools
  (III.H$'$ is the $n = 4$, $\aleph>0$ form of [Hin26c] Theorem 12.3's frequency splitting that G:39-42 leaves to Part
  III). At $\Box$ it carries over and is shorter: $\Box$ is its own stationary model (no Step 1, no iteration), it has
  one zero-energy state $W^*\in\mathcal A^2$ with no generalised partner (one integration in $t_*$, not two), and the
  sources it is applied to have $\mathscr I^+$-weight at least $\frac52$ (no Step 2a). For a source of $K^+$-weight
  $\alpha_K\in[\frac12,1)$ and $\iota^+$-weight $\gamma_++2$, $\gamma_+\in(\alpha_K,\frac32)$ (b-weights for II.F$'$'s
  $\mu_b$), the forward solution is $u'+\beta W^*$, $u'$ of $K^+$-weight $\alpha_K$ and $\partial_{t_*}\beta$ a
  convolution of a coefficient $B$ of $K^+$-weight $\alpha_K$. At $\alpha_K = \frac12$ this is Theorem R2.5 (Q1).
- **The rate** (Theorem R5.2): $u-c_f(t_*)W^* = O(t_*^{-\alpha_K})$ on compact $r$-sets with every derivative, $c_f$
  the horizon charge of (R2.2); that is $t_*^{-1/2-\kappa}$, $\kappa = \alpha_K-\frac12\in[0,\frac12)$.
- **The harmonic gauge settles at $t_*^{-1/2-\kappa}$ for every $\kappa\in(0,\delta_\sharp)$**, $\delta_\sharp =
  (1-e_\Upsilon)\gamma_\Upsilon$ (Corollary R5.3: Corollary R4.4, Theorem R3.4 (iii), Theorem R2.12 (iii)). The bound
  is the gauge source's: its $\iota^+$-order is $\frac52+\delta_\sharp$, and the theorem asks $\alpha_K<\gamma_+<
  (\iota^+\text{-order})-2$ (Q6). It equals round 4's formal $l = 0$ exponent (Proposition R4.5 (c)), so if that model
  is right the rate is sharp but for its endpoint.
- **A gauge vector with compactly supported data settles at $t_*^{-1+\epsilon}$** (Corollary R5.4: Corollary R4.6, and
  with it Corollary R2.8, Proposition R2.13 (b) and the $Y_h$-clauses). Here the operator, not the source, stops the
  method: at $\alpha_K = 1$ the source's time integral enters at zero energy as a Taylor term (Q4's control), the step
  III.I$'''$ takes for $L$; it is not carried here.
- **Downstream** (section R5.e): replacement texts for R2.13 (b), R3.4 (iii)-(iv), supplement 10.2 (iv) and 10.8, and
  the paper's section 8.2 (with the matching clause of section 9), superseding round 4's proposal.

### R5.a Theorem R2.5 at positive $K^+$-weight

*Setting* (READ, I3:22-60). $X = \{r\ge r_0\}$ and $M' = [\overline{\mathbb R}_{t_*}\times\bar X;\{\pm\infty\}\times
\partial\bar X]$, with faces $I$ (its part in $t_*>0$ is $\mathscr I^+$), $\iota = \iota^+\cup\iota^-$ and $K =
K^+\cup K^-$; $H^{k,(w_I,w_\iota,w_K)}_{\mathrm b}$ are the b-Sobolev spaces for $|dt_*/\langle t_*\rangle|\mu_{\mathrm
b}$, $\mu_{\mathrm b} = |dx|/\langle x\rangle^4$, which on $\Omega_*$ are II.F$'$'s (1.2) with its $\mu_b$ (G2:842-845,
F2:89-96); $X^\pm_{\mathrm{sc}\text-\mathrm b}$, with faces scf, tf, zf, are III.A's (I3:32-33). Here $L = L_b = \Box$ at
$b_0$, $\hat P(\sigma)$ its spectral family and $\tilde P(\sigma)$ Definition R2.1's augmentation.

*The dictionary* (computed Q1). Near $\iota^+\cap K^+$, with $\rho_+ = 1/r$ and $\rho_K = r/t_*$, $|dt_*\,dx| =
\rho_+^{-5}\rho_K^{-1}$ times the b-density, so $L^2(|dt_*\,dx|) = \rho_+^{5/2}\rho_K^{1/2}L^2_{\mathrm b}$: a 3b-weight
$(\beta_{\mathrm{sf}},\beta_K)$ of III.H$'$ (H$'$:27-41) is the b-weight $(\beta_{\mathrm{sf}}+\frac52,\beta_K+\frac12)$,
as II.F$'$ records ($b_+ = \alpha_++\frac52$ and the $K^+$-weight $-\aleph+\frac12$, F2:91, 96). So R2.5's source class
$H^{(\mathsf s;k),(\alpha_{\mathrm{sf}}+2,0)}_{3b;b}$ is the b-class $(\gamma_++2,\frac12)$ with $\gamma_+ :=
\alpha_{\mathrm{sf}}+\frac52$, its window $\alpha_{\mathrm{sf}}+2\in(0,1)$ is $\gamma_+-\frac12\in(0,1)$, and its
solution's 3b $K^+$-weight $-1$ is the b-weight $-\frac12$. A conormal function $O(\rho_+^A\rho_K^B)$ lies in
$\rho_+^{w_\iota}\rho_K^{w_K}L^2_{\mathrm b}$ near the corner iff $A>w_\iota$ and $B>w_K$ (Q1), and b-Sobolev embedding
(standard) goes back to pointwise bounds: on compact $r$-sets $\rho_K\asymp t_*^{-1}$, so the b-weight $\alpha_K$ at
$K^+$ is the rate $t_*^{-\alpha_K}$. Write $\alpha_K = \frac12+\kappa$.

*The gap and the window* (computed Q2; deduced). On Cartesian components $\hat P(0)$ is $-\Delta$ up to
$\rho^2$-relative terms (Lemma R4.1 (a); E1-E2), with the indicial roots $q = -l,\ l+2$ on $r^{-q}Y_l$ (round 4's G2; Q2
for $l\le8$). III.H's weight $\alpha$ (spaces on $L^2(dx)$) is the $\mu_{\mathrm b}$-weight $\alpha+2$; the root-free
interval around it is $(0,2)$, III.D$'$'s (G) for $\alpha+2\in(0,2)$ (R2.1); and the column $\hat f_*(0)\in\mathcal A^3$
lies in $\mathcal Y_0$, of $\mu_{\mathrm b}$-weight $\alpha+4$, iff $\alpha+2<1$ (R2.3). So III.H (1.1)'s window at
$\Box$ is $\alpha+2\in(0,1)$, inside the gap. At $\mathscr I^+$ the outgoing root is $\frac32$ ($\Box_0(r^{-p}e^{k(t-r)})
= k(2p-3)r^{-p-1}e^{k(t-r)}+O(r^{-p-2})$), the cap $\frac32+\bar S$ of II.G$'$ Corollary 4.5 with $\bar S = 0$ for $\Box$
(READ, D:136-139 at $\gamma_\Upsilon = 0$, as Lemma R3.5 reads it; E3). Control: at $n = 3$ the gap is $(0,1)$ and the
root 1.

**Theorem R5.1 (Theorem R2.5 at positive $K^+$-weight: III.I$''$ Proposition 5.1 at $\Box$, at $b_0$; deduced, computed
Q1-Q5).** Let $\alpha_K\in[\frac12,1)$, $\gamma_+\in(\alpha_K,\frac32)$, $w_I\ge\max(\frac52,\gamma_++2-\alpha_K)$ and
$$f\in H^{\infty,(w_I,\gamma_++2,\alpha_K)}_{\mathrm b}(\Omega_*;T^*)^{\bullet,-},\tag{R5.1}$$
and let $u$ be the forward solution of $\Box u = f$ (II.F$'$ Theorem 1.1 at $P = P_0 = \Box$). Then $\gamma_+-\alpha_K\in
(0,1)$, and for every $\epsilon\in(0,\frac15(\frac32-\gamma_+)]$:

(i) $u = u'+u_{\mathrm{sing}}$ with $u'\in H^{\infty,(\gamma_+-\epsilon,\gamma_+,\alpha_K)}_{\mathrm b}(M')$;

(ii) $u_{\mathrm{sing}} = \beta(t_*,r)W^*$, where for one $B\in H^{\infty,\alpha_K}_{\mathrm b}(\mathbb R)$ (II.G$'$
Definition 2.1: $\langle t\rangle^{\alpha_K-\frac12}\partial_t^p(t\partial_t)^qB\in L^2(dt)$, G2:79-81)
$\partial_{t_*}\beta(\cdot,r) = (\partial_t\chi_K)(\cdot,r)*B$ and $\beta(\cdot,r)-\beta(\cdot,r') = (\chi_K(\cdot,r)-
\chi_K(\cdot,r'))*B$;

(iii) $u_{\mathrm{sing}}$, and so $u$, lies in $H^{\infty,(\gamma_+-\epsilon,\gamma_+-\epsilon,\alpha_K-1)}_{\mathrm b}$:
one order lost at $K^+$, none at $\iota^+$.

At each order $k$ the norms are bounded by $C_k$ times the norm of $f$ in (R5.1) at an order $k+\ell$, $\ell$
independent of $k$. At $\alpha_K = \frac12$, (i)-(iii) are Theorem R2.5 (i)-(iii) in b-form (the dictionary), for
sources with b-regularity.

*Proof: the modifications, and why each step carries over.* References are to III.I$''$ (I3) unless said otherwise.
1. *The operator* (I3:52-60). III.I$''$'s $L = L^{g,g_0}$ is a perturbation of $L_b$, removed by its Step 1 and an
   iteration. Here $L = L_b = \Box$: the start (Step 0, I3:325-337), Step 1 (I3:346-352), the iteration (I3:339-344,
   423-426) and the continuity in $(S,h)$ (I3:428-440) are void. $\hat P(\sigma)$ is invertible for real $\sigma\ne0$
   (III.D Propositions 6.1-6.2, as in R2.4's proof), and $\tilde P(\sigma)$ for $0<|\sigma|\le c_k$ (Theorem R2.4). The
   window is the one above.
2. *Lemmas 2.1 and 3.1* (I3:64-189): no operator enters. Verbatim.
3. *The decomposition* (I3:193-214). For $f\in C^\infty_c(\Omega^\circ_*)$, R2.5's proof (III.H$'$ Lemma 2.1,
   (4.1)-(4.2), (5.1)-(5.2) at $\Box$) gives $u = u_{\mathrm{hi}}+u_{\mathrm{reg}}+u_{\mathrm{sing}}$ with $\mathcal
   Fu_{\mathrm{hi}} = (1-\chi(|\sigma|))\hat P(\sigma)^{-1}\hat f$, $\mathcal Fu_{\mathrm{reg}} = \chi(|\sigma|)\hat
   u_{\mathrm{reg},1}$, $(\hat u_{\mathrm{reg},1},\hat b_1) := \tilde P(\sigma)^{-1}(\hat f,0)$, and $\mathcal
   F(\partial_{t_*}u_{\mathrm{sing}}) = \chi(|\sigma|)G_1(\sigma)(\hat b_1)$, $G_1(\sigma)b := \Psi(\sigma,\cdot)bW^*$:
   III.I$''$ (4.1) without its second member (no $\hat S_1$, no $G_2$, no generalised state). $c$ is chosen as at
   I3:193-198 with Theorem R2.4's constants. Density: in place of III.I Theorem 5.3, the forward solution map of II.F$'$
   Theorem 1.1 at $P = P_0 = \Box$ (as Theorem R3.4 and Corollary R4.6 use it; (H$'$7) by (A16)), continuous from (1.4),
   which contains (R5.1) with $b_+ := \frac12(\frac12+\gamma_+)$, $b_I := \frac12(b_++\frac32)$ (Q5:
   $\frac12<b_+<b_I<\frac32$, $b_+\le \gamma_+$, $b_I+1\le w_I$; $\Box$ is 1-admissible with sf-weight $b_+-\frac52$ by
   Theorem R2.5 (iii)). The extension across $\{r = r_0\}$ is I3:210-214's.
4. *High and bounded frequencies: Lemma 4.1* (I3:216-242). Its inputs are II.G$'$ Corollary 4.5 (G2:830-845), which
   asks I.B's (H1)-(H8), Corollary 4.2 (2) (G2:672), which asks I.A's (H1)-(H4), and invertibility on the compact set
   $J$. At $\Box$: III.D Proposition 6.1's proof gives I.B's hypotheses for $\Box^\Upsilon_b$ on a compact parameter set
   (D:322-330), and R2.5's proof uses them at $\Box$; I.A's by R2.1; invertibility on $J$ by III.D Propositions
   6.1-6.2; $\bar S = 0$. Its weight conditions at $(\beta^f_I+1,\beta_\iota+2,\beta_K) = (w_I,\gamma_++2,\alpha_K)$ are
   $\alpha_K\in(0,1)$, $\beta^f_I = w_I-1\ge\frac32$ and $w_I\ge\gamma_++2-\min(\alpha_K,1-\epsilon_1)$ (Q5). So
   $u_{\mathrm{hi}}\in H^{\infty,(\frac32-\epsilon,N,N)}_{\mathrm b}(M')$ for every $N$.
5. *The transform of $f$*: (2.25a), II.G$'$ Proposition 3.3 (1) (G2:422-431), whose condition is $w_I\ge\gamma_++2-
   \min(\alpha_K,1-\epsilon)$: $\hat f|_{\pm(0,1]}\in H^{\infty,(\min(w_I,\gamma_++2)-\epsilon,\gamma_++1,\alpha_K-1)}
   _{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$, the zf index set $(0,0)$ dropping as $\alpha_K-1<0$ (as at
   I3:368-371).
6. *Low frequencies: Lemma 4.2* (I3:244-269), with $\tilde P$ for $\tilde L_b$. Its proof is II.G$'$ Proposition 4.7's
   (G2:917) with III.H Corollary 4.2 and Theorem 4.1 (3), which Theorem R2.4 gives at $\Box$, and with the outgoing
   order $\mathsf r_{\mathrm{out}} = \beta_{\mathrm{scf}}-2-\frac\epsilon2<-\frac12+\bar S = -\frac12$. With
   $\beta_{\mathrm{scf}} := \frac32-\epsilon$, $\beta_{\mathrm{tf}} := \gamma_+-1$, $\beta_{\mathrm{zf}} := \alpha_K-1$,
   so that $\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}} = \gamma_+-\alpha_K = \alpha+2\in(0,1)$, and the source space
   containing $\hat f$ ($\frac52-\epsilon\le\min(w_I,\gamma_++2)-\epsilon$; Q5): $\hat u_{\mathrm{reg},1}\in
   H^{\infty,(\frac32-2\epsilon,\gamma_+-1,\alpha_K-1)}_{\mathrm b}$ and $\hat b_1\in H^{\infty,\alpha_K-1}_{\mathrm b}
   (\pm(0,c],|\frac{d\sigma}\sigma|)$.
7. *The regular part* (I3:376-383): (2.26a), II.G$'$ Proposition 3.5 (1) (G2:526-538), at the $K$-weight $\alpha_K\in
   (0,1)$ with a void Taylor condition, gives $u_{\mathrm{reg}}\in H^{\infty,(\gamma_+-\epsilon,\gamma_+,\alpha_K)}
   _{\mathrm b}(M')$. With step 4 this is (i), $u' := u_{\mathrm{hi}}+u_{\mathrm{reg}}$, as $\gamma_+<\frac32$.
8. *The cut-off state: Lemma 4.3* (I3:271-305), with the one state $W^*\in\mathcal A^2$ ($q_1 = 2$; R2.1) and $\Psi$ of
   III.H Lemma 2.5, which does not depend on the operator: $\chi G_1(\hat b_1)\in H^{\infty,(N,\alpha_K+1-\epsilon,
   \alpha_K-1)}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$. Q3 computes $r^2W^*_t\to1$, $r^3W^*_r\to r_h$, the
   conormality, and the order $q-\epsilon$ of $\|W_\beta^{-1}\Phi(\sigma r)r^{-q}\|_{L^2(\mu_{\mathrm b})}$ that makes
   the tf-weight $a+2-\epsilon$ at $q = 2$ (control: the Killing form $(\partial_v)^\flat$ has $q = 0$).
9. *The singular part: one integration* (in place of I3:385-412). III.I$''$ integrates $\partial_{t_*}u_{\mathrm{sing}}$
   by Lemma 3.1 at $\beta_\iota = \gamma_++1$ and then $u_{\mathrm{sing}}$ by Lemma 2.1 (1), because its (5.7) carries
   $\partial^2_{t_*}$ of the generalised state. Here Lemma 3.1 is applied once, to $u := u_{\mathrm{sing}}$, with
   $\beta_I := \gamma_+-\epsilon$, $\beta_\iota := \gamma_+$, $\beta_K := \alpha_K-1\in[-\frac12,0)$. Its hypotheses
   (Q5): $\beta_\iota>\beta_I$; $\beta_K<0<\beta_\iota-\beta_I$; $\beta_K\in(-1,1)\setminus\{0\}$; (3.1) is step 8,
   whose tf-weight $\alpha_K+1-\epsilon$ is at least $\gamma_+$ (as $\epsilon\le\frac15(\frac32-\gamma_+)$ and $\alpha_K
   +1\ge\frac32$) and whose zf-weight $\beta_K<0$ carries no index term; the bound on $\Omega_<$: $u = 0$ for $t_*<1$, so
   $u_{\mathrm{sing}} = -(u_{\mathrm{hi}}+u_{\mathrm{reg}})$ there, of weights $(\cdot,\gamma_+,\alpha_K)$ by steps 4
   and 7, at least $(\infty,\beta_\iota,\beta_K)$; the support: $\mathcal F(\partial_{t_*}u_{\mathrm{sing}})$ is
   $\chi(|\sigma|)$ times the boundary value from $\mathrm{Im}\,\sigma>0$ of $\Psi\hat b_1W^*$ (III.H$'$ section 5 at
   $\Box$, R2.5's proof), so $\mathcal Fu_{\mathrm{sing}}$ is supported in $\mathrm{supp}\,\chi(|\cdot|)\cup\{0\}$, a
   compact subset of $(-c,c)$, $c\le\frac12$. Lemma 3.1 gives $u_{\mathrm{sing}}\in H^{\infty,(\gamma_+-\epsilon,
   \gamma_+-\epsilon,((0,0),\alpha_K-1))}_{\mathrm b}$, the term $(0,0)$ lying above the weight $\alpha_K-1<0$: (iii).
   With III.I$''$'s $\beta_\iota = \gamma_++1$ the tf-condition fails (Q5's control): the singular part's
   $\iota^+$-weight is $\gamma_+$, set by the bound on $\{t_*<1\}$, as (I$''$1) found for $L$ (I3:446-452).
10. *(ii).* $B := \mathcal F^{-1}(\chi\hat b_1)$. By step 6 the pair $(\chi\hat b_1|_{\sigma<0},\chi\hat
   b_1|_{\sigma>0})$ lies in II.G$'$ Definition 2.7's $X^{k,\alpha_K-1}$ (G2:233-237) with no polynomial part
   ($\alpha_K-1<0$), and II.G$'$ Proposition 2.8 (2) with $\beta = \alpha_K\in(0,1)$ (G2:246-253) gives $B\in
   H^{k,\alpha_K}_{\mathrm b}(\mathbb R)$. Q4 computes the transform pair
   $t_+^{-\alpha_K}\leftrightarrow\Gamma(1-\alpha_K)(0^+-i\sigma)^{\alpha_K-1}$ and that the two membership thresholds
   meet at $\beta = \alpha_K$. The identities are R2.5 (ii)'s, proved there from $\mathcal
   F(\partial_{t_*}u_{\mathrm{sing}}) = \chi\Psi\hat b_1W^*$ without a weight.
11. *What does not carry over, and is not used.* Step 2a (III.I$'$ Proposition 3.1 at $\Box$, the formal solutions at
   $\mathscr I^+$, I3:354-361) is void as $w_I\ge\frac52$; a source that reaches $\mathscr I^+$ with a lower order
   (Part VIII's $F_Y$ there, the slab commutator of Corollary R4.6) is first localised to a cone (section R5.b). Step 3
   (III.I$'$ Proposition 2.1 at $\Box$, the expansion at $\mathscr I^+$, I3:417-421) is not carried: (iii) states the
   plain weight $\gamma_+-\epsilon$ there. $\square$

*Why this was the missing step* (Proposition R4.5 (b)). III.I$''$'s argument splits the forward solution by frequency
and improves each piece at $K^+$. Of the operator it needs the high-energy and nonzero-frequency theory, the augmented
low-energy inverse with its symbol bounds, and the decay of the zero-energy states; at $\Box$ these are III.D section 6,
Theorem R2.4 and $W^*\in\mathcal A^2$. The zero-energy structure enters only through the window $\gamma_+-\alpha_K\in
(0,1)$ and through the absence of a zf Taylor term ($\alpha_K<1$); round 4's $\sigma^2\log\sigma$ (G1-G3) lies above
both.

**Theorem R5.2 (Theorem R2.7 at $K^+$-weight $\alpha_K$; deduced from Theorem R5.1, Lemma 2.2 and B4).** Let $f$, $u$
be as in Theorem R5.1 and $R'>r_0$. On $\{r_0<r\le R',\ t_*\ge8\max(R',1)\}$, with every number of derivatives in $x$
and $t_*$ (the constant depending on the number),
$$\big|u-c_f(t_*)W^*\big|\le C\,t_*^{-\alpha_K}\|f\|,\tag{R5.2}$$
with $c_f$ of (R2.2) and $\|f\|$ a norm of (R5.1). In particular (a) if $\ell(f) = 0$, $u = O(t_*^{-\alpha_K})$; (b) if
$\int_v^\infty|\ell(f)|\le C'v^{-\kappa'}$, then $u = c_\infty W^*+O(t_*^{-\min(\alpha_K,\kappa')})$.

*Proof.* Theorem R2.7's steps (1)-(5), with three replacements. In (2): $|B(t)|\le C\langle t\rangle^{-\alpha_K}\|f\|$,
by Lemma R2.6 with $H = \mathbb C$ on $[\frac T2,4T]$, as $\langle t\rangle^{\alpha_K-\frac12}(B,t\partial_tB)\in
L^2(dt)$ gives $\int_{T/2}^{4T}(|B|^2+|t\partial_tB|^2)\,dt\le CT^{1-2\alpha_K}\|B\|^2$ (standard); the kernels
$\partial_r\chi_K$, $\partial_t\chi_K$ and $\psi$ are supported in $[1,4\max(R',1)]$, so on $t_*\ge8\max(R',1)$ the
convolutions sample $B$ on $[\frac{t_*}2,t_*]$ ((A20)) and are $O(t_*^{-\alpha_K})$. In (3): $|Q[u'](v)|\le
C\|u'(t_*)\|_{C^1(K)}\le Ct_*^{-\alpha_K}\|f\|$, by b-Sobolev embedding of Theorem R5.1 (i) near $K^+$, where
$\rho_K\asymp t_*^{-1}$ on compact $r$-sets (standard). In (5): $u' = O(t_*^{-\alpha_K})$ the same way, with its
b-derivatives $t_*\partial_{t_*}$ and $\partial_x$; $\partial_{t_*}\beta = \partial_t\chi_K*B$ and $\partial_{t_*}c_f =
\ell(f)/4\pi^2$. Density as in R2.7, by Theorem R5.1's bounds. $\square$

### R5.b The rate

**Corollary R5.3 (the harmonic gauge at $t_*^{-1/2-\kappa}$; deduced, computed Q6).** Let $\delta_\sharp =
(1-e_\Upsilon)\gamma_\Upsilon\in(0,\frac14)$ (I10:44-46). For every $\kappa\in(0,\delta_\sharp)$ there is $C_\kappa$,
bounded by finitely many data norms, such that on each $\{r_0<r\le R',\ t_*\ge T'\}$, with every number of derivatives,
$$\big|\dot g_H-\dot\mu K^*-c_\infty\mathcal L_{W^*}g\big|\le C_\kappa\,t_*^{-1/2-\kappa},\tag{R5.3}$$
for $\dot g_H$ of Corollary R4.4 (all of $N^+$), of Theorem R3.4 (iii) (the late region) and of Theorem R2.12 (iii) (the
cone, Corollary R3.3), each with its $c_\infty$. The clauses adding $\mathcal L_{Y_h}g$ (R4.4's last, R3.4 (iv), R2.12
(iv)) hold at the same rate with $c_\infty+Q[Y_h]/4\pi^2$ (Corollary R5.4).

*Proof.* Fix $\kappa$ and put
$$\beta := \tfrac12(\kappa+\delta_\sharp),\quad\eta := \tfrac12(\delta_\sharp-\beta),\quad b_+ := \tfrac12+\beta,\quad
\gamma_+ := \tfrac12+\tfrac12(\kappa+\beta),\quad\alpha_K := \tfrac12+\kappa$$
(Q6 (ii): every inequality used below is a positive sum on the whole box $0<\kappa<\delta_\sharp<\frac14$). *The full
solution.* With Theorem R4.3 at this $\beta$ (some $p\in(\frac12+\beta,\min(\frac32,q_{\dot h}-1))$) and $b_I\in
(b_+,p)$, $Y := \chi(t^\flat_*)Z_1$ is the forward solution on $\Omega_*$ of $\chi F_Y+[\Box,\chi(t^\flat_*)]Z_1$
(Corollary R4.4's proof: Lemma R3.5, S7 with T1), and II.F$'$ (1.7) (F2:93-96) gives $Y\in H^{k,(b_I,b_+,-\frac12)}
_{\mathrm b}(\Omega_*,\mu_b)$ for every $k$. For Theorem R3.4, $Y$ is its own forward solution, with the same weights
(Lemma R3.5). *Cone localisation* (Theorem R3.4 (iii)'s proof, $\chi'$ of (A8)): $\chi'Y$ is the forward solution of
$$f := \chi'J_h+[\Box,\chi']Y.$$
$f$ vanishes near $\mathscr I^+$ ($\mathrm{supp}\,\chi'\subset\{r\le t_*/20\}$), so (R5.1) holds with every $w_I$.
$\chi'J_h$: on $\mathrm{supp}\,\chi'\subset\{\chi_K = 1\}$ it is conormal of $\iota^+$-order $\lambda_\sharp+1-\eta =
\frac52+\delta_\sharp-\eta$ and $K^+$-order $\alpha-2-\eta>1$ (Proposition R3.2), so it lies in (R5.1), as $\gamma_++2<
\frac52+\delta_\sharp-\eta$ and $\alpha_K<1$ (Q6; S4). $[\Box,\chi']Y$: on the cone part of $\mathrm{supp}\,d\chi'$,
$\{\frac1{40}\le r/t_*\le\frac1{20}\}$, $[\Box,\chi']\in\rho_+^2\mathrm{Diff}^1_{\mathrm b}$ (S6), and that cone stays
away from $K^+$ and $\mathscr I^+$; the rest of $\mathrm{supp}\,d\chi'$ is compact. So $[\Box,\chi']Y\in
H^{\infty,(N,b_++2,N)}_{\mathrm b}$ for every $N$, in (R5.1) as $\gamma_+<b_+$. (For Theorem R2.12, $f = \chi'J_h$.)
*The rate.* Theorem R5.2 gives $|\chi'Y-c_f(t_*)W^*|\le Ct_*^{-1/2-\kappa}$ with every derivative. For large $t_*$,
$\chi' = 1$ near the horizon and $\ell(f) = \ell(J_h) = -\ell(\Theta(h)) = O(v^{-w+\epsilon'})$ (Theorem 2.3), so
$c_f-c_\infty = O(t_*^{-(w-1)+\epsilon'})$, $w-1>1$. On compact $r$-sets at late times $\chi' = \chi(t^\flat_*) =
\chi_K = 1$, $Z_1 = \chi'Y$, and $\dot g_H-\dot\mu K^*-c_\infty\mathcal L_{W^*}g = h+\mathcal L_{Z_1-c_\infty W^*}g$
($K^* = K+\mathcal L_{W^{**}_H}g$), with $|h|_k = O(t_*^{-w+\epsilon'})$ ((0.2)). $\square$

*Why $\delta_\sharp$, and not more* (computed Q6; the sharpness formal). Eliminating $\gamma_+$ from Theorem R5.1's
bounds ($\alpha_K<\gamma_+$; $\gamma_+<\frac32$; $\gamma_++2$ below the source's $\iota^+$-order $a$; $\alpha_K<1$) gives
$\kappa<\min(\frac12,a-\frac52)$. The gauge source has $a = \lambda_\sharp+1 = \frac52+\delta_\sharp$, less any $\eta>0$,
and the commutator inherits it through $b_+<\frac12+\delta_\sharp$: so $\kappa<\delta_\sharp$, Proposition R4.5 (b)'s
bound, now attained. Round 4's model (Proposition R4.5 (c), formal) gives the $l = 0$ response $t^{2-a} =
t^{-1/2-(a-5/2)}$ for $a\in(\frac52,3)$; Q6 checks that the method's exponent equals the model's there and never
exceeds it (control: with the window's lower end dropped it would). So if the model is right and the $l = 0$ time
component of $J_h$'s $\lambda_\sharp$-term does not vanish, (R5.3) is sharp up to its endpoint; the endpoint $\kappa =
\delta_\sharp$ is not reached, every weight being an open condition. For this representative the first obstruction to
more is the source, the constraint damping's margin.

**Corollary R5.4 (Corollary R4.6 at $t_*^{-1+\epsilon}$; deduced, computed Q6).** Let $Y$ be a smooth 1-form on $N^+$
with $\Box Y = 0$ whose Cauchy data on $\Sigma^\circ$ have compact support. For every $\epsilon>0$, on each
$\{r_0<r\le R',\ t_*\ge T'\}$ and with every number of derivatives, $|Y-(Q[Y]/4\pi^2)W^*|\le C_\epsilon t_*^{-1+
\epsilon}$. Hence Corollary R2.8 (read as R4.6), Proposition R2.13 (b), and the $Y_h$-clauses of Theorems R2.12 (iv),
R3.4 (iv) and Corollary R4.4 hold with $t_*^{-1+\epsilon}$ for the gauge vector's part.

*Proof.* For $\epsilon\in(0,\frac12)$ let $\kappa := \frac12-\epsilon$, $\alpha_K := \frac12+\kappa$, $\gamma_+ :=
\alpha_K+\frac13(\frac32-\alpha_K)$, $b_+ := \alpha_K+\frac23(\frac32-\alpha_K)$, $b_I := \frac12(b_++\frac32)$, $p :=
\frac12(b_I+\frac32)$ (Q6 (iii): $\alpha_K<\gamma_+<b_+<b_I<p<\frac32$ and $\gamma_+-\alpha_K\in(0,1)$, on the whole
box). Corollary R4.6 (1) gives $Y$ the $\mathscr I^+$-order $p$ on the slab, and (2), with $\beta := b_+-\frac12\in
(0,1)$, makes $\chi(t^\flat_*)Y$ the forward solution of a slab source of $\mathscr I^+$-order $p+1>b_I+1$ and of
infinite $\iota^+$- and $K^+$-weights; so $Y\in H^{k,(b_I,b_+,-\frac12)}_{\mathrm b}$ on $\Omega_*\cap\{t^\flat_*\ge3\}$
for every $k$ (II.F$'$ (1.7)). As in Corollary R5.3, $\chi'Y$ is the forward solution of $[\Box,\chi']Y\in
H^{\infty,(N,b_++2,N)}_{\mathrm b}$, in (R5.1) as $\gamma_+<b_+$; at late times $d\chi' = 0$ near the horizon, so
$\ell$ of the source vanishes and $c_f = Q[Y]/4\pi^2$ (Corollary R4.6 (3)). Theorem R5.2 gives $t_*^{-\alpha_K} =
t_*^{-1+\epsilon}$. For R2.13 (b): $\mathcal L_{Z'_0}g-c\,\mathcal L_{W^*}g = \mathcal L_{Z'_0-cW^*}g$. $\square$

*Where this one stops: the operator.* The source here has $\iota^+$-order $b_++2$, up to $\frac72$, so the cap is the
theorem's $\alpha_K<1$ (Q6: $\kappa<\frac12$). At $\alpha_K\ge1$, II.G$'$ Proposition 3.3 (1) gives $\hat f$ the zf
index set $((0,0),\alpha_K-1)$: the Taylor term $\hat f(0) = \int f\,dt_*$, which Lemma 4.2 and (2.26a), as carried,
do not take (Q4's control: at $\alpha_K = 1$ the transform is no power; $\Gamma(0)$, and $E_1$'s $\log$). For $L$ that
step is III.I$'''$'s (Proposition 2.1 with Lemmas 1.2-1.3, I4:61-70, 120-125, for $\alpha_K\in(1,\frac32)$); at $\Box$
it is not written. It is not blocked at zero energy: $\hat f(0)$ has $\mu_{\mathrm b}$-weight $\gamma_++1$ (the Taylor
coefficients lie in $H^{k,\beta_\iota-1}_{\mathrm b}(X)$, G2:526-538), and $\mathcal Y_0$ asks $\alpha+4 = \gamma_+-
\alpha_K+2$, which is at most $\gamma_++1$ exactly when $\alpha_K\ge1$ (deduced, Q2's dictionary). The next cap is
$\alpha_K<\gamma_+<\frac32$, the radiation field's transport (Q2): $t_*^{-3/2+\epsilon}$.

### R5.c Amendments

(A32) *Round 4's first obstruction is discharged.* Proposition R4.5 (b) with the paragraph "The first obstruction,
precisely" (lines 1633-1640), R4.d item 1 (lines 1815-1816) and (GD20) (lines 1838-1841); round 3's section "The rate"
(lines 1267-1272), R3.5 item 2 (line 1280) and its result bullet (line 984); round 2's R2.5 item 3 (lines
905-907). Theorem R2.5 at positive
$K^+$-weight is Theorem R5.1, written; the rate it gives is Corollaries R5.3-R5.4. Read "is not written" (or "not
proved") in each as "is Theorem R5.1 (round 5)". Proposition R4.5 (b)'s first criterion is Theorem R5.1's class: G4's
"sf-weight $\beta$" is the window $\gamma_+-\alpha_K$ (Q6 (iv)). Its second criterion, pointwise in $\sigma$
($a>\beta+3$), fails as stated and is not needed: Theorem R5.1 uses $L^2$ in $|d\sigma/\sigma|$ with b-regularity.

(A33) *The rate of the harmonic-gauge representative.* Theorem R3.4 (iii) (lines 1205-1207), Corollary R4.4 (lines
1541-1542), Theorem R2.12 (iii) (lines 716-717) with Corollary R3.3, and the result paragraphs and findings that quote
them (lines 436-438, 935, 979-980, 1357-1360; (GD14), (GD19)), and round 2's "The rate $\frac12$ is what $L^2$ in
time gives; nothing better is claimed" (lines 428-429), which Theorem R5.2 now improves for sources with $K^+$-weight:
read "$\le Ct_*^{-1/2}$" as "$\le C_\kappa t_*^{-1/2-\kappa}$ for every $\kappa\in
(0,\delta_\sharp)$" (Corollary R5.3).

(A34) *The rate of a gauge vector with compactly supported data.* Corollary R4.6 (lines 1552-1554), Corollary R2.8 as
R4.6 reads it, Proposition R2.13 (b) (lines 820-823) and its summary (line 446), Theorem R2.12 (iv) (lines 721-722),
Theorem R3.4 (iv) (lines 1210-1212) and Corollary R4.4's last clause (lines 1543-1544): read the rate $t_*^{-1/2}$ of the
homogeneous gauge vector as $t_*^{-1+\epsilon}$, every $\epsilon>0$ (Corollary R5.4); where $\mathcal L_{Y_h}g$ is added
to the representative, the total rate is (R5.3)'s. The exact readings of R2.13 (b) and R3.4 (iii)-(iv) are in section
R5.e.

(A35) *Proposition R4.5 (c)* stays formal, and becomes the benchmark: the proved rate reaches its exponent on
$a\in(\frac52,3)$ up to the endpoint (Q6). Its last sentences (lines 1638-1640: for a representative whose $l = 0$ gauge
part has compactly supported data "the operator side, not the source, is the first obstruction") are made precise by
Corollary R5.4's last paragraph: for that $l = 0$ part the operator stops the method at $t_*^{-1}$, at the step
III.I$'''$ takes for $L$.

(A36) *Round 4's proposed paper texts* (lines 1857-1876) are superseded by section R5.e's.

### R5.d What is not proved

1. *Theorem R5.1 at $\alpha_K\ge1$*: III.I$'''$ at $\Box$, the zf Taylor term; so, for compactly supported gauge data, a
   rate past $t_*^{-1}$.
2. *The endpoint $\kappa = \delta_\sharp$ and the sharpness of (R5.3)*: Proposition R4.5 (c) is a model, and whether
   the $l = 0$ time component of $J_h$'s $\lambda_\sharp$-term vanishes is not decided.
3. *III.I$'$ at $\Box$* (Steps 2a and 3, the expansion at $\mathscr I^+$); not needed for decay on compact sets.
4. *A second reading* of rounds 2-5; in particular of Theorem R5.1's steps 3, 9 and 10, Proposition R4.2 and Corollary
   R4.6.

### R5.e Findings, labels, files and replacement texts

*Findings.*
- (GD23) III.I$''$ Proposition 5.1 carries over to $\Box$ at $b_0$ (Theorem R5.1), shorter than for $L$: no
  perturbation and no iteration, one zero-energy state $W^*\in\mathcal A^2$ and one integration in $t_*$, no step at
  $\mathscr I^+$ for sources of $\mathscr I^+$-weight $\ge\frac52$. For sources of $K^+$-weight $\alpha_K\in[\frac12,1)$
  and $\iota^+$-weight $\gamma_++2$, $\gamma_+\in(\alpha_K,\frac32)$, the forward solution is $u'+\beta W^*$ with $u'$
  and the coefficient $B$ at $K^+$-weight $\alpha_K$ (Q1-Q5).
- (GD24) Modulo the horizon-charge term the forward solution decays like $t_*^{-\alpha_K}$ on compact sets (Theorem
  R5.2).
- (GD25) The harmonic-gauge representative of Corollary R4.4 settles to $\dot\mu K^*+c_\infty\mathcal L_{W^*}g$ at
  $t_*^{-1/2-\kappa}$ for every $\kappa\in(0,\delta_\sharp)$ (Corollary R5.3); the bound is the gauge source's
  $\iota^+$-order, and it equals round 4's formal $l = 0$ exponent (Q6).
- (GD26) A gauge vector with $\Box Y = 0$ and data compactly supported on $\Sigma^\circ$ settles to
  $(Q[Y]/4\pi^2)W^*$ at $t_*^{-1+\epsilon}$ (Corollary R5.4); there the operator stops the method at $t_*^{-1}$, where
  the source's time integral enters at zero energy (Q4's control).

*Labels.* Computed: `checks/gdkplus5.py` Q1-Q6 (exact, sympy; Q2 for $l\le8$; Q3's main term exact and its remainder
by its order at 0; Q4 and Q6 (i) at exact rational samples; Q5 and Q6 (ii)-(iii) on the whole parameter box), each with
a control that fails. Deduced: Theorems R5.1-R5.2, Corollaries R5.3-R5.4, the two paragraphs on where the rate stops,
and (A32)-(A36). Formal: the sharpness of (R5.3) (Proposition R4.5 (c)). READ: the file:line citations above.
Standard: b-Sobolev embedding, Lemma R2.6. Everything is at $b_0$, where (Dyn) is Part VI.A Theorem 6.1.

*Replacement texts.*

(1) *This file, Proposition R2.13 (b)* (lines 820-823; a reading, per (A34), not an edit):

> (b) *Decaying gauge data.* If $Z'_0$ has Cauchy data compactly supported on $\Sigma^\circ$, then on each
> $\{r_0<r\le R'\}$, with every number of derivatives and for every $\epsilon>0$,
> $$(\dot g_H)_0 = \dot\mu K^*+c\,\mathcal L_{W^*}g+O(t_*^{-1+\epsilon}),\qquad c = Q[Z'_0]/4\pi^2$$
> (Corollaries R4.6 and R5.4). When $\dot\mu\ne0$ this grows linearly in $v$ and is not (stationary, smooth at $r_h$)
> $+\,o(1)$.

and in its proof (line 836), "(b): Corollary R2.8 for $Z'_0$" reads "(b): Corollary R5.4 for $Z'_0$".

(2) *This file, Theorem R3.4 (iii)-(iv)* (lines 1205-1212; a reading, per (A33)-(A34)):

> (iii) On each $\{r_0<r\le R',\ t_*\ge T'\}$, with every number of derivatives and for every $\kappa\in
> (0,\delta_\sharp)$, $\delta_\sharp = (1-e_\Upsilon)\gamma_\Upsilon$,
> $$\big|\dot g_H-\dot\mu K^*-c_\infty\mathcal L_{W^*}g\big|\le C_\kappa\,t_*^{-1/2-\kappa},\qquad c_\infty =
> \frac1{4\pi^2}\int\ell\big(\chi'J_h+[\Box,\chi']Y\big)\,dv,$$
> $\chi'$ of (A8): a horizon charge (Corollary R5.3).
>
> (iv) For $Y_h$ on $N^+$ with $\Box Y_h = 0$ and Cauchy data compactly supported on $\Sigma^\circ$, $\dot g_H+\mathcal
> L_{Y_h}g$ has (ii), induces $(\dot\gamma,\dot k)$ up to the data of $\mathcal L_{Y_h}g$, and has (iii) with
> $c_\infty+Q[Y_h]/4\pi^2$, as $Y_h-(Q[Y_h]/4\pi^2)W^* = O(t_*^{-1+\epsilon})$ (Corollaries R4.6 and R5.4).

Corollary R4.4's display (lines 1541-1542) reads the same as (iii).

(3) *Supplement 10.2 (iv)* (`N1STAR-PROOF.md`:1795-1798), from "When Z has compactly supported data" to "as in four
dimensions.":

> When Z has data compactly supported on the initial surface it settles to mu-dot K* + c pi_{W*} on each {r <= R} at
> the rate t_*^(-1+eps) for every eps > 0, c the conserved horizon charge of Z divided by that of W* (deduced,
> GAUGEDECAY5 Proposition R2.13 (b) with Corollaries R4.6 and R5.4, with (Dyn), which Part VI.A Theorem 6.1 proves at
> b_0; `checks/admbox5.py` B1-B8, `checks/gdkplus5.py` Q1-Q6); the mass change grows linearly in v, as in four
> dimensions.

(4) *Supplement 10.8* (`N1STAR-PROOF.md`:2940-2942), from "For W' with compactly supported data" to "proves at b_0);":

> For W' with data compactly supported on the initial surface GAUGEDECAY5 Proposition R2.13 (b), with Corollaries R4.6
> and R5.4, gives the rate t_*^(-1+eps), every eps > 0, on each {r <= R} (deduced, with (Dyn), which Part VI.A Theorem
> 6.1 proves at b_0; `checks/gdkplus5.py`);

(5) *The paper, section 8.2.* If round 4's proposal (lines 1857-1867) is seated, replace it, from "In harmonic gauge
every perturbation in the class has a representative" to "could gain at most the constraint damping's margin;", by:

> In harmonic gauge every perturbation in the class has a representative that is in harmonic gauge on the whole domain,
> induces the given data, and equals the solution above near the initial surface. On each region r ≤ R it settles to
> μ̇K* + c π_{W*}, growing linearly in v, with c a conserved horizon charge, at the rate τ^(−1/2−κ) for every κ below
> δ♯ = (1 − e_Υ)γ_Υ, the margin by which the constraint damping makes the gauge source decay along the forward cone; a
> model computation indicates that τ^(−1/2−δ♯) is the true rate when the spherically symmetric part of that source
> does not vanish. A gauge change whose gauge vector Z solves □Z = 0 with data compactly supported on the initial
> surface moves only c, and Z itself settles to a multiple of W* at the rate τ^(−1+ε) for every ε > 0 (deduced from
> the supplement's proved parts: GAUGEDECAY5 R3.4, R4.3, R4.4, R4.6, R5.1–R5.4; `docket68/n1star/checks/gdscri5.py`,
> `checks/gdext5.py`, `checks/gdkplus5.py`). Without decay of those data the growth can be traded for a stationary
> term that does not decay at infinity;

If the paper still carries its present sentence (`paper/RESPONSE-HL-5D.md`:805-810), replace in it "when Z has
compactly supported data it settles on each region r ≤ R to μ̇K* + c π_{W*}, growing linearly in v, at the rate
τ^(−1/2) (deduced from the zero-energy structure of the 1-form wave operator, supplement GAUGEDECAY5 R2.13,
`docket68/n1star/checks/admbox5.py`," by:

> when Z has data compactly supported on the initial surface it settles on each region r ≤ R to μ̇K* + c π_{W*},
> growing linearly in v, at the rate τ^(−1+ε) for every ε > 0 (deduced from the zero-energy structure of the 1-form
> wave operator and its estimate at positive weight at timelike infinity, supplement GAUGEDECAY5 R2.13, R4.6 and R5.4,
> `docket68/n1star/checks/admbox5.py`, `checks/gdkplus5.py`,

(6) *The paper, section 9*, round 4's proposal (lines 1872-1876): "settles to μ̇K* + c π_{W*} at τ^(−1/2)." reads
"settles to μ̇K* + c π_{W*} at τ^(−1/2−κ) for every κ below the constraint damping's margin δ♯."

(7) *The paper's list of checks*, after the entry for `checks/admbox5.py`:

> - `checks/gdkplus5.py` Q1–Q6: section 8.2's rates in harmonic gauge (supplement GAUGEDECAY5 round 5). Q1, the
>   dictionary between the time-weighted and the b-weighted spaces; Q2, the zero-energy gap (0, 2) of the 1-form wave
>   operator, the window (0, 1) inside it and the radiation root 3/2; Q3, W* decays like r⁻², and the order of its
>   cut-off transform; Q4, the time transform t^(−α) ↔ σ^(α−1) that turns a zero-frequency weight into a rate; Q5,
>   every weight condition of the carried-over steps on the whole parameter box; Q6, the rate: κ < min(1/2, a − 5/2)
>   for a source of order a at timelike infinity, every κ < δ♯ for the gauge source and every κ < 1/2 for compactly
>   supported gauge data, never above the formal model's exponent. Each with a control that must fail. Exact.

*Files.* `GAUGEDECAY5.md` (this section appended); `checks/gdkplus5.py` with `checks/gdkplus5.out`.

## Round 6 (2026-11-02)

*Status.* Written 2026-11-02 (round 6, this section). Not verified by a second reader. Rounds 1-5 are left as they
stand; every change to them is a numbered amendment, (A37)-(A56) in section R6.g, the findings of the verifiers of
rounds 4 and 5 among them. New program: `checks/gdrad5.py` (D1-D13) with `checks/gdrad5.out`; every check has a control
that mutates the computed path and must fail, and fails. Labels as in rounds 1-5. Readings use round 5's abbreviations
(I3, I4, G2, F2, D, H$'$) and I2 for `PART-III-I2-SCRI.md` (III.I$'$) and H for `PART-III-H-AUGMENT.md`, all under
`proof5/`. Section headings are lettered (R6.a-R6.h).

*The result, in one paragraph.*
- **III.I$'''$ Proposition 2.1 with Lemmas 1.1-1.3 carries over to $\Box$** (Lemmas R6.1-R6.3, Theorem R6.4). For a
  source of $K^+$-weight $\alpha_K\in(1,2)$ and $\iota^+$-weight $\gamma_++2$, $\gamma_+\in(\alpha_K,2)$, the forward
  solution is $c_0\chi_KW^*$ plus a remainder of $K^+$-weight $\alpha_K-1$, and finer, $u'+\beta W^*$ with $u'$ and the
  coefficient $B$ at $K^+$-weight $\alpha_K$; $c_0 = (4\pi^2)^{-1}\int\ell(f)$. The zero-frequency Taylor term
  $\hat f(0) = \int f\,dt_*$ is inverted by the augmented operator at $\alpha+2 = \gamma_+-1$ (round 5's stop), and one
  integration in $t_*$ suffices. The cap $\alpha_K<2$ is the zero-energy window, not the radiation field.
- **The rate** (Theorem R6.5): $u-c_f(t_*)W^* = O(t_*^{-\alpha_K})$ on compact sets for every $\alpha_K<2$.
- **A gauge vector with $\Box Y = 0$ and data compactly supported on $\Sigma^\circ$ settles at $t_*^{-2+\epsilon}$**
  (Corollary R6.6), for every $\epsilon>0$, to $(Q[Y]/4\pi^2)W^*$. The route is a cut-off with compact support in
  spacetime, admissible because $Y$ vanishes near $\Sigma^\circ$ off the domain of influence of the data; it gives a
  smooth compactly supported source. Round 5's "next cap $t_*^{-3/2}$ from the radiation field" belongs to the slab and
  cone route of Corollary R4.6, whose cone source inherits II.F$'$'s a priori $\iota^+$-weight $b_+<\frac32$: it is a
  cap of that route, not of the rate.
- **The low-frequency expansion, settled** (Proposition R6.7, formal; computed D5-D6). The round-4 verifier's m1 is
  right: on Tangherlini the first non-smooth term of $\Box$'s resolvent at zero energy is $\sigma\log\sigma$, one
  order above $\sigma^0$ and two above the pole, with coefficient $-\frac i{8\pi^2}\,d\psi\otimes\ell$; round 4's
  $\sigma^2\log\sigma$ is the free kernel's. Its time-domain counterpart is
  $Y-(Q/4\pi^2)W^* = \frac Q{8\pi^2}t_*^{-2}\,d\psi+o(t_*^{-2})$, so the proved exponent $2-\epsilon$ is the formal one
  up to $\epsilon$. No $\sigma^0\log\sigma$ term, so no $t_*^{-1}$ tail: that is proved (Theorem R6.4).
- **The harmonic-gauge exponent is sharp in its source class** (Lemma R6.8, Proposition R6.9; computed D7). The
  $l = 0$ part of the harmonic-gauge source is exactly $\Box$ of a radial 1-form, $F_{Y,0} = \Box(X_{\mathrm{RW},0}+
  \dot\mu(1-\chi_K)W^{**}_H)$. Within that form there is an explicit source of $\iota^+$-order $\frac52+\delta_\sharp$
  whose solution is $\chi'v^{-1/2-\delta_\sharp}d\psi$ exactly, with metric part $\mu_0v^{-1/2-\delta_\sharp}\mathcal
  L_{W^*}g+O(v^{-3/2-\delta_\sharp})$. "Formally sharp" is replaced by "sharp in the class" (proved). Whether the
  source of a particular perturbation attains the bound is the value of one coefficient, and the theorem does not
  depend on it.
- **III.I$'$ at $\Box$** (Lemma R6.10, Propositions R6.11-R6.12, Corollary R6.13; computed D13). At $\mathscr I^+$,
  $\rho_I^{-1}\rho_+^{-2}\Box = 2(X_+-X_I)(X_I-\frac32)+\rho_I\mathrm{Diff}^2_{\mathrm b}$ on Cartesian components, every
  component carries a radiation field, the index set is $\{(\frac32+j,0)\}$ with no logarithm, and the gauge vector of
  Corollary R6.6 has that expansion at $\mathscr I^+$ to every order, with $\iota^+$-weight up to $2-\epsilon$.
- **Verifiers.** The round-4 verifier's report (no mathematical error; M1, m1-m5, n1-n8) and the round-5 verifier's
  (no major error; minors 1-8 and nits) are seated as (A37)-(A56). Corrected checks for their findings are D1-D3, D8-D12.
- **Replacement texts** (section R6.h) for R2.13 (b), R3.4 (iii)-(iv), Corollary R4.4, supplement 10.2 (iv) and 10.8,
  and the paper's sections 8.2 and 9 and its list of checks, superseding rounds 4 and 5's.

### R6.a III.I$'''$ Lemmas 1.1-1.3 at $\Box$

*Setting* (READ, I4:24-33, I3:22-60). As in R5.a: $M'$, $X^\pm_{\mathrm{sc}\text-\mathrm b}$ with faces scf, tf, zf,
$\rho = \langle x\rangle^{-1}$, and $\chi_{\mathrm{zf}} := \chi_1(|\sigma|\langle x\rangle)$, II.G$'$ section 3.1's
cut-off; $c\le\frac1{8\sqrt5}$ and below the $k$-independent bound that makes $\chi_{\mathrm{zf}} = 1$ on
$\mathrm{supp}\,\varphi$ ($\varphi$ of R2.1). $L_b = \Box$ at $b_0$, $\hat P(\sigma)$ its spectral family, $\tilde
P(\sigma)$ Definition R2.1's augmentation, with one column $\hat f_*$ and no $\mathcal S_1$-column.

**Lemma R6.1 (III.I$'''$ Lemma 1.1 at $\Box$; deduced, computed D1).** I4:35-58 verbatim: no operator enters, only
$P\in\rho^p\mathrm{Diff}^m_{\mathrm b}(\bar X)$ with smooth coefficients. The Fubini count of (a) is D1 (b): the weight
it produces is $\rho^{-2(\gamma_{\mathrm{tf}}-j)}$ exactly, and the inner integral converges iff
$\gamma_{\mathrm{zf}}<j$ (control in D1: the weights of the column at $q = 1$).

**Lemma R6.2 (III.I$'''$ Lemma 1.2 at $\Box$; deduced, computed D1, D5).** For $u_0\in H^{\infty,a}_{\mathrm b}(X)$ and
$|\sigma|\le c$: (a) $(\hat P(\sigma)-\hat P(0))(\chi_{\mathrm{zf}}u_0)\in H^{\infty,(\infty,a+2,\gamma_{\mathrm{zf}})}
_{\mathrm b}$ for every $\gamma_{\mathrm{zf}}<1$; (b) $\hat f_*(\sigma)-\chi_{\mathrm{zf}}\hat f_*(0)\in H^{\infty,(N,
3-\epsilon,1-\epsilon)}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-\mathrm b})$ for every $N$ and $\epsilon>0$, and $\hat
f_*(0)\in\mathcal A^3$.

*Proof.* (a) $\hat P(\sigma)-\hat P(0) = -i\sigma L_1-\sigma^2L_2$ with $L_1\in\rho\,\mathrm{Diff}^1_{\mathrm b}$,
$L_2\in\rho^2C^\infty$ near $\partial X$ (R2.1, from III.D Lemma 2.1 (1)-(3); in the retarded frame $L_2 = 0$, D5);
then I4:76-83 verbatim. (b) $\hat f_*$ is the transform of $[\Box,\chi_K]W^*$ (Definition R2.1); by Lemma R2.2 (c),
III.H Lemma 2.4 (a) holds for it: $\hat f_* = \hat f_c+\hat f_\infty$, $\hat f_c$ entire and supported in $\{r\le2\}$,
$\hat f_\infty = r^{-3}G(\sigma r,x)$ with $G$ entire and rapidly decreasing for $\mathrm{Im}\,\zeta\ge0$. The form
$r^{-3}G(\sigma r)$ is the homogeneity of the commutator: D1 (a) computes $r^4[\Box_0,\chi(r/t)]r^{-2}$ as a function
of $r/t$ alone (control: on the Killing form's component $r^0$ it is $r^2$ times one), and B2 with Lemma R2.2 (a)
gives the $O(r^{-4})$ bound with the mass. Then I4:84-96 verbatim; the Fubini count is D1 (b): finite iff
$\gamma_{\mathrm{zf}}<1$ and $\gamma_{\mathrm{tf}}<3$ (control: $q = 1$ gives $\gamma_{\mathrm{tf}}<1$). $\hat
f_*(0)\in\mathcal A^3$ is Lemma R2.2 (b). $\square$

**Lemma R6.3 (III.I$'''$ Lemma 1.3 at $\Box$; deduced, computed D1).** With $G_1(\sigma)b := \Psi(\sigma,\cdot)bW^*$
(R5.1 step 3) and $b_0\in\mathbb C$, $\chi(|\sigma|)G_1(\sigma)(b_0)-\chi_{\mathrm{zf}}b_0W^*\in H^{\infty,(N,2-\epsilon,
1-\epsilon)}_{\mathrm b}$ for every $N$, $\epsilon>0$, and $W^*\in H^{\infty,2-\epsilon}_{\mathrm b}(X)$.

*Proof.* I4:107-117 for $G_1$ alone (there is no $G_2$: no generalised state): $\Psi = \Phi(\sigma r)$ for $r\ge1$,
$\Phi(0) = 1$ (III.H Lemma 2.5 (b)), $W^*\in\mathcal A^2$ (Q3), and the Fubini count with $\langle x\rangle^{-2}$ gives
$\gamma_{\mathrm{tf}}<2$ (D1 (b) at $q = 2$). D1 (c) computes the cut-off state's tf-order with the weight $W_\beta$ of
II.G$'$ Lemma 4.6's proof, not by assignment: $\|W_\beta^{-1}\Phi(\sigma r)r^{-2}\|_{L^2(\mu_{\mathrm b})} =
\sigma^{2-\epsilon}(2\epsilon)^{-1/2}(1+o(1))$ (control: $q = 0$ gives the order $-\epsilon$). $\square$

### R6.b III.I$'''$ Proposition 2.1 at $\Box$, and the rate

**Theorem R6.4 (III.I$'''$ Proposition 2.1 at $\Box$, at $b_0$; deduced, computed D1-D3).** Let $\alpha_K\in(1,2)$,
$\gamma_+\in(\alpha_K,2)$, $\epsilon_1\in(0,\frac12)$, $w_I\ge\max(\frac52,\gamma_++1+\epsilon_1)$ and
$$f\in H^{\infty,(w_I,\gamma_++2,\alpha_K)}_{\mathrm b}(\Omega_*;T^*)^{\bullet,-}\quad\text{(plain weights, no
expansion at }\mathscr I^+),\tag{R6.1}$$
and let $u$ be the forward solution of $\Box u = f$ (II.F$'$ Theorem 1.1 at $P = P_0 = \Box$). Then for every
$\epsilon\in(0,\frac15(2-\gamma_+)]$:

(i) $u = u'+u_{\mathrm{sing}}$, $u' := u_{\mathrm{hi}}+u_{\mathrm{reg}}\in H^{\infty,(\min(\frac32,\gamma_+)-3\epsilon,
\gamma_+,\alpha_K)}_{\mathrm b}(M')$;

(ii) $u_{\mathrm{sing}} = \beta(t_*,r)W^*$, $\partial_{t_*}\beta(\cdot,r) = (\partial_t\chi_K)(\cdot,r)*B$,
$\beta(\cdot,r)-\beta(\cdot,r') = (\chi_K(\cdot,r)-\chi_K(\cdot,r'))*B$, with $B\in H^{k,\alpha_K}_{\mathrm b}(\mathbb
R)$ (II.G$'$ Definition 2.1, G2:79-81) and $\int B = c_0 := (4\pi^2)^{-1}\int\ell(f)\,dv$;

(iii) $u-c_0\chi_KW^*\in H^{\infty,(\min(\frac32,1+\gamma_+-\alpha_K)-3\epsilon,\gamma_+-2\epsilon,\alpha_K-1)}_{\mathrm
b}(M')$: at $K^+$, $u = c_0W^*$ plus a term of weight $\alpha_K-1>0$.

At each order $k$ the norms are bounded by $C_k$ times the norm of $f$ in (R6.1) at an order $k+\ell$, $\ell$
independent of $k$. $u'$, $u_{\mathrm{sing}}$ and $B$ depend on $k$ through $c = c_k$ (I3:193-198); $u$ and $c_0$ do
not. (The same caveat applies to Theorem R5.1 (i)-(ii): (A52).)

*Proof: the steps of III.I$'''$ Proposition 2.1, and why each carries over.* References are to I4 unless said otherwise.
- *Step 0* (I4:133-144) improves $u$ through III.I$''$ Proposition 5.1 and the error $(L-L_b)u$. Here $L = L_b = \Box$,
so it is void. - *Step 1* (I4:145-158) removes the source's terms at $\mathscr I^+$ by III.I$'$ Proposition 3.1. (R6.1)
has none, as $w_I\ge\gamma_++1+\epsilon_1$ is what Step 2 asks; so $u^\flat = u$, $f^\flat = f$. For sources with
$\mathscr I^+$-terms, Proposition R6.12 does what Step 1 does, with the $\iota^+$-index sets it states. - *Step 2*
(I4:159-171). The decomposition $u = u_{\mathrm{hi}}+u_{\mathrm{reg}}+u_{\mathrm{sing}}$ is R5.1 step 3 (III.H$'$ at
$\Box$, R2.5's proof). III.I$''$ Lemma 4.1 (I3:216-242) applies with $(\beta^f_I+1,\beta_\iota+2,\beta_K) =
(w_I,\gamma_++2,\alpha_K)$. Its conditions are $\beta_K\in(0,\infty)\setminus\mathbb N$, $\beta^f_I\ge\frac32$ and
$\beta^f_I+1\ge\beta_\iota+2-\min(\beta_K,1-\epsilon_1) = \gamma_++1+\epsilon_1$ (as $\alpha_K>1$). These are the
hypotheses on $\alpha_K$ and $w_I$ (D2), and its inputs at $\Box$ are R5.1 step 4's. So $u_{\mathrm{hi}}\in
H^{\infty,(\frac32-\epsilon,N,N)}_{\mathrm b}$. (2.25a) (II.G$'$ Proposition 3.3 (1), G2:422-431, with $\beta_K =
\alpha_K\in(1,2)$) gives, as I4 (2.3) does,
$$\hat f|_{\pm(0,c]}\in H^{\infty,(\min(w_I,\gamma_++2)-\epsilon,\gamma_++1,((0,0),\alpha_K-1))}_{\mathrm b}(X^\pm
_{\mathrm{sc}\text-\mathrm b}),$$
with zf-coefficient $\hat f(0) = \int f\,dt_*\in H^{\infty,\gamma_++1}_{\mathrm b}(X)$, the same for both signs
($f(\cdot,x)$ is integrable, as $\alpha_K>1$). The density step is R5.1 step 3's, with $b_+ := 1$, $b_I := \frac54$ in
II.F$'$ (1.4) ($\frac12<b_+<b_I<\frac32$, $b_+\le\gamma_+$, $b_I+1\le w_I$; D2). - *Step 3.1, zero energy* (I4:172-193).
Proposition R2.3 at the weight $\alpha := \gamma_+-3$: $\alpha+2 = \gamma_+-1\in (0,1)$; $\mathcal Y_0$ has $\mu_{\mathrm
b}$-weight $\alpha+4 = \gamma_++1$, so $\hat f(0)\in\mathcal Y_0$; and the column $\hat f_*(0)\in\mathcal A^3$ lies in
$\mathcal Y_0$ as $\gamma_++1<3$ (D2). Put $(\hat u_0,c_0) := \tilde P(0) ^{-1}(\hat f(0),0)$, $\hat u_0\in
H^{\infty,\gamma_+-1}_{\mathrm b}(X)$. Applying $\ell$ to $\hat P(0)\hat u_0+c_0\hat f_*(0) = \hat f(0)$ gives $c_0 =
\ell(\hat f(0))/4\pi^2$: $\ell\circ\hat P(0) = 0$ on $\mathcal X_0$ and $\ell(\hat f_*(0)) = 4\pi^2$ (R2.3's proof, B3),
and $\ell(\hat f(0)) = \int\ell(f)\,dv$, $t_*-v$ being a function of $r$. As at I4 (2.5), for $0<|\sigma|\le c$, $\tilde
P(\sigma)(\chi_{\mathrm{zf}}\hat u_0,c_0) = (\hat f(\sigma)-\hat f_2(\sigma),0)$, with
$$\hat f_2 := (\hat f-\chi_{\mathrm{zf}}\hat f(0))-[\hat P(0),\chi_{\mathrm{zf}}]\hat u_0-(\hat P(\sigma)-\hat P(0))
(\chi_{\mathrm{zf}}\hat u_0)-c_0(\hat f_*(\sigma)-\chi_{\mathrm{zf}}\hat f_*(0)).$$
The row $\langle\cdot,\varphi\rangle_h$ is $\sigma$-independent, $\langle\chi_{\mathrm{zf}}\hat u_0,\varphi\rangle =
\langle\hat u_0,\varphi\rangle = 0$, and $\chi_{\mathrm{zf}}\hat u_0\in\mathcal X_\sigma$ by compact support. The four
terms lie in $H^{\infty,(\cdot,\gamma_++1,\alpha_K-1)}$ (definition of the space), $H^{\infty,(\infty,\gamma_++
1,\infty)}$ (Lemma R6.1 (b), $p = 2$, $\hat P(0)\in\rho^2\mathrm{Diff}^2_{\mathrm b}$), $H^{\infty,(\infty,\gamma_++
1,\gamma_{\mathrm{zf}})}$ (Lemma R6.2 (a), $a = \gamma_+-1$) and $H^{\infty,(N,3-\epsilon,1-\epsilon)}$ (Lemma R6.2 (b)).
As $\gamma_++1\le3-\epsilon$ and $\alpha_K-1<1-\epsilon$ (D2),
$$\hat f_2|_{\pm(0,c]}\in H^{\infty,(\frac52-\epsilon,\gamma_++1,\alpha_K-1)}_{\mathrm b}(X^\pm_{\mathrm{sc}\text-
\mathrm b}).$$
- *Step 3.2* (I4:195-207). $(\hat u_{\mathrm{reg},1},\hat b_1) = (\chi_{\mathrm{zf}}\hat u_0,c_0)+\tilde P(\sigma)^{-1}
(\hat f_2,0)$. III.I$''$ Lemma 4.2 (I3:244-269), at $\Box$ as in R5.1 step 6, applies with $\beta_{\mathrm{scf}} :=
\frac32-\epsilon$, $\beta_{\mathrm{tf}} := \gamma_+-1$, $\beta_{\mathrm{zf}} := \alpha_K-1$ and the window $\alpha'+2 :=
\gamma_+-\alpha_K\in(0,1)$ (Theorem R2.4 at that weight). It gives $\hat u_{\mathrm{reg},1}\in H^{\infty,(\frac32-
2\epsilon,\gamma_+-1,((0,0),\alpha_K-1))}_{\mathrm b}$ and $\hat b_1\in H^{\infty,((0,0),\alpha_K-1)}_{\mathrm b}(\pm(0,
c],|\frac{d\sigma}\sigma|)$ with coefficient $c_0$ at $\sigma = 0$, the same for both signs. (2.26a) (II.G$'$ Proposition
3.5 (1), G2:526-538), with $\beta_K = \alpha_K\in(1,2)$ and its one Taylor coefficient, of order $0<\alpha_K-1$, agreeing
for the two signs, gives $u_{\mathrm{reg}}\in H^{\infty,(\min(\frac32,\gamma_+)-3\epsilon, \gamma_+,\alpha_K)}_{\mathrm
b}(M')$, as I4 (2.8) does. With Step 2 this is (i). - *Step 3.3, the singular part: one integration* (in place of
I4:209-241). $\mathcal F(\partial_{t_*}u_{\mathrm{sing}}) = \chi(|\sigma|)G_1(\sigma)(\hat b_1)$ (R5.1 step 3). Lemma
R6.3 applies for $c_0$, and III.I$''$ Lemma 4.3 (I3:271-305, R5.1 step 8) with $a = \alpha_K-1$ for $\hat b_1-c_0$, of
tf-weight $\alpha_K+1-\epsilon>2-\epsilon$. So $\mathcal F(\partial_{t_*}u_{\mathrm{sing}})\in
H^{\infty,(N,2-\epsilon,((0,0),\alpha_K-1))}_{\mathrm b}$, with zf-coefficient $c_0W^*$, the same for both signs.
III.I$''$ Lemma 3.1 (I3:115-131) is applied once, to $u := u_{\mathrm{sing}}$, with $\beta_I := 1+\gamma_+-\alpha_K$,
$\beta_\iota := \gamma_+$, $\beta_K := \alpha_K-1\in(0,1)$. Its hypotheses are: $\beta_\iota>\beta_I$ (as $\alpha_K>1$);
$\beta_K\le\beta_\iota-\beta_I$ (an equality); $\beta_K\in(-1,1)\setminus\{0\}$; the zf-restrictions agree ($\beta_K>0$);
(3.1)'s tf-weight $2-\epsilon\ge\gamma_+$ ($\epsilon\le\frac15(2-\gamma_+)$); the bound on $\Omega_<$, from
$u_{\mathrm{sing}} = -(u_{\mathrm{hi}}+u_{\mathrm{reg}}) $ for $t_*<1$, of weights $(\cdot,\gamma_+,\alpha_K)$, at least
$(\infty,\beta_\iota,\beta_K)$; and the support of $\mathcal Fu_{\mathrm{sing}}$ in
$\mathrm{supp}\,\chi(|\cdot|)\cup\{0\}$ (R5.1 step 9). So $u_{\mathrm{sing}}\in
H^{\infty,(1+\gamma_+-\alpha_K,\gamma_+-\epsilon,((0,0),\alpha_K-1))}_{\mathrm b}(M')$. Its $(0,0)$-coefficient at $K^+$
is $\lim_{t_*\to\infty}u_{\mathrm{sing}} = \int\partial_{t_*}u_{\mathrm{sing}}\,dt_* = \mathcal F(\partial_{t_*}
u_{\mathrm{sing}})(0) = c_0W^*$. This is I4 Step 3.4's argument (I4:242-249) for one integration, $\partial_{t_*}
u_{\mathrm{sing}}(\cdot,x)$ being integrable since its $K^+$-weight is $\alpha_K>1$. Replacing $c_0W^*$ by $c_0\chi_KW^*$
($\chi_K = 0$ near $\mathscr I^+$; weights $(\infty,2-\epsilon,0)$) gives (iii). - *Step 3.4, the coefficient $B$* (R5.1
step 10). $B := \mathcal F^{-1}(\chi\hat b_1)$. The pair $(\chi\hat b_1|_{\sigma<0},\chi\hat b_1|_{\sigma>0})$ lies in
II.G$'$ Definition 2.7's $X^{k,\alpha_K-1}$ (G2:233-237). Its polynomial part, of degree $<\alpha_K-1\in(0,1)$, is the
constant $c_0$, the same for both signs. II.G$'$ Proposition 2.8 (2) (G2:246-253) with $\beta =
\alpha_K\in(1,2)\setminus\mathbb N$ gives $B\in H^{k,\alpha_K}_ {\mathrm b}(\mathbb R)$, and $\int B = (\chi\hat b_1)(0)
= c_0$. D3 computes the pair: the transform of $(1+t)^{-\alpha_K}$ is $\int B+\Gamma(1-\alpha_K)w^{\alpha_K-1}+O(w)$ at
four rational $\alpha_K\in(1,2)$. The control runs the same path at $\alpha_K = 2$: there the remainder over $w$ diverges
like $\log w$, $\Gamma(-1)$ being infinite. The identities of (ii) are R2.5 (ii)'s. - *Step 4* (I4:258-270) is III.I$'$
Proposition 2.1, the expansion at $\mathscr I^+$. It is not needed for (i)-(iii); at $\Box$ it is Proposition R6.11.
$\square$

*What changes against III.I$'''$, and where this one stops.* There are no Steps 0 and 1. There is one state and no
generalised partner, so one integration, and the $K^+$-term is the constant $c_0W^*$ where $L$ has $t_*h(\dot S)$. The
$\iota^+$-weight $\gamma_+$ may exceed $\frac32$. For $L$, III.I$'''$ (2.2) caps it at $\frac32+(1-e_\Upsilon)
\gamma_\Upsilon$ through the formal solutions of Step 1, which (R6.1) does not need. The cap here is $\gamma_+<2$: the
zero-energy inversion of Step 3.1 needs $\alpha+2 = \gamma_+-1<1$, the column $\hat f_*(0)\in\mathcal A^3$ having to
lie in $\mathcal Y_0$. The bookkeeping is D2, each condition a positive sum on the whole box $\alpha_K\in(1,2)$,
$\gamma_+\in(\alpha_K,2)$, $\epsilon$, $\epsilon_1$, with $w_I$ from its least admissible value. D2's control drops
Step 3.1: Lemma 4.2 would then be applied to $\hat f$ itself, whose plain zf-weight is that of its Taylor term, 0,
below $\beta_{\mathrm{zf}} = \alpha_K-1$, which was round 5's stop at $\alpha_K = 1$. At $\alpha_K = 2$ II.G$'$
Propositions 2.8, 3.3 and 3.5 exclude the integer, and the Taylor term of order 1 enters with $\sigma\log\sigma$ (D3's
control, Proposition R6.7). This is a stop of the method as carried; Proposition R6.7 says what lies beyond it.

**Theorem R6.5 (the rate at $K^+$-weight $\alpha_K\in(1,2)$; deduced from Theorem R6.4, Lemma 2.2 and B4).** Let $f$,
$u$ be as in Theorem R6.4 and $R'>r_0$. On $\{r_0<r\le R',\ t_*\ge8\max(R',1)\}$, with every number of derivatives in
$x$ and $t_*$ (the constant depending on the number),
$$\big|u-c_f(t_*)W^*\big|\le C\,t_*^{-\alpha_K}\|f\|,\tag{R6.2}$$
with $c_f$ of (R2.2). In particular, if $\ell(f)$ vanishes for large $v$, $u = c_\infty W^*+O(t_*^{-\alpha_K})$.

*Proof.* R5.2's proof verbatim, with Theorem R6.4 (i)-(ii) for R5.1 (i)-(ii). $|B(t)|\le C\langle t\rangle^{-\alpha_K}
\|f\|$ by Lemma R2.6 on $[\frac T2,4T]$, as $\langle t\rangle^{\alpha_K-\frac12}(B,t\partial_tB)\in L^2(dt)$, and the
convolutions sample $B$ on $[\frac{t_*}2,t_*]$ ((A20)). $u' = O(t_*^{-\alpha_K})$ with its b-derivatives by b-Sobolev
embedding near $K^+$, where $\rho_K\asymp t_*^{-1}$ on compact $r$-sets; so $|Q[u']|\le Ct_*^{-\alpha_K}\|f\|$, and
$4\pi^2\beta(t_*,r_h) = 4\pi^2c_f+O(t_*^{-\alpha_K})$ as in R2.7's step (4). $\square$

### R6.c Compactly supported gauge data: the rate $t_*^{-2+\epsilon}$

**Corollary R6.6 (deduced; computed D4).** Let $Y$ be a smooth 1-form on $N^+$ with $\Box Y = 0$ whose Cauchy data on
$\Sigma^\circ$ have compact support. For every $\epsilon>0$, on each $\{r_0<r\le R',\ t_*\ge T'\}$ and with every
number of derivatives,
$$\big|Y-(Q[Y]/4\pi^2)W^*\big|\le C_\epsilon\,t_*^{-2+\epsilon},\tag{R6.3}$$
$Q[Y]$ being constant at late times. Hence Corollary R4.6's late-time clause, Proposition R2.13 (b) and the
$Y_h$-clauses of Theorems R2.12 (iv), R3.4 (iv) and Corollary R4.4 hold with $t_*^{-2+\epsilon}$ for the gauge
vector's part.

*Proof.* (1) *The cut-off.* Let $K\subset\Sigma^\circ$ be the support of the data. $Y$ vanishes on $N^+\setminus J^+(K)$,
a relatively open set containing $\Sigma^\circ\setminus K$ (domain of dependence on $\Omega^\sharp$, IX Lemmas 1.1-1.2,
with Lemma R3.1). Take $\chi\in C^\infty_c(M^\circ)$ equal to 1 on a neighbourhood of $K$. Then $U := (1-\chi)Y$ vanishes
on a neighbourhood of $\Sigma^\circ$: near $K$ because $\chi = 1$, elsewhere because $Y = 0$. So $F := \Box U =
-[\Box,\chi]Y$ is smooth, supported in a compact subset of $N^+$, and vanishes near $\Sigma^\circ$. (2) *The forward
problem.* Let $T_a := \min t_*$ on $\mathrm{supp}\,F$. For $p\in N^+$ with $t_*(p)<T_a$, $J^-(p)$ within $N^+$ lies in
$\{t_*<T_a\}$ ($dt_*$ is timelike, III.B Lemma 3.7 (a), B:228-229), where $F = 0$; so $U(p) = 0$ by uniqueness with zero
data (IX Lemma 1.1 on $\Omega^\sharp$, Lemma R3.1). Extended by 0 below $\Sigma^\circ$, $U$ is smooth on $\{t_*\ge T_a,\
r\ge r_0\}$, vanishes for $t_*<T_a$, and solves $\Box U = F$ there. As $g_{b_0}$ is stationary ($\partial_{t_*}$ is
Killing), the translate of $U$ by $1-T_a$ in $t_*$ is the forward solution on $\Omega_*$ (II.E Proposition 3.4) of the
translate of $F$. That source is smooth with compact support, so it lies in (R6.1) for every $\alpha_K<2$, $\gamma_+<2$
and $w_I$. (3) *The rate.* On compact $r$-sets at late times $\chi = 0$ and $Y = U$. Theorem R6.5 with $\alpha_K :=
2-\epsilon$ and $\gamma_+\in(\alpha_K,2)$ gives $|U-c_fW^*|\le Ct_*^{-2+\epsilon}$. Once $\chi = 0$ near the horizon,
$c_f(t_*) = (4\pi^2)^{-1}\int^{v_h(t_*)}\ell(F) = Q[U]/4\pi^2 = Q[Y]/4\pi^2$, by (2.1) and $U = 0$ for $t_*<T_a$. For
R2.13 (b): $\mathcal L_{Z'_0}g-c\,\mathcal L_{W^*}g = \mathcal L_{Z'_0-cW^*}g$. $\square$

*What this replaces, and why round 5 stopped short.* R2.8's original proof took a cut-off $\chi(t_*)$ in time; its
commutator reaches $\mathscr I^+$, the false step of (A23). Corollary R4.6 repaired the route with the slab estimate of
Proposition R4.2 and a cone cut-off $\chi'$, and Corollary R5.4 kept that route. The cone source $[\Box,\chi']Y$ there
has $\iota^+$-order $b_++2$, $b_+<b_I<\frac32$, II.F$'$'s a priori weight, below the radiation order $\frac32$; that is
the "next cap $t_*^{-3/2}$" of R5.4's last paragraph. A cut-off with compact support in spacetime avoids it, and is
admissible because $Y$ vanishes near $\Sigma^\circ$ off $J^+(K)$. R4.6's statement at $\mathscr I^+$ on the slab is
unaffected. D4 computes the exponent: $\kappa_{\sup} = \min(\frac32,a-\frac52)$ for a source of $\iota^+$-order $a$,
$\kappa_{\sup} = \frac32$ for a compactly supported one, and $\kappa<\delta_\sharp$ still for the harmonic-gauge
source. Control: with round 5's $\alpha_K<1$ the compactly supported exponent is $\frac12$.

### R6.d The low-frequency expansion, and the true rate (formal)

**Proposition R6.7 (the first non-smooth term at zero energy; formal, computed D5-D6).** (a) *The operator.* On $l = 0$
1-forms $a\,dv+b\,dr$, in the retarded frame $T = v-2r_*$, $\hat P(\sigma) := e^{i\sigma T}\Box e^{-i\sigma T} = \hat P
(0)-i\sigma L_1$ exactly ($L_2 = -g^{-1}(dT,dT) = 0$), with $\hat P(0) = (r^{-3}fq',\ \phi'-r^{-3}q')$, $\phi = \delta
Y$, $q = r^3(dY)_{vr}$, round 2's B5 (D5, from $d\delta+\delta d$ on Tangherlini). (b) *The chain.* The formal outgoing
expansion $u_\sigma = W^*+\sigma u_1+\sigma^2(u_2+\log\sigma\,u_{2L})+\dots$ of III.D$'$ Proposition 4.1, Step 1's
$u_\sigma$ has $\hat P(0)u_1 = iL_1W^*$. The time component of $u_1$ is $-i/r+O(r^{-3})$, with no logarithm. The time
component of $u_2$ carries $-\frac12\log r$ at the indicial root 0 (D5; control: the chain started from $rW^*$, a state
decaying like $r^{-1}$, has $-\frac i2\log r$ already at order $\sigma$, which is the chain of the round-4 verifier's
m1). As in the free kernel (G3), the near-zone $\log r$ at the root 0 is the far zone's $\log(\sigma r)$. So $u_{2L}$ is
the bounded horizon-regular stationary solution whose time component is $-\frac12$ at infinity: $u_{2L} =
\frac12(\partial_v)^\flat+\alpha W^*$, $\alpha$ fixed by the normalisation. (c) *The resolvent.* With $\hat
P(\sigma)^{-1}f = w_\sigma-(d_\sigma/c_\sigma)u_\sigma$, $c_\sigma\ell(\psi) = i\sigma q(\sigma,u_\sigma)$ and
$q(0,\cdot) = Q$ (Lemma 2.2: $\ell(\hat P(\sigma)u) = -i\sigma q(\sigma,u)$), the coefficient of $\sigma\log\sigma$ in
$-(d_\sigma/c_\sigma)u_\sigma$ is $-\frac{\ell(f)}{4\pi^2i}(u_{2L}-\frac{Q[u_{2L}]}{4\pi^2}W^*) = -\frac{i\,\ell(f)}
{8\pi^2}\,d\psi$, $d\psi = \mu_0W^*-(\partial_v)^\flat$. It is independent of $\alpha$ (D6; control: without the charge's
$\sigma^2\log\sigma$ term in $c_\sigma$ the coefficient keeps $\alpha$), and $w_\sigma$'s first logarithm is at
$\sigma^2$. So
$$\hat P(\sigma)^{-1}f = \frac i{4\pi^2\sigma}\ell(f)W^*+R_0f-\frac{i\,\ell(f)}{8\pi^2}\,d\psi\;\sigma\log
\sigma+O(\sigma)\quad(\text{formal}),$$
the first non-smooth term being $\sigma\log\sigma$: one order above $\sigma^0$, two above the pole. (d) *Time domain.*
$\mathcal F[t_+^{-2}] = (-i\sigma)\log(-i\sigma)+(\text{analytic})$ (D6, the finite part of $\Gamma(s)(-i\sigma)^{-s}$ at
$s = -1$), and $\sigma\log\sigma = i(-i\sigma)\log(-i\sigma)$ modulo analytic terms. So a solution with charge
$4\pi^2c_\infty$ settles formally as
$$u = c_\infty W^*+\tfrac{c_\infty}2\,t_*^{-2}\,d\psi+o(t_*^{-2}),\qquad\mathcal L_ug-c_\infty\mathcal L_{W^*}g =
\tfrac{\mu_0c_\infty}2\,t_*^{-2}\,\mathcal L_{W^*}g+o(t_*^{-2})$$
on compact sets, since $\mathcal L_{d\psi}g = \mu_0\mathcal L_{W^*}g$ ($(\partial_v)^\flat$ is Killing). For $Y$ of
Corollary R6.6, $c_\infty = Q[Y]/4\pi^2$.

*What is proved and what is formal.* (a) is computed exactly. (b)-(d) are formal: they rest on the matching of the
near-zone logarithm at the root 0 with $\log\sigma$, as for the free kernel. Proved: there is no $\sigma^0\log\sigma$
term and no $t_*^{-1}$ tail, and the rate is $t_*^{-2+\epsilon}$ (Theorems R6.4-R6.5, Corollary R6.6). Proving the
leading term $\frac{c_\infty}2t_*^{-2}d\psi$ would need the expansion past the window, at $\alpha_K>2$, where the Taylor
term of order 1 and $\sigma\log\sigma$ enter (D3's control); II.G$'$ as written excludes integer $K^+$-weights. The
paper states the proved rate and does not state the formal coefficient.

*The round-4 verifier's m1, settled.* R4.5 (a)'s "first non-smooth term $\sigma^2\log\sigma$, two orders above the
pole" is the flat operator's, with no pole. On Tangherlini, relative to the pole $\sigma^{-1}$, the logarithm appears at
order $\sigma^1$, as the verifier found; the verifier's $u_1 = -\frac i2\log r$ is the chain indexed from the pole.
Its consequence is $t_*^{-2}$, not $t_*^{-1}$. "Does not block a first improvement" survives, and is now proved, to
$t_*^{-2+\epsilon}$. (A38) records the readings.

### R6.e The harmonic-gauge exponent: sharp in its source class

**Lemma R6.8 (the spherically symmetric part of the gauge source; deduced from Theorem 1.5 (a), Proposition 2.1 (d),
H1).** On $N^+$ the $l = 0$ part of $F_Y$ of (R3.2) is
$$F_{Y,0} = \Box\big(X_{\mathrm{RW},0}+\dot\mu(1-\chi_K)W^{**}_H\big),\qquad\text{so}\quad J_{h,0} =
\Box X_{\mathrm{RW},0}\ \text{on }\{\chi_K = 1\},\tag{R6.4}$$
$X_{\mathrm{RW},0}$ the $l = 0$ part of the Regge-Wheeler-type gauge vector of Theorem 1.5.

*Proof.* $\dot g = \dot g_{\mathrm{RW}}-\mathcal L_{X_{\mathrm{RW}}}g$ with $(\dot g_{\mathrm{RW}})_0 = \dot\mu K$
(Theorem 1.5 (a), read on $N^+$ by (A2)); $\Theta$ and $\mathcal L_\cdot g$ commute with the $SO(4)$-average ($SO(4)$
acts by isometries); $\Theta(\mathcal L_Xg) = \Box X$ (H1) and $\Theta(K) = -\Box W^{**}_H$ (Proposition 2.1 (d)). So
$F_{Y,0} = -\dot\mu\Theta(K)+\Box X_{\mathrm{RW},0}-\dot\mu\Box(\chi_KW^{**}_H)$. $\square$

So on the cone the spherically symmetric gauge source is $\Box$ of a radial 1-form, exactly, and Proposition R4.5 (c)'s
model coefficient is the $\iota^+$-behaviour of $X_{\mathrm{RW},0}$ there.

**Proposition R6.9 (the exponent is attained in the class; deduced, computed D7).** Let $a\in(\frac52,3)$, $\phi(v) :=
v^{2-a}$, $\chi'$ the cut-off of (A8), $d\psi = \mu_0W^*-(\partial_v)^\flat$ (B5), and
$$f_a := \Box\big(\chi'\phi(v)\,d\psi\big).$$
(a) $f_a$ is $\Box$ of a radial 1-form, as $J_{h,0}$ is (Lemma R6.8). It is supported in $\mathrm{supp}\,\chi'\subset\{r
\le t_*/20\}$, has $\iota^+$-order $a$ and $K^+$-order $a-1$, and lies in (R5.1) for every $\gamma_+<a-2$, $\alpha_K\in
[\frac12,\gamma_+)$ (D7: $\Box(\phi\,d\psi) = (\Box_0\phi)\,d\psi-2\nabla_{\mathrm{grad}\,\phi}d\psi$, $\Box_0\phi =
-3\phi'/r$, and along $r = \lambda v$, $v^{a-1}r\,\Box(\phi\,d\psi)$ has the finite nonzero limit $(3a-6)$ in the $dv$
component; the commutator terms on $\mathrm{supp}\,d\chi'$ have the same orders by S6).
(b) $Q[\phi(v)\,d\psi] = 0$ identically (D7; control: $Q[\phi(v)W^*] = 4\pi^2\phi\ne0$). So $\ell(f_a) = 0$ once
$\chi' = 1$ near the horizon, and $c_f = c_\infty = 0$ at late times.
(c) The forward solution of $\Box u = f_a$ is $u = \chi'\phi(v)\,d\psi$: it is smooth, vanishes for $t_*<T_1$ and solves
the equation (II.E Proposition 3.4). On compact $r$-sets at late times
$$u-c_\infty W^* = v^{2-a}\,d\psi,\qquad\mathcal L_ug = \mu_0v^{2-a}\mathcal L_{W^*}g+2(2-a)v^{1-a}\,dv\otimes_sd\psi
\tag{R6.5}$$
exactly (D7), and $d\psi$ (its $dv$-component is 1) and $\mathcal L_{W^*}g$ ($(\mathcal L_{W^*}g)_{vr} = -\frac7{24}
r_h^{-3}$ at $r = 2r_h$, D7) do not vanish.

So for sources of $\iota^+$-order $a$ the bound $t_*^{-\alpha_K}$, $\alpha_K<a-2$, of Theorem R5.2 is attained up to its
endpoint, with the explicit coefficient $\mu_0\mathcal L_{W^*}g$ in the metric. At $a = \frac52+\delta_\sharp$, the
$\iota^+$-order of the harmonic-gauge source (Proposition R3.2), the solution of $f_a$ decays like
$t_*^{-1/2-\delta_\sharp}$ and no faster. Hence, proved: **Corollary R5.3's rate $t_*^{-1/2-\kappa}$,
$\kappa<\delta_\sharp$, cannot be improved by any estimate that uses of the gauge source its $\iota^+$-order and the
structure (R6.4) of its $l = 0$ part.** This
replaces "formally sharp" (A35, R5.b, R5.d item 2). What Proposition R6.9 does not decide is whether the source of a
given perturbation attains the bound. That is the value of one coefficient, the $\iota^+$-term of order
$\lambda_\sharp-1$ of $X_{\mathrm{RW},0}$ on the cone. The theorem holds whatever that value is, and the paper states
it in that form: a rate valid for every perturbation in the class, sharp for the class of sources it uses.

### R6.f III.I$'$ at $\Box$: the expansion at null infinity

**Lemma R6.10 (III.I$'$ Lemma 1.1 at $\Box$; computed D13, gdext5.py E1-E2).** On $U_I$ with III.I's coordinates (3.1)
(I2:22-31, $\rho_+ = (t_*+1)^{-1}$, $\rho_I = (t_*+1)/|x|$), on Cartesian components,
$$\rho_I^{-1}\rho_+^{-2}\,\Box = 2(X_+-X_I)\big(X_I-\tfrac32\big)\otimes\mathrm{Id}+\tilde L_\Box,\qquad\tilde L_\Box\in
\rho_I\mathrm{Diff}^2_{\mathrm b}\ \text{(smooth coefficients)}.\tag{R6.6}$$
The scalar part is D13: $\rho_I^{-1}\rho_+^{-2}\Box_0$ acts on $\rho_+^m\rho_I^\lambda$ by
$2(m-\lambda)(\lambda-\frac32)$ plus a remainder gaining $\rho_I$ (control: at $n = 3$ the root is 1). The coupling
$C\partial+D$ of Lemma R4.1 (a), of degrees $-3$ and $-4$, has $\rho_I$-orders 2 and 3 there (D13). So $\bar A = 0$ (as
Lemma R4.1 (b) found in Part IV's chart), every Cartesian component is a slot of eigenvalue 0, I2's slot 6. The factor 2
against I2 (1.2) is $\Box$'s normalisation (principal symbol $G$); it moves no root, index set or integration step.

**Proposition R6.11 (III.I$'$ Lemma 2.2 and Proposition 2.1 at $\Box$, at $b_0$; deduced).** Let $u$, $f$ vanish for
$t_*\le1$ with $\Box u = f$ on $U_I$, $f\in H^{\infty,\ell_I+1,\ell_++2}_{\mathrm b}$ (plain weights) and $u\in
H^{\infty,\alpha_I,\ell_+}_{\mathrm b}$ for some $\alpha_I$, where $\ell_I>\frac32$, $\ell_+<\ell_I$ and $\ell_I,\ell_+
\notin\frac32+\mathbb N_0$. Then each Cartesian component is
$$u_c = \sum_{j\in\mathbb N_0,\ \frac32+j<\ell_I}\chi(\rho_I)\rho_I^{\frac32+j}u_{c,j}(\rho_+,\omega)+\tilde u_c,\qquad
\tilde u_c\in H^{\infty,\ell_I,\ell_+}_{\mathrm b},\tag{R6.7}$$
with $\mathscr I^+$-index set $\mathcal E_\Box := \{(\frac32+j,0):j\in\mathbb N_0\}$, no logarithm, the
$\iota^+$-weight $\ell_+$ kept, and $u_{c,0}$ the radiation field of the component.

*Proof.* I2's Lemma 2.2 (I2:72-135) with one slot type. Step 1 (I2:79-93): every eigenvalue is 0, so $\frac32+0>
\alpha_I+\eta$ and the two integrations (III.A Lemmas 1.2 and 3.2) hold in every component. $\tilde L_\Box$ gains a
full power of $\rho_I$ (smooth coefficients), where I2's $\tilde L$ gains $\frac12$. Step 2 (I2:95-110): every
component acquires $(\frac32,0)$, as slot 6 does there. Step 3 (I2:111-134): the shifts are integers, and at $z =
\frac32+j$, $j\ge1$, $X_I-\frac32$ acts by $j\ne0$ (D13's factor $z-\frac32$), so no logarithm is added. Then
Proposition 2.1's Steps 1-2 (I2:136-161) verbatim, with $\mathcal E_+ = \emptyset$ and $\mathcal E^{\mathrm{tot}}_I$
replaced by $\mathcal E_\Box$; III.A Lemma 3.2's conditions are $\ell_+\notin\frac32+\mathbb N_0$ and $\ell_+<\ell_I$.
The $\iota^+$-weight need not stay below $\frac32$. I2's Lemma 2.2 caps it at $\frac32$ because it starts from no a
priori $\iota^+$-information; with the a priori weight $\ell_+$, Step 2 of Proposition 2.1 keeps it, and the
$(\frac32,0)$-term that III.A Lemma 3.2 would add at $\iota^+$ lies above $\ell_+$ only when $\ell_+<\frac32$. For
$\ell_+>\frac32$ its coefficient must vanish, the a priori bound excluding it. $\square$

**Proposition R6.12 (III.I$'$ Proposition 3.1 at $\Box$; deduced, computed D13).** A source term $\chi\rho_I^{z+1}
(\log\rho_I)^kf^{(z+1,k)}$ at $\mathscr I^+$ is solved formally by $\rho_I^z(\log\rho_I)^ku^{(z,k)}$ with
$2(z-\frac32)(X_+-z)u^{(z,k)} = \rho_+^{-2}f^{(z+1,k)}$ plus lower log orders (D13: $L_0(\rho_I^zw) = \rho_I^z(z-\frac32)
(X_+-z)w$), for $z\ne\frac32$. Its $\iota^+$-index set gains $(z,0)$ (III.A Lemma 1.2), as I2 (3.2) records for $L$. At
$z = \frac32$, a source term of $\mathscr I^+$-order exactly $\frac52$, the factor vanishes: no power solves it, and the
formal solution carries $\rho_I^{3/2}\log\rho_I$. This is the radiation root, which I2's index sets avoid ($\min
\mathrm{Re}\,\mathcal E^C_I>\frac32+2\gamma_\Upsilon$). So for $\Box$ the formal solutions' $\iota^+$-index sets start
at the least $\mathscr I^+$-exponent of the source less one: this is III.I$'''$ Step 1 at $\Box$, for sources that
reach $\mathscr I^+$ with an expansion.

**Corollary R6.13 (the expansion of the gauge vector at null infinity; deduced).** Let $Y$ be as in Corollary R6.6 and
$U$ the translate of its proof. For every $\gamma_+<2$ and every $\ell_I>\max(\frac32,\gamma_+)$ off $\frac32+
\mathbb N_0$, $U$ has the expansion (R6.7) near $\mathscr I^+\cap\iota^+$, with $\iota^+$-weight $\gamma_+-2\epsilon$:
every Cartesian component has a radiation field $u_{c,0}$, and the expansion continues in integer steps with no
logarithm. *Proof.* Theorem R6.4 (i), (iii) gives the a priori weights ($\alpha_I = \frac32-3\epsilon$, $\ell_+ =
\gamma_+-2\epsilon$); the source is compactly supported, so (R6.1)'s plain weight holds at every $\ell_I$; Proposition
R6.11. $\square$

The same holds for the cone-localised piece $\chi'Y$ of the harmonic-gauge vector in R5.3's proof, whose source vanishes
near $\mathscr I^+$, with $\iota^+$-weight below $\frac12+\delta_\sharp$. For $Z_1$ itself near $\mathscr I^+$ on the
initial slab the expansion would need the slab source's own expansion, IV$''$ Theorem 2.4 Steps 4-6 at $\Box$ (R4.2 step
6). That is not carried and not used: R4.3 gives the order $p<\min(\frac32,q_{\dot h}-1)$ there, which is what (i)-(ii)
need.

### R6.g Amendments

*The round-4 verifier's findings* (relayed during round 6; verifier of round 4; nothing in the mathematics found false:
R4.2, R4.3, R4.4 and R4.6 hold as deduced).

(A37) *M1, the status claim* (verifier of round 4). Lines 1359-1361, 1586, 1835-1837 and the round-4 paper texts (lines
1863, 1875) say "no hypothesis beyond the write-out's proved parts". Corollary R4.4 also uses Part IX: Lemma R3.1 (IX
Theorem 2.2 Step 3), IX Lemmas 1.1-1.2, and Theorem 1.5 (d). Part IX is labelled verified (D347), repaired (D610),
repair read (D611), not proved. Read each as "from Part VIII and the write-out's proved parts, with Part IX
(verified)". The replacement texts of R6.h carry this as one clause, "with Part IX (verified)", which can be dropped if
Part IX is promoted to proved. Corollary R6.6 uses Part IX in the same way (domain of dependence on $\Omega^\sharp$).

(A38) *m1, Proposition R4.5 (a)* (verifier of round 4). Lines 1603-1613, the summary (1363), the indicial data (1596)
and (GD20) (1838-1841). Relabel R4.5 (a) formal: it is the flat operator's expansion, with no pole. On Tangherlini the
first non-smooth term is $\sigma\log\sigma$, with coefficient $-\frac i{8\pi^2}d\psi\otimes\ell$ (Proposition R6.7,
formal, D5-D6). Read "first non-smooth term $\sigma^2\log\sigma$, two orders above the pole" as "first non-smooth term
$\sigma\log\sigma$, one order above $\sigma^0$ and two above the pole; its time-domain counterpart is $t_*^{-2}$". "Does
not block a first improvement" stands, now as Theorem R6.4.

(A39) *m2, T3's S7 row* (verifier of round 4). `gdr3fix5.py`:161-162 tests $p = \frac32$ against $b_I =
\frac{\beta+2}2$, and fixes $\alpha = 4+\frac d2$. D8 re-encodes S4 and S7 with $b_I = \frac{b_++p}2$, $p\in(\frac12+
\beta,\min(\frac32,q-1))$, $q>\frac32+2\gamma_\Upsilon$ and $\alpha\ge4$ free; every row is a positive sum on the whole
box. Control: the old $b_I$ against the new $p$ fails at $\gamma_\Upsilon = \frac1{20}$. `gdr3fix5.py` is left as the
verifier read it; read T3's S4/S7 rows as D8.

(A40) *m3, compact-support claims outside (A23)'s list* (verifier of round 4). Lines 427-428, 437, 445, 655, 864-866
((S1)), 883-884 ((S3)), 893-894 ((S4)), 922-925 ((GD7)) and 929 ((GD9)): read "data compactly supported on
$\Sigma^\circ$" and cite Corollary R4.6, and for the rate Corollary R6.6 ($t_*^{-2+\epsilon}$). `N1STAR-PROOF.md`
1795-1797 and 2940-2942 cite R2.13 (b) without "on $\Sigma^\circ$": replacement texts in R6.h. Line 1582's promise
("with Corollary R4.6 added to the citation") is discharged by those texts.

(A41) *m4, the paper's section 9 text* (verifier of round 4). "The rate of section 8.2" is, in section 8.2's
Regge-Wheeler part, [HKW18]'s rate. Theorem 1.5 (b) proves Part VIII's rate $t_*^{-w+\epsilon'}$, $w>2$, with two
derivatives lost and a constant depending on $R'$. In harmonic gauge $X$ is determined only modulo solutions of $\Box Y
= 0$ (R2.0, (A13)). R6.h's section 9 text cites Theorem 1.5, states $O(t_*^{-2-\epsilon})$ on $r\le R$ with two
derivatives lost, and says "constructed" for the harmonic gauge.

(A42) *m5, Corollary R4.4 and the section 8.2 text* (verifier of round 4). Add to Corollary R4.4: "and $\dot g_H = \dot
g$ on a neighbourhood of $\Sigma^\circ$". Near $\Sigma^\circ$, $\chi_K = 0$, and $Z_1$ has zero data with source $F_Y =
\chi^\natural_0E^\Upsilon G\dot h$, which vanishes near $\Sigma_{\mathrm{IVP}}$ (R4.3 step (2), K Lemma 1.1 (d)); so $Z_1
= 0$ there by uniqueness with zero data (IX Lemma 1.1 on $\Omega^\sharp$, Lemma R3.1). In the section 8.2 text, "a
gauge change" reads "a gauge change by $Y$ with $\Box Y = 0$", and $c_\infty$ is "the limit of a horizon charge", not a
conserved one (R6.h).

(A43) *n1-n4, the controls* (verifier of round 4). E4's control (`gdext5.py`:339-344) was a hand-written limit; D9
mutates E4's normalisation ($\rho^{-1-\alpha}$), and the claim fails. E3's control printed an uncomputed "True" for the
full 1-form part (`gdext5.py`:304, 328-330); D10 runs the conjugation by $\rho$ through the same radial and full 1-form
pipeline, and both fail. In G4 (b) (`gdrate5.py`:162-163) "converges" and "predicted" were one inequality; D11 computes
the integral. G4 (c) and its control are superseded by Q6 and D4. In E6 (`gdext5.py`:396-402) $f_I$ was identically 0 and
$p>\frac12+\beta$ held by construction; D12 computes $f_I$ from the source's order ($\delta_\sharp>0$, not binding),
reports the interval's non-emptiness and $p_{\max} = \frac12+2\gamma_\Upsilon$, and the control without $|x|^{-1}$
empties it. The old files are left as the verifier read them.

(A44) *n5* (verifier of round 4). Proposition R4.2's heading: read "IV$'''$ Theorem 2.1 (i)-(iii) at $\Box$, without
IV$''$ Theorem 2.4's Steps 4-6 (step 6)".

(A45) *n6* (verifier of round 4). "Why the order is $\min(\frac32,q_{\dot h}-1)$ and not $\frac32$" (line 1531): label
it heuristic, a statement about the method's limit.

(A46) *n7* (verifier of round 4). (A14) cites `N1STAR-PROOF.md`:2938-2940; the text is at 2940-2942. IV$'''$:24-28 is
cited for $\rho_0$ bounded below on the slab; it is at IV$'''$:50. "Two orders above the pole" is superseded by (A38).

(A47) *n8* (verifier of round 4). `gdext5.py`'s docstring says "a few minutes"; E1 alone ran past 21 minutes under
load. Read "up to half an hour under load".

*The round-5 verifier's findings* (relayed during round 6; verifier of round 5; no major error; R5.1 carries III.I$''$
Proposition 5.1 faithfully and R5.2-R5.4 follow; `gdkplus5.py` reran byte-identically, with 11 code mutants all
failing).

(A48) *Minor 1* (verifier of round 5). R5.3's proof (line 2084): "$K^+$-order $\alpha-2-\eta>1$ (Proposition R3.2)"
reads "$K^+$-order $\alpha-2-\eta>2$ ($w = \alpha-2>2$, section 0, Part VIII (2.3)); Proposition R3.2 gives only
$>\frac12$". R5.1 needs more than $\alpha_K = \frac12+\kappa$.

(A49) *Minor 2* (verifier of round 5). (A33) is mis-scoped at lines 428-429. That bullet is R2.7's general class
($t_*^{-1/2}$ at $K^+$-weight $\frac12$) and the homogeneous solutions. Append: "for $K^+$-weight
$\alpha_K\in(\frac12,1)$ Theorem R5.2 gives $t_*^{-\alpha_K}$, and for $\alpha_K\in(1,2)$ Theorem R6.5; homogeneous
solutions with data compactly supported on $\Sigma^\circ$ settle at $t_*^{-2+\epsilon}$ (Corollary R6.6)".

(A50) *Minor 3* (verifier of round 5). Q5 fixed $w_I = 3$, lacked step 7's $\gamma_+\le\frac32-2\epsilon$, and had
vacuous entries (`eq_ok`, `Integer(1)`, a $10^{-6}$ offset). D2 re-encodes R5.1's box with $w_I$ from its least value
$\max(\frac52,\gamma_++2-\alpha_K)$, (2.25a)'s bound at $\epsilon' = \frac12(1-\alpha_K)$, and step 7's condition, with
no vacuous entry; all hold. Read Q5 as D2.

(A51) *Minor 4* (verifier of round 5). Q4's control was a separate branch; D3's control runs the same path at the
integer. Q3's tf-order was assigned and its tail hard-coded; D1 (c) computes it with $W_\beta$. Read Q3-Q4 as D1 (c) and
D3.

(A52) *Minor 5* (verifier of round 5). R5.1 (i)-(ii) read as $k$-independent. $u'$, $u_{\mathrm{sing}}$ and $B$ depend on
$k$ through $c = c_k$ (I3:193-198); $u$ does not. R5.2 uses finite $k$. Theorem R6.4 carries the caveat.

(A53) *Minor 6* (verifier of round 5). "Where this one stops: the operator" (lines 2123-2131), (GD26) and the summary
bullet: the stop at $\alpha_K = 1$ is the method as carried, not an obstruction. The verifier's route (invert
$\tilde P(0)$ on $(\hat f(0),0)$ at $\alpha+2 = \gamma_+-1$, Lemma 1.2 from R2.1 and R2.2 (c), Lemma 1.3 for $G_1$
alone, one integration, Proposition 2.8 (2) with a constant polynomial part) is Theorem R6.4's. With Corollary R6.6's
cut-off it gives $t_*^{-2+\epsilon}$, not the $t_*^{-3/2+\epsilon}$ the cone route gives. Read the paragraph as
superseded by R6.b-R6.c.

(A54) *Minor 7* (verifier of round 5). Incomplete supersession of $t_*^{-1/2}$ for compactly supported gauge data:
R2.S (S1) (line 865), (S3)/(A14) (lines 883-885, 1698), and R4.6's "their rate $t_*^{-1/2}$ stands" (line 1582). Add
them to (A34)'s list, read with Corollary R6.6's $t_*^{-2+\epsilon}$; the texts are R6.h's.

(A55) *Minor 8* (verifier of round 5). R5.e (5) said "deduced from the supplement's proved parts ... R5.1-R5.4" while
round 5 was unverified, and its condition "when the spherically symmetric part of that source does not vanish" was
broader than R4.5 (c)'s. Superseded by R6.h (5). Round 5 is now verified, with minors seated here. Round 6 is not
verified, and the text says so.

(A56) *Nits* (verifier of round 5). (A32) cites 905-907 for R2.5 item 3: it is 908-910. "Is Theorem R5.1" misdescribes
R3.4's ask (an expansion beyond the pole): read "is Theorem R5.1, and beyond the pole Theorem R6.4 and Proposition R6.7".
"$\mathscr I^+$-weight $\ge\frac52$" (summary, step 11, (GD23)) reads $\max(\frac52,\gamma_++2-\alpha_K)$. "At $\alpha_K
= \frac12$ this is Theorem R2.5" reads "... for b-regular sources". Q5's control applies III.I$''$'s $\beta_\iota =
\gamma_++1$ to $u_{\mathrm{sing}}$, where III.I$''$ uses it for $\partial_{t_*}u_{\mathrm{sing}}$. "$r^3W^*_r \to r_h$"
holds in the static frame; in $(dt_*,dx)$ the $dr$-component is $O(r^{-2})$, and $q = 2$ is unaffected. Q4's `expected`
was unused, and Q1's "iff" was tested at one point (D1 (b) tests the thresholds symbolically). $\beta$ had four meanings
in round 5; round 6 writes $B$ for the coefficient, $\beta(t_*,r)$ for its primitive and $\beta_I,\beta_\iota,\beta_K$
for Lemma 3.1's weights. R5.e (2)'s "reads the same" means with $Z_1$ for $Y$. R5.e (7)'s Q2 computes $-\Delta$'s roots
on Cartesian components; the 1-form reduction is `gdext5.py` E1-E2 and III.D Lemma 4.1. The "exactly when $\alpha_K\ge1$"
argument (lines 2127-2130) uses the window weight, whereas III.I$'''$ Step 3.1 inverts $\hat f(0)$ at $\alpha+2 =
\gamma_+-1$, as Theorem R6.4 does.

*Round 5's own items.* R5.d item 1 (Theorem R5.1 at $\alpha_K\ge1$) is Theorem R6.4. Item 2 (sharpness) is Proposition
R6.9, in the form stated there. Item 3 (III.I$'$ at $\Box$) is Lemma R6.10 and Propositions R6.11-R6.12. Corollary R5.4
is superseded by Corollary R6.6, and (A34)'s $t_*^{-1+\epsilon}$ reads $t_*^{-2+\epsilon}$.

### R6.h What is not proved; findings, labels, files and replacement texts

*Not proved, and not claimed anywhere downstream.*
1. *The leading coefficient at $t_*^{-2}$* for compactly supported gauge data, $\frac{Q}{8\pi^2}t_*^{-2}d\psi$
   (Proposition R6.7, formal). It needs $K^+$-weights above 2, past II.G$'$'s integer exclusion and the zero-energy
   window. The proved statement is $t_*^{-2+\epsilon}$ for every $\epsilon>0$ (Corollary R6.6).
2. *Whether a given perturbation's gauge source attains $t_*^{-1/2-\delta_\sharp}$.* That is the value of one coefficient
   (Proposition R6.9). The rate of Corollary R5.3 holds for every perturbation in the class and is sharp for its source
   class.
3. *The expansion of $Z_1$ at $\mathscr I^+$ on the initial slab beyond the order $p$ of Theorem R4.3*, which would need
   IV$''$ Theorem 2.4 Steps 4-6 at $\Box$. It is not used.
4. *A second reading* of round 6, in particular of Theorem R6.4's Steps 3.1-3.3, Corollary R6.6's cut-off and
   Proposition R6.11.

*Findings.* - (GD27) III.I$'''$ Proposition 2.1 and Lemmas 1.1-1.3 carry over to $\Box$ at $b_0$ (Theorem R6.4). For
sources of $K^+$-weight $\alpha_K\in(1,2)$ the zero-frequency term $\hat f(0)$ is inverted by the augmented operator at
$\alpha+2 = \gamma_+-1$, and one integration gives $u = c_0\chi_KW^*+O(K^+\text{-weight }\alpha_K-1)$, $c_0$ the total
horizon charge, with the finer form $u'+\beta W^*$ at weight $\alpha_K$ (D1-D3). The cap $\alpha_K<2$ is the zero-energy
window. - (GD28) Modulo the running charge the forward solution decays like $t_*^{-\alpha_K}$, $\alpha_K<2$ (Theorem
R6.5). A gauge vector with $\Box Y = 0$ and data compactly supported on $\Sigma^\circ$ settles to $(Q[Y]/4\pi^2)W^*$ at
$t_*^{-2+\epsilon}$ (Corollary R6.6, D4), by a cut-off with compact support in spacetime. Round 5's "radiation cap
$t_*^{-3/2}$" was a cap of the slab and cone route. - (GD29) The first non-smooth term of $\Box$'s resolvent at zero
energy on Tangherlini is $\sigma\log\sigma$, coefficient $-\frac i{8\pi^2}d\psi\otimes\ell$ (Proposition R6.7, formal;
D5-D6). Its time-domain counterpart is $\frac{c_\infty}2t_*^{-2}d\psi$, so $t_*^{-2+\epsilon}$ is the formal exponent up
to $\epsilon$; there is no $t_*^{-1}$ tail (proved). This settles the round-4 verifier's m1. - (GD30) The $l = 0$ part of
the harmonic-gauge source is $\Box$ of a radial 1-form (Lemma R6.8). An explicit source of that form and of
$\iota^+$-order $\frac52+\delta_\sharp$ has the solution $\chi'v^{-1/2-\delta_\sharp}d\psi$, metric part
$\mu_0v^{-1/2-\delta_\sharp}\mathcal L_{W^*}g$ (Proposition R6.9, D7). Corollary R5.3's $\kappa<\delta_\sharp$ is sharp
for its source class. - (GD31) III.I$'$ at $\Box$: at $\mathscr I^+$, $\rho_I^{-1}\rho_+^{-2}\Box =
2(X_+-X_I)(X_I-\frac32)+\rho_I\mathrm{Diff}^2 _{\mathrm b}$ on Cartesian components; the index set is
$\{(\frac32+j,0)\}$, a radiation field in every component, no logarithm, and formal solutions are obstructed only at
source order $\frac52$ (Lemma R6.10, Propositions R6.11-R6.12, D13). The gauge vector of Corollary R6.6 has this
expansion to every order (Corollary R6.13). - (GD32) The verifiers of rounds 4 and 5 found no mathematical error and no
major one; their findings are seated as (A37)-(A56), with corrected checks D1-D3 and D8-D12.

*Labels.* Computed: `checks/gdrad5.py` D1-D13 (exact, sympy; D2 and D8 on the whole parameter box, D12 at 60 exact
rational samples, D3 at four rationals and the integer; D5-D6 compute a formal expansion), each with a control that
mutates the computed path and fails. Deduced: Lemmas R6.1-R6.3, Theorems R6.4-R6.5, Corollary R6.6, Lemma R6.8,
Proposition R6.9, Lemma R6.10 (with D13), Propositions R6.11-R6.12, Corollary R6.13, and (A37)-(A56). Formal: Proposition
R6.7 (b)-(d). READ: the file:line citations above. Standard: b-Sobolev embedding, Lemma R2.6. Everything is at $b_0$,
where (Dyn) is Part VI.A Theorem 6.1. Corollaries R4.4 and R6.6 use Part IX (verified) as (A37) states.

*Files.* `GAUGEDECAY5.md` (this section appended); `checks/gdrad5.py` with `checks/gdrad5.out`.

*Replacement texts.* Each is old (quoted from the file as it now stands) and new. Those for this file are readings, per
the amendments; those for `N1STAR-PROOF.md` and the paper are for the main session to seat. The clause "with Part IX
(verified)" is the one to drop if Part IX is promoted to proved ((A37)).

(1) *This file, Proposition R2.13 (b)* (lines 820-823). Old:

```text
(b) *Decaying gauge data.* If $Z'_0$ has compactly supported Cauchy data, then on each $\{r_0<r\le R'\}$, with the
derivatives of (R2.2),
$$(\dot g_H)_0 = \dot\mu K^*+c\,\mathcal L_{W^*}g+O(t_*^{-1/2}),\qquad c = Q[Z'_0]/4\pi^2.$$
When $\dot\mu\ne0$ this grows linearly in $v$ and is not (stationary, smooth at $r_h$) $+\,o(1)$.
```

New:

> (b) *Decaying gauge data.* If $Z'_0$ has Cauchy data compactly supported on $\Sigma^\circ$, then on each
> $\{r_0<r\le R'\}$, with every number of derivatives and for every $\epsilon>0$,
> $$(\dot g_H)_0 = \dot\mu K^*+c\,\mathcal L_{W^*}g+O(t_*^{-2+\epsilon}),\qquad c = Q[Z'_0]/4\pi^2$$
> (Corollaries R4.6 and R6.6). When $\dot\mu\ne0$ this grows linearly in $v$ and is not (stationary, smooth at $r_h$)
> $+\,o(1)$.

and in its proof (line 836) "(b): Corollary R2.8 for $Z'_0$" reads "(b): Corollary R6.6 for $Z'_0$".

(2) *This file, Theorem R3.4 (iii)-(iv)* (lines 1205-1212). Old:

```text
(iii) On each $\{r_0<r\le R',\ t_*\ge T'\}$, with the derivatives of (R2.2),
$$\big|\dot g_H-\dot\mu K^*-c_\infty\mathcal L_{W^*}g\big|\le Ct_*^{-1/2},\qquad c_\infty = \frac1{4\pi^2}\int\ell\big(
\chi'J_h+[\Box,\chi']Y\big)\,dv,$$
$\chi'$ of (A8): a horizon charge, as in R2.12 (iii).

(iv) For $Y_h$ on $N^+$ with $\Box Y_h = 0$ and compactly supported Cauchy data on $\Sigma^\circ$, $\dot g_H+\mathcal
L_{Y_h}g$ has (ii), induces $(\dot\gamma,\dot k)$ up to the data of $\mathcal L_{Y_h}g$, and has (iii) with
$c_\infty+Q[Y_h]/4\pi^2$.
```

New:

> (iii) On each $\{r_0<r\le R',\ t_*\ge T'\}$, with every number of derivatives and for every
> $\kappa\in(0,\delta_\sharp)$, $\delta_\sharp = (1-e_\Upsilon)\gamma_\Upsilon$,
> $$\big|\dot g_H-\dot\mu K^*-c_\infty\mathcal L_{W^*}g\big|\le C_\kappa\,t_*^{-1/2-\kappa},\qquad c_\infty =
> \frac1{4\pi^2}\int\ell\big(\chi'J_h+[\Box,\chi']Y\big)\,dv,$$
> $\chi'$ of (A8): the limit of a horizon charge (Corollary R5.3). The exponent is sharp for the source class used
> (Proposition R6.9).
>
> (iv) For $Y_h$ on $N^+$ with $\Box Y_h = 0$ and Cauchy data compactly supported on $\Sigma^\circ$, $\dot g_H+\mathcal
> L_{Y_h}g$ has (ii), induces $(\dot\gamma,\dot k)$ up to the data of $\mathcal L_{Y_h}g$, and has (iii) with
> $c_\infty+Q[Y_h]/4\pi^2$, as $Y_h-(Q[Y_h]/4\pi^2)W^* = O(t_*^{-2+\epsilon})$ for every $\epsilon>0$ (Corollaries R4.6
> and R6.6).

(3) *This file, Corollary R4.4* (lines 1540-1544). Old:

```text
\dot g_H) = 0$, $\Theta(\dot g_H) = 0$ on all of $N^+$, $\dot g_H$ induces $(\dot\gamma,\dot k)$ exactly, and on each
$\{r_0<r\le R',\ t_*\ge T'\}$, with the derivatives of (R2.2) as amended by (A12),
$$\big|\dot g_H-\dot\mu K^*-c_\infty\mathcal L_{W^*}g\big|\le Ct_*^{-1/2},\qquad c_\infty = \frac1{4\pi^2}\int\ell\big(
\chi'J_h+[\Box,\chi']Z_1\big)\,dv,$$
a horizon charge; for $Y_h$ with $\Box Y_h = 0$ and compactly supported data on $\Sigma^\circ$, $\dot g_H+\mathcal
L_{Y_h}g$ has the same properties with $c_\infty+Q[Y_h]/4\pi^2$, the data changed by those of $\mathcal L_{Y_h}g$.
```

New:

> \dot g_H) = 0$, $\Theta(\dot g_H) = 0$ on all of $N^+$, $\dot g_H$ induces $(\dot\gamma,\dot k)$ exactly, $\dot g_H =
> \dot g$ on a neighbourhood of $\Sigma^\circ$ ((A42)), and on each $\{r_0<r\le R',\ t_*\ge T'\}$, with every number of
> derivatives and for every $\kappa\in(0,\delta_\sharp)$,
> $$\big|\dot g_H-\dot\mu K^*-c_\infty\mathcal L_{W^*}g\big|\le C_\kappa\,t_*^{-1/2-\kappa},\qquad c_\infty =
> \frac1{4\pi^2}\int\ell\big(\chi'J_h+[\Box,\chi']Z_1\big)\,dv,$$
> the limit of a horizon charge (Corollary R5.3, sharp for its source class by Proposition R6.9); for $Y_h$ with $\Box
> Y_h = 0$ and data compactly supported on $\Sigma^\circ$, $\dot g_H+\mathcal L_{Y_h}g$ has the same properties with
> $c_\infty+Q[Y_h]/4\pi^2$, the data changed by those of $\mathcal L_{Y_h}g$, and $Y_h-(Q[Y_h]/4\pi^2)W^* =
> O(t_*^{-2+\epsilon})$ (Corollary R6.6).

(4) *`N1STAR-PROOF.md`, 10.2 (iv)* (lines 1800-1803 as the file now stands; 1795-1798 when the verifier read
it), from "When" to "as in four dimensions.". Old:

```text
When
Z has compactly supported data it settles to mu-dot K* + c pi_{W*} on each {r <= R} at the rate t_*^-1/2, c the
conserved horizon charge of Z divided by that of W* (deduced, GAUGEDECAY5 Proposition R2.13 (b), with (Dyn), which Part
VI.A Theorem 6.1 proves at b_0; `checks/admbox5.py` B1-B8); the mass change grows linearly in v, as in four dimensions.
```

New:

> When Z has data compactly supported on the initial surface Sigma it settles to mu-dot K* + c pi_{W*} on each
> {r <= R} at the rate t_*^(-2+eps) for every eps > 0, c the conserved horizon charge of Z divided by that of W*
> (deduced, GAUGEDECAY5 Proposition R2.13 (b) with Corollaries R4.6 and R6.6, from Part VIII and the write-out's proved
> parts, with Part IX (verified); `checks/admbox5.py` B1-B8, `checks/gdkplus5.py` Q1-Q6, `checks/gdrad5.py` D1-D13);
> the mass change grows linearly in v, as in four dimensions.

(5) *`N1STAR-PROOF.md`, 10.8* (lines 2945-2947 now; 2940-2942 when read), from "For W' with compactly supported
data" to "proves at b_0);".
Old:

```text
For W' with compactly supported data
GAUGEDECAY5 Proposition R2.13 (b) gives the rate t_*^-1/2 on each {r <= R} (deduced, with (Dyn), which Part VI.A Theorem
6.1 proves at b_0);
```

New:

> For W' with data compactly supported on the initial surface Sigma, GAUGEDECAY5 Proposition R2.13 (b) with
> Corollaries R4.6 and R6.6 gives the rate t_*^(-2+eps), every eps > 0, on each {r <= R} (deduced, from Part VIII and
> the write-out's proved parts, with Part IX (verified); `checks/gdrad5.py`);

(6) *The paper, section 8.2* (`paper/RESPONSE-HL-5D.md`:805-811), from "In harmonic gauge the spherically symmetric
part of a" to "does not decay at infinity;". Old:

```text
In harmonic gauge the spherically symmetric part of a
perturbation is μ̇K* + π_Z, μ̇ the change of mass and Z a 1-form with □Z = 0; when Z has compactly supported data it
settles on each region r ≤ R to μ̇K* + c π_{W*}, growing linearly in v, at the rate τ^(−1/2) (deduced from the
zero-energy structure of the 1-form wave operator, supplement GAUGEDECAY5 R2.13, `docket68/n1star/checks/admbox5.py`,
with the horizon and trapping hypotheses the supplement's Part VI verifies at Tangherlini); without decay of Z's data
the growth can be traded for a stationary term that does not decay at infinity;
```

New (it supersedes round 4's and round 5's proposals, (A36) and (A55)):

> In harmonic gauge every perturbation in the class has a representative constructed on the whole domain: it is in
> harmonic gauge there, induces the given data and equals the solution above near the initial surface. Its
> spherically symmetric part is μ̇K* + π_Z, μ̇ the change of mass and Z a 1-form with □Z = 0. On each region r ≤ R the
> representative settles to μ̇K* + c π_{W*}, growing linearly in v, with c the limit of a horizon charge, at the rate
> τ^(−1/2−κ) for every κ < δ♯ = (1 − e_Υ)γ_Υ. δ♯ is the margin by which the constraint damping makes the gauge source
> decay along the forward cone, and the exponent is sharp for the sources the estimate uses: a source of the same form
> attains τ^(−1/2−δ♯) exactly. A gauge change by a 1-form Y with □Y = 0 and data compactly supported on the initial
> surface moves only c, by Y's horizon charge over W*'s, and Y itself settles to that multiple of W* at the rate
> τ^(−2+ε) for every ε > 0 (deduced from Part VIII and the supplement's proved parts, with Part IX (verified):
> supplement GAUGEDECAY5 R4.4, R5.3, R6.6, R6.9; `docket68/n1star/checks/gdscri5.py`, `checks/gdext5.py`,
> `checks/gdkplus5.py`, `checks/gdrad5.py`). Without decay of Z's data the growth can be traded for a stationary term
> that does not decay at infinity;

(7) *The paper, section 9, the "Settling" item* (`paper/RESPONSE-HL-5D.md`:1396-1398). Old:

```text
The decay of X is not proved, so the routes in a Regge–Wheeler-type
  gauge and in the harmonic gauge (Hung's sections 5–8 in five dimensions), which argue decay in those gauges, remain
  deductions.
```

New (it supersedes round 4's proposal and R5.e (6)):

> The gauge vector X is determined in a Regge–Wheeler-type gauge and constructed in the harmonic gauge, where it is
> unique only up to solutions of □Y = 0 (supplement GAUGEDECAY5). In the Regge–Wheeler-type gauge it is explicit, and
> the perturbation settles to the change of mass on each region r ≤ R, the horizon included, at Part VIII's rate,
> O(τ^(−2−ε)) for some ε > 0, with two derivatives lost (GAUGEDECAY5 Theorem 1.5). In the harmonic gauge a
> representative exists on the whole domain, induces the given data and settles to μ̇K* + c π_{W*} at τ^(−1/2−κ) for
> every κ < δ♯, an exponent sharp for the sources used (GAUGEDECAY5 R4.4, R5.3, R6.9). Both are deduced from Part VIII
> and the supplement's proved parts, with Part IX (verified). Hung's route in five dimensions (his sections 5–8) is
> needed for neither and remains a deduction.

(8) *The paper's list of checks*, after the entry for `checks/gdkplus5.py` (R5.e (7)), or after `checks/admbox5.py` if
that entry is not yet seated:

> - `checks/gdrad5.py` D1–D13: section 8.2's rates in harmonic gauge past the first zero-frequency term (supplement
>   GAUGEDECAY5 round 6). D1, the column and the cut-off state near zero energy (homogeneity, the Fubini counts, the
>   tf-order with its weight computed); D2, every weight condition of the carried-over steps on the whole parameter box;
>   D3, the transform (1 + t)^(−α) ↔ ∫B + Γ(1 − α) w^(α−1) for α in (1, 2), and its failure at α = 2; D4, the
>   exponent, τ^(−2+ε) for compactly supported gauge data; D5–D6, the low-frequency expansion on Tangherlini (formal):
>   no logarithm at order σ, −(1/2) log r at order σ², first non-smooth term σ log σ, a multiple of dψ; D7, a gauge
>   source of the harmonic-gauge form attaining τ^(−1/2−δ♯) exactly; D8–D12, corrected checks for the earlier rounds;
>   D13, the 1-form wave operator at null infinity. Each with a control that must fail. Exact; about a minute.

## Round 7 (2026-11-06)

*Status.* Written 2026-11-06 (round 7, this section). Not verified by a second reader. Rounds 1-6 are left as they
stand; every change to them is a numbered amendment, (A57)-(A70) in section R7.0: the coordinator's two items and the
findings of round 6's verifier, each re-derived before it is accepted. New program: `checks/gdtail5.py` (T1-T11) with
`checks/gdtail5.out` (EXIT 0, eleven checks, eleven controls failing; about four minutes). Every check has a control
that mutates the computed path and must fail, and fails. Labels as in rounds 1-6, with the corpus's status words, as
round 6's verifier asks: a statement argued here from proved parts is *deduced*, and *proved* is kept for a part that a
reading has promoted. Readings use round 6's abbreviations (I2, I3, I4, G2, F2, D, H, H$'$, K) and IX for
`PART-IX-GAUGE.md`, all under `proof5/`. Section headings are lettered (R7.0, R7.a-R7.e).

*The result, in one paragraph.*
- **The $t_*^{-2}$ term, deduced** (Theorem R7.3, Corollary R7.4). For $Y$ with $\Box Y = 0$ and Cauchy data compactly
  supported on $\Sigma^\circ$, on each $\{r_0<r\le R'\}$ with every derivative,
  $Y-cW^* = \frac c2t_*^{-2}\,d\psi+O(t_*^{-3+\epsilon})$, $c = Q[Y]/4\pi^2$, $d\psi = \mu_0W^*-(\partial_v)^\flat$; in
  the metric $\mathcal L_Yg-c\mathcal L_{W^*}g = \frac{\mu_0c}2t_*^{-2}\mathcal L_{W^*}g+O(t_*^{-3+\epsilon})$.
  Proposition R6.7 (d) is now deduced, for the class it holds in. Two steps. Theorem R7.1 carries Theorem R6.4 past
  its window, to $\alpha_K\in(2,3)$, for sources of zero total charge: the zero-frequency term is inverted without the
  column, so the cap $\gamma_+<2$ is gone. Lemma R7.2 builds one explicit solution of charge $4\pi^2$ whose $t_*^{-2}$
  term can be read off: the switched-on Coulomb field of flat $4+1$, placed on Tangherlini's outgoing Kerr-Schild form.
  The coefficient is computed two ways, from the low-frequency chain (formal) and from the time-domain model, and they
  agree (T1-T2). The hypothesis that the source decays faster than $r^{-3}$ at $\mathscr I^+$ cannot be dropped: the
  verifier's example (Major 4) has charge $4\pi^2$, a source of order exactly 3 there, and no $t_*^{-2}$ term.
- **The spherically symmetric part, decided** (Proposition R7.5, Corollaries R7.6-R7.7). The $l = 0$ part of Corollary
  R4.4's representative is exactly $\dot\mu K^*+\mathcal L_{Z'_0}g$ with $\Box Z'_0 = 0$ and $Z'_0 = Y_0-\dot\mu
  W^{**}_H$ near $\Sigma^\circ$, $Y_0$ the $l = 0$ gauge vector of Part VIII's solution. The coefficient that R6.9 named
  as deciding cancels identically, as round 6's verifier also found (Major 1). $Z'_0$ settles at $t_*^{-p+\epsilon}$,
  $p$ the order of its data at spatial infinity. In the class $p>\frac12+2\gamma_\Upsilon$, so the spherically
  symmetric part of no perturbation in the class reaches the cap $t_*^{-1/2-\delta_\sharp}$. For the data of the
  paper's settling statement, a change of mass beyond a ball, $p = 1$ exactly (T8), which gives $t_*^{-1+\epsilon}$;
  for compactly supported data the exact $t_*^{-2}$ term of Theorem R7.3.
- **The part with $l\ge2$.** Corollary R5.3's $t_*^{-1/2-\kappa}$, $\kappa<\delta_\sharp$, stands for it. R6.9's
  sharpness, reworded as the verifier asks, concerns the source class and not this part. One input is missing, (M): the
  low-energy hypotheses of I.C on the $l\ge2$ subspace at non-positive weights. With it this part settles at
  $t_*^{-3/2-\kappa}$, and the representative for the paper's data at $t_*^{-1+\epsilon}$. Proposition R7.8 shows that
  no argument of the kind used here does better without it.
- **The slab order suffices** (section R7.c, T10). No statement of the paper uses $Z_1$ at $\mathscr I^+$ on the
  initial slab beyond the order $p>\frac12+\beta$ of Theorem R4.3.
- **Verifiers and replacement texts** (sections R7.0, R7.e). The replacement texts replace R6.h's. They give the
  paper's sections 8.2 and 9, supplement 10.2 (iv) and 10.8, and entries for the paper's list of checks, its
  claims-to-checks table, its run list and its md5 table, for the five programs the texts cite.

### R7.0 Amendments: the coordinator's items and round 6's verifier

*The coordinator's items* (relayed during round 7).

(A57) *Part IX is proved* (READ, Part IX's status line: "Proved (D617): a full line-by-line re-read found no major gap;
its minor findings m1, m2 and nits n1-n8 are seated (finding (IX6))"). Read every "Part IX (verified)" and "with Part IX
(verified)" in this file as "Part IX (proved)": round 1's labels (line 391-392), Theorem 1.5 (d) (line 166), (A37)
(lines 2665-2670), R6.h's labels (line 2823) and texts (4)-(7). The texts of R7.e drop the clause; the round-6
verifier's Major 2 is the same item.

(A58) *Part IX's line numbers, again stale.* R3.1 (lines 988-995) cites IX:131-134, 209-216, 231-234 and 350-351, and
(A24) re-mapped them; Part IX moved again at D617. Read them by name: IX:131-134 is Lemma 1.2 (the domain); IX:209-216
is Theorem 2.2's comparison on future halves $\Omega'_+$, tensors smooth up to $\Sigma_U$; IX:231-234 is Theorem 2.2's
Step 1, the extension of $\Theta(k)$ across $\Sigma_U$ by Seeley's theorem and a cut-off; IX:350-351 is finding
(IX5), the withdrawal of $N^\circ$ and $N^{\mathcal D}$ (a text citing them reads $U^\sharp$, $\Omega^\sharp$, $N^+$).
Every other IX:line citation in rounds 3-6 is read as the statement it names beside it (Lemma 1.1, Lemma 1.2,
Theorem 2.2 and its Steps, Corollary 2.3, Remark 2.4 (c), the findings). This round cites Part IX by name only.

*The round-6 verifier's findings* (relayed during round 7; its scratch scripts are its own and nothing here depends on
them). Its verdicts: Lemmas R6.1-R6.3, Theorems R6.4-R6.5, Lemma R6.8 and Lemma R6.10 to Corollary R6.13 hold;
Corollary R6.6 holds with two gaps, (A60); R6.7 (a) is computed and (b)-(d) formal, correctly labelled, but (d) is
overgeneral, (A61); R6.9's computations hold and its sharpness claim is overstated, (A59). Its independent
recomputations agree with round 6's: the $\sigma\log\sigma$ coefficient $-\frac{i\ell(f)}{8\pi^2}d\psi$, the tail
$\frac{c_\infty}2t^{-2}d\psi$, and $u_2$'s $\log r$ coefficients $-\frac12$ in $dv$ and $+\frac12$ in $dr$, the
second of which D5 did not check and T2 now does.

(A59) *Major 1, R6.9's sharpness* (lines 2312-2314, 2594-2601, (GD30) 2810, texts (2) 2869, (3) 2895, (6) 2952-2954,
(7) 2976). Re-derived. "And the structure (R6.4) of its $l = 0$ part" adds nothing: every $l = 0$ source is $\Box$ of
its own forward solution, a radial 1-form. Read with Theorem 1.5 (c)'s decay, $J_{h,0} = \Box X_{\mathrm{RW},0}$ with
$X_{\mathrm{RW},0} = O(t_*^{-(w-1)+\epsilon'})$ on compact sets, it is not met by R6.9's example, whose 1-form
$\chi'\phi(v)d\psi$ decays only like $t_*^{-1/2-\delta_\sharp}$ there. Accepted. Read the bold sentence at 2595-2597 as
"Corollary R5.3's rate cannot be improved by any estimate that uses of the gauge source only its $\iota^+$-order
$\frac52+\delta_\sharp$, the only property of it that R5.3 uses". Delete "and the structure (R6.4)" wherever it occurs.
The last sentences, 2598-2601 ("What Proposition R6.9 does not decide ... the theorem holds whatever that value is"),
and R6.h item 2 are wrong for the spherically symmetric part: the coefficient cancels, and the $l = 0$ rate is that of
a homogeneous solution (Proposition R7.5). Status words: R6.9 is deduced. Read "proved" at lines 2307, 2312, 2548,
2556 and 2595 as "deduced" (round 6 was not verified when written; its verifier has now read it).

(A60) *Major 3, Corollary R6.6's proof.* Re-derived. Step (2), lines 2497-2500: $\Omega_* = \mathrm{cl}_M\{t^\flat_*
\ge1\}$ and $C_\flat t_*\le t^\flat_*\le t_*$ (READ, K section 0). A translation by $1-T_a$ puts $\min t_* = 1$ on
$\mathrm{supp}\,F$, where $t^\flat_*$ may be as small as $C_\flat<1$. Translate by $\hat T-T_a$, $\hat T := 2/C_\flat$
(K section 0): then $t_*\ge\hat T$ on the support and $t^\flat_*\ge C_\flat\hat T = 2$. Step (1), lines 2490-2492: that
$Y$ vanishes off $J^+(K)$ is [BGP] Theorem 3.2.11 (the support of the solution lies in $J$ of the supports of the data
and the source), as Part IX section 0 reads it (READ, IX section 0, "Theorem 3.2.11 (p. 85)"), applied on
$\Omega^\sharp$ with compactly supported data on $\Sigma^\circ$. IX Lemmas 1.1-1.2 state no support property. Cite
[BGP] Theorem 3.2.11, IX Lemma 1.1 (uniqueness) and Lemma R3.1. Nothing else in the proof changes.

(A61) *Major 4, R6.7 (c)-(d)* (lines 2539-2544). Re-derived. $u := \chi(t_*)W^*$ is the forward solution of
$[\Box,\chi(t_*)]W^*$. That source is supported in a $t_*$-slab and has $\mathscr I^+$-order exactly 3 (Lemma R2.2,
B1's $r^3L_1W^*\to-1$), so it lies in (R6.1) for $w_I<3$, that is for $\gamma_+<2-\epsilon_1$. Its charge is $4\pi^2$,
and $u = W^*$ at late times on compact sets: no $t_*^{-2}$ term. So (d) is false for "a solution with charge
$4\pi^2c_\infty$". In (c) the source's own $\sigma$-dependence enters, and a column-like tail $r^{-3}G(\sigma r)$ adds
$\sigma\log\sigma$ terms of its own. Accepted. Read (c)-(d) for sources compactly supported in spacetime, the class of
Corollary R6.6's $U$. Theorem R7.3 proves (d) for sources of $\mathscr I^+$-weight above 3, and the example shows
that this bound cannot be lowered to 3 (Remark R7.1').

(A62) *Minor, Theorem R6.4's (2.25a)* (lines 2397-2401, 2419). Take II.G$'$ Proposition 3.3 (1)'s $\epsilon$ as
$\epsilon_{\mathrm{PP}} := \min(\epsilon,\epsilon_1)$. Then $w_I\ge\gamma_++1+\epsilon_{\mathrm{PP}}$, which the
proposition asks, and $\min(w_I,\gamma_++2)-\epsilon_{\mathrm{PP}}\ge\frac52-\epsilon$, which Lemma 4.2's source
space asks. D2 does not encode $w_I$, and its docstring's "every bound asked of $w_I$ shown dominated" and (A50)'s "no
vacuous entry" overclaim. T11 encodes $w_I = \max(\frac52,\gamma_++1+\epsilon_1)$, handles the max and the min
argument by argument, and holds on the whole box. Its control takes $\epsilon_{\mathrm{PP}} = \epsilon$ and fails.

(A63) *Minor, texts (6)-(8).* (6)-(7) put R6.6 and R6.9, unverified, under "the supplement's proved parts", and
(A55)'s "the text says so" was not delivered. R7.e's texts state each status exactly. (8) is incomplete: the paper
also has a claims-to-checks table, a run list and an md5 table, and `gdscri5.py`, `gdext5.py`, `gdkplus5.py` and
`gdrad5.py`, which text (6) cites, are in none of the four. R7.e (5)-(8) give entries for all four and for
`gdtail5.py`.

(A64) *Minor, the round-4 verifier's $-\frac i2\log r$.* Two accounts stand side by side: D5's control "which is the
chain of the round-4 verifier's m1" (lines 2524-2526) and "the chain indexed from the pole" (line 2555). The second
is right: that verifier's $u_1$ is the order-$\sigma$ term of $\sigma\hat P(\sigma)^{-1}$, our $u_2$-level term, and it
reproduces its $-\frac i2\log r$ exactly. Delete the clause at 2525-2526; D5's control stays a control (a state
decaying like $r^{-1}$ has a logarithm at order $\sigma$).

(A65) *Minor, (A48).* "$\alpha-2-\eta>2$" needs $\eta<\epsilon_t$. Read "$\alpha-2-\eta>2+\epsilon_t-\eta>1$", which is
all Corollary R5.3 uses ($\alpha_K<1$).

(A66) *Minor, D12 against E6.* D12's $f_I = \delta_\sharp$ (`gdrad5.py`:585) is the conjugated $\mathscr I^+$-weight
of the source computed from S2's slot exponent $\lambda_\sharp+1$. E6's $\min(\frac{\delta_\sharp}4,0)$
(`gdext5.py`:396-398) uses the statement-level weight $\ell^\flat_I+1$ of III.C$'$ Theorem 3.1, any $\ell^\flat_I\in
(\frac32,\frac32+\delta_\sharp)$ (READ, `PART-III-C2-POLYHOM.md`:31), taken at $\frac32+\frac{\delta_\sharp}4$, and
then clipped at 0. Both are $\ge0>\alpha_I$. Neither binds, and Theorem R4.3 holds with either.

(A67) *Nits.* R6.h (3) cites lines 1540-1544; the text is at 1539-1544. (A37)'s quotations of lines 1359-1361, 1586
and 1837 are paraphrases: read "paraphrased". "$c_0$ the total horizon charge" (lines 2291, 2799) means that charge
divided by $4\pi^2$, $c_0 = (4\pi^2)^{-1}\int\ell(f)$. Lemma R6.3's $\sigma^{2-\epsilon}(2\epsilon)^{-1/2}$ omits the
factor $(2\pi^2)^{1/2}$ of $|S^3|$; the order is unaffected. Lemma R6.3 cites I4:107-117 for its proof, which is at
I4:105-113. Corollary R6.13 takes $\alpha_I = \frac32-3\epsilon$, but Theorem R6.4 (iii) gives $\min(\frac32,1+\gamma_+
-\alpha_K)-3\epsilon$: read that, and choose $\epsilon$ so that $\ell_+ = \gamma_+-2\epsilon$ avoids $\frac32$. Lines
2654-2655 are vacuous, $\chi'Y$ vanishing near $\mathscr I^+$ ($\mathrm{supp}\,\chi'\subset\{r\le t_*/20\}$): delete.

(A68) *`gdrad5.py`* (the verifier reran it byte-identically). Its mutation findings are accepted, and the checks are
relabelled where the claim outran the code. D1 (a) is a homogeneity check: it holds for any operator homogeneous of
degree $-2$, and the order 3 of the column is Lemma R2.2 (b) with B1-B2. D4 restates $\kappa_{\sup}$'s formula; it is
arithmetic, and R6.c's "D4 computes the exponent" reads "D4 records it". D2's $w_I$ is encoded in T11. D5's missing
kernel check ($W^*\in\ker\hat P(0)$) and its radial component are in T2, whose control drops $W^*$'s $dr$ component
and fails. D6's $\kappa_2$ is computed in T2, not hard-coded. What D5-D6 leave unexercised, $w_\sigma$'s first
logarithm at $\sigma^2$ and the matching $\log r\leftrightarrow\log\sigma$, is formal. No deduced statement uses it
now: Theorem R7.3 proves the time-domain coefficient without it. D13's coupling degrees are `gdext5.py` E1's,
computed there from the operator at integer points; read D13's entries as recorded from E1. Corollary R6.6's cut-off
and Proposition R6.11's $\iota^+$ argument are deduced, not computed. The file is left as the verifier read it.

(A69) *R6.h item 1, the $t_*^{-2}$ coefficient,* is Theorem R7.3 and Corollary R7.4 (section R7.a). *Item 2* is
Proposition R7.5 with Corollaries R7.6-R7.7 for the spherically symmetric part, and (M) with Proposition R7.8 for the
rest (section R7.b). *Item 3* is section R7.c.

(A70) *R6.h's replacement texts* (lines 2827-2991) are superseded by R7.e's.

### R7.a The $t_*^{-2}$ term

*Setting.* As in R6.a-R6.b: $M'$, $X^\pm_{\mathrm{sc}\text-\mathrm b}$, $\chi_{\mathrm{zf}}$, $\hat P(\sigma)$, the
augmentation $\tilde P(\sigma)$ of Definition R2.1 with its one column $\hat f_*$, and the weights of II.G$'$ (3.2).
The *total charge* of a source $f$ is $\int\ell(f)\,dv = \ell(\hat f(0))$ ($t_*-v$ is a function of $r$ near $r_h$),
and $c_f(t_*) := (4\pi^2)^{-1}\int^{v_h(t_*)}\ell(f)$ is the running charge of (R2.2).

**Theorem R7.1 (Theorem R6.4 past the window, for sources of zero total charge; at $b_0$; deduced, computed T7).**
Let $\alpha_K\in(2,3)$, $\gamma_+\in(\alpha_K,\min(3,\alpha_K+1))$, $\epsilon_1\in(0,3-\gamma_+)$,
$w_I\ge\gamma_++1+\epsilon_1$ and
$$f\in H^{\infty,(w_I,\gamma_++2,\alpha_K)}_{\mathrm b}(\Omega_*;T^*)^{\bullet,-}\ \text{(plain weights)},\qquad
\int\ell(f)\,dv = 0,\tag{R7.1}$$
and let $u$ be the forward solution of $\Box u = f$. Then for every $\epsilon\in(0,\epsilon_0]$, $\epsilon_0 :=
\frac13\min(\epsilon_1,3-\gamma_+,3-\alpha_K)$:

(i) $u = u'+u_{\mathrm{sing}}$, $u'\in H^{\infty,(\frac32-3\epsilon,\gamma_+,\alpha_K)}_{\mathrm b}(M')$;

(ii) $u_{\mathrm{sing}} = \beta(t_*,r)W^*$ with $\partial_{t_*}\beta(\cdot,r) = (\partial_t\chi_K)(\cdot,r)*B$ and
$\beta(\cdot,r)-\beta(\cdot,r') = (\chi_K(\cdot,r)-\chi_K(\cdot,r'))*B$, $B\in H^{k,\alpha_K}_{\mathrm b}(\mathbb R)$,
$\int B = 0$;

(iii) on $\{r_0<r\le R',\ t_*\ge8\max(R',1)\}$, with every number of derivatives in $x$ and $t_*$,
$|u-c_f(t_*)W^*|\le C\,t_*^{-\alpha_K}\|f\|$.

At each order $k$ the norms are bounded by $C_k$ times the norm of $f$ in (R7.1) at an order $k+\ell$; $u'$,
$u_{\mathrm{sing}}$ and $B$ depend on $k$ through $c = c_k$, $u$ does not ((A52)).

*Proof: Theorem R6.4's steps, and what changes.* References are to I4 and I3 unless said otherwise.
- *Steps 0-2* as in R6.4. III.I$''$ Lemma 4.1 at $(w_I,\gamma_++2,\alpha_K)$, $\alpha_K\in(2,3)\setminus\mathbb N$,
  gives $u_{\mathrm{hi}}\in H^{\infty,(\frac32-\epsilon,N,N)}_{\mathrm b}$. (2.25a), II.G$'$ Proposition 3.3 (1) at
  $\beta_K = \alpha_K$ with $\epsilon_{\mathrm{PP}} = \min(\epsilon,\epsilon_1)$ ((A62)), gives
  $\hat f|_{\pm(0,c]}\in H^{\infty,(\frac52-\epsilon,\gamma_++1,((0,0),(1,0),\alpha_K-1))}_{\mathrm b}$. Its two Taylor
  coefficients are $\hat f(0) = \int f\,dt_*\in H^{\infty,\gamma_++1}_{\mathrm b}(X)$ and $\hat f_1 := i\int t_*f\,dt_*
  \in H^{\infty,\gamma_+}_{\mathrm b}(X)$ (the order-1 coefficient lies in $\langle x\rangle H^{\infty,\gamma_++1}
  _{\mathrm b}$, G2:349-354), each the same for both signs. The density step is R6.4's.
- *Step 3.1$'$, zero energy at order 0, without the column.* Put $\beta_{\mathrm{tf}} := \gamma_+-1\in(1,2)$. At the
  b-weight $\beta_{\mathrm{tf}}$, inside the interval $(0,2)$ on which (G) holds (III.D$'$ section 1, READ: "(G) for
  every $\alpha$ with $\alpha+2\in(0,2)$"), $\hat P(0):\mathcal X_0\to\mathcal Y_0$ has kernel $\mathrm{span}\{W^*\}$
  and range $\ker\ell$ (III.D$'$ Lemma 2.1 (2)-(3); "kernels, annihilators of ranges and invertibility do not depend on
  these choices", III.D$'$ section 1, by I.C Theorem 3.1 (3)-(4)). $\hat f(0)\in\mathcal Y_0$, its $\mu_{\mathrm
  b}$-weight being $\beta_{\mathrm{tf}}+2$. As $\ell(\hat f(0)) = 0$, there is a unique $\hat u_0\in H^{\infty,
  \beta_{\mathrm{tf}}}_{\mathrm b}(X)$ with $\hat P(0)\hat u_0 = \hat f(0)$ and $\langle\hat u_0,\varphi\rangle_h = 0$.
  The column is not used. It could not be: $\hat f_*(0)\in\mathcal A^3$ is not in $\mathcal Y_0$ at the weight
  $\beta_{\mathrm{tf}}+2>3$, and a nonzero charge needs it (T7's control). This is R6.4's cap $\gamma_+<2$, and here it
  is not met.
- *Step 3.1$''$, order 1.* Put $g_1 := \hat f_1+iL_1\hat u_0\in H^{\infty,\beta_{\mathrm{tf}}+1}_{\mathrm b}(X)$
  ($L_1\in\rho\,\mathrm{Diff}^1_{\mathrm b}$). Proposition R2.3 at the weight $\alpha+2 := \beta_{\mathrm{tf}}-1 =
  \gamma_+-2\in(0,1)$, where $\mathcal Y_0$ has $\mu_{\mathrm b}$-weight $\gamma_+<3$ and so contains the column, gives
  $(\hat u_1,b_1) := \tilde P(0)^{-1}(g_1,0)$, $\hat u_1\in H^{\infty,\beta_{\mathrm{tf}}-1}_{\mathrm b}(X)$,
  $\langle\hat u_1,\varphi\rangle_h = 0$, $b_1 = \ell(g_1)/4\pi^2$.
- *The remainder.* With $\hat P(\sigma) = \hat P(0)-i\sigma L_1-\sigma^2L_2$ (R2.1), for $0<|\sigma|\le c$,
  $\tilde P(\sigma)\big(\chi_{\mathrm{zf}}(\hat u_0+\sigma\hat u_1),\sigma b_1\big) =
  (\hat f(\sigma)-\hat f_2(\sigma),0)$,
  $$\hat f_2 := \big(\hat f-\chi_{\mathrm{zf}}(\hat f(0)+\sigma\hat f_1)\big)-[\hat P(0),\chi_{\mathrm{zf}}]
  (\hat u_0+\sigma\hat u_1)+i\sigma[L_1,\chi_{\mathrm{zf}}]\hat u_0+\sigma^2L_2\chi_{\mathrm{zf}}\hat u_0
  +i\sigma^2L_1\chi_{\mathrm{zf}}\hat u_1+\sigma^3L_2\chi_{\mathrm{zf}}\hat u_1
  -\sigma b_1\big(\hat f_*(\sigma)-\chi_{\mathrm{zf}}\hat f_*(0)\big).$$
  The row vanishes, $\langle\hat u_0,\varphi\rangle = \langle\hat u_1,\varphi\rangle = 0$. The terms lie, in order,
  in $H^{\infty,(\frac52-\epsilon,\gamma_++1,\alpha_K-1)}$ (Step 2), $H^{\infty,(\infty,\gamma_++1,\infty)}$ (Lemma R6.1
  (b), $p = 2$, at $a = \beta_{\mathrm{tf}}$ and, with $\sigma$ of tf-order 1 on $\mathrm{supp}\,d\chi_{\mathrm{zf}}$,
  at $a = \beta_{\mathrm{tf}}-1$), the same (Lemma R6.1 (b), $p = 1$, and one $\sigma$), $H^{\infty,(\infty,
  \beta_{\mathrm{tf}}+4,\gamma_{\mathrm{zf}})}$ (Lemma R6.1 (a), $p = j = 2$), $H^{\infty,(\infty,\beta_{\mathrm{tf}}+2,
  \gamma_{\mathrm{zf}})}$ (Lemma R6.1 (a) at $a = \beta_{\mathrm{tf}}-1$, $p = 1$, $j = 2$, with Lemma R6.1 (b) for the
  commutator), $H^{\infty,(\infty,\beta_{\mathrm{tf}}+4,\gamma_{\mathrm{zf}})}$, every $\gamma_{\mathrm{zf}}<2$, and
  $H^{\infty,(N,4-\epsilon,2-\epsilon)}$ (Lemma R6.2 (b) and one $\sigma$, $|\sigma| = \rho_{\mathrm{tf}}
  \rho_{\mathrm{zf}}$). As $\alpha_K-1<2-\epsilon$ and $\beta_{\mathrm{tf}}+2 = \gamma_++1\le4-\epsilon$ (T7),
  $\hat f_2|_{\pm(0,c]}\in H^{\infty,(\frac52-\epsilon,\gamma_++1,\alpha_K-1)}_{\mathrm b}$.
- *Step 3.2.* III.I$''$ Lemma 4.2 (I3:244-269), whose $\beta_{\mathrm{zf}}$ is free and enters by division by
  $|\sigma|^{\beta_{\mathrm{zf}}}$, at $\beta_{\mathrm{scf}} := \frac32-\epsilon$, $\beta_{\mathrm{tf}}$,
  $\beta_{\mathrm{zf}} := \alpha_K-1$ and the window $\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}} =
  \gamma_+-\alpha_K\in(0,1)$ (Theorem R2.4 there), gives $(\hat u',\hat b') := \tilde P(\sigma)^{-1}(\hat f_2,0)$ with
  $\hat u'\in H^{\infty,(\frac32-2\epsilon,\beta_{\mathrm{tf}},\alpha_K-1)}_{\mathrm b}$, $\hat b'\in
  H^{\infty,\alpha_K-1}_{\mathrm b}(\pm(0,c],|\frac{d\sigma}\sigma|)$. So $\hat u_{\mathrm{reg},1} =
  \chi_{\mathrm{zf}}(\hat u_0+\sigma\hat u_1)+\hat u'$ and $\hat b_1 = \sigma b_1+\hat b'$. (2.26a), II.G$'$
  Proposition 3.5 (1) at $\beta_K = \alpha_K$, applies with the two Taylor terms: their coefficients $\hat u_0$ and
  $\hat u_1$ are the same for both signs, and $v_0 = \hat u_0$, $v_1 = \langle x\rangle^{-1}\hat u_1$ lie in
  $H^{\infty,\gamma_+-1}_{\mathrm b}(X)$, the tf-weight $\beta_\iota-1$ it asks. It gives $u_{\mathrm{reg}}\in
  H^{\infty,(\frac32-3\epsilon,\gamma_+,\alpha_K)}_{\mathrm b}(M')$. With Step 2 this is
  (i).
- *Step 3.4, the coefficient $B$.* $B := \mathcal F^{-1}(\chi\hat b_1)$. The pair $(\chi\hat b_1|_{\sigma<0},
  \chi\hat b_1|_{\sigma>0})$ lies in II.G$'$ Definition 2.7's $X^{k,\alpha_K-1}$ with the polynomial part $b_1\sigma$,
  of degree $1<\alpha_K-1$, the same for both signs. II.G$'$ Proposition 2.8 (2) at $\beta = \alpha_K\in(2,3)\setminus
  \mathbb N$ gives $B\in H^{k,\alpha_K}_{\mathrm b}(\mathbb R)$, and $\int B = (\chi\hat b_1)(0) = 0$. The identities of
  (ii) are R2.5 (ii)'s, proved there from $\mathcal F(\partial_{t_*}u_{\mathrm{sing}}) = \chi\Psi\hat b_1W^*$ without a
  weight.
- *(iii)* is Theorem R6.5's proof with (i)-(ii): $|B(t)|\le C\langle t\rangle^{-\alpha_K}\|f\|$ by Lemma R2.6, the
  convolutions sample $B$ on $[\frac{t_*}2,t_*]$, $u' = O(t_*^{-\alpha_K})$ with its b-derivatives by b-Sobolev
  embedding near $K^+$, so $|Q[u']|\le Ct_*^{-\alpha_K}\|f\|$ and $4\pi^2\beta(t_*,r_h) = 4\pi^2c_f+O(t_*^{-\alpha_K})$.
  No integration with a moment condition is needed (III.I$''$ Lemma 3.1, whose $\beta_K$ must lie in $(-1,1)$, is not
  used), and no $K^+$-statement for $u_{\mathrm{sing}}$ itself is claimed. $\square$

*What changes against R6.4, and where this one stops.* R6.4's cap $\gamma_+<2$ is the column at order 0. With zero
charge the column enters only at order 1, at the weight $\gamma_+<3$. The caps here are $\gamma_+<3$ ($\hat u_0\in
H^{\infty,<2}_{\mathrm b}$, as $\hat u_0\sim r^{-2}$, and the column at order 1) and $\alpha_K<3$ (the order-2 Taylor
term). The bookkeeping is T7: each condition is a positive sum on the whole box, the model's orders included.

*Remark R7.1$'$ (the $\mathscr I^+$-weight cannot be lowered to 3; deduced).* (R7.1) asks $w_I\ge\gamma_++1+\epsilon_1
>3$. This bound is needed. $\chi(t_*)W^*-u_{\mathrm{ex}}$, with $u_{\mathrm{ex}}$ of Lemma R7.2, is the forward solution
of $[\Box,\chi(t_*)]W^*-f_{\mathrm{ex}}$. That source has zero total charge (both terms have $4\pi^2$) and
$\mathscr I^+$-order 3 ((A61)). At late times on compact sets the solution is $-\frac12t_*^{-2}d\psi+O(t_*^{-3})$, which
is not $O(t_*^{-\alpha_K})$ for any $\alpha_K>2$. The weight enters through II.G$'$ Proposition 3.3 (1)'s condition
$\beta_I\ge\beta_\iota-\min(\beta_K,1-\epsilon)$.

**Lemma R7.2 (an explicit solution of charge $4\pi^2$; deduced, computed T1, T3-T6).** Put, for $w>0$, $r>0$,
$$K(w,r) := r^{-2}\Big(\frac{w+r}{\sqrt{w(w+2r)}}-1\Big),\qquad K(w,r) := 0\ \ (w<0),$$
so that $a(t,r) := r^{-2}H(t)+K(t-r,r) = \frac t{r^2\sqrt{t^2-r^2}}H(t-r)$ is, in flat $4+1$, the field of the charge
$4\pi^2\delta_0$ switched on at $t = 0$: $a = 4\pi^2\int_0^tE_4\,d\tau$, with $E_4 = -(4\pi^2)^{-1}(t^2-r^2)^{-3/2}$
inside the cone, $a\to r^{-2} = 4\pi^2G_4$ (T1). Let $R_T\ge3R_1$, let $h\in C^\infty([r_0,\infty))$ with $h(r) = -2r$
for $r\le R_T$ and $h(r) = -2r_*(r)$ for $r\ge2R_T$ (III.B section 4's $r_*$), and put $T := v+h(r)$. So $T = x^1 =
t-|x|$, the outgoing null coordinate, near infinity (III.B (4.1)), and $T = v-2r$ near compact sets. $t_*-T$ is a
bounded function of $r$ (near infinity $t_* = x^1+C'-8\mu_0|x|^{-1}$, III.B (3.6)). Fix $\chi_1\in C^\infty(\mathbb
R)$, equal to 0 on $(-\infty,T_1]$ and to 1 on $[T_1+1,\infty)$, with $T_1$ so large that $\{T\ge
T_1\}\subset\{t^\flat_*\ge\hat T\}$. Put
$$A(T,r) := \int\chi_1'(s)K(T-s,r)\,ds,\qquad u_{\mathrm{ex}} := \chi_1(T)W^*+A(T,r)\,d\psi,\qquad f_{\mathrm{ex}} :=
\Box u_{\mathrm{ex}}.$$
Then:

(a) $u_{\mathrm{ex}}$ is smooth on $\{r\ge r_0\}$, $G$-invariant ($l = 0$), and vanishes on $\{T<T_1\}$. At $\mu_0 = 0$
it is $(\chi_1'*a)\,dt$, the flat field of the charge switched on along $\chi_1$.

(b) $f_{\mathrm{ex}}$ has $\mathscr I^+$-order 4, $\iota^+$-order 6 and $K^+$-order 3, with b-regularity. So it lies in
(R7.1) for every $\alpha_K<3$, $\gamma_+<3$ and $w_I<4$, and in (R6.1) for every $\alpha_K<2$.

(c) $Q[u_{\mathrm{ex}}](v) = 4\pi^2\chi_1(T)-4\pi^2r_h^3\,\partial_rA$ at $r_h$ (T5), so $Q[u_{\mathrm{ex}}] =
4\pi^2+O(t_*^{-3})$ at late times, and the total charge of $f_{\mathrm{ex}}$ is $4\pi^2$, by (2.1).

(d) On compact $r$-sets at late times, with every derivative, $u_{\mathrm{ex}}-W^* = A\,d\psi = \frac12t_*^{-2}
d\psi+O(t_*^{-3})$.

*Proof.* (a) $K(\cdot,r)$ is smooth on $w>0$, with the integrable singularity $r^{-3/2}(2w)^{-1/2}$ at $w = 0^+$ (T6),
so $\chi_1'*K(\cdot,r)$ is smooth in $(T,r)$ for $r>0$. $T$, $W^*$ and $d\psi$ are smooth on $\{r\ge r_0\}$, $r_0>0$.
At $\mu_0 = 0$, $W^* = r^{-2}dt$ and $d\psi = dt$, and $\chi_1(T)r^{-2}+A = \chi_1'*(H r^{-2}+K) = \chi_1'*a$. (b) $T-v$
depends on $r$ alone and $\partial_v$ is Killing, so $\Box$ commutes with the convolution in $v$ at fixed $(r,\omega)$.
*Near infinity*, in the outgoing chart $(T,r)$, $g = -f\,dT^2-2\,dT\,dr+r^2\slashed g$ (III.B Lemma 4.1), with $W^* =
r^{-2}dT+\frac{dr}{r(r-r_h)}$ and $d\psi = dT+(1+\frac{\mu_0}{r(r-r_h)})dr$, both solutions of $\Box$ (T3). For arbitrary
$\chi(T)$ and $A(T,r)$, $E := \Box(\chi W^*+A\,d\psi)$ is reduced with the flat equation of $a := \chi r^{-2}+A$. $a =
\chi_1'*(Hr^{-2}+K)$ solves it on $r>0$, the flat solution's source $4\pi^2\chi_1\delta_0$ sitting at $r = 0$. The
reduced $E$ vanishes at $\mu_0 = 0$. It is a sum of explicit coefficients times $\chi'$, $\partial_TA$,
$\partial_rA$, $\partial_r^2A$; $\chi$ and $A$ undifferentiated do not occur (T3). $A = -\chi_1(T)r^{-2}+r^{-3/2}
F_{3/2}(T)+r^{-5/2}F_{5/2}(T)+\dots$ at $\mathscr I^+$ (T6, the expansion of $K$ in $w/r$, whose coefficients
$w^{-1/2},w^{1/2},\dots$ are locally integrable, so the convolution keeps it), with $\partial_r$ adding one order. So
every term of $E$ has $\mathscr I^+$-order at least 4, the least being the slab term $\chi_1'r_hr^{-4}$ (T3). At late
times, $\chi = 1$, and $E[\chi_1'*K] = \chi_1'*E[K]$ with $E[K]$ of $\iota^+$-order 6 along $T = \lambda r$ and
$\mathscr I^+$-order $\frac92$ at fixed $T$ (T3). $K$ is homogeneous of degree $-2$ (T6), so these are joint orders at
the corner. *Near compact sets*, $\chi_1(T) = 1$ at late times, and $\Box(A\,d\psi) = (\Box_0A)\,d\psi-2\nabla_{\mathrm
{grad}A}d\psi$ for every $A(v,r)$, with every term carrying a derivative of $A$ (T4). $K(w,r) = \frac12w^{-2}-rw^{-3}+
O(w^{-4})$ and $\partial_rK = -w^{-3}+O(w^{-4})$ uniformly on compact $r$-sets (T6), so $\partial_vA$, $\partial_rA =
O(T^{-3})$ there, with $(T\partial_T)^j$: $K^+$-order 3. Membership in (R7.1), (R6.1) is S4's criterion (pointwise
order above each weight) with T7's inequalities. (c) T5: $Q[\phi\,d\psi] = -4\pi^2r_h^3\partial_r\phi(v,r_h)$ for
every $\phi(v,r)$, $Q[\chi_1(T)W^*] = 4\pi^2(\chi_1-r_h\partial_r\chi_1(T))$ at $r_h$ (B4), and $\partial_r$ of
$\chi_1(T)$, $A$ at $r_h$ is $O(T^{-3})$ late ($\chi_1' = 0$ there). By (2.1), $\int\ell(f_{\mathrm{ex}}) =
\lim_vQ[u_{\mathrm{ex}}] = 4\pi^2$. (d) $\int\chi_1' = 1$, $K = \frac12w^{-2}+O(w^{-3})$ uniformly in $r$ on compact
sets, and $T-t_*$ is bounded there. $\square$

The coefficient $\frac12$ is that of the fundamental solution inside the cone, $4\pi^2\int_t^\infty(4\pi^2)^{-1}
\tau^{-3}d\tau = \frac12t^{-2}$ (T1). The low-frequency chain gives the same number formally: $\kappa_2 = -\frac12$, D6's
formula and $\mathcal F[t^{-2}H(t-1)] = E_2(-i\sigma) = 1+(-i\sigma)\log(-i\sigma)+\dots$ give $\frac c2t^{-2}d\psi$
(T2). The control of T1 is $3+1$, where the switched-on field is $H(t-r)/r$ and the coefficient is 0 (Huygens).

**Theorem R7.3 (the $t_*^{-2}$ term; deduced from Theorem R7.1 and Lemma R7.2).** Let $f$ satisfy (R7.1) without the
condition $\int\ell(f) = 0$, with $\gamma_+<3$ and $w_I<4$ (lowering weights is free), $c_0 := (4\pi^2)^{-1}
\int\ell(f)\,dv$, and $u$ its forward solution. Then on each $\{r_0<r\le R',\ t_*\ge T'\}$, with every number of
derivatives in $x$ and $t_*$,
$$u-c_f(t_*)W^* = \frac{c_0}2\,t_*^{-2}\,d\psi+O(t_*^{-\alpha_K}),\qquad d\psi = \mu_0W^*-(\partial_v)^\flat.
\tag{R7.2}$$
*Proof.* $g := f-c_0f_{\mathrm{ex}}$ lies in (R7.1) (Lemma R7.2 (b)) and has zero total charge (Lemma R7.2 (c)).
$u-c_0u_{\mathrm{ex}}$ is its forward solution: it is smooth, vanishes for $t^\flat_*<\hat T$, and solves the equation
(II.E Proposition 3.4). Theorem R7.1 (iii) gives $u-c_0u_{\mathrm{ex}}-c_g(t_*)W^* = O(t_*^{-\alpha_K})$. By (2.1),
$4\pi^2c_g = Q[u]-c_0Q[u_{\mathrm{ex}}] = 4\pi^2c_f-c_0Q[u_{\mathrm{ex}}]$ at late times, and $Q[u_{\mathrm{ex}}] =
4\pi^2+O(t_*^{-3})$. So $u = c_fW^*+c_0(u_{\mathrm{ex}}-W^*)+O(t_*^{-\alpha_K})$, and Lemma R7.2 (d) gives (R7.2), as
$\alpha_K<3$. $\square$

**Corollary R7.4 (gauge vectors with compactly supported data; deduced).** Let $Y$ be a smooth 1-form on $N^+$ with
$\Box Y = 0$ whose Cauchy data on $\Sigma^\circ$ have compact support, and $c := Q[Y]/4\pi^2$. For every $\epsilon>0$,
on each $\{r_0<r\le R',\ t_*\ge T'\}$ and with every number of derivatives,
$$Y-cW^* = \frac c2\,t_*^{-2}\,d\psi+O(t_*^{-3+\epsilon}),\qquad\mathcal L_Yg-c\,\mathcal L_{W^*}g =
\frac{\mu_0c}2\,t_*^{-2}\,\mathcal L_{W^*}g+O(t_*^{-3+\epsilon}).\tag{R7.3}$$
The second term is not $o(t_*^{-2})$ when $c\ne0$: $\mathcal L_{W^*}g\ne0$ ($(\mathcal L_{W^*}g)_{vr} =
-\frac7{24}r_h^{-3}$ at $r = 2r_h$, D7).

*Proof.* Corollary R6.6's cut-off, with (A60)'s translation, gives $U = Y$ on compact sets at late times and a source
smooth and compactly supported in spacetime, in (R7.1) for every $\alpha_K<3$, $\gamma_+<3$, $w_I$. Its charge is
constant once the cut-off vanishes near the horizon, $c_f = Q[U]/4\pi^2 = c$. Theorem R7.3 with $\alpha_K := 3-\epsilon$
gives the first identity. For the second, $\mathcal L_{\phi\,d\psi}g = \phi\,\mathcal L_{d\psi}g+2\,d\phi\otimes_s
d\psi$ and $\mathcal L_{d\psi}g = \mu_0\mathcal L_{W^*}g$, $(\partial_v)^\flat$ being Killing (D7). With $\phi =
\frac c2t_*^{-2}$, $d\phi = O(t_*^{-3})$. $\square$

So Proposition R6.7 (d) holds as stated there for $Y$ of Corollary R6.6, now deduced, not formal; (b)-(c) remain
formal statements about the resolvent, and no deduced statement rests on them. Corollary R6.6's $t_*^{-2+\epsilon}$ is
superseded by (R7.3), and with it Corollary R4.6's late-time clause, Proposition R2.13 (b) and the $Y_h$-clauses of
Theorems R2.12 (iv), R3.4 (iv) and Corollary R4.4: $Y_h-(Q[Y_h]/4\pi^2)W^* = \frac{Q[Y_h]}{8\pi^2}t_*^{-2}d\psi+
O(t_*^{-3+\epsilon})$.

### R7.b The rate of the harmonic-gauge representative

**Proposition R7.5 (the spherically symmetric part is homogeneous; deduced from Theorem 1.5 (a), Corollary R4.4,
(A42), H1, Proposition 2.1 (d)).** Let $\dot g_H = \dot g+\mathcal L_Zg$ be Corollary R4.4's representative, $Z =
\dot\mu\chi_KW^{**}_H+Z_1$, and $Y_0 := Y[h_0]^\flat = -X_{\mathrm{RW},0}$ (Theorem 1.5 (a)-(c), $h_0 = (\dot
g-\dot\mu K)_0$). Put $Z'_0 := Z_0+Y_0-\dot\mu W^{**}_H$. Then on $N^+$
$$(\dot g_H)_0 = \dot\mu K^*+\mathcal L_{Z'_0}g,\qquad\Box Z'_0 = 0,\qquad Z'_0 = Y_0-\dot\mu W^{**}_H\ \text{near }
\Sigma^\circ.\tag{R7.4}$$
For $\dot g_H+\mathcal L_{Y_h}g$ (R4.4's last clause) read $Z'_0+Y_{h,0}$.

*Proof.* $\dot g_0 = \dot\mu K+h_0 = \dot\mu K+\mathcal L_{Y_0}g$ (Theorem 1.5 (a), read on $N^+$ by (A2)), and the
$SO(4)$-average commutes with $\Theta$ and $\mathcal L_\cdot g$. So $(\dot g_H)_0 = \dot\mu K+\mathcal L_{Y_0+Z_0}g =
\dot\mu K^*+\mathcal L_{Z'_0}g$, $K^* = K+\mathcal L_{W^{**}_H}g$. $\Theta(\dot g_H) = 0$ on $N^+$ (Corollary R4.4), and
$\Theta(\mathcal L_Xg) = \Box X$ (H1), $\Theta(K^*) = 0$ (Proposition 2.1 (d)): so $\Box Z'_0 = \Theta((\dot g_H)_0)-
\dot\mu\Theta(K^*) = 0$. Near $\Sigma^\circ$, $\chi_K = 0$ and $Z_1 = 0$ ((A42)), so $Z = 0$ there. $\square$

So the $\lambda_\sharp$-term of $X_{\mathrm{RW},0}$ on the cone, which Lemma R6.8 puts into $J_{h,0}$, never reaches
$(\dot g_H)_0$. $Z_1$'s $l = 0$ part is $-Y_0+\dot\mu(1-\chi_K)W^{**}_H+Z'_0$; the slow piece $-Y_0$ cancels against
$\dot g$'s own $\mathcal L_{Y_0}g$, and on compact sets it is $O(t_*^{-(w-1)+\epsilon'})$ anyway (Theorem 1.5 (c)). The
$l = 0$ rate is the rate of $Z'_0$, a homogeneous solution whose Cauchy data on $\Sigma^\circ$ are those of
$Y_0-\dot\mu W^{**}_H$, fixed by the spherically symmetric part of the initial data. This is the round-6 verifier's
reduction (Major 1), here from Corollary R4.4 directly. It is round 1's Proposition 2.1 (c) for this representative.

*Data of order $p$.* A 1-form $Y$ on $N^+$ has *data of order $p$ at spatial infinity* if, near infinity on
$\Sigma_{\mathrm{IVP}}$, its Cartesian components and those of $\nabla_\nu Y$ are conormal of orders $p$ and $p+1$ in
$|x|^{-1}$, up to a constant multiple of the Killing form $(\partial_t)^\flat$. Data compactly supported up to that
multiple have every order.

**Corollary R7.6 (homogeneous solutions with data of order $p$; deduced from Proposition R4.2, Corollary R4.6's proof
and Theorems R5.1, R5.2, R6.4, R6.5; computed T9).** Let $\Box Y = 0$ on $N^+$, with data of order $p\in(\frac12,
\frac32)$. Then $Q[Y]$ is constant at late times and, for every $\alpha_K<p$, $\alpha_K\ne1$, on each $\{r_0<r\le R',\
t_*\ge T'\}$ with every number of derivatives, $|Y-c'(\partial_t)^\flat-(Q[Y]-4\pi^2\mu_0c')/(4\pi^2)\,W^*|\le
C\,t_*^{-\alpha_K}$, $c'$ the Killing multiple of the data. The metric part settles: $|\mathcal L_Yg-c\,\mathcal L_{W^*}
g|\le Ct_*^{-\alpha_K}$, $c := (Q[Y]-4\pi^2\mu_0c')/4\pi^2$.

*Proof.* Subtract $c'(\partial_t)^\flat$, a global solution with $Q = 4\pi^2\mu_0c'$ (H3). Let $\tau' := t_{\mathrm{IVP}}
/|x|$ (Theorem R4.3 (2)), $\chi_d\in C^\infty_c((-\frac1{16},\frac1{16}))$ equal to 1 near 0, and $\Upsilon :=
\chi_d(\tau')(y_0+t_{\mathrm{IVP}}y_1)$ near infinity, $(y_0,y_1)$ the data ($y_1$ the $t_{\mathrm{IVP}}$-derivative),
extended to a smooth 1-form with $Y$'s data on $\Sigma^\circ$. $\tau'$ is a b-time function at $I_0$ for every weight
(Lemma R4.1 (d)). So $\Box\Upsilon$ is conormal of $I_0$-order $p+2$, and supported in $\{|\tau'|\le\frac1{16}\}$ near
infinity, away from $\mathscr I^+$.
(1) *The slab.* $Y-\Upsilon$ has zero data and the source $-\Box\Upsilon$, whose conjugate $\rho_I\rho^{-7/2}
\Box\Upsilon$ lies in $H^{\infty,(a_0,2\alpha_I)}_{\mathrm b}$ for every $a_0<p-\frac32$ and every $\alpha_I$ (Theorem
R4.3 (3)'s shifts). Proposition R4.2 with $\alpha_I<\min(a_0,0)$ and b-Sobolev embedding, as in Theorem R4.3 (4), give
$Y$ the $\mathscr I^+$-order $p_{\mathrm{slab}} := \alpha_I+\frac32$, any number below $p$, on $N^+\cap\{2\le t^\flat_*
\le3\}$. (2) *Forward solution.* For $\beta\in(0,p_{\mathrm{slab}}-\frac12)$, $\chi(t^\flat_*)Y$ is the forward
solution of the slab commutator, of $\mathscr I^+$-order $p_{\mathrm{slab}}+1>\beta+\frac32$, which is in II.F$'$ (1.4)
(S7, T1 of `gdr3fix5.py`, (A29)). II.F$'$ (1.7) gives $\chi(t^\flat_*)Y\in H^{k,(b_I,b_+,-\frac12)}_{\mathrm b}$ for
$\frac12<b_+<b_I<p_{\mathrm{slab}}$. (3) *The cone.* $\chi'Y$ is the forward solution of $[\Box,\chi']Y\in H^{\infty,
(N,b_++2,N)}_{\mathrm b}$ (S6), which lies in (R5.1) for $\gamma_+<b_+$, $\alpha_K\in[\frac12,\gamma_+)$, $\alpha_K<1$,
and in (R6.1) for $\gamma_+\in(\alpha_K,\min(2,b_+))$, $\alpha_K\in(1,2)$. Theorems R5.2 and R6.5 give $|\chi'Y-c_f(t_*)
W^*|\le Ct_*^{-\alpha_K}$. At late times $d\chi' = 0$ near the horizon, so $c_f = Q[Y]/4\pi^2$, constant by (2.1). The
chain $\alpha_K<\gamma_+<b_+<b_I<p_{\mathrm{slab}}<p$ reaches every $\alpha_K<p$ (T9, on the whole box). The metric
part: $\mathcal L_{(\partial_t)^\flat}g = 0$. $\square$

At $p = \frac12$ the chain is empty (T9's control); for $p\ge\frac32$ the route stops at $t_*^{-3/2}$, the cone
source's a priori weight $b_+<\frac32$ (R6.c). For data with compact support Corollary R7.4 is better.

**Corollary R7.7 (the spherically symmetric rate; deduced, computed T8-T9).** Let $\dot g_H$ be Corollary R4.4's
representative for data $(\dot\gamma,\dot k)$ in Part VIII's class.

(a) $Z'_0$ of (R7.4) has data of order $p_0\ge\min(1,q-1)$, $q := \min(\min\mathrm{Re}\,\mathcal E_0,\ell_0,2)$, so
$p_0>\frac12+2\gamma_\Upsilon>\frac12+\delta_\sharp$. Hence $(\dot g_H)_0-\dot\mu K^*-c\,\mathcal L_{W^*}g =
O(t_*^{-\alpha_K})$ on compact sets for every $\alpha_K<\min(p_0,\frac32)$, $\alpha_K\ne1$: the spherically symmetric
part of no perturbation in the class reaches the cap $t_*^{-1/2-\delta_\sharp}$.

(b) If, outside a ball, $(\dot\gamma,\dot k)$ are $\dot\mu$ times the data of $K$, as for the data of the paper's
settling statement (glued to exact Tangherlini data beyond a ball, section 8.7 of the paper), then $Z'_0 = \dot\mu
Z^{(K)}+Z_c+c''(\partial_t)^\flat$. Here $Z_c$ is homogeneous with compactly supported data, and $Z^{(K)}$ is one
homogeneous solution, independent of the perturbation, with data of order exactly 1 (T8). So $(\dot g_H)_0-\dot\mu
K^*-c\,\mathcal L_{W^*}g = O(t_*^{-1+\epsilon})$ for every $\epsilon>0$. If $\dot\mu = 0$ (data with compact support:
the linearised mass of compactly supported data vanishes), then $(\dot g_H)_0-c\,\mathcal L_{W^*}g = \frac{\mu_0c}2
t_*^{-2}\mathcal L_{W^*}g+O(t_*^{-3+\epsilon})$ (Corollary R7.4).

*Proof.* (a) Near $\Sigma^\circ$, $Z'_0 = Y_0-\dot\mu W^{**}_H$. $Y_0 = (\zeta\partial_v+rH\partial_r)^\flat$ with
$d\zeta = \omega$ algebraic in $h_0$ and $dH$ (Lemma 1.4 (b)). $h_0$'s data are of order $q$, $\dot h$'s being in
$H^{\infty,(\mathcal E_0,\ell_0)}_{\mathrm b}$ (Part VIII Lemma 1.1) and $K$'s of order 2. So along $\Sigma^\circ$,
$\zeta-\zeta_\infty$ and $rH$ are of order $q-1$, and $\nabla Y_0$ of order $q$: $Y_0$ has data of order $q-1$ up to
$\zeta_\infty(\partial_v)^\flat$. $W^{**}_H$'s data are of order 1 (T8: value $O(r^{-1})$, $\partial_tW^{**}_H =
\frac12W^* = O(r^{-2})$). $q>\frac32+2\gamma_\Upsilon$ (K:54-57) and $\gamma_\Upsilon<\frac14$, $\delta_\sharp =
(1-e_\Upsilon)\gamma_\Upsilon$ (T9). Corollary R7.6 and (R7.4). (b) Lemma 1.1's construction is local, so
$(\dot h-\dot\mu K)$'s data are $\dot\mu(\dot h^{(K)}-K)$'s plus compactly supported ones, $\dot h^{(K)}$ the initial
solution for the data of $K$. $\mathcal L_{Y_K}g := \dot h^{(K)}-K$ induces zero data on $\Sigma_{\mathrm{IVP}}$ (Lemma
1.1 (1)), so $Y_K|_\Sigma$ is a Killing initial data set, a multiple of $\partial_t$ in the class (the paper's section
8.7, READ: "the G-invariant ones are ∂_t's alone"). And $\nabla_\nu Y_K$ is fixed by $(\mathcal L_{Y_K}g)(\nu,\cdot) =
-K(\nu,\cdot)$, as $\dot h^{(K)}(\nu,\cdot) = 0$ (Lemma 1.1). $Z^{(K)}$ is the homogeneous solution with the data of
$Y_K-W^{**}_H$. Near infinity, on $\Sigma_{\mathrm{IVP}} = \{t = C''\}$ (III.B Lemma 3.9's proof), $K = |x|^{-2}(dt-
d|x|)^2$, of order 2 in its normal components, and $W^{**}_H = -\frac{dt}{|x|}+\frac{d|x|}{4|x|}+O(|x|^{-2}\log|x|)$
(T8). The $|x|^{-1}$ term is not removed by $(\partial_t)^\flat$ (order 0) or $W^*$ (order 2): the order is exactly
1. Corollary R7.6 at $p = 1$ for $Z^{(K)}$, Corollary R7.4 for $Z_c$. For $\dot\mu = 0$: $\delta\mu$ of Lemma 1.4 is
constant (Theorem 1.5 (a)) and vanishes near $\Sigma^\circ$ outside the support, so $\dot\mu = \delta\mu[\dot g_0] =
0$. $\square$

*The part with $l\ge2$.* $(\dot g_H)_{\ge2} = h_{\ge2}+\mathcal L_{Z_{1,\ge2}}g$, $h_{\ge2} = O(t_*^{-w+\epsilon'})$ on
compact sets, and $Z_{1,\ge2}$ is the forward solution with zero data of $F_{Y,\ge2}$. Corollary R5.3 bounds it by
$t_*^{-1/2-\kappa}$, $\kappa<\delta_\sharp$. The bound comes from two places: the cone source's $\iota^+$-order, which
Part VIII's $\lambda_\sharp$-term sets at $\frac52+\delta_\sharp$ in every $l$ ((H1): $\mathcal E_+\ni(\lambda_\sharp,
0)$, and the write-out states no vanishing of its $l\ge2$ projection); and the window $\gamma_+-\alpha_K\in(0,1)$. On
the $l\ge2$ subspace there is no zero-energy state and no column, and the window's lower end $0$ is the $l = 0$ root.
What is missing is the low-energy theory there:

(M) *For $\hat P(\sigma)$ restricted to the closed subspace of class 1-forms with no $l = 0$ part (bounded on every
space used, the $SO(4)$-projections commuting with $\hat P(\sigma)$ and acting boundedly, Proposition 2.5 (iv)), I.C's
hypotheses (G) and (TF) hold at every b-weight $\alpha+2\in(-1,0]$. Then III.H Theorem 4.1 (3) and III.I$''$ Lemma 4.2
hold there without augmentation.*

At infinity $\hat P(0)$ is $-\Delta$ on Cartesian components up to $\rho^2$-relative terms (Lemma R4.1 (a)). On the
$l\ge2$ class 1-forms the Cartesian components carry harmonics of degree $m\ge1$, with the roots $r^{-q}$, $q\in\{-m,
m+2\}$ (round 4's G2). So the root-free interval about $(0,2)$ is $(-1,3)$ there, which is why (M) is expected. It is
not proved: I.C's proofs are written for the full bundle, and their transposition to an isotypic subspace, with (TF)
at the transition face, is not carried out.

**Proposition R7.8 ((M) is what is missing; deduced).** (a) Under (M), Theorems R5.1 and R6.4 hold on the $l\ge2$
subspace with the window $\gamma_+-\alpha_K\in(-1,1)$ and $u_{\mathrm{sing}} = 0$. So $(\dot g_H)_{\ge2} =
O(t_*^{-\alpha_K})$ on compact sets for every $\alpha_K<\frac32+\delta_\sharp$, and for the data of Corollary R7.7 (b)
the representative settles at $t_*^{-1+\epsilon}$. (b) Without (M), no estimate of the kind of Theorems R5.1, R6.4 and
R7.1 gives $(\dot g_H)_{\ge2}$ a rate $t_*^{-\alpha_K}$ with $\alpha_K\ge\gamma_+$, the source being of
$\iota^+$-order $\gamma_++2<\frac52+\delta_\sharp$. Nothing weaker than (M) suffices for that part, short of a property
of Part VIII's solution (the vanishing of the $l\ge2$ projection of its $\lambda_\sharp$-term) that the write-out does
not state.

*Proof.* (a) Every step of R5.1 and R6.4 carries over on the subspace with the column removed. At zero energy Step 3.1
needs $\hat P(0)$ invertible at $\beta_{\mathrm{tf}} = \gamma_+-1\in(-1,0)$, and Step 3.2 needs Lemma 4.2 at the window
$\gamma_+-\alpha_K\in(-1,0)$: both are (M). There is no $W^*$, so no singular part. With $\gamma_+<b_+<\frac12+
\delta_\sharp$ (R5.3's proof) this gives $\alpha_K<\gamma_++1<\frac32+\delta_\sharp$, and $\alpha_K<2$; the $l\ge2$ part
of $F_Y$ on the cone and the commutator $[\Box,\chi']Y$ are $l\ge2$ sources of the class used. With Corollary R7.7 (b)
this is $t_*^{-1+\epsilon}$. (b) In III.I$''$ Lemma 4.2 the weights obey $\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}} =
\alpha+2$, with $\beta_{\mathrm{tf}} = \gamma_+-1$ fixed by the source's $\iota^+$-weight $\gamma_++2$ ((2.25a)) and
$\beta_{\mathrm{zf}} = \alpha_K-1$ the output's $K^+$-weight ((2.26a)). So $\alpha_K\ge\gamma_+$ is $\alpha+2\le0$.
On the full bundle the uniform estimate fails at every $\alpha+2\le0$. $(\partial_v)^\flat$, stationary, smooth at the
horizon and $O(1)$ at infinity (B5), lies in $\mathcal X_0$ at every negative weight, with $\hat P(0)(\partial_v)^\flat
= 0$. So $\hat P(0)$ has the two-dimensional kernel $\mathrm{span}\{W^*,(\partial_v)^\flat\}$ there, and one column
cannot make $\tilde P(0)$ injective: III.H Theorem 4.1's hypothesis (Z$_{\mathcal P}$) fails. At $\alpha+2 = 0$ the
root 0 is on the weight line and (G) fails. Removing the $l = 0$ part is (M). The source's order: Part VIII's $h'$ has
$\iota^+$-order exactly $\lambda_\sharp$, $(\lambda_\sharp,0)\in\mathcal E_+$ (Proposition R3.2), and $E^\Upsilon G$ adds
one ($|x|^{-1}$). $\square$

### R7.c The expansion of $Z_1$ on the initial slab

Theorem R4.3 gives $Z_1$ the $\mathscr I^+$-order $p$ for every $p\in(\frac12+\beta,\min(\frac32,q_{\dot h}-1))$ on
$N^+\cap\{2\le t^\flat_*\le3\}$, $\beta\in(0,\delta_\sharp)$. No expansion beyond it is carried: IV$''$ Theorem 2.4
Steps 4-6 at $\Box$ would be needed, (A44). Every statement of the paper and of the supplement that uses $Z_1$ near
$\mathscr I^+$ on that slab uses only this order:
- harmonic gauge on all of $N^+$ (Proposition R3.6, Corollary R4.4) asks $p>\frac12+\beta$ for one $\beta\in(0,
  \delta_\sharp)$ (S7);
- the rate $t_*^{-1/2-\kappa}$ (Corollary R5.3) asks it for $\beta = \frac12(\kappa+\delta_\sharp)$, so for every
  $\beta<\delta_\sharp$;
- the $l\ge2$ statement under (M) (Proposition R7.8 (a)) asks the same;
- the spherically symmetric statements (Proposition R7.5, Corollaries R7.6-R7.7) do not use $Z_1$ near $\mathscr I^+$:
  $Z'_0$'s slab estimate comes from its own data through Proposition R4.2, step (1) of Corollary R7.6's proof;
- Corollary R7.4 uses a cut-off with compact support in spacetime and no slab;
- the expansion at $\mathscr I^+$ of Proposition R6.11 and Corollary R6.13 is stated for the gauge vector of Corollary
  R6.6 and for the cone-localised piece, not for $Z_1$ on the slab, and no text of the paper cites it.

Each asked order lies below Theorem R4.3's $\min(\frac32,q_{\dot h}-1)$ on the whole box (T10). The control asks an
expansion of $Z_1$ to order 2 at $\mathscr I^+$ on the slab, which no statement uses, and it lies outside that
interval. So the needed order suffices for every statement, and the expansion beyond it is not an open item of the
paper: no statement depends on it.

### R7.d What is not proved

1. *(M)*, so the rate of the part with $l\ge2$ beyond Corollary R5.3's $t_*^{-1/2-\kappa}$ (Proposition R7.8). This is
   the one missing input of the three items of R6.h. Nothing weaker suffices within the method (Proposition R7.8 (b)).
2. *The resolvent statements* R6.7 (b)-(c), formal. No deduced statement rests on them any longer: the time-domain
   coefficient is Theorem R7.3.
3. *The sharpness of Corollary R7.7 (b)'s $t_*^{-1+\epsilon}$*: whether $Z^{(K)}$ attains $t_*^{-1}$ is not computed
   here. The paper states the proved rate.
4. *A second reading* of round 7, in particular of Theorem R7.1's Steps 3.1$'$-3.2, Lemma R7.2 (b) and Corollaries
   R7.6-R7.7.

### R7.e Findings, labels, files and replacement texts

*Findings.*
- (GD33) Theorem R6.4 carries past its window, to $\alpha_K\in(2,3)$, for sources of zero total charge, the
  zero-frequency term being inverted without the column (Theorem R7.1, T7). The hypothesis $w_I>3$ cannot be dropped
  (Remark R7.1$'$).
- (GD34) The switched-on Coulomb field of flat $4+1$, placed on Tangherlini's outgoing Kerr-Schild form, gives an
  explicit solution of charge $4\pi^2$ with source of orders 4, 6, 3 at $\mathscr I^+$, $\iota^+$, $K^+$ (Lemma R7.2,
  T1, T3-T6). With Theorem R7.1 this gives the $t_*^{-2}$ term: $u-c_fW^* = \frac{c_0}2t_*^{-2}d\psi+
  O(t_*^{-\alpha_K})$ (Theorem R7.3), and for gauge vectors with compactly supported data (R7.3) with error
  $t_*^{-3+\epsilon}$ (Corollary R7.4). The coefficient, from the low-frequency chain (formal), agrees (T2).
- (GD35) The spherically symmetric part of Corollary R4.4's representative is $\dot\mu K^*+\mathcal L_{Z'_0}g$ with
  $Z'_0$ homogeneous (Proposition R7.5). R6.9's deciding coefficient cancels. $Z'_0$ settles at the rate its data's
  order allows (Corollary R7.6): $p_0>\frac12+2\gamma_\Upsilon$ in the class, $p_0 = 1$ for the paper's data
  (Corollary R7.7, T8-T9). The cap $t_*^{-1/2-\delta_\sharp}$ is never reached by that part.
- (GD36) For the part with $l\ge2$ the missing input is (M); with it the representative of the paper's data settles at
  $t_*^{-1+\epsilon}$ (Proposition R7.8).
- (GD37) The slab order of Theorem R4.3 suffices for every statement (section R7.c, T10).
- (GD38) The coordinator's items and the round-6 verifier's findings are seated as (A57)-(A70), with corrected checks
  T2 and T11.

*Labels.* Computed: `checks/gdtail5.py` T1-T11 (exact, sympy; T2's resolvent side recomputes round 6's formal chain;
T7, T9, T10 and T11 on the whole parameter box), each with a control that mutates the computed path and fails.
Deduced: Theorem R7.1, Remark R7.1$'$, Lemma R7.2, Theorem R7.3, Corollary R7.4, Proposition R7.5, Corollaries
R7.6-R7.7, Proposition R7.8 (conditional on (M) in (a)), section R7.c, and (A57)-(A70). Formal: R6.7 (b)-(c) and T2's
resolvent side. READ: the file:line and named citations above. Standard: b-Sobolev embedding, Lemma R2.6. Everything
is at $b_0$, where (Dyn) is Part VI.A Theorem 6.1; Part IX, used through Lemma R3.1 and IX Lemma 1.1, is proved
((A57)).

*Files.* `GAUGEDECAY5.md` (this section appended); `checks/gdtail5.py` with `checks/gdtail5.out`.

*Replacement texts.* Each is old (quoted from the file as it now stands, occurring there exactly once) and new.
Where an old text begins or ends inside a line, the new text's first and last lines are cut so that the seated lines
stay within 121 characters. They supersede R6.h's ((A70)). For `N1STAR-PROOF.md` and the paper they are for the main
session to seat after verification. Statuses are stated as the corpus has them: Part VIII and Part IX proved;
GAUGEDECAY5 deduced, rounds 2-6 read by independent verifiers with their findings seated, round 7 not yet read.

(1) *`N1STAR-PROOF.md`, 10.2 (iv)* (lines 1800-1803 as the file now stands), from "When" to "as in four dimensions.".
Old:

```text
When
Z has compactly supported data it settles to mu-dot K* + c pi_{W*} on each {r <= R} at the rate t_*^-1/2, c the
conserved horizon charge of Z divided by that of W* (deduced, GAUGEDECAY5 Proposition R2.13 (b), with (Dyn), which Part
VI.A Theorem 6.1 proves at b_0; `checks/admbox5.py` B1-B8); the mass change grows linearly in v, as in four dimensions.
```

New:

```text
When
Z has data compactly supported on the initial surface Sigma it settles to mu-dot K* + c pi_{W*} on each {r <= R}, c
the conserved horizon charge of Z divided by that of W*, with an exact leading term: Z - c W* = (c/2) t_*^-2 d psi +
O(t_*^(-3+eps)) for every eps > 0, d psi = mu W* - (d_v)^flat, so that pi_Z - c pi_{W*} = (mu c/2) t_*^-2 pi_{W*} +
O(t_*^(-3+eps)) (deduced, GAUGEDECAY5 Proposition R2.13 (b) with Corollaries R6.6 and R7.4, from Part VIII and the
write-out's proved parts, Part IX among them; `checks/admbox5.py` B1-B8, `checks/gdrad5.py` D1-D13,
`checks/gdtail5.py` T1-T11); the mass change grows linearly in v, as in four dimensions. For the harmonic-gauge
representative of GAUGEDECAY5 Corollary R4.4, Z is the homogeneous 1-form whose data are those of the l = 0 gauge
vector of the initial data less mu-dot W**, and it settles at t_*^(-p+eps), p > 1/2 + 2 gamma_Ups the order of those
data at spatial infinity, p = 1 for data that are a change of mass beyond a ball (GAUGEDECAY5 Proposition R7.5 and
Corollaries R7.6-R7.7, `checks/gdtail5.py` T8-T9).
```

(2) *`N1STAR-PROOF.md`, 10.8* (lines 2945-2947 now), from "For W' with compactly supported data" to "proves at b_0);".
Old:

```text
For W' with compactly supported data
GAUGEDECAY5 Proposition R2.13 (b) gives the rate t_*^-1/2 on each {r <= R} (deduced, with (Dyn), which Part VI.A Theorem
6.1 proves at b_0);
```

New:

```text
For W' with data compactly supported
on the initial surface Sigma, GAUGEDECAY5 Proposition R2.13 (b) with Corollaries R6.6 and R7.4 gives W' - c_1(oo) W*
= (c_1(oo)/2) t_*^-2 d psi + O(t_*^(-3+eps)) on each {r <= R}, every eps > 0, so h_0 - c K* - c_1(oo) pi_{W*} =
(mu c_1(oo)/2) t_*^-2 pi_{W*} + O(t_*^(-3+eps)); for data of order p in (1/2, 3/2) at spatial infinity GAUGEDECAY5
Corollary R7.6 gives the rate t_*^(-p+eps) (deduced, from Part VIII and the write-out's proved parts, Part IX among
them; `checks/gdrad5.py`,
`checks/gdtail5.py`);
```

(3) *The paper, section 8.2* (`paper/RESPONSE-HL-5D.md`:805-811), from "In harmonic gauge the spherically symmetric
part of a" to "does not decay at infinity;". Old:

```text
In harmonic gauge the spherically symmetric part of a
perturbation is μ̇K* + π_Z, μ̇ the change of mass and Z a 1-form with □Z = 0; when Z has compactly supported data it
settles on each region r ≤ R to μ̇K* + c π_{W*}, growing linearly in v, at the rate τ^(−1/2) (deduced from the
zero-energy structure of the 1-form wave operator, supplement GAUGEDECAY5 R2.13, `docket68/n1star/checks/admbox5.py`,
with the horizon and trapping hypotheses the supplement's Part VI verifies at Tangherlini); without decay of Z's data
the growth can be traded for a stationary term that does not decay at infinity;
```

New (it supersedes R6.h (6)):

```text
In harmonic gauge every perturbation in the class has a
representative constructed on the whole domain: it is in harmonic gauge there, induces the given data and equals the
solution above near the initial surface. On each region r ≤ R it settles to μ̇K* + c π_{W*}, growing linearly in v,
with c the limit of a horizon charge, at the rate τ^(−1/2−κ) for every κ < δ♯ = (1 − e_Υ)γ_Υ, the margin by which the
constraint damping makes the gauge source decay along the forward cone; no estimate that uses of that source only this
decay does better. Its spherically symmetric part settles faster. That part is μ̇K* + π_Z exactly, μ̇ the change of
mass and Z a 1-form with □Z = 0 whose data are those of the spherically symmetric gauge vector of the initial data
less μ̇W**, and it settles at τ^(−p+ε) for every ε > 0, p > 1/2 + 2γ_Υ the order of decay of Z's data at spatial
infinity, so faster than τ^(−1/2−δ♯) for every perturbation in the class. For the data of section 8.8, a change of mass
beyond a ball, p = 1 and the rate is τ^(−1+ε); for data with compact support the change of mass vanishes and that part
is c π_{W*} + (μ0 c/2) τ^(−2) π_{W*} + O(τ^(−3+ε)), with exactly that τ^(−2) term. A gauge change by a 1-form Y with
□Y = 0 and data compactly supported on the initial surface moves only c, by Y's horizon charge over W*'s, and on each
region r ≤ R, Y − cW* = (c/2) τ^(−2) dψ + O(τ^(−3+ε)), dψ = μ0 W* − (∂_v)^♭ (deduced from Part VIII and the
supplement's proved parts, Part IX among them: supplement GAUGEDECAY5 R4.4, R5.3, R6.6, R7.1–R7.7, whose rounds 2–6
independent verifiers have read, their findings seated, and whose round 7 is not yet read;
`docket68/n1star/checks/gdscri5.py`, `checks/gdext5.py`, `checks/gdkplus5.py`, `checks/gdrad5.py`,
`checks/gdtail5.py`). Without decay of Z's data the growth can be traded for a stationary term that does not decay
at infinity;
```

(4) *The paper, section 9, the "Settling" item* (`paper/RESPONSE-HL-5D.md`:1396-1398). Old:

```text
The decay of X is not proved, so the routes in a Regge–Wheeler-type
  gauge and in the harmonic gauge (Hung's sections 5–8 in five dimensions), which argue decay in those gauges, remain
  deductions.
```

New (it supersedes R6.h (7)):

```text
The gauge vector X is determined in a Regge–Wheeler-type gauge and
  constructed in the harmonic gauge, where it is unique only up to solutions of □Y = 0 (supplement GAUGEDECAY5). In
  the Regge–Wheeler-type gauge it is explicit, and the perturbation settles to the change of mass on each region
  r ≤ R, the horizon included, at Part VIII's rate, O(τ^(−2−ε)) for some ε > 0, with two derivatives lost
  (GAUGEDECAY5 Theorem 1.5). In the harmonic gauge a representative exists on the whole domain, induces the given
  data and settles to μ̇K* + c π_{W*} at τ^(−1/2−κ) for every κ < δ♯, its spherically symmetric part at τ^(−1+ε) for
  the data of section 8.8 and with an exact τ^(−2) term for data with compact support (GAUGEDECAY5 R4.4, R5.3,
  R7.3–R7.7). Both are deduced from Part VIII and the supplement's proved parts, Part IX among them; GAUGEDECAY5's
  rounds 2–6 have been read by independent verifiers and its round 7 not yet. Hung's route in five dimensions (his
  sections 5–8) is needed for neither and remains
  a deduction.
```

(5) *The paper's list of checks*, after the entry for `checks/admbox5.py` (it supersedes R5.e (7) and R6.h (8)).
Old:

```text
  restrict the gauge data; B7, the source's weighted norm finite iff a > β + 5/2; B8, the gauge's linearisation −Θ(k).
  Each with a control that must fail. Exact; several minutes.
```

New:

```text
  restrict the gauge data; B7, the source's weighted norm finite iff a > β + 5/2; B8, the gauge's linearisation −Θ(k).
  Each with a control that must fail. Exact; several minutes.
- `checks/gdscri5.py` S1–S8: section 8.2's harmonic gauge beyond the forward cone (supplement GAUGEDECAY5 round 3).
  S1, the constraint damping's term E^Υ G does not see the trace-free angular part, the one slot with a radiation
  field; S2, the source's order at null infinity, λ♯ + 1; S3–S4, the weights of the forward-solution theorem, and
  membership by pointwise order; S5, a cut-off on the slab gains one order at null infinity (re-run in the supplement
  with the slab's actual time function); S6, the cone cut-off gains two at timelike infinity; S7, the slab threshold
  p > β + 1/2; S8, the orders of the horizon-regular gauge vector W**. Each with a control that must fail. Exact;
  several minutes.
- `checks/gdext5.py` E1–E6: section 8.2's harmonic gauge down to the initial surface (round 4). E1, in Cartesian
  components the 1-form wave operator is the scalar one plus a coupling of order |x|⁻³; E2, after Part IV's
  conjugation the coupling has no first-order matrix; E3, the indicial roots at null infinity, a radiation field in
  every component; E4, no indicial restriction at spatial infinity; E5, the multiplier's sign condition; E6, the
  weights on the initial slab. Each with a control that must fail (those of E3, E4 and E6 recomputed in
  `checks/gdrad5.py`). Exact; up to half an hour under load.
- `checks/gdkplus5.py` Q1–Q6: section 8.2's rate in harmonic gauge (round 5). Q1, the dictionary between time-weighted
  and b-weighted spaces; Q2, the zero-energy gap (0, 2), the window (0, 1) inside it and the radiation root 3/2;
  Q3–Q5, the cut-off state's order, the time transform t^(−α) ↔ σ^(α−1), the weight conditions (recomputed in
  `checks/gdrad5.py` D1–D3 and `checks/gdtail5.py` T11); Q6, the rate: κ < min(1/2, a − 5/2) for a source of order a at
  timelike infinity, every κ < δ♯ for the gauge source. Each with a control that must fail. Exact; under a minute.
- `checks/gdrad5.py` D1–D13: section 8.2's rates past the first zero-frequency term (round 6). D1, the column's
  homogeneity and the Fubini counts near zero energy; D2, the weight conditions of the carried-over steps on the whole
  box; D3, the transform (1 + t)^(−α) ↔ ∫B + Γ(1 − α) w^(α−1) for α in (1, 2), and its failure at α = 2; D4, the
  exponent's arithmetic; D5–D6, the low-frequency expansion on Tangherlini (formal); D7, the 1-form φ(v) dψ: its
  charge 0 and its source's orders; D8–D12, corrected checks for the earlier rounds; D13, the 1-form wave operator at
  null infinity. Each with a control that must fail. Exact; under a minute.
- `checks/gdtail5.py` T1–T11: section 8.2's τ^(−2) term for compactly supported gauge data and the spherically
  symmetric part's rate (round 7). T1, the switched-on Coulomb field of flat 4+1, t/(r²√(t² − r²)), and its tail
  t^(−2)/2 from the fundamental solution inside the cone; T2, the same coefficient from the low-frequency chain
  (formal); T3–T4, that field placed on Tangherlini: its source vanishes at zero mass by the flat equation and has
  orders 4 at null infinity, 6 at timelike infinity and 3 at late times on compact sets; T5, the horizon charge of
  φ dψ; T6, the kernel's expansions; T7, the conditions of the zero-charge theorem on the whole box; T8, the r⁻¹ tail
  of the spherically symmetric gauge data of a change of mass; T9, the rate for data of order p at spatial infinity;
  T10, the slab order every statement uses; T11, round 6's conditions with the initial-surface weight encoded. Each
  with a control that must fail. Exact; about four minutes.
```

(6) *The paper's claims-to-checks table*, after the row for `checks/admbox5.py`. Old:

```text
| section 8.2: harmonic gauge, l = 0 settling modulo W* | `docket68/n1star/checks/admbox5.py` B1–B8 |
```

New:

```text
| section 8.2: harmonic gauge, l = 0 settling modulo W* | `docket68/n1star/checks/admbox5.py` B1–B8 |
| section 8.2: harmonic gauge beyond the forward cone | `docket68/n1star/checks/gdscri5.py` S1–S8 |
| section 8.2: harmonic gauge down to the initial surface | `docket68/n1star/checks/gdext5.py` E1–E6 |
| section 8.2: harmonic gauge, the rate τ^(−1/2−κ) | `docket68/n1star/checks/gdkplus5.py` Q1–Q6 |
| section 8.2: rates past the first zero-frequency term | `docket68/n1star/checks/gdrad5.py` D1–D13 |
| section 8.2: the τ^(−2) term; the spherically symmetric part's rate | `docket68/n1star/checks/gdtail5.py` T1–T11 |
```

(7) *The paper's run list*, after the line for `checks/admbox5.py`. Old:

```text
    python3 checks/admbox5.py                             # several minutes
```

New:

```text
    python3 checks/admbox5.py                             # several minutes
    python3 checks/gdscri5.py                             # several minutes
    python3 checks/gdext5.py                              # up to half an hour under load
    python3 checks/gdkplus5.py                            # under a minute
    python3 checks/gdrad5.py                              # under a minute
    python3 checks/gdtail5.py                             # about four minutes
```

(8) *The paper's md5 table*, after the row for `checks/admbox5.out`. Old:

```text
| `docket68/n1star/checks/admbox5.out` | `7c7b794f05e9c2536e2dae2d37a3c6eb` |
```

New (md5s measured 2026-11-06 on the files as they stand):

```text
| `docket68/n1star/checks/admbox5.out` | `7c7b794f05e9c2536e2dae2d37a3c6eb` |
| `docket68/n1star/checks/gdscri5.py` | `80beba46f3563ef26e94d3033d8039cb` |
| `docket68/n1star/checks/gdscri5.out` | `4188f6ad77b4d177755df44f90c9d61f` |
| `docket68/n1star/checks/gdext5.py` | `061d3dcfb594b76a3947223ee8b70227` |
| `docket68/n1star/checks/gdext5.out` | `373b5629960a577400213eede77f80c0` |
| `docket68/n1star/checks/gdkplus5.py` | `0ba1a17efc00b486928996b361758d78` |
| `docket68/n1star/checks/gdkplus5.out` | `7ea3fa87d132f1fb147a69ec02a3a467` |
| `docket68/n1star/checks/gdrad5.py` | `75983792199a9fb2f1919a6207f7cf22` |
| `docket68/n1star/checks/gdrad5.out` | `dd8faaed179d1818553da73845cd5dad` |
| `docket68/n1star/checks/gdtail5.py` | `54c224154367e0c869643555426d02aa` |
| `docket68/n1star/checks/gdtail5.out` | `4d9cf42ba7f67657e7dc3055854303ec` |
```
