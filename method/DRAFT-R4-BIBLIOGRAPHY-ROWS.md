# DRAFT — the eight bibliography rows with no correspondent in the six volumes

**NOTHING IN THIS FILE IS IN THE STORE.** It is a measurement written for M's ruling. No byte of any
volume has moved and no Register entry has been written. `method/proofs/bibindex3.py` is held (its
`OBJECT` fixture pins the pre-import 127); these figures are its current run, measured at BUILD293.

## What was measured

After the imports of W-292…W-295, `bibindex3.py` reports

    OBJECT 143 | CITED 9 | CITED-FULLER 2 | IMPORT-OWED 8

and the eight `IMPORT-OWED` rows are the whole residue. They were **read, not sorted by shape.**
Six of the eight are not works the six volumes fail to cite. They are faults in the bibliography's
own rows, and each one is settled by the volume's own prior-art line.

## Class 1 — the row pairs an author with a CO-CITED author's year (4 rows)

In every case the correct row already exists **and already carries the same handle**, so nothing is
lost by removing the false one and nothing is gained by importing a work.

| row | handle | what the object's own line says | the row it duplicates |
|---|---|---|---|
| `1913 \| Pauli` | `L.def` | L1468 *"Bohr 1913; Pauli 1925"*, L1470 *"the shell-structure rules of Bohr (1913) and Pauli (1925)"* | `1925 \| Pauli` (carries `L.def`); the year is Bohr's |
| `1958 \| Pauli` | `Q.delta` | L3082 *"the Pauli bound (Pauli 1925), the Thomas-Fermi deficit (Fermi 1928) and Seaton polarisation (1958)"* | `1925 \| Pauli` (carries `Q.delta`); the year is Seaton's |
| `1982 \| Racah` | `T.trad` | L1248 *"Racah 1943; … Freuder 1982"* — Racah died in 1965 | `1942 \| Racah` and `1943 \| Racah`; the year is Freuder's |
| `1964 \| Moebius` | `G.book` | L1520 *"Rota, On the foundations of combinatorial theory I: theory of Moebius functions, Z. Wahrscheinlichkeitstheorie 2 (1964) 340-368"* | `1964 \| Rota` (carries `G.book`); **"Moebius" is a word in Rota's title, not an author** |

Möbius the person is dated **1865** in this volume (L1180, L1230, the one-sided band, with Listing
1861). Neither has a bibliography row at all — a separate matter, and not this one.

`handlemap.py` corroborates two of the four independently: `L.def` resolves to *The definition of Λ*,
`G.book` to *The book as an index*.

## Class 2 — one work printed as two rows (2 rows, 1 work)

| rows | handles | the work as the volume prints it |
|---|---|---|
| `1999 \| Deville` and `1999 \| Hentenryck` | `A.env A.orient A.r4 T.tight` / `A.orient A.rule A.stair A.staircls T.tight` | L176, L332, L470: **Deville, Barette & Van Hentenryck, *Artif. Intell.* 109 (1999) 243-271** — one paper, three authors, split into two rows, and neither row is the full author list M ruled for |

## Class 3 — a year the volumes never print (1 row)

`1937 | Shannon | L.bits`. The bibliography carries **three** Shannon rows — 1937, 1938, 1948 — and
the volumes' prior-art lines name only two years: **1938** (L626, *Trans. AIEE* **57** (1938) 713-723,
the relay-circuit paper) and **1948** (*Bell Syst. Tech. J.* **27**). `handlemap.py` reports `L.bits`
**UNRESOLVED — no evidence in the volumes**: the only row for Shannon 1937 points at a handle nothing
in the six supports.

## Class 4 — the unpublished companion papers (2 rows)

`2026 | Lach, *The Löwdin Solution*` and `2026 | Lach, *The Three-Body Problem for Unknown Masses*`.
Void under M's six-volume ruling (W-291): a reader of the six cannot reach either.

## What this would cost the printed count

The bibliography prints its own extent as **162 works**. Class 1 removes four rows, class 2 merges
two into one, class 3 is either a year correction (162 unchanged) or a fifth removal, and class 4 is
M's. The four duplicate pairs already put to M (1964, 1969, 1983, 1999) overlap class 1 and class 2
at 1964 and 1999 — **they are the same finding read properly, and the merge M was asked about at
1964 is a deletion, not a merge, because "Moebius" is not an author of that work.**

RECORDED, NOT REPAIRED.


---

# THE MECHANISM, PROVED FROM HELD MATERIAL

M's instruction on the previous item was *"search the repo"*, and it applies here too. **The generator
is held**, at `extracted/archives/restore-point-2-13/compendium.py`, beside the register data
`mathreg.py` it reads. Run its own regex, verbatim, over that data: **it reproduces all seven rows
with exactly the handles the volume prints.**

| row | the span the generator matched | what happened |
|---|---|---|
| `1913 Pauli` `L.def` | `Pauli 1925 PRIOR ART: … the shell-structure rules of Bohr (1913)` | **the match crosses the `src`/`check` field boundary** — the generator joins the two fields with a space, so `src`'s last name pairs with `check`'s first parenthesised year |
| `1937 Shannon` `L.bits` | `Shannon 1938 PRIOR ART: Birkhoff (1937)` | the same crossing. **This row is not a Shannon year at all — it is Birkhoff's 1937 on Shannon's name** |
| `1982 Racah` `T.trad` | `Racah 1942 PRIOR ART: … is Freuder (1982)` | the same crossing |
| `1958 Pauli` `Q.delta` | `Pauli bound (Pauli 1925), the Thomas-Fermi deficit (Fermi 1928) and Seaton polarisation (1958)` | within one field: the regex anchors on the first name and skips up to **90 characters** to a later parenthesised year |
| `1964 Moebius` `G.book` | `Moebius inversion over a refinement lattice is Rota (1964)` | **"Moebius" is a word in the sentence**, not an author |
| `1999 Deville` / `1999 Hentenryck` | `Deville, Barette & Van Hentenryck (1999)` under one handle set, and the bare `Hentenryck 1999` under another | **one work written two ways in different objects becomes two rows** |

The pattern is one clause: `([A-Z]\w+…)(?:'s)?[^.;]{0,90}?\((1[6-9]\d\d|20[0-2]\d)\)`. **Ninety
characters of anything but a period or a semicolon may sit between the name and the year**, and the
two fields are concatenated before it runs.

## This corrects two things I put to M

1. I called `1937 Shannon` *"a year the volumes never print"*. **It is Birkhoff's year on Shannon's
   name**, taken across a field boundary — a sharper and different statement.
2. I called the four *"an author paired with a co-cited author's year"*. Right in effect, but the
   mechanism is a `src`/`check` join and a 90-character window, which is testable and now tested.

## Does the mechanism make them right?

**No — and that is the test the channel table passed and this fails.** There, Part II's opening
sentence *"Every captured series, with its fit"* made two rows for one series correct by
construction. Here the section's own opening is **"Every object of this compendium names a work"**,
and a (name, year) pair that no object attributes is not a work an object names.

**And register 1736 already ruled this generator's other output.** It removed ten rows *"no reader
could cite"* — a possessive, callout terms, *"COVER 1972" (the problem, not Karp)*, *"Killing 2024"
(a field, beside Sorce)*, five status words with dates the generator read as years — and expanded
`BFMY 1983` to its full author list. **Those ten are the case where the NAME is wrong. These six are
the case where the name is a real author and the YEAR belongs to someone else**, which is why a
match by author could not see them, and register 1890 now records that blind spot.

**The precedent's repair form is stated in the volume itself**: the rows are removed, the count is
restated, and the prior count is kept beside it — *"162 works … the count was 172."*
