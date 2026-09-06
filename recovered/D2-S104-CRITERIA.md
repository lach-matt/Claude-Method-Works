# D2-S104-CRITERIA -- locate the persistent I-matrix asymmetry in the VALENCE-ONLY basis (6s and
# 5s shells, row 58) before designing branch B's repair. Filed and hashed pre-run.
# Probe: recompute M unsymmetrized per w104's build; report every element pair (u,v) with
# |M[u,v]-M[v,u]| and each state's eigen-relation residual norm ||(H-eps)P||.
# DECISION RULE (stated before running):
#   (a) If the dominant asym pair involves an ENDPOINT hybrid (m or p) whose eigen-relation
#       residual > 1e-8, the T-action gate is violated at the endpoints -> branch B repair =
#       direct-grid T-action for endpoint rows/cols only.
#   (b) If residuals are all <= 1e-10 yet asym ~ 1e-4 persists, the asymmetry is operator
#       INHOMOGENEITY (Taction(hp,.) vs Taction(h5,.) use different SCF potentials; exact-T
#       identity holds per state, so the discrepancy is X/Vloc bookkeeping across hybrids)
#       -> branch B repair = evaluate all T-actions at the SINGLE h5 potential via
#       T P = (eps5 - Vloc5) P + X5-form applied to the foreign orbital... NOT valid; instead
#       repair = one-body I via direct kinetic quadrature <u'|v'>/2 + l(l+1)<u|r^-2|v>/2
#       (integration by parts; symmetric BY CONSTRUCTION; scalar-relativistic correction
#       enters only through the sealed kernel comparison and is scored, not assumed).
#   Comparison decides between (a)-repair and (b)-repair by whichever drives asym to
#   discretization level AND is scored against the 4 sealed chords (|d| <= 1e-8 to stand).
# This is a diagnostic: no prediction on the residual's fate is made here.