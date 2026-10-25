# Part II.A. Compactifications, Lie algebras and the microlocal toolkit on spacetime, at n = 4

*Status.* Written out in full (D192). Read line by line by the seventy-eighth verifier, whose two major findings, seven
minor findings and nits are seated in place (D194): the hypothesis of (L4) on the order, and the choice of operators in
the proof of Proposition 9.9. The seventy-ninth verifier read those repairs and confirmed each (D195), and the wording of
(S8) was then aligned with [SBG] Definition 4.6 (D195). The eightieth verifier confirmed the rewording and asked for the
reading of the theorem it cites to be stated, which (S8) now does (D196). Nothing here is labelled proved until Part
II.A$'$, which proves two of its inputs, is proved; the D196 wording of (S8) is read with it. This part proves, at
spatial dimension $n = 4$, the geometric and analytic setup of [Hin26c] sections 2 and 3, on which its sections 7, 8, 10,
11 and 13 rest. The source is [Hin26c] = P. Hintz, arXiv:2606.28008v1 (printed page = PDF page $-4$). The
pseudodifferential calculus is that of [SBG] = P. Hintz, *Pseudodifferential operators on manifolds with scaled bounded
geometry*, Commun. Amer. Math. Soc. 6 (2026), 153-243, arXiv:2408.06651v1, whose statements are READ here (section 3) and
hold on manifolds of every dimension; inside [Hin26c] that paper is cited as "[Hin26c]", and below it is always [SBG].
Two statements are standing inputs, not proved here: the elliptic and real principal type estimates without b-regularity,
for coefficients of finite regularity and variable orders ((L3)-(L4) of section 9.1), which the source cites as standard
and no text READ here states. They are proved in Part II.A$'$ (`PART-II-A2-STANDARD.md`, written, D193), with the
hypotheses of (L4) corrected ((G6)-(G7) there and in section 10); Part II.A is labelled proved only with it. Parts
I.A-I.C are `PART-I-SPECTRAL.md`, `PART-I-B-HIGHENERGY.md` and `PART-I-C-LOWENERGY.md`.

*What changes at n = 4.* The spacetime is $\mathbb R^{1+4}$ and the sphere of directions is $\mathbb S^3$, so every
construction of [Hin26c] section 2 is repeated with $\mathbb S^3$ for $\mathbb S^2$, and the proofs are unchanged (none
uses the dimension). Dimension enters through the volume density $|dt\,dx|$ in the $L^2$-spaces. Near $\iota^+$,
$|dt\,dx| = t_*\langle x\rangle^n$ times a b-density, and $t_*^{-1}\langle x\rangle^{-n}$ is a smooth positive multiple
of $x_I^{2n}\rho_+^{n+1}\rho_K$. So the weights $(2(\alpha_I+\frac32),\alpha_++2,\alpha_K+\frac12)$ of [Hin26c] (3.57),
Lemma 3.14 and Lemma 3.22 become $(2(\alpha_I+2),\alpha_++\frac52,\alpha_K+\frac12)$ (Lemmas 6.1, 6.2 and 8.8 below).
The Sobolev embedding $H^{d+3}\hookrightarrow C^d$ used there holds on $\mathbb R^5$ as well ($3>\frac52$). Section 10
lists what the write-out found.

*How it is organised.* Sections 1-2: the compactified spacetime and its Lie algebras of vector fields, with the
commutator lemmas behind b-regularity. Section 3: the statements of [SBG] that are used, READ. Section 4: the
e3b-calculus and its spaces. Sections 5-6: the Fourier transform near $K^+$ and the Mellin transform at $\iota^+$.
Section 7: supported and extendible spaces. Section 8: $L^\infty$-spaces, operators with coefficients of limited
regularity, Sobolev embedding. Section 9: elliptic and real principal type estimates on e3b-spaces with b-regularity,
and their tame versions. Section 10: findings.

## 1. Compactifications

Write $z = (t,x)\in\mathbb R^{1+4}$, $x = r\omega$, $r = |x|$, $\omega\in\mathbb S^3$, $\rho := r^{-1}$, and fix $r_0>0$
(in applications, the radius of the artificial boundary inside the horizon, as in I.A section 1.1).

*Radial compactification.* For $N\ge1$, $\overline{\mathbb R^N} := (\mathbb R^N\sqcup[0,\infty)_\varrho\times\mathbb
S^{N-1})/\sim$, with $Z = R\varpi\sim(\varrho,\varpi) = (R^{-1},\varpi)$ for $Z\ne0$ ([Hin26c] (2.1)). A linear
isomorphism $L$ of $\mathbb R^N$ extends to a diffeomorphism of $\overline{\mathbb R^N}$: in the coordinates
$(\varrho,\varpi)$ near the boundary, $L(\varpi/\varrho) = |L\varpi|\varpi'/\varrho$ with $\varpi' = L\varpi/|L\varpi|$,
so $L$ acts by $(\varrho,\varpi)\mapsto(\varrho/|L\varpi|,L\varpi/|L\varpi|)$, smooth with smooth inverse since
$|L\varpi|$ is bounded above and below on $\mathbb S^{N-1}$.

**Definition 1.1 (the spatial manifold; [Hin26c] Definition 2.1 at n = 4).** $\tilde X := \overline{\mathbb R^4}$, $X :=
\{r\ge r_0\}\subset\tilde X$, with boundary hypersurfaces $\partial_\sharp X := \{r = r_0\}$ and $\partial X := \{\rho =
0\}$. This is $\bar X$ of I.A section 1.1.

**Definition 1.2 (spacetime compactifications; [Hin26c] Definition 2.2).** Let $k_\pm\in\partial\overline{\mathbb
R^{1+4}}$ be the limit points of $(\pm t,0)$, $t\to\infty$ (in projective coordinates $\frac1{\pm t}$, $\frac x{\pm t}$
near $k_\pm$: $k_\pm = \{\frac1{\pm t} = 0, \frac x{\pm t} = 0\}$), and $Y^+ := \{\frac1t = 0, \frac{r-t}t = 0\}
\subset\partial\overline{\mathbb R^{1+4}}$, the light cone at future infinity, a smooth submanifold diffeomorphic to
$\mathbb S^3$.

(1) $\tilde M_0 := [\overline{\mathbb R^{1+4}};k_+,k_-]$, with boundary hypersurfaces sf (the lift of
$\partial\overline{\mathbb R^{1+4}}$) and $K^\pm$ (the lifts of $k_\pm$).

(2) $\tilde M_1 := [\tilde M_0;Y^+]$, with boundary hypersurfaces $\mathscr I^+_1$ (the front face), $K^\pm$,
$\iota^+_1$ (the closure of $\{\frac rt\in(0,1),\frac1t = 0\}$) and $I^0_1$ (the closure of $\{\frac tr<1,\frac1r =
0\}$); $\tilde M := [\tilde M_1;\mathscr I^+_1,\frac12]$, the square root blow-up of $\mathscr I^+_1$ (a square root of
a defining function of $\mathscr I^+_1$ is declared a defining function of its lift). Its boundary hypersurfaces are
null infinity $\mathscr I^+$, the Kerr faces $K^\pm$ (named as in the source; here the faces of the black hole region),
future timelike infinity $\iota^+$ and spacelike infinity $I^0$, with (local) defining functions $x_I$, $\rho_K$,
$\rho_+$, $\rho_0$; $\rho_I := x_I^2$ is a defining function of $\mathscr I^+_1$.

(3) $M_0$, $M_1$, $M$ are the closures of $\{r\ge r_0\}$ in $\tilde M_0$, $\tilde M_1$, $\tilde M$.

**Definition 1.3 (domains; [Hin26c] Definition 2.3).** $\tilde\Omega^\sharp := \mathrm{cl}_{\tilde M}\{t\ge0\}$,
$\Omega^\sharp := \tilde\Omega^\sharp\cap M$, $\Omega := \mathrm{cl}_M\{t-r\ge1\}$.

*Coordinates* ([Hin26c] (2.8)-(2.12)), with $t_* := t-r$ and $v := \frac{t-r}r = \rho t_*$. (A) In $M^\circ$: $(t,x)$,
$(t,r,\omega)$ or $(t_*,r,\omega)$. (B) Near the interiors: of $K^+$, $(\frac1t,x)$ or $(\frac1{t_*},x)$; of $\iota^+$,
$(v,\rho_+ = \frac1{t_*},\omega)$ or $(v,\frac1r,\omega)$; of $\mathscr I^+$, $(t-r,r^{-1/2},\omega)$; of
$I^0\cap\{t\ge0 \}$, $(\frac{r-t}r,\frac1r,\omega)$. (C) Near the corners: $I^0\cap\mathscr I^+$ ($t-r<2$): $\rho_0 =
\frac1{r-t+2}$, $x_I = (\frac{r-t+2}r)^{1/2}$; $\mathscr I^+\cap\iota^+$ ($t-r>0$): $\rho_+ = \frac1{t-r}$, $x_I =
(\frac{t-r}r)^{1/2} = \sqrt v$; $\iota^+\cap K^+$: $\rho_+ = \frac1r$, $\rho_K = \frac rt$; always with
$\omega\in\mathbb S^3$.

These are the projective coordinates of the blow-ups. For instance, near $k_+$ the functions $s := \frac1t$ and $y :=
\frac xt$ are coordinates on $\overline{\mathbb R^{1+4}}$, $k_+ = \{s = 0,y = 0\}$; on $[\overline{\mathbb
R^{1+4}};k_+]$ the projective coordinates $(s,y/s) = (\frac1t,x)$ cover the interior of the front face $K^+$, and
$(|y|,s/|y|,y/|y|) = (\frac rt,\frac1r,\omega)$ cover its corner with sf. Near $Y^+$ in sf$^\circ$,
$(\frac1r,\frac{t-r}r = v,\omega)$ are coordinates and $Y^+ = \{\frac1r = 0,v = 0\}$; the projective coordinates of
$[\tilde M_0;Y^+]$ near the corner of $\mathscr I^+_1$ with $\iota^+_1$ are $(v,\frac1{rv} = \frac1{t-r},\omega)$, and
the square root blow-up replaces $v$ by $x_I = \sqrt v$. The other charts are obtained in the same way.

The blow-down map realises $\mathscr I^+$ as the total space of a fibration $\overline{\mathbb R}\to\mathscr I^+\to Y^+
= \mathbb S^3$, the fibres having interiors $\{t-r\in\mathbb R, r^{-1/2} = 0,\omega = \omega_0\}$ ([Hin26c] (2.13)).

*Explicit defining functions on $\Omega$* ([Hin26c] Remark 2.4): $x_I = (\frac{t_*}{t_*+r})^{1/2}$, $\rho_+ =
\frac{t_*+r}{t_*r}$, $\rho_K = \frac r{t_*+r}$. Indeed, on $\Omega$, $t_*\sim\rho_+^{-1}\rho_K^{-1}$, $r\sim x_I^{-2}
\rho_+^{-1}$ and $t_*+r\sim x_I^{-2}\rho_+^{-1}\rho_K^{-1}$ (quotients positive and smooth), and the stated expressions
solve these relations.

## 2. Lie algebras of vector fields

### 2.1 Scattering and b-structures

The scattering tangent bundle ${}^{\mathrm{sc}}T\overline{\mathbb R^N}$ is $\overline{\mathbb R^N}\times\mathbb R^N$,
identified with $T\mathbb R^N$ over $\mathbb R^N$ by $(z,v)\mapsto v^\mu\partial_{z^\mu}$; $\mathcal V_{\mathrm{sc}}
(\overline{\mathbb R^N}) := C^\infty(\overline{\mathbb R^N};{}^{\mathrm{sc}}T\overline{\mathbb R^N})$. In the projective
chart $\rho_1 = \frac1{z^1}$, $\hat z^i = \frac{z^i}{z^1}$ ($z^1>0$), $\partial_{z^1} = \rho_1(-\rho_1
\partial_{\rho_1}-\sum_{i\ge2}\hat z^i\partial_{\hat z^i})$ and $\partial_{z^i} = \rho_1\partial_{\hat z^i}$; so
$\mathcal V_{\mathrm{sc}}(\overline{\mathbb R^N}) = \rho\mathcal V_b(\overline{\mathbb R^N})$, $\rho$ a boundary
defining function, where $\mathcal V_b$ is the space of smooth vector fields tangent to the boundary, spanned by
$\partial_{z^\mu}$ and $z^\mu\partial_{z^\nu}$. On a manifold with corners, $\mathcal V_b$ is the space of smooth vector
fields tangent to every boundary hypersurface. The Minkowski metric $\bar g = -dt^2+dx^2$ lies in
$C^\infty(\overline{\mathbb R^{1+4}};S^2\,{}^{\mathrm{sc}}T^*\overline{\mathbb R^{1+4}})$. $\mathcal T\to\tilde M_0,
\tilde M_1,\tilde M$ denotes the pullback of ${}^{\mathrm{sc}}T\overline{\mathbb R^{1+4}}$ along the blow-down maps
([Hin26c] Definition 2.6). $\mathcal V_b(\tilde M)$ and $\mathcal V_{\mathrm{sc}}$ are Lie algebras, and
$\mathrm{Diff}^m _b$, $\mathrm{Diff}^m_{\mathrm{sc}}$ are the spaces of up to $m$-fold compositions of their elements,
with smooth coefficients. For a boundary hypersurface $H$ with a collar $[0,\epsilon)_{\rho_H}\times H$, the b-normal
field $\rho_H\partial_{\rho_H}$ is independent of the collar modulo $\rho_H\mathcal V_b$.

*Spanning sets* ([Hin26c] Example 2.9). Near $(K^+)^\circ$ (coordinates $\rho_K = \frac1t$, $x$): $t\partial_t =
-\rho_K\partial_{\rho_K}$, $\partial_x$. Near $K^+\cap\iota^+$ ($\rho_+ = \frac1r$, $\rho_K = \frac rt$): $-\rho_+
\partial_{\rho_+} = t\partial_t+r\partial_r$, $-\rho_K\partial_{\rho_K} = t\partial_t$, $\partial_\omega$. Near
$\mathscr I^+_1\cap\iota^+_1$ ($\rho_+ = \frac1{t-r}$, $\rho_I = \frac{t-r}r$): $-\rho_+\partial_{\rho_+} = t\partial_t
+r\partial_r$, $\rho_I\partial_{\rho_I}-\rho_+\partial_{\rho_+} = (t-r)\partial_t$, $\partial_\omega$, and one may use
$-\rho_I\partial_{\rho_I} = r(\partial_t+\partial_r)$ in place of the first. On $\Omega$, $r\partial_x$, $t_*\partial
_{t_*}$ form a global frame (in the coordinates $(t_*,x)$). Each follows from the chain rule in the charts of section 1.

### 2.2 3b-structures

**Definition 2.1 ([Hin26c] Definition 2.10).** ${}^{3b}T\tilde M_0 := \tilde M_0\times\mathbb R^5$, identified with
$T\mathbb R^{1+4}$ over $\mathbb R^{1+4}$ by $(z,v)\mapsto v^\mu\langle x\rangle\partial_{z^\mu}$ (over $M_0$
equivalently $v^\mu r\partial_{z^\mu}$); $\mathcal V_{3b}(\tilde M_0)$ is its space of smooth sections, $\mathrm{Diff}
^m_{3b}(\tilde M_0)$ the space of up to $m$-fold compositions.

$\bar g = r^2(-(\frac{dt}r)^2+(\frac{dr}r)^2+\slashed g)\in r^2C^\infty(\tilde M_0;S^2\,{}^{3b}T^*\tilde M_0)$, with
$\bar g^{-1} = r^{-2}(-(r\partial_t)^2+(r\partial_r)^2+\slashed g^{-1})$ ([Hin26c] (2.20)). Near $K^+\cap\mathrm{sf}$,
with $\rho_K = \frac rt$, $\rho_+ = \frac1r$: $r\partial_t = -\rho_K^2\partial_{\rho_K}$, $r\partial_r = \rho_K
\partial_{\rho_K}-\rho_+\partial_{\rho_+}$. Hence $\mathcal V_{3b}\subset\mathcal V_b$, $\rho_K\mathcal V_b\subset
\mathcal V_{3b}$ (as $\rho_Kt\partial_t = r\partial_t$), and $[r\partial_r,r\partial_t] = r\partial_t$ shows that
$\mathcal V_{3b}$ is a Lie algebra. A b-vector field $V$ lies in $\mathcal V_{3b}$ if and only if $Vt\in t\rho_K
C^\infty$ near $K^+$ (the coefficient of $t\partial_t$ must lie in $\rho_KC^\infty$). Away from $K^+$, 3b- and b-vector
fields coincide, and ${}^{3b}T\tilde M|_{\tilde M\setminus(K^+\cup\mathscr I^+)} = {}^bT\tilde M|_{\tilde M\setminus
(K^+\cup\mathscr I^+)}$ ([Hin26c] (2.21)).

**Lemma 2.2 (commutators with time dilations; [Hin26c] Lemma 2.11).** Let $V\in\mathcal V_b(\tilde M_0)$ with
$V-t\partial_t\in\rho_K\mathcal V_b(\tilde M_0)$ near $K^+$, and $W\in\mathcal V_{3b}(\tilde M_0)$. Then $[V,W] =
\rho_Kw^\flat V+\rho_KW^\sharp$ with $w^\flat\in C^\infty(\tilde M_0)$, $W^\sharp\in\mathcal V_{3b}(\tilde M_0)$; in
particular $[V,W]\in\mathcal V_{3b}$. If
$W\in\rho_{\mathrm{sf}}^{-\alpha_{\mathrm{sf}}}\rho_K^{-\alpha_K}\mathrm{Diff}^m _{3b}(\tilde M_0)$, then $[V,W]$ lies
in the same space; and if $\alpha_K = 0$, $[V,W] = \rho_KW^\flat V+\rho_KW^\sharp$ with
$W^\flat\in\rho_{\mathrm{sf}}^{-\alpha_{\mathrm{sf}}}\mathrm{Diff}^{m-1}_{3b}$, $W^\sharp\in\rho_{\mathrm{sf}}^{
-\alpha_{\mathrm{sf}}}\mathrm{Diff}^m_{3b}$. The same holds on a smooth vector bundle $E$, with $V\in\mathrm{Diff}^1_b$,
$V-\nabla_{t\partial_t}\in\rho_K\mathrm{Diff}^1_b$ for a smooth connection $\nabla$.

(The source prints $W^\sharp\in\mathrm{Diff}^m_{3b}$ in the weighted case; section 10, (G1).)

*Proof.* Only the corner $K^+\cap\mathrm{sf}$ needs an argument; there take $\rho_K = \frac rt$, and note $Vf\in\rho_K
C^\infty$ for $f\in C^\infty$, since by hypothesis $V\equiv-\rho_K\partial_{\rho_K}$ modulo $\rho_K\mathcal V_b$, which
is $t\partial_t$, and $t\partial_tf = -\rho_K\partial_{\rho_K}f\in\rho_KC^\infty$. If the claim holds for $W$, it holds
for $fW$: $[V,fW] = f[V,W]+(Vf)W$, and $(Vf)W\in\rho_K\mathcal V_{3b}$. So it suffices to take
$W\in\{r\partial_t,r\partial _r,\partial_\omega\}$, which span $\mathcal V_{3b}$ there. For $V = t\partial_t$:
$[t\partial_t,r\partial_t] = -r \partial_t = -\rho_Kt\partial_t$, $[t\partial_t,r\partial_r] = 0$,
$[t\partial_t,\partial_\omega] = 0$; this is the claim with $w^\flat\in\{-1,0\}$, $W^\sharp = 0$. In general $V =
t\partial_t+\rho_K(at\partial_t+V')$ with $a\in C^\infty$ and $V'$ in the $C^\infty$-span of
$r\partial_r,\partial_\omega$ (so $V'\in\mathcal V_{3b}$). Then $[V,W] = (1+\rho_Ka)[t
\partial_t,W]-(W(\rho_Ka))t\partial_t+[\rho_KV',W]$. The last term lies in $\rho_K\mathcal V_{3b}$ (as $W\rho_K\in
\rho_KC^\infty$ for $W\in\mathcal V_{3b}\subset\rho_K^0\mathcal V_b$, $\rho_K$ being a defining function of a face to
which $W$ is tangent). The middle term is $\rho_Kft\partial_t$ with $f\in C^\infty$, which equals $\rho_KfV$ modulo
$\rho_K^2 \mathcal V_b\subset\rho_K\mathcal V_{3b}$. The first is $(1+\rho_Ka)(\rho_Kw^\flat
t\partial_t+\rho_KW^\sharp)$, and replacing $t\partial_t$ by $V$ costs $\rho_K^2\mathcal V_b\subset\rho_K\mathcal
V_{3b}$. For operators, write $W = wW_0$, $w = \rho_{\mathrm{sf}}^{-\alpha_{\mathrm{sf}}}\rho_K^{-\alpha_K}$,
$W_0\in\mathrm{Diff}^m_{3b}$; $[V,W_0]\in \mathrm{Diff}^m_{3b}$ by expanding $W_0$ into products of 3b-vector fields, and
$[V,w]\in wC^\infty$ for every b-vector field $V$, so $[V,W] = w[V,W_0]+[V,w]W_0\in w\mathrm{Diff}^m_{3b}$. If $\alpha_K
= 0$, take $\rho_{\mathrm{sf}} = \langle x\rangle^{-1}$, and first $V = t\partial_t$; then $V$ commutes with
$\rho_{\mathrm{sf}}$, so $[V,W] = w[V,W_0]$, and commuting $V$ through each product of 3b-vector fields to the right,
using the vector field case and $[V,f]\in\rho_K C^\infty$, gives the form claimed, with $W^\flat\in
w\mathrm{Diff}^{m-1}_{3b}$ and $W^\sharp\in w\mathrm{Diff}^m_{3b}$. For general $V = (1+\rho_Ka)t\partial_t+\rho_KV'$ as
above, $[V,W] = (1+\rho_Ka)[t\partial_t,W]-[W,\rho_Ka]\,t\partial_t+[\rho_KV',W]$. Here
$[W,\rho_Ka]\in\rho_Kw\mathrm{Diff}^{m-1}_{3b}$, as 3b-vector fields map $\rho_KC^\infty$ to itself, and $[\rho_KV',W] =
\rho_K[V',W]-[W,\rho_K]V'\in\rho_Kw\mathrm{Diff}^m_{3b}$, as $\mathcal V_{3b}$ is a Lie algebra and $V'w\in wC^\infty$.
Substituting $t\partial_t = (1+\rho_Ka)^{-1}(V-\rho_KV')$ in the first two terms, with the case $V = t\partial_t$ for
$[t\partial_t,W]$, gives the form claimed. (The source's proof asserts instead $[\rho_K\mathcal
V_b,w\mathrm{Diff}^m_{3b}]\subset\rho_Kw\mathrm{Diff}^m_{3b}$, which is false: $[r\partial_t,r\partial_r] = -r\partial_t
= -\rho_Kt\partial_t$; section 10.) For bundles, in a local trivialisation $\nabla_{t\partial_t}$ is $t\partial_t$
componentwise plus a term in $\rho_KC^ \infty(\mathrm{End}E)$ (as $t\partial_t = -\rho_K\partial_{\rho_K}$), whose
commutators with $w\mathrm{Diff}^m_{3b}$ lie in $\rho_Kw\mathrm{Diff}^{m-1}_{3b}$. $\square$

$V$ in Lemma 2.2 can be taken to be $t_*\partial_{t_*}$ in the coordinates $(t_*,r)$, which equals $(1-\rho_K)t
\partial_t$.

**Corollary 2.3 ([Hin26c] Corollary 2.12).** The 3b-commutator b-vector fields, that is, $W\in\mathcal V_b(\tilde M_0)$
with $[W,V]\in\mathcal V_{3b}$ for all $V\in\mathcal V_{3b}$, span $\mathcal V_b(\tilde M_0)$ over $C^\infty$.

*Proof.* Near $K^+$, $t\partial_t$ is one by Lemma 2.2, and $\langle x\rangle\partial_{z^\mu}$ are trivially ones; their
$C^\infty$-span is $\mathcal V_b$ near $K^+$ by the spanning sets of section 2.1. Away from $K^+$, $\mathcal V_{3b} =
\mathcal V_b$. $\square$

### 2.3 Edge-b-structures

In $\rho_+ = \frac1{t_*}$, $x_I = (\frac{t_*}r)^{1/2}$ near $\mathscr I^+\cap\iota^+$, so $t_* = \rho_+^{-1}$, $r =
\rho_+^{-1}x_I^{-2}$,

$$dt_* = -\rho_+^{-1}\tfrac{d\rho_+}{\rho_+},\quad dr = -\rho_+^{-1}x_I^{-2}\big(\tfrac{d\rho_+}{\rho_+}+2\tfrac{dx_I}
{x_I}\big),\quad\partial_{t_*} = \rho_+\big(-\rho_+\partial_{\rho_+}+\tfrac12x_I\partial_{x_I}\big),\quad\partial_r =
-\tfrac12\rho_+x_I^2\cdot x_I\partial_{x_I},$$

and $\bar g = -dt_*^2-2dt_*dr+r^2\slashed g$ becomes $2x_I^{-2}\rho_+^{-2}(-\frac{d\rho_+}{\rho_+}\otimes_s[(1+\frac12
x_I^2)\frac{d\rho_+}{\rho_+}+2\frac{dx_I}{x_I}]+\frac{\slashed g}{2x_I^2})$, as $r = \rho_+^{-1}x_I^{-2}$ ([Hin26c]
(2.26)-(2.27), whose bracket prints $\frac{\slashed g}{x_I^2}$; section 10); these are dimension-free computations,
$\slashed g$ the round metric on $\mathbb S^3$.

**Definition 2.4 ([Hin26c] Definition 2.13).** $\mathcal V_{eb}(\tilde M)$ is the space of b-vector fields on $\tilde M$
tangent to the fibres of the fibration of $\mathscr I^+$ (section 1); ${}^{eb}T\tilde M$ is the bundle with $\mathcal
V_{eb} = C^\infty(\tilde M;{}^{eb}T\tilde M)$, and $\mathrm{Diff}^m_{eb}$ is defined as before. A local frame near
$\mathscr I^+\cap\iota^+$ is $\rho_+\partial_{\rho_+}$, $x_I\partial_{x_I}$, $x_I\partial_\omega$ (with
$\partial_\omega$ the coordinate fields of a chart of $\mathbb S^3$), dual to $\frac{d\rho_+}{\rho_+}$,
$\frac{dx_I}{x_I}$, $\frac{d\omega} {x_I}$. Thus $\bar g\in\rho_0^{-2}x_I^{-2}\rho_+^{-2}C^\infty(\tilde M\setminus
K^+;S^2\,{}^{eb}T^*\tilde M)$, and ${}^{eb}T\tilde M = {}^bT\tilde M$ away from $\mathscr I^+$.

**Lemma 2.5 ([Hin26c] Lemma 2.14).** Near $\mathscr I^+$ (writing $d\omega$ for a 1-form on $\mathbb S^3$), $\rho_0^{-2}
x_I^{-2}\rho_+^{-2}C^\infty(\tilde M;S^2\,{}^{eb}T^*\tilde M)$ is spanned by $x_I^{-2}dt_*^2$, $dt_*\otimes_sdr$,
$x_I^{-1}dt_*\otimes_sr\,d\omega$, $x_I^2dr^2$, $x_Idr\otimes_sr\,d\omega$, $r\,d\omega\otimes_sr\,d\omega$; and, with
$x^0 = t+r$, $x^1 = t-r$, by $x_I^2(dx^0)^2$, $dx^0\otimes_sdx^1$, $x_Idx^0\otimes_sr\,d\omega$, $x_I^{-2}(dx^1)^2$,
$x_I^{-1}dx^1\otimes_sr\,d\omega$, $r\,d\omega\otimes_sr\,d\omega$.

*Proof.* By the formulas above, $x_I^{-1}dt_*$, $x_Idr$, $r\,d\omega$ span $\rho_+^{-1}x_I^{-1}C^\infty(U;{}^{eb}T^*
\tilde M)$ on a neighbourhood $U$ of $\mathscr I^+$ away from $K^+$ and $r = 0$, as do $x_Idx^0$, $x_I^{-1}dx^1$, $r\,d
\omega$ (using $dx^0 = dt_*+2dr$: $x_Idx^0 = -\rho_+^{-1}x_I^{-1}((2+x_I^2)\frac{d\rho_+}{\rho_+}+4\frac{dx_I}{x_I})$,
$x_I^{-1}dx^1 = -\rho_+^{-1}x_I^{-1}\frac{d\rho_+}{\rho_+}$, $r\,d\omega = \rho_+^{-1}x_I^{-1}\cdot x_I^{-1}d\omega$);
take symmetric products. Near $\mathscr I^+\cap I^0$ the same computation applies with $\rho_0$ in place of $\rho_+$.
$\square$

**Lemma 2.6 ([Hin26c] Lemma 2.15).** Let $W\in\mathcal V_{eb}(\tilde M)$. Near $\mathscr I^+\cap\iota^+$, $[W,\rho_+
\partial_{\rho_+}]$, $[W,x_I\partial_{x_I}]$, $[W,\partial_\omega]\in\mathcal V_{eb}$. More generally, if $V\in\mathcal
V_b(\tilde M)$ is such that, for each $\omega\in\mathbb S^3$, the pushforward to $T_\omega\mathbb S^3$ of $V$ at the
point $(t_*,0,\omega)$ of $\mathscr I^+$ does not depend on $t_*$, then $[V,W]\in\mathcal V_{eb}$ for all $W\in\mathcal
V_{eb}$, and $[V,W]\in\mathrm{Diff}^m_{eb}$ (weighted: in the same weighted space) for $W\in\mathrm{Diff}^m_{eb}$.

*Proof.* $\mathcal V_{eb}$ is a Lie algebra containing $\rho_+\partial_{\rho_+}$, $x_I\partial_{x_I}$, so only
$[\partial _\omega,W]$ needs proof. It lies in $\mathcal V_{eb}$ for $W = \rho_+\partial_{\rho_+}$, $x_I\partial_{x_I}$
and $W = x_I W'$ with $W'$ a vector field on $\mathbb S^3$; and $[fW,\partial_\omega] =
f[W,\partial_\omega]-(\partial_\omega f)W$. For the second part, write $V =
a\rho_+\partial_{\rho_+}+bx_I\partial_{x_I}+c\partial_\omega$ with $c|_{\mathscr I^+}$ constant on fibres, so $Wc\in
x_IC^\infty$ for $W\in\mathcal V_{eb}$ (which is tangent to the fibres), and $[W,c\partial _\omega] =
(Wc)\partial_\omega+c[W,\partial_\omega]\in\mathcal V_{eb}$ since $x_I\partial_\omega\in\mathcal V_{eb}$. For operators
expand into products. $\square$

**Corollary 2.7 ([Hin26c] Corollary 2.16).** The eb-commutator b-vector fields $\mathcal V_{b,[eb]}(\tilde M)$ (those
$W\in\mathcal V_b$ with $[V,W]\in\mathcal V_{eb}$ for all $V\in\mathcal V_{eb}$) span $\mathcal V_b(\tilde M)$ over
$C^\infty$: near $\mathscr I^+$ the fields of Lemma 2.6 span $\mathcal V_b$. $\square$

### 2.4 e3b-structures

**Definition 2.8 ([Hin26c] Definition 2.17).** ${}^{e3b}T\tilde M$ is ${}^{3b}T\tilde M_0$ over $\tilde
M\setminus\mathscr I^+ = \tilde M_0\setminus Y^+$ and ${}^{eb}T\tilde M$ over $\tilde M\setminus K^+$, glued over
$\tilde M\setminus(K^+\cup \mathscr I^+)$ by the identity of $T\mathbb R^{1+4}$ (which is how both are identified with
${}^bT$ there). Equivalently, $\mathcal V_{e3b}(\tilde M)$ is the space of b-vector fields tangent to the fibres of
$\mathscr I^+$ with $Vt\in t\rho_K C^\infty$ near $K^+$. $\mathrm{Diff}^m_{e3b}$ is defined as before. On $\Omega$,
$\bar g\in\rho_0^{-2}x_I^{-2}\rho_+^{-2} C^\infty(\Omega;S^2\,{}^{e3b}T^*\tilde M)$ and $\bar
g^{-1}\in\rho_0^2x_I^2\rho_+^2C^\infty(\Omega;S^2\,{}^{e3b}T\tilde M)$.

**Lemma 2.9 (good spanning sets; [Hin26c] Lemma 2.18).** $\mathcal V_b(\tilde M)$ is spanned over $C^\infty$ by the
e3b-commutator b-vector fields $\mathcal V_{b,[e3b]}$. More precisely there is a *good spanning set*: $\mathcal V =
\{V_1, \dots,V_N\}\subset\mathcal V_{b,[e3b]}$ spanning $\mathcal V_b$, with bounded weights $w_j\in C^\infty(\tilde M)$
such that $V_{0,j} := w_jV_j\in\mathcal V_{e3b}$ and $\{V_{0,j}\}$ spans $\mathcal V_{e3b}$ over $C^\infty$.

*Proof.* The spanning statement combines Corollaries 2.3 and 2.7, the two regions being disjoint up to the region where
both algebras equal $\mathcal V_b$. A good spanning set: finitely many e3b-vector fields spanning $\mathcal V_{e3b}$
(weights 1), together with $\chi_Kt\partial_t = \rho_K^{-1}\chi_Kr\partial_t$ ($w = \rho_K = \frac rt$) and, for a
spanning set of vector fields $\partial_\omega$ on $\mathbb S^3$, $\chi_I\partial_\omega = x_I^{-1}\chi_Ix_I\partial_
\omega$ ($w = x_I$), where $\chi_K$, $\chi_I$ localise near $K^+$, $\mathscr I^+$; these are commutator fields by Lemmas
2.2 and 2.6, and with the e3b-fields they span $\mathcal V_b$. $\square$

### 2.5 Hamiltonian vector fields

For $p\in C^\infty({}^{3b}T^*\tilde M_0)$, writing 3b-covectors near $K^+\cap\iota^+$ as
$\sigma_{3b}\frac{dt_*}r+\xi_{3b} \frac{dr}r+\eta_{3b}$, $\eta_{3b}\in T^*\mathbb S^3$, the change of variables to
$-\sigma\,dt_*+\xi\,dr+\eta$ gives

$$H_p = (\partial_{\sigma_{3b}}p)r\partial_{t_*}+(\partial_{\xi_{3b}}p)(r\partial_r+\sigma_{3b}\partial_{\sigma_{3b}})+
(\partial_{\eta_{3b}}p)\partial_\omega-(r\partial_{t_*}p)\partial_{\sigma_{3b}}-((r\partial_r+\sigma_{3b}\partial_{\sigma
_{3b}})p)\partial_{\xi_{3b}}-(\partial_\omega p)\partial_{\eta_{3b}}\tag{2.1}$$

([Hin26c] (2.35)), and for $p\in C^\infty({}^{e3b}T^*\tilde M)$ near $\mathscr I^+\cap\iota^+$, with covectors $\sigma
_{eb}\frac{d\rho_+}{\rho_+}+\xi_{eb}\frac{dx_I}{x_I}+\eta_{eb}\frac{d\omega}{x_I}$,

$$H_p = (\partial_{\sigma_{eb}}p)\rho_+\partial_{\rho_+}+(\partial_{\xi_{eb}}p)(x_I\partial_{x_I}+\eta_{eb}\partial_{
\eta_{eb}})+(\partial_{\eta_{eb}}p)x_I\partial_\omega-(\rho_+\partial_{\rho_+}p)\partial_{\sigma_{eb}}-((x_I\partial_
{x_I}+\eta_{eb}\partial_{\eta_{eb}})p)\partial_{\xi_{eb}}-(x_I\partial_\omega p)\partial_{\eta_{eb}}\tag{2.2}$$

([Hin26c] (2.38)). Both follow by writing the canonical symplectic form in these fibre coordinates; the dimension of
$\mathbb S^3$ does not enter. Structurally, the canonical 1-form is a smooth section of ${}^{e3b}T^*({}^{e3b}T^*\tilde
M)$, so $\omega = -d\alpha$ is a smooth e3b-2-form and $H_p\in\mathcal V_{e3b}({}^{e3b}T^*\tilde M)$, with $p\mapsto
H_p$ a first-order e3b-operator ([Hin26c] (2.39)).

### 2.6 Product compactifications

**Lemma 2.10 (slicing by X; [Hin26c] Lemma 2.19).** Let $M'_1 := [\overline{\mathbb R}_{t_*}\times X;\partial
\overline{\mathbb R}\times\partial X]$. The identity of $\mathbb R^{1+4}$ in the coordinates $(t_*,r,\omega) = (t-r,r,
\omega)$ induces a diffeomorphism $M_1\cap\mathrm{cl}\{t\ge0\}\to M'_1\cap\mathrm{cl}\{t_*\ge-r\}$ identifying $K^+$,
$\iota^+_1$, $\mathscr I^+_1$ and $I^0_1\cap\{\frac tr\ge0\}$ with the lift of $\{+\infty\}\times X$, the lift of $\{+
\infty\}\times\partial X$, the lift of $\mathbb R\times\partial X$, and the part of the lift of
$\{-\infty\}\times\partial X$ in $\{\rho_I\le1\}$.

*Proof.* Coordinates on $M'_1$: in the interior $(t_*,x)$; near $\partial\overline{\mathbb R}\times X^\circ$, $(\rho_K =
\frac1{\pm t_*},x)$, also coordinates near $(K^+)^\circ$; near $\mathbb R\times\partial X$, $(t_*,\rho,\omega)$, also
coordinates near $(\mathscr I^+_1)^\circ$; near the front face over $\{+\infty\}\times\partial X$: adjacent to
$\{+\infty \}\times X$, $(\rho,\frac{1/t_*}\rho = \frac r{t-r},\omega)$, and $\frac r{t-r} = \frac rt(1-\frac rt)^{-1}$
matches the coordinates near $\iota^+\cap K^+$; adjacent to $\mathbb R\times\partial X$, $(\frac1{t_*},\rho t_* =
v,\omega)$, the coordinates near $\mathscr I^+_1\cap\iota^+_1$; near the front face over $\{-\infty\}\times\partial X$
adjacent to $\mathbb R\times\partial X$, $(\rho_0 = \frac1{r-t+2},\rho_I = \frac{r-t+2}r,\omega)$, those near
$I^0_1\cap\mathscr I^+_1$, in which $\{t = 0\}$ is $\{\rho_I(1-2\rho_0) = 1\}$. Each chart of one space is thus a chart
of the other. $\square$

*The T-normal operator* ([Hin26c] (2.41)). For $A\in\mathrm{Diff}^m_{3b}(M_0)$, write near $K^+$, in $t_*$, $r$,
$\omega$ and the defining functions $\rho_K$, $\rho_+ = r^{-1}$, $A = \sum_{j+k+|\alpha|\le
m}a_{jk\alpha}(\rho_+,\rho_K,\omega)(r \partial_{t_*})^j(r\partial_r)^k\partial_\omega^\alpha$; then $A_0 := \sum
a_{jk\alpha}(r^{-1},0,\omega)(r\partial_{t_*}) ^j(r\partial_r)^k\partial_\omega^\alpha$ is the unique
$t_*$-translation-invariant operator with $\chi(A-A_0)\in\rho_K \mathrm{Diff}^m_{3b}$, $\chi$ a collar cut-off of $K^+$
(uniqueness: a translation-invariant operator in $\rho_K\mathrm {Diff}^m_{3b}$ near $K^+$ vanishes, its coefficients
being independent of $t_*$ and vanishing as $t_*\to\infty$).

**Lemma 2.11 (slicing by $\iota^+$; [Hin26c] Lemma 2.20).** $\iota^+ = ([0,2)_{\sqrt v}\cup(1,\infty]_v)\times\mathbb
S^3$. Let $M'_+ := [[0,\infty)_\tau\times\iota^+;\{0\}\times v^{-1}(\infty)]$. The map
$(t,r,\omega)\mapsto(\tau,v,\omega)$, $\tau = \frac1{t_*}$, $v = \frac{t_*}r$, induces a diffeomorphism
$M\cap\mathrm{cl}\{t_*\ge1,r\ge1\}\to M'_+\cap\mathrm{cl} \{\tau\le1,\tau v\le1\}$ identifying $\iota^+$,
$K^+\cap\{r\ge1\}$ and $\mathscr I^+\cap\{t_*\ge1\}$ with the lift of $\{0\}\times\iota^+$, the front face of $M'_+$
intersected with $\{\tau v\le1\}$, and $[0,1]\times v^{-1}(0)$.

*Proof.* In $v<2$, $(\sqrt v,\tau)$ on $M'_+$ are $(x_I,\rho_+)$ on $M$. In $v^{-1}<2$, use $(\frac1v,\tau)$ on
$[0,\infty) \times\iota^+$; after blowing up $\{\tau = 0,\frac1v = 0\}$, the projective coordinates near the corner of
the front face with the lift of $\{0\}\times\iota^+$ are $\frac1v = \frac r{t_*} = \frac rt(1-\frac rt)^{-1}$ and
$\tau/\frac1v = \frac1r$, which are coordinates near $\iota^+\cap K^+$ on $M$ by section 1. $\square$

*The $\iota^+$-normal operator* ([Hin26c] (2.44)). For $A\in\mathrm{Diff}^m_{e3b}(\tilde M)$ there is a unique
dilation-invariant $A_0$ on $(0,\infty)_\tau\times\iota^+$ with $\chi(A-A_0)\in\rho_+\mathrm{Diff}^m_{e3b}$, $\chi$ a
collar cut-off of $\iota^+$: near $\iota^+\cap\mathscr I^+$, in $x_I = \sqrt v$, $\rho_+ = \frac1{t_*}$, $\omega$, write
$A = \sum a_{jk\alpha}(x_I,\rho_+,\omega)(x_I\partial_{x_I})^j(\rho_+\partial_{\rho_+})^k(x_I\partial_\omega)^\alpha$
and freeze $\rho_+ = 0$; near $\iota^+\cap K^+$, with $R = \frac r{t_*} = \rho_K$, $\tau = \frac1{t_*}$ (so
$r\partial_{t_*} = -R(R \partial_R+\tau\partial_\tau)$, $r\partial_r = R\partial_R$), write $A = \sum
a_{jk\alpha}(\rho_+,\rho_K,\omega)(R\tau \partial_\tau)^j(R\partial_R)^k\partial_\omega^\alpha$ and freeze $\rho_+ = 0$.
The coordinates used are product coordinates on $[0,\infty)_\tau\times\iota^+$, and $R\tau\partial_\tau$, $R\partial_R$,
$\partial_\omega$ form a local frame of $\mathcal V_{3b}$ near $\iota^+\cap K^+$.

## 3. The scaled bounded geometry calculus (READ)

Everything in this section is READ in [SBG] (arXiv:2408.06651v1, statements by number); it holds on smooth manifolds of
every dimension $n$, and is quoted here without proof. Notation as in [SBG].

(S1) ([SBG] Definitions 1.1, 1.3.) A *b.g. structure* on an $n$-manifold $M$ without boundary is a collection $\mathcal
B = \{(U_\alpha,\phi_\alpha)\}$ of charts $\phi_\alpha:U_\alpha\to(-2,2)^n$ of finite multiplicity, with $M =
\bigcup\phi_ \alpha^{-1}((-1,1)^n)$ and transition maps $\tau_{\beta\alpha} = \phi_\beta\circ\phi_\alpha^{-1}$ uniformly
bounded in $C^\infty$. A *scaled b.g. structure* $\mathcal B^\times = \{(U_\alpha,\phi_\alpha,\rho_\alpha)\}$ adds
scalings $\rho _\alpha\in(0,1]^n$ with $|\partial^\gamma(\rho_{\alpha,i}\partial_i\tau^j_{\beta\alpha}(x))|\le
C_\gamma\rho_{\beta,j}$ ([SBG] (1.6)). Then: $\bar\rho_\alpha := \max_i\rho_{\alpha,i}$; the *coefficient Lie algebra*
$\mathcal W := C^\infty_{\mathrm{uni},\mathcal B}(M;TM)$ (coefficients uniformly bounded in $C^\infty$ in the charts);
the *operator Lie algebra* $\mathcal V\subset\mathcal W$ of those $V$ with $(\phi_\alpha)_*V = \sum
V^i_\alpha\rho_{\alpha,i}\partial_i$, $V^i_\alpha$ uniformly bounded in $C^\infty$.

(S2) ([SBG] Definitions 3.4, 3.6.) A *weight* is $0<w\in C^\infty(M)$ with $\frac{Ww}w\in
C^\infty_{\mathrm{uni},\mathcal B}$ for $W\in\mathcal W$; a scaling weight $\rho$ is a weight equivalent to
$\{\bar\rho_\alpha\}$.

(S3) ([SBG] Definitions 3.14, 3.17; Propositions 3.19, 3.22; Theorem 3.21.) With $\chi_\alpha = \phi^*_\alpha\chi$ and
$S_\alpha(x) = (x^1/\rho_{\alpha,1},\dots,x^n/\rho_{\alpha,n})$, $\|u\|^2_{wH^s_{\mathcal V}(M)} :=
\sum_\alpha\|w_\alpha ^{-1}(S_\alpha)_*(\phi_\alpha)_*(\chi_\alpha u)\|^2_{H^s(\mathbb R^n)}$, and $wH^{(s;k)}_{\mathcal
V;\mathcal W}(M)$ is the space of $u\in wH^s_{\mathcal V}$ with $W_1\cdots W_ju\in wH^s_{\mathcal V}$ for $j\le k$,
$W_i\in\mathcal W$. Every $P\in w\mathrm{Diff}^m_{\mathcal V}$ maps $w'H^{(s;k)}_{\mathcal V;\mathcal W}\to
ww'H^{(s-m;k)}_{\mathcal V;\mathcal W}$ boundedly. For weights with $w/w'\to0$ at infinity and $s>s'$ (or $s\ge s'$,
$k\ge k'$, one strictly), $wH^{(s;k)} _{\mathcal V;\mathcal W}\hookrightarrow w'H^{(s';k')}_{\mathcal V;\mathcal W}$ is
compact. For a uniformly positive $\mathcal V$-density $\mu$, the $L^2(\mu)$ pairing identifies $(wH^s_{\mathcal V})^*$
with $w^{-1}H^{-s}_{\mathcal V}$.

(S4) ([SBG] Definitions 3.7, 3.8, 3.31, 3.34, 3.43.) The $\mathcal V$-cotangent bundle ${}^{\mathcal V}T^*M$ has the
trivialisations $U_\alpha\times\mathbb R^n\ni(p,\xi)\mapsto\sum\xi_i\frac{dx^i_\alpha}{\rho_{\alpha,i}}$.
$S^m({}^{\mathcal V}T^*M)$ consists of the $a$ whose local expressions satisfy $|\partial_x^\beta\partial_\xi^\gamma
a|\le C_{\beta\gamma} \langle\xi\rangle^{m-|\gamma|}$ uniformly in $\alpha$. $\mathrm{Op}_{\mathcal V}(a) :=
\sum_\alpha\phi_\alpha^*\mathrm{Op} _\alpha((\phi_\alpha)_*(\chi_\alpha a))$, with $\mathrm{Op}_\alpha$ the quantization
with phase $\sum(x^j-x'^j)\xi_j/ \rho_{\alpha,j}$ and a cut-off $\psi(x-x')$. Residual operators
$w\rho^\infty\Psi^{-\infty}_{\mathcal V}$ map $w'\rho^{-N} H^{(-N;k)}_{\mathcal V;\mathcal W}\to
ww'\rho^NH^{(N;k)}_{\mathcal V;\mathcal W}$ for all $w'$, $N$, $k$, together with their adjoints. $w\Psi^m_{\mathcal
V}(M) := \{\mathrm{Op}_{\mathcal V}(a)+R\}$, $a\in wS^m$, $R$ residual.

(S5) ([SBG] Theorems 3.44, 3.51, 3.52; Proposition 3.55; Remark 3.47.) $A\in w\Psi^m_{\mathcal V}$ maps $w'H^{(s;k)}
_{\mathcal V;\mathcal W}\to ww'H^{(s-m;k)}_{\mathcal V;\mathcal W}$ boundedly, with norm bounded by a seminorm of $A$
(Remark 3.47). $w\rho^{-l}\Psi^m_{\mathcal V}$ is closed under adjoints ($\sigma(A^*) = \overline{\sigma(A)}$) and
compositions ($\sigma(A_1A_2) = \sigma(A_1)\sigma(A_2)$), $\sigma(i[A_1,A_2]) = H_{\sigma(A_1)}\sigma(A_2)$,
$\mathrm{WF}' (A_1A_2)\subset\mathrm{WF}'(A_1)\cap\mathrm{WF}'(A_2)$, and these operations are continuous. Microlocal
elliptic regularity: if $\mathrm{WF}'(B)\subset\mathrm{Ell}(A)$, $A\in w'\Psi^{m'}$, then $\|Bu\|_{w\rho^lH^m}\le
C_N(\|Au\|_{ww' \rho^lH^{m-m'}}+\|u\|_{w\rho^{-N}H^{-N}})$. Elliptic operators are Fredholm when $\mathcal V$ is fully
symbolic.

(S6) ([SBG] Remark 3.33.) The boundedness $\mathrm{Op}_{\mathcal V}(a):w'H^{(s;k)}_{\mathcal V;\mathcal W}\to ww'
H^{(s-m;k)}_{\mathcal V;\mathcal W}$ requires only uniform bounds $\langle\xi\rangle^{m-|\gamma|}$ on $(\rho_\alpha
\partial_x)^\beta\partial_x^{\beta'}\partial_\xi^\gamma a_\alpha$ for $|\beta'|\le k$ ("$\mathcal V$-regular symbols,
with $x$-derivatives up to order $k$"); the proof gives operator norms bounded by finitely many such seminorms, the
number depending on $s$, $m$ in a compact set (the source's Lemma 3.5).

(S7) ([SBG] Definitions 3.58-3.59.) For a parameterised scaled b.g. structure $(\mathcal B^{p,\times})_{p\in P}$, with
all bounds uniform in $p$, the above holds uniformly in $p$; operators are families with uniformly bounded symbols and
residual parts, bounded uniformly on the $p$-dependent spaces.

(S8) ([SBG] Definition 4.6, p. 66, and the paragraph after it; section 4.2.) Variable orders $\mathsf m,\mathsf l\in
S^0$: the symbols $\rho^{-\mathsf l}\lambda^{-\mathsf m}a_0$ with
$a_0\in\bigcap_{\delta\in(0,\frac12)}S^0_{1-\delta,\delta}$, contained in $\bigcap_\delta\rho^{-\sup\mathsf
l}S^{\sup\mathsf m}_{1-\delta,\delta}$, and the corresponding operators and Sobolev spaces (variable decay orders when
the scaling weight tends to 0). The source states that orders are additive under composition and that its Theorem 3.44
"remains valid, mutatis mutandis", the principal symbol being taken modulo $\bigcap_\delta\rho^{-\mathsf
l+1-2\delta}S^{\mathsf m-1+2\delta}$; Theorem 3.44 there is the boundedness theorem, and the composition context shows
that the calculus of its Theorem 3.51 is meant as well (a READ decision, D196). It also states that their operators map
$H^{\mathsf m',\mathsf l'}$ to $H^{\mathsf m'-\mathsf m,\mathsf l'-\mathsf l}$, by the proof of its Proposition 4.2. The
factor $a_0$ need not lie in $S^0$: its derivatives may carry logarithmic factors, as those of $\lambda^{-\mathsf m}$ do
(D195; this item earlier summarised the class with $a_0$ in $S^0$ and cited Theorem 3.51 for the calculus).

(S9) ([SBG] Definitions 4.11, 4.14; Propositions 4.15, 4.17, 4.18; (4.24a-b).) On $M = \mathbb R_t\times X$ with the
product structure built from a scaled b.g. structure on $X$ and weight families $\rho_{\alpha,0}\le1$, $\tau_\alpha$
(unit cells $((j-2)\frac{\tau_\alpha}{\rho_{\alpha,0}},(j+2)\frac{\tau_\alpha}{\rho_{\alpha,0}})\times U_\alpha$,
scalings $(\rho _{\alpha,0},\rho_\alpha)$), the Fourier transform in $t$ is an isomorphism $wH^s_{\mathcal V}(\mathbb
R\times X)\to L^2( \mathbb R_\sigma;w\langle\tau\sigma\rangle^{-s}H^s_{\hat{\mathcal V}_\sigma}(X))$, with $\hat{\mathcal
V}_\sigma$ the operator Lie algebra of the scalings $\rho_{\alpha,i}/\langle\tau_\alpha\sigma\rangle$. The spectral
family $\hat A(\sigma) u = e^{-i\sigma t}A(e^{i\sigma t}u)|_{t = 0}$ of a translation-invariant $A\in
w\mathrm{Diff}^m_{\mathcal V}$ lies in $w\langle\tau\sigma\rangle^m\mathrm{Diff}^m_{\hat{\mathcal V}}$ with principal
symbol $a(\sigma\,dt+\cdot)$; for pseudodifferential $A$, $\hat A(\sigma) = \mathrm{Op}_{\hat{\mathcal
V}_\sigma}(a|_{\sigma dt+T^*X})$ plus a residual family. (The sign convention of [SBG] (4.15) is $e^{-i\sigma t}A
e^{i\sigma t}$; [Hin26c] (3.17) and the spectral families of Part I use $e^{i\sigma t}Ae^{-i\sigma t}$, i.e.
$\sigma\mapsto-\sigma$.) For variable orders $\mathsf s,\mathsf l$ invariant under translations in $t$, the Fourier
transform is an isomorphism from $w\rho_X^{\mathsf l}H^{\mathsf s}_{\mathcal V}(\mathbb R\times X)$ onto the space of
$L^2$ functions of $\sigma$ with values in $w\rho_X^{\hat{\mathsf l}_\sigma}\langle\tau\sigma\rangle^{-\hat{\mathsf
s}_\sigma}H^{\hat{\mathsf s}_\sigma}_{\hat{\mathcal V}_\sigma}(X)$, with the restricted orders $\hat{\mathsf s}_\sigma :=
\mathsf s|_{\sigma\,dt+T^*X}$, $\hat{\mathsf l}_\sigma := \mathsf l|_{\sigma\,dt+T^*X}$; that space is the set of
elements of $L^2(\mathbb R_\sigma;w\rho_X^{l_0}\langle\tau\sigma\rangle^{-s_0}H^{s_0}_{\hat{\mathcal V}_0}(X))$,
$l_0\le\inf\mathsf l$, $s_0\le\inf\mathsf s$, whose image under a fixed elliptic operator of the spectral class of orders
$(\hat{\mathsf s},\hat{\mathsf l})$ lies in $L^2(\mathbb R_\sigma;L^2(X))$ ([SBG] (4.24a-b), pp. 73-74, stated there with
the remark that the proof is that of Proposition 4.18; [Hin26c] cites it as (4.25a-b)). Sections 5-7 use it in this form
for variable orders.

(S10) ([SBG] Definition 4.20, Proposition 4.22.) $\mathcal W_{[\mathcal V]}$ is the set of $W\in\mathcal W$ with
$[W,V]\in \mathcal V$ for all $V\in\mathcal V$. If it spans $\mathcal W$ over $C^\infty_{\mathrm{uni},\mathcal B}$, there
is a subalgebra $\Psi_{\mathcal V,[\,]}\subset\Psi_{\mathcal V}$, closed under compositions and adjoints and containing
all quantizations $\mathrm{Op}_{\mathcal V}(a)$, with $\mathrm{ad}_{W_1}\cdots\mathrm{ad}_{W_k}A\in\Psi_{\mathcal
V,[\,]}$ for $W_i\in\mathcal W_{[\mathcal V]}$; likewise with weights and variable orders. The operators of [Hin26c] are
taken in this subalgebra ([Hin26c] p. 48, in the text), and so are those here.

(S11) ([SBG] Proposition 4.2.) For phase space weights $w$, $w'$: $\Psi^w_{\mathcal V}$ maps $H^{w'}_{\mathcal V}\to
H^{ww'}_{\mathcal V}$, and $(H^w_{\mathcal V})^* = H^{w^{-1}}_{\mathcal V}$.

The sharp Gårding inequality, by which the source proves (L4) on each unit cell, is not used: Part II.A$'$ proves (L4)
without it.

## 4. The e3b-calculus at n = 4

### 4.1 Unit cells

The scaled b.g. structure is that of [Hin26c] section 3.2.1 with $\mathbb R^4_x$, $\mathbb S^3$ in place of $\mathbb
R^3_x$, $\mathbb S^2$; its coefficient and operator Lie algebras are $\mathcal W = C^\infty_b\mathcal V_b(\tilde M)$ and
$\mathcal V = C^\infty_b\mathcal V_{e3b}(\tilde M)$, where $C^\infty_b$ denotes functions that remain bounded under any
finite number of b-vector fields (conormal functions). On $\Omega\cap M^\circ$ there are four families of cells, which
are compatible on their overlaps (each family's charts are related to the others' by coordinate changes that are
uniformly bounded with the scalings, as one checks from the expressions of the spanning fields below).

(1) Near $K^+$: $U_{1,i} := (2^{i-2}-1,2^{i+2}-1)_t\times(-2,2)^4_x$, scalings $\rho_t = 2^{-i}$, $\rho_{x^q} = 1$; and,
for $j\in\{1,\dots,4\}$, $\pm$, $k\in\mathbb N_0$, $i\ge k+10$, $l\in\mathbb Z^3$ with $|l|\le2$, $U_{1,i,\pm jkl} :=
\{2^{ i-2}-1<t<2^{i+2}-1,\ \pm x^j\in(2^{k-2},2^{k+2}),\ \hat x_j/x^j\in(-2,2)^3+l\}$ ($\hat x_j$ the other three
coordinates), scalings $\rho_t = 2^{k-i}$, $\rho_{x^q} = 1$. In $U_{1,i}$, $\mathcal W$, $\mathcal V$ are spanned by
$\langle t\rangle \partial_t,\partial_x$, resp. $\partial_{t_*},\partial_x$; in $U_{1,i,\pm jkl}$ by
$t_*\partial_{t_*},r\partial_x$, resp. $r\partial_{t_*},r\partial_x$.

(2) Near $\iota^+\cap\{\rho_K\le3\}$, with $\tau = \frac1{t_*}$, $\rho_K = \frac r{t_*}$, and the eight chart domains
$\mathbb S^3_{k\pm} := \{\omega\in\mathbb S^3:\pm\omega_k>\frac14\}$, $k = 1,\dots,4$, each a graph over the other three
coordinates (they cover $\mathbb S^3$, as $\max_k|\omega_k|\ge\frac12$; the source uses the complements of the points
$-\hat e_k$, with stereographic charts, and any finite cover by charts gives an equivalent structure, [SBG] Proposition
3.2): $U_{2,ijk\pm} := (2^{-i-2},2^{-i+2})_\tau\times(2^{-j-2},2^{-j+2})_{\rho_K} \times\mathbb S^3_{k\pm}$, $j\ge i$,
scalings $\rho_\tau = 2^{-j}$, $\rho_{\rho_K} = \rho_\omega = 1$; $\mathcal V$ is spanned by $\rho_K\tau\partial_\tau$,
$\rho_K\partial_{\rho_K}$, $\partial_\omega$ (equivalently $r\partial_{t_*}$, $r\partial_r$, $\partial_\omega$),
$\mathcal W$ by $\tau\partial_\tau$, $\rho_K\partial_{\rho_K}$, $\partial_\omega$.

(3) Near $\iota^+\cap\{x_I\le3\}$, with $x_I = (\frac{t_*}r)^{1/2}$: $U_{3,ijk\pm} :=
(2^{-i-2},2^{-i+2})_\tau\times(2^{-j-2}, 2^{-j+2})_{x_I}\times\mathbb S^3_{k\pm}$, scalings $\rho_\tau = \rho_{x_I} =
1$, $\rho_\omega = 2^{-j}$; $\mathcal V$ is spanned by $\tau\partial_\tau$, $x_I\partial_{x_I}$, $x_I\partial_\omega$,
$\mathcal W$ by the b-vector fields.

(4) One cell covering the remaining compact part of $\Omega\cap M^\circ$; and analogous families for $t_*\le1$.

### 4.2 Operators and spaces

With these, [SBG] gives ([Hin26c] (3.23)-(3.24)): the weighted e3b-ps.d.o.s $C^\infty_b\Psi^{\mathsf
s,(2\alpha_I,\alpha_+, \alpha_K)}_{e3b}(\tilde M) = x_I^{-2\alpha_I}\rho_+^{-\alpha_+}\rho_K^{-\alpha_K}\Psi^{\mathsf
s}_{e3b}(\tilde M)$, $\mathsf s \in C^\infty({}^{e3b}S^*\tilde M)$, containing $C^\infty_b\mathrm{Diff}^m_{e3b}$; the
spaces $H^{\mathsf s,(2\alpha_I,\alpha_+, \alpha_K)}_{e3b} = x_I^{2\alpha_I}\rho_+^{\alpha_+}\rho_K^{\alpha_K}H^{\mathsf
s}_{e3b}(\tilde M,|dt\,dx|)$ and $H^{(\mathsf s;k),(2\alpha_I,\alpha_+,\alpha_K)}_{e3b;b}$ (with $k$ b-derivatives, the
$H^{(s;k)}_{\mathcal V;\mathcal W}$ of (S3)). The microlocalisation locus is ${}^{e3b}S^*\tilde M$. $|dt\,dx|$ is a
uniformly positive $\mathcal V$-density times a weight, so (S3) applies with that weight absorbed. The operators are
taken in $\Psi_{\mathcal V,[\,]}$ of (S10), which is possible because $\mathcal W_{[\mathcal V]}\supset\mathcal
V_{b,[e3b]}$ spans $\mathcal W$ (Lemma 2.9). Hence, by (S10):

$$A\in C^\infty_b\Psi^{\mathsf s}_{e3b},\ V\in\mathcal V_{b,[e3b]}\implies[V,A]\in C^\infty_b\Psi^{\mathsf s}_{e3b},\quad
\mathrm{WF}'_{e3b}([V,A])\subset\mathrm{WF}'_{e3b}(A).\tag{4.1}$$

(The wave front set inclusion: if $A$ is microlocally residual near a point, so is $[V,A]$, by (S10) applied to the
localised operator.)

**Lemma 4.1 ([Hin26c] Lemma 3.6).** Let $V_1,\dots,V_N\in\mathcal V_b(\tilde M)$ and $w_j\in C^\infty(\tilde M)$ bounded
with $V_{0,j} := w_jV_j\in\mathcal V_{e3b}$ spanning $\mathcal V_{e3b}$ over $C^\infty$, and $V_0 := I$. Then every
$A\in C^\infty_b\Psi^{\mathsf s}_{e3b}$ is $\sum_{j=0}^NA_jV_j$ with $A_j\in C^\infty_b\Psi^{\mathsf s-1}_{e3b}$.

*Proof.* $B := \sum_jV_{0,j}^*V_{0,j}\in\mathrm{Diff}^2_{e3b}$ is elliptic, so $I = QB+R$ with $Q\in
C^\infty_b\Psi^{-2}_{e3b}$ and $R\in C^\infty_b\Psi^{-1}_{e3b}$: take $Q := \mathrm{Op}(q)$ with $q\in S^{-2}$ equal to
$\sigma(B)^{-1}$ outside a compact subset of each fibre, uniformly; then $R := I-QB$ has principal symbol 0 at order 0,
so it has order $-1$ by the principal symbol sequence (S5). This is the first step of Lemma 8.4 (b), which does not use
the present lemma. (The source takes a full parametrix, which (S5) does not READ.) Then $A =
\sum_jAQV_{0,j}^*w_jV_j+ARV_0$, and $A_j := AQV_{0,j}^*w_j\in C^\infty_b\Psi^{\mathsf s-1}_{e3b}$, $A_0 := AR\in
C^\infty_b\Psi^{\mathsf s-1}_{e3b}$. $\square$

Passing to the secondary structure (subdividing cells into $\rho$-cuboids) gives the larger classes $\tilde\Psi_{e3b} =
C^\infty_{e3b}\Psi_{e3b}$ with e3b-regular coefficients (Remark 3.48 of [SBG]: $\Psi_{\mathcal V}\subset\Psi_{\mathcal
V'}$), still bounded on the same spaces.

### 4.3 Bundles

Operators on the trivial bundle $\mathbb C^N$ (the record's bundles, as in I.A section 1.2) are $N\times N$ matrices of
scalar operators; all statements above and below hold for them with matrix-valued symbols, principal symbols multiplying
as matrices ([SBG] Remark 3.13 for differential operators; for ps.d.o.s, matrices of scalar ones). Where a scalar
principal symbol is needed (commutators lowering order), it is assumed and said.

## 5. The Fourier transform near $K^+$

### 5.1 The 3b-structure and its spectral side

Near $K^+$ the secondary structure of section 4.1 has the cells $U_i := (i-2,i+2)_t\times(-2,2)^4_x$ and $U_{i,\pm jkl}
:= \{(i-2)2^k<t<(i+2)2^k,\ \pm x^j\in(2^{k-2},2^{k+2}),\ \hat x_j/x^j\in(-2,2)^3+l\}$, $i\in\mathbb Z$, $k\in\mathbb
N_0$, $l\in\mathbb Z^3$, $|l|\le2$. These are of the product form (S9) over the b-structure on $\mathbb R^4$ (cells
$(-2,2)^4$ and $\{\pm x^j\in(2^{k-2},2^{k+2}),\hat x_j/x^j\in(-2,2)^3+l\}$, scalings 1), with $\tau_{\pm jkl} =
2^k\sim\langle x \rangle$ and $\rho_{0} = 1$. Their Lie algebra is $C^\infty_{3b}\mathcal V_{3b}(\tilde M_0)$, and the
spaces are $\tilde \Psi^{\mathsf s,(\alpha_{\mathrm{sf}},\alpha_K)}_{3b} =
\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\rho_K^{\alpha_K}\tilde\Psi ^{\mathsf s}_{3b}$ and $H^{\mathsf
s,(\alpha_{\mathrm{sf}},\alpha_K)}_{3b}(\tilde M_0) = \rho_{\mathrm{sf}}^{\alpha_{\mathrm
{sf}}}\rho_K^{\alpha_K}H^{\mathsf s}_{3b}(\tilde M_0,|dt\,dx|)$ ([Hin26c] (3.27)), the weights meaning decay.

By (S9) the Fourier transform in $t$, $\hat u(\sigma) = \int e^{-i\sigma t}u\,dt$, leads to the parameterised scaled
b.g. structure on $\tilde X = \overline{\mathbb R^4}$ with the b-cells and scalings $\rho_{\sigma,\alpha,i} =
(1+|\sigma| \langle x\rangle)^{-1}$ ([Hin26c] section 3.2.2), coefficient Lie algebra $C^\infty_b\mathcal V_b(\tilde X)$
for all $\sigma$, and operator Lie algebras: (1) at $\sigma = 0$, $C^\infty_b\mathcal V_b(\tilde X)$ (the b-setting);
(2) at fixed $\sigma\ne0$, $C^\infty_b\mathcal V_{\mathrm{sc}}(\tilde X)$; (3) for $\pm\sigma\in[0,1]$, the
scattering-b- transition algebra $C^\infty_b\mathcal V_{\mathrm{sc}\text{-}b}(\tilde X)$ on $\tilde
X_{\mathrm{sc}\text{-}b} := [[0,1] _\varsigma\times\tilde X;\{0\}\times\partial\tilde X]$, $\varsigma = \pm\sigma$, with
faces scf, tf, zf and $\mathcal V _{\mathrm{sc}\text{-}b} = \{V\in\rho_{\mathrm{scf}}\mathcal V_b(\tilde
X_{\mathrm{sc}\text{-}b})$ tangent to the $\varsigma$-level sets$\}$, $\rho_{\mathrm{scf}} = (1+\varsigma\langle
x\rangle)^{-1}$, spanned by $\rho_{\mathrm{scf}} \langle x\rangle\partial_x$; the spaces $H^{\mathsf s,(\mathsf
r,l,q)}_{\mathrm{sc}\text{-}b,\sigma} := \rho_{\mathrm{scf}} ^{\mathsf
r}\rho_{\mathrm{tf}}^l\rho_{\mathrm{zf}}^qH^{\mathsf s}_{\mathrm{sc}\text{-}b,\sigma}$ ([Hin26c] (3.32)); (4) for
$\pm\sigma\in[1,\infty)$, the semiclassical scattering algebra with $h = |\sigma|^{-1}$ and spaces $H^{\mathsf s,\mathsf
r,\mathsf b}_{\mathrm{sc},h} = \rho^{\mathsf r}h^{\mathsf b}H^{\mathsf s}_{\mathrm{sc},h}$ ([Hin26c] (3.35)), the
semiclassical microlocalisation locus being identified with ${}^{\mathrm{sc}}\overline T^*\tilde X$ ([Hin26c] (3.36)).
All $L^2$-spaces use $|dx|$. With $k$ further b-derivatives ($\langle x\rangle\partial_x$) these are $H^{(\mathsf s;k),
(\mathsf r,l,q)}_{(\mathrm{sc}\text{-}b,\sigma);b}$ and $H^{(\mathsf s;k),\mathsf r,\mathsf
b}_{(\mathrm{sc},|\sigma|^{-1}); b}$ ([Hin26c] (3.40)-(3.41)).

For a $t$-translation-invariant $A_0\in\rho_{\mathrm{sf}}^{-l}\mathrm{Diff}^m_{3b}(\tilde M_0)$, written as $A_0 = \sum
a _{jk\alpha}(r^{-1},0,\omega)(r\partial_t)^j(r\partial_r)^k\partial_\omega^\alpha$ near $r = \infty$, the spectral
family is $\hat A_0(\sigma) = \sum a_{jk\alpha}(r^{-1},0,\omega)(-i\sigma r)^j(r\partial_r)^k\partial^\alpha_\omega$
([Hin26c] (3.28), with the convention $e^{i\sigma t}A_0e^{-i\sigma t}$), and ([Hin26c] (3.37))

$$(\hat A_0(\hat\sigma|\sigma|))_{|\sigma|\in[0,1]}\in\rho_{\mathrm{scf}}^{-l-m}\rho_{\mathrm{tf}}^{-l}\mathrm{Diff}^m_{
\mathrm{sc}\text{-}b}(\overline{\mathbb R^4}),\qquad(\hat A_0(i\nu\pm h^{-1}))_{h\in(0,
1]}\in\rho^{-l-m}h^{-m}\mathrm{Diff}^m
_{\mathrm{sc},\hbar}(\overline{\mathbb R^4}),\tag{5.1}$$

for $|\hat\sigma| = 1$ and $\nu\in\mathbb R$: each factor $-i\sigma r = -i\hat\sigma\cdot(|\sigma|r)$ is
$\rho_{\mathrm{scf}} ^{-1}\rho_{\mathrm{tf}}^0$ times a bounded sc-b-transition multiplier, and $r\partial_r$,
$\partial_\omega$ are b-fields, which are $\rho_{\mathrm{scf}}^{-1}$ times sc-b-transition fields; the weight
$\rho_{\mathrm{sf}}^{-l} = \langle x\rangle^l$ is $\rho_{\mathrm{scf}}^{-l}\rho_{\mathrm{tf}}^{-l}$ (as $\langle
x\rangle^{-1}\sim\rho_{\mathrm{scf}}\rho_{\mathrm{tf}}$). Likewise in the semiclassical regime with $h$ in place of
$|\sigma|^{-1}$.

### 5.2 Plancherel

**Lemma 5.1 ([Hin26c] Lemma 3.7 at n = 4).** Let $\mathsf s\in C^\infty({}^{3b}S^*\tilde M_0)$ be translation-invariant,
$\mathsf s_\sigma$ the induced orders ([Hin26c] (3.18): the restriction of $\mathsf s$ to $-\sigma\,dt+T^*\tilde X$),
and $\alpha_{\mathrm{sf}}\in\mathbb R$. For $u$ supported where the 3b-cells of section 5.1 apply,

$$\|u\|^2_{H^{\mathsf s,(\alpha_{\mathrm{sf}},0)}_{3b}(\tilde M_0,|dt\,dx|)}\sim\sum_\pm\int_{\pm[0,1]}\|\hat
u(\sigma)\|^2_{H^{\mathsf s_\sigma,(\mathsf s_\sigma+\alpha_{\mathrm{sf}},\alpha_{\mathrm{sf}},0)}_{\mathrm{sc}\text{-}b,
\sigma}(\tilde X,|dx|)}d\sigma
+\sum_\pm\int_{\pm[1,\infty)}\|\hat u(\sigma)\|^2_{H^{\mathsf s_\sigma,\mathsf s_\sigma+\alpha_{\mathrm{sf}},\mathsf
s_\sigma}_{\mathrm{sc},|\sigma|^{-1}}(\tilde X,|dx|)}d\sigma.$$

*Proof.* (S9) (Proposition 4.18 of [SBG], with the variable-order version referred to in [Hin26c] after (3.16)) gives
the isomorphism onto $L^2(\mathbb R_\sigma;\rho_{\mathrm{sf}}^{\alpha_{\mathrm{sf}}}\langle\tau\sigma\rangle^{-\mathsf
s_\sigma}H^{\mathsf s_\sigma}_{\hat{\mathcal V}_\sigma})$ with $\tau\sim\langle x\rangle$ and $|dt\,dx|$ on one side,
$|dx|$ on the other (the $t$-factor is unitary). It remains to name the spaces. For $|\sigma|\le1$, $\hat{\mathcal
V}_\sigma$ is the sc-b-transition algebra, $\langle\tau\sigma\rangle^{-1}\sim(1+|\sigma|\langle
x\rangle)^{-1}\sim\rho_{\mathrm{scf}}$ and $\rho_{\mathrm{sf}} = \langle
x\rangle^{-1}\sim\rho_{\mathrm{scf}}\rho_{\mathrm{tf}}$ ($\rho_{\mathrm{zf}}^0$), giving the weights $(\mathsf
s_\sigma+\alpha_{\mathrm{sf}},\alpha_{\mathrm{sf}},0)$. For $|\sigma|\ge1$, $\hat{\mathcal V}_\sigma$ is the
semiclassical scattering algebra with $h = |\sigma|^{-1}$, and $\langle\tau\sigma\rangle^{-1}\sim h\langle x\rangle
^{-1}$, giving $\rho^{\mathsf s_\sigma+\alpha_{\mathrm{sf}}}h^{\mathsf s_\sigma}$. The dimension does not enter: both
sides use Euclidean densities. $\square$

**Lemma 5.2 ([Hin26c] Lemma 3.9 at n = 4).** With $H^{(\mathsf s;k)}_{3b;b}(\tilde M_0) := \{u\in H^{\mathsf s}_{3b}:
\partial_t^{j_1}(t\partial_t)^{j_2}(\langle x\rangle\partial_x)^\alpha u\in H^{\mathsf s}_{3b},\ j_1+j_2+|\alpha|\le
k\}$ ([Hin26c] (3.39)),

$$\|u\|^2_{H^{(\mathsf s;k),(\alpha_{\mathrm{sf}},0)}_{3b;b}}\sim\sum_\pm\sum_{j = 0}^k\int_{\pm[0,1]}\|(\sigma\partial_
\sigma)^j\hat u(\sigma)\|^2_{H^{(\mathsf s_\sigma;k-j),(\mathsf s_\sigma+\alpha_{\mathrm{sf}},\alpha_{\mathrm{sf}},0)}_{(
\mathrm{sc}\text{-}b,\sigma);b}}d\sigma+\sum_\pm\sum_{j_1+j_2\le k}\int_{\pm[1,\infty)}\|\sigma^{j_1}(\sigma\partial_
\sigma)^{j_2}\hat u(\sigma)\|^2_{H^{(\mathsf s_\sigma;k-j),\mathsf s_\sigma+\alpha_{\mathrm{sf}},\mathsf s_\sigma}_{(
\mathrm{sc},|\sigma|^{-1});b}}d\sigma,$$

$j = j_1+j_2$ in the second sum.

*Proof.* Spatial b-derivatives commute with $\mathcal F$. $\mathcal F(\partial_tu) = i\sigma\hat u$ and $\mathcal
F(t\partial _tu) = -\partial_\sigma(\sigma\hat u) = -(1+\sigma\partial_\sigma)\hat u$. So, for $|\sigma|\le1$,
$\partial_t$ costs a factor $\sigma$, bounded, and $t\partial_t$ becomes $-(1+\sigma\partial_\sigma)$; for
$|\sigma|\ge1$, $\partial_t$ gives $\sigma^{j_1}$. Apply Lemma 5.1 to each $\partial_t^{j_1}(t\partial_t)^{j_2}(\langle
x\rangle\partial_x)^\alpha u$, expand $(1+\sigma\partial_\sigma)^{j_2}$, and use that the $(\mathsf s;k)$-norms are sums
of $\mathsf s$-norms of up to $k$ b-derivatives. The two sides are sums of equivalent terms, by induction on $k$.
$\square$

### 5.3 The low-energy norm of Part I.C

**Lemma 5.3 (the norms of I.C Definition 6.1; [Hin26c] (3.46) at n = 4).** Let $\chi_{\mathrm{zf}},\chi_{\mathrm{tf}}\in
C^\infty(\tilde X_{\mathrm{sc}\text{-}b})$ equal 1 near zf, resp. tf, supported near them. Uniformly in $\varsigma
= |\sigma| \in(0,\varsigma_1]$:

$$\|\chi_{\mathrm{zf}}u\|_{H^{\mathsf s,(\mathsf r,l,q)}_{\mathrm{sc}\text{-}b,
\sigma}}\sim\varsigma^{-q}\|\chi_{\mathrm{zf}}u
\|_{\bar H^{\mathsf s,l-q}_b},\qquad\|\chi_{\mathrm{tf}}u\|_{H^{\mathsf s,(\mathsf r,l,q)}_{\mathrm{sc}\text{-}b,
\sigma}}\sim
\varsigma^{-2-l}\|S_\varsigma(\chi_{\mathrm{tf}}u)\|_{H^{\mathsf s,(\mathsf r,q-l)}_{\mathrm{sc},b}(\mathrm{tf})},$$

the latter with the order $\mathsf r$ read on tf (I.C section 6.1); with $k$ b-derivatives likewise. In particular
$H^{(s;k),(\mathsf r,l,q)}_{(\mathrm{sc}\text{-}b,\varsigma);b}$, on functions supported in $\{\rho<\rho_1\}$ or in the
interior, is the space $\mathcal H^{(s;k),(\mathsf r,l,q)}_\varsigma$ of I.C Definition 6.1, with uniformly equivalent
norms. [Hin26c] prints the second power as $|\sigma|^{\frac32-l}$ at $n = 3$; it is $|\sigma|^{-\frac32-l}$ (I.C section
8, (F2)).

*Proof.* Both are defined by sums over cells, (S3). The sc-b-transition cells at $\varsigma$ are the b-cells of $\mathbb
R^4$ (at radius $r\sim2^k$) with scalings $(1+\varsigma2^k)^{-1}$. Where $\varsigma2^k\le1$ (near zf) the scalings lie
in $[\frac12,1]$, so the cells are b-cells up to a uniformly compatible change ([SBG] Proposition 3.2), and the weight
$\rho_{\mathrm{scf}}^{\mathsf r}\rho_{\mathrm{tf}}^l\rho_{\mathrm{zf}}^q$ is there $\sim\rho^{l-q}\varsigma^q$
($\rho_{\mathrm {scf}}\sim1$, $\rho_{\mathrm{tf}}\sim\rho+\varsigma\sim\rho$, $\rho_{\mathrm{zf}}\sim\varsigma/\rho$):
the first equivalence. Where $\varsigma2^k\ge1$ the scalings are $\sim(\varsigma2^k)^{-1} = \hat r^{-1}$; under
$S_\varsigma$ (I.C section 6.1) the cell at $r\sim2^k$ goes to the cell at $\hat r = \varsigma2^k$ with scaling $\hat
r^{-1}$, a scattering cell of tf near sctf, and the cells at $\hat r\lesssim1$ to b-cells of tf near ztf; the weights
become $\rho_{\mathrm{sctf}}^{\mathsf r} \rho_{\mathrm{ztf}}^{q-l}\varsigma^l$ ($\rho_{\mathrm{tf}}\sim\varsigma$ there,
and $\rho_{\mathrm{zf}}/\rho_{\mathrm{tf}}$ is the ztf weight); and $\|w\|_{L^2(|dx|)} = \varsigma^{-2}\|S_\varsigma
w\|_{L^2(|d\hat x|)}$, as $|d\hat x| = \varsigma^4|dx|$. The frequencies match as in I.C Lemma 6.2 (c). This gives the
second equivalence, with $\varsigma^{-2-l}$. $\square$

So Part I.C's low-energy estimates (I.C Theorem 6.4) are estimates on the spaces $H^{(s;k),(\mathsf
r+\alpha_+,\alpha,0)} _{(\mathrm{sc}\text{-}b,|\sigma|);b}$ of [Hin26c] (9.119) at $n = 4$, which is how they enter
Lemma 5.1 below (in Part II).

## 6. The Mellin transform at $\iota^+$

### 6.1 Near a conic end

The Mellin transform near $\partial\overline{\mathbb R^4}$ and the normal operator estimate are proved in I.C section 2
(Lemmas 2.2-2.7), with the transform $\mathcal Mv(\lambda) = \int e^{\lambda t}v\,dt$, $t = -\log\varrho$, for which the
line of the b-weight $c$ is $\mathrm{Re}\,\lambda = c$ (I.C (2.2)). In the source's convention $(\mathcal Mu)(\sigma) =
\int\varrho^{i\sigma}u\frac{d\varrho}\varrho$, i.e. $\lambda = -i\sigma$, that line is $\mathrm{Im}\,\sigma = c$.

### 6.2 At $\iota^+$

$\iota^+ = ([0,2)_{x_I}\cup(1,\infty]_v)\times\mathbb S^3$ (Lemma 2.11) has the cells $U_{2,jk\pm} = (2^{-j-2},2^{-j+2})
_{\rho_K}\times\mathbb S^3_{k\pm}$ (scalings 1) and $U_{3,jk\pm} = (2^{-j-2},2^{-j+2})_{x_I}\times\mathbb S^3_{k\pm}$
(scalings $1$ in $x_I$, $2^{-j}$ in $\omega$), the spatial parts of the cells of section 4.1. The coefficient Lie
algebra is $C^\infty_b\mathcal V_b(\iota^+)$, the operator Lie algebra $C^\infty_b\mathcal V_{b,e}(\iota^+)$ (b-fields
tangent to the fibres of $\iota^+\cap\mathscr I^+$). With $t = -\log_2\tau$ the cells (3.21)-(3.22) of the source are of
the product form (S9) ([Hin26c] (3.49)), so the Fourier transform in $t$ is the Mellin transform in $\tau$, $(\mathcal
Mu)(\sigma,p) = \int_0^\infty\tau^{i\sigma}u(\tau,p)\frac{d\tau}\tau$. The spectral side is the parameterised structure
on $(\iota^+)^\circ$ with scalings $(1+\rho_K|\sigma|)^{-1}$ near $K^+$ and $\langle\sigma\rangle^{-1}$,
$x_I\langle\sigma\rangle^{-1}$ near $\mathscr I^+$ ([Hin26c] section 3.2.4): for fixed $\sigma$ the 0,b-structure
$C^\infty_b\mathcal V_{0,b}(\iota^+)$ (0-fields $x_I\partial_{x_I}$, $x_I\partial_\omega$ at $\iota^+\cap\mathscr I^+$,
b-fields at $\iota^+\cap K^+$), spaces $H^{\mathsf s,(2\alpha_I,\gamma)}_{0,b}(\iota^+) = x_I^{2\alpha_I}\rho_K^\gamma
H^{ \mathsf s}_{0,b}$; and for $\pm\sigma\in[1,\infty)$, $h = |\sigma|^{-1}$, the semiclassical 0- and cone structure on
$\iota^+_{0\hbar,c\hbar} := [[0,1)_h\times\iota^+;\{0\}\times(\iota^+\cap K^+)]$ with faces cf, tf, sf, 0f and spaces
$H^{\mathsf s,(2\alpha_I,\alpha_{\mathrm{cf}},l,\mathsf b)}_{0\hbar,c\hbar} =
\rho_{0f}^{2\alpha_I}\rho_{\mathrm{cf}}^{\alpha _{\mathrm{cf}}}\rho_{\mathrm{tf}}^l\rho_{\mathrm{sf}}^{\mathsf
b}H^{\mathsf s}_{0\hbar,c\hbar}$ ([Hin26c] (3.50)-(3.56)), all with a b-density $\mu_b$ on $\iota^+$. The spectral
family of a dilation-invariant $A_0$ is (3.52) of the source, with $-i\sigma$ for $\rho_+\partial_{\rho_+}$.

**Lemma 6.1 (the density at n = 4).** On $\mathrm{supp}\,\chi$, $\chi$ a cut-off to $\mathrm{cl}\{r\ge1,t_*\ge1\}$,
$|dt\,dx|$ is a smooth positive multiple of $x_I^{-8}\rho_+^{-5}\rho_K^{-1}|\frac{d\tau}\tau|\mu_b$; so
$H^{0,(2\alpha_I, \alpha_+,\alpha_K)}_{e3b}(\tilde M,|dt\,dx|) =
H^{0,(2(\alpha_I+2),\alpha_++\frac52,\alpha_K+\frac12)}_{e3b}(\tilde M,|\frac{d \tau}\tau|\mu_b)$ there.

*Proof.* $|\frac{d\tau}\tau\mu_b|$ is a b-density on $[0,\infty)\times\iota^+$, hence on its blow-up, hence (Lemma 2.11)
on $\tilde M$ near $\iota^+$, so a smooth positive multiple of $|\frac{dt_*}{t_*}\frac{dx}{\langle x\rangle^4}|$. Thus
$|dt\,dx| = |dt_*\,dx|$ is $t_*\langle x\rangle^4$ times it. Near $\iota^+\cap\mathscr I^+$, $t_*\sim\rho_+^{-1}$ and
$r\sim x_I^{-2}\rho_+^{-1}$, so $t_*^{-1}\langle x\rangle^{-4}\sim\rho_+\cdot x_I^8\rho_+^4 = x_I^8\rho_+^5$; near
$\iota^+\cap K^+$, $t_*\sim\rho_+^{-1}\rho_K^{-1}$, $r\sim\rho_+^{-1}$, so $t_*^{-1}\langle
x\rangle^{-4}\sim\rho_+^5\rho_K$; in the interior of $\iota^+$ both are $\sim\rho_+^5$. Hence $t_*^{-1}\langle
x\rangle^{-4}\sim x_I^8\rho_+^5\rho_K$ on $\mathrm{supp}\,\chi$. Taking square roots, $L^2(|dt\,dx|) =
x_I^4\rho_+^{5/2}\rho_K^{1/2}L^2(|\frac{d\tau}\tau|\mu_b)$. $\square$

At $n = 3$ the same computation gives $x_I^6\rho_+^4\rho_K$, the source's
$(2(\alpha_I+\frac32),\alpha_++2,\alpha_K+\frac12)$.

**Lemma 6.2 ([Hin26c] Lemma 3.14 at n = 4).** Let $\chi$ be as in Lemma 6.1, $\mathsf s\in C^\infty({}^{e3b}S^*\tilde
M)$ invariant under the dilations $(t_*,v,\omega)\mapsto(\nu t_*,v,\omega)$, $\nu\ge1$, on $\mathrm{supp}\,\chi$,
$\mathsf s _\sigma$ the induced orders, and $\alpha_I,\alpha_+,\alpha_K\in\mathbb R$, $k\in\mathbb N_0$. Put $\beta_+ :=
\alpha_++ \frac52$. Then

$$\|\chi u\|^2_{H^{(\mathsf s;k),(2\alpha_I,\alpha_+,\alpha_K)}_{e3b;b}(|dt\,
dx|)}\sim\int_{-1}^1\|\mathcal M(\chi u)(\sigma+
i\beta_+)\|^2_{H^{(\mathsf s_\sigma;k),(2(\alpha_I+2),\alpha_K-\alpha_+-2)}_{0,b;b}(\iota^+,\mu_b)}d\sigma$$
$$+\sum_\pm\int_{\pm[1,\infty)}\sum_{j = 0}^k|\sigma|^{2j}\|\mathcal M(\chi u)(\sigma+i\beta_
+)\|^2_{H^{(\mathsf s_\sigma;k-j),(
2(\alpha_I+2),\alpha_K-\alpha_+-2,\alpha_K-\alpha_+-2,\mathsf s_\sigma)}_{(0\hbar,c\hbar,|\sigma|^{-1});b}(\iota^+,
\mu_b)}d
\sigma.$$

The source prints the line as $\sigma-i(\alpha_++2)$ (at $n = 3$); with its transform
$\int\tau^{i\sigma}u\frac{d\tau}\tau$ the Plancherel line of the weight $\tau^{\beta}$ is $\mathrm{Im}\,\sigma = +\beta$
(section 10, (G2); compare I.C (F1)).

*Proof.* By Lemma 6.1 the left side is the norm with the b-density and weights $(2(\alpha_I+2),\alpha_++\frac52,\alpha_K+
\frac12)$. Near $\iota^+$, $\tau\sim\rho_+\rho_K$ (Lemma 2.11), so $\rho_+^{\beta_+}\rho_K^{\alpha_K+\frac12} =
\tau^{\beta _+}\rho_K^{\alpha_K+\frac12-\beta_+} = \tau^{\beta_+}\rho_K^{\alpha_K-\alpha_+-2}$. With $t = -\log_2\tau$,
the factor $\tau^{\beta_+}$ is $e^{-\beta_+t\log2}$, and for $u = \tau^{\beta_+}v$, $(\mathcal Mu)(\zeta+i\beta_+) =
\int\tau^{i\zeta} \tau^{-\beta_+}u\frac{d\tau}\tau = (\mathcal Mv)(\zeta)$, $\zeta\in\mathbb R$. Now apply (S9) to $v$
(unweighted in $t$). The b-regularity splits: the b-field $\tau\partial_\tau = -(\log2)^{-1}\partial_t$ becomes
multiplication by $-i\sigma$ on the transform side, as $\mathcal M(\tau\partial_\tau u) = -i\sigma\mathcal Mu$, which is
bounded for $|\sigma|\le1$ and gives the factors $|\sigma|^{2j}$ for $|\sigma|\ge1$; the spatial b-fields of $\iota^+$
commute with $\mathcal M$ and give the $k-j$ b-derivatives of the spectral spaces. (For the conjugation by
$\tau^{\beta_+}$, $\tau\partial_\tau$ changes by the constant $\beta_+$, harmless.) The identification of the spectral
spaces with the 0,b- and $0\hbar,c\hbar$-spaces is by their definition as the spaces of the spectral scaled b.g.
structure ([Hin26c] (3.50)-(3.56)), and the weights $x_I^{2(\alpha_I+2)}$, $\rho_K^{\alpha_K-\alpha_+-2}$ are functions
on $\iota^+$, hence pass through. For $|\sigma|\ge1$, the factor $\langle\tau\sigma\rangle^{-\mathsf s}$ of (S9) is
$\rho_{\mathrm{sf}}^{\mathsf s_\sigma}$, the last index. $\square$

*The tf-normal operator at $\iota^+$* ([Hin26c] (3.58)-(3.60)). Near $\iota^+\cap K^+$, with $\hat\rho_K := \rho_K/h$,
the $0\hbar,c\hbar$-fields $\frac h{h+\rho_K}\rho_K\partial_{\rho_K}$, $\frac h{h+\rho_K}\partial_\omega$ become
$\frac1{1+ \hat\rho_K}\hat\rho_K\partial_{\hat\rho_K}$, $\frac1{1+\hat\rho_K}\partial_\omega$, the b,sc-fields of
$\mathrm{tf} = [0,\infty] _{\hat\rho_K}\times\mathbb S^3$; restriction of coefficients gives
$N_{\mathrm{tf}}(A)\in\mathrm{Diff}^{m,(\alpha_c,\mathsf b)} _{b,sc}(\mathrm{tf})$ for
$A\in\mathrm{Diff}^{m,(2\alpha_I,\alpha_c,0,\mathsf b)}_{0\hbar,c\hbar}$, and for $\chi_{\mathrm{tf}}$ supported near
tf, $\|\chi_{\mathrm{tf}}u\|_{H^{\mathsf s,(2\alpha_I,\alpha_{\mathrm{cf}},l,\mathsf b)}_{0\hbar,c\hbar,h}}\sim
h^{-l}\|\chi_{\mathrm{tf}}u\|_{H^{\mathsf s,(\alpha_{\mathrm{cf}},\mathsf b-l)}_{b,sc}(\mathrm{tf})}$, uniformly. Here
no power of $h$ comes from the density: both sides use b-densities, which are invariant under $\rho_K\mapsto\rho_K/h$;
so this is dimension-free. The proof is the comparison of cells, as for Lemma 5.3.

## 7. Supported and extendible spaces

Let $(\mathcal V_\sigma)_\sigma$ be the operator Lie algebra of a parameterised scaled b.g. structure on $M$ (possibly a
single $\sigma$), and fix a uniformly positive $\mathcal V$-density for $L^2_{\mathcal V_\sigma}$.

**Lemma 7.1 ([Hin26c] Lemma 3.15; uniform duality).** Let $\mathsf s$ be a constant or variable order. (1) The pairing
$\langle u,v\rangle$ extends to $H^{\mathsf s}_{\mathcal V_\sigma}\times H^{-\mathsf s}_{\mathcal V_\sigma}$ with
$|\langle u,v \rangle|\le C\|u\|_{H^{\mathsf s}}\|v\|_{H^{-\mathsf s}}$, $C$ independent of $\sigma$. (2)
$c\|u\|_{H^{\mathsf s}}\le\sup_{\|v \|_{H^{-\mathsf s}} = 1}|\langle u,v\rangle|\le C\|u\|_{H^{\mathsf s}}$ uniformly.

*Proof.* For $\mathsf s = 0$, Cauchy-Schwarz and Riesz. In general take an elliptic $A\in\Psi^{\mathsf s}_{\mathcal V}$
and a two-sided parametrix to finite order: $B\in\Psi^{-\mathsf s}_{\mathcal V}$ with $BA = I-R_1$, $AB = I-R_2$ and
$R_1,R_2\in\Psi^{-J}_{\mathcal V}$, $J\ge\sup|\mathsf s|$, all uniformly in $\sigma$. It is built as in Lemma 8.4 (b),
with $I$ in place of $B$ there, by (S5), (S7) and (S8). That gives $B_LA = I-R_1$, and the same for $A^*$ gives $AB_R =
I-R'_2$. Then $B_L-B_R = B_LR'_2-R_1B_R$ has order $-\mathsf s-J$, so $B := B_L$ satisfies $AB = I-R_2$ with $R_2$ of
order $-J$. (The source takes residual remainders, which need a full parametrix that (S5) does not READ.) As
$J\ge\sup|\mathsf s|$, $R_1$ maps $H^{\mathsf s}$ and $R_1^*$ maps $H^{-\mathsf s}$ into $L^2$, and $R_2$, $R_2^*$ map
$L^2$ into $H^{-\mathsf s}$, resp. $H^{\mathsf s}$. (1) For $u,v\in C_c^\infty$, $\langle u,v\rangle = \langle
Au,B^*v\rangle+\langle R_1u,v\rangle$, and, as $v = A^*B^*v+R_1^*v$, $\langle R_1u,v\rangle = \langle
AR_1u,B^*v\rangle+\langle R_1u,R_1^*v\rangle$; so $\langle u,v \rangle = \langle A(I+R_1)u,B^*v\rangle+\langle
R_1u,R_1^*v\rangle$, each factor bounded into $L^2$ from $H^{\mathsf s}$, resp. $H^{-\mathsf s}$. (2) Given
$\lambda\in(H^{-\mathsf s})^*$, the map $j:L^2\oplus L^2\ni(v_0,v_1)\mapsto Av_0+R_2v_1\in H^{- \mathsf s}$ is bounded
and onto, as $v = j(Bv,v)$. Write $\lambda\circ j = \langle\cdot,u_0\rangle+\langle\cdot,u_1\rangle$ with
$\|u_0\|+\|u_1\|\le C\|\lambda\|$. Then $\lambda(v) = \langle Bv,u_0\rangle+\langle R_2v,u_1\rangle = \langle
v,u\rangle$, $u := B^*u_0+R_2^*u_1\in H^{\mathsf s}$, $\|u\|_{H^{\mathsf s}}\le C'\|\lambda\|$. $\square$

**Definition 7.2 ([Hin26c] Definition 3.16).** For $\Omega\subset M$ open, $\dot H^{\mathsf s}_{\mathcal
V_\sigma}(\bar\Omega) := \{u\in H^{\mathsf s}_{\mathcal V_\sigma}(M):\mathrm{supp}\,u\subset\bar\Omega\}$ and $\bar
H^{\mathsf s}_{\mathcal V_\sigma} (\Omega) := \{u|_\Omega:u\in H^{\mathsf s}_{\mathcal V_\sigma}(M)\}$ with the quotient
norm, i.e. the norm of the minimal extension.

**Lemma 7.3 ([Hin26c] Lemma 3.17).** The $L^2$ pairing extends to $\bar H^{\mathsf s}(\Omega)\times\dot H^{-\mathsf
s}(\bar \Omega)$ with a uniform bound, and $c\|u\|_{\bar H^{\mathsf s}(\Omega)}\le\sup_{\|v\|_{\dot H^{-\mathsf
s}(\bar\Omega)} = 1}| \langle u,v\rangle|\le C\|u\|_{\bar H^{\mathsf s}(\Omega)}$, uniformly; likewise with the roles
exchanged.

*Proof.* With $\tilde u$ the minimal extension, $|\langle u,v\rangle| = |\langle\tilde u,v\rangle|\le C\|\tilde
u\|\|v\|$. For the lower bound, extend $\lambda\in\dot H^{-\mathsf s}(\bar\Omega)^*$ by 0 on the orthogonal complement
to $\tilde\lambda$ of the same norm, represent it by $\tilde u$ (Lemma 7.1 (2)), and put $u := \tilde u|_\Omega$; then
$\lambda(v) = \langle v, u\rangle$ for $v$ supported in $\bar\Omega$, and $\|u\|_{\bar H^{\mathsf s}}\le\|\tilde u\|\le
C\|\lambda\|$. The other case is the same with the roles of the spaces exchanged. $\square$

**Proposition 7.4 ([Hin26c] Proposition 3.18).** In the setting of (S9) with $\Omega\subset X$ open, the Fourier
transform in $t$ is an isomorphism $\dot H^{\mathsf s}_{\mathcal V}(\mathbb R\times\bar\Omega)\to L^2(\mathbb
R_\sigma;\langle\tau\sigma \rangle^{-\mathsf s}\dot H^{\mathsf s}_{\hat{\mathcal V}_\sigma}(\bar\Omega))$ and $\bar
H^{\mathsf s}_{\mathcal V}(\mathbb R \times\Omega)\to L^2(\mathbb R_\sigma;\langle\tau\sigma\rangle^{-\mathsf s}\bar
H^{\mathsf s}_{\hat{\mathcal V}_\sigma}(\Omega))$.

*Proof.* The supported case is (S9) restricted to the closed subspace of distributions supported in $\mathbb R\times\bar
\Omega$, whose transforms are supported in $\bar\Omega$ for each $\sigma$. For the extendible case, by Lemma 7.3
(without parameter), the supported case, Lemma 7.3 (1) at each $\sigma$ and Cauchy-Schwarz, $\|u\|^2_{\bar H^{\mathsf
s}}\le C\sup_{\|v\|_{\dot H^{-\mathsf s}} = 1}|\int\langle\hat u(\sigma),\hat v(\sigma)\rangle d\sigma|^2 \le C'\|\hat
u\|^2_{L^2(\langle\tau\sigma\rangle^{-\mathsf s}\bar H^{\mathsf s}_{\hat{\mathcal V}_\sigma})}$; the converse inequality
follows by applying (S9) to the minimal extension. $\square$

Hence Lemmas 5.1, 5.2 and 6.2 hold for supported and extendible distributions. For the domain $\Omega$ of Definition
1.3, $H^{\mathsf s}_{e3b}(\Omega)^{\bullet,-}$ denotes the restrictions to $\{r>r_0\}$ of elements of $H^{\mathsf
s}_{e3b}(\tilde M)$ supported in $\{t-r\ge1\}$, and $H^{(\mathsf s;k)}_{e3b;b}(\Omega)^{\bullet,-}$ likewise, with
weights ([Hin26c] (3.65)): the spacetime domain of forward problems.

## 8. $L^\infty$-spaces, operators of limited regularity, Sobolev embedding

Fix a good spanning set $V_1,\dots,V_N\in\mathcal V_{b,[e3b]}(\tilde M)$ with weights $w_j$ (Lemma 2.9), and put
$V_{0,j} := w_jV_j$ and $V_0 := I$. For a word $J = (j_1,\dots,j_p)$ in $\{1,\dots,N\}$ write $V^J := V_{j_1}\cdots
V_{j_p}$ and $|J| := p$, and likewise $V_0^I := V_{0,i_1}\cdots V_{0,i_q}$. Then $\mathrm{Diff}^k_b(\tilde M)$ is the
$C^\infty(\tilde M)$-span of the $V^J$ with $|J|\le k$, and $\mathrm{Diff}^d_{e3b}(\tilde M)$ that of the $V_0^I$ with
$|I|\le d$. Write $w_{(\alpha)} := x_I^{2\alpha_I}\rho_+^{\alpha_+}\rho_K^{\alpha_K}$ for $\alpha =
(\alpha_I,\alpha_+,\alpha_K)$, with the defining functions of section 1. For every b-vector field $V$, $Vw_{(\alpha)}\in
w_{(\alpha)}C^\infty(\tilde M)$. On the mixed spaces of section 4.2 we use the norm

$$\|u\|_{H^{(\mathsf s;k)}_{e3b;b}} := \sum_{|J|\le k}\|V^Ju\|_{H^{\mathsf s}_{e3b}},\tag{8.1}$$

which is equivalent to the norm of (S3). Indeed $\mathcal W = C^\infty_b\mathcal V_b$ is spanned over $C^\infty_b$ by
the $V_j$ (Lemma 2.9). A product of $j$ elements of $\mathcal W$ is a $C^\infty_b$-combination of the $V^J$ with $|J|\le
j$, since b-derivatives of $C^\infty_b$-functions are $C^\infty_b$. And multiplication by $C^\infty_b$-functions is
bounded on $H^{\mathsf s}_{e3b}$, these functions being symbols of order 0 ((S4), (S5)). Weights are suppressed in
sections 8.3-8.4 and 9, as in the source. Every statement there holds on weighted spaces. To see this, apply it to
$w^{-1}u$ and to the conjugated operators $w^{-1}Aw$, $w = w_{(\alpha)}$. These lie in the same classes with the same
principal symbols and wave front sets: $w$ is a weight in the sense of (S2) ((S5) for the composition $w^{-1}\cdot
A\cdot w$), and for coefficients $w^{-1}aw = a$.

### 8.1 e3b-continuous functions

**Definition 8.1 ([Hin26c] Definition 3.19).** Let $d_0\in\mathbb N_0$ and $\alpha_I,\alpha_+,\alpha_K\in\mathbb R$.
Then $C^{d_0,(2\alpha_I,\alpha_+,\alpha_K)}_{e3b}(\tilde M)$ is the space of $C^{d_0}$-functions $u$ on $\tilde M^\circ
= \mathbb R^{1+4}$ with $w_{(\alpha)}^{-1}Au\in L^\infty$ for all $A\in\mathrm{Diff}^{d_0}_{e3b}(\tilde M)$. For
$k\in\mathbb N_0$, the space $C^{(d_0;k),(2\alpha_I,\alpha_+,\alpha_K)}_{e3b;b}(\tilde M)$ is defined by the same
condition for all combinations of products $A_1A_2$ with $A_1\in\mathrm{Diff}^k_b$ and
$A_2\in\mathrm{Diff}^{d_0}_{e3b}$. For $d_0 = 0$ it is written $C^{k,(2\alpha_I,\alpha_+,\alpha_K)}_b(\tilde M)$. The
norm is

$$\|u\|_{C^{(d_0;k),(2\alpha_I,\alpha_+,\alpha_K)}_{e3b;b}} := \sum_{|J|\le k,\ |I|
\le d_0}\sup|w_{(\alpha)}^{-1}V^JV_0^Iu|.$$

This norm dominates $\sup|w_{(\alpha)}^{-1}A_1A_2u|$ for all $A_1$, $A_2$ as above. Write $A_1 = \sum f_JV^J$ and $A_2 =
\sum g_IV_0^I$ with $f_J,g_I\in C^\infty(\tilde M)$. By the Leibniz rule $A_1A_2$ is a combination of products
$V^{J'}V_0^I$, $|J'|\le k$, with coefficients that are b-derivatives of the $g_I$ times the $f_J$. These are bounded, as
$\tilde M$ is compact and b-vector fields preserve $C^\infty(\tilde M)$. The space is a Banach space. On a compact set
$K\subset\tilde M^\circ$ the $V_{0,j}$ span the tangent space with smooth coefficients, and $w_{(\alpha)}$ is bounded
above and below there, so the norm dominates the $C^{d_0}(K)$-norm. A Cauchy sequence therefore converges in
$C^{d_0}_{\mathrm{loc}}$, and the weighted suprema pass to the limit.

**Lemma 8.2.** (a) Replacing $A_1A_2$ by $A_2A_1$ in Definition 8.1 gives the same space with an equivalent norm. (b)
For $|J|\le k$, $\|V^Ju\|_{C^{(d_0;k-|J|),(\alpha)}}\le C\|u\|_{C^{(d_0;k),(\alpha)}}$. (c)
$\|uv\|_{C^{(d_0;k),(\alpha+\beta)}} \le C_k\sum_{j\le k}\|u\|_{C^{(d_0;j),(\alpha)}}\|v\|_{C^{(d_0;k-j),(\beta)}}$. (d)
For $f\in C^\infty(\tilde M)$, $\|fu\|_{C^{(d_0;k),(\alpha)}}\le C_{f,k}\|u\|_{C^{(d_0;k),(\alpha)}}$; and
$C^{(d_0;k),(2\delta,\delta,\delta)}\subset C^{(d_0;k)}$ continuously for $\delta\ge0$.

*Proof.* (a) Each $V_j$ is an e3b-commutator field, so $[V_j,V_{0,i}]\in\mathcal V_{e3b} = \sum_lC^\infty(\tilde
M)V_{0,l}$. As $[V_j,\cdot]$ is a derivation, $[V_j,A_2]\in\mathrm{Diff}^{d_0}_{e3b}$ for
$A_2\in\mathrm{Diff}^{d_0}_{e3b}$. Induction on $|J|$ gives $V^JA_2 = \sum A_2'V^{J'}$ and $A_2V^J = \sum V^{J'}A_2''$,
with $A_2',A_2''\in\mathrm{Diff}^{d_0}_{e3b}$ and $|J'|\le|J|$. The coefficients are smooth on $\tilde M$, hence bounded
with bounded derivatives. (b) $V^{J''}V_0^IV^Ju$ with $|J''|\le k-|J|$ is, by (a), a combination of $V^{J'''}V_0^{I'}u$
with $|J'''|\le k$ and $|I'|\le d_0$. (c) The Leibniz rule: $V^JV_0^I(uv)$ is a sum of products
$(V^{J_1}V_0^{I_1}u)(V^{J_2}V_0^{I_2}v)$ with $|J_1|+|J_2| = |J|$ and $|I_1|+ |I_2| = |I|$, the subwords keeping their
order. (d) Leibniz again, and $w_{(2\delta,\delta,\delta)}\le C$ for $\delta \ge0$. $\square$

### 8.2 Operators of limited regularity

**Definition 8.3 ([Hin26c] Definition 3.20).** For $m,\mathsf s$ and $d_0,k\in\mathbb N_0$,
$C^{(d_0;k)}_{e3b;b}\mathrm{Diff}^m_{e3b}(\tilde M)$, resp. $C^{(d_0;k)}_{e3b;b}\Psi^{\mathsf s}_{e3b}(\tilde M)$, is
the space of finite sums $\sum a_jP_j$ with $a_j\in C^{(d_0;k)}_{e3b;b}$ and $P_j\in\mathrm{Diff}^m_{e3b}$, resp.
$P_j\in C^\infty_b\Psi^{\mathsf s}_{e3b}$; weighted versions likewise. For a finite set $\mathcal P =
\{P_1,\dots,P_N\}$, the $C^{(d_0;k)}_{e3b;b}$-span of $\mathcal P$ is written $C^{(d_0;k)}_{e3b;b}\mathcal P$. A
*representation* of $A\in C^{(d_0;k)}_{e3b;b}\mathcal P$ is a tuple $\mathbf a = (a_1,\dots,a_N)$ with $A = \sum
a_jP_j$, and we write $\|\mathbf a \|_{(d_0;k)} := \max_j\|a_j\|_{C^{(d_0;k)}_{e3b;b}}$. The source's norms
(3.68)-(3.69) are the infimum of $\|\mathbf a \|_{(d_0;k)}$ over representations.

Statements below whose constants depend on $A$ only through a bound for $\|\mathbf a\|_{(d_0;k)}$ hold equally with the
infimum norm. If $\|A'-A\|<\epsilon$ in that norm, then $A'$ has a representation with $\|\mathbf
a'\|\le\|A\|+2\epsilon$. The tame estimates (Propositions 9.7-9.8) bound one quantity by a low norm of the coefficients
times a high norm of $u$, plus a high norm of the coefficients times a low norm of $u$. They are stated for a given
representation, whose low and high norms both enter. With the infimum norm, the low and the high norm may be nearly
attained by different representations, and the argument does not combine them (section 10, (G3)).

### 8.3 Smooth operators on mixed spaces

*Cut-offs.* [SBG] Definition 3.34 calls an operator *localized near the diagonal* when its Schwartz kernel is supported
within a finite $d_{\mathcal B}$-distance of the diagonal. This is a property an operator of the calculus may or may not
have, and residual operators need not have it ([SBG] Remark 3.48). Here the operators of $\mathcal P$ and all auxiliary
operators are taken localized near the diagonal. Quantizations are, by the cut-off $\psi(x-x')$ of [SBG] (3.26) and the
chart cut-offs of Definition 3.31. The class is closed under compositions and adjoints, since kernel supports add, resp.
are reflected, and under commutators with vector fields, and it contains the finite-order parametrices of Lemma 8.4 (b),
which are quantizations. For $\chi\in C^\infty(\tilde M)$, an operator $A$ is *carried by* $\chi$ if $A = \chi'A\chi'$
for some $\chi'\in C^\infty(\tilde M)$ such that $\chi = 1$ within $d_{\mathcal B}$-distance $D$ of
$\mathrm{supp}\,\chi'$. Here $D$ bounds the kernel ranges of the finitely many operators of the statement at hand; for
differential operators $\chi = 1$ on $\mathrm{supp}\,\chi'$ suffices. Then $A\chi = A = \chi A$, and $AP = AP\chi$ for
each operator $P$ of the statement. The source writes $B = \chi B\chi$, and its estimates are read with this convention.
The source does not require the localization ([Hin26c] p. 48); the restriction is recorded in section 10. Auxiliary
operators chosen in a proof are carried by cut-offs nested between $\chi'$ and $\chi$.

**Lemma 8.4.** Let $A\in C^\infty_b\Psi^{m'}_{e3b}$, $m'\in\mathbb R$, and let $\mathsf s$ be a variable order.

(a) $A$ maps $H^{(\mathsf s;k)}_{e3b;b}\to H^{(\mathsf s-m';k)}_{e3b;b}$ boundedly for every $k$. For $V\in\mathcal
V_{b,[e3b]}$, $[V,A]\in C^\infty_b\Psi^{m'}_{e3b}$ with $\mathrm{WF}'_{e3b}([V,A])\subset\mathrm{WF}'_{e3b}(A)$;
iterated commutators $\mathrm{ad}_{V_{j_1}}\cdots\mathrm{ad}_{V_{j_q}}A$ likewise.

(b) (Microlocal parametrix.) Let $B\in C^\infty_b\Psi^{m_B}_{e3b}$ with
$\mathrm{WF}'_{e3b}(B)\subset\mathrm{Ell}_{e3b}(A)$, and $J\in\mathbb N$. Then $B = QA+R$ with $Q\in
C^\infty_b\Psi^{m_B-m'}_{e3b}$ and $R\in C^\infty_b\Psi^{m_B-J}_{e3b}$.

(c) In (b), if $B$ and $A$ are carried by $\chi$, then for all $\mathsf s$, $N$, $k$,
$$\|Bu\|_{H^{(\mathsf s-m_B;k)}_{e3b;b}}\le C\big(\|Au\|_{H^{(\mathsf s-m';k)}_{e3b;b}}+\|\chi u\|_{H^{(-N;k)}_{e3b;b}}
\big).$$

(d) $H^{(\mathsf s;k)}_{e3b;b}\subset H^{(\mathsf s+1;k-1)}_{e3b;b}$ continuously for $k\ge1$; hence $H^{(\mathsf
s;k)}_{e3b;b}\subset H^{\mathsf s+k}_{e3b}$, and $H^{\bar s}_b = H^{(0;\bar s)}_{e3b;b}\subset H^{\bar s}_{e3b}$ for
$\bar s\in\mathbb N_0$.

*Proof.* (a) The mapping property is (S5) with (S8) for variable orders. The operators are taken in the subalgebra of
(S10) (section 4.2), and the $V_j$ lie in $\mathcal W_{[\mathcal V]}$. The commutator statement is (4.1), and the
iterated one follows by induction.

(b) Let $a$ and $b$ be principal symbols of $A$ and $B$. Choose symbols $\tilde\chi_0,\dots,\tilde\chi_{J-1}\in S^0$,
each equal to 1 near the support of the previous one, with $\tilde\chi_0 = 1$ near $\mathrm{WF}'_{e3b}(B)$ and all
supported in a closed subset of $\mathrm{Ell}_{e3b}(A)$ on which $|a|\ge c\lambda^{-m'}$ ($\lambda$ the elliptic weight
of (S8)). Put $Q_0 := \mathrm{Op}(\tilde\chi_0b/a)\in C^\infty_b\Psi^{m_B-m'}_{e3b}$. Then $R_1 := B-Q_0A$ has principal
symbol $(1- \tilde\chi_0)b$. This lies in $S^{-\infty}$, since $\tilde\chi_0 = 1$ near the essential support of $b$. So
$R_1\in C^\infty_b\Psi^{m_B-1}_{e3b}$ by the principal symbol sequence (S5), and
$\mathrm{WF}'_{e3b}(R_1)\subset\mathrm{supp} \tilde\chi_0$. Inductively, given $R_j\in C^\infty_b\Psi^{m_B-j}_{e3b}$
with wave front set in $\mathrm{supp}\tilde\chi _{j-1}$, put $Q_j := \mathrm{Op}(\tilde\chi_j\sigma(R_j)/a)$ and
$R_{j+1} := R_j-Q_jA\in C^\infty_b\Psi^{m_B-j-1}_{e3b}$. Then $B = (\sum_{j<J}Q_j)A+R_J$. Only finitely many steps are
taken, so no asymptotic summation is needed.

(c) $Bu = B(\chi u) = QA\chi u+R_J\chi u = QAu+R_J\chi u$, because $A\chi = A$ and $B\chi = B$ for operators carried by
$\chi$. Take $J\ge\sup\mathsf s+N$ and use (a).

(d) By Lemma 4.1 (with (S8) for variable orders), an elliptic $\Lambda\in C^\infty_b\Psi^{\mathsf s+1}_{e3b}$ is
$\sum_{l = 0}^N\Lambda_lV_l$ with $\Lambda_l\in C^\infty_b\Psi^{\mathsf s}_{e3b}$. Microlocal elliptic regularity (S5),
with $I$ in place of $B$, gives $\|v\|_{H^{\mathsf s+1}}\le C(\|\Lambda v\|_{L^2}+\|v\|_{H^{-N}})\le
C\sum_l\|V_lv\|_{H^{\mathsf s}}$. Apply this to $v = V^Ju$, $|J|\le k-1$, and sum, using (8.1). Iterating gives the
second claim. For the third, $H^{\bar s}_b$ is by definition the space of $u$ with $V^Ju\in L^2$ for $|J|\le\bar s$.
$\square$

### 8.4 Multiplication and pseudolocality

**Lemma 8.5 (the part of [Hin26c] Lemma 3.5 that is used, and the pseudolocality in the proof of its Proposition
3.28).** Let $\mathsf s,\mathsf s_0$ be variable orders.

(a) There are $d_0\in\mathbb N$ and $C$ with $\|\ell u\|_{H^{\mathsf s}_{e3b}}\le
C\|\ell\|_{C^{d_0}_{e3b}}\|u\|_{H^{\mathsf s}_{e3b}}$ for all $\ell\in C^{d_0}_{e3b}$. Moreover, for every $k$, $\|\ell
u\|_{H^{(\mathsf s;k)}_{e3b;b}}\le C_k\sum_{j \le k}\|\ell\|_{C^{(d_0;j)}_{e3b;b}}\|u\|_{H^{(\mathsf s;k-j)}_{e3b;b}}$,
with the same $d_0$.

(b) Let $B,B^\sharp\in C^\infty_b\Psi^0_{e3b}$ with $\mathrm{WF}'_{e3b}(I-B^\sharp)\cap\mathrm{WF}'_{e3b}(B) =
\emptyset$. Then there are $d_0$ and $C$ with $\|B\ell(I-B^\sharp)u\|_{H^{\mathsf s}_{e3b}}\le
C\|\ell\|_{C^{d_0}_{e3b}}\|u\|_{H^{\mathsf s_0}_{e3b}}$.

*Proof.* *Smooth coefficients.* Let $C^\infty_{e3b}$ be the space of functions all of whose e3b-derivatives are bounded.
With the seminorms $\|\cdot\|_{C^d_{e3b}}$ it is a Fréchet space. Such a function $\ell$ is a symbol of order 0,
independent of the fibre variable, for the secondary b.g. structure $\rho\mathcal B$. In its charts the e3b-vector
fields are the uniformly bounded combinations of the coordinate fields ([SBG] Remark 3.33, READ in section 3 as (S6)).
Its quantization is multiplication by $\ell$: in the local quantization of [SBG] (3.26) the cut-off $\psi(x-x')$ equals
1 near $x = x'$, so a fibre-independent symbol is quantized to multiplication by itself, and the cut-offs $\chi_\alpha$
of [SBG] Definition 3.31 sum to 1. Hence multiplication by $\ell$ lies in $\tilde\Psi^0_{e3b}$, which is bounded on
$H^{\mathsf s}_{e3b}$ (section 4.2, with (S8)). Consider $T:\ell\mapsto(u\mapsto\ell u)$, from $C^\infty_{e3b}$ to
$\mathcal L(H^{\mathsf s}_{e3b})$. Its graph is closed. Suppose $\ell_n\to\ell$ in $C^\infty_{e3b}$ and $T\ell_n\to T'$.
For $u\in H^{\mathsf s}_{e3b}$ (a distribution on $\mathbb R^{1+4}$, locally in $H^{\inf\mathsf s}$), $\ell_nu\to\ell u$
in $\mathcal D'$. So $T'u = \ell u$. By the closed graph theorem (Fréchet to Banach), $T$ is continuous, that is,
$\|T\ell\|\le C\|\ell\|_{C^{d_0}_{e3b}}$ for some $d_0$. Likewise $\ell\mapsto B\ell(I-B^\sharp)\in\mathcal L(H^{\mathsf
s_0}_{e3b},H^{\mathsf s}_{e3b})$ is well defined, as $B\ell(I-B^\sharp)\in\tilde\Psi^0_{e3b}$ has empty wave front set
((S5)) and so lies in $\tilde\Psi^{-\infty}_{e3b}$. Its graph is closed by the same argument, the convergence holding in
$\mathcal L(H^{\mathsf s_0},H^{\mathsf s_0})$. So it is bounded by $C\|\ell\|_{C^{d_0}_{e3b}}$.

*Finite regularity.* Let $d_*$ be the largest of the numbers just found, for (a) at the orders $\mathsf s$ and $\mathsf
s_0$ and for (b), $K := \max(0,\lceil-\inf\mathsf s\rceil, \lceil-\inf\mathsf s_0\rceil)$, and put $d_0 := d_*+K+1$. Let
$\ell\in C^{d_0}_{e3b}$. In the charts $\psi_\beta$ of $\rho\mathcal B$, with a uniformly smooth partition of unity
$\theta_\beta$ and a mollifier $\eta_\epsilon$, put $\ell_\epsilon :=
\sum_\beta((\theta_\beta\ell)\circ\psi_\beta^{-1}*\eta_\epsilon)\circ\psi_\beta$. Derivatives commute with convolution,
the charts have uniformly bounded transitions and finite multiplicity, and e3b-derivatives are uniformly equivalent to
coordinate derivatives in these charts. Hence $\|\ell_\epsilon\|_{C^{d}_{e3b}}\le C\|\ell\|_{C^{d}_{e3b}}$ for $d\le
d_0$, and $\ell_\epsilon\in C^\infty_{e3b}$. Moreover $\ell_\epsilon\to\ell$ in $C^{K}$ on compact sets. For $u\in
H^{\mathsf s}_{e3b}$, $\ell_\epsilon u\to\ell u$ in $\mathcal D'$, while $\|\ell_\epsilon u\|_{H^{\mathsf s}}\le C\|
\ell\|_{C^{d_*}_{e3b}}\|u\|_{H^{\mathsf s}}$. A subsequence converges weakly in the Hilbert space $H^{\mathsf s}_{e3b}$,
which embeds continuously in $\mathcal D'$, so its limit is $\ell u$. The norm is weakly lower semicontinuous, which
gives the first claim of (a). For (b), $\ell_\epsilon(I-B^\sharp)u\to\ell(I-B^\sharp)u$ weakly in $H^{\mathsf s_0}$, by
the first claim and the same argument. $B$ is weakly continuous on $H^{\mathsf s_0}$, and the bound holds uniformly in
$\epsilon$. So the limit $B\ell(I-B^\sharp)u$ lies in $H^{\mathsf s}$ with the bound.

*b-regularity.* By (8.1) and the Leibniz rule, $V^J(\ell u) = \sum(V^{J_1}\ell)(V^{J_2}u)$ over splittings of $J$, and
$\|V^{J_1}\ell\|_{C^{d_0}_{e3b}}\le C\|\ell\|_{C^{(d_0;|J_1|)}_{e3b;b}}$ by Lemma 8.2 (a). $\square$

The source states (a) as a consequence of its Lemma 3.5, whose proof is by inspection of [SBG] Proposition 3.32. It uses
(b) in the proof of its Proposition 3.28 for smooth $\ell$ and applies it to finite-regularity $\ell$. Here both are
proved from (S5), (S6), (S8) and the closed graph theorem.

**Lemma 8.6 (operators of limited regularity).** Let $\mathcal P\subset C^\infty_b\Psi^m_{e3b}$ be finite and $A\in
C^{(d_0;k)}_{e3b;b}\mathcal P$, with a representation $\mathbf a$. Let $\mathsf s$ and $N$ be given. There is $d_0 =
d_0(\mathsf s,m,N)$, independent of $k$, such that:

(a) $\|Au\|_{H^{(\mathsf s-m;k)}_{e3b;b}}\le C_k\|\mathbf a\|_{(d_0;k)}\|u\|_{H^{(\mathsf s;k)}_{e3b;b}}$;

(b) if $G,G'\in C^\infty_b\Psi^0_{e3b}$, both carried by $\chi$, with
$\mathrm{WF}'_{e3b}(G)\subset\mathrm{Ell}_{e3b}(G')$, then $\|GAu\|_{H^{(\mathsf s-m;k)}_{e3b;b}}\le C_k\|\mathbf
a\|_{(d_0;k)}(\|G'u\|_{H^{(\mathsf s;k)}_{e3b;b}}+\|\chi u\| _{H^{(-N;k)}_{e3b;b}})$.

*Proof.* (a) Lemma 8.5 (a) at the order $\mathsf s-m$, and Lemma 8.4 (a) for the $P_j$. (b) First $k = 0$. Choose $G'',
G'''\in C^\infty_b\Psi^0_{e3b}$ carried by $\chi$, microlocally equal to $I$ near $\mathrm{WF}'_{e3b}(G)$, with
$\mathrm{WF} '_{e3b}(G'')\subset\mathrm{Ell}_{e3b}(G')$ and $\mathrm{WF}'_{e3b}(G''')\cap\mathrm{WF}'_{e3b}(I-G'') =
\emptyset$. By the support convention, $GAu = GA\chi u$. Then
$$Ga_jP_j\chi u = Ga_jP_jG''\chi u+Ga_j(I-G''')P_j(I-G'')\chi u+Ga_jG'''P_j(I-G'')\chi u.$$
By Lemma 8.5 (a) and Lemma 8.4 (c), the first term is bounded by $C\|a_j\|_{C^{d_0}}(\|G'u\|_{H^{\mathsf s}}+\|\chi u\|
_{H^{-N}})$. The second is bounded by $C\|a_j\|_{C^{d_0}}\|\chi u\|_{H^{-N}}$, by Lemma 8.5 (b) with $\mathsf s_0 =
-N-m$. In the third, $G'''P_j(I-G'')\in C^\infty_b\Psi^{-\infty}_{e3b}$, since the wave front sets are disjoint (S5).
For $k\ge1$, argue by induction. By (8.1) it suffices to bound $\|V_iGAu\|_{H^{(\mathsf s-m;k-1)}}$, and
$$V_iGa_jP_ju = [V_i,G]a_jP_ju+G(V_ia_j)P_ju+Ga_j[V_i,P_j]u+Ga_jP_jV_iu.$$
The first three terms are of the form treated at level $k-1$. They involve $[V_i,G]$ (wave front set in that of $G$) or
the coefficients $V_ia_j\in C^{(d_0;k-1)}$ (Lemma 8.2 (b)), or the finite set $\mathcal P\cup\{[V_i,P_j]\}$. For the
last, choose $G_\flat$ carried by $\chi$ with $\mathrm{WF}'(G)\subset\mathrm{Ell}(G_\flat)$ and $\mathrm{WF}'(G_\flat)
\subset\mathrm{Ell}(G')$. The level $k-1$ bounds it by $C\|\mathbf a\|(\|G_\flat V_iu\|_{(\mathsf s;k-1)}+\|\chi_1V_iu\|
_{(-N;k-1)})$, with an inner cut-off $\chi_1$ carrying $G,G_\flat$. Next, $\|G_\flat V_iu\|_{(\mathsf
s;k-1)}\le\|G_\flat u\|_{(\mathsf s;k)}+\|[G_\flat,V_i]u\|_{(\mathsf s;k-1)}$, and both are bounded by
$C(\|G'u\|_{(\mathsf s;k)}+\|\chi u\| _{(-N;k)})$ (Lemma 8.4 (c)). Finally
$\|\chi_1V_iu\|_{(-N;k-1)}\le\|V_i(\chi_1u)\|+\|(V_i\chi_1)\chi u\|\le C\|\chi u\| _{(-N;k)}$, as $\chi = 1$ on
$\mathrm{supp}\,\chi_1$. $\square$

### 8.5 Sobolev embedding

**Lemma 8.7 ([Hin26c] Lemma 3.21).** Let $\mathsf s$ be a variable e3b-order, $\underline s := \max(0,\lceil-\inf\mathsf
s\rceil)$, and $k\ge\underline s$. Then $H^{(\mathsf s;k)}_{e3b;b}\subset H^{k-\underline s}_b$, continuously and with
weights.

*Proof.* If $\underline s = 0$ then $\mathsf s\ge0$ and $H^{(\mathsf s;k)}\subset H^{(0;k)} = H^k_b$. Otherwise let $A_j
:= V_{0,j}^{\underline s}$, $j = 1,\dots,N$. The symbols $\xi\mapsto\xi(V_{0,j})$ vanish simultaneously only at $\xi =
0$, as the $V_{0,j}$ span ${}^{e3b}T\tilde M$. So $\sum_jA_jA_j^*\in\mathrm{Diff}^{2\underline s}_{e3b}$ is elliptic,
with a parametrix $Q\in C^\infty_b\Psi^{-2\underline s}_{e3b}$ and $\sum A_jA_j^*Q = I-R$, $R\in
C^\infty_b\Psi^{-\infty}_{e3b}$ ((S5); or Lemma 8.4 (b) with $J$ large, which suffices). With $B_j := A_j^*Q\in
C^\infty_b\Psi^{-\underline s}_{e3b}$, $u = \sum_jA_jB_ju+Ru$. Here $B_ju\in H^{(\mathsf s+\underline s;k)}\subset
H^{(0;k)} = H^k_b$ (Lemma 8.4 (a); $\mathsf s+ \underline s\ge0$), and $A_j\in\mathrm{Diff}^{\underline s}_b$ maps
$H^k_b\to H^{k-\underline s}_b$. Also $Ru\in H^{(J;k)}\subset H^k_b$ for $R$ of order $-J\le0$. $\square$

**Lemma 8.8 ([Hin26c] Lemma 3.22 at n = 4).** Let $d\in\mathbb N_0$ and $\alpha_I,\alpha_+,\alpha_K\in\mathbb R$. Then
for $u$ supported in $\Omega$ (Definition 1.3),
$$\|u\|_{C^{d,(2(\alpha_I+2),\alpha_++\frac52,\alpha_K+\frac12)}_b}\le C\|u\|_{H^{d+3,(2\alpha_I,\alpha_+,
\alpha_K)}_b(\tilde
M;|dt\,dx|)}.\tag{8.2}$$
For an unweighted b-density $\mu_b$ on $\tilde M$ and all $\gamma_I,\gamma_+,\gamma_K$,
$\|u\|_{C^{d,(2\gamma_I,\gamma_+,\gamma_K)}_b}\le C\|u\|_{H^{d+3,(2\gamma_I,\gamma_+,\gamma_K)}_b(\tilde M,\mu_b)}$,
and, for $u$ supported in $\Omega$ and every $\delta>0$,
$$\|u\|_{H^{d,(2\gamma_I,\gamma_+,\gamma_K)}_b(\tilde M,\mu_b)}\le C_\delta\|u\|_{C^{d,(2\gamma_I+\delta,\gamma_++\delta,
\gamma_K+\delta)}_b}.\tag{8.3}$$

*Proof.* *The density.* With the explicit defining functions on $\Omega$ (section 1),
$$x_I^8\rho_+^5\rho_K = \Big(\frac{t_*}{t_*+r}\Big)^4\Big(\frac{t_*+r}{t_*r}\Big)^5\frac r{t_*+r} = \frac1{t_*r^4}.$$
The density $\mu_b := |dt_*\,dx|/(t_*\langle x\rangle^4)$ is a smooth positive b-density on $\tilde M$ near
$\bar\Omega$. Near $\iota^+$ this is Lemma 6.1. Near the interior of $K^+$, where $t_*\sim t$ and $r$ is bounded, it is
$\langle x\rangle^{-4}|\frac{dt}t\,dx|$. Near the interior of $\mathscr I^+$, where $t_*\in[1,T]$, it is $t_*^{-1}|dt_*
\,\frac{dr}r\,d\omega|$ times a smooth positive function, and $\frac{dr}r$ is $-2\frac{dx_I}{x_I}$ there. Since $\langle
x\rangle\sim r$ on $\Omega$ ($r\ge r_0>0$), $|dt\,dx| = |dt_*\,dx| = c\,x_I^{-8}\rho_+^{-5}\rho_K^{-1}\mu_b$ with $c$
smooth and positive. Thus $L^2(|dt\,dx|) = x_I^4\rho_+^{5/2}\rho_K^{1/2}L^2(\mu_b)$, and b-derivatives commute with the
weights up to bounded factors. So $H^{d+3,(2\alpha_I,\alpha_+,\alpha_K)}_b(|dt\,dx|) =
H^{d+3,(2(\alpha_I+2),\alpha_++\frac 52,\alpha_K+\frac12)}_b(\mu_b)$ for $u$ supported in $\Omega$, and (8.2) follows
from the second claim. At $n = 3$ the same product is $x_I^6\rho_+^4\rho_K = t_*^{-1}r^{-3}$, giving the source's
$(2(\alpha_I+\frac32),\alpha_++2,\alpha_K+\frac12)$.

*The embedding.* Writing $u = w_{(\gamma)}v$ reduces to $\gamma = 0$, again because b-derivatives of $w_{(\gamma)}$ are
$w_{(\gamma)}$ times smooth functions. Cover the compact manifold with corners $\tilde M$ by finitely many charts
$[0,1)^q_x\times\mathbb R^{5-q}_y$, with a subordinate partition of unity $\{\psi_i\}$. In logarithmic coordinates $z_j
= -\log x_j$ the b-fields are $\partial_{z_j}$, $\partial_y$, and $\mu_b$ is $|dz\,dy|$ times a smooth positive bounded
function. $\psi_iu$, extended by 0, is a function on $\mathbb R^5_{z,y}$ with $\|\psi_iu\|_{H^{d+3}(\mathbb R^5)}\le
C\|u\| _{H^{d+3}_b}$. The Sobolev embedding $H^{d+3}(\mathbb R^5)\hookrightarrow C^d(\mathbb R^5)$ holds since
$3>\frac52$: for $|\beta|\le d$, $\|\partial^\beta f\|_{L^\infty}\le\int|\zeta^\beta\hat
f|\le\|f\|_{H^{d+3}}(\int\langle\zeta\rangle^{2| \beta|-2d-6}d\zeta)^{1/2}$. The sup norms of $z,y$-derivatives are the
$C^d_b$-norm. Sum over $i$. At the artificial boundary $r = r_0$ the spaces are extendible. Apply the embedding to an
extension of comparable norm and restrict.

*The converse (8.3).* Write $w := w_{(\gamma)}$ and $w' := wx_I^\delta\rho_+^\delta\rho_K^\delta$. Then
$\|w^{-1}V^Ju\|_{L^2 (\mu_b)}\le\|w'^{-1}V^Ju\|_{L^\infty}\|(x_I\rho_+\rho_K)^\delta\|_{L^2(\mu_b;\Omega)}$. The last
factor is finite. On $\bar\Omega$ the only boundary faces are $\mathscr I^+$, $\iota^+$, $K^+$, with defining functions
among $x_I$, $\rho_+$, $\rho_K$, and in logarithmic coordinates the integrand is $e^{-2\delta(z_1+\dots+z_q)}$ over
$z_j\ge z_0$, with $y$ in a compact set. $\square$

The last claim needs the support in $\Omega$. Near a face where no weight decays (for instance $I^0$), $\mu_b$ has
infinite mass. The source states the support condition once, for the whole lemma.

At $n = 4$, as a variant with the same proof (Part I.C Lemma 2.9 (c)):
$$H^{d+3,\alpha}_b(\overline{\mathbb R^4},|dx|)\hookrightarrow C^{d,\alpha+2}_b(\overline{\mathbb R^4}).\tag{8.4}$$
Here $|dx| = r^4\mu_b$ near infinity, so $L^2(|dx|) = \rho^2L^2(\mu_b)$, and the embedding $H^{d+3}(\mathbb R^4)\subset
C^d(\mathbb R^4)$ (as $3>2$) applies in the coordinates $(\log r,\omega)$, $\omega\in\mathbb S^3$. The source's (3.72),
at $n = 3$, has $\alpha+\frac32$.

## 9. Estimates on mixed spaces, and their tame versions

Orders: $m,N\in\mathbb R$, and $\mathsf s,\mathsf s_0\in C^\infty({}^{e3b}S^*\tilde M)$ variable orders; wave front
sets, elliptic and characteristic sets are those of the e3b-calculus, in ${}^{e3b}S^*\tilde M$. Cut-offs are as in
section 8.3, and weights are suppressed (section 8, beginning). For an operator $L = \sum a_jP_j$ of limited regularity,
$\mathrm{Ell}_{e3b}(L)$ is the set where its principal symbol $\ell = \sum a_j\sigma(P_j)$ is invertible with inverse
bounded by a constant times $\lambda^{m}$, $\lambda$ the elliptic weight of (S8); on $\mathbb C^{N'}$-valued functions,
$\sigma(P_j)$ is matrix-valued (section 4.3).

*Choosing auxiliary operators.* Let $K\subset{}^{e3b}S^*\tilde M$ be compact and $O\supset K$ open, over the interior of
$\{\chi = 1\}$. Then there are $B_1,B_2,\ldots\in C^\infty_b\Psi^0_{e3b}$, carried by nested cut-offs between $\chi'$ and
$\chi$, with $K\subset\mathrm{Ell}(B_1)$, $\mathrm{WF}'(B_i)\subset\mathrm{Ell}(B_{i+1})$ and all wave front sets in $O$.
Some $B_i$ may be chosen microlocally equal to $I$ near $K$, that is, with $\mathrm{WF}'(I-B_i)\cap K = \emptyset$.
Quantize symbols $\tilde\chi_i\in S^0$ with $\tilde\chi_i = 1$ near the support of $\tilde\chi_{i-1}$, and multiply by
cut-offs. The hypotheses of the propagation estimates are open. Let $T$ be the union of the backward segments of the
integral curves of $\mathsf H$ from $\mathrm{WF}'(B)\cap\mathrm{Char}(L)$ up to their first entry into $\mathrm{Ell}(E)$,
and suppose that they reach $\mathrm{Ell}(E)$ within a time $T_0$, remaining in $\mathrm{Ell}(G)$. Then
$T\subset\mathrm{Ell}(G)$ is compact: it is the image under the flow of the set of $(\alpha,t)$ with $0\le t\le
t_\alpha$, $t_\alpha$ the first entry time, and this set is closed because $\alpha\mapsto t_\alpha$ is upper
semicontinuous, $\mathrm{Ell}(E)$ being open. Moreover:

(O) For every neighbourhood $U\subset\mathrm{Ell}(G)$ of $T$ there are a neighbourhood $U_T\subset\mathrm{Ell}(G)$ of
$T\cup\mathrm{WF}'(B)$, with $U_T\cap\mathrm{Char}(L)\subset U$, and compact sets $K_E\subset\mathrm{Ell}(E)$ and
$K_U\subset U$, such that the backward curve from every point of $U_T\cap\mathrm{Char}(L)$ reaches $K_E$ within time
$T_0+1$ and stays in $K_U$ until then. $U_T$ may be replaced by any smaller neighbourhood of $T\cup\mathrm{WF}'(B)$.

For $\alpha\in\mathrm{WF}'(B)\cap\mathrm{Char}(L)$ choose $t'_\alpha\in(t_\alpha,t_\alpha+1)$ with
$\exp(-t'_\alpha\mathsf H)\alpha\in\mathrm{Ell}(E)$ and the curve on $[0,t'_\alpha]$ in $U$, which is possible as $U$ is
open. By the continuity of the flow, every point near $\exp(-t\mathsf H)\alpha$, $0\le t\le t_\alpha$, has a backward
curve that stays in a fixed compact neighbourhood in $U$ of $\exp(-[t,t'_\alpha]\mathsf H)\alpha$ up to the time
$t'_\alpha-t$, and then lies in a fixed compact neighbourhood of $\exp(-t'_\alpha\mathsf H)\alpha$ in $\mathrm{Ell}(E)$.
Finitely many such neighbourhoods cover the compact set $T$. Their union, together with a neighbourhood in
$\mathrm{Ell}(G)$ of the compact set $\mathrm{WF}'(B)\setminus U$ disjoint from $\mathrm{Char}(L)$, is $U_T$. The flow is
continuous although $\mathsf H$ is only continuous at $\partial\tilde M$: its integral curves are unique, and limits of
integral curves are integral curves (II.A$'$ Lemma 5.1 (c)). When $\mathsf H\mathsf s\le0$ on $U$, the hypotheses of (L4)
therefore hold for $(B',E',G')$ whenever $\mathrm{WF}'(B')\subset U_T$, $E'$ is elliptic on $K_E$ and $G'$ is elliptic on
$K_U\cup\mathrm{WF}'(B')$. Below, "slightly larger" and "slightly smaller" operators refer to such choices.

### 9.1 The standard estimates

The two statements below are [Hin26c] Propositions 3.23 and 3.24 for $k = 0$ (pp. 69-71), at $n = 4$. Their statements
and the source's proofs do not use the dimension. The source proves them by the standard elliptic parametrix and positive
commutator arguments. For variable orders it cites [Vas18] Theorem 5.3, with the sharp Gårding inequality on each unit
cell and a commutant as in [dHUV15]. It takes the coefficient regularity $d_0$ finite because the arguments use the
boundedness of finitely many operators on a fixed range of spaces. No text READ in this write-out states them on
e3b-spaces with coefficients of finite regularity and variable orders. [SBG] does not treat propagation (its section 3.6
says so). [HJS] has constant differential orders and no sharp Gårding inequality. Hintz's paper with Sobolev coefficients
(arXiv:1311.6859) has constant orders. They are therefore **standing inputs of this part, (L3) and (L4)**, proved in Part
II.A$'$ (section 10, (G5)-(G7)), with the hypotheses of (L4) corrected there. Everything else in sections 8 and 9 is
proved here, from them and from the calculus READ in section 3.

(L3) *(Elliptic estimate, $k = 0$.)* There is $d_0 = d_0(m,\mathsf s,N)$ such that the following holds for every finite
$\mathcal P\subset C^\infty_b\Psi^m_{e3b}$, every $N'$ and every $L\in C^{d_0}_{e3b}\mathcal P$ on $\mathbb
C^{N'}$-valued functions. (The source states the scalar case; with matrix-valued principal symbols the proof is the same,
II.A$'$ Theorem 3.1.) Let $B,G\in C^\infty_b\Psi^0_{e3b}$ be carried by $\chi$, with
$\mathrm{WF}'(B)\subset\mathrm{Ell}(G)\cap\mathrm{Ell}(L)$. If $\chi u\in H^{-N}_{e3b}$ and $GLu\in H^{\mathsf
s-m}_{e3b}$, then $Bu\in H^{\mathsf s}_{e3b}$ and
$$\|Bu\|_{H^{\mathsf s}_{e3b}}\le C\big(\|GLu\|_{H^{\mathsf s-m}_{e3b}}+\|\chi u\|_{H^{-N}_{e3b}}\big),$$
with $C$ uniform for $L$ in a neighbourhood in $C^{d_0}_{e3b}\mathcal P$ on which
$\mathrm{WF}'(B)\subset\mathrm{Ell}(L)$ holds with a uniform bound.

(L4) *(Real principal type propagation, $k = 0$; hypotheses corrected, section 10, (G6)-(G7).)* Let $m\in\mathbb N_0$.
There is $d_0 = d_0(m,\mathsf s,N)$ such that the following holds for every $\delta>0$, all finite sets $\mathcal
P_{m-j}\subset C^\infty_b\Psi^{m-j}_{e3b}$, $j = 0,1$, the elements of $\mathcal P_m$ having classical principal symbols,
every $N'$, and operators on $\mathbb C^{N'}$ of the form
$$L = L_0+L_1+L_2,\quad L_0\in\mathrm{Diff}^m_{e3b}\otimes\mathrm{Id},\ L_1\in C^{d_0,(2\delta,\delta,\delta)}_{e3b}
\mathcal P_m\otimes\mathrm{Id},\ L_2\in C^{d_0}_{e3b}\mathcal P_{m-1}\otimes\mathrm{End}\,\mathbb C^{N'},$$
with the scalar principal symbol $\ell$ of $L$ real. Let $\rho_\infty\in S^{-1}_{\mathrm{hom}}$ be a fixed positive
elliptic symbol and $\mathsf H := \rho_\infty^{m-1}H_\ell$. Let $B,E,G\in C^\infty_b\Psi^0_{e3b}$ be carried by $\chi$,
with $\mathrm{supp}\,\chi$ disjoint from $I^0\cup K^-$, as on a neighbourhood of $\bar\Omega$, which meets
$\partial\tilde M$ only in $\mathscr I^+$, $\iota^+$ and $K^+$ (section 1). Over $\tilde M\setminus(I^0\cup K^-)$,
$\mathsf H$ is a continuous vector field on ${}^{e3b}S^*\tilde M$, as the coefficients of $L_1$ vanish at $\mathscr I^+$,
$\iota^+$ and $K^+$ ([Hin26c] p. 71; II.A$'$ Lemma 5.1). Suppose that $\mathrm{WF}'(B)\subset\mathrm{Ell}(G)$, that the
backward integral curves of $\mathsf H$ from $\mathrm{WF}'(B)\cap\mathrm{Char}(L)$ reach $\mathrm{Ell}(E)$ in uniformly
finite time while remaining in $\mathrm{Ell}(G)$, and that $\mathsf H\mathsf s\le0$ on a neighbourhood in
${}^{e3b}S^*\tilde M$ of the union $T$ of these backward segments, up to their first entry into $\mathrm{Ell}(E)$. If
$\chi u\in H^{-N}$, $GLu\in H^{\mathsf s-m+1}$ and $Eu\in H^{\mathsf s}$, then $Bu\in H^{\mathsf s}$ and
$$\|Bu\|_{H^{\mathsf s}_{e3b}}\le C\big(\|GLu\|_{H^{\mathsf s-m+1}_{e3b}}+\|Eu\|_{H^{\mathsf s}_{e3b}}+\|\chi u\|_{H^{-N}
_{e3b}}\big),$$
with $C$ locally uniform for perturbations of $L_0,L_1,L_2$ in $\mathrm{Diff}^m_{e3b}$, $C^{d_0,(2\delta,\delta,\delta)}
_{e3b}\mathcal P_m$ and $C^{d_0}_{e3b}\mathcal P_{m-1}$ with real principal symbols, for which $\mathsf H'\mathsf s\le0$
on the same neighbourhood of $T$; the other hypotheses persist under small perturbations, by the continuity of the flow
in the field (II.A$'$ Lemma 5.1 (c)). The source asks $\mathsf H\mathsf s\le0$ only near
$\mathrm{WF}'(B)\cap\mathrm{Char}(L)$ within $\mathrm{Char}(L)$, which does not suffice (section 10, (G6)).

### 9.2 Estimates with b-regularity

**Proposition 9.1 ([Hin26c] Proposition 3.23).** There is $d_0 = d_0(m,\mathsf s,N)$ such that the following holds for
all $k\in\mathbb N_0$ and $L\in C^{(d_0;k)}_{e3b;b}\mathcal P$, $\mathcal P\subset C^\infty_b\Psi^m_{e3b}$ finite. Let
$B,G$ be carried by $\chi$, with $\mathrm{WF}'(B)\subset\mathrm{Ell}(G)\cap\mathrm{Ell}(L)$. If $\chi u\in H^{(-N;k)}$
and $GLu\in H^{(\mathsf s-m;k)}$, then $Bu\in H^{(\mathsf s;k)}$ and
$$\|Bu\|_{H^{(\mathsf s;k)}_{e3b;b}}\le C\big(\|GLu\|_{H^{(\mathsf s-m;k)}_{e3b;b}}+\|\chi u\|_{H^{(-N;k)}_{e3b;b}}
\big).\tag{9.1}$$
The constant is locally uniform for $L$ in $C^{(d_0;k)}_{e3b;b}\mathcal P$: it depends on $L$ through a bound for
$\|\mathbf a\|_{(d_0;k)}$ for some representation, and through (L3).

*Proof.* Let $d_0$ be the largest of the numbers of (L3) and of Lemma 8.6 for the orders $(\mathsf s,m,N)$ and
$(-N,m,N)$. Induction on $k$; $k = 0$ is (L3). Let $k\ge1$ and assume (9.1) at $k-1$ for all admissible $B$, $G$,
$\chi$. Choose $B_1$, $G_1,G_2,G_3$, carried by $\chi_1$ with $\chi = 1$ near the required neighbourhood of
$\mathrm{supp}\, \chi_1$. They satisfy $\mathrm{WF}'(B)\subset\mathrm{Ell}(G_1)$,
$\mathrm{WF}'(G_1)\subset\mathrm{Ell}(G_2)$, $\mathrm{WF}'(G_2)\subset\mathrm{Ell}(G_3)$ and
$\mathrm{WF}'(G_3)\subset\mathrm{Ell}(G)\cap\mathrm{Ell}(L)$. By (8.1), $\|Bu\|_{(\mathsf s;k)}\le\|Bu\|_{(\mathsf
s;k-1)}+\sum_j\|V_jBu\|_{(\mathsf s;k-1)}$. The first term is bounded by (9.1) at $k-1$. Write $V_jBu = BV_ju+[V_j,B]u$.
Here $[V_j,B]$ is carried by $\chi_1$ with wave front set in that of $B$ (Lemma 8.4 (a)), so $\|[V_j,B]u\|_{(\mathsf
s;k-1)}$ is bounded by (9.1) at $k-1$. For $BV_ju$, apply (9.1) at $k-1$ to $V_ju$, with $G_1$ in place of $G$:
$$\|BV_ju\|_{(\mathsf s;k-1)}\le C\big(\|G_1LV_ju\|_{(\mathsf s-m;k-1)}+\|\chi_1V_ju\|_{(-N;k-1)}\big).$$
The last term is at most $C\|\chi u\|_{(-N;k)}$, since $\chi_1V_ju = V_j(\chi_1u)-(V_j\chi_1)\chi u$. Write $LV_ju =
V_jLu-[V_j,L]u$. First,
$$\|G_1V_jLu\|_{(\mathsf s-m;k-1)}\le\|G_1Lu\|_{(\mathsf s-m;k)}+\|[G_1,V_j]Lu\|_{(\mathsf s-m;k-1)}\le C\big(\|GLu\|
_{(\mathsf s-m;k)}+\|\chi_*Lu\|_{(-N-m;k)}\big)$$
by Lemma 8.4 (c), since $\mathrm{WF}'(G_1)\subset\mathrm{Ell}(G)$, with $\chi_*$ carrying $G_1$ and $G$. By the support
convention and Lemma 8.6 (a) at the order $-N$, $\|\chi_*Lu\|_{(-N-m;k)}\le C\|\mathbf a\|_{(d_0;k)}\|\chi
u\|_{(-N;k)}$. Second, $[V_j,L] = \sum_q((V_ja_q)P_q+a_q[V_j,P_q])$ lies in $C^{(d_0;k-1)}_{e3b;b}\mathcal P'$,
$\mathcal P' := \mathcal P\cup\{[V_j,P_q]\}$, with a representation of norm at most $C\|\mathbf a\|_{(d_0;k)}$ (Lemma
8.2 (b)). By Lemma 8.6 (b),
$$\|G_1[V_j,L]u\|_{(\mathsf s-m;k-1)}\le C\|\mathbf a\|_{(d_0;k)}\big(\|G_2u\|_{(\mathsf s;k-1)}+\|\chi u\|_{(-N;k-1)}
\big).$$
Since $\mathrm{WF}'(G_2)\subset\mathrm{Ell}(G_3)\cap\mathrm{Ell}(L)$, (9.1) at $k-1$ bounds $\|G_2u\|_{(\mathsf s;k-1)}$
by $C(\|G_3Lu\|_{(\mathsf s-m;k-1)}+\|\chi u\|_{(-N;k-1)})$. Lemma 8.4 (c) bounds $\|G_3Lu\|$ by $C(\|GLu\|_{(\mathsf
s-m;k-1)}+\|\chi_*Lu\|_{(-N-m;k-1)})$, and the last term is treated as before. Each step shows that the quantity bounded
is finite when the right side of (9.1) is: the step at $k-1$ applied to $V_ju$ has finite right side. So $V_jBu\in
H^{(\mathsf s;k-1)}$ for every $j$, that is, $Bu\in H^{(\mathsf s;k)}$, with (9.1). The constants depend on $L$ through
$\|\mathbf a\|_{(d_0;k)}$, the constants at $k-1$ and those of (L3), and $d_0$ does not depend on $k$. $\square$

**Proposition 9.2 ([Hin26c] Proposition 3.24).** There is $d_0 = d_0(m,\mathsf s,N)$ such that the following holds for
all $\delta>0$, $k\in\mathbb N_0$ and operators on $\mathbb C^{N'}$ of the form
$$L = L_0+L_1+L_2,\quad L_0\in\mathrm{Diff}^m_{e3b}\otimes\mathrm{Id},\ L_1\in C^{(d_0;k),(2\delta,\delta,
\delta)}_{e3b;b}
\mathcal P_m\otimes\mathrm{Id},\ L_2\in C^{(d_0;k)}_{e3b;b}\mathcal P_{m-1}\otimes\mathrm{End}\,\mathbb C^{N'},
\tag{9.2}$$
under the hypotheses of (L4) on $\ell$, $B$, $E$, $G$ and $\mathsf s$. If $\chi u\in H^{(-N;k)}$, $GLu\in H^{(\mathsf
s-m+1;k)}$ and $Eu\in H^{(\mathsf s;k)}$, then $Bu\in H^{(\mathsf s;k)}$ and
$$\|Bu\|_{H^{(\mathsf s;k)}_{e3b;b}}\le C\big(\|GLu\|_{H^{(\mathsf s-m+1;k)}_{e3b;b}}+\|Eu\|_{H^{(\mathsf s;k)}_{e3b;b}}+
\|\chi u\|_{H^{(-N;k)}_{e3b;b}}\big),\tag{9.3}$$
with $C$ locally uniform for perturbations as in (L4), at the regularity $(d_0;k)$.

*Proof.* Let $d_0$ be the largest of the numbers of (L4), of Lemma 8.6 for the orders that occur, and 2. Induction on
$k$; $k = 0$ is (L4). Let $k\ge1$. By Lemma 4.1, $[L_0,V_j] = \sum_{l = 0}^NA^0_{j,l}V_l$ with $A^0_{j,l}\in C^\infty_b
\Psi^{m-1}_{e3b}$ fixed operators; here $[L_0,V_j]\in\mathrm{Diff}^m_{e3b}$, by (4.1). For $L_1 = \sum a_qP_q$,
$$[a_qP_q,V_j] = a_q[P_q,V_j]-(V_ja_q)P_q = \sum_l\big(a_qA'_{qjl}-(V_ja_q)A''_{ql}\big)V_l,$$
with $A'_{qjl},A''_{ql}\in C^\infty_b\Psi^{m-1}_{e3b}$ fixed (Lemma 4.1 for $[P_q,V_j]$ and for $P_q$). Likewise for
$L_2$, with operators of order $m-2$. Hence
$$[L,V_j] = \sum_{l = 0}^NA_{j,l}V_l,\qquad A_{j,l}\in C^\infty_b\Psi^{m-1}_{e3b}+C^{(d_0;k-1),(2\delta,\delta,\delta)}
_{e3b;b}\Psi^{m-1}_{e3b}+C^{(d_0;k-1)}_{e3b;b}\Psi^{m-2}_{e3b},$$
each in the span of a fixed finite set, with coefficient norms at most $C$ times those of $L$ at $(d_0;k)$. Put $u^{(1)}
:= (V_ju)_{j = 0}^N$ and $f := Lu$. Then $LV_ju-\sum_lA_{j,l}V_lu = V_jf$, that is,
$$L^{(1)}u^{(1)} = f^{(1)} := (V_jf)_{j = 0}^N,\qquad L^{(1)} := (L\delta_{jl}-A_{j,l})_{j,l = 0,\dots,N}.$$
$L^{(1)}$ acts on $\mathbb C^{N'(N+1)}$, and is of the form (9.2) at the regularity $(d_0;k-1)$. Its parts are
$L_0\otimes \mathrm{Id}$ and $L_1\otimes\mathrm{Id}$, and a part of order $m-1$ that collects $L_2\otimes\mathrm{Id}$
and the $A_{j,l}$; the weighted coefficients lie in the unweighted class by Lemma 8.2 (d). Its principal symbol is
$\ell\,\mathrm{Id}$, so the hypotheses on $\ell$, $\mathsf H$ and $\mathsf s$ are those for $L$. Choose $B_1$ slightly
larger than $B$, with $\mathrm{WF}'(B)\subset\mathrm{Ell}(B_1)$, and $E_1$, $G_1$ slightly smaller than $E$, $G$, with
$\mathrm{WF}'(E_1) \subset\mathrm{Ell}(E)$ and $\mathrm{WF}'(G_1)\subset\mathrm{Ell}(G)$, such that the hypotheses hold
for $(B_1,E_1,G_1)$ (section 9, beginning). The inductive hypothesis, (9.3) at $k-1$ for $L^{(1)}$, gives
$$\|B_1u^{(1)}\|_{(\mathsf s;k-1)}\le C\big(\|G_1f^{(1)}\|_{(\mathsf s-m+1;k-1)}+\|E_1u^{(1)}\|_{(\mathsf s;k-1)}
+\|\chi_1u
^{(1)}\|_{(-N;k-1)}\big).$$
Here $\|G_1V_jf\|_{(\mathsf s-m+1;k-1)}\le\|G_1f\|_{(\mathsf s-m+1;k)}+\|[G_1,V_j]f\|_{(\mathsf s-m+1;k-1)}$. Both terms
are bounded by $C(\|GLu\|_{(\mathsf s-m+1;k)}+\|\chi u\|_{(-N;k)})$, by Lemma 8.4 (c) and Lemma 8.6 (a) for the error
term, as in Proposition 9.1. Similarly $\|E_1V_ju\|_{(\mathsf s;k-1)}\le C(\|Eu\|_{(\mathsf s;k)}+\|\chi u\|_{(-N;k)})$
and $\|\chi_1u^{(1)}\|_{(-N;k-1)}\le C\|\chi u\|_{(-N;k)}$. On the left, $\|Bu\|_{(\mathsf s;k)}\le
C\sum_j(\|BV_ju\|_{(\mathsf s;k-1)}+\|[V_j,B]u\|_{(\mathsf s;k-1)})$, and both are bounded by
$C(\|B_1u^{(1)}\|_{(\mathsf s;k-1)}+\|\chi u\|_{(-N;k)})$. For the first, Lemma 8.4 (c) applies with
$\mathrm{WF}'(B)\subset\mathrm{Ell}(B_1)$. For the second, the wave front set lies in that of $B$, and the $j = 0$
component of $u^{(1)}$ is $u$. The finiteness statements follow as in Proposition 9.1. $\square$

### 9.3 Tame estimates

**Lemma 9.3 ([Hin26c] Lemma 3.25).** Let $R$ be a ring, $\mathrm{ad}_A := [A,\cdot]$, and $P,X_1,\dots,X_N\in R$. Then
$$[X_1\cdots X_N,P] = \sum_{q = 1}^N\sum_{i_1<\dots<i_q}(\mathrm{ad}_{X_{i_1}}\cdots\mathrm{ad}_{X_{i_q}}P)\prod_{j\notin
\{i_1,\dots,i_q\}}X_j\tag{9.4}$$
$$\phantom{[X_1\cdots X_N,P]} = \sum_{q = 1}^N(-1)^{q-1}\sum_{i_1<\dots<i_q}\Big(\prod_{j\notin\{i_1,\dots,i_q\}}X_j\Big)
(\mathrm{ad}_{X_{i_q}}\cdots\mathrm{ad}_{X_{i_1}}P),\tag{9.5}$$
the products taken in increasing order of $j$.

*Proof.* $N = 1$ is the definition. For (9.4), assume it for $N$ and let $X_{N+1}\in R$. Then
$$[X_1\cdots X_{N+1},P] = [X_1\cdots X_N,P]X_{N+1}+(\mathrm{ad}_{X_{N+1}}P)X_1\cdots X_N+[X_1\cdots X_N,
\mathrm{ad}_{X_{N+1}}
P],$$
because $X_1\cdots X_NQ = QX_1\cdots X_N+[X_1\cdots X_N,Q]$ with $Q := \mathrm{ad}_{X_{N+1}}P$. The inductive hypothesis
applies to the first and third terms. The first gives the terms of (9.4) for $N+1$ whose index set omits $N+1$. The
second gives the set $\{N+1\}$. The third gives the sets containing $N+1$ and some $i_1<\dots<i_q\le N$, with
$\mathrm{ad}_{X_{N+1}}$ innermost, as (9.4) requires. Each subset occurs exactly once. For (9.5), assume it for the $N$
elements $X_2,\dots,X_{N+1}$. Then
$$[X_1\cdots X_{N+1},P] = X_1[X_2\cdots X_{N+1},P]+X_2\cdots X_{N+1}(\mathrm{ad}_{X_1}P)-[X_2\cdots X_{N+1},
\mathrm{ad}_{X_1}
P].$$
The first term gives the sets omitting 1, with $X_1$ first in the product. The second gives $\{1\}$. The third gives the
sets $\{1\}\cup S$, with sign $-(-1)^{|S|-1} = (-1)^{|S|}$ and with $\mathrm{ad}_{X_1}$ innermost. $\square$

**Notation 9.4 ([Hin26c] Notation 3.26).** Fix a finite set $\mathcal V^\sharp$ spanning $\mathcal V_b(\tilde M)$ over
$C^\infty(\tilde M)$, and the good spanning set $V_1,\dots,V_N$. $D^j_b$, resp. $D^j_{[b]}$, denotes the vector of all
$j$-fold compositions of elements of $\mathcal V^\sharp$, resp. of the $V_i$, and $D^{\le j}$ those of order at most
$j$. Each component of $D^j_b$ is a combination, with coefficients in $C^\infty(\tilde M)$, of components of $D^{\le
j}_{[b]}$, and conversely. The coefficients' derivatives produce terms of lower order. All the norms below are therefore
unchanged up to constants when $D_b$ is replaced by $D_{[b]}$. By Lemma 9.3, for $|J| = q$, schematically,
$$[D^q_{[b]},P] = \sum_{q' = 1}^q(\mathrm{ad}^{q'}_{D_{[b]}}P)D^{q-q'}_{[b]} = \sum_{q' 
= 1}^qD^{q-q'}_{[b]}(\mathrm{ad}^{q'}
_{D_{[b]}}P).\tag{9.6}$$

**Lemma 9.5 ([Hin26c] Lemma 3.27, with $C^3_b$ in the first term).** For $a,b\in\mathbb N_0$ there is $C_{a,b}$ with
$$\|(D^a_b\ell)(D^b_bu)\|_{L^2(\tilde M)}\le C_{a,b}\big(\|\ell\|_{C^3_b}\|u\|_{H^{a+b}_b}+\|\ell\|_{C^{a+b+3}_b}\|u\|
_{H^3_b}\big).$$

*Proof.* In each chart $\phi_\alpha$ of section 4.1, the b-vector fields are uniformly bounded combinations of the
coordinate fields of $(-2,2)^5$, and the density is a constant $c_\alpha$ times a uniformly smooth positive multiple of
$|dx|$. The coefficient Lie algebra is $C^\infty_b\mathcal V_b$ ((S1)). Hence $\|v\|^2_{L^2}$ and $\|v\|^2_{H^q_b}$ are
equivalent, uniformly, to $\sum_\alpha c_\alpha\|\chi(\phi_\alpha)_*v\|^2_{L^2(\mathbb R^5)}$ and to the same sum with
$H^q(\mathbb R^5)$-norms of $\tilde\chi(\phi_\alpha)_*v$, $\tilde\chi = 1$ on $\mathrm{supp}\,\chi$. And
$\|\tilde\chi(\phi_\alpha)_*\ell\|_{C^q}\le C\|\ell\|_{C^q_b}$ uniformly. It therefore suffices to show, for $f\in
C^{K+3}$ and $g\in H^K$ supported in $(-2,2)^5$, $K := a+b$, and $|\beta|\le a$, $|\gamma|\le b$, that
$$\|\partial^\beta f\,\partial^\gamma g\|_{L^2(\mathbb R^5)}\le C\big(\|f\|_{C^3}\|g\|_{H^K}+\|f\|_{C^{K+3}}\|g\|_{H^3}
\big),$$
and to sum over $\alpha$ (finite multiplicity). If $|\gamma|<3$, the left side is at most $\|f\|_{C^K}\|g\|_{H^2}$. If
$\beta = 0$, it is at most $\|f\|_{C^0}\|g\|_{H^K}$. Otherwise $|\beta|\ge1$, $|\gamma|\ge3$ and $K'
:= |\beta|+|\gamma|\ge 4$. Sobolev embedding on $\mathbb R^5$ ($3>\frac52$) gives $\|\partial^\beta f\|_{L^\infty}\le
C\|f\|_{H^{|\beta|+3}}$. On the Fourier side, Hölder's inequality gives $\|h\|_{H^{(1-\theta)t_0+\theta
t_1}}\le\|h\|^{1-\theta}_{H^{t_0}}\|h\|^\theta _{H^{t_1}}$. With $\theta := |\beta|/K'$ for $f$ ($t_0 = 3$, $t_1 =
K'+3$) and $\theta' := (|\gamma|-3)/(K'-3)$ for $g$ ($t_0 = 3$, $t_1 = K'$),
$$\|\partial^\beta f\,\partial^\gamma g\|_{L^2}\le C\,\|f\|^{1-\theta}_{H^3}\|f\|^\theta_{H^{K'
+3}}\|g\|^{1-\theta'}_{H^3}
\|g\|^{\theta'}_{H^{K'}}.$$
Now $\theta'\le1-\theta$, as $K'(|\gamma|-3)\le|\gamma|(K'-3)$, and $\|g\|_{H^3}\le\|g\|_{H^{K'}}$. So $\|g\|^{1-
\theta'}_{H^3}\|g\|^{\theta'}_{H^{K'}}\le\|g\|^\theta_{H^3}\|g\|^{1-\theta}_{H^{K'}}$, and the right side is at most
$C(\|f\|_{H^3}\|g\|_{H^{K'}})^{1-\theta}(\|f\|_{H^{K'+3}}\|g\|_{H^3})^\theta\le
C(\|f\|_{H^3}\|g\|_{H^{K'}}+\|f\|_{H^{K'+3}} \|g\|_{H^3})$ by Young's inequality. Finally $\|f\|_{H^q}\le C\|f\|_{C^q}$
for $f$ supported in $(-2,2)^5$, and $K'\le K$. $\square$

The source uses the Moser estimate in place of the interpolation above, with $\|\ell\|_{C^0_b}$ in the first term. The
three derivatives lost here are absorbed in the thresholds of Proposition 9.6.

**Proposition 9.6 ([Hin26c] Proposition 3.28).** Let $\mathsf s,\mathsf s_0$ be variable orders, $\bar s :=
\max(0,\lceil\sup\mathsf s\rceil)$, $\underline s := \max(0,\lceil-\inf\mathsf s\rceil)$ and $\underline s_0 :=
\max(0,\lceil-\inf\mathsf s_0\rceil)$. There are $d_0,\tilde d\in\mathbb N$ such that the following holds for all
$B,B^\sharp\in C^\infty_b\Psi^0_{e3b}$ carried by $\chi$ with $\mathrm{WF}'(B)\subset\mathrm{Ell}(B^\sharp)$. For all
$k$ there is $C_k$ such that, for all $0\le j\le k$,
$$\|B(D^j_{[b]}\ell)(D^{k-j}_{[b]}u)\|_{H^{\mathsf s}_{e3b}}\le C_k\Big(\|\ell\|_{C^{(d_0;\tilde d)}_{e3b;b}}
\big(\|B^\sharp u
\|_{H^{(\mathsf s;k)}_{e3b;b}}+\|\chi u\|_{H^{(\mathsf s_0;k)}_{e3b;b}}\big)+\|\ell\|_{C^{(d_0;k)}_{e3b;b}}
\big(\|B^\sharp u\|
_{H^{(\mathsf s;\tilde d)}_{e3b;b}}+\|\chi u\|_{H^{(\mathsf s_0;\tilde d)}_{e3b;b}}\big)\Big).\tag{9.7}$$
One can take $d_1 := \bar s+\max(\underline s,\underline s_0)+3$, $\tilde d := d_1+\max(\underline s,\underline s_0)+3$,
and $d_0$ the number of Lemma 8.5 for $(\mathsf s,\mathsf s_0)$.

*Proof.* Choose $B_1$, $B_2$ carried by $\chi$ with $\mathrm{WF}'(I-B_1)\cap\mathrm{WF}'(B) = \emptyset$,
$\mathrm{WF}'(B_1)\subset\mathrm{Ell}(B_2)$ and $\mathrm{WF}'(B_2)\subset\mathrm{Ell}(B^\sharp)$. By Lemma 8.4 (c),
$\|B_iv\|_{(\mathsf s;q)}\le C(\|B^\sharp v\|_{(\mathsf s;q)}+\|\chi v\|_{(\mathsf s_0;q)})$, taking $N\ge-\inf\mathsf
s_0$ there. It therefore suffices to prove (9.7) with $B_2$ in place of $B^\sharp$. By the support convention, $u$ may
be replaced by $\chi u$.

*$k = 0$.* $B\ell u = B\ell B_1u+B\ell(I-B_1)u$. Lemma 8.5 (a) and the boundedness of $B$ bound the first term by
$C\|\ell\|_{C^{d_0}_{e3b}}\|B_1u\|_{H^{\mathsf s}}$, and Lemma 8.5 (b) bounds the second by $C\|\ell\|_{C^{d_0}_{e3b}}\|
\chi u\|_{H^{\mathsf s_0}}$. Finally $\|B_1u\|_{H^{\mathsf s}}\le C(\|B_2u\|_{H^{\mathsf s}}+\|\chi u\|_{H^{\mathsf
s_0}})$.

*$k\le\tilde d$.* Apply the case $k = 0$ to $D^j\ell$ and $D^{k-j}u$. By Lemma 8.2 (b), $\|D^j\ell\|_{C^{d_0}_{e3b}}\le
C\|\ell\|_{C^{(d_0;j)}}\le C\|\ell\|_{C^{(d_0;\tilde d)}}$. By (9.6), $B_1D^{k-j} =
\sum_{q}D^{k-j-q}(\mathrm{ad}^q_{D_{[b]}} B_1)$, where $\mathrm{ad}^qB_1\in C^\infty_b\Psi^0_{e3b}$ has wave front set
in $\mathrm{WF}'(B_1)\subset\mathrm{Ell} (B_2)$ (Lemma 8.4 (a)). So, by Lemma 8.4 (c),
$$\|B_1D^{k-j}u\|_{H^{\mathsf s}}\le C\big(\|B_2u\|_{(\mathsf s;k-j)}+\|\chi u\|_{(\mathsf s_0;k-j)}\big).\tag{9.8}$$
Also $\|\chi D^{k-j}u\|_{H^{\mathsf s_0}}\le C\|\chi u\|_{(\mathsf s_0;k-j)}$, as in Proposition 9.1. This is (9.7).

*$k>\tilde d$.* If $j\le\tilde d$, the argument just given bounds the left side by the first line of (9.7). If $j\ge
k-\tilde d$, it bounds it by $\|D^j\ell\|_{C^{d_0}_{e3b}}\le C\|\ell\|_{C^{(d_0;k)}}$ times $\|B_2u\|_{(\mathsf s;\tilde
d)}+\|\chi u\|_{(\mathsf s_0;\tilde d)}$, the second line. Let $\tilde d<j<k-\tilde d$. By Lemma 8.4 (d),
$\|v\|_{H^{\mathsf s}_{e3b}}\le\|v\|_{H^{\bar s}_{e3b}}\le C\|v\|_{H^{\bar s}_b}\le C\sum_{l\le\bar
s}\|D^l_{[b]}v\|_{L^2}$. By (9.6), $D^l_{[b]}B = \sum_{l'\le l}(\mathrm{ad}^{l-l'}_{D_{[b]}}B)D^{l'}_{[b]}$, with
$\mathrm{ad}^{l-l'}B$ bounded on $L^2$. By the Leibniz rule, $D^{l'}((D^j\ell)(D^{k-j}u))$ is a sum of terms
$(D^{j+l_1}\ell)(D^{k-j+l_2}u)$, $l_1+l_2 = l'$. So it suffices to bound, for $l_1+l_2\le\bar s$ and
$v\in\{B_1u,(I-B_1)u\}$,
$$\|(D^{j+l_1}\ell)(D^{k-j+l_2}v)\|_{L^2}.\tag{9.9}$$
Apply Lemma 9.5 to $D^{d_1}\ell$ and $D^{d_1}v$, with $a := j+l_1-d_1$ and $b := k-j+l_2-d_1$. Both are positive, since
$j>\tilde d\ge d_1$ and $k-j>\tilde d$. Then $a+b+d_1 = k+l_1+l_2-d_1\le k+\bar s-d_1$, and (9.9) is at most
$$C\big(\|\ell\|_{C^{d_1+3}_b}\|v\|_{H^{k+\bar s-d_1}_b}+\|\ell\|_{C^{k+\bar s-d_1+3}_b}\|v\|_{H^{d_1+3}_b}\big).$$
Here $\|\ell\|_{C^{d_1+3}_b}\le\|\ell\|_{C^{(d_0;\tilde d)}}$, as $d_1+3\le\tilde d$, and $\|\ell\|_{C^{k+\bar
s-d_1+3}_b} \le\|\ell\|_{C^{(d_0;k)}}$, as $d_1\ge\bar s+3$. For $v = B_1u$, Lemma 8.7 and Lemma 8.4 (c) give
$\|B_1u\|_{H^{k+\bar s-d_1}_b}\le C\|B_1u\|_{(\mathsf s;k+\bar s-d_1+\underline s)}\le C(\|B_2u\|_{(\mathsf s;k)}+\|\chi
u\|_{(\mathsf s_0;k)})$, as $d_1\ge\bar s+\underline s$. Likewise $\|B_1u\|_{H^{d_1+3}_b}\le C(\|B_2u\|_{(\mathsf
s;\tilde d)}+\|\chi u\|_{(\mathsf s_0;\tilde d)})$, as $d_1+3+\underline s\le\tilde d$. For $v = (I-B_1)u$, the same
with $\mathsf s_0$ for $\mathsf s$ and $\underline s_0$ for $\underline s$ gives $\|\chi u\|_{(\mathsf s_0;k)}$ and
$\|\chi u\|_{(\mathsf s_0;\tilde d)}$, as $I-B_1$ is bounded on the mixed spaces. The products are those of (9.7).
$\square$

**Corollary 9.7 (tame bound for operators of limited regularity).** Let $\mathcal P\subset C^\infty_b\Psi^m_{e3b}$ be
finite, $A\in C^{(d_0;k)}_{e3b;b}\mathcal P$ with a representation $\mathbf a$, and $\chi'$, $\chi$ cut-offs with
$\chi'$ carried by $\chi$. With $d_0$, $\tilde d$ of Proposition 9.6 for $\mathsf s = \mathsf s_0 = \mathsf t-m$,
$$\|\chi'Au\|_{(\mathsf t-m;k)}\le C_k\big(\|\mathbf a\|_{(d_0;\tilde d)}\|\chi u\|_{(\mathsf t;k)}
+\|\mathbf a\|_{(d_0;k)}
\|\chi u\|_{(\mathsf t;\tilde d)}\big).$$

*Proof.* By (8.1) and the Leibniz rule, $V^J(a_qP_qu)$ is a sum of products $(V^{J_1}a_q)(V^{J_2}P_qu)$. Apply (9.7)
with $B := \chi'$ and $B^\sharp := \chi''$, multiplication operators with $\chi'' = 1$ near $\mathrm{supp}\,\chi'$ and
$\chi''$ carried by $\chi$, to $\ell := a_q$ and to $P_qu$ in place of $u$. Then $\|\chi''P_qu\|_{(\mathsf t-m;q')}\le
C\|\chi u\|_{(\mathsf t;q')}$, by the support convention and Lemma 8.4 (a). $\square$

**Proposition 9.8 ([Hin26c] Proposition 3.29).** Let $\mathcal P\subset C^\infty_b\Psi^m_{e3b}$ be finite. There are
$d_0,d\in\mathbb N$ such that the following holds for all $k$ and $L\in C^{(d_0;d)}_{e3b;b}\mathcal P$ with a
representation $\mathbf L$. Let $B,G$ be carried by $\chi$ with
$\mathrm{WF}'(B)\subset\mathrm{Ell}(G)\cap\mathrm{Ell}(L)$. If $\mathbf L$ is a representation at $(d_0;k)$, then
$$\|Bu\|_{(\mathsf s;k)}\le C_k\Big(\|GLu\|_{(\mathsf s-m;k)}+\|\chi u\|_{(-N;k)}+\|\mathbf L\|_{(d_0;k)}\big(\|GLu\|
_{(\mathsf s-m;d)}+\|\chi u\|_{(-N;d)}\big)\Big),\tag{9.10}$$
with the finiteness statement of Proposition 9.1. $C_k$ depends on $L$ only through a bound for $\|\mathbf L\|_{(d_0;d)}$
and the ellipticity margin of (L3), and so is locally uniform in $C^{(d_0;d)}_{e3b;b}\mathcal P$ for all $k$ at once.

*Proof.* Take $d := \tilde d+1$, with $d_0$ and $\tilde d$ those of Proposition 9.6 for $(\mathsf s-m,-N-m)$, enlarged
to serve also Proposition 9.1 and Corollary 9.7. For $k\le d$, (9.10) is Proposition 9.1, whose constant depends on
$\|\mathbf L\|_{(d_0;k)}\le\|\mathbf L\|_{(d_0;d)}$. Let $k>d$ and assume (9.10) at all orders below $k$, for all
admissible $B$, $G$. Choose $G_1,G_2,G_3$ as in Proposition 9.1, with
$\mathrm{WF}'(G_3)\subset\mathrm{Ell}(G)\cap\mathrm {Ell}(L)$. For a word $J$ of length $k$, (9.4) gives
$$LV^Ju = V^JLu-\sum_{\emptyset\ne S\subset J}(\mathrm{ad}_{V_S}L)V^{J\setminus S}u,\tag{9.11}$$
with $\mathrm{ad}_{V_S}$ the iterated commutator in the order of $S$ and $J\setminus S$ in its order. (L3), applied to
$V^Ju$ with $G_1$, has a constant depending only on $\|\mathbf L\|_{(d_0;0)}$:
$$\|BV^Ju\|_{H^{\mathsf s}}\le C\big(\|G_1V^JLu\|_{H^{\mathsf s-m}}
+\sum_S\|G_1(\mathrm{ad}_{V_S}L)V^{J\setminus S}u\|_{H^{\mathsf
s-m}}+\|\chi_1V^Ju\|_{H^{-N}}\big).$$
*The left side.* $\|Bu\|_{(\mathsf s;k)}$ is at most the sum of $\|Bu\|_{(\mathsf s;k-1)}$ and the
$\|V^JBu\|_{H^{\mathsf s}}$, $|J| = k$. By (9.4), $V^JB = BV^J+\sum_S(\mathrm{ad}_{V_S}B)V^{J\setminus S}$. The
operators $\mathrm{ad}_{V_S}B$ are carried by $\chi$ with wave front set in that of $B$, and each term with
$S\ne\emptyset$ has at most $k-1$ factors $V$. Moving them to the left by (9.5) bounds these terms by finitely many
$\|B'u\|_{(\mathsf s;k-1)}$, with $\mathrm{WF}' (B')\subset\mathrm{WF}'(B)$. These, and $\|Bu\|_{(\mathsf s;k-1)}$, are
bounded by (9.10) at $k-1$, which is at most the right side of (9.10) at $k$.

*The first two terms on the right.* $\|\chi_1V^Ju\|_{H^{-N}}\le C\|\chi u\|_{(-N;k)}$. By (9.6),
$\|G_1V^JLu\|_{H^{\mathsf s-m}}\le\|G_1Lu\|_{(\mathsf s-m;k)}+\sum\|G'Lu\|_{(\mathsf s-m;k-1)}$, with
$\mathrm{WF}'(G')\subset\mathrm{WF}'(G_1)$. By Lemma 8.4 (c) both are at most $C(\|GLu\|_{(\mathsf
s-m;k)}+\|\chi_*Lu\|_{(-N-m;k)})$. Corollary 9.7 bounds the error term tamely by $C_k(\|\mathbf L\|_{(d_0;\tilde
d)}\|\chi u\|_{(-N;k)}+\|\mathbf L\|_{(d_0;k)}\|\chi u\|_{(-N;\tilde d)})$.

*The commutator terms.* Let $|S| = j\ge1$. With $L = \sum_q\ell_qA_q$, iterating $\mathrm{ad}_V(\ell A) =
(V\ell)A+\ell\, \mathrm{ad}_VA$ gives $\mathrm{ad}_{V_S}L = \sum_q\sum_{S'\subset
S}(V_{S'}\ell_q)(\mathrm{ad}_{V_{S\setminus S'}}A_q)$. Here $\mathrm{ad}_{V_{S\setminus S'}}A_q\in
C^\infty_b\Psi^m_{e3b}$ is fixed, by (S10). By (9.5), $(\mathrm{ad}A_q) V^{J\setminus S} = \sum V^{J'}A'$ with $|J'|\le
k-j$ and $A'\in C^\infty_b\Psi^m_{e3b}$ fixed. So the terms to bound are $\|G_1(V_{S'}\ell_q)V^{J'}(A'u)\|_{H^{\mathsf
s-m}}$, with $j' := |S'|\le j$ and $|J'|\le k-j\le k-1$. If $j'\ge1$, write $V_{S'}\ell_q = V_{S'_2}(V_{s_1}\ell_q)$,
with $s_1$ the first letter of $S'$, and apply (9.7) with $\mathsf s-m$ for $\mathsf s$ and $-N-m$ for $\mathsf s_0$.
Use $(B,B^\sharp) = (G_1,G_2)$, $\ell := V_{s_1}\ell_q$, $A'u$ for $u$, and $(j'-1,j'-1+|J'|)$ for $(j,k)$. Note
$j'-1+|J'|\le k-1$. The bound is
$$C_k\Big(\|V_{s_1}\ell_q\|_{(d_0;\tilde d)}\big(\|G_2A'u\|_{(\mathsf s-m;k-1)}+\|\chi A'u\|_{(-N-m;k-1)}\big)
+\|V_{s_1}\ell_q
\|_{(d_0;k-1)}\big(\|G_2A'u\|_{(\mathsf s-m;\tilde d)}+\|\chi A'u\|_{(-N-m;\tilde d)}\big)\Big).$$
Now $\|V_{s_1}\ell_q\|_{(d_0;\tilde d)}\le C\|\mathbf L\|_{(d_0;d)}$ and $\|V_{s_1}\ell_q\|_{(d_0;k-1)}\le C\|\mathbf
L\| _{(d_0;k)}$ (Lemma 8.2 (b); this is why $d = \tilde d+1$). Next, $\|\chi A'u\|_{(-N-m;q)}\le C\|\chi u\|_{(-N;q)}$,
and $\|G_2A'u\|_{(\mathsf s-m;q)}\le C(\|G_3u\|_{(\mathsf s;q)}+\|\chi u\|_{(-N;q)})$ by Lemma 8.4 (c). By (9.10) at the
order $k-1$, with $G_3$ in place of $B$, $\|G_3u\|_{(\mathsf s;k-1)}$ is bounded by the right side of (9.10) at $k$. Its
constant depends only on $\|\mathbf L\|_{(d_0;d)}$, and its high norm $\|\mathbf L\|_{(d_0;k-1)}$ multiplies low norms
only. By Proposition 9.1 at the order $\tilde d<d$, $\|G_3u\|_{(\mathsf s;\tilde d)}\le C(\|GLu\|_{(\mathsf
s-m;d)}+\|\chi u\| _{(-N;d)})$. If $j' = 0$, the coefficient is $\ell_q$ itself and $|J'|\le k-1$, and (9.7) with $\ell
:= \ell_q$ and $(0,|J'|)$ gives the same bounds, with $\|\ell_q\|_{(d_0;\tilde d)}$ and $\|\ell_q\|_{(d_0;k-1)}$.
Collecting the terms gives (9.10). The source treats only the term with the most derivatives on the coefficient. The
others are bounded in the same way. $\square$

**Proposition 9.9 ([Hin26c] Proposition 3.30, with $\mathsf s-m+1$).** There are $d_0,d\in\mathbb N$ such that the
following holds for all $\delta>0$, all $k$, finite sets $\mathcal P_{m-j}$, $j = 0,1$, and $L = L_0+L_1+L_2$. Here
$L_0\in\mathrm{Diff}^m_{e3b}$, $L_1\in C^{(d_0;d),(2\delta,\delta,\delta)}_{e3b;b}\mathcal P_m$, $L_2\in
C^{(d_0;d)}_{e3b;b} \mathcal P_{m-1}$, with representations $\mathbf L_1$, $\mathbf L_2$, under the hypotheses of (L4).
If the representations are at $(d_0;k)$, then
$$\|Bu\|_{(\mathsf s;k)}\le C_k\Big(\|GLu\|_{(\mathsf s-m+1;k)}+\|Eu\|_{(\mathsf s;k)}+\|\chi u\|_{(-N;k)}+\|\mathbf L\|
_{(d_0;k)}\big(\|GLu\|_{(\mathsf s-m+1;d)}+\|Eu\|_{(\mathsf s;d)}+\|\chi u\|_{(-N;d)}\big)\Big),\tag{9.12}$$
with $\|\mathbf L\| := \|\mathbf L_1\|+\|\mathbf L_2\|$. $C_k$ depends on $L$ only through bounds at $(d_0;d)$, and is
locally uniform for perturbations of $L_0,L_1,L_2$ in $\mathrm{Diff}^m_{e3b}$,
$C^{(d_0;d),(2\delta,\delta,\delta)}_{e3b;b} \mathcal P_m$, $C^{(d_0;d)}_{e3b;b}\mathcal P_{m-1}$. The source prints
$\mathsf s-m$ for $\mathsf s-m+1$ in both places (section 10, (G4)).

*Proof.* Take $d := \tilde d+2$, with $d_0$, $\tilde d$ of Proposition 9.6 for $(\mathsf s-m+1,-N-m)$, enlarged to serve
Proposition 9.2 and Corollary 9.7. For $k\le d$, (9.12) is Proposition 9.2. Let $k>d$ and assume (9.12) below $k$. Let
$\mathcal W_k$ be the set of words of length $k$ in the letters $0,\dots,N$, with $V_0 = I$. Put $u^{(k)} := (V^\alpha
u)_{\alpha\in\mathcal W_k}$. By (9.4), $LV^\alpha u = V^\alpha
Lu-\sum_{S\ne\emptyset}(\mathrm{ad}_{V_S}L)V^{\alpha\setminus S}u$. For $|S| = 1$, $S = \{i\}$, Lemma 4.1 and the
computation in the proof of Proposition 9.2 give $\mathrm{ad}_{V_{\alpha_i}} L = \sum_\nu L_{\alpha_i,\nu}V_\nu$. Here
$L_{\alpha_i,\nu}\in C^\infty_b\Psi^{m-1}_{e3b}+C^{(d_0;d-1),(2\delta,\delta,\delta)}
_{e3b;b}\Psi^{m-1}_{e3b}+C^{(d_0;d-1)}_{e3b;b}\Psi^{m-2}_{e3b}$, in the span of a fixed finite set. Its coefficients
carry at most one b-derivative of those of $L$, so their $C^{d_0}_{e3b}$-norms are bounded by $C\|\mathbf
L\|_{(d_0;1)}$. And $V_\nu V^{\alpha\setminus\{i\}}$ is again a word of length $k$. Hence
$$L^{(k)}u^{(k)} = f^{(k)}+\tilde f^{(k)},\qquad f^{(k)} := (V^\alpha Lu)_\alpha,\qquad\tilde f^{(k)} := \Big(-\sum_{|S|
\ge2}
(\mathrm{ad}_{V_S}L)V^{\alpha\setminus S}u\Big)_\alpha,$$
where $(L^{(k)}w)_\alpha := Lw_\alpha+\sum_i\sum_\nu L_{\alpha_i,\nu}w_{\nu\cdot(\alpha\setminus\{i\})}$. $L^{(k)}$ is a
system of the form of (L4), built from commutators of the fixed operators with the $V_j$. Its principal symbol is
$\ell\,\mathrm{Id}$ and its coefficients have $C^{d_0}$-norms bounded by $C\|\mathbf L\|_{(d_0;1)}$. Apply (L4) to it,
with operators chosen as follows. Let $T$ be as in section 9 (beginning), and $U\subset\mathrm{Ell}(G)$ a neighbourhood
of $T$ on which $\mathsf H\mathsf s\le0$. Apply (O) to $U$, giving $U_T$, $K_E$, $K_U$, and again to $U_T\cap U$ in place
of $U$, giving $U'_T\subset U_T$, $K'_E$ and $K'_U\subset U_T$. Take $B_1$ with $\mathrm{WF}'(B)\subset\mathrm{Ell}(B_1)$
and $\mathrm{WF}'(B_1)\subset U'_T$, $E_1$ elliptic on $K'_E$ with $\mathrm{WF}'(E_1)\subset\mathrm{Ell}(E)$, and
$G_1,G_2,G_3$ microsupported in $U_T$, with $G_1$ elliptic on $K'_U\cup\mathrm{WF}'(B_1)$,
$\mathrm{WF}'(G_1)\subset\mathrm{Ell}(G_2)$ and $\mathrm{WF}'(G_2)\subset\mathrm{Ell}(G_3)$. By (O) the hypotheses of
(L4) hold for $(B_1,E_1,G_1)$, and for $(G_2,E,G)$ and $(G_3,E,G)$. (The source shrinks $G$ in the same way. Taking $G_1$
slightly smaller than $G$ would not do: then $\mathrm{WF}'(G_3)$ contains $T$ and may reach where the hypotheses fail;
D194.) The constant depends on $k$ through the size of the system, and on $L$ only through low norms:
$$\|B_1u^{(k)}\|_{H^{\mathsf s}}\le C_k\big(\|G_1f^{(k)}\|_{H^{\mathsf s-m+1}}+\|G_1\tilde f^{(k)}\|_{H^{\mathsf s-m+1}}
+\|
E_1u^{(k)}\|_{H^{\mathsf s}}+\|\chi_1u^{(k)}\|_{H^{-N}}\big).$$
The left side controls $\|Bu\|_{(\mathsf s;k)}$ up to terms $\|B'u\|_{(\mathsf s;k-1)}$,
$\mathrm{WF}'(B')\subset\mathrm{WF}' (B)$, which are bounded by (9.12) at $k-1$ (as in Proposition 9.8). The terms with
$f^{(k)}$, $E_1$ and $\chi_1$ are bounded as in Proposition 9.8, the error term of $G_1f^{(k)}$ by Corollary 9.7. It
remains to bound $G_1\tilde f^{(k)}$. Its terms are $G_1(\mathrm{ad}_{V_S}L)V^{\alpha\setminus S}u$ with $|S| = j\ge2$,
so at most $k-2$ factors $V$ act on $u$.

For $L_0$, $\mathrm{ad}_{V_S}L_0\in\mathrm{Diff}^m_{e3b}$ is fixed, and by Lemma 8.4 (c) and (d),
$$\|G_1(\mathrm{ad}_{V_S}L_0)V^{\alpha\setminus S}u\|_{H^{\mathsf s-m+1}}\le C\big(\|G_2u\|_{(\mathsf s+1;k-2)}
+\|\chi u\|
_{(-N;k)}\big)\le C\big(\|G_2u\|_{(\mathsf s;k-1)}+\|\chi u\|_{(-N;k)}\big).\tag{9.13}$$
The second inequality is [Hin26c] (3.87), here Lemma 8.4 (d). For $L_1$ and $L_2$, $\mathrm{ad}_{V_S}(\ell A) = \sum_{S'
\subset S}(V_{S'}\ell)(\mathrm{ad}_{V_{S\setminus S'}}A)$ with $A$ of order $m$ or $m-1$. Commute the fixed operator
through the $V$'s by (9.5). If $j' := |S'|\ge2$, apply (9.7) at the order $\mathsf s-m+1$, with $\ell$ replaced by
$V_{s_1}V_{s_2}\ell$ (two letters of $S'$ removed) and $(j'-2,\cdot)$ for $(j,\cdot)$. The coefficient norms are
$\|\ell\|_{(d_0;\tilde d+2)} \le C\|\mathbf L\|_{(d_0;d)}$ and $\|\ell\|_{(d_0;k)}$. The $u$-norms are
$\|G_2A'u\|_{(\mathsf s-m+1;k-2)}\le C(\|G_3u\| _{(\mathsf s+1;k-2)}+\ldots)\le C(\|G_3u\|_{(\mathsf s;k-1)}+\ldots)$
(Lemma 8.4 (c), (d)), and the same at $\tilde d$. If $j'\le1$, the coefficient carries at most one derivative, and (9.7)
with $\ell$ replaced by $V_{S'}\ell$ and $(0,\cdot)$ gives the same bounds, with $\|V_{S'}\ell\|_{(d_0;\tilde d)}\le
C\|\mathbf L\|_{(d_0;d)}$. Here $\|G_3u\|_{(\mathsf s;k-1)}$, and $\|G_2u\|_{(\mathsf s;k-1)}$ in (9.13), are bounded by
(9.12) at $k-1$ with $G_3$, resp. $G_2$, in place of $B$, for which the hypotheses hold by the choice above. And
$\|G_3u\|_{(\mathsf s;\tilde d+1)}$ is bounded by Proposition 9.2 at the order $\tilde d+1<d$, with constant depending on
$\|\mathbf L\|_{(d_0;d)}$. This gives (9.12). The local uniformity follows from that of (L4) and Proposition 9.2.
$\square$

## 10. What the write-out found

The write-out of sections 2-3 of [Hin26c] at $n = 4$ changes the following, and nothing else besides the silent repairs
listed at the end of this section. The changes forced by the dimension are $\mathbb S^3$ for $\mathbb S^2$ throughout and
three sets of numbers. The weights become $(2(\alpha_I+2), \alpha_++\frac52,\alpha_K+\frac12)$ in place of
$(2(\alpha_I+\frac32),\alpha_++2,\alpha_K+\frac12)$, in [Hin26c] (3.57), Lemma 3.14 and Lemma 3.22 (here Lemmas 6.1, 6.2
and 8.8). The weight in (3.72) becomes $\alpha+2$ in place of $\alpha+\frac32$ (here (8.4)). The Mellin line becomes
$\mathrm{Im}\,\sigma = \alpha_++\frac52$ (Lemma 6.2). The Sobolev embeddings $H^{d+3}\subset C^d$ and $H^3\subset
L^\infty$ hold on $\mathbb R^5$ as on $\mathbb R^4$, so no regularity threshold changes.

(G1) *Lemma 2.11 of the source, weighted case.* The source prints $W^\sharp\in\mathrm{Diff}^m_{3b}$ where the weighted
statement needs $W^\sharp\in\rho_{\mathrm{sf}}^{-\alpha_{\mathrm{sf}}}\mathrm{Diff}^m_{3b}$ (Lemma 2.2). A slip of the
pen; the proof gives the weighted class.

(G2) *Lemma 3.14 of the source, the Mellin line.* With the source's transform $\int\tau^{i\sigma}u\frac{d\tau}\tau$, the
Plancherel line of $\tau^\beta L^2$ is $\mathrm{Im}\,\sigma = +\beta$. The source prints $\sigma-i(\alpha_++2)$ (Lemma
6.2), the same reversal as Part I.C (F1). The argument is unchanged.

(G3) *Tame estimates and the infimum norm.* (3.84) and (3.85) are stated with the norm (3.69), an infimum over
representations, and with constants locally uniform in the low norm. The proofs expand $L$ in one representation. The
high norm multiplying the low norms and the low norm controlling the constant must then belong to the same
representation, and with an infimum norm the near-optimal representations for the two may differ. Propositions 9.8-9.9
are stated for a given representation. This is how they are used: an operator arrives with its coefficients.
Propositions 9.1-9.2, whose constants depend on one norm only, hold for the infimum norm as well (section 8.2).

(G4) *Slips in [Hin26c] section 3.4.* (a) (3.85) prints $\mathsf s-m$ twice where the real principal type estimate gives
$\mathsf s-m+1$. The proof of Proposition 3.30 uses $\mathsf s-m+1$, and $\mathsf s-m$ would be false, as propagation
loses one derivative. (b) The proof of Proposition 3.30 says it applies Proposition 3.28 to the system $L^{(k)}$. The
estimate applied is that of Proposition 3.24 at $k = 0$; Proposition 3.28 enters afterwards, for $\tilde f^{(k)}$. (c)
In the same proof, the second line of the bound for $G(\mathrm{ad}^jL)D^{k-j}u$ carries $\|\ell\|_{C^{(d_0;k-2)}}$,
where (3.79) gives $\|D^2\ell\|_{C^{(d_0;k-2)}}\le C\|\ell\|_{C^{(d_0;k)}}$. (d) Proposition 3.28 writes
$\mathrm{Ell}_{3b}$ for $\mathrm{Ell}_{e3b}$, and the proof of Proposition 3.24 sums $A_{j,l}V_l$ over $k$ for $l$. None
changes a statement once corrected.

(G5) *The standard estimates.* The source proves its Propositions 3.23 and 3.24 for $k = 0$ by citation to the standard
arguments. They are the standing inputs (L3) and (L4) of this part (section 9.1), proved in Part II.A$'$ (written, D193):
the elliptic parametrix with coefficients of finite regularity, and the positive commutator argument with variable orders
and local uniformity, without the sharp Gårding inequality. Part II.A is labelled proved only with Part II.A$'$. Two
further inputs used by the source in the same way, the boundedness of multiplication by functions of finite regularity on
variable-order spaces and the pseudolocality of such multiplication, are proved here (Lemma 8.5), from (S5), (S6), (S8)
and the closed graph theorem.

(G6)-(G7) *The hypotheses of the real principal type estimate (D194).* Recorded in Part II.A$'$ section 6, and found
independently by the verifier of this part. The source's hypothesis $\mathsf H\mathsf s\le0$ near
$\mathrm{WF}'(B)\cap\mathrm{Char}(L)$ within $\mathrm{Char}(L)$ (p. 70) does not suffice. Take $L = D_t$ in one unit
cell, so $\mathsf H = \partial_t$, and $\mathsf s = \mathsf s(t)$ equal to $s_0$ near $\mathrm{Ell}(E)$ at $t\approx-2$
and to $s_0+10$ near $\mathrm{WF}'(B)$ at $t\approx0$, so that $\mathsf H\mathsf s = 0$ near $\mathrm{WF}'(B)$. Let $u =
\chi(t)v(x)$, with $\chi = 1$ near the segments and $v\in H^{s_0}\setminus H^{s_0+\epsilon}$ microlocally at a point of
$\{\tau = 0\}$. Every hypothesis holds and the right side is finite, but $Bu\notin H^{\mathsf s}$. (L4) asks $\mathsf
H\mathsf s\le0$ on a neighbourhood of the segments, and classical principal symbols for $\mathcal P_m$, so that $\mathsf
H$ is continuous at fibre infinity. It takes $\chi$ supported away from $I^0\cup K^-$: the source's reason for the
continuity of $\mathsf H$, that the coefficients of $L_1$ vanish at $\partial\tilde M$ (p. 71), holds at the weighted
faces $\mathscr I^+$, $\iota^+$, $K^+$ only. Propositions 9.2 and 9.9 inherit the corrected hypotheses. The proof of the
source's Proposition 3.30 shrinks $G$ to a neighbourhood of the segments before applying its Proposition 3.28 at $k-1$.
The first version of Proposition 9.9 here took $G_1$ slightly smaller than $G$ and asked $G_3$ to lie near
$\mathrm{WF}'(B)$, which is impossible, as $\mathrm{WF}'(G_3)$ contains the segments. Whether every application of these
estimates in [Hin26c] meets the corrected hypotheses is checked where the applications are written out (Parts II.B-II.F).

*Changes of method, not of statement.* Lemma 9.5 replaces the Moser estimate by Sobolev embedding and interpolation, at
the cost of three b-derivatives on the coefficient. The thresholds of Proposition 9.6 absorb them. Lemma 8.4 (b)
constructs the microlocal parametrix to finite order from the principal symbol sequence, where the source cites it. The
cut-off convention of section 8.3 makes precise the source's $B = \chi B\chi$ for operators whose kernels are not local.
The lower-order terms of Propositions 9.8-9.9, which the source passes over in favour of the top-order term, are bounded
explicitly. Lemmas 4.1 and 7.1 use parametrices to finite order, where the source uses full ones, which (S5) does not
READ. The operators are taken localized near the diagonal (section 8.3), which the source does not require (p. 48); the
class is closed under every operation used here.

*Silent repairs and copied slips (D194).* The write-out also repairs without comment: in [Hin26c] Lemma 3.14,
$|\sigma|^j$ to $|\sigma|^{2j}$ and the $k-j$ left undefined in its first integral (here Lemma 6.2); in Lemma 3.15, the
single remainder $R$, where the duality argument needs one on each side (here Lemma 7.1). Two slips of the source were
first copied and are now repaired. The angular term of (2.27) is $\frac{\slashed g}{2x_I^2}$ inside the bracket, as $r =
\rho_+^{-1}x_I^{-2}$, and the inverse metric correspondingly carries $2x_I^2\slashed g^{-1}$ (section 2.3). The proof of
Lemma 2.11 asserts $[\rho_K\mathcal V_b,w\mathrm{Diff}^m_{3b}]\subset\rho_Kw\mathrm{Diff}^m_{3b}$, which is false, as
$[r\partial_t,r\partial_r] = -\rho_Kt\partial_t$; Lemma 2.2 replaces it by an argument, and the statement stands. Two
slips of this write-out, in the coefficients of $x_Idx^0$ (Lemma 2.5) and in the transform of $\tau\partial_\tau$ (Lemma
6.2), are repaired; neither changes a conclusion.

## Sources

[Hin26c] P. Hintz, *(Non-)linear waves on asymptotically flat spacetimes. II*, arXiv:2606.28008v1. READ: pp. 31-77
(sections 2-3), printed page = PDF page $-4$; Definitions 2.1-2.3, 2.10, 2.13, 2.17, 3.4, 3.16, 3.19, 3.20; Lemmas 2.11,
2.14, 2.15, 2.18-2.20, 3.5-3.7, 3.9, 3.14, 3.15, 3.17, 3.21, 3.22, 3.25, 3.27; Corollaries 2.12, 2.16; Remark 2.4;
Notation 3.26; Propositions 3.18, 3.23, 3.24, 3.28-3.30; (2.1)-(2.13), (3.19)-(3.26), (3.46)-(3.60), (3.65),
(3.66)-(3.69), (3.72), (3.73)-(3.87).

[SBG] P. Hintz, *Pseudodifferential operators on manifolds with scaled bounded geometry*, Commun. Amer. Math. Soc. 6
(2026), 153-243, arXiv:2408.06651v1. READ: Definitions 1.1, 1.3, 3.4, 3.6-3.8, 3.14, 3.17, 3.31, 3.34, 3.43, 3.58, 3.59,
4.6, 4.11, 4.14, 4.20; Propositions 3.19, 3.22, 3.32, 3.55, 4.2, 4.15, 4.17, 4.18, 4.22; Theorems 3.21, 3.44, 3.51, 3.52;
Remarks 3.33, 3.47, 3.48; (3.26)-(3.28) and the paragraph before Definition 3.34; (4.24a-b) and the paragraph containing
them (pp. 73-74); section 3.6, its last paragraph (no propagation results).

[HJS] A. Hassell, Q. Jia, E. Sussman, *Lecture notes on non-elliptic Fredholm theory*, arXiv:2604.18956v1, as READ in
Part I.A; consulted for (L3)-(L4): Theorems 5.2, 5.3, 5.5, 10.3 and Definition 10.2 (constant differential orders; no
sharp Gårding inequality stated).

[Hin16] P. Hintz, *Global well-posedness of quasilinear wave equations on asymptotically de Sitter spaces*,
arXiv:1311.6859; consulted for (L3)-(L4): its operators with Sobolev coefficients have constant orders.
