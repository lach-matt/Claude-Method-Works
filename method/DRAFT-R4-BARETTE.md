# DRAFT — one co-author's name, wrong at six sites in four volumes

**NOTHING IN THIS FILE IS IN THE STORE.** No volume byte has moved, no Register entry written.

## What it is

The corpus cites one paper — *Constraint satisfaction over connected row-convex constraints*,
**Artificial Intelligence 109 (1999) 243–271** — under **two different second authors**, and the two
are different real people.

| spelling | sites | where |
|---|---|---|
| **Barette** | **16** | Mathematical Compendium 14, The Register 2 (entries at L4574, L4614) |
| **Barták** | **6** | main volume L3709 (prose) and L11586 (References); Physics Compendium L907; Mathematical Compendium L552 and L606; The Register L1502 |

**Every one of the six names the same paper** — the main volume's L11586 gives the full citation with
title, journal, volume, year and pages, and it is that paper.

## Which is right, and why the count does not decide it

**Barette is right.** The authors are **Yves Deville, Olivier Barette and Pascal Van Hentenryck**.
dblp carries Olivier Barette under his own author page and keys both the 1999 journal paper and its
1997 IJCAI predecessor `DevilleBH99` / `DevilleBH97`.

**Roman Barták is a real and prominent constraint-programming researcher**, which is exactly why the
substitution is plausible and why it survived: a reader who knows the field reads "Barták" without a
flinch.

**I nearly reported this the other way round.** Three volumes print Barták and one prints Barette, so
by weight of volumes the Mathematical Compendium looked like the outlier — and the Mathematical
Compendium also contradicts itself, printing both. The count says the wrong thing; only the paper
settles it.

## What this does not touch

**The imports of W-292 to W-295 propagated the correct form.** They expanded six `Deville et al.`
sites, and the count of `Barette` in the Mathematical Compendium moved 11 → 14 across BUILD287–290.
I checked this expecting to find I had spread an error, and the opposite is the case.

## The routes, each already established

- **Mathematical Compendium L552, L606 and Physics Compendium L907** — `close_vol.py`, three
  count-asserted substitutions in one build. The route W-282 built.
- **Main volume L3709 and L11586** — a bespoke `r4-*.py` build instrument, as `r4-a1`, `r4-a2` and
  `r4-a3` did for §34.4 and §35. **A main-volume change requires a Register entry in the same build**
  (*no silent change*), so this build carries one.
- **The Register's L1502 is never edited.** Ruling 29 and the store's own mechanic: the repair is a
  **new appended entry citing the superseded one**. The same entry that records the volume changes
  can be that entry, which is why the two halves belong in one build.

An append does not move an earlier Register line, so `r2-ch28a4`'s `401 heading L1500` is unaffected;
the main volume's md5 moves and its line-anchored goldens are re-banked as usual.

RECORDED, NOT REPAIRED.
