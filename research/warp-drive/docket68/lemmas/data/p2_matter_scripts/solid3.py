"""solid3.py -- item 221 step 3 (solids): an fcc (Cu, Ag, Au) or nonmagnetic bcc (Cr, Mo) metal, one atom per primitive cell, under our law or position 2's law,
scanned over lattice constants in one process (each point starts from the previous point's density).  PBE,
GTH-PBE pseudopotential, GTH-DZVP-MOLOPT-SR basis, Fermi smearing, k-point symmetry (irreducible wedge), multigrid
integration.  The law is the Lowdin projector on the atom's d AOs, built per irreducible k from S(k):
V(k) = delta S(k)^1/2 Pi S(k)^1/2, and the reported E carries the gauge, E' = E + delta (N_d - N_obs) per atom, the same
gauge law.py gives the free atom.  usage: python3 solid3.py EL delta_eV nk sigma_Ha ke_cutoff_Ha a1,a2,... [mesh]
(a fixed FFT mesh across a scan keeps E(a) smooth: the ke_cutoff-derived mesh steps with the cell and puts ~1 meV
steps into the curve)  -> one RESULT line per a"""
import sys, json, time, os
import numpy as np, scipy.linalg
from pyscf.pbc import gto as pgto, dft as pdft, scf as pscf
from pyscf.pbc.dft import multigrid
HA = 27.211386245988
LAT = {"fcc": [[0, .5, .5], [.5, 0, .5], [.5, .5, 0]], "bcc": [[-.5, .5, .5], [.5, -.5, .5], [.5, .5, -.5]]}
NOBS = {"Cu": 10.0, "Ag": 10.0, "Au": 10.0, "Cr": 5.0, "Mo": 5.0}
STRUCT = {"Cu": "fcc", "Ag": "fcc", "Au": "fcc", "Cr": "bcc", "Mo": "bcc"}
el, delta_eV, nk, sigma, ke = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
alist = [float(x) for x in sys.argv[6].split(",")]
MESH = [int(sys.argv[7])] * 3 if len(sys.argv) > 7 else None
delta = delta_eV / HA
dm_prev = None
for a in alist:
    t = time.time()
    cell = pgto.Cell(); cell.atom = "%s 0 0 0" % el
    cell.a = np.array(LAT[STRUCT[el]]) * a
    cell.basis = "gth-dzvp-molopt-sr"; cell.pseudo = "gth-pbe"; cell.verbose = 0; cell.ke_cutoff = ke
    if MESH: cell.mesh = MESH
    cell.space_group_symmetry = True; cell.symmorphic = False; cell.build()
    kpts = cell.make_kpts([nk] * 3, space_group_symmetry=True, time_reversal_symmetry=True)
    kmf = pdft.KRKS(cell, kpts); kmf.xc = "pbe"; kmf.conv_tol = 1e-8; kmf.max_cycle = 100
    kmf = pscf.addons.smearing_(kmf, sigma=sigma, method="fermi")
    kmf._numint = multigrid.MultiGridNumInt(cell)
    kibz, w = kpts.kpts_ibz, kpts.weights_ibz
    didx = [i for i, (ia, e, nl, m) in enumerate(cell.ao_labels(fmt=False)) if nl.endswith("d")]
    Sh = [scipy.linalg.sqrtm(s) for s in cell.pbc_intor("int1e_ovlp", kpts=kibz)]
    Pi = np.zeros((cell.nao, cell.nao)); Pi[didx, didx] = 1.0
    if delta:
        if os.environ.get("LAW_KIND") == "mulliken":            # Mulliken count: delta (S Pi + Pi S)/2 per k (robustness test)
            Sk = cell.pbc_intor("int1e_ovlp", kpts=kibz)
            V = np.array([0.5 * delta * (s @ Pi + Pi @ s) for s in Sk])
        else:
            V = np.array([delta * (sh @ Pi @ sh) for sh in Sh])
        h0 = kmf.get_hcore
        kmf.get_hcore = lambda *args, _h0=h0, _V=V, **kw: np.asarray(_h0(*args, **kw)) + _V
    ncyc = [0]
    kmf.callback = lambda env: ncyc.__setitem__(0, ncyc[0] + 1)
    e = kmf.kernel(dm_prev) if dm_prev is not None else kmf.kernel()
    dm = kmf.make_rdm1(); dm_prev = dm
    Nd = float(np.real(sum(w[k] * np.trace((Sh[k] @ dm[k] @ Sh[k])[np.ix_(didx, didx)]) for k in range(len(kibz)))))
    mu = float(kmf.get_fermi())
    num = den = 0.0
    for k in range(len(kibz)):
        C = Sh[k] @ kmf.mo_coeff[k]
        wd = (np.abs(C[didx, :]) ** 2).sum(axis=0); occ = np.asarray(kmf.mo_occ[k]) / 2.0
        num += w[k] * float(np.sum(wd * occ * kmf.mo_energy[k])); den += w[k] * float(np.sum(wd * occ))
    out = dict(el=el, delta_eV=delta_eV, nk=nk, nk_ibz=len(kibz), law_kind=os.environ.get("LAW_KIND", "lowdin"), sigma=sigma, ke=ke, mesh_fixed=bool(MESH), mesh=[int(x) for x in cell.mesh], a=a, V_bohr3=float(cell.vol),
               E=float(e) - delta * NOBS[el], struct=STRUCT[el], N_obs=NOBS[el], E_raw=float(e), conv=bool(kmf.converged), cycles=ncyc[0], Nd=round(Nd, 4),
               mu=mu, eps_d_minus_EF_eV=round((num / den - mu) * HA, 4), sec=int(time.time() - t))
    print("RESULT " + json.dumps(out), flush=True)
