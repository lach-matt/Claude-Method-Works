#!/usr/bin/env python3
"""
device.py -- the parts list, with every field tested as it is specified.

M: test the specs periodically so the engineering is sound and does not raise
questions on the back end that testing parts and materials during the process
would have avoided.

So this is not a spec sheet with a test appendix.  Every row carries its own
test and its own verdict, and two rows failed on the first pass and changed the
design.  Those two are the reason for the discipline:

  TEST 4 FAILED AND CHANGED A PART.  The ferrite fixes the operating frequency;
  the split rings must then resonate ~17% above it.  A conventional SINGLE-GAP
  split ring of the required 2 mm size resonates at 118 GHz -- SIXTEEN TIMES too
  high.  Its gap capacitance is ~1 fF and nothing like enough.  The design must
  use a BROADSIDE-COUPLED ring on a high-permittivity substrate, where the
  capacitance is the ring-to-ring overlap across the dielectric: eps_r = 20 at
  0.5 mm gives 6.95 GHz.  Found by pricing the part, not by drawing it.

  TEST 5 FAILED AND ADDED A DESIGN RULE.  The wall is only a few unit cells, so
  the profile is quantised.  If the split-ring layer and the ferrite layer are
  MIS-REGISTERED BY ONE CELL -- g_x one step ahead of eps -- the stability bound
  is violated at the outermost step, margin -0.355.  It is fatal there and
  nowhere else, because the outer cell sits at zero margin BY CONSTRUCTION at
  the design limit.  Two fixes, both priced below: co-locate the ferrite inside
  the ring (Smolyaninov's own Fig. 2 geometry, now with a reason), and DERATE.

  THE DERATING IS THE DELIVERABLE OF TESTING EARLY.  Backing v_0 off from
  saturation buys registration tolerance, and the exchange rate is gentle:

      5 cells across the wall   ->  8.7% derate, wall 1.0 cm
     10 cells                   ->  4.8% derate, wall 2.1 cm
     20 cells                   ->  2.5% derate, wall 4.2 cm

  A built device that skipped this would have shown an unexplained instability
  at its outer boundary, and the cause -- a one-cell offset between two
  lithography layers -- is close to undiagnosable after the fact.

-- WHAT IT IS -----------------------------------------------------------------
A benchtop microwave block, roughly 17 cm across, that emulates the Alcubierre
metric for light at v_0 = 0.234 c.  It transports nothing.  Under door.py's test
it MEASURES, and neclab.py established that the analogue NEC violation costs it
3.15% of its stability margin.

Every material figure is PINNED to a real substance.  Nothing here is an
"advanced material".

stdlib only.  Imports neclab.py for the mapping rather than restating it.
"""
import math, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import neclab as L

MU0 = 4.0e-7 * math.pi
E0  = 8.8541878128e-12
c   = 299792458.0
N_BG = 2.0                       # background index; neclab: argmax of (n-1)/n^2

# ---- PINNED material constants ------------------------------------------------
GAMMA_G   = 2.0 * math.pi * 28.0e9   # rad/s/T, gyromagnetic ratio at g = 2
YIG_MU0MS = 0.175                    # T, 4 pi Ms = 1750 G for YIG
YIG_DH    = 0.5e-4                   # T, 0.5 Oe FMR linewidth, single-crystal YIG
BIAS      = 0.30                     # T, applied bias field  (ASSUMED, a design knob)
SRR_F     = 0.35                     # SRR oscillator strength (ASSUMED, typical)

# ---- the registration rule ----------------------------------------------------
def worst_misregistered_margin(beta, cells):
    """DERIVED.  Stability margin when the eps/mu layer and the g_x layer are
    offset by one unit cell.  Negative means the device is unstable somewhere."""
    lv = [i / (cells - 1.0) for i in range(cells)]
    return min((L.eps_mu(N_BG, beta, lv[i]) - 1.0) ** 2 - L.g_x(N_BG, beta, lv[i + 1]) ** 2
               for i in range(cells - 1))

def safe_beta(cells, lo=0.01):
    """DERIVED.  The largest v_0/c that survives a one-cell registration error."""
    hi = L.beta_max_exact()
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if worst_misregistered_margin(mid, cells) > 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def derate(cells):
    """DERIVED.  Fractional back-off from saturation that registration costs."""
    return 1.0 - safe_beta(cells) / L.beta_max_exact()

# ---- the ferrite ---------------------------------------------------------------
def fmr(bias=BIAS):
    """PINNED (Kittel).  omega_0 = gamma H_0."""
    return GAMMA_G * bias

def omega_m(mu0Ms=YIG_MU0MS):
    """PINNED.  omega_m = gamma mu_0 M_s."""
    return GAMMA_G * mu0Ms

def operating_omega(gx_required, bias=BIAS, mu0Ms=YIG_MU0MS):
    """DERIVED from Smolyaninov Eq (13): g_x ~ w0 wm / (w0^2 - w^2).
    Inverted for the frequency at which the ferrite delivers the required g_x."""
    w0, wm = fmr(bias), omega_m(mu0Ms)
    return math.sqrt(w0 * w0 - w0 * wm / gx_required)

def detuning_linewidths(gx_required, bias=BIAS):
    """DERIVED.  How far from ferromagnetic resonance the device sits, in YIG
    linewidths.  Large is good: it is why the loss stays low."""
    w0 = fmr(bias)
    return (w0 - operating_omega(gx_required, bias)) / (GAMMA_G * YIG_DH)

# ---- the split ring -------------------------------------------------------------
def srr_resonance_required(f_op, F=SRR_F, eps_required=None):
    """DERIVED.  A Lorentzian gives eps-1 = F/(1-(w/w0r)^2), so the ring must
    resonate above the operating frequency by a factor set by the detuning."""
    ratio = math.sqrt(1.0 - F / (eps_required - 1.0))
    return f_op / ratio

def srr_inductance(r, wt):
    """PINNED (standard loop formula): L = mu0 r [ln(8r/w) - 2]."""
    return MU0 * r * (math.log(8.0 * r / wt) - 2.0)

def srr_f0(L_ind, C):
    """PINNED.  f0 = 1/(2 pi sqrt(LC))."""
    return 1.0 / (2.0 * math.pi * math.sqrt(L_ind * C))

def cap_single_gap(wt, thick, gap, eps_r=4.0):
    """DERIVED.  A single split's gap capacitance: eps0 eps_r (w t)/g.  This is
    the part that FAILS -- it is femtofarads."""
    return E0 * eps_r * (wt * thick) / gap

def cap_broadside(r, wt, h, eps_r):
    """DERIVED.  Two rings facing across a substrate: eps0 eps_r (2 pi r w)/h.
    Two orders of magnitude larger, and the fix."""
    return E0 * eps_r * (2.0 * math.pi * r * wt) / h

# ---- geometry and loss ----------------------------------------------------------
def wavelength(f_op, eps):
    """DERIVED.  In-medium wavelength."""
    return c / f_op / eps

def loss_fraction(traverse_m, lam_m, Q):
    """DERIVED.  1 - exp(-x / L_abs) with L_abs = lambda Q / 2 pi."""
    return 1.0 - math.exp(-traverse_m / (lam_m * Q / (2.0 * math.pi)))

# ------------------------------------------------------------ the design point --
CELLS  = 10
SAFETY = 0.95     # a bisected boundary is not a design point.  The margin at
                  # safe_beta() is zero BY CONSTRUCTION -- it is where the
                  # mis-registered cell just touches Eq (9) -- so the design
                  # point sits 5% inside it.  Found by the selftest refusing to
                  # call a zero margin positive, which is the discipline working.

def design():
    """DERIVED.  The whole chain, computed from the registration rule outward so
    it is self-consistent by construction: choosing the derate changes beta,
    which changes g_x, which changes the ferrite's operating frequency, which
    changes the cell size and hence the wall.  Recomputed, never patched."""
    beta = SAFETY * safe_beta(CELLS)
    eps  = L.eps_mu(N_BG, beta, 1.0)
    gx   = L.g_x(N_BG, beta, 1.0)
    w    = operating_omega(gx)
    f_op = w / (2.0 * math.pi)
    lam  = wavelength(f_op, eps)
    cell = lam / 10.0
    wall = CELLS * cell
    R    = 4.0 * wall
    return dict(beta=beta, eps=eps, gx=gx, f_op=f_op, lam=lam, cell=cell,
                wall=wall, R=R, span=2.0 * (R + wall))

# ------------------------------------------------------------------- report ----
def selftest():
    ok = True
    def chk(label, got, want, tol=1e-6):
        nonlocal ok
        if isinstance(want, bool):
            good, g, w = got == want, got, want
        else:
            good = abs(got - want) <= tol * abs(want) if want else abs(got) < 1e-12
            g, w = "%.7g" % got, "%.7g" % want
        ok &= good
        print("  %-58s %14s %14s  %s" % (label, g, w, "ok" if good else "FAIL"))

    d = design()
    print("TEST 1 -- the ferrite delivers the required g_x, off resonance")
    chk("YIG FMR at 0.30 T (GHz)", fmr() / 2e9 / math.pi, 8.40)
    chk("omega_m as a frequency (GHz)", omega_m() / 2e9 / math.pi, 4.90)
    chk("g_x far below resonance is wm/w0", omega_m() / fmr(), 0.5833333, tol=1e-6)
    chk("required g_x is above that, so detuning is needed", d["gx"] > omega_m() / fmr(), True)
    chk("operating frequency (GHz)", d["f_op"] / 1e9, 5.7839395, tol=1e-7)
    chk("detuning in YIG linewidths", detuning_linewidths(d["gx"]), 1868.6146, tol=1e-7)
    chk("  -- far off resonance, so PASS", detuning_linewidths(d["gx"]) > 100.0, True)
    # Identity: at the FMR the required detuning vanishes, so g_x diverges.
    chk("g_x -> inf as w -> w0 (identity)",
        operating_omega(1e12) / fmr(), 1.0, tol=1e-9)

    print("\nTEST 2 -- the required eps and mu are modest")
    chk("eps = mu required at the wall's outside", d["eps"], 2.2331443, tol=1e-7)
    chk("  -- under 2.5, so no extreme metamaterial", d["eps"] < 2.5, True)
    chk("SRR must resonate above f_op (GHz)",
        srr_resonance_required(d["f_op"], SRR_F, d["eps"]) / 1e9, 6.8346277, tol=1e-7)

    print("\nTEST 3 -- geometry: does it fit, and does light get through?")
    chk("in-medium wavelength (cm)", d["lam"] * 100.0, 2.3210268, tol=1e-7)
    chk("unit cell (mm)", d["cell"] * 1000.0, 2.3210268, tol=1e-7)
    chk("wall = %d cells (cm)" % CELLS, d["wall"] * 100.0, 2.3210268, tol=1e-7)
    chk("bubble radius (cm)", d["R"] * 100.0, 9.2841072, tol=1e-7)
    chk("device span (cm)", d["span"] * 100.0, 23.210268, tol=1e-7)
    chk("  -- benchtop", d["span"] < 0.5, True)
    for Q, want in ((1e2, 0.46651191), (1e3, 0.060898633), (1e4, 0.0062634874)):
        chk("loss across the device at Q = %.0e" % Q,
            loss_fraction(d["span"], d["lam"], Q), want, tol=1e-7)
    # 6.1% across the whole block at Q = 1000.  The criterion is 10%, which is
    # what a proof-of-principle transmission measurement tolerates; Q = 100 needs
    # the gain-medium compensation Smolyaninov cites.
    chk("  -- under 10% at Q = 1000, so PASS",
        loss_fraction(d["span"], d["lam"], 1e3) < 0.10, True)

    print("\nTEST 4 -- THE ONE THAT FAILED: a single-gap SRR is 16x too high")
    r, wt, th = 0.8e-3, 0.2e-3, 35e-6
    Li = srr_inductance(r, wt)
    f_single = srr_f0(Li, cap_single_gap(wt, th, 0.2e-3))
    chk("single-gap SRR resonance (GHz)", f_single / 1e9, 117.76167, tol=1e-7)
    chk("  -- FAILS against the 6.83 GHz needed", f_single > 5.0 * d["f_op"], True)
    chk("its gap capacitance (fF)", cap_single_gap(wt, th, 0.2e-3) * 1e15, 1.2395863, tol=1e-7)
    f_bc = srr_f0(Li, cap_broadside(r, wt, 0.5e-3, 20.0))
    chk("broadside-coupled, eps_r = 20, h = 0.5 mm (GHz)", f_bc / 1e9, 6.9484519, tol=1e-7)
    chk("  -- in range, so the fix WORKS", 5e9 < f_bc < 10e9, True)
    chk("ring outer diameter fits the cell", 2.0 * (r + wt) < d["cell"], True)

    print("\nTEST 5 -- THE OTHER ONE: one-cell mis-registration is fatal")
    bsat = L.beta_max_exact()
    chk("at saturation, mis-registered margin", worst_misregistered_margin(bsat, 5), -0.35536435, tol=1e-7)
    chk("  -- NEGATIVE, so unstable", worst_misregistered_margin(bsat, 5) < 0.0, True)
    chk("co-located margin at the same point is fine",
        L.margin(N_BG, bsat, 0.75) > 0.0, True)
    print("   the derating curve:")
    for n_cells, want in ((5, 0.087199241), (10, 0.047543348), (20, 0.024941964)):
        chk("   %2d cells -> derate" % n_cells, derate(n_cells), want, tol=1e-4)
    chk("the design point's beta", d["beta"], 0.22243194, tol=1e-7)
    chk("the bisected boundary has ZERO margin, by construction",
        abs(worst_misregistered_margin(safe_beta(CELLS), CELLS)) < 1e-9, True)
    chk("so the design point sits %d%% inside it" % int(100 * (1 - SAFETY)),
        d["beta"] < safe_beta(CELLS), True)
    chk("and its mis-registered margin is genuinely positive",
        worst_misregistered_margin(d["beta"], CELLS) > 0.01, True)

    print("\nSELF-CONSISTENCY -- the chain is recomputed, not patched")
    # Changing the derate must move every downstream number together.
    chk("beta below saturation", d["beta"] < bsat, True)
    chk("eps follows beta", d["eps"], L.eps_mu(N_BG, d["beta"], 1.0))
    chk("g_x follows beta", d["gx"], L.g_x(N_BG, d["beta"], 1.0))
    chk("f_op follows g_x", d["f_op"] * 2.0 * math.pi, operating_omega(d["gx"]))
    chk("cell follows f_op and eps", d["cell"], wavelength(d["f_op"], d["eps"]) / 10.0)
    chk("neclab's NEC finding still holds here",
        L.margin(N_BG, d["beta"], 0.25) > L.margin(N_BG, d["beta"], 1.0), True)

    print("\n%s" % ("SELFTEST PASS" if ok else "SELFTEST FAIL"))
    return 0 if ok else 1


def report():
    d = design()
    bsat = L.beta_max_exact()
    print("""
device.py -- the parts list, tested as it was specified
================================================================================
A benchtop microwave block that emulates the Alcubierre metric for light.  Every
material figure is pinned to a real substance; nothing here is an "advanced
material".  Two rows failed on the first pass and changed the design.

-- THE DESIGN POINT ------------------------------------------------------------
  emulated warp speed v_0        %.4f c      derated %.1f%% total (%.1f%% registration + %.0f%% safety)
  background index n             %.1f            argmax of (n-1)/n^2
  eps = mu, outside the wall     %.4f
  magnetoelectric g_x            %.4f
  operating frequency            %.3f GHz     set by the ferrite, not chosen
  in-medium wavelength           %.3f cm
  unit cell                      %.3f mm      lambda/10
  wall                           %.3f cm      %d cells
  bubble radius                  %.2f cm
  DEVICE SPAN                    %.1f cm      a benchtop object

-- TEST 1: THE FERRITE (YIG) ---------------------------------------------------
  4 pi Ms = 1750 G, bias %.2f T -> FMR at %.2f GHz, omega_m/2pi = %.2f GHz.
  Far below resonance the ferrite gives g_x = wm/w0 = %.4f, short of the %.4f
  required, so the device must sit closer in.  Solving Eq (13):

      operating point   %.3f GHz   =  %.0f YIG linewidths off resonance

  YIG's 0.5 Oe linewidth is 1.4 MHz, so the device runs over a thousand
  linewidths clear of the lossy region.  PASS, with enormous margin.

-- TEST 2: THE SPLIT RINGS -----------------------------------------------------
  eps = mu = %.4f is a MODEST requirement -- no extreme metamaterial.  At an
  oscillator strength of %.2f the rings must resonate at %.3f GHz, %.0f%% above
  the operating frequency.  PASS.

-- TEST 3: GEOMETRY AND LOSS ---------------------------------------------------""" %
          (d["beta"], 100 * (1 - d["beta"] / L.beta_max_exact()), 100 * derate(CELLS),
            100 * (1 - SAFETY), N_BG, d["eps"], d["gx"], d["f_op"] / 1e9,
           d["lam"] * 100, d["cell"] * 1000, d["wall"] * 100, CELLS, d["R"] * 100,
           d["span"] * 100, BIAS, fmr() / 2e9 / math.pi, omega_m() / 2e9 / math.pi,
           omega_m() / fmr(), d["gx"], d["f_op"] / 1e9, detuning_linewidths(d["gx"]),
           d["eps"], SRR_F, srr_resonance_required(d["f_op"], SRR_F, d["eps"]) / 1e9,
           100 * (srr_resonance_required(d["f_op"], SRR_F, d["eps"]) / d["f_op"] - 1)))
    print("  %8s %18s %14s" % ("Q", "absorption length", "loss across %.1f cm" % (d["span"] * 100)))
    for Q in (1e2, 1e3, 1e4):
        print("  %8.0e %15.2f m %13.1f%%"
              % (Q, d["lam"] * Q / (2 * math.pi), 100 * loss_fraction(d["span"], d["lam"], Q)))
    r, wt, th = 0.8e-3, 0.2e-3, 35e-6
    Li = srr_inductance(r, wt)
    print("""  Copper rings at room temperature give Q ~ 10^2-10^3; superconducting
  designs reach 10^4.  PASS from Q = 10^3 up; at 10^2 the 31%% loss needs the
  gain-medium compensation Smolyaninov cites.

-- TEST 4: FAILED, AND CHANGED A PART ------------------------------------------
  The ferrite FIXES the operating frequency, so the rings are not free to be any
  size.  A conventional single-gap split ring of the required %.2f mm diameter:

      L = %.3e H   C_gap = %.3f fF   ->   f0 = %.1f GHz

  SIXTEEN TIMES too high.  The gap capacitance of a single split is femtofarads
  and nothing like enough.  The fix is a BROADSIDE-COUPLED ring -- two rings
  facing across a thin high-permittivity substrate, so the capacitance is the
  ring-to-ring overlap rather than the gap:

      eps_r = 20, h = 0.5 mm  ->  C = %.1f fF  ->  f0 = %.2f GHz    IN RANGE

  Found by pricing the part.  A layout drawn from the required f0 alone would
  have been fabricated before anyone noticed.

-- TEST 5: FAILED, AND ADDED A DESIGN RULE -------------------------------------
  The wall is only %d unit cells, so the profile is quantised.  If the split-ring
  layer and the ferrite layer are MIS-REGISTERED BY ONE CELL -- g_x one step
  ahead of eps -- then at saturation:

      worst margin, co-located          %+.5f
      worst margin, one cell offset     %+.5f      VIOLATES Eq (9)

  Fatal at the outermost step and nowhere else, because that cell sits at ZERO
  margin by construction at the design limit.  Two fixes, and the design takes
  both.  Co-locate the ferrite inside the ring -- Smolyaninov's own Fig. 2
  geometry, which now has a reason rather than a convenience.  And DERATE:
""" % (2 * (r + wt) * 1000, Li, cap_single_gap(wt, th, 0.2e-3) * 1e15,
       srr_f0(Li, cap_single_gap(wt, th, 0.2e-3)) / 1e9,
       cap_broadside(r, wt, 0.5e-3, 20.0) * 1e15,
       srr_f0(Li, cap_broadside(r, wt, 0.5e-3, 20.0)) / 1e9,
       CELLS, L.margin(N_BG, bsat, 0.75), worst_misregistered_margin(bsat, 5)))
    print("    %8s %14s %12s %12s" % ("cells", "safe v_0/c", "derate", "wall"))
    for n_cells in (5, 7, 10, 15, 20):
        b = safe_beta(n_cells)
        e = L.eps_mu(N_BG, b, 1.0)
        w = wavelength(operating_omega(L.g_x(N_BG, b, 1.0)) / (2 * math.pi), e) / 10.0
        print("    %8d %14.4f %11.1f%% %10.2f cm" % (n_cells, b, 100 * derate(n_cells), n_cells * w * 100))
    print("""
  A built device that skipped this would have shown an unexplained instability
  at its outer boundary, and a one-cell offset between two lithography layers is
  close to undiagnosable after the fact.

    THAT IS WHAT TESTING PARTS DURING THE DESIGN BOUGHT: ONE PART REPLACED AND
    ONE DERATING, BOTH BEFORE ANYTHING WAS DRAWN.

-- WHAT THIS DEVICE IS AND IS NOT ----------------------------------------------
  It emulates the Alcubierre metric for light at %.3f c inside a %.0f cm block.
  It transports nothing and it does not gravitate the emulated shift.  Under
  door.py's test it MEASURES -- and neclab.py established that the analogue NEC
  violation costs it only %.2f%% of its stability margin, which is why the parts
  list above is made of YIG and copper rather than of anything exotic.
""" % (d["beta"], d["span"] * 100, 100 * L.cost_of_the_violation()))
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
