# ADDITION FOR REVIEW — THE MATHEMATICAL COMPENDIUM
# New objects from the Löwdin solution. Not yet entered into the work.
# Register anchors 1701–1712. Verification status stated per object, per the
# compendium's own rule: a check named is not a check performed.

---

# THE LÖWDIN OBJECTS

## The entrant operator

> **ent(Z) = argmax over frontier (n,ℓ) of |D(n,ℓ)|**, where D is the converged
> one-channel depth in the self-consistent field of the ion (Z, cfg(Z−1)),
> scalar-relativistic, c = 137.035999 the only constant.

The operator Chapter 27 said a non-closing index requires. Chained: cfg(Z) =
cfg(Z−1) + ent(Z). **Verified: 107 of 107 against the measured ground
configurations, Z = 2–108** (register 1701, 1702). Sign-exact by construction;
the margin |D(ent)| − |D(runner-up)| is the operator's own error bar and is
recorded at every step.

## The ordering law (five clauses)

**Clause 1** (ordering): smaller n+ℓ opens first — 107/107, no exception.
**Clause 2** (tie-break): equal n+ℓ, smaller n first — exceptions exactly
{La, Ac, Th}, derived by the collapse condition. **Clause 3** (correlation): at
the five contested rows the second-order differential is positive — every
competition widens. **Domain clause**: Z ≤ 112; spin-orbit worst case 0.083 Ha
under every margin. **Relativistic clause**: the c → ∞ twin operator disagrees at
eleven elements. *Statement and proof form in the companion paper; register
1701–1706.*

## The collapse condition

The double-well criterion, stated from the field, for which f channel is
collapsed at which Z. **Decides exactly the Clause-2 exception set and occupies
exactly the domain where Chapter 34's corridor is silent (L = −∞ at f openings).**
Adjacent to the transition the mean-field equations admit two stationary
solutions of one configuration with distinct converged operators; a sign at SCF
tolerance there is branch content, not noise (register 1703; prior art Griffin–
Andrew–Cowan 1969, 1971).

## The pinned-channel theorem (no g block)

**Every g channel offered by the walk sits at −1/(2n²) to storage precision:**
5g over 65 elements, 6g over 70, 7g over 57, 8g over 28. dn*/dZ = 0 across a
hundred protons is the absence of collapse, not its slow approach. *A relation
the data cannot violate is defending something: here, the nonexistence of a g
period below Z = 121* (register 1704).

## The state-dependent multiplier identity

For u, v eigenstates of **different** self-consistent operators, the two
eigen-relation evaluations of ⟨u|T|v⟩ differ by exactly

> **asym(u,v) = (ε_v − ε_u)⟨u|v⟩ − ⟨u|(V_v − V_u)|v⟩ + [⟨u|X_v⟩ − ⟨v|X_u⟩]**

**Verified to machine precision, four of four elements (worst 2.6·10⁻¹⁵), and
independent of SCF tolerance** — it is a residual of large cancelling terms, not
a convergence artefact. An instance of Löwdin's 1950 non-orthogonality problem;
it reclassified a registered instrument fault as derived content (register 1708,
1709).

## The exact-quartic decomposition

The energy functional with one shell's orbital varying along a fixed direction is
**exactly quartic in the path parameter** (one-body quadratic; two-body quartic).
Five evaluations at t ∈ {0, ±½, ±1} therefore determine every Taylor coefficient
with **zero truncation error**; the floating-point floor at |E| ~ 10⁴ Ha is the
only limit, and it is stated, not implied (~10⁻¹²; protocol at register 1710).
Used to close both halves of the defect below.

## The defect, closed: chord = rot + perp

The walk's one systematic internal discrepancy — the Hellmann–Feynman-in-q
defect — is **a Pulay term of the occupation parameter** (Pulay 1969). In the
one-shell-frozen gauge it splits exactly:

**rot** = linear gradient law + (q·s/dq2)·⟨asym⟩ [the multiplier identity above;
signed trace verified at ratios 0.999992 and 1.000103] + endpoint-Hessian term
[exact quartic; +1.7·10⁻⁷ and +6.1·10⁻⁹ — twenty to five hundred times too small
for the residual it was hypothesised to explain, **a hypothesis falsified by the
clause that scored HIT**, register 1709].

**perp** = the first-order perturbed-HF response on the orthogonal complement
(Gerratt–Mills 1968), exact-quartic decomposed; first-order dominant at three of
four valence shells, the fourth's curvature extracted exactly.

**Balance: zero unexplained residue** (register 1711).

## The twin operator Λ-side: c → ∞

The identical entrant operator with the constant removed. **Disagrees with the
c = 137.035999 operator at eleven elements** — Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu,
Hg, Lr, Rf — every disagreement an error against nature, since the relativistic
operator scores 107/107 (register 1706).

---

*Unverified-by-script note, per the compendium's discipline: the objects above
are verified by the solution's own sealed instruments and receipts, not by
`mathverify.py`; wiring them into the book's verifier is a build task, and until
it is done this page states the verification that exists rather than implying one
that does not.*
