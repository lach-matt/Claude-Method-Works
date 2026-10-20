#!/usr/bin/env python3
"""settle_late.py -- item 540: whether the hole settles at late times, for the math to determine.  M: "whether the hole
settles at late times - for the math to determine".  Labels: computed (exact unless marked numerical), READ, deduced,
theorized, M's.  The N1* session (N1STAR-PROOF section 10, settle5.py) found the class's modes and their ringdown and
left settling open; this file determines what the math determines now.

  S0 (read) M's words, verbatim in the rulings file, 540.
  S1 (deduced, READ; computed exactly) The end state, if there is one, is Tangherlini of the final mass.  A stationary
     solution in the class has three commuting Killing fields (d_t, d_phi1, d_phi2), the phi-ones vanishing on the
     axes; in vacuum the 2-planes orthogonal to them are then integrable (Emparan and Reall, hep-th/0110258v2 p. 5,
     READ), so the metric is a Killing block plus a 2-metric.  Both reflections remove the t-phi and phi1-phi2 terms of
     the block (computed: the twist xi ^ d xi of the time Killing field vanishes; control: without the reflections it
     does not), so the end state is static, and the only asymptotically flat static vacuum black hole in five dimensions
     is Tangherlini (Gibbons, Ida and Shiromizu, gr-qc/0203004, READ).  The class excludes rotation (settle5 T1).
  S2 (READ, deduced; computed exactly) Linear settling in the class, the metric included.  The class carries only
     scalar- and tensor-type modes of even l >= 2 and the l = 0 mass shift (settle5 T1; Kodama and Ishibashi,
     hep-th/0305147v3, READ: the k = 0 mode is "a shift of the mass parameter of the black hole").  Their master
     quantities decay as tau^-2 in energy at every order (Hung, Keller and Wang, arXiv:1809.05144v1, Theorem 2, READ via
     settle5), and in Kodama and Ishibashi's gauge the metric components are those quantities, "represented as
     combinations of this field and its derivatives" ((3.12), (3.14); tensor type H_T = r^(-3/2) Phi), whose
     coefficients carry H = m + 6x in their denominators: positive on the whole exterior for l >= 2 (computed; control
     H = m - 30x fails).  So the linearised metric settles, in that gauge, to a change of mass -- the part
     Hung, Keller and Wang left untreated, for this class.  Their potential is settle5's exactly (computed).
  S3 (computed, numerical) The record's own nonlinear evolution taken to late times.  hf_mirror5's scheme (five-
     dimensional vacuum, T^2 with both reflections, cohomogeneity three; lam = 0.1, A = 1, seed 1) through the shell
     and on to v = 40 (thirty-seven times the final horizon radius, nine e-folds of the least-damped mode), at two
     resolutions:
     - the round part is Tangherlini of one mass at every radius probed, to 2e-7, unchanged in v (mu_f = 1.18689, the
       Isaacson prediction 1.18229 plus the second-order offset 4.6e-3 of hf_mirror5 X5); the apparent horizon closes
       onto sqrt(mu_f), round to 1e-4;
     - the non-round part falls from 1.15e-2 at the shell's end to 6.6e-5 at v = 40 (run a), its late maximum below its
       maximum at v = 14-24: no growth.  Below about 1e-3 its fall is at the scheme's floor (constraint residuals 1e-4 at
       16 x 10), so the late rate is not resolved; the early fall, v = 6-14, is at about the least-damped mode's rate.
  S4 (computed) The two resolutions agree on the final mass to 1e-4 and both bound the late non-round part.
  S5 (theorized, named) A proof of nonlinear settling in the class.  The nearest theorem READ, Dafermos and Holzegel
     (gr-qc/0510051): Tangherlini "orbitally stable (in the fully non-linear theory) with respect to vacuum perturbations
     of initial data preserving triaxial Bianchi IX symmetry" -- solutions depending on (t, r) alone.  The class here
     depends on (t, r, theta); its nonlinear stability is the five-dimensional counterpart of Klainerman and Szeftel's
     polarized axisymmetric case, open in the field.

So the math determines: if the hole settles, it settles to Tangherlini of the final mass (proved); linearly it does
(proved, metric included); in the full nonlinear equations it does, to the scheme's resolution (computed); a proof of
the nonlinear statement is open.

The runs are checkpointed, so a container restart costs only the steps since the last checkpoint.
python3 settle_late.py [--selftest | --mutants | --run NAME]     (the runs take about an hour each; --run resumes)
"""
import json, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hf_mirror5 as H

DATA = os.path.join(HERE, "data")
# name: (lam, A, Ny, Nx, m0, v_end); the shell passes past null infinity over 0.5 < v < 3.5
RUNS = {"a": (0.1, 1.0, 16, 10, 1.0, 40.0), "b": (0.1, 1.0, 20, 16, 1.0, 40.0)}
V_LATE, DV_LATE, CFL, EVERY = 4.0, 0.04, 0.8, 0.25
Y_PROBE = (0.5, 0.8, 1.0)


def probe(g, d, mu):
    """the non-round part at fixed y: the squashing fields' amplitude, W's spread over the sphere and its mean's
    departure from Tangherlini of mass mu; the shift's amplitude"""
    W = 1 + g.Y ** 3 * d["w"]
    out = []
    for y0 in Y_PROBE:
        i = int(np.argmin(np.abs(g.y - y0)))
        y = g.y[i]
        out.append(dict(y=float(y), F=float(np.abs(d["F"][i]).max()), G=float(np.abs(d["G"][i]).max()),
                        Wspread=float(W[i].max() - W[i].min()), Wmean=float(W[i].mean()),
                        dWt=float(W[i].mean() - (1 - mu * y ** 4)), q=float(np.abs(d["q"][i]).max())))
    return out


def run(name):
    lam, A, Ny, Nx, m0, v_end = RUNS[name]
    wd = os.environ.get("SETTLE_DIR", DATA)                  # the runs write elsewhere; the pinned histories land here
    ck = os.path.join(wd, "settle_late_%s.ckpt.npz" % name)
    hj = os.path.join(wd, "settle_late_%s.json" % name)
    g = H.Grid(Ny, Nx, H.YEX)
    data = H.Data(lam, A, m0=m0)
    fb, fa = H.filters(g)
    mu_end = data.mu_pred(10.0)
    if os.path.exists(ck):
        z = np.load(ck)
        st = [z["s0"], z["s1"], z["s2"], z["s3"]]
        v, nxt = float(z["v"]), float(z["nxt"])
        hist = json.load(open(hj))["hist"]
    else:
        Z = np.zeros((Ny + 1, Nx + 1))
        st = [Z.copy(), Z.copy(), np.full(Nx + 1, -m0 * H.YEX), np.zeros(Nx + 1)]
        v, nxt, hist = 0.0, 0.0, []
    t0, i = time.time(), 0
    while True:
        k1, d = H.rhs(g, st, v, data)
        if v >= nxt - 1e-9:
            rec = H.diag(g, st, d, v, data)
            rec["probe"] = probe(g, d, mu_end)
            hist.append(rec)
            nxt += EVERY
            print(json.dumps({"v": rec["v"], "P": rec["P"], "q": rec["q"], "dW": rec["dW"],
                              "probe_F": [p["F"] for p in rec["probe"]]}), flush=True)
        if v >= v_end - 1e-9:
            break
        if v < V_LATE:
            dv = min(lam * 0.125, nxt - v)
        else:
            speed = H.YEX ** 3 * np.abs(1 + H.YEX ** 3 * st[2]).max() / 4       # the excision's outgoing speed
            dv = min(DV_LATE, CFL * (g.y[-1] - g.y[-2]) / speed, nxt - v)
        s2 = [a + 0.5 * dv * b for a, b in zip(st, k1)]; k2 = H.rhs(g, s2, v + dv / 2, data)[0]
        s3 = [a + 0.5 * dv * b for a, b in zip(st, k2)]; k3 = H.rhs(g, s3, v + dv / 2, data)[0]
        s4 = [a + dv * b for a, b in zip(st, k3)]; k4 = H.rhs(g, s4, v + dv, data)[0]
        st = [a + dv / 6 * (b1 + 2 * b2 + 2 * b3 + b4) for a, b1, b2, b3, b4 in zip(st, k1, k2, k3, k4)]
        st = [fb(st[0]), fb(st[1]), fa(st[2]), fa(st[3])]
        v += dv
        i += 1
        if not np.all(np.isfinite(st[0])) or np.abs(st[3]).max() > 1e3:
            raise FloatingPointError("blew up at v = %.3f" % v)
        if i % 10 == 0:
            np.savez(ck + ".tmp.npz", s0=st[0], s1=st[1], s2=st[2], s3=st[3], v=v, nxt=nxt)
            json.dump({"cfg": RUNS[name], "hist": hist}, open(hj + ".tmp", "w"))
            os.replace(ck + ".tmp.npz", ck)
            os.replace(hj + ".tmp", hj)
    json.dump({"cfg": RUNS[name], "hist": hist, "done": True, "mu_end": mu_end}, open(hj, "w"))
    print("done", name, "%.0fs this leg" % (time.time() - t0), flush=True)


# ------------------------------------------------------------------ the determination
import importlib.util
import sympy as sp

RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
WORDS = "whether the hole settles at late times - for the math to determine"
MUT = set()
QNM_S2, QNM_T2 = 0.9477 + 0.2561j, 1.5106 + 0.3575j        # [CLY03b] Tables 1 and 3, n = 0, l = 2 (via settle5, READ)
ER_READ = ("Let xi(i), 1 <= i <= D-2 be commuting Killing vector fields such that for each i, (a) ... vanishes at at "
           "least one point of the spacetime ... and (b) ... Then the two planes orthogonal to the xi(i) are "
           "integrable")                                    # Emparan-Reall, hep-th/0110258v2 p. 5
GIS_READ = "We prove the uniqueness theorem for asymptotically flat static vacuum black hole solutions in higher " \
           "dimensional space-times"                        # Gibbons-Ida-Shiromizu, gr-qc/0203004 abstract
KI_READ = ("all gauge-invariant variables can be represented as combinations of this field and its derivatives",
           "H_T is gauge-invariant by itself", "a shift of the mass parameter of the black hole")   # hep-th/0305147v3
DH_READ = ("orbitally stable (in the fully non-linear theory) with respect to vacuum perturbations of initial data "
           "preserving triaxial Bianchi IX symmetry")       # Dafermos-Holzegel, gr-qc/0510051 abstract


def _settle5():
    spec = importlib.util.spec_from_file_location("sl_settle5", os.path.join(HERE, "..", "n1star", "settle5.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def words():
    return WORDS in open(RULINGS, encoding="utf-8").read()


def endpoint(control=False):
    """S1: a stationary T^2-invariant metric in the class, in the block form the integrability theorem gives, loses its
    t-phi and phi1-phi2 terms under the reflections, so the time Killing field is hypersurface orthogonal (static)"""
    r, th = sp.symbols("r theta", positive=True)
    X = sp.symbols("t r theta p1 p2")
    names = ["tt", "t1", "t2", "11", "12", "22"]
    c = {k: sp.Function("g" + k)(r, th) for k in names}
    full = sp.Matrix([[c["tt"], 0, 0, c["t1"], c["t2"]], [0, 1, 0, 0, 0], [0, 0, r ** 2, 0, 0],
                      [c["t1"], 0, 0, c["11"], c["12"]], [c["t2"], 0, 0, c["12"], c["22"]]])
    keep = full
    for i in (3, 4):                                         # phi_i -> -phi_i: components odd in phi_i must vanish
        R = sp.eye(5); R[i, i] = -1
        inv = R * keep * R
        if not control:
            keep = (keep + inv) / 2
    xi = [keep[0, j] for j in range(5)]                      # the lowered time Killing field
    dxi = [[sp.diff(xi[b], X[a]) - sp.diff(xi[a], X[b]) for b in range(5)] for a in range(5)]
    tw = 0
    for a in range(5):
        for b in range(5):
            for d in range(5):
                if len({a, b, d}) == 3:
                    tw += sp.simplify(xi[a] * dxi[b][d]) ** 2
    return sp.simplify(tw) == 0 and keep[0, 3] == 0 and keep[3, 4] == 0


def linear(control=False):
    """S2: the class carries only scalar- and tensor-type modes (settle5 T1); Kodama-Ishibashi's reconstruction of the
    scalar-type metric from the master field has the coefficient H = m + 6x in its denominators, positive on the whole
    exterior for l >= 2, and their potential is settle5's"""
    S5 = _settle5()
    l, x = sp.symbols("l x", positive=True)
    m = l * (l + 2) - 3
    H = m + 6 * x if not control else m - 30 * x
    pos = all(sp.N(H.subs({l: L, x: X0})) > 0 for L in (2, 4, 6) for X0 in (0, sp.Rational(1, 2), 1))
    r, rh, V = S5.potentials(2, "scalar")
    xx = rh ** 2 / r ** 2
    m2 = 5
    Q = (81 * 16 * xx ** 3 + 12 * (4 * 13 * m2 + 3 * (-1) * 4 * 1) * xx ** 2 - 36 * (-m2 + 12) * m2 * xx
         + 16 * m2 ** 3 + 60 * m2 ** 2)
    VKI = (1 - xx) * Q / (16 * r ** 2 * (m2 + 6 * xx) ** 2)
    return bool(S5.t1() and pos and sp.simplify(VKI - V) == 0)


def _maxima(v, a, v0):
    out = []
    for i in range(1, len(a) - 1):
        if v[i] >= v0 and a[i] > a[i - 1] and a[i] >= a[i + 1]:
            out.append((v[i], a[i]))
    return out


def analyse(name, v0=8.0):
    J = json.load(open(os.path.join(DATA, "settle_late_%s.json" % name)))
    h = J["hist"]
    mu = H.Data(*J["cfg"][:2], m0=J["cfg"][4]).mu_pred(10.0)
    rh = mu ** 0.5
    v = np.array([r["v"] for r in h])
    res = {"v_end": float(v[-1]), "mu": mu, "rh": rh, "probes": []}
    for k in range(len(h[0]["probe"])):
        a = np.array([max(r["probe"][k]["F"], r["probe"][k]["G"]) for r in h])
        w = np.array([r["probe"][k]["Wspread"] for r in h])
        mx = _maxima(v, a, v0)
        if MUT and "flat" in MUT:
            mx = [(vv, a[np.searchsorted(v, v0)]) for vv, _ in mx]
        rate = -np.polyfit([p[0] for p in mx], np.log([p[1] for p in mx]), 1)[0] if len(mx) >= 3 else float("nan")
        gap = float(np.median(np.diff([p[0] for p in mx]))) if len(mx) >= 3 else float("nan")
        i0, i1 = int(np.searchsorted(v, v0)), len(v) - 1
        res["probes"].append(dict(y=h[0]["probe"][k]["y"], rate=float(rate), gap=gap, n=len(mx),
                                  ratio=float(a[i1] / a[i0]), wratio=float(w[i1] / w[i0]),
                                  dWt_end=float(h[-1]["probe"][k]["dWt"]),
                                  drift=float(abs(h[-1]["probe"][k]["Wmean"] - h[-9]["probe"][k]["Wmean"]) / 2.0)))
    return res


def settled(name):
    """S3: the run's late state -- the round part against one Tangherlini mass at every probe, the horizon's
    roundness, the non-round part's fall and its late bound"""
    J = json.load(open(os.path.join(DATA, "settle_late_%s.json" % name)))
    h = J["hist"]
    v = np.array([r["v"] for r in h])
    amp = np.array([max(max(p["Wspread"], p["F"], p["G"], p["q"]) for p in r["probe"]) for r in h])
    if "growth" in MUT:
        amp = amp * np.exp(0.2 * np.maximum(v - 20, 0))
    late = [r for r in h if r["v"] >= 20]
    dl = np.array([[p["dWt"] / p["y"] ** 4 for p in r["probe"]] for r in late])
    if "two_masses" in MUT:
        dl[:, 0] += 1e-3
    mu_end = J.get("mu_end") or H.Data(*J["cfg"][:2], m0=J["cfg"][4]).mu_pred(10.0)
    mu_f = mu_end - float(dl.mean())
    i0 = int(np.searchsorted(v, 3.75))
    ve = v[-1]
    return dict(v_end=float(ve), mu_end=mu_end, mu_f=mu_f, d_spread=float(np.ptp(dl.mean(0))),
                d_drift=float(dl.std(0).max()), r_lo=h[-1]["r_lo"], r_hi=h[-1]["r_hi"],
                a_shell=float(amp[i0]), a_end=float(amp[-1]), fall=float(amp[-1] / amp[i0]),
                late_max=float(amp[v >= ve - 10].max()), mid_max=float(amp[(v >= 14) & (v <= 24)].max()),
                res=float(max(r["resv"] for r in late)))


def compute():
    o = dict(words=words(), endpoint=endpoint(), endpoint_ctrl=endpoint(True), linear=linear(),
             linear_ctrl=linear(True), runs={n: settled(n) for n in RUNS
                                            if os.path.exists(os.path.join(DATA, "settle_late_%s.json" % n))})
    return o


def checks(o):
    ck = {"S0": o["words"], "S1": o["endpoint"] and not o["endpoint_ctrl"],
          "S2": o["linear"] and not o["linear_ctrl"]}
    good = []
    for n, r in o["runs"].items():
        good.append(r["v_end"] >= 40 - 1e-9 and r["d_spread"] < 1e-5 and r["d_drift"] < 1e-6
                    and r["r_lo"] ** 2 - 1e-4 <= r["mu_f"] <= r["r_hi"] ** 2 + 1e-4
                    and r["r_hi"] - r["r_lo"] < 2e-4 and r["fall"] < 2e-2 and r["late_max"] < r["mid_max"])
    ck["S3"] = len(good) == len(RUNS) and all(good)
    if len(o["runs"]) == len(RUNS):
        a, b = o["runs"]["a"], o["runs"]["b"]
        ck["S4"] = abs(a["mu_f"] - b["mu_f"]) < 1e-4 and max(a["late_max"], b["late_max"]) < 5e-4
    else:
        ck["S4"] = False
    return ck


def report(o=None):
    o = o or compute()
    ck = checks(o)
    print("S0 M's words (540) verbatim: %s" % ck["S0"])
    print("S1 the end state, if any, is static and so Tangherlini (Emparan-Reall; Gibbons-Ida-Shiromizu): %s" % ck["S1"])
    print("S2 linear settling in the class, metric included (Kodama-Ishibashi; Hung-Keller-Wang): %s" % ck["S2"])
    for n, r in o["runs"].items():
        print("   run %s %s to v %.1f: mu_f %.6f (one mass at every probe, spread %.1e, drift %.1e); horizon %.5f-%.5f; "
              "non-round %.2e -> %.2e (x %.1e), late max %.1e < %.1e; residual %.1e"
              % (n, RUNS[n][2:4], r["v_end"], r["mu_f"], r["d_spread"], r["d_drift"], r["r_lo"], r["r_hi"],
                 r["a_shell"], r["a_end"], r["fall"], r["late_max"], r["mid_max"], r["res"]))
    print("S3 each run settles: %s; S4 the two resolutions agree: %s" % (ck["S3"], ck["S4"]))
    return ck


def selftest(quiet=False):
    o = compute()
    ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


MUTANTS = {"growth": "a late growth e^(0.2 (v - 20)) put into the non-round part (S3)",
           "two_masses": "one probe's round part moved off the common mass (S3)"}


def mutants():
    caught = 0
    for m, why in MUTANTS.items():
        MUT.clear(); MUT.add(m)
        ok = selftest(quiet=True)
        caught += not ok
        print("mutant %-11s %s  (%s)" % (m, "caught" if not ok else "MISSED", why))
    MUT.clear()
    print("%d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--run" in sys.argv:
        run(sys.argv[sys.argv.index("--run") + 1])
    elif "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    elif "--selftest" in sys.argv:
        r = selftest()
        print("selftest:", "PASS" if r else "FAIL")
        sys.exit(0 if r else 1)
    else:
        report()
