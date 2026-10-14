#!/usr/bin/env python3
"""
F53.1 REMEDY -- pack53/runsealed.py

FAULT: pack52/gate86.py and pack52/cinf.py both hard-code the SESSION 52 extraction
path '/home/claude/s52/LOWDIN-HANDOFF-51/rt' in a sys.path.insert and an os.chdir.
Neither can run from a fresh extract. open52.sh HALTED at step 4 on gate 86.

REMEDY CLASS: F44.1 precedent -- the sealed file is NOT edited. Its source is read,
the ONE stale path literal is rebound to this extract's rt/, and the result is exec'd
in memory. The bytes on disk are untouched and still hash to the sealed manifest.

DISCIPLINE:
  * the substitution is asserted to be EXACTLY the path literal and nothing else:
    source with the literal blanked must be byte-identical before and after.
  * the sha256 of the sealed file is printed on every run, so the object being run
    is always named by its seal, not by its filename.
  * the target rt/ must contain nlchain.py, or this refuses -- a wrapper that
    silently runs against the wrong tree is worse than the fault it remedies.

USAGE:  python3 pack53/runsealed.py <sealed.py> [args...]     (run from archive root)
"""
import sys, os, hashlib, io

STALE = '/home/claude/s52/LOWDIN-HANDOFF-51/rt'

def main():
    if len(sys.argv) < 2:
        print("usage: runsealed.py <sealed.py> [args...]"); return 2
    sealed = os.path.abspath(sys.argv[1])
    root   = os.path.dirname(os.path.dirname(sealed))       # archive root
    rt     = os.path.join(root, 'rt')

    if not os.path.isfile(os.path.join(rt, 'nlchain.py')):
        print("REFUSE: %s is not a built runtime (no nlchain.py)" % rt); return 3

    raw = open(sealed, 'rb').read()
    dig = hashlib.sha256(raw).hexdigest()
    src = raw.decode()

    n = src.count(STALE)
    if n == 0:
        print("NOTE: no stale path in this file; running it unmodified.")
    patched = src.replace(STALE, rt)

    # PROOF the rebinding touched nothing else: blank the literal in both and compare.
    if src.replace(STALE, '\x00') != patched.replace(rt, '\x00'):
        print("REFUSE: substitution altered something other than the path literal"); return 4

    print("RUNSEALED %s  sha256=%s  paths rebound=%d -> %s"
          % (os.path.basename(sealed), dig[:12], n, rt))
    sys.stdout.flush()

    g = {'__name__': '__main__', '__file__': sealed}
    sys.argv = [sealed] + sys.argv[2:]
    try:
        exec(compile(patched, sealed, 'exec'), g)
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
    return 0

if __name__ == '__main__':
    sys.exit(main())
