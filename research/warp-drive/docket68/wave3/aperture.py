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
      wavelength lambda = h c / kT.  A hollow single-conductor guide passes a mode only if it is at least about lambda/2
      wide (H-HALF-WAVE, order of magnitude).  So at the floor energy the MINIMUM opening scales as T/I: a faster
      schedule PERMITS a narrower one (any wider opening also passes).  Two caveats, both computed or named:
      (i) at width lambda/2 the cutoff sits exactly at hbar omega = kT, and 61 % of the floor channel's entropy flux
      (47 % of its energy flux) lies below that cutoff -- so a lambda/2 guide cannot carry the floor rate; it needs
      more width or more power (computed here from the 1D Bose integrals); (ii) a two-conductor (TEM) line has no
      cutoff at all (H-TEM-LINE, against the half-wave floor); and the throat-mass column uses the width as a radius --
      a circular guide's TE11 cutoff gives r ~ lambda/3.41 = 0.59 x (lambda/2) (H-TE11, NAMED-NOT-READ).
  (C) THE COUPLING VIEW (W3A, M items 21-22) -- the corridor as a coupling term has no cross-section at all.  Size is
      replaced by count and time: I couplings in parallel, or one used I times.  One coupling run at the schedule's
      pace needs a coupling energy hbar J = hbar I pi / (2 T) (two-site transfer time pi/2J per qubit, corridor.py).

  WHAT EACH SIZE COSTS AS A THROAT (if the corridor were a geometric throat): wormhole.throat_mass(r) = r c^2/(8 pi G),
  linear in r, against the 1 m figure.  The board's other limits on small throats stand as graded (DOCKET 66: held
  throats; DOCKET 67: the quantum inequalities; Ford-Roman crossover 0.307933 / 5.625229 l_P, M: "Carry both").

HISTORY (corrected after the W3A verifier, 2026-10-05): 'a faster schedule needs harder quanta and a narrower, but not
a larger, opening' (it permits a narrower minimum, at the floor energy only); H-HALF-WAVE without its scope or its two
caveats; WAVE3.md's 'the information corridor is between about 1e-21 m and 1e-10 m wide' (these are smallest openings
consistent with each reading, not widths it must have); identities counted as checks; a loop that never compared a year
with a century; a 3D-vs-1D 'control' that did not test the kT/2 identity; M's question not banked for a verbatim check.

NAMED HYPOTHESES
  H-HALF-WAVE     a hollow single-conductor opening passes a mode of wavelength lambda only if at least ~lambda/2 wide
                  (order of magnitude; a lambda/2 guide carries only part of the floor rate -- caveat (i)).
  H-TEM-LINE      a two-conductor line carries a TEM mode with no cutoff: no half-wave floor on its width.
  H-TE11          circular-guide TE11 cutoff lambda_c = 3.41 r (standard waveguide result, NAMED-NOT-READ).
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
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")


def _simpson(f, a, b, n=20000):
    h = (b - a) / n
    tot = f(a) + f(b)
    for i in range(1, n):
        tot += (4 if i % 2 else 2) * f(a + i * h)
    return tot * h / 3.0


def _integral(f, a, b):
    """int_a^b f, with the region below 1e-2 taken on a log scale (x = e^u) for the log singularity at 0."""
    lo = max(a, 1e-14)
    mid = min(b, 1e-2)
    tot = 0.0
    if mid > lo:
        tot += _simpson(lambda u: f(math.exp(u)) * math.exp(u), math.log(lo), math.log(mid), 4000)
    if b > mid:
        tot += _simpson(f, mid, b)
    return tot


def _bose_e(x):
    return x / math.expm1(x)


def _bose_s(x):
    return x / math.expm1(x) - math.log(-math.expm1(-x))


def energy_per_nat(dim):
    """Energy per nat of a thermal photon gas, in units of kT: 1D (one mode family) and 3D (density of states x^2)."""
    w = (lambda x: 1.0) if dim == 1 else (lambda x: x * x)
    E = _integral(lambda x: w(x) * _bose_e(x), 0.0, 60.0)
    S = _integral(lambda x: w(x) * _bose_s(x), 0.0, 60.0)
    return E / S


def below_cutoff_fractions(xc=1.0):
    """1D thermal channel: fractions of entropy and energy flux below hbar omega = xc kT (the lambda/2 guide's cutoff)."""
    s_lo, s_all = _integral(_bose_s, 0.0, xc), _integral(_bose_s, 0.0, 60.0)
    e_lo, e_all = _integral(_bose_e, 0.0, xc), _integral(_bose_e, 0.0, 60.0)
    return s_lo / s_all, e_lo / e_all


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
    print("How big must the corridor be if only information passes?  (smallest opening consistent with each reading)")
    print('  M: "%s"' % M_WORDS)
    print("\n  the 1 m throat (for a body): wormhole.throat_mass(1 m) = %.3g kg" % d["one_metre_throat_mass_kg"])
    print("\n(A) all at once -- the smallest throat whose A/4 holds the whole description (throatbits.r_fit):")
    for r in d["all_at_once"]:
        print("    %-42s %.3g bits: r = %.3g m (%.3g l_P); throat mass %.3g kg"
              % (r["count"], r["bits"], r["r_m"], r["r_m"] / d["l_P_m"], r["throat_mass_kg"]))
    fs, fe = below_cutoff_fractions()
    print("\n(B) streamed over one mode at the board's energy floor (H-THERMAL-1D, H-HALF-WAVE; smallest openings):")
    print("    caveat: at width lambda/2 the cutoff is hbar omega = kT; %.0f%% of the entropy flux and %.0f%% of the "
          "energy flux lie below it" % (100 * fs, 100 * fe))
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
    structural = []
    txt = " ".join(open(RULINGS, encoding="utf-8").read().split())
    chk("M's question (rulings item 35) found verbatim in the rulings file", M_WORDS in txt, True)
    a = all_at_once()
    chk("(A) r_fit by bisection matches the closed form l_P sqrt(I ln2/pi) for every count (to 1e-6)",
        all(abs(r["r_m"] / r["r_closed_m"] - 1) < 1e-6 for r in a), True)
    chk("(A) every all-at-once throat is far below 1 m and far above l_P (1e-24 m < r < 1e-18 m)",
        all(1e-24 < r["r_m"] < 1e-18 for r in a), True)
    s = streamed()
    chk("(B) LNM's 1D law reproduces the floor's own rate: (pi^2/3) kT/h equals N/T (to 1e-3) in every row",
        all(abs(r["rate_check"] - 1) < 1e-3 for r in s), True)
    chk("(B) every streamed opening is below 1 m at every schedule here", all(r["width_m"] < 1.0 for r in s), True)
    e1, e3 = energy_per_nat(1), energy_per_nat(3)
    chk("(B) the 1D thermal channel's energy per nat is kT/2 (to 1e-4), from the Bose integrals", abs(e1 - 0.5) < 1e-4,
        True)
    chk("CONTROL: the 3D photon gas's energy per nat is 3kT/4, not kT/2 -- the identity is the 1D law's (to 1e-4)",
        (abs(e3 - 0.75) < 1e-4, abs(e3 - 0.5) < 1e-4), (True, False), ctl=True)
    fs, fe = below_cutoff_fractions()
    chk("(B) caveat (i): at width lambda/2 a substantial share of the floor channel lies below cutoff (entropy %.2f, "
        "energy %.2f)" % (fs, fe), (0.5 < fs < 0.7, 0.4 < fe < 0.55), (True, True))
    chk("CONTROL: with the cutoff at 10 kT (a much narrower guide) almost all of the channel is below cutoff",
        below_cutoff_fractions(10.0)[0] > 0.99, True, ctl=True)
    structural.append("slower schedule -> wider minimum opening, throat mass linear in r, hbar J ~ I/T, r_fit ~ sqrt(I): "
                      "algebraic identities of the formulas as written")
    for x in structural:
        print("  [STRUCTURAL] " + x)
    print("\n%d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted"
          % (n_ok, n_ok + n_bad, n_ctl, len(structural)))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
