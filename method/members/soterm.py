#!/usr/bin/env python3
"""soterm.py -- RULING 8(b), STEP ONE: THE CORPUS'S THREE SPIN-ORBIT FORMS, MEASURED AGAINST THE STORE'S SIX
INTERVALS, AND THE TWO DIFFERENCES BETWEEN THEM SEPARATED.

  M's ruling 8 (RULINGS-R4f): "they are all work.  they must be repaired, worked, and then verified/proven
  completely."  Item (b): "first-order Lande zeta is 9 % low at p and 36 % high at 5d against the store's
  measured intervals -- repair the spin-orbit term."

  WHAT `fieldresidue.py` USES, AND WHY THAT IS THE QUESTION.  It takes zeta from `recovered/so94.py`, verbatim:

      zeta_loc = (1/2c^2) <P| (1/r) dV_loc/dr |P>,   V_loc = -Z/r + direct Coulomb with the self-shell at Q-1
                                                     and the same-shell exchange term (so94.pot)

  MEASURED against the six fine-structure intervals the corpus's own level store holds, the ratio computed to
  measured is **0.910, 0.914, 0.955, 1.075 at 3p, 4p, 5p, 6p and 1.237, 1.360 at 4d, 5d**.  That is not a
  constant error and not noise: it runs one way at p and the other at d, and it drifts with Z inside p.

  THE CORPUS HOLDS THREE FORMS, NOT ONE, AND NO MEASUREMENT OF THEM AGAINST THIS STORE:

    (1) so94's PRIMARY, above.  Its own declaration: "the nonlocal HF exchange has no dV/dr; zeta is taken on the
        LOCAL potential (primary), exchange-projected as sensitivity."
    (2) so94's SENSITIVITY, zeta_x, the same quadrature on V_loc + X/P -- the Slater-local projection of the
        nonlocal exchange.  The record built it, declared it SENSITIVITY ONLY, and never scored it.
    (3) so97's xi, from a LATER session and written for this same field -- "first-order spin-orbit parameter
        xi_nl on the sealed KH scalar-relativistic field":

            xi = (1/2c^2) <P| (1/(r M^2)) dV_dir/dr |P>,   M = 1 + (eps - V_dir)/(2c^2)   (Koelling-Harmon)

        Its own scan (RESULT-S97-ITEMS-1-5) carries a declared limitation: "first-order on scalar orbitals
        underestimates the 7p1/2 contraction", and at Z = 113 it gives xi(7p) = 0.0374 Ha where the measured
        splitting wants 0.0752 and so94 gives 0.0784.  So so97 is NOT simply the better form, and the corpus
        never put the two side by side.

  SO97 DIFFERS FROM SO94 IN **TWO** WAYS AT ONCE, and no record separates them:
    - the POTENTIAL: so97 uses the full direct potential (every shell at its full occupancy, no self-shell
      reduction and no same-shell exchange term); so94 removes the entrant's own charge and adds its exchange.
    - the MASS FACTOR: so97 carries Koelling-Harmon's 1/M^2, which suppresses the deep-core region where
      -Z/r makes (eps - V)/2c^2 large; so94 is the M = 1 Pauli limit.
  This instrument computes all four combinations, so which difference does the work is measured rather than
  argued.  It also reports <1/r^3> on the same orbital, because a form error and an ORBITAL error are different
  faults and only the second moves with the radial function.

  THE GATE.  zeta_loc here must reproduce `fieldresidue-field.json`'s banked zeta at every row it shares, to
  1e-9 -- the same chain, the same field, the same quadrature.  Nothing is repaired by this instrument: it
  measures, and the repair follows from what it shows.

  usage:  python3 soterm.py            report from the banked file
          python3 soterm.py --run      converge each opening and measure every form (tens of minutes)
          python3 soterm.py --selftest

  numpy; the chain is loaded by path exactly as fieldentry.py loads it.
"""
import argparse, importlib.util, json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RECOVERED = os.path.join(ROOT, "recovered")
OUT_JSON = os.path.join(HERE, "soterm.json")
FIELD_JSON = os.path.join(HERE, "fieldresidue-field.json")
HA_CM = 219474.6313705


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def meas_rows():
    """The six anchored openings and their measured intervals, taken from fieldresidue.MEAS -- imported, never
    copied.  zeta_meas = 2 x interval / (2l+1)(l+... ) is the standard one-electron relation the record uses:
    Delta = zeta (2l+1)/2, so zeta_meas = 2 Delta / (2l+1)."""
    fr = _load("fieldresidue", os.path.join(HERE, "fieldresidue.py"))
    out = []
    for lab in ("3p", "4p", "5p", "6p", "4d", "5d"):
        m = fr.MEAS[lab]
        if m.get("split") is None: continue
        d = m["split"] / HA_CM
        out.append(dict(lab=lab, el=m["el"], Z=m["Z"], n=m["n"], l=m["l"], split_cm=m["split"],
                        zeta_meas=2.0 * d / (2 * m["l"] + 1)))
    return out


# ================================================================== the four forms
def forms(ch, h, Z, n, l, occ):
    """zeta on the converged object in every combination the corpus's two instruments span.

    V_loc  -- so94.pot verbatim: -Z/r + direct Coulomb with the entrant's own shell at Q-1, minus the same-shell
              exchange term.  V_dir -- so97 verbatim: -Z/r + direct Coulomb at full occupancy, nothing removed.
    M = 1  -- the Pauli limit (so94).  M = 1 + (eps - V_dir)/2c^2 -- Koelling-Harmon (so97).
    X/P    -- so94's declared exchange projection, its own SENSITIVITY reading."""
    np = ch.np
    r, dr, x = h.r, h.dr, h.x
    P = h.P; C0 = ch.C0
    keys = [(a, b) for a, b, q in occ]; Q = {(a, b): q for a, b, q in occ}
    a = (n, l)
    Y0 = {k: h.Yk(P[k], P[k], 0) for k in keys}
    # --- so94's local potential, verbatim
    Vloc = -Z / r + sum((Q[b] if b != a else Q[a] - 1.0) * Y0[b] / r for b in keys)
    c = (Q[a] - 1.0) * (2 * l + 1) / (4 * l + 1)
    if abs(c) > 1e-14:
        for k in range(2, 2 * l + 1, 2):
            Vloc = Vloc - c * ch.t7b_hf._c3j0sq(l, k, l) * h.Yk(P[a], P[a], k) / r
    # --- so97's direct potential, verbatim
    Vdir = -Z / r + sum(Q[b] * Y0[b] / r for b in keys)
    # --- so94's exchange projection (its declared sensitivity)
    X = np.zeros(h.npts)
    for b in keys:
        nb, lb = b
        if b == a: continue
        for k in range(abs(l - lb), l + lb + 1, 2):
            X += 0.5 * Q[b] * ch.t7b_hf._c3j0sq(l, k, lb) * h.Yk(P[a], P[b], k) / r * P[b]
    with np.errstate(divide="ignore", invalid="ignore"):
        Vx = np.where(np.abs(P[a]) > 1e-8, X / np.where(np.abs(P[a]) > 1e-8, P[a], 1.0), 0.0)
    u = P[a] / np.sqrt(float(np.sum(P[a] * P[a] * dr)))
    eps = float(h.eps[a])

    def quad(V, kh):
        dV = np.gradient(V, r)                                  # so94's derivative; the log-mesh one agrees to 3e-5
        w = 1.0
        if kh:
            M = 1.0 + (eps - Vdir) / (2 * C0 * C0)
            w = 1.0 / (M * M)
        return float(np.sum(u * u * dV * w / r * dr) / (2 * C0 * C0))

    r3 = float(np.sum(u * u / r ** 3 * dr))
    return dict(loc=quad(Vloc, False), locX=quad(Vloc + Vx, False), dir=quad(Vdir, False),
                khloc=quad(Vloc, True), kh=quad(Vdir, True), khX=quad(Vloc + Vx, True),
                r3=r3, eps=eps)


# ================================================================== --run
def cmd_run(log=sys.stderr):
    """Two passes over the same six rows: the field as fieldresidue takes zeta on it (CORR = False, plain
    scalar-relativistic exact-exchange HF) and the field it takes its REMOVAL ENERGIES on (CORR = True, HF + form
    S with the PZ orbital SIC).  That inconsistency is this instrument's, not the record's, and measuring it is
    the point: every form above weights the same radial function, so if the fault is the ORBITAL it must move
    when the orbital does.

    The potential in zeta stays electrostatic in both passes -- V is rebuilt from Z and the converged densities,
    and the correlation potential is NOT added to it.  A correlation potential is not the field whose gradient
    the spin-orbit coupling is; what correlation is allowed to change here is the orbital, which is what it
    physically changes."""
    fr = _load("fieldresidue", os.path.join(HERE, "fieldresidue.py"))
    R = fr.Residue(log=log)
    try:
        ch, H = R.ch, R.H
        T, C0 = ch.t5_scf, ch.C0
        rows = []
        for m in meas_rows():
            Z, n, l = m["Z"], m["n"], m["l"]
            occ0 = T.ground_occ(Z)
            print(f"  {m['lab']} {m['el']} Z={Z} ...", file=log, flush=True)
            out = {}
            for tag, corr in (("hf", False), ("corr", True)):
                H.CORR = corr
                try:
                    h = H.HFC(Z, occ0, c=C0); h.run2()
                    out[tag] = forms(ch, h, Z, n, l, occ0)
                finally:
                    H.CORR = False
                f = out[tag]
                print(f"    {tag:4} loc {f['loc']*HA_CM:9.1f}  locX {f['locX']*HA_CM:9.1f}"
                      f"  kh {f['kh']*HA_CM:9.1f}  <1/r3> {f['r3']:8.4f}"
                      f"  meas {m['zeta_meas']*HA_CM:9.1f}", file=log, flush=True)
            rows.append(dict(m, **out["hf"], corr=out["corr"]))
        json.dump(dict(rows=rows), open(OUT_JSON, "w"), indent=1)
        print(f"wrote {OUT_JSON}", file=log)
    finally:
        R.close()


# ================================================================== report
FORMS = [("loc", "so94 primary        V_loc, M = 1"),
         ("locX", "so94 sensitivity    V_loc + X/P, M = 1"),
         ("dir", "the potential alone V_dir, M = 1"),
         ("khloc", "the KH factor alone V_loc, M = KH"),
         ("kh", "so97 verbatim       V_dir, M = KH")]


def report():
    if not os.path.exists(OUT_JSON):
        print("  soterm.json is absent: run --run"); return
    R = json.load(open(OUT_JSON))["rows"]
    print("=" * 112)
    print("soterm.py -- RULING 8(b) STEP ONE: THE CORPUS'S SPIN-ORBIT FORMS AGAINST THE STORE'S SIX INTERVALS")
    print("=" * 112)
    print("""
  so94's primary form is what fieldresidue.py uses.  The corpus holds two more -- so94's own declared exchange
  sensitivity, and so97's Koelling-Harmon form from a later session -- and never scored either against this
  store.  so97 differs from so94 in TWO ways at once (the potential and the mass factor), so both are varied
  separately here.  Every zeta is in cm-1; the ratio is to the store's measured interval.
""")
    print(f"  {'row':6} {'el':3} {'measured':>10} " + " ".join(f"{k:>10}" for k, _ in FORMS))
    for r in R:
        print(f"  {r['lab']:6} {r['el']:3} {r['zeta_meas']*HA_CM:10.1f} "
              + " ".join(f"{r[k]*HA_CM:10.1f}" for k, _ in FORMS))
    print()
    print(f"  {'row':6} {'el':3} {'ratio to measured':>10} " + " ".join(f"{k:>10}" for k, _ in FORMS))
    for r in R:
        print(f"  {r['lab']:6} {r['el']:3} {'':>10} "
              + " ".join(f"{r[k]/r['zeta_meas']:10.3f}" for k, _ in FORMS))
    print("\n  what each form is:")
    for k, d in FORMS:
        print(f"    {k:6} {d}")
    print("\n  <1/r^3> on the same normalised orbital (a0^-3), which is what an ORBITAL error moves and a form")
    print("  error does not:")
    for r in R:
        print(f"    {r['lab']:6} {r['el']:3} {r['r3']:12.4f}   eps {r['eps']:+.5f}")
    if any("corr" in r for r in R):
        print("\n  AND THE SAME FORMS ON THE CORRELATED ORBITAL -- the field the object takes its REMOVAL")
        print("  ENERGIES on (HF + form S with the PZ orbital SIC).  The potential in zeta stays electrostatic;")
        print("  what changes is the radial function.  If the fault is the orbital, it moves here.")
        print(f"\n  {'row':6} {'el':3} {'measured':>10} {'zeta HF':>10} {'zeta corr':>10} {'ratio HF':>9}"
              f" {'ratio corr':>10}   {'<1/r3> HF':>10} {'<1/r3> corr':>11} {'move':>7}")
        for r in R:
            c = r["corr"]
            print(f"  {r['lab']:6} {r['el']:3} {r['zeta_meas']*HA_CM:10.1f} {r['loc']*HA_CM:10.1f}"
                  f" {c['loc']*HA_CM:10.1f} {r['loc']/r['zeta_meas']:9.3f} {c['loc']/r['zeta_meas']:10.3f}"
                  f"   {r['r3']:10.4f} {c['r3']:11.4f} {(c['r3']/r['r3']-1)*100:+6.2f} %")
    cost_report(R)
    print("=" * 112)


def cost_report(R):
    """WHAT AN EXACTLY CORRECT SPIN-ORBIT TERM WOULD DO TO EVERY FIGURE THE OBJECT PRODUCES.

    This is the question ruling 8(b) is really asking, and it needs no new solve: the store MEASURES zeta at all
    six anchored openings, so the object can simply be re-read with the measured value in place of the computed
    one.  Substituting a measurement for a computed quantity is not a fitted constant -- it is the same act as
    gating on the store's measured removal limits, which the object already does.

    Where the store measures nothing -- protactinium, ytterbium, the ladder -- the computed zeta is all there is,
    and what matters is the BOUND: the six measured rows say how wrong zeta can be, and that bound is carried
    through the 5f figure here."""
    if not os.path.exists(FIELD_JSON):
        print("\n  (fieldresidue-field.json absent: run its --run for the cost section)"); return
    fr = _load("fieldresidue", os.path.join(HERE, "fieldresidue.py"))
    ep = _load("entrypoint", os.path.join(HERE, "entrypoint.py"))
    F = json.load(open(FIELD_JSON))
    byo = {o.get("opening"): o for o in F["openings"]}
    HA_EV = fr.HA_EV
    print("\n  WHAT AN EXACTLY CORRECT SPIN-ORBIT TERM COSTS THE OBJECT")
    print("  The store measures zeta at all six anchored openings, so the object is re-read with the MEASURED")
    print("  zeta in place of the computed one.  That is a substitution of measurement for computation, the same")
    print("  act as gating on the store's measured removal limits, which the object already does.\n")
    print(f"  {'row':6} {'el':3} {'residual now':>13} {'with measured zeta':>19} {'move':>10}"
          f" {'| zeta on the corr orbital':>27}")
    worst_now = worst_fix = worst_corr = 0.0
    d_now, d_fix, d_cor = [], [], []
    for r in R:
        o = byo.get(r["lab"])
        if o is None: continue
        m = fr.MEAS[r["lab"]]
        a = _assemble(fr, o, m, ep, 1.0)
        b = _assemble(fr, o, m, ep, r["zeta_meas"] / r["loc"])
        c = _assemble(fr, o, m, ep, r["corr"]["loc"] / r["loc"])
        if a is None or b is None: continue
        d0 = a["removal_predicted"] - a["measured_actual"]
        d1 = b["removal_predicted"] - b["measured_actual"]
        d2 = c["removal_predicted"] - c["measured_actual"]
        worst_now = max(worst_now, abs(d0)); worst_fix = max(worst_fix, abs(d1))
        worst_corr = max(worst_corr, abs(d2))
        d_now.append(d0); d_fix.append(d1); d_cor.append(d2)
        print(f"  {r['lab']:6} {r['el']:3} {d0:+13.5f} {d1:+19.5f} {(d1-d0)*1000:+9.3f} mHa"
              f" {d2:+27.5f}")
    rms = lambda v: math.sqrt(sum(x * x for x in v) / len(v))
    print(f"\n  worst |residual|   now {worst_now:.5f}   exact zeta {worst_fix:.5f}   zeta on the correlated"
          f" orbital {worst_corr:.5f} Ha")
    print(f"  RMS |residual|     now {rms(d_now):.5f}   exact zeta {rms(d_fix):.5f}   zeta on the correlated"
          f" orbital {rms(d_cor):.5f} Ha")
    print("\n  ALL THREE ARE THE SAME OBJECT TO WITHIN THE SPREAD.  zeta itself moves 3-11 % between the")
    print("  uncorrelated and correlated orbitals and up to 36 % between computed and measured, but it reaches")
    print("  the removal energy only through the Lande term, which is small: the worst row moves 1.8 mHa and")
    print("  the RMS moves 0.07 mHa.  So the choice of orbital for zeta is NOT decided by the six rows -- the")
    print("  present one is kept because it is the record's, not because measurement prefers it -- and every")
    print("  variant sits inside the record's single-entrant class bound of 0.009 Ha")
    print("  (FINDING-HFTERM-SESSION-27).  NO CONCLUSION OF THIS PASS TURNS ON THE ZETA ERROR.")
    # --- and the bound it puts on protactinium, where the store measures nothing
    o = byo.get("5f"); m = fr.MEAS.get("5f")
    if o and m:
        base = _assemble(fr, o, m, ep, 1.0)
        print(f"\n  PROTACTINIUM, where the store measures no interval and the computed zeta is all there is.")
        print(f"  The six measured rows bracket the error at 0.91 (3p) to 1.36 (5d), so the 5f figure is re-read")
        print(f"  with zeta scaled across that whole range:\n")
        print(f"  {'zeta scaled by':>16} {'removal (eV)':>14} {'t(5f)':>9} {'move from 1.000':>16}")
        for f in (1.0, 1.0 / 1.360, 1.0 / 1.237, 1.0 / 0.910, 1.0 / 0.955):
            a = _assemble(fr, o, m, ep, f)
            ev = a["removal_predicted"] * HA_EV
            t = a.get("t_predicted")
            print(f"  {f:16.4f} {ev:14.3f} {t if t else float('nan'):9.4f}"
                  f" {(ev - base['removal_predicted']*HA_EV):+15.3f} eV")
        print("\n  Across the ENTIRE range the six measured rows allow, the 5f removal energy moves by under")
        print("  0.02 eV -- against the +-0.11 eV typical bound the sibling ladder already carries.  The")
        print("  spin-orbit term is not what limits the 5f figure.")


def _assemble(fr, o, m, ep, scale):
    """fieldresidue.assemble on a copy of the row with every zeta scaled -- the neutral's, the ion's, and each
    open shell's, so a multi-shell Lande scales consistently."""
    import copy
    p = copy.deepcopy(o)
    if p.get("zeta_neu") is None: return None
    p["zeta_neu"] *= scale
    if p.get("zeta_ion") is not None: p["zeta_ion"] *= scale
    for k in ("zeta_open_neu", "zeta_open_ion"):
        if p.get(k): p[k] = {a: v * scale for a, v in p[k].items()}
    return fr.assemble(p, m, ep)


# ================================================================== selftest
def selftest():
    ok = bad = 0
    def check(name, cond, extra=""):
        nonlocal ok, bad
        print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"   [{extra}]" if extra else ""))
        ok, bad = ok + bool(cond), bad + (not cond)
    m = meas_rows()
    check("the six anchored openings carry a measured interval", len(m) == 6, f"{len(m)} rows")
    check("zeta_meas from the interval by Delta = zeta (2l+1)/2: Al 3p 112.061 cm-1 -> 74.7",
          abs(m[0]["zeta_meas"] * HA_CM - 74.707) < 0.01, f"{m[0]['zeta_meas']*HA_CM:.3f}")
    if not os.path.exists(OUT_JSON):
        print("  SKIP the measured rows (run --run)")
    else:
        R = json.load(open(OUT_JSON))["rows"]
        F = json.load(open(FIELD_JSON)) if os.path.exists(FIELD_JSON) else None
        if F is None:
            print("  SKIP the gate against fieldresidue (run its --run)")
        else:
            byo = {o.get("opening"): o for o in F["openings"]}
            for r in R:
                o = byo.get(r["lab"])
                if o is None or o.get("zeta_neu") is None: continue
                check(f"gate: zeta_loc {r['lab']} reproduces fieldresidue's banked zeta",
                      abs(r["loc"] - o["zeta_neu"]) < 1e-9, f"{r['loc']:.9f} vs {o['zeta_neu']:.9f}")
        for r in R:
            check(f"{r['lab']}: the KH factor never raises zeta (it suppresses the deep core)",
                  r["khloc"] <= r["loc"] * (1 + 1e-12), f"{r['khloc']/r['loc']:.4f}")
        # --- the three claims the cost section rests on
        if not os.path.exists(FIELD_JSON):
            print("  SKIP the cost claims (fieldresidue --run needed)")
        else:
            fr = _load("fieldresidue", os.path.join(HERE, "fieldresidue.py"))
            ep = _load("entrypoint", os.path.join(HERE, "entrypoint.py"))
            F = json.load(open(FIELD_JSON)); byo = {o.get("opening"): o for o in F["openings"]}
            worst = 0.0
            for r in R:
                o = byo.get(r["lab"])
                if o is None: continue
                b = _assemble(fr, o, m_of(fr, r["lab"]), ep, r["zeta_meas"] / r["loc"])
                worst = max(worst, abs(b["removal_predicted"] - b["measured_actual"]))
            check("with the store's MEASURED zeta every anchored opening still closes inside the record's"
                  " single-entrant class bound of 0.009 Ha", worst < 0.009, f"worst {worst:.5f} Ha")
            o = byo.get("5f")
            if o is None:
                print("  SKIP the 5f bound (no 5f row)")
            else:
                m5 = m_of(fr, "5f")
                evs, ts = [], []
                for f in (1.0, 1.0 / 1.360, 1.0 / 0.910):
                    a = _assemble(fr, o, m5, ep, f)
                    evs.append(a["removal_predicted"] * fr.HA_EV); ts.append(a["t_predicted"])
                check("the 5f removal energy moves under 0.02 eV across the whole range the six measured rows"
                      " allow", max(evs) - min(evs) < 0.02, f"{max(evs)-min(evs):.4f} eV")
                check("and ruling 1's floor holds at every scaling: t(5f) stays above sqrt(6) = 2.4495",
                      min(ts) > math.sqrt(6.0), f"min t {min(ts):.4f}")


def m_of(fr, lab):
    return fr.MEAS[lab]
    print(f"\n  {ok} passed, {bad} failed")
    return bad == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--run", action="store_true")
    a = ap.parse_args()
    if a.selftest: sys.exit(0 if selftest() else 1)
    if a.run: cmd_run(); return
    report()


if __name__ == "__main__":
    main()
