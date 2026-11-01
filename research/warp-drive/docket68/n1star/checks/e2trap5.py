"""e2trap5.py -- E2-PILOT section 3j (D486): Lemmas E2.7 and E2.8 harmonic by harmonic at large sigma, with a multiplier
that has a narrow core at the photon sphere and wide flanks.

Lemma E2.8's constant B_l(sigma) = ((2/m' + (M' + 2|sigma|)^2/w_I)/w_I)^(1/2) grows like 2|sigma|/w_I, and with the
symmetric tanh multipliers of checks/e2morawetz5.py (widths 0.2 to 0.98) its sup over l grows like 63 sigma, set by the
low harmonics (section 4, D452). Two changes:
  (i) every harmonic with sigma^2 > max V_l has Lemma E2.7's Lambda |sigma|/(sigma^2 - max V_l) (section 3c), which
      falls like Lambda/|sigma|, so the low harmonics cost little at large sigma;
  (ii) at and above the trapped harmonic, w_I is at most w(x_*) = -phi'''(x_*)/2 (U' = 0 there), of the order of the
      core width^-3, and w >= 0 lets the core shrink as l grows (V_l'' grows like l^2), while flanks of fixed width keep
      m' bounded below.
The multiplier is phi = tanh g, centred at x_* = r_*(sqrt 2), where U' = 0 (U = f/r^2), with
  g' = 1/s_R + (1/s_L - 1/s_R)/(1 + e^z) + beta sech^2((x - x_*)/kappa),   z = (x - x_*)/kappa_s,
in closed form g = (x - x_*)/s_R - (1/s_L - 1/s_R) kappa_s (ln(1 + e^-z) - ln 2) + beta kappa tanh((x - x_*)/kappa).
beta = 0 is D466's multiplier (s_L = 49/50, s_R = 2, kappa_s = 1/2); the core width is s_c = 1/g'(x_*) and kappa =
k s_c; the symmetric tanh of width s (s_L = s_R = s, beta = 0) is in the family. Since V_l = a U + W (a = l(l + 2) +
3/4, W = (9/4) f/r^4) and -phi U' >= 0 for this centre, w_l = (-phi W' - phi'''/2) + a (-phi U') increases with l: a
multiplier admissible (w >= 0 on R) at l is admissible at every larger l, w_I does not decrease and m', M' do not
change, so B*_l(sigma), the best over the family, is nonincreasing in l.

  T1  control: e2morawetz5's best symmetric multiplier at l = 5, sigma = 3 (21.35, centred at V_5's peak) reproduced
      by this file's multiplier and potential.
  T2  the trapped harmonic (the first l with max V_l > sigma^2) at sigma = 3, 6, ..., 96: B* against D452's 21.35,
      21.9, 27.2, 35.3, 47.7, 66.8.
  T3  sup over every l >= 0 of min(E2.7, B*) on sigma in [3, 96], steps of 0.01: l <= L computed, l > L bounded by
      B*_L (nonincreasing), l = 0 by E2.7 (sigma^2 > max V_0).
  T4  against the measured maximum over l of the cut-off norm (D444): every bound at least the measured value.
  T5  controls: a core too narrow for its harmonic fails w >= 0; B*_l(sigma) at least e2high5's computed norm at four
      (l, sigma).

Labels: E2.7 proved (section 3c), max V_l exact (a quadratic in 1/r^2); w >= 0 checked on the grid (floating point,
computed, not certified), as for D452 and D460.
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def rstar(r):
    return r + 0.5 * np.log((r - 1) / (r + 1))


XS = float(rstar(np.sqrt(2.0)))
LAM = float(rstar(4.0) - rstar(1.2))
SIG6 = (3.0, 6.0, 12.0, 24.0, 48.0, 96.0)
D452 = (21.35, 21.9, 27.2, 35.3, 47.7, 66.8)
D444 = (1.132, 0.618, 0.336, 0.181, 0.0972, 0.0519)


def grid():
    """t = ln(r - 1) from -120 (x = -59) to ln 119 (r = 120), finest near the photon sphere; U' and W' in x = r_*"""
    t = np.concatenate([np.arange(-120, -3, 0.01), np.arange(-3, 1.4, 5e-4), np.arange(1.4, np.log(119), 2e-4)])
    e = np.exp(t)
    r = 1 + e
    f = e * (2 + e) / r**2
    x = r + 0.5 * (t - np.log(2 + e))
    dU = f * (-2 / r**3 + 4 / r**5)
    dW = f * 2.25 * (-4 / r**5 + 6 / r**7)
    return x, r, dU, dW


def vpeak(l):
    """(max V_l, r at the peak): V = (1 - y)(a y + b y^2) in y = 1/r^2, dV/dy = 0 a quadratic"""
    a, b = l * (l + 2) + 0.75, 2.25
    y = (-(2 * a - 2 * b) + np.sqrt((2 * a - 2 * b)**2 + 12 * a * b)) / (6 * b)
    return (1 - y) * (a * y + b * y * y), 1 / np.sqrt(y)


def mult(x, sL, sR, ks, sc, k, xc=XS):
    """phi, phi', phi''' for the family above (chain rule on the closed-form g)"""
    d = x - xc
    D = 1 / sL - 1 / sR
    beta = 1 / sc - (1 / sR + D / 2)
    z = d / ks
    sg = 0.5 * (1 + np.tanh(z / 2))
    g = d / sR - D * ks * (np.logaddexp(0, -z) - np.log(2))
    g1 = 1 / sR + D * (1 - sg)
    g2 = -D / ks * sg * (1 - sg)
    g3 = -D / ks**2 * sg * (1 - sg) * (1 - 2 * sg)
    if abs(beta) > 1e-15:
        kap = k * sc
        y = d / kap
        ty = np.tanh(y)
        sy = 1 - ty**2
        g = g + beta * kap * ty
        g1 = g1 + beta * sy
        g2 = g2 - 2 * beta / kap * sy * ty
        g3 = g3 - 2 * beta / kap**2 * (sy**2 - 2 * sy * ty**2)
    T = np.tanh(g)
    em = np.exp(-2 * np.abs(g))
    S = 4 * em / (1 + em)**2
    p1 = g1 * S
    p3 = g3 * S - 6 * g1 * g2 * T * S + g1**3 * (-2 * S * S + 4 * S * T * T)
    return T, p1, p3


def family():
    out = [(s, s, 0.5, s, 1.0) for s in np.linspace(0.2, 0.98, 40)]
    for sR in (1.5, 2.0, 3.0):
        hp0 = 1 / sR + (1 / 0.98 - 1 / sR) / 2
        out.append((0.98, sR, 0.5, 1 / hp0, 1.0))
        for sc in np.geomspace(0.02, 1 / hp0, 31)[:-1]:
            for k in (0.5, 1.0, 2.0, 4.0):
                out.append((0.98, sR, 0.5, float(sc), k))
    return out


def admissible_table(ls, fam, G=None, verbose=False):
    """for each multiplier: m', M' on I; for each l in ls: admissible on the grid (w >= 0 on (-30, 120), the horizon
    tail as in e2morawetz5: 0.5|phi'''|/(-phi V') <= 1 and nondecreasing on (-60, -20)), and w_I"""
    x, r, dU, dW = G if G is not None else grid()
    core = (x > -30) & (x < 120)
    tail = (x > -60) & (x < -20)
    I = (r >= 1.2) & (r <= 4.0)
    a = np.array([l * (l + 2) + 0.75 for l in ls])
    P = len(fam)
    adm = np.zeros((len(ls), P), bool)
    wI = np.zeros((len(ls), P))
    m1 = np.zeros(P)
    M1 = np.zeros(P)
    for j, p in enumerate(fam):
        T, p1, p3 = mult(x, *p)
        A = -T * dU
        assert A.min() >= -1e-300, ("-phi U' < 0", p, A.min())
        B0 = -T * dW - 0.5 * p3
        m1[j], M1[j] = p1[I].min(), p1[I].max()
        wc = B0[core][None, :] + a[:, None] * A[core][None, :]
        ok = wc.min(axis=1) >= 0
        den = a[:, None] * A[tail][None, :] - (T * dW)[tail][None, :]
        num = 0.5 * np.abs(p3[tail])[None, :]
        with np.errstate(divide="ignore", invalid="ignore"):
            rat = np.where(den > 0, num / den, np.inf)
        mono = np.all(np.diff(rat, axis=1) >= -1e-12 * np.abs(rat[:, :-1]), axis=1)
        ok &= (rat.max(axis=1) <= 1) & mono
        adm[:, j] = ok
        wI[:, j] = (B0[I][None, :] + a[:, None] * A[I][None, :]).min(axis=1)
        if verbose and j % 50 == 0:
            print("    multiplier %d/%d" % (j, P), flush=True)
    adm = np.logical_or.accumulate(adm, axis=0) & (wI > 0)     # admissible at l implies at every larger l
    return adm, wI, m1, M1


def bstar(sig, adm, wI, m1, M1):
    """B*_l(sigma) for every l of the table (inf where nothing is admissible) and the minimising multiplier"""
    with np.errstate(divide="ignore", invalid="ignore"):
        B = np.sqrt((2 / m1[None, :] + (M1[None, :] + 2 * abs(sig))**2 / wI) / wI)
    B = np.where(adm, B, np.inf)
    return B.min(axis=1), B.argmin(axis=1)


def e27(l, sig):
    vm = vpeak(l)[0]
    return LAM * abs(sig) / (sig * sig - vm) if sig * sig > vm else np.inf


def trapped(sig):
    l = 0
    while vpeak(l)[0] <= sig * sig:
        l += 1
    return l


def main():
    t0 = time.time()
    ok = True
    # T1 control against e2morawetz5
    import e2morawetz5 as E
    rg, xg, fg = E.grid()
    sb, Bb, _ = E.best(5, rg, xg, fg, sigma=3.0)
    xp5 = float(rstar(vpeak(5)[1]))
    x, r, dU, dW = G = grid()
    a5 = 5 * 7 + 0.75
    T, p1, p3 = mult(x, sb, sb, 0.5, sb, 1.0, xc=xp5)
    w = -T * (a5 * dU + dW) - 0.5 * p3
    I = (r >= 1.2) & (r <= 4.0)
    wI_, m_, M_ = w[I].min(), p1[I].min(), p1[I].max()
    B_ = np.sqrt((2 / m_ + (M_ + 6.0)**2 / wI_) / wI_)
    c1 = abs(B_ / Bb - 1) < 2e-3 and abs(Bb - 21.35) < 0.01
    ok &= c1
    print("  T1 %s: e2morawetz5's best at l = 5, sigma = 3: width %.4f, B = %.4f; this file's multiplier and potential, "
          "centred at the exact peak: %.4f" % ("ok" if c1 else "FAIL", sb, Bb, B_), flush=True)
    # the table
    L = 2 * int(max(SIG6)) + 20
    ls = list(range(1, L + 1))
    fam = family()
    adm, wI, m1, M1 = admissible_table(ls, fam, G)
    print("  table: %d multipliers, l = 1..%d (%.0f s)" % (len(fam), L, time.time() - t0), flush=True)
    # T2 trapped harmonic
    rows, c2 = [], True
    for s_, ref in zip(SIG6, D452):
        lt = trapped(s_)
        b, jb = bstar(s_, adm, wI, m1, M1)
        p = fam[jb[lt - 1]]
        rows.append("%g: l = %d, %.4g (%s s_c = %.3g, k = %g, s_R = %g) against %g" %
                    (s_, lt, b[lt - 1], "core" if p[0] != p[1] else "symmetric", p[3], p[4], p[1], ref))
        c2 &= np.isfinite(b[lt - 1])
    ok &= c2
    print("  T2 %s: B* at the trapped harmonic, sigma = %s" % ("ok" if c2 else "FAIL", "; ".join(rows)), flush=True)
    # T3 sup over l of min(E2.7, B*)
    sigs = np.round(np.arange(3.0, 96.0 + 1e-9, 0.01), 2)
    vm = np.array([vpeak(l)[0] for l in ls])
    sup, arg = np.zeros(len(sigs)), np.zeros(len(sigs), int)
    tailB = np.zeros(len(sigs))
    for i, s_ in enumerate(sigs):
        b, _ = bstar(s_, adm, wI, m1, M1)
        e = np.where(s_ * s_ > vm, LAM * s_ / np.maximum(s_ * s_ - vm, 1e-300), np.inf)
        m = np.minimum(b, e)
        m0 = e27(0, s_)
        k = int(np.argmax(m))
        sup[i], arg[i] = max(m[k], m0), (ls[k] if m[k] >= m0 else 0)
        tailB[i] = b[-1]
    c3 = bool(np.all(np.isfinite(sup)) and np.all(tailB <= sup))
    ok &= c3
    at6 = [sup[np.argmin(abs(sigs - s_))] for s_ in SIG6]
    lg = np.log(sigs)
    sel = sigs >= 12
    slope = np.polyfit(lg[sel], np.log(sup[sel]), 1)[0]
    print("  T3 %s: sup over l >= 0 of min(E2.7, B*) at sigma = 3, 6, ..., 96: %s (attained at l = %s); over [3, 96] "
          "in steps of 0.01 its maximum is %.4g at sigma = %g, sigma^(1/2) times it lies in [%.4g, %.4g], log-log slope "
          "over [12, 96] %.3f; l > %d bounded by B*_%d, at most %.3g of the sup" %
          ("ok" if c3 else "FAIL", ", ".join("%.4g" % v for v in at6),
           ", ".join(str(arg[np.argmin(abs(sigs - s_))]) for s_ in SIG6), sup.max(), sigs[np.argmax(sup)],
           (sup * np.sqrt(sigs)).min(), (sup * np.sqrt(sigs)).max(), slope, L, L, (tailB / sup).max()), flush=True)
    # T4 against the measured maxima
    c4 = all(v >= mref for v, mref in zip(at6, D444))
    ok &= c4
    print("  T4 %s: bound / measured maximum (D444) at the six sigma: %s" %
          ("ok" if c4 else "FAIL", ", ".join("%.3g" % (v / mref) for v, mref in zip(at6, D444))), flush=True)
    # T5 controls
    T, p1, p3 = mult(x, 0.98, 2.0, 0.5, 0.05, 1.0)
    w = -T * (a5 * dU + dW) - 0.5 * p3
    core = (x > -30) & (x < 120)
    c5a = w[core].min() < 0
    import e2high5 as H
    pairs = ((5, 3.0), (11, 6.0), (23, 12.0), (47, 24.0))
    res, c5b = [], True
    for l, s_ in pairs:
        nrm = H.cutoff_norm(l, s_)[0]
        b = bstar(s_, adm, wI, m1, M1)[0][l - 1]
        bb = min(b, e27(l, s_))
        res.append("(%d, %g): %.4g >= %.4g" % (l, s_, bb, nrm))
        c5b &= bb >= nrm
    ok &= c5a and c5b
    print("  T5 %s: at l = 5 a core of width 0.05 fails w >= 0 (min w = %.3g); bound against e2high5's norm %s" %
          ("ok" if (c5a and c5b) else "FAIL", w[core].min(), "; ".join(res)), flush=True)
    print("  %s (%.0f s)" % ("all pass" if ok else "FAILED", time.time() - t0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
