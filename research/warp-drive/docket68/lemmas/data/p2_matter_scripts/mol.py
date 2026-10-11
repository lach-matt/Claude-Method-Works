"""mol.py -- item 221 step 2 (molecules): a diatomic AB under our law and under position 2's law (law.py), UKS PBE0 /
def2-TZVP (+def2 ECP).  At each bond length every listed spin state is solved from two starting guesses and the lowest
converged energy kept; a quadratic through the three lowest points gives r_e and the force constant; omega_e from it;
D_e against the free atoms in their ground state under the same law.  usage: python3 mol.py A B r0 spins law_json"""
import sys, json, time
import numpy as np
from pyscf import gto, dft
import law
HA, BOHR = 27.211386245988, 0.529177210903
AMU = {"H": 1.00782503, "Cu": 62.9295989, "Ag": 106.905091, "Au": 196.966570, "Pd": 105.903484, "Pt": 194.964794,
       "Cr": 51.940505, "Mo": 97.905404, "O": 15.9949146, "La": 138.906356, "Cl": 34.968853, "F": 18.99840316}

def shifts_for(mol, laws):
    out = []
    for ia in range(mol.natm):
        el = mol.atom_symbol(ia)
        if el in laws:
            l, delta, nobs = laws[el]
            out.append((ia, l, delta, nobs))
    return out

ATOM_DM = {}          # el -> list of (spin, (dma, dmb)) free-atom states under the law, filled by the caller

def sad(mol, flip_second=False, choice=None):
    """superposition of law-atom densities; choice[el] picks which stored state; flip_second swaps alpha/beta on atom 1"""
    nao = mol.nao
    dma = np.zeros((nao, nao)); dmb = np.zeros((nao, nao))
    off = mol.aoslice_by_atom()
    for ia in range(mol.natm):
        el = mol.atom_symbol(ia)
        st = ATOM_DM[el][(choice or {}).get(el, 0)][1]
        a0, a1 = off[ia][2], off[ia][3]
        a, b = st
        if flip_second and ia == 1: a, b = b, a
        dma[a0:a1, a0:a1] = a; dmb[a0:a1, a0:a1] = b
    return np.array([dma, dmb])

def solve(atom, spin, laws, charge=0, guesses=("minao", "atom", "sad", "sadflip")):
    best = None
    for g in guesses:
        try:
            mol = gto.M(atom=atom, basis="def2-tzvp", ecp="def2-tzvp", spin=spin, charge=charge, verbose=0)
            mf = dft.UKS(mol); mf.xc = "pbe0"; mf.max_cycle = 200
            dm0 = None
            if g in ("sad", "sadflip"):
                if mol.natm < 2 or any(mol.atom_symbol(i) not in ATOM_DM for i in range(mol.natm)): continue
                dm0 = sad(mol, flip_second=(g == "sadflip"))
                if abs((np.trace(dm0[0] @ mol.intor("int1e_ovlp")) - np.trace(dm0[1] @ mol.intor("int1e_ovlp"))) - spin) > 0.5:
                    continue
            else:
                mf.init_guess = g
            sh = shifts_for(mol, laws)
            if sh: law.apply_law(mf, sh)
            e = mf.kernel(dm0) if dm0 is not None else mf.kernel()
            if mf.converged and (best is None or e < best[0]):
                best = (float(e), mf)
        except Exception:
            pass
    return best

def curve(A, B, r0, spins, laws, dr=0.06, npts=7):
    rs = [r0 + dr * (i - npts // 2) for i in range(npts)]
    pts = []
    for r in rs:
        bests = {}
        for s in spins:
            b = solve("%s 0 0 0; %s 0 0 %.6f" % (A, B, r), s, laws)
            if b: bests[s] = b[0]
        if bests:
            s = min(bests, key=bests.get)
            pts.append((r, bests[s], s, bests))
    return pts

def fit(pts, A, B):
    """quartic through every point of the curve; r_e at the root of dE/dr nearest the lowest point, k = d2E/dr2 there"""
    pts = sorted(pts)
    r = np.array([p[0] for p in pts]); e = np.array([p[1] for p in pts])
    c = np.polyfit(r, e, min(4, len(r) - 1))
    d1, d2 = np.polyder(c), np.polyder(c, 2)
    r0 = r[int(np.argmin(e))]
    roots = [x.real for x in np.roots(d1) if abs(x.imag) < 1e-9 and np.polyval(d2, x.real) > 0]
    re = min(roots, key=lambda x: abs(x - r0))
    emin = float(np.polyval(c, re))
    k = float(np.polyval(d2, re)) * BOHR ** 2               # Ha/A^2 -> Ha/bohr^2
    mu = AMU[A] * AMU[B] / (AMU[A] + AMU[B]) * 1822.888486
    we = np.sqrt(k / mu) * 219474.6313705                   # cm^-1
    return float(re), emin, float(we)

if __name__ == "__main__":
    A, B, r0 = sys.argv[1], sys.argv[2], float(sys.argv[3])
    spins = [int(x) for x in sys.argv[4].split(",")]
    laws = {k: tuple(v) for k, v in json.loads(sys.argv[5]).items()}
    atom_spins = json.loads(sys.argv[6])                    # {"Cu":[1], "H":[1]}
    t = time.time()
    pts = curve(A, B, r0, spins, laws)
    re, emin, we = fit(pts, A, B)
    Eat = {}
    for el in (A, B):
        bs = [solve("%s 0 0 0" % el, s, laws) for s in atom_spins[el]]
        bs = [b for b in bs if b]
        Eat[el] = min(b[0] for b in bs)
    De = (Eat[A] + Eat[B] - emin) if A != B else (2 * Eat[A] - emin)
    o = dict(mol=A + B, laws={k: list(v) for k, v in laws.items()}, re=round(re, 4), we=round(we, 1), De_eV=round(De * HA, 4),
             spin_at_min=min(pts, key=lambda p: p[1])[2], pts=[(round(p[0], 4), p[1], p[2]) for p in pts],
             E_atoms=Eat, sec=int(time.time() - t))
    print("RESULT " + json.dumps(o), flush=True)
