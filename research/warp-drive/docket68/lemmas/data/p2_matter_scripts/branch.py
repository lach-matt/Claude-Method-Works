"""branch.py -- one spin state of a diatomic under a law along a list of bond lengths (mol.solve's four guesses, the free atoms under the law seeding the two sad guesses as in run_mol2.py), to
follow a branch the lowest-state curve leaves.  usage: python3 branch.py A B spin LAWJSON r1,r2,...  -> RESULT per r"""
import sys, json
import law, mol as M
from pyscf import gto, dft
HA = 27.211386245988
A, B, spin, dl = sys.argv[1], sys.argv[2], int(sys.argv[3]), json.loads(sys.argv[4])
laws = {el: (2, dl[el] / HA, 10.0) for el in (A, B) if el in dl}
for el in {A, B}:                                   # free atoms under the law, as run_mol2.py, for the sad guesses
    if el in ("Cu", "Ag", "Au"):
        st = []
        for d0 in (0.0, 0.25):
            mol = gto.M(atom="%s 0 0 0" % el, basis="def2-tzvp", ecp="def2-tzvp", spin=1, verbose=0)
            mf = dft.UKS(mol); mf.xc = "pbe0"; mf.max_cycle = 300
            if d0: law.apply_law(mf, [(0, 2, d0, 10.0)])
            mf.kernel(); dm = mf.make_rdm1()
            mf2 = dft.UKS(mol); mf2.xc = "pbe0"; mf2.max_cycle = 300
            if el in laws: law.apply_law(mf2, [(0,) + laws[el]])
            e = mf2.kernel(dm); st.append((float(e), mf2.make_rdm1()))
        st.sort(key=lambda x: x[0]); M.ATOM_DM[el] = [(1, (x[1][0], x[1][1])) for x in st]
    else:
        mol = gto.M(atom="%s 0 0 0" % el, basis="def2-tzvp", spin=1, verbose=0)
        mf = dft.UKS(mol); mf.xc = "pbe0"; mf.kernel(); dm = mf.make_rdm1(); M.ATOM_DM[el] = [(1, (dm[0], dm[1]))]
for r in [float(x) for x in sys.argv[5].split(",")]:
    b = M.solve("%s 0 0 0; %s 0 0 %.6f" % (A, B, r), spin, laws)
    nd = round(law.lowdin_shell_pop(b[1], 0, 2), 4) if b else None
    print("RESULT " + json.dumps(dict(mol=A + B, spin=spin, laws=dl, r=r, E=b[0] if b else None, Nd=nd)), flush=True)
