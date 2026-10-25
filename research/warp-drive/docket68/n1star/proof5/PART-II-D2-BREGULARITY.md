# Part II.D$'$. Microlocal regularity with b-regularity, and estimates tame in it, at n = 4

*Status.* Verified. Written out in full (D203). Read line by line by the eighty-fifth verifier, which re-derived Lemmas
2.1-2.5, the commutators of sections 3-6 and the assembly, and confirmed (D$'$1)-(D$'$2) at source. Its major finding,
that with the words of (2.2) the coupling at the horizon is not diagonal and its Hermitian part is indefinite for
$k\ge2$, is repaired by the form (2.2$'$) for commuting letters; its three minor findings (the form of $R^{(2)}$ in
(C2), the bound used in the tame assembly, half of (D$'$3)) and its nits are seated (D206). The part is labelled proved
once the next reader has confirmed them. This part proves, at spatial dimension $n = 4$, [Hin26c] section 7.2 (pp.
127-141): the global estimate of Part II.D with $k$ additional degrees of b-regularity (the source's Proposition 7.11),
its version tame in $k$, and the ingredients: commutators with b-vector fields near $\mathscr I^+$ (Lemma 7.12), and the
radial point and trapping estimates with b-regularity (Propositions 7.17 and 7.22, Lemmas 7.15-7.16 and 7.19-7.21). The
source is [Hin26c] = P. Hintz, arXiv:2606.28008v1 (printed page numbers). Part II.A (`PART-II-A-SETUP.md`) is cited as
II.A, Part II.B as II.B, Part II.C as II.C, Part II.C$'$ as II.C$'$ and Part II.D (`PART-II-D-REGULARITY.md`) as II.D.

*Method.* b-regularity is tested by commuting b-vector fields through $P$. For the elliptic and real principal type
estimates, II.A section 9 commutes a spanning set of b-vector fields; the commutators enter the commuted system below
principal order, where those estimates do not see them. At a radial set or at the trapped set the subprincipal symbol of
the commuted system enters the threshold. There one uses families of commutator fields whose commutators with $P$ either
decay at the face carrying the set, or contribute with the favourable sign, so that the commuted system has the threshold
of $P$. Section 2 writes the commuted system for an arbitrary family and proves, once, that the estimate for it gives the
estimate with b-regularity, and its tame version (Lemmas 2.3-2.4). The estimates of II.D hold for the commuted systems
(Lemma 2.5). Sections 3-6 supply the families: near $\mathscr I^+$, at the horizon, over $\partial K^+$ and at the
trapped set. Section 7 proves the global estimate.

*How it is organised.* Section 1: the setting and Theorem 1.1. Section 2: the commuted system, mixed norms, the induction
and its tame version, first-order perturbations. Sections 3-6: the four families and the estimates with b-regularity.
Section 7: the proof of Theorem 1.1. Section 8: findings.

## 1. Setting

The setting is that of II.D section 1, now with $k$ degrees of b-regularity. $P$ is a weakly admissible wave-type
operator relative to $P_0$ of class $((d_0;k),(2\ell_I,\ell_+,\ell_K))$ (II.C Definition 3.3), with
$\ell_I\in(0,\frac12]$, $\ell_+,\ell_K>0$, and $\epsilon_{P,k} := \|P-P_0\|_{(d_0;k),(2\ell_I,\ell_+,\ell_K)}$ (II.C
Definition 3.6). The bundle $E$ is the trivial bundle $\mathbb C^N$ (II.C section 1.1), and b-vector fields act on its
sections componentwise, so no connection is needed. $H^{(\mathsf s;k),(2\alpha_I,\alpha_+,\alpha_K)}_{e3b;b}$ are the
mixed spaces of II.A (8.1), with their supported and extendible versions as in II.A section 7, and $\|\cdot\|_{(\mathsf
s;k)}$ their norms, weights suppressed where they are fixed. $D^j_b$ is the schematic notation of II.A Notation 9.4.
Weights do not interfere with commutators: for a b-vector field $V$ and a weight $w$ (a product of powers of boundary
defining functions), $w^{-1}Vw = V+(V\log w)$ with $V\log w$ smooth. Two facts are used throughout.

(F1) $\|v\|_{(\mathsf t+1;k-1)}\le C\|v\|_{(\mathsf t;k)}$, and microlocally $\|Gv\|_{(\mathsf t+1;k-1)}\le
C(\|G'v\|_{(\mathsf t;k)}+\|\chi v\|_{(-N;k)})$ for $G'$ elliptic on $\mathrm{WF}'(G)$ (II.A Lemma 8.4 (c)-(d)): an
e3b-vector field is a b-vector field.

(F2) For elements $X_1,\dots,X_q$ and $P$ of a ring, $[X_1\cdots X_q,P] = \sum_{\emptyset\ne
S}(\mathrm{ad}_{X_S}P)X^{\{1..q\}\setminus S}$, the sum over subsets $S$ of the positions, $\mathrm{ad}_{X_S}$ the
iterated commutator and the remaining factors in their order (II.A Lemma 9.3, (9.4)).

**Theorem 1.1 ([Hin26c] Proposition 7.11 at $n = 4$).** Let $\alpha_I,\alpha_+,\alpha_K$, $\mathsf s_0<\mathsf s$ and
$\chi$ be as in II.D Theorem 1.2. For every $k\in\mathbb N_0$ there is $C_k$ such that
$$\|\chi u\|_{H^{(\mathsf s;k),(2\alpha_I,\alpha_+,\alpha_K)}_{e3b;b}}
\le C_k\Big(\|Pu\|_{H^{(\mathsf s;k),(2\alpha_I+2,\alpha_++2,\alpha_K)}_{e3b;b}(\Omega_*;E)^{\bullet,-}}+
\|u\|_{H^{(\mathsf s_0;k),(2\alpha_I,\alpha_+,\alpha_K)}_{e3b;b}(\Omega_*;E)^{\bullet,-}}\Big)\tag{1.1}$$
for $P = P_0$, in the strong sense, and for every $P$ of class $((d_0;k),(2\ell_I,\ell_+,\ell_K))$ with $\epsilon_{P,k}$
small, with $C_k$ uniform; $d_0$ depends only on $\mathsf s_0$ and $\mathsf s$. Moreover there is $d\in\mathbb N$ such
that for every $k$ and every $P$ of class $((d_0;k),(2\ell_I,\ell_+,\ell_K))$ with $\epsilon_{P,d}$ small,
$$\|\chi u\|_{(\mathsf s;k)}\le C_k\Big(\|Pu\|_{(\mathsf s;k)}+\|u\|_{(\mathsf s_0;k)}+
\epsilon_{P,k}\big(\|Pu\|_{(\mathsf s;d)}+\|u\|_{(\mathsf s_0;d)}\big)\Big),\tag{1.2}$$
with the spaces and weights of (1.1), and $C_k$ depending on $P$ only through a bound for $\epsilon_{P,d}$.

(1.2) is used for $k\ge d$, and (1.1) for $k<d$. The source prints the weights $(2\alpha_I+2,\alpha_++2,\alpha_K)$ on the
last norm of $u$ in (1.2); section 8, (D$'$2).

## 2. The commuted system

Throughout this section $\Gamma\subset{}^{e3b}S^*M$ is one of the sets of II.D sections 3-4 (a radial set or the trapped
set, over one of $\partial\Sigma^\pm$), $U_0$ an open neighbourhood of $\Gamma$ near fibre infinity, and $L$ the operator
that the corresponding estimate of II.D treats ($L = W'^{-1}P$, II.D section 1.1). $\lambda\in\{0,1\}$: $\lambda = 0$ at
the radial sets and $\lambda = 1$ at the trapped set, where the estimate loses one derivative. A *family* is $\mathcal X
= (X_1,\dots,X_J)$ with $X_i\in\mathrm{Diff}^1_b(M)$ acting componentwise and $X_J := I$. For $k\ge1$, $\mathcal W_k :=
\{1,\dots,J\}^k$ is the set of words of length $k$, $X^\alpha := X_{\alpha_1}\cdots X_{\alpha_k}$, and for a position $i$
and a letter $j$, $j\cdot(\alpha\setminus i)$ is the word obtained by deleting the $i$-th letter of $\alpha$ and putting
$j$ in front. The order of factors matters, as the $X_i$ need not commute; words take care of it.

*Operators of limited regularity.* "$Q$ is of class $\mathcal Q^m_q$" means that $Q$ is a finite sum $\sum a_lA_l$ with
$A_l\in C^\infty_b\Psi^m_{e3b}$ fixed and $a_l\in C^\infty+C^{(d_0;k-q)}_{e3b;b}$, carried by the cut-off $\chi$ of the
estimate, as in II.A section 8.2: $q$ b-derivatives of the coefficients of $P$ have been spent. Its *decaying part* is
the sum of the terms whose coefficients vanish at the face carrying $\Gamma$, at a rate $\rho_\Gamma^{\ell}$ for a
defining function $\rho_\Gamma$ of that face and some $\ell>0$. The hypotheses on a family are:

(C) For each $i<J$, $[L,X_i] = \sum_{j = 1}^JQ_{ij}X_j+R_i$, with $Q_{ij}$ of class $\mathcal Q^1_1$ and $R_i$ of class
$\mathcal Q^2_1$ with $\mathrm{WF}'(A_l)\cap\bar U_0 = \emptyset$ for all its terms.

(C2) (Only if $\lambda = 1$.) For $i,i'<J$, $[X_{i'},[X_i,L]] = \sum_{j,j' =
1}^JQ^{(2)}_{i'i,jj'}X_jX_{j'}+R^{(2)}_{i'i}$, with $Q^{(2)}_{i'i,jj'}$ of class $\mathcal Q^0_2$ and $R^{(2)}_{i'i} =
R'+\sum_jR''_jX_j$ with $R'$ of class $\mathcal Q^2_2$ and $R''_j$ of class $\mathcal Q^1_2$, all microsupported off
$\bar U_0$ as in (C) (the eighty-fifth verifier, D206).

(M) Over a neighbourhood of the base projection of $\bar U_0$, the $X_i$ together with $\mathcal V_{e3b}$ span $\mathcal
V_b$ over $C^\infty$; and either the $X_i$ alone span $\mathcal V_b$ there, or there are $i_0<J$ and a bounded weight
$w$, a product of non-negative powers of boundary defining functions, with $wX_{i_0}\in\mathrm{Diff}^1_{e3b}$ elliptic on
$\bar U_0$. Each $X_i$, $i<J$, is a commutator field there: $[X_i,\mathcal V_{e3b}]\subset\mathcal V_{e3b}$ (II.A Lemmas
2.2 and 2.6, Corollary 2.3). The four families of sections 3-6 extend to global elements of $\mathcal V_b$ that are
commutator fields everywhere ($\partial_r$ and $r\partial_r$ are e3b-fields, $t_*\partial_{t_*}$ is a commutator field
everywhere, and the $\Omega_{ab}$ are 3b-fields near $K^+$ and eb-commutator fields near $\mathscr I^+$), which is what
the global statements of II.A Lemma 2.2 and Lemma 8.4 (a) use.

*Parametrix remainders.* II.A Lemma 8.4 (b) gives microlocal parametrices of a finite order $J'$; a remainder said below
to be microsupported off $\bar U_0$ is the sum of such a term and of one of order $-J'$ near $\bar U_0$. Every use needs
only $J'$ large, depending on the orders, and we write as if the second term were absent.

**Lemma 2.1 (the commuted system; [Hin26c] (7.32), (7.43), (7.61)).** Assume (C), and (C2) if $\lambda = 1$. For $k\ge1$
put $u^{(k)} := (X^\alpha u)_{\alpha\in\mathcal W_k}$ and $f := Lu$. Then
$$L^{(k)}u^{(k)} = f^{(k)}+\tilde f^{(k)}+\tilde f^{(k)}_\flat,\qquad f^{(k)} := (X^\alpha f)_\alpha,\tag{2.1}$$
where $L^{(k)}$ acts on $(\mathbb C^N)^{\mathcal W_k}$ by
$$(L^{(k)}w)_\alpha := Lw_\alpha-\sum_{i = 1}^k\sum_{j = 1}^JQ_{\alpha_ij}w_{j\cdot(\alpha\setminus i)}+
\lambda\sum_{i<i'}\sum_{j,j'}Q^{(2)}_{\alpha_{i}\alpha_{i'},jj'}w_{jj'\cdot(\alpha\setminus\{i,i'\})}\tag{2.2}$$
(the last sum over pairs of positions, with $jj'\cdot(\alpha\setminus\{i,i'\})$ the word with those two letters deleted
and $j,j'$ put in front), $\tilde f^{(k)}_\alpha := -\sum_{|S|\ge2+\lambda}(\mathrm{ad}_{X_S}L)X^{\alpha\setminus S}u$,
the sum over sets $S$ of positions, and $\tilde f^{(k)}_{\flat,\alpha} := \sum_iR_{\alpha_i}X^{\alpha\setminus
i}u-\lambda\sum_{i<i'}R^{(2)}_{\alpha_i\alpha_{i'}}X^{\alpha\setminus\{i,i'\}}u$.

*Proof.* $LX^\alpha u = X^\alpha f-[X^\alpha,L]u$, and (F2) expands $[X^\alpha,L]$ over the sets $S$ of positions. For $S
= \{i\}$, $\mathrm{ad}_{X_{\alpha_i}}L = -[L,X_{\alpha_i}] = -\sum_jQ_{\alpha_ij}X_j-R_{\alpha_i}$ by (C), and
$X_jX^{\alpha\setminus i} = X^{j\cdot(\alpha\setminus i)}$. So $-(\mathrm{ad}_{X_{\alpha_i}}L)X^{\alpha\setminus i}u =
\sum_jQ_{\alpha_ij}u^{(k)}_{j\cdot(\alpha\setminus i)}+R_{\alpha_i}X^{\alpha\setminus i}u$. If $\lambda = 1$, for $S =
\{i,i'\}$, $i<i'$, (F2) gives $\mathrm{ad}_{X_{\alpha_i}}\mathrm{ad}_{X_{\alpha_{i'}}}L =
[X_{\alpha_i},[X_{\alpha_{i'}},L]]$, which (C2) writes as $\sum Q^{(2)}X_jX_{j'}+R^{(2)}$, with the indices of (2.2)
after relabelling; its contribution is moved to the left in the same way. $\square$

*Commuting letters.* If a letter $j<J$ commutes with every $X_i$, then for a word $\alpha$ and a position $i$,
$X_jX^{\alpha\setminus i} = X^{\alpha[i\to j]}$, where $\alpha[i\to j]$ is $\alpha$ with its $i$-th letter replaced by
$j$. So in (2.2) the term $Q_{\alpha_ij}w_{j\cdot(\alpha\setminus i)}$ may be replaced by $Q_{\alpha_ij}w_{\alpha[i\to
j]}$; call the operator so modified (2.2$'$). (2.1) holds for it with the same proof, since only $L^{(k)}u^{(k)}$ enters,
and Lemmas 2.3-2.5 use of $L^{(k)}$ only that it is $L\otimes\mathrm{Id}$ minus a coupling whose coefficients carry at
most $1+\lambda$ b-derivatives of those of $P$, so they hold for (2.2$'$). For a letter $1$ with $\alpha_i = 1$,
$\alpha[i\to1] = \alpha$: the coupling through that letter is diagonal. This is what the horizon needs (Lemma 4.1 (c));
with (2.2) the word $1\cdot(\alpha\setminus i)$ differs from $\alpha$ unless $i = 1$, and for $k\ge2$ the Hermitian part
of the coupling is indefinite (the eighty-fifth verifier, D206).

The coefficients of $L^{(k)}-L\otimes\mathrm{Id}$ carry at most $1+\lambda$ b-derivatives of those of $P$, whatever $k$
is; this is what makes the tame estimate possible.

**Lemma 2.2 (mixed norms; [Hin26c] Lemmas 7.15 and 7.19).** Assume (M). Let $B,\tilde B\in C^\infty_b\Psi^0_{e3b}$ be
carried by $\chi$, with operator wave front sets in $U_0$ and $\tilde B$ elliptic on $\mathrm{WF}'(B)$, and $\tilde\chi$
a cut-off equal to 1 near the base projection of $\bar U_0$. Then for all orders $\mathsf t,\mathsf t_0$ and $k\in\mathbb
N_0$,
$$\|Bu\|_{(\mathsf t;k)}\le C\Big(\|\tilde Bu\|_{(\mathsf t;k-1)}+
\sum_{\alpha\in\mathcal W_k}\|BX^\alpha u\|_{\mathsf t}+\|\tilde\chi u\|_{(\mathsf t_0;k)}\Big),\tag{2.3}$$
$$\sum_{\alpha\in\mathcal W_k}\|BX^\alpha u\|_{\mathsf t}\le C\big(\|\tilde Bu\|_{(\mathsf t;k)}+
\|\tilde\chi u\|_{(\mathsf t_0;k)}\big).\tag{2.4}$$
(2.4) holds without (M), for any family of b-differential operators of order 1.

*Proof.* (2.4): $BX^\alpha u = X^\alpha Bu-[X^\alpha,B]u$. The first term has $H^{\mathsf t}$-norm at most
$C\|Bu\|_{(\mathsf t;k)}$, as the $X_i$ are b-differential operators. By (F2), $[X^\alpha,B]$ is a sum of terms
$(\mathrm{ad}_{X_S}B)X^{\alpha\setminus S}$ with $\mathrm{ad}_{X_S}B\in C^\infty_b\Psi^0_{e3b}$ microsupported in
$\mathrm{WF}'(B)$ (II.A Lemma 8.4 (a)); moving the remaining factors to the left by II.A (9.5) bounds them by $C\|\tilde
Bu\|_{(\mathsf t;k)}+C\|\tilde\chi u\|_{(\mathsf t_0;k)}$, using an elliptic parametrix of $\tilde B$ (II.A Lemma 8.4
(c)). $\|Bu\|_{(\mathsf t;k)}\le C(\|\tilde Bu\|_{(\mathsf t;k)}+\|\tilde\chi u\|_{(\mathsf t_0;k)})$ in the same way.
(2.3): by (M) and II.A Notation 9.4, $\|Bu\|_{(\mathsf t;k)}$ is equivalent to the sum of $\|AX^\beta Bu\|_{\mathsf t}$
over $A\in\mathrm{Diff}^{k-|\beta|}_{e3b}$ from a fixed finite set and words $\beta$ in the $X_i$ with $|\beta|\le k$. If
the $X_i$ span $\mathcal V_b$, only $A = I$, $|\beta| = k$ is needed (words with the letter $J$ give the lower orders).
Otherwise, let $Q_q\in C^\infty_b\Psi^{-q}_{e3b}$ be a microlocal parametrix of $(wX_{i_0})^q$ on $\bar U_0$, $I =
Q_q(wX_{i_0})^q+R'_q$ with $\mathrm{WF}'(R'_q)\cap\bar U_0 = \emptyset$ (with $(wX_{i_0})^q =
w^qX_{i_0}^q+\sum_{q'<q}w_{q'}X_{i_0}^{q'}$, $w_{q'}$ bounded, as $X_{i_0}w\in wC^\infty$). Then for $A$ of order $q :=
k-|\beta|$,
$$AX^\beta Bu = AQ_qw^qX_{i_0}^qX^\beta Bu+\sum_{q'<q}AQ_qw_{q'}X_{i_0}^{q'}X^\beta Bu+AR'_qX^\beta Bu.$$
$AQ_qw^q$ and $AQ_qw_{q'}$ lie in $C^\infty_b\Psi^0_{e3b}$ (as $w^q$, $w_{q'}$ are bounded and $A$ has order $q$), so the
first term is bounded by $\|X^{i_0^q\beta}Bu\|_{\mathsf t}$, a word of length $k$, and the second by words of length $<k$
with letters $J$ added. The third is microsupported off $\bar U_0$ after commuting $X^\beta$ through $B$, and is at most
$C\|\tilde\chi u\|_{(\mathsf t_0;k)}$. Finally $X^\gamma Bu = BX^\gamma u+[X^\gamma,B]u$, and the commutator terms carry
at most $k-1$ factors and are at most $C\|\tilde Bu\|_{(\mathsf t;k-1)}+C\|\tilde\chi u\|_{(\mathsf t_0;k)}$, as in
(2.4). $\square$

In the estimates below, the operators $B,E,G$ of an estimate of II.D come with properties (1)-(4) listed there (wave
front sets in a given neighbourhood, Schwartz kernels in a given set, $B$ elliptic at $\Gamma$, and a condition on $E$).
A finite union of closed sets each satisfying (4) satisfies (4); and an operator elliptic on such a union, with wave
front set in a small neighbourhood of it, can be chosen to satisfy (4) again; for II.D Proposition 3.6 it satisfies (4)
with $t_{*,-}+\delta'$ in place of $t_{*,-}$, for any $\delta'>0$, and since $t_{*,-}$ is arbitrary there, starting the
inductions below from $t_{*,-}-k\delta'$ gives (4) as stated at the order $k$. We use this without comment.

*The estimate for systems.* We say $(\mathrm E_\lambda)$ holds for a family on $U_0$ if, for every $k\ge1$, every
neighbourhood $U\subset U_0$ of $\Gamma$ and every $\tilde\chi$ as in Lemma 2.2, there are $B_k,E_k,G_k$ with properties
(1)-(4), wave front sets in $U$ and $B_k$ elliptic at $\Gamma$, such that in the strong sense
$$\|B_kw\|_{\mathsf t}\le C\big(\|G_kL^{(k)}w\|_{\mathsf t-1+\lambda}+\|E_kw\|_{\mathsf t+\lambda}+
\|\tilde\chi w\|_{\mathsf t_0}\big)\tag{2.5}$$
for $\mathbb C^{N|\mathcal W_k|}$-valued $w$, with weights as in the estimate of II.D, and with $C$ depending on $k$ and
on $P$ only through bounds for finitely many $C^{d_0}$-norms of the coefficients of $L^{(k)}$. Lemma 2.5 gives $(\mathrm
E_\lambda)$ in each case below.

**Lemma 2.3 (the induction; [Hin26c] proofs of Propositions 7.17 and 7.22).** Assume (C), (M), (C2) if $\lambda = 1$, and
$(\mathrm E_\lambda)$, at the constant orders $\mathsf t>\mathsf t_0$, and that $P$ is of class $((d_0;k),\ldots)$ with
$d_0$ large depending on $\mathsf t$, $\mathsf t_0$. Then for every $k\in\mathbb N_0$ and every neighbourhood $U\subset
U_0$ of $\Gamma$ there are $B,E,G$ with properties (1)-(4), wave front sets in $U$ and $B$ elliptic at $\Gamma$, such
that in the strong sense
$$\|Bu\|_{(\mathsf t;k)}\le C_k\big(\|GLu\|_{(\mathsf t-1+\lambda;k)}+\|Eu\|_{(\mathsf t+\lambda;k)}+
\|\tilde\chi u\|_{(\mathsf t_0;k)}\big).\tag{2.6}$$
For $k = 0$ this is the estimate of II.D itself.

*Proof.* Induction on $k$. Let $k\ge1$ and assume (2.6) at $k-1$ for every neighbourhood of $\Gamma$. Let $U_{k-1}\subset
U$ be a neighbourhood of $\Gamma$ on which the conclusion at $k-1$ holds for operators $B'$ microsupported in $U_{k-1}$,
with operators $E',G'$ (the union of the sets of two applications, for $B'$ and a slightly larger one). Apply $(\mathrm
E_\lambda)$ with $U_{k-1}$ in place of $U$, to $w := u^{(k)}$, giving $B_k,E_k,G_k$ microsupported in $U_{k-1}$; choose
$G^\sharp_1,G^\sharp_2$ with $\mathrm{WF}'(G_k)\subset\mathrm{Ell}(G^\sharp_1)$,
$\mathrm{WF}'(G^\sharp_1)\subset\mathrm{Ell}(G^\sharp_2)$ and $\mathrm{WF}'(G^\sharp_2)\subset U_{k-1}$, and $B$ with
$\mathrm{WF}'(B)\subset\mathrm{Ell}(B_k)$, $B$ elliptic at $\Gamma$. By Lemma 2.1,
$\|G_kL^{(k)}u^{(k)}\|\le\|G_kf^{(k)}\|+\|G_k\tilde f^{(k)}\|+\|G_k\tilde f^{(k)}_\flat\|$, all norms of order $\mathsf
t-1+\lambda$. We bound each term of (2.5) at $w = u^{(k)}$.

*The left side.* By (2.3) with $\tilde B := G^\sharp_1$, $\|Bu\|_{(\mathsf t;k)}\le C(\|G^\sharp_1u\|_{(\mathsf
t;k-1)}+\sum_\alpha\|BX^\alpha u\|_{\mathsf t}+\|\tilde\chi u\|_{(\mathsf t_0;k)})$, and $\|BX^\alpha u\|_{\mathsf t}\le
C(\|B_ku^{(k)}\|_{\mathsf t}+\|\tilde\chi u\|_{(\mathsf t_0;k)})$, as $B_k$ is elliptic on $\mathrm{WF}'(B)$ and
$\|\tilde\chi X^\alpha u\|_{\mathsf t_0}\le C\|\tilde\chi'u\|_{(\mathsf t_0;k)}$, $\tilde\chi'$ slightly larger. The
first term is bounded by (2.6) at $k-1$.

*The a priori terms.* By (2.4), $\|E_kX^\alpha u\|_{\mathsf t+\lambda}\le C(\|Eu\|_{(\mathsf t+\lambda;k)}+\|\tilde\chi
u\|_{(\mathsf t_0;k)})$ for $E$ elliptic on $\mathrm{WF}'(E_k)$, and $\|\tilde\chi u^{(k)}\|_{\mathsf t_0}\le
C\|\tilde\chi'u\|_{(\mathsf t_0;k)}$.

*$f^{(k)}$.* By (2.4) for $f$, $\|G_kX^\alpha f\|_{\mathsf t-1+\lambda}\le C(\|G^\sharp_1f\|_{(\mathsf
t-1+\lambda;k)}+\|\tilde\chi f\|_{(\mathsf t_0-2;k)})$. Here $\|\tilde\chi f\|_{(\mathsf t_0-2;k)} = \|\tilde\chi
L\tilde\chi'u\|_{(\mathsf t_0-2;k)}\le C\|\tilde\chi'u\|_{(\mathsf t_0;k)}$, as $L$ is bounded on the mixed spaces with
coefficients of class $(d_0;k)$ (II.A Lemma 8.6 (a)), and $\|G^\sharp_1f\|\le C(\|GLu\|_{(\mathsf
t-1+\lambda;k)}+\|\tilde\chi f\|_{(\mathsf t_0-2;k)})$ for $G$ elliptic on $\mathrm{WF}'(G^\sharp_1)$.

*$\tilde f^{(k)}_\flat$.* $G_kR_i$ and $G_kR^{(2)}$ have every order, the wave front sets being disjoint (II.A Lemma 8.5
(b), with the coefficient regularity $(d_0;k-2)$); for the terms $R''_jX_jX^{\alpha\setminus\{i,i'\}}u$ of (C2) the word
$X_jX^{\alpha\setminus\{i,i'\}}$ has $k-1$ letters. So $\|G_k\tilde f^{(k)}_\flat\|_{\mathsf t-1+\lambda}\le
C\|\tilde\chi u\|_{(\mathsf t_0;k-1)}$.

*$\tilde f^{(k)}$.* Let $|S| = q\ge2+\lambda$. $\mathrm{ad}_{X_S}L$ is a second-order operator of class $\mathcal Q^2_q$:
each commutator with a b-vector field preserves $\mathrm{Diff}^2_{e3b}$ up to the coefficients (II.A Lemma 4.1 and Lemma
2.2 near $K^+$, Lemma 2.6 near $\mathscr I^+$), and differentiates the coefficients once. So by II.A Lemma 8.6 (b) and
(2.4),
$$\|G_k(\mathrm{ad}_{X_S}L)X^{\alpha\setminus S}u\|_{\mathsf t-1+\lambda}
\le C\big(\|G^\sharp_2u\|_{(\mathsf t+1+\lambda;k-q)}+\|\tilde\chi u\|_{(\mathsf t_0;k)}\big).$$
As $q-1\ge1+\lambda$, $q-1$ applications of (F1) bound $\|G^\sharp_2u\|_{(\mathsf t+1+\lambda;k-q)}$ by
$C(\|G^\sharp_3u\|_{(\mathsf t;k-1)}+\|\tilde\chi u\|_{(-N;k)})$, with $G^\sharp_3$ slightly larger than $G^\sharp_2$ and
still microsupported in $U_{k-1}$; this is bounded by (2.6) at $k-1$. This is where $\lambda = 1$ needs (C2): a term with
$q = 2$ would need $\|G^\sharp_2u\|_{(\mathsf t+2;k-2)}$, which (F1) bounds only by the norm at $(\mathsf t+1;k-1)$, one
order above what the induction controls.

Collecting the terms gives (2.6) at $k$, with $E$ elliptic on the union of $\mathrm{WF}'(E_k)$ and the $E$-sets of the
step $k-1$. Each quantity bounded is finite when the right side of (2.6) is, by (2.5) in the strong sense and the
inductive hypothesis, so the estimate holds in the strong sense. $\square$

**Lemma 2.4 (tame version; [Hin26c] (7.52), (7.68)).** Under the hypotheses of Lemma 2.3 there is $d\in\mathbb N$,
depending only on $\mathsf t$, $\mathsf t_0$, such that for all $k$ and $P$ of class $((d_0;k),\ldots)$, with the
operators of Lemma 2.3,
$$\|Bu\|_{(\mathsf t;k)}\le C_k\Big(\mathcal R_k+\epsilon_{P,k}\mathcal R_d\Big),\qquad\mathcal R_q :=
\|GLu\|_{(\mathsf t-1+\lambda;q)}+\|Eu\|_{(\mathsf t+\lambda;q)}+\|\tilde\chi u\|_{(\mathsf t_0;q)},\tag{2.7}$$
with $C_k$ depending on $P$ only through a bound for $\epsilon_{P,d}$.

*Proof.* Let $d_1$ and $\tilde d$ be the larger of the numbers $d_0$, resp. $\tilde d$, of II.A Proposition 9.6 for the
orders $(\mathsf t+1+\lambda,\mathsf t_0)$ and $(\mathsf t_0-2,\mathsf t_0-2)$; take $d_0\ge d_1+2$, enlarged to serve
Lemma 2.3, and $d := \tilde d+3$. For $k\le d$, (2.7) is (2.6), whose constant depends on
$\epsilon_{P,k}\le\epsilon_{P,d}$. Let $k>d$ and assume (2.7) below $k$. In the proof of Lemma 2.3 the coefficients of
$P$ enter with more than $2$ b-derivatives in two places only. The constant of (2.5) involves the coefficients of
$L^{(k)}$, which carry at most $1+\lambda$ derivatives (Lemma 2.1), so it depends on $\epsilon_{P,3}\le\epsilon_{P,d}$.
(a) $\|\tilde\chi L\tilde\chi'u\|_{(\mathsf t_0-2;k)}$: write $L = L_0+(L-L_0)$, $L_0$ the operator of $P_0$; $L_0$
contributes $C\|\tilde\chi'u\|_{(\mathsf t_0;k)}$, and II.A Corollary 9.7 bounds the rest by $C_k(\epsilon_{P,\tilde
d}\|\tilde\chi''u\|_{(\mathsf t_0;k)}+\epsilon_{P,k}\|\tilde\chi''u\|_{(\mathsf t_0;\tilde d)})$. (b)
$\|G_k(\mathrm{ad}_{X_S}L)X^{\alpha\setminus S}u\|_{\mathsf t-1+\lambda}$, $|S| = q\ge2+\lambda$: the coefficients of
$\mathrm{ad}_{X_S}(L-L_0)$ are sums of $(D^{q'}_{[b]}p)$ times fixed operators, $q'\le q$, $p$ a coefficient of $L-L_0$;
the part with $q'\le2+\lambda$ is bounded as in Lemma 2.3 with constant depending on $\epsilon_{P,3}$. For
$q'\ge3+\lambda$, commute the second-order factor to the front and $G_k$ through it, as in [Hin26c] (7.55)-(7.56); it
remains to bound $\|\tilde G(D^{q'}_{[b]}D^{\le2}_{e3b}p)(D^{k-q}_{[b]}u)\|_{\mathsf t+1+\lambda}$ with $\tilde G$
microsupported in $U_{k-1}$. II.A Proposition 9.6, with $D^{2+\lambda}_{[b]}D^{\le2}_{e3b}p$ for $\ell$ and
$(q'-2-\lambda,k')$ for $(j,k)$, $k' := k-q+q'-2-\lambda\le k-2-\lambda$, bounds it, after enlarging $k'$ to
$k-2-\lambda$ in the norms of $u$ (and the constant $C_{k'}$ to $C_k$), by
$$C_k\Big(\|p\|_{(d_1+2;\tilde d+2+\lambda)}\big(\|G^\sharp u\|_{(\mathsf t+1+\lambda;k-2-\lambda)}+
\|\tilde\chi u\|_{(\mathsf t_0;k)}\big)+\|p\|_{(d_1+2;k)}\big(\|G^\sharp u\|_{(\mathsf t+1+\lambda;\tilde d)}+
\|\tilde\chi u\|_{(\mathsf t_0;\tilde d)}\big)\Big),$$
as $\|D^{2+\lambda}_{[b]}D^{\le2}_{e3b}p\|_{(d_1;q)}\le C\|p\|_{(d_1+2;q+2+\lambda)}$ and $k'+2+\lambda\le k$. By (F1),
$\|G^\sharp u\|_{(\mathsf t+1+\lambda;k-2-\lambda)}\le C\|G^\sharp_1u\|_{(\mathsf t;k-1)}$, bounded by (2.7) at $k-1$,
whose high norm $\epsilon_{P,k-1}$ multiplies $\mathcal R_d$ only; and $\|G^\sharp u\|_{(\mathsf t+1+\lambda;\tilde
d)}\le C\|G^\sharp_1u\|_{(\mathsf t;\tilde d+1+\lambda)}$, bounded by (2.6) at the order $\tilde d+1+\lambda<d$. Here
$\|p\|_{(d_1+2;\tilde d+2+\lambda)}\le C\epsilon_{P,d}$ and $\|p\|_{(d_1+2;k)}\le C\epsilon_{P,k}$, as $d_1+2\le d_0$,
the coefficients of $L-L_0$ being those of $P-P_0$ up to fixed smooth factors (II.C Definition 3.6). The other terms of
the proof of Lemma 2.3 involve no coefficient with more than two derivatives. This gives (2.7). $\square$

**Lemma 2.5 (the estimates of II.D for systems).** Let $m\in\mathbb N$ and $\tilde L := L\otimes\mathrm{Id}_m-Q$ on
$(\mathbb C^N)^m$, with $Q$ of class $\mathcal Q^1_2$ (with the regularity $(d_0;0)$ for its coefficients). Let $\Gamma$
be one of the sets of II.D Propositions 3.1-3.6 and 4.2, with the fibre inner product $h$ used there, and suppose that at
$\Gamma$, as Hermitian matrices for $h^{\oplus m}$,
$$\varsigma\rho\,\sigma_1(\mathrm{Im}_{h^{\oplus m}}(-Q))\le0,\tag{2.8}$$
with $\rho$ the function of II.D used at $\Gamma$ and $\varsigma = \pm1$ on $\partial\Sigma^\pm$. Then the estimate of
II.D at $\Gamma$ holds for $\tilde L$ in place of $L$, with the same orders, weights and thresholds, and with constants
depending on finitely many norms of the coefficients of $Q$.

*Proof.* $L\otimes\mathrm{Id}_m$ is $L$ for the bundle $E^{\oplus m} = \mathbb C^{Nm}$, an operator of the same class
with the same thresholds in the inner product $h^{\oplus m}$, as all quantities are block diagonal. *Radial sets.* II.D
Remark 3.7: the estimates hold for $L\otimes\mathrm{Id}+\tilde P$ with $\tilde P$ first order of the form stated there,
with the thresholds computed from $\sigma_1(\mathrm{Im}_{h^{\oplus m}}\tilde L)$ at $\Gamma$. By (2.8) this differs from
that of $L\otimes\mathrm{Id}$ by a non-positive Hermitian matrix (times $\varsigma$). In each quantity $Q_\epsilon$ of
II.D section 3 it enters as $-2A^{-1}(\cdot)A$ (the term $-2A^{-1}\mathfrak p'A$, and at $\partial R_{\mathscr
I^+,\mathrm{out}}$ the term $4A^{-1}\mathrm{Re}_hp_1A = -2A^{-1}\mathfrak p'A$), so it only increases $Q_\epsilon$, and
every lower bound of II.D section 3 persists. *The trapped set.* In the proof of II.D Proposition 4.2 the operator enters
through its principal symbol $G\,\mathrm{Id}$, unchanged; through $\mathfrak p$ at $\partial\Gamma_{K^+}$, now $\mathfrak
p-\rho\sigma_1(\mathrm{Im}\,Q)$ after the conjugation of Step 0, whose largest eigenvalue is at most $\vartheta_\Gamma$
by (2.8), so (T3) and (4.3) hold as stated; through the form $\mathrm{Op}(\ell_f)+R_L$ of the remark after II.D Lemma
2.5, which $\tilde L$ has; and through the commutator (4.4), where $[Q,\Phi_u]$ has order 0 and joins $R_2$. Nothing else
in sections 2 and 4 of II.D uses the operator. $\square$

In sections 3-6, (2.8) holds because the first-order part of $Q$ either decays at the face carrying $\Gamma$, so that its
principal symbol vanishes at $\Gamma$, or is diagonal with a non-positive contribution (at the horizon). The part of $Q$
of order 0 does not enter (2.8).

## 3. Near $\mathscr I^+$

Near $\mathscr I^+\cap\Omega$ we use the coordinates $\rho_+ = t_*^{-1}$, $x_I = (t_*/r)^{1/2}$, $\omega\in\mathbb S^3$
of II.C section 5.1, $W := x_I^2\rho_+^2$ and $L := W^{-1}P$, as in II.D Propositions 3.5-3.6. Put
$$V_1 := x_I\partial_{x_I}-2\rho_+\partial_{\rho_+} = 2t_*\partial_{t_*},\qquad V_2 := x_I\partial_{x_I} = -2r\partial_r,
$$
the second at fixed $t_*$, and let $\Omega_{ab}$, $1\le a<b\le4$, be the six rotation fields
$y_a\partial_{y_b}-y_b\partial_{y_a}$ of $\mathbb S^3\subset\mathbb R^4$, extended independently of $(x_I,\rho_+)$. The
family is $\mathcal X_I := (V_1,V_2,\Omega_{12},\dots,\Omega_{34},I)$, $J = 9$.

**Lemma 3.1 ([Hin26c] Lemma 7.12 at $n = 4$).** (a) $[V_1,V_2] = [V_i,\Omega_{ab}] = 0$, the $\Omega_{ab}$ span
$\mathfrak{so}(4)$, and $\sum_{a<b}\Omega_{ab}^2$ is the Laplace-Beltrami operator of $\mathbb S^3$, so $\Delta_{\mathbb
S^3}$ of II.C Lemma 3.4 is $\pm\sum_{a<b}\Omega_{ab}^2$ and commutes with every $\Omega_{ab}$. (b) The family $\mathcal
X_I$ satisfies (C) on $\Omega_I = \Omega\cap\{x_I\le\epsilon_I\}$ with $R_i = 0$, and each $Q_{ij}$ is the sum of an
operator of order 0 and a first-order eb-operator whose coefficients lie in
$x_IC^\infty+x_I^{2\ell_I}C^{(d_0;k-1)}_{eb;b}$. (c) $\mathcal X_I$ spans $\mathcal V_b$ near $\mathscr I^+$, and its
elements are eb-commutator fields (II.A Lemma 2.6), so (M) holds. (d) At $\partial R_{\mathscr I^+,\mathrm{in},+}$ and
$\partial R_{\mathscr I^+,\mathrm{out}}$, which lie over $x_I = 0$, the first-order part of each $Q_{ij}$ has vanishing
principal symbol, so (2.8) holds with equality.

*Proof.* (a) $V_1$, $V_2$ are coordinate vector fields of the product coordinates $(\log x_I,\log\rho_+)$, up to constant
linear combinations, and the $\Omega_{ab}$ act on $\omega$ alone. The $\Omega_{ab}$ are the generators of the action of
$SO(4)$ on $\mathbb S^3$, and $\sum_{a<b}\Omega_{ab}^2$ is the Casimir operator of this action on functions, which is the
Laplace-Beltrami operator of the round metric (the identity $\sum_{a<b}(y_a\partial_b-y_b\partial_a)^2
= |y|^2\Delta_{\mathbb R^4}-(y\cdot\partial)^2-2\,y\cdot\partial$ restricted to $|y| = 1$, functions extended
homogeneously of degree 0). (b) By II.C Lemma 3.4, near $\mathscr I^+$,
$$2L = -(V_2-3-2p_1)V_1\pm2x_I^2\sum_{a<b}\Omega_{ab}^2+p_0+\tilde R,
\qquad\tilde R\in C^{(d_0;k),(2\ell_I,0)}_{eb;b}\mathrm{Diff}^2_{eb},$$
with $p_0$, $p_1 = S|_{\partial X}+\tilde p_1$ functions on $\mathscr I^+$ extended independently of $x_I$, so $V_2p_0 =
V_2p_1 = 0$. We compute $[2L,X]$ for $X\in\mathcal X_I$, $X\ne I$, using $[AB,X] = A[B,X]+[A,X]B$ and (a).

$[-(V_2-3-2p_1)V_1,X] = 2[p_1,X]V_1 = -2(Xp_1)V_1$: an operator of order 0 times $V_1$; it vanishes for $X = V_2$.
$[\pm2x_I^2\sum\Omega_{ab}^2,X] = \mp2(Xx_I^2)\sum\Omega_{ab}^2$, which is $\mp4x_I^2\sum\Omega_{ab}^2$ for $X = V_1,V_2$
(as $V_1x_I^2 = V_2x_I^2 = 2x_I^2$) and $0$ for $X = \Omega_{cd}$. Now $x_I^2\Omega_{ab}^2 =
x_I(x_I\Omega_{ab})\circ\Omega_{ab}$ with $x_I\Omega_{ab}\in\mathcal V_{eb}$: a first-order eb-operator with coefficient
in $x_IC^\infty$, times $\Omega_{ab}$. $[p_0,X] = -(Xp_0)$, of order 0 (a term $Q_{iJ}X_J$). Finally $[\tilde R,X]\in
C^{(d_0;k-1),(2\ell_I,0)}_{eb;b}\mathrm{Diff}^2_{eb}$, as $X$ is an eb-commutator field and differentiates the
coefficients once (II.A Lemma 2.6 and Lemma 8.2 (b)). $\mathcal V_{eb}$ is spanned over $C^\infty$ by $V_1$, $V_2$ and
$x_I\Omega_{ab}$, so every element of $x_I^{2\ell_I}C^{(d_0;k-1)}_{eb;b}\mathrm{Diff}^2_{eb}$ is a sum $\sum_jA_jX_j$
with $A_j\in x_I^{2\ell_I}C^{(d_0;k-1)}_{eb;b}\mathrm{Diff}^1_{eb}$ (for $j$ a rotation, the factor $x_I$ of
$x_I\Omega_{ab}$ joins $A_j$; the first-order part of the operator is $A_JX_J$). Collecting, $[L,X_i] = \sum_jQ_{ij}X_j$
with $Q_{ij}$ as stated. (c) Near $\mathscr I^+$, $\mathcal V_b$ is spanned by $\rho_+\partial_{\rho_+}$,
$x_I\partial_{x_I}$ and the vector fields on $\mathbb S^3$, which $V_1$, $V_2$ and the $\Omega_{ab}$ span. (d) The
principal symbol of a first-order eb-operator with coefficients in $x_IC^\infty+x_I^{2\ell_I}C^0$ vanishes over $x_I =
0$. $\square$

**Proposition 3.2 ([Hin26c] section 7.2.3, the analogues of Propositions 7.8-7.9, at $n = 4$).** II.D Propositions 3.5
and 3.6 hold with $H^{(\mathsf t;k)}_{e3b;b}$ in place of $H^{\mathsf t}_{e3b}$ for every $k\in\mathbb N_0$:
$$\|Bu\|_{(s;k),(2\alpha_I,\alpha_+)}\le C_k\big(\|GPu\|_{(s-1;k),(2\alpha_I+2,\alpha_++2)}+
\|Eu\|_{(s;k),(2\alpha_I,\alpha_+)}+\|\tilde\chi u\|_{(s_0;k),(2\alpha_I,\alpha_+)}\big),\tag{3.1}$$
with $B,E,G$ having the properties (1)-(4) stated there, in the strong sense, for $P = P_0$ and $P$ of class
$((d_0;k),\ldots)$ with $\epsilon_{P,k}$ small, $d_0$ depending only on $s,s_0$; and in the tame form (2.7), with
$\epsilon_{P,k}$ times the right side of (3.1) at the order $d$.

*Proof.* Lemmas 2.3-2.5 with $\lambda = 0$, the family $\mathcal X_I$ and Lemma 3.1;
$\|GLu\|_{(s-1;k),(2\alpha_I,\alpha_+)}$ and $\|GPu\|_{(s-1;k),(2\alpha_I+2,\alpha_++2)}$ are equivalent up to a
microlocal error, $W$ being a weight. The thresholds (II.D (3.7) and (3.9)) concern the weights only and are unchanged by
Lemma 3.1 (d). $\square$

## 4. The horizon

Near $\mathcal H^+\cap K^+ = \{r = r_h,\rho_K = 0\}$ use the coordinates $(t_*,r,\omega)$, $\rho_K = t_*^{-1}$, with
covectors $-\sigma\,dt_*+\xi_0\,dr+\eta$; $W' = 1$ and $L = P$, as in II.D Proposition 3.1. $\partial R_{\mathcal H^+}$
lies in $\{\sigma = 0,\eta = 0\}$ with $\xi_0\ne0$ (II.B Definition 4.1: it is the boundary of the conormal bundle of
$\{r = r_h\}$), so we take $U_0\subset\{|\xi_0|\ge c(|\sigma|+|\xi_0|+|\eta|)\}$, a small neighbourhood of $\partial
R_{\mathcal H^+}$. The family is $\mathcal X_{\mathcal H} := (\partial_r,t_*\partial_{t_*},I)$.

**Lemma 4.1 ([Hin26c] Lemmas 7.15-7.16 at $n = 4$).** (a) (M) holds: $\mathcal V_b$ near $\mathcal H^+\cap K^+$ is
spanned by $\mathcal V_{3b}$ and $t_*\partial_{t_*}$ (II.A Corollary 2.3); $\partial_r\in\mathcal V_{3b}$ is elliptic on
$\bar U_0$ (with $w = 1$); both are e3b-commutator fields (II.A Lemma 2.2). (b) (C) holds on $U_0$. (c) The system
$L^{(k)} = P\otimes\mathrm{Id}-Q$ of Lemma 2.1 in the form (2.2$'$), both letters commuting ($[\partial_r,
t_*\partial_{t_*}] = 0$), satisfies, at $\partial R_{\mathcal H^+}$,
$$\varsigma\rho\,\sigma_1(\mathrm{Im}(-Q)) = -\mathrm{diag}\big(j_\alpha\big)_{\alpha\in\mathcal W_k}\,\beta_0\le0,
\tag{4.1}$$
with $j_\alpha$ the number of letters 1 (that is, of factors $\partial_r$) in $\alpha$, $\rho$ the function of (H3) and
$\beta_0>0$ of II.B (4.1). So (2.8) holds, and the threshold of II.D Proposition 3.1 for $L^{(k)}$ is at most
$\vartheta_{\mathcal H}$.

*Proof.* (b) Write $P = \sum_lp_lA_l$ near $\mathcal H^+\cap K^+$, with $A_l\in\mathrm{Diff}^2_{3b}$ fixed and
independent of $t_*$ (products of $\partial_{t_*}$, $\partial_r$, $\partial_\omega$), and $p_l = p^\sharp_l+\tilde p_l$,
$p^\sharp_l$ the coefficients of $P_0$, independent of $t_*$, and $\tilde p_l\in\rho_K^{\ell_K}C^{(d_0;k)}_{3b;b}$ (II.C
Definition 3.3). Let $Q_r\in C^\infty_b\Psi^{-1}_{3b}$ be a microlocal parametrix of $\partial_r$ on $\bar U_0$: $I =
Q_r\partial_r+R_r$, $\mathrm{WF}'(R_r)\cap\bar U_0 = \emptyset$.

*$X_1 = \partial_r$.* $[P,\partial_r]$ is a second-order operator of class $\mathcal Q^2_1$. Put $Q_{11} :=
[P,\partial_r]Q_r$, $R_1 := [P,\partial_r]R_r$, and $Q_{1j} := 0$ for $j\ne1$; then $[P,\partial_r] =
Q_{11}\partial_r+R_1$. The principal symbol of $[P,\partial_r]$ is $\frac1i\{G,i\xi_0\} = H_G\xi_0$, as $\partial_r$ has
symbol $i\xi_0$. So $Q_{11}$ has principal symbol $H_G\xi_0/(i\xi_0) = -i(H_G\xi_0)/\xi_0$, a purely imaginary scalar,
and $\sigma_1(\mathrm{Im}(-Q_{11})) = (H_G\xi_0)/\xi_0$. Its lower-order part (from the first-order part of $P$, composed
with $Q_r$) has order 0 and does not enter.

*$X_2 = t_*\partial_{t_*}$.* $t_*\partial_{t_*}p^\sharp_l = 0$, and by II.A Lemma 2.2, $[t_*\partial_{t_*},A_l] =
\rho_KA^\flat_lt_*\partial_{t_*}+\rho_KA^\sharp_l$ with $A^\flat_l\in\mathrm{Diff}^1_{3b}$,
$A^\sharp_l\in\mathrm{Diff}^2_{3b}$. Hence
$$[P,X_2] = -\sum_l\big((X_2\tilde p_l)A_l+p_l\rho_KA^\flat_lX_2+p_l\rho_KA^\sharp_l\big),$$
and with $I = Q_r\partial_r+R_r$ on the second-order terms, $Q_{22} := -\sum_lp_l\rho_KA^\flat_l$, $Q_{21} :=
-\sum_l((X_2\tilde p_l)A_l+p_l\rho_KA^\sharp_l)Q_r$, $R_2 := -\sum_l((X_2\tilde p_l)A_l+p_l\rho_KA^\sharp_l)R_r$. Their
coefficients carry a factor $\rho_K$ or $\rho_K^{\ell_K}$ ($X_2\tilde p_l\in\rho_K^{\ell_K}C^{(d_0;k-1)}_{3b;b}$), so
they decay at $K^+$.

(c) By (b) and (2.2$'$), $-Q$ has, at $\partial R_{\mathcal H^+}\subset\{\rho_K = 0\}$, first-order principal symbol
$\mathrm{diag}(j_\alpha)\,i(H_{G_0}\xi_0)/\xi_0$: each letter 1 of $\alpha$ couples the component $\alpha$ to itself
through $Q_{11}$, as $\alpha[i\to1] = \alpha$, and the couplings through $Q_{21}$, $Q_{22}$ decay; $G = G_0$ there. Let
$\tilde\rho := |\xi_0|^{-1}$ on $U_0$ and $\mathsf H := \rho H_G$. Then $\rho(H_G\xi_0)/\xi_0 =
-\rho\tilde\rho^{-1}H_G\tilde\rho = -\tilde\rho^{-1}\mathsf H\tilde\rho$. At the radial set $\partial R_{\mathcal H^+}$
the vector field $\mathsf H$ on the cosphere bundle vanishes, so $\tilde\rho^{-1}\mathsf H\tilde\rho = \rho^{-1}\mathsf
H\rho+(\tilde\rho/\rho)^{-1}\mathsf H(\tilde\rho/\rho) = \rho^{-1}\mathsf H\rho = \beta_0$ there (II.B (4.1), as in the
proof of II.D Proposition 3.1), $\tilde\rho/\rho$ being homogeneous of degree 0. This gives (4.1) on $\partial\Sigma^+$,
where $\varsigma = 1$; on $\partial\Sigma^-$ the quantity $(H_G\xi_0)/\xi_0$ is even, the future field is $-\mathsf H$,
whose $\rho^{-1}(-\mathsf H)\rho$ is $\beta_0$, so $\rho^{-1}\mathsf H\rho = -\beta_0$ there, and $\varsigma = -1$
restores (4.1). The threshold of II.D Proposition 3.1 for $L^{(k)}$ is then $\sup\lambda_{\max}(\beta_0^{-1}(\mathfrak
p-j_\alpha\beta_0))\le\vartheta_{\mathcal H}$, in the inner product $h^{\oplus\mathcal W_k}$. $\square$

The non-positive sign in (4.1) is the red shift: commuting with $\partial_r$ lowers the threshold, so the minimal
regularity $s_0>\frac12+\vartheta_{\mathcal H}$ of II.D Proposition 3.1 does not rise with $k$.

**Proposition 4.2 ([Hin26c] Proposition 7.17 at $n = 4$).** Let $s>s_0>\frac12+\vartheta_{\mathcal H}$ and $k\in\mathbb
N_0$. There are $B,E,G$ with the properties (1)-(4) of II.D Proposition 3.1 such that for all $\alpha_K\in\mathbb R$ and
$\tilde\chi$ as there
$$\|Bu\|_{(s;k),\alpha_K}\le C_k\big(\|GPu\|_{(s-1;k),\alpha_K}+\|Eu\|_{(s;k),\alpha_K}+
\|\tilde\chi u\|_{(s_0;k),\alpha_K}\big),\tag{4.2}$$
in the strong sense, uniformly for $P = P_0$ and $P$ of class $((d_0;k),(0,0,\ell_K))$ near $K^+$ with $\epsilon_{P,k}$
small, $d_0$ depending only on $s,s_0$; and the tame estimate (2.7) holds, with $d$ depending only on $s,s_0$ and $C_k$
on $P$ only through $\epsilon_{P,d}$.

*Proof.* Lemmas 2.3-2.5 with $\lambda = 0$ and Lemma 4.1. $\square$

## 5. Over $\partial K^+$

Near $\partial K^+$ use $\rho_K := r/t_*$, $\rho_+ := r^{-1}$, $\omega$ (II.B section 3.1), $W' = \rho_+^2$ and $L :=
\rho_+^{-2}P$, as in II.D Propositions 3.2-3.3. The family is $\mathcal X_K := (t_*\partial_{t_*},I)$, and $U_0$ is a
small neighbourhood of $\partial R_{\partial K^+,\mathrm{in}}$ or of $\partial R_{\partial K^+,\mathrm{out}}$.

**Lemma 5.1 ([Hin26c] Lemmas 7.19-7.20 at $n = 4$).** (a) (M) holds with $i_0 = 1$, $w = \rho_K$: $\mathcal V_b$ near
$\partial K^+$ is spanned by $\mathcal V_{3b}$ and $t_*\partial_{t_*}$ (II.A Corollary 2.3), and $t_*\partial_{t_*}$ is a
commutator field (II.A Lemma 2.2), and $\rho_Kt_*\partial_{t_*} = r\partial_{t_*}\in\mathcal V_{3b}$ has principal symbol
a non-zero multiple of $\sigma_{3b}$, which is elliptic at both radial sets ($\sigma_{3b}<0$ there, II.B Definition 3.1).
(b) (C) holds on $U_0$, with $Q_{11}$ of class $\mathcal Q^1_1$ whose coefficients carry a factor $\rho_K$ or
$\rho_K^{\ell_K}$, so (2.8) holds with equality at both radial sets, which lie over $K^+$.

*Proof.* (b) Write $L = \sum_lp_lA_l$ with $A_l\in\mathrm{Diff}^2_{3b}$ fixed and independent of $t_*$, $p^\sharp_l$ the
coefficients of $\rho_+^{-2}P_0$, independent of $t_*$ in the coordinates $(t_*,r,\omega)$, and $\tilde
p_l\in\rho_+^{\ell_+}\rho_K^{\ell_K}C^{(d_0;k)}_{3b;b}$, the coefficients of $\rho_+^{-2}(P-P_0)$ (II.C Definition 3.3).
$t_*\partial_{t_*}$ commutes with $\rho_+$ and annihilates $p^\sharp_l$. II.A Lemma 2.2 gives $[X_1,A_l] =
\rho_KA^\flat_lX_1+\rho_KA^\sharp_l$, as in Lemma 4.1. Let $Q_K\in C^\infty_b\Psi^{-1}_{3b}$ be a microlocal parametrix
of $\rho_KX_1$ on $\bar U_0$, $I = Q_K\rho_KX_1+R_K$. Then
$$[L,X_1] = -\sum_l\big(p_l\rho_KA^\flat_l+\big((X_1\tilde p_l)A_l+
p_l\rho_KA^\sharp_l\big)Q_K\rho_K\big)X_1-\sum_l\big((X_1\tilde p_l)A_l+p_l\rho_KA^\sharp_l\big)R_K,$$
which is (C) with $Q_{11}$ the first sum and $R_1$ the second; the factors $\rho_K$, $\rho_K^{\ell_K}$ appear in every
coefficient of $Q_{11}$. $\square$

**Proposition 5.2 ([Hin26c] section 7.2.3, the analogues of Propositions 7.6-7.7, at $n = 4$).** II.D Propositions 3.2
and 3.3 hold with $H^{(\mathsf t;k)}_{e3b;b}$ in place of $H^{\mathsf t}_{e3b}$, with their thresholds (3.3) and (3.5)
unchanged, in the strong sense, uniformly for $P$ with $\epsilon_{P,k}$ small, and in the tame form (2.7).

*Proof.* Lemmas 2.3-2.5 with $\lambda = 0$ and Lemma 5.1. The threshold (3.5) at $\partial R_{\partial K^+,\mathrm{out}}$
is an upper bound on the order, which every order of the iteration in Lemma 2.3 meets, as there the order $s$ is fixed
and only $k$ increases. $\square$

## 6. The trapped set

Over $D$ near $\partial\Gamma_0$ (II.D section 4) use $(t_*,x)$, $\rho_K = t_*^{-1}$, $W' = 1$, $L = P$. The family is
$\mathcal X_\Gamma := (t_*\partial_{t_*},I)$, and $U_0$ is a small neighbourhood of the component of
$\partial\Gamma_{K^+}$ over $\partial\Sigma^+$ or $\partial\Sigma^-$; on it $\sigma\ne0$ (II.B Lemma 5.2 (a)).

**Lemma 6.1 ([Hin26c] Lemma 7.21 at $n = 4$).** (a) (M) holds with $i_0 = 1$, $w = \rho_K$: $t_*\partial_{t_*}$ is a
commutator field (II.A Lemma 2.2), and $\rho_Kt_*\partial_{t_*} = \partial_{t_*}$, whose principal symbol is a non-zero
multiple of $\sigma$, elliptic on $\bar U_0$. (b) (C) holds with $Q_{11}$ decaying at $K^+$, and (C2) holds with
$Q^{(2)}$ of order 0. So (2.8) holds with equality at $\partial\Gamma_{K^+}$.

*Proof.* (b) (C): as in Lemma 5.1, with $L = P = \sum_lp_lA_l$, $A_l\in\mathrm{Diff}^2_{3b}$ (cusp operators over $D$)
independent of $t_*$, $p^\sharp_l$ independent of $t_*$ and $\tilde p_l\in\rho_K^{\ell_K}C^{(d_0;k)}_{3b;b}$, and $Q_K$ a
microlocal parametrix of $\partial_{t_*}$ on $\bar U_0$. (C2): from the formula for $[L,X_1]$,
$$[X_1,[X_1,L]] = \sum_l\Big((X_1^2\tilde p_l)A_l+(X_1\tilde p_l)[X_1,A_l]+(X_1p_l)\rho_K\big(A^\flat_lX_1+
A^\sharp_l\big)-p_l\rho_K\big(A^\flat_lX_1+A^\sharp_l\big)+p_l\rho_K\big([X_1,A^\flat_l]X_1+[X_1,A^\sharp_l]\big)\Big),$$
using $X_1\rho_K = -\rho_K$. By II.A Lemma 2.2 again, $[X_1,A^\flat_l]$ and $[X_1,A^\sharp_l]$ are of the form
$\rho_K(\cdot)X_1+\rho_K(\cdot)$, and $[X_1,A_l] = \rho_KA^\flat_lX_1+\rho_KA^\sharp_l$. So every term is a second-order
operator $D$, or a first-order operator $D'$ followed by $X_1$ (the terms $p_l\rho_K^2cX_1X_1$, $c$ smooth, from
$p_l\rho_K[X_1,A^\flat_l]X_1$ are already of the form $Q^{(2)}X_1X_1$ with $Q^{(2)}$ of order 0), with coefficients in
$\rho_KC^\infty+\rho_K^{\ell_K}C^{(d_0;k-2)}_{3b;b}$. Let $Q'\in C^\infty_b\Psi^{-2}_{3b}$ be a microlocal parametrix of
$(\rho_KX_1)^2 = \partial_{t_*}^2$ on $\bar U_0$, $I = Q'(\rho_KX_1)^2+R'$, and note $(\rho_KX_1)^2 =
\rho_K^2X_1^2-\rho_K^2X_1$. Then
$$D = (DQ'\rho_K^2)X_1X_1-(DQ'\rho_K^2)X_1X_J+DR',\qquad D'X_1 = (D'Q_K\rho_K)X_1X_1+D'R_KX_1,$$
with $DQ'\rho_K^2$ and $D'Q_K\rho_K$ of order 0 and class $\mathcal Q^0_2$, $DR'$ of class $\mathcal Q^2_2$, and
$D'R_KX_1$ of the form $R''X_1$ with $R'' := D'R_K$ of class $\mathcal Q^1_2$, both microsupported off $\bar U_0$. This
is (C2). $\square$

**Proposition 6.2 ([Hin26c] Proposition 7.22 at $n = 4$).** There are $B,E,G$ with the properties (1)-(4) of II.D
Proposition 4.2 such that for all $s>s_0$, $k\in\mathbb N_0$, $\alpha_K\in\mathbb R$ and $\tilde\chi$ as there
$$\|Bu\|_{(s;k),\alpha_K}\le C_k\big(\|GPu\|_{(s;k),\alpha_K}+\|Eu\|_{(s+1;k),\alpha_K}+
\|\tilde\chi u\|_{(s_0;k),\alpha_K}\big),\tag{6.1}$$
in the strong sense, uniformly for $P = P_0$ and $P$ of class $((d_0;k),(0,0,\ell_K))$ with $\epsilon_{P,k}$ small, $d_0$
depending only on $s,s_0$; and the tame estimate (2.7) holds.

*Proof.* Lemmas 2.3-2.5 with $\lambda = 1$ and Lemma 6.1. Lemma 2.5 gives $(\mathrm E_1)$ from II.D Proposition 4.2 for
the systems $L^{(k)}$, whose first-order part differs from $P\otimes\mathrm{Id}$ by terms decaying at $K^+$, so that the
condition $\vartheta_\Gamma<\frac12\nu_{\min}$ at $\partial\Gamma_{K^+}$ is that of $P$. $\square$

## 7. Proof of Theorem 1.1

For $k = 0$, (1.1) is II.D Theorem 1.2. Let $k\in\mathbb N$, let $u$ be as in Theorem 1.1, and for $q\in\mathbb N_0$
write
$$\mathcal R_q := \|Pu\|_{(\mathsf s;q),(2\alpha_I+2,\alpha_++2,\alpha_K)}+
\|u\|_{(\mathsf s_0;q),(2\alpha_I,\alpha_+,\alpha_K)},$$
the norms being those of (1.1) on $\Omega_*$, so that the right side of (1.1) is $\mathcal R_k$ and that of (1.2) is
$\mathcal R_k+\epsilon_{P,k}\mathcal R_d$. As in II.D section 5, $u$ and $Pu$, extended by zero, are supported in
$\{t^\flat_*\ge1\}$; below $\|\cdot\|_{(\mathsf t;k)}$ carries the weights of $u$, and $Pu$ is measured with the weights
of (1.1), which is the measure of $Lu = W^{-1}Pu$ with the weights of $u$. We say $u$ is *controlled at order $(\mathsf
t;k)$* on an open set $V\subset{}^{e3b}S^*M$ if $\|Bu\|_{(\mathsf t;k)}\le C_k\mathcal R_k$, in the strong sense, for
every $B\in C^\infty_b\Psi^0_{e3b}$ carried by $\chi$ with $\mathrm{WF}'(B)\subset V$; and *tamely controlled* if
moreover, for every $P$ as in the second half of Theorem 1.1, $\|Bu\|_{(\mathsf t;k)}\le C_k(\mathcal
R_k+\epsilon_{P,k}\mathcal R_d)$, with $C_k$ depending on $P$ only through a bound for $\epsilon_{P,d}$.

The proof is that of II.D section 5, step for step, with each estimate replaced by its version with b-regularity. The
flow is that of $P$, unchanged, so the backward curves are those used there; only the estimates change. The replacements
are these.

(P0$_k$) *Elliptic estimate.* Off the characteristic set, II.A Proposition 9.1 with $m = 2$ controls $u$ at every order
$(\mathsf t;k)$ with $\mathsf t\le\mathsf s+1$, and its tame version, II.A Proposition 9.8, tamely.

(P1$_k$) *Propagation.* II.A Proposition 9.2, and its tame version Proposition 9.9, replace II.A$'$ Theorem 5.4 in II.D
(P1). Their hypotheses on the flow, on the orders and on $B,E,G$ are those of (L4), which II.D (P1) uses, and they give:
control at order $(\mathsf t;k)$ on $V$ gives control at order $(\mathsf t;k)$ at every $\varpi$ whose backward $\mathsf
H$-curve enters $V$ in finite time, provided $\mathsf H\mathsf t\le0$ along it and $Pu$ is in $H^{(\mathsf t-1;k)}$ near
it. The weights are put into the operator as for $k = 0$ (II.D section 1.2): the conjugation by a weight $w$ adds to $L$
terms whose coefficients are those of $L$ times the functions $w^{-1}Vw$ and $w^{-1}VV'w$, $V,V'\in\mathcal V_{e3b}$,
which are smooth with smooth b-derivatives (section 1), so the conjugated operator has the form (9.2) of II.A at the
regularity $(d_0;k)$.

(P2), (P3) are unchanged: as $u = 0$ in $\{t^\flat_*<1\}$, $u$ is controlled there at every order $(\mathsf t;k)$.

(R$_k$) *Radial sets and the trapped set.* II.D Propositions 3.1, 3.2, 3.3, 3.5, 3.6 and 4.2 are replaced by Propositions
4.2, 5.2, 5.2, 3.2, 3.2 and 6.2 here. Each is used with the orders of II.D section 5, which are constant near the set,
with the threshold conditions there, and with operators $B,E,G$ having the properties (1)-(4) of the proposition of II.D
it replaces. The thresholds do not change with $k$: at the horizon by Lemma 4.1 (c), elsewhere by Lemmas 3.1 (d), 5.1 (b)
and 6.1 (b).

*Step 1: finite times.* Let $t^\sharp$ and $\mathcal V_{\mathrm{out}}$ be as in II.D Step 1. Along the backward curves
used there, (P1$_k$) at order $(\mathsf s+1;k)$, with $Pu\in H^{(\mathsf s;k)}$, and (P2) control $u$ at order $(\mathsf
s+1;k)$ near every compact subset of $\partial\Sigma^+$ over $\Omega_*\cap\{t^\flat_*\le t^\sharp\}$ disjoint from
$\mathcal V_{\mathrm{out}}$.

*Step 2: the horizon and $\partial R_{\mathscr I^+,\mathrm{in},+}$.* Proposition 4.2 and Proposition 3.2 (for II.D
Proposition 3.5), with the orders $(\mathsf s+1,\mathsf s_0)$, $\mathsf s_0>\frac12+\vartheta_{\mathcal H}$ near
$\partial R_{\mathcal H^+}$ and (3.7) from (1.3). Their $E$ have property (4), so they lie at finite times, away from
$K^+$, resp. $\iota^+$, and operator wave front sets in small neighbourhoods of the two sets, the second away from
$\partial R_{\mathscr I^+,\mathrm{out}}$; this is what II.D Step 2 uses. So Step 1 bounds $\|Eu\|_{(\mathsf s+1;k)}$, and
$u$ is controlled at order $(\mathsf s+1;k)$ on neighbourhoods $V_{\mathcal H}$ of $\partial R_{\mathcal H^+}$ and $V_I$
of $\partial R_{\mathscr I^+,\mathrm{in},+}$.

*Step 3: $\partial R_{\partial K^+,\mathrm{in}}$.* Proposition 5.2 (for II.D Proposition 3.2), with the orders $(\mathsf
s+1,\mathsf s_0)$ and (3.3). Its $E$ has property (4) and operator wave front set in a small neighbourhood of $\partial
R_{\partial K^+,\mathrm{in}}$; the backward curves from it are those of II.D Step 3, which reach $\{t^\flat_*<1\}$ or
enter $V_I$. (P1$_k$) at order $(\mathsf s+1;k)$ and (P2) bound $\|Eu\|_{(\mathsf s+1;k)}$, and $u$ is controlled at
order $(\mathsf s+1;k)$ on a neighbourhood $V_K$ of $\partial R_{\partial K^+,\mathrm{in}}$.

*Step 4: the trapped set.* Proposition 6.2 with the orders $(\mathsf s,\mathsf s_0)$, $U_\Gamma$ small and $Pu\in
H^{(\mathsf s;k)}$. Its $E$ has $\mathrm{WF}'(E)\cap\Gamma^u_{K^+} = \emptyset$, and by II.D Step 4 the backward curves
from $\mathrm{WF}'(E)\cap\partial\Sigma^+$ reach $\{t^\flat_*<1\}$ or enter $V_{\mathcal H}\cup V_K$ in locally bounded
times. (P1$_k$) at order $(\mathsf s+1;k)$ and (P2) bound $\|Eu\|_{(\mathsf s+1;k)}$, and $u$ is controlled at order
$(\mathsf s;k)$ on a neighbourhood $V_\Gamma$ of $\partial\Gamma_{K^+}$.

*Step 5: $\partial R_{\partial K^+,\mathrm{out}}$.* Proposition 5.2 (for II.D Proposition 3.3), with the orders $(\mathsf
s,\mathsf s_0)$ and (3.5) at the order $\mathsf s$. Its $E$ has $\mathrm{WF}'(E)\cap\partial W_{\mathrm{out}} =
\emptyset$, and by II.D Step 5 the backward curves from it enter $V_{\mathcal H}\cup V_K\cup V_\Gamma\cup V_I$ or reach
$\{t^\flat_*<1\}$. (P1$_k$) at order $(\mathsf s;k)$ bounds $\|Eu\|_{(\mathsf s;k)}$, and $u$ is controlled at order
$(\mathsf s;k)$ on a neighbourhood $V_{K,\mathrm{out}}$ of $\partial R_{\partial K^+,\mathrm{out}}$.

*Step 6: $\partial R_{\mathscr I^+,\mathrm{out}}$.* Proposition 3.2 (for II.D Proposition 3.6), with $t_{*,-} :=
\frac12$, the orders $(\mathsf s,\mathsf s_0)$ and (3.9) from (1.3). By its property (4), $\mathrm{WF}'(E)\cap\partial
R_{\mathscr I^+,\mathrm{out}}$ lies over $\{t^\flat_*\le\frac12\}$, where $u = 0$, and (P2) controls $u$ at every order
near it. The rest of $\mathrm{WF}'(E)$ lies in a punctured neighbourhood of $\partial R_{\mathscr I^+,\mathrm{out}}$,
from which, by II.D Step 6, the backward curves reach $\{t_* = 1\}$ or $\{t^\flat_*<1\}$ or enter $V_I\cup
V_{K,\mathrm{out}}$. (P1$_k$) at order $(\mathsf s;k)$ bounds $\|Eu\|_{(\mathsf s;k)}$, and $u$ is controlled at order
$(\mathsf s;k)$ on a neighbourhood $V_{I,\mathrm{out}}$ of $\partial R_{\mathscr
I^+,\mathrm{out}}\cap\{t^\flat_*\ge\frac12\}$.

*Conclusion.* As in II.D section 5, every point of $\partial\Sigma^+$ over $\mathrm{supp}\,\chi$ has a neighbourhood on
which $u$ is controlled at order $(\mathsf s;k)$, by Step 1 or Step 6, or by (P1$_k$) at order $(\mathsf s;k)$ from one
of the sets of Steps 2-6 or from $\{t^\flat_*<1\}$; the same holds on $\partial\Sigma^-$ with the antipodal sets, for
which sections 3-6 prove the same estimates. Finitely many such $B$, with (P0$_k$) off $\Sigma$, are jointly elliptic
over $\mathrm{supp}\,\chi$, and II.A Lemma 8.4 (c) at $(\mathsf s;k)$, with $\|\chi u\|_{(-N;k)}\le\|u\|_{(\mathsf
s_0;k)}$, gives (1.1), in the strong sense.

*Uniformity.* Each estimate used holds uniformly for $P$ with $\epsilon_{P,k}$ small: Propositions 3.2, 4.2, 5.2 and 6.2,
and II.A Propositions 9.1-9.2, whose constants are locally uniform at the regularity $(d_0;k)$. The backward segments are
those of II.D section 5, whose persistence under perturbation is shown there. $d_0$ is the largest of the numbers
required by the steps at the orders $\mathsf s_0$, $\mathsf s$ and $\mathsf s+1$ and by Lemmas 2.3-2.5, and it does not
depend on $k$. With II.D Remark 1.3, which applies here because the constants of sections 3-6 depend on the model only
through finitely many norms of its coefficients and through the dynamical constants of II.B, II.C and II.C$'$, this
proves (1.1).

*The tame estimate (1.2).* Let $d$ be the largest of the numbers $d$ of Lemma 2.4 for the families and orders of Steps
2-6 and of II.A Propositions 9.8-9.9 at the orders $\mathsf s+1$ and $\mathsf s$. A tame estimate proved with some
$d'\le d$ holds with $d$, as $\mathcal R_{d'}\le\mathcal R_d$ and $\epsilon_{P,d'}\le\epsilon_{P,d}$. If
$\epsilon_{P,d}$ is small, then $P$ is of class $((d_0;d),\ldots)$ and $\epsilon_{P,q}\le\epsilon_{P,d}$ for $q\le d$,
so for $k\le d$ (1.2) follows from (1.1). Let $k>d$. Run Steps 1-6 and the conclusion with the tame versions: (P0$_k$)
and (P1$_k$) with II.A Propositions 9.8 and 9.9, and (R$_k$) with (2.7). Each turns tame control on the sets where its
$E$ lies into tame control on a neighbourhood of its own set. In its right side, the terms at $k$ are at most
$C_k(\mathcal R_k+\epsilon_{P,k}\mathcal R_d)$, by tame control, and those at $d$ at most $C_d\mathcal R_d$, by Steps
1-6 run at $k = d$ without the tame versions, which control $u$ on each $E$-set at the orders used there (among them
$(\mathsf s+1;d)$), with a constant depending on $P$ only through $\epsilon_{P,d}$ ((1.1) at $d$ bounds only the order
$\mathsf s$; the eighty-fifth verifier, D206). The coefficient norm that multiplies the terms at $d$ is $\epsilon_{P,k}$
in (2.7); in II.A Propositions 9.8-9.9 it is $\|\mathbf L\|_{(d_0;k)}$, which is at most $C'_k+C\epsilon_{P,k}$ with
$C'_k$ depending only on $P_0$, and the part $C'_kC_d\mathcal R_d\le C'_kC_d\mathcal R_k$ joins the terms at $k$. The
constants of those propositions depend on $L$ only through bounds at $(d_0;d)$, that is, through $\epsilon_{P,d}$. II.A
Lemma 8.4 (c) has no coefficients of limited regularity, so the conclusion is linear in the bounds of the steps. This
gives (1.2), with $C_k$ depending on $P$ only through a bound for $\epsilon_{P,d}$. $\square$

## 8. What this part found

(D$'$1) *Two inclusions printed reversed.* In the proof of [Hin26c] Proposition 7.17, (7.57) reads
$H^{(s+1;k-2)}_{3b;b}\subset H^{(s;k-1)}_{3b;b}$, and in the proof of Proposition 7.22 the source writes
$H^{(s+2;k-3)}_{cu;b}\subset H^{(s;k-1)}_{cu;b}$. As inclusions both are false. For $k = 2$ the first reads
$H^{s+1}_{3b}\subset H^{(s;1)}_{3b;b}$, and over $(K^+)^\circ$, where $\partial_{t_*}$ and $\partial_x$ are 3b-vector
fields and $t_*\partial_{t_*}$ is a b-vector field, $u := \phi(x)\psi(t_*)e^{it_*}t_*^{-\alpha_K-1}$, with $\phi\in
C^\infty_c$ and $\psi$ a cut-off to $\{t_*\ge2\}$, lies in $H^{\infty,\alpha_K}_{3b}$, while $t_*\partial_{t_*}u =
i\phi\psi e^{it_*}t_*^{-\alpha_K}+(\text{terms in }H^{\infty,\alpha_K}_{3b})$ lies in no $H^{s,\alpha_K}_{3b}$, its
restrictions to the slabs $\{T\le t_*\le T+1\}$ having norms bounded below. What the arguments use is the estimate
$\|v\|_{(s+1;k-2)}\le C\|v\|_{(s;k-1)}$, the reverse inclusion, which holds ((F1), II.A Lemma 8.4 (d)); Lemmas 2.3-2.4
use it in this direction.

(D$'$2) *The weights of the tame estimate.* [Hin26c] (7.28) prints the weights $(2\alpha_I+2,\alpha_++2,\alpha_K)$ on the
last norm of $u$, $\|u\|_{(s_0;d)}$. The proof gives the weights of $u$ in (7.27), $(2\alpha_I,\alpha_+,\alpha_K)$, and
(1.2) states them. The printed weights demand more decay of $u$, which an application with $u$ at the weights of (7.27)
does not supply.

(D$'$3) *Words, not multi-indices.* The source writes $\vec X^\alpha = X_1^{\alpha_1}\cdots X_N^{\alpha_N}$ for
$\alpha\in\mathbb N_0^N$ and expands $[\vec X^\alpha,P]$ by its Lemma 3.25 (II.A Lemma 9.3) as $\sum_{\beta+\gamma =
\alpha}c_{\beta\gamma}(\mathrm{ad}^\beta_{\vec X}P)\vec X^\gamma$ ((7.37), (7.43), (7.61)). Near $\mathscr I^+$ the
fields do not commute: the rotation fields, and at $n = 3$ also $[X_1,X_2]\in x_IC^\infty$ ((7.31)). The expansion
(7.37) is exact even so, as deleting positions from an ordered power leaves an ordered power. But $X_j\vec X^\gamma$ is
not $\vec X^{\gamma+e_j}$, and the source needs it to read $Q_{ij}X_j\vec X^\gamma u$ as a component of $u^{(k)}$. So the
system closes only modulo reordering commutators, which the source does not track (an earlier version of this finding
also called (7.37) inexact; the eighty-fifth verifier, D206); they lie in the span of the family
and could be absorbed, so the gap is one of bookkeeping. With words (section 2) the expansion (F2) is exact and the
commuted system closes without reordering. At the horizon, over $\partial K^+$ and at the trapped set the fields commute
($[\partial_r,t_*\partial_{t_*}] = 0$, or a single field besides $I$), and words and multi-indices agree up to counting.

(D$'$4) *What changes at $n = 4$* (Lemma 3.1). There are six rotation fields $\Omega_{ab}$ on $\mathbb S^3$ for the
source's three, and $\Delta_{\mathbb S^3} = \pm\sum_{a<b}\Omega_{ab}^2$ exactly, where the source writes $\not\Delta$
modulo $x_I\mathrm{Diff}^2_{eb}$ as a sum of products $X_aX_b$. The constant $3 = n-1$ of II.C Lemma 3.4 replaces $2$. As
the bundle is trivial and b-vector fields act componentwise, $[V_1,V_2] = [V_i,\Omega_{ab}] = 0$ exactly, where the
source's connection gives $x_IC^\infty$ ((7.31)). None of this changes the structure of (C).

(D$'$5) *The estimates for systems.* The source applies its Propositions 7.4, 7.6-7.9 and 7.10 to the commuted equations,
operators on $E^{(k)}$ with off-diagonal first-order terms. For the radial point estimates it cites its Remark 7.5
("straightforwardly handled"), and for the trapping estimate nothing. Lemma 2.5 proves the estimates of II.D for such
systems under the sign condition (2.8), and sections 3-6 verify (2.8). At the trapped set this rests on the form of the
proof of II.D Proposition 4.2, in which the operator enters only through its principal symbol, through $\mathfrak p$ and
through one commutator.

(D$'$6) *The sign at the horizon.* The source computes the principal symbol of the commutator with $\partial_r$ from the
Kerr formula, $-ij\varrho^{-2}\mu'(r_+)\xi_0$ ((7.48)). The model here is not Kerr. Lemma 4.1 (c) computes it from the
constant $\beta_0$ of II.B (4.1), $\varsigma\rho\,\sigma_1(\mathrm{Im}(-Q)) = -\mathrm{diag}(j_\alpha)\beta_0\le0$, and
this is what keeps the threshold from rising with $k$.

(D$'$7) *Bookkeeping near $\mathscr I^+$.* The source carries the terms $[X_i,p_0]$, $[X_i,p_1]X_1$ and $p_1[X_i,X_1]$ in
the forcing $\tilde f^{(k),0}$ of (7.32), with $k-1$ b-derivatives and one eb-derivative of $u$; here they are order-0
coefficients $Q_{i1}$, $Q_{iJ}$ of the system (Lemma 3.1 (b)). Both work. In the system they do not enter (2.8), being of
order 0.

(D$'$8) *The order condition of the induction.* A forcing term with $q$ commutators carries $2$ e3b-derivatives and $k-q$
b-derivatives of $u$; trading $q-1$ b-derivatives for e3b-derivatives, it is controlled by the induction exactly when
$q-1\ge1+\lambda$ (Lemma 2.3). At the trapped set, where $\lambda = 1$, this is why the double commutators join the
system ((C2)). The source says this in words on p. 139; Lemma 2.3 states it as the condition that decides which
commutators enter $L^{(k)}$.

## Sources

[Hin26c] P. Hintz, arXiv:2606.28008v1. READ: pp. 127-141 (section 7.2: Proposition 7.11 with (7.27)-(7.28), Lemma 7.12
with (7.29)-(7.39), Remarks 7.13-7.14, Lemmas 7.15-7.16 with (7.40)-(7.48), Proposition 7.17 with (7.51)-(7.57), Remark
7.18, Lemmas 7.19-7.21 with (7.61)-(7.62), Proposition 7.22 with (7.67)-(7.69)).

Part II.A: sections 2 (Lemmas 2.2, 2.6, Corollary 2.3), 4.1, 7, 8 ((8.1), Lemmas 8.2, 8.4, 8.6) and 9 (Lemma 9.3,
Notation 9.4, Propositions 9.1, 9.2, 9.6, 9.8, 9.9, Corollary 9.7, (L4)). Part II.B: section 3.1, Definitions 3.1, 4.1,
(4.1), Lemma 5.2. Part II.C: section 1.1, Definitions 3.3, 3.6, Lemma 3.4, section 5.1. Part II.D: sections 1-5 (Lemma
1.1, Remark 1.3, Theorem 1.2, Propositions 3.1-3.6 and 4.2, Remark 3.7, the remark after Lemma 2.5).
