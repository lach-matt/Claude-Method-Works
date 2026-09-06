# AUDIT — ground_occ CALL SITES. R-D, ruled RUN by M at s74. Closes F73.3's audit request.
Instrument: pack74/goaudit3.py (v1, v2 withdrawn — see FAULT-F74.1.md). Rows: pack74/GOAUDIT3.jsonl

## THE COUNT
    sites            170   across 84 runtime files
    DEFINITION         1   t5_scf.py:23  `def ground_occ(Z): return [tuple(t) for t in G.expand(Z)]`
    IMPORT            80
    CONSTRUCT         88   in 82 files   <- CEILING, not a measurement (see F74.1)
    SCORE              0
    prose mention      1   rg.py L26, a docstring line
    nlchain.py         0   ZERO SITES

## THE TWO FINDINGS
**(1) THE DERIVATION CHAIN NEVER TOUCHES THE OBSERVED TABLE.** nlchain.py has ZERO ground_occ
sites. F73.3 asserted this; it is now measured independently. Deliverable 1 is unaffected,
confirmed and not merely restated.

**(2) F73.3 UNDERSTATED THE SPREAD, AND THAT IS NOT THE SAME AS UNDERSTATING THE RISK.**
F73.3 confined construct-side use to ci2b.py and rg.py. The audit finds the pattern in 82
files — every t7c_*, hf*, frozen_*, xseam*, frachf_* probe. **THIS IS NOT BY ITSELF A FAULT.**
A mechanism probe that asks "what does the field say AT the observed configuration" constructs
from observation by design and is not circular, because the claim it scores is not "the field
predicts the observed configuration". Circularity arises only where a construct-side site feeds
a SCORED claim.

## THE DECISIVE CROSS-REFERENCE
Of the 82 construct-side files, the number NAMED by DELIVERABLE-1-THE-ORDERING-CLAUSE.md or by
any of the 30 gate files is **ZERO**.
**STATED LIMIT, BECAUSE IT MATTERS:** this is a NAME MATCH, not a dependency trace. A gate that
consumes a .jsonl produced by a construct-side instrument would not be caught by it. Closing
that gap requires an output-provenance trace and is NOT done here and NOT claimed.

## WHAT IS OPEN FOR M
Whether the name-match suffices, or whether the output-provenance trace is ordered.