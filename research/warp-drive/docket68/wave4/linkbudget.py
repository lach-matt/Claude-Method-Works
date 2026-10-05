#!/usr/bin/env python3
"""
linkbudget.py -- DOCKET 68 wave 4, W4A: the TRANSMITTED power the channel needs (Step 1c's OPEN item S1C-O8).

Not seated.  M (rulings item 40): "2 then 1 please" -- a D68 wave 4 first, pricing what Step 1c left OPEN, then the
close and the Q-1s gate.  seat.channel_floor establishes a floor on the RECEIVED power only (its own docstring: "What
the TRANSMITTED energy must be at these dishes ... is NOT established here").  This file establishes it, at the floor's
own quantum, for a range of apertures, under the far-field diffraction law.

    python3 linkbudget.py              report
    python3 linkbudget.py --selftest   checks, with CONTROLS
    python3 linkbudget.py --json       the numbers as JSON

WHAT IT COMPUTES (every input imported: seat, aperture, light via step1c/demand.py, loaded by path)
  The floor's received power P_r and its quantum kT at each schedule (seat.channel_floor one polarisation;
  aperture.kT_from_floor), the quantum's wavelength lambda = h c / kT, and for apertures D_t, D_r the far-field
  transverse-mode number m = A_t A_r / (lambda d)^2.  For m < 1 the received fraction is m (H-FRIIS-IDEAL: no pointing,
  absorption or detector loss -- a ceiling on the delivered fraction), so the transmitted power is P_t = P_r / m.  It is
  compared with the Sun's luminosity (light.SOLAR_LUMINOSITY).  The aperture diameter that makes the link single-mode
  (m = 1, so P_t = P_r) is D = sqrt(4 lambda d / pi), for equal apertures.
  Whether an aperture can focus at the floor quantum (hundreds of keV at a year) is READ at source in OPTICS.

NAMED HYPOTHESES
  H-FRIIS-IDEAL, H-EQUAL-APERTURES (for the single-mode diameter), H-AT-FLOOR-QUANTUM (the link runs at the floor's own
  quantum, which minimises received energy -- seat.py's law), H-FOCUS-AT-QUANTUM (an aperture of that size focuses at
  that quantum: see OPTICS), and seat.py's (H-EM-CARRIER, H-FEW-MODES, H-ONE-POL).
"""
import contextlib
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.abspath(os.path.join(HERE, "..", ".."))
S1C = os.path.join(WD, "step1c")


def _by_path(key, path):
    import importlib.util as _ilu
    if key in sys.modules:
        return sys.modules[key]
    spec = _ilu.spec_from_file_location(key, path)
    mod = _ilu.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


with contextlib.redirect_stdout(io.StringIO()):
    demand = _by_path("s1c_demand", os.path.join(S1C, "demand.py"))
    seat = demand.seat
    aperture = demand.aperture
    if WD not in sys.path:
        sys.path.append(WD)
    import light

H, C = seat.H, seat.C
EV = 1.602176634e-19
L = demand.w3corridor.before_light()["L_m"]
L_SUN = light.SOLAR_LUMINOSITY
APERTURES_M = (("DSOC (0.22 m, 5 m)", 0.22, 5.0), ("1 m, 1 m", 1.0, 1.0), ("10 m, 10 m", 10.0, 10.0),
               ("100 m, 100 m", 100.0, 100.0), ("1 km, 1 km", 1e3, 1e3))

# The hard X-ray / soft gamma-ray optics READ at source by this session's optics reader (2026-10-05, alphaXiv and
# Firecrawl).  The achieved beam spread is set by figure errors, not diffraction (NuSTAR p.5: the PSF is dominated by
# figure errors).
OPTICS = {
    "NuSTAR (Harrison et al. 1301.7307v1)": {
        "route": "READ via alphaXiv, Table 2 p.4, Table 3 p.5, Sec. 5.1 p.6 (optics reader)", "kind": "measured in flight",
        "E_max_keV": 78.4, "HPD_arcsec": 58.0, "focal_m": 10.14, "phrase": "half power diameter ... of 58 arcsec"},
    "CLAIRE Laue lens (Frontera & von Ballmoos review 1007.4308v3)": {
        "route": "READ via alphaXiv pp.16-18, a secondary account of von Ballmoos et al. 2005 (optics reader)",
        "kind": "flown (2001 balloon); efficiency measured", "E_keV": 170.0, "band_keV": 3.0, "geom_area_m2": 511e-4,
        "efficiency": 0.09, "phrase": "geometric area of the CLAIRE lens was 511 cm2"},
    "ASTENA Narrow Field Telescope (2302.09272v1; 2309.11187v1; Exp. Astron. 51, 1175)": {
        "route": "READ via alphaXiv and Firecrawl (optics reader)", "kind": "DESIGN / simulated",
        "band_keV": (50.0, 700.0), "HPD_arcsec": 30.0, "geom_area_m2": 7.0, "focal_m": 20.0,
        "phrase": "angular resolution in the sub-MeV energy range of 30 arcsec"},
    "TRILL crystal alignment (2309.11187v1)": {
        "route": "READ via alphaXiv p.10 (optics reader)", "kind": "measured", "bragg_error_arcsec": (101.0, 161.0),
        "requirement_arcsec": 10.0, "phrase": "101 arcsec, with a standard deviation of 161 arcsec"},
}
ARCSEC = math.pi / (180.0 * 3600.0)


def floor_rows():
    out = []
    bits = demand.counts()[0][1]
    for nm, T in zip(demand.SCHEDULE_NAMES, demand.SCHEDULES_S):
        cf = seat.channel_floor(bits, T)
        kT, _E = aperture.kT_from_floor(bits, T)
        out.append({"schedule": nm, "T_s": T, "P_r_W": cf["E_1d_one_pol_J"] / T, "kT_eV": kT / EV,
                    "lambda_m": H * C / kT})
    return out


def modes(Dt, Dr, lam, d=L):
    return (math.pi * Dt * Dt / 4.0) * (math.pi * Dr * Dr / 4.0) / (lam * d) ** 2


def single_mode_D(lam, d=L):
    """Equal apertures with m = 1 (H-EQUAL-APERTURES)."""
    return math.sqrt(4.0 * lam * d / math.pi)


def budget():
    out = []
    for f in floor_rows():
        rows = []
        for name, Dt, Dr in APERTURES_M:
            m = modes(Dt, Dr, f["lambda_m"])
            Pt = f["P_r_W"] / m if m < 1 else f["P_r_W"]
            rows.append({"apertures": name, "modes": m, "P_t_W": Pt, "P_t_over_L_sun": Pt / L_SUN})
        out.append(dict(f, single_mode_D_m=single_mode_D(f["lambda_m"]), rows=rows))
    return out


def figure_limited(P_r, hpd_arcsec, A_r):
    """H-BEAM-FIGURE: a beam of full angular width hpd (set by the optic's achieved figure, not diffraction) spreads over
    a disc of diameter hpd x d; a receiver of collecting area A_r takes the fraction A_r / (pi (hpd d / 2)^2); so
    P_t = P_r / fraction (H-TX-OPTIC: the transmitter's optic achieves the same figure)."""
    spot_r = hpd_arcsec * ARCSEC * L / 2.0
    frac = A_r / (math.pi * spot_r * spot_r)
    return {"spot_radius_m": spot_r, "fraction": frac, "P_t_W": P_r / frac, "P_t_over_L_sun": P_r / frac / L_SUN}


def figure_limited_budget():
    """At the 1 yr floor (quantum ~263 keV): the measured NuSTAR figure (58 arcsec, at <= 78.4 keV) with the flown CLAIRE
    effective area (511 cm^2 x 9%) and with ASTENA's DESIGN area (7 m^2); and ASTENA's DESIGN figure (30 arcsec) with
    its design area.  H-FIGURE-AT-QUANTUM: the achieved figure carries to the floor quantum (no mirror optic reaches
    263 keV: NuSTAR's stops at 78.4 keV; a Laue lens is the only optic flown above it)."""
    yr = [f for f in floor_rows() if f["schedule"] == "1 yr"][0]
    nu, cl, at = (OPTICS[k] for k in list(OPTICS)[:3])
    A_claire = cl["geom_area_m2"] * cl["efficiency"]
    return {"P_r_W": yr["P_r_W"], "kT_keV": yr["kT_eV"] / 1e3,
            "measured figure, flown area": figure_limited(yr["P_r_W"], nu["HPD_arcsec"], A_claire),
            "measured figure, design area": figure_limited(yr["P_r_W"], nu["HPD_arcsec"], at["geom_area_m2"]),
            "design figure, design area": figure_limited(yr["P_r_W"], at["HPD_arcsec"], at["geom_area_m2"])}


def collect():
    return {"budget": budget(), "figure_limited_1yr": figure_limited_budget(), "L_sun_W": L_SUN, "OPTICS": OPTICS}


def report():
    d = collect()
    print("D68 wave 4, W4A -- the transmitted power at the floor's quantum (species count, one polarisation; "
          "H-FRIIS-IDEAL)")
    for b in d["budget"]:
        print("\n  %s: received floor %.3g W at quantum %.3g eV (lambda %.3g m); single-mode equal apertures D = %.3g m"
              % (b["schedule"], b["P_r_W"], b["kT_eV"], b["lambda_m"], b["single_mode_D_m"]))
        for r in b["rows"]:
            print("    %-20s modes %.3g -> transmitted %.3g W = %.3g L_sun" % (r["apertures"], r["modes"], r["P_t_W"],
                                                                         r["P_t_over_L_sun"]))
    fl = d["figure_limited_1yr"]
    print("\n  FIGURE-LIMITED, 1 yr (received floor %.3g W at %.3g keV; H-BEAM-FIGURE, H-TX-OPTIC, H-FIGURE-AT-QUANTUM):"
          % (fl["P_r_W"], fl["kT_keV"]))
    for k in ("measured figure, flown area", "measured figure, design area", "design figure, design area"):
        v = fl[k]
        print("    %-30s spot radius %.3g m; fraction %.3g -> transmitted %.3g W = %.3g L_sun"
              % (k, v["spot_radius_m"], v["fraction"], v["P_t_W"], v["P_t_over_L_sun"]))


def selftest():
    n_ok = n_bad = n_ctl = 0

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-96s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:96], got))

    print("linkbudget.py selftest")
    d = collect()
    b = dict((x["schedule"], x) for x in d["budget"])
    dsoc = [dict((r["apertures"], r) for r in x["rows"])["DSOC (0.22 m, 5 m)"]["P_t_W"] for x in d["budget"]]
    chk("  CONTROL: above single mode (1 km apertures at 1 yr, %.3g modes) it is the received floor itself"
        % dict((r["apertures"], r) for r in b["1 yr"]["rows"])["1 km, 1 km"]["modes"],
        dict((r["apertures"], r) for r in b["1 yr"]["rows"])["1 km, 1 km"]["P_t_W"] == b["1 yr"]["P_r_W"], True,
        ctl=True)
    chk("the single-mode equal aperture at 1 yr is between 100 m and 1 km (%.3g m); the floor quantum is over 100 keV "
        "(%.3g keV)" % (b["1 yr"]["single_mode_D_m"], b["1 yr"]["kT_eV"] / 1e3),
        (100 < b["1 yr"]["single_mode_D_m"] < 1e3, b["1 yr"]["kT_eV"] > 1e5), (True, True))
    chk("no mirror optic READ reaches the 1 yr floor quantum: NuSTAR's stops at 78.4 keV",
        OPTICS["NuSTAR (Harrison et al. 1301.7307v1)"]["E_max_keV"] < b["1 yr"]["kT_eV"] / 1e3, True)
    fl = d["figure_limited_1yr"]
    chk("figure-limited at 1 yr, the transmitted power exceeds the Sun's luminosity in every case read (%.3g, %.3g, %.3g "
        "L_sun)" % tuple(fl[k]["P_t_over_L_sun"] for k in ("measured figure, flown area", "measured figure, design area",
                                                          "design figure, design area")),
        all(fl[k]["P_t_over_L_sun"] > 1 for k in ("measured figure, flown area", "measured figure, design area",
                                                 "design figure, design area")), True)
    chk("  CONTROL: a beam of 1e-6 arcsec onto 7 m^2 would need under one solar luminosity",
        figure_limited(fl["P_r_W"], 1e-6, 7.0)["P_t_over_L_sun"] < 1, True, ctl=True)
    chk("every OPTICS record names a route and a kind; phrases under 15 words; ASTENA marked DESIGN",
        ([k for k, v in OPTICS.items() if not (v.get("route") and v.get("kind"))],
         [k for k, v in OPTICS.items() if len(v["phrase"].split()) >= 15],
         OPTICS["ASTENA Narrow Field Telescope (2302.09272v1; 2309.11187v1; Exp. Astron. 51, 1175)"]["kind"]
         .startswith("DESIGN")), ([], [], True))
    print("  [STRUCTURAL] below single mode the transmitted power at fixed apertures is schedule-independent (P_r and m both "
          "go as 1/T^2; DSOC's: %.3g W) -- an identity of the two laws, printed" % dsoc[0])
    print("  [STRUCTURAL] P_t = P_r / m for m < 1 (Friis far field); the single-mode D solves m = 1")
    print("  [STRUCTURAL] the figure-limited fraction is A_r over the beam's disc at L")
    print("\n%d/%d checks pass, %d of them controls; 3 STRUCTURAL printed, not counted" % (n_ok, n_ok + n_bad, n_ctl))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
