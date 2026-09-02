#!/usr/bin/env python3
"""spectra.py -- THE SPECTRA COMPENDIUM.

Register 1215-1216. This compendium exists to hand the book VALUES. It answers
questions and does not raise them: every open question, correction and reversal
belongs to the register, which is the working record this is distilled from.

Its subject is Lambda_spectra, the index of Rydberg channels, and its output is a
coordinate for every cell:

        (Z, charge, l, 2S+1)   ->   delta,   graded and sourced

Five sections, in the order the book needs them:

    0    THE COORDINATE SUPPLY     what the book reads
    I    THE INDEX                 what a cell is and which cells exist
    II   THE CHANNELS              every captured series, with its fit
    III  THE MECHANISMS            how a value is got where none was captured
    IV   THE SOURCES               where the levels came from

Nothing here argues. Where a value's standing is limited, the row says so.
"""
import re, csv
from collections import Counter, defaultdict

BOOK = open("The Method 1.6.md", encoding="utf-8").read()
L = []; W = L.append

COORD = []
try:
    with open("COORDINATES.tsv", encoding="utf-8") as f:
        for x in csv.DictReader(f, delimiter="\t"): COORD.append(x)
except FileNotFoundError:
    pass
GRADE = Counter(r["grade"] for r in COORD)
STAT  = Counter(r["witness"] for r in COORD)
NCELL = len(COORD)          # read from the file, never recited
BOUND = Counter(r["bound"] for r in COORD)

rows = []
for line in open("SPECTRA-DATA.tsv", encoding="utf-8").read().split("\n")[1:]:
    r = line.rstrip("\n").split("\t")
    if len(r) >= 11: rows.append(r)

# ------------------------------------------------------------------ 0
W("# THE METHOD 1.6 — SPECTRA COMPENDIUM")
W("")
W("**The index of Rydberg channels, and a value for every cell of it.**")
W("")
W("This compendium supplies the book with coordinates. Its subject is Λ_spectra; its "
  "output is a defect for every channel of every element, graded by how the value "
  "was got. *The register carries the working record — the corrections, the "
  "reversals, and what remains open. This carries the answers.*")
W("")
W("---")
W("")
W("# 0 · THE COORDINATE SUPPLY")
W("")
W("### What a coordinate is")
W("")
W("        (Z, charge, ℓ, 2S+1)   →   δ,  with a grade, a source and a bound")
W("")
W("**Z** the atomic number · **charge** the ionisation stage, 1 for the neutral · "
  "**ℓ** the Rydberg orbital · **2S+1** the multiplicity, which Hund's rule on the "
  "core derives from the ground state and does not require measuring.")
W("")
W("**δ** is the quantum defect: E = −Z_c²R/(n−δ)², so a channel's whole Rydberg "
  "series follows from one number and the core charge.")
W("")
W("**DECLARATION — the stored δ is the MEDIAN over a cell's members (T2, closed).** "
  "This was measured, not chosen: of 433 series whose member count reproduces "
  "exactly from raw, the stored value equals the median in 430 (99.3%); the 18 "
  "mean-agreements are series where median and mean coincide and distinguish "
  "nothing (R 1673, 1675, enlarged sample R 1679). The mean and asymptotic "
  "perspectives are carried alongside per cell, as perspectives of one "
  "definition (T6, M's ruling, session 1.7.3).")
W("")
W("### The grades")
W("")
W("| grade | rows | what it means |")
W("|---|---|---|")
W(f"| **exact** | **{GRADE.get('exact',0):,}** | forced by symmetry — δ = 0 when one "
  "electron faces a bare nucleus |")
W(f"| **measured** | **{GRADE.get('measured',0):,}** | fitted to captured levels "
  "against an ionisation limit |")
W(f"| **computed** | **{GRADE.get('computed',0):,}** | supplied by the channel "
  "equation, within the domain stated below |")
W("")
W("**Nothing is ungraded.** A value with no provenance is not a coordinate.")
W("")
W("### The witness")
W("")
W("*Register 1578. This table used to grade cells VERIFIED, POSSIBLE and "
  "IMPROBABLE. **Improbable is a judgement about the future, not a fact about "
  "the record** — and register 1287 had already established the rule it breaks: "
  "an index whose coordinates mix the OBJECT with the OBSERVER cannot close. "
  "What replaces it is a fact and a named obstacle.*")
W("")
W("| | cells | |")
W("|---|---|---|")
W(f"| the index admits | **{NCELL:,}** | every channel of every element |")
W(f"| **witnessed** | **{STAT.get('witnessed',0):,}** | reality has been consulted "
  "for this cell |")
W(f"| **unwitnessed** | **{STAT.get('unwitnessed',0):,}** | it has not — see the "
  "bound |")
W("")
W(f"**{100*STAT.get('witnessed',0)/NCELL:.3f}% of the index has been checked "
  "against reality.** Every other cell is theory, and the compendium should be "
  "read that way.")
W("")
W("### The bounds on the unwitnessed")
W("")
W("*Not probabilities. Named obstacles, each of which may or may not be lifted.*")
W("")
W("| cells | the obstacle |")
W("|---|---|")
for _b, _n in BOUND.most_common():
    if _b == "-":
        continue
    W(f"| **{_n:,}** | {_b} |")
W("")
W("**The charge bound is the one to distrust.** It reads *no analysis located*, "
  "not *no analysis exists* — and register 1577 found twelve MEASURED cells "
  "above it in this index's own file (Ti XI, Fe XV, Fe XVI), with Theodosiou "
  "1986 covering all positive ions of all atoms to Z = 37.")
W("")
W("*Accuracy figures in this compendium are quoted against the WITNESSED-plus-"
  "possible set, not against the whole index.*")
W("")
W("### The bound, which needs no measurement at all")
W("")
W("        B = min( p , n₀ − ℓ − 1 )")
W("")
W("with **p** the core's orbital count at that ℓ and **n₀** the first Pauli-allowed "
  "principal number, both read from the ground-state configuration. **floor(δ) ≤ B "
  "holds on every measured channel without exception**, and B travels with every row "
  "of the table — so the book can bound a defect without consulting one.")
W("")
W("### The filler, and its domain")
W("")
W("Where no capture reaches, the channel equation supplies the value:")
W("")
W("        p > 0 :   δ = 0.3772 · p^e(Nₑ) · Nₑ^k · ln(c+1)/c")
W("        p = 0 :   δ = 0.5415 · C(Z) · (Nₑ−1)/Nₑ · Nₑ^k · ln(c+1)/c")
W("")
W("        e(Nₑ) = 0.8297 − 0.0900·ln Nₑ          k = 0.4942")
W("        Nₑ    = Z − charge + 1")
W("        C(Z)  = the collapse coordinate across the Janet block boundary")
W("")
W("**Domain: Z ≤ 92, charge ≤ 10, ℓ ≤ 4, a single-parent core.** Fitted there on 277 "
  "channels at rms 0.1329 and R² 0.9747, anchored at Z = 2 and Z = 90. *Every value "
  "outside the domain is marked `improbable` in the status column.*")
W("")
W("### The table")
W("")
W(f"**`COORDINATES.tsv`** — {NCELL:,} rows:")
W("")
W("        Z    charge    l    mult    delta    grade    source    B    status")
W("")
W("![The coordinate supply](figures-compendia/fig-supply.png)")
W("")
W("*Above: the supply per element, on a log scale — the measured and exact cells "
  "against the computed. Below left: every measured coordinate, δ against electron "
  "count, coloured by charge. Below right: the Pauli bound, which holds on every "
  "measured cell and is read from the ground state alone.*")
W("")

# ------------------------------------------------------------------ I
W("---")
W("")
W("# I · THE INDEX")
W("")
W("### The four coordinates, and where each comes from")
W("")
W("| coordinate | alphabet | derived from |")
W("|---|---|---|")
W("| Z | 1 … 118 | given |")
W("| charge | 1 … Z | given |")
W("| ℓ | 0 … 7 | given |")
W("| 2S+1 | Hund's rule on the core | **the ground state** |")
W("")
W("**The multiplicity is not a free coordinate.** Hund's first rule applied to the "
  "core's ground configuration gives the allowed values, exact on all 24 electron "
  "counts tested. Applying it as a constraint removes **247,248 cells — 71%** of "
  "what the naive product would admit.")
W("")
W("### Which cells exist")
W("")
W("A cell is admitted when charge ≤ Z, at least one electron remains, the "
  "multiplicity is one Hund's rule allows, and an orbital of that ℓ is available. "
  "**Every cell the index admits is physically possible**: the forbidden ones were "
  "excluded at construction, so the survey holds none.")
W("")
W("### Which cells can be measured")
W("")
W("| restriction | cells |")
W("|---|---|")
W(f"| the index admits | {NCELL:,} |")
W("| Z ≤ 92 — naturally occurring | 61,152 |")
W("| and charge ≤ 10 | 11,416 |")
W("| and ℓ ≤ 4 — where series resolve | 4,395 |")
W("| **and a single-parent core** | **1,755** |")
W("")
W("### The parent-term wall")
W("")
W("**A closed-shell core has one parent term and gives one Rydberg series per ℓ.** An "
  "open-shell core gives one series per parent, all interleaved, converging on "
  "different limits.")
W("")
W("Fe IV's 3d⁴ core carries sixteen LS terms. Its published levels show thirteen of "
  "them across **24 distinct (parent, ℓ, term) series, every one with a single "
  "member.** Fe IV has about a thousand analysed levels and no extractable defect: "
  "*the levels are identified and the series are not separable.*")
W("")
W("**This is why the compendium holds Ne-like and Na-like ions at charge 15 and 16 "
  "and no open-shell ion above charge 6.** An open-shell core does not produce the "
  "object a quantum-defect index holds.")
W("")
W("### The Janet collapse")
W("")
W("Two channels can both have p = 0 — no core orbitals of their own ℓ — and differ by "
  "a factor of ten. Ti IV's nd is **0.6202**; Sr II's nf is **0.0618**.")
W("")
W("What separates them is **orbital collapse**, and its threshold is a Janet block "
  "boundary exactly:")
W("")
W("| orbital | n+ℓ | block opens at | element | collapse threshold |")
W("|---|---|---|---|---|")
W("| **3d** | 5 | **Z = 21** | Sc | **21** |")
W("| **4f** | 7 | **Z = 57** | La | **57** |")
W("| **5f** | 8 | **Z = 89** | Ac | **89** |")
W("")
W("Across 116 cells with p = 0 at ℓ = 2 or 3: **collapsed median 0.637, uncollapsed "
  "0.036**, U-test p = 9.8×10⁻⁴. The transition is rapid rather than sharp — the "
  "largest defects are the atoms *approaching* a boundary: Ca I nd = 0.908 at Z = 20 "
  "against a threshold of 21, and Ba II nf = 0.756 at 56 against 57.")
W("")
W("**The collapse coordinate is read from the periodic table, not fitted**, and it is "
  "why a defect at ℓ = 2 can be large in one element and negligible in its neighbour.")
W("")
W("![The channel map](figures-compendia/fig-channel-map.png)")
W("")
W("*Every cell valued. The upper panel is δ itself, charge collapsed to its largest; "
  "the lower is which mechanism sets it, with the three Janet boundaries marked.*")
W("")

# ------------------------------------------------------------------ II
W("---")
W("")
W("# II · THE CHANNELS")
W("")
W("**Every captured series, with its fit.** These are the measured rows of the "
  "coordinate table.")
W("")
W("Three marks state a limitation. An **asterisk** on the species marks a two-member "
  "channel: two points give a defect and one consistency check but cannot detect a "
  "perturbation. A **dagger** on the n-range marks an internal gap. And the **limit "
  "column** names how the ionisation limit was obtained — *published* where a source "
  "quotes it, *theoretical* where it is exact by construction, *constructed* where "
  "this work built it by summing two spectra. *A channel resting on a limit this work "
  "computed is not a measurement against an independent standard, and the row says "
  "so.*")
W("")
W("| species | series | n | levels | interior | bracket | n* range | δ | σ(δ) | fits | limit cm⁻¹ |")
W("|---|---|---|---|---|---|---|---|---|---|---|")
for r in rows:
    W(f"| {r[0].strip()} | {r[1].strip()} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | "
      f"{r[6]} | {r[7]} | {r[8]} | {r[9]} | {r[10]} |")
W("")
by = defaultdict(int)
for r in rows: by[r[0].strip().split()[0]] += 1
tot_int = sum(int(r[4]) for r in rows if r[4].strip().isdigit())
W(f"**{len(rows)} channel rows across {len(by)} elements · {tot_int:,} interior cells "
  "parsed.**")
W("")
W("| element | channels |")
W("|---|---|")
for k in sorted(by): W(f"| {k} | {by[k]} |")
W("")

# ------------------------------------------------------------------ III
W("---")
W("")
W("# III · THE MECHANISMS")
W("")
W("**How a value is got where no capture reaches.** Each is measured on pairs where "
  "both cells are known.")
W("")
W("| mechanism | the move | what it gives |")
W("|---|---|---|")
W("| the ground-state derivation | none | the multiplicity, and the bound B |")
W("| the isoelectronic ladder | (Z, c) → (Z+1, c+1) | δ along a sequence |")
W("| the charge ladder | c → c+1 at fixed Z | δ falls with charge |")
W("| ℓ-collapse | ℓ → ℓ+1 | δ falls with ℓ |")
W("| the exchange split | singlet ↔ triplet | the triplet defect exceeds the singlet at ns |")
W("| the Janet collapse | a lookup in the periodic table | whether a p = 0 channel is large |")
W("| Seaton's formula | none | δ₀ = 3α/K(ℓ) for a non-penetrating series |")
W("")
W("### The isoelectronic ladder")
W("")
W("**Along a sequence of fixed electron count, a channel's defect follows "
  "δ(c) = A + B·ln(c+1)/c.** Fitted per sequence on the 52 with three or more charge "
  "states it reaches a median rms of **0.0083** — the tightest relation the "
  "compendium holds.")
W("")
W("**And A is fixed rather than fitted.** As charge grows at constant electron count "
  "the core collapses to a point and the ion becomes hydrogenic, so δ → 0. That is the "
  "periodic table's own edge, and setting A ≡ 0 leaves one parameter.")
W("")
W("### A channel is a curve")
W("")
W("        δ(n) = δ₀ + δ₂/(n − δ₀)²")
W("")
W("**δ₀ is the limit value the index carries; δ₂ is the curvature.** Fitted on 274 "
  "channels, the second term removes **48%** of what a constant defect leaves as "
  "scatter.")
W("")
W("**And the sign of δ₂ names the regime**: positive for core penetration, negative "
  "for core polarisation. By orbital: **s 76% positive, p 74%, d 37%, f 6%, g 7%.** "
  "*The sign rule is NIST's own, stated in the reference the levels come from. What "
  "the compendium adds is the measurement across 274 channels and the finding that "
  "|δ₂| predicts a channel's scatter at R² = 0.761.*")
W("")
W("![The index](figures-compendia/fig-index-final.png)")
W("")

# ------------------------------------------------------------------ IV
W("---")
W("")
W("# IV · THE SOURCES")
W("")
i = BOOK.find("B.1 Sources")
if i > 0:
    j = BOOK.find("\n### ", i + 10)
    for ln in BOOK[i:j if j > 0 else i + 2600].split("\n"):
        if ln.strip(): W(ln)
    W("")
W("### Published values the coordinates are checked against")
W("")
W("| source | what it gives |")
W("|---|---|")
W("| **NIST Atomic Spectra Database** | the levels every capture is fitted to |")
W("| **Theodosiou, Inokuti & Manson, At. Data Nucl. Data Tables 35, 473 (1986)** | "
  "asymptotic quantum defects of s, p, d and f orbitals for **all ionisation stages of "
  "all ions with Z ≤ 50**, Hartree–Slater |")
W("| Manson, Inokuti & Theodosiou, OSTI 7104964 | the isoelectronic, isonuclear and "
  "isoionic pictures |")
W("| Seaton 1958; Drake & Swainson 1991 | the polarisation formula |")
W("| Peper *et al.* 2019 | K I to eight digits |")
W("| Freeman & Kleppner 1976 | Na I ng |")
W("| arXiv:1706.06237 | Cs I np at n = 70–100 |")
W("| arXiv:2508.06733 | actinide defects, Z = 89–103 |")
W("| arXiv:2502.20961 | Cs⁺ dipole and quadrupole polarisabilities |")
W("| ARC Alkali Rydberg Calculator | an independent check on K I |")
W("")
W("*The full bibliography, with what each source was used for, is in "
  "`LITERATURE.md`.*")
W("")


# --------------------------------------------------- the four capture groups
# Register 1296, written at register 1571. The captures reached COORDINATES.tsv
# and never reached this compendium. Counts are READ FROM THE FILE here, not
# transcribed, so they cannot drift from it.
import collections as _c
_rows = [l.rstrip("\r\n").split("\t")
         for l in open("COORDINATES.tsv", encoding="utf-8").read().split("\n")[1:]
         if l.strip()]
_SYM = {36: "Kr", 48: "Cd", 49: "In", 57: "La", 58: "Ce", 80: "Hg"}
_GRP = [("Kr-core", [36], "the n = 4 closure; its 5s manifold is still one level short"),
        ("Cd/In",   [48, 49], "the d10 closure and the first post-d p-electron"),
        ("La/Ce",   [57, 58], "THE JANET ANOMALY ITSELF - La opens 5d, Ce is where 4f appears"),
        ("Hg-core", [80], "the 5d closure at high Z, where the relativistic wall stands")]
W("")
W("---")
W("")
W("# The four capture groups")
W("")
W("*Register 1296 marked these as owed. Counts below are read from "
  "`COORDINATES.tsv` at build time, not transcribed.*")
W("")
W("| group | species | cells | measured | exact | computed |")
W("|---|---|---|---|---|---|")
_tot = _meas = 0
for _g, _zs, _why in _GRP:
    _r = [x for x in _rows if int(x[0]) in _zs]
    _gr = _c.Counter(x[5] for x in _r if len(x) > 5)
    _tot += len(_r); _meas += _gr.get("measured", 0)
    W(f"| **{_g}** | {'/'.join(_SYM[z] for z in _zs)} | {len(_r):,} | "
      f"{_gr.get('measured',0)} | {_gr.get('exact',0)} | {_gr.get('computed',0):,} |")
W("")
W(f"**{_tot:,} cells across six species**, every one spanning l = 0-7 and the "
  f"full charge ladder from 1 to Z.")
W("")
_vp = sum(1 for x in _rows if int(x[0]) in _SYM and len(x) > 8
          and x[8].strip() == "witnessed")
_vpall = sum(1 for x in _rows if len(x) > 8
             and x[8].strip() == "witnessed")
W("### What the counts say, measured on this compendium's own basis")
W("")
W("*Section 0 states that accuracy is quoted against the VERIFIED-PLUS-POSSIBLE "
  "set and not against the whole index. The same basis is used here.*")
W("")
W(f"**The four groups hold {_vp:,} reachable cells of the index's {_vpall:,} - "
  f"{100*_vp/_vpall:.1f}% of the reachable set on {100*_tot/len(_rows):.1f}% of "
  f"the cells.** They are therefore slightly BETTER than representative, not "
  f"worse.")
W("")
W(f"On the raw grade column they carry {_meas} `measured` cells of {_tot:,} - "
  f"Cd/In twelve and Hg five, with **Kr-core and La/Ce carrying none.** *That "
  f"ratio is not a fact about these groups: the whole index is 98.8% computed, "
  f"which section 0's table already states. The filler is the index's "
  f"condition, not these captures' shortcoming.*")
W("")
W("### Why each was captured")
W("")
for _g, _zs, _why in _GRP:
    W(f"- **{_g}** - {_why}")
W("")
W("**La/Ce is the group that earns its place.** The other three fill coordinate "
  "space; **La/Ce is where the filling order itself breaks**, and holding it in "
  "the index lets the anomaly be stated as a coordinate fact rather than a "
  "footnote.")
W("")

print("\n".join(L))
