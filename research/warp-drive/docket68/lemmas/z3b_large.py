#!/usr/bin/env python3
"""z3b_large.py -- item 424 (2): Z3b, rays that meet the corridor keep (Z) at the large end, re-posed on C3's large
brane hole as Z3bs was at the small end (pair_math P1-P4, 318; readings Q1, 354).

M, 424: "review all the other open items in the warp theorem map, and close them".  The register's Z3b row waited on
"the bulk carrying the warp's kink into the corridor (232)" -- the record's corridor and its ring.  On the one-way
object at the large end (m1_large, 356) there is no ring and no fold, so the row is the small end's question asked of
the large hole.  Labels: computed (exact unless marked), deduced, READ, M's.  Worked in the conversation; not verified;
not seated.

  Z0 (read) M's words, verbatim in the rulings file: 177, the negative null energy "the appearance"; 183, "never
     violated" as a pair; 273, the option giving up "classical GR there" inside a small quantum region, "README only";
     318, "For the math".
  Z1 (computed; imported from rows_large Z1t and m1_large M1) In the bulk the large hole is Einstein, R_AB = -(4/ell^2)
     g_AB, so R_AB k^A k^B = 0 on every null ray: no five-dimensional null energy outside the README.  The plane's own
     four-dimensional reading is small and negative outside the face, of order (ell/r0)^2 -- the bulk's projected Weyl
     term, FW's dual stress: under 183 the appearance, never a five-dimensional violation (Z1t).
  Z2 (computed, exact; imported from arrival_large A1) The README's own flux on the plane's ingoing form is the only
     Einstein component, G_vv = 2 m'(v)/r^2, so its null energy is >= 0 on every ray iff the arrival only adds energy --
     at every arrival width (no number from SOURCE enters).
  Z3 (computed, exact) The plane's tension gives nothing on a null ray: S_ab = -sigma h_ab, and h_ab k^a k^b = 0 for the
     radial null ray of the plane's Schwarzschild form, k = (1/f, 1, 0, 0); the same for the tangential null ray.
  Z4 (read) The ring that blocked the record's (d) does not arise at the large end: m1_large says "The ring at the fold
     that blocked (d) on the record (m1_cypher M1) does not arise: the plane is smooth."
  Z5 (computed, exact) Raychaudhuri's identity in D = 4 and D = 5: for a twist-free radial null congruence,
     integral R_kk d lambda = theta_in - theta_out - integral (theta^2/(D - 2) + sigma^2) d lambda, negative whenever
     theta_in < 0 < theta_out -- pair_math P1 at either end, since nothing in it is the small end's.
  Z6 (deduced) So, as at the small end: outside 273's quantum region every classical ray segment that meets the object
     keeps 183 -- in the bulk (Z1), on the plane (Z2, Z3: S_kk = T_kk >= 0), inside our face to 273's region (focusing_
     parts F1, the core by M's 422) -- and the passage's negative, which Z5 requires on every ray the bounce turns, lies
     wholly inside the region 273 marks: 177's appearance, the reading readings Q1 proved (354) from 273, 318 and
     pair_math P1-P3, none of which is the small end's.  Z3b at the large end is DERIVED from M's rulings and computed
     results, as Z3bs is.  The Hawking flux's negative influx is quantum, outside the classical claim, as at the small
     end (355 (Q4); core_face A3).

What this does not claim: the plane's reading beyond first order in (ell/r0)^2 (rows_large); anything inside 273's
region; that SOURCE delivers the README (Z2 needs only that it adds energy).

python3 z3b_large.py [--selftest | --mutants]
"""
import os, re, sys, io, contextlib, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
_C = {}
WORDS = ((177, "appearance"), (183, "never violated"), (273, "classical GR there"), (273, "README only"),
         (318, "For the math"))
RING = "The ring at the fold that blocked (d) on the record (m1_cypher M1) does not arise: the plane is smooth."


def _load(name, alias):
    if alias not in _C:
        spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
        m = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(m)
        _C[alias] = m
    return _C[alias]


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


def bulk():
    """Z1: rows_large's Z1t, from m1_large M1"""
    o = _load("rows_large.py", "zb_rl").rows()
    return dict(null=o["bulk_null"], einstein=o["einstein"])


def flux():
    """Z2: arrival_large A1's G_vv"""
    ok, others = _load("arrival_large.py", "zb_al").vaidya_gvv()
    return ok and others


def tension_null():
    """Z3: h_ab k^a k^b on the radial and tangential null rays of the plane's Schwarzschild form"""
    r, M, th = sp.symbols("r M theta", positive=True)
    f = 1 - 2 * M / r
    h = sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2)
    kr = sp.Matrix([1 / f, 1, 0, 0])
    if "timelike" in MUT:
        kr = sp.Matrix([1 / f, 0, 0, 0])
    kt = sp.Matrix([1 / sp.sqrt(f), 0, 1 / r, 0])                 # tangential: -f/f + r^2/r^2 = 0
    return [sp.simplify((k.T * h * k)[0]) for k in (kr, kt)]


def ring():
    txt = " ".join(open(os.path.join(HERE, "m1_large.py"), encoding="utf-8").read().split())
    want = RING if "noring" not in MUT else RING.replace("does not arise", "arises")
    return want in txt


def raychaudhuri():
    """Z5: integral R_kk = theta_in - theta_out - integral(theta^2/(D-2) + sigma^2), negative for theta_in < 0 < out"""
    out = {}
    for D in (4, 5):
        l, l1 = sp.symbols("lambda lambda_1", positive=True)
        th, sg, Rkk = sp.Function("theta")(l), sp.Function("sigma")(l), sp.Function("R")(l)
        eq = sp.Eq(sp.diff(th, l), -th ** 2 / (D - 2) - sg ** 2 - Rkk)
        integrand = sp.solve(eq, Rkk)[0]                          # R_kk = -theta' - theta^2/(D-2) - sigma^2
        ti, to, Q = sp.symbols("theta_in theta_out Q", real=True)
        total = -(to - ti) - Q                                     # Q = integral (theta^2/(D-2) + sigma^2) >= 0
        sign = sp.ask(sp.Q.negative(total), sp.Q.negative(ti) & sp.Q.positive(to) & sp.Q.nonnegative(Q))
        out[D] = (sp.simplify(integrand + sp.diff(th, l) + th ** 2 / (D - 2) + sg ** 2) == 0, sign)
    return out


def report():
    print("Z0 M's words inside 177, 183, 273, 318:", words())
    print("Z1 the bulk Einstein, R_AB k^A k^B on a null ray (want 0):", bulk())
    print("Z2 the README's flux the only Einstein component, G_vv = 2 m'/r^2:", flux())
    print("Z3 h(k, k) on the radial and tangential null rays:", tension_null())
    print("Z4 the ring does not arise at the large end (m1_large):", ring())
    print("Z5 Raychaudhuri's integral negative for theta_in < 0 < theta_out (D: identity, sign):", raychaudhuri())


def selftest(quiet=False):
    ok = []
    def say(m):
        if not quiet:
            print(m, flush=True)
    z0 = words(); ok.append(z0); say("Z0 M's words verbatim inside their items: %s" % z0)
    b = bulk(); z1 = b["null"] == 0 and bool(b["einstein"]); ok.append(z1)        # R(k, k) = 0, the bulk Einstein
    say("Z1 the large hole's bulk Einstein, no five-dimensional null energy: %s" % z1)
    z2 = flux(); ok.append(z2); say("Z2 the README's flux the only Einstein component, >= 0 iff m' >= 0: %s" % z2)
    z3 = all(x == 0 for x in tension_null()); ok.append(z3)
    say("Z3 the tension gives nothing on the radial and tangential null rays: %s" % z3)
    z4 = ring(); ok.append(z4); say("Z4 the ring does not arise at the large end (m1_large's words): %s" % z4)
    rc = raychaudhuri(); z5 = all(i and s for i, s in rc.values()); ok.append(z5)
    say("Z5 Raychaudhuri's integral negative on every turned ray, D = 4 and 5: %s" % z5)
    return all(ok)


def mutants():
    caught = 0; names = ["timelike", "noring"]
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-9s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
