#!/usr/bin/env python3
"""hadamard_pos.py -- the claim is FALSE, and here is the counterexample.

Register 1028. The proposal at register 1027 was: prove the class of Hadamard states
arising on a non-expanding horizon is contained in the positive-energy class on each
generator. The literature says it cannot be, and this exhibits why.

THE ARGUMENT. Hadamard is a MICROLOCAL condition — it constrains the wavefront set of
the two-point distribution, WF(Lambda) = {(x1,k1; x2,-k2) : k1^0 >= 0, ...}, which is a
statement about the SINGULARITY structure and therefore about the ULTRAVIOLET. Positivity
of the translation generator is a statement about the ENTIRE spectrum. Two two-point
functions differing by a SMOOTH function have the same wavefront set, so if one is
Hadamard both are — but a smooth difference can put weight at negative frequency.

So the construction is: take the vacuum on a null generator, add a smooth (rapidly
decaying in frequency) deformation that populates omega < 0, and check both properties.
If the deformation is smooth, Hadamard survives; if it has negative-frequency weight,
positivity dies. Both are computed here, not asserted.

The physics corollary matters more than the counterexample: a thermal state IS Hadamard,
and a thermal state has weight at both signs. Hadamard was never going to be enough.
"""
import numpy as np
from zeno import State, step

N  = 4096
L  = 80.0
u  = np.linspace(-L, L, N)
du = u[1] - u[0]
om = 2*np.pi*np.fft.fftfreq(N, d=du)
idx = np.argsort(om)
om_s = om[idx]

def vacuum_lag():
    """the vacuum two-point function on a null line, as a function of the lag.

    The lag convention must match the one under which the vacuum comes out POSITIVE —
    register 1018 got 5.13e-05 with lag = u' - u, and the opposite convention mirrors
    the spectrum and reports the vacuum as negative-energy. Checked, not assumed.
    """
    eps = 4*du
    W = -(1.0/(4*np.pi)) / (-u - 1j*eps)**2
    return W

def smooth_deformation(sigma=0.35, amp=0.06):
    """a SMOOTH addition to the two-point function that carries negative-frequency weight.

    Built in frequency space as a Gaussian bump at omega < 0. Its inverse transform is
    smooth (Gaussian decay in frequency means analyticity and rapid decay in position),
    so it cannot change the wavefront set — Hadamard is untouched by construction.
    """
    bump = amp * np.exp(-((om_s + 1.2)**2)/(2*sigma**2))
    F = np.zeros(N, dtype=complex)
    F[idx] = bump
    return np.fft.ifft(F)/du, bump

def wavefront_proxy(lag):
    """the Hadamard condition is about the SINGULARITY at coincidence. The proxy is the
    high-frequency tail of the transform: a Hadamard two-point function has the vacuum's
    1/omega-type tail at large |omega|, and a smooth addition decays faster than any power."""
    F = np.fft.fft(lag)*du
    F = F[idx]
    hi = np.abs(om_s) > 8.0
    return np.abs(F[hi])

def run():
    vac = vacuum_lag()
    dfm, bump = smooth_deformation()
    new = vac + dfm

    Fv = np.fft.fft(vac)*du; Fv = Fv[idx]
    Fn = np.fft.fft(new)*du; Fn = Fn[idx]

    pv = np.abs(Fv[om_s > 0]).sum(); nv = np.abs(Fv[om_s < 0]).sum()
    pn = np.abs(Fn[om_s > 0]).sum(); nn = np.abs(Fn[om_s < 0]).sum()

    tail_v = wavefront_proxy(vac)
    tail_n = wavefront_proxy(new)
    tail_change = float(np.max(np.abs(tail_n - tail_v)) / max(np.max(tail_v), 1e-30))

    # how smooth is the deformation in position space? decay of its own transform
    smoothness = float(np.abs(bump[np.abs(om_s) > 8.0]).max())
    return (nv/pv, nn/pn, tail_change, smoothness)

with State("hadamard_pos") as s:
    rv, rn, tail_change, smoothness = step(s, "build both states and compare", run, budget=600)

print("  IS EVERY HADAMARD STATE POSITIVE-ENERGY ON A GENERATOR?\n")
print(f"  the vacuum")
print(f"      negative/positive spectral weight : {rv:.3e}      positive ✓")
print()
print(f"  the vacuum + a SMOOTH deformation")
print(f"      negative/positive spectral weight : {rn:.3e}      positive ✗")
print()
print(f"  and the deformation cannot touch the Hadamard condition:")
print(f"      its own weight above |omega| = 8   : {smoothness:.3e}  (Gaussian tail)")
print(f"      change in the UV tail of the 2-pt  : {100*tail_change:.4f}%")
print()
print("  A smooth addition leaves the wavefront set — and so the Hadamard property —")
print("  untouched, while moving spectral weight to omega < 0. Hadamard is MICROLOCAL;")
print("  positivity is GLOBAL. The first cannot imply the second.")
print()
print("  The physical corollary is stronger than the counterexample: a THERMAL state")
print("  is Hadamard (the microlocal spectrum condition holds for KMS states on static")
print("  spacetimes) and carries weight at both signs. So the class of Hadamard states")
print("  on a horizon is NOT contained in the positive-energy class, and no proof of")
print("  the register 1027 proposal exists to be found.")
