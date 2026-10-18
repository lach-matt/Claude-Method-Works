#!/usr/bin/env python3
"""face2_open.py -- item 489 (F1 of the 488 verification): position 2's face over its open period, on 390.

M, 390: "it closes when there is nothing contained within the corridor" (M-CLOSES-WHEN-EMPTY); 427: "Destination with
any sigma is supposed to be reachable" -- the junction model of position 2's face (c_junction J1, its 33.6 clocks)
withdrawn as the board's.  Six rows still rested on J1's period (O2's S6, O3s, B4ds D5/D15, E2us, E2xs, CLOSEs) and the
large end's on J2's 4 clocks (O3, M1P2x, E2u, E2x, CLOSE).  Here the period is computed on 390 and the face is held
against established physics over it.  Labels: computed (exact unless marked), deduced, READ, estimate.

  W0 (read) M's words, verbatim in the rulings file: 390, 427.
  W1 (computed, exact) The write at the face's balance (passage_est Q4, corrected at 489): the README's bits come in as
     the plane's own radiation at T_H, entropy (4/3) E/T, absorbed at the plane's share of the Hawking power.  With the
     first law (5D: N ln2 k T_H = (2/3) E) the inflow is E/2 and tau_w = E_in / P_brane = (1 + b) x the life, b the bulk
     gravitons' share (0.61 scalar dof, hold_small L5): 1.0062 x 8.57e14 = 8.63e14 face clocks at the example README.
     At the large end (4D: N ln2 k T_H = E/2) the inflow is (3/8) E and tau_w = 3 N ln2 / (32 pi alpha) clocks of GM/c^3.
     Thermal radiation at T_H is the most entropy per energy that the face's own area passes at its own power, so
     tau_w is the write's least time with the face at its size (162-163).
  [Item 491: W2, W5 and W6 rest on a premise against 432 (2) -- the README held whole through the write and released
  whole at its end -- and are withdrawn: position 2's face is open only for the release, at most 2 r_h/c, and holds
  (face2_release.py).  W1 (the write), W3's rates and W4's t_q stand and are used there.]
  W2 (computed, exact on 390 and junction_own G10) Position 2's face is open exactly while the README is within it:
     from the first part's emergence to the last part's, T_open = tau_w -- 8.63e14 clocks (3.2e-14 s) at the example,
     1.5e67 clocks of GM/c^3 (2.2e56 s) at the Earth cap.  J1's 33.6 clocks and J2's 4 are not its period.
  W3 (READ, computed) A perturbation from position 2.  Barcelo, Carballo-Rubio and Garay, JHEP 01 (2016) 157
     (arXiv:1511.00633, READ): a white-hole face open long is unstable to imperceptibly small perturbations; on the
     criterion the record used (c_junction J2), an inflow epsilon crossing near the face at age t forms a trapped surface
     once epsilon e^(kappa t) reaches 0.28 E -- 63.0 clocks for 1 eV at the example.  The expected number of perturbing
     particles over T_open, onto the capture disc pi (2 r_h)^2: blackbody photons 2.1e-36 (3 K) to 7.7e-8 (1e10 K), air
     6.4e-25, a metal's electrons 1.3e-15, inside a nucleus 0.43; at the Earth cap's 8.9 mm face over 2.2e56 s, every
     environment delivers one (above 1e60).
  W4 (computed; the stress exact in the s-wave model, the crossing in Dray-'t Hooft-Redmount form) Position 2's vacuum.
     With nothing coming in from position 2 (its past null infinity in vacuum, as (O) has it), the ingoing stress at the
     face is the Boulware value, T_vv = -M(2r - 3M)/(48 pi r^4) in the s-wave model, -kappa^2/(48 pi) at the face: the
     face's own negative flux, -P per unit time.  Crossing it, the emerging README (Delta, outgoing) and the ingoing
     packet (epsilon < 0) obey f(mu_past) f(mu_fut) = f(mu_in) f(mu_out) at r_h + delta (exact); to leading order in
     delta, mu_fut = -(Delta |epsilon|)/(2 delta r_h) in 5D: a negative mass between them, growing as e^(kappa t) with
     the face's age.  It reaches the face's own mass at t_q = ln(2 E/|epsilon|) clocks, |epsilon| = P r_h/c one clock's
     flux: 35.8 clocks at the example (31.2 at one percent); 155 e-folds (620 clocks of GM/c^3) at the Earth cap.  With epsilon > 0 the same
     algebra gives f_fut < 0 (Eardley's black hole).  So the face does not stay a semiclassical white hole past t_q.
  W5 (computed) The one state that holds it: the time reverse of our face's state (b_bounce Q1's isometry carried to the
     quantum state), T_vv' = T_uu(Unruh) = kappa^2/(48 pi) - M(2r - 3M)/(48 pi r^4), zero at the face as f^2 (regular).
     It needs position 2 to send in kappa^2/(48 pi) at infinity -- the face's own power at T_H (3.3e16 K at the example),
     P T_open = 0.503 E over the open period, correlated as our face's Hawking radiation.  Nothing in the theorem
     supplies it: the board's model of position 2 has a vacuum there.
  W6 (deduced) So the face's holding through its open period is not given by established physics: T_open / t_q =
     2.4e13 at the example, 2.4e64 at the Earth cap.  Every row that needs position 2's face to hold until the README
     has emerged rests on FACE2s / FACE2, OPEN: the release at its closing (E2us, E2xs, E2u, E2x, E3, R5), the bits
     rebuilt at position 2 (ARRIVALs, ARRIVAL), the one object one way (O1a) and the complete bulk (B3s, B3).  The
     record's figure passed for a reason now seen: J1's withdrawn 33.6 clocks lies below t_q (control, mutant).

What this does not claim: the quantum state at position 2's face beyond the s-wave model, or that no other mechanism
holds it -- only that none in the theorem does, and that the vacuum the board's position 2 carries does not.

python3 face2_open.py [--selftest | --mutants]
"""
import os, sys, math, re, io, contextlib, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((390, "it closes when there is nothing contained within the corridor"),
         (427, "Destination with any"))
EV = 1.602176634e-19
KB = 1.380649e-23
N_STAR = 1.3651e66                                                   # the Earth cap (item 372)
J1_OPEN = 33.6                                                       # c_junction J1, withdrawn at 427


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


# ------------------------------------------------------------------ W1, W2
def write_and_open():
    SS = _load("source_spec.py", "f2_ss"); HS = _load("hold_small.py", "f2_hs")
    k = SS.consts(); d = SS.energy_check(k)
    dof = sum(n_ for n_, _ in HS.GREY_SPIN.values())
    gam = sum(n_ * g for n_, g in HS.GREY_SPIN.values()) / dof
    b = HS.GRAV_BULK_DOF / (gam * dof)
    N, E, rh, c = d["N"], d["E"], d["rh"], k["c"]
    clock = rh / c
    life = 45 * N * k["ln2"] / (dof * gam * (1 + b))                 # hold_small L5, face clocks, every channel
    P_tot = E / (2 * life * clock)
    P_br = P_tot / (1 + b)
    kTH = k["hbar"] * c / (2 * math.pi * rh)
    E_in = 0.75 * N * k["ln2"] * kTH                                 # (4/3) E_in / T_H = N ln2: the plane's radiation
    tau_w = E_in / P_br / clock
    # large end, at the Earth cap (passage_est Q4's large-end form; close_large's alpha)
    Z = 108.75
    alpha = 27 * Z / (491520 * math.pi)
    lP = k["lP"]
    r0 = lP * math.sqrt(N_STAR * k["ln2"] / math.pi)
    M_ = r0 * c ** 2 / (2 * k["G"])
    gm = k["G"] * M_ / c ** 3                                        # one clock of GM/c^3
    tau_L = 3 * N_STAR * k["ln2"] / (32 * math.pi * alpha)           # clocks of GM/c^3
    P_L = alpha * k["hbar"] * c ** 6 / (k["G"] ** 2 * M_ ** 2)
    T_open = J1_OPEN if "short_open" in MUT else tau_w
    return dict(k=k, N=N, E=E, rh=rh, clock=clock, b=b, gam=gam, dof=dof, life=life, P_tot=P_tot, P_br=P_br,
                kTH=kTH, E_in=E_in, tau_w=tau_w, T_open=T_open, r0=r0, M=M_, gm=gm, tau_L=tau_L, P_L=P_L,
                T_open_L=J1_OPEN if "short_open" in MUT else tau_L, E_L=M_ * c ** 2, alpha=alpha)


def smarr():
    """W1's first law at both ends: N ln2 k T_H against E (5D 2/3, 4D 1/2), so E_in = E/2 and (3/8) E"""
    r, c, G5, G, hb = sp.symbols("r c G5 G hbar", positive=True)
    E5 = 3 * sp.pi * c ** 4 * r ** 2 / (8 * G5); S5 = 2 * sp.pi ** 2 * r ** 3 * c ** 3 / (4 * G5 * hb)
    T5 = hb * c / (2 * sp.pi * r)
    E4 = r * c ** 4 / (2 * G); S4 = 4 * sp.pi * r ** 2 * c ** 3 / (4 * G * hb); T4 = hb * c / (4 * sp.pi * r)
    return dict(ts5=sp.simplify(S5 * T5 / E5), ts4=sp.simplify(S4 * T4 / E4),
                ein5=sp.simplify(sp.Rational(3, 4) * S5 * T5 / E5), ein4=sp.simplify(sp.Rational(3, 4) * S4 * T4 / E4))


# ------------------------------------------------------------------ W3
def perturbations(w):
    k, rh, E = w["k"], w["rh"], w["E"]
    t_eV = math.log(0.28 * E / EV)                                   # clocks, kappa = c/r_h
    disc = math.pi * (2 * rh) ** 2                                   # capture disc, b_c = 2 r_h (5D, on the plane)
    T = w["T_open"] * w["clock"]
    def bb(TK):                                                      # blackbody photon number flux n c / 4
        n = 2 * 1.2020569031595942 / math.pi ** 2 * (KB * TK / (k["hbar"] * k["c"])) ** 3
        return n * k["c"] / 4
    env = {"blackbody 3 K": bb(3.0), "blackbody 300 K": bb(300.0), "blackbody 1e10 K": bb(1e10),
           "air (2.5e25 /m^3 at 500 m/s)": 2.5e25 * 500.0, "a metal's electrons (2.5e30 /m^3 at 1e7 m/s)": 2.5e30 * 1e7,
           "inside a nucleus (1.4e44 /m^3 at 0.2 c)": 1.4e44 * 0.2 * k["c"]}
    counts = {e: f * disc * T for e, f in env.items()}
    disc_L = math.pi * (1.5 * math.sqrt(3) * w["r0"]) ** 2           # 4D capture, b_c = 3 sqrt(3) M
    T_L = w["T_open_L"] * w["gm"]
    counts_L = {e: f * disc_L * T_L for e, f in env.items()}
    return dict(t_eV=t_eV, counts=counts, counts_L=counts_L, T_s=T, T_L_s=T_L)


# ------------------------------------------------------------------ W4, W5
def stress():
    """the s-wave (Polyakov) stress: Boulware ingoing (position 2's vacuum) and the time-reversed Unruh state"""
    r, M = sp.symbols("r M", positive=True)
    f = 1 - 2 * M / r
    fp, fpp = sp.diff(f, r), sp.diff(f, r, 2)
    Tvv_B = sp.factor(sp.simplify(-(fp ** 2 / 16 - f * fpp / 8) / (12 * sp.pi)))
    kap = 1 / (4 * M)
    Tuu_U = sp.simplify(Tvv_B + kap ** 2 / (48 * sp.pi))             # Unruh's outgoing; reversed, position 2's ingoing
    at_face = sp.simplify(Tvv_B.subs(r, 2 * M))
    reg = sp.simplify(sp.series(Tuu_U, r, 2 * M, 3).removeO() / f ** 2)
    regular = sp.limit(Tuu_U / f ** 2, r, 2 * M).is_finite and sp.simplify(Tuu_U.subs(r, 2 * M)) == 0
    return dict(Tvv_B=Tvv_B, at_face=at_face, face_is_kappa=sp.simplify(at_face + kap ** 2 / (48 * sp.pi)) == 0,
                Tuu_U=Tuu_U, regular=regular, infinity=sp.limit(Tuu_U, r, sp.oo))


def crossing():
    """DTR at r_h + delta in 5D (f = 1 - mu/r^2): ingoing epsilon meets the outgoing README Delta"""
    mu, D, eps, dl, rh = sp.symbols("mu Delta epsilon delta r_h", positive=True)
    R = rh + dl
    f = lambda m: 1 - m / R ** 2
    s = 1 if "positive_vac" in MUT else -1                           # the vacuum's packet is negative
    e = s * eps
    # past (between, before): mu; inside both: mu - Delta; outside both: mu + e; future (between, after): mu_fut
    f_fut = sp.simplify(f(mu - D) * f(mu + e) / f(mu))
    mu_fut = sp.simplify(R ** 2 * (1 - f_fut))
    lead = sp.limit(sp.simplify((mu_fut * dl).subs(mu, rh ** 2)), dl, 0)   # mu_fut ~ lead / delta
    return dict(lead=sp.simplify(lead), sign=s, f_fut=f_fut, trapped=s > 0)


def t_quantum(w):
    """the age at which the negative mass between reaches the face's own (W4): t_q = ln(2E/|eps|), |eps| = P r_h/c"""
    E_over_eps = w["E"] / (w["P_tot"] * w["clock"])
    t_q = math.log(2 * E_over_eps)
    t_q1 = math.log(2 * E_over_eps / 100)
    # large end: one e-fold per 4 clocks of GM/c^3; |eps| = P_L x 4 GM/c^3 per e-fold
    E_over_eps_L = w["E_L"] / (w["P_L"] * 4 * w["gm"])
    t_qL = math.log(2 * E_over_eps_L)                                 # e-folds
    return dict(t_q=t_q, t_q1=t_q1, t_qL_efolds=t_qL, t_qL_clocks=4 * t_qL)


def reflected(w):
    TH = w["kTH"] / KB
    need = w["P_tot"] * w["T_open"] * w["clock"] / w["E"]
    return dict(TH=TH, need=need)


def compute():
    w = write_and_open()
    return dict(words=words(), w=w, sm=smarr(), pt=perturbations(w), st=stress(), cr=crossing(), tq=t_quantum(w),
                rf=reflected(w))


def checks(o):
    w, sm, pt, st, cr, tq, rf = o["w"], o["sm"], o["pt"], o["st"], o["cr"], o["tq"], o["rf"]
    out = []
    def chk(n, c):
        out.append((n, bool(c)))
    chk("W0: M's words, verbatim in the rulings file (390, 427)", o["words"])
    chk("W1: N ln2 k T_H = (2/3) E in 5D and E/2 in 4D (exact), so the plane's thermal inflow is E/2 and (3/8) E; "
        "tau_w = (1 + b) x life = 8.63e14 clocks at the example, b = 0.0062",
        sm["ts5"] == sp.Rational(2, 3) and sm["ts4"] == sp.Rational(1, 2) and sm["ein5"] == sp.Rational(1, 2)
        and sm["ein4"] == sp.Rational(3, 8) and abs(w["E_in"] / w["E"] - 0.5) < 1e-12
        and abs(w["tau_w"] / w["life"] - (1 + w["b"])) < 1e-12 and "%.3g" % w["tau_w"] == "8.63e+14"
        and "%.2g" % w["b"] == "0.0062")
    chk("W2: position 2's face open exactly while the README is within it (390, G10): T_open = tau_w, 3.2e-14 s at "
        "the example and 2.2e56 s at the Earth cap -- not J1's 33.6 clocks",
        w["T_open"] == w["tau_w"] and "%.2g" % pt["T_s"] == "3.2e-14" and "%.2g" % pt["T_L_s"] == "2.2e+56")
    c = pt["counts"]
    chk("W3: Barcelo's criterion, 63.0 clocks for 1 eV; expected perturbations over T_open: 2.1e-36 (3 K) to 7.7e-8 "
        "(1e10 K), 6.4e-25 (air), 1.3e-15 (a metal's electrons), 0.43 (inside a nucleus); every environment above 1e60 at "
        "the Earth cap",
        "%.1f" % pt["t_eV"] == "63.0" and "%.2g" % c["blackbody 3 K"] == "2.1e-36"
        and "%.2g" % c["blackbody 1e10 K"] == "7.7e-08" and 1e-25 < c["air (2.5e25 /m^3 at 500 m/s)"] < 1e-24
        and 1e-16 < c["a metal's electrons (2.5e30 /m^3 at 1e7 m/s)"] < 1e-14
        and 0.1 < c["inside a nucleus (1.4e44 /m^3 at 0.2 c)"] < 1 and min(pt["counts_L"].values()) > 1e60)
    chk("W4: position 2's vacuum -- the Boulware stress -M(2r - 3M)/(48 pi r^4), -kappa^2/(48 pi) at the face; the "
        "crossing gives mu_fut = -(Delta eps)/(2 delta r_h), a negative mass growing as e^(kappa t); t_q = 35.8 "
        "clocks (31.2 at one percent) at the example, 155 e-folds at the Earth cap",
        st["face_is_kappa"] and cr["sign"] < 0
        and sp.simplify(cr["lead"] + sp.Symbol("Delta", positive=True) * sp.Symbol("epsilon", positive=True)
                        / (2 * sp.Symbol("r_h", positive=True))) == 0
        and "%.1f" % tq["t_q"] == "35.8" and "%.1f" % tq["t_q1"] == "31.2" and "%.0f" % tq["t_qL_efolds"] == "155")
    chk("W5: the time-reversed Unruh state is regular at the face (zero as f^2) and needs kappa^2/(48 pi) sent in from "
        "position 2's infinity: 0.503 E at T_H = 3.3e16 K over the open period",
        st["regular"] and sp.simplify(st["infinity"] - 1 / (768 * sp.pi * sp.Symbol("M", positive=True) ** 2)) == 0
        and "%.3f" % rf["need"] == "0.503" and "%.2g" % rf["TH"] == "3.3e+16")
    chk("W6: T_open / t_q = 2.4e13 at the example and 2.4e64 at the Earth cap -- the face's holding is not given; "
        "control: J1's withdrawn 33.6 clocks lies below t_q",
        "%.2g" % (w["T_open"] / tq["t_q"]) == "2.4e+13" and "%.2g" % (w["T_open_L"] / tq["t_qL_clocks"]) == "2.4e+64"
        and J1_OPEN < tq["t_q"])
    return out


def report(o=None):
    o = o or compute()
    w, pt, tq, rf = o["w"], o["pt"], o["tq"], o["rf"]
    print("face2_open.py -- position 2's face over its open period, on 390 (item 489, F1)\n")
    print("W1 the write at the face's balance: E_in = E/2 = %.4g J, tau_w = %.4g clocks = (1 + %.4f) x the life %.4g"
          % (w["E_in"], w["tau_w"], w["b"], w["life"]))
    print("W2 position 2's face open %.3g clocks = %.3g s (example); %.3g clocks of GM/c^3 = %.3g s (Earth cap)"
          % (w["T_open"], pt["T_s"], w["T_open_L"], pt["T_L_s"]))
    print("W3 1 eV from position 2 forms a trapped surface after %.1f clocks; expected perturbations over the open period:"
          % pt["t_eV"])
    for e in pt["counts"]:
        print("     %-46s %.2g   (Earth cap %.2g)" % (e, pt["counts"][e], pt["counts_L"][e]))
    print("W4 position 2's vacuum: the face's own negative flux breaks it at t_q = %.1f clocks (%.1f at 1%%); Earth cap "
          "%.1f e-folds" % (tq["t_q"], tq["t_q1"], tq["t_qL_efolds"]))
    print("W5 the reversed state holds it: position 2 sends %.3f E at T_H = %.3g K -- nothing supplies it"
          % (rf["need"], rf["TH"]))
    print("W6 T_open / t_q = %.3g (example), %.3g (Earth cap)" % (w["T_open"] / tq["t_q"],
                                                                    w["T_open_L"] / tq["t_qL_clocks"]))


MUTANTS = {"short_open": "position 2's face open J1's 33.6 clocks (W2, W6)",
           "positive_vac": "the vacuum's packet read as positive (W4)"}


def selftest(quiet=False):
    r_ = checks(compute())
    if not quiet:
        for n_, ok in r_:
            print("  [%s] %s" % ("ok" if ok else "FAIL", n_))
    k = sum(ok for _, ok in r_)
    if not quiet:
        print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            failed = [n_.split(":")[0] for n_, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  [%s] %s -> %s" % ("caught" if failed else "MISSED", desc, ", ".join(failed) or "nothing"))
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
