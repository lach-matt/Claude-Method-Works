#!/usr/bin/env python3
"""DOCKET 67 -- rederivation for 'bell-pair-entanglement-entropy'.
Source: Bennett, Bernstein, Popescu, Schumacher, quant-ph/9511030, eq. (4):
  E = -Tr rho_A log2 rho_A = -Tr rho_B log2 rho_B = -sum c_i^2 log2 c_i^2,
  '1 ebit for a maximally entangled pair of two-state particles (eg theta = pi/4)'.
Checks, exact (sympy) unless noted:
 C1  S(rho_B) of the tree's BELL = (|00>+|11>)/sqrt2 is exactly 1 bit; S(rho_A) equal.
 C2  E(theta) for cos t|00> + sin t|11> is H2(cos^2 t); max 1 at t = pi/4 only (on [0,pi/2]).
 C3  transit.entropy2 (imported read-only) agrees with exact eigen-entropy on random 2x2 states.
 C4  after teleportation, for every Bell outcome m: the post-measurement pure state of
     (input q0, A-half q1 | B q2) is a product across the A|B cut -> E_after = 0 exactly
     (the tree DECLARES CHANNEL_BITS_AFTER = 0.0 at transit.py:139; here it is computed).
 C5  A's input qubit q0 alone after the Bell measurement is I/2 (S = 1) for every outcome
     and independent of psi (the tree checks a hard-coded diag(0.5,0.5), transit.py:341-342).
 C6  the non-increase (LOCC monotone) that forbids 're-use': teleport half of a Bell pair
     with reference R; after the protocol E(R|B) = 1 and E(A-side|B) = 0: the ebit moved,
     total A|B entanglement did not increase (BBPS p.6 'cannot increase the expected entropy').
 C7  mixed-channel caveat: for a Werner mixture p|Phi+><Phi+| + (1-p) I/4, S(rho_B) = 1 bit
     for EVERY p, including separable p <= 1/3 -- S(rho_B) is an entanglement measure only
     under the purity hypothesis (BBPS sec. V).
"""
import sys, math, random, importlib.util
import sympy as sp

bad = 0
def chk(label, ok, got=""):
    global bad
    bad += (not ok)
    print(f"  {'ok  ' if ok else 'FAIL'} {label}  {got}")

def ket(bits):
    v = sp.zeros(2**len(bits), 1); v[int(bits, 2)] = 1; return v

def ptrace(rho, keep, n):
    """partial trace of an n-qubit density matrix, keeping qubits in `keep` (qubit 0 = MSB)."""
    keep = sorted(keep); dk = 2**len(keep)
    out = sp.zeros(dk, dk)
    for i in range(2**n):
        for j in range(2**n):
            bi = format(i, f"0{n}b"); bj = format(j, f"0{n}b")
            if all(bi[q] == bj[q] for q in range(n) if q not in keep):
                a = int("".join(bi[q] for q in keep), 2); b = int("".join(bj[q] for q in keep), 2)
                out[a, b] += rho[i, j]
    return out

def S2(rho):
    s = 0
    for lam, mult in rho.eigenvals().items():
        lam = sp.nsimplify(sp.simplify(lam))
        if lam != 0:
            s += -mult * lam * sp.log(lam, 2)
    return sp.simplify(s)

print("C1  Bell pair entropy of entanglement")
BELL = (ket("00") + ket("11")) / sp.sqrt(2)
rho = BELL * BELL.H
rB = ptrace(rho, [1], 2); rA = ptrace(rho, [0], 2)
chk("rho_B = I/2 exactly", sp.simplify(rB - sp.eye(2)/2) == sp.zeros(2), rB.tolist())
chk("S(rho_B) = 1 bit exactly", S2(rB) == 1, S2(rB))
chk("S(rho_A) = S(rho_B)", sp.simplify(S2(rA) - S2(rB)) == 0)

print("C2  E(theta) = H2(cos^2 theta), max 1 bit only at pi/4")
t = sp.symbols("t", positive=True)
c2 = sp.cos(t)**2
E = -c2*sp.log(c2, 2) - (1-c2)*sp.log(1-c2, 2)
chk("E(pi/4) = 1", sp.simplify(E.subs(t, sp.pi/4)) == 1, sp.simplify(E.subs(t, sp.pi/4)))
x = sp.symbols("x", positive=True)
H = -x*sp.log(x, 2) - (1-x)*sp.log(1-x, 2)
crit = sp.solve(sp.diff(H, x), x)
chk("unique stationary point of H2 on (0,1) is x = 1/2", crit == [sp.Rational(1, 2)], crit)
chk("H2 strictly concave", sp.simplify(sp.diff(H, x, 2) + 1/(x*(1-x)*sp.log(2))) == 0)

print("C3  transit.entropy2 against exact eigen-entropy (read-only import)")
p = "/home/user/Claude-Method-Works/research/warp-drive/transit.py"
spec = importlib.util.spec_from_file_location("transit_ro", p)
tr = importlib.util.module_from_spec(spec); spec.loader.exec_module(tr)
rng = random.Random(67); worst = 0.0
for _ in range(200):
    a = rng.random(); b = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
    # random 2-qubit pure state -> reduced state
    v = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(4)]
    nrm = math.sqrt(sum(abs(z)**2 for z in v)); v = [z/nrm for z in v]
    r = tr.ptrace_first(tr.rho_from(v))
    # exact eigenvalues via closed form
    trr = (r[0][0] + r[1][1]).real
    det = (r[0][0]*r[1][1] - r[0][1]*r[1][0]).real
    l1 = trr/2 + math.sqrt(max(0, trr*trr/4 - det)); l2 = trr - l1
    ref = -sum(l*math.log2(l) for l in (l1, l2) if l > 1e-15)
    # Schmidt route: singular values of the 2x2 coefficient matrix
    M = sp.Matrix([[v[0], v[1]], [v[2], v[3]]])
    sv = [complex(s).real**2 for s in M.singular_values()]
    ref2 = -sum(l*math.log2(l) for l in sv if l > 1e-15)
    worst = max(worst, abs(tr.entropy2(r) - ref), abs(tr.entropy2(r) - ref2))
chk("entropy2 = Schmidt-coefficient Shannon entropy (200 random states)", worst < 1e-10, f"worst {worst:.2e}")
chk("transit.entropy2(ptrace_first(BELL)) = 1", abs(tr.entropy2(tr.ptrace_first(tr.rho_from(tr.BELL))) - 1) < 1e-12)

print("C4/C5  teleportation: E across A|B after each outcome, and A's input qubit")
al, be = sp.symbols("alpha beta")
psi = al*ket("0") + be*ket("1")
state = sp.kronecker_product(psi, BELL)   # qubits q0 (input), q1 (A half), q2 (B)
bells = [(ket("00")+ket("11"))/sp.sqrt(2), (ket("01")+ket("10"))/sp.sqrt(2),
         (ket("00")-ket("11"))/sp.sqrt(2), (ket("01")-ket("10"))/sp.sqrt(2)]
norm_sub = {al*sp.conjugate(al): 1 - be*sp.conjugate(be)}
allprod = True; allmixed = True
for m, bv in enumerate(bells):
    P = sp.kronecker_product(bv*bv.H, sp.eye(2))
    post = P*state
    pm = sp.simplify((post.H*post)[0].subs(norm_sub))
    post = post / sp.sqrt(pm)
    rho3 = post*post.H
    rAside = ptrace(rho3, [0, 1], 3)    # q0q1
    # purity of A-side reduced state: 1 <=> product across A|B <=> E_after = 0
    pur = sp.simplify(sp.expand((rAside*rAside).trace()).subs(norm_sub))
    rq0 = sp.simplify(ptrace(rho3, [0], 3).subs(norm_sub))
    allprod &= (sp.simplify(pur - 1) == 0)
    allmixed &= (sp.simplify(rq0 - sp.eye(2)/2) == sp.zeros(2))
    print(f"    outcome {m}: p = {pm},  Tr(rho_A-side^2) = {pur},  rho_q0 = {rq0.tolist()}")
chk("E_after(A|B) = 0 for all four outcomes, any alpha,beta (computed, not declared)", allprod)
chk("A's input qubit = I/2 for all outcomes, independent of psi", allmixed)

print("C6  the ebit moves: teleport half of a Bell pair with reference R")
# qubits: R, q0 (to be teleported), q1 (A half), q2 (B)
st4 = sp.kronecker_product(BELL, BELL)   # (R,q0) Bell  x  (q1,q2) Bell
X = sp.Matrix([[0, 1], [1, 0]]); Z = sp.Matrix([[1, 0], [0, -1]]); I2 = sp.eye(2)
corr = [I2, X, Z, Z*X]
ok6 = True
for m, bv in enumerate(bells):
    P = sp.kronecker_product(sp.eye(2), bv*bv.H, sp.eye(2))
    post = P*st4; pm = sp.simplify((post.H*post)[0]); post = post/sp.sqrt(pm)
    post = sp.kronecker_product(sp.eye(8), corr[m])*post
    r = post*post.H
    E_RB = S2(sp.simplify(ptrace(r, [0], 4)))              # R vs rest; check R|B via purity of RB
    rRB = sp.simplify(ptrace(r, [0, 3], 4))
    pRB = sp.simplify((rRB*rRB).trace())
    rAside = sp.simplify(ptrace(r, [1, 2], 4)); pA = sp.simplify((rAside*rAside).trace())
    ok6 &= (pm == sp.Rational(1, 4) and pRB == 1 and E_RB == 1 and pA == 1)
    print(f"    outcome {m}: p={pm}  (R,B) pure={pRB}  S(R)={E_RB}  A-side pure={pA}")
chk("R-B end with 1 ebit; A-side|B end with 0: the ebit is transferred, never multiplied", ok6)

print("C7  purity hypothesis: S(rho_B) is not an entanglement measure for a mixed channel")
pp = sp.symbols("p", nonnegative=True)
W = pp*rho + (1-pp)*sp.eye(4)/4
rBW = ptrace(W, [1], 2)
chk("S(rho_B) of Werner state = 1 for all p", sp.simplify(rBW - sp.eye(2)/2) == sp.zeros(2))
# PPT test: partial transpose eigenvalue min = (1-3p)/4 -> separable (2x2) iff p <= 1/3
def ptranspose_B(r):
    out = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            a, b = divmod(i, 2); c, d = divmod(j, 2)
            out[a*2+d, c*2+b] = r[i, j]
    return out
ev = ptranspose_B(W).eigenvals()
chk("min PT eigenvalue = (1-3p)/4 -> separable for p <= 1/3 yet S(rho_B) = 1",
    any(sp.simplify(e - (1-3*pp)/4) == 0 for e in ev), list(ev))

print("\n" + ("REDERIVE PASS" if bad == 0 else f"REDERIVE FAIL -- {bad}"))
sys.exit(1 if bad else 0)
