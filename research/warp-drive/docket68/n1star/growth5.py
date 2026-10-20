#!/usr/bin/env python3
"""growth5.py -- the go/no-go at the prescribed wavelength 10 l5 (ROUTES-OPEN.md section 2; M, 2026-10-20, "all 3
please"): the growth factor exp int K dv of the computed solution on the record's own domain, measured non-rigorously,
and a finite-difference linear amplification beside it.  Labels: computed, deduced, READ.

The domain is hf_core5's: seed mu0 = 1, A = 1, the record's envelope on [1/2, 7/2], the ingoing slices continued inward
to the core boundary x_K = 1 on the seed, y_core = (sqrt 72/L)^(-1/8), L := mu0/l5^2.  lam = 10 l5 is lam/sqrt(mu0) =
10/sqrt(L): 1.000 at L = 100 (y_core = 1.361, r = 0.540) and 0.3162 at L = 1000 (y_core = 1.815, r = 0.304) (paper R7).

K.  The constant of a linear energy estimate for the reduced equations linearised about the computed solution is, up
to a frame constant, the sup over the slice of the first derivatives of the metric's departure from the seed.  Two
measures are recorded at every step of the scheme, in units 1/sqrt(mu0):
    K_v   := max |d_v P_i|           the radiation field's own rate, O(1) in lam (P ~ lam A env sin(v/lam) r^-3/2);
    K_all := max over the dimensionless fields {P1, P2, beta, r U, W - W_V} of the Bondi chart (r U is the shift's
             orthonormal component; W_V = 1 - mu(v) y^4 is five-dimensional Vaidya at the Isaacson mean mass, the
             record's own reference, so that the shell's mass is not counted as a departure) and the derivatives
             {d_v, d_r, r^-1 d_th}, d_r = -(y^3/2) d_y and r^-1 d_th = -2 y^2 sqrt(1 - x^2) d_x; the fifteen maxima
             are recorded separately at every step.  (A first run measured W against the seed, and the growth of the
             mass itself then dominated K_all: int K_all dv = 12.6 at lam = 0.1, of which 8.8 was d_r of the mass
             term.  That is the background's gradient, not the perturbation's; the field is now referenced to Vaidya.)
The growth factor is exp of the trapezoid of K over the run, sampled at every step (a first trial sampled every 0.25
and aliased the oscillation).  Whether K_v or K_all is the constant of the estimate is not decided here; both are
printed, and the finite-difference amplification below is what either must bound.

Breakdown.  The scheme's premise is that the core boundary is trapped (hf_core5 C3): the inner boundary is then
outflow and the region outside it is fixed by the data outside it.  Each run records v_break, the first v at which the
round spheres' outgoing expansion has a second zero in some column, or W at the boundary is >= 0, or a field is not
finite.  Past v_break nothing the scheme prints is a solution of anything; the growth factor is reported up to it.

Amplification.  The data are perturbed, A -> A (1 + delta), the two runs taken on the same fixed step, and
    amp := max over v, slice of |Delta F|, |Delta G|  /  max over v, x of |Delta F0|, |Delta G0| at past null infinity
is the finite-difference amplification along that one direction: a lower bound for the linear propagator's norm,
which exp int K bounds above when K is the constant of the estimate.  So amp <= exp int K is a consistency check on
the measure, not a theorem.

  G0 (computed, live) K_all = 0 on a slice of the seed alone (Tangherlini, hf_mirror5 X1); on a slice carrying the
     record's data at v = 2 over fields still zero, both measures are positive, K_all >= K_v, and the field whose
     derivative gives K_all is named.  Control: a perturbation of W alone at the boundary gives K_v = 0 with K_all > 0,
     so K_v alone is blind to it.
  G1 (computed) L = 100, lam = 1.000 (the wave's metric amplitude lam A r^-3/2 at the core boundary 2.5): the premise
     fails at v = 1.4516 (Ny = 20) and 1.4508 (Ny = 28), a second zero of the expansion; W at the boundary turns
     positive at 1.516 and 1.512 and the slice solve fails at 1.69 and 1.75, before the shell's peak at v = 2.  To the
     break, int K_v dv = 0.523 (exp 1.7), int K_all dv = 2.13 (exp 8.5).
  G2 (computed) L = 1000, lam = 0.3162 (amplitude 1.9 at the boundary), Ny = 24: the same sequence, the second zero at
     v = 1.5825, W positive at the boundary at 1.680, the slice solve failing at 1.704; to the break int K_v dv = 0.751
     (exp 2.1), int K_all dv = 12.27 (exp 2e5, from d_r of W - W_V at the deep boundary).
     the Ny = 28 and 20 runs to v = 1.75 are in progress at this commit and are seated in the next
  G3 (computed) the record's own regime as control, L = 100, lam = 0.1: complete to v = 4.5 with one zero throughout,
     int K_v dv = 1.933 (exp 6.9), int K_all dv = 8.77 (exp 6e3, from d_v of the oscillating part of W), and the
     amplification 1.713 <= exp int K_v.
  G4 (computed) the amplification to the break is 1.003 at L = 100 and 1.000 at L = 1000: the data's difference has not
     grown into the slices by then.
  So: no approximant on D_T at lam = 10 l5 comes from the record's own scheme at either seed; and the sup-norm Groenwall
  factor is no measure of the linear growth (1e3 to 1e5 against an amplification of 1.0 to 1.7), so a certified
  argument would need the propagator's norm, not a sup-norm bound.

python3 growth5.py [--selftest | --run L lam Ny Nx [delta] | --report]
Runs write data/growth5_runs.json (one key per run); --selftest reads it and asserts the pinned figures.
"""
import sys, os, json, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "lemmas"))
import hf_mirror5 as H                 # noqa: E402
from hf_core5 import y_core            # noqa: E402

RUNS = os.path.join(HERE, "data", "growth5_runs.json")
V_END, CFL, SAMPLE = 4.5, 2.0, 0.25


def fields(g, d, mu):
    """the five departures from Vaidya at the mean mass mu on a slice, from hf_mirror5's slice dictionary"""
    c2, s2 = (1 + g.X)/2, (1 - g.X)/2
    P1 = g.Y**3*(2*c2*d["G"] - s2*d["F"])/3
    P2 = g.Y**3*(2*s2*d["F"] - c2*d["G"])/3
    beta = g.Y**6*d["b"]
    rU = -g.Y**3*np.sqrt(np.maximum(1 - g.X**2, 0))*d["q"]/2          # r U, U the theta-shift: dth - U dv
    dW = g.Y**3*(d["w"] + mu*g.Y)                     # W - (1 - mu y^4)
    return {"P1": P1, "P2": P2, "beta": beta, "rU": rU, "dW": dW}


FIELDS, DERS = ("P1", "P2", "beta", "rU", "dW"), ("v", "r", "th")
MAXIMA = [f + "_" + d for f in FIELDS for d in DERS]


def K_measures(g, st, v, data, k1, d, h=1e-5):
    """K_v and K_all on the slice at v; the slice at v - h is rebuilt from the state and its rate"""
    dm = H.slice_fields(g, [a - h*b for a, b in zip(st, k1)], v - h, data)
    f, fm = fields(g, d, data.mu_pred(v)), fields(g, dm, data.mu_pred(v - h))
    best, Kall, maxima = "", 0.0, []
    for nm in FIELDS:
        ders = {"v": (f[nm] - fm[nm])/h, "r": -(g.Y**3/2)*(g.Dy @ f[nm]),
                "th": -2*g.Y**2*np.sqrt(np.maximum(1 - g.X**2, 0))*g.dx(f[nm])}
        for dn in DERS:
            m = float(np.abs(ders[dn]).max())
            maxima.append(m)
            if m > Kall:
                Kall, best = m, nm + "_" + dn
    c2, s2 = (1 + g.X)/2, (1 - g.X)/2
    F0p, G0p = data.FG(v + h, g.x); F0m, G0m = data.FG(v - h, g.x)
    Fv = (F0p - F0m)[None, :]/(2*h) + g.Iy @ k1[0]
    Gv = (G0p - G0m)[None, :]/(2*h) + g.Iy @ k1[1]
    P1v = g.Y**3*(2*c2*Gv - s2*Fv)/3; P2v = g.Y**3*(2*s2*Fv - c2*Gv)/3
    Kv = float(max(np.abs(P1v).max(), np.abs(P2v).max()))
    return Kv, Kall, best, maxima


def fixed_step(lam, g, yex, mu_final=1.25):
    """a step the excision's outgoing speed allows through the whole run (W_ex = 1 - mu y^4 at mu <= mu_final),
    landing on every sample time"""
    speed = max(1.0, yex**3*abs(1 - mu_final*yex**4)/4)
    dv = min(lam*0.125, CFL*(g.y[1] - g.y[0])/speed)
    n = int(np.ceil(SAMPLE/dv))
    return SAMPLE/n, n


def run(L, lam, Ny, Nx, delta=0.0, v_end=V_END, log=print):
    yex = float(y_core(1.0, L))
    g = H.Grid(Ny, Nx, yex); data = H.Data(lam, 1.0 + delta, m0=1.0); fb, fa = H.filters(g)
    dv, nper = fixed_step(lam, g, yex)
    Z = np.zeros((Ny + 1, Nx + 1))
    st = [Z.copy(), Z.copy(), np.full(Nx + 1, -yex), np.zeros(Nx + 1)]
    out = {"cfg": dict(L=L, lam=lam, Ny=Ny, Nx=Nx, delta=delta, yex=yex, r_core=yex**-2, dv=dv, maxima=MAXIMA),
           "steps": [], "samples": [], "v_break": None, "break_why": None, "end": None}
    v, i, t0 = 0.0, 0, time.time()
    try:
        while True:
            k1, d = H.rhs(g, st, v, data)
            Kv, Kall, lab, maxima = K_measures(g, st, v, data, k1, d)
            W = 1 + g.Y**3*d["w"]
            r_lo, r_hi, nz = H.horizon(g, d)
            Wex = float(W[-1].max())
            finite = bool(np.all(np.isfinite(st[0])) and np.isfinite(Kall))
            out["steps"].append([round(v, 6), Kv, Kall, lab, int(nz), Wex, maxima])
            if out["v_break"] is None and (nz > 1 or Wex >= 0 or not finite):
                out["v_break"] = round(v, 6)
                out["break_why"] = "nz=%d" % nz if nz > 1 else ("W_ex=%.3f" % Wex if Wex >= 0 else "not finite")
                log("BREAK at v = %.4f: %s" % (v, out["break_why"]))
            if i % nper == 0:
                dg = H.diag(g, st, d, v, data)
                dg.update(v=round(v, 6), Kv=Kv, Kall=Kall, Klabel=lab,
                          F=d["F"].tolist(), G=d["G"].tolist(), w=d["w"].tolist())
                out["samples"].append(dg)
                log("v %.3f Kv %.3f Kall %.3f (%s) M %.5f mu %.5f nz %d dW %.3f W_ex %.3f  %.0fs" % (
                    v, Kv, Kall, lab, dg["M_mean"], dg["mu"], nz, dg["dW"], Wex, time.time() - t0))
            if v >= v_end - 1e-9 or not finite:
                out["end"] = "complete" if finite else "not finite at v = %.4f" % v
                break
            s2 = [a + 0.5*dv*b for a, b in zip(st, k1)]; k2 = H.rhs(g, s2, v + dv/2, data)[0]
            s3 = [a + 0.5*dv*b for a, b in zip(st, k2)]; k3 = H.rhs(g, s3, v + dv/2, data)[0]
            s4 = [a + dv*b for a, b in zip(st, k3)]; k4 = H.rhs(g, s4, v + dv, data)[0]
            st = [a + dv/6*(b1 + 2*b2 + 2*b3 + b4) for a, b1, b2, b3, b4 in zip(st, k1, k2, k3, k4)]
            st = [fb(st[0]), fb(st[1]), fa(st[2]), fa(st[3])]
            v += dv; i += 1
    except (np.linalg.LinAlgError, FloatingPointError, ValueError) as e:
        out["end"] = "scheme failed at v = %.4f: %s" % (v, type(e).__name__)
        log(out["end"])
        if out["v_break"] is None:
            out["v_break"], out["break_why"] = round(v, 6), type(e).__name__
    out["seconds"] = round(time.time() - t0)
    return out


def integrals(rec):
    """trapezoid of K_v and K_all over the steps, up to v_break where there is one; and of each of the fifteen maxima"""
    vb = rec["v_break"]
    S = [s for s in rec["steps"] if vb is None or s[0] <= vb + 1e-9]
    vs = np.array([s[0] for s in S]); Kv = np.array([s[1] for s in S]); Ka = np.array([s[2] for s in S])
    M = np.array([s[6] for s in S])
    each = {nm: float(np.trapezoid(M[:, i], vs)) for i, nm in enumerate(rec["cfg"]["maxima"])}
    return float(np.trapezoid(Kv, vs)), float(np.trapezoid(Ka, vs)), float(vs[-1]), each


def amplification(base, pert):
    """max over samples and slice of |Delta F|, |Delta G| over the max of the data's own difference at y = 0"""
    num, den, per_v = 0.0, 0.0, []
    for a, b in zip(base["samples"], pert["samples"]):
        if abs(a["v"] - b["v"]) > 1e-9:
            break
        if base["v_break"] is not None and a["v"] > base["v_break"] + 1e-9:
            break
        dF = np.array(b["F"]) - np.array(a["F"]); dG = np.array(b["G"]) - np.array(a["G"])
        m = float(max(np.abs(dF).max(), np.abs(dG).max()))
        d0 = float(max(np.abs(dF[0]).max(), np.abs(dG[0]).max()))
        num, den = max(num, m), max(den, d0)
        per_v.append((a["v"], m))
    return (num/den if den > 0 else float("nan")), per_v


def key(L, lam, Ny, Nx, delta):
    return "L%g_lam%.4g_%dx%d_d%g" % (L, lam, Ny, Nx, delta)


def load():
    return json.load(open(RUNS)) if os.path.exists(RUNS) else {}


def report(R=None):
    R = R or load()
    for k, rec in sorted(R.items()):
        iv, ia, vend, each = integrals(rec)
        print("%-28s dv %.4f  end: %s  v_break %s (%s)  int K_v %.3f exp %.2f  int K_all %.3f exp %.2f  to v = %.3f" % (
            k, rec["cfg"]["dv"], rec["end"], rec["v_break"], rec["break_why"], iv, np.exp(iv), ia, np.exp(ia), vend))
        top = sorted(each.items(), key=lambda q: -q[1])[:5]
        print("    largest integrals: " + ", ".join("%s %.3f" % q for q in top))
    for k, rec in sorted(R.items()):
        if rec["cfg"]["delta"] == 0:
            kp = [q for q in R if q.startswith(k[:k.rfind("_d")]) and R[q]["cfg"]["delta"] != 0]
            for q in kp:
                amp, per_v = amplification(rec, R[q])
                print("%-28s amplification (delta = %g): %.3f" % (k, R[q]["cfg"]["delta"], amp))


# ---- live check -----------------------------------------------------------------------------------------------------
def g0(control=False):
    """K_all vanishes on the seed; on the data at v = 2 it is the radiation field's d_v (K_v = K_all at y -> 0)"""
    L, lam, Ny, Nx = 100, 0.1, 12, 8
    yex = float(y_core(1.0, L)); g = H.Grid(Ny, Nx, yex)
    Z = np.zeros((Ny + 1, Nx + 1)); st = [Z.copy(), Z.copy(), np.full(Nx + 1, -yex), np.zeros(Nx + 1)]
    seed = H.Data(lam, 0.0, m0=1.0)
    k1, d = H.rhs(g, st, 0.0, seed)
    Kv0, Kall0, _, _ = K_measures(g, st, 0.0, seed, k1, d)
    data = H.Data(lam, 1.0, m0=1.0)
    k1, d = H.rhs(g, st, 2.0, data)
    Kv, Kall, lab, _ = K_measures(g, st, 2.0, data, k1, d)
    if control:                                    # a wave in W alone: K_v = 0 and K_all > 0
        st2 = [Z.copy(), Z.copy(), np.full(Nx + 1, -yex) + 0.1*(1 - g.x**2), np.zeros(Nx + 1)]
        k1, d = H.rhs(g, st2, 0.0, seed)
        Kv, Kall, lab, _ = K_measures(g, st2, 0.0, seed, k1, d)
        return Kv < 1e-12 and Kall > 0.1
    ok = Kv0 == 0.0 and Kall0 < 1e-12 and Kall >= Kv > 0
    print("   seed: K_v %.2e K_all %.2e;  data at v = 2 (fields zero): K_v %.4f K_all %.4f from %s"
          % (Kv0, Kall0, Kv, Kall, lab))
    return ok


# ---- pinned figures ---------------------------------------------------------------------------------------------------
PINNED = {    # the runs of 2026-10-20 (data/growth5_runs.json): v_break, int K_v, int K_all to the break, amplification
    "L100_lam1_20x16_d0": dict(v_break=1.45161, int_Kv=0.5233, int_Kall=2.1344, amp=1.003),
    "L100_lam1_20x16_d0.001": dict(v_break=1.45161, int_Kv=0.5238, int_Kall=2.1375),
    "L100_lam1_28x16_d0": dict(v_break=1.45082, int_Kv=0.5214, int_Kall=2.1236),
    "L1000_lam0.3162_24x16_d0": dict(v_break=1.58251, int_Kv=0.7508, int_Kall=12.2742, amp=1.0),
    "L1000_lam0.3162_24x16_d0.001": dict(v_break=1.58251, int_Kv=0.7519, int_Kall=12.2896),
    "L100_lam0.1_20x16_d0": dict(v_break=None, int_Kv=1.9329, int_Kall=8.7663, amp=1.7132),
    "L100_lam0.1_20x16_d0.001": dict(v_break=None, int_Kv=1.9348, int_Kall=8.7755),
}


def selftest():
    ok = g0()
    print("[%s] G0 K_all = 0 on the seed; the data's own rate at past null infinity" % ("ok" if ok else "FAIL"))
    c = not g0(control=True)
    print("[%s]    control: a wave in W alone has K_v = 0 < K_all (so K_v alone would miss it)"
          % ("ok" if not c else "FAIL"))
    ok &= not c
    R = load()
    for k, pin in PINNED.items():
        if k not in R:
            print("[FAIL] %s not in %s" % (k, RUNS)); ok = False; continue
        iv, ia, vend, _ = integrals(R[k])
        good = (abs((R[k]["v_break"] or -1) - (pin["v_break"] or -1)) < 1e-6 and abs(iv - pin["int_Kv"]) < 1e-3
                and abs(ia - pin["int_Kall"]) < 1e-3)
        line = "v_break %s int K_v %.3f int K_all %.3f" % (R[k]["v_break"], iv, ia)
        if "amp" in pin:
            kp = k[:k.rfind("_d")] + "_d0.001"
            amp = amplification(R[k], R[kp])[0] if kp in R else float("nan")
            good &= abs(amp - pin["amp"]) < 1e-3 and amp <= np.exp(iv)
            line += " amplification %.3f (<= exp int K_v %.2f)" % (amp, np.exp(iv))
        tag = "G1" if "lam1_" in k else ("G2" if "L1000" in k else "G3")
        print("[%s] %s %s %s" % ("ok" if good else "FAIL", tag, k, line))
        ok &= good
    print("growth5.py: %s" % ("all checks pass" if ok else "FAILED"))
    return ok


if __name__ == "__main__":
    if "--run" in sys.argv:
        a = sys.argv[sys.argv.index("--run") + 1:]
        L, lam, Ny, Nx = float(a[0]), float(a[1]), int(a[2]), int(a[3])
        delta = float(a[4]) if len(a) > 4 else 0.0
        v_end = float(a[5]) if len(a) > 5 else V_END
        rec = run(L, lam, Ny, Nx, delta, v_end)
        k = key(L, lam, Ny, Nx, delta)
        part = RUNS.replace(".json", "_" + k + ".json")
        json.dump({k: rec}, open(part, "w"))
        print("wrote", part, "%ds" % rec["seconds"])
    elif "--merge" in sys.argv:            # the part files are intermediate (data/.gitignore); the merge is kept
        R = load()
        d = os.path.dirname(RUNS)
        parts = [f for f in sorted(os.listdir(d)) if f.startswith("growth5_runs_") and f.endswith(".json")]
        for f in parts:
            R.update(json.load(open(os.path.join(d, f))))

        def trim(x):                       # six significant digits: what the figures quote, a fifth of the bytes
            if isinstance(x, float):
                return float("%.6g" % x)
            if isinstance(x, list):
                return [trim(y) for y in x]
            if isinstance(x, dict):
                return {k: trim(y) for k, y in x.items()}
            return x
        json.dump(trim(R), open(RUNS, "w"), separators=(",", ":"))
        for f in parts:
            os.remove(os.path.join(d, f))
        report(load())
    elif "--report" in sys.argv:
        report()
    else:
        sys.exit(0 if selftest() else 1)
