s=open('mkmd2.py').read()

# --- register: add session-2 withdrawals and the audits
old="""{hdr(['claim','cause'])}
{chr(10).join(row([w[0],w[1]]) for w in E['withdrawals'])}

### 11.3 The recurring class"""
new="""{hdr(['claim','cause'])}
{chr(10).join(row([w[0],w[1]]) for w in E['withdrawals'])}

### 12.2b Withdrawn since v2.0

Every entry below post-dates the previous draft, and several correct claims that draft asserts.

{hdr(['claim','cause'])}
{chr(10).join(row([w[0],w[1]]) for w in F['withdrawals_2'])}

### 12.2c The audit suite has four blind spots, not one

{hdr(['audit','compares','status','result'])}
{chr(10).join(row(list(a)) for a in F['audits']['list'])}

**Audit 23 is the only external validation in the construction**, and it passes: ten published LS term
tables reproduced exactly, zero microstate discrepancies against C(4ℓ+2, k). The subroutine that produces
every density figure and the axis-11 bound is verified against Condon–Shortley.

**Audit 24 finds 14 of 105 numeric claims unbacked** — five are regex false positives, six are values
computed in session and never written to a dataset, and **none is wrong.**

**Both were automatable and neither existed in the twenty-one-audit suite.** The audit index of Part IX
predicted both by clustering: twenty-one of twenty-two audits share all three properties — internal,
automatable, pass/fail — and the empty combinations were exactly these two.

### 11.3 The recurring class"""
assert old in s; s=s.replace(old,new,1)

# --- error class count
old2="""**{E['error_class']['instances']} instances of one class: {E['error_class']['description']}.**"""
new2="""**{F['error_class_2']['instances']} instances of one class: {E['error_class']['description']}.**
The dominant subtype is now **{F['error_class_2']['dominant_subtype']}** — {F['error_class_2']['note']}."""
assert old2 in s; s=s.replace(old2,new2,1)

# --- results: add the new ones
old3="""**9. Openness is the signature, not a failure.**"""
new3="""**9. Everything built outside V1 closes.** V3 geometry, V6 solution, the local null-surface index and
the covered ANEC cases are all globally consistent. The defect is in V1, on the V1–V3 edge, and in the
partition — nowhere else.

**10. Closure does not certify the letters.** Λ closes in all four coupling schemes with seven of thirteen
letters conflated, one ungrounded, and one quantity read but never indexed. **E states that the cells are
mutually consistent and says nothing about whether the coordinates refer to anything.** The clean null
case is V3, not Λ.

**11. The vocabulary partition is the BFV functor.** Four parts — theory, spacetime, algebra, state — with
the terms that refuse to place being *relations* between them. The self-consistent achronal ANEC is one
such relation, which is why no law-index coordinate can carry it.

**12. The null-energy gap is a modular theory gap.** Five of six curved-space routes need a Killing field;
the geometric-modular-flow repair is excluded by theorem; and the live target is half-sided modular
inclusion on isolated horizons — one cell from where it is proved.

**13. Openness is the signature, not a failure.**"""
assert old3 in s; s=s.replace(old3,new3,1)

# --- open questions: refresh
old4="""{row(['whether the two failure modes hold for indices not built here','needs someone else’s index'])}"""
new4="""{row(['whether the two failure modes hold for indices not built here','needs someone else’s index'])}
{row(['HSMI on isolated horizons','the live target; being worked on from the corner-mode side'])}
{row(['the 32 unchecked term pairs','IC has six and has never been checked once'])}
{row(['the six undocumented values','computed in session, carried by the paper, absent from any dataset'])}"""
assert old4 in s; s=s.replace(old4,new4,1)

# --- abstract: add the second half
old5="""> **What this paper does not claim.**"""
new5="""**Six further indices are then built, and every one outside the law index closes** — geometry, solution
status, the local geometry of a null surface, and the covered cases of the null-energy literature. Λ is
audited against its own sources and found to have **seven of thirteen letters conflated, one with no
referent at all, and one quantity read but never indexed** — while closing in all four standard coupling
schemes. **Closure does not certify the letters**, and the clean null case transfers to the geometry index.

Finally the vocabulary partition is derived rather than chosen: it is the **Brunetti–Fredenhagen–Verch
functor** read as a list of its parts, and the terms that refuse to place are *relations* between them.
The self-consistent achronal ANEC is one such relation, which is why no coordinate of a law index can
carry it — and the gap it names turns out to be a **modular theory** gap, with a target one cell from
where it is proved.

> **What this paper does not claim.**"""
assert old5 in s; s=s.replace(old5,new5,1)
open('mkmd2.py','w').write(s)
print('patched: register, results, open, abstract')