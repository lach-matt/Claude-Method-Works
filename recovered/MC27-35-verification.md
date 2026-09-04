# Batch 6 (MC-27…35) — verification ledger. MEASURED unless marked.

## MC-27 (§12.11.0.1) — occupancy clock / definability≠reachability
- objects (source signatures) = 33 ................ MEASURED ✓
- object-pairs joined by a step = 739 ............. MEASURED ✓ EXACT
- steps raising k = 0 ............................. MEASURED ✓
- three SCCs pure in occupancy: 8@k=3, 15@k=2, 10@k=1 ... MEASURED (Tarjan) ✓ EXACT
- tick = k − g .................................... definitional
- census over 2,735,716 = 1654² ordered pairs:
  - lattice-comparable 311,180 = 11.4% ........... MEASURED ✓ EXACT
  - composition-path 675,606 = 24.7% ............. MEASURED (transitive closure) ✓ EXACT
  - in both 9,720 = 0.4% ......................... MEASURED ✓ EXACT
- nine = unique dim where time exists (reg 314/345) ... structural, from source

## MC-28 (§12.11.0.2) — arrow is frame-relative / observation
- (g,G) extended index = 13,775 cells ............ MEASURED ✓ EXACT
- composable pairs (extended) = 2,620,090 ........ MEASURED ✓ EXACT
- raise occupancy 826,950 = 31.6% ................ MEASURED (a.G > a.k over composable pairs) ✓ EXACT
- four arrows X_w (present-count G as target occ), all CLOSED E=0:
  - shell 9,407 ✓  subshell 9,845 ✓  occupancy 5,165 ✓  spin 7,160 ✓  ... MEASURED (double-proj) EXACT
- sum breaks closure (E=1,494>0) .................. MEASURED ✓ (max/min follow, standard)
- one arrow per coordinate, no others ............ from source (reg 352)