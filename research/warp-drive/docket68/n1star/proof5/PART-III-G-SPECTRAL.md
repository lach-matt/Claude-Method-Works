# Part III.G. The spectral family at future timelike infinity at n = 4 ([Hin26] section 9.1, Proposition 9.2)

*Status.* Proved (D240: verifier 99 read the repairs, correct; status synchronised with the README at D325). Written
(D236); verified (D238: one major finding, one minor and four nits of the ninety-eighth verifier seated, the repairs to
be read). This part proves, at spatial dimension $n = 4$, [Hin26] Proposition 9.2 (pp. 164-168): the spectral family
$N_{\mathrm{sf}}(\lambda)$ of the Minkowski model $\bar L$ of the linearised gauge-fixed Einstein operator, on spaces of
distributions on the front face sf supported in $\{v\ge-1\}$, is Fredholm of index 0 for every $\lambda\in\mathbb C$,
invertible for $\mathrm{Re}\,\lambda<2$ (raised from $\frac32$ at D238), invertible for all but finitely many $\lambda$
in every half plane $\{\mathrm{Re}\,\lambda\le C\}$, with a finite-meromorphic inverse; and solutions gain b-regularity
at the light cone $\{v = 0\}$ with their right sides. The rest of the source's section 9 (Proposition 9.4 and after) is
the next part. Parts are cited as before (I.A-I.C, II.A-II.G$'$, III.A-III.F$''''$, README.md); the source is [Hin26] =
P. Hintz, arXiv:2606.28253v2 (printed page numbers). Computations cited as *computed* are exact (sympy) and rerun by
`../sf5.py` S1-S8 (new, D236) and S11 (D238), each with a failing control.

*What n = 4 changes.* The radiative constant is $c = \frac32$ (his 1), so the operator is
$-2\partial_v(v\partial_v+\lambda-\frac32-\bar S)+\tilde L(0)(v\partial_v+\lambda)$, the regularity threshold at the
light cone is $s<2-\mathrm{Re}\,\lambda$ (his $\frac32-\mathrm{Re}\,\lambda$), and the operator is invertible for
$\mathrm{Re}\,\lambda<2$ (his $1+\epsilon_{\mathrm{ind}}$): at $n = 4$ the indicial gap of $\tilde L(0)$ contains
$(0,1]$ (III.F$'$ Proposition 2.3 (a)) and tf-admissibility holds for every weight in $(0,1]$ (III.F$'$ Proposition
3.3), so the weights of the injectivity argument fit for every $\mathrm{Re}\,\lambda<2$. The other two numbers that
change are the density shifts, which do not occur here: sf carries a b-density at its one end.

*Method.* For fixed $\lambda$ the source cites [Vas13], [Hin25a] and [HV15]; here the estimates are those of Parts I.A
and I.C, whose proofs use of their operators only facts that we verify for $N_{\mathrm{sf}}(\lambda)$: it is the
spectral family, in the dilation-invariant time $T = \log r$, of a stationary operator whose principal symbol is the
dual of the metric $r^{-2}\bar g$ (Lemma 1.2 (g)); its light cone $\{v = 0\}$ is a Killing horizon of $\partial_T$, at
whose conormal bundle the radial estimate of I.A Proposition 4.2 runs with one computed threshold (Lemma 2.2);
$\{-2<v<0\}$ is a region where $v$ is a time function, so I.A's energy estimates apply on slabs (Lemma 2.3); and the end
$\{v = \infty\}$ is a b-elliptic end, as in I.C. The b-regularity at the light cone ([HV15] in the source) is proved by
commuting with the dilation and the rotations, which act on the operator in a way that keeps the threshold (Proposition
2.7). Injectivity is II.F Lemma 5.8's argument, which at $n = 4$ already contains the source's Fourier transform and
tf-normal operator, with the tf-admissibility of III.F$'$. The index 0 property is the source's: invertibility for
$|\mathrm{Im}\,\lambda|$ large in every vertical strip, by a semiclassical estimate. Near the cone point
$\{v = \infty\}$ that estimate is II.F's ([Hin26c] section 10.1.2 at $n = 4$), which needs no lower bound on
$\mathrm{Im}\,\sigma$ there (the source's footnote 86); across $v = 0$ it is written out here, with an escape function
that the source does not state (Lemma 4.1 (b)) and which serves also as the variable semiclassical order (Lemma 4.2).

*Organisation.* Section 1: the operator, its structure, the spaces. Section 2: fixed $\lambda$, the Fredholm property
and the b-regularity (the source's parts (1) and (3)). Section 3: injectivity for $\mathrm{Re}\,\lambda<2$. Section 4:
the semiclassical estimate. Section 5: Proposition 9.2 at $n = 4$. Section 6: findings.

## 1. Setting

### 1.1 The operator

The parameters and the operator $L_b$ are those of III.F section 1 and III.F$'$ section 1, with (C1) assumed (III.F$'$
(C1), an obligation of Part IV) and $\gamma_\Upsilon$ small as in III.F$'$ Proposition 3.3. The Minkowski model $\bar L$
is III.F (2.1); by III.F Lemma 2.1 (2), on $\{|x|>0\}$,
$$2\bar L = -2\partial_{t_*}\rho\big(\rho\partial_\rho-\tfrac32-\bar S\big)+\widehat{2\bar L}(0),
 \qquad\widehat{2\bar L}(0) = \rho^2\tilde L(0)(\omega,\rho\partial_\rho,\partial_\omega),\tag{1.1}$$
where $\rho = |x|^{-1}$, $\bar S$ is the bundle endomorphism of III.F (2.2), homogeneous of degree 0, with
$\mathrm{spec}\,\bar S\subset[0,\infty)$ and $\min\mathrm{spec}\,\bar S = 0$ (III.F (3.1)), and $\tilde L(0)$ is
dilation invariant. By II.C Lemma 1.2 (for $P_0 = 2L_b$, whose $P^{(0)}$ frozen at $\rho = 0$ is $\tilde L(0)$, III.F
Lemma 2.1 (3)),
$$\tilde L(0)(\omega,x,\partial_\omega) = -x^2+a(\omega)x+\Delta_{\mathbb S^3}+V(\omega,\partial_\omega)
+b(\omega),\tag{1.2}$$
with $a$, $b$ smooth endomorphisms, $V$ a first-order operator on $\mathbb S^3$ and $\Delta_{\mathbb S^3}\ge0$ acting
componentwise; sections of $S^2T^*$ (rank 15) are trivialised by the products of $dt_*,dx^1,\dots,dx^4$. An indicial
root of $\tilde L(0)$ is $r\in\mathbb C$ with $\ker\tilde L(0)(\omega,r,\partial_\omega)\ne0$; these are the roots of
III.F$'$ Proposition 2.3, none with real part in $(0,1]$.

On $\mathbb R^{1+4}\setminus\{x = 0\}$ use $\rho$, $v := \rho t_* = (t-|x|)/|x|$ and $\omega$. Then
$\partial_{t_*}|_\rho = \rho\partial_v$ and $\rho\partial_\rho|_{t_*} = \rho\partial_\rho|_v+v\partial_v$, so (1.1)
reads $2\rho^{-2}\bar L = -2\partial_v(\rho\partial_\rho+v\partial_v-\frac32-\bar S)+\tilde
L(0)(\omega,\rho\partial_\rho+v\partial_v,\partial_\omega)$, which commutes with $\rho\partial_\rho$.

**Definition 1.1 ([Hin26] (9.2) at $n = 4$).** For $\lambda\in\mathbb C$,
$$N_{\mathrm{sf}}(\lambda) := -2\partial_v\big(v\partial_v+\lambda-\tfrac32-\bar S\big)+\tilde L(0)(\omega,v\partial_v
+\lambda,\partial_\omega),\tag{1.3}$$
so that $2\rho^{-2}\bar L(\rho^\lambda u) = \rho^\lambda N_{\mathrm{sf}}(\lambda)u$ for $u = u(v,\omega)$. It acts on
sections over $\mathrm{sf} := \mathbb R_v\times\mathbb S^3$; we write $R := v^{-1}$ near $v = +\infty$.

(*Computed:* `sf5.py` S1 finds (1.3) for the scalar wave operator, $\bar S = 0$,
$\tilde L(0)(x) = -x^2+2x+\Delta_{\mathbb S^3}$, from $\rho^{-2-\lambda}\Box(\rho^\lambda u)$; the control with $c = 1$
fails.)

**Lemma 1.2 (structure).** (a) The principal symbol of $N_{\mathrm{sf}}(\lambda)$ is $p_2\,\mathrm{Id}$,
$p_2(v,\omega;\xi,\eta) := v(v+2)\xi^2+|\eta|^2$ ($\xi$ dual to $v$, $|\eta|$ the round norm), so
$N_{\mathrm{sf}}(\lambda)$ is elliptic over $\{v>0\}\cup\{v<-2\}$, and on $\{-2<v<0\}$, $p_2$ is the dual of a
Lorentzian metric for which $dv$ is timelike.

(b) Near $v = \infty$, with $R = v^{-1}$,
$$N_{\mathrm{sf}}(\lambda) = 2R(R\partial_R)\big(-R\partial_R+\lambda-\tfrac32-\bar S\big)+\tilde L(0)(\omega,\lambda
-R\partial_R,\partial_\omega),\tag{1.4}$$
an operator $L$ of I.C section 2.5 at the end at 0 ($\varrho = R$), b-elliptic on $\{R<2\}$ (its b-principal symbol is
$(1+2R)\zeta^2+|\eta|^2$), with normal operator $\tilde L(0)(\omega,\lambda-R\partial_R,\partial_\omega)$ and Mellin
symbol
$$J_\lambda(\zeta) = \tilde L(0)(\omega,\lambda-\zeta,\partial_\omega) = -\zeta^2+(2\lambda-a)\zeta+\Delta_{\mathbb S^3}
+V+(b+a\lambda-\lambda^2),\tag{1.5}$$
of the form of I.C Lemma 2.4; its roots are $\{\lambda-r\}$, $r$ over the indicial roots of $\tilde L(0)$.

(c) $N_{\mathrm{sf}}(\lambda) = R^{2+\lambda}N_{\iota^+}(\lambda)R^{-\lambda}$ on $\{v>0\}$, with
$$N_{\iota^+}(\lambda) = -2R^{-1}(R\partial_R+\lambda)\big(R\partial_R+\tfrac32+\bar S\big)
+R^{-2}\tilde L(0)(\omega,-R\partial_R,\partial_\omega),\tag{1.6}$$
the source's (9.10)-(9.11) at $n = 4$; $N_{\iota^+}(\lambda)$ is the operator $N^0(\sigma)$ of II.F Definition 1.1 and
(1.6) for $P_0 = 2L_b$, $c = \frac32$, $S_0 = \bar S$, $P^{(0)}(0) = \tilde L(0)$, at $\sigma = -i\lambda$.

(d) $N_{\mathrm{sf}}(\lambda)$ commutes with the Lie derivatives $\mathcal L_\Omega$ along the rotation fields $\Omega$
of $\mathbb S^3$ (acting on sections of $S^2T^*\mathbb R^{1+4}$).

(e) $[v\partial_v,N_{\mathrm{sf}}(\lambda)] = -N_{\mathrm{sf}}(\lambda)+\tilde
L(0)(\omega,v\partial_v+\lambda,\partial_\omega)$, and
$N_{\mathrm{sf}}(\lambda+1)\partial_v = \partial_vN_{\mathrm{sf}}(\lambda)$.

(f) $N_{\mathrm{sf}}(\lambda)-N_{\mathrm{sf}}(\lambda')$ is $(\lambda-\lambda')$ times a first-order operator,
polynomial in $\lambda,\lambda'$, of the form $-2\partial_v+A_1(v\partial_v)+A_0$ with $A_1$, $A_0$ smooth endomorphisms
on $\mathbb S^3$; near $v = \infty$ it lies in $\mathrm{Diff}^1_{\mathrm b}$ (as $\partial_v = -R(R\partial_R)$).

(g) Let $\hat g := |x|^{-2}\bar g$ on $\mathbb R_T\times\mathrm{sf}$, $T := \log|x|$. Then
$\hat g^{-1} = \partial_T^2-2(v+1)\partial_T\partial_v+v(v+2)\partial_v^2+\slashed g^{-1}$; $dT$ is spacelike, $dv$ is
timelike exactly on $\{-2<v<0\}$, and $N_{\mathrm{sf}}(\lambda)$ is the spectral family $e^{i\sigma T}P_ce^{-i\sigma T}$
at $\sigma = -i\lambda$ of the $T$-independent operator $P_c := 2|x|^2\bar L$, whose principal symbol at
$-\sigma\,dT+\xi\,dv+\eta$ is $\hat g^{-1}(-\sigma\,dT+\xi\,dv+\eta) = \sigma^2+2(v+1)\sigma\xi+p_2$;
$P_c-\Box_{\hat g}\mathrm{Id}$ is a first-order operator with $T$-independent coefficients.

*Proof.* (a) The second-order part of (1.3) is $-2\partial_vv\partial_v-(v\partial_v)^2+\Delta_{\mathbb S^3}$, with
symbol $2v\xi^2+v^2\xi^2+|\eta|^2$. (b) $v\partial_v = -R\partial_R$ and $\partial_v = -R^2\partial_R$; the term
$-2R(R\partial_R)^2$ has b-symbol $2R\zeta^2$, and $-(R\partial_R)^2$ in $\tilde L(0)$ gives $\zeta^2$. On $R^\zeta$,
$v\partial_v+\lambda$ acts as $\lambda-\zeta$; expanding (1.2) at $x = \lambda-\zeta$ gives (1.5). (c) Conjugating (1.4)
by $R^{\lambda}$ replaces $R\partial_R$ by $R\partial_R+\lambda$; multiplying by $R^{-2}$ gives (1.6), which is II.F
(1.6) with these data at $\sigma = -i\lambda$. (d) $\bar g$, $t_*$, $|x|$, $d\bar t$ and $d|x|$ are invariant under the
rotations of the spatial factor, so $\bar L$, built from them (III.F (2.1), III.D section 2), commutes with
$\mathcal L_\Omega$; so does $\rho$, and $\mathcal L_\Omega$ preserves $v$. (e) $\bar S$ and the coefficients of
$\tilde L(0)$ do not depend on $v$, and $[v\partial_v,\partial_v] = -\partial_v$; the second identity is
$\partial_{t_*}\bar L = \bar L\partial_{t_*}$ with $\partial_{t_*}(\rho^\lambda u) = \rho^{\lambda+1}\partial_vu$.
(*Computed:* `sf5.py` S5, with a failing control.) (f) From (1.2)-(1.3). (g) With $r := |x| = e^T$ and $t = r(v+1)$,
$\bar g$ and its inverse are computed in $(T,v,\omega)$ (`sf5.py` S2, control $\hat g^{-1}(dT,dT) = -1$ fails);
$\rho^\lambda = e^{-\lambda T} = e^{-i\sigma T}$ for $\sigma = -i\lambda$; and $|x|^2\Box_{\bar g}-\Box_{\hat g}$ is
first order for the conformal factor $|x|^{-2}$. $\square$

At $\sigma = -i\lambda$, $\mathrm{Im}\,\sigma = -\mathrm{Re}\,\lambda$. The region $\{v>0\}$ is where $\partial_T$ is
timelike for $\hat g$ (inside the light cone of the origin); $\{v = 0\}$ is a Killing horizon of $\partial_T$;
$\{v = -2\}$ is past null infinity; and $v = \infty$ is the timelike line $\{x = 0\}$, a conic singularity of the
dilation-reduced space.

### 1.2 The spaces

Let $\mathrm{sf}_{\ge-1} := [-1,\infty]_v\times\mathbb S^3$, compactified at $v = \infty$ by $R = v^{-1}$, with the
density $\mu_{\mathrm{sf}} := |\frac{dv}{2+v}\,d\slashed g|$ ([Hin26] Proposition 9.2), smooth and positive on
$\{v>-2\}$ and a b-density at $R = 0$ ($\frac{|dv|}{2+v} = \frac{|dR|}{R(1+2R)}$). Fix
$\chi_\partial\in C^\infty(\mathbb R_v)$ with $\chi_\partial = 0$ on $\{v\le2\}$ and $\chi_\partial = 1$ on $\{v\ge4\}$.

**Definition 1.3 ([Hin26] Definition 9.1 at $n = 4$).** For $s,\mu\in\mathbb R$,
$\dot H^{s,\mu}_{\mathrm b}(\mathrm{sf}_{\ge-1})$ is the space of distributions $u$ on $\mathbb R_v\times\mathbb S^3$
supported in $\{v\ge-1\}$ with
$$\|u\|^2_{\dot H^{s,\mu}_{\mathrm b}} := \|(1-\chi_\partial)u\|^2_{H^s}
+\|\chi_\partial u\|^2_{H^s_{\mathrm b,\mu}}<\infty,\tag{1.7}$$
$H^s$ the Sobolev space on $(-2,5)\times\mathbb S^3$ and $H^s_{\mathrm b,\mu}$ I.C's Definition 2.1 at the end at 0 with
$\varrho = R$ (so at $s = 0$ the norm is that of $R^{-\mu}L^2(\mu_{\mathrm{sf}})$:
$\dot H^{s,\mu}_{\mathrm b} = \langle v\rangle^{-\mu}H^s_{\mathrm b}$ near $v = \infty$, the source's).
$\bar H^{s,\mu}_{\mathrm b}(\mathrm{sf}_{\ge-1})$ is the space of restrictions to $\{v>-1\}$ of such distributions
without the support condition (extendible at $v = -1$), with the quotient norm. For $k\in\mathbb N_0$,
$\dot H^{(s;k),\mu}_{\mathrm b;\mathrm b}$ consists of the $u\in\dot H^{s,\mu}_{\mathrm b}$ with
$(v\partial_v)^j\mathcal L_\Omega^\alpha u\in\dot H^{s,\mu}_{\mathrm b}$ for $j+|\alpha|\le k$,
$\mathcal L_\Omega^\alpha$ the words of length $|\alpha|$ in the Lie derivatives along the six rotation fields
$\Omega_1,\dots,\Omega_6$ of $\mathbb S^3$; $\dot H^{(s;\infty),\mu}_{\mathrm b;\mathrm b}$ is the intersection.

Since $\mathcal L_\Omega$ differs from $\Omega$ acting componentwise by a constant matrix, the same space results with
componentwise $\Omega$. On compact subsets of $\{v\ne0\}$, $v\partial_v$ and the $\Omega_a$ span the vector fields, so
there $\dot H^{(s;k),\mu}_{\mathrm b;\mathrm b}$ is $H^{s+k}$; near $R = 0$ it is $H^{s+k}_{\mathrm b,\mu}$ (I.C Lemma
2.2 (h)).

*Duality and calculi.* With the pairing of $L^2(\mu_{\mathrm{sf}})$ and a fibre inner product $h$ (below),
$(\dot H^{s,\mu}_{\mathrm b})^* = \bar H^{-s,-\mu}_{\mathrm b}$: near $v = -1$ by I.A Lemma 6.1 (b), near $R = 0$ by I.C
Lemma 2.2 (d), glued with $\chi_\partial$. For $\mathrm{Re}\,\lambda$ in a compact set,
$N_{\mathrm{sf}}(\lambda):\dot H^{s,\mu}_{\mathrm b}\to\dot H^{s-2,\mu}_{\mathrm b}$ is bounded (I.C Lemma 2.2 (c) near
$R = 0$, by (1.4)). On $\{-\frac32<v<5\}$ we use the diffeomorphism $(v,\omega)\mapsto x = e^v\omega$ onto an annulus of
$\mathbb R^4$, so that the pseudodifferential operators of I.A section 2 and the semiclassical ones of I.B section 2
with kernels supported there act; the decay orders are then immaterial. Near $R = 0$ we use $x = R\omega$, I.C's end at
0.

**Lemma 1.4 (fibre inner products).** For every $\delta>0$ there is a smooth fibre inner product $h$ on
$\mathbb S^3\times\mathbb C^{15}$, independent of $v$, with
$\mathrm{Re}_h\bar S := \frac12(\bar S+\bar S^{*h})\ge-\delta$ everywhere.

*Proof.* The construction in the proof of III.F$'$ Corollary 3.4 (a Jordan basis of $\bar S(\omega)$ rescaled, the
strict inequality persisting near $\omega$, a partition of unity on $\mathbb S^3$; the condition is convex in $h$), with
$\min\mathrm{spec}\,\bar S = 0$. $\square$

## 2. Fixed $\lambda$: the Fredholm property and b-regularity ([Hin26] Proposition 9.2 (1), (3))

### 2.1 The dynamics and the radial set

Write $\mathcal R_\pm := \{v = 0,\ \eta = 0,\ \pm\xi>0\}\subset T^*\mathrm{sf}\setminus o$, the two halves of
$N^*\{v = 0\}\setminus o$, $\partial\mathcal R_\pm$ their images at fibre infinity, $\Sigma_0 := \{p_2 = 0\}$ at fibre
infinity, $\rho_\infty := |\xi|^{-1}$ near $\partial\mathcal R_\pm$, $\hat\eta := \rho_\infty\eta$, and
$\mathsf H := \pm\rho_\infty H_{p_2}$ near $\partial\mathcal R_\pm$, the convention of I.A section 4.1.

**Lemma 2.1 (dynamics at fibre infinity).** (a) Over $\{v\ge0\}$,
$\Sigma_0 = \partial\mathcal R_+\cup\partial\mathcal R_-$; over $\{v>0\}$ and $\{v<-2\}$, $\Sigma_0 = \emptyset$.

(b) Near $\partial\mathcal R_\pm$: $\mathsf H\rho_\infty = \beta_0\rho_\infty$ with $\beta_0 = 2(1+v)$, $\mathsf H$
vanishes on $\partial\mathcal R_\pm$, and $\tilde q := v^2+|\hat\eta|^2$ is a quadratic defining function of
$\partial\mathcal R_\pm$ at fibre infinity with $\mathsf H\tilde q = 4(v+2)v^2+4(1+v)|\hat\eta|^2\ge2\tilde q$ on
$\{|v|\le\frac12\}$. So $\partial\mathcal R_\pm$ is a source for $\mathsf H$ in the sense of I.A section 4.1 (Lemma
4.1's conclusion holds with $\tilde q$).

(c) Over $\{-2<v<0\}$, $\mathsf Hv = 2v(v+2)<0$ on $\Sigma_0$. Every integral curve of $\mathsf H$ in $\Sigma_0$ over
$\{-2<v<0\}$ has $v$ strictly decreasing, tends to $\partial\mathcal R_+\cup\partial\mathcal R_-$ in the backward
direction, and reaches $\{v<-1\}$ in the forward direction.

*Proof.* (a) Over $v\ge0$, $p_2 = 0$ forces $\eta = 0$ and, for $v>0$, $\xi = 0$. (b)
$H_{p_2} = 2v(v+2)\xi\partial_v-2(1+v)\xi^2\partial_\xi+H_{|\eta|^2}$; $\{p_2,|\eta|^2\} = 0$, as $p_2$ is a sum of
functions of $(v,\xi)$ and of $(\omega,\eta)$; and $\rho_\infty = |\xi|^{-1}$. (*Computed:* `sf5.py` S3, with a failing
control.) (c) On $\Sigma_0$ over $(-2,0)$, $\xi\ne0$ (else $\eta = 0$), and
$\mathsf Hv = \pm\rho_\infty\cdot2v(v+2)\xi = 2v(v+2)$. Backward, $v$ increases and is bounded by 0; if its limit were
$v_1<0$, $\mathsf Hv\le-c<0$ near $v_1$ would contradict boundedness of the time; so $v\to0$, and then
$|\hat\eta|^2 = -v(v+2)\to0$ on $\Sigma_0$, so the curve tends to
$\{v = 0,\hat\eta = 0\} = \partial\mathcal R_+\cup\partial\mathcal R_-$. Forward, $\mathsf Hv\le-c(v_0)<0$ on
$\{v\le v_0\}$, $v_0<0$, so $v$ reaches every value in $(-2,v_0)$. $\square$

**Lemma 2.2 (radial estimate at the light cone).** Let $\mathcal D\subset\mathbb C$ be compact, $\delta>0$, $h$ as in
Lemma 1.4, and $M$ a first-order differential operator on a neighbourhood of $\{v = 0\}$, with smooth coefficients,
whose principal symbol vanishes on $\mathcal R_\pm$, acting on $\mathbb C^{15}\otimes\mathbb C^m$ (the case $M = 0$,
$m = 1$ being $N_{\mathrm{sf}}(\lambda)$ itself). Put $N := N_{\mathrm{sf}}(\lambda)\otimes\mathrm{Id}+M$. Let $U$ be a
neighbourhood of $\partial\mathcal R_\pm$.

(1) (*Below threshold.*) Let $s<2-\delta-\sup_{\mathcal D}\mathrm{Re}\,\lambda$. There are $B,G,E\in\Psi^0$,
microsupported in $U$, with kernels supported near $\{v = 0\}$, $B$ elliptic at $\partial\mathcal R_\pm$ and
$\mathrm{WF}'(E)\cap\partial\mathcal R_\pm = \emptyset$, such that for $\lambda\in\mathcal D$, all $N_1$, in the strong
sense,
$$\|Bu\|_{H^s}\le C\big(\|GNu\|_{H^{s-1}}+\|Eu\|_{H^s}+\|u\|_{H^{-N_1}}\big).\tag{2.1}$$

(2) (*Above threshold, the adjoint.*) Let $s'>s_0>\delta-1+\sup_{\mathcal D}\mathrm{Re}\,\lambda$. There are $B$, $G$ as
in (1) with, for $\lambda\in\mathcal D$, in the strong sense,
$$\|Bw\|_{H^{s'}}\le C\big(\|GN^{*h}w\|_{H^{s'-1}}+\|Gw\|_{H^{s_0}}+\|w\|_{H^{-N_1}}\big),\tag{2.2}$$
the adjoint taken for $L^2(\mu_{\mathrm{sf}})$ and $h$ (any other fibre inner product, as I.A Proposition 4.2 notes).

*Proof.* The proof of I.A Proposition 4.2 uses of $\hat P(\sigma)$ and of (H1)-(H5) only: that the operator is a
differential operator with principal symbol $G_0\,\mathrm{Id}$, $G_0$ real; that $\partial\mathcal R$ is a source of
$\mathsf H$ with $\mathsf H\rho_\infty = \beta_0\rho_\infty$, $\beta_0>0$; a quadratic defining function $\tilde q$ of
$\partial\mathcal R$ with $\mathsf H\tilde q\ge c'\tilde q$ (its Lemma 4.1); and the bound (4.1),
$\beta_0^{-1}p_1\le\vartheta\,\mathrm{Id}$ on $\partial\mathcal R$, where
$p_1 := \pm\rho_\infty\sigma_1(\mathrm{Im}_h(\cdot))$; its kernels are compactly supported, so the decay order is
immaterial. Here $G_0 = p_2$ (Lemma 1.2 (a); $M$ is first order), and Lemma 2.1 (b) gives the source structure with
$\beta_0 = 2(1+v)$ and $\tilde q$. It remains to compute $p_1$ on $\partial\mathcal R_\pm$.

*The subprincipal symbol at the light cone.* The first-order terms of $N_{\mathrm{sf}}(\lambda)$ are
$-2(\lambda-\frac32-\bar S)\partial_v$, the terms $a\,v\partial_v$, $-2\lambda\,v\partial_v$ and $V$ of (1.2)-(1.3), and
the first-order parts of $\mathrm{Im}_h$ of the second-order part
$-2\partial_vv\partial_v-(v\partial_v)^2+\Delta_{\mathbb S^3}$. The symbols of $v\partial_v$ and of $V$ vanish on
$\mathcal R_\pm$ ($v = 0$, resp. $\eta = 0$); so do those of $M$. For the second-order part: the density
$\mu_{\mathrm{sf}}$ and $h$ do not depend on $v$ except through the factor $(2+v)^{-1}$, and
$\Delta_{\mathbb S^3}-\Delta_{\mathbb S^3}^{*h} = H^{-1}[H,\Delta_{\mathbb S^3}]$ has symbol linear in $\eta$; the
first-order coefficient of $\mathrm{Im}$ of $-2\partial_vv\partial_v-(v\partial_v)^2$ at $v = 0$ is 0 (`sf5.py` S4: the
coefficient of $\partial_v^2$ in $N-N^*$ vanishes, and the full first-order coefficient of $(N-N^*)/2i$ at $v = 0$ comes
from $-2(\lambda-\frac32-S)\partial_v$ alone). And $\sigma_1(\mathrm{Im}_h(-2(\lambda-\frac32-\bar S)\partial_v)) =
\frac1{2i}(-2i\xi A-2i\xi A^{*h}) = -\xi(A+A^{*h})$, $A := \lambda-\frac32-\bar S$. So on $\mathcal R_\pm$
$$\sigma_1(\mathrm{Im}_hN) = \xi\big(3+2\,\mathrm{Re}_h\bar S-2\,\mathrm{Re}\,\lambda\big),\qquad p_1 = 3
+2\,\mathrm{Re}_h\bar S-2\,\mathrm{Re}\,\lambda,\qquad\beta_0^{-1}p_1 = \tfrac32+\mathrm{Re}_h\bar S
-\mathrm{Re}\,\lambda\tag{2.3}$$
(`sf5.py` S4 computes the scalar version with complex constants $\lambda$, $S$, with the control $c = 1$ failing).

*(2).* For $N^{*h}$, $\mathrm{Re}_h$ is the same and $\mathrm{Im}_h$ changes sign, so $\beta_0^{-1}p_1(N^{*h}) =
-(\frac32+\mathrm{Re}_h\bar S-\mathrm{Re}\,\lambda)\le(\mathrm{Re}\,\lambda-\frac32+\delta)\mathrm{Id}$ by Lemma 1.4:
the bound (4.1) of I.A with $\vartheta := \sup_{\mathcal D}\mathrm{Re}\,\lambda-\frac32+\delta$ (no
$\mathrm{Im}\,\sigma$ term enters: (4.1) is used in the proof only through
$Q_\epsilon\ge2\beta_0(s_0-\frac12-\vartheta)$). The proof of I.A Proposition 4.2 (1) for $N^{*h}$ gives (2.2) for
$s'>s_0>\frac12+\vartheta$, which is the stated condition.

*(1).* $N = (N^{*h})^{*h}$, and the proof of I.A Proposition 4.2 (2), with $\hat P(\sigma) := N^{*h}$ and the
$\vartheta$ just found, gives (2.1) at every order $1-s''$ with $s''>\frac12+\vartheta$, i.e. at every
$s<\frac12-\vartheta = 2-\delta-\sup\mathrm{Re}\,\lambda$, with the control operator $E$ microsupported in
$\mathrm{supp}\,\psi'(\varsigma_R\tilde q)$, away from $\partial\mathcal R_\pm$; the iteration runs from $-N_1$ with no
threshold, which is the strong sense. Uniformity in $\lambda\in\mathcal D$: the symbols are polynomial in $\lambda$.
$\square$

In (1), the threshold is $s<2+\min\mathrm{spec}\,\bar S-\mathrm{Re}\,\lambda$ up to $\delta$; the source's derivation
from the characteristic exponents $0$ and $\frac32+\alpha-\lambda$ of $vN_{\mathrm{sf}}(\lambda)$ at $v = 0$,
$\alpha\in\mathrm{spec}\,\bar S$, and $\chi^w_+\in H^{\mathrm{Re}\,w+\frac12-\epsilon}_{\mathrm{loc}}$, gives the same
number (the record's `iotasol5.py` J2).

### 2.2 The artificial boundary and the hyperbolic region

**Lemma 2.3 (slab estimates).** On slabs $\Omega_{a,b} := \{a<-v<b\}\times\mathbb S^3$ with $0<a<b<2$, the statements of
I.A Propositions 6.3, 6.4 and Corollary 6.5 hold for $L = N_{\mathrm{sf}}(\lambda)$ and for
$L = N_{\mathrm{sf}}(\lambda)^{*h}$, uniformly for $\lambda$ in compact sets, with $r := -v$ (so that the spaces
$H^s(\Omega_{a,b})^{\bullet,-}$, supported at $r = b$, are supported at $v = -b$). In particular, with the cut-offs of
I.A Corollary 6.5 placed at $r = \frac12$ and $r = \frac14$ (that is $v = -\frac12$ and $v = -\frac14$):
$$\|u|_{\{-1<v<-1/4\}}\|_{H^s}\le C\|N_{\mathrm{sf}}(\lambda)u|_{\{-1<v<-1/4\}}\|_{H^{s-1}},
 \qquad u\in\dot H^s\ \text{near}\ \{v = -1\},\tag{2.4}$$
$$\|\chi w\|_{\bar H^{1-s}}\le C\big(\|N_{\mathrm{sf}}(\lambda)^{*h}w\|_{\bar H^{-s}(\{-1<v<-1/4\})}
+\|\chi_1w\|_{H^{1-s}}\big),\qquad w\in\bar H^{1-s}\ \text{near}\ \{v = -1\},\tag{2.5}$$
with $\chi = 1$ on $\{v\le-\frac12\}$, $\chi = 0$ near $\{v\ge-\frac14\}$ and $\chi_1$ supported in
$\{-\frac12<v<-\frac14\}$, equal to 1 near $\mathrm{supp}\,d\chi$.

*Proof.* The proofs of I.A Propositions 6.3 and 6.4 use of $L$ only: order 2, principal symbol $G_0\,\mathrm{Id}$ with
$G_0$ the dual of a Lorentzian metric $\mathfrak g$ on the slab for which $dr$ is timelike, bounds for the coefficients
and for $\inf(-G_0(dr))$; that $L^*$ is of the same form; and that the null bicharacteristics of $G_0$ move strictly
monotonically in $r$ (I.A section 6.2 and (H4)), used with I.A Propositions 5.1 and 5.2. For $N_{\mathrm{sf}}(\lambda)$
on $\{-2<v<0\}$: $G_0 = p_2$ is the dual of a Lorentzian metric with $dv$ timelike and
$-p_2(dv) = -v(v+2)\ge\min\big(a(2-a),b(2-b)\big)>0$ on $\overline{\Omega_{a,b}}$ (Lemma 1.2 (a)); its adjoint has the
same principal symbol; and $v$ is strictly monotone along the bicharacteristics there (Lemma 2.1 (c), and at finite
frequencies the same, as $H_{p_2}v = 2v(v+2)\xi\ne0$ on $\{p_2 = 0\}\setminus o$). Time-orient $\mathfrak g$ so that $v$
increases to the future; then $r = -v$ decreases to the future, as in I.A. (2.4) is I.A (6.2) with the roles of $L$ and
$L^*$ exchanged (Proposition 6.4 (i) for the forward problem, the support at $r = 1$), and (2.5) is I.A (6.1)
(Proposition 6.4 (ii) applied to $\chi w$, the commutator $[L,\chi]$ supported in $\mathrm{supp}\,d\chi$). $\square$

### 2.3 The Fredholm property

Fix $\lambda\in\mathbb C$, and call $(s,\mu)$ *admissible for* $\lambda$ if
$$s<2-\mathrm{Re}\,\lambda,\qquad\mu\in(\mathrm{Re}\,\lambda-1,\mathrm{Re}\,\lambda).\tag{2.6}$$
Then $\mu$ is not the real part of a root of $J_\lambda$ (1.5): $\mathrm{Re}(\lambda-r) = \mu$ would give
$\mathrm{Re}\,r\in(0,1)$, which III.F$'$ Proposition 2.3 (a) excludes. Put
$$\mathcal X := \{u\in\dot H^{s,\mu}_{\mathrm b}:N_{\mathrm{sf}}(\lambda)u\in\dot H^{s
-1,\mu}_{\mathrm b}\},\quad\mathcal Y := \dot H^{s-1,\mu}_{\mathrm b},\quad\mathcal X^* := \{w\in\bar H^{1
-s,-\mu}_{\mathrm b}:N_{\mathrm{sf}}(\lambda)^{*h}w\in\bar H^{-s,-\mu}_{\mathrm b}\},\tag{2.7}$$
Hilbert spaces with the graph norms, $\mathcal Y^* = \bar H^{1-s,-\mu}_{\mathrm b}$. By Lemma 1.2 (f), $\mathcal X$ is
the same space for every $\lambda'$ near $\lambda$, with equivalent norms.

**Proposition 2.4 ([Hin26] Proposition 9.2 (1), the Fredholm property, at $n = 4$).** Let $(s,\mu)$ be admissible for
$\lambda$ and $\mu_0<\mu$.

(1) For every $N_1$ there is $C$ with, for $u\in\mathcal X$ and $w\in\mathcal X^*$,
$$\|u\|_{\dot H^{s,\mu}_{\mathrm b}}\le C\big(\|N_{\mathrm{sf}}(\lambda)u\|_{\dot H^{s-1,\mu}_{\mathrm b}}
+\|u\|_{\dot H^{-N_1,\mu_0}_{\mathrm b}}\big),\tag{2.8}$$
$$\|w\|_{\bar H^{1-s,-\mu}_{\mathrm b}}\le C\big(\|N_{\mathrm{sf}}(\lambda)^{*h}w\|_{\bar H^{-s,-\mu}_{\mathrm b}}
+\|w\|_{\bar H^{-N_1,-\mu-1}_{\mathrm b}}\big),\tag{2.9}$$
uniformly for $\lambda$ in a compact set on which $(s,\mu)$ stays admissible. (2.8) holds in the strong sense: if
$u\in\dot H^{-N_1,\mu}_{\mathrm b}$ has $N_{\mathrm{sf}}(\lambda)u\in\dot H^{s-1,\mu}_{\mathrm b}$, then
$u\in\dot H^{s,\mu}_{\mathrm b}$.

(2) $N_{\mathrm{sf}}(\lambda):\mathcal X\to\mathcal Y$ is Fredholm, and the annihilator of its range in $\mathcal Y^*$
is $\ker_{\mathcal X^*}N_{\mathrm{sf}}(\lambda)^{*h}$.

(3) Its kernel and the annihilator of its range do not depend on the admissible pair $(s,\mu)$; nor, therefore, does its
index. Kernel elements lie in $\dot H^{s',\mu'}_{\mathrm b}$ for every admissible $(s',\mu')$, are smooth on $\{v\ne0\}$
and, near $R = 0$, lie in $\mathcal A^{c}$ for every $c<\mathrm{Re}\,\lambda$; annihilator elements are smooth on
$(-1,\infty)\times\mathbb S^3$ up to $\{v = -1\}$ and lie in $\mathcal A^{c}$ near $R = 0$ for every
$c<1-\mathrm{Re}\,\lambda$.

*Proof.* (1) *Near $v = -1$.* (2.4) bounds $u$ on $\{-1<v<-\frac14\}$ in $H^s$ by $N_{\mathrm{sf}}(\lambda)u$ there,
with no error term.

*The hyperbolic region and the light cone.* Let $B_*$, $E$ be the operators of Lemma 2.2 (1) at
$\partial\mathcal R_+\cup\partial\mathcal R_-$, with $U$ so small that the closed set $K_E\supset\mathrm{WF}'(E)$ lies
over $\{-\frac18<v<\frac18\}$. Every point of $K_E$ is either elliptic for $p_2$ (Lemma 2.1 (a) and $p_2\ne0$ off
$\Sigma_0$) or a point of $\Sigma_0$ over $\{v<0\}$, whose forward $\mathsf H$-curve reaches $\{v<-\frac12\}$ by Lemma
2.1 (c) ($v$ decreases along it). Along these curves, of bounded length outside the neighbourhood $U_*$ of
$\partial\mathcal R_\pm$, I.A Proposition 5.2 applies at fibre infinity ($P_I = P_I^{\mathrm{sub}}$ there, the order
constant), with control from $\{v<-\frac12\}$, where (2.4) applies; finitely many such estimates, I.A Proposition 5.1
off $\Sigma_0$, and compactness give $\|Eu\|_{H^s}\le C(\|N_{\mathrm{sf}}u\|_{H^{s-1}}+\|\varphi u\|_{H^{-N_1}})$,
$\varphi$ a cut-off to $\{v<5\}$. With (2.1), I.A Proposition 5.1 on the rest of fibre infinity over $\{-1\le v\le5\}$
(elliptic by Lemma 2.1 (a) and (c), and Lemma 2.1 (c)'s curves for $\Sigma_0$ over $\{-1<v<0\}$), and the fact that at
finite frequencies over a compact set every operator of order $-\infty$ is bounded by $\|u\|_{H^{-N_1}}$ there,
$$\|(1-\chi_\partial)u\|_{H^s}\le C\big(\|N_{\mathrm{sf}}(\lambda)u\|_{H^{s-1}(\{v<5\})}
+\|\varphi u\|_{H^{-N_1}}\big).\tag{2.10}$$

*Near $R = 0$.* $N_{\mathrm{sf}}(\lambda)$ is of the form of I.C section 2.5 at the end at 0, b-elliptic (Lemma 1.2
(b)); I.C Lemma 2.5 at the b-weight $\mu$ gives $\|\chi_\partial u\|_{H^s_{\mathrm b,\mu}}\le C(\|\tilde\chi_\partial
N_{\mathrm{sf}}u\|_{H^{s-2}_{\mathrm b,\mu}}+\|\tilde\chi_\partial u\|_{H^{-N_1}_{\mathrm b,\mu}})$, and I.C Lemma 2.6
at $c = \mu$ (not the real part of a root of $J_\lambda$) with I.C Lemma 2.2 (g), exactly as in the proof of I.C Theorem
3.1 (1) (*Near $\partial X$*), bounds the last term by
$C\|N_{\mathrm{sf}}u\|_{H^{-N_1-2}_{\mathrm b,\mu}}+C\|u\|_{\dot H^{-N_1,\mu_0}_{\mathrm b}}$ plus a term absorbed. With
(2.10) this is (2.8); the overlap $\{2<v<5\}$ is in the interior, where the norms agree.

*The adjoint.* For $w\in\mathcal X^*$: (2.5) near $v = -1$, its last term controlled by the estimates that follow on
$\{-\frac12<v<-\frac14\}$. Lemma 2.2 (2) at $\partial\mathcal R_\pm$ at the order $1-s$, with
$s_0\in(\mathrm{Re}\,\lambda-1+\delta,1-s)$ ($\delta$ small: $1-s>\mathrm{Re}\,\lambda-1$ is (2.6)); then I.A
Proposition 5.2 along the $\mathsf H$-curves of Lemma 2.1 (c) forwards, from a neighbourhood of $\partial\mathcal R_\pm$
to $\{v<-\frac12\}$ (this is the adjoint chain of I.A section 7.1, the curves starting in the region controlled by the
radial estimate); I.A Proposition 5.1 elsewhere. The term $\|Gw\|_{H^{s_0}}$ is bounded by
$\delta'\|w\|_{H^{1-s}}+C_{\delta'}\|w\|_{H^{-N_1}}$ on a compact set (Ehrling, as $s_0<1-s$). Near $R = 0$,
$N_{\mathrm{sf}}(\lambda)^{*h}$ is b-elliptic with Mellin symbol $H_0^{-1}J_\lambda(-\bar\zeta)^\dagger H_0$ up to
$\mathbb S^3$-terms of lower order, whose roots are $\{-\bar\zeta:\zeta\ \text{a root of}\ J_\lambda\}$, for the
b-density $\mu_{\mathrm{sf}}$ ($(R\partial_R)^{\dagger} = -R\partial_R$; I.C (3.5) without the shift by 2, which there
came from $|dx|$); $-\mu$ is not the real part of one. I.C Lemmas 2.5-2.6 and 2.2 (g) give (2.9) as there.

(2) The inclusions $\dot H^{s,\mu}_{\mathrm b}\hookrightarrow\dot H^{-N_1,\mu_0}_{\mathrm b}$ and
$\bar H^{1-s,-\mu}_{\mathrm b}\hookrightarrow\bar H^{-N_1,-\mu-1}_{\mathrm b}$ are compact for $-N_1<\min(s,1-s)$ (I.C
Lemma 2.2 (e) at $R = 0$, Rellich on the compact remainder), so (2.8)-(2.9) give finite-dimensional kernels and closed
ranges (Peetre). *Green's formula* $\langle N_{\mathrm{sf}}u,w\rangle = \langle u,N_{\mathrm{sf}}^{*h}w\rangle$ for
$u\in\mathcal X$, $w\in\mathcal X^*$: split with $\chi_\partial$ and a cut-off near $v = -1$; near $v = -1$ it is I.A
Lemma 6.1 (d) and the density of $C_c^\infty(\{v>-1\})$ in $\dot H^s$ (I.A Lemma 6.1 (a)); near $R = 0$ the argument of
the proof of I.C Theorem 3.1 (*Green's formula*); in between, Friedrichs mollifiers $J_\epsilon$:
$[N_{\mathrm{sf}},J_\epsilon]$ is bounded $H^s\to H^{s-1}$ uniformly and tends to 0 strongly, so $J_\epsilon u\to u$ in
$\mathcal X$ locally. The cokernel then is the kernel of $N^{*h}_{\mathrm{sf}}$ on $\mathcal X^*$, as in I.C Theorem 3.1
(*Cokernel*).

(3) *Kernel.* Let $u\in\mathcal X$, $N_{\mathrm{sf}}(\lambda)u = 0$. The estimates of (1) hold in the strong sense at
every order $s'<2-\mathrm{Re}\,\lambda$: (2.1) needs no a priori regularity beyond $H^{-N_1}$, the propagation and
elliptic estimates and (2.4) hold at every order. So $u\in H^{s'}$ on $\{v<5\}$ for all such $s'$, and $u\in H^\infty$
on compact subsets of $\{v\ne0\}$ (there the radial estimate is not needed: ellipticity on $v>0$, propagation from (2.4)
on $v<0$). Near $R = 0$, I.C Lemma 2.5 at every order and Lemma 2.7, with
$(c_-,c_+) := (\mathrm{Re}\,\lambda-1,\mathrm{Re}\,\lambda)$ containing no real part of a root of $J_\lambda$ and
$c = \mu$, give $\chi_\partial u\in H^\infty_{\mathrm b,c'}$ for every $c'<\mathrm{Re}\,\lambda$, so
$u\in\mathcal A^{c'}$ there (I.C Lemma 2.2 (f)). So $u$ is in the kernel for every admissible pair. *Annihilator.* Let
$w\in\mathcal X^*$, $N^{*h}_{\mathrm{sf}}w = 0$. Lemma 2.2 (2) in the strong sense at every order $s'\ge1-s$ (with the a
priori order $1-s$ above threshold), propagation and ellipticity give $w\in H^\infty$ on $(-1,\infty)\times\mathbb S^3$
away from $R = 0$, and (2.5) at every order gives smoothness up to $v = -1$. Near $R = 0$, I.C Lemma 2.7 for
$N^{*h}_{\mathrm{sf}}$, whose root-free strip containing $-\mu$ is $(-\mathrm{Re}\,\lambda,1-\mathrm{Re}\,\lambda)$,
gives $w\in H^\infty_{\mathrm b,c'}$ for every $c'<1-\mathrm{Re}\,\lambda$, which contains the b-weight $-\mu'$ of every
admissible $\mu'$. So $w$ is an annihilator for every admissible pair. $\square$

### 2.4 b-regularity at the light cone ([Hin26] Proposition 9.2 (3))

Let $\mathcal D^m$ be the operators $\sum_{j+|\alpha|\le m}c_{j\alpha}(v,\omega)(v\partial_v)^j\mathcal L_\Omega^\alpha$
on $(-\frac12,2)\times\mathbb S^3$, $c_{j\alpha}$ smooth matrix functions. Since $v\partial_v$ commutes with each
$\mathcal L_\Omega$, $[\mathcal L_{\Omega_a},\mathcal L_{\Omega_b}]$ is a combination of the $\mathcal L_{\Omega_c}$,
and derivatives of the coefficients are smooth, $[\mathcal D^p,\mathcal D^q]\subset\mathcal D^{p+q-1}$ and
$\mathcal D^p\mathcal D^q\subset\mathcal D^{p+q}$. A word $W^\alpha$ is a product of $|\alpha|$ factors from
$\mathcal W := \{v\partial_v,\mathcal L_{\Omega_1},\dots,\mathcal L_{\Omega_6}\}$; every element of $\mathcal D^m$ is a
combination of words of length $\le m$ with smooth coefficients on the left. For $u$ supported in
$(-\frac12,2)\times\mathbb S^3$, $u\in\dot H^{(s;k),\mu}_{\mathrm b;\mathrm b}$ if and only if $W^\alpha u\in H^s$ for
$|\alpha|\le k$, and then $Du\in H^{s}$ for $D\in\mathcal D^k$, $Du\in H^{s-1}$ for $D\in\mathcal D^{k+1}$ (one factor
being a first-order differential operator).

**Lemma 2.5 (commuting with the dilation and the rotations).**
$N_{\mathrm{sf}}(\lambda)\mathcal L_\Omega = \mathcal L_\Omega N_{\mathrm{sf}}(\lambda)$, and
$$N_{\mathrm{sf}}(\lambda)(v\partial_v) = (v\partial_v+1)N_{\mathrm{sf}}(\lambda)-M_1(v\partial_v)
-\sum_aM_a\mathcal L_{\Omega_a}-M_0,\tag{2.11}$$
with $M_1$, $M_a$, $M_0\in\mathcal D^1$ (on all of $\{v>-2\}$, with coefficients independent of $v$), the principal
symbols of $M_1$ and $M_a$ (as first-order differential operators) vanishing on $N^*\{v = 0\}$.

*Proof.* The first identity is Lemma 1.2 (d). By Lemma 1.2 (e),
$N(v\partial_vu) = (v\partial_v+1)Nu-\tilde L(0)(\omega,v\partial_v+\lambda,\partial_\omega)u$. Normalise the rotation
fields so that $\Delta_{\mathbb S^3} = -\sum_a\Omega_a^2$ on functions; with $\Omega_a = \mathcal L_{\Omega_a}-A_a$,
$A_a$ constant matrices, and $V = \sum_aV_a\Omega_a+V_0$ ($V_a$, $V_0$ smooth), (1.2) gives
$$\tilde L(0)(\omega,v\partial_v+\lambda,\partial_\omega)u = M_1(v\partial_vu)+\sum_aM_a(\mathcal L_{\Omega_a}u)+M_0u,$$
$M_1 := -v\partial_v-2\lambda+a$, $M_a := -\Omega_a+A_a+V_a$ (from
$-\Omega_a^2 = -\Omega_a\mathcal L_{\Omega_a}+\Omega_aA_a$ and $\Omega_aA_a = A_a\mathcal L_{\Omega_a}-A_a^2$), and
$M_0 := a\lambda-\lambda^2+b+V_0-\sum_a(V_a+A_a)A_a$. The principal symbol of $M_1$ is $-iv\xi$, of $M_a$ is
$-i\eta(\Omega_a)$; both vanish on $\{v = 0,\eta = 0\}$. $\square$

**Proposition 2.6 (commuted equations).** For every word $W^\alpha$, $|\alpha| = j\ge1$, on
$(-\frac12,2)\times\mathbb S^3$,
$$N_{\mathrm{sf}}(\lambda)W^\alpha = \tilde W^\alpha N_{\mathrm{sf}}(\lambda)-\sum_{|\beta| = j}M_{\alpha\beta}W^\beta
-\sum_{|\beta|<j}M'_{\alpha\beta}W^\beta,\tag{2.12}$$
with $\tilde W^\alpha\in\mathcal D^j$, $M_{\alpha\beta}\in\mathcal D^1$ with principal symbols vanishing on
$N^*\{v = 0\}$, and $M'_{\alpha\beta}\in\mathcal D^{j-|\beta|}$ a combination of products $D_1D_2$ with
$D_1\in\mathcal D^1$ and $D_2\in\mathcal D^{j-1-|\beta|}$.

*Proof.* Induction on $j$. For $j = 1$ it is Lemma 2.5 ($\tilde W = v\partial_v+1$ or $\mathcal L_\Omega$;
$M'_{\cdot,\emptyset} = M_0$, of the form $D_1$ with $D_2 = \mathrm{Id}$). If (2.12) holds for $\alpha$ and
$W\in\mathcal W$, then $NWW^\alpha = (\tilde WN-\sum_{W'}M_{WW'}W'-M_W)W^\alpha$, and $\tilde WNW^\alpha = \tilde
W\tilde W^\alpha N-\sum_\beta\tilde WM_{\alpha\beta}W^\beta-\sum_\beta\tilde WM'_{\alpha\beta}W^\beta$. Write
$\tilde WM_{\alpha\beta}W^\beta = M_{\alpha\beta}\tilde WW^\beta+[\tilde W,M_{\alpha\beta}]W^\beta$: the first is
$M_{\alpha\beta}$ (vanishing symbol) times $WW^\beta$ (length $j+1$) plus terms $M_{\alpha\beta}cW^\beta$ of length $j$
(as $\tilde W-W$ is a constant), of the second kind with $D_1 = cM_{\alpha\beta}$,
$D_2 = \mathrm{Id}\in\mathcal D^{(j+1)-1-j}$; the commutator lies in $\mathcal D^1$ and multiplies $W^\beta$,
$|\beta| = j$, a term of the same kind. For $|\beta|<j$ and $M'_{\alpha\beta} = D_1D_2$,
$\tilde WD_1D_2W^\beta = D_1(\tilde WD_2)W^\beta+[\tilde W,D_1]D_2W^\beta$ with
$\tilde WD_2\in\mathcal D^{j-|\beta|} = \mathcal D^{(j+1)-1-|\beta|}$ and $[\tilde W,D_1]\in\mathcal D^1$: of the second
kind for the length $j+1$. $M_{WW'}W'W^\alpha$ is of the first kind ($W'W^\alpha$ of length $j+1$); $M_WW^\alpha$ is of
the second kind ($D_1 = M_W$, $D_2 = \mathrm{Id}$, $|\beta| = j$). $\square$

**Proposition 2.7 ([Hin26] Proposition 9.2 (3) at $n = 4$).** Let $(s,\mu)$ be admissible for $\lambda$,
$k\in\mathbb N_0$, $u\in\dot H^{s,\mu}_{\mathrm b}$ with
$N_{\mathrm{sf}}(\lambda)u\in\dot H^{(s-1;k),\mu}_{\mathrm b;\mathrm b}$. Then
$u\in\dot H^{(s;k),\mu}_{\mathrm b;\mathrm b}$.

*Proof.* Put $f := N_{\mathrm{sf}}(\lambda)u$. *Away from $v = 0$.* On $\{v<-\frac14\}$, $f\in H^{s-1+k}$, and (2.4) and
propagation at order $s+k$ give $u\in H^{s+k}$ there (Proposition 2.4 (1) in the strong sense, which on $\{v<0\}$ uses
no radial estimate); on compact subsets of $\{v>0\}$, ellipticity gives $u\in H^{s+1+k}_{\mathrm{loc}}$; near $R = 0$,
I.C Lemma 2.5 gives $\chi_\partial u\in H^{s+k}_{\mathrm b,\mu}$. Each of these is the module regularity there (section
1.2). *Near $v = 0$.* Let $\chi\in C_c^\infty((-\frac12,2))$ equal 1 on $[-\frac14,1]$ and $u_0 := \chi u$; then
$N_{\mathrm{sf}}u_0 = \chi f+[N_{\mathrm{sf}},\chi]u$, and $[N_{\mathrm{sf}},\chi]u$ is supported where $u\in H^{s+k}$,
so $N_{\mathrm{sf}}u_0\in\dot H^{(s-1;k)}$ with support in $(-\frac12,2)\times\mathbb S^3$. We show by induction on
$j\le k$ that $W^\alpha u_0\in H^s$ for $|\alpha|\le j$. For $j = 0$ it is the hypothesis. Let it hold for $j-1$, and
let $U := (W^\alpha u_0)_{|\alpha| = j}$, a priori in $H^{s-1}$ (one factor of each word is a first-order operator on
$W^{\alpha'}u_0\in H^s$). By (2.12),
$$\big(N_{\mathrm{sf}}(\lambda)\otimes\mathrm{Id}+M\big)U = F,\qquad M :
 = (M_{\alpha\beta})_{|\alpha| = |\beta| = j},\quad F := \big(\tilde W^\alpha N_{\mathrm{sf}}u_0
-\textstyle\sum_{|\beta|<j}M'_{\alpha\beta}W^\beta u_0\big)_\alpha,$$
and $F\in H^{s-1}$: $\tilde W^\alpha N_{\mathrm{sf}}u_0\in H^{s-1}$, as $\tilde W^\alpha\in\mathcal D^j$, $j\le k$, and
$N_{\mathrm{sf}}u_0\in\dot H^{(s-1;k)}$; and in each term $D_1D_2W^\beta u_0$ of $M'_{\alpha\beta}W^\beta u_0$,
$D_2W^\beta\in\mathcal D^{j-1}$, so $D_2W^\beta u_0\in H^s$ by the induction hypothesis (section 2.4 with $k = j-1$),
and $D_1\in\mathcal D^1$ maps $H^s$ to $H^{s-1}$. $N_{\mathrm{sf}}\otimes\mathrm{Id}+M$ satisfies Lemma 2.2 (1) at
$\partial\mathcal R_\pm$, with the threshold of $N_{\mathrm{sf}}$ (the symbol of $M$ vanishes there); along $\Sigma_0$
over $\{-\frac12<v<0\}$, I.A Proposition 5.2 applies to it (principal symbol $p_2\,\mathrm{Id}$; $M$ enters
$P_I^{\mathrm{sub}}$, on which no sign is imposed), with control from $\{v<-\frac14\}$, where $U\in H^s$ by the first
step; and it is elliptic elsewhere over $\mathrm{supp}\,u_0$. The estimates in the strong sense, as in Proposition 2.4
(1), give $U\in H^s$. $\square$

## 3. Injectivity for $\mathrm{Re}\,\lambda<2$ ([Hin26] Proposition 9.2 (2), first half)

**Lemma 3.1 (conormality at the light cone).** Let $s\in\mathbb R$ with $s-\frac12\notin\mathbb Z$, and let
$u\in H^s(\mathbb R\times\mathbb S^3)$ be supported in $\{v\ge0\}$ near $\{v = 0\}$, with $W^\alpha u\in H^s$ near
$\{v = 0\}$ for every word $W^\alpha$. Then for every $\alpha$ there is $C$ with
$|W^\alpha u(v,\omega)|\le Cv^{s-\frac12}$ on $(0,1)\times\mathbb S^3$.

*Proof.* Localise with a cut-off in $v$, which commutes with the rotations and with $v\partial_v$ up to a smooth
compactly supported function. With $\mathcal F$ in $v$ and the expansion in spherical harmonics, $\|u\|^2_{H^s} =
\int\sum_k(1+\xi^2+\kappa_k)^s|\hat u_k(\xi)|^2d\xi\ge\|u\|^2_{H^s(\mathbb R;L^2(\mathbb S^3))}$ for $s\ge0$, and the
same applied to $\Omega^\gamma u$, $|\gamma|\le m$, gives $u\in H^s(\mathbb R;H^m(\mathbb S^3))$ for every $m$, likewise
each $W^\alpha u$. Let $\mathcal H := H^m(\mathbb S^3)$ with $m\ge2$, so $\mathcal H\subset C^0(\mathbb S^3)$. Write
$s = k_0+\frac12+\theta$, $k_0\in\mathbb N_0$, $\theta\in(0,1)$. For $g\in H^s(\mathbb R;\mathcal H)$:
$g^{(k_0)}\in H^{\frac12+\theta}(\mathbb R;\mathcal H)$, and
$\|g^{(k_0)}(x)-g^{(k_0)}(y)\|_{\mathcal H}\le C|x-y|^\theta\|g\|_{H^s}$, since by Fourier inversion and Cauchy-Schwarz
this difference is at most $(2\pi)^{-1}\|\langle\tau\rangle^{\frac12+\theta}\widehat{g^{(k_0)}}\|_{L^2}$ times
$\big(\int\min(4,|x-y|^2\tau^2)\langle\tau\rangle^{-1-2\theta}d\tau\big)^{1/2}$, and the integral is at most
$C|x-y|^{2\theta}$ (split at $|\tau| = |x-y|^{-1}$; $0<\theta<1$); and $g^{(i)}$, $i\le k_0$, are continuous. If $g$ is
supported in $\{v\ge0\}$, then $g^{(i)}(0) = 0$ for $i\le k_0$, and Taylor's formula gives
$\|g(v)\|_{\mathcal H}\le Cv^{k_0+\theta} = Cv^{s-\frac12}$ for $v\in(0,1)$. Apply this to $g = W^\alpha u$; this proves
the case $s>\frac12$. For $s<0$ the first step uses $(1+\xi^2)^s\le(1+\xi^2+\kappa_k)^s(1+\kappa_k)^{-s}$ instead, at
the cost of $\lceil-s\rceil$ more rotations. *The case $s<\frac12$.* Let $j\in\mathbb N$ with $s+j>\frac12$, and let $I$
be the primitive in $v$ vanishing on $\{v<0\}$, cut off beyond the support. It maps $H^\sigma(\mathbb R;\mathcal H)$ to
$H^{\sigma+1}(\mathbb R;\mathcal H)$ for compactly supported elements, satisfies $v\partial_vI = I(v\partial_v+1)$, and
commutes with the rotations. So $U := I^ju$ satisfies the hypotheses at order $s+j$, and the case $s>\frac12$ gives
$|W^\alpha U|\le Cv^{s+j-\frac12}$. On $(0,1)$, $u = \partial_v^jU = v^{-j}\prod_{i=0}^{j-1}(v\partial_v-i)U$, and
$W^\alpha v^{-j} = v^{-j}W^\alpha_{(-j)}$, so $|W^\alpha u|\le Cv^{s-\frac12}$. (Written out, with the number of words
counted, in III.G$'$ Lemma 2.1; for $s>\frac12$ only before D238.) $\square$

**Proposition 3.2 (injectivity).** Let $\mathrm{Re}\,\lambda<2$ and $(s,\mu)$ admissible. Then
$N_{\mathrm{sf}}(\lambda):\mathcal X\to\mathcal Y$ is injective.

*Proof.* Let $u\in\mathcal X$, $N_{\mathrm{sf}}(\lambda)u = 0$. By Proposition 2.4 (3) we may change $(s,\mu)$: take
$s\in(\max(-\frac12,\frac12-\mathrm{Re}\,\lambda),2-\mathrm{Re}\,\lambda)$, possible as $\mathrm{Re}\,\lambda<2$, with
$s-\frac12\notin\mathbb Z$, and $\mu\in(\mathrm{Re}\,\lambda-1,\mathrm{Re}\,\lambda)$. Put $a_0 := s-\frac12>-1$, so
$a_0+\mathrm{Re}\,\lambda>0$.

*Step 1: support and regularity.* By Proposition 2.7, $u\in\dot H^{(s;\infty),\mu}_{\mathrm b;\mathrm b}$. On
$\{-1<v<0\}$, $u$ solves $N_{\mathrm{sf}}(\lambda)u = 0$, is supported in $\{v\ge-1\}$, and $v$ is a time function
there: by the uniqueness step of I.A Proposition 6.4 on the slabs $\{-1-\epsilon'<v<-\epsilon\}$ (Lemma 2.3), $u = 0$ on
$\{v<-\epsilon\}$ for every $\epsilon>0$. So $u$ is supported in $\{v\ge0\}$. It is smooth on $\{v>0\}$ (elliptic),
satisfies $|W^\alpha u|\le Cv^{a_0}$ on $(0,1)$ by Lemma 3.1, and
$|W^\alpha u|\le Cv^{-(\mathrm{Re}\,\lambda-\epsilon)}$ on $\{v\ge\frac12\}$ for every $\epsilon>0$ by Proposition 2.4
(3) ($u\in\mathcal A^{\mathrm{Re}\,\lambda-\epsilon}$ near $R = 0$, $R = v^{-1}$, the b-fields being
$v\partial_v = -R\partial_R$ and the rotations).

*Step 2: the Fourier transform.* $u$ is the extension by zero of $u|_{\{v>0\}}$. Let $\varphi$ be smooth with compact
support and $\chi\in C^\infty_c(\mathbb R)$ equal to 1 near 0. Then $\langle u,\varphi\chi(\cdot/\epsilon)\rangle\to0$
as $\epsilon\to0$, since $\|\varphi\chi(\cdot/\epsilon)\|_{H^{-s}} = O(\epsilon^{\min(\frac12,\frac12+s)})$ and
$s>-\frac12$; and $\langle u,\varphi(1-\chi(\cdot/\epsilon))\rangle\to\int_{v>0}u\varphi$ by dominated convergence
($|u|\le Cv^{a_0}$, $a_0>-1$). So II.F Lemma 5.7 (for $a>-1$, as amended at D238) applies to $f := u|_{\{v>0\}}$, with
$a := a_0$ and its exponent $\lambda$ there equal to $\mathrm{Re}\,\lambda-\epsilon$. The equation holds across $v = 0$
by hypothesis, so the Green's formula step of II.F Lemma 5.8 is not needed. So
$\hat u(\hat r,\omega) := \int e^{i\hat rv}u\,dv$ is smooth on $\{\hat r\ne0\}$ with
$$|(\hat r\partial_{\hat r})^j\partial^\alpha_\omega\hat u|\le C(1
+|\hat r|)^{-1-a_0}\Big(\frac{|\hat r|}{1+|\hat r|}\Big)^{\min(\mathrm{Re}\,\lambda-1-\epsilon,0)-\epsilon}.$$
By Lemma 1.2 (c), $N_{\mathrm{sf}}(\lambda)$ is II.F's $N^1(\sigma)$ of (5.11) at $i\sigma = \lambda$, with
$c = \frac32$, $S_0 = \bar S$ and $P^{(0)}(0) = \tilde L(0)$. So, as in II.F (5.12)-(5.13) (`sf5.py` S8, with a failing
control), $w^\flat_\pm(\hat r,\omega) := \hat r^{1-\lambda}\hat u(\pm\hat r,\omega)$, $\hat r>0$, satisfy
$N_{\mathrm{tf}}(\pm1)w^\flat_\pm = 0$ on $\mathrm{tf}^\circ$, with $N_{\mathrm{tf}}$ of I.C (4.1) for these data, which
is $N_{\mathrm{tf}}(\widehat{2L_b},\pm1)$ (III.F$'$ section 3).

*Step 3: the weights.* As $|\hat r^{1-\lambda}| = \hat r^{1-\mathrm{Re}\,\lambda}$ is conormal,
$$w^\flat_\pm\in\mathcal A^{a_0+\mathrm{Re}\,\lambda,\,-\beta}(\mathrm{tf}),\qquad\beta :
 = \max(2\epsilon,\mathrm{Re}\,\lambda-1+2\epsilon),\tag{3.1}$$
in I.C's notation ($\rho_{\mathrm{sctf}}$ first): at $\hat r\to\infty$ the exponent is $-1-a_0+1-\mathrm{Re}\,\lambda$,
at $\hat r\to0$ it is $1-\mathrm{Re}\,\lambda+\min(\mathrm{Re}\,\lambda-1-\epsilon,0)-\epsilon\ge-\beta$. Take
$\epsilon$ so small that $\beta<1$ (possible as $\mathrm{Re}\,\lambda<2$); then $\beta\in(0,1)$.

*Step 4: tf-admissibility.* By III.F$'$ Proposition 3.3, $\widehat{L_b}$ is tf-admissible with every weight in $(0,1]$.
Fix $\beta^*\in(\beta,1]$ and $q := 2-\beta^*$, and in the spaces of I.C section 4.3 take orders $\mathsf r_\pm$
admissible as there whose value near $R_{\mathrm{out}}$, the zero section over sctf, is below
$a_0+\mathrm{Re}\,\lambda-2$ (admissibility imposes only an upper bound there, I.A Lemma 7.1). Then
$w^\flat_+\in\mathcal X_{\mathrm{tf},0}$ and $w^\flat_-\in\mathcal X_{\mathrm{tf},\pi}$, exactly as in II.F Lemma 5.8
(*tf-admissibility*), with $\gamma_I$ there replaced by $a_0+\mathrm{Re}\,\lambda>0$: near sctf by I.A Lemma 7.4 (a),
near ztf as $\mathcal A^{-\beta}\subset H^\infty_{\mathrm b,q-2}$ (I.C Lemma 2.2 (f)), smooth in between. By I.C
Corollary 5.2 (a), $N_{\mathrm{tf}}(e^{i\theta})$ is invertible on these spaces at $\theta = 0,\pi$, so
$w^\flat_\pm = 0$ and $\hat u = 0$ on $\{\hat r\ne0\}$.

*Step 5.* As in II.F Lemma 5.8 (*Conclusion*): for $\psi\in C^\infty(\mathbb S^3;\mathbb C^{15})$,
$\langle\hat u,\psi\rangle$ is supported in $\{0\}$, so $\langle u,\psi\rangle$ is a polynomial in $v$, vanishing for
$v<0$; so $u = 0$. $\square$

At $n = 3$ the source obtains this for $\mathrm{Re}\,\lambda<1+\epsilon_{\mathrm{ind}}$; its bound comes from the
tf-weights, which there must lie in $(0,\epsilon_{\mathrm{ind}})$. At $n = 4$ the gap $(0,1]$ and the tf-admissibility
on all of it leave as the one constraint the tf weight $\beta<1$ of Step 3, i.e. $\mathrm{Re}\,\lambda<2$ (finding
(G2)).

## 4. High frequencies: the semiclassical estimate ([Hin26] (9.9) at $n = 4$)

### 4.1 The family

Fix $C_\lambda\ge1$. For $\lambda$ with $|\mathrm{Re}\,\lambda|\le C_\lambda$ and $|\mathrm{Im}\,\lambda|\ge1$ put
$\sigma := -i\lambda$, $h := |\mathrm{Im}\,\lambda|^{-1}$ and $z := h\sigma = \pm1+iy$, $y = -h\,\mathrm{Re}\,\lambda$,
$\pm = \mathrm{sgn}\,\mathrm{Im}\,\lambda$; so $z\in\mathcal Z_{h} := \{\pm1+iy:|y|\le C_\lambda h\}$ and
$\lambda = iz/h$. As in the source, let $\tilde R\in C^\infty((0,\infty))$ with $\tilde R(R) = R$ for $R<\frac12$,
$\tilde R\ge\frac12$ on $[\frac12,1]$, $\tilde R = 1$ for $R\ge1$, and
$$N_h := \tilde R^{-\lambda}\tilde R^{-2}N_{\mathrm{sf}}(\lambda)\tilde R^{\lambda},\qquad P := P_{h,z} :
 = h^2N_h.\tag{4.1}$$
By Lemma 1.2 (c), on $\{R<\frac12\}$, $P = h^2N^0(h^{-1}z) = P_{\iota,h,z}$ of II.F (1.11)-(1.12) for $P_0 = 2L_b$; on
$\{R\ge1\}$ ($v\le1$), $P = h^2N_{\mathrm{sf}}(\lambda)$. On $\{\frac12\le R\le1\}$ conjugation by
$\tilde R^\lambda = e^{\frac izh\log\tilde R}$ is the semiclassical conjugation by $e^{i\phi/h}$,
$\phi := z\log\tilde R$: it translates the fibres by $(\mathrm{Re}\,z)\,d\log\tilde R$ and multiplies by
$\tilde R^{-\mathrm{Re}\,\lambda}$, a smooth function bounded above and below, with $O(y/h)$ derivatives.

*The spaces.* On $\{R<\frac12\}$ the spaces of II.F section 3.1,
$H^{(\mathsf s';\cdot,\gamma_{\mathrm{cf}},\gamma_{\mathrm{cf}};\mathsf b)}$, for functions supported in $\{R<\frac12\}$
(the weight at 0f does not enter); on $\{v<4\}$ the semiclassical Sobolev spaces $H^{s,\mathsf b}_h$ of I.B section 2
(differential order $s$, constant, and semiclassical order $\mathsf b$, a function on phase space), supported at
$v = -1$. With a partition of unity in $v$, these define $\mathcal H_{\mathbf o}$,
$\mathbf o := (s;\gamma_{\mathrm{cf}},\gamma_{\mathrm{cf}};\mathsf b)$, and $\mathcal Y_{\mathbf o} := \mathcal
H_{(s-1;\gamma_{\mathrm{cf}}-2,\gamma_{\mathrm{cf}};\mathsf b+1)}$; on $\{\frac14<R<1\}$ II.F's spaces are the
semiclassical ones of the interior ($h\mathcal V(\iota^+)$, II.F section 2.1), so the two descriptions agree there,
uniformly in $h$. The differential order of II.F's spaces is chosen equal to $s$ on $\{R>\frac14\}$, which is allowed,
$P$ being elliptic at fibre infinity over $\{R<\frac12\}$ (II.F section 3.1). The weight $\gamma_{\mathrm{cf}}\in(-1,0)$
is fixed; $\alpha_+ := -\gamma_{\mathrm{cf}}-2$, so $\alpha_++2\in(0,1)$ is a weight with which $P_0 = 2L_b$ is
tf-admissible (III.F$'$ Proposition 3.3).

For fixed $h$, $\mathcal H_{\mathbf o}$ is $\dot H^{s,\gamma_{\mathrm{cf}}}_{\mathrm b}$ with an equivalent norm (II.F
section 2.1), and $u\mapsto\tilde R^{\lambda}u$ maps it onto
$\dot H^{s,\gamma_{\mathrm{cf}}+\mathrm{Re}\,\lambda}_{\mathrm b}$ ($|\tilde R^\lambda| = R^{\mathrm{Re}\,\lambda}$ near
$R = 0$; $R\partial_R\tilde R^{i\mathrm{Im}\lambda}$ is bounded); with
$N_{\mathrm{sf}}(\lambda) = \tilde R^{2+\lambda}N_h\tilde R^{-\lambda}$, the weight of the target matches:
$(\gamma_{\mathrm{cf}}-2)+2+\mathrm{Re}\,\lambda$.

### 4.2 Symbols and dynamics across the light cone

**Lemma 4.1 (symbols and dynamics).** On $\{v<4\}$:

(a) The principal symbol of $P$ is $p_z := (v\xi+z)((v+2)\xi+z)+|\eta|^2$ on $\{R\ge1\}$ ($v\le1$), and on
$\{\frac12\le R\le1\}$ the transport of $\tilde R^{-2}p_z$ by the fibre translation of section 4.1;
$\mathrm{Re}\,p_z = p_{\pm1}+O(y^2)$ and $\mathrm{Im}\,p_z = 2y((v+1)\xi\pm1)$, so $h^{-1}\mathrm{Im}\,P$ is a
semiclassical operator of first order with coefficients bounded by $C_\lambda$: in I.B's (1.3), $\lambda = 0$ and every
imaginary term is part of $\mathcal P_1$ (I.B Remark 4.7 (a), which holds also at fibre infinity over this compact
region, where $\lambda\mathcal Q$ and $\mathcal P_1$ have the same order). (*Computed:* `sf5.py` S6.)

(b) Let $z_0 = 1$ and $p := p_1$. With $\tilde\xi := -(v+2)(v\xi+1)$, $H_p\tilde\xi = 2(v+1)(|\eta|^2-p)$ and
$H_p|\eta|^2 = 0$. On $\Sigma := \{p = 0\}$ (finite frequencies), $\xi\ne0$, and $\tilde\xi$ is non-decreasing along
$H_p$ over $\{v>-1\}$, strictly where $\eta\ne0$; on $\Sigma\cap\{\eta = 0\}$ over $\{v>0\}$, $\tilde\xi\in\{-2,0\}$.

(c) $\Sigma = \Sigma_+\cup\Sigma_-$, $\pm\xi>0$. With $w := v+1$ and $t := |\xi|$, $L := |\eta|$ (constant along the
flow): $\Sigma_+$ lies over $\{-1-\delta_1\le v<0\}$ for small $\delta_1>0$, with $\xi\ge-1/v$ there and $H_pv\le-2$ on
$\{-1<v<0\}$ (negative on $[-1-\delta_1,-1]$); $\Sigma_-$ over $\{-1-\delta_1\le v\le0\}$ has $H_pv>0$ and
$t = [-w+(1+L^2(1-w^2))^{1/2}]/(1-w^2)$, bounded by a constant depending on $L$ (with the limit $(1+L^2)/2$ at $v = 0$);
over $\{v>0\}$, $\Sigma_-$ lies in $\{\frac1{v+2}\le t\le\frac1v\}\cap\{w^2\le1+L^{-2}\}$, so for $L>0$ in
$\{v\le v_{\max}(L) := (1+L^{-2})^{1/2}-1\}$.

(d) Every maximal integral curve of $H_p$ in $\Sigma$ over $\{v<4\}$ is one of: (i) a curve in $\Sigma_+$, which tends
to $\partial\mathcal R_+$ at fibre infinity backwards (with $v\uparrow0$, $t\to\infty$) and reaches $\{v<-1\}$ forwards;
(ii) a curve in $\Sigma_-$ with $L>0$, which comes from $\{v<-1\}$, crosses $\{v = 0\}$ at $t = (1+L^2)/2$, has one
turning point of $v$, and tends to $\partial\mathcal R_-$ at fibre infinity forwards, with $v\downarrow0$ and
$t\to\infty$ (if $v_{\max}(L)\ge4$, part of it lies in $\{R<\frac14\}$, where II.F's description applies); (iii) the
incoming ray $\{\eta = 0,\ \xi = -\frac1{v+2}\}$, from $\{v<-1\}$ to the cone point ($v\to\infty$; in II.F's coordinates
it tends to $R_{\mathrm{cf},1,\mathrm{in}}$), and the outgoing ray $\{\eta = 0,\ \xi = -\frac1v\}$ over $\{v>0\}$, from
the cone point ($R_{\mathrm{cf},\mathrm{out}}$) to $\partial\mathcal R_-$.

(e) In II.F's coordinates over $\{R<\frac12\}$ ($R = v^{-1}$ and, for $z = 1$, $\xi_{c\hbar} = -v(v\xi+1)$,
$\eta_{c\hbar} = v\eta$ under the conjugation), the symbol of $P$ is II.F (1.13), $G_{\iota,1} = v^2p$, and
$\tilde\xi = (1+2R)\xi_{c\hbar}$; with II.F (3.12)'s field, $\mathsf H\tilde\xi = -2(1+R)\xi_{c\hbar}(\tilde\xi+2)\ge0$
on $\{G_{\iota,1} = 0\}$ over sf, with equality only at $\xi_{c\hbar} = 0$ and at $\tilde\xi = -2$. The future flow of
II.F (its $\varsigma = +1$) is the flow of $H_p$, up to a positive factor.

(f) For $z_0 = -1$ everything holds after $(\xi,\eta)\mapsto(-\xi,-\eta)$ with the flow reversed, as
$p_{-z}(v,\omega;-\xi,-\eta) = p_z(v,\omega;\xi,\eta)$ (II.F section 3.2, *Symmetry*).

*Proof.* (a) The principal symbol of $h^2N_{\mathrm{sf}}(iz/h)$ is obtained from (1.3) with $h\partial_v\mapsto i\xi$,
$h\lambda = iz$, $h^2\Delta_{\mathbb S^3}\mapsto|\eta|^2$ (`sf5.py` S6); the transport is that of the conjugation.
$\mathrm{Im}\,p_z$ is computed from $(v\xi+z)((v+2)\xi+z)$ with $z = \pm1+iy$; $|y|\le C_\lambda h$. (b) `sf5.py` S6
computes $H_p\tilde\xi$; $H_p|\eta|^2 = \{p,|\eta|^2\} = 0$ as in Lemma 2.1 (b). If $\xi = 0$ then $p = 1+|\eta|^2>0$.
On $\Sigma$, $H_p\tilde\xi = 2(v+1)|\eta|^2$. With $a := v\xi+1$, $b := (v+2)\xi+1$, $p = ab+|\eta|^2$; $\eta = 0$
forces $a = 0$ ($\tilde\xi = 0$) or $b = 0$ ($\xi = -\frac1{v+2}$, $a = \frac2{v+2}$, $\tilde\xi = -2$). (c) With
$k := w\xi+1$, $a = k-\xi$, $b = k+\xi$, so $p = k^2-\xi^2+|\eta|^2$; $H_pv = \partial_\xi p = 2(v(v+2)\xi+v+1)$ and
$H_p\xi = -2\xi k$. On $\Sigma_+$ over $\{v\ge-1\}$, $k\ge1$ and $\xi^2\ge k^2$ give $\xi\ge w\xi+1$, so $v<0$ and
$\xi\ge-1/v$, whence $v(v+2)\xi\le-(v+2)$ and $H_pv\le-2$; near $v = -1$ the same expression is negative by continuity.
On $\Sigma_-$ ($\xi = -t$) over $[-1,0]$, $H_pv = 2(w+(1-w^2)t)>0$ (at $w = 0$ it is $2t>0$), and near $v = -1$ by
continuity; the formula for $t$ is the positive root of $(1-w^2)t^2+2wt-(1+L^2) = 0$, which is $p = 0$ in these
variables. Over $v>0$: $t\ge|1-wt|$ gives $\frac1{v+2}\le t\le\frac1v$, and real roots of the same quadratic need
$1+L^2(1-w^2)\ge0$. (d) Along a curve, $L$ is constant and, by (b), $\tilde\xi$ is monotone. (i) and the first half of
(ii) follow from the signs of $H_pv$ in (c); on $\Sigma_-$ over $\{v>0\}$ with $L>0$ the curve stays in the compact set
$\{0<v\le v_{\max}(L)\}$ while $t$ stays bounded, and $\tilde\xi$ increases strictly; it cannot stay in a compact subset
of $\{v>0\}$ at bounded $t$ for all time (on it $H_p\tilde\xi\ge c>0$, and $\tilde\xi$ is bounded there), so it leaves
through $v\to0$; there the only points of $\Sigma_-$ are at $t\le\frac1v\to\infty$ with $a = 1-vt\to0$ (the branch
$t\ge\frac1{v+2}$ near $t = \frac1{v+2}$ lies over $v<0$ backwards, by the sign of $H_pv$ there, and is the incoming
part); in rescaled coordinates $(\rho_\infty,v,\hat\eta) = (t^{-1},v,\eta/t)\to(0,0,0)$, i.e. to $\partial\mathcal R_-$.
The turning point is unique: at a critical point of $v$ on $\Sigma$ over $\{v>0\}$, $H_p^2v = -4(v+1)/(v(v+2))<0$
(`sf5.py` S11), so every critical point is a strict maximum, and there is at most one. (iii) On $\{\eta = 0\}$, $\Sigma$
is the two curves named; on the first $H_pv = 2$ and on the second $H_pv = -2$; II.F section 1.3 identifies their limits
at $R = 0$. (e) `sf5.py` S7 (with a failing control): the identities under $\xi_{c\hbar} = -v(v\xi+1)$,
$\eta_{c\hbar} = v\eta$, and the computation of $\mathsf H\tilde\xi$ from II.F (3.12) on $\{G_{\iota,1} = 0\}$. The
correspondence is the conjugation of section 4.1 on $\{R<\frac12\}$ ($\tilde R = R$, $\phi = \log R$, $d\phi = -dv/v$,
the translation by $d\log R$ at $z = 1$: the covector $\zeta$ of $h^2N^0$ corresponds to $\xi = \zeta_v-\frac1v$ of $P$,
so $\zeta_v = \xi+\frac1v$, whose $dR$-component is $-v^2\zeta_v = -v(v\xi+1) = \xi_{c\hbar}$, and
$\eta_{c\hbar} = R^{-1}\eta = v\eta$): it carries $p$ to $R^{-2}\cdot$ (the symbol of $h^2N^0$), i.e.
$v^2p = G_{\iota,1}$, and preserves $H_p$ up to the factor $v^2>0$ on $\Sigma$. (f) Complex conjugation of the
coefficients exchanges $z_0 = 1$ and $z_0 = -1$; the symbol identity is immediate. $\square$

The function $\tilde\xi$ is the escape function of the problem: it increases along every bicharacteristic that is not
one of the two rays through the cone point, and on those it is $-2$ and $0$; through the cone point it rises from $-2$
to $0$ along the curves of II.F's face $F_K$.

**Lemma 4.2 (the semiclassical order).** Let $b_{\mathrm{in}}>b_{\mathrm{out}}$ with
$b_{\mathrm{in}}+\alpha_+>\frac12(-1+\vartheta_{\mathrm{in}})$ and
$b_{\mathrm{out}}+\alpha_+<-\frac12+\bar S-\epsilon_0$ ($\bar S = \min\mathrm{spec}\,\bar S = 0$, $\epsilon_0>0$ small),
the thresholds (1.17) of II.F at $R_{\mathrm{cf},1,\mathrm{in}}$ and $R_{\mathrm{cf},\mathrm{out}}$. Let
$f_1\in C^\infty(\mathbb R)$ be non-increasing, $f_1 = 1$ on $(-\infty,-2+\delta']$, $f_1 = 0$ on $[-\delta',\infty)$;
$f_2\in C^\infty_c(\mathbb R)$, $0\le f_2\le1$, $f_2 = 1$ on $[0,L_0^2]$, $f_2 = 0$ on $[4L_0^2,\infty)$; and $\psi$ a
smooth compactly supported function on the finite-frequency semiclassical phase space over sf (including II.F's faces
over $R = 0$), with $0\le\psi\le1$, equal to 1 on a neighbourhood of
$K := \Sigma\cap\mathrm{supp}(f_1(\tilde\xi)f_2(|\eta|^2))$, which is compact; and $g\in C^\infty(\mathbb R)$
non-increasing, $g = 1$ on $(-\infty,-\frac14]$, $g = 0$ on $[-\frac18,\infty)$. Here $\tilde\xi$, $|\eta|^2$ and the
functions below are defined in $N_{\mathrm{sf}}$'s frame over $\{v<4\}$, pulled back to the frame of $P$ on
$\{\frac12\le R\le1\}$ by the fibre translation of section 4.1, and over $\{R<\frac12\}$ expressed in II.F's variables
(Lemma 4.1 (e)). Put
$$\mathsf b := b_{\mathrm{out}}+(b_{\mathrm{in}}-b_{\mathrm{out}})\big(1-(1-g(v))(1-\Phi)\big),\qquad
\Phi := \psi\,f_1(\tilde\xi)\,f_2(|\eta|^2)\qquad(z_0 = 1),\tag{4.2}$$
and the reflection for $z_0 = -1$. Then $\mathsf b$ is smooth; equal to the constant $b_{\mathrm{in}}$ over
$\{v\le-\frac14\}$ at all frequencies; equal to $b_{\mathrm{out}}$ near fibre infinity over $\{v\ge-\frac18\}$ and near
$R_{\mathrm{cf},\mathrm{out}}$; equal to $b_{\mathrm{in}}$ near $R_{\mathrm{cf},1,\mathrm{in}}$; and, on a neighbourhood
of $\Sigma$, non-increasing in the directions of propagation of Proposition 4.6. These are: along $H_p$ (II.F's future
flow) on $\Sigma_-$ and over $\{v>0\}$; and in the direction of increasing $v$ on $\Sigma_+$ over $\{v\le0\}$ (backward
along $H_p$) and at fibre infinity over $\{-1<v<0\}$. (Before D238, (4.2) had no factor $g$, and $\mathsf b$ varied over
the slab where Lemma 4.4's constant-order estimate is used; the ninety-eighth verifier's A1.) Its restriction to II.F's
face $F_K$ is a decay order admissible at $\sigma_0 = \pm1$ with weight $\alpha_+$ in the sense of I.A section 1.4, as
II.F Lemma 3.5 requires of $\mathsf b_\flat|_{F_K}$.

*Proof.* *Compactness of $K$.* In the cone region $\Sigma$ is compact over sf (II.F section 1.3:
$|\xi_{c\hbar}|,|\eta_{c\hbar}|$ bounded on $G_{\iota,1} = 0$). Over $\{v\le0\}$, $f_1\ne0$ excludes $\Sigma_+$ (there
$a\le0$, so $\tilde\xi\ge0$), and on $\Sigma_-$ with $L\le2L_0$ Lemma 4.1 (c) bounds $t$. Over $\{0<v\le1\}$, on
$\Sigma_-$ write $c := vt\in[0,1]$, so $a = 1-c$ and $|\eta|^2 = t^2-(1-t-c)^2 = (1-c)(2t-1+c)$; $f_1(\tilde\xi)\ne0$
gives $(v+2)(1-c)\ge\delta'$, so $1-c\ge\delta'/3$ and $|\eta|^2\ge\frac{\delta'}3(2t-1)$, and $f_2\ne0$ bounds $t$.
Over $\{1\le v<4\}$, $t\le\frac1v\le1$. *Values.* Near fibre infinity $\psi = 0$. Near $R_{\mathrm{cf},\mathrm{out}}$,
$\tilde\xi = (1+2R)\xi_{c\hbar}$ is near 0, so $f_1 = 0$. Near $R_{\mathrm{cf},1,\mathrm{in}}$, $\tilde\xi$ is near $-2$
and $|\eta|^2 = R^2|\eta_{c\hbar}|^2$ near 0, and $\psi = 1$, so $\mathsf b = b_{\mathrm{in}}$. *The factor $g$.* Over
$\{v\le-\frac14\}$, $g = 1$ and $\mathsf b = b_{\mathrm{in}}$. Over $\{v\ge-\frac18\}$, $g = 0$ and
$\mathsf b = b_{\mathrm{out}}+(b_{\mathrm{in}}-b_{\mathrm{out}})\Phi$, treated below. Near fibre infinity $\Phi = 0$
($\psi = 0$), and on a neighbourhood of $\Sigma_+\cap\{v\le0\}$, $\Phi = 0$ ($\tilde\xi\ge0$ there, so $f_1 = 0$ on
$\{\tilde\xi>-\delta'\}$). There $\mathsf b = b_{\mathrm{out}}+(b_{\mathrm{in}}-b_{\mathrm{out}})g(v)$ is non-increasing
in $v$. On a neighbourhood of $\Sigma_-$ over $\{-\frac14<v<-\frac18\}$, $H_pv>0$ (Lemma 4.1 (c)), and
$H_p\big(1-(1-g)(1-\Phi)\big) = g'(v)(H_pv)(1-\Phi)+(1-g)H_p\Phi\le0$, as $g'\le0$, $0\le\Phi\le1$, and $H_p\Phi\le0$
(below). *Monotonicity of $\Phi$.* $H_p\Phi = \psi f_2f_1'(\tilde\xi)H_p\tilde\xi+f_1f_2H_p\psi$, as $H_p|\eta|^2 = 0$
identically on $\{v<4\}$ (Lemma 4.1 (b)) and, in the cone region,
$\{G_{\iota,1},R^2|\eta_{c\hbar}|^2\} = \{v^2p,|\eta|^2\} = 0$ likewise. The second term vanishes on a neighbourhood of
$\Sigma$: $\mathrm{supp}\,d\psi\cap\mathrm{supp}(f_1(\tilde\xi)f_2(|\eta|^2))$ is compact, as $\psi$ has compact
support, and does not meet $\Sigma$, as $\psi = 1$ near $K$. For the first, $f_1'\le0$, and $H_p\tilde\xi>0$ on
$K' := \Sigma\cap\mathrm{supp}\,f_1'(\tilde\xi)\cap\mathrm{supp}\,f_2(|\eta|^2)$, compact: over $\{v<4\}$ by Lemma 4.1
(b), as $\eta\ne0$ on $K'$ ($\tilde\xi\in[-2+\delta',-\delta']$ there, and $\tilde\xi\in\{-2,0\}$ where $\eta = 0$,
Lemma 4.1 (b)); over the cone region by Lemma 4.1 (e), as $-\xi_{c\hbar} = -\tilde\xi/(1+2R)\ge\delta'/(1+2R)$ and
$\tilde\xi+2\ge\delta'$, so $\mathsf H\tilde\xi\ge2\delta'^2/(1+2R)$. By continuity $H_p\tilde\xi>0$ on a neighbourhood
$O'$ of $K'$. The compact set
$\mathrm{supp}\,\psi\cap\mathrm{supp}\,f_1'(\tilde\xi)\cap\mathrm{supp}\,f_2(|\eta|^2)\setminus O'$ does not meet
$\Sigma$, so on a neighbourhood of $\Sigma$ the first term is $\le0$. *The face $F_K$.* At $R = 0$, $|\eta|^2 = 0$, and
on a neighbourhood of $\Sigma\cap F_K$, $\psi = 1$, so
$\mathsf b = b_{\mathrm{out}}+(b_{\mathrm{in}}-b_{\mathrm{out}})f_1(\xi_{c\hbar})$: non-increasing along the boundary
flow on a neighbourhood of $\Sigma\cap F_K$, since at $R = 0$, $\mathsf H\xi_{c\hbar} = 2|\eta_{c\hbar}|^2\ge0$
everywhere (II.F (3.12)), as I.B (4.4) requires ($g = 0$ there) and constant near $R_{\mathrm{in}}$
($\xi_{c\hbar} = -2$) and $R_{\mathrm{out}}$ ($\xi_{c\hbar} = 0$), with the thresholds there, which are those of (1.17)
at $F_K$ (II.F Lemma 3.5, *The order*). $\square$

### 4.3 The estimates

**Lemma 4.3 (the semiclassical radial estimate at the light cone).** Let $\delta>0$, $h$ as in Lemma 1.4,
$s<2-\delta-C_\lambda$ constant and $\mathsf b$ as in Lemma 4.2. For each sign there are neighbourhoods $U_*\subset U_0$
of $\partial\mathcal R_\pm$ at fibre infinity and a compact $K_E\subset\bar U_0\setminus\partial\mathcal R_\pm$ such
that, uniformly for $z\in\mathcal Z_h$, $h<h_0$, with $B_*$ microsupported in $U_*$, $G$ elliptic on $\bar U_0$, $E'$
elliptic on $K_E$, and all $N_1$, $K$:
$$\|B_*u\|_{\mathbf o}\le C\big(h^{-1}\|GPu\|_{\mathbf o-(1,1,0)}+\|E'u\|_{\mathbf o}+h^{N_1}\|Gu\|_{\mathbf o}
+\|u\|_{-K\mathbf 1}\big),\qquad\mathbf o = (s,\mathsf b),\tag{4.3}$$
$$\|B_*v\|_{\mathbf o^*}\le C\big(h^{-1}\|GP^{*h}v\|_{\mathbf o^*-(1,1,0)}+h^{N_1}\|Gv\|_{\mathbf o^*}
+\|v\|_{-K\mathbf 1}\big),\qquad\mathbf o^* = (1-s,\mathsf b^*),\tag{4.4}$$
for any $\mathsf b^*$ constant near $\partial\mathcal R_\pm$ (in I.B's notation for orders, the decay order being
immaterial).

*Proof.* I.B Lemma 5.1 with $F$ fibre infinity, $\Lambda := \partial\mathcal R_\pm$. (i): $\mathrm{Re}_hP$ has principal
symbol $p_{\pm1}$ up to terms in the class of $\mathcal P_1$ (Lemma 4.1 (a)), and with $\mu := |\xi|$,
$\mathsf H^{\mathbf P} := \mu^{-1}H_{p_{\pm1}}$ vanishes on $\Lambda$ (Lemma 2.1 (b): $\Lambda$ consists of radial
points of the homogeneous part, and at fibre infinity the field is that of $p_2$); take
$\varsigma := -\mathrm{sgn}\,\xi$ for $P$ ($\epsilon_\flat = 1$), so that $\varsigma\mathsf H^{\mathbf P} = -\mathsf H$
near $\Lambda$ and $\beta_\varrho = -\beta_0 = -2(1+v)$: a sink; for $P^{*h}$ ($\epsilon_\flat = -1$),
$\varsigma := \mathrm{sgn}\,\xi$, a source. (ii): $\lambda := 0$, Lemma 4.1 (a). (iii): $g := \rho_\infty^2p_{\pm1}$,
$\phi := \tilde q$ of Lemma 2.1 (b); $\varsigma\mathsf H^{\mathbf P}\phi = \mp\mathsf H\tilde q+O(\rho_\infty)$, which
is (5.1) by Lemma 2.1 (b). (iv): $s$ is constant and $\mathsf b = b_{\mathrm{out}}$ near fibre infinity (Lemma 4.2).
(v): at fibre infinity $\mu^{-1}p_1 = \mathrm{sgn}\,\xi\,\big(3+2\,\mathrm{Re}_h\bar S-2\,\mathrm{Re}\,\lambda\big)$ by
(2.3), with $\mathrm{Re}\,\lambda = -y/h$: the term $-2\lambda h^2\partial_v = -2iz(h\partial_v)$ contributes
$2(y/h)\xi = -2(\mathrm{Re}\,\lambda)\xi$ to $\sigma(h^{-1}\mathrm{Im}_hP)$ and the large part $\mathrm{Re}\,z$ only to
$\mathrm{Re}_hP$, the remaining terms being as in Lemma 2.2. So for $P$, $\tilde\kappa = s-\frac12$,
$$\mathcal T = 2(s-\tfrac12)(-2(1+v))+2\big(3+2\,\mathrm{Re}_h\bar S-2\,\mathrm{Re}\,\lambda\big) = 4\big(2
+\mathrm{Re}_h\bar S-\mathrm{Re}\,\lambda-s\big)\ge4(2-\delta-C_\lambda-s)>0$$
at $\Lambda$ ($v = 0$); for $P^{*h}$ at $\mathbf o^*$, $\tilde\kappa = \frac12-s$ and $\epsilon_\flat = -1$, the same
condition, as in the proof of I.B Proposition 5.2. Lemma 5.1 gives (4.3) with the control term
($\delta_{\mathrm{sink}} = 1$) and (4.4) without it. $\square$

**Lemma 4.4 (semiclassical slab estimates).** I.B Propositions 7.1, 7.2 and Corollary 7.3 hold for
$P = h^2N_{\mathrm{sf}}(\lambda)$ on the slabs $\{a<-v<b\}$, $0<a<b<2$, for $z\in\mathcal Z_h$ and $h<h_0$, with $r$
replaced by $-v$, $t$ by $T$, and $g$ by $\hat g$ of Lemma 1.2 (g). In particular, with the cut-offs of Lemma 2.3,
$$\|u\|_{H^s_h(\{-1<v<-1/4\})}
 \le Ch^{-1}\|Pu\|_{H^{s-1}_h(\{-1<v<-1/4\})}\ \ (u\ \text{supported in}\ \{v\ge-1\}),\quad\|\chi v\|_{\bar H^{1-s}_h}
 \le C\big(h^{-1}\|P^{*h}v\|_{\bar H^{-s}_h}+\|\chi_1v\|_{H^{1-s}_h}\big).\tag{4.5}$$

*Proof.* By Lemma 1.2 (g), $N_{\mathrm{sf}}(\lambda) = \hat P_c(\sigma)$, $\sigma = -i\lambda = z/h$, for the stationary
operator $P_c$ on $M := \mathbb R_T\times\mathrm{sf}^\circ$ with metric $\hat g$, $P_c-\Box_{\hat g}$ of first order
with $T$-independent coefficients, and $dv$ timelike on the slab. The proof of I.B Proposition 7.1 uses (H6) only
through this, except at two places. First, it uses $\mathrm{Im}\,z\ge0$ and $T[u'](-\nabla t,X)\ge0$ to drop the term
$2h^{-1}(\mathrm{Im}\,z)T[u'](-\nabla t,X)$ of ${}^{(W)}K[u']$; here $\nabla T$ is spacelike, but
$|h^{-1}\mathrm{Im}\,z|\le C_\lambda$ and $|T[u'](\nabla T,X)|\le C|du'|^2_R$, so the term is bounded by $C'|du'|^2_R$
and absorbed by $\lambda T[u'](X,X)\ge\lambda c_0|du'|^2_R$ for $\lambda$ large. The flux identity $E(1) = E(0)$ uses
only the $T$-independence. Second, the adjoint estimate is obtained there by $t\mapsto-t$ to keep $\mathrm{Im}\,z\ge0$;
here the first argument applies directly to $P^{*h}$, the spectral family at $\bar z/h$ of the formal adjoint of $P_c$
($|\mathrm{Im}\,\bar z|\le C_\lambda h$), with the ends of the slab exchanged (I.A Proposition 6.3's backward case, with
the weight $e^{-\lambda r}$), $X$ unchanged. The proof of I.B Proposition 7.2 uses I.A Proposition 6.4 (iii) at fixed
$h$ (Lemma 2.3), the monotonicity of $v$ along every characteristic point over the slab, at finite frequencies and at
fibre infinity ($H_{\hat G}v = 2\hat g^{-1}(\nu,dv)\ne0$ for $\hat g$-null $\nu\ne0$, $dv$ being timelike), and I.B
Corollary 4.6$'$, valid here by I.B Remark 4.7 (a) (Lemma 4.1 (a)); it does not use the statement for $\mathrm{Im}\,z>0$
that there is no characteristic point at finite frequencies, which serves only as an alternative there. Corollary 7.3
follows as there. $\square$

**Lemma 4.5 (the cone point).** On $\{R<\frac12\}$, II.F Propositions 2.4-2.6 and Lemma 3.3 (R3)-(R4) hold for $P$ with
$z\in\mathcal Z_h$ and the order $\mathsf b$ of Lemma 4.2, and II.F Lemmas 3.5-3.6 hold for $u$ supported in
$\{R<\frac12\}$, with the proofs given there and these changes: in (R3), for $0<y\le C_\lambda h$ the term $-yQ_1$ is
put into $\mathcal P_1$ as for $y\le0$ (its contribution $\varpi^{-1}(-y)\sigma(Q_1) = 2y\xi_{c\hbar}(1+\hat h)^2R/h$ is
bounded by $2C_\lambda R$ and vanishes at $R = 0$); in (R4) and in the propagation along $o_{\mathrm{sf}}$,
$\lambda\mathcal A$ with $|\lambda| = |\mathrm{Im}\,z|/|z|^2\le C_\lambda h$ is part of $\mathcal P_1$ for either sign
(its symbol vanishes at $R_{\mathrm{cf},\mathrm{out}}$); and in step (4) of the proof of II.F Lemma 3.6,
$|\mathrm{Im}\,z|\le C_\lambda h$ replaces $|\mathrm{Im}\,z|\le\gamma_+h$. The constants depend on $C_\lambda$.

*Proof.* The three places listed are the only ones where II.F's proofs use the range of $\mathrm{Im}\,z$ near the cone
point: elsewhere they use it only at $\mathscr I^+$ (the face $F_I$, (R1)-(R2)), which does not occur here ([Hin26]'s
footnote 86). The order $\mathsf b$ enters through (1.17) at $R_{\mathrm{cf},1,\mathrm{in}}$ and
$R_{\mathrm{cf},\mathrm{out}}$, constancy near them, monotonicity along the future flow, and its restriction to $F_K$ in
Lemma 3.5, all of which Lemma 4.2 provides. $P_0 = 2L_b$ is tf-admissible with the weight $\alpha_++2\in(0,1)$ (III.F$'$
Proposition 3.3), which is Lemma 3.5's hypothesis. $\square$

**Proposition 4.6 ([Hin26] (9.9) at $n = 4$).** Let $C_\lambda\ge1$, $\delta>0$ small, $s<2-\delta-C_\lambda$,
$\gamma_{\mathrm{cf}}\in(-1,0)$, and $\mathsf b$ as in Lemma 4.2. There are $h_0>0$ and $C$ such that for $h<h_0$ and
$z\in\mathcal Z_h$:
$$\|u\|_{\mathbf o}\le C\|Pu\|_{\mathcal Y_{\mathbf o}},
 \qquad u\in\mathcal H_{\mathbf o},\ Pu\in\mathcal Y_{\mathbf o},\tag{4.6}$$
the dual estimate holds for $P^{*h}$ on the dual spaces, and
$P:\{u\in\mathcal H_{\mathbf o}:Pu\in\mathcal Y_{\mathbf o}\}\to\mathcal Y_{\mathbf o}$ is invertible.

*Proof.* *Step 1: the symbolic estimate.* We show
$\|u\|_{\mathbf o}\le C(\|Pu\|_{\mathcal Y_{\mathbf o}}+\|u\|_{\mathbf o_\flat})$,
$\mathbf o_\flat := (-N_1;\gamma_{\mathrm{cf}},\gamma_{\mathrm{cf}};\mathsf b-\frac14)$, first for $u$ smooth and
compactly supported in $\{v>-1\}\times\mathbb S^3$ with $R$ bounded below on its support, then by density (I.B Lemma 3.1
in $\{v<4\}$, II.F Lemma 2.2 (g) near the cone, I.A Lemma 6.1 (a) at $v = -1$). Cover the characteristic set, at finite
frequencies over sf and at fibre infinity, by finitely many open sets on which one of the following holds, in this order
(for $z_0 = 1$; $z_0 = -1$ by Lemma 4.1 (f)).

(1) $\{v<-\frac14\}$: Lemma 4.4 at the constant semiclassical order $\mathsf b = b_{\mathrm{in}}$ there (Lemma 4.2),
which controls $u$ there in $h^{-b_{\mathrm{in}}}H^s_h$ by $h^{-1-b_{\mathrm{in}}}\|Pu\|_{H^{s-1}_h}$, at all
frequencies, with no error term.

(2) Points of $\Sigma$, at finite frequencies or at fibre infinity, over $\{-\frac12<v<4\}$, that are reached from
$\{v<-\frac14\}$ along the direction of propagation: forward along $H_p$ on $\Sigma_-$ and on the fibre-infinity part of
$\Sigma$ over $\{-1<v<0\}$ with $\xi<0$; backward along $H_p$ on $\Sigma_+$ and on the part with $\xi>0$. I.B
Proposition 4.5 with Corollary 4.6$'$ and Remark 4.7 (a) (in either direction, as $\lambda = 0$) over $\{v<4\}$, and
II.F Proposition 2.5 over $\{R<\frac14\}$ away from the cone saddles, from (1). $\mathsf b$ is non-increasing in these
directions of propagation on a neighbourhood of $\Sigma$ (Lemma 4.2). This covers, by Lemma 4.1 (d): $\Sigma_+$ outside
a neighbourhood of $\partial\mathcal R_+$; the curves (ii) up to neighbourhoods of the cone saddles and of
$\partial\mathcal R_-$; the incoming ray (iii) up to a neighbourhood of $R_{\mathrm{cf},1,\mathrm{in}}$; and fibre
infinity over $\{-1<v<0\}$ outside neighbourhoods of $\partial\mathcal R_\pm$.

(3) Neighbourhoods of $\partial\mathcal R_+$ and $\partial\mathcal R_-$: (4.3), whose control sets $K_E$ consist of
elliptic points and of points of $\Sigma$ near $\partial\mathcal R_\pm$ off it, covered by (2) (on the curves (i) and
(ii) and at fibre infinity) or by (6) below (on the outgoing ray (iii) and the curves (ii) near it). For
$\partial\mathcal R_-$ this step is taken after (6).

(4) A neighbourhood $U_3$ of $R_{\mathrm{cf},1,\mathrm{in}}$ by (R3) (Lemma 4.5), whose $K_E\subset\{R\ge\delta_1\}$
lies in the set covered by (2) (the points of $\Sigma$ near $R_{\mathrm{cf},1,\mathrm{in}}$ with $R>0$ lie on curves
(ii) or (iii) from $\{v<-1\}$; others are elliptic).

(5) The curves in $F_K$ from $R_{\mathrm{cf},1,\mathrm{in}}$ to $R_{\mathrm{cf},\mathrm{out}}$, by II.F Proposition 2.5
from $U_3$; then a neighbourhood $U_5$ of $R_{\mathrm{cf},\mathrm{out}}$ by (R4), whose control set
$K_E\subset\{\phi\ge\delta_2\}$ consists of points of $\Sigma\cap F_K$ on these curves, points of $\Sigma$ over $R>0$
near them, on curves (ii) and so covered by (2) or by II.F Proposition 2.5 once more from (4), and elliptic points; this
is II.F Lemma 3.4's steps (3)-(5), with "curves from $R_{I^+,1,\mathrm{in}}$" read as "curves from $\{v<-1\}$".

(6) The outgoing ray (iii) and the curves (ii) near it, from $U_5$ to a neighbourhood of $\partial\mathcal R_-$: over
$\{R<\frac12\}$ II.F Proposition 2.5 (for $P$ or $\tilde P$, $\lambda\mathcal A$ part of $\mathcal P_1$), over
$\{R>\frac14\}$ I.B Proposition 4.5 with Remark 4.7 (a); $\mathsf b$ is non-increasing along them (Lemma 4.2), and equal
to $b_{\mathrm{out}}$ near them away from the cone.

(7) Elsewhere: the elliptic estimates (I.B Proposition 2.10 in $\{v<4\}$, II.F Proposition 2.6 near the cone), at finite
frequencies off $\Sigma$, at fibre infinity over $\{v\ge0\}$ off $\partial\mathcal R_\pm$, and at the fibre infinity of
the cone calculus.

Each estimate has its $h^{-1}\|GPu\|$ bounded by $C\|Pu\|_{\mathcal Y_{\mathbf o}}$ (in $\{v<4\}$ the differential order
of $\mathcal Y_{\mathbf o}$ is $s-1$ and its semiclassical order $\mathsf b+1$, which is $h^{-1}$ times the order
$\mathsf b$; near the cone II.F section 3.4 (d)), its $\|E'u\|_{\mathbf o}$ by an earlier one, and its errors
$h^{N_1}\|Gu\|_{\mathbf o}+\|u\|_{-K\mathbf 1}$ in $\{v<4\}$ and $\|Gu\|_{\mathbf o-\frac14\mathbf e}$ near the cone by
$C\|u\|_{\mathbf o_\flat}+Ch\|u\|_{\mathbf o}$; a microlocal partition of unity gives the claim, the last term absorbed
for $h$ small. The constants are uniform in $z\in\mathcal Z_h$: each estimate is uniform on neighbourhoods of
$z_*\in\{\pm1\}$, the dependence on $y$ being through $\mathcal P_1$ with $|y/h|\le C_\lambda$.

*Step 2: the transition face.* II.F Lemma 3.6 (Lemma 4.5) applied to $\chi_{\mathrm{tf}}u$, supported in
$\{R<Ch^{1/2}\}\subset\{R<\frac12\}$, with the commutator $[P,\chi_{\mathrm{tf}}]$ estimated there, and on the support
of $1-\chi_{\mathrm{tf}}$ the bound
$\|(1-\chi_{\mathrm{tf}})u\|_{\mathbf o_\flat}\le Ch^{\delta_\flat}\|u\|_{\mathbf o}$ of its proof, which in $\{v<4\}$
is the trivial bound for semiclassical orders ($\rho_{\mathrm{sf}}\sim h$ there):
$\|u\|_{\mathbf o_\flat}\le C\|Pu\|_{\mathcal Y_{\mathbf o}}+Ch^{\delta_\flat}\|u\|_{\mathbf o}$, with
$\mathsf b_\flat := \mathsf b-2\delta_\flat$ still satisfying Lemma 4.2's conditions. With Step 1, (4.6) follows for $h$
small.

*Step 3: the adjoint.* The same steps for $P^{*h}$ on the dual spaces, with the directions of propagation reversed and
sources and sinks interchanged: (4.4) at $\partial\mathcal R_\pm$, now with no control term; propagation backwards along
the curves (ii)-(iii) to the cone point and through it (II.F section 3.6, *The adjoint*, for (R3)-(R4) and $F_K$); on
$\Sigma_+$ and at fibre infinity, propagation from $\partial\mathcal R_\pm$ to $\{v<-\frac14\}$; and near $v = -1$ the
second estimate of (4.5), whose term $\|\chi_1v\|$ lies over $\{-\frac12<v<-\frac14\}$, controlled by the propagation
just described. The dual semiclassical order $-\mathsf b-1$ is non-increasing in these reversed directions, and is the
constant $-b_{\mathrm{in}}-1$ over $\{v\le-\frac14\}$, where the second estimate of (4.5) is used. Step 2 with the
second estimate of II.F (3.15).

*Step 4: invertibility.* For fixed $h<h_0$, (4.6) gives injectivity and closed range, and the dual estimate the
triviality of the annihilator of the range (the pairing $\langle Pu,v\rangle = \langle u,P^{*h}v\rangle$ for $u$ in a
dense set, as in II.F section 3.6). $\square$

## 5. [Hin26] Proposition 9.2 at $n = 4$

**Theorem 5.1 ([Hin26] Proposition 9.2 at $n = 4$).** Assume (C1) (III.F$'$), the parameters of III.F$'$ Proposition
3.3, and let $\lambda\in\mathbb C$ and $(s,\mu)$ be admissible for $\lambda$ (2.6).

(1) (*Fredholm property.*) $N_{\mathrm{sf}}(\lambda):\mathcal X\to\mathcal Y$ of (2.7) is Fredholm of index 0, with
kernel and cokernel independent of the admissible pair.

(2) (*Invertibility.*) It is invertible for $\mathrm{Re}\,\lambda<2$. For every $C$ it is invertible for all but
finitely many $\lambda$ with $\mathrm{Re}\,\lambda\le C$, and the inverse is finite-meromorphic: in every vertical strip
on which one admissible pair serves, $\lambda\mapsto N_{\mathrm{sf}}(\lambda)^{-1}\in\mathcal L(\mathcal Y,\mathcal X)$
is meromorphic with finite-rank principal parts, and for $f$ in the targets of two admissible pairs the two inverses
agree.

(3) (*b-regularity at the light cone.*) If $u\in\dot H^{s,\mu}_{\mathrm b}$ and
$N_{\mathrm{sf}}(\lambda)u\in\dot H^{(s-1;k),\mu}_{\mathrm b;\mathrm b}$, $k\in\mathbb N_0$, then
$u\in\dot H^{(s;k),\mu}_{\mathrm b;\mathrm b}$.

*Proof.* (3) is Proposition 2.7. (1): The Fredholm property and the independence are Proposition 2.4. *Index.* Let
$\mathrm{ind}(\lambda)$ be the index, independent of the admissible pair. Near any $\lambda_1$ fix a pair admissible for
every $\lambda$ in a disc $D_1$ around $\lambda_1$ (shrink the intervals of (2.6) by a margin). On $D_1$, $\mathcal X$
is fixed (Lemma 1.2 (f)) and $\lambda\mapsto N_{\mathrm{sf}}(\lambda)\in\mathcal L(\mathcal X,\mathcal Y)$ is
holomorphic (a polynomial), so $\mathrm{ind}$ is constant on $D_1$; hence constant on $\mathbb C$. By Proposition 4.6,
with $C_\lambda := |\mathrm{Re}\,\lambda_1|+1$, for $|\mathrm{Im}\,\lambda|$ large $N_h$ is invertible on
$\mathcal H_{\mathbf o}$, and by section 4.1 $N_{\mathrm{sf}}(\lambda)$ is invertible from $\{u\in\dot
H^{s',\gamma_{\mathrm{cf}}+\mathrm{Re}\,\lambda}_{\mathrm b}:N_{\mathrm{sf}}u\in\dot
H^{s'-1,\gamma_{\mathrm{cf}}+\mathrm{Re}\,\lambda}_{\mathrm b}\}$, an admissible pair
($s'<2-\delta-C_\lambda\le2-\mathrm{Re}\,\lambda$,
$\gamma_{\mathrm{cf}}+\mathrm{Re}\,\lambda\in(\mathrm{Re}\,\lambda-1,\mathrm{Re}\,\lambda)$). So $\mathrm{ind} = 0$.

(2): For $\mathrm{Re}\,\lambda<2$ the kernel is trivial (Proposition 3.2) and the index 0, so the operator is
invertible. *Finiteness.* For $2\le\mathrm{Re}\,\lambda\le C$, Proposition 4.6 with $C_\lambda := C$ gives invertibility
for $|\mathrm{Im}\,\lambda|\ge M$; the set of $\lambda$ where $N_{\mathrm{sf}}(\lambda)$ is not invertible is discrete
(below), so it meets the compact set $\{2\le\mathrm{Re}\,\lambda\le C,|\mathrm{Im}\,\lambda|\le M\}$ in finitely many
points. *Meromorphy.* On a disc $D_1$ as above the family is holomorphic, Fredholm of index 0 and, $D_1$ being contained
in a vertical strip, in which it is invertible at points of large $|\mathrm{Im}\,\lambda|$ joined to $D_1$ by a chain of
such discs, invertible at some point of each connected component; the analytic Fredholm theorem (I.C (K5)) gives a
meromorphic inverse with finite-rank principal parts and discrete poles. *Agreement.* If $f\in\mathcal Y\cap\mathcal Y'$
for two admissible pairs and $\lambda$ is not a pole, the two solutions $u$, $u'$ both lie in the larger domain (the
spaces are nested in $s$ and $\mu$, as in (2.6) one may pass to the minimum of the two $s$ and of the two $\mu$), where
the kernel is trivial (Proposition 2.4 (3)); so $u = u'$. $\square$

## 6. Findings

(G1) *The threshold at the light cone at $n = 4$* is
$s<2+\min\mathrm{spec}\,\bar S-\mathrm{Re}\,\lambda = 2-\mathrm{Re}\,\lambda$, from $\beta_0 = 2$ and
$p_1 = 3+2\,\mathrm{Re}_h\bar S-2\,\mathrm{Re}\,\lambda$ at $N^*\{v = 0\}$ (Lemma 2.2, (2.3)), against the source's
$\frac32+\min\mathrm{spec}\,\bar S-\mathrm{Re}\,\lambda$ at $n = 3$, where the constant of (1.3) is 1 rather than
$\frac32$; the record's `iotasol5.py` J2 had it by the characteristic exponents.

(G2) *Invertibility for $\mathrm{Re}\,\lambda<2$*, against the source's $1+\epsilon_{\mathrm{ind}}$ at $n = 3$. The
source's bound comes from the weights of the tf-problem, which must lie in its indicial gap
$(0,\epsilon_{\mathrm{ind}})$. At $n = 4$ that gap contains $(0,1]$ and tf-admissibility holds on all of it (III.F$'$),
so the bound is the tf weight $\beta<1$ of Proposition 3.2, that is $\mathrm{Re}\,\lambda<2$. Written at D236 with
$\mathrm{Re}\,\lambda<\frac32$, the limit of Lemma 3.1 as then stated ($s>\frac12$). The ninety-eighth verifier's A2
showed that this limit came from the method. Lemma 3.1 for every $s\notin\frac12+\mathbb Z$ and II.F Lemma 5.7 for
$a>-1$ remove it (D238). So the pure $\iota^+$ resonances of $\bar L$ at $n = 4$ have real part at least 2 (the record's
10.37 (c) had $1+\epsilon_{\mathrm{ind}}$, read from the source), and 10.37 (d) puts those below $\frac52$ at the
constraint candidates in $(2,\frac52)$. The $\epsilon$ of III.F$'$ (2.2) is $<3\times10^{-6}$ at the record's point and
plays no role here.

(G3) *The b-regularity* ([HV15] Theorem 6.3 in the source) is proved by the commutators of Lemma 2.5: the rotations
commute with $N_{\mathrm{sf}}(\lambda)$ through their Lie derivatives, and the dilation $v\partial_v$ produces
$N_{\mathrm{sf}}(\lambda)$ itself and terms whose first-order symbols vanish at the light cone, so the commuted system
has the same threshold. With componentwise rotations the commutator would contain $[\bar S,A_\Omega]\partial_v$, whose
symbol does not vanish there; the Lie derivatives avoid it.

(G4) *The escape function.* The source states the semiclassical estimate (9.9) "in essentially the standard fashion"
with "suitable (variable) semiclassical orders b". Here $\tilde\xi = -(v+2)(v\xi+1)$, with
$H_p\tilde\xi = 2(v+1)|\eta|^2$ on the characteristic set (Lemma 4.1 (b)), is the order's carrier: it equals II.F's
$(1+2R)\xi_{c\hbar}$ near the cone point, rises from $-2$ (the incoming ray) to 0 (the outgoing ray), and with the
conserved $|\eta|^2$ it gives an order that is constant near fibre infinity, as the radial estimate at the light cone
needs, and has II.F's thresholds at the cone saddles (Lemma 4.2).

(G5) *The energy estimates near $v = -1$* are those of Parts I.A-I.B with the spectral variable dual to a spacelike
coordinate ($dT$, Lemma 1.2 (g)): the sign condition $\mathrm{Im}\,z\ge0$ of I.B Proposition 7.1 is replaced by
$|\mathrm{Im}\,z|\le Ch$, which is all that the vertical strips need (Lemma 4.4).

(G6) *What is not proved here:* the source's Proposition 9.4 and the rest of section 9 (the next part); and (C1), an
obligation of Part IV, on which III.F$'$ Proposition 2.3 (a) and Proposition 3.3 rest.
