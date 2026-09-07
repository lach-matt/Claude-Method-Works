#!/usr/bin/env python3
"""fieldentry.py -- THE ENTRY POINT READ WITH THE ENTRANT'S OWN ELECTRON, ON THE CORPUS'S OWN FIELD.

  Chapter 34 fixes where `a` sits in its corridor by the ionisation energy:
      a_meas = (n - nu) / sqrt(p),   nu = sqrt(R / IE),   p = n - l - 1,
      t = (a_meas - L) / (U - L)     read at the subshell's opening,
  and states t(l) -> sqrt(l(l+1)/2), measured at p and d only (register 1337: "no f test").
  Finding R4-13 ran the f test with protactinium's FIRST ionisation energy and found +4.0 %;
  it then said the point reads the wrong electron -- an actinide ionises from 7s, not 5f --
  and that "a subshell-resolved binding energy for the 5f electron at protactinium" was not
  in the corpus.

  THAT LAST SENTENCE WAS WRONG, AND THIS INSTRUMENT IS THE CORRECTION.  The Lowdin work's own
  derived field -- the sealed chain, scalar-relativistic Hartree-Fock on the ruling field
  (hfc2, SR, CORR=False, c = 137.035999), reference the cation of Z carrying config(Z-1) --
  carries the 5f channel's removal energy at Z = 91 as its entrant row, D = -0.30535 Ha, quoted
  six times in the record; and DELIVERABLE-3 already converted it to n* = 1/sqrt(-2D) = 1.2796
  and delta = n - n* = 3.7204, which IS a_meas for 5f at Pa (p = 1).  The record computed the
  entry-point quantity from the field and used it for the collapse condition, never for t.

  WHAT THIS INSTRUMENT DOES.
  1. Lists every sealed field row the record quotes at an opening, with its quote.
  2. Rebuilds the field's producer from the repository and runs it: the entrant's own
     delta-SCF removal energy at all seven two-sided openings (3p 4p 5p 6p 4d 5d 5f) from the
     observed ground configuration (LW1-ground.py), and the chain's own step at Z = 91.  Where
     the record quotes a value the regenerated one is checked against it to 1e-5 Ha; 3p and 6p
     are quoted nowhere and are measured here for the first time.
  3. Reads t at every opening two ways -- with the first ionisation energy (register 1337) and
     with the entrant's own binding energy -- and reports both against sqrt(l(l+1)/2).

  THE PRODUCER, AND HOW IT IS REACHED.  Nothing under recovered/ is edited or copied into this
  tree.  The chain's modules are loaded by path in dependency order and registered under their
  own names so that their bare-name imports resolve: tfd rad step2_run eigen_fix derive_P
  ground(= LW1-ground.py, a seated member) hfs t5_scf t7b_hf t7c_kernel t7c_hfsr hfc2 nlchain.
  The C Numerov (recovered/shoot_x.c) is compiled into a temporary directory at run time.

  FOUR DEPARTURES FROM THE RECOVERED TEXT, EACH DECLARED, EACH GATED.
  (a) nlchain's reference is the CATION of Z carrying config(Z-1).  The recovered nlchain.py is
      the first build, whose reference sat at nuclear charge Z-1; FINDING-CHAIN-SESSION-40 s1
      (F40.1) records the correction and the gate that caught it (Li 2s -4.5717 -> -0.19629).
      The record's own fix, applied to the text in memory.
  (b) t7c_hfsr calls a 14-argument shoot_x -- two doubles seeding the inward particular branch
      from the previous orbital -- that the session-18 shoot_x.c (12 arguments, the only C file
      recovered) does not have.  shoot_x14 is written here as that C routine with the two seeds
      replacing its adiabatic start; everything else is the recovered text.  RECONSTRUCTED.
      Gate: the record's G1, He 1s at c = 1e6 -> -0.91796.
  (c) The seed bisections (step2_run.eigen, eigen_fix.eigen, t7c_kernel.eigen_sr) ride
      rad._shoot, which rescales by 1e200 and integrates on into the region where h^2 q/12 > 1,
      where the Numerov recursion flips sign every step; the bisection counts the flips as
      nodes and returns its bracket cap for every 1s at Z >= 10 (measured: -50.0 at Z = 10,
      -4140.5 at Z = 91).  The sealed runtime rode a C shoot (shoot.c, libshoot.so) that is not
      in the repository.  Here the outward integration stops at |y| > 1e150, which always
      precedes that region.  RECONSTRUCTED.  Gates: hydrogen's defects vanish, H 1s and Z = 70
      1s land on Dirac (the kernel's own gates), the TFD seeds are node-clean to Z = 91.
  (d) The recovered derive_P.numerov_wf has no forbidden-region tail clean; t7c_kernel's
      numerov_wf_sr carries one "as hfs.numerov_wf", so the sealed hfs had it and the recovered
      derive_P predates it.  The clean is appended verbatim from numerov_wf_sr.  RECONSTRUCTED.
  t7c_cuaudit.py, which hfc2 imports at module level, is absent from the repository; it is used
  only in the correlation path, which the chain runs with CORR=False.  A stub that raises if
  called stands in for it.

  THE GATE ON ALL FOUR TOGETHER is reproduction of the sealed rows: a seed cannot change a
  converged Hartree-Fock energy, so if the regenerated 4p, 5p, 4d, 5d, 4f and 5f rows land on
  the record's to 1e-5 Ha, the producer here is the producer there in every respect that reaches
  a number.  The record's own PC-0 machinery gate (Na 3s -0.18217, K 4s -0.14774, 3d -0.05807,
  4p -0.09363) is run as well.

  STATUS OF EVERY FIGURE.  Sealed rows: RECORD-CARRIED, quote given.  Regenerated rows: MEASURED
  here, stored in fieldentry-field.json by --field, never hand-edited.  The two Numerov repairs:
  RECONSTRUCTED, and nothing they touch survives to a converged energy.  Nothing is repaired in
  any volume.

  usage:  python3 fieldentry.py            report from the sealed rows and the banked field file
          python3 fieldentry.py --field    regenerate the field (minutes; needs gcc, numpy, scipy)
          python3 fieldentry.py --selftest

stdlib for the report; numpy and scipy for --field and the machinery half of --selftest.
"""
import argparse, contextlib, importlib.util, io, json, math, os, shutil, subprocess, sys, tempfile, types

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEMBERS = os.path.join(ROOT, "method", "members")
RECOVERED = os.path.join(ROOT, "recovered")
FIELD_JSON = os.path.join(HERE, "fieldentry-field.json")

HA_EV = 27.211386245988

# --------------------------------------------------------------------- the openings
# label, element, Z, n, l.  The corridors come from entrypoint.py, which computes them as
# walk.py does; 5f's floor is 5g's and exists only under RULINGS-R4e s1.
OPENINGS = [("3p", "Al", 13, 3, 1), ("4p", "Ga", 31, 4, 1), ("5p", "In", 49, 5, 1),
            ("6p", "Tl", 81, 6, 1), ("4d", "Y", 39, 4, 2), ("5d", "La", 57, 5, 2),
            ("5f", "Pa", 91, 5, 3)]

# --------------------------------------------------------------------- the sealed rows
# (Z, channel, D in Ha, quote).  Every one is the chain's D for that channel at that Z:
# E_HF(cation config(Z-1) + channel) - E_HF(cation config(Z-1)), scalar-relativistic.
SEALED = [
    (31, "4p", -0.20007,  "recovered/FINDING-CHAIN-4p.md:6, :20"),
    (49, "5p", -0.18833,  "recovered/FINDING-CHAIN-5p.md:6"),
    (39, "4d", -0.195614, "recovered/BRIDGE-LOWDIN-SESSION-42.md:38; FINDING-CHAIN-4d.md:43; PREDICTION-CHAIN-4d.md:6"),
    (57, "5d", -0.20585,  "recovered/PREDICTION-4fBLOCK-61-71.md:20, :33; DELIVERABLE-4-THE-TRANSIT-WIDTH.md:18, :35"),
    (57, "4f", -0.10556,  "recovered/DELIVERABLE-4-THE-TRANSIT-WIDTH.md:35; DELIVERABLE-3-COLLAPSE-CONDITION.md s3"),
    (58, "4f", -0.36700,  "recovered/PREDICTION-4fBLOCK-61-71.md:23, :34; DELIVERABLE-4:36; SCORE-TIEBREAK-CONTROLS.md:26"),
    (89, "6d", -0.15762,  "recovered/DELIVERABLE-4-THE-TRANSIT-WIDTH.md:37; PREDICTION-Z90CONFIRM.md:9"),
    (89, "5f", -0.03146,  "recovered/DELIVERABLE-4-THE-TRANSIT-WIDTH.md:37; DELIVERABLE-3 s3"),
    (90, "6d", -0.19094,  "recovered/PREDICTION-S81-ITEM1-Z90FIXED.md:6; DELIVERABLE-4:38; fixed81.py docstring"),
    (90, "5f", -0.13689,  "recovered/PREDICTION-S81-ITEM1-Z90FIXED.md:6; DELIVERABLE-4:38; BRIDGE-LOWDIN-SESSION-49.md:34"),
    (91, "5f", -0.30535,  "recovered/BRIDGE-LOWDIN-SESSION-55.md:71; SCORE-TIEBREAK-CONTROLS.md:28; PREDICTION-Z90CONFIRM.md:9; "
                          "DELIVERABLE-4:39; DELIVERABLE-3-COLLAPSE-CONDITION.md:49; BRIDGE-LOWDIN-SESSION-49.md:34"),
    (91, "6d", -0.22340,  "recovered/DELIVERABLE-4-THE-TRANSIT-WIDTH.md:39; BRIDGE-LOWDIN-SESSION-55.md:71"),
]
SEALED_NR = {(91, "5f"): -0.59532, (91, "6d"): -0.29923}   # c = 1e6, BRIDGE-LOWDIN-SESSION-55.md:71
# DELIVERABLE-3-COLLAPSE-CONDITION.md s3, the Z = 91 row: D(5f) -0.30535, n* 1.2796, delta 3.7204.
DELIV3_PA = (1.2796, 3.7204)

# The record's machinery gates, value for value.
PC0 = {(11, "3s"): -0.18217, (19, "4s"): -0.14774, (19, "3d"): -0.05807, (19, "4p"): -0.09363}  # FINDING-CHAIN-SESSION-40 s2
G1_HE = -0.91796            # t7c_hfsr G1: He 1s at c = 1e6 (Fischer 1977, the T7b gate A)
DIRAC_H1S = -0.5000067      # t7c_kernel gate (ii)
DIRAC_Z70 = -2634.8465      # t7c_kernel's own Z = 70 hydrogenic check

# Thallium's 6p fine structure and series limit, from the corpus's own spectra store (NIST ASD, fetched by the
# spectra work): extracted/archives/spectra-levels-store/deliver/queue2/TlI.tsv lines 13-14 (6s2.6p 2P* 1/2 at 0.0,
# 3/2 at 7792.7 cm^-1) and deliver/MEASUREMENTS.tsv (Z=81 limit 49266.66 cm^-1, Tl II 6s2 1S0).
TL_LIMIT_CM = 49266.66; TL_6P32_CM = 7792.7; CM_PER_EV = 8065.543937


def t_form(l):
    return math.sqrt(l * (l + 1) / 2)


def nu_from_D(D):
    """n* = 1/sqrt(-2D) for D in Hartree -- the same as sqrt(R/IE) with IE = -D."""
    return 1.0 / math.sqrt(-2.0 * D)


# ----------------------------------------------------------------- entrypoint.py by path
def load_entrypoint():
    p = os.path.join(HERE, "entrypoint.py")
    spec = importlib.util.spec_from_file_location("entrypoint", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ------------------------------------------------------------------ the chain, by path
SHOOT14_HEAD = ("void shoot_x14(int n, double h, const double *f, const double *s, int m, int ie, "
                "double y0, double y1, double y0p, double y1p,")
SHOOT_HEAD = ("void shoot_x(int n, double h, const double *f, const double *s, int m, int ie, "
              "double y0, double y1,")
ADIABATIC = ("    { double q0 = 12.0*(1.0-f[ie])/(h*h), q1 = 12.0*(1.0-f[ie-1])/(h*h);\n"
             "      yip[ie]   = (q0 > 1e-12) ? -s[ie]/q0 : 0.0;\n"
             "      yip[ie-1] = (q1 > 1e-12) ? -s[ie-1]/q1 : 0.0; }")
SEEDED = "    yip[ie] = y0p; yip[ie-1] = y1p;   /* RECONSTRUCTED: caller-supplied inward particular start */"

# (c) the outward Numerov the bisections ride, in C for the speed the sealed runtime had from shoot.c.
SHOOT_LIM_C = r"""
/* shoot_lim -- RECONSTRUCTED (fieldentry.py, departure (c)).  The outward Numerov every bisection uses, on the
   log mesh y'' = q y, y[0] = 1e-30, y[1] = y[0] e^{(l+1/2)h}; f = 1 - h^2 q/12 as rad._shoot; STOPS at the first
   point where |y| > 1e150 and counts nodes only up to it.  Returns the stop index. */
#include <math.h>
int shoot_lim(int n, double h, const double *q, int l, double *y, int *nodes)
{
    int i, last = 1; double h2 = h*h/12.0, f0, f1, f2;
    for (i = 0; i < n; i++) y[i] = 0.0;
    y[0] = 1e-30; y[1] = y[0]*exp((l+0.5)*h); *nodes = 0;
    for (i = 1; i < n-1; i++) {
        f0 = 1.0 - h2*q[i-1]; f1 = 1.0 - h2*q[i]; f2 = 1.0 - h2*q[i+1];
        y[i+1] = ((12.0 - 10.0*f1)*y[i] - f0*y[i-1]) / f2;
        if (y[i+1]*y[i] < 0) (*nodes)++;
        last = i+1;
        if (fabs(y[i+1]) > 1e150) break;
    }
    return last;
}
"""


def _once(src, old, new, what):
    if src.count(old) != 1:
        raise RuntimeError(f"{what}: expected exactly one site to patch, found {src.count(old)}")
    return src.replace(old, new)


def build_so(workdir):
    src = open(os.path.join(RECOVERED, "shoot_x.c")).read()
    s14 = _once(src, SHOOT_HEAD, SHOOT14_HEAD, "shoot_x.c signature")
    s14 = _once(s14, ADIABATIC, SEEDED, "shoot_x.c inward particular start")
    both = src + "\n" + s14[s14.index("void shoot_x14"):] + "\n" + SHOOT_LIM_C
    cpath = os.path.join(workdir, "shoot_x_both.c")
    open(cpath, "w").write(both)
    so = os.path.join(workdir, "libshoot_x.so")
    subprocess.run(["gcc", "-O2", "-shared", "-fPIC", "-o", so, cpath, "-lm"], check=True)
    return so


def _load(name, path, patch=None, quiet=True):
    src = open(path).read()
    if patch:
        src = patch(src)
    mod = types.ModuleType(name)
    mod.__file__ = path
    sys.modules[name] = mod
    code = compile(src, path, "exec")
    if quiet:
        with contextlib.redirect_stdout(io.StringIO()):
            exec(code, mod.__dict__)
    else:
        exec(code, mod.__dict__)
    return mod


def _patch_hfsr(src):
    src = _once(src, "from t7b_hf import HF, _lib, _D, L\n",
                "from t7b_hf import HF, _lib, _D, L\n"
                "import ctypes as _ct; _lib.shoot_x14.argtypes = [_ct.c_int, _ct.c_double, _D, _D, _ct.c_int, _ct.c_int, "
                "_ct.c_double, _ct.c_double, _ct.c_double, _ct.c_double, _D, _D, _D, _D]\n",
                "t7c_hfsr argtypes")
    return _once(src, "_lib.shoot_x(N,h,f.ctypes", "_lib.shoot_x14(N,h,f.ctypes", "t7c_hfsr shoot call")


def _patch_nlchain(src):
    return _once(src, "Eref, _, itref, _ = H.HFC(Z - 1, [tuple(t) for t in cfg_prev], c=C0).run2()",
                 "Eref, _, itref, _ = H.HFC(Z, [tuple(t) for t in cfg_prev], c=C0).run2()  # F40.1",
                 "nlchain reference")


def _shoot_limited(np, so):
    import ctypes
    lib = ctypes.CDLL(so); D = ctypes.POINTER(ctypes.c_double)
    lib.shoot_lim.argtypes = [ctypes.c_int, ctypes.c_double, D, ctypes.c_int, D, ctypes.POINTER(ctypes.c_int)]
    lib.shoot_lim.restype = ctypes.c_int
    def _shoot(q, h, l):
        q = np.ascontiguousarray(q, dtype=float); n = len(q); y = np.zeros(n); nodes = ctypes.c_int(0)
        last = lib.shoot_lim(n, float(h), q.ctypes.data_as(D), int(l), y.ctypes.data_as(D), ctypes.byref(nodes))
        if last < n - 1:
            y[-1] = y[last]
        return y, nodes.value
    return _shoot


def _numerov_wf_cleaned(np, eigen):
    """recovered derive_P.numerov_wf, verbatim, plus the tail clean of t7c_kernel.numerov_wf_sr."""
    def numerov_wf(V, l, n, zeta, Z, npts=3000):
        E = eigen(V, l, n, zeta, Z, npts=npts)
        rmin, rmax = 1e-5 / Z, max(80.0, 4.0 * n * n / zeta)
        x = np.linspace(np.log(rmin), np.log(rmax), npts); h = x[1] - x[0]; r = np.exp(x)
        q = (l + 0.5) ** 2 + 2 * r * r * (V(r) - E); f = 1 - h * h * q / 12.0
        allowed = np.where(q < 0)[0]
        m = allowed[-1] if len(allowed) else npts // 2
        yo = np.zeros(npts); yo[0] = 1e-30; yo[1] = yo[0] * np.exp((l + 0.5) * h)
        for i in range(1, m + 1):
            yo[i + 1] = ((12 - 10 * f[i]) * yo[i] - f[i - 1] * yo[i - 1]) / f[i + 1]
            if abs(yo[i + 1]) > 1e100: yo[:i + 2] /= 1e100
        yi = np.zeros(npts); yi[-1] = 1e-30; yi[-2] = yi[-1] * np.exp(np.sqrt(max(q[-1], 1e-12)) * h)
        for i in range(npts - 2, m, -1):
            yi[i - 1] = ((12 - 10 * f[i]) * yi[i] - f[i + 1] * yi[i + 1]) / f[i - 1]
            if abs(yi[i - 1]) > 1e100: yi[i - 1:] /= 1e100
        y = np.concatenate([yo[:m + 1], yi[m + 1:] * (yo[m] / yi[m])]) if yi[m] != 0 else yo
        u = np.exp(x / 2) * y
        dr = r * h
        a = np.abs(u); mm = int(np.argmax(a)); thr = 1e-9 * a[mm]
        tail = np.where(a[mm:] < thr)[0]
        if len(tail): u[mm + tail[0]:] = 0.0
        u /= np.sqrt(np.sum(u * u * dr))
        sg = np.sign(u); sg = sg[sg != 0]; nodes = int(np.sum(sg[1:] != sg[:-1]))
        return r, dr, u, E, nodes
    return numerov_wf


class Chain:
    """The sealed chain's producer, loaded from recovered/ by path into a temporary working
    directory (the C shoot, derive_P.json and nlchain.jsonl live there and nowhere else)."""

    def __init__(self, workdir=None, log=sys.stderr):
        import numpy as np
        self.np = np
        self.workdir = workdir or tempfile.mkdtemp(prefix="fieldentry-")
        self.log = log
        os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
        self.cwd0 = os.getcwd()
        os.chdir(self.workdir)
        so = build_so(self.workdir)
        R = lambda f: os.path.join(RECOVERED, f)
        self.tfd = _load("tfd", R("tfd.py"))
        self.rad = _load("rad", R("rad.py"))
        self.step2_run = _load("step2_run", R("step2_run.py"))
        self.eigen_fix = _load("eigen_fix", R("eigen_fix.py"))
        # (c) the range-limited shoot, before any bisection is built on it
        sh = _shoot_limited(np, so)
        for m in (self.rad, self.step2_run, self.eigen_fix):
            m._shoot = sh
        self.derive_P = _load("derive_P", R("derive_P.py"))
        self.ground = _load("ground", os.path.join(MEMBERS, "LW1-ground.py"))
        self.hfs = _load("hfs", R("hfs.py"))
        # (d) the tail-cleaned seed orbital
        nw = _numerov_wf_cleaned(np, self.eigen_fix.eigen)
        for m in (self.derive_P, self.hfs):
            m.numerov_wf = nw
        self.t5_scf = _load("t5_scf", R("t5_scf.py")); self.t5_scf.numerov_wf = nw
        self.t7b_hf = _load("t7b_hf", R("t7b_hf.py")); self.t7b_hf.numerov_wf = nw
        self.t7c_kernel = _load("t7c_kernel", R("t7c_kernel.py")); self.t7c_kernel._shoot = sh
        stub = types.ModuleType("t7c_cuaudit")
        def _absent(*a, **k):
            raise RuntimeError("t7c_cuaudit is absent from the repository; the chain runs with CORR=False")
        stub.v_gbz = stub._e0a = stub._lam0 = stub._lam1 = _absent; stub.E0B = 0.0; stub.LAM1 = False
        sys.modules["t7c_cuaudit"] = stub
        self.t7c_hfsr = _load("t7c_hfsr", R("t7c_hfsr.py"), patch=_patch_hfsr)      # (b)
        self.hfc2 = _load("hfc2", R("hfc2.py"))
        self.hfc2.CORR = False
        self.nlchain = _load("nlchain", R("nlchain.py"), patch=_patch_nlchain)       # (a)
        self.C0 = self.t7c_kernel.C0

    def close(self):
        os.chdir(self.cwd0)

    # ---- one delta-SCF removal from the observed ground configuration:
    #      D = E_HF(ground) - E_HF(ground minus one entrant electron) = -(removal energy), the chain's own sign
    def dscf(self, Z, n, l):
        H = self.hfc2; T = self.t5_scf
        occ0 = T.ground_occ(Z)
        occ1 = [(a, b, q) for a, b, q in T.minus(occ0, n, l, 1.0) if q > 0]
        E0, _, it0, e0 = H.HFC(Z, occ0, c=self.C0).run2()
        E1, _, it1, e1 = H.HFC(Z, occ1, c=self.C0).run2()
        return dict(Z=Z, nl=f"{n}{'spdfg'[l]}", how="dscf-observed-ground",
                    cfg="".join(f"{a}{'spdfg'[b]}{int(q)}" for a, b, q in occ0),
                    D=round(E0 - E1, 5), E0=round(E0, 5), E1=round(E1, 5),   # the chain's sign: bound is negative
                    eps=round(float(e0[(n, l)]), 6), it=[it0, it1])

    # ---- one chain step from the observed config(Z-1): every admissible channel's D
    def step(self, Z):
        G = self.ground
        with contextlib.redirect_stdout(self.log):
            o = self.nlchain.step(Z, G.expand(Z - 1), {}, "restart")
        return dict(Z=Z, how="chain-step-from-observed", ref_cfg=o["ref_cfg"], ent=o["ent"],
                    D_ent=o["D_ent"], margin=o["margin"], order=o["order"], nfail=o["nfail"], fail=o["fail"])


# ------------------------------------------------------------------------- --field
def cmd_field(args):
    """Every target is run under its own try; a failure is recorded as a row with an `err` field, never
    silently dropped, and the file is rewritten after each target so a long run can be read as it goes."""
    ch = Chain(log=sys.stderr)
    out = {"dscf": [], "steps": []}
    def save():
        json.dump(out, open(FIELD_JSON, "w"), indent=1)
    try:
        targets = [(lab, el, Z, n, l) for lab, el, Z, n, l in OPENINGS] + [("4f", "Ce", 58, 4, 3)]
        for lab, el, Z, n, l in targets:
            print(f"  dscf Z={Z} {lab} ...", file=sys.stderr, flush=True)
            try:
                r = ch.dscf(Z, n, l)
            except Exception as ex:
                r = dict(Z=Z, nl=lab, how="dscf-observed-ground", err=f"{type(ex).__name__}: {str(ex)[:160]}")
            r["el"] = el; out["dscf"].append(r); save()
            print(f"    D = {r.get('D', r.get('err'))}", file=sys.stderr, flush=True)
        for Z in (11, 19, 91):
            print(f"  chain step Z={Z} ...", file=sys.stderr, flush=True)
            try:
                o = ch.step(Z)
            except Exception as ex:
                o = dict(Z=Z, how="chain-step-from-observed", err=f"{type(ex).__name__}: {str(ex)[:160]}", order=[])
            out["steps"].append(o); save()
            print(f"    entrant {o.get('ent')} D {o.get('D_ent', o.get('err'))}", file=sys.stderr, flush=True)
    finally:
        ch.close()
    save()
    print(f"wrote {FIELD_JSON}")


# ------------------------------------------------------------------------- the report
def field():
    if not os.path.exists(FIELD_JSON):
        return None
    return json.load(open(FIELD_JSON))


def comparable(r):
    """A delta-SCF row from the observed ground is the chain's row only when the entrant shell holds one electron
    there, so that ground(Z) = config(Z-1) + channel.  True at every opening but protactinium (5f2)."""
    import re
    # cfg is the concatenation of n-letter-q tokens with no separator ("...4d15s2" is 4d1 then 5s2): a token's
    # occupancy ends where the next token's digit-and-letter begins, or at the end of the string.
    occ = {(int(a), "spdfg".index(b)): int(q) for a, b, q in re.findall(r"(\d)([spdfg])(\d{1,2})(?=\d[spdfg]|$)", r["cfg"])}
    n, l = int(r["nl"][0]), "spdfg".index(r["nl"][1])
    return occ.get((n, l)) == 1


def sealed_at(Z, nl):
    for z, c, D, q in SEALED:
        if z == Z and c == nl:
            return D
    return None


def report():
    ep = load_entrypoint()
    F = field()
    print("  THE ENTRY POINT READ WITH THE ENTRANT'S OWN ELECTRON, ON THE CORPUS'S OWN FIELD\n")
    print("  a_meas = (n - nu)/sqrt(p),  nu = sqrt(R/IE) = 1/sqrt(-2D),  t = (a - L)/(U - L),  form sqrt(l(l+1)/2)\n")

    print("  1. THE SEALED FIELD ROWS THE RECORD QUOTES  (scalar-relativistic HF, cation reference; D in Ha)")
    print("     Z   ch         D        eV      n*    quoted at")
    for Z, nl, D, q in SEALED:
        print(f"    {Z:>2}   {nl}   {D:9.5f}  {-D*HA_EV:7.3f}  {nu_from_D(D):6.4f}  {q}")
    ns, de = nu_from_D(-0.30535), 5 - nu_from_D(-0.30535)
    print(f"\n     DELIVERABLE-3 s3 at Z = 91: n* = {ns:.4f}, delta = {de:.4f}; the record prints {DELIV3_PA[0]}, {DELIV3_PA[1]}."
          f"  delta IS a_meas for 5f (p = 1).")
    print(f"     Non-relativistic (c = 1e6) at Z = 91: 5f {SEALED_NR[(91,'5f')]}, 6d {SEALED_NR[(91,'6d')]}.")
    print("     3p at Z = 13 and 6p at Z = 81: NOT QUOTED anywhere in the record.\n")

    print("  2. THE FIELD REGENERATED HERE  (MEASURED by --field from recovered/ by path; LW1-ground.py configurations)")
    if F is None:
        print("     fieldentry-field.json is absent: run  python3 fieldentry.py --field\n")
    else:
        print("     Z   el  ch   configuration              D here      sealed     diff      eps(entrant)")
        for r in F["dscf"]:
            if "err" in r:
                print(f"    {r['Z']:>2}   {r['el']:<2}  {r['nl']}   FAILED: {r['err']}"); continue
            s = sealed_at(r["Z"], r["nl"])
            if s is not None and not comparable(r):
                sd = f"{s:9.5f}  (other config)"
            elif s is not None:
                sd = f"{s:9.5f}  {r['D']-s:+8.5f}"
            else:
                sd = "  not quoted        "
            print(f"    {r['Z']:>2}   {r['el']:<2}  {r['nl']}   {r['cfg']:<24} {r['D']:9.5f}  {sd}  {r['eps']:10.6f}")
        print("     (other config): the sealed row is the chain's step, config(Z-1) + channel; protactinium's observed ground is")
        print("     5f2 6d1 7s2, not the chain's 5f1 6d2 7s2, so the two 5f numbers at Z = 91 are different quantities -- see 3.")
        print("\n     the chain's own step, every admissible channel (reference = cation of Z with the observed config(Z-1)):")
        for s in F["steps"]:
            if "err" in s:
                print(f"    Z={s['Z']:>2}  FAILED: {s['err']}"); continue
            top = "  ".join(f"{k} {v:.5f}" for k, v in s["order"][:5])
            print(f"    Z={s['Z']:>2}  ref {s['ref_cfg']}  entrant {s['ent']} D {s['D_ent']}  margin {s['margin']}  |  {top}")
            for k, v in s["order"]:
                key = (s["Z"], k)
                if key in PC0:
                    print(f"          PC-0 gate {s['Z']} {k}: here {v:.5f}  record {PC0[key]:.5f}  diff {v-PC0[key]:+.5f}")
                sv = sealed_at(s["Z"], k)
                if sv is not None:
                    print(f"          sealed    {s['Z']} {k}: here {v:.5f}  record {sv:.5f}  diff {v-sv:+.5f}")
        print()

    print("  3. THE ENTRY POINT, TWO READINGS AT EVERY TWO-SIDED OPENING")
    print("     first IE = register 1337's reading (the atom's first ionisation energy, whatever electron leaves);")
    print("     entrant  = the entrant's own removal energy on the field, sealed where the record quotes it, here otherwise.")
    print("     op  el   Z  p     L        U    |  first IE    nu    a_meas      t    t/form |  D entrant   nu    a_meas      t    t/form")
    rows = []
    for lab, el, Z, n, l in OPENINGS:
        _, _, _, _, lo, hi = ep.CORRIDOR[lab]
        p = n - l - 1
        ie = ep.IE[el]; nu1 = math.sqrt(ep.R_EV / ie); a1 = (n - nu1) / math.sqrt(p); t1 = (a1 - lo) / (hi - lo)
        D = sealed_at(Z, lab); src = "sealed"
        if F is not None:
            for r in F["dscf"]:
                if r["Z"] == Z and r["nl"] == lab and D is None and "D" in r:
                    D = r["D"]; src = "here"
        if D is None:
            print(f"     {lab}  {el:<2} {Z:>3}  {p}  {lo:6.4f}  {hi:6.4f}  |  {ie:7.4f}  {nu1:6.4f}  {a1:7.4f}  {t1:6.4f}  {t1/t_form(l):6.4f} |  (no field value: run --field)")
            continue
        nu2 = nu_from_D(D); a2 = (n - nu2) / math.sqrt(p); t2 = (a2 - lo) / (hi - lo)
        rows.append((lab, el, Z, n, l, t1, t2, src, D))
        print(f"     {lab}  {el:<2} {Z:>3}  {p}  {lo:6.4f}  {hi:6.4f}  |  {ie:7.4f}  {nu1:6.4f}  {a1:7.4f}  {t1:6.4f}  {t1/t_form(l):6.4f} |"
              f"  {D:9.5f}  {nu2:6.4f}  {a2:7.4f}  {t2:6.4f}  {t2/t_form(l):6.4f}  ({src})")
    if rows:
        print("\n     by l, the mean of t/form:")
        for l, name in ((1, "p"), (2, "d"), (3, "f")):
            sel = [r for r in rows if r[4] == l]
            if not sel: continue
            m1 = sum(r[5] for r in sel) / len(sel) / t_form(l); m2 = sum(r[6] for r in sel) / len(sel) / t_form(l)
            print(f"       {name}: first IE {m1:6.4f} ({(m1-1)*100:+5.2f} %)   entrant {m2:6.4f} ({(m2-1)*100:+5.2f} %)   on {len(sel)} opening(s)")
        print("\n     the p row along n (s34.7 reads t as a limit approached along n):")
        for r in rows:
            if r[4] == 1:
                print(f"       {r[0]}  first IE {r[5]:6.4f}   entrant {r[6]:6.4f}")
        fr = [r for r in rows if r[4] == 3]
        if fr:
            r = fr[0]
            nr = SEALED_NR[(91, "5f")]; nun = nu_from_D(nr); an = 5 - nun; tn = (an - ep.CORRIDOR["5f"][4]) / (ep.CORRIDOR["5f"][5] - ep.CORRIDOR["5f"][4])
            print(f"\n     the f point: first IE t = {r[5]:.4f} ({(r[5]/t_form(3)-1)*100:+.1f} %); the 5f electron's own binding t = {r[6]:.4f}"
                  f" ({(r[6]/t_form(3)-1)*100:+.1f} %); non-relativistic field t = {tn:.4f} ({(tn/t_form(3)-1)*100:+.1f} %); form sqrt(6) = {t_form(3):.4f}")
            if F is not None:
                for q in F["dscf"]:
                    if q["Z"] == 91 and q["nl"] == "5f" and "D" in q:
                        nug = nu_from_D(q["D"]); ag = 5 - nug; tg = (ag - ep.CORRIDOR["5f"][4]) / (ep.CORRIDOR["5f"][5] - ep.CORRIDOR["5f"][4])
                        print(f"     the 5f removal from protactinium's OBSERVED ground {q['cfg'][-12:]}: D = {q['D']} Ha, t = {tg:.4f} ({(tg/t_form(3)-1)*100:+.1f} %)")
                        tq = (ag / math.sqrt(1 + 1 / 14) - ep.CORRIDOR["5f"][4]) / (ep.CORRIDOR["5f"][5] - ep.CORRIDOR["5f"][4])
                        print(f"       the same removal under the finished form (one 5f already present, radicand 1 + 1/14): t = {tq:.4f} ({(tq/t_form(3)-1)*100:+.1f} %)")
        # the spin-orbit share of the field's shortfall at 6p, from the corpus's own thallium levels
        jav_cm = TL_LIMIT_CM - (2.0 / 3.0) * TL_6P32_CM; jav_ev = jav_cm / CM_PER_EV
        nuj = math.sqrt(ep.R_EV / jav_ev); aj = (6 - nuj) / 2.0; tj = (aj - ep.CORRIDOR["6p"][4]) / (ep.CORRIDOR["6p"][5] - ep.CORRIDOR["6p"][4])
        print(f"\n     6p at Tl, the spin-orbit share: the corpus's own Tl I levels put 6p 2P3/2 at {TL_6P32_CM} cm^-1 above 2P1/2 and the")
        print(f"     limit at {TL_LIMIT_CM} cm^-1; the j-averaged 6p removal energy is {jav_cm:.1f} cm^-1 = {jav_ev:.4f} eV, t = {tj:.4f};")
        print(f"     first IE 1.0237 -> j-average {tj:.4f} is spin-orbit, j-average -> field 0.9513 is what the field lacks besides.")
    print()


# ------------------------------------------------------------------------- --selftest
def selftest():
    ok = 0; bad = 0
    def check(name, cond, detail=""):
        nonlocal ok, bad
        ok += cond; bad += (not cond)
        print(f"  {'OK  ' if cond else 'FAIL'} {name}  {detail}")
    ep = load_entrypoint()
    # arithmetic on the record's own numbers
    ns = nu_from_D(-0.30535)
    check("DELIVERABLE-3 n*, delta at Z=91 from D=-0.30535", abs(ns - DELIV3_PA[0]) < 5e-5 and abs(5 - ns - DELIV3_PA[1]) < 5e-5, f"{ns:.4f} {5-ns:.4f}")
    for lab, want in ep.REG_1337.items():
        t, a = ep.t_at(lab)
        check(f"register 1337 t at {lab}", abs(t - want) < 5e-5, f"{t:.4f} printed {want}")
    check("first IE f point (R4-13)", abs(ep.t_at("5f")[0] - 2.5476) < 5e-5, f"{ep.t_at('5f')[0]:.4f}")
    # the sealed rows are consistent with one another where two quotes overlap
    check("Z=91 margin 81.95 mHa = 5f - 6d", abs((-0.22340 - -0.30535) - 0.08195) < 1e-9)
    jav_ev = (TL_LIMIT_CM - (2.0 / 3.0) * TL_6P32_CM) / CM_PER_EV
    tj = ((6 - math.sqrt(ep.R_EV / jav_ev)) / 2.0 - ep.CORRIDOR["6p"][4]) / (ep.CORRIDOR["6p"][5] - ep.CORRIDOR["6p"][4])
    check("Tl 6p j-averaged reading from the corpus's own levels", abs(tj - 0.9888) < 5e-5, f"{tj:.4f}")
    # the field file, if present
    F = field()
    if F is None:
        print("  SKIP fieldentry-field.json absent: the regenerated rows are not checked (run --field)")
    else:
        for r in F["dscf"]:
            if "err" in r:
                check(f"regenerated {r['Z']} {r['nl']} ran", False, r["err"]); continue
            s = sealed_at(r["Z"], r["nl"])
            if s is not None and comparable(r):
                check(f"regenerated {r['Z']} {r['nl']} vs sealed", abs(r["D"] - s) <= 1.5e-5, f"{r['D']} vs {s}")
            elif s is not None:
                print(f"  SKIP regenerated {r['Z']} {r['nl']} is the observed-ground removal ({r['cfg'][-12:]}), not the chain's row; the chain's row is checked below")
            if r["Z"] == 91 and r["nl"] == "5f":
                tg = (5 - nu_from_D(r["D"]) - ep.CORRIDOR["5f"][4]) / (ep.CORRIDOR["5f"][5] - ep.CORRIDOR["5f"][4])
                check("Pa observed-ground 5f removal reads t = 2.4420", abs(tg - 2.4420) < 5e-5, f"D {r['D']} t {tg:.4f} form {t_form(3):.4f}")
        for lab, Z in (("3p", 13), ("6p", 81)):
            got = [r for r in F["dscf"] if r["Z"] == Z and "D" in r]
            check(f"{lab} at Z={Z} measured (quoted nowhere in the record)", bool(got), f"D {got[0]['D'] if got else None}")
        for s in F["steps"]:
            if "err" in s:
                check(f"chain step {s['Z']} ran", False, s["err"]); continue
            for k, v in s["order"]:
                if (s["Z"], k) in PC0:
                    check(f"PC-0 {s['Z']} {k}", abs(v - PC0[(s['Z'], k)]) <= 1.5e-5, f"{v} vs {PC0[(s['Z'], k)]}")
                sv = sealed_at(s["Z"], k)
                if sv is not None:
                    check(f"chain step {s['Z']} {k} vs sealed", abs(v - sv) <= 1.5e-5, f"{v} vs {sv}")
    # the machinery, if it can be built here
    if shutil.which("gcc") is None or importlib.util.find_spec("numpy") is None or importlib.util.find_spec("scipy") is None:
        print("  SKIP machinery gates: gcc, numpy and scipy are all needed")
    else:
        ch = Chain(log=io.StringIO())
        try:
            np = ch.np
            Vh = lambda r: -1.0 / np.asarray(r, float)
            d = max(abs(ch.rad.defect(Vh, l, n, 1.0, 1)[0]) for l, n in ((0, 1), (0, 2), (1, 2), (2, 3)))
            check("hydrogen defects vanish with the range-limited shoot", d < 1e-6, f"max |delta| {d:.1e}")
            e = ch.t7c_kernel.eigen_sr(Vh, 0, 1, 1.0, 1)
            check("kernel gate: H 1s scalar-relativistic on Dirac", abs(e - DIRAC_H1S) < 1e-5, f"{e:.7f} vs {DIRAC_H1S}")
            Vz = lambda r: -70.0 / np.asarray(r, float)
            e = ch.t7c_kernel.eigen_sr(Vz, 0, 1, 1.0, 70)
            check("kernel gate: Z=70 1s on Dirac", abs(e - DIRAC_Z70) < 0.01, f"{e:.4f} vs {DIRAC_Z70}")
            for Z in (13, 91):
                try:
                    Vf, Es, E, it = ch.t5_scf.scf_occ(Z, ch.t5_scf.ground_occ(Z), 1); good = True
                except Exception as ex:
                    good = False; E = float("nan")
                check(f"TFD seed node-clean at Z={Z}", good, f"E {E:.3f}")
            h = ch.t7c_hfsr.HFSR(2, ch.t5_scf.ground_occ(2), c=1e6); eps, E, it, _ = h.run("hf", qtail=1)
            check("G1: He 1s at c=1e6 (14-argument shoot)", abs(eps[(1, 0)] - G1_HE) < 5e-6, f"{eps[(1,0)]:.5f} vs {G1_HE}")
        finally:
            ch.close()
    print(f"\n  {ok} passed, {bad} failed")
    return bad == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--field", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    if a.field:
        cmd_field(a); return
    report()


if __name__ == "__main__":
    main()
