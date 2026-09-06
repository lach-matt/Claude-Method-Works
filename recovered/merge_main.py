import re
f='The_Method_1_6-1.md'; m=open(f).read()
L=m.split('\n')

# ---- 1. cross-reference lines, inserted at section ends (line numbers from the audit; insert from bottom up) ----
xref={8566:' *Completed in Chapter 36: the families are indexed, the index closes, and the closure is the reason nothing here touches Poincaré.*',
      6932:' *Chapter 36 runs this on three bodies: E(Λ₃) = 0 and this section together give zero predictions, and that is Brudno\'s theorem on the chaotic stratum.*',
      5662:' *The same shortfall on a classical object — K₃, treewidth 2, one level short — is §36.3.*',
      3361:' *Three bodies carry all three excluded forms at once; §36.3 runs the method on that case and reports that the maximal forbidden case is the solved one.*'}
for ln in sorted(xref,reverse=True):
    L.insert(ln-1, xref[ln]+'\n')
m='\n'.join(L)

# ---- 2. contents block ----
old='## 34. The Löwdin challenge\n\n# APPENDICES'
assert m.count(old)==1
m=m.replace(old,'## 34. The Löwdin challenge\n## 35. The Löwdin solution\n## 36. Three bodies, and what a complete index is allowed to say\n\n# APPENDICES')

# ---- 3. chapters 35 and 36 into Part VII, before APPENDICES ----
c35=open('BODY2-CHAPTER-35-THE-LOWDIN-SOLUTION.md').read()
c35=re.sub(r'^# ADDITION.*\n# New chapter.*\n\n','',c35).strip()
c36=open('Chapter_36_Three_Bodies_RENUMBERED.md').read()
c36=c36.replace('# 36. Three Bodies, and What a Complete Index Is Allowed to Say','## 36. Three bodies, and what a complete index is allowed to say')
c36=c36.replace('Serving PART III — THE LAW and PART VI — THE REACH. The chapter runs',
 '*Serving PART III — THE LAW and PART VI — THE REACH, and placed here because it is a challenge posed outside this work. The chapter runs')
c36=c36.replace('reports that the method\'s negative is the problem\'s solution.','reports that the method\'s negative is the problem\'s solution. The formal statement is a companion paper, "The Three-Body Problem for Unknown Masses"; register entries 1713–1724 carry the record.*',1)
c36=c36.split('\n---\n\n**Cross-references:**')[0].strip()   # the build note is executed, not printed
anchor='\n\n# APPENDICES\n'
assert m.count(anchor)==1
m=m.replace(anchor,'\n\n---\n\n'+c35+'\n\n---\n\n'+c36+'\n\n'+anchor.lstrip('\n'))

# ---- 4. Index entries and counts ----
old='**Verified:** 51 terms, 129 entries, 40 specialisation relations, **0 violations — E(index) = 0.**'
assert old in m
m=m.replace(old,'**Verified:** 57 terms, 139 entries, 44 specialisation relations, **0 violations — E(index) = 0.** *Six terms and four relations entered with Chapters 35–36; the down-set condition holds by construction, and the closure script is owed a re-run.*')
old=' **prediction** …… §25.6 · §25.6 · §24.6 · App E'
assert old in m
m=m.replace(old,''' **Löwdin** …… §34 · §35 · §31.2.4 · App B

 challenge …… §34 · §31.2.4 solution …… §35 · App B

 **prediction** …… §25.6 · §25.6 · §24.6 · App E''')
old=' **closure** …… §6.1'
assert old in m
# add three-body block just before the 'closure' term block
m=m.replace(old,''' **three bodies** …… §12.11.2 · §21.5.1 · §25.6 · §31.1.1 · §36

 Λ₃ …… §36 · §25.6 shape sphere …… §36 · §12.11.2

'''+old,1)

# ---- 5. References: two groups appended before the closing constants note ----
old=' No source is cited for the lattice itself.'
assert m.count(old)==1
refs=''' **The Löwdin solution.** Entered at registers 1701–1712. The companion paper carries the full list; these are the works Chapter 35 rests on.

 · Löwdin, P.-O. (1969). Some comments on the periodic system of the elements. *Int. J. Quantum Chem.* **3**(S3A), 331–334. — the challenge.
 · Löwdin, P.-O. (1950). On the non-orthogonality problem. *J. Chem. Phys.* **18**, 365. — the multiplier identity is an instance.
 · Koelling, D. D. & Harmon, B. N. (1977). *J. Phys. C* **10**, 3107. — the scalar-relativistic kernel; c the one entered number.
 · Griffin, D. C., Andrew, K. L. & Cowan, R. D. (1969). *Phys. Rev.* **177**, 62–71; Griffin, Cowan & Andrew (1971). — orbital collapse; the double well the collapse condition reads.
 · Pulay, P. (1969). *Mol. Phys.* **17**, 197. — the occupation-parameter term that is the walk's one defect.
 · Gerratt, J. & Mills, I. M. (1968). *J. Chem. Phys.* **49**, 1719. — the orthogonal-complement response.
 · Madelung, E. (1936). *Die Mathematischen Hilfsmittel des Physikers*, 3rd ed. Springer. — the rule as a rule.
 · Lach, M. (2026). *The Löwdin Solution.* — the companion paper; the formal statement.

 **The three-body problem.** Entered at registers 1713–1724. Hill 1878, Poincaré 1890, Freuder 1982 and Mardling & Aarseth 2001 are cited above and reused.

 · Montgomery, R. (2014). The three-body problem and the shape sphere. *Amer. Math. Monthly* **122** (2015), 299–321. — shape space, the metric, the potential; **every structural object of Chapter 36 is his or older.**
 · Montgomery, R. (1998). *Nonlinearity* **11**, 363; (2002). *Arch. Ration. Mech. Anal.* **164**, 311. — braids and syzygies.
 · Chenciner, A. & Montgomery, R. (2000). *Ann. Math.* **152**, 881. — the figure-eight.
 · Hsiang, W.-Y. & Straume, E. (2006). arXiv:math-ph/0608060. — kinematic geometry of triangles.
 · Euler, L. (1767). *Novi Comm. Acad. Sci. Petrop.* **11**, 144; Lagrange, J.-L. (1772). *Prix Acad. Roy. Sci. Paris* **9**. — the five fixed points.
 · Lagrange, J.-L. (1770–71). *Mém. Acad. Berlin.* — the resolvent; N₈ is not new mathematics.
 · Maupertuis (1744); Jacobi, C. G. J. (1837). *C. R. Acad. Sci.* **5**, 61; (1842–43). *Vorlesungen über Dynamik.* — the metric whose geodesics are the trajectories.
 · Chazy, J. (1922). *Ann. Sci. École Norm. Sup.* **39**, 29. — the asymptotic classes; the five cells.
 · Saari, D. G. (1971). *Trans. AMS* **162**, 267; (1973) **181**, 351; (1984) *J. Diff. Eq.* **55**, 300. — collisions improbable; the strata disjoint up to measure zero.
 · Fleischer, S. & Knauf, A. (2019). *Arch. Ration. Mech. Anal.* **234**, 1007. — the same for n bodies.
 · Painlevé, P. (1897). *Leçons sur la théorie analytique des équations différentielles.* — the natural boundary; n = 3.
 · McGehee, R. (1974). *Invent. Math.* **27**, 191. — triple collision.
 · Kolmogorov (1954); Arnold (1963); Moser (1962, 1973). — the KAM stratum.
 · Alekseev, V. M. (1968–69). *Math. USSR Sbornik* **5–7**. — quasirandom motion; the chaotic stratum.
 · Brudno, A. A. (1983). *Trans. Moscow Math. Soc.* **2**, 127. — **entropy equals complexity: why a complete index predicts nothing on the chaotic stratum.**
 · Marchal, C. & Saari, D. G. (1975). *Celest. Mech.* **12**, 115; Marchal & Bozis (1982). *Celest. Mech.* **26**, 311. — Hill regions and Hill stability.
 · Monaghan, J. J. (1976a, b). *MNRAS* **176**, 63; **177**, 583; Nash & Monaghan (1978). *MNRAS* **184**, 119. — the statistical disruption theory.
 · Stone, N. C. & Leigh, N. W. C. (2019). *Nature* **576**, 406; Kol, B. (2021). *CMDA* **133**, 17; (2023) **135**, 29. — the statistical solution and the flux; "microcanonical ergodic flux" is Kol's term.
 · Moore, C. (1993). *Phys. Rev. Lett.* **70**, 3675. — braids in classical dynamics.
 · Montanari, U. (1974). *Inf. Sci.* **7**, 95; Baker & Pixley (1975). *Math. Z.* **143**, 165; Dechter, R. (1992). *Artif. Intell.* **55**, 87. — local-to-global consistency; the deficit's owners.
 · Lach, M. (2026). *The Three-Body Problem for Unknown Masses.* — the companion paper.

'''
m=m.replace(old,refs+old)
open('MAIN_MERGED.md','w').write(m)
print([l for l in m.splitlines() if re.match(r'^## 3[3-6]\.',l)])
print('§36. refs:',len(re.findall(r'§36\.',m)),' Chapter 36:',m.count('Chapter 36'),' words:',len(m.split()))
