"""Symbolic derivation of the axis-regular evolution system (computed, exact sympy).
Unknowns R, m, n, W, s of (u, v, x).  From the axis-regular components f_ab/rho (regform.py):
  E1 := (f_11 - f_xx)/(1 + x),  E2 := (f_22 - f_xx)/(1 - x),  E3 := f_xx,  E4 := f_ln   -> (R, m, n, W)_uv
  E5 := f_lx (divided by sqrt w)                                                       -> s_vv
The divisions by 1 +- x are exact polynomial divisions (the numerators vanish identically at x = -1, +1)."""
import sympy as sp, pickle, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from regform import regular_components

x, ES, OM2 = sp.symbols('x ES OM2')
FN = ('R', 'm', 'n', 'W', 's')
D2 = ('', 'u', 'v', 'x', 'uu', 'uv', 'vv', 'ux', 'vx', 'xx')
J = {f: {d: sp.Symbol(f + ('_' + d if d else '')) for d in D2} for f in FN}
T = [J[f]['uv'] for f in ('R', 'm', 'n', 'W')]

def exact_div(e, lin):
    """e / lin for a rational expression e whose numerator vanishes where lin = 0 (exact)"""
    num, den = sp.fraction(sp.together(e))
    num = sp.expand(num)
    q, r = sp.div(sp.Poly(num, x), sp.Poly(lin, x))
    assert r.is_zero, 'not divisible'
    return q.as_expr() / den

def main():
    t0 = time.time()
    f = regular_components(x, J, ES, OM2, one=sp.Integer(1))
    E = {'E1': (f['11'] - f['xx'], 1 + x), 'E2': (f['22'] - f['xx'], 1 - x), 'E3': (f['xx'], None), 'E4': (f['ln'], None)}
    out = {}
    for k, (e, lin) in E.items():
        e = sp.expand(e)
        M = [sp.diff(e, t) for t in T]
        assert all(not any(t in m_.free_symbols for t in T) for m_ in M)
        r = sp.expand(e - sum(m_ * t for m_, t in zip(M, T)))
        if lin is not None:
            M = [exact_div(m_, lin) for m_ in M]
            r = exact_div(r, lin)
        out[k] = (M, r)
        print(k, 'ops M', [sp.count_ops(m_) for m_ in M], 'ops r', sp.count_ops(r), 'syms',
              sorted(str(s_) for s_ in r.free_symbols), '%.0f s' % (time.time() - t0), flush=True)
    e5 = sp.expand(f['lx'])
    svv = J['s']['vv']
    c5 = sp.diff(e5, svv); r5 = sp.expand(e5 - c5 * svv)
    assert svv not in c5.free_symbols
    out['E5'] = ([c5], r5)
    print('E5 coef', c5, 'ops r', sp.count_ops(r5), 'syms', sorted(str(s_) for s_ in r5.free_symbols), flush=True)
    pickle.dump(dict(out=out), open(sys.argv[1] if len(sys.argv) > 1 else 'derive.pkl', 'wb'))

if __name__ == '__main__':
    main()
