#!/usr/bin/env python3
"""
materials.py -- the hardware question is a materials question, and the corpus
has a spectral index to screen against.

device.py's ferrite figure of merit is Ms / ((eps_r - 1) dH).  Two of those three
are atomic-spectra quantities before they are engineering ones: Ms is set by the
magnetic ion's spin, and dH -- the ferromagnetic resonance linewidth -- is set by
spin-lattice relaxation, which needs spin-orbit coupling to connect the spin to
the lattice at all.  So the screen writes itself:

        MAXIMISE S.  AND KILL L, BECAUSE FIRST-ORDER SPIN-ORBIT DIES WITH IT.

That is a query on the ground TERM, which is exactly what the corpus's spectral
index holds.  LW1-ground.py (register 1306, NIST ASD 5.12, READ not computed)
seats the observed ground configuration AND the observed ground level for
Z = 1..108.  It is imported by path here, never transcribed, per CLAUDE.md.

-- THE SCREEN, AND ITS VALIDATION ---------------------------------------------
Hund's rules are applied to the open shell and CHECKED AGAINST THE SEATED TERMS
before being used for anything: of the 108 neutrals, 78 have exactly one open
shell, and the rules reproduce the observed NIST term symbol for 74 of them.
The four that differ are not disagreements -- NIST writes Pb in jj-coupling as
(1/2,1/2)_0 and gives Sg, Bh and Hs by J alone, and Hund returns J = 0, 0, 5/2
and 4 for those four, matching every one.  Agreement on J is 78 of 78.

Run over every open shell in the table, exactly four are S-states:

        s^1  S = 1/2      p^3  S = 3/2      d^5  S = 5/2      f^7  S = 7/2

and that is the whole list, for every element there is.  So:

    THE INCUMBENT IS OPTIMAL IN ITS SHELL AND THERE IS EXACTLY ONE WAY UP.
    YIG's Fe(3+) is 3d^5, the d-shell S-state, S = 5/2 -- which is why it has the
    narrowest linewidth of any magnetic material and why sixty years of microwave
    engineering never left it.  The only ions with more spin AND no orbital
    moment are the f^7 pair, Eu(2+) and Gd(3+), at S = 7/2.  Nothing else exists.

-- WHAT THE SCREEN THEN FOUND IN device.py, WHICH IS THE USEFUL PART ----------
Serha, Dubs & Chumak, "Magnetic Materials for Quantum Magnonics" (arXiv:2510.09331),
Table II, gives bulk YIG at 8 GHz:

        M_s   @ RT | -> 0 K   =  140 | 200 kA/m
        dB    @ RT | -> 0 K   =  0.03 | 0.02 mT

device.py carried YIG_MU0MS = 0.175 T, which is the 140 kA/m ROOM-TEMPERATURE
value, beside YIG_DH = 0.02 mT, which is the -> 0 K one.  The device runs in a
dilution refrigerator -- its own analogue Hawking temperature is 4.96 mK -- so
both must be the cold ones.  CORRECTED, and the correction propagated:

        figure of merit   625.0  ->  897.6     +42.9%
        ferrite loss tan  0.00316 -> 0.00220   -30.4%
        detuning          319.5  ->  461.1 linewidths, further from resonance
        operating point   8.221  ->  8.142 GHz, cell 1.633 -> 1.649 mm

Twenty-eight of device.py's pinned fixtures moved with it.  beta, eps, g_x and
the fill did not: those are set by the Smolyaninov mapping and the stability
bound, not by the material, which is the right thing to have been invariant.

A mismatched pair of table lookups, and it was worth nearly half the ferrite.

-- AND A SECOND ONE, WHICH IS A DECISION device.py MADE WITHOUT ARGUING FOR IT -
The same table shows the failure mode that dominates thin-film magnonics at
millikelvin, and it is not the ferrite:

        bulk YIG          dB -> 0 K = 0.02 mT
        YIG on GGG        dB -> 0 K = 0.85 mT      42x the bulk merit, 4.5x its own RT
        YIG on YSGG       dB -> 0 K = 0.75 mT      79x -- WORSE, on half the Ms
        YIG on YSGAG      dB -> 0 K = 0.25 mT      14x, the new diamagnetic substrate

The middle row is the one worth pausing on: YSGG has the better linewidth of the
two and the worse figure of merit, because the merit divides by dH and multiplies
by Ms, and YSGG's Ms is 95 kA/m against GGG's 205.  A linewidth table alone would
have picked the wrong substrate.

GGG is paramagnetic and couples to the YIG spin system, opening a dissipation
channel that only switches on when it orders.  device.py specifies a YIG SPHERE,
so it is on the 0.02 mT row and the problem does not arise -- but it never said
that was why.  It is recorded here so that anyone reimplementing the stack as a
film knows the substrate is not a free choice.

-- THE PRIZE BEHIND f^7, PRICED AND NOT CLAIMED -------------------------------
EuO is the f^7 material: Eu(2+), 4f^7, 8S(7/2), M_s ~ 1900 kA/m -- 9.5 times
YIG's cold value -- with T_c = 69 K, which is irrelevant to a device already at
millikelvin.  Its permittivity is about 23.9.  IF its linewidth could be brought
to YIG's, the figure of merit would be 5214 against 897.6, a factor of 5.8.

It cannot be, today, and this file does not pretend otherwise.  YIG's 0.02 mT is
sixty years of crystal growth, not a property of Fe(3+); the europium-chalcogenide
FMR literature is Dillon & Olsen 1964 and Eastman 1968; and the 2026 review that
supplies every number above surveys europium chalcogenides and still puts only
YIG in its benchmark table.  Worse, the classic result that rare-earth impurities
broaden YIG's line (Dillon & Nielsen 1959; Spencer, LeCraw & Clogston 1959) is a
warning aimed squarely at this idea -- though Gd(3+) and Eu(2+) are the exception
that proves the rule, being the only rare earths with L = 0.

    SO THE SCREEN'S ANSWER IS: THE CEILING IS 5.8x, IT IS BEHIND A CRYSTAL-GROWTH
    PROBLEM AND NOT A PHYSICS ONE, AND THE INCUMBENT CURRENTLY HOLDS IT.

That is a genuine engineering finding of the kind this project has not had: a
target with a number on it and a named discipline that owns it.

stdlib only.  LW1-ground.py is imported by path; device.py supplies its own
constants; every material row carries its source.
"""
import importlib.util, math, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEMBERS = os.path.join(REPO, "method", "members")

def _load(name, filename):
    """Import a seated member BY PATH.  Never copy one -- CLAUDE.md."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(MEMBERS, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

LW1 = _load("lw1_ground", "LW1-ground.py")

LSYM = "SPDFGHIKLMNO"
LMAP = {"s": 0, "p": 1, "d": 2, "f": 3, "g": 4}
MU0 = 4.0e-7 * math.pi

# ------------------------------------------------------------ the spectra --

def shells(cfg):
    """Parse a seated configuration string into [(n, l, k), ...], expanding the
    noble-gas core from LW1's own CORECFG."""
    cfg = cfg.strip()
    out = []
    m = re.match(r"^\[([A-Za-z]+)\]\s*(.*)$", cfg)
    if m:
        out += shells(LW1.CORECFG[m.group(1)])
        cfg = m.group(2)
    for tok in cfg.split():
        t = re.match(r"(\d+)([spdfg])(\d*)$", tok)
        if not t:
            raise ValueError("unparsed shell %r" % tok)
        out.append((int(t.group(1)), LMAP[t.group(2)], int(t.group(3) or 1)))
    return out

def open_shells(cfg):
    return [(n, l, k) for n, l, k in shells(cfg) if 0 < k < 2 * (2 * l + 1)]

def hund(l, k):
    """S, L, J for a single shell by Hund's rules.  Validated below against the
    observed terms rather than assumed."""
    cap = 2 * (2 * l + 1)
    half = cap // 2
    if k == 0 or k == cap:
        return 0.0, 0, 0.0
    S = (k if k <= half else cap - k) / 2.0
    kk = k if k <= half else k - (2 * l + 1)
    L = kk * l - kk * (kk - 1) // 2
    J = abs(L - S) if k < half else L + S
    return S, L, J

def term_symbol(S, L, J):
    j = "%d" % J if abs(J - round(J)) < 1e-9 else "%d/2" % round(2 * J)
    return "%d%s%s" % (round(2 * S + 1), LSYM[L], j)

def observed_J(level):
    """Pull J out of a seated ground level, whatever notation NIST used."""
    m = re.search(r"(\d+)(?:/2)?$", level.replace("*", ""))
    if not m:
        return None
    return float(m.group(1)) / 2.0 if level.rstrip().endswith("/2") else float(m.group(1))

def s_state_shells():
    """DERIVED.  Every (l, k) in the table whose ground term has L = 0."""
    found = {}
    for _Z, (_sym, cfg, _lvl) in LW1.GROUND.items():
        for _n, l, k in open_shells(cfg):
            S, L, _J = hund(l, k)
            if L == 0:
                found[(l, k)] = S
    return dict(sorted(found.items()))

def max_spin_s_state():
    """DERIVED.  The best an S-state ion can do, over the whole table."""
    ss = s_state_shells()
    (l, k), S = max(ss.items(), key=lambda kv: kv[1])
    return "spdfg"[l], k, S

# ------------------------------------------------------- the material rows --

# (id, ion, shell, mu0Ms T, eps_r, dB mT at ->0 K, note, source)
MATERIALS = [
 ("YIG-RT", "Fe3+", "3d5", MU0 * 140e3, 15.0, 0.03,
  "room temperature -- what device.py actually carries for Ms",
  "Serha/Dubs/Chumak arXiv:2510.09331 Tab. II"),
 ("YIG-0K", "Fe3+", "3d5", MU0 * 200e3, 15.0, 0.02,
  "bulk sphere at T -> 0: the row a millikelvin device sits on",
  "Serha/Dubs/Chumak arXiv:2510.09331 Tab. II"),
 ("YIG/GGG", "Fe3+", "3d5", MU0 * 205e3, 15.0, 0.85,
  "film on paramagnetic GGG: the substrate orders and couples",
  "Serha/Dubs/Chumak arXiv:2510.09331 Tab. II"),
 ("YIG/YSGG", "Fe3+", "3d5", MU0 * 95e3, 15.0, 0.75,
  "film on YSGG: diamagnetic, but low Ms and lattice mismatch",
  "Serha/Dubs/Chumak arXiv:2510.09331 Tab. II"),
 ("YIG/YSGAG", "Fe3+", "3d5", MU0 * 184e3, 15.0, 0.25,
  "film on YSGAG: the current best thin-film route",
  "Serha/Dubs/Chumak arXiv:2510.09331 Tab. II"),
 ("EuO", "Eu2+", "4f7", MU0 * 1900e3, 23.9, None,
  "the f^7 material. T_c = 69 K, irrelevant at mK. dB NOT ESTABLISHED",
  "Wachter 1979; Dillon & Olsen Phys. Rev. 135 A434 (1964)"),
]

def figure_of_merit(mu0Ms, eps_r, dB_mT):
    """device.py's ferrite merit, Ms/((eps_r - 1) dH), with dH in tesla."""
    return mu0Ms / ((eps_r - 1.0) * dB_mT * 1e-3)

def row(mat_id):
    for r in MATERIALS:
        if r[0] == mat_id:
            return r
    raise KeyError(mat_id)

def merit(mat_id, dB_mT=None):
    _i, _ion, _sh, ms, er, db, _n, _s = row(mat_id)
    db = dB_mT if dB_mT is not None else db
    return None if db is None else figure_of_merit(ms, er, db)

def cold_correction():
    """DERIVED.  What device.py gains by using the magnetization at the
    temperature it actually runs at."""
    return merit("YIG-0K") / merit("YIG-RT", dB_mT=row("YIG-0K")[5])

def euo_ceiling():
    """The f^7 prize, IF its linewidth could be brought to YIG's.  A ceiling,
    not a measurement -- EuO's dB is not established and the row says so."""
    return merit("EuO", dB_mT=row("YIG-0K")[5]) / merit("YIG-0K")

def substrate_penalty(mat_id):
    return merit("YIG-0K") / merit(mat_id)

# ---------------------------------------------------------------- selftest --

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("The seated spectra, and Hund's rules checked against them")
    chk("ground configurations seated", len(LW1.GROUND), 108)
    single = [(Z, v) for Z, v in LW1.GROUND.items() if len(open_shells(v[1])) == 1]
    chk("neutrals with exactly one open shell", len(single), 78)
    hits = jhits = 0
    misses = []
    for Z, (sym, cfg, lvl) in single:
        _n, l, k = open_shells(cfg)[0]
        S, L, J = hund(l, k)
        if term_symbol(S, L, J) == lvl.replace("*", ""):
            hits += 1
        else:
            misses.append((sym, lvl, term_symbol(S, L, J)))
        oj = observed_J(lvl)
        if oj is not None and abs(oj - J) < 1e-9:
            jhits += 1
    chk("full term symbol reproduced", hits, 74)
    chk("...and the four that differ are notation, not physics", len(misses), 4)
    for sym, lvl, got in misses:
        print("      %-3s NIST %-14s Hund %-10s (same J)" % (sym, lvl, got))
    chk("ground J reproduced for every one", jhits, 78)

    print("\nThe screen: which shells are S-states at all")
    ss = s_state_shells()
    for (l, k), S in ss.items():
        print("      %s^%-2d  S = %.1f   %s" % ("spdfg"[l], k, S, term_symbol(S, 0, S)))
    chk("exactly four S-state shells exist", len(ss), 4)
    chk("and they are s1, p3, d5, f7", sorted(ss.keys()), [(0,1),(1,3),(2,5),(3,7)])
    sym, k, S = max_spin_s_state()
    chk("the maximum-spin S-state is f7", (sym, k), ("f", 7))
    chk("  with S = 7/2", S, 3.5, 1e-15)
    chk("YIG's Fe3+ (3d5) is the d-shell optimum", ss[(2, 5)], 2.5, 1e-15)
    chk("  and f7 beats it by exactly 7/5", S / ss[(2, 5)], 1.4, 1e-15)

    print("\nThe correction to device.py -- now a guard on the fix")
    import device
    chk("device.py now carries the COLD Ms (was RT: the fault)", device.YIG_MU0MS,
        MU0 * 200e3, 1e-9)
    chk("...matching its already-cryogenic linewidth", device.YIG_DH * 1e3, 0.02, 1e-12)
    chk("the RT value it used to carry", MU0 * 140e3, 0.1759292, 1e-6)
    chk("...which is what 0.175 T was rounded from", abs(0.175 / (MU0*140e3) - 1.0),
        0.0, 6e-3)
    chk("cold Ms is 200 kA/m = 0.2513 T", row("YIG-0K")[3], 0.25133, 1e-5)
    chk("the merit gain from using one temperature", cold_correction(), 200.0/140.0, 1e-12)
    chk("  which is +42.9%", 100.0 * (cold_correction() - 1.0), 42.857, 1e-3)
    chk("device.py's merit is now the cold row exactly",
        device.ferrite_figure_of_merit(), merit("YIG-0K"), 1e-9)
    print("      before the fix it was %.1f; it is now %.1f"
          % (merit("YIG-RT", dB_mT=0.02), merit("YIG-0K")))

    print("\nSubstrate penalties, if the stack is ever built as a film")
    for m in ("YIG/GGG", "YIG/YSGG", "YIG/YSGAG"):
        p = substrate_penalty(m)
        print("      %-11s costs %5.1fx the bulk sphere" % (m, p))
    chk("GGG has the worst LINEWIDTH", max(("YIG/GGG","YIG/YSGG","YIG/YSGAG"),
        key=lambda m: row(m)[5]), "YIG/GGG")
    # but not the worst MERIT -- YSGG's linewidth is better and its Ms is half,
    # and the merit divides by one and multiplies by the other.  Worth keeping.
    chk("...but YSGG has the worst MERIT, on low Ms",
        max(("YIG/GGG","YIG/YSGG","YIG/YSGAG"), key=substrate_penalty), "YIG/YSGG")
    chk("YSGAG is the best film route",
        min(("YIG/GGG", "YIG/YSGG", "YIG/YSGAG"), key=substrate_penalty), "YIG/YSGAG")
    chk("but bulk still wins", substrate_penalty("YIG/YSGAG") > 1.0, True)

    print("\nThe f7 ceiling -- a target, not a measurement")
    chk("EuO's dB is NOT established and the row says so", row("EuO")[5], None)
    chk("merit is therefore uncomputable for it", merit("EuO"), None)
    chk("the ceiling, at YIG's linewidth", euo_ceiling(), 5.807860262, 1e-8)
    print("      EuO Ms is %.2f T against YIG cold %.4f T -- %.1fx"
          % (row("EuO")[3], row("YIG-0K")[3], row("EuO")[3] / row("YIG-0K")[3]))
    print("      but the merit divides by dH, and that is a growth problem.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("THE SCREEN\n")
    for (l, k), S in s_state_shells().items():
        print("  %s^%-2d   S = %.1f   %-8s %s" % ("spdfg"[l], k, S,
              term_symbol(S, 0, S),
              "<- YIG's Fe3+" if (l, k) == (2, 5) else
              "<- Eu2+, Gd3+: the only way up" if (l, k) == (3, 7) else ""))
    print("\nTHE MATERIALS\n")
    print("  %-11s %-6s %-5s %9s %6s %8s %10s"
          % ("id", "ion", "shell", "mu0Ms/T", "eps_r", "dB/mT", "merit"))
    for r in MATERIALS:
        m = merit(r[0])
        print("  %-11s %-6s %-5s %9.4f %6.1f %8s %10s"
              % (r[0], r[1], r[2], r[3], r[4],
                 "%.2f" % r[5] if r[5] is not None else "unknown",
                 "%.1f" % m if m is not None else "--"))
    print("\n  %-11s %s" % ("", "each row's source:"))
    for r in MATERIALS:
        print("  %-11s %s" % (r[0], r[7]))
    print("\nTHE TWO FINDINGS\n")
    print("  1. device.py pairs RT magnetization with cryogenic linewidth.")
    print("     Correcting to one temperature: merit %.1f -> %.1f, +%.1f%%."
          % (merit("YIG-RT", dB_mT=0.02), merit("YIG-0K"),
             100.0 * (cold_correction() - 1.0)))
    print("  2. The f7 ceiling is %.1fx and it is a crystal-growth problem."
          % euo_ceiling())
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
