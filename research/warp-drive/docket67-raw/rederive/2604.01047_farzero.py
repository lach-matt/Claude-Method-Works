# Is there a real NEGATIVE zero of F_S for every b2<0, far out at |gamma| ~ m^2 exp(16 pi^2 |b2|)?
import mpmath as mp
mp.mp.dps = 420
def J(gv, mm):
    gv = mp.mpc(gv)
    return (1/(8*mp.pi**2))*(1/gv - mp.sqrt(4*mm**2-gv)*mp.asin(mp.sqrt(gv)/(2*mm))/gv**mp.mpf(1.5))
def FS(gv, mm, kk, alv, xiv, b2v):
    cc = 6*(mp.mpf(1)/6-xiv)**2
    B0 = -alv*4*mm**4/cc; B1 = -(2/kk)/cc; A_ = 2*mm**2/(6*xiv-1)
    return mp.re(gv*(A_-gv)**2*J(gv, mm)) - (B0 + B1*gv + b2v*gv**2)
MP_EV = mp.mpf('2.435323e27'); mm = mp.mpf('7.885e-3')/MP_EV; kk = mp.mpf(1); AL = 1/(64*mp.pi**2)
for b2s in ('-1', '-10', '-1000', '-1e100', '-8.62e121'):
    b2 = mp.mpf(b2s)
    L = 16*mp.pi**2*abs(b2)           # predicted log(X/m^2) scale
    out = []
    for f in ('0.9', '1.1'):
        X = mm**2*mp.exp(mp.mpf(f)*L)
        out.append(mp.sign(FS(-X, mm, kk, AL, mp.mpf(0), b2)))
    print("b2=%s: sign F_S at -m^2 e^{0.9L}, -m^2 e^{1.1L} = %s  (sign change => real negative zero, log10|gamma| ~ %s)" % (b2s, out, mp.nstr(mp.log10(mm**2)+L/mp.log(10), 5)))
