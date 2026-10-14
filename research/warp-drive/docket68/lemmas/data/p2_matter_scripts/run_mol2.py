"""run_mol2.py -- one diatomic under one law (item 221 step 2).  Free atoms first (both configurations, under the law);
then a coarse curve (7 points, 0.06 A), then a fine curve (7 points, 0.02 A) about the coarse minimum.  Every point keeps
the lowest converged state over the listed spins and four guesses, with its Lowdin d count, so a change of branch along
the curve is visible; the quartic through the fine points gives r_e and omega_e, and its largest residual is reported
(a kink means a branch change inside the fit window).  usage: python3 run_mol2.py A B r0 spins LAWNAME 'json {el: delta_eV}'"""
import sys, json, time
import numpy as np
from pyscf import gto, dft
import law, mol as M
HA = 27.211386245988
A, B, r0 = sys.argv[1], sys.argv[2], float(sys.argv[3])
spins, name, dl = [int(x) for x in sys.argv[4].split(",")], sys.argv[5], json.loads(sys.argv[6])
METALS = {"Cu", "Ag", "Au"}
laws = {el: (2, dl[el] / HA, 10.0) for el in (A, B) if el in METALS and dl.get(el)}
t = time.time()
atoms = {}
for el in {A, B}:
    if el in METALS:
        st = []
        for d0 in (0.0, 0.25):
            mol = gto.M(atom="%s 0 0 0" % el, basis="def2-tzvp", ecp="def2-tzvp", spin=1, verbose=0)
            mf = dft.UKS(mol); mf.xc = "pbe0"; mf.max_cycle = 300
            if d0: law.apply_law(mf, [(0, 2, d0, 10.0)])
            mf.kernel(); dm = mf.make_rdm1()
            mf2 = dft.UKS(mol); mf2.xc = "pbe0"; mf2.max_cycle = 300
            if el in laws: law.apply_law(mf2, [(0,) + laws[el]])
            e = mf2.kernel(dm)
            st.append((float(e), law.lowdin_shell_pop(mf2, 0, 2), mf2.make_rdm1(), mf2.converged))
        st.sort(key=lambda x: x[0]); atoms[el] = st
        M.ATOM_DM[el] = [(1, (x[2][0], x[2][1])) for x in st]
    else:
        mol = gto.M(atom="%s 0 0 0" % el, basis="def2-tzvp", spin=1, verbose=0)
        mf = dft.UKS(mol); mf.xc = "pbe0"; e = mf.kernel()
        atoms[el] = [(float(e), 0.0, mf.make_rdm1(), mf.converged)]
        M.ATOM_DM[el] = [(1, (mf.make_rdm1()[0], mf.make_rdm1()[1]))]

def point(r):
    best = None
    for s in spins:
        b = M.solve("%s 0 0 0; %s 0 0 %.6f" % (A, B, r), s, laws)
        if b and (best is None or b[0] < best[0]): best = (b[0], s, b[1])
    if best is None: return None
    nd = [round(law.lowdin_shell_pop(best[2], i, 2), 4) if best[2].mol.atom_symbol(i) in METALS else None for i in range(2)]
    return (round(r, 4), best[0], best[1], nd)

coarse = [p for p in (point(r0 + 0.06 * (i - 3)) for i in range(7)) if p]
rc = min(coarse, key=lambda p: p[1])[0]
fine = [p for p in (point(rc + 0.02 * (i - 3)) for i in range(7)) if p]
re, emin, we = M.fit([(p[0], p[1], p[2]) for p in fine], A, B)
c = np.polyfit([p[0] for p in fine], [p[1] for p in fine], 4)
resid = max(abs(p[1] - np.polyval(c, p[0])) for p in fine) * HA * 1000
Eat = {el: atoms[el][0][0] for el in atoms}
De = (Eat[A] + Eat[B] - emin) if A != B else (2 * Eat[A] - emin)
o = dict(mol=A + B, law=name, delta_eV={k: round(v[1] * HA, 4) for k, v in laws.items()}, re=round(re, 4), we=round(we, 1),
         De_eV=round(De * HA, 4), D0_eV=round(De * HA - we / 2 / 8065.543937, 4), fit_resid_meV=round(resid, 3),
         spin_at_min=min(fine, key=lambda p: p[1])[2], Nd_fine=[p[3] for p in fine],
         atom_ground_Nd={el: round(atoms[el][0][1], 4) for el in atoms},
         atom_gap_eV={el: round((atoms[el][1][0] - atoms[el][0][0]) * HA, 4) for el in atoms if len(atoms[el]) > 1},
         E_atoms=Eat, atom_states={el: [(x[0], round(x[1], 4), bool(x[3])) for x in atoms[el]] for el in atoms},
         coarse=coarse, fine=fine, sec=int(time.time() - t))
print("RESULT " + json.dumps(o), flush=True)
