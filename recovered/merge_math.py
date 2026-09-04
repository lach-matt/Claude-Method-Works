import re
f='The_Method_1_6___Mathematical_Compendium-1.md'
m=open(f).read()

# ---------- II · OPERATORS: two rows ----------
old_row='| **S** | envelope-step count; 2S = the tight-pair count | sets of cells | §14.5.9 |'
assert old_row in m
new_rows=old_row+'''
| **ent** | the entrant operator: argmax over frontier (n,ℓ) of \\|D(n,ℓ)\\| in the ion's self-consistent field | subshells | §35; register 1701 |
| **π** | the shape map ℂ³ → ℝ³, w = (½(\\|Z₁\\|²−\\|Z₂\\|²), Re Z₁Z̄₂, Im Z₁Z̄₂) | configurations | Montgomery 2014; Hopf 1931 |
| **N₈** | the norm ∏_{ε∈{±1}³}(U − ε·u) — the minimal polynomial of a sum of three square roots | potentials | Lagrange 1770 |'''
m=m.replace(old_row,new_rows)
m=m.replace('Every derivation in the book runs through these. Nine are this work\'s own.',
            'Every derivation in the book runs through these. Ten are this work\'s own; two (π, N₈) are cited and used as found.')

# ---------- IV · OBJECTS: two new families, after Q ----------
LS='''## LS. The Löwdin solution — the order derived from the equation — 8 objects

*Chapter 35 and its companion paper; register 1701–1712. These objects are verified by the solution's own sealed instruments and receipts, not yet by `mathverify.py`; wiring them into the book's verifier is a build task, and until it is done this page states the verification that exists rather than implying one that does not. The mathematics of the challenge (Chapter 34, registers 1249–1357) is stated separately below under THE MATHEMATICS OF THE LÖWDIN WORK.*

### `LS.ent` — the entrant operator

**ent(Z) = argmax over frontier (n,ℓ) of |D(n,ℓ)|, D the converged one-channel depth in the self-consistent field of the ion (Z, cfg(Z−1)); scalar-relativistic Koelling–Harmon; c = 137.035999 the only entered number. Chained, cfg(Z) = cfg(Z−1) + ent(Z): 107 of 107 against the measured ground configurations, Z = 2–108**

*the operator Chapter 27 said a non-closing index requires; sign-exact by construction, and the margin |D(ent)| − |D(runner-up)| is its own error bar, recorded at every step*

grade **COMPUTED**· source *M §35; register 1701, 1702*· depends on `L.closed`, `Q.final`· depth 15

### `LS.law` — the ordering law, five clauses

**Clause 1 (ordering): smaller n+ℓ opens first — 107/107. Clause 2 (tie-break): equal n+ℓ, smaller n first — exceptions exactly {La, Ac, Th}, derived by `LS.coll`. Clause 3 (correlation): at the five contested rows the second-order differential is positive — every competition widens. Domain clause: Z ≤ 112; spin-orbit worst case 0.083 Ha under every margin. Relativistic clause: the c → ∞ twin disagrees at eleven elements**

*statement and proof form in the companion paper*

grade **PROVED**· source *M §35; register 1701–1706*· depends on `LS.ent`, `LS.coll`, `LS.twin`· depth 16

### `LS.coll` — the collapse condition

**The double-well criterion, stated from the field, for which f channel is collapsed at which Z: decides exactly the Clause-2 exception set and occupies exactly the domain where Chapter 34's corridor is silent (L = −∞ at f openings)**

*adjacent to the transition the mean-field equations admit two stationary solutions of one configuration with distinct converged operators; a sign at SCF tolerance there is branch content, not noise*

grade **COMPUTED**· source *M §35; register 1703; Griffin–Andrew–Cowan 1969, 1971*· depends on `LS.ent`· depth 16

> **PRIOR ART: the orbital-collapse double well is Griffin, Andrew & Cowan, Phys. Rev. 177 (1969) 62; the placement of it against the corridor's silence is this work's.**

### `LS.pin` — the pinned-channel theorem (no g block)

**Every g channel offered by the walk sits at −1/(2n²) to storage precision: 5g over 65 elements, 6g over 70, 7g over 57, 8g over 28. dn*/dZ = 0 across a hundred protons**

*the absence of collapse, not its slow approach; a relation the data cannot violate is defending something — here, the nonexistence of a g period below Z = 121*

grade **MEASURED**· source *M §35; register 1704*· depends on `LS.ent`· depth 16

### `LS.asym` — the state-dependent multiplier identity

**For u, v eigenstates of different self-consistent operators, the two eigen-relation evaluations of ⟨u|T|v⟩ differ by exactly asym(u,v) = (ε_v − ε_u)⟨u|v⟩ − ⟨u|(V_v − V_u)|v⟩ + [⟨u|X_v⟩ − ⟨v|X_u⟩]; verified to machine precision, four of four elements, worst 2.6·10⁻¹⁵, independent of SCF tolerance**

*a residual of large cancelling terms, not a convergence artefact; it reclassified a registered instrument fault as derived content*

grade **PROVED**· source *M §35; register 1708, 1709; Löwdin 1950*· depends on `LS.ent`· depth 16

> **PRIOR ART: an instance of the non-orthogonality problem, Löwdin, J. Chem. Phys. 18 (1950) 365.**

### `LS.quart` — the exact-quartic decomposition

**The energy functional with one shell's orbital varying along a fixed direction is exactly quartic in the path parameter (one-body quadratic; two-body quartic); five evaluations at t ∈ {0, ±½, ±1} determine every Taylor coefficient with zero truncation error**

*the floating-point floor at |E| ~ 10⁴ Ha (~10⁻¹²) is the only limit, and it is stated, not implied; protocol at register 1710*

grade **PROVED**· source *M §35; register 1710*· depends on `LS.ent`· depth 16

### `LS.chord` — the defect closed: chord = rot + perp

**The walk's one systematic internal discrepancy — the Hellmann–Feynman-in-q defect — is a Pulay term of the occupation parameter. In the one-shell-frozen gauge it splits exactly: rot = linear gradient law + (q·s/dq2)·⟨asym⟩ + endpoint-Hessian term; perp = the first-order perturbed-HF response on the orthogonal complement. Balance: zero unexplained residue**

*the signed trace verified at ratios 0.999992 and 1.000103; the endpoint-Hessian term (+1.7·10⁻⁷, +6.1·10⁻⁹) is twenty to five hundred times too small for the residual it was hypothesised to explain — a hypothesis falsified by the clause that scored HIT, and kept*

grade **PROVED**· source *M §35; register 1707, 1709, 1711; Pulay 1969; Gerratt–Mills 1968*· depends on `LS.asym`, `LS.quart`· depth 17

> **PRIOR ART: the occupation-parameter term is Pulay, Mol. Phys. 17 (1969) 197; the orthogonal-complement response is Gerratt & Mills, J. Chem. Phys. 49 (1968) 1719.**

### `LS.twin` — the twin operator, c → ∞

**The identical entrant operator with the constant removed disagrees with the c = 137.035999 operator at eleven elements — Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf — every disagreement an error against nature, since the relativistic operator scores 107/107**

*the relativistic clause of `LS.law`, measured rather than asserted*

grade **MEASURED**· source *M §35; register 1706*· depends on `LS.ent`· depth 16

## 3B. Three bodies — the index of families — 9 objects

*Chapter 36 and its companion paper; register 1713–1724. No new root: the family derives from `L.c1`–`L.c8`, `B.brk` and the operators, and the seed did not move — the cycle's falsifier passing on a new subject.*

### `3B.shape` — shape space and the shape sphere

**ℝ³ = ℂ³ / (translations × rotations); S² = that / scale. Onto; identifies exactly the oriented-congruent triangles; only triple collision maps to 0; w₃ = signed area up to a mass constant; ‖w‖ = I/2**

*the coordinates in which three bodies become one point*

grade **PROVED**· source *Montgomery 2014, Thm 1; Hopf 1931*· depends on —· depth 1

### `3B.metric` — the shape metric

**ds² = |dw|²/(2√‖w‖); every plane through 0 totally geodesic; cone metric dr² + ¼r²dθ²**

*as `3B.shape`*

grade **PROVED**· source *Montgomery 2014, Thm 3*· depends on `3B.shape`· depth 2

### `3B.JM` — the Jacobi–Maupertuis metric

**g_E = (E+U)·ds²; trajectories at energy E are its geodesics; dt = ds_E/√(2(E+U))**

*licence in the index: §12.11.1.3, §12.11.0.2*

grade **PROVED**· source *Maupertuis 1744; Jacobi 1837*· depends on `3B.metric`, `3B.pot`· depth 3

### `3B.pot` — the potential on shape space

**U(w) = Σ c_ij/d_ij, c_ij = (m_i m_j)^{3/2}/√(m_i+m_j), d_ij² = ‖w‖ − w·b_ij; identity r_ij² = d_ij²/μ_ij. No hyper-radius factor**

*650 triangles, 13 mass cases, error < 10⁻¹⁰; the first audit's uniform 13/13 failure was a hyper-radius divisor inherited from working material — register 1718, protocol 1722*

grade **MEASURED**· source *Montgomery 2014 §11; register 1718*· depends on `3B.shape`· depth 2

### `3B.norm` — the algebraic variety

**With u_ij = c_ij/d_ij, p = Σu², q = Σu_i²u_j², r = ∏u²: U⁸ − 4pU⁶ + (6p²−8q)U⁴ − 4(p³−4pq+16r)U² + (p²−4q)² = 0; constant term ∏(u₁±u₂±u₃)²**

*proved symbolically (sympy) and measured at 13 mass cases; an inherited form with U⁴ coefficient "6S₂²−4S₄+8S₁₁" = 2p²+16q was wrong and is withdrawn — register 1719*

grade **PROVED**· source *Lagrange 1770; register 1719, 1720*· depends on `3B.pot`· depth 3

> **PRIOR ART: N₈ is the norm over (ℤ/2)³ — Lagrange's resolvent method, 1770. Not new mathematics.**

### `3B.five` — the five fixed points

**Three Euler roots (one positive root of the quintic per ordering) and two Lagrange points, for every mass triple — 13/13**

*seed of the family index in §14.5's sense*

grade **MEASURED**· source *Euler 1767; Lagrange 1772; register 1717*· depends on `3B.pot`· depth 3

### `3B.tri` — the triangle form on K₃

**{|a−b| ≤ c ≤ a+b}: join-closed, meet-broken. Cap 8: 344 cells, 0 join failures, 8,385 meet failures; caps 3–12 meet failures 12·111·477·1,488·3,780·8,385·16,812·31,227·54,555·90,705; two-body chain 0 throughout**

*confirms §12.11.2 on a grid the book never ran*

grade **MEASURED**· source *M §36; register 1716*· depends on `L.c1`–`L.c8`· depth 4

### `3B.def` — the deficit

**K₃ has treewidth 2; strong 3-consistency is required; ℛ reaches 2 (§32.3). Shortfall exactly one level**

*the separation hypothesis of §7.1 broken by the smallest graph that can break it*

grade **PROVED**· source *M §21.5.1; Freuder 1982*· depends on `3B.tri`, `G.tw`· depth 5

### `3B.index` — the index Λ₃

**Λ₃ = {KAM, per, chaos, erg, coll} on ℳ_{E,L}. E(Λ₃) = 0: exhaustive (Chazy classes), disjoint up to measure zero (Saari 1971/73; Painlevé, n = 3). By §25.6, predictions = 0 — Brudno's theorem on the chaotic stratum**

*cited theorems assembled; the assembly is this work's. The maximal forbidden case of Chapter 18 is the solved case, because what is forbidden is exactly what Poincaré excludes — register 1724*

grade **PROVED**· source *M §36; register 1713, 1714, 1724; Chazy 1922; Saari 1971; Brudno 1983*· depends on `3B.def`, `3B.five`· depth 6

'''
anchor='# V · THE CHAINS'
assert m.count(anchor)==1
m=m.replace(anchor,LS+anchor)

# ---------- V · CHAINS: two new chains (appended before the closing rule) ----------
chains_new='''**depth 17** · `LS.chord` ← `LS.asym` ← `LS.ent` ← `L.closed` ← `L.dist` ← `L.birk` ← `L.bits` ← `L.circuit` · *the Löwdin solution's longest path; the walk's one defect closed at zero residue*

**depth 9** · `3B.index` ← `3B.def` ← `3B.tri` ← `L.c1`–`L.c8` ← tree ← §7.1 separation hypothesis · *nine links, no new root; closes to §25.6 and the Brudno rate*

---

# VI · WHAT IS UNFINISHED'''
assert m.count('---\n\n# VI · WHAT IS UNFINISHED')==1
m=m.replace('---\n\n# VI · WHAT IS UNFINISHED',chains_new)
m=m.replace('# VI · WHAT IS UNFINISHED\n','# VI · WHAT IS UNFINISHED\n\n*Neither the Löwdin solution nor the three-body work adds an open object; the two below are untouched by both.*\n',1)

# ---------- I · CYCLE recount ----------
m=m.replace('| closure — objects the register holds | **248** |','| closure — objects the register holds | **265** |')
m=m.replace('| ratio | **14.6 : 1** |','| ratio | **15.6 : 1** |')

# ---------- VII · BIBLIOGRAPHY: year-sorted insertions ----------
adds=[(1744,'Maupertuis','`3B.JM`'),(1767,'Euler','`3B.five`'),(1770,'Lagrange','`3B.norm`'),(1772,'Lagrange','`3B.five`'),
(1837,'Jacobi','`3B.JM`'),(1842,'Jacobi','`3B.JM`'),(1878,'Hill','`3B.index`'),(1890,'Poincaré','`3B.index`'),
(1922,'Chazy','`3B.index`'),(1931,'Hopf','`3B.shape`'),(1950,'Löwdin','`LS.asym`'),(1954,'Kolmogorov','`3B.index`'),
(1963,'Arnold','`3B.index`'),(1968,'Alekseev','`3B.index`'),(1968,'Gerratt & Mills','`LS.chord`'),(1969,'Griffin, Andrew & Cowan','`LS.coll`'),
(1969,'Pulay','`LS.chord`'),(1971,'Griffin, Andrew & Cowan','`LS.coll`'),(1971,'Saari','`3B.index`'),(1973,'Saari','`3B.index`'),
(1974,'McGehee','`3B.index`'),(1975,'Marchal & Saari','`3B.index`'),(1976,'Monaghan','`3B.index`'),(1982,'Marchal & Bozis','`3B.index`'),
(1998,'Montgomery','`3B.shape`'),(2000,'Chenciner & Montgomery','`3B.five`'),(2002,'Montgomery','`3B.metric`'),(2006,'Hsiang & Straume','`3B.shape`'),
(2014,'Montgomery','`3B.shape` `3B.metric` `3B.pot`'),(2019,'Fleischer & Knauf','`3B.index`'),(2021,'Kol','`3B.index`'),(2023,'Kol','`3B.index`'),
(2026,'Lach, *The Löwdin Solution*','`LS.ent` `LS.law` `LS.coll` `LS.pin` `LS.asym` `LS.quart` `LS.chord` `LS.twin`'),
(2026,'Lach, *The Three-Body Problem for Unknown Masses*','`3B.tri` `3B.def` `3B.index`')]
head,rest=m.split('# VII · THE BIBLIOGRAPHY',1)
lines=rest.split('\n')
# locate table rows
rows=[i for i,l in enumerate(lines) if re.match(r'\| \d{4} \|',l)]
tbl=[lines[i] for i in rows]
def yr(l): return int(l.split('|')[1])
newtbl=[(yr(l),l) for l in tbl]+[(y,f'| {y} | {w} | {o} |') for y,w,o in adds]
newtbl.sort(key=lambda t:t[0])
lines=lines[:rows[0]]+[l for _,l in newtbl]+lines[rows[-1]+1:]
rest='\n'.join(lines)
# Freuder 1982: append 3B.def
rest=re.sub(r'(\| 1982 \| Freuder[^\n]*)\|\n', lambda mm: mm.group(1).rstrip()+' `3B.def` |\n', rest, count=1)
rest=re.sub(r'\*\*(\d+) works, 1669–2026\.\*\*', lambda mm: f'**{int(mm.group(1))+len(adds)} works, 1669–2026.**', rest)
m=head+'# VII · THE BIBLIOGRAPHY'+rest
open('MATH_MERGED.md','w').write(m)
print('families:',len(re.findall(r'^## [A-Z0-9]+\. ',m,flags=re.M)),'objects:',len(re.findall(r'^### `',m,flags=re.M)))
