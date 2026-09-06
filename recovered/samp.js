B.push(h3('24.1  Sample sizes and what they permit'));
B.push(p([t('The warrants in Table 7 divide into those resting on exhaustive computation, where the search space is finite and fully enumerated, and those resting on statistics, where a sample stands for a population. The first kind carries no sampling uncertainty at all: when the paper reports that Λ has 21,945 pairs and none violates closure, the figure is the population. The second kind does, and the samples available in this subject are small. It is worth setting out how small, and what each permits.')]));
B.push(tcap(8,'Sample sizes and uncertainty for every statistical claim in the paper. Intervals are bootstrap percentile for R², Clopper–Pearson for proportions, and exact permutation where the sample is too small for an asymptotic test.'));
B.push(table(
  ['Claim','Section','n','Estimate','Interval or exact test'],
  [['Structure-map separation gain','23.2','139','+0.000','McNemar p = 1.000'],
   ['Pettifor MN from lattice + ℓ²','18.2','78','R² = 0.594','[0.50, 0.74]'],
   ['Ionisation energy','23.5','69','R² = 0.280','—'],
   ['Electronegativity','23.5','66','R² = 0.090','—'],
   ['Hydride formation enthalpy','23.1','39','R² = 0.592','[0.43, 0.78]'],
   ['Exchange-energy labelling','23.4','30','AUC = 0.589','p = 0.233'],
   ['Anomaly enrichment','23.3','20','—','all directions reversed'],
   ['Secondary periodicity, pooled','12.3','14','12 of 14','[0.57, 0.98]'],
   ['Covalent-radius minima','12.3','10','10 of 10','[0.69, 1.00]'],
   ['Reduction-potential maxima','12.3','5','5 of 5','[0.48, 1.00]'],
   ['Deficit ranked by k','12.3','5','ρ = −1.000','exact p = 0.0083'],
   ['Magic numbers','18.3','6','d = −1.01','power 0.51 — withdrawn']],
  [2600,900,700,1400,2100],['Magic numbers']));
B.push(p([t('Three practices follow from the table and are used throughout. Where the sample is too small for an asymptotic test, an exact one is used instead: the rank agreement between the contraction deficits and the occupancy coordinate rests on five points, and its probability of 0.0083 is computed by enumerating all 120 permutations rather than by approximation. Where a proportion is reported, a Clopper–Pearson interval accompanies it, which is why the five-of-five reduction-potential result is described as corroborating the others rather than standing alone — its interval reaches down to chance. And where a null result is reported, it is reported as a null result rather than as evidence of absence, except in the one case where the distinction was worth labouring.')],
  {spacing:{before:160,after:120}}));
B.push(p([t('That case is the magic-number test, which Section 18.3 now withdraws. It is the only claim in the paper that was reported as a finding and has been removed on statistical grounds rather than corrected, and the reason is instructive: with six proton magic numbers below Z = 118 and an observed effect size of about one standard deviation, the test has roughly even odds of detecting a real effect, and no larger sample can be obtained. The population is six. A test that cannot be adequately powered in principle should not be reported as having returned an answer.')]));
B.push(p([t('The general position is that the order-theoretic results of Parts II and III do not depend on sample size at all, being exhaustive over stated finite spaces, while every empirical claim in Part V and in Section 12.3 does. The largest empirical sample in the paper is 139 and the smallest that is retained is 5. Readers weighing the two kinds of result against each other should weigh them accordingly, and the asymmetry is the honest summary of what this work has established: a well-characterised combinatorial object, and a thin empirical record attached to it.')]));
