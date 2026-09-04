# PREDICTION — K-HALF AND THE GATE AS DOMAIN EDGE
# Session 69. Filed BEFORE any row is read. Instrument: pack69/kgate.py.
# Sealed data only (rt/nlchain.jsonl). NO SOLVES.

## ORIGIN
M's ruling, s69: item 6 (the l(l+1)/2 coincidence between t(l) and the defect
telescope) is what answers item 2 (what sets k).

## TIMING FLAG — MANDATORY, R 1449
Formed AFTER reading (a) Lambda_t's twelve cells and (b) s68's three binned
values of alpha/(l+1) = 0.5276, 0.5344, 0.5006. Those three numbers are
CONTAMINATED for P-1. NOT read: any per-row value, any scatter, any standard
error, any l=3 row, any gate split. P-2 and P-3 are clean.

## THE HYPOTHESIS UNDER TEST
  delta_0 - delta_l = k * l(l+1)/2 ,  with k = 1/2 EXACTLY,
  hence  alpha(l) = delta_l - delta_{l+1} = (l+1)/2 ,
  hence  delta_0 - delta_l = l(l+1)/4  with NO FITTED PARAMETER.

## P-1  IS k EXACTLY ONE HALF?
Pooled over every sealed row, alpha/(l+1) is consistent with 0.500 within its
own standard error, and the per-l residual shows NO monotone trend in l.
FALSIFIER: |mean - 0.500| > 2 s.e., OR the three per-l means are monotone in l.
Either kills k = 1/2 and returns k to a fitted constant.

## P-2  THE GATE IS THE DOMAIN EDGE  (clean)
Rows split by the R 1255 / PD-4 centrifugal gate on the ENTERING channel:
GATED means l >= l_core + 2, where l_core is the largest l occupied at Z-1.
PREDICTED: the (l+1) law holds on UNGATED rows and FAILS on GATED rows.
Quantitatively, median alpha/(l+1) on gated rows lies BELOW that on ungated
rows, and the gated set is the one carrying the scatter.
FALSIFIER: gated and ungated are indistinguishable -> the gate is not the edge,
the domain is unexplained, and item 6 supplies no boundary.

## P-3  l = 3 BREAKS THE LAW  (clean, out of sample)
alpha at l=3 is f->g. The linear law demands alpha(3) = 4k ~ 2.0-2.1.
P.lcollapse says the defect has already reached zero by f.
PREDICTED: alpha(l=3) < 1.0 where measurable, i.e. the law BREAKS at l=3, and
it breaks because f->g lies beyond the centrifugal gate for every atom in the
chain. NO-DATA is an acceptable outcome and is reported as NO-DATA.
FALSIFIER: alpha(l=3) ~ 2.0-2.1, which would mean the law continues past the
gate, delta does not reach zero by f, and P.lcollapse is contradicted.

## CAN-FAIL
kgate.py must be shown to fail in both directions before any row is scored:
a lever check that l actually moves the output, and a null scored against a
deliberately wrong k. rc=4 if either check is dead.

## CARRIED CAVEAT — F67.4, NOT TO BE DROPPED
The sealed rows are a filtered subset (survival 50.0% / 11.3% / 7.1% by l).
Per-row readings are unaffected; any POPULATION claim inherits the bias and
must say so.