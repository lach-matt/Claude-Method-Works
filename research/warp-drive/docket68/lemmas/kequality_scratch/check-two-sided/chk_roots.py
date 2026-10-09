"""Refine the discrete solutions found by chk_grid.py under the reading ell_ref = ell_1 (ell_2 = c ell_1),
ours at RS(ell_1) [the author's clause-(B) reading (iii)], and verify every equation UNSQUARED at 60 digits.
Units ell_s = 1.  Unknowns: L1, mu, R1, R2.  Equations:
  ours  (outer decaying):  lam1 R1 = sqrt(f_s(R1)) + sqrt(f_1(R1)),  B1 = (1-2mu/R1^2)/sqrt f_s + 1/sqrt f_1 = 0,  lam1 = 2/L1
  P2    (outer growing):   lam2 R2 = sqrt(f_s(R2)) - sqrt(f_2(R2)),  B2 = (1-2mu/R2^2)/sqrt f_s - 1/sqrt f_2 = 0,  L2 = c L1
"""
import mpmath as mp
mp.mp.dps = 60
import chk_grid as g

def solve(name2, c, bracket):
    r1 = g.LAM1['(iii) RS at ell_1']; r2 = g.LAM2[name2]
    def F(L1):
        rr = g.residuals(L1, r1, r2, c, 'ell_1')
        assert len(rr) == 1, len(rr)
        return rr[0][0]
    L1 = mp.findroot(F, bracket, solver='illinois', tol=mp.mpf(10)**-50)
    rr = g.residuals(L1, r1, r2, c, 'ell_1')[0]
    res, x, u1, m, y, u2, l2 = rr
    L2 = c*L1
    lam1 = 2/L1
    fs = lambda u: 1 + u - m/u
    f1 = lambda u: 1 + u/L1**2
    f2 = lambda u: 1 + u/L2**2
    T1 = lam1*mp.sqrt(u1) - (mp.sqrt(fs(u1)) + mp.sqrt(f1(u1)))
    B1 = (1-2*m/u1)/mp.sqrt(fs(u1)) + 1/mp.sqrt(f1(u1))
    lam2_t = r2(lam1, L1, L2)
    T2 = lam2_t*mp.sqrt(u2) - (mp.sqrt(fs(u2)) - mp.sqrt(f2(u2)))
    B2 = (1-2*m/u2)/mp.sqrt(fs(u2)) - 1/mp.sqrt(f2(u2))
    rh = mp.sqrt((-1 + mp.sqrt(1+4*m))/2)
    return dict(L1=L1, L2=L2, mu=m, R1=mp.sqrt(u1), R2=mp.sqrt(u2), rh=rh, lam1=lam1, lam2=lam2_t,
                ratio=lam2_t/lam1, T1=T1, B1=B1, T2=T2, B2=B2, u1_lt_2mu=u1 < 2*m, u2_gt_2mu=u2 > 2*m,
                fs1=fs(u1), fs2=fs(u2))

cases = [('ratio -1/4', mp.mpf(1), (mp.mpf('0.42658'), mp.mpf('0.436516'))),
         ('ratio -1/8', mp.mpf(1), (mp.mpf('0.74131'), mp.mpf('0.758578'))),
         ('ratio -1/8', mp.mpf(4)/3, (mp.mpf('0.467735'), mp.mpf('0.47863'))),
         ('-1/6 RS(ell_2)', mp.mpf(4)/3, (mp.mpf('0.467735'), mp.mpf('0.47863'))),
         ('-1/6 RS(ell_2)', mp.mpf(1), (mp.mpf('0.645654'), mp.mpf('0.660693'))),
         ('-1/6 RS(ell_2)', mp.mpf(3), (mp.mpf('0.158489'), mp.mpf('0.162181'))),
         ('-1/6 RS(ell_1)', mp.mpf(1), (mp.mpf('0.645654'), mp.mpf('0.660693'))),
         ('-1/6 RS(ell_1)', mp.mpf(4)/3, (mp.mpf('0.346737'), mp.mpf('0.354813')))]
if __name__ == '__main__':
    for n2, c, br in cases:
        d = solve(n2, c, br)
        print(f"P2 {n2:15s} c={mp.nstr(c,4):6s} L1=ell_1/ell_s={mp.nstr(d['L1'],20)} L2={mp.nstr(d['L2'],12)} mu={mp.nstr(d['mu'],15)} "
              f"R1={mp.nstr(d['R1'],12)} R2={mp.nstr(d['R2'],12)} r_h={mp.nstr(d['rh'],12)} lam1={mp.nstr(d['lam1'],10)} "
              f"lam2/lam1={mp.nstr(d['ratio'],10)}")
        print(f"     residuals T1={mp.nstr(d['T1'],3)} B1={mp.nstr(d['B1'],3)} T2={mp.nstr(d['T2'],3)} B2={mp.nstr(d['B2'],3)}; "
              f"u1<2mu {d['u1_lt_2mu']} u2>2mu {d['u2_gt_2mu']} f_s(R1)={mp.nstr(d['fs1'],6)} f_s(R2)={mp.nstr(d['fs2'],6)}; "
              f"in ell_1 units: mu/ell_1^2={mp.nstr(d['mu']/d['L1']**2,12)} r_h/ell_1={mp.nstr(d['rh']/d['L1'],12)} "
              f"R1/ell_1={mp.nstr(d['R1']/d['L1'],12)}")
