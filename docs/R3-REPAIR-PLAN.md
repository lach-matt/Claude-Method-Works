# R3-REPAIR-PLAN — the 25 live-superseded findings, as items to approve or refuse

**This is a proposal. Nothing here has been done.** The chat-67 full hold governs: a finding is
recorded, never repaired. `RETRACTION-AUDIT.tsv` is the finding; this is what repairing it would
*mean*, item by item, so the decision is yours and is made once per item rather than once for the
list.

**Each item states: the site, what stands there now, what the correction replaces it with, the
proposed action, and the grade.** A `MEDIUM` item also says what would settle it — approving a
MEDIUM without settling it is a judgement, not a repair.

## The two mechanics, and they are the corpus's own

`DEFERRED.md` states the split, on exactly this class of finding:

> *"Register 523 is append-only and is **corrected by 1790, not edited** (Ruling 29 does not apply —
> this is not a pointer removal). **R3 repairs the two main-volume sites.**"*

and again:

> *"Register 547 and Register 548 disagree in the same way … and both are append-only, so **a new
> entry citing both is the only correction path**."*

So:

- **Batch A — volume sites (9 rows, 7 findings).** `The_Method_1_6-2.md`, `Transitions.md` and the
  companions are **repaired in place** by R3.
- **Batch B — Register sites (17 rows, 13 findings).** A Register entry is **never edited**. The
  repair is a **new appended entry** that cites the superseded one. The Register does annotate
  superseded entries with a `WARNING:` block naming the correcting entry — 38 entries carry one, and
  `**SUPERSEDED` appears 70 times — so whether the annotation accompanies the append is a question
  for you, not a default I have assumed.

**Batch A is the smaller and the more certain, and it is where I would start.**

---

## Batch A — volume sites, repaired in place

### A1 · `PO-0019` / `PO-0080` — 2,475 cells · **HIGH** · already docketed

**Sites:** `The_Method_1_6-2.md` **L914** and **L3434** assert it; **L3477** withdraws it.

> L3477: *"…it breaks the factorisation by **15,150 cells at Λ₁₂ and 45,450 at Λ₁₃**, 21.4% and
> 22.8% of the product — recomputed; **the 2,475 previously printed here is withdrawn**."*

**The volume prints its own withdrawal and asserts the withdrawn figure twice more.** The correction
records the price as wrong by roughly a factor of six. *"Previously printed **here**"* is the tell:
the passage being edited was fixed and the other two were not.

**Proposed:** replace 2,475 at L914 and L3434 with the recomputed 15,150 / 45,450 figures, keeping
each sentence's own framing. L3477 needs no change.

**Grade HIGH.** This needs no external evidence — it is a self-contradiction inside one file.

### A2 · `PO-0019` — register 230's row cited as current · **MEDIUM**

**Site:** `The_Method_1_6-2.md` **L3433–3434** — *"§A.15 and register 230 record what it costs,
2,475 cells of the cylinder."*

**Proposed:** the citation survives; the figure does not. Either update the figure and keep the
pointer, or drop the appeal to 230 as authority for a superseded number. **Settled by** A1 and by
whether register 230 is itself corrected in Batch B.

### A3 · `PO-0081` — the closure rule is printed one-sided · **HIGH**

**Sites, all unmarked:** `Transitions.md` **L202** (§1.8) · `The_Method_1_6-2.md` **L11379**
(App F.4.3, `A.rule`) · `The_Method_1_6___The_Index_of_Indices-2.md` **L2022** ·
`The_Method_1_6___Mathematical_Compendium-2.md` **L516**.

All four print: *"A tightening preserves E = 0 if and only if it binds one coordinate by a monotone
function of one other."* **Register 402 states the correction outright** — *"THE CLOSURE RULE WAS
ONE-SIDED AND THE OPERATOR IS TWO-SIDED … a band closes at E = 0 where the stated rule refuses it."*

**Proposed:** replace the one-sided `iff` at all four sites with the corrected form — *a tightening
preserves E = 0 iff each of its binary projections is the intersection of that projection's own two
upper envelopes* — and cite 402.

**Grade HIGH**, and it is the widest-reach item here: four volumes state a rule the Register has
already corrected. **Note** `DEFERRED.md` docket 9(a) touches L11379 for a *pointer* fault; that is a
different repair at the same line and the two should be done together.

### A4 · `PO-0013` — "descend from two origins" · **HIGH** · already `10-04` in `READ-ch10.md`

**Site:** `The_Method_1_6-2.md` **L2049**.

The main volume gives the correlation an origin-count cause; the Mathematical Compendium gives the
real one — two decreasing functions of one width variable, Chebyshev's sum inequality, *"positive for
this reason and no other."*

**Proposed:** replace the origin-count explanation at L2049 with the Chebyshev cause, or cite the
Compendium rather than restating a cause. **Volume against volume**, so one of the two must move.

### A5 · `PO-0091` — "the whole tower" · **MEDIUM** · partly docketed

**Sites:** `The_Method_1_6-2.md` **L5751** (Figure 21.1 caption) and **L5773** (§21.5.3 table);
Register **1953** repeats it.

The same caption says the base Λ₈ *is a caterpillar* and that cycles enter at Λ₁₀; MC L1644 gives Λ₈
as *"8 nodes, 7 edges, a caterpillar; treewidth 1"*; MC L1324 states **treewidth 1 ⟺ exact closure
under ℛ**. By the volumes' own figures ℛ is exactly sufficient at Λ₈.

**But register 1790, a banked correction, re-asserts the scope** — *"its treewidth is still 2, so
§21.5.1's ONE-LEVEL SHORTFALL STANDS"* — while its own stage table gives cycle rank `(0,0,1,1,2,2)`,
so Λ₈ and Λ₉ carry no cycle.

**Proposed:** *do not edit either site yet.* **Settled by** a ruling on what "the tower" quantifies
over: if it includes Λ₈, the scope claim is wrong and both sites narrow to Λ₁₀ and above; if the
sentence means the cyclic stages only, it needs saying. **This is the one item where a repair could
make the volume contradict a later correction**, so it should be ruled before it is edited.

### A6 · `PO-0158` — "not a lattice" where only "not a sublattice" was shown · **MEDIUM**

**Sites:** `The_Method_1_6-2.md` **L3375**; `The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md`
**L79** (Law 3) and **L157**.

Componentwise meet/join failure refutes sublattice-hood *of the product*, not lattice-hood — a
distinction the corpus holds elsewhere (`READ-ch16b.md`: *"zero join leaks, zero meet leaks — Λ₈ is a
sublattice"*; MC L516: *"the index is a sublattice of a product of chains"*).

**Proposed:** narrow the three sentences from *"is not a lattice"* to *"is not a sublattice of the
product"*. **Settled by** checking whether any downstream claim depends on the stronger reading; the
counts themselves are unaffected.

### A7 · `PO-0015` — the seed bit-table properties · **MEDIUM**

**Site:** `The_Method_1_6-2.md` near **L4074**, the registers 602–605 passage.

The correction says properties 1–3 are *refuted at the Λ₈ cap itself*, not merely "untested at other
caps". **Proposed:** restate as refuted, and drop "untested at other caps". **Settled by** the exact
enumeration in Batch B item B5 — the two are one finding seen from two volumes.

### A8 · `PO-0190` — register 314's supporting evidence · **MEDIUM**

**Site:** `The_Method_1_6-2.md` **L314-region** (one occurrence) and the Mathematical Compendium
phrase the audit mis-attributed to main (recorded in `docs/RETRACTION-AUDIT.md`).

**The correction is explicit that the general claim SURVIVES** — *"an axis can be exact and not
composable; none is composable and not exact"* — and only the supporting evidence falls: Λ₁₀ was
never structurally barred and Λ₉ is not alone.

**Proposed:** keep the claim, narrow the evidence. **This is the item most easily over-repaired**; a
reader who repairs the headline rather than the evidence would delete a result that stands.

---

## Batch B — Register sites, corrected by a new appended entry

Thirteen findings, 17 rows. **No existing entry is edited.** Each proposed entry cites the entry it
corrects; whether a `WARNING:` annotation is also added to the old entry is your call, and the
Register does it 38 times elsewhere.

| # | id | entry | grade | what stands | what the correction says |
|---|---|---|---|---|---|
| B1 | `PO-0051` | **1450** | HIGH | Belokolos 2017 credited for the period-two result | Kitagawara & Barut 1983 predates it by 34 years; Kitagawara appears **0** times in the corpus, Belokolos 8 |
| B2 | `PO-0087` | **500**, 502, 0.980 | HIGH / MED | κ = 0.2506·S − 0.765 at correlation +0.980; 502 reads THE PREDICTION HELD | the whole κ apparatus is withdrawn — *"six cycles of expressions were measuring the heuristic"* |
| B3 | `PO-0105` | **0.922** | HIGH | `k = 0.9220 ± 0.0324`, `k = 1 EXCLUDED at t = −2.41` | the functional form it rests on is refuted; b is a proxy for δ_neutral and adds nothing |
| B4 | `PO-0006` | **164** | HIGH | the Register begins at entry 1 | **the correction is the stale record** — see below |
| B5 | `PO-0015` / `PO-0026` | **602** | MED | *"219 distinct minimum covers; the same four cells appear in every one"* | 219 was a biased randomised sample; exact enumeration gives **24,585** covers, only corner 3 common |
| B6 | `PO-0074` | **64,290** | MED | *"the tower above Λ₈ runs to 64,290 at Λ₁₃"* (§646) | 22,275 / 64,290 are the exact-triangle law build, not the tower's own Λ₁₃ |
| B7 | `PO-0094` | **599** | MED | statistics standing as a sixth language | a language that cannot state a defect is not a sixth language |
| B8 | `PO-0101` | **807** | MED | the testable claim framed as *"δ falls monotonically"* | the law is *"δ approaches δ₀ monotonically"*, direction `sign(δ₂)` — 804–807 tested the wrong claim |
| B9 | `PO-0107` | **1148** | MED | *"A STRUCTURAL FLAW REMAINS"* on δ = 2.38 > B = 2 | a floor-comparison error: channels with `⌊δ⌋ > B` are **0 of 311** |
| B10 | `PO-0124` | **1.732** | MED | `t(ℓ) = √(ℓ(ℓ+1)/2)` confirmed | measured 1.6214 against predicted 1.732 — right at p, wrong at both ends; two points fitted |
| B11 | `PO-0128` | **1395** | MED | *"THE RESIDUAL IS ELEVEN NAMED CELLS"* | at the correct limit the split is **38 beyond, 20 within**; the extra nine are elements 109–118 |
| B12 | `PO-0136` | **1461** | MED | the atomic order **is** additively representable | retracted by applying that entry's own imported warning to itself |
| B13 | `PO-0145` | **1595**, 1628 | MED | a per-host-and-path fetch cache; 1628 adds a second mechanism | *"There is no cache. There never was."* — and there is one mechanism, not two |

**B4 is not a repair and must not be treated as one.** `PO-0006` is the file's single
`CORRECTION-SUPERSEDED` row: the chat correction claims the Register never held entries 1–164, but
**Ruling 66 later seated the genesis block flat**, so the Register does begin at 1 and the volume is
right. The action is to record the correction as superseded — nothing in the Register changes. It is
in this list only because a reader scanning for `SUPERSEDED` will find it.

**Register 1395's `WARNING`** (B11) is the one flagged entry that already carries a marker, which is
why `docs/RETRACTION-AUDIT.md` downgrades `PO-0128`. It may need no new entry at all — read the
existing `WARNING` first.

---

## What this plan does not propose

- **The 7 `CANNOT-TELL` rows.** Genuinely two-sided; the volume both corrects and retains. They need
  reading, not repairing, and are not in this plan.
- **The 187 `UNRELATED` rows.** Digit coincidence, dismissed on ±260 characters of context. Cheap to
  spot-check, and not repair candidates.
- **The 29 `NOT-IN-VOLUMES` rows.** Absent from the nine volumes ≠ absent from the repo; the
  governance tree sits outside them.
- **Any edit to `graphify-out/`, `recovered/` or `extracted/`.** Generated trees are regenerated.
- **Anything at all, until you approve it.** Approve by item number; a batch approval is fine but the
  MEDIUMs each carry a condition and A5 carries a ruling.

## Order I would work them

1. **A1** — self-contained, HIGH, two lines, and the file already disagrees with itself.
2. **A3** — HIGH and the widest reach, four volumes; do it with `DEFERRED` docket 9(a).
3. **A4** — HIGH, volume against volume, one of the two must move.
4. **B1, B2, B3** — HIGH Register appends, each a single new entry.
5. **A6, A7 + B5** — the same finding from both sides; do them together or not at all.
6. **The remaining MEDIUM Batch B appends**, each after its condition is met.
7. **A5 last**, and only after a ruling — it is the one item where repairing could put the volume in
   conflict with a later correction.

## Re-verification

```bash
# the 25, with their sites and grades
awk -F'\t' 'NR==1 || $4 ~ /SUPERSEDED/ {print $1"\t"$4"\t"$5"\t"$3"\t"$6}' RETRACTION-AUDIT.tsv

# A1: the volume contradicting itself
grep -n '2,475' method/members/The_Method_1_6-2.md          # L914, L3434 assert; L3477 withdraws

# A3: four sites, and the register that corrects them
grep -rn 'binds one coordinate by a monotone' method/members/*.md
grep -n 'THE CLOSURE RULE WAS ONE-SIDED' method/members/The_Method_1_6___The_Register-2.md

# the append-only rule this plan is built on
grep -n 'append-only' method/members/DEFERRED.md
```
