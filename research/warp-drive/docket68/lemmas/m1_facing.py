#!/usr/bin/env python3
"""m1_facing.py -- item 197: our plane facing the other plane, not its own reflection (computed, deduced, STRUCTURAL;
not verified by a separate session; not seated; 2026-10-10).

M, item 197, verbatim (the first sentence is the board's, from the F1 audit, quoted back by M; the clause after the
dash is M's):
  "A plane on its own can read eq. (17) smoothly only if it carries extra matter. - because it sees its own
   reflection, not the other plane"

The F1 audit (lemmas/F1-AUDIT.md, lemmas/f1_audit.py) computed, in Kaus-Reall's warped-product near-horizon class
ds^2 = A(rho)^2 dSigma_AdS2^2 + drho^2 + R(rho)^2 dOmega^2 (vacuum, R_AB = -(4/ell^2) g_AB), that ONE Z2 plane reading
eq. (17)'s near-horizon AdS2(2m) x S2(2m) regularly needs added plane matter (8.02 sigma_RS at 2m/ell = 0.0739), because
the bulk must close on a compact-horizon cap (R -> 0; KR p.5), and that without the cap the matter-free plane's bulk
runs into a curvature singularity at y_s.  This instrument works 197 in that same class.

  F1  (L1, STRUCTURAL, computed symbolically) at a plane reading equal radii A = R the bulk constraint is
      a^2 + 4ab + b^2 = 6 on each side (a = ell A'/A, b = ell R'/R along that side's outward normal); a plane carrying
      the RS tension and nothing else needs (a1 + a2)/2 = (b1 + b2)/2 = 1.  The only solution is a1 = b1 = a2 = b2 = 1,
      so (ODE uniqueness) both sides are the same solution: the plane is locally mirror-symmetric whatever lies beyond.
      Control: with added matter allowed the two sides need not agree.  A different ell on the far side is outside
      (real solutions only for (ell/ell2)^2 <= 1 or >= 9, and the tension is then not sigma_RS).
      So the reflection is forced at the plane; what 197 changes is WHERE THE BULK ENDS: on a cap (the horizon closing
      on itself, one plane and its image) or on the other plane P2 (the horizon running from P1 to P2, compact by being
      bounded, so KR's one-brane premise "R must vanish somewhere" no longer applies).
  F2  (computed, reproduced from f1_audit) the single-plane cap at 2m/ell = 0.0739 needs 8.02 sigma_RS on our plane.
  F3  (computed) facing: P1 at the RS tension only (eq. (17)'s Q = 0 data), the bulk integrated toward y_s, P2 a Z2
      plane at constant depth y2 < y_s.  P1 needs NO added matter.  P2's stress obeys the NEC at every sampled depth at
      every ell (e2 + P2 = (alpha - beta) sigma/3 > 0, -> 0+ at coincidence), and tends to the RS1 sheet (-sigma) as
      y2 -> 0, as SIM2-FACING S15 found in the full static bulk.
  F4  (computed) the energy left on P2 after a tension q2 is subtracted is positive in a depth band whose existence
      depends on q2.  139 (1) ("1 - yes" to "whether position 2's plane is the negative-tension one, a quarter of
      ours, with ours positive") gives q2 = -1/4 of ours on one sheet (per-sheet count; -1/8 per sheet on the doubled
      count, COUNT-CYPHER.md, undecided): the remainder is then positive in a depth band for ell > 8.54m (doubled:
      ell > 10.40m), and negative at coincidence (-3/4) at every ell.  For comparison only: q2 = +1
      (H-SPLIT-AT-OUR-TENSION, P2 a piece of our plane, which 139 (1) and 197's "the other plane" read against) needs
      ell > 27.07m -- SIM2-FACING's edge (a consistency check: the same configuration in its throat limit, not
      independent evidence); q2 = -1 (the RS1 sheet, the coincidence value of the trace) is positive at every ell.
  F5  (computed) controls: P2 removed -> the single-plane verdict returns (singular at y_s, or a cap with added
      matter); P2 at or beyond y_s -> the slab holds the singularity.
  F6  (computed; the cypher CLASSIFIES, it derives nothing) roster 1173 on the computed cells (H-CYPHER-FACING, the
      board's encoding): the facing cell is admitted by every operator-bearing language -- forced, since it is data;
      with it left out NO language regrows it (the other plane is not implied by the reflection cells); the control
      (a plane facing its reflection, no added matter, regular) is refused by information and statistics under every
      ordering of 'end', by geometry on the native ordering, and admitted by order and algebra (their closure reaches a
      cell the computation refutes: a STRUCTURAL caveat, recorded).
  F7  (computed) a second engine -- scipy DOP853, rtol 1e-11, right-hand sides typed independently -- agrees on y_s and
      on the 27.07m threshold.

Named readings (the board's, never M's): H-CYPHER-FACING (the index); H-WHERE-THE-BULK-ENDS (197 read as: the
reflection is local and forced, the extra matter comes from the bulk closing on itself); H-SPLIT-AT-OUR-TENSION and
H-LAW-READ-BY-TRACE (carried from SIM2-FACING).  Near-horizon class only: the throat region, not the full bulk.
Imports lemmas/f1_audit.py and tools/cypher.py by path.  Stdlib + sympy (+ scipy for F7).
python3 m1_facing.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
M197 = ('"A plane on its own can read eq. (17) smoothly only if it carries extra matter. - because it sees its own\n'
        '    reflection, not the other plane"')
XS = (0.0044, 0.0439, 0.0739, 0.179, 0.5, 1.72)        # 2m/ell, the F1 audit's grid points
Q2S = {"+1 (H-SPLIT-AT-OUR-TENSION)": 1.0, "-1 (RS1 sheet, coincidence)": -1.0, "-1/3 (M4)": -1 / 3,
       "-1/4 (per-sheet)": -0.25, "-1/8 (doubled)": -0.125}
MUT = {}                                                # mutation switches (--mutants)


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, os.path.dirname(D68)]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[key] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


_F1 = []


def f1():
    if not _F1:
        _F1.append(_load(os.path.join(HERE, "f1_audit.py"), "m1f_f1_audit"))
    return _F1[0]


# ------------------------------------------------------------------------------------------------ F1: the mirror lemma
def mirror_lemma():
    a1, b1, a2, b2, r, u = sp.symbols("a1 b1 a2 b2 r u", real=True)
    con = lambda a, b, rr=1: a**2 + 4 * a * b + b**2 - 6 * rr
    tension = 2 if not MUT.get("l1_tension_off") else sp.Rational(5, 2)
    sol = sp.solve([con(a1, b1), con(a2, b2), a1 + a2 - tension, b1 + b2 - tension], [a1, b1, a2, b2], dict=True)
    unique_mirror = len(sol) == 1 and all(sol[0][s] == 1 for s in (a1, b1, a2, b2))
    # control: added matter u = (rho + 2p)/sigma on the plane frees the A-slopes; non-mirror solutions then exist
    ctrl = sp.solve([con(a1, b1), con(a2, b2), (a1 + a2) / 2 - (1 - u), b1 + b2 - 2], [a1, b1, a2, b2], dict=True)
    ctrl_nonmirror = any(sp.simplify(s[a1] - s[a2]).subs(u, sp.Rational(1, 2)) != 0 for s in ctrl)
    far = sp.solve([con(a1, b1), con(a2, b2, r), a1 + a2 - 2, b1 + b2 - 2], [a1, b1, a2, b2], dict=True)
    disc = sp.factor(3 * r**2 - 30 * r + 27)
    return {"unique_mirror": unique_mirror, "sol": sol, "ctrl_nonmirror": ctrl_nonmirror, "far_disc": disc,
            "far_real_gap": all(disc.subs(r, v) < 0 for v in (2, 5, 8)) and all(disc.subs(r, v) >= 0 for v in (1, 9, sp.Rational(1, 2), 10)),
            "far_count": len(far)}


# --------------------------------------------------------------------------------------- F2-F5: the computed stresses
def traj(x, n=40000):
    """P1 at the RS tension only (eq. (17)'s Q = 0 data): A = R = 2m (m = 1), slopes -1/ell into the bulk."""
    F = f1()
    ell = 2.0 / x
    f = F._rhs(1 / ell**2, 4.0)
    ys = F.ys(ell)
    side = -1.0 if not MUT.get("p1_wrong_side") else 1.0
    s = [0.0, 2.0, side * 2.0 / ell, 2.0, side * 2.0 / ell]
    out, h = [], ys / n
    while s[0] < 0.999 * ys and s[1] > 1e-6:
        s = F._rk4(f, s, h)
        if not all(v == v for v in s):
            break
        out.append(s)
    return ell, ys, out


def p2_stress(s, ell):
    """Israel at P2, a Z2 plane at depth y2 bounding the slab; normal into the slab (back toward P1).  Units sigma_RS.
    e = -(alpha + 2 beta)/3, P = (2 alpha + beta)/3; RS tension is alpha = beta = -1 along the into-bulk normal."""
    y, A, Ap, R, Rp = s
    sgn = -1.0 if not MUT.get("p2_normal_flip") else 1.0
    z2 = 1.0 if not MUT.get("p2_no_z2") else 0.5
    al, be = sgn * ell * Ap / A, sgn * ell * Rp / R
    e, P = -z2 * (al + 2 * be) / 3, z2 * (2 * al + be) / 3
    return y, e, P, e + P


def facing(x, n=40000):
    ell, ys, T = traj(x, n)
    S = [p2_stress(s, ell) for s in T[1:]]
    p1 = f1().plane_matter({"Ap_A": 1.0, "Rp_R": 1.0})            # P1's added matter from its Q = 0 slopes
    bands = {}
    for name, q in Q2S.items():
        pos = [y / ys for (y, e, P, n_) in S if e - q > 0]
        bands[name] = (min(pos), max(pos)) if pos else None
    return {"ell": ell, "ys": ys, "reached": T[-1][0] / ys if T else 0.0, "p1_rho": p1["rho"], "p1_p": p1["p"],
            "nec_min": min(r[3] for r in S), "first": S[0], "emax": max(r[1] for r in S), "bands": bands}


def threshold(q=1.0, lo=0.03, hi=0.2):
    """2m/ell at which max over depth of (e2 - q) crosses 0 (q = +1: H-SPLIT-AT-OUR-TENSION)."""
    if MUT.get("threshold_sub_minus"):
        q = -1.0
    g = lambda x: max(p2_stress(s, 2.0 / x)[1] for s in traj(x, 20000)[2][1:]) - q
    if not (g(lo) > 0 > g(hi)):
        return None
    for _ in range(36):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if g(mid) > 0 else (lo, mid)
    return (lo + hi) / 2


def single_plane_cap(x=0.0739):
    F = f1()
    A0 = F.find_A0_for_x(x)
    c = F.cap_cut(A0)
    pm = F.plane_matter(c)
    return {"A0": A0, "rho": pm["rho"], "p": pm["p"]}


def controls():
    """P2 removed: the Q = 0 bulk runs to A -> 0 at y_s (singular); P2 at/after y_s: the slab holds that end."""
    F = f1()
    out = {}
    for x in (0.0739, 0.5):
        ell = 2.0 / x
        out[x] = {"ys": F.ys(ell), "reaches_singular": F.ys(ell) is not None}
    return out


# ------------------------------------------------------------------------------------------------- F6: the cypher
C_NAMES = ["face", "end", "extra", "regular"]
CELLS = {
    "one plane, Q = 0, no cap: singular at y_s (F1-AUDIT C2)": (0, 2, 0, 0),
    "one plane, compact-horizon cap: added matter (F1-AUDIT C4-C6; two caps C7)": (0, 0, 1, 1),
    "facing P2 at y2 < y_s, P1 at Q = 0: P2 NEC at every depth (F3)": (1, 1, 0, 1),
    "facing P2 at or beyond y_s: the slab holds the singularity (F5)": (1, 2, 0, 0),
}
MAIN = (1, 1, 0, 1)
CTRL = ((0, 0, 0, 1), (0, 2, 0, 1))
OPS = ("order", "algebra", "geometry", "information", "statistics")


def cypher_run():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "m1f_cypher")
    cells = dict(CELLS)
    if MUT.get("seat_control"):
        cells["(mutant) reflection, no added matter, regular"] = (0, 0, 0, 1)
    leave = {k: v for k, v in cells.items() if not k.startswith("facing P2 at y2")}
    if MUT.get("leave_out_keeps"):
        leave = dict(cells)

    def admits(cellset, perm, targets):
        m = lambda t: (t[0], perm[t[1]], t[2], t[3])
        cl = sorted(set(m(c) for c in cellset))
        ix = cy.Index("i197", C_NAMES, [list(c) for c in cl])
        enc = lambda t: tuple(ix.code[i][v] if v in ix.code[i] else None for i, v in enumerate(t))
        res, Es = {}, {}
        for lang in OPS:
            out, _ = cy.ADMISSION[lang][0](ix, {})
            if out is None:
                res[lang] = None
                continue
            Es[lang] = len(out) - len(ix.cells)
            res[lang] = [None not in enc(m(t)) and enc(m(t)) in out for t in targets]
        silent = {lang: cy.ADMISSION[lang][0](ix, {})[0] is None for lang in ("documentary",) if lang in cy.ADMISSION}
        return res, Es, silent
    native = (0, 1, 2)
    allr, allE, sil = admits(cells.values(), native, (MAIN,) + CTRL)
    lo, loE, _ = admits(leave.values(), native, (MAIN,))
    perms = {}
    for p in itertools.permutations((0, 1, 2)):
        a, _, _ = admits(cells.values(), p, (MAIN,) + CTRL)
        b, _, _ = admits(leave.values(), p, (MAIN,))
        perms[p] = (a, b)
    return {"all": allr, "allE": allE, "leave": lo, "leaveE": loE, "perms": perms,
            "documentary_silent": "documentary" not in cy.ADMISSION or all(sil.values()),
            "analysis_declared": "analysis" not in cy.ADMISSION}


# --------------------------------------------------------------------------------------------- F7: a second engine
def second_engine(xs=(0.0739, 0.5)):
    try:
        import numpy as np
        from scipy.integrate import solve_ivp
        from scipy.optimize import brentq
    except ImportError:
        return None

    def rhs(y, s, il2):
        A, Ap, R, Rp = s
        return [Ap, A * (4 * il2 - 1 / A**2 - Ap**2 / A**2 - 2 * Ap * Rp / (A * R)), Rp,
                R * (4 * il2 + 1 / R**2 - Rp**2 / R**2 - 2 * Ap * Rp / (A * R))]

    def run(x):
        ell = 2 / x
        ev = lambda y, s, il2: s[0] - 1e-6
        ev.terminal = True
        sol = solve_ivp(rhs, [0, 50], [2, -2 / ell, 2, -2 / ell], args=(1 / ell**2,), method="DOP853", rtol=1e-11,
                        atol=1e-13, events=ev, dense_output=True)
        ys = sol.t[-1]
        yy = np.linspace(1e-4 * ys, 0.999 * ys, 4001)
        A, Ap, R, Rp = sol.sol(yy)
        al, be = -ell * Ap / A, -ell * Rp / R
        return ys, float(np.max(-(al + 2 * be) / 3)), float(np.min((al - be) / 3))
    out = {x: run(x) for x in xs}
    out["threshold"] = brentq(lambda x: run(x)[1] - 1.0, 0.05, 0.1, xtol=1e-7)
    return out


# ------------------------------------------------------------------------------------------------------- checks
def compute():
    q = -0.25 if not MUT.get("quarter_as_ours") else 0.25
    return {"L1": mirror_lemma(), "cap": single_plane_cap(), "face": {x: facing(x) for x in XS},
            "thr": threshold(), "thr_q": {"-1/4": threshold(q, 0.05, 0.6), "-1/8": threshold(-0.125, 0.05, 0.6)},
            "ctl": controls(), "cy": cypher_run(), "eng2": second_engine()}


def checks(d):
    res = []
    add = lambda name, ok: res.append((name, bool(ok)))
    L1 = d["L1"]
    add("C1 L1: RS tension only + equal radii force a1 = b1 = a2 = b2 = 1 (local mirror); control: added matter frees "
        "it; a different far-side ell has no real solution for 1 < (ell/ell2)^2 < 9",
        L1["unique_mirror"] and L1["ctrl_nonmirror"] and L1["far_real_gap"])
    c = d["cap"]
    add("C2 the single-plane cap at 2m/ell = 0.0739 needs 8.0-8.05 sigma_RS on our plane (F1-AUDIT C6 reproduced)",
        8.0 <= c["rho"] < 8.05)
    F = d["face"]
    add("C3 facing: P1 needs no added matter (rho = p = 0 from its Q = 0 slopes)",
        all(abs(F[x]["p1_rho"]) < 1e-12 and abs(F[x]["p1_p"]) < 1e-12 for x in XS))
    add("C4 facing: P2 obeys the NEC at every sampled depth (0, y_s) at all six ell; P2 -> the RS1 sheet (-1, +1) as "
        "y2 -> 0", all(F[x]["nec_min"] > 0 and F[x]["reached"] > 0.99 for x in XS)
        and all(abs(F[x]["first"][1] + 1) < 5e-3 and abs(F[x]["first"][2] - 1) < 5e-3 for x in XS))
    thr = d["thr"]
    add("C5 the energy left on P2 after our tension (+1) is positive somewhere only for ell > 27.07m: threshold "
        "2m/ell = 0.07389 (SIM2-FACING's 27.07m edge; consistency, not independent)",
        thr is not None and abs(2 / thr - 27.0665) < 0.01
        and F[0.0044]["bands"]["+1 (H-SPLIT-AT-OUR-TENSION)"] is not None
        and all(F[x]["bands"]["+1 (H-SPLIT-AT-OUR-TENSION)"] is None for x in (0.0739, 0.179, 0.5, 1.72)))
    add("C6 with P2's tension read as -1 (RS1 sheet) the remainder is positive in a depth band from coincidence at "
        "every ell tested", all(F[x]["bands"]["-1 (RS1 sheet, coincidence)"] is not None
                                and F[x]["bands"]["-1 (RS1 sheet, coincidence)"][0] < 0.01 for x in XS))
    tq = d["thr_q"]
    add("C6b with P2's tension at 139 (1)'s 'a quarter of ours' (-1/4, per-sheet) the remainder is positive in a depth "
        "band only for ell > 8.54m (-1/8 per sheet, doubled: ell > 10.40m), and negative at coincidence (-3/4) at "
        "every ell", tq["-1/4"] is not None and abs(2 / tq["-1/4"] - 8.5415) < 0.01 and tq["-1/8"] is not None
        and abs(2 / tq["-1/8"] - 10.3998) < 0.01 and all(F[x]["first"][1] + 0.25 < 0 for x in XS)
        and F[0.0044]["bands"]["-1/4 (per-sheet)"] is not None and F[0.5]["bands"]["-1/4 (per-sheet)"] is None)
    ctl = d["ctl"]
    add("C7 controls: P2 removed, the Q = 0 bulk reaches the singular end y_s (the single-plane verdict returns)",
        all(v["reaches_singular"] for v in ctl.values()))
    cy = d["cy"]
    a = cy["all"]
    add("C8 cypher: MAIN admitted by every operator-bearing language with the facing cell in (forced: it is data)",
        all(a[l] is not None and a[l][0] for l in OPS))
    add("C9 cypher leave-out: with the facing cell removed NO language regrows it, under every ordering of 'end'",
        all(not cy["leave"][l][0] for l in OPS if cy["leave"][l] is not None)
        and all(not b[l][0] for (_, b) in cy["perms"].values() for l in OPS if b[l] is not None))
    add("C10 cypher control: 'facing its reflection, no added matter, regular' refused by information and statistics "
        "under every ordering, by geometry on the native one; order and algebra admit it (STRUCTURAL caveat)",
        all(not any(pa[l][1:]) for (pa, _) in cy["perms"].values() for l in ("information", "statistics"))
        and not any(a["geometry"][1:]) and a["order"][1] and a["algebra"][1])
    add("C11 documentary silent by construction; analysis needs a declared witness (not run)",
        cy["documentary_silent"] and cy["analysis_declared"])
    e2 = d["eng2"]
    add("C12 second engine (scipy DOP853): y_s agrees to 1e-4 relative; NEC positive; threshold 27.07m",
        e2 is not None and all(abs(e2[x][0] - F[x]["ys"]) / F[x]["ys"] < 1e-4 and e2[x][2] > 0 for x in (0.0739, 0.5))
        and abs(2 / e2["threshold"] - 27.0665) < 0.01)
    rul = open(os.path.join(D68, "M-RULINGS-2026-10-03.md")).read()
    add("CG guards: 197 quoted verbatim from the rulings file; no status claimed green; the cypher not called a "
        "derivation", M197 in rul and "GREEN" not in __doc__.split("Named readings")[0].upper().replace("GREEN ", ""))
    return res


def selftest():
    d = compute()
    r = checks(d)
    for name, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", name))
    n = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (n, len(r)))
    return n == len(r)


MUTANTS = {
    "l1_tension_off": "L1 with the tension sum 5/2 instead of 2",
    "p1_wrong_side": "P1's slopes integrated into the wrong side",
    "p2_normal_flip": "P2's normal pointing out of the slab",
    "p2_no_z2": "P2's Israel without the Z2 doubling",
    "threshold_sub_minus": "the threshold computed against -1 instead of our tension",
    "seat_control": "the control cell seated in the index",
    "leave_out_keeps": "the leave-out keeping the facing cell",
    "quarter_as_ours": "P2's quarter tension taken positive (+1/4)",
}


def mutants():
    base = {n for n, ok in checks(compute()) if ok}
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            r = checks(compute())
            failed = [n.split()[0] for n, ok in r if not ok and n in base]
        except Exception as ex:                      # a mutant that crashes the computation is also caught
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-22s %-55s %s" % (k, desc, ("caught by " + ", ".join(failed)) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("m1_facing.py -- item 197: facing the other plane, not the reflection (near-horizon class)\n")
    print("L1: unique solution %s (local mirror forced); far-side discriminant %s" % (d["L1"]["sol"], d["L1"]["far_disc"]))
    print("single-plane cap at 2m/ell = 0.0739: rho = %.3f sigma, p = %.3f sigma on OUR plane" % (d["cap"]["rho"], d["cap"]["p"]))
    print("\nfacing (P1 at the RS tension only; P2 a Z2 plane at depth y2):")
    for x in XS:
        f = d["face"][x]
        print("  2m/ell=%-6g ell=%7.4gm y_s=%.5gm  P1 added matter %g  min NEC(P2) %.2e  max e2 %+.4f" %
              (x, f["ell"], f["ys"], f["p1_rho"], f["nec_min"], f["emax"]))
        for name, b in f["bands"].items():
            print("      remainder after q2 = %-28s %s" % (name, "positive on y2/y_s in [%.3f, %.3f]" % b if b else "never positive"))
    print("\nthreshold (q2 = +1): 2m/ell = %.5f, ell = %.4fm" % (d["thr"], 2 / d["thr"]))
    for k, v in d["thr_q"].items():
        print("threshold (q2 = %s): 2m/ell = %.5f, ell = %.4fm" % (k, v, 2 / v))
    cy = d["cy"]
    print("\ncypher, native ordering:  E", cy["allE"])
    for l in OPS:
        print("  %-12s MAIN %s  controls %s  | leave-out MAIN %s" % (l, cy["all"][l][0], cy["all"][l][1:], cy["leave"][l][0]))
    if d["eng2"]:
        print("\nsecond engine: threshold ell = %.4fm" % (2 / d["eng2"]["threshold"]))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
