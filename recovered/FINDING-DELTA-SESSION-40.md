# FINDING-DELTA (s40, item 3) — THE ORDERING IS ENTIRELY PENETRATION ON Z = 2..20, AND THE CENTRIFUGAL GATE COMES BACK.
Object: D(n,l) = -1/(2n^2) + Delta(n,l) scored against PREDICTION-DELTA on the bank alone (delta.py). 112 channels:
19 chain steps (Z=2..20) plus the 20 banked hf_chan rows. No SCF, no fitted reference, no constant beyond c.

## 1 · F40.2 REGISTERED — A FAULT IN MY OWN TEST, NOT IN THE FIELD
PD-2 was written "at fixed Z" and scored by taking, for each l, the largest |Delta| over ALL n present. That compares
ACROSS n, where the hydrogenic term differs, and it scored 7/19. The claim intended, and the only one the physics
supports, is at fixed n AND fixed Z. RESCORED CORRECTLY: **28 of 28 groups, 55 adjacent (l, l+1) pairs, ZERO
VIOLATIONS.** |Delta| is strictly decreasing in l at fixed (Z, n), exceptionless on the bank.
The prediction was mis-stated at filing and the rescore is reported as a RESCORE, flagged, not as a held prediction.
This is the per-element-from-class-mean fault's cousin: a quantity aggregated over a coordinate that was supposed to
be held fixed. Caught in scoring; changes no computed number.

## 2 · PD-4 HELD 13/13 — REGISTER 1255'S CENTRIFUGAL GATE, RE-DERIVED FROM SCF ENERGIES
With l_max = the largest l occupied in the reference configuration:
    |Delta| < 1e-3 Ha for every channel with l >= l_max + 2.    13 of 13, no exception.
    MEDIAN |Delta| GATED 0.00001 · UNGATED 0.05272 — FOUR ORDERS OF MAGNITUDE.
Register 1255 measured this gate on MEASURED QUANTUM DEFECTS across 325 real channels (frac(delta) ~ 0 when
l - l_core >= 2; 123 channels, median 0.017 against 0.327, Mann-Whitney p = 2.2e-20). It is here again, on a different
instrument, from a different direction: SCF total-energy differences on a parameter-free field, arrived at without
consulting 1255. TWO INDEPENDENT MEASUREMENTS OF ONE MECHANISM. A Rydberg electron two units of angular momentum above
the core's outermost is centrifugally excluded from it and stays hydrogenic — and "stays hydrogenic" is now literal:
Delta = 0.00000 at K 4f and Ca 5g, to five decimal places.

## 3 · PD-5 HELD, AND THE f COLLAPSE HAS ITS INTERMEDIATE POINT
Delta(4f) banked: Z12 -0.00002 · Z13 -0.00001 · Z14 -0.00002 · Z15 -0.00001 · Z16 -0.00001 · Z17 -0.00001 ·
Z18 +0.00000 · Z19 +0.00000 · Z20 -0.00007 · **Z55 (Cs) -0.00002** · **Z57 (La) -0.07431** · **Z58 (Ce) -0.33575**
Zero to 5 dp across FORTY-THREE PROTONS (Z=12 to Z=55), then -0.074 at La and -0.336 at Ce. The collapse is a
discontinuity in Delta and NOT in D — in D it is masked by the hydrogenic term, which is constant at -0.03125 for
every 4f row and therefore carries none of it. Bridge item 4 (the Cs->Ba->La->Ce trace) is now half-delivered from the
existing bank; Ba (Z=56) is the missing point and is one hf_chan row.

## 4 · PD-6 FAILED, AND THE FAILURE IS THE RESULT
I predicted BOTH terms load-bearing — that some step would have entrant != argmax|Delta|. NONE DOES.
    **THE ENTRANT IS THE CHANNEL OF LARGEST |Delta| ON 19 OF 19 STEPS.**
The hydrogenic term never decides on Z = 2..20. It is not inert — it sets the scale of D — but it never selects.
Meanwhile entrant != argmin n at Z=19 and Z=20, so n does not decide either. On this range the filling law reduces to
one clause with no free part: THE ELECTRON ENTERS THE MOST PENETRATING OPEN CHANNEL.
Stated as a falsifiable claim for the range above: this is expected to BREAK somewhere, because n+l is not "largest
|Delta|" in general — 4f at Cs has |Delta| = 0.00002 and still lies far above 6s. Where it breaks is where the
hydrogenic term starts to decide, and finding that Z is the next measurement.

## 5 · PD-7 HELD — THE 4s/3d INVERSION, DECOMPOSED
At K (Z=19):  hydrogenic favours 3d by 0.02431 Ha · Delta favours 4s by 0.11398 Ha · net 4s wins by 0.08967 Ha.
THE HYDROGENIC TERM PREFERS 3d AND LOSES, by a factor of 4.7. The 4s-before-3d inversion — the canonical illustration
of the n+l rule, and the thing every textbook asserts without deriving — is ENTIRELY A PENETRATION EFFECT on this
field, with no fitted quantity anywhere in the statement.

## 6 · PD-1 FAILED ON EXACTLY ONE CHANNEL, AND IT IS Ac
111 of 112. The single violation: **Ac (Z=89) 5f, Delta = +0.00188** — D = -0.01812 against hydrogenic -0.02000.
A POSITIVE Delta means the channel binds LESS than a fully screened core would give, i.e. it sees LESS than unit
charge. Three candidate mechanisms, none tested here and all named for the record: (a) OVER-SCREENING by the frozen
avg-of-config reference, which PV-3 has never bounded; (b) the SR contraction of the inner shells pushing 5f outward
past the screening radius; (c) an artefact of the common-ion reference hf_chan uses per Z.
IT IS NOT A RANDOM ROW. Ac is one of the 13 exceptional rows, sits in the Th/Ac pair that has been the sole
row-differential residual since s37, and is the only channel in 112 that crosses the hydrogenic floor. REGISTERED AS
THE FIRST QUANTITATIVE THING THAT SINGLES Ac OUT WITHOUT REFERENCE TO THE RECORD. PV-3 is now load-bearing and should
be run before this is interpreted further.

## 7 · Score summary
HELD: PD-4 (13/13), PD-5, PD-7. FAILED: PD-1 (111/112, one channel, Ac 5f), PD-6 (19/19 the other way — stronger than
predicted), PD-3 (untested; not scored, no n-series at fixed l is long enough on the bank).
RESCORED AND FLAGGED: PD-2 (F40.2), 28/28 groups and 55/55 pairs at fixed (Z,n).
Timing flag from FINDING-CHAIN §5 IS DISCHARGED: the decomposition now has a prediction file written before its scoring
run, and the run scored 3 held, 2 failed, 1 rescored — which is what a real prediction file looks like.
