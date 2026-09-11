# FUELFORM.md — is there a material other than salt?

`python3 tools/fuelform.py` · `--selftest` · stdlib only

## The chain being tested

`materials.py` says the blanket's chemistry is **forced rather than chosen**, in three links:

1. **ν = 2.9 is Pu-239 fast**, so there is no thermal spectrum
2. **L = 0.20 must cover fission products for forty years**, so the fuel must be **liquid**
3. **a liquid fast fuel is a salt**, and a fast salt is a **chloride**

`deck.py --provenance` then found the chloride is the one material in the design with **no critical
benchmark behind it**. So the chain is worth testing — and **two of its three links are weaker than
stated.**

## Link 3 first, because it is the one that breaks

**The always-subcritical property is not bought by the salt.** `k_inf` is a *ratio* of macroscopic
cross sections and every one of them scales with number density, **so density cancels**. A dense fuel
and a dilute one at the same fissile fraction and the same absorber per heavy atom have the same
`k_inf`. What sets the threshold is the fissile fraction and what the carrier absorbs — nothing else.
(The selftest asserts this *structurally*: `k_infinity` takes no density argument, because a ratio
cannot depend on one.)

| fuel form | k_inf = 1 at |
|---|---:|
| MOX oxide, bare fuel | **7.21 %** |
| U-Pu-Zr metal, the IFR fuel | 7.39 % |
| molten plutonium metal, Pu-Fe eutectic | 7.52 % |
| NaCl-UCl₃ at the eutectic, 34 mol % | 7.93 % |
| MOX in lead-bismuth, 50 vol % coolant | 8.08 % |
| mononitride fuel | 8.16 % |
| **NaCl-UCl₃, the design's 18.9 mol %** | **8.35 %** ← the design |
| LiF-ThF₄-UF₄ fluoride salt | 9.71 % |

**The whole band is 7.21 to 9.71 percent — a spread of 1.35.** Every fast fuel form has an
always-subcritical threshold and they are all in the same place. **The salt is not special**, and the
design's own salt is the **second worst** of them: it needs **1.16×** more fissile than bare oxide for
the same property.

## Link 2, which is weaker than it looks

*"The fuel must be liquid"* is really *"fission products must come out"*, and a liquid is one way to do
that — not the only demonstrated one.

| form | fission-product removal |
|---|---|
| NaCl-UCl₃ (both) | online, continuous |
| LiF fluoride salt | online, continuous |
| MOX oxide | batch, aqueous or pyro |
| MOX in LBE | batch |
| **U-Pu-Zr metal, IFR** | **batch pyroprocessing, DEMONSTRATED** |
| mononitride | batch |
| molten Pu metal | liquid, but never demonstrated |

**EBR-II closed its own fuel cycle on site for thirty years** with solid metal fuel and batch
pyroprocessing. Batch is not online and the difference is real — an online loop holds a lower
equilibrium fission-product inventory — but *"the fuel must be liquid"* overstates it, **and this work
has never priced the difference.**

## Link 1 stands

Nothing here challenges the fast spectrum: ν = 2.9 is Pu-239 fast, `materials.py` derives it, and every
form in the table is a fast form.

## And the column that decides it

| form | operating history | criticality benchmarks |
|---|---|---|
| **NaCl-UCl₃ (the design)** | **NONE** — no fast chloride salt has ever gone critical | **NONE** — MCRE is being built to make the first |
| NaCl-UCl₃ eutectic | NONE | NONE — this is MCRE's own salt |
| LiF fluoride salt | MSRE, thermal, 1965–69 | MSFR two-code benchmark |
| MOX oxide | Phénix, Superphénix, BN-600, BN-800, Joyo, FFTF — decades | abundant |
| **MOX in lead-bismuth** | **the ADS field's own choice: MYRRHA and CiADS** | abundant, plus LBE-specific work |
| U-Pu-Zr metal | EBR-II, thirty years, fuel cycle closed on site | abundant |
| mononitride | test irradiations only | some |
| molten Pu metal | LAMPRE, Los Alamos, critical 1961, several thousand hours | little |

**The design's own material is the only row with NONE in both columns** — and the two
accelerator-driven systems actually being built, **MYRRHA and CiADS**, chose MOX in lead-bismuth, which
has decades of operating fast reactors behind it *and* a lower threshold.

## So what does the salt uniquely buy?

**One thing: online fission-product removal.** That is link 2, and it is real.

**What it uniquely costs is provenance** — no benchmark, no operating history, and a chlorine
evaluation known to disagree with measurement outside its own covariance.

**And `deck.py --provenance` says the salt may not deliver the safety property at its operating
fraction anyway.** If that flag holds, the design is paying its entire provenance budget for a property
it does not get — and the same property is available at a *lower* fissile fraction in a material with
sixty years of operating history.

## What this file does not do

**It does not take the decision.** It is a change of material, it costs the online removal loop, and
what that loop is worth in equilibrium fission-product inventory has never been computed here. What it
does is **remove the word "forced" from a choice that was never forced**, and put the trade where the
author can see both sides of it.

## `--removal`: what online fission-product removal is worth

The main report left link 2 open — *"the fuel must be liquid"* overstates *"fission
products must come out"*, and the difference had never been priced. `--removal` prices
it, and finds a **comparison error** before it finds a number.

`materials.py`'s link 2 compares online removal against **never removing anything**.
Nobody proposes never. Every solid fast fuel that has ever operated removed fission
products in **batches**, and the comparison that decides link 2 is online against batch.

Fission products only absorb, so a holding of `n` per heavy-metal atom costs a relative
fall in `k` of `n·σ_FP / (absorption per heavy atom)`. The lumped one-group fast capture
cross section is **0.20 barn** (SOURCED; the important individual fission products agree
to better than **10 % RMS** across evaluated datasets, and that is the only uncertainty
claimed for the lump).

| removal regime | n_FP/HM | dk/k | beam |
|---|---|---|---|
| online, 30 day residence | 0.00104 | 0.039 % | +0.7 % |
| online, 90 day residence | 0.00311 | 0.117 % | +2.0 % |
| batch, 2 year cycle, average | 0.01264 | 0.477 % | +7.9 % |
| batch, 3 year cycle, average | 0.01896 | 0.715 % | +11.9 % |
| batch, 5 year cycle, average | 0.03160 | 1.192 % | +19.9 % |
| batch, 5 year cycle, end of cycle | 0.06319 | 2.383 % | +39.7 % |
| never removed, 40 years | 0.50554 | 19.065 % | +317.7 % |

**Against never, the chain is right** — 19.1 % of k against an `L = 0.20` allowance, so a
fuel that cannot remove fission products at all is excluded and that much of link 2
stands. **Against batch it does not**: a three-year cycle costs **0.715 %**, which is
**3.6 %** of the allowance it was said to eat and **27×** smaller than the case the chain
compared against. On the leakage budget — the argument link 2 actually makes — **batch
removal passes**, so link 2 forces *removal*, not a liquid.

The difference is still real, and it stops being small through the k cliff:
`explore.py`'s elasticity of **−16.7** turns a three-year batch cycle into **+11.9 %
beam** against the design's own online loop, and a five-year end-of-cycle into **+39.7 %**.
**The liquid is worth about a tenth of the beam**, and that is the price of the provenance
the salt does not have.

Two things run the other way and both are recorded.

**The sign is safe.** Fission products only absorb, so a batch plant's k *falls* through
its cycle. In a subcritical source-driven assembly that is a power droop the beam follows,
not a reactivity excursion — the composition moves *away* from critical as it burns.
Batch costs money, not margin.

**And the obvious fix for the droop is bounded by the safety property** — the finding this
section exists for. A batch plant offsets the swing by loading extra fissile at beginning
of cycle, which walks the loading composition toward the always-subcritical threshold:
7.928 % operating, 8.046 % / 8.126 % / 8.327 % to offset the three cases above, against
the design salt's own threshold of **8.346 %**. **The longest batch cycle that can be
compensated at loading without crossing it is 5.23 years.** The batch cycle is not bounded
by chemistry or by the leakage budget — **it is bounded by the always-subcritical
property**, and nothing here had stated that coupling.

**Not counted, and each would move it:** fissile burnup and breeding are excluded (the
design holds its fissile fraction by breeding at `f_b`, so this is the *residual* swing),
the lump is a lump, and out-of-pile inventory, decay heat and a batch handling campaign
are not priced at all. **The decision is still not taken here.** What changed is that link
2 now has a number instead of a word.

    python3 tools/fuelform.py --removal
