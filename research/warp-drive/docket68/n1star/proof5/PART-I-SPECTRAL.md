# Part I.A. The spectral family at bounded nonzero frequencies, at n = 4, on bundles

*Status.* Verified. Proved at D189; returned to verified at D195, when the seventy-ninth verifier, reading Part II.A$'$,
which copied them, found that the cut-offs of Proposition 5.2 are not equal to 1 where the proof needs them. They are
repaired (D195), and the part is labelled proved again once the eightieth verifier has read the repair. Written out in
full (D185). Read line by line by the seventy-fourth verifier, whose two major and seven minor findings and nits are
seated (D186); the seventy-fifth confirmed those repairs and found two minor gaps and six nits, seated (D187); the
seventy-sixth, reading Part I.B, confirmed both D187 repairs (D189). Every earlier finding is seated and its repair read.
This part replaces, for the statements it covers, the deductions of `../N1STAR-PROOF.md` 10.84 (a)-(e) and 10.86 (a)-(e),
which re-ran [Hin26c] sections 9.1-9.2 on bundles at proof level and cited the standard steps. Here those steps are
proved, from the calculus statements listed in section 2, each READ at source in a text that states it for every
dimension. The source is [Hin26c] = P. Hintz, arXiv:2606.28008v1 (printed page = PDF page - 4). The calculus is that of
[HJS] = A. Hassell, Q. Jia, E. Sussman, *Lecture notes on non-elliptic Fredholm theory*, arXiv:2604.18956v1.

*What is proved here.* Theorem 7.2: [Hin26c] Theorem 9.5 at n = 4, for operators on a trivial bundle of any rank, with
two changes forced by n = 4 and one forced by a sign slip in the source, for a constant regularity order (Remark 1.1).
The n = 4 changes are that (9.20) and (9.21) read $A^{3/2+\bar S-\epsilon}$ and $\rho^{3/2+S}$ (his $1+\bar S$ and $1+S$
are the values at n = 3), and that the term $-\tfrac{n-1}{2}$ in the operator is $-\tfrac32$. The sign slip is in (9.45)
and its repair is Lemma 4.8. The constants are uniform under continuous perturbations of the operator (section 8). The
full expansion (9.21) is proved in its first step only (Theorem 7.2 (5)), which is what the record uses.

*How it is organised.* Section 1 fixes the setting and the hypotheses (H1)-(H5), stated for the spectral family alone.
Section 2 lists the calculus. Section 3 proves the one positive commutator lemma used throughout, with its
regularisation. Section 4 proves the three radial point estimates and the commutator lemma for b-regularity. Section 5
proves the elliptic and propagation estimates, and section 6 the estimates near the artificial boundary. Section 7
proves the theorem and section 8 its uniformity. Section 9 lists what this write-out found against the record.

## 1. Setting and hypotheses

### 1.1 The space

Let $\overline{\mathbb R^4}$ be the radial compactification of $\mathbb R^4$, with boundary
$\partial\overline{\mathbb R^4} \cong\mathbb S^3$. Near it we use $\rho = |x|^{-1}$ and $\omega = x/|x|\in\mathbb S^3$,
so that a neighbourhood of the boundary is $[0,\rho_1)_\rho\times\mathbb S^3_\omega$. Fix radii
$0 < r_0 - 2\delta_0 < r_0 < r_2 < r_h$ and set

$$\bar X := \{x : |x|\ge r_0\}\cup\partial\overline{\mathbb R^4},\qquad \partial X := \partial\overline{\mathbb R^4},
\qquad \partial_\sharp X := \{|x| = r_0\},\qquad \tilde X := \{|x| > r_0 - 2\delta_0\}\cup\partial X.$$

Write $r := |x|$. The radius $r_h$ is that of the horizon in (H3) and $\partial_\sharp X$ is the artificial boundary. All
operators below are defined on $\tilde X$. Every function space on $\bar X$ is built from a space on $\mathbb R^4$,
through the extendible and supported constructions at $\partial_\sharp X$ of section 6.1, and every Schwartz kernel used
has support in $\tilde X\times\tilde X$. The density is the Euclidean one,
$|dx| = r^3\,dr\,d\omega = \rho^{-5}\,d\rho\,d\omega$ near $\partial X$, where $d\omega$ is the round density on
$\mathbb S^3$.

### 1.2 The bundle

$E := \tilde X\times\mathbb C^N$, $N\ge 1$. The record's bundles are the restrictions to $X$ of $T^*M$ and $S^2T^*M$,
trivialised by $dt_*, dx^1,\dots,dx^4$ and their symmetric products, with $N = 5$ and $N = 15$; nothing below uses more
than that $E$ is trivial. (The letter $N$ also denotes Sobolev orders, as in $H^{-N}$, and in section 7.5 a nilpotency
index; the context separates them.) A *fibre inner product* is $h(x)(v,w) = \langle H(x)v, w\rangle_{\mathbb C^N}$, where
$H\in C^\infty(\overline{\mathbb R^4};\mathrm{End}\,\mathbb C^N)$ is Hermitian, smooth on the compactification (that is,
smooth in $(\rho,\omega)$ up to $\rho = 0$), and satisfies $c\,\mathrm{Id}\le H\le C\,\mathrm{Id}$ with $c>0$. $L^2_h :=
L^2(\mathbb R^4;\mathbb C^N)$ with the norm $\|u\|_h^2 = \int h(u,u)\,|dx|$, which is equivalent to the standard one. For
an operator $A$, $A^{*h} = H^{-1}A^*H$ is its formal adjoint in $L^2_h$, and $A^*$ its adjoint in the standard $L^2$.

### 1.3 The operator

Let $\mathbb C\ni\sigma\mapsto\hat P(\sigma)\in\mathrm{Diff}^2(\tilde X^\circ;E)$ be of the form

$$\hat P(\sigma) = \hat P(0) + \sigma T + \sigma^2 P_2 .\tag{1.1}$$

This is the form of the spectral family $e^{i\sigma t_*}P_0e^{-i\sigma t_*}$ of a $t_*$-translation-invariant
second-order operator $P_0$, with $T = -i[P_0,t_*]$ and $P_2$ of order 0 (cf. [Hin26c] (9.30)). The hypotheses are
these.

(H1) (*Principal symbol.*) $\sigma_2(\hat P(0)) = G_0\,\mathrm{Id}$, where $G_0\in C^\infty(T^*\tilde X^\circ)$ is real,
fibrewise quadratic and even in the fibres, and $\sigma_1(T) = \tau_1\,\mathrm{Id}$ with $\tau_1$ real and fibre-linear.
$P_2 = g_{00}\,\mathrm{Id}$ with $g_{00}$ a real function.

(H2) (*Structure at infinity*, [Hin26c] Definition 9.4 and (9.31) at $n = 4$.) On $\{\rho<\rho_1\}$,

$$T = 2i\rho\big(\rho\partial_\rho - \tfrac32 - S\big) - iQ,\qquad \hat P(0) = \rho^2P^{(0)},\qquad
g_{00}\in\rho^2C^\infty
(\overline{\mathbb R^4}),\tag{1.2}$$

where $S\in C^\infty(\overline{\mathbb R^4};\mathrm{End}\,\mathbb C^N)$, $Q\in\rho^3\mathrm{Diff}^1_b$, and
$P^{(0)}\in\mathrm{Diff}^2_b$ with $P^{(0)} - ((\rho D_\rho)^2 + \Delta_{\mathbb S^3})\,\mathrm{Id}\in\mathrm{Diff}^1_b +
\rho\,\mathrm{Diff}^2_b$. All b-operators here have $\mathrm{End}\,\mathbb C^N$-valued coefficients smooth on the
compactification, $D = -i\partial$, and $\Delta_{\mathbb S^3}\ge 0$ is the Laplacian of the round metric. The first
equation in (1.2) is the meaning of "$-\tfrac{n-1}{2}$" at $n = 4$. Set

$$\bar S := \inf_{p\in\partial X}\ \min\mathrm{Re}\,\mathrm{spec}\,S(0,p)\qquad\text{([Hin26c] (5.2))}.$$

(H3) (*The horizon*, [Hin26c] section 9.2.1 (1)-(4).) $\mathcal H := \{r = r_h\}$. $\mathcal R_+$ is one of the two
components of $N^*\mathcal H\setminus o$ and $\mathcal R_- := -\mathcal R_+$; both lie in $\Sigma_0 := \{G_0 = 0\}$. Let
$\rho_\infty$ be positive, homogeneous of degree $-1$ and even near $N^*\mathcal H$. The *future-directed rescaled
Hamilton vector field* on $\Sigma_0$ is $\mathsf H := \pm\rho_\infty H_{G_0}$ on the component $\Sigma_0^\pm$ containing
$\mathcal R_\pm$. Then for each sign:

$$\beta_0 := \rho_\infty^{-1}\mathsf H\rho_\infty > 0\ \text{on}\ \partial\mathcal R_\pm,\qquad
\beta := \inf_{\partial\mathcal R_\pm}\big(\mp\beta_0^{-1}\rho_\infty\tau_1\big) > 0,\tag{1.3}$$

and there is a quadratic defining function $q_\pm$ of $\partial\mathcal R_\pm$ in $\partial\Sigma_0$ with
$\mathsf H q_\pm \ge c\,q_\pm$ near $\partial\mathcal R_\pm$, for some $c > 0$. Here $\partial(\cdot)$ denotes the
boundary at fibre infinity, viewed in $S^*\tilde X^\circ$. For the record's spectral families,
$\mp\rho_\infty\tau_1 = \mathsf H t_*$ by $\tau_1 = -H_{G}t_*$ ([Hin26c] (9.30)), so the second condition is his
$\beta > 0$.

(H4) (*Dynamics at fibre infinity.*) $\partial\Sigma_0 = \partial\Sigma_0^+\sqcup\partial\Sigma_0^-$ lies over $\{r\le
r_e\}$ for some $r_e > r_h$. Every maximal integral curve of $\mathsf H$ in $\partial\Sigma_0\setminus (\partial\mathcal
R_+\cup\partial\mathcal R_-)$ tends to $\partial\mathcal R_+\cup\partial\mathcal R_-$ as its parameter tends to
$-\infty$, and reaches $\{r < r_0-\delta_0\}$ at a finite positive parameter. On $\{r_0 - 2\delta_0 < r < r_2\}$, $G_0$
is a Lorentzian form (signature $(1,3)$) on each fibre of $T^*\tilde X$, $dr$ is timelike for it ($G_0(dr) < 0$), and
$\mathsf H r < 0$ on $\partial\Sigma_0$ there: the future direction decreases $r$. (For a spectral family, $G_0$ is
$g^{-1}$ restricted to the annihilator of $\partial_{t_*}$, and such a restriction of a Lorentzian form is Lorentzian
wherever it contains a timelike covector, as $dr$ is inside the horizon.)

(H5) (*Uniformity data.*) $\hat P$ may depend on a parameter $b$ in a compact metric space $\mathcal B$, continuously
into the coefficient topology (every coefficient continuous in $b$ into $C^\infty$, and in the classes of (H2)). The
objects $\mathcal H$, $\rho_\infty$, $q_\pm$, $r_e$ in (H3)-(H4) may depend continuously on $b$, and the constants
$c$, $\inf\beta_0$, $\beta$ in (H3) and the lengths of the curves in (H4) are bounded uniformly. Section 8 uses (H5).

*Remarks on the hypotheses.* (a) By (H1) the principal symbol of $\hat P(\sigma)$, of order 2, is $G_0\,\mathrm{Id}$ for
every $\sigma$. Since $\hat P(0) - \hat P(0)^{*h}$ has vanishing principal symbol, $\mathrm{Im}_h\hat P(0) :=
(\hat P(0) - \hat P(0)^{*h})/2i\in\mathrm{Diff}^1$, and near $\partial X$ it lies in $\rho^2\mathrm{Diff}^1_b$. Indeed
$\hat P(0)\in\rho^2\mathrm{Diff}^2_b$ by (1.2), adjoints preserve $\rho^2\mathrm{Diff}^2_b$ for the density
$\rho^{-5}d\rho\,d\omega$ (a b-vector field's adjoint is a b-operator), and the b-principal symbols cancel. (b) By
(H1), for $\sigma\in\mathbb C$,

$$\sigma_1\big(\mathrm{Im}_h\hat P(\sigma)\big) = \sigma_1\big(\mathrm{Im}_h\hat P(0)\big) +
(\mathrm{Im}\,\sigma)\,\tau_1\,\mathrm{Id}.
\tag{1.4}$$

To see this, write

$$\mathrm{Im}_h(\sigma T) = (\sigma T - \bar\sigma T^{*h})/2i = (\mathrm{Re}\,\sigma)\,\mathrm{Im}_hT +
(\mathrm{Im}\,\sigma)\,\mathrm{Re}_hT$$

. Then $\mathrm{Im}_hT$ has order 0, $\sigma_1(\mathrm{Re}_hT) = \tau_1\,\mathrm{Id}$, and $\sigma^2P_2$ has order 0. (c)
(H3)-(H4) are [Hin26c]'s hypotheses in section 9.2.1 and the dynamics of section 9.1.1. For the record's operators on
Tangherlini and on nearby Myers-Perry metrics they are verified in the record: 10.19, 10.36 and 10.60 for the dynamics,
10.79 for the thresholds. That verification is not repeated here. (d) $\hat P(\sigma)^{*h}$ satisfies (H1)-(H4) as well,
with $\tau_1$, $S$, $Q$ replaced by $\tau_1$, $-S^{*h}$ and suitable $Q'$, and with $\sigma$ replaced by $\bar\sigma$.
Only its principal symbol and its imaginary part enter below, and they are computed where they are used.

### 1.4 Orders and thresholds

The phase space is the scattering cotangent bundle ${}^{\mathrm{sc}}\overline T^*\overline{\mathbb R^4}$, compactified in
the fibres. Its boundary consists of *fibre infinity*, ${}^{\mathrm{sc}}S^*\overline{\mathbb R^4}$, and the *boundary
face* ${}^{\mathrm{sc}}\overline T^*_{\partial X}\overline{\mathbb R^4}$ over $\partial X$, meeting at a corner. Near
$\partial X$ we write scattering covectors as $\xi\,dr + r\,\eta$, $\xi\in\mathbb R$, $\eta\in T^*\mathbb S^3$, so that
$(\rho,\omega,\xi,\eta)$ are coordinates ([Hin26c] section 9.2.2; $\xi,\eta$ are his
$\xi_{\mathrm{sc}},\eta_{\mathrm{sc}}$).

An *order pair* is $(s,\mathsf r)$ with $s\in\mathbb R$ a constant (regularity; Remark 1.1) and $\mathsf r\in
C^\infty({}^{\mathrm{sc}}\overline T^*_{\partial X}\overline{\mathbb R^4})$ (decay), each extended smoothly to a
neighbourhood of its face. For $\sigma_0\ne 0$ real it is *admissible for* $\sigma_0$ with weight $\alpha_+\in \mathbb R$
if:

(O1) $s = s_c$, a constant (Remark 1.1);

(O2) $\mathsf r$ is constant near $R_{\sigma_0,\mathrm{in}}$ and near $R_{\mathrm{out}}$ (defined in (4.6)), and on the
characteristic set $\Sigma_{\sigma_0}^\partial$ of (4.7) it is monotone non-increasing along the future-directed flow
($\mathrm{sgn}(\sigma_0)\,\mathsf H_{\sigma_0}\mathsf r\le 0$, in the notation of section 4.2);

(O3) the thresholds ([Hin26c] (9.16a)-(9.16c)): with respect to some fibre inner products, chosen separately for each
radial set (section 2.4),

$$s_c > \tfrac12 + \vartheta_{\mathcal H},\qquad \mathsf r + \alpha_+ > \tfrac12(-1 + \vartheta_{\mathrm{in}})\
\text{at}\
R_{\sigma_0,\mathrm{in}},\qquad \mathsf r + \alpha_+ < -\tfrac12 + \bar S\ \text{at}\ R_{\mathrm{out}}.\tag{1.5}$$

Here $\vartheta_{\mathcal H} := \max_\pm\sup_{\partial\mathcal R_\pm}\lambda_{\max}\big(\beta_0^{-1}p_{1,\pm}(0)\big)$,
where $p_{1,\pm}(\sigma) := \pm\rho_\infty\sigma_1(\mathrm{Im}_h\hat P(\sigma))$, an $h$-self-adjoint endomorphism; this
is [Hin26c] (5.17) (Remark 4.3 below). Next,
$\vartheta_{\mathrm{in}} := \sup_{\partial X}\lambda_{\max}\big(p_{\mathrm{in}} - (S + S^{*h})\big)$ with
$p_{\mathrm{in}} := \sigma(\rho^{-1}\mathrm{Im}_h\hat P(0))|_{\xi = -2,\eta = 0}$ ([Hin26c] (9.32), (9.38b); Proposition
4.6). $\lambda_{\max}$ and $\lambda_{\min}$ are the extreme eigenvalues of an $h$-self-adjoint endomorphism. For complex
$\sigma = \sigma_0 + i\sigma_1$, the orders used are those for $\sigma_0$.

The spaces are those of [Hin26c] Theorem 9.5:

$$\bar H^{s,\mathsf r} := \bar H^{s,\mathsf r}_{\mathrm{sc}}(\bar X;E),\quad \dot H^{s,\mathsf r} := \dot H^{s,\mathsf
r}_
{\mathrm{sc}}(\bar X;E),$$

extendible, resp. supported, at $\partial_\sharp X$ (section 6.1), with the scattering Sobolev spaces of [HJS] Definition
10.2 on $\mathbb R^4$ (constant regularity order, variable decay order), componentwise.

*Remark 1.1 (constant regularity order; D186).* [Hin26c] lets the regularity order vary at fibre infinity over a region
$\{r > r_\Gamma\}$, $r_\Gamma > r_e$, where $\hat P(\sigma)$ is elliptic. The calculus READ here takes the differential
order constant ([HJS] p. 77: "we will take the differential order to be constant, and the spatial order to be variable"),
and every proof below uses only $s\equiv s_c$, so Theorem 7.2 is proved for constant $s$. Part I.B (in preparation)
proves in its section 2 a calculus with variable orders in all three senses; at $h = 1$ it would supply the elliptic
estimate at a variable $s$ over $\{r > r_\Gamma\}$, should a later part need it. Whether one does is recorded where
Theorem 7.2 is used.

## 2. The calculus

### 2.1 What is used, and where it is stated

All statements are for $\mathbb R^n$ with $n$ arbitrary, so they hold at $n = 4$. Every operator below has Schwartz
kernel supported in $\tilde X\times\tilde X$, and $\bar X\subset\overline{\mathbb R^4}$, so the calculus on
$\mathbb R^4$ is the calculus used. READ at source ([HJS], arXiv:2604.18956v1, 2026-10-25; page numbers printed):

(C1) (composition, p. 9; principal symbol, pp. 49-50) $\Psi^{m,\ell}_{\mathrm{sc}}\circ\Psi^{m',\ell'}_{\mathrm{sc}}
\subset\Psi^{m+m',\ell+\ell'}_{\mathrm{sc}}$ (2.1); Proposition 7.4: "$A\in\Psi^{m,l}_{\mathrm{sc}}(M)\Rightarrow
A^*\in\Psi^{m,l}_{\mathrm{sc}}(M)$", and "$\sigma_{m_1+m_2,l_1+l_2}(AB) = \sigma_{m_1,l_1}(A)\sigma_{m_2,l_2}(B)$"
(7.29), the principal symbol taking values in $S^{m,l}_{\mathrm{sc}}/S^{m-1,l-1}_{\mathrm{sc}}$ (Definition 7.2).

(C2) (commutators, p. 50) Proposition 7.5: "$[A,B]\in\Psi^{m_1+m_2-1,l_1+l_2-1}_{\mathrm{sc}}(M)$ and
$\sigma(i[A,B]) = \{\sigma(A),\sigma(B)\}$", the Poisson bracket being $H_pa$, with the scattering Hamilton vector field
(7.34).

(C3) (boundedness, p. 20) Proposition 3.11: "If $A\in\Psi^{m,l}_{\mathrm{sc}}$, then, for all $s,r\in\mathbb R$, A maps
$A : H^{s,r}_{\mathrm{sc}}\to H^{s-m,r-l}_{\mathrm{sc}}$ ... and does so boundedly". Remark 3.12: "Op(a), viewed as an
element of $L(H^{s,r}_{\mathrm{sc}}, H^{s-m,r-l}_{\mathrm{sc}})$, depends continuously on a". Since $a\mapsto
\mathrm{Op}(a)$ is linear and continuous from the Fréchet space $S^{m,l}_{\mathrm{sc}}$ to a Banach space, it is
bounded by one seminorm: *a family bounded in $\Psi^{m,l}$ is uniformly bounded* $H^{s,r}\to H^{s-m,r-l}$.

(C4) (compactness, p. 20) Proposition 3.13: "For any $s,s',r,r'$, with $s<s'$ and $r<r'$, the embedding
$H^{s',r'}_{\mathrm{sc}}\hookrightarrow H^{s,r}_{\mathrm{sc}}$ is compact." (Duality, p. 19: Proposition 3.7, the
$L^2$-pairing identifies $(H^{s,r}_{\mathrm{sc}})^*$ with $H^{-s,-r}_{\mathrm{sc}}$.)

(C5) (ellipticity, pp. 12, 29, 79) Proposition 2.3 ("Every elliptic element of the scattering calculus has a
parametrix"), Proposition 4.10 (microlocal parametrix at a closed subset of the elliptic set: "$AB - 1$, $BA - 1$ have
$\mathrm{WF}'_{\mathrm{sc}}$ disjoint from p. This also applies with p replaced by any closed subset"), Proposition 10.1
(variable orders). Proposition 4.9 (microlocality): "$\mathrm{WF}^{s,r}_{\mathrm{sc}}(Au)\subseteq\mathrm{WF}^{s+m,r+l}_
{\mathrm{sc}}(u)\cap\mathrm{WF}'_{\mathrm{sc}}(A)$".

(C6) (variable orders, pp. 77-80) Section 10.1: symbol classes $S^{m,l}_{\mathrm{sc}}$ with $l$ variable, defined with
the vector fields $\langle x\rangle^{-\delta}\mathcal V_b$ (10.3)-(10.4), so that "the logarithmic factor" in derivatives
of $\langle x\rangle^{l(x,\xi)}$ costs an arbitrary $\delta > 0$; composition and the principal symbol (section 10.2);
Definition 10.2 and section 10.3 (the spaces, independent of the choices, Hilbert, with the boundedness of
$\Psi^{m,l}_{\mathrm{sc}}$).

(C7) (bundles, pp. 52-53) Section 7.5: "$\Psi^{m,l}_{\mathrm{sc}}(M;E,F) := C^\infty(X;\mathrm{Hom}(E,F))\otimes
\Psi^{m,l}_{\mathrm{sc}}(M)$ ... Equivalently, an element in $\Psi^{m,l}_{\mathrm{sc}}(M;E,F)$ is a matrix with entries
in $\Psi^{m,l}_{\mathrm{sc}}(M)$."

(C8) (a regularising family, p. 95) Lemma 12.5:
$T_t := \chi(t\langle z\rangle)\mathrm{Op}(\chi(\langle t\zeta\rangle)) \in\Psi^{-\infty,-\infty}_{\mathrm{sc}}$,
$t\in(0,t_0]$, with $T_t\to\mathrm{Id}$ strongly on each $H^{s,r}_{\mathrm{sc}}$; its proof records "$T_r$ being
uniformly bounded in $\Psi^{0,0}_{\mathrm{sc}}$ and $T_r\to\mathrm{Id}$ in the operator topology of
$\Psi^{\delta,\delta}_{\mathrm{sc}}$".

In the interior, at fibre infinity, the scattering calculus restricted to kernels supported in a compact set is the
classical calculus, and the scattering principal symbol there is the classical one: over a compact set $\langle x\rangle$
is bounded above and below, so the scattering estimates of order $(m,\ell)$ for symbols supported over it are the
Kohn-Nirenberg estimates of order $m$. ([HJS] Proposition 4.1, cited here before D186, is a statement about wave front
sets.)

### 2.2 Matrix-valued operators

Write
$\Psi^{m,\ell} := \Psi^{m,\ell}_{\mathrm{sc}}(\mathbb R^4;\mathbb C^N) = M_N(\Psi^{m,\ell}_{\mathrm{sc}}(\mathbb R^4))$
by (C7), and $H^{s,\mathsf r} := (H^{s,\mathsf r}_{\mathrm{sc}})^N$. The principal symbol of $A = (A_{ij})$ is the matrix
$(\sigma(A_{ij}))$.

**Lemma 2.1.** (a) $\Psi^{m,\ell}\circ\Psi^{m',\ell'}\subset\Psi^{m+m',\ell+\ell'}$ and $\sigma(AB) =
\sigma(A)\sigma(B)$, a matrix product. (b) For a fibre inner product $h$, $A^{*h}\in\Psi^{m,\ell}$ and $\sigma(A^{*h}) =
\sigma(A)^{*h} := H^{-1}\sigma(A)^\dagger H$. (c) If $A = \tilde a\,\mathrm{Id}$ with $\tilde
a\in\Psi^{m,\ell}_{\mathrm{sc}}$ scalar, and $B\in\Psi^{m',\ell'}$, then $[A,B]\in\Psi^{m+m'-1,\ell+\ell'-1}$ and
$\sigma(i[A,B]) = H_a\sigma(B)$, entrywise. If $A\in\Psi^{m,\ell}$ has scalar principal symbol $a\,\mathrm{Id}$, and $B$
has scalar principal symbol $b\,\mathrm{Id}$, then $[A,B]\in\Psi^{m+m'-1,\ell+\ell'-1}$ and $\sigma(i[A,B]) =
(H_ab)\,\mathrm{Id}$. More generally, if $A$ has scalar principal symbol, then $[A,B]\in\Psi^{m+m'-1,\ell+\ell'-1}$ for
every $B\in\Psi^{m',\ell'}$: write $A = \tilde a\,\mathrm{Id} + A'$ with $A'\in\Psi^{m-1,\ell-1}$ and use the first
statement and (a). This is what is meant below when a commutator with an operator of scalar principal symbol lowers both
orders (D186). (d) The statements (C3)-(C6) and (C8) hold for $\Psi^{m,\ell}$ and $H^{s,\mathsf r}$, with
$T_t\,\mathrm{Id}$ in (C8), and ellipticity meaning that the principal symbol is invertible with inverse bounded in the
inverse orders.

*Proof.* (a) $(AB)_{ij} = \sum_kA_{ik}B_{kj}$, with (C1) entrywise. (b) $(A^*)_{ij} = (A_{ji})^*$, so
$\sigma(A^*) = \sigma(A)^\dagger$ by (C1). Multiplication by $H$ or $H^{-1}$ lies in $\Psi^{0,0}$: a function smooth on
$\overline{\mathbb R^4}$ is a symbol of order $(0,0)$, its $x$-derivatives of order $k$ being $O(\langle x\rangle^{-k})$.
Then (a) gives (b). (c) $[\tilde a\,\mathrm{Id},B]_{ij} = [\tilde a, B_{ij}]$, with (C2). For the second statement write
$A = \tilde a\,\mathrm{Id} + A'$ and $B = \tilde b\,\mathrm{Id} + B'$, with $A'\in\Psi^{m-1,\ell-1}$ and
$B'\in\Psi^{m'-1,\ell'-1}$. Then $[A',B']\in\Psi^{m+m'-2,\ell+\ell'-2}$ by (a); $[\tilde a\,\mathrm{Id},B']$ and
$[A',\tilde b\,\mathrm{Id}]$ lie there by the first statement; and $[\tilde a,\tilde b]$ gives $H_ab$. (d) Boundedness,
compactness and duality are statements about each entry. For an elliptic $A$, take
$B_0 := \mathrm{Op}(\sigma(A)^{-1} \chi)$ for a cut-off $\chi$, and run the Neumann series of [HJS] Proposition 2.3 with
matrices: $AB_0 = \mathrm{Id} - R_1$, $R_1\in\Psi^{-1,-1}$ by (a), and the asymptotic sum $\sum R_1^j$ exists entrywise.
The microlocal versions are identical. $\square$

**Lemma 2.2 (square roots).** Let $\mathcal K$ be a compact set of $h$-self-adjoint endomorphisms with spectra in
$[c,\infty)$, $c > 0$. Then $Q\mapsto Q^{1/2}$ (the $h$-positive square root) is real-analytic on a neighbourhood of
$\mathcal K$ in $\mathrm{End}\,\mathbb C^N$, with $Q^{1/2} = \frac1{2\pi i}\oint_\gamma z^{1/2}(z-Q)^{-1}\,dz$, $\gamma$
a fixed contour in $\{\mathrm{Re}\,z > 0\}$ around $[c/2, C]$. Consequently, if $q$ is an $h$-self-adjoint symbol in a
bounded family in $S^{2\mu,2\nu}$ (possibly with variable orders), with $q\ge c\langle\xi\rangle^{2\mu}\langle x\rangle^
{2\nu}$ on a set $W$ of phase space, then on $W$, $q^{1/2}$ is an $h$-self-adjoint symbol, bounded in $S^{\mu,\nu}$, and
$(q^{1/2})^{2} = q$.

*Proof.* The integral is $Q^{1/2}$ for $Q$ $h$-self-adjoint with spectrum inside $\gamma$: diagonalise $Q$ in an
$h$-orthonormal basis and use Cauchy's formula. It is holomorphic in the entries of $Q$ wherever $\gamma$ avoids
$\mathrm{spec}\,Q$. For the symbols, set $\lambda := \langle\xi\rangle^{\mu}\langle x\rangle^{\nu}$ (or the
variable-order elliptic weight of (C6)), so $q^{1/2} = \lambda(\lambda^{-2}q)^{1/2}$. Here $\lambda^{-2}q$ is bounded in
$S^{0,0}$ with values in a compact set of positive matrices, the chain rule gives the symbol estimates of
$(\lambda^{-2}q)^{1/2}$, and the product rule those of $q^{1/2}$. $\square$

**Lemma 2.3 (microlocal square root).** Let $K = K^{*h}\in\Psi^{2\mu,2\nu}$ have principal symbol $k$ with $k\ge
c\langle\xi\rangle^{2\mu}\langle x\rangle^{2\nu}$ on a neighbourhood $W$ of a closed set $W_0$ of the boundary of phase
space. Then there is $L\in\Psi^{\mu,\nu}$ with $\mathrm{WF}'(K - L^{*h}L)\cap W_0 = \emptyset$. The construction depends
continuously on $K$, and so is uniform for bounded families with a uniform $c$.

*Proof.* Let $\chi\in C^\infty$ equal 1 near $W_0$ with support in $W$. Set $L_0 := \mathrm{Op}(\chi k^{1/2})$, by
Lemma 2.2, and replace it by $(L_0 + L_0^{*h})/2$. Then $K - L_0^{*h}L_0$ is $h$-self-adjoint, and by Lemma 2.1 it lies
in $\Psi^{2\mu-1,2\nu-1}$ microlocally near $W_0$, with $h$-self-adjoint principal symbol $k_1$. Given $L_0,\dots,
L_{j-1}$ with $K - (\sum_{i<j}L_i)^{*h}(\sum_{i<j}L_i)\in\Psi^{2\mu-j,2\nu-j}$ near $W_0$, of principal symbol $k_j$,
solve $k^{1/2}l_j + l_jk^{1/2} = k_j$ for $l_j$. The Lyapunov equation has a unique solution, which is $h$-self-adjoint,
given by $l_j = \int_0^\infty e^{-\tau k^{1/2}}k_je^{-\tau k^{1/2}}\,d\tau$, because $k^{1/2}\ge c^{1/2}$ on $W$; it
lies in $S^{\mu-j,\nu-j}$ by the chain rule. With $L_j := \mathrm{Op}(\chi l_j)$, the error drops one order near $W_0$.
Then $L\sim\sum L_j$ (asymptotic sum, (C1)). $\square$

### 2.3 Inner products near $\partial X$

**Lemma 2.4 ([Hin26c] Lemma 5.12, at $n = 4$).** For every $\epsilon>0$ there is a fibre inner product $h$ such that
$\tfrac12\lambda_{\min}(S + S^{*h})\ge\bar S - \epsilon$ at every point of $\partial X$.

*Proof.* At one point $p$, let $S(0,p) = V(D + N)V^{-1}$ with $D$ diagonal, $\mathrm{Re}\,D\ge\bar S$ and $N$ nilpotent
upper triangular in Jordan form. Let $D_t := \mathrm{diag}(1,t,t^2,\dots)$. Then $D_t^{-1}(D + N)D_t = D + tN$, with
$\|tN\|\le t$. In the inner product $\langle u,v\rangle_t := \langle D_t^{-1}V^{-1}u, D_t^{-1}V^{-1}v\rangle$, $S(0,p)$
is unitarily equivalent to $D + tN$, so $\mathrm{Re}\langle Su,u\rangle_t\ge(\bar S - t)|u|_t^2$. Take $t = \epsilon/2$.
The inequality $\mathrm{Re}\,h(Su,u)\ge(\bar S - \epsilon)h(u,u)$ is open in $p$, so it holds for this constant inner
product on a neighbourhood of $p$. It is also convex in $h$: if it holds for $h_1,\dots,h_k$, it holds for
$\sum \chi_ih_i$ with $\chi_i\ge0$ and $\sum\chi_i = 1$. Cover $\partial X$ by finitely many such neighbourhoods, take a
subordinate partition of unity, and extend the resulting inner product smoothly to $\overline{\mathbb R^4}$. Since
$\tfrac12\lambda_{\min}(S + S^{*h}) = \min_{h(u,u)=1}\mathrm{Re}\,h(Su,u)$, this is the claim. $\square$

Different estimates below use different fibre inner products. All $L^2_h$ norms are equivalent, so each estimate
proved in one inner product holds in any other with a changed constant. No single inner product needs to serve two
radial sets.

## 3. The positive commutator lemma

Orders are pairs, $\mathbf s = (s,\mathsf r)$, the decay order possibly variable (C6), with $\mathbf 1 := (1,1)$ and
$\mathbf N := (N,N)$. Inequalities between orders hold componentwise and pointwise. For an operator family,
*microsupported in $K$ uniformly* means that the full symbols are supported in the closed set $K$, modulo a family
bounded in $\Psi^{-\infty,-\infty}$. For a fibre inner product $h$ and $P\in\Psi^{\mathbf m}$, write

$$P_R := \mathrm{Re}_hP = \tfrac12(P + P^{*h}),\qquad P_I := \mathrm{Im}_hP = \tfrac1{2i}(P - P^{*h}).$$

**Lemma 3.1 (one step).** Let $P\in\Psi^{\mathbf m}$, let $\mathbf s$ be an order,
$\mathbf k := \mathbf s - \frac12(\mathbf m - \mathbf 1)$, and $\kappa\in(0,\frac12]$. Let $K_1\subset U$ with $K_1$
closed and $U$ open in the boundary of phase space, and let $G\in\Psi^{0,0}$ be elliptic on $\bar U$. Suppose that for
$\epsilon\in(0,1]$ there are the following.

(i) $\check A_\epsilon = \check A_\epsilon^{*h}$, bounded in $\Psi^{\mathbf k}$, in $\Psi^{\mathbf k - \kappa\mathbf 1}$
for each $\epsilon$, and microsupported in $K_1$ uniformly.

(ii) For a sign $\varsigma\in\{1,-1\}$, the operator $C_\epsilon := i[P_R,\check A_\epsilon^2] + \check A_\epsilon^2P_I +
P_I\check A_\epsilon^2$ satisfies

$$\varsigma C_\epsilon = -B_\epsilon^{*h}B_\epsilon - F_\epsilon + E_\epsilon^{*h}E_\epsilon + J_\epsilon P + R_\epsilon
.\tag{3.1}$$

The operators in (3.1) are as follows. $B_\epsilon$ is bounded in $\Psi^{\mathbf s}$, lies in $\Psi^{\mathbf s - \kappa
\mathbf 1}$ for each $\epsilon$, and converges to $B_0$ in $\Psi^{\mathbf s + \delta\mathbf 1}$ for every $\delta > 0$.
$\check A_\epsilon = Z_\epsilon B_\epsilon + Y_\epsilon$, with $Z_\epsilon$ bounded in $\Psi^{-\frac12(\mathbf m -
\mathbf 1)}$ and $Y_\epsilon$ bounded in $\Psi^{\mathbf k - \mathbf 1}$. $\langle F_\epsilon w, w\rangle_h\ge
-C_F\|w\|^2_{-\mathbf N}$ for every Schwartz $w$ ($F_\epsilon$ is never paired with $u$ itself, so it may have any order;
D186). $E_\epsilon$ is bounded in $\Psi^{\mathbf s}$ and lies in $\Psi^{\mathbf s - \kappa\mathbf 1}$ for each
$\epsilon$, $J_\epsilon$ in $\Psi^{2\mathbf s - \mathbf m}$, and $R_\epsilon$ in $\Psi^{2\mathbf s - \mathbf 1}$. All of
these are microsupported in $K_1$ uniformly, $E_\epsilon$ in a closed set $K_E$, and $J_\epsilon$ in a closed set
$K_J\subset \mathrm{Ell}(P)$.

Let $E\in\Psi^{0,0}$ be elliptic on $K_E$. Then there is $C$ such that for every $u\in H^{-\mathbf N}$ with $Gu\in
H^{\mathbf s - \kappa\mathbf 1}$, $GPu\in H^{\mathbf s - \mathbf m + \mathbf 1}$ and $Eu\in H^{\mathbf s}$, we have
$B_0u\in L^2$ and

$$\|B_0u\|^2\le C\big(\|GPu\|^2_{\mathbf s - \mathbf m + \mathbf 1} + \|Eu\|^2_{\mathbf s} + \|Gu\|^2_{\mathbf s -
\frac12\mathbf 1} + \|u\|^2_{-\mathbf N}\big).\tag{3.2}$$

$C$ depends only on $C_F$, on bounds for the families in their classes, and on finitely many seminorms of $P$, $G$ and
$E$.

*Proof.* Norms are those of $L^2_h$ and of $H^{\mathbf t}$ (any fixed choice, (C6)); $C$ changes from line to line.

*Step 0: microlocalisation.* By (C5) there is $\Phi\in\Psi^{0,0}$ with $\mathrm{WF}'(\Phi)\subset\mathrm{Ell}(G)$ and
$\mathrm{WF}'(\mathrm{Id} - \Phi)\cap(K_1\cup K_E\cup K_J) = \emptyset$. Let $v := \Phi u$. The microlocal parametrix
of $G$ gives

$$\|v\|_{\mathbf t}\le C(\|Gu\|_{\mathbf t} + \|u\|_{-\mathbf N})\ (\mathbf t\le\mathbf s - \kappa\mathbf 1),\qquad
\|\Phi Pu\|_{\mathbf s - \mathbf m + \mathbf 1}\le C(\|GPu\|_{\mathbf s - \mathbf m + \mathbf 1} + \|u\|_{-\mathbf N}),$$

and $Pv = \Phi Pu + [P,\Phi]u$. Here $\mathrm{WF}'([P,\Phi])\subset\mathrm{WF}'(\mathrm{Id} - \Phi)$, which is disjoint
from $K_1$. So if $W_\epsilon$ is any family bounded in some $\Psi^{\mathbf t}$ and microsupported in $K_1$ uniformly,
then $W_\epsilon[P,\Phi]$ and $W_\epsilon(\mathrm{Id} - \Phi)$ are bounded in $\Psi^{-\infty,-\infty}$ (the composition
formula (C1): the product of the symbols vanishes, and the remainders are bounded by seminorms). In particular

$$\|\check A_\epsilon Pv\|_{\frac12(\mathbf 1 - \mathbf m) + \kappa\mathbf 1}\le C(\|GPu\|_{\mathbf s - \mathbf m +
\mathbf 1} + \|u\|_{-\mathbf N}),\tag{3.3}$$

because $\check A_\epsilon\in\Psi^{\mathbf k - \kappa\mathbf 1}$ maps $H^{\mathbf s - \mathbf m + \mathbf 1}$ to

$$H^{\mathbf s - \mathbf m + \mathbf 1 - \mathbf k + \kappa\mathbf 1} = H^{\frac12(\mathbf 1 - \mathbf m) +
\kappa\mathbf 1}$$

. The bound (3.3) holds for each $\epsilon > 0$, with a constant that may depend on $\epsilon$. Likewise
$\check A_\epsilon v\in H^{\frac12(\mathbf m - \mathbf 1)}$ for each $\epsilon > 0$, as
$v\in H^{\mathbf s - \kappa\mathbf 1}$. Both pairings below are therefore of $H^{\mathbf t}$ with $H^{\mathbf t'}$,
$\mathbf t + \mathbf t'\ge 0$, and are defined by (C4).

*Step 1: the pairing.* For $\epsilon > 0$ and Schwartz $w$,

$$\langle C_\epsilon w, w\rangle = 2\,\mathrm{Im}\,\langle\check A_\epsilon Pw,\check A_\epsilon w\rangle.\tag{3.4}$$

This is algebra: $2\,\mathrm{Im}\langle\check A_\epsilon Pw,\check A_\epsilon w\rangle = \frac1i\langle (\check
A_\epsilon^2P - P^{*h}\check A_\epsilon^2)w, w\rangle$, and $\check A^2P - P^{*h}\check A^2 = [\check A^2,P_R] + i(\check
A^2P_I + P_I\check A^2)$. Let $w_t := T_tv$ with $T_t$ from (C8). We show that the right side of (3.4) at $w = w_t$ tends
to its value at $v$; $C_\epsilon$ itself is never applied to $v$, since with an absorbing term of top order it need not
act on $H^{\mathbf s - \kappa\mathbf 1}$ (D186). As $t\to0$:

$w_t\to v$ in $H^{\mathbf s - \kappa\mathbf 1}$, and $\check A_\epsilon w_t\to\check A_\epsilon v$ in $H^{\frac12(\mathbf
m - \mathbf 1)}$.

Write $Pv = \Phi Pu + [P,\Phi]u$ (Step 0), so that $\check A_\epsilon Pw_t = \check A_\epsilon T_t\Phi Pu + \check
A_\epsilon T_t[P,\Phi]u + \check A_\epsilon[P,T_t]v$. (This avoids $[\check A_\epsilon,T_t]$, which for a variable decay
order is bounded only in $\bigcap_\delta\Psi^{\mathbf k - \kappa\mathbf 1 - \mathbf 1 + (0,\delta)}$, [HJS] p. 79; D187.)
The first term tends to $\check A_\epsilon\Phi Pu$ in $H^{\frac12(\mathbf 1 - \mathbf m) + \kappa\mathbf 1}$, since
$T_t\to\mathrm{Id}$ strongly on $H^{\mathbf s - \mathbf m + \mathbf 1}$ and $\check A_\epsilon\in\Psi^{\mathbf k -
\kappa\mathbf 1}$ for the fixed $\epsilon$. The second is bounded in $\Psi^{-\infty,-\infty}$ uniformly in $t$, as
$\check A_\epsilon$ and $[P,\Phi]$ have disjoint microsupports and $T_t$ is bounded in $\Psi^{0,0}$, and it tends to
$\check A_\epsilon[P,\Phi]u$. In the third, $[P,T_t]$ is bounded in $\Psi^{\mathbf m - \mathbf 1}$ and tends to 0 in
$\Psi^{\mathbf m - \mathbf 1 + \delta\mathbf 1}$ (Lemma 2.1 (c); $P$ has constant orders), so the term is bounded in
$H^{\frac12(\mathbf 1 - \mathbf m)}$, since $v\in H^{\mathbf s - \kappa\mathbf 1}$, and tends to 0 as distributions,
hence weakly in $H^{\frac12(\mathbf 1 - \mathbf m)}$.

A weakly null sequence paired with a strongly convergent one tends to 0. So $\langle\check A_\epsilon Pw_t,\check
A_\epsilon w_t\rangle\to\langle\check A_\epsilon Pv,\check A_\epsilon v\rangle$.

*Step 2: the estimate.* By (3.1) and (3.4), for Schwartz $w$,

$$\|B_\epsilon w\|^2\le-\varsigma\cdot2\,\mathrm{Im}\langle\check A_\epsilon Pw,\check A_\epsilon w\rangle +
C_F\|w\|^2_{-\mathbf N} + \|E_\epsilon w\|^2 + \langle J_\epsilon Pw, w\rangle + \langle R_\epsilon w,w\rangle.$$

Take $w = w_t := T_tv$ and let $t\to0$, with $\epsilon > 0$ fixed. The left side tends to $\|B_\epsilon v\|^2$ and
$\|E_\epsilon w_t\|^2$ to $\|E_\epsilon v\|^2$, as $B_\epsilon, E_\epsilon\in\Psi^{\mathbf s - \kappa\mathbf 1}$;
$\langle R_\epsilon w_t,w_t\rangle\to\langle R_\epsilon v,v\rangle$, as $R_\epsilon\in\Psi^{2\mathbf s - \mathbf 1}$ and
$2\kappa\le1$; the first term converges by Step 1 and the $J$-term by the splitting in (d). So the inequality holds with
$v$ in place of $w$, and $F_\epsilon$ has dropped out. We bound each term uniformly in $\epsilon\in(0,1]$. (a)

$$|\langle\check A_\epsilon Pv,\check A_\epsilon v\rangle|\le \|\check A_\epsilon Pv\|_{-\frac12(\mathbf m - \mathbf
1)}\|\check A_\epsilon v\|_{\frac12(\mathbf m - \mathbf 1)}$$

. Since $\check A_\epsilon$ is bounded in $\Psi^{\mathbf k}$, Step 0 gives

$$\|\check A_\epsilon Pv\|_{-\frac12(\mathbf m - \mathbf 1)}\le C(\|GPu\|_{\mathbf s - \mathbf m + \mathbf 1} +
\|u\|_{-\mathbf N})$$

. Next,

$$\|\check A_\epsilon v\|_ {\frac12(\mathbf m - \mathbf 1)}\le\|Z_\epsilon B_\epsilon v\|_{\frac12(\mathbf m - \mathbf
1)} + \|Y_\epsilon v\|_ {\frac12(\mathbf m - \mathbf 1)}\le C\|B_\epsilon v\| + C\|v\|_{\mathbf s - \mathbf 1}$$

. So twice the term is at most

$$\frac12\|B_\epsilon v\|^2 + C(\|GPu\|^2_{\mathbf s - \mathbf m + \mathbf 1} + \|v\|^2_{\mathbf s - \frac12\mathbf
1} + \|u\|^2_{-\mathbf N})$$

. (b) $C_F\|v\|^2_{-\mathbf N}\le C\|u\|^2_{-\mathbf N}$. (c) $E_\epsilon v = E_\epsilon u - E_\epsilon(\mathrm{Id} -
\Phi)u$, and $E_\epsilon(\mathrm{Id} - \Phi)$ is bounded in $\Psi^{-\infty,-\infty}$ (Step 0), so $\|E_\epsilon v\|\le
C(\|E_\epsilon u\| + \|u\|_{-\mathbf N})\le C(\|Eu\|_{\mathbf s} + \|u\|_{-\mathbf N})$, the last by the microlocal
parametrix of $E$ on $K_E$ (D186; $[E,\Phi]$ is not residual). (d) Choose $\Phi_J\in\Psi^{0,0}$ microlocally the identity
near $K_J$, with $\mathrm{WF}'(\Phi_J)\subset\mathrm{Ell}(P)$ and $\mathrm{WF}'(\Phi_J)\cap\mathrm{WF}'(\mathrm{Id} -
\Phi) = \emptyset$; this is possible as $K_J$ is closed, lies in the open set $\mathrm{Ell}(P)$ and misses
$\mathrm{WF}'(\mathrm{Id} - \Phi)$. Then $\langle J_\epsilon Pv,v\rangle = \langle J_\epsilon Pv,\Phi_Jv\rangle$ plus a
term bounded by $C\|u\|^2_{-\mathbf N}$, since $(\mathrm{Id} - \Phi_J)^{*h}J_\epsilon$ is residual; the same splitting at
$w_t$ gives the convergence used above, as $\Phi_JT_tv\to\Phi_Jv$ in $H^{\mathbf s + \kappa\mathbf 1}$ (the bound below
puts $\Phi_Jv$ in $H^{\mathbf s + \mathbf 1}$, and $[\Phi_J,T_t]$ is bounded in $\Psi^{-1,-1}$ and tends to 0 strongly).
Then

$$|\langle J_\epsilon Pv,\Phi_Jv\rangle|\le\|J_\epsilon Pv\|_{-\mathbf s}\|\Phi_Jv\|_{\mathbf s}$$

, and the microlocal parametrix of $P$ on $\mathrm{WF}'(\Phi_J)$ gives
$\|\Phi_Jv\|_{\mathbf s} \le C(\|\Phi Pu\|_{\mathbf s - \mathbf m} + \|u\|_{-\mathbf N})$. (e)
$|\langle R_\epsilon v,v\rangle|\le C\|v\|^2_ {\mathbf s - \frac12\mathbf 1}$, and

$$\|v\|_{\mathbf s - \frac12\mathbf 1}\le C(\|Gu\|_{\mathbf s - \frac12\mathbf 1} + \|u\|_{-\mathbf N})$$

. Absorbing $\frac12\|B_\epsilon v\|^2$ and using Step 0,

$$\|B_\epsilon v\|^2\le C\big(\|GPu\|^2_{\mathbf s - \mathbf m + \mathbf 1} + \|Eu\|^2_{\mathbf s} + \|Gu\|^2_{\mathbf
s - \frac12\mathbf 1} + \|u\|^2_{-\mathbf N}\big)\quad\text{for all }\epsilon\in(0,1].$$

The left side is finite for each $\epsilon > 0$ (as $B_\epsilon\in\Psi^{\mathbf s - \kappa\mathbf 1}$), so nothing is
assumed about $B_0v$. The qualitative hypothesis $Gu\in H^{\mathbf s - \kappa\mathbf 1}$ is used only for the limits
$t\to0$ in Steps 1 and 2; the bound uses $\|Gu\|_{\mathbf s - \frac12\mathbf 1}$.

*Step 3: the limit.* $B_\epsilon v$ is bounded in $L^2$ and tends to $B_0v$ as distributions, since $B_\epsilon\to B_0$
in $\Psi^{\mathbf s + \delta\mathbf 1}$. A weak limit point in $L^2$ is therefore $B_0v$, with $\|B_0v\|\le
\liminf\|B_\epsilon v\|$. Finally $B_0u = B_0v + B_0(\mathrm{Id} - \Phi)u$, where $B_0(\mathrm{Id} - \Phi)\in
\Psi^{-\infty,-\infty}$. $\square$

**Lemma 3.2 (iteration).** Let $\Gamma$ be a closed subset of the boundary of phase space, $U_0$ an open neighbourhood of
it, and $\mathbf s_0 = \mathbf s - \tau\mathbf 1$ with $\tau > 0$ a constant. Suppose that for every $\kappa\in(0,
\frac12]$, every order $\mathbf s' = \mathbf s_0 + \tau'\mathbf 1$ with $\kappa\le\tau'\le\tau$, and every open $U$ with
$\Gamma\subset U\subset U_0$, the hypotheses of Lemma 3.1 hold with $(\mathbf s',\kappa, U)$ for some closed $K_1\subset
U$. Suppose this holds with the $E$-terms microsupported in a closed set $K_E(U)\subset\bar U_0\setminus\Gamma$ (or with
no $E$ term), and with $B_0$ elliptic on the closure of an open neighbourhood $U'$ of $\Gamma$. Let $G$ be elliptic on
$\bar U_0$. Then there are a neighbourhood $U_*$ of $\Gamma$ and a closed set $K_E^*\subset\bar U_0\setminus\Gamma$ such
that for every $E\in\Psi^{0,0}$ elliptic on $K_E^*$, every $B\in\Psi^{0,0}$ microsupported in $U_*$ and every $\mathbf
N$,

$$\|Bu\|_{\mathbf s}\le C\big(\|GPu\|_{\mathbf s - \mathbf m + \mathbf 1} + \|Eu\|_{\mathbf s} + \|Gu\|_{\mathbf s_0} +
\|u\|_{-\mathbf N}\big),\tag{3.5}$$

in the strong sense: if the right side is finite, so is the left.

*Proof.* Let $J$ be an integer with $J\ge4\tau$, $\kappa := \tau/J\le\frac14$, and $\mathbf s_j := \mathbf s_0 +
j\kappa\mathbf 1$, so that $\mathbf s_j - \kappa\mathbf 1 = \mathbf s_{j-1}$. Construct $U_0\supset U_1\supset\dots
\supset U_J\supset\Gamma$ inductively, $U_j$ being the $U'$ of the hypothesis for $(\mathbf s_j,\kappa, U_{j-1})$, with
$B_0^{(j)}$ elliptic on $\bar U_j$, and let $K_E^* := \bigcup_{j=1}^JK_E(U_{j-1})$, a finite union of closed sets missing
$\Gamma$ (the sets move with $U$, so one $K_E$ need not serve every step; D186). Let $G_0 := G$ and, for $j\ge1$, let
$G_j\in\Psi^{0,0}$ be elliptic on $\bar U_j$ with $\mathrm{WF}'(G_j)\subset\mathrm{Ell}(B_0^{(j)})$, so that
$\|G_ju\|_{\mathbf s_j}\le C(\|B_0^{(j)}u\| + \|u\|_{-\mathbf N})$ by (C5). Lemma 3.1 with $(\mathbf s_j,\kappa, U_{j-1},
G_{j-1})$ needs $G_{j-1}u\in H^{\mathbf s_j - \kappa\mathbf 1} = H^{\mathbf s_{j-1}}$ and gives

$$\|B_0^{(j)}u\|\le C\big(\|G_{j-1}Pu\|_{\mathbf s_j - \mathbf m + \mathbf 1} + \|Eu\|_{\mathbf s_j} +
\|G_{j-1}u\|_{\mathbf s_{j-1}} + \|u\|_{-\mathbf N}\big).$$

Here $\|G_{j-1}Pu\|\le C(\|GPu\| + \|u\|_{-\mathbf N})$, since $U_{j-1}\subset U_0$, and $\|Eu\|_{\mathbf s_j}\le
\|Eu\|_{\mathbf s}$. Inducting on $j$ gives (3.5) with $U_* := U_J$, using $\|Bu\|_{\mathbf s}\le C(\|B_0^{(J)}u\| +
\|u\|_{-\mathbf N})$. The strong sense holds because each step's qualitative hypothesis, $G_{j-1}u\in
H^{\mathbf s_{j-1}}$, is the previous step's conclusion. $\square$

**Remark 3.3 (logarithmic losses).** With variable orders, symbols of the commutants carry factors $\log\varrho$ (C6).
Suppose, in Lemma 3.1, that $B_\epsilon$ is only bounded in $\Psi^{\mathbf s + \delta\mathbf 1}$ for every $\delta > 0$,
and $R_\epsilon$ only in $\Psi^{2\mathbf s - \mathbf 1 + \delta\mathbf 1}$, while the other hypotheses hold as stated,
$\kappa < \frac12$, and $B_0$ has principal symbol bounded below by $c > 0$ times an elliptic weight of order $\mathbf
s$. Then the conclusion holds with the a priori term $\|Gu\|_{\mathbf s - \kappa\mathbf 1}$. The proof is unchanged,
except that (e) is bounded by $C\|v\|^2_{\mathbf s - \frac12\mathbf 1 + \delta\mathbf 1}\le C\|v\|^2_{\mathbf s -
\kappa\mathbf 1}$ for $\delta\le\frac12 - \kappa$, and $\|Bu\|_{\mathbf s}\le C(\|B_0u\| + \|u\|_{-\mathbf N})$ for $B$
microsupported in $\mathrm{Ell}(B_0)$: $b_0^{-1}$ is bounded by the inverse weight, so it is a symbol of order $-\mathbf
s$ in (C6)'s class. Lemma 3.2 holds with this variant, since its steps have $\kappa\le\frac14$. For fixed $\epsilon$,
$B_\epsilon$ now lies only in $\Psi^{\mathbf s - \kappa\mathbf 1 + \delta\mathbf 1}$, so in Step 2 the left side is not
known to converge. Instead, $B_\epsilon w_t\to B_\epsilon v$ in $H^{-\delta\mathbf 1}$, and $\|B_\epsilon w_t\|^2$ is
bounded by the right side at $w_t$, which converges to the right side at $v$; so $B_\epsilon v\in L^2$ and, by weak lower
semicontinuity, $\|B_\epsilon v\|^2\le\liminf\|B_\epsilon w_t\|^2$ is bounded by the right side at $v$ (D187). Likewise
$Y_\epsilon$ is bounded only in $\Psi^{\mathbf k - \mathbf 1 + 2\delta\mathbf 1}$, which is harmless in (a).

*The cut-off.* Fix once and for all $\psi\in C_c^\infty((-1,1))$, even, with $\psi = 1$ on $[-\frac12,\frac12]$,
$\psi'\le 0$ on $[0,\infty)$ and $\sqrt{-x\psi(x)\psi'(x)}\in C^\infty([0,\infty))$ ([Hin26c] (9.25)). For example,
let $\nu\in C^\infty([0,1))$ vanish on $[0,\frac12]$, be positive on $(\frac12,1)$ and equal $(1-x)^{-1}$ near 1, and
set $\psi(x) := \exp(-\int_0^{|x|}\nu^2)$ for $|x| < 1$ and $\psi := 0$ otherwise. Then $\psi$ is smooth, since
$\int_0^x\nu^2\to\infty$ like $(1-x)^{-1}$; $-\psi' = \nu^2\psi$ for $x\ge0$; and $\sqrt{-x\psi\psi'} = \sqrt x\,\nu\,
\psi$, smooth because $\nu = 0$ on $[0,\frac12]$ and $\nu\psi$ is smooth (flat at 1).

*The regulariser.* For $\kappa\in(0,\frac12]$ and a defining function $\varrho$ of a boundary face of phase space, let
$\varphi_\epsilon(\varrho) := (1 + \epsilon\varrho^{-1})^{-\kappa}$, $\epsilon\in(0,1]$, and $\theta_\epsilon :=
\epsilon\varrho^{-1}(1 + \epsilon\varrho^{-1})^{-1}\in[0,1)$. For any vector field $V$,

$$V(\varphi_\epsilon^2) = 2\kappa\,\theta_\epsilon\,(\varrho^{-1}V\varrho)\,\varphi_\epsilon^2,\qquad V(\varrho^{-a}
\varphi_\epsilon^2) = -(a - 2\kappa\theta_\epsilon)(\varrho^{-1}V\varrho)\,\varrho^{-a}\varphi_\epsilon^2.\tag{3.6}$$

Indeed $\varphi_\epsilon^2 = \varrho^{2\kappa}(\varrho + \epsilon)^{-2\kappa}$, so $V\log\varphi_\epsilon^2 = 2\kappa(1 -
\varrho(\varrho + \epsilon)^{-1})\varrho^{-1}V\varrho = 2\kappa\theta_\epsilon\varrho^{-1}V\varrho$. The same formula
shows that $\varphi_\epsilon$ is bounded in $S^0$ (in $\varrho$), lies in $S^{-\kappa}$ for each $\epsilon > 0$, and
tends to 1 in $S^\delta$ for every $\delta > 0$, and that $\theta_\epsilon$ is bounded in $S^0$. So regularising a
commutant of weight $\varrho^{-a}$, $a = 2\mathsf s' - 1$, replaces $\mathsf s'$ by an effective order $\mathsf
s'_\epsilon := \mathsf s' - \kappa\theta_\epsilon\in(\mathsf s' - \kappa,\mathsf s']$ in the component the regulariser
acts on. In Lemma 3.2 that interval is $(\mathsf s_{j-1},\mathsf s_j]\subset[\mathsf s_0,\mathsf s]$.

## 4. Radial point estimates

### 4.1 At the horizon ([Hin26c] Proposition 9.9)

Fix a sign and write $\mathcal R := \mathcal R_\pm$, $\mathsf H := \pm\rho_\infty H_{G_0}$ near $\partial\mathcal R$,
$p_1(\sigma) := p_{1,\pm}(\sigma) = \pm\rho_\infty\sigma_1(\mathrm{Im}_h\hat P(\sigma))$ and

$$\vartheta := \sup_{\partial\mathcal R}\lambda_{\max}\big(\beta_0^{-1}p_1(0)\big)\qquad\text{(with respect to } h).$$

By (1.4), $p_1(\sigma) = p_1(0)\pm(\mathrm{Im}\,\sigma)\rho_\infty\tau_1\,\mathrm{Id}$. So by (1.3), for
$\mathrm{Im}\,\sigma\ge0$,

$$\beta_0^{-1}p_1(\sigma)\le(\vartheta - \beta\,\mathrm{Im}\,\sigma)\,\mathrm{Id}\quad\text{at }\partial\mathcal
R.\tag{4.1}$$

**Lemma 4.1 (a defining function in $S^*\tilde X^\circ$).** There are $M$, $c' > 0$ and a neighbourhood $W$ of
$\partial\mathcal R$ in $S^*\tilde X^\circ$ such that $\tilde q := q_{\mathrm{ext}} + M(\rho_\infty^2G_0)^2$ is a
quadratic defining function of $\partial\mathcal R$ in $S^*\tilde X^\circ$ and $\mathsf H\tilde q\ge c'\tilde q$ on $W$.
Here $q_{\mathrm{ext}} := q_\pm\circ\pi$ for a smooth retraction $\pi$ of a neighbourhood of $\partial\mathcal R$ onto
$\partial\Sigma_0$, an extension with $dq_{\mathrm{ext}} = 0$ on $\partial\mathcal R$ (an arbitrary extension may carry a
term linear in $\rho_\infty^2G_0$, and then $\tilde q$ need not be a defining function; D186), and $\mathsf H$ is given
near $\partial \mathcal R$ by the same formula off $\Sigma_0$.

*Proof.* At $\partial\mathcal R$, $\mathsf H\rho_\infty = \beta_0\rho_\infty\ne0$, so $H_{G_0}\ne0$ and $dG_0\ne0$; hence
$y := \rho_\infty^2G_0$ defines $\partial\Sigma_0$ near $\partial\mathcal R$. Since $\mathsf HG_0 = 0$, $\mathsf Hy =
2\beta_0y$, with $\beta_0 := \rho_\infty^{-1}\mathsf H\rho_\infty$ extended as a smooth function, $\ge b_0 > 0$ near
$\partial\mathcal R$. $\mathsf H$ vanishes on $\partial\mathcal R$, which consists of radial points. So
$q_{\mathrm{ext}}$ and $\mathsf Hq_{\mathrm{ext}}$ vanish to second order at $\partial\mathcal R$, and so does $Z :=
\mathsf Hq_{\mathrm{ext}} - \frac c2q_{\mathrm{ext}}$. In local coordinates $(y,z,w)$ near a point of $\partial\mathcal
R$ ($\partial\mathcal R = \{y = 0, z = 0\}$): $Z(0,z,w)\ge\frac c2q_\pm\ge c_1|z|^2$; $\partial_yZ(0,z,w) = O(|z|)$,
since $\partial_yZ(0,0,w) = 0$; so $Z\ge c_1|z|^2 - C|y||z| - Cy^2\ge\frac{c_1}2|z|^2 - C'y^2$. Then

$$\mathsf H\tilde q = Z + \tfrac c2q_{\mathrm{ext}} + 4M\beta_0y^2\ge\tfrac{c_1}2|z|^2 + (4Mb_0 - C')y^2,$$

while $\tilde q\le C''(|z|^2 + y^2) + My^2$ and $\tilde q\ge c''(|z|^2 + y^2)$ near $\partial\mathcal R$. Take
$M\ge\max(C'/(2b_0), 2C_2)$, where by Taylor's formula $q_{\mathrm{ext}}\ge c_1|z|^2 - C|y||z| -
Cy^2\ge\frac{c_1}2|z|^2 - C_2y^2$, because $q_{\mathrm{ext}} = q_\pm$ on $\{y = 0\}$ and $dq_{\mathrm{ext}} = 0$ on
$\partial\mathcal R$; so $\tilde q\ge\frac{c_1}2|z|^2 + \frac M2y^2$ (D187). Take $c'$ small; finitely many coordinate
patches cover the compact set $\partial\mathcal R$. $\square$

**Proposition 4.2 (radial estimate at the horizon).** Let $\mathcal D\subset\{\mathrm{Im}\,\sigma\ge0\}$ be compact, $U$
a neighbourhood of $\partial\mathcal R$ in ${}^{\mathrm{sc}}S^*\overline{\mathbb R^4}$, and $N\in\mathbb R$.

(1) (*Direct.*) Let $s > s_0 > \frac12 + \vartheta$. There are $B, G\in\Psi^{0,0}$, microsupported in $U$, with kernels
supported near $\mathcal H$ and $B$ elliptic at $\partial\mathcal R$, such that for $\sigma\in\mathcal D$, in the strong
sense,

$$\|Bu\|_{H^s}\le C\big(\|G\hat P(\sigma)u\|_{H^{s-1}} + \|Gu\|_{H^{s_0}} + \|u\|_{H^{-N}}\big).\tag{4.2}$$

(2) (*Adjoint.*) Let $s > \frac12 + \vartheta$. There are $B, G, E\in\Psi^{0,0}$ as in (1), with $\mathrm{WF}'(E)\cap
\partial\mathcal R = \emptyset$, such that for $\sigma\in\mathcal D$, in the strong sense,

$$\|Bu\|_{H^{1-s}}\le C\big(\|G\hat P(\sigma)^{*h}u\|_{H^{-s}} + \|Eu\|_{H^{1-s}} + \|u\|_{H^{-N}}\big).\tag{4.3}$$

The same holds with $\hat P(\sigma)^{*h'}$ for any fibre inner product $h'$. Indeed $\hat P^{*h'} = \Theta^{-1}\hat
P^{*h}\Theta$ with $\Theta := H^{-1}H'$ invertible of order $(0,0)$, and conjugation by $\Theta$ preserves
microsupports and Sobolev spaces.

*Proof.* (1) We verify the hypotheses of Lemma 3.2 with $\Gamma = \partial\mathcal R$, $\mathbf m = (2,0)$, and
orders in the regularity component only (the kernels are compactly supported, so the decay order is immaterial). Fix
$s'\in[s_0,s]$ and a neighbourhood $U$ of $\partial\mathcal R$. Let $\chi_\infty := \chi(\rho_\infty)$, where $\chi\in
C^\infty$ equals 1 near 0 and is supported in $[0,\rho_*)$, and let $\psi_R := \psi(\varsigma_R\tilde q)$ for a large
parameter $\varsigma_R$, extended homogeneously of degree 0. Set

$$\check a_\epsilon := \rho_\infty^{-s'+\frac12}\varphi_\epsilon(\rho_\infty)\,\chi_\infty\,\psi_R,\qquad \check
A_\epsilon := \tfrac12\big(\mathrm{Op}(\check a_\epsilon)\mathrm{Id} + (\mathrm{Op}(\check a_\epsilon)\mathrm{Id})^{*h}
\big).$$

$\check A_\epsilon$ is $h$-self-adjoint with principal symbol $\check a_\epsilon\,\mathrm{Id}$. It is bounded in
$\Psi^{s'-1/2}$, lies in $\Psi^{s'-1/2-\kappa}$ for $\epsilon > 0$, and is microsupported in $\mathrm{supp}\,\psi_R$,
which lies in $U$ for $\varsigma_R$ large. This is (i), with $\mathbf k = s' - \frac12$.

By Lemma 2.1 (c), $\hat P(\sigma)_R$ has principal symbol $G_0\,\mathrm{Id}$ and $\hat P(\sigma)_I\in\Psi^1$ has
principal symbol $\sigma_1(\mathrm{Im}_h\hat P(\sigma))$, so

$$\sigma_{2s'}(C_\epsilon) = H_{G_0}(\check a_\epsilon^2)\,\mathrm{Id} + 2\check a_\epsilon^2\,\sigma_1(\mathrm{Im}_h\hat
P(\sigma)) = \pm\rho_\infty^{-1}\big[\mathsf H(\check a_\epsilon^2)\,\mathrm{Id} + 2\check
a_\epsilon^2p_1(\sigma)\big].$$

By (3.6) with $\varrho = \rho_\infty$, $a = 2s' - 1$, $V = \mathsf H$ (so $\varrho^{-1}V\varrho = \beta_0$) and the
regulariser of the step ($\kappa = s_j - s_{j-1}$),

$$\mathsf H(\check a_\epsilon^2) = \rho_\infty^{-2s'+1}\varphi_\epsilon^2\chi_\infty^2\big[-\beta_0(2s'_\epsilon - 1)
\psi_R^2 + 2\varsigma_R\psi_R\psi_R'\,\mathsf H\tilde q\big] + r_\epsilon,
\qquad s'_\epsilon := s' - \kappa\theta_\epsilon,$$

where $r_\epsilon$ collects the terms with $\chi_\infty'$. These are supported at bounded frequencies over a compact
set, so $r_\epsilon$ is bounded in $S^{-\infty}$. Let $Q_\epsilon := \beta_0(2s'_\epsilon - 1)\mathrm{Id} -
2p_1(\sigma)$. In Lemma 3.2 the order is $s' = s_j$ with $\kappa = s_j - s_{j-1}$, so $s'_\epsilon\in(s_{j-1},s_j]
\subset[s_0,s]$. With $s'_\epsilon\ge s_0$, (4.1) gives, at $\partial\mathcal R$,

$$Q_\epsilon\ge2\beta_0\big(s'_\epsilon - \tfrac12 - \vartheta + \beta\,\mathrm{Im}\,\sigma\big)\mathrm{Id}\ge2\beta_0
\big(s_0 - \tfrac12 - \vartheta\big)\mathrm{Id}.$$

Since $\beta_0 > 0$ near $\partial\mathcal R$ and $s'_\epsilon\ge s_0$, $Q_\epsilon\ge Q^{(0)} := \beta_0(2s_0 -
1)\mathrm{Id} - 2p_1(\sigma)$ there, for every $\epsilon$. $Q^{(0)}$ does not depend on $\epsilon$, is continuous in the
base point and in $\sigma\in\mathcal D$, and is at least $2\beta_0(s_0 - \frac12 - \vartheta)\mathrm{Id}$ at
$\partial\mathcal R$ by (4.1). ($Q_\epsilon$ itself is not equicontinuous in $\epsilon$ at $\rho_\infty = 0$, since
$\theta_\epsilon$ is not; D186.) So there is a neighbourhood $W'\subset W\cap U$ of $\partial\mathcal R$ and $c_Q > 0$
with $Q_\epsilon\ge c_Q\,\mathrm{Id}$ on $W'$. Choose $\varsigma_R$ so large that $\mathrm{supp}\,\psi_R\subset W'$, so
that also $\mathsf H\tilde q\ge c'\tilde q\ge0$ on $\mathrm{supp}\,\psi_R$ by Lemma 4.1. Let $\tilde\chi$ equal 1 on
$\mathrm{supp}\,\psi_R$ with support in $W'$, and set $\tilde Q_\epsilon := \tilde\chi Q_\epsilon + (1 -
\tilde\chi)c_Q\,\mathrm{Id}\ge c_Q\,\mathrm{Id}$. Define

$$b_\epsilon := \rho_\infty^{-s'}\varphi_\epsilon\chi_\infty\psi_R\,\tilde Q_\epsilon^{1/2},\qquad b_{R,\epsilon} :=
\rho_\infty^{-s'}\varphi_\epsilon\chi_\infty\Big(\frac{2\,\mathsf H\tilde q}{\tilde q}\Big)^{1/2}\sqrt{-x\psi(x)\psi'(x)}
\Big|_{x = \varsigma_R\tilde q}.$$

Both are smooth: the first by Lemma 2.2; the second because $\psi'(\varsigma_R\tilde q)\ne0$ only where $\tilde q\ge
(2\varsigma_R)^{-1}$, on which $\mathsf H\tilde q/\tilde q\ge c'$. They satisfy $b_\epsilon^{*h} = b_\epsilon$ and

$$\pm\rho_\infty\,\sigma_{2s'}(C_\epsilon) = -\rho_\infty\big(b_\epsilon^2 + b_{R,\epsilon}^2\,\mathrm{Id}\big) +
\rho_\infty r_\epsilon,$$

using $2\varsigma_R\psi_R\psi_R'\mathsf H\tilde q = -2(\mathsf H\tilde q/\tilde q)(-x\psi\psi')|_{x = \varsigma_R\tilde
q}$. Let $B_\epsilon := \frac12(\mathrm{Op}(b_\epsilon) + \mathrm{Op}(b_\epsilon)^{*h})$ and $B_{R,\epsilon} :=
\mathrm{Op}(b_{R,\epsilon})\mathrm{Id}$. By Lemma 2.1, $\pm C_\epsilon = -B_\epsilon^{*h}B_\epsilon - B_{R,\epsilon}^
{*h}B_{R,\epsilon} + R_\epsilon$ with $R_\epsilon$ bounded in $\Psi^{2s'-1}$ and microsupported in $\mathrm{supp}\,
\psi_R$. This is (3.1) with $\varsigma = \pm$, $F_\epsilon := B_{R,\epsilon}^{*h}B_{R,\epsilon}\ge0$, and no $E$ or $J$
term.

$B_\epsilon$ is bounded in $\Psi^{s'}$, lies in $\Psi^{s'-\kappa}$ for $\epsilon > 0$, and tends to $B_0$ (the same with
$\varphi_0 = 1$, $s'_0 = s'$) in $\Psi^{s'+\delta}$; $B_0$ is elliptic where $\psi_R = 1$ near fibre infinity, a
neighbourhood of $\partial\mathcal R$. With $z_\epsilon := \rho_\infty^{1/2}\tilde Q_\epsilon^{-1/2}$, bounded in
$S^{-1/2} = S^{-\frac12(\mathbf m - \mathbf 1)}$, we have $z_\epsilon b_\epsilon = \check a_\epsilon\,\mathrm{Id}$, so
$\check A_\epsilon - \mathrm{Op}(z_\epsilon)B_\epsilon$ is bounded in $\Psi^{s'-3/2}$. All constants are uniform in
$\sigma\in\mathcal D$: every symbol depends polynomially on $\sigma$, and $c_Q$, $W'$ and $\varsigma_R$ do not depend
on $\sigma$. Lemma 3.2 gives (4.2).

(2) For $\hat P(\sigma)^{*h}$: $\mathrm{Re}_h(\hat P^{*h}) = \hat P_R$ and $\mathrm{Im}_h(\hat P^{*h}) = -\hat P_I$.
Take the target order $\tilde s := 1 - s'$ ($s'\ge s$) and the same commutant with $\tilde s$ in place of $s'$. The
computation gives $\pm\rho_\infty\sigma(C_\epsilon) = \rho_\infty^{-2\tilde s+1}\varphi_\epsilon^2\chi_\infty^2[\psi_R^2
Q^\flat_\epsilon + 2\varsigma_R\psi_R\psi_R'\mathsf H\tilde q] + \rho_\infty r_\epsilon$, where

$$Q^\flat_\epsilon := \beta_0(1 - 2\tilde s_\epsilon)\mathrm{Id} - 2p_1(\sigma)\ge2\beta_0\big(s' - \tfrac12 -
\vartheta +
\beta\,\mathrm{Im}\,\sigma\big)\mathrm{Id}\ge c_Q\,\mathrm{Id}$$

at and near $\partial\mathcal R$, because $\tilde s_\epsilon\le\tilde s = 1 - s'$. So $\mp C_\epsilon = -B_\epsilon^{*h}
B_\epsilon + B_{R,\epsilon}^{*h}B_{R,\epsilon} + R_\epsilon$ with $b_\epsilon := \rho_\infty^{-\tilde s}\varphi_\epsilon
\chi_\infty\psi_R(\tilde Q^\flat_\epsilon)^{1/2}$ and $b_{R,\epsilon}$ as before. This is (3.1) with $\varsigma = \mp$
and $E_\epsilon := B_{R,\epsilon}$, which is microsupported in $\mathrm{supp}\,\psi'(\varsigma_R\tilde q)$, a closed set
disjoint from $\partial\mathcal R$. The regulariser only lowers $\tilde s_\epsilon$, which increases $Q^\flat_\epsilon$,
so the iteration of Lemma 3.2 runs from $\mathbf s_0 = -N$ with no threshold. Choose $E$ elliptic on the set $K_E^*$ of
Lemma 3.2, a finite union of such sets, closed and disjoint from $\partial\mathcal R$. $\square$

*Remark 4.3 (the threshold is [Hin26c]'s).* His (5.17) takes $\vartheta_{\mathcal H^+} := \sup_{N^*\mathcal H^+
\setminus o}\mathrm{spec}\,\big[\beta_0^{-1}\rho_\infty\sigma_1\big(\frac1{2i}(P_0 - P_0^*)\big)\big]$ with $\rho_\infty
:= \xi_0^{-1}$. That function is odd in the fibres, and $\beta_0^{-1}$ is his $\varrho^2/(2(r_+ - m))$ by his (4.28).
At covectors annihilating $\partial_{t_*}$, $\sigma_1(\frac1{2i}(P_0 - P_0^*)) = \sigma_1(\mathrm{Im}\,\hat P(0))$. So
on $\mathcal R_+$ his quantity is $\beta_0^{-1}p_{1,+}(0)$ and on $\mathcal R_-$ it is $\beta_0^{-1}p_{1,-}(0)$, and
$\max_\pm\vartheta_\pm = \vartheta_{\mathcal H^+}$. For the record's operators it is computed in 10.79 (`hthresh5.py`).

### 4.2 The geometry over $\partial X$

**Lemma 4.4 (symbols at the boundary face).** Assume (H1)-(H2), and write $\sigma = \sigma_0 + i\sigma_1$.

(a) At the boundary face, $\hat P(\sigma)\in\Psi^{2,0}$ has principal symbol $G_\sigma\,\mathrm{Id}$ with $G_\sigma :=
2\sigma\xi + \xi^2 + |\eta|^2$, $|\eta|$ the round norm. $T\in\Psi^{1,0}$ has principal symbol $2\xi\,\mathrm{Id}$ there.

(b) $\mathrm{Im}_hT = -\rho(S + S^{*h}) + T_2$ with $T_2\in\Psi^{1,-2}$, and
$\mathrm{Im}_h\hat P(0)\in\rho^2\mathrm{Diff}^1_b \subset\Psi^{1,-1}$. At $\rho = 0$, $\rho^{-1}\mathrm{Im}_h\hat P(0)$
has a principal symbol that is linear in $(\xi,\eta)$ and $h$-self-adjoint.

(c) For a symbol $p(\omega,\xi,\eta)$ at the boundary face, the scattering Hamilton vector field satisfies $H_p =
\rho\,\mathsf V_p$, with $\mathsf V_p$ a b-vector field. At $\rho = 0$,

$$\mathsf V_p = -(\partial_\xi p)\,(\rho\partial_\rho + \eta\cdot\partial_\eta) + (\eta\cdot\partial_\eta p)\,
\partial_\xi + H^{\mathbb S^3}_p,\tag{4.4}$$

where $H^{\mathbb S^3}_p$ is the Hamilton vector field of $p(\omega,\xi,\cdot)$ on $T^*\mathbb S^3$.

*Proof.* (a) $\rho^2\partial_\rho = -\partial_r$, whose symbol is $-i\xi$, so $2i\rho^2\partial_\rho$ has symbol $2\xi$.
The rest of $T$ lies in $\rho C^\infty + \rho^3\mathrm{Diff}^1_b\subset\Psi^{1,-1}$. $\rho^2(\rho D_\rho)^2$ and
$\rho^2\Delta_{\mathbb S^3}$ have symbols $\xi^2$ and $|\eta|^2$ at $\rho = 0$, since $\rho D_\rho$ has symbol
$-\rho^{-1}\xi$ and a covector $r\eta$ has length $|\eta|$. The remainder of $\hat P(0)$, in $\rho^2(\mathrm{Diff}^1_b +
\rho\mathrm{Diff}^2_b)\subset\Psi^{2,-1}$, vanishes at $\rho = 0$, and $\sigma^2g_{00}\in\Psi^{0,-2}$.

(b) Let $A := 2i\rho(\rho\partial_\rho - \frac32)$ act componentwise. For the density $\rho^{-5}d\rho\,d\omega$,
integration by parts gives $(\rho^2\partial_\rho)^\dagger = -\rho^2\partial_\rho + 3\rho$, so $A^\dagger = A$. Then
$A^{*h} = H^{-1}AH = A + 2i\rho^2H^{-1}(\partial_\rho H)$, and
$\mathrm{Im}_hA = -\rho^2H^{-1}\partial_\rho H\in\rho^2C^\infty \subset\Psi^{0,-2}$. Next,
$\mathrm{Im}_h(-2i\rho S) = -\rho(S + S^{*h})$, and
$\mathrm{Im}_h(-iQ) = -\mathrm{Re}_hQ\in \rho^3\mathrm{Diff}^1_b\subset\Psi^{1,-2}$. $\mathrm{Im}_h\hat P(0)$ is Remark
(a) of section 1.3, and $\rho^2\mathrm{Diff}^1_b = \rho\cdot\rho\mathrm{Diff}^1_b$ with
$\rho\mathrm{Diff}^1_b\subset\mathrm{Diff}^1_{\mathrm{sc}}$. The symbol of $\rho\mathrm{Diff}^1_b$ at $\rho = 0$ is
linear in $(\xi,\eta)$: its zeroth-order part lies in $\rho C^\infty$. Self-adjointness follows from Lemma 2.1 (b).

(c) READ ([HJS] p. 50, (7.33)-(7.34)): for covectors $\tau\frac{dx}{x^2} + \mu\cdot\frac{dy}x$,

$$H_p = \partial_\tau p\,(x^2\partial_x) + \partial_\mu p\,(x\partial_y) - (x^2\partial_xp + x\mu\cdot\partial_\mu
p)\partial_\tau -
(x\partial_yp - x(\partial_\tau p)\mu)\cdot\partial_\mu.$$

Here $x = \rho$ and $y = \omega$. From $dr = -d\rho/\rho^2$ we get
$\xi\,dr + r\eta = -\xi\frac{d\rho}{\rho^2} + \eta\cdot \frac{d\omega}\rho$, so $\tau = -\xi$ and $\mu = \eta$. Dividing
by $\rho$ and setting $\rho = 0$, with $\partial_\tau = -\partial_\xi$, gives (4.4). $\square$

So the face symbol of $\mathrm{Re}_h\hat P(\sigma)$ is $g_{\sigma_0} := 2\sigma_0\xi + \xi^2 + |\eta|^2$. Write
$\mathsf H_{\sigma_0} := \mathsf V_{g_{\sigma_0}}$. By (4.4),

$$\mathsf H_{\sigma_0} = -2(\sigma_0 + \xi)(\rho\partial_\rho + \eta\cdot\partial_\eta) + 2|\eta|^2\partial_\xi +
H_{|\eta|^2},\qquad\rho^{-1}\mathsf H_{\sigma_0}\rho = -2(\sigma_0 + \xi),\qquad\mathsf H_{\sigma_0}g_{\sigma_0} = 0.
\tag{4.5}$$

(Hintz writes the same, [Hin26c] p. 166.) For $\sigma_0\ne0$ define

$$R_{\sigma_0,\mathrm{in}} := \{\rho = 0,\ \xi = -2\sigma_0,\ \eta = 0\},\qquad R_{\mathrm{out}} := \{\rho = 0,\ \xi =
0,\
\eta = 0\},\tag{4.6}$$

$$\Sigma^\partial_{\sigma_0} := \{\rho = 0,\ g_{\sigma_0} = 0\}.\tag{4.7}$$

$R_{\mathrm{out}}$ is the zero section over $\partial X$.

**Lemma 4.5 (the flow over $\partial X$).** Let $\sigma_0\ne0$ and $\varepsilon_0 := \mathrm{sgn}\,\sigma_0$. The
characteristic set $\Sigma^\partial_{\sigma_0}$ is compact and lies at finite frequencies. $\mathsf H_{\sigma_0}$ is
tangent to it and vanishes exactly on $R_{\sigma_0,\mathrm{in}}\cup R_{\mathrm{out}}$ there. Every maximal integral curve
of $\varepsilon_0\mathsf H_{\sigma_0}$ in
$\Sigma^\partial_{\sigma_0}\setminus(R_{\sigma_0,\mathrm{in}}\cup R_{\mathrm{out}})$ is defined for all times, tends to
$R_{\sigma_0,\mathrm{in}}$ as $t\to-\infty$ and to $R_{\mathrm{out}}$ as $t\to+\infty$, uniformly on compact subsets.
Moreover $\varepsilon_0\rho^{-1}\mathsf H_{\sigma_0}\rho = 2|\sigma_0|$ at $R_{\sigma_0,\mathrm{in}}$ and $-2|\sigma_0|$
at $R_{\mathrm{out}}$.

*Proof.* On $\Sigma^\partial_{\sigma_0}$, $|\eta|^2 = -\xi(\xi + 2\sigma_0)$. So $\xi$ lies between $-2\sigma_0$ and 0,
and $\eta = 0$ exactly at the two endpoints. By (4.5), $\varepsilon_0\mathsf H_{\sigma_0}\xi = 2\varepsilon_0|\eta|^2 =
-2\varepsilon_0\xi(\xi + 2\sigma_0)$, and $\mathsf H_{\sigma_0}$ vanishes at $\eta = 0$. Along the flow, $\xi$ solves
the logistic equation $\dot\xi = -2\varepsilon_0\xi(\xi + 2\sigma_0)$ on the open interval between $-2\sigma_0$ and 0.
Its solutions exist for all time and tend monotonically to 0 as $t\to\infty$ and to $-2\sigma_0$ as $t\to-\infty$. Then
$|\eta|^2 = -\xi(\xi + 2\sigma_0)\to0$, and the convergence is exponential, so $\int|\dot\omega|\,dt\le\int2|\eta|\,dt <
\infty$ and $\omega$ converges as well. The last statement is (4.5) at $\xi = -2\sigma_0$ and at $\xi = 0$. $\square$

### 4.3 At $R_{\mathrm{in}}$ ([Hin26c] Proposition 9.10)

Let $p_{\mathrm{in}} := \sigma(\rho^{-1}\mathrm{Im}_h\hat P(0))|_{\rho = 0,\,\xi = -2,\,\eta = 0}$. By the linearity in
Lemma 4.4 (b), $\sigma(\rho^{-1}\mathrm{Im}_h\hat P(0)) = \sigma_0\,p_{\mathrm{in}}$ at $R_{\sigma_0,\mathrm{in}}$, for
either sign of $\sigma_0$. Let $\vartheta_{\mathrm{in}} := \sup_{\partial X}\lambda_{\max}(p_{\mathrm{in}} - (S +
S^{*h}))$.

**Proposition 4.6 (radial estimate at $R_{\mathrm{in}}$).** Let $I\subset\mathbb R\setminus0$ be compact, $\nu\ge0$, $U$
a neighbourhood of $\bigcup_{\sigma_0\in I}R_{\sigma_0,\mathrm{in}}$, and $s,N\in\mathbb R$. For $\sigma\in I + i[0,\nu]$
the radial set is $R_{\mathrm{Re}\,\sigma,\mathrm{in}}$.

(1) (*Direct.*) Let $\mathsf r > \mathsf r_0 > \frac12(-1 + \vartheta_{\mathrm{in}})$ (constants). There are $B, G\in
\Psi^{0,0}$ microsupported in $U$ and at finite frequencies, with $B$ elliptic at $R_{\mathrm{Re}\,\sigma,\mathrm{in}}$,
such that for $\sigma\in I + i[0,\nu]$, in the strong sense,

$$\|Bu\|_{s,\mathsf r}\le C\big(\|G\hat P(\sigma)u\|_{s-2,\mathsf r+1} + \|Gu\|_{-N,\mathsf r_0} + \|u\|_{-N,-N}\big).
\tag{4.8}$$

(2) (*Adjoint.*) Let $\mathsf r > \frac12(-1 + \vartheta_{\mathrm{in}})$. There are $B,G,E$ as in (1), with
$\mathrm{WF}'(E)\cap R_{\mathrm{Re}\,\sigma,\mathrm{in}} = \emptyset$, such that, in the strong sense,

$$\|Bu\|_{-s+2,-\mathsf r-1}\le C\big(\|G\hat P(\sigma)^{*h}u\|_{-s,-\mathsf r} + \|Eu\|_{-s+2,-\mathsf r-1} +
\|u\|_{-N,-N}\big).\tag{4.9}$$

The regularity orders are immaterial, the operators being microsupported at finite frequencies. As with Proposition 4.2,
the adjoint may be taken in any fibre inner product. $B$, $G$ and $E$ depend on $\sigma_0$, the commutant being centred
at $R_{\sigma_0,\mathrm{in}}$; their bounds in $\Psi^{0,0}$, the ellipticity of $B$ at $R_{\sigma_0,\mathrm{in}}$ and $C$
are uniform in $\sigma\in I + i[0,\nu]$ (D186).

*Proof.* Write $P := \hat P(\sigma)$ and fix $h$, the inner product in which $\vartheta_{\mathrm{in}}$ is computed.
Then

$$P_I = P_I^{(0)} + \sigma_1\mathrm{Re}_hT,\qquad P_I^{(0)} := \mathrm{Im}_h\hat P(0) + \sigma_0\,\mathrm{Im}_hT +
\mathrm{Im}
(\sigma^2)g_{00}\in\Psi^{1,-1},$$

by $\mathrm{Im}_h(\sigma T) = \sigma_0\mathrm{Im}_hT + \sigma_1\mathrm{Re}_hT$ and Lemma 4.4 (b). Its symbol at
$\rho = 0$ is $\rho\,\hat p$ with $\hat p := \sigma(\rho^{-1}\mathrm{Im}_h\hat P(0)) - \sigma_0(S + S^{*h})$, so
$\hat p = \sigma_0(p_{\mathrm{in}} - (S + S^{*h}))$ at $R_{\sigma_0,\mathrm{in}}$. Let
$K := -\varepsilon_0\mathrm{Re}_hT$, $h$-self-adjoint with principal symbol $-2\varepsilon_0\xi\,\mathrm{Id}$, which
equals $4|\sigma_0|$ at $R_{\sigma_0,\mathrm{in}}$.

*Commutant.* For an order $\mathsf r'$ and a regulariser $\varphi_\epsilon(\rho)$ of exponent $\kappa$, let

$$\check a_\epsilon := \rho^{-\mathsf r'-\frac12}\varphi_\epsilon\,\psi_\partial\,\psi_\Sigma\,\psi_R,\qquad
\psi_\partial := \psi(\varsigma_\partial\rho),\quad\psi_\Sigma := \psi(\varsigma_\Sigma g_{\sigma_0}^2),\quad\psi_R :=
\psi(\varsigma_Rq),\quad q := (\xi + 2\sigma_0)^2 + |\eta|^2,$$

with $g_{\sigma_0}$ and $q$ extended independently of $\rho$, and $\check A_\epsilon$ the $h$-symmetrisation of
$\mathrm{Op}(\check a_\epsilon)\mathrm{Id}$. This is (i) of Lemma 3.1 with $\mathbf m = (2,0)$ and decay order
$\mathsf r' + \frac12$; the regularity order is $-\infty$. Using $X\check A^2 + \check A^2X = 2\check AX\check A +
[[X,\check A],\check A]$,

$$C_\epsilon = i[P_R,\check A_\epsilon^2] + 2\check A_\epsilon P_I^{(0)}\check A_\epsilon - 2\varepsilon_0\sigma_1
\check A_\epsilon K\check A_\epsilon + R'_\epsilon,$$

where

$$R'_\epsilon := [[P_I^{(0)},\check A_\epsilon],\check A_\epsilon] + \sigma_1[[\mathrm{Re}_hT,\check A_\epsilon],
\check A_\epsilon]$$

is bounded in $\Psi^{-\infty,2\mathsf r'-1}$. Each commutator with $\check A_\epsilon$, whose principal symbol is scalar,
lowers both orders by one (Lemma 2.1 (c)).

*Symbol.* $P_R$ has face symbol $g_{\sigma_0}\,\mathrm{Id}$. Its lower-order part, which is matrix-valued and depends on
$\sigma_1$, enters $i[P_R,\check A^2]$ one order lower. The decay-$2\mathsf r'$ symbol of $i[P_R,\check A_\epsilon^2] +
2\check A_\epsilon P_I^{(0)}\check A_\epsilon$ is $\rho\,\mathsf H_{\sigma_0}(\check a_\epsilon^2)\mathrm{Id} +
2\rho\check a_\epsilon^2\hat p$ at $\rho = 0$. Terms with an extra factor $\rho$ lie in $\Psi^{-\infty,2\mathsf r'-1}$,
and the derivatives of $\psi_\partial$, supported at $\rho\in[(2\varsigma_\partial)^{-1},\varsigma_\partial^{-1}]$ and
at finite frequencies, are in $\Psi^{-\infty,-\infty}$. By (3.6) and (4.5), $\mathsf H_{\sigma_0}\psi_\Sigma = 0$ and
$\mathsf H_{\sigma_0}q = -2(\sigma_0 + \xi)\cdot2|\eta|^2 + 2|\eta|^2\cdot2(\xi + 2\sigma_0) = 4\sigma_0|\eta|^2$, so at
$\rho = 0$

$$\varepsilon_0\rho^{2\mathsf r'}\big[\rho\mathsf H_{\sigma_0}(\check a_\epsilon^2) + 2\rho\check a_\epsilon^2\hat
p\big] =
-\varphi_\epsilon^2\psi_\Sigma^2\big[\psi_R^2Q_\epsilon - 8|\sigma_0|\varsigma_R|\eta|^2\psi_R\psi_R'\big],$$

$$Q_\epsilon := \varepsilon_0\big[(2\mathsf r'_\epsilon + 1)(\rho^{-1}\mathsf H_{\sigma_0}\rho)\,\mathrm{Id} - 2\hat
p\big],
\qquad\mathsf r'_\epsilon := \mathsf r' - \kappa\theta_\epsilon.$$

At $R_{\sigma_0,\mathrm{in}}$, $\varepsilon_0\rho^{-1}\mathsf H_{\sigma_0}\rho = 2|\sigma_0|$ (Lemma 4.5) and
$\varepsilon_0\hat p = |\sigma_0|(p_{\mathrm{in}} - (S + S^{*h}))$. So

$$Q_\epsilon = 2|\sigma_0|\big[(2\mathsf r'_\epsilon + 1)\mathrm{Id} - (p_{\mathrm{in}} - S - S^{*h})\big]\ge2|\sigma_0|
(2\mathsf r_0 + 1 - \vartheta_{\mathrm{in}})\,\mathrm{Id} > 0\quad\text{at }R_{\sigma_0,\mathrm{in}},$$

for $\mathsf r'_\epsilon\ge\mathsf r_0$. In Lemma 3.2 the orders are $\mathsf r_j\in[\mathsf r_0,\mathsf r]$ and $\mathsf
r'_\epsilon\in(\mathsf r_{j-1},\mathsf r_j]$. Near $R_{\sigma_0,\mathrm{in}}$, where $\varepsilon_0\rho^{-1}\mathsf
H_{\sigma_0}\rho > 0$, $Q_\epsilon\ge Q^{(0)} := \varepsilon_0\big[(2\mathsf r_0 + 1)(\rho^{-1}\mathsf
H_{\sigma_0}\rho)\mathrm{Id} - 2\hat p\big]$, which does not involve $\epsilon$ (D187). By continuity of $Q^{(0)}$,
uniformly in $\sigma_0\in I$ and $\sigma_1\in[0,\nu]$ ($Q^{(0)}$ does not involve $\sigma_1$), there are a neighbourhood
$W\subset U$ and $c_Q > 0$ with $Q_\epsilon\ge c_Q$ and $K$'s symbol $\ge2|\sigma_0|$ on $W$.

*The cut-off term.* On $\mathrm{supp}\,\psi_\Sigma\psi_R'$ at $\rho = 0$, write $\xi = -2\sigma_0 + x$. Then $q = x^2 +
|\eta|^2\in[(2\varsigma_R)^{-1},\varsigma_R^{-1}]$, and $|g_{\sigma_0}|\le\gamma := \varsigma_\Sigma^{-1/2}$ with
$g_{\sigma_0} = x(x - 2\sigma_0) + |\eta|^2$. So $2|\sigma_0||x|\le\gamma + q$. Take $\varsigma_\Sigma$ with $\gamma\le
(2\varsigma_R)^{-1}\le q$. Then $x^2\le q^2/\sigma_0^2\le q/2$ once $\varsigma_R\ge2/\min_I\sigma_0^2$, and $|\eta|^2\ge
q/2$. Hence

$$b_{R,\epsilon} := \rho^{-\mathsf r'}\varphi_\epsilon\psi_\partial\psi_\Sigma\big(8|\sigma_0||\eta|^2/q\big)^{1/2}
\sqrt{-x\psi(x)\psi'(x)}\big|_{x = \varsigma_Rq}$$

is smooth, the factor $(|\eta|^2/q)^{1/2}\ge2^{-1/2}$ being needed only on the support of the last factor. Moreover
$-8|\sigma_0|\varsigma_R|\eta|^2\psi_R\psi_R' = b_{R,\epsilon}^2\rho^{2\mathsf r'}\varphi_\epsilon^{-2}
\psi_\partial^{-2}\psi_\Sigma^{-2}$. Choose $\varsigma_R$ (then $\varsigma_\Sigma$, then $\varsigma_\partial$) so large
that $\mathrm{supp}\,\check a_\epsilon\subset W$.

*Decomposition.* With $\tilde Q_\epsilon$ as in Proposition 4.2, $b_\epsilon := \rho^{-\mathsf r'}\varphi_\epsilon
\psi_\partial\psi_\Sigma\psi_R\tilde Q_\epsilon^{1/2}$ and $B_\epsilon$, $B_{R,\epsilon}$ their quantisations,

$$\varepsilon_0C_\epsilon = -B_\epsilon^{*h}B_\epsilon - B_{R,\epsilon}^{*h}B_{R,\epsilon} - 2\sigma_1\check A_\epsilon K
\check A_\epsilon + R_\epsilon,$$

with $R_\epsilon$ bounded in $\Psi^{-\infty,2\mathsf r'-1}$. By Lemma 2.3, $K = L^{*h}L + K'$ with
$\mathrm{WF}'(K')\cap \bar W = \emptyset$. So

$$2\sigma_1\check A_\epsilon K\check A_\epsilon = 2\sigma_1(L\check A_\epsilon)^{*h}(L\check A_\epsilon) +
2\sigma_1\check A_\epsilon K'\check A_\epsilon$$

, the last term bounded in $\Psi^{-\infty,-\infty}$, and

$$F_\epsilon := B_{R,\epsilon}^{*h}B_{R,\epsilon} + 2\sigma_1\check A_\epsilon K\check A_\epsilon$$

satisfies $\langle F_\epsilon w,w\rangle\ge-C\|w\|^2_{-\mathbf N}$ for Schwartz $w$, as $\sigma_1\ge0$. This is (3.1)
with $\varsigma = \varepsilon_0$. The remaining hypotheses ($Z_\epsilon$, $Y_\epsilon$, convergence) are verified as in
Proposition 4.2, with $z_\epsilon := \rho^{-1/2}\tilde Q_\epsilon^{-1/2}$, bounded in $S^{-\infty,1/2} =
S^{-\frac12(\mathbf m - \mathbf 1)}$, as $\mathbf m - \mathbf 1 = (1,-1)$ (D187). Lemma 3.2 in the decay component gives
(4.8).

(2) For $P^{*h}$ the imaginary part is $-P_I$. With target decay order $\tilde{\mathsf r} := -\mathsf r' - 1$, the same
commutant and computation give, at $R_{\sigma_0,\mathrm{in}}$,

$$\varepsilon_0\rho^{2\tilde{\mathsf r}}\sigma(C^\flat_\epsilon) =
2|\sigma_0|\varphi_\epsilon^2\psi^2\big[-(2\tilde{\mathsf
r}_\epsilon + 1)\mathrm{Id} - (p_{\mathrm{in}} - S - S^{*h})\big] + (\text{cut-off term}).$$

Since $-(2\tilde{\mathsf r}_\epsilon + 1)\ge2\mathsf r' + 1$ and $2\mathsf r' + 1 - \vartheta_{\mathrm{in}} > 0$, the
bracket is positive definite. The cut-off term is $-b_{R,\epsilon}^2$. The $\sigma_1$ term is now $+2\sigma_1\check A
K\check A$, of the sign of the bracket. So $-\varepsilon_0C^\flat_\epsilon = -B_\epsilon^{*h} B_\epsilon -
2\sigma_1\check A_\epsilon K\check A_\epsilon + B_{R,\epsilon}^{*h}B_{R,\epsilon} + R_\epsilon$: (3.1) with $\varsigma =
-\varepsilon_0$ and $E_\epsilon := B_{R,\epsilon}$, microsupported in $\mathrm{supp}\,\psi'(\varsigma_R q)$, which is
disjoint from $R_{\sigma_0,\mathrm{in}}$; $E$ is taken elliptic on the set $K_E^*$ of Lemma 3.2. The regulariser lowers
$\tilde{\mathsf r}_\epsilon$, which keeps the bracket positive, so Lemma 3.2 runs from $-N$. $\square$

### 4.4 Sums of squares, and commutators with b-vector fields ([Hin26c] (9.49), Lemma 9.13)

Near $\partial X$ let $V_1 := \rho\partial_\rho$ and
$V_{jk} := \omega_j\partial_{\omega_k} - \omega_k\partial_{\omega_j}$ ($1\le j < k\le 4$), the rotation fields of
$\mathbb S^3\subset\mathbb R^4$. They span $\mathcal V_b$ near $\partial X$ over $C^\infty$, and
$\sum_{j<k}V_{jk}^\dagger V_{jk} = \Delta_{\mathbb S^3}$: the $V_{jk}$ are Killing, hence anti-adjoint for $d\omega$, and
$-\sum_{j<k}V_{jk}^2$ is the Casimir of $\mathfrak{so}(4)$ acting on functions on $\mathbb S^3$, which is
$\Delta_{\mathbb S^3}$. All act componentwise.

**Lemma 4.7 ([Hin26c] (9.49) on $E$).** Near $\partial X$, $\mathrm{Re}_h\hat P(0) = \sum_jW_j^{*h}W_j + R_1 + R_2$, with
$W_j\in\rho\,\mathrm{Diff}^1_b$ acting componentwise, $R_1\in\rho^2\mathrm{Diff}^1_b$ and
$R_2\in\rho^3\mathrm{Diff}^2_b$, both $h$-self-adjoint. The $\sigma$-independent symbols $r_1 := \sigma(\rho^{-1}R_1)$
and $r_2 := \sigma(\rho^{-1}R_2)$ at $\rho = 0$ are homogeneous of degrees 1 and 2 in $(\xi,\eta)$, and so vanish at
$R_{\mathrm{out}}$.

*Proof.* $\mathrm{Re}_h\hat P(0) = \hat P(0) - i\,\mathrm{Im}_h\hat P(0)$ with
$\mathrm{Im}_h\hat P(0)\in\rho^2\mathrm{Diff}^1_b$. So by (H2),

$$\rho^{-1}\mathrm{Re}_h\hat P(0)\rho^{-1} = P^{(0)} + \rho[P^{(0)},\rho^{-1}] + \rho^{-1}(\rho^2\mathrm{Diff}^1_b)
\rho^{-1}\equiv(\rho D_\rho)^2 + \Delta_{\mathbb S^3}$$

mod $\mathrm{Diff}^1_b + \rho\mathrm{Diff}^2_b$. For the density $\rho^{-5}d\rho\,d\omega$,
$(\rho D_\rho)^\dagger = \rho D_\rho + 4i$, so $(\rho D_\rho)^2 = (\rho D_\rho)^\dagger(\rho D_\rho) - 4i\rho D_\rho$.
Hence $\rho^{-1}\mathrm{Re}_h\hat P(0)\rho^{-1} = \sum_jY_j^\dagger Y_j + D_1 + \rho D_2$, with
$Y_j\in\{ \rho D_\rho, V_{jk}\}$, $D_1\in\mathrm{Diff}^1_b$ and $D_2\in\mathrm{Diff}^2_b$. Multiply by $\rho$ on both
sides. Since $\rho Y^\dagger Y\rho = (Y\rho)^\dagger(Y\rho)$, setting $W_j := Y_j\rho\in\rho\,\mathrm{Diff}^1_b$ gives
$\mathrm{Re}_h\hat P(0) = \sum W_j^\dagger W_j + \rho D_1\rho + \rho^2D_2\rho$. Next,
$W^{*h}W = W^\dagger W + H^{-1} [W^\dagger,H]W$, and $[W^\dagger,H]\in\rho C^\infty$ (a b-vector field times $\rho$,
applied to $H$), so the difference lies in $\rho^2\mathrm{Diff}^1_b$. Thus
$\mathrm{Re}_h\hat P(0) = \sum W_j^{*h}W_j + R_1' + R_2'$ in the stated classes. The left side and $\sum W^{*h}W$ are
$h$-self-adjoint, so $R_1' + R_2' = \mathrm{Re}_hR_1' + \mathrm{Re}_hR_2'$, and the $h$-adjoint preserves both classes.
The degrees follow as in Lemma 4.4 (b). $\square$

**Lemma 4.8 ([Hin26c] Lemma 9.13, corrected).** Let $V = (V_1, V_{12},\dots,V_{34})$, and for a multi-index $\alpha$
let $V^\alpha$ be the ordered product, $\alpha_1$ the number of factors $V_1$, $|\alpha| = k$ and $A_k := \{|\alpha| =
k\}$. If $\hat P(\sigma)u = f$ near $\partial X$, then $u^{(k)} := (V^\alpha u)_{\alpha\in A_k}$ satisfies

$$\hat P(\sigma)V^\alpha u + \sum_{\beta\in A_k}\tilde P_{\alpha\beta}V^\beta u = V^\alpha f - \alpha_1V^{\alpha'}f +
\sum_{|\beta|\le k-1}R_{\alpha\beta}V^\beta u,\tag{4.10}$$

where $\alpha' := \alpha - (1,0,\dots,0)$ (the term is absent if $\alpha_1 = 0$),
$\tilde P_{\alpha\beta}\in\rho^2 \mathrm{Diff}^1_b$ (so $\rho^{-1}\tilde P_{\alpha\beta}\in\mathrm{Diff}^1_{\mathrm{sc}}$
has symbol 0 at $R_{\mathrm{out}}$), and $R_{\alpha\beta}\in\rho\,\mathrm{Diff}^2_{\mathrm{sc}}$, all with
$\mathrm{End}\,\mathbb C^N$-valued coefficients depending polynomially on $\sigma$. The diagonal term is $\hat P(\sigma)$
alone.

*Proof.* $V^\alpha f = \hat P V^\alpha u + [V^\alpha,\hat P]u$. Split $\hat P = 2i\sigma\rho V_1 + \mathcal R$, with
$\mathcal R := -2i\sigma\rho(\frac32 + S) + \hat P(0) - i\sigma Q + \sigma^2g_{00}$. Since $[V_1,\rho] = \rho$,
$[V_{jk},\rho] = 0$ and $[V_1,V_{jk}] = 0$, we get $[V^\alpha,2i\sigma\rho V_1] = 2i\alpha_1\sigma\rho V^\alpha$ mod
$\rho\mathrm{Diff}^{k-1}_b$. Here the source prints 0 unless $\alpha = (k,0,\dots,0)$, which is true only for $\alpha_1 =
0$. Hence

$$V^\alpha f = (\hat P + 2i\alpha_1\sigma\rho)V^\alpha u + [V^\alpha,\mathcal R]u\quad\text{mod
}\rho\mathrm{Diff}^{k-1}_b
u.$$

The diagonal term is $+2i\alpha_1\sigma\rho$; [Hin26c] (9.45) prints $-2ik\sigma\rho$. We do not keep it on the
diagonal. With $V^\alpha = V^{\alpha'}V_1$ (the $V_1$ commute with the $V_{jk}$),

$$2i\alpha_1\sigma\rho V^\alpha u = \alpha_1V^{\alpha'}(2i\sigma\rho V_1u) - \alpha_1[V^{\alpha'},2i\sigma\rho]V_1u =
\alpha_1V^{\alpha'}(f - \mathcal Ru)\quad\text{mod }\rho\mathrm{Diff}^{k-1}_bu.$$

Now $V^{\alpha'}\mathcal Ru = \mathcal RV^{\alpha'}u + [V^{\alpha'},\mathcal R]u$, and both $[V^\alpha,\mathcal R]$ and
$\mathcal RV^{\alpha'}$, $[V^{\alpha'},\mathcal R]$ are sorted by class as follows. Terms from $\rho C^\infty$ parts of
$\mathcal R$ give $\rho\mathrm{Diff}^{k-1}_b$. Terms from $\hat P(0)\in\rho^2\mathrm{Diff}^2_b$ give
$\rho^2\mathrm{Diff}^1_b \circ V^\beta$ with $|\beta|\le k$ (reorder products of $V$'s modulo $\mathrm{Diff}^{k-1}_b$).
Terms from $Q\in\rho^3 \mathrm{Diff}^1_b$ and $g_{00}\in\rho^2C^\infty$ give $\rho^2\mathrm{Diff}^1_b\circ V^{\le k}$.
Terms with $|\beta|\le k-1$ are of the form $R_{\alpha\beta}V^\beta$ with
$R_{\alpha\beta}\in\rho^2\mathrm{Diff}^1_b + \rho\mathrm{Diff}^0_b\subset\rho \mathrm{Diff}^2_{\mathrm{sc}}$; those with
$|\beta| = k$ form $\tilde P_{\alpha\beta}$. Collecting gives (4.10). That
$\rho^{-1}\tilde P_{\alpha\beta}\in\rho\mathrm{Diff}^1_b\subset\mathrm{Diff}^1_{\mathrm{sc}}$ has symbol 0 at the zero
section follows as in Lemma 4.4 (b). $\square$

*Remark (what the correction changes).* With the source's sign, the diagonal $-2ik\sigma\rho$ contributes
$\mathrm{Im}(\sigma^{-1}\cdot(-2ik\sigma\rho)) = -2k\rho$ to the imaginary part, of the good sign at $R_{\mathrm{out}}$.
With the true sign $+2i\alpha_1\sigma\rho$ it would contribute $+2\alpha_1\rho$. That moves the threshold for $u^{(k)}$
to $\mathsf r < -\frac12 + \bar S - \alpha_1$, which would make the source's Step 2 (p. 171) fail for $\mathsf r\in
[-\frac32 + \bar S, -\frac12 + \bar S)$. Rewriting the term through the equation removes it, so the statement (9.44)
stands with its threshold unchanged.

### 4.5 At $R_{\mathrm{out}}$ ([Hin26c] Proposition 9.11)

For $\sigma\ne0$ let $\tilde P(\sigma) := \sigma^{-1}\hat P(\sigma)$, and write
$\kappa_\sigma := \mathrm{Re}(\sigma^{-1}) = \sigma_0/|\sigma|^2$ and
$\iota_\sigma := -\mathrm{Im}(\sigma^{-1}) = \sigma_1/|\sigma|^2\ge0$. By Lemma 4.4, $\mathrm{Re}_h\tilde P$ has face
symbol $\tilde g := 2\xi + \kappa_\sigma(\xi^2 + |\eta|^2)$, and with $\tilde{\mathsf H} := \mathsf V_{\tilde g}$, (4.4)
gives

$$\tilde{\mathsf H} = -2(1 + \kappa_\sigma\xi)(\rho\partial_\rho + \eta\cdot\partial_\eta) + 2\kappa_\sigma|\eta|^2
\partial_\xi + \kappa_\sigma H_{|\eta|^2},\quad\rho^{-1}\tilde{\mathsf H}\rho = -2(1 +
\kappa_\sigma\xi),\quad\tilde{\mathsf
H}(\xi^2 + |\eta|^2) = -4|\eta|^2,\tag{4.11}$$

and $\tilde{\mathsf H}\tilde g = 0$. By
$\mathrm{Im}_h(cA) = (\mathrm{Re}\,c)\mathrm{Im}_hA + (\mathrm{Im}\,c)\mathrm{Re}_hA$, Lemma 4.4 (b) and Lemma 4.7,

$$\mathrm{Im}_h\tilde P = \tilde P_I^{(0)} - \iota_\sigma\sum_jW_j^{*h}W_j,\qquad\tilde P_I^{(0)} := \mathrm{Im}_hT +
\kappa_\sigma\mathrm{Im}_h\hat P(0) - \iota_\sigma(R_1 + R_2) + \sigma_1g_{00}\in\Psi^{2,-1}.\tag{4.12}$$

(Here $\mathrm{Im}_h(\sigma^{-1}\sigma^2g_{00}) = \sigma_1g_{00}$.) $\tilde P_I^{(0)}$ has symbol $\rho\tilde p$ at
$\rho = 0$, with $\tilde p := -(S + S^{*h}) + \kappa_\sigma r_3 - \iota_\sigma(r_1 + r_2)$ and $r_3 := \sigma(\rho^{-1}
\mathrm{Im}_h\hat P(0))$. The last three terms vanish at $R_{\mathrm{out}}$, so $\tilde p = -(S + S^{*h})$ there.

**Proposition 4.9 (radial estimate at $R_{\mathrm{out}}$).** Let $\mathcal D$ be a compact subset of $\{\sigma\ne0,
\mathrm{Im}\,\sigma\ge0\}$, $U$ a neighbourhood of $R_{\mathrm{out}}$, $s,N\in\mathbb R$, and $h$ a fibre inner product.

(1) (*Direct.*) Let $\mathsf r < -\frac12 + \frac12\inf_{\partial X}\lambda_{\min}(S + S^{*h})$. There are $B,E,G\in
\Psi^{0,0}$ microsupported in $U$ at finite frequencies, $B$ elliptic at $R_{\mathrm{out}}$ and $\mathrm{WF}'(E)\cap
R_{\mathrm{out}} = \emptyset$, such that for $\sigma\in\mathcal D$, in the strong sense,

$$\|Bu\|_{s,\mathsf r}\le C\big(\|G\hat P(\sigma)u\|_{s-2,\mathsf r+1} + \|Eu\|_{s,\mathsf r} + \|u\|_{-N,-N}\big).
\tag{4.13}$$

(2) (*Adjoint.*) Let $\mathsf r < \mathsf r_0 < -\frac12 + \frac12\inf_{\partial X}\lambda_{\min}(S + S^{*h})$. There are
$B,G$ as in (1) such that, in the strong sense,

$$\|Bu\|_{-s+2,-\mathsf r-1}\le C\big(\|G\hat P(\sigma)^{*h}u\|_{-s,-\mathsf r} + \|Gu\|_{-N,-\mathsf r_0-1} + \|u\|_{-N,
-N}\big).\tag{4.14}$$

(3) (*b-regularity*, [Hin26c] (9.44).) In the setting of (1), for every $k\in\mathbb N_0$, with the norms of section
4.6,

$$\|Bu\|_{(s;k),\mathsf r}\le C\big(\|G\hat P(\sigma)u\|_{(s-2;k),\mathsf r+1} + \|Eu\|_{(s;k),\mathsf r} + \|u\|_{-N,-N}
\big).\tag{4.15}$$

With Lemma 2.4, $\frac12\inf\lambda_{\min}(S + S^{*h})$ can be taken within any $\epsilon > 0$ of $\bar S$. So every
$\mathsf r < -\frac12 + \bar S$ is admissible in (1) and (3), and every $\mathsf r_0 < -\frac12 + \bar S$ in (2), for a
suitable $h$, which is [Hin26c]'s threshold (9.16c). As in Proposition 4.6, $B$, $E$ and $G$ depend on $\sigma$, through
$\kappa_\sigma$ in $\psi_\Sigma$, with bounds and constants uniform on $\mathcal D$ (D186).

*Proof.* (1) $\hat P(\sigma)u = f$ is equivalent to $\tilde Pu = \sigma^{-1}f$, and $|\sigma|^{-1}$ is bounded on
$\mathcal D$. Commutant: $\check a_\epsilon := \rho^{-\mathsf r'-\frac12}\varphi_\epsilon\psi_\partial\psi_\Sigma\psi_R$
with $\psi_\Sigma := \psi(\varsigma_\Sigma\tilde g^2)$, $\psi_R := \psi(\varsigma_Rq)$ and $q := \xi^2 + |\eta|^2$.
Using (4.12), and with $R'_\epsilon$ (double commutators) bounded in $\Psi^{-\infty,2\mathsf r'-1}$,

$$C_\epsilon = i[\tilde P_R,\check A_\epsilon^2] + 2\check A_\epsilon\tilde P_I^{(0)}\check A_\epsilon - 2\iota_\sigma
\sum_j(W_j\check A_\epsilon)^{*h}(W_j\check A_\epsilon) + R'_\epsilon.$$

The third term is $\le0$ exactly. At $\rho = 0$, by (3.6), (4.11), $\tilde{\mathsf H}\psi_\Sigma = 0$ and $\tilde{\mathsf
H}q = -4|\eta|^2$,

$$\rho^{2\mathsf r'}\big[\rho\tilde{\mathsf H}(\check a_\epsilon^2) + 2\rho\check a_\epsilon^2\tilde p\big] =
-\varphi_\epsilon^2\psi_\Sigma^2\big[\psi_R^2Q_\epsilon - 8\varsigma_R|\eta|^2(-\psi_R\psi_R')\big],\qquad
Q_\epsilon := (2\mathsf r'_\epsilon + 1)(\rho^{-1}\tilde{\mathsf H}\rho)\mathrm{Id} - 2\tilde p.$$

At $R_{\mathrm{out}}$, $Q_\epsilon = -2(2\mathsf r'_\epsilon + 1)\mathrm{Id} + 2(S + S^{*h})\ge2(\lambda_{\min}(S +
S^{*h}) - 2\mathsf r' - 1) > 0$, since $\mathsf r'_\epsilon\le\mathsf r'\le\mathsf r$. Near $R_{\mathrm{out}}$,
$\rho^{-1}\tilde{\mathsf H}\rho = -2(1 + \kappa_\sigma\xi) < 0$, so $Q_\epsilon\ge(2\mathsf r' +
1)(\rho^{-1}\tilde{\mathsf H}\rho)\mathrm{Id} - 2\tilde p$, which does not involve $\epsilon$ and whose remaining terms
vanish at $R_{\mathrm{out}}$ and are bounded uniformly in $\sigma\in\mathcal D$ (D187). So $Q_\epsilon\ge c_Q$ on a
neighbourhood $W$ of $R_{\mathrm{out}}$, uniformly. The cut-off term is now $+8\varsigma_R|\eta|^2(-\psi_R\psi_R')\ge0$.
On $\mathrm{supp}\,\psi_\Sigma\psi_R'$ we have $2\xi = \tilde g - \kappa_\sigma q$, so $|\xi|\le\frac12(\gamma +
|\kappa_\sigma|q)\le\frac12(1 + |\kappa_\sigma|)q$ when $\gamma\le q$. Then $\xi^2\le q/2$ for $\varsigma_R\ge (1 +
\sup_{\mathcal D}|\kappa_\sigma|)^2$, hence $|\eta|^2\ge q/2$, and

$$e_{R,\epsilon} := \rho^{-\mathsf r'}\varphi_\epsilon\psi_\partial\psi_\Sigma\big(8|\eta|^2/q\big)^{1/2}\sqrt{-x\psi(x)
\psi'(x)}\big|_{x = \varsigma_Rq}$$

is smooth. So $C_\epsilon = -B_\epsilon^{*h}B_\epsilon + E_\epsilon^{*h}E_\epsilon - F_\epsilon + R_\epsilon$, with
$b_\epsilon := \rho^{-\mathsf r'}\varphi_\epsilon\psi_\partial\psi_\Sigma\psi_R\tilde Q_\epsilon^{1/2}$, $E_\epsilon :=
\mathrm{Op} (e_{R,\epsilon})\mathrm{Id}$, $F_\epsilon := 2\iota_\sigma\sum_j(W_j\check A_\epsilon)^{*h}(W_j\check
A_\epsilon)\ge0$, and $R_\epsilon$ bounded in $\Psi^{-\infty,2\mathsf r'-1}$. $E_\epsilon$ is microsupported in
$\mathrm{supp}\,\psi'( \varsigma_Rq)$, a closed set disjoint from $R_{\mathrm{out}}$; let $E$ be elliptic on the union
$K_E^*$ of these sets over the steps of Lemma 3.2, closed and disjoint from $R_{\mathrm{out}}$. This is (3.1) with
$\varsigma = 1$. Regularising lowers $\mathsf r'_\epsilon$ and keeps $Q_\epsilon > 0$, so Lemma 3.2 runs from $-N$.

(2) For $\tilde P^{*h}$ the imaginary part is $-\mathrm{Im}_h\tilde P$. With target
$\tilde{\mathsf r} := -\mathsf r' - 1$ and a priori order $-\mathsf r_0 - 1$, the bracket at $R_{\mathrm{out}}$ is
$2(2\tilde{\mathsf r}_\epsilon + 1) \mathrm{Id} + 2(S + S^{*h})$. This is positive definite when
$\tilde{\mathsf r}_\epsilon > -\frac12 - \frac12\lambda_{\min} (S + S^{*h})$, which holds for
$\tilde{\mathsf r}_\epsilon\ge-\mathsf r_0 - 1$, that is, in Lemma 3.2's range of effective orders from the a priori
order up. The cut-off term $-e_{R,\epsilon}^2$ and the term $+2\iota_\sigma\sum(W_j \check A)^{*h}(W_j\check A)$ both now
carry the sign of $-b_\epsilon^2$ in $-C^\flat_\epsilon$. So
$-C^\flat_\epsilon = -B_\epsilon^{*h}B_\epsilon - F_\epsilon + R_\epsilon$, with no $E$ term. Lemma 3.2 from
$\mathbf s_0 = (-N,-\mathsf r_0 - 1)$ gives (4.14); this is an above-threshold estimate.

(3) By induction on $k$, the case $k = 0$ being (1). Apply (1) to the system (4.10) for $u^{(k)}$, with the inner product
$h^{\oplus A_k}$. Its principal part at the face is $\tilde g\,\mathrm{Id}$, and its decay-0 imaginary part is
$-\iota_\sigma\sum W_j^{*h}W_j\otimes\mathrm{Id}$, the same as before. Its decay-$(-1)$ imaginary part has symbol
$\tilde p \otimes\mathrm{Id}$ plus the symbols of $\sigma^{-1}\tilde P_{\alpha\beta}$ divided by $\rho$, which vanish at
$R_{\mathrm{out}}$ by Lemma 4.8. So the proof of (1) applies verbatim, with the same threshold. The right side of (4.10),
divided by $\sigma$, contains $V^\alpha f - \alpha_1V^{\alpha'}f$, bounded in $H^{s-2,\mathsf r+1}$ by
$\|Gf\|_{(s-2;k),\mathsf r+1}$, and $R_{\alpha\beta}V^\beta u$ with
$R_{\alpha\beta}\in\rho\mathrm{Diff}^2_{\mathrm{sc}} \subset\Psi^{2,-1}$ and $|\beta|\le k-1$. The latter is bounded in
$H^{s-2,\mathsf r+1}$ by $C\|\tilde Gu\|_{(s;k-1), \mathsf r}$, plus $C\|u\|_{-N,-N}$ for a microlocaliser $\tilde G$
elliptic on $\mathrm{WF}'(G)$. This uses that a b-vector field lies in $\Psi^{1,1}$ (it is $\rho^{-1}$ times a scattering
vector field), so its commutator with any $A\in\Psi^{m,l}$ lies in $\Psi^{m,l}$ by Lemma 2.1 (c). The induction
hypothesis bounds $\|\tilde Gu\|_{(s;k-1),\mathsf r}$. The term $\|Eu^{(k)}\|_{s,\mathsf r}$ is bounded by
$\|E'u\|_{(s;k),\mathsf r}$ for $E'$ elliptic on $\mathrm{WF}'(E)$. Finally $\|Bu^{(k)}\|_{s,\mathsf r}$ controls
$\|B'u\|_{(s;k),\mathsf r}$ for $B'$ microsupported in $\mathrm{Ell}(B)$, since $[V^\alpha,B]$ lowers the module order.
$\square$

### 4.6 b-regularity spaces

For $k\in\mathbb N_0$ let
$H^{(s;k),\mathsf r} := \{u\in H^{s,\mathsf r} : (\langle x\rangle D_x)^\alpha u\in H^{s,\mathsf r}, |\alpha|\le k\}$,
normed by the sum, and $\bar H^{(s;k),\mathsf r}$ the extendible version (section 6.1). The fields
$\langle x\rangle\partial_{x_j}$ span $\mathcal V_b(\overline{\mathbb R^4})$ over $C^\infty(\overline{\mathbb R^4})$, so
near $\partial X$ the norm is equivalent to the one defined with the $V^\alpha$ of section 4.4. This is [Hin26c]'s space
(3.42), which Hintz uses with the fields $(r\partial_x)^\alpha$ (p. 106).

**Lemma 4.10 ([Hin26c] Remark 9.14, (9.53)).** Let $o_{\partial X} = R_{\mathrm{out}}$ be the zero section over
$\partial X$. If $B\in\Psi^{0,0}$ is microsupported away from $o_{\partial X}$, then for every $k$,
$\|Bu\|_{(s;k),\mathsf r}\le C(\|Bu\|_{s+k,\mathsf r+k} + \|u\|_{-N,-N})$, and conversely.

*Proof.* $\langle x\rangle D_{x_j}\in\Psi^{1,1}$, and $\sum_j(\langle x\rangle D_{x_j})^*(\langle x\rangle D_{x_j})$ has
principal symbol $\langle x\rangle^2|\zeta|^2$ in terms of the Euclidean frequency $\zeta$. This is elliptic in
$\Psi^{2,2}$ off the zero section of the boundary face, including at fibre infinity. Ellipticity (C5) gives both
inequalities, inductively in $k$. $\square$

## 5. Elliptic and propagation estimates

**Proposition 5.1 (elliptic estimate).** Let $\mathcal D\subset\mathbb C$ be compact and $B\in\Psi^{0,0}$ microsupported
in a closed set $K$ of the boundary of phase space on which $\hat P(\sigma)$ is elliptic in $\Psi^{2,0}$ for every
$\sigma\in\mathcal D$, with a uniform lower bound on its principal symbol. Then for $G$ elliptic on $K$, all orders
$\mathbf s$ and all $N$, uniformly in $\sigma\in\mathcal D$, in the strong sense,

$$\|Bu\|_{\mathbf s}\le C\big(\|G\hat P(\sigma)u\|_{\mathbf s - (2,0)} + \|u\|_{-\mathbf N}\big).$$

*Proof.* By Lemma 2.1 (d) and (C5) there is a microlocal parametrix $Q_\sigma\in\Psi^{-2,0}$ with
$Q_\sigma\hat P(\sigma) = \mathrm{Id} + R_\sigma$, where $\mathrm{WF}'(R_\sigma)\cap K = \emptyset$. Then
$Bu = BQ_\sigma\Phi\hat P(\sigma)u - BR_\sigma u + BQ_\sigma(\mathrm{Id} - \Phi)\hat P(\sigma)u$, with $\Phi$
microlocally the identity near $K$ and microsupported in $\mathrm{Ell}(G)$. The construction is continuous in the symbol,
so its seminorms are uniform on $\mathcal D$; the last two terms are residual. $\square$

**Proposition 5.2 (propagation).** Let $P\in\Psi^{\mathbf m}$ and let $h$ be a fibre inner product. Let $F$ be one of
the two boundary faces of phase space, with defining function $\varrho$ ($\rho_\infty$ at fibre infinity, $\rho$ at the
boundary face over $\partial X$). Suppose the following.

(a) Near a compact set $\Lambda\subset F$, $P_R = \mathrm{Re}_hP$ has principal symbol $p\,\mathrm{Id}$ with $p$ real.
Then $H_p = \mu\,\mathsf V$ near $\Lambda$, where $\mu > 0$ is a weight of order $\mathbf m - \mathbf 1$ and $\mathsf V$
is a smooth vector field tangent to $F$ ([HJS] (7.34); at fibre infinity $\mathsf V = \rho_\infty H_p$ for $\mathbf m =
2$, and over $\partial X$ it is (4.4)). Fix a sign $\varepsilon$ and set $\mathsf H_f := \varepsilon\mathsf V$, the
*forward* field.

(b) $P_I = P_I^{\mathrm{sub}} + P_I^{\mathrm{abs}}$, where $P_I^{\mathrm{sub}}\in\Psi^{\mathbf m - \mathbf 1}$ is
$h$-self-adjoint and $\varepsilon P_I^{\mathrm{abs}} = -c\,L^{*h}L + K'$ with $c\ge0$ a constant, $L$ of order
$\frac12\mathbf m$ and $\mathrm{WF}'(K')\cap\bar W = \emptyset$ for a neighbourhood $W$ of $\Lambda$.

(c) $\gamma : [0,T]\to F\cap\{p = 0\}$ is an integral curve of $\mathsf H_f$, injective, with $\mathsf H_f\ne0$ on it,
and $\gamma([0,T])\subset\Lambda$.

(d) $\mathbf s$ is an order whose component $\mathsf k_F$ on $F$ satisfies $\mathsf H_f\mathsf k_F\le0$ near $\gamma$.

Let $E\in\Psi^{0,0}$ be elliptic at $\gamma(0)$. Then there are $B$, elliptic on $\gamma([0,T])$, and $G$, both
microsupported in any given neighbourhood of $\gamma([0,T])$, such that in the strong sense

$$\|Bu\|_{\mathbf s}\le C\big(\|GPu\|_{\mathbf s - \mathbf m + \mathbf 1} + \|Eu\|_{\mathbf s} + \|u\|_{-\mathbf N}\big).
\tag{5.1}$$

*Proof.* *Coordinates.* Since $\gamma$ is injective and $\mathsf H_f\ne0$ on it, there are coordinates
$(z,y)\in(-2\delta, T + 2\delta)\times\{|y| < 2\delta_1\}$ on a neighbourhood $O$ of $\gamma([0,T])$ in $F$, in which
$\mathsf H_f = \partial_z$ and $\gamma(t) = (t,0)$ (flow out a small transversal disc through $\gamma(-\delta)$). Extend
$z,y$ off $F$ independently of $\varrho$. Choose $\delta,\delta_1$ so small that $O\subset W$ and
$\{z\in[-\delta,0], |y|\le\delta_1\}\subset \mathrm{Ell}(E)$.

*Cut-offs.* Let $\chi_s(z) := \psi(-z/\delta)$ for $z\le0$ and $\chi_s(z) := 1$ for $z\ge0$, smooth as $\psi = 1$ on
$[-\frac12,\frac12]$. So $\chi_s = 1$ for $z\ge0$ and $\chi_s = 0$ for $z\le-\delta$, and $\partial_z(\chi_s^2) =
\frac2\delta(-\psi\psi')(-z/\delta)\ge0$, supported in $[-\delta,-\frac\delta2]$. Let $\chi_e(z) := \psi((z - T)/\delta)$
for $z\ge T$ and $\chi_e(z) := 1$ for $z\le T$. So $\chi_e = 1$ for $z\le T$, and $-\partial_z(\chi_e^2) =
\frac2\delta(-\psi\psi')((z - T)/\delta)\ge0$, supported in $[T+\frac\delta2,T+\delta]$. ($\psi$ is even, so
$\psi(-z/\delta)$ alone would vanish for $z\ge\delta$, and $\partial_z(\chi_s^2)$ would be negative on
$[\frac\delta2,\delta]$; D195.) Since $-\psi\psi' = (\nu\psi)^2$ on $[0,\infty)$ (section 3), both derivatives are
squares of smooth functions. Let $\psi_y := \psi(|y|^2/\delta_1^2)$.

*Commutant.* With $\mathbf k = \mathbf s - \frac12(\mathbf m - \mathbf 1)$, its component $\mathsf k := \mathsf k_F$, a
regulariser $\varphi_\epsilon(\varrho)$ of exponent $\kappa$ and a large constant $M$, let

$$\check a_\epsilon := \varrho^{-\mathsf k}\varphi_\epsilon\,e^{-Mz}\chi_s(z)\chi_e(z)\psi_y,$$

multiplied by a cut-off to a neighbourhood of $F$ whose derivatives are residual. As in section 4, the operator is
$\check A_\epsilon := \frac12(\mathrm{Op}(\check a_\epsilon)\mathrm{Id}+(\mathrm{Op}(\check
a_\epsilon)\mathrm{Id})^{*h})$, $h$-self-adjoint as Lemma 3.1 (i) requires, so that the identity (3.4) holds (D195). At
$F$, by (3.6) and since $\mathsf H_f\psi_y = 0$ there,

$$\mathsf H_f(\check a_\epsilon^2) = \varrho^{-2\mathsf
k}\varphi_\epsilon^2\psi_y^2e^{-2Mz}\Big[\chi_s^2\chi_e^2\big(-2M -
2\mathsf k_\epsilon(\varrho^{-1}\mathsf H_f\varrho) - 2(\mathsf H_f\mathsf k)\log\varrho\big) +
\chi_e^2\partial_z(\chi_s^2) +
\chi_s^2\partial_z(\chi_e^2)\Big],$$

with $\mathsf k_\epsilon := \mathsf k - \kappa\theta_\epsilon$. Here $\mathsf H_f(\varrho^{-2\mathsf k}) = \varrho^{-2
\mathsf k}(-2\mathsf k\,\varrho^{-1}\mathsf H_f\varrho - 2(\mathsf H_f\mathsf k)\log\varrho)$; the log term is
$-2(\mathsf H_f\mathsf k)\log\varrho\le0$, since $\mathsf H_f\mathsf k\le0$ and $\log\varrho < 0$ near $F$. Let $p' :=
\mu^{-1}\varepsilon\,\sigma(P_I^{\mathrm{sub}})$, an $h$-self-adjoint symbol bounded on $O$ (it has order 0 relative to
$\mu$), and

$$Q_\epsilon := \big(2M + 2\mathsf k_\epsilon(\varrho^{-1}\mathsf H_f\varrho)\big)\mathrm{Id} - 2p' + 2(\mathsf
H_f\mathsf k)
\log\varrho\,\mathrm{Id}.$$

Choose $M\ge1 + \sup_O(2|\mathsf k_\epsilon\varrho^{-1}\mathsf H_f\varrho| + 2\|p'\|)$, uniformly in $\epsilon$ since
$\mathsf k_\epsilon\in(\mathsf k - \kappa,\mathsf k]$. Then $Q_\epsilon\ge M\,\mathrm{Id}$. It is a symbol of the
logarithmic class of (C6). So is $Q_\epsilon^{1/2}$: write $Q_\epsilon = Q_0 + \lambda\,\mathrm{Id}$ with $Q_0 := (2M +
2\mathsf k_\epsilon\varrho^{-1}\mathsf H_f\varrho)\mathrm{Id} - 2p'\ge M\,\mathrm{Id}$, bounded, and $\lambda :=
2(\mathsf H_f\mathsf k)\log\varrho\ge0$, scalar. By Cauchy's formula as in Lemma 2.2, $\partial_\lambda^j(Q_0 +
\lambda)^{1/2} = O((M + \lambda)^{\frac12 - j})$, and the derivatives of $Q_0$ and of $\lambda$ along the vector fields
$\langle x\rangle^{-\delta}\mathcal V_b$ of (C6) are bounded; by the chain rule $Q_\epsilon^{1/2}$ lies in the class for
every $\delta > 0$. (Lemma 2.2 does not apply to $Q_\epsilon/(1 + |\log\varrho|)$, which is not bounded below where
$\mathsf H_f\mathsf k = 0$; [HJS] p. 81 notes the point; D186.)

*Decomposition.* As in section 4, $\sigma(\varepsilon C_\epsilon) = \mu[\mathsf H_f(\check a_\epsilon^2)\mathrm{Id} +
2\check a_\epsilon^2p'] + \varepsilon\sigma(\check A^2P_I^{\mathrm{abs}} + P_I^{\mathrm{abs}}\check A^2)$, and

$$\mu\big[\mathsf H_f(\check a^2_\epsilon) + 2\check a_\epsilon^2p'\big] = -b_\epsilon^2 - b_{e,\epsilon}^2 +
e_\epsilon^2,$$

with

$$b_\epsilon := \mu^{\frac12}\varrho^{-\mathsf k}\varphi_\epsilon\psi_ye^{-Mz}\chi_s\chi_e\tilde Q_\epsilon^{1/2},\qquad
b_{e,\epsilon} := \mu^{\frac12}\varrho^{-\mathsf
k}\varphi_\epsilon\psi_ye^{-Mz}\chi_s\big(-\partial_z(\chi_e^2)\big)^{1/2},$$

$$e_\epsilon := \mu^{\frac12}\varrho^{-\mathsf
k}\varphi_\epsilon\psi_ye^{-Mz}\chi_e\big(\partial_z(\chi_s^2)\big)^{1/2}.$$

$\tilde Q_\epsilon$ is $Q_\epsilon$ cut off as in Proposition 4.2. $e_\epsilon$ is supported in $\{z\in[-\delta,0]\}$,
inside $\mathrm{Ell}(E)$. As $U$ shrinks in Lemma 3.2, $\delta$ and $\delta_1$ shrink with it, and every step's $E$-set
lies in $\{z\in[-\delta,-\delta/2], |y|\le\delta_1\}\subset\mathrm{Ell}(E)$, which misses $\gamma([0,T])$; so the given
$E$ is elliptic on $K_E^*$ (D187). By (b) and Lemma 2.3, $\varepsilon(\check A^2P_I^{\mathrm{abs}} +
P_I^{\mathrm{abs}}\check A^2) = -2c(L\check A)^{*h}(L\check A)$ plus a double commutator in $\Psi^{2\mathbf s - \mathbf
1}$ plus a residual term. So $\varepsilon C_\epsilon = -B_\epsilon^{*h}B_\epsilon - F_\epsilon +
E_\epsilon^{*h}E_\epsilon + R_\epsilon$, with $F_\epsilon := B_{e,\epsilon}^{*h}B_{e,\epsilon} + 2c(L\check
A_\epsilon)^{*h}(L\check A_\epsilon)$ and $R_\epsilon$ bounded in $\Psi^{2\mathbf s - \mathbf 1}$. The orders are right:
$\mu\varrho^{-2\mathsf k}$ is the weight of order $2\mathbf s$ on $F$. $\check a_\epsilon = z_\epsilon b_\epsilon$ with
$z_\epsilon := \mu^{-1/2}\tilde Q_\epsilon^{-1/2}$, of order $-\frac12(\mathbf m - \mathbf 1)$. $B_0$ is elliptic on
$\gamma([0,T])$, where $\chi_s = \chi_e = \psi_y = 1$. The factor $(\mathsf H_f\mathsf k)\log\varrho$ makes $b_\epsilon$
bounded only in $\Psi^{\mathbf s + \delta\mathbf 1}$ for every $\delta > 0$, while $z_\epsilon$ stays bounded since
$Q_\epsilon\ge M$; this is Remark 3.3's case. There is no threshold, so Lemma 3.2 runs from $\mathbf s_0 = \mathbf s -
\tau\mathbf 1$ with $\tau$ large, giving (5.1) with $\|Gu\|_{\mathbf s_0}\le\|u\|_{-\mathbf N}$. $\square$

*The two uses.* (i) At fibre infinity over $\tilde X^\circ$: $P = \hat P(\sigma)$, $p = G_0$,
$\mathsf V = \rho_\infty H_{G_0}$, $\varepsilon = \pm$ on $\partial\Sigma_0^\pm$, $P_I = P_I^{\mathrm{sub}}\in\Psi^1$,
and $c = 0$; the order is $s_c$, constant (O1). (ii) At the boundary face, for $\sigma = \sigma_0 + i\sigma_1$ with
$\sigma_1\ge0$: $p = g_{\sigma_0}$, $\mathsf V = \mathsf H_{\sigma_0}$, $\varepsilon = \varepsilon_0$,
$P_I^{\mathrm{sub}} = P_I^{(0)}\in \Psi^{1,-1}$ and $P_I^{\mathrm{abs}} = \sigma_1\mathrm{Re}_hT$. Then
$\varepsilon_0P_I^{\mathrm{abs}} = -\sigma_1K$ with $K := -\varepsilon_0\mathrm{Re}_hT$, whose principal symbol
$-2\varepsilon_0\xi$ is positive on $\Sigma^\partial_{\sigma_0} \setminus R_{\mathrm{out}}$ (there $\varepsilon_0\xi < 0$
by Lemma 4.5). So (b) holds on any neighbourhood $W$ of a compact subset of
$\Sigma^\partial_{\sigma_0}\setminus R_{\mathrm{out}}$ on which $-2\varepsilon_0\xi > 0$, by Lemma 2.3. For the adjoint
$\hat P(\sigma)^{*h}$, use the backward field $-\mathsf H_f$: then $P_I^{\mathrm{abs}}$ becomes
$-\sigma_1\mathrm{Re}_hT$, and $(-\varepsilon_0)(-\sigma_1\mathrm{Re}_hT) = -\sigma_1K$ again. (d) for the adjoint asks
for monotonicity along $-\mathsf H_f$ of the dual order, which is minus the order: the same condition.

## 6. The artificial boundary

### 6.1 Extendible and supported spaces

Let $\Omega := \{|x| > r_0\}$. For an order pair whose regularity component is constant near $\partial_\sharp X$ (true
by (O1)) define

$$\bar H^{s,\mathsf r} := \{u|_\Omega : u\in H^{s,\mathsf r}(\mathbb R^4;\mathbb C^N)\}\ \text{(quotient norm)},\qquad
\dot H^{s,\mathsf r} := \{u\in H^{s,\mathsf r} : \mathrm{supp}\,u\subset\bar\Omega\}.$$

On a slab $\Omega_{a,b} := \{a < r < b\}$, with $r_0 - 2\delta_0 < a < b < r_2$, let $H^s(\Omega_{a,b})^{\bullet,-}$ be
the space of restrictions to $\{r > a\}$ of elements of $H^s(\mathbb R^4)$ supported in $\{r\le b\}$: supported at $b$,
extendible at $a$. $H^s(\Omega_{a,b})^{-,\bullet}$ is the space with the roles of $a$ and $b$ exchanged. On compact sets
the decay order is immaterial.

**Lemma 6.1.** (a) $\dot H^{s,\mathsf r}$ is the closure of $C_c^\infty(\Omega)$. (b) The $L^2$ pairing identifies
$(\bar H^{s,\mathsf r})^*$ with $\dot H^{-s,-\mathsf r}$. (c) The same holds on slabs:
$(H^s(\Omega_{a,b})^{\bullet,-})^* = H^{-s}(\Omega_{a,b})^{-,\bullet}$, and $C_c^\infty(\Omega_{a,b})$ is dense in
$H^s(\Omega_{a,b})^{\bullet,\bullet}$. (d) A differential operator maps each of these spaces to the corresponding space
of order $s - m$. For $u\in\bar H^{s,\mathsf r}$ and $v\in\dot H^{-s+m,-\mathsf r+\ell}$, the pairing
$\langle Lu, v\rangle$ is well defined, and it equals $\langle u, L^*v\rangle$ for
$u\in C_c^\infty(\mathbb R^4)|_\Omega$.

*Proof.* (a) Let $u\in\dot H^{s,\mathsf r}$, and write $u = \chi u + (1 - \chi)u$, with $\chi\in C_c^\infty(\{|x| <
2r_0\})$ equal to 1 on $\{|x|\le\frac32r_0\}$. Then $(1 - \chi)u$ is supported in $\{|x|\ge\frac32r_0\}$. Let
$\tilde\chi\in C_c^\infty(\{|x| < \frac54r_0\})$ equal 1 on $\{|x|\le\frac98r_0\}$. Then $(1 - \tilde\chi)(1 - \chi) =
1 - \chi$, multiplication by $1 - \tilde\chi$ is bounded on $H^{s,\mathsf r}$, and $T_t\to\mathrm{Id}$ strongly (C8).
So the Schwartz functions $(1 - \tilde\chi)T_t(1 - \chi)u$, which are supported in $\Omega$, tend to $(1 - \chi)u$. A
Schwartz function supported in $\Omega$ is approximated by its products with $\chi_0(t|x|)$, $\chi_0\in C_c^\infty$
equal to 1 near 0, as $t\to0$. The function $\chi u$ has compact support, so only the constant regularity order $s$
matters. For $\lambda > 1$ let $(D_\lambda w)(x) := w(x/\lambda)$. Then $\mathrm{supp}\,D_\lambda(\chi
u)\subset\{|x|\ge\lambda r_0\} \subset\Omega$. $D_\lambda$ is bounded on $H^s$ uniformly for $\lambda\in[1,2]$:
$\|D_\lambda w\|_{L^2} = \lambda^2\|w\|_{L^2}$, and $D_\lambda f(D)D_\lambda^{-1} = f(\lambda D)$, so $\langle
D\rangle^sD_\lambda\langle D\rangle^{-s}D_\lambda^{-1}$ is the Fourier multiplier
$\langle\zeta\rangle^s\langle\lambda\zeta\rangle^{-s}$, bounded uniformly. Also $D_\lambda\to\mathrm{Id}$ strongly as
$\lambda\to1$: this holds on $C_c^\infty$, which is dense, and $D_\lambda$ is uniformly bounded. Finally mollify with a
mollifier of radius $< (\lambda - 1)r_0$. (b) $\bar H^{s,\mathsf r} = H^{s, \mathsf r}/Z$ with $Z := \{u :
\mathrm{supp}\,u\subset\mathbb R^4\setminus\Omega\}$, so $(\bar H^{s,\mathsf r})^* = Z^\perp \subset H^{-s,-\mathsf r}$
(C4). If $f\in Z^\perp$, then $f$ annihilates $C_c^\infty(\{|x| < r_0\})\subset Z$, so
$\mathrm{supp}\,f\subset\bar\Omega$. Conversely, if $\mathrm{supp}\,f\subset\bar\Omega$ and $z\in Z$, approximate $z$
in $H^{s,\mathsf r}$ by elements of $C_c^\infty(\{|x| < r_0\})$, which is (a) for the ball, with $\lambda < 1$; each
pairs to 0 with $f$, so $\langle f,z\rangle = 0$. (c) Separate the two boundary spheres by a partition of unity and
apply (a) and (b) at each. (d) Locality of $L$ and (b). $\square$

### 6.2 The energy estimate

On $\{r_0 - 2\delta_0 < r < r_2\}$ let $\mathfrak g$ be the Lorentzian metric on $\tilde X$ whose inverse is the
bilinear form of $G_0$. Its signature is $(1,3)$ there, by (H4). Let $X := \mathfrak
g^{-1}(dr,\cdot) = \nabla r$, a $\mathfrak g$-timelike vector field, and time-orient $\mathfrak g$ so that $X$ is future
directed. Then $dr(V) = \mathfrak g(X,V) < 0$ for $V$ future timelike: $r$ decreases to the future, as in (H4). Let
$\square := -|\mathfrak g|^{-1/2}\partial_i|\mathfrak g|^{1/2}\mathfrak g^{ij}\partial_j$ act componentwise, with
principal symbol $G_0\,\mathrm{Id}$, and for $u$ valued in $\mathbb C^N$ (standard inner product) let

$$T[u](Y,Z) := \mathrm{Re}\big(\langle Yu, Zu\rangle - \tfrac12\mathfrak g(Y,Z)\,\mathfrak g^{ij}\langle\partial_iu,
\partial_ju\rangle\big),\qquad{}^{(Y)}K[u] := \tfrac12T[u]^{ij}(\mathcal L_Y\mathfrak g)_{ij}.$$

**Lemma 6.2 (energy identity).** For smooth $u$ and a smooth vector field $W$,
$\mathrm{div}_{\mathfrak g}(T[u](W,\cdot)^\sharp) = -\mathrm{Re}\langle\square u, Wu\rangle + {}^{(W)}K[u]$, and for
$w > 0$, ${}^{(wX)}K[u] = w\,{}^{(X)}K[u] + T[u](\nabla w, X)$.

*Proof.* Componentwise, with $T_{ij} = \mathrm{Re}(\partial_iu\,\partial_j\bar u - \frac12\mathfrak g_{ij}\partial^ku\,
\partial_k\bar u)$ summed over components,

$$\nabla^iT_{ij} = \mathrm{Re}\big(\nabla^i\partial_iu\,\partial_j\bar u + \partial^iu\,\nabla_i\partial_j\bar u -
\partial^ku\,\nabla_j\partial_k\bar u\big) = -\mathrm{Re}(\square u\,\partial_j\bar u),$$

since the Hessian of a function is symmetric and $\square = -\nabla^i\partial_i$. Then
$\nabla^i(T_{ij}W^j) = -\mathrm{Re}(\square u\,W\bar u) + T_{ij}\nabla^iW^j$ and
$T_{ij}\nabla^iW^j = \frac12T^{ij}(\mathcal L_W\mathfrak g)_{ij}$ by symmetry of $T$. For $W = wX$,
$T_{ij}\nabla^i(wX^j) = wT_{ij}\nabla^iX^j + T(\nabla w, X)$. $\square$

**Proposition 6.3 (the $H^1$ estimate).** Let $L$ be a differential operator of order 2 on $\{r_0 - 2\delta_0 < r <
r_2\}$ with principal symbol $G_0\,\mathrm{Id}$, and $r_0 - 2\delta_0 < a < b < r_2$. There is $C$, depending on bounds
for $L$'s coefficients and on $\inf(-G_0(dr))$ over the slab, such that

$$\|u\|_{H^1(\Omega_{a,b})}\le C\|Lu\|_{L^2(\Omega_{a,b})}$$

for $u\in H^2(\Omega_{a,b})^{\bullet,-}$ (forward), and likewise for $u\in H^2(\Omega_{a,b})^{-,\bullet}$ (backward).

*Proof.* By density (Lemma 6.1 (c), and smooth approximation up to the extendible side) take $u$ smooth on
$\bar\Omega_{a,b}$, vanishing near $r = b$ (forward case). Write $L = \square + L_1$ with $L_1\in\mathrm{Diff}^1$. Fix a
Riemannian metric $R$ and a density, and use coordinates $(r,\omega)$ on the slab ($r = |x|$). On the compact slab
there are constants with $T[u](X,X)\ge c_0|du|^2_R$ (in a $\mathfrak g$-orthonormal frame with $e_0 = X/|X|$,
$T(e_0,e_0) = \frac12\sum_\alpha|e_\alpha u|^2$), $|{}^{(X)}K[u]|\le C_0|du|_R^2$ and $|L_1u|\le C_1(|du|_R + |u|)$.

Let $w := e^{\lambda r}$, so $\nabla w = \lambda wX$, and $J := T[u](wX,\cdot)^\sharp$. By Stokes ($d(\iota_J|d\mathfrak
g|) = \mathrm{div}\,J\,|d\mathfrak g|$; the outward conormal at $r = a$ is $-dr$) and since $u = 0$ near $b$,

$$\int_{\Omega_{a,b}}\big(-\mathrm{Re}\langle\square u, wXu\rangle + {}^{(wX)}K[u]\big)|d\mathfrak g| =
-\int_{\{r = a\}}dr(J)\,\mu_a = -\int_{\{r = a\}}w\,T[u](X,X)\,\mu_a\le0,$$

where $\mu_a$ is the induced density, and $dr(J) = T(wX,\nabla r)$. So, by Lemma 6.2,

$$\int w\big(\lambda c_0 - C_0\big)|du|_R^2\le\int w\,|\square u||Xu|\le\int w|Lu||Xu| + C\int w(|du|^2_R + |u||du|_R).$$

*Weighted Poincaré inequality.* Since $u(r,\omega) = -\int_r^b\partial_su(s,\omega)\,ds$, with $\ell := b - a$,

$$\int_a^be^{\lambda r}|u(r)|^2dr\le\ell\int_a^b|\partial_su(s)|^2\int_a^se^{\lambda r}dr\,ds\le\frac\ell\lambda\int_a^b
e^{\lambda s}|\partial_su(s)|^2ds.$$

Integrating over $\omega$ with bounded Jacobians, $\int w|u|^2\le\frac{C_P}\lambda\int w|du|_R^2$. Hence
$C\int w|u||du|\le C(C_P/\lambda)^{1/2}\int w|du|^2$. For $\lambda$ large (depending on $c_0, C_0, C_1, C_P$) we get
$\frac{\lambda c_0}2 \int w|du|^2\le\int w|Lu||Xu|\le\frac{\lambda c_0}4\int w|du|^2 + \frac C\lambda\int w|Lu|^2$. So
$\int w|du|^2\le C\lambda^{-2}\int w|Lu|^2$, and with $e^{\lambda a}\le w\le e^{\lambda b}$ and Poincaré once more,
$\|u\|_{H^1}\le C\|Lu\|_{L^2}$.

Backward case: $u = 0$ near $a$; take $w := e^{-\lambda r}$. The flux is now at $r = b$, with sign $+$, and ${}^{(wX)}
K = w({}^{(X)}K - \lambda T(X,X))$. So $\int w(\lambda T(X,X) - {}^{(X)}K)\le\int w|\square u||Xu|$, and Poincaré runs
from $r = a$, where $w$ is largest. $\square$

(This is the corrected form of `../N1STAR-PROOF.md` 10.86 (r) at bounded frequency: the direct estimate takes
$e^{\lambda r}$, the adjoint $e^{-\lambda r}$, and $|u|^2$ comes from the Poincaré inequality; D184.)

**Proposition 6.4 (all orders).** Let $L$ be as in Proposition 6.3 on $\{r_0 - 2\delta_0 < r < r_2\}$, with $L^*$
also of that form (true for $\hat P(\sigma)$ and its adjoints). For every $s\in\mathbb R$ and slab $\Omega_{a,b}$ inside
$(r_0 - \delta_0, r_2 - \delta_0)$, the following hold.

(i) For every $u\in H^s(\Omega_{a,b})^{\bullet,-}$:
$\|u\|_{H^s(\Omega_{a,b})^{\bullet,-}}\le C\|Lu\|_{H^{s-1}(\Omega_{a,b})^ {\bullet,-}}$.

(ii) For every $u\in H^s(\Omega_{a,b})^{-,\bullet}$:
$\|u\|_{H^s(\Omega_{a,b})^{-,\bullet}}\le C\|Lu\|_{H^{s-1}(\Omega_{a,b})^ {-,\bullet}}$.

(iii) $L : H^s(\Omega_{a,b})^{\bullet,-}\to H^{s-1}(\Omega_{a,b})^{\bullet,-}$ is invertible, and so is the backward map.

$C$ depends only on bounds for the coefficients and on $\inf(-G_0(dr))$.

*Proof.* Fix $a' < a$ with $a' > r_0 - \delta_0$, and let $\Omega' := \Omega_{a',b}$. We prove (i); (ii) is the same with
the roles of the ends exchanged.

*Uniqueness.* Let $d\in H^t(\Omega_{a,b})^{\bullet,-}$ for some $t$, with $Ld = 0$. Let $D\in H^t(\mathbb R^4)$ be
supported in $\{r\le b\}$ with $D|_{\{r>a\}} = d$. Then $LD = 0$ on $\{r > a\}$ and $D = 0$ on $\{r > b\}$. By (H4) and
section 6.2, every null bicharacteristic of $G_0$ over $\{a < r < b + \delta_0\}$ moves monotonically in $r$, and its
backward direction (increasing $r$) reaches $\{r > b\}$, where $D$ vanishes. Proposition 5.2 (i) at every order gives
$D\in C^\infty(\{r > a\})$, as $D$ is smooth off the characteristic set by Proposition 5.1. So $d|_{[a+\epsilon,b]}$ is
smooth up to $r = b$ and vanishes to infinite order there; extended by 0 it lies in
$H^2(\Omega_{a+\epsilon,b})^{\bullet,-}$, and Proposition 6.3 on $\Omega_{a+\epsilon,b}$ gives $d = 0$ there, for every
$\epsilon > 0$ (D186).

*Existence for $s\ge0$.* Let
$f\in H^{s-1}(\Omega')^{\bullet,-}\subset H^{-1}(\Omega')^{\bullet,-} = (H^1(\Omega')^{-,\bullet})^*$. On
$\{L^*\varphi : \varphi\in H^2(\Omega')^{-,\bullet}\}\subset L^2(\Omega')$, the functional
$L^*\varphi\mapsto\langle f,\varphi\rangle$ is well defined. It is bounded, by $C\|f\|_{H^{-1}}\|L^*\varphi\|_{L^2}$, by
Proposition 6.3 (backward) for $L^*$. By Hahn-Banach and Riesz there is $w\in L^2(\Omega')$, with
$\|w\|\le C\|f\|_{H^{-1}}$, such that $\langle w, L^*\varphi\rangle = \langle f,\varphi\rangle$ for all such $\varphi$.
Taking $\varphi\in C_c^\infty(\{a' < r < b + \delta_0\})$, restricted, shows that the extension $W$ of $w$ by 0 beyond
$b$ satisfies $LW = F$ on $\{r > a'\}$, where $F$ is $f$'s supported extension. So
$w\in L^2(\Omega')^{\bullet,-} = L^2(\Omega')$ solves $Lw = f$.

*Regularity.* $W\in L^2$, $W = 0$ on $\{r > b\}$, and $LW\in H^{s-1}$ on $\{r > a'\}$. Proposition 5.2 (i) at order $s$,
propagating from $\{r > b\}$ along the monotone bicharacteristics, together with Proposition 5.1, gives $W\in H^s$ on
$\{r > a\}$, with
$\|w\|_{H^s(\Omega_{a,b})}\le C(\|f\|_{H^{s-1}(\Omega')} + \|w\|_{L^2(\Omega')})\le C\|f\|_ {H^{s-1}(\Omega')}$. Here
(5.1)'s error term $\|W\|_{-N}$ is bounded by $\|w\|_{L^2}$ for $N\ge0$.

*Proof of (i) and (iii) for $s\ge0$.* Given $u\in H^s(\Omega_{a,b})^{\bullet,-}$, extend $f := Lu$ to
$f'\in H^{s-1}(\Omega')^{\bullet,-}$ with $\|f'\|\le2\|f\|$, and let $w$ solve $Lw = f'$ on $\Omega'$. By uniqueness on
$\Omega_{a,b}$, $w|_{\Omega_{a,b}} = u$. So $\|u\|_{H^s}\le C\|f\|_{H^{s-1}}$, and $L$ is onto with this bound. It is
injective by uniqueness.

*$s < 0$.* By the case $1 - s > 0$ of (ii) for $L^*$, $\|\varphi\|_{H^{1-s}}\le C\|L^*\varphi\|_{H^{-s}}$ for
$\varphi\in H^{1-s}(\Omega')^{-,\bullet}$. The Hahn-Banach argument with these spaces produces, for
$f\in H^{s-1}(\Omega')^{\bullet,-} = (H^{1-s}(\Omega')^{-,\bullet})^*$, a solution
$w\in(H^{-s}(\Omega')^{-,\bullet})^* = H^s(\Omega')^{\bullet,-}$ with $\|w\|\le C\|f\|$, using Lemma 6.1 (c). Uniqueness
and the extension step finish (i) and (iii). $\square$

**Corollary 6.5 (the estimates used near $\partial_\sharp X$).** Let $r_0 < b' < b'' < r_2 - \delta_0$, $\chi_1\in
C_c^\infty(\{b' < r < b''\})$ equal to 1 on a neighbourhood of $\mathrm{supp}\,d\chi$, where $\chi = 1$ on $\{r\le b'\}$
and $\chi = 0$ near $\{r\ge b''\}$. Let $\mathcal D\subset\mathbb C$ be compact. Then for $\sigma\in\mathcal D$:

$$\|\chi u\|_{\bar H^s}\le C\big(\|\hat P(\sigma)u\|_{\bar H^{s-1}(\{r_0 < r < b''\})} + \|\chi_1u\|_{H^s}\big),\qquad
u\in
\bar H^s,\tag{6.1}$$

$$\|u|_{\Omega_{r_0,b''}}\|_{H^{1-s}(\Omega_{r_0,b''})^{-,\bullet}}\le C\|(\hat P(\sigma)^{*h}u)|_{\Omega_{r_0,b''}}\|_
{H^{-s}(\Omega_{r_0,b''})^{-,\bullet}},\qquad u\in\dot H^{1-s}.\tag{6.2}$$

*Proof.* (6.1): $\chi u\in H^s(\Omega_{r_0,b''})^{\bullet,-}$, and $\hat P(\chi u) = \chi\hat Pu + [\hat P,\chi]u$, with
$[\hat P,\chi]\in\mathrm{Diff}^1$ supported in $\mathrm{supp}\,d\chi$. Apply Proposition 6.4 (i). (6.2): the restriction
of $u$ to $\Omega_{r_0,b''}$ lies in $H^{1-s}(\Omega_{r_0,b''})^{-,\bullet}$ (supported at $r_0$, extendible at $b''$);
apply Proposition 6.4 (ii) to $L = \hat P(\sigma)^{*h}$. The constants are uniform in $\sigma\in\mathcal D$ since the
coefficients are polynomial in $\sigma$. $\square$

## 7. The spectral family at bounded nonzero frequencies

**Lemma 7.1 (admissible orders exist, locally uniformly).** Let $\sigma_*\ne0$ be real. Fix constants
$\mathsf r_{\mathrm{in}} > \frac12(-1 + \vartheta_{\mathrm{in}}) - \alpha_+$ and
$\mathsf r_{\mathrm{out}} < -\frac12 + \bar S - \alpha_+$ with $\mathsf r_{\mathrm{in}}\ge\mathsf r_{\mathrm{out}}$, and
$s_c > \frac12 + \vartheta_{\mathcal H}$. Then there is an order pair $(s,\mathsf r)$ admissible for every $\sigma_0$ in
a neighbourhood $J$ of $\sigma_*$, with weight $\alpha_+$ and a margin independent of $\sigma_0\in J$.

*Proof.* Take $s\equiv s_c$. Let $\varepsilon_* := \mathrm{sgn}\,\sigma_*$ and
$J := \{\sigma_0 : |\sigma_0 - \sigma_*| < |\sigma_*|/4\}$. Let $\Theta\in C^\infty(\mathbb R)$ satisfy
$\varepsilon_*\Theta'\le0$, $\Theta = 1$ on $\{\varepsilon_*\xi\le-\frac32|\sigma_*|\}$ and $\Theta = 0$ on
$\{\varepsilon_*\xi\ge-\frac12|\sigma_*|\}$. Let $\chi_c\in C_c^\infty$ equal 1 on
$\{\xi^2 + |\eta|^2\le(3|\sigma_*|)^2\}$, which contains $\Sigma^\partial_{\sigma_0}$ for $\sigma_0 \in J$ (Lemma 4.5:
$|\xi|\le2|\sigma_0|$, $|\eta|\le|\sigma_0|$ there). On the boundary face set

$$\mathsf r := \mathsf r_{\mathrm{out}} + (\mathsf r_{\mathrm{in}} - \mathsf
r_{\mathrm{out}})\,\Theta(\xi)\,\chi_c(\xi^2 +
|\eta|^2),$$

and extend it smoothly. Every $R_{\sigma_0,\mathrm{in}}$, $\sigma_0\in J$, has
$\varepsilon_*\xi = -2|\sigma_0| < -\frac32|\sigma_*|$, where $\mathsf r = \mathsf r_{\mathrm{in}}$; and
$R_{\mathrm{out}}$ has $\xi = 0$, where $\mathsf r = \mathsf r_{\mathrm{out}}$. By (4.5),
$\mathsf H_{\sigma_0}\xi = 2|\eta|^2$ at $\rho = 0$. So on $\Sigma^\partial_{\sigma_0}$,

$$\varepsilon_*\mathsf H_{\sigma_0}\mathsf r = (\mathsf r_{\mathrm{in}} - \mathsf
r_{\mathrm{out}})\varepsilon_*\Theta'(\xi)\, 2|\eta|^2\le0$$

, which is (O2). The thresholds (1.5) hold with the margins of the constants. $\square$

Fix a fibre inner product $h$ for the adjoints. For orders $(s,\mathsf r)$ and $\sigma$ set

$$\mathcal Y_\sigma := \bar H^{s-1,\mathsf r + \alpha_+ + 1},\qquad\mathcal X_\sigma := \{u\in\bar H^{s,\mathsf r +
\alpha_+} : \hat P(\sigma)u\in\mathcal Y_\sigma\},\qquad\mathcal X^*_\sigma := \{v\in\dot H^{1-s,-\mathsf r -
\alpha_+ - 1}
: \hat P(\sigma)^{*h}v\in\dot H^{-s,-\mathsf r - \alpha_+}\},$$

the first two being the domain and target of [Hin26c] (9.18). These are Hilbert spaces with the graph norms.

**Theorem 7.2 ([Hin26c] Theorem 9.5, at $n = 4$ on $E$).** Assume (H1)-(H4), and let $\alpha_+\in\mathbb R$.

(1) (*Fredholm estimates, I.*) Let $I\subset(0,\infty)$ or $I\subset(-\infty,0)$ be compact, $\nu\ge0$ and $N\in\mathbb
R$. Let $I\ni\sigma_0\mapsto(s,\mathsf r_{\sigma_0})$ be order pairs, continuous into $C^\infty$, each admissible for
$\sigma_0$ with weight $\alpha_+$, with margins and constancy neighbourhoods uniform in $\sigma_0$. There is $C$ such
that for $\sigma = \sigma_0 + i\sigma_1$ with $\sigma_0\in I$ and $\sigma_1\in[0,\nu]$, writing $\mathsf r :=
\mathsf r_{\sigma_0}$,

$$\|u\|_{\bar H^{s,\mathsf r + \alpha_+}}\le C\big(\|\hat P(\sigma)u\|_{\bar H^{s-1,\mathsf r + \alpha_+ + 1}} +
\|u\|_{\bar H^{-N,-N}}\big),\qquad u\in\mathcal X_\sigma,\tag{7.1}$$

$$\|v\|_{\dot H^{-s+1,-\mathsf r - \alpha_+ - 1}}\le C\big(\|\hat P(\sigma)^{*h}v\|_{\dot H^{-s,-\mathsf r - \alpha_+}} +
\|v\|_{\dot H^{-N,-N}}\big),\qquad v\in\mathcal X^*_\sigma.\tag{7.2}$$

(2) (*Fredholm estimates, II.*) Let $I\subset\mathbb R$ be compact and $0 < \nu^\flat\le\nu$. Let $s$ satisfy (O1) with
$s_c > \frac12 + \vartheta_{\mathcal H}$, and let $\mathsf r$ be constant near $R_{\mathrm{out}}$ with $\mathsf r +
\alpha_+ < -\frac12 + \bar S$ there. Then (7.1)-(7.2) hold uniformly for $\sigma\in I + i[\nu^\flat,\nu]$.

(3) (*Fredholm property.*) In the settings of (1) and (2), $\hat P(\sigma) : \mathcal X_\sigma\to\mathcal Y_\sigma$ is
Fredholm. Its kernel and the annihilator of its range do not depend on the admissible orders. Its index is independent
of $\sigma\in\{\sigma\ne0,\ \mathrm{Im}\,\sigma\ge0\}$. (That it is 0 is [Hin26c] Theorem 9.16 (3), in Part I.B.)

(4) (*Higher b-regularity.*) If $u\in\mathcal X_\sigma$ and $\hat P(\sigma)u\in\bar H^{(s-1;k),\mathsf r + \alpha_+ + 1}$
for some $k\in\mathbb N_0$, then $u\in\bar H^{(s;k),\mathsf r + \alpha_+}$ and

$$\|u\|_{\bar H^{(s;k),\mathsf r + \alpha_+}}\le C\big(\|\hat P(\sigma)u\|_{\bar H^{(s-1;k),\mathsf r + \alpha_+ + 1}} +
\|u\|_{\bar H^{s,\mathsf r + \alpha_+}}\big).\tag{7.3}$$

(5) (*Kernel elements, at $n = 4$.*) In the settings of (1) and (2), every $u\in\bar H^{s,\mathsf r + \alpha_+}$ with
$\hat P(\sigma)u = 0$ lies in

$$\mathcal A^{\frac32 + \bar S - \epsilon}(\bar X;E) := \rho^{\frac32 + \bar S - \epsilon}C^\infty_b(\bar
X;E)\quad\text{for
every }\epsilon > 0.\tag{7.4}$$

Here $C^\infty_b$ means smooth up to $\partial_\sharp X$ and conormal at $\partial X$. Conversely,
$\bigcap_{\epsilon>0}\mathcal A^{\frac32 + \bar S - \epsilon}\subset\mathcal X_\sigma$. If moreover $S(0,\cdot)$ has
constant spectrum on $\partial X$, then

$$u = \rho^{\frac32 + S(0,\cdot)}u_0 + \tilde u,\qquad u_0\in C^\infty(\partial X;E),\quad\tilde u\in\mathcal
A^{\frac52 +
\bar S - \epsilon}\ \ \forall\epsilon > 0,\tag{7.5}$$

where $\rho^{\frac32 + S(0,\cdot)} = \rho^{3/2}\exp(S(0,\cdot)\log\rho)$. This is the first step of [Hin26c] (9.21) at
$n = 4$; his $1 + \bar S$ and $\rho^{1+S}$ are the values at $n = 3$.

(6) (*Regularity in $\sigma$.*) Suppose $\hat P(\sigma_*) : \mathcal X_{\sigma_*}\to\mathcal Y_{\sigma_*}$ is invertible.
Then for $\sigma$ near $\sigma_*$, with orders fixed near $\sigma_*$ as in Lemma 7.1, the estimates (7.1) and (7.3) hold
without their last terms, uniformly, and $\hat P(\sigma)$ is invertible. For each $j\in\mathbb N_0$ and $\epsilon > 0$,
$\sigma\mapsto\hat P(\sigma)^{-1}$ is $j$ times continuously differentiable near $\sigma_*$ in the strong operator
topology, as a map
$\bar H^{(s+\epsilon-1;j),\mathsf r + \epsilon + \alpha_+ + 1}\to\bar H^{(s-\epsilon;0),\mathsf r - \epsilon + \alpha_+}$
(orders those at $\sigma_*$). If $\mathrm{Im}\,\sigma_* > 0$, it is holomorphic near $\sigma_*$ as a map
$\bar H^{s-1,\mathsf r + \alpha_+ + 1}\to\bar H^{s,\mathsf r + \alpha_+ - 1}$. Finally, for $k\in\mathbb N_0$,

$$\partial_\sigma^j\hat P(\sigma_*)^{-1} : \bar H^{(s-1;k+j),\mathsf r + \alpha_+ + 1}\to\bar H^{(s+j;k),\mathsf r +
\alpha_+}\ \text{boundedly}.\tag{7.6}$$

*Remark 7.3 (strong estimates, [Hin26c] Remark 9.6).* Each microlocal estimate below holds in the strong sense. Hence
(7.1) holds in the strong sense with the error term replaced by $\|u\|_{\bar H^{s_0,\mathsf r_0 + \alpha_+}}$ for orders
$s_0 < s$, $\mathsf r_0 < \mathsf r$ that are still above the thresholds at $\partial\mathcal R_\pm$ and at
$R_{\mathrm{in}}$: if the right side is finite, so is the left. Likewise for (7.2), with an a priori order at
$R_{\mathrm{out}}$.

### 7.1 Proof of (1)

Fix $\sigma = \sigma_0 + i\sigma_1$ as in (1), and write $\mathbf s := (s,\mathsf r + \alpha_+)$ and $\mathbf s' :=
\mathbf s - (1,-1)$. All constants below are uniform over $\sigma_0\in I$ and $\sigma_1\in[0,\nu]$, for three
reasons. The component estimates are uniform over compact parameter sets. The order family is continuous. And the
finite coverings chosen below for one $\sigma_0$ serve for $\sigma_0'$ near it, by continuity of the flows and of the
characteristic sets, so compactness of $I$ leaves finitely many.

*The pieces.* Let $\chi$, $\chi_1$, $b' < b''$ be as in Corollary 6.5, and $\chi_{\mathrm{far}} := 1 - \chi$, supported
in $\{r\ge b'\}\subset\bar X^\circ$. Then
$\|u\|_{\bar H^{\mathbf s}}\le C(\|\chi u\|_{\bar H^s} + \|\chi_{\mathrm{far}}u\|_ {H^{\mathbf s}})$. Choose a finite
microlocal partition of unity $\chi_{\mathrm{far}} = \sum_kQ_k + Q_{\mathrm{res}}$, with $Q_k\in\Psi^{0,0}$,
$Q_{\mathrm{res}}\in\Psi^{-\infty,-\infty}$ and kernels supported in $\{r > r_0 + \frac12(b' - r_0)\}^2$. Each $Q_k$ is
microsupported in one of the following open sets of the boundary of phase space, over the support of
$\chi_{\mathrm{far}}$.

(A) A neighbourhood $U_{\mathcal H}$ of $\partial\mathcal R_+\cup\partial\mathcal R_-$.

(B) A neighbourhood of a compact subset of $\partial\Sigma_0\setminus U'_{\mathcal H}$, with $\bar U'_{\mathcal H}\subset
U_{\mathcal H}$.

(C) A neighbourhood $U_{\mathrm{in}}$ of $R_{\sigma_0,\mathrm{in}}$.

(D) A neighbourhood of a compact subset of $\Sigma^\partial_{\sigma_0}\setminus(U'_{\mathrm{in}}\cup U'_{\mathrm{out}})$.

(E) A neighbourhood $U_{\mathrm{out}}$ of $R_{\mathrm{out}}$.

(F) The elliptic set of $\hat P(\sigma)$, uniformly in $\sigma$: fibre infinity off $\partial\Sigma_0$, including the
corner over $\partial X$ where the symbol is $\sim\xi^2 + |\eta|^2$, and the boundary face off a neighbourhood of
$\Sigma^\partial_{\sigma_0}$, where $|G_\sigma|\ge|g_{\sigma_0}|$ is bounded below.

For each $k$ choose $B_k$ elliptic on $\mathrm{WF}'(Q_k)$ from the corresponding estimate, so that $\|Q_ku\|_{\mathbf
s}\le C(\|B_ku\|_{\mathbf s} + \|u\|_{-\mathbf N})$.

*The estimates, in order.* (A): Proposition 4.2 (1), with $s_c > s_0 > \frac12 + \vartheta_{\mathcal H}$, gives
$\|B_Au\|_{s_c}\le C(\|G\hat Pu\|_{s_c-1} + \|Gu\|_{s_0} + \|u\|_{-N})$. (B): by (H4) every point of $\partial\Sigma_0$
over $\{r\ge b'\}$ outside $U'_{\mathcal H}$ lies on a curve of $\mathsf H$ whose backward continuation enters
$U'_{\mathcal H}$ in finite time. Proposition 5.2, use (i), with $E$ microsupported in $\mathrm{Ell}(B_A)$, applies along
it. By compactness finitely many curves suffice. (Near $r = b'$ such a curve stays over $\{r > r_0\}$ backward, since $r$
increases backward.) (C): Proposition 4.6 (1), with $\mathsf r_0 := \mathsf r - \frac\eta2$ at $R_{\mathrm{in}}$. (D): by
Lemma 4.5 every point of $\Sigma^\partial_{\sigma_0}$ outside $U'_{\mathrm{in}}\cup U'_{\mathrm{out}}$ lies on a curve of
$\varepsilon_0\mathsf H_{\sigma_0}$ whose backward continuation enters $U'_{\mathrm{in}}$. Proposition 5.2, use (ii),
applies, with $E$ in $\mathrm{Ell}(B_C)$ and the order monotone by (O2). (E): Proposition 4.9 (1), with $E$ elliptic on
the set $K_E^*$ of Lemma 3.2 and microsupported near it, $U'_{\mathrm{out}}$ being chosen disjoint from $K_E^*$ (D187);
its part on $\Sigma^\partial_{\sigma_0}$ lies in the region (D), and its part off it lies in (F). (F): Proposition 5.1.
Each $E$-term is bounded by the estimates of earlier pieces. Each $\|G\hat P(\sigma)u\|$ is at most $C\|\hat
P(\sigma)u\|_{\bar H^{\mathbf s'}}$, since $G$ has kernel supported in $\bar X^\circ$. The orders used are those of
$\mathbf s$, through (O1)-(O3): at fibre infinity over the compact region only $s_c$ matters, at the boundary face only
$\mathsf r + \alpha_+$, and at the corner both, by ellipticity.

*The artificial boundary.* By (6.1),
$\|\chi u\|_{\bar H^s}\le C(\|\hat P(\sigma)u\|_{\bar H^{s-1}} + \|\chi_1u\|_{H^s})$. $\chi_1u$ is compactly supported in
$\{b' < r < b''\}$, so $\|\chi_1u\|_{H^s}$ is bounded by the pieces (B) and (F) over that region, at order $s_c$.

*Absorbing the a priori terms.* Adding up,

$$\|u\|_{\bar H^{\mathbf s}}\le C\big(\|\hat P(\sigma)u\|_{\bar H^{\mathbf s'}} + \|u\|_{\bar H^{\mathbf s - \tau\mathbf
1}} + \|u\|_{\bar H^{-\mathbf N}}\big),\qquad\tau := \min(s_c - s_0,\tfrac\eta2) > 0.$$

The embedding $\bar H^{\mathbf s}\hookrightarrow\bar H^{\mathbf s - \tau\mathbf 1}$ is compact: take extensions,
multiply by a fixed cut-off, and use (C4). Ehrling's lemma then gives $\|u\|_{\mathbf s - \tau\mathbf 1}\le\delta
\|u\|_{\mathbf s} + C_\delta\|u\|_{-\mathbf N}$. For $u\in\bar H^{\mathbf s}$ the left side is finite, so taking $\delta$
small and absorbing proves (7.1).

*The adjoint estimate.* For $v\in\dot H^{1-s,-\mathsf r - \alpha_+ - 1}$, run the chain in the reverse order with the
adjoint estimates. (E*): Proposition 4.9 (2) at $R_{\mathrm{out}}$, above threshold, with an a priori order
$-\mathsf r_0' - \alpha_+ - 1 < -\mathsf r - \alpha_+ - 1$, still above the adjoint threshold by (1.5)'s margin. (D*):
Proposition 5.2 for $\hat P^{*h}$ with the backward field, propagating from $U'_{\mathrm{out}}$; the order is
$-\mathsf r - \alpha_+ - 1$, monotone along the backward field. (C*): Proposition 4.6 (2), with $E$ in the region (D*).
At fibre infinity: (6.2) bounds $v$ on $\{r_0\le r\le b''\}$ by $\hat P^{*h}v$ alone. (B*): Proposition 5.2 with the
backward field, from that region toward $\partial\mathcal R_\pm$, since backward curves of $\mathsf H$ starting near
$r_0$ reach every point of $\partial\Sigma_0$ outside $U'_{\mathcal H}$. (A*): Proposition 4.2 (2), with $E$ in the
region (B*). (F) as before. The a priori term at $R_{\mathrm{out}}$ is absorbed as above, which proves (7.2).

### 7.2 Proof of (2)

For $\sigma_1\ge\nu^\flat > 0$, $G_\sigma = g_{\sigma_0} + 2i\sigma_1\xi$ vanishes on the boundary face only where
$\xi = 0 = |\eta|$, that is on $R_{\mathrm{out}}$. On the complement of a neighbourhood of $R_{\mathrm{out}}$,
$|G_\sigma|$ is bounded below uniformly for $\sigma\in I + i[\nu^\flat,\nu]$, including near fibre infinity. So the
boundary face contributes only (E) and (F) (and (E*), (F) for the adjoint). Proposition 4.9 holds on the compact set
$I + i[\nu^\flat, \nu]\subset\{\sigma\ne0,\mathrm{Im}\,\sigma\ge0\}$, and its $E$-term lies in (F). Fibre infinity and
the artificial boundary are as in (1). No condition on $\mathsf r$ is used except at $R_{\mathrm{out}}$. $\square$

### 7.3 Proof of (3)

*Fredholm.* $\mathcal X_\sigma\hookrightarrow\bar H^{-N,-N}$ is compact for $N > \max(-s, \sup(-\mathsf r - \alpha_+))$,
so (7.1) gives a finite-dimensional kernel and closed range (Peetre's lemma). Likewise (7.2) for $\hat P^{*h}$ on
$\mathcal X^*_\sigma$.

*Green's formula.* For $u\in\mathcal X_\sigma$ and $v\in\mathcal X^*_\sigma$, $\langle\hat P(\sigma)u,v\rangle = \langle
u,\hat P(\sigma)^{*h}v\rangle$, with the $h$-pairings $\langle\cdot,\cdot\rangle_h$: the pairings of Lemma 6.1 (b) with
the weight $H$ inserted, for which $\hat P^{*h}$ is the adjoint (D186). *Proof.* Let $f := \hat Pu$, and extend $\chi u$
beyond $r_0$ as a solution. With $a'\in(r_0 - \delta_0, r_0)$, let $f'$ extend $\hat P(\chi u)$ to $\Omega_{a', b''}$,
and let $w$ solve $\hat Pw = f'$ there (Proposition 6.4 (iii)); by uniqueness $w = \chi u$ on $\Omega_{r_0,b''}$. Then
$\tilde u := \chi'(w + (1 - \chi)u)$, with $\chi'$ a cut-off equal to 1 on $\{r\ge r_0 - \frac12(r_0 - a')\}$ and
supported in $\{r > a'\}$, lies in $H^{\mathbf s}(\mathbb R^4)$, restricts to $u$, and has $\hat P\tilde u\in H^{\mathbf
s'}(\mathbb R^4)$. With $T_t$ from (C8), $u_t := T_t\tilde u$ is Schwartz, $u_t\to\tilde u$ in $H^{\mathbf s}$, and $\hat
Pu_t = T_t\hat P\tilde u + [\hat P,T_t]\tilde u\to\hat P\tilde u$ in $H^{\mathbf s'}$. This uses that $[\hat P,T_t]$ is
bounded in $\Psi^{1,-1}$, maps $H^{\mathbf s}\to H^{\mathbf s'}$, and tends to 0 strongly (as in Lemma 3.1, Step 1). For
Schwartz $u_t$ the identity is the definition of $\hat P^{*h}v$ as a distribution. Pass to the limit, using that $v$ and
$\hat P^{*h}v$ are supported in $\bar X$, so the pairings see only $u$ and $\hat Pu$. $\square$

*Cokernel.* $v\in\dot H^{1-s,-\mathsf r - \alpha_+ - 1} = \mathcal Y_\sigma^*$ annihilates the range if and only if
$v\in \ker_{\mathcal X^*_\sigma}\hat P^{*h}$. Indeed, $C_c^\infty(\mathbb R^4)|_{\bar X}\subset\mathcal X_\sigma$, so an
annihilator satisfies $\langle\varphi,\hat P^{*h}v\rangle = 0$ for all $\varphi\in C_c^\infty(\mathbb R^4)$; the converse
is Green's formula. Symmetrically, $w\in\bar H^{s,\mathsf r + \alpha_+} = (\dot H^{-s,-\mathsf r - \alpha_+})^*$
annihilates $\hat P^{*h}(\mathcal X^*_\sigma)$ if and only if $w\in\ker_{\mathcal X_\sigma}\hat P$, testing with
$C_c^\infty(\bar X^\circ)\subset\mathcal X^*_\sigma$. Hence
$\mathrm{ind}(\hat P^{*h}|_{\mathcal X^*_\sigma}) = -\mathrm{ind} (\hat P|_{\mathcal X_\sigma})$.

*Independence of the orders.* By (5), whose proof uses only (1)-(2) and (4), kernel elements lie in
$\bigcap_\epsilon \mathcal A^{\frac32 + \bar S - \epsilon}$, contained in $\mathcal X_\sigma$ for every admissible order.
For the adjoint: if $v$ lies in the kernel for one admissible order, the strong forms of the adjoint estimates place it
in the space of any other. At $R_{\mathrm{out}}$ the adjoint estimate is above threshold, with the a priori order given
by $v$'s own space (whose order is above the threshold, by (O3)). Elsewhere the adjoint estimates are below threshold or
propagation estimates, with no a priori condition.

*Local constancy of the index.* Let $\sigma_*$ be in one of the settings, and fix orders admissible for all $\sigma$ near
$\sigma_*$: Lemma 7.1 if $\sigma_*$ is real, any $\mathsf r$ as in (2) if $\mathrm{Im}\,\sigma_* > 0$. Let
$\mathcal N := \ker\hat P(\sigma_*)$. Let $\mathcal R\subset C_c^\infty(\bar X^\circ;E)$ be a complement of the closed,
finite codimensional range in $\mathcal Y_{\sigma_*}$; it exists because $C_c^\infty(\bar X^\circ)$ is dense in
$\mathcal Y_{\sigma_*}$. Let $E_{01} : \mathbb C^{\dim\mathcal R}\to\mathcal R$ be an isomorphism and
$E_{10}u := (\langle u, v_j\rangle)_j$ with $v_j\in C_c^\infty(\bar X^\circ)$ chosen so that $E_{10}|_{\mathcal N}$ is an
isomorphism. Then
$\tilde P(\sigma) := \big(\begin{smallmatrix}\hat P(\sigma) & E_{01}\\ E_{10} & 0\end{smallmatrix}\big)$ has index
$\mathrm{ind}\,\hat P(\sigma) + \dim\mathcal R - \dim\mathcal N$, and is invertible at $\sigma_*$.

*$\tilde P(\sigma)$ is injective near $\sigma_*$.* Otherwise there are $\sigma_j\to\sigma_*$ and $(u_j,c_j)\ne0$ in the
kernel, normalised by $\|u_j\|_{-\mathbf N} + |c_j| = 1$. By (7.1),
$\|u_j\|_{\mathbf s}\le C(|c_j| + \|u_j\|_{-\mathbf N})\le C$. Pass to a subsequence with $u_j\rightharpoonup u$ in
$\bar H^{\mathbf s}$, hence $u_j\to u$ in $\bar H^{-\mathbf N}$ (compactness), and $c_j\to c$. Then
$\|u\|_{-\mathbf N} + |c| = 1$. Moreover $\hat P(\sigma_j)u_j\to\hat P(\sigma_*)u$ as distributions, so
$\hat P(\sigma_*)u = -E_{01}c$ and $u\in\mathcal X_{\sigma_*}$, and $E_{10}u = \lim E_{10}u_j = 0$. This contradicts
invertibility at $\sigma_*$.

So $\mathrm{ind}\,\hat P(\sigma)\le\dim\mathcal N - \dim\mathcal R = \mathrm{ind}\,\hat P(\sigma_*)$ near $\sigma_*$. The
same argument for the adjoint family, with (7.2), gives
$\mathrm{ind}\,\hat P^{*h}(\sigma)\le\mathrm{ind}\,\hat P^{*h}(\sigma_*)$, that is
$\mathrm{ind}\,\hat P(\sigma)\ge\mathrm{ind}\,\hat P(\sigma_*)$. So the index is locally constant, and by independence of
the orders it does not depend on the local choice of orders. The set $\{\sigma\ne0,\mathrm{Im}\, \sigma\ge0\}$ is
connected and covered by these neighbourhoods, so the index is constant. $\square$

### 7.4 Proof of (4)

Run the chain of section 7.1 with the orders $\mathbf s + k\mathbf 1$ away from $R_{\mathrm{out}}$, and with Proposition
4.9 (3) at $R_{\mathrm{out}}$. By Lemma 4.10, away from the zero section of the boundary face (and at fibre infinity)
$H^{(s;k),\mathsf r}$ and $H^{s+k,\mathsf r+k}$ are microlocally the same, uniformly. The shifted orders still satisfy
(O1)-(O3) at $\partial\mathcal R_\pm$ and $R_{\mathrm{in}}$ (they are larger there) and (O2) (shifted by a constant).
Over compact subsets of $\bar X^\circ$, $(s;k)$-regularity is $H^{s+k}$, and Corollary 6.5 holds at order $s + k$. The a
priori terms are bounded by $\|u\|_{\bar H^{s,\mathsf r + \alpha_+}}$ because $u\in\mathcal X_\sigma$. $\square$

### 7.5 Proof of (5)

**Lemma 7.4 (conormal functions and scattering spaces).** Let $a\in\mathbb R$. (a)
$\mathcal A^a\subset\bar H^{s,\mathsf r'}$ for every $s$ and every order $\mathsf r'$ with $\mathsf r' < a - 2$ on a
neighbourhood of the zero section $o_{\partial X}$ of the boundary face. (b) Conversely, if
$u\in\bar H^{(s;k),\mathsf r'}$ for every $k$, with $\mathsf r'\equiv\mathsf r_*$ constant near $o_{\partial X}$, then
$u\in\rho^{\mathsf r_* + 2}C^\infty_b$ near $\partial X$.

*Proof.* Near $\partial X$, $|dx| = \rho^{-5}d\rho\,d\omega$, and $\mu_b := \rho^4|dx| = \rho^{-1}d\rho\,d\omega$ is the
b-density. So $H^{0,\mathsf r_*}_{\mathrm{sc}} = \rho^{\mathsf r_*}L^2(|dx|) = \rho^{\mathsf r_* + 2}L^2(\mu_b)$. Also
$H^{(s;k),\mathsf r'}\subset H^{s+k,\mathsf r'}$. For $k = 1$: if $u\in H^{(s;1),\mathsf r'}$ then
$\partial_ju = \langle x\rangle^{-1}(\langle x\rangle\partial_ju)\in H^{s,\mathsf r'+1}\subset H^{s,\mathsf r'}$, and
$u,\partial u\in H^{s,\mathsf r'}$ give $u\in H^{s+1,\mathsf r'}$ by ellipticity of $\langle D\rangle\in\Psi^{1,0}$;
induct on $k$. By Lemma 4.10, microlocally away from $o_{\partial X}$, $H^{(s;k),\mathsf r'}$ is $H^{s+k,\mathsf r'+k}$.

(a) For $u = \rho^aw$ with $V^\alpha w$ bounded for all $\alpha$, $\int|V^\alpha u|^2\rho^{-2\mathsf r_*}|dx|<\infty$
near $\partial X$ if and only if $2a - 2\mathsf r_* - 5 > -1$, that is $\mathsf r_* < a - 2$. So
$u\in H^{(0;k),\mathsf r_*}$ for all $k$, near $o_{\partial X}$ at order $\mathsf r_*$, and away from it at every order.
Hence $u\in H^{s,\mathsf r'}$ for every $s$ and every $\mathsf r'$ as stated.

(b) Let $Q\in\Psi^{0,0}$ be microlocally the identity near $o_{\partial X}$, microsupported where
$\mathsf r' = \mathsf r_*$. Then $(\mathrm{Id} - Q)u\in H^{\infty,\infty}$ by the last remark, and
$Qu\in H^{(0;\infty),\mathsf r_*}$, so $\rho^{-\mathsf r_* - 2}Qu\in H^\infty_b(\mu_b)$ near $\partial X$, as
$[V,\rho^c]\in\rho^cC^\infty$. In $t := -\log\rho$, $(\rho,\omega)\mapsto(t,\omega)$ takes b-vector fields to vector
fields on the half-cylinder $(t_1,\infty)\times\mathbb S^3$ spanned by $\partial_t$ and $\mathcal V(\mathbb S^3)$, and
$\mu_b$ to $dt\,d\omega$. Sobolev embedding on the unit cylinders $(t_0,t_0+1)\times\mathbb S^3$, with $k > 2 = \frac n2$
and constants independent of $t_0$, gives $H^\infty_b(\mu_b)\subset C^\infty_b$. $\square$

*Proof of (5).* Let $u\in\bar H^{s,\mathsf r + \alpha_+}$ with $\hat P(\sigma)u = 0$. By Remark 7.3, $u$ lies in
$\bar H^{s',\mathsf r' + \alpha_+}$ for every admissible $(s',\mathsf r')$, since the a priori terms are given by $u$'s
own space. In particular this holds for every $s'\ge s$ and for decay orders whose value at $R_{\mathrm{out}}$ is any
number $< -\frac12 + \bar S - \alpha_+$ (Lemma 7.1, with Lemma 2.4 for the inner product at $R_{\mathrm{out}}$). By (4)
with $f = 0$, $u\in\bar H^{(s';k),\mathsf r' + \alpha_+}$ for all $k$. Lemma 7.4 (b), with $\mathsf r_* = (\mathsf r' +
\alpha_+)(R_{\mathrm{out}})$ arbitrarily close to $-\frac12 + \bar S$, gives $u\in\rho^{\frac32 + \bar S - \epsilon}
C^\infty_b$ near $\partial X$. Away from $\partial X$, $u\in\bar H^{s'}$ for all $s'$, which is smoothness up to
$\partial_\sharp X$. This proves (7.4).

Converse. Let $u\in\bigcap_\epsilon\mathcal A^{\frac32 + \bar S - \epsilon}$. Since $\mathsf r + \alpha_+$ is constant
and $< -\frac12 + \bar S$ near $R_{\mathrm{out}} = o_{\partial X}$, Lemma 7.4 (a) with $a = \frac32 + \bar S - \epsilon$
($\epsilon$ small) gives $u\in\bar H^{s,\mathsf r + \alpha_+}$. Each part of $\hat P(\sigma)$ maps $\mathcal A^a$ to
$\mathcal A^{a+1}$: $\rho\mathrm{Diff}^1_b$, $\rho^2\mathrm{Diff}^2_b$, $\rho^3\mathrm{Diff}^1_b$ and $\rho^2C^\infty$
do. So $\hat P(\sigma)u\in\mathcal A^{a+1}\subset\bar H^{s-1,\mathsf r + \alpha_+ + 1}$, again by Lemma 7.4 (a). Hence
$u\in\mathcal X_\sigma$.

The leading term. Let $S_0 := S(0,\cdot)$, with constant spectrum $\{\lambda_1,\dots,\lambda_m\}$. Its Riesz projections
$\Pi_\lambda(\omega) = \frac1{2\pi i}\oint_{|z - \lambda| = \delta}(z - S_0)^{-1}dz$ are smooth, the contours being
fixed. They commute with $S_0$, and $N_\lambda := (S_0 - \lambda)\Pi_\lambda$ is nilpotent and smooth. Let
$a := \frac32 + \bar S - \epsilon$. Near $\partial X$, $\hat P(\sigma)u = 0$ and (1.2) give

$$(\rho\partial_\rho - \tfrac32 - S_0)u = F' := -(2i\sigma\rho)^{-1}\big(\hat P(0) - i\sigma Q +
\sigma^2g_{00}\big)u + (S -
S_0)u\in\mathcal A^{a+1},$$

because $\hat P(0)u\in\mathcal A^{a+2}$, $Qu\in\mathcal A^{a+3}$, $g_{00}u\in\mathcal A^{a+2}$ and
$S - S_0\in\rho C^\infty$. Let $v := \Pi_\lambda u$, $\mu := \frac32 + \lambda$ and $g := \Pi_\lambda F'$; then
$(\rho\partial_\rho - \mu - N_\lambda)v = g$. Equivalently
$\partial_\rho(\rho^{-\mu - N_\lambda}v) = \rho^{-\mu - N_\lambda - 1}g$, and
$\|\tau^{\mu + N_\lambda}\|\le C\tau^{\mathrm{Re}\mu}(1 + |\log\tau|)^{N-1}$.

Case $\mathrm{Re}\,\mu < a + 1$. Then $\int_0^{\rho_1}\|s^{-\mu - N_\lambda - 1}g(s)\|ds < \infty$, so
$v = \rho^{\mu + N_\lambda}c_\lambda + \rho^{\mu + N_\lambda}\int_0^\rho s^{-\mu - N_\lambda - 1}g(s)\,ds$ with
$c_\lambda\in C^\infty(\partial X;\mathrm{ran}\,\Pi_\lambda)$. The integral term is bounded by
$C\rho^{a+1}\int_0^1\tau^{a - \mathrm{Re}\mu}(1 + |\log\tau|)^ {N-1}d\tau\le C\rho^{a+1}$. The same holds for its
$V^\alpha$-derivatives: $\rho\partial_\rho$ of it is $(\mu + N_\lambda)$ times it plus $g$, and angular derivatives fall
on smooth factors. So it lies in $\mathcal A^{a+1}$.

Case $\mathrm{Re}\,\mu\ge a + 1$. Write $v = \rho^{\mu + N_\lambda}\rho_1^{-\mu - N_\lambda}v(\rho_1) - \rho^{\mu +
N_\lambda}\int_\rho^{\rho_1}s^{-\mu - N_\lambda - 1}g\,ds$. Both terms are $O(\rho^{a+1}|\log\rho|^N)$ with their
derivatives, hence in $\mathcal A^{a+1-\epsilon'}$.

Summing over $\lambda$,

$$u = \sum_{\mathrm{Re}\lambda < \bar S + 1 - \epsilon}\rho^{\frac32 + \lambda + N_\lambda}c_\lambda + \mathcal
A^{\frac52 + \bar S - \epsilon - \epsilon'}$$

. This is $\rho^{\frac32 + S_0}u_0$ with $u_0 := \sum c_\lambda$ (the terms with
$\mathrm{Re}\,\lambda\ge\bar S + 1 - \epsilon$ being absorbed into the remainder), which is (7.5). No condition on
integer differences of the spectrum is needed for this step. $\square$

### 7.6 Proof of (6)

Fix orders admissible near $\sigma_*$ (Lemma 7.1, or (2)).

*Estimates without error terms.* If (7.1) without its last term failed uniformly near $\sigma_*$, there would be
$\sigma_j\to\sigma_*$ and $u_j$ with $\|u_j\|_{\mathbf s} = 1$ and $\|\hat P(\sigma_j)u_j\|_{\mathbf s'}\to0$. By (7.1),
$\|u_j\|_{-\mathbf N}\ge c > 0$. A weak limit in $\bar H^{\mathbf s}$, which is a norm limit in $\bar H^{-\mathbf N}$,
is nonzero and lies in $\ker\hat P(\sigma_*)$. That is a contradiction. The same argument applies to (7.3).

*Invertibility.* By the above, $\hat P(\sigma)$ is injective near $\sigma_*$; by (3) its index equals that at $\sigma_*$,
which is 0. So it is invertible, with $\|\hat P(\sigma)^{-1}\|_{\mathcal Y_\sigma\to\bar H^{\mathbf s}}\le C$ uniformly.

*Continuity.* Let $f\in\bar H^{\mathbf s' + \epsilon\mathbf 1}$ and $u(\sigma) := \hat P(\sigma)^{-1}f$. The orders
$\mathbf s\pm\frac\epsilon2\mathbf 1$ are admissible for $\epsilon$ small (the margins), so $u(\sigma)$ is bounded in
$\bar H^{\mathbf s + \frac\epsilon2\mathbf 1}$. For $\sigma_j\to\sigma$, a subsequence converges weakly there, hence in
norm in $\bar H^{\mathbf s - \epsilon\mathbf 1}$, to some $u_0$ with $\hat P(\sigma)u_0 = f$. By uniqueness in
$\mathcal X_\sigma$ at the orders $\mathbf s - \epsilon\mathbf 1$ (admissible), $u_0 = u(\sigma)$, so the whole sequence
converges.

*Differentiability.* $\hat P(\sigma) - \hat P(\sigma_*) = (\sigma - \sigma_*)(T + (\sigma + \sigma_*)P_2)$, so

$$\frac{\hat P(\sigma)^{-1} - \hat P(\sigma_*)^{-1}}{\sigma - \sigma_*} = -\hat P(\sigma)^{-1}\big(T + (\sigma +
\sigma_*)
P_2\big)\hat P(\sigma_*)^{-1}.$$

$T\in\rho\mathrm{Diff}^1_b$ near $\partial X$ (by (1.2)) and $P_2\in\rho^2C^\infty$. So $T$ maps $\bar H^{(t;q),\mathsf
t}\to\bar H^{(t;q-1),\mathsf t + 1}$, trading one b-derivative for one order of decay; away from $\partial X$ it is a
first-order operator, and $(t;q)$-regularity is $H^{t+q}$ there. Hence $f\in\bar H^{(s + \epsilon - 1;1),\mathsf r +
\epsilon + \alpha_+ + 1}$ maps under $\hat P(\sigma_*)^{-1}$ to $\bar H^{(s+\epsilon;1),\mathsf r + \epsilon + \alpha_+}$
by (4), then under $T + \dots$ to $\bar H^{s+\epsilon,\mathsf r + \epsilon + \alpha_+ + 1}$. By continuity, $\hat
P(\sigma)^{-1}$ of that tends to $\hat P(\sigma_*)^{-1}$ of it in $\bar H^{\mathbf s - \epsilon\mathbf 1}$. So the
difference quotients converge strongly, to $-\hat P^{-1}(T + 2\sigma_*P_2)\hat P^{-1}$. For $j\ge2$ the same argument
runs at b-regular levels. First, for $q\in\mathbb N_0$ and $f\in\bar H^{(s+\epsilon-1;q),\mathsf r+\epsilon+\alpha_++1}$,
$\sigma\mapsto\hat P(\sigma)^{-1}f$ is continuous into $\bar H^{(s-\epsilon;q),\mathsf r-\epsilon+\alpha_+}$: the proof
of *Continuity* applies with (7.3), uniform near $\sigma_*$ by the first paragraph, in place of (7.1), since $\bar
H^{(t;q),\mathsf t}\hookrightarrow\bar H^{(t';q),\mathsf t'}$ is compact for $t'<t$, $\mathsf t'<\mathsf t$ ((C4) for
each b-derivative up to order $q$). Then $\partial^j_\sigma\hat P^{-1}$, a finite sum of products as in (7.6), is
obtained from $\partial^{j-1}_\sigma\hat P^{-1}$ as $\partial_\sigma\hat P^{-1}$ was from $\hat P^{-1}$: the difference
quotient of a product splits into terms in which one factor $\hat P^{-1}$ is differenced, handled by the case $j = 1$ at
a b-regular level, and terms in which a factor $D_i$ is differenced, polynomial in $\sigma$. Every factor is uniformly
bounded and strongly continuous between the spaces of (7.6) with $\epsilon$-losses, so the products are strongly
continuous. This spends $j$ b-derivatives and $j\epsilon$ in orders; renaming $\epsilon$ gives the $C^j$ statement
(D186).

*Holomorphy.* For $\mathrm{Im}\,\sigma_* > 0$ the orders in (2) may have any decay order below the threshold at
$R_{\mathrm{out}}$, so $\mathsf r - 1$ is admissible. $T + (\sigma + \sigma_*)P_2\in\Psi^{1,0}$ maps $\bar H^{s,\mathsf
r + \alpha_+}\to\bar H^{s-1,\mathsf r + \alpha_+}$, and $\hat P(\sigma)^{-1}$ maps that to $\bar H^{s,\mathsf r +
\alpha_+ - 1}$, uniformly near $\sigma_*$. So $\|\hat P(\sigma)^{-1} - \hat P(\sigma')^{-1}\|\le C|\sigma - \sigma'|$
for $\sigma,\sigma'$ near $\sigma_*$, as maps $\mathcal A := \bar H^{s-1,\mathsf r + \alpha_+ + 1}\to\mathcal B := \bar
H^{s,\mathsf r + \alpha_+ - 1}$, and likewise at the orders $(s,\mathsf r - 1)$. A Lipschitz bound does not by itself
make difference quotients converge (D186), so we argue as follows. The difference quotient is $D(\sigma) := -\hat
P(\sigma)^{-1}M(\sigma)\hat P(\sigma_*)^{-1}$, $M(\sigma) := T + (\sigma + \sigma_*)P_2$, and $D(\sigma) - D(\sigma') =
-(\hat P(\sigma)^{-1} - \hat P(\sigma')^{-1})M(\sigma)\hat P(\sigma_*)^{-1} - (\sigma - \sigma')\hat
P(\sigma')^{-1}P_2\hat P(\sigma_*)^{-1}$. By the Lipschitz bound at the orders $(s,\mathsf r - 1)$, both terms are
$O(|\sigma - \sigma'|)$ as maps $\mathcal A\to\mathcal B' := \bar H^{s,\mathsf r + \alpha_+ - 2}$. So $D(\sigma)$ is
Cauchy in $L(\mathcal A,\mathcal B')$ as $\sigma\to\sigma_*$, and the same holds at every point near $\sigma_*$: $\hat
P^{-1}$ is holomorphic into $L(\mathcal A,\mathcal B')$. It is norm-continuous into $L(\mathcal A,\mathcal B)$ by the
Lipschitz bound. Cauchy's integral formula over a small circle holds in $L(\mathcal A,\mathcal B')$, and its integrand
is continuous into $L(\mathcal A,\mathcal B)$; so it represents $\hat P^{-1}$ as a holomorphic $L(\mathcal A,\mathcal
B)$-valued function.

*(7.6).* $\partial_\sigma^j(\hat P^{-1})$ is a sum of products $\hat P^{-1}D_1\hat P^{-1}D_2\cdots D_m\hat P^{-1}$ with
$D_i\in\{\partial_\sigma\hat P,\partial^2_\sigma\hat P\} = \{T + 2\sigma P_2, 2P_2\}$ and $\sum(\text{order of }\partial)
= j$. Each $D_i$ maps $\bar H^{(t;q),\mathsf t}\to\bar H^{(t;q-1),\mathsf t + 1}$ (and $2P_2$ even to $\bar H^{(t;q),
\mathsf t + 2}$). Each $\hat P^{-1}$ maps $\bar H^{(t-1;q),\mathsf r + \alpha_+ + 1}\to\bar H^{(t;q),\mathsf r +
\alpha_+}$ for $t = s + \ell$, $\ell\ge0$. That is (4) and invertibility at the orders $(s + \ell,\mathsf r)$, which are
admissible since raising $s$ by a constant preserves (O1)-(O3). Starting from $\bar H^{(s-1;k+j),\mathsf r + \alpha_+ +
1}$, each pair $D_i\hat P^{-1}$ raises $t$ by one and spends one b-derivative, which ends in $\bar H^{(s+j;k),\mathsf r +
\alpha_+}$. This is [Hin26c] (9.57) at $n = 4$; the formula $\sigma\partial_\sigma\hat P(\sigma) =
2i\sigma\rho(\rho\partial_\rho - \frac32 - S) - i\sigma Q + 2\sigma^2g_{00}$ is his (9.56) at $n = 4$. The count treats
every $D_i$ as spending one b-derivative; the factors $2P_2$ spend none, which only helps, since $\bar H^{(t;q+1),\mathsf
t}\subset\bar H^{(t+1;q),\mathsf t}$ (D186). $\square$

## 8. Uniformity in the operator

**Theorem 8.1.** Assume (H1)-(H5). Then the constants in Propositions 4.2, 4.6, 4.9, 5.1, 5.2, 6.3, 6.4 and Theorem 7.2
(1), (2) and (4) can be chosen uniform in $b\in\mathcal B$, for fixed orders admissible at every $b$ (with uniform
margins). The index in Theorem 7.2 (3) is constant on connected subsets of $\{(\sigma,b)\}$. If $\hat P^{b_*}(\sigma_*)$
is invertible, then $\hat P^b(\sigma)$ is invertible for $(\sigma,b)$ near $(\sigma_*,b_*)$, with uniformly bounded
inverses that depend continuously on $(\sigma,b)$ in the strong operator topology, and the statements of Theorem 7.2 (6)
hold jointly in $(\sigma,b)$.

*Proof.* Every constant above is produced by finitely many seminorms of the operator's coefficients, which depend
continuously on $b$ by (H5). It is also produced by positivity margins: $c_Q$ in each radial estimate, $M$ in Proposition
5.2, $c_0$ and $C_P$ in Proposition 6.3. These margins depend continuously on the data $\mathcal H$, $\rho_\infty$,
$q_\pm$ and on the order functions, so a choice made at $b_1$ serves for $b$ near $b_1$ with halved margins. So does the
finite covering of the characteristic sets by flow boxes in section 7.1, with the flow-box coordinates of Proposition 5.2
rebuilt at each $b$ from the flow of $\mathsf H_f^b$ through the same transversals, so that $\mathsf H_f^b = \partial_z$
exactly (D186): the flows are continuous in $b$ in $C^\infty$, and the backward entry times into the neighbourhoods of
the radial sets are bounded by (H5), so the same covering serves nearby. The commutants are built from these data and are
bounded in their symbol classes uniformly in $b$ near $b_1$. Compactness of $\mathcal B$ gives finitely many $b_1$. The
index and invertibility statements follow by the arguments of sections 7.3 and 7.6, run with sequences
$(\sigma_j,b_j)\to(\sigma_*,b_*)$ in place of $\sigma_j\to\sigma_*$: the uniform estimates supply the bounds, and $\hat
P^{b_j}(\sigma_j)u_j\to\hat P^{b_*}(\sigma_*)u$ as distributions supplies the limit. This is `../N1STAR-PROOF.md` Lemma
10.59 in the present setting. $\square$

## 9. What this part found against the record and the source

(F1) *A sign slip in the source.* [Hin26c] (9.45) prints the diagonal term of the commuted system as $-2ik\sigma\rho$.
The true term is $+2i\alpha_1\sigma\rho$, and the source's printed commutator, zero unless $\alpha = (k,0,\dots,0)$,
holds only for $\alpha_1 = 0$. With the true sign, Step 2 of his proof of Proposition 9.11 fails. Lemma 4.8 removes the
term through the equation, and Proposition 4.9 (3), which is [Hin26c] (9.44), holds as he states it. Seated in the record
as D184.

(F2) *Two n = 3 numbers in the record.* `../N1STAR-PROOF.md` 10.86 (e) Part (5) carried $C^{\infty,1+\bar S-\epsilon}_b$
and $\rho^{1+S}$. At $n = 4$ they are $\mathcal A^{3/2+\bar S-\epsilon}$ and $\rho^{3/2+S}$ (Theorem 7.2 (5)), as 10.75
(xlviii) has them. Repaired in D184, on the seventy-third verifier's report.

(F3) *The energy estimate's weight.* 10.86 (r) used $e^{-\lambda r}$ for the direct estimate. Proposition 6.3 takes
$e^{\lambda r}$, and also needs a Poincaré inequality for the zeroth-order terms. Repaired in D184.

(F4) *Steps the source leaves implicit, filled here.* (a) At $R_{\mathrm{in}}$ and $R_{\mathrm{out}}$ ([Hin26c]
Propositions 9.10-9.11), $H q\ge c\,q$ holds only near the characteristic set. So $b_R$ is not a smooth square root
without a cut-off to that set. The commutants here carry $\psi_\Sigma = \psi(\varsigma_\Sigma g^2)$, with $\mathsf
Hg = 0$, so the cut-off costs nothing. (b) At the horizon, Lemma 4.1 replaces the source's $\psi_\Sigma$ and $jG_0$ term
by a defining function in $S^*X$. (c) The regularisation and the half-step iteration (Lemmas 3.1-3.2), which the source
omits ("We only recall the symbolic computations and omit their regularization ... and quantization", p. 165), are
written out, with steps of size $\kappa\le\frac14$ so that the effective order never leaves the admissible
range. (d)
The energy estimate near $\partial_\sharp X$ at every order (Proposition 6.4) is proved, where the source cites [Hin25a]
Corollary 9.38.

(F5) *A computation printed with a slip, harmless.* In the proof of [Hin26c] Proposition 9.10 (p. 167),
$H_{\mathrm{Re} G_\sigma}q$ over $\partial X$ is printed as
$2|\eta|^2(\xi + 2\mathrm{Re}\,\sigma) - 2(\xi + \mathrm{Re}\,\sigma)|\eta|^2$, that is $2\sigma_0|\eta|^2$. The value is
$4\sigma_0|\eta|^2$ (section 4.3). Only its sign is used.

(F6) *A formal step in the source.* [Hin26c] (9.39) and (9.50) pair the commutator with $u$ itself. Where the absorbing
term has top decay order ($\sigma_1\mathrm{Re}_hT$ at $R_{\mathrm{in}}$, $-\iota\sum W^*W$ at $R_{\mathrm{out}}$), that
pairing is undefined for $u$ in the a priori space. Lemma 3.1 pairs only Schwartz approximants and passes to the limit in
the other terms (D186, on the seventy-fourth verifier's report).

## Sources

[Hin26c] P. Hintz, *(Non-)Linear waves on asymptotically flat spacetimes. II: trapping, bound states, nonlinear
applications*, arXiv:2606.28008v1. READ: section 9.1-9.2, pp. 157-174 (alphaXiv full text, 2026-10-25); the definitions
and Lemma 5.12 of section 5, pp. 100-105.

[HJS] A. Hassell, Q. Jia, E. Sussman, *Lecture notes on non-elliptic Fredholm theory*, arXiv:2604.18956v1 (2026). READ
(alphaXiv full text, 2026-10-25): (2.1) and Proposition 2.3 (pp. 9-13); Propositions 3.7, 3.11, Remark 3.12, Proposition
3.13 (pp. 19-20); Propositions 4.9-4.10 (pp. 27-29); Definition 7.2, Propositions 7.4-7.5, (7.33)-(7.34), section 7.5
(pp. 48-53); section 10.1-10.3, Proposition 10.1, Definition 10.2 (pp. 77-80); Lemma 12.5 (p. 95). All are stated on
$\mathbb R^n$, or on manifolds with boundary, for every $n$.

No other source is used. Hörmander's extendible and supported spaces are defined and their duality proved in section
6.1. The energy estimate is proved in section 6.2.
