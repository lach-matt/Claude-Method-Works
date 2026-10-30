# Part III.I$'''''''''$. Correction terms #4 and the operator, n = 4 ([Hin26] section 11.8 to Lemma 11.57)

*Status.* Proved (D274: verifier 116 read the repairs, correct; status synchronised with the README at D325). Verified
(D271: the hundred-and-fifteenth verifier; no major finding, two minor ones and seven nits seated, to be read). Written
(D270). This part proves, at spatial dimension $n = 4$, the opening of [Hin26] section 11.8 and its section 11.8.1 (pp.
273-277): the correction terms that undo the pure gauge terms of the $K^+$-expansion which decay no faster than
$t_*^{-2}$ (Definition 11.55), the gauge-fixed Einstein operator with all modification parameters (Definition 11.56),
and its linearisation in the new parameters (Lemma 11.57). Theorem 11.59, which uses them, is the next part,
III.I$''''''''''$.

*What n = 4 changes.* The scheme is the source's: for each pure gauge term of the $K^+$-expansion that decays no faster
than $t_*^{-2}$, a cut-off pure gauge tensor $m_\nu$, built from the generalised gauge 1-forms of III.D$'''$, with a
correction $h_\nu$ at the cut-off and a gauge counterterm $\vartheta_\nu$, so that the linearisation of the operator in
the new parameter is $L_{b_0}m_\nu$ exactly. Four things differ. (1) *The rows.* At $n = 4$ every $\iota^+$-exponent is
at least $\lambda_\sharp>\frac32$, so the exponent 1 does not occur: the source's logarithmic time reparametrisation ($A
= \log t_*$, (11.191)) and its exceptional parameters $V^{(1,0)}_1$, $S^{(0),(1,0)}_0$, $S^{(0),(1,0)}_2$,
$S^{(-\lambda^\Upsilon_{\mathrm sl,1}+1),(\lambda^\Upsilon_{\mathrm sl,1},0)}_l$, $S^{(-1),(2,0)}_3$, $V^{(-1),(2,0)}_2$
((11.192)) do not arise. The rows of III.G$''$ Table 1.1 that reach $K^+$-rate at most 2 are six: the boosts s1 (rate
$\lambda-1$), the rotations v1, the time translation s0 and the s2 row at the root 0 (rate $\lambda$), and the class
roots of types s0 and s1 in $(-1,0)$ (rate $\lambda+d$, $0<d<1$); the rows at the root $-1$ of types s3 and v2, which
the source keeps at $\lambda = 1$, have rate above $\frac52$. (2) *Killing rotations.* The v1 parameters lie in a
complement of the rotations whose state vanishes, which at the non-rotating $b_0$ is 0 ((I$'''''''''$2)). (3) *An exact
linearisation.* $f^\nu = L_{h,\vec p}m_\nu+r^\nu$ with a remainder $r^\nu$ that vanishes at $(h,\vec p) = (0,0)$ and has
$\iota^+$-weight above $5+\epsilon_+$ with no index set (Lemma 2.6 (c)); this replaces the source's (11.194) and makes
the elimination of Part III.I$''''''''''$ a perturbation of the identity, as in III.I$''''''''$. (4) *The source
classes* record $\iota^+$-index sets up to weight $5+\epsilon_+$ (section 1), the analogue of the source's (11.195).
Everything is at $b = b_0$; the case $b\ne b_0$ is III.I$'''''''''''''''$ Theorem 3.1 (D330, verifier 146's n5).
Notation: Parts II.E, III.B, III.D$''$, III.D$'''$, III.G$''$, III.G$''''$, III.H, III.I-III.I$''''''''$; no instrument
is used.

## 1. Setting

Everything of III.I$''''''''$ section 1 is kept: $b = b_0$, $\mathfrak b$, the enlarged $\mathcal E_{\mathrm{ind}}$,
$\mathcal E^\iota_{\mathrm{ind}}$, $\mathcal E^\sharp_+$ and $\lambda_\sharp = \frac32+(1-e_\Upsilon)\gamma_\Upsilon =
\min\mathrm{Re}\,\mathcal E^\sharp_+$, the index set $\mathcal E_{++}$ with (1.1) there and $\mathcal M =
\{(\lambda,k)\in\mathcal E_{++}:\mathrm{Re}\,\lambda<2\}$ of (1.2) there, $\mathcal G = (2,0)\cup(2+\mathcal
E_{\mathrm{ind}})$, $\ell_I\le a_I$, the translated background III.I$'''''''$ (1.3), and III.I$''''$'s cut-offs,
$\mathcal C$, $\Theta$, conventions (1.2) and identities (i)-(iii). $\mathcal E_{\mathrm{ind}}$ is enlarged once more,
to contain also the index sets of III.D$'''$ Proposition 3.1 (1), (3) and (4)-(7) at $b_0$ (those of the towers of
section 2; there $\mathcal E_{\mathrm{ind}}$ changes from line to line) and $(2,0)$ (III.D$''$ (3.2)); III.I$''''''''$
(1.1), $\mathcal E_{++}$ and the conditions on $\mathcal E_+$ there are taken with the enlarged set, which only
strengthens them. Put $\mathcal F := (0,0)\cup\mathcal E_{\mathrm{ind}}$, $\tilde{\mathcal E}_+ := \mathcal
G\cup(\mathcal E_++\mathcal G)$ (III.I$''''$ (3.2)), $2\mathcal E_+ := \mathcal E_++\mathcal E_+$ (the product index set
of III.I Proposition 4.1 (4.2)), and
$$\delta_\sharp := \lambda_\sharp-\tfrac32>0,$$
in $(0,\frac14)$, as $0<e_\Upsilon<1$ and $0<\gamma_\Upsilon<\frac14$ (III.C (1.1)). Fix constants
$$0<\epsilon_K<\epsilon_+<\min(\delta_\sharp,\epsilon_{\mathrm{ind}}),\qquad w_+ := 5+\epsilon_+,\tag{1.1}$$
the source's (11.9) with $\delta_\sharp$ in place of $\epsilon_I$ ($\epsilon_{\mathrm{ind}}$ III.G$''''$ Proposition
5.1's). Part III.I$''''''''''$ may decrease them; every statement here holds for all smaller values.

*Hypotheses on the class $\mathcal X$* (the source's (11.148) and Remarks 11.61-11.62):

(H1) $a_+>\lambda_\sharp$ and $\mathcal E_+\subset\{\mathrm{Re}\ge\lambda_\sharp\}$; so $m_+ :=
\min(a_+,\min\mathrm{Re}\,\mathcal E_+) = \lambda_\sharp$, as $\mathcal E_+\supset\mathcal E_{++}\supset\mathcal
E^\sharp_+\cap\{\mathrm{Re}<2\}$.

(H2) $a_K\ge4+\epsilon_K$: $h$ has $4+\epsilon_K$ orders of decay at $K^+$.

(H3) is stated below, after the rows.

*The parameter exponents.* Fix an index set $\mathcal E_{\mathrm{par}}\subset\mathbb C\times\mathbb N_0$, closed under
conjugation, with
$$\min\mathrm{Re}\,\mathcal E_{\mathrm{par}}\ge\lambda_\sharp,\qquad\mathcal E_{\mathrm{par}}\cap\{\mathrm{Re}<2\} =
\mathcal M.\tag{1.2}$$
Part III.I$''''''''''$ fixes it (the source's $\tilde{\mathcal E}'_{++}$ of Definition 11.56, built after Theorem
11.59); here it is any such set.

*Rows.* The types are $\mathcal T := \{\mathrm{s1},\mathrm{v1},\mathrm{s0},\mathrm{s2},\mathrm{c0},\mathrm{c1}\}$: the
rows of III.G$''$ Table 1.1 at the roots $-1$ (s1, v1) and 0 (s0, s2) of $\widehat{L_{b_0}}(0)$, and its class roots
$\mu_{\mathrm c0} := 2-\lambda^\Upsilon_{\mathrm s0,2}$ (type s0) and $\mu_{\mathrm c1} := 2-\lambda^\Upsilon_{\mathrm
s1,2}$ (type s1). These are $\mu_{\mathrm s0}+1$ and $\mu_{1,0}+1$ for the class roots $\mu_{\mathrm
s0},\mu_{1,0}\in(-2,-1)$ of $\Box^\Upsilon$ in III.D$'''$ (R4), so $\mu_{\mathrm c0},\mu_{\mathrm c1}\in(-1,0)$ (Table
1.1 places them in $[-\frac{z_\Upsilon}3,0)$ and $(-\frac14,0)$). Put $d_{\mathrm s1} := -1$, $d_{\mathrm v1} =
d_{\mathrm s0} = d_{\mathrm s2} := 0$, $d_{\mathrm c0} := -\mu_{\mathrm c0}$, $d_{\mathrm c1} := -\mu_{\mathrm c1}$, so
$d_{\mathrm c0},d_{\mathrm c1}\in(0,1)$. A row is $\nu = (\tau,\lambda,k)$ with $\tau\in\mathcal T$ and
$(\lambda,k)\in\mathcal E_{\mathrm{par}}$; its $K^+$-exponent is $e_\nu := \lambda+d_\tau$, and
$$\mathcal N := \{\nu = (\tau,\lambda,k):\tau\in\mathcal T,\ (\lambda,k)\in\mathcal E_{\mathrm{par}},\
\mathrm{Re}\,e_\nu\le2\},$$
a finite set, with $\mathrm{Re}\,\lambda\le3$ on it. The row $\nu$ records the term $t_*^{-e_\nu}(\log t_*)^kh_\tau$
(Definition 2.1) that the $\iota^+$-exponent $(\lambda,k)$ produces at $K^+$ through III.G$''$ (4.3): the s1 and v1
terms through $a_{\mathrm s1}\sim t_*^{-\lambda+1}$ and $a_{\mathrm v1}\sim t_*^{-\lambda}$ of (4.2), the others through
$t_*^{-\lambda+\mu}$. The rows of Table 1.1 outside $\mathcal T$ have $\mu\le-1$ and are not the boost or rotation rows
(whose rates come from (4.2)), so $\mathrm{Re}(\lambda-\mu)\ge\lambda_\sharp+1>\frac52$, and need no correction. The s1
rows with $\mathrm{Re}\,\lambda<2$ are III.I$''''''''$'s motions: $\{(\mathrm{s1},\lambda,k):(\lambda,k)\in\mathcal M\}$.

(H3) $(\lambda,k)+\mathcal F\subset\mathcal E_+$ for every $(\tau,\lambda,k)\in\mathcal N$. For $\mathrm{Re}\,\lambda<2$
this holds by III.I$''''''''$ (1.1), as $\mathcal E_{++}+\mathcal E_{\mathrm{ind}}\subset\mathcal E_{++}\subset\mathcal
E_+$.

*Coefficient spaces.* $\mathcal W_{\mathrm s1} = \mathcal W_{\mathrm c1} := \mathcal S_1$, $\mathcal W_{\mathrm s0} =
\mathcal W_{\mathrm c0} := \mathcal S_0$, $\mathcal W_{\mathrm s2} := \mathcal S_2$, and $\mathcal W_{\mathrm v1} :=
\mathcal V'$, a fixed complement in $\mathcal V_1$ of
$$\mathcal V_K := \{V\in\mathcal V_1:\delta^*_{g_{b_0}}\omega^{(-1)}_{b_0,\mathrm v1}(V) = 0\},$$
the kernel of the state $h_{b_0,\mathrm v1}$ of III.D$''$ (3.4), which contains every $V$ whose rotation $R_V$ is
Killing for $g_{b_0}$ (III.D$''$ Proposition 3.1 (3)). At $b_0 = (\mu_0,0)$, the non-rotating member (III.B Proposition
3.4), every rotation is Killing, so $\mathcal V_K = \mathcal V_1$ and $\mathcal V' = 0$: the v1 rows are kept in the
notation and carry no parameter. $\mathcal W_{\tau,\mathbb C}$ is the complexification. The parameters are $\vec p =
(\vec p_{\le0},(W_\nu)_{\nu\in\mathcal N})$ with $\vec p_{\le0} = (S,b-b_0,S^{(0)}_1)$ as in III.I$'''''''$ and
$W_\nu\in\mathcal W_{\tau,\mathbb C}$, conjugation-symmetric: $W_{\bar\nu} = \overline{W_\nu}$ for $\bar\nu :=
(\tau,\bar\lambda,k)$, which lies in $\mathcal N$ ($\mathcal E_{\mathrm{par}}$ is closed under conjugation, $d_\tau$ is
real); so $W_\nu\in\mathcal W_\tau$ for real $\lambda$. $\mathcal P$ is the real vector space of these tuples. For $\nu
= (\mathrm{s1},\lambda,k)$ with $(\lambda,k)\in\mathcal M$, $W_\nu$ is III.I$''''''''$'s $S^{(\lambda-1,k)}_1$.

*Sources.* Let $\mathcal E_{\mathrm{rows}} := \bigcup_{(\tau,\lambda,k)\in\mathcal N}\big((\lambda,k)+\mathcal
F+((0,0)\cup\mathcal E_+)\big)$, and fix an index set $\mathcal E_{\mathrm{src}}$, closed under conjugation, with
$$\tilde{\mathcal E}_+\cup2\mathcal E_+\cup\mathcal E_{\mathrm{rows}}\subset\mathcal E_{\mathrm{src}},\qquad\mathcal
E_{\mathrm{src}}\cap\{\mathrm{Re}<2\}\subset\mathcal E_{++};\tag{1.3}$$
Part III.I$''''''''''$ may enlarge it within (1.3). The least choice satisfies the second condition: $\tilde{\mathcal
E}_+$ and $2\mathcal E_+$ lie in $\{\mathrm{Re}\ge2\}$ ((H1): $2\lambda_\sharp>3$), and an element of $\mathcal
E_{\mathrm{rows}}$ with real part below 2 has no $\mathcal E_+$-summand (which adds at least $\lambda_\sharp$ to
$\mathrm{Re}\,\lambda\ge\lambda_\sharp$), so it is $(\lambda,k)+(z,l)$ with $(\lambda,k)\in\mathcal M$ and
$(z,l)\in\mathcal F$, in $\mathcal E_{++}$ by III.I$''''''''$ (1.1). For $\alpha\in(2,4+\epsilon_K]$ let
$$\mathcal Y_1(\alpha) := \bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),((\mathcal
E_{\mathrm{src}})_{\ge2}+2,\,w_+-\epsilon),\alpha}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-},\qquad(\mathcal
E_{\mathrm{src}})_{\ge2} := \mathcal E_{\mathrm{src}}\cap\{\mathrm{Re}\ge2\},$$
$\mathcal Y_2(\alpha)$ the sections supported in $\mathrm{supp}\,\chi^\sharp_K$ (III.I (1.2)) lying in $\bigcap_\epsilon
H^{\infty,\infty,(\mathcal E_{\mathrm{src}}+2,\,w_+-\epsilon),\alpha}_{\mathrm b}$, and $\mathcal Y(\alpha) := \mathcal
Y_1(\alpha)+\mathcal Y_2(\alpha)$, real sections: the analogue of the source's (11.195). For $\alpha\in(2,3)$, $\mathcal
Y(\alpha)$ lies in III.I$''''''''$'s class of the same name: $\mathcal Y_1(\alpha)$ has plain $\iota^+$-weight
$4-\epsilon$, and the exponents of $\mathcal E_{\mathrm{src}}+2$ below 4 lie in $\mathcal E_{++}+2$ by (1.3). "$h$
small" means as in III.I$''''''''$. For complex $W$, $f^\nu(W)$ and $r^\nu(W)$ of Lemma 2.6 lie in $\mathcal
Y_2(\alpha)+i\mathcal Y_2(\alpha)$; the conjugation-symmetric sums over $\mathcal N$ are real and lie in $\mathcal
Y_2(\alpha)$.

## 2. Correction terms #4 and the operator ([Hin26] Definitions 11.55-11.56, Lemma 11.57 at n = 4)

*Towers.* Put $K_{\mathrm s1} = K_{\mathrm s0} := 4$, $K_{\mathrm v1} = K_{\mathrm s2} := 3$, $K_{\mathrm c0} =
K_{\mathrm c1} := 2$. For $\tau\in\mathcal T$ and $W\in\mathcal W_\tau$ let $\breve\omega^i_\tau(W)$, $0\le i\le
K_\tau$, be the following stationary 1-forms at $b_0$, linear in $W$ (extended complex-linearly to $\mathcal
W_{\tau,\mathbb C}$):

(s1) $\breve\omega^0 := \omega^{(0)}_{b_0,\mathrm s1}(S)$, $\breve\omega^1 := \breve\omega^{(0),1}_{b_0,\mathrm s1}(S)$
(III.D$''$ Proposition 3.1), $\breve\omega^i := \breve\omega^{(0),i}_{b_0,\mathrm s1}(S)$, $i = 2,3,4$ (III.D$'''$
Proposition 3.1 (2)): III.I$''''''''$ section 2's $\breve\omega^i(S)$;

(v1) $\breve\omega^0 := \omega^{(-1)}_{b_0,\mathrm v1}(V)$ (III.D$''$ Proposition 3.1), $\breve\omega^i :=
\breve\omega^{(-1),i}_{b_0,\mathrm v1}(V)$, $i = 1,2,3$ (III.D$'''$ (3));

(s0) $\breve\omega^0 := \omega^{(0)}_{b_0,\mathrm s0}(S)$, $\breve\omega^i := \breve\omega^{(0),i}_{b_0,\mathrm s0}(S)$,
$i = 1,\dots,4$ (III.D$'''$ (1)), with $\mathcal S_0 = \mathbb R$ acting by multiplication;

(s2) $\breve\omega^0 := \omega^{(-1)}_{b_0}(S)$ and $\breve\omega^i := \breve\omega^{(-1),i}_{b_0}(S)$, $i\le3$, of
III.D$'''$ (4)-(7) at the sl root $-l+1 = -1$, $l = 2$, of (R4), whose range is $K = 5-l = 3$;

(c0) the same at the s0 class root $\mu_{\mathrm s0} = \mu_{\mathrm c0}-1$, range $K = 2$; (c1) the same at the s1 class
root $\mu_{1,0} = \mu_{\mathrm c1}-1$, range $K = 2$.

In every case $\omega^{\le k}_\tau := \sum_{i\le
k}\frac{k!}{(k-i)!}t_*^{k-i}\breve\omega^i_\tau\in\ker\Box^\Upsilon_{b_0}$ for $k\le K_\tau$ (III.D$'''$ Proposition
3.1, in its convention, as in III.I$''''''''$ section 2), $\Box^\Upsilon_{b_0} =
2\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}\delta^*_{g_{b_0}}$. Near infinity in $\bar X$,
$$\breve\omega^i_\tau\in\mathcal A^{(\sigma_\tau-i,0)+\mathcal F},\qquad\sigma_{\mathrm s1} = \sigma_{\mathrm s0} :=
0,\quad\sigma_{\mathrm v1} = \sigma_{\mathrm s2} := -1,\quad\sigma_{\mathrm c0} := \mu_{\mathrm
c0}-1,\quad\sigma_{\mathrm c1} := \mu_{\mathrm c1}-1:\tag{2.1}$$
for s1 by III.I$''''$ section 1 and III.D$'''$ (2) (as in III.I$''''''''$ Lemma 2.2's proof); for v1 by III.D$''$ (3.2)
($\omega^{(-1)}_{b_0,\mathrm v1}(V)-V\in\mathcal A^{(2,0)+\mathcal F}$, the rotation 1-form $V$
homogeneous of degree 1) and III.D$'''$ (3); for s0 as $\omega^{(0)}_{b_0,\mathrm s0} = g_{b_0}(\partial_{t_*},\cdot)$
differs from a form with constant Cartesian components by $\rho^2C^\infty$ (III.D$''$ (3.1)-(3.2)),
$\breve\omega^{(0),1}_{b_0,\mathrm s0}-\chi_\partial\bar W\in\mathcal A^{(1,0)+\mathcal E_{\mathrm{ind}}}$ with $\bar W$
homogeneous of degree 1, and III.D$'''$ (1) for $i\ge2$; for s2, c0, c1 by III.D$'''$ (4)-(7). The *states* are
$$h_\tau(W) := \delta^*_{g_{b_0}}\breve\omega^0_\tau(W)\quad(\tau\ne\mathrm{s0}),\qquad h_{\mathrm s0}(S) :=
h^{(0)}_{b_0,\mathrm s0}(S) = \delta^*_{g_{b_0}}\omega^{(0),\le1}_{b_0,\mathrm s0}(S)\ \text{(III.D$'''$ (3.1))};$$
so $h_{\mathrm s1}(S) = h(S)$, $h_{\mathrm v1} = h_{b_0,\mathrm v1}$ of III.D$''$ (3.4), which vanishes on $\mathcal
V_K$, and for s2, c0, c1, $h_\tau = h^{(\mu+1)}_{b_0}$ of III.D$'''$ (4)-(7). $\omega^{(0)}_{b_0,\mathrm s0}$ is
Killing: $\delta^*_{g_{b_0}}\omega^{(0)}_{b_0,\mathrm s0} = 0$ (III.D$''$ Proposition 3.1 (2)).

**Definition 2.1 ([Hin26] Definition 11.55 at n = 4).** For $\nu = (\tau,\lambda,k)\in\mathcal N$ let $r_\nu(t_*) :=
t_*^{-e_\nu}(\log t_*)^k$ (on $\Omega_*$, $t_*\ge1$) and $a_\nu := r_\nu$ for $\tau\ne\mathrm s0$, while for $\tau =
\mathrm s0$
$$a_\nu(t_*) := A_\nu(t_*) := (-1)^k\partial_\lambda^k\Big(\frac{t_*^{1-\lambda}}{1-\lambda}\Big),\qquad\text{so }A_\nu'
= r_\nu$$
(the source's (11.190); $\lambda\ne1$ as $\mathrm{Re}\,\lambda\ge\lambda_\sharp$). For $W\in\mathcal W_{\tau,\mathbb C}$
put
$$\omega_\nu(W) := \sum_{i=0}^{K_\tau}a_\nu^{(i)}(t_*)\,\breve\omega^i_\tau(W),\qquad m_\nu(W) :=
\chi_K\delta^*_{g_{b_0}}\omega_\nu(W),\qquad h_\nu(W) := -[\delta^*_{g_{b_0}},\chi_K]\omega_\nu(W) =
-d\chi_K\otimes_s\omega_\nu(W),$$
$$\vartheta_\nu(W) := \delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}m_\nu(W),\qquad\vartheta_{\nu,\sharp}(W) :=
\vartheta_\nu(W)-\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}h_\nu(W),$$
the last the counterterm of the source's Remark 11.27, as in III.I$''''$, III.I$'''''''$, III.I$''''''''$. For $\nu =
(\mathrm{s1},\lambda,k)$ with $(\lambda,k)\in\mathcal M$ these are III.I$''''''''$ Definition 2.1's $m_{\lambda,k}$,
$h^{(\lambda-1,k)}_{\mathrm s1}$, $\vartheta^{(\lambda-1,k)}_{\mathrm s1}$, $\vartheta^{(\lambda-1,k)}_{\mathrm
s1,\sharp}$ ($a_\nu = t_*^{-\lambda+1}(\log t_*)^k$). The source indexes its tensors by the $K^+$-rate (its footnote
123); here the index is the $\iota^+$-exponent $\lambda$, with the rate $e_\nu$ recorded, as its footnote 124 does for
the class-root parameters. Since $a_{\bar\nu} = \overline{a_\nu}$ and the $\breve\omega^i_\tau$ are real on $\mathcal
W_\tau$, $m_{\bar\nu}(\overline W) = \overline{m_\nu(W)}$, and likewise for $h_\nu$, $\vartheta_\nu$,
$\vartheta_{\nu,\sharp}$.

**Lemma 2.2 ([Hin26] Definition 11.55's memberships and (11.187)-(11.189) at n = 4).** Let $\nu =
(\tau,\lambda,k)\in\mathcal N$, $W\in\mathcal W_{\tau,\mathbb C}$, $a := a_\nu$ and $K := K_\tau$.

(a) There are stationary operators $A_1,A_2$ with
$$\Box^\Upsilon_{b_0}\,\omega_\nu(W) =
a^{(K+1)}\big(A_1\breve\omega^K_\tau+A_2\breve\omega^{K-1}_\tau\big)+a^{(K+2)}A_2\breve\omega^K_\tau.\tag{2.2}$$

(b) Near $(\iota^+)^\circ$: $\omega_\nu(W)\in\mathcal A^{(\lambda-1,k)+\mathcal F}$; $m_\nu(W),h_\nu(W)\in\mathcal
A^{(\lambda,k)+\mathcal F}$; $\vartheta_\nu(W),\vartheta_{\nu,\sharp}(W)\in\mathcal A^{(\lambda+1,k)+\mathcal F}$; and
$D_{g_0}\mathrm{Ric}(h_\nu(W))\in\mathcal A^{(\lambda+2,k)+\mathcal F}$ ($g_0$ as in III.I$''''$ Lemma 2.2).

(c) $h_\nu(W)$ is supported in $\mathcal C$; $m_\nu(W)$, $\vartheta_\nu(W)$, $\vartheta_{\nu,\sharp}(W)$ in
$\mathrm{supp}\,\chi_K$; all vanish for $t^\flat_*<10$.

(d) Near $K^+$, $\vartheta_{\nu,\sharp}(W) = \vartheta_\nu(W) = \frac12\Box^\Upsilon_{b_0}\omega_\nu(W)$, of
$K^+$-weight $\kappa_\nu-\epsilon$ for every $\epsilon>0$, where
$$\kappa_\nu := \mathrm{Re}\,\lambda+4\quad(\tau\in\{\mathrm{s1},\mathrm{v1},\mathrm{s0},\mathrm{s2}\}),\qquad\kappa_\nu
:= \mathrm{Re}\,\lambda+d_\tau+3\quad(\tau\in\{\mathrm{c0},\mathrm{c1}\});$$
in every case $\kappa_\nu>\lambda_\sharp+3 = \frac92+\delta_\sharp$.

(e) $m_\nu(W)-\chi_Kr_\nu h_\tau(W)$ has $K^+$-weight $\mathrm{Re}\,e_\nu+1-\epsilon$, and $m_\nu(W)$ has $K^+$-weight
$\mathrm{Re}\,e_\nu-\epsilon$, for every $\epsilon>0$.

(f) $h_\tau$ is injective on $\mathcal W_{\tau,\mathbb C}$.

All seminorms are $O(|W|)$.

*Proof.* (a) As III.I$''''''''$ (2.1): $\Box := \Box^\Upsilon_{b_0}$ is stationary and of second order in
$\partial_{t_*}$, so $\Box(\varphi(t_*)v) = \sum_{m=0}^2\varphi^{(m)}A_mv$ for stationary $v$, and $\Box\,\omega_\nu =
\sum_{j\le K+2}a^{(j)}B_j$, $B_j := \sum_mA_m\breve\omega^{j-m}_\tau$ ($\breve\omega^i_\tau := 0$ for $i<0$, $i>K$).
With $t_*^k$, $k\le K$, in place of $a$ this is $\Box\,\omega^{\le k}_\tau = 0$, whose $t_*^0$-coefficient is $k!B_k$;
so $B_j = 0$ for $j\le K$, and $B_{K+1}$, $B_{K+2}$ are as stated.

(b) Near $(\iota^+)^\circ$, $|x|\sim t_*\sim\rho_+^{-1}$, so $\breve\omega^i_\tau\in\mathcal
A^{(\sigma_\tau-i,0)+\mathcal F}$ there by (2.1), and $a^{(i)}\in\mathcal A^{(\lambda-1-\sigma_\tau+i,k)}$: for
$\tau\ne\mathrm s0$, $a^{(i)}$ is a combination of $t_*^{-e_\nu-i}(\log t_*)^j$, $j\le k$, and $e_\nu =
\lambda-1-\sigma_\tau$ (s1: $\lambda-1$; v1, s2: $\lambda$; c0, c1: $\lambda-\mu_\tau$); for s0, $A_\nu^{(i)}$ is a
combination of $t_*^{1-\lambda-i}(\log t_*)^j$, $j\le k$. So each term of $\omega_\nu$ lies in $\mathcal
A^{(\lambda-1,k)+\mathcal F}$. $\delta^*_{g_{b_0}}$, $\delta_{g_{b_0},E_\Upsilon}G_{g_{b_0}}$ and $D_{g_0}\mathrm{Ric}$
lie in $\rho_+\mathrm{Diff}^1_{\mathrm b}$, $\rho_+\mathrm{Diff}^1_{\mathrm b}$ and $\rho_+^2\mathrm{Diff}^2_{\mathrm
b}$ there, and $d\chi_K\in\rho_+C^\infty$ (III.I$''''$ section 1), which gives the orders, as in III.I$''''''''$ Lemma
2.2.

(c) Every derivative of $\chi_K$ is supported in $\mathcal C$, and $\mathrm{supp}\,\chi_K\subset\{t^\flat_*\ge10\}$
(III.I (1.2)); $\delta_{E_\Upsilon}Gh_\nu$ is supported in $\mathcal C\subset\mathrm{supp}\,\chi_K$.

(d) Near $K^+$, $\chi_K = 1$, so $h_\nu = 0$, $m_\nu = \delta^*\omega_\nu$ and $\vartheta_\nu =
\frac12\Box\,\omega_\nu$, which by (2.2) is $a^{(K+1)}$ and $a^{(K+2)}$ times stationary tensors smooth on compact
spatial sets. For $\tau\ne\mathrm s0$, $a^{(K+1)}$ has $K^+$-weight $\mathrm{Re}\,e_\nu+K+1-\epsilon$:
$\mathrm{Re}\,\lambda-1+5$ (s1), $\mathrm{Re}\,\lambda+4$ (v1, s2), $\mathrm{Re}\,\lambda+d_\tau+3$ (c0, c1); for s0,
$A_\nu^{(5)} = r_\nu^{(4)}$ has weight $\mathrm{Re}\,\lambda+4-\epsilon$. Since $\mathrm{Re}\,\lambda\ge\lambda_\sharp$
by (1.2) and $d_\tau>0$, $\kappa_\nu>\lambda_\sharp+3$.

(e) For stationary $v$, $\delta^*_{g_{b_0}}(\varphi(t_*)v) = \varphi\,\widehat{\delta^*}(0)v+\varphi'\,dt_*\otimes_sv$
(III.I$''''$ (1.2)). For $\tau\ne\mathrm s0$ the term of $\delta^*\omega_\nu$ without a derivative of $a$ is
$a\,\widehat{\delta^*}(0)\breve\omega^0_\tau = r_\nu h_\tau$, and every other term carries $a^{(j)}$, $j\ge1$, of
$K^+$-weight $\mathrm{Re}\,e_\nu+1-\epsilon$. For s0, $\widehat{\delta^*}(0)\breve\omega^0 = 0$ (Killing), the terms
carrying $A_\nu' = r_\nu$ are $r_\nu(dt_*\otimes_s\breve\omega^0+\widehat{\delta^*}(0)\breve\omega^1) = r_\nu
h^{(0)}_{b_0,\mathrm s0}$ (as $h^{(0)}_{b_0,\mathrm s0} = \delta^*(t_*\breve\omega^0+\breve\omega^1)$), and the others
carry $A_\nu^{(j)} = r_\nu^{(j-1)}$, $j\ge2$, of weight $\mathrm{Re}\,\lambda+1-\epsilon$. $h_\tau$ is stationary, which
gives the weight of $m_\nu$.

(f) s1: $h$ is injective by the rows of III.H (3.1) (III.I$'''''''$ section 1). v1: by the choice of $\mathcal V'$. s0:
$\mathcal S_0 = \mathbb R$ and $h^{(0)}_{b_0,\mathrm s0}$ has the nonzero leading term $\bar h^{(0)}_{\mathrm s0}$
(III.D$'''$ (1)). s2, c0, c1: $h_\tau(S)$ has the leading term $\widehat{\bar\delta^*}(0)\bar\omega$, nonzero for the
nonzero indicial solution $\bar\omega$ that $S\ne0$ gives (III.D$'''$ (4)-(7)). Complex-linear extension keeps
injectivity. $\square$

**Definition 2.3 ([Hin26] Definition 11.56 at n = 4).** For $\vec p = (\vec p_{\le0},(W_\nu)_{\nu\in\mathcal
N})\in\mathcal P$ small and $h$ small, with $g_0 := g_{\vec p_{\le0}}$ (III.I$'''''''$ (1.3)),
$$h_{\mathrm{tot}}(\vec p) := h^{\mathrm{III.I'''''''}}_{\mathrm{tot}}(\vec p_{\le0})+\sum_{\nu\in\mathcal
N}h_\nu(W_\nu),\qquad\vartheta_{\mathrm{tot}}(\vec p) := \vartheta^{\mathrm{III.I'''''''}}_{\mathrm{tot}}(\vec
p_{\le0})+\sum_{\nu\in\mathcal N}\vartheta_{\nu,\sharp}(W_\nu),$$
the first terms III.I$'''''''$ Definition 2.3's, and
$$P_4(h,\vec p) := \mathrm{Ric}(g')-\delta^*_{g_0,E_C}\Big(\Upsilon^{E_\Upsilon}(g',g_0)-\vartheta_{\mathrm{tot}}(\vec
p)\Big),\quad g' := g_0+h_{\mathrm{tot}}(\vec p)+h,\qquad L_{h,\vec p} := D_hP_4(\cdot,\vec p)\text{ at }h.\tag{2.3}$$
The sums are real by the conjugation symmetry (Definition 2.1). The formulas extend holomorphically to tuples $(W_\nu)$
near $\mathcal P$ without the symmetry; a derivative in one $W_\nu$, written $D_{\vec p}P_4(h,\vec p)(W_\nu = W)$, is
taken in that extension and is complex-linear in $W$. $P_4 = P_3$ (III.I$''''''''$ (2.3), with $S^{(\lambda-1,k)}_1 =
W_{(\mathrm{s1},\lambda,k)}$) where $W_\nu = 0$ for the rows outside $\{(\mathrm{s1},\lambda,k):(\lambda,k)\in\mathcal
M\}$, and $P_4 = P_2$ (III.I$'''''''$ (2.2)) where every $W_\nu = 0$.

**Lemma 2.4 (the row identity; [Hin26] (11.187)-(11.189) at n = 4).** For $\nu\in\mathcal N$ and $W\in\mathcal
W_{\tau,\mathbb C}$, $D_{\vec p}P_4(0,0)(W_\nu = W) = L_{b_0}(m_\nu(W))$, and $m_\nu(W)$, vanishing for $t^\flat_*<10$,
is its forward solution (II.E Proposition 3.4). The identities III.I$'''''''$ (2.3) hold for $P_4$.

*Proof.* At $\vec p = 0$, $g' = g_0 = g_{b_0}$; $g_0$ does not depend on $W_\nu$, and $\dot g' = h_\nu(W) =
\chi_K\delta^*\omega_\nu-\delta^*(\chi_K\omega_\nu) = m_\nu(W)-\zeta_\nu(W)$, $\zeta_\nu(W) :=
\delta^*_{g_{b_0}}(\chi_K\omega_\nu(W))$, by III.I$''''$ (1.2). By (ii), $D_1\Upsilon^{E_\Upsilon}(g_{b_0},g_{b_0}) =
-\delta_{E_\Upsilon}G$, so $DP_4 = D\mathrm{Ric}(\dot g')+\delta^*_{E_C}(\delta_{E_\Upsilon}G\dot
g'+\vartheta_{\nu,\sharp}(W))$; by (iii) $D\mathrm{Ric}(\zeta_\nu) = 0$, and
$\delta_{E_\Upsilon}Gh_\nu+\vartheta_{\nu,\sharp} = \vartheta_\nu = \delta_{E_\Upsilon}Gm_\nu$, so $DP_4 =
D\mathrm{Ric}(m_\nu)+\delta^*_{E_C}\delta_{E_\Upsilon}Gm_\nu = L_{b_0}m_\nu$. On the directions of $\vec p_{\le0}$, $P_4
= P_2$ at $W = 0$, which gives III.I$'''''''$ (2.3). $\square$

The identity is exact because the gauge term is the full $\delta_{E_\Upsilon}G$ of the cut-off pure gauge tensor, not a
commutator; (2.2) makes it decay to $K^+$-order $\kappa_\nu$, which is why the towers have length $K_\tau$. The source's
(11.187)-(11.189) are the same computation written as $L_{b_0}(\chi_K\delta^*\omega) =
-D\mathrm{Ric}([\delta^*,\chi_K]\omega)+\delta^*_{E_C}\delta_{E_\Upsilon}G(\chi_K\delta^*\omega)$.

**Lemma 2.5 (the linearisation in $h$).** Let $\vec p\in\mathcal P$ (with $b = b_0$) and $h$ be small. Then
$h_{\mathrm{tot}}(\vec p)\in\mathcal X^\infty$ with $\|h_{\mathrm{tot}}(\vec p)\|_{\mathcal X^k}\le C_k|\vec p|$,
$L_{h,\vec p} = L^{g',g_0}$, and III.I$'''''''$ Lemma 2.5 (b)-(c) hold for $L_{h,\vec p}$.

*Proof.* As III.I$'''''''$ Lemma 2.5 and III.I$''''''''$ Lemma 2.5: the new terms $h_\nu(W_\nu)$ are supported in
$\mathcal C$, whose closure meets $\partial M$ only in a compact subset of $(\iota^+)^\circ$, and lie in $\mathcal
A^{(\lambda,k)+\mathcal F}\subset\mathcal A^{\mathcal E_+}$ there by Lemma 2.2 (b) and (H3). $\square$

**Lemma 2.6 ([Hin26] Lemma 11.57 at n = 4).** Let $\vec p\in\mathcal P$ (with $b = b_0$) and $h\in\mathcal X^k$,
$k\ge5$, be small, and $\alpha\in(2,4+\epsilon_K]$.

(a) The derivatives $f^S_{h,\vec p}$, $f^b_{h,\vec p}$, $f^{\mathrm s1}_{h,\vec p}$ of $P_4$ in $S$, $b$, $S^{(0)}_1$
satisfy III.I$'''''''$ Lemma 3.1 up to a term $(\partial\delta^*_{g_0,E_C})\vartheta_{\mathrm{rows}}$,
$\vartheta_{\mathrm{rows}} := \sum_{\nu\in\mathcal N}\vartheta_{\nu,\sharp}(W_\nu)$, which lies in $\mathcal
Y_2(\alpha)$. For $h\in\mathcal X^\infty$: $f^S_{h,\vec p}$ and $f^{\mathrm s1}_{h,\vec p}$ lie in $\mathcal Y(\alpha)$,
and $f^b_{h,\vec p}$ in $\mathcal Y_2(\alpha)$.

(b) For $\nu = (\tau,\lambda,k)\in\mathcal N$ and $W\in\mathcal W_{\tau,\mathbb C}$, $f^\nu_{h,\vec p}(W) := D_{\vec
p}P_4(h,\vec p)(W_\nu = W)$ is supported in $\mathrm{supp}\,\chi_K$ and, for every $\epsilon>0$,
$$f^\nu_{h,\vec p}(W)\in H^{k-2,\infty,((\lambda+2,k)+\mathcal F+((0,0)\cup\mathcal
E_+),\,a_++\mathrm{Re}\,\lambda+2-\epsilon),\,\kappa_\nu-\epsilon}_{\mathrm b}(\Omega_*),$$
with norm $O(|W|)$; for $h\in\mathcal X^\infty$ it lies in $\mathcal Y_2(\alpha)$ and in III.I$''''''''$'s $\mathcal
Y_2(\alpha')$ for every $\alpha'\in(2,3)$.

(c) $f^\nu_{h,\vec p}(W) = L_{h,\vec p}m_\nu(W)+r^\nu_{h,\vec p}(W)$, where, with $\zeta_\nu(W) :=
\delta^*_{g_{b_0}}(\chi_K\omega_\nu(W)) = m_\nu(W)-h_\nu(W)$,
$$r^\nu_{h,\vec p}(W) = -\big(L_{h,\vec
p}-L_{b_0}\big)\zeta_\nu(W)+\big(\delta^*_{g_0,E_C}-\delta^*_{g_{b_0},E_C}\big)\vartheta_{\nu,\sharp}(W).\tag{2.4}$$
$r^\nu_{0,0} = 0$; $r^\nu_{h,\vec p}(W)$ is supported in $\mathrm{supp}\,\chi_K$, and for every $\epsilon>0$
$$r^\nu_{h,\vec p}(W)\in
H^{k-2,\infty,\,\mathrm{Re}\,\lambda+2+\lambda_\sharp-\epsilon,\,\mathrm{Re}\,e_\nu+a_K-\epsilon}_{\mathrm
b}(\Omega_*),\quad\text{with norm}\le C_\epsilon|W|\big(\|h\|_{\mathcal X^k}+|\vec p|\big).\tag{2.5}$$
In particular, for $h\in\mathcal X^\infty$, $r^\nu_{h,\vec p}(W)\in\mathcal Y_2(\alpha)$, each seminorm bounded by
$C|W|(\|h\|_{\mathcal X^{k'}}+|\vec p|)$ for some $k'$.

(d) All are linear in the direction (complex-linear in $W$), continuous in $(h,\vec p)$ with $h\in\mathcal X^k$, and at
$(0,0)$ given by III.I$'''''''$ (2.3) and Lemma 2.4.

*Proof.* (a) As III.I$''''''''$ Lemma 2.6 (a): III.I$'''''''$ Lemma 3.1's counts use $h_{\mathrm{tot}}$ only through
$g'-\eta\in H^{k,(\mathcal E_+,a_+)}_{\mathrm b}$ near $(\iota^+)^\circ$, which still holds (Lemma 2.5), and the
derivative in $S$, $b$ or $S^{(0)}_1$ falls on the row terms only through $\delta^*_{g_0,E_C}$, which depends on these
parameters through $g_0$, applied to $\vartheta_{\mathrm{rows}}$. That term is linear in the $W_\nu$ and supported in
$\mathrm{supp}\,\chi_K$; for $S$ and $S^{(0)}_1$ in $\mathcal C$, as $\partial g_0$ is supported in
$\mathrm{supp}(1-\chi_K)$ there (III.I$'''''''$ (1.3)). Near $(\iota^+)^\circ$ its order is at least
$\mathrm{Re}\,\lambda+4\ge\lambda_\sharp+4>w_+$: the derivative of $g_0$ has $\iota^+$-order 2 (III.I$'''''''$ Lemma 1.3
(c) for $S$, $S^{(0)}_1$; $\partial_bg_0 = \chi_K\dot g_{b_0}\in\mathcal A^{\mathcal G}$ for $b$, III.I$'''''''$ (1.1)),
$\delta^*_{g,E_C}\in\rho_+\mathrm{Diff}^1_{\mathrm b}$, and $\vartheta$ has order $\lambda+1$ (Lemma 2.2 (b)). Its
$K^+$-weight is $\kappa_\nu-\epsilon>\frac92+\delta_\sharp-\epsilon>4+\epsilon_K\ge\alpha$ for $\epsilon$ small (Lemma
2.2 (d), (1.1)). So it lies in $\mathcal Y_2(\alpha)$. Next, $f^S$ and $f^{\mathrm s1}$ satisfy III.I$''''$ (3.3)
(III.I$'''''''$ Lemma 3.1 (a)): $\mathscr I^+$-data $(\langle\mathcal E^C_I+1\rangle',a_I+1)$, contained in $\mathcal
Y_1$'s as $\ell_I\le a_I$; $\iota^+$-index set $(\tilde{\mathcal E}_+\cup2\mathcal E_+)+2\subset(\mathcal
E_{\mathrm{src}})_{\ge2}+2$ by (1.3) and $\min\mathrm{Re}(\tilde{\mathcal E}_+\cup2\mathcal E_+)\ge2$; remainder
$a_++2+\min(2,m_+)-\epsilon = a_++2+\lambda_\sharp-\epsilon$ by (H1), and $a_++2+\lambda_\sharp>2\lambda_\sharp+2 =
5+2\delta_\sharp>w_+$ by (1.1); $K^+$-weight $\infty$. So they lie in $\mathcal Y_1(\alpha)+\mathcal Y_2(\alpha)$. $f^b$
satisfies III.I$'''''''$ (3.1): it is supported in $\mathrm{supp}\,\chi_K$, with $\iota^+$-data $(\tilde{\mathcal
E}_++2,a_++4-\epsilon)$, $a_++4>w_+$, and $K^+$-weight $a_K\ge4+\epsilon_K\ge\alpha$ by (H2); so it lies in $\mathcal
Y_2(\alpha)$.

(b) $P_4$ depends on $W_\nu$ only through $h_\nu(W_\nu)$ in $g'$ (in $\mathcal C$) and $\vartheta_{\nu,\sharp}(W_\nu)$
in $\vartheta_{\mathrm{tot}}$ (in $\mathrm{supp}\,\chi_K$), linearly; so, with $h' := h_\nu(W)$,
$$f^\nu = D_{g'}\mathrm{Ric}(h')-\delta^*_{g_0,E_C}\big(D_1\Upsilon^{E_\Upsilon}(g',g_0)h'-\vartheta_{\nu,\sharp}(W)\big)
\tag{2.6}$$
$$\phantom{f^\nu} = D_{g'}\mathrm{Ric}(h')-\delta^*_{g_0,E_C}\big([D_1\Upsilon(g',g_0)-D_1\Upsilon(g_{b_0},g_{b_0})]h'
-\vartheta_\nu(W)\big)$$
by the definition of the counterterm and (ii). The counts are III.I$''''''''$ Lemma 2.6 (b)'s:
$D_{g'}\mathrm{Ric}\in\rho_+^2(C^\infty+H^{(\mathcal E_+,a_+)}_{\mathrm b})\mathrm{Diff}^2_{\mathrm b}$,
$\delta^*_{g_0,E_C}\in\rho_+\mathrm{Diff}^1_{\mathrm b}$, the bracket linear in $(g'-g_{b_0},g_0-g_{b_0})\in
H^{(\mathcal E_+,a_+)}_{\mathrm b}$ and their first derivatives, and Lemma 2.2 (b) give the $\iota^+$-data; near $K^+$
only $\delta^*_{g_0,E_C}\vartheta_\nu = \delta^*_{g_{b_0},E_C}\vartheta_\nu$ remains ($h' = 0$ and $g_0 = g_{b_0}$
there, III.I$'''''''$ (1.3) at $b = b_0$), of weight $\kappa_\nu-\epsilon$. For $\mathcal Y_2(\alpha)$: the index set
lies in $\mathcal E_{\mathrm{rows}}+2\subset\mathcal E_{\mathrm{src}}+2$ by (1.3); the remainder
$a_++\mathrm{Re}\,\lambda+2>2\lambda_\sharp+2>w_+$; $\kappa_\nu-\epsilon\ge\alpha$ as in (a). For III.I$''''''''$'s
$\mathcal Y_2(\alpha')$ (index set $\mathcal E_{++}+2$, remainder $4-\epsilon$): if $\mathrm{Re}\,\lambda<2$, then
$(\lambda,k)\in\mathcal M$ and $(\lambda,k)+\mathcal F+((0,0)\cup\mathcal E_+)\subset\mathcal E_{++}$ by III.I$''''''''$
(1.1); if $\mathrm{Re}\,\lambda\ge2$, every exponent has real part at least 4; and $\kappa_\nu-\epsilon>3$.

(c) $L_{h,\vec p} = L^{g',g_0} = D_{g'}\mathrm{Ric}-\delta^*_{g_0,E_C}D_1\Upsilon^{E_\Upsilon}(g',g_0)$ (Lemma 2.5;
III.B), so (2.6) reads $f^\nu = L_{h,\vec p}h_\nu+\delta^*_{g_0,E_C}\vartheta_{\nu,\sharp} =
L_{h,\vec p}m_\nu-L_{h,\vec p}\zeta_\nu+\delta^*_{g_0,E_C}\vartheta_{\nu,\sharp}$. At $(0,0)$, $L_{b_0}\zeta_\nu =
D_{g_{b_0}}\mathrm{Ric}(\zeta_\nu)+\delta^*_{g_{b_0},E_C}\delta_{E_\Upsilon}G\zeta_\nu =
\delta^*_{g_{b_0},E_C}(\vartheta_\nu-\delta_{E_\Upsilon}Gh_\nu) = \delta^*_{g_{b_0},E_C}\vartheta_{\nu,\sharp}$, by
(iii) and $\zeta_\nu = m_\nu-h_\nu$. Subtracting gives (2.4), and $r^\nu_{0,0} = 0$ as $g' = g_0 = g_{b_0}$ there.
$\zeta_\nu$ is supported in $\mathrm{supp}\,\chi_K$, equals $m_\nu$ near $K^+$ (weight $\mathrm{Re}\,e_\nu-\epsilon$,
Lemma 2.2 (e)), and lies in $\mathcal A^{(\lambda,k)+\mathcal F}$ near $(\iota^+)^\circ$ (Lemma 2.2 (b)), with seminorms
$O(|W|)$. *First term of (2.4).* Near $(\iota^+)^\circ$, $L^{g',g_0}-L^{g_{b_0},g_{b_0}}$ lies in
$\rho_+^2\mathrm{Diff}^2_{\mathrm b}$ with coefficients linear, with smooth bounded factors, in $g'-g_{b_0}$,
$g_0-g_{b_0}$ and their b-derivatives of order at most 2: the count of III.I Proposition 4.1 (4.2). There
$g_0-g_{b_0}\in\rho_+^2C^\infty$ with seminorms $O(|\vec p|)$ (III.I$'''''''$ Lemma 1.3 (c)), and $h_{\mathrm{tot}}(\vec
p)+h\in H^{k,(\mathcal E_+,a_+)}_{\mathrm b}$ with norm $O(|\vec p|+\|h\|_{\mathcal X^k})$ (Lemma 2.5); as
$(2,0)\in\mathcal E_+$ and $m_+ = \lambda_\sharp$ (H1), both lie in $\rho_+^{\lambda_\sharp-\epsilon}H^k_{\mathrm b}$.
So the first term lies in $\rho_+^{\mathrm{Re}\,\lambda+2+\lambda_\sharp-2\epsilon}H^{k-2}_{\mathrm b}$ near
$(\iota^+)^\circ$. Near $K^+$, $g_0 = g_{b_0}$ and $h_{\mathrm{tot}}(\vec p) = 0$ (every correction is supported in
$\mathcal C$: III.I$''''$ Lemma 2.2, III.I$'''''''$ Definition 2.3 at $b = b_0$, Lemma 2.2 (c)), so $L_{h,\vec
p}-L_{b_0} = L^{g_{b_0}+h,g_{b_0}}-L_{b_0}$ has coefficients of $K^+$-weight $a_K$ with norm $O(\|h\|_{\mathcal X^k})$
(III.I Proposition 4.1 (4.2)), and the first term has $K^+$-weight $\mathrm{Re}\,e_\nu+a_K-\epsilon$. $\zeta_\nu$
vanishes near $\mathscr I^+$; the weights combine at the corner of $\iota^+$ and $K^+$ as in III.I Proposition 4.1.
*Second term.* At $b = b_0$, $g_0-g_{b_0} = (1-\chi_K)\big((\psi_{-S^{(0)}_1}\circ\phi_{-S})^*g_{b_0}-g_{b_0}\big)$ is
supported in $\mathrm{supp}(1-\chi_K)$ and $\vartheta_{\nu,\sharp}$ in $\mathrm{supp}\,\chi_K$, so the term is supported
in $\mathcal C$, away from $K^+$ and $\mathscr I^+$. $\delta^*_{g,E_C}\in\rho_+\mathrm{Diff}^1_{\mathrm b}$ near
$(\iota^+)^\circ$ with coefficients depending smoothly on $g$ and its first derivatives (III.B Definition 6.1), so
$\delta^*_{g_0,E_C}-\delta^*_{g_{b_0},E_C}\in\rho_+^3\mathrm{Diff}^1_{\mathrm b}$ there with seminorms $O(|\vec p|)$, as
in (a); the term has $\iota^+$-order $\mathrm{Re}\,\lambda+4\ge\mathrm{Re}\,\lambda+2+\lambda_\sharp$. This gives (2.5).
Finally $\mathrm{Re}\,\lambda+2+\lambda_\sharp\ge2\lambda_\sharp+2 = 5+2\delta_\sharp>w_+$ by (1.1), and
$\mathrm{Re}\,e_\nu+a_K\ge\lambda_\sharp-1+4+\epsilon_K>\alpha$ by (H2) ($e_\nu\ge\lambda-1$); so $r^\nu\in\mathcal
Y_2(\alpha)$ when $h\in\mathcal X^\infty$, with the stated bounds (each seminorm of $H^{k''}$ uses $h\in\mathcal
X^{k''+2}$).

(d) Linearity is clear from (2.3); continuity as in III.I$'''''''$ Lemma 3.1 (c), $g'$ and $g_0$ depending smoothly on
$(h,\vec p)$ (III.I$'''''''$ Lemma 1.3 (a), Lemma 2.5); the values at $(0,0)$ are Lemma 2.4. $\square$

*Comparison with the source.* The source's Lemma 11.57 records the classes of the linearisations (the $K^+$-order
$\lambda+\mu+1+j-\epsilon$ of its footnote 125, which is $\kappa_\nu$ here: $j = K_\tau$ terms below the leading one,
except $j = K_{\mathrm s0}-1 = 3$ for s0, whose leading term is the $A_\nu'$-term) and, in (11.194), that the leading
$\iota^+$-part of $f^\nu$ is $\chi_\iota\bar L$ applied to the model of $m_\nu$. Lemma 2.6 (b)-(c) give the classes and
the exact form $f^\nu = L_{h,\vec p}m_\nu+r^\nu$, from which the $n = 4$ analogue of (11.194) in its $L_b$ form follows,
at a plain $\iota^+$-weight: $f^\nu-L_{b_0}m_\nu = (L_{h,\vec p}-L_{b_0})m_\nu+r^\nu$ has $\iota^+$-weight
$\mathrm{Re}\,\lambda+2+\lambda_\sharp-\epsilon$. The source's index set $(\lambda+2,k)+((0,0)\cup\mathcal
E_{\mathrm{ind}}\cup\mathcal E_+\cup\tilde{\mathcal E}'_{++})$ has here no $\tilde{\mathcal E}'_{++}$-term, the new
corrections lying in $\mathcal X$ by (H3) (the source's Remark 11.62). The source's (11.191), for the logarithmic s0
correction at $\lambda = 1$, has no analogue ((I$'''''''''$1)).

## 3. Findings, labels and sources

### 3.1 Findings

(I$'''''''''$1) *The rows at n = 4.* The least $\iota^+$-exponent is $\lambda_\sharp>\frac32$, so the corrections of
the source that exist because of the exponent 1 (the logarithmic time reparametrisation $A = \log t_*$ with its
(11.191), the first parameter of each group in (11.192), and the rows at the root $-1$ of types s3 and v2) are absent,
and six types remain, with $K^+$-rates $\lambda-1$ (s1), $\lambda$ (v1, s0, s2) and $\lambda+d_\tau$ (the class roots
c0, c1). No row needs a logarithm in its gauge function beyond those of $(\lambda,k)$ itself.

(I$'''''''''$2) *Killing rotations.* For $V\in\mathcal V_K$ the v1 term of III.G$''$ (4.3) has no $t_*^{-\lambda}$-part
at $K^+$: as $\delta^*\breve\omega^0_{\mathrm v1}(V) = 0$, its leading term carries $a_{\mathrm v1}'$, of rate
$\lambda+1>\frac52$. A parameter in $\mathcal V_K$ would correct nothing that needs correcting and would make the
finite-dimensional map of the elimination singular, so $\mathcal W_{\mathrm v1}$ is a complement $\mathcal V'$ of
$\mathcal V_K$. Here $b_0 = (\mu_0,0)$ is the non-rotating member (III.B Proposition 3.4), at which every rotation is
Killing (III.D$''$ Proposition 3.1 (3)), so $\mathcal V_K = \mathcal V_1$ and the v1 coefficient space $\mathcal V'$ is
0: the v1 rows carry no parameter. How the source treats the axis of a rotating $b_0$ in its $\mathcal V_1$ is not
needed here and was not read.

(I$'''''''''$3) *An exact linearisation with a conormal remainder.* $f^\nu = L_{h,\vec p}m_\nu+r^\nu$ holds exactly,
and $r^\nu$ carries a factor of $\iota^+$-order at least $\lambda_\sharp$ (from $h$, $h_{\mathrm{tot}}$ or
$g_0-g_{b_0}$), which lifts it from $\mathrm{Re}\,\lambda+2\ge\lambda_\sharp+2$ to at least $2\lambda_\sharp+2 =
5+2\delta_\sharp>w_+$, past every exponent that could create a row: no $\iota^+$-index set of $r^\nu$ needs to be
tracked. At $n = 3$ the same count gives $2+2 = 4<5$, and the source tracks the index set $\tilde{\mathcal E}'_{++}$
instead. So Part III.I$''''''''''$ can eliminate the rows as III.I$''''''''$ Proposition 4.1 does: the solution of
$L_{h,\vec p}u = F-\sum f^\nu(W_\nu)$ is $u = v-\sum m_\nu(W_\nu)$ with $L_{h,\vec p}v = F-\sum r^\nu(W_\nu)$.

(I$'''''''''$4) *The $K^+$-orders.* The gauge towers of III.D$'''$ have exactly the lengths needed: every counterterm
$\vartheta_\nu$ has $K^+$-order $\kappa_\nu>\frac92+\delta_\sharp$, above the $4+\epsilon_K$ that Theorem 11.59's
sources carry; the shortest towers (length 2, the class roots) are compensated by their larger rate $\lambda+d_\tau$.

(I$'''''''''$5) *Hypotheses on $\mathcal X$.* (H1)-(H3) are the $n = 4$ form of the source's (11.148) and Remarks
11.61-11.62: the strong $K^+$-decay of $h$ is needed for the $b$-derivative (Lemma 2.6 (a)) and for the $K^+$-weight of
$r^\nu$ (Lemma 2.6 (c), which needs $a_K>\alpha+1-\lambda_\sharp$; the source's $f^\nu$ has no such term, so its Remark
11.61 does not transfer verbatim); the new corrections must lie in $\mathcal X$, which asks $\mathcal E_+$ to contain
their index sets; and $a_+>\lambda_\sharp$ with $\min\mathrm{Re}\,\mathcal E_+ = \lambda_\sharp$ gives the gain $m_+ =
\lambda_\sharp$ behind (I$'''''''''$3).

(I$'''''''''$6) *The parameter derivatives of the counterterms.* The term $(\partial\delta^*_{g_0,E_C})\vartheta$
recorded by the D269 repair of III.I$''''''''$ Lemma 2.6 (a) is present for every row; its $K^+$-order $\kappa_\nu$
keeps the $b$-derivative in $\mathcal Y_2(\alpha)$ up to $\alpha = 4+\epsilon_K$.

### 3.2 Labels

Proved: Lemmas 2.2, 2.4, 2.5 and 2.6, given the parts cited. Comparisons with the source are commentary. READ: the
source's statements quoted from pp. 273-277. Inputs: II.E Proposition 3.4; III.B Definition 6.1; III.D$''$ Proposition
3.1 (3.1)-(3.4), (2)-(3); III.D$'''$ (R4), Proposition 3.1 (1)-(7), (3.1); III.G$''$ Table 1.1, (4.2), (4.3);
III.G$''''$ Proposition 5.1 ($\epsilon_{\mathrm{ind}}$); III.B Proposition 3.4; III.H (3.1); III.I (1.2), Proposition
4.1 (4.2); III.I$''''$ section 1, (1.2), (3.2), (3.3), Lemma 2.2; III.I$'''''''$ section 1, (1.1), (1.3), Lemma 1.3,
Definition 2.3, (2.3), Lemmas 2.5, 3.1; III.I$''''''''$ section 1, (1.1), (1.2), section 2.

### 3.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 11.8 to Lemma 11.57
(pp. 273-277: (11.187)-(11.194), Definitions 11.55-11.56, Lemma 11.57, footnotes 122-125; (11.9), (11.148), (11.195) and
Remarks 11.61-11.62 for the hypotheses). N1STAR-PROOF.md 10.45 (b) and 10.61 (b) (the deductions this part replaces).
