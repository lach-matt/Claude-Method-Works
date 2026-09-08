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
