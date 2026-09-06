# B.2.10 enumeration — targets BEFORE searching. B.2.13 commitment.

WHAT IS NEEDED (the measurement, stated exactly)
For cells (n,l) sharing species + parent term, the MEASURED term value T(n,l)=I-E.
Then per interior cell:
  channel bracket W_c = T(n-1,l) - T(n+1,l)
  lattice bracket W_l = min(T(n-1,l), T(n,l-1)) - max(T(n+1,l), T(n,l+1))
  ratio W_l / W_c
Appendix C carries delta-bar and spread only. Levels themselves are NOT in the book.

TARGET SPECIES — ranked by l-span x overlapping n, from Appendix C, all monotone:
  1. Na I    l=0..5  (1.3506, 0.8584, 0.0141, 0.0014, 0.0003, 0.0000)  Sansonetti 2008 JPCRD 37,1659
  2. Mg II   l=0..6  (1.0749, 0.7077, 0.0411, 0.0030, 0.0007, 0.0002, 0.0000)  NIST ASD
  3. C II    l=0..4  (0.6624, 0.3928, 0.0924, 0.0220, 0.0054)  NIST ASD
  4. Ca II   l=0..4  (1.8192, 1.4748, 0.6338, 0.0248, 0.0048)  NIST ASD
  5. Li I    l=0..2  (0.4014, 0.1477, 0.0031)  NIST ASD
EXCLUDED by D1, do not fetch: Al I, Al II, He I, Li II, Ne I (non-monotone in l)

ROUTES per target, in order (Chapter 14 route set):
  R1 NIST ASD levels form (dynamic query)
  R2 NIST Handbook of Basic Atomic Spectroscopic Data (static per-element pages)
  R3 the JPCRD compilation Appendix C already names
  R4 any secondary compilation carrying the same levels

COMMITTED PREDICTION (B.2.13), written before any fetch:
  P-a. Mean W_l/W_c on real Na I levels falls in 0.40 - 0.70.
       (cavity gave 0.549; recalled-defect Na gave ~0.52)
  P-b. The ratio will be WORSE (closer to 1) at low l and BETTER at high l,
       because the l-neighbour is only tight when the two defects are close.
  P-c. At least one fetched cell will violate the lattice bracket outright,
       because 11.2% of adjacent-l pairs are non-monotone and Na I l=4,5
       sit at |delta| < 0.001.