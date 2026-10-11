"""calibrate2.py -- item 221: delta_X by continuation.  The observed state is the default-guess SCF at delta = 0 (its
energy is delta-independent in this gauge while its shell stays full); the aufbau state is found at a large delta and
followed DOWN in delta from its own density, so it is never asked to exist where it is not a stable SCF solution.  The
gap(delta) = E_auf - E_obs is tabulated on the way down, and each law's delta is where gap = -target, by linear
interpolation between bracketing points; where the aufbau state collapses before the crossing, by first-order
extrapolation from the last two rows whose shell count is unmixed, and the result says which.  usage: python3 calibrate2.py EL l spin_obs[,spin_auf] dE_exp_eV N_obs N_auf
[basis pseudo|none xc]  -> JSON"""
import sys, json, time
import numpy as np
from pyscf import gto, dft
import law
HA = 27.211386245988
el, l, spins, dexp, nobs, nauf = sys.argv[1], int(sys.argv[2]), sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
basis, pseudo, xc = sys.argv[7:10] if len(sys.argv) > 9 else ("def2-tzvp", None, "pbe0")
pseudo = None if pseudo in (None, "none") else pseudo
sign = 1.0 if l == 2 and el != "Lr" else -1.0
spin_obs, spin_auf = (int(x) for x in (spins.split(",") * 2)[:2])     # '1' or '6,4' (observed, aufbau)
spin = spin_obs

def mk(spin):
    if pseudo: return gto.M(atom="%s 0 0 0" % el, basis=basis, pseudo=pseudo, spin=spin, verbose=0)
    return gto.M(atom="%s 0 0 0" % el, basis=basis, ecp=basis, spin=spin, verbose=0)

def scf(delta, dm0=None, spin=None):
    mol = mk(spin_obs if spin is None else spin); mf = dft.UKS(mol); mf.xc = xc; mf.max_cycle = 300
    if delta: law.apply_law(mf, [(0, l, delta, nobs)])
    e = mf.kernel(dm0) if dm0 is not None else mf.kernel()
    if not mf.converged:
        mf2 = dft.UKS(mol); mf2.xc = xc; mf2.max_cycle = 500; mf2.damp = 0.5; mf2.diis_start_cycle = 30
        if delta: law.apply_law(mf2, [(0, l, delta, nobs)])
        e = mf2.kernel(mf.make_rdm1()); mf = mf2
    return float(e), law.lowdin_shell_pop(mf, 0, l), mf.make_rdm1(), bool(mf.converged)

t = time.time()
Eo, No, dmo, co = scf(0.0, spin=spin_obs)
grid = [sign * x for x in (0.30, 0.27, 0.24, 0.21, 0.18, 0.15, 0.12, 0.10, 0.08, 0.06, 0.04, 0.02, 0.0)]
tab, dm, started = [], None, False
for d in grid:
    e, n, dm1, c = scf(d, dm, spin=spin_auf)
    if abs(n - nauf) > 0.5:                                  # not (or no longer) the aufbau configuration
        if started: break                                   # collapsed on the way down: stop the descent
        dm = None; continue                                 # not yet reached from the default guess: next delta
    started = True
    eo, no, _, _ = scf(d, dmo, spin=spin_obs)                               # the observed state at the same delta
    flag = abs(no - No) > 0.5
    if flag: eo = Eo                                         # it left its configuration: use the gauge-fixed delta=0 value
    tab.append((d, (e - eo) * HA, n, no, c and not flag)); dm = dm1
out = dict(el=el, l=l, spin_obs=spin_obs, spin_auf=spin_auf, basis=basis, pseudo=pseudo, xc=xc, E_obs0=Eo, N_obs0=round(No, 4), dE_exp_eV=dexp,
           table=[(round(d * HA, 4), round(g, 4), round(n, 4), round(no, 4), c) for d, g, n, no, c in tab], laws={})
clean = [r for r in tab if abs(r[2] - nauf) < 0.01]           # aufbau rows with an unmixed shell count
for name, target in (("switch", 0.0), ("min", 0.05), ("mirror", dexp)):
    hit, how = None, None
    for (d1, g1, *_), (d2, g2, *_) in zip(tab, tab[1:]):    # descending delta: gap rises
        if (g1 + target) * (g2 + target) <= 0:
            hit, how = d1 + (d2 - d1) * (-target - g1) / (g2 - g1), "BRACKETED"; break
    if hit is None and len(clean) >= 2:                     # first order from the last two clean rows (E_auf linear in delta)
        (d1, g1, *_), (d2, g2, *_) = clean[-2], clean[-1]
        hit, how = d2 + (d2 - d1) * (-target - g2) / (g2 - g1), "EXTRAPOLATED (first order, last two clean rows)"
    out["laws"][name] = round(hit * HA, 4) if hit is not None else None
    out["laws"][name + "_how"] = how
out["collapsed_below_eV"] = round(tab[-1][0] * HA, 4)
out["sec"] = int(time.time() - t)
print("RESULT " + json.dumps(out), flush=True)
