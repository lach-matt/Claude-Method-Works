# FINDING — E0B(zeta) is exactly zeta-independent; item (1)(i) closed by derivation, item (1)(ii) closed as no-op.  s31.
PE1 HELD (derivation, this project's scaling argument; attributed: Onsager-Mittag-Stephen Ann. Phys. 18 (1966) value; Loos-Gill PRB 84 033103 (2011) Table I
    lists eps_0^b(0) = eps_0^b(1) = ln2/6 - 3 zeta(3)/(4 pi^2) with spin-scaling Upsilon_0^b = 1). E0B = 0.0241792 Ha = 0.0483583 Ry.
PE2 HELD: eps0a_table.json eps_0^a(0) = -0.071019 (LG/Hoffman -0.0710995, d 8e-5), eps_0^a(1) = -0.049884 (-0.0499167, d 3e-5). eps_0 = eps_0^a + E0B:
    -0.046840 (PW92 -0.046644), -0.025705 (PW92 -0.025599) Ha.
PE3 stands as a statement (not run): the Cs zeta~1 cut belongs to form R as defined (bare SOX + resummed ring); it is not removed by any zeta-dependence.
Consequence for the bridge: (1)(i) requires NO code change (both forms already carry the exact zeta-dependence: none); (1)(ii) "rerun the six class rows under
    R with E0B(zeta)" is a no-op — pack30/frachf_ring.jsonl rows STAND as the E0B(zeta) rows. (1)(iii) proceeds: corr='R' hook in t7c_corrz, 15 chain rows.
Not entered: a screened second-order exchange (the bare diagram is polarisation-independent; screening would make its size r_s-dependent) — a candidate for M's
    ruling only; not opened here (no scans, comparison first).
Timing flag F31.1 recorded in PREDICTION-E0B (literature read preceded the file).