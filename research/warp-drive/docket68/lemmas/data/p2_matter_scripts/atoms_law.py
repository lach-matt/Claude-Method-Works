"""atoms_law.py -- the free-atom block of run_mol2.py on its own (same code path, same guesses), so the molecule runs
that predate the E_atoms field get their atom energies banked.  usage: python3 atoms_law.py EL delta_eV -> JSON"""
import sys, json
from pyscf import gto, dft
import law
HA = 27.211386245988
el, d = sys.argv[1], float(sys.argv[2])
out = []
if el == "H":
    mol = gto.M(atom="H 0 0 0", basis="def2-tzvp", spin=1, verbose=0)
    mf = dft.UKS(mol); mf.xc = "pbe0"; e = mf.kernel(); out.append((float(e), 0.0, bool(mf.converged)))
else:
    for d0 in (0.0, 0.25):
        mol = gto.M(atom="%s 0 0 0" % el, basis="def2-tzvp", ecp="def2-tzvp", spin=1, verbose=0)
        mf = dft.UKS(mol); mf.xc = "pbe0"; mf.max_cycle = 300
        if d0: law.apply_law(mf, [(0, 2, d0, 10.0)])
        mf.kernel(); dm = mf.make_rdm1()
        mf2 = dft.UKS(mol); mf2.xc = "pbe0"; mf2.max_cycle = 300
        if d: law.apply_law(mf2, [(0, 2, d / HA, 10.0)])
        e = mf2.kernel(dm)
        out.append((float(e), round(law.lowdin_shell_pop(mf2, 0, 2), 4), bool(mf2.converged)))
    out.sort()
print("RESULT " + json.dumps(dict(el=el, delta_eV=d, states=out)), flush=True)
