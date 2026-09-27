#!/usr/bin/env python3
"""
DOCKET 67 audit -- teleportation-transfers-state-not-matter.

Re-derives, symbolically (sympy), what is finite and closed-form in the claim
    transit.py:56-59 "Teleportation writes a quantum state onto matter ALREADY AT
    THE DESTINATION.  It moves no mass and no energy."

PART 1  Bennett et al. 1993 (read via restatement: Pirandola et al. 2015,
        arXiv:1505.07831 p.1-2; Boschi et al. quant-ph/9710013 p.1-2):
        arbitrary a|0>+b|1>, four Bell outcomes, p = 1/4 each, output = input
        after the Pauli correction.  Symbolic, all a, b.
PART 2  Energy accounting of standard teleportation (Hotta 2011, arXiv:1101.3954
        p.4 example): uncoupled H = w*sz on every qubit.  (i) Alice's Bell
        measurement changes Bob's AVERAGE energy by exactly 0 (for all a, b);
        (ii) Bob's local correction changes it by w(|a|^2-|b|^2), which his own
        device supplies/absorbs; (iii) so no energy crosses the channel -- the
        state's energy is paid at the destination.
PART 3  The named exception, Quantum Energy Teleportation (Hotta 2011 sec.3,
        minimal model; Ikeda 2023 arXiv:2301.02666 Table II): coupled
        H = H_A + H_B + V with ground-state entanglement.  Verify <g|H_A|g> =
        <g|H_B|g> = <g|V|g> = 0, H >= 0, E_A = h^2/sqrt(h^2+k^2) (eq. 8),
        E_B (eq. 14 and max eq. 11) > 0, E_B <= E_A, Alice's measurement leaves
        <H_B>,<V> at 0, and an alpha-INDEPENDENT Bob unitary extracts <= 0.
        Reproduce Ikeda's analytical <E_1> column.
Exit 0 iff every check passes.
"""
import sys, random, math
import sympy as sp

bad = 0
def chk(name, ok):
    global bad
    print(("  ok    " if ok else "  FAIL  ") + name)
    if not ok: bad += 1

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return out
def dag(m): return m.conjugate().T

# ---------------------------------------------------------------- PART 1
print("PART 1  Bennett 1993 teleportation, symbolic in (a, b)")
a, b = sp.symbols('a b', complex=True)
ar, ai, br, bi = sp.symbols('ar ai br bi', real=True)
subsAB = {a: ar + sp.I*ai, b: br + sp.I*bi}
norm = {}
psi = sp.Matrix([a, b])
s2 = 1/sp.sqrt(2)
bell = [s2*sp.Matrix([1, 0, 0, 1]), s2*sp.Matrix([0, 1, 1, 0]),
        s2*sp.Matrix([1, 0, 0, -1]), s2*sp.Matrix([0, 1, -1, 0])]
corr = [I2, X, Z, Z*X]
state = kron(psi, bell[0])        # qubits: a (input), A (Alice's half), B (Bob's)
outs = []
for k, bv in enumerate(bell):
    proj = kron(dag(bv), I2)      # <bell_k|_{aA} (x) 1_B
    vB = proj*state               # unnormalised Bob vector
    pk = sp.simplify((dag(vB)*vB)[0].subs(subsAB).expand())
    pk_norm = sp.simplify(pk.subs(ar**2, 1 - ai**2 - br**2 - bi**2))
    fixed = sp.simplify(corr[k]*vB*2)   # times 2 = 1/sqrt(p_k) with p_k = 1/4
    outs.append((pk_norm, fixed))
    chk(f"outcome {k}: p = 1/4 for every normalised (a,b)", sp.simplify(pk_norm - sp.Rational(1, 4)) == 0)
    chk(f"outcome {k}: corrected output == input exactly", sp.simplify(fixed - psi) == sp.zeros(2, 1))

# ---------------------------------------------------------------- PART 2
print("\nPART 2  energy accounting, uncoupled H = w*sz per qubit (Hotta 2011 p.4)")
w = sp.symbols('w', positive=True)
HB = kron(I2, I2, w*Z)
rho0 = state*dag(state)
EB_before = sp.simplify((rho0*HB).trace().subs(subsAB))
chk("Bob's energy in the shared Bell state = 0", sp.simplify(EB_before) == 0)
# after Alice's Bell measurement, bits withheld (non-selective)
EB_nobits = 0
EB_bits = 0
for k, bv in enumerate(bell):
    P = kron(bv*dag(bv), I2)
    rk = P*rho0*P
    EB_nobits += (rk*HB).trace()
    U = kron(I2, I2, corr[k])
    EB_bits += (U*rk*dag(U)*HB).trace()
EB_nobits = sp.simplify(sp.expand(EB_nobits.subs(subsAB)))
EB_bits = sp.simplify(sp.expand(EB_bits.subs(subsAB)))
target = sp.expand((w*(sp.Abs(a)**2 - sp.Abs(b)**2)).subs(subsAB))
chk("Alice's measurement changes Bob's average energy by exactly 0", EB_nobits == 0)
chk("after correction Bob's energy = w(|a|^2-|b|^2)", sp.simplify(EB_bits - target) == 0)
print("    -> the change w(|a|^2-|b|^2) is made by Bob's LOCAL unitary: his device pays it")
# no-signalling of energy under ANY Alice unitary on (a, A): numeric random check
rng = random.Random(67)
def rand_u4():
    M = sp.Matrix(4, 4, lambda i, j: complex(rng.gauss(0, 1), rng.gauss(0, 1)))
    Q, _ = M.QRdecomposition()
    return Q
num = {ar: 0.6, ai: 0.0, br: 0.0, bi: 0.8}
rho_num = rho0.subs(subsAB).subs(num).evalf()
dev = 0.0
for _ in range(3):
    UA = sp.kronecker_product(rand_u4(), I2)
    dev = max(dev, abs(complex((UA*rho_num*dag(UA)*HB.subs(w, 1)).trace().evalf())))
chk(f"any Alice unitary: Bob's energy stays 0 (max dev {dev:.1e})", dev < 1e-12)

# ---------------------------------------------------------------- PART 3
print("\nPART 3  QET minimal model (Hotta 2011 sec.3; Ikeda 2023)")
h, k = sp.symbols('h k', positive=True)
r = sp.sqrt(h**2 + k**2)
HA = h*kron(Z, I2) + h**2/r*kron(I2, I2)
HBq = h*kron(I2, Z) + h**2/r*kron(I2, I2)
V = 2*k*kron(X, X) + 2*k**2/r*kron(I2, I2)
H = HA + HBq + V
g = s2*sp.sqrt(1 - h/r)*sp.Matrix([1, 0, 0, 0]) - s2*sp.sqrt(1 + h/r)*sp.Matrix([0, 0, 0, 1])
ev = lambda O, v: sp.simplify((v.T*O*v)[0])   # g is real: transpose, not conjugate
chk("<g|g> = 1", sp.simplify((g.T*g)[0] - 1) == 0)
chk("<g|H_A|g> = 0", ev(HA, g) == 0)
chk("<g|H_B|g> = 0", ev(HBq, g) == 0)
chk("<g|V|g> = 0", ev(V, g) == 0)
R = sp.Rational
Hg = H*g   # sympy.simplify does not close the nested radicals; evaluate at 6 points to 50 digits
okHg = all(max(abs(sp.N(c.subs({h: hv, k: kv}), 50)) for c in Hg) < sp.Float('1e-45')
           for hv, kv in [(1, R(1,10)), (1, R(1,5)), (1, R(1,2)), (1, 1), (R(3,2), 1), (R(1,5), 5)])
chk("H|g> = 0 (ground energy 0; 6 points, 50-digit)", okHg)
eigs = [sp.simplify(e) for e in H.subs({h: 1, k: sp.Rational(1, 2)}).eigenvals()]
chk("H >= 0 (all eigenvalues >= 0 at h=1,k=1/2)", all(sp.N(e) > -1e-12 for e in eigs))
PA = {al: (kron(I2, I2) + al*kron(X, I2))/2 for al in (1, -1)}
rhoM = sum((PA[al]*g*g.T*PA[al] for al in (1, -1)), sp.zeros(4, 4))
EA = sp.simplify((rhoM*H).trace())
chk("E_A = h^2/sqrt(h^2+k^2)  (eq. 8)", sp.simplify(EA - h**2/r) == 0)
chk("after Alice's measurement <H_B> = 0", sp.simplify((rhoM*HBq).trace()) == 0)
chk("after Alice's measurement <V> = 0", sp.simplify((rhoM*V).trace()) == 0)
th = sp.symbols('theta', real=True)
UB = {al: sp.cos(th)*kron(I2, I2) - sp.I*al*sp.sin(th)*kron(I2, Y) for al in (1, -1)}
rhoF = sum((UB[al]*PA[al]*g*g.T*PA[al]*dag(UB[al]) for al in (1, -1)), sp.zeros(4, 4))
EB = sp.simplify(EA - (rhoF*H).trace())
EB14 = (h*k*sp.sin(2*th) - (h**2 + 2*k**2)*(1 - sp.cos(2*th)))/r
chk("E_B(theta) = eq. (14)", sp.simplify(sp.expand_trig(EB - EB14)) == 0)
D = sp.sqrt((h**2 + 2*k**2)**2 + h**2*k**2)
EB_max_sub = ((h*k*(h*k/D) - (h**2 + 2*k**2)*(1 - (h**2 + 2*k**2)/D))/r)
EB11 = (h**2 + 2*k**2)/r*(sp.sqrt(1 + h**2*k**2/(h**2 + 2*k**2)**2) - 1)
okmax = all(abs(float((EB_max_sub - EB11).subs({h: hv, k: kv}))) < 1e-12
            for hv, kv in [(1, .1), (1, .2), (1, .5), (1, 1), (1.5, 1), (3, .7)])
chk("eq. (14) at eqs. (9)-(10) = eq. (11)", okmax)
ikeda = {(1, .1): -0.0049, (1, .2): -0.0180, (1, .5): -0.0726, (1, 1): -0.1147, (1.5, 1): -0.1425}
for (hv, kv), E1 in ikeda.items():
    val = -float(EB11.subs({h: hv, k: kv}))
    chk(f"Ikeda Table II <E_1>({hv},{kv}) = {E1}: computed {val:.4f}", abs(val - E1) < 6e-5)
for hv, kv in [(1, .1), (1, 1), (1.5, 1), (3, .7), (0.2, 5)]:
    ebv = float(EB11.subs({h: hv, k: kv})); eav = float((h**2/r).subs({h: hv, k: kv}))
    chk(f"0 < E_B <= E_A at (h,k)=({hv},{kv}): E_B={ebv:.4f}, E_A={eav:.4f}, ratio {ebv/eav:.4f}", 0 < ebv <= eav)
# alpha-independent Bob unitary cannot extract (Hotta eq. 13)
worst = -1e9
hv, kv = 1.0, 0.5
Hn = H.subs({h: hv, k: kv}).evalf(); rn = rhoM.subs({h: hv, k: kv}).evalf()
EAn = float(EA.subs({h: hv, k: kv}))
for _ in range(20):
    M = sp.Matrix(2, 2, lambda i, j: complex(rng.gauss(0, 1), rng.gauss(0, 1)))
    Q, _ = M.QRdecomposition()
    W = kron(I2, Q)
    ext = EAn - float(sp.re((W*rn*dag(W)*Hn).trace()))
    worst = max(worst, ext)
chk(f"alpha-independent Bob unitaries extract <= 0 (best of 20: {worst:.2e})", worst <= 1e-12)

print("\nSUMMARY")
print("  Standard teleportation: state transferred; no energy crosses the channel;")
print("  the teleported state's energy is supplied/absorbed by Bob's local device.")
print("  QET (coupled, ground-state-entangled medium already spanning A..B): E_B > 0")
print("  extracted at B by LOCC, E_B <= E_A, energy drawn from B's local zero-point")
print("  fluctuation, classical bits at <= c.  Neither moves matter.")
print("\n" + ("ALL CHECKS PASS" if bad == 0 else f"{bad} CHECK(S) FAILED"))
sys.exit(1 if bad else 0)
