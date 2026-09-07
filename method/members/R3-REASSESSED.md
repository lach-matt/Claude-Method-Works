# R3, REASSESSED IN FULL — on M's order of 6 September 2026. **R3 is complete and superseded.** The store is not where `method/CLAUDE.md` §3 says it is: it is sixteen main builds and thirty-eight compendia builds further on, R3's classes are executed, its "56 readings" are eight held instruments with a stated reason each, and the successor framework is already seated and approved — the R4 publication plan. **What now needs seating is the record of M's own rulings.**

M: *"yes. reassess R3 in full."* Measured 6 September 2026 by running the store's own gate on the live pair.

## 1. Where the store actually is

| | `method/CLAUDE.md` §3 says | **measured today** |
|---|---|---|
| main bundle | BUILD94, md5 `6079e066…` | **BUILD110**, md5 `e1264def…`, 2,054,674 B, 18,692 lines |
| compendia bundle | BUILD194, md5 `d7f362b3…` | **BUILD232**, md5 `199df633…`, 15,170,136 B, 123,726 lines |
| members | 427 | **667** |
| Register | 1 to 1800 | **1 to 1835; 1,677 seated** (1,670 numbered + 7 grouped) |
| Working Register | W-202, 203 entries | **W-239** |
| gate | *"KNOWN RED, and it is now 56, not three"* — 44 UNEXPLAINED, 12 UNRUNNABLE | **86 live goldens, census a fixed point; 8 held, each with a reason** |
| R3 | *"IS OPEN and its first two classes are executed"* | **complete through Q5/Q6**; superseded by the R4 plan, approved and seated at W-239 |

**§3 is not merely stale in its numbers. It is stale in its instruments and in its procedure**, and that is what
made it dangerous to act on:

- It names `shiftcheck.py` as the guard before a re-bank. That tool's window *cannot* sort a Register-line shift
  — 132 of 136 UNEXPLAINED at W-234 — and the store has since built `tools/shiftinv.py`, `tools/shiftcheck2.py`,
  `tools/reanchor.py` and `tools/proveanchor.py` for the job.
- It names `gate.py census` as a gate step. That step **stays red by construction** now; the live census step is
  `tools/gate_live.py --census`.
- It names `gate.py run --all` as the verdict. That walk reports nothing the held list does not, and
  `tools/gate_live.py` — the walk over goldens with no seated successor — is what the store treats as live.
- It gives the manifest command with `--main …BUILD92…`, two main builds before the one it elsewhere names and
  eighteen before the one on disk.

## 2. The gate, run today on the live pair

| step | verdict |
|---|---|
| `python3 method/verify.py` | **VERIFY OK** — 667 members match size and md5; both bundles recovered by splicing |
| `gate.py run --core` | **5 OK** — `tower-2`, `kinds`, `minmax`, `r2-tools-constants`, `extent` |
| `gate.py manifest --main …BUILD110…` | **OK**, 666 listed / 668 extracted; one note: `r2-28b3.py` is in `members/` and in no bundle (recorded at DEF-153O, superseded by `r2-28b4`, left in place) |
| `tools/gate_live.py --census` | **OK** — the seated census is a fixed point: 1,609 rows (2 carried retired), 1,607 regenerated exactly, 0 NEW, 0 GONE, md5 `4742c83a…` equal to the seated member |
| `tools/gate_live.py` (86 goldens) | *(recorded below)* |

## 3. What R3 executed — the answer to "is R3 open?"

From `DEF-153O-PENDING.md`, which is R3's own running account, and confirmed against the Working Register:

- **DEF-152's ten items**, all executed, at Register entries 1807–1813 and the census closure file.
- **The withdrawn-law class** (`r3-wl2`, entries 1798–1799) and **the arithmetic class** (`r3-arith-01`, entry 1800).
- **reg1-04 repaired with its class** at entry 1815 — the Register's span and counts current; `kinds` and `extent`
  re-banked for the first time since BUILD90. §3's *"the front matter was stale by one entry, and is now stale by
  five"* is **closed**.
- **The positional class closed by generator**: forty-four successors seated, each proved byte-exact by
  `tools/proveanchor.py` on the bundle its predecessor's golden was banked against.
- **Q5 in full** — the five Register queue documents and the owed-expansions document, entries 1821–1835, every
  figure re-derived by a standard-library instrument before its entry was written, six independent auditors
  reading the entries before seating.
- **The census made content-keyed**: `census2.py` and `close_census2.py` seated, 1,557 → 1,609 rows, ids matched
  by content in four printed tiers, two rows carried RETIRED under a typed ruling rather than dropped.
- **Every tool in the repository seated as a member** on M's 5 September ruling (W-236), twenty members, each
  proved to run from `members/`.

**So R3's classes are executed.** What §3 calls "the next work" — *"the 56 readings before any further R3 class
lands"* — resolved into forty-eight re-banks and **eight held instruments**, each named with its reason:
`r2-26b` (unrunnable, successor owed), `r2-ch18b`, `r2-ch23a`, `r2-ch23b`, `r2-ch28a` (readings, not re-banks),
`r2-reg11a2`, `r2-reg12b` (census rows keyed by Register line), `r3-wl` (re-taken by `r3-wl2`).

## 4. Where the remaining work lives now

Not in R3. `PLAN-R4-PUBLICATION.md` — **written from a survey of every record of outstanding work the store holds,
approved by M on 5 September and seated at W-239** — carries it, in eight phases, with `PLAN-R4-ANNEX.tsv`'s 800
rows as the item inventory (731 open at the survey). Ten of its fifteen Phase 0 rulings are given; five are not,
and they are named rather than inferred: 3 (the nine heading-only sections, which only M can author or withdraw),
4 (entry 1797), 6 (the language roster), 7 (the retraction and prose-only triage).

**And `RULINGS-R4f`'s R3 items map onto that plan rather than standing beside it:**

| ruling (RULINGS-R4f) | where it lands in the approved plan |
|---|---|
| **2** — lanthanum's 5d reading in registers 1334/1337 | **Phase 1**, the mathematics leg: a computable claim contradicted, re-derived by instrument, settled by entry |
| **3** — the f test enters, register 1337 corrected | **Phase 1**, then **Phase 2** for the appended entry |
| **9** — docket 34re-04 withdrawn | **Phase 1**, the arithmetic-convention class |
| **10** — D-61 withdrawn | **Phase 1** |
| **11** — §34.4 repairs with its class | **Phase 1**, the withdrawn-law class (its class is already executed twice) |
| **12** — §35's g-block bound widened | **Phase 1**, then the prose wording at **Phase 3** |

Every one is a Phase 1 item. **There is no separate "R3 corrections pass" to open** — opening one would duplicate
a phase the plan already owns and M has already approved.

## 5. The finding that matters most, and it is structural

**M's rulings from five sittings are not in the store.**

| | working file | seated member |
|---|---|---|
| `RULINGS-R4.md` (Phase 0, ten rulings) | yes | **yes** — W-239 |
| `RULINGS-R4b.md` … `RULINGS-R4f.md` | yes | **no** |
| `SETTLED-R4.tsv` (134 rows) | yes | **no** |
| `FINDING-R4-01` … `FINDING-R4-23` (23 files) | yes | **no** |

The store's own discipline puts rulings in a member: `RULINGS-R2.md` is append-only and read at every open, and
`RULINGS-R4.md` was seated the moment M gave the Phase 0 rulings. **Five further ruling documents — including
`RULINGS-R4f`, which governs everything this session did — exist only as files on a branch.** A chat that opens
by the §0 gate reads `RULINGS-R2.md` and `RULINGS-R4.md` and would not see them.

That is the same fault class the corpus records against itself twice over: a governing document that the store
does not carry (`register_review.py` never becoming a member, which is why entry 1617's repair did not hold), and
a ruling recorded outside the archive.

## 6. What is owed, in order

1. **Seat the rulings.** `RULINGS-R4b` … `RULINGS-R4f` as members, by the same route `RULINGS-R4.md` took — a
   guarded close with a Working Register entry. Until that lands, the governing rulings of this branch are outside
   the store of record.
2. **`method/CLAUDE.md` §3 rewritten** from the measurements above — done in this pass, since §3 is a project
   instruction and not a bundle member, and M ordered it.
3. **The findings and the settled ledger.** Whether `FINDING-R4-01…23` and `SETTLED-R4.tsv` are seated as members
   or stay working notes is M's ruling, and it is put rather than assumed. The plan's own precedent is that a
   record of the work is seated (`PLAN-R4-ANNEX.tsv` is a member).
4. **Then Phase 1 opens** with `RULINGS-R4f`'s six items among its rows — not as an R3 pass.

Nothing is repaired in any volume by this reassessment. Every figure is MEASURED by the command named beside it.
