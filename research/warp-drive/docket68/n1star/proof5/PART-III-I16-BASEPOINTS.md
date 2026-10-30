# Part III.I$'''''''''''''''$. The linear theory at base points near $b_0$, n = 4 ([Hin26] sections 11.2-12 at black
hole parameters $b\ne b_0$)

*Status.* Three major gaps and one minor one found by the base-point ledger (BASEPOINT-LEDGER.md, verifiers 145-149) and
repaired (D329-D331), to be read; verifier 150 read D329-D330 and found the expansion's repair incomplete (its M1),
repaired by the parity under $-1$ in (P3) (D331). The major gaps: III.I$''''$'s boost identity (section 2.6),
III.I$''''''''''''$'s expansion at a rotating $b$ (section 2.7), and III.I$'''''''$'s parameter identities and base
level (section 2.8). The minor gap is the reality of the objects at $b$, now in (P3). Theorem 3.1's census is now that
reading. Written (D297); verified (D299, D302: verifiers 130-131's findings seated, to be read). The parts
III.I$'$-III.I$''''''''''''''$ and III.J-III.J$'''$ prove the linear theory at base points whose black hole parameter is
$b = b_0$, with derivatives in $b$ taken at $b_0$; III.I Remark 5.4 and (I3) of III.I recorded why. III.H$''$ supplied
the two inputs that were missing for $b\ne b_0$ (its Corollary 5.1) and recorded the rest as (H$''$5). This part proves
that rest. At every base point $(h,\vec p)$, or $(h,\vec p,q)$, or $U$, whose black hole parameter is $b\in\mathcal B_*$
($\mathcal B_*$ of III.H$''$), the statements of those parts hold with constants uniform in $b$. *The statement at $b$*
of each of them is obtained as follows: $L_{b_0}$, $g_{b_0}$ near $K^+$, the states, towers and companions at $b_0$, and
the index set $\mathcal E_{\mathrm{ind}}$ are replaced by those at $b$; derivatives in $b$ are taken at $b$; and the v1
terms are treated by section 2. This closes (J$'$3) of III.J$'$, and with it (I3) and (H$''$5). Verifier 133's findings
seated (D309): the direct bound now covers every level (A-m1); A-n1 to A-n3; to be read. Proved (D311): verifier 134
read the D309 repairs, correct.

*What n = 4 changes.* At $b_0$ every rotation is Killing. At a rotating $b$ only the rotations commuting with the spin
are, and the rotation state $h_{b,\mathrm v1}$ is $O(|b-b_0|)$ but not zero (III.E$'$). The v1 terms of exponent of real
part at most 2 then decay at $K^+$ one order less than at $b_0$, below the levels' target $\alpha-2$. An elimination
through their $K^+$-coefficients would invert $V\mapsto h_{b,\mathrm v1}(V)$, a map that degenerates as $b\to b_0$. As
in the source ([Hin26] pp. 279-280, "for a suitable $V^{(1,0)\prime}\approx\dot V$"), they are assigned directly: the
coefficient of the rotation row is read from the construction that produced the term, the $\iota^+$-data of the graft or
the tf-data of the spectral pieces. No $K^+$-coefficient is inverted (Proposition 2.2). The rotation rows of
III.I$''''''''''''''$ Definition 1.3, whose coefficient space is all of $\mathcal V_1$, are what makes this possible;
III.I$''''''''''''''$ introduced them for the same reason (its "What n = 4 changes" (3)). The rest transfers by
continuity in $b$, and the joint injectivity of the states, proved at $b_0$ by spherical symmetry, by perturbation
(Lemma 1.2).

## 1. The model at $b$

**Lemma 1.1 (the model objects at $b$).** For $b\in\bar{\mathcal B}_*$, uniformly in $b$:

(P1) III.I Theorem 5.3 holds at $b$, with continuity in $(b,S,h)$ (III.H$''$ Corollary 5.1), and so do III.I
Propositions 3.3-3.4, 4.1, Corollaries 4.2, 5.2 and Lemmas 3.2 and 3.6 (verifier 145's n4), which are stated for $g_0 =
g_{b_0,b,-S}$ with $|b-b_0|$ small, and for the translated backgrounds $g_{\vec p}$ of III.I$'''''''$ Definition 1.2 at
$b$, which III.H$''$ Corollary 5.1's proof (PART-III-H3-UNIFORM.md:324-336) covers with III.I$'''''''$ Lemma 1.3 (a)
(verifier 146's n3).

(P2) $N_{\iota^+}(2L_b) = N_{\iota^+}(2\bar L)$ (III.H$''$ Lemma 3.2), so $\mathrm{spec}_{\iota^+}$, III.G$'$ Theorem
3.1 and III.G$'''$ do not depend on $b$; III.G$''$ Theorem 4.2 and Corollary 4.3 are stated for general $b$ (with the
$K^+$-towers of $L_b$); the tf-normal operator does not depend on $b$ (III.G$''''$ Lemma 1.1); and the indicial roots of
III.F$'$ Proposition 2.3 do not depend on $b$, the normal operator of $\widehat{L_b}(0)$ at $\partial X$ being that of
$2\bar L$ (III.F Lemma 2.1 (3)).

(P3) The states of III.G$''$ Table 1.1 for $L_b$, their companions, the 1-form towers of III.D$'''$, the physical states
of III.F$''''$ and $\dot g_b$ are real and smooth in $b$, with index sets in $(\mu-j)+\mathcal E_{\mathrm{ind}}$,
$\mathcal E_{\mathrm{ind}}$ independent of $b$, and, except for $\dot g_b$, with leading terms at $\partial X$ that do
not depend on $b$ (those of $\dot g_b$ may depend on $b$ through the mass, PART-III-I15-AUGMENT5.md:140-141, and the
parts use its index sets and its smoothness in $b$; verifier 147's n3, 148's n1, m3); the rotation state $h_{b,\mathrm
v1}\in\mathcal A^3$ is smooth in $b$ and vanishes at $b_0$ (III.I$''''''''''''''$ Lemma 2.1). The element $-1$ of
$SO(4)$, $x\mapsto-x$ on the spatial factor, is an isometry of every $g_b$: it is central in $SO(4)$, so it lies in the
torus of rotations commuting with the spin. It preserves $t_*$ and the gauge data, $c_C$, $c_\Upsilon$ and the cut-offs
being spherically symmetric, so it commutes with $L_b$, $\Box^\Upsilon_b$ and $\widehat{L_b}(0)$. The states are
equivariant under it: $h_b(S)$ and its companions are odd, $\dot g_b(\dot b)$, $h_{b,\mathrm v1}(V)$ and their
companions even (verifier 150's M1).

(P4) III.H Corollaries 4.2-4.4 and III.H$'$ Theorem 1.3 hold at $b$ (III.H$''$ Theorem 2.1 and its compactness
paragraph), and so do the other statements of III.H and III.H$'$ the parts use: III.H Definitions 2.1 and 3.1, Lemmas
2.3-2.5, Proposition 3.2 and Theorem 4.1, which III.H states for $b$ near $b_0$ (verifier 146's n3), and III.H$'$ Lemma
2.1, (4.1)-(5.2) and section 5. III.H$''$ Theorem 2.1 reruns III.H$'$ sections 2-7 at $b$, and its compactness paragraph
covers Proposition 3.2. The states' bounds are uniform in $\mathcal A^{q-\delta}$ for every $\delta>0$ (III.H Remark
2.6), a loss the parts absorb, each using its weights with room (verifier 145's m4). III.H$''$ Proposition 1.1 bounds
the high-frequency loss at every order $k$ at every $b\in\bar{\mathcal B}_1$, with constants independent of $b$
(PART-III-H3-UNIFORM.md:158-170; verifier 149's m1). III.G$''''$'s propositions and Lemma 4.3
(PART-III-I7-PARAMS.md:133-134; verifier 146's n3) hold at $b$, their inputs being the tf-normal operator (P2), the zero
energy states (P3) and III.H.

(P5) The time translation $\partial_{t_*}$ is Killing for $g_b$, so every statement that uses only that the s0 gauge
1-form $\omega^{(0)}_{b,\mathrm s0}$ is Killing (as III.I$'''''''''$ section 2 and III.I$''''''''''$ Lemma 2.1 do) holds
at $b$.

(P6) *Rows at $b$, corrections at $b_0$.* The rows and towers are built at the base point's $b$ (the towers $T_{\rho,b}$
of III.I$''''''''''''''$ Definition 1.2, smooth in $b$ by (P3)); the corrections #1-#4 (#1 III.I$''''$ Definition
2.1, #2 III.I$'''''''$ Definition 2.1, #3 III.I$''''''''$ Definition 2.1, #4 III.I$'''''''''$ Definition 2.1; verifier
145's n3, 146's n2) and their counterterms are the tensors built from $b_0$-objects, as the source builds them ([Hin26]
p. 275, Definition 11.55; its operator is at $b$, Definition 11.56). At a base point $(h,\vec p)$ with parameter $b$,
$$D_{\vec p}P_4(h,\vec p)(W_\nu = W) = L_{h,\vec p}m_\nu(W)+r^\nu_{h,\vec p}(W)+E^\nu_{h,\vec p}(W).\tag{1.1}$$
Here $f^\nu_b := L_{h,\vec p}m_\nu+r^\nu_{h,\vec p}$ is III.I$'''''''''$ Lemma 2.6 (c) at $b$, with every object (rows,
corrections, counterterms) built at $b$, in the classes of III.I$'''''''''$ (2.5) uniformly in $b$. And
$$E^\nu_{h,\vec p}(W) := L_{h,\vec
p}\big(h^{b_0}_\nu-h^b_\nu\big)(W)
+\delta^*_{g_0,E_C}\big(\vartheta^{b_0}_{\nu,\sharp}-\vartheta^b_{\nu,\sharp}\big)(W),$$
the difference between the corrections and counterterms built at $b_0$ and at $b$, lies in $\mathcal
Y^\natural_2(\alpha-)\cap\mathcal Y(\alpha_1)$, with norm $O(|b-b_0||W|)$. Its support is in $\mathrm{supp}\,\chi_K$,
its $K^+$-weight is $\kappa_\nu-\epsilon>\alpha$, and its $\iota^+$-exponents below $w_+$ lie in $\mathcal E^\natural+2$
(III.I$'''''''''''''$ Definition 1.2).

*Proof.* (P1)-(P4) are the cited statements. (P5): $g_b$ is stationary. The reality in (P3) holds as at $b_0$: $L_b$,
$\delta^*_{g_b}$ and $\Box_{g_b}$ are real, and III.D$'''$ Proposition 3.1, III.F$''''$ Proposition 5.1 and
III.I$''''''''''''''$ Lemma 2.1's normalisation are real constructions (verifier 148's m3). The parity in (P3): the
pullback by $-1$ maps the nullspace of $\widehat{L_b}(0)$ in $\mathcal X_0$ to itself, and an element of that nullspace
is fixed by its leading terms at $\partial X$ (the matrix $B(b)$ of III.H Proposition 3.2's proof is invertible). The
leading terms of $h_b(S)$ are those at $b_0$ ((P3)), odd, as the translations are; $g_{b'}$ is invariant for every $b'$,
so $\dot g_b(\dot b)$ is even; and $h_{b,\mathrm v1}(V)$ is $\delta^*_{g_b}$ of the 1-form of III.D$''$ (3.4) in
$\ker\Box^\Upsilon_b$ fixed by its leading term, the rotation 1-form $x^idx^j-x^jdx^i$, which is even, and $-1$ commutes
with every rotation $V$. The companions are fixed by the tower relations and their leading terms, and inherit the
parity. (P6): $f^\nu_b$ is III.I$'''''''''$ Lemma 2.6 (c)'s computation at $b$. Its errors near $K^+$ are $L_{h,\vec
p}-L_b$, which gains $a_K$ there, $g_0 = g_b$ near $K^+$ (III.I Lemma 3.6); its objects are smooth in $b$ (P3), so the
bounds are uniform. For $E^\nu$ (verifier 131's m1 and section B): - The differences $h^{b_0}_\nu-h^b_\nu$ and
$\vartheta^{b_0}_{\nu,\sharp}-\vartheta^b_{\nu,\sharp}$ are $b$-differences of the 1-form towers and of their
commutators with $\chi_K$, so $O(|b-b_0|)$ by (P3), and supported in $\mathrm{supp}\,\chi_K$. - Near $K^+$ the
corrections vanish (they are supported in $\mathcal C$), but the counterterms do not: there $\vartheta_{\nu,\sharp} =
\frac12\Box\omega_\nu$ (III.I$'''''''''$ section 2). Their difference has the $K^+$-weight $\kappa_\nu$ of the tops of
the towers (III.I$'''''''''$ Lemma 2.2 (a), (d), and (P3)). So $E^\nu$ has $K^+$-weight $\kappa_\nu-\epsilon>\alpha$. -
At $\iota^+$, the $b$-differences of the towers have exponents $\lambda_\nu+\mathcal E_{\mathrm{ind}}$ (for v1 also
$\lambda_\nu+3$; III.I$''''''''''''''$ Lemma 2.1), with $\lambda_\nu$ the row's $\iota^+$-exponent in $\mathcal
E_{\mathrm{par}}\cap\{\mathrm{Re}\le3\}\subset\mathcal E_\sharp$. $L$ and $\delta^*$ add 2 and increments, and the parts
of $L_{h,\vec p}-L_b$ from $h$ and $h_{\mathrm{tot}}$ gain $\rho_+^{\lambda_\sharp}$. So below $w_+$ the exponents lie
in $\mathcal E^\natural+2$ (III.I$'''''''''''''$ Definition 1.2), with log orders bounded by III.I$'''''''''''''$ Lemma
1.3 (a), and above it the plain weight is $\mathrm{Re}\,\lambda+2+\lambda_\sharp>w_+$. - So $E^\nu\in\mathcal
Y^\natural_2(\alpha-)$, and $E^\nu\in\mathcal Y(\alpha_1)$ as $\mathcal E^\natural\cap\{\mathrm{Re}<2\}\subset\mathcal
E_{++}$ (III.I$'''''''''''''$ Lemma 1.3 (a)). $\square$

The source makes the same choice: its corrections are built at $b_0$, its operator is at $b$ (Definition 11.56), and its
expansion's towers are those of $L_b$ (Theorem 11.59). Rows built at $b_0$ would leave $(L_b-L_{b_0})m^{b_0}_\nu$ near
$K^+$, of $K^+$-order only $\mathrm{Re}\,e_\nu+2$. Rows at $b$ move the mismatch into the $b$-differences of the
corrections and counterterms, which near $K^+$ enter only through the counterterms, at the weight $\kappa_\nu$ (verifier
130's m2, 131's m1). Corrections #1-#2 are commutator terms in $\mathrm{supp}\,d\chi_K$ (III.I$''''$, III.I$'''''''$),
so $f^S$, $f^b$ and $f^{\mathrm s1}$ vanish near $K^+$, and their $b_0/b$ mismatch lies at $\iota^+$ only, with the gain
$\rho_+^2$ of $g_b-g_{b_0}$ (verifier 131's n8). For $f^S$ in III.I$''''$ that mismatch is Lemma 2.7's $E^S_b$, carried
by Proposition 2.8 (D329); for $f^S$, $f^b$ and $f^{\mathrm s1}$ in III.I$'''''''$ it is Lemma 2.11's
$E^{\mathrm{mot}}_b$, carried by Proposition 2.12 (D330). The corrections #3 are not commutators, and their counterterms
do not vanish near $K^+$ (PART-III-I9-COMMOTION.md:99-100); their rows $(\mathrm s1,\lambda,k)$ are rows of
III.I$'''''''''$'s $\mathcal N$ (PART-III-I10-CORR4.md:179-181), so they enter through (1.1) (verifier 146's n2, n4). At
$b_0$, $E^\nu = 0$ and (1.1) is III.I$'''''''''$'s identity.

**Lemma 1.2 (joint injectivity at $b$).** Shrinking $\mathcal B_*$, III.I$''''''''''$ Lemma 2.2 and Corollary 2.3 hold
at every $b\in\bar{\mathcal B}_*$, for the states at $b$: if $\sum_{\tau\ne\mathrm v1}h_{b,\tau}(W_\tau) = 0$ then every
$W_\tau = 0$; and a finite sum of rows $\nu\ne\mathrm v1$ at $b$ with $K^+$-weight above the largest of their rates
vanishes. Moreover, there are a compact $\mathcal K_0\subset X^\circ$ and $c>0$, independent of $b$, with
$\sup_{\mathcal K_0}|\sum_\tau h_{b,\tau}(W_\tau)|\ge c\sum_\tau|W_\tau|$.

*Proof.* The space $\mathcal W := \bigoplus_{\tau\ne\mathrm v1}\mathcal W_{\tau,\mathbb C}$ is finite-dimensional. At
$b_0$ the map $\Theta_{b_0}: W\mapsto\sum_\tau h_{b_0,\tau}(W_\tau)$ is injective (III.I$''''''''''$ Lemma 2.2). Each
nonzero element of its range is a nonzero smooth tensor on $X^\circ$, nonzero on an open set, so by compactness of the
unit sphere of $\mathcal W$ there is a compact $\mathcal K_0\subset X^\circ$ on which $\sup_{\mathcal
K_0}|\Theta_{b_0}W|\ge2c|W|$. $\Theta_b$ depends continuously on $b$ in $C^0(\mathcal K_0)$ (P3), so the bound with $c$
holds for $b$ near $b_0$. Corollary 2.3's proof uses only Lemma 2.2 and III.I$'''''''''$ Lemma 2.2 (e), the $K^+$-weight
$\mathrm{Re}\,e_\nu+1-\epsilon$ of $m_\nu(W)-\chi_Kr_\nu h_\tau(W)$, which is a computation with the tower relations and
holds at $b$ (P3). $\square$

v1 stays excluded at $b$, as at $b_0$, for a quantitative reason. At $b$, $h_{b,\mathrm v1}(V)$ is $\delta^*_{g_b}$ of a
1-form in $\ker\Box^\Upsilon_b$ (III.D$''$ (3.4)), so it lies in $\ker\widehat{L_b}(0)$ in III.H's space $\mathcal X_0$,
and it is $O(|b-b_0||V|)$ (P3). Near $b_0$ that nullspace has the dimension it has at $b_0$, with the continuous basis
$\dot g_b(\dot b)$, $h_b(S)$ (III.H Proposition 3.2's proof: the matrix $B(b)$ is invertible). So $h_{b,\mathrm v1}(V) =
\dot g_b(\dot b_V)+h_b(S_V)$ with $|\dot b_V|+|S_V| = O(|b-b_0||V|)$. Moreover $S_V = 0$: the pullback by $-1$ fixes
$h_{b,\mathrm v1}(V)$ and $\dot g_b(\dot b_V)$ and reverses $h_b(S_V)$ ((P3)), so $h_b(S_V) = 0$, and $S_V = 0$ by the
injectivity of $S\mapsto h_b(S)$. So $h_{b,\mathrm v1}(V) = \dot g_b(\dot b_V)$, and $\ker h_{b,\mathrm v1} = \{V:\dot
b_V = 0\}$ (verifier 150's M1). A $K^+$-extraction that read a v1 coefficient beside the $b$- and $S$-coefficients would
invert a map that degenerates as $b\to b_0$ (verifier 130's m4). This is why the v1 coefficients are assigned in section
2, not read from the $K^+$-expansion.

## 2. The rotation rows at $b$

Let $\mathcal N_{\mathrm{rot}}$, $\mathcal M_{\mathrm{rot}} = \mathcal E_\sharp\cap\{\mathrm{Re}\le2\}$ and the rotation
rows $m_\nu$, $\nu = (\mathrm{rot},\lambda,k)$, be those of III.I$''''''''''''''$ Definitions 1.1 and 1.3, with the v1
tower $T_{\mathrm v1,b}$ at the base point's $b$: $m_\nu(W) = \chi_KT_{\mathrm v1,b}(a_\nu W)$, $a_\nu =
t_*^{-\lambda}(\log t_*)^k$, $W\in\mathcal V_{1,\mathbb C}$.

**Lemma 2.1 (rotation rows at $b$).** At $b\in\bar{\mathcal B}_*$, $m_\nu(W)$ has $K^+$-weight
$\mathrm{Re}\,\lambda-\epsilon$ (its bottom $a_\nu h_{b,\mathrm v1}(W)$, of size $O(|b-b_0||W|)$), and
$m_\nu(W)-\chi_Ka_\nu h_{b,\mathrm v1}(W)$ has $K^+$-weight $\mathrm{Re}\,\lambda+1-\epsilon$. III.I$'''''''''$ Lemmas
2.2 (a)-(e) and 2.4-2.6 hold for $\nu$ at $b$, with $e_\nu = \lambda$ and $\kappa_\nu = \mathrm{Re}\,\lambda+4$; in
particular $f^\nu_{h,\vec p}(W) := D_{\vec p}P_4(h,\vec p)(W_\nu = W) = f^\nu_b(W)+E^\nu_{h,\vec p}(W)$ as in (1.1),
with $f^\nu_b(W) = L_{h,\vec p}m_\nu(W)+r^\nu_{h,\vec p}(W)\in\mathcal Y_2(\alpha)$ uniformly in $b$, and $E^\nu_{h,\vec
p}(W)\in\mathcal Y^\natural_2(\alpha-)\cap\mathcal Y(\alpha_1)$ of size $O(|b-b_0||W|)$.

*Proof.* As III.I$''''''''''''''$ Definition 1.3 states for $b_0$: the proofs of III.I$'''''''''$ Lemmas 2.2 (a)-(e) and
2.4-2.6 use the tower relations and not the coefficient space, and hold at $b$ by (P3) and (P6). The only change is the
bottom, which at $b_0$ vanishes and at $b$ is $a_\nu h_{b,\mathrm v1}(W)$; it has $K^+$-weight
$\mathrm{Re}\,\lambda-\epsilon$ and is $O(|b-b_0||W|)$ by (P3). The source term $L_{h,\vec p}m_\nu(W)$ involves only the
top of the tower, as $T_{\mathrm v1,b}$ solves $L_b$ to its length (the tower relations), so its $K^+$-order is
unchanged. $\square$

**Proposition 2.2 (the v1 terms are rotation rows with assigned coefficients).** Let $b\in\bar{\mathcal B}_*$ be the
black hole parameter of the base point.

(a) *The spacetime phase.* In III.I$''''''''''$ Proposition 3.1 at $b$, for each $u$-exponent $\lambda_0$ with
$\mathrm{Re}\,\lambda_0<2$ the graft's tower part $\chi_Ku^{(j)}_{b,0}$ (III.G$''$ (4.3) at $b$) equals
$$\sum_{\tau\in\mathcal T\setminus\{\mathrm
v1\}}m_{(\tau,\lambda_0,j)}(W^{(j)}_\tau)+m_{(\mathrm{rot},\lambda_0,j)}(V^{(j)})$$
up to $K^+$-weight $\mathrm{Re}\,\lambda_0+1-\epsilon$. Here $V^{(j)}$ is the graft's v1 coefficient of
$t_*^{-\lambda_0}(\log t_*)^j$, read from the $\iota^+$-data $u_+$ by III.G$''$ Theorem 3.1, in the normalisation of
III.I$''''''''''$'s rows, in which a $(\log t_*)^j$-term keeps the prefactor of the term $j = 0$ (verifier 130's n1);
for $j = 0$ it is $-\lambda_0^{-1}V^{(-1)}_1$, by $a_{\mathrm v1} = -\lambda_0^{-1}t_*^{-\lambda_0}$ (III.G$''$ (4.2)).
It is linear and continuous in the source, uniformly in $b$. $(\lambda_0,j)\in\mathcal M\subset\mathcal
M_{\mathrm{rot}}$, so the rotation row exists. So III.I$''''''''''$ Proposition 3.1 (b) holds at $b$ with the rows
$\mathcal N_\iota\sqcup\mathcal N_{\iota,\mathrm{rot}}$ and these coefficients.

(b) *The spectral phase.* In III.I$'''''''''''$ Proposition 3.1 at $b$, the v1 term of III.I$'''''''''''$ Lemma 2.3's
(2.2), $c_{\mathrm v1}(\sigma)T_{\mathrm v1,b}(\sigma)$, now has the bottom $c_{\mathrm v1}(\sigma)h_{b,\mathrm v1}(Y)$,
and its rate is $\alpha_0$ (at $b_0$, $\alpha_0+1$). At level 1 ($2\le\mathrm{Re}\,\alpha_0<2+\eta_1$) this is below
$\alpha-2$ only for $\mathrm{Re}\,\alpha_0 = 2$ (by (G), no rate lies in $(2,2+\epsilon_K]$). Those exponents lie in
$\mathcal E_\sharp\cap\{\mathrm{Re} = 2\}\subset\mathcal M_{\mathrm{rot}}$, and the term is, by III.I$''''''''''''$
Lemma 2.1 (b), $m_{(\mathrm{rot},\alpha_0,k)}(Y')$ up to $K^+$-weight $\mathrm{Re}\,\alpha_0+1-\epsilon$, with $Y'$ the
coefficient that III.I$'''''''''''$ Lemma 2.3 gives the v1 tower: $Y$ times the constant of $c_{\mathrm v1}$, read from
the tf-data. It is linear and continuous in the source, uniformly in $b$ by (P2) and (P4). At level 2 the v1 rate is
$\alpha_0+1\ge2+\eta_1>2+\epsilon_K\ge\alpha-2$, as for the s0 and s2 towers there. So III.I$'''''''''''$ Proposition
3.1 holds at $b$ with the rows $\mathcal N_\sigma\sqcup\mathcal N_{\sigma,\mathrm{rot}}$ and these coefficients.

(c) *No other v1 term.* Every v1 coefficient of the expansion has its exponents in $\mathcal E_\sharp$
(III.I$''''''''''''$ Theorem 3.1, at $b$ Corollary 2.10: an $\iota^+$-exponent $\lambda$ of $u$ gives the coefficient
$t_*^{-\lambda+d_\rho}$, $d_{\mathrm v1} = 0$). So it either has real part at most 2, and is one of (a)-(b), or real
part above $2+\epsilon_K\ge\alpha-2$, and is carried by $q$ (III.I$''''''''''''''$ Definition 1.1, whose rates at a
rotating $b$ are $\mathrm{Re}\,z>2+\epsilon_K$).

*Proof.* (a) At $b$, III.G$''$ Theorem 4.2 gives the v1 term $h^{\le2}_{b,\mathrm v1}(a_{\mathrm v1}V^{(-1)}_1)$ of
(4.3), with $V^{(-1)}_1$ from $u_+$, which does not depend on $b$ ((P2): $u_+ = N_{\iota^+}(\lambda)^{-1}(2f_+)$, and
III.G$''$ Theorem 3.1's decomposition is of $u_+$ on $\iota^+$). By (4.2), $a_{\mathrm v1} =
-\lambda_0^{-1}t_*^{-\lambda_0}$, so $\chi_Kh^{\le2}_{b,\mathrm v1}(a_{\mathrm v1}V) =
m_{(\mathrm{rot},\lambda_0,0)}(-\lambda_0^{-1}V)$ up to the tower terms of order $\ge3$, of $K^+$-weight
$\mathrm{Re}\,\lambda_0+3-\epsilon$ (III.I$''''''''''''''$ Definition 1.3, the rotation rows using $h^{\le2}$ and the
tower of III.I$'''''''''$). The other rows are identified as in III.I$''''''''''$ Proposition 3.1 at $b$, by
III.I$''''''''''$ Lemma 2.1 (c) at $b$ (P3). (b) The proof of III.I$'''''''''''$ Lemma 2.3 at $b$ is unchanged except
that the v1 tower $T_{\mathrm v1,b}(\sigma) = \sum_i(-i\sigma)^i\breve h^i_{b,\mathrm v1}(Y)$ has $\breve h^0_{b,\mathrm
v1} = h_{b,\mathrm v1}\ne0$. Its contribution with $c_{\mathrm v1}$ is a piece of type (b) of III.I$''''''''''''$ Lemma
2.1, a tower with polyhomogeneous coefficient. Its rate is that of $\mathcal F^{-1}(\chi c_{\mathrm v1})$, which at
level 1 is $\alpha_0$ (the piece is $\sigma u_{(\alpha_0,k)}$, and $c_{\mathrm v1}$ contributes $|\sigma|^{\alpha_0-1}$
to it). The level-2 count is III.I$'''''''''''$'s, with the rate lowered by 1. (c) As stated. $\square$

**Definition 2.3 (the assigned rotation coordinates).** Let $(h,\vec p)$ be a base point with parameter
$b\in\bar{\mathcal B}_*$, and $G\in\mathcal Y^\natural(\beta)$, $\beta>3$. The *assigned rotation coordinates*
$A_{b,\nu}(G)\in\mathcal V_{1,\mathbb C}$, $\nu\in\mathcal N_{\mathrm{rot}}$, are the coefficients of the rotation rows
that Proposition 2.2 (a)-(b) produces in the forward solution of $L_{h,\vec p}u = G$: the graft's v1 coefficients at the
exponents of $\mathcal M$ (spacetime phase), and the spectral level-1 coefficients at the exponents of real part 2. They
do not depend on $\beta$ or on $\epsilon$, and neither does $E^\nu$ ((P6); verifier 148's n3). $A_b$ commutes with
complex conjugation, $A_{b,\bar\nu}(\bar G) = \overline{A_{b,\nu}(G)}$, as $L_{h,\vec p}$ is real and the objects of
Proposition 2.2 are real ((P3)); so for real $G$ the tuple $(A_{b,\nu}(G))_\nu$ is conjugation-symmetric, as (2.2) and
III.I$''''''''''''''$ Definition 1.3 need (verifier 147's n2, 148's m3). $A_b := (A_{b,\nu})_\nu$ is linear and
continuous on $\mathcal Y^\natural(\beta)$, uniformly in $b$ and in $(h,\vec p)$ small, (Proposition 2.2, (P2), (P4)).
No continuity in $b$ is claimed or needed (Proposition 2.5's Step 3). It is defined at $b_0$ by the same formulas.

**Lemma 2.4 (III.I$'''''''''''''$ Lemmas 2.2-2.3 at $b$).** Let $\beta\in(3,4+\epsilon_K]$ be admissible, $(h,\vec p)$ a
base point with parameter $b\in\bar{\mathcal B}_*$ and $h\in\mathcal X^\infty$ small, $G\in\mathcal Y^\natural(\beta)$,
and let the forward solution $u$ of $L_{h,\vec p}u = G$ satisfy the hypothesis of III.I$'''''''''''''$ Lemma 2.2. Then
$$u = \sum_{\nu\in\mathcal N_\beta}m_\nu(S_\nu)+\sum_{\nu\in\mathcal
N^{<\beta}_{\mathrm{rot}}}m_\nu\big(A_{b,\nu}(G)\big)+\tilde u,\qquad\mathcal N^{<\beta}_{\mathrm{rot}} :=
\{\nu\in\mathcal N_{\mathrm{rot}}:\mathrm{Re}\,\lambda_\nu<\beta-2\},\tag{2.1}$$
with $\tilde u$ in the class of III.I$'''''''''''''$ (2.2) and $S_\nu = S^{h,\vec p,\beta}_\nu(G)$ determined by
$u-\sum_{\mathcal N^{<\beta}_{\mathrm{rot}}}m_\nu(A_{b,\nu}(G))$, conjugation-symmetric, linear and continuous in $G$,
uniformly. At a fixed $b$: if $(h_j,\vec p_j)\to(0,\vec p_b)$, with $\vec p_b$ the parameter whose only nonzero
component is $b-b_0$, and $G_j\to G$ in $\mathcal Y^\natural(\beta)$, with the hypothesis of III.I$'''''''''''''$ Lemma
2.3, then $S^{h_j,\vec p_j,\beta}_\nu(G_j)\to S^{0,\vec p_b,\beta}_\nu(G)$. At $b_0$ the second sum in (2.1) is absent
(the rotation rows' rates there are $\mathrm{Re}\,\lambda+1>\alpha-2\ge\beta-2$), and (2.1) is III.I$'''''''''''''$
(2.2). For $\beta<3$ no rotation row has rate below $\beta-2$ ($\mathrm{Re}\,\lambda-\epsilon>1$, Lemma 2.1), and
III.I$''''''''$ Lemma 3.2 holds at $b$ as at $b_0$.

*Proof.* III.I$'''''''''''''$ Lemma 2.2's proof builds the expansion from the pieces of III.I$''''''''''$ Proposition
3.1 (the spacetime phase), III.I$'''''''''''$ Proposition 3.1 and Theorem 4.1 (the spectral phase), III.I$''''''''''''$
Theorem 3.1 (at $b$, Corollary 2.10) and III.I$'''''''''''''$ Proposition 2.1, and reads the coefficients by
III.I$''''''''''$ Corollary 2.3. At $b$ these hold with the model objects at $b$ ((P1)-(P6)), except the v1 pieces of
exponent in $\mathcal M_{\mathrm{rot}}$. By Proposition 2.2 (a)-(c) those are the rotation rows with the coefficients
$A_{b,\nu}(G)$, up to $K^+$-weight $\mathrm{Re}\,\lambda+1-\epsilon>\beta-2$, which goes into $\tilde u$. The rows other
than v1 are then read from $u-\sum m_\nu(A_{b,\nu}(G))$, uniquely, by Corollary 2.3 at $b$ (Lemma 1.2). For the
continuity at fixed $b$, III.I$'''''''''''''$ Lemma 2.3's proof runs with $L_{0,\vec p_b}$ in place of $L_{b_0}$. Its
remainder $(L_{h_j,\vec p_j}-L_{0,\vec p_b})u_j$ gains $a_K$ near $K^+$, where both backgrounds equal $g_b$ (III.I Lemma
3.6). Continuity across $b$ is not claimed: the proofs perturb from a reference operator, and $L_b-L_{b_0}$ gains only 2
at $K^+$ (verifier 131's M1). $\square$

**Proposition 2.5 (III.I$''''''''''''''$ Theorem 3.1 at $b$).** Let $h\in\mathcal X^\infty$, $\vec p\in\mathcal P$ with
parameter $b\in\bar{\mathcal B}_*$, and $q\in\mathcal Q$ be small, and $F\in\mathcal Y^\natural(\alpha-)$. For $\vec
p\,'\in\mathcal P$ let $u(\vec p\,')$ be the forward solution of III.I$''''''''''''''$ (3.1), and (III.I$''''''''''''''$
Step 2, with (1.1))
$$G'(\vec p\,') := \tilde G-f^S_{h,\vec p}(S')-f^b_{h,\vec p}(b')-f^{\mathrm s1}_{h,\vec
p}(S^{(0)\prime}_1)-\sum_{\nu\in\mathcal N\sqcup\mathcal N_{\mathrm{rot}}}\big(r^\nu_{h,\vec p}+E^\nu_{h,\vec
p}\big)(W'_\nu),\qquad\tilde G := F-\Delta_q(\vec p\,')-R_qu(\vec p\,').$$
There is a unique $\vec p\,'\in\mathcal P$ with
$$W'_\nu = A_{b,\nu}\big(G'(\vec p\,')\big)\qquad(\nu\in\mathcal N_{\mathrm{rot}})\tag{2.2}$$
such that $u(\vec p\,')$ satisfies the conclusions of III.I$''''''''''''''$ Theorem 3.1: (3.1)-(3.2), and $u =
h_{b,\mathrm{rem}}(q')+h'$ with $q'\in\mathcal Q$. $\vec p\,'$, $q'$ and $h'$ are linear in $F$, with bounds uniform for
$(h,\vec p,q)$ small, $b$ included. At $b_0$, (2.2) is III.I$''''''''''''''$ Step 4$'$'s condition $C^{\mathrm{rot}} =
0$, and $\vec p\,'$ is that of III.I$''''''''''''''$ Theorem 3.1.

*Proof.* *Steps 0-1* are III.I$''''''''''''''$'s at $b$, by (P1)-(P6). $E^\nu\in\mathcal Y(\alpha_1)$, by (P6), joins
the terms of Step 1. The rotation rows, of $K^+$-weight $\mathrm{Re}\,\lambda-\epsilon>1>\alpha_1-2$ (Lemma 2.1), lie
above the base level.

*Step 2 at $b$.* Let $u := u(\vec p\,')\in\mathcal Z_{\beta_k}$. As in III.I$''''''''''''''$ Step 2, by (1.1), $u_0 :=
u+\sum_{\mathcal N\sqcup\mathcal N_{\mathrm{rot}}}m_\nu(W'_\nu)$ solves $L_{h,\vec p}u_0 = G'(\vec p\,')\in\mathcal
Y^\natural(\beta_{k+1})$ (resp. $\mathcal Y^\natural(\alpha-)$ for $k+1 = K$). Lemma 2.4 gives, for $\beta_{k+1}>3$
(below 3, III.I$''''''''$ Lemma 3.2 as in III.I$''''''''''''''$ Step 2),
$$u = \sum_{\nu\in\mathcal N_{\beta_{k+1}}\sqcup\mathcal N^{<\beta_{k+1}}_{\mathrm{rot}}}m_\nu\big(C^{k+1}_\nu(\vec
p\,')\big)+\tilde u,\qquad\tilde u\in\mathcal Z_{\beta_{k+1}},\tag{2.3}$$
with $C^{k+1}_\nu := S^{h,\vec p,\beta_{k+1}}_\nu(G'(\vec p\,'))-W'_\nu$ for $\nu\in\mathcal N_{\beta_{k+1}}$, and
$C^{k+1}_\nu := A_{b,\nu}(G'(\vec p\,'))-W'_\nu$ for $\nu\in\mathcal N^{<\beta_{k+1}}_{\mathrm{rot}}$. The
$m_\nu(W'_\nu)$ of the other rows, of $K^+$-weight above $\beta_{k+1}-2$, are part of $\tilde u$. The *new rows* of the
level are those of $\mathcal N_{\beta_{k+1}}$ of rate in $[\beta_k-2,\beta_{k+1}-2)$, as at $b_0$, and the rotation rows
of $\mathcal N^{<\beta_{k+1}}_{\mathrm{rot}}\setminus\mathcal N^{<\beta_k}_{\mathrm{rot}}$. If the conditions of the
lower levels hold, then the coefficients of the old rows vanish. For a rotation row, $C^{k+1}_\nu$ is the same function
of $\vec p\,'$ at every level, $A_b$ not depending on $\beta$. For the other rows, $\sum_{\mathcal
N_{\beta_k}}m_\nu(C^{k+1}_\nu)\in\mathcal Z_{\beta_k}$, so they vanish by Lemma 1.2. Hence $u\in\mathcal
Z_{\beta_{k+1}}$ if $C^{k+1}_\nu(\vec p\,') = 0$ for the new rows. The converse is not claimed for the rotation rows
(Remark 2.6).

*Step 3 at $b$.* Let $\mathcal P_k$ be the set of $\vec p\,'\in\mathcal P_0$ with $C^j_\nu(\vec p\,') = 0$ for the new
rows of every level $j\le k$; by Step 2, $u(\vec p\,')\in\mathcal Z_{\beta_k}$ on $\mathcal P_k$. As in
III.I$''''''''''''''$ Step 3, $\mathcal P_k$ is, by induction, the graph of an affine map from the coordinates of the
rows of rate $\ge\beta_k-2$ to the others. The rotation rows enter by their rates $\mathrm{Re}\,\lambda$ at $b$. On
$\mathcal P_k$, $C^{k+1}$ restricted to the new coordinates is $-\mathrm{id}+A_k$, with $A_k\to0$ as $(h,\vec
p,q)\to(0,0,0)$, the parameter of $\vec p$ tending to $b_0$. The bound on $A_k$ is direct, with no continuity in $b$. By
Step 2, $C^{k+1}_\nu(\vec p\,') = S^{h,\vec p,\beta_{k+1}}_\nu(G'(\vec p\,'))-W'_\nu$, resp. $A_{b,\nu}(G'(\vec
p\,'))-W'_\nu$, and $G'$ is affine in $\vec p\,'$. Its dependence on the coordinates $W'_\nu$ of the rows of $\mathcal
N\sqcup\mathcal N_{\mathrm{rot}}$ is through: - $(r^\nu_{h,\vec p}+E^\nu_{h,\vec p})(W'_\nu)$. At the base point
$(0,\vec p_b)$ the identity of III.I$'''''''''$ Lemma 2.4 at $b$ gives $f^\nu_b = L_{0,\vec p_b}m_\nu$ up to the
$O(|b-b_0|)$ mixing of $g_{b_0,b,0}$ in $\mathcal C$. So $r^\nu_{h,\vec p}+E^\nu_{h,\vec p}$ has norm $O(\|h\|+|\vec
p-\vec p_b|+|b-b_0|)$ in $\mathcal Y^\natural_2(\alpha-)$ (III.I$'''''''''$ Lemma 2.6's bounds at $b$, and (P6)). -
$\Delta_q(\vec p\,')$ and $R_qu(\vec p\,')$, of norm $O(\|q\|)$ (III.I$''''''''''''''$ Lemmas 2.3-2.4).

The motion coordinates enter through $f^S$, $f^b$, $f^{\mathrm s1}$, but they lie at the base level, below every new
row. On $\mathcal P_k$ the lower coordinates are, by the induction, affine functions of the free ones with coefficients
of the same smallness. $S^{h,\vec p,\beta}$ and $A_b$ are bounded uniformly in $b$ and $(h,\vec p)$ small (Lemma 2.4,
Definition 2.3). So in the new coordinates $C^{k+1} = -\mathrm{id}+A_k$ with $|A_k|\le C(\|h\|+|\vec p-\vec
p_b|+\|q\|+|b-b_0|)$, $C$ uniform in $b$ (verifier 131's M1, by the direct bound). At the levels below 3 the same direct
bound applies (verifier 133's A-m1): there $C^{k+1}$ is the $K^+$-coefficient of $u = u_0-\sum m(W')$ given by
III.I$''''''''$ Lemma 3.2, a bounded functional of $G'$, uniform in $b$ by (P1), minus $W'$, and $G'$ depends on the new
$W'$ only through the small terms listed above, the rows there being rows of (1.1). At the base level the new
coordinates are the motion parameters $(S',b',S'')$, which enter $G'$ through $f^S$, $f^b$, $f^{\mathrm s1}$ in full.
There the level map is that of III.I$'''''''$ Corollary 4.6, the composite of the maps of its Lemmas 4.3 and 4.5, and
Proposition 2.12 bounds those directly, within $C(\|h\|+|\vec p-\vec p_b|+|b-b_0|)$ of $\pm\mathrm{id}$, with $\|q\|$
entering through $\Delta_q$ and $R_q$ as above (verifier 146's M1, n1). Their composite is block-triangular, not of the
form $-\mathrm{id}+A_k$; what the elimination uses is that its inverse is bounded uniformly, which this gives (verifier
150's n4). So $|A_k|\le C(\|h\|+|\vec p-\vec p_b|+\|q\|+|b-b_0|)$ at every level above the base, the base level's map
has a uniformly bounded inverse, and the continuity statements that III.I$''''''''''''''$ Step 3 cites are not needed.

So $-\mathrm{id}+A_k$ is invertible for $(h,\vec p,q)$ small, and $\mathcal P_{k+1}$ is a graph. At $k = K$ every row
has rate below $\alpha-2$ (the rotation rows at $b$: $\mathrm{Re}\,\lambda\le2<\alpha-2$), so $\mathcal P_K$ is one
point $\vec p\,'$. It satisfies (2.2), and $u(\vec p\,')\in\mathcal Z_\alpha$ with no rotation-row content. The rest of
III.I$''''''''''''''$'s proof, the splitting $u = h_{b,\mathrm{rem}}(q')+h'$ by III.I$''''''''''''$ Theorem 3.1 at $b$
(Corollary 2.10), then applies. The v1 coefficient of $q'$ has no term at $\mathcal M_{\mathrm{rot}}$. $\vec p\,'$ is
affine in $F$, which enters through $\tilde G$ only, and linear since it vanishes at $F = 0$. Uniqueness: any $\vec
p\,''$ satisfying (2.2) with $u(\vec p\,'')\in\mathcal Z_\alpha$ lies in $\mathcal P_0$ (III.I$''''''''''''''$ Step 1's
uniqueness). Its non-rotation coefficients vanish level by level by Lemma 1.2, since (2.2) removes the rotation rows
from (2.3). So $\vec p\,''\in\mathcal P_K$.

*At $b_0$.* At $b_0$ the v1 coefficient of $u = u_0-\sum m_\nu(W'_\nu)$ at $\mathcal M_{\mathrm{rot}}$ is
$A_{b_0}(G')-\vec W'^{\mathrm{rot}}$. The v1 pieces of $u_0$ are the construction's, with the coefficients $A_{b_0}(G')$
(Proposition 2.2 at $b_0$). On $\mathcal P_K$ the coefficients of the rows of $\mathcal N$ vanish, and
III.I$''''''''''''''$ Step 4$'$'s functional $\ell$, applied to $u = u_0-\sum m_\nu(W'_\nu)$, returns its v1 coefficient
uniquely; by Proposition 2.2 (c) and Definition 2.3 it is $A_{b_0}(G')-\vec W'^{\mathrm{rot}}$ (verifier 131's n3), and
$m_\nu(W)$, $\nu\in\mathcal N_{\mathrm{rot}}$, has v1 coefficient $a_\nu W$. So $C^{\mathrm{rot}} = 0$ is (2.2) (with
the sign of Step 4$'$'s derivative $-\mathrm{id}$; verifier 130's m1 corrects D297's sign). The $\vec p\,'$ of
III.I$''''''''''''''$ Theorem 3.1 satisfies the level conditions and (2.2), so it is the point $\mathcal P_K$. $\square$

**Remark 2.6 (uniqueness at $b$).** At a rotating $b$, the $\vec p\,'$ of Proposition 2.5 is unique only together with
(2.2). The bottom of $m_\nu(W)$, $\nu\in\mathcal N_{\mathrm{rot}}$, is $a_\nu h_{b,\mathrm v1}(W) = a_\nu(\dot g_b(\dot
b_W)+h_b(S_W))$, with coefficients $O(|b-b_0||W|)$ (Lemma 1.2's remark). The $K^+$-expansion does not separate it from
the $b$- and $S$-rows, so the conditions $u\in\mathcal Z_{\beta_k}$ alone are not shown to fix $\vec W'^{\mathrm{rot}}$
(verifier 131's n5). The later parts use only the constructed map $F\mapsto(\vec p\,',q',h')$:

- III.J$'$ Theorem 2.1 builds $U'$ from it; its Remark 2.2 records that $D_U\Phi$ is not injective.

- III.J$''$ Theorem 4.1 estimates it.

- III.J$'''$ cites "Step 3 and its uniqueness" to identify the exact and the lossy solutions (its paragraph on
III.I$''''''''''''''$ Theorem 3.1 at exact weights). At $b$, Proposition 2.5's constrained uniqueness serves there:
$A_b$ does not depend on the loss, being computed from $\iota^+$- and tf-data, which the exact and the lossy classes
share.

### 2.6 The boost parameter at $b$

III.I$''''$ Lemma 2.4 is an identity at $b_0$. It uses that $g_{b_0}$ is Ricci flat in $\mathcal C$, and that the
correction and the leading term are built from the same $b_0$-state. At $b$ the background in $\mathcal C$ interpolates
between $g_{b_0}$ and $g_b$, so the identity acquires an error, and III.I$''''$ Proposition 4.1 (2) is proved at $b$ by
a direct bound rather than by continuity at fixed $b$ (verifier 145's M1, D329).

**Lemma 2.7 (the boost identity at $b$).** Let $b\in\bar{\mathcal B}_*$, $G := g_{b_0,b,0} =
(1-\chi_K)g_{b_0}+\chi_Kg_b$ (III.I (1.1)), $P_1(h,S,b)$ as in III.I$''''$ (2.2) with $g_0 := g_{b_0,b,-S}$, and
$f_{0,0;b}(\dot S) := D_SP_1(0,S,b)|_{S=0}(\dot S)$. Let $h^{\le1}_{b,\natural}(\dot S) :=
\delta^*_{g_b}\omega^{\le1}_{b,\natural}(\dot S)$ be the re-centred s1 state at $b$ ((P3), with the gauge 1-form of
III.D$'''$ at $b$; at $b_0$ it is III.I$''''$'s $h^{\le1}_\natural$). Then
$$f_{0,0;b}(\dot S) = L^{G,G}\big(\chi_Kh^{\le1}_{b,\natural}(\dot S)\big)+E^S_b(\dot S),\tag{2.4}$$
where $E^S_b(\dot S)$ is supported in $\mathcal C$, vanishes at $b = b_0$, and, near $(\iota^+)^\circ$, lies in
$\mathcal A^{\mathcal G+2-\delta}$ for every $\delta>0$, $\mathcal G := (2,0)\cup(2+\mathcal E_{\mathrm{ind}})$, with
seminorms $O(|b-b_0||\dot S|)$ uniformly on $\bar{\mathcal B}_*$.

*Proof.* *Support.* By III.I (1.1), $g_{b_0,b,-S} = (1-\chi_K)\phi^*_{-S}g_{b_0}+\chi_Kg_b$, and the corrections
$h^{(-1)}$, $\vartheta_\sharp$ of III.I$''''$ Definition 2.1 are supported in $\mathcal C$ (III.I$''''$ Lemma 2.2). In
the interior of $\chi_K^{-1}(0)$, $g' = g_0 = \phi^*_{-S}g_{b_0}$ is Ricci flat for every $S$, and
$\Upsilon^{E_\Upsilon}(g_0,g_0) = 0$ (III.I$''''$ (i)); so $P_1(0,S,b) = 0$ there for all $S$, and $f_{0,0;b} = 0$. In
the interior of $\chi_K^{-1}(1)$, $g' = g_0 = g_b$ does not depend on $S$, so again $f_{0,0;b} = 0$. On both sets
$L^{G,G}(\chi_Kh^{\le1}_{b,\natural})$ vanishes as well. On the first it vanishes trivially. On the second it is
$L_bh^{\le1}_{b,\natural}$, which is 0: $h^{\le1}_{b,\natural} = \delta^*_{g_b}\omega^{\le1}_{b,\natural}$ lies in $\ker
D_{g_b}\mathrm{Ric}$ by III.I$''''$ (iii), and in $\ker\delta_{g_b,E_\Upsilon}G_{g_b}$ because
$\omega^{\le1}_{b,\natural}$ is a generalised zero energy state of the gauge potential operator at $b$ (III.D$'''$ at
$b$, (P3)). So $E^S_b$ is supported in $\mathcal C$. *At $b_0$.* $G = g_{b_0}$, $L^{G,G} = L_{b_0}$ and
$h^{\le1}_{b_0,\natural} = h^{\le1}_\natural$, so (2.4) with $E^S_{b_0} = 0$ is III.I$''''$ (2.3). *Size.* Every term of
$E^S_b(\dot S)$ is linear in $\dot S$ and a smooth function of $b$ on $\mathcal C$. Its ingredients are $G-g_{b_0} =
\chi_K(g_b-g_{b_0})$, which lies in $|b-b_0|\rho_+^2C^\infty$ near $(\iota^+)^\circ$ (on $\mathcal C$, $|x|\ge t/10$,
and $g_b-g_{b_0} = O(|b-b_0||x|^{-2})$ with all Cartesian derivatives, III.B); the state $h^{\le1}_{b,\natural}$, smooth
in $b$ in $\mathcal A^{\mathcal G-\delta}$ ((P3), with III.H Remark 2.6's loss, (P4)); the $b$-independent corrections;
and $k_0 := \partial_Sg_S(\dot S) = -(1-\chi_K)\delta^*(\Theta w)$, $b$-independent and in $\rho_+^2C^\infty$ near
$(\iota^+)^\circ$ (PART-III-I5-UNBOOST.md:274-279), which enters as $w$ itself has order $\rho_+^{-1}$ (verifier 150's
n2). III.I$''''$ Lemma 2.2's count, that $D_{g_0}\mathrm{Ric}$ and $\delta^*\delta G$ lie in
$\rho_+^2\mathrm{Diff}^2_{\mathrm b}$ near $(\iota^+)^\circ$, takes $\mathcal A^{\mathcal G-\delta}$ into $\mathcal
A^{\mathcal G+2-\delta}$, uniformly for $b\in\bar{\mathcal B}_*$. So $\partial_bE^S_b(\dot S)$ is bounded there by
$C|\dot S|$, and $E^S_b = E^S_b-E^S_{b_0}$ is $O(|b-b_0||\dot S|)$ by the mean value theorem along the segment from
$b_0$ to $b$, which lies in $\bar{\mathcal B}_*$ (a ball, VI.C row b4). $\square$

**Proposition 2.8 (III.I$''''$ Proposition 4.1 (2) and Corollary 4.3 at $b$).** Read III.I$''''$ Proposition 4.1 (1) at
$b\in\bar{\mathcal B}_*$ with the leading term $\chi^H_Kh^{\le1}_b(\dot S)$ built at $b$ ((P3)), and $\dot S(f)$ read
from the coefficient of $t_*$ at $K^+$, which determines it by Lemma 1.2 (the s1 states alone). There are $C$ and a
smallness of $(h,S)$, uniform on $\bar{\mathcal B}_*$, with
$$|S^{(-1)}_{h,S;b}-\mathrm{id}|\le C\big(\|h\|_{\mathcal X^d}+|S|+|b-b_0|\big).\tag{2.5}$$
So, after shrinking $\mathcal B_*$ and the smallness of $(h,S)$, $S^{(-1)}_{h,S;b}$ is invertible with inverse of norm
at most 2, and III.I$''''$ Corollary 4.3 and III.I$'''''$ Corollary 2.2 hold at $b$, with constants uniform in $b$.

*Proof.* At $b$, III.I$''''$ Lemma 4.2's map is $\dot S_{h,S;b}(f) = \Pi_bf'$, with $f' := f-(L_{h,S;b}-L_b)u$. Here
$\Pi_b$ is built from III.I$'$ Proposition 3.1's construction for $L_b$ and from $\tilde L_b(0)^{-1}$ (III.H Proposition
3.2 at $b$, (P4)). Its bound (a) holds with $C$ uniform in $b$, by (P1) and (P4). By Lemma 2.7,
$\chi_Kh^{\le1}_{b,\natural}(S')$ vanishes for $t^\flat_*<10$. It is therefore the forward solution of $L_{0,0;b} =
L^{G,G}$ (III.I$''''$ Lemma 2.5 at $h = 0$, $S = 0$) with the source $f_{0,0;b}(S')-E^S_b(S')$, and it has the form
(4.1) with $\dot S = S'$ and $\tilde u = 0$. Hence, for $S'$ in a basis of $\mathcal S_1$,
$$S^{(-1)}_{h,S;b}(S')-S' = \dot S_{h,S;b}\big(f_{h,S;b}(S')-f_{0,0;b}(S')\big)+\big(\dot S_{h,S;b}-\dot
S_{0,0;b}\big)\big(f_{0,0;b}(S')\big)+\dot S_{0,0;b}\big(E^S_b(S')\big).$$
*The first term.* $f_{h,S;b} := D_SP_1(h,S,b)$ depends smoothly on $(h,S)$. III.I$''''$ Lemma 3.2's bounds hold for
small $(h,S)$ and depend on $b$ only through finitely many seminorms of $g_{b_0,b,-S}$; the derivative of $f_{h,S;b}$ in
$h$ is bounded by III.I$''''$ Lemma 3.1 (3.1), and that in $S$ by the count of its (3.4), for $d$ as in III.I$''''$
Proposition 4.1 (verifier 150's n3). So $\|f_{h,S;b}(S')-f_{0,0;b}(S')\|\le C(\|h\|_{\mathcal X^d}+|S|)|S'|$ in the norm
of Lemma 4.2 (a), and the first term is at most $C(\|h\|_{\mathcal X^d}+|S|)|S'|$. *The second term.* By Lemma 4.2 (b)'s
formula, with $(h_1,S_1) := (h,S)$ and $(h,S) := (0,0)$, it is
$-\Pi_b\big((L_{h,S;b}-L_{0,0;b})u_{h,S}+(L_{0,0;b}-L_b)(u_{h,S}-u_{0,0})\big)$. Here $u_\bullet$ are the forward
solutions with the source $f := f_{0,0;b}(S')$, which vanishes near $\mathscr I^+$ (it is supported in $\mathcal C$).
The coefficients of $L_{h,S;b}-L_{0,0;b}$ lie in Lemma 3.1's class (3.6) with norm at most $C(\|h\|_{\mathcal
X^d}+|S|)$: they are polynomial in the differences of the metrics, with coefficients smooth in their inverses (Lemma
3.1's proof, Lemma 2.5). So (4.2) gives $\|(L_{h,S;b}-L_{0,0;b})u_{h,S}\|\le C(\|h\|_{\mathcal X^d}+|S|)\|f\|$. Since
$L_{0,0;b}(u_{h,S}-u_{0,0}) = -(L_{h,S;b}-L_{0,0;b})u_{h,S}$, III.I$''$ Proposition 5.1, with the weights lowered by the
room $\varsigma$ of Lemma 4.2's proof, gives $\|u_{h,S}-u_{0,0}\|\le C(\|h\|_{\mathcal X^d}+|S|)\|f\|$, and (4.2) bounds
the second summand the same way. $\Pi_b$ is bounded on the space with that room, uniformly in $b$. So the second term is
at most $C(\|h\|_{\mathcal X^d}+|S|)|S'|$. *The third term.* By Lemma 2.7, $E^S_b(S')$ is supported in $\mathcal C$. It
vanishes near $\mathscr I^+$ and $K^+$, and its $\iota^+$-order is at least $4-\delta>\alpha_++2$, as $\alpha_+<2$
(PART-III-I5-UNBOOST.md:320), for $\delta<2-\alpha_+$ (verifier 150's n1). So it lies in the source space of Lemma 4.2
(a) with norm at most $C|b-b_0||S'|$, and the third term is at most $C|b-b_0||S'|$. This proves (2.5), and the Neumann
series gives the inverse. III.I$''''$ Corollary 4.3's proof and III.I$'''''$ Corollary 2.2's use the invertibility
alone, so they hold at $b$. $\square$

III.I$''''$ Lemma 4.2 (b), a continuity at fixed $(h,S)$, is not used at $b$: its difference formula enters only through
the bound above. The same pattern replaced the continuity lemmas for the elimination in Proposition 2.5's Step 3
(verifier 131's M1).

### 2.7 The expansion at $b$: III.I$''''''''''''$ Lemmas 2.3-2.4

III.I$''''''''''''$ Lemmas 2.3 and 2.4 use $h_{b_0,\mathrm v1} = 0$ without saying so. They put $\breve h^1_{b_0,\mathrm
v1}(V)$ in $\ker L_0$, and they remove the v1 content through an antiderivative. At a rotating $b$, $h_{b,\mathrm v1}(V)
= \dot g_b(\dot b_V)$ (Lemma 1.2's remark), and both steps change (verifier 147's M1, D330; verifier 150's M1, D331).
Below, $L_0 := \widehat{L_b}(0)$, $L_1 := [L_b,t_*]$, $L_2 := \frac12[[L_b,t_*],t_*]$; $h := h_{b,\mathrm s1}$, $\breve
h^j := \breve h^j_{b,\mathrm s1}$; $\mathcal G$ is III.I$''''''''''''$'s space of sections conormal of order $>-3$; and
$T_{\mathrm v1,b}(aV) := \sum_ja^{(j)}\breve h^j_{b,\mathrm v1}(V)$, $\breve h^0_{b,\mathrm v1} := h_{b,\mathrm v1}$, is
the rotation row of III.I$''''''''''''''$ Definition 1.3. Put
$$\kappa_b(V) := \breve h^1_{b,\mathrm v1}(V),\qquad L_0\kappa_b(V) = -L_1\dot g_b(\dot b_V).\tag{2.6}$$
The identity holds by the tower relation $L_0\breve h^1_{b,\mathrm v1}(V) = -L_1h_{b,\mathrm v1}(V)$. At $b_0$,
$\kappa_{b_0}(V) = \breve h^1_{b_0,\mathrm v1}(V)$ lies in $\ker L_0$. Let $\mathcal V^0_b := \{V:\dot b_V = 0\} = \ker
h_{b,\mathrm v1}$.

**Lemma 2.9 (III.I$''''''''''''$ Lemmas 2.3-2.4 at $b$).** Let $b\in\bar{\mathcal B}_*$.

(a) If $p\in\mathcal G$ and $L_0p = 0$, then $p = \sum_\rho\breve
h^{(\mu_\rho),0}_{b,\tau_\rho}(Y_\rho)+\kappa_b(V)+\dot g_b(\dot b)+h(S)$, the sum over the rows of $\mathcal R'$ other
than v1, with $V\in\mathcal V^0_b$ and unique coefficients.

(b) If $X\in\mathcal G$ and $L_0X = L_1\dot g_b(\dot b)+L_1\breve h^1(S)+L_2h(S)$, then $\dot b+\dot b_{V_X} = 0$. Here
$V_X$ is the v1 coefficient that Lemma 2.3's reduction of $X$ removes at the root $-1$. The s1 statement is as at $b_0$.

(c) III.I$''''''''''''$ Lemma 2.4 holds at $b$, with its (2.4) read as
$$\chi_K\sum_iy_ip_i = \chi_K\Big(\sum_{\rho\ne\mathrm v1}T_{\rho,b}(a_\rho)+T_{\mathrm v1,b}(a_{\mathrm v1})
+h^{\le1}_{b,\mathrm s1}(a_{\mathrm s})+\dot g_b(a_{\mathrm b})\Big)+w''.$$
The exponents are as there; those of $a_{\mathrm v1}$ lie in $\bigcup_iE_i+\mathbb N_0-1$, and those of $a_{\mathrm b}$
have real part $\ge\beta-1$. The constants are uniform on $\bar{\mathcal B}_*$, and no map $V\mapsto h_{b,\mathrm
v1}(V)$ is inverted.

*Proof.* (a) and (b). Run III.I$''''''''''''$ Lemma 2.3's reduction at $b$, with the states at $b$ ((P3)). At the v1
root $-1$, subtract $\kappa_b(V)$, whose leading coefficient is $\bar h_{\mathrm v1}(V)$, independent of $b$ ((P3)). By
(2.6) this adds $L_1\dot g_b(\dot b_V)$ to the right side. So the reduced section $X_1\in\mathcal A^1$ satisfies $L_0X_1
= L_1\dot g_b(\dot b+\dot b_{V_X})+L_1\breve h^1(S+S')+L_2h(S+S')$. III.H (2.2) and Proposition 3.2 at $b$ ((P4)),
applied as in III.I$''''''''''''$'s proof of (b), give $\dot b+\dot b_{V_X} = 0$ and $S' = -S$. This is (b). For (a),
$p$ is (b) with $\dot b = 0$ and $S = 0$, so $\dot b_V = 0$. The rest is as at $b_0$, the nullspace of III.F$'''$
Proposition 4.1 at $b$ being spanned by $\dot g_b$ and $h_b$ (Lemma 1.2's remark).

(c) The removal of pairs proceeds as at $b_0$. By (a), the coefficient section of the first pair $(z_0,k_0)$ is
$$P = \sum_\rho\breve h^{(\mu_\rho),0}_{b,\tau_\rho}(Y_\rho)+\kappa_b(V)+\dot g_b(\dot b)+h(S),
\qquad V\in\mathcal V^0_b.$$
Two steps change. Write $a := \chi_+t_*^{-z_0}(\log t_*)^{k_0}$, and let $\tilde a$ be its antiderivative.

*The v1 part of $P$.* Subtract $T_{\mathrm v1,b}(\tilde aV)$. Its bottom $\tilde ah_{b,\mathrm v1}(V)$ vanishes, as
$V\in\mathcal V^0_b = \ker h_{b,\mathrm v1}$, and its next term is $a\kappa_b(V)$. It is a tower, so $L_b$ of it
involves $a''$ and higher only, and has $K^+$-order $\mathrm{Re}\,z_0+2\ge\beta$. Its coefficient $\tilde aV$ enters
$a_{\mathrm v1}$ at the exponent $z_0-1$, and $a_{\mathrm s}$ is unchanged, which is why the exponents are as there
(verifier 150's M1).

*The $\dot g$ part of $P$.* If $\mathrm{Re}\,z_0+1\ge\beta$, subtract $\dot g_b(a\dot b)$ as at $b_0$. Otherwise the
next coefficient gives $L_0P_1 = z_0L_1P$, and with the tower relations $L_0X = z_0L_1\dot g_b(\dot b)$ for a section
$X\in\mathcal G$. By (b), $z_0\dot b = -\dot b_{V_X}$. Put $V'' := -V_X/z_0$, so that $\dot b_{V''} = \dot b$. Subtract
$T_{\mathrm v1,b}(aV'')$ instead of $\dot g_b(a\dot b)$. Its bottom is $ah_{b,\mathrm v1}(V'') = a\dot g_b(\dot b_{V''})
= a\dot g_b(\dot b)$, as required. $L_b$ of it involves $a''$ and higher. Its next term, $a'\kappa_b(V'')$, carries the
v1 content $V_X$ that the next pair's reduction would remove; that content is therefore removed here, at the earlier
pair.

The new terms are again compatible: a companion $a^{(j)}\breve h^j$ has the exponent $z+j$ and degree $\mu-j$, as at
$b_0$. $|V''|\le C|V_X|$ with $C$ depending only on $|z_0|^{-1}$ and $\mathrm{Re}\,z_0\ge\beta-2>1$. The coefficients
are read off leading coefficients, which are independent of $b$ ((P3)) or, for $\dot g_b$, smooth in $b$, so the bounds
are uniform on $\bar{\mathcal B}_*$. $\square$

**Corollary 2.10 (III.I$''''''''''''$ Theorem 3.1 at $b$).** III.I$''''''''''''$ Theorem 3.1 holds at $b\in\bar{\mathcal
B}_*$, uniformly. Two changes are needed:

- Its Step 2 uses Lemma 2.9 (c) for III.I$''''''''''''$ Lemma 2.4, so the v1 coefficients and the early $\dot g$ terms
enter through rotation rows $T_{\mathrm v1,b}$.

- The conormal towers $C$ of its Step 1 (viii) include $T_{\mathrm v1,b}(Y^c_{\mathrm v1})$. At $b$ the level-3 conormal
rotation tower has $K^+$-rate $\alpha_\tau+2\in[3+\eta_2-2\epsilon,4)$, below $\alpha$, since its bottom $h_{b,\mathrm
v1}$ no longer vanishes. III.I$''''''''''''''$ Definition 1.1 admits this coefficient ($w_{\mathrm v1} =
3+\eta_2-2\epsilon$), and $L_b$ of it has $K^+$-order $\alpha_\tau+5>\alpha$ (verifier 147's m2).

*Proof.* Step 1 is unchanged at $b$: its pieces are those of (P2)-(P4). Step 2 is the assembly, with Lemma 2.9 (c) in
place of III.I$''''''''''''$ Lemma 2.4. $\square$

### 2.8 The parameter columns at $b$: III.I$'''''''$ Lemma 2.4 and the base level

III.I$'''''''$ Lemma 2.4 is exact at the base point $(0,0)$ only. At $(0,\vec p_b)$, $\vec p_b := (0,b-b_0,0)$, the
background is $G = g_{b_0,b,0} = (1-\chi_K)g_{b_0}+\chi_Kg_b$ (III.I$'''''''$ (1.3)), and the corrections #1-#2 and
their counterterms, among them $h^{(0)}(\dot b) = -d\chi_K\otimes_s\dot\omega_{b_0}(\dot b)$, are built at $b_0$ ((P6)).
So each parameter identity acquires an error, as the boost identity does (section 2.6). III.I$'''''''$ Lemmas 4.3, 4.5
and Corollary 4.6, and III.I$''''''''$ Proposition 4.1's base step, invert their maps by continuity from $(0,0)$; at $b$
they are proved by a direct bound (verifier 146's M1, D330).

**Lemma 2.11 (III.I$'''''''$ Lemma 2.4 at $b$).** Let $b\in\bar{\mathcal B}_*$, $\vec p_b := (0,b-b_0,0)$, and
$L_{0,\vec p_b} := D_hP_2(0,\vec p_b)$. For $\dot S,\dot S^{(0)}\in\mathcal S_1$ and $\dot b\in\mathfrak b$,
$$D_{\vec p}P_2(0,\vec p_b)(\dot S,\dot b,\dot S^{(0)}) = L_{0,\vec p_b}\Big(\chi_K\big(h^{\le1}_{b,\natural}(\dot S)
+\dot g_b(\dot b)+h_b(\dot S^{(0)})\big)\Big)+E^{\mathrm{mot}}_b(\dot S,\dot b,\dot S^{(0)}),\tag{2.7}$$
where $E^{\mathrm{mot}}_b$ is linear, supported in $\mathcal C$, vanishes at $b = b_0$, and, near $(\iota^+)^\circ$,
lies in $\mathcal A^{\mathcal G+2-\delta}$ for every $\delta>0$ ($\mathcal G$ of Lemma 2.7), with seminorms
$O(|b-b_0||(\dot S,\dot b,\dot S^{(0)})|)$ uniformly on $\bar{\mathcal B}_*$. So $E^{\mathrm{mot}}_b$ lies in
III.I$'''''''$'s source class $\mathcal Y$ with norm $O(|b-b_0|)$. The tensors $\chi_Kh^{\le1}_{b,\natural}(\dot S)$,
$\chi_K\dot g_b(\dot b)$ and $\chi_Kh_b(\dot S^{(0)})$ vanish for $t^\flat_*<10$; the first has the form of III.I$''''$
(4.1) with boost parameter $\dot S$ and $\tilde u = 0$, and the sum of the other two the form of III.I$''''''$ (2.1) at
$b$ with parameters $(\dot b,\dot S^{(0)})$ and $\tilde u = 0$ ((P3)).

*Proof.* *Support.* By III.I$'''''''$ (1.3) and Definition 1.2, in the interior of $\chi_K^{-1}(0)$ the background $g_0$
is a translate of $g_{b_0}$ and does not depend on $b$, and in the interior of $\chi_K^{-1}(1)$ it is $g_b$ and does not
depend on $S$ or $S^{(0)}_1$. The corrections #1-#2 and their counterterms are supported in $\mathcal C$ (III.I$''''$
Lemma 2.2, III.I$'''''''$ Lemma 2.2). So on the first set $g' = g_0$ is Ricci flat and $\Upsilon^{E_\Upsilon}(g_0,g_0) =
0$ for every $\vec p$ near $\vec p_b$, and on the second $g' = g_0 = g_{b'}$ with $b'$ the parameter of $\vec p$, again
Ricci flat with $\Upsilon^{E_\Upsilon}(g_0,g_0) = 0$. Hence $P_2(0,\vec p) = 0$ on both sets for every $\vec p$ near
$\vec p_b$, and $D_{\vec p}P_2(0,\vec p_b) = 0$ there. The first term on the right of (2.7) vanishes on both sets too:
trivially on the first, and on the second it is $L_b$ of $h^{\le1}_{b,\natural}$, $\dot g_b$, $h_b$, which lie in $\ker
L_b$ (Lemma 2.7's proof for the first; the others span the nullspace of $\widehat{L_b}(0)$ and are stationary, Lemma
1.2's remark). So $E^{\mathrm{mot}}_b$ is supported in $\mathcal C$. *At $b_0$.* $\vec p_{b_0} = 0$, $L_{0,0} =
L_{b_0}$, and the states at $b_0$ are those of III.I$'''''''$ Lemma 2.4, so $E^{\mathrm{mot}}_{b_0} = 0$ is
III.I$'''''''$ (2.3). *Size.* As in Lemma 2.7's proof. Every term of $E^{\mathrm{mot}}_b$ is linear in the direction and
a smooth function of $b$ on $\mathcal C$. Its ingredients are $G-g_{b_0} =
\chi_K(g_b-g_{b_0})\in|b-b_0|\rho_+^2C^\infty$ near $(\iota^+)^\circ$; the states $h^{\le1}_{b,\natural}$, $\dot g_b$
and $h_b$, smooth in $b$ in $\mathcal A^{\mathcal G-\delta}$ there ((P3), with III.H Remark 2.6's loss, (P4); on
$\mathcal C$, $|x|\ge t/10$, and the stationary states are $O(|x|^{-2})$ with all Cartesian derivatives); the
corrections and counterterms built at $b_0$; and the values at $\vec p_b$ of $g'-g_0$ and of
$\Upsilon^{E_\Upsilon}(g',g_0)-\vartheta_{\mathrm{tot}}$, which are $O(|b-b_0|)$ and supported in $\mathcal C$, the
corrections #2 being linear in $b-b_0$. III.I$''''$ Lemma 2.2's count, that $D_{g_0}\mathrm{Ric}$ and $\delta^*\delta G$
lie in $\rho_+^2\mathrm{Diff}^2_{\mathrm b}$ near $(\iota^+)^\circ$, takes $\mathcal A^{\mathcal G-\delta}$ into
$\mathcal A^{\mathcal G+2-\delta}$, uniformly for $b\in\bar{\mathcal B}_*$. So $\partial_bE^{\mathrm{mot}}_b$ is bounded
there by $C$ times the size of the direction, and the mean value theorem along the segment from $b_0$ to $b$ gives the
bound. $\square$

The $\dot S$-part of $E^{\mathrm{mot}}_b$ is the analogue for $P_2$ of Lemma 2.7's $E^S_b$; it differs from it by the
$S$-derivative of the corrections #2 at $\vec p_b$, which has the same properties.

**Proposition 2.12 (III.I$'''''''$ Lemmas 4.3, 4.5 and Corollary 4.6 at $b$).** Let $(h,\vec p)$ be as in III.I$'''''''$
Lemma 2.5, with parameter $b\in\bar{\mathcal B}_*$, and write $\|h\|$ for the norm in which that lemma takes $h$ small.
Let $S^{(-1)}_{h,\vec p} := \dot S_{h,\vec p}\circ f^S_{h,\vec p}$ be the boost map of III.I$'''''''$ Lemma 4.3's proof,
and $M_{h,\vec p} := \dot{\vec p}^{,=0}_{h,\vec p}(0,\cdot)$ the map of its Lemma 4.5. There are $C$ and a smallness of
$(h,\vec p-\vec p_b)$, uniform on $\bar{\mathcal B}_*$, with
$$|S^{(-1)}_{h,\vec p}-\mathrm{id}|+|M_{h,\vec p}+\mathrm{id}|\le C\big(\|h\|+|\vec p-\vec p_b|+|b-b_0|\big).\tag{2.8}$$
So, after shrinking $\mathcal B_*$ and the smallness of $(h,\vec p-\vec p_b)$, both maps are invertible with inverses of
norm at most 2, and III.I$'''''''$ Lemmas 4.3, 4.5 and Corollary 4.6 hold at $b$, with constants uniform in $b$; Lemma
4.3's last claim holds with $o(1)$ replaced by $O(\|h\|+|\vec p-\vec p_b|+|b-b_0|)$. The same bound gives
III.I$''''''''$ Proposition 4.1's base step at $b$, and the bounds on $(S^{(-1)}_{h,\vec p})^{-1}$ that III.J$''$ Lemma
2.1 (c) takes (PART-III-J3-TAME.md:124-127).

*Proof.* At $b$ the maps are built as in III.I$'''''''$ Lemmas 4.3-4.5, from $\dot S_{h,\vec p}$ (III.I$''''$
Proposition 4.1 (1) for $L_{h,\vec p}$) and $Q_{h,\vec p}$ (III.I$''''''$ Proposition 2.1 for $L_{h,\vec p}$, with the
states at $b$), which are bounded on $\mathcal Y$ uniformly in $b$ ((P1), (P4), III.I$'''''''$ Lemma 2.5 (c)). Write
$f^\bullet_{h,\vec p}$ for $D_{\vec p}P_2(h,\vec p)$ in the direction $\bullet$, and $f^{=0}_{h,\vec p}(b',S'') :=
f^b_{h,\vec p}(b')+f^{\mathrm s1}_{h,\vec p}(S'')$. *Two bounds at fixed $b$.* (1) $\|f^\bullet_{h,\vec
p}-f^\bullet_{0,\vec p_b}\|_{\mathcal Y}\le C(\|h\|+|\vec p-\vec p_b|)$ per unit direction. $f^\bullet$ is smooth in
$(h,\vec p)$, and III.I$'''''''$ Lemma 3.1's bounds, which hold at $b$ (Theorem 3.1's bullet for III.I$'''''''$, which
the reading supplies independently of this proposition; verifier 150's n8), apply to its derivative in $(h,\vec p)$ (its
(3.1) for $h$, the count of III.I$''''$ (3.4) for $\vec p$; verifier 150's n3), whose terms are again polynomial in the
differences of the metrics with coefficients smooth in their inverses; the mean value theorem along the segment from
$(0,\vec p_b)$ gives the bound. (2) For $F\in\mathcal Y$, $|\dot S_{h,\vec p}(F)-\dot S_{0,\vec p_b}(F)|\le
C(\|h\|+|\vec p-\vec p_b|)\|F\|_{\mathcal Y}$. And for $F_1,F_2\in\mathcal Y$ with $\dot S_{h,\vec p}(F_1) = 0 = \dot
S_{0,\vec p_b}(F_2)$, where alone $Q_{h,\vec p}$ and $Q_{0,\vec p_b}$ are defined (PART-III-I8-UNPARAM.md:332-335),
$|Q_{h,\vec p}(F_1)-Q_{0,\vec p_b}(F_2)|\le C\|F_1-F_2\|_{\mathcal Y}+C(\|h\|+|\vec p-\vec p_b|)\|F_1\|_{\mathcal Y}$
(verifier 150's m1). This is III.I$'''''''$ Lemma 4.1 (b)'s comparison made quantitative
(PART-III-I8-UNPARAM.md:368-376), with $L_{0,\vec p_b}$ in place of $L_{b_0}$. Let $u_1$, $u_2$ be the forward solutions
of $L_{h,\vec p}u_1 = F_1$ and $L_{0,\vec p_b}u_2 = F_2$. Then $L_{0,\vec p_b}(u_1-u_2) = R := F_1-F_2-(L_{h,\vec
p}-L_{0,\vec p_b})u_1$, and $\|(L_{h,\vec p}-L_{0,\vec p_b})u_1\|_{\mathcal Y}\le C(\|h\|+|\vec p-\vec p_b|)\|F_1\|$:
both backgrounds equal $g_b$ near $K^+$ (III.I Lemma 3.6), so the difference gains $a_K$ there, and at $\iota^+$ it
gains as in Lemma 4.1's proof. With $F_1 = F_2 = F$, the boost terms of $u_1$ and $u_2$ are built from the same state at
$b$, so the difference of the boost parameters is $\dot S_{0,\vec p_b}(R)$. Under the condition, $u_1-u_2$ has no boost
term, so $\dot S_{0,\vec p_b}(R) = 0$, and $Q_{h,\vec p}(F_1)-Q_{0,\vec p_b}(F_2) = Q_{0,\vec p_b}(R)$ by the uniqueness
of Lemma 4.1's proof at $b$, which uses the injectivity of $(\dot b,\dot S)\mapsto\dot g_b(\dot b)+h_b(\dot S)$ (Lemma
1.2's remark). *The boost map.* By (2.7), $\chi_Kh^{\le1}_{b,\natural}(S')$ is the forward solution of $L_{0,\vec p_b}u
= f^S_{0,\vec p_b}(S')-E^{\mathrm{mot}}_b(S',0,0)$, so $\dot S_{0,\vec p_b}(f^S_{0,\vec p_b}(S')) = S'+\dot S_{0,\vec
p_b}(E^{\mathrm{mot}}_b(S',0,0))$. Hence
$$S^{(-1)}_{h,\vec p}(S')-S' = \dot S_{h,\vec p}\big(f^S_{h,\vec p}(S')-f^S_{0,\vec p_b}(S')\big)
+\big(\dot S_{h,\vec p}-\dot S_{0,\vec p_b}\big)\big(f^S_{0,\vec p_b}(S')\big)
+\dot S_{0,\vec p_b}\big(E^{\mathrm{mot}}_b(S',0,0)\big),$$
and by (1), (2) and Lemma 2.11 the three terms are at most $C(\|h\|+|\vec p-\vec p_b|+|b-b_0|)|S'|$. *Lemma 4.5's map.*
At $(0,\vec p_b)$, Lemma 4.3's formula gives $S'_0 := \vec p\,'^{,<0}_{0,\vec p_b}(0,\vec p\,'^{,=0}) =
-(S^{(-1)}_{0,\vec p_b})^{-1}\dot S_{0,\vec p_b}(f^{=0}_{0,\vec p_b}(b',S''))$. By (2.7), $\chi_K(\dot
g_b(b')+h_b(S''))$ is the forward solution of $L_{0,\vec p_b}u = f^{=0}_{0,\vec
p_b}(b',S'')-E^{\mathrm{mot}}_b(0,b',S'')$; it has $K^+$-weight $-\epsilon>-1$, so no boost term, and $Q_{0,\vec p_b}$
of it is $(b',S'')$. So $|S'_0|\le C|b-b_0||\vec p\,'^{,=0}|$, and
$$M_{0,\vec p_b}(\vec p\,'^{,=0}) = -\vec p\,'^{,=0}
-Q_{0,\vec p_b}\big(E^{\mathrm{mot}}_b(0,b',S'')+f^S_{0,\vec p_b}(S'_0)\big),$$
whence $|M_{0,\vec p_b}+\mathrm{id}|\le C|b-b_0|$. For $(h,\vec p)$ near $(0,\vec p_b)$, $M_{h,\vec p}(\vec p\,'^{,=0})
= Q_{h,\vec p}(F_{h,\vec p})$, with $F_{h,\vec p}$ the source of III.I$'''''''$ Lemma 4.5's proof and $\dot S_{h,\vec
p}(F_{h,\vec p}) = 0$ by Lemma 4.3, and likewise at $(0,\vec p_b)$. So (2), for the pair $(F_{h,\vec p},F_{0,\vec
p_b})$, bounds $M_{h,\vec p}-M_{0,\vec p_b}$ by $C\|F_{h,\vec p}-F_{0,\vec p_b}\|_{\mathcal Y}+C(\|h\|+|\vec p-\vec
p_b|)$ per unit $\vec p\,'^{,=0}$; and (1) bounds $\|F_{h,\vec p}-F_{0,\vec p_b}\|_{\mathcal Y}$, with $\vec
p\,'^{,<0}_{h,\vec p}-\vec p\,'^{,<0}_{0,\vec p_b}$ bounded the same way through Lemma 4.3's formula and the bound on
the boost map. This proves (2.8), and the Neumann series gives the inverses. III.I$'''''''$ Corollary 4.6's proof and
III.I$''''''''$ Proposition 4.1's base step use, beyond III.I$'''''''$ Lemma 2.5 (c), only these inverses and their
bounds. $\square$

III.I$'''''''$ Lemma 4.1 and III.I$''''''''$ Proposition 4.1 (ii), continuity statements at the reference point, are
used at $b$ at fixed $b$ only, with $L_{0,\vec p_b}$ as the reference, as Lemma 2.4 uses the later parts' (verifier
146's m2).

## 3. The parts at $b$

**Theorem 3.1 (the linear theory at base points near $b_0$).** For base points with black hole parameter
$b\in\bar{\mathcal B}_*$, the statements at $b$ of the following hold, with constants and smallness conditions uniform
in $b$:

- III.I$'$-III.I$''''''$ (the parts below level 3; the backgrounds $g_0 := g_{b_0,b_0,-S}$ of III.I$''$ section 1 and
$g_S$ of III.I$''''$ (1.1) become $g_{b_0,b,-S}$, and the correction #1 stays the tensor built at $b_0$, (P6); verifier
146's n2), with III.I$''''$ Proposition 4.1 (2), Corollary 4.3 and III.I$'''''$ Corollary 2.2 in the form of Proposition
2.8 (D329; verifier 145's M1, m1);

- III.I$'''''''$ Lemmas 1.3, 2.2, 2.4, 2.5, 3.1, 4.1, 4.3, 4.5, Definition 4.4 and Corollary 4.6: Lemma 2.2 being
independent of $b$, Lemma 3.1 with $\vec p = (S,b-b_0,S^{(0)}_1)$ (its proof transfers, $g_b$ being Ricci flat for every
$b$ and $\dot g_b$ given by (P3)), Lemma 2.4 in the form of Lemma 2.11, Lemma 4.1 at fixed $b$ only, and Lemmas 4.3, 4.5
and Corollary 4.6 in the form of Proposition 2.12 (verifier 146's M1, m1, m2);

- III.I$''''''''$ Proposition 4.1 and its lemmas, in the form of Proposition 2.5's direct bound, with the base step by
Proposition 2.12, Lemma 2.4 in the form (1.1), its rows being rows of III.I$'''''''''$'s $\mathcal N$, and Proposition
4.1 (ii) and Lemma 3.3 at fixed $b$ only (verifier 146's M1, m2, n4);

- III.I$'''''''''$ section 2, with Lemmas 2.4 and 2.6 (c) ($r_{0,0} = 0$) in the form (1.1) (verifier 146's m2);

- III.I$''''''''''$ Definitions 1.1, 1.3, Lemmas 1.2, 2.1 (c) and Proposition 3.1 (verifier 147's n1);

- III.I$'''''''''''$ Proposition 3.1, Lemmas 3.2-3.3 (at fixed $b$, Lemma 2.4's proof), and Theorem 4.1 only inside
Lemma 2.4 and Proposition 2.5: at a rotating $b$ its parameter space lacks the rotation rows, and Proposition 2.5 with
$q = 0$ is its form there (verifier 131's m2);

- III.I$''''''''''''$ Lemmas 2.3-2.4 and Theorem 3.1, in the forms of Lemma 2.9 and Corollary 2.10 (verifier 147's M1,
m2);

- III.I$'''''''''''''$ Proposition 2.1, Lemmas 2.2-2.3 in the form of Lemma 2.4, and Proposition 2.4 only inside
Proposition 2.5, as for III.I$'''''''''''$ Theorem 4.1;

- III.I$''''''''''''''$ Definition 1.2 with (1.4), Lemmas 2.2-2.5, Remark 3.2 (2), and Theorem 3.1 in the form of
Proposition 2.5 (unique among the $\vec p\,'$ with the assigned rotation coordinates; verifier 148's n2);

- III.J Lemmas 2.1-2.2, Theorem 2.4 and Remark 2.5, as written, with its rows built at $b_0$ ((viii); verifier 148's
m1);

- III.J$'$ Lemma 1.1, for Proposition 2.5's output, and Theorem 2.1 (verifier 148's m2);

- III.J$''$ Theorems 4.1-4.2, Proposition 4.3;

- III.J$'''$ Propositions 3.4, 4.3, 4.6, 5.2, 5.4, Theorems 5.3, 5.5 and Corollary 6.6, Theorem 5.3 in the form of
Proposition 2.5 at exact weights (verifier 149's m2).

*Proof.* The census is a reading, not a search. Every line of these parts was read by an independent reader, five in all
(verifiers 145-149), and every step whose justification uses a property of the base point that a general
$b\in\bar{\mathcal B}_*$ need not have, or an object built at $b_0$, is a row of BASEPOINT-LEDGER.md, with what supplies
it at $b$ and whether that supply is uniform in $b$. Implicit uses count, the symmetries of $b_0$ among them (static,
spherical, isotypic, Killing, $SO(4)$). Each supply is one of (P1)-(P6), Lemma 1.2 or section 2, and the rows group into
the uses (i)-(xi) below. The uses that nothing supplied were the major gaps (I$'''''''''''''''$6)-(I$'''''''''''''''$8),
a minor one, the reality of the objects at $b$ (verifier 148's m3, now in (P3) and Definition 2.3), and an unstated
theorem, III.J$'''$ Theorem 5.3 at $b$; each is now supplied, by sections 2.6-2.8 and the list above.

(i) The forward solutions: III.I$'$-III.I$''''''''''''''$ solve with $L^{g,g_0}$ at the base point through III.I Theorem
5.3 and its corollaries (P1). The splitting $L_{h,\vec p} = L_{b_0}+(L_{h,\vec p}-L_{b_0})$ near $K^+$, used to move a
perturbation into the source (III.I$''''''''$-III.I$''''''''''''$, for instance III.I$''''''''''''$ Step 0), becomes
$L_{h,\vec p} = L_b+(L_{h,\vec p}-L_b)$. This has the same $K^+$-gain, $g_0 = g_b$ near $K^+$ (III.I Lemma 3.6).
III.I$''''$'s class statement $k_S := g_S-g_{b_0}\in\mathcal K$ reads $k_S := g_{b_0,b,-S}-g_b\in\mathcal K$ at $b$,
with differences taken from $g_b$; $k' := \partial_Sk_S$ is unchanged and vanishes near $K^+$. At $b$, $L_{h,S} :=
D_hP_1(\cdot,S,b)$, and $P_1(0,0,b)\ne0$ in $\mathcal C$; the linear theory uses only $D_hP_1$ and $D_SP_1$ (verifier
145's m2, n5).

(ii) The model at $\iota^+$ and at tf: III.G-III.G$''''$ through (P2), (P4).

(iii) The states, towers and index sets: III.I$''''$, III.I$'''''''$, III.I$''''''''$, III.I$'''''''''$ use the index
sets of III.D$''$, III.D$'''$ and III.F$'''$ "at $b_0$". They are independent of $b$ (P3), so the index sets $\mathcal
E_{\mathrm{ind}}$, $\mathcal E_\sharp$, $\mathcal E_+$ of these parts serve at every $b$, and so does $\mathcal
E^\natural$ (III.I$'''''''''''''$ Definition 1.2), built from $\mathcal E_\sharp$ and $\mathcal E_{\mathrm{ind}}$
(verifier 148's n7). The collision set $\mathcal E_{\mathrm{col}}$ (PART-III-I11-SPACETIME.md:71,
PART-III-I12-SPECTRAL.md:73-106, 555-560), which generates $\Lambda$ and through it $\mathcal E_{\mathrm{par}}$,
$\mathcal N$, $\mathcal E_\sharp$, $\mathcal E^\natural$, (G) and admissibility, is read at every $b$ as the
$b$-independent set $((\{(2,0),(3,0)\}\cup(2+\mathcal E_{\mathrm{ind}})\cup(3+\mathcal E_{\mathrm{ind}}))+\mathbb
N_0)\cap\{\mathrm{Re}\ge0\}$, which contains the exponents it collects at $b$, by (P3)'s index sets, the smooth
coefficients of the $L_k$ (III.I$'''$ Lemma 1.1 at $b$) and the boundedness of $F$ (III.H Lemma 2.4 (a), (P4); verifier
147's m1).

(iv) The derivatives in $b$, taken at $b_0$ in III.I$'''''''$ Corollary 4.6 and III.I$''''''''''''''$ Lemma 2.4 (c): at
$b$, the $b$-column $\dot g_b$ (P3). So does $\dot g = \partial_bg_b$ in III.I$''$-III.I$'''''$, which enters through
III.H's columns and singular part ((P3), (P4); verifier 145's n1). III.I$''''''''''''''$ Lemma 2.4 (c)'s proof is
written for every $b$ near $b_0$; it uses that every coefficient of $q$ has rate $>2$ at every such $b$. The point of
III.I$''''''''''''''$ Theorem 3.1's Step 1 that uses $\widehat{L_{b_0}}(0)\partial_bh_{b,\mathrm v1} = 0$ needs only
that the $q$-terms have $K^+$-order above $\alpha_1$. At $b$, $\widehat{L_b}(0)\partial_bh_{b,\mathrm v1} =
-(\partial_b\widehat{L_b}(0))h_{b,\mathrm v1}$ need not vanish, but $q$'s v1 coefficients have rate
$>2+\epsilon_K>\alpha_1$ (Definition 1.1, (G)), so the $K^+$-order of $L(\partial_bh_{b,\mathrm{rem}}(q)b')$ is still
$>2+\epsilon_K>\alpha_1$.

(v) The joint injectivity: III.I$''''''''''$ Lemma 2.2 and Corollary 2.3 at $b$ by Lemma 1.2, III.I$''''''''''''''$ Step
4$'$ is not used at $b$, Proposition 2.5 replacing it. The injectivity of $S\mapsto h(S)$ (III.F$'''$ Proposition 4.1
(1), proved at $b_0$ by symmetry), used at PART-III-I4-BOOST.md:128, PART-III-I5-UNBOOST.md:343 and
PART-III-I6-ALMOSTBDD.md:211, holds at $b$ by Lemma 1.2, the s1 states alone (verifier 145's m3).

(vi) The v1 terms: III.I$'''''''''$ section 1 ($\mathcal W_{\mathrm v1} = \mathcal V' = 0$, kept at every $b$),
III.I$''''''''''$ Lemma 2.1 and Proposition 3.1, III.I$'''''''''''$ Lemma 2.3, III.I$''''''''''''$ section 1, Lemmas
2.3-2.4 and Theorem 3.1, and III.I$''''''''''''''$ Definitions 1.1, 1.3, Steps 2-3 and 4$'$. These are section 2:
Proposition 2.2, Lemma 2.4, Proposition 2.5, Lemma 2.9 and Corollary 2.10 (verifier 147's M1, m2). At a rotating $b$,
the rate of a v1 coefficient at $z$ (PART-III-I15-AUGMENT5.md:64, 233; PART-III-J-PARAM.md:234) is at least
$\mathrm{Re}\,z$, and $\mathrm{Re}\,z+1$ on $\ker h_{b,\mathrm v1}$, the rotations commuting with the spin; only the
lower bound is used (verifier 148's n4). The $a_{\mathrm v1}$ term of III.I$'''''$ (PART-III-I6-ALMOSTBDD.md:146-151) is
covered by Lemma 2.1 (verifier 145's n2).

(vii) The time translation as a Killing field: (P5).

(viii) III.J-III.J$'''$: their base points $U$ map by $\Phi$ to $(h,\vec p,q)$ with parameter $b$ (III.J Theorem 2.4),
and their proofs use III.I$''''''''''''''$ Theorem 3.1 and the maps of III.J at that base point, by (i)-(vii).
III.J$''$'s tame calculus (section 1, Lemmas 2.1-2.4) has constants that depend on the base point through finitely many
seminorms, continuous in $b$; III.J$'''$'s exact classes and conditions (E1)-(E5) do not involve $b$ ((P2)-(P3): the
exponents, roots and index sets are those at $b_0$). III.J$''$ Theorem 4.1's solution maps of III.I-III.I$'''''''''''''$
are read at $b$ as in Lemma 2.4 and Proposition 2.5. The new objects enter III.J$''$ Lemma 2.1 (c)'s inventory (verifier
131's m3): $A_b$ is bounded by a fixed low seminorm of $G$, as it reads the $\iota^+$-data $u_+$ and the tf-data
(Proposition 2.2); $E^\nu$ is bounded by $C|b-b_0||W|$ in a fixed seminorm ((P6)); the rotation rows enter
$-\mathrm{id}+A_k$ as the other rows do; and $d_*$ includes their orders.

In III.J$''$, Lemma 2.1 (f), the loss at every order, holds at $b$ by III.H$''$ Proposition 1.1, uniformly on
$\bar{\mathcal B}_1$; this supersedes (J$''$2)'s neighbourhood shrinking with $k$. III.J$''$ Lemma 2.3's continuity is
read at $b$ through Lemma 2.4 at $(0,\vec p_b)$ and Proposition 2.5's direct bound, both in fixed seminorms, so $d_*$ is
unchanged; and III.J$''$ Theorem 4.1 at $b$ takes $\delta_0$ at most the radius of $\mathcal B_*$ as shrunk below
(verifier 149's m1, n1, n5). III.J$'''$ Theorem 5.3 at $b$ is Proposition 2.5 at the exact weights: $E^\nu$ is exact
there, having $K^+$-weight $\kappa_\nu-\epsilon>\alpha$ and $\iota^+$-exponents in $\mathcal E^\natural+2$, which
III.J$'''$ (E1) covers (III.I$'''''''''''''$ Lemma 1.3 (a)); $A_b$ does not depend on the loss, being computed from
$\iota^+$- and tf-data (Remark 2.6); and the errors of the rotation rows' identification have $K^+$-order
$\mathrm{Re}\,\lambda_0+1-\epsilon>\alpha-2$, with room. III.I$''''''''''''''$ Step 4$'$, which III.J$'''$ cites
(PART-III-J4-EXACT.md:587-588), is not used at $b$, Proposition 2.5 replacing it, and Propositions 3.4, 4.3 carry the
rotation rows of Proposition 2.2 (verifier 149's m2).

III.J builds its rows at $b_0$ (PART-III-J-PARAM.md:160, 268-271), and its Lemmas 2.1-2.2, Theorem 2.4 and Remark 2.5
hold as written at $b$, with rows $m^{b_0}_\nu$, towers $T_{\rho,b}$ and corrections at $b_0$: (P6)'s rule of rows at
$b$ is not applied there. $P_5$ and the coordinates $W_\nu$ do not depend on the convention, as rows enter $P_4$ only
through the corrections and counterterms built at $b_0$ (PART-III-I15-AUGMENT5.md:204-206), and III.J$'$'s Step 2 uses
only the rows' $\lambda_0$-terms, which do not depend on $b$ (PART-III-J-PARAM.md:187-190, 212-219). III.J$'$ composes
$\Phi$ with Proposition 2.5 independently of the convention, and III.J Remark 2.6's pure gauge refers to $g_{b_0}$
(verifier 148's m1). III.J$'$ Lemma 1.1, whose proof applies $\tilde L_{b_0}(0)^{-1}$ (PART-III-J2-LINEAR.md:44), holds
for Proposition 2.5's output: at $b$ its roots are those of (P2), III.H Proposition 3.2 holds by (P4), and neither
$A_b$, which reads only $\iota^+$-data and level-1 tf-data (Definition 2.3), nor $E^\nu$, a fixed tensor ((P6)), depends
on $\eta_2$ (verifier 148's m2).

(ix) The boost column: III.I$''''$ Lemma 2.4, Proposition 4.1 (2), Corollary 4.3 and III.I$'''''$ Corollary 2.2 at $b$
are Lemma 2.7 and Proposition 2.8 (verifier 145's M1, D329).

(x) The parameter columns: III.I$'''''''$ Lemma 2.4 at $b$ is Lemma 2.11, and its Lemmas 4.3, 4.5, Corollary 4.6 and
III.I$''''''''$ Proposition 4.1's base step are Proposition 2.12 (verifier 146's M1, D330).

(xi) The expansion: III.I$''''''''''''$ Lemmas 2.3-2.4 and Theorem 3.1 at $b$ are Lemma 2.9 and Corollary 2.10 (verifier
147's M1, m2, D330).

The constants: every constant above is a finite combination of constants of (P1)-(P4) and (P6), of Lemma 1.2, of Lemmas
2.1, 2.4, 2.7, 2.9 and 2.11, of Propositions 2.8 and 2.12, and of the maps of Proposition 2.2, each uniform on
$\bar{\mathcal B}_*$. The continuity statements (III.I$''''''''$ Proposition 4.1 (ii) and Lemma 3.3, III.I$'''''''''''$
Lemma 3.3, III.I$'''''''''''''$ Lemma 2.3) enter Lemma 2.4 at fixed $b$ only and are not used for the elimination's
bounds. III.I$''''$ Lemma 4.2 (b) and III.I$'''''''$ Lemma 4.1 are not used across $b$; the direct bounds of
Propositions 2.8 and 2.12 replace them (D329, D330). The smallness of the elimination, across $b$, comes from the direct
bound of Proposition 2.5's Step 3, through (P6) and Definition 2.3 (verifier 131's M1 and n2). $\mathcal B_*$ is shrunk,
beyond III.H$''$ (B5), so that Lemma 1.2's bound holds and the maps $-\mathrm{id}+A_k$ of Proposition 2.5 are invertible
on it (verifier 130's m3). $\square$

**Corollary 3.2 ((J$'$3) closed).** III.J$'$ Theorem 2.1 and its tame and exact forms (III.J$''$ Theorem 4.2, III.J$'''$
Corollary 6.6) hold at every base point $U\in\mathcal D^\infty$ small in $\mathcal D^d$, with black hole parameter
$b\in\mathcal B_*$, which smallness of $U$ in $\mathcal D^d$ ensures, with constants uniform in $U$; at a rotating $b$
the right inverse is the one constructed by Proposition 2.5. These are the right inverses that II.G Theorem 2.1 (iii)
asks for at every $u\in U$.

## 4. Findings, labels and sources

(I$'''''''''''''''$1) *The rotation rows are new rows at $b$.* At a rotating base point, the v1 terms of exponent of
real part at most 2 decay one order less at $K^+$ than at $b_0$, and they fall below the levels. They are new rows of
the levels at which their rates lie, with coefficients assigned from the construction (Definition 2.3): the graft's
$\iota^+$-data and the spectral pieces' tf-data. So the rotation coordinates are fixed level by level inside the
elimination (Proposition 2.5), not at the end as by III.I$''''''''''''''$ Step 4$'$. This is the source's
"$V'\approx\dot V$" (pp. 279-280). Verifier 130's M1 found that D297's text had left them to the end.

(I$'''''''''''''''$2) *v1 is not separable at $b$.* $h_{b,\mathrm v1}(V)$ is a combination of $\dot g_b$ and $h_b(S)$
with coefficients $O(|b-b_0||V|)$ (Lemma 1.2's remark). So a $K^+$-reading of v1 degenerates as $b\to b_0$, and the
coefficients are assigned.

(I$'''''''''''''''$3) *Corrections at $b_0$, rows at $b$.* As in the source, the corrections #1-#4 and their
counterterms are built at $b_0$, while the rows and towers are built at the base point's $b$ ((P6), (1.1)). The mismatch
$E^\nu$ is the $b$-difference of the corrections and counterterms: supported in $\mathrm{supp}\,\chi_K$, of $K^+$-weight
$\kappa_\nu-\epsilon>\alpha$, and $O(|b-b_0|)$. Its $\iota^+$-exponents lie in $\mathcal E^\natural+2$, so
$E^\nu\in\mathcal Y^\natural_2(\alpha-)\cap\mathcal Y(\alpha_1)$. Settled in D302 (verifier 131's section B); verifier
130's m2 had left it open.

(I$'''''''''''''''$4) *Uniqueness at $b$ only with the assigned coordinates* (Remark 2.6).

(I$'''''''''''''''$5) *The census.* Theorem 3.1 first rested on a search of the parts for the uses of $b_0$ and of its
symmetries, and a use the search did not see would have been a gap, for instance an argument at $b_0$ that does not name
it. The search is replaced by a reading, BASEPOINT-LEDGER.md: five independent readers (verifiers 145-149) read every
line of the parts and recorded every use of the base point with its supply at $b$. The reading found three major gaps
that the search had missed, (I$'''''''''''''''$6)-(I$'''''''''''''''$8), a minor one, the reality of the objects at $b$,
and one theorem used at $b$ but not stated there, III.J$'''$ Theorem 5.3; all are repaired in sections 2.6-2.8 and in
Theorem 3.1's list (D329-D330).

(I$'''''''''''''''$6) *The boost identity holds at $b_0$ only.* III.I$''''$ Lemma 2.4 uses that $g_{b_0}$ is Ricci flat
in $\mathcal C$ and that correction and leading term are the same $b_0$-state. At $b$ the identity carries the error
$E^S_b$ of Lemma 2.7, $O(|b-b_0|)$ and supported in $\mathcal C$, and III.I$''''$ Proposition 4.1 (2) holds at $b$ by
Proposition 2.8's direct bound. The token search behind Theorem 3.1 did not see it: the identity names $b_0$ through
$g_{b_0}$, but its use at $b$ named nothing. Found by the first batch of the base-point ledger (verifier 145, D329).

(I$'''''''''''''''$7) *The parameter identities hold at $b_0$ only.* III.I$'''''''$ Lemma 2.4 is exact at $(0,0)$. At
$(0,\vec p_b)$ the background mixes $g_{b_0}$ and $g_b$ in $\mathcal C$ and the corrections #2 are built at $b_0$, so
each identity carries an error, Lemma 2.11's $E^{\mathrm{mot}}_b$. The base level of the elimination, III.I$'''''''$
Lemmas 4.3, 4.5 and Corollary 4.6 and III.I$''''''''$ Proposition 4.1's base step, inverted its maps by continuity from
$(0,0)$; Proposition 2.12 bounds them directly. Proposition 2.5's Step 3 had covered that level by a sentence that is
false there, that $G'$ depends on the new coordinates only through small terms. Found by the second batch of the
base-point ledger (verifier 146, D330).

(I$'''''''''''''''$8) *The expansion used $h_{b_0,\mathrm v1} = 0$.* III.I$''''''''''''$ Lemmas 2.3-2.4 put $\breve
h^1_{b_0,\mathrm v1}(V)$ in $\ker L_0$ and removed the v1 content through an antiderivative, both because the rotation
state vanishes at $b_0$, which they do not say. At a rotating $b$, $h_{b,\mathrm v1}(V) = \dot g_b(\dot b_V)$, Lemma 2.3
(b)'s conclusion $\dot b = 0$ fails when $\dot b_V\ne0$, and the level-3 conormal rotation tower falls below $\alpha$.
Lemma 2.9 and Corollary 2.10 restate them at $b$, with the rotation rows $T_{\mathrm v1,b}$ in place of the
antiderivative and no map inverted. Found by the third batch of the base-point ledger (verifier 147, D330).

(I$'''''''''''''''$9) *The rotation state at $b$ is a change of the black hole parameter alone.* In the nullspace of
$\widehat{L_b}(0)$, $h_{b,\mathrm v1}(V)$ is a combination of $\dot g_b$ and $h_b$; the antipodal map, an isometry of
every $g_b$ under which the translations are odd and the rotations even, removes the translation part, so $h_{b,\mathrm
v1}(V) = \dot g_b(\dot b_V)$. Without it, section 2.7's first repair put the translation part into the s1 coefficients
one order too low. Found by verifier 150 (D331).

*Labels.* Lemmas 1.1, 1.2, 2.1, 2.4, 2.7, 2.9, 2.11 (the parity in (P3) new), Propositions 2.2, 2.5, 2.8, 2.12,
Definition 2.3, Remark 2.6, Corollary 2.10, Theorem 3.1 and Corollary 3.2 are new at $n = 4$; Theorem 3.1 is what the
source states throughout its sections 11.2-12 by taking its base points with $|b-b_0|$ small.

*Sources.* [Hin26] pp. 275 (Definition 11.55), 278-280 (Theorem 11.59's statement, the v1 elimination
"$V^{(1,0)\prime}\approx\dot V$"), 293 ((11.228)-(11.229)), read at source. Inputs: II.C Lemma 1.4; III.D$''$ (3.4),
Proposition 3.1; III.D$'''$ Proposition 3.1; III.E$'$; III.F Lemma 2.1; III.F$'$ Proposition 2.3; III.F$'''$ Proposition
2.2; III.F$''''$ Proposition 5.1; III.G$'$ Theorem 3.1; III.G$''$ Table 1.1, (4.2)-(4.3), Theorems 3.1, 4.2, Corollary
4.3; III.G$''''$ Lemma 1.1, Propositions 4.4, 5.1; III.H Proposition 3.2, Corollaries 4.2-4.4; III.H$'$ Theorem 1.3;
III.H$''$ Lemma 3.2, Theorem 2.1, Corollary 5.1; III.I Lemma 3.6, Theorem 5.3, Remark 5.4;
III.I$'$-III.I$''''''''''''''$ as listed in Theorem 3.1; III.J Theorem 2.4; III.J$'$ Theorem 2.1; III.J$''$; III.J$'''$.
