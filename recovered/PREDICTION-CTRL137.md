# PREDICTION — THE RESTART CONTROL AT c = 137.035999 (F53.2 RESOLUTION)
# Filed 2026-08-20T03:0xZ, BEFORE any control row is computed or read. R 1449.
# Instrument: the SEALED nlchain.py in 'restart' mode, unpatched, c at its default
# 137.035999. Same reference configuration as cinf.py -- OBSERVED config(Z-1) -- so the
# ONLY difference between the control and the c=1e6 walk is c itself.
#
# WHY: gate 87 found the c=1e6 restart walk disagreeing with the sealed CHAINED walk at
# 11 steps and showing 5 ordering failures and 4 extra tie-break failures. Every one of
# those steps carries a reference configuration that differs between the two walks, so
# NONE of them is attributable to c. This control removes the confound at exactly the
# disputed steps. Z = 25 30 47 48 60 61 62 71 80 103 104.

CT-1  DECISIVE. At all 11 steps the control returns the SAME entrant as the c=1e6 walk.
      Reading: the 11 disagreements are borne by the REFERENCE CONFIGURATION, not by c,
      and the count of c-attributed entrant changes over Z=2..108 is ZERO.
      If instead any step returns a DIFFERENT entrant from the c=1e6 walk, that step IS
      a c effect, NR-4 becomes scoreable on it, and it must be reported as such.

CT-2  The five ordering failures at Z = 42 43 45 46 79 are reference-set artefacts and
      would reproduce in the control were it run there: at each, the offending channel
      (5s, 5s, 5s, 5s, 6s) is HALF-OCCUPIED in the observed reference and FULL in the
      chained one, so it is admissible in one walk and absent from the other. This is a
      statement about configurations and holds independently of c.

CT-3  The four extra tie-break failures at Z = 60 61 62 103 are likewise reference-set:
      4f carries one MORE electron in the observed reference than in the chained one at
      60-62, and 6d carries two FEWER at 103.

CT-4  No control step fails to converge; all return at rung 0.

SCORING: CT-1 decides whether NR-4 can be released from HELD. A clause reworded to pass
is FALSIFIED and recorded as such. The control does NOT rescue NR-1, which is stated
over the whole chain and can only be tested by a CHAINED c=1e6 walk.
