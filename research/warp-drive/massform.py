#!/usr/bin/env python3
r"""
massform.py -- DOCKET 65.  MASS FORMATION AT THE SEAT.  M'S MECHANISM, TESTED
IN M'S OWN TERMS.

    python3 massform.py             the reading
    python3 massform.py --selftest  every figure, every control; STDLIB ONLY

Run under python3 (3.11) from research/warp-drive.  STDLIB ONLY.  It imports
higgs, excite, warpfolder, stock, stockgate, transit, ledger, nopath, permute,
gravity and pdgcapture from this directory -- ledger at call time only, since
ledger.py asks this file for its rows while it is itself being imported -- and
COPIES NONE OF THEM: every figure an owner holds is ASKED of it at run time.
The selftest checks with `inspect` that no callable used here is a local
re-implementation carrying an owner's name, checks by identity that each asked
constant IS the owner's object, and reads this file's own source to confirm
each one is assigned from its owner.  It edits no peer.

M's mechanism, verbatim (ledger.RULED_BY_M, row M-S1A-P1):

    "As soon as the information hits the seat, it triggers the higgs field,
     and atomic mass forms."

M's consideration, verbatim, same row:

    "If the elements required for seating are present, then the conditions
     for a higgs field or something like it are also present."

M ruled it be TESTED AS A DOCKET.  It was neither dismissed nor accepted in
advance.  The selftest checks both strings against the ledger row, so a misquote
of M breaks the build.

IN M'S TERMS.  The information is the TRIGGER.  The Higgs field, once
triggered, is what makes atomic mass form.  Mass has an energy, and the energy
has to come from somewhere.  M's sentence names no source; the only candidate
source in M's sentence is the triggered Higgs field, so that is the one tested
first (section 3).  The sentence can be read six ways, and every result below
says which reading it answers, and why:

    SWITCH-ON     arrival turns on a field that was off at the seat;
    EXCITATION, in two branches:
      DISPLACEMENT  arrival displaces the field, and mass forms from that;
      QUANTA        arrival makes Higgs quanta, and mass forms from them;
    CREATION      the triggered field supplies the energy of the mass that
                  forms;
    STOCK         the elements are already at the seat (M's consideration
                  presupposes them) and the triggered field gives them their
                  mass -- the elements present as elements, with their
                  measured mass (H-PRESENT);
    TEMPLATE      STOCK's complement: templates at the seat without all or
                  part of their HIGGS-GIVEN mass (|phi| < v there before
                  arrival), and the triggered field restores it.  H-PRESENT
                  or not, the split is three-way: before arrival the seat
                  is r = |phi|/v < 1 (TEMPLATE, C1), r = 1 (STOCK on
                  H-PRESENT, C5) or r > 1 (neither reading's claim: the
                  trigger has nothing to give; holding r > 1 needs a
                  source outside D20's model).  Section 6, H-PRESENT.

===============================================================================
0.  THE ANSWER
===============================================================================

THE CONSIDERATION IS TRUE, AND, ON P-UNIFORM, IT SINGLES OUT NO PLACE.  THE
MECHANISM, AS STATED -- THE TRIGGERED FIELD FORMING THE PAYLOAD'S ATOMIC MASS --
IS REFUSED ON EVERY READING; ON DISPLACEMENT AND QUANTA IT IS REFUSED AS NET
FORMATION ONLY, AND ATOMIC MASS CAN STILL FORM THERE AS MATTER WITH ITS
ANTIMATTER (THE PAIR ROUTE, PRICED); ON TEMPLATE IT IS REFUSED ON
P-UNIFORM AND H-UNSOURCED-SEAT, AND WHERE THE LATTER FAILS A SEAT PREPARED IN
ADVANCE CAN STILL HAVE ITS ELEMENTS' HIGGS-GIVEN MASS RESTORED ON ARRIVAL (THE
HELD-SEAT RELEASE ROUTE, PRICED; IT FORMS NO BARYONS).  NO READING IS REFUSED
ON A CONTESTED
FIGURE ALONE.  EACH COUNT IS LISTED ONLY AGAINST THE READINGS IT HAS A STATED
REASON TO ANSWER, AND THE TABLE IN SECTION 5 GIVES THE REASON, AND THE REASON
EACH OMITTED COUNT DOES NOT ANSWER.  THE SEAT SPLITS THREE WAYS.  WITH THE
ELEMENTS
PRESENT AS ELEMENTS (H-PRESENT) STOCK IS REFUSED ON PRIOR MASS (C5): THEY
ALREADY CARRY THEIR HIGGS-GIVEN MASS BEFORE ANYTHING ARRIVES, SO THE TRIGGER
GIVES THEM NOTHING, AND THAT CASE NEEDS NO P-UNIFORM.  ITS COMPLEMENT, TEMPLATE
(TEMPLATES AT THE SEAT WITHOUT ALL OR PART OF THEIR HIGGS-GIVEN MASS, |phi| < v
THERE BEFORE ARRIVAL), IS REFUSED BY C1: ON P-UNIFORM THE UNSOURCED FIELD AT
THE SEAT IS AT v, AND ANY LOWER VALUE NEEDS A LOCAL SOURCE (D15, D16), WHICH
ON H-UNSOURCED-SEAT NOTHING HOLDS THERE BEFORE ARRIVAL (THE SENTENCE GIVES NO
SUCH SOURCE; ONLY THE INFORMATION ARRIVES).  H-PRESENT OR NOT, THE SPLIT IS
THREE-WAY: r = |phi|/v < 1 IS TEMPLATE (C1), r = 1 IS STOCK ON H-PRESENT (C5),
AND r > 1 IS NEITHER READING'S CLAIM (THE TRIGGER HAS NOTHING TO GIVE).
THE FINITE HIGGS SHARE -- WHAT THE FIELD GIVES, MEASURED WITH IT SWITCHED OFF
-- IS OPEN: NOT COMPUTED, NOT READ, AND WHETHER IT EXCEEDS HALF IS UNDECIDED
HERE; NO VERDICT RESTS ON IT.  FIVE READINGS KEEP A REMAINDER, EVERY ONE BUT
SWITCH-ON: DISPLACEMENT AND QUANTA (THE PAIR ROUTE, PRICED), CREATION (THE
ENERGY MUST COME IN THE CARRIER), STOCK (RECONSTRUCTION FROM STOCK, WHERE NO
MASS FORMS) AND TEMPLATE (THE HELD-SEAT RELEASE ROUTE, PRICED).

  M65-1 PRESENCE.  The consideration holds, and more strongly than M put it.
     An electron of the measured mass REQUIRES a nonzero Higgs field where it
     is, because fermion masses are proportional to phi (READ).  With the vev
     uniform (P-UNIFORM, a named premise) the condition holds everywhere, with
     or without the elements, so it cannot be what triggers anything.  C1: the
     field is not switched on by arrival, because it is already on.  That
     answers SWITCH-ON, and TEMPLATE below.  C5, PRIOR MASS: on the STOCK
     reading the elements are at the seat before anything arrives, and
     elements of measured mass REQUIRE phi != 0 where they are, so they
     already carry their Higgs-given mass; the trigger gives them nothing,
     and no mass forms.  On H-PRESENT that case needs NO P-UNIFORM: the
     elements' own measured masses fix phi at their location (H-TREE,
     H-PRESENT).  It answers STOCK read with the elements present as
     elements.  STOCK's complement, TEMPLATE -- templates at the seat
     without all or part of their HIGGS-GIVEN mass (|phi| < v there before
     arrival), for the trigger to restore -- is refused by C1: on P-UNIFORM
     the unsourced field at the seat is at v; any lower value needs a local
     source (D15, D16), and on H-UNSOURCED-SEAT nothing holds one there
     before arrival (M's sentence names no such source; only the information
     arrives); H-TREE.  Without H-UNSOURCED-SEAT, TEMPLATE keeps a priced
     remainder, the held-seat release route (section 5 (d)).  H-PRESENT or
     not, the split is three-way: before arrival the seat is r = |phi|/v < 1
     (TEMPLATE, C1), r = 1 (STOCK on H-PRESENT, C5) or r > 1 (neither
     reading's claim: the trigger has nothing to give; holding r > 1 needs a
     source outside D20's model).  Under the EXCITATION reading the
     field CAN be triggered: a local source displaces phi (D15, D16), at a
     price, and within D20's model a source of positive rest energy can only
     LOWER |phi|, and every Yukawa mass with it.  What excitation makes forms
     no net baryon number (C3).  It CAN form atomic mass as matter-antimatter
     pairs, with the carrier paying at least the pair floor and the
     antibaryons held apart; the Higgs is then an intermediary, not the
     source.  That is EXCITATION's remainder, the pair route, and it is
     priced (section 4), not dismissed.
  M65-2 SHARE.  C2: the Higgs gives the payload 3.010e-4 of its mass through
     the electrons (H-TREE: their mass is proportional to phi); in the
     nucleons, AT FIRST ORDER (H-LINEAR), the quark-mass part is 9.28 % (FLAG
     2+1) to 10.85 % (FLAG 2+1+1) of their mass by the READ sigma terms.  The
     largest central reading of all the READ rows is Ji's quark-mass term in
     his m_s -> 0 column, 17.04 % of the nucleon.  Only if the heavy-quark
     trace-anomaly coupling is counted, which is CONTESTED as a mass share,
     does it reach 0.2944 to 0.3066.
     Every row puts the Higgs below half of the atomic mass -- as a
     FIRST-ORDER (sigma-term) response at the physical point with the QCD
     scale held fixed (H-LINEAR).  At first order the rest is QCD.  THE
     FINITE SHARE, with the field switched off, where the heavy-quark
     thresholds and the QCD scale move too, is OPEN: not computed, not read,
     and whether it exceeds half is undecided here.  C2 answers DISPLACEMENT,
     and there a SMALL displacement only; a finite one is OPEN, and C3
     carries the refusal regardless: a small displacement of phi is exactly
     a first-order response, so H-LINEAR applies and is the right measure
     there, and at first order, with the QCD scale held fixed (H-LINEAR),
     only the quark-mass part moves.  It does NOT answer SWITCH-ON, STOCK or
     TEMPLATE, which ask what the field GIVES, the finite counterfactual C2
     does not measure.  Nor does it
     answer CREATION or QUANTA: if the triggered field or its quanta paid for
     the mass, the QCD share would be paid out of that same energy, so how
     the nucleon's mass divides says nothing there.
  M65-3 THE ONLY CANDIDATE SOURCE IN M'S SENTENCE.  C4: the triggered Higgs
     field has no energy to give.  Its energy density about v is
     (1/2)phi_t^2 + (1/2)|grad phi|^2 + rho_EW eps^2(2-eps)^2, a sum of
     squares, zero only in the vacuum (THEOREM on H-TREE-V, asked of
     higgs.T_scalar and excite, for the real scalar higgs.T_scalar models;
     that the doublet's other components and the gauge fields add only
     non-negative terms is H-REAL, claimed and not computed).  Any change of
     phi about v COSTS energy.  The one way a Higgs field could RELEASE
     energy is decay of a metastable electroweak vacuum to a deeper one.  At
     the central measured masses metastability is preferred but not
     established: "we cannot conclusively establish the fate of the EW
     vacuum, although metastability is now preferred at 99.3% CL", and "the
     main source of uncertainty" is the top mass (READ).  If it decays, a
     bubble of true vacuum expands at near the speed of light, with "the
     different masses of fundamental particles in the bubble interior"
     (READ).  INFERENCE from that READ text: decay forms no atomic mass at
     the seat, since it replaces the vacuum in which atomic masses have their
     values.  Stable or metastable, then, the field supplies no mass-energy
     at the seat.  The energy must come in the signal's CARRIER: Mc^2 =
     6.2913e18 J, 1504 megatons, or 1.9975 Mc^2 with B and L conserved.
     This answers the CREATION reading.
  M65-4 CONSERVATION.  C3: every Yukawa term is a fermion bilinear, so no
     Higgs coupling carries B or L.  The payload holds 4.2109e28 baryons and
     2.3132e28 electrons, so B - L = N_n = 1.8977e28.  With B and L conserved,
     making it from energy needs at least 1.9975 Mc^2, and 4.2109e28 units of
     antibaryon number must be held apart: that is the pair route, priced.  The
     only Standard Model violation of B comes from the SU(2) anomaly, with
     Delta B = Delta L = 3 per unit of Chern-Simons number.  At zero
     temperature it is INSTANTON tunnelling, suppressed by 10^-160.95 per
     transition (a figure that inherits NAMED-NOT-READ through v); the payload
     needs 1.4036e28 transitions.  Thermally it goes over the SPHALERON
     (whether two-particle collisions at high energy do is CONTESTED, section
     4), a gauge-Higgs saddle whose height the vev sets, 3226 times the rest
     energy of the 3 baryons one transition makes.  Above T_c the thermal
     sphaleron transitions are unsuppressed and the vev is approximately zero.
     Below T_c they keep running down to T* = 131.7 GeV, where the vev is
     finite (READ).  At collider energies the two-particle rate is CONTESTED:
     the prevalent semiclassical results find it exponentially suppressed,
     resting on conjectures and assumptions they state as unproven, and Tye and
     Wong dissent, stating that "both estimates involve assumptions based on
     intuitions as well as approximations remaining to be fully justified" and
     calling their own figure "only an order of magnitude guesstimate"; it is
     recorded, not resolved, and nothing is refused on it.  C3 answers
     DISPLACEMENT, QUANTA and CREATION.
  M65-5 WHAT SURVIVES.  Reconstruction from destination stock (D25,
     transit.CARRIES_SUBSTANCE = False).  That is the STOCK reading, less its
     claim that mass forms: no mass forms, and the Higgs triggers nothing.
     Two routes on which atomic mass CAN form also survive, PRICED, not
     dismissed: the pair route (EXCITATION's remainder) and the anomaly
     route.  So does TEMPLATE's remainder where H-UNSOURCED-SEAT fails, the
     held-seat release route, PRICED: a seat prepared in advance with a
     source holding |phi| below v, released on arrival, restores the
     Higgs-given mass of elements already there; it forms no baryons.

===============================================================================
1.  M65-1  PRESENCE -- SWITCH-ON, STOCK, TEMPLATE AND EXCITATION
===============================================================================

THE CONSIDERATION, COMPUTED.  At tree level in unitary gauge, "the masses of the
W+/- and Z0 weak vector bosons and the fermions are proportional to phi"
(Morrissey & Ramsey-Musolf 1206.2942 p.4, READ).  So m_f = y_f v/sqrt(2).  If
m_f > 0 at a place, then phi != 0 at that place.  The electron mass in the
capture is 0.510998951 MeV (READ).  Wherever the payload's elements exist with
their measured masses, therefore, the Higgs field has its vev.  THEOREM, on
H-TREE.

The Yukawas y_f = sqrt(2) m_f / v are computed from the READ masses for all
nine charged fermions.  The top's is 0.9914 and the electron's is 2.935e-6.
Every y_f inherits G_F's NAMED-NOT-READ through v = higgs.vev().

THE SWITCH-ON READING.  P-UNIFORM: where nothing sources it, the vev takes one
value everywhere.  This is a PREMISE, named.  It is higgs.py's caveat (b) as it
survives DOCKET 63 F3 (the prohibition was withdrawn, the price kept), and it
is supported by the measured constancy of fermion masses, which is not read
here.  No owner boolean asserts it, so none is asked for it.  On P-UNIFORM the
field at the seat before arrival already has the value it has wherever massive
matter is measured, so arrival has nothing to switch on (C1).

THE STOCK READING: PRIOR MASS (C5).  STOCK puts the elements at the seat before
anything arrives, and asks the triggered field to give them their mass.  But an
element present with its measured mass REQUIRES phi != 0 where it is, by the
same READ proportionality, so the elements at the seat already carry their
Higgs-given mass; the trigger has nothing left to give them, and no mass forms.
On H-PRESENT this needs NO P-UNIFORM: it does not carry the field's value from
anywhere else, because the elements' own measured masses fix phi at their
location.  It rests on H-TREE and on H-PRESENT (an element present at the seat
is present with its measured mass), and answers STOCK in that case only.

THE TEMPLATE READING (C1).  The complement puts templates at the seat without
all or part of their HIGGS-GIVEN mass (|phi| < v there before arrival), for the
trigger to restore.  (With phi = 0 the nucleons would keep their non-Higgs
mass, so what is missing is the Higgs-given part.)  C1 refuses it: on P-UNIFORM
the unsourced field at the seat is at v; any lower value needs a local source
(D15, D16), and on H-UNSOURCED-SEAT nothing holds one there before arrival
(M's sentence names no such source; only the information arrives); H-TREE.  So
the no-P-UNIFORM claim holds for STOCK on H-PRESENT and not for its complement.
H-UNSOURCED-SEAT is not vacuous: within D20's model a positive source is an
equilibrium on 0 < |phi| < v ((a) below) and, within excite's section-3
model (source rest mass proportional to phi), a stable hold only on
0.5774 v < |phi| < v.  Where it fails, TEMPLATE keeps a priced remainder,
the held-seat release route (section 5 (d)), on that range only, within
excite's section-3 model.  H-PRESENT
or not, the split is three-way: before arrival the seat is r = |phi|/v < 1
(TEMPLATE, C1), r = 1
(STOCK on H-PRESENT, C5) or r > 1 (neither reading's claim: the trigger has
nothing to give; holding r > 1 needs a source outside D20's model).  Giving
present elements MORE mass would need raising |phi|, which is a displacement,
and DISPLACEMENT answers that.

THE EXCITATION READING.  There are exactly three ways to change a field that is
already on, and each is asked of its owner:

  (a) a RADIAL displacement.  It returns to v at rate exactly m_h outside its
      source (D15, excite.TAIL_RATE_IS_MASS), over hbar/(m_h c) =
      1.577e-18 m.  Inside the source it is -J/m_h^2, ultralocal (D16,
      excite.DISPLACEMENT_IS_ULTRALOCAL).  A signal that brings no source to
      the seat changes nothing there.  WITHIN D20'S MODEL, a source whose
      mass comes from phi holds phi = v(1 - eps) with rest energy
      4 rho_EW eps(2-eps)(1-eps)^2 (excite.holding_terms).  The factorisation
      is exact, so its sign is settled on every interval between its roots
      0, 1, 1, 2: positive exactly for 0 < eps < 2, eps != 1, which is
      0 < |phi| < v.  So a source of POSITIVE rest energy can only LOWER |phi|,
      and every Yukawa mass by the same fraction.  Raising |phi| above v,
      whether eps < 0 or eps > 2, would need a source of negative rest
      energy.  Holding eps costs 4(1-eps)^2/(eps(2-eps)) joules of source per
      joule of field (excite.holding_ratio), 2/eps at small eps.
  (b) a displacement along a GAUGE direction.  It changes no mass and no
      derivative-free gauge-invariant local observable (D19,
      excite.FLAT_DIRECTIONS_ARE_INERT).
  (c) making Higgs QUANTA.  Each costs m_h c^2 and lives about 2e-22 s
      (excite.QUANTUM_LIFETIME_S, one significant figure by excite's refusal
      6).  A number state has <delta phi> = 0 (excite section 0).  Their
      decays carry no net B or L (C3, section 4).  They CAN end in atomic
      mass, as matter with its antimatter: the pair route of section 4, paid
      for by the carrier, with the Higgs an intermediary, not the source.

So the field CAN be triggered, in the sense of excited.  Doing so costs energy
(section 3), lowers |phi| or makes quanta, and forms no net baryon number.
What remains of EXCITATION is the pair route, priced in section 4.
And where a displacement does change m_e, the result is an exact dilation, not
new mass (D18, excite.ELECTRON_MASS_IS_A_RULER: "THEOREM given alpha fixed (H2)
and clamped point nuclei").

This is NOT higgs.py's withdrawn "cannot be switched on in one place" (DOCKET 63
F3; higgs.CANNOT_BE_SWITCHED_ON_IN_ONE_PLACE = False, asked).  A source does
displace the vev locally, at the price D20 states.  What fails is the SWITCH:
there is no off state at the seat for arrival to end.

    SO THE CONSIDERATION IS TRUE AND, ON P-UNIFORM, DISCRIMINATES NOTHING.  It
    is true at the seat because it is true everywhere.  This is nopath.py's
    Campbell-Magaard lesson in a second setting: a condition that always holds
    carries no information about any one place.

===============================================================================
2.  M65-2  SHARE -- WHAT PART OF THE PAYLOAD'S MASS THE HIGGS SUPPLIES
===============================================================================

The payload is stock.HUMAN (ICRP Reference Man, CITED by stock.py) at
stock.py's own default of 70 kg, asked through inspect (regenerated).  No
fraction is retyped.  The atom count of element e is f_e M / (A_r(e) u).  The
electrons number Z per atom, with Z READ from the AME2020 capture through
gravity.symbol_to_Z().  The nucleons number A per atom, on H-A.  Every count,
and so every payload share below, INHERITS NAMED-NOT-READ through u =
gravity.U_KG and stock.ATOMIC_MASS.

THE MEASURES OF THE NUCLEONS' HIGGS PART, KEPT APART:

  NAIVE VALENCE.  (2m_u + m_d)/m_p = 0.961 % and (m_u + 2m_d)/m_n = 1.230 %,
     from the capture's current-quark masses (READ).  This counts the valence
     quarks' own masses and nothing else.
  SIGMA TERMS.  The FLAG 2024 averages, READ with their locators.  sigma_piN
     is 60.9(6.5) MeV at N_f = 2+1+1 and 42.2(2.4) MeV at N_f = 2+1.  sigma_s
     is 41.0(8.8) and 44.9(6.4) MeV.  Each gives f_l = (sigma_piN + sigma_s)/
     m_N = 10.85 % and 9.28 %, with m_N = (m_p + m_n)/2 READ.  "The
     sigma_piN,s,c give the shift in M_N due to nonzero light-, strange- and
     charm-quark masses" (FLAG).  AT FIRST ORDER (H-LINEAR: the response at
     the physical point, with the QCD scale held fixed) this is the part of
     the nucleon mass that moves with the quark masses, i.e. with the Higgs;
     it is not the finite share the field gives, which is OPEN (below).
     Both averages are READ,
     and the tension between them is recorded: "there is now a 2.7 sigma
     difference between the N_f = 2 + 1 and N_f = 2 + 1 + 1 FLAG averages"
     (FLAG p.273).  FLAG finds it "unlikely to be due to the inclusion of
     charm quarks in the sea" and names the open issue: "The control of
     excited-state contributions remains an issue", citing PNDME 21's
     narrow-width prior; and "The N_f = 2 + 1 + 1 lattice average is in
     agreement with Hoferichter et al." (FLAG p.274).  Which is right is
     CONTESTED, and neither is chosen: both are printed and
     the verdict uses the larger.  The chiQCD lattice gives 9(2)(1)% (READ).
  JI.  Table I of Ji's decomposition gives the quark mass term b as 160 MeV
     (m_s -> 0) and 110 MeV (m_s -> infinity), READ: 17.04 % and 11.72 % of
     the nucleon.  His prose rounds this to "about 1/8".  Ji rounded every
     entry to 10 MeV; the errors he did not show (higher orders, the sigma
     term, the current quark masses) come to 5 to 10 MeV (READ).  His
     largest uncertainty is larger: "The largest uncertainty is from the
     matrix element <P|m_s ss|P>, which could be larger than the difference
     of the two estimates shown" (p.6, READ), and that difference is 50 MeV.
  HEAVY QUARKS.  The SVZ relation gives f_TQ = (2/27)(1 - f_l) for each of c,
     b, t (Ellis-Olive-Savage eq. (10), READ; SVZ 1978 CITED).  The coupling
     sum is 2/9 + (7/9) f_l, which is 0.3066 and 0.2944 here against
     Hoferichter et al.'s 0.305(9) (READ).  The algebra is checked exactly
     over Fraction.  AS THE SOURCE STATES IT this is the Higgs's COUPLING to
     the nucleon, and Ji: "the contributions cancel each other in the limit of
     m_f -> infinity".  FLAG also prints a charm sigma term, up to 107(22) MeV
     (ETM 19, READ).  Counting heavy-quark terms as mass the Higgs MAKES is
     CONTESTED.  They are printed with that label and never added to the READ
     rows.

AT FIRST ORDER (H-LINEAR) THE REMAINDER IS QCD: 1 - f_l of each nucleon's
mass is not light-quark-mass mass.  Whether the heavy-quark terms inside it
count as Higgs-given is CONTESTED (above), and the finite share is OPEN.
chiQCD's decomposition (quark energy, glue energy, and a quarter of the trace
anomaly at 23(1)(1)%) is READ.  The nuclear binding is computed as the closure
term: nucleon rest masses plus electron rest masses, minus the listed payload.
It comes to 0.5020 kg, the nuclear binding net of Coulomb.  It is the one
figure here that H-A moves materially: raising every mean nucleon number by
0.01 moves it by 0.1124 kg.  So it is printed to close the books, and nothing
turns on it.

    NO SINGLE HIGGS SHARE IS PRINTED.  C2 uses only the LARGEST CENTRAL
    READING, computed twice: over the READ rows alone (0.1719 of the
    payload) and over all of them (0.3090).  It is a largest central value,
    not a bound: uncertainties are dropped.  AN ILLUSTRATION OF MARGIN, not
    a bound either: FLAG's rows moved up by 3 sigma linearly (3 sigma is
    this file's choice, not a stated uncertainty), Ji's by his 10 MeV of
    omitted error plus that difference of his two estimates, which he
    says the strange matrix element's uncertainty "could be larger than".
    The READ rows then reach 0.2362.  Nothing near one half AT FIRST ORDER.

THE FINITE SHARE IS OPEN.  What the field GIVES -- the nucleon mass with phi at
v, less the nucleon mass with phi switched off -- is a finite counterfactual.
With the field off the heavy-quark thresholds move and the QCD scale moves with
them, so the first-order measures above do not settle it.  It is NOT computed
and NOT read here, and whether it exceeds half is UNDECIDED here.  No verdict
rests on it: STOCK is refused on prior mass (C5), SWITCH-ON and TEMPLATE on C1,
and C2 is listed only on DISPLACEMENT, and there for a SMALL displacement only;
a finite one is OPEN, and C3 carries the refusal regardless: a small
displacement of phi is exactly a first-order response.  It is carried as an
OPEN item, a candidate question for a future docket (S10 (open)): on M's
ruling M-D65-2 it is carried inside ledger row S10's note, not as a row of its
own.

===============================================================================
3.  M65-3  ENERGY -- THE SOURCE M'S SENTENCE IMPLIES, AND THE CARRIER
===============================================================================

THE TRIGGERED FIELD HAS NO ENERGY TO GIVE ABOUT v.  For the Higgs field the
energy density, asked of higgs.T_scalar, is

    T_00 = (1/2) phi_t^2 + (1/2) |grad phi|^2 + V(phi).

The selftest checks this decomposition exactly, on a rational grid of five
points per axis (at least three are needed, and the function refuses fewer),
which settles a polynomial of degree two in each derivative.  Measured from the
vacuum, V(phi) - V(v) = rho_EW eps^2 (2 - eps)^2 with phi = v(1 - eps)
(excite.FIELD_POLY, equal to excite.FIELD_CLOSED); that is the square of
eps(2 - eps).  Every term is a square, so the field's energy above the vacuum
is >= 0, and zero only where phi_t = 0, grad phi = 0 and |phi| = v.  ANY change
of phi about v COSTS energy; the present vacuum has none to give up.  THEOREM,
on the tree-level potential (H-TREE-V), for the real scalar that higgs.T_scalar
models.  That the doublet's other components and the gauge fields add only
non-negative terms is claimed, NOT computed and NOT read: it is the named
hypothesis H-REAL (section 6), and C4 and D29 carry it.

THE ONE WAY A HIGGS FIELD COULD RELEASE ENERGY.  Beyond tree level, at the
central measured masses, the potential has a deeper minimum at large field:
"the Higgs vacuum does not reside in the configuration of minimal energy, but
in a metastable state close to a phase transition" (Buttazzo et al. 1307.3536
p.3, READ).  The instability sets in at "10^10-10^12 GeV" in field value
(p.32).  STATUS, AS THE SOURCE GIVES IT: vacuum stability up to the Planck
scale "is excluded at 2.8 sigma", the stability condition is
M_t < (171.53 +/- 0.42) GeV, and "the main source of uncertainty in eq. (64)
comes from M_t" (p.20); "we cannot conclusively establish the fate of the EW
vacuum" (p.31).  Degrassi et al. 1205.6497 give the earlier 2 sigma, for
M_h < 126 GeV (READ).
So metastability is PREFERRED, not established, and it turns on the top mass.
If the vacuum is metastable, "the SM vacuum is likely to survive for times that
are enormously longer than any significant astrophysical age" (p.31).  If a
bubble of true vacuum nucleates, it expands "at near the speed of light",
"releasing energy into the bubble wall", with "the different masses of
fundamental particles in the bubble interior" and a gravitational collapse of
the bubble (Markkanen, Rajantie, Stopyra 1809.06923 p.24, READ); "it expands at
the speed of light, destroying everything in its way" (p.54).

WHAT THAT MEANS FOR M'S MECHANISM, EXACTLY.  If the SM vacuum is stable, the
triggered field has no energy to release at all.  If it is metastable, its one
release is vacuum decay.  That it forms no atomic mass at the seat is an
INFERENCE from the READ text, not a sentence of it: inside the bubble
fundamental particles have different masses, the energy goes into a wall moving
at near c, and the bubble destroys what it meets.  What matters for C4 is that
v stays a local minimum, which both cases keep.  Whether any local process at a
seat could nucleate such a bubble is NOT computed here.  Either way the Higgs
field supplies no mass-energy at the seat, so the top-mass dependence does not
reach C4.

THE CARRIER.  A signal carries energy only through its carrier.  For mass to
form, the carrier must deliver at least Mc^2 = 6.2913e18 J
(warpfolder.rest_energy_j) if B is free.  If B and L are conserved it must
deliver 1.9975 Mc^2 (section 4).  That is energy conservation.  THEOREM.

SUPPORTING NOTE N-INFO (no verdict rests on it).  M's sentence makes the
information the trigger, not the source, so this answers a link M did not
state.  By energy conservation a bit brings only its carrier's energy.  The two
information bounds confirm that neither supplies any:
  LANDAUER, at the CMB temperature.  At least k_B T ln 2 of heat per bit
     ERASED (Lloyd, Bennett; READ), computed by nopath.landauer_energy.  At
     permute.T_CMB = 2.7255 K that is 2.608e-23 J per bit, so Mc^2 equals the
     minimum heat of erasing 2.4120e41 bits.  Heat has B = 0.  Reversible
     transfer has no minimum cost (nopath.LANDAUER_IS_THE_WEAKER_HALF), and an
     inequality on dissipation turns nothing into mass.
  BEKENSTEIN, for a body of energy Mc^2 within R = 1 m (H-R).  The bound
     is S <= 2 pi E R/(hbar c) (READ), here 1.8038e45 bits in bit units
     (nopath.bekenstein_bits).  WHAT IT IS, held with its caution: an entropy
     bound whose widely accepted proven version is Casini's (one of several
     viable formulations), "an
     information-theoretic statement about state distinguishability"; it is
     "often interpreted as a fundamental limit on the information that can be
     stored by physical objects", but "this interpretation remains folklore
     rather than established fact" (Hayden and Wang, 2309.07436v3, abstract
     p.1 and pp.2-3, READ).  So this file does NOT read the figure as the
     most information such a body can hold.  In either reading it bounds by
     energy; it supplies none.
     The ratio of the two counts is 2 pi R k_B T / (hbar c) = 7478,
     INDEPENDENT OF THE MASS.  They break even only for R < hbar c/(2 pi k_B
     T) = 0.134 mm.  How many bits a human actually is: no reliable figure
     exists (section 9), and this file quotes none.

===============================================================================
4.  M65-4  CONSERVATION
===============================================================================

THE COUNT.  B = 4.2109e28 and L = N_e = 2.3132e28.  N_p = N_e because the atoms
are neutral.  So N_n = 1.8977e28 and B - L = N_n.  Cross-check: B against
warpfolder's M/m_p is 1.0062.  The excess is the nuclear binding, net of the
neutrons' extra mass and the electrons.

FROM ENERGY, WITH B AND L CONSERVED.  Every Yukawa term is a fermion bilinear.
The selftest computes B = L = 0 for each one, so no Higgs coupling carries B or
L (C3).  Higgs couplings DO create fermions, in fermion-antifermion pairs;
what they cannot create is net baryon number.  So the payload must come with
antimatter carrying B' = -B.  Its mirror costs exactly 2 Mc^2 (CPT).  The
rigorous floor is Mc^2 + B mu_min c^2, where mu_min = 930.1746 MeV is the least
nuclear mass per nucleon among the AME2020 capture's measured nuclides (56Fe).
That gives 1.9975 Mc^2.  (H-AME: no bound state carries baryon number more
cheaply.  Gravitational binding could, but it is of order G M/(R c^2) = 5.2e-26
of the rest energy at R = 1 m: negligible at payload scale.)  AND THE ANTIMATTER
MUST GO SOMEWHERE: at least 4.2109e28 units of antibaryon number, held apart
from all matter.

THE PAIR ROUTE, PRICED.  This is what remains of the EXCITATION reading, and
it is listed in what survives.  Atomic mass CAN form as matter with its
antimatter.  The carrier supplies at least the pair floor, 1.9975 Mc^2; the
antibaryons, 4.2109e28 units of antibaryon number, are held apart; the Higgs,
where it appears (a displacement relaxing, or its quanta decaying), is an
intermediary, not the source, since it has no energy to give about v (C4).
Nothing is refused on the antimatter by-product: it is priced, and whether it
can be held apart is not computed here.

B - L.  The payload's B - L = N_n = 1.8977e28 must be balanced by -N_n outside
it.  On the pair route that balance is the antimatter.  On a B-violating,
B-L-conserving route that makes no antibaryons, it is N_n extra leptons.

WITH B VIOLATED: THE ANOMALY ROUTE.  B is violated in the Standard Model by the
SU(2) anomaly: the fermion numbers change by the gauge field's topological
number N[A] (Rubakov & Shaposhnikov eqs. (2.2)-(2.4), READ), so the violation
is a property of the gauge field.  The selection rule is READ in the source's
own order: "the factor 1/3 comes from the baryon number of a quark, while the
factor 3 . 3 is due to colour and number of generations", so "Delta N_e =
Delta N_mu = Delta N_tau = (1/3) Delta B ; (B - L) is conserved while (B + L) is
violated".  That is Delta B = Delta L = N_f = 3 per transition, with N_f
counted from the capture's charged leptons.  The Higgs's part is the barrier:
the sphaleron is "the static saddle point solution to the Yang-Mills-Higgs
equations" (READ), with E_sph = (2 m_W/alpha_W) B(m_H/m_W) = (4 pi v/g) B, set
by the vev.  Two regimes, kept apart:

  ZERO TEMPERATURE: INSTANTON TUNNELLING.  "At zero energies and
     temperatures, the transition between vacua with different n[omega] is a
     tunnelling event which is described by instantons" (READ).
     alpha_W = g^2/4 pi, with g = 2 m_W/v, m_W READ and v from higgs.vev():
     1/29.49.  It INHERITS NAMED-NOT-READ through v.  The suppression,
     exactly as the source states it, exp(-4 pi/alpha_W) = exp(-16 pi^2/g^2):
     10^-160.95 per transition.  No prefactor was read, so NO RATE IS
     PRINTED.  To make the payload's 1.4036e28 transitions, (attempts) x
     (prefactor) must reach 10^189.10.  RECORDED, NOT REPAIRED: Rubakov &
     Shaposhnikov's own eq. (2.8) prints 10^-170 at alpha_W = 1/29, where the
     arithmetic gives 10^-158.27, 11.73 decades apart; Tye-Wong's p.2
     pairing is 1.73 decades off (section 8).
  OVER THE BARRIER: THE SPHALERON.  E_sph = 4.740 TeV x B, with B between
     1.56 and 2.72 (READ).  The READ values at the measured Higgs mass are
     9.11 TeV (Tye-Wong, pure SU(2)), 9.08 TeV (Funakubo et al.) and 9.0 TeV
     (with U(1)).  At 9.08 TeV the barrier is 3226 times the rest energy of
     the 3 baryons one transition makes.  E_sph is a barrier HEIGHT, not a
     rest-mass cost: over the payload's transitions the heights sum to 3246
     Mc^2, and whether that energy is recovered is not computed.
  THERMAL, ABOVE T_c = 159.5 +/- 1.5 GeV (D'Onofrio-Rummukainen abstract,
     READ), which is 1.851e15 K.  The rate is unsuppressed: the READ figure
     is Gamma/T^4 = (8.0 +/- 1.3) x 10^-7.  The source's form (18 +/- 3)
     alpha_W^5 absorbs factors of ln alpha_W into its constant, so at this
     file's alpha_W, 8.07e-7, it is a cross-check only.  The Higgs field
     there is "approximately zero" (READ), and fermion masses are
     proportional to phi, so the Yukawa masses are approximately zero above
     T_c: on the approximate-zero reading, and with H-THERM not asserted.
     This is warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY, asked.
  THERMAL, BELOW T_c: THE BROKEN-PHASE WINDOW.  B freezes out at T* = 131.7
     GeV (READ), BELOW T_c, so transitions keep running in T* < T < T_c
     where the vev is finite: the broken phase "at T < T_c GeV where it is
     finite" (READ).  The READ fit, "in the physically interesting
     temperature range 130 GeV < T < T_c", is log(Gamma/T^4) = (0.83 +/-
     0.01)T/GeV - (147.7 +/- 1.9).  Its T_c is its own paper's, "T_c = (159
     +/- 1) GeV" (1404.3565 abstract, READ), and broken_phase_ln_rate() is
     bounded by that 159 GeV, not by 1508.07161's 159.5.  The fit was
     measured "In the interval 140 <~ T <~ 155 GeV" (p.3) and extended "down
     to T ~ 130 GeV" on its match to perturbation theory (p.4), so the
     report's 159 GeV lies at the stated range's edge and outside the
     measured interval.  At T* that is -38.39, a rate of 2.13e-17 T^4; at
     155 GeV, -19.05.  In this window fermions carry nonzero Yukawa masses,
     whose size v(T) this file does not compute.
  In the Standard Model alone the crossover yields no net asymmetry: "EWBG
     is unable to explain the observed baryon asymmetry within the SM alone"
     (READ).
  AT COLLIDER ENERGIES: CONTESTED, WITH THE BALANCE AS THE SOURCES GIVE IT.
     This is the two-particle rate at energies near and above E_sph, not the
     instanton's T = 0 factor and not the thermal sphaleron rate.
     (i) The prevalent result.  Bezrukov, Levkov, Rebbi, Rubakov and Tinyakov
     find that B + L violation "remains exponentially suppressed up to very
     high energies of at least 30 sphaleron masses (250 TeV)" (hep-ph/0304180
     and hep-ph/0305300, abstracts p.1, READ), for s-wave scattering, on the
     conjecture that the two-particle exponent is the few-particle limit,
     "although not proven rigorously" (hep-ph/0304180 p.2, READ).  Khoze and
     Milne, computing from the instanton side, find the 't Hooft exponent
     reduced by "not more than ~ 30%" and instantons "exponentially
     suppressed by at least e^(-(4 pi/alpha_w) 0.70)" (2011.07167 printed
     p.9 and p.16, READ), while "there is no rigorous proof of
     exponentiation" (p.13, READ) and the result is "based in part on an
     assumption that there are no additional exponentially growing"
     contributions at higher orders (p.15, READ).  These are results resting
     on conjectures and assumptions their authors state as unproven, not
     theorems.  The dissent is no firmer, by its own account: Tye and Wong
     write that "both estimates involve assumptions based on intuitions as
     well as approximations remaining to be fully justified" (1710.07223
     p.2, CONTESTED), and call their own figure "only an order of magnitude
     guesstimate" (p.3).
     (ii) The dissent.  Tye and Wong claim B + L violation "without the
     exponential tunneling suppression" above the barrier (1505.03690,
     CONTESTED); their later paper agrees "with this estimate for a single
     sphaleron" and claims multi-sphaleron resonance changes it, and itself
     calls the other side "the prevalent picture" (1710.07223 pp.2 and 11,
     CONTESTED).  Funakubo, Fuyuto and Senaha rebut it with an overlap
     suppression of about 10^-155, found "in the leading order of the WKB
     approximation", that remains "regardless of the band structure"
     (1612.05431 p.4, READ).  The rebuttal is not conceded: 1710.07223 cites
     it (its ref. [27], p.13) and replies to it on p.3 -- "As argued at times
     in the literature (see e.g., Ref.[26] and recently in [27])", then
     "However, the above argument is somewhat misleading" -- and keeps the
     claim.
     (iii) Experiment.  CMS, with 35.9 fb^-1 at 13 TeV, sets "An upper limit
     of 0.021" on the fraction of quark-quark interactions above 9 TeV that
     make the transition (1805.06013 abstract, READ).  An upper limit cannot
     contradict an exponentially small rate, and Tye-Wong's own event count
     is "A very crude order of magnitude estimate" (READ), so the experiment
     does not decide it.
     NOT RESOLVED HERE, AND NO REFUSAL RESTS ON IT.

===============================================================================
5.  M65-5  VERDICT, READING BY READING, FROM PINNED BOOLEANS WITH OWNERS
===============================================================================

Each count is a boolean with an owner; derive_reading() reads the booleans a
reading turns on, and derive_verdict() refuses a reading only on a count that
does not rest on a CONTESTED figure alone.  The selftest builds that case and
checks it returns OPEN.  Nothing in the verdict is typed.

  C1 FIELD_SWITCHED_ON_BY_ARRIVAL = False       (M65-1; D15, D16, P-UNIFORM;
                                                 on TEMPLATE, H-UNSOURCED-SEAT)
  C2 HIGGS_SUPPLIES_MOST_ATOMIC_MASS = False    (M65-2; READ rows alone; first
                                                 order, H-LINEAR)
  C3 HIGGS_COUPLING_CARRIES_B_OR_L = False      (M65-4; Yukawa charges)
  C4 HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY = False (M65-3; T_00, V on H-TREE-V
                                                 and H-REAL; decay by inference)
  C5 TRIGGER_GIVES_THE_ELEMENTS_THEIR_MASS = False (M65-1; PRIOR MASS: READ
                                                 masses, H-TREE, H-PRESENT; no
                                                 P-UNIFORM on H-PRESENT)

  READING       COUNTS THAT ANSWER IT   RESULT
  SWITCH-ON     C1                      REFUSED on P-UNIFORM
  DISPLACEMENT  C2, C3                  REFUSED as net formation (C3); C2
                                        answers a SMALL displacement only; a
                                        finite one is OPEN, and C3 carries the
                                        refusal regardless; what remains is
                                        the pair route (survivor b), PRICED
  QUANTA        C3                      REFUSED as net formation; what
                                        remains is the pair route (survivor
                                        b), PRICED
  CREATION      C4, C3                  REFUSED; the energy must come in the
                                        carrier
  STOCK         C5                      REFUSED on prior mass (H-PRESENT);
                                        what remains is survivor (a), where
                                        no mass forms
  TEMPLATE      C1                      REFUSED on P-UNIFORM and
                                        H-UNSOURCED-SEAT (|phi| < v at the
                                        seat needs a local source, D15, D16,
                                        which nothing holds there before
                                        arrival); what remains is the
                                        held-seat release route (survivor d),
                                        PRICED

WHY EACH COUNT ANSWERS, AND WHY EACH OMITTED ONE DOES NOT (READING_REASONS,
checked in the selftest: every count, on every reading, carries a stated
reason, listed or omitted).  C2 answers DISPLACEMENT, and there a SMALL
displacement only; a finite one is OPEN, and C3 carries the refusal
regardless: a small displacement of phi is exactly a first-order response, so
H-LINEAR applies and is the right measure there, and at first order, with the
QCD scale held fixed (H-LINEAR), only the quark-mass part moves.  C2 does NOT
answer SWITCH-ON, STOCK or TEMPLATE: they ask what the field GIVES, a finite
counterfactual with the field off or below v, which C2 does not measure and
which is OPEN.  C2 does NOT answer CREATION or QUANTA: there the energy of the
whole mass would come from the field or its quanta, the QCD share included, so
how the nucleon's mass divides is silent.  C3 answers DISPLACEMENT, QUANTA and
CREATION because each makes matter from the field or its energy, and no Higgs
coupling carries net B.  C4 answers CREATION only: the other readings do not
claim the field pays.  C1 answers SWITCH-ON and TEMPLATE: each needs the field
off, or below v, at the seat before arrival, and on P-UNIFORM the unsourced
field at the seat is at v; any lower value needs a local source (D15, D16),
which on H-UNSOURCED-SEAT nothing holds there.  C5 answers STOCK only: there
the elements are at the seat already, present as elements with their measured
mass (H-PRESENT), and those masses fix phi where they are.

C1 is the only count on SWITCH-ON and on TEMPLATE, C3 the only count on QUANTA
and C5 the only count on STOCK, so each of those refusals rests on one count.
The selftest shows it: with C1 reversed SWITCH-ON and TEMPLATE stand; with C3
reversed QUANTA stands; with C5 reversed STOCK stands, and TEMPLATE is still
refused on C1.  The one count of SWITCH-ON and of TEMPLATE rests on the premise
P-UNIFORM; TEMPLATE's also on H-UNSOURCED-SEAT; STOCK's does not, on H-PRESENT.

THE MECHANISM AS STATED: REFUSED on every reading; on DISPLACEMENT and QUANTA
as NET formation only -- atomic mass can still form there as matter with its
antimatter (the pair route, PRICED); on TEMPLATE on P-UNIFORM and
H-UNSOURCED-SEAT -- where the latter fails, a seat prepared in advance can still
have its elements' Higgs-given mass restored on arrival (the held-seat release
route, PRICED; it forms no baryons).
THE CONSIDERATION: TRUE (THEOREM on H-TREE); on P-UNIFORM it discriminates
nothing.

WHAT SURVIVES:
  (a) RECONSTRUCTION FROM DESTINATION STOCK.  stockgate.GATE is the condition,
      and transit.CARRIES_SUBSTANCE = False.  No mass forms at the seat: the
      stock's masses are already given where the stock is, by phi there
      (prior mass, C5).  The Higgs's part is a precondition already met,
      which is M's consideration, and it is not a trigger.  S5 and D25 stand
      unchanged.
  (b) THE PAIR ROUTE, priced in section 4: EXCITATION's remainder.  Atomic
      mass forms as matter with its antimatter; the carrier supplies at
      least the pair floor; the antibaryons are held apart; the Higgs is an
      intermediary, not the source.
  (c) THE ANOMALY ROUTE, priced in section 4.  B + L is violated by the SU(2)
      anomaly: instanton tunnelling at T = 0; thermally over the sphaleron,
      above T_c and in the broken-phase window down to T*; whether
      two-particle collisions at high energy cross it is CONTESTED (section
      4) and not resolved; the sphaleron is a gauge-Higgs saddle whose height
      the vev sets.
  (d) THE HELD-SEAT RELEASE ROUTE, TEMPLATE's remainder where
      H-UNSOURCED-SEAT fails, and the reading closest to M's mechanism.  The
      seat is prepared in advance with a source holding |phi| below v; the
      arriving information triggers its release (H-RELEASE); |phi| returns
      to v, and the elements regain their Higgs-given mass.  PRICED by D20,
      asked of excite, at eps = 1/100: a source of 2.148e27 kg/m^3 of
      Higgs-derived mass where the templates sit (D16), holding 197.0 J of
      source rest energy per J of field (excite.holding_ratio; 2/eps at
      small eps).  (i) It forms no baryons: the elements were already
      there, and no Higgs coupling carries B (C3).  (ii) The energy: as
      |phi| relaxes to the elements' own lowering eps0 the field releases
      F(eps) - F(eps0), with F = rho_EW eps^2(2-eps)^2 per unit volume
      (excite.holding_terms), and by energy conservation that is what pays
      for the elements' regained rest energy, which cannot exceed it; the
      rest is radiated (the selftest checks the balance exactly over
      Fraction).  With the elements' own lowering at eps0 = 1e-12, 1e-6,
      1/1000, 1/200: regained/released = 2.020e-10, 2.020e-4, 0.1834,
      0.6695.  That field energy was stored
      in advance: the phi-coupled rest energy at the seat (the prepared
      source's with the elements') was 197.0 times as much, so per joule
      regained at least 197.0 J of it sat at the seat.  What becomes of
      the source at release is not computed.  (iii) What can be regained:
      the electrons' part exactly, eps x 3.010e-4 of the payload (3.010e-6
      at eps = 1/100; H-TREE); the nucleons' part is eps times the
      first-order share at small eps (the largest READ nucleon row gives
      1.716e-3 at eps = 1/100; an estimate, not a bound) and, up to the
      stability edge, a finite response that is OPEN like the finite
      share.  Within excite's section-3 model (source rest mass
      proportional to phi) a static hold is stable only below
      eps = 0.4226 (excite.stability_edge), on 0.5774 v < |phi| < v; a
      TEMPLATE seat below that keeps no held-seat remainder.  (iv) It needs
      the seat prepared in advance: something reached the destination
      first, at <= c, which is D23's point for reconstruction, asked of
      the ledger (transit.TRAVERSAL_IS_REMOVED = False).  The Higgs is an
      intermediary here too, holding what the source stored, not the source
      (C4).

===============================================================================
6.  NAMED HYPOTHESES AND PREMISES -- EVERY LIMITATION, NONE BURIED
===============================================================================

  H-TREE  m_f = y_f v/sqrt(2), at tree level in unitary gauge, as the READ
          source states it.  The capture's mass column is used as it stands
          (PDG: MS-bar u, d, s at 2 GeV; m_c(m_c), m_b(m_b); t direct), so each
          Yukawa carries that scheme.
  H-TREE-V The field-energy theorem of section 3 is for the tree-level
          potential (excite's Mexican hat).  Beyond it, what matters for C4 is
          that v stays a local minimum, which both the stable and the READ
          metastable case keep; the metastable case's one release is carried
          in section 3.
  H-REAL  The field-energy theorem is PROVED for the real scalar that
          higgs.T_scalar models.  That the doublet's other components and the
          gauge fields add only non-negative terms to T_00 is claimed, not
          computed from an owner and not read.  C4's THEOREM and D29 carry it.
  H-LINEAR C2 measures the Higgs share as the FIRST-ORDER response of the
          nucleon mass to the quark masses (sigma terms, Feynman-Hellmann) at
          the physical point, with the QCD scale held fixed.  That is exactly
          the measure for DISPLACEMENT, and C2 is listed there for a SMALL
          displacement only; a finite one is OPEN, and C3 carries the refusal
          regardless: a small displacement of phi is a first-order response.
          SWITCH-ON, STOCK and TEMPLATE ask what the field GIVES, a finite
          counterfactual; with the field switched off the heavy-quark
          thresholds move and the QCD scale moves with them.  That finite
          share is OPEN: NOT computed, NOT read, and whether it exceeds half
          is undecided here.  C2 is therefore NOT listed on SWITCH-ON, STOCK
          or TEMPLATE, and no verdict rests on the finite share.
  H-PRESENT A CASE DEFINITION, not a finding: an element present at the seat
          is present with its measured mass (the masses READ), i.e. with all
          of its Higgs-given mass, |phi| = v there before arrival.  Measured
          mass means phi as it is where the masses were measured; the
          matter's own D20 lowering (eps of 1e-18 per 2.202e11 kg/m^3 of
          Higgs-derived mass, asked of excite, linear) sits inside the
          measured mass, so |phi| = v here names that phi and no verdict
          moves.  C5 rests on H-PRESENT, and so does the claim that STOCK
          needs no P-UNIFORM.  Its complement -- templates at the seat
          without all or part of their HIGGS-GIVEN mass, |phi| < v there
          before arrival -- is the TEMPLATE reading, refused by C1 on
          P-UNIFORM and H-UNSOURCED-SEAT.  (With phi = 0 the nucleons keep
          their non-Higgs mass, so the missing part is the Higgs-given one.)
          H-PRESENT or not, the split is three-way: before arrival the seat
          is r = |phi|/v < 1 (TEMPLATE, C1), r = 1 (STOCK on H-PRESENT, C5)
          or r > 1 (neither reading's claim: the trigger has nothing to give;
          holding r > 1 needs a source outside D20's model).  The selftest
          checks that the three cases partition the seat, on the boundaries
          and inside each interval.
  H-UNSOURCED-SEAT Nothing at the seat holds |phi| below v before arrival.
          M's sentence names no such source: only the information arrives.
          C1 refuses TEMPLATE on it, with P-UNIFORM, D15 and D16.  It is not
          vacuous: within D20's model a positive source is an equilibrium on
          0 < |phi| < v (section 1 (a)) and, within excite's section-3
          model (source rest mass proportional to phi), a stable hold only
          on 0.5774 v < |phi| < v, at 4(1-eps)^2/(eps(2-eps)) J of source per J
          of field (excite.holding_ratio; 2/eps at small eps).  Where it
          fails, TEMPLATE keeps a priced remainder, the held-seat release
          route (section 5 (d)), on that range only, within excite's
          section-3 model.  Within excite's
          section-3 model (source rest mass proportional to phi) it does not
          reach SWITCH-ON: the off state lies past D20's stability edge,
          eps = 0.4226 (excite.stability_edge), where the medium is unstable
          and no static hold stands.  A source whose mass rises convexly
          with |phi| (D20'S MODEL; not computed) could hold it, and with the
          elements seated that is TEMPLATE at |phi| = 0.
  H-RELEASE On the held-seat release route the trigger removes the prepared
          source without doing work on the field or the elements.  What
          becomes of the source's own rest energy is not computed.
  P-UNIFORM Where nothing sources it the vev takes one value everywhere.  A
          PREMISE: supported by the constancy of measured fermion masses, not
          read here, and asserted by no owner boolean.  C1 (on SWITCH-ON and
          TEMPLATE) and the consideration's 'discriminates nothing' rest on
          it; C5 (prior mass, STOCK on H-PRESENT) does not.
  H-A     A_e is the nearest integer to stock.ATOMIC_MASS[e], and the natural
          mixture's mean nucleon number lies within 1/2 of it.  The selftest
          recomputes every count at A_e +/- 1/2 and checks that no boolean
          moves.
  H-LIST  The payload is stock.HUMAN's 14 listed elements.  Their fractions
          sum to 0.99992; the unlisted remainder is carried as its own line
          and assigned no composition.
  H-AME   mu_min is the least mass per nucleon among AME2020's measured
          nuclides; gravitational binding is negligible at payload scale
          (section 4).
  H-R     R = 1 m for the Bekenstein comparison.  The ratio of section 3 is
          linear in R and independent of M.
  H-BL    B - L is exactly conserved ("(B - L) is conserved", READ).  A
          Majorana neutrino mass would break it by 2 units.  That was not read.
  H-FLAV  Each lepton flavour is conserved (massless neutrinos).  It is used
          ONLY for the flavour sub-count in the report, which carries no
          verdict.
  H-THERM Plasma fermions above T_c may carry thermal masses of order gT.
          That was NOT read in any source, it is not asserted, and nothing
          here uses it.
  D20'S MODEL  The sign of section 1 (a) holds for a source whose mass comes
          from phi, rising with |phi|, as every SM mass does.  A source outside
          that model (a negative-sign portal coupling, say) could raise |phi|.
          The stability edge of section 5 (d) needs excite's narrower section-3
          hypotheses: a static source of fixed number density whose rest mass
          is proportional to phi.  A source whose mass rises convexly with
          |phi| could hold stably below it; that is not computed.

===============================================================================
7.  WHAT THIS FILE REFUSES
===============================================================================

   1. ONE NUMBER FOR THE HIGGS SHARE.  The measures are printed apart.
   2. RESOLVING THE COLLIDER-ENERGY DISPUTE.  It is CONTESTED in the READ.
   3. A REFUSAL ON A CONTESTED FIGURE ALONE.  derive_verdict() makes this
      structurally impossible, and the selftest proves it.
   4. A ZERO-TEMPERATURE RATE WITHOUT ITS PREFACTOR.  Only the exponent was
      read.
   5. AN EXACT ZERO FOR THE VEV ABOVE T_c.  The source says "approximately
      zero".
   6. ANY FIGURE FOR THE INFORMATION CONTENT OF A HUMAN.  None was found.
   7. TREATING k_B T ln 2 AS THE ENERGY OF A BIT.  It is a bound on erasure.
   8. COUNTING THE HEAVY-QUARK COUPLING AS HIGGS-MADE MASS.  It is printed as
      CONTESTED.
   9. DISMISSING A PRICED ROUTE.  The pair route, the anomaly route and the
      held-seat release route are all priced and all listed in what
      survives, and no refusal of the mechanism is printed without its
      priced remainder.
  10. A FIGURE HELD WITHOUT ITS SOURCE TEXT.  Every READ number used here
      appears in a quotation held in SOURCES, and the selftest checks it.
  11. THE STATUS WORD M RETIRED.  No status here is that word.
  12. COUNTING ONE OBJECTION TWICE, OR A COUNT AGAINST A READING IT DOES NOT
      ANSWER.  Each count is reported only against the readings it has a
      stated reason to answer, and no count is claimed as independent of
      another.

Every refusal is a flag DERIVED at selftest time, from the computed objects or
from a scan of this docstring, the report and the proposed rows, and each scan
has a control that plants a violation and must catch it.

===============================================================================
8.  STATUSES AND DIVERGENCES, RECORDED
===============================================================================

THEOREM: the consideration on H-TREE; prior mass (C5) on H-TREE and H-PRESENT;
D15, D16, D18, D19 as excite states them; the sign of the holding source within
D20's model; the field-energy theorem on H-TREE-V and H-REAL; the Yukawa
charges; the pair floor; energy conservation.  INFERENCE FROM READ TEXT: that
vacuum decay forms no atomic mass at the seat.  MEASURED: every count, share,
energy and exponent, each carrying its inputs' status.  Through v, every
Yukawa, alpha_W, E_sph formula value and exponent INHERITS NAMED-NOT-READ.
Through u = gravity.U_KG (CODATA 2018) and stock.ATOMIC_MASS, every count and
payload share INHERITS NAMED-NOT-READ.  READ: every figure in SOURCES marked
READ, including both FLAG sigma_piN averages.  CONTESTED: which sigma_piN is
right; the heavy-quark terms as a mass share; the collider rate.  PREMISE:
P-UNIFORM.  CASE DEFINITION: H-PRESENT.  NAMED HYPOTHESIS OF C1 ON TEMPLATE:
H-UNSOURCED-SEAT.  OPEN: the finite Higgs share (not computed, not read).
CAUTION HELD: the Bekenstein figure is not read as an information capacity
(Hayden and Wang).

DIVERGENCES FROM THE SOURCES, RECORDED AND NOT REPAIRED.  Rubakov &
Shaposhnikov print 10^-170 for exp(-4 pi/alpha_W) at alpha_W = 1/29
(arithmetic: 10^-158.27).  Tye-Wong pair 10^-162 with alpha_W ~ 1/30 on p.2
(arithmetic: 10^-163.73, so 1.73 decades off; their p.7 pairing with 1/29.7
gives 10^-162.09).  Tye-Wong's 4.75 TeV x 1.91 is 9.07, not their 9.11.
chiQCD's abstract and p.5 differ on quark and glue energy.

DIVERGENCE FROM THE DOCKET TEXT.  The docket calls the CMB temperature READ.
The tree holds it as permute.T_CMB = 2.7255 with a comment naming Fixsen 2009,
with no capture and no quoted locator.  Here it is CITED, and the Landauer count
inherits CITED.  Nothing turns on it: the ratio of section 3 moves linearly
with T.

NOTHING IS REPAIRED.

===============================================================================
9.  SOURCES
===============================================================================

SOURCES below holds, for every figure used, its locator, its status and the
verbatim text the READ stage returned (ligature and OCR artefacts normalised
only).  The primaries from before arXiv ('t Hooft 1976, Klinkhamer-Manton 1984,
Ringwald 1990, Espinosa 1990, Sakharov 1967, SVZ 1978, Landauer 1961) are CITED
through the papers that were read.  The two published counts of the bits in a
human body (Braunstein; Nelms et al.) are NOT-FOUND: the proxy blocked both
pages, and neither is used.
"""

import ast
import contextlib
import inspect
import io
import math
import re
import sys
from fractions import Fraction

import gravity
import excite
import higgs
# ledger is NOT imported here.  Since DOCKET 65 was seated, ledger.py asks this
# file for its rows while ledger is being imported, so this file may not need
# ledger while IT is being imported, or whichever loads first finds the other
# empty.  Everything this file asks of the board -- M's words, D23, the rows
# it checks are seated -- is asked at call time, through _ledger().
import nopath
import pdgcapture
import permute
import stock
import stockgate
import transit
import warpfolder

# ---------------------------------------------------------------------------
# IMPORTED, NEVER COPIED.  Every owner name this file asks, by module
# attribute.  The selftest checks that each callable is defined in the module
# it is asked of.
# ---------------------------------------------------------------------------
IMPORTS = (
    ("higgs", ("vev", "_capture_row", "M_HIGGS", "GEV_IN_J", "c", "G",
               "T_scalar", "CAVEAT_B_AS_FIRST_WRITTEN",
               "CANNOT_BE_SWITCHED_ON_IN_ONE_PLACE")),
    ("excite", ("TAIL_RATE_IS_MASS", "DISPLACEMENT_IS_ULTRALOCAL",
                "ELECTRON_MASS_IS_A_RULER", "FLAT_DIRECTIONS_ARE_INERT",
                "holding_terms", "holding_ratio", "QUANTUM_LIFETIME_S",
                "LAMBDA_H_READ_M", "one_sig", "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18",
                "SOURCE_POLY", "SOURCE_CLOSED", "FIELD_POLY", "FIELD_CLOSED",
                "pmul", "P", "peval", "RHO_EW", "EPS_CHEMICAL", "EPS_AT_FIXTURE",
                "exact_source_density", "stability_edge")),
    ("warpfolder", ("HEATING_TO_EW_SCALE_RESTORES_SYMMETRY", "rest_energy_j",
                    "megatons", "baryons_in", "FLASH_IS_A_RECONSTRUCTION_MECHANISM")),
    ("stock", ("HUMAN", "ATOMIC_MASS", "feedstock_kg")),
    ("stockgate", ("GATE",)),
    ("transit", ("CARRIES_SUBSTANCE", "TRAVERSAL_IS_REMOVED")),
    ("nopath", ("landauer_energy", "bekenstein_bits", "KB", "HBAR", "C",
                "LANDAUER_IS_THE_WEAKER_HALF", "BEKENSTEIN_IS_THE_ARGUMENT")),
    ("permute", ("T_CMB",)),
    ("gravity", ("U_KG", "symbol_to_Z", "nuclides")),
    ("pdgcapture", ("read",)),
    ("ledger", ("RULED_BY_M", "DEMAND", "SUPPLY")),
)
_MODS = {"higgs": higgs, "excite": excite, "warpfolder": warpfolder,
         "stock": stock, "stockgate": stockgate, "transit": transit,
         "nopath": nopath, "permute": permute, "gravity": gravity,
         "pdgcapture": pdgcapture}


def _ledger():
    """ledger.py, imported at CALL time, never at import (see the import block):
    ledger asks this file for PROPOSED_ROWS during its own import."""
    import ledger
    return ledger


def _mod(name):
    """An owner module by name: _MODS's, or the ledger, asked at call time."""
    return _ledger() if name == "ledger" else _MODS[name]

# ------------------------------------------------------------------ M's words
M_MECHANISM = ("As soon as the information hits the seat, it triggers the higgs "
               "field, and atomic mass forms")
M_CONSIDERATION = ("If the elements required for seating are present, then the "
                   "conditions for a higgs field or something like it are also "
                   "present")
M_ROW = "M-S1A-P1"

# ------------------------------------------------------------- the SI bridge
C = higgs.c                                     # SI-exact, via ladder
G_NEWTON = higgs.G                              # via ladder
MEV_J = higgs.GEV_IN_J / 1000.0                 # SI-exact
MEV_KG = MEV_J / C ** 2
U_KG = gravity.U_KG                             # CODATA 2018  NAMED-NOT-READ
U_MEV = U_KG / MEV_KG

# --------------------------------------------------------------- READ masses
PDGID = {"e": 11, "mu": 13, "tau": 15, "d": 1, "u": 2, "s": 3, "c": 4,
         "b": 5, "t": 6, "p": 2212, "n": 2112, "W": 24}
CHARGED_FERMIONS = ("e", "mu", "tau", "u", "d", "s", "c", "b", "t")


def _read_masses(row=None):
    """{name: mass in MeV}, each through higgs._capture_row -- the reader that
    owns captures/PDG-2026.tsv's path in this tree.  READ.  `row` lets the
    selftest substitute a mutated reader and watch the masses follow it."""
    row = higgs._capture_row if row is None else row
    return {k: float(row(i)["mass_MeV"]) for k, i in PDGID.items()}


MASS_MEV = _read_masses()                                        # READ
M_N_MEV = (MASS_MEV["p"] + MASS_MEV["n"]) / 2.0                  # from READ
M_W_GEV = MASS_MEV["W"] / 1000.0                                 # READ


def lightest_baryon():
    """(name, mass MeV) of the lightest baryon in the capture.  READ."""
    rows = [(float(r["mass_MeV"]), r["name"]) for r in pdgcapture.read()
            if r["family"] == "baryon"]
    m, name = min(rows)
    return name, m


def n_generations():
    """N_f, counted from the capture: charged leptons (family lepton, Q3 = -3).
    The capture excludes the tau' by PDG's own status flag (pdgcapture.py)."""
    return sum(1 for r in pdgcapture.read()
               if r["family"] == "lepton" and r["Q3"] == "-3")


N_F = n_generations()

# ==================================================================== SOURCES
# key: (status, locator, verbatim text as the READ stage returned it).  The
# text is what the misquote check reads; nothing is paraphrased inside it.
SOURCES = {
    "RS96-sel": ("READ",
                 "Rubakov & Shaposhnikov, hep-ph/9603208 (Usp. Fiz. Nauk 166 "
                 "(1996) 493), Sec. 2, eqs. (2.4)-(2.5), printed pp. 4-5 (PDF "
                 "pp. 5-6); held in the source's own order",
                 "where the factor 1/3 comes from the baryon number of a quark, "
                 "while the factor 3 . 3 is due to colour and number of "
                 "generations. So, the amounts of non-conservation of baryon and "
                 "lepton numbers are related: Delta N_e = Delta N_mu = Delta "
                 "N_tau = (1/3) Delta B ; (B - L) is conserved while (B + L) is "
                 "violated."),
    "RS96-anom": ("READ", "Rubakov & Shaposhnikov hep-ph/9603208, Sec. 2, eqs. "
                  "(2.2)-(2.4), printed p. 4 (PDF p. 5)",
                  "At the quantum level these currents are no longer conserved "
                  "due to the triangle anomaly ... Therefore, one expects that "
                  "fermion numbers ... are not conserved in any process where the "
                  "gauge field evolves in such a way that N[A] != 0 ... Namely, "
                  "Delta N_F^(i) = N[A]"),
    "RS96-T0": ("READ", "Rubakov & Shaposhnikov hep-ph/9603208, Sec. 2, printed "
                "p. 5 (PDF p. 6); the same passage goes on: 'In pure Yang-Mills "
                "theory an instanton is the solution to the Euclidean field "
                "equations'",
                "At zero energies and temperatures, the transition between vacua "
                "with different n[omega] is a tunnelling event which is described "
                "by instantons"),
    "RS96-2.8": ("READ", "Rubakov & Shaposhnikov hep-ph/9603208, eq. (2.8), "
                 "printed p. 6 (PDF p. 7)",
                 "In the electroweak theory, the tunneling probability is "
                 "unobservably small, Gamma_inst ~ exp(-4 pi / alpha_W) ~ "
                 "10^-170, (2.8) where alpha_W = g^2/4 pi = alpha/sin^2 theta_W "
                 "= 1/29"),
    "RS96-sph": ("READ", "Rubakov & Shaposhnikov hep-ph/9603208, Sec. 2, printed "
                 "p. 7 (PDF p. 8), above eq. (2.11)",
                 "This height is determined by the static saddle point solution "
                 "to the Yang-Mills-Higgs equations, the sphaleron"),
    "tHooft": ("CITED", "cited as ref [20] in hep-ph/9603208 and ref [43] in "
               "CMS 1805.06013; not on arXiv; not read",
               "[20] G. 't Hooft. Phys. Rev. Lett., 37:8, 1976."),
    "RS96-inst": ("READ", "Rubakov & Shaposhnikov hep-ph/9603208, Sec. 4.1, "
                  "printed p. 11 (PDF p. 12)",
                  "This process can be described by instantons and is strongly "
                  "suppressed by the semiclassical exponent exp(-4 pi / alpha_W)."),
    "TW-size": ("CONTESTED", "Tye & Wong 1505.03690, printed p.2 (Introduction) "
                "and p.7 (Sec. 2.1)",
                "exponentially suppressed, by a factor like exp(-4 pi/alpha_W) ~ "
                "10^-162 where alpha_W ~ 1/30.   /  since an instanton action S = "
                "2 pi/alpha_W where the weak coupling alpha_W ~ 1/29.7, the "
                "tunneling rate goes like exp(-2S) ~ 10^-162"),
    "RS96-esph": ("READ", "Rubakov & Shaposhnikov hep-ph/9603208, eq. (2.11), "
                  "printed p. 7 (reporting Klinkhamer & Manton PRD 30, 2212 "
                  "(1984), CITED)",
                  "E_sph = (2 m_W / alpha_W) B(m_H/m_W), where m_H is the mass of "
                  "the Higgs boson. The function B(m_H/m_W) has been evaluated "
                  "numerically [32]; it varies from 1.56 to 2.72 as m_H/m_W varies "
                  "from zero to infinity. So, the height of the barrier in the "
                  "electroweak theory is of order 10 TeV."),
    "TW-FFS-esph": ("READ", "Tye & Wong 1505.03690 eq.(1.2) p.3; Funakubo, Fuyuto, "
                    "Senaha 1612.05431 eq.(10) p.2",
                    "Using the known Higgs vacuum expectation value v = 246 GeV, W "
                    "Boson mass m_W = 80 GeV and the Higgs Boson mass m_H = 125 "
                    "GeV, we obtain V(Q) ~ 4.75 TeV (1.31 sin^2(m_W Q) + 0.60 "
                    "sin^4(m_W Q)), E_sph = max[V(Q)] = V(pi/(2 m_W)) = 9.11 TeV   "
                    "/   E_sph = g_2 v V(pi/2) ~ 9.08 TeV."),
    "DR-Tc": ("READ", "D'Onofrio & Rummukainen, 1508.07161 (PRD 93 (2016) 025003): "
              "abstract p.1 (the value used); Sec. VII p.8 prints 159.6 +/- 0.1 "
              "+/- 1.5",
              "While the cross-over is smooth, it is very well defined with a "
              "width of only ~ 5 GeV. We measure the cross-over temperature from "
              "the maximum of the susceptibility of the Higgs condensate, with "
              "the result T_c = 159.5 +/- 1.5 GeV.  /  we obtain T_c = 159.6 +/- "
              "0.1 +/- 1.5 GeV, where the first error is due to the statistical "
              "accuracy of the lattice computation and the second one is the "
              "estimated uncertainty of the effective theory approach"),
    "DRT-vev": ("READ", "D'Onofrio, Rummukainen, Tranberg 1404.3565 p.1 and p.3; "
                "1508.07161 footnote 1 p.1",
                "the electroweak symmetry breaking transition in the early "
                "Universe was a smooth cross-over from the symmetric phase at T > "
                "T_c, where the (expectation value of the) Higgs field was "
                "approximately zero, to the broken phase at T < T_c GeV where it "
                "is finite  /  If the temperature is below T_c, v^2(T) is "
                "approximately linear in T, and at T > T_c, it is close to zero.  "
                "/  Although there is no real symmetry breaking phase transition, "
                "we use the conventional labels 'broken' and 'symmetric'"),
    "MRM-phi": ("READ", "Morrissey & Ramsey-Musolf 1206.2942, Sec. 2, below eq.(1), p.4",
                "Note that (in unitary gauge) the masses of the W+/- and Z0 weak "
                "vector bosons and the fermions are proportional to phi."),
    "DRT-rate": ("READ", "D'Onofrio, Rummukainen, Tranberg 1404.3565 (PRL 113 (2014) "
                 "141602): abstract p.1; eq.(8) p.4 (the figure used, 8.0(1.3)e-7)",
                 "The sphaleron rate in the symmetric phase (T > T_c) is "
                 "Gamma/T^4 = (18 +/- 3) alpha_W^5 ... The freeze-out temperature "
                 "in the early Universe, where the Hubble rate wins over the "
                 "baryon number violation rate, is T* = (131.7 +/- 2.3) GeV.  /  "
                 "Gamma_Symm./T^4 = (8.0 +/- 1.3) x 10^-7 ~ (18 +/- 3) alpha_W^5, "
                 "(8) where, in the last form, factors of ln alpha_W have been "
                 "absorbed in the numerical constant."),
    "DRT-broken": ("READ", "D'Onofrio, Rummukainen, Tranberg 1404.3565: abstract "
                   "p.1; eq.(7) p.3; range extended to T ~ 130 GeV on p.4",
                   "and in the broken phase in the physically interesting "
                   "temperature range 130 GeV < T < T_c it can be parametrized as "
                   "log(Gamma/T^4) = (0.83 +/- 0.01)T/GeV - (147.7 +/- 1.9)."),
    "DRT-Tc": ("READ", "D'Onofrio, Rummukainen, Tranberg 1404.3565: abstract p.1 "
               "(its own T_c, which bounds its fit); p.3 (the measured interval); "
               "p.4 (the extension)",
               "the cross-over is sharply defined at T_c = (159 +/- 1) GeV.  /  In "
               "the interval 140 <~ T <~ 155 GeV the broken phase rate is very "
               "close to a pure exponential  /  the match gives us confidence to "
               "extend the range of validity of our fit (7) down to T ~ 130 GeV, "
               "in order to cover the physically interesting range."),
    "RS96-coll": ("CITED", "Rubakov & Shaposhnikov hep-ph/9603208 printed p.3, refs "
                  "[39] Ringwald NPB 330 (1990) 1 and [40] Espinosa NPB 343 (1990) "
                  "310, neither read",
                  "This problem has attracted considerable interest in recent "
                  "years, after the first -- and encouraging at the time -- "
                  "quantitative results were obtained [39,40]. In spite of "
                  "remarkable theoretical developments, this problem is still not "
                  "completely solved; existing results indicate that the "
                  "electroweak baryon number violating processes occur at "
                  "unobservable rates even at very high energies."),
    "BLRRT": ("READ", "Bezrukov, Levkov, Rebbi, Rubakov, Tinyakov hep-ph/0304180 "
              "(PRD 68 (2003) 036005): abstract p.1; Sec. II p.7; their scope: "
              "s-wave, N -> 0, m_H = m_W",
              "Our results show that baryon and lepton number violation remains "
              "exponentially suppressed up to very high energies of at least 30 "
              "sphaleron masses (250 TeV).  /  up to the energy 8 M_W/alpha_W ~ "
              "20TeV the suppression is still high: the suppression factor is "
              "smaller than e^-60 ~ 10^-26 for alpha_W ~ 1/30."),
    "BLRRT-PLB": ("READ", "Bezrukov, Levkov, Rebbi, Rubakov, Tinyakov hep-ph/0305300 "
                  "(PLB 574 (2003) 75): abstract p.1",
                  "We also derive lower bounds on the tunneling exponent which show "
                  "that baryon number violation remains exponentially suppressed up "
                  "to very high energies of at least 30 sphaleron masses (250 TeV)."),
    "BLRRT-conj": ("READ", "Bezrukov et al. hep-ph/0304180, Sec. I p.2",
                   "This approach is based on the conjecture that, with exponential "
                   "accuracy, the two-particle initial state can be substituted by a "
                   "multiparticle one provided that the number of particles is not "
                   "parametrically large (although not proven rigorously, this "
                   "conjecture was checked in several orders of perturbation theory "
                   "in E/E_sph in gauge theory [31, 35] and explicitly in quantum "
                   "mechanics with two degrees of freedom [36, 37])."),
    "KM-2020": ("READ", "Khoze & Milne, arXiv:2011.07167v1 (IPPP/20/56): printed p.9 "
                "(PDF p.10), p.13 (PDF p.14), p.15 and p.16 (PDF pp.16-17)",
                "The instanton suppression factor is significant with the minimal "
                "value of the holy-grail function, F ~ 0.70, loosing only 30% of "
                "the original 't Hooft instanton suppression. ... Electroweak "
                "instantons remain exponentially suppressed by at least "
                "e^(-(4 pi/alpha_w) 0.70) and are unobservable in high energy 2 "
                "particle collisions for any value of the energy.  /  So, while "
                "there is no rigorous proof of exponentiation, we are comfortably "
                "optimistic that the Mueller correction does exponentiate  /  This "
                "was based in part on an assumption that there are no additional "
                "exponentially growing (and unphysical, as explained at the end of "
                "section 3.1) contributions generated at higher orders in instanton "
                "perturbation theory.  /  the the 't Hooft suppression in the "
                "exponent is reduced by not more than ~ 30% over the entire energy "
                "range."),
    "TW-claim": ("CONTESTED", "Tye & Wong 1505.03690 (PRD 92 (2015) 045005): "
                 "abstract p.1; printed p.5 (the 10^{4+/-2} estimate)",
                 "We show that the baryon-lepton number violating processes can "
                 "take place without the exponential tunneling suppression (at "
                 "zero temperature) at energies around and above the barrier "
                 "height (sphaleron energy) at 9.0 TeV.  /  A very crude order of "
                 "magnitude estimate gives 10^{4+/-2} such events in the coming "
                 "Large Hadron Collider (LHC) run at 14 TeV"),
    "TW-2017": ("CONTESTED", "Tye & Wong arXiv:1710.07223v1: abstract p.1; p.2; "
                "Sec. II-III p.3; Sec. XIII p.11; ref. [27] p.13 (it cites the "
                "rebuttal, and replies to it on p.3)",
                "there is a discrepancy of about 70 orders of magnitude between the "
                "two estimates  /  We agree with this estimate for a single "
                "sphaleron. However, we claim that multi-sphaleron processes can "
                "drastically change the picture.  /  Recently we proposed that the "
                "existing estimate of the cross-sections of such processes in the "
                "prevalent picture are off (too small) by many orders of magnitude. "
                " /  [27] K. Funakubo, K. Fuyuto, and E. Senaha, 'Does a band "
                "structure affect sphaleron processes?,' arXiv:1612.05431  /  It "
                "is clear that both estimates involve assumptions based on "
                "intuitions as well as approximations remaining to be fully "
                "justified.  /  Admittedly, the estimate (4) is only an order of "
                "magnitude guesstimate  /  As argued at times in the literature "
                "(see e.g., Ref.[26] and recently in [27])  /  However, the above "
                "argument is somewhat misleading."),
    "FFS-rebut": ("READ", "Funakubo, Fuyuto, Senaha 1612.05431, p.4",
                  "It is shown that, in the leading order of the WKB "
                  "approximation, the overlap between the coherent state and the "
                  "n-particle state produces a multiplicative factor ... "
                  "Therefore, the overlap between the coherent state and the in-state "
                  "composed of two particles whose total momentum is E_sph yields "
                  "a suppression factor ~ e^{-pi E_sph/m_W} ~ 10^-155, rendering "
                  "(B + L)-changing process unobservably small. ... Those types of "
                  "the suppressions still remain regardless of the band "
                  "structure, which is not properly discussed in Ref. [8]"),
    "CMS": ("READ", "CMS Collaboration 1805.06013 (JHEP 11 (2018) 042): abstract p.1, "
            "Sec. 8.2 p.17",
            "The data sample corresponds to an integrated luminosity of 35.9 "
            "fb^-1 collected with the CMS experiment at the LHC in proton-proton "
            "collisions at a center-of-mass energy of 13 TeV in 2016. ... An upper limit of 0.021 is set at 95% confidence level on the "
            "fraction of all quark-quark interactions above the nominal threshold "
            "energy of 9 TeV resulting in the sphaleron transition."),
    "Sakharov": ("READ", "Rubakov & Shaposhnikov hep-ph/9603208, Sec. 1, p.2 "
                 "(Sakharov JETP Lett. 5 (1967) 24 CITED)",
                 "Today, this short extract is usually dubbed as three necessary "
                 "Sakharov's conditions for baryon asymmetry generation from the "
                 "initial charge symmetric state in the hot Universe, namely: (i) "
                 "Baryon number non-conservation. (ii) C and CP violation. (iii) "
                 "Deviations from thermal equilibrium."),
    "MRM-SM": ("READ", "Morrissey & Ramsey-Musolf 1206.2942 (New J. Phys. 14 (2012) "
               "125003), Sec. 1 pp.2-3",
               "All the ingredients required for EWBG are contained in the SM. "
               "Unfortunately, EWBG is unable to explain the observed baryon "
               "asymmetry within the SM alone. The first impediment is that the "
               "SM electroweak phase transition is first-order only if the mass "
               "of the Higgs boson lies below m_h <~ 70 GeV [18, 19]. ... Even if "
               "the phase transition were first order, the CP violation induced "
               "by the CKM phase does not appear to be sufficient to generate "
               "large enough chiral asymmetries [22, 23, 24]."),
    # ------------------------------------------------- the vacuum's stability
    "BU-meta": ("READ", "Buttazzo, Degrassi, Giardino, Giudice, Sala, Salvio, "
                "Strumia, arXiv:1307.3536v4, Sec. 1, p.3",
                "in the context of the SM the measured value of M_h is special "
                "because it corresponds to a near-critical situation in which the "
                "Higgs vacuum does not reside in the configuration of minimal "
                "energy, but in a metastable state close to a phase transition"),
    "BU-mt": ("READ", "Buttazzo et al. arXiv:1307.3536v4, Sec. 4.3, eqs. (65)-(66), "
              "p.20",
              "M_h > (129.6 +/- 1.5) GeV (stability condition). (65) From this "
              "result we conclude that vacuum stability of the SM up to the "
              "Planck scale is excluded at 2.8 sigma (99.8% C.L. one-sided). "
              "Since the main source of uncertainty in eq. (64) comes from M_t, "
              "any refinement in the measurement of the top mass is of great "
              "importance for the question of EW vacuum stability. ... M_t < "
              "(171.53 +/- 0.42) GeV. (66)"),
    "BU-life": ("READ", "Buttazzo et al. arXiv:1307.3536v4, Sec. 6.3 p.31 and "
                "Sec. 7 p.31",
                "As shown, the SM vacuum is likely to survive for times that are "
                "enormously longer than any significant astrophysical age (e.g. "
                "the sun will exhaust its fuel in about five billion years).  /  "
                "Because of the present experimental uncertainties on the SM "
                "parameters (mostly the top quark mass), we cannot conclusively "
                "establish the fate of the EW vacuum, although metastability is "
                "now preferred at 99.3% CL."),
    "BU-scale": ("READ", "Buttazzo et al. arXiv:1307.3536v4, Sec. 7, p.32",
                 "The critical condition for stability is defined as the vanishing "
                 "of the effective coupling lambda_eff, see eq. (63), at some "
                 "energy scale Lambda_I. We find Lambda_I = 10^10-10^12 GeV, see "
                 "eq. (67), suggesting that the instability is reached well below "
                 "the Planck mass."),
    "DG-2012": ("READ", "Degrassi, Di Vita, Elias-Miro, Espinosa, Giudice, Isidori, "
                "Strumia, arXiv:1205.6497v2, Sec. 1, eq. (3), p.2",
                "M_h > 129.4 +/- 1.8 GeV. (3) From this result we conclude that "
                "vacuum stability of the SM up to the Planck scale is excluded at "
                "2 sigma (98% C.L. one sided) for M_h < 126 GeV."),
    "MRS-bubble": ("READ", "Markkanen, Rajantie, Stopyra, arXiv:1809.06923v2, "
                   "Sec. 4.1 printed p.24 and Sec. 6 printed p.54",
                   "This causes it to expand at near the speed of light, resulting "
                   "in the space around a nucleation point being converted to the "
                   "true vacuum, releasing energy into the bubble wall. Apart from "
                   "the destruction that this would unleash, and the different "
                   "masses of fundamental particles in the bubble interior, the "
                   "result is also gravitational collapse of the bubble  /  Once a "
                   "bubble has formed, it expands at the speed of light, destroying "
                   "everything in its way."),
    # ------------------------------------------------------------ the masses
    "FLAG-447": ("READ", "FLAG Review 2024, Aoki et al., arXiv:2411.04268v3, "
                 "Sec. 10.4.4 Eq. (447), p.272",
                 "N_f = 2 + 1 + 1 : sigma_piN = 60.9(6.5) MeV Refs. [26, 101]. (447)"),
    "FLAG-448": ("READ", "FLAG 2024, arXiv:2411.04268v3, Sec. 10.4.4 Eq. (448), "
                 "p.273; 2.7 sigma from Eq. (447), recorded in FLAG-tension",
                 "N_f = 2 + 1 : sigma_piN = 42.2(2.4) MeV Refs. [102-106]. (448)"),
    "FLAG-tension": ("READ", "FLAG 2024, arXiv:2411.04268v3, p.273",
                     "Notably, there is now a 2.7 sigma difference between the N_f "
                     "= 2 + 1 and N_f = 2 + 1 + 1 FLAG averages. This is unlikely "
                     "to be due to the inclusion of charm quarks in the sea. The "
                     "control of excited-state contributions remains an issue. In "
                     "particular, the PNDME 21 study utilizes a narrow-width prior "
                     "in their fitting analysis ... If this constraint is relaxed "
                     "then a sigma term of around 42 MeV is obtained."),
    "FLAG-HRKM23": ("READ", "FLAG 2024, arXiv:2411.04268v3, p.274 (the three-sigma "
                    "tension is with Hoferichter 23, ref. [1035], not with "
                    "1506.04142)",
                    "The N_f = 2 + 1 + 1 lattice average is in agreement with "
                    "Hoferichter et al. [1035] (Hoferichter 23 in Fig. 46), while "
                    "there is some tension, at the level of around three standard "
                    "deviations, with the lattice average for N_f = 2 + 1."),
    "FLAG-449": ("READ", "FLAG 2024, arXiv:2411.04268v3, Eq. (449), p.273",
                 "N_f = 2 + 1 + 1 : sigma_s = 41.0(8.8) MeV Ref. [107]. (449)"),
    "FLAG-450": ("READ", "FLAG 2024, arXiv:2411.04268v3, Eq. (450), p.273",
                 "N_f = 2 + 1 : sigma_s = 44.9(6.4) MeV Refs. [102-108], (450)"),
    "FLAG-sc": ("READ", "FLAG 2024, arXiv:2411.04268v3, Sec. 10.4.4, p.275",
                "the RQCD 16 N_f = 2 analysis of Ref. [870] that reports f_Tc = "
                "0.075(4) or sigma_c = 70(4) MeV, is consistent with the direct "
                "determinations of ETM 19 [983] for N_f = 2 + 1 + 1 of sigma_c = "
                "107(22) MeV"),
    "HRKM-21": ("READ", "Hoferichter, Ruiz de Elvira, Kubis, Meissner, "
                "arXiv:1506.04142v2 (PRL 115, 092301), Eq. (21), p.4",
                "we obtain sigma_piN = (59.1 +- 1.9 +- 3.0) MeV = (59.1 +- 3.5) MeV"),
    "FLAG-def": ("READ", "FLAG 2024 arXiv:2411.04268v3, p.261; the definitions "
                 "Eqs. (431)-(433) are on p.260",
                 "The sigma_piN,s,c give the shift in M_N due to nonzero light-, "
                 "strange- and charm-quark masses."),
    "EOS-SVZ": ("READ", "Ellis, Olive, Savage, arXiv:0801.3656v2 (PRD 77, 065026), "
                "Eqs. (10) and (12), p.5 (SVZ PLB 78, 443 (1978) CITED)",
                "f_N/m_N = sum_{q=u,d,s} f_Tq alpha_3q/m_q + (2/27) f_TG "
                "sum_{q=c,b,t} alpha_3q/m_q ... f_TG = 1 - sum_{q=u,d,s} f_Tq (12)"),
    "HRKM-24": ("READ", "Hoferichter et al., arXiv:1506.04142v2, Eq. (24), p.5",
                "sum_{q=u,...,t} f_q^N = 2/9 + 7/9 (f_u^N + f_d^N + f_s^N) = "
                "0.305 +- 0.009"),
    "Ji-cancel": ("READ", "X. Ji, arXiv:hep-ph/9410274 (PRL 74, 1071), after Eq. (25), p.5",
                  "Note that the heavy quarks do contribute to the mass term, the "
                  "kinetic and potential energy term, and the trace anomaly term. "
                  "However, the contributions cancel each other in the limit of "
                  "m_f -> infinity"),
    "Ji-eighth": ("READ", "X. Ji, arXiv:hep-ph/9410274, bullet p.7",
                  "The quark mass term accounts for about 1/8 of the nucleon mass. "
                  "About half of which or more is carried by the strange quark."),
    "Ji-table": ("READ", "X. Ji, arXiv:hep-ph/9410274, Table I p.9; the omitted "
                 "errors, the rounding and the largest uncertainty, p.6",
                 "TABLE I. A decomposition of the nucleon mass into different "
                 "contributions. ... mass type  H_i  M_i  m_s -> 0 (MeV)  m_s -> "
                 "infinity (MeV) ... quark mass  psibar m psi  b  160  110  /  I "
                 "have not shown the errors due to omission of higher-order "
                 "perturbative effects and errors on the sigma-term and current "
                 "quark masses. The total effect on individual numbers is about 5 "
                 "to 10 MeV. Thus I have rounded up the numbers to nearest 10 MeV. "
                 "The largest uncertainty is from the matrix element "
                 "<P|m_s ss|P>, which could be larger than the difference of the "
                 "two estimates shown."),
    "chiQCD": ("READ", "Yang et al. (chiQCD), arXiv:1808.08677v2 (PRL 121, 212001), "
               "abstract p.1 and p.5 (the abstract and p.5 disagree on quark and "
               "glue energy, 33/37 % against 32/36 %: recorded, not repaired)",
               "A quarter of the trace anomaly gives a 23(1)(1)% contribution to "
               "the proton mass based on the sum rule, given 9(2)(1)% contribution "
               "from the u, d, and s quark scalar condensates."),
    # ----------------------------------------------------------- information
    "Landauer": ("READ", "Lloyd, arXiv:quant-ph/9908043v3, Box pp.8-9; Bennett, "
                 "arXiv:physics/0210005v2, pp.1 and 4 (Landauer, IBM J. Res. Dev. "
                 "5, 183 (1961) CITED)",
                 "irreversible, many-to-one operations such as AND or ERASE "
                 "require dissipation at least k_B ln 2 for each bit of "
                 "information lost (Lloyd p.9); 'This is an irreversible entropy "
                 "increase of k ln 2' (Bennett p.4)"),
    "Bekenstein": ("READ", "Bekenstein, arXiv:quant-ph/0404042v1, Eq. (1) p.1 "
                   "(PRD 23, 287 (1981) CITED); bit form Lloyd "
                   "arXiv:quant-ph/9908043v3 p.7",
                   "S <= 2 pi E R / hbar c. (1)  [k_B = 1];  'The amount of "
                   "information that can be registered by a physical system is "
                   "I = S(E)/k_B ln 2' (Lloyd p.7)"),
    "HW-folk": ("READ", "Hayden & Wang, 'What exactly does Bekenstein bound?', "
                "arXiv:2309.07436v3: abstract p.1; printed p.2 (PDF p.3); printed "
                "p.3 (PDF p.4)",
                "The Bekenstein bound posits a maximum entropy for matter with "
                "finite energy confined to a spatial region. It is often "
                "interpreted as a fundamental limit on the information that can be "
                "stored by physical objects.  /  The key insight of Casini's "
                "formulation is that the Bekenstein bound can be understood as an "
                "information-theoretic statement about state distinguishability  /  "
                "Casini's entropy bound is a widely accepted proven version of the "
                "Bekenstein bound, but it is not the only viable formulation "
                "[10, 11]. A general interpretation of the Bekenstein bound is that "
                "it represents a fundamental limit on the information content "
                "carried by matter [7, 12]. ... However, it is important to note "
                "that this interpretation remains folklore rather than established "
                "fact"),
    "Braunstein": ("NOT-FOUND", "S. L. Braunstein, 'A fun talk on teleportation' "
                   "(egress-blocked; not opened)",
                   "NOT QUOTED -- page could not be fetched; figure known only "
                   "from a search-engine summary"),
    "Leicester": ("NOT-FOUND", "Nelms, Roberts, Thomas, Starkey, J. Phys. Special "
                  "Topics P4_4 (2013) (egress-blocked; not opened)",
                  "NOT QUOTED -- page could not be fetched; figure known only "
                  "from search summaries (ScienceDaily/phys.org 2013)"),
}

# (source key, the numeral as the source prints it, the value this file uses).
# The selftest checks that each numeral occurs in its source's held text and
# that it parses (parse_numeral) to exactly the value used.
PINS = (
    ("FLAG-447", "60.9", 60.9), ("FLAG-448", "42.2", 42.2),
    ("FLAG-449", "41.0", 41.0), ("FLAG-450", "44.9", 44.9),
    ("FLAG-447", "(6.5)", 6.5), ("FLAG-448", "(2.4)", 2.4),
    ("FLAG-449", "(8.8)", 8.8), ("FLAG-450", "(6.4)", 6.4),
    ("FLAG-sc", "107(22)", 107.0),
    ("HRKM-21", "59.1", 59.1), ("HRKM-24", "0.305", 0.305),
    ("chiQCD", "9(2)(1)%", 9.0), ("chiQCD", "23(1)(1)%", 23.0),
    ("Ji-table", "160", 160.0), ("Ji-table", "110", 110.0),
    ("Ji-table", "5 to 10 MeV", 5.0), ("Ji-table", "10 MeV.", 10.0),
    ("RS96-esph", "1.56", 1.56), ("RS96-esph", "2.72", 2.72),
    ("TW-FFS-esph", "9.11", 9.11), ("TW-FFS-esph", "9.08", 9.08),
    ("TW-FFS-esph", "4.75", 4.75), ("TW-FFS-esph", "1.31", 1.31),
    ("TW-FFS-esph", "0.60", 0.60), ("TW-claim", "9.0 TeV", 9.0),
    ("DR-Tc", "159.5 +/- 1.5", 159.5), ("DRT-rate", "131.7", 131.7),
    ("DRT-rate", "(18 +/- 3)", 18.0),
    ("DRT-rate", "(8.0 +/- 1.3) x 10^-7", 8.0e-7),
    ("DRT-broken", "(0.83 +/- 0.01)", 0.83), ("DRT-broken", "(147.7 +/- 1.9)", 147.7),
    ("DRT-broken", "130 GeV", 130.0),
    ("CMS", "0.021", 0.021), ("CMS", "35.9", 35.9), ("CMS", "13 TeV", 13.0),
    ("DG-2012", "126 GeV", 126.0),
    ("TW-size", "1/29.7", 29.7), ("TW-size", "1/30", 30.0),
    ("RS96-2.8", "1/29", 29.0), ("RS96-2.8", "10^-170", -170.0),
    ("TW-size", "10^-162", -162.0), ("DRT-Tc", "(159 +/- 1)", 159.0),
    ("FLAG-tension", "2.7 sigma", 2.7),
    ("BU-mt", "(171.53 +/- 0.42)", 171.53), ("BU-mt", "2.8 sigma", 2.8),
    ("BU-life", "99.3%", 99.3), ("DG-2012", "2 sigma", 2.0),
)

SIGMA_PIN_2P1P1 = 60.9          # MeV  READ          FLAG-447
SIGMA_PIN_2P1 = 42.2            # MeV  READ          FLAG-448 (2.7 sigma apart)
SIGMA_S_2P1P1 = 41.0            # MeV  READ          FLAG-449
SIGMA_S_2P1 = 44.9              # MeV  READ          FLAG-450
SIGMA_ERR = {"FLAG 2+1+1": (6.5, 8.8), "FLAG 2+1": (2.4, 6.4)}   # READ
SIGMA_C_ETM19 = 107.0           # MeV  READ          FLAG-sc (largest printed)
SIGMA_PIN_ROY_STEINER = 59.1    # MeV  READ          HRKM-21
COUPLING_SUM_HRKM = 0.305       # READ               HRKM-24
CHIQCD_QUARK_CONDENSATE = 9.0   # %    READ          chiQCD
CHIQCD_QUARTER_ANOMALY = 23.0   # %    READ          chiQCD
JI_QUARK_MASS_MEV = {"m_s -> 0": 160.0, "m_s -> infinity": 110.0}   # READ Ji-table
JI_ROUNDING_MEV = 10.0          # READ  Ji-table: the omitted-error effect, larger end
#: The difference of Ji's two estimates, which his largest uncertainty "could be
#: larger than" (READ Ji-table): computed from the two READ rows, never typed.
JI_ESTIMATE_DIFFERENCE_MEV = (JI_QUARK_MASS_MEV["m_s -> 0"]
                              - JI_QUARK_MASS_MEV["m_s -> infinity"])
B_KM_RANGE = (1.56, 2.72)       # READ               RS96-esph
TW_B_TERMS = (1.31, 0.60)       # READ               TW-FFS-esph
TW_PREFACTOR_TEV = 4.75         # READ, rounded (section 4 check)
E_SPH_TEV = {"Tye-Wong, pure SU(2)": 9.11, "Funakubo-Fuyuto-Senaha": 9.08,
             "Tye-Wong, with U(1)": 9.0}                 # READ
E_SPH_USED = "Funakubo-Fuyuto-Senaha"
T_C_GEV = 159.5                 # READ  DR-Tc, the abstract's figure
T_FREEZE_GEV = 131.7            # READ  DRT-rate
RATE_SYMM_READ = 8.0e-7         # READ  DRT-rate eq.(8): THE figure
RATE_COEFF_SYMM = 18.0          # READ  DRT-rate: 18 alpha_W^5, a cross-check only
BROKEN_FIT = (0.83, 147.7)      # READ  DRT-broken: ln(Gamma/T^4) = a T/GeV - b
BROKEN_FIT_LOW_GEV = 130.0      # READ  DRT-broken: the fit's stated lower end
BROKEN_FIT_HIGH_GEV = 159.0     # READ  DRT-Tc: its own paper's T_c bounds the fit
CMS_PEF_BOUND = 0.021           # READ  CMS
CMS_LUMI_FB = 35.9              # READ  CMS: fb^-1
CMS_SQRT_S_TEV = 13.0           # READ  CMS
DG_MH_CONDITION_GEV = 126.0     # READ  DG-2012: its 2 sigma holds "for M_h < 126 GeV"
TW_ALPHA_INV = (29.7, 30.0)     # READ  TW-size, the two pairings
RS96_ALPHA_INV = 29.0           # READ  RS96-2.8
RS96_PRINTED_LOG10 = -170.0     # READ  RS96-2.8
TW_PRINTED_LOG10 = -162.0       # READ  TW-size, printed with alpha_W ~ 1/30 (p.2)

# fragments quoted in this module's docstring, each against its source
QUOTED = (
    ("MRM-phi", "the masses of the W+/- and Z0 weak vector bosons and the "
                "fermions are proportional to phi"),
    ("FLAG-def", "The sigma_piN,s,c give the shift in M_N due to nonzero "
                 "light-, strange- and charm-quark masses"),
    ("Ji-cancel", "the contributions cancel each other in the limit of m_f -> "
                  "infinity"),
    ("Ji-eighth", "about 1/8"),
    ("RS96-sel", "the factor 1/3 comes from the baryon number of a quark, while "
                 "the factor 3 . 3 is due to colour and number of generations"),
    ("RS96-sel", "Delta N_e = Delta N_mu = Delta N_tau = (1/3) Delta B ; (B - L) "
                 "is conserved while (B + L) is violated"),
    ("RS96-T0", "At zero energies and temperatures, the transition between vacua "
                "with different n[omega] is a tunnelling event which is described "
                "by instantons"),
    ("RS96-sph", "the static saddle point solution to the Yang-Mills-Higgs "
                 "equations"),
    ("DRT-vev", "approximately zero"),
    ("DRT-vev", "at T < T_c GeV where it is finite"),
    ("DRT-broken", "in the physically interesting temperature range 130 GeV < T "
                   "< T_c"),
    ("MRM-SM", "EWBG is unable to explain the observed baryon asymmetry within "
               "the SM alone"),
    ("RS96-sel", "(B - L) is conserved"),
    ("FLAG-tension", "there is now a 2.7 sigma difference between the N_f = 2 + "
                     "1 and N_f = 2 + 1 + 1 FLAG averages"),
    ("BU-meta", "the Higgs vacuum does not reside in the configuration of minimal "
                "energy, but in a metastable state close to a phase transition"),
    ("BU-scale", "10^10-10^12 GeV"),
    ("BU-mt", "is excluded at 2.8 sigma"),
    ("BU-mt", "the main source of uncertainty in eq. (64) comes from M_t"),
    ("BU-life", "we cannot conclusively establish the fate of the EW vacuum"),
    ("BU-life", "we cannot conclusively establish the fate of the EW vacuum, "
                "although metastability is now preferred at 99.3% CL"),
    ("BU-life", "the SM vacuum is likely to survive for times that are enormously "
                "longer than any significant astrophysical age"),
    ("MRS-bubble", "at near the speed of light"),
    ("MRS-bubble", "releasing energy into the bubble wall"),
    ("MRS-bubble", "the different masses of fundamental particles in the bubble "
                   "interior"),
    ("MRS-bubble", "it expands at the speed of light, destroying everything in its "
                   "way"),
    ("Ji-table", "The largest uncertainty is from the matrix element <P|m_s ss|P>, "
                 "which could be larger than the difference of the two estimates "
                 "shown"),
    ("FLAG-tension", "unlikely to be due to the inclusion of charm quarks in the sea"),
    ("FLAG-tension", "The control of excited-state contributions remains an issue"),
    ("FLAG-HRKM23", "The N_f = 2 + 1 + 1 lattice average is in agreement with "
                    "Hoferichter et al"),
    ("DG-2012", "for M_h < 126 GeV"),
    ("DRT-Tc", "T_c = (159 +/- 1) GeV"),
    ("DRT-Tc", "In the interval 140 <~ T <~ 155 GeV"),
    ("DRT-Tc", "down to T ~ 130 GeV"),
    ("HW-folk", "an information-theoretic statement about state distinguishability"),
    ("HW-folk", "often interpreted as a fundamental limit on the information that "
                "can be stored by physical objects"),
    ("HW-folk", "this interpretation remains folklore rather than established fact"),
    ("BLRRT", "remains exponentially suppressed up to very high energies of at least "
              "30 sphaleron masses (250 TeV)"),
    ("BLRRT-PLB", "remains exponentially suppressed up to very high energies of at "
                  "least 30 sphaleron masses (250 TeV)"),
    ("BLRRT-conj", "although not proven rigorously"),
    ("KM-2020", "not more than ~ 30%"),
    ("KM-2020", "exponentially suppressed by at least e^(-(4 pi/alpha_w) 0.70)"),
    ("KM-2020", "there is no rigorous proof of exponentiation"),
    ("KM-2020", "based in part on an assumption that there are no additional "
                "exponentially growing"),
    ("TW-claim", "without the exponential tunneling suppression"),
    ("TW-2017", "with this estimate for a single sphaleron"),
    ("TW-2017", "the prevalent picture"),
    ("FFS-rebut", "regardless of the band structure"),
    ("FFS-rebut", "in the leading order of the WKB approximation"),
    ("TW-2017", "both estimates involve assumptions based on intuitions as well as "
                "approximations remaining to be fully justified"),
    ("TW-2017", "only an order of magnitude guesstimate"),
    ("TW-2017", "As argued at times in the literature (see e.g., Ref.[26] and "
                "recently in [27])"),
    ("TW-2017", "However, the above argument is somewhat misleading"),
    ("CMS", "An upper limit of 0.021"),
    ("TW-claim", "A very crude order of magnitude estimate"),
)

# Quotations in the docstring whose owner is a peer module, not a paper.
OWNER_TEXTS = {
    "excite.ELECTRON_MASS_IS_A_RULER": excite.ELECTRON_MASS_IS_A_RULER,
    "higgs.CAVEAT_B_AS_FIRST_WRITTEN": higgs.CAVEAT_B_AS_FIRST_WRITTEN,
}


def _norm(s):
    return re.sub(r"\s+", " ", s)


def _e(x, p):
    """%.pe with the exponent written as the docstring writes it: 6.2913e18."""
    return re.sub(r"e([+-])0*(\d)",
                  lambda m: "e" + ("-" if m.group(1) == "-" else "") + m.group(2),
                  "%.*e" % (p, x))


# ===================================================================== M65-1
def vev_gev():
    """v, asked of higgs.  From G_F: NAMED-NOT-READ."""
    return higgs.vev()


def yukawa(m_mev, v_gev=None):
    """y_f = sqrt(2) m_f / v.  H-TREE.  Inherits v's NAMED-NOT-READ."""
    v = vev_gev() if v_gev is None else v_gev
    return math.sqrt(2.0) * (m_mev / 1000.0) / v


def yukawas(masses=None):
    masses = MASS_MEV if masses is None else masses
    return {f: yukawa(masses[f]) for f in CHARGED_FERMIONS}


def consideration_holds(masses=None):
    """M's consideration, computed.  H-TREE: m_f = y_f v/sqrt(2), so any
    fermion of the payload with m_f > 0 forces phi != 0 where it is.  The
    payload's fermions are e, u, d.  Returns True iff one of them is massive
    in the capture."""
    masses = MASS_MEV if masses is None else masses
    return any(masses[f] > 0.0 for f in ("e", "u", "d"))


#: P-UNIFORM.  A NAMED PREMISE, not an owner's boolean: where nothing sources
#: it, the vev takes one value everywhere.  higgs.py's caveat (b) as it survives
#: DOCKET 63 F3 (asked below only for its words).  Supported by the constancy of
#: measured fermion masses, which is not read here.
P_UNIFORM = True
P_UNIFORM_STATUS = "PREMISE"
VEV_IS_UNIFORM = P_UNIFORM
CONSIDERATION_HOLDS = consideration_holds()
#: True everywhere with or without the elements, so it singles out no place.
CONSIDERATION_DISCRIMINATES = not VEV_IS_UNIFORM


# ---- the sign of D20's source, PROVED from the factorisation, not scanned
SIGN_INTERVALS = (   # (open interval of eps, a sample inside it, |phi| > v on it)
    ((None, 0), Fraction(-1), True),
    ((0, 1), Fraction(1, 2), False),
    ((1, 2), Fraction(3, 2), False),
    ((2, None), Fraction(3), True),
)


def source_factorisation_holds():
    """excite's derived source polynomial equals 4 eps (2-eps) (1-eps)^2
    coefficient by coefficient (both asked of excite, and the product rebuilt
    here from excite's own P and pmul).  Degree 4 with roots 0, 1, 1, 2: the
    sign is constant on each open interval between them."""
    P, pm = excite.P, excite.pmul
    rebuilt = [4 * x for x in pm(pm(P(0, 1), P(2, -1)), pm(P(1, -1), P(1, -1)))]
    return (list(excite.SOURCE_POLY) == list(excite.SOURCE_CLOSED) == rebuilt
            and len(rebuilt) == 5)


def source_sign_table():
    """[(interval, sign of the source there, |phi| > v there)].  Exact: one
    sample per interval suffices once the factorisation holds, and the
    boundaries of |1 - eps| = 1 (eps = 0, 2) are among the roots."""
    return [(iv, (excite.holding_terms(x)[0] > 0) - (excite.holding_terms(x)[0] < 0),
             above) for iv, x, above in SIGN_INTERVALS]


#: A source of POSITIVE rest energy raises |phi| above v somewhere?  THEOREM
#: within D20's model: the factorisation settles it on every interval.
SOURCE_CAN_RAISE_VEV = (not source_factorisation_holds()) or any(
    s > 0 and above for _iv, s, above in source_sign_table())
#: And a positive source CAN hold some eps: the field can be excited.
FIELD_CAN_BE_EXCITED = any(s > 0 for _iv, s, _a in source_sign_table())


def field_switched_on_by_arrival(vev_uniform=None, massive_matter_present=None,
                                 d15=None, d16=None):
    """C1 (SWITCH-ON and TEMPLATE).  Arrival switches the field on, or
    restores it to v, only if it was off or below v at the seat, or if a
    sourceless arrival could displace it.  The first is refuted by M65-1
    (massive matter present, P-UNIFORM: the unsourced field at the seat is at
    v) and, for below v, by H-UNSOURCED-SEAT (nothing at the seat holds
    |phi| below v before arrival); the second by D15 and D16 together (any
    lower value needs a local source).  A source that did hold it, released
    by the trigger, is TEMPLATE's priced remainder, the held-seat release
    route; within excite's section-3 model it does not reach SWITCH-ON's off
    state, which lies past D20's stability edge (a source whose mass rises
    convexly with |phi| could hold it; not computed).  Owner: this function; inputs D15, D16, P-UNIFORM; on
    TEMPLATE, H-UNSOURCED-SEAT."""
    vev_uniform = VEV_IS_UNIFORM if vev_uniform is None else vev_uniform
    present = CONSIDERATION_HOLDS if massive_matter_present is None else massive_matter_present
    d15 = excite.TAIL_RATE_IS_MASS if d15 is None else d15
    d16 = excite.DISPLACEMENT_IS_ULTRALOCAL if d16 is None else d16
    already_on = vev_uniform and present
    sourceless_change = not (d15 and d16)
    return (not already_on) or sourceless_change


FIELD_SWITCHED_ON_BY_ARRIVAL = field_switched_on_by_arrival()

#: READ: fermion masses are proportional to phi (MRM-phi), derived from the held
#: text, not typed.
MASS_PROPORTIONAL_TO_PHI = (_norm("and the fermions are proportional to phi")
                            in _norm(SOURCES["MRM-phi"][2]))
#: H-PRESENT is a CASE DEFINITION (it says which case STOCK is), named; the
#: masses it names are READ, the case itself is not a finding.
H_PRESENT_STATUS = "NAMED CASE DEFINITION; the masses it names are READ"
#: H-TREE (section 6), asked by specthm's SR5 so the placement names it: prior
#: mass (C5), C1's reason on TEMPLATE and the electrons' exact regain rest on it.
H_TREE_STATUS = ("NAMED HYPOTHESIS: m_f = y_f v/sqrt(2), at tree level in unitary "
                 "gauge, as the READ source states it; each Yukawa carries the "
                 "capture's mass scheme")
#: H-TREE-V (section 6), asked by specthm's SR5: C4's THEOREM, and so D29,
#: rests on it (C4's status says so; the selftest checks the two agree).
H_TREE_V_STATUS = ("NAMED HYPOTHESIS: the field-energy theorem is for the "
                   "tree-level potential; beyond it, what C4 needs is that v "
                   "stays a local minimum, which the stable and the READ "
                   "metastable case both keep")
#: D20'S MODEL (section 6), asked by specthm's SR5: D27's 'a source of positive
#: rest energy can only LOWER |phi|' and S10's and S13's movers rest on it.
D20_MODEL_STATUS = ("NAMED MODEL: a source whose mass comes from phi, rising "
                    "with |phi|, as every SM mass does; a source outside it (a "
                    "negative-sign portal coupling, say) could raise |phi|")


def trigger_gives_the_elements_their_mass(elements_massive=None, mass_prop_phi=None):
    """C5 (STOCK), PRIOR MASS.  STOCK puts the elements at the seat before
    anything arrives.  An element present with its measured mass (H-PRESENT)
    REQUIRES phi != 0 where it is, because its fermion masses are proportional
    to phi there (READ, H-TREE); so its Higgs-given mass is already given, and
    the trigger gives it nothing.  The link could hold only in a world where
    e, u, d were massless, and there C1 flips with it; elements at the seat
    without all or part of their Higgs-given mass (r < 1) are TEMPLATE's
    case, not STOCK's, and a seat above v (r > 1) leaves the trigger nothing
    to give either.  Inputs: the READ masses (e, u, d massive) and the READ
    proportionality.  It reads nothing that carries phi's value from
    elsewhere: the elements' own masses fix phi at their location."""
    massive = CONSIDERATION_HOLDS if elements_massive is None else elements_massive
    prop = MASS_PROPORTIONAL_TO_PHI if mass_prop_phi is None else mass_prop_phi
    already_given = massive and prop
    return not already_given


#: C5.  THEOREM on H-TREE and H-PRESENT; needs no P-UNIFORM.
TRIGGER_GIVES_THE_ELEMENTS_THEIR_MASS = trigger_gives_the_elements_their_mass()
_P_UNIFORM_NAMES = ("P_UNIFORM", "VEV_IS_UNIFORM", "vev_uniform",
                    "field_switched_on_by_arrival", "FIELD_SWITCHED_ON_BY_ARRIVAL",
                    "CONSIDERATION_DISCRIMINATES")


def reads_p_uniform(fn):
    """[the P-UNIFORM names fn's code or parameters use].  Empty means fn cannot
    depend on the premise."""
    names = set(fn.__code__.co_names) | set(fn.__code__.co_varnames)
    return sorted(n for n in _P_UNIFORM_NAMES if n in names)

# ===================================================================== M65-2
PAYLOAD_KG = inspect.signature(stock.feedstock_kg).parameters["payload_kg"].default
COMPOSITION = stock.HUMAN
Z_OF = gravity.symbol_to_Z()                                     # READ, AME2020
SHARE_INHERITS = "NAMED-NOT-READ (u = gravity.U_KG, stock.ATOMIC_MASS)"


def mass_number(el, shift=Fraction(0)):
    """A_e on H-A: the nearest integer to the standard atomic weight."""
    return Fraction(round(stock.ATOMIC_MASS[el])) + shift


def counts(payload_kg=None, comp=None, a_shift=Fraction(0)):
    """Exact rational counts over the listed elements.  Returns floats for
    B, N_e, N_p, N_n, and the listed mass fraction.  u and the atomic weights
    are NAMED-NOT-READ; Z is READ."""
    payload_kg = PAYLOAD_KG if payload_kg is None else payload_kg
    comp = COMPOSITION if comp is None else comp
    M = Fraction(repr(float(payload_kg)))
    u = Fraction(repr(U_KG))
    B = Ne = Fraction(0)
    for el, f in comp.items():
        atoms = Fraction(repr(f)) * M / (Fraction(repr(stock.ATOMIC_MASS[el])) * u)
        B += atoms * mass_number(el, a_shift)
        Ne += atoms * Z_OF[el]
    listed = sum(Fraction(repr(f)) for f in comp.values())
    return {"B": float(B), "N_e": float(Ne), "N_p": float(Ne),
            "N_n": float(B - Ne), "B_minus_L": float(B - Ne),
            "listed": float(listed), "unlisted": float(1 - listed)}


COUNTS = counts()


def valence_fractions(masses=None):
    """(proton, neutron): (2m_u + m_d)/m_p and (m_u + 2m_d)/m_n.  READ inputs."""
    m = MASS_MEV if masses is None else masses
    return ((2 * m["u"] + m["d"]) / m["p"], (m["u"] + 2 * m["d"]) / m["n"])


def sigma_fraction(sigma_pin, sigma_s, sigma_c=0.0):
    """f = (sigma_piN + sigma_s [+ sigma_c])/m_N -- the Feynman-Hellmann
    quark-mass part."""
    return (sigma_pin + sigma_s + sigma_c) / M_N_MEV


#: Both FLAG averages are READ; the 2.7 sigma between them is recorded and
#: neither is chosen (the verdict takes the larger).
SIGMA_MEASURES = {
    "FLAG 2+1+1": (SIGMA_PIN_2P1P1, SIGMA_S_2P1P1, "READ"),
    "FLAG 2+1": (SIGMA_PIN_2P1, SIGMA_S_2P1, "READ"),
}
F_LIGHT = {k: sigma_fraction(a, b) for k, (a, b, _s) in SIGMA_MEASURES.items()}
JI_FRACTION = {k: mev / M_N_MEV for k, mev in JI_QUARK_MASS_MEV.items()}


def coupling_sum(f_l):
    """sum over six quarks = 2/9 + (7/9) f_l.  EXACT over Fraction."""
    return Fraction(2, 9) + Fraction(7, 9) * f_l


def svz_heavy_sum(f_l):
    """3 x (2/27)(1 - f_l), the three heavy quarks by SVZ.  EXACT."""
    return 3 * Fraction(2, 27) * (1 - f_l)


def payload_masses(c=None, masses=None):
    """{line: kg} of the payload's rest-mass bookkeeping, closing exactly.
    nucleon rest masses + electron rest masses - binding = listed payload."""
    c = COUNTS if c is None else c
    m = MASS_MEV if masses is None else masses
    nuc = (c["N_p"] * m["p"] + c["N_n"] * m["n"]) * MEV_KG
    ele = c["N_e"] * m["e"] * MEV_KG
    listed = PAYLOAD_KG * c["listed"]
    return {"nucleon rest": nuc, "electron rest": ele,
            "binding (closure)": nuc + ele - listed, "listed payload": listed,
            "unlisted (H-LIST)": PAYLOAD_KG * c["unlisted"]}


def binding_sensitivity_kg(step=Fraction(1, 100)):
    """How far the binding closure moves when every mean nucleon number rises
    by `step`: the one figure H-A moves materially."""
    return (payload_masses(counts(a_shift=step))["binding (closure)"]
            - payload_masses()["binding (closure)"])


def share_rows(c=None):
    """[(measure, status of the fraction, fraction of the payload, what it is,
    inherits)].  Electrons first, then each nucleon measure on its own.  NEVER
    SUMMED ACROSS ROWS.  Every row is f x a counted rest mass / M, so every row
    INHERITS the counts' NAMED-NOT-READ."""
    pm = payload_masses(c)
    nuc, M = pm["nucleon rest"], PAYLOAD_KG
    cc = COUNTS if c is None else c
    val_kg = (cc["N_p"] * (2 * MASS_MEV["u"] + MASS_MEV["d"])
              + cc["N_n"] * (MASS_MEV["u"] + 2 * MASS_MEV["d"])) * MEV_KG
    inh = SHARE_INHERITS
    rows = [("electrons (all Higgs-given, H-TREE)", "MEASURED from READ",
             pm["electron rest"] / M, "electron rest mass", inh),
            ("nucleons: naive valence sum", "MEASURED from READ",
             val_kg / M, "valence current-quark masses only", inh)]
    for k, (_a, _b, st) in SIGMA_MEASURES.items():
        rows.append(("nucleons: sigma terms, %s" % k, st,
                     F_LIGHT[k] * nuc / M, "quark-mass part (Feynman-Hellmann)", inh))
    rows.append(("nucleons: chiQCD u,d,s condensate", "READ",
                 CHIQCD_QUARK_CONDENSATE / 100.0 * nuc / M, "lattice, proton", inh))
    for k in JI_QUARK_MASS_MEV:
        rows.append(("nucleons: Ji quark mass term, %s" % k, "READ",
                     JI_FRACTION[k] * nuc / M, "Ji Table I", inh))
    rows.append(("nucleons: sigma_piN + sigma_s + sigma_c (ETM 19)",
                 "CONTESTED as mass",
                 sigma_fraction(SIGMA_PIN_2P1P1, SIGMA_S_2P1P1, SIGMA_C_ETM19) * nuc / M,
                 "adds the charm sigma term", inh))
    for k in SIGMA_MEASURES:
        rows.append(("nucleons: six-quark coupling, %s" % k, "CONTESTED as mass",
                     float(coupling_sum(Fraction(F_LIGHT[k]))) * nuc / M,
                     "coupling incl. heavy-quark trace anomaly", inh))
    rows.append(("nucleons: six-quark coupling, Hoferichter", "CONTESTED as mass",
                 COUPLING_SUM_HRKM * nuc / M, "0.305(9), READ as a coupling", inh))
    return rows


def largest_central_reading(rows=None, read_only=False):
    """The LARGEST CENTRAL reading, electrons plus one nucleon measure.  Not a
    bound (uncertainties dropped), never a share.  read_only drops every
    CONTESTED row."""
    rows = share_rows() if rows is None else rows
    ele = rows[0][2]
    nucs = [r[2] for r in rows[1:]
            if not (read_only and r[1].startswith("CONTESTED"))]
    return ele + max(nucs)


MARGIN_SIGMAS = 3                # THIS FILE'S CHOICE for FLAG, not a stated uncertainty


def read_rows_margin_illustration():
    """An ILLUSTRATION OF MARGIN on the READ rows, not a bound: FLAG central +
    MARGIN_SIGMAS x (err_piN + err_s), linearly, no correlation assumed (the 3
    is this file's choice); Ji + his 10 MeV of omitted error + the 50 MeV
    difference of his two estimates, which he says his largest uncertainty
    "could be larger than" -- so even this is not Ji's uncertainty at its
    largest."""
    pm = payload_masses()
    nuc, M = pm["nucleon rest"], PAYLOAD_KG
    ele = share_rows()[0][2]
    cands = [sigma_fraction(a + MARGIN_SIGMAS * SIGMA_ERR[k][0],
                            b + MARGIN_SIGMAS * SIGMA_ERR[k][1])
             for k, (a, b, _s) in SIGMA_MEASURES.items()]
    cands += [(mev + JI_ROUNDING_MEV + JI_ESTIMATE_DIFFERENCE_MEV) / M_N_MEV
              for mev in JI_QUARK_MASS_MEV.values()]
    return ele + max(cands) * nuc / M


HIGGS_SHARE_LARGEST_ALL = largest_central_reading()
HIGGS_SHARE_LARGEST_READ = largest_central_reading(read_only=True)
HIGGS_SHARE_READ_MARGIN = read_rows_margin_illustration()
#: C2, AT FIRST ORDER (H-LINEAR): would a change of phi move MOST of atomic
#: mass?  Listed on DISPLACEMENT only; the finite share is OPEN (below).
HIGGS_SUPPLIES_MOST_ATOMIC_MASS = HIGGS_SHARE_LARGEST_ALL >= 0.5
#: Would C2 still refuse on the READ rows alone?  (It must, or it is
#: contested-only and cannot carry a refusal.)
C2_CONTESTED_ONLY = not (HIGGS_SHARE_LARGEST_READ < 0.5)
#: THE FINITE HIGGS SHARE -- the nucleon mass with phi at v, less the nucleon
#: mass with phi switched off (heavy-quark thresholds and the QCD scale moving
#: with it).  OPEN: not computed, not read.  Whether it exceeds half is
#: UNDECIDED here, so its comparison with one half is None, never a boolean.
#: No count reads it and no verdict rests on it.
FINITE_HIGGS_SHARE_STATUS = "OPEN"
FINITE_HIGGS_SHARE_EXCEEDS_HALF = None

# ===================================================================== M65-3
def rest_energy_j(kg=None):
    return warpfolder.rest_energy_j(PAYLOAD_KG if kg is None else kg)


# ---- THE ONLY CANDIDATE SOURCE IN M'S SENTENCE: the triggered field's energy about v
def field_energy_is_a_square():
    """V(v(1-eps)) - V(v) in units of rho_EW (excite.FIELD_POLY, equal to
    excite.FIELD_CLOSED) is exactly (eps (2 - eps))^2.  A real square: >= 0,
    zero only at eps = 0, 2, i.e. |phi| = v."""
    q = excite.P(0, 2, -1)
    return list(excite.FIELD_POLY) == list(excite.FIELD_CLOSED) == excite.pmul(q, q)


T00_GRID_MIN_POINTS = 3         # a degree-2 polynomial per axis needs 3 points


def t00_decomposes(grid=(-2, -1, 0, 1, 2), Vs=(Fraction(0), Fraction(1), Fraction(5, 3)),
                   tscalar=None):
    """higgs.T_scalar's T_00 equals (1/2) phi_t^2 + (1/2)|grad phi|^2 + V,
    exactly, at every point of the rational grid.  T_scalar is of degree two in
    each derivative and one in V, and the grid has five points per axis (it
    REFUSES fewer than three distinct points, and fewer than two V values), so
    agreement on it is agreement everywhere.  For the REAL scalar T_scalar
    models: the doublet and gauge terms are H-REAL."""
    if len(set(grid)) < T00_GRID_MIN_POINTS or len(set(Vs)) < 2:
        raise ValueError("grid too small to settle a degree-2 polynomial")
    tscalar = higgs.T_scalar if tscalar is None else tscalar
    half = Fraction(1, 2)
    for a in grid:
        for b in grid:
            for c_ in grid:
                for d in grid:
                    dphi = [Fraction(a), Fraction(b), Fraction(c_), Fraction(d)]
                    for V in Vs:
                        t00 = tscalar(dphi, V)[0][0]
                        want = half * dphi[0] ** 2 + half * (dphi[1] ** 2 + dphi[2] ** 2
                                                            + dphi[3] ** 2) + V
                        if t00 != want:
                            return False
    return True


FIELD_ENERGY_IS_A_SQUARE = field_energy_is_a_square()
T00_DECOMPOSES = t00_decomposes()
#: Can the field about v give up energy?  Only if some term of its energy
#: density above the vacuum could be negative.  THEOREM on H-TREE-V.
HIGGS_FIELD_RELEASES_ENERGY_ABOUT_V = not (FIELD_ENERGY_IS_A_SQUARE and T00_DECOMPOSES)


def _in(key, frag):
    return _norm(frag) in _norm(SOURCES[key][2])


#: The READ status of metastability, derived from the held text.
METASTABILITY_PREFERRED = _in("BU-life", "metastability is now preferred at 99.3% CL")
VACUUM_FATE_ESTABLISHED = not _in("BU-life", "we cannot conclusively establish the "
                                             "fate of the EW vacuum")
METASTABILITY_TURNS_ON_TOP_MASS = _in("BU-mt", "the main source of uncertainty in "
                                               "eq. (64) comes from M_t")
DECAY_CHANGES_PARTICLE_MASSES = _in("MRS-bubble", "the different masses of "
                                    "fundamental particles in the bubble interior")
DECAY_DESTROYS_WHAT_IT_MEETS = _in("MRS-bubble", "destroying everything in its way")
#: The one release (decay) forms atomic mass at the seat?  Refuted by the READ
#: text: inside the bubble the masses differ, and what it meets is destroyed.
VACUUM_DECAY_FORMS_ATOMIC_MASS_AT_THE_SEAT = not (DECAY_CHANGES_PARTICLE_MASSES
                                                  and DECAY_DESTROYS_WHAT_IT_MEETS)
def field_supplies_mass_energy(metastable, releases_about_v=None, decay_forms=None):
    """C4 (CREATION), case by case.  Stable: the only candidate is a release
    about v.  Metastable: that, or the one further release, vacuum decay."""
    rel = HIGGS_FIELD_RELEASES_ENERGY_ABOUT_V if releases_about_v is None else releases_about_v
    dec = VACUUM_DECAY_FORMS_ATOMIC_MASS_AT_THE_SEAT if decay_forms is None else decay_forms
    return rel or (metastable and dec)


def c4_combined(releases_about_v=None, decay_forms=None):
    """C4 over BOTH cases, stable or metastable: True if either case lets the
    field supply the mass-energy.  The top mass (which case holds) cannot reach
    it unless the two cases disagree."""
    return (field_supplies_mass_energy(True, releases_about_v, decay_forms)
            or field_supplies_mass_energy(False, releases_about_v, decay_forms))


#: C4.  THEOREM on H-TREE-V and H-REAL for the release about v; an INFERENCE
#: from READ text for the decay case.
HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY = c4_combined()

# ---- the carrier, and supporting note N-INFO (no verdict)
T_CMB = permute.T_CMB                  # CITED (Fixsen 2009 per permute.py)
R_BEKENSTEIN_M = 1.0                   # H-R


def landauer_bits(E=None, T=None):
    """Erased bits whose MINIMUM heat equals E, at T."""
    E = rest_energy_j() if E is None else E
    T = T_CMB if T is None else T
    return E / nopath.landauer_energy(1.0, T)


def bekenstein_bits(E=None, R=None):
    E = rest_energy_j() if E is None else E
    R = R_BEKENSTEIN_M if R is None else R
    return nopath.bekenstein_bits(R, E)


def bek_over_landauer_closed(R=None, T=None):
    """2 pi R k_B T/(hbar c): the ratio of the two counts, with no M in it."""
    R = R_BEKENSTEIN_M if R is None else R
    T = T_CMB if T is None else T
    return 2.0 * math.pi * R * nopath.KB * T / (nopath.HBAR * nopath.C)


def break_even_radius_m(T=None):
    T = T_CMB if T is None else T
    return nopath.HBAR * nopath.C / (2.0 * math.pi * nopath.KB * T)


N_INFO = ("SUPPORTING NOTE, NO VERDICT: by energy conservation a bit brings only "
          "its carrier's energy; Landauer prices erasure; Bekenstein bounds entropy "
          "by energy and size, and its reading as an information capacity is held "
          "as folklore (HW-folk).  It answers a link M did not state.")

# ===================================================================== M65-4
# Every Standard Model Yukawa term, as its field content with (B, L) charges.
# A bar is the conjugate field and carries the opposite charges.  (H carries
# none.)  The selftest computes the total charge of each term.
_Q = {"Q": (Fraction(1, 3), 0), "u_R": (Fraction(1, 3), 0),
      "d_R": (Fraction(1, 3), 0), "L": (0, 1), "e_R": (0, 1), "H": (0, 0)}
YUKAWA_TERMS = {
    "y_e  Lbar H e_R": (("L", -1), ("H", +1), ("e_R", +1)),
    "y_d  Qbar H d_R": (("Q", -1), ("H", +1), ("d_R", +1)),
    "y_u  Qbar Hc u_R": (("Q", -1), ("H", -1), ("u_R", +1)),
}
#: The anomaly vertex per the READ rule: one (q q q l) per generation.
THOOFT_VERTEX = tuple([("Q", +1)] * 3 * N_F + [("L", +1)] * N_F)


def term_charge(term):
    """(B, L) of a product of fields; sign +1 field, -1 conjugate."""
    B = sum(s * _Q[f][0] for f, s in term)
    L = sum(s * _Q[f][1] for f, s in term)
    return B, L


#: C3.  Some Higgs coupling carries net B or L?  Computed, term by term.  (The
#: couplings DO create fermions, in pairs; they carry no net B or L.)
HIGGS_COUPLING_CARRIES_B_OR_L = any(term_charge(t) != (0, 0)
                                    for t in YUKAWA_TERMS.values())
#: And the anomaly vertex does, by exactly N_F each: the READ rule reproduced.
THOOFT_DELTA_B_L = term_charge(THOOFT_VERTEX)


def mu_min_mev():
    """The least nuclear mass per nucleon in the AME2020 capture (measured
    rows), (A u + Delta - Z m_e)/A.  Electron binding is dropped, which only
    lowers the figure, so the floor built on it stays a floor.  Returns
    (MeV per nucleon, symbol, A)."""
    best = None
    for Z, _N, A, sym, d_kev, q in gravity.nuclides():
        if q != "M" or A < 1:
            continue
        mu = (A * U_MEV + d_kev / 1000.0 - Z * MASS_MEV["e"]) / A
        if best is None or mu < best[0]:
            best = (mu, sym, A)
    return best


MU_MIN = mu_min_mev()


def gravitational_binding_order(R=None):
    """G M/(R c^2): the order of gravitational binding against rest energy,
    for H-AME.  At R = 1 m (H-R).  No shape factor is claimed."""
    R = R_BEKENSTEIN_M if R is None else R
    return G_NEWTON * PAYLOAD_KG / (R * C ** 2)


def pair_floor_j(c=None):
    """Mc^2 + B mu_min c^2: the least energy that makes the payload from
    energy with B and L conserved.  THEOREM on B, L conservation and H-AME."""
    c = COUNTS if c is None else c
    return rest_energy_j() + c["B"] * MU_MIN[0] * MEV_J


def alpha_w(m_w_gev=None, v_gev=None):
    """g = 2 m_W / v, alpha_W = g^2 / 4 pi.  m_W READ; v NAMED-NOT-READ."""
    m_w = M_W_GEV if m_w_gev is None else m_w_gev
    v = vev_gev() if v_gev is None else v_gev
    g = 2.0 * m_w / v
    return g * g / (4.0 * math.pi), g


def log10_suppression(aw=None):
    """log10 exp(-4 pi / alpha_W), exactly the source's form."""
    aw = alpha_w()[0] if aw is None else aw
    return -(4.0 * math.pi / aw) / math.log(10.0)


def log10_suppression_g(g=None):
    """log10 exp(-16 pi^2 / g^2): the second form, computed independently."""
    g = alpha_w()[1] if g is None else g
    return -(16.0 * math.pi ** 2 / g ** 2) / math.log(10.0)


def transitions_needed(c=None):
    c = COUNTS if c is None else c
    return math.ceil(c["B"] / N_F)


def log10_attempts_times_prefactor(c=None):
    return math.log10(transitions_needed(c)) - log10_suppression()


def esph_formula_tev(B_fn):
    """(2 m_W / alpha_W) x B, TeV."""
    aw, _g = alpha_w()
    return 2.0 * M_W_GEV / aw * B_fn / 1000.0


def esph_over_three_baryons(tev):
    return tev * 1e6 / (N_F * MASS_MEV["p"])


def barrier_heights_over_mc2(c=None, tev=None):
    """The payload's transitions x E_sph, over Mc^2: a SUM OF BARRIER HEIGHTS,
    not a cost; whether the energy is recovered is not computed."""
    tev = E_SPH_TEV[E_SPH_USED] if tev is None else tev
    return transitions_needed(c) * tev * 1e6 * MEV_J / rest_energy_j()


def extra_leptons(c=None):
    """Leptons the anomaly route makes beyond the payload's electrons:
    N_F x transitions - N_e.  B - L conservation makes it N_n (to rounding)."""
    c = COUNTS if c is None else c
    return N_F * transitions_needed(c) - c["N_e"]


def electron_family_shortfall(c=None):
    """H-FLAV ONLY.  Delta N_e = Delta B/3 (READ); the payload holds N_e
    electrons.  Carries no verdict."""
    c = COUNTS if c is None else c
    return c["N_e"] - transitions_needed(c)


def t_kelvin(gev):
    return gev * higgs.GEV_IN_J / nopath.KB


def symmetric_rate_crosscheck(aw=None):
    """18 alpha_W^5 at this file's alpha_W: a CROSS-CHECK on the READ
    8.0(1.3)e-7 only, since the source absorbed ln alpha_W into the 18."""
    aw = alpha_w()[0] if aw is None else aw
    return RATE_COEFF_SYMM * aw ** 5


def broken_phase_ln_rate(t_gev):
    """ln(Gamma/T^4) = 0.83 T/GeV - 147.7, the READ fit, stated for
    130 GeV < T < T_c with T_c its own paper's 159 GeV (DRT-Tc), measured over
    140-155 GeV.  Refuses a temperature outside the stated range."""
    if not (BROKEN_FIT_LOW_GEV <= t_gev <= BROKEN_FIT_HIGH_GEV):
        raise ValueError("outside the READ fit's stated range")
    a, b = BROKEN_FIT
    return a * t_gev - b


#: The collider exponent, as the READ has it.  Never resolved here.
COLLIDER_RATE_STATUS = "CONTESTED"
#: Transitions keep running below T_c, where the vev is finite: derived from
#: the READ T* < T_c and the READ words.
SPHALERONS_RUN_WHERE_VEV_IS_FINITE = (T_FREEZE_GEV < min(T_C_GEV, BROKEN_FIT_HIGH_GEV)
                                      and _in("DRT-vev", "where it is finite"))
VEV_ABOVE_TC_IS_APPROXIMATELY_ZERO = _in("DRT-vev", "approximately zero")


def anomaly_route_priced():
    """The route is PRICED iff every figure of its price is a finite number."""
    figs = (transitions_needed(), log10_suppression(), barrier_heights_over_mc2(),
            extra_leptons(), broken_phase_ln_rate(T_FREEZE_GEV), RATE_SYMM_READ)
    return all(math.isfinite(float(x)) for x in figs)


ANOMALY_ROUTE_PRICED = anomaly_route_priced()


def pair_route_priced():
    """The pair route (EXCITATION's remainder) is PRICED iff its floor and the
    antibaryon number to be held apart are finite numbers, and the Higgs is not
    its source (C4 False: an intermediary, not the source)."""
    figs = (pair_floor_j(), pair_floor_j() / rest_energy_j(), COUNTS["B"])
    return all(math.isfinite(float(x)) for x in figs) and not HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY


PAIR_ROUTE_PRICED = pair_route_priced()
#: Would the pair route be refused on its antimatter by-product?  No premise
#: disqualifies it here; whether the antimatter can be held apart is not
#: computed.  Derived: the route is priced, not refused.
PAIR_ROUTE_REFUSED = not PAIR_ROUTE_PRICED


# ---- TEMPLATE's priced remainder: THE HELD-SEAT RELEASE ROUTE (round 6)
#: H-UNSOURCED-SEAT: nothing at the seat holds |phi| below v before arrival.
#: C1's premise on TEMPLATE, NAMED: M's sentence names no such source; only
#: the information arrives.  Not vacuous: FIELD_CAN_BE_EXCITED (D20).
H_UNSOURCED_SEAT = True
#: Where a positive source is a STABLE hold, not only an equilibrium (0 < |phi|
#: < v): above excite.stability_edge() in |phi|.  Computed, never typed.
STABLE_RANGE = "%.4f v < |phi| < v" % (1 - excite.stability_edge())
H_UNSOURCED_SEAT_STATUS = ("NAMED HYPOTHESIS of C1 on TEMPLATE; not vacuous: a "
                           "positive source is an equilibrium on 0 < |phi| < v and "
                           "a stable hold only on %s within excite's section-3 "
                           "model (source rest mass proportional to phi)" % STABLE_RANGE)
#: H-RELEASE: on the held-seat release route the trigger removes the prepared
#: source without doing work on the field or the elements.  What becomes of
#: the source's own rest energy is not computed.
H_RELEASE_STATUS = "NAMED HYPOTHESIS of the held-seat release route"
#: The eps the route is priced at: excite's chemically visible probe, ASKED.
HELD_SEAT_EPS = excite.EPS_CHEMICAL
def d23_row():
    """D23, asked of the ledger (the first trip), at call time: ledger.py asks
    this file for its rows while it is imported, so no module-level value here
    may need the ledger."""
    return [r for r in _ledger().DEMAND if r[0] == "D23"][0]


def preparation_needs_prior_arrival(row=None):
    """D23, asked of the ledger: a destination-side arrangement needed
    something to reach the destination at <= c first; its owner,
    transit.TRAVERSAL_IS_REMOVED, is False (the traversal is moved earlier,
    not removed).  A seat prepared in advance is such an arrangement."""
    row = d23_row() if row is None else row
    return (row[3] == ("transit", "TRAVERSAL_IS_REMOVED")
            and getattr(transit, row[3][1]) is False
            and "had to reach the destination at <= c" in _norm(row[1]))


def held_release_balance(eps, eps0):
    """Energy per unit volume in units of rho_EW, EXACT over Fraction, in D20's
    model (excite.holding_terms), with the elements' Higgs-given energy linear
    in phi (exact for the electrons on H-TREE; first order for the nucleons,
    H-LINEAR).  The elements alone hold eps0 (their own lowering, inside the
    measured mass), so at equilibrium their Higgs-given energy density at v is
    u = S(eps0)/(1 - eps0).  A prepared source holds eps > eps0; the trigger
    removes it (H-RELEASE) and phi relaxes to eps0.  The field gives up
    F(eps) - F(eps0), the elements regain u (eps - eps0), and the difference
    is radiated."""
    S0, F0 = excite.holding_terms(eps0)
    S, Fe = excite.holding_terms(eps)
    u = S0 / (1 - eps0)
    released = Fe - F0
    regained = u * (eps - eps0)
    return {"field at eps": Fe, "source at eps": S, "field released": released,
            "regained": regained, "radiated": released - regained}


def held_release_faults(eps, eps0s, balance=None):
    """[eps0] for every sampled eps0 at which the release does not balance as
    stated: radiated >= 0, regained <= F(eps), and S(eps)/regained >=
    excite.holding_ratio(eps) (per joule regained, at least that much
    phi-coupled rest energy sat at the seat).  Empty = the accounting holds
    exactly.  `balance` replaces held_release_balance for the controls."""
    balance = held_release_balance if balance is None else balance
    bad = []
    for e0 in eps0s:
        b = balance(eps, e0)
        if not (b["radiated"] >= 0 and b["regained"] <= b["field at eps"]
                and b["source at eps"] >= excite.holding_ratio(eps) * b["regained"]):
            bad.append(e0)
    return bad


#: eps0 samples for the balance: the elements' own lowering is tiny (excite:
#: 1e-18 per 2.2e11 kg/m^3 of Higgs-derived mass), so these span far above it.
HELD_RELEASE_EPS0 = (Fraction(1, 10 ** 12), Fraction(1, 10 ** 6), Fraction(1, 1000),
                     Fraction(1, 200))


def held_release_regained_shares(eps=None, eps0s=HELD_RELEASE_EPS0):
    """[(eps0, regained/released)], exact: of the energy the field RELEASES as
    |phi| relaxes to the elements' own lowering eps0, F(eps) - F(eps0), how
    much the elements regain; the rest of what it releases is radiated, and
    F(eps0) stays in the field."""
    eps = HELD_SEAT_EPS if eps is None else eps
    out = []
    for e0 in eps0s:
        b = held_release_balance(eps, e0)
        out.append((e0, b["regained"] / b["field released"]))
    return out


def regained_shares_text(shares=None):
    """The regained shares as the docstring and the report print them."""
    shares = held_release_regained_shares() if shares is None else shares
    fmt = lambda x: _e(float(x), 3) if x < Fraction(1, 100) else "%.4f" % x
    lab = lambda e0: str(e0) if e0.denominator <= 1000 else _e(float(e0), 0)
    return ("eps0 = %s: regained/released = %s" % (", ".join(lab(e0) for e0, _r in shares),
                                             ", ".join(fmt(r) for _e0, r in shares)))


def holding_ratio_form(source=None, field=None):
    """(S eps (2-eps) == 4 (1-eps)^2 F as polynomials, the limit of eps S/F as
    eps -> 0), from excite's own SOURCE_POLY and FIELD_POLY, exact over
    Fraction: excite.holding_ratio is 4(1-eps)^2/(eps(2-eps)), and 2/eps is
    only its small-eps limit."""
    s_ = list(excite.SOURCE_POLY) if source is None else list(source)
    f_ = list(excite.FIELD_POLY) if field is None else list(field)
    P, pm = excite.P, excite.pmul
    four = [4 * x for x in pm(P(1, -1), P(1, -1))]
    lhs, rhs = pm(s_, P(0, 2, -1)), pm(four, f_)
    n = max(len(lhs), len(rhs))
    same = all((lhs[i] if i < len(lhs) else 0) == (rhs[i] if i < len(rhs) else 0)
               for i in range(n))
    ok = len(s_) > 1 and len(f_) > 2 and s_[0] == 0 and f_[0] == f_[1] == 0 and f_[2] != 0
    return same, (Fraction(s_[1]) / Fraction(f_[2]) if ok else None)


def self_lowering_per_kg_m3():
    """eps per kg/m^3 of Higgs-derived mass, asked of excite (D20's owner,
    linear): EPS_AT_FIXTURE / HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18."""
    return excite.EPS_AT_FIXTURE / excite.HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18


def largest_read_nucleon_row(rows=None):
    """The largest central reading among the READ nucleon rows alone (electrons
    excluded): largest_central_reading(read_only=True) less the electrons."""
    rows = share_rows() if rows is None else rows
    return max(r[2] for r in rows[1:] if not r[1].startswith("CONTESTED"))


def held_seat_route(eps=None):
    """TEMPLATE's remainder where H-UNSOURCED-SEAT fails, every figure asked
    of its owner at `eps`: the prepared source (excite.holding_terms, D20),
    what it costs per joule of field (excite.holding_ratio), its Higgs-derived
    density (excite.exact_source_density), whether a static hold is stable
    there (excite.stability_edge), what the electrons regain (exact on H-TREE)
    and the first-order figure for the nucleons (eps x the largest READ nucleon
    row, an estimate, not a bound) and whether it forms baryons (C3).  Whether
    it needs a prior arrival (D23) is preparation_needs_prior_arrival(), asked
    of the ledger at call time and so not part of this dict, which is built at
    import (HELD_SEAT_ROUTE) while the ledger may be importing this file."""
    eps = HELD_SEAT_EPS if eps is None else eps
    S, Fe = excite.holding_terms(eps)
    return {
        "eps": eps,
        "source (rho_EW)": S, "field (rho_EW)": Fe,
        "source J/m^3": float(S) * excite.RHO_EW,
        "field J/m^3": float(Fe) * excite.RHO_EW,
        "source per J of field": excite.holding_ratio(eps),
        "Higgs-derived kg/m^3": excite.exact_source_density(eps),
        "stable": eps < excite.stability_edge(),
        "electrons regained": float(eps) * share_rows()[0][2],
        "nucleons first order": float(eps) * largest_read_nucleon_row(),
        "forms baryons": HIGGS_COUPLING_CARRIES_B_OR_L,
        "balance faults": held_release_faults(eps, HELD_RELEASE_EPS0),
    }


def held_seat_route_priced(route=None):
    """PRICED iff a positive source can hold the seat below v (D20), the hold
    is stable at the eps priced, every figure of the price is a finite
    positive number, and the energy balances exactly on every sample."""
    r = held_seat_route() if route is None else route
    figs = (r["source J/m^3"], r["field J/m^3"], float(r["source per J of field"]),
            r["Higgs-derived kg/m^3"], r["electrons regained"])
    return (FIELD_CAN_BE_EXCITED and r["stable"] and not r["balance faults"]
            and all(math.isfinite(x) and x > 0 for x in figs))


HELD_SEAT_ROUTE = held_seat_route()
HELD_SEAT_ROUTE_PRICED = held_seat_route_priced()


def held_seat_share_faults(route=None):
    """[] iff the nucleons' figure is eps x the largest READ nucleon row and,
    with the electrons', sums to eps x HIGGS_SHARE_LARGEST_READ (no double
    count of the electrons)."""
    r = HELD_SEAT_ROUTE if route is None else route
    e = float(r["eps"])
    out = []
    if r["nucleons first order"] != e * largest_read_nucleon_row():
        out.append("nucleons")
    if not math.isclose(r["electrons regained"] + r["nucleons first order"],
                        e * HIGGS_SHARE_LARGEST_READ, rel_tol=1e-12):
        out.append("sum")
    return out


#: The route, as printed wherever TEMPLATE's remainder is named.
HELD_SEAT_TEXT = (
    "the held-seat release route, where H-UNSOURCED-SEAT fails: a seat prepared "
    "in advance with a source holding |phi| below v, released by the arriving "
    "trigger (H-RELEASE); |phi| returns to v and the elements regain their "
    "Higgs-given mass.  It forms no baryons (C3: the elements were already "
    "there).  PRICED at eps = %s (excite.EPS_CHEMICAL): %s kg/m^3 of "
    "Higgs-derived mass where the templates sit, %.1f J of source rest energy "
    "per J of field (excite.holding_ratio).  Within excite's section-3 model (a "
    "static source of fixed number density whose rest mass is proportional to "
    "phi), a static "
    "hold is stable only on "
    "%s (excite.stability_edge): a TEMPLATE seat below that keeps no held-seat "
    "remainder.  The energy the field releases as |phi| relaxes to the elements' "
    "own lowering pays for the regained rest energy, "
    "which cannot exceed it, and the rest is radiated (with the elements' own "
    "lowering at %s), so per joule regained at least %.1f J of phi-coupled rest "
    "energy (the prepared source's with the elements') sat at the seat.  The "
    "electrons' part is regained exactly (%s of the payload at that eps, "
    "H-TREE); the nucleons' is eps times the first-order share at small eps "
    "(an estimate, not a bound) and, up to the stability edge, a finite "
    "response that is OPEN like the finite share.  It needs the seat prepared "
    "in advance, a prior arrival at <= c (D23)"
    % (HELD_SEAT_ROUTE["eps"], _e(HELD_SEAT_ROUTE["Higgs-derived kg/m^3"], 3),
       HELD_SEAT_ROUTE["source per J of field"], STABLE_RANGE, regained_shares_text(),
       HELD_SEAT_ROUTE["source per J of field"],
       _e(HELD_SEAT_ROUTE["electrons regained"], 3)))

# ===================================================================== M65-5
#: (id, pinned boolean name, owner, status, contested_only, what it answers).
#: True means the link the mechanism needs HOLDS on this count.
COUNTS_ON_THE_MECHANISM = (
    ("C1", "FIELD_SWITCHED_ON_BY_ARRIVAL",
     ("massform", "field_switched_on_by_arrival; inputs excite D15, D16, P-UNIFORM; "
                  "on TEMPLATE, H-UNSOURCED-SEAT"),
     "THEOREM (D15, D16) on P-UNIFORM; on TEMPLATE also on H-UNSOURCED-SEAT", False,
     "the field was off, or below v, at the seat and arrival turns it on or "
     "restores v"),
    ("C2", "HIGGS_SUPPLIES_MOST_ATOMIC_MASS",
     ("massform", "HIGGS_SHARE_LARGEST_READ"),
     "MEASURED from READ fractions, as first-order response (H-LINEAR); counts "
     "inherit NAMED-NOT-READ", C2_CONTESTED_ONLY,
     "at first order, a change of phi moves (most of) atomic mass"),
    ("C3", "HIGGS_COUPLING_CARRIES_B_OR_L",
     ("massform", "YUKAWA_TERMS"), "THEOREM (perturbative SM)", False,
     "what the triggered field makes carries the payload's net B"),
    ("C4", "HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY",
     ("massform", "c4_combined; T00_DECOMPOSES, FIELD_ENERGY_IS_A_SQUARE, READ decay text"),
     "THEOREM on H-TREE-V and H-REAL; inference from READ text for the decay case",
     False,
     "the triggered field supplies the energy of the mass"),
    ("C5", "TRIGGER_GIVES_THE_ELEMENTS_THEIR_MASS",
     ("massform", "trigger_gives_the_elements_their_mass; inputs CONSIDERATION_HOLDS "
                  "(READ masses), MASS_PROPORTIONAL_TO_PHI (READ)"),
     "THEOREM on H-TREE and H-PRESENT (PRIOR MASS); needs no P-UNIFORM", False,
     "the trigger gives the elements present at the seat (H-PRESENT) their "
     "Higgs-given mass"),
)

#: (reading, what M would mean, the counts that answer it).
READINGS = (
    ("SWITCH-ON", "arrival turns on a field that was off at the seat", ("C1",)),
    ("DISPLACEMENT", "EXCITATION: arrival displaces the field, and mass forms "
                     "from that", ("C2", "C3")),
    ("QUANTA", "EXCITATION: arrival makes Higgs quanta, and mass forms from them",
     ("C3",)),
    ("CREATION", "the triggered field supplies the energy of the mass that forms",
     ("C4", "C3")),
    ("STOCK", "the elements are at the seat and the triggered field gives them "
              "their mass -- read with the elements present as elements, i.e. "
              "with their measured mass (H-PRESENT)", ("C5",)),
    ("TEMPLATE", "STOCK's complement: templates at the seat without all or part "
                 "of their HIGGS-GIVEN mass (|phi| < v there before arrival), and "
                 "the triggered field restores it", ("C1",)),
)

#: {(reading, count): (answers?, the stated reason)}.  EVERY count on EVERY
#: reading carries a reason, listed or omitted; the selftest checks the table is
#: complete and agrees with READINGS, so no count is set against a reading
#: without an argument, and none is left off one without an argument either.
#: C2's scope on DISPLACEMENT (round 5, SF-4), stated once and guarded.
C2_SCOPE = ("a SMALL displacement only; a finite one is OPEN, and C3 carries the "
            "refusal regardless")
_C2_YES = ("at first order, with the QCD scale held fixed (H-LINEAR), only the "
           "quark-mass part moves")
_C2_FINITE = ("the reading asks what the field GIVES, a finite counterfactual with "
              "the field switched off or lowered (heavy-quark thresholds and the "
              "QCD scale moving); C2 measures only the first-order response (H-LINEAR), and "
              "the finite share is OPEN, not computed and not read")
_C2_NO = ("the whole mass-energy would come from the field or its quanta, the QCD "
          "share included, so how the nucleon's mass divides is silent")
_C3_YES = ("matter is made from the field or its energy, and no Higgs coupling "
           "carries net B or L")
_C4_NO = "this reading does not claim the field pays for the mass"
_C1_NO = ("C1 is about an off or lowered field at the seat, which this reading "
          "does not assume")
#: C1's reason on TEMPLATE, as the table states it (round 5, SF-3).
_C1_TEMPLATE = ("on P-UNIFORM the unsourced field at the seat is at v; any lower "
                "value needs a local source (D15, D16), and on H-UNSOURCED-SEAT "
                "nothing holds one there before arrival (M's sentence names no such "
                "source; only the information arrives); H-TREE")
#: The three-way split of the seat before arrival (round 6, A), stated once.
THREE_WAY = ("the split is three-way: before arrival the seat is r = |phi|/v < 1 "
             "(TEMPLATE, C1), r = 1 (STOCK on H-PRESENT, C5) or r > 1 (neither "
             "reading's claim: the trigger has nothing to give; holding r > 1 "
             "needs a source outside D20's model)")
#: H-PRESENT failing, as every mover states it (round 6, A).
H_PRESENT_FAILING = ("on H-PRESENT failing the case is TEMPLATE (r < 1) or a seat "
                     "above v (r > 1: nothing to give; needs a source outside D20's "
                     "model)")
#: What moves TEMPLATE, as every mover states it (round 6, B).
TEMPLATE_MOVES = ("TEMPLATE moves if C1 reverses: P-UNIFORM, D15 or D16 failing, or "
                  "H-UNSOURCED-SEAT failing (a source at the seat holding |phi| < v, "
                  "which the trigger releases: the held-seat release route, S13)")
#: The prior-mass argument, as the table states it (C5 on STOCK).
_C5_YES = ("PRIOR MASS: the elements are at the seat before anything arrives, and "
           "elements of measured mass REQUIRE phi != 0 where they are (READ: "
           "fermion masses are proportional to phi), so they already carry their "
           "Higgs-given mass; the trigger gives them nothing, and no mass forms.  "
           "Their own measured masses fix phi at their location, so this needs NO "
           "P-UNIFORM (H-TREE, H-PRESENT)")
READING_REASONS = {
    ("SWITCH-ON", "C1"): (True, "the reading needs the field off at the seat before "
                                "arrival; on P-UNIFORM it is already on (D15, D16)"),
    ("SWITCH-ON", "C2"): (False, _C2_FINITE),
    ("SWITCH-ON", "C3"): (False, "switching on claims no new B; it is silent"),
    ("SWITCH-ON", "C4"): (False, _C4_NO),
    ("SWITCH-ON", "C5"): (False, "SWITCH-ON does not place the elements at the seat "
                                 "before arrival; carrying the field's value to a seat "
                                 "where nothing massive is needs P-UNIFORM, which is "
                                 "C1 (read with the elements already seated, it is "
                                 "TEMPLATE at |phi| = 0, refused on C1)"),
    ("DISPLACEMENT", "C1"): (False, _C1_NO),
    ("DISPLACEMENT", "C2"): (True, "C2 answers " + C2_SCOPE + ": a small "
                                   "displacement is exactly a first-order response, "
                                   "so H-LINEAR applies and is the right measure "
                                   "there; " + _C2_YES + "; within D20's model a "
                                   "positive source only LOWERS |phi|"),
    ("DISPLACEMENT", "C3"): (True, _C3_YES),
    ("DISPLACEMENT", "C4"): (False, _C4_NO),
    ("DISPLACEMENT", "C5"): (False, "the reading claims mass forms from displacing a "
                                    "field already on, not that the trigger gives "
                                    "elements present at the seat (H-PRESENT) their "
                                    "mass; raising a mass already given is a "
                                    "displacement, which this reading's own counts, "
                                    "C2 and C3, answer"),
    ("QUANTA", "C1"): (False, _C1_NO),
    ("QUANTA", "C2"): (False, _C2_NO),
    ("QUANTA", "C3"): (True, _C3_YES + ": quanta decay to pairs"),
    ("QUANTA", "C4"): (False, "quanta are paid for by what makes them, and this "
                              "reading does not claim the field pays"),
    ("QUANTA", "C5"): (False, "the reading claims mass forms from quanta, not that "
                              "the trigger gives elements present at the seat "
                              "(H-PRESENT) their mass"),
    ("CREATION", "C1"): (False, _C1_NO),
    ("CREATION", "C2"): (False, _C2_NO),
    ("CREATION", "C3"): (True, _C3_YES),
    ("CREATION", "C4"): (True, "the reading claims the field supplies the energy; "
                               "about v it has none to give, and its one release "
                               "(decay) forms no atomic mass at the seat"),
    ("CREATION", "C5"): (False, "the reading claims the field pays for new mass, not "
                                "that the trigger gives elements present at the seat "
                                "(H-PRESENT) theirs"),
    ("STOCK", "C2"): (False, _C2_FINITE),
    ("STOCK", "C3"): (False, "the elements are already there; no B is made"),
    ("STOCK", "C4"): (False, "no mass-energy is created on this reading"),
    ("STOCK", "C5"): (True, _C5_YES),
    ("STOCK", "C1"): (False, "on H-PRESENT the elements' own measured masses fix phi "
                             "where they are, so no off or lowered state and no "
                             "P-UNIFORM enter; that is C5 (prior mass), not C1"),
    ("TEMPLATE", "C1"): (True, "templates without all or part of their Higgs-given "
                               "mass need |phi| < v at the seat before arrival (READ: "
                               "fermion masses are proportional to phi); " + _C1_TEMPLATE),
    ("TEMPLATE", "C2"): (False, _C2_FINITE),
    ("TEMPLATE", "C3"): (False, "the reading makes no new baryon number; it is "
                                "silent"),
    ("TEMPLATE", "C4"): (False, "the reading fails earlier, at the off or lowered "
                                "field C1 denies (on H-UNSOURCED-SEAT); where that "
                                "fails, the field energy that pays is what the "
                                "prepared source stored in it (the held-seat release "
                                "route), so the field is an intermediary, not the "
                                "source"),
    ("TEMPLATE", "C5"): (False, "C5 rests on H-PRESENT, which this reading denies"),
}

#: What remains of each reading once refused, and whether it is priced.
READING_REMAINDERS = {
    "SWITCH-ON": "none: the field is already on",
    "DISPLACEMENT": "the pair route (survivor b): atomic mass as matter with its "
                    "antimatter, the carrier paying the pair floor",
    "QUANTA": "the pair route (survivor b): atomic mass as matter with its "
              "antimatter, the carrier paying the pair floor",
    "CREATION": "the energy must come in the carrier",
    "STOCK": "survivor (a): reconstruction from stock, where no mass forms (the "
             "elements' mass is already given where they are)",
    "TEMPLATE": "survivor (d), " + HELD_SEAT_TEXT,
}


def reading_reason_table_complete(readings=None, reasons=None, counts=None):
    """[] iff every (reading, count) pair has a stated reason, the reason's
    answers-flag agrees with READINGS, and every reason is a real sentence."""
    readings = READINGS if readings is None else readings
    reasons = READING_REASONS if reasons is None else reasons
    counts = [c[0] for c in COUNTS_ON_THE_MECHANISM] if counts is None else counts
    bad = []
    for name, _w, cids in readings:
        for c in counts:
            r = reasons.get((name, c))
            if r is None:
                bad.append((name, c, "no stated reason"))
            elif r[0] != (c in cids):
                bad.append((name, c, "reason disagrees with the listing"))
            elif len(r[1].split()) < 5:
                bad.append((name, c, "reason too short to be an argument"))
    return bad


def derive_verdict(values, contested=None):
    """values: {count id: bool, True = the link holds on that count}.
    contested: {count id: bool, True = the count rests on a CONTESTED figure
    alone}.  REFUSED iff some non-contested count fails its link; OPEN iff only
    contested counts fail; STANDS iff none fails."""
    contested = {} if contested is None else contested
    failing = [k for k in sorted(values) if not values[k]]
    carried = [k for k in failing if not contested.get(k, False)]
    if carried:
        return "REFUSED", carried
    if failing:
        return "OPEN", failing
    return "STANDS", []


def mechanism_values():
    g = globals()
    return {cid: bool(g[name]) for cid, name, _o, _s, _c, _w in COUNTS_ON_THE_MECHANISM}


def mechanism_contested():
    return {cid: c for cid, _n, _o, _s, c, _w in COUNTS_ON_THE_MECHANISM}


def derive_readings(values=None, contested=None):
    """{reading: derive_verdict over the counts that answer that reading}."""
    values = mechanism_values() if values is None else values
    contested = mechanism_contested() if contested is None else contested
    return {name: derive_verdict({k: values[k] for k in cids},
                                 {k: contested.get(k, False) for k in cids})
            for name, _what, cids in READINGS}


def derive_mechanism(readings):
    """REFUSED iff every reading is refused; STANDS if any reading stands;
    OPEN otherwise."""
    verdicts = {r: v[0] for r, v in readings.items()}
    if all(v == "REFUSED" for v in verdicts.values()):
        return "REFUSED", sorted(verdicts)
    standing = sorted(r for r, v in verdicts.items() if v == "STANDS")
    if standing:
        return "STANDS ON A READING", standing
    return "OPEN", sorted(r for r, v in verdicts.items() if v == "OPEN")


READING_VERDICTS = derive_readings()
MECHANISM_VERDICT = derive_mechanism(READING_VERDICTS)

#: The readings whose remainder is a PRICED route on which atomic mass forms.
#: A refusal there is a refusal of NET formation only, and every printed
#: verdict says so (M's rule: never refuse a reading whose remainder is priced).
REMAINDER_FORMS_MASS = {"DISPLACEMENT": PAIR_ROUTE_PRICED, "QUANTA": PAIR_ROUTE_PRICED}
#: The reading whose remainder is a PRICED route that RESTORES the Higgs-given
#: mass of elements already there (no baryon forms): TEMPLATE, where
#: H-UNSOURCED-SEAT fails.  Its refusal is a refusal on that premise only.
REMAINDER_RESTORES_MASS = {"TEMPLATE": HELD_SEAT_ROUTE_PRICED}
#: A count listed on a reading for part of it only: printed after the others,
#: with its scope, so a headline never reads stronger than the count.
COUNT_SCOPE = {("DISPLACEMENT", "C2"): "for a small displacement only"}


def reading_premises(name, verdicts=None, c1_status=None, any_count=False):
    """The named premises a reading refused on ONE count rests on, ASKED of
    that count's status.  On C1: 'on P-UNIFORM' gives P-UNIFORM, and 'on
    <reading> also on <H>' adds that hypothesis (H-UNSOURCED-SEAT on TEMPLATE).
    With any_count, a refusal on any other single count whose status reads
    'THEOREM ... on <H-...> [and <H-...>]' gives those tokens, less the
    reading's own case definition (reading_case_definition: H-PRESENT defines
    the STOCK case, so it is not a premise of C5's refusal but its case).  So
    SWITCH-ON's, TEMPLATE's and STOCK's refusals are printed on their premises,
    never unconditional -- the same limit mechanism_label() prints."""
    v, cs = (READING_VERDICTS if verdicts is None else verdicts)[name]
    statuses = dict((c[0], c[3]) for c in COUNTS_ON_THE_MECHANISM)
    c1 = statuses["C1"] if c1_status is None else c1_status
    if v != "REFUSED" or len(cs) != 1:
        return []
    if list(cs) == ["C1"]:
        prem = ["P-UNIFORM"] if "on P-UNIFORM" in c1 else []
        m = re.search(r"on %s also on ([A-Z][\w-]*)" % re.escape(name), c1)
        return prem + ([m.group(1)] if m else [])
    if not any_count:
        return []
    m = re.match(r"THEOREM\b[^;]*? on ((?:[HP]-[A-Z-]+)(?:(?:,| and) [HP]-[A-Z-]+)*)",
                 statuses[cs[0]])
    toks = re.findall(r"[HP]-[A-Z-]+", m.group(1)) if m else []
    return [t for t in toks if t not in reading_case_definition(name)]


def reading_case_definition(name):
    """The hypotheses a reading's OWN case is defined by, asked of READINGS'
    text for it ('with their measured mass (H-PRESENT)' on STOCK)."""
    what = [w for n, w, _c in READINGS if n == name]
    return re.findall(r"\b[HP]-[A-Z][A-Z-]*[A-Z]\b", what[0]) if what else []


def reading_label(name, verdicts=None, c1_status=None):
    v = (READING_VERDICTS if verdicts is None else verdicts)[name][0]
    prem = reading_premises(name, verdicts, c1_status)
    if v == "REFUSED" and REMAINDER_FORMS_MASS.get(name):
        return "REFUSED as net formation; remainder the pair route, PRICED"
    if v == "REFUSED" and REMAINDER_RESTORES_MASS.get(name):
        return ("REFUSED on %s; remainder the held-seat release route, PRICED"
                % " and ".join(prem or ["H-UNSOURCED-SEAT"]))
    if prem:
        return "REFUSED on %s (C1 alone)" % " and ".join(prem)
    return v


def reading_row(name, verdicts=None):
    """The report's row for a reading: 'REFUSED on C3 (C2 for a small
    displacement only) -- as net formation; remainder the pair route, PRICED'
    -- the counts first, a scoped count after the others with its scope, then
    the qualification, so the counts are never read as the remainder's."""
    v, cs = (READING_VERDICTS if verdicts is None else verdicts)[name]
    whole = [c for c in cs if (name, c) not in COUNT_SCOPE]
    part = ["%s %s" % (c, COUNT_SCOPE[(name, c)]) for c in cs if (name, c) in COUNT_SCOPE]
    row = "%s on %s" % (v, ", ".join(whole)) if whole else v
    if part:
        row += " (%s)" % "; ".join(part)
    prem = reading_premises(name, verdicts)
    if v == "REFUSED" and REMAINDER_FORMS_MASS.get(name):
        row += " -- as net formation; remainder the pair route, PRICED"
    elif v == "REFUSED" and REMAINDER_RESTORES_MASS.get(name):
        row += (" -- on %s; remainder the held-seat release route, PRICED"
                % " and ".join(prem or ["H-UNSOURCED-SEAT"]))
    elif prem:
        row += " -- on %s" % " and ".join(prem)
    return row


def mechanism_label():
    v, rs = MECHANISM_VERDICT
    pair = [r for r in rs if v == "REFUSED" and REMAINDER_FORMS_MASS.get(r)]
    held = [r for r in rs if v == "REFUSED" and REMAINDER_RESTORES_MASS.get(r)]
    out = "%s on %s" % (v, ", ".join(rs))
    # A reading refused on C1 alone, outside the held-seat case, is refused on
    # C1's premise: C1 is a THEOREM on P-UNIFORM (its status is asked), so the
    # label says so beside TEMPLATE's scope, and never reads unconditional.
    c1 = dict((c[0], c[3]) for c in COUNTS_ON_THE_MECHANISM)["C1"]
    prem = [r for r in rs if v == "REFUSED" and READING_VERDICTS[r][1] == ["C1"]
            and not REMAINDER_RESTORES_MASS.get(r) and "on P-UNIFORM" in c1]
    if prem:
        out += "; on %s on P-UNIFORM (C1 alone)" % ", ".join(prem)
    # A reading refused on ONE other count is refused on that count's own
    # premises, asked of its status (STOCK on C5, a THEOREM on H-TREE, with
    # H-PRESENT defining the STOCK case), so beside SWITCH-ON's and TEMPLATE's
    # scoped refusals it never reads unconditional.
    for r in rs:
        cs = READING_VERDICTS[r][1]
        if v != "REFUSED" or len(cs) != 1 or list(cs) == ["C1"]:
            continue
        p = reading_premises(r, any_count=True)
        if p:
            d = reading_case_definition(r)
            out += "; on %s on %s (%s alone%s)" % (
                r, " and ".join(p), cs[0],
                ("; %s is its case definition" % " and ".join(d)) if d else "")
    if pair:
        out += ("; on %s as NET formation only -- atomic mass can still form there as "
                "matter with its antimatter (the pair route, PRICED)" % ", ".join(pair))
    if held:
        out += ("; on %s on P-UNIFORM and H-UNSOURCED-SEAT -- where the latter "
                "fails, a seat prepared in advance can still have its elements' Higgs-given mass restored on arrival (the "
                "held-seat release route, PRICED; it forms no baryons)" % ", ".join(held))
    return out


def derive_consideration(holds=None, discriminates=None, uniform=None):
    """The consideration's verdict.  Its second half rests on P-UNIFORM (a
    PREMISE): it discriminates nothing BECAUSE the vev is uniform, so where
    that is the reason the verdict says so, and never reads unconditional."""
    holds = CONSIDERATION_HOLDS if holds is None else holds
    discriminates = CONSIDERATION_DISCRIMINATES if discriminates is None else discriminates
    uniform = VEV_IS_UNIFORM if uniform is None else uniform
    if not holds:
        return "NOT ESTABLISHED"
    if discriminates:
        return "TRUE"
    return ("TRUE, AND, ON P-UNIFORM, DISCRIMINATES NOTHING" if uniform
            else "TRUE, AND DISCRIMINATES NOTHING")


CONSIDERATION_VERDICT = derive_consideration()

SURVIVES = (
    ("reconstruction from destination stock",
     "stockgate.GATE is the condition; transit.CARRIES_SUBSTANCE = %s.  No mass "
     "forms at the seat: the stock's masses are already given where the stock "
     "is, by phi there (prior mass, C5; on H-PRESENT no P-UNIFORM is needed).  "
     "The Higgs's part "
     "is a precondition already met -- M's consideration -- not a trigger.  S5 "
     "and D25 unchanged."
     % transit.CARRIES_SUBSTANCE),
    ("the pair route",
     "EXCITATION's remainder.  Atomic mass forms as matter with its antimatter.  "
     "PRICED in M65-4: the carrier supplies at least %.4f Mc^2 (%s J); %s units "
     "of antibaryon number are held apart; the Higgs is an intermediary, not "
     "the source (C4).  Nothing is refused on the antimatter by-product; whether "
     "it can be held apart is not computed."
     % (pair_floor_j() / rest_energy_j(), _e(pair_floor_j(), 4), _e(COUNTS["B"], 4))),
    ("the anomaly route",
     "B + L violated by the SU(2) anomaly, crossed over a gauge-Higgs saddle "
     "whose height the vev sets (E_sph = (4 pi v/g) B).  PRICED in M65-4: "
     "INSTANTON tunnelling at zero temperature (the exp(-4 pi/alpha_W) factor); "
     "the SPHALERON thermally (above T_c and in the broken-phase window down to "
     "T*); the two-particle collider rate is %s and is not resolved."
     % COLLIDER_RATE_STATUS),
    ("the held-seat release route",
     "TEMPLATE's remainder, and the reading closest to M's mechanism -- "
     + HELD_SEAT_TEXT + ".  The Higgs is an intermediary, holding what the source "
     "stored, not the source (C4); nothing is refused on the source's fate at "
     "release (H-RELEASE), which is not computed."),
)
RECONSTRUCTION_SURVIVES = (not transit.CARRIES_SUBSTANCE) and bool(stockgate.GATE)
NOTHING_IS_REPAIRED = True
EDITS_A_PEER = False

# ------------------------------------------------------------- proposed rows
PROPOSED_ROWS = (
    ("D27", "DEMAND",
     "M's consideration, computed: fermion masses are proportional to phi "
     "(READ, 1206.2942), so wherever the payload's elements exist with their "
     "measured masses the vev is nonzero there.  On P-UNIFORM (a named premise: "
     "the vev takes one value wherever nothing sources it) the condition holds "
     "everywhere and singles out no seat; arrival switches nothing on.  A "
     "change at the seat needs a local source (D15, D16).  Within D20's model "
     "(source mass rising with |phi|, true of every SM mass) a source of "
     "positive rest energy can only LOWER |phi|: D20's source term "
     "4 eps(2-eps)(1-eps)^2 is positive only where 0 < |phi| < v, proved from "
     "the factorisation.  On the STOCK reading the elements are at the seat "
     "before anything arrives, and with their measured masses (H-PRESENT) they "
     "already carry their Higgs-given mass, so a trigger gives them nothing "
     "(PRIOR MASS, C5; on H-PRESENT it needs no P-UNIFORM, since their own "
     "masses fix phi where they are).  On TEMPLATE, templates at the seat "
     "without all or part of their Higgs-given mass (|phi| < v there before "
     "arrival), C1 refuses: " + _C1_TEMPLATE + ".  H-PRESENT or not, " + THREE_WAY
     + ".  Where H-UNSOURCED-SEAT fails, TEMPLATE's remainder is the held-seat "
     "release route (S13), priced",
     "THEOREM", ("massform", "CONSIDERATION_HOLDS"),
     "a fermion mass not proportional to phi at tree level (H-TREE fails); a "
     "failure of P-UNIFORM or of D15/D16's hypotheses; a source outside D20's "
     "model; FIELD_SWITCHED_ON_BY_ARRIVAL is the boolean that would flip.  For "
     "prior mass: H-TREE failing; TRIGGER_GIVES_THE_ELEMENTS_THEIR_MASS would "
     "flip.  On H-PRESENT failing the case is TEMPLATE (r < 1) or a seat above v "
     "(r > 1: nothing to give; needs a source outside D20's model).  "
     + TEMPLATE_MOVES + ".  SWITCH-ON moves if C1 reverses (P-UNIFORM, D15 or D16); "
     "within excite's section-3 model (source rest mass proportional to phi) "
     "H-UNSOURCED-SEAT failing does not reach it, since the off state lies past "
     "D20's stability edge, where no static hold stands; a source whose mass "
     "rises convexly with |phi| (not computed) could hold it, and with the "
     "elements seated that is TEMPLATE at |phi| = 0"),
    ("D28", "DEMAND",
     "Forming the payload from energy with B and L conserved costs at least "
     "Mc^2 + B mu_min c^2 (mu_min the least nuclear mass per nucleon among "
     "AME2020's measured nuclides; gravitational binding, of order G M/(R c^2), "
     "negligible at payload scale) and leaves B units of antibaryon number to "
     "be held apart.  The payload's B - L = N_n must be balanced by -N_n "
     "outside it: on the pair route that balance is the antimatter; on a "
     "B-violating, B-L-conserving route that makes no antibaryons (the anomaly "
     "route), it is N_n extra leptons",
     "THEOREM", ("massform", "pair_floor_j"),
     "B - L violation (a Majorana neutrino mass; H-BL); a bound state lighter "
     "per baryon than 56Fe (H-AME); the numbers move with gravity.U_KG and "
     "stock.ATOMIC_MASS, both NAMED-NOT-READ"),
    ("D29", "DEMAND",
     "The Higgs field has no energy to give about v: its energy density above "
     "the vacuum, (1/2)phi_t^2 + (1/2)|grad phi|^2 + rho_EW eps^2(2-eps)^2, is "
     "a sum of squares (higgs.T_scalar, excite.FIELD_POLY), so any change of "
     "phi about v costs energy.  Proved for the real scalar higgs.T_scalar "
     "models; that the doublet's other components and the gauge fields add "
     "only non-negative terms is H-REAL, claimed and not computed.  Its one "
     "release is decay of a metastable vacuum, which is preferred at the "
     "central measured masses but not established (top-mass dependent, READ "
     "1307.3536).  That decay forms no atomic mass at the seat is an INFERENCE "
     "from READ text (1809.06923: a bubble expanding at near c, with different "
     "particle masses inside, destroying what it meets)",
     "THEOREM", ("massform", "HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY"),
     "a potential whose electroweak minimum is not a local minimum; H-REAL "
     "failing (a doublet or gauge term of negative energy density); a source "
     "reading vacuum decay as forming atomic mass.  The top mass does not move "
     "it: the case split covers both stable and metastable"),
    ("S10", "SUPPLY",
     "M's mechanism, \"As soon as the information hits the seat, it triggers "
     "the higgs field, and atomic mass forms\", as a supply of payload mass.  "
     # The verdict word is the owner's, MECHANISM_VERDICT[0], never typed.
     + MECHANISM_VERDICT[0]
     + ", gap None, reading by reading, on no contested-only count, and "
     "each count only where it has a stated reason to answer: SWITCH-ON by C1 "
     "alone (the field is already on, D27, on P-UNIFORM); EXCITATION, "
     "displacement branch, by C3, and by C2 for " + C2_SCOPE + " (the field "
     "can be excited, at a cost, lowering |phi|; at first order, H-LINEAR, the "
     "largest central reading is 0.172 of atomic mass on the READ rows and "
     "0.309 on all rows, and an illustration of margin reaches 0.236 on the "
     "READ rows, none a bound; no Higgs coupling carries net B or L); "
     "EXCITATION, quanta branch, by C3 alone; CREATION by C4 (the field has no "
     "energy to give about v, and its one release, vacuum decay, forms no atomic "
     "mass at the seat, D29) and C3; STOCK, with the elements present as "
     "elements (H-PRESENT), by C5 alone, PRIOR MASS (they already carry their "
     "Higgs-given mass, since fermion masses are proportional to phi where they "
     "are; on H-PRESENT it needs no P-UNIFORM); TEMPLATE, its complement "
     "(templates at the seat without all or part of their Higgs-given mass, "
     "|phi| < v there before arrival), by C1 alone: " + _C1_TEMPLATE + ".  "
     "H-PRESENT or not, " + THREE_WAY + ".  EXCITATION is "
     "refused as NET formation only: what remains is the pair route (S12), "
     "priced.  TEMPLATE is refused on P-UNIFORM and H-UNSOURCED-SEAT; where the "
     "latter fails, what remains is the held-seat release route (S13), priced, "
     "which forms no baryons.  What "
     "remains of STOCK is reconstruction from stock.  OPEN, and "
     "no verdict rests on it: the FINITE Higgs share, what the field gives "
     "with it switched off, not computed and not read; whether it exceeds half "
     "is undecided here (S10 (open)); STOCK is refused on C5, SWITCH-ON and "
     "TEMPLATE on C1, and DISPLACEMENT on C3 regardless",
     MECHANISM_VERDICT[0], ("massform", "MECHANISM_VERDICT"),
     "STOCK moves only if H-TREE fails; " + H_PRESENT_FAILING + "; "
     + TEMPLATE_MOVES + "; SWITCH-ON moves if C1 reverses (P-UNIFORM, D15 or "
     "D16), or if a source outside excite's section-3 model (mass rising "
     "convexly with |phi|; not computed) holds the seat off; QUANTA if C3 "
     "reverses; DISPLACEMENT "
     "needs C3, and C2 as well for a small displacement (a finite one reaches "
     "the finite share, OPEN; within D20's model a positive source only lowers "
     "|phi|); CREATION needs C4 and C3.  The finite Higgs share, OPEN (a "
     "candidate question for a future docket): computed or read, it would say "
     "how much of atomic mass the field gives; it moves no refusal here, since "
     "no count reads it and C2 is listed only where a first-order response is "
     "the measure"),
    ("S11", "SUPPLY",
     "The anomaly route: B + L violated by the SU(2) anomaly over a gauge-Higgs "
     "saddle whose height the vev sets.  Zero temperature: INSTANTON "
     "tunnelling, exp(-4 pi/alpha_W) per transition, alpha_W from READ m_W and "
     "v (NAMED-NOT-READ, via G_F); B/3 transitions.  Over the barrier, the SPHALERON: E_sph ~ %.0f TeV "
     "(READ), ~%s x the 3 baryons' rest energy.  Thermal: unsuppressed above "
     "T_c, vev approximately zero; below T_c down to T*, the READ broken-phase "
     "rate with the vev finite.  Two-particle collisions: CONTESTED (the "
     "prevalent semiclassical results find exponential suppression; Tye-Wong "
     "dissent; CMS decides nothing).  It must emit N_n "
     "extra leptons (D28)"
     # Both figures ASKED of their owners (E_SPH_TEV, esph_over_three_baryons);
     # row_figures() regenerates them, so a typed copy cannot drift green.
     % (E_SPH_TEV[E_SPH_USED], _e(esph_over_three_baryons(E_SPH_TEV[E_SPH_USED]), 1)),
     "OPEN", ("massform", "ANOMALY_ROUTE_PRICED"),
     "a READ prefactor (turns the exponent into a rate); a settlement of the "
     "collider-energy dispute (Tye-Wong against Bezrukov et al., Khoze-Milne "
     "and Funakubo et al.): Bezrukov et al. and Khoze-Milne rest on conjectures "
     "or assumptions they state as unproven; Funakubo et al. argue \"in the "
     "leading order of the WKB approximation\"; Tye-Wong state that \"both "
     "estimates involve assumptions based on intuitions as well as "
     "approximations remaining to be fully justified\" and call their own "
     "figure \"only an order of magnitude guesstimate\"; a READ G_F (lifts "
     "alpha_W's NAMED-NOT-READ)"),
    ("S12", "SUPPLY",
     "The pair route, EXCITATION's remainder: atomic mass forms as matter with "
     "its antimatter, B and L conserved.  The carrier supplies at least the "
     "pair floor Mc^2 + B mu_min c^2 (D28); B units of antibaryon number are "
     "held apart; the Higgs, where it appears, is an intermediary, not the "
     "source (D29).  Priced, not refused: no premise here disqualifies an "
     "antimatter by-product",
     "OPEN", ("massform", "PAIR_ROUTE_PRICED"),
     "a way to hold the antibaryons apart (not computed here); H-BL or H-AME "
     "failing (moves the floor); the Higgs field shown to supply energy (D29 "
     "reversed)"),
    ("S13", "SUPPLY",
     "TEMPLATE's remainder and the reading closest to M's mechanism -- "
     + HELD_SEAT_TEXT + ".  The field releases F(eps) - F(eps0), with F = "
     "rho_EW eps^2(2-eps)^2 per unit volume, as |phi| relaxes to the elements' "
     "own lowering eps0 (excite.holding_terms); by energy conservation, the source removed "
     "without doing work (H-RELEASE), that pays for the regained rest energy "
     "and the rest is radiated, checked exactly over Fraction.  Within excite's "
     "section-3 model (source rest mass proportional to phi) a static hold is "
     "stable only below eps = %.4f (excite.stability_edge)"
     % excite.stability_edge(),
     "OPEN", ("massform", "HELD_SEAT_ROUTE_PRICED"),
     "a way to prepare and release the source at the seat (not computed here); "
     "what becomes of the source's own rest energy at release (H-RELEASE); the "
     "finite response of the nucleon mass to |phi| (OPEN, like the finite share "
     "of S10 (open)), which sets what the nucleons regain up to the stability "
     "edge; H-UNSOURCED-SEAT holding in the case at hand, which closes the "
     "route; a source outside D20's model; a source whose mass rises convexly "
     "with |phi| (outside excite's section-3 model; not computed), which could "
     "extend the route below the stability edge"),
    ("S10 (open)", "SUPPLY",
     "OPEN ITEM, a candidate question for a future docket: the FINITE Higgs share "
     "of atomic mass -- the nucleon mass with phi at v, less the nucleon mass "
     "with phi switched off, where the heavy-quark thresholds and the QCD scale "
     "move too.  Not computed and not read here; whether it exceeds half is "
     "undecided here.  The first-order (sigma-term) measures of C2 do not settle "
     "it (H-LINEAR).  No DOCKET 65 verdict rests on it: STOCK is refused on prior "
     "mass (C5), SWITCH-ON and TEMPLATE on C1, and DISPLACEMENT on C3 "
     "regardless",
     "OPEN", ("massform", "FINITE_HIGGS_SHARE_STATUS"),
     "a computation of the nucleon mass with the field switched off, or a READ "
     "source giving it; nothing in DOCKET 65 moves on it"),
    ("S5 (note)", "SUPPLY",
     "APPEND to S5's note: DOCKET 65 -- reconstruction from destination stock "
     "survives M's mechanism: no mass forms at the seat and the Higgs plays no "
     "triggering role (massform.RECONSTRUCTION_SURVIVES)",
     "OPEN (unchanged)", ("massform", "RECONSTRUCTION_SURVIVES"),
     "nothing in DOCKET 65; S5's own owed items stand"),
)
#: Not opened, and why (one row per question).  The finite Higgs share is
#: here as M approved it: the seating first opened it as a ledger row (O8), and
#: M ruled M-D65-2, 'Fold into S10 (Recommended)' -- an open item inside S10's
#: note, not a separate row (ledger.RULED_BY_M; the board's principle for
#: opening a row, ledger.py docstring section 4).
NOT_OPENED = ("the first-order Higgs share as one figure (C2 of S10 prints only "
              "measures)",
              "the finite Higgs share (OPEN: not computed, not read; whether it "
              "exceeds half is undecided here; S10 (open), a candidate question "
              "for a future docket)",
              "the information counts (supporting note N-INFO; no verdict)",
              "how the held-seat source is prepared and released, and what becomes "
              "of its rest energy (H-RELEASE; S13)",
              "the electron-family shortfall (H-FLAV only)")


# ================================================================ doc figures
def doc_figures():
    """[(label, the string the docstring prints)], each regenerated now from its
    computation.  The guard (doc_figure_guard) is two-sided."""
    c = COUNTS
    vp, vn = valence_fractions()
    aw, _g = alpha_w()
    return [
        ("electron share", _e(share_rows()[0][2], 3)),
        ("f_l FLAG 2+1+1", "%.2f %%" % (100 * F_LIGHT["FLAG 2+1+1"])),
        ("f_l FLAG 2+1", "%.2f %%" % (100 * F_LIGHT["FLAG 2+1"])),
        ("Ji m_s -> 0", "%.2f %%" % (100 * JI_FRACTION["m_s -> 0"])),
        ("Ji m_s -> infinity", "%.2f %%" % (100 * JI_FRACTION["m_s -> infinity"])),
        ("valence p", "%.3f %%" % (100 * vp)),
        ("valence n", "%.3f %%" % (100 * vn)),
        ("coupling 2+1+1", "%.4f" % float(coupling_sum(Fraction(F_LIGHT["FLAG 2+1+1"])))),
        ("coupling 2+1", "%.4f" % float(coupling_sum(Fraction(F_LIGHT["FLAG 2+1"])))),
        ("largest READ", "%.4f of the payload" % HIGGS_SHARE_LARGEST_READ),
        ("largest all", "(%.4f)" % HIGGS_SHARE_LARGEST_ALL),
        ("READ margin illustration", "reach %.4f" % HIGGS_SHARE_READ_MARGIN),
        ("Ji estimate difference", "difference is %g MeV" % JI_ESTIMATE_DIFFERENCE_MEV),
        ("payload kg", "own default of %g kg" % PAYLOAD_KG),
        ("T_CMB", "T_CMB = %.4f" % T_CMB),
        ("Mc^2", _e(rest_energy_j(), 4) + " J"),
        ("megatons", "%.0f megatons" % warpfolder.megatons(rest_energy_j())),
        ("Landauer bits", _e(landauer_bits(), 4) + " bits"),
        ("per bit", _e(nopath.landauer_energy(1.0, T_CMB), 3) + " J per bit"),
        ("Bekenstein bits", _e(bekenstein_bits(), 4) + " bits"),
        ("ratio", "= %.0f" % bek_over_landauer_closed()),
        ("break-even", "%.3f mm" % (1000 * break_even_radius_m())),
        ("B", _e(c["B"], 4) + " baryons"), ("B count", "B = " + _e(c["B"], 4)),
        ("antibaryons", _e(c["B"], 4) + " units of"),
        ("N_e", _e(c["N_e"], 4)),
        ("N_n", "N_n = " + _e(c["N_n"], 4)),
        ("B/(M/m_p)", "%.4f" % (c["B"] / warpfolder.baryons_in(PAYLOAD_KG))),
        ("pair floor", "%.4f Mc^2" % (pair_floor_j() / rest_energy_j())),
        ("mu_min", "%.4f MeV" % MU_MIN[0]),
        ("mu_min nuclide", "(%d%s)" % (MU_MIN[2], MU_MIN[1])),
        ("G M/(R c^2)", _e(gravitational_binding_order(), 1)),
        ("1/alpha_W", "1/%.2f" % (1.0 / aw)),
        ("suppression", "10^%.2f" % log10_suppression()),
        ("transitions", _e(transitions_needed(), 4) + " transitions"),
        ("attempts x prefactor", "10^%.2f" % log10_attempts_times_prefactor()),
        ("RS96 arithmetic", "10^%.2f" % log10_suppression(1.0 / RS96_ALPHA_INV)),
        ("RS96 gap", "%.2f decades" % (log10_suppression(1.0 / RS96_ALPHA_INV)
                                       - RS96_PRINTED_LOG10)),
        ("TW 1/30", "10^%.2f" % log10_suppression(1.0 / 30.0)),
        ("TW 1/29.7", "10^%.2f" % log10_suppression(1.0 / 29.7)),
        ("TW gap", "%.2f decades off" % abs(log10_suppression(1.0 / TW_ALPHA_INV[1])
                                             - TW_PRINTED_LOG10)),
        ("TW product", "%.2f TeV x %.2f is %.2f" % (TW_PREFACTOR_TEV, sum(TW_B_TERMS),
                                                    TW_PREFACTOR_TEV * sum(TW_B_TERMS))),
        ("2 m_W/alpha_W", "%.3f TeV" % esph_formula_tev(1.0)),
        ("barrier ratio", "%.0f times" % esph_over_three_baryons(E_SPH_TEV[E_SPH_USED])),
        ("T_c kelvin", _e(t_kelvin(T_C_GEV), 3) + " K"),
        ("18 alpha^5", _e(symmetric_rate_crosscheck(), 2)),
        ("barrier heights", "%.0f Mc^2" % barrier_heights_over_mc2()),
        ("ln rate at T*", "%.2f" % broken_phase_ln_rate(T_FREEZE_GEV)),
        ("rate at T*", _e(math.exp(broken_phase_ln_rate(T_FREEZE_GEV)), 2) + " T^4"),
        ("ln rate at 155", "%.2f" % broken_phase_ln_rate(155.0)),
        ("y_t", "%.4f" % yukawas()["t"]), ("y_e", _e(yukawas()["e"], 3)),
        ("lambda_h", _e(excite.LAMBDA_H_READ_M, 3) + " m"),
        ("quantum lifetime", excite.one_sig(excite.QUANTUM_LIFETIME_S) + " s"),
        ("binding", "%.4f kg" % payload_masses()["binding (closure)"]),
        ("binding sensitivity", "%.4f kg" % binding_sensitivity_kg()),
        ("listed", "%.5f" % COUNTS["listed"]),
        ("stock elements", "%d listed" % len(COMPOSITION)),
        ("m_e", "%.9f MeV" % MASS_MEV["e"]),
        # round 6: TEMPLATE's priced remainder and the matter's own lowering
        ("held-seat eps", "eps = %s" % HELD_SEAT_ROUTE["eps"]),
        ("held-seat density", _e(HELD_SEAT_ROUTE["Higgs-derived kg/m^3"], 3) + " kg/m^3"),
        ("held-seat ratio", "%.1f J" % HELD_SEAT_ROUTE["source per J of field"]),
        ("held-seat ratio times", "%.1f times" % HELD_SEAT_ROUTE["source per J of field"]),
        ("held-seat electrons", _e(HELD_SEAT_ROUTE["electrons regained"], 3)),
        ("held-seat first order", _e(HELD_SEAT_ROUTE["nucleons first order"], 3)),
        ("stable range", "%.4f v < |phi| < v" % (1 - excite.stability_edge())),
        ("regained shares", regained_shares_text()),
        ("stability edge", "eps = %.4f" % excite.stability_edge()),
        ("self lowering", "eps of %s per %s kg/m^3" % (
            _e(excite.EPS_AT_FIXTURE, 0), _e(excite.HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18, 3))),
    ]


def row_figures():
    """[(row id, the string the row prints)], regenerated now."""
    return [("S10", "%.3f of atomic mass" % HIGGS_SHARE_LARGEST_READ),
            ("S10", "%.3f on all rows" % HIGGS_SHARE_LARGEST_ALL),
            ("S10", "reaches %.3f on the READ rows" % HIGGS_SHARE_READ_MARGIN),
            ("S11", "E_sph ~ %.0f TeV" % E_SPH_TEV[E_SPH_USED]),
            ("S11", "~%s x the 3 baryons" % _e(esph_over_three_baryons(E_SPH_TEV[E_SPH_USED]), 1)),
            ("S13", "%.1f J of source rest energy" % HELD_SEAT_ROUTE["source per J of field"]),
            ("S13", "%s kg/m^3" % _e(HELD_SEAT_ROUTE["Higgs-derived kg/m^3"], 3)),
            ("S13", "below eps = %.4f" % excite.stability_edge())]


#: Numerals the docstring prints that are neither regenerated, pinned, quoted
#: nor cited, and only those: the python version, DOCKET 63, two years (Fixsen
#: 2009, 't Hooft 1976), the study label ETM 19, and the 16 of the formula
#: exp(-16 pi^2/g^2).  Every entry is a literal, never a result
#: (literals_that_are_results), and every entry is needed (unneeded_literals).
DOC_LITERALS = frozenset({"3.11", "63", "2009", "1976", "19", "16"})


def _figure_numerals(s):
    """The numerals a regenerated figure string carries, with the '10^' of a
    power written out of it (so 10^-160.95 carries 160.95, not 10)."""
    return _numerals(re.sub(r"10\^", "", s))


def unneeded_literals(literals=None, doc=None):
    """[] iff every DOC_LITERALS entry is printed in the docstring (once the
    regenerated figures are struck) and is not already allowed otherwise: an
    allowance the docstring does not need is a hole the guard does not need."""
    literals = DOC_LITERALS if literals is None else literals
    doc = _norm(__doc__ if doc is None else doc)
    struck = doc
    for _lab, s in sorted(doc_figures(), key=lambda f: -len(f[1])):
        struck = struck.replace(s, " ")
    present = _numerals(struck)
    other = _allowed_numerals(struck)
    return sorted(l for l in literals
                  if l not in present or l in other or (l.isdigit() and int(l) < 10))


def literals_that_are_results(literals=None, figures=None):
    """[] iff no DOC_LITERALS entry is a numeral of any regenerated figure (a
    doc figure or a proposed-row figure): a literal may never stand in for a
    computed result."""
    literals = DOC_LITERALS if literals is None else literals
    figures = (doc_figures() + row_figures()) if figures is None else figures
    out = set()
    for _lab, fs in figures:
        out |= literals & _figure_numerals(fs)
    return sorted(out)


_NUM = re.compile(r"(?<![A-Za-z_\d.^])\d+(?:\.\d+)?(?:e-?\d+)?(?![A-Za-z_\d])")


def _numerals(text):
    return set(_NUM.findall(text))


def _allowed_numerals(struck_doc):
    """NARROWED.  The numerals a docstring may print without regenerating them:
    each PIN's numeral (checked against its source and the value used); the
    numerals inside the docstring's own double-quoted spans (each span is
    checked verbatim against a held text by check_quotes); and the numerals of
    the SOURCES LOCATORS (page, equation and arXiv citations), never of the
    held texts themselves."""
    out = set()
    for _k, numeral, _v in PINS:
        out |= _numerals(numeral)
    for q in _DQ.findall(struck_doc):
        out |= _numerals(q)
    for _st, loc, _t in SOURCES.values():
        out |= _numerals(loc) | set(re.findall(r"\d+\.\d+", loc))
    return out


def doc_figure_guard(doc=None, figures=None):
    """TWO-SIDED.  Every occurrence of every regenerated figure is struck from
    the docstring (so a duplicate goes stale only by leaving a numeral behind);
    then every numeral left must be a PIN's, one inside a checked quotation, a
    locator's, a small integer, or a DOC_LITERALS entry (_allowed_numerals).
    Returns the offending numerals (empty = clean), and the regenerated
    figures the docstring does not print at all."""
    doc = _norm(__doc__ if doc is None else doc)
    figures = doc_figures() if figures is None else figures
    missing = [(lab, s) for lab, s in figures if s not in doc]
    struck = doc
    for _lab, s in sorted(figures, key=lambda f: -len(f[1])):
        struck = struck.replace(s, " ")
    allowed = _allowed_numerals(struck) | DOC_LITERALS
    stray = sorted(n for n in _numerals(struck)
                   if n not in allowed and not (n.isdigit() and int(n) < 10))
    return stray, missing


def _doc_section(n):
    m = re.search(r"\n%d\.  [^\n]*\n=+\n(.*?)\n=+\n" % n, __doc__ or "", re.S)
    return m.group(1) if m else ""


def doc_refusal_numbers():
    return [int(k) for k in re.findall(r"(?m)^ {2,3}(\d+)\. ", _doc_section(7))]


_DQ = re.compile(r'"([^"]+)"')


def _quote_homes():
    homes = [_norm(t) for _s, _l, t in SOURCES.values()]
    homes += [_norm(M_MECHANISM), _norm(M_CONSIDERATION)]
    homes += [_norm(t) for t in OWNER_TEXTS.values()]
    return homes


def stray_quotations(texts):
    """Every double-quoted span in `texts` must sit verbatim in a source's held
    text, in M's words, or in a peer's owner text.  Returns the ones that do
    not (empty = clean)."""
    homes = _quote_homes()
    bad = []
    for t in texts:
        for q in _DQ.findall(_norm(t)):
            q = _norm(q).strip().rstrip(".")
            if not any(q in h for h in homes):
                bad.append(q)
    return bad


def parse_numeral(numeral):
    """The value a source's numeral denotes, as this file uses it.  '1/x' is
    the denominator x; '10^-n' is its exponent -n; 'a ... x 10^-n' is a x
    10^-n; otherwise the first number."""
    s = numeral.strip()
    if s.startswith("1/"):
        return float(re.search(r"\d+(?:\.\d+)?", s[2:]).group(0))
    if s.startswith("10^"):
        return float(re.match(r"10\^([+-]?\d+)", s).group(1))
    m = re.search(r"\d+(?:\.\d+)?", s)
    if m is None:
        return None
    x = re.search(r"x 10\^([+-]?\d+)", s)
    return float("%se%s" % (m.group(0), x.group(1))) if x else float(m.group(0))


def check_quotes(sources=None, quoted=None, pins=None, doc=None, rows=None,
                 survives=None):
    """The misquote check.  Returns a list of failures (empty = clean):
    every QUOTED fragment is in its source's held text AND in the docstring;
    every PIN's numeral is in its source's text and parses to the value used;
    every double-quoted span in the docstring, PROPOSED_ROWS and SURVIVES sits
    in a source, M's words or an owner text; and S10 carries M verbatim."""
    sources = SOURCES if sources is None else sources
    quoted = QUOTED if quoted is None else quoted
    pins = PINS if pins is None else pins
    doc = _norm(__doc__ if doc is None else doc)
    rows = PROPOSED_ROWS if rows is None else rows
    survives = SURVIVES if survives is None else survives
    bad = []
    for key, frag in quoted:
        if _norm(frag) not in _norm(sources[key][2]):
            bad.append(("not in source", key, frag))
        if _norm(frag) not in doc:
            bad.append(("not in docstring", key, frag))
    for key, numeral, value in pins:
        if numeral not in sources[key][2]:
            bad.append(("numeral not in source", key, numeral))
        if parse_numeral(numeral) != value:
            bad.append(("numeral does not parse to the value", key, numeral))
    row_texts = [" ".join(str(x) for x in r) for r in rows]
    surv_texts = [" ".join(s) for s in survives]
    for q in stray_quotations([doc] + row_texts + surv_texts):
        bad.append(("quotation with no home", "", q))
    s10 = [t for r, t in zip(rows, row_texts) if r[0] == "S10"]
    if not s10 or _norm(M_MECHANISM) not in _norm(s10[0]):
        bad.append(("S10 does not quote M verbatim", "S10", ""))
    return bad


# ================================================================== refusals
def scan_text():
    """The text every derived refusal flag scans: the docstring, the report as
    printed, the proposed rows and what survives."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    return "\n".join([__doc__, buf.getvalue()]
                     + [" ".join(str(x) for x in r) for r in PROPOSED_ROWS]
                     + [" ".join(s) for s in SURVIVES])


_BITS = re.compile(r"(\d+(?:\.\d+)?(?:e[+-]?\d+)?)\s+(?:erased\s+)?bits")

# ---- the collider balance, scanned (refusal 2)
_CONJ_WORD = re.compile(r"(?i)conjectur|unproven|not proven|no rigorous proof")
_CONJ_CLAIM = re.compile(r"(?i)\brest(?:s|ing)?\s+on\s+(?:[^.;:]{0,40}?)"
                         r"(?:conjectur|unproven)")
_FFS_NAMES = re.compile(r"Funakubo|Fuyuto|Senaha|FFS|1612\.05431")
#: The dissent's own admission (TW-2017 p.2), held: the caveat on the other side.
DISSENT_CAVEAT = "both estimates involve assumptions"


def _clauses(unit):
    """A unit's clauses, split at . ; : -- with 'et al.' and 'e.g.' protected."""
    u = re.sub(r"\bet al\.", "et al", _norm(unit))
    u = re.sub(r"\be\.g\.", "eg", u)
    return [c for c in re.split(r"(?<=[.;:])\s+", u) if c.strip()]


def one_sided_conjecture_claims(text):
    """[(why, clause)] for every clause that (a) attributes a conjecture or an
    unproven step to Funakubo et al. -- no held FFS text states one; they argue
    in the leading order of the WKB approximation -- or (b) says the prevalent
    results rest on conjectures without the dissent's own admission (TW-2017
    p.2) in the same passage.  A passage is a blank-line-separated unit of the
    scanned text (a docstring paragraph block, a report block, a proposed row).
    Empty = the balance is kept on both sides."""
    bad = []
    for unit in re.split(r"\n\s*\n", text):
        has_caveat = DISSENT_CAVEAT in _norm(unit)
        for cl in _clauses(unit):
            if _CONJ_WORD.search(cl) and _FFS_NAMES.search(cl):
                bad.append(("conjecture attributed to Funakubo et al.", cl))
            elif _CONJ_CLAIM.search(cl) and not has_caveat:
                bad.append(("one-sided: no dissent caveat in the passage", cl))
    return bad


# ---- a refusal of the mechanism printed without its priced remainder (refusal 9)
_EVERY = re.compile(r"(?i)refused on (?:every|all|each) readings?")


def unqualified_refusals(text):
    """[sentence] for every 'REFUSED on every reading' whose own sentence does
    not go on to say that DISPLACEMENT and QUANTA are refused as NET formation
    only, and -- while TEMPLATE's remainder is priced -- that TEMPLATE keeps
    the held-seat release route.  M's rule: never refuse a reading whose
    remainder is priced."""
    t = _norm(text)
    need = [r"(?i)net formation"]
    if REMAINDER_RESTORES_MASS.get("TEMPLATE"):
        need.append(r"(?i)held-seat release route")
    bad = []
    for m in _EVERY.finditer(t):
        rest = re.split(r"(?<=[.])\s", t[m.end():], maxsplit=1)[0]
        if not all(re.search(n, rest) for n in need):
            bad.append(t[max(0, m.start() - 60):m.end() + len(rest)])
    return bad


# ---- the Higgs share printed flat, without H-LINEAR (section 2)
def flat_share_claims(doc=None, rep=None):
    """[phrase] for every sentence that states the Higgs part of the nucleon as
    a finite fact rather than a first-order response: 'THIS is the part of the
    nucleon mass that comes from'; 'Nothing near one half' not followed by 'AT
    FIRST ORDER'; 'the remainder (or rest) is QCD' in a sentence of the
    docstring or the report that does not say 'first order'; and a report line
    printing 'remainder 1 - f_l' without 'first order'."""
    d = _norm(__doc__ if doc is None else doc)
    rep = _report_text() if rep is None else rep
    bad = [m.group(0) for m in re.finditer(r"THIS is the part of the nucleon mass", d)]
    for m in re.finditer(r"(?i)nothing near one half", d):
        if not d[m.end():m.end() + 20].strip().startswith("AT FIRST ORDER"):
            bad.append(d[m.start():m.end() + 20])
    for sent in _sentences(d) + [s for ln in rep.splitlines() for s in _sentences(ln)]:
        if (re.search(r"(?i)\b(?:remainder|rest) is QCD", sent)
                and not re.search(r"(?i)first order", sent)):
            bad.append(sent)
    bad += [ln.strip() for ln in rep.splitlines()
            if "remainder 1 - f_l" in ln and "first order" not in ln.lower()]
    return bad


# ---- round 5 (lens 2 on 7e94280): every text fixed is guarded, both ways
def _report_text():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    return buf.getvalue()


_SENT_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z(\"'|])")


def _sentences(block):
    """The sentences of one block of text, whitespace normalised."""
    return [x for x in _SENT_END.split(_norm(block).strip()) if x]


def _fn_docs():
    """The C1 and C5 function docstrings, as the guards read them (round 6)."""
    return {"fn C1": field_switched_on_by_arrival.__doc__ or "",
            "fn C5": trigger_gives_the_elements_their_mass.__doc__ or ""}


def guard_units(doc=None, rep=None, rows=None, survives=None, reasons=None,
                remainders=None, readings=None, fns=None):
    """Every sentence the round-5 and round-6 guards scan: the docstring
    paragraph by paragraph, the report line by line, every proposed row field,
    what survives, the READING_* tables, COUNTS_ON_THE_MECHANISM and NOT_OPENED
    as stored (not only as printed), and the C1 and C5 function docstrings."""
    doc = __doc__ if doc is None else doc
    rep = _report_text() if rep is None else rep
    rows = PROPOSED_ROWS if rows is None else rows
    survives = SURVIVES if survives is None else survives
    reasons = READING_REASONS if reasons is None else reasons
    remainders = READING_REMAINDERS if remainders is None else remainders
    readings = READINGS if readings is None else readings
    fns = _fn_docs() if fns is None else fns
    blocks = re.split(r"\n\s*\n", doc) + rep.splitlines()
    blocks += [str(x) for r in rows for x in r if isinstance(x, str)]
    blocks += [t for s in survives for t in s]
    blocks += [why for _yes, why in reasons.values()] + list(remainders.values())
    blocks += [w for _n, w, _c in readings]
    blocks += [str(x) for c in COUNTS_ON_THE_MECHANISM for x in c if isinstance(x, str)]
    blocks += list(NOT_OPENED)
    blocks += list(fns.values())
    return [s for b in blocks for s in _sentences(b)]


#: WORDING RETIRED, and why.  (id, regex over one sentence, a regex the same
#: sentence must also match to pass -- or None -- and the OLD wording, which
#: the selftest plants to prove the scan turns red on it).
STALE_WORDING = (
    ("SF1 C1 is not SWITCH-ON's alone (TEMPLATE)", r"SWITCH-ON(?: reading)? only", None,
     "C1 answers SWITCH-ON only: it needs P-UNIFORM to carry the field's value."),
    ("SF1 the finite-share readings are three (TEMPLATE)",
     r"STOCK or SWITCH-ON|SWITCH-ON or STOCK|STOCK and SWITCH-ON|SWITCH-ON and STOCK",
     None, "C2 is therefore NOT listed on STOCK or SWITCH-ON."),
    ("SF1 the one-count paragraph names TEMPLATE",
     r"C1 is the only count on SWITCH-ON,|with C1 reversed SWITCH-ON stands"
     r"|SWITCH-ON's one count", None,
     "C1 is the only count on SWITCH-ON, C3 the only count on QUANTA.  With C1 "
     "reversed SWITCH-ON stands.  SWITCH-ON's one count rests on the premise."),
    ("SF1 C5 on STOCK carries H-PRESENT", r"C5 answers STOCK only", r"H-PRESENT",
     "C5 answers STOCK only: there the elements are at the seat already, and "
     "their own measured masses fix phi where they are."),
    ("SF1 P-UNIFORM's dependants name TEMPLATE", r"C1 and the consideration", None,
     "C1 and the consideration's 'discriminates nothing' rest on it."),
    ("SF2/R6-A H-PRESENT failing is TEMPLATE's case or a seat above v, never a "
     "rescue of STOCK", r"H-PRESENT fail", r"(?s)(?=.*the case is TEMPLATE)(?=.*r > 1)",
     "For prior mass: H-PRESENT failing (elements present at the seat without "
     "their measured mass) would flip it."),
    ("R6-A H-PRESENT failing names the seat above v too",
     r"the case is TEMPLATE(?! \(r < 1\) or a seat above v \(r > 1)", None,
     "On H-PRESENT failing the case is TEMPLATE, which moves only if C1 reverses "
     "(P-UNIFORM, D15 or D16)."),
    ("SF2 C5 does not reverse on H-PRESENT", r"H-TREE or H-PRESENT", None,
     "The STOCK reading moves if C5 reverses (H-TREE or H-PRESENT failing)."),
    ("SF3 TEMPLATE lacks all or part of its Higgs-given mass",
     r"(?i)without their (?:measured |Higgs-given )?mass", None,
     "STOCK's complement: the elements' templates sit at the seat WITHOUT their mass."),
    ("SF3 TEMPLATE is not only the off state",
     r"(?i)(?:requires?|needs?) phi = 0|SWITCH-ON state|\(phi = 0 there before", None,
     "Templates without their mass REQUIRE phi = 0 at the seat, which is the "
     "SWITCH-ON state."),
    ("SF4 C2's small displacement carries its finite remainder",
     r"(?i)small displacement", r"(?i)finite|\(C2 for a small displacement only\)",
     "C2 answers DISPLACEMENT only: a small displacement of phi is exactly a "
     "first-order response."),
    ("SF4 C2 is scoped within DISPLACEMENT", r"C2 answers DISPLACEMENT only", None,
     "C2 answers DISPLACEMENT only, and the finite one is OPEN."),
    ("NOTE the remainder is QCD at first order only", r"(?i)\b(?:remainder|rest) is QCD",
     r"(?i)first order", "The remainder is QCD."),
    ("NOTE no P-UNIFORM holds on H-PRESENT", r"(?i)\bno[ -]P-UNIFORM", r"H-PRESENT",
     "The elements' own measured masses fix phi where they are; no P-UNIFORM."),
    ("NOTE the finite share's non-reliance lists TEMPLATE",
     r"(?i)verdict rests on it: STOCK", r"TEMPLATE",
     "No verdict rests on it: STOCK is refused on prior mass (C5), SWITCH-ON on C1."),
    ("SF3 C5's omitted reasons name STOCK's case (H-PRESENT), not a lack",
     r"(?i)\black (?:their|theirs)\b", None,
     "The reading claims mass forms from quanta, not that elements at the seat lack "
     "their mass."),
    ("NOTE H-PRESENT is a case definition, not READ",
     r"present with its measured mass \(READ\)", None,
     "An element present at the seat is present with its measured mass (READ), "
     "since that mass is part of what the measurement names."),
    # ---- round 6
    ("R6-A the seat split is three-way, never 'exhaustive' alone", r"(?i)exhaustive",
     r"(?i)three-way", "H-PRESENT or not, the split is exhaustive."),
    ("R6-A the seat does not split in two", r"(?i)splits? in two|two-way split", None,
     "STOCK SPLITS IN TWO."),
    ("R6-B C1's TEMPLATE refusal names H-UNSOURCED-SEAT", r"(?i)nothing places there",
     r"H-UNSOURCED-SEAT",
     "Any lower value needs a local source (D15, D16), which nothing places there."),
    ("R6-B TEMPLATE moves not only on C1's three premises",
     r"TEMPLATE,? (?:which )?moves only if C1 reverses", None,
     "On H-PRESENT failing the case is TEMPLATE, which moves only if C1 reverses "
     "(P-UNIFORM, D15 or D16)."),
    ("R6-C TEMPLATE keeps a priced remainder", r"(?i)TEMPLATE[^.]*\bno remainder", None,
     "TEMPLATE is refused on P-UNIFORM; no remainder."),
    ("R6-C TEMPLATE's remainder is not 'none'",
     r"(?i)none: on P-UNIFORM the (?:unsourced )?field is (?:at v|on) where the "
     r"templates", None,
     "none: on P-UNIFORM the unsourced field is at v where the templates would sit"),
    ("R6-D SWITCH-ON with the elements seated is TEMPLATE, not STOCK",
     r"(?i)already seated, it is (?:the )?STOCK", None,
     "C1 (read with the elements already seated, it is the STOCK reading)."),
    ("R6-E section 0 names the readings that keep a remainder",
     r"TWO READINGS KEEP A REMAINDER", None,
     "TWO READINGS KEEP A REMAINDER: EXCITATION (THE PAIR ROUTE, PRICED) AND STOCK."),
    ("R6-E the DISPLACEMENT headline scopes C2", r"REFUSED on C2, C3", None,
     "DISPLACEMENT REFUSED on C2, C3 -- as net formation; remainder the pair route."),
    ("R6-F C5's docstring: the link never holds on a lack",
     r"(?i)link holds (?:only )?if\b[^.]*\black\b", None,
     "The link holds only if the elements LACK that mass before arrival."),
    ("R6-F C1's docstring and link name below v", r"(?i)only if it was off (?:at|there)\b"
     r"|the field was off at the seat and arrival turns it on\b", None,
     "Arrival switches the field on only if it was off at the seat."),
    ("R6-F the off-only wordings name the lowered field too",
     r"(?i)about an off (?:state|field) at the seat|with the field switched off \(heavy"
     r"|at the off state C1|so no off state and no", None,
     "C1 is about an off state at the seat, which this reading does not assume."),
    # ---- round 7
    ("R7-2 the holding price is excite's exact ratio; 2/eps is its small-eps limit",
     r"(?i)2/eps", r"(?i)small[- ]eps|limit|-> ?2/eps|overstat|2/eps overstates",
     "Holding any eps costs 2/eps joules of source per joule of field "
     "(excite.holding_ratio)."),
    ("R11 no sentence ties stability to bare D20's model",
     r"(?i)D20's model[^.]*\bstab|\bstab[^.]*D20's model", r"section-3",
     "Within D20's model a static hold is stable only on 0.5774 v < |phi| < v."),
    ("R8 the report's holding-ratio label never gives 2/eps as the value",
     r"(?i)J of source per J of field \(2/eps\)", None,
     "  J of source per J of field (2/eps)    197.0050"),
    ("R7-3 a positive source is an equilibrium below v, a stable hold only in the "
     "stable range", r"(?i)source holds 0 < \|phi\| < v", None,
     "It is not vacuous: within D20's model a positive source holds 0 < |phi| < v."),
    ("R7-1 the nucleons' first-order figure is never a bound",
     r"(?i)(?:first-order|at first order|nucleon row|largest central reading)[^;]*"
     r"\ban? (?:upper |lower )?bound\b", r"(?i)\b(?:not|none|never) an? (?:upper )?bound",
     "The nucleons' part at first order (the largest READ nucleon row) gives "
     "1.716e-3 at eps = 1/100, an upper bound."),
    ("R7-1 the first-order share is an estimate of the nucleons' part, not its bound",
     r"(?i)bounded by the first-order share", None,
     "The nucleons' part is bounded by the first-order share only at small eps."),
    ("R7-5 the Higgs is an intermediary, never the source", r"(?i)\bHiggs(?: field)? is "
     r"(?:the|its) source", None, "The Higgs is the source here (C4)."),
    ("R7-5 H-UNSOURCED-SEAT does not reach SWITCH-ON", r"(?i)\breach(?:es)? SWITCH-ON",
     r"(?i)does not reach SWITCH-ON",
     "It also reaches SWITCH-ON: the off state lies past D20's stability edge."),
    ("R7-5 the release radiates the rest", r"(?i)\b(?:none|nothing) (?:of it )?is radiated",
     None, "The field pays for the regained rest energy; none is radiated."),
    ("R7-4 the floor counts the phi-coupled rest energy, the elements' included",
     r"(?i)J of source rest energy sat at the seat|the source, which held [\d.]+ times",
     None, "So per joule regained at least 197.0 J of source rest energy sat at the seat."),
    ("R7-5 TEMPLATE is refused on P-UNIFORM and H-UNSOURCED-SEAT, not the latter only",
     r"(?i)on H-UNSOURCED-SEAT only", None,
     "On TEMPLATE it is refused on H-UNSOURCED-SEAT only."),
    ("R7-5 the report's lowering is per kg/m^3 of Higgs-derived mass",
     r"eps per kg/m\^3\s+\S+\s+inside the measured mass", None,
     "      the matter's own lowering, eps per kg/m^3    4.5407e-30  inside the measured "
     "mass"),
    ("R7-1 S13's mover: the finite response sets the nucleons' regain, not the share",
     r"finite Higgs share \(S10 \(open\)\), which sets", None,
     "the finite Higgs share (S10 (open)), which sets what the nucleons regain at "
     "large eps"),
    ("R7-5 H-PRESENT: the matter's own lowering sits inside the measured mass",
     r"(?i)negligible beside the measured mass", None,
     "The matter's own D20 lowering is negligible beside the measured mass."),
)


def stale_wording(units=None, table=None):
    """[(id, sentence)] for every sentence carrying retired wording."""
    units = guard_units() if units is None else units
    table = STALE_WORDING if table is None else table
    return [(i, s) for i, pat, unless, _old in table for s in units
            if re.search(pat, s) and not (unless and re.search(unless, s))]


def selftest_labels(src=None):
    """Every literal chk() label in this file's source: the first argument, or
    the left side of its % format, read with ast (round 7)."""
    src = inspect.getsource(sys.modules[__name__]) if src is None else src
    out = []
    for node in ast.walk(ast.parse(src)):
        if (isinstance(node, ast.Call) and getattr(node.func, "id", "") == "chk"
                and node.args):
            a = node.args[0]
            a = a.left if isinstance(a, ast.BinOp) else a
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                out.append(a.value)
    return out


#: The STALE_WORDING entries the selftest labels are scanned against.
LABEL_SCAN = ("R6-A the seat split is three-way, never 'exhaustive' alone",)


def stale_labels(labels=None, ids=LABEL_SCAN):
    """[(id, label)] for every non-CONTROL selftest label carrying retired
    wording (a CONTROL label names the old wording it plants)."""
    labels = selftest_labels() if labels is None else labels
    return [(i, lab) for i, pat, unless, _old in STALE_WORDING if i in ids
            for lab in labels if not lab.startswith("CONTROL")
            and re.search(pat, lab) and not (unless and re.search(unless, lab))]


def _intro(doc=None):
    d = __doc__ if doc is None else doc
    return d.split("\n0.  THE ANSWER", 1)[0]


_REPORT_C1 = re.compile(r"(?m)^\s*C1 FIELD_SWITCHED_ON_BY_ARRIVAL\s+(?:True|False)\s+(.*)$")


def guard_locations(doc=None, rep=None, rows=None, reasons=None, readings=None,
                    fns=None, remainders=None, survives=None):
    """{locator: normalised text} for every place a REQUIRED_WORDING entry is
    checked."""
    doc = __doc__ if doc is None else doc
    rep = _report_text() if rep is None else rep
    rows = PROPOSED_ROWS if rows is None else rows
    reasons = READING_REASONS if reasons is None else reasons
    readings = READINGS if readings is None else readings
    fns = _fn_docs() if fns is None else fns
    remainders = READING_REMAINDERS if remainders is None else remainders
    survives = SURVIVES if survives is None else survives
    old_doc = globals()["__doc__"]
    try:
        globals()["__doc__"] = doc
        loc = {"intro": _intro(doc), "doc": doc}
        loc.update({"doc %d" % n: _doc_section(n) for n in range(10)})
    finally:
        globals()["__doc__"] = old_doc
    loc["report"] = rep
    m = _REPORT_C1.search(rep)
    loc["report C1"] = m.group(1) if m else ""
    for r in rows:
        loc["%s claim" % r[0]] = r[2]
        loc["%s moves" % r[0]] = r[5]
    for (name, cid), (_y, why) in reasons.items():
        loc["reason %s %s" % (name, cid)] = why
    for name, what, _c in readings:
        loc["reading %s" % name] = what
    for cid, _n, own, st, _c, what in COUNTS_ON_THE_MECHANISM:
        loc["count %s" % cid] = what
        loc["count %s status" % cid] = st
        loc["count %s owner" % cid] = own[1]
    for name, text in remainders.items():
        loc["remainder %s" % name] = text
    for name, text in survives:
        loc["survives %s" % name] = text
    loc.update(fns)
    return {k: _norm(v) for k, v in loc.items()}


_TEMPLATE_DEF = ("templates at the seat without all or part of their HIGGS-GIVEN "
                 "mass (|phi| < v there before arrival)")
_TEMPLATE_DEF_ROW = ("templates at the seat without all or part of their Higgs-given "
                     "mass (|phi| < v there before arrival)")
_PHI0_DEF = "templates at the seat without their Higgs-given mass (phi = 0 there before arrival)"
#: WORDING REQUIRED where each round-5 and round-6 fix landed.  (id, locator,
#: exact phrase (normalised), the OLD wording the control puts back in its place).
REQUIRED_WORDING = (
    # DOCKET 65's closing round: two row phrases, each with the wording it
    # replaced as its control.
    ("D65-close S10 claim: CREATION refused in D29's own words", "S10 claim",
     "CREATION by C4 (the field has no energy to give about v, and its one "
     "release, vacuum decay, forms no atomic mass at the seat, D29) and C3",
     "CREATION by C4 (the field has no energy to give, D29) and C3"),
    ("D65-close S11 claim: v is NAMED-NOT-READ, via G_F", "S11 claim",
     "alpha_W from READ m_W and v (NAMED-NOT-READ, via G_F); B/3 transitions",
     "alpha_W from READ m_W and v; B/3 transitions"),
    ("SF3 intro defines TEMPLATE", "intro", _TEMPLATE_DEF,
     "the elements' templates sit at the seat WITHOUT their mass"),
    ("R6-A intro: the split is three-way", "intro", THREE_WAY,
     "the split is exhaustive: before arrival the elements at the seat lack none"),
    ("SF3 section 0 (caps) defines TEMPLATE", "doc 0",
     "TEMPLATES AT THE SEAT WITHOUT ALL OR PART OF THEIR HIGGS-GIVEN MASS, |phi| < v "
     "THERE BEFORE ARRIVAL", "THE ELEMENTS' TEMPLATES AT THE SEAT WITHOUT THEIR MASS"),
    ("SF3 section 0 (M65-1) defines TEMPLATE", "doc 0",
     "templates at the seat without all or part of their HIGGS-GIVEN mass (|phi| < v "
     "there before arrival)", "the elements' templates at the seat WITHOUT their mass"),
    ("SF3 section 0 gives C1's reason on TEMPLATE", "doc 0", _C1_TEMPLATE,
     "needs phi = 0 there, which is the SWITCH-ON state"),
    ("R6-A section 0 (caps): three-way", "doc 0",
     "H-PRESENT OR NOT, THE SPLIT IS THREE-WAY: r = |phi|/v < 1 IS TEMPLATE (C1), "
     "r = 1 IS STOCK ON H-PRESENT (C5), AND r > 1 IS NEITHER READING'S CLAIM",
     "H-PRESENT OR NOT, THE SPLIT IS EXHAUSTIVE"),
    ("R6-A section 0 (M65-1): three-way", "doc 0", "H-PRESENT or not, " + THREE_WAY,
     "H-PRESENT or not, the split is exhaustive"),
    ("R6-B section 0 (caps): C1 on TEMPLATE rests on H-UNSOURCED-SEAT", "doc 0",
     "WHICH ON H-UNSOURCED-SEAT NOTHING HOLDS THERE BEFORE ARRIVAL",
     "WHICH NOTHING PLACES THERE (H-TREE)"),
    ("R6-C/R7 section 0 (caps): TEMPLATE refused on P-UNIFORM and H-UNSOURCED-SEAT",
     "doc 0", "ON TEMPLATE IT IS REFUSED ON P-UNIFORM AND H-UNSOURCED-SEAT, AND WHERE "
     "THE LATTER FAILS A SEAT PREPARED IN ADVANCE CAN STILL HAVE ITS ELEMENTS' "
     "HIGGS-GIVEN MASS RESTORED ON ARRIVAL (THE HELD-SEAT RELEASE ROUTE, PRICED; IT "
     "FORMS NO BARYONS)", "ON TEMPLATE IT IS REFUSED ON H-UNSOURCED-SEAT ONLY, AND A "
     "SEAT PREPARED IN ADVANCE"),
    ("R6-C section 0 (M65-1): TEMPLATE keeps a priced remainder", "doc 0",
     "Without H-UNSOURCED-SEAT, TEMPLATE keeps a priced remainder, the held-seat "
     "release route", "TEMPLATE has no remainder"),
    ("R6-C section 0 (M65-5): the held-seat route survives", "doc 0",
     "So does TEMPLATE's remainder where H-UNSOURCED-SEAT fails, the held-seat "
     "release route, PRICED", "Two routes survive"),
    ("SF1 section 0: C1 answers SWITCH-ON and TEMPLATE", "doc 0",
     "That answers SWITCH-ON, and TEMPLATE below.",
     "That answers the SWITCH-ON reading only."),
    ("SF1 section 0: C2 off SWITCH-ON, STOCK and TEMPLATE", "doc 0",
     "It does NOT answer SWITCH-ON, STOCK or TEMPLATE",
     "It does NOT answer SWITCH-ON or STOCK"),
    ("SF4 section 0 scopes C2", "doc 0", "C2 answers DISPLACEMENT, and there " + C2_SCOPE,
     "C2 answers DISPLACEMENT only"),
    ("R6-F section-1 header", "doc",
     "1. M65-1 PRESENCE -- SWITCH-ON, STOCK, TEMPLATE AND EXCITATION",
     "1. M65-1 PRESENCE -- THE SWITCH-ON AND EXCITATION READINGS"),
    ("SF3 section 1 has the TEMPLATE reading", "doc 1", "THE TEMPLATE READING (C1)",
     "The complement, TEMPLATE"),
    ("R6-F section 1 defines TEMPLATE", "doc 1", _TEMPLATE_DEF,
     "templates at the seat without their Higgs-given mass (phi = 0 there before "
     "arrival)"),
    ("SF3 section 1 gives C1's reason on TEMPLATE", "doc 1", _C1_TEMPLATE,
     "that needs phi = 0 at the seat before arrival"),
    ("R6-B/R7 section 1: H-UNSOURCED-SEAT is not vacuous, on the stable range",
     "doc 1", "H-UNSOURCED-SEAT is not vacuous: within D20's model a positive source "
     "is an equilibrium on 0 < |phi| < v ((a) below) and, within excite's section-3 "
     "model (source rest mass proportional to phi), a stable hold only on "
     + STABLE_RANGE + ".  Where it fails, TEMPLATE keeps a priced remainder, the "
     "held-seat release route (section 5 (d)), on that range only",
     "H-UNSOURCED-SEAT is not vacuous: within D20's model a positive source holds "
     "0 < |phi| < v ((a) below).  Where it fails, TEMPLATE keeps a priced remainder, "
     "the held-seat release route (section 5 (d))"),
    ("R7-2 section 1 (a): the exact holding ratio, 2/eps its limit", "doc 1",
     "Holding eps costs 4(1-eps)^2/(eps(2-eps)) joules of source per joule of field "
     "(excite.holding_ratio), 2/eps at small eps",
     "Holding any eps costs 2/eps joules of source per joule of field "
     "(excite.holding_ratio)"),
    ("R6-A section 1: three-way", "doc 1", "H-PRESENT or not, " + THREE_WAY,
     "The split is exhaustive, H-PRESENT or not"),
    ("NOTE section 1: no P-UNIFORM on H-PRESENT", "doc 1",
     "On H-PRESENT this needs NO P-UNIFORM", "This needs NO P-UNIFORM"),
    ("SF4 section 2 closing scopes C2", "doc 2", C2_SCOPE,
     "where a small displacement of phi is exactly a first-order response"),
    ("NOTE section 2: no verdict rests on it lists TEMPLATE", "doc 2",
     "SWITCH-ON and TEMPLATE on C1", "SWITCH-ON on C1"),
    ("R6-B section 5: C1's list line names H-UNSOURCED-SEAT", "doc 5",
     "(M65-1; D15, D16, P-UNIFORM; on TEMPLATE, H-UNSOURCED-SEAT)",
     "(M65-1; D15, D16, P-UNIFORM)"),
    ("R6-F section 5: C5's list line, no P-UNIFORM on H-PRESENT", "doc 5",
     "no P-UNIFORM on H-PRESENT)", "no P-UNIFORM)"),
    ("SF1 section 5 prose: C1 answers SWITCH-ON and TEMPLATE", "doc 5",
     "C1 answers SWITCH-ON and TEMPLATE: each needs the field off, or below v",
     "C1 answers SWITCH-ON only: it needs P-UNIFORM"),
    ("R6-B section 5 prose: C1 on TEMPLATE rests on H-UNSOURCED-SEAT", "doc 5",
     "which on H-UNSOURCED-SEAT nothing holds there", "which nothing places there"),
    ("SF4 section 5 prose scopes C2", "doc 5", "C2 answers DISPLACEMENT, and there "
     + C2_SCOPE, "C2 answers DISPLACEMENT only"),
    ("SF1 section 5 prose: C2 off SWITCH-ON, STOCK and TEMPLATE", "doc 5",
     "C2 does NOT answer SWITCH-ON, STOCK or TEMPLATE",
     "C2 does NOT answer SWITCH-ON or STOCK"),
    ("SF1 section 5 prose: C5 carries H-PRESENT", "doc 5",
     "C5 answers STOCK only: there the elements are at the seat already, present as "
     "elements with their measured mass (H-PRESENT)",
     "C5 answers STOCK only: there the elements are at the seat already"),
    ("SF1 section 5: C1 the only count on SWITCH-ON and TEMPLATE", "doc 5",
     "C1 is the only count on SWITCH-ON and on TEMPLATE",
     "C1 is the only count on SWITCH-ON,"),
    ("SF1 section 5: with C1 reversed both stand", "doc 5",
     "with C1 reversed SWITCH-ON and TEMPLATE stand", "with C1 reversed SWITCH-ON stands"),
    ("SF1 section 5: TEMPLATE still refused when C5 reverses", "doc 5",
     "with C5 reversed STOCK stands, and TEMPLATE is still refused on C1",
     "with C5 reversed STOCK stands."),
    ("SF1 section 5: the one count of SWITCH-ON and TEMPLATE", "doc 5",
     "The one count of SWITCH-ON and of TEMPLATE rests on the premise P-UNIFORM",
     "SWITCH-ON's one count rests on the premise P-UNIFORM"),
    ("R6-B section 5: TEMPLATE's one count also on H-UNSOURCED-SEAT", "doc 5",
     "TEMPLATE's also on H-UNSOURCED-SEAT", "TEMPLATE's also"),
    ("SF4 section 5 table scopes C2", "doc 5", "C2 answers a SMALL displacement only; "
     "a finite one is OPEN, and C3 carries the refusal regardless",
     "C2 answers a SMALL displacement only (H-LINEAR), a finite one being OPEN"),
    ("R6-C/R7 section 5 verdict line names the held-seat route", "doc 5",
     "on TEMPLATE on P-UNIFORM and H-UNSOURCED-SEAT -- where the latter fails, a "
     "seat prepared in advance can still have its elements' Higgs-given mass "
     "restored on arrival (the held-seat release route, PRICED; it forms no "
     "baryons)", "on TEMPLATE on H-UNSOURCED-SEAT only -- a seat prepared in advance"),
    ("R6-C section 5 (d): the held-seat release route", "doc 5",
     "(d) THE HELD-SEAT RELEASE ROUTE, TEMPLATE's remainder where H-UNSOURCED-SEAT "
     "fails, and the reading closest to M's mechanism", "(d)"),
    ("R6-C section 5 (d)(i): no baryons", "doc 5",
     "(i) It forms no baryons: the elements were already there, and no Higgs coupling "
     "carries B (C3)", "(i)"),
    ("R6-C section 5 (d)(ii): the field's own energy pays, and cannot be exceeded",
     "doc 5", "by energy conservation that is what pays for the elements' regained "
     "rest energy, which cannot exceed it", "the field pays"),
    ("R6-C section 5 (d)(ii): per joule regained, at least", "doc 5",
     "so per joule regained at least", "so per joule regained"),
    ("R7-4 section 5 (d)(ii): the phi-coupled rest energy, the elements' included",
     "doc 5", "the phi-coupled rest energy at the seat (the prepared source's with "
     "the elements') was", "stored in advance by the source, which held"),
    ("R7-5 section 5 (d)(ii): the rest is radiated", "doc 5",
     "which cannot exceed it; the rest is radiated", "which cannot exceed it; none is "
     "radiated"),
    ("R7-2 section 5 (d): 2/eps is the small-eps limit", "doc 5",
     "(excite.holding_ratio; 2/eps at small eps)", "(excite.holding_ratio; eps/2 at "
     "small eps)"),
    ("R7-1 section 5 (d)(iii): eps times the first-order share, at small eps", "doc 5",
     "the nucleons' part is eps times the first-order share at small eps (the largest "
     "READ nucleon row gives", "the nucleons' part is bounded by the first-order "
     "share only at small eps (the largest central reading on the READ rows gives"),
    ("R7-1 section 5 (d)(iii): not a bound", "doc 5", "; an estimate, not a bound)",
     ", an upper bound)"),
    ("R7-1 section 5 (d)(iii): the finite response OPEN up to the edge", "doc 5",
     "and, up to the stability edge, a finite response that is OPEN like the finite "
     "share", "and at large eps by the finite share, which is OPEN"),
    ("R7-3 section 5 (d)(iii): stable range; none below it", "doc 5",
     "(excite.stability_edge), on " + STABLE_RANGE + "; a TEMPLATE seat below that "
     "keeps no held-seat remainder", "(excite.stability_edge)."),
    ("R7-5 section 5 (d): intermediary, not the source (C4)", "doc 5",
     "The Higgs is an intermediary here too, holding what the source stored, not the "
     "source (C4)", "The Higgs is the source here (C4)"),
    ("R6-C section 5 (d)(iv): a prior arrival (D23)", "doc 5",
     "It needs the seat prepared in advance: something reached the destination "
     "first, at <= c, which is D23's point for reconstruction", "(iv)"),
    ("SF1 section 6 H-LINEAR: C2 off three readings", "doc 6",
     "C2 is therefore NOT listed on SWITCH-ON, STOCK or TEMPLATE",
     "C2 is therefore NOT listed on STOCK or SWITCH-ON"),
    ("SF4 section 6 H-LINEAR scopes C2", "doc 6", C2_SCOPE,
     "where a small displacement of phi is a first-order response"),
    ("NOTE section 6 H-PRESENT is a case definition", "doc 6",
     "H-PRESENT A CASE DEFINITION, not a finding", "H-PRESENT An element present"),
    ("NOTE section 6 H-PRESENT tags only the masses READ", "doc 6",
     "present with its measured mass (the masses READ)",
     "present with its measured mass (READ)"),
    ("R6-A NOTE section 6 H-PRESENT: measured mass names phi as measured", "doc 6",
     "Measured mass means phi as it is where the masses were measured; the matter's "
     "own D20 lowering", "|phi| = v there before arrival."),
    ("R6-F section 6 defines TEMPLATE", "doc 6",
     "templates at the seat without all or part of their HIGGS-GIVEN mass, |phi| < v "
     "there before arrival", "templates at the seat without their mass, phi = 0 there "
     "before arrival"),
    ("R6-B section 6 H-PRESENT: TEMPLATE refused on H-UNSOURCED-SEAT", "doc 6",
     "refused by C1 on P-UNIFORM and H-UNSOURCED-SEAT", "refused by C1 on P-UNIFORM"),
    ("R6-A section 6 H-PRESENT: three-way", "doc 6", "H-PRESENT or not, " + THREE_WAY,
     "H-PRESENT or not, the split is exhaustive"),
    ("R6-B section 6 names H-UNSOURCED-SEAT", "doc 6",
     "H-UNSOURCED-SEAT Nothing at the seat holds |phi| below v before arrival", ""),
    ("R6-B/R7 section 6: H-UNSOURCED-SEAT is not vacuous, on the stable range", "doc 6",
     "It is not vacuous: within D20's model a positive source is an equilibrium on "
     "0 < |phi| < v (section 1 (a)) and, within excite's section-3 model (source rest "
     "mass proportional to phi), a stable hold only on " + STABLE_RANGE,
     "It is not vacuous: within D20's model a positive source holds 0 < |phi| < v"),
    ("R7-2 section 6: the exact holding ratio, 2/eps its limit", "doc 6",
     "at 4(1-eps)^2/(eps(2-eps)) J of source per J of field (excite.holding_ratio; "
     "2/eps at small eps)", "at 2/eps J of source per J of field (excite.holding_ratio)"),
    ("R7-3 section 6: the remainder on the stable range only", "doc 6",
     "the held-seat release route (section 5 (d)), on that range only",
     "the held-seat release route (section 5 (d))"),
    ("R7-5 section 6: H-UNSOURCED-SEAT does not reach SWITCH-ON", "doc 6",
     "section-3 model (source rest mass proportional to phi) it does not reach "
     "SWITCH-ON: the off state lies past D20's stability edge", "It does not reach "
     "SWITCH-ON: the off state lies past D20's stability edge"),
    ("R9 section 6: the off state could be held by a convex-mass source", "doc 6",
     "A source whose mass rises convexly with |phi| (D20'S MODEL; not computed) could "
     "hold it, and with the elements seated that is TEMPLATE at |phi| = 0",
     "No source whose mass comes from phi can hold it"),
    ("R7-5 section 6 H-PRESENT: the lowering sits inside the measured mass", "doc 6",
     "sits inside the measured mass, so |phi| = v here names that phi",
     "is negligible beside the measured mass, so |phi| = v here names that phi"),
    ("R6-C section 6 names H-RELEASE", "doc 6",
     "H-RELEASE On the held-seat release route the trigger removes the prepared "
     "source without doing work on the field or the elements", ""),
    ("SF1 section 6 P-UNIFORM names TEMPLATE", "doc 6",
     "C1 (on SWITCH-ON and TEMPLATE) and the consideration's",
     "C1 and the consideration's"),
    ("R6-C section 7 refusal 9 names the held-seat route", "doc 7",
     "The pair route, the anomaly route and the held-seat release route are all priced",
     "The pair route and the anomaly route are both priced"),
    ("R6-F section 8 CASE DEFINITION: H-PRESENT", "doc 8", "CASE DEFINITION: H-PRESENT",
     "NAMED: H-PRESENT"),
    ("R6-B section 8 names H-UNSOURCED-SEAT", "doc 8",
     "NAMED HYPOTHESIS OF C1 ON TEMPLATE: H-UNSOURCED-SEAT", ""),
    ("R6-A/B S10 mover: STOCK on H-TREE; H-PRESENT failing; TEMPLATE's movers",
     "S10 moves", "STOCK moves only if H-TREE fails; " + H_PRESENT_FAILING + "; "
     + TEMPLATE_MOVES, "STOCK moves only if H-TREE fails; on H-PRESENT failing the "
     "case is TEMPLATE, which moves only if C1 reverses (P-UNIFORM, D15 or D16)"),
    ("SF4 S10 mover: DISPLACEMENT needs C3, C2 for a small one", "S10 moves",
     "DISPLACEMENT needs C3, and C2 as well for a small displacement (a finite one "
     "reaches the finite share, OPEN; within D20's model a positive source only "
     "lowers |phi|)", "DISPLACEMENT needs C2 and C3"),
    ("SF3 S10 claim defines TEMPLATE", "S10 claim",
     "templates at the seat without all or part of their Higgs-given mass, |phi| < v "
     "there before arrival", "templates without their mass"),
    ("SF3 S10 claim gives C1's reason on TEMPLATE", "S10 claim", _C1_TEMPLATE,
     "by C1 on P-UNIFORM"),
    ("R6-A S10 claim: three-way", "S10 claim", "H-PRESENT or not, " + THREE_WAY,
     "H-PRESENT or not, the STOCK/TEMPLATE split is exhaustive"),
    ("R6-C/R7 S10 claim names the held-seat route", "S10 claim",
     "TEMPLATE is refused on P-UNIFORM and H-UNSOURCED-SEAT; where the latter fails, "
     "what remains is the held-seat release route (S13), priced, which forms no "
     "baryons", "TEMPLATE is refused on H-UNSOURCED-SEAT only: what remains is the "
     "held-seat release route (S13), priced, which forms no baryons"),
    ("SF4 S10 claim scopes C2", "S10 claim", C2_SCOPE, "by C2 and C3"),
    ("NOTE S10 claim: no verdict rests on it lists TEMPLATE", "S10 claim",
     "SWITCH-ON and TEMPLATE on C1, and DISPLACEMENT on C3 regardless",
     "(S10 (open))"),
    ("R6-F D27 claim defines TEMPLATE", "D27 claim", _TEMPLATE_DEF_ROW, _PHI0_DEF),
    ("R6-F D27 claim gives C1's reason on TEMPLATE", "D27 claim", _C1_TEMPLATE,
     "C1 refuses"),
    ("R6-A D27 claim: three-way", "D27 claim", "H-PRESENT or not, " + THREE_WAY,
     "H-PRESENT or not, the split is exhaustive"),
    ("R6-A D27 mover: H-PRESENT failing names r > 1", "D27 moves",
     "the case is TEMPLATE (r < 1) or a seat above v (r > 1: nothing to give; needs "
     "a source outside D20's model)",
     "the case is TEMPLATE, which moves only if C1 reverses (P-UNIFORM, D15 or D16)"),
    ("R6-B D27 mover: TEMPLATE's movers include H-UNSOURCED-SEAT", "D27 moves",
     TEMPLATE_MOVES, "TEMPLATE moves only if C1 reverses (P-UNIFORM, D15 or D16)"),
    ("R6-C S13 claim is the held-seat route", "S13 claim", HELD_SEAT_TEXT, ""),
    ("NOTE S10 (open): no verdict rests on it lists TEMPLATE", "S10 (open) claim",
     "SWITCH-ON and TEMPLATE on C1", "SWITCH-ON on C1"),
    ("R6-F report header", "report",
     "M65-1 PRESENCE -- SWITCH-ON, STOCK, TEMPLATE AND EXCITATION",
     "M65-1 PRESENCE -- SWITCH-ON AND EXCITATION"),
    ("R6-F/B report C1 line: SWITCH-ON, TEMPLATE, on H-UNSOURCED-SEAT", "report C1",
     "SWITCH-ON, TEMPLATE (on TEMPLATE, H-UNSOURCED-SEAT)", "SWITCH-ON"),
    ("NOTE report: no P-UNIFORM on H-PRESENT", "report", "on H-PRESENT, no P-UNIFORM",
     "fix phi where they are; no P-UNIFORM"),
    ("NOTE report: remainder label first order", "report",
     "remainder 1 - f_l, first order (H-LINEAR)",
     "remainder 1 - f_l (heavy-quark part CONTESTED)"),
    ("R6-E report: the DISPLACEMENT headline scopes C2", "report",
     "DISPLACEMENT REFUSED on C3 (C2 for a small displacement only) -- as net "
     "formation", "DISPLACEMENT REFUSED on C2, C3 -- as net formation"),
    ("R6-C report: TEMPLATE's row names its priced remainder", "report",
     "TEMPLATE REFUSED on C1 -- on P-UNIFORM and H-UNSOURCED-SEAT; remainder the "
     "held-seat release route, PRICED", "TEMPLATE REFUSED on C1"),
    ("FIX65 report: SWITCH-ON's row names its premise (C1 is a THEOREM on P-UNIFORM)",
     "report", "SWITCH-ON REFUSED on C1 -- on P-UNIFORM",
     "SWITCH-ON REFUSED on C1 "),
    ("R6-C report: the mechanism line names the held-seat route", "report",
     "(the held-seat release route, PRICED; it forms no baryons)", "(the pair route, PRICED)"),
    ("SF3 READINGS defines TEMPLATE", "reading TEMPLATE", _TEMPLATE_DEF,
     "the elements' templates sit at the seat WITHOUT their mass"),
    ("SF3 C1's reason on TEMPLATE", "reason TEMPLATE C1", _C1_TEMPLATE,
     "on P-UNIFORM it is on (D15, D16)"),
    ("SF4 C2's reason on DISPLACEMENT scopes it", "reason DISPLACEMENT C2", C2_SCOPE,
     "read as a SMALL displacement"),
    ("R6-D SWITCH-ON's C5 reason: seated elements are TEMPLATE at |phi| = 0",
     "reason SWITCH-ON C5", "(read with the elements already seated, it is TEMPLATE at "
     "|phi| = 0, refused on C1)", "(read with the elements already seated, it is the "
     "STOCK reading)"),
    ("R6-F _C1_NO names the lowered field", "reason QUANTA C1", "an off or lowered field",
     "an off state"),
    ("R6-F _C2_FINITE names the lowered field", "reason SWITCH-ON C2",
     "the field switched off or lowered", "the field switched off"),
    ("R6-F TEMPLATE's C4 reason names the lowered field", "reason TEMPLATE C4",
     "at the off or lowered field C1 denies (on H-UNSOURCED-SEAT)",
     "at the off state C1 denies"),
    ("R6-F STOCK's C1 reason names the lowered field", "reason STOCK C1",
     "no off or lowered state", "no off state"),
    ("R6-F COUNTS C1 link: off or below v, restores v", "count C1",
     "the field was off, or below v, at the seat and arrival turns it on or restores v",
     "the field was off at the seat and arrival turns it on"),
    ("R6-B COUNTS C1 status: on TEMPLATE also H-UNSOURCED-SEAT", "count C1 status",
     "on TEMPLATE also on H-UNSOURCED-SEAT", "on P-UNIFORM"),
    ("R6-F COUNTS C5 link: the elements present (H-PRESENT)", "count C5",
     "the elements present at the seat (H-PRESENT)", "the elements at the seat"),
    ("R6-C READING_REMAINDERS: TEMPLATE's is the held-seat route", "remainder TEMPLATE",
     HELD_SEAT_TEXT, "none: on P-UNIFORM the unsourced field is at v where the "
     "templates would sit"),
    ("R6-C SURVIVES: the held-seat release route", "survives the held-seat release route",
     HELD_SEAT_TEXT, ""),
    # HELD_SEAT_TEXT, TEMPLATE_MOVES and H_PRESENT_FAILING are constants, so a
    # phrase that IS the constant cannot see a change to it: their content is
    # required literally as well.
    ("R6-C remainder: released by the trigger, on H-RELEASE", "remainder TEMPLATE",
     "a seat prepared in advance with a source holding |phi| below v, released by the "
     "arriving trigger (H-RELEASE); |phi| returns to v and the elements regain their "
     "Higgs-given mass", "the field restores the mass"),
    ("R6-C remainder (i): no baryons", "remainder TEMPLATE",
     "It forms no baryons (C3: the elements were already there)", ""),
    ("R6-C remainder (ii): the field pays, cannot be exceeded, the rest radiated",
     "remainder TEMPLATE", "The energy the field releases as |phi| relaxes to the "
     "elements' own lowering pays for the regained rest energy, which cannot exceed "
     "it, and the rest is radiated (with the elements' own lowering at",
     "The field's own energy pays for the regained rest energy, which cannot exceed "
     "it, and the rest is radiated (with the elements' own lowering at"),
    ("R8 remainder (ii): per joule regained, at least", "remainder TEMPLATE",
     "so per joule regained at least", "so per joule regained"),
    ("R8 remainder: the stable range is within D20's model", "remainder TEMPLATE",
     "Within excite's section-3 model (a static source of fixed number density whose "
     "rest mass is proportional to phi), a static hold is stable only on",
     "Within D20's model (a static source of fixed number density whose rest mass is "
     "proportional to phi), a static hold is stable only on"),
    ("R8 section 6: the stability edge needs excite's section-3 hypotheses", "doc 6",
     "The stability edge of section 5 (d) needs excite's narrower section-3 "
     "hypotheses: a static source of fixed number density whose rest mass is "
     "proportional to phi.  A source whose mass rises convexly with |phi| could hold "
     "stably below it; that is not computed", "The stability edge of section 5 (d) "
     "needs excite's narrower section-3 hypotheses: a source whose mass comes from "
     "phi, rising with |phi|.  No source whose mass comes from phi can hold stably "
     "below it"),
    ("R8 section 5 (d)(ii): shares against the released energy", "doc 5",
     "regained/released = 2.020e-10", "regained/F = 2.020e-10"),
    ("R8 section 5 (d)(ii): the field relaxes to eps0, not v", "doc 5",
     "relaxes to the elements' own lowering eps0 the field releases", "returns to v the "
     "field gives up its own energy"),
    ("R8 S13: the field releases F(eps) - F(eps0)", "S13 claim",
     "The field releases F(eps) - F(eps0)", "The field gives up rho_EW"),
    ("R8 S13: the rest is radiated", "S13 claim",
     "that pays for the regained rest energy and the rest is radiated",
     "that pays for the regained rest energy and all of it is regained"),
    ("R8 D27 mover: H-UNSOURCED-SEAT does not reach SWITCH-ON", "D27 moves",
     "SWITCH-ON moves if C1 reverses (P-UNIFORM, D15 or D16); within excite's "
     "section-3 model (source rest mass proportional to phi) H-UNSOURCED-SEAT failing "
     "does not reach it, since the off state lies past D20's stability edge, where no "
     "static hold stands; a source whose mass rises convexly with |phi| (not computed) "
     "could hold it", "SWITCH-ON moves if C1 reverses (P-UNIFORM, D15 or D16); "
     "H-UNSOURCED-SEAT failing moves it too"),
    ("R8 report: the exact holding-ratio form label", "report",
     "= 4(1-eps)^2/(eps(2-eps)); eps x it -> 2", "= 2/eps at every eps; eps x it -> 2"),
    ("R8 report: the nucleon label excludes the electrons", "report",
     "nucleons at first order (largest READ row)", "electrons and nucleons at first "
     "order"),
    ("R12 section 1: the remainder's range is scoped to excite's section-3 model",
     "doc 1", "on that range only, within excite's section-3 model",
     "on that range only.  H-PRESENT"),
    ("R12 section 6: the remainder's range is scoped to excite's section-3 model",
     "doc 6", "on that range only, within excite's section-3 model",
     "on that range only.  Within excite's"),
    ("R8 report: the stable range within D20's model", "report",
     "within excite's section-3 model (source rest mass proportional to phi), a stable "
     "hold only on", "within D20's model, a stable hold only on"),
    ("R10 no stable range is scoped to bare D20's model", "doc 5",
     "Within excite's section-3 model (source rest mass proportional to phi) a static "
     "hold is stable only below", "Within D20's model a static hold is stable only "
     "below"),
    ("R7-4 remainder (ii): the floor is phi-coupled rest energy, the elements' included",
     "remainder TEMPLATE", "J of phi-coupled rest energy (the prepared source's with "
     "the elements') sat at the seat", "J of source rest energy sat at the seat"),
    ("R7-3 remainder: a stable hold only on the stable range; none below it",
     "remainder TEMPLATE", "a static hold is stable only on " + STABLE_RANGE
     + " (excite.stability_edge): a TEMPLATE seat below that keeps no held-seat "
     "remainder", ""),
    ("R6-C/R7 remainder (iii): eps times the first-order share, not a bound; finite "
     "OPEN", "remainder TEMPLATE", "the nucleons' is eps times the first-order share "
     "at small eps (an estimate, not a bound) and, up to the stability edge, a finite "
     "response that is OPEN like the finite share", "the nucleons' is bounded by the "
     "first-order share only at small eps and by the finite share, OPEN, at large eps"),
    ("R6-C remainder (iv): a prior arrival (D23)", "remainder TEMPLATE",
     "It needs the seat prepared in advance, a prior arrival at <= c (D23)", ""),
    ("R6-B S10 mover: H-UNSOURCED-SEAT failing moves TEMPLATE (literal)", "S10 moves",
     "TEMPLATE moves if C1 reverses: P-UNIFORM, D15 or D16 failing, or H-UNSOURCED-SEAT "
     "failing (a source at the seat holding |phi| < v, which the trigger releases: the "
     "held-seat release route, S13)", "TEMPLATE moves only if C1 reverses"),
    ("R6-B D27 mover: H-UNSOURCED-SEAT failing moves TEMPLATE (literal)", "D27 moves",
     "TEMPLATE moves if C1 reverses: P-UNIFORM, D15 or D16 failing, or H-UNSOURCED-SEAT "
     "failing (a source at the seat holding |phi| < v, which the trigger releases: the "
     "held-seat release route, S13)", "TEMPLATE moves only if C1 reverses"),
    ("R6-A S10 mover: H-PRESENT failing names r > 1 (literal)", "S10 moves",
     "on H-PRESENT failing the case is TEMPLATE (r < 1) or a seat above v (r > 1: "
     "nothing to give; needs a source outside D20's model)",
     "on H-PRESENT failing the case is TEMPLATE"),
    ("R6-F fn C5: below v is TEMPLATE's case, not STOCK's", "fn C5",
     "are TEMPLATE's case, not STOCK's", "the link holds only if the elements LACK "
     "that mass"),
    ("R6-A fn C5: a seat above v leaves nothing to give", "fn C5",
     "a seat above v (r > 1) leaves the trigger nothing to give either", ""),
    ("R6-F fn C1: off or below v", "fn C1", "only if it was off or below v at the seat",
     "only if it was off at the seat"),
    ("R6-B fn C1: below v refuted on H-UNSOURCED-SEAT", "fn C1",
     "for below v, by H-UNSOURCED-SEAT", ""),
    # ---- round 7
    ("R7-1 S13 mover: the finite response, OPEN, up to the stability edge", "S13 moves",
     "the finite response of the nucleon mass to |phi| (OPEN, like the finite share of "
     "S10 (open)), which sets what the nucleons regain up to the stability edge",
     "the finite Higgs share (S10 (open)), which sets what the nucleons regain at "
     "large eps"),
    ("R7-5 fn C1: H-UNSOURCED-SEAT does not reach SWITCH-ON", "fn C1",
     "within excite's section-3 model it does not reach SWITCH-ON's off",
     "it also reaches SWITCH-ON's off state"),
    ("R9 S10 mover: SWITCH-ON also moves on a source outside excite's model", "S10 moves",
     "or if a source outside excite's section-3 model (mass rising convexly with "
     "|phi|; not computed) holds the seat off", ""),
    ("R7-5 SURVIVES: the Higgs an intermediary, not the source (C4)",
     "survives the held-seat release route", "The Higgs is an intermediary, holding "
     "what the source stored, not the source (C4)", "The Higgs is the source (C4)"),
    ("R11 H_UNSOURCED_SEAT_STATUS: the stable range within excite's section-3 model",
     "report", "a stable hold only on " + STABLE_RANGE + " within excite's section-3 "
     "model (source rest mass proportional to phi)", "a stable hold only on "
     + STABLE_RANGE + " (D20)"),
    ("R11 S13 claim: the stability edge within excite's section-3 model", "S13 claim",
     "Within excite's section-3 model (source rest mass proportional to phi) a static "
     "hold is stable only below", "Within D20's model a static hold is stable only "
     "below"),
    ("R11 S13 moves: a convex-mass source could extend the route", "S13 moves",
     "a source whose mass rises convexly with |phi| (outside excite's section-3 model; "
     "not computed)", ""),
    ("R7-5 COUNTS C1 owner: on TEMPLATE, H-UNSOURCED-SEAT", "count C1 owner",
     "on TEMPLATE, H-UNSOURCED-SEAT", ""),
    ("R7-3/5 report: H-UNSOURCED-SEAT's sub-line, an equilibrium, stable on a range",
     "report", "H-UNSOURCED-SEAT: NAMED HYPOTHESIS of C1 on TEMPLATE; not vacuous: a "
     "positive source is an equilibrium on 0 < |phi| < v and a stable hold only on "
     + STABLE_RANGE, "H-UNSOURCED-SEAT: NAMED HYPOTHESIS of C1 on TEMPLATE; not "
     "vacuous: a positive source holds 0 < |phi| < v"),
    ("R7-1 report: the nucleons' first-order figure is not a bound", "report",
     "not a bound; finite OPEN", "an upper bound; finite OPEN"),
    ("R7-5 report: the lowering is per kg/m^3 of Higgs-derived mass", "report",
     "of Higgs-derived mass, inside the measured mass", "inside the measured mass"),
    ("R7-3 report: the stable range, and no remainder below it", "report",
     "a stable hold only on " + STABLE_RANGE + "; below it no held-seat remainder", ""),
    ("R7-4 report: the regained shares, the rest radiated", "report",
     regained_shares_text() + "; the rest is radiated", ""),
    ("R7-4 section 5 (d)(ii): the regained shares at the eps0 samples", "doc 5",
     "With the elements' own lowering at " + regained_shares_text(), ""),
)


def required_wording(locations=None, table=None):
    """[id] for every REQUIRED_WORDING entry whose phrase is missing from its
    location."""
    locations = guard_locations() if locations is None else locations
    table = REQUIRED_WORDING if table is None else table
    return [i for i, loc, phrase, _old in table
            if _norm(phrase) not in locations.get(loc, "")]


def doc_verdict_table(doc=None, with_results=False):
    """{reading: counts} as the section-5 table prints them, or, with
    with_results, {reading: (counts, the RESULT column's text)}."""
    old_doc = globals()["__doc__"]
    try:
        globals()["__doc__"] = __doc__ if doc is None else doc
        sec = _doc_section(5)
    finally:
        globals()["__doc__"] = old_doc
    m = re.search(r"\n  READING +COUNTS THAT ANSWER IT +RESULT\n(.*?)\n\n", sec, re.S)
    rows, last = {}, None
    for ln in (m.group(1).splitlines() if m else []):
        r = re.match(r"^  ([A-Z][A-Z-]+) +(C\d(?:, C\d)*) +(\S.*)$", ln)
        if r:
            last = r.group(1)
            rows[last] = [tuple(sorted(r.group(2).split(", "))), r.group(3).strip()]
        elif last and re.match(r"^ {30,}\S", ln):
            rows[last][1] += " " + ln.strip()
    if with_results:
        return {k: (c, t) for k, (c, t) in rows.items()}
    return {k: c for k, (c, _t) in rows.items()}


def doc_table_mismatch(doc=None, readings=None):
    """[] iff the section-5 table has a row for every READINGS name, with the
    same counts, and no other row."""
    readings = READINGS if readings is None else readings
    want = {n: tuple(sorted(c)) for n, _w, c in readings}
    got = doc_verdict_table(doc)
    return sorted(set(want.items()) ^ set(got.items()))


#: What each section-5 RESULT must say (and, for STOCK, must not): (reading,
#: required phrases, forbidden phrases).
TABLE_RESULTS = (
    ("SWITCH-ON", ("REFUSED on P-UNIFORM",), ()),
    ("TEMPLATE", ("REFUSED on P-UNIFORM and H-UNSOURCED-SEAT",
                  "held-seat release route (survivor d), PRICED"), ("no remainder",)),
    ("STOCK", ("REFUSED on prior mass (H-PRESENT)", "survivor (a)"), ("P-UNIFORM",)),
    ("DISPLACEMENT", ("REFUSED as net formation (C3)", "pair route"), ()),
    ("QUANTA", ("REFUSED as net formation", "pair route"), ()),
    ("CREATION", ("REFUSED", "carrier"), ()),
)


def doc_table_result_faults(doc=None, table=TABLE_RESULTS):
    """[(reading, phrase, 'missing' or 'forbidden')] over the section-5
    table's RESULT column."""
    got = doc_verdict_table(doc, with_results=True)
    bad = []
    for name, need, forbid in table:
        text = got.get(name, ((), ""))[1]
        bad += [(name, p, "missing") for p in need if p not in text]
        bad += [(name, p, "forbidden") for p in forbid if p in text]
    return bad


def doc_overlong_lines(doc=None, width=80):
    """[(line number, length)] for every docstring line wider than `width`."""
    d = __doc__ if doc is None else doc
    return [(i, len(ln)) for i, ln in enumerate(d.splitlines(), 1) if len(ln) > width]


_NUMBER_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
                 "seven": 7}


def reading_count_words(doc=None):
    """[(word, value)] for every 'read N ways' the docstring prints."""
    d = _norm(__doc__ if doc is None else doc)
    return [(w, _NUMBER_WORDS.get(w.lower())) for w in re.findall(r"read (\w+) ways", d)]


_KEEP = re.compile(r"(\w+) READINGS KEEP A REMAINDER, EVERY ONE BUT ([A-Z][A-Z -]*?): "
                   r"(.*?)\.(?:\s|$)")


def doc_remainder_faults(doc=None, remainders=None):
    """[] iff section 0 names, in one sentence, exactly the readings whose
    READING_REMAINDERS entry is not 'none', with their number in words, and
    names the others as the exceptions (round 6, E: computed, not typed)."""
    old_doc = globals()["__doc__"]
    try:
        globals()["__doc__"] = __doc__ if doc is None else doc
        sec = _norm(_doc_section(0))
    finally:
        globals()["__doc__"] = old_doc
    remainders = READING_REMAINDERS if remainders is None else remainders
    keep = {r for r, t in remainders.items() if not t.startswith("none")}
    none = set(remainders) - keep
    m = _KEEP.search(sec)
    if not m:
        return ["no 'N READINGS KEEP A REMAINDER, EVERY ONE BUT ...' sentence"]
    bad = []
    if _NUMBER_WORDS.get(m.group(1).lower()) != len(keep):
        bad.append(("count word", m.group(1), len(keep)))
    but = set(re.split(r" AND ", m.group(2).strip()))
    if but != none:
        bad.append(("exceptions", sorted(but), sorted(none)))
    named = {r for r in remainders if re.search(r"(?<![A-Z-])%s(?![A-Z-])" % re.escape(r),
                                                m.group(3))}
    if named != keep:
        bad.append(("named", sorted(named), sorted(keep)))
    return bad


# ---- the seat, split THREE WAYS as stated (round 6, A)
#: r = |phi|/v at the seat before arrival, v meaning phi as it is where the
#: masses were measured (H-PRESENT's note).  TEMPLATE lacks all or part of the
#: Higgs-given mass (0 <= r < 1); STOCK is H-PRESENT (r = 1); r > 1 is neither
#: reading's claim (the trigger has nothing to give; holding it needs a source
#: outside D20's model).  One boundary sample and one inside each interval.
SEAT_SAMPLES = (Fraction(0), Fraction(1, 1000), Fraction(1, 2), Fraction(999, 1000),
                Fraction(1), Fraction(1001, 1000), Fraction(3, 2))


def _is_template(r):
    return 0 <= r < 1


def _is_stock(r):
    return r == 1


def _is_above(r):
    return r > 1


def _nothing_to_give(r):
    return r >= 1


def seat_case_gaps(template=None, stock=None, above=None, samples=SEAT_SAMPLES):
    """[r] for every sampled seat that is not in exactly one of the three
    cases (TEMPLATE, STOCK, above v).  Empty = the three cases partition the
    samples."""
    template = _is_template if template is None else template
    stock = _is_stock if stock is None else stock
    above = _is_above if above is None else above
    return [r for r in samples if [template(r), stock(r), above(r)].count(True) != 1]


def nothing_to_give_mismatch(samples=SEAT_SAMPLES, ntg=None):
    """[r] where 'the trigger has nothing to give' is not exactly STOCK or above
    v.  Empty = the trigger gives only on TEMPLATE's interval."""
    ntg = _nothing_to_give if ntg is None else ntg
    return [r for r in samples if ntg(r) != (_is_stock(r) or _is_above(r))]


def partial_seat_case(template=None):
    """The case a half-mass seat (r = 1/2) falls in."""
    template = _is_template if template is None else template
    return "TEMPLATE" if template(Fraction(1, 2)) else (
        "STOCK" if _is_stock(Fraction(1, 2)) else "UNCOVERED")


#: Objects the selftest requires to be DERIVED in this source, never typed:
#: (name, the assignment regex, a typed line the control plants in its place).
DERIVED_ASSIGNMENTS = (
    ("C1", r"^FIELD_SWITCHED_ON_BY_ARRIVAL = field_switched_on_by_arrival\(\)$",
     "FIELD_SWITCHED_ON_BY_ARRIVAL = False"),
    ("C5", r"^TRIGGER_GIVES_THE_ELEMENTS_THEIR_MASS = "
           r"trigger_gives_the_elements_their_mass\(\)$",
     "TRIGGER_GIVES_THE_ELEMENTS_THEIR_MASS = False"),
    ("READING_VERDICTS", r"^READING_VERDICTS = derive_readings\(\)$",
     "READING_VERDICTS = {'SWITCH-ON': ('REFUSED', ['C1'])}"),
    ("MECHANISM_VERDICT", r"^MECHANISM_VERDICT = derive_mechanism\(READING_VERDICTS\)$",
     "MECHANISM_VERDICT = ('REFUSED', ['STOCK'])"),
    ("S10 status", r'^     MECHANISM_VERDICT\[0\], \("massform", "MECHANISM_VERDICT"\),$',
     '     "REFUSED", ("massform", "MECHANISM_VERDICT"),'),
    ("HELD_SEAT_ROUTE", r"^HELD_SEAT_ROUTE = held_seat_route\(\)$",
     "HELD_SEAT_ROUTE = {}"),
    ("HELD_SEAT_ROUTE_PRICED", r"^HELD_SEAT_ROUTE_PRICED = held_seat_route_priced\(\)$",
     "HELD_SEAT_ROUTE_PRICED = True"),
    ("STABLE_RANGE", r'^STABLE_RANGE = "%\.4f v < \|phi\| < v" % '
                     r'\(1 - excite\.stability_edge\(\)\)$',
     'STABLE_RANGE = "0.5774 v < |phi| < v"'),
)


def underived(src, table=DERIVED_ASSIGNMENTS):
    """[name] for every object in `table` not assigned from its derivation in
    `src`."""
    return [n for n, pat, _typed in table if not re.search(pat, src, re.M)]


def plant_typed(src, name, table=DERIVED_ASSIGNMENTS):
    """`src` with `name`'s derived assignment replaced by its typed literal."""
    for n, pat, typed in table:
        if n == name:
            return re.sub(pat, lambda _m: typed, src, count=1, flags=re.M)
    return src


def duplicate_dict_keys(src, name):
    """[key source] for every key repeated in the dict literal assigned to
    `name` in `src`: a repeated key silently drops the earlier entry."""
    import ast
    for node in ast.walk(ast.parse(src)):
        if (isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict)
                and any(isinstance(t, ast.Name) and t.id == name for t in node.targets)):
            keys = [ast.dump(k) for k in node.value.keys]
            return sorted({k for k in keys if keys.count(k) > 1})
    return None


_ARXIV = re.compile(r"(?:arXiv:)?((?:hep-ph|hep-th|quant-ph)/\d{7}|\d{4}\.\d{4,5})")


def arxiv_id(locator):
    """The arXiv identifier a SOURCES locator names first, or None."""
    m = _ARXIV.search(locator)
    return m.group(1) if m else None


def refusal_flags(text=None, readings=None, rows=None, contested=None, survives=None,
                  reasons=None):
    """{refusal number: (name, value)}.  Every value DERIVED, from the computed
    objects or a scan of `text`; True would mean the refusal is broken."""
    text = scan_text() if text is None else text
    readings = READING_VERDICTS if readings is None else readings
    rows = share_rows() if rows is None else rows
    t = _norm(text)
    contested = mechanism_contested() if contested is None else contested
    survives = SURVIVES if survives is None else survives
    reasons = READING_REASONS if reasons is None else reasons
    known_bits = (landauer_bits(), bekenstein_bits(), bekenstein_bits(R=0.875))
    bits = [float(b) for b in _BITS.findall(t)]
    return {
        1: ("PRINTS_ONE_HIGGS_SHARE",
            bool(re.search(r"(?i)\bthe higgs share (is|=)", t))
            or any("total" in r[0].lower() for r in rows)),
        2: ("RESOLVES_COLLIDER_DISPUTE",
            COLLIDER_RATE_STATUS != "CONTESTED" or SOURCES["TW-claim"][0] != "CONTESTED"
            or bool(re.search(r"(?i)collider[- ]energy dispute (is|was) "
                              r"(settled|resolved)", t))
            or bool(one_sided_conjecture_claims(text))),
        3: ("REFUSES_ON_A_CONTESTED_FIGURE_ALONE",
            any(v == "REFUSED" and all(contested.get(k, False) for k in cs)
                for v, cs in readings.values())),
        4: ("PRINTS_A_ZERO_TEMPERATURE_RATE_WITHOUT_PREFACTOR",
            bool(re.search(r"(?i)(s\^-1|per second|transitions per (s|year))", t))),
        5: ("CLAIMS_EXACT_ZERO_VEV_ABOVE_TC",
            bool(re.search(r"(?i)(no (yukawa )?masses|vev (is|=) (exactly )?zero|"
                           r"vev vanishes|higgs field vanishes|exactly zero)", t))),
        6: ("QUOTES_A_HUMAN_INFORMATION_CONTENT",
            any(all(abs(b - k) > 1e-3 * k for k in known_bits) for b in bits)),
        7: ("TREATS_LANDAUER_AS_BIT_ENERGY",
            bool(re.search(r"(?i)(energy of (a|one|each) bit (is|=)|"
                           r"(a|each) bit (carries|contains) (k_B T ln 2|energy))", t))),
        8: ("COUNTS_HEAVY_QUARK_COUPLING_AS_HIGGS_MADE_MASS",
            any(not r[1].startswith("CONTESTED") for r in rows
                if "coupling" in r[0] or "sigma_c" in r[0])),
        9: ("DISMISSES_A_PRICED_ROUTE",
            not ANOMALY_ROUTE_PRICED or not PAIR_ROUTE_PRICED
            or not HELD_SEAT_ROUTE_PRICED
            or not any("anomaly" in n for n, _t in survives)
            or not any("pair" in n for n, _t in survives)
            or not any("held-seat" in n for n, _t in survives)
            or bool(unqualified_refusals(text))),
        10: ("HOLDS_A_FIGURE_WITHOUT_ITS_SOURCE_TEXT", bool(check_quotes())),
        11: ("USES_THE_RETIRED_STATUS_WORD",
             bool(re.search(r"\bDECLARED\b", t))
             or any(s == "DECLARED" for s, _l, _x in SOURCES.values())
             or any(r[3] == "DECLARED" for r in PROPOSED_ROWS)),
        12: ("COUNTS_ONE_OBJECTION_TWICE_OR_ONE_THAT_DOES_NOT_ANSWER",
             bool(re.search(r"(?i)((four|five) (independent )?counts|each (count )?alone "
                            r"(is )?sufficient|independent counts|each alone "
                            r"suffices|answers (all|every) (four |five |six )?readings?)", t))
             or bool(reading_reason_table_complete(reasons=reasons))),
    }


# ===================================================================== report
#: Labels that overran _p's 46-column field in the last report() run.
_P_WIDTH = 46
_P_OVERRUNS = []


def _p(label, value, status=""):
    if len(label) > _P_WIDTH:
        _P_OVERRUNS.append(label)
    print("      %-46s %20s  %s" % (label, value, status))


def report():
    print(__doc__.split("=====", 1)[0].strip())
    print()
    print("=" * 79)
    print("M65-1  PRESENCE -- SWITCH-ON, STOCK, TEMPLATE AND EXCITATION")
    print("=" * 79)
    v = vev_gev()
    _p("v = higgs.vev()", "%.6f GeV" % v, "NAMED-NOT-READ (G_F)")
    print("      %-10s %16s %18s" % ("fermion", "m (MeV, READ)", "y = sqrt2 m/v"))
    for f, y in yukawas().items():
        print("      %-10s %16.9g %18.6e" % (f, MASS_MEV[f], y))
    _p("consideration: massive e, u, d force phi != 0", CONSIDERATION_HOLDS,
       "THEOREM on H-TREE")
    _p("P-UNIFORM: the vev takes one value unsourced", VEV_IS_UNIFORM, P_UNIFORM_STATUS)
    _p("so the condition singles out the seat", CONSIDERATION_DISCRIMINATES)
    _p("D15 excite.TAIL_RATE_IS_MASS", excite.TAIL_RATE_IS_MASS, "THEOREM")
    _p("D16 excite.DISPLACEMENT_IS_ULTRALOCAL", excite.DISPLACEMENT_IS_ULTRALOCAL,
       "THEOREM")
    _p("  tail length hbar/(m_h c)", _e(excite.LAMBDA_H_READ_M, 3) + " m", "READ m_h")
    _p("D20 source = 4 eps(2-eps)(1-eps)^2, exactly", source_factorisation_holds(),
       "asked of excite")
    for iv, s, above in source_sign_table():
        print("        eps in (%4s, %4s): source sign %+d   |phi| > v: %s"
              % (iv[0] if iv[0] is not None else "-inf",
                 iv[1] if iv[1] is not None else "inf", s, above))
    _p("a positive source can RAISE |phi| above v", SOURCE_CAN_RAISE_VEV,
       "THEOREM in D20's model")
    _p("a positive source can hold some eps (excite)", FIELD_CAN_BE_EXCITED)
    _p("source/field -> 2/eps; eps x ratio at 1e-9",
       "%.9f" % (excite.holding_ratio(Fraction(1, 10 ** 9)) * Fraction(1, 10 ** 9)))
    _p("D19 excite.FLAT_DIRECTIONS_ARE_INERT", excite.FLAT_DIRECTIONS_ARE_INERT)
    print("      D18 excite.ELECTRON_MASS_IS_A_RULER = %r" % excite.ELECTRON_MASS_IS_A_RULER)
    _p("higgs.CANNOT_BE_SWITCHED_ON_IN_ONE_PLACE", higgs.CANNOT_BE_SWITCHED_ON_IN_ONE_PLACE,
       "WITHDRAWN (DOCKET 63 F3)")
    _p("Higgs quantum lifetime (excite)", excite.one_sig(excite.QUANTUM_LIFETIME_S) + " s")
    _p("Higgs quanta with total rest energy Mc^2",
       "%.4e" % (rest_energy_j() / (higgs.M_HIGGS * higgs.GEV_IN_J)))
    _p("C1 FIELD_SWITCHED_ON_BY_ARRIVAL", FIELD_SWITCHED_ON_BY_ARRIVAL,
       "SWITCH-ON, TEMPLATE (on TEMPLATE, H-UNSOURCED-SEAT)")
    print("        H-UNSOURCED-SEAT: %s" % H_UNSOURCED_SEAT_STATUS)
    _p("fermion masses proportional to phi (MRM-phi)", MASS_PROPORTIONAL_TO_PHI, "READ")
    _p("C5 TRIGGER_GIVES_THE_ELEMENTS_THEIR_MASS", TRIGGER_GIVES_THE_ELEMENTS_THEIR_MASS,
       "STOCK: PRIOR MASS")
    print("        on H-PRESENT, no P-UNIFORM: the elements' own masses fix phi there")
    print("        H-PRESENT: %s" % H_PRESENT_STATUS)
    print("        (names of the premise C5's code reads: %s)"
          % (reads_p_uniform(trigger_gives_the_elements_their_mass) or "none"))
    _p("the matter's own lowering, eps per kg/m^3", _e(self_lowering_per_kg_m3(), 4),
       "of Higgs-derived mass, inside the measured mass")
    print("      THE HELD-SEAT RELEASE ROUTE (TEMPLATE's remainder; H-UNSOURCED-SEAT fails)")
    h = HELD_SEAT_ROUTE
    _p("eps priced (excite.EPS_CHEMICAL)", str(h["eps"]), "asked")
    _p("  source S, field F (units of rho_EW)", "%.6f, %.6f"
       % (h["source (rho_EW)"], h["field (rho_EW)"]), "excite.holding_terms")
    _p("  source S (J/m^3)", _e(h["source J/m^3"], 4), "D20")
    _p("  field F (J/m^3), what pays the regain", _e(h["field J/m^3"], 4), "D20")
    _p("  J of source per J of field", "%.4f" % h["source per J of field"],
       "excite.holding_ratio")
    _hf = holding_ratio_form()
    _p("  = 4(1-eps)^2/(eps(2-eps)); eps x it -> 2", "%s; %s" % (_hf[0], _hf[1]),
       "exact, excite's polynomials")
    _p("  Higgs-derived density of the source", _e(h["Higgs-derived kg/m^3"], 4) + " kg/m^3",
       "excite.exact_source_density")
    _p("  stable (eps below the stability edge)", h["stable"],
       "edge %.4f, excite" % excite.stability_edge())
    print("        within excite's section-3 model (source rest mass proportional to "
          "phi), a stable hold only on %s; below it no held-seat "
          "remainder" % STABLE_RANGE)
    _p("  balance faults over the eps0 samples", str(h["balance faults"]),
       "exact over Fraction; H-RELEASE")
    print("        %s; the rest is radiated" % regained_shares_text())
    _p("  electrons regained / payload mass", _e(h["electrons regained"], 4),
       "exact on H-TREE")
    _p("  nucleons at first order (largest READ row)", _e(h["nucleons first order"], 4),
       "not a bound; finite OPEN")
    _p("  forms baryons (C3)", h["forms baryons"], "the elements were there")
    _p("  needs a prior arrival at <= c (D23)", preparation_needs_prior_arrival(),
       "ledger D23, asked")
    _p("  PRICED", HELD_SEAT_ROUTE_PRICED, "on H-RELEASE, a named hypothesis")
    print()
    print("=" * 79)
    print("M65-2  SHARE   (stock.HUMAN at %.0f kg, asked of stock.feedstock_kg)"
          % PAYLOAD_KG)
    print("=" * 79)
    c = COUNTS
    for k in ("B", "N_e", "N_p", "N_n"):
        _p(k, "%.6e" % c[k], "MEASURED; u, A_r NAMED-NOT-READ; Z READ")
    _p("listed mass fraction (H-LIST)", "%.6f" % c["listed"])
    _p("binding closure per +0.01 in every A (H-A)", "%.6f kg" % binding_sensitivity_kg())
    for k, kg in payload_masses().items():
        _p(k, "%.6f kg" % kg)
    vp, vn = valence_fractions()
    _p("naive valence, proton (2m_u+m_d)/m_p", "%.4f %%" % (100 * vp), "READ inputs")
    _p("naive valence, neutron (m_u+2m_d)/m_n", "%.4f %%" % (100 * vn), "READ inputs")
    _p("m_N = (m_p+m_n)/2", "%.7f MeV" % M_N_MEV, "READ")
    for k, (a, b, st) in SIGMA_MEASURES.items():
        f = F_LIGHT[k]
        _p("f_l %s (%.1f + %.1f)/m_N" % (k, a, b), "%.4f %%" % (100 * f), st)
        _p("  SVZ heavy-quark coupling (2/9)(1-f_l)",
           "%.4f" % float(svz_heavy_sum(Fraction(f))), "CONTESTED as mass")
        _p("  six-quark coupling 2/9 + 7/9 f_l",
           "%.4f" % float(coupling_sum(Fraction(f))), "CONTESTED as mass")
        _p("  remainder 1 - f_l, first order (H-LINEAR)",
           "%.4f %%" % (100 * (1 - f)), "heavy-quark part CONTESTED")
    print("      the 2.7 sigma between the FLAG averages: recorded; neither chosen")
    for k, fr in JI_FRACTION.items():
        _p("Ji quark mass term b, %s" % k, "%.4f %%" % (100 * fr), "READ, Table I")
    _p("sigma_piN, Roy-Steiner (alone)", "%.4f %%"
       % (100 * SIGMA_PIN_ROY_STEINER / M_N_MEV), "READ")
    print()
    print("      the payload, measure by measure -- NEVER SUMMED ACROSS ROWS")
    print("      every row inherits %s" % SHARE_INHERITS)
    for name, st, frac, what, _inh in share_rows():
        print("      %-48s %11.4e  %-20s %s" % (name, frac, st, what))
    _p("largest central reading, READ rows only", "%.4f" % HIGGS_SHARE_LARGEST_READ,
       "central, not a bound")
    _p("largest central reading, all rows", "%.4f" % HIGGS_SHARE_LARGEST_ALL,
       "central, not a bound")
    _p("READ rows, margin illustration (not a bound)", "%.4f"
       % HIGGS_SHARE_READ_MARGIN, "FLAG +%d sigma (file's choice)" % MARGIN_SIGMAS)
    print("        Ji row + %g MeV omitted error + %g MeV difference of his two"
          % (JI_ROUNDING_MEV, JI_ESTIMATE_DIFFERENCE_MEV))
    print("        estimates, which his largest uncertainty 'could be larger than'")
    _p("C2 HIGGS_SUPPLIES_MOST_ATOMIC_MASS", HIGGS_SUPPLIES_MOST_ATOMIC_MASS,
       "DISPLACEMENT (first order, H-LINEAR)")
    _p("FINITE Higgs share (field switched off)", FINITE_HIGGS_SHARE_STATUS,
       "not computed, not read")
    _p("  exceeds one half?", str(FINITE_HIGGS_SHARE_EXCEEDS_HALF), "undecided here")
    print()
    print("=" * 79)
    print("M65-3  ENERGY -- THE ONLY CANDIDATE SOURCE IN M'S SENTENCE, AND THE CARRIER")
    print("=" * 79)
    _p("T_scalar T_00 = phi_t^2/2 + |grad|^2/2 + V", T00_DECOMPOSES,
       "THEOREM, exact grid, real scalar")
    print("      H-REAL: doublet and gauge terms non-negative -- claimed, not computed")
    _p("V(phi) - V(v) = rho_EW (eps(2-eps))^2", FIELD_ENERGY_IS_A_SQUARE,
       "asked of excite")
    _p("rho_EW (excite.RHO_EW)", "%.4e J/m^3" % excite.RHO_EW, "inherits NAMED-NOT-READ")
    _p("the field releases energy about v", HIGGS_FIELD_RELEASES_ENERGY_ABOUT_V,
       "THEOREM on H-TREE-V, H-REAL")
    _p("metastability preferred (1307.3536)", METASTABILITY_PREFERRED, "READ")
    _p("the vacuum's fate established", VACUUM_FATE_ESTABLISHED, "READ")
    _p("  and it turns on the top mass", METASTABILITY_TURNS_ON_TOP_MASS, "READ")
    _p("decay: different particle masses inside", DECAY_CHANGES_PARTICLE_MASSES, "READ")
    _p("decay: destroys everything in its way", DECAY_DESTROYS_WHAT_IT_MEETS, "READ")
    _p("  (Degrassi's earlier 2 sigma holds for M_h <", "%g GeV" % DG_MH_CONDITION_GEV, "READ")
    _p("vacuum decay forms atomic mass at the seat",
       VACUUM_DECAY_FORMS_ATOMIC_MASS_AT_THE_SEAT, "INFERENCE from READ text")
    _p("C4 stable case / metastable case",
       "%s / %s" % (field_supplies_mass_energy(False), field_supplies_mass_energy(True)))
    _p("C4 HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY", HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY,
       "CREATION")
    E = rest_energy_j()
    _p("Mc^2 (warpfolder.rest_energy_j)", "%.6e J" % E, "the carrier must bring it")
    _p("  in megatons (warpfolder.megatons)", "%.1f" % warpfolder.megatons(E))
    _p("  with B, L conserved (section 4 floor)", "%.6e J" % pair_floor_j(), "THEOREM")
    print("      %s" % N_INFO)
    _p("T_CMB (permute.T_CMB)", "%.4f K" % T_CMB, "CITED")
    _p("k_B T ln 2 (nopath.landauer_energy)", "%.6e J" % nopath.landauer_energy(1.0, T_CMB))
    _p("erased bits whose minimum heat = Mc^2", "%.6e" % landauer_bits(), "inherits CITED")
    _p("Bekenstein, E = Mc^2, R = 1 m (H-R)", "%.6e bits" % bekenstein_bits(),
       "bound, in bit units")
    print("      not read as an information capacity: 'folklore rather than "
          "established fact' (HW-folk)")
    _p("ratio (computed from the two counts)", "%.4f" % (bekenstein_bits() / landauer_bits()))
    _p("ratio 2 pi R k_B T/(hbar c), no M", "%.4f" % bek_over_landauer_closed())
    _p("break-even R = hbar c/(2 pi k_B T)", "%.6e m" % break_even_radius_m())
    _p("nopath.LANDAUER_IS_THE_WEAKER_HALF", nopath.LANDAUER_IS_THE_WEAKER_HALF)
    _p("nopath.BEKENSTEIN_IS_THE_ARGUMENT", nopath.BEKENSTEIN_IS_THE_ARGUMENT)
    print("      human information content: NOT-FOUND (Braunstein, Nelms et al.); "
          "not quoted")
    print()
    print("=" * 79)
    print("M65-4  CONSERVATION")
    print("=" * 79)
    for name, t in YUKAWA_TERMS.items():
        _p("(B, L) of %s" % name, str(tuple(str(x) for x in term_charge(t))))
    _p("(B, L) of the anomaly vertex, N_F = %d" % N_F,
       str(tuple(str(x) for x in THOOFT_DELTA_B_L)), "READ rule reproduced")
    _p("C3 HIGGS_COUPLING_CARRIES_B_OR_L", HIGGS_COUPLING_CARRIES_B_OR_L,
       "DISPLACEMENT, QUANTA, CREATION")
    _p("B - L of the payload = N_n", "%.6e" % c["B_minus_L"])
    lb = lightest_baryon()
    _p("lightest baryon in the capture", "%s %.6f MeV" % lb, "READ")
    _p("mu_min, AME2020 measured (nuclear/nucleon)", "%.4f MeV (%d%s)"
       % (MU_MIN[0], MU_MIN[2], MU_MIN[1]))
    _p("gravitational binding order G M/(R c^2)", "%.3e" % gravitational_binding_order(),
       "H-AME, R = 1 m")
    _p("pair floor / Mc^2", "%.6f" % (pair_floor_j() / E), "THEOREM")
    _p("mirror antipayload / Mc^2 (CPT)", "2", "THEOREM")
    _p("antibaryon number to be held apart", "%.6e" % c["B"])
    _p("THE PAIR ROUTE (EXCITATION's remainder) priced", PAIR_ROUTE_PRICED,
       "Higgs an intermediary")
    aw, g = alpha_w()
    _p("g = 2 m_W / v", "%.6f" % g, "inherits NAMED-NOT-READ")
    _p("alpha_W = g^2/4pi", "%.6f = 1/%.4f" % (aw, 1 / aw))
    print("      ZERO TEMPERATURE: instanton tunnelling")
    _p("log10 exp(-4 pi/alpha_W)", "%.4f" % log10_suppression())
    _p("log10 exp(-16 pi^2/g^2)", "%.4f" % log10_suppression_g())
    _p("transitions needed ceil(B/N_F)", "%.6e" % transitions_needed())
    _p("log10 (attempts x prefactor) needed", "%.4f" % log10_attempts_times_prefactor())
    print("      NO RATE PRINTED: the prefactor was not read (refusal 4).")
    _p("RS96 eq.(2.8) printed log10, alpha_W = 1/29", "%.0f" % RS96_PRINTED_LOG10, "READ")
    _p("  the arithmetic at 1/29", "%.4f" % log10_suppression(1.0 / RS96_ALPHA_INV),
       "recorded, not repaired")
    print("      OVER THE BARRIER: the sphaleron")
    _p("2 m_W/alpha_W", "%.4f TeV" % esph_formula_tev(1.0))
    for B_ in B_KM_RANGE + (sum(TW_B_TERMS),):
        _p("  x B = %.2f" % B_, "%.4f TeV" % esph_formula_tev(B_))
    for k, tev in E_SPH_TEV.items():
        _p("E_sph READ, %s" % k, "%.2f TeV" % tev, "READ")
        _p("  / rest energy of %d baryons" % N_F, "%.1f" % esph_over_three_baryons(tev))
    _p("sum of barrier heights / Mc^2", "%.1f" % barrier_heights_over_mc2(),
       "%s; heights, not a cost" % E_SPH_USED)
    _p("leptons beyond the payload", "%.6e" % extra_leptons(), "B - L conservation")
    _p("  H-FLAV only: electron-family shortfall", "%.6e" % electron_family_shortfall(),
       "carries no verdict")
    print("      THERMAL")
    _p("T_c (1508.07161 abstract)", "%.1f GeV = %.4e K" % (T_C_GEV, t_kelvin(T_C_GEV)), "READ")
    _p("Gamma/T^4 above T_c (1404.3565 eq. 8)", "%.1e" % RATE_SYMM_READ, "READ, the figure")
    _p("  18 alpha_W^5 at this alpha_W", "%.4e" % symmetric_rate_crosscheck(),
       "cross-check only")
    _p("vev above T_c 'approximately zero'", VEV_ABOVE_TC_IS_APPROXIMATELY_ZERO, "READ")
    print("      warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY = %r"
          % warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY)
    _p("freeze-out T*", "%.1f GeV = %.4e K" % (T_FREEZE_GEV, t_kelvin(T_FREEZE_GEV)), "READ")
    _p("transitions run below T_c, vev finite", SPHALERONS_RUN_WHERE_VEV_IS_FINITE,
       "READ T* < T_c")
    _p("fit bounded by its own paper's T_c (DRT-Tc)", "%.1f GeV" % BROKEN_FIT_HIGH_GEV, "READ")
    for T in (T_FREEZE_GEV, 140.0, 155.0, BROKEN_FIT_HIGH_GEV):
        ln = broken_phase_ln_rate(T)
        note = "READ fit" if 140.0 <= T <= 155.0 else "READ fit, outside 140-155 measured"
        _p("  broken phase ln(Gamma/T^4) at %.1f GeV" % T, "%.2f (%.2e)" % (ln, math.exp(ln)),
           note)
    print("      two-particle collisions near and above E_sph: %s --" % COLLIDER_RATE_STATUS)
    print("        (not the instanton's T = 0 factor; not the thermal sphaleron rate)")
    for role, key in (("prevalent", "BLRRT"), ("prevalent", "BLRRT-PLB"),
                      ("  on", "BLRRT-conj"), ("prevalent", "KM-2020"),
                      ("dissent", "TW-claim"), ("dissent", "TW-2017"),
                      ("rebuttal", "FFS-rebut"), ("experiment", "CMS")):
        st, loc, _t = SOURCES[key]
        print("        %-10s %-10s %-9s arXiv %s" % (role, key, st, arxiv_id(loc)))
    print("      CMS: PEF < %g at %g TeV, %g fb^-1 -- an upper limit; it decides nothing"
          % (CMS_PEF_BOUND, CMS_SQRT_S_TEV, CMS_LUMI_FB))
    print("      the prevalent results rest on conjectures and assumptions their authors")
    print("      state as unproven, not theorems; the dissent is no firmer by its own")
    print("      account -- Tye-Wong (1710.07223 p.2): 'both estimates involve assumptions")
    print("      based on intuitions as well as approximations remaining to be fully")
    print("      justified'; their own figure is 'only an order of magnitude guesstimate'")
    print("      (p.3).  The rebuttal (1612.05431, 'in the leading order of the WKB")
    print("      approximation') is not conceded: 1710.07223 replies on p.3, 'the above")
    print("      argument is somewhat misleading'.  NOT RESOLVED; no refusal rests on it.")
    print()
    print("=" * 79)
    print("M65-5  VERDICT, READING BY READING")
    print("=" * 79)
    for cid, name, owner, st, cont, what in COUNTS_ON_THE_MECHANISM:
        print("      %s %-38s = %-5s %s%s" % (cid, name, globals()[name], st,
                                              "  [contested only]" if cont else ""))
        print("         link: %s;  owner %s.%s" % (what, owner[0], owner[1]))
    print()
    for name, what, cids in READINGS:
        v = READING_VERDICTS[name]
        print("      %-12s %s (answered by %s)" % (name, reading_row(name), ", ".join(cids)))
        print("                  %s" % what)
        for cid in [c[0] for c in COUNTS_ON_THE_MECHANISM]:
            yes, why = READING_REASONS[(name, cid)]
            print("                  %s %s: %s" % (cid, "answers" if yes else "does not", why))
        print("                  remainder: %s" % READING_REMAINDERS[name])
    print()
    print("      THE MECHANISM AS STATED: %s" % mechanism_label())
    print("      THE CONSIDERATION:       %s" % CONSIDERATION_VERDICT)
    print()
    print("      WHAT SURVIVES")
    for name, text in SURVIVES:
        print("        %s: %s" % (name, text))
    print()
    print("      LEDGER ROWS (seated by ledger.py, which asks their text here; "
          "this file edits no peer).  'S5 (note)' is appended to S5's note and "
          "'S10 (open)' is an OPEN item inside S10's note, not a row (M-D65-2)")
    for rid, side, claim, st, owner, moves in PROPOSED_ROWS:
        print("        %-9s %-6s %-16s owner %s.%s" % (rid, side, st, owner[0], owner[1]))
        print("          %s" % claim)
        print("          what would move it: %s" % moves)
    print("        not opened: %s" % "; ".join(NOT_OPENED))
    print()
    print("  NOTHING IS REPAIRED.")


# =================================================================== selftest
def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-64s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    def chkrel(label, got, want, rtol):
        ok = abs(got - want) <= rtol * abs(want)
        print("  [%s] %-64s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("massform.py --selftest\n")

    # ---------------------------------------------- imported, never copied
    for modname, names in IMPORTS:
        mod = _mod(modname)
        for n in names:
            obj = getattr(mod, n, None)
            chk("%s.%s exists" % (modname, n), obj is not None, True)
            if callable(obj) and inspect.isfunction(obj):
                chk("  and is defined in %s" % modname, obj.__module__, modname)
    chk("no owner function is redefined here under its own name",
        [n for n in ("vev", "_capture_row", "holding_terms", "landauer_energy",
                     "symbol_to_Z", "nuclides", "megatons", "baryons_in", "T_scalar",
                     "pmul", "peval")
         if n in globals() and inspect.isfunction(globals()[n])], [])
    # asked constants ARE the owners' objects (identity, not value)
    chk("T_CMB IS permute.T_CMB", T_CMB is permute.T_CMB, True)
    chk("U_KG IS gravity.U_KG", U_KG is gravity.U_KG, True)
    chk("C IS higgs.c; G_NEWTON IS higgs.G", (C is higgs.c, G_NEWTON is higgs.G), (True, True))
    chk("COMPOSITION IS stock.HUMAN", COMPOSITION is stock.HUMAN, True)
    chk("PAYLOAD_KG IS stock.feedstock_kg's default object",
        PAYLOAD_KG is inspect.signature(stock.feedstock_kg).parameters["payload_kg"].default,
        True)
    chk("CONTROL a retyped copy of T_CMB is NOT the owner's object",
        float(repr(permute.T_CMB)) is permute.T_CMB, False)
    # ... and each is assigned from its owner in this file's own source
    src = inspect.getsource(sys.modules[__name__])
    assigns = (r"^T_CMB = permute\.T_CMB\b", r"^U_KG = gravity\.U_KG\b",
               r"^C = higgs\.c\b", r"^G_NEWTON = higgs\.G\b",
               r"^COMPOSITION = stock\.HUMAN\b",
               r"^PAYLOAD_KG = inspect\.signature\(stock\.feedstock_kg\)",
               r"^N_F = n_generations\(\)", r"^MASS_MEV = _read_masses\(\)",
               r'^M_W_GEV = MASS_MEV\["W"\] / 1000\.0',
               r'^M_N_MEV = \(MASS_MEV\["p"\] \+ MASS_MEV\["n"\]\) / 2\.0')
    chk("each asked constant is assigned from its owner in this source",
        [a for a in assigns if not re.search(a, src, re.M)], [])
    # the masses follow the owner's reader: a mutated reader moves them
    real = higgs._capture_row
    mutated = _read_masses(lambda i: dict(real(i), mass_MeV=str(float(real(i)["mass_MeV"])
                                                                * 2)))
    chk("CONTROL a mutated capture reader doubles every mass read",
        all(mutated[k] == 2 * MASS_MEV[k] for k in MASS_MEV), True)
    chk("m_W is the capture row 24 as read now", M_W_GEV,
        float(higgs._capture_row(24)["mass_MeV"]) / 1000.0)
    chk("N_F is recounted from the capture now", N_F, n_generations())

    # ------------------------------------------------------- M's words
    ledger = _ledger()
    row = [r for r in ledger.RULED_BY_M if r[0] == M_ROW][0]
    text = _norm(" ".join(str(x) for x in row))
    chk("M's mechanism is verbatim in ledger row M-S1A-P1", M_MECHANISM in text, True)
    chk("M's consideration is verbatim in the same row", M_CONSIDERATION in text, True)
    chk("the row names DOCKET 65", "DOCKET 65" in text, True)
    chk("the docstring quotes both verbatim",
        (_norm(M_MECHANISM) in _norm(__doc__), _norm(M_CONSIDERATION) in _norm(__doc__)),
        (True, True))

    # ------------------------------------------------ the ledger rows asked
    dem = {r[0]: r for r in ledger.DEMAND}
    sup = {r[0]: r for r in ledger.SUPPLY}
    for rid, st, owner in (("D15", ledger.THEOREM, ("excite", "TAIL_RATE_IS_MASS")),
                           ("D16", ledger.THEOREM, ("excite", "DISPLACEMENT_IS_ULTRALOCAL")),
                           ("D18", ledger.THEOREM, ("excite", "ELECTRON_MASS_IS_A_RULER")),
                           ("D19", ledger.THEOREM, ("excite", "FLAT_DIRECTIONS_ARE_INERT")),
                           ("D20", ledger.MEASURED, ("excite", "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18")),
                           ("D25", ledger.OPEN, ("stockgate", "GATE"))):
        chk("ledger %s is %s, owned by %s.%s" % ((rid, st) + owner),
            (dem[rid][2], dem[rid][3]), (st, owner))
    for rid, st, owner in (("S5", ledger.OPEN, ("branelink", "S5_FIGURES_MEASURED")),
                           ("S6", ledger.REFUSED, ("excite", "ROLE1_DOMINATED_BY_OWN_SOURCE")),
                           ("S7", ledger.REFUSED, ("excite", "ROLE2_REBINDS")),
                           ("S8", ledger.REFUSED, ("higgs", "MINIMAL_SCALAR_SATISFIES_NEC")),
                           ("S9", ledger.REFUSED, ("warpfolder", "FLASH_IS_A_RECONSTRUCTION_MECHANISM"))):
        chk("ledger %s is %s, owned by %s.%s" % ((rid, st) + owner),
            (sup[rid][2], sup[rid][3]), (st, owner))
    # SEATED (DOCKET 65, M: "Seat as proposed").  This check first asked that
    # the proposed ids be FREE on the board; the board has moved, so it now
    # asks that every row is seated there as this file states it -- the text,
    # status and owner ledger.py carries are the ones asked here.
    opn = {r[0]: r for r in ledger.OPEN_ROWS}
    s5_add = [r for r in PROPOSED_ROWS if r[0] == "S5 (note)"][0][2]
    chk("every proposed row is seated on the board as stated here",
        [r[0] for r in PROPOSED_ROWS
         if not ((r[1] == "DEMAND" and r[0] in dem
                  and dem[r[0]][1:] == (r[2], r[3], r[4], r[5]))
                 or (r[1] == "SUPPLY" and r[0] in sup
                     and (sup[r[0]][2], sup[r[0]][3]) == (r[3], r[4])
                     and r[2] in sup[r[0]][4] and r[5] in sup[r[0]][4])
                 or (r[1] == "OPEN" and r[0] in opn
                     and opn[r[0]][1:] == (r[2], r[5], r[4]))
                 or (r[0] == "S5 (note)" and sup["S5"][2] == r[3].split(" (")[0]
                     and s5_add.split(": ", 1)[1] in sup["S5"][4])
                 # M-D65-2: the finite share is an OPEN item inside S10's note.
                 or (r[0] == "S10 (open)" and r[0] not in opn
                     and r[2] in sup["S10"][4] and r[5] in sup["S10"][4]))], [])
    chk("every proposed status is in the ledger's vocabulary",
        [r[3] for r in PROPOSED_ROWS
         if r[3].split(" (")[0] not in (ledger.THEOREM, ledger.MEASURED, ledger.OPEN,
                                        ledger.REFUSED, ledger.SURVEY)], [])
    chk("S9's owner says the flash is not a reconstruction mechanism",
        warpfolder.FLASH_IS_A_RECONSTRUCTION_MECHANISM, False)

    # ------------------------------------------------ READ masses, fixtures
    # FIXTURES: captures/PDG-2026.tsv's own rows, reproduced through
    # higgs._capture_row, never typed into the computation.
    chk("m_e READ 0.510998951 MeV", MASS_MEV["e"], 0.510998951)
    chk("m_p READ 938.272089 MeV", MASS_MEV["p"], 938.272089)
    chk("m_n READ 939.565422 MeV", MASS_MEV["n"], 939.565422)
    chk("m_W READ 80.362 GeV", M_W_GEV, 80.362)
    chk("m_u, m_d READ 2.16, 4.7 MeV", (MASS_MEV["u"], MASS_MEV["d"]), (2.16, 4.7))
    chkrel("m_e/m_p = 5.446170e-4 (the READ finding's ratio)",
           MASS_MEV["e"] / MASS_MEV["p"], 5.446170e-4, 1e-6)
    chkrel("m_N = 938.9187555 MeV (the READ finding's figure)", M_N_MEV, 938.9187555, 1e-12)
    chk("the lightest baryon in the capture is the proton", lightest_baryon()[0], "p")
    chk("N_F counted from the capture's charged leptons", N_F, 3)
    chk("which is the 3 of the READ rule's '3 . 3'", "3 . 3" in SOURCES["RS96-sel"][2], True)
    chk("RS96-sel is held in the source's order (factor sentence first)",
        SOURCES["RS96-sel"][2].index("factor 1/3") < SOURCES["RS96-sel"][2].index("Delta N_e"),
        True)

    # ------------------------------------------------------------ M65-1
    chkrel("v from higgs.vev() (higgs's own fixture 246.2196)", vev_gev(), 246.2196, 1e-5)
    y = yukawas()
    chkrel("y_t = sqrt2 x 172.6 GeV / v", y["t"], math.sqrt(2) * 172.6 / vev_gev(), 1e-12)
    chk("y_t is of order one, y_e of order 1e-6",
        (0.9 < y["t"] < 1.1, 1e-6 < y["e"] < 1e-5), (True, True))
    pert = dict(MASS_MEV, e=MASS_MEV["e"] * 1.01)
    chkrel("CONTROL m_e x 1.01 moves y_e by exactly 1.01",
           yukawas(pert)["e"] / y["e"], 1.01, 1e-12)
    chk("  and moves no other Yukawa",
        all(yukawas(pert)[f] == y[f] for f in CHARGED_FERMIONS if f != "e"), True)
    chk("consideration holds (massive e, u, d force phi != 0)", CONSIDERATION_HOLDS, True)
    chk("CONTROL with e, u, d massless it is NOT ESTABLISHED",
        derive_consideration(consideration_holds(dict(MASS_MEV, e=0.0, u=0.0, d=0.0))),
        "NOT ESTABLISHED")
    chk("P-UNIFORM is a named PREMISE, not an owner boolean",
        (P_UNIFORM, P_UNIFORM_STATUS, "P_UNIFORM" not in dir(higgs)), (True, "PREMISE", True))
    chk("  higgs's caveat (b) words begin 'IT IS UNIFORM' (asked for its words)",
        higgs.CAVEAT_B_AS_FIRST_WRITTEN.startswith("IT IS UNIFORM"), True)
    chk("so the consideration discriminates nothing", CONSIDERATION_DISCRIMINATES, False)
    chk("CONSIDERATION VERDICT", CONSIDERATION_VERDICT,
        "TRUE, AND, ON P-UNIFORM, DISCRIMINATES NOTHING")
    chk("CONTROL the consideration's second half carries P-UNIFORM only where "
        "the premise is its reason",
        (derive_consideration(True, False, True), derive_consideration(True, False, False),
         derive_consideration(True, True, True), "P-UNIFORM" in CONSIDERATION_VERDICT),
        ("TRUE, AND, ON P-UNIFORM, DISCRIMINATES NOTHING", "TRUE, AND DISCRIMINATES NOTHING",
         "TRUE", True))
    chk("SWITCH-ON's refusal is printed on P-UNIFORM in the mechanism label "
        "(C1 is a THEOREM on it)",
        "on SWITCH-ON on P-UNIFORM (C1 alone)" in mechanism_label(), True)
    chk("STOCK's refusal is printed on C5's premise in the mechanism label, asked "
        "of C5's status: H-TREE, with H-PRESENT the STOCK case's definition",
        ("; on STOCK on H-TREE (C5 alone; H-PRESENT is its case definition)"
         in mechanism_label(),
         reading_premises("STOCK", any_count=True), reading_premises("STOCK"),
         reading_case_definition("STOCK")),
        (True, ["H-TREE"], [], ["H-PRESENT"]))
    _keep_counts = COUNTS_ON_THE_MECHANISM
    globals()["COUNTS_ON_THE_MECHANISM"] = tuple(
        (c[0], c[1], c[2], "THEOREM (PRIOR MASS); needs no P-UNIFORM", c[4], c[5])
        if c[0] == "C5" else c for c in _keep_counts)
    try:
        _lab_c5 = mechanism_label()
        _prem_c5 = reading_premises("STOCK", any_count=True)
    finally:
        globals()["COUNTS_ON_THE_MECHANISM"] = _keep_counts
    chk("CONTROL C5's status edited to name no hypothesis drops STOCK's premise "
        "clause from the label (asked of the status, not typed)",
        ("on STOCK on" in _lab_c5, _prem_c5), (False, []))
    _s10_claim = [r for r in PROPOSED_ROWS if r[0] == "S10"][0][2]
    _src = open(__file__, encoding="utf-8").read()
    chk("S10's claim carries the owner's verdict word, MECHANISM_VERDICT[0], "
        "interpolated and not typed (the source is read: no literal '\"REFUSED, "
        "gap None' beside the asked status)",
        (MECHANISM_VERDICT[0] + ", gap None, reading by reading" in _s10_claim,
         "MECHANISM_VERDICT[0]\n     + \", gap None" in _src,
         '"REFUSED, gap' + ' None, reading' in _src),
        (True, True, False))
    _hd = " ".join(higgs.__doc__.split())
    _pu = ("IT IS UNIFORM WHERE NOTHING SOURCES IT (P-UNIFORM, a named premise: "
           "massform.P_UNIFORM_STATUS)")
    chk("higgs.py's caveat (b) names P-UNIFORM as the premise it is here "
        "(P_UNIFORM_STATUS asked)", (_pu in _hd, P_UNIFORM_STATUS), (True, "PREMISE"))
    chk("CONTROL higgs.py's caveat (b) as it stood, naming no premise, is caught",
        _pu in _hd.replace(" (P-UNIFORM, a named premise: massform.P_UNIFORM_STATUS)",
                           ""), False)
    chk("CONTROL were P-UNIFORM false, it would discriminate",
        derive_consideration(True, discriminates=True), "TRUE")
    chk("D15 asked of excite", excite.TAIL_RATE_IS_MASS, True)
    chk("D16 asked of excite", excite.DISPLACEMENT_IS_ULTRALOCAL, True)
    chk("D19 asked of excite", excite.FLAT_DIRECTIONS_ARE_INERT, True)
    chk("higgs.py's withdrawn 'cannot be switched on' is not restated (F3, asked)",
        higgs.CANNOT_BE_SWITCHED_ON_IN_ONE_PLACE, False)
    chk("D18 asked of excite, a THEOREM",
        excite.ELECTRON_MASS_IS_A_RULER.startswith("THEOREM"), True)
    chk("  and the docstring's D18 sentence carries D18's hypotheses verbatim",
        _norm(excite.ELECTRON_MASS_IS_A_RULER) in _norm(__doc__), True)
    chkrel("lambda_h at READ m_h (excite / higgs fixture 1.576976e-18 m)",
           excite.LAMBDA_H_READ_M, 1.576976e-18, 1e-6)
    chk("D20 source polynomial IS 4 eps(2-eps)(1-eps)^2, coefficient by coefficient",
        source_factorisation_holds(), True)
    chk("  sign by interval: -, +, +, - (roots 0, 1, 1, 2)",
        [s for _iv, s, _a in source_sign_table()], [-1, 1, 1, -1])
    chk("  |phi| > v on exactly the negative intervals (eps < 0, eps > 2)",
        [a for _iv, _s, a in source_sign_table()], [True, False, False, True])
    chk("  so a positive source can only LOWER |phi| (covers |phi| > v)",
        SOURCE_CAN_RAISE_VEV, False)
    chk("  and a positive source can hold some eps: the field CAN be excited",
        FIELD_CAN_BE_EXCITED, True)
    chk("CONTROL a sign-flipped polynomial would raise |phi| (the test can fire)",
        any(-s > 0 and a for _iv, s, a in source_sign_table()), True)
    chkrel("D20 source/field x eps -> 2 at eps = 1e-9",
           float(excite.holding_ratio(Fraction(1, 10 ** 9)) * Fraction(1, 10 ** 9)), 2.0, 1e-8)
    chk("C1 FIELD_SWITCHED_ON_BY_ARRIVAL", FIELD_SWITCHED_ON_BY_ARRIVAL, False)
    chk("CONTROL C1 flips if no massive e, u, d were present (consideration false)",
        field_switched_on_by_arrival(massive_matter_present=False), True)
    chk("CONTROL C1 flips if P-UNIFORM failed", field_switched_on_by_arrival(vev_uniform=False),
        True)
    chk("CONTROL C1 flips if D16 failed (a sourceless change)",
        field_switched_on_by_arrival(d16=False), True)
    chk("Higgs quantum lifetime, one significant figure (excite refusal 6)",
        excite.one_sig(excite.QUANTUM_LIFETIME_S), "2e-22")

    # ------------------------------------------------------------ M65-2
    chk("payload is stock.py's own default, asked", PAYLOAD_KG, 70.0)
    chk("Z READ from AME2020 via gravity: O 8, Zn 30", (Z_OF["O"], Z_OF["Zn"]), (8, 30))
    chkrel("listed fraction 0.9999231 (H-LIST)", COUNTS["listed"], 0.9999230998799999, 1e-12)
    chk("N_p = N_e: neutral atoms", COUNTS["N_p"], COUNTS["N_e"])
    chkrel("B - L = N_n", COUNTS["B_minus_L"], COUNTS["N_n"], 0)
    ratio = COUNTS["B"] / warpfolder.baryons_in(PAYLOAD_KG)
    chk("B against warpfolder's M/m_p lies within 1 %", 1.0 < ratio < 1.01, True)
    pm = payload_masses()
    chkrel("the bookkeeping closes exactly on the listed payload",
           pm["nucleon rest"] + pm["electron rest"] - pm["binding (closure)"],
           pm["listed payload"], 1e-12)
    chk("binding is positive and under 1 % (nuclear, residual strong)",
        0 < pm["binding (closure)"] / PAYLOAD_KG < 0.01, True)
    vp, vn = valence_fractions()
    chkrel("naive valence proton (2x2.16 + 4.7)/938.272089", vp,
           (2 * 2.16 + 4.7) / 938.272089, 1e-12)
    chkrel("naive valence neutron (2.16 + 2x4.7)/939.565422", vn,
           (2.16 + 2 * 4.7) / 939.565422, 1e-12)
    chk("six-quark sum, FLAG 2+1+1 = 0.3066 (READ finding's recomputation)",
        round(float(coupling_sum(Fraction(F_LIGHT["FLAG 2+1+1"]))), 4), 0.3066)
    chk("six-quark sum, FLAG 2+1 = 0.2944", round(float(coupling_sum(Fraction(F_LIGHT["FLAG 2+1"]))), 4), 0.2944)
    chk("f_l FLAG 2+1+1 = 10.9 % (101.9/938.92, READ dispute text)",
        round(100 * F_LIGHT["FLAG 2+1+1"], 1), 10.9)
    chk("3 x (2/27)(1-f) + f == 2/9 + (7/9) f, exact, 200 rationals",
        all(svz_heavy_sum(Fraction(k, 199)) + Fraction(k, 199)
            == coupling_sum(Fraction(k, 199)) for k in range(200)), True)
    chk("  and 2/9 + 7/9 x 1 = 1: the sum is 1 when f_l = 1", coupling_sum(Fraction(1)), 1)
    chk("the 2+1+1 recomputation lies within 1 sigma of Hoferichter's 0.305(9)",
        abs(float(coupling_sum(Fraction(F_LIGHT["FLAG 2+1+1"]))) - 0.305) < 0.009, True)
    chk("both FLAG sigma_piN averages carry the same status, READ",
        (SOURCES["FLAG-447"][0], SOURCES["FLAG-448"][0],
         SIGMA_MEASURES["FLAG 2+1+1"][2], SIGMA_MEASURES["FLAG 2+1"][2]),
        ("READ", "READ", "READ", "READ"))
    chk("  and the 2.7 sigma tension is held and quoted",
        "2.7 sigma difference" in SOURCES["FLAG-tension"][2], True)
    chk("Ji Table I, READ: 160 and 110 MeV of the nucleon",
        (JI_QUARK_MASS_MEV["m_s -> 0"], JI_QUARK_MASS_MEV["m_s -> infinity"]), (160.0, 110.0))
    chk("  as fractions 17.0 % and 11.7 %",
        (round(100 * JI_FRACTION["m_s -> 0"], 1), round(100 * JI_FRACTION["m_s -> infinity"], 1)),
        (17.0, 11.7))
    rows = share_rows()
    chk("every share row inherits the counts' NAMED-NOT-READ",
        all(r[4] == SHARE_INHERITS for r in rows), True)
    chk("  and SHARE_INHERITS says so: NAMED-NOT-READ, gravity.U_KG, stock.ATOMIC_MASS",
        [w for w in ("NAMED-NOT-READ", "gravity.U_KG", "stock.ATOMIC_MASS")
         if w not in SHARE_INHERITS], [])
    _buf = io.StringIO()
    with contextlib.redirect_stdout(_buf):
        report()
    chk("  and the report prints it in full",
        "every row inherits NAMED-NOT-READ (u = gravity.U_KG, stock.ATOMIC_MASS)"
        in _buf.getvalue(), True)
    chk("the heavy-quark rows (couplings, sigma_c) are labelled CONTESTED as mass",
        all(r[1] == "CONTESTED as mass" for r in rows
            if "coupling" in r[0] or "sigma_c" in r[0]), True)
    chk("no row is a sum across measures (one electron row, the rest nucleon)",
        [r[0] for r in rows].count("electrons (all Higgs-given, H-TREE)"), 1)
    chk("electron share is 3.01e-4", round(rows[0][2], 6), 0.000301)
    chk("the largest READ central reading is Ji's m_s -> 0 row",
        max((r for r in rows[1:] if not r[1].startswith("CONTESTED")),
            key=lambda r: r[2])[0], "nucleons: Ji quark mass term, m_s -> 0")
    chk("largest READ-only central reading is under one half", HIGGS_SHARE_LARGEST_READ < 0.5, True)
    chk("  and so is the margin illustration (FLAG +3 sigma; Ji +10 +50 MeV)",
        HIGGS_SHARE_READ_MARGIN < 0.5, True)
    chk("  Ji's two-estimate difference is computed from the READ rows: 50 MeV",
        JI_ESTIMATE_DIFFERENCE_MEV, 50.0)
    chk("  and his 'largest uncertainty' sentence is held (p.6)",
        _in("Ji-table", "The largest uncertainty is from the matrix element <P|m_s ss|P>, "
                        "which could be larger than the difference of the two "
                        "estimates shown"), True)
    chk("  the margin figure is the Ji m_s -> 0 row + 10 + 50 MeV",
        round(HIGGS_SHARE_READ_MARGIN, 6),
        round(rows[0][2] + (160.0 + 10.0 + 50.0) / M_N_MEV
              * payload_masses()["nucleon rest"] / PAYLOAD_KG, 6))
    chk("  and the docstring calls it an illustration, not a bound, with 3 sigma "
        "the file's choice",
        ("AN ILLUSTRATION OF MARGIN, not a bound" in _norm(__doc__),
         "3 sigma is this file's choice" in _norm(__doc__)), (True, True))
    chk("largest central reading of all is under one half", HIGGS_SHARE_LARGEST_ALL < 0.5, True)
    chk("C2 HIGGS_SUPPLIES_MOST_ATOMIC_MASS", HIGGS_SUPPLIES_MOST_ATOMIC_MASS, False)
    chk("C2 does NOT rest on a CONTESTED figure alone", C2_CONTESTED_ONLY, False)
    fake = [r if "FLAG 2+1+1" not in r[0] or "sigma terms" not in r[0]
            else (r[0], r[1], 0.6, r[3], r[4]) for r in rows]
    chk("CONTROL a READ sigma-term row at 0.6 would lift the reading above 1/2",
        largest_central_reading(fake) >= 0.5, True)

    # ------------------------------------------------------------ M65-3
    chk("T_00 from higgs.T_scalar = phi_t^2/2 + |grad phi|^2/2 + V, exact grid",
        T00_DECOMPOSES, True)
    chk("CONTROL the grid test fires on a T_00 missing the gradient term",
        t00_decomposes(tscalar=lambda d, V: [[d[0] ** 2 / 2 + V]]), False)
    _g = inspect.signature(t00_decomposes).parameters["grid"].default
    chk("the T_00 grid has at least 3 distinct points per axis (5 as claimed)",
        (len(set(_g)) >= T00_GRID_MIN_POINTS, len(set(_g))), (True, 5))
    try:
        t00_decomposes(grid=(0, 1))
        _refused = False
    except ValueError:
        _refused = True
    chk("CONTROL a 2-point grid (cannot settle degree 2) is refused", _refused, True)
    chk("H-LINEAR is named in section 6, in C2's status and in S10",
        ("H-LINEAR" in _doc_section(6),
         "H-LINEAR" in [c for c in COUNTS_ON_THE_MECHANISM if c[0] == "C2"][0][3],
         "H-LINEAR" in [r for r in PROPOSED_ROWS if r[0] == "S10"][0][2]), (True, True, True))
    chk("H-TREE-V and D20'S MODEL, asked by specthm's SR5, are named in section 6; "
        "C4's status rests on H-TREE-V",
        ("H-TREE-V" in _doc_section(6), "D20'S MODEL" in _doc_section(6),
         "H-TREE-V" in [c for c in COUNTS_ON_THE_MECHANISM if c[0] == "C4"][0][3],
         H_TREE_V_STATUS.startswith("NAMED HYPOTHESIS"),
         D20_MODEL_STATUS.startswith("NAMED MODEL")), (True,) * 5)
    chk("DISPLACEMENT and QUANTA print as refused as NET formation, remainder priced",
        [reading_label(r) for r in ("DISPLACEMENT", "QUANTA")],
        ["REFUSED as net formation; remainder the pair route, PRICED"] * 2)
    REMAINDER_FORMS_MASS["DISPLACEMENT"] = False
    try:
        bare = reading_label("DISPLACEMENT")
    finally:
        REMAINDER_FORMS_MASS["DISPLACEMENT"] = PAIR_ROUTE_PRICED
    chk("  and the mechanism line names them; a control without a priced remainder "
        "prints bare REFUSED", ("as NET formation only" in mechanism_label(), bare),
        (True, "REFUSED"))
    chk("Ji's two-estimate difference is DERIVED from the READ rows (not typed)",
        JI_ESTIMATE_DIFFERENCE_MEV == (JI_QUARK_MASS_MEV["m_s -> 0"]
                                       - JI_QUARK_MASS_MEV["m_s -> infinity"])
        and bool(re.search(r"(?m)^JI_ESTIMATE_DIFFERENCE_MEV = \(JI_QUARK_MASS_MEV",
                           open(__file__, encoding="utf-8").read())), True)
    chk("PAIR_ROUTE_PRICED is DERIVED by pair_route_priced() (not typed)",
        PAIR_ROUTE_PRICED == pair_route_priced()
        and bool(re.search(r"(?m)^PAIR_ROUTE_PRICED = pair_route_priced\(\)",
                           open(__file__, encoding="utf-8").read())), True)
    chk("the dissent's own admission is held in TW-2017, and S11 states the caveats "
        "on both sides",
        ("both estimates involve assumptions" in SOURCES["TW-2017"][2],
         'Funakubo et al. argue "in the leading order of the WKB approximation"'
         in [r for r in PROPOSED_ROWS if r[0] == "S11"][0][5],
         "whose results rest on unproven" in [r for r in PROPOSED_ROWS if r[0] == "S11"][0][5]),
        (True, True, False))
    chk("H-REAL is named in section 6, in C4's status and in D29",
        ("H-REAL" in _doc_section(6),
         "H-REAL" in [c for c in COUNTS_ON_THE_MECHANISM if c[0] == "C4"][0][3],
         "H-REAL" in [r for r in PROPOSED_ROWS if r[0] == "D29"][0][2]), (True, True, True))
    chk("the decay case is labelled an INFERENCE from READ text (C4 status, D29)",
        ("inference from READ text" in [c for c in COUNTS_ON_THE_MECHANISM
                                        if c[0] == "C4"][0][3],
         "INFERENCE from READ text" in [r for r in PROPOSED_ROWS if r[0] == "D29"][0][2]),
        (True, True))
    chk("metastability is stated at the central measured masses; Degrassi's "
        "condition kept",
        ("at the central measured masses" in _norm(__doc__),
         "for M_h < 126 GeV" in _norm(__doc__), _in("DG-2012", "for M_h < 126 GeV")),
        (True, True, True))
    chk("H-TREE-V says only that v stays a local minimum (no 'whole of what changes')",
        ("v stays a local minimum" in _norm(_doc_section(6)),
         "the whole of what changes" in _norm(__doc__)), (True, False))
    chk("M's sentence is never said to NAME the source",
        [p_ for p_ in ("source M names", "M'S SENTENCE NAMES", "M's sentence names the")
         if p_ in __doc__ or p_ in scan_text()], [])
    chk("V(phi) - V(v) IS (eps(2-eps))^2 in rho_EW (asked of excite)",
        FIELD_ENERGY_IS_A_SQUARE, True)
    chk("  zero exactly at eps = 0 and 2 (|phi| = v), positive elsewhere sampled",
        ([excite.holding_terms(Fraction(e))[1] == 0 for e in (0, 2)],
         all(excite.holding_terms(Fraction(e, 7))[1] > 0 for e in (-7, -1, 3, 7, 13, 20))),
        ([True, True], True))
    chk("so the field releases no energy about v", HIGGS_FIELD_RELEASES_ENERGY_ABOUT_V, False)
    chk("metastability: preferred, not established, top-mass dependent (READ)",
        (METASTABILITY_PREFERRED, VACUUM_FATE_ESTABLISHED, METASTABILITY_TURNS_ON_TOP_MASS),
        (True, False, True))
    chk("vacuum decay: different masses inside, destroys what it meets (READ)",
        (DECAY_CHANGES_PARTICLE_MASSES, DECAY_DESTROYS_WHAT_IT_MEETS), (True, True))
    chk("C4 HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY", HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY, False)
    chk("C4 is the same whether the vacuum is stable or metastable",
        (field_supplies_mass_energy(False), field_supplies_mass_energy(True)), (False, False))
    chk("C4 IS the combination of the two cases",
        HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY,
        field_supplies_mass_energy(True) or field_supplies_mass_energy(False))
    chk("  and is assigned from c4_combined() in this source",
        bool(re.search(r"^HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY = c4_combined\(\)$",
                       inspect.getsource(sys.modules[__name__]), re.M)), True)
    chk("CONTROL the combination flips if decay formed atomic mass (metastable case "
        "reaches it)", c4_combined(decay_forms=True), True)
    chk("CONTROL were decay to form atomic mass, C4 would flip in the metastable case only",
        (field_supplies_mass_energy(False, decay_forms=True),
         field_supplies_mass_energy(True, decay_forms=True)), (False, True))
    E = rest_energy_j()
    chkrel("Mc^2 at 70 kg (warpfolder.rest_energy_j)", E, 70.0 * 299792458.0 ** 2, 1e-15)
    chk("T_CMB asked of permute", T_CMB, 2.7255)
    chkrel("Landauer at 310 K = 2.967e-21 J (READ finding's arithmetic)",
           nopath.landauer_energy(1.0, 310.0), 2.967e-21, 1e-3)
    chkrel("  = 0.01852 eV", nopath.landauer_energy(1.0, 310.0) / 1.602176634e-19, 0.01852, 1e-3)
    chkrel("Bekenstein 70 kg, R = 1 m = 1.80e45 bits (READ finding)",
           bekenstein_bits(), 1.80e45, 3e-3)
    chkrel("Bekenstein 70 kg, R = 0.875 m = 1.58e45 bits", bekenstein_bits(R=0.875),
           1.58e45, 3e-3)
    chkrel("the two counts' ratio equals the closed form with no M",
           bekenstein_bits() / landauer_bits(), bek_over_landauer_closed(), 1e-12)
    chkrel("  and is the same at 1 kg and at 1e6 kg",
           bekenstein_bits(rest_energy_j(1.0)) / landauer_bits(rest_energy_j(1.0)),
           bekenstein_bits(rest_energy_j(1e6)) / landauer_bits(rest_energy_j(1e6)), 1e-12)
    chkrel("break-even radius makes the ratio exactly 1",
           bek_over_landauer_closed(R=break_even_radius_m()), 1.0, 1e-12)
    chk("N-INFO is a note: it names no count and no verdict rests on it",
        (any("INFO" in c[1] for c in COUNTS_ON_THE_MECHANISM), "NO VERDICT" in N_INFO),
        (False, True))
    chk("the human-information figures are NOT-FOUND and unused",
        (SOURCES["Braunstein"][0], SOURCES["Leicester"][0]), ("NOT-FOUND", "NOT-FOUND"))

    # ------------------------------------------------------------ M65-4
    chk("every Yukawa term carries (B, L) = (0, 0)",
        all(term_charge(t) == (0, 0) for t in YUKAWA_TERMS.values()), True)
    chk("C3 HIGGS_COUPLING_CARRIES_B_OR_L", HIGGS_COUPLING_CARRIES_B_OR_L, False)
    chk("the anomaly vertex carries Delta B = Delta L = N_F (READ rule)",
        THOOFT_DELTA_B_L, (Fraction(N_F), N_F))
    chk("CONTROL a lone quark field carries B = 1/3",
        term_charge((("Q", +1), ("H", +1))), (Fraction(1, 3), 0))
    chk("mu_min is 56Fe (AME2020, measured)", (MU_MIN[1], MU_MIN[2]), ("Fe", 56))
    chk("mu_min lies below m_p (bound nucleons are lighter)", MU_MIN[0] < MASS_MEV["p"], True)
    chk("gravitational binding order at 1 m is below 1e-20 (H-AME)",
        gravitational_binding_order() < 1e-20, True)
    fl = pair_floor_j() / E
    chk("the pair floor lies between 1.99 and 2 Mc^2", 1.99 < fl < 2.0, True)
    aw, g = alpha_w()
    chkrel("alpha_W = g^2/4pi from READ m_W and higgs.vev()", aw,
           (2 * 80.362 / vev_gev()) ** 2 / (4 * math.pi), 1e-12)
    chkrel("the two exponent forms agree (alpha_W = g^2/4pi)",
           log10_suppression(), log10_suppression_g(), 1e-12)
    chkrel("CONTROL m_W x 1.01 moves alpha_W by 1.0201",
           alpha_w(M_W_GEV * 1.01)[0] / aw, 1.0201, 1e-12)
    chk("Tye-Wong: alpha_W = 1/29.7 gives 10^-162.09",
        round(log10_suppression(1 / 29.7), 2), -162.09)
    chk("  and 1/30 gives 10^-163.73",
        round(log10_suppression(1 / 30.0), 2), -163.73)
    chk("  so the p.2 pairing (printed 10^-162) is 1.73 decades off",
        round(abs(log10_suppression(1 / TW_ALPHA_INV[1]) - TW_PRINTED_LOG10), 2), 1.73)
    chk("RS96 eq. (2.8): 1/29 gives 10^-158.27, printed 10^-170",
        (round(log10_suppression(1 / RS96_ALPHA_INV), 2), RS96_PRINTED_LOG10),
        (-158.27, -170.0))
    chk("Tye-Wong eq. (1.2): 4.75 x 1.91 = 9.07, not 9.11",
        round(TW_PREFACTOR_TEV * sum(TW_B_TERMS), 2), 9.07)
    chk("  the prefactor is rounded: 9.11/1.91 = 4.770",
        round(E_SPH_TEV["Tye-Wong, pure SU(2)"] / sum(TW_B_TERMS), 3), 4.770)
    chk("implied B = 1.91 lies inside KM's range",
        B_KM_RANGE[0] < sum(TW_B_TERMS) < B_KM_RANGE[1], True)
    chk("FFS: pi x 9080/80.4 gives 10^-154.1 (printed 10^-155)",
        round(-math.pi * 9080 / 80.4 / math.log(10), 1), -154.1)
    chk("FFS: 80 log10(1/(4 pi)^2) = -175.9", round(80 * math.log10(1 / (4 * math.pi) ** 2), 1), -175.9)
    chk("the symmetric-phase figure used is the READ 8.0e-7", RATE_SYMM_READ, 8.0e-7)
    chkrel("  18 alpha_W^5 cross-checks it within its own 1.3e-7",
           symmetric_rate_crosscheck(), RATE_SYMM_READ, 1.3e-7 / 8.0e-7)
    chk("our alpha_W lies inside [1/30, 1/29] -- the sources' range",
        1 / 30 < aw < 1 / 29, True)
    chkrel("E_sph formula x implied B lies within 1 % of the READ 9.08",
           esph_formula_tev(sum(TW_B_TERMS)), 9.08, 1e-2)
    chk("transitions = ceil(B/3)", transitions_needed(), math.ceil(COUNTS["B"] / 3))
    chkrel("extra leptons = N_n (B - L conservation)", extra_leptons(), COUNTS["N_n"], 1e-12)
    chk("H-FLAV sub-count is positive (2 N_p > N_n)", electron_family_shortfall() > 0, True)
    chk("above T_c: heating restores the symmetry (asked of warpfolder)",
        warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY, True)
    chk("the vev above T_c is READ as 'approximately zero'",
        VEV_ABOVE_TC_IS_APPROXIMATELY_ZERO, True)
    chk("transitions run below T_c where the vev is finite (T* < T_c, READ)",
        SPHALERONS_RUN_WHERE_VEV_IS_FINITE, True)
    chk("broken-phase fit at T* = 0.83 x 131.7 - 147.7 = -38.389",
        round(broken_phase_ln_rate(T_FREEZE_GEV), 3), -38.389)
    try:
        broken_phase_ln_rate(120.0)
        refused = False
    except ValueError:
        refused = True
    chk("CONTROL the fit refuses a temperature outside its stated range", refused, True)
    try:
        broken_phase_ln_rate(159.3)
        refused_hi = False
    except ValueError:
        refused_hi = True
    chk("CONTROL the fit refuses 159.3 GeV: bounded by its own T_c, 159 GeV",
        (refused_hi, BROKEN_FIT_HIGH_GEV), (True, 159.0))
    chk("  and 159 GeV lies outside the measured 140-155 GeV (held, p.3)",
        (not (140.0 <= BROKEN_FIT_HIGH_GEV <= 155.0),
         _in("DRT-Tc", "In the interval 140 <~ T <~ 155 GeV")), (True, True))
    chk("collider rate CONTESTED", COLLIDER_RATE_STATUS, "CONTESTED")
    chk("the Tye-Wong claim is held as CONTESTED", SOURCES["TW-claim"][0], "CONTESTED")
    chk("the anomaly route is priced (every figure finite)", ANOMALY_ROUTE_PRICED, True)
    chk("the pair route is priced, not refused; the Higgs is not its source",
        (PAIR_ROUTE_PRICED, PAIR_ROUTE_REFUSED, HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY),
        (True, False, False))
    chk("  and the priced routes are in what survives (pair, anomaly, held-seat)",
        [n for n, _t in SURVIVES], ["reconstruction from destination stock",
                                    "the pair route", "the anomaly route",
                                    "the held-seat release route"])
    chk("the collider balance is held as the sources give it (statuses)",
        [(k, SOURCES[k][0]) for k in ("BLRRT", "BLRRT-PLB", "BLRRT-conj", "KM-2020",
                                      "TW-claim", "TW-2017", "FFS-rebut", "CMS")],
        [("BLRRT", "READ"), ("BLRRT-PLB", "READ"), ("BLRRT-conj", "READ"),
         ("KM-2020", "READ"), ("TW-claim", "CONTESTED"), ("TW-2017", "CONTESTED"),
         ("FFS-rebut", "READ"), ("CMS", "READ")])
    chk("  the rebuttal is not conceded: TW-2017 cites 1612.05431 and keeps the claim",
        (_in("TW-2017", "arXiv:1612.05431"),
         _in("TW-2017", "we claim that multi-sphaleron processes can drastically "
                        "change the picture")), (True, True))
    chk("  the prevalent results are held as resting on conjecture, not theorem",
        (_in("BLRRT-conj", "although not proven rigorously"),
         _in("KM-2020", "there is no rigorous proof of exponentiation"),
         "not theorems" in _norm(__doc__)), (True, True, True))
    _coll = _norm(__doc__)[_norm(__doc__).index("AT COLLIDER ENERGIES"):]
    _coll = _coll[:_coll.index("NOT RESOLVED HERE")]
    chk("  instanton and sphaleron kept apart: the collider paragraph disowns both "
        "the T = 0 factor and the thermal rate",
        "not the instanton's T = 0 factor and not the thermal sphaleron rate" in _coll, True)
    chk("  and S11 and SURVIVES name INSTANTON (T = 0) and SPHALERON separately",
        [("INSTANTON" in t and "SPHALERON" in t)
         for t in ([r[2] for r in PROPOSED_ROWS if r[0] == "S11"]
                   + [t for n, t in SURVIVES if n == "the anomaly route"])], [True, True])
    chk("the Bekenstein bound is held with Hayden-Wang's caution, not as a capacity",
        (_in("HW-folk", "this interpretation remains folklore rather than established fact"),
         "does NOT read the figure as the most information such a body can hold"
         in _norm(__doc__)), (True, True))

    # ------------------------------------------------------------ M65-5
    vals = mechanism_values()
    cont = mechanism_contested()
    chk("the counts' values", vals,
        {"C1": False, "C2": False, "C3": False, "C4": False, "C5": False})
    chk("no count on the mechanism is contested-only", [c for c, v in cont.items() if v], [])
    ALL_READINGS = ["CREATION", "DISPLACEMENT", "QUANTA", "STOCK", "SWITCH-ON", "TEMPLATE"]
    chk("READING VERDICTS",
        {r: v for r, v in READING_VERDICTS.items()},
        {"SWITCH-ON": ("REFUSED", ["C1"]), "DISPLACEMENT": ("REFUSED", ["C2", "C3"]),
         "QUANTA": ("REFUSED", ["C3"]), "CREATION": ("REFUSED", ["C3", "C4"]),
         "STOCK": ("REFUSED", ["C5"]), "TEMPLATE": ("REFUSED", ["C1"])})
    chk("MECHANISM VERDICT", MECHANISM_VERDICT, ("REFUSED", ALL_READINGS))
    chk("every count on every reading carries a stated reason that agrees with the "
        "listing", reading_reason_table_complete(), [])
    chk("  C2 is listed on DISPLACEMENT only, and says why everywhere else",
        [r for r in ALL_READINGS if READING_REASONS[(r, "C2")][0]], ["DISPLACEMENT"])
    chk("  C2's reason is the first-order one, H-LINEAR carried",
        (_C2_YES, _C2_YES in READING_REASONS[("DISPLACEMENT", "C2")][1]),
        ("at first order, with the QCD scale held fixed (H-LINEAR), only the "
         "quark-mass part moves", True))
    chk("  and C2 is off SWITCH-ON, STOCK and TEMPLATE because they ask the FINITE "
        "share, OPEN",
        [("finite" in READING_REASONS[(r, "C2")][1] and "OPEN" in READING_REASONS[(r, "C2")][1])
         for r in ("SWITCH-ON", "STOCK", "TEMPLATE")], [True, True, True])
    chk("  C5 (prior mass) is listed on STOCK only, and the table states the argument",
        ([r for r in ALL_READINGS if READING_REASONS[(r, "C5")][0]],
         all(w in READING_REASONS[("STOCK", "C5")][1]
             for w in ("already carry their Higgs-given mass", "NO P-UNIFORM",
                       "REQUIRE phi != 0"))), (["STOCK"], True))
    chk("CONTROL a count listed with no stated reason is caught",
        len(reading_reason_table_complete(reasons={k: v for k, v in READING_REASONS.items()
                                                   if k != ("STOCK", "C5")})) > 0, True)
    chk("CONTROL C2 put back on STOCK without an argument for it is caught",
        len(reading_reason_table_complete(
            readings=tuple((n, w, c + ("C2",)) if n == "STOCK" else (n, w, c)
                           for n, w, c in READINGS))) > 0, True)
    chk("CONTROL C2 listed against CREATION without an argument for it is caught",
        len(reading_reason_table_complete(
            readings=tuple((n, w, c + ("C2",)) if n == "CREATION" else (n, w, c)
                           for n, w, c in READINGS))) > 0, True)
    chk("every reading states its remainder; EXCITATION's is the pair route",
        (sorted(READING_REMAINDERS) == ALL_READINGS,
         all("pair route" in READING_REMAINDERS[r] for r in ("DISPLACEMENT", "QUANTA"))),
        (True, True))
    chk("CONTROL every count reversed -> the mechanism STANDS on every reading",
        derive_mechanism(derive_readings({k: True for k in vals}, cont)),
        ("STANDS ON A READING", ALL_READINGS))
    _refd = {r: "REFUSED" for r in ALL_READINGS}
    chk("CONTROL C5 alone reversed -> the STOCK reading stands, the others refused",
        {r: v[0] for r, v in derive_readings(dict(vals, C5=True), cont).items()},
        dict(_refd, STOCK="STANDS"))
    chk("CONTROL C2 alone reversed -> every reading still refused (DISPLACEMENT on C3)",
        ({r: v[0] for r, v in derive_readings(dict(vals, C2=True), cont).items()},
         derive_readings(dict(vals, C2=True), cont)["DISPLACEMENT"]),
        (_refd, ("REFUSED", ["C3"])))
    chk("CONTROL C3 alone reversed -> the QUANTA reading stands, the others refused",
        {r: v[0] for r, v in derive_readings(dict(vals, C3=True), cont).items()},
        dict(_refd, QUANTA="STANDS"))
    chk("CONTROL C1 alone reversed -> SWITCH-ON and TEMPLATE stand (both rest on "
        "P-UNIFORM), the others refused",
        {r: v[0] for r, v in derive_readings(dict(vals, C1=True), cont).items()},
        dict(_refd, **{"SWITCH-ON": "STANDS", "TEMPLATE": "STANDS"}))
    chk("CONTROL C5 contested-only -> STOCK is OPEN, not REFUSED",
        derive_readings(vals, dict(cont, C5=True))["STOCK"], ("OPEN", ["C5"]))
    chk("CONTROL C2 contested-only -> DISPLACEMENT is refused on C3 alone",
        derive_readings(vals, dict(cont, C2=True))["DISPLACEMENT"], ("REFUSED", ["C3"]))
    # ---- the prior-mass argument, and its controls
    chk("C5 TRIGGER_GIVES_THE_ELEMENTS_THEIR_MASS (prior mass)",
        TRIGGER_GIVES_THE_ELEMENTS_THEIR_MASS, False)
    chk("  and is assigned from its function in this source",
        bool(re.search(r"^TRIGGER_GIVES_THE_ELEMENTS_THEIR_MASS = "
                       r"trigger_gives_the_elements_their_mass\(\)$", src, re.M)), True)
    chk("  its READ input, fermion masses proportional to phi, is derived from MRM-phi",
        MASS_PROPORTIONAL_TO_PHI, True)
    _massless = consideration_holds(dict(MASS_MEV, e=0.0, u=0.0, d=0.0))
    chk("CONTROL if e, u, d were massless, C5 flips (recomputed from its function)",
        trigger_gives_the_elements_their_mass(elements_massive=_massless), True)
    _mw = dict(vals, C5=trigger_gives_the_elements_their_mass(elements_massive=_massless),
               C1=field_switched_on_by_arrival(massive_matter_present=_massless))
    chk("  and C1 flips with it, recomputed consistently: the massless world, where "
        "STOCK, TEMPLATE and SWITCH-ON all stand",
        ({k: _mw[k] for k in ("C1", "C5")},
         {r: v[0] for r, v in derive_readings(_mw, cont).items()}),
        ({"C1": True, "C5": True},
         dict(_refd, **{"STOCK": "STANDS", "TEMPLATE": "STANDS", "SWITCH-ON": "STANDS"})))
    chk("CONTROL the template branch: C5 True with C1 held False (H-PRESENT failing) "
        "-> TEMPLATE still REFUSED on C1",
        derive_readings(dict(vals, C5=True, C1=False), cont)["TEMPLATE"],
        ("REFUSED", ["C1"]))
    chk("CONTROL C5 flips if fermion masses were not proportional to phi",
        trigger_gives_the_elements_their_mass(mass_prop_phi=False), True)
    chk("C5 needs NO P-UNIFORM: its code reads no name of the premise",
        reads_p_uniform(trigger_gives_the_elements_their_mass), [])
    chk("  whereas C1's does (the scan can see the premise)",
        reads_p_uniform(field_switched_on_by_arrival) != [], True)
    chk("CONTROL a C5 that consulted P-UNIFORM would be caught",
        reads_p_uniform(lambda massive=True: massive and VEV_IS_UNIFORM), ["VEV_IS_UNIFORM"])
    chk("  and C5 is unmoved where C1 flips on P-UNIFORM failing",
        (field_switched_on_by_arrival(vev_uniform=False),
         trigger_gives_the_elements_their_mass()), (True, False))
    chk("MASS_PROPORTIONAL_TO_PHI is DERIVED from the held MRM-phi text (not typed)",
        bool(re.search(r"(?m)^MASS_PROPORTIONAL_TO_PHI = \(_norm\(",
                       open(__file__, encoding="utf-8").read())), True)
    chk("S10's status equals MECHANISM_VERDICT[0], bound in the row's source "
        "(the source regex, not an identity: CPython interns the literal)",
        ([r for r in PROPOSED_ROWS if r[0] == "S10"][0][3] == MECHANISM_VERDICT[0],
         "S10 status" not in underived(src)), (True, True))
    chk("the STOCK/TEMPLATE case split: C5 carries STOCK without P-UNIFORM, C1 carries "
        "TEMPLATE on it", (READING_VERDICTS["STOCK"][1], READING_VERDICTS["TEMPLATE"][1]),
        (["C5"], ["C1"]))
    chk("H-PRESENT is a case definition in its status and in section 6; only the "
        "masses carry READ",
        (H_PRESENT_STATUS.startswith("NAMED CASE DEFINITION"),
         "H-PRESENT A CASE DEFINITION, not a finding" in _norm(_doc_section(6)),
         "(the masses READ)" in _norm(_doc_section(6))), (True, True, True))
    chk("H-PRESENT is named in section 6 and in C5's status",
        ("H-PRESENT" in _doc_section(6),
         "H-PRESENT" in [c for c in COUNTS_ON_THE_MECHANISM if c[0] == "C5"][0][3]),
        (True, True))
    # ---- the finite share, OPEN
    chk("the finite Higgs share is OPEN, its comparison with one half undecided (None)",
        (FINITE_HIGGS_SHARE_STATUS, FINITE_HIGGS_SHARE_EXCEEDS_HALF), ("OPEN", None))
    chk("  no count reads it",
        [c[1] for c in COUNTS_ON_THE_MECHANISM if "FINITE" in c[1]], [])
    chk("  it is in S10's claim and movers, in NOT_OPENED and the item S10 (open)",
        ("FINITE Higgs share" in [r for r in PROPOSED_ROWS if r[0] == "S10"][0][2],
         "finite Higgs share" in [r for r in PROPOSED_ROWS if r[0] == "S10"][0][5],
         any("finite Higgs share" in n for n in NOT_OPENED),
         [(r[1], r[3], r[4]) for r in PROPOSED_ROWS if r[0] == "S10 (open)"]),
        (True, True, True, [("SUPPLY", "OPEN", ("massform", "FINITE_HIGGS_SHARE_STATUS"))]))
    # M-D65-2 (ledger.RULED_BY_M): 'Fold into S10 (Recommended)' -- an open item
    # inside S10's note, not a separate row.  The board is asked, at call time.
    _lg = _ledger()
    chk("  on M's ruling M-D65-2 it is in S10's note on the board and is no row "
        "of its own (no O row, no row id beyond S10)",
        ([r for r in _lg.RULED_BY_M if r[0] == "M-D65-2"] != [],
         [r for r in PROPOSED_ROWS if r[0] == "S10 (open)"][0][2]
         in [r for r in _lg.SUPPLY if r[0] == "S10"][0][4],
         [r[0] for r in _lg.OPEN_ROWS + _lg.DEMAND + _lg.SUPPLY
          if "FINITE Higgs share" in " ".join(str(x) for x in r[1:3])]),
        (True, True, []))
    chk("section 2 carries H-LINEAR on every share sentence (no flat claim)",
        flat_share_claims(), [])
    chk("CONTROL a flat 'Nothing near one half.' is caught",
        flat_share_claims(_norm(__doc__).replace("one half AT FIRST ORDER",
                                                 "one half. Really")) != [], True)
    chk("CONTROL a flat 'THIS is the part of the nucleon mass that comes from' is caught",
        flat_share_claims(__doc__ + " THIS is the part of the nucleon mass that comes "
                          "from quark masses") != [], True)
    chk("  and the finite share is said OPEN in sections 0, 2 and 6",
        ["OPEN" in _norm(_doc_section(n)) and "finite" in _norm(_doc_section(n)).lower()
         for n in (0, 2, 6)], [True, True, True])
    for k in sorted(vals):
        only = {j: (j != k) for j in vals}
        chk("CONTROL derive_verdict: only %s failing, contested-only -> OPEN" % k,
            derive_verdict(only, {k: True}), ("OPEN", [k]))
    _c1r = derive_readings(dict(vals, C1=field_switched_on_by_arrival(
        massive_matter_present=False)), cont)
    chk("CONTROL recomputing C1 from its function flips it in both its readings",
        (_c1r["SWITCH-ON"], _c1r["TEMPLATE"]), (("STANDS", []), ("STANDS", [])))
    for sh in (Fraction(-1, 2), Fraction(1, 2)):
        cc = counts(a_shift=sh)
        b = largest_central_reading(share_rows(cc)) >= 0.5
        chk("H-A: at A %+s every boolean stands (C2 %s; floor > 1.9 Mc^2)" % (sh, b),
            (b, pair_floor_j(cc) / E > 1.9, extra_leptons(cc) > 0), (False, True, True))
    chk("what survives: reconstruction from stock", RECONSTRUCTION_SURVIVES, True)
    chk("  transit carries no substance (asked)", transit.CARRIES_SUBSTANCE, False)

    # ------------------------------------------- the misquote check, and its controls
    bad = check_quotes()
    chk("every quotation and pinned numeral has its home; S10 quotes M verbatim", bad, [])
    mutated = dict(SOURCES)
    st, loc, t = mutated["DR-Tc"]
    mutated["DR-Tc"] = (st, loc, t.replace("159.5", "159.9"))
    chk("CONTROL a misquoted T_c is caught", len(check_quotes(sources=mutated)) > 0, True)
    chk("CONTROL a fragment altered in the docstring is caught",
        len(check_quotes(doc=_norm(__doc__).replace("approximately zero", "exactly zero"))) > 0,
        True)
    bad_rows = tuple((r[0], r[1], r[2].replace("it triggers the higgs field", "triggers the "
                                                "Higgs field"), r[3], r[4], r[5])
                     if r[0] == "S10" else r for r in PROPOSED_ROWS)
    chk("CONTROL a paraphrase of M inside S10's quotation marks is caught",
        len(check_quotes(rows=bad_rows)) > 0, True)
    bad_surv = SURVIVES + (("x", 'as the source puts it, "the vev is born at the seat"'),)
    chk("CONTROL an invented quotation in SURVIVES is caught",
        len(check_quotes(survives=bad_surv)) > 0, True)
    chk("pinned values are the ones used",
        (SIGMA_PIN_2P1P1, SIGMA_S_2P1P1, T_C_GEV, E_SPH_TEV[E_SPH_USED], RATE_SYMM_READ),
        (60.9, 41.0, 159.5, 9.08, 8.0e-7))
    chk("every source status is in the vocabulary",
        sorted({s for s, _l, _t in SOURCES.values()}),
        ["CITED", "CONTESTED", "NOT-FOUND", "READ"])

    # ----------------------------------------------- docstring figures, two-sided
    stray, missing = doc_figure_guard()
    chk("every regenerated figure is printed in the docstring", missing, [])
    rowtext = {r[0]: _norm(r[2]) for r in PROPOSED_ROWS}
    chk("every figure a proposed row prints is regenerated",
        [(rid, s_) for rid, s_ in row_figures() if s_ not in rowtext[rid]], [])
    _s11f = [s_ for rid, s_ in row_figures() if rid == "S11"]
    _drift = dict(rowtext)
    _drift["S11"] = rowtext["S11"].replace(_s11f[1], _s11f[1].replace("~", "~1", 1))
    chk("CONTROL a drifted S11 figure (the sphaleron over 3 baryons) is caught",
        (len(_s11f), [(rid, s_) for rid, s_ in row_figures() if s_ not in _drift[rid]]),
        (2, [("S11", _s11f[1])]))
    chk("no docstring numeral is stale or unregenerated (two-sided)", stray, [])
    ndoc = _norm(__doc__)
    first = ndoc.replace("3226 times", "3227 times", 1)
    chk("CONTROL a stale FIRST occurrence (3226 -> 3227) is caught",
        doc_figure_guard(doc=first)[0] != [], True)
    i = ndoc.rfind("1.9975 Mc^2")
    last = ndoc[:i] + "1.9976 Mc^2" + ndoc[i + len("1.9975 Mc^2"):]
    chk("CONTROL a stale LAST occurrence (1.9975 -> 1.9976) is caught",
        doc_figure_guard(doc=last)[0] != [], True)
    chk("CONTROL a stale unlisted-looking figure (2e-22 -> 3e-22 s) is caught",
        doc_figure_guard(doc=ndoc.replace("2e-22 s", "3e-22 s"))[0] != [], True)
    chk("CONTROL a stale exponent (10^-160.95 -> 10^-161.95) is caught",
        doc_figure_guard(doc=ndoc.replace("10^-160.95", "10^-161.95", 1))[0] != [], True)
    chk("CONTROL a stale payload (70 kg -> 7 kg) is caught",
        doc_figure_guard(doc=ndoc.replace("own default of 70 kg", "own default of 7 kg"))
        != ([], []), True)
    chk("CONTROL a stale Tye-Wong gap (1.73 -> 1.6 decades) is caught",
        doc_figure_guard(doc=ndoc.replace("1.73 decades off", "1.6 decades off")) != ([], []),
        True)
    chk("CONTROL a numeral held only in a source's TEXT is no longer allowed "
        "(planted 'at 99.8 %')",
        "99.8" in doc_figure_guard(doc=ndoc + " at 99.8 %")[0], True)
    chk("no DOC_LITERALS entry is a computed result", literals_that_are_results(), [])
    chk("every DOC_LITERALS entry is needed (printed, and allowed no other way)",
        unneeded_literals(), [])
    chk("CONTROL an unneeded literal ('1.6', printed nowhere) is caught",
        unneeded_literals(DOC_LITERALS | {"1.6"}), ["1.6"])
    chk("CONTROL a literal that is a result ('1.73') is caught",
        literals_that_are_results(DOC_LITERALS | {"1.73"}), ["1.73"])

    # ----------------------------------------------- refusals, derived
    chk("refusals enumerated in the docstring match the flags",
        doc_refusal_numbers(), sorted(refusal_flags("").keys()))
    text = scan_text()
    flags = refusal_flags(text)
    chk("every refusal flag, DERIVED, is unset",
        [v[0] for v in flags.values() if v[1]], [])
    chk("CONTROL refusal 5 fires on a planted 'no masses form'",
        refusal_flags(text + " so no masses form.")[5][1], True)
    chk("CONTROL refusal 6 fires on a planted human bit count",
        refusal_flags(text + " a human is 1e32 bits")[6][1], True)
    chk("CONTROL refusal 7 fires on 'the energy of a bit is k_B T ln 2'",
        refusal_flags(text + " the energy of a bit is k_B T ln 2")[7][1], True)
    chk("CONTROL refusal 12 fires on 'four independent counts'",
        refusal_flags(text + " refused on four independent counts")[12][1], True)
    chk("CONTROL refusal 4 fires on a rate per second",
        refusal_flags(text + " 3e-150 transitions per s")[4][1], True)
    chk("CONTROL refusal 3 fires if a reading were refused on a contested count",
        refusal_flags(text, readings={"X": ("REFUSED", ["C2"])},
                      contested={"C2": True})[3][1], True)
    chk("CONTROL refusal 9 fires if the pair route were dropped from what survives",
        refusal_flags(text, survives=tuple(x for x in SURVIVES
                                           if x[0] != "the pair route"))[9][1], True)
    chk("CONTROL refusal 12 fires on 'C2 answers every reading'",
        refusal_flags(text + " C2 answers every reading")[12][1], True)
    chk("CONTROL refusal 12 fires on a reading-reason table with a hole",
        refusal_flags(text, reasons={k: v for k, v in READING_REASONS.items()
                                     if k != ("QUANTA", "C3")})[12][1], True)
    # ---- B: the collider balance, both sides, scanned over docstring, report, rows
    chk("the collider balance is kept on both sides everywhere scanned (refusal 2 scan)",
        one_sided_conjecture_claims(text), [])
    chk("CONTROL refusal 2 fires on a planted 'Funakubo et al. rest on unproven "
        "conjectures'",
        refusal_flags(text + "\n\nFunakubo et al. rest on unproven conjectures.")[2][1], True)
    chk("CONTROL  ... and on the same planted inside S11's own passage",
        bool(one_sided_conjecture_claims(
            [" ".join(str(x) for x in r) for r in PROPOSED_ROWS if r[0] == "S11"][0]
            + "  Funakubo et al. rest on unproven conjectures.")), True)
    chk("CONTROL refusal 2 fires on a lone 'the prevalent results rest on unproven "
        "conjectures, not theorems'",
        refusal_flags(text + "\n\nthe prevalent results rest on unproven conjectures, "
                             "not theorems.")[2][1], True)
    _stripped = one_sided_conjecture_claims(
        re.sub(r"\s+".join(DISSENT_CAVEAT.split()), "XXX", text))
    chk("CONTROL with the dissent's admission struck, the scan catches the docstring's "
        "section 0 and section 4, the report and S11",
        [any(frag in c for _w, c in _stripped) for frag in (
            "resting on conjectures and assumptions they state as",
            "These are results resting on conjectures and assumptions their authors",
            "the prevalent results rest on conjectures and assumptions their authors "
            "state as unproven, not theorems",
            "Bezrukov et al and Khoze-Milne rest on conjectures")], [True] * 4)
    _rep = io.StringIO()
    with contextlib.redirect_stdout(_rep):
        report()
    _rep = _norm(_rep.getvalue())
    _sec4 = _norm(_doc_section(4))
    chk("section 4 and the report each carry TW's p.2 admission and p.3 guesstimate",
        [(DISSENT_CAVEAT in x, "only an order of magnitude guesstimate" in x)
         for x in (_sec4, _rep)], [(True, True), (True, True)])
    chk("'not conceded' cites TW's p.3 reply, held, in section 4 and the report",
        (_in("TW-2017", "However, the above argument is somewhat misleading"),
         "replies to it on p.3" in _sec4 and "somewhat misleading" in _sec4,
         "replies on p.3" in _rep), (True, True, True))
    chk("Funakubo et al.'s WKB order is held (1612.05431 p.4) and quoted, never "
        "a conjecture",
        (_in("FFS-rebut", "in the leading order of the WKB approximation"),
         "in the leading order of the WKB approximation" in _sec4), (True, True))
    chk("report locators print the arXiv id of every collider source",
        [(k, arxiv_id(SOURCES[k][1]) is not None and ("arXiv %s" % arxiv_id(SOURCES[k][1]))
          in _rep) for k in ("BLRRT", "BLRRT-PLB", "BLRRT-conj", "KM-2020", "TW-claim",
                             "TW-2017", "FFS-rebut", "CMS")],
        [(k, True) for k in ("BLRRT", "BLRRT-PLB", "BLRRT-conj", "KM-2020", "TW-claim",
                             "TW-2017", "FFS-rebut", "CMS")])
    chk("  and no locator is truncated to 'hep-ph/03'",
        bool(re.search(r"hep-ph/03(?!\d)", _rep)), False)
    # ---- C: the verdict line qualified, scanned
    chk("no 'REFUSED on every reading' is printed without its NET-formation "
        "qualification", unqualified_refusals(text), [])
    chk("  the section-5 verdict line carries it",
        "THE MECHANISM AS STATED: REFUSED on every reading; on DISPLACEMENT and QUANTA "
        "as NET formation only" in _norm(_doc_section(5)), True)
    chk("CONTROL refusal 9 fires on the old bare 'THE MECHANISM AS STATED: REFUSED on "
        "every reading.'",
        refusal_flags(text + "\n\nTHE MECHANISM AS STATED: REFUSED on every reading.\n")[9][1],
        True)
    chk("CONTROL  ... and on the section-5 line with its qualification struck",
        bool(unqualified_refusals(__doc__.replace(
            "REFUSED on every reading; on DISPLACEMENT and QUANTA\nas NET formation only",
            "REFUSED on every reading.  On DISPLACEMENT and QUANTA\nsomething"))), True)
    # ---- NOTES: survivor (c) matched to section 0; report rows
    chk("survivor (c) says the sphaleron thermally, the collider case CONTESTED "
        "(as section 0)",
        ("the sphaleron thermally and at high energy" in _norm(__doc__),
         "whether two-particle collisions at high energy cross it is CONTESTED"
         in _norm(_doc_section(5))), (False, True))
    chk("report rows read 'REFUSED on <counts> -- <qualification>; remainder ...', "
        "C2 scoped after C3 (R6-E)",
        [reading_row(r) for r in ("DISPLACEMENT", "QUANTA", "TEMPLATE")],
        ["REFUSED on C3 (C2 for a small displacement only) -- as net formation; "
         "remainder the pair route, PRICED",
         "REFUSED on C3 -- as net formation; remainder the pair route, PRICED",
         "REFUSED on C1 -- on P-UNIFORM and H-UNSOURCED-SEAT; remainder the "
         "held-seat release route, PRICED"])
    chk("SWITCH-ON's label and row carry C1's premise, P-UNIFORM (asked of C1's "
        "status), and never read unconditional",
        (reading_label("SWITCH-ON"), reading_row("SWITCH-ON"),
         reading_premises("SWITCH-ON"), reading_premises("TEMPLATE")),
        ("REFUSED on P-UNIFORM (C1 alone)", "REFUSED on C1 -- on P-UNIFORM",
         ["P-UNIFORM"], ["P-UNIFORM", "H-UNSOURCED-SEAT"]))
    chk("CONTROL a C1 status without P-UNIFORM drops the premise from the label "
        "(asked, not typed)",
        (reading_label("SWITCH-ON", c1_status="THEOREM (D15, D16)"),
         reading_label("TEMPLATE", c1_status="THEOREM (D15, D16)")),
        ("REFUSED", "REFUSED on H-UNSOURCED-SEAT; remainder the held-seat release "
         "route, PRICED"))
    chk("  and the report prints exactly those rows",
        all(reading_row(r) in _rep for r in ALL_READINGS), True)
    chk("CONTROL refusal 8 fires on a coupling row relabelled READ",
        refusal_flags(text, rows=[(r[0], "READ", r[2], r[3], r[4]) if "coupling" in r[0]
                                  else r for r in share_rows()])[8][1], True)
    # ---- ROUND 5 (lens 2 on 7e94280): every text fixed is guarded, and each
    # guard has a control that puts the OLD wording back and turns it red.
    _units = guard_units()
    chk("R5 no retired wording anywhere scanned (docstring, report, rows, SURVIVES, "
        "READING_* tables, COUNTS, NOT_OPENED)", stale_wording(_units), [])
    for _id, _pat, _unless, _old in STALE_WORDING:
        chk("CONTROL R5 planted old wording is caught: %s" % _id,
            _id in [i for i, _s in stale_wording(_units + _sentences(_old))], True)
    _locs = guard_locations()
    chk("R5 every required wording is where the fix put it", required_wording(_locs), [])
    for _id, _loc, _phrase, _old in REQUIRED_WORDING:
        _l2 = dict(_locs)
        _l2[_loc] = _l2[_loc].replace(_norm(_phrase), _norm(_old))
        chk("CONTROL R5 old wording put back in place is caught: %s" % _id,
            _id in required_wording(_l2), True)
    chk("R5 the old section-5 prose, planted in place in the docstring, is caught by "
        "both scans",
        (bool(stale_wording(guard_units(doc=__doc__.replace(
            "C1 answers SWITCH-ON and TEMPLATE: each needs the field\noff, or below v",
            "C1 answers SWITCH-ON only: it needs P-UNIFORM.  Each needs the field\noff, "
            "or below v")))),
         "SF1 section 5 prose: C1 answers SWITCH-ON and TEMPLATE" in required_wording(
             guard_locations(doc=__doc__.replace(
                 "C1 answers SWITCH-ON and TEMPLATE: each needs the field\noff",
                 "C1 answers SWITCH-ON only: it needs P-UNIFORM.  Each needs the "
                 "field\noff")))), (True, True))
    chk("SF1 every READINGS name has a section-5 table row with its counts",
        doc_table_mismatch(), [])
    chk("  the table rows parsed", sorted(doc_verdict_table()), sorted(ALL_READINGS))
    _no_tmpl = re.sub(r"\n  TEMPLATE      C1 .*?\n(?=\n)", "\n", __doc__, flags=re.S)
    chk("CONTROL SF1 the section-5 table without its TEMPLATE row is caught",
        ("TEMPLATE" in str(doc_table_mismatch(_no_tmpl)), _no_tmpl != __doc__), (True, True))
    chk("CONTROL SF1 a table row with the wrong counts is caught",
        doc_table_mismatch(__doc__.replace("  TEMPLATE      C1  ", "  TEMPLATE      C5  ")) != [],
        True)
    chk("SF2 the S10 and D27 movers send H-PRESENT failing to TEMPLATE, not STOCK",
        [("the case is TEMPLATE" in _norm(r[5]), "H-TREE or H-PRESENT" in r[5])
         for r in PROPOSED_ROWS if r[0] in ("S10", "D27")], [(True, False), (True, False)])
    chk("R6-A the seat splits three ways: TEMPLATE (r < 1), STOCK (r = 1) and above v "
        "(r > 1) partition the samples, boundaries and interiors", seat_case_gaps(), [])
    chk("  and 'nothing to give' is exactly STOCK or above v (the trigger gives only "
        "on TEMPLATE's interval)", nothing_to_give_mismatch(), [])
    chk("CONTROL R6-A a two-way split (no above-v case) leaves r > 1 uncovered",
        seat_case_gaps(above=lambda r: False), [Fraction(1001, 1000), Fraction(3, 2)])
    chk("CONTROL R6-A 'nothing to give' moved to r > 1 is caught",
        nothing_to_give_mismatch(ntg=lambda r: r > 1), [Fraction(1)])
    chk("  a partial-mass seat (|phi| = v/2) is TEMPLATE", partial_seat_case(), "TEMPLATE")
    chk("CONTROL SF3 the old TEMPLATE (phi = 0 only) leaves the partial-mass seats "
        "uncovered", seat_case_gaps(template=lambda r: r == 0),
        [Fraction(1, 1000), Fraction(1, 2), Fraction(999, 1000)])
    chk("CONTROL SF3  ... and the half-mass seat falls between", partial_seat_case(
        template=lambda r: r == 0), "UNCOVERED")
    chk("SF3 C1's reason on TEMPLATE is the stated one, in the table and in S10",
        (_C1_TEMPLATE in READING_REASONS[("TEMPLATE", "C1")][1],
         _C1_TEMPLATE in [r for r in PROPOSED_ROWS if r[0] == "S10"][0][2]), (True, True))
    chk("SF4 C2's scope is one phrase, carried by the DISPLACEMENT reason and S10",
        (C2_SCOPE, C2_SCOPE in READING_REASONS[("DISPLACEMENT", "C2")][1]),
        ("a SMALL displacement only; a finite one is OPEN, and C3 carries the refusal "
         "regardless", True))
    chk("NOTE flat_share_claims is clean over the docstring and the report",
        flat_share_claims(), [])
    chk("CONTROL NOTE a bare 'The remainder is QCD.' is caught (docstring)",
        flat_share_claims(__doc__ + "\n\nThe remainder is QCD.\n") != [], True)
    chk("CONTROL NOTE the old report label without 'first order' is caught",
        flat_share_claims(rep=_report_text().replace(
            "remainder 1 - f_l, first order (H-LINEAR)",
            "remainder 1 - f_l (heavy-quark part CONTESTED)")) != [], True)
    chk("NOTE the docstring's 'read N ways' matches len(READINGS)",
        reading_count_words(), [("six", len(READINGS))])
    chk("CONTROL NOTE a stale 'read five ways' is caught",
        reading_count_words(__doc__.replace("read six ways", "read five ways"))
        != [("six", len(READINGS))], True)
    chk("CONTROL NOTE refusal 12 fires on 'answers all six readings'",
        refusal_flags(text + " C3 answers all six readings")[12][1], True)
    chk("NOTE every docstring line is at most 80 columns", doc_overlong_lines(), [])
    chk("CONTROL NOTE an 81-column docstring line is caught",
        [n for _i, n in doc_overlong_lines(__doc__ + "\n" + "x" * 81)], [81])
    del _P_OVERRUNS[:]
    _report_text()
    chk("NOTE no report label overruns _p's 46-column field", list(_P_OVERRUNS), [])
    with contextlib.redirect_stdout(io.StringIO()):
        _p("  remainder 1 - f_l (at first order; heavy-quark part CONTESTED)", "x")
    chk("CONTROL NOTE the old 63-column label is caught", len(_P_OVERRUNS), 1)
    del _P_OVERRUNS[:]
    chk("NOTE READING_REASONS has no duplicate key (a repeat drops an entry silently)",
        duplicate_dict_keys(src, "READING_REASONS"), [])
    chk("CONTROL NOTE a planted duplicate key is caught",
        duplicate_dict_keys("READING_REASONS = {('STOCK', 'C1'): 1, ('STOCK', 'C1'): 2}",
                            "READING_REASONS") != [], True)
    # ---- ROUND 6: three-way seat, H-UNSOURCED-SEAT, TEMPLATE's priced remainder
    # ---- (the held-seat release route), and the round-5 guard gaps closed.
    chk("R6-F every verdict object is DERIVED in this source (C1, C5, READING_VERDICTS, "
        "MECHANISM_VERDICT, S10's status, the held-seat route), not typed",
        underived(src), [])
    for _n, _pat, _typed in DERIVED_ASSIGNMENTS:
        chk("CONTROL R6-F a typed %s is caught by the source check" % _n,
            _n in underived(plant_typed(src, _n)), True)
    chk("R6-F  and each equals a fresh derivation now",
        (FIELD_SWITCHED_ON_BY_ARRIVAL == field_switched_on_by_arrival(),
         READING_VERDICTS == derive_readings(),
         MECHANISM_VERDICT == derive_mechanism(derive_readings()),
         HELD_SEAT_ROUTE_PRICED == held_seat_route_priced(held_seat_route())),
        (True, True, True, True))
    chk("R6-F the section-5 RESULT column says what each reading's refusal rests on",
        doc_table_result_faults(), [])
    chk("  the table's results parsed for every reading",
        sorted(doc_verdict_table(with_results=True)), sorted(ALL_READINGS))
    for _lab, _old, _new in (
            ("SWITCH-ON's result bare 'REFUSED'",
             "  SWITCH-ON     C1                      REFUSED on P-UNIFORM\n",
             "  SWITCH-ON     C1                      REFUSED\n"),
            ("STOCK's result 'REFUSED on P-UNIFORM'",
             "  STOCK         C5                      REFUSED on prior mass (H-PRESENT);",
             "  STOCK         C5                      REFUSED on P-UNIFORM;"),
            ("TEMPLATE's result with 'no remainder'",
             "arrival); what remains is the\n                                        "
             "held-seat release route (survivor d),\n                                        "
             "PRICED", "arrival); no remainder")):
        chk("CONTROL R6-F the section-5 table with %s is caught" % _lab,
            (_old in __doc__, doc_table_result_faults(__doc__.replace(_old, _new)) != []),
            (True, True))
    chk("R6-E section 0 names exactly the readings that keep a remainder, computed from "
        "READING_REMAINDERS", doc_remainder_faults(), [])
    chk("  (they are every reading but SWITCH-ON; TEMPLATE now keeps one)",
        sorted(r for r, t in READING_REMAINDERS.items() if not t.startswith("none")),
        sorted(r for r in ALL_READINGS if r != "SWITCH-ON"))
    _two = _norm(__doc__).replace(
        "FIVE READINGS KEEP A REMAINDER, EVERY ONE BUT SWITCH-ON: DISPLACEMENT AND "
        "QUANTA (THE PAIR ROUTE, PRICED), CREATION (THE ENERGY MUST COME IN THE "
        "CARRIER), STOCK (RECONSTRUCTION FROM STOCK, WHERE NO MASS FORMS) AND TEMPLATE "
        "(THE HELD-SEAT RELEASE ROUTE, PRICED).",
        "TWO READINGS KEEP A REMAINDER: EXCITATION (THE PAIR ROUTE, PRICED) AND STOCK "
        "(RECONSTRUCTION FROM STOCK, WHERE NO MASS FORMS).")
    chk("CONTROL R6-E the old 'TWO READINGS KEEP A REMAINDER' is caught",
        (_two != _norm(__doc__), doc_remainder_faults(_two) != []), (True, True))
    chk("CONTROL R6-E a TEMPLATE remainder of 'none' makes the sentence wrong",
        doc_remainder_faults(remainders=dict(READING_REMAINDERS, TEMPLATE="none: x")) != [],
        True)
    # the fn docstrings, planted old, in place
    _fold = dict(_fn_docs())
    _fold["fn C5"] = _fold["fn C5"].replace(
        "The link could hold only in a world where\n    e, u, d were massless, and there "
        "C1 flips with it; elements at the seat\n    without all or part of their "
        "Higgs-given mass (r < 1) are TEMPLATE's\n    case, not STOCK's, and a seat above "
        "v (r > 1) leaves the trigger nothing\n    to give either.",
        "The link holds only if the elements LACK\n    that mass before arrival.")
    chk("CONTROL R6-F the old C5 docstring, planted in place, is caught by both scans",
        (_fold["fn C5"] != _fn_docs()["fn C5"],
         bool(stale_wording(guard_units(fns=_fold))),
         "R6-F fn C5: below v is TEMPLATE's case, not STOCK's"
         in required_wording(guard_locations(fns=_fold))), (True, True, True))
    _fold = dict(_fn_docs())
    _fold["fn C1"] = _fold["fn C1"].replace("only if it was off or below v at the seat",
                                            "only if it was off at the seat")
    chk("CONTROL R6-F the old C1 docstring, planted in place, is caught by both scans",
        (bool(stale_wording(guard_units(fns=_fold))),
         "R6-F fn C1: off or below v" in required_wording(guard_locations(fns=_fold))),
        (True, True))
    # A: three-way, and H-PRESENT failing names the seat above v
    _s10m = [r for r in PROPOSED_ROWS if r[0] == "S10"][0][5]
    chk("R6-A the S10 and D27 movers send H-PRESENT failing to TEMPLATE (r < 1) or a "
        "seat above v (r > 1)",
        [("the case is TEMPLATE (r < 1) or a seat above v (r > 1" in _norm(r[5]))
         for r in PROPOSED_ROWS if r[0] in ("S10", "D27")], [True, True])
    chk("CONTROL R6-A the mover without its above-v clause is caught",
        bool(stale_wording(guard_units(rows=tuple(
            (r[0], r[1], r[2], r[3], r[4], r[5].replace(H_PRESENT_FAILING,
             "on H-PRESENT failing the case is TEMPLATE, which moves only if C1 reverses "
             "(P-UNIFORM, D15 or D16)")) if r[0] == "S10" else r for r in PROPOSED_ROWS)))),
        True)
    chk("R6-A no 'exhaustive' is printed without 'three-way' anywhere scanned",
        [x for x in stale_wording(_units) if x[0].startswith("R6-A the seat")], [])
    chk("CONTROL R6-A the caps 'THE SPLIT IS EXHAUSTIVE', planted in place, is caught",
        bool(stale_wording(guard_units(doc=__doc__.replace(
            "THE SPLIT IS\nTHREE-WAY:", "THE SPLIT IS\nEXHAUSTIVE.  SO:")))), True)
    chk("R6-A NOTE the matter's own lowering is asked of excite (eps per kg/m^3)",
        self_lowering_per_kg_m3(),
        excite.EPS_AT_FIXTURE / excite.HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18)
    # B: H-UNSOURCED-SEAT, named and load-bearing
    chk("R6-B H-UNSOURCED-SEAT is a NAMED HYPOTHESIS of C1 on TEMPLATE, and not vacuous "
        "(a positive source is an equilibrium on 0 < |phi| < v)",
        (H_UNSOURCED_SEAT, H_UNSOURCED_SEAT_STATUS.startswith("NAMED HYPOTHESIS"),
         FIELD_CAN_BE_EXCITED,
         all(not a for _iv, sg, a in source_sign_table() if sg > 0)), (True, True, True, True))
    chk("R6-B it is carried in C1's TEMPLATE reason, the table, section 6, S10, D27 and "
        "C1's status and docstring",
        ["H-UNSOURCED-SEAT" in t for t in (
            READING_REASONS[("TEMPLATE", "C1")][1],
            doc_verdict_table(with_results=True).get("TEMPLATE", ((), ""))[1],
            _doc_section(6),
            _s10m, [r for r in PROPOSED_ROWS if r[0] == "D27"][0][5],
            [c for c in COUNTS_ON_THE_MECHANISM if c[0] == "C1"][0][3],
            field_switched_on_by_arrival.__doc__)], [True] * 7)
    chk("R6-B the off state lies past D20's stability edge (H-UNSOURCED-SEAT does not "
        "reach SWITCH-ON)", excite.stability_edge() < 1, True)
    # C: the held-seat release route, priced, derived
    _h = HELD_SEAT_ROUTE
    chk("R6-C the route is priced at excite's own eps (asked, the owner's object)",
        HELD_SEAT_EPS is excite.EPS_CHEMICAL, True)
    chk("R6-C (i) it forms no baryons (C3)", _h["forms baryons"], False)
    chk("R6-C (ii) the energy balances exactly over Fraction on every eps0 sample "
        "(radiated >= 0, regained <= F(eps), S/regained >= holding_ratio)",
        _h["balance faults"], [])
    _b = held_release_balance(HELD_SEAT_EPS, HELD_RELEASE_EPS0[1])
    chk("  the field pays: regained = field released - radiated, every term exact",
        (_b["regained"] + _b["radiated"] == _b["field released"],
         all(isinstance(v, Fraction) for v in _b.values())), (True, True))
    _d = Fraction(1, 10 ** 6)
    _b2 = held_release_balance(Fraction(1, 1000) + _d, Fraction(1, 1000))
    chk("  the elements are in equilibrium at their own lowering: the release radiates "
        "only at second order (0 <= radiated <= 4 d^2, F'' <= 8 there)",
        0 <= _b2["radiated"] <= 4 * _d * _d, True)
    chk("  the phi-coupled rest energy is holding_ratio(eps) J per J of field (excite)",
        _h["source (rho_EW)"] / _h["field (rho_EW)"], excite.holding_ratio(HELD_SEAT_EPS))
    chk("CONTROL R6-C past the stability edge the balance fails (the check can fire)",
        held_release_faults(Fraction(3, 5), [Fraction(1, 2)]), [Fraction(1, 2)])
    chk("R6-C (iii) the electrons regain eps x their share exactly; the nucleons' "
        "first-order figure is eps x the largest READ nucleon row",
        (_h["electrons regained"] == float(HELD_SEAT_EPS) * share_rows()[0][2],
         _h["nucleons first order"] == float(HELD_SEAT_EPS) * largest_read_nucleon_row()),
        (True, True))
    chk("  and the hold is stable at the eps priced; CONTROL at eps = 1/2 it is not, "
        "and the route is not priced there",
        (_h["stable"], held_seat_route(Fraction(1, 2))["stable"],
         held_seat_route_priced(held_seat_route(Fraction(1, 2)))), (True, False, False))
    chk("R6-C (iv) it needs a prior arrival: D23 asked of the ledger (owner "
        "transit.TRAVERSAL_IS_REMOVED = False)",
        (preparation_needs_prior_arrival(), d23_row()[3], transit.TRAVERSAL_IS_REMOVED),
        (True, ("transit", "TRAVERSAL_IS_REMOVED"), False))
    chk("CONTROL R6-C a D23 row with another owner is not read as D23's point",
        preparation_needs_prior_arrival((d23_row()[0], d23_row()[1], d23_row()[2],
                                         ("transit", "CARRIES_SUBSTANCE"))), False)
    chk("R6-C the route is PRICED, in READING_REMAINDERS, SURVIVES, S10 and S13",
        (HELD_SEAT_ROUTE_PRICED, HELD_SEAT_TEXT in READING_REMAINDERS["TEMPLATE"],
         any(n == "the held-seat release route" and HELD_SEAT_TEXT in t for n, t in SURVIVES),
         "held-seat release route (S13)" in [r for r in PROPOSED_ROWS if r[0] == "S10"][0][2],
         [(r[3], r[4]) for r in PROPOSED_ROWS if r[0] == "S13"]),
        (True, True, True, True, [("OPEN", ("massform", "HELD_SEAT_ROUTE_PRICED"))]))
    chk("R6-C TEMPLATE prints refused on H-UNSOURCED-SEAT, remainder priced; the "
        "mechanism line names it",
        (reading_label("TEMPLATE"), "held-seat release route, PRICED" in mechanism_label()),
        ("REFUSED on P-UNIFORM and H-UNSOURCED-SEAT; remainder the held-seat release "
         "route, PRICED", True))
    REMAINDER_RESTORES_MASS["TEMPLATE"] = False
    try:
        _bare_t = (reading_label("TEMPLATE"), "held-seat" in mechanism_label())
    finally:
        REMAINDER_RESTORES_MASS["TEMPLATE"] = HELD_SEAT_ROUTE_PRICED
    chk("CONTROL R6-C without a priced remainder TEMPLATE prints no remainder "
        "(refused on C1's premises alone)",
        _bare_t, ("REFUSED on P-UNIFORM and H-UNSOURCED-SEAT (C1 alone)", False))
    chk("CONTROL R6-C refusal 9 fires on the old section-5 verdict line (pair route "
        "only)", bool(unqualified_refusals(
            "THE MECHANISM AS STATED: REFUSED on every reading; on DISPLACEMENT and "
            "QUANTA as NET formation only -- atomic mass can still form there as matter "
            "with its antimatter (the pair route, PRICED).")), True)
    chk("CONTROL R6-C refusal 9 fires if the held-seat route were dropped from what "
        "survives",
        refusal_flags(text, survives=tuple(x for x in SURVIVES
                                           if x[0] != "the held-seat release route"))[9][1],
        True)
    # D: SWITCH-ON's C5 reason
    chk("R6-D SWITCH-ON's C5 reason: seated elements at |phi| = 0 are TEMPLATE, refused "
        "on C1", ("it is TEMPLATE at |phi| = 0, refused on C1"
                  in READING_REASONS[("SWITCH-ON", "C5")][1],
                  _is_template(Fraction(0))), (True, True))
    chk("CONTROL R6-D the old 'it is the STOCK reading' is caught",
        bool(stale_wording(guard_units(reasons={k: ((v[0], v[1].replace(
            "it is TEMPLATE at |phi| = 0, refused on C1", "it is the STOCK reading"))
            if k == ("SWITCH-ON", "C5") else v) for k, v in READING_REASONS.items()}))),
        True)
    # ---- ROUND 7 (round-6 verifiers)
    # 1: the nucleons' figure, electrons excluded
    chk("R7-1 the nucleons' first-order figure is eps x the largest READ nucleon row, "
        "and with the electrons' it sums to eps x HIGGS_SHARE_LARGEST_READ",
        held_seat_share_faults(), [])
    chk("  it is 1.7157e-3 at eps = 1/100 (electrons 3.0102e-6, not counted twice)",
        ("%.4e" % _h["nucleons first order"], "%.4e" % _h["electrons regained"]),
        ("1.7157e-03", "3.0102e-06"))
    chk("CONTROL R7-1 the round-6 expression, eps x (electrons + nucleons), is caught",
        held_seat_share_faults(dict(_h, **{"nucleons first order":
                                            float(HELD_SEAT_EPS) * HIGGS_SHARE_LARGEST_READ})),
        ["nucleons", "sum"])
    # 2: the holding price is the owner's exact ratio; 2/eps its limit
    chk("R7-2 excite.holding_ratio is 4(1-eps)^2/(eps(2-eps)) as polynomials, and "
        "eps x it -> 2 as eps -> 0 (exact, excite's own SOURCE_POLY, FIELD_POLY)",
        holding_ratio_form(), (True, 2))
    _r = excite.holding_ratio(HELD_SEAT_EPS)
    _ee = Fraction(excite.stability_edge())
    chk("  at eps = 1/100 it equals the closed form; 2/eps overstates it, over 2x at the edge",
        (_r == 4 * (1 - HELD_SEAT_EPS) ** 2 / (HELD_SEAT_EPS * (2 - HELD_SEAT_EPS)),
         _r < 2 / HELD_SEAT_EPS, excite.holding_ratio(_ee) < Fraction(1, 2) * (2 / _ee)),
        (True, True, True))
    _F = list(excite.FIELD_POLY)
    chk("CONTROL R7-2 a price of 2/eps fails the exact form; a price of eps/2 fails the "
        "limit",
        (holding_ratio_form(source=[2 * x for x in _F[1:]])[0],
         holding_ratio_form(source=[0] + [x / 2 for x in _F])[1] == 2), (False, False))
    # 3: an equilibrium on 0 < |phi| < v, a stable hold only on the stable range
    _eh = excite.stability_edge()
    chk("R7-3 the stable range is (1 - excite.stability_edge()) v < |phi| < v, and the "
        "route is priced just inside it and not just outside",
        (STABLE_RANGE == "%.4f v < |phi| < v" % (1 - _eh),
         held_seat_route_priced(held_seat_route(Fraction(_eh) - Fraction(1, 10 ** 6))),
         held_seat_route_priced(held_seat_route(Fraction(_eh) + Fraction(1, 10 ** 6)))),
        (True, True, False))
    chk("  it is stated wherever the route's reach is: the status, the remainder, "
        "sections 1, 5 and 6",
        [STABLE_RANGE in _norm(t) for t in (H_UNSOURCED_SEAT_STATUS, HELD_SEAT_TEXT,
                                             _doc_section(1), _doc_section(5),
                                             _doc_section(6))], [True] * 5)
    # 4: the floor, and how loose it is at the samples
    _sh = held_release_regained_shares()

    def _shares_recomputed(shares, eps=HELD_SEAT_EPS):
        """Each share recomputed from excite.holding_terms directly, and the
        energy closing: regained + radiated + F(eps0) == F(eps)."""
        S_e, F_e = excite.holding_terms(eps)
        ok = True
        for e0, x in shares:
            S0, F0 = excite.holding_terms(e0)
            reg = S0 / (1 - e0) * (eps - e0)
            ok = ok and x == reg / (F_e - F0) and reg + (F_e - F0 - reg) + F0 == F_e
        return ok
    chk("R7-4 regained/released at every eps0 sample is below 1 (the rest of what is "
        "released is radiated; F(eps0) stays in the field), recomputed from excite, "
        "and the sampled figures are printed",
        (all(0 < x < 1 for _e0, x in _sh), _shares_recomputed(_sh),
         regained_shares_text() in _norm(__doc__), regained_shares_text() in _rep),
        (True, True, True, True))
    _old = [(e0, held_release_balance(HELD_SEAT_EPS, e0)["regained"]
             / excite.holding_terms(HELD_SEAT_EPS)[1]) for e0 in HELD_RELEASE_EPS0]
    chk("CONTROL the old F(eps) denominator fails the recomputation",
        _shares_recomputed(_old), False)
    # 5: the guard gaps round 6 left
    chk("R7-5 no selftest label says 'exhaustive' without 'three-way' (CONTROL labels "
        "quote old wording and are exempt)", stale_labels(), [])
    chk("CONTROL R7-5 the round-5 label, planted in this source, is caught",
        bool(stale_labels(selftest_labels(inspect.getsource(sys.modules[__name__]).replace(
            'chk("R6-A the seat splits three ways', 'chk("R6-A the STOCK/TEMPLATE split is '
            'exhaustive')))), True)
    _bal = lambda e, e0, **kw: dict(held_release_balance(e, e0), **kw)
    _e0 = HELD_RELEASE_EPS0[:1]
    chk("CONTROL R7-5 each balance conjunct can fire alone: regained above the field's "
        "energy; S below holding_ratio x regained",
        (held_release_faults(HELD_SEAT_EPS, _e0, lambda e, e0: _bal(
            e, e0, **{"field at eps": held_release_balance(e, e0)["regained"] / 2})),
         held_release_faults(HELD_SEAT_EPS, _e0, lambda e, e0: _bal(
             e, e0, **{"source at eps": Fraction(0)}))), (list(_e0), list(_e0)))
    chk("CONTROL R7-5 a route with balance faults is not priced",
        held_seat_route_priced(dict(_h, **{"balance faults": [Fraction(1, 200)]})), False)
    chk("CONTROL R7-5 a D23 row with the right owner and the wrong text is not read as "
        "D23's point", preparation_needs_prior_arrival(
            (d23_row()[0], "a destination-side arrangement", d23_row()[2],
             d23_row()[3])), False)
    chk("nothing is repaired, no peer is edited", (NOTHING_IS_REPAIRED, EDITS_A_PEER), (True, False))

    print()
    if fails:
        print("  SELFTEST FAILED: %d" % len(fails))
        for f in fails:
            print("    %s: got %r want %r" % f)
        return 1
    print("  SELFTEST OK")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    report()
