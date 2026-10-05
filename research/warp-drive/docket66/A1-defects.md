# DOCKET 66 · A1-defects: H-DEFECT-SEAT tested alone

**Seated since (R-apply note, 2026-10-04).** DOCKET 66 wave 1 has been seated at D66-seat: `ledger.py` section 8 and O9's DOCKET 66 answer, `LEDGER.md` regenerated, a comment in `index3.py` and no index3 row. The status line below was written at D66-fix, when nothing here was seated and `ledger.py`, `index3.py`, `specthm.py`, `LEDGER.md`, `paper/` and `docket68/` were untouched; it is kept as written, as history. M's ruling on spec.py's TURN (M-RULINGS item 27, "Any crossing") is applied here at R-apply: section 0 (R-apply) below.

**Status: a docket work item, wave 1, step 1 (2026-10-04), corrected at D66-fix the same day.** Nothing here is
seated. `ledger.py`, `index3.py`, `specthm.py`, `LEDGER.md`, `paper/` and `docket68/` are untouched. The instrument
is `defects.py`, beside this file. `PYTHONDONTWRITEBYTECODE=1 python3 defects.py --selftest` runs **89 counted checks
and passes all 89** in about 33 s (mostly the owners' import of `ledger.py`); **27 of them are controls** (a mutation, a
wrong coefficient, a wrong sign or a non-defect source, each of which must turn its check red); **1 item is
STRUCTURAL** (cannot fail by construction) and is printed, not counted. `python3 defects.py --json PATH` writes the
report, including `a1_grades()` (the grade table below, built from the computations) and `HISTORY` (what wave 1 first
said). Wave 1 ran 71 checks with 19 controls.

## 0 (R-apply, 2026-10-04): M's ruling on TURN, and the D66-repro residuals

**M-RULINGS item 27, verbatim** (docket68/M-RULINGS-2026-10-03.md): *"spec.py's TURN. Asked whether TURN means a genuine
conjugate point or any crossing of light paths, M: "Any crossing". H-TURN-CROSSING is adopted; the straight cosmic string
TURNs (rays cross without focusing)."* Applied in `defects.py` exactly as worded:

| site | D66-fix said | now | ground |
|---|---|---|---|
| the straight string's turn (`SEAT_GRADES`, `a1_grades`) | a TURN under H-TURN-CROSSING, none under H-TURN-CONJUGATE; the reading M's to rule | **a TURN** (H-TURN-CROSSING adopted): rays on opposite sides cross at L = b/tan(4 pi G mu), **2,467 AU at b = R_sun** and the Planck NG bound (the Sun's own focus: 548 AU); no conjugate point, so none under H-TURN-CONJUGATE, **kept as the alternative on record** | `string_turn` (new): the crossing from `string_crossing`, cross-checked as the two deflected rays' line intersection (agree to 1e-12); `turn_under` (new) grades either reading; `TURN_RULING` (new) records the ruling; `HISTORY` keeps D66-fix's words |
| the global monopole | a TURN under both | unchanged: a TURN under both (its axis recrossings are conjugate points) | `monopole_conjugate` |
| H-TURN-CONJUGATE, H-TURN-CROSSING (`HYPOTHESES`) | the two readings, named | unchanged as definitions; the ruling is recorded beside them (`TURN_RULING`), not by rewriting either | — |

**Does any specthm / spec class verdict move? No, and the reason is computed, not declared.** specthm's seat classes are
defined by the literals `wl` and `ball` alone (S-1 `wl`; S-2 `ball`; S-3 neither); no literal, and no feature text, names a
turn, a crossing or a conjugate point; and specthm's `derive` makes NONEMPTY only for S-1 (its witness rule). The string
stays in S-3, whose verdict is OPEN with or without a crossing TURN; S-1 stays NONEMPTY (the Sun), S-2 OPEN. A selftest
check asks this of specthm's source at run time, with a planted-literal control. What the ruling does change is the
string's PART 2: under M's reading a string seat has a TURN at a computed range (L linear in b) -- a candidate S-3 seat's
second part, not a class verdict. `spec.py`'s PART 2 still reads "a conjugate point"; it is not this docket's file to
edit unless TURN were a constant there (it is docstring text, no constant or check reads it), and the line is reported
for its owner.

**Selftest:** `PYTHONDONTWRITEBYTECODE=1 python3 defects.py --selftest` now runs **95 counted checks and passes all 95**,
**30 of them controls**, 1 STRUCTURAL not counted (D66-fix: 89, 27 controls). The six new: M-RULINGS item 27 read at run
time and `TURN_RULING` matching it; the string TURNs under the adopted reading (and not under the alternative); CONTROL
G mu = 0 gives no crossing, so no TURN; CONTROL a class with a conjugate point TURNs under H-TURN-CONJUGATE too; no
specthm class literal names a turn and only S-1 can be NONEMPTY; CONTROL a planted S literal 'turn' is caught.

**D66-repro residuals here** (`wave1/FIX-SEAT-RESULT.json`, `result.v`), each applied: the docstring's item 5 said "the
literature's precise sense of ..." -- now "a counterpart ... under a named reading (H-YUKAWA, H-FORM-IS-MASS-AND-DIMENSION)"
(V66-0 #3), first wording kept in place; the CGS reading note now cites the source itself -- CGS Appendix A, eqs.(A.12)-(A.13)
(printed p.21), gives the transformation with conformal factor e^(+-2 beta z), and p.8 writes the M4 side as A = e^(+2 beta z)
(READ via alphaXiv, open arXiv PDF gr-qc/9306005v1, by D66-repro and again here): the 2 is the source's, so eq.(3.48)'s
printed exponent is the source's slip, not an extraction loss. The code was right and is unchanged.

## D66-fix: what the three verifier reports found here, and what was done

Each item was applied or answered with a computed or READ reason. Wave 1's words are kept in `defects.HISTORY`.

| verifier item | wave 1 first said | now | ground |
|---|---|---|---|
| V66-1 #1 (grade-moving) | the string-supported throat's O-MAKE-TOPO "binds if made from flat space"; whether M's singular-throat admission is a board ruling was left "for M" | **O-MAKE-TOPO OPEN via N_WNCC.** M has ruled: ledger M-S1A-P3 reads "APPLIED at the seat; a singular throat is not disqualified" with the consequence "the throat-creation classes stay OPEN". Geroch/Borde's pathology sits at the throat, which the ruling admits; specthm's W-create-ncc is OPEN at its owner, not shown realisable | `grades()` new z3 item with mutation controls `ruling-dropped` and `wncc-asserted`; the ledger text is read at run time |
| V66-1 #3 (grade-moving) | the wall seat's CTC/Borde status OPEN (VIS causal structure "not computed"); O-LOOP OPEN | **PASSES under H-VIS-MINKOWSKI; O-LOOP none.** Each side of the M4-M4 wall is Minkowski, Minkowski T is a global time function | `vis_time_function` (sympy): the pullback is exact on both sides, g^(mu nu) dT dT = -1, T continuous at the wall, kappa sigma = 4 beta from the Israel jump; CGS p.15 and Fig.4 READ; controls: R is spacelike, and the conformal factor as printed fails the pullback |
| V66-1 #4 (grade-moving) | the global monopole's rays "cross but do not focus": a turn under H-TURN-CROSSING, none under H-TURN-CONJUGATE | **a TURN under both readings.** Every recrossing of the source-centre axis is a conjugate point (a line caustic) | `monopole_conjugate`: the out-of-plane Jacobi field (sectional curvature b^2(1-A)/(A r^4)) first vanishes at the axis crossing, to 1e-11 relative; controls: curvature halved misses it, A = 1 has none |
| V66-1 #5 (grade-moving) | gauge monopole lensing seat "not computed (OPEN)"; specthm class "S-3 (or S-1 ...)" | **S-1 IF {H-MONOPOLE-MASS, H-WEAK-FIELD, H-S1-VACUUM}.** A 1 AU focus at b = 2.81e-13 m for M = 1e17 GeV/c^2; b / r_core = 3.6e18, b / r_s = 1.1e24, the field energy beyond b is 1.2e-19 of Mc^2 | `gauge_monopole_lens` through `spec.focal_length`; the scan 1e15 .. 1e19 GeV holds; control: a 1e-27 kg "monopole" fails |
| V66-0 #2 | N_DEFB: "direction, rate and feedstock computed nowhere" | **the direction is READ: wash-out.** HK eq.(4.33) p.64: an existing asymmetry "can relax to zero via scattering off strings". Emission needs CP violation and a departure from thermal equilibrium (HK p.65). N_DEFB is OPEN only IF {CP-violating core couplings, departure from equilibrium}; feedstock leptons; rate not computed. READ for GUT strings and gauge monopoles; for walls and global monopoles not READ, OPEN as unchecked | HK pp.63-65 re-read at D66-fix (alphaXiv) |
| V66-0 #3 | F1: zero modes are an "exact counterpart"; SUPPORTED | **a counterpart under a named reading: SUPPORTED-IF {H-YUKAWA, H-FORM-IS-MASS-AND-DIMENSION}.** HK pp.33-34 say only that the mass vanishes at the core and the modes move at c; the mapping to "geometric form" is this file's | wording |
| V66-2 #1 | global monopole deficit "Delta = 8 pi eta^2/(1 + 8 pi eta^2)", labelled EXACT | **Delta = 8 pi G eta^2 exactly outside the core** (Barriola-Vilenkin). Wave 1 equated the cone metric's rho with the flat-space hedgehog density; in the cone metric the gradient energy is eta^2/(A r^2) | `hedgehog_curved`, `monopole_deficit`; control: wave 1's input gives the other value. The Sturm verdict and the deflection eps*pi are unchanged |
| V66-2 #2 | a Gott pair "cannot form in an open universe" | cannot be **created in an open (2+1)-dimensional universe with timelike total momentum** (CFG94) | wording |
| V66-2 #3 | "DISQUALIFIED inside r < S/alpha unless S < kappa" | with dislocation kappa: CTCs iff S > kappa, in **r < sqrt(S^2 - kappa^2)/alpha**; r < S/alpha only for kappa = 0 (DLM04 eqs.(2)-(3)) | wording (the checks already carried both forms) |
| V66-2 #7 | "the GV ring's curvature singularity is at the throat" | a singular ring bounding the throat disc: **conical only at sigma = 0** (the figures' tension, T = -c^4/(4G)); conical plus power-law at sigma != 0 (GV pp.20-22, re-read) | wording; the M-S1A-P3 (i) reading is unaffected |
| (follows from #4, #5) | F4: the wall is "the only class that gives light a genuine focal point" | the wall is the only class that focuses a whole **planar** congruence at one distance; the global monopole (line caustic) and the gauge monopole (S-1 point lens) also give conjugate points; **only the string is crossing-only** | — |

## M's words, verbatim (read at run time from `ledger.RULED_BY_M`, row M-S1A-P3)

> Seating occurs in a place where matter can occur but not in its original geometric form

Carried as **H-DEFECT-SEAT** (docket66/CHARTER.md). M's clarification of reading (i), also on that row: *"My ruling
refers to the seat/destination. Singular occurs in the throat where the geometry is compressed to binary information,
and then push to the seat"* -- so the seat must be free of a closed causal curve and of a Borde pathology, and a
singular throat is not disqualified. The row's consequence reads: *"the throat-creation classes stay OPEN"*. Both are
applied below: the seat condition at the seat only, and the singular-throat admission to the throat's creation.

## The answer, first

1. **M's phrase has a counterpart in the literature under a named reading.** Where a fermion gets its mass from a
   Yukawa coupling to the defect's order parameter (**H-YUKAWA**), that mass *vanishes at the core*: matter occurs
   there as massless modes confined to the defect -- chiral 1+1-dimensional modes moving at c along a string,
   2+1-dimensional modes on a wall, a bound zero mode on a monopole (Hindmarsh & Kibble p.33-34; Eto & Suzuki p.15-16,
   p.22, App. A; READ). `defects.py` computes the Jackiw-Rebbi profile cosh(x)^-1, finds it normalisable with the mass
   exactly 0 at the core, and finds the opposite coupling sign non-normalisable (the control). The zero modes' group
   velocity is exactly 1 (c), never more. The sources say nothing about "geometric form"; reading it as rest mass and
   dimensionality is this file's mapping, named **H-FORM-IS-MASS-AND-DIMENSION**. **Graded: SUPPORTED-IF {H-YUKAWA,
   H-FORM-IS-MASS-AND-DIMENSION}, for strings, walls and monopoles.** The literature gives the phenomenon; it does not
   give a seat.
2. **As seats, the static string, the thin wall, the global monopole and the gauge monopole pass M-S1A-P3 (i).** The
   string and the monopoles are static metrics with g^tt < 0, so t is a time function (computed). **The wall** (the
   non-extreme Vilenkin-Ipser-Sikivie wall with Lambda = 0 on both sides) is not static, but each side is Minkowski and
   Minkowski T is a global time function across it (`vis_time_function`; CGS p.15, Fig.4): **PASSES under
   H-VIS-MINKOWSKI** (no identification made; CTCs in CGS arise only by identification across AdS Cauchy horizons,
   p.14). None changes the spatial topology, so Geroch/Borde have no premise at the seat
   (`create.is_topology_change(False, False)` is False). **A spinning string with dislocation kappa is DISQUALIFIED
   where S > kappa, inside r < sqrt(S^2 - kappa^2)/alpha** (r < S/alpha when kappa = 0; De Lorenci & Moreira eqs.(2)-(3),
   READ; recomputed). A **Gott pair** carries CTCs but needs gamma > 5.3e5 at the Planck bound and cannot be created in
   an open (2+1)-dimensional universe with timelike total momentum (Carroll, Farhi, Guth & Olum, READ). The **texture**
   is a spacetime *event* (Durrer Table 1) that collapses (Derrick, computed): **EMPTY IF {H-SEAT-PERSISTS}** as a seat.
3. **Sturm never certifies a defect seat -- and in every class the certificate lies past the class's own gravitational
   limit.** Sturm's sufficient condition, in the form `specthm.py` states it (4 pi G T_kk s^2/c^4 >= pi^2, read from its
   source at run time), needs: in a string core (H-UNIFORM-CORE) mu >= pi^2/16 (or pi^2/32), against the cone closing
   at G mu = 1/4; for a global monopole eps >= pi^2/2 = 4.93, against eps < 1; for a gauge monopole Q/b >= pi, i.e.
   2 M_out/b >= pi^2 > 1 (inside its own gravitational radius); for a thick wall a thickness of at least pi^2/2 = 4.93
   of its own de Sitter radii; outside a string core T_kk = 0. This parallels `spec.py`'s 2 pi^2/3 for the ball (S-2).
   Since Sturm is *sufficient*, its failure does not refute seating; it means no defect is certified by that route.
4. **The defects' turns.** Only the string is crossing-only.
   - **String:** turns every ray by 4 pi G mu *independently of impact parameter* (HK p.90): two rays on opposite
     sides cross at L = b/tan(4 pi G mu), linear in b. Neighbouring rays on one side see a flat cone (J'' = 0), so there
     is no conjugate point (at b = R_sun and the Planck bound, L = 2,467 AU against the Sun's 548 AU from
     `spec.focal_length`). **A TURN: M ruled TURN = "Any crossing" (M-RULINGS item 27), so H-TURN-CROSSING is
     adopted**; none under H-TURN-CONJUGATE, kept as the alternative on record (`string_turn`). *D66-fix first said "A
     TURN under H-TURN-CROSSING, none under H-TURN-CONJUGATE", the reading M's to rule.*
   - **Global monopole:** deflects by eps*pi for every b (Durrer eq.38), and every recrossing of the source-centre
     axis is a **conjugate point**: the rotation Killing field about that axis is a Jacobi field vanishing at the source
     and on the axis (`monopole_conjugate`). A line caustic (an axicon). A TURN under **both** readings. *Wave 1 first
     said none under H-TURN-CONJUGATE.*
   - **Gauge monopole:** an S-1 point lens (item 5 of section 1), with conjugate points on the axis as for the Sun.
   - **Wall:** violates the SEC (repulsive to matter at rest, R_uu = -4 pi G sigma) yet focuses null rays that cross
     it (R_kk = +8 pi G sigma); the Raychaudhuri equation gives a genuine caustic of a whole planar congruence at
     f = c^4/(4 pi G sigma) = 1/(2 beta), half the wall's own de Sitter radius (computed; the negative-tension control
     has none). A 1 AU focus would need sigma = 6.4e31 J/m^2.
5. **Against D68's obstructions:**

   | obstruction | H-DEFECT-SEAT: the defect at the seat | a defect as the throat's support (the wormhole literature) |
   |---|---|---|
   | **O-SEAT** (supply at the seat) | **OPEN via N_S5 \| N_DEFB** -- no defect supplies the payload in any source read. N_DEFB (a B-violating core) is READ with its direction: **wash-out** (HK eq.(4.33) p.64), a supply only IF {CP-violating core couplings, departure from equilibrium} (HK p.65); feedstock leptons, rate not computed; for walls and global monopoles not READ (OPEN as unchecked). The board's grade (`docket68/seat.grade_o_seat` = OPEN) is not moved | -- |
   | **O-HOLD** (holding the throat) | **LEAVES** (the seat is not the throat; the board's grade stands) | **LEFT given H-CANONICAL**: every canonical scalar + gauge field satisfies the NEC pointwise (computed: T_kk is a sum of squares), so topological censorship (FSW Thm 1, READ) binds. **OPEN via N_NEGT** outside it: the flat ring/polyhedral wormholes need strings of *negative* tension, T = -c^4/(4G) (Gibbons & Volkov; Visser 1989; READ and recomputed) -- and "no natural mechanism ... is currently known" (Visser p.5). A string's *quantum* fluctuations give a transient opening only, "exponentially fragile", transit d + logs (Fu, Grado-White & Marolf, READ): not a hold. Never REMOVED |
   | **O-LOOP** (time loops) | static seats and the wall: none (computed; the wall through its global time function); spinning string: CTCs where S > kappa (disqualified at a seat) | ring-wormhole mouths in one space with unequal surrounding mass become a time machine after T ~ R L c/(G M) (Frolov, Krtous & Zelnikov eq.6.9, READ; 1.4e9 yr for an Earth-mass shell, L = 1 ly) -- **O-LOOP reintroduced**, and the seat mouth lies on the loop |
   | **O-MAKE-TOPO** | LEAVES (no topology change at a defect seat) | **OPEN via N_WNCC.** A ring wormhole *made* from flat space is a topology change (`create.is_topology_change(False, True)`); Geroch needs no matter assumption, and Gannon makes a non-simply-connected Cauchy surface singular under the WEC (FKZ p.1; FSW p.2). The pathology they force sits at the throat, which M has ruled not disqualifying, and the throat-creation classes stay OPEN (ledger M-S1A-P3); specthm's W-create-ncc is OPEN at its owner, not shown realisable. *Wave 1 first said "binds".* |
   | **O-MAKE-DIST** | LEAVES | LEAVES |
   | **O-BITS** | LEAVES: zero modes travel at exactly c; the cone shortens a path across a string by 1 - cos(Delta/4) = 4.4e-13 at the Planck bound, relative to flat space only -- in the string's own geometry light is still fastest | LEAVES; FGM: wormholes cannot be the fastest causal curves |

   A defect *made* at the seat is a preparation in advance, so it needs a prior arrival at <= c (D23, asked of the
   ledger through `massform.preparation_needs_prior_arrival()` = True).
6. **Under H-SM-ONLY there is no stable defect seat at all.** The electroweak vacuum manifold is S^3: simply connected
   (no topological string, HK p.36), with pi_2 = 0 (no monopole, Durrer p.4) and connected (no wall); its Z-strings are
   unstable at the physical Weinberg angle (HK p.26); pi_3 = Z gives only textures, which are unstable events. Every
   stable defect seat needs fields beyond the Standard Model: **OPEN** there. And even at an electroweak core, only the
   Higgs share of the payload's mass would change form -- at most 0.172 on the largest READ first-order reading
   (`massform.HIGGS_SHARE_LARGEST_READ`); the rest is QCD mass that keeps its original form.
7. **A connection to S13, recorded, not claimed as a route.** DOCKET 65's held-seat release route holds |phi| below v
   with a prepared source, stable only on 0.5774 v < |phi| < v (`massform.STABLE_RANGE`, `excite.stability_edge` =
   1 - 1/sqrt 3). A defect core holds the order parameter at 0 *with no source*, by topology. But the same topology
   forbids a local release: the hold ends only by annihilating the defect, releasing its rest energy (mu c^2 =
   1.8e37 J per metre of string at the Planck bound), and the S13 route's H-RELEASE (release without work) cannot
   apply to it. Not computed further; carried as a finding for the combination step.

**Overall grade of H-DEFECT-SEAT, alone:** the phrase is SUPPORTED-IF {H-YUKAWA, H-FORM-IS-MASS-AND-DIMENSION}; static
string and monopole seats, and the wall seat under H-VIS-MINKOWSKI, pass the seat's causality condition; the string,
wall and global monopole land in specthm's S-3 and the gauge monopole in S-1 under named hypotheses; Sturm never
certifies one; every class but the string gives a conjugate point; **it removes no obstruction**: O-SEAT stays OPEN
(N_DEFB named, its READ direction wash-out), O-HOLD is LEFT for canonical defects and OPEN via N_NEGT for
negative-tension ones, O-MAKE-TOPO for a made string-supported throat is OPEN via N_WNCC under M's ruling, and no route
arrives faster than light. Not retired: a failure alone does not retire a hypothesis (docket68/CHARTER.md, M's standing
instruction), and the combinations are step 3.

## 1. What was computed (all in `defects.py`, each with its owner or source)

**Stress tensors and energy conditions** (orthonormal frame, outside the core, **H-THIN**), exact:

| class | (rho; p1, p2, p3) / scale | NEC | WEC | SEC (rho + sum p) | DEC | source of the row |
|---|---|---|---|---|---|---|
| string (axis 3) | (1; 0, 0, -1) mu | SAT, SAT, SATURATED | SAT | SATURATED (0) | BOUNDARY | HK eq.(4.1) |
| wall (normal 1) | (1; 0, -1, -1) sigma | SAT, SATURATED, SATURATED | SAT | **VIOLATED (-1)** | BOUNDARY | CGS eqs.(2.18)-(2.19) |
| global monopole | (1; -1, 0, 0) eta^2/r^2 (flat); eta^2/(A r^2) in the cone metric | SATURATED, SAT, SAT | SAT | SATURATED (0) | BOUNDARY | sigma model on the hedgehog, computed (`hedgehog_stress`, `hedgehog_curved`) |
| gauge monopole (exterior) | (1; -1, 1, 1) u | SATURATED, SAT, SAT | SAT | SAT (2) | BOUNDARY | radial Maxwell stress, computed |
| *control*: negative-tension string | (-1; 0, 0, 1) | **VIOLATED** | VIOLATED | VIOLATED | VIOLATED | Visser 1989; GV17 |

NEC per axis equals the full null-cone minimum (checked independently on the sphere); WEC is the infimum of T_uu
over observers (checked on a grid to v = 0.999); DEC "BOUNDARY" means rho = |p_i| -- every observer's energy flux is
timelike and turns null only as v -> c. **The texture** is a canonical sigma-model field: its NEC holds by the theorem
below, and it is graded through Derrick.

**The canonical-field NEC theorem**, computed: for two scalars with any potential V and a Maxwell field, every
derivative and field strength a free symbol, T_kk along k = (1,0,0,1) is (d_0 phi + d_3 phi)^2 summed + (E_x - B_y)^2 +
(E_y + B_x)^2, a sum of squares, with V dropping out. Control: a phantom scalar gives T_kk = -1 at d0_0 = 1.
**Named limit:** classical, minimally coupled, positive kinetic terms (**H-CANONICAL**); quantum expectation values
are outside it (that is where FGM's negative null energy lives).

**Geometry.**
- String: the linearised field HK eq.(4.3) gives the deficit 8 pi G mu (**H-LINEAR-GRAV**); with tension T, deficit
  4 pi G (mu + T) and potential 4 G (mu - T) ln R (HK eq.(4.6)) -- the canonical string (T = mu) has no Newtonian force
  (HK p.84); the control T = 0 has. HK's printed 5.18 arcsec and 1.35e21 kg/m at G mu = 1e-6 are reproduced (5.1840;
  1.3466e21 with `spec.G_SI`, `spec.C_SI`), and 4 pi G mu does not reproduce them.
- Global monopole: the exact Einstein tensor of dr^2 + A r^2 dOmega^2 gives rho = (1 - A)/(8 pi A r^2), p_r = -rho,
  p_t = 0. The hedgehog's own stress **in that metric** is (eta^2/(A r^2); -eta^2/(A r^2), 0, 0) (`hedgehog_curved`),
  the same form, and equating the two gives **Delta = 1 - A = 8 pi G eta^2 exactly** outside the core
  (Barriola-Vilenkin; `monopole_deficit`). *Wave 1 equated the geometric rho with the flat-space density eta^2/r^2 and
  printed Delta = 8 pi eta^2/(1 + 8 pi eta^2) as EXACT; that input is inconsistent, and the selftest keeps it as a
  control that gives the other value.*
- Global monopole conjugate points (`monopole_conjugate`): a ray from a source on the axis lies in a plane through
  the axis; unrolled, that plane is a cone of total angle 2 pi sqrt(A), on which the ray is straight. The out-of-plane
  Jacobi field obeys J'' + K J = 0 with K = b^2 (1 - A)/(A r^4) (K_radial = 0, K_tangential = (1 - A)/(A r^2)). From
  J(0) = 0 its first zero is the far-axis crossing: at A = 0.9, D = 10, b = 1 both lie at s = 26.30987 (relative
  difference 6e-12); at A = 0.999, D = 1e3, the same to 3e-12. Controls: the curvature halved misses the crossing, and
  A = 1 has neither.
- Wall: R_uu = -4 pi sigma delta, R_kk = +8 pi sigma delta (crossing), 0 along the wall; Tolman mass per area
  sigma - 2 tau = -sigma (CGS p.12); beta = 2 pi G sigma/c^4 from CGS's kappa sigma = 4 beta.
- **Wall, global structure** (`vis_time_function`, D66-fix): on each side the comoving metric
  e^(-2 beta |z|) (-dt^2 + dz^2 + beta^-2 cosh^2(beta t) dOmega^2) is the pullback of Minkowski under CGS's own map
  T = beta^-1 e^(-beta|z|) sinh(beta t), R = beta^-1 e^(-beta|z|) cosh(beta t) (CGS p.15); g^(mu nu) dT dT = -1 on both
  sides, T is continuous at the wall and dT/dt = cosh(beta t) > 0 there, and the Israel jump gives S_ij = -sigma h_ij
  with kappa sigma = 4 beta, CGS p.10's relation. A continuous function strictly increasing along every future causal
  curve on each side increases along every future causal curve of the glued spacetime, so there is no closed causal
  curve. *Reading note:* CGS print the conformal factor of eq.(3.48) as e^(-+ beta z), while their own transformation
  maps to Minkowski only with e^(-2 beta |z|); the selftest shows the printed form failing the pullback. CGS's own
  Appendix A settles it: eqs.(A.12)-(A.13) (printed p.21) give the same transformation with e^(+-2 beta z), and p.8 writes
  the M4 side as A = e^(+2 beta z) (READ via alphaXiv, open arXiv PDF, by D66-repro and again at R-apply). *D66-fix first
  said: "Recorded as a reading note, not a finding against CGS (an extraction may have dropped a 2)."*
- Texture: Derrick's dE/dlambda = I1 + 3 I2 > 0 in d = 3 (z3: no stationary point), while d = 1 admits one (the
  control: walls exist).
- Gauge monopole lens (`gauge_monopole_lens`): spec.focal_length inverted for a 1 AU focus and checked by calling it.
  At M = 1e17 GeV/c^2 (**H-MONOPOLE-MASS**: core radius (1/alpha_GUT) hbar/(M c) with alpha_GUT = 1/40; Dirac charge
  h/e), b = 2.81e-13 m, r_s = 2.6e-37 m, r_core = 7.9e-32 m, and the magnetic field energy beyond b is 1.2e-19 of Mc^2.
  So S-1's weak-field point-lens formula applies (**H-WEAK-FIELD**) and the "through vacuum" literal holds to 1e-19
  (**H-S1-VACUUM**). The scan 1e15 .. 1e19 GeV keeps all three; the control (1e-27 kg) fails them.

**Figures** (each recomputed): Planck NG bound G mu < 1.5e-7 (95%, Planck+WP; 1.3e-7 with high-l; AH 3.2e-7): deficit
3.77e-6 rad, mu = 2.02e20 kg/m, mu c^2 = 1.82e37 J/m. String crossing at b = 1 m: 5.3e5 m; at b = 1 AU: 8.39 ly.
Gott: gamma > 5.305e5 (1 - v < 1.8e-12). GV ring: |T| = c^4/(4G) = 3.0256e43 N (printed 3.0257e43); a 1 m ring needs
2.115e27 kg-equivalent, 1.11 Jupiter masses (Jupiter from `spec.LENSES`). Visser cube edge c^4/(8G) = 1.513e43 J/m
(printed 1.52e43); c^4/(4 pi G) does not reproduce it.

## 2. The z3 bookkeeping

`grades()` encodes, as constraints: a held traversable throat needs NEC violation (FSW Thm 1; GV p.3; Visser p.4);
H-CANONICAL forbids NEC violation (the theorem above); in this screen the only NEC-violating source is a negative
tension, possible only through N_NEGT; O-SEAT is removed only by a supply shown through N_S5 (board) or N_DEFB; the
seat condition forbids a CTC and a topology change at the seat; static means CTC-free; inside a spinning string's
radius means CTC. **D66-fix adds the throat's creation:** a made throat is a topology change, Geroch/Borde force a
pathology at the throat, M's ruling lets that pathology stand at the throat, and a made throat is realised only through
N_WNCC (specthm's W-create-ncc). Vacuity: the board is SAT, and canonical-without-throat is SAT. Verdicts (checked):
O-HOLD given H-CANONICAL **LEFT**; outside it **OPEN via N_NEGT**; O-SEAT **OPEN via N_S5 | N_DEFB**; O-MAKE-TOPO for a
made string-supported throat **OPEN via N_WNCC**; static seats **PASS**; inside a spinning string's CTC radius
**DISQUALIFIED**. Six mutation controls each move a verdict and are caught (`drop-FSW`, `neg-asserted`,
`defb-asserted`, `spin-ok`, and D66-fix's `ruling-dropped` and `wncc-asserted`). STRUCTURAL, not counted: OPEN pathways
are free atoms, so "OPEN via" is their encoding. The screen is bookkeeping over findings owned elsewhere, not new
physics, and only as good as its encoding.

## 3. Findings (recorded, not repaired)

- **F1 (FOR M).** "Matter can occur but not in its original geometric form" has a literature counterpart -- zero modes
  at defect cores -- for all three persistent classes, on H-YUKAWA and under the named reading
  H-FORM-IS-MASS-AND-DIMENSION. A grader who said the phrase had no sense in the literature would under-represent it;
  one who called it an exact counterpart would over-represent it (*wave 1 first said "exact"*).
- **F2 (AGAINST M).** No source read gives a defect that *supplies* matter at a seat; the phenomenon is a change of
  form of matter already there. And the one B-violating mechanism read runs the other way: its READ direction is
  wash-out (HK eq.(4.33)), so a supply needs CP violation and a departure from equilibrium (HK p.65). O-SEAT does not
  move.
- **F3.** In every class Sturm's certificate lies past the class's own gravitational limit (cone closing, solid angle
  exhausted, trapping, thicker than its own horizon) -- the same shape as `spec.py`'s 2 pi^2/3 for the ball.
- **F4.** The wall is the one class that focuses a whole planar congruence of light at one distance, while being
  repulsive to matter at rest -- an SEC-violating, NEC-respecting lens -- and its seat passes M-S1A-P3 (i) under
  H-VIS-MINKOWSKI. The global monopole (a line caustic) and the gauge monopole (an S-1 point lens) also give conjugate
  points; only the string is crossing-only. *Wave 1 first said the wall was "the only class that gives light a genuine
  focal point" and that its causal structure was OPEN.*
- **F5.** The board's PART 2 "TURN" was never fixed as conjugate point versus crossing. After D66-fix the readings
  split only on the string (crossing, no conjugate point); the global monopole turns under both. **M has ruled "Any
  crossing" (M-RULINGS item 27): H-TURN-CROSSING is adopted and the straight string TURNs, at L = b/tan(4 pi G mu);
  H-TURN-CONJUGATE is kept as the alternative on record. No specthm class verdict moves (section 0 (R-apply)).** *D66-fix
  first said: "Named both ways (H-TURN-CONJUGATE, H-TURN-CROSSING); M's to rule if it matters for the string."*
- **F6.** Every string-supported traversable throat in the sources read needs a negative tension (or a quantum,
  transient, fragile opening). With both mouths in one space and unequal surrounding mass it becomes a time machine
  (FKZ), so the seat mouth would carry a CTC -- excluded at the seat by M-S1A-P3 (i) unless the masses balance. Under
  M-S1A-P3 the GV ring -- conical only at the figures' tension, conical and power-law at sigma != 0 -- is at the throat
  and not itself disqualifying, and the throat's creation is OPEN via N_WNCC.
- **F7.** Under H-SM-ONLY no stable defect exists; and at an electroweak core at most the Higgs share (<= 0.172, first
  order, massform) of the payload changes form.
- **F8 (route record).** arXiv hep-th/0001128, tried as Rubakov & Shaposhnikov 1983 ("Do we live inside a domain
  wall?"), is an unrelated paper. R-S 1983 is NOT READ; the wall zero mode rests on Eto & Suzuki (and their refs to
  Jackiw-Rebbi 1976 / Jackiw-Rossi 1981, CITED there, not read) and on the computation.

## 4. Named hypotheses

H-DEFECT-SEAT (M's, under test); H-CANONICAL; H-THIN; H-LINEAR-GRAV; H-UNIFORM-CORE; H-SM-ONLY; H-SEAT-PERSISTS;
H-TURN-CONJUGATE; H-TURN-CROSSING; H-YUKAWA; H-STATIC-STRING; and from D66-fix H-FORM-IS-MASS-AND-DIMENSION,
H-VIS-MINKOWSKI, H-MONOPOLE-MASS, H-WEAK-FIELD, H-S1-VACUUM. OPEN pathways N_NEGT, N_DEFB and N_WNCC (specthm's
W-create-ncc), and the board's N_S5. Each is stated in `defects.HYPOTHESES`.

## 5. Open

- N_DEFB: whether a B-violating core can supply baryons. The direction is READ (wash-out); a supply needs CP violation
  and a departure from equilibrium (HK p.65); the rate is computed nowhere; for walls and global monopoles B violation
  is not READ at all.
- N_NEGT: a negative-tension string -- no mechanism known.
- N_WNCC: specthm's W-create-ncc, admitted by M's ruling, not shown realisable.
- Whether a texture "event-seat" means anything on the board (no definition exists): OPEN without H-SEAT-PERSISTS.
- *Closed at R-apply:* the reading of TURN -- M ruled "Any crossing" (item 27); H-TURN-CROSSING adopted, the string
  TURNs. *D66-fix listed it here as "now material for the string only (H-TURN-CONJUGATE vs H-TURN-CROSSING): for M".*
- Walls with an AdS side (CGS's CTCs by identification, p.14) are outside H-VIS-MINKOWSKI and not graded here.
- Combinations (step 3): screened in B-combine66.md.
- Observational bounds on walls and monopoles (Zel'dovich-Kobzarev-Okun; Parker): NAMED, NOT READ.
- *Closed at D66-fix:* the wall's global causal structure (computed); the gauge monopole's lensing seat (computed);
  N_DEFB's direction (READ).

## 6. Sources (READ at source; route recorded; open content only; no paywall or login wall met)

| key | source | route | used |
|---|---|---|---|
| HK | Hindmarsh & Kibble, *Cosmic strings*, arXiv hep-ph/9411342v1 | alphaXiv answer_pdf_queries (full text) | pp.16, 26, 33-34, 36, 53-54, 63, 84-85, 90; **pp.63-65 re-read at D66-fix** (eq.(4.33) wash-out; p.65 Sakharov conditions) |
| DURRER | Durrer, *Global field dynamics ...*, arXiv astro-ph/9411010 | alphaXiv | pp.4, 8-10, 12-13, 18 |
| CGS | Cvetic, Griffies & Soleng, arXiv gr-qc/9306005 | alphaXiv | abstract, pp.2, 6, 10, 12; **pp.14-15 and Fig.4 read at D66-fix** |
| VISSER89 | Visser, *Traversable wormholes: some simple examples*, arXiv 0809.0907 (PRD 39 3182) | alphaXiv | pp.3-6 |
| GV17 | Gibbons & Volkov, *Weyl metrics and wormholes*, arXiv 1701.05533v3 | alphaXiv | pp.3, 20-22 (**re-read at D66-fix**: conical and power-law singularities, sigma = 0 locally flat) |
| FKZ23 | Frolov, Krtous & Zelnikov, *Ring wormholes and time machines*, arXiv 2305.03887 | alphaXiv | pp.1, 5, 17-18 |
| CFG94 | Carroll, Farhi, Guth & Olum, arXiv gr-qc/9404065 | alphaXiv | abstract, pp.2, 4, 10 |
| DLM04 | De Lorenci & Moreira, arXiv gr-qc/0309122v2 | alphaXiv | p.1 eqs.(2)-(3) |
| PLANCK13 | Planck 2013 XXV, arXiv 1303.5085 | alphaXiv | abstract, Tables 2-3 |
| FSW93 | Friedman, Schleich & Witt, *Topological censorship*, arXiv gr-qc/9305017v2 | alphaXiv | pp.2-3 |
| FGM19 | Fu, Grado-White & Marolf, arXiv 1908.03273v2 | alphaXiv | abstract, pp.1-5, 15-17 |
| ETO25 | Eto & Suzuki, arXiv 2506.16765v1 | alphaXiv | pp.1, 15-16, 22, 24-25 |
| gauge monopole attractive | arXiv gr-qc/9506068 | Firecrawl research search (abstract) | abstract (authors not read) |
| thick walls | arXiv gr-qc/9903059 | Firecrawl research search (abstract) | abstract (authors not read) |
| *route error* | arXiv hep-th/0001128 | alphaXiv | not R-S 1983; nothing rests on it |

Copyrighted text stays out of the tree except short phrases with their page. No host refused a request.

## 7. Adversarial notes, both directions

- *Could this over-represent M?* The zero-mode reading is conditional on H-YUKAWA and H-FORM-IS-MASS-AND-DIMENSION and
  gives a change of form, not a supply (F2); N_DEFB's READ direction is wash-out; no class is certified by Sturm; the
  gauge monopole's S-1 placement rests on three named hypotheses; no obstruction is removed.
- *Could this under-represent M?* The static string, the monopoles and the wall (under H-VIS-MINKOWSKI) pass the seat's
  causality condition outright; every class but the string gives a conjugate point; N_NEGT, N_DEFB and N_WNCC are kept
  OPEN, not LEFT; M's singular-throat ruling is applied to the throat's creation as a board ruling, not held back as a
  question; H-SM-ONLY is named, not assumed, so the beyond-SM cases stay OPEN.
