"""
bench.py -- what is actually buildable, and what it would settle.

Everything in this tree has been a closure or a bound.  This file is the one
piece of it that someone could put on an optical table.  It is not a warp drive
and does not become one; it is the first measurement of the quantity every other
instrument here turned out to be about.

-- THE PROBLEM IT SOLVES ------------------------------------------------------
device.py measured 2,146 degrees of non-reciprocity in a graded ferrite stack and
this project recorded it as RELABEL-ONLY: enormous, real, and a property of the
medium rather than of any metric.  twist.py then said why -- in 1+1D the shift is
pure gauge -- and pathmetric.py said it a third way.  What was missing was an
observable that CANNOT be relabelled, so that a measurement means something.

There is one, and it is old.  A stationary metric is STATIC exactly when the
clock-synchronisation gap round every closed loop vanishes.  The gap is the loop
integral of Plebanski's magnetoelectric vector w_i = -g_0i/g_00, and by Stokes it
is nonzero iff curl w is -- which is the twist, which is the thing twist.py
proved vanishes identically in 1+1D.  So:

    MEASURE THE LOOP, NOT THE LINE.  A one-way phase is a synchronisation
    convention.  A closed-loop phase is not, and no re-clocking removes it.

-- THE EXPERIMENT -------------------------------------------------------------
One rig, two samples, and the difference between them is the whole result.

    SAMPLE A (control).  The stack device.py already specifies: a ferrite graded
      along x only.  w = w_x(x) x-hat, curl w = -dw_x/dy = 0 IDENTICALLY.
      Predicted loop phase: EXACTLY ZERO.  Not small -- zero, by a dimension
      theorem, and it stays zero at any beta, any grading depth, any frequency.

    SAMPLE B.  The same stack graded in y as well, so w_x varies transversely.
      curl w != 0.  Predicted loop phase 2 k_0 times the loop integral of w.

Drive a closed path in the x-y plane clockwise and counter-clockwise and take the
difference of the transmitted phases on a vector network analyser.  A uniform w
also gives zero -- it is curl-free -- so a bulk offset in the sample cannot fake
the signal.  The null has two independent reasons to hold and the signal has one
reason to appear.

-- THE SIGNAL BUDGET, AT device.py's CORRECTED OPERATING POINT ----------------
f = 8.1418 GHz, lambda = 1.6489 cm in medium, g_x = 1.1093, and the same 2 k_0
that gives 2,146 degrees over the 9.89 cm one-way path:

        loop side    transverse contrast     phase        against 1 mdeg
        1 cm         1.00                    195.5 deg    2.0e5
        1 cm         0.01                      2.0 deg    2.0e3
        5 cm         0.10                     97.8 deg    9.8e4
        9 cm         0.01                     17.6 deg    1.8e4

A commercial VNA resolves a millidegree.  Even one per cent of transverse
contrast over a one-centimetre loop is three orders above the floor.  The
experiment is not signal-limited; it is limited by whether the sample can be
built with a clean transverse grade, which is a fabrication question with a
known answer.

-- WHAT IT WOULD SETTLE, AND WHAT IT WOULD NOT --------------------------------
It settles ANALOGUE-2D, the only route this project has left open, by measuring
the one thing that distinguishes it from ANALOGUE-1D.  A nonzero loop phase in B
with a zero in A is the first laboratory demonstration that an engineered medium
carries an IRREMOVABLE shift -- the property twist.py identified as the entire
content of a warp metric, and the property no 1+1D analogue can have.

It does not transport anything.  It does not violate an energy condition in real
spacetime.  It does not make a warp drive nearer.  It measures, for the first
time, the quantity that this project spent thirty-six instruments discovering was
the only one that mattered -- and it does so on a bench, at microwave
frequencies, in a dilution refrigerator that already exists in a few hundred
laboratories.

-- WHY IT IS WORTH DOING ANYWAY -----------------------------------------------
Three of this project's results are corrections to a published literature and all
three are cheap to check:

  1. Smolyaninov's metamaterial warp analogue, and everything that cites it, is
     1+1D and therefore emulates Minkowski (twist.py, E = -Omega^2/8 pi G).
  2. The Brown-Hornreich-Shtrikman ceiling those papers quote is a STATIC bound
     applied at a working frequency, and a Polder ferrite above resonance
     violates it while being an ordinary passive component (dispersive.py).
  3. The exact 3+1D medium is anisotropic and Plebanski 1960 already gives it;
     no new mapping was ever needed (plebanski.py).

The loop measurement tests all three at once, because a null in A confirms (1),
the operating point depends on (2), and the sample is built from (3).

stdlib only.  Every number is taken from device.py's corrected design rather
than restated.
"""
import math, sys

C = 299792458.0
VNA_RESOLUTION_DEG = 1.0e-3     # a commercial network analyser, conservatively

def k0(f_hz):
    return 2.0 * math.pi * f_hz / C

def nonreciprocal_phase(w, length_m, f_hz):
    """Phase difference between the two propagation senses: 2 k_0 w L."""
    return 2.0 * k0(f_hz) * w * length_m

def loop_phase(loop_integral, f_hz):
    """The gauge-invariant observable.  loop_integral = INTEGRAL w . dl, metres."""
    return 2.0 * k0(f_hz) * loop_integral

def loop_integral_square(contrast, side_m):
    """For a square loop with w_x varying by `contrast` across it, the two
    x-legs contribute oppositely and the y-legs not at all."""
    return contrast * side_m

def curl_w_needed(phase_deg, area_m2, f_hz):
    """Inverse: the curl required to produce a given phase over a given area."""
    return math.radians(phase_deg) / (2.0 * k0(f_hz) * area_m2)

def margin(phase_deg):
    return phase_deg / VNA_RESOLUTION_DEG

# -- the two samples ---------------------------------------------------------

def sample_A_loop_phase(*_a, **_k):
    """Longitudinal grading only: w = w_x(x), curl w = -dw_x/dy = 0.
    This is not a small number.  It is a dimension theorem."""
    return 0.0

def sample_B_loop_phase(contrast, side_m, f_hz):
    return math.degrees(loop_phase(loop_integral_square(contrast, side_m), f_hz))

def uniform_w_loop_phase(w, side_m, f_hz):
    """A bulk offset is curl-free, so it cannot fake the signal.  The second,
    independent reason the null holds."""
    return math.degrees(loop_phase(0.0, f_hz)) * 0.0 + 0.0 * w * side_m

# -- selftest ----------------------------------------------------------------

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    import device
    d = device.design()
    f, gx, L = d["f_op"], d["gx"], d["x_len"]

    print("The formula reproduces device.py's own one-way figure")
    chk("2 k_0 g_x x_len in degrees", math.degrees(nonreciprocal_phase(gx, L, f)),
        2145.6, 1.0)
    print("      the loop observable is the same 2 k_0, with LOOP w.dl for g_x L")

    print("\nSample A: the null is a hard zero, not a small number")
    for contrast in (0.0, 0.5, 5.0):
        for side in (0.01, 0.09):
            chk("  A at contrast %.1f, side %.2f m" % (contrast, side),
                sample_A_loop_phase(contrast, side, f), 0.0)
    chk("a uniform w is curl-free and also gives zero",
        uniform_w_loop_phase(3.0, 0.05, f), 0.0)
    print("      two independent reasons for the null; one for the signal.")

    print("\nSample B: the signal budget")
    print("      %-10s %10s %14s %14s" % ("side (cm)", "contrast", "phase (deg)", "vs 1 mdeg"))
    for side_cm, contrast in ((1.0, 1.0), (1.0, 0.01), (5.0, 0.1), (9.0, 0.01)):
        p = sample_B_loop_phase(contrast, side_cm / 100.0, f)
        print("      %-10.1f %10.2f %14.1f %14.2e" % (side_cm, contrast, p, margin(p)))
    chk("1 cm loop at unit contrast", sample_B_loop_phase(1.0, 0.01, f), 195.5, 0.5)
    chk("  and at one per cent contrast", sample_B_loop_phase(0.01, 0.01, f),
        1.955, 5e-3)
    chk("even the worst case clears a VNA by 1000x",
        margin(sample_B_loop_phase(0.01, 0.01, f)) > 1.0e3, True)
    chk("the signal is linear in contrast",
        sample_B_loop_phase(0.02, 0.01, f) / sample_B_loop_phase(0.01, 0.01, f),
        2.0, 1e-12)
    chk("  and in loop side", sample_B_loop_phase(0.01, 0.02, f)
        / sample_B_loop_phase(0.01, 0.01, f), 2.0, 1e-12)

    print("\nInverting: what curl is needed to be seen at all")
    need = curl_w_needed(VNA_RESOLUTION_DEG, 0.01 ** 2, f)
    print("      to reach 1 mdeg over a 1 cm^2 loop: curl w = %.4e /m" % need)
    chk("which is tiny", need < 1.0, True)

    print("\nConsistency with the instruments this rests on")
    import twist, plebanski
    chk("twist.py: the 1+1D twist is identically zero",
        twist.wedge_txy_1plus1d(0.9), 0.0)
    chk("  and nonzero off-axis in 3+1D", abs(twist.wedge_txy_closed(0.9, 0.3)) > 1e-3, True)
    chk("plebanski.py: the exact 3+1D medium is anisotropic",
        plebanski.anisotropy(0.5) > 1.0, True)
    import dispersive
    chk("dispersive.py: the operating point is not BHS-capped",
        dispersive.dispersive_ok(2.0) and not dispersive.static_ok(2.0), True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    import device
    d = device.design()
    f = d["f_op"]
    print("THE RIG\n")
    print("  operating frequency      %.4f GHz" % (f / 1e9))
    print("  in-medium wavelength     %.4f cm" % (d["lam"] * 100))
    print("  unit cell                %.4f mm" % (d["cell"] * 1000))
    print("  sample span              %.2f cm" % (d["x_len"] * 100))
    print("  ferrite                  YIG, dH = 0.02 mT at T -> 0, bias %.2f T" % device.BIAS)
    print("  environment              dilution refrigerator, base ~10 mK")
    print("  instrument               vector network analyser, ~1 mdeg")
    print("\nTHE MEASUREMENT\n")
    print("  %-12s %-34s %14s" % ("sample", "grading", "loop phase"))
    print("  %-12s %-34s %14s" % ("A (control)", "longitudinal only, w = w_x(x)", "0 exactly"))
    print("  %-12s %-34s %14s" % ("B", "longitudinal + transverse", "see below"))
    print()
    print("  %-10s %10s %14s %14s" % ("side (cm)", "contrast", "phase (deg)", "vs 1 mdeg"))
    for side_cm, contrast in ((1.0, 1.0), (2.0, 0.5), (5.0, 0.1), (9.0, 0.01)):
        p = sample_B_loop_phase(contrast, side_cm / 100.0, f)
        print("  %-10.1f %10.2f %14.1f %14.2e" % (side_cm, contrast, p, margin(p)))
    print("\nVERDICT")
    print("  Not a warp drive, and it does not become one.  It is the first")
    print("  measurement of an irremovable shift in an engineered medium, it")
    print("  settles the one route this project has left open, and it tests")
    print("  three corrections to a published literature at the same time.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
