import numpy as np, glob, re, solver_fw as SF
rows = []
for fpath in glob.glob("fw_bt*_*_*.npy"):
    m = re.match(r"fw_bt([\d.]+)_(\d+)_(\d+)\.npy", fpath); b, Ns, Nx = float(m.group(1)), int(m.group(2)), int(m.group(3))
    G = SF.setup(Ns, Nx); U = np.load(fpath)
    R, _ = SF.residual_and_jac(G, U, b, False)
    rows.append((b, Ns, np.abs(R).max(), SF.phimax(G, U, b), SF.R4(G, U, b)))
for r in sorted(rows):
    print("bt=%5g N=%2d |R|=%.1e phi_max=%.2e R4/ell=%.5f" % r)
