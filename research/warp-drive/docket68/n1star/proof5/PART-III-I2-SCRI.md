# Part III.I$'$. Asymptotics and formal solutions at null infinity, n = 4 ([Hin26] section 11.2)

*Status.* Verified (D256: the hundred-and-seventh verifier; three major and two minor findings and eight nits seated, to
be read). Written (D253). This part proves, at spatial dimension $n = 4$, [Hin26] section 11.2 (pp. 226-231): the
partial polyhomogeneity at $\mathscr I^+$ of solutions of $L^{g,g_0}u = f$ without loss at $\iota^+$ (Proposition 11.14,
with Lemma 11.15), and formal solutions of $L_bu = f$ at $\mathscr I^+$ (Proposition 11.16).

*What n = 4 changes.* The leading part of the operator at $\mathscr I^+$ is $(X_+-X_I)(X_I-\frac32-\bar A)$ with the
constant lower-triangular $\bar A$ of III.C Lemma 4.2, for the dynamical operator as for $L_b$ (III.I Proposition 3.3):
the source's $A^h$, $B^h$ and its $h$-dependent coupling $(A^h)_{7,6}$ of the radiation field into the 11-component are
half an order lower and enter only through the error. So the first expansion exponent is $\frac32$ (the radiation field,
in $\slashed\pi_0$ only), $\pi_{11}u$ acquires no term at $\frac32$, and in the formal solutions one exceptional source
term ($\frac52+(1-e_\Upsilon)\gamma_\Upsilon$ in the 11-component) is solved away where the source has two ($2$ and
$2+(1-e_\Upsilon)\gamma_\Upsilon$). The $\mathscr I^+$-weights reach $\min(a_I+\frac12,\ell_I^{\max})$: $a_I+\frac12$
from the products with the coefficients of the error (the source's $3+\epsilon_I$ is this bound at $n = 3$), and
$\ell_I^{\max} = \frac32+(1-e_C)(1-v_C)\gamma_C$, the least indicial root of the $\pi_C$-slots ((I$'$2)). Notation:
Parts III.A, III.C, III.F and III.I; no instrument is used.

## 1. Setting and structure

On the region $U_I := [0,c_I]_{\rho_I}\times[0,1]_{\rho_+}\times\mathbb S^3$ with III.I's coordinates (3.1)
($\rho_+ = (t_*+1)^{-1}$, $\rho_I = (t_*+1)/|x|$; so $\{\rho_+ = 1\} = \{t_* = 0\}$), $c_I\in(0,1]$ small, weights are
listed at $(\mathscr I^+,\iota^+)$ and none at $K^+$ (as in the source). $L := L^{g,g_0}$ with $g_0 := g_{b_0,b,-S}$, $g
:= g_0+h$, $h\in\mathcal X^\infty$ small (III.I (1.4), Proposition 3.4). All functions below vanish for $t_*\le1$, so the
region $\{0\le t_*\le1\}$, where $h$ is extended arbitrarily, plays no role. Components are taken in the splitting
III.C (1.6), slots $1,\dots,7$, $\pi_C$ the first three; $\sigma_\Upsilon = \{0,(1-e_\Upsilon)\gamma_\Upsilon,
\gamma_\Upsilon,2\gamma_\Upsilon\}$ are the eigenvalues of $\bar A$ on slots 6, 4, 5, 7, and
$\lambda_C\in\gamma_C\{2(1-v_C), (1-v_C),(1-e_C)(1-v_C)\}$ those on slots 1-3 (III.C (4.3)). III.F section 1 takes
$(1-e_C)(1-v_C)\gamma_C>100$. Put
$$\ell_I^{\max} := \tfrac32+(1-e_C)(1-v_C)\gamma_C\ (>100).\tag{1.1}$$

**Lemma 1.1 (the structure; the source's (11.26) and (11.34)).** On $U_I$,
$$\rho_I^{-1}\rho_+^{-2}L = L_0+\tilde L,\qquad L_0 := (X_+-X_I)\big(X_I-\tfrac32-\bar A\big),\qquad
\tilde L\in\big(\rho_IC^\infty+H^{\infty,(\mathcal E^{\mathrm{tot}}_I-1,a_I-1),(\mathcal E_+,a_+)}_{\mathrm b}\big)
\mathrm{Diff}^2_{\mathrm b},\tag{1.2}$$
and for $L_b$ the same with $\tilde L\in\rho_I\mathrm{Diff}^2_{\mathrm b}$ (smooth coefficients). $X_+-X_I$ and
$X_I-\frac32-\bar A$ commute.

*Proof.* III.I Proposition 3.3 divided by $\rho_I\rho_+^2$, and III.I Lemma 3.2 with the frame change of III.C Lemma 1.3
for $L_b$. $\bar A$ is constant and $X_+$, $X_I$ commute. $\square$

The source's $L_0$ is
$-(\rho_I\partial_{\rho_I}-(I+A^h))(\rho_I\partial_{\rho_I}-\rho_+\partial_{\rho_+})+\rho_+^{-1}B^h$, with $\tilde
L\in(\rho_IC^\infty+H^{k-2,(\mathcal E^C_I-1,2+\epsilon_I),(\mathcal E_+,3+\epsilon_+)}_{\mathrm b})
\mathrm{Diff}^2_{\mathrm b}$, which gains $\min\mathrm{Re}(\mathcal E^C_I-1)>2\gamma_\Upsilon$; here $\tilde L$ gains
$\frac12$ (as $\min\mathrm{Re}\,\mathcal E^{\mathrm{tot}}_I = \frac32$) and $L_0$ has constant coefficients.

*Integration tools.* III.A Lemma 1.2 ([Hin26] Lemma 2.12: $(x\partial_x-z)u = f$ adds $(z,0)$ to the index set when
$\mathrm{Re}\,z\le\alpha$, for $\alpha\ne\mathrm{Re}\,z$), Lemma 3.1 ([Hin26] Lemma 2.22) and Lemma 3.2 ([Hin26] Lemma
2.23: $(x\partial_x-y\partial_y+z)u = f$, with $\alpha+\mathrm{Re}\,z>\beta$ and an a priori bound near $y = 1$). Here
$(x,y) = (\rho_I,\rho_+)$ when integrating forward from $\{\rho_+ = 1\}$ (where $u = 0$), and $(x,y) = (\rho_+,\rho_I)$
when integrating backward from $\{\rho_I = c_I\}$. Slot $j$ of $L_0u$ is
$$(L_0u)_j = (X_+-X_I)\Big(\big(X_I-\tfrac32-\bar A_{jj}\big)u_j-\sum_{i<j}\bar A_{ji}u_i\Big),\tag{1.3}$$
the couplings being at $(3,1)$, $(4,1)$, $(4,3)$, $(5,2)$, $(7,3)$, $(7,4)$ (III.C Lemma 4.2).

## 2. Partial polyhomogeneity at null infinity ([Hin26] Proposition 11.14, Lemma 11.15 at n = 4)

**Proposition 2.1 ([Hin26] Proposition 11.14 at n = 4).** Let $\mathcal E^C_I$, $\mathcal E_+$ be as in III.I
Definition 1.1. Let $\frac32<\ell_I<\min(a_I+\frac12,\ell_I^{\max})$, $\ell_+<\min(\ell_I,a_++\min\mathrm{Re}\,\mathcal
E_+)$, $\ell_+\notin\mathrm{Re}\,\pi_1\mathcal E_+\cup\mathrm{Re}\,\pi_1\mathcal E^{\mathrm{tot}}_I$,
$\ell_I\notin\frac32+\sigma_\Upsilon$. Suppose $u$ and $f$ vanish for $t_*\le1$, and
$$Lu = f\in H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),(\mathcal E_++2,\ell_++2)}_{\mathrm b},\qquad u\in
H^{\infty,\alpha_I,(\mathcal E_+,\ell_+)}_{\mathrm b}\tag{2.1}$$
for some $\alpha_I\in\mathbb R$. Then $u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal
E_+,\ell_+)}_{\mathrm b}$.

The source asks $\ell_+<\ell_I\le3+\epsilon_I$, its $3+\epsilon_I$ being the product bound $a_I$ at $n = 3$ ((I$'$2));
its exceptional roots $1+\sigma_\Upsilon$ ($\le1+2\gamma_\Upsilon$) can equal a small $\ell_I$, which its statement does
not exclude, and its $\pi_C$-roots $1+\lambda_C$ lie far above.

**Lemma 2.2 ([Hin26] Lemma 11.15 at n = 4).** Under the assumptions of Proposition 2.1,
$u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\alpha_+}_{\mathrm b}$ for every
$\alpha_+<\min(\alpha_I,\frac32,\ell_+,\min\mathrm{Re}\,\mathcal E_+)$.

*Proof.* Reducing $\alpha_I$ if necessary, $\alpha_I<\frac32$ and $u\in H^{\infty,\alpha_I,\alpha_+}_{\mathrm b}$
(2.2).

*Step 1 (the weight below $\frac32$).* Fix $\eta\in(0,\frac12)$ with $\alpha_I+\eta<\frac32$. By (1.2) and III.C Lemma
2.1 (the coefficient's $\mathscr I^+$-index set has $\min\mathrm{Re} = \frac12>\eta$; at $\iota^+$,
$\min\mathrm{Re}\,\mathcal E_+>0$), $\tilde Lu\in H^{\infty,\alpha_I+\eta,
\alpha_+}_{\mathrm b}$; and $\rho_I^{-1}\rho_+^{-2}f\in H^{\infty,\alpha_I+\eta,\alpha_+}_{\mathrm b}$, its $\mathscr
I^+$-index sets $\mathcal E^C_I$ and $\mathcal F_{I,11}-1$ having $\min\mathrm{Re}>\frac32$ and its $\iota^+$-data being
$(\mathcal E_+,\ell_+)$ with $\alpha_+<\min(\ell_+,\min\mathrm{Re}\,\mathcal E_+)$. So $L_0u\in H^{\infty,\alpha_I+\eta,
\alpha_+}_{\mathrm b}$. In slot 1, by (1.3), $(X_I-\frac32-\lambda)w = (L_0u)_1$ for $w := (X_+-X_I)u_1$ and the slot's
eigenvalue $\lambda$: III.A Lemma 1.2 in $\rho_I$ (with $\mathrm{Re}(\frac32+\lambda)>\alpha_I+\eta$, so no term is
added; the a priori hypothesis, on $\rho_I$ near $c_I$, away from $\mathscr I^+$, holds by (2.2)) gives $w\in
H^{\infty,\alpha_I+\eta,\alpha_+}_{\mathrm b}$. Then $(X_I-X_+)u_1 = -w$ with $u_1 = 0$ near $\{\rho_+ = 1\}$: III.A
Lemma 3.2 with $(x,y) = (\rho_I,\rho_+)$, $z = 0$, $E = F = \emptyset$, $\alpha = \alpha_I+\eta>\beta = \alpha_+$, gives
$u_1\in H^{\infty,\alpha_I+\eta,\alpha_+}_{\mathrm b}$. In slot $j>1$ the couplings $(X_+-X_I)\bar A_{ji}u_i$, $i<j$,
already improved, go to the right; the same two steps apply, as every eigenvalue satisfies
$\frac32+\lambda\ge\frac32>\alpha_I+\eta$. So (2.2) holds with $\alpha_I+\eta$, and iterating,
$u\in\bigcap_{\alpha_I<3/2}H^{\infty,\alpha_I,\alpha_+}_{\mathrm b}$ (2.3).

*Step 2 (the first expansion term).* Let $0<\eta<\min((1-e_\Upsilon)\gamma_\Upsilon,\frac12)$, the least nonzero element
of $\sigma_\Upsilon$ being $(1-e_\Upsilon)\gamma_\Upsilon$ (as $0<e_\Upsilon<1$). By
(2.3) and (1.2), $\tilde Lu$ and $\rho_I^{-1}\rho_+^{-2}f$ lie in $H^{\infty,\frac32+\eta,\alpha_+}_{\mathrm b}$. In
slots 1-5 and 7, whose eigenvalues exceed $\eta$, the two steps of Step 1 give membership at $\frac32+\eta$ (slot 7 by
the couplings $(7,3)$, $(7,4)$ from slots already improved; $\bar A_{76} = 0$). In slot 6 ($\slashed\pi_0$, eigenvalue
0), III.A Lemma 1.2 adds $(\frac32,0)$: $(X_+-X_I)\slashed\pi_0u\in
H^{\infty,((\frac32,0),\frac32+\eta),\alpha_+}_{\mathrm b}$, and III.A Lemma 3.2 ($E = \{(\frac32,0)\}$, $\alpha =
\frac32+\eta>\alpha_+$, $\frac32\ne\alpha_+$) gives $\slashed\pi_0u\in
H^{\infty,((\frac32,0),\frac32+\eta),\alpha_+}_{\mathrm b}$, the $\iota^+$-terms it adds lying above the weight
$\alpha_+<\frac32$. So
$$u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\alpha_I),\alpha_+}_{\mathrm b}\qquad\text{for every }\alpha_I<\tfrac32+
(1-e_\Upsilon)\gamma_\Upsilon,\tag{2.4}$$
with $\slashed\pi_0u$ carrying $(\frac32,0)$ and no other slot an expansion term below the weight. At $n = 3$ the
source's $u_{11}$ acquires $(1,0)$ here, from $(A^h)_{7,6}$ acting on $\slashed\pi_0u$ (its (11.29)); at $n = 4$ that
coupling is in $\tilde L$, and acting on $(\frac32,0)$ it gives $\mathscr I^+$-order $\ge2>\frac32+\eta$.

*Step 3 (the full expansion).* Suppose (2.4) holds for some $\alpha_I$, and let $0<\eta<\frac12$. Every slot of $u$ has
$\mathscr I^+$-index set in $\mathcal E^{\mathrm{tot}}_I$ (III.C Lemma 3.2 (c)), so by (1.2) and III.C Lemma 2.1 with
$(\mathcal E^{\mathrm{tot}}_I-1)+\mathcal E^{\mathrm{tot}}_I\subset\mathcal E^C_I$ (III.C Definition 3.1 (3)) and
$\mathcal E^{\mathrm{tot}}_I+1\subset\mathcal E^C_I$ (III.C Lemma 3.2 (a)), $\tilde Lu\in H^{\infty,(\mathcal
E^C_I,\alpha'),\alpha_+}_{\mathrm b}$ with $\alpha' := \min(\ell_I,\alpha_I+\eta)$ (the three inequalities of III.C
Lemma 2.1: $\alpha'<\alpha_I+\frac12$; $\alpha'\le\alpha_I+a_I-1$ as $a_I>\frac32$; and $\alpha'<(a_I-1)+\frac32 =
a_I+\frac12$, the coefficient's remainder at weight $a_I-1$, which has no expansion, against the least exponent
$\frac32$ of $u$: this is where $\ell_I<a_I+\frac12$ enters). The source term $\rho_I^{-1}\rho_+^{-2}f$ has $\mathscr
I^+$-index sets $\mathcal E^C_I$ (slots 1-6) and $\mathcal E^C_I\cup(\frac32+(1-e_\Upsilon)\gamma_\Upsilon,0)$ (slot 7)
at the weight $\ell_I$. Here $\alpha'$ is chosen off $\frac32+\sigma_\Upsilon$ (decreasing $\eta$; $\ell_I$ is off it by
hypothesis). Slots 1-3: the eigenvalues satisfy $\frac32+\lambda_C\ge\ell_I^{\max}>\ell_I\ge\alpha'$, so III.A Lemma 1.2
adds nothing and $(X_+-X_I)u_j\in H^{\infty,(\mathcal E^C_I,\alpha'),\alpha_+}_{\mathrm b}$; III.A Lemma 3.2 ($E =
\mathcal E^C_I$, $\alpha'>\alpha_+$, $\alpha_+\notin\mathrm{Re}\,\pi_1\mathcal E^C_I$ as $\alpha_+<\frac32$) gives
$u_j\in H^{\infty,(\mathcal E^C_I,\alpha'),
\alpha_+}_{\mathrm b}$, the $\iota^+$-index set it adds being above the weight $\alpha_+$. Slots 4, 5, 6: with the
couplings $(4,1)$, $(4,3)$, $(5,2)$ from slots 1-3 on the right, the eigenvalue $s\in\{(1-e_\Upsilon)\gamma_\Upsilon,
\gamma_\Upsilon,0\}$ adds $(\frac32+s,0)$: $u_{01}$, $\pi_{1/}u$, $\slashed\pi_0u$ lie in the classes of $\mathcal
E_{I,01}$, $\mathcal E_{I,1/}$, $\slashed{\mathcal E}_{I,0}$ at the weight $\alpha'$. Slot 7: the couplings $(7,3)$
(index set $\mathcal E^C_I$) and $(7,4)$ (index set $\mathcal E_{I,01}$), the source term's
$(\frac32+(1-e_\Upsilon)\gamma_\Upsilon, 0)$, and, through $\tilde L$, the $h$-dependent couplings, which land in
$\mathcal E^C_I$ (above); with the eigenvalue $2\gamma_\Upsilon$, III.A Lemma 1.2 gives $\mathcal
E^C_I\cup(\frac32+(1-e_\Upsilon)\gamma_\Upsilon,0)\cup(\frac32+ 2\gamma_\Upsilon,0) = \mathcal E_{I,11}$
($(1-e_\Upsilon)\gamma_\Upsilon\ne2\gamma_\Upsilon$). So (2.4) holds with $\alpha'$ for $\alpha_I$, in the class of
III.I Definition 1.1 (1); finitely many steps reach $\ell_I$. $\square$

*Proof of Proposition 2.1.* *Step 1 (the $\iota^+$-data, a weaker $\mathscr I^+$-weight).* Suppose $u\in
H^{\infty,(\langle\mathcal E^C_I\rangle,\alpha_I),(\mathcal E_+,\ell_+)}_{\mathrm b}$ for some $\alpha_I<\ell_+$ (or
$u\in H^{\infty,\alpha_I,(\mathcal E_+,\ell_+)}_{\mathrm b}$ when $\alpha_I<\frac32$; this holds for the given
$\alpha_I$). By (1.2), $\tilde Lu$ has $\mathscr I^+$-weight $\alpha_I+\eta$ for $\eta<\frac12$, with some index set,
and the $\iota^+$-data $(\mathcal E_+,\ell_+)$ ($\mathcal E_++\mathcal E_+\subset\mathcal E_+$; the product's remainder
needs $\ell_+<a_++\min\mathrm{Re}\,\mathcal E_+$, the coefficient's remainder at weight $a_+$ against $u$'s least
exponent). Integrate $L_0u =
\rho_I^{-1}
\rho_+^{-2}f-\tilde Lu$ slot by slot as in Lemma 2.2, except that the hyperbolic field is integrated backward from
$\{\rho_I = c_I\}$: III.A Lemma 3.2 with $(x,y) = (\rho_+,\rho_I)$, the a priori bound near $\{\rho_I = c_I\}$ being the
hypothesis $u\in H^{\infty,\cdot,(\mathcal E_+,\ell_+)}$ there (away from $\mathscr I^+$), needs $\ell_+>\alpha_I+\eta$
($\alpha+\mathrm{Re}\,z>\beta$) and $\alpha_I+\eta\notin\mathrm{Re}\,\pi_1\mathcal E_+$, and in the slot-by-slot step
III.A Lemma 1.2 in $\rho_I$ needs $\alpha_I+\eta$ off $\frac32+\mathrm{spec}\,\bar A$; decrease $\eta$ to ensure all
three. It gives $\iota^+$-data $(\mathcal E_+,\ell_+)$ and $\mathscr I^+$-index sets that are extended unions with
$\mathcal E_+$; but by Lemma 2.2 the $\mathscr I^+$-expansion of $u$ (determined by $u$ away from $\iota^+$) has
exponents only in $\langle\mathcal E^C_I\rangle$ up to the weight $\ell_I$, so the coefficients of all other terms
vanish. Hence the hypothesis holds with $\alpha_I+\eta$; finitely many steps give it for every $\alpha_I<\ell_+$.

*Step 2 (both).* Now integrate forward as in Lemma 2.2, from $\alpha_I<\ell_+$ close to $\ell_+$ up to $\ell_I$, keeping
the $\iota^+$-data $(\mathcal E_+,\ell_+)$: in III.A Lemma 3.2 with $(x,y) = (\rho_I,\rho_+)$, the source term's
$\mathscr I^+$-weight $\alpha_I+\eta$ exceeds $\ell_+$ ($\alpha+\mathrm{Re}\,z>\beta$ with $\beta = \ell_+$), and
$\ell_+\notin\mathrm{Re}\,\pi_1$ of the $\mathscr I^+$-index sets, which lie in $\mathcal E^{\mathrm{tot}}_I$ (a
hypothesis; these sets do not depend on the weight); also $\ell_+<\ell_I$ and $\ell_+\notin\mathrm{Re}\,\pi_1\mathcal
E_+$; the $\iota^+$-index sets it produces are extended unions of $\mathcal E_+$ with $\mathscr I^+$-index sets of
components of $u$, but $u$ has $\iota^+$-index set $\mathcal E_+$ by Step 1, so no other exponent occurs. After finitely
many steps, $u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I), (\mathcal E_+,\ell_+)}_{\mathrm b}$. $\square$

## 3. Formal solutions at null infinity ([Hin26] Proposition 11.16 at n = 4)

**Proposition 3.1 ([Hin26] Proposition 11.16 at n = 4).** Let $\mathcal E^C_I$ be as in III.I Definition 1.1 and
$\breve{\mathcal E}_+\subset\mathbb C\times\mathbb N_0$ an index set. Let $\breve\ell_+<\ell_I<\ell_I^{\max}$,
$\ell_I>\frac32$, with $\breve\ell_+,\ell_I\notin\mathrm{Re}\,\pi_1\mathcal E^C_I$ and
$\breve\ell_+,\ell_I\ne\frac32+(1-e_\Upsilon)
\gamma_\Upsilon$. Let $f\in H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),(\breve{\mathcal E}_++2,\breve\ell_++2)}
_{\mathrm b}$ vanish for $t_*<1$. Then there are an index set $\mathcal E^\sharp_+$ depending only on $\mathcal E^C_I$
and $\breve{\mathcal E}_+$, and $u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),(\mathcal E^\sharp_+,\breve\ell_+)}
_{\mathrm b}$ vanishing on $\{t_*<1\}\cup\{\rho_I>\frac12c_I\}$, with
$$f-L_bu\in H^{\infty,\ell_I+1,(\mathcal E^\sharp_++2,\breve\ell_++2)}_{\mathrm b}(\Omega_*;S^2T^*).\tag{3.1}$$
One can take $\mathcal E^\sharp_+ = \bigcup_{j\ge1}\mathcal E^{\sharp,(j)}_+$ with
$$\mathcal E^{\sharp,(1)}_+ := \breve{\mathcal E}_+\bar\cup\{(\tfrac32+(1-e_\Upsilon)\gamma_\Upsilon,0)\},\qquad
\mathcal E^{\sharp,(j+1)}_+ := \mathcal E^{\sharp,(j)}_+\bar\cup^{k(\mathcal E^C_I,z)+1}\{(z,0)\}\ \text{for each
}z\in\pi_1\mathcal E^C_I,\ m_j\le\mathrm{Re}\,z<m_j+1,\tag{3.2}$$
$m_j := \min\mathrm{Re}\,\mathcal E^C_I+j-1$ (only $\mathrm{Re}\,z\le\ell_I$ matters), where $E\bar\cup^m\{(z,0)\}$ is
III.A Lemma 1.2's extended union taken $m$ times: $E\cup\{(z,m-1)\}$ if $z\notin\pi_1E$, the log order at $z$ raised by
$m$ otherwise. (The proof's rounds take the windows $[\mu_j,\mu_j+1)$, $\mu_j\ge m_j$ the least real part left; the
union $\mathcal E^\sharp_+$ is the same.) If all $\rho_I^{z+1}(\log\rho_I)^k$ terms of $f$'s $\mathscr I^+$-expansion
vanish for $\mathrm{Re}\,z\le C_0$, these $z$ may be omitted from (3.2).

The source has $\mathcal E^{\sharp,(1)}_+ = \breve{\mathcal E}_+\cup\{(1,0)\}\cup\{(1+(1-e_\Upsilon)\gamma_\Upsilon,0)\}$
((11.33a)) and windows $j<\mathrm{Re}\,z\le j+1$; the $(1,0)$ comes from its Step 1, the radiation coupling, which
$n = 4$ does not have.

*Proof.* By Lemma 1.1, $\rho_I^{-1}\rho_+^{-2}L_b = L_0+\tilde L$, $\tilde L\in\rho_I\mathrm{Diff}^2_{\mathrm b}$. Let
$\chi = \chi(\rho_I)\in C^\infty_c([0,\frac12c_I))$ equal 1 near 0. By III.I Definition 1.1 (2) (III.C (5.1)), write
$$f = \chi\rho_I^{\frac52+(1-e_\Upsilon)\gamma_\Upsilon}f_{11}^\flat\,(dx^1)^2+\tilde f,\qquad f_{11}^\flat\in
H^{\infty,(\breve{\mathcal E}_++2,\breve\ell_++2)}_{\mathrm b}(\Omega_*\cap\mathscr I^+),\quad\tilde f\in
H^{\infty,(\mathcal E^C_I+1,\ell_I+1),(\breve{\mathcal E}_++2,\breve\ell_++2)}_{\mathrm b},$$
the 11-component's exceptional term ($\mathcal F_{I,11} = 1+(\mathcal
E^C_I\cup(\frac32+(1-e_\Upsilon)\gamma_\Upsilon,0))$; $z_1 :=
\frac32+(1-e_\Upsilon)\gamma_\Upsilon<\frac32+2\gamma_\Upsilon<\min\mathrm{Re}\,\mathcal E^C_I$ by III.C Definition 3.1
(2), so the split is clean).

*Step 1 (the exceptional term).* With $z_1 := \frac32+(1-e_\Upsilon)\gamma_\Upsilon$, try $v := \chi\rho_I^{z_1}u^\flat
(dx^1)^2$, $u^\flat = u^\flat(\rho_+,\omega)$. On slot 7, the last, $(X_I-\frac32-\bar A)$ acts by
$z_1-\frac32-2\gamma_\Upsilon = -(1+e_\Upsilon)\gamma_\Upsilon\ne0$ (no slot below it), and $(X_+-X_I)\rho_I^{z_1} =
\rho_I^{z_1}(X_+-z_1)$; so, where $\chi = 1$, $L_0v =
-(1+e_\Upsilon)\gamma_\Upsilon\rho_I^{z_1}((X_+-z_1)u^\flat)(dx^1)^2$, and $\rho_I^{-1}\rho_+^{-2}f$'s term is
$\rho_I^{z_1}\rho_+^{-2}f^\flat_{11}(dx^1)^2$. Solve
$$(X_+-z_1)u^\flat = -\big((1+e_\Upsilon)\gamma_\Upsilon\big)^{-1}\rho_+^{-2}f^\flat_{11},\qquad u^\flat = 0\ \text{near
}
\{\rho_+ = 1\},$$
on $\mathscr I^+$; III.A Lemma 1.2 in $\rho_+$ ($\breve\ell_+\ne z_1$; the right side vanishes for $t_*<1$, so the
solution vanishing at $\rho_+ = 1$ does too) gives $u^\flat\in H^{\infty,(\breve{\mathcal
E}_+\bar\cup\{(z_1,0)\},\breve\ell_+)}_{\mathrm b}(\Omega_*\cap\mathscr I^+)$. Then $f-L_bv$ has no $\rho_I^{z_1+1}$
term in slot 7: the remainder from $\tilde L$ is $\rho_I^{z_1+2}$ times $H^\infty$ functions of $\iota^+$-index set
$\mathcal E^{\sharp,(1)}_++2$, and $z_1+2\in\mathcal E^{\mathrm{tot}}_I+2\subset\mathcal E^C_I+1$ (III.C Lemma 3.2 (c));
the derivatives of $\chi$ are supported away from $\mathscr I^+$. So $f$ is reduced to
$$f\in H^{\infty,(F_I+1,\ell_I+1),(F_++2,\breve\ell_++2)}_{\mathrm b},\qquad F_I = \mathcal E^C_I,\quad F_+ =
\mathcal E^{\sharp,(1)}_+.\tag{3.3}$$

*Step 2 (the remaining terms).* Given (3.3), let $z\in\pi_1F_I$ with $\mathrm{Re}\,z<\min\mathrm{Re}\,F_I+1$ and
$\mathrm{Re}\,z\le\ell_I$, $k := k(F_I,z)$, and $\chi\rho_I^{z+1}(\log\rho_I)^kf^{(z+1,k)}$ the corresponding term of
$f$, $f^{(z+1,k)}\in H^{\infty,(F_++2,\breve\ell_++2)}_{\mathrm b}(\Omega_*\cap\mathscr I^+;S^2T^*)$. As $\mathrm{Re}\,z>
\frac32+2\gamma_\Upsilon$ (III.C Definition 3.1 (2)) and $\mathrm{Re}\,z\le\ell_I<\ell_I^{\max}$, $z\notin\frac32+
\mathrm{spec}\,\bar A$, so $z-\frac32-\bar A$ is invertible. Let $u^{(z,k)}$ solve
$$(z-\tfrac32-\bar A)(X_+-z)u^{(z,k)} = \rho_+^{-2}f^{(z+1,k)},\qquad u^{(z,k)} = 0\text{ for }t_*\le1;$$
by III.A Lemma 1.2 ($\breve\ell_+\ne\mathrm{Re}\,z$), $u^{(z,k)}\in
H^{\infty,(F_+\bar\cup\{(z,0)\},\breve\ell_+)}_{\mathrm b}(\Omega_*\cap\mathscr I^+)$. By (III.A (1.1) in $\rho_I$)
$$L_0\big(\rho_I^z(\log\rho_I)^ku^{(z,k)}\big) = \rho_I^z(\log\rho_I)^k\rho_+^{-2}f^{(z+1,k)}+\rho_I^z\sum_{k'<k}(\log
\rho_I)^{k'}\rho_+^{-2}f'^{(z+1,k')},$$
with explicit $f'^{(z+1,k')}\in H^{\infty,((F_+\bar\cup\{(z,0)\})+2,\breve\ell_++2)}_{\mathrm b}$, and $\tilde L$
applied to it gives $\rho_I^{z+1+j}(\log\rho_I)^{k''}$ terms, $j\ge1$, $k''\le k$, which lie in $F_I+1$ at $\mathscr
I^+$ beyond the current window ($z+j\in\mathcal E^C_I$ as $\mathcal E^C_I+1\subset\mathcal E^C_I$, III.C Lemma 3.2 (a);
$\tilde L$ has smooth coefficients, so the shifts are integers). Replacing $f$ by
$f-L_b(\chi\rho_I^z(\log\rho_I)^ku^{(z,k)})$ replaces $(F_I,F_+)$ by $(F_I\setminus\{(z,k)\},F_+\bar\cup\{(z,0)\})$;
repeating for $(z,k-1),\dots,(z,0)$ gives $(F_I\setminus\{(z,j)\}_{j\le k},F_+\bar\cup^{k+1}\{(z,0)\})$, the log order
at $z$ rising by one at each repetition through the extended union. Doing this for every such $z$ (finitely many, III.C
Lemma 3.2 (e)'s construction) replaces $F_I$ by $\{(z,k)\in F_I:\mathrm{Re}\,z\ge\min\mathrm{Re}\,F_I+1\}$ and $F_+$ by
the next set of (3.2). Finitely many rounds exhaust the terms with $\mathrm{Re}\,z\le\ell_I$, and the remainder has
$\mathscr I^+$-weight $\ell_I+1$ with no expansion, which is (3.1). The terms of $u$ vanish on $\{\rho_I>\frac12c_I\}$
by the cut-off and on $\{t_*<1\}$ by construction, and lie in the class of III.I Definition 1.1 (1): their $\mathscr
I^+$-exponents are those of $\mathcal E^C_I$ and $z_1$ in slot 7, $\mathcal E_{I,11}\ni(z_1,0)$. If $f$'s terms vanish
for $\mathrm{Re}\,z\le C_0$, the corresponding $u^{(z,k)}$ are 0. $\square$

## 4. Findings, labels and sources

### 4.1 Findings

(I$'$1) *No radiation coupling into the 11-component.* At $n = 4$ the $h$-dependent coupling $(A^h)_{7,6}$ is half an
order lower (III.C (C1)), so $\pi_{11}u$ acquires no $\frac32$-term (Lemma 2.2, Step 2), the formal solutions have one
exceptional term, and $\mathcal E^{\sharp,(1)}_+$ omits the source's $(1,0)$ (Proposition 3.1). This proves, in the
forward cone, N1STAR-PROOF.md 10.44's reading that the iteration's $\iota^+$-index set starts at
$\frac32+(1-e_\Upsilon)\gamma_\Upsilon$ when $\breve{\mathcal E}_+$ does not go lower.

(I$'$2) *The upper weights (D256).* The source's $\ell_I\le3+\epsilon_I$ is the product bound: its coefficients'
remainder at weight $2+\epsilon_I$ against $u$'s least exponent 1, $a_I-1+1$ with $a_I = 3+\epsilon_I$. At $n = 4$ it is
$\ell_I<a_I+\frac12$ (the least exponent being $\frac32$), as in III.I (I6); separately $\ell_I<\ell_I^{\max} =
\frac32+(1-e_C)(1-v_C)\gamma_C$ keeps $\ell_I$ below the $\pi_C$-roots, which the source states as
$3+\epsilon_I<1+(1-e_C)(1-v_C)\gamma_C$. At $\iota^+$ likewise $\ell_+<a_++\min\mathrm{Re}\,\mathcal E_+$. Proposition
2.1 also excludes $\ell_I\in\frac32+\sigma_\Upsilon$ (III.A Lemma 1.2's $\alpha\ne\mathrm{Re}\,z$) and
$\ell_+\in\mathrm{Re}\,\pi_1\mathcal E^{\mathrm{tot}}_I$ (III.A Lemma 3.2), conditions the source's Proposition 11.14
does not state.

(I$'$3) *The windows of (3.2)* are taken from $\min\mathrm{Re}\,\mathcal E^C_I$ upward in steps of 1, which is what the
induction uses; the source's $j<\mathrm{Re}\,z\le j+1$ relies on $\min\mathrm{Re}\,\mathcal E^C_I\in(1,2)$ at $n = 3$.

(I$'$4) *Extended unions (D256).* III.A Lemma 1.2 returns $E\bar\cup\{(z,0)\}$, raising the log order when $z\in\pi_1E$;
the source's (11.33a)-(11.33b) write $\cup$, which understates the log orders at $\iota^+$ when $\breve{\mathcal E}_+$
meets $z_1$ or $\pi_1\mathcal E^C_I$. (3.2) carries $\bar\cup$; the existence of $\mathcal E^\sharp_+$ is unaffected.

### 4.2 Labels

Proved: Lemmas 1.1, 2.2, Propositions 2.1, 3.1, given the parts cited. Comparisons with the source are commentary.
READ: the source's statements quoted from pp. 226-231. Inputs: III.A Lemmas 1.2, 3.1, 3.2 and (1.1); III.C Definitions
1.2, 3.1, 5.1, Lemmas 1.3, 2.1, 3.2, 4.2; III.F section 1; III.I Definition 1.1, (1.4), (3.1), Lemma 3.2, Propositions
3.3-3.4.

### 4.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 11.2 (pp. 226-231:
Proposition 11.14, (11.25)-(11.32), Lemma 11.15, Proposition 11.16, (11.33)-(11.37)). N1STAR-PROOF.md 10.44.
