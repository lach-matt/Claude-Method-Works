#!/usr/bin/env python3
"""r1_realize.py -- item 490: R1's realizability (opened at 489).

R1 is M's definition: position 2 reconstructs the README with no tolerance.  Item 441 (2) requires a definition to be
realizable.  489 set R1 OPEN because position 2 holds each README mode alone: the mode's partner is kept in the core,
which makes the channel an amplifier.  This instrument settles both halves.  "No tolerance" cannot be realized.  The
realizable form, error below any epsilon chosen in advance, is realized by a computed code.  Labels: computed (exact
unless marked), deduced, READ.

  Z1 (computed, exact; READ) Zero error is impossible at any block length.
     Each README mode arrives as a' = alpha a + beta b^+.  Its gain is G = 1 + |beta|^2 > 1 at every k (passage_est Q5),
     and the partner b is thermal with n = 1/(e^(2 pi k r_h) - 1) > 0.  In quadrature variance (vacuum 1/2) the channel
     is X = sqrt(G), Y = (G - 1)(n + 1/2).  It is exactly the quantum-limited amplifier, Y = (G - 1)/2, followed by
     classical Gaussian noise of variance (G - 1) n > 0.
     That noise smears every output over the displacements, which act irreducibly, on one mode or on many.  So every
     output state is faithful, and no two outputs are orthogonal.  A zero-error code needs orthogonal outputs (Duan,
     Severini and Winter, IEEE Trans. Inf. Theory 59, 1164 (2013), READ), so the zero-error capacity is exactly 0.
     For two orthogonal inputs, the vacuum and one quantum, the outputs overlap by Tr(rho0' rho1') = 2 Y / (G + 2 Y)^2.
     This is zero only for the identity channel; it is 0.0119 to 0.185 across the inflow's band.
  Z2 (computed) The realizable form is realized.  Decode each mode by heterodyne, giving a classical complex Gaussian
     channel at SNR = G n / ((G - 1)(n + 1) + 1), with the inflow's own occupation n as the power.  Gallager's random-
     coding bound for parallel Gaussian channels, P_e <= exp(-(E_0(rho) - rho n_b R)) with E_0 = rho sum ln(1 + SNR_i /
     (1 + rho)), applies at half the heterodyne rate.  Blocks of 6.4e9 modes, drawn with the inflow's spectrum, each
     carrying 2.1e3 of the README's bits, deliver the whole example README (2.74e15 bits) with total error below
     1e-100 (union bound over the blocks).  The cost is rate: heterodyne at half rate recovers a fraction 0.112 of the
     inflow's entropy (0.224 at the full heterodyne rate), against Q5's F = 0.27 (Holevo, which an optimal joint
     measurement reaches).  The write therefore lasts tau_w / 0.112 with this code, and tau_w / F at best.  Computed
     on passage_est's band at mu/l5^2 = 1e6; most of the band's modes are nearly empty, so most of a block is room.
  Z3 (deduced) So R1 as written cannot be realized (Z1), and the form 489 named can (Z2): "position 2 reconstructs the
     README with error below any epsilon > 0 chosen in advance, at a rate below the channel's capacity".  The wording
     is M's to adopt (414).  R1 stays OPEN until M does; with it adopted, R1 stands as a realizable definition under
     441 (2), realized by Z2.

python3 r1_realize.py [--selftest | --mutants]
"""
import os, sys, math, io, contextlib, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
N_EX = 2742570311524972
TARGET = 1e-100


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


_ROWS = {}


def band():
    """passage_est Q5's band at mu/l5^2 = 1e6: (k r_h, |beta|^2, n, Holevo C, g(n)) and the k^3 d ln k weights"""
    if "rows" not in _ROWS:
        PE = _load("passage_est.py", "r1_pe")
        cap = PE.capacity(1e6)
        _ROWS["rows"], _ROWS["F"] = cap["rows"], cap["F"]
    rows = _ROWS["rows"]
    lk = [math.log(r[0]) for r in rows]
    w = [0.0] * len(rows)
    for i in range(len(rows) - 1):                                   # trapezoid weights in ln k, weight k^3
        h = lk[i + 1] - lk[i]
        w[i] += h / 2 * rows[i][0] ** 3; w[i + 1] += h / 2 * rows[i + 1][0] ** 3
    tot = sum(w)
    return rows, [x / tot for x in w], _ROWS["F"]


# ------------------------------------------------------------------ Z1
def zero_error():
    G, n, Y, s = sp.symbols("G n Y s", positive=True)
    Yc = (G - 1) * (n + sp.Rational(1, 2))
    split = sp.simplify(Yc - (G - 1) / 2 - (G - 1) * n) == 0          # quantum-limited part + classical noise (G-1)n
    # characteristic functions (vacuum chi = e^(-|xi|^2/2)): out chi(xi) = chi_in(sqrt(G) xi) e^(-Y |xi|^2)
    over = sp.integrate((1 - G * s) * sp.exp(-(G + 2 * Y) * s), (s, 0, sp.oo))   # Tr(rho0' rho1'), s = |xi|^2
    over = sp.simplify(over)
    ident = sp.simplify(over.subs({G: 1, Y: 0})) == 0
    purity0 = sp.simplify(sp.integrate(sp.exp(-(G + 2 * Y) * s), (s, 0, sp.oo)).subs({G: 1, Y: 0})) == 1
    rows, _, _ = band()
    if "no_partner_noise" in MUT:
        vals = [float(over.subs({G: 1, Y: 0})) for _ in rows]
    else:
        vals = [float(over.subs({G: 1 + r[1], Y: r[1] * (r[2] + 0.5)})) for r in rows]
    return dict(split=split, over=over, ident=ident, purity0=purity0, vals=vals, nmin=min(r[2] for r in rows),
                g_min=min(1 + r[1] for r in rows))


# ------------------------------------------------------------------ Z2
def code():
    rows, w, F = band()
    snr = []
    for kr, b2, n, C, gn in rows:
        G = 1 + b2
        noise = (G - 1) * (n + 1) + (0.0 if "no_het_noise" in MUT else 1.0)
        snr.append(G * n / noise)
    Chet = sum(wi * math.log(1 + x) for wi, x in zip(w, snr))         # nats per mode, the band's mix
    Hin = sum(wi * r[4] for wi, r in zip(w, rows))                    # the inflow's entropy per mode (g(n))
    R = 0.5 * Chet
    rhos = [i / 200 for i in range(1, 201)]
    Er = max(sum(wi * r_ * math.log(1 + x / (1 + r_)) for wi, x in zip(w, snr)) - r_ * R for r_ in rhos)
    bits_per_mode = R / math.log(2)
    def total_err_log10(nb):
        blocks = N_EX / (bits_per_mode * nb)
        return math.log10(blocks) - nb * Er / math.log(10)
    nb = 1000
    while total_err_log10(nb) > math.log10(TARGET):
        nb = int(nb * 1.05) + 1
    return dict(snr=snr, Chet=Chet, Hin=Hin, R=R, Er=Er, nb=nb, err=total_err_log10(nb), frac=R / Hin, F=F,
                frac_full=Chet / Hin, bits_block=nb * bits_per_mode)


def compute():
    return dict(z1=zero_error(), z2=code())


def checks(o):
    z1, z2 = o["z1"], o["z2"]
    G, Y = sp.symbols("G Y", positive=True)
    return [("Z1: the channel is the quantum-limited amplifier then classical noise (G-1) n > 0 (n >= %.2g, G >= %.3g "
             "on the band); Tr(rho0' rho1') = 2Y/(G + 2Y)^2, zero only for the identity, 0.0119 to 0.185 on the band: "
             "no orthogonal outputs, zero-error capacity 0" % (z1["nmin"], z1["g_min"]),
             z1["split"] and sp.simplify(z1["over"] - 2 * Y / (G + 2 * Y) ** 2) == 0 and z1["ident"] and z1["purity0"]
             and z1["nmin"] > 0 and z1["g_min"] > 1 and min(z1["vals"]) > 0
             and "%.3g" % min(z1["vals"]) == "0.0119" and "%.3g" % max(z1["vals"]) == "0.185"),
            ("Z2: heterodyne at half rate, Gallager's bound: blocks of 6.4e9 modes (2.1e3 README bits each) carry the "
             "example README with total error below 1e-100; recovered fraction 0.112 of the inflow's entropy (0.224 at "
             "the full heterodyne rate; Holevo F = 0.27)",
             z2["err"] <= math.log10(TARGET) and "%.2g" % z2["nb"] == "6.4e+09" and "%.2g" % z2["bits_block"] == "2.1e+03"
             and "%.3g" % z2["frac"] == "0.112" and "%.3g" % z2["frac_full"] == "0.224"
             and "%.2f" % z2["F"] == "0.27" and z2["frac"] < z2["F"])]


def report(o=None):
    o = o or compute(); z1, z2 = o["z1"], o["z2"]
    print("r1_realize.py -- R1's realizability (item 490)\n")
    print("Z1 split exact: %s; Tr(rho0' rho1') = %s; identity 0: %s; on the band: %s"
          % (z1["split"], z1["over"], z1["ident"], ", ".join("%.3g" % v for v in z1["vals"])))
    print("Z2 SNR per k: %s; C_het %.4g nats/mode (mix), inflow entropy %.4g; rate %.4g; E_r %.3g; n_b %d; total "
          "error 10^%.1f; %.3g README bits per block; fraction %.3g (half rate), %.3g (full heterodyne), Holevo F %.3f"
          % (", ".join("%.3g" % x for x in z2["snr"]), z2["Chet"], z2["Hin"], z2["R"], z2["Er"], z2["nb"], z2["err"],
             z2["bits_block"], z2["frac"], z2["frac_full"], z2["F"]))


MUTANTS = {"no_partner_noise": "the partner taken as crossing with the mode: the identity channel (Z1)",
           "no_het_noise": "heterodyne's own vacuum noise dropped (Z2)"}


def selftest(quiet=False):
    r_ = checks(compute())
    if not quiet:
        for n_, ok in r_:
            print("  [%s] %s" % ("ok" if ok else "FAIL", n_))
    k = sum(ok for _, ok in r_)
    if not quiet:
        print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        failed = [n_.split(":")[0] for n_, ok in checks(compute()) if not ok]
        MUT.clear()
        caught += bool(failed)
        print("  [%s] %s -> %s" % ("caught" if failed else "MISSED", desc, ", ".join(failed) or "nothing"))
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
