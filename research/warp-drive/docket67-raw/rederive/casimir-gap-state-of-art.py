"""DOCKET 67 / casimir-gap-state-of-art -- re-derivation.

Checks, without editing the tree:
  (A) achievable.py's apparatus-row arithmetic (densities, b, ly, 72.951, 8.541)
      reproduced from its own functions (imported by path, no bytecode written).
  (B) the hypothesis the row drops: casimir_density() is the IDEAL perfect-
      conductor energy density pi^2 hbar c/(720 d^4).  The tree itself states
      (scale.py:142-143) that this idealisation needs the gap to exceed the
      plate material's plasma wavelength.  Gold's lambda_p = 137.8 nm (tolman.py
      :1511, hbar omega_p = 9.0 eV, tolman.py:1142).  Both gaps (10 nm, 0.1 nm)
      are below it.  We compute the T = 0 Lifshitz energy for two gold half-
      spaces (plasma model, and Drude with gamma = 35 meV) at 10 nm and the
      ratio eta = E_real/E_ideal, then the corridor b the REAL density needs.
  (C) at 0.1 nm the continuum theory itself fails (gap < gold nearest-neighbour
      distance 0.288 nm); we report the non-retarded Lifshitz (Hamaker) value
      only as an order-of-magnitude comparison, and flag it as outside validity.
  (D) direction: does replacing ideal by real move the row's conclusion?
"""
import sys, math, importlib.util
sys.dont_write_bytecode = True
from scipy import integrate

WD = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, WD)
spec = importlib.util.spec_from_file_location("achievable", WD + "/achievable.py")
A = importlib.util.module_from_spec(spec)
spec.loader.exec_module(A)

HBAR, C = A.HBAR, A.C_SI
HBAR_C = A.HBAR_C
EV = 1.602176634e-19
LY = 9.461e15
ok_all = True


def chk(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + label)


print("(A) THE TREE'S OWN ARITHMETIC")
for gap, want_b, want_ly in ((1e-8, 6.5e20, 68000.0), (1e-10, 6.5e16, 6.8)):
    rho = A.casimir_density(gap)
    b = A.casimir_b_needed(gap)
    print("   gap %.0e m: ideal rho = %.4e J/m^3, b = %.4e m = %.4g ly" % (gap, rho, b, b / LY))
    chk("b matches tree's printed %.1e m to 2 sig figs" % want_b, abs(b / want_b - 1) < 0.01)
    chk("ly matches tree's printed %g to 2 sig figs" % want_ly, abs(b / LY / want_ly - 1) < 0.01)
r = A.quantum_bound(1e-10) / A.casimir_density(1e-10)
chk("bound/ideal = 720/pi^2 = %.6f (tree 72.951)" % (720 / math.pi ** 2), abs(r - 72.951) < 1e-3)
chk("sqrt = %.5f (tree 8.541)" % math.sqrt(r), abs(math.sqrt(r) - 8.541) < 1e-3)
# the original pre-DOCKET-55 rows (quantum_bound), kept in the file's text
for gap, want in ((1e-8, 7.6e19), (1e-10, 7.6e15)):
    b0 = A.b_needed_for(A.quantum_bound(gap))
    chk("withdrawn row gap %.0e -> b %.3e (tree %.1e)" % (gap, b0, want), abs(b0 / want - 1) < 0.01)


# ---------------------------------------------------------------- (B) Lifshitz
def eps_plasma(xi, wp):
    return 1.0 + (wp / xi) ** 2


def eps_drude(xi, wp, gam):
    return 1.0 + wp ** 2 / (xi * (xi + gam))


def lifshitz_E_over_A(d, eps_fn):
    """T=0 Lifshitz energy per area for two identical half-spaces, vacuum gap d.
    Dimensionless: zeta = xi d/c, y = q d >= zeta.
      E/A = hbar c/(4 pi^2 d^3) INT_0^inf dzeta INT_zeta^inf y dy
            [ln(1 - rTM^2 e^-2y) + ln(1 - rTE^2 e^-2y)]."""
    def inner(zeta):
        if zeta == 0.0:
            zeta = 1e-12
        xi = zeta * C / d
        e = eps_fn(xi)

        def f(y):
            kap = math.sqrt(y * y + (e - 1.0) * zeta * zeta)
            rtm = (e * y - kap) / (e * y + kap)
            rte = (y - kap) / (y + kap)
            x = math.exp(-2 * y)
            return y * (math.log1p(-rtm * rtm * x) + math.log1p(-rte * rte * x))
        v, _ = integrate.quad(f, zeta, zeta + 40.0, limit=400)
        return v
    v, _ = integrate.quad(inner, 0.0, 40.0, limit=400)
    return HBAR_C / (4 * math.pi ** 2 * d ** 3) * v


def ideal_E_over_A(d):
    return -math.pi ** 2 * HBAR_C / (720.0 * d ** 3)


# self-check of the integrator: perfect reflector r = 1 must reproduce -pi^2/720
def ideal_check():
    f = lambda y, z: y * 2 * math.log1p(-math.exp(-2 * y))
    v, _ = integrate.dblquad(f, 0, 40, lambda z: z, lambda z: z + 40)
    return v / (4 * math.pi ** 2)


print("\n(B) THE DROPPED HYPOTHESIS: PERFECT CONDUCTOR, GAP ABOVE lambda_p")
ic = ideal_check()
chk("integrator self-check: r=1 gives %.8f vs -pi^2/720 = %.8f" % (ic, -math.pi ** 2 / 720), abs(ic + math.pi ** 2 / 720) < 1e-6)

WP = 9.0 * EV / HBAR          # tree's CITED gold plasma energy (tolman.py:1142)
GAM = 0.035 * EV / HBAR       # common gold Drude relaxation (NAMED here, not the tree's)
lam_p = 2 * math.pi * C / WP
print("   gold lambda_p = 2 pi c/omega_p = %.2f nm (tree tolman.py:1511 says 137.8)" % (lam_p * 1e9))
chk("both gaps are below lambda_p, so scale.py:142-143's own condition fails", 1e-8 < lam_p and 1e-10 < lam_p)

rows = []
for d in (1e-6, 1e-7, 3e-8, 1e-8):
    Ep = lifshitz_E_over_A(d, lambda xi: eps_plasma(xi, WP))
    Ed = lifshitz_E_over_A(d, lambda xi: eps_drude(xi, WP, GAM))
    Ei = ideal_E_over_A(d)
    rows.append((d, Ep / Ei, Ed / Ei))
    print("   d = %6.1f nm: eta_plasma = %.4f  eta_drude(T=0) = %.4f" % (d * 1e9, Ep / Ei, Ed / Ei))
eta10p = rows[-1][1]
eta10d = rows[-1][2]
chk("eta < 1 at every gap (real metal is WEAKER than the ideal formula)", all(r[1] < 1 and r[2] < 1 for r in rows))
chk("eta rises toward 1 at large gap (1 um plasma eta > 0.8)", rows[0][1] > 0.8)

b_ideal10 = A.casimir_b_needed(1e-8)
b_real10 = A.b_needed_for(A.casimir_density(1e-8) * eta10p)
print("   10 nm: ideal b = %.3e m (%.3g ly); plasma-model gold b = %.3e m (%.3g ly); factor %.3f"
      % (b_ideal10, b_ideal10 / LY, b_real10, b_real10 / LY, b_real10 / b_ideal10))
chk("real gold needs a LARGER corridor at 10 nm than the tree prints (row strengthened)", b_real10 > b_ideal10)

# ---------------------------------------------------------------- (C) 0.1 nm
print("\n(C) 0.1 nm: BELOW ATOMIC CONTACT -- CONTINUUM THEORY OUT OF VALIDITY")
NN_AU = 0.2884e-9    # gold fcc nearest-neighbour distance a/sqrt2, a = 0.4078 nm (NAMED)
chk("0.1 nm < gold nearest-neighbour distance %.4f nm" % (NN_AU * 1e9), 1e-10 < NN_AU)
# non-retarded Lifshitz energy per area E/A = -H/(12 pi d^2); H from our plasma-model
# Lifshitz at small d: H_eff(d) = -12 pi d^2 E/A
d_small = 1e-9
H_eff = -12 * math.pi * d_small ** 2 * lifshitz_E_over_A(d_small, lambda xi: eps_plasma(xi, WP))
print("   plasma-model Hamaker at 1 nm, H = -12 pi d^2 E/A = %.3e J" % H_eff)
H_lit = 28e-20   # search-snippet SFA value for Au-air-Au (NOT READ; order-of-magnitude only)
for H, tag in ((H_eff, "plasma-model H"), (H_lit, "H = 28e-20 J (snippet, unread)")):
    E_nr = H / (12 * math.pi * (1e-10) ** 2)       # magnitude
    E_id = abs(ideal_E_over_A(1e-10))
    print("   at 0.1 nm, %s: |E/A|_nonret = %.3e J/m^2 vs ideal %.3e J/m^2, ratio %.3e"
          % (tag, E_nr, E_id, E_nr / E_id))
    chk("ideal formula exceeds the non-retarded magnitude at 0.1 nm (row strengthened)", E_nr < E_id)

b_nr01 = A.casimir_b_needed(1e-10) / math.sqrt(H_eff / (12 * math.pi * 1e-20) / abs(ideal_E_over_A(1e-10)))
print("   0.1 nm with the (out-of-validity) non-retarded plasma-model density: b = %.3e m = %.3g ly" % (b_nr01, b_nr01 / LY))
core_au = A.A_OVER_B * A.casimir_b_needed(1e-10) / 1.495978707e11
print("   tree's 'a core 0.02 of that' at 0.1 nm ideal: %.0f AU" % core_au)
chk("'thousands of astronomical units' (achievable.py:138-139) holds: 1e3 <= %.0f < 1e4" % core_au, 1e3 <= core_au < 1e4)

# ---------------------------------------------------------------- (D)
print("\n(D) DIRECTION")
chk("replacing the ideal formula by real gold moves b UP at both gaps; the row's "
    "'not an engineering programme' is not weakened", b_real10 > b_ideal10)
print("\nALL PASS" if ok_all else "\nSOME FAIL")
print("eta10_plasma=%.5f eta10_drude=%.5f b_real10=%.4e H_eff=%.4e" % (eta10p, eta10d, b_real10, H_eff))
sys.exit(0 if ok_all else 1)
