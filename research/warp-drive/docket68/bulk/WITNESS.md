# Two witnesses: the README and the corridor (M-RULINGS item 145; deduced and computed; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)". The first draft said the corridor witnesses N exactly and
that the pair is a checksum fixing one string; both over-stated (History).

## What you said

- **Item 145:** *"There is ever only one true complete reconstruction. And it is supported by two witnesses, the README
  and the corridor"*.
- **Carried:** H-ONE-RECONSTRUCTION and H-TWO-WITNESSES.
- **The instrument:** `witness.py`. Selftest 6/6.
  - Four checks are STRUCTURAL: they hold by construction.
  - Two are computed: the quantum-correction ratio, and the measured-G resolution.

## What each witness carries

### 1. The corridor carries the count, N (T1)

- **The corridor's throat area is the README's bit count:** 4πr_min² = N·A_bit (exactE.py; chain.py's coefficient).
- **One bit adds exactly one A_bit of area** (STRUCTURAL). So classically N and N + 1 give different throats.

### 2. But the throat cannot carry that distinction by itself (T2)

- **Quantum corrections smear the throat by about 4.5 bits.**
  - The board's estimate of quantum corrections at the throat is π/(N ln 2) (kderive.py K2: an estimate of standard
    order, not READ).
  - One bit is 1/N of the area.
  - **Their ratio is π/ln 2 = 4.53 at every N.** So the classical throat is uncertain by about 4.5 bits' worth of area,
    however large the README.
- **Measurement is far coarser.** G is known to 2.2 parts in 10⁵ (chain.py), so a measured throat fixes N only to about
  6×10¹⁰ bits at the board's example README.
- **So N is exact only through your item 137: the passage *is* N bits** (H-PASSAGE-IS-N). It is not exact through the
  throat's geometry.
- **This sits in tension with your M-EXACT-VALUES** (item 125: *"The device will only ever be able to use precise
  values"*). The values are exact in the theory, but no measurement of a throat reaches one bit. That reading is the
  board's.

### 3. The corridor does not carry the content (T3)

- **All 2^N strings of length N share one throat** (STRUCTURAL).

### 4. What the two together add (T4)

- **The corridor adds a length check.**
  - A README one bit short or one bit long is rejected (STRUCTURAL).
  - **None of the 2^N − 1 same-length substitutions is caught** (STRUCTURAL).
- **The string itself is fixed by the README alone, under your one fixed exact encoding** (item 136, answer 5).
- **Under item 137, the corridor also witnesses that N bits crossed.** A string alone cannot.
- **So the board reads your two witnesses as two different testimonies:**
  - the README, to *what*;
  - the corridor, to *how much*, and *that it crossed*.
  - That reading is the board's.

## What this does to the question of ε

- **Two readings of "only one true complete reconstruction":**
  - **(i) no tolerance at all.** The reconstruction is complete only if it is exact.
  - **(ii) completeness measured against the two witnesses** (the README's content and the corridor's count), not
    against the original's physical frequencies.
- **Under (ii), a difference in μ does not make a reconstruction incomplete by itself.** It enters only through what
  position 2 can realize (item 136 H).
- **That makes the encoding matter.** Under the board's H-ALPHA-IS-LIGHT and H-SAME-HAMILTONIAN, with your
  H-LIGHT-INVARIANT (*"light likely doesn't vary"*):
  - the electrons' structure and the Löwdin table are the same in every universe (samelight.py, cited, not computed
    here);
  - molecular frequencies move with μ (nucleus.py U4, under your H-LAWS-ON-NUCLEUS).
- **So the board offers H-INVARIANT-ENCODING:** the one fixed exact encoding is written in what every universe shares,
  such as element identity and electron configuration.
- **A limit on that reading:** your item 144 lets universes differ in which nuclei are stable. So an element named by Z
  may be unstable, or absent, at position 2. That is item 136 H's *"what can be reconstructed"*.

## Named hypotheses

- **Yours:**
  - H-ONE-RECONSTRUCTION, H-TWO-WITNESSES (145);
  - H-LAWS-ON-NUCLEUS (144);
  - H-LIGHT-INVARIANT (143);
  - H-PASSAGE-IS-N (137);
  - H-FIXED-ENCODING (136, answer 5);
  - item 136 H;
  - M-EXACT-VALUES (125).
- **The board's:**
  - H-ALPHA-IS-LIGHT, H-SAME-HAMILTONIAN;
  - H-COPY-TAKES-P2-LAWS;
  - H-INVARIANT-ENCODING;
  - H-MANY-BITS (the chain read classically, kderive.py).

## OPEN

1. **Which reading of "only one true complete reconstruction" is yours:** (i) no tolerance, or (ii) measured against
   the two witnesses.
2. Whether the encoding is written in invariants (H-INVARIANT-ENCODING).

## History (verifier, 2026-10-07)

Ten findings, all applied:

1. **The STRUCTURAL count was wrong.** The trivially true checks are now marked, and two computed ones replace them.
2. **"The corridor tells N from N + 1 exactly" failed by the board's own K2.** The correction is 4.5 bits' worth at
   every N. Exactness is now credited to item 137, not to geometry.
3. **The M-EXACT-VALUES link** is now the board's reading, with the tension stated: measured G fixes N only to about
   6×10¹⁰ bits.
4. **"Checksum … fix one reconstruction" overstated.** A length check catches no substitution, and this is now
   computed.
5. **T3 and T5 were listed but not checked.** T5 is now cited, not claimed as computed.
6. **The Löwdin-table claim's conditions** are now stated, and the missing hypotheses are listed.
7. **The stricter reading (no tolerance)** is now offered. Item 136, answer 4 is no longer used as grounds.
8. **"1/(2N) of the throat"** was ambiguous. It is now "one bit adds exactly one A_bit of area".
9. **The missed findings** are stated.
10. **The instrument loads chain.py once.**
