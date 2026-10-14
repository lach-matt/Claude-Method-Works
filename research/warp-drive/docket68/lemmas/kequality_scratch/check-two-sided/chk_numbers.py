"""Remaining numbers: author's off-convention example at 50 digits, the family limits, k=-1 cases, the depth example."""
import mpmath as mp
mp.mp.dps = 60
import chk_grid as g

def p2_L2_for(m, lam):
    """RS at ell_s branch: P2 at |lam| given mu: 4mu^2(u+u^2-mu) = lam^2 u^2 (u-2mu)^2, L2^2 = u/(Q^2-1)."""
    co = [lam**2, -4*m*lam**2, 4*m**2*lam**2 - 4*m**2, -4*m**2, 4*m**3]  # lam^2 u^2 (u^2 - 4mu u + 4mu^2) - 4mu^2 u^2 - 4mu^2 u + 4mu^3
    out = []
    for z in mp.polyroots(co, maxsteps=500, extraprec=500):
        if abs(mp.im(z)) > mp.mpf(10)**-40: continue
        uu = mp.re(z)
        if uu <= 2*m: continue
        Q2 = lam**2*uu**3/(4*m**2)
        if Q2 <= 1: continue
        L2 = mp.sqrt(uu/(Q2-1))
        ok = g.unsquared_ok(uu, m, 1/L2, -1, -lam)
        out.append((uu, L2, ok))
    return out

if __name__ == '__main__':
    m = mp.mpf(4)/3
    for lam in (mp.mpf(1)/2, mp.mpf(1)/4):
        print("RS at ell_s, L1=2, mu=4/3, |lam2|=%s:" % mp.nstr(lam, 3),
              [(mp.nstr(mp.sqrt(a), 10), mp.nstr(b, 22), ok) for a, b, ok in p2_L2_for(m, lam)])
    # limits of the family: L1 -> inf (mu->1+), L1 -> 1+ (mu -> inf)
    for lam, nm in ((mp.mpf(1)/2, '-1/4'), (mp.mpf(1)/4, '-1/8')):
        for mm in (mp.mpf(1) + mp.mpf(10)**-12, mp.mpf(1)+mp.mpf(10)**-3, 2, 10, 10**4, 10**6, 10**9):
            r = p2_L2_for(mp.mpf(mm), lam)
            print(f"  ratio {nm}: mu={mp.nstr(mm,8)} L2={[mp.nstr(b,12) for a,b,ok in r]} ok={[ok for a,b,ok in r]}")
    # exact large-mu limit: u ~ s mu, leading order: 4mu^2 (s^2 mu^2) = lam^2 s^2 mu^2 (s-2)^2 mu^2 -> s-2 = 2/(lam mu)?? -> do numerically above
    # k=-1, ours with decaying outer: static needs mu < -u/2, check it lies inside inner horizon
    print("\nk=-1 ours decaying outer: B=0 needs (-1-2mu/u) sqrt f_o = sqrt f_s > 0 -> mu < -u/2.")
    bad = 0
    for i in range(1, 200):
        mm = -mp.mpf(1)/4 + mp.mpf(i)/800   # mu in (-1/4, 0)
        up = (1 + mp.sqrt(1+4*mm))/2
        if -2*mm >= up: bad += 1
    print("  any mu in (-1/4,0) with -2mu >= u_+ (exterior reachable)?", bad, "(0 => only inside the inner horizon)")
    # extremal k=-1 position 2
    for L in (mp.mpf('0.6'), mp.mpf('0.8'), mp.mpf('0.95')):
        u = L**2/(1-L**2); mm = -mp.mpf(1)/4
        fs = -1 + u - mm/u; fo = -1 + u/L**2
        bal = (-1-2*mm/u)/mp.sqrt(fs) + 1/mp.sqrt(fo)
        lamv = (mp.sqrt(fs) - mp.sqrt(fo))/mp.sqrt(u)
        print(f"  extremal k=-1 P2 L={L}: u={mp.nstr(u,10)} bal={mp.nstr(bal,3)} lam={mp.nstr(lamv,12)} claim={mp.nstr(-(1-L**2)/(2*L**2),12)}")
    # depth example: mu = 1/2 (r_h = 0.605), mirrored static R^2 = 2mu = 1
    mm = mp.mpf(1)/2
    rh = mp.sqrt((-1+mp.sqrt(1+4*mm))/2)
    depth = mp.quad(lambda rr: 1/mp.sqrt(1 + rr**2 - mm/rr**2), [rh, 1])
    print(f"\ndepth from R=1 to r_h={mp.nstr(rh,10)} at mu=1/2: {mp.nstr(depth,10)}")
