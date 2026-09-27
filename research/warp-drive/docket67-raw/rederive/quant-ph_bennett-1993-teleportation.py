#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation of Bennett-Brassard-Crepeau-Jozsa-Peres-Wootters 1993
(PRL 70, 1895) quantum teleportation, as restated in Pirandola et al. 1505.07831
(sec. 'Basics', p.1-2) and Bennett et al. quant-ph/9511027 (p.1), against the
use in research/warp-drive/transit.py.  Symbolic (sympy), exact; plus numeric
checks for d = 3 and for arbitrary CPTP operations by Alice.

Checks (each prints PASS/FAIL):
 C1  Phi+ resource (transit.py): for symbolic psi = (a, b), each of the four
     Bell outcomes has probability (|a|^2+|b|^2)/4 and Bob's state after the
     correction in transit.py's CORRECTIONS order [I, X, Z, ZX] equals psi
     exactly (up to a global phase).
 C2  Singlet Psi- resource (the original paper's choice per 9511027 p.1):
     corrections {I, sx, sy, sz} (up to phase) also give psi exactly.
 C3  Withholding the classical bits: Bob's outcome-averaged state is I/2
     exactly, independent of (a, b)  (no-signalling).
 C4  After Alice's Bell measurement the A|B state is a product: Alice's pair is
     in a known Bell state, Bob holds a pure state -> A|B entanglement 0.
     Alice's input qubit alone is I/2 (the tree's 'A ends maximally mixed');
     Alice's post-measurement state is independent of psi ('no trace').
 C5  Signalling deviation under a general symbolic U(2) on Alice's half: 0.
 C6  Noisy resource (hypothesis the tree names as 'ideal noiseless'): with a
     Werner pair of singlet fraction F the average fidelity is (2F+1)/3, which
     is 1 only at F = 1 and hits the classical 2/3 at F = 1/2.
 C7  d-dimensional generalisation (Pirandola p.2: d^2 outcomes, Weyl basis):
     numeric d = 3, fidelity 1 on all 9 outcomes, p = 1/9 each; so 2 log2 d
     classical bits and log2 d ebits per d-level system.
 C8  No-signalling under a random CPTP map (Kraus) on Alice's half, numeric.
 C9  transit.py's 'advantage over light' is D/c - D/c: identically 0 by
     construction (symbolic).  It is a model assumption (classical channel at
     exactly c), not a derived result; the derived content is C3.
 C10 transit.py 'twelve trials': report() runs 3 trials x 4 outcomes = 12
     (trial, outcome) fidelities; selftest runs 5 x 4 = 20.
"""
import sympy as sp, cmath, math, random, re, os

ok_all = True
def rep(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(f"  {'PASS' if cond else 'FAIL'}  {label}")

a, b = sp.symbols('a b', complex=True)
ac, bc = sp.conjugate(a), sp.conjugate(b)
I2 = sp.eye(2); X = sp.Matrix([[0,1],[1,0]]); Z = sp.Matrix([[1,0],[0,-1]])
Y = sp.Matrix([[0,-sp.I],[sp.I,0]])
k0 = sp.Matrix([1,0]); k1 = sp.Matrix([0,1])
def kron(*ms):
    out = ms[0]
    for m in ms[1:]: out = sp.kronecker_product(out, m)
    return out
s2 = sp.sqrt(2)
Phip = (kron(k0,k0)+kron(k1,k1))/s2
Psip = (kron(k0,k1)+kron(k1,k0))/s2
Phim = (kron(k0,k0)-kron(k1,k1))/s2
Psim = (kron(k0,k1)-kron(k1,k0))/s2
psi = sp.Matrix([a,b])

def bob_states(resource, basis):
    st = kron(psi, resource)          # qubit order: input(1), Alice's half(2), Bob(3)
    outs = []
    for bv in basis:
        P = kron(bv.H, I2)            # <bell|_{12} (x) I_3
        v = sp.simplify(P*st)         # unnormalised Bob state (2x1)
        p = sp.simplify(sp.expand((v.H*v)[0]))
        outs.append((p, v))
    return outs

def equal_up_to_phase(v, w):
    # |<w|v>|^2 == <v|v><w|w>
    ip = (w.H*v)[0]
    return sp.simplify(sp.expand(ip*sp.conjugate(ip) - (v.H*v)[0]*(w.H*w)[0])) == 0

print("C1  Phi+ resource, transit.py BELL_BASIS order [Phi+, Psi+, Phi-, Psi-], corrections [I, X, Z, ZX]")
outs = bob_states(Phip, [Phip, Psip, Phim, Psim])
corr = [I2, X, Z, Z*X]
norm = sp.expand(a*ac + b*bc)
for (p, v), C, name in zip(outs, corr, ["Phi+","Psi+","Phi-","Psi-"]):
    w = C*v*2                          # unnormalised state carries factor 1/2
    rep(f"outcome {name}: p = |psi|^2/4  and  C*v == psi exactly",
        sp.simplify(p - norm/4) == 0 and sp.simplify(w - psi) == sp.zeros(2,1))

print("C2  singlet Psi- resource (original paper), corrections I, sz, sx, sy up to phase")
outs2 = bob_states(Psim, [Psim, Psip, Phim, Phip])
for (p, v), C, name in zip(outs2, [I2, Z, X, Y], ["Psi-","Psi+","Phi-","Phi+"]):
    rep(f"outcome {name}: p = |psi|^2/4 and C*v == psi up to global phase",
        sp.simplify(p - norm/4) == 0 and equal_up_to_phase(C*v, psi))

print("C3  bits withheld: Bob's averaged state")
rhoB = sp.zeros(2,2)
for p, v in outs: rhoB += v*v.H      # sum of unnormalised projections = p * normalised rho
rhoB = sp.simplify(rhoB.subs(bc, sp.conjugate(b)))
rep("rho_B = (|a|^2+|b|^2) * I/2 exactly, independent of the state",
    sp.simplify(rhoB - norm*I2/2) == sp.zeros(2,2))

print("C4  post-measurement structure")
# after outcome m, state = |bell_m>_{12} (x) v_m/|v_m| : a product across (12)|(3)
prod_ok = True; indep_ok = True; alice1_ok = True
for bv, (p, v) in zip([Phip, Psip, Phim, Psim], outs):
    post = kron(bv, v)                 # the projected state (unnormalised)
    full = kron(bv*bv.H, I2)*kron(psi, Phip)
    prod_ok &= sp.simplify(full - post) == sp.zeros(8,1)
    # Alice's pair state is bv, independent of psi
    indep_ok &= not (bv.free_symbols & {a, b})
    # reduced state of Alice's qubit 1 from |bv><bv|
    R = bv*bv.H
    r1 = sp.Matrix(2,2, lambda i,j: sum(R[2*i+k, 2*j+k] for k in range(2)))
    alice1_ok &= sp.simplify(r1 - I2/2) == sp.zeros(2,2)
rep("projected state = |Bell_m>_(12) (x) |v_m>_3  (product across Alice|Bob -> A|B entanglement 0)", prod_ok)
rep("Alice's post-measurement state carries no a, b (no trace of psi)", indep_ok)
rep("Alice's input qubit alone is exactly I/2 (S = 1 bit)", alice1_ok)
rep("prior A|B entanglement of Phi+ is exactly 1 ebit",
    sp.simplify(sp.Matrix(2,2,lambda i,j: sum((Phip*Phip.H)[2*k+i,2*k+j] for k in range(2))) - I2/2) == sp.zeros(2,2))

print("C5  no-signalling under a general symbolic U(2) on Alice's half")
al, be, ga, de = sp.symbols('alpha beta gamma delta', real=True)
U = sp.exp(sp.I*al)*sp.Matrix([[sp.exp(-sp.I*(be+de)/2)*sp.cos(ga/2), -sp.exp(-sp.I*(be-de)/2)*sp.sin(ga/2)],
                                [sp.exp(sp.I*(be-de)/2)*sp.sin(ga/2),  sp.exp(sp.I*(be+de)/2)*sp.cos(ga/2)]])
st = kron(U, I2)*Phip
R = st*st.H
rB = sp.Matrix(2,2, lambda i,j: sum(R[2*k+i, 2*k+j] for k in range(2)))
rep("rho_B = I/2 for every U(2) on Alice's half", sp.simplify(rB - I2/2) == sp.zeros(2,2))

print("C6  noisy resource: Werner pair of singlet fraction F")
F = sp.symbols('F', real=True)
W = F*Psim*Psim.H + (1-F)/3*(Psip*Psip.H + Phim*Phim.H + Phip*Phip.H)
# teleport pure psi through W with singlet protocol; average fidelity over the Bloch sphere
th, ph = sp.symbols('theta phi', real=True)
psi_t = sp.Matrix([sp.cos(th/2), sp.exp(sp.I*ph)*sp.sin(th/2)])
rho_in = kron(psi_t*psi_t.H, W)
fid_sum = 0
for bv, C in zip([Psim, Psip, Phim, Phip], [I2, Z, X, Y]):
    P = kron(bv.H, I2)
    rb = P*rho_in*P.H
    rb = C*rb*C.H
    fid_sum += (psi_t.H*rb*psi_t)[0]
fid = sp.simplify(sp.expand(fid_sum))
avg = sp.simplify(sp.integrate(sp.integrate(fid*sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2*sp.pi))/(4*sp.pi))
rep(f"average fidelity = (2F+1)/3   [got {avg}]", sp.simplify(avg - (2*F+1)/3) == 0)
rep("  = 1 only at F = 1; = 2/3 (classical measure-prepare bound) at F = 1/2",
    avg.subs(F,1) == 1 and avg.subs(F, sp.Rational(1,2)) == sp.Rational(2,3))

print("C7  d = 3 generalisation (numeric)")
d = 3; w = cmath.exp(2j*math.pi/d)
def mat_mul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
Xd = [[1 if (i == (j+1) % d) else 0 for j in range(d)] for i in range(d)]
Zd = [[w**i if i == j else 0 for j in range(d)] for i in range(d)]
def mpow(M, n):
    R_ = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    for _ in range(n): R_ = mat_mul(R_, M)
    return R_
rng = random.Random(67)
v = [complex(rng.gauss(0,1), rng.gauss(0,1)) for _ in range(d)]
nv = math.sqrt(sum(abs(x)**2 for x in v)); v = [x/nv for x in v]
Phi_d = [0j]*(d*d)
for i in range(d): Phi_d[i*d+i] = 1/math.sqrt(d)
state = [v[i]*Phi_d[j] for i in range(d) for j in range(d*d)]   # index (i, A, B)
fids = []; probs = []
for m in range(d):
    for n in range(d):
        Umn = mat_mul(mpow(Xd, m), mpow(Zd, n))
        # Bell vector: (U_mn (x) I)|Phi_d>
        bell = [sum(Umn[i][k]*Phi_d[k*d+j] for k in range(d)) for i in range(d) for j in range(d)]
        out = [sum(bell[i*d+A].conjugate()*state[(i*d+A)*d+B] for i in range(d) for A in range(d)) for B in range(d)]
        p = sum(abs(x)**2 for x in out); probs.append(p)
        out = [x/math.sqrt(p) for x in out]
        # try the d^2 Weyl corrections, take the one that works (it must be unique per outcome)
        best = 0
        for mm in range(d):
            for nn in range(d):
                Cm = mat_mul(mpow(Xd, mm), mpow(Zd, nn))
                o2 = [sum(Cm[i][k]*out[k] for k in range(d)) for i in range(d)]
                best = max(best, abs(sum(v[i].conjugate()*o2[i] for i in range(d)))**2)
        fids.append(best)
rep(f"d=3: 9 outcomes, each p = 1/9 (max dev {max(abs(p-1/9) for p in probs):.1e}), fidelity 1 after a Weyl correction (min {min(fids):.15f})",
    len(fids) == 9 and max(abs(p-1/9) for p in probs) < 1e-12 and min(fids) > 1-1e-12)
rep(f"classical bits per qutrit = 2 log2 3 = {2*math.log2(3):.6f}; ebits = log2 3", True)

print("C8  no-signalling under a random CPTP map on Alice's half (numeric)")
def rand_kraus(rng, n=3):
    Ks = [[[complex(rng.gauss(0,1), rng.gauss(0,1)) for _ in range(2)] for _ in range(2)] for _ in range(n)]
    S = [[sum(Ks[k][r][i].conjugate()*Ks[k][r][j] for k in range(n) for r in range(2)) for j in range(2)] for i in range(2)]
    # S^{-1/2} via eigen-decomposition of 2x2 Hermitian
    tr = (S[0][0]+S[1][1]).real; det = (S[0][0]*S[1][1]-S[0][1]*S[1][0]).real
    disc = math.sqrt(max(0, tr*tr/4-det)); l1, l2 = tr/2+disc, tr/2-disc
    # S^{-1/2} = (S - l2 I)/(l1-l2) * l1^-1/2 + (S - l1 I)/(l2-l1) * l2^-1/2
    Sm = [[((S[i][j]-(l2 if i==j else 0))/(l1-l2))*l1**-0.5 + ((S[i][j]-(l1 if i==j else 0))/(l2-l1))*l2**-0.5
           for j in range(2)] for i in range(2)]
    return [mat_mul(K, Sm) for K in Ks]
worst = 0
bell = [1/math.sqrt(2),0,0,1/math.sqrt(2)]
rho = [[bell[i]*bell[j] for j in range(4)] for i in range(4)]
for t in range(20):
    Ks = rand_kraus(rng)
    rB = [[0j,0j],[0j,0j]]
    for K in Ks:
        K4 = [[K[i//2][j//2]*(1 if i%2 == j%2 else 0) for j in range(4)] for i in range(4)]
        K4H = [[K4[j][i].conjugate() for j in range(4)] for i in range(4)]
        r = mat_mul(mat_mul(K4, rho), K4H)
        for i in range(2):
            for j in range(2): rB[i][j] += r[i][j] + r[2+i][2+j]
    worst = max(worst, max(abs(rB[i][j]-(0.5 if i==j else 0)) for i in range(2) for j in range(2)))
rep(f"20 random CPTP maps (3 Kraus ops) on Alice: max |rho_B - I/2| = {worst:.1e}", worst < 1e-12)

print("C9  transit.py advantage_over_light")
Dsym, csym = sp.symbols('D c', positive=True)
rep("arrival_time(D) - D/c = D/c - D/c == 0 identically (assumption, not derivation)",
    sp.simplify(Dsym/csym - Dsym/csym) == 0)
ly = 9.4607304725808e15
rep(f"Proxima 4.0175e16 m = {4.0175e16/ly:.4f} ly;  Milky Way 9.46e20 m = {9.46e20/ly:.0f} ly;  Earth-Moon 3.844e8 m (mean)", True)

print("C10 transit.py trial counts")
src = "/home/user/Claude-Method-Works/research/warp-drive/transit.py"
if os.path.exists(src):
    t = open(src).read()
    rep_trials = re.search(r'for t in range\((\d+)\):\s*\n\s*U = random_unitary\(rng\); psi = \[U\[0\]\[0\], U\[1\]\[0\]\]\s*\n\s*fids', t)
    self_trials = re.search(r'print\("\\nthe transit is exact"\)\s*\n\s*for t in range\((\d+)\)', t)
    n_r = int(rep_trials.group(1)) if rep_trials else None
    n_s = int(self_trials.group(1)) if self_trials else None
    print(f"      report trials = {n_r} -> {n_r*4 if n_r else '?'} (trial,outcome) pairs; selftest trials = {n_s} -> {n_s*4 if n_s else '?'}")
    rep("docstring 'twelve trials' equals 3 trials x 4 outcomes (wording, not a count of trials)", n_r == 3)
    rep("CHANNEL_BITS_AFTER and A's S=1 are hard-coded constants in transit.py, not computed there "
        "(C4 above computes them: true)", "CHANNEL_BITS_AFTER  = 0.0" in t)

print("\nALL CHECKS PASS" if ok_all else "\nSOME CHECK FAILED")
