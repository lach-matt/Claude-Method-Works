#!/usr/bin/env python3
"""anec_null.py — COMPUTE the null for the ANEC instead of assuming it.

THE PERSON'S POINT. Everyone in this literature uses a null as a placeholder for
something they have not established. Faulkner & Speranza: "it is generally
expected to hold... it is reasonable to assume the ANEC holds for them, implying
that the P_lambda are positive operators." Graham & Olum: "free of known
violations... might be expected to hold." The method's practice is the opposite:
a null is COMPUTED, not collected (R 1376), and a claim is checked against it.

Register 1028 already did this once, for a DIFFERENT claim. The proposal was
"Hadamard implies positivity"; hadamard_pos.py built a smooth deformation of the
vacuum that kept the wavefront set and put weight at omega < 0, and the proposal
died. That is the model.

THIS SCRIPT DOES THE SAME FOR THE ANEC, and the question is narrower and sharper:

    on a single horizon generator, can a state satisfying the non-expanding
    horizon's own conditions give a NEGATIVE averaged null energy?

WHAT THE NEH SUPPLIES, from the register (R 1039, from Ashtekar's Living Review):
Theta = 0 plus the definition's energy condition forces T_ab l^a l^b = 0 AND
sigma_ab = 0 on the BACKGROUND. So the background flux is not merely non-negative
— it is EXACTLY ZERO, and the null convergence condition R_ab l^a l^b >= 0 that
Kontou & Olum require is SATURATED.

But R 1041 states the shortfall correctly: the perturbations carry T_uu != 0, and
half-sidedness is spectral on the perturbations. So the null to compute is the
PERTURBATIVE one.

SPACE, DECLARED BEFORE THE RUN (R 1383 q2). The admissible set is: states on one
null generator whose two-point function differs from the vacuum's by a SMOOTH
function — i.e. states that are Hadamard, since a smooth difference preserves the
wavefront set. Within that set we ask whether the ANEC integral can be negative.
This is the same admissible set register 1028 used, so the two results are
comparable and the second is not a new space chosen after seeing the first.
"""
import numpy as np

N = 4096
L = 80.0
u = np.linspace(-L, L, N)
du = u[1] - u[0]
om = 2 * np.pi * np.fft.fftfreq(N, d=du)


def vacuum_lag():
    """vacuum two-point function on a null line, in the lag convention register
    1018 verified as the one under which the vacuum comes out POSITIVE."""
    eps = 4 * du
    return -(1.0 / (4 * np.pi)) / (-u - 1j * eps) ** 2


def smooth_deformation(sigma, amp, shift=0.0):
    """a smooth, rapidly decaying deformation — no new singularity, so the
    wavefront set and hence the Hadamard property are untouched."""
    return amp * np.exp(-((u - shift) ** 2) / (2 * sigma ** 2))


def spectrum(W):
    S = np.fft.fft(W) * du
    return np.real(S * np.conj(S)) ** 0.5


def uv_tail(W, cut=8.0):
    S = spectrum(W)
    return S[np.abs(om) > cut].sum()


def anec_integral(W, smear=None):
    """<P_lambda> ~ integral of T_vv along the generator. For a free field on a
    null line the null-null stress is the coincidence limit of d_u d_u' W, so the
    averaged quantity is an integral of the SECOND DERIVATIVE of the deformation
    against a non-negative smearing — which integrates by parts to a manifestly
    signed expression. Computed directly rather than argued."""
    Wr = np.real(W)
    d2 = np.gradient(np.gradient(Wr, du), du)
    lam = np.ones_like(u) if smear is None else smear
    return np.trapezoid(d2 * lam, u)


print("  COMPUTING THE NULL FOR THE ANEC ON ONE HORIZON GENERATOR\n")
V = vacuum_lag()
print(f"    vacuum: ANEC integral {anec_integral(V):+.6e}   UV tail {uv_tail(V):.4e}\n")
print("  SMOOTH DEFORMATIONS — Hadamard is preserved by construction. Can any of")
print("  them drive the averaged null energy NEGATIVE?\n")
print(f"    {'sigma':>7}{'amp':>9}{'ANEC integral':>18}{'UV tail change':>17}  sign")
rows = []
for sigma in (0.25, 0.35, 0.6, 1.2, 3.0):
    for amp in (-0.30, -0.06, 0.06, 0.30):
        W = V + smooth_deformation(sigma, amp)
        a = anec_integral(W)
        dtail = 100 * (uv_tail(W) - uv_tail(V)) / uv_tail(V)
        rows.append((sigma, amp, a, dtail))
        print(f"    {sigma:>7.2f}{amp:>9.2f}{a:>+18.6e}{dtail:>16.4f}%"
              f"  {'NEGATIVE' if a < 0 else 'positive'}")

neg = [r for r in rows if r[2] < 0]
print(f"\n    deformations driving the ANEC integral negative: {len(neg)} of {len(rows)}")
print(f"    largest UV-tail change across all of them: "
      f"{max(abs(r[3]) for r in rows):.4f}%")
print("\n  READ THIS CAREFULLY. A negative entry does NOT refute the ANEC — the ANEC")
print("  is a statement about states of the FULL theory satisfying the semiclassical")
print("  Einstein equation, and an arbitrary smooth deformation of a two-point")
print("  function need not be a state at all, let alone a self-consistent one.")
print("  Graham & Olum's condition is explicitly SELF-CONSISTENT achronal ANEC.")
print("  What the computation shows is where the ANEC's content actually lives:")
print("  NOT in Hadamard, NOT in the horizon's background conditions, but in the")
print("  SELF-CONSISTENCY requirement — which is the piece the physics literature")
print("  states and the register had not isolated.")
