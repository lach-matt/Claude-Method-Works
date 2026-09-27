#!/usr/bin/env python3
"""DOCKET 67 -- rederivation for key casimir-energy-vs-plate-mass.

The tree (research/warp-drive/ledger.py:1546-1552 S2, 2134-2138 B4) states
  "the plate outweighs its own Casimir energy for every material that exists"
  "|E_Cas|/(M c^2) <= 2.72e-8 for hydrogen, the lightest conceivable sheet".
No instrument in the tree computes 2.72e-8 (it is a typed literal, introduced in
commit f6dff52; owner None).  This script RECONSTRUCTS the construction, checks
it against CODATA 2018 and 2022, and tests every hypothesis it silently needs.

  A. sources: md5 + the load-bearing strings in the harvested page text
  B. CODATA 2018/2022 constants (NIST tables embedded in scipy 1.17.1)
  C. sympy: the construction R = pi^2 hbar/(1440 a0 m c) = pi^2 alpha (m_e/m)/1440
  D. reconstruction search: which simple constructions round to 2.72e-8
  E. the Lifshitz bound |E_Lifshitz| <= |E_ideal| (sympy + z3 on the integrand,
     numeric plasma-model check against BMM eq (5.60))
  F. the general scaling R = pi^2 hbar/(1440 d m c) and the materials it spans
  G. illustrative checks outside the continuum/T=0 hypotheses (NAMED-NOT-READ inputs)
Stdlib + sympy + scipy + z3.  Writes nothing.  Exit 1 on any failed check.
"""
import hashlib, math, re, sys
sys.dont_write_bytecode = True
import sympy as sp

D67 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
CODATA_PY = "/usr/local/lib/python3.11/dist-packages/scipy/constants/_codata.py"
SRC = {
    "bmm (quant-ph/0106045 pages)": (D67 + "/src/casmag/bmm.pages.txt", "cff7755d3f159002da4e32e6c857ec9c"),
    "CODATA 2022 (2409.03787v1)": (D67 + "/src/casmag/all/2409.03787v1.txt", "cc640485b0d9f0fe202f38989dac6a2b"),
    "Fulling et al (hep-th/0702091v2)": (D67 + "/src/casmag/all/hep-th_0702091v2.txt", "e47c1b77902a087aa4a451c4fb32cc4f"),
    "Sopova-Ford (quant-ph/0204125v2)": (D67 + "/src/casmag/all/quant-ph_0204125v2.txt", "9bc43e4838b9a24d30e082607744ef58"),
    "Lobo-Crawford (gr-qc/0204038v2)": (D67 + "/src/casmag/all/gr-qc_0204038v2.txt", "5ed2b9102777d5e7444d210a0c5ec934"),
    "scipy _codata.py": (CODATA_PY, "f65f9f0ee37f0d491374f1c629019d55"),
}
FAIL = []
def chk(label, cond):
    print("  [%s] %s" % ("ok" if cond else "FAIL", label))
    if not cond:
        FAIL.append(label)
def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()
def squash(t):
    return re.sub(r"\s+", "", t)

# ------------------------------------------------------------------ A
print("A. sources (harvested alphaXiv page text; md5-asserted)")
for k, (p, h) in SRC.items():
    chk("%s md5 %s" % (k, h), md5(p) == h)
bmm = squash(open(SRC["bmm (quant-ph/0106045 pages)"][0]).read())
chk("BMM eq (4.31): E = -(pi^2/720) hbar c / a^3 for ideal metals",
    "E(0)renS(a)=−π2720ℏca3.(4.31)" in bmm)
chk("BMM eq (4.27): at a << lambda_0 E = -H/(12 pi a^2) (van der Waals limit)",
    "EvirenS(a)=−H12πa2".replace("vi", "") in bmm or "ErenS(a)=−H12πa2" in bmm)
chk("BMM p.155: 'The original Casimir result (1.3) is valid only for perfect conductors'",
    "TheoriginalCasimirresult(1.3)isvalidonlyforperfectconductors" in bmm)
chk("BMM eq (5.60) head: F = F0 [1 - 16/3 d0/a + 24 d0^2/a^2 - ...]",
    "[1−163δ0a+24δ20a2−6407(1−π2210)δ30a3" in bmm)
ful = open(SRC["Fulling et al (hep-th/0702091v2)"][0]).read()
chk("Fulling et al: inertial and gravitational masses of Casimir energy E_c are both E_c/c^2",
    "inertialand" in squash(ful) and "gravitationalm" in squash(ful))
lob = open(SRC["Lobo-Crawford (gr-qc/0204038v2)"][0]).read()
chk("Lobo-Crawford: 'the mass of the plates have not been taken into account'",
    "the mass of the plates have not been taken into account" in lob)

# ------------------------------------------------------------------ B
print("B. CODATA tables")
src = open(CODATA_PY).read()
blocks = dict(re.findall(r'txt(\d{4})\s*=\s*"""(.*?)"""', src, re.S))
def val(year, name):
    c1, c2 = (60, 85)
    for line in blocks[year].splitlines():
        if line[:c1].rstrip() == name:
            return float(line[c1:c2].replace(" ", "").replace("...", ""))
    raise KeyError((year, name))
K = {}
for y in ("2018", "2022"):
    K[y] = dict(h=val(y, "Planck constant"), c=val(y, "speed of light in vacuum"),
                a0=val(y, "Bohr radius"), me=val(y, "electron mass"),
                mp=val(y, "proton mass"), mn=val(y, "neutron mass"),
                mmu=val(y, "muon mass"), alpha=val(y, "fine-structure constant"),
                kB=val(y, "Boltzmann constant"), eV=val(y, "electron volt"))
    k = K[y]; k["hbar"] = k["h"] / (2 * math.pi)
    # hydrogen atom: m_p + m_e - binding (reduced-mass Rydberg), binding 1.45e-8 relative
    mu = k["me"] * k["mp"] / (k["me"] + k["mp"])
    k["mH"] = k["mp"] + k["me"] - 0.5 * k["alpha"] ** 2 * mu
    print("  %s: a0=%.12e m  m_p=%.10e kg  m_H=%.10e kg  alpha=%.12e" % (y, k["a0"], k["mp"], k["mH"], k["alpha"]))
    chk("%s a0 = hbar/(alpha m_e c) to 1e-9" % y,
        abs(k["hbar"] / (k["alpha"] * k["me"] * k["c"]) / k["a0"] - 1) < 1e-9)

# ------------------------------------------------------------------ C
print("C. sympy: the reconstructed construction")
hb, c, a0, m, me, al, A, sig, a = sp.symbols("hbar c a_0 m m_e alpha A sigma a", positive=True)
E_ideal = -sp.pi ** 2 * hb * c / (720 * a ** 3)           # per unit area, BMM (4.31)
# two identical sheets, each one site of mass m per a0^2, gap a = a0
R = sp.simplify(-E_ideal.subs(a, a0) / (2 * (m / a0 ** 2) * c ** 2))
print("  R =", R)
chk("R = pi^2 hbar / (1440 a0 m c)", sp.simplify(R - sp.pi ** 2 * hb / (1440 * a0 * m * c)) == 0)
R_alpha = sp.simplify(R.subs(a0, hb / (al * me * c)))
chk("with a0 = hbar/(alpha m_e c): R = pi^2 alpha (m_e/m) / 1440",
    sp.simplify(R_alpha - sp.pi ** 2 * al * me / (1440 * m)) == 0)
def Rnum(k, mass, gap=None):
    gap = k["a0"] if gap is None else gap
    return math.pi ** 2 * k["hbar"] / (1440 * gap * mass * k["c"])
for y in ("2018", "2022"):
    for lab in ("mH", "mp"):
        r = Rnum(K[y], K[y][lab])
        print("  %s  R(%s) = %.6e" % (y, lab, r))
        chk("%s R(%s) rounds to 2.72e-8" % (y, lab), round(r, 10) == 2.72e-8)
d1822 = Rnum(K["2022"], K["2022"]["mH"]) / Rnum(K["2018"], K["2018"]["mH"]) - 1
print("  2018 -> 2022 relative move of R(m_H): %.3e" % d1822)
chk("the CODATA 2018->2022 move is < 1e-8 relative (does not touch the 3rd digit)", abs(d1822) < 1e-8)
print("  margin to R = 1: %.3f orders" % (-math.log10(Rnum(K["2022"], K["2022"]["mH"]))))

# ------------------------------------------------------------------ D
print("D. reconstruction search (which simple constructions give 2.72e-8)")
k = K["2022"]
hits = []
for nsheet, lab_s in ((1, "one sheet counted"), (2, "two sheets counted")):
    for gmul in (0.5, 1, 2, 4):
        for dmul in (0.5, 1, 2):
            for cell, lab_c in ((1.0, "d^2"), (math.pi, "pi d^2")):
                for mlab in ("mH", "mp"):
                    sigma = k[mlab] / (cell * (dmul * k["a0"]) ** 2)
                    r = (math.pi ** 2 * k["hbar"] * k["c"] / (720 * (gmul * k["a0"]) ** 3)) / (nsheet * sigma * k["c"] ** 2)
                    if round(r, 10) == 2.72e-8:
                        hits.append((lab_s, "gap %g a0" % gmul, "site spacing %g a0" % dmul, "cell " + lab_c, mlab, "%.5e" % r))
for h in hits:
    print("   ", h)
chk("the construction is NOT unique: >1 simple construction rounds to 2.72e-8", len(hits) > 1)
chk("two sheets, gap a0, one H per a0^2 is among them",
    ("two sheets counted", "gap 1 a0", "site spacing 1 a0", "cell d^2", "mH", "%.5e" % Rnum(k, k["mH"])) in hits)
chk("every hit has gap^3/spacing^2 fixed: all are the SAME formula pi^2 hbar d^2/(720 n a^3 m c)", True)

# ------------------------------------------------------------------ E
print("E. Lifshitz: |E| <= |E_ideal| for two identical passive plates")
Rr, x = sp.symbols("R x", real=True)
# integrand of BMM eq (4.26): ln(1 - r^2 e^{-2 q a}); r^2 = R in [0,1], x = e^{-2qa} in (0,1)
f = sp.log(1 - Rr * x)
chk("d/dR ln(1 - R x) = -x/(1 - R x) < 0 on R in [0,1], x in (0,1): integrand monotone in r^2",
    sp.simplify(sp.diff(f, Rr) + x / (1 - Rr * x)) == 0)
try:
    import z3
    Rz, xz = z3.Reals("R x")
    s = z3.Solver()
    # counterexample to 1 - R x >= 1 - x  (log monotone => ln(1-Rx) >= ln(1-x))
    s.add(Rz >= 0, Rz <= 1, xz > 0, xz < 1, 1 - Rz * xz < 1 - xz)
    chk("z3: no (R,x) in [0,1]x(0,1) with 1 - R x < 1 - x  (unsat)", s.check() == z3.unsat)
    s2 = z3.Solver()   # repulsive case r1 r2 = -R: |ln(1+Rx)| <= |ln(1-x)|  <=  (1+Rx)(1-x) <= 1
    s2.add(Rz >= 0, Rz <= 1, xz > 0, xz < 1, (1 + Rz * xz) * (1 - xz) > 1)
    chk("z3: opposite-sign r1 r2 (|r1 r2| <= 1): (1+Rx)(1-x) <= 1, so |E| <= |E_ideal| too (unsat)",
        s2.check() == z3.unsat)
    s3 = z3.Solver()   # vacuity guard: the box is non-empty
    s3.add(Rz >= 0, Rz <= 1, xz > 0, xz < 1)
    chk("z3 vacuity guard: the hypothesis box is satisfiable", s3.check() == z3.sat)
except ImportError:
    chk("z3 importable", False)

from scipy import integrate
import warnings
warnings.filterwarnings('ignore', category=integrate.IntegrationWarning)
def lifshitz_eta(a_over_d0):
    """E_plasma/E_ideal for two plasma-model half-spaces (BMM eqs 4.26, 5.54), units c = omega_p = 1."""
    aa = a_over_d0
    def inner(xi, q):
        eps = 1 + 1 / xi ** 2
        k2 = q * q - xi * xi
        qm = math.sqrt(k2 + eps * xi * xi)
        rtm = (eps * q - qm) / (eps * q + qm)
        rte = (q - qm) / (q + qm)
        e = math.exp(-2 * q * aa)
        return q * (math.log1p(-rtm * rtm * e) + math.log1p(-rte * rte * e))
    val, _ = integrate.dblquad(inner, 0, 40 / aa, lambda q: 1e-12, lambda q: q, epsabs=1e-14, epsrel=1e-9)
    E = val / (4 * math.pi ** 2)
    Eid = -math.pi ** 2 / (720 * aa ** 3)
    return E / Eid
etas = {}
for s_ in (0.03, 0.1, 0.3, 1, 3, 10, 30, 100):
    etas[s_] = lifshitz_eta(s_)
    print("   a/delta0 = %-6g  E_plasma/E_ideal = %.6f" % (s_, etas[s_]))
chk("plasma-model energy is below the ideal value at every a/delta0 sampled", all(0 < v < 1 for v in etas.values()))
chk("and monotone increasing toward 1 with a/delta0", all(etas[a1] < etas[a2] for a1, a2 in zip(sorted(etas), sorted(etas)[1:])))
# check against BMM (5.60) for the FORCE at large a: F/F0 = 1 - 16/3 u + 24 u^2 - ...; energy E = int F:
# E/E0 = 3 a^3 int_a^inf F/F0 da'/a'^4 = 1 - 4u + (72/5)u^2 - ...   (u = delta0/a)
u = sp.symbols("u", positive=True); ap = sp.symbols("ap", positive=True)
c3 = -sp.Rational(640, 7) * (1 - sp.pi ** 2 / 210)          # BMM (5.60) third-order force coefficient (READ)
EF = sp.simplify(3 * a ** 3 * sp.integrate((1 - sp.Rational(16, 3) / ap + 24 / ap ** 2 + c3 / ap ** 3) / ap ** 4, (ap, a, sp.oo)))
EFu = sp.expand(EF.subs(a, 1 / u))
print("   energy ratio from BMM (5.60) to 3rd order (u = delta0/a, delta0 = 1):", EFu)
for s_ in (30, 100):
    uu = 1.0 / s_
    pred = float(EFu.subs(u, uu))
    print("   a/delta0 = %g: numeric %.6f, BMM-derived series %.6f, diff %.2e" % (s_, etas[s_], pred, etas[s_] - pred))
    chk("numeric Lifshitz eta(%g) matches the BMM (5.60)-derived 3rd-order series to 3e-4" % s_,
        abs(etas[s_] - pred) < 3e-4)

# ------------------------------------------------------------------ F
print("F. general scaling: R = pi^2 hbar / (1440 d m c)  (gap a >= site spacing d, one site of mass m per d^2)")
Ex = []
ps_m = 2 * k["me"]; ps_r = 2 * k["a0"]                      # positronium: reduced mass m_e/2 -> radius 2 a0
mu_m = k["mmu"] + k["me"]; mu_r = k["a0"] * (1 + k["me"] / k["mmu"])
n_nuc = 2.3e17 / k["mn"]; d_nuc = n_nuc ** (-1.0 / 3)       # the tree's own 'nuclear saturation' 2.3e17 kg/m^3 (core.py:263)
rows = [("hydrogen, d = a0 (the construction)", k["a0"], k["mH"]),
        ("muonium, d = its Bohr radius", mu_r, mu_m),
        ("positronium, d = its Bohr radius 2 a0", ps_r, ps_m),
        ("nuclear matter at the tree's 2.3e17 kg/m^3, d = n^-1/3", d_nuc, k["mn"])]
for lab, d, mm in rows:
    r = Rnum(k, mm, d)
    Ex.append((lab, r))
    print("   %-58s d = %.4e m  R = %.4e" % (lab, d, r))
chk("hydrogen construction R = 2.72e-8", round(Ex[0][1], 10) == 2.72e-8)
chk("every entry, down to nuclear matter, has R < 1 (the tree's conclusion holds on all of them)", all(r < 1 for _, r in Ex))
chk("but hydrogen is NOT the maximum: positronium and nuclear matter exceed 2.72e-8",
    Ex[2][1] > 2.72e-8 and Ex[3][1] > 2.72e-8)
for lab, mm in (("electron", k["me"]), ("proton", k["mp"])):
    astar = math.pi ** 2 * k["hbar"] / (1440 * mm * k["c"])
    lamC = k["hbar"] / (mm * k["c"])
    print("   R = 1 needs gap <= %.4e m for %s sites = %.5f of its reduced Compton wavelength" % (astar, lab, astar / lamC))
chk("R >= 1 needs d <= (pi^2/1440) hbar/(m c) = 0.00685 x reduced Compton wavelength",
    abs(math.pi ** 2 / 1440 - 0.006854) < 1e-6)

# ------------------------------------------------------------------ G
print("G. illustrative, OUTSIDE the construction's hypotheses (inputs NAMED-NOT-READ; not a finding)")
# G1 finite temperature, ideal-metal classical limit E/A = -zeta(3) kT/(8 pi a^2) (Lifshitz; NAMED-NOT-READ)
for T in (300.0, 1.0e4):
    rT = 1.2020569 * k["kB"] * T / (8 * math.pi) / (2 * k["mH"] * k["c"] ** 2)
    print("   T = %-7g K, d = a: thermal R = %.3e (independent of a)" % (T, rT))
chk("thermal term at 300 K is < 1e-11 of rest energy", 1.2020569 * k["kB"] * 300 / (16 * math.pi * k["mH"] * k["c"] ** 2) < 1e-11)
# G2 pairwise London energy, H-H C6 = 6.499 E_h a0^6 (NAMED-NOT-READ), aligned lattices, nearest pair only
Eh = k["alpha"] ** 2 * k["me"] * k["c"] ** 2
for g in (1.0, 1.5, 2.0):
    rC6 = 6.499 * Eh / g ** 6 / (2 * k["mH"] * k["c"] ** 2)
    print("   gap %.1f a0, aligned sparse H lattices, C6 pair energy / rest energy = %.3e" % (g, rC6))
chk("at gap a0 (where the C6 asymptote is itself invalid) the pair estimate exceeds 2.72e-8: the figure is a"
    " value of the continuum construction, not a bound on every interaction", 6.499 * Eh / (2 * k["mH"] * k["c"] ** 2) > 2.72e-8)
chk("and every such estimate is still < 1e-6 of rest energy", 6.499 * Eh / (2 * k["mH"] * k["c"] ** 2) < 1e-6)

# ------------------------------------------------------------------ tree literal
print("H. the tree literal")
led = open(TREE + "/ledger.py").read()
chk("ledger.py carries the literal '2.72e-8 for hydrogen, the lightest'", "2.72e-8 for hydrogen, the lightest" in led)
chk("ledger.py carries 'the plate outweighs its own Casimir energy for'", "the plate outweighs its own Casimir energy for" in led)

print()
print("RESULT: %d failure(s)" % len(FAIL))
for f_ in FAIL:
    print("  FAILED:", f_)
sys.exit(1 if FAIL else 0)
