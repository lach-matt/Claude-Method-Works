# Session handoff, 2026-10-09 (restart to load M's plugins)

M asked for a restart so that the claude.ai plugins load in the session. They are installed on M's account: Research
integrity, Research Desk, Mathbox, math-olympiad, paper-search, Deep Review and Data, possibly also Citation Needed and
verify-ai-output. Everything below is committed. Read this, then `WARPTHEOREM.md` and the last rulings.

## Where B4d stands

- **Rulings run to item 177** (`M-RULINGS-2026-10-03.md`). The ones since phase 2 began:
  - 168: phases follow M's trajectories;
  - 169–171: no travel through time alone; the clocks; space-only teleportation;
  - 172: README stress on position 2's piece, and coinciding as the endless approach down the throat;
  - 173: E-PASS next;
  - 174: three questions left to the math, decided by the board;
  - 175–176: entanglement, carried as the board's H-PAIRING-IS-ENTANGLEMENT;
  - 177: negative null energy from coupling the entangled ends is the appearance of 117/120, which opens escape E-Q.
- **Simulation phase 1:** `lemmas/sim1_transition.py` and `SIM1-TRANSITION.md`, verified.
- **Simulation phase 2:** `lemmas/sim2_facing.py`, selftest 17/17, and `SIM2-FACING.md`, verified and re-verified.
  - Two matter-free pieces of our plane cannot face each other across a static bulk (T5c).
  - With the README on position 2's piece, facing is possible only near the throat on the verified map.
  - **S15:** at exact coincidence, position 2's piece is a sheet of tension −1, so the pair carries zero net stress.
    Positive energy needs an approach depth of at least d₊ = 24m²/ℓ (ℓ > 27.07m).
  - Item 174's decisions are carried in the note but **not yet verified**.
- **E-PASS design** (workflow `epass-design`; the ground stage is saved in `lemmas/epass_ground.json`).
  - **Literature:** Kaus–Reall confirm that a vacuum-brane extremal throat has no smooth bulk cap; its singular end
    agrees with SIM2's y_s^th to four decimals.
  - **Causal, computed in scratch:** without a second sheet, the singular layer lies in the causal past of the
    README's horizon crossing, so the cone premise refutes E-PASS alone. With the near-coinciding sheet the slab
    excises it.
  - **Caution:** Horowitz–Kolanowski–Santos show that tidal forces generically diverge at extremal horizons with
    Λ < 0.
  - **Interrupted by the restart:** proposals, judges and spec. They had been re-run to cover items 174–177 and the
    E-Q angle (Maldacena–Qi coupled AdS₂ ends; Maldacena–Milekhin, where the 4D negative energy is classical in 5D).
  - **Next:** re-run the design (proposals, judges, spec) from this ground. Then build `lemmas/sim2_passage.py`
    and `SIM2-PASSAGE.md`, verify, and report to M.
- **After E-PASS:** phase 2b-i, whether a whole position-2 piece exists (OPEN G; far out, positive energy fails, so the
  piece must close up). Then E-NS, the brief evolution. Then phase 3, between universes.

## Tools and access

- **Skill `mathematica`:** the Wolfram connector (Wolfram 15.0.1), or Mathics3 offline. The connector also loads xAct
  and FeynCalc.
- **Science tools sweep:** `research/warp-drive/toolsweep/toolsweep_result.json`, 371 items.
  - **Its packaging into two skills was interrupted by the restart:** `.claude/skills/science-tools` (`sci install
    <group>`, legitimate routes only) and `.claude/skills/science-databases` (a connector routing table).
  - **To finish it:** re-run from the JSON.
  - **Excluded:** anything obtained through GitHub-content side doors (the Go module proxy, jsDelivr /gh,
    raw.githubusercontent, codeload). The environment's network policy blocks github.com.
- **Connectors added by M:** Wolfram, SciSpace, PDF Viewer and Wiley Scholar Gateway. Elicit needs a paid plan. NASA
  ADS needs a free token from M.

## Housekeeping still owed

- The map (`chainmap.html`) is at version 18. Republish it after E-PASS.
- WARPTHEOREM's B4d row and its history carry phase 2; items 172–177 need a history line when E-PASS lands.
- `CLAUDE.md` still says Lean and Coq cannot be installed. Lean 4 core (conda-forge) and Coq 8.18 (Ubuntu debs) do work;
  Mathlib does not, because it needs GitHub.
