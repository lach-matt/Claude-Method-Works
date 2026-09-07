"""
dispersive.py -- the exemption, tested.  And it is not the one that was asked for.

The question was whether GAIN lifts Brown-Hornreich-Shtrikman, since BHS assumes
passivity.  The answer is that passivity was never the problem.  STATICITY was.

BHS 1968 bounds the EQUILIBRIUM magnetoelectric susceptibility by requiring the
free energy density

        F = 1/2 (eps E^2 + mu H^2) + alpha E H

to be positive definite, giving alpha^2 <= (eps - 1)(mu - 1).  That is a
thermodynamic statement about a STATIC response.  neclab.py, device.py and
plebanski.py all apply it at a working frequency to a magnetised ferrite, which
is a dispersive medium, and it is the wrong bound there.

-- AND IT IS DEMONSTRABLY THE WRONG BOUND, WHICH NEEDS NO NEW THEORY ----------
A magnetised ferrite has the Polder response

        mu(w) - 1 = wm w0/(w0^2 - w^2)        kappa(w) = wm w/(w0^2 - w^2)

Above resonance, w > w0, |kappa| > |mu - 1| -- computed here at w/w0 = 1.001,
1.2, 2 and 5, where the static bound is violated by factors of 1.0005, 1.2, 2.0
and 5.0.  Above-resonance ferrites are ordinary, stable, passive components sold
by the reel.  So the static bound forbids a regime that demonstrably exists, and
the refutation is a catalogue rather than an argument.

-- WHAT REPLACES IT, AND IT IS SATISFIED IDENTICALLY --------------------------
At a working frequency the positivity that matters is of the BRILLOUIN stored
energy, which carries d(w eps)/dw rather than eps (Landau & Lifshitz sec. 80).
Generalising to the bianisotropic case -- marked RECONSTRUCTED, since BHS's own
derivation is static and this is the natural extension, not a quoted result:

        |d(w alpha)/dw|^2  <=  (d(w eps)/dw - 1)(d(w mu)/dw - 1)

For the Polder tensor both sides are computable in closed form,

        d(w mu)/dw - 1 = wm w0 (w0^2 + w^2)/D^2      D = w0^2 - w^2
        d(w kappa)/dw  = 2 w wm w0^2 / D^2

checked here against finite differences at six frequencies, and their ratio is

        2 w w0 / (w0^2 + w^2)   <=  1   <=>   0 <= (w0 - w)^2

    TRUE FOR EVERY FREQUENCY, WITH EQUALITY EXACTLY AT RESONANCE.  The dispersive
    condition is never violated by a real ferrite and saturates only where the
    medium is lossy anyway.  The static one is violated by half the spectrum.

-- WHAT THAT COSTS THIS PROJECT'S TWO CLOSURES --------------------------------
Both rested on the static bound:

  neclab.py / device.py, 1+1D.  beta <= 0.245826 at n = 2 -- the c/4 ceiling.
    Without it the ceiling is the mapping's own singularity, n beta f = 1, which
    is the analogue horizon at beta = 1/n.

  plebanski.py, 3+1D.  w^2 <= (eps_yy - 1)^2 gave v^2 <= v^4, forbidding EVERY
    subluminal shift.  That was the whole of MAPPING-2D's negative closure.

Priced against device.py's own ferrite at the corrected cold magnetization:

        beta = 0.2224  g_x = 13.84 bulk   461 linewidths   ferrite loss 0.0022
        beta = 0.8250  g_x = 59.70 bulk   211 linewidths   ferrite loss 0.0095

    A FACTOR 3.7 IN BETA FOR A FACTOR 4.3 IN FERRITE LOSS, AND THE LOSS IS STILL
    UNDER ONE PER CENT.  The c/4 ceiling was not a material limit.  It was a
    static bound applied to a dispersive device.

-- WHAT DOES NOT REOPEN, AND THIS MATTERS MORE THAN WHAT DOES -----------------
twist.py is untouched.  In 1+1D the shift is pure gauge, E = -Omega^2/(8 pi G)
vanishes on the axis, and the emulated geometry is Minkowski AT ANY BETA.  A
faster 1+1D analogue emulates flat spacetime faster.  So ANALOGUE-1D stays
CLOSED-NEGATIVE and nothing here should be read as reviving it.

What reopens is the 3+1D route -- exactly where twist.py said the content is.
plebanski.py's mapping stands (it is Plebanski 1960, not a bound), its anisotropy
stands, and only its BHS verdict falls.

-- AND THE ANSWER TO THE GAIN QUESTION ----------------------------------------
Not needed.  Gain would exempt the medium from a bound that does not apply to it
in the first place, at the cost of noise and of converting a thermodynamic
condition into a dynamical one -- which is the trade wall.py already made twice.
Passive dispersion is free and sufficient.

-- THE SHAPE WORTH NOTICING ---------------------------------------------------
Both of this project's live routes were closed by a STATIC positivity condition
and both loosen when the dynamics is put in.  The warpshell: the centre-of-mass
theorem forbids self-acceleration for an isolated system, and the escape is to
radiate.  The analogue: BHS forbids the coupling for an equilibrium medium, and
the escape is to disperse.  Same shape, different physics, and neither is a
material.

stdlib only.  neclab and device are imported for their own numbers.
"""
import math, sys

W0_REF, WM_REF = 1.0, 0.30      # normalised Polder parameters for the algebra
H = 1e-7

# ------------------------------------------------------------- Polder ------

def mu_minus_1(w, w0=W0_REF, wm=WM_REF):
    return wm * w0 / (w0 * w0 - w * w)

def kappa(w, w0=W0_REF, wm=WM_REF):
    return wm * w / (w0 * w0 - w * w)

def d_w_mu(w, w0=W0_REF, wm=WM_REF, h=H):
    """d(w mu)/dw by finite difference -- the check on the closed form."""
    f = lambda x: x * (1.0 + mu_minus_1(x, w0, wm))
    return (f(w + h) - f(w - h)) / (2.0 * h)

def d_w_kappa(w, w0=W0_REF, wm=WM_REF, h=H):
    f = lambda x: x * kappa(x, w0, wm)
    return (f(w + h) - f(w - h)) / (2.0 * h)

def d_w_mu_closed(w, w0=W0_REF, wm=WM_REF):
    D = w0 * w0 - w * w
    return 1.0 + wm * w0 * (w0 * w0 + w * w) / (D * D)

def d_w_kappa_closed(w, w0=W0_REF, wm=WM_REF):
    D = w0 * w0 - w * w
    return 2.0 * w * wm * w0 * w0 / (D * D)

# ------------------------------------------------- the two bounds ----------

def static_ok(w, w0=W0_REF, wm=WM_REF):
    """BHS as applied: |kappa| <= |mu - 1|."""
    return abs(kappa(w, w0, wm)) <= abs(mu_minus_1(w, w0, wm))

def static_violation(w, w0=W0_REF, wm=WM_REF):
    """How badly, as a ratio.  > 1 means the static bound says 'impossible'."""
    return abs(kappa(w, w0, wm)) / abs(mu_minus_1(w, w0, wm))

def dispersive_ratio(w, w0=W0_REF, wm=WM_REF):
    """RECONSTRUCTED.  d(w kappa)/dw / (d(w mu)/dw - 1).  Must be <= 1."""
    return d_w_kappa_closed(w, w0, wm) / (d_w_mu_closed(w, w0, wm) - 1.0)

def dispersive_ratio_exact(w, w0=W0_REF):
    """DERIVED, and the point: the ratio is 2 w w0/(w0^2 + w^2), and
    2 w w0 <= w0^2 + w^2 is (w0 - w)^2 >= 0."""
    return 2.0 * w * w0 / (w0 * w0 + w * w)

def dispersive_ok(w, w0=W0_REF, wm=WM_REF):
    return dispersive_ratio(w, w0, wm) <= 1.0 + 1e-12

# ------------------------------------------- what the ceiling becomes ------

def horizon_beta(n):
    """The mapping's own singularity, n beta f = 1 at f = 1: the analogue
    horizon.  This is the ceiling once the static bound is withdrawn."""
    return 1.0 / n

def bhs_beta(n):
    import neclab
    return neclab.beta_max_exact(n)

def gain_over_static(n=2.0):
    return horizon_beta(n) / bhs_beta(n)

def detuning_for(gx):
    """Linewidths of detuning at which device.py's ferrite supplies g_x."""
    import device
    return (device.omega_m() / gx) / (device.GAMMA_G * device.YIG_DH)

def loss_for(gx):
    import device
    return device.ferrite_loss_tangent(gx)

def reach(n=1.2, frac=0.99):
    """(beta, g_x bulk, detuning, ferrite loss) at frac of the analogue horizon."""
    import neclab
    b = frac * horizon_beta(n)
    g = neclab.g_x(n, b, 1.0)
    return b, g, detuning_for(g), loss_for(g)

# ------------------------------------------------------------ selftest -----

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("Polder: the closed forms, against finite differences")
    for w in (0.2, 0.5, 0.8, 0.95, 1.2, 2.0):
        chk("  d(w mu)/dw at w/w0 = %.2f" % w, d_w_mu(w), d_w_mu_closed(w), 1e-6)
        chk("  d(w kappa)/dw", d_w_kappa(w), d_w_kappa_closed(w), 1e-6)

    print("\nThe static bound forbids a regime that exists")
    for w in (0.2, 0.5, 0.8, 0.95):
        chk("  satisfied below resonance, w/w0 = %.2f" % w, static_ok(w), True)
    for w, v in ((1.001, 1.0005), (1.2, 1.2), (2.0, 2.0), (5.0, 5.0)):
        chk("  VIOLATED above resonance, w/w0 = %.3f" % w, static_ok(w), False)
        chk("    by a factor", static_violation(w), v, 2e-3)
    print("      an above-resonance ferrite is an ordinary passive component.")

    print("\nThe dispersive condition, and it is satisfied identically")
    for w in (0.2, 0.5, 0.8, 0.95, 1.001, 1.2, 2.0, 5.0, 20.0):
        chk("  ratio <= 1 at w/w0 = %.3f" % w, dispersive_ok(w), True)
        chk("    == 2 w w0/(w0^2+w^2)", dispersive_ratio(w),
            dispersive_ratio_exact(w), 1e-12)
    chk("saturates exactly at resonance", dispersive_ratio_exact(1.0), 1.0, 1e-15)
    chk("  and only there", dispersive_ratio_exact(1.0001) < 1.0, True)
    chk("the condition is 0 <= (w0 - w)^2, so it cannot fail",
        all(dispersive_ratio_exact(w) <= 1.0 + 1e-15
            for w in (0.01, 0.5, 1.0, 2.0, 100.0)), True)

    print("\nWhat the two closures rested on")
    chk("neclab's c/4 at n = 2", bhs_beta(2.0), 0.2458263, 1e-6)
    chk("the mapping's own horizon at n = 2", horizon_beta(2.0), 0.5, 1e-15)
    chk("  so the static bound cost a factor", gain_over_static(2.0), 2.0343, 1e-3)
    b, g, lw, ls = reach(n=1.2)
    chk("at n = 1.2, 99% of the horizon gives beta", b, 0.825, 1e-12)
    chk("  requiring bulk g_x", g, 59.6985, 1e-3)
    chk("  at detuning (linewidths)", lw, 210.5, 0.5)
    chk("  and ferrite loss", ls, 0.009501, 1e-5)
    import device
    d = device.design()
    chk("against the current design's beta", d["beta"], 0.22243194, 1e-7)
    chk("  and its loss", d["tan_f"], 0.0022025389, 1e-9)
    chk("beta gains a factor", b / d["beta"], 3.7090, 1e-3)
    chk("  for a loss factor", ls / d["tan_f"], 4.3135, 1e-3)
    chk("and the loss is still under one per cent", ls < 0.01, True)

    print("\nWhat does NOT reopen")
    import twist
    chk("1+1D is still gauge: Omega = 0 on the axis", twist.omega_bbv(0.9, 0.0), 0.0)
    chk("  and E = 0 with it", twist.energy_density_bbv(0.9, 0.0), 0.0)
    print("      a faster 1+1D analogue emulates flat spacetime faster.")
    import plebanski
    chk("plebanski's MAPPING stands -- it is not a bound",
        plebanski.anisotropy(0.5) > 1.0, True)
    print("      only its BHS verdict falls.  The 3+1D route reopens.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("THE TWO BOUNDS, ACROSS THE SPECTRUM\n")
    print("  %-10s %12s %12s %10s | %12s %10s"
          % ("w/w0", "kappa", "mu-1", "static", "disp. ratio", "dispersive"))
    for w in (0.2, 0.5, 0.8, 0.95, 1.001, 1.2, 2.0, 5.0):
        print("  %-10.3f %12.5f %12.5f %10s | %12.6f %10s"
              % (w, kappa(w), mu_minus_1(w),
                 "ok" if static_ok(w) else "VIOLATED",
                 dispersive_ratio(w), "ok" if dispersive_ok(w) else "VIOLATED"))
    print("\nWHAT THE CEILING BECOMES\n")
    print("  %-8s %12s %12s %10s" % ("n", "beta_BHS", "beta_horizon", "factor"))
    for n in (1.2, 1.5, 2.0, 3.0):
        print("  %-8.1f %12.5f %12.5f %10.2f"
              % (n, bhs_beta(n), horizon_beta(n), horizon_beta(n) / bhs_beta(n)))
    print("\n  priced on device.py's own ferrite:\n")
    print("  %-10s %10s %10s %12s %12s" % ("case", "beta", "g_x bulk", "detune(lw)", "loss"))
    import device
    d = device.design()
    print("  %-10s %10.5f %10.2f %12.0f %12.6f"
          % ("current", d["beta"], d["gxp"], d["detune_lw"], d["tan_f"]))
    for n in (2.0, 1.5, 1.2):
        b, g, lw, ls = reach(n)
        print("  %-10s %10.5f %10.2f %12.1f %12.6f" % ("n=%.1f" % n, b, g, lw, ls))
    print("\nVERDICT")
    print("  The c/4 ceiling and the 3+1D subluminal prohibition both rested on a")
    print("  STATIC bound applied to a dispersive device.  The correct dispersive")
    print("  condition is satisfied identically by a real ferrite.  ANALOGUE-1D")
    print("  stays closed -- it emulates Minkowski at any beta -- but the 3+1D")
    print("  route reopens, and gain was never needed.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
