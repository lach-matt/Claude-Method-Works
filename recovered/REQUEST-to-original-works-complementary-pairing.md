# Request to the original-works project — the seed's complementary-pairing property

**From:** the main-volume prose pass (The Method 1.6), source Chapter 14 §14.5.14.
**Purpose:** determine whether a specific structural property was tested-and-established (or is derivable) but never written into the book — so that, if so, the reader volume may state it as a law with evidence, rather than as a description of Λ₈.
**Discipline:** this is a confirmation question. The prose currently states the property at its recorded status (a described property, not a law) and will not be raised unless this request returns "established" or "derivable with proof." Do not assume; answer from the record.

---

## The property in question

Source §14.5.14 reduces the minimum seed of Λ₈ to five cells and writes each as a bit-word (1 = coordinate at its maximum, 0 = at its minimum, · = interior):

```
  n  l  k  q  e  f  g 2S
  0  0  ·  ·  1  1  ·  ·     corner 1    1s² → 3p    out
  ·  1  1  1  0  0  0  1     corner 2    2p³ → 1s    in
  ·  1  1  1  ·  1  1  0     corner 3    2p³ → 2p    across
  1  1  0  0  1  1  0  0     corner 4    3p¹ → 3p    still
  1  0  0  ·  1  0  ·  ·     unit  5     3s¹ → 3s    the unit
```

The recorded findings on these five:
1. **Corner 1 and corner 2 are exact complements** — differ on 3 bits of the 3 they both fix.
2. **Corner 3 and the unit cell are exact complements** — 3 of 3.
3. **Corner 4 is the only fully specified cell — 11001100 — the static transition.**
4. **Every one of the eight coordinates receives both a 0 and a 1 across the five** — no column is one-sided.

**The recorded status (Registers 602–605):** *"Measured at one cap setting. Whether the complementary pairing survives other caps is not tested, and until it is this is a description of Λ₈ and not a structural law."*

## What is already known (so the request is precise about the gap)

- The seed's **size and constructibility** WAS tested across caps: the seed is determined by φ̂ alone, verified at four cap settings; |Λ| grows ~31× across them while the seed grows ~1.4×, compression rising 24× → 518×; the seed is bounded by O(d² × cap depth), not by |Λ|. (This is on record.)
- So the gap is narrow and specific: **the size law is cap-tested; the complementary-pairing bit-structure of the seed cells is not.** The request is only about the latter.

## The two questions

**Q1 — Was it tested?**
In the original-works sessions, was the complementary-pairing structure of the minimum-seed cells (properties 1–4 above) ever computed at cap settings other than the one Λ₈ setting — i.e. was it established that at other caps the minimum seed still resolves to a set of bit-words in which (a) the corners pair as exact complements and (b) every coordinate receives both a 0 and a 1? If yes, please return the cap settings tested, the seed cells found at each, and the result — even if the result was that the pairing FAILS at another cap (a negative is as decisive as a positive here).

**Q2 — If it was not tested, can it be derived?**
Is the complementary-pairing property DERIVABLE from results already established — rather than requiring fresh computation? Specifically, does it follow from:
- the set-cover characterisation of the seed (elements = envelope steps, sets = cells), together with
- the requirement that a covering set reach the **breadth** of the object (the Carathéodory = breadth result), and
- the particle–hole / reflection symmetry of the coupling axes already proved for the tower (terms(ℓᵏ) = terms(ℓ^(4ℓ+2−k)))?

The intuition to test (offered as a lead, not an assumption): a minimum cover of the envelope steps must witness every coordinate at both extremes, because an envelope step exists at each extreme of each coordinate and a cover omitting one extreme would leave that step uncovered — which would make property 4 ("every letter spoken both ways") a **consequence of minimality**, cap-independent by construction. If that argument (or a corrected form of it) holds, property 4 is a law now, with proof. Properties 1–3 (the specific exact-complement PAIRINGS) are stronger and may be Λ₈-special; please assess them separately from property 4.

## What we need back

For each of the four properties, one of:
- **ESTABLISHED** (tested across caps) — with the caps and the seed cells found;
- **DERIVABLE** — with the derivation, or enough of it that the Mathematical Compendium can carry a full expansion;
- **OPEN / Λ₈-SPECIFIC** — in which case the reader prose keeps its current honest status and states it as a described property of Λ₈.

If property 4 is derivable but properties 1–3 are not, that is a useful and publishable split: the "every letter both ways" law general, the specific complement-pairings a feature of Λ₈. We can state exactly that, with evidence.

## Where the answer lands

- If ESTABLISHED or DERIVABLE: the reader chapter (14A §14.5.14) is raised from "a described property of Λ₈, not yet a structural law" to a stated law with a compendium pointer, and a full expansion is authored (currently held as [MC-54], and would gain a proof rather than a description). The derivation becomes subject-matter for the Mathematical Compendium.
- If OPEN: prose unchanged; the item stays a watched open finding (logged in OWED-REGISTER-EXPANSIONS.md) for the reader-audit pass.