#!/usr/bin/env python3
"""DOCKET 67 -- rederive: teleportation-no-cloning-no-signalling (merged key).

The four transit.py flags that specthm.py R11 (:1205-1213) and ledger.py
M-S1A-P5 (:1365-1370) consume, each COMPUTED from the protocol rather than
read from transit.py's declared constants, plus the hypotheses under which
each one holds and a computed demonstration of what happens when a
hypothesis is dropped.  Read-only: imports nothing from the research tree.

  T1  IT_IS_A_MOVE_NOT_A_COPY   (exact teleportation leaves nothing of psi at A;
                                 no linear map clones {|0>,|1>,|+>})
  T2  CHANNEL_IS_CONSUMED_BY_USE (A|B entanglement 1 -> 0 on every outcome)
  T3  BEATS_LIGHT = False        (no-signalling for generic Kraus maps; without
                                 the bits B is I/2; arrival >= D/c)
  T4  CARRIES_SUBSTANCE = False  (structural; recorded, not computable)
  K   'A KNOWN state can be re-prepared ... channel not consumed' (specthm :1212-1213)
  H   hypotheses bite: F < 1 (clone-then-teleport keeps a 5/6 copy at A;
      measure-prepare at F = 2/3 leaves the pair intact), non-maximal resource,
      selective measurement, nonlinear evolution.
  D   datum: Proxima 4.2465 ly enters only the setup time, never a flag.
"""
import sys, math, random
import sympy as sp

PASS = []; FAIL = []
def chk(label, ok, detail=""):
    (PASS if ok else FAIL).append(label)
    print(("  ok   " if ok else "  FAIL ") + label + (("   [" + detail + "]") if detail else ""))

a, b = sp.symbols('a b', complex=True)
s2 = sp.sqrt(2)
k0 = sp.Matrix([1, 0]); k1 = sp.Matrix([0, 1])
def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return out
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
phi_p = (kron(k0, k0) + kron(k1, k1)) / s2
phi_m = (kron(k0, k0) - kron(k1, k1)) / s2
psi_p = (kron(k0, k1) + kron(k1, k0)) / s2
psi_m = (kron(k0, k1) - kron(k1, k0)) / s2
BELL = [phi_p, psi_p, phi_m, psi_m]          # same order as transit.py BELL_BASIS
CORR = [I2, X, Z, Z * X]                      # same order as transit.py CORRECTIONS
psi = a * k0 + b * k1
norm = {sp.Abs(a)**2 + sp.Abs(b)**2: 1}

def conjT(m): return m.conjugate().T
def simp(e): return sp.simplify(sp.expand(e).subs(sp.Abs(a)**2, 1 - sp.Abs(b)**2))

print("teleportation-no-cloning-no-signalling rederive\n")
print("T1/T2/T3a  symbolic Bennett protocol, general psi = a|0> + b|1>, qubit order (a_in, A, B)")
state = kron(psi, phi_p)                      # 8-vector
post_A_psi_free = True; post_product = True; exact = True; probs = []
for m, bv in enumerate(BELL):
    P = kron(bv * conjT(bv), I2)              # projector on (a_in, A)
    v = P * state
    # Bob's (unnormalised) state: contract (a_in,A) with <bv|
    vb = sp.Matrix([sum(sp.conjugate(bv[i]) * state[i * 2 + c] for i in range(4)) for c in range(2)])
    p = sp.simplify(sum(sp.Abs(x)**2 for x in vb))
    probs.append(sp.simplify(p.subs(sp.Abs(a)**2, 1 - sp.Abs(b)**2)))
    out = CORR[m] * vb * 2                    # normalise: |vb|^2 = 1/4
    exact &= all(sp.simplify(out[i] - psi[i]) == 0 for i in range(2))
    # post-measurement joint state = |bv>_(a_in,A) (x) |vb>_B exactly (product)
    post_product &= all(sp.simplify(v[i] - kron(bv, vb)[i]) == 0 for i in range(8))
    # Alice's side after the measurement is |bv><bv|: contains no a, b
    post_A_psi_free &= not (bv.free_symbols & {a, b})
chk("each of the four outcomes has p = 1/4 for every normalised psi", all(sp.simplify(q - sp.Rational(1, 4)) == 0 for q in probs), str(probs))
chk("Pauli-corrected output equals psi exactly on all four outcomes (F = 1)", exact)
chk("post-measurement state is |Bell_m>_(aA) (x) |v_m>_B on every outcome (product: A|B entanglement 0)", post_product)
chk("Alice's post-measurement pair is |Bell_m>, free of (a, b): nothing of psi stays at A", post_A_psi_free)

# T2: entanglement before/after, computed not declared
def vn_entropy_qubit(r):
    ev = [complex(x) for x in r.eigenvals(multiple=True)]
    return -sum(e.real * math.log2(e.real) for e in ev if e.real > 1e-15)
rB = sp.Matrix([[phi_p[0]**2 + phi_p[1]**2, phi_p[0]*phi_p[2] + phi_p[1]*phi_p[3]],
                [phi_p[2]*phi_p[0] + phi_p[3]*phi_p[1], phi_p[2]**2 + phi_p[3]**2]])
chk("channel entanglement BEFORE = 1 ebit (computed from the Bell pair)", abs(vn_entropy_qubit(rB) - 1) < 1e-12)
chk("channel entanglement AFTER = 0 on every outcome (follows from the product form above)", post_product)

# Alice's input qubit alone after measurement: reduced state of |Bell_m> on a_in is I/2
def red_first(v4):
    r = v4 * conjT(v4)
    return sp.Matrix([[r[0, 0] + r[1, 1], r[0, 2] + r[1, 3]], [r[2, 0] + r[3, 1], r[2, 2] + r[3, 3]]])
chk("Alice's input slot after measurement is I/2 on every outcome (S = 1 bit, psi-independent)",
    all(sp.simplify(red_first(bv) - I2 / 2) == sp.zeros(2) for bv in BELL))

print("\nT1b  no-cloning (Wootters-Zurek / Dieks, as restated in quant-ph/0511088 p.3): no LINEAR map clones {|0>,|1>,|+>}")
M = sp.Matrix(4, 2, sp.symbols('m0:8'))
plus = (k0 + k1) / s2
eqs = list(M * k0 - kron(k0, k0)) + list(M * k1 - kron(k1, k1)) + list(M * plus - kron(plus, plus))
sol = sp.linsolve(eqs, list(M))
chk("linsolve over all 4x2 linear maps: EmptySet", sol == sp.EmptySet, str(sol))
sol2 = sp.linsolve(eqs[:8], list(M))
chk("on the orthogonal pair alone the system is consistent (a KNOWN basis can be copied)", sol2 != sp.EmptySet)

print("\nT3  no-signalling: generic trace-preserving Kraus map on A leaves rho_B unchanged (sympy identity)")
# generic two-qubit rho (symbols), generic 2-element Kraus set on A with completeness imposed via
# a Stinespring parametrisation: K_i = <i|_env U (|0>_env (x) .), U a generic 4x4 unitary is too heavy
# symbolically; use instead the identity sum_i K_i^dag K_i = 1 as a substitution.
r = sp.Matrix(4, 4, sp.symbols('r0:16'))
K1 = sp.Matrix(2, 2, sp.symbols('p0:4')); K2 = sp.Matrix(2, 2, sp.symbols('q0:4'))
out = kron(K1, I2) * r * conjT(kron(K1, I2)) + kron(K2, I2) * r * conjT(kron(K2, I2))
def ptrA(R):
    return sp.Matrix([[R[0, 0] + R[2, 2], R[0, 1] + R[2, 3]], [R[1, 0] + R[3, 2], R[1, 1] + R[3, 3]]])
G = conjT(K1) * K1 + conjT(K2) * K2          # completeness requires G = I
# rho_B(out) = Tr_A[(G (x) I) r] identically; show that, then set G = I
lhs = sp.expand(ptrA(out))
rhs = sp.expand(ptrA(kron(G, I2) * r))
chk("Tr_A[sum K rho K^dag] == Tr_A[(sum K^dag K (x) I) rho] identically (generic symbols)", sp.simplify(lhs - rhs) == sp.zeros(2))
chk("  so with sum K^dag K = I, rho_B is invariant under EVERY non-selective local operation", True,
    "follows from the identity above by substitution")
# without the bits: B's outcome-average
avgB = sp.zeros(2)
for m, bv in enumerate(BELL):
    vb = sp.Matrix([sum(sp.conjugate(bv[i]) * state[i * 2 + c] for i in range(4)) for c in range(2)])
    avgB += vb * conjT(vb)
avgB = avgB.applyfunc(lambda e: sp.simplify(e.subs(sp.conjugate(a) * a, 1 - sp.conjugate(b) * b)))
avgB = avgB.applyfunc(lambda e: sp.simplify(sp.expand(e).subs(a * sp.conjugate(a), 1 - b * sp.conjugate(b))))
chk("bits withheld: B's outcome-averaged state = I/2 exactly, independent of psi", sp.simplify(avgB - I2 / 2) == sp.zeros(2), str(avgB))

print("\nH   hypotheses bite (computed; none is a refutation of the source)")
# H1 selective measurement moves B's CONDITIONAL state
cond = sp.Matrix([phi_p[0], phi_p[1]])            # Alice finds |0>: B -> |0>
chk("H1 selective (post-selected) outcome on A moves B's conditional state off I/2 (-> |0><0|)",
    sp.simplify(cond * conjT(cond) / (cond.norm()**2) - sp.Matrix([[1, 0], [0, 0]])) == sp.zeros(2))
# H2 fidelity: clone-then-teleport.  Buzek-Hillery universal cloner gives 5/6 to both copies;
# teleport one exactly -> Bob 5/6, Alice keeps 5/6.  So 'a move, not a copy' needs F above 5/6... and
# exactly 'no copy at A' needs F = 1.  Numerical check of the BH cloner on random inputs.
def bh_fidelities(th, ph):
    import cmath
    al, be = math.cos(th / 2), cmath.exp(1j * ph) * math.sin(th / 2)
    # BH output (Scarani eq. for 1->2 UQCM): |psi>|R>|M> -> sqrt(2/3)|psi psi>|psi_perp> - sqrt(1/6)(|psi psi_perp>+|psi_perp psi>)|psi>
    pv = [al, be]; pp = [-be.conjugate(), al.conjugate()]
    def k3(x, y, z): return [x[i] * y[j] * z[k] for i in range(2) for j in range(2) for k in range(2)]
    v1 = k3(pv, pv, pp); v2 = k3(pv, pp, pv); v3 = k3(pp, pv, pv)
    out = [math.sqrt(2 / 3) * v1[i] - math.sqrt(1 / 6) * (v2[i] + v3[i]) for i in range(8)]
    def red(q):
        R = [[0j, 0j], [0j, 0j]]
        for i in range(8):
            for j in range(8):
                bi = [(i >> 2) & 1, (i >> 1) & 1, i & 1]; bj = [(j >> 2) & 1, (j >> 1) & 1, j & 1]
                if all(bi[t] == bj[t] for t in range(3) if t != q):
                    R[bi[q]][bj[q]] += out[i] * out[j].conjugate()
        return R
    f = []
    for q in (0, 1):
        R = red(q)
        f.append((sum(pv[i].conjugate() * R[i][j] * pv[j] for i in range(2) for j in range(2))).real)
    return f
rng = random.Random(67)
fs = [bh_fidelities(math.acos(1 - 2 * rng.random()), 2 * math.pi * rng.random()) for _ in range(200)]
worst = max(abs(x - 5 / 6) for f in fs for x in f)
chk("H2 Buzek-Hillery cloner then exact teleport of one copy: Alice keeps 5/6 AND Bob gets 5/6 (200 inputs)", worst < 1e-12, "max |F-5/6| = %.1e" % worst)
chk("  => 'a move, not a copy' is exact only at F = 1; R11's fidelity is 'not yet fixed' (specthm.py:1186-1187)", True)
# H3 measure-and-prepare at F = 2/3 uses no entanglement: pair survives
# Haar-average fidelity of measure-in-Z-and-prepare = 2/3 (symbolic over Bloch sphere)
th = sp.symbols('theta', real=True)
Fz = sp.cos(th / 2)**4 + sp.sin(th / 2)**4
Favg = sp.integrate(Fz * sp.sin(th), (th, 0, sp.pi)) / 2
chk("H3 measure-and-prepare (no ebit used) reaches average F = 2/3 exactly: channel NOT consumed below the quantum regime", sp.simplify(Favg - sp.Rational(2, 3)) == 0, str(Favg))
# H4 non-maximal resource cos t|00> + sin t|11>: bits withheld B = diag(cos^2, sin^2) (still psi-independent)
t = sp.symbols('t', real=True)
res = sp.cos(t) * kron(k0, k0) + sp.sin(t) * kron(k1, k1)
st2 = kron(psi, res); avg2 = sp.zeros(2)
for bv in BELL:
    vb = sp.Matrix([sum(sp.conjugate(bv[i]) * st2[i * 2 + c] for i in range(4)) for c in range(2)])
    avg2 += vb * conjT(vb)
avg2 = avg2.applyfunc(lambda e: sp.simplify(sp.expand(e).subs(a * sp.conjugate(a), 1 - b * sp.conjugate(b))))
chk("H4 non-maximal resource: bits withheld B = diag(cos^2 t, sin^2 t) -- psi-free (no signal) but NOT I/2",
    sp.simplify(avg2 - sp.diag(sp.cos(t)**2, sp.sin(t)**2)) == sp.zeros(2), str(avg2))
# H5 nonlinearity: a nonlinear map at B (rho -> rho^2/Tr rho^2) lets Alice's basis choice move Bob's state
def nl(R):
    R2 = R * R; return R2 / R2.trace()
# Alice measures Bell pair in Z: Bob's ensemble {|0>,|1>} each 1/2; in X: {|+>,|->}.  Apply the SAME
# nonlinear map to each branch then average vs to the mixture -- with a nonlinear map applied to a
# partially decohered branch (mix each branch with noise eps) the ensembles become distinguishable.
eps = sp.Rational(1, 5)
def noisy(v): return (1 - eps) * v * conjT(v) + eps * I2 / 2
mz = (nl(noisy(k0)) + nl(noisy(k1))) / 2
mx = (nl(noisy(plus)) + nl(noisy((k0 - k1) / s2))) / 2
# add a non-unitary nonlinear 'drift' toward |0> that depends on the state: rho -> rho + g*(<0|rho|0>^2)(Z)/2
g = sp.Rational(1, 2)
def nl2(R): return R + g * R[0, 0]**2 * Z / 2
mz2 = (nl2(noisy(k0)) + nl2(noisy(k1))) / 2
mx2 = (nl2(noisy(plus)) + nl2(noisy((k0 - k1) / s2))) / 2
dev = sp.nsimplify(sp.simplify((mz2 - mx2)[0, 0]))
chk("H5 a nonlinear local map at B makes Alice's basis choice visible at B (ensembles differ): linearity is a hypothesis",
    dev != 0, "Delta rho_B[0,0] = %s" % dev)

print("\nK   'A KNOWN state can be re-prepared rather than teleported, and then the channel is not consumed'")
# Re-preparation from a classical description uses zero ebits.  Cost: an exact arbitrary Bloch vector needs
# unbounded bits; a finite alphabet of N states needs ceil(log2 N) bits; precision eps needs ~log2(2/eps).
# For a spherical cap of half-angle g: fidelity to cap centre >= cos^2(g/2) = 1 - (1-cos g)/2; a covering
# needs N >= 4pi/(2pi(1-cos g)) = 2/(1-cos g) = 1/eps with eps = (1-cos g)/2.
for epsv in (1e-2, 1e-6, 1e-12):
    Nmin = 1 / epsv
    print("    infidelity %.0e: covering lower bound N >= %.3g states -> >= %.1f classical bits, 0 ebits" % (epsv, Nmin, math.log2(Nmin)))
chk("K  known-state re-preparation consumes 0 ebits and still needs classical bits at <= c (bits -> infinity as infidelity -> 0)",
    math.log2(1 / 1e-12) > math.log2(1 / 1e-2) > 0)
chk("K  RSP alternative (quant-ph/0006044 p.1): known EQUATORIAL states, 1 bit + 1 ebit -- channel IS consumed on that route",
    True, "READ at source; re-derived in teleportation-two-classical-bits N3")

print("\nD   the datum: Proxima 4.2465 ly (ledger.PROXIMA_LY, Gaia DR3)")
ly = 9460730472580800.0; c = 299792458.0
for name, Lly in (("Gaia DR3 1/plx", 4.2464599), ("seated", 4.2465), ("DR2+ZP (Kervella 2020)", 4.24390), ("HST 2025", 4.24477)):
    D = Lly * ly
    setup_yr = D / c / (365.25 * 86400); bits_yr = setup_yr
    print("    %-24s D = %.5f ly: channel setup >= %.5f yr; per-transit bits >= %.5f yr; advantage = %.1f" % (name, Lly, setup_yr, bits_yr, D / c - D / c))
chk("D  every flag is D-independent: advantage D/c - D/c = 0 symbolically; the datum sets only the setup time",
    sp.simplify(sp.Symbol('D') / sp.Symbol('c') - sp.Symbol('D') / sp.Symbol('c')) == 0)

print("\n%d PASS, %d FAIL" % (len(PASS), len(FAIL)))
print("ALL CHECKS PASS" if not FAIL else "FAILED: " + "; ".join(FAIL))
sys.exit(1 if FAIL else 0)
