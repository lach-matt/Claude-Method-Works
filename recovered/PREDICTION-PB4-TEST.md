# PREDICTION-PB4-TEST (s48) — FILED BEFORE `pb4_terms.py` EXISTS

Binding under R 1449 and design-precedes-result. Scores PB-4 of PREDICTION-4fBLOCK-61-71.
Every configuration below is RECALLED-NOT-ENTERED from the record and used only as a
COMPARISON TARGET; none is entered as an input to any SCF.

## 1 · PB-4's FRAMING IS PARTLY WRONG, AND THE CORRECTION IS REGISTERED BEFORE THE RUN

PB-4 named Gd(64) and Lu(71) as the elements where exchange must be tested. Reading the
closed block shows that is **the wrong pair of elements**, and the error is registered here
rather than quietly repaired:

    Z    walk cfg              record cfg (RECALLED)   ok     cfg
    58   4f1 5d1 6s2           4f1 5d1 6s2             True   MATCH
    59   4f2 5d1 6s2           4f3 6s2                 True   FAIL   <- divergence STARTS
    63   4f6 5d1 6s2           4f7 6s2                 True   FAIL
    64   4f7 5d1 6s2           4f7 5d1 6s2             False  MATCH  <- reconverges
    71   4f14 5d1 6s2          4f14 5d1 6s2            False  MATCH

At 64 the walk was choosing between **4f7 5d1 6s2** and **4f6 5d2 6s2**, and it chose the
first — WHICH IS THE RECORD'S CONFIGURATION. The field won that competition. Its ok=False is
a LABEL failure: the record's 5d occupancy rises 0->1 there, so the record's differentiating
electron is 5d, while the walk (already holding 5d1 since La) added its 4f. The same holds at
71. **The field never faced 4f8 6s2 at Gd, because its own Z=63 configuration is 4f6 5d1 6s2.**
So a 4f8-vs-4f7-5d1 exchange test at 64 tests the RECORD's question, not the walk's, and
cannot score the walk either way.

**The divergence has ONE origin: Z=59.** The record vacates 5d at Pr and puts TWO electrons
into 4f; the walk cannot vacate anything. Every cfg failure from 59 to 70, and both label
failures at 64 and 71, descend from that single step. That is where exchange must be tested.

## 2 · THE TEST

At **Z=59** (the origin) and, as a control, at **Z=64** (PB-4's named element), compare two
neutral configurations on the ruling field — hfc2, SR HF, CORR=False, frozen
average-of-configuration orbitals from each configuration's OWN SCF:

    Z=59   A = [Xe] 4f2 5d1 6s2   (the walk's)      B = [Xe] 4f3 6s2   (the record's)
    Z=64   A = [Xe] 4f7 5d1 6s2   (both)            B = [Xe] 4f8 6s2   (the record's rejected)

For each: E_avg from `H.HFC(Z,occ,c=C0).run2()`, then the Slater term correction
dE = E_open(hund_det(shells),Fk,Gk) - E_avg(shells,Fk,Gk) from that state's own radials, as
in `nlterm.state`. Report **dTOT = (E_A + dE_A) - (E_B + dE_B)**, and the same difference at
avg-of-config alone (**dAVG = E_A - E_B**), so the term contribution is isolated:
**dTERM = dTOT - dAVG**. Negative means A (the 5d-holding configuration) is lower.

## 3 · THE CLAUSES

**PT-1 — AT Z=59 THE AVERAGE-OF-CONFIGURATION FIELD PREFERS A (the walk's 4f2 5d1 6s2).**
dAVG < 0. This must hold or the walk's own 59 step is inconsistent with its field, which
would be an internal fault, not a physics result. Falsified by dAVG >= 0.

**PT-2 — AT Z=59 THE TERM CORRECTION FAVOURS B, i.e. dTERM > 0.** 4f3 has three parallel f
electrons and a 4I lowest term; 4f2 5d1 spreads the same three electrons over two shells and
cannot align as many pairs. Exchange must push toward B. Falsified by dTERM <= 0.

**PT-3 — THE SHARP ONE: AT Z=59 EXCHANGE FLIPS THE ORDER OUTRIGHT, dTOT > 0.**
If it flips, the record's promotion at Pr is EXCHANGE, computed on the walk's own field with
no new constant, and the 59..70 cfg divergence closes at its origin. Falsified by dTOT <= 0,
which would mean exchange is necessary but not sufficient and the promotion needs a further
mechanism (relaxation, correlation, or SO) — a real outcome, to be logged as such.

**PT-4 — AT Z=64 THE FIELD PREFERS A ON BOTH MEASURES, dAVG < 0 AND dTOT < 0.**
4f7 5d1 6s2 is the record's Gd. The half-filled 4f7 shell is present in A, absent in B, so
exchange should REINFORCE the choice the field already made rather than overturn it, and
|dTERM| at 64 should carry the sign OPPOSITE to its sign at 59. Falsified by dTOT >= 0, which
would put the field on the wrong side of an element it currently gets right.

**PT-5 — NO CONSTANT IS INTRODUCED.** The only entered number remains c = 137.035999.
Falsified by any clause requiring a fitted or swept parameter.

## 4 · NOT PREDICTED

Magnitudes of any of dAVG, dTERM, dTOT — no bands, per the s48 ruling; the SIGNS above are the
claims. Whether a promotion operator built on this result reproduces 60..70 (that is its own
object and is NOT closed by PT-3 holding). Lu(71). Anything relativistic beyond the SR field
already in use. SO splitting (zeta is a separate column and is not run here).
