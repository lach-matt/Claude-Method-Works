# CERTIFICATE — the register session (1.8.5), closing pass

**M's ruling for this chat:** keep the register current by monitoring the other chats.
Nothing rendered to PDF; the press stays where it is until the works are done. **No press was run.**

## Bank
| | |
|---|---|
| in | `restore-point-2_13.tar.gz` — sha256 `8057709403…d857a5`, verified against the banked header |
| interim | `restore-point-2_14.tar.gz` — the register write |
| **out** | **`restore-point-2_15.tar.gz`** — sha256 `b5459cbbcde58c8f9854f9fe8fb336416694604074267c4402625b6f7fa9c044` |
| C4 | **729 archive entries = 715 files + 14 dir entries**, of which `./` is one → 13 dirs below root |

## Register — by the instrument now declared
| | in | out |
|---|---|---|
| **entries (canonical, distinct ids)** | 1,486 | **1,518** |
| numbered headings | 1,483 | 1,518 |
| bolded headings | 1,352 | 1,385 |
| max id | 1700 | **R 1732** |
| duplicates | 0 | **0** |

`REGISTER.md` rebuilt by `python3 register_gen.py > REGISTER.md` — with the redirect, every time.

## Gates — run after every change, `.zeno/` cleared each time (R 1709 applied to itself)
| | baseline | after register write | after four repairs | after §8 rewrite | at seal |
|---|---|---|---|---|---|
| prime audits | 25/25 | 25/25 | 25/25 | 25/25 | **25/25** |
| round-trip | 6/6 | 6/6 | 6/6 | 6/6 | **6/6** |
| `mech_audit` | MISMATCH (17 vs 0) | — | **LISTS AGREE** | — | **LISTS AGREE** |

## Written
**R 1701–1732** — thirty-two entries. R 1701–1727 reconciled four chats that each allocated ids
from R 1700; R 1728–1732 are this session's own work, including two faults it committed.

## The four owed repairs, now in the tree
1. **Quote branch** of `press_compendia.py` buffers and joins as the body branch has since R 632.
   Original line recovered verbatim from the Books transcript and confirmed byte-identical to the
   banked line **before** anything changed. Undo at `UNDO-PRESS-REPAIR.txt`. Tested on a bold span
   wrapped across two quote lines — balanced where the unrepaired branch leaks.
2. **`artefact_audit.py` widened to six documents** — Physics enters the list it has been absent
   from since register 901. R 995's omission closed.
3. **Figure assertions corrected to measurement** — INDICES 4 → 5, SPECTRA 0 → 3, both counted from
   source here. The book's 33 and the Register's 0 deliberately untouched.
4. **P family restored to `QUEUE.md`** from `MECHANISMS.md`; `QUEUE.prev.md` holds the prior state.

## Also closed
- **`CHAPTER-LOWDIN.md` §8 rewritten** and now states the register range it is current to (R 1729).
  Prior text at `CHAPTER-LOWDIN.PRE-1728.bak.md`.
- **`register_count.py` built and declared canonical** (R 1730); reports, does not gate, not wired
  into the press — that remains M's ruling under R 1706.
- **`DIGEST.md` extended** with the 1.8.5 carry, so a fresh session inherits the instrument and the
  single-writer rule rather than the argument.

## Two faults, both registered
- **R 1728** — I measured the P family with `P[0-9]+`, caught this chapter's unrelated P1–P4, and
  nearly reported the press certificate wrong. The family is `P.name`. R 1672 fired on a POSITIVE,
  which is the more dangerous direction.
- **R 1730** — `register_count.py` failed on its first live run against the entry that declares it:
  a wrapped line beginning "1476a." read as a heading. R 1617's fault, inside the entry written
  against it. Reflowed, not suppressed — the instrument was right and the prose was wrong.

## Standing with M, untouched
- **Two reopens (R 1721, R 1731)** — R 1457 and R 1458. Requested on recorded fact, not asserted.
- **Wiring `register_count.py` into the press** — R 1706's remaining half.
- **Ladder-as-limit · T8-J width · Kr II URL · the 93 series · T9's 65** — board rows 1–5, unmoved.
- **`BOARD-3-REVISED.md`** is banked as history and still carries R 1702's withdrawn necessity claim
  in §B-10 and N-2; discharged at R 1716. Not corrected — §H.4.