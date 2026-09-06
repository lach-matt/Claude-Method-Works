# FINDING R4-11 — the t contradiction was mine, not the book's. Two findings withdrawn, twelve values rebuilt, and the f test run for the first time.

M: *"lets address it."* Addressed. `method/proofs/entrypoint.py` holds the work; its selftest asserts
registers 1334 and 1337 value for value, nineteen checks, all passing.

## 1. There is no contradiction. I built one by not reading register 1334.

I reported that §34.7 and §34.9 define *t* incompatibly: §34.9 gives **t = (a−L)/(U−L)**, a fraction
of the corridor that cannot exceed 1, while §34.7 measures **1.028 at p and 1.785 at d**.

**Register 1334 states the input, and it is not the walk's carried `a`:**

> *"**ν = c√(R/IE) gives a = (n−ν)/√p from ONE OBSERVATION with no comparison. 18 of 51 fall INSIDE
> their corridor, 33 OUTSIDE, and a_meas is systematically TOO LARGE.**"*

**`a_meas` is measured from the ionisation energy, it usually lies above the corridor, and t > 1 is
exactly what that means.** The record had the definition, the count, and the reason — *"ν depends on
OCCUPANCY and the law has no coordinate for it"*. **T-01 is withdrawn.** It was the fourth time in
this pass that I measured before searching, and the rule earns another restatement: the record
first, the instrument second.

## 2. And 34re-04 does not survive either, in either half

The record's own finding reads: *"1.028 at p … is a median, and its convention is unnamed … **1.028
at p is no mean or median of any printed row — UNREPRODUCIBLE, budget the Löwdin delivery**"*, and
*"**1.785 / 1.028 is 0.25 % from √3, not 0.19 %**"*.

**Rebuilt from the ionisation energies, every printed value returns exactly:**

| | |
|---|---|
| **register 1334**, the 3p filling | Al 1.49 · Si 1.71 · P 1.86 · S 1.85 · Cl 1.98 · Ar 2.07 — **six of six** |
| **register 1337**, t at the opening | 3p 1.0925 · 4p 1.0331 · 5p 1.0124 · 6p 1.0237 · 4d 1.8453 · 5d 1.7240 — **six of six** |

**So 1.028 IS a median** — of register 1337's four p values, which are themselves reproduced. Not
unreproducible; reproduced.

**And the 0.25 % is a rounding artefact.** From the printed 1.785 and 1.028 the ratio is 1.736381,
which is 0.25 % from √3. **From the unrounded values it is 1.735267, which is 0.19 %** — the book's
own figure. That is precisely the class `method/proofs/precision.py` exists for, and it is the second
recorded finding to fall to it after D-61.

## 3. The f test, which register 1337 calls "predicted and unmeasured", now runs

Register 1337 closes: *"**no f test — no f subshell has a two-sided corridor, so √6 = 2.4495 is
predicted and unmeasured.**"*

**M's ruling of 6 September admits g to the candidate set, and 5g is what gives the 5f opening a
floor.** So the 5f corridor is two-sided, and the test that could not be run can be run.

**Protactinium, 5f opening.** IE = 5.89 eV, ν = 1.519857, p = 1, **a_meas = 3.480143**, corridor
(0, 1.3660254), and

> **t(5f) = 2.5476, against t(f) = √6 = 2.4495 — high by 4.01 %.**

| ℓ | measured | t(ℓ) = √(ℓ(ℓ+1)/2) | high by |
|---|---|---|---|
| p | 1.0284 | 1.0000 | **+2.84 %** |
| d | 1.7846 | 1.7321 | **+3.04 %** |
| **f** | **2.5476** | **2.4495** | **+4.01 %** |

**And that answers a question register 1337 could not answer.** It records: *"Not derived: a common
factor of 1.029, both p and d 2.9 % high, **which two ℓ values cannot adjudicate**."* **There are
three now, and the factor is not common — it drifts with ℓ.**

## 4. The result survives the estimate, which is the reason it is worth having

**Protactinium's first ionisation energy is an estimate, not a measurement**, so the test is reported
across its plausible range and never as one number:

| IE (eV) | t | vs √6 |
|---|---|---|
| 5.69 | 2.5283 | +3.22 % |
| 5.89 | 2.5476 | +4.01 % |
| 6.19 | 2.5749 | +5.12 % |

**Across the whole range f is high by 3.2 % to 5.1 %, above the p and d factor at every point.** For
t to reach √6 exactly the ionisation energy would have to be **4.97 eV**, far below any estimate.
**So the drift is not an artefact of the estimate.**

**And one thing is deliberately not done.** Three points do not make a law, and the third rests on an
estimated input. **No form is fitted to the drift here**, and none should be until a second f opening
or a better protactinium value exists. Register 1337's *"not derived"* stands; what has changed is
that it is now not-derived over three ℓ values instead of two.

## What is owed, and it is M's

1. **Register 1337's closing clause is superseded**: *"no f test"* was true when written and is not
   true under the ruling. A new entry citing it is the Register's own form.
2. **34re-04 is withdrawn** and its docket entry should carry the withdrawal, with the precision
   reasoning as the ground.
3. **§34.7's sentence** — *"Where `a` sits in its corridor is fixed by the single-state observation"* —
   is loose in the way that produced my false finding. **`a_meas` sits outside its corridor at 33 of
   51 measurements**, by register 1334's own count. The prose says *in its corridor*; the measurement
   says usually above it. That is a prose repair and it is the one that would have stopped me.

**Nothing is repaired here.**
