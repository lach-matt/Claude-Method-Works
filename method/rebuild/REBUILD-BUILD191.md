# REBUILD-BUILD187…191 and BUILD92 — the builds that followed M's two rulings

Written by **chat 151-R**. All were made in the repository, not carried. `REBUILD-BUILD185.md` and
`REBUILD-BUILD186.md` cover the chain up to BUILD186.

## BUILD92 — the main bundle, first build since chat 62

| object | bytes | md5 |
|---|---:|---|
| old, BUILD90 main | 1,983,081 | `49065309b0c4fe8e055f693aed295cca` |
| entries file, 1793–1796 | 4,366 | the exact tail of chat 152's BUILD91 Register |
| **new, BUILD92 main** | **1,987,447** | **`ac49200f5a8a02511865260202e75cbb`**, 18,485 lines |

```
python3 members/close_main.py --old …BUILD90… --new …BUILD92… --entries ENTRIES-1793-1796.md
```

**No `--recount`.** M ruled the entries stand and the count repair waits, so the Register's two count
sites are untouched. Assert before building, not after: **BUILD90's Register plus the entries file
differs from chat 152's BUILD91 Register at exactly two lines — both count sites — and nowhere else
in 6,627.** The reverse guard recovers `49065309…`.

BUILD91 is chat 152's retired main bundle (`7ff88249…`). **The name 91 is skipped** so that no two
bundles ever share one.

## BUILD187 — M's two rulings, and `close_rebank.py`

`close.py` with `--old …BUILD186…`, `--new …BUILD187…`, `--main …BUILD92…`,
`--w W-196.md`, `--append RULINGS-R2.md RUL-151R2.md`, `--append DEFERRED.md DEF-151r3.md`,
`--append DOCKET.md DOCKET-151r3.md`, `--members members/close_rebank.py`.
**Assert 6,617,107 B / `7b9e656754c826874e300e4ba7da64e8` / 75,045 lines / 421 members**; reverse
recovers `7144d18d…`.

## BUILD188 — 25 goldens re-banked

```
python3 members/close_rebank.py --old …187… --new …188… --main …BUILD92… --w W-197.md \
  --rebank kinds r2-21a r2-23a r2-24a r2-25b r2-26c r2-27a r2-28a2 r2-28b2 \
           r2-ch16f r2-ch16k r2-ch16m r2-ch16p r2-ch16r r2-ch16s r2-ch19b r2-ch21a r2-ch28b \
           r2-ch34re r2-reg1a r2-reg8a r2-reg12 r2-scf r2-warn r3-em
```

**Assert 6,621,520 B / `5474f081db6983ee99a8fedbe7e26c84` / 75,060 lines / 421 members**; reverse
recovers `7b9e6567…`. Every golden is regenerated **by running its instrument** — the tool refuses a
copy, refuses a non-zero exit, and refuses an unchanged output.

**`r2-regsweep` is deliberately NOT in that list.** It exits 0 and prints `INSTRUMENT FAULT - STOP`.
The tool's exit-code guard would have re-banked it; it was excluded by hand. **That is a limit of the
tool and is recorded as one.**

## BUILD189 — `close_census.py`

`close.py … --w W-198.md --members members/close_census.py`.
**Assert 6,633,624 B / `fb219294c00a517359c4fe8f04fc8fc9` / 75,199 lines / 422 members.**

## BUILD190 — the census regenerated

```
python3 /home/claude/members/close_census.py --old …189… --new …190… --main …BUILD92… --w W-199.md
```

Run it **from the staged tree**: `census.py` hard-codes `/home/claude/DEFECT-CENSUS.tsv`, so the tool
must resolve its HOME there. `./method/bin/stage-gate` first.

**Assert 6,637,503 B / `a535574bb04e9f34c1c2928b79460f7d` / 75,210 lines / 422 members**; reverse
recovers `fb219294…`. Expected: `DEFECT-CENSUS.tsv` 236,413 B / `ba8306f2ffafb1f5373990bc1790a289`;
**1,556 → 1,557 data rows, no id lost, none moved, 1,553 byte-identical**, ids 677/686/701 moving
only in a site count and **1557 appended** — `C13-HANDLE-LEAK` at reg L6626, entry 1796 printing
`BUILD180` in a reader-facing volume.

## The gate at BUILD190

`census` byte-identical · `run --core` 5/5 · `manifest --main …BUILD92…` **OK 423 / 424** ·
`verify.py` 424 members, both bundles recovered.

**`gate.py manifest` must be given `--main`.** Its `MAIN` constant still names BUILD90; that constant
is a **default** and line 42 takes the flag. Nothing is patched to make this work.

**Known red:** `run --all` carries `r2-regsweep`, `r2-26b` and `r3-wl`. All three assert the
Register's extent as an invariant rather than scoring it. `r2-regsweep2`, `r2-26b2` and `r3-wl2` are
owed and are **readings, not re-banks**.

## BUILD191 — the second order

```
python3 members/close_rebank.py --old …190… --new …191… --main …BUILD92… --w W-200.md \
  --rebank r2-ch16t r2-reg12
```

**Assert 6,640,248 B / `072cc2b825eb52102a23ab657e680ccd` / 75,219 lines / 422 members**; reverse
recovers `a535574b…`.

BUILD190 regenerated `DEFECT-CENSUS.tsv`, which is **itself an input to instruments**, so two goldens
moved again on it: `r2-ch16t` (census rows 1,556 → 1,557) and `r2-reg12` (rows engaged 249 → 250,
`C13-HANDLE-LEAK` 11 → 12). **`r2-reg12` had already been re-banked at BUILD188 and moved a second
time.**

**The rule this establishes: a chain that touches a volume re-banks in TWO passes** — first the
goldens that read the volume, then, after any derived member is regenerated, the goldens that read
the derived member. One pass leaves the second set silently stale, and **a stale golden is worse than
a red one, because the gate reports it green.**
