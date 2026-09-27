#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation of the no-communication (no-signalling) theorem as the
warp board uses it (transit.py:15-18,106-110,149,176-180,312-318; ledger.py D13/D23).

Reads research/warp-drive/transit.py READ-ONLY (bytecode writing disabled); writes nothing.

  C1  sympy, exact: for GENERIC symbolic rho on C^dA (x) C^dB and GENERIC symbolic Kraus
      operators K_1..K_n on A,  Tr_A[sum_i (K_i(x)I) rho (K_i(x)I)^dag]
                              - Tr_A[((sum_i K_i^dag K_i)(x)I) rho]  == 0 identically.
      Hence rho_B is invariant under EVERY trace-preserving (sum K^dag K = I) local
      operation on A -- the Peres-Terno eq.(10)->(11) / GRW eq.(12) step.  dA in {2,3}, dB=2.
  C2  sympy, exact: transit.py's Euler-angle U(a,b,c,g) is unitary for all angles and leaves
      the Bell pair's rho_B = I/2 for all angles (not just the 6/40 sampled draws).
  C3  numeric: random CPTP maps WITH ancillas (Stinespring isometries), dA=2..4, and
      non-selective projective measurements -- the classes transit.py's docstring claims
      ('EVERY operation') but its instrument never samples.
  C4  numeric: the hypotheses bite (none of these refutes the theorem; each leaves its class):
      (a) SELECTIVE (post-selected) measurement on A: conditional rho_B moves (to |0><0|);
      (b) Sorkin 1993 (gr-qc/9302018 p.6): a NON-LOCAL ideal measurement B=|Phi+><Phi+|
          makes a kick on subsystem 1 visible at 2: |d><d| vs I/2, and measuring sigma_1
          gives (1/4)|u><u|+(3/4)|d><d| -- re-derived;
      (c) Peres-Terno 2003 (quant-ph/0212023 p.9, eq.16): incomplete Bell measurement
          lets |00> vs |01> be distinguished with probability 0.75 -- re-derived;
      (d) NONLINEAR map at B (Gisin 1989 / Simon-Buzek-Gisin): Alice's basis choice
          (Z vs X) changes Bob's post-map state.
  C5  transit.py's own instrument re-run: worst deviation over its 6 report draws (seed 7)
      and its 40 selftest draws (seed 101); index3.py:1362 says '1.110e-16 under FORTY'.
  C6  D23 arithmetic: advantage_over_light(D) = D/c - D/c == 0 symbolically; Earth-Proxima
      4.0175e16 m in light years vs PROXIMA_LY = 4.2465.
"""
import sys, os, math, cmath, random, itertools
sys.dont_write_bytecode = True
import sympy as sp
import numpy as np

TREE = "/home/user/Claude-Method-Works/research/warp-drive"
results = {}
def rec(k, ok, detail):
    results[k] = (bool(ok), detail)
    print(f"  {'PASS' if ok else 'FAIL'}  {k}: {detail}")

def ptrace_A(M, dA, dB):
    R = sp.zeros(dB, dB)
    for i in range(dB):
        for j in range(dB):
            R[i, j] = sum(M[a*dB+i, a*dB+j] for a in range(dA))
    return R

# ---------------------------------------------------------------- C1
print("C1  exact identity Tr_A[(K(x)I) rho (K(x)I)^+] = Tr_A[(K^+K (x) I) rho]")
for dA, nK in ((2, 2), (3, 2)):
    dB = 2; N = dA*dB
    rho = sp.Matrix(N, N, lambda i, j: sp.Symbol(f"r{i}_{j}"))       # fully generic (not even Hermitian)
    Ks = [sp.Matrix(dA, dA, lambda i, j, k=k: sp.Symbol(f"k{k}_{i}{j}") + sp.I*sp.Symbol(f"q{k}_{i}{j}"))
          for k in range(nK)]
    IB = sp.eye(dB)
    lhs = sp.zeros(dB, dB); S = sp.zeros(dA, dA)
    for K in Ks:
        KI = sp.kronecker_product(K, IB)
        lhs += ptrace_A(KI*rho*KI.H, dA, dB)
        S += K.H*K
    rhs = ptrace_A(sp.kronecker_product(S, IB)*rho, dA, dB)
    diff = (lhs - rhs).applyfunc(sp.expand)
    rec(f"C1 dA={dA} nKraus={nK}", diff == sp.zeros(dB, dB),
        "difference expands to the zero matrix; with sum K^+K = I the rhs is Tr_A rho, so rho_B is unchanged")

# ---------------------------------------------------------------- C2
print("C2  transit.py's Euler U(a,b,c,g), symbolic")
a, b, c, g = sp.symbols("a b c g", real=True)
E = sp.exp
U = sp.Matrix([[E(sp.I*g)*E(sp.I*(b+c)/2)*sp.cos(a/2), -E(sp.I*g)*E(sp.I*(b-c)/2)*sp.sin(a/2)],
               [E(sp.I*g)*E(-sp.I*(b-c)/2)*sp.sin(a/2), E(sp.I*g)*E(-sp.I*(b+c)/2)*sp.cos(a/2)]])
UU = (U.H*U).applyfunc(lambda x: sp.simplify(sp.expand(x)))
rec("C2 unitarity", UU == sp.eye(2), "U^+U = I for all real a,b,c,g")
bell = sp.Matrix([1, 0, 0, 1])/sp.sqrt(2)
v = sp.kronecker_product(U, sp.eye(2))*bell
rB = ptrace_A(v*v.H, 2, 2).applyfunc(lambda x: sp.simplify(sp.expand(x)))
rec("C2 Bell rho_B", rB == sp.eye(2)/2, "rho_B = I/2 exactly for every angle (the sampled draws are instances)")

# ---------------------------------------------------------------- C3
print("C3  numeric: random CPTP maps with ancillas; non-selective measurements")
rng = np.random.default_rng(67)
def rand_state(d):
    X = rng.normal(size=(d, d)) + 1j*rng.normal(size=(d, d)); R = X@X.conj().T; return R/np.trace(R)
def rand_isometry(din, dout):
    X = rng.normal(size=(dout, din)) + 1j*rng.normal(size=(dout, din)); Q, _ = np.linalg.qr(X); return Q[:, :din]
def ptA(M, dA, dB): return np.einsum("aiaj->ij", M.reshape(dA, dB, dA, dB))
worst = 0.0; trials = 0
for dA in (2, 3, 4):
    dB = 2
    for _ in range(200):
        rho = rand_state(dA*dB); r0 = ptA(rho, dA, dB)
        nK = int(rng.integers(1, 5)); V = rand_isometry(dA, dA*nK)            # Stinespring: Kraus K_k = V[k-block]
        Ks = [V[k*dA:(k+1)*dA, :] for k in range(nK)]
        assert np.allclose(sum(K.conj().T@K for K in Ks), np.eye(dA))
        out = sum(np.kron(K, np.eye(dB))@rho@np.kron(K, np.eye(dB)).conj().T for K in Ks)
        worst = max(worst, np.abs(ptA(out, dA, dB) - r0).max()); trials += 1
        # non-selective projective measurement in a random basis
        Q = rand_isometry(dA, dA); Ps = [np.outer(Q[:, k], Q[:, k].conj()) for k in range(dA)]
        out2 = sum(np.kron(P, np.eye(dB))@rho@np.kron(P, np.eye(dB)) for P in Ps)
        worst = max(worst, np.abs(ptA(out2, dA, dB) - r0).max()); trials += 1
rec("C3 CPTP+ancilla+nonselective", worst < 1e-13, f"worst |rho_B' - rho_B| = {worst:.2e} over {trials} random operations, dA=2..4, generic mixed rho")

# ---------------------------------------------------------------- C4
print("C4  where the hypotheses bite")
k0 = np.array([1, 0], complex); k1 = np.array([0, 1], complex)
PHI = (np.kron(k0, k0) + np.kron(k1, k1))/np.sqrt(2)
rhoBell = np.outer(PHI, PHI.conj())
P0 = np.kron(np.outer(k0, k0), np.eye(2))
sel = P0@rhoBell@P0; sel = sel/np.trace(sel)
rBsel = ptA(sel, 2, 2)
rec("C4a selective measurement", np.allclose(rBsel, np.outer(k0, k0)),
    f"post-selected on A's outcome 0, rho_B = diag{tuple(np.round(np.diag(rBsel).real, 12))} != I/2: outside the non-selective class; usable only once the outcome is sent at <= c (GRW 2013 p.14)")
# Sorkin: basis u=|0>, d=|1>; initial |dd>
u, d = k0, k1
psi = np.kron(d, d); rho = np.outer(psi, psi.conj())
PhiUD = (np.kron(u, u) + np.kron(d, d))/np.sqrt(2); B = np.outer(PhiUD, PhiUD.conj()); IB = np.eye(4) - B
def after_B(r): return B@r@B + IB@r@IB
sx = np.array([[0, 1], [1, 0]], complex); KX = np.kron(sx, np.eye(2))
r_kick = ptA(after_B(KX@rho@KX), 2, 2); r_none = ptA(after_B(rho), 2, 2)
r_meas = ptA(after_B(0.5*(rho + KX@rho@KX)), 2, 2)
ok = (np.allclose(r_kick, np.outer(d, d)) and np.allclose(r_none, np.eye(2)/2)
      and np.allclose(r_meas, 0.25*np.outer(u, u) + 0.75*np.outer(d, d)))
rec("C4b Sorkin 1993 coupled-spin example", ok,
    f"kick -> diag{tuple(np.round(np.diag(r_kick).real,6))}, none -> diag{tuple(np.round(np.diag(r_none).real,6))}, sigma_1 measured -> diag{tuple(np.round(np.diag(r_meas).real,6))}: matches gr-qc/9302018 p.6 (non-local ideal measurement, not a local operation)")
# Peres-Terno eq.16: Bob (2nd) prepares |00> or |01>; incomplete Bell PVM E1=|Phi+><Phi+|; Alice's rho_A
def rhoA_after(psi):
    r = np.outer(psi, psi.conj()); r2 = B@r@B + IB@r@IB
    return np.einsum("iaja->ij", r2.reshape(2, 2, 2, 2))
rA01 = rhoA_after(np.kron(k0, k1)); rA00 = rhoA_after(np.kron(k0, k0))
pguess = 0.5 + 0.25*np.abs(np.linalg.eigvalsh(rA01 - rA00)).sum()
rec("C4c Peres-Terno eq.16 incomplete Bell measurement", abs(pguess - 0.75) < 1e-12,
    f"rho_A = diag{tuple(np.round(np.diag(rA01).real,6))} vs diag{tuple(np.round(np.diag(rA00).real,6))}; Helstrom success {pguess:.6f} = 0.75 as quant-ph/0212023 p.9 states (a joint, non-localizable operation)")
# Gisin-type nonlinear map at B
def nonlin(v, eps=0.3):                       # a norm-restoring state-dependent (nonlinear) map on pure states
    w = v + eps*abs(v[0])**2*k0; return w/np.linalg.norm(w)
def bob_after(basis):
    out = np.zeros((2, 2), complex)
    for e in basis:
        amp = np.kron(e.conj(), np.eye(2))@PHI      # Bob's unnormalised conditional state
        p = np.vdot(amp, amp).real
        if p < 1e-15: continue
        w = nonlin(amp/np.sqrt(p)); out += p*np.outer(w, w.conj())
    return out
Zb = [k0, k1]; Xb = [(k0+k1)/np.sqrt(2), (k0-k1)/np.sqrt(2)]
dZX = np.abs(bob_after(Zb) - bob_after(Xb)).max()
linZ = sum(0.5*np.outer(e, e.conj()) for e in Zb); linX = sum(0.5*np.outer(e.conj(), e) for e in Xb)
rec("C4d nonlinear map signals (linearity is load-bearing)", dZX > 1e-3 and np.allclose(linZ, linX),
    f"with a nonlinear map at B, Alice's basis choice moves Bob's state by {dZX:.4f}; with the linear identity map both ensembles give I/2")

# ---------------------------------------------------------------- C5
print("C5  transit.py's own instrument, re-run read-only")
sys.path.insert(0, TREE)
import transit
r7 = random.Random(7); w6 = max(transit.signalling_deviation(transit.random_unitary(r7)) for _ in range(6))
r101 = random.Random(101); w40 = max(transit.signalling_deviation(transit.random_unitary(r101)) for _ in range(40))
rec("C5 report (6 draws, seed 7)", w6 < 1e-14, f"worst = {w6:.3e} (report prints 1.1e-16)")
rec("C5 selftest (40 draws, seed 101)", w40 < 1e-14, f"worst = {w40:.3e}; index3.py:1362 quotes '1.110e-16' under FORTY -- selftest prints only the boolean")
rec("C5 READING_CARRIES_NOTHING_ALONE is a constant", transit.READING_CARRIES_NOTHING_ALONE is True,
    "hard-coded at transit.py:149; selftest :318 checks the constant against True (not a derivation) -- C1 supplies the derivation")

# ---------------------------------------------------------------- C6
print("C6  D23 arithmetic")
D, cc = sp.symbols("D c", positive=True)
rec("C6 advantage identically 0", sp.simplify(D/cc - D/cc) == 0,
    "advantage_over_light(D) = D/c - D/c = 0 for every D: ZERO BY CONSTRUCTION, as D23 itself says; no distance datum can move it")
yr = 365.25*86400
ly = transit.DISTANCES[2][1]/transit.C_SI/yr
rec("C6 Earth-Proxima in ly", abs(ly - 4.2465) < 5e-4, f"4.0175e16 m / c = {ly:.5f} Julian yr; PROXIMA_LY = 4.2465 (Gaia DR3 1/plx = 4.24646 ly per audits/gaia-dr3-proxima-distance.json)")

nf = sum(1 for ok, _ in results.values() if not ok)
print(f"\n{len(results)-nf}/{len(results)} checks pass")
sys.exit(1 if nf else 0)
