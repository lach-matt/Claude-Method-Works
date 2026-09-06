# F79.2 — THE Z=89 MARGINS COMPARE ONE-ELECTRON EIGENVALUES AGAINST TOTAL-ENERGY
# DIFFERENCES. SEVERITY: CATEGORY ERROR IN THE COMPARISON, PRE-EXISTING AT s77 AND
# INHERITED BY THIS SESSION'S OWN ITEM-2 RESULT. RAISED HERE. NOT CLOSED.

## WHAT -0.15762 ACTUALLY IS, MEASURED
pack77/o89_89_A.jsonl carries one column, `E`, a TOTAL ENERGY.
  ref  E = -25694.384010   |   6d  E = -25694.541631   |   5f  E = -25694.415473
  **6d - ref = -0.157621 Ha.  5f - ref = -0.031463 Ha.**
**SO -0.15762 IS A TOTAL-ENERGY DIFFERENCE, dE = E(cfg + channel) - E(ref), AND
m(89) = 32.330 mHa IS A MARGIN BETWEEN TWO SUCH DIFFERENCES** (157.621 - 125.290).

## WHAT THE WINDOWS AND THE FOUND ZEROS ARE
nodespec's window and refine79's bisected zero are energies `e` inside `solve_one` —
**ONE-ELECTRON EIGENVALUES of the radial Fock problem.** They are a different object.

## THE TWO ARE NOT EQUAL, AND THE SIZE OF THE GAP IS NOW MEASURED
At Z=89 for 6d: **dE = -0.157621 while eps(6d) = -0.176898. THEY DIFFER BY 19.277 mHa** —
core relaxation plus the correlation potential Vc. **Not a rounding difference; comparable
to the 32.330 mHa margin itself.**

## WHERE THE ERROR ENTERS THE RECORD
1. **pack77/RESULT-S77-ITEM1-FIVE-CHANNELS.md** — *"103.8 mHa above 6d"*, *"71.45 mHa
   ABOVE THE RUNNER-UP ... 2.2 and 3.2 times the 32.330 mHa argmin margin."* Every one of
   those five comparisons puts an eigenvalue window against a dE.
2. **pack79/RESULT-S79-ITEM2-Z89-FOUND-STATES.md, WRITTEN THIS SESSION.** Its margin table
   — 93.690 mHa, 2.898 m and the rest — has the same defect. **REGISTERED HERE AGAINST MY
   OWN RESULT IN THE SAME SESSION, NOT LEFT FOR A LATER ONE TO FIND.**
3. **The item-1 prediction's W3** named -0.15762 as the comparand for the frozen 6d probe.

## WHAT SURVIVES AND WHAT DOES NOT
**SURVIVES — pack79/RESULT-S79-ITEM1-FIXED-FIELD.md IS UNAFFECTED.** It compares eps
against eps in one frozen field. Both sides are the same object. Its 155.369 mHa stands.
**SURVIVES, PROVISIONALLY — the qualitative verdict at Z=89.** The measured currency
offset at 6d is 19.3 mHa; the smallest eigenvalue margin quoted is 93.690 mHa. An offset
of that size does not reverse a gap of that size. **BUT THAT IS AN ESTIMATE FROM ONE
CHANNEL'S OFFSET, NOT A BOUND ON THE OFFSET IN THE OTHERS.**
**DOES NOT SURVIVE — every stated MULTIPLE OF THE MARGIN.** "2.898 m", "2.2 and 3.2 times",
"more than twice the margin" are ratios of unlike quantities and are withdrawn as stated.

## THE REPAIR, SPECIFIED AND NOT RUN — OWED
**Convert the three found f states into dE, the currency the ranking is actually in:**
run the Z=89 SCF at cfg+6f, cfg+7f, cfg+8f with refine79's node-count-targeted scan as the
solver's fallback, and take E - (-25694.384010). **This is now REACHABLE, and it was not
before item 2, because the SCF could not stay on the target node count.** Until it is run,
the Z=89 hole is three eigenvalues and two brackets, and **NOT three entries in the table
that decides the row.**

## THE STANDING POINT
**F78.1 said: read the raise, not the sentence. F79.1 said: read the instrument, not the
label on its output column. F79.2 says: READ THE UNITS.** Three faults in two sessions,
all the same species — a number carried forward under a name that did not describe it.