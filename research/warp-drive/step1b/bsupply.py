#!/usr/bin/env python3
"""
bsupply.py -- Step 1b: the energy B must supply locally, against Proxima's own light.

Not seated.  Nothing here edits the board: figures are IMPORTED (openterms, balance, seat, settle, light); the stellar
luminosity is READ at source.  M (2026-10-05): "I agree, continue" -- on the lead's next step: openterms.py leaves B a local
deficit (chemistry, up to its ceiling, when A's residue and B's stock share a form; openterms.global_chem), which B's
surroundings must supply.  The obvious supply is Proxima's light.

    python3 bsupply.py              report
    python3 bsupply.py --selftest   checks, with CONTROLS
    python3 bsupply.py --json       the numbers as JSON

WHAT IT COMPUTES
  The flux at Proxima b's orbit, F = L / (4 pi a^2), with L* = 0.0016 +- 0.0006 L_sun READ (Faria et al. 2022,
  arXiv:2202.05188v1, Table 1 p.2, citing Boyajian et al. 2012; via alphaXiv) and a = seat.FARIA_2022's 0.04856 au
  (Table C.1 p.17, READ by the board); L_sun = light.SOLAR_LUMINOSITY (3.828e26 W).  CONTROL: the same expression at
  1 au with L_sun gives the solar constant's 1361 W/m^2 to 1 W/m^2.
  Then the time to gather each local term at B with a collector of area A and efficiency eta (H-COLLECT):
      t = E / (F A eta)
  for: B's chemical deficit ceiling (openterms.chem_ceiling_j), B's register reset floor (balance OUT-B-HEAT), and -- for
  scale, not as a term of the equation -- the payload's rest energy and seat.erec_ceiling at beta 0.01.
  All three L* values (low, central, high) are carried; the spread is the READ uncertainty.

HISTORY (Step 1b verifier, 2026-10-05): 'a 100 m^2 collector gathers it in under a week' fails at Faria's low L*
(7.22 days); Faria's +-0.0006 is not in the primary source it cites (Boyajian 2012, READ: +-0.00002) -- both carried;
'shortest times' was wrong for the ceiling row; the area and eta checks were identities (now STRUCTURAL).
HISTORY: the first selftest asserted the reset floor is gathered 'in under a minute' on 1 m^2; it takes 268.6 s.  The
guessed threshold failed, not a finding; the check now compares it with the chemical term and prints the time.

NAMED HYPOTHESES
  H-COLLECT    a collector of area A and efficiency eta <= 1 (eta = 1 gives the shortest time FOR A GIVEN E; for the
               chemical row E is itself a ceiling, so its t is neither a floor nor a ceiling).
  H-AT-ORBIT   flux taken at b's orbit, above any atmosphere (b's atmosphere and albedo are unknown).
  H-STEADY     Proxima's mean luminosity; its flares and the planet's day side are not modelled.
  H-STOCK-FORM (openterms.py) the deficit is the chemical ceiling only when A's residue and B's stock share a form; it is
               a ceiling, not a value.
"""
import contextlib
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.abspath(os.path.join(HERE, ".."))
for _p in (os.path.join(WD, "docket68"), WD, HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

with contextlib.redirect_stdout(io.StringIO()):
    import openterms
    import balance
    import seat
    import settle
    import light
    import massform

L_SUN = light.SOLAR_LUMINOSITY
AU = settle.AU_M
YEAR_S = seat.YEAR_S
FARIA_2022_TABLE1 = {"source": "arXiv:2202.05188v1", "route": "READ via alphaXiv (answer_pdf_queries), Table 1 p.2",
                     "L_over_Lsun": (0.0016, 0.0006), "L_ref": "Boyajian et al. (2012)",
                     "Teff_K": (2900, 100), "R_over_Rsun": (0.141, 0.021), "HZ_au": (0.0423, 0.0816)}
BOYAJIAN_2012 = {"source": "arXiv:1208.2431v2", "route": "READ via alphaXiv (answer_pdf_queries), Table 6 p.46",
                 "GJ551_L_over_Lsun": (0.00155, 0.00002), "GJ551_R_over_Rsun": (0.1410, 0.0070), "GJ551_Teff_K": (3054, 79),
                 "note": "the primary source Faria 2022 cites for L*; its uncertainty is 30x smaller than Faria's 0.0006 "
                         "-- a DISCREPANCY between the two READ sources, recorded, not adjudicated"}
AREAS_M2 = (1.0, 100.0, 1.0e4)


def flux(L, a):
    return L / (4.0 * math.pi * a * a)


def flux_b():
    l, s = FARIA_2022_TABLE1["L_over_Lsun"]
    a = seat.FARIA_2022["b_a_au"] * AU
    return {k: flux(v * L_SUN, a) for k, v in (("low", l - s), ("central", l), ("high", l + s))}


def flux_b_boyajian():
    l, s = BOYAJIAN_2012["GJ551_L_over_Lsun"]
    a = seat.FARIA_2022["b_a_au"] * AU
    return {k: flux(v * L_SUN, a) for k, v in (("low", l - s), ("central", l), ("high", l + s))}


def gather_time_s(E, F, A, eta=1.0):
    return E / (F * A * eta)


def terms_at_B():
    reset = [x[4] for x in balance.equation(balance.counts()[0][1], "R-QUANTUM") if x[0] == "OUT-B-HEAT"][0]
    return {"chemical deficit ceiling (openterms.py, H-STOCK-FORM)": openterms.chem_ceiling_j(),
            "register reset floor (balance OUT-B-HEAT, H-RESET)": reset}


def scale_at_B():
    return {"payload rest energy (scale only)": massform.rest_energy_j(),
            "E_rec payback ceiling at beta 0.01 (seat, scale only)": seat.erec_ceiling()[0.01]}


def collect():
    F = flux_b()
    rows = []
    for name, E in list(terms_at_B().items()) + list(scale_at_B().items()):
        for k in ("high", "central", "low"):
            for A in AREAS_M2:
                rows.append({"term": name, "E_J": E, "L_case": k, "A_m2": A,
                             "t_s": gather_time_s(E, F[k], A), "t_yr": gather_time_s(E, F[k], A) / YEAR_S})
    E = openterms.chem_ceiling_j()
    week = {"Faria " + k: gather_time_s(E, v, 100.0) / 86400.0 for k, v in F.items()}
    week.update({"Boyajian " + k: gather_time_s(E, v, 100.0) / 86400.0 for k, v in flux_b_boyajian().items()})
    return {"flux_W_m2": F, "flux_boyajian_W_m2": flux_b_boyajian(), "earth_control_W_m2": flux(L_SUN, AU),
            "rows": rows, "chem_100m2_days": week, "READ": [FARIA_2022_TABLE1, BOYAJIAN_2012]}


def report():
    d = collect()
    F = d["flux_W_m2"]
    print("Step 1b -- B's local supply against Proxima's light (H-AT-ORBIT, H-STEADY, H-COLLECT eta = 1)")
    print("  flux at b's orbit: low %.0f, central %.0f, high %.0f W/m^2 (L* = 0.0016 +- 0.0006 L_sun, READ); at 1 au "
          "from the Sun %.0f W/m^2 (control)" % (F["low"], F["central"], F["high"], d["earth_control_W_m2"]))
    last = None
    for r in d["rows"]:
        if r["L_case"] != "central":
            continue
        if r["term"] != last:
            print("\n  %s: %.4g J" % (r["term"], r["E_J"]))
            last = r["term"]
        print("    collector %8.0f m^2: %.4g s = %.4g yr" % (r["A_m2"], r["t_s"], r["t_yr"]))
    print("\n  (central L*; the low and high cases scale the times by %.2f and %.2f)"
          % (F["central"] / F["low"], F["central"] / F["high"]))
    B = d["flux_boyajian_W_m2"]
    print("  Boyajian 2012 (the primary source, READ): L* = 0.00155 +- 0.00002 L_sun -> %.0f W/m^2 (%.0f-%.0f); "
          "DISCREPANCY with Faria's +-0.0006, recorded, not adjudicated" % (B["central"], B["low"], B["high"]))
    print("  chemical ceiling on 100 m^2, days: %s" % {k: round(v, 2) for k, v in d["chem_100m2_days"].items()})


def selftest():
    n_ok = n_bad = n_ctl = 0

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-92s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:92], got))

    print("bsupply.py selftest")
    chk("CONTROL: L_sun / (4 pi au^2) gives the solar constant 1361 W/m^2 to 1 W/m^2",
        abs(flux(L_SUN, AU) - 1361.0) < 1.0, True, ctl=True)
    F = flux_b()
    chk("flux at b, central: 0.0016 L_sun at 0.04856 au = 0.0016/0.04856^2 x the 1 au flux (to 1e-9)",
        abs(F["central"] / flux(L_SUN, AU) - 0.0016 / 0.04856 ** 2) < 1e-9, True)
    chk("the flux at b lies below the 1 au flux for every READ L* (b receives less than Earth)",
        all(v < flux(L_SUN, AU) for v in F.values()), True)
    chk("b lies inside the READ habitable-zone range 0.0423-0.0816 au (Table 1)",
        FARIA_2022_TABLE1["HZ_au"][0] < seat.FARIA_2022["b_a_au"] < FARIA_2022_TABLE1["HZ_au"][1], True)
    tb = terms_at_B()
    E = tb["chemical deficit ceiling (openterms.py, H-STOCK-FORM)"]
    t = gather_time_s(E, F["central"], 1.0)
    chk("chemical deficit ceiling over 1 m^2, central L*: between 1 and 2 years (a computed range, printed)",
        1.0 < t / YEAR_S < 2.0, True)
    wk = collect()["chem_100m2_days"]
    chk("on 100 m^2 the chemical ceiling is gathered within a week at Faria's central L* and every Boyajian case, but "
        "NOT at Faria's low L* (%.2f days)" % wk["Faria low"],
        (wk["Faria central"] < 7, all(wk["Boyajian " + k] < 7 for k in ("low", "central", "high")), wk["Faria low"] < 7),
        (True, True, False))
    bf = flux_b_boyajian()
    chk("Boyajian's L* gives a flux within Faria's range and its spread is ~1.3% (READ, computed)",
        (F["low"] < bf["central"] < F["high"], abs(bf["high"] / bf["central"] - 1 - 0.0129) < 0.001), (True, True))
    _tr = gather_time_s(tb["register reset floor (balance OUT-B-HEAT, H-RESET)"], F["central"], 1.0)
    chk("the register reset floor (%.0f s on 1 m^2, central L*) is gathered over 1e4 times faster than the chemical "
        "deficit ceiling" % _tr, _tr * 1e4 < t, True)
    print("  [STRUCTURAL] t = E/(F A eta): inverse in area, flux and efficiency -- identities of the formula")
    print("\n%d/%d checks pass, %d of them controls; 1 STRUCTURAL printed, not counted" % (n_ok, n_ok + n_bad, n_ctl))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
