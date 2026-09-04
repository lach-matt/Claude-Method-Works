#!/usr/bin/env python3
"""doubt82.py -- THE R82.2 HARNESS. BUILT AT s82. **FIRST EXERCISE ORDERED AT s83.**

R82.2: a control must be sited where the instrument is DOUBTED, not where it is TRUSTED.

Basis, measured (F82.2): the target-node search recovered 6d exactly, to nine digits, at
every field it was ever pointed at -- and cannot see any state above the valence
eigenvalue.  Three sessions of passing controls, all sited at 6d, in the one region where
the instrument works.

WHAT THIS ENFORCES, AND WHAT IT DELIBERATELY DOES NOT:
  * It enforces that the domain is DECLARED, that a control EXISTS in the doubted region,
    that its expectation was filed BEFORE it ran, and that the run HALTS if no such
    control can be built.
  * **IT DOES NOT DECIDE WHERE THE DOUBT LIES.**  That is a physical judgement and the
    harness must not pretend to make it.  What the harness guarantees is that the
    judgement was WRITTEN DOWN and then TESTED, not that it was correct.  A wrong doubt
    region declared honestly is recoverable; an undeclared one is what F82.2 was.
  * A doubt-sited control MAY FAIL.  Failure restricts the result to the trusted region
    and is reported.  **Only NOT LOOKING is forbidden** (R82.2 clause 5).

RETURN CODES
  0  all controls ran; verdicts reported
  5  **NO DOUBT-SITED CONTROL COULD BE CONSTRUCTED.**  R82.2 clause 4.  The impossibility
     is the finding.  This is NOT an error to be worked around.
  6  a doubt-sited control's expectation was not filed before it ran (R82.2 clause 3)
  7  the domain was not declared (R82.2 clause 1)

usage, as a library:

    D = Domain('conf82 l=2 census',
               trusted='E <= eps(valence): the channel carrying the SCF solution',
               doubted='E > eps(valence): every state shallower than valence, where the '
                       'matching function has never been shown to return to zero')
    D.control('6d recovers SCF eps to 1 mHa', region='trusted',
              expect='diff < 1.0 mHa', filed_in='PREDICTION-...md')
    D.control('inward-matched 7d against a hydrogenic quantum-defect estimate',
              region='doubted', expect='eps in [-14, -9] mHa', filed_in='PREDICTION-...md')
    D.gate()                      # halts unless R82.2 is satisfied
    ... run the question rows ...
    D.record('6d ...', True, '0.000000 mHa')
    D.record('inward-matched 7d ...', False, 'no inward solution')
    print(D.report())             # trusted/doubted verdicts, and the scope of the claim
"""
import os, sys, json, hashlib, time

VERSION = 'R82.2 harness, s82, unexercised'


class Domain:
    def __init__(self, name, trusted=None, doubted=None, log=None):
        self.name = name
        self.trusted = trusted
        self.doubted = doubted
        self.controls = []
        self.results = {}
        self.log = log
        self.t0 = time.time()

    # ---- R82.2 clause 1
    def _declared(self):
        return bool(self.trusted and self.doubted)

    # ---- R82.2 clauses 2 and 3
    def control(self, label, region, expect, filed_in=None, sha_of=None):
        """A control.  `region` is 'trusted' or 'doubted'.  `expect` is the answer stated
        BEFORE the run.  `filed_in` names the hashed prediction carrying it."""
        if region not in ('trusted', 'doubted'):
            raise ValueError("region must be 'trusted' or 'doubted'")
        sha = None
        if sha_of and os.path.exists(sha_of):
            sha = hashlib.sha256(open(sha_of, 'rb').read()).hexdigest()
        self.controls.append(dict(label=label, region=region, expect=expect,
                                  filed_in=filed_in, sha=sha))
        return self

    # ---- R82.2 clause 4: the gate
    def gate(self, allow_impossible=False, impossibility_note=None):
        """Halts unless R82.2 is satisfied.  If NO doubt-sited control can be built, the
        caller must say so EXPLICITLY via allow_impossible with a written reason -- and
        the run still halts at rc=5.  The note is what gets recorded as the finding."""
        if not self._declared():
            print("HALT rc=7 (R82.2 clause 1): the domain was not declared.")
            print("  Both a TRUSTED and a DOUBTED region must be named in the source.")
            sys.exit(7)

        doubt = [c for c in self.controls if c['region'] == 'doubted']
        for c in self.controls:
            if not c['filed_in']:
                print(f"HALT rc=6 (R82.2 clause 3): control {c['label']!r} carries no "
                      f"filed expectation. An expectation formed after the output is not "
                      f"a control.")
                sys.exit(6)

        if not doubt:
            print("=" * 72)
            print("HALT rc=5 (R82.2 clause 4): NO DOUBT-SITED CONTROL.")
            print(f"  instrument : {self.name}")
            print(f"  trusted    : {self.trusted}")
            print(f"  DOUBTED    : {self.doubted}")
            print(f"  controls   : {len(self.controls)}, all in the trusted region")
            if impossibility_note:
                print(f"\n  DECLARED IMPOSSIBILITY:\n    {impossibility_note}")
                print("\n  **THIS IS THE FINDING. RECORD IT AS ONE.**")
                print("  The instrument's reach in the doubted region cannot be "
                      "established,")
                print("  and every claim it makes there is unsupported regardless of how "
                      "many")
                print("  trusted-region controls pass. This is F82.2, stated in advance "
                      "instead")
                print("  of discovered three sessions later.")
            else:
                print("\n  No impossibility note was written. If a doubt-sited control "
                      "genuinely")
                print("  cannot be constructed, SAY WHY -- that sentence is the result.")
            print("=" * 72)
            sys.exit(5)

        print(f"  R82.2 GATE PASS · {len(self.controls)} control(s): "
              f"{len(self.controls) - len(doubt)} trusted, **{len(doubt)} DOUBT-SITED**")
        for c in doubt:
            print(f"      doubted: {c['label']}  -- expected {c['expect']} "
                  f"({c['filed_in']})")
        return self

    def record(self, label, passed, measured):
        self.results[label] = dict(passed=bool(passed), measured=measured)
        return self

    # ---- R82.2 clause 5
    def report(self):
        out = [f"=== R82.2 CONTROL REPORT · {self.name} ===",
               f"  TRUSTED : {self.trusted}",
               f"  DOUBTED : {self.doubted}"]
        dt, df = [], []
        for c in self.controls:
            r = self.results.get(c['label'])
            v = 'NOT RUN' if r is None else ('PASS' if r['passed'] else '**FAIL**')
            m = '' if r is None else f"  measured {r['measured']}"
            out.append(f"  [{c['region']:>7}] {v:9s} {c['label']}{m}")
            (dt if c['region'] == 'trusted' else df).append(r)
        bad = [r for r in df if r is not None and not r['passed']]
        miss = [r for r in df if r is None]
        if miss:
            out.append("  **A DOUBT-SITED CONTROL WAS DECLARED AND NOT RUN. "
                       "THE RESULT IS NOT SCOREABLE.**")
        elif bad:
            out.append("  **THE DOUBT-SITED CONTROL FAILED.** Under R82.2 clause 5 this "
                       "does not")
            out.append("  void the result -- IT RESTRICTS IT. Every claim below is "
                       "limited to the")
            out.append("  TRUSTED region and must say so. Reporting the failure is the "
                       "compliance.")
        else:
            out.append("  Doubt-sited control(s) PASSED. The instrument's reach is "
                       "demonstrated")
            out.append("  in the region where it was doubted -- not merely where it was "
                       "trusted.")
        return "\n".join(out)

    def dump(self, path):
        json.dump(dict(name=self.name, trusted=self.trusted, doubted=self.doubted,
                       controls=self.controls, results=self.results,
                       version=VERSION, sec=int(time.time() - self.t0)),
                  open(path, 'w'), indent=1)


# ---- the harness's own can-fails.  It must halt when it should and pass when it should.
def _selftest():
    import subprocess
    print("=== doubt82 SELF-TEST: the harness must HALT correctly ===")
    cases = [
        ("no domain declared", 7,
         "D=Domain('x'); D.gate()"),
        ("control with no filed expectation", 6,
         "D=Domain('x',trusted='a',doubted='b');"
         "D.control('c','doubted','e',filed_in=None); D.gate()"),
        ("trusted-region controls ONLY -- **THE F82.2 CASE**", 5,
         "D=Domain('x',trusted='a',doubted='b');"
         "D.control('c','trusted','e',filed_in='P.md');"
         "D.gate(impossibility_note='none can be built')"),
        ("compliant", 0,
         "D=Domain('x',trusted='a',doubted='b');"
         "D.control('c','trusted','e',filed_in='P.md');"
         "D.control('d','doubted','e',filed_in='P.md'); D.gate()"),
    ]
    ok = True
    for label, want, body in cases:
        src = f"import sys; sys.path.insert(0,{os.path.dirname(os.path.abspath(__file__))!r})\n" \
              f"from doubt82 import Domain\n{body}\n"
        rc = subprocess.run([sys.executable, '-c', src],
                            capture_output=True, text=True).returncode
        good = rc == want
        ok &= good
        print(f"  {label:48s} rc={rc} want={want}  {'PASS' if good else '**FAIL**'}")
    print(f"\n  SELF-TEST: {'PASS' if ok else '**FAIL**'}")
    print("  **NOTE: this exercises the HARNESS, not any physical instrument.**")
    print("  R82.2's first real exercise is ordered at s83.")
    return 0 if ok else 1


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'selftest':
        sys.exit(_selftest())
    print(__doc__)
