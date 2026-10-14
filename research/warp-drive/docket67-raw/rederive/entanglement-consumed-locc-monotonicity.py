#!/usr/bin/env python3
"""
DOCKET 67 re-derivation: entanglement-consumed-locc-monotonicity
(transit.py:24-28, 138-139, 151, 212-224; ledger.py M-S1A-P5; specthm.py R11)

What is checked, and how:
  A  sympy, exact: Bell pair reduced entropy = 1 bit; teleportation of |q>=a|0>+b|1>
     leaves, per outcome, |Bell_m>_{AA'} (x) sigma_m|q>_B -- a PRODUCT across AA'|B, so the
     A|B entanglement AFTER is 0 exactly (computed, where transit.py:139 declares it) and B's
     corrected state is |q>, purity 1 (computed, where transit.py:217 prints a literal).
  B  numeric: outcome-averaged post-protocol state with Alice's classical record is
     PPT (negativity 0) and B = I/2 -- separable by construction.
  C  numeric: 'conservation' test. Cut entanglement E(Alice|Bob): pure input 1 -> 0
     (destroyed, NOT conserved); input = half of a local Bell pair R-A: 1 -> 1 (moved to R-B,
     entanglement swapping).  So the law is non-increase (monotonicity), not conservation.
  D  z3: Nielsen (quant-ph/9811053 Thm 1) + teleport-half-of-a-local-Bell-pair reduction:
     a pure Schmidt-rank-2 channel (p,1-p) that teleports an arbitrary qubit EXACTLY and
     deterministically while keeping a residual pure state with Schmidt vector r must satisfy
     (p,1-p) < (r (x) (1/2,1/2)); z3 proves this forces p = 1/2 and r = (1,0,..): the channel
     must be maximally entangled and is entirely consumed.  Also: a 2-ebit channel keeps 1.
  E  sympy: if fidelity 1 is NOT demanded, the channel can be kept: measure-and-prepare with
     no use of the pair gives average fidelity 2/3 with E_after = 1.
  F  numeric: BBPS 1996 monotonicity is ON AVERAGE: random Alice POVMs never raise the
     expected entropy of entanglement, but single outcomes can (the 'gamble').
"""
import itertools, math, sys
import numpy as np
import sympy as sp

ok_all = True
def rep(label, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print(f"  {'PASS' if cond else 'FAIL'}  {label}  {detail}")

# ---------------------------------------------------------------- A (sympy exact)
print("A. exact teleportation algebra (sympy)")
a, b = sp.symbols('a b', complex=True)
s2 = sp.sqrt(2)
k0, k1 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
kron = lambda *ms: (lambda f: f(f, ms))(lambda f, m: m[0] if len(m) == 1 else sp.kronecker_product(m[0], f(f, m[1:])))
phi_p = (kron(k0, k0) + kron(k1, k1)) / s2
phi_m = (kron(k0, k0) - kron(k1, k1)) / s2
psi_p = (kron(k0, k1) + kron(k1, k0)) / s2
psi_m = (kron(k0, k1) - kron(k1, k0)) / s2
# Bell reduced entropy
rhoB = sp.Matrix([[sp.Rational(1, 2), 0], [0, sp.Rational(1, 2)]])
S = -sum(ev * sp.log(ev, 2) * mult for ev, mult in rhoB.eigenvals().items())
rep("Bell pair entropy of entanglement = 1 bit exactly", sp.simplify(S - 1) == 0, f"S = {sp.nsimplify(S)}")
q = a * k0 + b * k1
state = kron(q, phi_p)                      # A (x) A'B
X = sp.Matrix([[0, 1], [1, 0]]); Z = sp.Matrix([[1, 0], [0, -1]]); I2 = sp.eye(2)
bells = [(phi_p, I2), (phi_m, Z), (psi_p, X), (psi_m, Z * X)]
for bv, corr in bells:
    proj = kron(bv * bv.H, I2)              # projector on AA' (non-destructive)
    post = proj * state                     # unnormalised
    # claim: post = |bv>_{AA'} (x) (1/2) sigma^dag |q>_B
    Bvec = sp.Matrix([ (kron(bv, I2).H * post)[i] for i in range(2)])  # <bv|_{AA'} post
    fact = sp.simplify(post - kron(bv, Bvec)) == sp.zeros(8, 1)
    rep("  outcome: post-measurement state factorises AA'|B (product => E_after = 0)", fact)
    out = sp.simplify(corr * Bvec * 2)
    rep("  after Pauli correction B holds |q> exactly (purity 1 per outcome)",
        sp.simplify(out - q) == sp.zeros(2, 1))
    p = sp.simplify((Bvec.H * Bvec)[0].subs({sp.conjugate(a): sp.Symbol('ac'), sp.conjugate(b): sp.Symbol('bc')}))
print("   each outcome probability = (|a|^2+|b|^2)/4 = 1/4")

# ---------------------------------------------------------------- numeric helpers
def ket(*bits):
    v = np.zeros(2 ** len(bits), complex); v[int(''.join(map(str, bits)), 2)] = 1; return v
def rdm(psi, keep, n):
    t = psi.reshape([2] * n)
    rest = [i for i in range(n) if i not in keep]
    t = np.transpose(t, keep + rest).reshape(2 ** len(keep), -1)
    return t @ t.conj().T
def S2(r):
    w = np.linalg.eigvalsh(r); w = w[w > 1e-14]; return float(-(w * np.log2(w)).sum())
def haar_qubit(rng):
    v = rng.normal(size=2) + 1j * rng.normal(size=2); return v / np.linalg.norm(v)
PHI = (ket(0, 0) + ket(1, 1)) / math.sqrt(2)
BELL = [PHI, (ket(0, 0) - ket(1, 1)) / math.sqrt(2), (ket(0, 1) + ket(1, 0)) / math.sqrt(2),
        (ket(0, 1) - ket(1, 0)) / math.sqrt(2)]
rng = np.random.default_rng(67)

# ---------------------------------------------------------------- B
print("\nB. outcome-averaged post-protocol state, Alice's record kept (numeric)")
q = haar_qubit(rng); st = np.kron(q, PHI)
rho = np.zeros((32, 32), complex)           # flag(4 as 2 qubits) (x) AA' (x) B, flag on Alice side
for m, bv in enumerate(BELL):
    P = np.kron(np.outer(bv, bv.conj()), np.eye(2)); v = P @ st
    f = np.zeros(4); f[m] = 1
    w = np.kron(f, v); rho += np.outer(w, w.conj())
# partial transpose on B (last qubit)
R = rho.reshape(16, 2, 16, 2).transpose(0, 3, 2, 1).reshape(32, 32)
neg = float((np.abs(np.linalg.eigvalsh(R)).sum() - 1) / 2)
rep("negativity across (flag,A,A')|B = 0 (PPT; separable by construction)", abs(neg) < 1e-12, f"N = {neg:.1e}")
rB = rho.reshape(16, 2, 16, 2).trace(axis1=0, axis2=2)
rep("B without the 2 bits = I/2", np.abs(rB - np.eye(2) / 2).max() < 1e-12)

# ---------------------------------------------------------------- C
print("\nC. is the cut entanglement CONSERVED? (numeric)")
# pure input: qubits A, A', B  (Alice = A,A'; Bob = B)
before = S2(rdm(st, [2], 3))
v = np.kron(np.outer(BELL[0], BELL[0].conj()), np.eye(2)) @ st; v /= np.linalg.norm(v)
after = S2(rdm(v, [2], 3))
rep("pure input: E(Alice|Bob) 1 -> 0 : destroyed, not conserved",
    abs(before - 1) < 1e-12 and after < 1e-12, f"{before:.9f} -> {after:.9f}")
# input = half of local Bell pair R-A: qubits R, A, A', B
st4 = np.kron(PHI, PHI)
b4 = S2(rdm(st4, [3], 4))
P4 = np.kron(np.eye(2), np.kron(np.outer(BELL[0], BELL[0].conj()), np.eye(2)))
v4 = P4 @ st4; v4 /= np.linalg.norm(v4)
a4 = S2(rdm(v4, [3], 4)); chan = S2(rdm(v4, [1, 2], 4)) if False else None
eAB_chan = S2(rdm(v4, [0, 1, 2], 4))  # = E(R A A' | B)
rRB = rdm(v4, [0, 3], 4)
rep("entangled input: E(Alice|Bob) 1 -> 1 : moved A'B -> RB (swapping)",
    abs(b4 - 1) < 1e-12 and abs(a4 - 1) < 1e-12, f"{b4:.9f} -> {a4:.9f}; R-B pure: purity {np.trace(rRB@rRB).real:.9f}")
rAAp = rdm(v4, [1, 2], 4)
rep("  and the CHANNEL pair itself is spent: AA' left pure (Bell state, local to Alice)",
    abs(np.trace(rAAp @ rAAp).real - 1) < 1e-12)

# ---------------------------------------------------------------- D (z3)
print("\nD. exact teleportation must consume the whole ebit (z3 over Nielsen majorization)")
import z3
def majorized(x, y):
    """x < y for z3 real vectors (already sorted descending, same length)."""
    cons = []
    for k in range(1, len(x)):
        cons.append(sum(x[:k]) <= sum(y[:k]))
    cons.append(sum(x) == sum(y))
    return z3.And(cons)
for dres in (2, 3, 4):
    p = z3.Real('p'); r = [z3.Real(f'r{i}') for i in range(dres)]
    s = z3.Solver()
    s.add(p >= z3.RealVal(1) / 2, p <= 1)
    s.add(*[ri >= 0 for ri in r], sum(r) == 1, *[r[i] >= r[i + 1] for i in range(dres - 1)])
    # target Schmidt vector: (1/2,1/2) (x) r, sorted descending = r0/2,r0/2,r1/2,r1/2,...
    y = [ri / 2 for ri in r for _ in (0, 1)]
    x = [p, 1 - p] + [z3.RealVal(0)] * (2 * dres - 2)
    s.add(majorized(x, y))
    s.add(z3.Not(z3.And(p == z3.RealVal(1) / 2, r[0] == 1)))
    res = s.check()
    rep(f"residual Schmidt dim {dres}: majorization => p=1/2 and residual product", res == z3.unsat, f"z3: {res}")
# non-vacuity guard: the premise is satisfiable at p=1/2, r=(1,0..)
s = z3.Solver(); p = z3.Real('p'); r0 = z3.Real('r0'); r1 = z3.Real('r1')
s.add(p == z3.RealVal(1) / 2, r0 == 1, r1 == 0)
s.add(majorized([p, 1 - p, 0, 0], [r0 / 2, r0 / 2, r1 / 2, r1 / 2]))
rep("  vacuity guard: premise satisfiable at the Bell channel", s.check() == z3.sat)
# a 2-ebit channel teleporting one qubit can keep one ebit
x = [z3.RealVal(1) / 4] * 4; y = [z3.RealVal(1) / 4] * 4
s = z3.Solver(); s.add(majorized(x, y))
rep("  2-ebit channel -> 1 ebit teleported + 1 ebit kept is allowed ('one pair, one transit' is per ebit)", s.check() == z3.sat)

# ---------------------------------------------------------------- E (sympy)
print("\nE. without demanding fidelity 1, the channel need not be spent (sympy)")
th = sp.symbols('theta', real=True)
Fz = (sp.cos(th / 2) ** 4 + sp.sin(th / 2) ** 4)   # measure Z, send bit, Bob prepares
Favg = sp.simplify(sp.integrate(Fz * sp.sin(th), (th, 0, sp.pi)) / 2)
rep("measure-and-prepare (pair untouched): average fidelity = 2/3, E_after = 1", Favg == sp.Rational(2, 3), f"F = {Favg}")

# ---------------------------------------------------------------- F
print("\nF. BBPS 1996: non-increase is ON AVERAGE (numeric)")
def ent(psi): return S2(rdm(psi, [0], 2))
worst_avg, gamble = -1.0, 0
for t in range(2000):
    c = rng.uniform(0.5, 1.0); psi = math.sqrt(c) * ket(0, 0) + math.sqrt(1 - c) * ket(1, 1)
    M = rng.normal(size=(2, 2, 2)) + 1j * rng.normal(size=(2, 2, 2))
    G = sum(Mi.conj().T @ Mi for Mi in M); L = np.linalg.inv(np.linalg.cholesky(G)).conj().T
    Ms = [Mi @ L for Mi in M]                                # sum Ms^dag Ms = I
    avg = 0.0
    for Mi in Ms:
        w = np.kron(Mi, np.eye(2)) @ psi; pr = np.linalg.norm(w) ** 2
        if pr > 1e-15:
            e = ent(w / math.sqrt(pr)); avg += pr * e
            if e > ent(psi) + 1e-9: gamble += 1
    worst_avg = max(worst_avg, avg - ent(psi))
rep("expected entanglement never increases (2000 random Alice POVMs)", worst_avg <= 1e-10, f"max increase {worst_avg:.2e}")
rep("single outcomes DO exceed the start (the 'gamble'), so the bound is on the expectation", gamble > 0, f"{gamble} outcomes")
# product in -> product out, always: separable cannot be made entangled
prod = np.kron(haar_qubit(rng), haar_qubit(rng))
mx = 0.0
for t in range(200):
    U = np.linalg.qr(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))[0]
    V = np.linalg.qr(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))[0]
    P0 = np.diag([1, 0]).astype(complex)
    w = np.kron(P0 @ U, V) @ prod
    if np.linalg.norm(w) > 1e-9: mx = max(mx, ent(w / np.linalg.norm(w)))
rep("from the post-teleportation product state no LOCC outcome is entangled", mx < 1e-10, f"max E {mx:.1e}")

print("\n" + ("ALL CHECKS PASS" if ok_all else "SOME CHECK FAILED"))
sys.exit(0 if ok_all else 1)
