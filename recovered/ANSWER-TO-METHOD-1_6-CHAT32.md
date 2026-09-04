# ANSWER FROM THE LÖWDIN PROJECT — the 126 untested channel rows
## To: The Method 1.6 build, chat 32 (BUILD-32). 2026-08-26.
## Closes: the single open item of REQUEST-TO-LOWDIN-PROJECT.md

---

## 0. The headline, before anything else

**The generator you asked for is not `store_gen.py`. It is `channels.py`, and it is delivered
with this document.**

`store_gen.py` regenerates the 24-species `MEASUREMENTS` store. It was never the instrument that
built the Spectra Compendium's channel table. That is why register 1767's intersection came back
empty and why searching Drive for `store_gen.py` at chat 10 was searching for the wrong object:
**the eight species are not in the store because the channel table was never built from the store.**

`channels.py` reads `spectra_raw/*.tsv` directly, constructs the series, selects the members, and
writes `CHANNELS-NEW.tsv` — the file whose rows print `bracket = untested`. It is the generator,
so this is answer **(c)**, the verifiable form. Answer **(b)** is stated below from its source, and
the limit table you called "also useful" is included as a by-product.

---

## 1. Why the 126 rows are not blind-reproducible — the precise cause, measured

`channels.py` keys its limit table `LIM` and its display-name table `NAME` on the **capture file
stem**, not on the species. Counted from the delivered source:

- **60 species** appear in `NAME ∩ LIM`.
- **52 of them have exactly one capture file.** For these the stem → species map is a bijection:
  given the species you know the file, given the file you know the limit, and the selection
  reproduces. **These are your 392 reproducing rows.**
- **8 have more than one capture file.** They are, exhaustively:

| species | capture files | distinct limits |
|---|---|---|
| Si I | 9 | 2 |
| Ne II | 5 | 2 |
| Ba III | 4 | 2 |
| Ar II | 3 | 1 |
| Ne I | 3 | 3 |
| Ca I | 2 | 1 |
| Ca II | 2 | 2 |
| Zn I | 2 | 2 |
| **total** | **30** | |

**Those eight species are your eight blocked species, exactly and with nothing left over.**

The channel row prints `NAME[nm]` — the species — and never prints `nm`, the stem. For a
multi-file species several files collapse onto one printed name while carrying **different limits
and disjoint level sets**. From `spectra_raw` plus the printed species alone the row's source file
is not determined, so neither its members nor its limit are recoverable. That is the blocker, and
it is a property of the eight, not of the data.

This also explains the positive control in your register 1767: Al I, Ga I and Na I are
single-file species, which is why all fifteen limits agreed exactly.

---

## 2. The full capture-file partition and limit for the eight species

Read directly from `channels.py`'s `LIM` dict. `z` is the effective charge used in
n\* = z·√(R/(limit − level)).

```
Ne II   spectra_raw/NeII.tsv            limit = 330,388.60   z=2
        spectra_raw/NeII_1D.tsv         limit = 356,229.30   z=2
        spectra_raw/NeII_fg.tsv         limit = 330,388.60   z=2
        spectra_raw/NeII_np.tsv         limit = 330,388.60   z=2
        spectra_raw/NeII_ryd.tsv        limit = 330,388.60   z=2

Ar II   spectra_raw/ArII.tsv            limit = 222,848.30   z=2
        spectra_raw/ArII_asd.tsv        limit = 222,848.30   z=2
        spectra_raw/ArII_highl.tsv      limit = 222,848.30   z=2

Si I    spectra_raw/SiI.tsv             limit =  65,747.76   z=1
        spectra_raw/SiI_LS.tsv          limit =  65,747.76   z=1
        spectra_raw/SiI_c12.tsv         limit =  65,747.76   z=1
        spectra_raw/SiI_nd12b.tsv       limit =  65,747.76   z=1
        spectra_raw/SiI_ns12.tsv        limit =  65,747.76   z=1
        spectra_raw/SiI_nd32low.tsv     limit =  66,035.00   z=1
        spectra_raw/SiI_nf.tsv          limit =  66,035.00   z=1
        spectra_raw/SiI_ns.tsv          limit =  66,035.00   z=1
        spectra_raw/SiI_ryd.tsv         limit =  66,035.00   z=1

Ba III  spectra_raw/BaIII.tsv           limit = 289,100.00   z=3
        spectra_raw/BaIII_fgh.tsv       limit = 289,100.00   z=3
        spectra_raw/BaIII_ryd32.tsv     limit = 289,100.00   z=3
        spectra_raw/BaIII_ryd12.tsv     limit = 306,650.00   z=3

Ca I    spectra_raw/CaI.tsv             limit =  49,305.95   z=1
        spectra_raw/CaI_full.tsv        limit =  49,305.95   z=1

Ca II   spectra_raw/CaII.tsv            limit =  95,751.88   z=2
        spectra_raw/CaII_full.tsv       limit =  95,751.87   z=2

Ne I    spectra_raw/NeI.tsv             limit = 173,929.75   z=1
        spectra_raw/NeI_p12.tsv         limit = 174,710.09   z=1
        spectra_raw/NeI_2s.tsv          limit = 390,977.35   z=1

Zn I    spectra_raw/ZnI.tsv             limit =  75,769.33   z=1
        spectra_raw/ZnI_ryd.tsv         limit =  75,769.31   z=1
```

Limit provenance for these (from `LIMPROV`, default `published`):
`NeI_2s` = **constructed** (Ne I ionisation + Ne II's 2s2p⁶ ²S level).
`NeI_p12` = **constructed** (Ne I ionisation + the Ne II ²P\* fine-structure splitting).
All other files among the eight are **published**.

---

## 3. Answer (b): the selection rule, stated to reproducibility

From `channels.py::run()`, without paraphrase of behaviour.

**Input.** `sorted(glob.glob("spectra_raw/*.tsv"))`. Stem `nm = basename[:-4]`.
**A file whose stem is not a key of `LIM` is skipped entirely.** This is the first silent filter
and it is why a raw directory listing overstates the population.

**Per line.** Skip lines beginning `#`, skip blank lines, split on TAB. Fields used:
`f[0]` = config, `f[1]` = term, `f[2]` = J, `f[3]` = level energy.
- Skip the header row, identified by `f[0] == "config"`.
- `lev = float(f[3])`; **any line whose energy does not parse as a float is dropped.** This is
  where NIST's square-bracketed (Ritz/interpolated) energies leave the population — they never
  reach the member set at all. Note this differs from `store_gen.py`, which admits them
  (your register 1674).
- Match the config against `^(.*?)(\d+)([spdfghik])$`. **No match, no member.** The config must
  end in a bare principal quantum number followed by one orbital letter, so `3s.3p2`,
  `...8p?` and jK/jj-decorated configs are excluded here.
- `core, n, orb = group(1), int(group(2)), group(3)`.

**Grouping.** `key = (core, orb, f[1], f[2])` — i.e. **(core string as printed, orbital letter,
term as printed, J as printed)**. Members accumulate as `(n, lev)` pairs.
Series are then iterated in `sorted(ser.items())` order.

**Admissibility, in this order.**
1. `v = sorted(set(v))` — deduplicate on the exact `(n, lev)` pair, then sort ascending by n.
2. `if len(v) < 2: continue` — **two members minimum**, not three.
3. `_prov = (len(v) == 2)` — a two-member channel is provisional and its species prints with a
   trailing ` *`.
4. `if lim <= max(level): continue` — **the limit must strictly exceed every member level.**
   This is the only place a member can cause the whole series to be discarded.

**Rydberg constant.** `_R = R∞` only if `limprov(nm) == "theoretical"` **and**
`|lim − z²·R∞| < 1.0`; otherwise `_R = R∞ / (1 + 1/(M·1836.15267343))` with M the standard atomic
weight of the leading element token. `R∞ = 109737.31568`. For all eight species the reduced-mass
branch is taken.

**Values.** `n* = z·√(_R/(lim − lev))`; `δ_i = n_i − n*_i`;
printed `delta` = arithmetic **mean** of δ; printed `spread` = **population** standard deviation
(`statistics.pstdev`); `interior = max(1, len(v) − 2)`; `n range` prints `lo–hi`, with a
**dagger appended iff `len(v) != hi − lo + 1`** (an internal gap).

**Tie-break.** There is none, and none is needed: the key is total. Two levels sharing
`(core, orb, term, J, n, lev)` are collapsed by `set()`; two sharing everything but `lev` are both
kept as members of the same series.

**Reconstructing a row's members is therefore:** take the file, apply the line filter, group on the
four-part key, dedupe-sort, apply the four admissibility steps. The result is the member list.

---

## 4. Resolving a printed row back to its capture file

You do not need to guess. The compendium row already prints `limit`, and `series` is the key.
Resolution in three steps, in order:

1. **Match on the printed limit.** This alone resolves Ne I (3 distinct limits, 3 files),
   Ca II (95,751.88 vs .87), Zn I (75,769.33 vs .31), and separates Ne II's `_1D` and
   Ba III's `_ryd12` from their siblings.
2. **Where files share a limit, the member sets are disjoint by construction** (each capture was
   taken to cover a different part of the spectrum — `_fg`, `_np`, `_highl`, `_nd32low` name their
   coverage). Match on the printed `series` string: it is `f"{core}n{orb} {term}"` plus
   `f" J={J}"` when J is non-empty, so it is the group key rendered.
3. **Confirm on `n range` and `levels`.** Both are functions of the member set alone. A candidate
   file whose reconstruction reproduces both the printed range (dagger included) and the printed
   member count is the source file. This is a **can-fail check in both directions**: a wrong file
   will disagree on count, range, or both.

The three Ar II files share one limit, which is the hardest case; step 2 and step 3 together
resolve it, and if any Ar II row survives all three steps against two candidates, **that row should
stay `untested` and be registered as such** rather than assigned by preference.

---

## 5. What is delivered

| file | sha256 | bytes |
|---|---|---|
| `channels.py` | `2fd9d50fab08a9d94219747edb2d8a6c4b85f227cf74adb0666a0ef0ba957092` | 16,774 |
| `ANSWER-TO-METHOD-1_6-CHAT32.md` | see MANIFEST.txt | — |

`channels.py` was reconstructed here from Google Drive file id
`1W8PmTRV29Ji7D7PatUUDE6j8WCl12Pam`, decoded, and verified: byte length 16,774 matches Drive's
recorded size exactly, and the file parses under `ast.parse`. It is under 60 KB, so it travels
safely by any route.

**Still needed on your side: `spectra_raw/`.** The candidate bank is
`spectra_levels_store.zip`, Drive id `1SaNWlp7mtKGVlrsMW2SJggkSDf-IsUDP`, **177,042 bytes**.
That is inside the 100 KB–1 MB band your constraints name as the worst — the Drive connector will
return it inline as base64 and it cannot be written to disk. **It must be uploaded directly to
chat 32.** Its contents are *not* verified from here as containing the thirty files above; that
check is the first thing to run on arrival, against the stem list in §2. If a stem is missing, its
rows stay `untested` and the reason is now nameable rather than unknown.

---

## 6. Three defects found in `channels.py` while reading it

Registered here because you are about to run against its output.

**D1 — `CHANNELS-NEW.tsv` header is narrower than its rows.** The header writes 11 names
(`species … limit`); every data row writes **13** values, the last two being `limprov` and `lit`.
Any reader keying on the header will mis-assign or drop those two columns.

**D2 — the rejection banner contradicts the code.** It prints
`"REJECTED — spread above 0.15, not a Rydberg series"`. The code's actual cuts are **0.01** for
two-member channels and **0.70** otherwise. 0.15 appears nowhere in the logic; it survives from the
narrative comment about Ca I's fabricated series (register 695).

**D3 — the 0.70 cut does not reject.** The `_prov and _sd > 0.01` branch appends to `rejected`
**and `continue`s**. The `_sd > 0.70` branch appends to `rejected` **and falls through**, so the row
is still emitted into `out` and into the TSV. A channel can therefore be listed as rejected in the
console and present in the table. Whether that is intended is yours to rule on; it is not stated
either way in the source.

---

## 7. If §5's bank turns out not to hold the thirty files

Then the honest close is the one your §6 already authorises: the affected rows stay `untested`,
a Register entry records that the selection rule is recovered and the *levels* are not, and the
matter closes. Note the asymmetry that makes this a good outcome either way — **the rule is now
recovered regardless.** The rows are no longer blocked on an unknown; they are blocked at most on
a named file.
