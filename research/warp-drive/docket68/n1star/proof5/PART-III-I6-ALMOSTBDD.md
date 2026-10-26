# Part III.I$'''''$. Almost boundedness, n = 4 ([Hin26] section 11.5)

*Status.* Written (D261). This part proves, at spatial dimension $n = 4$, [Hin26] section 11.5 (pp. 247-252): once the
boost term is eliminated (Part III.I$''''$), the forward solutions of the augmented linearised operator have
$K^+$-weight $\alpha_K-2$ for every $\alpha_K<2$, that is, they grow at most like $t_*^{2-\alpha_K}$ in compact spatial
sets, almost boundedly (Proposition 11.32).

*What n = 4 changes.* The scheme is the source's: improve the $K^+$-weight in steps, each step a run of Part
III.I$'''$'s argument with no boost term. Three things differ. The exponents that the formal solution at null infinity
leaves at $\iota^+$ begin at $\frac32+(1-e_\Upsilon)\gamma_\Upsilon$ (III.I$'$ (3.2)), not at the source's 1, and the
$\iota^+$-spectrum is empty below 2 (III.G$'$ Lemma 4.2 (a)), so the step at $\iota^+$ solves away finitely many
quasi-homogeneous terms with no pole. The zero energy step needs neither the source's Lemma 11.33 nor its Step 3.2 (its
Proposition 9.30): there is no indicial root of $\widehat{L_b}(0)$ in $(0,1]$ (III.F$'$ Proposition 2.3 (a)) and the
columns have tf-order $3-\epsilon$ (III.I$'''$ Lemma 1.2 (b)), so the relative tf-zf order stays in $(2,3)$. And the
$\iota^+$-weight of the solution is $\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+)-\epsilon$, the source's
$1-\epsilon$. Everything is at $b = b_0$. Notation: Parts III.C, III.F$'$, III.F$'''$, III.G$'$, III.G$''$, III.H and
III.I-III.I$''''$, with III.I$''''$ section 1; no instrument is used.

## 1. Setting

$L := L_{h,S}$ is the linearisation of Part III.I$''''$'s augmented operator $P_1$ at $(h,S,b_0)$, with $h\in\mathcal
X^\infty$ vanishing near $\{t^\flat_* = 1\}$, $\|h\|_{\mathcal X^d}$ and $|S|$ small, and (III.I$''''$ (2.4))
$$2+\mathcal E_{\mathrm{ind}}\subset\mathcal E_+.\tag{1.1}$$
By III.I$''''$ Lemma 2.5, $L = L^{g',g_0}$ with $g' = g_S+h'$, $h' = h^{(-1)}(S)+h$, so every result of Parts
III.I-III.I$'''$ holds for $L$. $\chi_K$ is III.B's cut-off and $h^{\le1}_\natural$ the re-centred state of III.I$''''$
Definition 1.1. Fix $\ell_I$ with III.I$''$ (5.1),
$$2\le\ell_I<\min(a_I+\tfrac12,\ell_I^{\max}),\qquad\ell_I\notin\mathrm{Re}\,\pi_1\mathcal
E^C_I\cup(\tfrac32+\sigma_\Upsilon),\tag{1.2}$$
$\ell_I^{\max} = \frac32+s_C$, $s_C = \gamma_C(1-e_C)(1-v_C)$ (III.I$'$ (1.1), III.G$'$ Lemma 1.1), and write
$\lambda_\sharp := \frac32+(1-e_\Upsilon)\gamma_\Upsilon$, the exceptional exponent of III.I$'$ Proposition 3.1. For
$f\in H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),\alpha_++2,\alpha_K}_{\mathrm b}(\Omega_*)^{\bullet,-}$ with
$1<\alpha_K<\min(a_K-1,\frac32)$ and $\alpha_+>\alpha_K$, III.I$''''$ Proposition 4.1 (1) writes the forward solution of
$Lu = f$ as $\chi_Kh^{\le1}_\natural(\dot S(f))+\tilde u$.

*Two inclusions of index sets.* (a) The $\mathscr I^+$-index sets of the $\iota^+$-analysis lie in those of III.I
Definition 1.1: $\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I} =
\bigcup_{s\in\sigma_\Upsilon}(\frac32+s,0)\subset\mathcal E^{\mathrm{tot}}_I$ (III.G$'$ (1.5), III.C (3.1)), so
$\mathcal E^C_{\iota^+,\mathscr I} = \mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}+1\subset\mathcal
E^{\mathrm{tot}}_I+1\subset\mathcal E^C_I$ (III.C Lemma 3.2 (c)), and the slot index sets $\mathcal E_s = \mathcal
E^C_{\iota^+,\mathscr I}\cup(\frac32+s,0)$ lie in III.C (3.2)'s for the same slots (III.G$'$ Definition 1.2 (2)). So
$H^{k,(\langle\mathcal E^C_{\iota^+,\mathscr I}\rangle,\ell_I),\cdot,\cdot}_{\mathrm b}\subset H^{k,(\langle\mathcal
E^C_I\rangle,\ell_I),\cdot,\cdot}_{\mathrm b}$. (b) $\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I}+2\subset\mathcal
E^{\mathrm{tot}}_I+2\subset\mathcal E^C_I+1$, so $H^{k,(\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr
I}+2,\ell_I+1),\cdot,\cdot}_{\mathrm b}\subset H^{k,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),\cdot,\cdot}_{\mathrm b}$
(III.I Definition 1.1 (2); $\mathcal F_{I,11}\supset\mathcal E^C_I+1$), with no $\rho_I^{z+1}$-term for
$\mathrm{Re}\,z<\frac52$.

## 2. Almost boundedness ([Hin26] Proposition 11.32 at n = 4)

**Proposition 2.1 ([Hin26] Proposition 11.32 at n = 4, at $b_0$).** Let $1<\alpha_K<\alpha_+<2$ and $f\in
H^{\infty,(\langle\mathcal E^C_I+1\rangle',\ell_I+1),\alpha_++2,\alpha_K}_{\mathrm b}(\Omega_*;S^2T^*)^{\bullet,-}$, and
suppose that $\dot S(f) = 0$ (III.I$''''$ Proposition 4.1 (1), for any admissible $K^+$-weight there). Then the forward
solution of $Lu = f$ satisfies
$$u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta_+,\alpha_K-2}_{\mathrm
b}(\Omega_*;S^2T^*)^{\bullet,-}\quad\text{for every }\beta_+<\min(\alpha_+,\tfrac32,\min\mathrm{Re}\,\mathcal
E_+),\tag{2.1}$$
continuously in $f$. In compact spatial sets $u$ grows at most like $t_*^{2-\alpha_K}$, and $\alpha_K$ may be taken
arbitrarily close to 2.

The source's (11.96)-(11.97) have $\iota^+$-weight $1-\epsilon$, $\mathscr I^+$-weight $3+\epsilon_I$, and a second
summand $f_2$ with $\iota^+$-index set $\tilde{\mathcal E}_++2\ni(3,0)$ and $K^+$-weight $2-\epsilon$. At $n = 4$ the
corresponding terms have $\iota^+$-order 4 (III.I$''''$ Lemma 3.2), above $\alpha_++2$, so one class suffices.

**Corollary 2.2 (the source's remark after Proposition 11.32).** For $f$ as in Proposition 2.1 but with $\dot S(f)$
arbitrary, and $\ell_I\le a_I$, the solution $u$ of III.I$''''$ Corollary 4.3 ($L u+f_{h,S}(S'') = f$, $S'' =
(S^{(-1)}_{h,S})^{-1}\dot S(f)$) satisfies (2.1).

*Proof.* $f-f_{h,S}(S'')$ lies in the space of Proposition 2.1: $f_{h,S}(S'')$ has $\mathscr I^+$-data $(\langle\mathcal
E^C_I+1\rangle',a_I+1)$, $\iota^+$-weight $4-\epsilon\ge\alpha_++2$ and vanishes near $K^+$ (III.I$''''$ Lemma 3.2). Its
$\dot S$ is $\dot S(f)-S^{(-1)}_{h,S}(S'') = 0$ (III.I$''''$ Corollary 4.3's proof). $\square$

*Proof of Proposition 2.1.* The proof raises the $K^+$-weight in steps. Suppose, for some $\alpha'_K\in(1,\alpha_K]$ and
$\beta'_+\in(1,\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+))$,
$$u\in H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\beta'_+,\alpha'_K-2}_{\mathrm
b}(\Omega_*)^{\bullet,-}.\tag{2.2}$$
*Start.* III.I$''''$ Proposition 4.1 (1) with $K^+$-weight $\alpha'_K\in(1,\min(a_K-1,\frac32,\alpha_K))$ (the space of
$f$ for $\alpha_K$ lies in that for $\alpha'_K$) gives $u = \chi_Kh^{\le1}_\natural(\dot S(f))+\tilde u = \tilde u$, so
(2.2) holds.

*Step 0 (the source's (11.98)-(11.100)).* III.I Proposition 4.1 (4.2) ($\frac32<\ell_I<a_I+\frac12$;
$\beta'_+<\min\mathrm{Re}\,\mathcal E_+$, so $\beta'_+\le\max(a_+,\min\mathrm{Re}\,\mathcal E_+)$ and
$\beta'_+<a_++\min\mathrm{Re}\,\mathcal E_+$) gives $(L-L_b)u$ the $\mathscr I^+$-data $(\langle\mathcal
E^C_I+1\rangle',\ell_I+1)$, the $\iota^+$-weight $\beta'_++2+m_+-\epsilon>4$ ($\beta'_+>1$, $m_+>1$; its index set
$2\mathcal E_++2$ has real parts $>4$) and the $K^+$-weight $\alpha'_K-2+a_K$. Put $\tilde\alpha_K :=
\min(\alpha'_K+a_K-2,\alpha_K)>\alpha'_K$, and fix
$$\alpha^\sharp_+\in(\tilde\alpha_K,\alpha_+),\qquad\alpha^\sharp_+\notin\mathrm{Re}\,\pi_1\mathcal
E^C_I\cup\{\lambda_\sharp\},\qquad\alpha^\sharp_+\ge\min(\alpha_+,\tfrac32)-\epsilon\tag{2.3}$$
for a given small $\epsilon>0$ (possible: the excluded set is finite below 2). Then $\alpha^\sharp_+\in(1,2)$,
$\alpha^\sharp_+-1\in(0,1)$, $\alpha^\sharp_+-\tilde\alpha_K\in(0,1)$, and
$$L_bu = f' := f-(L-L_b)u\in H^{\infty,(\langle\mathcal
E^C_I+1\rangle',\ell_I+1),\alpha^\sharp_++2,\tilde\alpha_K}_{\mathrm b}(\Omega_*)^{\bullet,-}.$$

*Step 1 (null infinity; the source's (11.101)).* III.I$'$ Proposition 3.1 with $\breve{\mathcal E}_+ := \emptyset$ and
$\breve\ell_+ := \alpha^\sharp_+$ ($\alpha^\sharp_+<2\le\ell_I$; (2.3)) gives $u_I$, vanishing on
$\{t_*<1\}\cup\{\rho_I>\frac12c_I\}$, with $\mathscr I^+$-data $(\langle\mathcal E^C_I\rangle,\ell_I)$ and
$\iota^+$-data $(\mathcal E^\sharp_+,\alpha^\sharp_+)$, and
$$f^\flat_0 := f'-L_bu_I\in H^{\infty,\ell_I+1,(\mathcal E^\sharp_++2,\alpha^\sharp_++2),\tilde\alpha_K}_{\mathrm
b}(\Omega_*)^{\bullet,-}.$$
$\min\mathrm{Re}\,\mathcal E^\sharp_+ = \lambda_\sharp$ (III.I$'$ (3.2) with $\breve{\mathcal E}_+ = \emptyset$;
$\min\mathrm{Re}\,\mathcal E^C_I>\frac32+2\gamma_\Upsilon>\lambda_\sharp$). If $\alpha^\sharp_+<\lambda_\sharp$,
$f^\flat_0$ has plain $\iota^+$-weight $\alpha^\sharp_++2$ and Step 2 is void; this is Part III.I$'''$'s case. Otherwise
$f^\flat_0$ has finitely many $\iota^+$-expansion terms below $\alpha^\sharp_++2$,
$$\chi_\iota t_*^{-\lambda-2}(\log t_*)^kf^{(\lambda,k)}_+,\qquad(\lambda,k)\in\mathcal
E^\sharp_+,\quad\lambda_\sharp\le\mathrm{Re}\,\lambda<\alpha^\sharp_+,\tag{2.4}$$
whose coefficients $f^{(\lambda,k)}_+\in H^{\infty,\ell_I+1}_{\mathrm b}(\iota^+)$ come from $L_bu_I$ ($f'$ has plain
$\iota^+$-weight) and so are supported in $\{\rho_I\le\frac12c_I\}$, away from $K^+$.

*Step 2 ($\iota^+$; the source's (11.102)-(11.104)).* Fix $\ell_K\in(\frac12,1)$ with $\ell_K\ne-\mathrm{Re}\,\mu$ for
the roots $\mu$ of III.G$''$ and $\ell_K\notin\mathrm{Re}\,\pi_1\mathcal E_K$ (finitely many exclusions;
$\ell_K<\ell_K^{\max}$). Let $F$ be the current source, initially $f^\flat_0$, and $c_0$ the least real part of its
$\iota^+$-exponents below $\alpha^\sharp_++2$, minus 2. For each $\lambda_0$ in its $\iota^+$-index set with
$\mathrm{Re}\,\lambda_0\in[c_0,c_0+\epsilon_{\mathrm{ind}})$ (finitely many), with $k$ the largest log power at
$\lambda_0$, apply III.G$''$ Corollary 4.3 to the terms of $F$ at $\lambda_0$, with $f' := 0$: its hypotheses hold, as
$\mathrm{Re}\,\lambda_0\ge\lambda_\sharp>1$; $l_0 = 0$, since $\mathrm{spec}_{\iota^+}(\bar
L)\subset\{\mathrm{Re}\,z\ge2\}$ (III.G$'$ Lemma 4.2 (a)) and $\mathrm{Re}\,\lambda_0<2$; $\ell_I<\frac32+s_C$,
$\ell_I\notin\mathrm{Re}\,\pi_1\mathcal E^{\mathrm{tot}}_{\iota^+,\mathscr I} = \frac32+\sigma_\Upsilon$ by (1.2), and
$\mathrm{Re}\,\lambda_0<2\le\ell_I$; and the coefficients lie in $H^{\infty,\ell_I+1,\ell_K-2-\epsilon}_{\mathrm
b}(\iota^+)$, vanishing near $K^+$. It gives $u_{\lambda_0}$, vanishing for $t_*<1$, with
$$u_{\lambda_0}\in\bigcap_{\epsilon>0}H^{\infty,(\langle\mathcal E^C_{\iota^+,\mathscr
I}\rangle,\ell_I),(\lambda_0,k)\cup(\lambda_0+\mathcal E_{\mathrm{ind}}+(0,k)),(\mathcal
E^{\mathrm{gr}}_K(\lambda_0)+(0,k),\ell_K-\epsilon)}_{\mathrm b},$$
and an error, the terms of $F$ at $\lambda_0$ minus $L_bu_{\lambda_0}$, in $H^{\infty,(\mathcal
E^{\mathrm{tot}}_{\iota^+,\mathscr I}+2,\ell_I+1),\lambda_0+2+\mathcal
E_{\mathrm{ind}}+(0,k),\lambda_0+\ell_K-\epsilon}_{\mathrm b}$. Here $\min\mathrm{Re}\,\mathcal
E^{\mathrm{gr}}_K(\lambda_0) = \mathrm{Re}\,\lambda_0-1$: the least exponent is that of $a_{\mathrm s1}\sim
t_*^{-\lambda_0+1}$ (III.G$''$ (4.2)), the others being that of $a_{\mathrm v1}\sim t_*^{-\lambda_0}$ and
$\lambda_0-\mu+j$, $j\ge0$, for the roots $\mu\in\mathcal W(\ell_K)$, which have $-\ell_K<\mathrm{Re}\,\mu\le0$
(III.G$''$ section 1). So $u_{\lambda_0}$ has $K^+$-weight $\min(\mathrm{Re}\,\lambda_0-1,\ell_K)-\epsilon>0>\alpha_K-2$
($\ell_K<\ell_K^{\max} = \min(3,2+2\gamma_Cv_C)$, III.G$''$ (1.1)), and the error has $K^+$-weight
$\mathrm{Re}\,\lambda_0+\ell_K-\epsilon>2>\alpha_K$.

The error's $\mathscr I^+$-expansion is removed by III.I$'$ Proposition 3.1 with $\breve{\mathcal E}_+ :=
\lambda_0+\mathcal E_{\mathrm{ind}}+(0,k)$ and $\breve\ell_+ := \alpha^\sharp_+$: by inclusion (b) of section 1 the
error lies in its space, and its $\mathscr I^+$-expansion has no $\rho_I^{z+1}$-term with $\mathrm{Re}\,z<\frac52$, so
by the last sentence of that proposition (with $C_0<\frac52$) neither $\lambda_\sharp$ nor any $z\in\pi_1\mathcal E^C_I$
with $\mathrm{Re}\,z<\frac52$ enters its $\mathcal E^\sharp_+$. The solution $u'_{\lambda_0}$ vanishes on
$\{t_*<1\}\cup\{\rho_I>\frac12c_I\}$, has $\mathscr I^+$-data $(\langle\mathcal E^C_I\rangle,\ell_I)$, and its
$\iota^+$-exponents below $\alpha^\sharp_+$ lie in $\lambda_0+\mathcal E_{\mathrm{ind}}+(0,k)$; the new error has plain
$\mathscr I^+$-weight $\ell_I+1$ and $\iota^+$-exponents below $\alpha^\sharp_++2$ in $\lambda_0+2+\mathcal
E_{\mathrm{ind}}+(0,k)$, real parts $\ge\mathrm{Re}\,\lambda_0+2+\epsilon_{\mathrm{ind}}$.

Replacing $F$ by $F-L_b(u_{\lambda_0}+u'_{\lambda_0})$ for all $\lambda_0$ of the window raises $c_0$ by at least
$\epsilon_{\mathrm{ind}}$ (the terms of $F$ above the window are untouched), keeps the plain $\mathscr I^+$-weight
$\ell_I+1$ and the $K^+$-weight $\tilde\alpha_K$, and the exponents that occur lie in $\mathcal E^\sharp_++\mathbb
N_0\mathcal E_{\mathrm{ind}}$, an index set with finitely many elements below 2. So after finitely many rounds
($c_0<\alpha^\sharp_+<2$, starting at $c_0\ge\lambda_\sharp$) no $\iota^+$-term below $\alpha^\sharp_++2$ is left. Let
$u_\iota$ be the sum of the $u_{\lambda_0}$ and $u'_{\lambda_0}$. By inclusion (a), $u_\iota\in
H^{\infty,(\langle\mathcal E^C_I\rangle,\ell_I),\lambda_\sharp-\epsilon,0}_{\mathrm b}(\Omega_*)^{\bullet,-}$, and
$$u^\flat := u-u_I-u_\iota:\qquad L_bu^\flat = f^\flat := f^\flat_0-L_bu_\iota\in
H^{\infty,\ell_I+1,\alpha^\sharp_++2,\tilde\alpha_K}_{\mathrm b}(\Omega_*)^{\bullet,-},\tag{2.5}$$
and $u^\flat$, vanishing for $t_*<1$, is the forward solution (II.E Proposition 3.4).

*Step 3 (spectral; the source's Step 3).* (2.5) is III.I$'''$'s $f^\flat$ (its Step 1) with $\tilde\alpha_K$ for
$\alpha_K$, and III.I$'''$ Proposition 2.1's Steps 2-3 apply with $(\alpha^\sharp_+,\tilde\alpha_K)$. They use
$\alpha_K$ only through the following, each of which holds for $\alpha^\sharp_+,\tilde\alpha_K\in(1,2)$ with
$\alpha^\sharp_+>\tilde\alpha_K$:

(i) (2.25a) and (2.26a) with $\beta_K = \tilde\alpha_K\in(1,2)\setminus\mathbb N$, one Taylor coefficient (of order
$0<\tilde\alpha_K-1<1$);

(ii) III.H Proposition 3.2 at the weight $\alpha^\sharp_+-3$ ($\alpha^\sharp_+-1\in(0,1)$), and III.I$''$ Lemma 4.2 at
III.H's weight with $\alpha+2 = \alpha^\sharp_+-\tilde\alpha_K\in(0,1)$;

(iii) in III.I$'''$ (2.6), the column terms $(N,3-\epsilon,1-\epsilon)$ and the commutator term lie in
$(\frac52-\epsilon,\alpha^\sharp_++1,\tilde\alpha_K-1)$, as $\alpha^\sharp_+<2-\epsilon$ and
$\tilde\alpha_K-1<1-\epsilon$ for $\epsilon$ small;

(iv) in Step 3.3, the remainder tf-weights $\tilde\alpha_K+1-\epsilon$, $\tilde\alpha_K+2-\epsilon$ exceed $2-\epsilon$,
$3-\epsilon$, and $1-\epsilon>\tilde\alpha_K-1$; in the first integration, III.I$''$ Lemma 3.1 with $\beta_K :=
\tilde\alpha_K-1\in(0,1)\subset(-1,1)\setminus\{0\}$, $\beta_K\le\alpha^\sharp_+-\frac12$, and the tf-weight
$3-\epsilon\ge\alpha^\sharp_++1$; in the second, III.I$''$ Lemma 2.1 (1) with the $K^+$-weight
$\tilde\alpha_K-2\in(-1,0)$, $\ne0$, and $\mathcal E_K = \{(-1,0)\}$.

So $u^\flat = u_{\mathrm{hi}}+u_{\mathrm{reg}}+u_{\mathrm{sing}}$ with (III.I$'''$ (2.8), (2.12)-(2.13))
$$u^\flat-\chi_Kt_*h(S_0)\in
H^{\infty,\min(\frac32,\alpha^\sharp_+)-3\epsilon,\min(\frac32,\alpha^\sharp_+)-4\epsilon,\tilde\alpha_K-2}_{\mathrm
b}(M'),$$
$S_0$ the $\mathcal S_1$-component of $\tilde L_b(0)^{-1}(\hat f^\flat(0),0,0)$. $u_I$ and $u_\iota$ have $K^+$-weights
$\infty$ and $0$, and $u$ has $K^+$-weight $\alpha'_K-2>-1$ by (2.2); so the coefficient $h(S_0)$ of $t_*$ in $u$ at
$K^+$ vanishes, and $S_0 = 0$ (III.F$'''$ Proposition 4.1 (1)). As in III.I$'''$ Step 3.4, replacing $t_*h$ by
$h^{\le1}$ costs nothing here.

*Step 4 (null infinity).* $u = u_I+u_\iota+u^\flat$ has $\iota^+$-weight $\ell'_+ :=
\min(\frac32,\alpha^\sharp_+,\lambda_\sharp)-4\epsilon = \min(\frac32,\alpha^\sharp_+)-4\epsilon$ and $K^+$-weight
$\tilde\alpha_K-2$. III.I$'$ Proposition 2.1 with $\ell_+ := \min(\ell'_+,\min\mathrm{Re}\,\mathcal E_+-\epsilon)$ (so
$\ell_+\notin\mathrm{Re}\,\pi_1\mathcal E_+$), exactly as in III.I$'''$ Step 4 (near $\mathscr I^+$, $Lu = f$), gives
the $\mathscr I^+$-data $(\langle\mathcal E^C_I\rangle,\ell_I)$. So (2.2) holds with
$(\tilde\alpha_K,\min(\ell'_+,\min\mathrm{Re}\,\mathcal E_+-\epsilon))$, and, $\epsilon$ being arbitrary and
$\alpha^\sharp_+\ge\min(\alpha_+,\frac32)-\epsilon$, with any $\beta'_+<\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal
E_+)$.

*Conclusion.* Each round raises $\alpha'_K$ to $\min(\alpha'_K+a_K-2,\alpha_K)$, $a_K>2$, so finitely many rounds reach
$\alpha_K$; this is (2.1). The growth: $K^+$-weight $\alpha_K-2$ and b-Sobolev embedding give $|u|\lesssim
t_*^{2-\alpha_K}$ in compact spatial sets. *Continuity:* every map of the rounds is linear and bounded between the
spaces above (III.I$''''$ Proposition 4.1 (1), III.I Proposition 4.1 (4.2), III.I$'$ Propositions 2.1, 3.1, III.G$''$
Corollary 4.3, and III.I$'''$'s Steps 2-3 with their continuity paragraph). $\square$

The source's Step 2 begins at $\lambda = 1$, where $\mathcal E^\sharp_+\ni(1,0)$ forces its Proposition 9.11 at $\lambda
= 1$ and a logarithm in $a_{\mathrm s1}$; at $n = 4$ the least exponent is $\lambda_\sharp>\frac32$ and $a_{\mathrm s1}$
is a power ((I$'''''$2)). The source's Step 3 needs the expansion (11.107b) of $\hat u_{\mathrm{reg},1}(0)$ over the
indicial roots in $(0,\alpha_+-1]$, its Lemma 11.33 for the columns, and its Step 3.2, because its relative tf-zf order
$1+\min\mathrm{Re}\,\mathcal E_{\mathrm{ind}}$ is below 2; at $n = 4$ none is needed ((I$'''''$3)).

## 3. Findings, labels and sources

### 3.1 Findings

(I$'''''$1) *The weights.* Proposition 11.32 holds at $n = 4$ with the $\iota^+$-weight
$\min(\alpha_+,\frac32,\min\mathrm{Re}\,\mathcal E_+)-\epsilon$, where the source's is $1-\epsilon$, the cap $\frac32$
again being the transport of the radiation order from $\mathscr I^+$ (III.I$''$ (I$''$1)). One source class suffices,
since the parameter derivatives have $\iota^+$-order 4.

(I$'''''$2) *The step at $\iota^+$.* It is needed at $n = 4$ only when $\alpha^\sharp_+\ge\lambda_\sharp =
\frac32+(1-e_\Upsilon)\gamma_\Upsilon$, which is why Part III.I$'''$ (with $\alpha_K<\frac32$) could omit it and this
part cannot. It solves away finitely many quasi-homogeneous terms with $\mathrm{Re}\,\lambda\in[\lambda_\sharp,2)$;
there is no pole of the $\iota^+$-normal operator there (III.G$'$ Lemma 4.2 (a)), so no logarithm is created, and
re-solving at null infinity creates no new exponent below $\frac52$ (III.I$'$ Proposition 3.1's last sentence), so the
iteration ends. The source starts at $\lambda = 1$ with a logarithm.

(I$'''''$3) *The zero energy step.* The source's Lemma 11.33, its normal operator argument (11.107) and its Step 3.2
(Proposition 9.30) are not needed: $\widehat{L_b}(0)$ has no indicial root in $(0,1]$ (III.F$'$ Proposition 2.3 (a)),
and with the columns of tf-order $3-\epsilon$ the relative tf-zf order of the remainder,
$\alpha^\sharp_+-\tilde\alpha_K+2$, lies in $(2,3)$ throughout.

### 3.2 Labels

Proved: Proposition 2.1 and Corollary 2.2, given the parts cited. Comparisons with the source are commentary. READ: the
source's statements quoted from pp. 247-252. Inputs: II.E Proposition 3.4; III.A section 4 ((2.25a), (2.26a)); III.C
(3.1)-(3.2), Definition 3.1, Lemma 3.2 (c); III.F$'$ Proposition 2.3 (a); III.F$'''$ Proposition 4.1 (1); III.G$'$
(1.5), Definition 1.2, Lemmas 1.1, 4.2 (a); III.G$''$ (4.2), Theorem 3.1, Corollary 4.3; III.H Proposition 3.2; III.I
Definition 1.1, Proposition 4.1; III.I$'$ (1.1), (3.2), Propositions 2.1, 3.1; III.I$''$ (5.1), Lemmas 2.1, 3.1, 4.2;
III.I$'''$ Proposition 2.1 and its proof, Lemma 1.2; III.I$''''$ section 1, (2.4), Lemmas 2.5, 3.2, Proposition 4.1,
Corollary 4.3.

### 3.3 Sources

[Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2: section 11.5 (pp. 247-252:
Proposition 11.32, Lemma 11.33, (11.96)-(11.115)). N1STAR-PROOF.md 10.45 (b) and 10.61 (b) (the deductions this part
replaces).
