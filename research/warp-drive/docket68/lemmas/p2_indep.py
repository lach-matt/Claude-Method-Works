#!/usr/bin/env python3
"""p2_indep.py -- item 509: whatever matter sits at position 2, it reconstructs only position 1's matter.

M, 509: "position 2's matter is only relevant in the sense that its matter reconstructs the same matter from position 1.
No matter what matter sits at position 2, it always only reconstructs the matter from position 1. - prove this".  On the
record's rulings: 146 (no tolerance; the encoding in what every universe shares), 148 (position 2's matter rearranges to
accommodate the README; after, position 2's laws govern), 240 (built from position 2's bulk as an exact copy under its
laws), 284-285 (the copy takes its room by displacing what is there), 386 (only information travels).  Labels: READ,
computed (exact unless marked), deduced, M's.

The claim, made exact.  The README r (classical, N bits; reader, encode_read) fixes the copy's state sigma_r: discrete
labels (exactcopy X3: element, configuration, quantum numbers), so sigma_r has definite conserved charges, as every
state of matter does (superselection).  Position 2's matter is in any state rho of the room and of the bulk around it.
Reconstruction is a physical process Lambda_r on that matter, run by r alone.  The claim: Lambda_r(rho) restricted to
the room is sigma_r for every rho -- position 2's matter enters as material, never as content.

  I0 (M's) 509, verbatim.
  I1 (computed, exact) No other outcome is possible.  A linear map that returns sigma for every density matrix is the
     replacement map sigma Tr( . ): density matrices span all matrices, and the coefficients are solved exactly (d = 4,
     rational arithmetic), giving Phi(E_ij) = delta_ij sigma.  So a reconstruction exact for every rho (146: no
     tolerance) cannot carry anything of rho into the copy.  The process of I2, fed maximally entangled with a
     reference, has Choi matrix sigma_r (x) I/8: it is that map.
  I2 (computed) It is physical, and it conserves what physics conserves.  Room A, a cold dump D (the displaced matter's
     destination, 284-285) and a reservoir R of the conserved charge, the process a product of swaps chosen by r alone:
     the room ends in |r><r| for pure, mixed and reference-entangled rho alike (to machine precision); the unitary
     commutes with total charge and with the total energy of identical local Hamiltonians.
  I3 (computed) Where position 2's matter goes (Braunstein and Pati's no-hiding theorem, PRL 98, 080502 (2007), READ by
     its statement): with a reference purifying rho, I(ref : copy) = 0 and I(ref : dump) = 2 S(rho).  All that position
     2's matter was is in what was displaced; none of it is in the copy.
  I4 (computed) "The same matter" is literal.  Identical particles carry no identity (the symmetrization postulate):
     the two-fermion and two-boson states built with position 2's particle in one mode and position 1's in the other are
     the same state up to sign, and every symmetric observable reads the same on both (100 random ones).  A copper atom
     from position 2's stock is position 1's copper atom, in every observable.
  I5 (computed, AME2020 Table I READ through tools/isotopes.py) The kind of matter enters only the energy balance.  The
     record's copper piece (Cu-63) built from hydrogen, helium, carbon, oxygen (with hydrogen) or iron (with hydrogen):
     the same Cu-63, with Q released 524.8, 123.8, 87.4, 160.7 and 56.0 MeV per atom.  Baryon number is conserved, so
     position 2's matter must hold at least the copy's baryons -- necessary for any process whatever; given that, its
     composition does not reach the copy.
  I6 (computed, molar entropies READ, NIST at 298.15 K) The kind of matter enters the cost too, never the copy: clearing
     a 1 cm^3 room costs at least T S, 1394 J if it held copper, 1154 J for water, 2.4 J for air (Landauer); the copy is
     the same in all three.
  What this does not do: position 2's laws still govern the copy after the instant (148, 240; rearrange R1-R2) -- that
  is a law, not prior matter, and it is not what 509 asks.

python3 p2_indep.py [--selftest | --mutants]
"""
import sys, os, itertools, importlib.util
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
MUT = set()
rng = np.random.default_rng(509)


def words():
    s = open(RULINGS).read()
    return "No matter what matter sits at position 2, it always only reconstructs the matter from position 1. - prove this" in s


def i1():
    """the linear maps with constant output on every density matrix, solved exactly"""
    d = 4
    E = lambda i, j: sp.Matrix(d, d, lambda a, b: 1 if (a, b) == (i, j) else 0)
    dens = []                                    # an exact spanning set of density matrices
    for i in range(d):
        dens.append(E(i, i))
    for i in range(d):
        for j in range(i + 1, d):
            dens.append((E(i, i) + E(j, j) + E(i, j) + E(j, i))/2)
            dens.append((E(i, i) + E(j, j) - sp.I*E(i, j) + sp.I*E(j, i))/2)
    C = sp.Matrix([[X[i, j] for i in range(d) for j in range(d)] for X in dens])   # rows: density matrices in the E basis
    Ci = C.inv()                                  # E_ij = sum_k Ci[k, ij] X_k  ->  Phi(E_ij) = (sum_k Ci[k, ij]) sigma
    coef = [sp.nsimplify(sp.simplify(sum(Ci[i*d + j, k] for k in range(d*d)))) for i in range(d) for j in range(d)]
    want = [1 if i == j else 0 for i in range(d) for j in range(d)]
    return dict(exact=coef == want, rank=C.rank())


def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


def op_on(n, k, o):
    return kron(*[o if q == k else np.eye(2) for q in range(n)])


def swap_q(n, a, b):
    """the swap of qubits a and b in an n-qubit register"""
    D = 2**n
    U = np.zeros((D, D))
    for x in range(D):
        bits = [(x >> (n - 1 - q)) & 1 for q in range(n)]
        bits[a], bits[b] = bits[b], bits[a]
        y = sum(bt << (n - 1 - q) for q, bt in enumerate(bits))
        U[y, x] = 1
    return U


def i2_i3():
    """room A = qubits 0..2, dump D = 3..5 (cold |000>), reservoir R = 6..8 (charge supply |111>), reference 9..11"""
    n, m = 3, 12
    A, Dm, Rr, Ref = range(0, 3), range(3, 6), range(6, 9), range(9, 12)
    r = (1, 0, 1)                                           # a README's labels for the room
    U = np.eye(2**m)
    if "no_dump" not in MUT:
        for a, d_ in zip(A, Dm):
            U = swap_q(m, a, d_) @ U                        # the room's matter displaced into the dump (284-285)
    for k, (a, rr) in enumerate(zip(A, Rr)):
        if r[k]:
            if "charge_violating" in MUT:
                U = op_on(m, a, np.array([[0, 1], [1, 0]])) @ U   # a bare flip: charge made from nothing
            else:
                U = swap_q(m, a, rr) @ U                    # a charge moved in from the reservoir
    num = np.array([[0, 0], [0, 1.0]])
    Q = sum(op_on(m, q, num) for q in range(9))             # total charge of room, dump and reservoir
    om = 1.0
    Hl = sum(om*op_on(m, q, num) for q in range(9))         # identical local Hamiltonians
    comm_Q = np.abs(U @ Q - Q @ U).max(); comm_H = np.abs(U @ Hl - Hl @ U).max()
    target = np.zeros((8, 8)); idx = int("".join(map(str, r)), 2); target[idx, idx] = 1
    errs, Iref_copy, Iref_dump, S2 = [], [], [], []
    for trial in range(6):
        # a random pure state of room + reference (entangled), the dump cold, the reservoir full
        psi_AR = rng.normal(size=64) + 1j*rng.normal(size=64)
        psi_AR /= np.linalg.norm(psi_AR)
        psi_AR = psi_AR.reshape(8, 8)                       # (room, reference)
        if "keep_trace" in MUT:
            pass
        dump0 = np.zeros(8); dump0[0] = 1
        res0 = np.zeros(8); res0[7] = 1
        full = np.einsum("ar,d,s->adsr", psi_AR, dump0, res0).reshape(-1)
        out = (U @ full).reshape(8, 8, 8, 8)               # (A, D, R, Ref)
        rhoA = np.einsum("adsr,bdsr->ab", out, out.conj())
        if "keep_trace" in MUT:
            rho_in = np.einsum("ar,br->ab", psi_AR, psi_AR.conj())
            rhoA = 0.95*rhoA + 0.05*rho_in
        errs.append(np.abs(rhoA - target).max())
        def S(rho):
            w = np.linalg.eigvalsh(rho); w = w[w > 1e-14]
            return float(-(w*np.log2(w)).sum())
        rho_Ref = np.einsum("adsr,adst->rt", out, out.conj())
        rho_A_Ref = np.einsum("adsr,bdst->arbt", out, out.conj()).reshape(64, 64)
        rho_D = np.einsum("adsr,aesr->de", out, out.conj())
        rho_D_Ref = np.einsum("adsr,aest->dret", out, out.conj()).reshape(64, 64)
        rho_Ain = np.einsum("ar,br->ab", psi_AR, psi_AR.conj())
        Iref_copy.append(S(rhoA) + S(rho_Ref) - S(rho_A_Ref))
        Iref_dump.append(S(rho_D) + S(rho_Ref) - S(rho_D_Ref))
        S2.append(2*S(rho_Ain))
    # the process's Choi matrix: the room fed maximally entangled with the reference; it must be sigma_r (x) I/8
    psi_AR = np.eye(8)/np.sqrt(8)
    dump0 = np.zeros(8); dump0[0] = 1
    res0 = np.zeros(8); res0[7] = 1
    out = (U @ np.einsum("ar,d,s->adsr", psi_AR, dump0, res0).reshape(-1)).reshape(8, 8, 8, 8)
    J = np.einsum("adsr,bdst->arbt", out, out.conj()).reshape(64, 64)
    if "keep_trace" in MUT:
        J = 0.95*J + 0.05*np.einsum("ar,bt->arbt", psi_AR, psi_AR.conj()).reshape(64, 64)
    choi_err = np.abs(J - np.kron(target, np.eye(8)/8)).max()
    return dict(err=max(errs), comm_Q=comm_Q, comm_H=comm_H, I_copy=max(Iref_copy),
                I_dump_gap=max(abs(a - b) for a, b in zip(Iref_dump, S2)), S2=min(S2), choi_err=choi_err)


def i4():
    """two identical particles in modes a, b: 'which came from position 2' is not a degree of freedom"""
    d = 3                                                    # single-particle space (modes)
    a = np.zeros(d); a[0] = 1
    b = np.zeros(d); b[1] = 1
    P = np.zeros((d*d, d*d))
    for i in range(d):
        for j in range(d):
            P[j*d + i, i*d + j] = 1                          # exchange of particle labels
    out = {}
    for name, sgn in (("fermion", -1), ("boson", 1)):
        x = np.kron(a, b); y = np.kron(b, a)
        st12 = (x + sgn*y)/np.sqrt(2)                        # position 2's particle in a, position 1's in b
        st21 = (y + sgn*x)/np.sqrt(2)                        # the other way round
        if "distinguishable" in MUT:
            st12, st21 = x, y
        same = min(np.linalg.norm(st12 - st21), np.linalg.norm(st12 + st21))
        dev = 0.0
        for _ in range(100):
            h = rng.normal(size=(d, d)) + 1j*rng.normal(size=(d, d)); h = h + h.conj().T
            V = rng.normal(size=(d*d, d*d)) + 1j*rng.normal(size=(d*d, d*d)); V = V + V.conj().T; V = (V + P @ V @ P)/2
            O = np.kron(h, np.eye(d)) + np.kron(np.eye(d), h) + V          # a symmetric observable
            dev = max(dev, abs(st12.conj() @ O @ st12 - st21.conj() @ O @ st21))
        out[name] = dict(same=same, dev=dev)
    return out


def _isotopes():
    spec = importlib.util.spec_from_file_location("isotopes_tool", os.path.join(REPO, "tools", "isotopes.py"))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return {(z, a_): dk for (z, nn, a_, sym, dk, unc, q) in mod.read()}


def i5():
    """Cu-63 from five kinds of matter: atomic mass excesses (keV); A balanced, the charge by beta processes whose
    positrons annihilate with the surplus electrons, so Q = sum Delta(inputs) - Delta(Cu-63)"""
    D = _isotopes()
    H1, He4, C12, O16, Fe56, Cu63 = D[(1, 1)], D[(2, 4)], D[(6, 12)], D[(8, 16)], D[(26, 56)], D[(29, 63)]
    recipes = {"hydrogen": [(H1, 63)], "helium": [(He4, 15), (H1, 3)], "carbon": [(C12, 5), (H1, 3)],
               "oxygen": [(O16, 3), (H1, 15)], "iron": [(Fe56, 1), (H1, 7)]}
    A_of = {H1: 1, He4: 4, C12: 12, O16: 16, Fe56: 56}
    out = {}
    for k, rec in recipes.items():
        A = sum(A_of[dk]*cnt for dk, cnt in rec)
        out[k] = dict(A=A, Q_MeV=(sum(dk*cnt for dk, cnt in rec) - Cu63)/1000)
    return out


def i6():
    """the least work to clear a 1 cm^3 room at 298.15 K, by what it held: W >= T S (S = n S_m; molar entropies READ)"""
    T, R = 298.15, 8.314462618
    Sm = {"copper": 33.15, "water": 69.95, "air": 0.7808*191.61 + 0.2095*205.15 + 0.0097*154.85}
    n = {"copper": 8.96/63.546, "water": 0.99705/18.015, "air": 101325e-6/(R*T)}
    return {k: T*n[k]*Sm[k] for k in Sm}


def compute():
    return dict(words=words(), i1=i1(), i23=i2_i3(), i4=i4(), i5=i5(), i6=i6())


def checks(o):
    c = {}
    c["I0 words of 509"] = o["words"]
    a = o["i1"]
    c["I1 a map constant on every state is the replacement map (exact); the process's Choi is sigma_r x I"] = (
        a["exact"] and a["rank"] == 16 and o["i23"]["choi_err"] < 1e-12)
    a = o["i23"]
    c["I2 the room ends in the README's state for every rho; charge and energy conserved"] = (
        a["err"] < 1e-12 and a["comm_Q"] < 1e-12 and a["comm_H"] < 1e-12)
    c["I3 no-hiding: nothing of rho in the copy, all of it in what was displaced"] = (
        a["I_copy"] < 1e-9 and a["I_dump_gap"] < 1e-9 and a["S2"] > 0.5)
    a = o["i4"]
    c["I4 identical particles: position 2's atom is position 1's in every observable"] = all(
        v["same"] < 1e-12 and v["dev"] < 1e-10 for v in a.values())
    a = o["i5"]
    c["I5 the same Cu-63 from five kinds of matter; only Q differs"] = (
        all(v["A"] == 63 for v in a.values()) and abs(a["hydrogen"]["Q_MeV"] - 524.8) < 0.1
        and all(abs(a[k]["Q_MeV"] - q) < 0.1 for k, q in (("helium", 123.8), ("carbon", 87.4), ("oxygen", 160.7), ("iron", 56.0))))
    a = o["i6"]
    c["I6 the cost depends on what the room held, the copy does not"] = (
        abs(a["copper"] - 1394) < 1 and abs(a["water"] - 1154) < 1 and abs(a["air"] - 2.365) < 0.005)
    return c


def report(o=None):
    o = o or compute()
    for k, v in checks(o).items():
        print("%-80s %s" % (k, "PASS" if v else "FAIL"))
    a = o["i23"]
    print("  I2/I3: room error %.1e; [U,Q] %.1e, [U,H] %.1e; I(ref:copy) %.1e; I(ref:dump) - 2S(rho) %.1e" % (
        a["err"], a["comm_Q"], a["comm_H"], a["I_copy"], a["I_dump_gap"]))
    print("  I5 Q released per Cu-63 atom (MeV): " + ", ".join("%s %.1f" % (k, v["Q_MeV"]) for k, v in o["i5"].items()))
    print("  I6 least work to clear 1 cm^3 (J): " + ", ".join("%s %.4g" % (k, v) for k, v in o["i6"].items()))
    return o


MUTANTS = {"keep_trace": "a reconstruction that keeps 5 % of position 2's prior state (I1, I2, I3)",
           "no_dump": "a reset with nothing to displace into: a unitary on the room alone (I2, I3)",
           "charge_violating": "the README's charges made from nothing instead of moved in (I2)",
           "distinguishable": "atoms treated as carrying an identity (I4)"}


def selftest():
    o = compute(); c = checks(o); report(o)
    print("%s: %d/%d" % (os.path.basename(__file__), sum(c.values()), len(c)))
    return all(c.values())


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            c = checks(compute()); failed = [k for k, v in c.items() if not v]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-17s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
