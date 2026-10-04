# DOCKET 66 · A1-defects: H-DEFECT-SEAT tested alone

**Status: a docket work item, wave 1, step 1 (2026-10-04).** Nothing here is seated. `ledger.py`, `index3.py`,
`specthm.py`, `LEDGER.md`, `paper/` and `docket68/` are untouched. The instrument is `defects.py`, beside this file.
`PYTHONDONTWRITEBYTECODE=1 python3 defects.py --selftest` runs **71 counted checks and passes all 71** in about 30 s
(mostly the owners' import of `ledger.py`); **19 of them are controls** (a mutation, a wrong coefficient, a wrong sign
or a non-defect source, each of which must turn its check red); **1 item is STRUCTURAL** (cannot fail by construction)
and is printed, not counted. `python3 defects.py --json PATH` writes the report.

## M's words, verbatim (read at run time from `ledger.RULED_BY_M`, row M-S1A-P3)

> Seating occurs in a place where matter can occur but not in its original geometric form

Carried as **H-DEFECT-SEAT** (docket66/CHARTER.md). M's clarification of reading (i), also on that row: *"My ruling
refers to the seat/destination. Singular occurs in the throat where the geometry is compressed to binary information,
and then push to the seat"* -- so the seat must be free of a closed causal curve and of a Borde pathology, and a
singular throat is not disqualified. Both are applied below, at the seat only.

## The answer, first

1. **M's phrase has a precise meaning in the literature, and it holds -- under a named hypothesis.** Where a
   fermion gets its mass from a Yukawa coupling to the defect's order parameter (**H-YUKAWA**), that mass *vanishes
   at the core*: matter occurs there as massless modes confined to the defect -- chiral 1+1-dimensional modes moving
   at c along a string, 2+1-dimensional modes on a wall, a bound zero mode on a monopole (Hindmarsh & Kibble p.33-34;
   Eto & Suzuki p.15-16, p.22, App. A; READ). `defects.py` computes the Jackiw-Rebbi profile cosh(x)^-1, finds it
   normalisable with the mass exactly 0 at the core, and finds the opposite coupling sign non-normalisable (the
   control). The zero modes' group velocity is exactly 1 (c), never more. **Graded: the phrase is SUPPORTED in the
   literature's sense, for strings, walls and monopoles, on H-YUKAWA.** It is M's hypothesis carried as a hypothesis:
   the literature gives the phenomenon; it does not give a seat.
2. **As seats, the static string, the global monopole and the gauge monopole pass M-S1A-P3 (i).** Each is a static
   metric with g^tt < 0, so t is a time function and there is no closed causal curve (computed). None changes the
   spatial topology, so Geroch/Borde have no premise at the seat (`create.is_topology_change(False, False)` is False).
   **The spinning string is DISQUALIFIED inside r < S/alpha** (De Lorenci & Moreira eq.(2), READ; recomputed), unless
   its spin is below its dislocation (S < kappa, globally hyperbolic). A **Gott pair** carries CTCs but needs
   gamma > 5.3e5 at the Planck bound and cannot be assembled in an open universe with timelike total momentum (Carroll,
   Farhi, Guth & Olum, READ). The **wall**'s global causal structure is **OPEN** (not computed here). The **texture**
   is a spacetime *event* (Durrer Table 1) that collapses (Derrick, computed): **EMPTY IF {H-SEAT-PERSISTS}** as a seat.
3. **Sturm never certifies a defect seat -- and in every class the certificate lies past the class's own gravitational
   limit.** Sturm's sufficient condition, in the form `specthm.py` states it (4 pi G T_kk s^2/c^4 >= pi^2, read from its
   source at run time), needs: in a string core (H-UNIFORM-CORE) mu >= pi^2/16 (or pi^2/32), against the cone closing
   at G mu = 1/4; for a global monopole eps >= pi^2/2 = 4.93, against eps < 1; for a gauge monopole Q/b >= pi, i.e.
   2 M_out/b >= pi^2 > 1 (inside its own gravitational radius); for a thick wall a thickness of at least pi^2/2 = 4.93
   of its own de Sitter radii; outside a string core T_kk = 0. This parallels `spec.py`'s 2 pi^2/3 for the ball (S-2).
   Since Sturm is *sufficient*, its failure does not refute seating; it means no defect is certified by that route.
4. **The defects' "turns" are not the board's conjugate points, except the wall's.** A straight string turns every
   ray by 4 pi G mu *independently of impact parameter* (HK p.90): two rays at b cross at L = b/tan(4 pi G mu), linear
   in b -- no caustic, no single focus (at b = R_sun and the Planck bound, L = 2,467 AU against the Sun's 548 AU from
   `spec.focal_length`). The global monopole deflects by eps*pi for every b (Durrer eq.38): a focal *line*. Whether
   these count as a TURN depends on a reading the board never fixed, named both ways: **H-TURN-CROSSING** (any second
   meeting: yes) and **H-TURN-CONJUGATE** (a caustic: no). **The wall is different:** it violates the SEC (repulsive
   to matter at rest, R_uu = -4 pi G sigma) yet focuses null rays that cross it (R_kk = +8 pi G sigma); the
   Raychaudhuri equation gives a genuine caustic at f = c^4/(4 pi G sigma) = 1/(2 beta), half the wall's own de Sitter
   radius (computed; the negative-tension control has none). A 1 AU focus would need sigma = 6.4e31 J/m^2.
5. **Against D68's obstructions:**

   | obstruction | H-DEFECT-SEAT: the defect at the seat | a defect as the throat's support (the wormhole literature) |
   |---|---|---|
   | **O-SEAT** (supply at the seat) | **OPEN via N_S5 \| N_DEFB** -- no defect supplies the payload in any source read; a B-violating core (HK p.63) is a new named OPEN pathway N_DEFB, direction, rate and feed computed nowhere. The board's grade (`docket68/seat.grade_o_seat` = OPEN) is not moved | -- |
   | **O-HOLD** (holding the throat) | **LEAVES** (the seat is not the throat; the board's grade stands) | **LEFT given H-CANONICAL**: every canonical scalar + gauge field satisfies the NEC pointwise (computed: T_kk is a sum of squares), so topological censorship (FSW Thm 1, READ) binds. **OPEN via N_NEGT** outside it: the flat ring/polyhedral wormholes need strings of *negative* tension, T = -c^4/(4G) (Gibbons & Volkov; Visser 1989; READ and recomputed) -- and "no natural mechanism ... is currently known" (Visser p.5). A string's *quantum* fluctuations give a transient opening only, "exponentially fragile", transit d + logs (Fu, Grado-White & Marolf, READ): not a hold. Never REMOVED |
   | **O-LOOP** (time loops) | static seats: none (computed); spinning string: CTCs inside r < S/alpha (disqualified at a seat) | ring-wormhole mouths in one space with unequal surrounding mass become a time machine after T ~ R L c/(G M) (Frolov, Krtous & Zelnikov eq.6.9, READ; 1.4e9 yr for an Earth-mass shell, L = 1 ly) -- **O-LOOP reintroduced**, and the seat mouth lies on the loop |
   | **O-MAKE-TOPO** | LEAVES (no topology change at a defect seat) | a ring wormhole *made* from flat space is a topology change (`create.is_topology_change(False, True)`), Geroch needs no matter assumption, and Gannon makes a non-simply-connected Cauchy surface singular under the WEC (FKZ p.1; FSW p.2): binds |
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

**Overall grade of H-DEFECT-SEAT, alone:** the phrase is SUPPORTED in the literature's precise sense (H-YUKAWA);
static string and monopole seats pass the seat's causality condition; every class lands in specthm's S-3 (as specthm
already placed it), Sturm never certifies one, only the wall gives a genuine caustic; **it removes no obstruction**:
O-SEAT stays OPEN (one new OPEN pathway named, N_DEFB), O-HOLD is LEFT for canonical defects and OPEN via N_NEGT for
negative-tension ones, and no route arrives faster than light. Not retired: a failure alone does not retire a
hypothesis (docket68/CHARTER.md, M's standing instruction), and the combinations are step 3.

## 1. What was computed (all in `defects.py`, each with its owner or source)

**Stress tensors and energy conditions** (orthonormal frame, outside the core, **H-THIN**), exact:

| class | (rho; p1, p2, p3) / scale | NEC | WEC | SEC (rho + sum p) | DEC | source of the row |
|---|---|---|---|---|---|---|
| string (axis 3) | (1; 0, 0, -1) mu | SAT, SAT, SATURATED | SAT | SATURATED (0) | BOUNDARY | HK eq.(4.1) |
| wall (normal 1) | (1; 0, -1, -1) sigma | SAT, SATURATED, SATURATED | SAT | **VIOLATED (-1)** | BOUNDARY | CGS eqs.(2.18)-(2.19) |
| global monopole | (1; -1, 0, 0) eta^2/r^2 | SATURATED, SAT, SAT | SAT | SATURATED (0) | BOUNDARY | sigma model on the hedgehog, computed |
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

**Geometry.** String: the linearised field HK eq.(4.3) gives the deficit 8 pi G mu (**H-LINEAR-GRAV**); with tension
T, deficit 4 pi G (mu + T) and potential 4 G (mu - T) ln R (HK eq.(4.6)) -- the canonical string (T = mu) has no
Newtonian force (HK p.84); the control T = 0 has. HK's printed 5.18 arcsec and 1.35e21 kg/m at G mu = 1e-6 are
reproduced (5.1840; 1.3466e21 with `spec.G_SI`, `spec.C_SI`), and 4 pi G mu does not reproduce them. Global monopole:
the exact Einstein tensor of dr^2 + A r^2 dOmega^2 gives rho = (1 - A)/(8 pi A r^2), p_r = -rho, p_t = 0, which
matches the hedgehog exactly when Delta = 8 pi eta^2/(1 + 8 pi eta^2) -- Barriola-Vilenkin's 8 pi G eta^2 at first
order. Wall: R_uu = -4 pi sigma delta, R_kk = +8 pi sigma delta (crossing), 0 along the wall; Tolman mass per area
sigma - 2 tau = -sigma (CGS p.12); beta = 2 pi G sigma/c^4 from CGS's kappa sigma = 4 beta. Texture: Derrick's
dE/dlambda = I1 + 3 I2 > 0 in d = 3 (z3: no stationary point), while d = 1 admits one (the control: walls exist).

**Figures** (each recomputed): Planck NG bound G mu < 1.5e-7 (95%, Planck+WP; 1.3e-7 with high-l; AH 3.2e-7): deficit
3.77e-6 rad, mu = 2.02e20 kg/m, mu c^2 = 1.82e37 J/m. String crossing at b = 1 m: 5.3e5 m; at b = 1 AU: 8.39 ly.
Gott: gamma > 5.305e5 (1 - v < 1.8e-12). GV ring: |T| = c^4/(4G) = 3.0256e43 N (printed 3.0257e43); a 1 m ring needs
2.115e27 kg-equivalent, 1.11 Jupiter masses (Jupiter from `spec.LENSES`). Visser cube edge c^4/(8G) = 1.513e43 J/m
(printed 1.52e43); c^4/(4 pi G) does not reproduce it.

## 2. The z3 bookkeeping

`grades()` encodes, as constraints: a held traversable throat needs NEC violation (FSW Thm 1; GV p.3; Visser p.4);
H-CANONICAL forbids NEC violation (the theorem above); in this screen the only NEC-violating source is a negative
tension, possible only through N_NEGT; O-SEAT is removed only by a supply shown through N_S5 (board) or N_DEFB (new);
the seat condition forbids a CTC and a topology change at the seat; static means CTC-free; inside a spinning string's
radius means CTC. Vacuity: the board is SAT, and canonical-without-throat is SAT. Verdicts (checked): O-HOLD given
H-CANONICAL **LEFT**; outside it **OPEN via N_NEGT**; O-SEAT **OPEN via N_S5 | N_DEFB**; static seats **PASS**; inside
a spinning string's CTC radius **DISQUALIFIED**. Four mutation controls each move a verdict and are caught
(`drop-FSW`, `neg-asserted`, `defb-asserted`, `spin-ok`). STRUCTURAL, not counted: OPEN pathways are free atoms, so
"OPEN via" is their encoding. The screen is bookkeeping over findings owned elsewhere, not new physics, and only as
good as its encoding.

## 3. Findings (recorded, not repaired)

- **F1 (FOR M).** "Matter can occur but not in its original geometric form" has an exact literature counterpart --
  zero modes at defect cores -- for all three persistent classes, on H-YUKAWA. A grader who said the phrase had no
  precise sense would under-represent it.
- **F2 (AGAINST M).** No source read gives a defect that *supplies* matter at a seat; the phenomenon is a change of
  form of matter already there. O-SEAT does not move. A grader who read F1 as a supply would over-represent it.
- **F3.** In every class Sturm's certificate lies past the class's own gravitational limit (cone closing, solid angle
  exhausted, trapping, thicker than its own horizon) -- the same shape as `spec.py`'s 2 pi^2/3 for the ball.
- **F4.** The wall is the one class with a genuine focal point for light (crossing rays), while being repulsive to
  matter at rest -- an SEC-violating, NEC-respecting lens. Its global causal structure is OPEN here.
- **F5.** The board's PART 2 "TURN" was never fixed as conjugate point versus crossing; the string and the global
  monopole split on it. Named both ways (H-TURN-CONJUGATE, H-TURN-CROSSING); M's to rule if it matters.
- **F6.** Every string-supported traversable throat in the sources read needs a negative tension (or a quantum,
  transient, fragile opening). With both mouths in one space and unequal surrounding mass it becomes a time machine
  (FKZ), so the seat mouth would carry a CTC -- excluded at the seat by M-S1A-P3 (i) unless the masses balance.
  Under M-S1A-P3 (i) the GV ring's curvature singularity, being at the throat, is not itself disqualifying.
- **F7.** Under H-SM-ONLY no stable defect exists; and at an electroweak core at most the Higgs share (<= 0.172, first
  order, massform) of the payload changes form.
- **F8 (route record).** arXiv hep-th/0001128, tried as Rubakov & Shaposhnikov 1983 ("Do we live inside a domain
  wall?"), is an unrelated paper. R-S 1983 is NOT READ; the wall zero mode rests on Eto & Suzuki (and their refs to
  Jackiw-Rebbi 1976 / Jackiw-Rossi 1981, CITED there, not read) and on the computation.

## 4. Named hypotheses

H-DEFECT-SEAT (M's, under test); H-CANONICAL; H-THIN; H-LINEAR-GRAV; H-UNIFORM-CORE; H-SM-ONLY; H-SEAT-PERSISTS;
H-TURN-CONJUGATE; H-TURN-CROSSING; H-YUKAWA; H-STATIC-STRING; OPEN pathways N_NEGT and N_DEFB (and the board's N_S5).
Each is stated in `defects.HYPOTHESES`.

## 5. Open

- The domain wall's global causal structure (CTC / Borde at a wall seat): not computed.
- N_DEFB: whether a B-violating core can supply baryons -- direction, rate and feedstock computed nowhere.
- N_NEGT: a negative-tension string -- no mechanism known.
- The gauge monopole's lensing seat (S-1-like) for any specific monopole: not computed.
- Whether a texture "event-seat" means anything on the board (no definition exists): OPEN without H-SEAT-PERSISTS.
- The reading of TURN (H-TURN-CONJUGATE vs H-TURN-CROSSING): for M.
- Combinations (step 3): defect seat x H-THROAT-BITS (a singular ring throat is not disqualified by M-S1A-P3 (i), but
  still needs N_NEGT); defect core x S13 (topological hold vs H-RELEASE); defect seat x H-QET-EXOTIC. Not screened here.
- Observational bounds on walls and monopoles (Zel'dovich-Kobzarev-Okun; Parker): NAMED, NOT READ.

## 6. Sources (READ at source; route recorded; open content only; no paywall or login wall met)

| key | source | route | used |
|---|---|---|---|
| HK | Hindmarsh & Kibble, *Cosmic strings*, arXiv hep-ph/9411342v1 | alphaXiv answer_pdf_queries (full text) | pp.16, 26, 33-34, 36, 53-54, 63, 84-85, 90 |
| DURRER | Durrer, *Global field dynamics ...*, arXiv astro-ph/9411010 | alphaXiv | pp.4, 8-10, 12-13, 18 |
| CGS | Cvetic, Griffies & Soleng, arXiv gr-qc/9306005 | alphaXiv | abstract, pp.2, 6, 10, 12 |
| VISSER89 | Visser, *Traversable wormholes: some simple examples*, arXiv 0809.0907 (PRD 39 3182) | alphaXiv | pp.3-6 |
| GV17 | Gibbons & Volkov, *Weyl metrics and wormholes*, arXiv 1701.05533v3 | alphaXiv | pp.3, 20-22 |
| FKZ23 | Frolov, Krtous & Zelnikov, *Ring wormholes and time machines*, arXiv 2305.03887 | alphaXiv | pp.1, 5, 17-18 |
| CFG94 | Carroll, Farhi, Guth & Olum, arXiv gr-qc/9404065 | alphaXiv | abstract, pp.2, 4, 10 |
| DLM04 | De Lorenci & Moreira, arXiv gr-qc/0309122v2 | alphaXiv | p.1 eqs.(2)-(3) |
| PLANCK13 | Planck 2013 XXV, arXiv 1303.5085 | alphaXiv | abstract, Tables 2-3 |
| FSW93 | Friedman, Schleich & Witt, *Topological censorship*, arXiv gr-qc/9305017v2 | alphaXiv | pp.2-3 |
| FGM19 | Fu, Grado-White & Marolf, arXiv 1908.03273v2 | alphaXiv | abstract, pp.1-5, 15-17 |
| ETO25 | Eto & Suzuki, arXiv 2506.16765v1 | alphaXiv | pp.1, 15-16, 22, 24-25 |
| gauge monopole attractive | arXiv gr-qc/9506068 | Firecrawl research search (abstract) | abstract |
| thick walls | arXiv gr-qc/9903059 | Firecrawl research search (abstract) | abstract |
| *route error* | arXiv hep-th/0001128 | alphaXiv | not R-S 1983; nothing rests on it |

Copyrighted text stays out of the tree except short phrases with their page. No host refused a request.

## 7. Adversarial notes, both directions (for the verification step)

- *Could this over-represent M?* The zero-mode reading is conditional on H-YUKAWA and gives a change of form, not a
  supply (F2); no class is certified by Sturm; no obstruction is removed. Checked: every "holds" in this file carries
  its hypothesis.
- *Could this under-represent M?* The static string and the monopoles pass the seat's causality condition outright;
  the wall gives a genuine caustic; N_NEGT and N_DEFB are kept OPEN, not LEFT; H-SM-ONLY is named, not assumed, so the
  beyond-SM cases stay OPEN; M-S1A-P3 (i)'s "singular throat not disqualified" is applied to the GV ring.
