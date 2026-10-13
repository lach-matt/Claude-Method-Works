import numpy as np, interior_fw as IF
st = dict(file="fw_bt1_24_24.npy", Ns=24, Nx=24)
for s0 in (-0.002, -0.005, -0.01, -0.02):
    for order in (2, 3, 4):
        I = IF.Interior(16, 1.0, st); Y0 = I.initial(s0, order)
        print("s0=%g order=%d  max|phi| at start %.2e" % (s0, order, np.nanmax(np.abs(IF.phi_at(I, s0, Y0)))), flush=True)
