# Part II.G. The Nash-Moser theorem, smoothing operators and tame bounds, at n = 4

*Status.* Proved (D216: verifier 90 read the repairs, correct; amended D304, Theorem 2.1 (iii) and (H10); status
synchronised with the README at D325). Verified. Written out in full (D211) and read line by line by the eighty-ninth
verifier (D213), which redid the exponent algebra of the Nash-Moser iteration by machine: no major finding; its five
minor findings, two of which withdraw findings (H2) and (H7) as misreadings of the source, and its nits are seated
(section 6.3). The part is labelled proved once the next reader has confirmed the repairs. This part proves, at spatial
dimension $n = 4$, the tools of [Hin26c] section 12 (pp. 233-243) on which the nonlinear step of the route rests: the
Nash-Moser theorem in the form of its Theorem 12.4, the smoothing operators of its Proposition 12.6 and Example 12.7 on
the spaces of its Theorem 11.1, and the tame bounds of its Lemma 12.8. The source is [Hin26c] = P. Hintz,
arXiv:2606.28008v1 (printed page numbers). Parts II.A (`PART-II-A-SETUP.md`), II.C, II.E (`PART-II-E-ENERGY.md`), II.F
(`PART-II-F-IOTA.md`) and II.F$'$ (`PART-II-F2-TAME.md`) are cited as II.A, II.C, II.E, II.F and II.F$'$.

*Method.* None of the three statements depends on the dimension; $n = 4$ enters only through the spaces to which they are
applied. The source quotes the Nash-Moser theorem from [SR89] in the form of [Hin24a] Theorem 6.11, neither of which is
read here; the theorem is proved here instead (section 2), by Saint Raymond's iteration with a smoothing step at each
stage and with the supports tracked, under the source's hypotheses made precise where it states them loosely. The proof
needs the constants of the hypotheses up to the order $21d+6$, where the source quotes $16d^2+43d+24$; no later part
depends on the number. The smoothing operators are built as in the source, with the support bookkeeping and the charts at
the hypersurface $\{t^\flat = 1\}$ written out for the domain $\Omega_*$ of Part II.F$'$ (section 3), and the tame bounds
are proved from the Gagliardo-Nirenberg inequality, read off the Fourier transform (section 4). Section 5 records the
weights of the source's section 12.1 at $n = 4$, and what of section 12 is not carried; section 6 the findings and the
sources.

*Organisation.* Section 1: scope. Section 2: the Nash-Moser theorem. Section 3: smoothing operators. Section 4: tame
bounds. Section 5: the weights at $n = 4$; what is not carried. Section 6: findings and sources.

## 1. Scope

[Hin26c] section 12, "Application I: nonlinear scalar waves", has five subsections. Its subsection 12.2 holds the three
general tools that later parts use: the Nash-Moser theorem (Theorem 12.4, with Remark 12.5 on the norms), smoothing
operators on spaces of supported b-Sobolev functions (Proposition 12.6 and Example 12.7), and tame bounds for products
and nonlinear functions (Lemma 12.8). They are proved here, in sections 2-4. The rest of the section concerns the scalar
wave operator $\Box_g$ on a subextremal Kerr spacetime: its 0-admissibility (Theorem 12.2, through Theorem 12.3, "mode
stability implies 0-admissibility", and the mode stability of Kerr) and three model problems (Theorems 12.9, 12.11 and
12.12, a power nonlinearity, a quasilinear equation and a null form). The route to Theorem 4 does not pass through them:
its linear operator is the gauge-fixed linearised Einstein operator of [Hin26] (Part III), whose admissibility has a loss
$\aleph>0$ from zero-energy states and is established in [Hin26], not by Theorem 12.2; and the model problems are not
used. They are not carried (section 5). Theorem 12.3 at $n = 4$, the passage from the spectral theory of Part I to the
estimate (2.2) of II.C Definition 2.7 (3) with $\aleph = 0$, is the model for that admissibility proof and is to be
written with its $\aleph>0$ version in Part III.

Throughout, $\mathbb N = \{1,2,\dots\}$, $\mathbb N_0 = \mathbb N\cup\{0\}$, and constants $C$ may change from line to
line, depending only on the quantities named.

## 2. The Nash-Moser theorem

### 2.1 The statement

The source writes the two families of spaces with the same letter in two fonts; here $B^k$ are the spaces of unknowns and
$F^k$ those of right sides.

**Theorem 2.1 ([Hin26c] Theorem 12.4).** Let $d\in\mathbb N$, $\delta>0$ and $\eta_0\in(0,1]$. For $k\in\mathbb N_0$ let
$(B^k,|\cdot|_k)$ and $(F^k,\|\cdot\|_k)$ be Banach spaces with continuous inclusions $B^s\hookrightarrow B^t$,
$F^s\hookrightarrow F^t$ for $s\ge t$, along which the norms do not increase: $|v|_t\le|v|_s$, $\|f\|_t\le\|f\|_s$
(Remark 2.2). Put $B^\infty := \bigcap_kB^k$, $F^\infty := \bigcap_kF^k$. For $\eta\in[0,1]$ let $B^k_\eta\subset B^k$ be
closed linear subspaces, non-increasing in $\eta$, with $B^k_0 = B^k$, and $B^\infty_\eta := \bigcap_kB^k_\eta$; let
$F^\infty_\eta\subset F^\infty$ be linear subspaces, non-increasing in $\eta$, with $F^\infty_0 = F^\infty$. Assume:

(i) (*Smoothing.*) For every $\theta>1$ there is a linear map $S_\theta:B^\infty_{\theta^{-1/2}}\to B^\infty$ with
$S_\theta(B^\infty_\eta)\subset B^\infty_{\eta-\theta^{-1/2}}$ for $\eta\in[\theta^{-1/2},1]$, and constants $C_{s,t}$,
independent of $\theta$, with
$$|S_\theta v|_s\le C_{s,t}\theta^{s-t}|v|_t\ \ (s\ge t),\qquad|v-S_\theta v|_s\le C_{s,t}\theta^{s-t}|v|_t\ \ (s\le t),
\qquad v\in B^\infty_{\theta^{-1/2}}.\tag{2.1}$$

(ii) (*The map.*) $\Phi:U\to F^\infty$, $U := \{u\in B^\infty:|u|_{3d}<\delta\}$, maps $U\cap B^\infty_\eta$ into
$F^\infty_\eta$ for $\eta\in[0,\eta_0]$, and is twice differentiable in the following sense: for $u\in U$ there are a
linear map $\Phi'(u):B^\infty\to F^\infty$ and a symmetric bilinear map $\Phi''(u):B^\infty\times B^\infty\to F^\infty$
such that for $u,u+h\in U$ the maps $s\mapsto\Phi'(u+sh)h$ and $s\mapsto\Phi''(u+sh)(h,h)$, $s\in[0,1]$, are continuous
into $F^{2d}$ and
$$\Phi(u+h)-\Phi(u) = \int_0^1\Phi'(u+sh)h\,ds,\qquad\Phi(u+h)-\Phi(u)-\Phi'(u)h = \int_0^1(1-s)\Phi''(u+sh)(h,h)\,ds
\tag{2.2}$$
in $F^{2d}$. There are constants $C_1$, $C_2$ and $C_k$, $k\ge d$, such that for $u\in U$ and $v,w\in B^\infty$
$$\|\Phi(u)\|_k\le C_k(1+|u|_{k+d})\ (k\ge d),\qquad\|\Phi'(u)v\|_{2d}\le C_1|v|_{3d},\qquad\|\Phi''(u)(v,w)\|_{2d}
\le C_2|v|_{3d}|w|_{3d}.\tag{2.3}$$

(iii) (*Right inverses.*) For $u\in U$ there is a linear map $\Psi(u):F^\infty\to B^\infty$ with
$\Psi(u)(F^\infty_\eta)\subset B^\infty_\eta$ for $\eta\in[0,1]$ whenever $u\in U\cap B^\infty_\eta$ (amended in D304,
finding (H10)), $\Phi'(u)\Psi(u)f = f$ for $f\in F^\infty$, and (with the same constants $C_k$, enlarged if necessary)
$$|\Psi(u)f|_k\le C_k\big(\|f\|_{k+d}+|u|_{k+d}\|f\|_{2d}\big),\qquad k\ge d,\ f\in F^\infty.\tag{2.4}$$

Let $N := 21d+6$. There is $\epsilon>0$, depending only on $d$, $\delta$, $\eta_0$, $C_1$, $C_2$ and the constants $C_k$,
$C_{s,t}$ with $k,s,t\le N$, such that if $\|\Phi(0)\|_{2d}<\epsilon$, then there is $u\in B^\infty_{\eta_0/2}$ with
$|u|_{3d}<\delta$ and $\Phi(u) = 0$.

The source states (ii) for all $\eta\in[0,1]$, together with $\Phi(0)\in F^\infty_{\eta_0}$; as $0\in B^\infty_{\eta}$
for every $\eta$, the hypothesis for all $\eta\in[0,1]$ would force $\Phi(0)\in F^\infty_1$. The form above asks (ii)
only for $\eta\le\eta_0$; in the source's applications both forms hold, with $\eta_0 = 1$. The source's conclusion is
$u\in B^\infty$; as its $B^k_0$ is the whole space ((12.21)), that is the support $t_*\ge1$ its applications use (p.
240). Theorem 2.1 strengthens the conclusion to $u\in B^\infty_{\eta_0/2}$, which costs the closedness of the $B^k_\eta$,
available for the spaces of Proposition 3.1 (section 6, (H2)-(H3), as amended in D213).

**Remark 2.2 ([Hin26c] Remark 12.5).** The monotonicity of the norms costs nothing: if the inclusions are continuous,
$|v|'_s := \max_{t\le s}|v|_t$ is an equivalent norm on $B^s$ and is non-decreasing in $s$, and likewise for $F^s$. (2.1)
persists with other constants: for $s\ge t$ and $t'\le s$, $|S_\theta v|_{t'}\le C_{t',t}\theta^{t'-t}|v|_t$ if $t'\ge t$
and $|S_\theta v|_{t'}\le C_{t',t'}|v|_{t'}$ if $t'<t$, both at most $C\theta^{s-t}|v|'_t$; for $s\le t$ and $t'\le s$,
$|v-S_\theta v|_{t'}\le C_{t',t}\theta^{t'-t}|v|_t\le C_{t',t}\theta^{s-t}|v|'_t$. (2.3) and (2.4) persist, the norms of
index below $d$ (resp. $2d$) being bounded by those of index $d$ (resp. $2d$).

### 2.2 The proof

*Parameters.* Let $\kappa := \frac32$, $\alpha := 8d+2$ and $\beta := 4d+2$; then
$$N = 5d+\beta+\kappa\alpha+1,\qquad4d-2\alpha = -\kappa\alpha-1,\qquad\beta+2d+1 = \kappa\beta.\tag{2.5}$$
For $\theta_0\ge2$, to be fixed, put $\theta_j := \theta_0^{\kappa^j}$. As $\kappa^j\ge1+\frac j2$ (Bernoulli's
inequality), for $\gamma>0$ with $\theta_0^{\gamma/2}\ge2$,
$$\sum_{j\ge0}\theta_j^{-\gamma}\le\theta_0^{-\gamma}\sum_{j\ge0}\theta_0^{-\gamma j/2}\le2\theta_0^{-\gamma}.\tag{2.6}$$

*The iteration.* Put $u_0 := 0$ and $\eta_j := \eta_0-\sum_{i<j}\theta_i^{-1/2}$. As long as $u_j\in U\cap
B^\infty_{\eta_j}$ with $\eta_j\ge\frac12\eta_0$, put
$$e_j := \Phi(u_j),\qquad v_j := \Psi(u_j)e_j,\qquad w_j := S_{\theta_j}v_j,\qquad u_{j+1} := u_j-w_j.\tag{2.7}$$

*The induction.* We show that, for $\theta_0$ large (depending only on the quantities named in the theorem) and
$\|\Phi(0)\|_{2d}\le\theta_0^{-\alpha}$, every $j\ge0$ satisfies

(a$_j$) $u_j\in B^\infty_{\eta_j}$, $\eta_j\ge\frac12\eta_0$, and $|u_j|_{3d}\le\frac12\delta$;

(b$_j$) $\|e_j\|_{2d}\le\theta_j^{-\alpha}$;

(c$_j$) $|u_j|_N\le\theta_j^{\beta}$.

For $j = 0$ this is the hypothesis ($u_0 = 0$). Assume (a$_i$)-(c$_i$) for $i\le j$.

*Bounds on $v_j$.* By (2.4) at $k = d$, with $|u_j|_{2d}\le|u_j|_{3d}\le\delta$, and (b$_j$),
$$|v_j|_d\le C_d(1+\delta)\|e_j\|_{2d}\le K_1\theta_j^{-\alpha}.$$
By (2.4) at $k = N-2d\ge d$, (2.3) at $k = N-d$, the monotonicity of the norms and $\|e_j\|_{2d}\le1$,
$$|v_j|_{N-2d}\le C_{N-2d}\big(C_{N-d}(1+|u_j|_N)+|u_j|_N\big)\le K_2(1+|u_j|_N)\le2K_2\theta_j^\beta.$$

*Supports.* By (ii), $e_j\in F^\infty_{\eta_j}$ ($\eta_j\le\eta_0$); by (iii), as $u_j\in B^\infty_{\eta_j}$, $v_j\in
B^\infty_{\eta_j}$. Choose $\theta_0\ge16\eta_0^{-2}$, with $\theta_0^{1/4}\ge2$. Then
$\theta_j^{-1/2}\le\theta_0^{-1/2}\le\frac14\eta_0\le\eta_j$, so $S_{\theta_j}$ applies to $v_j$, and $w_j\in
B^\infty_{\eta_j-\theta_j^{-1/2}} = B^\infty_{\eta_{j+1}}$; also $u_j\in B^\infty_{\eta_j}\subset
B^\infty_{\eta_{j+1}}$, so $u_{j+1}\in B^\infty_{\eta_{j+1}}$. By (2.6) with $\gamma = \frac12$,
$\eta_{j+1}\ge\eta_0-2\theta_0^{-1/2}\ge\frac12\eta_0$.

*Bounds on $w_j$.* By (2.1),
$$|w_j|_{3d}\le C_{3d,d}\theta_j^{2d}|v_j|_d\le K_3\theta_j^{2d-\alpha},\qquad|w_j|_N\le C_{N,N-2d}
\theta_j^{2d}|v_j|_{N-2d}\le K_4\theta_j^{\beta+2d},$$
$$|v_j-w_j|_{3d}\le C_{3d,N-2d}\theta_j^{5d-N}|v_j|_{N-2d}\le K_5\theta_j^{5d-N+\beta}.\tag{2.8}$$

*(a$_{j+1}$).* By (2.8) and (2.6) with $\gamma = \alpha-2d = 6d+2$, $|u_{j+1}|_{3d}\le\sum_{i\le
j}|w_i|_{3d}\le2K_3\theta_0^{-6d-2}\le\frac12\delta$ for $\theta_0$ large.

*(c$_{j+1}$).* $|u_{j+1}|_N\le\theta_j^\beta+K_4\theta_j^{\beta+2d}\le(1+K_4)\theta_j^{\beta+2d}\le\theta_j^{\beta+2d+1}
= \theta_j^{\kappa\beta} = \theta_{j+1}^\beta$, for $\theta_0\ge1+K_4$, by (2.5).

*(b$_{j+1}$).* $u_j$ and $u_{j+1}$ lie in $U$, which is convex. By (2.2) with $h = -w_j$, and $\Phi'(u_j)v_j = e_j$,
$$e_{j+1} = \Phi'(u_j)(v_j-w_j)+\int_0^1(1-s)\Phi''(u_j-sw_j)(w_j,w_j)\,ds,$$
so by (2.3), (2.8) and (2.5),
$$\|e_{j+1}\|_{2d}\le C_1K_5\theta_j^{5d-N+\beta}+\tfrac12C_2K_3^2\theta_j^{4d-2\alpha} = \big(C_1K_5+\tfrac12C_2K_3^2
\big)\theta_j^{-\kappa\alpha-1}\le\theta_j^{-\kappa\alpha} = \theta_{j+1}^{-\alpha}$$
for $\theta_0\ge C_1K_5+\frac12C_2K_3^2$. This completes the induction.

The constants $K_1,\dots,K_5$ depend only on $d$, $\delta$ and $C_d$, $C_{N-2d}$, $C_{N-d}$, $C_{3d,d}$, $C_{N,N-2d}$,
$C_{3d,N-2d}$. Fix $\theta_0$ as required above and put $\epsilon := \theta_0^{-\alpha}$; it depends only on the
quantities named in the theorem.

*Higher norms.* Let $M\ge N$. By (2.4) at $k = M-2d$, (2.3) at $k = M-d$ and (b$_j$), $|v_j|_{M-2d}\le K_M(1+|u_j|_M)$,
so by (2.1), $|w_j|_M\le K'_M\theta_j^{2d}(1+|u_j|_M)$, with $K'_M\ge1$, and
$$1+|u_{j+1}|_M\le(1+K'_M\theta_j^{2d})(1+|u_j|_M).$$
Hence $1+|u_j|_M\le\prod_{i<j}2K'_M\theta_i^{2d} =
(2K'_M)^j\theta_0^{2d(\kappa^j-1)/(\kappa-1)}\le(2K'_M)^j\theta_j^{4d}$. As $\theta_j\ge2^{\kappa^j}$ and
$\kappa^j/j\to\infty$, $L_M := \sup_j(2K'_M)^j\theta_j^{-1}$ is finite, and
$$|u_j|_M\le L_M\theta_j^{4d+1},\qquad|w_j|_M\le L'_M\theta_j^{6d+1}.\tag{2.9}$$

*Convergence in every $B^k$.* Let $k>3d$, $\mu := (3d+1)/(k-3d)$ and $M := \max(N,3k-6d)$, so that $\mu(M-k)\ge6d+2$. For
$j$ so large that $\theta_j^\mu\ge16\eta_0^{-2}$, $S_{\theta_j^\mu}$ applies to $w_j\in B^\infty_{\eta_{j+1}}$
($\eta_{j+1}\ge\frac12\eta_0\ge\theta_j^{-\mu/2}$), and by (2.1), (2.8) and (2.9)
$$|w_j|_k\le|S_{\theta_j^\mu}w_j|_k+|w_j-S_{\theta_j^\mu}w_j|_k\le C_{k,3d}\theta_j^{\mu(k-3d)}K_3
\theta_j^{-6d-2}+C_{k,M}\theta_j^{\mu(k-M)}L'_M\theta_j^{6d+1}\le C\big(\theta_j^{-3d-1}+\theta_j^{-1}\big).$$
So $\sum_j|w_j|_k<\infty$ for every $k$ (for $k\le3d$ by (2.8) and monotonicity), and $u_j = -\sum_{i<j}w_i$ converges in
every $B^k$; the limits agree, the inclusions being continuous, and define $u\in B^\infty$ with
$|u|_{3d}\le\frac12\delta<\delta$. As $u_j\in B^k_{\eta_0/2}$ for all $j$ and $k$ ((a$_j$), the subspaces being
non-increasing in $\eta$) and $B^k_{\eta_0/2}$ is closed, $u\in B^\infty_{\eta_0/2}$.

*The equation.* $u$ and $u_j$ lie in $U$; by (2.2) and (2.3), $\|\Phi(u)-\Phi(u_j)\|_{2d}\le C_1|u-u_j|_{3d}\to0$, and
$\|\Phi(u_j)\|_{2d}\le\theta_j^{-\alpha}\to0$. So $\Phi(u) = 0$. $\square$

## 3. Smoothing operators

### 3.1 The setting and the statement

Let $M$ be a compact manifold with corners whose boundary hypersurfaces are embedded, its set of boundary hypersurfaces
split as $\mathcal H = \mathcal H_b\sqcup\bar{\mathcal H}$, and $M'\supset M$ an extension of $M$ across the faces in
$\bar{\mathcal H}$: a manifold with corners containing $M$ as a closed subset, whose boundary hypersurfaces are those of
$\mathcal H_b$, extended. Let $\mu$ be a smooth positive b-density on $M'$ (b at the faces of $\mathcal H_b$), and
$\mathcal V_b$ the smooth vector fields on $M'$ tangent to every face of $\mathcal H_b$. For $k\in\mathbb N_0$,
$H^k_b(M')$ is the space of $u\in L^2(M',\mu)$ with $Au\in L^2$ for every product $A$ of at most $k$ elements of
$\mathcal V_b$, normed by the sum of the $L^2$-norms of $Au$ over a finite spanning set (II.A section 4: the Sobolev
spaces of the bounded geometry structure of $\mathcal V_b$, (S3)); $\bar H^k_b(M)$ is the space of restrictions to
$M^\circ$, with the quotient norm. For a weight $w = \prod_{H\in\mathcal H_b}\rho_H^{a_H}$, $a_H\in\mathbb R$, $\rho_H$
defining functions, $w\bar H^k_b(M) := \{u:w^{-1}u\in\bar H^k_b(M)\}$ with $\|u\|_{w\bar H^k_b} := \|w^{-1}u\|_{\bar
H^k_b}$.

Let $t$ be a real function on $M'\setminus\bigcup_{H\in\mathcal H_b}H$, and $c_1\in(0,1]$, such that:

(T1) $t$ is smooth with $dt\ne0$ on $\{|t|<2c_1\}$, and this set meets each $H\in\bar{\mathcal H}$ only in $H^\circ$
(away from all other faces), with $dt|_{TH}\ne0$ there;

(T2) every point $p$ of $\overline{\{|t|\le c_1\}}\cap H$, $H\in\mathcal H_b$, lies on no other boundary hypersurface,
and has a neighbourhood $V$ in $M'$ with a function $\bar t\in C^\infty(V)$ such that $d\bar t|_{TH}\ne0$ on $V\cap H$
and $t-\bar t\in\rho_H^\epsilon C^\infty_b(V)$ for some $\epsilon>0$, $C^\infty_b$ denoting the functions bounded with
all their derivatives along $\mathcal V_b$;

(T3) the functions of $t$ used below, $\psi(t)$ with $\psi\in C^\infty(\mathbb R)$ constant on $(-\infty,-c_1]$ and on
$[c_1,\infty)$, are smooth on $M'$ with all derivatives along $\mathcal V_b$ bounded (that is, $\psi(t)\in C^\infty_b$).

For $\eta\in\mathbb R$ let $\Omega_\eta := M\cap\{t\ge\eta\}$ and $w\bar H^k_b(\Omega_\eta)^{\bullet,-} := \{u\in w\bar
H^k_b(M):\mathrm{supp}\,u\subset\Omega_\eta\}$, a closed subspace, with the norm of $w\bar H^k_b(M)$.

**Proposition 3.1 ([Hin26c] Proposition 12.6).** Let $c_0 := \frac18c_1$, and for $\eta\in[0,1]$ and $k\in\mathbb N_0$
let $B^k := w\bar H^k_b(\Omega_0)^{\bullet,-}$, $B^k_\eta := w\bar H^k_b(\Omega_{c_0\eta})^{\bullet,-}$, with the norms
$|\cdot|_k$ of $w\bar H^k_b(M)$. There are linear maps $S_\theta:B^0\to\bigcap_kw\bar H^k_b(M)$, $\theta>1$, with
$S_\theta(B^\infty_\eta)\subset B^\infty_{\eta-\theta^{-1/2}}$ for $\eta\in[\theta^{-1/2},1]$, and constants $C_{s,t}$,
independent of $\theta$, such that for $v\in B^\infty_0$
$$|S_\theta v|_s\le C_{s,t}\theta^{s-t}|v|_t\ \ (s\ge t),\qquad|v-S_\theta v|_s\le C_{s,t}\theta^{s-t}|v|_t\ \ (s\le t).
\tag{3.1}$$
In particular the $B^k_\eta$ satisfy hypothesis (i) of Theorem 2.1, and are closed subspaces of $B^k$.

**Example 3.2 ([Hin26c] Example 12.7, on $\Omega_*$ at $n = 4$).** Let $M$ be the closure of $\{t_*\ge\frac12,\ r\ge
r_0\}$ in the compactified spacetime $\tilde M$ of II.A section 1, a compact manifold with corners with boundary
hypersurfaces $\mathscr I^+$, $\iota^+$, $K^+$ (forming $\mathcal H_b$) and $\{r = r_0\}$, $\{t_* = \frac12\}$ (forming
$\bar{\mathcal H}$), and $M'$ the closure of $\{t_*>\frac14,\ r>r^\sharp\}$ less its faces at $t_* = \frac14$ and $r =
r^\sharp$; $\mu := |dt_*\,dx|/(t_*\langle x\rangle^4)$, a smooth positive b-density (II.F$'$ Corollary 1.2, II.A Lemma
8.8); $w := \rho_I^{a_I}\rho_+^{a_+}\rho_K^{a_K}$ with the defining functions of II.F$'$ (1.1); $t := t^\flat-1$, with
$t^\flat$ the time function of II.C Lemma 3.2, defined on $M'\cap\{t_*\ge\frac12\}$ by II.E Lemma 1.2 (iv), and $t :=
-1$ on $M'\cap\{t_*<\frac12\}$. As $t^\flat\le t_*$ (II.C Lemma 3.2 (b)), $t<-c_1$ on $\{t_*<\frac78\}$, so every
function $\psi(t)$ of (T3) is constant there, and $t$ is smooth wherever (T1) asks. The spaces $B^k_0$ of Proposition
3.1 are then the spaces $H^{k,(\alpha_I,\alpha_+,\alpha_K)}_b(\Omega_*;E)^{\bullet,-}$ of II.F$'$ (1.2), componentwise
and with $w$ adjusted by the factor relating $|dt\,dx|$ to $\mu$, which is a product of powers of $\rho_I$, $\rho_+$,
$\rho_K$ (II.F$'$ Corollary 1.2), with equivalent norms: there the quotient is over extensions supported in
$\{t^\flat\ge1\}$, here over all extensions to $M'$, and the extension of II.F$'$ Lemma 2.5 preserves that support and
is bounded at every order; and $B^k_\eta$ consists of their elements supported in $\{t^\flat\ge1+c_0\eta\}$. The
hypotheses hold with $c_1 := \frac18$:

(T1): $dt^\flat$ is past timelike, so non-zero. On $\{|t^\flat-1|<\frac14\}$, $t_*\le\frac54/C'$ (II.C Lemma 3.2 (b)),
so this set stays away from $\iota^+$ and $K^+$, and $t_*\ge t^\flat>\frac34$, so it does not meet $\{t_* = \frac12\}$;
it meets $\{r = r_0\}$ only away from the other faces, and there $dt^\flat = C'dt_*$ (II.C Lemma 3.2 (c); its proof
takes $r'_0$ large, so $r'_0-1>r_2>r_0$), whose restriction to $\{r = r_0\}$ is non-zero.

(T2): as $t^\flat\ge C't_*$, $\{t^\flat\le\frac98\}$ meets $\mathcal H_b$ only in $\mathscr I^+\cap\{t_*\le\frac98/C'\}$,
away from $\iota^+$, and on $\mathscr I^+$, $t^\flat = t_*$, so the points concerned have $t_*\in[\frac78,\frac98]$, on
no other face. Near them $\bar t := t_*-1$ is smooth, $t_*$ is a coordinate along $\mathscr I^+$, and $t-\bar t =
-t_*(t_*/r)^{\ell_I}$ (II.C Lemma 3.2 (a)), with $t_*/r = \rho_I/(1-\rho_I)$, lies in $\rho_I^{\ell_I}C^\infty_b$.

(T3): near $\mathscr I^+$ at bounded $t_*$, $t^\flat = t_*(1-(t_*/r)^{\ell_I})$
or a smooth function of $t_*$ and $r$ glued to it (II.C Lemma 3.2), with derivatives along $t_*\partial_{t_*}$,
$r\partial_r$, $\partial_\omega$ bounded; and $\psi(t)$ is constant on $\{t^\flat\ge1+c_1\}$, which contains a
neighbourhood of $\iota^+\cup K^+$ in $M'$.

### 3.2 The proof

*Step 1: smoothing on $\mathbb R^m$.* Fix $\phi\in C^\infty_c(\mathbb R^m)$ with $0\le\phi\le1$, $\phi = 1$ on
$\{|\xi|\le1\}$ and $\mathrm{supp}\,\phi\subset\{|\xi|\le2\}$, and put $\check\phi := \mathcal F^{-1}\phi\in\mathcal
S(\mathbb R^m)$. For $\lambda\ge1$ let $S^{(0)}_\lambda v := k_\lambda*v$ with $k_\lambda(y) :=
\phi(\lambda^{1/2}y)\lambda^m\check\phi(\lambda y)$. Then $\mathrm{supp}\,S^{(0)}_\lambda v$ lies in the
$2\lambda^{-1/2}$-neighbourhood of $\mathrm{supp}\,v$, and, with $\|v\|_{H^s} := \|\langle\xi\rangle^s\hat v\|_{L^2}$,
for $s,t\in\mathbb N_0$,
$$\|S^{(0)}_\lambda v\|_{H^s}\le C\lambda^{s-t}\|v\|_{H^t}\ \ (s\ge t),\qquad\|v-S^{(0)}_\lambda v\|_{H^s}\le C
\lambda^{s-t}\|v\|_{H^t}\ \ (s\le t).\tag{3.2}$$
Indeed, $M_\lambda v := \lambda^m\check\phi(\lambda\cdot)*v$ is the Fourier multiplier $\phi(\xi/\lambda)$, and on
$\mathrm{supp}\,\phi(\cdot/\lambda)$, $\langle\xi\rangle\le3\lambda$, while on $\mathrm{supp}(1-\phi(\cdot/\lambda))$,
$\langle\xi\rangle\ge\lambda$; so (3.2) holds for $M_\lambda$ with $C = 3^{|s-t|}$. $R_\lambda :=
M_\lambda-S^{(0)}_\lambda$ is the convolution with $r_\lambda(y) := (1-\phi(\lambda^{1/2}y))\lambda^m\check\phi(\lambda
y)$. By the Leibniz rule $\partial^\gamma r_\lambda$ is a sum of terms
$\lambda^{|\gamma_1|/2}(\partial^{\gamma_1}(1-\phi))(\lambda^{1/2}y)\,\lambda^{m+|\gamma_2|}(\partial^{
\gamma_2}\check\phi)(\lambda y)$, $\gamma_1+\gamma_2 = \gamma$, supported in $\{|\lambda y|\ge\lambda^{1/2}\}$; with
$|\partial^{\gamma_2}\check\phi(z)|\le C_L\langle z\rangle^{-L}$,
$$\|\partial^\gamma r_\lambda\|_{L^1}\le C\lambda^{|\gamma|}\int_{|z|\ge\lambda^{1/2}}\langle z\rangle^{-L}\,dz\le C_{
\gamma,L}\lambda^{|\gamma|-(L-m)/2},$$
which is at most $C\lambda^{-K}$ for any $K$, choosing $L$. By Young's inequality, $\|\partial^\gamma R_\lambda
v\|_{L^2}\le\|\partial^\gamma r_\lambda\|_{L^1}\|v\|_{L^2}$, so $\|R_\lambda v\|_{H^s}\le C_{s,K}\lambda^{-K}\|v\|_{L^2}$
for all $s$ and $K$, and (3.2) holds for $R_\lambda$, hence for $S^{(0)}_\lambda = M_\lambda-R_\lambda$ and
$I-S^{(0)}_\lambda = (I-M_\lambda)+R_\lambda$.

*Step 2: orthants.* For $\mathbb R^m_l := [0,\infty)^l\times\mathbb R^{m-l}$, $\bar H^s(\mathbb R^m_l)$ is the space of
restrictions of $H^s(\mathbb R^m)$, with the quotient norm. Let $E$ be the composition of Seeley's extension operators
across the hyperplanes $\{x_i = 0\}$, $i\le l$ ([Hin26c] Lemma 8.5, after Seeley; the operator, with infinitely many
reflections, is written out in the proof of II.E Lemma 1.3 (b) and is the one of II.F$'$ Lemma 2.5): each acts in $x_i$
with the other variables as parameters, is bounded $\bar H^s\to\bar H^s$ (one orthant face fewer) for every $s\in\mathbb
N_0$, and is the identity on $\{x_i\ge0\}$; so $E:\bar H^s(\mathbb R^m_l)\to H^s(\mathbb R^m)$ is bounded for every $s$,
$Ev = v$ on $\mathbb R^m_l$, and if $\mathrm{supp}\,v\subset\{x_m\ge a\}$ with $m>l$, then
$\mathrm{supp}\,Ev\subset\{x_m\ge a\}$. Put $S^{(l)}_\lambda v := (S^{(0)}_\lambda Ev)|_{\mathbb R^m_l}$. Then
$\|S^{(l)}_\lambda v\|_{\bar H^s}\le\|S^{(0)}_\lambda Ev\|_{H^s}$, and $v-S^{(l)}_\lambda v$ is the restriction of
$Ev-S^{(0)}_\lambda Ev$; so (3.2) holds for $S^{(l)}_\lambda$ on the spaces $\bar H^s(\mathbb R^m_l)$, with $C$
multiplied by the norm of $E$ on $\bar H^t$. If $\mathrm{supp}\,v\subset\{x_m\ge a\}$, $m>l$, then
$\mathrm{supp}\,S^{(l)}_\lambda v\subset\{x_m\ge a-2\lambda^{-1/2}\}$.

*Step 3: charts at $\{|t|\le c_1\}$.* We use charts $\phi_\alpha:U_\alpha\to\mathbb R^m_{l_\alpha}$ ($m = \dim M$,
$l_\alpha\in\{0,1\}$) of two kinds, in each of which $t$ is the last coordinate $x_m$. (a) Near a point of $M\cap\{|t|\le
c_1\}$ on no face of $\mathcal H_b$: by (T1), $t$ and, at a face $H\in\bar{\mathcal H}$, a defining function $x_1$ of $H$
are part of a coordinate system ($dt|_{TH}\ne0$), giving a chart onto an open subset of $\mathbb R^m_1$, or of $\mathbb
R^m$ away from $\bar{\mathcal H}$, with image in $\{|x_m|<2c_1\}$. (b) Near a point $p$ as in (T2): shrinking $V$,
$(\rho,z,\bar t)$, $\rho := \rho_H$, are coordinates on $V\cong[0,2)\times(-2,2)^{m-2}\times(-a,a)$, and the cells $V_j
:= \{2^{-j-2}<\rho<2^{-j+1}\}$, $j\ge3$, with the coordinates $(x^{(j)},z,\bar t)$, $x^{(j)} := -\log_2\rho-j\in(-1,2)$,
are unit cells of the b-structure: $\rho\partial_\rho$, $\partial_z$, $\partial_{\bar t}$ are constant multiples of the
coordinate fields, uniformly in $j$. As $t-\bar t\in\rho^\epsilon C^\infty_b(V)$, in these coordinates $t-\bar t$ and all
its derivatives are $O(2^{-\epsilon j})$; so for $j\ge j_0$, $(x^{(j)},z,t)$ are coordinates on $V_j$ (shrunk slightly),
with transition maps to $(x^{(j)},z,\bar t)$ bounded in $C^\infty$ uniformly in $j$. The cells with $j<j_0$ lie in a
compact subset of $M'^\circ$, near which charts of kind (a) serve. By compactness of $M\cap\{|t|\le
c_1\}\setminus\bigcup_{H\in\mathcal H_b}\{\rho_H<\rho_1\}$ for small $\rho_1$, finitely many charts of kind (a) and
finitely many families of cells of kind (b) cover $M\cap\{-c_1\le t\le c_1\}$; together they form a family of finite
multiplicity with transition maps uniformly bounded in $C^\infty$, a bounded geometry structure on a neighbourhood $W$ of
that set in the sense of II.A (S1), the b-structure there, and contained in $\{|t|<2c_1\}$. Choose $\chi_\alpha\in
C^\infty_c(U_\alpha)$, uniformly bounded in $C^\infty$ in the chart coordinates, with $\sum_\alpha\chi_\alpha = 1$ on
$M\cap\{-\frac12c_1\le t\le\frac34c_1\}$, and $\tilde\chi_\alpha\in C^\infty_c(U_\alpha)$, likewise uniform, equal to 1
on the $\frac12$-neighbourhood (in the chart coordinates) of $\mathrm{supp}\,\chi_\alpha$ (shrinking the supports of the
$\chi_\alpha$ within the cells if necessary).

*Step 4: the operators.* Let $\psi,\psi_3\in C^\infty(\mathbb R)$ with $\psi = 1$ on $(-\infty,\frac12c_1]$, $\psi = 0$
on $[\frac34c_1,\infty)$, $\psi_3 = 0$ on $(-\infty,\frac18c_1]$ and $\psi_3 = 1$ on $[\frac14c_1,\infty)$; by (T3),
$\psi(t),\psi_3(t)\in C^\infty_b$, so multiplication by them is bounded on every $w\bar H^k_b(M)$. Let $\tilde S_\theta$
be a smoothing operator on all of $w\bar H^0_b(M)$, built in the same way from a bounded geometry cover of a
neighbourhood of $M$ in $M'$ by b-cells and, at the faces of $\bar{\mathcal H}$ and their corners with those of
$\mathcal H_b$, charts onto orthants $\mathbb R^m_l$, with no condition on supports:
$\tilde S_\theta v := \sum_\beta\tilde\chi_\beta\phi_\beta^*S^{(l_\beta)}_\theta((\phi_\beta)_*(\chi_\beta v))$. With
$\lambda := 4\theta/c_0^2$ ($\ge16$), put
$$S_\theta u := \sum_\alpha\tilde\chi_\alpha\phi_\alpha^*S^{(l_\alpha)}_\lambda\big((\phi_\alpha)_*(\chi_\alpha\psi(t)u)
\big)+\psi_3(t)\tilde S_\theta\big((1-\psi(t))u\big),\qquad u\in B^0.\tag{3.3}$$

*Supports.* Let $u\in B^0_\eta$, $\eta\in[\theta^{-1/2},1]$, so $\mathrm{supp}\,u\subset\{t\ge c_0\eta\}$. In the chart
$\phi_\alpha$, $(\phi_\alpha)_*(\chi_\alpha\psi(t)u)$ is supported in $\{x_m\ge c_0\eta\}$, so by Step 2 the
$\alpha$-term is supported in $\{t\ge c_0\eta-2\lambda^{-1/2}\} = \{t\ge c_0(\eta-\theta^{-1/2})\}$. The last term is
supported in $\{t\ge\frac18c_1\} = \{t\ge c_0\}\subset\Omega_{c_0(\eta-\theta^{-1/2})}$. So $S_\theta u\in
B^\infty_{\eta-\theta^{-1/2}}$ when $u\in B^\infty_\eta$. For $u\in B^0$ the same argument gives $\mathrm{supp}\,S_\theta
u\subset\Omega_{-c_0\theta^{-1/2}}$, within the domain of the charts.

*Estimates.* By II.A (S3), on the bounded geometry structure of Step 3 (and on that of $\tilde S_\theta$), the norm of
$w\bar H^k_b(M)$ on functions supported in $W$ is equivalent to $\big(\sum_\alpha
w_\alpha^{-2}\|(\phi_\alpha)_*(\chi_\alpha u)\|^2_{\bar H^k(\mathbb R^m_{l_\alpha})}\big)^{1/2}$, $w_\alpha :=
\sup_{U_\alpha}w$, the weight $w$ being bounded above and below by a fixed multiple of $w_\alpha$ on each cell
(b-weights vary by bounded factors on b-cells), with constants independent of the choice of the uniform family
$\chi_\alpha$. (S3) is stated for charts onto cubes in a manifold without boundary, and the norm of $w\bar H^k_b(M)$ is
a quotient norm, so at the faces of $\bar{\mathcal H}$ two lines are added: the bound of the sum by the norm follows
from (S3) on $M'$ applied to an extension of $u$ with almost minimal norm, and the converse because
$\sum_\alpha\tilde\chi_\alpha\phi_\alpha^*E((\phi_\alpha)_*(\chi_\alpha u))$, with the Seeley operator $E$ of Step 2, is
an extension of $u$ whose norm (S3) bounds by the sum (D213); and multiplication by $\tilde\chi_\alpha$ and the maps
$\phi_\alpha^*$ are uniformly bounded. Hence, with (3.2) for $S^{(l_\alpha)}_\lambda$, $\lambda\le C\theta$, and the
finite multiplicity,
$$\Big|\sum_\alpha\tilde\chi_\alpha\phi_\alpha^*S^{(l_\alpha)}_\lambda((\phi_\alpha)_*(\chi_\alpha\psi u))\Big|_s^2\le C
\sum_\alpha w_\alpha^{-2}\theta^{2(s-t)}\|(\phi_\alpha)_*(\chi_\alpha\psi u)\|^2_{\bar H^t}\le C\theta^{2(s-t)}|
\psi u|_t^2\le C\theta^{2(s-t)}|u|_t^2$$
for $s\ge t$, and the same for $\tilde S_\theta$ and for the product with $\psi_3(t)$. For $s\le t$: $\psi u$ is
supported in $\{0\le t\le\frac34c_1\}$, where $\sum_\alpha\chi_\alpha = 1$, and $\tilde\chi_\alpha\chi_\alpha =
\chi_\alpha$; so $\psi u-\sum_\alpha\tilde\chi_\alpha\phi_\alpha^*S^{(l_\alpha)}_\lambda(\cdots) =
\sum_\alpha\tilde\chi_\alpha\phi_\alpha^*(I-S^{(l_\alpha)}_\lambda)((\phi_\alpha)_*(\chi_\alpha\psi u))$. As $\psi_3 =
1$ on $\mathrm{supp}(1-\psi(t))$, $(1-\psi)u-\psi_3\tilde S_\theta((1-\psi)u) = \psi_3(I-\tilde S_\theta)((1-\psi)u)$.
Adding, and estimating as before with the second inequality of (3.2), $|u-S_\theta u|_s\le C\theta^{s-t}|u|_t$. Finally
$S_\theta u\in\bigcap_kw\bar H^k_b(M)$, every term being smooth with all norms bounded by (3.2) with $t = 0$. $\square$

The weights enter only through the factors $w_\alpha$; this is the weighted case of the source's statement. The source's
Step 3 covers $\{t>0\}$ by charts contained in $\{t>0\}$; the splitting (3.3) by $\psi(t)$ avoids the charts away from
$\{|t|\le c_1\}$, where $t$ need not be a b-smooth coordinate ($t^\flat$ grows like $t_*$ towards $\iota^+$), and needs
no support control there (section 6, (H6)).

## 4. Tame bounds

**Lemma 4.1 ([Hin26c] Lemma 12.8).** Let $l,m,n\in\mathbb N_0$, $D := l+m+n$, $M :=
[0,\infty)^l_\rho\times[0,\infty)^m_x\times\mathbb R^n_y$ with the density
$|\frac{d\rho_1}{\rho_1}\cdots\frac{d\rho_l}{\rho_l}dx\,dy|$, and for $k\in\mathbb N_0$ let $\bar H^k_b(M)$ be the space
of $u\in L^2(M)$ with $(\rho\partial_\rho)^a\partial_x^b\partial_y^cu\in L^2(M)$ for $|a|+|b|+|c|\le k$ (distributional
derivatives on $M^\circ$), $\|u\|_k$ the sum of these $L^2$-norms. Let $d\in\mathbb N$, $d>\frac D2$.

(1) (*Sobolev embedding.*) There is $C_{\mathrm{Sob}}$ with $\|u\|_{L^\infty}\le C_{\mathrm{Sob}}\|u\|_d$.

(2) (*Products.*) For $k\in\mathbb N_0$ there is $C_k$ with $\|uv\|_k\le C_k(\|u\|_d\|v\|_k+\|u\|_{k+d}\|v\|_0)$ for
$u\in\bar H^{k+d}_b(M)$, $v\in\bar H^k_b(M)$.

(3) (*Nonlinear functions.*) Let $\delta>0$ and $F:[-\delta,\delta]\to\mathbb R$ smooth with $F(0) = 0$. For $k\in\mathbb
N_0$ there is $C_k$ with $\|F(u)\|_k\le C_k\|u\|_{k+d}$ for real $u\in\bar H^{k+d}_b(M)$ with
$\|u\|_d\le\delta/C_{\mathrm{Sob}}$.

*Proof.* *Reductions.* In $s_i := -\log\rho_i\in\mathbb R$, $\rho_i\partial_{\rho_i} = -\partial_{s_i}$ and
$\frac{d\rho_i}{\rho_i} = ds_i$, so $\bar H^k_b(M)$ is isometric to the space defined in the same way on
$[0,\infty)^m\times\mathbb R^{n+l}$ with standard derivatives; relabel, $l = 0$. Seeley's extension $E$ across the
hyperplanes $\{x_i = 0\}$ (Step 2 of section 3.2) is bounded from $\bar H^k$ to $H^k(\mathbb R^D)$ for every $k$, with
$Ew = w$ on $M$, the space defined by distributional derivatives on the interior of an orthant being that of
restrictions, with equivalent norms, by this boundedness. As $uv = (Eu\,Ev)|_M$ and $F(u) = F(Eu)|_M$ when
$|Eu|\le\delta$, it suffices to prove (1)-(3) on $\mathbb R^D$, with $\|u\|_k := \sum_{|\gamma|\le k}\|\partial^\gamma
u\|_{L^2}$, and to take for $M$ the constant $C_{\mathrm{Sob}}$ of $\mathbb R^D$ times the norm of $E$ on $\bar H^d$,
which makes $\|u\|_d\le\delta/C_{\mathrm{Sob}}$ imply $\|Eu\|_{L^\infty}\le\delta$.

*(1)* $\|u\|_{L^\infty}\le(2\pi)^{-D}\|\hat
u\|_{L^1}\le(2\pi)^{-D}\|\langle\xi\rangle^{-d}\|_{L^2}\|\langle\xi\rangle^d\hat u\|_{L^2}$, and
$\langle\xi\rangle^{-d}\in L^2$ as $2d>D$; $\|\langle\xi\rangle^d\hat u\|_{L^2}\le C\|u\|_d$ by Plancherel.

*Interpolation.* For $0\le p\le k$, $k\ge1$, and $w\in H^k(\mathbb R^D)$, Hölder's inequality with the exponents $\frac
k{k-p}$, $\frac kp$ gives $\|\,|\xi|^p\hat w\|_{L^2}\le\|\hat w\|_{L^2}^{1-p/k}\|\,|\xi|^k\hat w\|_{L^2}^{p/k}$, and
$\sum_{|\gamma| = p}\|\partial^\gamma w\|_{L^2}$ is bounded above and below by constant multiples of $\|\,|\xi|^p\hat
w\|_{L^2}$; so
$$\sum_{|\gamma| = p}\|\partial^\gamma w\|_{L^2}\le C\|w\|_0^{1-p/k}\|w\|_k^{p/k}.\tag{4.1}$$

*(2)* For $k = 0$, $\|uv\|_0\le\|u\|_{L^\infty}\|v\|_0\le C_{\mathrm{Sob}}\|u\|_d\|v\|_0$. Let $k\ge1$, $|\gamma|\le k$
and $\beta\le\gamma$, $p := |\beta|$, $q := |\gamma|-p\le k-p$. By (1) and (4.1) applied to $\partial^\epsilon u$,
$|\epsilon|\le d$,
$$\|\partial^\beta u\|_{L^\infty}\le C_{\mathrm{Sob}}\sum_{|\epsilon|\le d}\|\partial^\beta\partial^\epsilon u\|_{L^2}
\le C\|u\|_d^{1-p/k}\|u\|_{k+d}^{p/k},$$
and by (4.1), as $q/k\le1-p/k$ and $\|v\|_0\le\|v\|_k$, $\|\partial^{\gamma-\beta}v\|_{L^2}\le
C\|v\|_0^{1-q/k}\|v\|_k^{q/k}\le C\|v\|_0^{p/k}\|v\|_k^{1-p/k}$. So
$$\|\partial^\beta u\,\partial^{\gamma-\beta}v\|_{L^2}\le C(\|u\|_d\|v\|_k)^{1-p/k}(\|u\|_{k+d}\|v\|_0)^{p/k}\le C(\|u
\|_d\|v\|_k+\|u\|_{k+d}\|v\|_0),$$
by $a^{1-\lambda}b^\lambda\le a+b$; the Leibniz rule and the sum over $|\gamma|\le k$ give (2).

*(3)* $|F(s)|\le C|s|$ on $[-\delta,\delta]$, so $\|F(u)\|_0\le C\|u\|_0$. Let $k\ge1$; as $k+d>k+\frac D2$, $u$ has
bounded continuous derivatives of order $\le k$, and for $1\le|\gamma|\le k$, by the chain rule, $\partial^\gamma F(u)$
is a sum of terms $c\,F^{(r)}(u)\partial^{\gamma_1}u\cdots\partial^{\gamma_r}u$ with $1\le r\le|\gamma|$,
$\gamma_1+\dots+\gamma_r = \gamma$ and $p_i := |\gamma_i|\ge1$. $|F^{(r)}(u)|\le C$, and, as in (2),
$\|\partial^{\gamma_i}u\|_{L^\infty}\le C\|u\|_d^{1-p_i/k}\|u\|_{k+d}^{p_i/k}$ for $i\ge2$, and
$\|\partial^{\gamma_1}u\|_{L^2}\le C\|u\|_0^{1-p_1/k}\|u\|_k^{p_1/k}\le C\|u\|_d^{1-p_1/k}\|u\|_{k+d}^{p_1/k}$. So the
term is bounded in $L^2$ by
$$C\|u\|_d^{r-|\gamma|/k}\|u\|_{k+d}^{|\gamma|/k}\le C\|u\|_d^{r-1}\|u\|_{k+d}\le C'\|u\|_{k+d},$$
as $\|u\|_d\le\|u\|_{k+d}$ and $\|u\|_d\le\delta/C_{\mathrm{Sob}}$. $\square$

The source states (3) for $u\in\bar H^k_b(M)$; the bound is in terms of $\|u\|_{k+d}$, which is finite only for $u\in\bar
H^{k+d}_b(M)$ (section 6, (H9)). Its proof of (2) interpolates by iterating an integration by parts; (4.1) is the same
inequality read off the Fourier transform.

## 5. The weights of section 12.1 at n = 4, and what is not carried

### 5.1 The weights

Let $P_0$ be a stationary wave-type operator with $\bar S = 0$ which is 0-admissible with sf-loss 0, as the source proves
for the scalar wave operator on Kerr (Theorem 12.2). Theorem 11.1 (II.F$'$ Theorem 1.1, with $\aleph = \delta = 0$) then
applies for weights with $\alpha_I<-\frac12$ and $\alpha_+<\alpha_I-\frac12$ ((1.3) there), and $\alpha_++2$ must lie in
the indicial gap $(\beta_-,\beta_+)$ of $\hat P_0(0)$ (II.C Definition 2.7 (2)). For the scalar wave operator at $n = 4$
the gap is $(0,2)$, the indicial roots at angular momentum 0 being $0$ and $2$ (II.C, after Definition 2.7); so
$\alpha_+\in(-2,\alpha_I-\frac12)$, and with $\alpha_I = -\frac12-\epsilon_I$, $\alpha_+ = -1-\epsilon_+$,
$$0<\epsilon_I<\epsilon_+<1.\tag{5.1}$$
At $n = 3$ the same reasoning, with the gap shifted to $(-\frac32,-\frac12)$ for $\alpha_+$, gives
$0<\epsilon_I<\epsilon_+<\frac12$; the source's (12.7) prints $0<\epsilon_+<\epsilon_I<\frac12$ (section 6, (H1)). In the
b-weights of II.F$'$ Corollary 1.2, $b_I = \alpha_I+2 = \frac32-\epsilon_I$ and $b_+ = \alpha_++\frac52 =
\frac32-\epsilon_+$, and II.F$'$ (1.8) gives, for $k\ge3$ and forward solutions of $Pu = f$ with $P$ as in II.F$'$
Theorem 1.1 and $f$ in the space (1.4) of II.F$'$, with the density $\mu_b$ of its (1.7),
$$\big|(t_*\partial_{t_*},r\partial_x)^{\le k-3}u\big|\le C\rho_I^{\frac32-\epsilon_I}\rho_+^{\frac32-\epsilon_+}\rho_K^{
\frac12},\tag{5.2}$$
the form at $n = 4$ of the source's (12.8a), whose exponents at $n = 3$ are $1-\epsilon_I$ and $1-\epsilon_+$: at
$\mathscr I^+$, where $\rho_I\sim r^{-1}$ at bounded $t_*$, waves decay nearly like $r^{-3/2}$ in five spacetime
dimensions, against $r^{-1}$ in four.

### 5.2 What is not carried

(a) Theorem 12.2, the 0-admissibility of $\Box_g$ on Kerr, is a four-dimensional statement resting on the mode stability
of Kerr. Its analogue for the scalar wave operator on the five-dimensional background would rest on the scalar mode
stability there, which the route does not use.

(b) Theorem 12.3, mode stability implies 0-admissibility. Its proof assembles Part I's estimates at high, bounded and low
frequencies on the Fourier transform in $t_*$ and closes with a Paley-Wiener argument for the support; at $n = 4$ it is
to be written in Part III together with its version with a loss $\aleph>0$, which the gauge-fixed linearised Einstein
operator needs.

(c) The model problems: Theorem 12.9 (power nonlinearity, $p\ge4$), Remark 12.10, Theorem 12.11 (a quasilinear equation
with spatially compact metric perturbations), Theorem 12.12 (a null form) and Remark 12.13. They are read, and not used
by the route. Their weights are subject to (H1) and (H4) below.

## 6. Findings, and the sources

### 6.1 Findings against the source

(H1) (12.7) prints $0<\epsilon_+<\epsilon_I<\frac12$. Theorem 11.1's condition $\alpha_+<\alpha_I-\frac12$, with
$\alpha_I = -\frac12-\epsilon_I$ and $\alpha_+ = -1-\epsilon_+$, is $\epsilon_+>\epsilon_I$. The same reversal is in
Theorem 12.9 ("$0<\epsilon_+<\min(\frac13,\epsilon_I)$") and Theorem 12.11 ("$0<\epsilon_+<\epsilon_I<\frac12$"): in the
b-weights of (11.5), $\beta_I = 1-\epsilon_I$ and $\beta_+ = 1-\epsilon_+$, and (11.5) requires $\beta_+<\beta_I$, that
is $\epsilon_+>\epsilon_I$ ((11.5), p. 228). In Theorem 12.9 the proof's own conditions (12.23),
$(p-1)(1-\epsilon_I)\ge1$ and $(p-1)(1-\epsilon_+)\ge2$, hold for $p\ge4$ and $\epsilon_I<\epsilon_+\le\frac13$.
(Recorded in II.F$'$ as (F'12).)

(H2) *Withdrawn (D213).* An earlier version said that the source's applications need the support of the solution that
the subspaces $B^k_\eta$ give, which Theorem 12.4 does not state. In the source's (12.21) $B^k_0$ is the whole space, so
the support $t_*\ge1$ used on p. 240 is $u\in B^\infty_0$, which Theorem 12.4 gives, and the better support $t_*\ge2$ is
obtained there by local uniqueness. Theorem 2.1's conclusion $u\in B^\infty_{\eta_0/2}$ is a strengthening, which costs
the closedness of the $B^k_\eta$ (the eighty-ninth verifier's M1).

(H3) Theorem 12.4 asks that $u\in B^\infty_\eta$ imply $\Phi(u)\in F^\infty_\eta$ for all $\eta\in[0,1]$, and separately
that $\Phi(0)\in F^\infty_{\eta_0}$; the first, applied to $u = 0\in B^\infty_1$, forces $\Phi(0)\in F^\infty_1$. Theorem
2.1 (ii) asks the first for $\eta\le\eta_0$ only. In the source's applications $f$ is supported in $\{t_*\ge2\}$, so both
forms hold there, with $\eta_0 = 1$ (D213).

(H4) Theorem 12.12 prints $\beta_+ = -1-\epsilon_+$; its proof uses $\beta_+ = 1-\epsilon_+$ ("$\ell_+\le\beta_+ =
1-\epsilon_+$", p. 243).

(H5) In Step 1 of the proof of Proposition 12.6, $\phi$ equals 1 on $\{|\xi|<1\}$, so its support is not in the unit
ball, and the localiser $\phi(\theta^{1/2}y)$ enlarges supports by
$\sup\{|\xi|:\xi\in\mathrm{supp}\,\phi\}\cdot\theta^{-1/2}$, not by $\theta^{-1/2}$; the factor is absorbed by the choice
$\lambda = 4\theta/c_0^2$ (section 3.2, Step 4).

(H6) Step 3 of the proof of Proposition 12.6 covers $\{t>0\}$ by charts contained in $\{t>0\}$. For the supports to stay
in $\Omega_{c_0(\eta-\theta^{-1/2})}$ for $\eta$ up to 1, such charts must lie in $\{t>c_0\}$, which near $\mathscr I^+$
requires charts small in $t$; and towards $\iota^+$ the function $t^\flat$ is not a b-smooth coordinate
($t_*\partial_{t_*}t^\flat\sim t^\flat$). Section 3.2 splits by a cut-off $\psi(t)$ and smooths the part in
$\{t\ge\frac12c_1\}$ without support control, multiplying back by $\psi_3(t)$.

(H7) *Withdrawn (D213).* Example 12.7 takes $\bar t := t_*-1$ and $t := \bar t_*-1$ (the time function of Lemma 5.16,
here $t^\flat$), and Proposition 12.6 asks for $(t-\bar t)\chi\in\prod_H\rho_H^\epsilon C^\infty_b$ with $\chi = 1$ near
$\bar t^{-1}(0)$. An earlier version said this holds only near $\mathscr I^+$. As $\rho_H^\epsilon$ is bounded below
away from the faces of $\mathcal H_b$, the condition imposes no smallness there, and it holds in Example 12.7 (the
eighty-ninth verifier's M2). (T2) asks for $\bar t$ only near the points of $t^{-1}(0)$ on the faces of $\mathcal H_b$,
which is what the proof uses.

(H8) The proof of Theorem 2.1 needs the constants up to the order $N = 21d+6$; the source quotes $16d^2+43d+24$ from
[SR89] in the form of [Hin24a] Theorem 6.11 (neither read). No later part uses the number; they use Theorem 2.1 only
through the existence of some finite order.

(H9) Lemma 12.8 (3) is stated for $u\in\bar H^k_b(M)$; its bound by $\|u\|_{k+d}$ is finite only for $u\in\bar
H^{k+d}_b(M)$, as in Lemma 4.1 (3). Lemma 12.8 (2) has the same feature, and Lemma 4.1 (2) states $u\in\bar
H^{k+d}_b(M)$.

(H10) *(D304.)* Theorem 12.4 asks the support property of the right inverses at every $u\in U$. Theorem 2.1 (iii) asks it
only at $u\in U\cap B^\infty_\eta$, which is all the proof uses (*Supports*: $u_j\in B^\infty_{\eta_j}$ and $e_j\in
F^\infty_{\eta_j}$), so the conclusion is unchanged. The weaker hypothesis is what the right inverses of [Hin26]'s
nonlinear theorem provide at $n = 4$: at a base point whose tail does not vanish below the level, the boost direction
contributes a source there (III.K Lemma 2.3; verifier 132's A-M1, a gap also of [Hin26]'s Step 3 (3), p. 322).

### 6.2 Sources

[Hin26c] P. Hintz, *(Non-)linear waves on asymptotically flat spacetimes. II*, arXiv:2606.28008v1, section 12 (pp.
233-243), read in the record's text extraction; and (11.4)-(11.5) (p. 228).

[SR89] X. Saint Raymond, *A simple Nash-Moser implicit function theorem*, Enseign. Math. (2) 35 (1989): cited by the
source for Theorem 12.4; not read, and not used: Theorem 2.1 is proved here.

[Hin24a] P. Hintz, Theorem 6.11 and Lemma 6.12: cited by the source for the form of Theorem 12.4 and for Step 1 of
Proposition 12.6; not read, and not used.

[Hin23b] P. Hintz, Lemma 3.33: cited by the source for the proof of Lemma 12.8; not read, and not used.

Seeley's extension enters through the operator written out in the proof of II.E Lemma 1.3 (b) (from [Hin26c] Lemma
8.5), as in II.F$'$ Lemma 2.5; the bounded geometry
Sobolev spaces through II.A (S1)-(S3), READ in [SBG].

### 6.3 The verifier's findings, and the repairs (D213)

The eighty-ninth verifier read this part line by line and redid the exponent algebra of section 2 by machine (24
identities and inequalities, all holding): Theorem 2.1 is a complete proof, and Proposition 3.1 and Lemma 4.1 are correct
up to presentational gaps. No major finding; five minor findings and nine nits, seated here. (1) (H2) misread the
source: its $B^k_0$ is the whole space, so the support it uses is the conclusion $u\in B^\infty$ of Theorem 12.4;
withdrawn, and Theorem 2.1's conclusion is described as a strengthening. (2) (H7) misread the source: its hypothesis
imposes no smallness away from the faces of $\mathcal H_b$ and holds in Example 12.7; withdrawn. (3) The first clause of
(T3) was false in Example 3.2 (the corner of $\mathscr I^+$ with $\{t_* = \frac12\}$) and unused; deleted. (4) The norm
equivalence in Step 4 of the proof of Proposition 3.1 was attributed to II.A (S3), which covers no orthant charts; the
two lines it needs are added, with the Seeley operator. (5) Example 3.2 asserted that its spaces are those of II.F$'$
(1.2); the equivalence of the two quotient norms is now argued, with II.F$'$ Lemma 2.5. Of the nits: the Seeley operator
is cited to the proof of II.E Lemma 1.3 (b) and to II.F$'$ Lemma 2.5; $t$ is defined on all of $M'$ in Example 3.2;
the covers of Step 4 are of a neighbourhood of $M$; $r'_0-1>r_0$ is cited to the proof of II.C Lemma 3.2; (5.2)'s
source space is (1.4) of II.F$'$; (H3) no longer says that the source's applications provide (ii) only for
$\eta\le\eta_0$ (they have $\eta_0 = 1$); (H9) notes Lemma 12.8 (2); (T2) takes the closure of $\{|t|\le c_1\}$; and
II.F$'$ names how $P$ acts on its uniqueness class. The verifier also confirmed the D212 repairs to Parts II.E, II.F
and II.F$'$.
