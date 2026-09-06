#!/usr/bin/env python3
"""canary.py -- THE ENVIRONMENT DRIFT CHECK (s58).

Replaces the 71-gate replay at open.

WHY THE REPLAY WAS REDUNDANT.  A clean manifest proves the bytes are identical.
Identical bytes plus deterministic code produce identical output.  Re-running 71
gates to confirm what the hash already proved re-proves the code, not the
environment -- and the code is what the hash covers.

WHAT A HASH CANNOT COVER: the compiler, the interpreter, libm, numpy.  That is
the only thing the replay ever added, and it needs ONE probe, not seventy-one.

    python3 pack58/canary.py --emit    # write the reference (seal time, once)
    python3 pack58/canary.py           # check against it (every open)

Probes, cheapest first, each sensitive to a different layer:
    1. float/libm      -- IEEE arithmetic and transcendentals
    2. kernel dlopen   -- all three .so load and expose their entry points
    3. numpy           -- linear algebra reproducibility
    4. physics         -- nlterm gate: the full chain to 6 decimals
"""
import sys, os, json, math, subprocess, hashlib

REF = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CANARY-REF.json')


def probe_float():
    v = [math.sqrt(2.0), math.exp(1.0), math.log(7.0), math.sin(1.0),
         math.pow(1.0000001, 1e6), sum(0.1 for _ in range(10)) - 1.0]
    return hashlib.sha256(repr([float.hex(x) for x in v]).encode()).hexdigest()[:16]


def probe_kernel(rt):
    import ctypes
    out = []
    for k in ('libshoot.so', 'libshoot_sr.so', 'libshoot_x.so'):
        p = os.path.join(rt, k)
        if not os.path.exists(p):
            out.append('%s:MISSING' % k); continue
        try:
            lib = ctypes.CDLL(p)
            names = [n for n in ('shoot', 'shoot_sr', 'shoot_x', 'integrate', 'solve')
                     if hasattr(lib, n)]
            out.append('%s:OK:%s' % (k, ','.join(names) or 'none'))
        except OSError as e:
            out.append('%s:LOADFAIL' % k)
    return '|'.join(out)


def probe_numpy():
    try:
        import numpy as np
    except ImportError:
        return 'NONUMPY'
    a = np.arange(1, 26, dtype=float).reshape(5, 5) + np.eye(5) * 13.0
    w = np.linalg.eigvalsh(a + a.T)
    return hashlib.sha256(np.round(w, 9).tobytes()).hexdigest()[:16]


def probe_physics(rt):
    try:
        r = subprocess.run([sys.executable, 'nlterm.py', 'gate'], cwd=rt,
                           capture_output=True, text=True, timeout=300)
    except Exception as e:
        return 'RUNFAIL:%s' % type(e).__name__
    if r.returncode != 0:
        return 'RC%d' % r.returncode
    for ln in r.stdout.splitlines():
        if 'sum_dets' in ln:
            return ln.strip()
    return 'NOLINE'


def collect():
    here = os.path.dirname(os.path.abspath(__file__))
    rt = os.path.abspath(os.path.join(here, '..', 'rt'))
    return {
        'float': probe_float(),
        'kernel': probe_kernel(rt),
        'numpy': probe_numpy(),
        'physics': probe_physics(rt),
    }


def main():
    emit = '--emit' in sys.argv
    got = collect()
    if emit:
        json.dump(got, open(REF, 'w'), indent=1, sort_keys=True)
        print('CANARY-REF written:')
        for k in sorted(got):
            print('  %-8s %s' % (k, got[k]))
        return 0
    if not os.path.exists(REF):
        print('CANARY: no reference. Run --emit at seal time.'); return 1
    ref = json.load(open(REF))
    bad = [k for k in sorted(ref) if ref[k] != got.get(k)]
    for k in sorted(ref):
        print('  %-8s %s' % (k, 'OK' if k not in bad else 'DRIFT'))
    if bad:
        for k in bad:
            print('    %s\n      sealed : %s\n      now    : %s' % (k, ref[k], got.get(k)))
        print('CANARY: ENVIRONMENT DRIFT. The bytes are sealed but the machine changed.')
        print('  Only now is a full gate replay warranted: pack55/gates_run55.sh 1 71')
        return 1
    print('CANARY: CLEAN -- environment reproduces the sealed reference.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
