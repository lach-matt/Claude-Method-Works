#!/usr/bin/env python3
"""
geometry.py -- DOCKET 68, work item A4-geometry: H-IT (spacetime from information), H-ZERO (with H-IT), H-NULL and
the reading R-QUANTUM.

Not seated.  Nothing here edits the board.  Board figures are IMPORTED from the instrument that owns them --
zero.py, nullinfo.py, cosmin.py (pre-docket, beside this file), ../achievable.py (duration_bound, hold_time, the
Fewster constant, CODATA constants) and ../transit.py (BEATS_LIGHT, TRAVERSAL_IS_REMOVED) -- never retyped.

    python3 geometry.py              report
    python3 geometry.py --selftest   checks, with CONTROLS (cases built to fail, which must fail)
    python3 geometry.py --json       the report's numbers as JSON

Needs numpy, sympy, z3-solver (pip install z3-solver).  About 10-20 s, most of it sympy.

SOURCES, READ at source through alphaXiv on 2026-10-03 (arXiv is the object, M-D67-2).  Page numbers are the PDF's.
  Gao & Wald, arXiv:gr-qc/0007021v2 (28 Jul 2000), all 15 pages.  Thm 1 p.6, Thm 2 pp.12-13; hypotheses NEC (2) and
      the null generic condition (9) (p.4), strong causality and compactness of J+(p)^J-(q) (p.12); footnote 3 p.12
      lets Borde's averaged condition replace the NEC; p.14: pure AdS fails the null generic condition.  The paper
      reads Thm 2 as a "time delay" relative to AdS (p.6, p.14); it does NOT mention a CFT or boundary causality --
      that holographic reading is NAMED-NOT-READ here.
  Van Raamsdonk, arXiv:1005.3035v2 (v2 dated 7 Jul 2025; essay of 31 Mar 2010), all 8 pages.  Eq.(1) the entangled
      state, p.2; horizons that "forbid communication" are associated with "the absence of interactions between the
      two CFTs", p.2; eq.(2) mutual information bounds correlations, p.4; eq.(3) <O O> ~ e^{-mL}, p.4; pinch-off,
      pp.3-5; footnote 1 p.4: geometry likely fails "before the entanglement is strictly zero".
  Jacobson, arXiv:gr-qc/9504004v2 (6 Jun 1995), all 8 pages.  Eqs.(1)-(6) pp.4-5; Lambda "for some constant", p.5;
      G = (4 hbar eta)^-1 and "The undetermined cosmological constant ... remains as enigmatic as ever", p.6; the
      derivation presumes local equilibrium, p.6.
  Bousso, Fisher, Koeller, Leichenauer & Wall, arXiv:1509.02542v2 (15 Sep 2015).  Abstract p.1; p.1-2 (<T_kk> at a
      point can be made negative "with magnitude as large as we wish"); p.2 RHS "can have any sign"; p.4 "fixed
      background spacetimes with no dynamical gravity"; p.4 quantum expansion -> classical expansion as hbar -> 0;
      eq.(2.2) p.7; eq.(5.3) p.25 (uniform second variation <= sum of diagonal ones, by strong subadditivity).
  Maldacena & Susskind, arXiv:1306.0533v2: footnote 1 p.2 (non-traversability "can be shown using the integrated
      null energy condition"; "If this were not true, the ER=EPR connection would be wrong"); p.16 sec.3.1; p.16-17
      sec.3.2 (no bridge between distant black holes "without preexisting bridges"; pairs made together, then
      separated, then merged, do make one); p.17 non-trivial topologies "should be allowed as possible quantum
      states".
  Padmanabhan & Padmanabhan, arXiv:1703.06144v1, pp.6-7: emergent gravity -- field equations "invariant under the
      addition of a constant to the matter Lagrangian", Lambda "an integration constant".
  Board holdings (DOCKET 67 grades, docket67-raw/GRADES.tsv and audits/): Bousso hep-th/9905177 bousso-covariant
      NARROWED (hypotheses: Einstein's equation, dominant -- or null + causal -- energy condition); QNEC BFKLW
      NARROWED; 1208.5399 NARROWED (duration bound eq.(4), C ~ 3.17); fewster-osterbrink-qei NARROWED; gr-qc/0209036
      NARROWED; kontou-fo-ffkp-nmc-qei NARROWED; gr-qc/9510071 NARROWED; gr-qc/9506083 STANDS -- which is
      Poisson-Visser thin-shell stability, NOT a quantum energy inequality (a discrepancy in the charter's list).
"""
import contextlib
import io
import json
import math
import os
import random
import sys

import numpy as np
import sympy as sp
import z3

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, ".."))

_IMPORT_LOG = {}


def _quiet(modname):
    """Import a pre-docket script without letting its top-level prints through."""
    if modname in sys.modules:
        return sys.modules[modname]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mod = __import__(modname)
    _IMPORT_LOG[modname] = buf.getvalue()
    return mod


zero = _quiet("zero")
nullinfo = _quiet("nullinfo")
cosmin = _quiet("cosmin")
achievable = _quiet("achievable")
transit = _quiet("transit")

HBAR, C, G, LP = achievable.HBAR, achievable.C_SI, achievable.G_SI, achievable.L_PLANCK
R0 = 1.0          # the throat radius the charter asks for, metres

# =====================================================================================================================
# PART (i) -- H-IT.  The READ emergent-spacetime model: two non-interacting systems in Van Raamsdonk's eq.(1).
# MODEL CHOICE (named H-QUDIT): a d-level system with E_i = i stands in for one CFT; the TFD state of eq.(1) is
# then |psi(beta)> = sum_i exp(-beta E_i / 2)|i>|i> / sqrt(Z).  The CFT, the bulk and Ryu-Takayanagi are not modelled;
# only the quantum-information statements the essay makes are, and those hold for any finite system.
# =====================================================================================================================

def tfd(d, beta):
    w = np.exp(-beta * np.arange(d) / 2.0)
    psi = np.zeros(d * d, dtype=complex)
    for i in range(d):
        psi[i * d + i] = w[i]
    return psi / np.linalg.norm(psi)


def rho_of(psi):
    return np.outer(psi, psi.conj())


def ptrace(rho, d, keep):
    r = rho.reshape(d, d, d, d)
    return np.einsum('ijkj->ik', r) if keep == 0 else np.einsum('ijil->jl', r)


def vn_bits(r):
    ev = np.linalg.eigvalsh((r + r.conj().T) / 2)
    ev = ev[ev > 1e-15]
    return float(-(ev * np.log2(ev)).sum())


def haar(d, rng):
    z = (rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    ph = np.diag(r) / np.abs(np.diag(r))
    return q * ph


def bob_state_after(psi, d, alice_op):
    """Bob's reduced state after Alice applies a local unitary, or a local projective measurement whose outcome Bob
    is not told (alice_op = ('U', U) or ('M', basis)).  This is the statistic the docket's question is about."""
    rho = rho_of(psi)
    I = np.eye(d)
    if alice_op[0] == 'U':
        K = np.kron(alice_op[1], I)
        out = K @ rho @ K.conj().T
    else:
        B = alice_op[1]
        out = np.zeros_like(rho)
        for k in range(d):
            P = np.outer(B[:, k], B[:, k].conj())
            K = np.kron(P, I)
            out += K @ rho @ K.conj().T
    return ptrace(out, d, keep=1)


def it_no_signal(d=4, betas=(0.1, 0.7, 2.0), trials=150, seed=68):
    """Max over Alice's choices of the change in Bob's state.  Linear QM: 0 (a theorem; computed here)."""
    rng = np.random.default_rng(seed)
    worst = 0.0
    for beta in betas:
        psi = tfd(d, beta)
        ref = ptrace(rho_of(psi), d, keep=1)
        thermal = np.diag(np.exp(-beta * np.arange(d)))
        thermal /= np.trace(thermal)
        worst = max(worst, float(np.abs(ref - thermal).max()))   # Van Raamsdonk p.2: Tr_2 |psi><psi| = rho_T
        for _ in range(trials):
            for op in (('U', haar(d, rng)), ('M', haar(d, rng))):
                worst = max(worst, float(np.abs(bob_state_after(psi, d, op) - ref).max()))
    return worst


def it_coupled_control(d=4, beta=0.7, g=0.9, seed=5):
    """CONTROL: the same two systems WITH an interaction after Alice's choice, U_int = exp(-i g Z_A (x) X_B).
    Van Raamsdonk ties non-communication to the absence of interactions (p.2); with one, Bob's state must depend on
    Alice's choice.  Returns the largest change -- the detector must see it."""
    rng = np.random.default_rng(seed)
    Z = np.diag(np.exp(2j * np.pi * np.arange(d) / d))
    Zh = (Z + Z.conj().T) / 2
    X = np.roll(np.eye(d), 1, axis=0)
    Xh = (X + X.T) / 2
    H = np.kron(Zh, Xh)
    ev, V = np.linalg.eigh(H)
    Uint = V @ np.diag(np.exp(-1j * g * ev)) @ V.conj().T
    psi = tfd(d, beta)
    outs = []
    for _ in range(12):
        U = np.kron(haar(d, rng), np.eye(d))
        st = Uint @ (U @ psi)
        outs.append(ptrace(rho_of(st), d, keep=1))
    return max(float(np.abs(a - b).max()) for a in outs for b in outs)


def mutual_info_bits(psi, d):
    rho = rho_of(psi)
    return vn_bits(ptrace(rho, d, 0)) + vn_bits(ptrace(rho, d, 1)) - vn_bits(rho)


def vr_eq2_check(d=4, betas=(0.05, 0.3, 1.0, 3.0, 8.0), trials=200, seed=11, factor=1.0):
    """Van Raamsdonk eq.(2), p.4: I(C,D) >= (<O_C O_D> - <O_C><O_D>)^2 / (2 |O_C|^2 |O_D|^2), I in nats (log base
    e is the reading taken; with base 2 the bound is weaker by ln 2 on the left, so nats is the stricter reading).
    `factor` multiplies the right side -- the CONTROL passes factor >> 1 and must find a violation."""
    rng = np.random.default_rng(seed)
    fails, Is = 0, []
    for beta in betas:
        psi = tfd(d, beta)
        I_nats = mutual_info_bits(psi, d) * math.log(2)
        Is.append(I_nats / math.log(2))
        rho = rho_of(psi)
        for _ in range(trials):
            A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d)); A = (A + A.conj().T) / 2
            B = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d)); B = (B + B.conj().T) / 2
            I = np.eye(d)
            eAB = np.trace(rho @ np.kron(A, B)).real
            eA = np.trace(rho @ np.kron(A, I)).real
            eB = np.trace(rho @ np.kron(I, B)).real
            nA = np.abs(np.linalg.eigvalsh(A)).max(); nB = np.abs(np.linalg.eigvalsh(B)).max()
            rhs = factor * (eAB - eA * eB) ** 2 / (2 * nA ** 2 * nB ** 2)
            if I_nats < rhs - 1e-12:
                fails += 1
    monotone = all(Is[i] > Is[i + 1] for i in range(len(Is) - 1))
    return fails, Is, monotone


def locc_entropy_change(d=4, beta=0.7, trials=100, seed=3, nonlocal_control=False):
    """Entanglement entropy across the cut under LOCAL unitaries U_A (x) U_B (Maldacena-Susskind sec.3.2: LOCC cannot
    create or increase entanglement; local unitaries are the reversible part and must leave it EXACTLY unchanged).
    CONTROL: a nonlocal unitary (a generalised CNOT) must change it."""
    rng = np.random.default_rng(seed)
    psi = tfd(d, beta)
    S0 = vn_bits(ptrace(rho_of(psi), d, 0))
    worst = 0.0
    for _ in range(trials):
        if nonlocal_control:
            CN = np.zeros((d * d, d * d))
            for a in range(d):
                for b in range(d):
                    CN[a * d + (a + b) % d, a * d + b] = 1   # |a,b> -> |a, a+b>
            st0 = np.zeros(d * d, complex); st0[0] = 1     # product |0,0>
            st = CN @ (np.kron(haar(d, rng), np.eye(d)) @ st0)
            worst = max(worst, abs(vn_bits(ptrace(rho_of(st), d, 0)) - 0.0))
        else:
            st = np.kron(haar(d, rng), haar(d, rng)) @ psi
            worst = max(worst, abs(vn_bits(ptrace(rho_of(st), d, 0)) - S0))
    return S0, worst


# ---- Gao-Wald Theorem 2, as logic.  The theorem: (NEC or Borde-ANEC) & NullGeneric & StrongCausality & Compact &
# TimelikeBoundary  =>  every causal curve between boundary points p, q in A-dot(p) lies in the boundary, i.e. NO bulk
# shortcut.  Encoded propositionally; what z3 adds is only bookkeeping of which hypothesis a shortcut must break --
# the content is the theorem's, READ.
GW_HYPS = ["NEC_or_BordeANEC", "NullGeneric", "StrongCausality", "Compactness", "TimelikeBoundary"]


def gw_python(assign):
    """The theorem's implication as a plain function (the encoding-drift reference)."""
    return (not all(assign[h] for h in GW_HYPS)) or (not assign["Shortcut"])


def gao_wald_z3():
    v = {h: z3.Bool(h) for h in GW_HYPS + ["Shortcut"]}
    thm = z3.Implies(z3.And(*[v[h] for h in GW_HYPS]), z3.Not(v["Shortcut"]))
    out = {}
    s = z3.Solver(); s.add(thm, *[v[h] for h in GW_HYPS]); out["vacuity_hyps_sat"] = s.check() == z3.sat
    s = z3.Solver(); s.add(thm, *[v[h] for h in GW_HYPS], v["Shortcut"]); out["shortcut_with_all_hyps"] = str(s.check())
    s = z3.Solver(); s.add(thm, v["Shortcut"], z3.Not(v["NEC_or_BordeANEC"]),
                           *[v[h] for h in GW_HYPS if h != "NEC_or_BordeANEC"])
    out["shortcut_with_NEC_broken_only"] = str(s.check())
    # which single hypotheses, if dropped, re-admit a shortcut: each one (the theorem gives no ranking among them)
    out["each_single_drop_readmits"] = []
    for h in GW_HYPS:
        s = z3.Solver(); s.add(thm, v["Shortcut"], z3.Not(v[h]), *[v[k] for k in GW_HYPS if k != h])
        out["each_single_drop_readmits"].append((h, str(s.check())))
    # encoding drift: z3's thm vs gw_python on all 64 assignments
    drift = 0
    names = GW_HYPS + ["Shortcut"]
    for m in range(2 ** len(names)):
        a = {n: bool((m >> i) & 1) for i, n in enumerate(names)}
        zv = z3.simplify(z3.substitute(thm, *[(v[n], z3.BoolVal(a[n])) for n in names]))
        drift += (z3.is_true(zv) != gw_python(a))
    out["encoding_drift"] = drift
    return out


# =====================================================================================================================
# PART (ii) -- H-ZERO, alone and with H-IT.
# =====================================================================================================================

def _rv(v):
    from fractions import Fraction
    return z3.RealVal(str(Fraction(float(v))))     # exact rational of the double: no parse drift


def nec_shift_z3(control_timelike=False):
    """z3 (nonlinear real arithmetic): for EVERY symmetric T, every lambda and every null k = (1, x, y, z) with
    x^2+y^2+z^2 = 1, k.(T + lambda g).k == k.T.k.  Proved by UNSAT of the negation.  CONTROL: the same statement
    for a unit timelike u = (ch, sh, 0, 0) with ch^2 - sh^2 = 1 must be SAT (the WEC density does move)."""
    T = [[z3.Real(f"T{min(i, j)}{max(i, j)}") for j in range(4)] for i in range(4)]
    lam = z3.Real("lam")
    g = [-1, 1, 1, 1]
    if control_timelike:
        ch, sh = z3.Reals("ch sh")
        k = [ch, sh, 0, 0]
        prem = z3.And(ch * ch - sh * sh == 1, ch > 0)
    else:
        x, y, zz = z3.Reals("x y z")
        k = [1, x, y, zz]
        prem = (x * x + y * y + zz * zz == 1)
    q = lambda M: sum(M(i, j) * k[i] * k[j] for i in range(4) for j in range(4))
    base = q(lambda i, j: T[i][j])
    shifted = q(lambda i, j: T[i][j] + (lam * g[i] if i == j else 0))
    s = z3.Solver(); s.add(prem); vac = s.check() == z3.sat                       # vacuity guard
    s = z3.Solver(); s.add(prem, shifted != base); res = str(s.check())
    # encoding drift: evaluate both sides numerically at random points against numpy
    rng = random.Random(9); drift = 0.0
    for _ in range(20):
        Tn = np.array([[0.0] * 4 for _ in range(4)])
        for i in range(4):
            for j in range(i, 4):
                Tn[i, j] = Tn[j, i] = rng.uniform(-3, 3)
        ln = rng.uniform(-5, 5)
        if control_timelike:
            eta = rng.uniform(-2, 2); kn = np.array([math.cosh(eta), math.sinh(eta), 0, 0])
            sub = [(ch, _rv((kn[0]))), (sh, _rv((kn[1])))]
        else:
            a, b = rng.uniform(0, 2 * math.pi), rng.uniform(0, math.pi)
            kn = np.array([1, math.cos(a) * math.sin(b), math.sin(a) * math.sin(b), math.cos(b)])
            sub = [(x, _rv((kn[1]))), (y, _rv((kn[2]))), (zz, _rv((kn[3])))]
        sub += [(T[i][j], _rv((Tn[i, j]))) for i in range(4) for j in range(i, 4)] + [(lam, _rv((ln)))]
        zval = z3.simplify(z3.substitute(shifted - base, *sub))
        zf = float(zval.as_fraction()) if z3.is_rational_value(zval) else float(zval.as_decimal(20).rstrip('?'))
        nval = kn @ (Tn + ln * np.diag(g)) @ kn - kn @ Tn @ kn
        drift = max(drift, abs(zf - nval))
    return {"vacuity_premise_sat": vac, "negation": res, "drift_vs_numpy": drift}


def jacobson_null_equation():
    """Jacobson gr-qc/9504004v2 eqs.(2),(5),(6), pp.4-5.  delta Q = T dS on every local Rindler horizon gives
    T_kk = (hbar eta / 2 pi) R_kk for all null k -- ONLY the null-null part.  Computed: (a) contract eq.(6),
    R_ab - R g_ab/2 + Lambda g_ab = (2 pi/hbar eta) T_ab, with null k: Lambda and R drop out, leaving exactly
    R_kk = (2 pi / hbar eta) T_kk.  (b) T_ab -> T_ab + lam g_ab leaves it unchanged.  (c) CONTROL: the same contraction
    with a unit timelike u keeps Lambda.  (d) the sign bookkeeping of eqs.(2),(5): with lambda < 0 on the past
    horizon and kappa > 0, delta Q and delta A both carry the sign of T_kk (resp. R_kk)."""
    Lam, lam, Rs, hb, eta = sp.symbols('Lambda lam R hbar eta', real=True)
    Rm = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"R{min(i, j)}{max(i, j)}", real=True))
    Tm = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"T{min(i, j)}{max(i, j)}", real=True))
    g = sp.diag(-1, 1, 1, 1)
    a1, a2 = sp.symbols('a1 a2', real=True)
    k = sp.Matrix([1, sp.cos(a1) * sp.sin(a2), sp.sin(a1) * sp.sin(a2), sp.cos(a2)])
    eq6 = Rm - Rs * g / 2 + Lam * g - (2 * sp.pi / (hb * eta)) * Tm          # = 0
    con = sp.simplify((k.T * eq6 * k)[0])
    target = sp.simplify((k.T * Rm * k)[0] - (2 * sp.pi / (hb * eta)) * (k.T * Tm * k)[0])
    a_ok = sp.simplify(con - target) == 0
    b_ok = sp.simplify((k.T * (Tm + lam * g) * k)[0] - (k.T * Tm * k)[0]) == 0
    w = sp.symbols('w', real=True)
    u = sp.Matrix([sp.cosh(w), sp.sinh(w), 0, 0])
    con_u = sp.expand((u.T * eq6 * u)[0])
    c_keeps_Lambda = sp.diff(con_u, Lam) != 0
    # (d) signs: on lambda in [-eps, 0], with constant T_kk = t, R_kk = (2 pi/hbar eta) t:
    l, eps, kap, t, dA0 = sp.symbols('l epsilon kappa t dA0', real=True)
    dQ = -kap * sp.integrate(l * t, (l, -eps, 0)) * dA0
    dA = -sp.integrate(l * (2 * sp.pi / (hb * eta)) * t, (l, -eps, 0)) * dA0
    pos = {eps: 1, kap: 1, hb: 1, eta: 1, dA0: 1}
    d_ok = (sp.sign(dQ.subs(pos).subs(t, -1)) == -1) and (sp.sign(dA.subs(pos).subs(t, -1)) == -1)
    G_of_eta = sp.Rational(1, 4) / (hb * eta)                               # p.6: G = (4 hbar eta)^-1
    return {"null_contraction_drops_Lambda_and_R": a_ok, "zero_shift_invisible": b_ok,
            "CONTROL_timelike_keeps_Lambda": bool(c_keeps_Lambda), "negative_Tkk_gives_dQ_dA_negative": d_ok,
            "G_of_eta": str(G_of_eta), "dQ": str(sp.simplify(dQ)), "dA": str(sp.simplify(dA))}


# =====================================================================================================================
# PART (iii) -- H-NULL.  The throat against the light-sheet construction, and the QNEC price (nullinfo.py).
# =====================================================================================================================

def ricci(gm, X):
    n = len(X)
    ginv = gm.inv()
    Gam = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(gm[d, b], X[c]) + sp.diff(gm[d, c], X[b]) - sp.diff(gm[b, c], X[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                                        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n))
                                        for a in range(n)))
    return Ric


_MT = {}


def morris_thorne():
    """Morris-Thorne, Phi = 0: ds^2 = -dt^2 + dr^2/(1 - b/r) + r^2 dOmega^2 (geometric units).  Radial null tangent
    k = (1, sqrt(1 - b/r), 0, 0) is affinely parametrised (dt/dlambda = E = 1 for g_tt = -1).  Computed:
      R_kk(r) and its throat value; equality with 8 pi (rho + p_r) of zero.py; the expansion theta = (2/r) dr/dlambda
      of the radial null congruence from a sphere of radius r, and d theta / d lambda at the throat."""
    if _MT:
        return _MT
    t, r, th, ph = sp.symbols('t r theta phi', positive=True)
    r0 = sp.symbols('r_0', positive=True)
    b = sp.Function('b')(r)
    gm = sp.diag(-1, 1 / (1 - b / r), r ** 2, r ** 2 * sp.sin(th) ** 2)
    Ric = ricci(gm, [t, r, th, ph])
    k = sp.Matrix([1, sp.sqrt(1 - b / r), 0, 0])
    Rkk = sp.simplify((k.T * Ric * k)[0])
    # zero.py's rho + p_r (imported expression), times 8 pi
    assert zero.r == r and zero.b == b          # same symbol and function: zero.py's expressions apply as they stand
    nec_zero = sp.simplify(8 * sp.pi * (zero.rho + zero.p_r))
    agree = sp.simplify(Rkk - nec_zero) == 0
    drdl = sp.sqrt(1 - b / r)
    theta = 2 / r * drdl
    dtheta = sp.simplify(sp.diff(theta, r) * drdl)        # d theta / d lambda = d theta/dr * dr/dlambda
    bp = sp.symbols('bprime', real=True)
    at_throat = lambda e: sp.simplify(e.subs(sp.Derivative(b, r), bp).subs(b, r0).subs(r, r0))
    _MT.update(r=r, r0=r0, b=b, bp=bp, Rkk=Rkk, agree=agree, theta=theta, dtheta=dtheta,
               Rkk_throat=at_throat(Rkk), dtheta_throat=at_throat(dtheta), theta_throat=at_throat(theta))
    return _MT


def shape_checks():
    """Concrete shapes: flare-out shapes have theta = 0 at r0 and theta > 0 on BOTH sides (r increases away from the
    throat on either sheet), so no congruence leaving the throat sphere has theta <= 0: no light-sheet.  CONTROLS:
    Minkowski (b = 0) -- the inward congruence of any sphere has theta < 0, a light-sheet exists; b'(r0) = 1 --
    no flare-out, d theta/d lambda = 0 and R_kk = 0 at r0."""
    mt = morris_thorne()
    r, b, r0 = mt["r"], mt["b"], mt["r0"]
    out = {}
    for name, bb in (("b=r0", r0), ("b=r0^2/r", r0 ** 2 / r), ("b=sqrt(r0 r)", sp.sqrt(r0 * r))):
        th = mt["theta"].subs(b, bb).doit()
        dth = sp.simplify(mt["dtheta"].subs(sp.Derivative(b, r), sp.diff(bb, r)).subs(b, bb).doit())
        Rkk = sp.simplify(mt["Rkk"].subs(sp.Derivative(b, r), sp.diff(bb, r)).subs(b, bb).doit())
        num = {r0: 1}
        out[name] = {"theta(r0)": float(th.subs(num).subs(r, 1)),
                     "theta(1.01 r0)": float(th.subs(num).subs(r, 1.01)),
                     "dtheta(r0)": float(dth.subs(num).subs(r, 1)),
                     "Rkk(r0)": float(Rkk.subs(num).subs(r, 1))}
    # CONTROL 1: Minkowski, ingoing congruence from a sphere of radius R: theta = -2/R < 0
    out["CONTROL Minkowski ingoing theta at R=1"] = float(-2 / 1.0)
    # CONTROL 2: b'(r0) = 1 (e.g. b = r near r0 -- not a throat): dtheta and R_kk vanish
    out["CONTROL bprime=1 dtheta(r0)"] = float(mt["dtheta_throat"].subs(mt["bp"], 1).subs(r0, 1))
    out["CONTROL bprime=1 Rkk(r0)"] = float(mt["Rkk_throat"].subs(mt["bp"], 1).subs(r0, 1))
    return out


def qnec_price(r0=R0, bprime=0.0):
    """nullinfo.py's requirement, imported as an expression and evaluated -- IF the QNEC applied at the throat (it is
    proven only on fixed backgrounds with no dynamical gravity, BFKLW p.4: carried here as the named hypothesis
    H-QNEC-OUT-OF-SCOPE)."""
    req = nullinfo.req
    sub = {nullinfo.G: G, nullinfo.hbar: HBAR, nullinfo.c: C, nullinfo.r0: r0, nullinfo.bp: bprime}
    req_nats = float(req.subs(sub))
    req_bits = req_nats / math.log(2)
    sheet_bits_per_m2 = 1.0 / (4 * (HBAR * G / C ** 3) * math.log(2))
    # identity: req = -(1-b')/r0^2 * (light-sheet density) -- symbolic, from nullinfo's own expressions
    ident = sp.simplify(req - (-(1 - nullinfo.bp) / nullinfo.r0 ** 2) * (1 / (4 * nullinfo.lP2))) == 0
    # H-CONST: S''/A constant over a null run of length r0 starting from S' = 0: |Delta S|/A = |S''/A| r0^2 / 2
    dS_per_area = abs(req_bits) * r0 ** 2 / 2
    dS_throat = dS_per_area * 4 * math.pi * r0 ** 2
    return {"Spp_over_A_bits_per_m4": req_bits, "light_sheet_bits_per_m2": sheet_bits_per_m2,
            "identity_req_eq_sheet_density_over_r0sq": ident,
            "ratio_|req| r0^2 / sheet": abs(req_bits) * r0 ** 2 / sheet_bits_per_m2,
            "dS_per_area_over_run_r0_bits_per_m2": dS_per_area, "fraction_of_sheet_cap": dS_per_area / sheet_bits_per_m2,
            "dS_over_throat_sphere_bits": dS_throat}


# =====================================================================================================================
# PART (iv) -- R-QUANTUM.  Hold a throat of radius r0 with negative energy from QEI-bounded states.
# =====================================================================================================================

def boosted_density():
    """For a radial observer at speed v: T_0'0' = gamma^2 (rho + v^2 p_r).  At v^2 = 1/2 (gamma v = 1) and rho = 0
    (b'(r0) = 0, so all the deficit is radial tension) it equals p_r = rho + p_r: the NEC combination itself, as an
    energy density that the T_00 duration bound speaks to.  Proper time to cross a radial extent r0 at gamma v = 1 is
    r0/c, which is achievable.hold_time(r0)."""
    rho, pr, v = sp.symbols('rho p_r v', real=True)
    gam2 = 1 / (1 - v ** 2)
    T00p = gam2 * (rho + v ** 2 * pr)
    at = sp.simplify(T00p.subs(v, 1 / sp.sqrt(2)).subs(rho, 0))
    gv = sp.simplify(sp.sqrt(gam2) * v).subs(v, 1 / sp.sqrt(2))
    return {"T00_at_v2_half_rho0": str(at), "equals_p_r": sp.simplify(at - pr) == 0, "gamma_v": str(sp.nsimplify(gv))}


def r_quantum(r0=R0, bprime=0.0):
    required = (1 - bprime) * C ** 4 / (8 * math.pi * G * r0 ** 2)      # |rho + p_r| in Pa (J m^-3)
    T = achievable.hold_time(r0)                                          # r0 / c
    allowed = achievable.duration_bound(T)                                # C hbar / (c^3 T^4), Pa
    T_star = (achievable.FEWSTER_C * HBAR / (C ** 3 * required)) ** 0.25  # how long the required density may last
    # where required == allowed at T = r0/c: r0^2 = 8 pi C hbar G / c^3 (computed from the constants, not from the
    # rounded L_PLANCK literal, which differs from sqrt(hbar G/c^3) by 1.5e-8 relative -- rounding)
    r_star = math.sqrt(8 * math.pi * achievable.FEWSTER_C * HBAR * G / C ** 3)
    return {"r0_m": r0, "required_Pa": required, "hold_time_s": T, "allowed_Pa": allowed,
            "fraction_covered": allowed / required, "T_star_s": T_star, "T_star_over_hold": T_star / T,
            "T_star_over_planck_time": T_star / (LP / C), "r_star_m": r_star, "r_star_over_lP": r_star / LP,
            "fewster_C": achievable.FEWSTER_C}


# =====================================================================================================================
# Grades
# =====================================================================================================================
OBS = ["O-BITS", "O-MAKE", "O-HOLD", "O-MATTER", "O-LOOP"]

GRADES = [
    {"hypothesis": "H-IT (spacetime from information), alone", "verdict": "PARTIAL",
     "removes": ["O-MAKE as Geroch/Tipler topology change: under ER=EPR the bridge is a property of an entangled state "
                 "and Maldacena-Susskind p.17 say non-trivial topologies 'should be allowed as possible quantum states'; "
                 "Geroch is a theorem about Lorentzian manifolds and does not reach that description"],
     "leaves": ["O-BITS (computed: Bob's state in Van Raamsdonk's eq.(1) state moves by <1e-14 over 900 choices of "
                "Alice; transit.BEATS_LIGHT False)",
                "O-MAKE as entanglement distribution: MS sec.3.2 p.16-17 -- no bridge 'without preexisting bridges'; "
                "a bridge is made by making pairs together, separating them (at <= c) and merging; LOCC cannot create "
                "entanglement (computed: local unitaries change S by <1e-13; a nonlocal control changes it)",
                "O-HOLD (MS footnote 1: non-traversability via the integrated NEC; Gao-Wald Thm 2: a bulk shortcut "
                "needs one of NEC/Borde-ANEC, null-generic, strong causality, compactness to fail)",
                "O-MATTER (no READ result on it)", "O-LOOP (no READ result on it; H-FRAME is A2's)"]},
    {"hypothesis": "H-ZERO (zero = ground state), alone", "verdict": "LEAVES-ALL",
     "removes": [],
     "leaves": OBS[:],
     "note": "relabels WEC violations away; the NEC combination changes by exactly 0 (zero.py; z3 UNSAT of the "
             "negation over every T, lambda and null k)"},
    {"hypothesis": "H-ZERO with H-IT (emergent gravity: Jacobson; Padmanabhan pp.6-7)", "verdict": "LEAVES-ALL",
     "removes": [],
     "leaves": OBS[:],
     "note": "removes the GR objection to H-ZERO itself: in Jacobson's derivation only T_kk enters, Lambda is an "
             "integration constant and a zero shift is invisible (computed). It removes none of the five: the throat "
             "needs R_kk < 0, i.e. T_kk < 0, which is exactly the part the free zero cannot touch."},
    {"hypothesis": "H-NULL (null is a containment where information lives)", "verdict": "LEAVES-ALL",
     "removes": [],
     "leaves": OBS[:],
     "note": "prices O-HOLD in bits (QNEC outside scope): S''/A <= -1.38e69 bits/m^4 at r0 = 1 m; over a null run r0 "
             "that is |dS|/A = 0.5 x the light-sheet cap. The containment (a light-sheet, theta <= 0) is exactly what "
             "the throat breaks: no light-sheet leaves the throat sphere (computed)."},
    {"hypothesis": "R-QUANTUM (QEI-bounded negative energy holds the throat)", "verdict": "LEAVES-ALL",
     "removes": [],
     "leaves": OBS[:],
     "note": "in the bound's proven scope (massless minimal scalar, Hadamard, flat: H_flat) the allowed density at "
             "the hold time covers ~2e-68 of the deficit at r0 = 1 m; OPEN for the nonminimally coupled scalar "
             "(no state-independent QEI, Fewster-Osterbrink, board NARROWED)"},
]


def report_data():
    S0, locc = locc_entropy_change()
    _, locc_ctrl = locc_entropy_change(nonlocal_control=True)
    fails, Is, mono = vr_eq2_check()
    mt = morris_thorne()
    return {
        "i_H-IT": {"no_signal_max_dev": it_no_signal(), "coupled_control_dev": it_coupled_control(),
                   "vr_eq2_fails": fails, "mutual_info_bits_by_beta": Is, "I_decreasing_in_beta": mono,
                   "S_cut_bits": S0, "locc_max_dS": locc, "nonlocal_control_dS": locc_ctrl,
                   "gao_wald": gao_wald_z3(),
                   "transit": {"BEATS_LIGHT": transit.BEATS_LIGHT, "TRAVERSAL_IS_REMOVED": transit.TRAVERSAL_IS_REMOVED,
                               "CARRIES_SUBSTANCE": transit.CARRIES_SUBSTANCE}},
        "ii_H-ZERO": {"zero_py_nec_change": str(zero.nec), "zero_py_wec_change": str(zero.wec),
                      "zero_py_sec_change": str(zero.sec),
                      "z3_nec_invariance": nec_shift_z3(), "z3_CONTROL_timelike": nec_shift_z3(control_timelike=True),
                      "jacobson": jacobson_null_equation(),
                      "cosmin_nu": cosmin.nu, "cosmin_checkA_Ic_minus_4pi": cosmin.Ic_of(cosmin.nu) - 4 * math.pi},
        "iii_H-NULL": {"Rkk_throat": str(mt["Rkk_throat"]), "dtheta_throat": str(mt["dtheta_throat"]),
                       "theta_throat": str(mt["theta_throat"]), "Rkk_equals_8pi(rho+p_r)_of_zero_py": mt["agree"],
                       "shapes": shape_checks(), "qnec_price": qnec_price()},
        "iv_R-QUANTUM": {"boost": boosted_density(), "r0=1m": r_quantum()},
        "grades": GRADES,
    }


def report():
    d = report_data()
    i, ii, iii, iv = d["i_H-IT"], d["ii_H-ZERO"], d["iii_H-NULL"], d["iv_R-QUANTUM"]
    print("DOCKET 68 / A4-geometry -- H-IT, H-ZERO, H-NULL, R-QUANTUM   (not seated)\n")
    print("(i) H-IT, Van Raamsdonk eq.(1) state, d = 4 (model H-QUDIT)")
    print(f"    Bob's state, max change over Alice's choices (unitaries + unread measurements): {i['no_signal_max_dev']:.2e}")
    print(f"    CONTROL with an interaction exp(-i g Z(x)X), g = 0.9:                           {i['coupled_control_dev']:.3f}")
    print(f"    eq.(2) I >= corr^2/(2|O|^2|O|^2): violations {i['vr_eq2_fails']} of 1000; "
          f"I(beta) bits = {[round(x, 4) for x in i['mutual_info_bits_by_beta']]} (decreasing: {i['I_decreasing_in_beta']})")
    print(f"    LOCC (local unitaries): max |dS| = {i['locc_max_dS']:.1e} bits of S = {i['S_cut_bits']:.4f}; "
          f"CONTROL nonlocal unitary from a product state: S reaches {i['nonlocal_control_dS']:.3f} bits")
    gw = i["gao_wald"]
    print(f"    Gao-Wald Thm 2 (logic): shortcut with every hypothesis -> {gw['shortcut_with_all_hyps']}; "
          f"with only the NEC broken -> {gw['shortcut_with_NEC_broken_only']}; drift {gw['encoding_drift']}/64")
    print(f"    transit.py: BEATS_LIGHT={i['transit']['BEATS_LIGHT']}  TRAVERSAL_IS_REMOVED={i['transit']['TRAVERSAL_IS_REMOVED']}")
    print("\n(ii) H-ZERO")
    print(f"    zero.py: NEC changes by {ii['zero_py_nec_change']}, WEC by {ii['zero_py_wec_change']}, SEC by {ii['zero_py_sec_change']}")
    print(f"    z3, all T, lambda, null k: negation {ii['z3_nec_invariance']['negation']} "
          f"(premise sat {ii['z3_nec_invariance']['vacuity_premise_sat']}, drift {ii['z3_nec_invariance']['drift_vs_numpy']:.1e}); "
          f"CONTROL timelike: {ii['z3_CONTROL_timelike']['negation']}")
    j = ii["jacobson"]
    print(f"    Jacobson eq.(6) contracted with null k drops Lambda and R: {j['null_contraction_drops_Lambda_and_R']}; "
          f"zero shift invisible: {j['zero_shift_invisible']}; CONTROL timelike keeps Lambda: {j['CONTROL_timelike_keeps_Lambda']}")
    print(f"    negative T_kk -> delta Q < 0 and delta A < 0 (eqs. 2, 5): {j['negative_Tkk_gives_dQ_dA_negative']}")
    print(f"    cosmin.py: nu = {ii['cosmin_nu']:.4g}; Ic(nu) - 4 pi = {ii['cosmin_checkA_Ic_minus_4pi']:.1e}")
    print("\n(iii) H-NULL, Morris-Thorne Phi = 0")
    print(f"    R_kk at the throat = {iii['Rkk_throat']}   (= 8 pi (rho + p_r) of zero.py: {iii['Rkk_equals_8pi(rho+p_r)_of_zero_py']})")
    print(f"    theta at throat = {iii['theta_throat']};  d theta/d lambda at throat = {iii['dtheta_throat']}")
    for k, v in iii["shapes"].items():
        print(f"      {k}: {v}")
    q = iii["qnec_price"]
    print(f"    QNEC (out of scope) at r0 = 1 m, b' = 0: S''/A <= {q['Spp_over_A_bits_per_m4']:.4e} bits/m^4; "
          f"light-sheet cap {q['light_sheet_bits_per_m2']:.4e} bits/m^2")
    print(f"    |dS|/A over a null run r0 = {q['dS_per_area_over_run_r0_bits_per_m2']:.4e} bits/m^2 "
          f"= {q['fraction_of_sheet_cap']:.3f} of the cap; over the throat sphere {q['dS_over_throat_sphere_bits']:.3e} bits")
    rq = iv["r0=1m"]
    print("\n(iv) R-QUANTUM")
    print(f"    boost v^2 = 1/2, rho = 0: T_0'0' = {iv['boost']['T00_at_v2_half_rho0']}, gamma v = {iv['boost']['gamma_v']}")
    print(f"    required |rho + p_r| = {rq['required_Pa']:.4e} Pa; hold time r0/c = {rq['hold_time_s']:.4e} s; "
          f"duration_bound = {rq['allowed_Pa']:.4e} Pa; fraction covered = {rq['fraction_covered']:.3e}")
    print(f"    the required density may last T* = {rq['T_star_s']:.3e} s = {rq['T_star_over_hold']:.2e} of the hold time "
          f"= {rq['T_star_over_planck_time']:.3e} Planck times")
    print(f"    bound stops refusing at r* = sqrt(8 pi C) l_P = {rq['r_star_over_lP']:.3f} l_P (dimensional, not evidence)")
    print("\nGRADES")
    for g in GRADES:
        print(f"  {g['verdict']:10s} {g['hypothesis']}")
        print(f"             removes: {g['removes'] or 'none of the five'}")
    return d


def selftest():
    ok = True
    n = [0, 0]

    def chk(label, cond, control=False):
        nonlocal ok
        n[0] += 1; n[1] += control
        ok &= bool(cond)
        print(f"  {'CONTROL ' if control else ''}{label:96s} {'ok' if cond else 'FAIL'}")

    print("geometry.py --selftest")
    # (i)
    chk("H-IT: Bob's state independent of Alice's choice in the eq.(1) state (< 1e-12)", it_no_signal() < 1e-12)
    chk("an interaction makes Bob's state depend on Alice's choice (> 1e-3) -- the detector is not blind",
        it_coupled_control() > 1e-3, control=True)
    fails, Is, mono = vr_eq2_check()
    chk("Van Raamsdonk eq.(2) holds on 1000 random operator pairs", fails == 0)
    chk("mutual information falls as beta rises (less entanglement -> pinch-off direction)", mono)
    f50, _, _ = vr_eq2_check(factor=50.0)
    chk("eq.(2) with its right side x50 is violated somewhere", f50 > 0, control=True)
    S0, dS = locc_entropy_change()
    chk("local unitaries leave the entanglement entropy unchanged (< 1e-10 bits)", dS < 1e-10)
    _, dSc = locc_entropy_change(nonlocal_control=True)
    chk("a nonlocal unitary creates entanglement from a product state (> 0.1 bit)", dSc > 0.1, control=True)
    gw = gao_wald_z3()
    chk("Gao-Wald: hypotheses jointly satisfiable (vacuity guard)", gw["vacuity_hyps_sat"])
    chk("Gao-Wald: a shortcut with every hypothesis is UNSAT", gw["shortcut_with_all_hyps"] == "unsat")
    chk("Gao-Wald: a shortcut with the NEC (and Borde-ANEC) broken is SAT -- not forbidden",
        gw["shortcut_with_NEC_broken_only"] == "sat", control=True)
    chk("Gao-Wald: dropping any single hypothesis re-admits a shortcut (no ranking among them)",
        all(r == "sat" for _, r in gw["each_single_drop_readmits"]))
    chk("Gao-Wald: encoding matches the implication on all 64 assignments", gw["encoding_drift"] == 0)
    chk("transit.py: BEATS_LIGHT is False, TRAVERSAL_IS_REMOVED is False",
        transit.BEATS_LIGHT is False and transit.TRAVERSAL_IS_REMOVED is False)
    # (ii)
    lam = zero.lam
    chk("zero.py: NEC change is 0, WEC change is -lambda, SEC change is +lambda",
        zero.nec == 0 and sp.simplify(zero.wec + lam) == 0 and sp.simplify(zero.sec - lam) == 0)
    zz = nec_shift_z3()
    chk("z3: null premise satisfiable (vacuity guard)", zz["vacuity_premise_sat"])
    chk("z3: k.(T + lam g).k != k.T.k is UNSAT for every T, lam, null k", zz["negation"] == "unsat")
    chk("z3 encoding agrees with numpy at 20 random points (< 1e-9)", zz["drift_vs_numpy"] < 1e-9)
    zc = nec_shift_z3(control_timelike=True)
    chk("the same claim for a unit timelike vector is SAT (the WEC density moves)", zc["negation"] == "sat", control=True)
    j = jacobson_null_equation()
    chk("Jacobson eq.(6) contracted with null k: Lambda and R drop out, R_kk = (2pi/hbar eta) T_kk",
        j["null_contraction_drops_Lambda_and_R"])
    chk("Jacobson: T_ab -> T_ab + lam g_ab invisible to the null equation", j["zero_shift_invisible"])
    chk("contracted with a timelike u, Lambda stays", j["CONTROL_timelike_keeps_Lambda"], control=True)
    chk("Jacobson eqs.(2),(5): T_kk < 0 gives delta Q < 0 and delta A < 0", j["negative_Tkk_gives_dQ_dA_negative"])
    chk("cosmin.py's check A round-trips: Ic(nu) = 4 pi (< 1e-9)", abs(cosmin.Ic_of(cosmin.nu) - 4 * math.pi) < 1e-9)
    # (iii)
    mt = morris_thorne()
    r0, bp = mt["r0"], mt["bp"]
    chk("MT: R_kk = 8 pi (rho + p_r) of zero.py, for arbitrary b(r)", mt["agree"])
    chk("MT: R_kk at the throat = (b' - 1)/r0^2", sp.simplify(mt["Rkk_throat"] - (bp - 1) / r0 ** 2) == 0)
    chk("MT: theta = 0 at the throat", mt["theta_throat"] == 0)
    chk("MT: d theta/d lambda at the throat = (1 - b')/r0^2 = -R_kk (Raychaudhuri, theta = sigma = 0)",
        sp.simplify(mt["dtheta_throat"] - (1 - bp) / r0 ** 2) == 0)
    sh = shape_checks()
    flare = [sh[k] for k in ("b=r0", "b=r0^2/r", "b=sqrt(r0 r)")]
    chk("three flare-out shapes: theta(r0) = 0, theta > 0 just outside, R_kk(r0) < 0",
        all(abs(s["theta(r0)"]) < 1e-12 and s["theta(1.01 r0)"] > 0 and s["Rkk(r0)"] < 0 for s in flare))
    chk("Minkowski ingoing sphere: theta < 0, a light-sheet exists", sh["CONTROL Minkowski ingoing theta at R=1"] < 0,
        control=True)
    chk("b'(r0) = 1: no flare-out, d theta/d lambda = 0 and R_kk = 0 at r0",
        sh["CONTROL bprime=1 dtheta(r0)"] == 0 and sh["CONTROL bprime=1 Rkk(r0)"] == 0, control=True)
    q = qnec_price()
    chk("nullinfo.py: req = -(1 - b')/r0^2 x 1/(4 l_P^2), symbolically", q["identity_req_eq_sheet_density_over_r0sq"])
    chk("nullinfo.py at r0 = 1 m, b' = 0: S''/A = -1.3807e69 bits/m^4 (charter's figure, 4 s.f.)",
        abs(q["Spp_over_A_bits_per_m4"] / -1.3807e69 - 1) < 1e-4)
    chk("|S''/A| r0^2 equals the light-sheet density exactly (ratio 1)", abs(q["ratio_|req| r0^2 / sheet"] - 1) < 1e-12)
    q2 = qnec_price(bprime=1.0)
    chk("b' = 1 (no flare-out): the QNEC price is 0", q2["Spp_over_A_bits_per_m4"] == 0, control=True)
    # (iv)
    bd = boosted_density()
    chk("boost v^2 = 1/2 with rho = 0: T_0'0' = p_r = rho + p_r, gamma v = 1", bd["equals_p_r"] and bd["gamma_v"] == "1")
    chk("achievable.FEWSTER_C = 3.17 to 3 s.f. (1208.5399 eq.(4) prints 'C ~ 3.17')",
        round(achievable.FEWSTER_C, 2) == 3.17)
    rq = r_quantum()
    chk("required |rho + p_r| at r0 = 1 m = c^4/(8 pi G) = 4.815e42 Pa (4 s.f.)", abs(rq["required_Pa"] / 4.8154e42 - 1) < 1e-4)
    chk("hold time = r0/c = 3.3356e-9 s", abs(rq["hold_time_s"] / 3.33564e-9 - 1) < 1e-5)
    chk("fraction of the deficit the QEI allows at the hold time < 1e-60", rq["fraction_covered"] < 1e-60)
    chk("T* is between the Planck time and the hold time", 1 < rq["T_star_over_planck_time"] and rq["T_star_over_hold"] < 1)
    rs = r_quantum(r0=rq["r_star_m"])
    chk("at r0 = r* the fraction is 1 (round trip, 1e-9)", abs(rs["fraction_covered"] - 1) < 1e-9)
    rh = r_quantum(r0=0.5 * rq["r_star_m"])
    chk("at r0 = r*/2 the bound does NOT refuse (fraction > 1) -- the instrument can say 'covered'",
        rh["fraction_covered"] > 1, control=True)
    print(f"\n{n[0]} checks, {n[1]} of them controls: {'ALL PASS' if ok else 'FAILURES'}")
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(report_data(), indent=1, default=str))
    else:
        report()
