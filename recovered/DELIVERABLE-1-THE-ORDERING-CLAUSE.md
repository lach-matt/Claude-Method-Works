# DELIVERABLE 1 — THE ORDERING CLAUSE
## A parameter-free field derivation of the Madelung sequence, and what it does and does not claim
Session 52. Scored against PREDICTION-DELIVERABLE-1.md (sha256 e19fc0a2…, filed
2026-08-19T23:34:19Z before the chain was read). Evidence: `nlchain.jsonl`, 119 rows,
sealed in pack51; gates 83, 84, 85; `verify51.sh` ok=1038 bad=0 extra=0.

---

## §0 · WHAT IS CLAIMED, IN ONE PARAGRAPH

From a parameter-free scalar-relativistic Hartree-Fock field, computed independently at
each atom, the channel of the differentiating electron was predicted before each run and
scored after it, for Z = 2..108. **The ordering clause of the Madelung rule — fill in
increasing n+l — has ZERO failures in 119 steps.** The tie-break clause — lower n first
within equal n+l — is exercised and obeyed at 94 of 107 steps, and its three failures
fall inside a domain boundary that the field itself computes. The differentiating
electron is correct at 96 of 107 steps; the total ground-state configuration at 73 of
107. **The two are shown to be different objects with almost disjoint failure sets**,
which is Löwdin's second clause answered from data rather than from argument.

The only number ever entered into this chain is **c = 137.035999**. No screening
constant, no fitted parameter, no ionization energy, no experimental level.

---

## §1 · THE PRIOR ART, AND THE JOINT ON WHICH IT IS REJECTED

Löwdin (1969) named the derivation of the n+l rule an unsolved problem. Attempts since
divide into three families. Full citations: ATTRIBUTION-LEDGER-LOWDIN.md.

**Family B — a chosen potential or symmetry.** Demkov & Ostrovsky (1972) obtain the rule
from a focusing potential of Thomas-Fermi type; Ostrovsky (2001) develops the dynamic
group. Kitagawara & Barut (1983, 1984) identified flaws in the DO logic. Thyssen &
Ceulemans (2017, p.381) state the DO results, though correct, **cannot be considered a
solution of the Löwdin challenge**, on the ground that the effective potential was
GUESSED and that level-energy quantization was replaced by quantization of coupling
constants at zero energy. The group-theoretic descendants (Kibler; Fet; Varlamov; the
SO(4,4) tower) inherit the same status: they exhibit a symmetry under which the sequence
is natural, not a field from which it follows. Kholodenko (2017, 2020) derives it from
the Tietz potential and claims the challenge solved analytically, while conceding the
transition-metal, lanthanide and actinide exceptions are not described in detail. Aruna
Kumar (2026) obtains 1s<2s<2p<...<8s<5g from a regularized one-centre Coulomb problem —
but fixes the orbital label by MINIMISING its own spectrum and assigning that branch to
the s-sector, and the author disclaims it as no replacement for many-electron theory.
Baez (2026) obtains Madelung-type rules from a second-quantized Kepler model.

**Family C — published tables.** Allen & Knight (2002) devise a perturbation operator
locating the d- and f-blocks and verify it against Desclaux's 1973 Dirac-Fock tables for
Z = 1..118. The ordering is read from data, not computed toward.

**Family D — reinterpretation.** Scerri, having long argued the rule was underivable,
now holds that the anomalies are the crossing of the s1 and s2 CONFIGURATION energies,
computable by Hartree-Fock; and that the rule does not give the order of occupation of
orbitals within the independent-electron approximation at all.

**THE JOINT.** Family B is rejected because the potential is chosen; family C because
the ordering is read; family D declines to derive and reframes instead. This work stands
at neither joint: **the field is computed at each atom from the nuclear charge alone,
and the entrant is predicted before it is scored.** That is the distinction, and it is
the only one being claimed here.

---

## §2 · THE ORDERING CLAUSE

At each Z the field is solved and every admissible channel returns a depth D. The
entrant is the deepest admissible channel. Scored across Z = 2..120:

    ORDERING FAILURES: 0 in 119 steps.

The clause is therefore not fitted to the table; it is what the depths say at every atom
independently. Gate 85 locks this over all 119 rows.

**The mechanism of the margin is a further result.** The margin between winner and
runner-up does not vary with Z. It changes discontinuously, and every discontinuity is a
change of WHICH TWO CHANNELS COMPETE: 0.26417 collapsing to 0.05809 at Z=113 where the
competing pair turns from 6d/7p to 7p/8s, recovering to 0.21015 by 118, falling again at
the 8s opening. Four such events. The margin is a property of the adjacent pair, not of
the nucleus.

---

## §3 · THE TIE-BREAK CLAUSE AND ITS DOMAIN

The tie-break is a second law, not a corollary: the ordering clause is readable from any
single atom's depths, the tie-break is a property of the SEQUENCE and is readable from
none. It is exercised and obeyed at **94 of 107** steps, with three failures: La(57),
Ac(89), Th(90).

The domain is computed, not fitted. Every g channel sits pinned at exactly -1/(2n^2) and
does not move with Z — 5g across 65 atoms spanning Z=20..120, 6g across 70, 7g 57, 8g
28, each with total spread at or below 1e-5, while every s, p, d and f channel in the
same rows moves. A channel that does not respond to the nucleus is not in the field.
With kappa = D_field / (-1/(2n^2)) and n* = 1/sqrt(-2D), collapse is complete when
dn*/dZ = 0 fails to hold — i.e. the channel has entered the field and reached its depth.

    TIE-BREAK CLAUSE: lower n first among equal n+l,
                      OVER CHANNELS WHOSE COLLAPSE IS COMPLETE.

The three failures are the only steps in the table where a tie-break pair becomes
testable before the lower-n channel has finished collapsing. Ac(89) is the plateau case
(5f genuinely uncollapsed, dn*/dZ = -0.0095); La(57) and Th(90) are transit cases, n*
falling 1.82 and 2.08 in a single proton. No s, p or d pair is ever affected — only f
openings have a plateau to leave. Plateau spreads 0.0057 (4f) and 0.0115 (5f) against a
transit near 2: the regimes are sharply separated.

**And the field says why there is no g block.** No g channel collapses anywhere below
Z=121. They are admissible at every step and win none. 5g never comes within 0.16 Ha of
winning.

**NOT CLAIMED:** kappa does not separate the three failures from the 94 holds by any
threshold. La sits at 3.38 and Th at 6.84, inside the holds' range (2.33 to 39.73, none
below 2.0); only Ac at 1.57 falls below every hold. The separation is by REGIME, read
from the derivative. A cut on a value would be a fitted constant and is refused.

---

## §4 · LÖWDIN'S CLAUSE 2 — THE FILLING AMBIGUITY, ANSWERED FROM THE DATA

The challenge asks what the derivation actually governs: the ground-state filling of all
electrons, or the differentiating electron. **The sealed chain answers by measurement.**

    DIFFERENTIATING ELECTRON (ok)     96 / 107     first failure Z=25
    TOTAL CONFIGURATION    (cfg)      73 / 107     first failure Z=24

These are not one column with two error rates. **Their failure sets are almost
disjoint**: 34 cfg-failures, 11 ok-failures, overlap of THREE (47, 96, 103). Thirty-one
steps carry a correct differentiating electron and a wrong total configuration; eight
carry a correct total configuration and a wrong differentiating electron. Gate 83's
`disagree` count stands at 39.

**The structure behind the disjointness is exceptionless and one-directional.** Every
one of the eleven ok-failures is immediately preceded by a cfg-failure at Z-1:

    25<-24  30<-29  43<-42  47<-46  48<-47  64<-63
    71<-70  80<-79  96<-95  103<-102  104<-103        ALL 11, no exception

The converse fails: 23 cfg-failures are not followed by an ok-failure. So the relation
is informative, not a restatement. Its reading: the walk's entrant is wrong at exactly
the step where an EARLIER PROMOTION IS BEING UNDONE — the observed atom refills the s
orbital the one-electron walk never emptied. The ok-failures are recovery steps of
promotions recorded one element earlier, not independent failures of the rule.

**Therefore: the derivation governs the differentiating electron.** The n+l rule is a
law about which channel receives the next electron. It is not a law about the total
configuration, and the 34 cfg disagreements are the measure of the difference between
the two questions rather than errors in the answer to one of them. This reaches Scerri's
and Schwarz's conclusion independently and by a different route, and gives the promotion
structure a scored form neither states.

---

## §5 · LÖWDIN'S CLAUSE 7 — THE PARADOX OF EXCEPTIONS

The known anomalies partition cleanly, and none of them is an ordering failure.

  (a) **PROMOTIONS** (Cr 24, Cu 29, Nb 41, Mo 42, Ru 44, Rh 45, Pd 46, Ag 47, Pt 78,
      Au 79, the 4f run 59-70, the 5f run 91-103). An electron already placed moves
      s->d or s->f. The one-electron walk format CANNOT EXPRESS this, because its unit
      of action is the addition of one electron, not the rearrangement of the set. This
      is a limitation of the format, and it is visible as the cfg column. The n+l rule
      is untouched: the ENTRANT channel is still the deepest admissible one.
  (b) **RECOVERIES** (the 11 ok-failures). Consequences of (a), one step later, per §4.
  (c) **TIE-BREAK DOMAIN CASES** (La 57, Ac 89, Th 90). Not exceptions to the rule but
      steps outside the clause's computed domain, per §3.

Every known anomaly falls in (a), (b) or (c). **No residue class remains.**

---

## §6 · WHAT IS OWED, NAMED AND NOT GLOSSED

1. **THE FIELD IS SCALAR-RELATIVISTIC; THE CHALLENGE SPECIFIES THE NON-RELATIVISTIC
   SCHRÖDINGER EQUATION.** This is the live exposure of clause 3. Because c = 137.035999
   is the ONLY entered number, the test is direct: re-walk at c -> infinity and show the
   ordering clause survives. Not yet run. Until it is, this document claims a derivation
   from a scalar-relativistic field, not from the non-relativistic Schrödinger equation.
2. **THE REVERSE DERIVATION** — the explicit chain from the many-electron Schrödinger
   equation to the field actually solved, with each approximation named and its effect
   on the ordering bounded. Owed since s47 item (10).
3. **THE TRANSIT WIDTH** — why the lag is one proton at 4f and two at 5f. The gap
   between a condition that IDENTIFIES the domain boundary, which §3 is, and one that
   DERIVES it, which §3 is not.
4. **THE EVIDENTIARY BOUNDARY** — the derivation is 107 rows, Z=2..108. The 12 rows
   Z=109..120 are OUTPUT, predicted and unscored. Any claim of 119 derived rows is a
   boundary violation.

---

## §7 · EVIDENCE INDEX

    nlchain.jsonl            119 rows, pack51, sealed
    gate 83                  cfg (73,107) ok (96,107) cfg_first 24 ok_first 25 str_mismatch []
    gate 84                  nlguard, PASS
    gate 85                  20 clauses, PASS, can-failed both directions
    gates 1..71              replayed s52 from fresh extract, 283 lines, 71 rc=0, diff ZERO
    verify51.sh              ok=1038 bad=0 extra=0, both halves, can-failed both directions
    PREDICTION-DELIVERABLE-1.md   e19fc0a2…, filed before the chain was read
    ATTRIBUTION-LEDGER-LOWDIN.md  6589437256…, 26 entries, all fetched this session