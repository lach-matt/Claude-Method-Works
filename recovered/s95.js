B.push(h3('9.5  The admissible coordinates, and a five-dimensional lattice'));
B.push(p([t('Section 9.4 states the criterion and applies it to four candidates. Applied systematically to every quantity that specifies an atomic state, it returns a short list, and the list is worth having because it bounds what the framework can become.')]));
B.push(tcap(4,'Every quantity that specifies an atomic state, screened against the criterion of Section 9.4. A coordinate is admissible when its range depends on a single existing coordinate, its floor does not fall, and it is not determined by the others.'));
B.push(table(
  ['Quantity','Range','Depends on','Verdict'],
  [['relativistic j, as J = 2j','2ℓ−1 ≤ J ≤ 2ℓ+1','ℓ alone','admissible — Section 9.3'],
   ['ionic charge q','0 ≤ q ≤ k','k alone','admissible'],
   ['excitation target shell e','n ≤ e ≤ E','n alone, floor rises','admissible'],
   ['total spin, as 2S','2S ≡ k (mod 2), 2S ≤ k','k, with a parity condition','FAILS — see below'],
   ['total orbital momentum L','0 ≤ L ≤ ℓ·k','ℓ and k together','fails — a combination'],
   ['magnetic sublevel M_J','−J ≤ M_J ≤ J','falling floor','fails — orientation'],
   ['magnetic quantum number m','−ℓ ≤ m ≤ ℓ','falling floor','fails — Section 9.2'],
   ['radial node count n−ℓ−1','determined','n and ℓ','fails — functional graph'],
   ['unpaired electron count','determined','ℓ and k','fails — functional graph'],
   ['atomic number Z','determined','all three','fails — Section 9.4'],
   ['neutron number N','N_min(Z) ≤ N ≤ N_max(Z)','a combination','fails — Section 9.4']],
  [2400,2000,1900,2100],['total spin, as 2S']));
B.push(p([t('The spin entry repays attention because it fails for a reason the criterion does not state and which was found only by asking what a particular cell meant. Taken loosely, with 0 ≤ 2S ≤ k, the spin axis is closed and appears admissible. But for k electrons in a subshell the total spin is constrained in parity as well as magnitude: 2S must have the same parity as k, since a single electron has S = ½ and each further electron changes 2S by one. Imposing that condition destroys closure, returning 52,173 join and meet failures — the componentwise minimum of two admissible cells can pair an occupancy of one parity with a spin of the other. So the spin axis is closed exactly when it is loose enough to admit impossible states, which is the same defect the neutron axis showed in Section 9.4 arriving by a different route. It is withdrawn.')],
  {spacing:{before:160,after:120}}));
B.push(p([t('Three coordinates therefore survive, and they attach to different places: the relativistic index to ℓ, the ionic charge to k, the excitation target to n. They may be adjoined together, since each is bounded in one of the original three and adding one does not disturb the conditions the others satisfy — the sublattice-intersection argument of Section 9.1 applied repeatedly. Setting aside the relativistic index, which Section 9.3 shows to be a relabelling, the result is a five-coordinate lattice')]));
B.push(eq('Λ₅ = { (n, ℓ, k, q, e) ∈ ℤ⁵ :  ℓ ≤ n−1,  k ≤ 2(2ℓ+1),','' ));
B.push(eq('                                0 ≤ q ≤ k,  n ≤ e ≤ E }','12'));
B.push(p([t('with 7,136 cells at n ≤ 7, ℓ ≤ 4 and E = 9, closed under join and meet, least element (1, 0, 1, 0, 1) — hydrogen, neutral, unexcited — and greatest (7, 4, 18, 18, 9). Its order dimension is five exactly: it embeds in ℤ⁵, and it contains a Boolean 5-cube based at (2, 0, 1, 0, 3), a 2s¹ configuration excited to the third shell, all thirty-two of whose cells are admissible and physically meaningful.')]));
B.push(p([t('The slice structure is what makes the extension intelligible. Fixing q = 0 and e = n recovers Λ itself, 210 cells. Fixing e = n alone gives the 1,565 cells of neutral and ionic species without excitation; fixing q = 0 alone gives the 1,000 cells of neutral species in ground and excited configurations. The two four-dimensional slices are distinct and their intersection is Λ. So the lattice of Part I is the neutral, unexcited slice of a five-dimensional object, and the periodic system is what one sees looking at that object along two of its axes.')]));
B.push(p([t('Two cautions. The excitation ceiling E is a truncation of the same kind as n ≤ 7 and ℓ ≤ 4, and it binds in the same way: at E ≥ 7 every cell admits every target and the population stops growing, so counts quoted at E = 9 are counts for that truncation. And the parity balance of Section 10.3 does not survive the extension. Λ divides evenly at 105 and 105, and its occupied set at 59 and 59, because every column capacity is even; Λ₅ divides 3,575 to 3,561, since the ranges of q and e are not. That invariant is specific to three dimensions.')]));
