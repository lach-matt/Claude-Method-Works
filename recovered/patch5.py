s=open('mkmd2.py').read()

# ---- replace the whole 8.6 severance section
old = s[s.index("### 8.6 The system is severed"):s.index("### 8.7 Connectivity against acyclicity")]
new = """### 8.6 The system is connected — the severance was an artefact

**A previous draft concluded that the exclusion of macroscopic wormholes lives in a component the law
index cannot reach, and that this was why six repair operations failed.** Rebuilt on the four derived
vocabularies, that is wrong.

```
nodes       {len(F['system_tmas']['nodes'])}   T, M, A, S
edges       {F['system_tmas']['edges']}
components  {F['system_tmas']['components']}
cycles      {F['system_tmas']['cycles']}
complete    {F['system_tmas']['complete']}
```

**Every vocabulary connects to every other**, with all four at degree three.

{hdr(['charger','trigger','jurisdiction','currency','spans','status'])}
{chr(10).join(row([k, ','.join(v['trigger']), ','.join(v['jurisdiction']), ','.join(v['currency']), ','.join(v['spans']), v['status']]) for k,v in F['system_tmas']['chargers'].items())}

> **{F['system_tmas']['withdrawn']}**

**So what is the obstruction?** Not connectivity.

> **{F['system_tmas']['restated']}**

**The charger is reachable and does not fire on the cell in question** — which is precisely what
Maldacena, Milekhin and Popov demonstrated, arrived at here from the graph rather than from the
construction.

**And the six repairs failed on arity**, which was always the explanation. Part VII and §8.2 are
untouched by this correction; the graph story was decoration on a partition already withdrawn in §8.4.

### 8.6b Graham–Olum is a conjecture

{hdr(['','',])}
{row(['status',F['graham_olum']['status']])}
{row(['what is proved',F['graham_olum']['what_is_proved']])}
{row(['what is not',F['graham_olum']['what_is_not']])}
{row(['age',F['graham_olum']['age']])}
{row(['function',F['graham_olum']['function']])}
{row(['why violation-free',F['graham_olum']['why_violation_free']])}

**The charger index of §10.1 lists it as firing. It should be conditional** — a conjecture with a
sufficiency proof is a third category the index does not have.

**And this explains §10.1's V6 result from the other end.** Four of five known violations fall outside
V6's admissible region **because the condition was built to have that property**: its clauses exclude
chronal geodesics, non-self-consistent solutions and Planck-scale effects by construction.

**A curved-space proof does exist** — the achronal ANEC for general QFTs in the near-horizon geometry of
spherical extremal black holes. **Another Killing horizon**, and the sixth independent instance of the
same restriction.

"""
s=s.replace(old,new,1)

# ---- add the theorem chain and the repair taxonomy as a new section in Part X
anchor="### 10.5 A term whose status is scope-dependent"
newsec="""### 10.5 The translator, and the theorem chain that defines it

Three of the instances above need different repairs, and only one needs anything invented.

{hdr(['repair','in bits','cost','instance'])}
{chr(10).join(row(list(k)) for k in F['repairs']['kinds'])}

**Status is one bit per vocabulary, and the partition forces one-hot.** Across
{F['repairs']['one_hot']['terms_tested']} terms, {F['repairs']['one_hot']['patterns_used']} of
{F['repairs']['one_hot']['patterns_available']} patterns occur and every one has weight 0 or 1:
**{F['repairs']['one_hot']['finding']}**

{hdr(['weight','count','meaning'])}
{row([0,F['repairs']['one_hot']['weight_0'],'needs a translator, or is ungrounded'])}
{row([1,F['repairs']['one_hot']['weight_1'],'predicates on exactly one vocabulary'])}
{row([2,F['repairs']['one_hot']['weight_2'],'a relation, or an unsplit conflation'])}

**The test recovers by one rule what three separate investigations found by hand, and finds nothing
new** — {F['repairs']['one_hot']['new_findings']} new flags across forty terms. Its limit is real:
{F['repairs']['one_hot']['limit']}

**And n and ℓ have no dictionary.** {F['repairs']['no_dictionary']}

> **{F['repairs']['functor']}**

### 10.6 The chain, primary-sourced

{hdr(['','theorem','statement','role'])}
{chr(10).join(row(list(t)) for t in F['theorem_chain'])}

```
IN     type III_1     no trace, no density matrix, no entropy     weight 0
OUT    type II_inf    trace, density matrix, entropy              weight 1
```

**The status bit is semifiniteness**, and von Neumann's classification makes it genuinely binary: an
algebra either admits a trace or it does not. **T3 flips it and T2 licenses T3 to run on a horizon** —
without a positive-generator translation there is nothing to cross by. T3's uniqueness and invertibility
are what make it a bit rather than a rung on a ladder.

**Four caveats, and the third is the weak joint:**

{hdr(['caveat',''])}
{chr(10).join(row(list(c)) for c in F['chain_caveats'])}

### 10.7 A term whose status is scope-dependent"""
assert anchor in s
s=s.replace(anchor,newsec,1)
open('mkmd2.py','w').write(s)
print('patched: 8.6 rebuilt, 8.6b added, 10.5-10.6 added')