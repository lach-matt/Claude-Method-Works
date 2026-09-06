import re
f='The_Method_1_6___The_Index_of_Indices-1.md'
m=open(f).read()
low=open('BODY3-INDEX-OF-INDICES-ADDITIONS.md').read()
low=re.sub(r'^# .*\n','',low,flags=re.M).strip().lstrip('-').strip()
low=low.replace('**Figure A1.**','**Figure 12.**').replace('**Figure A2.**','**Figure 13.**')

# ---- V: Λ₃ subsection, inserted before "## The languages" in V ----
l3='''## Λ₃ — the three-body index

**The second index built from physics rather than from Λ** (the first is Λ_spectra), and the first whose subject is classical. Chapter 36; register 1713–1724.

| coordinate | values | bound |
|---|---|---|
| stratum | KAM, per, chaos, erg, coll | five, exhaustive |
| E | ℝ | sign fixes bounded/unbounded |
| L | ℝ | — |
| masses | ℝ₊³ | 13 order-types; symmetry order 6, 2, 1 |

**E(Λ₃) = 0.** Certificate (§18.4.1): the shape map, three dropped coordinates. *Its cells are configurations, not moves, so it carries no time column — the flow is the geodesic flow of the Jacobi–Maupertuis metric, and time is a quadrature (§12.11.1.3).* Named at §12.11.2 as the maximal case of what Chapter 18 forbids; built, and the completeness is the impossibility theorem read as an index.

'''
anchor='## The languages\n'
first=m.index(anchor)            # the one inside V (VIII has a second)
m=m[:first]+l3+m[first:]

# ---- VIII: new row form — a subsection before "## The one-line summary" ----
v8='''## Λ₃ — the three-body index

**What it is.** Five strata on ℳ_{E,L} over three unspecified masses; E = 0.

**Where it comes from.** The classes are Chazy 1922; disjointness is Saari 1971/73 and Painlevé for n = 3; the assembly into one index with a certificate is this work's (register 1713).

**What only it contributes.** *A complete index whose completeness IS the impossibility theorem.* E = 0 read as Poincaré: by §25.6 a complete index with no time column predicts nothing, and that is Brudno's rate on the chaotic stratum, not a failure of the method (register 1714, 1724).

'''
anchor2='## The one-line summary\n'
assert m.count(anchor2)==1
m=m.replace(anchor2,v8+anchor2)
old='| **the book\'s own** | E > 0 as a theorem about shape |'
assert old in m
m=m.replace(old,old+'\n| **Λ₃** | a complete index whose completeness *is* the impossibility theorem — E = 0 read as Poincaré |')
m=m.replace('**Λ is the only one built from physics.','**Λ and Λ₃ are the only ones built from physics.')

# ---- extended one-line summary: new rows ----
old2='| **Λ_t** | ℓ carries the limit, n carries the approach |'
assert old2 in m
i=m.index(old2); j=m.index('\n\n',i)
tail_rows=m[i:j]
m=m[:j]+'''
| **Λ_chain** | Λ's input column as a derived object — the order from the equation, one constant |
| **Λ_cinf** | that the periodic table is not a solution of the non-relativistic equation |
| **Λ_V5** | every contested competition widens under correlation |
| **Λ_j120** | Λ's falsification frontier, twelve rows wide |
| **Λ₃** | masses enter through six numbers; structure is mass-free — the three-body factorisation, closed |'''+m[j:]

# ---- Part X: the Löwdin-solution indexes ----
partx=f'''

# X · THE INDEXES BUILT IN THE LÖWDIN SOLUTION

*Registers 1701–1712; Chapter 35. Four indexes the solution builds beside Λ — what each holds, whether it closes, whether it carries time, and what role it plays for Λ. The template differs from Part IX's by design: these are transition indexes, and closure and time are the questions they exist to answer.*

{low}
'''
m=m.rstrip()+partx+'\n'
open('IOI_MERGED.md','w').write(m)
print([l for l in m.splitlines() if l.startswith('# ')])
print('Λ₃ occurrences:',m.count('Λ₃'),' Λ_chain:',m.count('Λ_chain'))
