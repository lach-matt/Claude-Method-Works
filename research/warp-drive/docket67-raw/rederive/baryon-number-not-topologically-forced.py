#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'baryon-number-not-topologically-forced'.

Tree's use (permute.py:132-134, :346, :562-564): in a spatially closed universe
total electric charge is forced to zero by Gauss's law, and baryon number has
"no topological constraint; not forced".

What is checked here (all finite / closed form):

 B1  Standard-Model anomaly coefficients of U(1)_B, U(1)_L, U(1)_{B-L} (exact
     rationals, per generation, with and without nu_R), with the hypercharge
     anomaly cancellation as a sanity guard.  Shows: U(1)_B is ANOMALOUS in the
     SM (SU(2)^2 B and Y^2 B nonzero) -> it cannot be gauged with SM content, so
     there is no Gauss law for B; U(1)_{B-L} is anomaly-free with nu_R -> it CAN
     be gauged (the hypothesis the tree must name).
 B2  't Hooft counting: Delta B per unit Chern-Simons number = sum over SU(2)
     doublets of B = N_f; Delta B = Delta L; B-L unchanged.  With PDG 2026
     N_nu = 2.996 +- 0.007 -> N_f = 3 -> Delta B = 3 (quoted in 1710.07223 and
     2505.05607, READ).
 B3  The topological contrast behind 'not forced': the Gauss density rho d^3x =
     d(*E) is EXACT, so its integral over a closed slice is 0; the Skyrme baryon
     density is the pullback of the normalised volume form of S^3, CLOSED BUT NOT
     EXACT, so its integral over a closed slice is the map degree -- an integer,
     any integer.  (a) pointwise: the full -(1/24 pi^2) eps Tr(L L L) of the
     hedgehog equals -(sin^2F F')/(2 pi^2 r^2) at random points; (b) B = n for
     F(0) = n pi, F(inf) = 0, n = -3..3; (c) on the closed space S^3 itself the map
     (chi,th,ph) -> (n chi,th,ph) has degree n for n = 0..4.
     => closure QUANTISES B in this realisation (topological), but does NOT force
     its value: 'not forced' re-derived, 'no topological constraint' too strong.
 B4  z3 on a periodic 3x3x3 lattice (T^3): a Gauss-constrained charge
     (q = lattice divergence of integer link flux) has total != 0 UNSAT; a global
     number with no Gauss constraint has total = 1 SAT (vacuity guards SAT).
 B5  Data: the observed baryon-to-photon ratio from Planck 2018 Omega_b h^2 =
     0.0224 +- 0.0001 (1807.06209, READ): eta ~ 6.1e-10 != 0, while Omega_K =
     0.001 +- 0.002 cannot decide closure; and a Proca-type (massive) gauged B-L
     would not force the total either (sibling audit D5 mechanism, re-shown).
"""
import itertools
import math
import random
import sys

import sympy as sp

FAIL = []


def chk(label, got, want):
    ok = (got == want)
    print("  [%s] %s: got %r want %r" % ("ok" if ok else "FAIL", label, got, want))
    if not ok:
        FAIL.append(label)


R = sp.Rational

# ---------------------------------------------------------------- B1 anomalies
# left-handed Weyl fields, one generation: (name, dim3, dim2, Y, B, L)
GEN = [
    ("Q",   3, 2, R(1, 6),  R(1, 3),  0),
    ("u^c", 3, 1, R(-2, 3), R(-1, 3), 0),
    ("d^c", 3, 1, R(1, 3),  R(-1, 3), 0),
    ("L",   1, 2, R(-1, 2), 0,        1),
    ("e^c", 1, 1, R(1),     0,       -1),
]
NUR = ("nu^c", 1, 1, R(0), 0, -1)
T3 = R(1, 2)  # Dynkin index of the fundamental
T2 = R(1, 2)


def anomalies(fields, X):
    """X: function field -> charge.  Returns dict of anomaly coefficients."""
    a = dict(SU3sqX=0, SU2sqX=0, YsqX=0, gravX=0, X3=0, YX2=0)
    for f in fields:
        _, d3, d2, Y, _B, _L = f
        x = X(f)
        dim = d3 * d2
        if d3 == 3:
            a["SU3sqX"] += T3 * d2 * x
        if d2 == 2:
            a["SU2sqX"] += T2 * d3 * x
        a["YsqX"] += dim * Y ** 2 * x
        a["gravX"] += dim * x
        a["X3"] += dim * x ** 3
        a["YX2"] += dim * Y * x ** 2
    return {k: sp.nsimplify(v) for k, v in a.items()}


def B(f): return sp.S(f[4])
def L(f): return sp.S(f[5])
def BmL(f): return sp.S(f[4]) - sp.S(f[5])
def Y(f): return sp.S(f[3])


print("B1  anomaly coefficients per generation (left-handed Weyl basis)")
aY = anomalies(GEN, Y)
chk("sanity: SM hypercharge anomalies all cancel (Y^3, grav-Y, SU2^2 Y, SU3^2 Y)",
    (aY["X3"], aY["gravX"], aY["SU2sqX"], aY["SU3sqX"]), (0, 0, 0, 0))
aB = anomalies(GEN, B)
print("     U(1)_B :", aB)
chk("SU(3)^2 B", aB["SU3sqX"], 0)
chk("SU(2)^2 B  (nonzero -> B anomalous)", aB["SU2sqX"], R(1, 2))
chk("Y^2 B      (nonzero -> B anomalous)", aB["YsqX"], R(-1, 2))
chk("grav^2 B", aB["gravX"], 0)
chk("B^3", aB["X3"], 0)
chk("Y B^2", aB["YX2"], 0)
aL = anomalies(GEN, L)
chk("SU(2)^2 L equals SU(2)^2 B (so B-L is SU(2)-anomaly-free)", aL["SU2sqX"], aB["SU2sqX"])
chk("Y^2 L equals Y^2 B", aL["YsqX"], aB["YsqX"])
aBL = anomalies(GEN, BmL)
aBLn = anomalies(GEN + [NUR], BmL)
print("     U(1)_{B-L} without nu_R:", aBL)
print("     U(1)_{B-L} with nu_R   :", aBLn)
chk("B-L without nu_R: grav and cubic anomalies nonzero (-1 each in the LH basis)", (aBL["gravX"], aBL["X3"]), (-1, -1))
chk("B-L with one nu_R per generation: every anomaly vanishes (gaugeable)",
    tuple(aBLn.values()), (0, 0, 0, 0, 0, 0))
# B alone cannot be rescued by nu_R (nu_R carries no B)
aBn = anomalies(GEN + [NUR], B)
chk("U(1)_B stays anomalous with nu_R added", (aBn["SU2sqX"], aBn["YsqX"]), (R(1, 2), R(-1, 2)))

# ---------------------------------------------------------------- B2 't Hooft
print("\nB2  't Hooft zero-mode counting")
NU_PDG2026, NU_ERR = 2.9963, 0.007  # PDG 2026 S007NE 'Number of Light nu Types'
Nf = round(NU_PDG2026)
chk("N_f from PDG 2026 N_nu = 2.996 +- 0.007 (|N-3| < 1 sigma)",
    (Nf, abs(NU_PDG2026 - 3) < NU_ERR), (3, True))
dB = sum(f[1] * f[4] for f in GEN if f[2] == 2) * Nf   # one zero mode per doublet component-colour
dL = sum(f[1] * f[5] for f in GEN if f[2] == 2) * Nf
chk("Delta B per unit Delta N_CS = N_f = 3", dB, 3)
chk("Delta L per unit Delta N_CS = 3", dL, 3)
chk("Delta(B-L) = 0 (B-L survives the anomaly)", dB - dL, 0)
chk("Delta B = 2 N_f * A[SU(2)^2 B] (normalisation consistent)", 2 * Nf * aB["SU2sqX"], dB)

# ---------------------------------------------------------------- B3 topology
print("\nB3  exact vs closed-not-exact: Gauss density against Skyrme degree")
x, y, z = sp.symbols("x y z", real=True)
r = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
Fs = sp.Function("F")
I2 = sp.eye(2)
tau = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]),
       sp.Matrix([[1, 0], [0, -1]])]


def baryon_density_full(Fexpr):
    n = [x / r, y / r, z / r]
    U = sp.cos(Fexpr) * I2 + sp.I * sp.sin(Fexpr) * (n[0] * tau[0] + n[1] * tau[1] + n[2] * tau[2])
    Ud = U.H.subs({sp.conjugate(x): x, sp.conjugate(y): y, sp.conjugate(z): z})
    Li = [Ud * sp.diff(U, v) for v in (x, y, z)]
    return U, Li


# (a) pointwise, with a concrete profile F = pi*exp(-r) (F(0)=pi, F(inf)=0)
Fexpr = sp.pi * sp.exp(-r)
U, Li = baryon_density_full(Fexpr)
random.seed(67)
maxdev = 0.0
for _ in range(4):
    pt = {x: random.uniform(-1.5, 1.5), y: random.uniform(-1.5, 1.5), z: random.uniform(-1.5, 1.5)}
    Ln = [sp.N(M.subs(pt)) for M in Li]
    s = 0
    for (i, j, k) in itertools.permutations(range(3)):
        s += sp.LeviCivita(i, j, k) * (Ln[i] * Ln[j] * Ln[k]).trace()
    full = complex(sp.N(-s / (24 * sp.pi ** 2)))
    rr = float(sp.N(r.subs(pt)))
    Fv = math.pi * math.exp(-rr)
    Fp = -math.pi * math.exp(-rr)
    red = -(math.sin(Fv) ** 2 * Fp) / (2 * math.pi ** 2 * rr ** 2)
    maxdev = max(maxdev, abs(full.real - red), abs(full.imag))
print("     max |full eps Tr(LLL) density - reduced hedgehog density| = %.2e" % maxdev)
chk("full SU(2) baryon density equals the hedgehog reduction at 4 random points",
    maxdev < 1e-10, True)

# (b) degree on R^3 u {inf} = S^3 for F(0) = n pi
Fv_ = sp.symbols("Fv", real=True)
for n in range(-3, 4):
    # B = int 4 pi r^2 B0 dr = -(2/pi) int sin^2 F dF from F=n pi to 0
    Bn = sp.simplify(-(2 / sp.pi) * sp.integrate(sp.sin(Fv_) ** 2, (Fv_, n * sp.pi, 0)))
    chk("hedgehog with F(0) = %d pi has baryon number" % n, Bn, n)

# (c) on the closed space S^3: map (chi,th,ph) -> (n chi, th, ph), normalised volume 2 pi^2
chi, th, ph = sp.symbols("chi theta phi", real=True)
vol = sp.integrate(sp.sin(chi) ** 2 * sp.sin(th), (chi, 0, sp.pi), (th, 0, sp.pi), (ph, 0, 2 * sp.pi))
chk("vol(S^3) = 2 pi^2 (normalisation; nonzero => the volume form is NOT exact by Stokes)",
    sp.simplify(vol - 2 * sp.pi ** 2), 0)
for n in range(0, 5):
    f = n * chi
    deg = sp.integrate(sp.sin(f) ** 2 * sp.diff(f, chi) * sp.sin(th),
                       (chi, 0, sp.pi), (th, 0, sp.pi), (ph, 0, 2 * sp.pi)) / vol
    chk("degree of S^3 -> S^3 map chi -> %d chi (closed space, B = degree)" % n, sp.simplify(deg), n)
# Gauss contrast on S^3: an exact 3-form integrates to zero. rho = div E for
# E = grad(cos chi) (any global field works; this one is enough to show the shape)
phi_ = sp.cos(chi)
lap = sp.diff(sp.sin(chi) ** 2 * sp.diff(phi_, chi), chi) / sp.sin(chi) ** 2  # S^3 Laplacian, chi-only
Qtot = sp.integrate(lap * sp.sin(chi) ** 2 * sp.sin(th), (chi, 0, sp.pi), (th, 0, sp.pi), (ph, 0, 2 * sp.pi))
chk("Gauss density rho = div grad(cos chi) on S^3 integrates to 0 (exact form)", sp.simplify(Qtot), 0)

# ---------------------------------------------------------------- B4 z3 lattice
print("\nB4  z3: Gauss-constrained charge vs unconstrained global number on periodic 3^3")
try:
    import z3
    N = 3
    sites = list(itertools.product(range(N), repeat=3))
    link = {(s, d): z3.Int("l_%d%d%d_%d" % (s + (d,))) for s in sites for d in range(3)}

    def nb(s, d, sgn):
        t = list(s); t[d] = (t[d] + sgn) % N; return tuple(t)

    q = {s: z3.Sum([link[(s, d)] - link[(nb(s, d, -1), d)] for d in range(3)]) for s in sites}
    tot = z3.Sum(list(q.values()))
    so = z3.Solver(); so.add(tot != 0)
    chk("Gauss-constrained: 'total charge != 0' over all integer link fields", str(so.check()), "unsat")
    sv = z3.Solver(); sv.add(q[(0, 0, 0)] == 1)
    chk("vacuity guard: a nonzero local charge exists", str(sv.check()), "sat")
    bnum = {s: z3.Int("b_%d%d%d" % s) for s in sites}
    sb = z3.Solver(); sb.add(z3.Sum(list(bnum.values())) == 1)
    chk("global number, no Gauss constraint: total = 1 is satisfiable", str(sb.check()), "sat")
except ImportError:
    print("  [skip] z3 not installed (pip install z3-solver)")
    FAIL.append("z3 missing")

# ---------------------------------------------------------------- B5 data
print("\nB5  data")
zeta3 = float(sp.zeta(3))
kB, hbar, c, G = 1.380649e-23, 1.054571817e-34, 299792458.0, 6.67430e-11
Tcmb = 2.7255
Mpc = 3.0856775814913673e22
n_gamma = 2 * zeta3 / math.pi ** 2 * (kB * Tcmb / (hbar * c)) ** 3
H100 = 100e3 / Mpc
rho_c_h2 = 3 * H100 ** 2 / (8 * math.pi * G)
m_p = 1.67262192369e-27
for obh2 in (0.0224, 0.0223, 0.0225):
    eta = obh2 * rho_c_h2 / m_p / n_gamma
    print("     Omega_b h^2 = %.4f  ->  n_gamma = %.1f cm^-3, eta = %.3e" % (obh2, n_gamma * 1e-6, eta))
eta0 = 0.0224 * rho_c_h2 / m_p / n_gamma
chk("eta from Planck 2018 is ~6.1e-10 (nonzero net B observed)", round(eta0 * 1e10, 1), 6.1)
# Omega_K = -k/(a H)^2: a closed (k=+1) universe has Omega_K < 0
OmK, sOmK = 0.001, 0.002
chk("Planck+BAO Omega_K = 0.001 +- 0.002 admits closed (Omega_K<0) within 2 sigma, and open",
    (OmK - 2 * sOmK < 0 < OmK + 2 * sOmK), True)
# Proca/massive gauged B-L on T^3: -lap A0 + m^2 A0 = rho, uniform rho0 solved by A0 = rho0/m^2
m, rho0 = sp.symbols("m rho0", positive=True)
A0 = rho0 / m ** 2
resid = -sum(sp.diff(A0, v, 2) for v in (x, y, z)) + m ** 2 * A0 - rho0
chk("massive (Higgsed) gauged B-L: uniform net charge solves the constraint on T^3", sp.simplify(resid), 0)

print()
if FAIL:
    print("FAILED: %d check(s): %s" % (len(FAIL), FAIL))
    sys.exit(1)
print("ALL CHECKS PASS")
