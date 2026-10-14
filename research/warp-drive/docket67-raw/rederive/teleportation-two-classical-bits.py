#!/usr/bin/env python3
"""
DOCKET 67 -- rederivation for key 'teleportation-two-classical-bits'
(transit.py:35-44, 129-140, 197-210, 329-335).

Checks, each printed with PASS/FAIL:
 S1  (sympy, exact) standard Bennett et al. protocol on a SYMBOLIC qubit a|0>+b|1>:
     every one of the 4 outcomes has p = 1/4 (given |a|^2+|b|^2 = 1), B's branch state is
     sigma_m psi, corrections restore psi exactly, and the outcome-average of B's state with
     corrections withheld is EXACTLY I/2 (entry-wise, symbolically) -- independent of a,b.
 S2  (sympy, exact) the same average for a NON-maximally entangled resource c0|00>+c1|11>:
     it is diag(c0^2, c1^2) -- NOT I/2 -- but still independent of a,b (zero information).
     So 'exactly I/2' needs the maximally-entangled hypothesis; 'zero information' does not.
 N1  (numeric) the LOWER BOUND the tree hard-codes: with a reference R maximally entangled
     with the input, I(R;B) = 0 before any message, exact teleportation needs I(R;B_out) = 2
     bits, and I(R;B M) <= I(R;B) + H(M) <= log2 k for a k-valued classical message M
     (classical M: H(M|RB) >= 0).  Hence k >= 4, i.e. >= 2 bits.  The standard protocol is
     shown to SATURATE it: I(R;BM) = 2.000, H(M) = 2.000.
 N2  (numeric) the inequality I(R;BM) <= log2 k checked on random protocols (random k-outcome
     POVMs on Alice's two qubits, k = 2,3,4) -- a sanity check of the chain, not a proof.
 N3  (numeric) remote state preparation (Pati 1999 / Bennett et al. 2001): for KNOWN
     equatorial states ONE bit suffices exactly; B's averaged state is still I/2.
     So '2 bits per qubit' is a bound for UNKNOWN (arbitrary) input, not for every transfer.
 N4  (numeric) transit.py's own quantities: the no-bits deviation from I/2 at double precision,
     and the fact that advantage_over_light(D) = D/c - D/c is identically zero by definition.
stdlib + sympy + numpy.
"""
import math, sys
import numpy as np
import sympy as sp

ok_all = True
def rec(label, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print(f"  {'PASS' if cond else 'FAIL'}  {label}  {detail}")

# ---------------------------------------------------------------- S1 exact, symbolic
print("S1  symbolic standard protocol (maximally entangled resource)")
ar, ai, br, bi = sp.symbols('a_r a_i b_r b_i', real=True)
a = ar + sp.I*ai; b = br + sp.I*bi
norm = {ar**2: 1 - ai**2 - br**2 - bi**2}
psi = sp.Matrix([a, b])
s2 = 1/sp.sqrt(2)
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
bell = [sp.Matrix([s2, 0, 0, s2]), sp.Matrix([0, s2, s2, 0]),
        sp.Matrix([s2, 0, 0, -s2]), sp.Matrix([0, s2, -s2, 0])]
corr = [I2, X, Z, Z*X]
res = sp.Matrix([s2, 0, 0, s2])                    # |Phi+> on (A', B)
state = sp.kronecker_product(psi, res)              # order: input, A', B
def project(bv, st):
    # <bv|_(input,A') (x) 1_B |st>
    return sp.Matrix([sum(sp.conjugate(bv[i*2+j])*st[i*4+j*2+c]
                          for i in range(2) for j in range(2)) for c in range(2)])
avg = sp.zeros(2, 2)
all_quarter = True; all_exact = True
for m in range(4):
    v = project(bell[m], state)
    p = sp.simplify(sp.expand((v.H*v)[0]).subs(norm))
    all_quarter &= sp.simplify(p - sp.Rational(1, 4)) == 0
    out = corr[m]*v*2                                # normalise (sqrt(p) = 1/2)
    all_exact &= sp.simplify(sp.expand(out - psi)) == sp.zeros(2, 1)
    avg += v*v.H                                     # p * |v_n><v_n| = |v><v|
avg = sp.simplify(sp.expand(avg).subs(norm))
rec("each outcome p = 1/4 for every input", all_quarter)
rec("corrections restore psi exactly on all 4 outcomes (fidelity 1)", all_exact)
rec("no-bits average rho_B == I/2 EXACTLY, independent of (a,b)",
    sp.simplify(avg - sp.eye(2)/2) == sp.zeros(2, 2), f"rho_B = {avg.tolist()}")

# ---------------------------------------------------------------- S2 non-maximal resource
print("\nS2  symbolic, non-maximally entangled resource c0|00> + c1|11>")
t = sp.symbols('theta', real=True)
c0, c1 = sp.cos(t), sp.sin(t)
res2 = sp.Matrix([c0, 0, 0, c1])
state2 = sp.kronecker_product(psi, res2)
avg2 = sp.zeros(2, 2)
for m in range(4):
    v = project(bell[m], state2)
    avg2 += v*v.H
avg2 = sp.simplify(sp.expand(avg2).subs(norm))
rec("no-bits average rho_B = diag(c0^2, c1^2) (psi-independent, NOT I/2 unless c0=c1)",
    sp.simplify(avg2 - sp.diag(c0**2, c1**2)) == sp.zeros(2, 2), f"rho_B = {avg2.tolist()}")
rec("  its (a,b)-dependence vanishes identically",
    all(sp.simplify(sp.diff(avg2[i, j], s)) == 0 for i in range(2) for j in range(2)
        for s in (ai, br, bi)))

# ---------------------------------------------------------------- numeric helpers
def ket(*bits):
    v = np.zeros(2**len(bits), complex); v[int("".join(map(str, bits)), 2)] = 1; return v
def ptrace(rho, keep, n):
    """rho on n qubits; keep = sorted list of qubit indices to keep."""
    rho = rho.reshape([2]*2*n)
    tr = [q for q in range(n) if q not in keep]
    # trace out from highest index down
    for q in sorted(tr, reverse=True):
        nn = rho.ndim//2
        rho = np.trace(rho, axis1=q, axis2=q+nn)
    d = 2**len(keep)
    return rho.reshape(d, d)
def S(rho):
    w = np.linalg.eigvalsh((rho+rho.conj().T)/2); w = w[w > 1e-13]
    return float(-(w*np.log2(w)).sum())
def blockdiag_cq(pm, rhos):
    """classical-quantum state sum_m p_m |m><m| (x) rho_m."""
    k = len(pm); d = rhos[0].shape[0]
    out = np.zeros((k*d, k*d), complex)
    for m in range(k): out[m*d:(m+1)*d, m*d:(m+1)*d] = pm[m]*rhos[m]
    return out

# ---------------------------------------------------------------- N1 the lower bound, saturated
print("\nN1  information-theoretic lower bound (reference-system argument), standard protocol")
# qubits: R(0), input(1), A'(2), B(3).  R-input maximally entangled; A'-B Bell pair.
phi = (ket(0, 0)+ket(1, 1))/math.sqrt(2)
full = np.kron(phi, phi)                                   # R,in,A',B
rho = np.outer(full, full.conj())
rho_RB = ptrace(rho, [0, 3], 4)
I_RB_before = S(ptrace(rho_RB, [0], 2)) + S(ptrace(rho_RB, [1], 2)) - S(rho_RB)
rec("I(R;B) before any message = 0", abs(I_RB_before) < 1e-12, f"{I_RB_before:.3e}")
Bn = [np.array([1, 0, 0, 1])/math.sqrt(2), np.array([0, 1, 1, 0])/math.sqrt(2),
      np.array([1, 0, 0, -1])/math.sqrt(2), np.array([0, 1, -1, 0])/math.sqrt(2)]
Xn = np.array([[0, 1], [1, 0]]); Zn = np.diag([1, -1]); Cn = [np.eye(2), Xn, Zn, Zn@Xn]
pm, rRB = [], []
for m in range(4):
    P = np.kron(np.kron(np.eye(2), np.outer(Bn[m], Bn[m].conj())), np.eye(2))
    v = P@full; p = np.vdot(v, v).real; v = v/math.sqrt(p)
    r = ptrace(np.outer(v, v.conj()), [0, 3], 4)
    pm.append(p); rRB.append(r)
cq = blockdiag_cq(pm, rRB)                                  # M (x) R (x) B
HM = float(-sum(p*math.log2(p) for p in pm))
rho_MB = sum(np.kron(np.eye(4)[m:m+1].T@np.eye(4)[m:m+1], pm[m]*ptrace(rRB[m], [1], 2)) for m in range(4))
S_RMB = S(cq); S_MB = S(rho_MB); S_R = S(ptrace(rRB[0], [0], 2)*0 + sum(pm[m]*ptrace(rRB[m], [0], 2) for m in range(4)))
I_R_BM = S_R + S_MB - S_RMB
rec("H(M) = 2 bits (four equiprobable outcomes)", abs(HM-2) < 1e-12, f"{HM:.12f}")
rec("I(R;B M) = 2 bits = log2 k -> the bound k >= 4 is SATURATED", abs(I_R_BM-2) < 1e-9, f"{I_R_BM:.12f}")
# after correction: R-B maximally entangled on every branch
Imax = []
for m in range(4):
    U = np.kron(np.eye(2), Cn[m]); r = U@rRB[m]@U.conj().T
    Imax.append(2*S(ptrace(r, [0], 2)) - S(r))
rec("after correction I(R;B_out) = 2 on every branch (exact teleportation)",
    max(abs(x-2) for x in Imax) < 1e-9, f"{Imax}")
print("      => any exact scheme needs log2 k >= I(R;B_out) - I(R;B) = 2 - 0: k >= 4, >= 2 bits."
      "\n         Chain: I(R;B_out) <= I(R;BM) (data processing, Bob local) = I(R;B)+I(R;M|B)"
      "\n         <= 0 + H(M|B) <= log2 k  (M classical => H(M|RB) >= 0).")

# ---------------------------------------------------------------- N2 random protocols
print("\nN2  I(R;BM) <= log2 k on random k-outcome protocols (sanity check, not a proof)")
rng = np.random.default_rng(67)
def rand_povm(k, d):
    G = [rng.normal(size=(d, d))+1j*rng.normal(size=(d, d)) for _ in range(k)]
    Sm = sum(g.conj().T@g for g in G)
    w, V = np.linalg.eigh(Sm); Sinv = V@np.diag(w**-0.5)@V.conj().T
    return [g@Sinv for g in G]          # Kraus K_m with sum K^dag K = 1
def I_R_BM(Ks):
    k = len(Ks); pm, rRB = [], []
    for K in Ks:
        Kf = np.kron(np.kron(np.eye(2), K), np.eye(2))
        r4 = Kf@rho@Kf.conj().T; p = np.trace(r4).real
        pm.append(p); rRB.append(ptrace(r4/p, [0, 3], 4))
    cq = blockdiag_cq(pm, rRB)
    rMB = np.zeros((2*k, 2*k), complex)
    for m in range(k): rMB[2*m:2*m+2, 2*m:2*m+2] = pm[m]*ptrace(rRB[m], [1], 2)
    rR = sum(pm[m]*ptrace(rRB[m], [0], 2) for m in range(k))
    return S(rR) + S(rMB) - S(cq)
PB = [np.outer(v, v.conj()) for v in Bn]
for lab, Ks, k in (("Bell measurement, k=4", PB, 4),
                   ("coarse-grained Bell, k=3 {P0,P1,P2+P3}", [PB[0], PB[1], PB[2]+PB[3]], 3),
                   ("coarse-grained Bell, k=2 {P0+P1,P2+P3}", [PB[0]+PB[1], PB[2]+PB[3]], 2)):
    I = I_R_BM(Ks)
    rec(f"extremal {lab}: I(R;BM) = {I:.6f} <= log2 k = {math.log2(k):.6f}", I <= math.log2(k)+1e-9)
worst = {}
for k in (2, 3, 4):
    worst[k] = -math.inf
    for trial in range(200):
        Ks = rand_povm(k, 4)
        pm, rRB = [], []
        for K in Ks:
            Kf = np.kron(np.kron(np.eye(2), K), np.eye(2))
            r4 = Kf@rho@Kf.conj().T; p = np.trace(r4).real
            pm.append(p); rRB.append(ptrace(r4/p, [0, 3], 4))
        cq = blockdiag_cq(pm, rRB)
        rMB = np.zeros((2*k, 2*k), complex)
        for m in range(k): rMB[2*m:2*m+2, 2*m:2*m+2] = pm[m]*ptrace(rRB[m], [1], 2)
        rR = sum(pm[m]*ptrace(rRB[m], [0], 2) for m in range(k))
        I = S(rR) + S(rMB) - S(cq)
        worst[k] = max(worst[k], I - math.log2(k))
    rec(f"k = {k}: max over 200 random protocols of I(R;BM) - log2 k <= 0", worst[k] <= 1e-9,
        f"{worst[k]:+.4f}")
print("      (k = 2, 3 cannot reach I = 2, so no exact teleportation with < 4 messages.)")

# ---------------------------------------------------------------- N3 RSP, known equatorial states
print("\nN3  remote state preparation of KNOWN equatorial states with ONE bit (Pati 1999)")
worstF = 1.0; worstDev = 0.0
bell_pair = (ket(0, 0)+ket(1, 1))/math.sqrt(2)
for trial in range(50):
    ph = rng.uniform(0, 2*math.pi)
    target = np.array([1, np.exp(1j*ph)])/math.sqrt(2)
    perp = np.array([1, -np.exp(1j*ph)])/math.sqrt(2)
    avgB = np.zeros((2, 2), complex)
    for m, e in enumerate((target.conj(), perp.conj())):   # Alice measures in conj basis
        P = np.kron(np.outer(e, e.conj()), np.eye(2))
        v = P@bell_pair; p = np.vdot(v, v).real; v = v/math.sqrt(p)
        rB = ptrace(np.outer(v, v.conj()), [1], 2)
        avgB += p*rB
        corrB = rB if m == 0 else Zn@rB@Zn               # ONE bit: apply Z or not
        worstF = min(worstF, np.vdot(target, corrB@target).real)
    worstDev = max(worstDev, np.abs(avgB-np.eye(2)/2).max())
rec("one classical bit prepares every known equatorial state with fidelity 1", worstF > 1-1e-12,
    f"min F = {worstF:.15f}")
rec("  and without the bit B is still I/2 (no-signalling holds for RSP too)", worstDev < 1e-14,
    f"dev {worstDev:.1e}")

# ---------------------------------------------------------------- N4 transit.py's own numbers
print("\nN4  transit.py's quantities")
dev = 0.0
for trial in range(1000):
    th, ph = rng.uniform(0, math.pi), rng.uniform(0, 2*math.pi)
    ps = np.array([math.cos(th/2), np.exp(1j*ph)*math.sin(th/2)])
    st = np.kron(ps, bell_pair)
    avgB = np.zeros((2, 2), complex)
    for m in range(4):
        v = np.array([sum(np.conj(Bn[m][i*2+j])*st[i*4+j*2+c] for i in range(2) for j in range(2))
                      for c in range(2)])
        avgB += np.outer(v, v.conj())
    dev = max(dev, np.abs(avgB-np.eye(2)/2).max())
rec("no-bits deviation from I/2 is double-precision rounding only (exact value 0 by S1)",
    dev < 1e-14, f"max over 1000 inputs = {dev:.2e}")
D, c = sp.symbols('D c', positive=True)
rec("advantage_over_light(D) = arrival_time(D) - D/c is 0 BY DEFINITION (arrival_time := D/c)",
    sp.simplify(D/c - D/c) == 0,
    "-> the ledger's '0.000' restates the <= c hypothesis; it is not a measurement")

print("\n" + ("ALL CHECKS PASS" if ok_all else "SOME CHECK FAILED"))
sys.exit(0 if ok_all else 1)
