print("="*90)
print("  ALL BOUNDS ON §23.4, RE-EVALUATED AGAINST WHAT NOW EXISTS")
print("="*90)
rows=[
("chain of row supports is sufficient","SUFFICIENT, 2,649 instances","STANDS — and now explained: a chain is the Young-diagram case of the two-sided condition"),
("Γ-free / totally balanced necessary","NECESSARY","STANDS, subsumed — C1P is the sharper form and implies it"),
("C1P necessary","NECESSARY, 0 FN in 2,500","**PROMOTED** — with monotone endpoints it is the CHARACTERISATION, proved"),
("width ≤ 2 per container","NECESSARY","STANDS, and is now a corollary: three incomparable rows cannot reach two ends"),
("≤ 2 immediate children","NECESSARY","STANDS, same corollary at one level"),
("end-assignment 2-SAT","NECESSARY","**SUPERSEDED** — it is the projection form of the path constraint"),
("path 2-SAT on the tree","NECESSARY","**SUPERSEDED** — correct in form, failed on the tree, not the logic"),
("containment 2-SAT on the poset","NECESSARY, 0 FN","**EXPLAINED** — loses the overlap axis; §13.4 predicts it"),
("pointwise containment 2-SAT","NECESSARY, 0 FN","**EXPLAINED** — intersects more projections, still a projection"),
("overlap components ≤ 2","NECESSARY","STANDS"),
("row/column-deleted sub-instances","NECESSARY, derived from §13.4","STANDS — a GENERATOR, not a single condition"),
("no constant-depth local descent","NEGATIVE","STANDS — stall rate rises with size"),
("backtrack-free methods excluded","NEGATIVE","**REFINED** — as filters they decide 57.6% correctly"),
("descent complete after the cascade","CONJECTURE","**REFUTED** — 1.54% missed at three restarts"),
("no strict nesting ⟺ monotone endpoints","EQUIVALENCE, 20,000/20,000","**PROVED**, Lemma 3"),
("closure ⟺ intervals + monotone","EQUIVALENCE","**PROVED**, Lemmas 1–2"),
("no row spans two P-node children","STRUCTURAL, 1,167 instances","**NEW, VERIFIED** — makes the reduced search sound"),
("reduced search k(k−1) per P-node","PROCEDURE","**NEW, EXACT** on 2,164 instances, median 1 frontier"),
("frontier-correct ⇏ anchor-complete","STRUCTURAL","**NEW NEGATIVE** — the finding nine tree attempts each rediscovered"),
("steps ~ d², slope 1.97 mean / 2.12 max","MEASUREMENT","**STRENGTHENED** — 4,124 instances, six points, constant not growing"),
("§13.4 forbids any projection criterion","THEOREM, cited","**THE ORGANISING BOUND** — accounts for 11 of the above"),
]
print("\n  %-40s%-30s%s"%("bound","was","now"))
print("  "+"-"*118)
for a,b,c in rows: print("  %-40s%-30s%s"%(a[:40],b[:30],c[:60]))
import collections
k=collections.Counter()
for a,b,c in rows:
    if c.startswith("**PROVED") or c.startswith("**NEW, VERIFIED") or c.startswith("**NEW, EXACT"): k['promoted']+=1
    elif c.startswith("**REFUTED"): k['refuted']+=1
    elif c.startswith("**SUPERSEDED"): k['superseded']+=1
    elif c.startswith("**EXPLAINED"): k['explained']+=1
    elif c.startswith("**PROMOTED") or c.startswith("**STRENGTHENED") or c.startswith("**REFINED") or c.startswith("**NEW NEGATIVE"): k['strengthened']+=1
    else: k['unchanged']+=1
print("\n     promoted to proof/verified : %d"%k['promoted'])
print("     strengthened or refined    : %d"%k['strengthened'])
print("     explained by §13.4         : %d"%k['explained'])
print("     superseded                 : %d"%k['superseded'])
print("     refuted                    : %d"%k['refuted'])
print("     unchanged                  : %d"%k['unchanged'])
print("="*90)
print("  WHAT THE RE-EVALUATION SHOWS")
print("="*90)
print("""
  **The eleven necessary conditions did not survive as eleven results.**
  Two became a proved characterisation; two were superseded by the form
  they were approximating; two are explained as projections; the rest are
  corollaries of one theorem.

  > **§13.4 is the organising bound.** It accounts for every projection
  > failure, and it predicted the outcome of every attempt made after it
  > was found — including the four made since.

  **Three genuinely new bounds appeared today**, and one of them is a
  negative that nine implementations each rediscovered separately:

     no row spans two P-node children            — verified
     the reduced search is exact                 — verified
     **frontier-correct does NOT imply anchor-complete** — the reason
     every traversal failed, and not visible until the tree was verified
     against the right property

  **And one conjecture was refuted rather than left standing**: the
  descent is not complete after the cascade.
""")
print("="*90)
print("  THE BOUND THAT REMAINS UNTESTED")
print("="*90)
print("""
  Every bound above is about d = 2. **§23.4's slice-chain result says the
  d = 2 condition does not lift, and nothing since has tested d ≥ 3
  against the corrected theory.**

  > **The characterisation is proved for d = 2 and unexamined above it.**

  That is the largest untested claim in the section, and it was true before
  today and is still true.
""")