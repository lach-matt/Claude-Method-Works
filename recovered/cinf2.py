"""cinf2.py -- F59.3 REMEDY. Sets c WHERE IT IS ACTUALLY READ.
NO SEALED FILE IS TOUCHED (F44.1 precedent): this rebinds module globals and
__defaults__ in memory, before nlchain is imported.

WHY cinf.py FAILED: it patched only the kernel functions' __defaults__.
t7c_hfsr.HFSR.__init__ carries its OWN default c=C0 (bound at import) and passes it
POSITIONALLY to eigen_sr, so the patched default is never consulted.

usage: python3 pack59/cinf2.py canfail          -- prove the patch bites. RUN THIS FIRST.
       python3 pack59/cinf2.py walk Z0 Z1 OUT   -- restart-mode rows Z0..Z1 at c=CINF
       python3 pack59/cinf2.py rows OUT Z...    -- restart-mode rows at an explicit Z LIST
"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
CINF = 1e6

def patch(c):
    import t7c_kernel as K, t7c_hfsr as HS, hfc2 as H
    n = 0
    for name in ('eigen_sr', 'numerov_wf_sr', 'scf_occ_sr'):      # the old patch
        f = getattr(K, name); d = list(f.__defaults__); co = f.__code__
        names = co.co_varnames[:co.co_argcount]; off = co.co_argcount - len(d)
        for i, nm in enumerate(names[off:]):
            if nm == 'c': d[i] = c; n += 1
        f.__defaults__ = tuple(d)
    K.C0 = HS.C0 = H.C0 = c                                       # the module globals
    ini = HS.HFSR.__init__                                        # HFSR's OWN default
    d = list(ini.__defaults__); co = ini.__code__
    names = co.co_varnames[:co.co_argcount]; off = co.co_argcount - len(d)
    for i, nm in enumerate(names[off:]):
        if nm == 'c': d[i] = c; n += 1
    ini.__defaults__ = tuple(d)
    # REFUSE TO PROCEED unless c reached the object the physics actually uses.
    got = HS.HFSR(2, [(1, 0, 2.0)]).c
    if got != c:
        raise SystemExit("REFUSE: patch did not reach HFSR.self.c (%r != %r)" % (got, c))
    print("PATCH OK  sites=%d  HFSR.self.c=%r" % (n, got))
    return n

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'canfail':
        import numpy as np, t7c_kernel as K, t7c_hfsr as HS
        print("--- BEFORE PATCH ---")
        print("  HFSR.self.c =", HS.HFSR(2, [(1, 0, 2.0)]).c)
        assert HS.HFSR(2, [(1, 0, 2.0)]).c == 137.035999, "baseline is not c=137.035999"
        patch(CINF)
        print("--- AFTER PATCH ---")
        ok = True
        for Z in (42, 79):
            V = lambda r: -Z / np.asarray(r, float)
            e1 = K.eigen_sr(V, 0, 1, 1.0, Z, 137.035999)
            e2 = K.eigen_sr(V, 0, 1, 1.0, Z, CINF)
            e1 = float(e1 if not hasattr(e1, '__len__') else e1[0])
            e2 = float(e2 if not hasattr(e2, '__len__') else e2[0])
            shift = e1 - e2
            print("  Z=%-3d 1s shift c=137 vs c=1e6 : %10.4f Ha   (exact -Z^2/2 = %.2f)"
                  % (Z, shift, -Z * Z / 2))
            if abs(shift) < 1.0: ok = False
        print("CANFAIL:", "PASS -- c moves the physics" if ok
              else "FAIL -- patch changes nothing, this IS the fault")
        sys.exit(0 if ok else 1)
    if a and a[0] in ('walk', 'rows'):
        patch(CINF)
        import nlchain as NC, ground as G
        rows = NC.load()
        if a[0] == 'walk': out, Zs = a[3], list(range(int(a[1]), int(a[2]) + 1))
        else:              out, Zs = a[1], [int(x) for x in a[2:]]
        fh = open(out, 'a')
        for Z in Zs:
            t = time.time()
            r = NC.step(Z, G.expand(Z - 1), rows, 'cinf2')
            r['sec'] = round(time.time() - t, 1); r['clight'] = CINF
            fh.write(json.dumps(r) + '\n'); fh.flush()
            print('DONE Z=%d ent=%s sec=%s' % (Z, r.get('ent'), r['sec']), flush=True)
        fh.close()