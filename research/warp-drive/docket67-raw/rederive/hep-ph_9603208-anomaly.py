#!/usr/bin/env python3
"""DOCKET 67 / pass S / 17 -- hep-ph/9603208-anomaly (Rubakov & Shaposhnikov).

Re-derives, from the Standard Model's per-generation quantum numbers alone
(no number taken from massform.py), the selection rule the tree uses:

  (a) per unit of SU(2) topological number N[A], each left-handed SU(2)
      doublet gets 2 T(2) = 1 zero mode (index theorem), so
      Delta B = N_c * N_f * (1/3) = N_f  (N_c = 3), Delta L = N_f,
      Delta N_e = Delta N_mu = Delta N_tau = Delta B / 3 ;
  (b) B - L has zero SU(2)^2 and zero U(1)_Y^2 anomaly; B + L has both;
      B has zero SU(3)^2 anomaly (vector-like under colour);
  (c) the mixed gravitational anomaly of B - L (sum of B - L charges over
      left-handed Weyl fields): -N_f without nu^c, 0 with nu^c -- a
      coefficient COMPUTED here; the anomaly EQUATION it enters is
      NAMED-NOT-READ in this stage;
  (d) the SM gauge anomalies cancel generation by generation and the number
      of doublets per generation is even (Witten SU(2)), i.e. N_f counts
      complete generations;
  (e) the tree's numbers: transitions = ceil(B/N_f), extra leptons =
      N_f*transitions - N_e = N_n (B - L balance), read from massform with
      bytecode writing disabled (research/ is never written).

Exit 0 iff every check passes.
"""
import math
import os
import sys
from fractions import Fraction as F

import sympy as sp

fails = []


def chk(name, got, want):
    ok = (got == want)
    print(("PASS " if ok else "FAIL ") + name + ": got " + str(got) + ", want " + str(want))
    if not ok:
        fails.append(name)


# Left-handed Weyl fields, one generation: (name, SU3 dim, SU3 rep T, SU2 dim, Y, B, L)
# T(fund of SU(N)) = 1/2.  Y normalised so Q = T3 + Y.
GEN = [
    ("Q",   3, F(1, 2), 2, F(1, 6),  F(1, 3),  0),
    ("u^c", 3, F(1, 2), 1, F(-2, 3), F(-1, 3), 0),
    ("d^c", 3, F(1, 2), 1, F(1, 3),  F(-1, 3), 0),
    ("L",   1, 0,       2, F(-1, 2), 0,        1),
    ("e^c", 1, 0,       1, F(1, 1),  0,        -1),
]
NUC = ("nu^c", 1, 0, 1, F(0), 0, -1)


def su2_sq(fields, charge):
    """sum_f X_f * T(2) * (colour multiplicity) over doublets."""
    return sum(charge(f) * F(1, 2) * f[1] for f in fields if f[3] == 2)


def y_sq(fields, charge):
    return sum(charge(f) * f[4] ** 2 * f[1] * f[3] for f in fields)


def su3_sq(fields, charge):
    return sum(charge(f) * f[2] * f[3] for f in fields if f[1] == 3)


def grav(fields, charge):
    return sum(charge(f) * f[1] * f[3] for f in fields)


B = lambda f: F(f[5])
L = lambda f: F(f[6])
BmL = lambda f: F(f[5]) - F(f[6])
BpL = lambda f: F(f[5]) + F(f[6])

print("== (a) zero-mode count per instanton (N[A] = 1), symbolic N_f, N_c")
Nf, Nc = sp.symbols("N_f N_c", positive=True, integer=True)
# each doublet: 2T(2) = 1 zero mode per colour component; quark B = 1/3 as the source states
dB_sym = Nf * Nc * sp.Rational(1, 3)
dL_sym = Nf * 1
print("   Delta B =", dB_sym, " Delta L =", dL_sym)
chk("Delta B at N_c = 3 equals N_f", sp.simplify(dB_sym.subs(Nc, 3) - Nf), 0)
chk("Delta B - Delta L at N_c = 3", sp.simplify(dB_sym.subs(Nc, 3) - dL_sym), 0)
chk("Delta N_e = 1 (one e-doublet) equals Delta B/3 at N_c = N_f = 3",
    sp.simplify(1 - dB_sym.subs({Nc: 3, Nf: 3}) / 3), 0)
# numeric per-generation version with the field table
dB1 = sum(B(f) * 2 * F(1, 2) * f[1] for f in GEN if f[3] == 2)
dL1 = sum(L(f) * 2 * F(1, 2) * f[1] for f in GEN if f[3] == 2)
chk("Delta B per generation per instanton (field table)", dB1, F(1))
chk("Delta L per generation per instanton (field table)", dL1, F(1))
for nf in (1, 2, 3, 4):
    chk("N_f=%d: Delta B = Delta L = N_f" % nf, (nf * dB1, nf * dL1), (F(nf), F(nf)))
# 't Hooft vertex (Q Q Q L)^N_f -- same content as massform's THOOFT_VERTEX
v = [("Q", F(1, 3), 0)] * 9 + [("L", 0, 1)] * 3
chk("'t Hooft vertex (qqql)^3: (B, L)", (sum(x[1] for x in v), sum(F(x[2]) for x in v)), (F(3), F(3)))

print("== (b) gauge anomalies of the global currents, per generation")
chk("SU(2)^2 anomaly of B", su2_sq(GEN, B), F(3, 2) * F(1, 3))
chk("SU(2)^2 anomaly of L", su2_sq(GEN, L), F(1, 2))
chk("SU(2)^2 anomaly of B - L", su2_sq(GEN, BmL), F(0))
chk("SU(2)^2 anomaly of B + L (nonzero)", su2_sq(GEN, BpL), F(1))
chk("U(1)_Y^2 anomaly of B", y_sq(GEN, B), F(-1, 2))
chk("U(1)_Y^2 anomaly of L", y_sq(GEN, L), F(-1, 2))
chk("U(1)_Y^2 anomaly of B - L", y_sq(GEN, BmL), F(0))
chk("U(1)_Y^2 anomaly of B + L (nonzero: the hypercharge term)", y_sq(GEN, BpL), F(-1))
chk("SU(3)^2 anomaly of B (vector-like)", su3_sq(GEN, B), F(0))
print("   ratio SU(2)^2 : U(1)_Y^2 for B+L =", su2_sq(GEN, BpL), ":", y_sq(GEN, BpL),
      " -> d(B+L) ∝ N_f (g^2 W Wt - g'^2 Y Yt) structure (sign/normalisation convention-dependent)")

print("== (c) mixed gravitational anomaly (sum of charges over Weyl fields)")
chk("grav anomaly of B", grav(GEN, B), F(0))
chk("grav anomaly of L, no nu^c", grav(GEN, L), F(1))
chk("grav anomaly of B - L, no nu^c (per generation)", grav(GEN, BmL), F(-1))
chk("grav anomaly of B - L, with nu^c", grav(GEN + [NUC], BmL), F(0))
cube = sum(BmL(f) ** 3 * f[1] * f[3] for f in GEN)
chk("(B-L)^3 anomaly, no nu^c (per generation)", cube, F(-1))
cube_n = sum(BmL(f) ** 3 * f[1] * f[3] for f in GEN + [NUC])
chk("(B-L)^3 anomaly, with nu^c", cube_n, F(0))

print("== (d) SM gauge anomalies cancel per generation; doublet count even")
Y = lambda f: f[4]
chk("SU(3)^2 U(1)_Y", sum(Y(f) * f[2] * f[3] for f in GEN if f[1] == 3), F(0))
chk("SU(2)^2 U(1)_Y", sum(Y(f) * F(1, 2) * f[1] for f in GEN if f[3] == 2), F(0))
chk("U(1)_Y^3", sum(Y(f) ** 3 * f[1] * f[3] for f in GEN), F(0))
chk("grav^2 U(1)_Y", sum(Y(f) * f[1] * f[3] for f in GEN), F(0))
ndoub = sum(f[1] for f in GEN if f[3] == 2)
chk("SU(2) doublets per generation (Witten: must be even)", (ndoub, ndoub % 2), (4, 0))
chk("an incomplete generation (Q only) spoils U(1)_Y^3",
    sum(Y(f) ** 3 * f[1] * f[3] for f in GEN[:1]) != 0, True)

print("== (e) the tree's numbers, recomputed from massform's COUNTS (read-only)")
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
try:
    import massform as mf
    Bp, Ne, Nn = mf.COUNTS["B"], mf.COUNTS["N_e"], mf.COUNTS["N_n"]
    print("   B = %.6e  N_e = %.6e  N_n = %.6e  N_F = %d" % (Bp, Ne, Nn, mf.N_F))
    chk("N_F from capture", mf.N_F, 3)
    T = math.ceil(Bp / 3)
    chk("transitions = ceil(B/3) matches 1.4036e28", "%.4e" % T, "1.4036e+28")
    chk("massform.transitions_needed agrees", mf.transitions_needed(), T)
    xl = 3 * T - Ne
    chk("extra leptons 3T - N_e matches 1.8977e28", "%.4e" % xl, "1.8977e+28")
    chk("extra leptons equal N_n to 1e-12 relative", abs(xl - Nn) / Nn < 1e-12, True)
    chk("THOOFT_DELTA_B_L", tuple(mf.THOOFT_DELTA_B_L), (F(3), 3))
    # sensitivity: a hypothetical 4th sequential generation (excluded by data, see report)
    T4 = math.ceil(Bp / 4)
    print("   [sensitivity only] N_f=4 -> transitions %.4e, extra leptons %.4e (still N_n)"
          % (T4, 4 * T4 - Ne))
    chk("B-L balance independent of N_f (N_f=4 hypothetical)", abs(4 * T4 - Ne - Nn) / Nn < 1e-12, True)
except Exception as e:  # pragma: no cover
    print("FAIL import massform:", repr(e))
    fails.append("import massform")

print()
print("FAILS:", fails if fails else "none")
sys.exit(1 if fails else 0)
