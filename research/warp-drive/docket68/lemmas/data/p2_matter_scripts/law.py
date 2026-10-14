"""law.py -- position 2's one different law, as the board states it (item 221 reading (b), RECONSTRUCTED): on every
atom of an exception element X, the electrons of X's d (or f) shell carry an extra energy delta_X each, counted by the
Lowdin (symmetric-orthogonalised) population of X's d (or f) atomic orbitals.  E' = E + sum_X delta_X (N_X - N_X,obs);
the constant N_X,obs (the free atom's observed shell count) only fixes the gauge.  Everything else is our law."""
import numpy as np
from pyscf import gto, scf, dft, lib
from pyscf.scf import addons
import scipy.linalg

def shell_projector(mol, atom_index, l):
    S = mol.intor_symmetric("int1e_ovlp")
    Sh = scipy.linalg.sqrtm(S).real
    labels = mol.ao_labels(fmt=False)
    L = "spdfghi"[l]
    idx = [i for i, (ia, el, nl, m) in enumerate(labels) if ia == atom_index and nl.endswith(L)]
    Pi = np.zeros(S.shape); Pi[idx, idx] = 1.0
    return Sh @ Pi @ Sh, Sh, idx

def apply_law(mf, shifts):
    """shifts: list of (atom_index, l, delta_Ha, N_obs).  Adds sum delta*S^1/2 Pi S^1/2 to hcore; energy_nuc absorbs -delta*N_obs.
    With LAW_KIND=mulliken in the environment the shell count is Mulliken's, N = Tr(Pi D S), and the operator is
    delta (S Pi + Pi S)/2 -- the same count as Lowdin's on a free atom (same-centre shells of different l are orthogonal),
    so the calibration carries over unchanged; it differs only where atoms overlap (a robustness test of the projector)."""
    import os
    mol = mf.mol
    V = 0.0; const = 0.0
    for ia, l, delta, nobs in shifts:
        if os.environ.get("LAW_KIND") == "mulliken":
            _, _, idx = shell_projector(mol, ia, l)
            S = mol.intor_symmetric("int1e_ovlp")
            Pi = np.zeros(S.shape); Pi[idx, idx] = 1.0
            P = 0.5 * (S @ Pi + Pi @ S)
        else:
            P, _, _ = shell_projector(mol, ia, l)
        V = V + delta * P; const -= delta * nobs
    h0 = mf.get_hcore
    mf.get_hcore = lambda *a, **k: h0(*a, **k) + V
    e0 = mf.energy_nuc
    mf.energy_nuc = lambda *a, **k: e0(*a, **k) + const
    return mf

def lowdin_shell_pop(mf, atom_index, l, dm=None):
    mol = mf.mol
    dm = mf.make_rdm1() if dm is None else dm
    if isinstance(dm, (tuple, list)) or (hasattr(dm, "ndim") and dm.ndim == 3):
        dm = dm[0] + dm[1]
    P, Sh, idx = shell_projector(mol, atom_index, l)
    D = Sh @ dm @ Sh
    return float(np.trace(D[np.ix_(idx, idx)]))
