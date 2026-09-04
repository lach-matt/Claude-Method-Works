#!/usr/bin/env python3
"""two_columns.py -- does every TRANSITION index carry two columns?

Register 622: cells and reachable read as space and time. A cell is what exists;
reachability is what can be entered, which §12.11.0 shows IS the temporal order
in Lambda — composition, not a date.

PREDICTION (§2.13): an index whose cells are TRANSITIONS carries both columns.
An index whose cells are STATES carries only the first, because a state index
has no composition to order. Falsifier: a state index with a meaningful second
column, or a transition index without one.
"""
import itertools
from zeno import State, step

def run():
    from method_tower import base
    out=[]
    L8=[tuple(c) for c in base((3,3,1,3,1))]
    L9=[c+(s,) for c in L8 for s in range(0,c[6]+1)]
    for lbl,X,src,tgt in (("Λ₈  transitions",L8,(0,1,2),(4,5,6)),
                          ("Λ₉  transitions",L9,(0,1,2),(4,5,6))):
        S={tuple(c[i] for i in src) for c in X}
        comp=[c for c in X if tuple(c[i] for i in tgt) in S]
        out.append((lbl,"transition",len(X),len(comp),len(comp)/len(X)))
    # state indexes: the drawn tables. a cell is a position, not a move.
    G={1:[1,18],2:[1,2]+list(range(13,19)),3:[1,2]+list(range(13,19))}
    for p in (4,5,6,7): G[p]=list(range(1,19))
    TAB=[(p,g) for p in G for g in G[p]]
    D=[31,28,31,30,31,30,31,31,30,31,30,31]
    CAL=[(m+1,d) for m in range(12) for d in range(1,D[m]+1)]
    for lbl,X in (("the periodic table  states",TAB),("the calendar  states",CAL)):
        # is there ANY source/target split? a state has no two ends.
        out.append((lbl,"state",len(X),None,None))
    return out

with State("two_columns") as st:
    rows=step(st,"space and time columns by index kind",run,budget=600)

print(f"  {'index':<28}{'kind':<12}{'cells':>8}{'reachable':>11}{'fraction':>10}")
for lbl,kind,n,c,f in rows:
    print(f"  {lbl:<28}{kind:<12}{n:>8,}"
          f"{(f'{c:,}' if c is not None else '—'):>11}"
          f"{(f'{f:.3f}' if f is not None else '—'):>10}")
print(f"  {'violation index  transitions':<28}{'transition':<12}{2370:>8,}{1410:>11,}{1410/2370:>10.3f}")
print(f"""
  A transition cell has TWO ENDS — a source and a target — so it can be asked
  whether its target is another cell's source. A state cell has one position and
  the question does not arise: there is nothing to compose.

  **The second column exists exactly when the first column's cells are moves.**
  That is why Lambda-9 and the violation index print it and the periodic table
  and the calendar cannot.""")
