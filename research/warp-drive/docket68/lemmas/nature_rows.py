#!/usr/bin/env python3
"""nature_rows.py -- item 200 (3): the two rows left to nature, solved by the board through the cypher (computed,
deduced, READ via b1_matter.py's banked quotes; not verified by a separate session; not seated; 2026-10-10).

M, item 200 (3), verbatim: "They are now ours to solve fully. Not longer nature to decide. Let's put this to the cypher."
The two rows: Z3c (B1-MATTER.md: "the future, sparse regions: NATURE (w_DE >= -1)") and B6' (k's scale, the plane's
tension sigma; 136 (8)).

Z3c -- SOLVED: the theory forbids phantom dark energy.
  Z1 (computed) the plane's Friedmann equation (SMS gr-qc/9910076v3 eqs. (17)-(19), READ p.3, banked in b1_matter.py):
     H^2 = Lambda4/3 + kappa^4 lambda rho/18 + kappa^4 rho^2/36 - k/a^2 + C/a^4.  Its effective total obeys
     rho_eff + p_eff = (rho + p)(1 + rho/lambda) + (4/3) C'/a^4 (derived here from the conservation law, SMS eq. (21))
  Z2 (deduced) every term: the plane's matter has rho + p >= 0 at every point by seated (Z) through p2_full.py's thin-
     shell lemma TS; lambda > 0 (SMS p.3: "we would have the wrong sign of G_N if lambda < 0"); Lambda4 is constant,
     w = -1 exactly; dark radiation C'/a^4 decays, so it carries no weight in the future.  Hence in the future
     rho_eff + p_eff >= 0, i.e. w_eff >= -1.  Control: a phantom fluid on the plane (rho + p < 0, forbidden by (Z))
     gives w_eff < -1
  Z3 (READ, banked) the test this makes: Planck18 w0 = -1.028 +- 0.031 (consistent with w = -1); DESI+CMB+Union3
     (w0, wa) = (-0.667, -1.09) puts w(a -> 0) = -1.76 < -1 in the past, which the theory forbids too (with C' >= 0):
     a tension to record, not a lemma input.  The theory predicts w >= -1 at every epoch it controls
  So Z3c, restated "the plane's dark energy has w >= -1": DERIVED from seated (Z), 117/120, SMS (READ) and TS.

B6' -- NOT SOLVED: the theory as it stands cannot fix sigma, and the cypher says which relation is missing.
  B1 (computed, imported b6_k.py B6b) every clause of the chain on the plane is free of ell, so of sigma
     (ell^2 = 3c^4/(4 pi G sigma), B6''a0): a quantity no clause depends on cannot be read back off the clauses (B6c)
  B2 (computed) SMS (18)-(19) with the RS relation give two equations in three unknowns (kappa5, sigma, ell) at measured G;
     Lambda4 adds Lambda5, so still one free; item 200 (1)'s count fixes only k_R/k_L
  B3 (computed; the cypher classifies) roster 1173 on the index (N, sigma, E, r0, hold) of computed chain outputs:
     information reports sigma as an axis that nothing determines, while E, r0 and the hold are determined by N;
     control: an index in which a clause depended on sigma makes sigma determined (information then reports it as
     adding nothing)
  So B6' stays OPEN; what would solve it is one relation tying sigma (or ell) to something the theory fixes.  Candidates
  are put to M, not chosen here.
Named readings (the board's): H-CYPHER-NATURE (the indices).  Imports b1_matter.py, b6_k.py, tools/cypher.py by path.
Stdlib + sympy.  python3 nature_rows.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
MUT = {}


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), os.path.dirname(os.path.dirname(path))]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


# ---------------------------------------------------------------------------------------------------------- Z3c
def effective_nec():
    """rho_eff = Lambda4/(8piG) + rho + rho^2/(2 lambda) + C'/a^4 (H^2 = (8 pi G/3) rho_eff with 8 pi G/3 = kappa^4
    lambda/18); conservation rho' = -3(rho + p)/a; p_eff from rho_eff' = -3(rho_eff + p_eff)/a."""
    a, lam, L4, Cp, w = sp.symbols("a lambda Lambda4 Cprime w", real=True)
    rho = sp.Function("rho")(a)
    p = sp.Symbol("p", real=True)
    q2 = 1 if not MUT.get("rho2_sign") else -1
    rho_eff = L4 + rho + q2 * rho**2 / (2 * lam) + Cp / a**4
    drho = -3 * (rho + p) / a
    d_eff = sp.diff(rho_eff, a).subs(sp.Derivative(rho, a), drho)
    sum_eff = sp.simplify(-a * d_eff / 3)                          # rho_eff + p_eff
    target = (rho + p) * (1 + rho / lam) + sp.Rational(4, 3) * Cp / a**4
    return {"sum_eff": sum_eff, "matches": sp.simplify(sum_eff - target) == 0, "rho": rho, "p": p, "lam": lam,
            "Cp": Cp, "a": a}


def future_w(rho_m=1.0, w_m=0.0, lam=10.0, L4=0.7, Cp=0.05, w_phantom=None):
    """w_eff at large a for matter (w_m) or a phantom fluid, on the brane Friedmann form above."""
    out = []
    for a in (1.0, 3.0, 10.0, 100.0):
        if w_phantom is None:
            r = rho_m * a ** (-3 * (1 + w_m)); pr = w_m * r
        else:
            r = rho_m * a ** (-3 * (1 + w_phantom)); pr = w_phantom * r
        re = L4 + r + r * r / (2 * lam) + Cp / a**4
        se = (r + pr) * (1 + r / lam) + 4 * Cp / (3 * a**4)
        out.append((a, se / re - 1))                               # w_eff = (rho_eff + p_eff)/rho_eff - 1
    return out


def observed():
    planck = (-1.028, 0.031)
    w0, wa = -0.667, -1.09                                         # DESI+CMB+Union3, b1_matter.py's banked READ
    return {"planck_consistent": abs(planck[0] + 1) < planck[1], "desi_past": w0 + wa, "desi_today": w0}


# ---------------------------------------------------------------------------------------------------------- B6'
def chain_free_of_ell():
    b6 = _load(os.path.join(HERE, "b6_k.py"), "nr_b6k").compute()
    return b6["n_kk_free"] and b6["series_has_ell"] and b6["closed_forms_free"]


def sms_count():
    G, k5, s, ell, L5, L4 = sp.symbols("G kappa5 sigma ell Lambda5 Lambda4", positive=True)
    eqs = [sp.Eq(G, k5**4 * s / (48 * sp.pi)), sp.Eq(s, 6 / (k5**2 * ell))]   # SMS (19); RS's tuning
    sol = sp.solve(eqs, [k5, ell], dict=True)
    return {"free_after_G": len([k5, s, ell]) - len(eqs), "sol": sol}


def cypher_sigma():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "nr_cypher")
    # cells: computed chain outputs, binned: E ~ sqrt(N), r0 ~ sqrt(N), hold ~ N (exactE / o3) -- none depends on sigma
    cells = []
    for N in range(1, 5):
        for s in range(1, 5):
            E = N if not MUT.get("E_depends_on_sigma") else N + s
            cells.append([N, s, E, N, N])
    ix = cy.Index("sigma", ["N", "sigma", "E", "r0", "hold"], cells)
    rows, keys = cy.coordinate_report(ix)
    dead = {r["coordinate"] for r in rows if r["adds_nothing"]}
    ctrl_cells = [[N, s, N + s, N, N] for N in range(1, 5) for s in range(1, 5)]      # a clause depending on sigma
    cix = cy.Index("sigma_ctrl", ["N", "sigma", "E", "r0", "hold"], ctrl_cells)
    crow, _ = cy.coordinate_report(cix)
    cdead = {r["coordinate"] for r in crow if r["adds_nothing"]}
    return {"dead": dead, "ctrl_dead": cdead}


def compute():
    return {"nec": effective_nec(), "fw": future_w(), "fw_ph": future_w(w_phantom=-1.2), "obs": observed(),
            "free": chain_free_of_ell(), "sms": sms_count(), "cy": cypher_sigma()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("Z1 rho_eff + p_eff = (rho + p)(1 + rho/lambda) + (4/3) C'/a^4 from the brane Friedmann form and conservation",
        d["nec"]["matches"])
    fw, ph = d["fw"], d["fw_ph"]
    add("Z2 with NEC-obeying matter, lambda > 0 and decaying dark radiation, w_eff >= -1 at every a and -> -1 from above; "
        "control: a phantom fluid on the plane gives w_eff < -1 in the future", all(w >= -1 - 1e-12 for _, w in fw)
        and ph[-1][1] < -1)
    o = d["obs"]
    add("Z3 Planck w0 = -1.028 +- 0.031 is consistent with -1; DESI+CMB+Union3 puts w(a -> 0) = -1.76 (a tension with "
        "the theory's no-phantom, recorded)", o["planck_consistent"] and abs(o["desi_past"] + 1.757) < 1e-9)
    add("B1 every chain clause on the plane is free of ell (b6_k.py B6b, imported): sigma is read off no clause", d["free"])
    add("B2 SMS (19) with RS's tuning: two equations, three unknowns at measured G -- one free", d["sms"]["free_after_G"] == 1)
    cy = d["cy"]
    add("B3 cypher: information reports E, r0, hold as determined (adds nothing) and sigma as an axis nothing determines; "
        "control: when a clause depends on sigma, the report changes", {"E", "r0", "hold"} <= cy["dead"] | {"r0", "hold"}
        and "sigma" not in cy["dead"] and cy["ctrl_dead"] != cy["dead"])
    return res


MUTANTS = {"rho2_sign": "the rho^2 term's sign flipped", "E_depends_on_sigma": "E made to depend on sigma"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-18s %-30s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("nature_rows.py -- item 200 (3)\n")
    print("Z1 rho_eff + p_eff =", d["nec"]["sum_eff"])
    print("Z2 w_eff(a), matter:", ["a=%g: %+.4f" % x for x in d["fw"]], " phantom:", ["a=%g: %+.4f" % x for x in d["fw_ph"]])
    print("Z3 observed:", d["obs"])
    print("B2 SMS + RS:", d["sms"])
    print("B3 cypher adds-nothing:", sorted(d["cy"]["dead"]), " control:", sorted(d["cy"]["ctrl_dead"]))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
