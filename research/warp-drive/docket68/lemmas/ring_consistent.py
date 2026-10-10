#!/usr/bin/env python3
"""ring_consistent.py -- the rim's balance with the corridor's own tension entered (items 208, 209).  Computed by import
of corridor_shape.py / rim_profile.py, deduced where marked; checked by an adversarial verifier in the item-208 critic
pass (its findings F5, F1 and F2 survived; the sign result "stronger than stated"); seated on item 208 (206):
Z3b OPEN on the ring, M1's record corrected; 2026-10-10.

forming_rim.py F3b (ii) balances the rim (B, Z2 images) with a ring lambda = a sigma (1 - cos t)(1 + 2 cos t) > 0, and
rim_profile.py P5 evaluates it at 0.013-0.10 a sigma over the marginal family.  That count gives the corridor's sheet the
tension -sigma at the rim (forming_rim TENS["corr"] = -1), which is rim_readme R5's coincidence law -- facing sheets
meeting at y2 -> 0 -- while the meeting angle t comes from the tilted marginal corridor.  The two inputs are from two
different corridors.

  C1 (computed, sympy) the balance with the corridor's tension left as tau sigma: the sheets pull the rim outward by
     R_x = sigma (-2 cos 2t - 2 tau cos t), R_y = 0, so the ring that holds it is lambda/(a sigma) = -cos 2t - tau cos t;
     tau = -1 gives back F3b's (1 - cos t)(1 + 2 cos t) exactly
  C2 (computed, imported) the marginal corridor's own stress at its rim, every admissible member: energy density
     rho_rim > 0 and rho + p_r = 0, so its pull along its conormal is -p_r = rho_rim > 0 -- a positive tension,
     tau = rho_rim ell/(3m) in sigma's units (sigma = (2/kappa5^2)(3/ell), the stress in 2/kappa5^2 per m)
  C3 (deduced from C1, C2) every admissible member meets the plane below 45 deg, where cos 2t > 0; with tau >= 0 the
     ring is then negative: lambda/(a sigma) = -0.60 to -1.16 at ell/m = 8.5415 over the members computed (the seated
     count gives +0.013 to +0.70 at the same angles).  In the flat
     limit the bank is computed in (ell >> m) tau >> 1 and lambda -> -a rho_rim cos t (2/kappa5^2): the corridor's pull
     dominates the planes' tension, and the junction must push back.  So the rim does not balance with a ring of positive
     tension: it needs a junction of NEGATIVE tension -- a strut, in compression.  Read as a Nambu-Goto ring (energy
     density = tension, P5's reading) that strut has negative energy and breaks the NEC; with energy density >= 0 and
     positive pressure it keeps the NEC but is not pure tension
  C4 (computed) members past 45 deg balance with no junction at all at ell/m = -3 cos 2t / (rho_rim cos t) = 0.29-4.2,
     outside the flat limit their bank is computed in, and their tangential null energy turns negative inside the
     corridor (near r = 2.5-2.6m) -- in the scan the edge of admissibility falls within a degree of 45 deg; at the rim
     itself the tangential null energy stays positive, so the coincidence is not an identity
  C5 (computed) corridor_shape S2's "at most 0.76 (m/ell) E" is not reproduced on the corrected bank: the marginal
     members carry E_corr = q (m/ell) E with q = 0.67-5.66 (box members), 2.71-4.22 at slope 0, depth 1-1.5m
So the ring as seated -- positive, NEC-keeping, 0.013-0.10 a sigma -- does not belong: it is the product of R5's -sigma
entered at a rim the marginal corridor reaches at an angle.  What the balance asks for, with the corridor's own tension,
is a junction in compression of the corridor's own scale; and the ring's coefficient was in any case broad (a free family
of launches, a Pade flat-limit bulk; 209).
Imports rim_profile.py (and through it corridor_shape.py).  Stdlib + sympy (+ mpmath).  python3 ring_consistent.py
[--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = {}
_C = {}
WINDOW = 8.5415
PAST45 = ((1.95, 0.25), (2.0, 0.5), (2.05, 0.0), (2.1, 0.0))
WIDE = ((1.5, 0.0), (1.9, 0.0), (2.0, 1.0))


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def shape():
    if "shape" not in _C:
        rp = _load(os.path.join(HERE, "rim_profile.py"), "rc_rim_profile")
        _C["rp"] = rp
        _C["shape"] = rp.shape()
    return _C["shape"]


# ============================================================================================================== C1
def balance():
    import sympy as sp
    th, tau, S = sp.symbols("theta tau sigma", real=True)
    v = lambda a: sp.Matrix([sp.cos(a), sp.sin(a)])
    img = lambda e: sp.Matrix([e[0], -e[1]])
    o, ours, p2, corr = v(0), v(sp.pi), v(sp.pi - 2 * th), v(sp.pi - th)
    R = S * o + S * ours + S * p2 + S * img(p2) + tau * S * (corr + img(corr))
    lam = sp.simplify(sp.expand_trig(R[0] / (2 * S)))                  # the ring pulls 2 lambda / a toward the axis
    if MUT.get("drop_images"):
        R = S * o + S * ours + S * p2 + tau * S * corr
        lam = sp.simplify(sp.expand_trig(R[0] / (2 * S)))
    seated = (1 - sp.cos(th)) * (1 + 2 * sp.cos(th))
    return {"Ry": sp.simplify(R[1]), "lam": lam,
            "form": sp.simplify(sp.expand_trig(lam - (-sp.cos(2 * th) - tau * sp.cos(th)))) == 0,
            "seated": sp.simplify(sp.expand_trig(lam.subs(tau, -1) - seated)) == 0, "f": sp.lambdify((th, tau), lam)}


# ========================================================================================================= C2, C3
def member(d, s):
    cs, ks, bulk = shape()
    R = cs.marginal(ks, bulk, d, 0.0, s, rmax=12.0)
    rows = R["rows"]
    r, Y, Y1, rho, rad, tan = rows[-1][:6]
    th = math.atan(abs(Y1) / math.sqrt(bulk.at(r, max(Y, 1e-6))["B"][0]))
    if MUT.get("corridor_negative"):
        rho = -abs(rho)
    imin = min(range(len(rows)), key=lambda i: rows[i][5])
    return {"rim": R["rim"], "theta": th, "rho_rim": rho, "rad_rim": rad, "tan_rim": tan,
            "min_tan": rows[imin][5], "min_tan_r": rows[imin][0], "min_rho": min(x[3] for x in rows),
            "admissible": bool(R["rim"]) and R["rim"] > 3.01 and min(x[5] for x in rows) > 0 and min(x[3] for x in rows) > 0}


def family():
    shape()
    fam = {(d, s): member(d, s) for d, s in _C["rp"].FAMILY + list(WIDE)}
    past = {(d, s): member(d, s) for d, s in PAST45}
    return fam, past


def compute():
    b = balance()
    fam, past = family()
    f = b["f"]
    rows = {}
    for k, m in fam.items():
        tau = m["rho_rim"] * WINDOW / 3
        rows[k] = dict(m, tau=tau, lam=f(m["theta"], tau), lam_seated=f(m["theta"], -1),
                       flat=-m["rho_rim"] * math.cos(m["theta"]))
    ringless = {}
    for k, m in past.items():
        c2 = math.cos(2 * m["theta"])
        ringless[k] = dict(m, ell_m=(-3 * c2 / (m["rho_rim"] * math.cos(m["theta"]))) if c2 < 0 and m["rho_rim"] > 0 else None)
    return {"b": b, "rows": rows, "ringless": ringless}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    b = d["b"]
    add("C1 the balance with the corridor's tension tau sigma: R_y = 0 and lambda/(a sigma) = -cos 2t - tau cos t; tau = -1 "
        "gives back F3b's (1 - cos t)(1 + 2 cos t)", b["Ry"] == 0 and b["form"] and b["seated"])
    rows = d["rows"]
    adm = {k: v for k, v in rows.items() if v["admissible"]}
    add("C2 every admissible member computed carries a positive tension at its rim: rho_rim > 0 with rho + p_r = 0 there",
        len(adm) >= 7 and all(v["rho_rim"] > 0 and abs(v["rad_rim"]) < 1e-9 for v in adm.values()))
    add("C3 every admissible member meets the plane below 45 deg, and with its own tension the ring is negative at "
        "ell/m = 8.5415 (-0.60 to -1.16 a sigma; the seated count gives +0.013 to +0.70 at the same angles); in the flat "
        "limit lambda -> -a rho_rim cos t < 0",
        all(math.degrees(v["theta"]) < 45 for v in adm.values()) and all(-1.17 < v["lam"] < -0.59 for v in adm.values())
        and all(v["lam_seated"] > 0 for v in adm.values()) and all(v["flat"] < 0 for v in adm.values()))
    rl = d["ringless"]
    add("C4 members past 45 deg balance with no junction only at ell/m = 0.29-4.2, outside the flat limit, and their "
        "tangential null energy turns negative inside the corridor (r = 2.4-2.7m) though it is positive at the rim",
        all(math.degrees(v["theta"]) > 45 for v in rl.values()) and all(v["ell_m"] and 0.25 < v["ell_m"] < 4.3 for v in rl.values())
        and all(v["min_tan"] < 0 < v["tan_rim"] and 2.4 < v["min_tan_r"] < 2.7 for v in rl.values()))
    return res


MUTANTS = {"drop_images": "the Z2 images left out of the balance",
           "corridor_negative": "the corridor's rim energy density entered negative (R5's sign)"}


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
        print("  mutant %-18s %-55s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("ring_consistent.py -- the rim's balance with the corridor's own tension\n")
    print("C1 lambda/(a sigma) =", d["b"]["lam"])
    for (dd, s), v in sorted(d["rows"].items()):
        print("  d %.2f s %.2f rim %.2f theta %5.2f rho_rim %+.4f tau(8.54) %+.3f  lambda %+.3f a sigma (seated count %+.3f) "
              "flat-limit lambda %+.4f (2/k5^2) a  %s" % (dd, s, v["rim"], math.degrees(v["theta"]), v["rho_rim"], v["tau"],
                                                        v["lam"], v["lam_seated"], v["flat"], "ADM" if v["admissible"] else "not"))
    for (dd, s), v in sorted(d["ringless"].items()):
        print("  past 45: d %.2f s %.2f theta %5.2f no junction at ell/m %.3f; tangential at rim %+.3e, minimum %+.3e at r %.2f"
              % (dd, s, math.degrees(v["theta"]), v["ell_m"], v["tan_rim"], v["min_tan"], v["min_tan_r"]))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
