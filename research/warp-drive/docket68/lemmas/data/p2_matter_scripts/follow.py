"""follow.py -- follow one electronic branch of a diatomic under a law by continuation: the start point takes the lowest
converged state over mol.solve's four guesses at r_start, then each step in r starts from the previous point's density,
outward and inward, so the branch is tracked through regions where a fresh guess falls onto another state.
usage: python3 follow.py A B spin LAWJSON r_start step n_out n_in  -> one RESULT per point (r, E, N_d of atom 0)"""
import sys, json
import numpy as np
from pyscf import gto, dft
import law, mol as M
HA = 27.211386245988
A, B, spin, dl = sys.argv[1], sys.argv[2], int(sys.argv[3]), json.loads(sys.argv[4])
r0, step, nout, nin = float(sys.argv[5]), float(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8])
laws = {el: (2, dl[el] / HA, 10.0) for el in (A, B) if el in dl}
for el in {A, B}:                                   # free atoms under the law for the sad guesses, as run_mol2.py
    if el in ("Cu", "Ag", "Au"):
        st = []
        for d0 in (0.0, 0.25):
            mol = gto.M(atom="%s 0 0 0" % el, basis="def2-tzvp", ecp="def2-tzvp", spin=1, verbose=0)
            mf = dft.UKS(mol); mf.xc = "pbe0"; mf.max_cycle = 300
            if d0: law.apply_law(mf, [(0, 2, d0, 10.0)])
            mf.kernel(); dm = mf.make_rdm1()
            mf2 = dft.UKS(mol); mf2.xc = "pbe0"; mf2.max_cycle = 300
            if el in laws: law.apply_law(mf2, [(0,) + laws[el]])
            mf2.kernel(dm); st.append((float(mf2.e_tot), mf2.make_rdm1()))
        st.sort(key=lambda x: x[0]); M.ATOM_DM[el] = [(1, (x[1][0], x[1][1])) for x in st]
    else:
        mol = gto.M(atom="%s 0 0 0" % el, basis="def2-tzvp", spin=1, verbose=0)
        mf = dft.UKS(mol); mf.xc = "pbe0"; mf.kernel(); dm = mf.make_rdm1(); M.ATOM_DM[el] = [(1, (dm[0], dm[1]))]

def run(r, dm0):
    mol = gto.M(atom="%s 0 0 0; %s 0 0 %.6f" % (A, B, r), basis="def2-tzvp", ecp="def2-tzvp", spin=spin, verbose=0)
    mf = dft.UKS(mol); mf.xc = "pbe0"; mf.max_cycle = 300
    sh = M.shifts_for(mol, laws)
    if sh: law.apply_law(mf, sh)
    e = mf.kernel(dm0)
    if not mf.converged:
        mf2 = dft.UKS(mol); mf2.xc = "pbe0"; mf2.max_cycle = 400; mf2.damp = 0.5
        if sh: law.apply_law(mf2, sh)
        e = mf2.kernel(mf.make_rdm1()); mf = mf2
    return float(e), mf

b = M.solve("%s 0 0 0; %s 0 0 %.6f" % (A, B, r0), spin, laws)
start = b[1].make_rdm1()
def emit(r, e, mf):
    nd = round(law.lowdin_shell_pop(mf, 0, 2), 4) if mf.mol.atom_symbol(0) in ("Cu", "Ag", "Au") else None
    print("RESULT " + json.dumps(dict(mol=A + B, spin=spin, laws=dl, r=round(r, 4), E=e, Nd=nd, conv=bool(mf.converged))), flush=True)
emit(r0, b[0], b[1])
for sgn, n in ((1, nout), (-1, nin)):
    dm = start
    for i in range(1, n + 1):
        r = r0 + sgn * step * i
        e, mf = run(r, dm)
        emit(r, e, mf); dm = mf.make_rdm1()
