"""P3 double-null evolution continued past a singularity by excision (item 464).  Points j < jL are cut out once |K|
passes Kcut there; at jL the stencils are one-sided (no boundary condition: valid only while the cut moves faster than
light, dchi/dtau > 1, which is checked and reported); m is integrated from jL with m(jL) from its definition."""
import sys, pickle, warnings, numpy as np, sympy as sp, dnE, dnrun
warnings.filterwarnings("ignore")
KR = dnrun.KR


class DNX(dnE.DNE):
    jL = 0

    def jets(self, Y):
        J = super().jets(Y)
        j, h = self.jL, self.h
        if j > 0:
            for k, nm in enumerate(dnE.F):
                f, ft = Y[k], Y[k + 3]
                J[nm + "_x"][j] = (-3 * f[j] + 4 * f[j + 1] - f[j + 2]) / (2 * h)
                J[nm + "_xx"][j] = (2 * f[j] - 5 * f[j + 1] + 4 * f[j + 2] - f[j + 3]) / h**2
                J[nm + "_tx"][j] = (-3 * ft[j] + 4 * ft[j + 1] - ft[j + 2]) / (2 * h)
        return J

    def mass(self, J):
        if self.jL == 0:
            return super().mass(J)
        j, chi, h = self.jL, self.chi, self.h
        JJ = dict(J, chi=chi, m=0 * chi)
        mx = dnE.MX(*[JJ[n] for n in dnE.names])
        md = dnE.MDEF(*[JJ[n] for n in dnE.names])
        inc = (mx[j:-1] + mx[j + 1:]) * h / 2
        m = np.full_like(chi, np.nan)
        m[j:] = md[j] + np.concatenate([[0.0], np.cumsum(inc)])
        return m, m / J["r"]**3

    def rhs(self, Y):
        out = super().rhs(Y)
        if self.jL > 0:
            for o in out:
                o[:self.jL] = 0.0
        return out

    def step(self, Y, dt):
        Yn = super().step(Y, dt)
        if self.jL > 0:
            for yn, y in zip(Yn, Y):
                yn[:self.jL] = y[:self.jL]
        return Yn


def run(fn, s0, N, kap, Ns, tmax, Kcut=1e8, cfl=0.25, tag=None, nout=60, quiet=False, cls=None):
    Y, chk = dnrun.initial(fn, s0, N, kap, Ns)
    ev = (cls or DNX)(N, kap)
    dt = cfl * ev.h
    nst = int(round(tmax / dt))
    every = max(1, nst // nout)
    hist, cut = [], []
    for n in range(nst + 1):
        K, m = dnrun.physics(ev, Y)
        aK = np.abs(K)
        aK[:ev.jL] = np.inf
        if ev.jL == 0:
            aK[0] = aK[1]
        bad = np.where(~(aK[ev.jL:] < Kcut))[0]
        if len(bad) and bad[0] <= 2:
            jn = ev.jL
            while jn < N and not (aK[jn] < Kcut):
                jn += 1
            jn = min(jn + 2, N)
            if jn != ev.jL:
                cut.append((n * dt, ev.chi[jn]))
                ev.jL = jn
        if ev.jL > N - 4:
            if not quiet:
                print("tau %.4f: the cut reaches the plane" % (n * dt))
            break
        A, S, r = Y[1], Y[0], Y[2]
        R = np.exp(-A / 2) * r
        dRpl = R[-1] * (Y[5][-1] / r[-1] - Y[4][-1] / 2) * np.exp(-(S[-1] - A[-1] / 2))   # dR/d(proper time)
        rec = dict(tau=n * dt, jL=ev.jL, chiL=ev.chi[ev.jL], Npl=np.exp(2 * A[-1]), Rpl=R[-1], Kpl=K[-1], dRpl=dRpl,
                   Nmin=np.exp(2 * A[ev.jL:]).min(), Kin=np.nanmax(aK[ev.jL:]), Rmin=np.nanmin(R[max(ev.jL, 1):]))
        hist.append(rec)
        if (n % every == 0 or n == nst) and not quiet:
            print("tau %.4f | cut chi %.3f | plane N %.4e R %.4f K %.3e | Nmin %.3e  max|K| (kept) %.2e  Rmin %.4f" % (
                rec["tau"], rec["chiL"], rec["Npl"], rec["Rpl"], rec["Kpl"], rec["Nmin"], rec["Kin"], rec["Rmin"]), flush=True)
        if not np.all(np.isfinite(Y[0][ev.jL:])) or rec["Npl"] < 1e-10 or abs(rec["Kpl"]) > Kcut:
            if not quiet:
                print("stop at tau %.4f: plane N %.3e K %.3e" % (rec["tau"], rec["Npl"], rec["Kpl"]))
            break
        if n < nst:
            Y = ev.step(Y, dt)
    if tag:
        pickle.dump(dict(hist=hist, cut=cut, args=(fn, s0, N, kap, Ns, tmax, Kcut, cfl), Y=Y), open(tag + ".pkl", "wb"))
    return hist, cut


if __name__ == "__main__":
    fn, s0, kap, Ns, N, tmax = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
    Kcut = float(sys.argv[7]) if len(sys.argv) > 7 else 1e8
    hist, cut = run(fn, s0, N, kap, Ns, tmax, Kcut=Kcut, tag=sys.argv[8] if len(sys.argv) > 8 else None)
    if len(cut) > 1:
        c = np.array(cut)
        print("cut curve (tau, chi):", " ".join("(%.3f, %.3f)" % tuple(v) for v in c[::max(1, len(c) // 12)]))
        sl = np.diff(c[:, 1]) / np.maximum(np.diff(c[:, 0]), 1e-12)
        print("cut speed dchi/dtau: min %.2f median %.2f (must exceed 1)" % (sl[sl > 0].min() if (sl > 0).any() else 0, np.median(sl)))
