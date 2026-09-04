import re
f='The_Method_1_6___The_Physics_Compendium-1.md'
m=open(f).read()
low=open('BODY3-PHYSICS-COMPENDIUM-ADDITIONS.md').read()
low=re.sub(r'^# .*\n','',low,flags=re.M).strip().lstrip('-').strip()   # strip review header + first rule
tb=open('Compendium_Additions_Three_Body_RENUMBERED.md').read()
tb_sec=tb.split('## B. PHYSICS COMPENDIUM — additions')[1].split('### To Λ_phys')[0]
tb_sec=tb_sec.replace('### New section: Λ₃ — THE THREE-BODY INDEX','').strip()
tb_sec=re.sub(r' ?!\[Fig \d\]\([^)]+\)','',tb_sec)   # figures carried in the chapter, not the compendium
tb_sec=tb_sec.replace('This is the interface §93 found','This is the interface *Kinematic and stateful* (above) found')

block=f'''# THE LÖWDIN-SOLUTION INDEXES — Λ_chain, Λ_cinf, Λ_V5

*Interface entries for the indexes of Chapter 35, in this compendium's own template: what the cells stand for, what number is attached, the rule taking one to the other, the constants that rule requires, what must be measured rather than computed, and what physics does and does not do. Register 1701–1712. The mechanisms are stated once, in the Mathematical Compendium (family LS); a second copy would drift.*

{low}

---

# Λ₃ — THE THREE-BODY INDEX

*Chapter 36; register 1713–1724. Objects in the Mathematical Compendium, family 3B.*

{tb_sec}

---

'''
anchor='# Λ_phys — THE INDEX OF PHYSICAL PARAMETERS'
assert m.count(anchor)==1
m=m.replace(anchor,block+anchor)

# ---- Λ_phys: count and new rows in the template ----
m=m.replace('**22 parameters.**','**27 parameters.**')
newp='''### speed of light — `c = 137.035999`

**137.035999 a.u.** · measured constant · from international standard · valid universal · 8 objects rest on it

**What it is.** the one entered number of the Löwdin solution: the constant in the Koelling–Harmon scalar-relativistic kernel of the entrant operator. No screening constant, no fitted parameter, no observed energy enters beside it.

**Where it comes from.** CODATA; the inverse fine-structure constant in Hartree atomic units.

> **Where it fails.** at c → ∞ — and the failure is measured, not anticipated: the twin index Λ_cinf disagrees with Λ_chain at eleven elements, each an error against nature (register 1706).

### three-body masses — `m₁, m₂, m₃`

**three positive reals** · free parameters · from the problem statement · valid all mass triples · 3 objects rest on it

**What it is.** the masses of the three bodies, unspecified; they enter Λ₃ through exactly six numbers — three c_ij and three unit vectors b_ij — and nowhere else.

**Where it comes from.** the problem as posed; the six-number coordinate supply is Montgomery 2014 §11.

> **Where it fails.** nowhere structural — S², the metric, N₈ and K₃ are mass-free. The masses move the five fixed points and nothing else.

### three-body energy — `E`

**a real** · free parameter · from the problem statement · valid E < 0 for bound strata · 2 objects rest on it

**What it is.** the conserved energy, entering as the conformal factor E + U of the Jacobi–Maupertuis metric.

**Where it comes from.** Maupertuis 1744; Jacobi 1837.

> **Where it fails.** at the zero-velocity surface {E + U = 0} (Hill 1878), where the metric degenerates and the geodesic flow stops.

### three-body angular momentum — `L`

**a real** · free parameter · from the problem statement · valid all L · 2 objects rest on it

**What it is.** the conserved angular momentum, carrying the reduction 6 → 4 of the phase space.

**Where it comes from.** standard; the reduction is Jacobi 1842.

> **Where it fails.** at the angular-momentum stratum boundary, which is envelope, not exact (`3B.tri`).

### gravitational constant — `G`

**1** · exact by scaling · from convention · valid universal · 0 objects rest on it

**What it is.** the coupling of Newton's potential, set to 1 by choice of units.

**Where it comes from.** scaling; carries no content once units are fixed.

> **Where it fails.** nowhere.

'''
anchor2='## The three failures that are measured rather than anticipated'
assert m.count(anchor2)==1
m=m.replace(anchor2,newp+anchor2)

# ---- aufbau entry: origin now resolved ----
old="AND the rule's ORIGIN is unresolved: Loewdin's challenge, Allen & Knight, Int. J. Quantum Chem. 90 (2003) 80-88."
assert old in m
m=m.replace(old,"The rule's ORIGIN was unresolved when this entry was written (Loewdin's challenge, Allen & Knight, Int. J. Quantum Chem. 90 (2003) 80-88); it is now derived — Λ_chain above, Chapter 35, register 1701 — and the three tie-break exceptions La, Ac, Th are derived with it. The remaining exceptions of the Cr class are total-energy rearrangements inside an open block, outside Λ_chain's claim.")

# ---- stale channel-constants sentence ----
old2="**The three fitted constants are the amplitude law's**, and they are why nothing\nin this work answers Loewdin's challenge."
assert old2 in m
m=m.replace(old2,"**The three fitted constants are the amplitude law's**, and they are why nothing\nin the *amplitude* work answers Loewdin's challenge. *Written at register 1571; the challenge was closed at register 1701 by a different instrument, Λ_chain, which carries no fitted constant. The sentence is kept because it was true of what it described.*")

open('PHYS_MERGED.md','w').write(m)
print(len(re.findall(r'^### ',m,flags=re.M)),'parameter entries;', 'sections:',[l for l in m.splitlines() if l.startswith('# ')])
