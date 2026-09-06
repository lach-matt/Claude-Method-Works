"""induct.py -- s53. THE INDUCTION TEST FOR CLAUSE 3.
Walks the 34 confounded steps at c=1e6 ON THE CHAINED REFERENCE cfg_from_chain(Z-1).
c is rebound as a DEFAULT ARGUMENT in memory; NO SEALED FILE IS TOUCHED (F44.1).
The patch() body is pack52/cinf.py's, reused deliberately so the two walks differ in
nothing but the reference configuration.
usage: python3 induct.py OUT Z...
"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
CINF = 1e6

def patch(c):
    import t7c_kernel as K
    n = 0
    for name in ('eigen_sr', 'numerov_wf_sr', 'scf_occ_sr'):
        f = getattr(K, name); d = list(f.__defaults__); co = f.__code__
        names = co.co_varnames[:co.co_argcount]; off = co.co_argcount - len(d)
        for i, nm in enumerate(names[off:]):
            if nm == 'c': d[i] = c; n += 1
        f.__defaults__ = tuple(d)
    return n

if __name__ == '__main__':
    out = sys.argv[1]; ZS = [int(z) for z in sys.argv[2:]]
    n = patch(CINF); print('patched %d defaults to c=%g' % (n, CINF), flush=True)
    import nlchain as NC
    rows = NC.load()
    fh = open(out, 'a')
    for Z in ZS:
        t = time.time()
        r = NC.step(Z, NC.cfg_from_chain(Z - 1, rows), rows, 'cinf-chainref')
        r['sec'] = round(time.time() - t, 1); r['clight'] = CINF
        fh.write(json.dumps(r) + '\n'); fh.flush()
        print('DONE Z=%d ent=%s sealed=%s sec=%s' % (Z, r['ent'], rows[Z]['ent'], r['sec']), flush=True)
    fh.close()