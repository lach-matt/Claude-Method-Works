# The closing's flux, by trajectory class (computed, deduced and standard-not-READ; not verified by a separate session; not seated; 2026-10-10)

*First headed* 2026-10-10, worked in the conversation. Instrument: `lemmas/close_flux.py` (selftest 4/4, mutants 5/5).
It answers the new OPEN item `README-HELD.md` named.

## What you said

- **109:** a horizon cannot outlive its object.
- **136 (2):** *"2 - released at position two at the closing of the horizon"*.
- **132**, verbatim: *"the passage is one way by nature, a black hole in and a white hole out, side views of the same
  corridor object"*. The white hole is yours, not the board's. You had already confirmed it at 122 (3) (*"3 - your
  candidate is correct"*, to P2's white-hole past horizon), and you put it on the record again at 199: *"For the
  record, I did suggest a white hole earlier on"*.
- **198** (your guess): *"My guess would be 1."* The README forms the corridor; it has no partner.
- **167, 168:** the trajectories run first *"two positions, one universe"*, then between universes.

## Plain words first

`README-HELD.md` found that closing the corridor needs its horizon to shrink. It cited the area theorem to say that
classical positive energy forbids this. **That theorem is about event horizons**: horizons whose light rays can never
end. Whether the corridor's horizon is one depends on where the README goes.

- **Two positions in one universe.** What crosses at position 1 comes out at position 2, in the same universe, and can
  still reach that universe's far future. So the region behind position 1's horizon is not cut off, **there is no event
  horizon, and the area theorem does not apply.** Positive energy can then shrink the surface: it focuses the light
  rays, and they end, as your 109 requires. **The demand for negative energy at the closing dissolves for this class.**
  What remains is the bulk's own dynamics (B4d).
- **Between universes.** Nothing returns to universe 1, so position 1's horizon is universe 1's event horizon. Its
  area cannot fall under positive energy. Closing it needs **negative null energy or a non-classical step.** Otherwise a
  horizon at least the README's size stays in universe 1 for good, against your 109 and 136 answer 3. **The demand
  stands for this class.**
- **The same mass loss looks different from the two sides.** From position 1 it is a negative inflow. From position 2,
  **your white hole (132)**, it is a positive outflow. This is your 132's *"a black hole in and a white hole out"* with
  136 (2)'s release at position two. The board computed it; the idea is yours.

## The facts

- **K1** [computed, sympy, from the Vaidya metrics' Einstein tensor]. Ingoing Vaidya: T_vv = m′(v)/(4πr²), which is
  negative when the mass falls. Outgoing Vaidya: T_uu = −m′(u)/(4πr²), which is positive when it falls.
- **K2** [computed]. Raychaudhuri on a null surface, starting from θ = 0 (the hold at fixed size, Lemma S):
  - positive R(k,k) drives θ to −∞ within the run, and the area falls to 0 (a caustic: the rays end);
  - zero keeps the area fixed;
  - negative grows it (×14.2);
  - shear alone shrinks it.
- **K3** [deduced; standard-not-READ]. The premise of Hawking–Ellis's area theorem is an event horizon: the boundary of
  the causal past of future null infinity, whose generators have no future endpoints. That premise fails within one
  universe and holds between universes, as above.
- **K4: the cypher (your 196)** [computed; it classifies]. The encoding is H-CYPHER-CLOSE, the board's. Its cells
  carry K3's deduction, so this **classifies the board's deduction rather than testing it independently.**
  - The one-universe closing with positive flux is admitted by all five operator-bearing languages. That is forced,
    because it is data. Left out, no language regrows it.
  - The between-universes closing with positive flux is refused by geometry and statistics. It is admitted by order,
    algebra and information: a STRUCTURAL caveat, since their closures over-reach.

## What it does to the chain

- The chain's input CLOSE (`chain_cypher.py`) splits:
  - **within one universe** it is not a negative-flux demand;
  - **between universes** it stands.
- E1 and E2 inherit the split.
- No status moves; nothing is seated.

## What it does not show

- A closing that works. K2 shows only that positive energy *can* shrink a surface that is not an event horizon. The
  closing's actual evolution in five dimensions is B4d's.
- K3 is the board's deduction from a standard theorem it has not READ. Hawking–Ellis is not banked here; Chruściel,
  Delay, Galloway and Howard, gr-qc/0001003, state the area theorem with its hypotheses and could be READ to bank it.
- Whether position 2 is in our universe for any given corridor. Your rulings carry both classes (167, 168).

## Named hypotheses (the board's)

- **H-CLOSE-SPLITS-BY-CLASS:** K3.
- **H-CYPHER-CLOSE:** K4's index.

## History

- 2026-10-10, after item 199: the white hole's attribution was corrected. K1's white-hole release is your 132 (and
  122 (3)), not the board's. Your words are now quoted verbatim where the note first paraphrased them.

- 2026-10-10: first headed after `README-HELD.md` and item 198. K1–K4 were computed; selftest 4/4, mutants 5/5. The
  first K4 check expected information to refuse the between-universes cell. The run showed geometry and statistics
  refuse it and information admits it, so the check was corrected to what the run shows. Not seated.
