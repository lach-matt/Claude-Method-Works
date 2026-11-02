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
