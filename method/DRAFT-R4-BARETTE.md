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

---

# THE FULL READING (M: *"read all the associated citations and references first"*)

## Every one of the twenty-two sites cites one paper, and the two full records are identical

| | |
|---|---|
| main volume L11586 | *Deville, Y., **Barták, R.** and Van Hentenryck, P. (1999). Constraint satisfaction over connected row-convex constraints.* **Artificial Intelligence 109**, 243–271 |
| Mathematical Compendium L562 | *Deville, **Barette** & Van Hentenryck, Constraint satisfaction over connected row-convex constraints,* **Artif. Intell. 109 (1999) 243-271** |

Same title, journal, volume, year and pages. **There is no second work**, and the six sites all cite
the same thing the sixteen do: the (α,β)-monotone staircase / connected row-convex class. Read in
full: main L3709 (prose) and L11586 (References); Physics Compendium L907 (the prior-art chain);
Mathematical Compendium L552 (the *Staircase / connected row-convex* object, grade CITED) and L606
(the generation criterion's prior art); The Register 401 at L1502.

## There IS a reason the six survive — and it explains rather than justifies

**Every pass that touched them verified the internal triangle and none checked the author list.**
`recovered/READ-ch13g.md`, the R2 read of main §14.1, records for this citation only that it *"is in
the References and cited for the staircase class; Register 401 (Register L1491) records it."*
W-117 summarised the segment as *"consistent across text, References and Registers 224, 400, 401."*

**The same READ file shows what a real source check looks like in this corpus**, two bullets earlier:
Freuder 1982 was being credited with Dechter 1992's theorem, the source was read, and register 400
records the correction. **The corpus corrected the wrong theorem attributed to the right paper. It
never checked the right theorem's author list.**

## And it is original, not introduced

**BUILD12 already carries both spellings**, with `Barták` at exactly the one object — grade CITED,
*Staircase / connected row-convex* — that still carries it today. Nothing later introduced it and no
pass of mine spread it.

## One internal asymmetry

**The corpus never gives an initial with Barette — 0 of 16 sites.** The only initialled form it holds
is the main volume's *"Barták, R."*, which matches Roman Barták, a real and prominent
constraint-programming researcher. So the corpus's one initialled form is the one the external record
contradicts, and its unintialled form is the one the external record supports.

## THE EVIDENCE IS HELD IN THIS REPOSITORY (M: *"search the repo"*)

I said the primary sources were egress-blocked and my evidence was two search summaries. **That was
premature: the repository already holds the answer**, and it holds it three times over.

`drive/chats/2026-08/764406b9-5552-45a2-9bf6-adb32378bf73.json` — conversation *transitions*,
777 messages, md5 `3cf127ea816e288eab05a8f78f9960bd`, `INDEX.tsv` row 1 — carries **three
independently captured reference lists**, each from a different peer-reviewed publication, each
citing this paper:

| captured source | the line, verbatim |
|---|---|
| Kong, Li, Li & Long, *On tree-preserving constraints*, **Ann. Math. AI (2017)**, via Springer | *Deville, Y., **Barette, O.**, Hentenryck, P.V.: Constraint satisfaction over connected row convex constraints. Artif. Intell. **109(1-2), 243–271 (1999)*** |
| Zhang & Freuder, *Tractable Tree Convex Constraint Networks*, **AAAI-04**, via aaai.org | *Deville, Y.; **Barette, O.**; and Van Hentenryck, P. … (See also Artificial Intelligence …)* |
| *Exploring Directional Path-Consistency for Solving Constraint Networks*, **arXiv 1708.05522** | *Deville, Y., **Barette, O.**, van Hentenryck, P.: Constraint satisfaction over connected row convex constraints. Artificial Intelligence **109(1-2), 243–271 (1999)*** |

Three independent typesettings — *Hentenryck, P.V.* / *Van Hentenryck, P.* / *van Hentenryck, P.* —
agreeing on **Barette, O.** and on volume, issue, year and pages.

**And the other side is empty.** Searched over all 352 conversations: **not one captured source
anywhere in this repository gives Barták for this paper.** Every `Barták` occurrence in the export is
the corpus's own prose. The asymmetry is total: 3 captured sources to 0.

**The evidence was already held when the six sites were written.** The capture is dated 2026-08-02.

## What the reading did NOT find

**A reason for the six to be right.** It found the reason nothing caught them, which is a different
thing. Unlike the channel table's extra rows — where Part II's opening sentence *"Every captured
series, with its fit"* made the pattern correct by construction — nothing here makes two different
second authors for one paper correct.

**What would settle it:** the title page of *Artificial Intelligence* 109 (1999) 243–271, or its
IJCAI-97 predecessor, read directly.

