"""Convention grid with ell_2 = c * ell_ref, ell_ref in {ell_s, ell_1}; ours at RS read (ii) at ell_s or (iii) at ell_1;
P2 tension in several recorded forms.  Units ell_s = 1.  Exact reduction used:
 ours: lam1^2 = (1+x)(2 + v1^2 (x-1))/(2x-1),  u1 = (2x-1)(x+1)/(2(1-x^2 v1^2)),  mu = u1 (1+x)/2,  x>0
 P2:   lam2^2 = (1-y)(v2^2 (1+y) - 2)/(2y+1) [sign -], u2 = (2y+1)(y-1)/(2(1-y^2 v2^2)), mu = u2 (1-y)/2, 0<y<1
Unknowns (x, y, L1) [L2 = c L1 or c]; equations: lam1 = target1, lam2 = target2, mu1 = mu2.
"""
import mpmath as mp
mp.mp.dps = 60

def ours(x, v1, lam1=None):
    """u1 from the tension relation lam^2 u = (1+x)^2 (1 + u v^2) (no 0/0 at x v = 1); G=0 checked by caller."""
    if lam1 is None:
        u1 = (2*x-1)*(x+1)/(2*(1-x**2*v1**2))
        return u1, u1*(1+x)/2, mp.sqrt((1+x)*(2+v1**2*(x-1))/(2*x-1))
    u1 = (1+x)**2/(lam1**2 - (1+x)**2*v1**2)
    return u1, u1*(1+x)/2, lam1

def p2(y, v2):
    u2 = (2*y+1)*(y-1)/(2*(1-y**2*v2**2))
    return u2, u2*(1-y)/2, -mp.sqrt((1-y)*(v2**2*(1+y)-2)/(2*y+1))

def unsquared_ok(u, m, vo, eps_o, lamv):
    fs = 1 + u - m/u; fo = 1 + u*vo**2
    if fs <= 0 or u <= 0 or m <= 0: return False
    t1 = (1-2*m/u)/mp.sqrt(fs); t2 = eps_o/mp.sqrt(fo)
    bal = (t1 + t2)/(abs(t1) + abs(t2))
    ten = ((mp.sqrt(fs) + eps_o*mp.sqrt(fo))/mp.sqrt(u) - lamv)/abs(lamv)
    return abs(bal) < mp.mpf(10)**-20 and abs(ten) < mp.mpf(10)**-20

def ours_solutions(L1, lam1):
    v1 = 1/L1
    co = [v1**2, 2 - 2*lam1**2, 2 - v1**2 + lam1**2]
    out = []
    for xr in mp.polyroots(co, maxsteps=300, extraprec=300):
        if abs(mp.im(xr)) > mp.mpf(10)**-25: continue
        xr = mp.re(xr)
        if xr <= 0: continue
        u1, m, l = ours(xr, v1, lam1)
        if unsquared_ok(u1, m, v1, +1, lam1):
            out.append((xr, u1, m))
    return out

def p2_curve_y_for_mu(m, L2, ngrid=None):
    """y in (1/v2, 1) with mu(y) = m (P2 static, outer growing): cubic 2y^3 - (3+4 m v2^2) y^2 + (1+4m) = 0."""
    v2 = 1/L2
    if v2 <= 1: return []
    out = []
    for yr in mp.polyroots([2, -(3+4*m*v2**2), 0, 1+4*m], maxsteps=300, extraprec=300):
        if abs(mp.im(yr)) > mp.mpf(10)**-25: continue
        yr = mp.re(yr)
        if 1/v2 < yr < 1:
            u2, m2, l2 = p2(yr, v2)
            assert abs(m2 - m) < mp.mpf(10)**-25
            assert unsquared_ok(u2, m2, v2, -1, l2)
            out.append(yr)
    return out

def residuals(L1, lam1_rule, lam2_rule, c, ref):
    L1 = mp.mpf(L1)
    L2 = c*L1 if ref == 'ell_1' else mp.mpf(c)
    lam1 = lam1_rule(L1)
    res = []
    for (xr, u1, m) in ours_solutions(L1, lam1):
        for yy in p2_curve_y_for_mu(m, L2):
            u2, m2, l2 = p2(yy, 1/L2)
            tgt = lam2_rule(lam1, L1, L2)
            res.append((l2 - tgt, xr, u1, m, yy, u2, l2))
    return res

LAM1 = {'(ii) RS at ell_s': lambda L1: mp.mpf(2), '(iii) RS at ell_1': lambda L1: 2/L1}
LAM2 = {'ratio -1/4': lambda l1, L1, L2: -l1/4, 'ratio -1/8': lambda l1, L1, L2: -l1/8,
        '-1/3 RS(ell_2)': lambda l1, L1, L2: -(mp.mpf(2)/3)/L2, '-1/6 RS(ell_2)': lambda l1, L1, L2: -(mp.mpf(1)/3)/L2,
        '-1/3 RS(ell_1)': lambda l1, L1, L2: -(mp.mpf(2)/3)/L1, '-1/6 RS(ell_1)': lambda l1, L1, L2: -(mp.mpf(1)/3)/L1}
CS = [mp.mpf(1), mp.mpf(4)/3, mp.mpf(3), mp.mpf(6)]

if __name__ == '__main__':
    import sys
    report = []
    for ref in ('ell_s', 'ell_1'):
        for n1, r1 in LAM1.items():
            for n2, r2 in LAM2.items():
                for c in CS:
                    if ref == 'ell_s':
                        # L2 = c >= 1: P2 has no static mu>0 point (exact). confirm numerically at one L1
                        L1s = [mp.mpf(3)/2, 2, 5] if n1.startswith('(ii)') else [mp.mpf(1)/2, mp.mpf(4)/5]
                        found = sum(len(residuals(L1, r1, r2, c, ref)) for L1 in L1s)
                        report.append((ref, n1, n2, mp.nstr(c, 4), 'P2 static points found: %d (exact: none, L2>=1)' % found))
                        continue
                    # ell_1: scan L1 over the admissible range
                    if n1.startswith('(ii)'):
                        Lgrid = [1 + mp.mpf(10)**(-3 + 6*mp.mpf(i)/200) for i in range(201)]  # L1>1 needed
                    else:
                        Lgrid = [mp.mpf(10)**(-4 + 4*mp.mpf(i)/400) for i in range(1, 400)]  # L1<1 needed
                    rows = []
                    for L1 in Lgrid:
                        rr = residuals(L1, r1, r2, c, ref)
                        rows.append((L1, rr))
                    # count P2 static points and sign changes of residual
                    npts = sum(len(rr) for _, rr in rows)
                    signs = []
                    for L1, rr in rows:
                        for t in rr:
                            signs.append((L1, t[0]))
                    flips = []
                    for (La, ra), (Lb, rb) in zip(signs, signs[1:]):
                        if ra*rb < 0: flips.append((La, Lb))
                    report.append((ref, n1, n2, mp.nstr(c, 4), 'P2 static points on grid: %d; residual sign flips: %d %s' %
                                   (npts, len(flips), [(mp.nstr(a, 6), mp.nstr(b, 6)) for a, b in flips[:4]])))
    for row in report:
        print(' | '.join(row))
