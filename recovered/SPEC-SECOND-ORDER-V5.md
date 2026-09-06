# SPEC-SECOND-ORDER (V5) -- S95 ITEM 1. DESIGN ONLY; NO BUILD UNTIL RULED. Written against the frozen Step-0 functional (Route A discipline).
## 0. Object
Step-0 functional Phi[P] = RHF average-of-configuration energy (hfc2.HFC; scalar-relativistic kernel libshoot_sr; c = 137.035999 the only number)
on the sealed log mesh (npts=4000, r in [1e-6/Z, 300] a.u.). Sealed chain quantity: D(c;Z) = E[core(Z-1)+c] - E[core(Z-1)], m(Z) = D(run) - D(ent).
V5 quantity: E2 = second-order Rayleigh-Schroedinger energy of H_{N,Z} about the SEALED RHF determinant, in the SEALED object's own orbitals.
   dD2(c;Z) = E2[core+c] - E2[core];   dm2(Z) = dD2(run) - dD2(ent).   The filed number per row is dm2 (Ha) and dm2/m.
## 1. Partition (declared, term by term)
E2 = sum_{ab in occ, vw in virt} |<ab||vw>|^2 / (e_a+e_b-e_v-e_w) with (a) core-core, (b) core-entrant, (c) entrant-entrant (open shell, fractional
   weight = q(q-1)/(Q(Q-1)) under H4 AOC; declared, NOT a theorem), (d) single excitations: NON-ZERO for AOC-RHF (Brillouin fails for
   average-of-configuration), included explicitly as sum_{a,v} |<a|f|v>|^2/(e_a-e_v).
Differential dD2: core-core term (a) does NOT cancel exactly (the core RELAXES between core and core+c in RHF); it is computed on both sides
   (J2 standing law: each side its own stationary object; no frozen-core shortcut). Cheap check: frozen-core (a)-cancelled variant as a second column.
## 2. Virtual spectrum (the new object)
Per channel l = 0..l_max (l_max = 6; J1 standard, Dzuba-Flambaum), diagonalise the SEALED one-electron operator h_l = T_SR + Vloc + X (nonlocal
   exchange as the sealed kernel applies it, projected on the grid to a dense 4000x4000 symmetric matrix via the Numerov stencil + exchange kernel)
   -> full spectrum: occupied + bound virtuals + BOX-DISCRETISED continuum (box = sealed rmax 300 a.u.; the mesh IS the box). No Sturmian, no
   B-splines: the grid basis is the sealed object's own basis (Route A: no new mathematical object enters). Keep virtuals with e_v < E_cut;
   E_cut swept 20/50/100 Ha as the convergence lever (instrument rule: lever must move output before any row is filed).
   Exchange in h_l: the sealed kernel's nonlocal X (not the Slater projection of so94) -- declared difference from so94, which was a sensitivity column only.
## 3. Two-electron integrals
Slater R^k(ab;vw) by the standard Y^k cumulative construction on the log mesh (O(npts) per (a,b,k)); contracted with virtual pairs blockwise per
   (l_v,l_w) as matrix products (N_v(l) x N_w(l') x npts <= 60x60x4000 doubles = 115 MB). k-range by triangle rules; angular factors = the AOC
   average-of-configuration coefficients (same tables the sealed kernel uses).
## 4. Cost per row (estimate, to be measured on row 89 first)
Spectra: 7 dense eigensolves 4000^2 per side, ~7 x 2 s = 15 s/side. Integrals: N_occ ~ 30 shells, N_virt ~ 7 x 60 after cut, pairs (a,b) ~ 500,
   R^k evaluation ~ 500 x 10 k x 4000 + contractions 500 x 10 x 60^2 x 4000 x 49 channel pairs ~ 4e12 flop worst case -> bounded by the l-triangle to
   ~4e11 -> ~1-3 min/side in numpy. Two sides x two channels = 4 objects/row -> ~10 min/row, 5 rows ~ 1 h. Zeno: one (row, side, channel) per run, JSON per object.
## 5. What V5 IS and IS NOT (declared before any number)
IS: the second-order estimate of the differential correlation shift of a decided margin, in the field's own orbitals -- the object ledger J says
   nobody publishes at our rows (J4a). Accuracy envelope from the literature: second order within 10-40% of all-order (J2 screening factors).
IS NOT: a bound. dm2 cannot certify criterion 3; it converts "(iii) not bounded" into "estimated to second order with a literature-calibrated
   envelope". A rigorous bound would need the third-order remainder, which no route on the chain supplies. T4 must say so.
## 6. Can-fails (required before any row is scored; cases from OUTSIDE the instrument)
CF-A lever-dead: E_cut := 0 (no virtuals) -> E2 = 0 exactly on both sides, dm2 = 0.     CF-B non-vacuity: He (Z=2) E2 must land within 10% of the
   textbook MP2 correlation energy of He (-0.0374 Ha; external number) -> proves the integral/denominator machinery on a closed shell with no AOC weight.
CF-C independence: scale all |<ab||vw>|^2 by 2 -> E2 doubles exactly.    CF-D J2: core-core term differs between sides (relaxation present, >= floor).
## 7. Route-A discipline
Instrument reads sealed orbitals from rt/ and never re-converges them; every object hashed; predictions (pack95/PREDICTION-S95-V5.md) hashed BEFORE
   any build. Rows: 38 56 72 89 105 only. No sealed file edited; results in pack9N/v5-ROW-SIDE-CHAN.json.