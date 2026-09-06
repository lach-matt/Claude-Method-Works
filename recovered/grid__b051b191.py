from itertools import product
print("="*94)
print("  §23.4 AS AN INDEX — WHAT IS OCCUPIED, AND WHAT THE STRUCTURE ADMITS")
print("="*94)
ROWS=["characterisation","decision procedure","YES certificate","NO certificate",
      "obstruction family","construction rules","hardness","the data structure"]
COLS=["d = 2","d = 3","d ≥ 4"]
CELL={
 ("characterisation","d = 2"):"PROVED — C1P + monotone endpoints",
 ("characterisation","d = 3"):"",
 ("characterisation","d ≥ 4"):"",
 ("decision procedure","d = 2"):"linear (Booth & Lueker) + a sort",
 ("decision procedure","d = 3"):"",
 ("decision procedure","d ≥ 4"):"",
 ("YES certificate","d = 2"):"an order, O(|X|²)",
 ("YES certificate","d = 3"):"an order, O(|X|²)",
 ("YES certificate","d ≥ 4"):"an order, O(|X|²)",
 ("NO certificate","d = 2"):"Tucker submatrix — UNBOUNDED family",
 ("NO certificate","d = 3"):"unbounded (inherits Tucker)",
 ("NO certificate","d ≥ 4"):"unbounded (inherits Tucker)",
 ("obstruction family","d = 2"):"Tucker 1972 — M_I, M_II, M_III",
 ("obstruction family","d = 3"):"census to 6 cells; UNBOUNDED, route closed",
 ("obstruction family","d ≥ 4"):"unbounded",
 ("construction rules","d = 2"):"6 preserving, disjoint union fails",
 ("construction rules","d = 3"):"6 preserving, disjoint union fails",
 ("construction rules","d ≥ 4"):"6 preserving, disjoint union fails",
 ("hardness","d = 2"):"P — the CSP is binary",
 ("hardness","d = 3"):"",
 ("hardness","d ≥ 4"):"",
 ("the data structure","d = 2"):"PQ-tree",
 ("the data structure","d = 3"):"",
 ("the data structure","d ≥ 4"):"",
}
print("\n  %-20s%-36s%-30s%s"%("",COLS[0],COLS[1],COLS[2]))
print("  "+"-"*116)
for r in ROWS:
    print("  %-20s%-36s%-30s%s"%(r,
        CELL[(r,"d = 2")][:34] or "·",
        CELL[(r,"d = 3")][:28] or "·",
        CELL[(r,"d ≥ 4")][:26] or "·"))
empty=[(r,c) for r in ROWS for c in COLS if not CELL[(r,c)]]
print("\n     occupied : %d of %d      **empty : %d**"%(24-len(empty),24,len(empty)))
print("="*94)
print("  WHAT THE EMPTY CELLS ARE")
print("="*94)
for r,c in empty: print("     %-22s %s"%(c,r))
print("="*94)
print("  AND WHAT THE STRUCTURE SAYS ABOUT THEM")
print("="*94)
print("""
  **Read the rows that are FULL.** Three rows are complete across every
  column:

     YES certificate     — an order, at every d
     obstruction family  — unbounded, at every d
     construction rules  — six preserving, at every d

  **Those three needed no d-specific work.** They were established once and
  they hold everywhere. **The book's own mechanism supplied them: closure
  under construction, and the certificate is the order itself.**

  **Now read the empty cells.** All seven sit in two rows and one column
  pattern:

     characterisation / procedure / hardness / data structure  at d ≥ 3

  > **Every empty cell is downstream of ONE missing object: the d ≥ 3
  > analogue of a PQ-tree.** Supply it and the characterisation follows (as
  > it did at d = 2), the procedure follows from the structure, and the
  > hardness classification follows from the procedure's cost.

  **That is what the grid shows and what hunting obscured.** Twenty-two
  formulations were attempts on four cells that all depend on one.
""")
print("="*94)
print("  AND ONE CELL THE GRID SAYS SHOULD EXIST AND NOBODY ASKED FOR")
print("="*94)
print("""
  **The construction-rules row is full and the characterisation row is
  nearly empty.** But a construction grammar IS a characterisation — of the
  reachable objects rather than of all objects.

  > **The cell that presents itself: 'which sets are reachable by the six
  > preserving rules?' That is a characterisation at every d, and it is
  > exactly the question an INDEX answers rather than an algorithm.**

  Λ is reachable. **The open problem asks about sets that are not**, and the
  book never needed those.
""")