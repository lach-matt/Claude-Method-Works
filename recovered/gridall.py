print("="*100)
print("  THE GRID METHOD ON EVERY OPEN QUESTION")
print("="*100)
print("""
  For each open item, lay out what an ANSWER would require, mark what is
  occupied, and read the empty cells. **The method's value at §23.4 was that
  eight empty cells collapsed to one missing object.**
""")
Q={}
Q['B — Paschen & Götze §III / Runge 1926']=dict(
 rows=["the document exists","it is public domain","a scan exists","the scan is text-searchable",
       "the section is read","its content is compared to Ch.16"],
 cells=["YES — Springer 1922, cited","YES — since 2017","YES — Springer Book Archives",
        "","",""])
Q['C — nine unentered literatures']=dict(
 rows=["the literatures are named","the search vocabulary is known","each is entered",
       "precedence is settled per claim","the register is updated"],
 cells=["YES — §22.7","YES — excess width, Newton decrement, partial identification, zero-error capacity","","",""])
Q['D — E(X) of Kreuzer–Skarke']=dict(
 rows=["the data is published","a readable copy is obtained","the 30,108 pairs are parsed",
       "E(X) is computed","the result is compared to Λ"],
 cells=["YES — KS 2000, 30,108 pairs","","","",""])
Q['E — the target-spin axis']=dict(
 rows=["the omission is identified","the new coordinate is defined","the extended lattice is built",
       "closure is tested","E(X) is computed","the physical meaning is stated"],
 cells=["YES — §7.10","YES — target 2S, capped as parent 2S is","","","",""])
Q['A — Sc VI 6s']=dict(
 rows=["the channel is constructed","the bracket is committed","the prediction is deductive",
       "the falsification is graded","the level is MEASURED"],
 cells=["YES — δ(4s), δ(5s)","YES — C.2.13, [735,860 · 737,380]",
        "YES — monotone + convex","YES — lower edge tests monotonicity, upper tests convexity",""])
Q['F — reorderability at d ≥ 3']=dict(
 rows=["characterisation","decision procedure","YES certificate","NO certificate",
       "obstruction family","construction rules","hardness","the data structure"],
 cells=["","","YES — an order, O(|X|²)","unbounded (Tucker)","unbounded — route CLOSED",
        "YES — six preserving","",""])
for name,D in Q.items():
    print("="*100)
    print("  "+name)
    print("="*100)
    occ=sum(1 for c in D['cells'] if c)
    print("\n  %-42s%s"%("requirement","status"))
    print("  "+"-"*92)
    for r,c in zip(D['rows'],D['cells']):
        print("  %-42s%s"%(r,c[:48] if c else "·  EMPTY"))
    print("\n     occupied %d of %d      **empty %d**"%(occ,len(D['cells']),len(D['cells'])-occ))
    em=[r for r,c in zip(D['rows'],D['cells']) if not c]
    if em:
        first=em[0]
        print("     **first empty cell : %s**"%first)
        print("     everything below it is downstream of that one.")
print("="*100)
print("  WHAT THE METHOD SHOWS ACROSS ALL SIX")
print("="*100)
print("""
  | item | first empty cell | kind of obstacle |
  |---|---|---|
  | A  Sc VI | the level is MEASURED | **an instrument** |
  | B  Paschen & Götze | the scan is text-searchable | **an artefact of digitisation** |
  | C  literatures | each is entered | **labour** |
  | D  Kreuzer–Skarke | a readable copy | **a file format** |
  | E  target spin | the extended lattice is built | **labour** |
  | F  reorderability | characterisation at d ≥ 3 | **a missing OBJECT** |

  > **Five of the six are blocked by something OUTSIDE the index: an
  > instrument, a scan, a file, and two units of work.** Only F is blocked
  > by something that does not exist yet.

  **That is a sharper statement of |Q| = 6 than the section makes.** It
  currently says 'four external, one construction, one mathematical'. The
  grid says: **four are retrievable, one is buildable, and one requires a
  new object.**

  **And it says which to do first.** C, D and E have their first empty cell
  reachable by labour alone. **Three of six could be closed without any new
  idea**, which the section does not say.
""")