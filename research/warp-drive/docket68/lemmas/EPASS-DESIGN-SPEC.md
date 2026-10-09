<!-- E-PASS design spec (workflow epass-design, run wf_718c7606-e5a, finished 2026-10-09). A design document: not verified, not seated. Scratch paths inside refer to the old session's container. -->
# Build specification: E-PASS stage 2, `lemmas/sim2_passage.py` (X11–X25) and `lemmas/SIM2-PASSAGE.md`

**Status.** This is a design document. It synthesises the ground stage, four designs and two judgments, plus three checks of my own. Nothing is written into docket68, drive/, extracted/, recovered/ or method/. Every number below marked "spec check" was computed in scratch at `/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/epass/spec/`. Those numbers are not board evidence, not verified and not seated.

---

## 0. Read first: three things changed after the designs were written

### 0.1 The file already exists

- `lemmas/sim2_passage.py` was written at 15:58 on 2026-10-09 (34,332 bytes). It holds X1–X10, the ground stage, built independently by the new session.
- Item 178 already cites it: "sim2_passage X10 (e)".
- **The build therefore appends X11–X25.** It must not renumber or remove X1–X10. It keeps the current CLI (`--selftest`, `--json PATH`) and keeps checks C1–C14 passing.
- `SIM2-PASSAGE.md` does not exist yet.

### 0.2 Items 179–181 were recorded after the designs (read verbatim)

- **179.** "Let's approach this from a different angle. We know the corridor doesn't not sit on either position's plane, it only bridges them. So one could surmise that the corridor is exclusive to the bulk."
- **180.** M's correction: "*does not sit on either position's plane".
- **181.** "this bears directly on B4d, and requires priority"

The rulings file carries H-CORRIDOR-IN-BULK as M's reading, and records the board's own reading of what it touches: "B4d stages 5-7, simulation phases 1-2 and sim2_passage.py took eq. (17) as a plane's own metric, so they describe the board's configuration, not M's, and are re-read". Under 181 the board's recorded next step is the two-plane balance.

**What this means for this build.** Every section below is tagged:
- **[FREE]**: holds whatever carries the corridor, whether our plane, a sheet, or the bulk alone.
- **[PLANE]**: uses eq. (17) as our plane's own metric. This is the board's pre-179 configuration.

The decisive new results are [FREE]: Lemma S, in both its sheet form and its pure-5D form, the pair demand, Lemma K, the generator classes and Lemma P.

Sequencing under 181 is the board's call. **Recommended:** build the [FREE] core first, since it says where the README's energy cannot go and the balance work will need that. Build the [PLANE] sections only after the 179 re-read decides whether the plane configuration stays as the board's comparison case.

### 0.3 The judged graft is changed at one point

Both judges grafted design 4's Lemma A (Gauss, Israel, null transport and Raychaudhuri, integrated along the horizon). **Its geometric premise fails exactly where the README crosses.** This is a refutation of a premise, reported as one.

- Lemma A assumes premise (i): the bulk horizon meets the sheet at right angles, with geodesic generators.
- But the README's own flux enters Israel: K(k,k) = −S(k,k)/ν ≠ 0 on the sheet wherever it crosses.
- In Gaussian normal coordinates, a bulk null geodesic tangent to the sheet along k obeys y″ = K(k,k) = −S(k,k)/ν (spec check `lemmaS.py`).
- So a bulk horizon that is C² up to the sheet, with the brane horizon as its trace, carries no net flux on that trace (deduced). This is Lemma K, X14.

What survives and what changes:
- **Survives.** Lemma A's algebra was right. Its Gauss and transport identities are kept as checks C15 and C16.
- **Replaced (static case).** The stationary case is decided by a simpler exact statement, Lemma S (X13), which does not depend on the sheet's tension.
- **Withdrawn.** Design 4's O-C, "a sheet with q_Σ ≥ 0 absorbs classically" (between universes), and its B_start budget.
- **Kept.** The changing case uses the pointwise brane ledger, Lemma L, READ in SMS. The judges' one-line inequality survives as Lemma Q.

---

## 1. Names and files

### 1.1 Files

| file | role |
|---|---|
| `lemmas/sim2_passage.py` | Extended with X11–X25. The docstring gets an X11–X25 block. |
| `lemmas/SIM2-PASSAGE.md` | New note (outline in §11). |
| `lemmas/sim2_passage_bank.json` | New. Holds the owner columns (X11), the nine caps (X22) and the λ-scans. Rebuilt with `--regenerate [--procs 3]`. `compute()` reads it when present; when absent it computes the selftest subset and records `"bank_missing": true`. |
| `lemmas/sim2_passage_reads.json` | New. Holds the READs of §10 verbatim, as {source, quote, page, status, bearing}. |

- **CLI:** `--selftest`, `--json PATH`, `--regenerate [--procs N]`, `--quick` (C24 at order 24 with a 3% tolerance).
- **X1–X10 docstring.** Add one line: "X1–X10 describe the board's configuration (eq. (17) as our plane's own metric); under 179–180 re-read (H-CORRIDOR-IN-BULK)".
- **X10 (c).** Its last sentence ("the change E-PASS needs is position 2's sheet: the coupled ends are the slab …") gets this note: "superseded in part by X13: position 2's piece regularises the crossing's past; it does not pay the crossing (Lemma S)". Do not delete it; item 178 cites X10.

### 1.2 Key and argument discipline

- Output keys may not contain the existing `BANNED_KEYS`: dist, separation, time, redshift, speed, velocity, length, clock, arrival.
  - So use no `timing`, `advanced_time` or `clock_class`. Use `hold_…`, `advanced`, `generator_class`.
- Function arguments may not be names in `sim2_facing.BANNED_ARGS`: d, D, sep, separation, distance, dist, gap, length, time, speed, velocity, redshift, arrival.
  - So depth arguments are named `dep`.
- The extended `address_guard` checks keys and also function signatures, the latter imported from `SF.BANNED_ARGS`.

### 1.3 New lemma names

These avoid clashing with sim2_facing's Lemmas T, C, W and N:
- **Lemma S**: the stationary pairing law.
- **Lemma K**: the crossing kinks the bulk horizon.
- **Lemma L**: the brane ledger of a changing crossing.
- **Lemma Q**: no sheet at our law focuses less than its tension.
- **Lemma P**: frames and Killing charges.
- **Lemma X**: excision (from design 2).
- Design 4's integrated identity is referred to as "the smooth-horizon identity".

---

## 2. Lemma 0, already decided: E-PASS without a second sheet [PLANE]

This goes first in the instrument and first in the note.

- **Statement.** With no second sheet, a curvature singularity lies in the causal past of the README's crossing and of every corridor event of the write. Stage 6's cone premise, under 174 (1)'s strict rule as the board decided it, refutes E-PASS on its own.
- **Advanced-time half (existing X1–X8, unverified).**
  - The Kasner layer is at finite conformal depth (η_s = 5.726 … 1.733 at the nine ℓ).
  - The exact AdS₂ criterion v_c − v_q ≥ ζ_q·2 sin²(η/4) holds.
  - The budgets are ≤ 223 clocks (layer K ≤ 10⁶ K_bs), against ≥ 2.0×10⁵.
  - This rests on H-HOLD-IN-ADVANCED-TIME.
- **Far-time half (new X11).** Before it crosses, the README's own events on end 1 at r = 2.02–2.2m already have stage 5's F2 surface in their past within ≤ 65 clocks, round trip (table in X11).
  - This needs only H-HOLD-FRAME, the plane's static clock.
  - So the refutation holds under every hold reading. Under 170 the README is null dust and has no proper time, and its pre-crossing events are plane events covered by X11.
- **Conjunction:**
  - eq. (17) on P1 at our tension, with clause (B) in full on P1;
  - vacuum Λ₅;
  - the analytic class;
  - the throat ODE and its O(x) correction, and stage 5's Padé columns, as evidence;
  - H-QUASI-STATIC-CORRIDOR;
  - a write of ≥ 2.0×10⁵ clocks (o3_write W3, kept by 163).
- **Labels:** computed and deduced.

---

## 3. M's words used (verbatim; typing kept; never paraphrased as M's)

- **101 (7):** "distance is irrelevant. The device only sees the two positions as one, never the distance between the two."
- **117:** "An NEC is never violated, between two entangled positions the NEC is like a coin, each position sits on a separate side. That action is that the coin flips. The NEC appears broken, but is not"
- **120:** "it was an methaphor to describe that the NEC only ever appears to break, but never does"
- **122:** "3 - your candidate is correct" (P1's future horizon and P2's past horizon); "4 - … The rules apply, but do not restrict information"
- **123:** "forget the coin metaphor."
- **126:** "The corridor will always entangle separate plane position using the shortest distance needed. The second position isn't built far away, it is realized in the same place the position 1 occupies while the corridor exists"
- **127:** "1 - yes"
- **128:** "A genuine loop would me creating a paradox of transition from position 1 to position 1."
- **129 (1):** "the corridor is a bridge, so it adds nothing to either position."
- **130 (1):** "i - no added matter."
- **132:** "yes. And the passage is one way by nature, a black hole in and a white hole out, side views of the same corridor object" and "*different views of the same object"
- **133:** "There is only one exact energy needed for any given README"
- **136:**
  - (2) "released at position two at the closing of the horizon";
  - (3) "it lives in a dimension that connects the positions. It is a bridge, not a physical place.";
  - (10) "the passage is not a ratio. It is an exact value of entanglement between any two given point.";
  - G "the README is the energy, not separate"
- **137 (1):** "1 - yes"
- **139:**
  - (1) "1 - yes";
  - (2) "positive, and you have to prove it.";
  - (3) "Absorbing of the README into position 2 is an expansion of that universe which means the README/information itself is the trigger.";
  - (4) "why are you still chasing distance/speed? This was ruled out"
- **140:** "Our math is not dependent on k, k is dependent on our work." and "Which is position 2's plane? - entangled. … Everything everywhere across every multiverse and every spacetime is always entangled is some way"
- **141:** "I suggest the planes are static, but their surfaces contain their own movements from within their own contained dimensions"
- **143 A:** "the only thing that can cross is that which can cross the horizon of a black hole."
- **152 (1):** "two separate positions connected by/reached through a dimension."
- **155 (2):** "Yes, in bits"
- **158:** (2) "Exactly as long as the write needs  I should think"; (4) "This too is a question for the math."
- **159:** "test both options"
- **160:** "the corridor and the opening are the same object"
- **161:** "my inclination is yes"
- **162:** "I submit that it may be more like a black hole, containing both mouths and throat at once. The throat doesn't change size because the whole chain object only every takes on the size that contains the README upon opening. It is and always will be only the size that is needed to hold the object once and at once"
- **163:** M chose "All together, one whole".
- **170:** "Position 1's clock gets absorbed into position 2's clock. However, time according to the object transported, because memory is part of the reconstruction, will always be relative to the clock of position 1, like an astronaut taking relative time with him"
- **172:** M chose (1) "Yes, it may" and (2) "Yes, that is coinciding". The board's question in (2) read "(so it never actually touches)".
- **173:** "Go ahead with E-PASS next"
- **174:** "For the math" (three times).
- **176:** "But what if it is in fact entanglement?" This is also the user's relayed question for this run.
- **177:** M chose "Yes, that is the appearance".
- **178:** "If the is a positive null energy, why not a negative null energy? We have positive and negative tension, charge, etc... I would imagine the very same principles apply to null energy."
- **179–181:** as quoted in §0.2.

---

## 4. Readings carried

### 4.1 M's readings, used as recorded

H-COUPLING-IS-THE-APPEARANCE (177), H-README-ON-P2 and H-COINCIDE-DOWN-THE-THROAT (172), H-ONE-WAY-BY-NATURE and H-HORIZON-AND-THROAT-HOLD (132), H-ONE-OBJECT and H-FIXED-SIZE (162), H-AT-ONCE-IS-WHOLE (163), H-HOLD-AT-BOUND (158 (2)), H-SIDES-AS-HORIZON-PAIR (122 (3)), H-STATIC-PLANES (141), H-CORRIDOR-IS-OPENING (160), H-CORRIDOR-IN-BULK (179).

### 4.2 The board's existing readings, carried as they stand

- H-QUASI-STATIC-CORRIDOR (stage 5).
- H-HOLD-IN-ADVANCED-TIME (ground).
- H-HOLD-FRAME.
- H-Z2-PIECES.
- H-SPLIT-AT-OUR-TENSION and H-COINCIDE-UP-TO-GAP (decided under 174).
- H-APPROACH-AT-DEPTH.
- H-POSITIVE-ON-P2.
- H-LAW-READ-BY-TRACE (phase 3 only).
- H-README-AS-NULL-DUST (opening.py).
- H-REACHED-ONLY-BY-THE-CROSSER (X9).
- H-PAIRING-IS-ENTANGLEMENT (176). X18 refutes the board's own sentence in it.

### 4.3 New readings, each named and each put to M

| reading | content | blocking? |
|---|---|---|
| H-FIXED-SIZE-AS-THETA-ZERO | 162's fixed size, read on the horizon the README crosses as zero expansion of its generators through the crossing. | No. Refusing it means the horizon grows: the standard accretion picture, against 162 as worded. |
| H-STATIONARY-CROSSING | The corridor (bulk and sheets) is stationary while the README crosses. Follows from H-QUASI-STATIC-CORRIDOR, 141 and 162 "always will be". Refused, it becomes E-NS. | No. Both branches are reported. |
| H-CROSSABLE-HORIZON | 143 read as admitting only sheets whose stress is bounded in a frame regular across u = 0 (the smooth and band classes; not S7's power law). | No. |
| H-PARTNER-IS-THE-COUPLING | 177 read as covering the exact negative null flux that Lemma S requires along the horizon. GJW's coupling produces exactly this kind, T_UU < 0 along the horizon. Decided by the board under 149; M can correct it. | No. The verdict is OPEN either way, because the supply is beyond the board's instruments. |
| H-POSITIVE-IN-OWN-FRAME | Once any negative null energy is admitted, 139 (2)'s "positive" can be met only as each piece's own-frame density, since boosted observers read densities unbounded below (Lemma P). | No. |
| H-README-AT-THE-THROAT | README stress on P1 across the throat (the cap, X22). As worded, 129 (1), 130 (1) and 172 (1)'s carry (clause (B) in full on P1) read against it. | No. The cap is a held configuration, not a passage. |
| H-NEC-IN-5D | A sheet's transverse null energy T(u+n,u+n) = ρδ(y). Reported beside the verdict only. | No. |
| H-WEYL-IS-THE-COUPLING-FOR-TEST-RAYS | Offered only. For test rays, eq. (17)'s projected Weyl term is the classical-5D form of the coupled ends (MM). Used in no decision. | n/a |
| H-PAIR-CANCELS-ON-THE-HORIZON | Offered for 176/178. The README's positive null energy and its partner's equal negative one sum to zero along every crossed generator. The NEC "appears broken" on one member and holds for the pair. | Put with the report. |

### 4.4 Dropped

H-POSITIVE-AS-PAIR-TOTAL (a total of zero is not "positive"); design 2's G4 (N bits; the normaliser makes it true by construction); design 3's δ-scan; H-COUPLING-ON-THE-PLANE versus H-COUPLING-IN-THE-WEYL-TERM (made moot by Lemma S); "the work selects k → 0" (140).

---

## 5. Setup and exact equations

**Units and constants.**
- m = 1 and e = m/ℓ.
- ν = 2/κ₅², σ_RS = 3ν/ℓ, κ₄² = 8πG_N = κ₅⁴σ_RS/6 = 2/(νℓ) (SMS eq. (19), READ).
- ℓ scan: SF.ES2 (∞, 32, 16, 8, 4, 2, 1, ½, ¼ m), plus 64m, 128m, 1024m and 4096m for asymptotics.

**Throat bulk [PLANE].**
- SF.throat_bulk(e): ds² = dy² + α²[−(x/2)(1+xa₁)dt² + (dx²/x²)(1+xb₁)] + 4β²(1+xc₁)dΩ².
- At the plane: α = β = 1, p = q = −e, a₁ = −½, b₁ = 5/2, c₁ = 1.
- EF chart (X1): x = u², t = v + 2√2/u, giving dy² + α²[−(u²/2)dv² + 2√2 dv du] + 4β²dΩ².
- The Killing field ξ = ∂_v has ξ·ξ = −α²u²/2, so it is null on u = 0 at every depth (X2).
- End 1 is u > 0 and end 2 is u < 0.

**Israel (one-sided, mirrored, normal into the kept side).**
- S^a_b = −ν(K^a_b − δK); for a sheet this gives K_ab = −(1/ν)(S_ab − h_ab S/3) (SMS eq. (16)).
- For an AdS₂-invariant stress at the horizon: ρ = −ν(K_r + 2q_Σ), P = ν(K_t + K_r + q_Σ), ρ + p_r = ν(K_t − K_r) → 0.
- Hence **q_Σ = −(2ρ + P)/(3ν)**.
- The README is null dust T = μ l⊗l, so T(k,k) = μ(l·k)² with k = ξ on the horizon.

**Contracted Gauss** (SMS eq. (3), READ PDF p.2):
- R⁽⁴⁾(k,k) = R⁽⁵⁾(k,k) − R(k,n,k,n) + K·K(k,k) − K(k,·)K(·,k).
- With K₀ having k as an eigenvector (eigenvalue p_Σ; angular eigenvalue q_Σ) and δK = −T/ν (traceless; δK·δK = 0 for null dust), the quadratic terms are exactly −(2q_Σ/ν)T(k,k).
- With held stress, −2q_Σ/ν = 8πG_N + κ₅⁴(ρ_m/3 + P_m/6). This is SMS eqs. (17) and (20) contracted with null k; checked algebraically in this spec.

**Raychaudhuri on a 4D generator:** dθ/dλ = −θ²/2 − σ² − R⁽⁴⁾(k,k). The convention is fixed by C16.

**Lemma S's kinematics.**
- On a Killing horizon, ∇_ξξ = κξ. For a sheet tangent to ξ, K(ξ,ξ) = −n·∇_ξξ = −κ n·ξ = 0.
- R(ξ,ξ) = 0 on any Killing horizon (computed identity, C18).

**Lemma K's kinematics.** In Gaussian normal coordinates, Γ^y_μν = −K_μν, so a null geodesic tangent to the sheet along k has y″ = K(k,k).

**Cap conic.**
- At y = 0 with α = β = 1: p² + q² + 4pq = 6e², i.e. 3s² − t² = 12e² with s = p+q and t = p−q. Our branch is s < 0.
- Stress: ρ + P = νt; ρ_m = −ν[(3s−t)/2 + 3e]; s_τ = −ℓs/2.

**O(x) system.** SF.throat_rhs. Momentum constraint: −¾a₁′ + ¼b₁′ − c₁′ + c₁(p − q) = 0. O(x) Hamiltonian constraint as in SF.throat_first_order.
- At the cap plane: a₁′ + b₁′ + c₁′ = 0 (Hamiltonian), and a₁′/4 + 5b₁′/4 = q (momentum, with p = 0 at ℓ = 4m). That leaves one free number μ.
- Radial null stress: (ρ + p_r) = c_r νx with c_r = (a₁′ − b₁′)(0)/2.
- In the crossing direction, E-normalised: T_KK = 2c_r ν.

**Clocks.**
- Global AdS₂ embedding: Y^{−1} = cos T/sin σ, Y⁰ = sin T/sin σ, Y¹ = −cos σ/sin σ.
- Generators are so(2,1) matrices.
- The throat's Poincaré form: x = 8/z² gives −(x/2)dt² + dx²/x² = 4(−dt² + dz²)/z², with z = 2√2/u (spec check).

**Bronnikov–Kim patches.**
- H = (1−2/r)(1−r₀/r)/(1−3/(2r)), F = 1 − 2/r.
- Near r₀ = 2 + δ: H ≈ x(x − δ), F ≈ x/2.
- x = δ/cos²χ gives 4(−dτ² + dχ²)/cos²χ, with dτ/dt = √(δ/8) and area 4 + 4δ/cos²χ (spec check `maps.py`).

**README energy (W1, STRUCTURAL).** E = mc² of the hole of N bits, so on P1 κ₄²∫T_vv dv = 8π·m/(4π(2m)²) = 1/(2m) per generator.

---

## 6. Results X11–X25

Each item gives its label, its functions and the expected numbers. Wherever an expected number differs from the instrument's value, the instrument's value stands, and the difference is reported in the note.

### X11 Lemma 0's far-time half: the README's own pre-crossing events [PLANE] (computed; deduced)

**Functions.**
- `precross_columns(es=(Fr(0),Fr(1,8),Fr(1)), radii=("101/50","41/20","21/10","43/20","11/5"), N=32, procs=3)` returns, per column, `{"ys", "hold_T90", "hold_T95", "Amin", "orders_agree"}` via `S5.column(e, N, rc)`. These are banked.
  - The criterion is stage 5's: three orders within 1%, otherwise UNDECIDED.
- `ingoing_leg_cost()`: sympy, with v = t + r\*(r) and dr\*/dr = 1/√(FH) for eq. (17). Along the ingoing leg dt = −dr\*, so dv = 0 exactly. Control: the outgoing leg gives dv = 2dr\* ≠ 0.
- `hold_readings()` returns three rows:
  - H-HOLD-IN-ADVANCED-TIME, with X7's budgets;
  - H-HOLD-FRAME, with these budgets;
  - 170's "time according to the object", with the README as null dust: no proper time, and its pre-crossing events are covered by H-HOLD-FRAME.
- Also add a deduced line: timing cannot help. Under 163 the README is held through ≥ 2.0×10⁵ clocks, and every corridor event after the budget has the layer in its past, however fast any crossing is.

**Expected round trip `hold_T90`** (ground-stage owner columns, one-way × 2; stage 5 F3, verified once, at r = 2.15m):

| r | ℓ = ∞ | ℓ = 8m | ℓ = m |
|---|---|---|---|
| 2.02m | 65.2 | 54.8 | 32.4 |
| 2.05m | 40.0 | 34.6 | 21.0 |
| 2.10m | 26.8 | 24.8 | 16.2 |
| 2.15m | 20.2 | 19.4 | 13.0 |
| 2.20m | 17.4 | 18.4 | 12.2 |

All are ≪ 2.0×10⁵ clocks.

### X12 Footprint, ceiling, Lemma X and the far gate [PLANE] (computed from the bank; STRUCTURAL; deduced)

**`footprint(bank=SF.load_bank())`.** R_F(ℓ) is the largest radius whose column has `ys_stable == True`. The ceiling y_s(r) is the median of that column's `ys`. Expected R_F (spec check from sim2_bank.json):

| e | 0 | 1/32 | 1/16 | 1/8 | 1/4 | 1/2 | 1 | 2 | 4 |
|---|---|---|---|---|---|---|---|---|---|
| R_F (m) | 2.2 | 2.2 | 2.2 | 2.2 | 2.15 | 2.2 | 2.1 | 2.5 | 10.0 |

- At e = 4, the columns at r = 3, 4 and 5 are unstable; r = 10 is stable (y_s = 0.867).
- Ceilings at ℓ = ∞: 2.589 (r = 2.005) … 2.630 (r = 2.2).
- Beyond R_F everything is **UNDECIDED, never "regular"**.

**`lemma_x()`** (STRUCTURAL; premise: the analytic class and unique continuation, standard-not-READ). It reuses X10 (c)'s computed data dependence.
- A two-sided sheet within one universe removes nothing.
- A mirrored (one-sided) sheet cannot end on P1.
- So excision within one universe needs a global one-sided sheet, or one that closes: phase 2b-i, OPEN G.

**`far_gate()`.**
- Exact: in the RS2 region a level P2 (K^a_b = +δ/ℓ, normal toward P1) has `israel` giving ρ = −σ_RS, so ρ_m = −2σ_RS at every depth.
- Imported `SF.far_level(Fr(1,32), 1.0)` gives −1.8913, −1.9917 and −1.9996 at r = 3, 5 and 10m. These are S14's numbers.

### X13 Lemma S, the stationary pairing law [FREE] (deduced; computed as identities)

**(a) Sheet form.**
- For every Israel sheet tangent to the corridor's Killing field ξ (P1; position 2's piece at any depth with any profile crossing u = 0), K(ξ,ξ) = 0 on the horizon. So S(ξ,ξ) = −ν[K(ξ,ξ) − (ξ·ξ)K] = 0.
- **While the corridor is stationary, the net surface null flux across its horizon vanishes on every sheet.** The README's T^R(ξ,ξ) ≥ 0 must be cancelled on the same sheet, generator by generator, by T^c(ξ,ξ) = −T^R(ξ,ξ).
- This holds for κ = 0 and κ ≠ 0, at any tension or law, within and between universes, coinciding or not.
- A held static stress has T(ξ,ξ) = 0 on the horizon automatically, so the partner must be a genuine negative null flux.
- Function: `pairing_sheet(gvv)`. Sympy. Sheet y = F(u) with general F, metric with general α(y), β(y). Returns K(ξ,ξ)|_H.
- Expected: 0 for g_vv = −α²u²/2 (degenerate) and for −α²(u² − 1/9)/2 at u = 1/3 (non-degenerate). Mutation: g_vv + εy sin v gives a nonzero value (spec check `lemmaS.py`).

**(b) Bulk form, for 179's corridor exclusive to the bulk.**
- R(ξ,ξ) = 0 on any Killing horizon, with no field equations used.
- With Einstein's equations and Λ₅ (Λg(ξ,ξ) = 0): T⁽⁵⁾(ξ,ξ) = 0. The README's 5D null flux across a stationary bulk horizon must be cancelled by equal negative null flux along the same generators.
- Function: `pairing_bulk(gvv)`. General stationary metric with g_vv = −A(y,u)u² or −A(y,u)u, g_vu = B, g_yy = D, angular part C.
- Expected R(ξ,ξ)|_{u=0} = 0 in both cases. Mutation (v-dependence) gives a nonzero value (spec check `lemmaS5.py`).

**(c) The Weyl term gives nothing.** Gauss on the brane gives R⁽⁴⁾(ξ,ξ) = −E(ξ,ξ), and R⁽⁴⁾(ξ,ξ) = 0, so E(ξ,ξ) = 0. The static bulk's Weyl term supplies nothing along the generators. A bulk field cannot change a sheet's surface flux.

**(d) Reading (the board's).** H-PAIR-CANCELS-ON-THE-HORIZON and H-PARTNER-IS-THE-COUPLING. The paired crossing changes S not at all. The board notes, without claiming it as M's meaning, that this is the shape of 129 (1)'s words.

### X14 Lemma K: a net-flux crossing kinks the bulk horizon [FREE for sheets] (deduced; computed)

**Statement.**
- In Gaussian normal coordinates, a null geodesic tangent to the sheet along the brane horizon's generator k obeys y″ = K(k,k) = −S(k,k)/ν.
- If S(k,k) > 0, it bends out of the kept side: positive brane null energy pulls bulk light onto the sheet.
- The null direction of a C¹ null hypersurface through the brane horizon is k, and the generators of a C² null hypersurface are geodesics. So a bulk horizon that is C² up to the sheet, with that trace, has S(k,k) = 0 there.
- **Consequence:** a net-flux crossing is a five-dimensional event (E-NS). The bulk horizon creases at the sheet, or separates from the brane horizon.
- The smooth-horizon identity (design 4's Lemma A) holds where the horizon is smooth, but it cannot be integrated across the README's support. Its B_start budget and its "q ≥ 0 absorbs classically" claim are withdrawn.

**Functions.**
- `tangent_deflection(Kvv)`: sympy, giving y″ = −Γ^y_vv = K_vv (spec check).
- `deflection_numeric(S_vv, nu=1)`: integrates the tangent geodesic in an explicit Gaussian normal metric with h_vv = 2yK_vv and K_vv = −S_vv/ν. Reports whether it stays in y ≥ 0 to 1e−12.

### X15 Lemmas L and Q, and the absorbing band [PLANE] (deduced; READ SMS; computed)

**Lemma L.**
- At fixed size (θ₄ ≡ 0) on the sheet carrying the README, pointwise: Ẽ(k,k) − R⁽⁵⁾(k,k) = −(2q_Σ/ν)T(k,k) + σ₄², with Ẽ(k,k) = R(k,n,k,n). In a vacuum Λ₅ bulk, Ẽ = E and R⁽⁵⁾(k,k) = 0.
- On P1: −2q/ν = 2/(νℓ) = 8πG_N.
- Integrated per crossed generator on P1, with W1: **∫(E − R⁽⁵⁾)(k,k)dλ ≥ 1/(2m)**, i.e. at least 0.5 per clock of v.

**Lemma Q.**
- q_Σ = −1/ℓ − [ρ_m + (ρ_m + P_m)]/(3ν) ≤ −1/ℓ − ρ_m/(3ν) under H-SPLIT-AT-OUR-TENSION, with ρ_m ≥ 0 and angular NEC.
- So every positive, angular-NEC sheet at our law needs at least P1's Weyl support.
- Sheets with q_Σ ≥ 0 have negative ρ_m or broken angular NEC.

**Position 2's piece.**
- For any crossable profile, q_Σ = −q(dep): at u = 0, n^u = 0, and the n^v term vanishes because ∂_v ln β = 0.
- So q_Σ ≥ 0 if and only if dep ≤ d_β, where d_β is β's minimum.
- Deduced asymptotics:
  - q(0) = −e, q′(0) = ¼ and p′(0) = −¼ exactly, so d_β = 4m²/ℓ(1+…);
  - ρ_m(d_β) → −5σ/3, d₊/d_β → 6, q(d₊)ℓ → 5, d0 → 12m²/ℓ.

**Functions.** `q_sigma(rho, P, nu)`; `lemma_q_samples(n=2000, law=+1, seed=11)`; `absorbing_band(e)` returning `{"d_beta", "rho_m_at_dbeta_rs", "ang_at_dbeta_rs", "d_plus", "dplus_over_dbeta", "q_dplus_ell", "d0"}`.

**Expected** (spec check `dbeta.json` and `qdplus.py`):

| ℓ | d_β | ρ_m(d_β)/σ | (ρ+P)(d_β)/σ | d₊ | d₊/d_β | q(d₊)ℓ | d0 |
|---|---|---|---|---|---|---|---|
| 4096m | 0.00097656 | −1.666667 | 0.666667 | 0.0058594 | 6.0000 | 5.0000 | 0.0029297 |
| 1024m | 0.0039062 | −1.666668 | 0.666668 | 0.023439 | 6.0005 | 5.0006 | 0.011719 |
| 128m | 0.031230 | −1.666721 | 0.666721 | 0.18834 | 6.0309 | 5.0359 | 0.093750 |
| 64m | 0.062338 | −1.666883 | 0.666883 | 0.38227 | 6.1322 | 5.1536 | 0.18751 |
| 32m | 0.123717 | −1.667525 | 0.667525 | 0.83954 | 6.7860 | 5.9121 | 0.37537 |
| 16m | 0.240152 | −1.669985 | 0.669985 | none | — | — | 0.76665 |
| 8m | 0.432046 | −1.678435 | 0.678435 | none | — | — | none |
| 4m | 0.641243 | −1.699999 | 0.699999 | none | — | — | none |
| 2m | 0.715734 | −1.733485 | 0.733485 | none | — | — | none |
| m | 0.624981 | −1.765544 | 0.765544 | none | — | — | none |
| m/2 | 0.465564 | −1.788036 | 0.788036 | none | — | — | none |
| m/4 | 0.314347 | −1.801416 | 0.801416 | none | — | — | none |
| ∞ | 0 | 0 | 0 | 0 | — | — | 0 |

- At d_β the identity ρ_m = −σ − (ρ+P) holds exactly, since 2ρ + P = 0 there.
- At d₊ for 32m, the angular part is ν(q − p) = 0.4605ν > 0.

### X16 The crossable class at the horizon [PLANE] (computed)

**`crossing_profiles(e, dep)`** uses `SF.piece_stress(tb, dep, x, ("local", f_u, f_uu))` on both ends, with u = ln x in sim2_facing's profile variable:
- End 1: f_u = g₁√x/2 + g₂x, f_uu = g₁√x/4 + g₂x.
- End 2: the same with g₁ → −g₁.
- g₁ = 0.05 and g₂ = `SF._smooth_g2`.
- Evaluated at x = 1e−8, 1e−11 and 1e−14.

**Expected.**
- On both ends, ρ tends to the level value ν(p + 2q)(dep) within 1e−6σ at x = 1e−14.
- (ρ + p_r)/x converges (EF-bounded).
- The NEC on end 2 is evaluated, not assumed.
- The power law ("pow", 0.25) has (ρ + p_r)/x growing like x^{−3/4}, by at least 10³ from 1e−8 to 1e−14 (EF-unbounded; S7's growth).
- Consequence: no crossable sheet trades positive energy for broken angular NEC at the horizon.

**`pinch_point(dep_frac=1e-4)`.** At ℓ = ∞, g₁ = 0.05 and g₂ = −1: the smooth family continued across u = 0 meets P1 at u_× = −0.0046715, against −d/g₁ = −0.0051071 (spec check). It lies inside the O(x) domain if and only if g₁ > d/u_lim, which is a map.

### X17 The demands [FREE stationary; PLANE changing] (deduced; computed)

**Stationary (Lemma S).**
- T^c(ξ,ξ) = −T^R(ξ,ξ) pointwise.
- On P1, per generator: κ₄²∫T^c_vv dv = −1/(2m).
- On the README's sheet under 172 (1), the same, in that sheet's normalisation.

**Changing (Lemma L).**
- ∫(E − R⁽⁵⁾)(k,k)dλ ≥ 1/(2m) on P1.
- On position 2's piece at d₊ the coefficient is |q(d₊)|ℓ times P1's: 5.912 (32m), 5.154 (64m), 5.036 (128m), 5.0006 (1024m), tending to 5.

**`readme_flux_P1()`.** Sympy: 8π·m/(4π(2m)²) = 1/(2m) exactly. Mutation r² → r fails.

**`demand_si()`.**
- At o3_write.EXAMPLE_N = 2742570311524972: E = exactE.e_per_sqrt_bit()·√N = 2.40588×10¹⁶ J, m = GE/c⁴ = 1.98791×10⁻²⁸ m, 1/(2m) = 2.51521×10²⁷ m⁻¹.
- At item 155's E = 3.8×10²² J: m = 3.13983×10⁻²² m, 1/(2m) = 1.59244×10²¹ m⁻¹.
- G's relative uncertainty, 2.25×10⁻⁵, is carried (CODATA, standard-not-READ; G as banked in o3_write).

**Set beside the demands (READ, parametric, never a supply).**
- GJW: ANEC violation is a prerequisite; the coupling joins the boundaries "with the same time orientation"; footnote 2; ΔV ∼ hG_N/R^{D−2}.
- MSY: "we cannot send more information through the wormhole than we transferred in order to set up the OO interaction"; eq. (2.25); "only parametric bounds".
- MQ PDF p.53.
- MSY's bound is set against 122 (4)'s "The rules apply, but do not restrict information". Reported, not decided.

**Answer to 158 (4)'s "a question for the math".**
- Stationary: nothing net is absorbed. The pair cancels.
- Changing: into the bulk's Weyl field and the creased bulk horizon. This is a necessary condition only.

### X18 Ends, generators and Lemma P: the answer to 176 [FREE given an AdS₂ throat] (computed; deduced; READ)

**`generator_classes()`.** Spec check `maps.py`.
- ∂_T is elliptic (eigenvalues ±i, 0), with boundary components 1 and 1.
- The boost about the origin is hyperbolic (eigenvalues ±1, 0), with −cos T at σ→0 and +cos T at σ→π.
- The other boost gives +sin T and −sin T.
- J ± K are parabolic: M³ = 0, M² ≠ 0, components 1 ± sin T at the two boundaries, both ≥ 0.
- The throat's ∂_v is Poincaré time (x = 8/z²), hence parabolic.
- Deduced from z = 2√2/u: u > 0 is the Poincaré patch on one boundary, u < 0 the one on the other, and u = 0 is patch 1's future horizon and patch 2's past horizon (122 (3), 132).

**`lemma_p(n=1000, seed=5)`.**
- (i) A δ-stress S = sδ reads density −s for every observer (exact rationals).
- (ii) Eq. (17)'s Weyl fluid at r = 3m (ρ_W = 1/81 and ρ_W + p_r = −2/81, in units of 1/(8π), S5's R̂_rad) reads ρ′ = ρ + γ²v²(ρ + p) < 0 beyond the boost parameter v\* = 1/√3 = 0.577350 (rapidity atanh(1/√3) = 0.658479). This is an observer's boost, not a speed.
- (iii) The Killing charge flips under the boost at one boundary and not under the parabolic generator.

**Deduced.**
- S15's coincident −σ_RS is a δ-stress, so no clock makes it positive.
- The board's own 176 sentence ("position 2's −1 would be the partner's sign seen from our side") is **refuted for this object**.
- The corridor is the extremal (parabolic) member of the entangled family: between the thermofield double (hyperbolic, thermal, no passage) and MQ's coupled wormhole (elliptic, no horizon, two-way).

### X19 Three phases of a coupling [PLANE] (STRUCTURAL, sympy; READ)

**`bk_patches()`.**
- δ > 0 gives global AdS₂ 4(−dτ² + dχ²)/cos²χ with dτ/dt = √(δ/8) and area 4 + 4δ/cos²χ.
- δ = 0 gives Poincaré.
- δ < 0 gives Rindler 4(−sinh²ρ dτ² + dρ²).
- These are MQ eqs. (2.1)–(2.2) (READ).

**Corollary (deduced).** A coupling of MQ's eternal kind is r₀ > 2m. It has no horizon (MQ PDF p.53, READ), against 143 A, 132 and clause (G). It is not E-PASS. **No δ-scan.**

### X20 The classical placements of E-Q [PLANE] (computed; deduced; READ)

- **(a) MQ (2.10) analogue on the plane's chain.** Per leg, 8π × X10(b) equals `coin.anec_closed(1,2)` = −0.8264360024660358 to 1e−12 (spec check). The whole passage is −1.6528720049. Schwarzschild gives 0. coin at r₀ = 1.8m gives −1.914712. For test rays the ends are already "coupled" classically by eq. (17)'s Weyl term.
- **(b) Generator versus crossing direction.** R⁽⁴⁾(ξ,ξ) → 0 as r → 2m (sympy limit), while along the crossing direction, E-normalised, `sim1_transition.eq17_rkk`/F → −1 at r = 2m. The README's ledger uses the generator.
- **(c) Weyl.** Lemma S (c): a bulk Weyl term changes no surface flux.
- **(d) Conformal coupling layer** T^A_B = c(δ − 5nn) in the slab: Gauss at P1 (R⁽⁴⁾ = 0, K = −h/ℓ) gives T_yy = 0, so c(0) = 0. Bianchi gives c′ = −(5/2)(p+q)c (spec check), so c ≡ 0.
- **(e) Persistence.** `throat_bulk(e, s2=1±1e-3)` moves y_s by O(10⁻³), and the Kasner exponents are unchanged to 1e−4. With X10 (c) and KR's open singular interval (READ p.7): E-Q that leaves the plane's data unchanged cannot remove the layer.

### X21 The transverse reading and the two pairs, for 177 and 178 [PLANE; Lemma S's pair FREE] (deduced; computed)

- **(a) Transverse.** T(u+n,u+n) = ρδ(y) for a sheet: P1 gives +σ, the coincident P2 gives −σ, and the sum is 0 (via `SF.coinciding`). The d0 table is in X15. H-NEC-IN-5D, reported beside the verdict.
- **(b) Tangential at coincidence.** A pure tension: S_m(k,k) ≤ 1e−6σ. So 177's "negative null energy", read as tangential, does not reach coinciding's cost (−2σ is an energy density).
- **(c) Lemma S's pair.** The README plus its partner along the horizon, net zero.
- These are **two distinct pairs**. The report keeps them apart, and offers both for 178.

### X22 The cap: a held configuration [PLANE] (computed; conditional on H-README-AT-THE-THROAT; build after the core)

**Functions.**
- `conic_scan(e, n=400)` returns the endings along s < 0 and counts α→0 / β→0 switches. Expected: one.
- `cap_brane(e)` bisects t.
- `cap_tip(e)` shoots from KR's tip series (2.9) with k = −1, A₀ as the shooting parameter and an adaptive bracket from the brane-side α_c (needed at m/4). It integrates until A = R, scales to L = 2m, and returns t\*.
- `cap_exact_4m()`.
- `cap_stress(e)`.
- `cap_ox(e)` finds μ\* by shooting to z₀ = y_c − y ∈ {1e−3, 1e−4, 1e−5} with the root of a₁z, extrapolated to z₀ → 0. It returns c_r, T_KK = 2c_rν, and c₁z → const (the gauge mode).
- `cap_lambda_scan(e, lams)` works on the homogeneous O(x^λ) system re-derived by sympy, with eq. (17) fixed on the plane (a = b = c = 0 at y = 0; constraints at order λ), and returns the sign of the singular axis coefficient S_a(λ).
- `cap_sms(e)`: local part κ₄²τ_kk + κ₅⁴π_kk, with π from SMS eq. (20) (it equals T_kk(ρ_m/3 + P_m/6)), against R_KK(eq. 17) = −1.

**Expected** (spec check `cap.py` and `cr4.py`; design pilot otherwise):

| ℓ | t\* | q\* | ρ_m\* (ν/m) | ρ_m\*/σ | c_r |
|---|---|---|---|---|---|
| ∞ | 0.727722 | −0.573937 | 0.99409 | — | −0.6433 |
| 32m | 0.725492 | −0.574496 | 0.90425 | 9.645 | −0.6432 |
| 16m | 0.718900 | — | 0.822 | 4.38 | −0.6428 |
| 8m | 0.693940 | −0.583094 | 0.68034 | 1.814 | −0.6409 |
| 4m | 0.6123724 (√(3/8)) | −0.6123724 | 0.47474 | 0.6330 | **−0.62773** |
| 2m | 0.436169 | −0.733694 | 0.26491 | 0.1766 | −0.5431 |
| m | 0.244799 | −1.124893 | 0.12988 | 0.04329 | −0.330 |
| m/2 | 0.124724 | — | 0.063 | 0.0106 | −0.151 |
| m/4 | 0.062488 | — | 0.031 | 0.0026 | to compute |

- At 4m: μ\* = c₁′(0) = 1.653471, c₁(y_c − y) → 3.2852, constraints ≤ 1.2e−9 (spec check). Exact cap: AdS₂(2m) × H³(2√2m), y_c = 2√2 asinh(1/√2) = 1.862460, α ≡ 1. It is KR's eq. (2.18) member, with the brane at sinh = 1/√2 instead of KR's 1.
- λ\* = 1.62957 at 4m, with no regular mode on (0, 1.6] (judge).
- **Verdict line:** regular near the throat; positive and NEC-obeying at zeroth order; NEC broken beside the horizon at O(x) at every ℓ computed. Nothing crosses: a held stress has T(ξ,ξ) = 0. If the README were made to cross, q\* ≤ −0.574 puts it under Lemmas L and S like P1. Off the throat: **UNDECIDED (E-DIR)**.

### X23 Kaus–Reall reproduced [PLANE support] (computed; READ)

- `kr_ode_identity(k=-1)`: with A = 2mα, R = 2mβ and y = ρ₀ − ρ, KR's eqs. (2.4), (2.6) and (2.7) minus SF's P, Q and constraint simplify to 0. Mutation k = +1 gives nonzero differences.
- `kr_exact()`: (2.18) A ≡ ℓ/2, R = (ℓ/√2)sinh(√2ρ/ℓ) solves (2.4)–(2.7) exactly. Israel (2.16) at sinh(√2ρ₀/ℓ) = 1 gives Q = ℓ/√2, L₁ = ℓ/2 and L₂ = ℓ/√2, which are (2.20)–(2.21).
- `kr_q0_end(e)`: Q = 0 data reach α → 0 at SIM2's y_s^th: 2.553551 (∞), 2.374421 (32m), 1.986775 (8m), 0.913855 (m).
- `kr_small_bh()` (full run only): L₁, L₂ and ρ₀ over (ℓQ²)^{1/3} extrapolate to [0.22, 0.26], [0.64, 0.68] and [0.54, 0.58]. Israel is solvable at 0.95ℓ and not at 1.05ℓ.
- Premise check (READ): KR's ref. [16] is Kunduri–Lucietti–Reall arXiv:0705.4214, whose Lemma 0 is READ (pp.4–5). This resolves judge 1's "read [16] at the source" risk.

### X24 Between universes, the phase 3 column [PLANE] (deduced; computed; never reported as a within-universe result)

- Lemma S does not depend on the law. So a stationary crossing between universes also needs the exact pair. **Design 4's O-C is withdrawn.**
- In a changing crossing on a sheet with q_Σ ≥ 0 (for example the coincident P2 at −σ, with q_Σ = +1/ℓ), Lemma L needs no Weyl support. It is still a 5D event (Lemma K).
- The coincident pair's coefficients cancel: c₁ + c₂(0) = 2/(νℓ) − 2/(νℓ) = 0.
- Handed to phase 3 with E-ASYM.

### X25 The decision table [mixed] (deduced from X7–X24)

The gates are:
- **G1 REGULAR PAST** (174 (1)).
- **G2 POSITIVE** (139 (2); H-POSITIVE-ON-P2, own frame).
- **G3 NEC** (117/120; 177's class taken as H-PARTNER-IS-THE-COUPLING).
- **G4 CROSSES AT FIXED SIZE** (143 A, 132, 162, 163): Lemma S when stationary; Lemmas L, Q and K when changing.

| row | G1 | G2 | G3 | G4 | verdict |
|---|---|---|---|---|---|
| R0 no second sheet, README on P1 | ✗ (X7: ≤ 223 clocks; X11: ≤ 65) | — | — | stationary ✗ classically; changing needs ∫E ≥ 1/(2m); clause (B) on P1 (cost) | REFUTED (G1 alone suffices) |
| R1 cap (README held on P1 at the throat) | near throat ✓; off-throat UNDECIDED | ✓ at the throat | ✗ at O(x) | nothing crosses | held configuration, not a passage |
| R2 P2 at depth ≤ d_β | near throat ✓; cover OPEN G | ✗ (ρ_m ≤ −1.6675σ at 32m … −1.8014σ at m/4) | ✓ angular | stationary ✗ classically; changing is a 5D event | REFUTED on G2 |
| R3 d_β < depth < d₊ | as R2 | ✗ | ✓ | as R4 | REFUTED |
| R4 depth ≥ d₊ (ℓ > 27.07m only) | near throat ✓; cover to R_F = 2.2m and far closure OPEN (E-FAR, E-G) | ✓ | ✓ classically | stationary: exact pair only (classical ✗; with 177: OPEN, demand = the README's own); changing: coefficient 5.9 → 5 × P1's (E-NS, OPEN) | classical REFUTED; OPEN only as the coupled ends' exact pair (supply not computed) or as E-NS |
| R5 coinciding, depth → 0 | slab pinches at the crossing (X9, X16) | ✗ at every finite ℓ (−2σ, S15) | marginal | as R2 | REFUTED at finite ℓ; at ℓ = ∞ a LIMIT on G2 only (G4 stationary still needs the pair) |
| R6 E-Q, classical (Weyl; conformal layer; BK gap) | — | — | — | E(ξ,ξ) = 0; layer ≡ 0; r₀ > 2m has no horizon | pays nothing |
| R7 coupled ends, quantum (177) | — | — | admitted | exact negative partner per generator (sheet form, or bulk form under 179) | OPEN (demand exact; supply beyond the board) |
| R8 changing corridor (E-NS; 152 (2), 160) | open | — | — | ∫E ≥ 1/(2m) on P1; creased bulk horizon | OPEN → phase 2b-ii, with its number |
| R9 between universes | phase 3 | — | — | Lemma S holds; pair needed | handed to phase 3 |

**Combined answer, to print in the note.**
- Within one universe at our tension, no configuration is shown to carry the README across the corridor object's horizon with a regular past through the write.
- Position 2's near-coinciding piece regularises the crossing's past near the throat. It does not make the crossing possible.
- A stationary horizon of fixed size is crossed only by an exact ± null pair (Lemma S).
- A changing horizon needs the bulk to deliver at least the README's focusing (Lemmas L, Q and K).
- Classical E-Q supplies none of this. Quantum E-Q can, but only as the exact partner, which the board cannot compute.

---

## 7. Outcomes for B4d and O3

All outcomes below were possible before computation.

- **E1 (expected): C17–C19 pass.**
  - **B4d's E-PASS row changes** from "the next instrument" to: "stationary: needs an exact ± null pair along the horizon (Lemma S, any sheet and any law); classical matter cannot supply it; with 177 it is OPEN, the supply not computable. Changing: needs ∫E dλ ≥ 1/(2m) per crossed generator on our plane, and creases the bulk horizon (E-NS, phase 2b-ii). Regularity: without a second sheet, refuted under every hold reading; with the near-coinciding piece, regular near the throat; the cover and the far field are OPEN G."
  - Within one universe, the classical static E-PASS is refuted on this conjunction:
    - H-STATIONARY-CROSSING;
    - H-FIXED-SIZE-AS-THETA-ZERO;
    - Israel sheets tangent to ξ (H-Z2-PIECES);
    - NEC on all classical matter (117/120).
  - It needs no Padé, no clause (B) on P2 and no hold reading.
  - **B4d stays OPEN. O3 stays OPEN as B4d's.**
- **E2: C17 or C18 fails.** That means a code error, since both are identities. Lemma S is withdrawn and the verdict reverts to regularity plus Lemma L.
- **E3: the cap's λ-scan finds a regular mode with λ ≤ 1 at some ℓ.** The cap's NEC-at-O(x) row is withdrawn at that ℓ. The passage verdict is unaffected.
- **E4: a generator class is not parabolic.** Impossible algebraically; the controls prove the classifier can return the other classes. If it happened, 176's sign reading would become admissible, with existence still open.
- **E5: at some ℓ the bank has no order-stable surface at r ≥ 2.02m.** Lemma 0 then rests on X7 alone.
- **Nothing in this instrument can make B4d green or move O3.**

---

## 8. Selftest: C15–C35 added to the existing C1–C14 (each able to fail; mutations named)

| check | what must hold | mutation that must fail |
|---|---|---|
| C15 Gauss (SMS eq. (3)) | Explicit polynomial metric dy² − A dt² + B dr² + C dΩ² at (t, r, θ) = (1/3, 5/2, 7/10): residual 0 (spec check) | sign of R(k,n,k,n) flipped gives −0.6249 |
| C16 transport and Raychaudhuri | On −2dudv + a²dy² + b²dz₁² + c²dz₂²: R(k,e,k,e) + dB_ee/dλ + B_ee² = 0 with e parallel; Raychaudhuri residual 0 | coordinate derivative of the component B_yy leaves 2a_v²/a² |
| C17 Lemma S, sheet | K(ξ,ξ)\|_H = 0 for a general sheet, degenerate and non-degenerate | non-stationary g_vv gives a nonzero value |
| C18 Lemma S, bulk | R(ξ,ξ) = 0 at the horizon, general stationary metric | v-dependence gives a nonzero value |
| C19 Lemma K | y″ = K_vv; numeric geodesic leaves y ≥ 0 if and only if S_vv ≠ 0 | S_vv = 0 must stay to 1e−12; flipped Israel must deflect the other way |
| C20 junction coefficient | Quadratic Gauss terms equal −(2q/ν)T_kk; at q = −1/ℓ they equal κ₅⁴σ_RS/6; with held stress they equal 8πG_N + κ₅⁴(ρ_m/3 + P_m/6) | two-sided Israel factor (gives 4/(νℓ)); first-draft p + 2q (gives 3/(νℓ)); normal flipped in δK only (sign) |
| C21 Lemma Q | q_Σ = −(2ρ+P)/(3ν) (sympy); 2000 random rationals at our law have max q_Σ ≤ −1/ℓ | law −σ must find q_Σ ≥ 0 with positive NEC matter |
| C22 band | d_β(32m) = 0.123717 ± 1e−5; d_βℓ/4 at 4096m = 1 ± 1e−5; d₊/d_β at 4096m = 6 ± 1e−3; ρ_m(d_β)/σ at 4096m = −5/3 ± 1e−5; ρ_m(d_β) = −σ − (ρ+P) to 1e−10 at all ℓ; q(d₊)ℓ at 1024m = 5 ± 1e−3; no d₊ for ℓ ≤ 16m | planted q → q − 6e must flip the overlap flag |
| C23 crossable class | Both ends tend to the level value within 1e−6σ; (ρ+p_r)/x converges; u_× = −0.0046715 ± 1e−5 | power law 0.25 must diverge by at least 10³ |
| C24 far time | `S5.column(Fr(0),32,"43/20")` gives median hold_T90 within 2% of 20.2; ingoing dv = 0 | control column r = 3m at ℓ = ∞ (no order-stable `ys`) must return "none within the verified top" |
| C25 footprint | R_F table exact; flags True | reading `ys` without `ys_stable` (R_F → 10m at ℓ = ∞) must be refused |
| C26 demands | 1/(2m) exact; SI values to 1e−5 relative | r² → r |
| C27 cap (ℓ ∈ {∞, 4m, m}) | one switch; t\* to 1e−5; exact √(3/8) to 1e−9; y_c = 1.862460 to 1e−6; α ≡ 1; q\* < 0; tip and brane agree to 1e−7 | s2 = −1 gives no switch; sign of the tip ρ² coefficient flipped gives residual > 1e−3 |
| C28 cap O(x) at 4m | μ\* = 1.65347 ± 1e−3; c_r = −0.62773 ± 3e−4; c₁z → 3.285 ± 0.01; constraints ≤ 1e−8 to 0.9y_c; coarse λ-scan with no sign change on (0, 1.6] and one at 1.6296 ± 0.005; Frobenius μ (log in c₁) equals the shooting μ within 1e−3 | drop c₁/(2β²) moves μ\* by > 1e−2 |
| C29 KR | identity 0; (2.18)–(2.21) exact | k = +1 gives nonzero differences |
| C30 generators | classes and boundary components as in X18; x = 8/z² gives Poincaré | non-degenerate g_vv must classify hyperbolic; outgoing chart puts end 2 on σ = 0 |
| C31 Lemma P | 1000 boosts preserve δ-density; v\* = 1/√3 exactly; NEC-obeying gives ρ′ ≥ ρ | p_r sign flipped gives no v\*; ξ·ξ in place of ξ·n removes the flip |
| C32 patches | maps exact; dτ/dt = √(δ/8) | r₀ = 2m − δ in the global map leaves a residual |
| C33 classical placements | 8π·X10(b) = −0.826436002 to 1e−12; R⁽⁴⁾(ξ,ξ) → 0; crossing-direction value → −1; c′ = −(5/2)(p+q)c; T_yy(P1) = 0; s2 ± 1e−3 persistence | AdS₄-sliced plane data (R⁽⁴⁾ ≠ 0) must allow c(0) ≠ 0 |
| C34 transverse and pairs | S(u+n,u+n) sums to 0 to 1e−12; tangential ≤ 1e−6σ; d0(32m) = 0.375374 ± 1e−5; d0ℓ/12 at 4096m = 1 ± 1e−6 | normal out of the slab gives s = +1 |
| C35 guards | keys and arguments (names only, labelled as such); every row carries one of the six labels; every READ has a page | a planted key "hold_time" must be caught |

- **Selftest budget** (measured in spec checks: Lemma S identities about 2 s, cap about 34 s for six ℓ, O(x) about 3 s): **≤ 4.5 min.** C24's live column (about 60–100 s) is the largest item. `--quick` runs C24 at order 24 with a 3% tolerance.
- **Full run:** 15 owner columns on 3 processes (about 6–8 min), plus nine caps, O(x) and λ-scans (about 5 min on 3 processes). About 15 min wall time.

---

## 9. Owners imported by path, never copied

- `lemmas/sim2_facing.py`: throat_bulk, throat_rhs, throat_first_order, kret_throat, israel, piece_stress, _profile, _smooth_g2, _ystar, wec_window, coinciding, far_level, load_bank, x_valid, address_guard, BANNED_ARGS, ES2, S5.k_bs, B4._eq17, B4._schwarzschild, _ricci_diag.
- `lemmas/b4d_stage5.py`: column, evaluator, nearest_real, orders, k_bs.
- `lemmas/b4_static.py`: series and the eq. (17) data, via SF.B4.
- `lemmas/sim1_transition.py`: eq17_rkk (S3b is the 4D limit of Lemma L).
- `copy/coin.py`: anec_closed, anec_leg.
- `copy/exactE.py`: e_per_sqrt_bit.
- `lemmas/o3_write.py`: EXAMPLE_N, G_SI, C_SI, t_min (via the existing write_floor).
- `lemmas/ledger.py`: e4 (the E/4 control, if the note cites E4).
- `lemmas/epass_ground.json`: expected values and READ quotes only. These are scratch from the ground stage and never imported as evidence.
- The existing X1–X10 functions of `sim2_passage.py` itself: tb, eta_of, budget, layer, slab_rows, plane_null_energy, data_fixes_bulk.

---

## 10. READs to cite (READ status only; verbatim; PDF page)

**Kaus–Reall, arXiv:0901.4236v1.**
- PDF p.4: "In the bulk, the surface gravity is constant. Hence, by continuity, it will take the same value on the brane. Therefore if the horizon is degenerate on the brane then it will also be degenerate in the bulk. … It was proven in [16] that the near-horizon geometry of a static extreme black hole can be written in the warped product form".
- PDF p.13, ref. [16]: "H. K. Kunduri, J. Lucietti and H. S. Reall, 'Near-horizon symmetries of extremal black holes,' … [arXiv:0705.4214 [hep-th]]".
- PDF pp.4–5: eqs. (2.2)–(2.7).
- PDF p.5: (2.8), and "R is monotonically increasing in the bulk".
- PDF p.6: (2.16)–(2.17); and "First, if A0 = ℓ/2 we find A ≡ ℓ/2, R = (ℓ/√2) sinh(√2ρ/ℓ). (2.18) The bulk metric is then AdS2 × H3."
- PDF p.7: "For the AdS2 × H3 solution we find that the Israel equations are satisfied if sinh(√2ρ0/ℓ) = 1, Q = ℓ/√2. (2.20) We then have L1 = ℓ/2 = Q/√2, L2 = ℓ/√2 = Q. (2.21)"; the singular branch; "The Israel junction condition can be satisfied if, and only if, 0 < A0 < ℓ".
- PDF p.9: "L1 ≈ 0.24(ℓQ²)^{1/3}, L2 ≈ 0.66(ℓQ²)^{1/3}, ρ0 ≈ 0.56(ℓQ²)^{1/3}".

**Kunduri–Lucietti–Reall, arXiv:0705.4214v3**, pp.4–5: "Lemma 0. A static near-horizon geometry is locally a warped product of a 2d maximally symmetric space-time with a compact (D − 2)-manifold." (ground READ).

**Shiromizu–Maeda–Sasaki, gr-qc/9910076v3.**
- PDF p.2: eq. (3), the contracted Gauss equation; eq. (9), "Note that E_μν is traceless".
- PDF p.3: eqs. (16), (17), (19) "G_N = κ⁴₅λ/48π" and (20).
- PDF p.6: (A8), Ẽ_μν = −£_n K_μν + K_μα K^α_ν.

**Maldacena–Qi, arXiv:1804.00491v3.**
- PDF p.3: "AdS2, viewed as a global spacetime, has two boundaries that are causally connected."
- PDF p.6: eqs. (2.1)–(2.2), and "a different generator for each of the coordinate systems".
- PDF p.7: eq. (2.10); "the left hand side is negative if φ is growing towards both boundaries"; footnote 2, "(2.10) is the two dimensional version of the Raychaudhuri equation."
- PDF p.8, footnote 3: "the AdS2 stress tensor should be SL(2) invariant."
- PDF p.9: "a finite amount of negative energy is enough".
- PDF p.20: t′ "is an effective (rescaled) temperature".
- PDF p.28: "the time to go accross is π". Cite as MQ's statement about their own wormhole only.
- PDF p.53: "The full geometry will not contain a horizon" and "The throat is supported by negative null energy … produced by quantum effects."
- PDF p.64: (B.171), H_R − H_L is "the boost generator around the origin in AdS2".
- PDF p.6's "Since the metric is set to be exactly AdS2 …" describes JT's construction and is **never cited as evidence about the 5D bulk**.

**Gao–Jafferis–Wall, arXiv:1608.05687v3.**
- PDF p.2: "Violation of the averaged null energy condition (ANEC) is a prerequisite for all traversable wormholes".
- PDF p.3: eq. (1.2), "This connects the boundaries with the same time orientation".
- PDF p.4: "|tfd⟩ is invariant under H_R − H_L, which corresponds to the bulk Killing symmetry i∂_t (note the directions are opposite in left and right wedges)"; footnote 2, "We do not consider the case of a time-independent interaction, in order to prevent the quantum state from becoming non-regular on the past horizon."
- PDF p.12: eq. (5.1), ΔV ∼ hG_N/R^{D−2}.
- PDF p.13: "An object travelling at light speed from left to right contributes to T_VV but not to T_UU"; footnote 8, "Presumably there is some limit on how much information can get through".

**Maldacena–Stanford–Yang, arXiv:1704.05333v1.**
- PDF p.13: "the backreaction effect … is enough to ensure that we cannot send more information through the wormhole than we transferred in order to set up the OO interaction … We will not provide sharp bounds, only parametric bounds."
- PDF p.14: eq. (2.25).
- PDF p.11, footnote 5: "In higher dimensions we have tidal forces if the operators O_L O_R are localized in the extra dimensions."
- PDF p.21: "−P− = ∫dx−T−− ≤ 0. However, the actual ADM energy, or killing energy, is given by E = ∫dx−x−T−−. The fact that this can be positive, negative or zero"; Fig. 7(c), "too weak to make the wormhole traversable".

**Maldacena–Milekhin, arXiv:2008.06618v2.**
- PDF p.6, footnote b: "The Casimir energy contribution from the effective two dimensional theory is the leading contribution that violates the SL(2) symmetry".
- PDF p.11: "This circle is then 'filled in' by the extra dimension".
- PDF p.12: "what looks like a quantum Casimir energy in four dimensions is actually a classical effect in five dimensions".

**Ground-stage READs, carried with their pages:**
- Chamblin–Hawking–Reall PDF p.7, "visible from our domain wall"; pp.2–3, the continuations.
- Emparan–Horowitz–Myers PDF p.2, "can be reached by observers in finite proper time".
- Horowitz–Kolanowski–Santos PDF pp.1 and 3.
- Karasik et al. pp.3 and 6.
- Bronnikov–Kim p.4, eq. (18) and r₀ = 2m.

**standard-not-READ (labelled so, never cited as READ):** the Rácz–Wald theorem; the Raychaudhuri equation; unique continuation in the analytic class; the 5D area theorem; CODATA u(G); Carter's extension; HKS's 5D analysis.

---

## 11. SIM2-PASSAGE.md outline

1. **First headed:** "(computed, READ and deduced; not verified; not seated; 2026-10-09)".
2. **Plain words.**
   - Lemma 0 first.
   - Then: "a horizon that keeps its size and stays still can be crossed only by a pair of null energies that sum to zero on it". The README's positive and an equal negative partner (Lemma S), in the sheet form and in the 179 bulk form.
   - What 177 then has to supply, and that the board cannot compute it.
   - What a changing corridor needs (E-NS, with its number).
   - What position 2's piece does (regularises the past) and does not do (pay the crossing).
   - The answer to 176 in so many words:
     - the object is the extremal, parabolic member of the entangled family;
     - the thermofield-double sign reading of −σ is refuted (Lemma P), the board's own sentence included;
     - if the ends are coupled, the passage needs the exact pair, and MSY's parametric bound says such a coupling exchanges about as much information as it lets through (against 122 (4); not decided);
     - a coupling of the eternal kind would remove the horizon (X19).
   - The [FREE]/[PLANE] split under 179–181.
3. **What you said** (§3).
4. **Setup** (§5).
5. **Results P0–P5**, mapping onto X11–X25, every claim labelled.
6. **Where the computation differs from this spec.**
7. **Verdict** (§6, X25), and §7.
8. **Questions for you.** None blocks the verdict; each has options in M's phrasing plus "For the math":
   - (1) H-PARTNER-IS-THE-COUPLING;
   - (2) 172 (2): coincidence reached at finite advanced time against "(so it never actually touches)";
   - (3) under 179, whether the plane configuration stays as the board's comparison case.
9. **Named hypotheses.**
10. **History.** Include the departure from the judged graft (§0.3), and the X10 (c) note.

---

## 12. Pitfalls

1. **Do not renumber X1–X10.** Supersede X10 (c) by a note. Tag every new section [FREE] or [PLANE] (179–181).
2. **Do not use the smooth-horizon identity as the crossing ledger.** Its premise fails wherever T(k,k) ≠ 0 (Lemma K). Keep its identities as C15 and C16 only.
3. **Lemma S needs stationarity during the crossing.** Stage 5 F1's quasi-static inflow (E/T ≈ 5×10⁻⁶ m per clock) is small, but 162 forbids any growth. The pair must be exact to the order at which the corridor is held fixed.
4. **The partner must be on the README's own sheet** (K(ξ,ξ) belongs to the sheet), or in the bulk along the bulk horizon in the 179 form. A bulk Weyl term changes no surface flux.
5. **Transport identity:** use the covariant derivative along a parallel unit normal. The coordinate derivative of a component is wrong (C16 shows the 2a_v²/a² residual).
6. **Israel conventions:** the normal points into the kept side (the slab, for P2). C20 has three mutations.
7. **Banned substrings in keys** ("time", "clock", "length" and the rest) and in arguments ("d", "gap" and the rest). Use `dep` and `hold_`.
8. **Footprint:** use the bank's `ys_stable` flag only. Unstable columns are UNDECIDED.
9. **Cap:** zeroth-order NEC is not NEC. The cap is held, not a passage. Off the throat it is UNDECIDED (E-DIR). At m/4 the tip bracket must widen adaptively.
10. **The flat limit is a limit with no RS localisation.** It is never the headline. Every ℓ is reported. Never write "k → 0 selected" (140).
11. **MQ's "exactly AdS2" sentence is not evidence about the 5D bulk.** "π to go across" is MQ's statement about their own wormhole. Any global-time quantity is a causal separation, never a transit time.
12. **MSY's and GJW's bounds are parametric.** Never print a number of channels or bits as a supply.
13. **Lemma P and frames:** boost parameters are observers' parameters, never a speed of anything the device sees. Never print a pair total of zero as "positive".
14. **HKS:** the cap's static mode u^{2λ\*} = u^{3.26} at 4m is C² but not C⁴ (finite curvature). Name E-AN; do not close it.
15. **A massive README** adds π-type O(T²/ν²) terms (named). The README is null dust by H-README-AS-NULL-DUST.
16. **Budgets** in clocks are hold lengths for the cone premise, not transit times. Depths are locations. Length is in bits (155 (2)).
17. **Owner columns are heavy.** Use 3 processes and bank them. The selftest runs one column.

---

## 13. Scratch evidence and departures from the designs and judgments

**Spec checks**, all in `/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/epass/spec/`. All are scratch, not board evidence:
- `dbeta.py` with `dbeta.json`: the band, d₊ and d0 at 13 values of ℓ.
- `qdplus.py`: q(d₊)ℓ.
- `lemmaA_ids.py`: Gauss (READ form) and transport identities, with their mutations.
- `cap.py` with `cap.json`: t\*, q\* and the stresses at six values of ℓ.
- `cr4.py`: the cap's O(x) correction at 4m, giving c_r = −0.627731, μ\* = 1.653471 and c₁z = 3.2852.
- `maps.py`: so(2,1) classes, the Poincaré map, the BK patches, the conformal-layer Bianchi.
- `lemmaS.py`: Lemma S (sheet form) and the tangent-geodesic deflection.
- `lemmaS5.py`: Lemma S (bulk identity).

**Departures.**
1. Design 4's Lemma A is replaced as the crossing ledger by Lemmas S, K, L and Q. Its O-C and its B_start budget are withdrawn (§0.3).
2. The judges' inequality is kept, as Lemma Q, now applied to changing crossings.
3. Design 1's cap is kept as a held configuration only.
4. Design 2's Lemma X, far gate and pure-tension point are kept. Its G4 is dropped.
5. Design 3's KR controls, patch map, conformal-layer exclusion and far-time refutation are kept. Its δ-scan is dropped.
6. Design 4's Lemma P is kept, plus design 2's generator-class test.
7. KR's ref. [16] is confirmed to be KLR 0705.4214, which is READ.
8. Items 179–181 are taken into account.

**The new deduction here (Lemma S, and Lemma K's consequence) is unverified.** The verifiers should attack it first.