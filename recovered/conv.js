B.push(h3('13.3  The idealised and the measured periodic system differ'));
B.push(p([t('The argument of Section 13.2 was that anomalies cannot break downward closure because they relocate an electron without removing a cell that an earlier element already occupied. That argument is wrong, and the correction matters enough to be given in full, because it changes what object Sections 13 to 16 describe.')]));
B.push(p([t('An anomaly does not merely relocate an electron; it may cause an occupancy value to be skipped entirely. Vanadium has three 3d electrons and chromium, measured, has five — so no element has exactly four. Nickel has eight and copper has ten, so none has nine. Rhodium has eight 4d electrons and palladium has ten, so none has nine. Iridium has seven 5d electrons and platinum has nine, so none has eight. Where a skip occurs, the cell corresponding to the skipped value is occupied by nothing, and downward closure fails at that cell.')]));
B.push(p([t('Recomputing the occupied set from strictly measured configurations, assigning each element the observed occupancy of its differentiating subshell, gives 110 distinct cells rather than 118 and 172 violations of downward closure across seven missing cells: (3, 2, 4), (3, 2, 9), (4, 2, 3), (4, 2, 6), (4, 2, 9), (5, 2, 8) and (5, 3, 1). Four columns are then partially filled — 3d holds eight of ten cells, 4d seven of ten, 5d nine of ten and 5f twelve of fourteen — so the saturation property of Section 14 fails as well. The occupied set acquires a fourth maximal cell, and atomic number ceases to be a linear extension, reversing nine of 3,670 comparable pairs.')]));
B.push(tcap(4,'Convention dependence. Results defined on Λ alone are unaffected by the assignment of anomalous configurations; results defined on the occupied set are not. The idealised column is the block assignment used by conventional periodic tables and adopted throughout this paper.'));
B.push(table(
  ['Result','Section','Idealised','Strictly measured'],
  [['Order dimension of Λ','7','3','3 — unaffected'],
   ['Λ closed; minimum (1,0,1)','8','yes','unaffected'],
   ['All invariants of Λ','10','—','unaffected'],
   ['Madelung slices; Janet projection','11','—','unaffected'],
   ['Helium on the alkaline-earth fibre','12.1','yes','yes'],
   ['Elements on the ℓ = n−1 diagonal','12.2','32','32'],
   ['Admissible ℓ-orderings','12.3','1 of 120','0 of 120'],
   ['Distinct occupied cells','13','118','110'],
   ['Occupied set is an order ideal','13','yes','NO — 7 holes'],
   ['Columns fully filled or empty','14','19 / 6 / 0 partial','4 partial'],
   ['Maximal occupied cells','16','3','4'],
   ['Z is a linear extension of Λ','19','0 violations','9 violations']],
  [2900,900,1500,1900],['Occupied set is an order ideal']));
B.push(p([t('The consequence is a change of scope rather than a loss of result, but the change must be stated plainly. Sections 13, 14, 16 and 19 describe the idealised periodic system — the block assignment in which each subshell fills sequentially to capacity, which is what every printed periodic table displays and what the aufbau rule prescribes. They do not describe the measured periodic system, in which twenty elements depart from that prescription and seven cells are consequently never realised. Part II is unaffected throughout, because it concerns Λ as an abstract lattice and never consults the occupied set; the only exception is the rigidity result of Section 12.3, which depends on downward closure and therefore inherits the dependence.')],
  {spacing:{before:160,after:120}}));
B.push(p([t('Read the other way, the failure is informative. The seven missing cells are not scattered: every one of them sits immediately below an anomalously occupied cell, and each corresponds to an occupancy value that the measured filling sequence jumps over. Downward closure therefore functions as a diagnostic. It holds exactly when filling is sequential, and its failures locate the departures — which is a sharper statement than the one it replaces, and a falsifiable one. If a future measurement revised chromium to 3d⁴4s², the hole at (3, 2, 4) would close.')]));
B.push(p([t('An earlier draft of this work stated that every structural result is identical under either convention. That statement was based on comparing two assignments which both used idealised d-block occupancies, and it is false for the strictly measured assignment. It has been withdrawn.')]));
