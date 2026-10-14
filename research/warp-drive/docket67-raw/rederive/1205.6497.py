"""DOCKET 67 -- re-derivation for Degrassi et al., arXiv:1205.6497v2.
Every number below is READ from the paper (page cited) or from the later paper
named, or COMPUTED here.  Nothing repaired; discrepancies are printed."""
import math
from fractions import Fraction as F
from statistics import NormalDist

ok = True
def chk(name, got, want, tol=0.0):
    global ok
    good = abs(got - want) <= tol if isinstance(want, (int, float)) else got == want
    ok &= good
    print(("PASS " if good else "FAIL ") + name + ": got %r want %r" % (got, want))

print("== C1  eq.(2) -> eq.(3): errors combined in quadrature (p.2 printed)")
th, mt_term, as_term = 1.0, 1.4, 0.5         # eq.(2): 1.4 per 0.7 GeV of M_t, 0.5 per 0.0007 of alpha_s, 1.0 th
comb = math.sqrt(th**2 + mt_term**2 + as_term**2)
chk("sqrt(1.0^2+1.4^2+0.5^2) rounds to 1.8", round(comb, 1), 1.8)
chk("Table 1 experiment total sqrt(1.4^2+0.5^2) = 1.5", round(math.hypot(1.4, 0.5), 1), 1.5)
chk("Table 1 theory total sqrt(.7^2+.6^2+.3^2+.2^2) = 1.0", round(math.sqrt(.49+.36+.09+.04), 1), 1.0)
edge2 = 129.4 - 2 * 1.8
chk("2 sigma lower edge 129.4 - 2(1.8) = 125.8 (source rounds: 'M_h < 126')", round(edge2, 1), 125.8)
chk("one-sided 2 sigma CL = 97.7% ('98% C.L.')", round(NormalDist().cdf(2.0) * 100, 1), 97.7)

print("== C2  eq.(64) at M_h = 125 -> 'lambda(M_Pl) = -0.014 +- 0.006' (p.27 printed / PDF p.28)")
lam = -0.0129 + 0.0028 * (125 - 125.5)
err = math.sqrt(0.0047**2 + 0.0018**2 + 0.0028**2)
chk("central -0.0143 rounds to -0.014", round(lam, 3), -0.014)
chk("quadrature error 0.0058 rounds to 0.006", round(err, 3), 0.006)

print("== C3  the tree's arithmetic on Degrassi's band (excite.py:983-1024)")
M_red = 2.435e18   # reduced Planck mass, GeV
phi = 2e16         # xigate.GUT_SCALE_GEV
xi = (M_red / phi) ** 2
chk("xi_required(2e16) = (M_red/phi)^2 ~ 1.48e4", round(xi / 1e4, 2), 1.48)
ratios = [phi / 10 ** L for L in (12, 11, 10)]
chk("phi/10^12, 10^11, 10^10 = 2e4, 2e5, 2e6", [round(r) for r in ratios], [20000, 200000, 2000000])
frac = math.log10(2e5 / 2e4) / math.log10(ratios[2] / ratios[0])
chk("ruling '2e4 to 2e5' spans 0.5 of the band in log10", frac, 0.5, 1e-12)

print("== C4  hypothesis Degrassi Sec.4.2 names and the tree drops: phi vs the unitarity scale M_Pl/xi")
# p.21 printed: 'Perturbative unitarity is violated at the scale M_Pl/xi ... expected [to] affect the
# scalar potential above M_Pl/xi in an uncontrollable way'; 'Higgs xi-inflation requires stability
# of the potential up to the inflationary scale M_Pl/sqrt(xi)'.
cut = M_red / xi
inflscale = M_red / math.sqrt(xi)
chk("the tree's phi IS M_red/sqrt(xi) (Degrassi's inflationary scale)", round(inflscale / 1e16, 6), 2.0)
print("     M_red/xi = %.3g GeV; phi / (M_red/xi) = sqrt(xi) = %.1f  -> phi sits above the cutoff" % (cut, phi / cut))
chk("phi above M_red/xi", phi > cut, True)

print("== C5  data then vs now, through Degrassi's own linear eq.(2) (a linearisation about 173.1/0.1184)")
def mh_crit(mt, a_s):
    return 129.4 + 1.4 * (mt - 173.1) / 0.7 - 0.5 * (a_s - 0.1184) / 0.0007
def nsig(mh, mt, dmt, a_s, das, dmh=0.0):
    c = mh_crit(mt, a_s)
    s = math.sqrt(1.0**2 + (1.4 * dmt / 0.7)**2 + (0.5 * das / 0.0007)**2 + dmh**2)
    return c, s, (c - mh) / s
# then: M_t = 173.1 +- 0.7 (eq.61), alpha_s = 0.1184 +- 0.0007 (eq.58), M_h = 125 (p.27 sentence)
c, s, n = nsig(125.0, 173.1, 0.7, 0.1184, 0.0007)
print("     THEN  M_h,crit = %.2f +- %.2f ; M_h=125.0 -> %.2f sigma" % (c, s, n))
# now: PDG 2024 as READ in arXiv:2401.08811 Table I: M_h=125.20(11), M_t^MC=172.57(29), M_t^sigma=172.4(7), alpha_s=0.1180(9)
# FINDING (recorded, not repaired): which side of 2 sigma depends on WHICH top mass is used.
for lab, mt, dmt, want in (("M_t^MC 172.57(29)", 172.57, 0.29, True), ("M_t^sigma 172.4(7)", 172.4, 0.7, False)):
    c, s, n = nsig(125.20, mt, dmt, 0.1180, 0.0009, 0.11)
    print("     NOW   %-20s M_h,crit = %.2f +- %.2f ; M_h=125.20 -> %.2f sigma" % (lab, c, s, n))
    chk("  exclusion > 2 sigma via eq.(2) [" + lab + "] is " + str(want), n > 2.0, want)
# Hiller et al. 2401.08811 Table I (full N3LO-class machinery, not eq.(2)): -1.9 sigma (M_t^sigma), -5.1 sigma (M_t^MC)
# critical top mass (stability) at M_h = 125.20, alpha_s = 0.1180, from eq.(2) inverted
mtc = 173.1 + 0.7 / 1.4 * (125.20 - 129.4 + 0.5 * (0.1180 - 0.1184) / 0.0007)
print("     eq.(2) inverted: M_t,crit(125.20, 0.1180) = %.2f GeV (+-0.5 th); Hiller 2401.08811 Table I: 171.10" % mtc)

print("== C6  instability scale then vs now")
# Buttazzo 1307.3536 eq.(67) (as seated in endpoint.py), Lambda_I ~ 13 Lambda_V (Landau gauge)
def log10LI(mh, mt, a_s):
    return 9.5 + 0.7 * (mh - 125.15) - 1.0 * (mt - 173.34) + 0.3 * (a_s - 0.1184) / 0.0007 + math.log10(13)
for lab, mt in (("M_t^MC 172.57", 172.57), ("M_t^sigma 172.4", 172.4)):
    L = log10LI(125.20, mt, 0.1180)
    print("     Buttazzo eq.(67) at PDG 2024, %-16s: log10 Lambda_I = %.2f" % (lab, L))
    chk("  inside Degrassi's 11 +- 1", abs(L - 11) <= 1, True)
L_h = math.log10(5.3e11)   # Hiller et al. 2401.08811 p.3: Lambda_0,eff ~ 5.3e11 GeV (Landau gauge), PDG 2024
chk("Hiller 2024 Lambda_0,eff = 5.3e11 inside 10^(11+-1)", abs(L_h - 11) <= 1, True)
print("     phi / 5.3e11 = %.2g  (inside the tree's 2e4..2e6 band)" % (phi / 5.3e11))
chk("phi/Lambda(Hiller) inside tree band [2e4, 2e6]", 2e4 <= phi / 5.3e11 <= 2e6, True)
# Espinosa-Garny-Konstandin-Riotto 1608.06765: gauge-independent large-n Lambda_I ~ 1e11; h_I gauge-dependent
# by up to two orders of magnitude (xi up to ~300).  Not a formula; recorded.

print("\nALL PASS" if ok else "\nSOME FAIL")
