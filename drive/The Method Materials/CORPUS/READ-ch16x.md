# READ-ch16x — chat 126 — main volume L9494–L9608

**Unit.** Chapter 34 head and epigraph, §34.1 *The problem, and the wrong target*, §34.2 *The three
bodies, and the pair that has no variable*, §34.3 *What the ladders can and cannot reach*, §34.4
*The rule*. **115 lines.**

**Boundary, MEASURED by heading scan on the member before any line was read.** Chapter 34 body opens
**L9494**; `## 35.` body opens **L9716**; the chapter is **222 lines**, above the measured 74–150
band, so it was cut. Section heads: 34.1 L9500 · 34.2 L9532 · 34.3 L9562 · 34.4 L9578 · 34.5 L9609 ·
34.6 L9622 · 34.7 L9634 · 34.8 L9649 · 34.9 L9661 · 34.10 L9673. **Cut taken at the end of §34.4**,
where the statement of the rule closes and its execution begins; L9609–L9715 (107 lines) is chat
127's unit. Main volume **81.0 % read at L9608 of 11,855**.

**Resolvers.** Every pointer resolved under **both** `body_range` and `section_span`. They
**COINCIDE at ten of twelve**: §34.1–§34.10 all coincide. They **differ at §34 and §35**, which is
the resolvers' own semantics on a chapter heading with subsections, not a defect — `body_range`
returns the head alone, `section_span` the chapter. No section of this unit ends a Part, so chat
124's C1 does not bite.

**Instruments.** `r2-ch16w` (computable, 336 lines banked) and `r2-ch16x` (prose, 160 lines banked).

---

## A. Deviations

### 16x-01 — the printed opening sequence overruns the population it is read from

**Printed, L9504–L9507:**
> Read from the observed ground configurations of all 108 neutrals, the sequence in which subshells
> OPEN is
> `1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s **5d 4f** 6p 7s **6d 5f** 7p`

**Restated, L9592:** *Read from the observed ground configurations of the 108 neutrals, not from a
fit.*

**MEASURED.** The sequence's last opening is **7p**. Deriving each opening's Z from the printed
sequence and the unit's own capacity rule 2(2ℓ+1) — a subshell opens at Z = 1 + the total capacity
of everything before it — gives **7p at Z = 113**. The derivation is not recited: it is validated
against the two anchors the unit itself prints, returning **5d at Z = 57** (*Lanthanum opens 5d at
Z = 57*, L9509) and **6d at Z = 89** (*actinium opens 6d at Z = 89*, L9510), both exact. The only
opening the model cannot supply is the second member of an inverted pair (4f, 5f), for which the
unit prints no Z either.

**7p cannot have been read from a population capped at Z = 108.** The cap is stated four times in
the chapter's own neighbourhood: L9504 and L9592 (*108 neutrals*), **§34.9 L9663** (*Exceptionless
on 106 elements, Z = 3 to 108*) and **§35.2 L9746** (*107 of 107. Across Z = 2–108*). 106 = 108 − 3
+ 1 and 107 = 108 − 2 + 1, so those two are internally exact; it is the sequence that reaches past
the boundary. **Openings requiring Z > 108: exactly one, 7p.**

**Present in Prints & Proofs unchanged** (P9410, P9413), so this is authored, not produced.

### 16x-02 — *Seventeen of nineteen* is exact under one convention and false under the other

**Printed, L9511:** *Seventeen of nineteen openings agree; two do not.*

**MEASURED** against a Madelung order **generated** (sort by n+ℓ, then n), not recited:
`1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p`.

- **Convention A, position by position: 15 of 19 agree, 4 differ** — positions 13, 14, 17, 18.
- **Convention B, longest common subsequence (= minimum displacement): 17 of 19, 2 displaced.**

The printed figure is **exact under B and false under A**, and the unit names no convention. The
figure is internally consistent with itself (17 + 2 = 19, and the parsed sequence holds 19
openings), and with the **89%** printed at L9514 and L9605: 17/19 = 89.47 → **89** under
`Decimal.quantize` HALF_UP; convention A would give **79**. Both inversions named at L9509 are
confirmed inverted against the generated order.

**R3 names the convention** — displacement, not position — and the figure stands as printed.

### 16x-03 — Λ_var carries eleven variables in the main volume and twelve in the Index of Indices

**Printed, main L9537:** *Λ_var places every variable of the problem on (body, role). E = 0.*

**MEASURED.** The table at L9539–L9546 places **eleven**: Z · Nₑ · ℓ_core · n_out · p · n₀ · T · c ·
u · ℓ · δ.

**Index of Indices, ioi L1598, read in full at its entry `## Λ_var — the variables`:** *Twelve
variables on (body, role), body order nucleus < core < core+rydberg < nucleus+core < rydberg.*
**E = 0.**

The twelfth is **n\***, and the ioi's singleton rule depends on it: *Λ_var passes ℛ with both δ and
n\* present, because both land in the same cell* (ioi L1609–L1612). **n\* is absent from the
main-volume table**, so as printed the main volume cannot support the compendium's own rule.

Corroborated exactly: **E = 0** (the only E assignment in the entry), the body order, and the empty
pair row (ioi L1869, *no nucleus + rydberg cell — the three-body factorisation*).

### 16x-04 — the radicand is called a count of states and is a count of subshells

**Printed, L9524–L9525:** *The radicand is the count of states below: complete lower shells of the
same ℓ, plus the fraction of the current one already filled.* **Restated L9593.**

**MEASURED over (n, ℓ) for n = 2…7, ℓ = 0…3.** n − ℓ − 1 equals the number of complete lower
subshells of the same ℓ (those with n′ = ℓ+1 … n−1) in **every** case, and equals the number of
**states** below of the same ℓ in **none** of the 18 non-trivial cases: the two differ by the factor
2(2ℓ+1), which is never 1. Example: (n, ℓ) = (3, 1) gives n − ℓ − 1 = 1 against 6 states.

**The apposition is exact and the head of the sentence is not.** No clash with the third reading the
unit gives the same term — *the node count* (L9587) and the node theorem (L9593) — since radial
nodes are also n − ℓ − 1.

### 16x-05 — *the provenance of every term is §34.8's table*, and one term has no row

**Printed, L9596–L9597:** **No parameter is fitted**; the provenance of every term is §34.8's table.

**MEASURED by reading §34.8 (L9649–L9660) in full**, not by probing it. The table carries **five
data rows**: n − ℓ − 1 (the node theorem) · 2(2ℓ+1) (antisymmetry, twice) · ℓ(ℓ+1) (the centrifugal
term) · the energy of a single state · the endpoints (arithmetic on the above).

The rule is ν(n,ℓ,q) = n − a·√( n − ℓ − 1 + q/2(2ℓ+1) ). **The occupancy q has no row and zero
occurrences in §34.8** — and q is precisely the term §34.1 argues for at L9527–L9530. *Every term*
is therefore a false universal against the table it cites. (`a` is arguably carried by *the
endpoints*, which bound it; q is not carried by anything.)

### 16x-06 — Janet dated 1929 in the body and 1928 in the bibliography

**Printed, L9599–L9600:** *n+ℓ belongs to Madelung (1936), to Janet (1929) before him, and to
Klechkovskii.*

**References body occurrence L11503–L11855, L11777:** *Janet, C. (**1928**). — the left-step
periodic table; E(Janet) = 0.*

**MEASURED:** the year **1929 has zero sites in the References body**. Madelung is exact —
L9599's (1936) against L11815's *Madelung, E. (1936)*. **Docket 16.**

### 16x-07 — *Both Pauli quantities* names one quantity twice

**Printed, L9523–L9524:** **Both Pauli quantities appear.** *The capacity 2(2ℓ+1) governs
admissibility AND sits inside the radicand.*

**MEASURED:** the paragraph prints exactly **one** distinct Pauli quantity, 2(2ℓ+1), in two roles.
The unit's own restatement says so: L9594, *antisymmetry the capacity 2(2ℓ+1), **twice***. **Count
word against its own body: one, not both.**

---

## B. Verified findings

1. **The rule is printed twice and the two printings are identical.** L9518 and L9583 both read
   `ν(n,ℓ,q) = n − a·√( n − ℓ − 1 + q/2(2ℓ+1) )` — **byte-identical** on the extracted form. The
   admissibility clause matches too (L9520–L9521 against L9580–L9581, *q < 2(2ℓ+1)* in both).
2. **The two Z anchors are exact.** 5d at Z = 57 and 6d at Z = 89, both recovered from the printed
   sequence and the printed capacity rule with no constant supplied by hand.
3. **The ladder table is exact against its own identity.** Z = Nₑ + c − 1 (L9564) leaves two of
   three free; **all four rows** name a fix and a variation that together cover {Z, Nₑ, c}; *no
   ladder can vary Z alone* holds under the identity; *Three ladders exhaust the electronic space*
   matches **3 electronic rows against a 4th that varies the neutron number**.
4. **The Λ_var table's shape is exact.** Three bodies give 3 singletons + C(3,2) = 3 pairs = **6
   DATA rows**, and the table has exactly 6. **Exactly one** row is empty in every value cell —
   *nucleus + rydberg* — which is the section's whole claim, corroborated at ioi L1869.
5. **The channel equation matches the index.** δ = √p · f(u) (L9558): p is a **core + rydberg**
   variable and u a **nucleus + core** variable in the table, so the two factors are the two
   populated pairs, exactly as claimed.
6. **`E = 0` is corroborated** at the Index of Indices entry, and is the only E assignment there.
7. **L9580's forward pointer holds, and a probe would have failed it.** *Stated here in the form
   §34.5 to §34.7 use it.* §34.5–§34.7 were **printed in full** (13, 12 and 15 lines): §34.5 opens
   *Requiring the observed subshell to have least ν*, §34.6 carries and resets `a`, §34.7 fixes
   where `a` sits in its corridor. A ν-token probe scores §34.6 and §34.7 at **zero** and would have
   recorded a false defect.
8. **L9588's reset clause is exact at its target.** *reset only at a subshell opening, an aufbau
   exception or the return from one (§34.6)*; §34.6 L9624–L9626 prints **eighteen** resets as
   **8 + 6 + 4**, and 8 + 6 + 4 = 18.
9. **Madelung (1936) is bibliographed and dated exactly** (L11815).
10. **Ruling 46: zero sites** in the unit. **First person: zero sites** (guarded against the Roman
    numeral form). **Unmarked sub-headings: zero** (blank-line-above test).
11. **Duplicated-section sweep: 1 of 56 long lines recurs**, and it is the epigraph already recorded
    as chat 125's 16v-06 — a duplicated sentence, not a duplicated section. **Twenty consecutive
    units with zero duplicated sections.**
12. **Prints & Proofs: five headings for five**, at offset −94 (chapter head, §34.1) and −96
    (§34.2, §34.3, §34.4).
13. **Element names all resolve** — lanthanum, cerium, actinium and protactinium each carry name
    and symbol sites across the volumes (Register 6–19 sites each). **Not absent-member class.**
14. **The unit cites the Register nowhere**, and neither does the whole of Chapter 34
    (L9494–L9715): **zero** `register NNN` citations. No pointer to fail.
15. **The scatter figures all fall as claimed** — 0.187→0.041, 0.119→0.028, 0.088→0.018,
    0.059→0.021, 0.086→0.047 — and every one of the ten is corroborated at **register L5065**, so
    none is single-witness.

---

## C. Incidentals

1. **The offset shift −94 → −96 is one added sentence, and it is a Ruling 45 member.** Aligned diff
   of main L9512–L9531 against PP L9418–L9435 returns exactly one change: the volume adds *The rule
   that names the order exactly is stated, derived and attributed at §34.4; what follows here is the
   reading that found its shape.* (L9515–L9516). **The clause about the reading is post-PP.**
2. **PP carries BOTH epigraph copies** — P9396–P9398 (Part frame: *This part states what the method
   delivered, what it cost…*) and P9402–P9404 (chapter frame: *This chapter states the challenge…*).
   Chat 125's **16v-06** should carry this: the two are a Part frame and a chapter frame sharing a
   126-character prefix, present in the original, **not a splice**. The R3 repair is a rewording of
   the shared opening, not a deletion.
3. **Ruling 45 candidates in the unit, five:** L9516 (*the reading that found its shape*), L9580
   (*Stated here*), **L9593 (*§34.10 gives the session that did it*)**, L9599 (*not this work's*),
   L9601 (*this record's own, first stated in this work*). Under chat 115's discriminator **L9593 is
   the unambiguous member** — it names the work's own making. L9599 and L9601 are priority claims,
   which the class has always allowed.
4. **L9559's *no third factor because the index holds no third pair*.** The table **prints** a third
   pair row; it carries no variable. Exact only under *holds* = *carries a variable in*.
5. **L9576's *has never been traced*** — the census's own row 1195 flags it. Unmeasurable by sweep;
   what the sweep covered: *isotopic* has **1 main site (the table row itself), 6 Register, 3 ioi, 1
   pc, 0 mc, 0 sc**. **Docket 19.**
6. **Klechkovskii, Pauli and Schrödinger are unbibliographed** (References body L11503–L11855).
   Schrödinger is chat 125's 16v-07 at the epigraph's other copy; **Klechkovskii is new** and is
   named as one of the three owners of the n+ℓ rule, the other two both bibliographed. Pauli is used
   adjectivally throughout (*Pauli's capacity*), the same shape as chat 125's members. **Docket 36.**
7. **L9605's *Chapter 35 and the paper* is not a stale reference.** References L11816 bibliographs
   *Lach, M. (2026). The Löwdin Solution. — the companion paper*, and L11807 says the companion
   paper carries the full list. **Not a defect.**
8. **§34.6's eighteen resets include only 8 subshell openings against the sequence's 19 openings.**
   Out of unit; flagged for chat 127 to test at §34.6 rather than assumed.
9. **§34.8's table covers ℓ(ℓ+1)**, which is not a term of the ν rule but of §34.7's entry point —
   the table's scope is the chapter's apparatus, not the rule alone. This is why 16x-05 turns on q
   and not on the table's extra row.
