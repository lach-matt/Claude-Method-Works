#!/usr/bin/env python3
"""entrypoint.py -- the entry point t, rebuilt from the ionisation energies, and the
f test run for the first time.

TWO FINDINGS ARE WITHDRAWN HERE AND BOTH WERE MINE OR THE RECORD'S, NOT THE BOOK'S.

  T-01, mine.  I reported that sections 34.7 and 34.9 define t incompatibly: 34.9
  gives t = (a-L)/(U-L), a fraction of the corridor that cannot exceed 1, while 34.7
  measures 1.028 at p and 1.785 at d.  THERE IS NO CONTRADICTION.  Register 1334
  states the input and it is not the walk's carried `a`:

      "nu = c*sqrt(R/IE) gives a = (n-nu)/sqrt(p) from ONE OBSERVATION with no
       comparison.  18 of 51 fall INSIDE their corridor, 33 OUTSIDE, and a_meas is
       systematically TOO LARGE."

  a_meas is measured from the ionisation energy, it usually lies ABOVE the corridor,
  and t > 1 is exactly what that means.  The record had the definition, the count and
  the reason.  I constructed the contradiction by assuming `a` meant the walk's `a`.

  34re-04, the record's.  It reports that "1.028 at p is no mean or median of any
  printed row -- UNREPRODUCIBLE", and that "1.785/1.028 is 0.25% from sqrt(3), not
  0.19%".  Both halves fall.  1.028 IS the median of register 1337's four p values,
  every one of which is rebuilt here from the ionisation energies; and the 0.25%
  divides two ROUNDED printed numbers, where the unrounded ratio gives the book's own
  0.19%.  That is the precision class method/proofs/precision.py exists for.

WHAT IS REBUILT
  a_meas = (n - nu) / sqrt(p),  nu = sqrt(R / IE),  p = n - l - 1,  R = 13.6056931 eV
  t      = (a_meas - L) / (U - L), read at the subshell's OPENING
  Twelve printed values, all exact: register 1334's six across the 3p filling, and
  register 1337's six t values at four p and two d openings.

AND THE f TEST, WHICH COULD NOT BE RUN BEFORE
  Register 1337 closes: "no f test -- no f subshell has a two-sided corridor, so
  sqrt(6) = 2.4495 is predicted and unmeasured."  M's ruling of 6 September 2026
  (RULINGS-R4e.md sec 1) admits g to the candidate set, and 5g is what gives the 5f
  opening a floor.  SO 5f HAS A TWO-SIDED CORRIDOR AND THE TEST RUNS.

REFUSALS
  Protactinium's first ionisation energy is an ESTIMATE, not a precise measurement.
  The f result is therefore reported with its sensitivity across the plausible range
  and never as a single number.  The corridors are the node-only form, which is what
  register 1337 read; the finished form is a different object and is not mixed in.
  Nothing is repaired.

stdlib only.  --selftest asserts registers 1334 and 1337 value for value.
"""
import argparse, math, statistics, sys

R_EV = 13.605693122994

# Standard first ionisation energies in eV.  Protactinium's is an estimate and is
# marked; every other value here is a measurement, and the twelve figures registers
# 1334 and 1337 print are reproduced from them exactly, which is the check on the set.
IE = {
    "Al": 5.985769, "Si": 8.15168, "P": 10.486686, "S": 10.36001,
    "Cl": 12.967632, "Ar": 15.7596112,
    "Ga": 5.999302, "In": 5.7863557, "Tl": 6.1082871,
    "Y": 6.21726, "La": 5.5769,
    "Pa": 5.89,
}
IE_ESTIMATED = {"Pa"}

# The node-only corridors at each opening, as walk.py computes them.  5f's floor is
# 5g's, and exists only under the ruling.
CORRIDOR = {
    "3p": ("Al", 13, 3, 1, 0.0, 1.3660254),
    "4p": ("Ga", 31, 4, 1, 0.0, 1.7071068),
    "5p": ("In", 49, 5, 1, 0.5773503, 1.9840594),
    "6p": ("Tl", 81, 6, 1, 1.0, 2.2247449),
    "4d": ("Y", 39, 4, 2, 0.0, 1.3660254),
    "5d": ("La", 57, 5, 2, 0.7071068, 1.7071068),
    "5f": ("Pa", 91, 5, 3, 0.0, 1.3660254),
}

# What the registers print.
REG_1334 = {"Al": 1.49, "Si": 1.71, "P": 1.86, "S": 1.85, "Cl": 1.98, "Ar": 2.07}
REG_1337 = {"3p": 1.0925, "4p": 1.0331, "5p": 1.0124, "6p": 1.0237,
            "4d": 1.8453, "5d": 1.7240}


def nu(el):
    return math.sqrt(R_EV / IE[el])


def a_meas(n, l, el):
    return (n - nu(el)) / math.sqrt(n - l - 1)


def t_at(sub, ie=None):
    el, Z, n, l, lo, hi = CORRIDOR[sub]
    if ie is not None:
        a = (n - math.sqrt(R_EV / ie)) / math.sqrt(n - l - 1)
    else:
        a = a_meas(n, l, el)
    return (a - lo) / (hi - lo), a


def t_form(l):
    return math.sqrt(l * (l + 1) / 2)


# ----------------------------------------------------------- the q = 0 question
# Register 1337 reads t "at the subshell's OPENING", where the entrant already holds
# one electron (q = 1), and says t rises linearly with occupancy.  The law's p is the
# node count, which is the q = 0 quantity.  Nowhere in the record are the two put
# together.  This section does, using register 1335's own slopes and, for the four p
# fillings, slopes rebuilt from the ionisation energies below.
IE_FILL = {
    "3p": (3, 1, {13: 5.985769, 14: 8.15168, 15: 10.486686, 16: 10.36001, 17: 12.967632, 18: 15.7596112}),
    "4p": (4, 1, {31: 5.999302, 32: 7.899435, 33: 9.78855, 34: 9.752392, 35: 11.81381, 36: 13.9996055}),
    "5p": (5, 1, {49: 5.7863557, 50: 7.343918, 51: 8.608389, 52: 9.009808, 53: 10.45126, 54: 12.1298436}),
    "6p": (6, 1, {81: 6.1082871, 82: 7.4166799, 83: 7.285516, 84: 8.414, 85: 9.31751, 86: 10.7485}),
}
# The 5f filling, protactinium to americium.  The entrant is 5f at every step; 6d and
# 7s move but do not enter.  Pa's value is the estimate; the other four are measured.
IE_5F = {91: (5.89, 2), 92: (6.19405, 3), 93: (6.26554, 4), 94: (6.02576, 6), 95: (5.97381, 7)}
REG_1335 = {"3p": (0.1054, 0.927), "4p": (0.0670, 0.931), "5p": (0.0505, 0.953),
            "6p": (0.0276, 0.953), "4d": (0.1129, 0.671), "5d": (0.0427, 0.344)}


def fit(xs, ys):
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    sl = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    ic = my - sl * mx
    ssr = sum((y - ic - sl * x) ** 2 for x, y in zip(xs, ys))
    sst = sum((y - my) ** 2 for y in ys)
    return sl, ic, 1 - ssr / sst


def q0():
    out = {}
    for sub, (n, l, ies) in IE_FILL.items():
        el, Z, _, _, lo, hi = CORRIDOR[sub]
        W = hi - lo
        q = list(range(1, 7))
        a = [(n - math.sqrt(R_EV / ies[z])) / math.sqrt(n - l - 1) for z in sorted(ies)]
        sl, ic, r2 = fit(q, a)
        t1 = (a[0] - lo) / W
        out[sub] = dict(slope=sl, r2=r2, tslope=sl / W, t1=t1,
                        t0_back=t1 - sl / W,          # one electron's slope back from q = 1
                        t0_fit=(ic - lo) / W)         # the fitted line's own intercept
    for sub in ("4d", "5d"):
        el, Z, n, l, lo, hi = CORRIDOR[sub]
        W = hi - lo
        sl = REG_1335[sub][0]
        t1 = t_at(sub)[0]
        out[sub] = dict(slope=sl, r2=REG_1335[sub][1], tslope=sl / W, t1=t1,
                        t0_back=t1 - sl / W, t0_fit=None)
    # 5f: the actinide first ionisation energies are flat across the filling
    q = [v[1] for v in IE_5F.values()]
    a = [5 - math.sqrt(R_EV / v[0]) for v in IE_5F.values()]
    sl, ic, r2 = fit(q, a)
    W = CORRIDOR["5f"][5] - CORRIDOR["5f"][4]
    out["5f"] = dict(slope=sl, r2=r2, tslope=sl / W, t1=t_at("5f")[0],
                     t0_back=t_at("5f")[0] - sl / W * 2, t0_fit=ic / W)
    return out


def measure():
    filling = {el: a_meas(3, 1, el) for el in REG_1334}
    ts = {k: t_at(k)[0] for k in CORRIDOR}
    p = [ts[k] for k in ("3p", "4p", "5p", "6p")]
    d = [ts[k] for k in ("4d", "5d")]
    medp, meand = statistics.median(p), statistics.mean(d)
    sens = [(ie, t_at("5f", ie)[0]) for ie in (5.69, 5.79, 5.89, 5.99, 6.09, 6.19)]
    return dict(filling=filling, ts=ts, p=p, d=d, medp=medp, meand=meand, q0=q0(),
                ratio=meand / medp, sens=sens,
                hi_p=medp / t_form(1) - 1, hi_d=meand / t_form(2) - 1,
                hi_f=ts["5f"] / t_form(3) - 1,
                r_rounded=1.785 / 1.028, r_exact=meand / medp)


def report(o):
    print("  THE ENTRY POINT, REBUILT FROM THE IONISATION ENERGIES")
    print()
    print("  a_meas = (n - nu) / sqrt(p),  nu = sqrt(R / IE),  p = n - l - 1")
    print()
    print("  1. REGISTER 1334, the 3p filling at constant n, l and p")
    print(f"     {'el':<4}{'IE (eV)':>10}{'nu':>9}{'a_meas':>9}   printed")
    for el in ("Al", "Si", "P", "S", "Cl", "Ar"):
        print(f"     {el:<4}{IE[el]:>10.4f}{nu(el):>9.4f}{o['filling'][el]:>9.4f}   "
              f"{REG_1334[el]}   {'agrees' if abs(round(o['filling'][el], 2) - REG_1334[el]) < 1e-9 else 'DIFFERS'}")
    print("     Six of six.  a_meas rises as the subshell fills, which is register 1334's")
    print("     point: nu depends on OCCUPANCY and the law has no coordinate for it.")
    print()
    print("  2. REGISTER 1337, t at the opening")
    print(f"     {'sub':<5}{'el':<4}{'a_meas':>9}{'L':>11}{'U':>11}{'t':>9}   printed")
    for k in ("3p", "4p", "5p", "6p", "4d", "5d"):
        el, Z, n, l, lo, hi = CORRIDOR[k]
        t, a = t_at(k)
        print(f"     {k:<5}{el:<4}{a:>9.4f}{lo:>11.7f}{hi:>11.7f}{t:>9.4f}   {REG_1337[k]}   "
              f"{'agrees' if abs(round(t, 4) - REG_1337[k]) < 1.1e-4 else 'DIFFERS'}")
    print("     Six of six.  Every t exceeds 1 because a_meas sits ABOVE the corridor --")
    print("     register 1334 counts it: 18 of 51 inside, 33 outside, systematically large.")
    print()
    print(f"     median p = {o['medp']:.4f}  (printed 1.028)   against t(p) = 1")
    print(f"     mean   d = {o['meand']:.4f}  (printed 1.785)   against t(d) = sqrt(3) = {t_form(2):.4f}")
    print(f"     ratio    = {o['ratio']:.4f}   {100 * (o['ratio'] / math.sqrt(3) - 1):+.2f}% from sqrt(3)")
    print(f"     the record's 34re-04 reports 0.25%, from 1.785/1.028 = {o['r_rounded']:.6f},")
    print("     which divides two ROUNDED printed numbers.  The book's 0.19% is right.")
    print()
    print("  3. THE f TEST, which register 1337 calls 'predicted and unmeasured'")
    print("     It could not be run because no f opening had a two-sided corridor.  Under")
    print("     M's ruling g is in the candidate set, 5g gives the 5f opening a floor, and")
    print("     the corridor at protactinium is two-sided.  So the test runs.")
    t, a = t_at("5f")
    print(f"     Pa 5f: IE = {IE['Pa']} eV (AN ESTIMATE), nu = {nu('Pa'):.6f}, "
          f"a_meas = {a:.6f}")
    print(f"     corridor (0.0000000, 1.3660254)   t = {t:.4f}   against sqrt(6) = {t_form(3):.4f}")
    print()
    print(f"     {'l':<3}{'measured':>10}{'t(l)':>10}{'high by':>10}")
    for lab, m, l in (("p", o["medp"], 1), ("d", o["meand"], 2), ("f", o["ts"]["5f"], 3)):
        print(f"     {lab:<3}{m:>10.4f}{t_form(l):>10.4f}{100 * (m / t_form(l) - 1):>+9.2f}%")
    print()
    print("     Register 1337 records 'a common factor of 1.029, both p and d 2.9% high,")
    print("     WHICH TWO l VALUES CANNOT ADJUDICATE'.  There are three now, and the factor")
    print("     is NOT common: it drifts with l.")
    print()
    print("  4. AND THE f RESULT IS ROBUST TO THE ESTIMATE")
    print("     Protactinium's ionisation energy is an estimate, so the test is reported")
    print("     across the plausible range rather than as one number:")
    print(f"     {'IE (eV)':>9}{'t':>9}{'vs sqrt(6)':>12}")
    for ie, tv in o["sens"]:
        print(f"     {ie:>9.2f}{tv:>9.4f}{100 * (tv / t_form(3) - 1):>+11.2f}%")
    lo_, hi_ = o["sens"][0][1], o["sens"][-1][1]
    print(f"     Over the whole range t runs {lo_:.4f} to {hi_:.4f}, so f is high by "
          f"{100 * (lo_ / t_form(3) - 1):+.1f}% to {100 * (hi_ / t_form(3) - 1):+.1f}%,")
    print("     above the p and d factor at every point.  For t to reach sqrt(6) exactly the")
    print("     ionisation energy would have to be 4.97 eV, far below any estimate.")
    print()
    print("  5. THE OPEN QUESTION, AND ITS SHAPE -- t at q = 0")
    print("     Register 1337 reads t at the opening, where the entrant already holds one")
    print("     electron, and says t rises linearly with occupancy.  The law's p is the node")
    print("     count, a q = 0 quantity.  Nowhere does the record carry t back to q = 0.")
    print()
    print(f"     {'sub':<5}{'a-slope':>9}{'r^2':>7}{'1335':>16}{'t(q=1)':>9}{'t(0) back':>11}{'t(0) fit':>10}")
    for sub in ("3p", "4p", "5p", "6p", "4d", "5d", "5f"):
        r = o["q0"][sub]
        reg = f"{REG_1335[sub][0]:+.4f} ({REG_1335[sub][1]})" if sub in REG_1335 else "--"
        fitv = "--" if r["t0_fit"] is None else f"{r['t0_fit']:.4f}"
        print(f"     {sub:<5}{r['slope']:>+9.4f}{r['r2']:>7.3f}{reg:>16}{r['t1']:>9.4f}"
              f"{r['t0_back']:>11.4f}{fitv:>10}")
    pb = [o["q0"][k]["t0_back"] for k in ("3p", "4p", "5p", "6p")]
    pf = [o["q0"][k]["t0_fit"] for k in ("3p", "4p", "5p", "6p")]
    db = [o["q0"][k]["t0_back"] for k in ("4d", "5d")]
    print()
    print(f"     {'':<12}{'q = 1':>10}{'q = 0, back':>13}{'q = 0, fit':>12}{'predicted':>11}")
    print(f"     {'p median':<12}{o['medp']:>10.4f}{statistics.median(pb):>13.4f}{statistics.median(pf):>12.4f}{1.0:>11.4f}")
    print(f"     {'  excess':<12}{100*(o['medp']-1):>+9.2f}%{100*(statistics.median(pb)-1):>+12.2f}%{100*(statistics.median(pf)-1):>+11.2f}%")
    print(f"     {'d mean':<12}{o['meand']:>10.4f}{statistics.mean(db):>13.4f}{'--':>12}{t_form(2):>11.4f}")
    print(f"     {'  excess':<12}{100*(o['meand']/t_form(2)-1):>+9.2f}%{100*(statistics.mean(db)/t_form(2)-1):>+12.2f}%")
    f = o["q0"]["5f"]
    print(f"     {'f':<12}{f['t1']:>10.4f}{f['t0_back']:>13.4f}{f['t0_fit']:>12.4f}{t_form(3):>11.4f}")
    print(f"     {'  excess':<12}{100*(f['t1']/t_form(3)-1):>+9.2f}%{100*(f['t0_back']/t_form(3)-1):>+12.2f}%{100*(f['t0_fit']/t_form(3)-1):>+11.2f}%")
    print()
    print("     Three of register 1335's four p slopes rebuild from the ionisation energies to")
    print("     the fourth decimal; 6p rebuilds as the slope per corridor width, +0.0276, where")
    print("     the register prints that figure as the slope in a.  Its r^2 is exact either way.")
    print()
    print("     READ TOGETHER.  The 2.9% the record could not derive is mostly the occupancy")
    print("     offset: one electron's worth of slope, at the opening.  Carried back to q = 0")
    print("     the p and d excesses fall from about +3% to within a percent, and the sign is")
    print("     no longer fixed.  f does NOT move: the actinide first ionisation energies are")
    print("     flat across the 5f filling (slope near zero), because an actinide ionises from")
    print("     7s and not from 5f, so a_meas at protactinium is reading the wrong electron.")
    print("     The survey has no measured f channel above Z = 81; the actinide 5f rows are")
    print("     computed and unwitnessed.  So the f point cannot be sharpened from the data")
    print("     the corpus holds.  That is the question's shape, and it is OPEN.")
    print()
    print("  Nothing is repaired here.")


FIXTURES = """registers 1334 and 1337, value for value:
  1334  Al 1.49  Si 1.71  P 1.86  S 1.85  Cl 1.98  Ar 2.07
  1337  3p 1.0925  4p 1.0331  5p 1.0124  6p 1.0237  4d 1.8453  5d 1.7240
  1337  median p 1.028, mean d 1.785, ratio 0.19% from sqrt(3)
  1334  a_meas is systematically too large: 33 of 51 lie outside their corridor"""


def selftest():
    o = measure()
    checks = []

    def eq(n, got, want):
        checks.append((n, got, want, got == want))

    for el, want in REG_1334.items():
        eq(f"1334: {el}", round(o["filling"][el], 2), want)
    for k, want in REG_1337.items():
        eq(f"1337: t at {k}", round(o["ts"][k], 4), want)
    eq("1337: median p", round(o["medp"], 3), 1.028)
    eq("1337: mean d", round(o["meand"], 3), 1.785)
    eq("1337: ratio is 0.19% from sqrt(3)",
       round(100 * (o["ratio"] / math.sqrt(3) - 1), 2), 0.19)
    eq("34re-04's 0.25% comes from rounded inputs",
       round(100 * (o["r_rounded"] / math.sqrt(3) - 1), 2), 0.25)
    eq("every t exceeds 1", all(v > 1 for k, v in o["ts"].items() if k != "5f"), True)
    eq("f is high by more than p or d",
       o["hi_f"] > o["hi_p"] and o["hi_f"] > o["hi_d"], True)
    eq("f stays above the p/d factor across the estimate range",
       all(tv / t_form(3) - 1 > max(o["hi_p"], o["hi_d"]) for _, tv in o["sens"]), True)
    q = o["q0"]
    for sub in ("3p", "4p", "5p"):
        eq(f"1335: {sub} slope rebuilds", round(q[sub]["slope"], 4), REG_1335[sub][0])
        eq(f"1335: {sub} r^2 rebuilds", round(q[sub]["r2"], 3), REG_1335[sub][1])
    eq("1335: 6p r^2 rebuilds", round(q["6p"]["r2"], 3), REG_1335["6p"][1])
    eq("1335: 6p prints the slope per corridor width", round(q["6p"]["tslope"], 4), REG_1335["6p"][0])
    pb = statistics.median([q[k]["t0_back"] for k in ("3p", "4p", "5p", "6p")])
    eq("p at q = 0 is within a percent of 1", abs(pb - 1) < 0.01, True)
    eq("5f slope is flat", abs(q["5f"]["slope"]) < 0.005, True)
    print(FIXTURES)
    print()
    bad = 0
    for n, got, want, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {n:<38} {got!r:<10} expected {want!r}")
        bad += not ok
    print()
    print("SELFTEST OK" if not bad else f"SELFTEST FAILED: {bad}")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    report(measure())
    return 0


if __name__ == "__main__":
    sys.exit(main())
