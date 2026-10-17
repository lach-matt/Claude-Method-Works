"""run P3's double-null evolution from the static slice s0 (item 464)"""
import sys, pickle, warnings, numpy as np, sympy as sp, dnE, dninit
warnings.filterwarnings("ignore")
KR = sp.lambdify(dnE.SY, dnE.D["K"], "numpy")


def initial(fn, s0, N, kap, Ns, bt=2.0, Nx=20, smin=-0.30):
    U = np.load(fn)
    chi, d, chk = dninit.conformal(U, s0, N, kap, Ns=Ns, Nx=Nx, btv=bt, smin=smin)
    sig, A, psi = d["sig"], d["A"], d["psi"]
    S = sig + A / 2
    R = chi * np.exp(sig + psi)
    r = np.exp(A / 2) * R
    St = d["sig_t"] + d["A_t"] / 2
    rt = r * (d["A_t"] / 2 + d["sig_t"] + d["psi_t"])
    return [S, A, r, St, d["A_t"], rt], chk


def physics(ev, Y):
    J = ev.jets(Y)
    m, mr3 = ev.mass(J)
    J["chi"], J["m"] = ev.chi, m
    K = np.asarray(KR(*[J[n] for n in dnE.names])) * np.ones(ev.N + 1)
    return K, m


def run(fn, s0, N, kap, Ns, tmax, cfl=0.25, nout=40, quiet=False, tag=None):
    Y, chk = initial(fn, s0, N, kap, Ns)
    ev = dnE.DNE(N, kap)
    dt = cfl * ev.h
    nst = int(round(tmax / dt))
    every = max(1, nst // nout)
    hist, snaps = [], []
    for n in range(nst + 1):
        if n % every == 0 or n == nst:
            dg = ev.diag(Y)
            K, m = physics(ev, Y)
            q = int(0.25 * N)
            dg.update(tau=n * dt, Kpl=K[-1], Kmax=np.nanmax(np.abs(K[1:])), Kax1=K[1],
                      Cu=np.abs(dnE.CU(*[dict(ev.jets(Y), chi=ev.chi, m=m)[k] for k in dnE.names])[q:] /
                                np.exp(2 * Y[0][q:] - Y[1][q:])).max())
            hist.append(dg); snaps.append([y.copy() for y in Y])
            if not quiet:
                print("tau %.4f | plane N %.3e R %.4f K %.4e | axis N %.3e K(h) %.3e | Nmin %.3e Kmax %.3e | "
                      "Cuu %.1e dm %.1e ef %.1e" % (dg["tau"], dg["Npl"], dg["Rpl"], dg["Kpl"], dg["Nax"], dg["Kax1"],
                                                     dg["Nmin"], dg["Kmax"], dg["Cu"], dg["dm"], dg["ef"]), flush=True)
            if not (np.isfinite(dg["Kmax"]) and np.all(np.isfinite(Y[0]))) or dg["Kmax"] > 1e9 or dg["Nmin"] < 1e-12:
                break
        if n < nst:
            Y = ev.step(Y, dt)
    if tag:
        pickle.dump(dict(hist=hist, snaps=snaps, chi=ev.chi, chk=chk, args=(fn, s0, N, kap, Ns, tmax, cfl)),
                    open(tag + ".pkl", "wb"))
    return Y, hist, chk


if __name__ == "__main__":
    fn, s0, kap, Ns, N, tmax = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
    run(fn, s0, N, kap, Ns, tmax, tag=sys.argv[7] if len(sys.argv) > 7 else None)
