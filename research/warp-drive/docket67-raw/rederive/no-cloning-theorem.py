#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the no-cloning theorem (Wootters-Zurek / Dieks 1982)
and of transit.py's use of it (A ends maximally mixed, 'a move, not a copy').

Exact (sympy) where closed-form; numeric (numpy) where a random sample suffices.
Exits 1 if any check fails.  Writes nothing.
"""
import sys, sympy as sp, numpy as np

FAIL = []
def chk(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"  -- {detail}" if detail else ""))
    if not ok: FAIL.append(label)

print("C1  inner-product argument (WZ/Dieks via unitarity): <a|b> = <a|b>^2 => s in {0,1}")
s = sp.symbols('s')           # s = <a|b>, complex in general; s(s-1)=0 is polynomial
sol = sp.solve(sp.Eq(s, s**2), s)
chk("solutions of s = s^2", set(sol) == {0, 1}, f"{sol}")

print("C2  linearity argument (the WZ proof as restated by Scarani et al. 2005 eq. 2 ff.)")
k0, k1 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
kp = (k0 + k1) / sp.sqrt(2)
kr = lambda a, b: sp.Matrix(sp.kronecker_product(a, b))
lin_image = (kr(k0, k0) + kr(k1, k1)) / sp.sqrt(2)     # what linearity forces for |+>
want = kr(kp, kp)
ov = sp.simplify((want.H * lin_image)[0])
chk("linear extension of a {0,1}-cloner on |+> is NOT |++>", ov != 1, f"<++|lin> = {ov}, fidelity {sp.nsimplify(ov**2)}")

print("C3  no LINEAR map at all (unitary or not) sends psi -> psi(x)psi on {|0>,|1>,|+>}")
M = sp.Matrix(4, 2, sp.symbols('m0:8'))
eqs = []
for v in (k0, k1, kp):
    eqs += list(M * v - kr(v, v))
res = sp.linsolve(eqs, list(M))
chk("linear system inconsistent (EmptySet)", res == sp.EmptySet, f"{res}")
# and for an orthogonal pair alone it IS consistent (CNOT-type copier exists)
eqs2 = []
for v in (k0, k1):
    eqs2 += list(M * v - kr(v, v))
res2 = sp.linsolve(eqs2, list(M))
chk("orthogonal pair {|0>,|1>} alone: consistent (cloneable)", res2 != sp.EmptySet)
CNOT = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
chk("CNOT clones |0>,|1> into blank |0>", all(CNOT*kr(v, k0) == kr(v, v) for v in (k0, k1)))
# any non-orthogonal, non-identical pair: <a|b>=c with 0<|c|<1 violates C1
chk("|0>,|+> overlap 1/sqrt2 not in {0,1} -> not jointly cloneable", sp.simplify((k0.H*kp)[0]) not in (0, 1))

print("C4  transit.py's claim, computed FROM THE PROTOCOL (transit.py hard-codes I/2 at :230/:342)")
al, be = sp.symbols('alpha beta', complex=True)
psi = sp.Matrix([al, be])
bell = (kr(k0, k0) + kr(k1, k1)) / sp.sqrt(2)
state = kr(psi, bell)                           # qubits: C (input), A, B
r2 = 1/sp.sqrt(2)
BB = [sp.Matrix([r2,0,0,r2]), sp.Matrix([0,r2,r2,0]), sp.Matrix([r2,0,0,-r2]), sp.Matrix([0,r2,-r2,0])]
X = sp.Matrix([[0,1],[1,0]]); Z = sp.Matrix([[1,0],[0,-1]]); I2 = sp.eye(2)
CORR = [I2, X, Z, Z*X]
norm = {al*sp.conjugate(al) + be*sp.conjugate(be): 1}
def ptrace(rho4, keep):     # two-qubit density matrix, keep 0 or 1
    r = sp.zeros(2, 2)
    for i in range(2):
        for j in range(2):
            r[i, j] = sum(rho4[2*i+k, 2*j+k] for k in range(2)) if keep == 0 else \
                      sum(rho4[2*k+i, 2*k+j] for k in range(2))
    return r
avg_alice = sp.zeros(4, 4)
for m, bv in enumerate(BB):
    P = kr(bv * bv.H, I2)                       # project C,A onto Bell state m
    post = P * state
    p = sp.simplify((post.H * post)[0].subs(norm))
    # Alice's pair after the projection is exactly bv, whatever psi was:
    # post = bv (x) (bob vector); extract bob vector and check factorisation
    bobv = sp.Matrix([sum(bv[a] * state[2*a + c] for a in range(4)) for c in range(2)])  # bv real
    rebuilt = kr(bv, bobv)
    chk(f"outcome {m}: post-measurement state = |Bell_{m}>_CA (x) |b>_B (factorises)",
        sp.simplify(post - rebuilt) == sp.zeros(8, 1))
    pn = sp.simplify(sp.expand(p).subs(be*sp.conjugate(be), 1 - al*sp.conjugate(al)))
    chk(f"outcome {m}: p = 1/4 independent of psi (on |a|^2+|b|^2=1)", pn == sp.Rational(1, 4), f"p={p} -> {pn}")
    rhoCA = bv * bv.H                           # contains no alpha, beta
    chk(f"outcome {m}: Alice's pair state free of alpha,beta", not (rhoCA.free_symbols & {al, be}))
    for keep, nm in ((0, 'C'), (1, 'A')):
        chk(f"outcome {m}: reduced state of qubit {nm} = I/2", ptrace(rhoCA, keep) == I2/2)
    out = (CORR[m] * bobv) / sp.sqrt(p)
    fid = sp.simplify((psi.H * out)[0] * sp.conjugate((psi.H * out)[0]))
    fid = sp.simplify(sp.expand(fid).subs(norm))
    # fidelity = |<psi|out>|^2 = (|a|^2+|b|^2)^2 -> 1 on the normalised sphere
    chk(f"outcome {m}: B's corrected state = psi (fidelity 1 on |a|^2+|b|^2=1)",
        sp.simplify(fid.subs(norm) - 1) == 0 or sp.simplify(fid - (al*sp.conjugate(al)+be*sp.conjugate(be))**2) == 0,
        f"{fid}")
    avg_alice += rhoCA / 4
chk("averaged over outcomes Alice's pair = I/4 (2 bits, psi-free)", avg_alice == sp.eye(4)/4)
lam = sp.Rational(1, 2)
S = sp.simplify(-2 * lam * sp.log(lam, 2))
chk("S(I/2) = 1 bit exactly (transit.py prints 1.000000000)", S == 1, f"S={S}")
chk("but the pair C,A is PURE given the outcome: S(pair) = 0", (BB[0]*BB[0].H).rank() == 1)

print("C5  later literature: approximate cloning (Buzek-Hillery 1996) F = 5/6, numerically")
rng = np.random.default_rng(67)
def ket(*bits):
    v = np.zeros(8, complex); v[int(''.join(map(str, bits)), 2)] = 1; return v
a23, a16 = np.sqrt(2/3), np.sqrt(1/6)
U0 = a23*ket(0,0,0) + a16*(ket(0,1,1) + ket(1,0,1))      # |0>|0>_B|0>_M -> ...
U1 = a23*ket(1,1,1) + a16*(ket(0,1,0) + ket(1,0,0))      # |1>|0>_B|0>_M -> ...
chk("BH images orthonormal (extendable to a unitary)",
    abs(np.vdot(U0, U1)) < 1e-15 and abs(np.vdot(U0, U0) - 1) < 1e-15 and abs(np.vdot(U1, U1) - 1) < 1e-15)
fs = []
for _ in range(200):
    v = rng.normal(size=2) + 1j*rng.normal(size=2); v /= np.linalg.norm(v)
    out = v[0]*U0 + v[1]*U1
    T = out.reshape(2, 2, 2)
    rA = np.einsum('ijk,ljk->il', T, T.conj()); rB = np.einsum('jik,jlk->il', T, T.conj())
    fs += [np.real(v.conj() @ rA @ v), np.real(v.conj() @ rB @ v)]
chk("BH fidelity = 5/6 for every sampled input, both copies", max(abs(f - 5/6) for f in fs) < 1e-12,
    f"min {min(fs):.15f} max {max(fs):.15f}")

print("C6  why it matters to the warp board: Herbert's FLASH needs a perfect cloner")
p0, p1 = np.array([1, 0]), np.array([0, 1]); pp, pm = (p0+p1)/np.sqrt(2), (p0-p1)/np.sqrt(2)
proj = lambda v: np.outer(v, v.conj())
rx = 0.5*proj(np.kron(pp, pp)) + 0.5*proj(np.kron(pm, pm))
rz = 0.5*proj(np.kron(p0, p0)) + 0.5*proj(np.kron(p1, p1))
e01 = np.kron(p0, p1)
chk("with a perfect cloner Bob's two-copy states differ: <01|rho_x|01>=1/4, <01|rho_z|01>=0",
    abs(np.real(e01 @ rx @ e01) - 0.25) < 1e-15 and abs(np.real(e01 @ rz @ e01)) < 1e-15)
chk("without cloning Bob's single qubit is I/2 either way (no signal)",
    np.allclose(0.5*proj(pp)+0.5*proj(pm), 0.5*proj(p0)+0.5*proj(p1)))

print()
print("RESULT:", "ALL PASS" if not FAIL else f"{len(FAIL)} FAIL: {FAIL}")
sys.exit(1 if FAIL else 0)
