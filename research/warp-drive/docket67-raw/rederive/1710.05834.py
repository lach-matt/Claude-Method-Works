"""DOCKET 67 -- re-derivation of arXiv:1710.05834 sec 4.1 eq (1) and of the tree's use of it.
Stdlib + sympy only.  Reads nothing from research/warp-drive (constants retyped HERE only to
check them, marked with their source)."""
import sympy as sp
from decimal import Decimal, getcontext

c   = sp.Integer(299792458)                       # m/s, exact (SI)
Mpc = sp.Rational('3.0856775814913673e22')        # m, IAU 2015 (pc = 648000/pi au)
ok = True
def chk(name, cond, *vals):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name, *vals)

# ---- (A) the source's own inputs (READ, 1710.05834v2 p.6 sec 4.1) ------------------------
D   = 26*Mpc                        # lower bound of 90% credible interval on D_L
dt  = sp.Rational('1.74'); sdt = sp.Rational('0.05')
T   = D/c
hi  = (dt+sdt)/T                    # 'attributing the entire 1.74+0.05 s lag to faster travel by GW'
lo  = -(10-(dt-sdt))/T              # 'SGRB emitted 10 s after the GW'; most conservative with 1.69 s
lo_c= -(10-dt)/T                    # central lag
print("D/c = %.6e s" % float(T))
print("upper bound  = %+.4e  (published +7e-16)" % float(hi))
print("lower bound  = %+.4e (1.69 s) / %+.4e (1.74 s)  (published -3e-15)" % (float(lo), float(lo_c)))
chk("upper reproduces 7e-16 when rounded to 1 s.f., and published value is >= computed (conservative)",
    round(float(hi)*1e16) == 7 and float(hi) <= 7e-16, float(hi))
chk("lower reproduces -3e-15 when rounded to 1 s.f.", round(float(lo)*1e15) == -3, float(lo))
chk("DISCREPANCY (recorded, not a refutation): published |lower| 3e-15 is BELOW the computed 3.1e-15",
    abs(float(lo)) > 3e-15, "%.4e" % abs(float(lo)))

# ---- (B) cosmology: the delay accrues over COMIOVING distance D_C = D_L/(1+z) -------------
# For a constant fractional speed offset delta, Delta t_obs = delta * D_C / c (a0 = 1).
H0 = sp.Rational(674, 10)*1000/Mpc              # Planck 2018 67.4 km/s/Mpc (s^-1)
# low-z: D_L ~ (c/H0) z (1 + (1-q0) z/2), q0 = Om/2 - OL = 0.3153/2 - 0.6847
q0 = sp.Rational(3153,20000) - sp.Rational(6847,10000)
zs = sp.Symbol('z', positive=True)
zsol = sp.nsolve((c/H0)*zs*(1+(1-q0)*zs/2) - D, zs, 0.006)
hi_cosmo = hi*(1+zsol)
print("z(D_L=26 Mpc, H0=67.4) = %.5f ; upper bound with D_C: %.4e" % (float(zsol), float(hi_cosmo)))
chk("using D_C instead of D_L weakens the upper bound by (1+z) ~0.6%, still <= 7e-16",
    float(hi_cosmo) <= 7e-16, float(hi_cosmo))

# ---- (C) moved datum: EM distance to NGC 4993 (SBF, Cantiello+2018; NAMED-NOT-READ here) -----
for Dm, lab in ((40.7, "SBF central 40.7 Mpc"), (40.7-2.4, "SBF minus ~1 sigma (1.4 (+) 1.9) 38.3 Mpc"),
                (40.0, "tree's GW170817_DISTANCE_MPC 40.0")):
    h = (dt+sdt)/(sp.Rational(str(Dm))*Mpc/c)
    print("  upper bound at %-42s %.4e" % (lab, float(h)))
chk("any D >= 26 Mpc only TIGHTENS the upper bound (monotone in 1/D)",
    sp.diff((dt+sdt)*c/sp.Symbol('D', positive=True), sp.Symbol('D', positive=True)).subs(sp.Symbol('D', positive=True), D) < 0)

# ---- (D) the 'exotic' emission window the source names: (-100 s, 1000 s) -------------------
hi_exotic = (100+dt+sdt)/T; lo_exotic = -(1000-(dt-sdt))/T
print("exotic window: %+.3e <= dv/v <= %+.3e (source: '2 orders of magnitude broadening')" % (float(lo_exotic), float(hi_exotic)))
chk("exotic window broadens upper by ~2 orders (factor 57) and lower by ~2 orders (factor 121)",
    50 < float(hi_exotic/hi) < 60 and 100 < float(lo_exotic/lo) < 130, float(hi_exotic/hi), float(lo_exotic/lo))

# ---- (E) the tree's arithmetic (branelink.py:55-66), 50 digits ------------------------------
getcontext().prec = 50
d = Decimal('7e-16')
beta = (d*(2+d)).sqrt()/(1+d)
span = Decimal('4.2465')*Decimal(299792458)*Decimal('31557600')   # 4.2465 ly, Julian-year ly
Tp = span/Decimal(299792458)
dtau = Tp*d/(1+d)
print("beta = %s ; 1/beta = %s ; T = %s s ; dtau = %s ns" % (
      format(beta, '.12e'), format(1/beta, '.12f'), format(Tp, '.1f'), format(dtau*10**9, '.8f')))
chk("beta = 3.74165738677e-08", abs(beta - Decimal('3.74165738677e-08')) < Decimal('1e-19'))
chk("1/beta = 26726124.1912", abs(1/beta - Decimal('26726124.1912')) < Decimal('1e-4'))
chk("T = 134009348.4 s", abs(Tp - Decimal('134009348.4')) < Decimal('0.05'))
chk("Delta_tau = 93.80654 ns", abs(dtau*10**9 - Decimal('93.80654')) < Decimal('5e-6'))
# symbolic: gamma = 1+d  =>  beta = sqrt(1-1/gamma^2) = sqrt(d(2+d))/(1+d)
ds = sp.Symbol('d', positive=True)
chk("identity sqrt(1-1/(1+d)^2) == sqrt(d(2+d))/(1+d)",
    sp.simplify(sp.sqrt(1-1/(1+ds)**2) - sp.sqrt(ds*(2+ds))/(1+ds)) == 0)

# with the computed (unrounded) upper bound and with the SBF distance
for dd, lab in ((float(hi), "computed unrounded 6.69e-16"), (float((dt+sdt)/(sp.Rational('40.7')*Mpc/c)), "SBF 40.7 Mpc")):
    D2 = Decimal(repr(dd)); print("  saving at B=0 with d = %.4e (%s): %.3f ns ; beta = %.4e" % (
        dd, lab, float(Tp*D2/(1+D2)*10**9), float((D2*(2+D2)).sqrt()/(1+D2))))

# ---- (F) the tree's manyc.py framing ---------------------------------------------------------
Tm = 40*sp.Rational('3.0857e22')/c
print("manyc 1.74 s / (40 Mpc/c) = %.4e ; 1/that = %.3e" % (float(dt/Tm), float(Tm/dt)))
chk("manyc.py:29 4.226e-16 reproduces as 1.74 s over 40 Mpc (a central-distance lag ratio, not a published bound)",
    abs(float(dt/Tm) - 4.226e-16) < 5e-20)
yr = 31557600; ly = 299792458*yr
for nm, Dly in (("Proxima", 4.246), ("Andromeda", 2.5e6)):
    t3 = Dly*ly/299792458*3e-15; t7 = Dly*ly/299792458*7e-16
    print("  %-10s saved at 3e-15: %.4e s ; at the published FAST edge 7e-16: %.4e s" % (nm, t3, t7))
chk("manyc.py:34/167-172: '3e-15 FAST' uses the SLOW-side magnitude; the fast edge is 7e-16 (4.29x smaller)",
    abs(3e-15/7e-16 - 4.2857) < 1e-3)
print("\nALL PASS" if ok else "\nSOME FAIL")
