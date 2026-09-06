B.push(h3('10.5  Which results depend on the ceilings'));
B.push(p([t('The bounds n ≤ 7 and ℓ ≤ 4 in Equation (1) are modelling choices reflecting the elements presently known, not features of the physics. It is therefore necessary to say which of the results above survive a change in those bounds and which do not, since a property of a truncation is a weaker thing than a property of the construction. Every result in this part was recomputed under six ceiling configurations, from (n ≤ 7, ℓ ≤ 3) to (n ≤ 9, ℓ ≤ 4) and (n ≤ 8, ℓ ≤ 5), with the occupied set held fixed. The outcome divides cleanly.')]));
B.push(tcap(3,'Sensitivity of each result to the shell and subshell ceilings, recomputed across six configurations with the occupied set held fixed. Invariant results hold in every configuration tested; contingent results take a value specific to the chosen bounds.'));
B.push(table(
  ['Result','Section','Status','Value at (7, 4)'],
  [['Λ is closed under join and meet','8','invariant','—'],
   ['Unique minimum is (1, 0, 1)','8','invariant','hydrogen'],
   ['Rank sequence is not palindromic','10.4','invariant','—'],
   ['Parity balance F(−1) = 0','10.3','invariant','105 / 105'],
   ['Occupied set is an order ideal','13','invariant','—'],
   ['Occupied set has three maximal cells','16','invariant','Lr, Cn, Og'],
   ['Admissible cell count','3','contingent','210'],
   ['Reserved cell count','3','contingent','92'],
   ['Column count','14','contingent','25'],
   ['Down-sets of the column poset','14','contingent','120'],
   ['Covering cells at the frontier','16','contingent','5'],
   ['Largest rank level (Sperner value)','10.2','contingent','15'],
   ['Σ 2(2ℓ+1) = 2n²','10.1','holds where ℓ ≤ n−1 does not bind','n ≤ 5']],
  [2900,900,1900,1500]));
B.push(p([t('The invariant results are the ones this paper rests on most heavily. Closure, the identity of the minimum element, the parity balance, the rank asymmetry and the order-ideal property all hold under every configuration tested, and in three cases the reason is a proof rather than a computation: closure follows from the form of the constraints, the minimum follows from the constant floors, and the parity balance follows from every column capacity being even.')],
  {spacing:{before:160,after:120}}));
B.push(p([t('The contingent results are counts, and each should be read as a count for the lattice as bounded here. That the reserved cells number 92, that the column poset has 120 down-sets, that the frontier offers five covering cells and that the largest antichain has 15 elements are all statements about (n ≤ 7, ℓ ≤ 4). Extending the lattice to n ≤ 8 raises them to 142, 219, six and 18 respectively. The qualitative claims built on them survive — reserved cells still concentrate at high n and high ℓ, the realised system is still one down-set among many, the frontier is still a small finite set — but the numbers do not transfer, and the paper states them as figures for this truncation rather than as invariants.')]));
B.push(p([t('One entry requires a correction to what was said earlier. Section 10.4 attributed the failure of rank symmetry to the interaction of the two ceilings. That explanation is wrong. The rank sequence remains non-palindromic when the ℓ ceiling is lifted entirely, tested up to n ≤ 20 with ℓ ≤ n−1 and 5,740 cells, so the asymmetry is a property of the constraint structure itself — the growth of the k-range with ℓ against the bounding of ℓ by n — and not of the truncation. The conclusion of Section 10.4 stands; its stated reason did not, and has been amended there.')]));
