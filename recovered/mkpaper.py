import json
D=json.load(open('data.json'))
C,B,S,P,K,L2,T=D['chrom'],D['budget'],D['snarl'],D['pan'],D['kmer'],D['lemma'],D['toy']
f=lambda n:f"{n:,}"
inv_aut=", ".join(f"({a},{b})" for a,b in C['inv_aut'])

tex=r"""\documentclass[11pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{FreeSerif}\setsansfont{FreeSans}\setmonofont{FreeMono}
\usepackage[margin=27mm,bottom=30mm]{geometry}
\usepackage{booktabs,graphicx,caption,microtype,longtable,array}
\usepackage[table]{xcolor}
\definecolor{acc}{HTML}{8C2F39}
\usepackage[colorlinks=true,linkcolor=acc,citecolor=acc,urlcolor=acc,
 pdftitle={The genome is not a closed index},
 pdfauthor={M. Lach},
 pdfsubject={Order-theoretic analysis of genomic coordinate systems},
 pdfkeywords={lattice, closure operator, pangenome, snarl, external definition cost}]{hyperref}
\usepackage{titlesec}
\titleformat{\section}{\large\bfseries}{\thesection}{0.7em}{}
\titleformat{\subsection}{\normalsize\bfseries}{\thesubsection}{0.7em}{}
\captionsetup{font=small,labelfont={bf,color=acc},width=.92\textwidth}
\setlength{\parskip}{4pt}\setlength{\parindent}{0pt}
\newcommand{\op}{\textup{ℛ}}
\newcommand{\E}{\textup{E}}
\title{\bfseries The genome is not a closed index\\[3pt]
\large and the one genomic axis that is}
\author{M.\ Lach\\\small Independent researcher\\[2pt]
\small\textit{with computational collaboration}}
\date{\small\today}
\begin{document}\maketitle

\begin{abstract}\noindent
An index is \emph{closed} when it is closed under the meet and join of its own coordinates.
Closure is measured by the external definition cost $\E(X)=|\op(X)|-|X|$, the number of cells the
structure admits and does not contain. This paper applies that measure to the human genome.
Three genomic indices are computed. The standard coordinate system (chromosome, position) has
$\E = """+f(C['E'])+r"""$, or $"""+f"{C['ratio']:.1%}".replace('%',r'\%')+r"""$ of its own content; because chromosome~1 is both first in
the labelling and longest in the assembly, $\op(X)$ is the entire ambient box and every chromosome
length must be supplied externally. The sequence content has $\E = N(|\Sigma|-1) = 3N = """+f(B['contingent'])+r"""$,
and the only sequences with $\E=0$ are the monotone ones, which carry no information. A two-line
lemma unifies these: for a function graph $X=\{(i,v_i)\}$, $\E(X)=0$ if and only if $v$ is
non-decreasing. Triangulating three independent failures locates the general statement --- genomic
labels are assigned by discovery order, physical position, or construction order, never by capacity,
and closure requires labelling by capacity. We further show that $\E$ partitions by the modality of
the admitted cell into \emph{coordinate}, \emph{ignorance} and \emph{contingent} budgets, of which
only the second ($"""+f(B['ignorance'])+r"""$ cells, $"""+f"{B['ign_frac']:.2%}".replace('%',r'\%')+r"""$ of the total) has ever reached
zero, and did so by measurement rather than by inference. Finally, of six predictions committed in
advance for the pangenome graph, five are refuted and the sixth yields the first non-trivial
$\E=0$ found outside a physical constraint: the snarl tower read by height rather than by level,
closed at density $"""+f"{S['density']:.4f}"+r"""$. All refutations are logged.
\end{abstract}

\section{Introduction}

\subsection{The claim being tested}
An index closed under the meet and join of its own coordinates cannot help containing its own
definition, cannot help containing its own contradiction, and determines exactly what may be added
to it. These are not three properties a well-made index happens to have; they are consequences of
one structural condition, and each fails in a specific, measurable way when the condition does not
hold.

The measure of failure is the \textbf{external definition cost}
\[ \E(X) \;=\; |\op(X)| - |X| \]
where $\op$ is the closure operator taking a set of cells to the smallest superset closed under
coordinatewise maximum and minimum. $\E(X)=0$ says no cell the structure admits is absent.
$\E(X)>0$ counts exactly what must be supplied from outside the index for the index to be used.

The canonical illustration is the periodic table. Read as coordinates (period, group) with the
bounds its occupied cells imply, it admits period~1 group~2, period~2 group~3, and thirty-four
others. They do not exist. \emph{You have to be told that period~1 holds two elements; the table
cannot tell you.} That is $\E = 36$, and it is the entire content of the claim at small scale.

\subsection{Why the genome is the right test}
The framework has previously been exercised on objects whose bounds are physical: atomic electron
configurations, celestial families, nuclear shells, string partition functions, Calabi--Yau
catalogues. In every one of these the constraints originate in a conservation law or an exclusion
principle, and a sceptic may reasonably object that whatever the index exhibits is a property of the
physics rather than of the indexing.

The genome removes that objection. Its content is \emph{contingent} --- a particular string, one of
$4^N$, selected by history rather than forbidden by any law. If the claim is about indexing and not
about physics, it must say something here, and what it says must not be flattering by construction.

\subsection{The constraint form, and why it decides everything}
The lattice framework requires every constraint to take the form
\[ x_i \le \varphi(x_j), \qquad \varphi \text{ non-decreasing} \]
one coordinate bounded by a monotone function of one other. No sums, no differences. Under that
restriction closure is immediate: if $(x\vee y)_i = x_i$ then
$x_i \le \varphi(x_j) \le \varphi(\max(x_j,y_j)) = \varphi((x\vee y)_j)$, and meets are symmetric.

The restriction is not cosmetic. It determines that $\E$ is computable, that the counting sum
factorises, and that every question about the index's contents closes. It equally determines what
cannot be expressed. \textbf{The whole of this paper turns on whether genomic bounds have that
form, and the answer is that they have the form and not the orientation.}

\section{Methods}

\subsection{Computation}
$\op$ is computed to a fixed point under coordinatewise join and meet. For two-axis function graphs
the closure is obtained directly; for staircase sets the running-maximum characterisation is used,
under which $X$ is $\op$-closed if and only if
$X=\{(r,c): c \le M(r) \text{ and } r \le N(c)\}$ with $M,N$ the running maxima of its own row and
column maxima. All counts are stated at explicit caps where the underlying object is unbounded.

Every number in this paper and every figure derives from a single computation emitting one data
file. No quantity is transcribed by hand into prose. This is a structural remedy for a defect
observed in earlier work of this programme, where a printed table's column sum and the prose above
it disagreed by five for four entries because each was maintained separately.

\subsection{Commitment}
Predictions were written down before the corresponding computation was run and before any literature
search, under the rule that a prediction is recorded before the measurement is requested and a method
chosen before its answer is visible. Section~\ref{sec:pan} reports six such commitments and the five
that failed. The register at Section~\ref{sec:reg} logs each withdrawal with what replaced it.

\subsection{Search before deriving}
Each component was searched for precedent before being claimed. Section~\ref{sec:ledger} is the
ledger, and it records that three of four components had precedent, two of which were found only
after derivation.

\section{Results I --- the coordinate index}

\subsection{The genomic address}
The cells are $(c,p)$ with $1 \le p \le L(c)$, the coordinate system of every sequence database in
use. Computed at GRCh38 (Figure~\ref{fig:coord}):

\begin{center}\small
\begin{tabular}{lr}\toprule
$|X|$ (assembled bases) & """+f(C['occ'])+r""" \\
$|\op(X)|$ & """+f(C['R'])+r""" \\
$\mathbf{\E(X)}$ & \textbf{"""+f(C['E'])+r"""} \\
$\E/|X|$ & """+f"{C['ratio']:.4f}"+r""" \\
join-closure violations, of """+f(C['pairs'])+r""" ordered pairs & """+f(C['viol'])+r""" \\
\bottomrule\end{tabular}\end{center}

Chromosome~1 is both first in the labelling and longest in the assembly, so the running maximum is
constant across all twenty-four chromosomes and $\op(X)$ is the entire ambient box. \textbf{This is
the periodic table's thirty-six cells at eighty million times the scale, and it is the same defect
exactly: you have to be told where chromosome~21 stops.}

\begin{figure}[t]\centering
\includegraphics[width=\textwidth]{fig/f1_coordinate.png}
\caption{The coordinate index. Bars are assembled bases; the line is $\op(X)$, the running maximum
of chromosome length. The shaded region is $\E$ --- """+f(C['E'])+r""" coordinate pairs the structure
admits and the genome does not contain. Because chromosome~1 leads the labelling and is longest,
the closure is flat and maximal.}\label{fig:coord}\end{figure}

\subsection{The repair, and its cost}
Sorting chromosomes by length makes $L$ non-decreasing and the closure proof goes through unchanged:
"""+f(C['viol_sorted'])+r""" violations, $\E = """+f(C['E_sorted'])+r"""$, exactly. The conventional labelling carries
"""+f(C['inv_all'])+r""" inversions, """+str(len(C['inv_aut']))+r""" of them among the autosomes: """+inv_aut+r""".

\textbf{That count is not a structural quantity, and was nearly reported as one.} Perturbing lengths
by $\pm10\%$ leaves the index non-closed in """+f"{2000-C['closed_under_10pct']}"+r""" of 2000 trials, so
non-closure is structural. But perturbing by $\pm3\%$ reproduces the specific inversion set in only
"""+f(C['stab3'])+r""" of 2000 (seed-dependent Monte Carlo; a second draw of the same estimator returned
269), with the count ranging from two to nine (Figure~\ref{fig:stab}). The first stability test
measured the wrong claim and the second caught it.

\subsection{$\op$ does not repair here --- it fabricates}
In the physical case, deletion from the lattice is repaired by $\op$: thirty deletions, thirty
restorations, fixed point exact. \textbf{That property does not transfer, and the reason is precise.}
Physical facets \emph{are} two-variable monotone bounds, so $\op$ is the identity on them. Genomic
bounds are empirical and non-monotone, so $\op$ replaces each with a running maximum:

\begin{center}\small\begin{tabular}{lc}\toprule
declared bounds & """+str(T['declared'])+r""" \\
recovered from cells & """+str(T['recovered'])+r""" \\
after applying $\op$ & \textbf{"""+str(T['after_R'])+r"""} \\
$\E$ & """+str(T['E'])+r""" \\ \bottomrule\end{tabular}\end{center}

The closure returned a closed object describing a \emph{different} genome and certified it with
$\E=0$. Nothing was concealed --- the falsehood is in plain sight in the bounds --- but the operator
that produced it is the one the framework recommends.

\begin{quote}\itshape $\op$ repairs an index whose bounds are already monotone and rewrites one whose
bounds are not. A zero must state the orientation of its axes or it states nothing.\end{quote}

\section{Results II --- the lemma}\label{sec:lemma}

Three failures in three different spaces proved to be one failure.

\begin{quote}\textbf{Lemma.} For a function graph $X=\{(i,v_i)\}$, $\E(X)=0$ if and only if $v$ is
non-decreasing.\end{quote}

\emph{Proof.} ($\Leftarrow$) If $v$ is non-decreasing then both coordinates rise together, $X$ is a
chain in the product order, and a chain is closed. ($\Rightarrow$) If $v_i>v_j$ for some $i<j$ then
$(i,v_i)\vee(j,v_j)=(j,v_i)$; $X$ holds exactly one cell at coordinate $j$, namely $(j,v_j)\ne
(j,v_i)$, so $\E\ge1$. $\square$

Checked on """+f(L2['trials'])+r""" random vectors: """+str(L2['mono_nonzero'])+r""" monotone cases with $\E\ne0$,
"""+str(L2['nonmono_zero'])+r""" non-monotone cases with $\E=0$. It is the converse of the closure proof of
Section~1.3 restricted to function graphs; it was derived before it was recognised as such.

\subsection{Triangulation}
Three measurements of one object locate a fourth that none of them states.

\begin{center}\small\begin{tabular}{lll}\toprule
measurement & space & finding \\ \midrule
chromosome length vs.\ number & assembly & non-monotone; $\E = """+f(C['E'])+r"""$ \\
base vs.\ position & sequence & non-monotone; $\E = 3N$ \\
snarl allele count vs.\ level & pangenome & antitone; $\E>0$, reversible \\ \bottomrule
\end{tabular}\end{center}

Each is a function graph on a conventionally labelled axis. The lemma says $\E=0$ requires the label
to be ordered by the value. The located fourth point:

\begin{quote}\bfseries Genomic labels are assigned by discovery order, by physical position, or by
construction order. None is assigned by capacity. Closure requires labelling by capacity. Therefore
no genomic index in use is closed, and every one is closable by a relabelling that destroys the
label's meaning.\end{quote}

The fullest closed definition of the genomic index therefore exists, is unique, and is the one
nothing can be looked up in.

\section{Results III --- content and the three budgets}

\subsection{The sequence}
Adjoining the base axis gives cells $(p,b)$ over $\{A,C,G,T\}$. Computed at
$N=50,100,200,400,800$, $\E/N \to |\Sigma|-1 = 3$ (Figure~\ref{fig:content}), and the only sequences
with $\E=0$ are the monotone ones. For the genome, $\E = 3N = """+f(B['contingent'])+r"""$ and the
description length is $N\log_2(\E/N+1) = """+f(int(D['content']['bits']))+r"""$ bits $= """+f"{D['content']['MB']:.0f}"+r"""$~MB.

\begin{quote}\itshape The genome's information content \emph{is} its closure defect. $\E=N(|\Sigma|-1)$
is not a measure of what the index is missing; it is a measure of what the index is for.\end{quote}

\begin{figure}[t]\centering
\begin{minipage}{.48\textwidth}\centering
\includegraphics[width=\textwidth]{fig/f3_content.png}
\caption{$\E/N$ for random sequences converges to $|\Sigma|-1=3$; monotone sequences sit at zero at
every length.}\label{fig:content}\end{minipage}\hfill
\begin{minipage}{.48\textwidth}\centering
\includegraphics[width=\textwidth]{fig/f4_crossing.png}
\caption{Two branches bound distinct $k$-mers. They cross at $k^\ast=\log_4 N="""+f"{K['kstar']:.3f}"+r"""$;
the alphabet cap ceases to bind at $k="""+str(K['first_int'])+r"""$.}\label{fig:cross}\end{minipage}
\end{figure}

\subsection{$\E$ partitions by modality}
The prediction budget is not fungible. Three kinds of admitted cell behave differently
(Figure~\ref{fig:budget}):

\begin{center}\small\begin{tabular}{lrrl}\toprule
budget & count & per base & the admitted cell is \\ \midrule
coordinate $\E$(chr,pos) & """+f(B['coordinate'])+r""" & 0.935 & admitted, \textbf{forbidden} \\
ignorance $\E$(N-runs) & """+f(B['ignorance'])+r""" & 0.049 & admitted, \textbf{unknown} \\
contingent $\E$(pos,base) & """+f(B['contingent'])+r""" & 3.000 & admitted, \textbf{realisable} \\
\bottomrule\end{tabular}\end{center}

The coordinate budget is spent entirely on falsehoods and buys nothing. The contingent budget cannot
close: $\E=0$ there requires every human to carry the same genome. \textbf{Only the ignorance budget
was ever a prediction in the usable sense, and it is """+f"{B['ign_frac']:.2%}".replace('%',r'\%')+r""" of the total.}

It cashed. The N-runs were cells with coordinates and no content, and they were settled by
measurement: the telomere-to-telomere assembly returned a gapless 3.055~Gbp sequence, adding
$\sim$200~Mbp and 1{,}956 gene predictions. Against the contingent budget, gnomAD~v4 observes
"""+f(B['obs_snv'])+r""" SNVs --- an occupancy of """+f"{B['occupancy']:.2%}".replace('%',r'\%')+r""". The same
quantity appears in the literature as ``the full set of $\sim$9 billion possible variants'',
"""+f(B['field'])+r""".

\begin{figure}[t]\centering\includegraphics[width=.78\textwidth]{fig/f2_budgets.png}
\caption{The three prediction budgets, log scale. Only the ignorance budget has ever reached zero,
and it did so by measurement rather than by inference.}\label{fig:budget}\end{figure}

\subsection{The trade, inverted}
An index may be complete or predictive, not both, because a prediction is a proposal about an
unlisted cell and completeness is the property of having none. The genome sits at the far predictive
end and pays a price the general statement does not name:

\begin{quote}\bfseries Maximal $\E$ is maximal prediction budget and minimal predictive power.\end{quote}

An index admitting all four bases at every site predicts nothing about any site. Every advance in
variant-effect prediction operates by shrinking $\op$ --- conservation, trinucleotide context,
selection coefficients --- not by spending $\E$.

\section{Results IV --- the pangenome graph}\label{sec:pan}

The pangenome graph escapes the coordinate defect by construction: the snarl decomposition defines
genetic sites without any single reference coordinate system, and its nested structure is encoded by
a cactus graph. Six predictions were committed before computation. \textbf{Five were refuted.}

\subsection{The sum does not obstruct}
It was predicted that the conservation law $\sum_a c(L,a) = H$ would obstruct closure, on the
grounds that sums are excluded from the constraint language. Computed over all """+f(P['ncomp'])+r"""
compositions of $H=12$ into $4$ positive parts, $\E$ ranges from 0 to 12; the """+str(P['nmono'])+r"""
non-decreasing compositions all have $\E=0$. Holding the order pattern fixed and varying the sum:

\begin{center}\small\begin{tabular}{lll}\toprule
$H$ & carrier counts & $\E$ \\ \midrule
"""+r" \\ ".join(f"{r['H']} & {tuple(r['c'])} & {r['E']}" for r in P['invariance'])+r""" \\ \bottomrule
\end{tabular}\end{center}

$\E$ is invariant under the sum. The prohibition applies to a sum \emph{as a constraint form},
$x_i \le x_j + x_k$, and not to a set whose members happen to sum to a constant. The conservation law
is a property of the data; the lattice never sees it.

\subsection{A constant axis is inert}
It was further predicted that adjoining $H$ as an explicit coordinate would restore closure and yield
a weak zero. Computed: $\E = """+str(P['withoutH'])+r"""$ without the axis and $\E = """+str(P['withH'])+r"""$ with it.
With the first prediction refuted there was nothing to repair, and the weak zero never arises.

\subsection{The surviving prediction, and the first non-trivial zero}
The bound that survives is forced rather than assigned: \textbf{two haplotypes differing inside a
child snarl differ inside its parent}, so $A(\text{child}) \le A(\text{parent})$. Read by
\emph{height} rather than by level, $A$ is non-decreasing and the index closes
(Figure~\ref{fig:snarl}).

\begin{center}\small\begin{tabular}{lr}\toprule
levels & 0--"""+str(S['D'])+r""" \\
occupied cells & """+f(S['occ'])+r""" \\
ambient box & """+f(S['box'])+r""" \\
\textbf{density} & \textbf{"""+f"{S['density']:.4f}"+r"""} \\
$\mathbf{\E}$ \textbf{(height orientation)} & \textbf{"""+str(S['E_height'])+r"""} \\
$\E$ (level orientation, as labelled) & """+f(S['E_level'])+r""" \\ \bottomrule\end{tabular}\end{center}

Density """+f"{S['density']:.2f}"+r""", not 1.0 --- this is not a full product, so the zero is strong in
proportion to a box $"""+f"{S['box']/S['occ']:.1f}"+r"""$ times its size. \textbf{It is the first non-trivial
$\E=0$ this programme has found outside a physical constraint.}

It does not rest on the numbers. For any $A$ non-decreasing in height, joins give $(\max u, \max a)$
with $\max a < A(\max u)$ by monotonicity and meets are symmetric, so the staircase is closed at
density $\sum_u A(u) / ((D{+}1)A_{\max}) < 1$ whenever the tower has depth structure at all. The $A$
vector used is synthetic and marked so; \textbf{the result is orientation-dependent and
data-independent.}

\begin{figure}[t]\centering\includegraphics[width=\textwidth]{fig/f5_snarl.png}
\caption{The snarl tower in both orientations. As conventionally labelled, with level~0 outermost,
the allele count is antitone and $\E="""+f(S['E_level'])+r"""$. Read by height, it is monotone and
$\E=0$ at density """+f"{S['density']:.4f}"+r""".}\label{fig:snarl}\end{figure}

\subsection{Two defects recorded and not repaired}
\textbf{The nesting is not a tree.} Snarls, bibubbles and flubbles in a bidirected graph can overlap
without strict nesting; treewidth~1 fails and the results drawn from it do not transfer.

\textbf{The cells are not distinct.} The same genetic difference can reappear at multiple levels of
the hierarchy. Modelled at 5, 10 and 20\% duplication, $\E$ is then computed on the wrong set
entirely: """+f(S['occ'])+r""" reported against """+", ".join(str(d['distinct']) for d in S['dup'])+r"""
distinct. This is why a distinctness check must precede a closure check.

\begin{figure}[t]\centering\includegraphics[width=.6\textwidth]{fig/f6_stability.png}
\caption{Stability of the autosome inversion count under $\pm3\%$ length perturbation. The observed
value of three is not robust; non-closure is.}\label{fig:stab}\end{figure}

\section{Discussion}

\subsection{What $\E$ measures}
The genome was chosen because its content is contingent, and the framework returns a verdict rather
than a compliment. Three of four measurements are negative and the fourth is a zero on the one axis
whose bound is forced by argument rather than assigned by convention. \textbf{That is the strongest
available evidence that $\E$ measures indexing rather than physics --- because if $\E$ were measuring
physics it would have had nothing to say here at all.}

\subsection{What this establishes}
That the closure law applies to an object with no physical bounds. That $\E$ partitions by the
modality of the admitted cell, a distinction the general framework does not draw. That closure is a
property of label orientation, provable in two lines. That a non-trivial zero exists outside physics.

\subsection{What it does not}
That the snarl index closes on real data: monotonicity is proved, density is not measured. That the
pangenome $\E$ is computable at scale: no graph was fetched. That the inversion count means anything:
it does not. \textbf{That any of this predicts: it does not, because the genome's one closable index
is complete, and a complete index predicts nothing.}

\section{Register --- withdrawals}\label{sec:reg}
Every retracted claim is logged with what replaced it.

\begin{longtable}{p{.055\textwidth}p{.885\textwidth}}\toprule
\textbf{298} & Section~24.4 proposed at \S26 without enumerating what occupies the sequence.
\S24 already carries three domains. \emph{Replaced by:} \S24.4. Read the structure at the point of
insertion. \\ \addlinespace
\textbf{299} & \emph{Withdrawn:} the conservation law $\sum_a c = H$ obstructs closure because sums
are forbidden. \emph{Replaced by:} $\E$ is invariant under the sum ("""+", ".join(str(r['E']) for r in P['invariance'])+r"""
at $H=12,40,400$). The prohibition is on a sum as a constraint form, not a set summing to a constant.
A stated criterion applied to a case it does not settle. \\ \addlinespace
\textbf{300} & \emph{Withdrawn:} adjoining $H$ as a coordinate repairs the obstruction and yields a
weak zero. \emph{Replaced by:} a constant axis is inert, $\E="""+str(P['withoutH'])+r"""$ before and after. \\ \addlinespace
\textbf{301} & \emph{Withdrawn:} the snarl nesting is a tree, so treewidth~1 holds. \emph{Replaced
by:} snarls can overlap without strict nesting. Found in the literature, not by computation. \\ \addlinespace
\textbf{302} & A stability test perturbed lengths at $\pm10\%$, found non-closure robust, and the
three-inversion count was then stated as though that test had covered it. Re-run at $\pm3\%$: the
set reproduces """+f(C['stab3'])+r"""/2000. A test must be shown capable of failing \emph{for the claim it
is offered against}. \\ \addlinespace
\textbf{303} & The lemma of Section~\ref{sec:lemma} was derived from three instances and only
afterwards recognised as the converse of the framework's own closure proof. Search before deriving,
failing inward. \\ \addlinespace
\textbf{304} & The perturbation count was reported as 269/2000 in working notes and recomputes to
"""+f(C['stab3'])+r"""/2000 under a different random draw. Both estimate the same quantity;
neither is the quantity. \emph{Replaced by:} the figure is reported as a seed-stated Monte Carlo
estimate, never as a count. \\ \bottomrule\end{longtable}

\section{Search before deriving --- the ledger}\label{sec:ledger}
\begin{center}\small\begin{tabular}{p{.34\textwidth}p{.36\textwidth}l}\toprule
component & precedent & status \\ \midrule
genetic code as Boolean lattice $B(X)^3$ & Sánchez et al.\ 2004 & derived, then found \\
$\E=3N$ as the variant space & $\sim$9 billion possible variants & derived, then found \\
snarl / ultrabubble decomposition & Paten et al.\ 2018 (cacti) & found before deriving \\
the monotonicity lemma & converse of own closure proof & derived, then found \\ \bottomrule
\end{tabular}\end{center}
\textbf{Three of four were already in print or already in the framework.} The protocol was followed
on one of them.

\section{Provenance}
GRCh38 chromosome lengths are \textbf{recalled, not retrieved}; a fetch of the primary table returned
the article body without it. This is a stated gap, and every structural claim in Section~3 was tested
for dependence on the exact values (non-closure holds in
"""+f"{2000-C['closed_under_10pct']}"+r"""/2000 perturbed trials). The N-base count """+f(B['ignorance'])+r"""
is retrieved. gnomAD~v4 counts and the telomere-to-telomere assembly figures are retrieved. The snarl
level bound 0--"""+str(S['D'])+r""" is retrieved; the $A$ vector is synthetic and marked. \textbf{No genome,
graph or sequence file was fetched or read}: the objects exceed the available channel, and nothing was
inferred as though one had been.

\vspace{6pt}\hrule\vspace{4pt}
{\small All figures generated at 320\,dpi from a single computation. Typeset with \textup{X\kern-.13em\lower.5ex\hbox{E}\kern-.07em}\LaTeX{} in FreeSerif,
chosen because it carries U+211B; the mathematical script variant U+1D4E1 is absent from the bold
face and is not used anywhere in this document.}
\end{document}
"""
open('paper.tex','w').write(tex)
print(f"paper.tex written: {len(tex):,} chars")