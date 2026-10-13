import numpy as np, solver_fw as SF, sys
prev = (SF.setup(12, 12), np.load("fw_bt1_12_12.npy"))
for N in (16, 20, 24):
    G = SF.setup(N, N); U, nr = SF.newton(G, SF.regrid(prev[0], prev[1], G), 1.0)
    print("bt=1 N=%d |R|=%.1e phi=%.2e R4/ell=%.7f" % (N, nr, SF.phimax(G, U, 1.0), SF.R4(G, U, 1.0)), flush=True)
    np.save("fw_bt1_%d_%d.npy" % (N, N), U); prev = (G, U)
G = prev[0]; U = prev[1]
for b in (1.5, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20):
    U, nr = SF.newton(G, U, b)
    print("bt=%g N=%d |R|=%.1e phi=%.2e R4/ell=%.5f" % (b, G["Ns"], nr, SF.phimax(G, U, b), SF.R4(G, U, b)), flush=True)
    np.save("fw_bt%g_%d_%d.npy" % (b, G["Ns"], G["Nx"]), U)
