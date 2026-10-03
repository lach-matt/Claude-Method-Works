#!/usr/bin/env python3
"""
measure.py -- DOCKET 68, work item A3-measure: Q-1 (the substrate-free measure), H-INFO and R-INDEX.

Not seated.  Nothing here edits the board: every board figure is IMPORTED from the instrument that owns it
(nopath, massform, stock, wormhole, transit, tools/cypher), never retyped.

    python3 measure.py              report
    python3 measure.py --selftest   checks, with CONTROLS (cases built to fail, which must fail)
    python3 measure.py --json       the report's numbers as JSON

WHAT IT DOES
  (i)   Q-1.  Baez-Fritz-Leinster, arXiv:1106.1791v3, Theorem 2 (p.4), READ at source: a map F from morphisms of
        FinProb (finite sets with probability measures; measure-preserving FUNCTIONS) to [0, inf) that is
        functorial, convex-linear and continuous (in their sense, p.4) is F(f) = c (H(p) - H(q)), c >= 0.
        Verified computationally on random finite spaces: functoriality, convex linearity, continuity, the
        Faddeev grouping rule (Thm 5(iii)/Thm 6(iv), p.7-8), the uniform case phi(nm) = phi(n) + phi(m) (p.8),
        eq.(5) (p.6), and -- symbolically, sympy -- convex linearity on a generic map.  CONTROLS: four
        functionals that are NOT Shannon (squared loss, Renyi-2, Tsallis-2, Hartley-of-support) must each fail a
        named axiom.  Tsallis-2 must instead pass Theorem 7's degree-2 rule (p.10) -- a positive control.
        Quantum analogue: Parzygnat arXiv:2009.07125v3, Thm 1.4 = 4.26 (pp.3, 24), READ: von Neumann entropy
        difference, with "orthogonal affinity" replacing BFL's convex linearity; the difference can be NEGATIVE
        for quantum systems (p.2).
  (ii)  The Method's closed index.  |Lambda| = 976 and the product box 6,912 are COMPUTED by importing
        tools/cypher.py's own Lambda builder; the identity "6,912 = 976 + 0 + 5,936" is READ from
        method/members/The_Method_1_6-2.md line 4 (register 833 per the Physics Compendium) and the two are
        compared.  Per cell, under H-UNIFORM: log2 976 = 9.930737 and log2 6912 = 12.754888 bits.  Strong
        additivity is checked on the corpus's own partition.
  (iii) The exchange rates, each READ at source:
        HOLEVO   quant-ph/9611023v1 p.2-3 (entropy bound, capacity theorem); BSST quant-ph/9904023v5 p.2 (C1 <=
                 log2 d - avg S), p.1 (C_E = 2C for a noiseless channel; prior entanglement ALONE carries no
                 classical information), p.3 (FCCC >= C_E, "otherwise a violation of causality").
        LANDAUER Bennett physics/0210005v2 p.1 (statement), p.4 (k ln 2 per merge); Berut-Petrosyan-Ciliberto
                 1503.06537v1 p.2 (kT ln 2 per bit, ~3e-21 J at 300 K), p.13-14 (asymptote A = 0.72 kT, generalised
                 bound 0.19 kT at P = 80 %); del Rio et al. 1009.1630v2 p.2-4 (W(S|O) = H(S|O) kT ln 2; Bell pair
                 H(S|Q) = -1, net work gain kT ln 2 -- with operations on S and O jointly, NOT restricted to LOCC, p.3).
        BEKENSTEIN quant-ph/0404042v1 eq.(1) p.1 (S <= 2 pi E R / hbar c; E the total gravitating energy, which
                 "disposes of any ambiguity" about the zero of energy, p.1; E "must include the ground state
                 energy", p.8); board: bekenstein-bound NARROWED (docket67-raw/GRADES.tsv:96).
        and prices, in bits and joules, the information defining a 70 kg body under NAMED counting hypotheses,
        against the board's geometric prices (wormhole.throat_mass, nopath.coincidence_mass, massform floors).
  (iv)  Grades H-INFO, R-INDEX and Q-1 per obstruction (O-BITS, O-MAKE, O-HOLD, O-MATTER, O-LOOP).

NAMED HYPOTHESES (every limitation carried by name)
  H-FINITE   BFL's theorem is about FINITE sets and measure-preserving FUNCTIONS (deterministic maps); it says
             nothing about continuous spaces or stochastic maps.
  H-UNIT     c is undetermined by the theorem: bits are c = 1/ln 2, a choice of unit.
  H-ALT      WHICH alternatives count as distinguishable, and with WHAT probabilities, is outside the theorem.
             On The Method's index X is fixed by the coordinate list; for a physical object it is a choice.
  H-UNIFORM  per-cell figures assume every admitted cell equiprobable.  Any other measure gives fewer bits.
  H-LISTED   the body's composition is stock.HUMAN (ICRP Reference Man, as the board holds it, unlisted mass
             fraction 7.69e-5 dropped); atomic weights stock.ATOMIC_MASS; u = massform.U_KG.
  H-RHO      body density 1000 kg/m^3 (NOT read at source; a round assumption) -> V = M / rho.
  H-GRID     a classical "atomic-level definition" = species + position of every atom on a cubic grid of pitch
             delta, one atom per site, identical atoms of a species indistinguishable.  delta is a choice.
  H-THERMO   the body's thermodynamic entropy approximated as pure liquid water at 298.15 K, S = 69.95 J/(mol K)
             (NAMED-NOT-READ: a standard tabulated value not read at source this pass) -> the figure is
             CONDITIONAL on that datum.
  H-FAITHFUL to move a quantum definition its whole support (dimension d >= 2^S) must be transmitted noiselessly;
             then FCCC >= C_E = 2 log2 d (BSST p.3) -- at least 2 classical bits per qubit.
  H-ERASE    Landauer prices only logically irreversible steps (Bennett p.1): a joule figure is the price of
             ERASING (or resetting a register for) the count, not of holding or copying it.
  H-R        R = 1 m for the Bekenstein comparison (massform's H-R).
  H-TBODY    310 K for a warm-body reservoir; T_CMB = nopath.T_CMB for the coldest natural one.
  H-IT       (M's) spacetime comes from information.  NECESSARY for a measure-level statement to bear on a physical
             corridor; NOT sufficient (wave 2: C-verify-0 #0, #1).
  H-MEASURE-PHYSICAL (wave 2) under H-IT, the absence of an NEC from the measure is a fact about the corridor.  No
             instrument and no READ source supplies it; it is named so the grade can say what it would take.
  H-INFO-S   (wave 2) the sufficiency reading of M's premise: information at the destination SUFFICES to constitute
             the matter (CHARTER: "only the information defining it is necessary"; "the only multi-universal
             currency").  Graded against the board holding B-RECV (a holder must be at the destination).

WAVE 2 (repair after three adversarial verifications).  Wave 1 first said: R-INDEX 'PARTIAL', removing O-HOLD and
O-MAKE 'within the measure' because they are 'not expressible' there; the information is 'cheap at every exchange
rate' ('the costs-little half priced'); H-SETTLE x H-INFO 'removes O-BITS, in nlcontrol's model only'.  Now:
  * 'not expressible' is SILENCE, as for O-LOOP: within the measure O-HOLD, O-MAKE and O-LOOP are SILENT.  For a
    physical corridor the NEC and Geroch are NOT-BOUND-IF {H-IT, H-MEASURE-PHYSICAL} -- not REMOVED: showing a
    theorem cannot be stated in a formalism is not showing its conclusion false.  R-INDEX alone: LEAVES-ALL.
  * Landauer and Bekenstein give FLOORS (least energies), not prices.  No upper bound on any cost is computed here;
    Landauer prices erasure, which teleportation does not require; the Bekenstein floor is a property of the
    destination holder (O-MATTER), not a price of holding a corridor open.  The one READ-backed holder, the body,
    has Mc^2 = 6.29e18 J.
  * H-SETTLE x H-INFO shows a channel EXISTS in nlcontrol's model (chi = (2T)^2 eps^2/(8 ln 2) per use for small
    eps, computed coefficient 6.49 at T = 3) under H-C2; O-BITS is REMOVED-IF {N_EPS (A1's timing), H-C2,
    H-BORN-AT-BOB, H-FRAME3b}.  nlcontrol has no distance, so 'before light' is not defined inside it.
  * H-INFO-S is graded: a CLASH with B-RECV, not a removal (info_s_clash).
  * Checks that cannot fail by construction are printed STRUCTURAL and are not counted as controls.

stdlib + numpy (eigenvalues) + sympy (one symbolic identity).
"""
import contextlib
import io
import json
import math
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.join(HERE, "..")
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, WD)
sys.path.insert(0, os.path.join(REPO, "tools"))

import numpy as np  # noqa: E402

LN2 = math.log(2.0)


# ============================================================================ (i) Q-1: BFL Theorem 2

def H(p):
    """Shannon entropy in nats, 0 ln 0 = 0 (BFL p.3)."""
    return -sum(x * math.log(x) for x in p if x > 0)


def push(p, f, ny):
    """q_j = sum_{i in f^-1(j)} p_i (BFL Definition 1, p.3)."""
    q = [0.0] * ny
    for i, j in enumerate(f):
        q[j] += p[i]
    return q


def F_shannon(p, f, ny):
    """Information loss H(p) - H(q) of the measure-preserving function f: p -> q."""
    return H(p) - H(push(p, f, ny))


def F_eq5(p, f, ny):
    """BFL eq.(5), p.6: F(f) = sum_i p_i ln(q_f(i) / p_i) -- the conditional entropy of x given f(x)."""
    q = push(p, f, ny)
    return sum(pi * math.log(q[f[i]] / pi) for i, pi in enumerate(p) if pi > 0)


# control functionals (NOT Shannon); each must fail a named axiom
def F_squared(p, f, ny):
    return (H(p) - H(push(p, f, ny))) ** 2


def renyi2(p):
    s = sum(x * x for x in p)
    return -math.log(s)


def F_renyi2(p, f, ny):
    return renyi2(p) - renyi2(push(p, f, ny))


def tsallis2(p):
    return 1.0 - sum(x * x for x in p)


def F_tsallis2(p, f, ny):
    return tsallis2(p) - tsallis2(push(p, f, ny))


def F_hartley(p, f, ny, eps=0.0):
    sp = sum(1 for x in p if x > eps)
    sq = sum(1 for x in push(p, f, ny) if x > eps)
    return math.log(sp) - math.log(sq)


def rand_prob(rng, n, zeros=0):
    w = [rng.random() + 1e-3 for _ in range(n)]
    for k in range(zeros):
        w[k] = 0.0
    s = sum(w)
    return [x / s for x in w]


def rand_surj(rng, n, m):
    """A random function {0..n-1} -> {0..m-1} that hits every point (m <= n)."""
    f = list(range(m)) + [rng.randrange(m) for _ in range(n - m)]
    rng.shuffle(f)
    return f


def direct_sum(lam, p1, f1, ny1, p2, f2, ny2):
    """lam f (+) (1 - lam) g on the disjoint union (BFL p.3)."""
    p = [lam * x for x in p1] + [(1 - lam) * x for x in p2]
    f = list(f1) + [ny1 + j for j in f2]
    return p, f, ny1 + ny2


def check_functorial(F, rng, trials=300, tol=1e-10):
    worst = 0.0
    for _ in range(trials):
        a = rng.randint(3, 9)
        b = rng.randint(2, a)
        c = rng.randint(1, b)
        m = rand_prob(rng, a)
        g = rand_surj(rng, a, b)
        p = push(m, g, b)
        f = rand_surj(rng, b, c)
        fg = [f[g[i]] for i in range(a)]
        worst = max(worst, abs(F(m, fg, c) - F(m, g, b) - F(p, f, c)))
    return worst <= tol, worst


def check_convex(F, rng, trials=300, tol=1e-10, degree=1):
    """degree 1: BFL Thm 2(ii).  degree alpha: Thm 7(ii), F(lam f + (1-lam) g) = lam^a F(f) + (1-lam)^a F(g)."""
    worst = 0.0
    for _ in range(trials):
        n1, n2 = rng.randint(2, 7), rng.randint(2, 7)
        m1, m2 = rng.randint(1, n1), rng.randint(1, n2)
        p1, p2 = rand_prob(rng, n1), rand_prob(rng, n2)
        f1, f2 = rand_surj(rng, n1, m1), rand_surj(rng, n2, m2)
        lam = rng.random()
        p, f, ny = direct_sum(lam, p1, f1, m1, p2, f2, m2)
        lhs = F(p, f, ny)
        rhs = lam ** degree * F(p1, f1, m1) + (1 - lam) ** degree * F(p2, f2, m2)
        worst = max(worst, abs(lhs - rhs))
    return worst <= tol, worst


def check_continuity(F, steps=(1e-2, 1e-4, 1e-6, 1e-8, 1e-10), tol=1e-6):
    """BFL p.4: fixed sets and function, p(n) -> p pointwise.  Probe the hardest case: a point of p(n) whose
    mass -> 0 (the limit p has a zero), mapped onto a point that keeps mass."""
    f, ny = [0, 0, 1], 2
    limit = F([0.0, 0.5, 0.5], f, ny)
    gaps = [abs(F([e, 0.5 - e, 0.5], f, ny) - limit) for e in steps]
    return gaps[-1] <= tol, gaps


def check_nonneg(F, rng, trials=300):
    worst = 0.0
    for _ in range(trials):
        n = rng.randint(2, 9)
        m = rng.randint(1, n)
        p = rand_prob(rng, n)
        f = rand_surj(rng, n, m)
        worst = min(worst, F(p, f, m))
    return worst >= -1e-12, worst


def phi(n):
    """phi(n) = F(!) on the uniform n-point space (BFL p.8)."""
    return F_shannon([1.0 / n] * n, [0] * n, 1)


def check_uniform(N=30, tol=1e-12):
    worst = 0.0
    for n in range(1, N + 1):
        for m in range(1, N + 1):
            worst = max(worst, abs(phi(n * m) - phi(n) - phi(m)))
    log_ok = all(abs(phi(n) - math.log(n)) <= tol for n in range(1, 200))
    diffs = [phi(n + 1) - phi(n) for n in (10, 100, 1000, 10000)]
    return worst <= tol and log_ok and diffs[-1] < diffs[0], worst, diffs


def check_grouping(rng, trials=200, tol=1e-12):
    """Strong additivity, BFL Thm 6(iv) p.8: H(sum p_i q(i)) = H(p) + sum p_i H(q(i))."""
    worst = 0.0
    for _ in range(trials):
        n = rng.randint(2, 6)
        p = rand_prob(rng, n)
        qs = [rand_prob(rng, rng.randint(1, 5)) for _ in range(n)]
        joint = [pi * x for pi, q in zip(p, qs) for x in q]
        worst = max(worst, abs(H(joint) - H(p) - sum(pi * H(q) for pi, q in zip(p, qs))))
    return worst <= tol, worst


def check_eq5(rng, trials=200, tol=1e-12):
    worst = 0.0
    for _ in range(trials):
        n = rng.randint(2, 9)
        m = rng.randint(1, n)
        p = rand_prob(rng, n, zeros=rng.randint(0, 1))
        f = rand_surj(rng, n, m)
        worst = max(worst, abs(F_shannon(p, f, m) - F_eq5(p, f, m)))
    return worst <= tol, worst


def recover_c(scale=1.0 / LN2, rng=None):
    """Theorem 2's uniqueness, as a computation: fit c on ONE morphism (a fair coin crushed to a point), predict
    every other.  For F = scale * Shannon the fit is the scale and every prediction holds; for Renyi-2 the
    single-morphism fit fails elsewhere (control)."""
    rng = rng or random.Random(7)

    def fitted_err(F):
        c = F([0.5, 0.5], [0, 0], 1) / math.log(2.0)
        worst = 0.0
        for _ in range(200):
            n = rng.randint(2, 8)
            m = rng.randint(1, n)
            p = rand_prob(rng, n)
            f = rand_surj(rng, n, m)
            worst = max(worst, abs(F(p, f, m) - c * F_shannon(p, f, m)))
        return c, worst

    return fitted_err(lambda p, f, ny: scale * F_shannon(p, f, ny)), fitted_err(F_renyi2)


def symbolic_convex_linearity(entropy="shannon"):
    """sympy: F(lam f (+) (1-lam) g) - lam F(f) - (1-lam) F(g) == 0 identically, for f: 3 points -> 2 points and
    g: 2 points -> 1 point with symbolic measures.  ENCODING-DRIFT GUARD: the symbolic F is evaluated at random
    points and compared with F_shannon, the operator the report actually uses."""
    import sympy as sp
    a, b, c_, d, lam = sp.symbols("a b c d lam", positive=True)
    p1 = [a, b, 1 - a - b]
    f1 = [0, 0, 1]
    p2 = [d, 1 - d]
    f2 = [0, 0]

    def Hs(p):
        if entropy == "tsallis2":               # CONTROL: must NOT be convex-linear at degree 1
            return 1 - sum(x * x for x in p)
        return -sum(x * sp.log(x) for x in p)

    def pushs(p, f, ny):
        q = [sp.Integer(0)] * ny
        for i, j in enumerate(f):
            q[j] += p[i]
        return [sp.simplify(x) for x in q]

    def Fs(p, f, ny):
        return Hs(p) - Hs(pushs(p, f, ny))

    P = [lam * x for x in p1] + [(1 - lam) * x for x in p2]
    Ff = list(f1) + [2 + j for j in f2]
    expr = Fs(P, Ff, 3) - lam * Fs(p1, f1, 2) - (1 - lam) * Fs(p2, f2, 1)
    zero = sp.simplify(sp.expand(sp.expand_log(expr, force=True))) == 0
    rng = random.Random(11)
    drift = 0.0
    for _ in range(20):
        va, vb, vd, vl = 0.1 + 0.3 * rng.random(), 0.1 + 0.3 * rng.random(), rng.random(), rng.random()
        sub = {a: va, b: vb, d: vd, lam: vl}
        sym = float(Fs(p1, f1, 2).subs(sub))
        num = F_shannon([va, vb, 1 - va - vb], f1, 2)
        drift = max(drift, abs(sym - num))
    return zero, drift


def vacuity_guard(rng, trials=300):
    """The random instances are not trivial: some maps are non-injective, losses are positive and varied."""
    losses, noninj = [], 0
    for _ in range(trials):
        n = rng.randint(2, 9)
        m = rng.randint(1, n)
        p = rand_prob(rng, n)
        f = rand_surj(rng, n, m)
        noninj += m < n
        losses.append(F_shannon(p, f, m))
    return noninj > trials // 2 and max(losses) > 1.0 and min(losses) >= -1e-12, noninj, max(losses)


# ============================================================================ (ii) The Method's closed index

IDENTITY_FILE = os.path.join(REPO, "method", "members", "The_Method_1_6-2.md")


def read_identity():
    """READ, not scanned: the first 6 lines of the live main volume, where the identity is printed."""
    with open(IDENTITY_FILE, encoding="utf-8") as fh:
        head = [next(fh) for _ in range(6)]
    for line in head:
        m = re.search(r"([\d,]+) = ([\d,]+) \+ ([\d,]+) \+ ([\d,]+)", line)
        if m:
            return tuple(int(g.replace(",", "")) for g in m.groups()), line.strip()
    return None, None


def lambda_counts():
    """COMPUTED by tools/cypher.py's own builder (imported, never copied).  E is cypher's order operator."""
    import cypher
    ix = cypher._lambda()
    with contextlib.redirect_stdout(io.StringIO()):
        res = cypher.run(ix, "33.1", {})
    E = {v.language: v.E for v in res["_verdicts"]}
    return len(ix.cells), ix.box, E.get("order")


def method_bits():
    cells, box, E = lambda_counts()
    refused = box - cells - (E or 0)
    p_adm = cells / box
    chain = (-(p_adm * math.log2(p_adm) + (1 - p_adm) * math.log2(1 - p_adm))
             + p_adm * math.log2(cells) + (1 - p_adm) * math.log2(refused))
    return {"cells": cells, "box": box, "E_order": E, "refused": refused,
            "bits_per_cell": math.log2(cells), "bits_per_box_cell": math.log2(box),
            "closure_bits": math.log2(box / cells),
            "chain_rule_box": chain, "refused_fraction": refused / box}


# ============================================================================ (iii) exchange rates

def vn_entropy(rho):
    """von Neumann entropy in bits."""
    w = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    return float(-sum(x * math.log2(x) for x in w if x > 1e-14))


def holevo_chi(probs, states):
    avg = sum(p * s for p, s in zip(probs, states))
    return vn_entropy(avg) - sum(p * vn_entropy(s) for p, s in zip(probs, states))


def rand_density(rng, d, rank=None):
    rank = rank or rng.randint(1, d)
    A = np.array([[complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(rank)] for _ in range(d)])
    r = A @ A.conj().T
    return r / np.trace(r).real


def check_holevo(rng, trials=200):
    """chi <= log2 d - avg S (BSST p.2 form of the Holevo bound) <= log2 d, for d = 2, 4, 8 (1-3 qubits)."""
    worst = -1e9
    for _ in range(trials):
        d = rng.choice((2, 4, 8))
        k = rng.randint(2, 12)
        pr = rand_prob(rng, k)
        st = [rand_density(rng, d) for _ in range(k)]
        chi = holevo_chi(pr, st)
        avgS = sum(p * vn_entropy(s) for p, s in zip(pr, st))
        worst = max(worst, chi - (math.log2(d) - avgS))
    return worst <= 1e-9, worst


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULIS = [I2, X, Z, X @ Z]
BELL = np.array([1, 0, 0, 1], dtype=complex) / math.sqrt(2)


def ptrace_A(rho4):
    """Trace out the FIRST qubit (Alice's), leaving Bob's 2x2."""
    r = rho4.reshape(2, 2, 2, 2)
    return np.einsum("ijik->jk", r)


def ptrace_B(rho4):
    r = rho4.reshape(2, 2, 2, 2)
    return np.einsum("ijkj->ik", r)


def superdense(channel=False):
    """Alice encodes 2 bits by a Pauli on HER half of a Bell pair (Bennett-Wiesner, restated BSST p.1).
    Returns (chi of the joint states -- Bob holds both qubits after Alice SENDS hers;
             chi of Bob's qubit alone -- nothing sent).
    channel=True is the CONTROL: Alice's Pauli acts on a fresh |0> that IS delivered to Bob (a channel exists),
    so Bob's ensemble is {|0>, |1>, |0>, |1>}.  (A Pauli on Bob's own half of the Bell pair would NOT do: his
    reduced state stays I/2 -- local unitaries on a maximally mixed marginal leave it unchanged.)"""
    joint, bob = [], []
    zero = np.array([1, 0], dtype=complex)
    for P in PAULIS:
        v = np.kron(P, I2) @ BELL
        r = np.outer(v, v.conj())
        joint.append(r)
        if channel:
            w = P @ zero
            bob.append(np.outer(w, w.conj()))
        else:
            bob.append(ptrace_A(r))
    pr = [0.25] * 4
    return holevo_chi(pr, joint), holevo_chi(pr, bob)


def conditional_entropy_bell():
    """S(A|B) = S(AB) - S(B) for a Bell pair: -1 bit (del Rio et al. p.2, 'H(S|Q) = -n')."""
    r = np.outer(BELL, BELL.conj())
    return vn_entropy(r) - vn_entropy(ptrace_A(r))


def label_count_control():
    """CONTROL for the O-BITS fallacy 'count the labels, not the distinguishable states': four BB84 states on ONE
    qubit, uniform prior.  The label entropy H(pi) is 2 bits; the Holevo chi is 1 bit = log2 2.  A check that
    accepted H(pi) as the carried information would pass a value the bound forbids."""
    s0 = np.array([[1, 0], [0, 0]], dtype=complex)
    s1 = np.array([[0, 0], [0, 1]], dtype=complex)
    plus = np.array([[0.5, 0.5], [0.5, 0.5]], dtype=complex)
    minus = np.array([[0.5, -0.5], [-0.5, 0.5]], dtype=complex)
    pr = [0.25] * 4
    return H(pr) / LN2, holevo_chi(pr, [s0, s1, plus, minus])


def import_board():
    """Every board constant and price, imported from its owner."""
    with contextlib.redirect_stdout(io.StringIO()):
        import nopath
        import massform
        import stock
        import wormhole
        import transit
    return nopath, massform, stock, wormhole, transit


def landauer_j(bits, T):
    nopath = import_board()[0]
    return nopath.landauer_energy(bits, T)


def berut_generalised(p):
    """Berut et al. eq.(1), p.3: <Q> >= kT [ln 2 + p ln p + (1-p) ln(1-p)], in kT."""
    return LN2 + (p * math.log(p) if p > 0 else 0) + ((1 - p) * math.log(1 - p) if p < 1 else 0)


def bekenstein_floor_j(bits, R=1.0):
    """The least total gravitating energy E that Bekenstein's eq.(1) permits a complete system of radius R to
    have while holding `bits`: E >= bits hbar c ln2 / (2 pi R).  A FLOOR on the destination holder's energy
    (O-MATTER), not a price paid and not a cost of holding a corridor open."""
    nopath = import_board()[0]
    return bits * nopath.HBAR * nopath.C * LN2 / (2.0 * math.pi * R)


# ---------------------------------------------------------------- the object: a 70 kg body, under named counts

RHO_BODY = 1000.0          # H-RHO, NOT read
S_WATER = 69.95            # H-THERMO, J/(mol K), NAMED-NOT-READ
M_WATER = 18.015e-3        # kg/mol, H-THERMO (same status)
T_BODY = 310.0             # H-TBODY
GRID_PITCHES = (1e-10, 1e-11)   # H-GRID


def atom_counts():
    _, massform, stock, _, _ = import_board()
    M = massform.PAYLOAD_KG
    u = massform.U_KG
    return {e: f * M / (stock.ATOMIC_MASS[e] * u) for e, f in stock.HUMAN.items()}, M


def object_bits():
    N, M = atom_counts()
    Ntot = sum(N.values())
    frac = [n / Ntot for n in N.values()]
    species_bits_per_atom = H(frac) / LN2
    V = M / RHO_BODY
    out = {"atoms": Ntot, "species_bits_per_atom": species_bits_per_atom,
           "species_sequence_bits": Ntot * species_bits_per_atom, "volume_m3": V, "grid": {}}
    for delta in GRID_PITCHES:
        G = V / delta ** 3
        lg = math.lgamma(G + 1) - sum(math.lgamma(n + 1) for n in N.values()) - math.lgamma(G - Ntot + 1)
        out["grid"][delta] = {"sites": G, "fill": Ntot / G, "bits": lg / LN2, "bits_per_atom": lg / LN2 / Ntot}
    nopath = import_board()[0]
    S = (M / M_WATER) * S_WATER
    out["thermo_bits"] = S / (nopath.KB * LN2)
    return out


def price_table():
    nopath, massform, _, wormhole, transit = import_board()
    ob = object_bits()
    C2 = nopath.C ** 2
    counts = [("species sequence (H-LISTED)", ob["species_sequence_bits"]),
              ("grid 1 A (H-GRID, H-RHO)", ob["grid"][1e-10]["bits"]),
              ("grid 0.1 A (H-GRID, H-RHO)", ob["grid"][1e-11]["bits"]),
              ("thermal entropy (H-THERMO, CONDITIONAL)", ob["thermo_bits"])]
    rows = []
    for name, bits in counts:
        rows.append({"count": name, "bits": bits,
                     "landauer_J_310K": landauer_j(bits, T_BODY),
                     "landauer_J_TCMB": landauer_j(bits, nopath.T_CMB),
                     "bekenstein_floor_J_R1m": bekenstein_floor_j(bits, 1.0),
                     "qubits_sent_min_with_ebits": bits / 2.0,
                     "qubits_sent_min_without": bits,
                     "classical_bits_to_teleport_if_qubits": 2.0 * bits})
    geo = {"O-HOLD: wormhole.throat_mass(1 m) c^2": wormhole.throat_mass(1.0) * C2,
           "O-MAKE: nopath.coincidence_mass() c^2 (Proxima, contraction)": nopath.coincidence_mass() * C2,
           "O-MATTER: massform.rest_energy_j() (Mc^2, 70 kg)": massform.rest_energy_j(),
           "O-MATTER: massform.pair_floor_j() (B, L conserved floor)": massform.pair_floor_j()}
    ceilings = {"bekenstein ceiling, 70 kg, R = 1 m (massform)": massform.bekenstein_bits(),
                "holographic A/4, R = 1 m (nopath)": nopath.holographic_bits(1.0)}
    return rows, geo, ceilings, ob


# ============================================================================ (v) a complementary pairing
# H-SETTLE x H-INFO.  The O-BITS bound read above (BSST p.3: FCCC >= C_E) is argued from CAUSALITY -- "otherwise
# a violation of causality would occur".  nlcontrol.py (pre-docket, imported) shows a deterministic Weinberg-type
# drift makes Bob's state depend on Alice's basis.  The substrate-free measure prices that channel: Holevo chi of
# Bob's two ensembles, in bits per use.  NAMED: H-BORN-AT-BOB (Bob's final measurement obeys the Born rule, so his
# statistics are fixed by the ensemble-averaged density matrix), nlcontrol's own model (H = eps <X> Z at Bob,
# T = 3, 3000 steps), and Alice's two bases equiprobable.

def settle_bits(eps, lin=False):
    with contextlib.redirect_stdout(io.StringIO()):
        import nlcontrol as nl
    rs = {b: sum(np.outer(v, v.conj()) for v in (nl.evolve(s, eps, lin) for s in nl.ENS[b])) / 2 for b in "zx"}
    tr = 0.5 * float(np.abs(np.linalg.eigvalsh(rs["z"] - rs["x"])).sum())
    return holevo_chi([0.5, 0.5], [rs["z"], rs["x"]]), tr


def settle_small_eps_coefficient(T=3.0):
    """chi ~ k eps^2 for small eps: Bob's two ensembles are I/2 and Bloch (0, D, 0) with D = tanh(2 eps T) ~ 2 eps T;
    Holevo with prior 1/2 is D^2/(8 ln 2) to leading order, so k = (2T)^2/(8 ln 2).  Computed, not fitted."""
    return (2 * T) ** 2 / (8 * LN2)


def info_s_clash():
    """H-INFO-S against B-RECV, computed from what this file already holds.
      phi(1): Q-1 assigns 0 bits to a one-point space -- a destination with one state holds nothing, so I > 0 bits at
              the destination needs a holder with >= 2^I distinguishable states there (BFL, READ p.3-4);
      Bekenstein at E = 0: the bound admits 0 bits -- within its scope (complete, weakly self-gravitating systems,
              READ p.2) information presupposes gravitating energy at the destination;
      transit.CARRIES_SUBSTANCE: False -- the protocol moves state into a receiver already there.
    H-INFO-S says the arriving information suffices; B-RECV says a holder must already be there.  As commitments
    they clash; nothing computed here makes the information constitute its own holder."""
    nopath, _, _, _, transit = import_board()
    return {"phi_1_bits": phi(1), "bekenstein_bits_at_E0_R1m": nopath.bekenstein_bits(1.0, 0.0),
            "transit_CARRIES_SUBSTANCE": transit.CARRIES_SUBSTANCE,
            "holder_states_needed_for_1_bit": 2 ** 1}


# ============================================================================ (iv) grades

OBSTRUCTIONS = ("O-BITS", "O-MAKE", "O-HOLD", "O-MATTER", "O-LOOP")
VERDICTS = ("REMOVES", "PARTIAL", "LEAVES-ALL", "REFUTED", "OPEN", "CLASH")
# per-obstruction words (wave 2): LEAVES / SILENT (the formalism cannot state it) / NOT-BOUND-IF {premise} (a theorem
# does not bind; its conclusion is not shown false) / REMOVED-IF {premise} / REMOVED / OPEN / CLASH
REMOVING = ("REMOVED", "REMOVES")

GRADES = {
    "Q-1": {
        "verdict": "LEAVES-ALL",
        "reading": "DELIVERED as a measure: BFL Thm 2 verified on finite spaces (functorial, convex-linear, "
                   "continuous => c(H(p)-H(q))); quantum analogue READ (Parzygnat Thm 4.26).  A measure COUNTS; "
                   "it moves no bit, holds no throat, forms no matter, closes or opens no loop.",
        "per": {o: "LEAVES" for o in OBSTRUCTIONS},
    },
    "H-INFO": {
        "verdict": "LEAVES-ALL",
        "reading": "Clause (a) 'information can be quantified independently of physicalities' is SUPPORTED: the "
                   "BFL hypotheses name only finite sets, probability measures and functions (READ p.3-4) -- up "
                   "to H-UNIT and H-ALT.  Clause (b) 'matter cannot exist without it' is OPEN: the measure "
                   "assigns 0 bits to a one-point space and none of the READ exchange rates is a LOWER bound on "
                   "information per unit matter (Bekenstein is an upper bound).  Alone it removes no obstruction.  "
                   "It FLOORS, not prices, the transfer: erasing the information defining a 70 kg body would cost "
                   "AT LEAST 2.8e7-3.2e8 J at 310 K (2.5e5-2.8e6 J at T_CMB) under the four counts here -- and "
                   "teleportation need not erase -- and a holder at R = 1 m must have AT LEAST 33-379 J of "
                   "gravitating energy; no upper bound on any cost is computed, and the one READ-backed holder (the "
                   "body) has Mc^2 = 6.29e18 J.  Wave 1 first said these were the 'costs little' half 'priced'.",
        "per": {"O-BITS": "LEAVES (BSST p.1: prior entanglement alone carries no classical information; chi_Bob "
                          "= 0 computed)",
                "O-MAKE": "LEAVES (a premise about primacy is not a mechanism for identification)",
                "O-HOLD": "LEAVES (same)",
                "O-MATTER": "LEAVES (Bekenstein: a complete system with E > 0 must hold the bits)",
                "O-LOOP": "SILENT (no time variable) -- left, not decided"},
    },
    "H-INFO-S (sufficiency reading)": {
        "verdict": "CLASH",
        "reading": "Information at the destination suffices to constitute the matter.  Against the board holding "
                   "B-RECV it is a named clash, not a removal: Q-1 gives a one-state destination 0 bits (phi(1) = 0), "
                   "Bekenstein admits 0 bits at E = 0 within its scope, and transit.CARRIES_SUBSTANCE is False -- "
                   "the arriving state needs a receiver already there.  So O-MATTER's survival is a board-versus-M "
                   "clash, not something 'none of the seven touches'.  No instrument here shows information "
                   "constituting its own holder.",
        "per": {"O-BITS": "LEAVES", "O-MAKE": "LEAVES", "O-HOLD": "LEAVES",
                "O-MATTER": "CLASH (with B-RECV: REMOVED-IF {H-INFO-S} only in a board without B-RECV)",
                "O-LOOP": "SILENT"},
    },
    "R-INDEX": {
        "verdict": "LEAVES-ALL",
        "reading": "Within the measure there is no stress tensor, no metric and no manifold (BFL's objects are "
                   "finite probability spaces), so neither Morris-Thorne's NEC nor Geroch's theorem can be STATED.  "
                   "That is SILENCE, exactly as for O-LOOP -- wave 1 first called it 'removed within the measure' "
                   "and graded R-INDEX PARTIAL.  For a physical corridor the two theorems are NOT-BOUND-IF "
                   "{H-IT, H-MEASURE-PHYSICAL}: H-IT is necessary, not sufficient, and no source supplies the second "
                   "premise.  Energy and geometry re-enter at the exchange rates -- Holevo (moving), Landauer "
                   "(erasing), Bekenstein (holding: E the GRAVITATING energy, R a radius, READ p.1) -- each a FLOOR.  "
                   "The Bekenstein floor (33-379 J at R = 1 m) belongs to the destination holder, O-MATTER.",
        "per": {"O-BITS": "LEAVES (a cell's bits must still be sent: C_E = 2 log2 d per qudit sent; nothing "
                          "without a sent system)",
                "O-MAKE": "SILENT within the measure; for a physical corridor Geroch/Tipler NOT-BOUND-IF {H-IT, "
                          "H-MEASURE-PHYSICAL}",
                "O-HOLD": "SILENT within the measure; for a physical corridor the NEC NOT-BOUND-IF {H-IT, "
                          "H-MEASURE-PHYSICAL}; nothing here prices holding a corridor open",
                "O-MATTER": "LEAVES (a holder with at least 2^I distinguishable states must be at the "
                            "destination; Bekenstein E counts its rest energy, READ p.2, p.8; its floor 33-379 J)",
                "O-LOOP": "SILENT (the index has no time coordinate in the measure: not decided)"},
    },
    "H-SETTLE x H-INFO": {
        "verdict": "PARTIAL",
        "reading": "nlcontrol's drift (imported) under H-C2 carries chi_Bob = 6.49e-6 / 6.48e-4 / 5.71e-2 bits per "
                   "use at eps = 1e-3 / 1e-2 / 1e-1, T = 3 (linear control 0; small-eps law (2T)^2 eps^2/(8 ln 2), "
                   "coefficient 6.49 computed): a channel EXISTS in that model.  nlcontrol has no distance, so "
                   "'before light' is undefined inside it; the O-BITS removal is A1's, REMOVED-IF {N_EPS, H-C2, "
                   "H-BORN-AT-BOB, H-FRAME3b}.  Under C1 there is no channel.  Wave 1 first said 'removes O-BITS, in "
                   "nlcontrol's model only, at a priced capacity' and named H-BORN-AT-BOB but not H-C2.",
        "per": {"O-BITS": "REMOVED-IF {N_EPS (A1 eps > eps_any_advantage(L, N)), H-C2, H-BORN-AT-BOB, H-FRAME3b, "
                          "H-NLCONTROL-FORM for the figures}",
                "O-MAKE": "LEAVES (each use consumes a pre-distributed pair)", "O-HOLD": "LEAVES",
                "O-MATTER": "LEAVES", "O-LOOP": "LEAVES (A1: REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, N_SIGKEY})"},
    },
}


def grades_consistent():
    """Each verdict agrees with its per-obstruction words: LEAVES-ALL has no REMOVED/REMOVED-IF anywhere (SILENT and
    NOT-BOUND-IF are not removals); PARTIAL has at least one; CLASH has a CLASH entry."""
    ok = True
    for k, g in GRADES.items():
        ok &= g["verdict"] in VERDICTS
        ok &= set(g["per"]) == set(OBSTRUCTIONS)
        rem = any(v.startswith(REMOVING) for v in g["per"].values())
        if g["verdict"] == "LEAVES-ALL":
            ok &= not rem
        if g["verdict"] == "PARTIAL":
            ok &= rem
        if g["verdict"] == "CLASH":
            ok &= any(v.startswith("CLASH") for v in g["per"].values())
    return ok


def grades_consistent_control():
    """CONTROL: wave 1's R-INDEX grade (PARTIAL with no REMOVED word, only 'MOVED') must fail the rule above."""
    g = {"verdict": "PARTIAL", "per": {o: ("MOVED to the exchange rate" if o in ("O-HOLD", "O-MAKE") else "LEAVES")
                                       for o in OBSTRUCTIONS}}
    return any(v.startswith(REMOVING) for v in g["per"].values())


# ============================================================================ report / selftest

def collect():
    rows, geo, ceil, ob = price_table()
    mb = method_bits()
    ident, line = read_identity()
    sd = superdense()
    return {"method": mb, "identity_read": ident, "identity_line": line, "object": {
        "atoms": ob["atoms"], "species_bits_per_atom": ob["species_bits_per_atom"],
        "grid": {str(k): v for k, v in ob["grid"].items()}, "thermo_bits": ob["thermo_bits"]},
        "prices": rows, "geometric_J": geo, "ceilings_bits": ceil,
        "superdense_chi": {"joint_after_send": sd[0], "bob_alone": sd[1]},
        "S_A_given_B_bell": conditional_entropy_bell(),
        "settle_chi_bits_per_use": {str(e): settle_bits(e)[0] for e in (1e-3, 1e-2, 1e-1)},
        "grades": GRADES}


def report():
    d = collect()
    nopath = import_board()[0]
    print("DOCKET 68 / A3-measure -- Q-1, H-INFO, R-INDEX  (not seated)\n")
    m = d["method"]
    print("(ii) The Method's closed index (cypher._lambda, imported)")
    print(f"     |Lambda| = {m['cells']}, box = {m['box']}, E(order) = {m['E_order']}, refused = {m['refused']}"
          f"  | READ: {d['identity_line']}")
    print(f"     log2 976 = {m['bits_per_cell']:.6f} bits/cell (H-UNIFORM); log2 6912 = {m['bits_per_box_cell']:.6f}"
          f"; closure supplies log2(6912/976) = {m['closure_bits']:.6f} bits; chain rule on the partition = "
          f"{m['chain_rule_box']:.12f}")
    print("\n(iii) exchange rates")
    print(f"     superdense: chi(joint, after Alice SENDS her qubit) = {d['superdense_chi']['joint_after_send']:.6f}"
          f" bits; chi(Bob alone, nothing sent) = {d['superdense_chi']['bob_alone']:.2e}")
    print(f"     S(A|B) of a Bell pair = {d['S_A_given_B_bell']:.6f} bits (del Rio: erasure with entangled memory "
          f"yields kT ln2)")
    print(f"     kT ln2: 310 K {landauer_j(1, T_BODY):.4e} J; 300 K {landauer_j(1, 300.0):.4e} J; "
          f"T_CMB {landauer_j(1, nopath.T_CMB):.4e} J")
    print(f"\n     object: {d['object']['atoms']:.4e} atoms (stock.HUMAN), "
          f"{d['object']['species_bits_per_atom']:.4f} species bits/atom")
    for r in d["prices"]:
        print(f"     {r['count']:<42} {r['bits']:.4e} bits | Landauer FLOOR 310 K {r['landauer_J_310K']:.3e} J, T_CMB "
              f"{r['landauer_J_TCMB']:.3e} J | Bekenstein floor (R=1 m) {r['bekenstein_floor_J_R1m']:.3e} J | "
              f"teleport {r['classical_bits_to_teleport_if_qubits']:.3e} classical bits")
    print("     FLOORS, not prices: no upper bound on any cost is computed; Landauer prices erasure only (H-ERASE)")
    print("     board geometric figures (imported):")
    for k, v in d["geometric_J"].items():
        print(f"       {k:<62} {v:.4e} J")
    for k, v in d["ceilings_bits"].items():
        print(f"     ceiling: {k:<52} {v:.4e} bits")
    print("\n(v) H-SETTLE x H-INFO: the drift channel priced in bits per use (nlcontrol, imported)")
    grid_bits = d["prices"][1]["bits"]
    for eps in (1e-3, 1e-2, 1e-1):
        chi, tr = settle_bits(eps)
        chil, _ = settle_bits(eps, lin=True)
        print(f"     eps = {eps:<6} chi_Bob = {chi:.4e} bits/use (linear control {chil:.1e}); trace distance "
              f"{tr:.4e}; uses to carry the 1 A grid count: {grid_bits / chi:.3e}")
    print(f"     small-eps law chi = k eps^2, k = (2T)^2/(8 ln 2) = {settle_small_eps_coefficient():.4f} at T = 3 (under H-C2; C1 gives 0)")
    print(f"\n(vi) H-INFO-S vs B-RECV: {info_s_clash()}")
    print("\n(iv) grades")
    for k, g in GRADES.items():
        print(f"  {k}: {g['verdict']}")
        for o in OBSTRUCTIONS:
            print(f"     {o:<9} {g['per'][o]}")


def selftest():
    rng = random.Random(20261003)
    results = []

    def chk(name, ok, detail="", control=False, structural=False):
        """structural=True: the check cannot fail by construction (a literal, or a comparison of typed values).
        It is printed and must pass, but it is NOT counted as a control and is not evidence (wave 2)."""
        results.append((name, bool(ok), control and not structural, structural))
        tag = "[STRUCTURAL: cannot fail, not evidence] " if structural else ("[CONTROL] " if control else "")
        print(f"  {'ok  ' if ok else 'FAIL'} {tag}{name}  {detail}")

    print("(i) BFL Theorem 2 (1106.1791v3 p.4), on finite spaces")
    ok, w = check_functorial(F_shannon, rng); chk("Shannon loss is functorial", ok, f"max err {w:.1e}")
    ok, w = check_convex(F_shannon, rng); chk("Shannon loss is convex-linear", ok, f"max err {w:.1e}")
    ok, g = check_continuity(F_shannon); chk("Shannon loss is continuous at a vanishing point", ok,
                                              f"gaps {['%.1e' % x for x in g]}")
    ok, w = check_nonneg(F_shannon, rng); chk("Shannon loss is >= 0", ok, f"min {w:.1e}")
    ok, w, diffs = check_uniform(); chk("uniform case: phi(nm) = phi(n) + phi(m), phi(n) = ln n, phi(n+1)-phi(n) -> 0",
                                        ok, f"max err {w:.1e}; diffs {['%.1e' % x for x in diffs]}")
    ok, w = check_grouping(rng); chk("Faddeev grouping / strong additivity (Thm 6(iv), p.8)", ok, f"{w:.1e}")
    ok, w = check_eq5(rng); chk("eq.(5) p.6: loss = conditional entropy", ok, f"{w:.1e}")
    (c, werr), (c_r, werr_r) = recover_c()
    chk("uniqueness: c fitted on one morphism predicts all (bits: c = 1/ln2)",
        abs(c - 1 / LN2) < 1e-12 and werr < 1e-10, f"c = {c:.6f}, err {werr:.1e}")
    chk("Renyi-2 fitted on one morphism fails elsewhere", werr_r > 1e-3, f"err {werr_r:.3f}", control=True)
    zero, drift = symbolic_convex_linearity()
    chk("sympy: convex linearity holds identically (generic 3->2 (+) 2->1)", zero)
    chk("encoding-drift guard: symbolic F == F_shannon at 20 random points", drift < 1e-12, f"{drift:.1e}")
    zt, _ = symbolic_convex_linearity("tsallis2")
    chk("sympy: the same identity for Tsallis-2 does NOT vanish", not zt, "", True)
    ok, ni, mx = vacuity_guard(rng)
    chk("vacuity guard: instances non-trivial", ok, f"{ni}/300 non-injective, max loss {mx:.3f} nats")
    ok, w = check_functorial(F_squared, rng); chk("squared loss FAILS functoriality", not ok, f"{w:.3f}", True)
    ok, w = check_convex(F_renyi2, rng); chk("Renyi-2 loss FAILS convex linearity", not ok, f"{w:.3f}", True)
    ok, w = check_convex(F_tsallis2, rng); chk("Tsallis-2 loss FAILS degree-1 convex linearity", not ok, f"{w:.3f}", True)
    ok, w = check_convex(F_tsallis2, rng, degree=2)
    chk("Tsallis-2 PASSES Theorem 7's degree-2 rule (p.10) -- positive control", ok, f"{w:.1e}")
    ok, g = check_continuity(F_hartley); chk("Hartley-of-support FAILS continuity", not ok, f"gap {g[-1]:.3f}", True)
    ok, w = check_convex(F_hartley, rng); chk("Hartley-of-support FAILS convex linearity", not ok, f"{w:.3f}", True)
    ok, w = check_functorial(F_shannon, rng, tol=-1.0)
    chk("guard: a functoriality check with an impossible tolerance reports FAIL", not ok, "", True, structural=True)

    print("\n(ii) The Method's closed index")
    m = method_bits()
    ident, line = read_identity()
    chk("cypher._lambda: |Lambda| = 976, box = 6912 (computed)", m["cells"] == 976 and m["box"] == 6912)
    chk("cypher order operator: E(Lambda) = 0", m["E_order"] == 0)
    chk("READ identity matches computation: 6,912 = 976 + 0 + 5,936",
        ident == (m["box"], m["cells"], m["E_order"], m["refused"]), line or "")
    chk("identity is exact: 976 + 0 + 5,936 = 6,912", ident and ident[1] + ident[2] + ident[3] == ident[0])
    chk("a mis-stated identity (5,935 refused) fails the sum (literal arithmetic)",
        not (976 + 0 + 5935 == 6912), "", True, structural=True)
    # wave 2: the same control given content -- the READ-vs-computed comparison must reject a mis-stated line
    bad_line = "6,912 = 976 + 0 + 5,935"
    mm = re.search(r"([\d,]+) = ([\d,]+) \+ ([\d,]+) \+ ([\d,]+)", bad_line)
    bad_ident = tuple(int(g.replace(",", "")) for g in mm.groups())
    chk("a mis-stated identity line, parsed by read_identity's pattern, fails the comparison with cypher's computation",
        bad_ident != (m["box"], m["cells"], m["E_order"], m["refused"]), bad_line, True)
    chk("log2 976 = 9.930737 (charter)", abs(m["bits_per_cell"] - 9.930737) < 5e-7, f"{m['bits_per_cell']:.7f}")
    chk("log2 6912 = 12.754888 (charter)", abs(m["bits_per_box_cell"] - 12.754888) < 5e-7,
        f"{m['bits_per_box_cell']:.7f}")
    chk("strong additivity on the corpus's partition: H(box) = H(adm/ref) + sum", abs(m["chain_rule_box"] -
        m["bits_per_box_cell"]) < 1e-12, f"{m['chain_rule_box']:.12f}")
    worst = max(H(rand_prob(rng, 976)) / LN2 for _ in range(50))
    chk("H-UNIFORM is the maximum: 50 random measures on 976 cells all < log2 976", worst < m["bits_per_cell"],
        f"max {worst:.4f}")
    chk("a claim of 10.0 bits per cell exceeds log2 976 and is flagged", 10.0 > m["bits_per_cell"], "",
        True, structural=True)

    print("\n(iii) exchange rates")
    ok, w = check_holevo(rng); chk("Holevo: chi <= log2 d - avg S on 200 random ensembles, d = 2,4,8", ok,
                                   f"max excess {w:.1e}")
    labels, chi = label_count_control()
    chk("label entropy of 4 BB84 states = 2 bits", abs(labels - 2) < 1e-12)
    chk("their Holevo chi = 1 bit = log2 2", abs(chi - 1) < 1e-9, f"{chi:.6f}")
    chk("counting labels (2 bits) would breach log2 d = 1 -- flagged", labels > math.log2(2) + 1e-9, "",
        True)
    j, b = superdense()
    chk("superdense: chi of the four joint states = 2 bits = 2 log2 2 (C_E = 2C, BSST p.1)", abs(j - 2) < 1e-9,
        f"{j:.6f}")
    chk("prior entanglement alone carries nothing: chi(Bob, nothing sent) = 0 (BSST p.1)", abs(b) < 1e-9,
        f"{b:.1e}")
    jb, bb = superdense(channel=True)
    chk("when Alice's choice is DELIVERED to Bob (a channel), chi(Bob) = 1 > 0 -- the test sees it",
        bb > 0.99, f"{bb:.6f}", True)
    chk("S(A|B) of a Bell pair = -1 bit (del Rio p.2)", abs(conditional_entropy_bell() + 1) < 1e-9)
    nopath, massform, stock, wormhole, transit = import_board()
    chk("Berut p.2: kT ln2 at 300 K is ~3e-21 J", 2.5e-21 < landauer_j(1, 300.0) < 3.5e-21,
        f"{landauer_j(1, 300.0):.3e}")
    chk("Berut p.13: generalised bound at P = 0.80 is ~0.19 kT", abs(berut_generalised(0.80) - 0.19) < 0.005,
        f"{berut_generalised(0.80):.4f}")
    chk("Berut p.14: fitted asymptote A = 0.72 kT within the +/-0.15 kT bars of ln 2 (two READ numbers and ln 2)",
        abs(0.72 - LN2) <= 0.15, f"ln2 = {LN2:.4f}", structural=True)
    chk("a 'measured' 0.5 kT at full efficiency is below ln 2 and flagged", 0.5 < berut_generalised(1.0),
        "", True, structural=True)
    chk("board: massform.bekenstein_bits() = 1.80e45 (READ finding, 3e-3)",
        abs(massform.bekenstein_bits() / 1.80e45 - 1) < 3e-3, f"{massform.bekenstein_bits():.4e}")
    chk("Bekenstein floor inverts the bound: bits(floor(I)) = I",
        abs(nopath.bekenstein_bits(1.0, bekenstein_floor_j(1e30, 1.0)) / 1e30 - 1) < 1e-12)
    chk("R in cm instead of m moves the 70 kg figure by 100x -- flagged",
        abs(nopath.bekenstein_bits(100.0, massform.rest_energy_j()) / 1.80e45 - 1) > 1, "", True)
    chk("transit's DECLARED 2 bits/qubit agrees with the READ lower bound FCCC >= C_E = 2 log2 2",
        transit.CLASSICAL_BITS_PER_QUBIT == 2 * math.log2(2))
    chk("transit.BEATS_LIGHT is False (imported, not re-graded)", transit.BEATS_LIGHT is False)

    ob = object_bits()
    chk("atom count of 70 kg (stock.HUMAN) is 6.71e27", abs(ob["atoms"] / 6.7117e27 - 1) < 1e-3,
        f"{ob['atoms']:.5e}")
    chk("H-GRID at 1 A: one atom per site is possible (fill < 1)", ob["grid"][1e-10]["fill"] < 1,
        f"fill {ob['grid'][1e-10]['fill']:.4f}")
    chk("H-GRID at 3 A cannot seat the atoms (fill > 1) -- flagged",
        ob["atoms"] / ((70.0 / RHO_BODY) / (3e-10) ** 3) > 1, "", True)
    rows, geo, ceil, _ = price_table()
    allb = [r["bits"] for r in rows]
    chk("every count lies below the Bekenstein ceiling (1.80e45 bits)", max(allb) < massform.bekenstein_bits())
    chk("every Landauer FLOOR at 310 K is below the board's 1 m throat figure (a floor vs a board figure, not cost vs cost)",
        max(r["landauer_J_310K"] for r in rows) < wormhole.throat_mass(1.0) * nopath.C ** 2)
    chk("every Bekenstein floor (R = 1 m) is below Mc^2 of the body (the one READ-backed holder)", max(r["bekenstein_floor_J_R1m"] for r in rows)
        < massform.rest_energy_j())

    print("\n(v) H-SETTLE x H-INFO")
    c3, _ = settle_bits(1e-3); c2, _ = settle_bits(1e-2); c1, _ = settle_bits(1e-1)
    l2, _ = settle_bits(1e-2, lin=True)
    chk("drift channel carries information: chi_Bob(eps = 1e-2) > 0", c2 > 1e-5, f"{c2:.4e} bits/use")
    chk("linear control carries none: chi_Bob = 0", abs(l2) < 1e-12, f"{l2:.1e}", True)
    chk("small-eps scaling is quadratic: chi(1e-2)/chi(1e-3) ~ 100", 95 < c2 / c3 < 105, f"{c2 / c3:.2f}")
    chk("chi stays within Holevo's log2 2 = 1 bit", c1 <= 1.0, f"{c1:.4f}")
    k = settle_small_eps_coefficient()
    chk("small-eps law chi = (2T)^2 eps^2/(8 ln 2): computed coefficient 6.49 matches chi(1e-3)/1e-6", abs(c3 / 1e-6 / k - 1) < 1e-2,
        f"k = {k:.4f}, measured {c3 / 1e-6:.4f}")

    print("\n(vi) H-INFO-S against B-RECV (wave 2)")
    ic = info_s_clash()
    chk("Q-1: a one-state destination holds 0 bits (phi(1) = 0)", abs(ic["phi_1_bits"]) < 1e-15)
    chk("Bekenstein at E = 0 admits 0 bits (nopath.bekenstein_bits)", abs(ic["bekenstein_bits_at_E0_R1m"]) < 1e-12)
    chk("transit.CARRIES_SUBSTANCE is False (imported)", ic["transit_CARRIES_SUBSTANCE"] is False)
    chk("a two-state destination holds 1 bit (phi(2) = ln 2 nats)", abs(phi(2) / LN2 - 1) < 1e-12, "", True)

    print("\n(iv) grades")
    chk("grades well-formed and internally consistent (LEAVES-ALL has no removal; SILENT/NOT-BOUND-IF are not removals)",
        grades_consistent())
    chk("wave 1's R-INDEX grade (PARTIAL, only 'MOVED') fails the consistency rule", not grades_consistent_control(),
        "", True)
    bad = [n for n, ok, _, _ in results if not ok]
    nctl = sum(1 for _, _, c, _ in results if c)
    nst = sum(1 for _, _, _, st in results if st)
    print(f"\n{len(results) - len(bad)}/{len(results)} pass ({nctl} controls; {nst} structural checks, not counted as controls)")
    return not bad


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
