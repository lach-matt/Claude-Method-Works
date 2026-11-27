"""Post-processing of a solver run: residual of the unquantized approximant and of printed versions at sample points.
usage: post.py case run.coef workdir [quanta list e.g. 28,29,30] [npts per direction]
Writes workdir/pts_*.txt, workdir/approx_*.txt and runs evalres (EVALRES env, default evalres_dd next to the run)."""
import sys, os, json, subprocess, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import approx, tables
NAPP1 = os.environ.get('NAPP1', '/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/napp1')
sys.path.insert(0, NAPP1)
import rep

def summarize(fn, case):
    a = np.loadtxt(fn)
    m = np.abs(a[:, 3:]).max(1)
    L = rep.layout(case)
    out = {}
    for i in range(len(L['xi'])):
        for j in range(len(L['v'])):
            x0, x1, v0, v1 = approx.use_box(case, i, j)
            sel = (a[:, 0] >= x0 - 1e-12) & (a[:, 0] <= x1 + 1e-12) & (a[:, 1] >= v0 - 1e-12) & (a[:, 1] <= v1 + 1e-12)
            if sel.any():
                out['%d%d' % (i + 1, j + 1)] = dict(max=float(m[sel].max()), median=float(np.median(m[sel])))
    out['all'] = dict(max=float(m.max()), median=float(np.median(m)), n=int(len(m)))
    return out

def main():
    case, cf, wd = sys.argv[1], sys.argv[2], sys.argv[3]
    quanta = [int(q) for q in sys.argv[4].split(',')] if len(sys.argv) > 4 and sys.argv[4] else []
    npts = int(sys.argv[5]) if len(sys.argv) > 5 else 7
    ev = os.environ.get('EVALRES', os.path.join(os.path.dirname(os.path.abspath(cf)), '..', 'evalres_dd'))
    os.makedirs(wd, exist_ok=True)
    C = approx.read_coef(cf)
    L = rep.layout(case)
    pts = approx.points(case, n=(npts, npts, 6))
    open(os.path.join(wd, 'pts.txt'), 'w').write('\n'.join(pts) + '\n')
    res = {}
    # the unquantized approximant (coefficients below 1e-36 of the block maximum dropped)
    blocks = {}; e = 0
    for i in range(len(L['xi'])):
        for j in range(len(L['v'])):
            for f in range(5):
                parts = C[e][f].copy()
                mx = np.abs(parts[..., 0]).max(); parts[np.abs(parts[..., 0]) < 1e-36 * mx] = 0
                nz = np.argwhere(parts[..., 0] != 0); hi = nz.max(0) + 1
                blocks[(i, j, f)] = (-1, parts[:hi[0], :hi[1], :hi[2]])
            e += 1
    approx.write_approx(case, blocks, os.path.join(wd, 'approx_raw.txt'))
    subprocess.run([ev, os.path.join(wd, 'approx_raw.txt'), os.path.join(wd, 'pts.txt'), os.path.join(wd, 'res_raw.txt')], check=True)
    res['raw'] = summarize(os.path.join(wd, 'res_raw.txt'), case)
    print('unquantized:', json.dumps(res['raw']), flush=True)
    for p in quanta:
        blocks = {}; e = 0
        for i in range(len(L['xi'])):
            for j in range(len(L['v'])):
                for f in range(5):
                    blocks[(i, j, f)] = (p, tables.trim(tables.quantize_parts(C[e][f], p)))
                e += 1
        fn = os.path.join(wd, 'approx_p%d.txt' % p)
        approx.write_approx(case, blocks, fn)
        subprocess.run([ev, fn, os.path.join(wd, 'pts.txt'), os.path.join(wd, 'res_p%d.txt' % p)], check=True)
        res['p%d' % p] = summarize(os.path.join(wd, 'res_p%d.txt' % p), case)
        print('p = %d:' % p, json.dumps(res['p%d' % p]), flush=True)
    json.dump(res, open(os.path.join(wd, 'post.json'), 'w'), indent=1)

main()
