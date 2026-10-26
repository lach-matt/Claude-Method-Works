# Part III.I$''''''''$. Decaying centre-of-mass motions, n = 4 ([Hin26] section 11.7)

*Status.* Verified (D269: the hundred-and-fourteenth verifier; no major finding, two minor ones and seven nits seated,
to be read). Written (D267). This part proves, at spatial dimension $n = 4$, [Hin26] section 11.7 (pp. 262-273): the
correction terms for decaying centre-of-mass motions (Definition 11.47), the operator with these parameters (Definition
11.48), its linearisation in them (Lemma 11.49), and Proposition 11.51: for sources with almost three orders of decay at
$K^+$ there is a unique choice of all modification parameters for which the forward solution has $K^+$-weight
$\alpha_K-2$ for every $\alpha_K<\min(a_K,3)$, that is, decays like $t_*^{-\alpha_K+2}$, almost like $t_*^{-1}$, in
compact spatial sets.

*What n = 4 changes.* The scheme is the source's: induction on $\alpha_K$, at each level an expansion of the solution
into finitely many decaying centre-of-mass motions $\chi_Kt_*^{-\lambda+1}(\log t_*)^kh_{b_0,\mathrm s1}(S)$ plus a
remainder, then their elimination by gauge modifications. Four things differ. (1) The motions come only from the
$\iota^+$-exponents $\lambda$ of the effective source with $\mathrm{Re}\,\lambda\in[\lambda_\sharp,2)$, through the s1
row of III.G$''$ Corollary 4.3, which is present exactly when $\ell_K = \alpha_K-\mathrm{Re}\,\lambda>1$; the zero
energy analysis produces none, as $\widehat{L_b}(0)$ has no indicial root in $(0,1]$ (III.F$'$ Proposition 2.3 (a)). So
they are extracted on spacetime by Part III.I$'''''$'s step at $\iota^+$, where the source passes to the Fourier
transform (its Step 1.2 discussion), and the rates are $\mathrm{Re}\,\lambda-1\in[\lambda_\sharp-1,1)$, present only for
$\alpha_K>\lambda_\sharp+1>\frac52$. (2) There is no proliferation of logarithms: the $\iota^+$-normal operator has no
pole below 2 and re-solving at null infinity creates no exponent below $\frac52$, so the index set of the motions is
fixed in advance and closed, the source's device $u_\Sigma$ ((11.180)-(11.183)) is not needed, and each level is linear
algebra close to the identity. (3) The zero energy analysis is Part III.I$''''''$'s, with the tf-improvement iterated
(Step 3.4$'$ below) once $\alpha_K\ge2+\epsilon_{\mathrm{ind}}$, as the source's Step 1.6. (4) The gauge modification
uses the generalised gauge 1-forms to order 4 of III.D$'''$, so that it decays to $K^+$-order $\mathrm{Re}\,\lambda+4$.
Everything is at $b = b_0$. Notation: Parts III.D$'''$, III.F$'$, III.G$''$, III.G$''''$, III.H, III.I-III.I$'''''''$;
no instrument is used.

## 1. Setting

Everything of Part III.I$'''''''$ section 1 is kept: $b = b_0$, $\mathfrak b$, $\mathcal E_{\mathrm{ind}}$ and
(1.1)-(1.2) there, $\mathcal G$, $\ell_I$ with $\ell_I\le a_I$, the translated background (1.3) there, and III.I$''''$'s
cut-offs, $\mathcal C$, $\Theta$, conventions and identities (i)-(iii). $\mathcal E_{\mathrm{ind}}$ is enlarged to
contain also the index sets of III.D$'''$ Proposition 3.1 (2) at $b_0$ (those of the $\breve\omega^i$ of section 2);
everything of III.I$'''''''$ holds with the enlarged set, which only strengthens the conditions on $\mathcal E_+$ there.
$\mathcal E^\iota_{\mathrm{ind}}$ is III.G$''$ (4.4)'s index set and $\mathcal E^\sharp_+$ is III.I$'$ (3.2) with
$\breve{\mathcal E}_+ = \emptyset$ (as in III.I$'''''$); $\min\mathrm{Re}\,\mathcal E^\sharp_+ = \lambda_\sharp =
\frac32+(1-e_\Upsilon)\gamma_\Upsilon$. Fix an index set $\mathcal E_{++}$ with
$$\mathcal E^\sharp_+\cap\{\mathrm{Re}<2\}\subset\mathcal E_{++}\subset\mathcal E_+,\qquad\min\mathrm{Re}\,\mathcal
E_{++}\ge\lambda_\sharp,\qquad\mathcal E_{++}+(\mathcal E^\iota_{\mathrm{ind}}\cup\mathcal E_{\mathrm{ind}}\cup\mathcal
E_+)\subset\mathcal E_{++};\tag{1.1}$$
for instance the least index set containing $\mathcal E^\sharp_+\cap\{\mathrm{Re}<2\}$ with the last property, provided
$\mathcal E_+$ contains $\mathcal E^\sharp_+\cap\{\mathrm{Re}<2\}$ and $\mathcal E_++(\mathcal
E^\iota_{\mathrm{ind}}\cup\mathcal E_{\mathrm{ind}}\cup\mathcal E_+)\subset\mathcal E_+$ (conditions on $\mathcal E_+$
alone, as $\mathcal E^\sharp_+$, $\mathcal E^\iota_{\mathrm{ind}}$ and $\mathcal E_{\mathrm{ind}}$ do not depend on it).
Then $\mathcal E_{++}+\mathcal E_{++}\subset\mathcal E_{++}$, and
$$\mathcal M := \{(\lambda,k)\in\mathcal E_{++}:\mathrm{Re}\,\lambda<2\}\tag{1.2}$$
is finite, with $\mathrm{Re}\,\lambda\in[\lambda_\sharp,2)$. Its exponents may be complex: $\mathcal E_{++}$ is taken
closed under conjugation (as $\mathcal E^\sharp_+$, $\mathcal E^\iota_{\mathrm{ind}}$, $\mathcal E_{\mathrm{ind}}$ and
$\mathcal E_+$ may be, coming from real operators), the motion parameters $S^{(\lambda-1,k)}_1$ below lie in $\mathcal
S_{1,\mathbb C}$ with $S^{(\bar\lambda-1,k)}_1 = \overline{S^{(\lambda-1,k)}_1}$ (for real $\lambda$:
$S^{(\lambda-1,k)}_1\in\mathcal S_1$), which makes the motion terms real, and the coefficients $S_{\lambda,k}$ of a real
$u$ in (3.1) have the same symmetry. For $\alpha\in(2,3)$ put $\mathcal M_\alpha :=
\{(\lambda,k)\in\mathcal M:\mathrm{Re}\,\lambda-1<\alpha-2\}$.

*Admissible levels.* $\alpha\in(2,\min(a_K,3))$ is admissible if $\alpha-2\ne\mathrm{Re}\,\lambda-1$ and
$\alpha-\mathrm{Re}\,\lambda\notin\{-\mathrm{Re}\,\mu\}\cup\mathrm{Re}\,\pi_1\mathcal E_K$ for every
$\lambda\in\pi_1\mathcal M$ and every root $\mu$ of III.G$''$ (a finite set of exclusions in $(2,3)$, the roots being
real and discrete). $\mathcal M_{\alpha_0} = \emptyset$ for $\alpha_0<\lambda_\sharp+1$.

*Sources.* For $\alpha\in(2,3)$, $\mathcal Y_1(\alpha) := \bigcap_\epsilon H^{\infty,(\langle\mathcal
E^C_I+1\rangle',\ell_I+1),4-\epsilon,\alpha}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-}$ (III.I$'''''''$'s $\mathcal Y$
with $\alpha$ for $\alpha_K$), $\mathcal Y_2(\alpha)$ the sections supported in $\mathrm{supp}\,\chi^\sharp_K$ (III.I
(1.2); so vanishing near $\mathscr I^+$ and for $t^\flat_*<10$) lying in $\bigcap_\epsilon H^{\infty,\infty,(\mathcal
E_{++}+2,4-\epsilon),\alpha}_{\mathrm b}$, and $\mathcal Y(\alpha) := \mathcal Y_1(\alpha)+\mathcal Y_2(\alpha)$, real
sections: the source's class (11.155). "$h$ small" means as in III.I$'''''''$ (small in $\mathcal X^d$, $d$ fixed large,
vanishing near $\{t^\flat_* = 1\}$).

## 2. Correction terms #3 and the operator ([Hin26] Definitions 11.47-11.48, Lemma 11.49 at n = 4)

*Generalised gauge 1-forms.* By III.D$'''$ Proposition 3.1 (2) at $b_0$, for $S\in\mathcal S_1$ there are stationary
1-forms $\breve\omega^i(S) := \breve\omega^{(0),i}_{b_0,\mathrm s1}(S)$, $i = 0,\dots,4$, linear in $S$, with
$\breve\omega^0 = \omega_{\mathrm s1}$, $\breve\omega^1 = \breve\omega$ (III.I$''''$ section 1),
$\breve\omega^i\in\mathcal A^{(-i,0)\cup(-i+\mathcal E_{\mathrm{ind}})}$ for $i = 2,3,4$, and $\omega^{\le k} =
\sum_{i\le k}\frac{k!}{(k-i)!}t_*^{k-i}\breve\omega^i\in\ker\Box^\Upsilon_{b_0}$ for $k\le4$, $\Box^\Upsilon_{b_0} =
2\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}\delta^*_{g_{b_0}}$ (III.D$'''$ (1.3)). For a function $a$ of $t_*$ put
$\omega^{\le4}(aS) := \sum_{i=0}^4a^{(i)}(t_*)\breve\omega^i(S)$, so that $\omega^{\le4}(t_*^kS) = \omega^{\le k}(S)$
for $k\le4$.

**Definition 2.1 ([Hin26] Definition 11.47 at n = 4).** For $(\lambda,k)\in\mathcal M$ let $a_{\lambda,k}(t_*) :=
t_*^{-\lambda+1}(\log t_*)^k$ (on $\Omega_*$, $t_*\ge1$), and for $S\in\mathcal S_{1,\mathbb C}$
$$m_{\lambda,k}(S) := \chi_K\delta^*_{g_{b_0}}\omega^{\le4}(a_{\lambda,k}S),\qquad h^{(\lambda-1,k)}_{\mathrm s1}(S) :=
-[\delta^*_{g_{b_0}},\chi_K]\omega^{\le4}(a_{\lambda,k}S) = -d\chi_K\otimes_s\omega^{\le4}(a_{\lambda,k}S),$$
$$\vartheta^{(\lambda-1,k)}_{\mathrm s1}(S) :=
\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}m_{\lambda,k}(S),\qquad\vartheta^{(\lambda-1,k)}_{\mathrm s1,\sharp} :=
\vartheta^{(\lambda-1,k)}_{\mathrm s1}-\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}h^{(\lambda-1,k)}_{\mathrm s1},$$
the last the counterterm of the source's Remark 11.27, as in III.I$''''$ and III.I$'''''''$. $m_{\lambda,k}(S)$ is the
cut-off centre-of-mass motion; the source's $h^{(\lambda-1,k)}_{b_0}$ of (11.181).

**Lemma 2.2 ([Hin26] (11.152a)-(11.152b) at n = 4).** Let $(\lambda,k)\in\mathcal M$ and $a := a_{\lambda,k}$. There are
stationary operators $A_1,A_2$ with
$$\Box^\Upsilon_{b_0}\,\omega^{\le4}(aS) =
a^{(5)}\big(A_1\breve\omega^4+A_2\breve\omega^3\big)+a^{(6)}A_2\breve\omega^4.\tag{2.1}$$
Near $(\iota^+)^\circ$, with $\mathcal F := (0,0)\cup\mathcal E_{\mathrm{ind}}$, $\omega^{\le4}(aS)\in\mathcal
A^{(\lambda-1,k)+\mathcal F}$, $m_{\lambda,k}(S)\in\mathcal A^{(\lambda,k)+\mathcal F}$, $h^{(\lambda-1,k)}_{\mathrm
s1}(S)\in\mathcal A^{(\lambda,k)+\mathcal F}$, $\vartheta^{(\lambda-1,k)}_{\mathrm
s1}(S),\vartheta^{(\lambda-1,k)}_{\mathrm s1,\sharp}(S)\in\mathcal A^{(\lambda+1,k)+\mathcal F}$ and
$D_{g_0}\mathrm{Ric}(h^{(\lambda-1,k)}_{\mathrm s1}(S))\in\mathcal A^{(\lambda+2,k)+\mathcal F}$ ($g_0$ as in
III.I$''''$ Lemma 2.2). $h^{(\lambda-1,k)}_{\mathrm s1}(S)$ is supported in $\mathcal C$; $m_{\lambda,k}(S)$ and
$\vartheta^{(\lambda-1,k)}_{\mathrm s1}(S)$ in $\mathrm{supp}\,\chi_K$, and $\vartheta^{(\lambda-1,k)}_{\mathrm s1}(S)$
has $K^+$-weight $\mathrm{Re}\,\lambda+4-\epsilon$ for every $\epsilon>0$. Finally
$$m_{\lambda,k}(S)-\chi_Ka_{\lambda,k}h(S)\ \text{has }K^+\text{-weight }\mathrm{Re}\,\lambda-\epsilon\text{ for every
}\epsilon>0.\tag{2.2}$$
All seminorms are $O(|S|)$.

*Proof.* (2.1): $\Box := \Box^\Upsilon_{b_0}$ is stationary and of second order in $\partial_{t_*}$, so
$\Box(\varphi(t_*)v) = \sum_{m=0}^2\varphi^{(m)}A_mv$ for stationary $v$, with stationary $A_m$. Hence
$\Box\,\omega^{\le4}(aS) = \sum_{j\le6}a^{(j)}B_j$, $B_j := \sum_mA_m\breve\omega^{j-m}$ ($\breve\omega^i := 0$ for
$i<0$ or $i>4$). With $a = t_*^k$, $k\le4$, this is $\Box\omega^{\le k} = 0$, whose $t_*^0$-coefficient is $k!B_k$; so
$B_j = 0$ for $j\le4$, and $B_5 = A_1\breve\omega^4+A_2\breve\omega^3$, $B_6 = A_2\breve\omega^4$. *Orders.* Near
$(\iota^+)^\circ$, $|x|\sim t_*\sim\rho_+^{-1}$, so $\breve\omega^i\in\mathcal A^{(-i,0)+\mathcal F}$ there (for $i =
0,1$ by III.I$''''$ section 1: $\omega_{\mathrm s1}-\bar\omega_{\mathrm s1}\in\mathcal A^{\mathcal G}$ with
$\bar\omega_{\mathrm s1}$ of constant Cartesian components, $\breve\omega-\breve{\bar\omega}_{\mathrm s1}\in\mathcal
A^{(1,0)+\mathcal E_{\mathrm{ind}}}$ with $\breve{\bar\omega}_{\mathrm s1}$ homogeneous of degree 1), and
$a^{(i)}\in\mathcal A^{(\lambda-1+i,k)}$; so each term of $\omega^{\le4}(aS)$ lies in $\mathcal
A^{(\lambda-1,k)+\mathcal F}$. $\delta^*_{g_{b_0}}$, $D_{g_0}\mathrm{Ric}$ and $\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}$
lie in $\rho_+\mathrm{Diff}^1_{\mathrm b}$, $\rho_+^2\mathrm{Diff}^2_{\mathrm b}$, $\rho_+\mathrm{Diff}^1_{\mathrm b}$
there, and $d\chi_K\in\rho_+C^\infty$ (III.I$''''$ Lemma 2.2's proof), which gives the $\iota^+$-orders. *Supports* are
clear. *$K^+$.* Near $K^+$, $\chi_K = 1$ and $\vartheta^{(\lambda-1,k)}_{\mathrm s1} = \frac12\Box\,\omega^{\le4}(aS)$,
which by (2.1) is $a^{(5)}$ and $a^{(6)}$ times stationary tensors smooth on compact spatial sets, of $K^+$-weight
$\mathrm{Re}\,\lambda+4-\epsilon$. (2.2): $\delta^*_{g_{b_0}}(a^{(i)}\breve\omega^i) =
a^{(i)}\widehat{\delta^*}(0)\breve\omega^i+a^{(i+1)}dt_*\otimes_s\breve\omega^i$, and
$\widehat{\delta^*}(0)\breve\omega^0 = h(S)$; every other term carries $a^{(j)}$, $j\ge1$, of $K^+$-weight
$\mathrm{Re}\,\lambda-\epsilon$. $\square$

**Definition 2.3 ([Hin26] Definition 11.48 at n = 4).** For $\vec p =
(S,b-b_0,S^{(0)}_1,(S^{(\lambda-1,k)}_1)_{(\lambda,k)\in\mathcal M})$ small and $h$ small, with $g_0 :=
g_{(S,b-b_0,S^{(0)}_1)}$ (III.I$'''''''$ (1.3)),
$$h_{\mathrm{tot}}(\vec p) := h^{\mathrm{III.I'''''''}}_{\mathrm{tot}}+\sum_{(\lambda,k)\in\mathcal
M}h^{(\lambda-1,k)}_{\mathrm s1}(S^{(\lambda-1,k)}_1),\qquad\vartheta_{\mathrm{tot}}(\vec p) :=
\vartheta^{\mathrm{III.I'''''''}}_{\mathrm{tot}}+\sum_{(\lambda,k)\in\mathcal M}\vartheta^{(\lambda-1,k)}_{\mathrm
s1,\sharp}(S^{(\lambda-1,k)}_1),$$
the first terms III.I$'''''''$ Definition 2.3's at $(S,b-b_0,S^{(0)}_1)$, and
$$P_3(h,\vec p) := \mathrm{Ric}(g')-\delta^*_{g_0,E_C}\Big(\Upsilon^{E_\Upsilon}(g',g_0)-\vartheta_{\mathrm{tot}}(\vec
p)\Big),\quad g' := g_0+h_{\mathrm{tot}}(\vec p)+h,\qquad L_{h,\vec p} := D_hP_3(\cdot,\vec p)\text{ at }h.\tag{2.3}$$
$P_3 = P_2$ where the motion parameters vanish.

**Lemma 2.4 (the motion identity; [Hin26] (11.137), (11.154) at n = 4).** For $(\lambda,k)\in\mathcal M$ and
$S\in\mathcal S_1$, $D_{\vec p}P_3(0,0)(S^{(\lambda-1,k)}_1 = S) = L_{b_0}(m_{\lambda,k}(S))$, and $m_{\lambda,k}(S)$,
vanishing for $t^\flat_*<10$, is its forward solution (II.E Proposition 3.4). The identities III.I$'''''''$ (2.3) hold
for $P_3$.

*Proof.* At $\vec p = 0$, $g' = g_0 = g_{b_0}$ and $\Upsilon^{E_\Upsilon}(g_{b_0},g_{b_0})-\vartheta_{\mathrm{tot}}(0) =
0$; $g_0$ does not depend on $S^{(\lambda-1,k)}_1$, and $\dot g' = h^{(\lambda-1,k)}_{\mathrm s1}(S) =
\chi_K\delta^*\omega^{\le4}(aS)-\delta^*(\chi_K\omega^{\le4}(aS)) = m_{\lambda,k}(S)-\delta^*(\chi_K\omega^{\le4}(aS))$
by III.I$''''$ (1.2). As in III.I$'''''''$ Lemma 2.4, $DP_3 = D\mathrm{Ric}(\dot g')-\delta^*_{E_C}(D_1\Upsilon\,\dot
g'-\vartheta^{(\lambda-1,k)}_{\mathrm s1,\sharp}(S))$ with $D_1\Upsilon = -\delta_{E_\Upsilon}G$ by (ii), so $DP_3 =
D\mathrm{Ric}(m_{\lambda,k}(S))+\delta^*_{E_C}\vartheta^{(\lambda-1,k)}_{\mathrm s1}(S)$ by (iii) and the counterterm,
which is $L_{b_0}m_{\lambda,k}(S) = D\mathrm{Ric}(m)+\delta^*_{E_C}\delta_{E_\Upsilon}Gm$ by Definition 2.1. The rest is
III.I$'''''''$ Lemma 2.4, as $P_3 = P_2$ on the other directions at $\vec p = 0$. $\square$

As in the source, the identity is exact because the gauge term is the full $\delta_{E_\Upsilon}G$ of the cut-off motion,
not a commutator; (2.1) makes it decay to $K^+$-order $\mathrm{Re}\,\lambda+4$, which is why four generalised gauge
1-forms are used (the source's Remark 11.39).

**Lemma 2.5 (the linearisation in $h$).** Let $\vec p$ (with $b = b_0$) and $h$ be small. Then $h_{\mathrm{tot}}(\vec
p)\in\mathcal X^\infty$ with $\|h_{\mathrm{tot}}(\vec p)\|_{\mathcal X^k}\le C_k|\vec p|$, $L_{h,\vec p} = L^{g',g_0}$,
and III.I$'''''''$ Lemma 2.5 (b)-(c) hold for $L_{h,\vec p}$.

*Proof.* As III.I$'''''''$ Lemma 2.5, with Lemma 2.2: the new terms are supported in $\mathcal C$ and lie in $\mathcal
A^{(\lambda,k)+\mathcal F}\subset\mathcal A^{\mathcal E_{++}}\subset\mathcal A^{\mathcal E_+}$ near $(\iota^+)^\circ$ by
(1.1). $\square$

**Lemma 2.6 ([Hin26] Lemma 11.49 at n = 4).** Let $\vec p$ (with $b = b_0$) and $h\in\mathcal X^k$, $k\ge5$, be small.
(a) The derivatives $f^S_{h,\vec p}$, $f^b_{h,\vec p}$, $f^{\mathrm s1}_{h,\vec p}$ of $P_3$ in $S$, $b$, $S^{(0)}_1$
satisfy III.I$'''''''$ Lemma 3.1 up to terms lying in $\mathcal Y_1(\alpha)$ for every $\alpha\in(2,3)$; in particular
they lie in $\mathcal Y_1(\alpha)$ for $\alpha\le a_K$ (with $\ell_I\le a_I$). (b) For $(\lambda,k)\in\mathcal M$,
$f^{(\lambda,k)}_{h,\vec p}(S) := D_{\vec p}P_3(h,\vec p)(S^{(\lambda-1,k)}_1 = S)$ is supported in
$\mathrm{supp}\,\chi_K$ and lies in $H^{k-2,\infty,((\lambda+2,k)+\mathcal F+((0,0)\cup\mathcal
E_+),\,4-\epsilon),\,\mathrm{Re}\,\lambda+4-\epsilon}_{\mathrm b}$, with norm $O(|S|)$, so in $\mathcal Y_2(\alpha)$
when $h\in\mathcal X^\infty$ (as "$h$ small" requires). (c) All are linear in the direction, continuous in $(h,\vec p)$,
and at $(0,0)$ given by Lemma 2.4.

*Proof.* (a) III.I$'''''''$ Lemma 3.1's proof: its counts use $h_{\mathrm{tot}}$ only through $g'-\eta\in H^{k,(\mathcal
E_+,a_+)}_{\mathrm b}$ near $(\iota^+)^\circ$, which still holds (Lemma 2.5). The derivative in each of $S$, $b$,
$S^{(0)}_1$ falls on the motion terms only through $\delta^*_{g_0,E_C}$, which depends on these parameters through $g_0$
and acts on $\vartheta_{\mathrm{mot}} := \sum_{(\lambda,k)\in\mathcal M}\vartheta^{(\lambda-1,k)}_{\mathrm
s1,\sharp}(S^{(\lambda-1,k)}_1)$, nonzero near $K^+$. The extra term
$(\partial\delta^*_{g_0,E_C})\vartheta_{\mathrm{mot}}$ is linear in the motion parameters, supported in
$\mathrm{supp}\,\chi_K$, of $\iota^+$-order at least $\mathrm{Re}\,\lambda+4$ (the derivative of $g_0$ has
$\iota^+$-order 2, and $\vartheta$ order $\lambda+1$ by Lemma 2.2) and of $K^+$-weight
$\mathrm{Re}\,\lambda+4-\epsilon\ge\lambda_\sharp+4-\epsilon>3$, and continuous in $(h,\vec p)$; so it lies in $\mathcal
Y_1(\alpha)$ for every $\alpha\in(2,3)$. (b) $P_3$ depends on $S^{(\lambda-1,k)}_1$ only through
$h^{(\lambda-1,k)}_{\mathrm s1}$ (in $\mathcal C$) and $\vartheta^{(\lambda-1,k)}_{\mathrm s1,\sharp}$ (in
$\mathrm{supp}\,\chi_K$), linearly; so $f^{(\lambda,k)} = D_{g'}\mathrm{Ric}(h')-\delta^*_{g_0,E_C}\big(
[D_1\Upsilon(g',g_0)-D_1\Upsilon(g_{b_0},g_{b_0})]h' -\vartheta^{(\lambda-1,k)}_{\mathrm s1}(S)\big)$, $h' :=
h^{(\lambda-1,k)}_{\mathrm s1}(S)$, by the definition of the counterterm. With
$D_{g'}\mathrm{Ric}\in\rho_+^2(C^\infty+H^{(\mathcal E_+,a_+)}_{\mathrm b})\mathrm{Diff}^2_{\mathrm b}$,
$\delta^*_{g_0,E_C}\in\rho_+\mathrm{Diff}^1_{\mathrm b}$, the bracket linear in $(g'-g_{b_0},g_0-g_{b_0})\in
H^{(\mathcal E_+,a_+)}_{\mathrm b}$ and their first derivatives, and Lemma 2.2, the $\iota^+$-data are
$((\lambda+2,k)+\mathcal F+((0,0)\cup\mathcal E_+),a_++\mathrm{Re}\,\lambda+2)$, and $a_++\mathrm{Re}\,\lambda+2>4$;
near $K^+$ only $\delta^*_{g_0,E_C}\vartheta^{(\lambda-1,k)}_{\mathrm s1}$ remains, of weight
$\mathrm{Re}\,\lambda+4-\epsilon$. $(\lambda+2,k)+\mathcal F+((0,0)\cup\mathcal E_+)\subset\mathcal E_{++}+2$ by (1.1).
(c) As in III.I$'''''''$ Lemma 3.1 (c). $\square$

The source's (11.153) has the $K^+$-order $\lambda+4-\epsilon$ and the index set $(\lambda+2,k)+((0,0)\cup\mathcal
E_{\mathrm{ind}}\cup\mathcal E_+\cup\tilde{\mathcal E}'_{++})$; its (11.154) is used for its device $u_\Sigma$, not
needed here ((I$''''''''$2)).

## 3. The expansion at one level ([Hin26] Proposition 11.51, Part 1, at n = 4)

**Lemma 3.1 (the base level).** Let $\alpha_0\in(2,\min(a_K,2+\epsilon_{\mathrm{ind}},\frac52))$ be admissible
($\epsilon_{\mathrm{ind}}$ III.G$''''$ Proposition 5.1's). Then III.I$''''''$ Proposition 2.1 and III.I$'''''''$ Lemmas
4.1, 4.3, 4.5 and Corollary 4.6 hold with $\mathcal Y(\alpha_0)$ in place of $\mathcal Y$, at the base points of Lemma
2.5, with the conclusions at $K^+$-weight $\alpha_0-2-\epsilon$ for every $\epsilon>0$.

*Proof.* Steps 0-2 of III.I$''''''$ Proposition 2.1's proof change. Let the source be $F = F_1+F_2$, $F_j\in\mathcal
Y_j(\alpha_0)$. *Step 0.* Step 2 below, applied to $F_2$ alone (with $L_b$; $F_2$ vanishes near $\mathscr I^+$), gives
$u_F := \sum_{\lambda_0}(u_{\lambda_0}+u'_{\lambda_0})$, over the finitely many $\lambda_0\in\pi_1\mathcal E_{++}$ with
$\mathrm{Re}\,\lambda_0<2$, with $F_2-L_bu_F$ of plain $\iota^+$-weight $4-\epsilon$, of $K^+$-weight
$\alpha_0-\epsilon$ and with the $\mathscr I^+$-data of $\mathcal Y_1$, for every $\epsilon>0$. $u_F$ vanishes near
$\{t^\flat_* = 1\}$ (Step 2's pieces are cut off near $\iota^+$) and has $\iota^+$-weight $\lambda_\sharp-\epsilon$ and
$K^+$-weight $\alpha_0-2-\epsilon$ (as there: $\ell_K(\lambda_0)>\alpha_0-2$ and
$\mathrm{Re}\,\lambda_0-1>\frac12>\alpha_0-2$), so $(L-L_b)u_F$ has $\iota^+$-weight above 4 and $K^+$-weight above
$\alpha_0$ (III.I Proposition 4.1 (4.2), $a_K>2$). So $u-u_F$ is the forward solution of $L(u-u_F) =
F_1+(F_2-L_bu_F)-(L-L_b)u_F$, a source of plain $\iota^+$-weight $4-\epsilon$ whose boost parameter is that of $F$
($\dot S(Lu_F) = 0$ by the uniqueness in III.I$''''$ Proposition 4.1 (1), $u_F$ being the decaying forward solution),
and III.I$'''''$ Proposition 2.1 applies to it with any $\alpha_+<2$: $u-u_F$ has $K^+$-weight $\alpha'_K-2$ for every
$\alpha'_K<2$. With $\alpha'_K>\alpha_0+2-a_K$ (possible, as $a_K>\alpha_0$), $(L-L_b)u$ has $K^+$-weight above
$\alpha_0$ and $\iota^+$-weight above $4-\epsilon$, which is III.I$''''''$ Step 0's conclusion. Write $f'_1 :=
F_1-(L-L_b)u\in\mathcal Y_1(\alpha_0)$, so that $L_bu = f'_1+F_2$. Step 1 applies III.I$'$ Proposition 3.1 to $f'_1$
alone ($\breve{\mathcal E}_+ = \emptyset$), and $f^\flat_0 := f'_1-L_bu_I+F_2$; its $\iota^+$-terms below
$\alpha^\sharp_++2$ have exponents in $(\mathcal E^\sharp_+\cup\mathcal E_{++})+2$, with coefficients from $L_bu_I$
(vanishing near $K^+$) or from $F_2$ (supported in $\mathrm{supp}\,\chi^\sharp_K$, away from $\mathscr I^+$), and
III.I$'''''$ (2.3) is taken with $\mathcal E_{++}$ added to the excluded exponents (still finite below 2). Step 2 takes
$c_K := \alpha_0$, so $\ell_K(\lambda_0) = \alpha_0-\mathrm{Re}\,\lambda_0$; its exclusions hold by admissibility, and
$\ell_K(\lambda_0)\in(\alpha_0-2,1)\subset(0,1)$ as $\mathrm{Re}\,\lambda_0\in[\lambda_\sharp,2)$ and
$\alpha_0<\frac52<\lambda_\sharp+1$. The coefficients at $\lambda_0$ of $F_2$ and of later errors (of $K^+$-weight
$\alpha_0-\epsilon$ for every $\epsilon$) have $R$-weight $\ge\ell_K(\lambda_0)-2-\epsilon$ for every $\epsilon$, which
is III.G$''$ Corollary 4.3's hypothesis; the errors have $K^+$-weight $\alpha_0-\epsilon$; and $u_{\lambda_0}$ has
$K^+$-weight $\min(\mathrm{Re}\,\lambda_0-1,\ell_K(\lambda_0))-\epsilon>\alpha_0-2$ for $\epsilon$ small. The iteration
and its termination are III.I$'''''$'s, all exponents lying in $(\mathcal E^\sharp_+\cup\mathcal E_{++})+\mathbb
N_0\mathcal E^\iota_{\mathrm{ind}}\subset\mathcal E_{++}$ below 2 by (1.1). So $f^\flat\in\bigcap_\epsilon
H^{\infty,\ell_I+1,4-\epsilon,\alpha_0-\epsilon}_{\mathrm b}$, and Steps 3-6 apply with $\alpha_0-\epsilon'$ for
$\alpha_K$, for every small $\epsilon'$ (their hypotheses on $\alpha_K$ are open conditions). III.I$'''''''$ section 4
uses III.I$''''$ Proposition 4.1 (1), whose source space contains $\mathcal Y(\alpha_0)$ ($F_2$ has $\iota^+$-weight
above $\alpha_++2$ for $\alpha_+<\min\mathrm{Re}\,\mathcal E_{++}$), III.I$''''''$ Proposition 2.1, and in Lemma 4.1 the
bound of $(L_j-L_{b_0})u_j$ in $\mathcal Y_1(\alpha_0)$, unchanged. $\square$

**Lemma 3.2 (the expansion; [Hin26] Proposition 11.51, Part 1, at n = 4).** Let $\alpha'<\alpha$ be admissible,
$\alpha-\alpha'<a_K-2$, let $\vec p$ ($b = b_0$) and $h$ be small, and $F\in\mathcal Y(\alpha)$. Suppose that the
forward solution $u$ of $L_{h,\vec p}u = F$ lies in $\bigcap_\epsilon H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\beta'_+,\alpha'-2-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}$ for some
$\beta'_+\in(1,\min(\frac32,\min\mathrm{Re}\,\mathcal E_+))$. Then
$$u = \sum_{(\lambda,k)\in\mathcal M_\alpha\setminus\mathcal M_{\alpha'}}\chi_Kt_*^{-\lambda+1}(\log
t_*)^kh(S_{\lambda,k})+\tilde u,\qquad\tilde u\in\bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal
E^C_I\rangle,\ell_I),\beta_+,\alpha-2-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}\tag{3.1}$$
for every $\beta_+<\min(\frac32,\min\mathrm{Re}\,\mathcal E_+)$, with $S_{\lambda,k} =: S^{h,\vec
p}_{\lambda,k}(F)\in\mathcal S_{1,\mathbb C}$ determined by $u$ (its $K^+$-expansion), linear and continuous in $F$,
with bounds uniform for $(h,\vec p)$ small.

*Proof.* *Step 0.* $f' := F-(L-L_b)u = f'_1+F_2$ with $f'_1 := F_1-(L-L_b)u\in\mathcal Y_1(\alpha)$: III.I Proposition
4.1 (4.2) (for $L = L_{h,\vec p}$, Lemma 2.5) gives the $\mathscr I^+$-data $(\langle\mathcal
E^C_I+1\rangle',\ell_I+1)$, the $\iota^+$-weight $\beta'_++2+m_+-\epsilon>4-\epsilon$ and the $K^+$-weight
$\alpha'-2-\epsilon+a_K\ge\alpha$ for $\epsilon$ small.

*Steps 1-2 (null infinity and $\iota^+$).* As in Lemma 3.1, with $\alpha$ for $\alpha_0$ and $\alpha^\sharp_+ :=
2-\epsilon$: Step 1 gives $u_I$; Step 2, with $\ell_K(\lambda_0) := \alpha-\mathrm{Re}\,\lambda_0\in(\alpha-2,\frac32)$
(below $\ell^{\max}_K = \min(3,2+2\gamma_Cv_C)$ and off its exclusions by admissibility), gives $u_\iota = \sum
u_{\lambda_0}+\sum u'_{\lambda_0}$ with errors of $K^+$-weight $\alpha-\epsilon$, so
$$u^\flat := u-u_I-u_\iota:\qquad L_bu^\flat = f^\flat\in\bigcap_\epsilon
H^{\infty,\ell_I+1,4-\epsilon,\alpha-\epsilon}_{\mathrm b}(\Omega_*)^{\bullet,-}.\tag{3.2}$$
Now $\ell_K(\lambda_0)>1$ exactly when $\mathrm{Re}\,\lambda_0-1<\alpha-2$, and then $-1\in\mathcal
W(\ell_K(\lambda_0))$ and the s1 row of III.G$''$ (4.3) is present. By III.G$''$ Corollary 4.3, $u_{\lambda_0}$ has
$K^+$-index set $\mathcal E^{\mathrm{gr}}_K(\lambda_0)+(0,k)$ at weight $\ell_K(\lambda_0)-\epsilon$, whose elements
with real part below $\mathrm{Re}\,\lambda_0$ are $(\lambda_0-1,j)$, $j\le k$, from the s1 row: the v1 row gives
$\lambda_0$ and the other rows $\lambda_0-\mu+j$ with $\mathrm{Re}\,\mu\le0$ (III.G$''$ Theorem 4.2). The s1 row is
$h^{\le3}_{b_0,\mathrm s1}$ of $a_{\mathrm s1}$-type functions times $S^{(-1)}_1$-coefficients, whose leading term at
$K^+$ is that function times $h(\cdot)$, the other terms carrying derivatives of it, as in Lemma 2.2 (2.2). So
$$u_{\lambda_0}-\sum_{j\le k}\chi_Kt_*^{-\lambda_0+1}(\log t_*)^jh(S_{\lambda_0,j})\ \text{has }K^+\text{-weight
}\min(\mathrm{Re}\,\lambda_0,\ell_K(\lambda_0))-\epsilon>\alpha-2,$$
the sum present only when $\mathrm{Re}\,\lambda_0-1<\alpha-2$, with $S_{\lambda_0,j}$ linear in the coefficients of the
source; $u'_{\lambda_0}$ vanishes near $K^+$. As $\lambda_0$ runs over $\mathcal M$ (Lemma 3.1's proof), $u_\iota =
\sum_{(\lambda,k)\in\mathcal M_\alpha}\chi_Kt_*^{-\lambda+1}(\log t_*)^kh(S_{\lambda,k})+(K^+\text{-weight}>\alpha-2)$;
every term of $u_\iota$ decays at $K^+$ (weight $\ge\min(\lambda_\sharp-1,\alpha-2)-\epsilon>0$).

*Step 3 (zero energy).* III.I$''''''$ Steps 3-3.3 apply to (3.2) with $\alpha-\epsilon'$ for $\alpha_K$ ($\epsilon'>0$
small, so $\alpha-\epsilon'\in(2,3)$ with the same exclusions): they use $\alpha_K\in(2,3)\setminus\mathbb N$ only
((2.25a), III.I$''$ Lemma 4.1, III.G$''''$ Proposition 5.1 with $\ell_{\mathrm{zf}} = \alpha_K-2\notin\mathbb N_0$ and
$w = \alpha_K-2+\epsilon$, and the remainder weights of (2.4)). They give $\hat u_0$, $\dot b_0$, $S_0 = 0$ (the
argument there: $u$ has $K^+$-weight $>-1$), $\hat u'_3$, $\Sigma_3$, $(\hat u_4,\hat b_4,\hat S_4)$ and
$$\hat f_5\in H^{\infty,(\frac52-\epsilon,\tau_0,\alpha-2-\epsilon')}_{\mathrm b},\qquad\tau_0 :=
2+\epsilon_{\mathrm{ind}}-2\epsilon\quad\text{(III.I$''''''$ (2.7))}.$$

*Step 3.4$'$ (the tf-iteration; the source's Step 1.6).* Put $\hat f^{(0)} := \hat f_5$. While
$\tau_i\le\alpha-\epsilon'$, apply III.G$''''$ Proposition 5.1 on $X^\pm_{\mathrm{sc}\text-\mathrm b}$ separately to
$g_i := \sigma^{-1}\hat f^{(i)}\in H^{\infty,(\frac52-\epsilon,\tau_i-1,\alpha-3-\epsilon')}_{\mathrm b}$ ($|\sigma| =
\rho_{\mathrm{tf}}\rho_{\mathrm{zf}}$) with $\alpha_i := \tau_i-1\in(1,2)$ for its $\alpha$, $\ell_{\mathrm{scf}} :=
\frac32-\epsilon$, $\ell_{\mathrm{zf}} := \alpha-3-\epsilon'\in(-1,0)$, $k_0 := 1$ (so the zf-expansion of its proof is
empty), and $w = \ell_{\mathrm{zf}}-\alpha_i+2 = \alpha-\epsilon'-\tau_i\in[0,1)$, inside
$(-\epsilon_{\mathrm{ind}},\ell^{\max}_K)$; $\epsilon,\epsilon'$ are chosen so that $w$ and every $2-\alpha_i+j$,
$j\in\mathbb N_0$, avoid the discrete set of the $-\mu$ (finitely many $i$). It gives $v_i =
\chi_{\mathrm{zf}}u^{(i)}_b+\chi^\sharp_{\mathrm{tf}}\tilde v_i\in
H^{\infty,(\frac32-2\epsilon,\alpha_i-2,\alpha_i-3)}_{\mathrm b}$ with $g_i-\widehat{L_b}(\sigma)v_i\in
H^{\infty,(\frac52-\epsilon,\alpha_i+\epsilon_{\mathrm{ind}}-\epsilon,\alpha-3-\epsilon')}_{\mathrm b}$. With the s1
coefficient $S_i := S^{(-1)}_1$ of $u^{(i)}_b$ (III.G$''''$ (5.2)), $\Sigma^{(i)} := -\sigma^2|\sigma|^{\alpha_i-3}S_i$
and $v'_i := v_i-\hat h^{\mathrm{aug}}(\sigma)(\Sigma^{(i)})$, III.I$''''''$ Lemma 1.4 and (2.6) there give
$\widehat{L_b}(\sigma)v'_i+\hat f_{\Sigma^{(i)}}(\sigma) = \widehat{L_b}(\sigma)v_i$, $v'_i$ of tf- and zf-weight
$\alpha_i-2$ near zf and tf, $r(v'_i) = O(|\sigma|^{\alpha_i-2})$, and $\Sigma^{(i)} = O(|\sigma|^{\alpha_i-1})$. Put
$$\hat f^{(i+1)} := \hat f^{(i)}-\sigma\widehat{L_b}(\sigma)v_i\in
H^{\infty,(\frac52-\epsilon,\tau_{i+1},\alpha-2-\epsilon')}_{\mathrm b},\qquad\tau_{i+1} :=
\tau_i+\epsilon_{\mathrm{ind}}-\epsilon.$$
The increments are below 1 ($\epsilon_{\mathrm{ind}}<1$: the class roots of III.G$''$ Table 1.1 are not integers, and
III.G$''''$ section 3 places every $\{-\mu\}$ at 0 or in $[\epsilon_{\mathrm{ind}},1-\epsilon_{\mathrm{ind}}]$), so
after finitely many rounds, $i_0$ say, $\tau_{i_0}\in(\alpha-\epsilon',\alpha-\epsilon'+1)$ ($i_0 = 0$ if
$\tau_0>\alpha-\epsilon'$, which is III.I$''''''$'s case $\alpha_K<2+\epsilon_{\mathrm{ind}}$). Then III.I$''$ Lemma 4.2
with $\beta_{\mathrm{scf}} := \frac32-2\epsilon$, $\beta_{\mathrm{tf}} := \tau_{i_0}-2$, $\beta_{\mathrm{zf}} :=
\alpha-2-\epsilon'$, $\beta_{\mathrm{tf}}-\beta_{\mathrm{zf}}\in(0,1)$, gives $(\hat u_6,\hat b_6,\hat S_6) := \tilde
L_b(\sigma)^{-1}(\hat f^{(i_0)},0,0)$, $\hat u_6\in
H^{\infty,(\frac32-3\epsilon,\tau_{i_0}-2,\alpha-2-\epsilon')}_{\mathrm b}$, $\hat b_6,\hat S_6\in
H^{\infty,\alpha-2-\epsilon'}_{\mathrm b}(\pm(0,c],|\frac{d\sigma}\sigma|)$. With $(U^{(i)},B^{(i)},\Sigma^{(i)}_r) :=
\tilde L_b(\sigma)^{-1}(0,\sigma r(v'_i))$,
$$(\hat u_5,\hat b_5,\hat S_5) := \sum_{i<i_0}\Big[(\sigma
v'_i,0,\sigma\Sigma^{(i)})-(U^{(i)},B^{(i)},\Sigma^{(i)}_r)\Big]+(\hat u_6,\hat b_6,\hat S_6)\tag{3.3}$$
equals $\tilde L_b(\sigma)^{-1}(\hat f_5,0,0)$: applying $\tilde L_b(\sigma)$, the first components give
$\sum_i\sigma\widehat{L_b}(\sigma)v_i+\hat f^{(i_0)} = \hat f_5$ (telescoping, with $\tilde L_b(\sigma)(\sigma
v'_i,0,\sigma\Sigma^{(i)}) = (\sigma\widehat{L_b}(\sigma)v_i,\sigma r(v'_i))$ by III.H Lemma 2.5 (c)), the rows
$\sum_i(\sigma r(v'_i)-\sigma r(v'_i)) = 0$, and every first component lies in the space of III.I$''''''$ Lemma 1.2, so
injectivity applies. By III.I$''''''$ Lemma 1.3, $B^{(i)},\Sigma^{(i)}_r =
O(|\sigma|^{1-\epsilon}\cdot|\sigma|^{\alpha_i-1})$ and $U^{(i)}$ has zf- and tf-weight at least $\alpha_i-1-\epsilon$.
This replaces III.I$''''''$ Step 3.4.

*Step 3.5$'$ (assembly).* III.I$''''''$ (2.8) holds with this $(\hat u_5,\hat b_5,\hat S_5)$, by the same computation.
In (2.9) the new terms are $\sigma^2v'_i$, of zf- and tf-weight
$\alpha_i\ge1+\epsilon_{\mathrm{ind}}-2\epsilon>\alpha-2$, $\sigma U^{(i)}$, $\sigma\hat u_6$ (zf-weight
$\alpha-1-\epsilon'$), $\sigma B^{(i)}$, $\sigma\hat b_6$, and in $\sigma^{-1}\hat S_1-\hat S_4$ the terms
$\sigma\Sigma^{(i)} = O(|\sigma|^{\alpha_i})$, $\Sigma^{(i)}_r$ and $\hat S_6$, all $O(|\sigma|^{\alpha-2-\epsilon'})$
with $\sigma\partial_\sigma$-regularity ($\alpha_i>1>\alpha-2$). So (2.9) holds with $\alpha-\epsilon'$ for $\alpha_K$.

*Steps 4-5.* III.I$''''''$ Steps 4 and 5 then give $u_{\mathrm{reg}}$ of $K^+$-weight $\alpha-1-\epsilon'$,
$u_{\mathrm{hi}}$ of weight $N$, and $u_{\mathrm{sing}}-\chi_K(\dot g(\dot b_0)+h(i\hat S_4))$ of weight
$\alpha-2-\epsilon'$ (with the matching there). *Step 6.* $u^\flat = u-u_I-u_\iota$ has positive $K^+$-weight ($u$ by
hypothesis, $\alpha'>2$; $u_\iota$ by Steps 1-2; $u_I$ vanishes near $K^+$), so the stationary tensor $\dot g(\dot
b_0)+h(i\hat S_4)$ times $\chi_K$ has positive $K^+$-weight and vanishes, and $\dot b_0 = 0$, $\hat S_4 = 0$
(injectivity, III.H (3.1)). *Step 7.* So $u = u_\iota+(u_I+u^\flat)$ is (3.1) with the sum over $\mathcal M_\alpha$; the
terms with $(\lambda,k)\in\mathcal M_{\alpha'}$ vanish, as $u$ has $K^+$-weight $\alpha'-2-\epsilon$ for every
$\epsilon$ and $\mathrm{Re}\,\lambda-1<\alpha'-2$ ($\alpha'$ admissible): a finite sum of such polyhomogeneous terms in
that space is zero, the functions $t_*^{-\lambda+1}(\log t_*)^j$ being independent and $h$ injective. *Step 8.* The
$\mathscr I^+$-data of $\tilde u$ follow from III.I$'$ Proposition 2.1 as in III.I$''''''$ Step 6 ($\chi_K = 0$ near
$\mathscr I^+$). *Determination, linearity, bounds.* The $S_{\lambda,k}$ are the coefficients of the $K^+$-expansion of
$u$ below $\alpha-2$; every map used is linear, and fixed by $L_{b_0}$, given by $L-L_{b_0}$, or III.I$'$ Proposition
2.1 applied to $L$ (Step 8), with coefficient bounds uniform for small $(h,\vec p)$ (Lemma 2.5, III.I$'''''''$ Lemma 2.5
(c)). $\square$

**Lemma 3.3 (the coefficients near the base point).** Let $\alpha'<\alpha$ be as in Lemma 3.2, $(h_j,\vec p_j)\to(0,0)$,
$F_j\to F$ in $\mathcal Y(\alpha)$, and suppose that the forward solutions $u_j$ of $L_{h_j,\vec p_j}u_j = F_j$ and $u$
of $L_{b_0}u = F$ lie in the space of Lemma 3.2's hypothesis, $u_j$ bounded there. Then $S^{h_j,\vec
p_j}_{\lambda,k}(F_j)\to S^{0,0}_{\lambda,k}(F)$ for every $(\lambda,k)\in\mathcal M_\alpha\setminus\mathcal
M_{\alpha'}$.

*Proof.* $u_j-u$ is the forward solution of $L_{b_0}(u_j-u) = R_j := F_j-F-(L_j-L_{b_0})u_j$, and $(L_j-L_{b_0})u_j\to0$
in $\mathcal Y_1(\alpha)$ by Step 0's count (coefficients of norm $o(1)$, Lemma 2.5). So $R_j\to0$, $u_j-u$ satisfies
Lemma 3.2's hypothesis, and comparing the expansions (3.1) of $u_j$, $u$ and $u_j-u$ gives $S^{h_j,\vec
p_j}_{\lambda,k}(F_j)-S^{0,0}_{\lambda,k}(F) = S^{0,0}_{\lambda,k}(R_j)\to0$. $\square$

## 4. Elimination ([Hin26] Proposition 11.51 at n = 4)

For an admissible $\alpha$ put $\mathcal P_\alpha := \mathcal S_1\oplus\mathfrak b\oplus\mathcal
S_1\oplus\big(\bigoplus_{(\lambda,k)\in\mathcal M_\alpha}\mathcal S_{1,\mathbb C}\big)^{\mathrm{sym}}$ (the
conjugation-symmetric tuples of section 1), the modification parameters with motion components only in $\mathcal
M_\alpha$, and write $D_{\vec p}P_3(h,\vec p)(\vec p\,')$ for $\vec p\,'\in\mathcal P_\alpha$ (the other motion
components zero). By Lemma 2.6, $D_{\vec p}P_3(h,\vec p)(\vec p\,')\in\mathcal Y(\alpha)$.

**Proposition 4.1 ([Hin26] Proposition 11.51 at n = 4).** Let $\alpha\in(2,\min(a_K,3))$ be admissible, and $\vec p$ ($b
= b_0$) and $h$ small. For every $F\in\mathcal Y(\alpha)$ there is a unique $\vec p\,' = \vec p\,'_{h,\vec
p}(F)\in\mathcal P_\alpha$ such that the forward solution of
$$L_{h,\vec p}u = F-D_{\vec p}P_3(h,\vec p)(\vec p\,')\tag{4.1}$$
satisfies
$$u\in\bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta_+,\alpha-2-\epsilon}_{\mathrm
b}(\Omega_*;S^2T^*)^{\bullet,-}\quad\text{for every }\beta_+<\min(\tfrac32,\min\mathrm{Re}\,\mathcal E_+).\tag{4.2}$$
Moreover (i) $\vec p\,'_{h,\vec p}$ and $F\mapsto u$ are linear, with bounds uniform for $(h,\vec p)$ small; (ii) if
$(h_j,\vec p_j)\to(0,0)$ and $F_j\to F$ in $\mathcal Y(\alpha)$, then $\vec p\,'_{h_j,\vec p_j}(F_j)\to\vec
p\,'_{0,0}(F)$. In compact spatial sets $u = O(t_*^{-\alpha+2+\epsilon})$, almost $O(t_*^{-1})$ as $\alpha\to3$.

*Proof.* Choose admissible $\alpha_0<\alpha_1<\dots<\alpha_N = \alpha$ with
$\alpha_0\in(2,\min(a_K,2+\epsilon_{\mathrm{ind}},\frac52))$ and $\alpha_{i+1}-\alpha_i<a_K-2$ (the excluded set is
finite). By induction on $i$ we prove the statement, with (i)-(ii), at $\alpha_i$.

*Base.* $\mathcal M_{\alpha_0} = \emptyset$, as $\mathrm{Re}\,\lambda-1\ge\lambda_\sharp-1>\frac12>\alpha_0-2$. By Lemma
3.1, III.I$'''''''$ Corollary 4.6 gives existence, uniqueness and linearity; the bounds are uniform by III.I$'''''''$
Lemma 2.5 (c) and as the finite-dimensional maps inverted in Lemmas 4.3 and 4.5 there are uniformly close to
$\pm\mathrm{id}$; and (ii) holds as those lemmas' maps converge (by their proofs and Lemma 4.1 there, which allows
sources varying with $j$).

*Step.* Let the statement hold at $\alpha' := \alpha_i$, and let $\alpha'' := \alpha_{i+1}$, $\mathcal N := \mathcal
M_{\alpha''}\setminus\mathcal M_{\alpha'}$ and $F\in\mathcal Y(\alpha'')\subset\mathcal Y(\alpha')$. For $\vec S =
(S_\nu)_{\nu\in\mathcal N}$ conjugation-symmetric (section 1; $T_{h,\vec p}$ below preserves these, $L$ and $F$ being
real) put $F(\vec S) := F-\sum_{\nu\in\mathcal N}f^\nu_{h,\vec p}(S_\nu)\in\mathcal Y(\alpha'')$ (Lemma 2.6 (b)), and
let $u(\vec S)$ be the forward solution of
$$L_{h,\vec p}u(\vec S) = G(\vec S) := F(\vec S)-D_{\vec p}P_3(h,\vec p)\big(\vec p\,'_{h,\vec p,\alpha'}(F(\vec
S))\big)\in\mathcal Y(\alpha''),$$
which lies in (4.2) at $\alpha'$ by the hypothesis. Lemma 3.2 (with $\alpha'$, $\alpha''$) applies and gives the
coefficients $C_\nu(\vec S) := S^{h,\vec p}_\nu(G(\vec S))$, $\nu\in\mathcal N$, affine in $\vec S$: $C(\vec S) =
C(0)-T_{h,\vec p}\vec S$, where $T_{h,\vec p}\vec S := S^{h,\vec p}(G_1(\vec S))$ with $G_1(\vec S) := \sum_\nu
f^\nu_{h,\vec p}(S_\nu)-D_{\vec p}P_3(h,\vec p)(\vec p\,'_{h,\vec p,\alpha'}(\sum_\nu f^\nu_{h,\vec p}(S_\nu)))$. *At
$(0,0)$:* $f^\nu_{0,0}(S_\nu) = L_{b_0}m_\nu(S_\nu)$ (Lemma 2.4), whose forward solution $m_\nu(S_\nu)$ has $K^+$-weight
$\mathrm{Re}\,\lambda-1-\epsilon>\alpha'-2-\epsilon$ ($\nu = (\lambda,k)\notin\mathcal M_{\alpha'}$) and the other
properties of (4.2) (Lemma 2.2; it vanishes near $\mathscr I^+$); by uniqueness at $\alpha'$, $\vec
p\,'_{0,0,\alpha'}(f^\nu_{0,0}(S_\nu)) = 0$, so the forward solution for $G_1(\vec S)$ is $\sum_\nu m_\nu(S_\nu)$, and
by (2.2) its coefficients are $\vec S$ ($\mathrm{Re}\,\lambda-\epsilon>\alpha''-2$): $T_{0,0} = \mathrm{id}$. *Near
$(0,0)$:* for fixed $\vec S$, $G_1$ at $(h_j,\vec p_j)$ tends to $G_1$ at $(0,0)$ in $\mathcal Y(\alpha'')$ (Lemma 2.6
(c) and (ii) at $\alpha'$), and the forward solutions are bounded in (4.2) at $\alpha'$ ((i) at $\alpha'$), so Lemma 3.3
gives $T_{h_j,\vec p_j}\vec S\to\vec S$; on the finite-dimensional $\mathcal S_1^{\mathcal N}$, $T_{h,\vec p}$ is close
to the identity for $(h,\vec p)$ small, hence invertible. Put $\vec S := T_{h,\vec p}^{-1}C(0)$ and $\vec p\,'_{h,\vec
p,\alpha''}(F) := \vec p\,'_{h,\vec p,\alpha'}(F(\vec S))\oplus\vec S\in\mathcal P_{\alpha''}$. The source of (4.1) is
then $G(\vec S)$ (linearity of $D_{\vec p}P_3(h,\vec p)$ in the direction), whose solution $u(\vec S)$ has no term of
$\mathcal N$ in (3.1), so lies in (4.2) at $\alpha''$. *Uniqueness:* if $\vec p\,''\in\mathcal P_{\alpha''}$ also gives
(4.2) at $\alpha''$, with $\mathcal N$-part $\vec S''$, then its solution lies in (4.2) at $\alpha'$ with source $F(\vec
S'')-D_{\vec p}P_3(\vec q)$, $\vec q\in\mathcal P_{\alpha'}$, so $\vec q = \vec p\,'_{h,\vec p,\alpha'}(F(\vec S''))$ by
uniqueness at $\alpha'$, the solution is $u(\vec S'')$, and $C(\vec S'') = 0$ gives $\vec S'' = \vec S$. *(i), (ii)* at
$\alpha''$: linear by construction; uniform as $T_{h,\vec p}^{-1}$ and the maps of Lemma 3.2 are; and (ii) from
$T_{h_j,\vec p_j}\to\mathrm{id}$, Lemma 3.3 for $C(0)$ (with $F_j(0)$) and (ii) at $\alpha'$. $\square$

The source's statement has $f_2$ of $K^+$-weight $4+\epsilon_K$ and $h$ with $4+\epsilon_K$ orders of decay ((11.148));
here $\alpha<a_K$ is what the $b$-derivative needs (III.I$'''''''$ Lemma 3.1 (b)), and the remainder is
$\alpha-2-\epsilon$ for every $\epsilon$, the source's $\alpha_K-2$, since the step at $\iota^+$ takes $c_K = \alpha$ to
admit sources of $K^+$-weight exactly $\alpha$. Its index set $\tilde{\mathcal E}'_{++}$, built by the procedure after
its proof ((11.186)), is here fixed in advance by (1.1).

## 5. Findings, labels and sources

### 5.1 Findings

(I$''''''''$1) *The motions are extracted on spacetime.* At $n = 4$ the decaying centre-of-mass motions come only from
the s1 row of III.G$''$ Corollary 4.3 at the $\iota^+$-exponents $\lambda_0\in\mathcal M$, present exactly when
$\ell_K(\lambda_0) = \alpha_K-\mathrm{Re}\,\lambda_0>1$; the zero energy analysis gives none, as $\widehat{L_b}(0)$ has
no indicial root in $(0,1]$. So the source's reason to pass to the Fourier transform (its $\sigma^{\lambda-1}$-terms
from indicial roots, to be combined with the $\iota^+$-ones) does not arise, and Part III.I$'''''$'s step at $\iota^+$
reads the motions off directly. Their rates are $\mathrm{Re}\,\lambda-1\in[\lambda_\sharp-1,1)$, so they matter only for
$\alpha_K>\lambda_\sharp+1>\frac52$, which is why Part III.I$''''''$ could stop at $\frac52$.

(I$''''''''$2) *No proliferation of logarithms.* The $\iota^+$-normal operator has no pole below 2 (III.G$'$ Lemma 4.2
(a)), so Corollary 4.3 adds no logarithm, and re-solving at null infinity creates no exponent below $\frac52$ (III.I$'$
Proposition 3.1's last sentence), while the sources supported away from $\mathscr I^+$ are not re-solved there. So the
motion index set $\mathcal E_{++}$ is fixed in advance and closed ((1.1)), and the source's device $u_\Sigma$
((11.180)-(11.183)), and its Remark 11.52, are not needed: each level is a finite-dimensional map close to the identity
(Proposition 4.1's proof).

(I$''''''''$3) *The tf-iteration.* For $\alpha_K\ge2+\epsilon_{\mathrm{ind}}$ the remainder after the second zero energy
inversion has relative tf-zf order below 2, and III.G$''''$ Proposition 5.1 is applied finitely often (Step 3.4$'$),
each time moving the conormal s1 term into the $\mathcal S_1$-column by III.I$''''''$ Lemma 1.4; those terms are
$O(|\sigma|^{\alpha_i})$ in the $\mathcal S_1$-component with $\alpha_i>1$, so they decay faster than $t_*^{-1}$ — the
source's "inherits stronger decay" for its term (ii) of p. 262.

(I$''''''''$4) *Assumptions on $\mathcal E_+$.* The motion corrections have $\iota^+$-order $\lambda<2$, so $\mathcal
X$'s index set must contain $\mathcal E_{++}$ ((1.1)), as the source's (11.149) and (11.151) enlarge its index sets; at
$n = 4$ this means $\mathcal E_+\supset\mathcal E^\sharp_+\cap\{\mathrm{Re}<2\}$ and $\mathcal E_++(\mathcal
E^\iota_{\mathrm{ind}}\cup\mathcal E_{\mathrm{ind}}\cup\mathcal E_+)\subset\mathcal E_+$, compatible with III.I (1.3)
($\lambda_\sharp>1$).

(I$''''''''$5) *Origin of the motions.* As in the source's Remark 11.54, the motions come from quasi-homogeneous
$\iota^+$-terms that the formal solution at null infinity transports there; at $n = 4$ their least exponent is the
radiative $\lambda_\sharp$, so the slowest motion decays like $t_*^{-\frac12-(1-e_\Upsilon)\gamma_\Upsilon}$.

### 5.2 Labels

Proved: Lemmas 2.2, 2.4, 2.5, 2.6, 3.1, 3.2, 3.3 and Proposition 4.1, given the parts cited. Comparisons with the source
are commentary. READ: the source's statements quoted from pp. 262-273. Inputs: II.E Proposition 3.4; III.D Definition of
$\Box^\Upsilon$ (as in III.D$'''$ (1.3)); III.D$'''$ (1.3), Proposition 3.1 (2); III.F$'$ Proposition 2.3 (a); III.G$'$
Lemma 4.2 (a); III.G$''$ (4.3), (4.4), Theorem 4.2, Corollary 4.3; III.G$''''$ Proposition 5.1; III.H (3.1), Lemma 2.5
(c); III.I (1.2), (1.3), Proposition 4.1; III.I$'$ (3.2), Propositions 2.1, 3.1; III.I$''$ Lemmas 4.1, 4.2; III.I$''''$
section 1, (1.2), Lemma 2.2, Proposition 4.1 (1); III.I$'''''$ Proposition 2.1 and its Steps 1-2, (2.3); III.I$''''''$
Proposition 2.1 and its Steps 3-6, Lemmas 1.2-1.4; III.I$'''''''$ section 1, Definition 2.3, Lemmas 2.4, 2.5, 3.1,
section 4.

### 5.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 11.7 (pp. 262-273:
(11.148)-(11.186), Definitions 11.47-11.48, Lemma 11.49, Remarks 11.50, 11.52-11.54, Proposition 11.51). N1STAR-PROOF.md
10.45 (b) and 10.61 (b) (the deductions this part replaces).
