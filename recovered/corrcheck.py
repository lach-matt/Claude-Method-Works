"""corrcheck.py -- s60. CAN-FAIL FOR THE CLAIM "THE RULING WALK RUNS WITH CORRELATION OFF".

WHY THIS EXISTS. Deliverable 1 and every Clause-1 statement rest on the ruling field being
E_HF with CORR=False -- because the correlation branch (hfc2.eps_c / corr_pot / E_c) is a
Gell-Mann-Brueckner high-density functional, and its coefficients are NOT derived in this
chain. If it executes, the no-fitted-constants claim is dead. The claim is currently
carried by ONE LINE: nlchain.py:17  H.CORR = False.

F59.3's lesson, standing rule s59 §7.7: a control must be PROVEN to vary the thing it
controls for. `H.CORR = False` sets a module global; `C0` also looked like it was being
set and was not, because run2's sibling call site read a value bound at import instead.
CORR is read as a bare global INSIDE run2, which SHOULD resolve at call time -- but
"should" is exactly what F59.3 punished. So this script does not read the source. It
counts executions on the real path.

NO SEALED FILE IS TOUCHED (F44.1): the counters are wrappers rebound in memory.

PATH UNDER TEST is the walk's own: nlguard.run_guarded -> H.HFC(...).run2(...).
Not a hand-built HFC call -- the same function nlchain.step calls for every channel.

usage: python3 pack60/corrcheck.py
"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))

CNT = {'corr_pot': 0, 'E_c': 0}

def instrument(H):
    ocp, oec = H.HFC.corr_pot, H.HFC.E_c
    def cp(self, P):
        CNT['corr_pot'] += 1
        return ocp(self, P)
    def ec(self, P):
        CNT['E_c'] += 1
        return oec(self, P)
    H.HFC.corr_pot, H.HFC.E_c = cp, ec

def reset():
    CNT['corr_pot'] = 0; CNT['E_c'] = 0

def solve(NG, Z, cfg):
    g = NG.run_guarded(Z, cfg, 'corrcheck')
    if not g['conv']:
        raise SystemExit("REFUSE: reference did not converge -- %s" % g['err'])
    return g['E']

CASES = [(4, [(1, 0, 2.0), (2, 0, 2.0)]),
         (12, [(1, 0, 2.0), (2, 0, 2.0), (2, 1, 6.0), (3, 0, 2.0)])]

if __name__ == '__main__':
    # PHASE 0 -- import exactly as the walk does. nlchain.py:17 runs on import.
    import nlchain as NC          # sets H.CORR = False as a side effect of import
    import hfc2 as H
    import nlguard as NG
    print("PHASE 0  import nlchain (the walk's own import)")
    print("         hfc2.CORR after import      = %r" % H.CORR)
    print("         nlguard's H is hfc2         = %s" % (NG.H is H))
    if H.CORR is not False:
        raise SystemExit("REFUSE: importing nlchain did not set hfc2.CORR False (got %r)" % H.CORR)

    instrument(H)
    results = {}

    # PHASE 1 -- CORR False. The correlation branch must NEVER be entered.
    print("\nPHASE 1  CORR=False  (the ruling walk)")
    H.CORR = False
    for Z, cfg in CASES:
        reset(); t = time.time()
        E = solve(NG, Z, cfg)
        results[('off', Z)] = E
        print("   Z=%-3d E=%14.6f  corr_pot calls=%d  E_c calls=%d  (%.1fs)"
              % (Z, E, CNT['corr_pot'], CNT['E_c'], time.time() - t))
        if CNT['corr_pot'] or CNT['E_c']:
            raise SystemExit("FAIL DIRECTION 1: correlation EXECUTED with CORR=False at Z=%d" % Z)

    # PHASE 2 -- CORR True. The branch MUST be entered and MUST move the energy.
    # This is the half F59.3 skipped: proving the switch controls what it claims to.
    print("\nPHASE 2  CORR=True   (the control must vary the thing it controls for)")
    H.CORR = True
    for Z, cfg in CASES:
        reset(); t = time.time()
        E = solve(NG, Z, cfg)
        results[('on', Z)] = E
        d = E - results[('off', Z)]
        print("   Z=%-3d E=%14.6f  corr_pot calls=%d  E_c calls=%d  dE=%+.6f Ha  (%.1fs)"
              % (Z, E, CNT['corr_pot'], CNT['E_c'], d, time.time() - t))
        if CNT['corr_pot'] == 0:
            raise SystemExit("FAIL DIRECTION 2: CORR=True did NOT enter corr_pot at Z=%d "
                             "-- the switch is a no-op and this whole check is blind" % Z)
        if d == 0.0:
            raise SystemExit("FAIL DIRECTION 2: CORR=True changed NOTHING at Z=%d "
                             "-- F59.3's exact signature" % Z)

    # PHASE 3 -- back off. Must return to the phase-1 number EXACTLY, not approximately.
    print("\nPHASE 3  CORR=False again  (reversible, and bit-exact)")
    H.CORR = False
    for Z, cfg in CASES:
        reset()
        E = solve(NG, Z, cfg)
        same = (E == results[('off', Z)])
        print("   Z=%-3d E=%14.6f  corr_pot calls=%d  identical to PHASE 1: %s"
              % (Z, E, CNT['corr_pot'], "YES" if same else "NO"))
        if CNT['corr_pot'] or not same:
            raise SystemExit("FAIL DIRECTION 3: state did not restore at Z=%d" % Z)

    print("\nCORRCHECK: PASS -- CORR=False is REAL on the walk's own path, CORR=True bites,")
    print("           and the switch is reversible bit-exactly.")
    print("           The ruling field is E_HF with NO correlation functional executed.")
