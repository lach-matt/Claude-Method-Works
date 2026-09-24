"""cinf.py -- CLAUSE 3 DRIVER. Re-walks the chain in the NON-RELATIVISTIC LIMIT c -> inf.
NO SEALED FILE IS TOUCHED (F44.1 precedent). c is a DEFAULT ARGUMENT on the SR kernel
functions; this rebinds those defaults in memory before nlchain is imported.
usage: python3 cinf.py probe Z        -- single-Z depth comparison, no chain
       python3 cinf.py walk Z0 Z1 OUT -- chain rows Z0..Z1 at c=1e6 -> OUT.jsonl
"""
import sys, os, json, time
sys.path.insert(0, '/home/claude/s52/LOWDIN-HANDOFF-51/rt')
os.chdir('/home/claude/s52/LOWDIN-HANDOFF-51/rt')
CINF = 1e6

def patch(c):
    import t7c_kernel as K
    n = 0
    for name in ('eigen_sr', 'numerov_wf_sr', 'scf_occ_sr'):
        f = getattr(K, name)
        d = list(f.__defaults__)
        co = f.__code__
        names = co.co_varnames[:co.co_argcount]
        off = co.co_argcount - len(d)
        for i, nm in enumerate(names[off:]):
            if nm == 'c':
                d[i] = c; n += 1
        f.__defaults__ = tuple(d)
    return n

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'probe':
        Z = int(a[1])
        import t7c_kernel as K
        import numpy as np
        V = lambda r: -Z / np.asarray(r, float)
        rel = K.eigen_sr(V, 0, 1, 1.0, Z)
        n = patch(CINF)
        nr = K.eigen_sr(V, 0, 1, 1.0, Z)
        e_nr = -Z * Z / 2.0
        print('Z=%d  patched %d defaults' % (Z, n))
        print('  1s  c=137.035999 : %.8f' % (rel if not hasattr(rel,'__len__') else rel[0]))
        print('  1s  c=1e6        : %.8f' % (nr  if not hasattr(nr,'__len__')  else nr[0]))
        print('  1s  exact -Z^2/2 : %.8f' % e_nr)
        sys.exit(0)
    if a and a[0] == 'walk':
        Z0, Z1, out = int(a[1]), int(a[2]), a[3]
        patch(CINF)
        import nlchain as NC, ground as G
        rows = NC.load()
        fh = open(out, 'a')
        for Z in range(Z0, Z1 + 1):
            t = time.time()
            # each step is INDEPENDENT of the c=1e6 predecessor: the reference config for
            # Z-1 is the OBSERVED one, exactly as the sealed walk does at 'restart'.
            r = NC.step(Z, G.expand(Z - 1), rows, 'cinf')
            r['sec'] = round(time.time() - t, 1); r['clight'] = CINF
            fh.write(json.dumps(r) + '\n'); fh.flush()
            print('DONE Z=%d ent=%s sec=%s' % (Z, r.get('ent'), r['sec']), flush=True)
        fh.close()
