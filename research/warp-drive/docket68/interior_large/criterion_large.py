"""criterion_large.py -- 405-3: the interior's criterion derived from what O1b and O1c need, not chosen.

M, 405: "The criterion - for the math/cypher".  M, 410, on the board's "phi <= 1e-4" pass mark of item 392 (carried over
from the record's practice, never derived): "this is the failure point, and it is yours".

What O1b and O1c ask of the large hole's 5D interior (INTERIOR-REQUIRED (a)-(c)) is yes or no, so each becomes a sign
condition on a quantity the computation holds (deduced, within the record's ansatz; the record computes in Euclidean
signature, g_tautau = s T / Dl^2, so inside the horizon, s < 0, the Lorentzian g_tt = -s T / Dl^2):
  (a) a forward clock: s, whose gradient is timelike exactly when N^2 = -g_ss + g_sx^2 / g_xx > 0; along any traveller
      its rate is then at least 1/N (reverse Cauchy-Schwarz for two timelike vectors);
  (b) no inner horizon: within the ansatz an inner horizon is where the static Killing field turns null again,
      g_tt = 0; so g_tt > 0, and the spheres and the x-direction alive, S > 0 and B > 0;
  (c) curvature finite to 273's region (not measured here; every computed step is finite by construction, and its
      growth per halving is the measure still owed).
A cell is one requirement at one node of one slice.  It is VIOLATED if its quantity is <= 0, UNDECIDED if the
quantity's measured error is at least its size, and decided otherwise.  The criterion is E = 0, E counting violated and
undecided cells: no number is chosen, and no factor multiplies the error.  The error is measured, not assumed: here the
disagreement between the two independent meshes that both reached the half's end (the fourth attempt,
zeno_half_dsem_10.pkl, and the fifth, zeno_half_dsem5_10.pkl), at the fifth's nodes and at common s, each attempt's
nearest saved step moved to s by its own s-slope.  That disagreement cannot see an error both share: the static start
(the same in both) and the departure from Einstein's law (xi) are not in it, and are named as owed, not as passed.

python3 criterion_large.py              -- the table over the half (nine slices); CRITERION-405.tsv
python3 criterion_large.py --start PKL  -- the same with the shared start's error added (item 411): PKL is the same half
                                          (dsem5, n = 10) run from another resolution's static start; each cell's
                                          error is the meshes' disagreement plus the starts'; CRITERION-411.tsv
python3 criterion_large.py --selftest | --mutants
"""
import sys, pickle
import numpy as np, mpmath as mp

MUT = set()
SLICES = (-0.6, -0.8, -1.0, -1.2, -1.4, -1.6, -1.8, -1.9, -2.0)
REQS = ("N2", "gtt", "S", "B")
FIFTH, FOURTH = "zeno_half_dsem5_10.pkl", "zeno_half_dsem_10.pkl"


def quantities(sv, xv, X, b):
    """the requirements' quantities at nodes xv of slice s from the fields X (rows T, S, A, B, F)"""
    T, S, A, B, F = X
    f = 1 - sv; Dl = 1 / b + (1 - xv ** 2) / f; g = 2 - xv ** 2
    gss = A / (f ** 4 * sv) / Dl ** 2; gsx = xv * F / (2 * f ** 3) / Dl ** 2; gxx = 4 * B / (f ** 2 * g) / Dl ** 2
    sgn = -1 if "sign" in MUT else 1
    out = {"N2": sgn * (-gss + gsx ** 2 / gxx), "gtt": -sv * T / Dl ** 2, "S": S, "B": B}
    if "nogtt" in MUT:
        out["gtt"] = np.abs(out["gtt"])
    return out


def cells(q, err):
    """(violated, undecided) counts for one requirement over nodes"""
    viol = q <= 0
    und = (~viol) & (err >= np.abs(q))
    return int(viol.sum()), int(und.sum())


def scheme(path):
    import zeno_run as Z
    R = pickle.load(open(path, "rb")); mesh = R.get("mesh", "dsem5")
    kw = dict(edges=Z.DSEM5_EDGES, ns=Z.DSEM5_NS) if mesh == "dsem5" else dict(ns=Z.DSEM_NS)
    return R, Z.FoldedDSEM(R.get("n", 10), Z.B, Z.STATIC, Z.KAP, Z.AT, n0=Z.SAT_N0, **kw)


def at(R, I, sv):
    """the fields at s = sv: the nearest saved step, moved to sv by its own s-slope (not moved under mutant noslope)"""
    import zeno_run as Z
    m = I.m; P = np.repeat(Z.P_EXP, m); ts, ys = R["t"], R["y"]
    k = int(np.argmin(np.abs((1 - np.exp(ts)) - sv))); lam = ts[k]; ss = 1 - np.exp(lam); e = np.exp(-P * lam)
    X = (e * ys[:5 * m, k]).reshape(5, m)
    Xs = (-(e * (ys[5 * m:, k] - P * ys[:5 * m, k])) / np.exp(lam)).reshape(5, m)
    X, Xs = I.brane_values(ss, X, Xs)
    return (X if "noslope" in MUT else X + Xs * (sv - ss)), Xs, ss


def table(slices=SLICES, quiet=False, start=None):
    """rows (s, requirement, min q, mesh error/|q|, start error/|q|, total/|q|, at x, violated, undecided) and E; the
    start error is zero unless start names the half run from another static start"""
    import zeno_run as Z, deturck_exact as D
    R5, I5 = scheme(FIFTH); R4, I4 = scheme(FOURTH); xs = I5.xn; rows = []
    Rb, Ib = scheme(start) if start else (None, None)
    for sv in slices:
        X5, _, s5 = at(R5, I5, sv); X4, Xs4, s4 = at(R4, I4, sv)
        parts = D.parts_of(I4, X4, Xs4); X4i = np.zeros_like(X5)
        for j, xv in enumerate(xs):
            p = next(pp for pp in parts if pp["lo"] - 1e-12 <= xv <= pp["hi"] + 1e-12)
            for e, n in enumerate(D.NAMES):
                X4i[e, j] = float(D.poly_at(p["nodes"], p["w"], p["vals"][n], mp.mpf(xv))[0])
        q5, q4 = quantities(sv, xs, X5, Z.B), quantities(sv, xs, X4i, Z.B)
        qb = quantities(sv, xs, at(Rb, Ib, sv)[0], Z.B) if start else q5
        for r in REQS:
            em = np.abs(q5[r] - q4[r]); es = np.abs(q5[r] - qb[r]); err = em + es
            v, u = cells(q5[r], err); a = np.abs(q5[r]); j = int(np.argmax(err / a))
            rows.append((sv, r, float(q5[r].min()), float((em / a).max()), float((es / a).max()),
                         float((err / a).max()), float(xs[j]), v, u))
        if not quiet:
            print("s %5.2f: " % sv + "; ".join("%s min %.2e, error/|q| mesh %.1e start %.1e total %.1e (x %.3f), "
                                                "violated %d, undecided %d" % r[1:] for r in rows[-4:]), flush=True)
    E = sum(r[7] + r[8] for r in rows)
    if not quiet:
        print("E = %d over %d cells (%d slices x %d nodes x %d requirements)" % (
            E, len(slices) * len(xs) * len(REQS), len(slices), len(xs), len(REQS)))
    return rows, E


def run(start=None):
    out = "CRITERION-411.tsv" if start else "CRITERION-405.tsv"
    rows, E = table(start=start)
    with open(out, "w") as fh:
        if start:
            fh.write("s\trequirement\tmin_q\tmesh_error_over_q\tstart_error_over_q\ttotal_error_over_q\tat_x"
                     "\tviolated\tundecided\n")
            for r in rows:
                fh.write("%.2f\t%s\t%.6e\t%.6e\t%.6e\t%.6e\t%.4f\t%d\t%d\n" % r)
        else:
            fh.write("s\trequirement\tmin_q\tmax_error_over_q\tat_x\tviolated\tundecided\n")
            for r in rows:
                fh.write("%.2f\t%s\t%.6e\t%.6e\t%.4f\t%d\t%d\n" % (r[0], r[1], r[2], r[3], r[6], r[7], r[8]))
    return E


# ---------------------------------------------------------------------------------------------- selftest / mutants
def selftest(quiet=False):
    ok = []
    def say(m):
        if not quiet:
            print(m, flush=True)
    # K1: on the reference (T = S = A = B = 1, F = 0) inside, every quantity is known in closed form and positive
    s_, b = -0.7, 1.0; xv = np.linspace(0.05, 0.95, 7); X = np.vstack([np.ones((4, 7)), np.zeros((1, 7))])
    q = quantities(s_, xv, X, b); f = 1 - s_; Dl = 1 / b + (1 - xv ** 2) / f
    k1 = (np.allclose(q["N2"], -1 / (f ** 4 * s_ * Dl ** 2), rtol=1e-14) and np.allclose(q["gtt"], -s_ / Dl ** 2,
                                                                                      rtol=1e-14)
          and np.all(q["N2"] > 0) and np.all(q["gtt"] > 0))
    ok.append(k1); say("K1 the quantities on the reference interior equal their closed forms and are positive: %s" % k1)
    # K2: counting -- an error at least the quantity's size is undecided (equality included); q <= 0 is violated
    qq = np.array([1.0, 0.5, 0.2, -0.1, 0.0]); ee = np.array([0.1, 0.5, 0.3, 0.0, 0.0])
    k2 = cells(qq, ee) == (2, 2)
    ok.append(k2); say("K2 cells: two violated (q <= 0), two undecided (error >= |q|, equality included): %s" % k2)
    # K3: an inner horizon in the data is caught -- T through zero makes g_tt <= 0 at those nodes
    X3 = X.copy(); X3[0, 3:] = np.array([0.0, -0.02, -0.05, -0.1])
    v3, _ = cells(quantities(s_, xv, X3, b)["gtt"], np.zeros(7))
    k3 = v3 == 4
    ok.append(k3); say("K3 an inner horizon (T through zero) is counted as violated at its four nodes: %s" % k3)
    # K4: the recorded numbers -- the two meshes at s = -2.0
    rows, E = table(slices=(-2.0,), quiet=True); d = {r[1]: r for r in rows}
    k4 = (E == 0 and abs(d["N2"][3] - 4.8e-5) < 0.05e-5 and abs(d["N2"][2] - 7.48e-5) < 0.01e-5
          and abs(d["gtt"][2] - 2.49e-2) < 0.01e-2)
    ok.append(k4); say("K4 at s = -2.0: E = %d, N^2 min %.3e, its error/|q| %.2e (recorded 7.48e-5, 4.8e-5): %s" % (
        E, d["N2"][2], d["N2"][3], k4))
    return all(ok)


def mutants():
    caught = 0; names = ["sign", "nogtt", "noslope"]
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-8s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    if a and a[0] == "--start":
        sys.exit(0 if run(a[1]) == 0 else 1)
    sys.exit(0 if run() == 0 else 1)
