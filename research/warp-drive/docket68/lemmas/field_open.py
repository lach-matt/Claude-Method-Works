#!/usr/bin/env python3
"""field_open.py -- item 494: can a magnetic or other non-electric field open and hold a corridor, with no initial
README, opened by the field itself, that information or matter can pass?  Run on what the board holds and on prior
art, not answered from memory.

M, 494: "Can we possibly conceive a condition where a magnetic or non electric field can open and hold a corridor that
either information or matter can pass without an initial readme, opened by the field itself?"  Uses magnetic_chain
(463: the Ernst-instanton action), mmp_corridor (445 (2): MMP and MM, READ in full) and mag2m (493: two spacetimes,
no).  Labels: computed (exact unless marked), deduced, READ, M's.

  F0 (read) M's words, verbatim in the rulings file: 494; with 109, 162, 390 and 493.
  F1 (computed, exact; READ) A classical non-electric field cannot hold a throat open.
     - A throat (Morris-Thorne) needs flare-out, b'(r0) < 1.  Einstein's equations give
       8 pi (rho + p_r) = (b'(r0) - 1)/r0^2 there, so it needs rho + p_r < 0.
     - A magnetic field (and any Maxwell or Yang-Mills field) has T_ab k^a k^b = |F.k|^2/(4 pi) >= 0 for every null
       k, since F.k is orthogonal to k.  A radial magnetic field gives rho + p_r = 0 exactly: the marginal throat,
       b' = 1, which is the extremal hole's infinite AdS2 x S2 throat and not a passage.
     - A canonical scalar gives rho + p_r = (1 - b/r) phi'^2/(4 pi), which is >= 0 and is zero at the throat.
     - Only a phantom scalar does it classically: Ellis-Bronnikov, rho + p_l = -a^2/(4 pi (l^2 + a^2)^2) < 0.  It is
       a ghost field, off established physics, and linearly unstable (Gonzalez, Guzman and Sarbach; Cremona,
       Pirotta and Pizzocchero 1805.02602, READ).  The non-minimally coupled scalar's wormholes (Barcelo and Visser
       gr-qc/9908029) are unstable too, the growth having no upper bound (Bronnikov and Grinyok gr-qc/0201083,
       gr-qc/0411063, READ).
     - MMP (READ): "Solutions with this topology are forbidden in classical physics because of the average null energy
       condition"; and a non-abelian magnetic field "can be screened ... This is why we insisted that the gauge field
       is U(1)".
  F2 (computed; READ) The field opens it itself only by tunnelling, and only at the hole's own field strength.
     - Classical topology change needs a closed timelike curve (Geroch 1967), and Einstein's equation with a
       non-negative energy density forbids it (Tipler 1977; both READ through Borde gr-qc/9406053 and 1010.2311).  So the one route
       is quantum: pair creation of magnetic holes whose horizons are identified, a wormhole made by the field
       (Garfinkle-Strominger; Dowker, Gauntlett, Giddings and Horowitz, READ).  The flux through the throat is the
       field's own lines, so no magnetic monopole is needed and dF = 0 holds (deduced).
     - The rate is e^(-S_E), S_E = 4 pi q^2 (1 - qB)^2/(1 - (1 - qB)^4).  At qB = 1/2 this is 16 pi q^2/15 exactly:
       of order the pair's area in Planck units, unless qB -> 1.
     - At qB = 1 the field is the mouth's own horizon field, 1/q.  Its energy within the mouth's radius is 1/6 of the
       mouth's mass (exact), and that region is 1/3 of the way to its own horizon (2E/r).  The field opening a mouth
       is self-gravitating over the mouth's size.
     - Once in the observable universe's history, were the field to fill it for its whole age: S_E <= ln(V4/l_P^4)
       = 563 (H0 67.4 km/s/Mpc, t0 13.787 Gyr; the prefactor taken as Planck, shifting this by its log only).
     - The smallest magnetic mouth (one Dirac charge, 5.85 l_P) is opened at that rate by 6.3e51 T (qB = 0.17 of its
       horizon field, 3.7e52 T).  At 1/10 of hbar c/TeV, MMP's Standard-Model window, it needs 1 - qB = 5.5e-15.
       At 1 m it needs 3.5e18 T tuned to
       1 - qB = 1.1e-34, and at 2 m 1.7e18 T tuned to 5.4e-35.  At qB = 1/2 the action is 1.3e70 at 1 m.  The
       strongest field known is a magnetar's, 1e11 T.
     - Near qB = 1 the background's own gravity is of the pair's scale, so the formula there is the weak-field family
       continued and its numbers are order of magnitude (deduced).
  F3 (computed: exact Newtonian and Coulomb forms; READ) The field that opens cannot be the field that holds.
     - The pair is made at rest at separation d0 = 2m/(qB): the field's work equals the pair's rest energy.  For the
       extremal pair (m = q) it stays bound only if the field ends within one mouth radius beyond d0 (exact,
       whatever B: qB (d - d0) < 2 q^2/d0 gives d - d0 < q).
     - If the field goes on, d grows without bound, the fermions' return path L = l + d is infinite, and the hold is
       gone: 493's dE/dl < 0.
     - No static field holds the mouths apart: the potential energy of a magnetic charge in the partner's field, a
       uniform field and gravity has zero Laplacian (exact), so no equilibrium is stable (Earnshaw).
     - So the mouths must orbit.  Gravity plus the magnetic attraction give Omega = 2 sqrt(r_e/d^3) exactly, which is
       MMP's (6.50) ("the total force includes gravity and the magnetic attraction", READ).
     - A pair made at rest along the field has no angular momentum: released, "these would attract and would fall
       into each other" (MMP, READ).  The orbit's angular momentum must come from the field's own geometry within
       about one mouth radius.  How to take the made pair to MMP's state is open in prior art: "we did not describe a
       simple procedure for taking the system to that solution" (MMP 9.3, READ).  It is not computed here.
  F4 (computed by mmp_corridor; READ) Held, it can pass information and matter.
     - The hold is the field's own quantum modes: massless charged fermions on the closed field lines, negative
       Casimir energy (MMP).  In the board's RS2 with the bulk U(1), MM's classical five-dimensional form.
     - At 1 m on our plane: l = 3.0e5 m, gap 6.5e-13 eV (held below 7.5e-9 K), binding 1.3e33 J, and a throat
       destroyed by 2.1e34 J (16 x binding, MMP's q/l).  At 2 m: l = 1.3e6 m, below 1.8e-9 K, binding 6.1e32 J.
       At MM's floor (10 R5 = 0.14 mm on the board's R5): l = 2.7 mm, below 0.85 K.
     - No mouth in MM's regime holds in the cosmic background (2.725 K): the largest held temperature, at the floor,
       is 0.85 K, and it falls as the mouth grows.
     - Information passes as low-energy waves.  Matter passes if smaller than the mouth (large N_f, MMP 7) and far
       below the destroying energy: "If enough energy is sent through the wormhole mouth, a pair of horizons will
       develop" (MMP, READ).
     - It is never a shortcut: pi l > d (211 times at 1 m at the orbit's d, 8.4 at the floor), "a long wormhole
       that does not lead to causality violations" (MMP, READ).
     - It has no horizon (MMP, READ), so no inner or Cauchy horizon is used anywhere (481, 484).  The opening's
       instanton uses only the section outside r+.
  F5 (M's; deduced) With no README.  Nothing in F2-F4 involves one.
     - The opening's energy is the field's.  The holding's is the field's fermion modes.  The size is the field's,
       r = 1/B at qB = 1.
     - It opens because of the field, not the README (390), and takes the field's size, not the README's (162).
     - It is a corridor, but not the theorem's.  It joins two places in one universe only: between two spacetimes the
       return path is infinite (493).
  F6 (deduced) So: yes, it is conceivable, under these conditions together.
     (i)   A magnetic (U(1)) field at the mouth's own horizon strength, over a region a few mouth radii across, opens
           a pair of mouths by tunnelling.
     (ii)  The field ends within one mouth radius of the pair, and the pair orbits.
     (iii) Massless charged species thread the throat along closed field lines, and the throat stays colder than its
           gap.
     (iv)  One universe, and a long wormhole: information and small, light matter pass, never faster than outside.
     One step is not computed: taking the made pair, which has no angular momentum, into MMP's orbit.  Prior art
     leaves it open (MMP 9.3), and the made pair falls back without it.
     - It is not classical: a classical field gives rho + p_r = 0 at best.
     - It is not between two spacetimes (493).  Phantom and non-minimal scalars, pure gravity and rotation are
       excluded.
     - Its scales:
       - The opening is real only near the Planck size (6e51 T), where semiclassical physics is not trusted.
       - The holding needs r_e << hbar c/TeV in the Standard Model, or r >= 10 R5 in RS2, and a throat colder than
         0.85 K even at RS2's floor.
       - At 1-2 m the opening needs a field 3e7 times a magnetar's, tuned to 1e-34.
     - Neutral pairs opened by vacuum energy (Bousso and Hawking gr-qc/9606052, READ: suppressed unless the vacuum
       energy is near Planck's) carry no flux to hold a throat, and with quantum effects most evaporate.
Imports magnetic_chain.py and mmp_corridor.py by path.  Stdlib + sympy.
python3 field_open.py [--selftest | --mutants]
"""
import os, sys, math, re, io, random, contextlib, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((494, "Can we possibly conceive a condition where a magnetic or non electric field can open and hold a corridor"),
         (493, "Can a magnetic warp corridor of be opened between two different spacetimes"),
         (109, "A horizon cannot exist without the object"), (162, "only the size that is needed to hold the object"),
         (390, "it closes when there is nothing contained within the corridor"))
H0_KMS_MPC, T0_GYR = 67.4, 13.787           # Planck 2018; standard, not READ here
MPC_M, GYR_S = 3.0857e22, 3.15576e16
T_CMB = 2.7255                              # K; standard


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    ok = True
    for n, w in WORDS:
        m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
        ok = ok and bool(m) and w in " ".join(m.group(0).split())
    return ok


# ------------------------------------------------------------------ F1
def einstein_mixed(g, x):
    """G^a_b of a diagonal metric g in coordinates x"""
    n = len(x)
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    def Ric(b, c):
        return sp.simplify(sum(sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c])
                               + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n))
                               for a in range(n)))
    R = sp.Matrix(n, n, lambda b, c: Ric(b, c))
    Rs = sp.simplify(sum(gi[a, b] * R[a, b] for a in range(n) for b in range(n)))
    return sp.simplify(gi * R - Rs / 2 * sp.eye(n))


def f1():
    t, r, th, ph, l, a = sp.symbols("t r theta phi l a", positive=True)
    b, Phi, psi = sp.Function("b")(r), sp.Function("Phi")(r), sp.Function("phi")(r)
    # Morris-Thorne: rho + p_r = (G^r_r - G^t_t)/(8 pi); at the throat b = r0
    g = sp.diag(-sp.exp(2 * Phi), 1 / (1 - b / r), r ** 2, r ** 2 * sp.sin(th) ** 2)
    Gm = einstein_mixed(g, [t, r, th, ph])
    nec_r = sp.simplify(Gm[1, 1] - Gm[0, 0])                       # = 8 pi (rho + p_r)
    r0, bp = sp.symbols("r_0 bprime", positive=True)
    at_throat = sp.simplify(nec_r.subs(sp.Derivative(b, r), bp).subs(b, r0).subs(r, r0))
    flare = sp.simplify(at_throat - (bp - 1) / r0 ** 2) == 0
    # the extremal magnetic hole in this form: 1 - b/r = (1 - q/r)^2, so b(q) = q and b'(q) = 1
    q = sp.symbols("q", positive=True)
    bx = 2 * q - q ** 2 / r
    marginal = sp.simplify(bx.subs(r, q) - q) == 0 and sp.simplify(sp.diff(bx, r).subs(r, q) - 1) == 0
    # radial magnetic field B = q/r^2: rho = B^2/(8 pi), p_r = -B^2/(8 pi), p_t = +B^2/(8 pi) (Gaussian, G = c = 1)
    B = q / r ** 2
    s = -1 if "ghost_maxwell" in MUT else 1                          # the mutant: the Maxwell stress with its sign flipped
    rho, pr, pt = s * B ** 2 / (8 * sp.pi), -s * B ** 2 / (8 * sp.pi), s * B ** 2 / (8 * sp.pi)
    mag_radial = sp.simplify(rho + pr) == 0
    mag_tangential = sp.simplify(rho + pt - B ** 2 / (4 * sp.pi)) == 0
    # any Maxwell (or, per colour, Yang-Mills) field: T_kk = (F.k).(F.k)/(4 pi) with (F.k).k = 0, so T_kk >= 0
    eta = sp.diag(-1, 1, 1, 1)
    random.seed(494)
    worst = float("inf")
    for _ in range(4000):
        Fl = sp.zeros(4, 4)
        for i in range(4):
            for j in range(i + 1, 4):
                v = random.gauss(0, 1)
                Fl[i, j], Fl[j, i] = v, -v
        n3 = [random.gauss(0, 1) for _ in range(3)]
        nn = math.sqrt(sum(c * c for c in n3))
        k = sp.Matrix([1] + [c / nn for c in n3])                      # null, upper index
        Fk = Fl * k                                                     # v_a = F_ab k^b
        vu = eta * Fk                                                   # raise with eta (eta^-1 = eta)
        Tkk = s * float((Fk.T * vu)[0]) / (4 * math.pi)
        orth = abs(float((Fk.T * k)[0]))
        worst = min(worst, Tkk)
        if orth > 1e-12:
            worst = -1.0
    maxwell_nec = worst >= -1e-15
    # canonical scalar: T_ab = d_a phi d_b phi - g_ab (...)/2, so rho + p_r = g^rr phi'^2 = (1 - b/r) phi'^2 (x 1/(4 pi))
    scal = (1 - b / r) * sp.diff(psi, r) ** 2 / (4 * sp.pi)
    scal_throat = sp.simplify(scal.subs(b, r)) == 0
    # Ellis-Bronnikov: ds^2 = -dt^2 + dl^2 + (l^2 + a^2) dOmega^2
    ge = sp.diag(-1, 1, l ** 2 + a ** 2, (l ** 2 + a ** 2) * sp.sin(th) ** 2)
    Ge = einstein_mixed(ge, [t, l, th, ph])
    ellis = sp.simplify((Ge[1, 1] - Ge[0, 0]) / (8 * sp.pi) + a ** 2 / (4 * sp.pi * (l ** 2 + a ** 2) ** 2)) == 0
    return dict(flare=flare, at_throat=at_throat, marginal=marginal, mag_radial=mag_radial,
                mag_tangential=mag_tangential, maxwell_nec=maxwell_nec, worst=worst, scal_throat=scal_throat,
                ellis=ellis)


# ------------------------------------------------------------------ F2
def s_star():
    """ln of the observable universe's four-volume in Planck units: the action for one event in its history"""
    MP = _load("mmp_corridor.py", "fo_mp")
    R = MP.C / (H0_KMS_MPC * 1e3 / MPC_M)
    V4 = 4 / 3 * math.pi * R ** 3 * MP.C * T0_GYR * GYR_S
    return math.log(V4 / MP.LP ** 4)


def tuning(q, S):
    """1 - qB at which 4 pi q^2 e^2/(1 - e^4) = S, e = 1 - qB (exact root of S e^4 + 4 pi q^2 e^2 - S = 0)"""
    if "weak_tuning" in MUT:                                            # the mutant: the weak-field form pi q^2/(qB)
        return 1 - math.pi * q ** 2 / S
    A = 4 * math.pi * q ** 2
    e2 = 2 * S / (A + math.sqrt(A * A + 4 * S * S))
    return math.sqrt(e2)


def solve_qB(MC, q, S):
    """qB at which the Ernst instanton's action equals S"""
    e = tuning(q, S)
    if "weak_tuning" in MUT or e > 1e-3:
        lo, hi = 1e-9, 1 - 1e-15                                        # bisection on the action itself
        if "weak_tuning" in MUT:
            return 1 - e, e
        for _ in range(200):
            mid = (lo + hi) / 2
            if MC.pair_action(q, mid) > S:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2, 1 - (lo + hi) / 2
    return 1 - e, e


def f2():
    MC = _load("magnetic_chain.py", "fo_mc"); MP = _load("mmp_corridor.py", "fo_mp2")
    q, x, rr = sp.symbols("q x r", positive=True)
    S = 4 * sp.pi * q ** 2 * (1 - x) ** 2 / (1 - (1 - x) ** 4)
    half = sp.simplify(S.subs(x, sp.Rational(1, 2)) - 16 * sp.pi * q ** 2 / 15) == 0
    # the field at qB = 1 is 1/q; with r = q its energy within r (B^2/8pi x 4 pi r^3/3) over the mass r
    E_field = (1 / rr) ** 2 / (8 * sp.pi) * sp.Rational(4, 3) * sp.pi * rr ** 3
    sixth = sp.simplify(E_field / rr - sp.Rational(1, 6)) == 0
    third = sp.simplify(2 * E_field / rr - sp.Rational(1, 3)) == 0
    Ss = s_star()
    e_ = math.sqrt(4 * math.pi * MC.ALPHA0)
    sizes = {"one Dirac charge": 1 / (2 * math.sqrt(MC.ALPHA0)) * MP.LP, "TeV/10": MP.TEV_LENGTH / 10,
             "1 m": 1.0, "2 m": 2.0}
    rows = {}
    for name, r in sizes.items():
        qp = r / MP.LP                                                  # Planck units (extremal: q = r)
        x_, eps = solve_qB(MC, qp, Ss)
        B_T = x_ / (r * MC.GEOM_PER_TESLA)
        S_back = MC.pair_action(qp, x_) if eps > 1e-12 else 4 * math.pi * qp ** 2 * eps ** 2 / (1 - eps ** 4)
        rows[name] = dict(r=r, q=qp, Qd=qp * e_ / math.sqrt(math.pi), qB=x_, eps=eps, B_T=B_T,
                          B_h=1 / (r * MC.GEOM_PER_TESLA), S_half=16 * math.pi * qp ** 2 / 15,
                          back=S_back / Ss, magnetar=B_T / MC.B_MAGNETAR_T)
    return dict(half=half, sixth=sixth, third=third, S_star=Ss, rows=rows, magnetar_T=MC.B_MAGNETAR_T)


# ------------------------------------------------------------------ F3
def f3():
    q, B, d, d0, m, re_, D = sp.symbols("q B d d_0 m r_e D", positive=True)
    # Newtonian, extremal m = q: made at rest at d0 = 2m/(qB); field force qB on each (relative coordinate), attraction
    # gravity m^2/d^2 plus magnetic q^2/d^2
    d0v = 2 * q / (q * B)
    KE = q * B * (d - d0v) - (2 * q ** 2 / d0v - 2 * q ** 2 / d)            # kinetic energy at d, field on up to d
    bound = sp.solve(sp.Eq(KE, 2 * q ** 2 / d), d)                          # the escape line: KE = U(d)
    bound_ok = len(bound) == 1 and sp.simplify(bound[0] - d0v - q) == 0
    # Earnshaw: potential energy of +q at x in the partner's (-q at the origin) field, a uniform field, and gravity
    X, Y, Z = sp.symbols("X Y Z", real=True)
    rho = sp.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    U = -q * B * Z - q ** 2 / rho - m ** 2 / rho                            # q psi, psi = -B Z - q/rho; and gravity
    lap = sp.simplify(sp.diff(U, X, 2) + sp.diff(U, Y, 2) + sp.diff(U, Z, 2)) == 0
    # the orbit: each mouth at d/2, m Omega^2 d/2 = (m^2 + q^2)/d^2 with m = q = r_e
    W = sp.symbols("Omega", positive=True)
    force = re_ ** 2 / d ** 2 if "gravity_only" in MUT else 2 * re_ ** 2 / d ** 2   # the mutant: no magnetic pull
    Om = sp.solve(sp.Eq(re_ * W ** 2 * d / 2, force), W)[0]
    mmp_650 = sp.simplify(Om - 2 * sp.sqrt(re_ / d ** 3)) == 0
    # with the field on everywhere the separation grows without bound: the relative force qB - 2q^2/d^2 > 0 beyond d0
    beyond = sp.simplify((q * B - 2 * q ** 2 / d ** 2).subs(d, d0v))
    runaway = sp.simplify(beyond - q * B * (1 - q * B / 2)) == 0
    return dict(bound_ok=bound_ok, bound=bound, lap=lap, mmp_650=mmp_650, runaway=runaway)


# ------------------------------------------------------------------ F4
def f4():
    MP = _load("mmp_corridor.py", "fo_mp3")
    R5 = MP.ell()
    pts = {"1 m": MP.point(1.0, R5), "2 m": MP.point(2.0, R5), "10 R5": MP.point(10 * R5, R5)}
    for p in pts.values():
        p["E_destroy"] = 16 * p["Eb_J"]                                   # c2/l = 16 |E_min| (MMP's q/l)
        p["long"] = math.pi * p["l"] / p["d_rot"]
    tmax = [MP.point(10 * R5 * 10 ** (k / 4), R5)["Tmax"] for k in range(30)]   # the floor up past 2 m
    return dict(pts=pts, R5=R5, falls=all(tmax[i] > tmax[i + 1] for i in range(len(tmax) - 1)))


def compute():
    return dict(words=words(), f1=f1(), f2=f2(), f3=f3(), f4=f4())


def checks(o):
    a, b, c, d = o["f1"], o["f2"], o["f3"], o["f4"]
    R, P = b["rows"], d["pts"]
    return [("F0: M's 494, 493, 109, 162 and 390 verbatim in the rulings", o["words"]),
            ("F1: flare-out needs rho + p_r < 0 (8 pi (rho + p_r) = (b' - 1)/r0^2); a magnetic field gives rho + p_r = 0 "
             "(the extremal throat, b' = 1) and T_kk >= 0 for every null k (4000 fields); a canonical scalar 0 at the "
             "throat; only the phantom Ellis field goes negative, -a^2/(4 pi (l^2 + a^2)^2)",
             a["flare"] and a["marginal"] and a["mag_radial"] and a["mag_tangential"] and a["maxwell_nec"]
             and a["scal_throat"] and a["ellis"]),
            ("F2: S_E(qB = 1/2) = 16 pi q^2/15; at qB = 1 the field's energy within the mouth is 1/6 of its mass, 1/3 "
             "of the way to its own horizon; one event in the universe's history at S_E = 563",
             b["half"] and b["sixth"] and b["third"] and round(b["S_star"]) == 563),
            ("F2: one Dirac charge (5.85 l_P) opened by 6.3e51 T, qB 0.17; TeV/10 needs 1 - qB = 5.5e-15; 1 m 3.5e18 T "
             "tuned to 1.1e-34 (S_E 1.3e70 at qB = 1/2), 2 m 1.7e18 T tuned to 5.4e-35; each S_E back at 563",
             "%.3g" % (R["one Dirac charge"]["q"]) == "5.85" and "%.2g" % R["one Dirac charge"]["B_T"] == "6.3e+51"
             and "%.2g" % R["one Dirac charge"]["qB"] == "0.17" and "%.2g" % R["TeV/10"]["eps"] == "5.5e-15"
             and "%.2g" % R["1 m"]["B_T"] == "3.5e+18"
             and "%.2g" % R["1 m"]["eps"] == "1.1e-34" and "%.2g" % R["1 m"]["S_half"] == "1.3e+70"
             and "%.2g" % R["2 m"]["B_T"] == "1.7e+18" and "%.2g" % R["2 m"]["eps"] == "5.4e-35"
             and all(abs(v["back"] - 1) < 1e-9 for v in R.values())),
            ("F3: the made pair stays bound only if the field ends within one mouth radius beyond d0 = 2/B; with the "
             "field on it runs away; no static field holds it (zero Laplacian); the orbit is MMP's Omega = 2 sqrt(r/d^3)",
             c["bound_ok"] and c["runaway"] and c["lap"] and c["mmp_650"]),
            ("F4: held at 1 m: l 3.0e5 m, below 7.5e-9 K, binding 1.3e33 J, destroyed by 2.1e34 J; 2 m: l 1.3e6 m, "
             "1.8e-9 K, 6.1e32 J; 10 R5: l 2.7 mm, below 0.85 K, so none held in the 2.725 K background (the bound falls "
             "with size); pi l / d = 211 at 1 m, every case long",
             "%.2g" % P["1 m"]["l"] == "3e+05" and "%.2g" % P["1 m"]["Tmax"] == "7.5e-09"
             and "%.2g" % P["1 m"]["Eb_J"] == "1.3e+33" and "%.2g" % P["1 m"]["E_destroy"] == "2.1e+34"
             and "%.2g" % P["2 m"]["l"] == "1.3e+06" and "%.2g" % P["2 m"]["Tmax"] == "1.8e-09"
             and "%.2g" % P["2 m"]["Eb_J"] == "6.1e+32" and "%.2g" % P["10 R5"]["l"] == "0.0027"
             and "%.2g" % P["10 R5"]["Tmax"] == "0.85" and P["10 R5"]["Tmax"] < T_CMB and d["falls"]
             and "%.3g" % P["1 m"]["long"] == "211" and all(p["long"] > 1 for p in P.values()))]


def report(o=None):
    o = o or compute()
    a, b, c, d = o["f1"], o["f2"], o["f3"], o["f4"]
    print("F1 at the throat 8 pi (rho + p_r) = %s; Maxwell min T_kk over 4000 fields %.3g" % (a["at_throat"], a["worst"]))
    print("F2 S* = %.2f (magnetar %.0e T)" % (b["S_star"], b["magnetar_T"]))
    for k, v in b["rows"].items():
        print("   %-17s r %.3g m  q %.3g l_P  Dirac %.3g  qB %.6g  1-qB %.3g  B %.3g T (horizon %.3g T)  S(1/2) %.3g  "
              "x magnetar %.2g" % (k, v["r"], v["q"], v["Qd"], v["qB"], v["eps"], v["B_T"], v["B_h"], v["S_half"],
                                    v["magnetar"]))
    print("F3 escape at d = %s" % c["bound"])
    print("F4 R5 = %.3g m; the held temperature falls with size from the floor: %s" % (d["R5"], d["falls"]))
    for k, p in d["pts"].items():
        print("   %-6s l %.3g m  gap %.3g eV  Tmax %.3g K  Eb %.3g J  destroy %.3g J  d_rot %.3g m  pi l/d %.3g  regime %s"
              % (k, p["l"], p["gap_eV"], p["Tmax"], p["Eb_J"], p["E_destroy"], p["d_rot"], p["long"], p["regime"]))
    for n_, ok in checks(o):
        print("  [%s] %s" % ("ok" if ok else "FAIL", n_))


MUTANTS = {"ghost_maxwell": "the Maxwell stress with its sign flipped (F1)",
           "weak_tuning": "the weak-field action pi q^2/(qB) used near qB = 1 (F2)",
           "gravity_only": "the mouths' orbit with gravity alone, no magnetic attraction (F3)"}


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
        except Exception as ex:                                          # a mutant that breaks the run is caught
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
