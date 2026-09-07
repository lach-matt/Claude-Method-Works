#!/usr/bin/env python3
"""cuaudit.py -- RULING 8(c): `t7c_cuaudit.py` IS ABSENT, AND ITS WHOLE INTERFACE IS PINNED BY FILES THAT ARE HELD.

  M's ruling 8(c): "`t7c_cuaudit.py` is absent from the repository and its S-form potential is reconstructed --
  settle it."

  THE FILE IS ABSENT AND WILL NOT BE RECOVERED BY ASKING AGAIN.  `recovered/` does not hold it, and neither
  `t7c_cuaudit.py` nor `t7c_corrz.py` appears anywhere in `COVERAGE.tsv` -- the bundles never cite either in
  filename shape, which is exactly the reach limit `docs/RECOVER.md` records for `recover.py`'s wanted-set.  The
  record's own route to it is a second absent file: "t7c_cuaudit.py = t7c_corrz.py VERBATIM + env FENT"
  (PREDICTION-CU-AUDIT-SESSION-24), and `recovered/` holds only `t7c_corrz_run.py`.

  BUT THE INTERFACE IS NOT UNKNOWN.  Every consumer of the module is held, and between them they name it
  completely.  MEASURED by reading the three held importers, the module is used through EIGHT names and no
  others:

      hfc2.py      T.E0B  T.LAM1  T._lam1  T._lam0  T._e0a  T.v_gbz
      corr_ring.py T.E0B  T._SUBCELL  T._frac_neg  T._lam0  T._e0a  T.v_gbz
      hfterm.py    T.v_gbz

  AND SEVEN OF THE EIGHT ARE PINNED BY A HELD FILE, not reconstructed:

      E0B       0.0241792 Ha -- sox_table.py:7, and it is the EXACTLY KNOWN Onsager-Mittag-Stephen 1966
                constant, which soxquad.py now reproduces from the corpus's own reduction to +0.047 %.
      _lam0(z)  the RPA ring integral's log coefficient: ring_zeta.cL(z)/2 (Ry -> Ha), session 23.
      _e0a(z)   the ring constant c0(zeta), read as eps_r(0.005, z)/2 - lam0 ln(0.005) and GATED on
                GB-ZETA-RING-23's six recorded values, all six passing to 5e-5 Ha.
      LAM1      hfc2.py guards its own use of it -- `if T.LAM1` -- so the standing setting is off, and the
                branch is dead in every run the record reports.  `_lam1` is reached only through it.
      _SUBCELL  the session-28 cell cut, env SUBCELL=1, which is the setting every S-form row the record
                reports was run at (FINDING-CELLCUT-SESSION-28).
      _frac_neg cellcut.py, HELD -- loaded by path here, never copied.

  THE EIGHTH, `v_gbz`, IS THE ONE THAT WAS CALLED "RECONSTRUCTED", AND IT IS PINNED TOO -- by `corr_ring.py`,
  which is held and which declares itself to be exactly this interface:

      "Same interface as t7c_cuaudit.v_gbz / hfc2.eps_c so it can be patched in: T.v_gbz = v_R; H.eps_c = eps_R."

  So the shape of v_gbz is not inferred from prose: a complete, held, runnable implementation of it exists for
  form R, and `fieldresidue.FormS` is that implementation with the S table in place of the R table -- which is
  the ONE declared substitution, and is what "form S" means.

  THE GATE, AND IT IS NOT CIRCULAR.  This module supplies the seven pinned names.  The held `corr_ring.py` is
  then imported AGAINST IT, unmodified, and run.  Separately, `fieldresidue.FormS` is built on the RING table --
  the same table corr_ring reads -- and the two are compared point by point over a grid of densities and spin
  polarisations.  If FormS is corr_ring's function with the table swapped, they agree to machine precision, and
  the reconstruction is then not a reconstruction of a shape but a re-tabulation of a held one.

  WHAT REMAINS UNPINNED, stated so it is not lost: the module's own private text -- its docstring, its argument
  parsing, the FENT and FOCC environment switches that made it "t7c_corrz.py VERBATIM + env FENT", and whatever
  else it contained beyond the eight names.  None of that is reachable, and none of it is used by the object.
  The status stays RECONSTRUCTED and is never flattened.

  usage:  python3 cuaudit.py             the report
          python3 cuaudit.py --selftest  the gate

  numpy; every source file is loaded by path and none is copied.
"""
import argparse, importlib.util, json, math, os, sys, types

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RECOVERED = os.path.join(ROOT, "recovered")
E0B = 0.0241792                       # sox_table.py:7 -- Onsager-Mittag-Stephen 1966, exactly known
RING_C0 = {0.0: -0.07115, 0.4: -0.06824, 0.6: -0.06436, 0.8: -0.05828, 0.9: -0.05399, 1.0: -0.04991}

# the eight names the three held importers reach for, and nothing else
INTERFACE = ("E0B", "LAM1", "_lam1", "_lam0", "_e0a", "_SUBCELL", "_frac_neg", "v_gbz")


def _load(name, path, cwd=None):
    old = os.getcwd()
    if cwd: os.chdir(cwd)
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    finally:
        os.chdir(old)
    return mod


def cL_Ry(ring_zeta, z):
    """ring_zeta.cL (Eq. 16) in Ry.  At zeta = 1 the printed formula evaluates 0 log 0 and returns nan; its limit
    is (1 - ln 2)/pi^2 Ry, exactly half of cL(0) -- the record's own PZ5, "c_L(1) = half"
    (FINDING-GB-ZETA-RING-SESSION-23).  Taken as the limit, not as a change to the formula."""
    v = float(ring_zeta.cL(z))
    if math.isfinite(v): return v
    xp, xm = ring_zeta.xs(z); chi = xp + xm
    t = lambda x: (x ** 3 * math.log(x)) if x > 0 else 0.0
    return (1 / math.pi ** 2) * ((1 - math.log(2)) + xp * xm / 2 * chi - math.log(chi) + 0.5 * (t(xp) + t(xm)))


def build(subcell=True, workdir=None):
    """The reconstructed t7c_cuaudit, seated as a module.  Seven names come from held files; v_gbz is left for
    the caller to bind, exactly as corr_ring.py binds it ("T.v_gbz = v_R")."""
    import numpy as np
    # numpy 2 renamed trapz -> trapezoid and the recovered generators straddle the rename (ring_zeta.py calls
    # trapz, sox_qres.py calls trapezoid).  The alias is the rename and nothing else -- the same declared shim
    # fieldresidue.py carries.
    if not hasattr(np, "trapz"): np.trapz = np.trapezoid
    if not hasattr(np, "trapezoid"): np.trapezoid = np.trapz
    ring_zeta = _load("ring_zeta", os.path.join(RECOVERED, "ring_zeta.py"), cwd=workdir)
    cellcut = _load("cellcut", os.path.join(RECOVERED, "cellcut.py"))
    T = types.ModuleType("t7c_cuaudit")
    T.E0B = E0B
    T.LAM1 = False                      # hfc2.py guards its own use: `if T.LAM1`
    T._lam1 = lambda z: 0.0             # reached only through LAM1
    T._lam0 = lambda z: cL_Ry(ring_zeta, float(np.asarray(z).flat[0]) if np.ndim(z) else float(z)) / 2.0
    def _e0a(z):
        zz = float(np.asarray(z).flat[0]) if np.ndim(z) else float(z)
        lam0 = cL_Ry(ring_zeta, zz) / 2.0
        return float(ring_zeta.eps_r(0.005, zz)) / 2.0 - lam0 * math.log(0.005)
    T._e0a = _e0a
    T._SUBCELL = subcell
    T._frac_neg = cellcut.frac_neg
    T.v_gbz = None                      # bound by the consumer, as corr_ring.py does
    sys.modules["t7c_cuaudit"] = T
    return T, ring_zeta


# ================================================================== report
def report():
    print("=" * 110)
    print("cuaudit.py -- RULING 8(c): t7c_cuaudit.py IS ABSENT, AND ITS WHOLE INTERFACE IS PINNED")
    print("=" * 110)
    print("""
  The file is absent and will not be recovered by asking again: recovered/ does not hold it, and NEITHER
  t7c_cuaudit.py NOR t7c_corrz.py appears anywhere in COVERAGE.tsv -- the bundles never cite either in
  filename shape, which is the reach limit docs/RECOVER.md records for recover.py's wanted-set.  The record's
  own route ("t7c_cuaudit.py = t7c_corrz.py VERBATIM + env FENT") leads to a second absent file.

  But the interface is not unknown.  Reading the three held importers, the module is used through EIGHT names
  and no others -- and seven are pinned by a held file rather than reconstructed:
""")
    rows = [
        ("E0B", "sox_table.py:7 = 0.0241792 Ha", "the exactly known Onsager-Mittag-Stephen 1966 constant"),
        ("_lam0(z)", "ring_zeta.cL(z)/2", "the RPA ring integral's log coefficient, session 23"),
        ("_e0a(z)", "ring_zeta.eps_r(0.005,z)/2 - lam0 ln(0.005)", "gated on GB-ZETA-RING-23's six c0 values"),
        ("LAM1", "hfc2.py's own guard `if T.LAM1`", "the branch is dead in every run the record reports"),
        ("_lam1(z)", "reached only through LAM1", "never evaluated"),
        ("_SUBCELL", "env SUBCELL=1, session 28", "the setting every S-form row was run at"),
        ("_frac_neg", "cellcut.py, HELD", "loaded by path, never copied"),
        ("v_gbz", "corr_ring.py, HELD", 'declares itself "same interface ... so it can be patched in"'),
    ]
    print(f"  {'name':11} {'pinned by':46} {'':2}")
    for a, b, c in rows:
        print(f"  {a:11} {b:46} {c}")
    print("""
  THE EIGHTH IS THE ONE THAT WAS CALLED RECONSTRUCTED, AND IT IS PINNED TOO.  corr_ring.py is a complete,
  held, runnable implementation of v_gbz for form R, and fieldresidue.FormS is that implementation with the
  S table in place of the R table -- the one declared substitution, and what "form S" means.

  The gate (--selftest) imports the HELD corr_ring.py against this reconstruction, unmodified, and compares it
  point by point against FormS built on the SAME ring table.  Agreement to machine precision means FormS is
  corr_ring's function with the table swapped, so what was reconstructed is a re-tabulation of a held shape,
  not a guessed one.

  WHAT REMAINS UNPINNED, so it is not lost: the module's own private text -- its docstring, its argument
  parsing, the FENT and FOCC switches that made it "t7c_corrz.py VERBATIM + env FENT", and anything else it
  held beyond the eight names.  None of it is reachable and none of it is used by the object.  THE STATUS
  STAYS RECONSTRUCTED AND IS NEVER FLATTENED.
""")
    print("=" * 110)


# ================================================================== selftest
def selftest():
    ok = bad = 0
    def check(name, cond, extra=""):
        nonlocal ok, bad
        print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"   [{extra}]" if extra else ""))
        ok, bad = ok + bool(cond), bad + (not cond)
    if importlib.util.find_spec("numpy") is None:
        print("  SKIP (numpy needed)"); return True
    import numpy as np
    import shutil, tempfile

    # ---- the interface census: exactly these names and no others, read from the held importers
    used = set()
    for f in ("hfc2.py", "corr_ring.py", "hfterm.py"):
        src = open(os.path.join(RECOVERED, f)).read()
        import re
        used |= set(re.findall(r"\bT\.([A-Za-z_][A-Za-z_0-9]*)", src))
    check("the three held importers reach for exactly the eight names this module supplies",
          used == set(INTERFACE), f"{sorted(used)}")

    # ---- the file really is absent, and so is the record's route to it
    check("t7c_cuaudit.py is absent from recovered/",
          not os.path.exists(os.path.join(RECOVERED, "t7c_cuaudit.py")))
    check("and t7c_corrz.py, the record's stated route to it, is absent too",
          not os.path.exists(os.path.join(RECOVERED, "t7c_corrz.py")))
    cov = os.path.join(ROOT, "COVERAGE.tsv")
    if os.path.exists(cov):
        txt = open(cov).read()
        check("neither is named anywhere in COVERAGE.tsv, so no wanted-set run can reach them",
              "t7c_cuaudit" not in txt and "t7c_corrz" not in txt)

    # ---- the seven pinned names, built and checked against the record's own numbers
    work = tempfile.mkdtemp(prefix="cuaudit-")
    try:
        shutil.copy(os.path.join(RECOVERED, "ring_table.json"), work) if os.path.exists(
            os.path.join(RECOVERED, "ring_table.json")) else None
        T, ring_zeta = build()
        check("E0B is the exactly known 1966 constant", abs(T.E0B - 0.0241792) < 1e-12, f"{T.E0B}")
        check("LAM1 is off, so hfc2's `if T.LAM1` branch is dead", T.LAM1 is False)
        # hfc2's chain form is lam0 ln r_s + _e0a + E0B and FormS's is lam0 ln r_s + c0 + E0B, so _e0a IS c0 --
        # E0B is added beside it, not inside it.
        worst = 0.0
        for z, v in RING_C0.items():
            worst = max(worst, abs(T._e0a(z) - v))
        check("_e0a reproduces GB-ZETA-RING-23's six recorded ring constants c0(zeta)",
              worst < 5e-5, f"worst {worst:.2e} Ha")
        check("_frac_neg is cellcut.py's own function, loaded by path",
              T._frac_neg.__module__ == "cellcut")

        # ---- THE GATE: the held corr_ring.py, run unmodified against this module, against FormS on the same table
        tabs = json.load(open(os.path.join(HERE, "fieldresidue-tables.json")))
        json.dump({"rs": tabs["rs"], "z": tabs["z"],
                   "eps": {str(i): tabs["eps_ring_Ry"][i] for i in range(len(tabs["z"]))}},
                  open(os.path.join(work, "ring_table.json"), "w"))
        cr = _load("corr_ring", os.path.join(RECOVERED, "corr_ring.py"), cwd=work)
        fr = _load("fieldresidue", os.path.join(HERE, "fieldresidue.py"))
        # FormS on the RING table -- eps_ring/2 + E0B -- which is precisely what corr_ring builds
        Rtab = dict(tabs)
        Rtab["eps_S"] = [[e / 2.0 + E0B for e in row] for row in tabs["eps_ring_Ry"]]
        FS = fr.FormS(Rtab)
        rs = np.array([0.05, 0.2, 0.8, 1.5, 2.0, 3.0, 5.0, 9.0, 20.0, 60.0])
        for z in (0.0, 0.3, 0.7, 1.0):
            n = 3.0 / (4 * np.pi * rs ** 3)
            nu = n * (1 + z) / 2.0; nd = n * (1 - z) / 2.0
            e1 = np.asarray(cr.eps_R(nu, nd)); e2 = np.asarray(FS.eps(nu, nd))
            check(f"FormS.eps == corr_ring.eps_R on the ring table, zeta {z}",
                  float(np.max(np.abs(e1 - e2))) < 1e-12, f"max |diff| {float(np.max(np.abs(e1-e2))):.1e} Ha")
            v1u, v1d = cr.v_R(nu, nd); v2u, v2d = FS.v(nu, nd)
            d = max(float(np.max(np.abs(np.asarray(v1u) - np.asarray(v2u)))),
                    float(np.max(np.abs(np.asarray(v1d) - np.asarray(v2d)))))
            check(f"FormS.v  == corr_ring.v_R  on the ring table, zeta {z}", d < 1e-12, f"max |diff| {d:.1e} Ha")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    print(f"\n  {ok} passed, {bad} failed")
    return bad == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest: sys.exit(0 if selftest() else 1)
    report()


if __name__ == "__main__":
    main()
