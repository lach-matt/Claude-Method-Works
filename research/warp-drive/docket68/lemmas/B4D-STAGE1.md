# B4d stage 1: what bulk can stand through the write (computed, READ and deduced; not verified; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `b4d_stage1.py`, selftest 6/6.

## What you said

- **2026-10-08:** *"Continue B4d as well please"*.
- **Item 157:** *"we already have at least half the model, our current universe."*
- **Items 117/120:** null energy at every point (Z3).
- **Item 127 (1):** *"yes"*: the planes coincide.
- **Item 138:** the bulk is multi-universal.
- **Item 141:** the planes are static.

## The question

- **What the write demands.** It lasts at least 2.0×10⁵ clocks at the example README (O3-WRITE.md).
- **What stage 1 asks.** Which bulks can stand regular for that long, and is any of them the corridor?

## D1. The regime (computed)

- **What B4c needs.** B4c's far model (H-FAR-MODEL) needs ℓ > 2·R_reach.
- **The reach is now the write's.** So ℓ > 4.0×10⁵ m, which is ℓ/r₀ > 2×10⁵.
- **What that means.** The corridor sits deep in the flat limit, where gravity at its own scale is five-dimensional.

## D2. With one plane: what can stand

There are three candidates the board can name.

| bulk | through the write | the corridor? |
|---|---|---|
| the black string (the Vaidya opening's bulk) | unstable (Gregory–Laflamme, `o3_readings.py`); ends in a naked singularity (Lehner–Pretorius, READ) | — |
| eq. (17)'s static bulk | reaches its singular surface by ~18 clocks (`b4_static.py`) | — |
| the localized black hole: the 5D Schwarzschild hole cut by the plane | **stands**: stable against every perturbation type (Ishibashi–Kodama, READ); the small-hole limit of Figueras–Wiseman's static braneworld black holes (READ) | **no** |

The localized hole's slice through the plane, computed:
- g_tt = −(1 − r_h²/r²). There is no 1/r term, so it carries no Newtonian 1/r tail.
- Its surface gravity is 1/r_h, not 0. So O2 (an extremal horizon) fails on it.
- Its areal radius is monotonic outside the horizon. So it has a horizon but no throat.

## D3. A closing plane below the singular surface (computed)

**The proposal.** One of your item-138 planes at height y_w would close the bulk there, mirrored (Z2). That would cut eq. (17)'s static bulk off below its singular surface and switch the string's instability off.

**What it must carry.** The Israel junction condition fixes the plane's matter from the static bulk's own extrinsic curvature at y_w. That curvature comes from `b4_static.py`'s exact series, continued by Padé at two orders. The figure below is in units of 2/κ²:

| r \ y_w | 0.25 | 0.5 | 1.0 | 1.5 | 2.0 | 2.3 |
|---|---|---|---|---|---|---|
| 2.1 | −0.008 | −0.016 | −0.032 | −0.053 | −0.097 | −0.186 |
| 2.15 | −0.010 | −0.020 | −0.042 | −0.078 | −0.191 | −0.562 |
| 2.25 | −0.011 | −0.023 | −0.051 | −0.100 | −0.241 | −0.506 |
| 2.5 | −0.010 | −0.021 | −0.046 | −0.083 | −0.150 | −0.212 |
| 3 | −0.006 | −0.013 | −0.027 | −0.044 | −0.066 | −0.081 |
| 4 | −0.003 | −0.005 | −0.010 | −0.016 | −0.022 | −0.026 |
| 6 | −0.001 | −0.001 | −0.003 | −0.004 | −0.006 | −0.007 |

**ρ + p_r is negative everywhere.** The two Padé orders differ by at most 3.4×10⁻⁵, a twentieth of the smallest value. The closing plane would need matter that breaks the null energy condition, which your 117/120 forbid at every point.

**Controls:**
- The RS1 second brane comes out at negative tension with ρ + p = 0 exactly.
- On the flat-limit black string a closing plane carries nothing.
- On the same plane at r = 2.1m, ρ + p_θ is positive. So the sign of ρ + p_r is the bulk's, not forced by the method.

## D4. The slab for the string (computed and deduced)

- **What it costs.** The same plane on the opening's black string costs nothing (D3's control).
- **What it does.** It switches the instability off when y_w < π·r₊/μ_c = 3.59 r₊ (GL pp.8–9 READ; μ_c from `o3_readings.py`).
- **Early in the opening.** r₊ is small, so the hole is a localized 5D hole in the slab, which is stable. It becomes a string once it spans the slab. That sequence of phases is the board's reading (H-SLAB-PHASES, not READ).
- **The end state.** The opening ends as a black string: Schwarzschild on the plane at r ≫ y_w. That is regular, but non-extremal, and not eq. (17).

## Verdict

- **Nothing standing is the corridor.** Through the write, every bulk the board can show standing regular is a black hole or a black string. None is eq. (17)'s extremal corridor.
- **The corridor's own bulk can't be rescued by a closing plane.** Its static bulk can be closed below the singular surface only by a plane that breaks the null energy condition, which your rulings forbid.
- **Not decided here:**
  - a plane with bulk on both sides (H-TWO-SIDED);
  - finite ℓ (B6′, nature's), which B4c's far model now excludes unless that reading changes;
  - whether the write's own hypotheses (O3-WRITE.md) hold.

## Named hypotheses

- **Yours:** 117/120, 127, 138, 141, 157, 159.
- **The board's:**
  - H-FAR-MODEL (B4c);
  - the flat limit;
  - R-VAIDYA-HOLDS;
  - H-SLAB-PHASES;
  - B4b's locally analytic class (for the static bulk and its series);
  - the hypotheses of `o3_write.py`.
