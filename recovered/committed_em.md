# Committed before computation — B.2.13

Reconstruction of the two EM indices from their stated invariants.

Lambda_cav (rectangular): coords (m,n,l,s), M=N=L=4,
  s in 1..nu-1 with nu = [m>0]+[n>0]+[l>0].
E1. |L_cav| = 2MNL+MN+ML+NL = 176, and C(176,2) = 15,400 pairs.
E2. join failures 0; meet failures 768.
E3. (m,n,l) core alone: distributive, rank-modular, E(X)=0.

Lambda_sph (spherical): coords (t, l', m', n'), caps t<=1, l'<=5,
  m' <= 2l'+2, n'<=4.   [derived: count 2(N+1)(L+1)(L+3)=480,
  height 3L+N+3=22, pairs C(480,2)=114,960 — three stated invariants,
  one solution]
S1. |L_sph| = 480, height 22, pairs 114,960.
S2. join failures 0, meet failures 0, rank-modularity violations 0,
    distributivity violations 0.
S3. Sperner width 41.
S4. F(-1) = 0 exactly (t is a free 2-chain, contributing (1+(-1))=0).