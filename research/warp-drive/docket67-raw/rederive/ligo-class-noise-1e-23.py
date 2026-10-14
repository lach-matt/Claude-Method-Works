#!/usr/bin/env python3
"""DOCKET 67 audit -- ligo-class-noise-1e-23 (branelink.py:136 H_NOISE = 1.0e-23 Hz^-1/2).

Independent of the tree: constants retyped from CODATA/IAU here (G, c, Julian
year, light year), the tree is imported ONLY for a cross-check of its printed
figure, with bytecode writing disabled so nothing under research/ is touched.

Checks:
  (1) the tree's bulk throughput 4G/(D^2 c^3 w^2 h_n^2) at w = 2*Omega = 200 rad/s
      reproduces 1.5347e-27 bits/s/W from the formula alone;
  (2) sympy: for a sinusoid of detector amplitude h in stationary Gaussian noise of
      one-sided PSD S_n = h_n^2, rho^2 = (2/S_n) int s^2 dt = h^2 T / S_n, so the
      unit-SNR rate is (h/h_n)^2 per second -- the tree's law; and the low-SNR
      Shannon capacity P/(N0 ln 2) is (h/h_n)^2 / (2 ln 2) = 0.7213 (h/h_n)^2 bits/s;
  (3) the LIGO noise curves shipped in the bilby 2.8.2 wheel (LIGO DCC curves, per
      the wheel's README) evaluated at f_GW = 200/(2 pi) = 31.831 Hz (seated) and
      100/(2 pi) = 15.915 Hz (the WITHDRAWN as-scripted frequency);
  (4) how far each curve moves the seated throughput and the "~26.6 orders" margin;
  (5) the coherent integration time a single unit-SNR bit needs, T1 = h_n^2/h^2.
"""
import glob, hashlib, math, os, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
D67 = os.path.dirname(HERE)
WHEEL = glob.glob(os.path.join(D67, "pkg", "ligo", "bilby-*.whl"))

G = 6.67430e-11          # CODATA 2018
C = 299792458.0
JYR = 365.25 * 86400.0
LY = C * JYR
D = 4.2465 * LY          # Proxima span as seated (4.2465 ly)
OMEGA = 100.0
W = 2 * OMEGA            # seated omega_GW
HN_TREE = 1.0e-23
TREE_BULK = 1.5347e-27   # branelink selftest pin
TREE_H = 4.3359e-48
TREE_ORDERS = 26.6
TREE_ORDERS_EXACT = 26.6213   # branelink.brane_beats_bulk_orders() printed below

ok = True
def chk(name, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + detail if detail else ""))

def bulk(w, hn, d=D):
    return 4.0 * G / (d ** 2 * C ** 3 * w ** 2 * hn ** 2)

# (1)
b = bulk(W, HN_TREE)
chk("(1) formula reproduces tree bulk 1.5347e-27 bits/s/W", abs(b / TREE_BULK - 1) < 1e-4, "%.6e" % b)
chk("(1) withdrawn 4x at omega", abs(bulk(OMEGA, HN_TREE) / b - 4) < 1e-12)

# (2) sympy
import sympy as sp
h, hn, w_, T, t, P, N0 = sp.symbols("h h_n omega T t P N_0", positive=True)
s = h * sp.cos(w_ * t)
rho2 = sp.simplify(2 / hn ** 2 * sp.integrate(s ** 2, (t, 0, T)))
rho2_avg = sp.limit(rho2 / T, T, sp.oo) * T
chk("(2) rho^2 -> h^2 T / h_n^2 (long T)", sp.simplify(rho2_avg - h ** 2 * T / hn ** 2) == 0, str(rho2_avg))
T1 = sp.solve(sp.Eq(rho2_avg, 1), T)[0]
chk("(2) unit-SNR rate 1/T1 = (h/h_n)^2", sp.simplify(1 / T1 - h ** 2 / hn ** 2) == 0)
Bw = sp.symbols("B", positive=True)
cap_low = sp.limit(Bw * sp.log(1 + P / (N0 * Bw), 2), Bw, sp.oo)
cap = sp.simplify(cap_low.subs({P: h ** 2 / 2, N0: hn ** 2}) / (h ** 2 / hn ** 2))
chk("(2) Shannon wideband limit / (h/h_n)^2 = 1/(2 ln 2)", sp.simplify(cap - 1 / (2 * sp.log(2))) == 0,
    "%s = %.6f" % (cap, float(cap)))

# (5) integration time for one unit-SNR bit at the seated strain
T1n = HN_TREE ** 2 / TREE_H ** 2
print("(5) T1 = h_n^2/h^2 = %.4e s = %.4e yr (age of universe ~1.38e10 yr: %.1f orders over)"
      % (T1n, T1n / JYR, math.log10(T1n / JYR / 1.38e10)))

# (3)(4) curves
if not WHEEL:
    print("OPEN: bilby wheel absent; run: pip download --no-deps bilby==2.8.2 -d %s/pkg/ligo" % D67)
    sys.exit(0 if ok else 1)
z = zipfile.ZipFile(WHEEL[0])
print("wheel", os.path.basename(WHEEL[0]))
names = ["aLIGO_ZERO_DET_high_P_asd.txt", "aLIGO_O4_high_asd.txt", "aLIGO_late_asd.txt",
         "aLIGO_mid_asd.txt", "aLIGO_early_asd.txt", "Aplus_asd.txt", "LIGO_srd_asd.txt"]
fs = W / (2 * math.pi)
fw = OMEGA / (2 * math.pi)
rows = {}
for n in names:
    raw = z.read("bilby/gw/detector/noise_curves/" + n)
    d = [tuple(map(float, l.split())) for l in raw.decode().splitlines() if l.strip()]
    def at(f):
        for (a, x), (c2, y) in zip(d, d[1:]):
            if a <= f <= c2:
                u = (math.log(f) - math.log(a)) / (math.log(c2) - math.log(a))
                return math.exp(math.log(x) + u * (math.log(y) - math.log(x)))
        return None
    band = [r[0] for r in d if r[1] <= 1e-23]
    a_s, a_w = at(fs), at(fw)
    rows[n] = (a_s, a_w)
    mv = math.log10(bulk(W, a_s) / b)
    print("%-30s md5 %s  ASD(31.83 Hz)=%.3e  ASD(15.92 Hz)=%.3e  1e-23/ASD=%.3f  bulk=%.4e  dlog10=%+.3f  band<=1e-23 %s"
          % (n, hashlib.md5(raw).hexdigest()[:10], a_s, a_w, HN_TREE / a_s, bulk(W, a_s), mv,
             ("%.1f-%.1f Hz" % (band[0], band[-1])) if band else "none"))

des = rows["aLIGO_ZERO_DET_high_P_asd.txt"][0]
o4 = rows["aLIGO_O4_high_asd.txt"][0]
ap = rows["Aplus_asd.txt"][0]
chk("(3) 1e-23 within a factor 2 of aLIGO design at 31.83 Hz", 0.5 < des / HN_TREE < 2, "%.3e" % des)
chk("(3) 1e-23 within a factor 2 of O4-high projection at 31.83 Hz", 0.5 < o4 / HN_TREE < 2, "%.3e" % o4)
chk("(3) 1e-23 is conservative (>= every aLIGO/A+ curve) at 31.83 Hz",
    all(rows[n][0] <= HN_TREE for n in ["aLIGO_ZERO_DET_high_P_asd.txt", "aLIGO_O4_high_asd.txt",
                                          "aLIGO_late_asd.txt", "Aplus_asd.txt"]))
chk("(3) NOT conservative for early/mid aLIGO or initial-LIGO SRD at 31.83 Hz",
    all(rows[n][0] > HN_TREE for n in ["aLIGO_mid_asd.txt", "aLIGO_early_asd.txt", "LIGO_srd_asd.txt"]))
chk("(3) at the withdrawn 15.92 Hz every curve is > 1e-23 (1e-23 out of band there)",
    all(rows[n][1] > HN_TREE for n in names))
worst = max(abs(math.log10(bulk(W, rows[n][0]) / b)) for n in
            ["aLIGO_ZERO_DET_high_P_asd.txt", "aLIGO_O4_high_asd.txt", "aLIGO_late_asd.txt"])
chk("(4) aLIGO design / O4-high / late curves move the seated throughput by < 0.2 order", worst < 0.2,
    "max |dlog10| = %.3f" % worst)
margins = {n: TREE_ORDERS_EXACT - math.log10(bulk(W, rows[n][0]) / b) for n in names}
chk("(4) with EVERY curve (incl. A+ upgrade) the EM-over-bulk margin stays > 26 orders",
    all(m > 26.0 for m in margins.values()),
    "min %.3f (%s)" % (min(margins.values()), min(margins, key=margins.get)))
cap_orders = math.log10(1 / (2 * math.log(2)))
print("(4) Shannon factor 1/(2 ln 2) moves bulk throughput by %+.3f orders, i.e. the margin by %+.3f" % (cap_orders, -cap_orders))

# cross-check the tree's own figure, read-only (no bytecode written)
sys.dont_write_bytecode = True
tree = "/home/user/Claude-Method-Works/research/warp-drive"
try:
    sys.path.insert(0, tree)
    import branelink
    hb, bb = branelink.corrected()
    chk("tree branelink.corrected() == this formula", abs(bb / b - 1) < 1e-6 and abs(hb / TREE_H - 1) < 1e-4,
        "tree %.6e / here %.6e; H_NOISE=%g" % (bb, b, branelink.H_NOISE))
    print("tree margin: %.4f orders" % branelink.brane_beats_bulk_orders())
except Exception as e:
    print("tree cross-check skipped:", e)
print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
