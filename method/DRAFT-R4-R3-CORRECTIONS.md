# DRAFT R4 — the R3 corrections rulings 2, 3, 9, 10, 11 and 12 authorise: **every site measured, every substitution written, and NOTHING DONE.**

`RULINGS-R4f` §5 item 3, prepared for approval. This is a **specification, not a repair** — no volume,
member, bundle or ledger is touched by it, and the chat-67 hold stands until M rules item by item.
Prepared 6 September 2026 on M's *"continue"*, following the discharge of §5 items 1 and 2.

Every line number below is MEASURED in the live pair — **BUILD110 main** (`e1264def…`) and **BUILD232
compendia** (`199df633…`) — by extracting each member with `verify.py`'s own regex and counting lines in
the member, not the bundle. Every substitution anchor was counted: **all three are unique in the whole
main bundle**, so a count-asserted substitution cannot land twice.

---

## 1. The six rulings do not form one class, and treating them as one would be the error

| ruling | site | class | can it be executed on the rulings already given? |
|---|---|---|---|
| **11** §34.4 "No parameter is fitted" | main §34.4 | Batch A | **YES** — one substitution, mechanical |
| **12** the g-block bound | main §35.2, §35.5 (+ siblings) | Batch A + B | **YES for §35; the siblings need a ruling** |
| **2** La's 5d entry point | main §34.7, registers 1334/1337 | Batch A + B | **NO — see §3** |
| **3** the f test and 1337 | main §34.7, register 1337 | Batch B | **NO — same site as ruling 2** |
| **9** 34re-04 withdrawn | no volume site | disposition | **YES — but the mechanic is a question** |
| **10** D-61 withdrawn | no volume site | disposition | **YES — same question** |

**Rulings 1, 2, 3, 5 and 9 all land on the same two objects — §34.7 and register 1337.** They are one
repair, not five, and §3 below is why it cannot be executed as a mechanical substitution.

---

## 2. READY — the two that are mechanical

### 2A · Ruling 11 · §34.4 takes "in the form"

**Site.** `The_Method_1_6-2.md` **L9602**, under `### 34.4 The rule` (heading at L9584). Anchor unique
in the bundle (1 occurrence); the bare string `No parameter is fitted` occurs **3×** in the volume —
L9602 (§34.4), L9693 (§34.8, which already carries the qualifier), L9904 (§35.5) — so the anchor must
be the long form and never the bare string.

```
OLD  §34.6 walks *a* through it. **No parameter is fitted**; the provenance of every term is §34.8's
NEW  §34.6 walks *a* through it. **No parameter is fitted in the form**; the provenance of every term is §34.8's
```

**Guard.** count = 1 asserted before and after; reverse substitution must recover md5
`e1264def2a04df9ac010db3f0ea90953`.
**Scope note, and it matters.** Ruling 11 names **§34.4**. **§35.5 L9904** — *"No parameter is fitted.
No observation enters upstream of the score."* — is a different chapter and is **NOT in scope**; it is
listed here so that leaving it alone is visibly a decision and not an oversight.

### 2B · Ruling 12 · the g-block bound takes the wider reach

**The measured bound.** `RULINGS-R4e` §4: carrying `a` = 1.9840594 out of lawrencium and re-fitting it
nowhere, `method/proofs/forward.py` walks the law forward seventeen elements. **Through Z = 125 the law
never makes a g subshell the entrant**, and the reason is exact — a node-free subshell has p = 0, so
ν = n with `a` dropping out; 5g sits at ν = 5 forever while 7d at `a` = 1.98 sits at 3.03. Twelve of
twelve blocks above Z = 108 come out right and there is no reset.

**Site 1 — prose.** `The_Method_1_6-2.md` **L9797**, under `### 35.2 What the walk returned`:

```
OLD  the field.** There is no g block below Z = 121, and the table did not have to be
NEW  the field.** There is no g block through Z = 125, and the table did not have to be
```

**Site 2 — the provenance table.** `The_Method_1_6-2.md` **L9898**, under `### 35.5 The provenance`:

```
OLD  | **no g block below 121** | the pinned channels, −1/(2n²) |
NEW  | **no g block through 125** | the pinned channels, −1/(2n²) |
```

**Guard.** Both anchors unique in the bundle; count = 1 each; reverse-md5 as above.

**Two main-volume sites are NOT edited, and each for a stated reason.** **L9874** (§35.4) says *"the
finding that there is no g block"* with no bound at all — nothing to widen. **L10839** (Appendix D.5.9)
is an index row reading `LS.pin the pinned-channel theorem, no g block` — also unbounded.

---

## 3. BLOCKED — §34.7 and register 1337, where five rulings converge

### 3A · What ruling 2 actually does to the printed sentence, MEASURED

Register 1337 reads *t* at each opening from the element's **first ionisation energy**. At lanthanum
that removes a **6s** electron, so the printed 5d value is of the wrong electron (`FINDING-R4-15` §3).
The store carries the right number — **La II 6s² ¹S₀ at 52,376 cm⁻¹ = 6.4938 eV**, the 5d electron's
own removal — giving **t(5d) = 1.8049** against the printed **1.7240**. At yttrium nothing moves: Y II's
ground *is* 5s², so Y's first ionisation energy already is the 4d removal.

**And that changes §34.7's headline claim.** Recomputed through `method/proofs/entrypoint.py`, whose
selftest asserts registers 1334 and 1337 value for value:

| | d values | d median | ratio to the p median 1.0284 | against √3 |
|---|---|---|---|---|
| **as printed** (first IE) | 1.8453 · **1.7240** | 1.7846 | 1.735360 | **+0.19 %** |
| **corrected** (own removal) | 1.8453 · **1.8049** | 1.8251 | 1.774712 | **+2.46 %** |

**So the repair ruling 2 orders removes the sentence ruling 9 was asked about.** §34.7 L9675 prints
*"Measured 1.028 at p across four subshells and 1.785 at d across two: the ratio is √3 to 0.19%."*
Under ruling 2 the d figure becomes 1.825 and the ratio 2.46 % — **the √3 agreement does not survive
reading the right electron.** That consequence is not stated in ruling 2 and **is not mine to resolve.**

### 3B · Why it cannot be a mechanical substitution

Five rulings land on this one sentence and its register entry:

- **ruling 1** — the form is a **floor approached from above**; the excess is +4.04 % at p and +5.37 %
  at d, one-signed and growing with ℓ. *"The subject matter is settled by this ruling; the wording is
  the prose pass's, which is M's and comes after"* (`RULINGS-R4c` §3).
- **ruling 2** — the La reading is repaired, which is the table above.
- **ruling 3** — register 1337's *"no f test — no f subshell has a two-sided corridor"* is false under
  the g ruling; 5f has a two-sided corridor and the f test is run.
- **ruling 5** — the volume carries **both** readings, the first-ionisation one it prints and the
  corrected one on the entrant's own electron, with 3p at aluminium and 6p at thallium as figures.
- **ruling 9** — 1.028 is the median, and the 0.25 %/0.19 % split is a rounding artefact.

**A substitution cannot express that.** What §34.7 becomes is a rewritten passage carrying two readings,
a floor statement, an f row and a changed ratio — **prose, which is M's under `RULINGS-R4c` §3 and comes
after the subject matter, not before it.** The subject matter is settled; the wording is not written
here and is not proposed here.

### 3C · The one tension a reading has to resolve, and I have not resolved it

Ruling 5 says both readings are carried. Ruling 2 says the La reading is **repaired**. Those are
compatible only on a reading — that for Al, Ga, In, Tl and Y the first ionisation energy *is* the
entrant's removal, so "both readings" is a genuine pair, while at La the first ionisation energy is not
a 5d datum at all and so is an error rather than an alternative. **That is an interpretation, it is
stated so it can be refused, and nothing is built on it.**

---

## 4. Rulings 9 and 10 — withdrawals, and the mechanic is the open question

Neither touches a volume. **34re-04** (`READ-ch34re.md` L12; `DEFERRED.md` L3333; `DOCKET.md` L319;
cited by `PLAN-R4-ANNEX.tsv` row **F-151**) and **D-61** (`PLAN-R4-ANNEX.tsv` row 140, status
`OPEN` — *"1,585-fold printed vs 1,582.93 at printed precision (two sites) unscored"* — whose cited
source is `DOCKET.md` L279, where the identifier `D-61` itself does not appear) are withdrawn by M's *"yes."*

**All four files are seated members** — `PLAN-R4-ANNEX.tsv` is byte-identical to `members/` — and
**a member is never edited in place.** `DEFERRED.md` and `DOCKET.md` are the two append-only members and
grow only through `close.py --append`. So the disposition has a mechanic question of its own: whether a
withdrawal is recorded by an append to `DEFERRED.md`, by a Register entry, or by a successor annex.
**That is M's, and no file is touched until it is answered.**

---

## 5. The Register appends owed — Batch B

The Register runs **1 to 1835**, so the next free number is **1836**. A Register entry is never edited;
each of these is a **new appended entry citing the superseded one** (`docs/R3-REPAIR-PLAN.md`'s Batch B
mechanic, from `DEFERRED.md`'s own statement of it).

| # | cites | records |
|---|---|---|
| **1836** | 1334, 1337 | the La 5d reading is of the 6s electron; La II 6s² ¹S₀ 52,376 cm⁻¹ gives t = 1.8049; the d median and the √3 ratio move with it |
| **1837** | 1337 | the f test exists under the g ruling — 5f has a two-sided corridor; the value(s) that complete the f subshell corridor |
| **1838** | 1704 | the g-block bound is widened to **through Z = 125** on the forward walk, twelve of twelve blocks and no reset |

**Whether the append also carries a `WARNING:` block on the superseded entry is M's** —
`docs/R3-REPAIR-PLAN.md` records that 38 entries carry one and `**SUPERSEDED` appears 70 times, so the
annotation is precedented but is **not** assumed here. **The numbers, order and wording of all three
entries are M's**; the rows above are what each must record, not a draft of it.

---

## 6. What the gate costs — measured, and it is the reason a build is guarded

Batch B costs nothing: a new appended entry leaves 1337's text untouched, so `r2-ch16y` — which
hard-codes `d_open = [D('1.8453'), D('1.7240')]` at L72 against register 1337 — still passes unchanged.

**Batch A breaks live goldens, and these are they:**

| golden | what it asserts | broken by |
|---|---|---|
| `r2-ch17a2` | L117 prints *"no g block below Z = 121"*; L167 matches `below Z = 121\|Z = 121` | **ruling 12** |
| `r2-ch17c2` | L186–187 count *"below 121\|below Z = 121"* across the six volumes | **ruling 12** |
| `r2-ch17d2` | L130 matches `no g block` (substring survives; the site count does not) | **ruling 12** |
| `r2-ch34re2` | L300/L310 key §34.4 and §34.8 by line for *"No parameter is fitted"* | **ruling 11** |
| `r2-ch16z3` | L182 keys the same claim | **ruling 11** |
| `r2-ch16x2` | L163 carries it in a fixed list | **ruling 11** |

Each is re-banked with `gate.py bank` **after** the build and **as part of it**, never separately, and
`tools/gate_live.py` must return **86 OK, 0 FAIL** before the close. `python3 method/verify.py` must
return VERIFY OK on the new pair.

---

## 7. The sibling sites ruling 12's own rule reaches, and they are a question

Ruling 12 names §35 and then generalises: *"where two true statements differ only in reach, the volume
takes the more expanded one."* Four sites outside §35 print the Z = 121 bound:

| member | line | text |
|---|---|---|
| `THE-LOWDIN-SOLUTION-2.md` | **L13** | *"proves that no g block exists anywhere below Z = 121"* |
| `THE-LOWDIN-SOLUTION-2.md` | **L47** | *"there is no g block anywhere below Z = 121"* |
| `THE-LOWDIN-SOLUTION-2.md` | **L114** | *"The absence of a g block below Z = 121 is not an accident"* (§V.3) |
| `The_Method_1_6___Mathematical_Compendium-2.md` | **L3182** | *"the nonexistence of a g period below Z = 121"* |

`The_Method_1_6___The_Physics_Compendium-2.md` **L219** says *"derived absence (no g block)"* with no
bound and needs nothing. **Whether the rule reaches the companion paper and the compendium, or whether
ruling 12 is confined to §35 as its words say, is M's** — and it is the difference between a two-site
build and a six-site one.

---

## 8. What must be ruled before any file is written

1. **Ruling 11 and ruling 12's two §35 sites** — execute as written above, or not.
2. **The sibling sites** in the Löwdin companion and the Mathematical Compendium — in or out (§7).
3. **§34.7's rewritten passage** — M's prose; nothing is drafted here (§3B).
4. **The three Register appends** — numbers, wording, and whether a `WARNING:` accompanies each (§5).
5. **The withdrawal mechanic** for 34re-04 and D-61 (§4).
6. **And the consequence in §3A**: reading the right electron at lanthanum moves §34.7's ratio from
   √3 + 0.19 % to √3 + 2.46 %. **The √3 agreement does not survive the repair ruling 2 orders.** That is
   reported, not decided.

Nothing is repaired in any volume. Every figure here is MEASURED by an instrument named beside it or
RECORD-CARRIED with its quote.
