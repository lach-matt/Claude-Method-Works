# ADDENDUM S103 ITEM2 -- row 91 node q=0.95309 resolution. Filed+hashed BEFORE the two new solves.
# Lever: Richardson h=0.1/0.05 central at the node (new solves q=0.90309, 1.00309; q=0.85309,
# 1.05309 from cache). Rule B: sign-exact. Criteria:
#  (a) crossing REAL iff both h=0.2/0.1 and h=0.1/0.05 estimates < -2e-5 (filed falsifier). 
#  (b) stencil-STABLE small negative iff estimates agree within 2e-6 and both in (-2e-5, 0):
#      defect crosses near q~1 at row 91 by a small margin -- derived content, enter as such.
#  (c) NOISE iff estimates disagree by > 2e-6: node unresolved at SCF tol; residue stays open,
#      escalation = tighter SCF rung (next lever, not this addendum).