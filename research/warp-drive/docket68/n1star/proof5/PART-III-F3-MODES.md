# Part III.F$''$. Mode stability of the linearised operator away from zero frequency, at n = 4 ([Hin26] Proposition 8.8)

*Status.* Proved (D238: verifier 98 read the repairs, correct; two nits seated; status synchronised with the README at
D325). Written (D232). This part proves, at spatial dimension $n = 4$, [Hin26] Proposition 8.8 (p. 153), mode stability
of the linearised gauge-fixed Einstein operator $L_b$ at the nonzero frequencies of the closed upper half plane: at the
five-dimensional Tangherlini parameter $b_0$ for every such frequency, and for $b$ near $b_0$ for the frequencies
bounded away from zero. The source takes its input from [AHW24] Theorem 6.1 (1), mode stability of the linearised
Einstein equation on Kerr, which has no five-dimensional counterpart; at $b_0$ it is proved here from the
Kodama-Ishibashi decomposition, with the gauge 1-form built by an ordinary differential equation in the radial direction
and continued inside the horizon as a solution (sections 2-3). The range $b\ne b_0$ with small nonzero frequency is
recorded as open (section 5). Section 1 first supplies what Part III.F does not state, the threshold of $L_b$ at the
event horizon, by which Part I's theory applies to $L_b$. Notation is that of Parts III.F and III.F$'$; $P' :=
D_{g_b}\mathrm{Ric}+\delta^*_{g_b}\delta_{g_b,E^\Upsilon}G_{g_b}$ is the operator without the constraint damping
modification (III.F$'$ Proposition 3.3, Step 5). Computations cited as *computed* are exact (sympy) and rerun by
`lhor5.py` (new) and `gmodes5.py` G1-G5.

## 1. Part I's hypotheses for $L_b$

**Lemma 1.1 (the horizon threshold; [Hin26] footnote 78 at n = 4).** On Tangherlini, in the ingoing chart
$(v,r,\omega)$, let $c_C = a_v\,dv+a_r\,dr$ and $c_{\Upsilon,H} = c_v\,dv+c_r\,dr$ at $r_h$, and put
$x := a_v\gamma_Cr_h$, $y := c_v\gamma_{\Upsilon,H}r_h$. At $N^*\mathcal H$, $\zeta = \xi\,dr$, the subprincipal symbol
of $2L_{b_0}$ on half densities by $|dg|$ is $i\xi f'(r_h)K$ with
$$\det(k-K) = k^5\,(k-1+x)^3\,(k-2+2x)\,(k+(1-e_C)x)\;(k-y)\,(k+1-y)^3\,(k+2-2y).\tag{1.1}$$
So the threshold quantity $\vartheta_{\mathcal H}$ of I.A (1.5), in a suitable fibre inner product, is any number above
$\vartheta_L := \max\{0,\,1-x,\,2-2x,\,-(1-e_C)x,\,y,\,y-1,\,2y-2\}$, and the regularity condition is
$s>\frac12+\vartheta_L$. With III.D$'$'s choice $c_{\Upsilon,H} = -\frac12\chi\,dr$ ($y = 0$), $x = a_v\gamma_Cr_h>0$
(at $r_h$, $g^{-1}(c_C,c_C) = 2a_va_r$, so the past timelike $c_C$ has $a_v>0$), and $e_C\in(0,1)$ makes $-(1-e_C)x<0$;
so $\vartheta_L = \max(0,2-2x)$: it is 0 when $a_v\gamma_Cr_h\ge1$, and below 2 always; 2, the threshold $s>\frac52$ of
the source's footnote 78, is its value without the damping ($\gamma_C = 0$), which that footnote ignores. For every
$\delta>0$ there is a neighbourhood of $b_0$ (and of the modification parameters, in a compact set) on which
$\vartheta_{\mathcal H}<\vartheta_L+\delta$ in a fixed fibre inner product.

*Proof.* Only the first-order part of $2L_{b_0} = \Box+2E^C\delta G+2\delta^*_{E^C}E^\Upsilon G+2R$ (III.F (1.2)) enters
a subprincipal symbol: $-\nabla^a\nabla_a+2E^C\delta G+2\delta^*E^\Upsilon G$, the curvature term, $2E^CE^\Upsilon G$
and $2R$ being of order zero. Near the horizon $E^\Upsilon$ is its horizon part $\gamma_{\Upsilon,H}E_H$ (III.B Lemma
6.2; III.D Lemma 5.1), and only the values of $c_C$ and $c_{\Upsilon,H}$ at $r_h$ enter (they multiply first
derivatives). *Computed* (`lhor5.py` H1-H2, $\mu_0 = 1$ by the homothety, under which $x$ and $y$ are invariant): (1.1),
and at $\gamma_C = \gamma_{\Upsilon,H} = 0$ the polynomial $(k-2)(k+2)(k-1)^3(k+1)^3k^7$, the sums of two of the 1-form
values $1,-1,0,0,0$ of III.D Lemma 5.1. The normalisation of I.A (1.5) is that of III.D Lemma 5.1's proof,
$\beta_0^{-1}p_{1,\pm}$ being $K$ up to the orientation sign. For a matrix $K$ and $\delta>0$, a Jordan basis rescaled
so that the off-diagonal entries are at most $\delta$ defines an inner product in which the self-adjoint part of $K$ has
its eigenvalues below $\max\mathrm{Re}\,\mathrm{spec}\,K+\delta$; $K$ is constant on $N^*\mathcal H$ up to the
rotations, which act by isometries of such a choice made at one point and transported. The continuity in $b$ and the
parameters is as in III.D Lemma 5.1. $\square$

The constraint damping thus helps at the horizon as it does at infinity (III.F (3.1)): its five eigenvalues are the
background's $2,1,1,1,0$ lowered by $x\cdot(2,1,1,1,1-e_C)$, and the gauge modification's five are the background's
$-2,-1,-1,-1,0$ raised by $y\cdot(2,1,1,1,1)$; the other five are 0. The value of $x$ is Part IV's (it depends on $c_C$
at the horizon); the regularity $s$ is chosen accordingly, once.

**Corollary 1.2.** For $b$ near $b_0$ and the parameters of III.F$'$ section 1, $\widehat{L_b}$ satisfies, with (Dyn),
the hypotheses (H1)-(H5) of I.A, with $\vartheta_{\mathcal H}<\vartheta_L+\delta$, and (H6)-(H7) of I.B: (H1), (H2) and
the operator part of (H6) by III.F Lemma 2.1, the threshold at infinity by III.F (3.1)
($\min\mathrm{spec}\,\bar S = 0$), (H7) by III.F Proposition 4.1, and the horizon by Lemma 1.1, the remaining items
concerning the metric alone and holding as for $\Box^\Upsilon_b$ (III.D sections 2-5). Hence, for
$s>\frac12+\vartheta_L$ and admissible orders: $\widehat{L_b}(\sigma):\mathcal X_\sigma\to\mathcal Y_\sigma$ is Fredholm
of index 0 for $\sigma\ne0$, $\mathrm{Im}\,\sigma\ge0$ (I.A Theorem 7.2 (3), I.B Theorem 1.3 (3)); there is
$C_{\mathrm{hf}}$ with $\widehat{L_b}(\sigma)$ invertible for $|\sigma|\ge C_{\mathrm{hf}}$, $\mathrm{Im}\,\sigma\ge0$
(I.B Theorem 1.3, as III.D Proposition 6.1 for $\Box^\Upsilon_b$); and the constants and the openness of invertibility
are uniform in $b$ (I.A Theorem 8.1). The same holds for $P'$, whose horizon matrix is (1.1) at $x = 0$.

**Lemma 1.3 (conormal states).** Let $\hat P$ satisfy (H1)-(H4), $\sigma\ne0$ with $\mathrm{Im}\,\sigma\ge0$, and
$u\in\mathcal A^a(\bar X;E)$ for some $a\in\mathbb R$ (smooth up to $\partial_\sharp X$, conormal at $\partial X$) with
$\hat P(\sigma)u = 0$. Then $u\in\mathcal X_\sigma$ for admissible orders, so $u\in\mathcal A^{\frac32+\bar S-\epsilon}$
for every $\epsilon>0$ (I.A Theorem 7.2 (5)), and $u = 0$ if $\hat P(\sigma)$ is invertible.

*Proof.* Admissibility (I.A (O1)-(O3)) bounds $\mathsf r+\alpha_+$ at $R_{\mathrm{out}}$, the zero section of the
boundary face, only from above; so I.A Lemma 7.1 gives admissible orders with
$\mathsf r_{\mathrm{out}}+\alpha_+<\min(a-2,-\frac12+\bar S)$ when $\mathrm{Re}\,\sigma\ne0$, and the constant order
$\mathsf r_{\mathrm{out}}$ is allowed when $\mathrm{Re}\,\sigma = 0$ (I.A Theorem 7.2 (2)). By I.A Lemma 7.4 (a),
$u\in\bar H^{s,\mathsf r+\alpha_+}$ for every $s$ (the order exceeds $a-2$ only away from the zero section, where it is
unrestricted), and $\hat P(\sigma)u = 0\in\mathcal Y_\sigma$. The kernel does not depend on the admissible orders (I.A
Theorem 7.2 (3)). $\square$

## 2. The linearised Einstein equation on Tangherlini

On $\{r>r_h\}$ use the static chart $(t,r,z)$, $g = -f\,dt^2+f^{-1}dr^2+r^2\gamma$, $f = 1-\mu_0/r^2$,
$r_* = r+\frac{r_h}2\log\frac{r-r_h}{r+r_h}$, and III.B's $t_*$, which is $v+F_H(r)$ near $r_h$ ($v = t+r_*$, $F_H$
smooth in the ingoing chart) and $t-r_*+c_0+O(r^{-1})$, with all derivatives, at infinity (III.D Proposition 6.2, *The
class*). A *mode* is $h = e^{-i\sigma t_*}u$ with $u$ smooth on $\{r>r_0\}$ (in the ingoing chart near $r_h$) and
conormal at infinity, $u\in\mathcal A^a$ for some $a$; equivalently, on $\{r>r_h\}$,
$h = e^{-i\sigma t}e^{-i\sigma r_*}\times$(smooth across $r_h$) near $r_h$ and
$e^{-i\sigma t}e^{i\sigma r_*}\times$(conormal) near infinity. The operators $D\mathrm{Ric}$, $\delta^*$,
$\Box^\Upsilon_{b_0}$ and $P'$ at $b_0$ commute with the rotations ($E^\Upsilon$ at $b_0$ is built from $d\bar t$, $dr$,
III.B (6.5), and $c_{\Upsilon,H} = -\frac12\chi\,dr$), and the projections onto a type and degree (III.A$'$ Lemma 1.6)
preserve modes. *The ODE fact* (III.D Proposition 6.2's proof): a solution of $-\Phi_{**}+V\Phi = \sigma^2\Phi$ on
$(r_h,\infty)$, $V$ real, positive, $O(r^{-2})$ with derivatives at infinity and $O(f)$ at $r_h$, of the form
$e^{-i\sigma r_*}\times$(smooth at $r_h$) and $e^{i\sigma r_*}\times$(conormal, polynomially bounded) at infinity,
vanishes.

**Lemma 2.1 (the radial equations).** Fix a type and degree, $\sigma\ne0$, and a chart $(\tau,r,z)$ in which $\tau$ is a
time function with $\partial_\tau$ the Killing field ($\tau = t$ on $\{r>r_h\}$, or $\tau = t_*$ on $\{r>r_0\}$). For a
symmetric 2-tensor $h = e^{-i\sigma\tau}k$ of that type and degree, the $r$-row of $\delta^*\omega = h$,
$(\delta^*\omega)_{r\mu} = h_{r\mu}$ for $\omega = e^{-i\sigma\tau}w$ of the same type and degree, is a linear system
$\partial_rW = A(r)W+H(r)$ for the coefficients $W$ of $w$, with $A$ smooth where the chart is:
$\partial_rw_r = h_{rr}+\Gamma^\lambda_{rr}w_\lambda$,
$\partial_rw_\tau = 2h_{r\tau}+i\sigma w_r+2\Gamma^\lambda_{r\tau}w_\lambda$,
$\partial_rw_A = 2h_{rA}-\partial_Aw_r+2\Gamma^\lambda_{rA}w_\lambda$, the angular derivative acting on the harmonic
algebraically. Hence: (a) every 1-form of that type with $\delta^*\omega = h$ on an interval is the solution of the
system determined by its value at one point; (b) in the chart $(t_*,r,z)$ on $\{r>r_0\}$, if $h$ is a mode, so are the
solutions (near infinity, for $\tilde W := (w_r,r^{-1}w_{t_*},r^{-1}w_A)$ the system is a b-system
$r\partial_r\tilde W = \tilde A\tilde W+\tilde H$ with $\tilde A$ bounded with b-derivatives, so variation of constants
gives polynomial bounds and conormality); (c) in the static chart the coefficients are real-analytic in $r$ on
$(r_h,\infty)$.

*Proof.* The formulas are the definition of $\delta^*$ with $\partial_\tau\mapsto-i\sigma$. (a) is uniqueness for the
system. (b) $A$ is smooth on $(r_0,\infty)$, as the chart is. Near infinity, in III.B's $t_*$ ($t-r_*+c_0+O(r^{-1})$
there), $g_{t_*t_*}+1$, $g_{t_*r}+1$ and $g_{rr}$ are $O(r^{-2})$ with b-derivatives, and $g$ is $t_*$-independent and
block-diagonal against the sphere. So $\Gamma^\lambda_{rr}$ and $\Gamma^\lambda_{rt_*}$ ($\lambda\in\{t_*,r\}$) are
$O(r^{-3})$, $\Gamma^{t_*}_{rA} = \Gamma^r_{rA} = \Gamma^A_{rr} = \Gamma^A_{rt_*} = 0$ and
$\Gamma^B_{rA} = r^{-1}\delta^B_A$: the one entry of $A$ that does not decay is $i\sigma$, coupling $w_r$ into the
$w_{t_*}$ row. In $\tilde W := (w_r,r^{-1}w_{t_*},r^{-1}w_A)$ the system is
$r\partial_r\tilde W = \tilde A\tilde W+\tilde H$ with $\tilde A$ bounded with all b-derivatives (the entry $i\sigma$ in
the second row; in the angular row $r\partial_r\tilde W_A = \tilde W_A-\partial_A\tilde W_r+2h_{rA}$, from
$\Gamma^B_{rA} = r^{-1}\delta^B_A$ and the scaling, a diagonal $+1$ and an $O(1)$ coupling $-\partial_A$ to
$\tilde W_r$, bounded on each type and degree; $O(r^{-1})$ and $O(r^{-2})$ entries elsewhere; corrected at D238) and
$\tilde H$ conormal with a polynomial bound; for this b-system variation of constants gives polynomial bounds and
propagates b-regularity. (A bound $A = O(r^{-1})$ in the frame $(dt_*,dr,r\,dz)$, stated here before D235, is false
because of the entry $i\sigma$; the ninety-seventh verifier.) (c) The static Tangherlini metric is analytic in $r>r_h$.
$\square$

**Theorem 2.2 ([AHW24] Theorem 6.1 (1) on five-dimensional Tangherlini).** Let $\sigma\ne0$, $\mathrm{Im}\,\sigma\ge0$,
and let $h$ be a mode of one type and degree with $D_{g_{b_0}}\mathrm{Ric}(h) = 0$ on $\{r>r_h\}$. Then there is a mode
1-form $\omega$ on $\{r>r_0\}$, of the same type and degree, with $h = \delta^*\omega$ on $\{r>r_h\}$.

*Proof.* We work on $\{r>r_h\}$ in the static chart, with the Kodama-Ishibashi splitting into $(t,r)$- and
$\mathbb S^3$-parts ([KI03] at their $n = 3$, $K = 1$, $\Lambda = 0$, $2M = \mu_0$; `gmodes5.py` works at a point of
$\mathbb S^3$ with free jets of the harmonic, which suffices as the isometries act transitively and commute with
$D\mathrm{Ric}$). In each sector we find a 1-form $\zeta$, smooth on $\{r>r_h\}$ off at most one radius, with
$h = \delta^*\zeta$ there; Step 5 removes the exceptional radius, and Step 6 makes $\zeta$ a mode on $\{r>r_0\}$. Each
master field below is, as a function of the components of $h$ in the ingoing chart, free of $1/f$ (*computed*, G5), so
it is $e^{-i\sigma t}e^{-i\sigma r_*}\times$(smooth at $r_h$); at infinity the static components are combinations of
those in $(t_*,r,z)$ with bounded conormal coefficients, so it is $e^{-i\sigma t}e^{i\sigma r_*}\times$(conormal,
polynomially bounded).

*Step 1: tensor type, $l\ge2$.* $h = 2r^2H\,T_{ij}dz^idz^j$, $T$ a trace-free, divergence-free tensor harmonic with
$(\Delta+k_T^2)T = 0$, $k_T^2 = l(l+2)-2$. $D\mathrm{Ric}(h) = 0$ is $\Box H+\frac3rDr\cdot DH-\frac{k_T^2+2}{r^2}H = 0$
([KI03] (5.3); *computed*, G1), and $\Phi := r^{3/2}H$ solves $-\Phi_{**}+V_T\Phi = \sigma^2\Phi$,
$V_T = \frac f{r^2}(k_T^2+2+\frac34+\frac{9\mu_0}{4r^2})>0$. $H$ is an angular component, the same in both charts; the
ODE fact gives $\Phi = 0$, so $h = 0 = \delta^*0$.

*Step 2: vector type, $l\ge2$.* $h = 2rf_aV_i\,dy^adz^i+2r^2H_TV_{ij}dz^idz^j$, $V$ co-closed with
$(\Delta+k_V^2)V = 0$, $k_V^2 = l(l+2)-1$, $V_{ij} = -(D_iV_j+D_jV_i)/(2k_V)$. With $\zeta_0 := r^2B\,V_idz^i$,
$B := -2H_T/k_V$, $h' := h+\delta^*\zeta_0$ has $H_T = 0$ and $f_a = F_a := f_a+\frac r{k_V}D_aH_T$, the gauge invariant
([KI03] (5.10); *computed*, G2). $D\mathrm{Ric}(h') = D\mathrm{Ric}(h) = 0$ gives, at $\sigma\ne0$, with
$\Omega := r^2F^r/(i\sigma)$: $r^2F^t = \Omega'$, and $\Phi := r^{-3/2}\Omega$ solves the master equation with
$V_V = \frac f{r^2}(k_V^2+1+\frac34-\frac{27\mu_0}{4r^2})\ge\frac f{r^2}(l(l+2)-6)>0$ ([KI03] (5.15); *computed*, G2,
G5). The ODE fact gives $\Phi = 0$, so $F = 0$, $h' = 0$, and $h = \delta^*(-\zeta_0)$.

*Step 3: scalar type, $l\ge2$.* $h = f_{ab}S\,dy^ady^b+2rf_aS_i\,dy^adz^i+2r^2(H_L\gamma_{ij}S+H_TS_{ij})dz^idz^j$,
$(\Delta+k^2)S = 0$, $S_i = -D_iS/k$, $S_{ij} = D_iD_jS/k^2+\frac13\gamma_{ij}S$. With
$\zeta_1 := -2X_aS\,dy^a-\frac{2r^2}kH_TS_idz^i$, $X_a := \frac rk(f_a+\frac rkD_aH_T)$ ([KI03] (2.8)),
$h' := h+\delta^*\zeta_1$ has $f_a = H_T = 0$ and the invariants $F$, $F_{ab}$ of [KI03] (2.7) as its remaining
components. $D\mathrm{Ric}(h') = 0$ is seven equations. The trace-free angular one is
$-\frac{k^2}{4r^2}(F^a{}_a+2F) = 0$, the algebraic relation that [KI03]'s $X$, $Y$, $Z$ ((2.20)-(2.21)) parametrise; at
$\sigma\ne0$, with $Z = i\sigma\tilde Z$, three of the others are [KI03] (2.24a-c) and the remaining three reduce to one
linear constraint preserved by the flow, so the solutions form a two-dimensional space;
$\Phi := (3\tilde Z-r(X+Y))/(r^{1/2}H)$, $H := m+6\mu_0/r^2$, $m := k^2-3$, solves the master equation with
$V_S = fQ/(16r^2H^2)$ on the constraint, and the determinant of $(r^{1/2}\Phi,r^{1/2}\Phi',\text{constraint})$ in
$(X,Y,\tilde Z)$ is $-r^4(r^2-\mu_0)^5\ne0$ ([KI03] (3.1)-(3.7); *computed*, G3). $Q>0$ on $r>r_h$ for $l\ge2$ ($m\ge5$;
*computed*, G5: with $\varkappa := \mu_0/r^2\in[0,1]$,
$Q = 1296\varkappa^3+(624m-144)\varkappa^2+36m(m-12)\varkappa+16m^3+60m^2$ is at least $16m(m-3)(m+9)$ for $3<m\le12$
and at least $16m^3+60m^2$ for $m\ge12$). The ODE fact gives $\Phi = 0$, so $X = Y = \tilde Z = 0$, $F = F_{ab} = 0$,
$h' = 0$ and $h = \delta^*(-\zeta_1)$.

*Step 4: the exceptional sectors* (*computed*, G4). *Scalar type 0* ($S = 1$): $\delta^*(A_t\,dt+A_r\,dr)$ shifts
$f_{tt}$ by $-i\sigma A_t-\Gamma^r_{tt}A_r$ and $H_L$ by $fA_r/(2r)$, so $f_{tt} = H_L = 0$ is reached with
$A_r = -2rH_L/f$ and then $A_t$, algebraically on $\{r>r_h\}$; the mode equations then force $f_{tr} = f_{rr} = 0$. So
$h$ is pure gauge; there is no change of mass, $\sigma$ being nonzero. *Vector type 1* ($V$ a Killing field of
$\mathbb S^3$, $V_{ij} = 0$): $D\mathrm{Ric}(h)_{ab} = 0$ and
$D\mathrm{Ric}(h)_r = \frac{r^2\partial_tF^{(1)}_{tr}}{2(r^2-\mu_0)}$ with
$F^{(1)}_{tr} = r\partial_t(f_r/r)-r\partial_r(f_t/r)$ ([KI03] (5.16)), so a mode has $F^{(1)} = 0$, and then
$f_a = \frac r2D_aB$ with $B = 2if_t/(\sigma r)$: $h$ is pure gauge. *Scalar type 1* ($D_iD_jS = -\gamma_{ij}S$,
$S_{ij} = 0$): the shifts of $f_{tt}$, $f_t$ and $H_L$ under $\delta^*(A_aS\,dy^a+r^2BS_idz^i)$ are free of derivatives,
with determinant $(r^2-\mu_0)(\sigma^2r^4-\mu_0)/(4r^6)$; so off the radius $r_\sigma$ with $\sigma^2r_\sigma^4 = \mu_0$
(which exists, in $(r_h,\infty)$, only for real $\sigma$ with $\sigma^2<1/\mu_0$) the gauge reaching
$f_{tt} = f_t = H_L = 0$ is algebraic, and the mode equations then force $f_{tr} = f_{rr} = f_r = 0$:
$h = \delta^*\zeta_\pm$ on the intervals $(r_h,r_\sigma)$ and $(r_\sigma,\infty)$.

*Step 5: the radius $r_\sigma$.* Let $\omega$ be the solution, on $(r_h,\infty)$, of the static radial system of Lemma
2.1 equal to $\zeta_-$ at a point of $(r_h,r_\sigma)$. By Lemma 2.1 (a), $\omega = \zeta_-$ on $(r_h,r_\sigma)$, so
$\kappa := h-\delta^*\omega$, smooth on $(r_h,\infty)$, vanishes there. On $(r_\sigma,\infty)$, $\zeta_+-\omega$ solves
the homogeneous radial system, so it is $Z(r)c$ for a fundamental matrix $Z$, analytic on $(r_h,\infty)$ (Lemma 2.1
(c)), and $\kappa = \delta^*(Zc)$ there. $\delta^*(Zc)$ is analytic on $(r_h,\infty)$, and at $r_\sigma$ all its
derivatives from the right are those of the smooth $\kappa$, which vanish (from the left); so $\delta^*(Zc)\equiv0$ and
$\kappa = 0$ on $(r_\sigma,\infty)$ too: $h = \delta^*\omega$ on $(r_h,\infty)$.

*Step 6: the mode.* In each sector $h = \delta^*\zeta$ on $(r_h,\infty)$ with $\zeta$ smooth there. Let $\omega$ be the
solution on $(r_0,\infty)$ of the radial system in the chart $(t_*,r,z)$ equal to $\zeta$ at a point $r_1>r_h$; by Lemma
2.1 (a) in that chart, $\omega = \zeta$ on $(r_h,\infty)$, so $h = \delta^*\omega$ there, and by Lemma 2.1 (b) $\omega$
is a mode. $\square$

The sectors exhaust the types and degrees of III.A$'$ Lemma 1.6 for symmetric 2-tensors on $\mathbb S^3$: tensor
$l\ge2$, vector $l\ge1$, scalar $l\ge0$.

**Lemma 2.3 (continuing a solution inside the horizon).** Let $Q$ be a stationary operator on $\{r>r_0-\delta_0\}$ whose
principal part is a positive multiple of $\Box_{g_{b_0}}$, commuting with the rotations, $\sigma\ne0$ with
$\mathrm{Im}\,\sigma\ge0$, and $w$ of one type and degree, smooth on $\{r\ge r_h\}$ (up to the horizon; D238, the proof
uses $w$ there only), with $\hat Q(\sigma)w = 0$ on $\{r>r_h\}$. Then there is $\tilde w$ of that type and degree,
smooth on $\{r>r_0-\delta_0\}$ (so up to $\{r = r_0\}$), with $\hat Q(\sigma)\tilde w = 0$ on $\{r>r_0-\delta_0\}$ and
$\tilde w = w$ on $\{r\ge r_h\}$.

*Proof.* As in III.D Proposition 6.2 (d), in the ingoing chart the equation on the coefficients $U(r)$ of the type and
degree is $-fU''+AU'+BU = 0$ with $A$, $B$ smooth on $(r_0-\delta_0,\infty)$, and with $Y := (U,(r-r_h)U')$ it is
$(r-r_h)Y' = MY$, $M$ smooth. $Y$ is smooth on $[r_h,\infty)$ and solves the equation on $(r_h,\infty)$, so its Taylor
series at $r_h$ solves it formally. Let $Y_B$ be smooth on $(r_h-\epsilon,r_h]$ with that Taylor series (Borel), so
$R := (r-r_h)Y_B'-MY_B$ vanishes to infinite order at $r_h$. Let $\Psi$ be a fundamental matrix of
$(r-r_h)\Psi' = M\Psi$ on $(r_h-\epsilon,r_h)$; Gronwall gives $|\Psi(r)|+|\Psi(r)^{-1}|\le C|r-r_h|^{-m}$,
$m := \max\|M\|$. Then $Z(r) := -\Psi(r)\int_{r_h}^r\Psi(s)^{-1}R(s)(s-r_h)^{-1}ds$ converges, vanishes to infinite
order at $r_h$ (the integrand does, and the equation $Z' = (MZ-R)/(r-r_h)$ carries this to every derivative), and solves
$(r-r_h)Z' = MZ-R$. So $Y_B+Z$ solves the equation on $(r_h-\epsilon,r_h)$ with the Taylor series of $Y$ at $r_h$; glued
to $Y$ it is smooth on $(r_h-\epsilon,\infty)$, and on $(r_0-\delta_0,r_h-\epsilon]$, where $f<0$, the equation is a
regular second-order system and the solution continues. Its first entry, times the harmonic and $e^{-i\sigma t_*}$, is
$\tilde w$ (the first row of $M$ being $(0,1)$, the second entry stays $(r-r_h)U'$). $\square$

## 3. Mode stability at the Tangherlini parameter

**Proposition 3.1 ([Hin26] Proposition 8.8 at $b_0$).** Let the modification parameters be those of III.D$'$ Proposition
4.1 and III.F$'$ section 1, and $s>\frac12+\vartheta_L$. For every $\sigma\ne0$ with $\mathrm{Im}\,\sigma\ge0$,
$\widehat{L_{b_0}}(\sigma):\mathcal X_\sigma\to\mathcal Y_\sigma$ is invertible, and $\widehat{L_{b_0}}(\sigma)$ has
trivial kernel on $\mathcal A^\alpha(\bar X;S^2T^*X)$ for every $\alpha\in\mathbb R$.

*Proof.* By Corollary 1.2 the operator is Fredholm of index 0, so injectivity suffices; and by Lemma 1.3 a kernel
element in $\mathcal A^\alpha$ lies in $\mathcal X_\sigma$. Let $u\in\mathcal X_\sigma$,
$\widehat{L_{b_0}}(\sigma)u = 0$. By I.A Theorem 7.2 (5), $u\in\mathcal A^{\frac32-\epsilon}$, smooth up to
$\{r = r_0\}$, conormal at infinity. Let $h := e^{-i\sigma t_*}u$, a mode, with $L_{b_0}h = 0$.

*The gauge 1-form.* $\eta := \widehat{\delta_{E^\Upsilon}}(\sigma)Gu$ is conormal and smooth up to $\{r = r_0\}$, and
the linearised second Bianchi identity $\delta GD\mathrm{Ric} = 0$ gives
$\delta G(2L_{b_0}) = \Box^C\delta_{E^\Upsilon}G$, so $\widehat{\Box^C_{b_0}}(\sigma)\eta = 0$. By Lemma 1.3 for
$\Box^C_{b_0}$, which satisfies (H1)-(H4) (III.E), and III.E Theorem 1.1 (1), $\eta = 0$. So $D\mathrm{Ric}(h) = 0$ and
$\delta_{E^\Upsilon}Gh = 0$ on $\{r>r_0\}$, and $P'h = 0$ there.

*The exterior.* Let $h_\pi$ be the component of $h$ of one type and degree, again a mode with both equations. By Theorem
2.2 there is a mode 1-form $\omega_\pi = e^{-i\sigma t_*}w_\pi$ with $h_\pi = \delta^*\omega_\pi$ on $\{r>r_h\}$; then
$\Box^\Upsilon\omega_\pi = 2\delta_{E^\Upsilon}G\delta^*\omega_\pi = 2\delta_{E^\Upsilon}Gh_\pi = 0$ there. Lemma 2.3,
with $Q = \Box^\Upsilon_{b_0}$, gives $\tilde w_\pi$, smooth on $\bar X$ (that is, up to $\{r = r_0\}$), conormal at
infinity (it is $w_\pi$ on $\{r\ge r_h\}$), with $\widehat{\Box^\Upsilon_{b_0}}(\sigma)\tilde w_\pi = 0$ on all of
$\bar X$. By Lemma 1.3 and III.D$'$ Proposition 4.1 (invertibility for every $\sigma$ of the closed upper half plane),
$\tilde w_\pi = 0$; so $h_\pi = 0$ on $\{r>r_h\}$.

*The interior.* $h_\pi$ vanishes on $\{r>r_h\}$ and solves $P'h_\pi = 0$ on $\{r>r_0\}$,
$2P' = \Box+2\delta^*E^\Upsilon G$ having the principal part of $\Box$; III.D Proposition 6.2 (d) (the system
$(r-r_h)Y' = MY$ and Gronwall) gives $h_\pi = 0$ on $\{r>r_0\}$. As this holds for every type and degree, $u = 0$.
$\square$

## 4. Near the Tangherlini parameter

**Proposition 4.1 ([Hin26] Proposition 8.8 for $|\sigma|\ge c_0$).** Fix the modification parameters as in Proposition
3.1. For every $c_0>0$ there is a neighbourhood $\mathcal B(c_0)$ of $b_0$ such that for $b\in\mathcal B(c_0)$ and every
$\sigma$ with $\mathrm{Im}\,\sigma\ge0$, $|\sigma|\ge c_0$,
$\widehat{L_b}(\sigma):\mathcal X_\sigma\to\mathcal Y_\sigma$ is invertible and has trivial kernel on every
$\mathcal A^\alpha$.

*Proof.* As III.D Proposition 6.3. For $|\sigma|\ge C_{\mathrm{hf}}$, Corollary 1.2. On the compact set
$K := \{c_0\le|\sigma|\le C_{\mathrm{hf}},\ \mathrm{Im}\,\sigma\ge0\}$, $\widehat{L_{b_0}}(\sigma)$ is invertible
(Proposition 3.1); by I.A Theorem 8.1 every $\sigma\in K$ has a neighbourhood $U_\sigma$ and a neighbourhood of $b_0$ on
which invertibility holds; finitely many $U_\sigma$ cover $K$. The kernel on $\mathcal A^\alpha$ by Lemma 1.3. $\square$

## 5. What remains open

For $b\ne b_0$ and $0<|\sigma|<c_0$, invertibility of $\widehat{L_b}(\sigma)$ is not proved here: Proposition 4.1's
perturbation degenerates as $c_0\to0$, the neighbourhood $\mathcal B(c_0)$ shrinking. The source covers this range by
[AHW24] Theorem 6.1 (1), proved on Kerr from the Teukolsky equation, which has no counterpart for the five-dimensional
Myers-Perry family. Where the source uses Proposition 8.8 (the contour deformation before his (10.3), through [Hin26c]
Theorem 9.5, p. 168) this range is needed. It is to be supplied by the low-energy analysis of the parts on [Hin26]
sections 9-12, which treat $\widehat{L_b}(\sigma)$ for small $\sigma$ near the zero energy operator (whose kernel and
cokernel are the subject of the next part), or else added to Part VI's obligations; the record's supplement 10.27
computed it at $b_0$ only, which Proposition 3.1 now proves.

## 6. Findings

(F$''$1) *[AHW24] replaced at $b_0$.* The input of [Hin26] Proposition 8.8 is proved on five-dimensional Tangherlini by
the Kodama-Ishibashi master equations, whose potentials are positive for $l\ge2$, and the three exceptional sectors,
which are pure gauge at $\sigma\ne0$ (Theorem 2.2). The gauge 1-form is built by the radial equations of Lemma 2.1, with
no estimate in $l$ needed: mode stability is shown harmonic by harmonic, and the localisation to the exterior is removed
by continuing the gauge potential inside the horizon as a solution (Lemma 2.3) and applying the mode stability of
$\Box^\Upsilon$ on all of $\bar X$, in place of a statement on $X$ like the source's.

(F$''$2) *The horizon threshold of $L_b$* (Lemma 1.1), which Part III.F did not state and Part I's theory needs:
$s>\frac12+\max(0,2-2a_v\gamma_Cr_h)$ with III.D$'$'s horizon modification and $a_v>0$ ($c_C$ past timelike), below the
source's $\frac52$, which his footnote 78 states without the damping; constraint damping lowers it, as it lowers the
threshold at infinity.

(F$''$3) *The scalar type 1 sector at real $\sigma$.* The algebraic gauge degenerates on the sphere
$\sigma^2r^4 = \mu_0$, which the record's G4 avoided by working off it; the two gauge 1-forms are glued by the
analyticity of the radial system (Theorem 2.2, Step 5).

(F$''$4) *Open:* small nonzero $\sigma$ away from $b_0$ (section 5).
