B.push(p([t('Principal Results',{bold:true,size:23})],
  {align:AlignmentType.LEFT,spacing:{before:280,after:100}}));
B.push(p([t('The paper is long because it reports its failures at the same length as its findings. This list is provided so that a reader may take the substance without the argument. Results resting on exhaustive computation over a stated finite space are marked ',{size:SM}),
  t('[E]',{size:SM,bold:true}),t('; those resting on proof ',{size:SM}),t('[P]',{size:SM,bold:true}),
  t('; those on statistics ',{size:SM}),t('[S]',{size:SM,bold:true}),
  t('. Section numbers are given for each.',{size:SM})],{spacing:{before:0,after:140}}));

function pr(txt,tag,sec){return p([t('· ',{size:SM,bold:true}),t(txt,{size:SM}),
  t(`  ${tag} §${sec}`,{size:SM,color:'666666'})],
  {spacing:{before:26,after:26},indent:{left:convertInchesToTwip(0.18)}});}

B.push(p([t('Construction',{bold:true,italic:true,size:SM})],{spacing:{before:100,after:40}}));
B.push(pr('Of the 630 cells in the enclosing box, 210 are admissible: 118 occupied, 92 reserved, and the remainder void or beyond Pauli capacity.','[E]','3'));
B.push(pr('The displacement vector ΔQ takes just two magnitudes and sorts the elements into three geometric classes on angular-momentum grounds alone.','[E]','6'));

B.push(p([t('The lattice as an ordered set',{bold:true,italic:true,size:SM})],{spacing:{before:120,after:40}}));
B.push(pr('The order dimension of Λ is exactly three, so no two linear orders encode its containment relation and the third coordinate is necessary rather than convenient.','[P]','7'));
B.push(pr('Λ is a bounded distributive lattice; hydrogen at (1, 0, 1) is its unique minimum, not a chosen origin.','[E]','8'));
B.push(pr('Closure follows from the form of the constraints. A coordinate may be added only if its bounds are monotone in a single existing coordinate and oriented the same way; three candidate additions fail, for three distinct reasons.','[P]','9.1–9.4'));
B.push(pr('A relativistic lattice built on j-subshells exists, is closed, has the same 210 cells, and preserves the capacities and the parity balance.','[E]','9.3'));
B.push(pr('Shell capacities 2n² are slice volumes wherever the ℓ ceiling does not bind; Λ is Sperner without being rank-symmetric; the rank generating function vanishes at q = −1, an exact parity balance forced by spin degeneracy.','[P]','10'));
B.push(pr('Madelung slice volumes pair exactly, V(2m−1) = V(2m) = 2m², by a floor identity; the two slices of a pair are each the image of a shell under a shear, which is why period lengths coincide with shell capacities.','[P]','11.1'));
B.push(pr('Projecting Λ along n + ℓ reproduces the Janet left-step table; fibring it along n reproduces the chemical groups, placing helium with the alkaline earths by a second and independent route.','[E]','11.2, 12.1'));
B.push(pr('Under spin–orbit splitting the Madelung functional keeps its volumetric content and loses its ordering content; no functional of (n, ℓ, j) reproduces the relativistic filling sequence.','[E]','11.4'));
B.push(pr('The kainosymmetric subshells are exactly the boundary diagonal ℓ = n − 1. Because that diagonal meets only odd Madelung levels, and levels pair, secondary periodicity recurs every second period — confirmed at 12 of 14 group–diagnostic pairs.','[P][S]','12.2, 12.3'));
B.push(pr('The orientation of the lattice is rigid: exactly one of 120 subshell orderings survives, and the Madelung functional is unique among small-integer shears.','[E]','12.4'));

B.push(p([t('The periodic system within the lattice',{bold:true,italic:true,size:SM})],{spacing:{before:120,after:40}}));
B.push(pr('The occupied cells form an order ideal. This is a corollary of monotone filling, with a two-line derivation, and is presented as such.','[P]','13.1'));
B.push(pr('The property is convention-dependent: under strictly measured configurations the occupied set has 110 cells and seven holes, and closure, column saturation and the linear-extension property of Z all fail. The holes locate the anomalies.','[E]','13.3'));
B.push(pr('The ideal is all-or-nothing by column — nineteen full, six empty, none partial — making the realised system one of exactly 120 admissible configurations.','[E]','14'));
B.push(pr('Three maximal cells leave five covering addresses for any further element. Those addresses lie in the columns 5g, 6f and 7d, which are exactly the columns relativistic calculation predicts will fill next among those the ceilings permit naming.','[E]','16, 16.1'));

B.push(p([t('Among the sorting systems',{bold:true,italic:true,size:SM})],{spacing:{before:120,after:40}}));
B.push(pr('Atomic number and Madelung order are linear extensions of Λ, reversing none of its 3,742 comparable pairs. Pettifor\'s scale is not order-compatible in either orientation, reversing 960 of 1,684.','[E]','19'));
B.push(pr('No linear function of the lattice coordinates reproduces Pettifor\'s scale, because ∂MN/∂k changes sign at the f-block. This is a theorem, not a difficulty of fitting.','[P]','20'));
B.push(pr('Nuclear structure lies outside the framework: the nuclear shell model imposes no condition ℓ ≤ n − 1, which is the first of the two bounds defining Λ.','[P]','18.4'));

B.push(p([t('Limits',{bold:true,italic:true,size:SM})],{spacing:{before:120,after:40}}));
B.push(pr('Every axis is a count, so Λ ⊆ ℕ³ and every derived quantity is dimensionless. No metric coordinate can be adjoined without destroying closure.','[P][E]','22'));
B.push(pr('Six predictive applications were attempted. All six failed or were outperformed by descriptors available since the 1980s, and each failure is reported with its diagnosis.','[S]','23'));
B.push(pr('One narrow result survives: valence occupancy carries information about hydride formation enthalpy that established scales do not encode. Tested on the structure-map task those scales were built for, it adds nothing.','[S]','23.1, 23.2'));
B.push(pr('The lattice fixes where anomalies fall and the order of their magnitudes, and supplies no magnitude.','[S]','12.3'));

B.push(p([t('The order-theoretic results carry no sampling uncertainty, being exhaustive over finite spaces that are stated in each case. The empirical results rest on samples between five and 139 and are reported with intervals or exact tests throughout. One claim, on nuclear magic numbers, was withdrawn because it cannot be adequately powered at any sample the subject affords.',{size:SM})],
  {spacing:{before:160,after:80}}));
