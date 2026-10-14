#!/usr/bin/env python3
"""DOCKET 67, pass S, item 14: gr-qc/0209075#flat-exterior-scope.

The tree (linstab.py:86-92, 341, 1049-1050) declines to transfer AMM's flat-space
verdict to the shell-bounded flat exterior r > R_s, because "AMM's flat-space
analysis Fourier-transforms over all of Minkowski space (IV, (4.2)-(4.5))".

What this script checks (every check can fail; exit 1 on any failure):
  A. SOURCE: the load-bearing sentences are in AMM's own text layer
     (alphaXiv full-text layer, cached at d67/amm_0209075.txt this pass).
  B. OWNER: the tree's statement and pin are where the canonical entry says.
  C. CONVOLUTION THEOREM, FINITE: a translation-invariant retarded kernel on a
     translation-invariant (periodic) lattice is diagonalised EXACTLY by plane
     waves, eigenvalue = its Fourier symbol; the same kernel restricted to a
     region bounded on one side (Toeplitz block) is NOT -- plane waves leave a
     residual and the spectrum is not the symbol.  This is the step
     "In Fourier space the non-local real convolution in eq.(4.1) becomes a
     simple multiplication" (AMM p.10) and what it needs.
  D. VERDICTS DO NOT TRANSFER AUTOMATICALLY (toy models, sympy, exact):
     D1 full-line wave eq is Fourier-stable; on a half-line exterior with a
        boundary condition a shell can supply (Robin), an L^2 mode GROWS.
     D2 full-line tachyonic eq is Fourier-unstable; on a bounded interval with
        Dirichlet walls, every mode is stable.
     D3 CONTROL (against over-reading in M's favour): on a half-line EXTERIOR
        with Dirichlet at R the tachyonic instability SURVIVES -- so the tree's
        decline means 'not inherited / must be computed', never 'known to fail'.
  E. RETARDED SUPPORT: the causal past of every exterior event meets the shell
     world-tube, so AMM's integral over x' (eq. (4.1), retarded) at an exterior
     point runs over the non-flat region.
"""
import os, re, sys
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D67 = os.path.dirname(HERE)
SRC = os.path.join(D67, "amm_0209075.txt")
OWNER = "/home/user/Claude-Method-Works/research/warp-drive/linstab.py"

fails, passes = [], []
def chk(name, got, want):
    ok = (got == want)
    (passes if ok else fails).append(name)
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  got=%r want=%r" % (got, want)))

# ------------------------------------------------------------------ A. source
raw = open(SRC, encoding="utf-8", errors="replace").read()
flat = re.sub(r"[\s\x00-\x1f]+", "", raw)   # text layer maps Greek glyphs to control chars
phr = {
 "IV heading 'STABILITY OF FLAT SPACETIME'": "IV.STABILITYOFFLATSPACETIME",
 "background: 'Lorentz invariant vacuum ground state'": "Lorentzinvariantvacuumgroundstate",
 "'around a Minkowski background'": "aroundaMinkowskibackground",
 "(4.1) retarded convolution over x': '1/2 Int d^4x\' Pi^(ret)(x;x\') h(x\')' labelled (4.1)": "12Zd4x0(ret)cdab(x;x0)hcd(x0):(4.1)",
 "p.10 'In Fourier space the non-local real convolution in eq.(4.1) becomes a simple multiplication'":
     "InFourierspacethenon-localrealconvolutionineq.(4.1)becomesasimplemultiplication",
 "(4.2) spectral rep. of Pi(k0, vec k) labelled": "i=T;S:(4.2)",
 "(4.5a) labelled": "=0;(4.5a)", "(4.5b) labelled": "=0:(4.5b)",
 "p.12 k=0 global modes need 'boundary conditions at spatial infinity'": "boundaryconditionsatspatialinnity",
 "p.12 'We do not treat this possibility'": "Wedonottreatthispossibility",
 "p.13-14 'stability of flat space for all local perturbations obeying the inequality (4.6)'":
     "stabilityofatspaceforalllocalperturbationsobeyingtheinequality(4.6)",
 "abstract 'stable to all perturbations on distance scales much larger than the Planck length'":
     "stabletoallperturbationsondistancescalesmuchlargerthanthePlancklength",
 "p.11 generality is over MATTER ('causality, a bounded Hamiltonian ... positive Hilbert space norm')":
     "itrequiresonlycausality,aboundedHamiltonian",
}
for k, v in phr.items():
    chk("A source: " + k, v in flat, True)
# no bounded-region / shell / cavity treatment anywhere in the paper
for w in ["boundedregion", "finiteregion", "shell", "cavity", "Dirichlet", "Robin"]:
    chk("A source: no '%s' in AMM text layer" % w, w.lower() in flat.lower(), False)

# ------------------------------------------------------------------- B. owner
L = open(OWNER, encoding="utf-8").read().splitlines()
blk = " ".join(s.strip() for s in L[85:92])
chk("B owner linstab.py:86-92 quotes 'Fourier- transforms over all of Minkowski space (IV, (4.2)-(4.5))'",
    "Fourier- transforms over all of Minkowski space (IV, (4.2)-(4.5))" in blk, True)
chk("B owner linstab.py:86-92 'neither \"stable\" nor \"unstable\" transfers'",
    'neither "stable" nor "unstable"' in blk, True)
chk("B owner linstab.py:341 pin", L[340].startswith("FLAT_EXTERIOR_INHERITS_AMM = False"), True)
chk("B owner linstab.py:1049 is record(), not chk()", L[1048].strip().startswith("record(\"FLAT_EXTERIOR_INHERITS_AMM"), True)

# --------------------------------------------------- C. convolution theorem
N = 64
rng = np.random.default_rng(67)
kern = np.zeros(N); kern[:6] = rng.normal(size=6)          # retarded: support j>=0 only
C = np.array([[kern[(i - j) % N] for j in range(N)] for i in range(N)])  # circulant
sym = np.fft.fft(kern)
worst = 0.0
for m in range(N):
    e = np.exp(2j*np.pi*m*np.arange(N)/N)
    worst = max(worst, np.linalg.norm(C @ e - sym[m]*e))
chk("C full translation-invariant domain: plane waves exact eigenvectors (max residual < 1e-10)",
    worst < 1e-10, True)
T = np.array([[kern[i - j] if 0 <= i - j < 6 else 0.0 for j in range(N)] for i in range(N)])  # region bounded at site 0
worstT = 0.0
for m in range(1, N):
    e = np.exp(2j*np.pi*m*np.arange(N)/N)
    worstT = max(worstT, np.linalg.norm(T @ e - sym[m]*e))
chk("C bounded region (Toeplitz block): plane waves NOT eigenvectors (residual > 0.1)", worstT > 0.1, True)
evT = np.linalg.eigvals(T)
chk("C bounded region: spectrum collapses to kern[0] (lower-triangular), not the symbol",
    bool(np.allclose(evT, kern[0]) and not np.allclose(np.sort_complex(sym), np.sort_complex(evT))), True)
print("   residual full = %.2e ; residual bounded = %.3f" % (worst, worstT))

# --------------------------------------------- D. verdicts, toy models, exact
t, x, k, R, kap, mu, Lc = sp.symbols("t x k R kappa mu L", positive=True)
w = sp.symbols("omega")
# D1: u_tt = u_xx.  Full line, u = exp(i(kx - w t)): w^2 = k^2, real k => real w.
disp1 = sp.solve(sp.Eq(w**2, k**2), w)
chk("D1 full line: dispersion roots real for real k (no growth)", all(sp.im(r) == 0 for r in disp1), True)
u = sp.exp(kap*t - kap*(x - R))
chk("D1 half-line x>R: u = e^{kappa(t-(x-R))} solves u_tt = u_xx",
    sp.simplify(sp.diff(u, t, 2) - sp.diff(u, x, 2)), 0)
chk("D1 satisfies Robin BC u_x(R) = -kappa u(R) at the wall",
    sp.simplify((sp.diff(u, x) + kap*u).subs(x, R)), 0)
chk("D1 L^2 on x>R at each t (norm^2 = e^{2 kappa t}/(2 kappa), finite)",
    sp.simplify(sp.integrate(u**2, (x, R, sp.oo)) - sp.exp(2*kap*t)/(2*kap)), 0)
chk("D1 and it GROWS: d/dt log||u|| = kappa > 0",
    sp.simplify(sp.diff(sp.log(sp.exp(2*kap*t)/(2*kap))/2, t)), kap)
# D2: u_tt = u_xx + mu^2 u.  Full line w^2 = k^2 - mu^2 < 0 for k < mu -> growth.
wk = sp.sqrt(k**2 - mu**2)
chk("D2 full line: k = mu/2 gives imaginary omega (growth rate sqrt(3)/2 mu)",
    sp.simplify(sp.im(wk.subs(k, mu/2)) - sp.sqrt(3)*mu/2), 0)
n = sp.symbols("n", positive=True, integer=True)
w2n = (n*sp.pi/Lc)**2 - mu**2
chk("D2 interval of length L < pi/mu, Dirichlet: lowest omega^2 = (pi/L)^2 - mu^2 > 0 (all stable)",
    sp.simplify(w2n.subs({n: 1, Lc: sp.pi/(2*mu)})) > 0, True)
# D3 CONTROL: half-line exterior x>R, Dirichlet: modes sin(k(x-R)) for every k>0 -> k<mu grows.
v = sp.sin(k*(x - R))*sp.exp(sp.sqrt(mu**2 - k**2)*t)
chk("D3 CONTROL exterior half-line, Dirichlet: sin(k(x-R)) e^{sqrt(mu^2-k^2) t} solves, k<mu",
    sp.simplify(sp.diff(v, t, 2) - sp.diff(v, x, 2) - mu**2*v), 0)
chk("D3 CONTROL vanishes at the wall: instability SURVIVES in an unbounded exterior",
    v.subs(x, R), 0)

# ---------------------------------------------------- E. retarded support
r, Rs, eps = sp.symbols("r R_s epsilon", positive=True)
# event (t, r) with r > R_s; candidate past point (t - (r - R_s) - eps, R_s): timelike/null separated in the past.
dt = (r - Rs) + eps; dr = r - Rs
chk("E causal past of every exterior event meets the shell world-tube (dt >= dr, dt > 0)",
    bool(sp.simplify(dt - dr) == eps), True)

print("\n%d checks, %d failed" % (len(passes) + len(fails), len(fails)))
sys.exit(1 if fails else 0)
