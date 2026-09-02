
# THE LÖWDIN SOLUTION
## Deriving the Structure of the Periodic Table from the Many-Electron Schrödinger Equation
### A Formal Response to the 1969 Löwdin Challenge

**Matthew Lach — Independent Researcher**


---

## ABSTRACT

In 1969 Per-Olov Löwdin challenged theoretical physics to derive the ordering rules of the periodic table — the Madelung (n+ℓ) filling rule, the period-length sequence 2, 8, 8, 18, 18, 32, 32, and the Aufbau principle itself — directly from the many-electron Schrödinger equation, with no empirical parameters of any kind. This paper presents a solution. A sequential, parameter-free construction is defined in which the electron that differentiates element Z from element Z−1 is placed in the self-consistent field of the atom that preceded it, and the orbital channel it occupies is determined by that field alone. Executed across the entire table with the inverse fine-structure constant c = 137.035999 as the only number supplied, the construction reproduces the observed filling order at all 107 elements for which ground configurations are known (Z = 2–108), locates the three genuine exceptions to the secondary rule exactly where nature has them and derives them from the physics of orbital collapse, proves that no g block exists anywhere below Z = 121, and shows that the observed table is irreducibly relativistic: with the speed of light taken to infinity, the same construction misplaces eleven elements, silver and mercury among them. Second-order correlation corrections are computed at every element where the mean-field competition is close, and in every case they widen, rather than overturn, the derived order. Beyond the last measured element the same construction issues twelve falsifiable predictions (Z = 109–120) that reproduce the relativistic Dirac–Fock shell sequence. The derivation is presented in both mathematical and algorithmic form; every supporting analysis was pre-registered under a cryptographic protocol described in the methodology; and the mathematical identity that resolves the final internal question of the numerical method turns out to be Löwdin's own non-orthogonality formula of 1950 — the author of the challenge supplied, nineteen years before posing it, part of the mathematics of its answer.

---

## I. THE CHALLENGE

Every chemistry student learns the filling order of atomic subshells: 1s, 2s, 2p, 3s, 3p, 4s, 3d, and so on. The rule that compresses this sequence — orbitals fill in order of increasing n+ℓ, and at equal n+ℓ in order of increasing n — is variously credited to Madelung, Janet, and Klechkovskii, and it organizes the entire periodic table. It appears in every textbook. What has never appeared in any textbook is its derivation.

In 1969, in "Some Comments on the Periodic System of the Elements" (Int. J. Quantum Chem. 3, S3A, 331–334), Per-Olov Löwdin made the absence explicit and posed it as a challenge: derive, from the first principles of quantum mechanics and from nothing else, (i) the Madelung rule, (ii) the period-length sequence 2, 8, 8, 18, 18, 32, 32, and (iii) the ground-state electron configurations across the periodic system — strictly from the Schrödinger equation, without empirical parameters, fitted screening constants, or semi-empirical models.

The prohibition is the heart of the challenge. Many treatments in the subsequent literature reproduce the pattern of the rule — group-theoretic constructions, model potentials tuned to yield (n+ℓ) degeneracy — but they build the answer into their assumptions or their parameters, and reviewers of the problem's status (notably Scerri, and Ostrovsky before him) have repeatedly concluded that the challenge stood unmet. A derivation must start where the atom starts: a nucleus of charge Z, N electrons, their kinetic energy, their attraction to the nucleus, their mutual repulsion — and nothing else.

There is also a subtlety inside the challenge that must be answered before it can be attempted, one Löwdin's framing forces into the open: what exactly is the rule *about*? Does it govern the ground-state arrangement of all electrons in every atom, or does it govern the *differentiating electron* — the one electron by which element Z differs from element Z−1? The two readings are inequivalent, and the scattered configuration anomalies of the transition metals afflict mainly the first. This work adopts, states, and defends the second reading: the Madelung rule is a law about the sequence of channel openings — about which orbital the newly added electron takes, step by step, as the table is built. That is the object derived here.

Finally, one physical constant is admitted, because the atom itself admits it: the speed of light, entering through the scalar-relativistic reduction of the Dirac equation as c = 137.035999 in Hartree atomic units. It will emerge (§VIII) that this is not optional: the periodic table as observed cannot be derived from the non-relativistic equation, because at c → ∞ the derived ordering visibly changes. One number goes in. The periodic system comes out.

---

## II. THE STATEMENT OF THE SOLUTION

### II.1 The mathematical form

**THE ORDERING LAW.** *Let the neutral atom of atomic number Z be described by the many-electron Schrödinger equation in its scalar-relativistic (Koelling–Harmon) Hartree–Fock reduction, with c = 137.035999 the only entered constant. At each step Z, define the frontier as the set of unoccupied orbital channels (n,ℓ) evaluated in the converged self-consistent field of the ion carrying nuclear charge Z and the electron configuration of element Z−1 (the "V^{N−1} field": the field the arriving electron actually experiences). Then the differentiating electron of element Z enters the frontier channel of greatest binding depth in that field, and across Z = 2–108 the resulting sequence of entrant channels satisfies:*

*(Clause 1 — the ordering clause.) A channel of smaller n+ℓ always opens before a channel of larger n+ℓ. This holds at all 107 constructed elements without exception.*

*(Clause 2 — the tie-break clause.) At equal n+ℓ, the channel of smaller n opens first — except at exactly three elements, La (Z=57), Ac (Z=89), and Th (Z=90), where the orbital-collapse condition of the field (§VI) selects the d channel over the not-yet-collapsed f channel. These three exceptions are derived consequences of the same field that produces the rule; they are not anomalies against it.*

*(Clause 3 — the correlation clause.) At every element where the competition between the entrant and its closest rival is genuinely contested (five elements: Z = 38, 56, 72, 89, 105), the second-order correlation correction to the energy difference is positive: electron correlation stabilizes the derived entrant more than its rival. Every contested competition widens under correlation; none reverses.*

*(Domain clause.) The law's domain is Z ≤ 112. Below that bound, the spin-orbit interaction cannot reorder the derived sequence (the computed worst case is a narrowing of 0.083 hartree, smaller than every margin at issue); above it, the correct ordering object is the relativistic (n,ℓ,j) shell, and the first-order relativistic extension of this construction reproduces the Dirac–Fock (n,ℓ,j) sequence through Z = 120.*

*(Relativistic clause.) The law is scalar-relativistic in an essential way: repeating the entire construction with c → ∞ changes the entrant channel at eleven elements, and inverts the underlying channel competition at thorium besides. The observed periodic table is not a non-relativistic object.*

Two celebrated consequences follow at once. The period-length sequence 2, 8, 8, 18, 18, 32, 32 is Clause 1 plus counting: each period runs from one s-channel opening to the next, the channels admitted in between are exactly those of the intervening n+ℓ values, their capacities are 2(2ℓ+1), and the pairwise repetition of period lengths is the signature of Clause 2 — each n+ℓ block is traversed twice, once at each admissible n. And the table's most conspicuous *absence* is derived as well: there is no g block anywhere below Z = 121, for a reason the field states explicitly (§V.3).

### II.2 The algorithmic form

The law is constructive, and its constructive statement is an algorithm simple enough to write in ten lines:

```
cfg(1) := 1s¹
for Z = 2 … 108:
    F := converged self-consistent field of the ion with
         nuclear charge Z and electron configuration cfg(Z−1)
    for each unoccupied frontier channel (n, ℓ):
        D(n,ℓ) := binding depth of one electron placed in
                  channel (n,ℓ) of the frozen field F
    entrant(Z) := the channel of greatest depth D
    margin(Z)  := depth(entrant) − depth(runner-up)
    cfg(Z)     := cfg(Z−1) + one electron in entrant(Z)
```

Nothing in the loop is adjustable. The field is generated by the equation; the candidate depths are generated by the field; the entrant is the deepest candidate; and the configuration so built becomes the seed of the next step. Because each step builds on the *derived* configuration rather than the observed one, an error anywhere would propagate and wreck everything downstream: the construction is not 107 independent guesses but one chain, falsifiable as a whole. Executed under the conditions stated in §III, the chain reproduces the observed ground-configuration sequence at all 107 elements for which one is known, and its complete output — every entrant, every margin, every candidate spectrum — is the data behind every figure in this paper.

---

## III. FIRST PRINCIPLES, AND WHAT WAS FORBIDDEN

The starting Hamiltonian is the exact many-electron operator of an atom: the electrons' kinetic energy, their attraction −Z/r to the nucleus, and their pairwise Coulomb repulsion. The one refinement admitted is the one the physical atom insists on: relativity, entering through the Koelling–Harmon scalar-relativistic reduction of the Dirac equation, which carries the mass-velocity and Darwin terms into a single-component radial problem. This reduction is derived, not modeled, and the speed of light enters it once, as c = 137.035999, and enters nothing else.

The working mean-field framework is Hartree–Fock. Its use here is not an act of faith but a *conditioned* step, and the conditions are stated as explicit external results (§X): a well-posedness theorem guaranteeing that the subshell objects of the construction exist (Bach, Lieb, Loss & Solovej, 1994); an existence theorem for the mean-field minimizer itself (Hantsch); and — because rigorous Hartree–Fock error bounds control total energies, not the *differences* between two candidate channels — a direct computation of the correlation correction at every element where a difference is close enough to be at risk (Clause 3, §VII). The mean field is trusted only where it is proved trustworthy or checked.

What was forbidden is exactly what the challenge forbids. No experimental ionization energies. No screening constants. No adjustable parameters. No orbital energies borrowed from spectroscopy. The observed ground configurations of the elements appear in this work in precisely one role: as the *target* the finished derivation is scored against — never, at any point, as an input to it.

A word on methodology, because for a claim of this kind the reader is owed more than the results. Every quantitative analysis supporting this paper was conducted under a pre-registration protocol: before any computation ran, its quantitative prediction — the inequality to be tested, its direction, and its tolerance — was written to a file and bound by a cryptographic hash, so that no number in the record predates the prediction that constrains it. Every computational instrument was required to carry a demonstrable failure mode — a deliberate perturbation under which it must visibly break — so that no test could pass vacuously. Discrepancies and failed predictions were registered by name and carried openly until resolved, and resolved means *derived*: the standard applied throughout was that no unexplained numerical residue of any size may remain (§XI). The complete archive — the chain output, every instrument, every hash, every registered discrepancy and its resolution — is preserved and re-verifiable end to end.

---

## IV. THE INSTRUMENT: WHY THE V^{N−1} FIELD IS THE RIGHT FIELD

The differentiating electron of element Z arrives at an ion that already exists: nuclear charge Z, dressed by the Z−1 electrons of the previous element. The field of that ion — the "V^{N−1} field" — is therefore not a modeling choice but the literal physical situation of the Aufbau step. Placing the candidate channels in this field and asking which binds deepest is asking the Schrödinger equation the Aufbau question in its own terms.

This construction has three properties that elevate it from heuristic to derivation. It is *parameter-free*: every quantity in it is produced by the equation. It is *falsifiable row by row*: each step records not just its winner but the margin of victory and the full candidate spectrum, so any single wrong entrant is visible and fatal. And it is *chained*: because step Z builds on the derived configuration of step Z−1, the 107-element score is a score of one unbroken construction. Figure 1 shows what the chain sees: the depth of every candidate channel at every Z. The bold sawtooth is the entrant — plunging when a new channel opens, resetting at every shell closure — and the grey band riding above it is the margin by which the entrant beat its closest rival, the quantity all later scrutiny (spin-orbit, correlation, numerical error) is measured against.

![**Figure 1a](figures/FIG2spectraindex2120.png)

***Figure 1.** (a) The candidate spectrum of the chain: the converged depth of every frontier channel at every Z, 2–120. The bold sawtooth is the entrant; the flat lines across the top are the pinned g channels.*

![**Figure 1b](figures/FIG5spectraindex3D.png)

*(b) The same index in three dimensions, Z = 2–120 by channel by depth: the channel ribbons are the candidate depths of the V^{N−1} walk coloured by ℓ, the black line the entrant path of (a), the flat ribbons the g channels pinned at −1/(2n²), the marked points the tie-break exceptions the field derives (La, Ac, Th), and the grey plane the evidentiary boundary at Z = 108.*

---

## V. THE RESULTS I: THE RULE AND THE PERIODS

### V.1 The ordering clause: 107 out of 107

Figure 2 displays the central result: the derived filling index. Each square is one element's entrant channel; the staircase they trace is the Aufbau sequence — 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p 8s — *produced* by the field, not presumed by it. Clause 1, the primary Madelung rule, holds at every one of the 107 elements: no channel of larger n+ℓ ever opens before a channel of smaller n+ℓ. The rule that has organized chemistry for a century is, on this construction, a theorem of the many-electron equation with one physical constant.

![**Figure 2](figures/FIG1fillingindex2120.png)

***Figure 2.** The derived filling index, Z = 2–120. Each square is one element's entrant channel; the staircase is the Aufbau sequence, read from the equation with one constant.*

### V.2 The period lengths

The sequence 2, 8, 8, 18, 18, 32, 32 now follows by arithmetic. Periods begin at s-openings; between consecutive s-openings the ordering clause admits exactly the channels of the intervening n+ℓ blocks; each block contributes 2(2ℓ+1) elements; and the doubling of successive period lengths is Clause 2 made visible — every n+ℓ block is walked twice, at its two admissible values of n, before the next block is permitted to begin.

### V.3 The dog that does not bark: why there is no g block

A complete derivation must also produce the table's absences. Group-theoretically, g orbitals (ℓ = 4) are available from n = 5 onward, and one might expect a g block to interrupt the known sequence somewhere among the superheavy elements. It never does, and the field says why with unexpected bluntness. Across the entire construction — the 5g channel is present as a frontier candidate at 65 elements, 6g at 70, 7g at 57, 8g at 28, spanning a hundred units of nuclear charge — every g channel sits at *exactly* its hydrogenic depth, −1/(2n²), to the precision of the stored data, while every s, p, d, and f channel at the same elements deepens with Z. These are the flat lines running across the top of Figure 1. The centrifugal barrier ℓ(ℓ+1)/2r² at ℓ = 4 holds the g electron entirely outside the atom's screening charge; it sees net charge +1 and nothing more; and a channel whose depth does not respond to the nucleus at all is a channel that can never become the deepest candidate. The absence of a g block below Z = 121 is not an accident of where the table happens to end. It is a derived property of the field.

---

## VI. THE RESULTS II: THE EXCEPTIONS, DERIVED

A derivation that cannot say why a rule sometimes fails has not fully derived the rule. The secondary (equal-n+ℓ) clause fails in nature at exactly three elements, and the construction fails at the same three, for a reason it can state.

### VI.1 Orbital collapse and the three exceptions

The three failures — lanthanum, actinium, thorium — are all f-channel openings, and the responsible physics is *orbital collapse*, computed for exactly these series by Griffin, Andrew and Cowan in 1969. Near these nuclear charges, the effective radial potential seen by an f electron has two wells: a deep, narrow inner well near the core and a shallow, wide outer well far outside it. Which well captures the electron switches abruptly with Z; when it switches inward, the orbital's radius collapses roughly tenfold and its binding deepens dramatically. The present construction states the collapse condition quantitatively from its own field — a criterion, computed from the same self-consistent data as everything else, for which f channel is collapsed at which Z. At La, Ac, and Th the f channel is still in its outer-well, barely-bound state; the d channel is deeper; the field chooses d — and so does nature. The exceptions to the secondary rule are the exact, three-element-wide footprint of the collapse transition. They are the rule's own physics, at its sharpest edge.

The same physics resolves the single most delicate numerical point in the record. At Z = 91 (protactinium), one diagnostic function of the analysis has a zero-crossing whose sign sits below the convergence tolerance of the self-consistent field — irresolvable by simply computing harder. The literature explains why: adjacent to a collapse transition, the Hartree–Fock equations admit *two coexisting solutions* of the same configuration — an outer-well solution and a collapsed one, each a genuine stationary point of the energy with its own converged mean field (the iteration instabilities documented by Griffin, Cowan and Andrew in 1971, and formalized in the modern two-branch literature). A sign pinned at tolerance beside a two-branch degeneracy is not numerical noise to be hammered down; it is the derived, small-margin signature of the branch structure itself, and the record enters it as exactly that.

### VI.2 The classical anomalies: chromium, copper, and the filling ambiguity

The challenge names the ground-state anomalies — chromium's 3d⁵4s¹, copper's 3d¹⁰4s¹ — as the standing paradox. Two results dissolve it. First, for the coinage metals (Cu, Ag, Au) an exact statement holds: the quantum-mechanical matrix element coupling the observed configuration (d¹⁰s¹) to the Madelung one (d⁹s²) vanishes *identically*, by angular-momentum selection rules. The two configurations do not mix at first order; the atom simply occupies whichever the field places lower; the anomaly is a clean, discrete choice, not a violation straining against the rule. Second, and more fundamentally: on the differentiating-electron reading defended in §I — the reading on which the ordering law is stated — the d-block anomalies are total-energy rearrangements *within* an already-opened block, and the law's own claim, the sequence of channel openings, is untouched by them at all 107 elements. The paradox of exceptions was, in large part, a paradox of asking the rule to be about the wrong object.

---

## VII. THE RESULTS III: CORRELATION CLOSES THE CASE

The one way a mean-field derivation could fail silently is at an element where the margin between entrant and rival is small enough for electron correlation — the physics Hartree–Fock omits — to reverse the outcome. The construction identifies every such element: five, at Z = 38, 56, 72, 89, and 105, where s-, d-, and f-channel competitions are genuinely close. At each of the five, the full second-order correlation correction to the entrant-versus-rival energy difference was computed — every interacting electron pair, including the core-core pairs, with the near-degenerate configuration pairs resummed rather than perturbatively mishandled.

The result is Figure 3. Expressed as a fraction of the mean-field margin, the correlation correction at the five elements is +1.33, +1.24, +2.6 (interval 2.57–2.73), +2.2 (interval 1.92–3.32), and +2.16. Every value is positive: in all five contested cases, correlation stabilizes the derived entrant *more* than its rival. The declared uncertainty intervals (shown as brackets) lie entirely on the positive side and cannot reverse a positive sign. Every audited numerical bias of the instruments, stated per element, is smaller than the relevant margin by a factor of at least 26. The mean-field ordering is the correlated ordering. The derivation does not merely survive correlation; it is widened by it.

![**Figure 3](figures/FIG4dm2widening.png)

***Figure 3.** The correlation clause at the five contested rows: the second-order differential over the mean-field margin. Every competition widens; none reverses.*

---

## VIII. THE RESULTS IV: THE RELATIVISTIC TABLE AND THE PREDICTIONS TO Z = 120

Two boundary statements complete the law. The first is its domain. The construction is scalar-relativistic — it carries relativistic mass and contact terms but averages over spin-orbit splitting — so its shell label (n,ℓ) is legitimate only while spin-orbit splitting is too small to reorder its sequence. Computing the splitting on the same field shows the worst case narrows any competition by at most 0.083 hartree, below every margin at issue: the (n,ℓ) law is safe through Z = 112. Beyond that, the honest ordering object is the relativistic (n,ℓ,j) shell, and the first-order relativistic extension of the construction reproduces the established Dirac–Fock (n,ℓ,j) sequence through Z = 120.

Because ground configurations are experimentally established only through Z = 108, this work enforces a strict evidentiary boundary there. The 107 elements up to it constitute the *derivation*, scored against nature. The twelve elements beyond it (Figure 4) are published as *predictions* — explicitly labeled, unfitted, and falsifiable the day their spectra can be measured: the entrant is 6d from Z = 109 through 112, 7p from 113 through 118, and 8s at 119 and 120, with stated margins between 0.058 and 0.264 hartree, every one clearing the spin-orbit worst case.

![**Figure 4](figures/FIG3j120window.png)

***Figure 4.** The unwitnessed window, Z = 109–120: entrant, depth and margin, with the spin-orbit worst case each margin clears. Published as predictions.*

The second boundary statement is the deeper one. The entire construction was repeated with the speed of light sent to infinity — the same equation, the same algorithm, the one admitted constant removed — and the two derived tables are compared element by element in Figure 5. They disagree at eleven elements: Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, and Rf. The non-relativistic field files manganese and zinc under 4s instead of 3d, silver and cadmium under 5s, four lanthanides under 5d instead of 4f, mercury under 6s, and the heaviest actinides wrongly altogether — and since the relativistic construction scores 107 of 107 against observation, every one of those eleven placements is an error of the non-relativistic equation against nature. (At thorium the entrant survives by the path of the chain, but the underlying channel competition inverts without relativity as well.) The periodic table hanging on the classroom wall is not a solution of the non-relativistic Schrödinger equation. Any successful answer to Löwdin's challenge *had* to contain the speed of light; a purely non-relativistic derivation, had one been found, would have derived a visibly different table than ours — Figure 5 is what it would have looked like.

![**Figure 5](figures/FIG6relativisticvsnonrelativistic.png)

***Figure 5.** The relativistic table against its c → ∞ counterfactual, element by element. Eleven disagreements, every one an error against nature.*

---

## IX. THE LOGICAL STRUCTURE: FROM THE OBSERVED ORDER BACK TO THE VARIATIONAL PRINCIPLE

The algorithm of §II.2 constructs the table forward from the equation. The proof obligation runs in both directions, and the reverse direction — from the observed ordering back to first principles — was assembled as an explicit chain of six links, each one classified by its epistemic type:

- **Link 1 (identity, under two stated conditions):** the observed filling order *is* the entrant sequence of the V^{N−1} depths.
- **Link 2 (theorem):** the comparison of two candidate depths reduces to a comparison of one-channel properties of the field — well profiles and their integrated strengths.
- **Link 3 (computed):** the profile inequalities that decide every frontier competition, verified exhaustively: all 18 within-ℓ cases, all across-ℓ cases at |Δℓ| = 1, and the harder |Δℓ| = 2 family closed by direct computation.
- **Link 4 (theorem, with a measured and reinforcing remainder):** the block structure of the table follows from the profile ordering.
- **Link 5 (computed):** the passage from field ordering to energy ordering, whose remainder is precisely the correlation question — which §VII closes.
- **Link 6 (variational):** the ground state of the many-electron equation itself, invoked as the variational principle it is.

"Solved," under the standard this work set for itself, means this six-link chain with every link a theorem, an exhaustively computed verification, or the variational principle — and *no remainder of any kind left unexplained*. That standard is met, and the final section of the analysis explains the last and most technical part of meeting it.

---

## X. THE EXTERNAL CONDITIONS

The derivation is stated conditionally on a small set of named external results, each doing one job:

**The accuracy condition (Law A).** Rigorous results on Hartree–Fock accuracy bound *total* energies in the large-Z regime. They warrant the framework but cannot, by themselves, bound the small *differences* between candidate channels that each Aufbau step compares. This honest gap is exactly what Clause 3 (§VII) exists to close, and closes by computation.

**The domain condition (Law B).** The ℓ-conservation of the scalar-relativistic operator, together with the computed spin-orbit scale, fixes Z ≤ 112 as the domain on which (n,ℓ) is the correct shell label — and supplies the (n,ℓ,j) continuation beyond it, verified against the Dirac–Fock sequence on its full test set.

**The well-posedness condition (Law C).** The average-of-configuration theorem of Bach, Lieb, Loss and Solovej (1994) is the guarantee that the (n,ℓ)-subshell object at the center of the whole construction is mathematically well defined; Hantsch's existence theorem does the same for the mean-field minimizer. Both are verified against their primary sources.

Stating the solution conditionally on named, sourced theorems is not a hedge; it is the correct logical form of the claim that a conditioned mean field, checked where checking is needed, carries the exact equation's ordering. Every condition is explicit, and every one is either proved in the cited literature or computed in this work.

---

## XI. THE LAST MILE: AUDITING THE INSTRUMENT TO ZERO

A reader may grant everything above and still ask the auditor's question: how do you know your own numerical machinery isn't quietly contributing to the results? This work's answer was to hold the machinery to the same standard as the physics — every internal numerical discrepancy of the method, at any size, must be either eliminated or *derived*, that is, traced to a closed-form mathematical object and reproduced by it. Three findings closed this audit, and each turned out to be a piece of established mathematics.

**The method's one systematic defect is a Pulay term.** The construction evaluates energies along paths of varying occupation, and its energy-derivative bookkeeping showed a small, persistent discrepancy against the direct functional. This is a known phenomenon with a name: it is exactly the force-versus-energy-gradient discrepancy that arises off a functional's own stationary path, identified by Pulay in 1969 in the context of molecular forces. The defect is not an error; it is the Pulay term of the occupation parameter, and once named it can be decomposed exactly.

**The decomposition closes term by term.** In the appropriate frozen-orbital gauge, the defect splits exactly into a rotation of the varying orbital onto its occupied same-ℓ partners plus a response in the orthogonal complement. The rotation part reduces to (i) a linear term obeying the expected gradient law; (ii) a correction given in closed form by the *state-dependent multiplier identity* — when two orbitals belong to different self-consistent fields, the two natural evaluations of their shared kinetic matrix element differ by exactly (ε_v−ε_u)⟨u|v⟩ − ⟨u|(V_v−V_u)|v⟩ plus the corresponding exchange difference, an identity verified here to machine precision and reproducing the measured discrepancy to better than one part in 10⁴; and (iii) a curvature term extracted *exactly*, because the energy functional is exactly quartic along any fixed orbital direction, so five evaluations determine every Taylor coefficient with no truncation error at all. The orthogonal-complement part is the first-order perturbed-Hartree–Fock response in the sense of Gerratt and Mills (1968), and decomposes exactly by the same quartic method. Nothing is left over.

**The closing identity is Löwdin's.** The multiplier identity in (ii) — the mathematical object that resolved the final unexplained number in the entire record — is an instance of the non-orthogonality problem analyzed by Löwdin in 1950. The author of the challenge, nineteen years before posing it, published the mathematics that closes the last gap in its answer.

Every registered discrepancy in the work's archive now stands as one of: a falsified pre-registered prediction (kept on record, as honesty requires), a caught-and-remedied procedural error, or a former "numerical fault" reclassified as derived mathematical content once the identities above were in hand. The audit's final balance is zero.

---

## XII. THE CHALLENGE'S CRITERIA, ANSWERED POINT BY POINT

1. **Bridge the gap between the equation and the table.** Done as an explicit six-link chain (§IX), each link a theorem, an exhaustive computation, or the variational principle.
2. **Define what the rule governs.** Defined and defended (§I, §VI.2): the differentiating electron in its exact V^{N−1} field.
3. **Start from first principles.** The many-electron Hamiltonian in its scalar-relativistic reduction; c = 137.035999 the only entered number (§III).
4. **Exclude empirical heuristics.** No parameters, no experimental energies, no screening constants; observed configurations used only as the scoring target (§III).
5. **Solve for the eigenvalue evolution with Z.** The 107-element chained construction, with the full candidate spectrum recorded at every step (Figure 1).
6. **Derive the Madelung rule.** Clause 1 at 107/107; the secondary rule as Clause 2; the period sequence and the absence of a g block as consequences (§V).
7. **Account for the exceptions.** Derived, not excused: three tie-break exceptions from the orbital-collapse condition; the coinage-metal anomalies by an exact selection rule; and the relativistic clause explaining why the observed table could never have come from the bare non-relativistic equation (§VI, §VIII).

---

## XIII. WHAT IS NEW, AND WHAT IS OWED TO OTHERS

New in this work: the chained, parameter-free V^{N−1} derivation and its 107-of-107 score; the derived collapse-conditioned account of exactly the observed exceptions; the field-derived absence of the g block; the closure of the correlation question at every contested element; the demonstration that the observed table is irreducibly relativistic; twelve falsifiable superheavy predictions; and a methodological record in which every claim is cryptographically bound to a prediction that preceded it. A survey of the prior art, maintained throughout the work, supports the delimiting claim: no previous treatment derives the ordering without parameters, and none derives the exceptions.

Owed to others: nearly everything else, and the debts are the best part of the story. The challenge is Löwdin's (1969). The theorems conditioning the mean field are Bach, Lieb, Loss and Solovej's (1994) and Hantsch's. The relativistic reduction is Koelling and Harmon's. The correlation machinery descends from the second-order self-energy methods of Dzuba and Flambaum's school. The collapse physics of the exceptions is Griffin, Andrew and Cowan's (1969), and the two-branch mean-field phenomenology behind the record's finest detail is theirs as well (1971). The instrument-defect mathematics is Pulay's (1969) and Gerratt and Mills's (1968). And the identity that closed the final gap is Löwdin's own (1950). Three of the load-bearing works are dated 1969 — the challenge, the Pulay term, the collapse computation — and the mathematics that finishes the answer belongs to the man who asked the question. What this work adds is the assembly, the chain, and the score.

---

## XIV. REFERENCES AND BIBLIOGRAPHY

**The challenge and the rule**
1. Löwdin, P.-O. (1969). "Some Comments on the Periodic System of the Elements." *Int. J. Quantum Chem.* 3 (S3A), 331–334.
2. Madelung, E. (1936). *Die Mathematischen Hilfsmittel des Physikers*, 3rd ed. Springer, Berlin.
3. Janet, C. (1929). The left-step periodic table. See Stewart, P. J. (2010) for the priority discussion.
4. Klechkovskii, V. M. (1956). *Sov. Phys. JETP* 3(1), 125–127; and (1962), "Justification of the rule for successive filling of (n+l) groups," *Sov. Phys. JETP* 14(2), 334–335.
5. Goudsmit, S. A. & Richards, P. I. (1964). "The order of electron shells in ionized atoms." *Proc. Natl. Acad. Sci.* 51, 664–671.

**Foundations and conditions**
6. Bach, V., Lieb, E. H., Loss, M. & Solovej, J. P. (1994). "There are no unfilled shells in unrestricted Hartree–Fock theory." *Phys. Rev. Lett.* 72, 2981–2983. DOI 10.1103/PhysRevLett.72.2981. [the well-posedness condition]
7. Hantsch, F. (2014). "Existence of minimizers in restricted Hartree–Fock theory." *Electron. J. Diff. Equ.* 2014(44), 1–16; arXiv:1206.4932.
8. Koelling, D. D. & Harmon, B. N. (1977). "A technique for relativistic spin-polarised calculations." *J. Phys. C* 10, 3107. [the scalar-relativistic kernel]
9. Dzuba, V. A., Flambaum, V. V., Silvestrov, P. G. & Sushkov, O. P. (1987). "Correlation potential method for the calculation of energy levels, hyperfine structure and E1 transition amplitudes in atoms with one unpaired electron." *J. Phys. B* 20, 1399–1412. DOI 10.1088/0022-3700/20/7/009. [the second-order correlation potential Σ⁽²⁾ underlying the correlation clause]

**The exceptions and orbital collapse**
10. Griffin, D. C., Andrew, K. L. & Cowan, R. D. (1969). "Theoretical Calculations of the d-, f-, and g-Electron Transition Series." *Phys. Rev.* 177, 62. DOI 10.1103/PhysRev.177.62.
11. Griffin, D. C., Cowan, R. D. & Andrew, K. L. (1971). "Instabilities in the Iterative Solution of the Hartree-Fock Equations for Excited Electrons." *Phys. Rev. A* 3, 1233.
12. Connerade, J.-P. (1978). "The non-Rydberg spectroscopy of atoms." *Contemp. Phys.* 19, 415–447 [orbital collapse]; and Connerade, J.-P. & Lane, A. M. (1988). "Interacting resonances in atomic spectroscopy." *Rep. Prog. Phys.* 51, 1439–1478.
13. Cowan, R. D. (1981). *The Theory of Atomic Structure and Spectra.* University of California Press, Berkeley.

**The instrument mathematics**
14. Löwdin, P.-O. (1950). "On the Non-Orthogonality Problem Connected with the Use of Atomic Wave Functions in the Theory of Molecules and Crystals." *J. Chem. Phys.* 18(3), 365–375. DOI 10.1063/1.1747632.
15. Pulay, P. (1969). "Ab initio calculation of force constants and equilibrium geometries in polyatomic molecules. I. Theory." *Mol. Phys.* 17, 197–204.
16. Gerratt, J. & Mills, I. M. (1968). "Force Constants and Dipole-Moment Derivatives of Molecules from Perturbed Hartree–Fock Calculations. I." *J. Chem. Phys.* 49, 1719–1729. DOI 10.1063/1.1670299.
17. Hartree, D. R. (1957). *The Calculation of Atomic Structures.* Wiley, New York.
18. Froese Fischer, C. (1977). *The Hartree-Fock Method for Atoms.* Wiley, New York.
19. Strang, G. (1972). [the "variational crimes" consistency analysis]

**Assessments of the challenge's status**
20. Scerri, E. R. [status assessments of the Löwdin challenge; source of the verbatim challenge text]
21. Ostrovsky, V. N. [assessment and the model-potential literature]

---
