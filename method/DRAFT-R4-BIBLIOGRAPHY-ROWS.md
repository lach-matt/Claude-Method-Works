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
