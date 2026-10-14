"""band.py -- item 221 step 3b: at a metal's computed equilibrium lattice constant under one law, the d band's place
against the Fermi level (top and bottom of the occupied d band, Lowdin-d weight > 0.5, over the irreducible k mesh;
the top sets the interband absorption edge E_F - E_d,top that colours Cu and Au), and whether a spin-polarised
solution with a moment exists (UKS from a d-polarised start, a common Fermi level, the moment left free).
Same method as solid3.py.  usage: python3 band.py EL delta_eV a_angstrom nk mesh [spin]
(a denser k mesh and half the smearing of the scans: the Fermi level on the scans' 4x4x4 mesh moves by up to 1.4 eV
between neighbouring lattice constants, so band positions against it are read here, not there)  -> JSON"""
import sys, json, time
import numpy as np, scipy.linalg
from pyscf.pbc import gto as pgto, dft as pdft, scf as pscf
from pyscf.pbc.dft import multigrid
HA = 27.211386245988
LAT = {"fcc": [[0, .5, .5], [.5, 0, .5], [.5, .5, 0]], "bcc": [[-.5, .5, .5], [.5, -.5, .5], [.5, .5, -.5]]}
NOBS = {"Cu": 10.0, "Ag": 10.0, "Au": 10.0, "Cr": 5.0}
STRUCT = {"Cu": "fcc", "Ag": "fcc", "Au": "fcc", "Cr": "bcc"}
el, delta_eV, a, nk, mesh = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
spin = len(sys.argv) > 6 and sys.argv[6] == "spin"
SIGMA = 0.005
delta = delta_eV / HA
t = time.time()
cell = pgto.Cell(); cell.atom = "%s 0 0 0" % el; cell.a = np.array(LAT[STRUCT[el]]) * a
cell.basis = "gth-dzvp-molopt-sr"; cell.pseudo = "gth-pbe"; cell.verbose = 0; cell.ke_cutoff = 160; cell.mesh = [mesh] * 3
cell.space_group_symmetry = True; cell.symmorphic = False; cell.build()
kpts = cell.make_kpts([nk] * 3, space_group_symmetry=True, time_reversal_symmetry=True)
kibz, w = kpts.kpts_ibz, kpts.weights_ibz
didx = [i for i, (ia, e, nl, m) in enumerate(cell.ao_labels(fmt=False)) if nl.endswith("d")]
Sh = [scipy.linalg.sqrtm(s) for s in cell.pbc_intor("int1e_ovlp", kpts=kibz)]
Pi = np.zeros((cell.nao, cell.nao)); Pi[didx, didx] = 1.0
V = np.array([delta * (sh @ Pi @ sh) for sh in Sh])

def make(kind):
    kmf = (pdft.KUKS if kind == "u" else pdft.KRKS)(cell, kpts); kmf.xc = "pbe"; kmf.conv_tol = 1e-8; kmf.max_cycle = 150
    kmf = pscf.addons.smearing_(kmf, sigma=SIGMA, method="fermi")
    kmf._numint = multigrid.MultiGridNumInt(cell)
    if delta:
        h0 = kmf.get_hcore
        kmf.get_hcore = lambda *args, _h0=h0, **kw: np.asarray(_h0(*args, **kw)) + V
    return kmf

r = make("r"); er = r.kernel(); mu = float(r.get_fermi())
bands = []                                                  # (k weight, eps - mu in eV, d weight) for -12 .. +5 eV
for k in range(len(kibz)):
    C = Sh[k] @ r.mo_coeff[k]
    wd = (np.abs(C[didx, :]) ** 2).sum(axis=0)
    for e, x in zip(r.mo_energy[k], wd):
        x_ev = (e - mu) * HA
        if -12.0 < x_ev < 5.0:
            bands.append((round(float(w[k]), 6), round(float(x_ev), 4), round(float(x), 4)))
dd = [b[1] for b in bands if b[2] > 0.5]                    # the d manifold: Lowdin-d weight above one half, inside the window
out = dict(el=el, delta_eV=delta_eV, a=a, nk=nk, nk_ibz=len(kibz), sigma=SIGMA, mesh=mesh, E_R=float(er) - delta * NOBS[el], conv_R=bool(r.converged), mu=mu,
           d_top_minus_EF_eV=max(dd), d_bottom_minus_EF_eV=min(dd), d_width_eV=round(max(dd) - min(dd), 4), bands=bands)
if spin:
    u = make("u")
    dm = r.make_rdm1()
    dma = 0.5 * np.array(dm); dmb = 0.5 * np.array(dm)
    for k in range(len(kibz)):                                  # +-10 % on the d-d block: a ferromagnetic start
        blk = np.ix_(didx, didx)
        dma[k][blk] *= 1.10; dmb[k][blk] *= 0.90
    eu = u.kernel(np.array([dma, dmb]))
    dmu = u.make_rdm1()
    Na = float(np.real(sum(w[k] * np.trace((Sh[k] @ dmu[0][k] @ Sh[k])) for k in range(len(kibz)))))
    Nb = float(np.real(sum(w[k] * np.trace((Sh[k] @ dmu[1][k] @ Sh[k])) for k in range(len(kibz)))))
    out.update(E_U=float(eu) - delta * NOBS[el], conv_U=bool(u.converged), moment_muB=round(Na - Nb, 4),
               dE_U_minus_R_meV=round((float(eu) - float(er)) * HA * 1000, 3))
out["sec"] = int(time.time() - t)
print("RESULT " + json.dumps(out), flush=True)
