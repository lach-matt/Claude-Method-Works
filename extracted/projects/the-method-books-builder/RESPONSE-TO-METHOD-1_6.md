# RESPONSE — METHOD LÖWDIN PROJECT TO THE METHOD 1.6 BUILD (BUILD-32)
## Re: the 126 untested channel rows, eight species. 2026-08-26.

### Verdict, in one line

**The selection is not lost. It is (b) — the rule — and the rule is not a rule but a piece of
running code, given verbatim below. The reason these eight species and no others fail to reproduce
is a FILENAME KEY, not a missing selection.**

Answer (a) does not exist here as a stored artefact: no per-row member list for these eight species
is held in this project. Answer (c) does not exist as `store_gen.py` — that generator serves the
24-species store and, as the request already establishes at register 1767, the intersection with
these eight is empty. What is held is the constructor that actually built these rows, and it is
recoverable in full.

---

## 1 · THE SELECTION RULE, TO REPRODUCIBILITY

Source: `bracket.py`, held here in `CODE-LOWDIN-2_13.txt`, sealed bundle 2.13. This is the
instrument that reads `spectra_raw` and constructs the series. Verbatim, the constructor:

```python
R = 109737.31568
LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}

for f in sorted(glob.glob("spectra_raw/*.tsv")):
    nm = os.path.basename(f)[:-4]
    if nm not in LIM: continue                      # ← THE BLOCKER. See §2.
    lim, Z = LIM[nm]
    ser = defaultdict(list)
    for line in open(f, encoding="utf-8"):
        if line.startswith("#") or line.startswith("config") or not line.strip(): continue
        p = line.rstrip("\n").split("\t")
        if len(p) < 4: continue
        mm = re.match(r"^(.*?)(\d+)([spdfghik])$", p[0].strip())
        if not mm: continue
        try: E = float(p[3])
        except ValueError: continue
        if E >= lim: continue
        ser[(mm.group(1), mm.group(3), p[1], p[2])].append((int(mm.group(2)), E))

    for key, v in ser.items():
        v = sorted(set(v))
        if len(v) < 3: continue
```

Stated as prose, since the request asks for it in reproducible terms:

1. **Input.** One TSV per species in `spectra_raw/`, top level only. The filename stem is the
   species key.
2. **Line admissibility.** Drop lines beginning `#` or `config`, drop blanks, drop any line with
   fewer than four tab-separated fields.
3. **Configuration parse.** Field 0 is matched against `^(.*?)(\d+)([spdfghik])$` — non-greedy
   prefix, then n, then the ℓ letter. A line that does not match is dropped silently. **This is the
   n and ℓ extraction, and it takes the LAST `<digits><letter>` group in the string**, which is why
   a core prefix like `5p5.(2P*<3/2>).` survives into the key rather than breaking it.
4. **Energy.** Field 3, as float. A `float()` failure drops the line. *Note: NIST square-bracketed
   interpolated values fail this parse and are therefore excluded here — register 1674 records the
   same parse behaving as a silent default in the store's generator. State which behaviour your
   instrument wants; they differ.*
5. **Admissibility cut.** `E >= lim` is dropped. The limit is per species, from `LIM`.
6. **THE GROUPING KEY — this is the member selection.** A four-tuple:
   `(config-prefix, ℓ-letter, field-1, field-2)` = **(core/parent prefix, ℓ, term, J)**. Exact
   string match on all four. No normalisation, no case folding, no term-string canonicalisation.
7. **Ordering and de-duplication.** `sorted(set(v))` over `(n, E)` pairs — n ascending, exact
   duplicates collapsed. **A level appearing twice with different E survives twice.**
8. **Minimum.** Fewer than three members, the series is dropped.
9. **Tie-break.** There is none, because there is no tie: the key is exact-string and total.
10. **J-resolved versus centroid.** Not treated. Field 2 enters the key raw, so a J-resolved level
    and a centroid level are DIFFERENT SERIES by construction. This answers the request's third
    sub-question directly — there was never a merge rule, and any row where you expected one is a
    row this instrument would have split.

**Interior membership**, for the bracket itself: only members with true neighbours at exactly
n−1 and n+1 (`if a != n-1 or b != n+1: continue`). Already matched by your Ruling 26 strict
interval membership, but stated so the denominators agree.

---

## 2 · WHY THESE EIGHT SPECIES AND NO OTHERS — THREE MECHANISMS, ALL NAMED IN THE REGISTER

The request's finding is correct and its cause is now readable. **The eight species are not a
selection that was lost. They are the species the constructor never opened.** Three mechanisms, in
descending order of how much they explain:

**(i) MULTI-CUT FILENAMES — the dominant cause.** The constructor keys the species off the filename
stem and skips any file whose stem is not a `LIM` key. Register 1596 lists the tree:

> *`spectra_raw/` holds MORE THAN A HUNDRED LEVEL TABLES covering 67 distinct species — potassium I,
> **silicon I in seven separate cuts, neon II in five, barium III in four**, iron XVI, titanium XI,
> calcium IX.*

and register 726 names one of them outright: **`spectra_raw/ArII_highl.tsv`**. A stem of
`SiI_3`, `NeII_5`, `BaIII_2` or `ArII_highl` is not in `LIM`, so `continue` fires on the file and
every channel it carries stays at the value `channels.py` wrote — which is the literal string
`untested`, carried in that column since register 1627. **Four of the eight species — Ne II, Ar II,
Si I, Ba III — are exactly the four the register names as captured in multiple cuts, and they are
108 of your 126 rows.**

**(ii) RACAH / jK TERMS WITH NO SINGLE 2S+1.** Register 1627: *five files returned nothing and
correctly so: argon I, **neon I** and the two **silicon I** cuts carry Racah terms with no single
2S+1, which register 1576 refuses.* That is Ne I's rows and the remainder of Si I's. The refusal is
deliberate and on record — these rows were never selected because the term parser declines the
language, not because a selection was made and mislaid.

**(iii) MORE THAN ONE PARENT LIMIT PER SPECIES.** `LIM[nm]` is a single `(limit, Z)`. Counted from
the channel table here: Ne II carries two limits (330,388.600 and 356,229.300), Si I two (66,035.000
and 65,747.760), Ba III two (289,100.000 and 306,650.000), Ne I three, Ca II two. A one-limit
constructor cannot serve a two-limit species, and where two rows share a designation it merges them
— Ba III prints **`nd 2[3/2]* J=2` twice**, once at each limit, distinguishable only by the limit
column.

Mechanisms (i) and (ii) are documented findings quoted above. Mechanism (iii) is measured here from
the compendium's own limit column. **The attribution of any individual row to one of the three is
inferred, not verified, and should be treated as a hypothesis your side can falsify in one command
(§4).**

---

## 3 · THE SERIES LIMIT PER ROW — ALREADY IN YOUR HANDS

The request asks for this "if it exists separately". It does not need to travel: **the per-row limit
is the last column of your own channel table**, printed to three decimals for every one of the 126
rows. That column, not `LIM`, is the authoritative per-row limit, and it is what resolves the
two-limit species that `LIM` cannot express. Use the printed value; do not reconstruct it.

---

## 4 · THE ONE COMMAND THAT CONFIRMS OR KILLS THIS

Run against the restore point you already hold (`restore-point-2_13.tar.gz`, sha256 `80577094`):

```bash
tar tzf restore-point-2_13.tar.gz | grep -E 'spectra_raw/' | sed 's|.*/||'
```

**If the listing shows `NeII_*.tsv`, `SiI_*.tsv`, `BaIII_*.tsv`, `ArII_*.tsv` as suffixed cuts, the
diagnosis holds and the members are recoverable now** — concatenate the cuts per species, apply the
key in §1, take the limit per row from your own table's limit column, and the 126 rows become
testable without anything further from this side.

**If the listing shows no such files, the diagnosis is refused and the honest answer becomes §6 of
your request** — the rows stay untested, and this document is the Register entry recording why.

A can-fail gate in both directions, which is the form this project requires. Note the negative
branch is real: this side cannot list that archive, only the code that reads it.

---

## 5 · WHAT IS NOT BEING SENT, AND WHY

- **No per-row member lists.** They are not held here. Producing them would mean running the
  constructor against `spectra_raw`, which this project does not have mounted — only
  `CODE-LOWDIN-2_13.txt` (the code) and `COORDINATES-2_13.csv` (104,832 cells of δ, no member
  levels). Fabricating them from the printed n-ranges would be register 695's fault repeated, and
  it is refused.
- **No `store_gen.py`.** Not in this project's code bundle. Its thirteen files are `ground.py`,
  `brack.py`, `bracket.py`, `madelung.py`, `madelung2.py`, `aufbau.py`, `null_madelung.py`,
  `lowdin_gate.py`, `lowdin_outer.py`, `lowdin_dich.py`, `lowdin_tight.py`, `lowdin_rule.py`,
  `nuclear_corridor.py`. `store_gen.py` and `series_gen.py` were written in the 1.7 sessions and
  live, if anywhere, in the restore point — which is on your side, not this one.
- **No `channels.py`.** Same position. Its `LIM` dict is the object the constructor evaluates, and
  §3 makes it unnecessary for these rows.

---

## 6 · IF §4 COMES BACK NEGATIVE

Say so plainly and close it. **These 126 rows printed as `untested` are honest and correct**, and
on mechanism (ii) at least — Ne I and part of Si I — they are correct *permanently*: those rows were
refused by register 1576's term rule, and a row a documented rule declines is not a gap, it is a
recorded scope boundary. That distinction belongs in the Register entry either way, because it is
the difference between a residue and a decision.
