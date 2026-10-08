# B4d stage 1: what bulk can stand through the write (computed, READ and deduced; verified once; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `b4d_stage1.py`, selftest 7/7.

The first draft aimed its main test at a reading of the write that item 159's test had already withdrawn. It also never
said that a closing plane leaves no room for B4c's far surface, and it left out escapes that are still open. All of
this is corrected below (History).

## What you said

- **2026-10-08:** *"Continue B4d as well please"*.
- **Item 157:** *"we already have at least half the model, our current universe."*
- **Items 117/120:** H-NEC-COIN; *"the NEC only ever appears to break, but never does"*.
- **Item 127 (1):** *"yes"*: the planes coincide.
- **Item 138:** the bulk is multi-universal.
- **Item 139:** position 2's plane has negative tension.
- **Item 141:** the planes are static.
- **Item 159:** *"test both options"*.

## The question, reading by reading

- **Readings (ii) and (i′), the live ones.** The corridor stands only after the README has arrived. So the question for
  the bulk is the opening: it lasts at least 2.0×10⁵ clocks, and can it end in eq. (17)?
- **Reading (i), as first tested and since withdrawn** (H-WRITE-IN-STATIC-HOLD, inconsistent with your 115 (c)). Only
  here would eq. (17)'s static bulk itself have to stand through the write. D3 tests that reading.

## D1. The regime (computed)

- **How far the write reaches.** By O3-WRITE W3, the README starts spread over a ball of radius (2 + T)m. Here m =
  GE/c⁴ is the corridor's mass length; one clock is about 6.6×10⁻³⁷ s at the example README. Light moves at most at 1,
  so the region the write disturbs reaches about T·m.
- **What B4c needs.** B4c's far model needs ℓ > 2·R_reach = **4.0×10⁵ m**, in those mass lengths.
- **What that means.** It is the flat limit, where gravity at the corridor's scale is five-dimensional.

## D2. What stands with one plane

This is an enumeration of the board's own candidates, not a classification of every possible bulk.

| bulk | through the write | the corridor? |
|---|---|---|
| the black string (the Vaidya opening's bulk, by construction) | unstable (`o3_readings.py`, under H-QUASI-STATIC-STRING, H-MASS-RISES, H-README-ALONE or H-SEED); Lehner–Pretorius's extrapolated end is a naked singularity | — |
| eq. (17)'s static bulk | its singular surface by ~18 clocks (`b4_static.py`) | — |
| the localized hole (5D Schwarzschild cut by the plane, by choice) | linearly stable against all tensorial types (Ishibashi–Kodama, READ); Figueras–Wiseman's small holes "should be stable" (READ p.4), though their computed range, R₄/ℓ from 0.07 to 20, lies above ours (~10⁻³) | **no** |

Why the localized hole is not the corridor:
- **No 1/r tail.** Its slice through the plane has lim r·(f − 1) = 0 (computed; 4D Schwarzschild's −2m is the control).
  So it has no Newtonian 1/r tail at r ≪ ℓ.
- **Not extremal.** Its surface gravity is 1/r_h, not 0, so O2 fails.
- **No throat.** Its areal radius is r (STRUCTURAL).
- **Far too large.** A 5D hole carrying the README's energy has r_h² = (8/3π)·m·ℓ (deduced, standard Randall–Sundrum,
  not READ). That is **about 580 m at ℓ = 4×10⁵ m**, against the corridor's r₀ = 2 m. So G3 and H1 fail too.
- **No extremal version on offer.**
  - A Z2-symmetric extremal vacuum hole is not available: a single spin has no regular extremal limit, and a second
    spin breaks Z2 (standard, not READ).
  - Extremal charged Randall–Sundrum holes need matter on the plane, which clause (B) forbids.

## D3. Reading (i) only: a plane closing eq. (17)'s static bulk

**The proposal.** One of your item-138 planes at height y_w, mirrored (Z2), below the singular surface.

**What it must carry.**
- Through the Israel junction condition, the stress S_μν the plane carries *is* its stress-energy: localized, real
  matter. That differs from eq. (17)'s own apparent deficit, which sits on a plane carrying no matter. That deficit is
  the kind your 117/120 read as only an appearance.
- In units of 2/κ²: ρ + p_r = −A_y/(2A) + B_y/(2B).

**STRUCTURAL at small heights.**
- A tensionless mirrored plane has dh/dy = 0, so d²h/dy² = 2R⁽⁴⁾. That gives

  **ρ + p_r = y_w · R⁽⁴⁾_kk(radial) + O(y_w³),  with R⁽⁴⁾_kk = −2(r − 2)/(r²(2r − 3)²) < 0 for every r > 2.**

- R⁽⁴⁾_kk is eq. (17)'s own radial null combination (opening.py O3). It matches the computed slope exactly at every
  radius from 2.01 to 32.
- So the closing plane would have to carry, as real matter, the deficit the theorem's (Z) clause reads as the bulk's
  pull.

**Numerically, to the singular surface** (exact series, Padé at two orders):
- negative at every r from 2.1m to 32m and every y_w up to 2.3m;
- positive near the throat (r ≤ 2.05m) for y_w ≳ 2. That is the control showing the sign is not forced by the method;
- one negative point per plane is enough, and every constant-height plane has one.

**Adding tension does not help.** A tension adds +σ to ρ and −σ to p, so ρ + p is unchanged. That includes the
negative-tension plane of your 139.

**It is excluded anyway.** Any closing plane within about 2.5 m leaves no room for B4c's far surface.

## D4. A slab for the string (deduced)

- **What it costs and does.** A closing plane on the flat-limit string carries nothing. It stops the *final* string
  when y_w < π·r₊/μ_c = 3.59 r₊. That is deduced from Gregory's eq. (11), the mirrored form of Gregory–Laflamme's
  compactification (GL abstract p.1, READ).
- **Why it still doesn't save the string.** `o3_readings.py`'s escape (b) stays closed under H-QUASI-STATIC-STRING:
  starting from zero mass, every allowed mode crosses the unstable band (2.2×10⁴ e-folds).
- **What would reopen it.** Only an early opening that is not a string. That is the board's H-SLAB-PHASES: a localized
  hole until it spans the slab. It denies H-QUASI-STATIC-STRING early on, and it is carried as open, not shown.
- **Excluded by the far model too.** A slab is excluded by H-FAR-MODEL as written, and no far model for a slab has been
  built.
- **Its end is still not the corridor.** It ends as a uniform string: Schwarzschild on the plane, not eq. (17).

## Verdict

- **(ii) and (i′):** on the board's models, no regular bulk through the opening ends in eq. (17). The candidates are an
  enumeration built from the board's own choices.
- **(i):** a constant-height mirrored plane closing the static bulk must break the null energy condition with real
  matter. This is structural at small heights and numerical up to the singular surface, and the plane is excluded by
  H-FAR-MODEL anyway.
- **Not decided:**
  - H-TWO-SIDED, a plane with bulk on both sides;
  - a curved closing wall y_w(r), whose bending terms may outweigh the small R⁽⁴⁾_kk at large r;
  - finite ℓ (B6′, nature's), excluded by H-FAR-MODEL unless B4c's reading changes;
  - H-SLAB-PHASES;
  - `o3_readings.py`'s open escapes: (a) an extremal opening, (d) the opening's bulk is not the string, (e) a late
    shell, (f) the short write with small seeds, and (i′).

## Named hypotheses

- **Yours:** 117/120, 127, 138, 139, 141, 157, 159.
- **The board's:**
  - H-FAR-MODEL;
  - the flat limit;
  - R-VAIDYA-HOLDS;
  - H-QUASI-STATIC-STRING;
  - H-MASS-RISES;
  - H-README-ALONE or H-SEED;
  - H-WRITE-IN-STATIC-HOLD (D3's reading);
  - H-SLAB-PHASES;
  - B4b's locally analytic class;
  - the hypotheses of `o3_write.py`.

## History (verifier, 2026-10-08)

**What the verifier confirmed.** It ran the selftest (6/6) and checked each step independently:
- built the 5D Ricci tensor and confirmed the series is vacuum through y⁹;
- calibrated the Israel sign convention a second way (gluing flat balls);
- re-derived ρ + p_r and spot-checked r = 3, y_w = 1 to 10⁻²⁶;
- READ every quote.

**Its findings, all applied:**

**MUST-FIX**
1. **The draft never said which reading D3 tests.** D3 is now labelled reading (i), and the verdict is given reading by
   reading.
2. **D3/D4 clash with D1.** A closing plane leaves no room for B4c's far surface; that is now stated. `o3_readings.py`'s
   closed escape (b) is now cited, and H-SLAB-PHASES is named as what would reopen it.
3. **Open escapes were missing.** They are added, and the candidate list is now called an enumeration.

**SHOULD-FIX**
4. **"Negative everywhere" over-claimed.** It is now negative at r ≥ 2.1 to 32m, with the positive near-throat region
   as the control. One negative point per plane is enough.
5. **The small-height identity** is now a STRUCTURAL check: ρ + p_r = y_w·R⁽⁴⁾_kk.
6. **Why the plane's violation is real** — Israel stress is matter, not an appearance — is now stated.
7. **A curved wall** is now named as an open escape.
8. **Tension doesn't help** (ρ + p unchanged); 139 is added.
9. **Two D2 checks could not fail.** The 1/r check now computes lim r·(f − 1), with a 4D control. The no-throat claim
   is now STRUCTURAL, and "no 1/r tail" is qualified to r ≪ ℓ.
10. **READ scopes corrected.** FW's small-hole sentence is now p.4 "should be stable", with the note that their range
    lies above ours. Ishibashi–Kodama is "linearly stable against all tensorial types". Lehner–Pretorius is marked an
    extrapolation, and the hypotheses are added.

**NOTE**
11. **Gregory–Laflamme's compactification phrase** is in the abstract on p.1, not pp.8–9. The mirrored-slab form is
    deduced from Gregory's eq. (11).
12. **D1's reach** now comes from the README's starting ball (W3), with m as the corridor's mass length.
13. **The localized hole's r_h ≈ 580 m**, and the absence of extremal versions, are added (deduced, not READ).
14. **Order 40 is now noted as adequate** under the banked tops. The uniform string's slice is exactly Schwarzschild.
    The equatorial slice is correct in the flat limit.
