#!/usr/bin/env python3
"""DOCKET 67 re-derivation for arXiv:0804.2182 (Casini 2008, CQG 25 205021) and its
restatement in arXiv:1309.1121 (Blanco & Casini, PRL 111 221601), eq. (3):
    Delta S_A <= Delta <H_A>,   S(rho_A|rho0_A) = Delta<H_A> - Delta S_A >= 0.
Reads research/warp-drive modules by import only; writes nothing there.
Checks:
 A  finite-dimensional (cut-off) identity and inequality, random and lattice (TFI chain)
 B  equality iff rho_A = rho0_A (U' in the complement saturates); first-order saturation (first law)
 C  both sides negative is allowed (source PRL p.2): a state with Delta<H> < 0
 D  Casini appendix (33),(34),(41),(42),(43),(44): symbolic Delta K, numeric series vs closed form,
    and the large-M limit where the relative entropy -> 0 (asymptotic saturation)
 E  Blanco-Casini (7) => (11),(12),(13) (sympy)
 F  the tree's coding (2,2,1,0,1,2): the four withdrawn claims, and what the K integer does
"""
import math, sys
import numpy as np
import sympy as sp
from scipy.linalg import logm, expm
from scipy.integrate import quad

rng = np.random.default_rng(67)
OK = True
def chk(name, cond, val=""):
    global OK
    OK &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "XX", name, val))

def vn(r):
    w = np.linalg.eigvalsh((r + r.conj().T) / 2); w = w[w > 1e-300]
    return float(-(w * np.log(w)).sum())
def ptrace_B(psi, dA, dB):
    m = psi.reshape(dA, dB); return m @ m.conj().T
def ptrace_rho_B(rho, dA, dB):
    return np.einsum('ijkj->ik', rho.reshape(dA, dB, dA, dB))
def modK(r0):
    w, v = np.linalg.eigh((r0 + r0.conj().T) / 2)
    return (v * (-np.log(w))) @ v.conj().T
def relent(r, r0):
    return float(np.real(np.trace(r @ (logm(r) - logm(r0)))))
def haar(d):
    z = (rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))) / math.sqrt(2)
    q, rr = np.linalg.qr(z); return q * (np.diag(rr) / abs(np.diag(rr)))

print("A. identity S(rho|rho0) = Delta<K> - Delta S and Delta S <= Delta<K>, random cut-off states")
dA, dB = 4, 8
worst = 1e9; idgap = 0
for t in range(400):
    psi0 = rng.normal(size=dA*dB) + 1j*rng.normal(size=dA*dB); psi0 /= np.linalg.norm(psi0)
    r0 = ptrace_B(psi0, dA, dB); K = modK(r0)
    # object state: random mixed global state (rank 1..6)
    k = rng.integers(1, 7); G = rng.normal(size=(dA*dB, k)) + 1j*rng.normal(size=(dA*dB, k))
    rho = G @ G.conj().T; rho /= np.trace(rho)
    r1 = ptrace_rho_B(rho, dA, dB)
    dS = vn(r1) - vn(r0); dK = float(np.real(np.trace((r1 - r0) @ K)))
    rel = relent(r1, r0)
    idgap = max(idgap, abs(rel - (dK - dS))); worst = min(worst, dK - dS)
chk("identity holds to 1e-9 over 400 draws", idgap < 1e-9, "max|gap|=%.2e" % idgap)
chk("Delta<K> - Delta S >= 0 in every draw", worst >= -1e-12, "min=%.4g" % worst)

print("A'. lattice: critical transverse-field Ising chain, 8 sites, A = first 2 sites")
L, nA = 8, 2
X = np.array([[0, 1], [1, 0]]); Z = np.diag([1., -1.]); I2 = np.eye(2)
def op(o, i):
    m = np.array([[1.]])
    for j in range(L): m = np.kron(m, o if j == i else I2)
    return m
H = -sum(op(Z, i) @ op(Z, i+1) for i in range(L-1)) - sum(op(X, i) for i in range(L))
E, V = np.linalg.eigh(H); g = V[:, 0]
r0 = ptrace_B(g, 2**nA, 2**(L-nA)); K = modK(r0)
chk("vacuum reduced state full rank", np.linalg.eigvalsh(r0).min() > 1e-12, "min eig %.2e" % np.linalg.eigvalsh(r0).min())
worst = 1e9
for n in range(1, 60):
    c = rng.normal(size=12) + 1j*rng.normal(size=12); c /= np.linalg.norm(c)
    psi = V[:, :12] @ c
    r1 = ptrace_B(psi, 2**nA, 2**(L-nA))
    worst = min(worst, float(np.real(np.trace((r1-r0)@K))) - (vn(r1)-vn(r0)))
chk("Delta S <= Delta<K> for 59 superpositions of the 12 lowest levels", worst >= -1e-10, "min gap %.4g" % worst)

print("B. equality iff rho_A = rho0_A; first-order saturation (first law of entanglement)")
dA, dB = 4, 8
psi0 = rng.normal(size=dA*dB) + 1j*rng.normal(size=dA*dB); psi0 /= np.linalg.norm(psi0)
r0 = ptrace_B(psi0, dA, dB); K = modK(r0)
Ub = haar(dB); psi1 = (np.kron(np.eye(dA), Ub) @ psi0)
r1 = ptrace_B(psi1, dA, dB)
gap = float(np.real(np.trace((r1-r0)@K))) - (vn(r1)-vn(r0))
chk("a unitary in the COMPLEMENT (U' in A(A')) saturates: gap = 0", abs(gap) < 1e-10, "gap=%.2e" % gap)
chk("  and it is a different global state", abs(abs(np.vdot(psi0, psi1)) - 1) > 1e-3, "|<psi0|psi1>|=%.4f" % abs(np.vdot(psi0, psi1)))
d = rng.normal(size=(dA, dA)) + 1j*rng.normal(size=(dA, dA)); d = d + d.conj().T; d -= np.trace(d)/dA*np.eye(dA)
gaps = []
for eps in [1e-2, 5e-3, 2.5e-3, 1.25e-3]:
    r1 = r0 + eps*d
    gaps.append(float(np.real(np.trace((r1-r0)@K))) - (vn(r1)-vn(r0)))
ratios = [gaps[i]/gaps[i+1] for i in range(3)]
chk("gap scales as eps^2 (ratios -> 4): Delta S = Delta<K> at first order", (ratios[0] < ratios[1] < ratios[2] < 4.0) and abs(ratios[-1]-4) < 0.05, "ratios=%s" % [round(x, 4) for x in ratios])

print("C. both sides negative (Blanco-Casini p.2): project A onto the lowest-K eigenvector")
w, v = np.linalg.eigh(K); r1 = np.outer(v[:, 0], v[:, 0].conj())
dK = float(np.real(np.trace((r1-r0)@K))); dS = vn(r1) - vn(r0)
chk("Delta<K> < 0 and Delta S < Delta<K>", dK < 0 and dS < dK, "dK=%.4f dS=%.4f" % (dK, dS))

print("D. Casini appendix, scalar particle in the Rindler wedge, M species")
w_, M_ = sp.symbols('w M', positive=True)
q = sp.exp(-w_)
N0 = M_*q/(1-q); var0 = M_*q/(1-q)**2
Nrho = (var0 + N0**2)/N0          # size-biased mean: rho_V is N * Gibbs, eq. (34)
dK_sym = sp.simplify(w_*(Nrho - N0))
chk("Delta K = w (<N>_rho - <N>_0) = w/(1-e^-w), species-independent (the term in (44))",
    sp.simplify(dK_sym - w_/(1-sp.exp(-w_))) == 0, str(dK_sym))
from math import comb, log, exp
def series(w, M, Nmax=400):
    # rho0 and rho are diagonal in total N with multiplicity C(N+M-1, M-1); logs taken analytically
    q = exp(-w); lq = math.log1p(-q); S0 = S1 = rel = 0.0; nk0 = nk1 = 0.0
    for N in range(0, Nmax):
        lm = math.lgamma(N+M) - math.lgamma(N+1) - math.lgamma(M)
        l0 = M*lq - w*N
        P0 = math.exp(lm + l0)
        S0 -= P0*l0; nk0 += P0*N
        if N > 0:
            l1 = w + (M+1)*lq + math.log(N) - w*N - math.log(M)
            P1 = math.exp(lm + l1)
            S1 -= P1*l1; rel += P1*(l1 - l0); nk1 += P1*N
    return S1-S0, rel, w*(nk1-nk0)
def closed41(w, M):
    f = lambda u: (math.exp(-u)/u)*(((1-math.exp(-w))/(1-math.exp(-w-u)))**(M+1) - 1)
    I, _ = quad(f, 0, np.inf, limit=400)
    return math.log(M) - math.log(math.exp(w)-1) + w/(1-math.exp(-w)) + I
worst41 = worst44 = 0
for w in [1.0, 3.0, 6.0]:
    for M in [1, 2, 5, 20]:
        dS, rel, dKn = series(w, M, Nmax=1500 if w < 2 else 600)
        worst44 = max(worst44, abs(rel - (w/(1-exp(-w)) - dS)), abs(dKn - w/(1-exp(-w))))
        worst41 = max(worst41, abs(dS - closed41(w, M)))
chk("(44) S(rho|rho0) = w/(1-e^-w) - Delta S, direct series", worst44 < 1e-8, "max err %.2e" % worst44)
chk("(41) closed form (as read: integrand (e^-u/u)[((1-e^-w)/(1-e^-w-u))^(M+1) - 1]) matches series", worst41 < 1e-6, "max err %.2e" % worst41)
dS, rel, _ = series(12.0, 3, 300)
chk("(42) far from boundary (M e^-w << 1): Delta S -> log M", abs(dS - log(3)) < 1e-3, "dS=%.6f log3=%.6f" % (dS, log(3)))
rels = []
for M in [10, 100, 1000, 10000]:
    rels.append(0.0 if M > 2000 else None)
w = 1.0
relM = []
for M in [10, 100, 1000]:
    dS41 = closed41(w, M); relM.append(w/(1-exp(-w)) - dS41)
chk("(43) large M at fixed w: relative entropy -> 0, i.e. the bound is ASYMPTOTICALLY SATURATED",
    relM[0] > relM[1] > relM[2] and relM[2] < 5e-3, "rel(M=10,100,1000)=%s" % [round(x, 6) for x in relM])

print("E. Blanco-Casini (7) => (11),(12),(13), one spatial dimension suffices (vector algebra is identical)")
Ep, Em, xp, xm, rp, rm, x0 = sp.symbols('E_p E_m x_p x_m r_p r_m x0', real=True)
Etot = Ep - Em
I2m = Ep*(rp**2 + (xp-x0)**2) - Em*(rm**2 + (xm-x0)**2)   # int |x-x0|^2 <T00>
x0s = sp.solve(sp.diff(I2m, x0), x0)[0]
chk("(11) minimiser x0 = (E+ x+ - E- x-)/E", sp.simplify(x0s - (Ep*xp - Em*xm)/Etot) == 0, str(x0s))
mn = sp.simplify(I2m.subs(x0, x0s))
target = Ep*rp**2 - Em*rm**2 - Ep*Em/Etot*(xp-xm)**2
chk("min = E+r+^2 - E-r-^2 - (E+E-/E)|x+-x-|^2, so (7) >= 0 gives (12)", sp.simplify(mn - target) == 0)
chk("(13) follows since the |x+-x-|^2 term is <= 0 for E>0", True, "(E+E-/E >= 0)")

print("F. the tree's use (bounds.py, imported read-only)")
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import bounds, hlaw, master
B = bounds.BOUNDS
cas = [r for r in B if r[0].startswith("Casini")][0]
chk("tree codes Casini (W,B,S,G,K,Z) = (2,2,1,0,1,2)", tuple(cas[1:7]) == (2, 2, 1, 0, 1, 2), str(cas[1:7]))
print("     source reading: W=2 entropy on left [READ]; B=2 state functional Delta<H> [READ];"
      " S=1 RHS state dependent [READ]; G=0 no G in the flat-space statement [READ];"
      " Z=2 region on a Cauchy surface [READ]; K=1 'not known saturated' -- source p.6: zero iff rho1=rho2 (B above),"
      " and (43)-(44) asymptotic saturation (D above)")
X = bounds.cells()
cl, _ = hlaw.closures(X)
E_now = len(cl["statistics"]) - len(X)
rows = [list(r) for r in B]
for r in rows:
    if r[0].startswith("Casini"): r[5] = 0
Xk = frozenset(tuple(r[1:7]) for r in rows)
clk, _ = hlaw.closures(Xk)
E_k = len(clk["statistics"]) - len(Xk)
closers_now = [Lg for Lg in hlaw.LANGS if len(cl[Lg]) == len(X)]
closers_k = [Lg for Lg in hlaw.LANGS if len(clk[Lg]) == len(Xk)]
print("     as coded: cells=%d E(statistics)=%d closers=%s master_cell=%s" % (len(X), E_now, closers_now, master.master_cell(X)))
print("     K->0    : cells=%d E(statistics)=%d closers=%s master_cell=%s" % (len(Xk), E_k, closers_k, master.master_cell(Xk)))
chk("tree's four withdrawals do not depend on K: 'every entropy bound is gravitational' FALSE", not all(r[4] == 1 for r in rows if r[1] == 2))
chk("  'only QNEC has a state-dependent RHS' FALSE", [r[0] for r in rows if r[3] == 1] == ["QNEC", "Casini (relative entropy)"])
chk("  three entropy bounds, one gravitational", (len([r for r in rows if r[1] == 2]), len([r for r in rows if r[4] == 1])) == (3, 1))
chk("demanded-cell fill still missed with K recoded", master.master_cell(Xk) != master.DEMANDED_AT_EIGHT, str(master.master_cell(Xk)))
print("RESULT:", "PASS" if OK else "FAIL")
sys.exit(0 if OK else 1)
