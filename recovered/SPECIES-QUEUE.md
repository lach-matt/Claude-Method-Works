# The species queue — one batch per session

**Purpose.** Partition the collection's 1,442 cells by value provenance, per Q item P.
The lookup is a delimiter read plus a provenance note, and it is bounded: 35 species,
one search each. **Small batches, one per session, so the rest of the work continues.**

## The method, per species

1. **Take the search key from the book's own References.** The bibliography maps species
   to compilation, and the ASD page names its primary compilation — so the compilation
   is the search key. No URL construction, which the fetch tool refuses.
2. **Search.** `NIST ASD levels output "<species>" Levels Found <compilation> primary data source`
3. **Read the snippet first.** It usually carries the provenance note, and the note is
   the deciding datum — it settled He I's 189 cells before a delimiter was counted.
4. **Fetch only if the note is absent or ambiguous.** Prefer the nublado mirror when its
   URL surfaces: `data.nublado.org/nist/asd_v5.12/levels/asd.ZZZCCC`, kilobytes against
   megabytes.
5. **Record**: plain / `[ ]` / `( )` counts, the note verbatim, and the n at which the
   method changes.

## What is being counted, and why it is not cells

The bracket relates T(n−1), T(n), T(n+1). A cell is an independent test only if **all
three** of its levels are independent, so one derived level poisons three tests and the
surviving fraction goes as (1−f)³. **And LOPT fits neighbouring levels from overlapping
line sets**, so even the triple count is a ceiling. `asd_pass.py` counts triples.

## The three markings

| marking | NIST's wording | distance from measurement |
|---|---|---|
| plain | optimised from measured lines | one inversion |
| `[ ]` | interpolation, extrapolation, **or fitting the Ritz-type formulas along series** | two |
| `( )` | determined from an ab-initio calculation | none from measurement |

---

## DONE — 2 species, 244 cells

| species | cells | result |
|---|---|---|
| **H I** | 5 | ~57 of 106 levels bracketed; every level n = 13–40. **13 of 64 interior cells independent — 20%.** nd series: six plain levels of ten, **not one clean triple** |
| **He I** | 189 | **Every level bracketed. No observed values at all.** Note: n ≤ 10 from Drake's theory anchored to Kandula's measured ground level; n ≥ 11 by fitting the extended Ritz quantum-defect expansion. **§22.9's defence of He I is unsound** |

## NEXT BATCH — keyed and ready

| species | cells | search key from the References |
|---|---|---|
| **Na I** | 80 | Sansonetti 2008, *JPCRD* **37**, 1659 — *URL already surfaced, 430 levels, v5.12* |
| **K I** | 105 | Sansonetti 2008, *JPCRD* **37**, 7 |
| **Ne I** | 131 | Saloman & Sansonetti 2004, *JPCRD* — found this session |

Those three plus the two done cover **555 of 1,442 cells, 38%.**

## QUEUE — keyed by the References' own mapping

**Named directly in the References line** — *Ar II · Be II · Bi I · C II · Ca II · Cd II ·
Ga I · He II · Hg II · K II · Li I · Li II · Mg II · N II · Na II · Ne I(³⁄₂) · Ne I(¹⁄₂) ·
Si I · Si II · Zn II* — search key `NIST Atomic Spectra Database` plus the species.

**With their own compilations:** Be I → Kramida & Martin 1997, *JPCRD* **26**, 1185 ·
Sc VI → Sugar & Corliss 1985, *JPCRD* **14** Suppl. 2 · ionisation limits → Sugar &
Musgrove 1990/1995.

**Unkeyed, needing a search for the compilation first:** Al I · Al II · Li III · Ti I ·
Cu II · Kr I · Sr I · Ba I · Ba II · Ba III · Bi II · Bi III · P II · Sc III · Zn I.

## The pattern so far, five species examined

**No ASD level is a direct measurement.** H I, He I, Ne I, Na I and Hg I all rest on
critical compilations in which levels are *derived from measured lines* by least-squares
optimisation — LOPT, Kramida 2011. Martin & Zalubas say it of sodium: *we have derived or
recalculated the levels.* Cloudy's Stout database says it of the whole ASD.

**Predict before each batch, per §2.13:** the species will be plain at low n and bracketed
above the n where its compilation switches to a Ritz or quantum-defect fit, and the note
will name that n. Two of two so far. **Record any species that breaks it.**
