#!/usr/bin/env python3
"""refute.py -- the refutation of the four-body shape, run on author-chosen terms.

The weakness admitted: I chose the 26 terms. The repair is not to choose better
but to stop choosing. Two term lists are used, and neither is mine:

  L1  The Method 1.4's own Index -- 51 terms, chosen by the author, and closed
      at E = 0 by the book's own construction
  L2  Transitions' own coordinate tables -- the nine-letter alphabet, the
      fifteen-letter alphabet, and audit 22's coordinate column

Classification is still mine and cannot be otherwise, so it is disciplined: each
term is assigned to the part in which the corpus DEFINES it, and the section is
named. A term whose defining section belongs to two parts gets weight 2.

Two refutations are available and both are run.
  R1  exhibit a term predicating on REFERENCE alone that is already content of
      another part -> REFERENCE collapses to a relation
  R2  show one of the six edges has no relation term -> the graph is not
      complete and the treewidth drops
"""
import itertools
from zeno import State, step

# ---- L1: The Method 1.4's Index, transcribed from the printed page ----------
L1 = [
 ("bracket","PROCEDURE","§20.1 the rule, a method of working"),
 ("bracket failure","LAW","§23.3 the failure condition"),
 ("bracket width","OBJECT","§21.1 w, a quantity of the series"),
 ("interiority","PROCEDURE","§20.2 rule 1"),
 ("limit-free","LAW","§20.3 invariance under an affine map"),
 ("the four rules","PROCEDURE","§20.2"),
 ("closure","LAW","§14"),
 ("closed index","LAW","§14.1"),
 ("closure defect","LAW","§6.1"),
 ("closure operator","LAW","§14.2"),
 ("R(X) = X","LAW","§14.1"),
 ("cost of a guarantee","LAW","§21 the price, a structural bound"),
 ("V = 4nu/3","OBJECT","§21.1 computed from three levels"),
 ("the floor","LAW","§21.2 Prop 14.1"),
 ("the pole","LAW","§18.5"),
 ("nu_V","PROCEDURE","§2.3 an admissibility rule"),
 ("extension","LAW","§17"),
 ("addable cells","LAW","§17.1 E1"),
 ("adjoinable axes","LAW","§17.2 E2"),
 ("imposable constraints","LAW","§17.3 E3"),
 ("prediction","LAW","§18.6 E(X) is the prediction budget"),
 ("E(X) as budget","LAW","§18.6"),
 ("Sc VI","OBJECT","§23.6 a channel"),
 ("second route","PROCEDURE","§23.6.6 two disjoint derivations"),
 ("quantum defect","OBJECT","§22 delta"),
 ("isoelectronic law","OBJECT","§22.13"),
 ("penetration","OBJECT","§22.3"),
 ("retrieval","PROCEDURE","§19 / §2.10"),
 ("retrieval redundancy","PROCEDURE","§19.1 rho"),
 ("route set","PROCEDURE","§19.1"),
 ("self-defence","LAW","§16"),
 ("totality","LAW","§16.5 D3"),
 ("process index","PROCEDURE","§26.8"),
 ("two routes","PROCEDURE","§2.8"),
 ("D_def","LAW","§16.4"),
 ("D_phys","LAW","§16.3"),
 ("self-reference","LAW","§15"),
 ("alphabet recovery","LAW","§15.1 S1"),
 ("bound recovery","LAW","§15.2 S3"),
 ("order recovery","LAW","§15.3 S2"),
 ("the collection","OBJECT","§22"),
 ("decline modes","PROCEDURE","§22.11 declines are recorded"),
 ("isoelectronic pairs","OBJECT","§22.6"),
 ("provenance","PROCEDURE","§2.11 a protocol"),
 ("the census","PROCEDURE","§2.5 census before search"),
 ("the index","OBJECT","the back-matter index, as an object"),
 ("index, self-referencing","LAW","the fixed point made visible"),
 ("the record","PROCEDURE","§26"),
 ("margins","PROCEDURE","App C"),
 ("recomputed","PROCEDURE","App C"),
 ("withdrawals","PROCEDURE","§26 / §2.12"),
]

# ---- L2: Transitions' own coordinate tables --------------------------------
L2 = [
 ("X causal ladder","OBJECT","T §5.1 an axis"),
 ("S_corr","OBJECT","T §5.1"),
 ("IC","OBJECT","T §5.1"),
 ("U unitarity","OBJECT","T §5.1"),
 ("NEC","OBJECT","T §5.1"),
 ("X_exp / X_spon","OBJECT","T §6.5 split"),
 ("U_open / U_ghost","OBJECT","T §6.5 split"),
 ("EOM","OBJECT","T §6.5 new axis"),
 ("core cell","OBJECT","T §5.3"),
 ("minimal support","LAW","T §5.4"),
 ("sub-case A, ordering","LAW","T §1.6"),
 ("sub-case B, arity","LAW","T §1.6"),
 ("global consistency","LAW","T §1.4"),
 ("possibility bound","LAW","T audit 27"),
 ("density","LAW","T §1.9"),
 ("trigger","LAW","T §8.1"),
 ("currency","LAW","T §8.1"),
 ("admission grade","PROCEDURE","T §0.2"),
 ("collision","PROCEDURE","T §0.2"),
 ("merge rule","PROCEDURE","T §0.3"),
 ("audit 22","PROCEDURE","T §6.4 an instrument"),
 ("promotion ledger","PROCEDURE","T §11.1"),
 # the candidates for REFERENCE-only content
 ("referent","REFERENCE","T §10.3 what a term points at"),
 ("ungrounded","REFERENCE","T §10.3 a term with no referent"),
 ("stated hypothesis","REFERENCE","T App. A per equation"),
 ("access grade [F/A/S/B]","REFERENCE","T App. B per source"),
 ("vocabulary (T/M/A/S)","REFERENCE","T §8.4 the BFV partition"),
 ("dictionary","REFERENCE","T §10.5 one vector, two bases"),
 # the relations
 ("conflated","OBJECT+REFERENCE","T §6.1"),
 ("jurisdiction","LAW+REFERENCE","T §8.1"),
 ("term-sharing pair","PROCEDURE+REFERENCE","T §6.4"),
 ("precedent","LAW+REFERENCE","M §27"),
 ("cap / frame","OBJECT+LAW","M §7.4"),
 ("computable","OBJECT+PROCEDURE","M §2.18"),
 ("falsification test","LAW+PROCEDURE","M §30.6"),
]

PARTS = ["OBJECT", "LAW", "PROCEDURE", "REFERENCE"]

def tally(L, name):
    w1 = {p: [] for p in PARTS}
    w2 = {}
    for t, p, src in L:
        if "+" in p:
            w2.setdefault(frozenset(p.split("+")), []).append(t)
        else:
            w1[p].append((t, src))
    print(f"\n  {name} -- {len(L)} terms, none of them chosen by me")
    for p in PARTS:
        print(f"    weight-1 on {p:<11} {len(w1[p]):>3}")
    print(f"    weight-2 (relations)      {sum(len(v) for v in w2.values()):>3}")
    return w1, w2

def treewidth(nodes, E):
    best = len(nodes)
    for order in itertools.permutations(nodes):
        adj = {n: set() for n in nodes}
        for e in E:
            a, b = tuple(e); adj[a].add(b); adj[b].add(a)
        w = 0
        for v in order:
            nb = adj[v]; w = max(w, len(nb))
            for a, b in itertools.combinations(nb, 2):
                adj[a].add(b); adj[b].add(a)
            for u in nb: adj[u].discard(v)
            del adj[v]
        best = min(best, w)
    return best

with State("refute") as st:
    A = step(st, "tally The Method's Index", lambda: tally(L1, "L1  The Method 1.4, back-matter Index"), budget=20)
    B = step(st, "tally Transitions' coordinate tables", lambda: tally(L2, "L2  Transitions, coordinate and audit tables"), budget=20)

w1a, w2a = tally(L1, "L1  The Method 1.4, back-matter Index")
w1b, w2b = tally(L2, "L2  Transitions, coordinate and audit tables")

print("\n\n  REFUTATION 1 -- is REFERENCE a relation wearing a node's clothes?\n")
print(f"    REFERENCE-only terms in The Method's own Index : {len(w1a['REFERENCE'])}")
print(f"    REFERENCE-only terms in Transitions' tables    : {len(w1b['REFERENCE'])}")
for t, s in w1b["REFERENCE"]:
    print(f"        {t:<26} {s}")
overlap = {t for t, _ in w1b["REFERENCE"]} & {t for p in PARTS[:3] for t, _ in w1a[p] + w1b[p]}
print(f"\n    of those, already content of another part      : {len(overlap)}  {sorted(overlap) or ''}")

print("\n  REFUTATION 2 -- is any of the six edges unwitnessed?\n")
E = set(w2a) | set(w2b)
allpairs = {frozenset(p) for p in itertools.combinations(PARTS, 2)}
for p in sorted(allpairs, key=lambda s: sorted(s)):
    wit = (w2a.get(p, []) + w2b.get(p, []))
    print(f"    {' — '.join(sorted(p)):<26} {'witnessed by ' + ', '.join(wit) if wit else '*** NO RELATION TERM ***'}")
missing = allpairs - E
print(f"\n    edges with no relation term: {len(missing)}  {sorted(map(sorted, missing))}")
print(f"    complete: {len(E) == 6}   width/treewidth: {treewidth(PARTS, E) if len(E)==6 else treewidth(PARTS, E)}")
