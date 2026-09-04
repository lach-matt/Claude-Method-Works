# FINDING-TERMS (s38, item 1) — LS term/multiplet energies on the walk's field, 13 d/s rows (nlterm.py/.jsonl; TABLE-TERMS-SESSION-38).
Design filed BEFORE the run in PREDICTION-TERMS-VALIDATION-SESSION-38.md; that file's decisions (i)(ii)(iii) were DETERMINED BY THE ROWS
(M's ruling, s38), not chosen. No constant beyond c. Record first-ionised subshells and record ground-term labels RECALLED-NOT-ENTERED, comparison only.

## 1 · Machinery validated before any result was read
Gate PT0 (hfterm, inherited): determinant average == Slater average on d^2, f^2, d^3 and d^1s^1, |diff| <= 2.2e-16.
Gate PT8 (NEW, s38): the Slater DIAGONAL-SUM rule over all determinants of l^N — sum over determinants == sum over terms weighted (2S+1)(2L+1)
to 0..2.8e-17, determinant mean == E_avg to 1.7e-18, and the LOWEST term COMPUTED: d^2 -> 3F, f^2 -> 3H, f^3 -> 4I, f^7 -> 8S.
These are the record's Hund ground terms, reproduced by computation, and they agree with the hund_det (max S then max L) column on every row.
PV-1 HELD. Decision (i) is therefore settled BY MEASUREMENT: the arrangement is computed; the record label is a comparison column that agreed.
PV-2 HELD exactly: on class A (Sc Y La Lu Ac) the d-removed ion is closed-shell and its term energy is 0.00000 identically.
Field check: D_d and D_s reproduce nlwalk_hf to 5 dp on every row (Sc -0.26664/-0.20292 vs -0.2666/-0.2029; Lu -0.15979/-0.21137). The term column
sits on the WALK'S OWN FIELD, not a neighbouring one.

## 2 · THE STRUCTURAL RESULT: the neutral's term cancels out of the gap
gap = D_d - D_s, and with terms D_x(term) = D_x(avg) + dE(neu) - dE(ion_x). Therefore
        gap_term - gap_avg = dE_s - dE_d
and dE(neutral) DROPS OUT IDENTICALLY. The Hund-I term of the neutral's open d^2/f^n — the object PREDICTION-TERMS (s37) named as the mechanism —
cannot differentiate the pair at all. What differentiates is the TERM ENERGY OF THE TWO IONS, and specifically the s-removed ion, which retains the
whole open d (or f) shell AND gains an unpaired s to couple to it, while the d-removed ion has one electron fewer and often closes the shell outright.
Hence the shift is NEGATIVE ON ALL 13 ROWS (every row is pushed toward s-first) with size set by the ion's open-shell structure:
    class A (d^1 s^2, ion closed)   shift -0.0052 .. -0.0098   mean -0.0077
    class B (d^2 s^2, ion d^1)      shift -0.0387 .. -0.0480   mean -0.0438
    class C (f^n d^1 s^2, ion f^n)  shift -0.0189 .. -0.0504   mean -0.0389
This is the mechanism restated correctly by the run. The s37 statement ("removing the d loses that term energy -> D_d deepens") is not wrong about D_d —
D_d does deepen by dE(neu) — but D_s deepens by the SAME amount, so only the ion difference survives.

## 3 · The row-differential exists, and it is the first one measured on the pair
PV-7 HELD. The term correction is NOT class-flat: range 0.0052 to 0.0504, a factor of ten across rows, against every previously measured object
(exchange seam +0.034 +- 0.007 class-flat; S-correlation +0.014 class-flat). Th and Ac — adjacent in Z, split by class — are separated by
    Th shift -0.0387   Ac shift -0.0091   ->  row-differential 0.0296 Ha,
against the 0.016 Ha residual to be explained. The residual is REACHABLE by this mechanism and by no other object measured so far.
Th itself is resolved: gap +0.0083 (d-first, WRONG against the record) -> -0.0304 (s-first, RIGHT). PT-1 HELD. Ac stays d-first (+0.0240 -> +0.0149).
The one row HF got wrong is now right, and it is right for a stated structural reason: Th's ion keeps an open d, Ac's ion does not.

## 4 · AND THE CORRECTION AS APPLIED MAKES THE WALK WORSE, SO THE COMPARISON DECIDES AGAINST IT
SCORE: HF (no terms) 12/13. HF + LS terms 9/13. Fixed: Th. Broken: Hf (+0.0279 -> -0.0168), Pa (+0.0241 -> -0.0198), U (+0.0267 -> -0.0237),
Cm (+0.0463 -> -0.0009, a tie at the boundary). PV-6 FAILED (predicted >= 12/13 within +-0.010 of zero).
Per "comparison decides", LS terms in this form are NOT adopted into the walk field. Residue is not closure: the object is registered as MEASURED,
ROW-DIFFERENTIAL and REJECTED-AS-APPLIED, not carried as an improvement.
THE FAILURES ARE NOT SCATTERED. All four are the rows where LS coupling is least valid — Hf (5d), Pa U Cm (5f actinides). The LS term energy is an
UPPER BOUND on the real term splitting: spin-orbit mixes the LS terms and quenches the splitting, and it does so hardest exactly on 5f/6d.
Decision (iii)'s reason is now a measurement rather than a caution: SO cannot be left out, because the rows it would change are precisely the rows that broke.

## 5 · Failed predictions (logged, not suppressed) and what they cost
PV-4 (class A direction) FAILED. Predicted the gap to INCREASE toward d-first on d^1 s^2 rows; measured DECREASE on all five (-0.005..-0.010).
     Reason: the neutral term cancels (§2); the s-removed ion's d^1 s^1 triplet makes the s removal CHEAPER, pushing toward s-first. Direction of the
     class-A conclusion survives (Ac stays d-first) but the stated mechanism did not.
PV-6 FAILED (9/13, not >=12/13). PT-3 FAILED at Hf (predicted within +-0.010 of zero; measured -0.0168, class flipped). PT-2 FAILED at Cm (predicted
     stays d-first; measured -0.0009). PT-3's Pa/U clause FAILED (predicted decrease <= 0.02 and stay d-first; measured 0.044/0.050 and both flipped).
PT-1 HELD (Th <= -0.010, and Ac stays d-first). PV-1 PV-2 PV-7 HELD. PV-3 and PV-5 NOT TESTED this session — see open items.
Timing flags: none; every prediction above was filed before nlterm.py existed. Faults: F38.1 (rebuild, §H — .json data files omitted from the pack
layering loop; eps0a_table.json missing; caught at the OPEN gates, repaired, all 71 gates re-run from clean before any new work; no result read from the
faulted state).

## 6 · Open, in the order the finding leaves them
(a) SO / intermediate coupling as the companion to terms — now the leading candidate, and PV-5's separation test is unrun. zeta per row (t7c_so /
    t7c_3dhund machinery) against the four broken rows: if SO quenching restores Hf Pa U Cm while leaving Th fixed, the pair closes on terms+SO.
(b) PV-3 frozen-vs-relaxed (decision (ii)) is UNTESTED. The frozen convention was used; its bound is not yet measured. Class A gives the exact zero
    test (both must agree identically) and the flatness test is defined.
(c) correlation x terms (s37 item 2) unchanged, and now must be run on terms+SO rather than terms alone.
