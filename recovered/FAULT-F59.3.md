# F59.3 — BLOCKING. THE c=1e6 WALK WAS RUN AT c = 137.035999.
# Session 59. Registered BEFORE any result was interpreted (Zeno: close flags first).

## THE FAULT
`cinf.py` sets c by rebinding the DEFAULT ARGUMENT of three kernel functions:

    for name in ('eigen_sr','numerov_wf_sr','scf_occ_sr'):  f.__defaults__ = (... c ...)

The HF solve never consults those defaults. `t7c_hfsr.py`:

    line  6   from t7c_kernel import qlog, eigen_sr, _derivs, C0
    line  8   def __init__(self, Z, occ, npts=4000, c=C0, srcM=True)
    line  9   self.c = c
    line 39   eh = float(eigen_sr(Vf, l, n, 1.0, self.Z, c, Vp=Vpf, Vpp=Vppf))

`C0` is bound into t7c_hfsr's namespace AT IMPORT. `HFSR.__init__` carries its OWN
default `c=C0`, and line 39 passes it POSITIONALLY. A patched default is unreachable.
`hfc2.py` line 84 likewise constructs `HFC(Z, occ, c=C0)` explicitly.

## PROOF, TWO INDEPENDENT WAYS
1. DIRECT. Apply cinf.patch(1e6) verbatim, then instantiate:
       patched defaults: 3
       HFSR instance self.c AFTER PATCH = 137.035999      <-- unmoved
2. EMPIRICAL. Five restart rows computed this session at the default c reproduce
   pack53/cinf.jsonl BIT-FOR-BIT in D_ent, margin and the full order list, at all of
   Z = 42,43,45,46,79 -- INCLUDING GOLD. The kernel, when c does reach it, moves the
   Z=79 1s level by 314.08 Ha (and Z=42 by 21.75 Ha). Zero shift is impossible unless
   c never varied.

## WHY THE PROBE GAVE FALSE CONFIDENCE
`cinf.py probe` calls `K.eigen_sr(V,0,1,1.0,Z)` with NO c -- the one call site in the
whole program that DOES use the default. The probe exercised the patch; the walk did not.
The instrument was validated on a path the physics never takes.

## WHAT THIS VOIDS
    pack53/cinf.jsonl        107 rows. NOT a non-relativistic walk. It is a RESTART-mode
                             walk at c = 137.035999. Its 'clight': 1e6 field is FALSE.
    pack53/ctrl137.jsonl     Was intended as the c-control against it. Both sides are at
                             the same c, so CT-1's "same entrant" was true BY
                             CONSTRUCTION, not measured. NR-4 CANNOT be released.
    DELIVERABLE-5 §4         NR-1/NR-2/NR-4/NR-5 are properties of RESTART MODE, not of c.
    pack53/induct.jsonl,     mode 'cinf-chainref' -- same driver, presumed same fault,
    pack54/induct34.jsonl    NOT yet verified. Owed.
    CLAUSE 3                 DOES NOT CLOSE. The c-dependence of the ordering clause is
                             UNMEASURED over the whole table.

## WHAT SURVIVES, AND IT IS NOT NOTHING
The 94/107 IMMUNITY THEOREM (Deliverable 5 §1) is combinatorial -- a statement about
which channels share n+l -- and does not depend on c or on any walk. La(57) and Ac(89)
remain IMMUNE. That result stands untouched.

## REMEDY, NOT YET APPLIED
Rebind c where it is actually read, and CAN-FAIL it before trusting it:
  * set t7c_hfsr.C0 AND HFSR.__init__.__defaults__, AND hfc2.C0, before nlchain imports;
  * ASSERT HFSR(2,[(1,0,2.0)]).c == target and REFUSE to walk if not;
  * CAN-FAIL: the corrected patch MUST move Z=79's D_ent. A patch that changes nothing
    is the fault, not the fix. No sealed file is edited (F44.1 precedent).