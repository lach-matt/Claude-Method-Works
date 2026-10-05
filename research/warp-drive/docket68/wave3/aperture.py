#!/usr/bin/env python3
"""
aperture.py -- DOCKET 68 wave 3: how big must the corridor be if only information passes?

Not seated.  stdlib only.  Every figure is IMPORTED from its owner (docket66/throatbits, seat, wormhole, measure, nopath,
gravity); nothing outside is newly READ.  M (2026-10-05), verbatim: "If information is what is being sent, how big does
the corridor actually have to be? We assumed 1 meter, but that was for moving matter instead of information".

    python3 aperture.py              report
    python3 aperture.py --selftest   checks, with CONTROLS
    python3 aperture.py --json       the numbers as JSON

THE 1 m FIGURE.  The board's 1 m throat (measure.price_table's 'O-HOLD: wormhole.throat_mass(1 m)') was a size for a
body to pass through.  Information sets the size differently, three ways, each computed for all four of the object's
counts (M, item 33: "Keep all four"):

  (A) ALL AT ONCE -- the whole description held at the throat in one moment.  The smallest throat whose holographic
      capacity A/4 equals the count: throatbits.r_fit (DOCKET 66, imported), r = l_P sqrt(I ln2 / pi), under its named
      hypotheses (H-CAP-AT-THROAT, H-NECK-DOGMA, H-COUNT-IS-ENTROPY).  A ceiling on what a throat that size can hold,
      not an encoding anyone has built.
  (B) STREAMED -- the description sent bit by bit over a schedule T.  One channel mode is enough for any amount of
      information given time.  The board's floor on the energy of sending N bits in time T over one mode is
      seat.channel_floor (LNM eq. 8, one polarisation).  For that 1D thermal channel the energy per nat is kT/2
      (computed here from LNM's own law -- P = pi^2 (kT)^2 / (6h) and dS/dt = (pi^2/3) kT / h per polarisation -- and
      checked against seat.channel_floor), so the channel's characteristic quantum is kT = 2 E_bit / ln 2 and its
      wavelength lambda = h c / kT.  A mode of wavelength lambda passes an opening no narrower than about lambda/2
      (H-HALF-WAVE).  So the streamed corridor's width is set by the SCHEDULE: a faster schedule needs harder quanta and
      a narrower, but not a larger, opening.
  (C) THE COUPLING VIEW (W3A, M items 21-22) -- the corridor as a coupling term has no cross-section at all.  Size is
      replaced by count and time: I couplings in parallel, or one used I times.  One coupling run at the schedule's
      pace needs a coupling energy hbar J = hbar I pi / (2 T) (two-site transfer time pi/2J per qubit, corridor.py).

  WHAT EACH SIZE COSTS AS A THROAT (if the corridor were a geometric throat): wormhole.throat_mass(r) = r c^2/(8 pi G),
  linear in r, against the 1 m figure.  The board's other limits on small throats stand as graded (DOCKET 66: held
  throats; DOCKET 67: the quantum inequalities; Ford-Roman crossover 0.307933 / 5.625229 l_P, M: "Carry both").

NAMED HYPOTHESES
  H-HALF-WAVE     an opening passes a mode of wavelength lambda only if it is at least about lambda/2 wide.
  H-THERMAL-1D    the streamed channel is LNM's 1D thermal channel at the board's floor (seat.channel_floor); its
                  characteristic quantum is kT.  A coded channel could use other quanta at higher energy cost.
  H-CAP-AT-THROAT, H-NECK-DOGMA, H-COUNT-IS-ENTROPY (throatbits.py) for (A).
  H-DIRECT-COUPLING (corridor.py) for (C).
"""
import contextlib
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.abspath(os.path.join(HERE, ".."))
WD = os.path.abspath(os.path.join(D68, ".."))
for _p in (os.path.join(WD, "docket66"), WD, D68):
    if _p not in sys.path:
        sys.path.insert(0, _p)

with contextlib.redirect_stdout(io.StringIO()):
    import throatbits
    import seat
    import wormhole
    import measure
    import nopath

M_WORDS = ("If information is what is being sent, how big does the corridor actually have to be? We assumed 1 meter, "
           "but that was for moving matter instead of information")
H = seat.H
C = seat.C
HBAR = nopath.HBAR
SCHEDULES_S = (86400.0, 3.15576e7, 3.15576e9)     # a day, a year, a century (Julian)


def counts():
    rows, _, _, _ = measure.price_table()
    return [(r["count"], r["bits"]) for r in rows]


# ============================================================================ (A) all at once
def all_at_once():
    return [{"count": n, "bits": b, "r_m": throatbits.r_fit(b), "r_closed_m": throatbits.r_fit_closed(b),
             "throat_mass_kg": wormhole.throat_mass(throatbits.r_fit(b))} for n, b in counts()]


# ============================================================================ (B) streamed
def kT_from_floor(N, T):
    """kT of LNM's 1D one-polarisation channel carrying N bits in time T at the board's floor."""
    E = seat.channel_floor(N, T)["E_1d_one_pol_J"]
    e_nat = E / (N * math.log(2.0))
    return 2.0 * e_nat, E


def lnm_rate_bits(kT):
    """dS/dt = (pi^2/3) kT / h nats/s per polarisation, in bits/s."""
    return (math.pi ** 2 / 3.0) * kT / H / math.log(2.0)


def streamed():
    out = []
    for n, b in counts():
        for T in SCHEDULES_S:
            kT, E = kT_from_floor(b, T)
            lam = H * C / kT
            out.append({"count": n, "bits": b, "T_s": T, "E_J": E, "kT_eV": kT / 1.602176634e-19,
                        "lambda_m": lam, "width_m": lam / 2.0, "throat_mass_kg": wormhole.throat_mass(lam / 2.0),
                        "rate_check": lnm_rate_bits(kT) / (b / T)})
    return out


# ============================================================================ (C) the coupling view
def coupling_view():
    return [{"count": n, "bits": b, "T_s": T, "hbarJ_J": HBAR * b * math.pi / (2.0 * T),
             "hbarJ_eV": HBAR * b * math.pi / (2.0 * T) / 1.602176634e-19}
            for n, b in counts() for T in SCHEDULES_S]


def collect():
    return {"one_metre_throat_mass_kg": wormhole.throat_mass(1.0), "all_at_once": all_at_once(),
            "streamed": streamed(), "coupling": coupling_view(), "l_P_m": throatbits.lp()}


def report():
    d = collect()
    print("How big must the corridor be if only information passes?")
    print('  M: "%s"' % M_WORDS)
    print("\n  the 1 m throat (for a body): wormhole.throat_mass(1 m) = %.3g kg" % d["one_metre_throat_mass_kg"])
    print("\n(A) all at once -- the smallest throat whose A/4 holds the whole description (throatbits.r_fit):")
    for r in d["all_at_once"]:
        print("    %-42s %.3g bits: r = %.3g m (%.3g l_P); throat mass %.3g kg"
              % (r["count"], r["bits"], r["r_m"], r["r_m"] / d["l_P_m"], r["throat_mass_kg"]))
    print("\n(B) streamed over one mode at the board's energy floor (H-THERMAL-1D, H-HALF-WAVE):")
    for r in d["streamed"]:
        if not r["count"].startswith("species") and not r["count"].startswith("grid 0.1"):
            continue
        print("    %-30s T = %9.3g s: quantum %.3g eV, wavelength %.3g m, opening >= %.3g m; throat mass %.3g kg"
              % (r["count"][:30], r["T_s"], r["kT_eV"], r["lambda_m"], r["width_m"], r["throat_mass_kg"]))
    print("    (species and 0.1 A counts shown; --json has all four)")
    print("\n(C) the coupling view (W3A): no cross-section; one coupling at the schedule's pace needs hbar J =")
    for r in d["coupling"]:
        if r["count"].startswith("species"):
            print("    T = %9.3g s: %.3g eV" % (r["T_s"], r["hbarJ_eV"]))


def selftest():
    n_ok = n_bad = n_ctl = 0

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-92s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:92], got))

    print("aperture.py selftest")
    a = all_at_once()
    chk("(A) r_fit by bisection matches the closed form l_P sqrt(I ln2/pi) for every count (to 1e-6)",
        all(abs(r["r_m"] / r["r_closed_m"] - 1) < 1e-6 for r in a), True)
    chk("(A) every all-at-once throat is far below 1 m and far above l_P (1e-24 m < r < 1e-18 m)",
        all(1e-24 < r["r_m"] < 1e-18 for r in a), True)
    s = streamed()
    chk("(B) LNM's 1D law reproduces the floor's own rate: (pi^2/3) kT/h equals N/T (to 1e-3) in every row",
        all(abs(r["rate_check"] - 1) < 1e-3 for r in s), True)
    chk("(B) a slower schedule means softer quanta and a wider (never narrower) opening",
        all(s[i]["width_m"] < s[i + 1]["width_m"] for i in range(0, len(s), 3)), True)
    chk("(B) every streamed opening is below 1 m at every schedule here",
        all(r["width_m"] < 1.0 for r in s), True)
    chk("CONTROL: LNM's 3D law (eq. 6) gives a different rate at the same power -- the kT/2 identity is the 1D law's",
        abs(seat.lnm_rate_3d(1.0, 1.0, 1.0, 1.0) - seat.lnm_rate_1d(1.0, pol=1)) < 1e-9, False, ctl=True)
    chk("throat mass is linear in r: the 1 m figure over a 1e-11 m opening is 1e11 (to 1e-9)",
        abs(wormhole.throat_mass(1.0) / wormhole.throat_mass(1e-11) / 1e11 - 1) < 1e-9, True)
    cv = coupling_view()
    chk("(C) hbar J scales with I/T: a century schedule needs 1/100 of a year's coupling energy (to 1e-9)",
        abs(cv[2]["hbarJ_J"] * 100 / cv[1]["hbarJ_J"] - 1) < 1e-9, True)
    chk("CONTROL: (A)'s radius grows as sqrt(I): 4x the bits, 2x the radius (to 1e-6)",
        abs(throatbits.r_fit(4e28) / throatbits.r_fit(1e28) - 2) < 1e-6, True, ctl=True)
    print("\n%d/%d checks pass, %d of them controls" % (n_ok, n_ok + n_bad, n_ctl))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
