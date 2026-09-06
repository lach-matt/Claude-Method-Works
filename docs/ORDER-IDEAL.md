# ORDER-IDEAL — register 66 re-measured, for R3

`tools/orderideal.py` runs the test register 66 states, against the seated observed data. This
records what it found. **It does not repair register 66, and it offers no verdict on it** — the
chat-67 full hold governs this exactly as it governs a section read. It is filed for review, repair
or correction in R3.

```
python3 tools/orderideal.py --selftest     # assert the corpus's own numbers first
python3 tools/orderideal.py                # the measurement
python3 tools/orderideal.py --verbose      # every violation, gap and Z-order break
```

## The three records

| | cells | order ideal | violations | gaps | ℓ-orderings |
|---|---:|---|---:|---:|---|
| **register 66** (seated) | 118 | **yes**, "without exception" | 0 | — | 1 of 120 |
| **unbanked re-measurement** (`PROSE-ONLY.tsv`) | 110 | **no** | 172 | 7 | **0 of 120** |
| **this run**, on `LW1-ground.py` | 98 | **no** | 197 | 5 | **0 of 120** |

**The counts differ before the property does, and that is the first thing to settle.** 118 is the
Register's own first census (registers 11, 12: *"180 void, 240 reactive, 78 reserved, 118 occupied"*,
plus 14 ghost cells). This run reads Z = 1..108 — the range the seated member holds — so a smaller
cell count is expected and is not itself a discrepancy. The 110 of the re-measurement is a third
convention whose element range is not stated in the prose.

**The property does not depend on which of the three counts is right.** All three conventions that
have actually been run agree the set is not downward closed, and two of them independently give
**0 of 120** admissible ℓ-orderings against register 66's 1 of 120. That number is the cleanest
comparison available: it is a pure property of the occupied set and does not move with the element
range.

## What the violation is, concretely

The occupied set has **occupancy gaps** — a subshell realised at some occupancy `k` while a lower
occupancy in the same subshell is realised by no element at all:

| subshell | top occupancy | missing k |
|---|---:|---|
| 3d | 10 | **4**, **9** |
| 4d | 10 | 3, 6, **9** |
| 4f | 14 | 2, 8 |
| 5d | 10 | **8** |
| 5f | 14 | 1, 5, 8 |

The four in bold are the mechanism the unbanked re-measurement named, and they are forced by the
anomalous ground configurations the seated member itself records:

| | seated config | the hole |
|---|---|---|
| V → **Cr** | `3d3` → **`3d5`** | nothing has 3d⁴ |
| Ni → **Cu** | `3d8` → **`3d10`** | nothing has 3d⁹ |
| Rh → **Pd** | `4d8` → **`4d10`** | nothing has 4d⁹ |
| Ir → **Pt** | `5d7` → **`5d9`** | nothing has 5d⁸ |

`LW1-ground.py`'s own docstring (register 1306) says this in its own words: *"Every previous version
of this work built configurations by aufbau and patched the exceptions by hand. That table was wrong
at Pd — aufbau plus my patch gave [Kr]4d9 5s, and the observed configuration is [Kr]4d10 with no 5s
at all."*

So the anomalies are not in dispute. They are seated, measured, and documented as the correction that
produced the member.

## Z is not a linear extension either

Six elements drop a subshell their predecessor held:

| step | lost |
|---|---|
| Z 45→46, Rh→Pd | `5s` |
| Z 58→59, Ce→Pr | `5d` |
| Z 64→65, Gd→Tb | `5d` |
| Z 93→94, Np→Pu | `6d` |
| Z 96→97, Cm→Bk | `6d` |
| Z 103→104, Lr→Rf | `7p` |

The re-measurement reported 9; this run finds 6 over Z = 1..108. Same direction, different count —
consistent with the two runs covering different element ranges.

## Conventions, and where each comes from

- **Admissibility** — `(n, l, k)` is admissible iff `l < n` and `1 ≤ k ≤ 2(2l+1)`. **RECOVERED**:
  read from the Register's own partition (registers 11, 12) — *"void (l ≥ n, orbital cannot exist),
  reactive (electron count exceeds subshell capacity), and reserved (valid but unoccupied)"*.
- **Occupied** — a cell is occupied iff some element's ground configuration contains that subshell at
  exactly that occupancy. An element with `2p6` occupies `(2,1,6)`; it does not also occupy
  `(2,1,1..5)` — those are occupied by B, C, N, O and F. Downward closure is a question about the
  union across elements. **RECOVERED**: register 66's own wording, *"if an element has ground-state
  configuration (n,ℓ,k), then every configuration with no larger shell, subshell or occupancy is
  likewise realised"*.
- **Data** — imported from the seated member `method/members/LW1-ground.py` (register 1306, NIST ASD
  5.12, Z = 1..108). The instrument imports; it never copies a member.
- **ℓ-orderings** — all 120 permutations of `l ∈ {s,p,d,f,g}`. Only the `≤` test on `l` is permuted;
  admissibility stays in the original coordinates, because `l < n` and Pauli capacity are physics,
  not an artefact of the ordering. **RECONSTRUCTED**: the corpus states the 1-of-120 and 0-of-120
  results but not the permutation convention that produced them, so this reading is the instrument's
  own and is the most likely place for the two runs to differ on method rather than on fact.

## What this does not settle

- **Which cell count is correct.** 118, 110 and 98 come from three different element ranges and
  possibly three different counting conventions. Only 98 has its convention stated in full.
- **Whether register 66 is wrong.** It may be exactly right about the object it was measuring — an
  aufbau-built table, or the full 118-element table, or a different notion of cell. This run measures
  the *observed* configurations for Z = 1..108, which is the object `LW1-ground.py` holds, and that
  member exists precisely because an earlier aufbau-built table was found wrong.

**The open question for R3 is therefore narrower than "is register 66 true".** It is: *which object
does register 66 quantify over, and is that object the observed table?* If it is, the register's
"without exception" does not survive the four anomalies. If it is not, the register needs its object
named — because as printed it says "ground-state configuration", which the seated member reads as the
observed one.

## Re-verification

```bash
python3 tools/orderideal.py --selftest    # seated member intact; anomalies and holes present
python3 tools/orderideal.py --verbose     # full listing
python3 method/members/LW1-ground.py      # the member's own check: 108/108 electron counts
```

The selftest asserts, from the corpus's own data: every element's electron count equals Z;
admissibility matches registers 11/12 on known cells; the four anomalous configurations
(`3d5`, `3d10`, `4d10`, `5d9`) are present as seated; and the four holes they force
(`3d4`, `3d9`, `4d9`, `5d8`) are unoccupied.
