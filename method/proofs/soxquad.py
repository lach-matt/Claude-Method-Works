#!/usr/bin/env python3
"""soxquad.py -- RULING 8(a): THE SECOND-ORDER-EXCHANGE QUADRATURE, REPAIRED, CONVERGED AND PROVEN.

  M's ruling 8 (RULINGS-R4f): the three limits FINDING-R4-15 recorded are not recorded and left -- "they are all
  work.  they must be repaired, worked, and then verified/proven completely."  The first is (a):

    "the g_2b quadrature runs 1.0 % low at the recovered defaults -- converge it."

  THE RECORD ALREADY FOUND THIS FAULT AND ALREADY FIXED IT, and it says so in one sentence:

    FINDING-SOSEX-SESSION-32: "Numerical fault found and fixed BEFORE the table (not a registered fault: caught in
    the convergence study, no result read): a uniform P_perp^2 grid leaves 1/|q+P|^2 unresolved near P_par -> -q;
    a per-column grid uniform in ln(w_q^2 + v) absorbs it exactly (was 1 % low; now 3e-4 converged)."
    BRIDGE-LOWDIN-SESSION-32 repeats it as the session's one numerical note: "Numerical fix before any read:
    P_perp^2 grid -> ln(w_q^2+v) grid (was 1 % low on g_2b)."

  AND THE RECOVERED FILE IS THE SNAPSHOT FROM BEFORE THAT FIX.  `recovered/sox_qres.py` line 35 still reads
  `v=4*(np.arange(NPV)+0.5)/NPV` -- the uniform P_perp^2 grid, the fault named above, verbatim.  So the 1 % is
  not a limit of the record and never was: the record measured it, fixed it, and ran its table on the fixed
  quadrature; what reached this repository through the chat export is the text as it stood before the fix was
  typed in place.  MEASURED here against the record's own sealed golden, the deficit is **-0.725 %**.

  THE ONE DECLARED DEPARTURE.  `rho_q` -- the lens pair density, the whole physical content of the reduction -- is
  the recovered function, called verbatim through the module, never copied and never altered.  What this
  instrument replaces is the six lines of `g2b` that lay down the P grid, and it replaces them with the grid the
  record's own sentence specifies: for each column w_q, a P_perp^2 grid uniform in ln(w_q^2 + v).  The change is
  exact rather than approximate, which is what "absorbs it exactly" means --

      d^3P = pi dw dv  and  v = e^s - w^2  gives  dv = (w^2 + v) ds,
      so   r / ((w^2 + v) (q w)) dv  =  r / (q w) ds,

  and the singular factor is gone from the integrand instead of being resolved by brute force.  The column's upper
  limit is the exact support boundary v_max = 4 - P_par^2 (|P| <= 2, since P = k1 + k2 with both |k| < 1), which
  replaces the recovered text's cell-wise `|P|<=2` mask and is the second half of the same repair.

  FOUR GATES, AND TWO OF THEM THE RECORD DID NOT HAVE:

    (1) THE RECORD'S OWN SEALED GOLDEN.  README-HANDOFF-32 gate (51): "python3 sox_qres.py 1.44881 ... (NZ=80
        NU=80 NPP=64 NPV=128) reprints g2b_Ry 0.0293843".  Nothing here is fitted to it, and the fixed quadrature
        at that exact mesh returns 0.0293844 -- one part in 3e5.  That is the proof that the sentence quoted above
        describes this grid and no other, and it recovers a number the recovered text cannot produce.
    (2) THE BALL AUTOCONVOLUTION, the record's own internal check, run through the recovered `rho_q` unchanged.
    (3) THE ANALYTIC LARGE-q LIMIT, which the record does not state.  For q > 2 the lens L_q is the whole unit
        ball, so int d^3P rho_q = |L|^2 = (4 pi / 3)^2, and |q+P|^2 (q^2 + q.P) -> q^4, giving

            g_2b(q) -> (3/(16 pi^5)) 4 pi (4 pi/3)^2 / q^4 = 4 / (3 pi^2 q^4).

        MEASURED: the ratio to that limit is 1.006 at q = 16.  It fixes the prefactor 3/(16 pi^5) independently of
        E0B -- the record confirmed that prefactor *by* E0B, so this is the first check of it that does not use
        the constant it is later gated on.
    (4) G-S1 AGAINST THE EXACT CONSTANT.  int dq g_2b = E0B = 0.0241792 Ha exactly (Onsager-Mittag-Stephen 1966).
        The record read +1.5e-5 Ha there and called it agreement to 0.06 %.  MEASURED here, that residual is not
        the reduction: it is the (z, rho) lens mesh at the record's own NZ = NU = 80, which carries +0.062 % at
        the peak and converges away.  Converged, the reduction reproduces the 1966 constant to better than it.

  STATUS.  This repairs a reconstruction, not a volume.  Nothing in `recovered/` is touched -- it is a generated
  tree and the pre-fix text is part of what it records.  Every figure printed here is MEASURED by this instrument
  or RECORD-CARRIED with its quote.

  usage:  python3 soxquad.py                 report from the banked files
          python3 soxquad.py --converge      the mesh study, both meshes and the q grid  (~15 min)
          python3 soxquad.py --table         the converged g_2b(q) table, 130 q          (~45 min)
          python3 soxquad.py --selftest      the four gates

  numpy only.
"""
import argparse, importlib.util, json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RECOVERED = os.path.join(ROOT, "recovered")
TABLE_JSON = os.path.join(HERE, "soxquad-table.json")
CONV_JSON = os.path.join(HERE, "soxquad-converge.json")

E0B = 0.0241792                 # bare second-order exchange, Ha (Onsager-Mittag-Stephen 1966; sox_table.py:7)
GS1_RECORD = 0.0241943          # FINDING-SOSEX-SESSION-32's own reading of int g_2b, +1.5e-5 Ha on E0B
GOLD_Q, GOLD_G = 1.44881, 0.0293843          # README-HANDOFF-32 gate (51), at (NZ,NU,NPP,NPV) = (80,80,64,128)
GOLD_MESH = (80, 80, 64, 128)
RECORD_MESH = (160, 160, 96, 96)             # the mesh the pre-fix reconstruction ran at (fieldresidue-tables)
PROD_MESH = (160, 160, 96, 192)              # this instrument's converged production mesh
TAIL = 4.0 / (3.0 * math.pi ** 2)            # g_2b(q) q^4 -> 4/(3 pi^2), derived above


def _load_sox(mesh):
    """recovered/sox_qres.py at a given (NZ, NU, NPP, NPV).  The module reads them from the environment at import,
    so the mesh is set and the module re-executed; nothing in the file is altered."""
    NZ, NU, NPP, NPV = mesh
    os.environ["NZ"], os.environ["NU"] = str(NZ), str(NU)
    os.environ["NPP"], os.environ["NPV"] = str(NPP), str(NPV)
    path = os.path.join(RECOVERED, "sox_qres.py")
    spec = importlib.util.spec_from_file_location("sox_qres", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["sox_qres"] = mod
    spec.loader.exec_module(mod)
    return mod


def g2b_fixed(m, q):
    """g_2b(q) with the record's declared fix: a per-column P_perp^2 grid uniform in ln(w_q^2 + v).

    The recovered text (sox_qres.g2b) is reproduced line for line except for the P_perp^2 grid and the support
    mask it replaces.  m.rho_q -- the lens pair density -- is the recovered function, called unchanged."""
    import numpy as np
    NPP, NPV, PRE = m.NPP, m.NPV, m.PRE
    u = (np.arange(NPP) + 0.5) / NPP; W = 2 + q
    wq = W * u * u; dw = W * 2 * u / NPP                      # recovered: w_q stretched toward 0 by u^2
    Ppar = -q + wq
    vmax = np.maximum(0.0, 4.0 - Ppar ** 2)                   # exact |P| <= 2 support per column
    a = wq * wq
    s0 = np.log(a); s1 = np.log(a + np.maximum(vmax, 1e-300))
    sg = (np.arange(NPV) + 0.5) / NPV
    S = s0[:, None] + (s1 - s0)[:, None] * sg[None, :]        # uniform in ln(w_q^2 + v)
    ds = ((s1 - s0) / NPV)[:, None]
    V = np.maximum(np.exp(S) - a[:, None], 0.0)               # v = P_perp^2
    Pperp = np.sqrt(V); PparG = np.broadcast_to(Ppar[:, None], V.shape)
    r = np.zeros(V.shape)
    msk = np.broadcast_to((vmax > 0)[:, None], V.shape)
    r[msk] = m.rho_q(q, PparG[msk], Pperp[msk])
    # d^3P = pi dw dv and dv = (w^2 + v) ds, so the 1/|q+P|^2 factor cancels identically:
    #   r / ((w^2 + v)(q w)) dv dw pi  ==  r / (q w) ds dw pi
    I = float(np.sum(r / (q * wq[:, None]) * ds * np.broadcast_to(dw[:, None], V.shape)) * np.pi)
    return PRE * 4 * np.pi * I


def int_g2b(Q, G):
    """int dq g_2b(q) [Ry], exactly as sox_table.py:_int reads it -- trapezoid in ln q with the two tails
    (g ~ q below the grid, g ~ q^-4 above)."""
    import numpy as np
    trap = getattr(np, "trapezoid", None) or np.trapz
    Q = np.asarray(Q, float); G = np.asarray(G, float); LQ = np.log(Q)
    return float(trap(G * Q, LQ) + G[0] * Q[0] / 2 + G[-1] * Q[-1] / 3)


def richardson(fs, ns, p=2.0):
    """the h^p limit from the last two rungs of a mesh ladder."""
    if len(fs) < 2: return None
    r = (ns[-1] / ns[-2]) ** p
    return fs[-1] + (fs[-1] - fs[-2]) / (r - 1.0)


# ================================================================== --converge
QS_CONV = [0.05, 0.516, 1.44881, 2.5]


def cmd_converge(log=sys.stderr):
    import numpy as np
    out = {"q": QS_CONV, "lens": [], "pmesh": [], "ladder": [], "qgrid": [], "recovered": {}}
    print("lens mesh (NZ = NU) varied, P mesh held at the recovered (64, 128)", file=log, flush=True)
    for nz in (40, 80, 160, 240):
        m = _load_sox((nz, nz, 64, 128))
        row = {"NZ": nz, "g": [g2b_fixed(m, q) for q in QS_CONV]}
        out["lens"].append(row)
        print(f"  NZ=NU={nz:4d} " + " ".join(f"{v:.7f}" for v in row["g"]), file=log, flush=True)
    print("P mesh varied, lens mesh held at the record's (80, 80)", file=log, flush=True)
    for npp, npv in ((32, 64), (64, 128), (128, 256)):
        m = _load_sox((80, 80, npp, npv))
        row = {"NPP": npp, "NPV": npv, "g": [g2b_fixed(m, q) for q in QS_CONV]}
        out["pmesh"].append(row)
        print(f"  NPP,NPV={npp:4d},{npv:4d} " + " ".join(f"{v:.7f}" for v in row["g"]), file=log, flush=True)
    print("production ladder at the peak, P mesh (96, 192)", file=log, flush=True)
    for nz in (160, 200, 240):
        m = _load_sox((nz, nz, 96, 192))
        g = g2b_fixed(m, GOLD_Q); out["ladder"].append({"NZ": nz, "g": g})
        print(f"  NZ=NU={nz:4d} g_2b({GOLD_Q}) = {g:.7f}", file=log, flush=True)
    print("q-grid and tail, lens mesh held at (60, 60), P mesh (64, 128)", file=log, flush=True)
    m = _load_sox((60, 60, 64, 128))
    for n in (51, 101, 201):
        for lo, hi in ((0.02, 30.0), (0.002, 120.0)):
            qs = sorted(set([round(x, 8) for x in np.exp(np.linspace(np.log(lo), np.log(hi), n))] + [2.0]))
            G = [g2b_fixed(m, q) for q in qs]
            I = int_g2b(qs, G)
            out["qgrid"].append({"n": n, "lo": lo, "hi": hi, "int_Ry": I})
            print(f"  n={n:4d} q in [{lo}, {hi}]: {I/2:.7f} Ha ({(I/2/E0B-1)*100:+.3f} % of E0B)", file=log, flush=True)
    print("the deficit of the recovered text, at the record's own golden mesh", file=log, flush=True)
    m = _load_sox(GOLD_MESH)
    rec, fix = float(m.g2b(GOLD_Q)), g2b_fixed(m, GOLD_Q)
    out["recovered"] = {"mesh": list(GOLD_MESH), "q": GOLD_Q, "recovered_text": rec, "fixed": fix, "record": GOLD_G}
    print(f"  recovered {rec:.7f}  fixed {fix:.7f}  record {GOLD_G}"
          f"  ({(rec/GOLD_G-1)*100:+.3f} % / {(fix/GOLD_G-1)*100:+.3f} %)", file=log, flush=True)
    json.dump(out, open(CONV_JSON, "w"), indent=1)
    print(f"wrote {CONV_JSON}", file=log)
    return out


# ================================================================== --table
def cmd_table(mesh=PROD_MESH, log=sys.stderr):
    """the converged g_2b(q) table on the same 130-point q grid the pre-fix table used, so the quadrature is the
    only thing that changes.  The grid is read from that table rather than regenerated, because it was laid down
    in pieces (0.002 to 120, piecewise geometric) and a regenerated one would not be the same grid."""
    import numpy as np
    src = os.path.join(HERE, "fieldresidue-tables.json")
    if os.path.exists(src):
        qs = sorted(json.load(open(src))["q"])
    else:
        qs = sorted(set([round(x, 8) for x in np.exp(np.linspace(np.log(0.002), np.log(120.0), 129))] + [2.0]))
    m = _load_sox(mesh)
    G = []
    for i, q in enumerate(qs):
        G.append(g2b_fixed(m, q))
        print(f"  {i+1}/{len(qs)} q={q:.5f} g={G[-1]:.7f}", file=log, flush=True)
    I = int_g2b(qs, G)
    out = dict(mesh=list(mesh), q=qs, g2b_Ry=G, int_g2b_Ry=I, int_g2b_Ha=I / 2, E0B=E0B,
               grid="uniform in ln(w_q^2 + v) per column, v_max = 4 - P_par^2 (FINDING-SOSEX-SESSION-32's fix)",
               note="rho_q is recovered/sox_qres.py's own function, called unchanged")
    json.dump(out, open(TABLE_JSON, "w"))
    print(f"wrote {TABLE_JSON}: int g_2b = {I/2:.7f} Ha vs E0B {E0B} ({(I/2/E0B-1)*100:+.3f} %)", file=log)
    return out


# ================================================================== report
def report():
    T = json.load(open(TABLE_JSON)) if os.path.exists(TABLE_JSON) else None
    C = json.load(open(CONV_JSON)) if os.path.exists(CONV_JSON) else None
    print("=" * 108)
    print("soxquad.py -- RULING 8(a): THE SECOND-ORDER-EXCHANGE QUADRATURE, REPAIRED AND CONVERGED")
    print("=" * 108)
    print("""
  RULING 8(a) (RULINGS-R4f, M): "the g_2b quadrature runs 1.0 % low at the recovered defaults -- converge it",
  under "they are all work.  they must be repaired, worked, and then verified/proven completely."

  THE FAULT IS THE RECORD'S OWN, ALREADY FOUND AND ALREADY FIXED -- and the recovered text predates the fix:
    FINDING-SOSEX-SESSION-32: "a uniform P_perp^2 grid leaves 1/|q+P|^2 unresolved near P_par -> -q; a per-column
    grid uniform in ln(w_q^2 + v) absorbs it exactly (was 1 % low; now 3e-4 converged)."
  recovered/sox_qres.py:35 still lays down the uniform grid.  The fix is implemented here from that sentence.
""")
    if C:
        r = C.get("recovered", {})
        print("  1. THE DEFICIT, MEASURED AT THE RECORD'S OWN SEALED GOLDEN")
        print(f"     gate (51), q = {r['q']} at mesh {tuple(r['mesh'])}:")
        print(f"       recovered text (uniform P_perp^2)   {r['recovered_text']:.7f}   {(r['recovered_text']/r['record']-1)*100:+.3f} %")
        print(f"       the record's fix (ln(w^2 + v))      {r['fixed']:.7f}   {(r['fixed']/r['record']-1)*100:+.3f} %")
        print(f"       the record's banked value           {r['record']:.7f}")
        print("     Nothing here is fitted to that number.  The fix recovers it to one part in 3e5 at the")
        print("     record's own mesh, which is what identifies the grid the record's sentence describes.\n")
        print("  2. CONVERGENCE, THE TWO MESHES SEPARATED (g_2b at q = 0.05, 0.516, 1.44881, 2.5)")
        for row in C["lens"]:
            print(f"     lens NZ=NU={row['NZ']:4d}  " + "  ".join(f"{v:.7f}" for v in row["g"]))
        for row in C["pmesh"]:
            print(f"     P  {row['NPP']:4d},{row['NPV']:4d}  " + "  ".join(f"{v:.7f}" for v in row["g"]))
        print("     The lens mesh carries the residual; the P mesh is converged by (64, 128).")
        if C.get("ladder"):
            fs = [x["g"] for x in C["ladder"]]; ns = [x["NZ"] for x in C["ladder"]]
            lim = richardson(fs, ns)
            print(f"\n     the ladder at the peak, P mesh (96, 192):  " + "  ".join(f"NZ {n}: {f:.7f}" for n, f in zip(ns, fs)))
            print(f"     h^2 limit {lim:.7f};  the record's own NZ = 80 sits {(C['lens'][1]['g'][2]/lim-1)*100:+.3f} % above it,")
            print(f"     and the production mesh {PROD_MESH} sits {(fs[0]/lim-1)*100:+.3f} %.")
            print("     SO THE RECORD'S +1.5e-5 Ha ON G-S1 IS THIS MESH, NOT THE REDUCTION.")
        if C.get("qgrid"):
            print("\n  3. THE q GRID AND THE TWO TAILS (lens mesh held coarse, so the q error is read alone)")
            for x in C["qgrid"]:
                print(f"     n={x['n']:4d} q in [{x['lo']}, {x['hi']}]: {x['int_Ry']/2:.7f} Ha  ({(x['int_Ry']/2/E0B-1)*100:+.3f} % of E0B)")
    else:
        print("  (run --converge for the mesh study)")
    if T:
        print(f"\n  4. THE CONVERGED TABLE  ({len(T['q'])} q from {T['q'][0]} to {T['q'][-1]}, mesh {tuple(T['mesh'])})")
        print(f"     G-S1:  int dq g_2b = {T['int_g2b_Ha']:.7f} Ha")
        print(f"            exact E0B  = {E0B} Ha   (Onsager-Mittag-Stephen 1966)   {(T['int_g2b_Ha']/E0B-1)*100:+.3f} %")
        print(f"            the record's own reading {GS1_RECORD} Ha  ({(GS1_RECORD/E0B-1)*100:+.3f} %)")
        print("     The reduction reproduces the 1966 constant more closely than the record's own gate did,")
        print("     and it is the same reduction -- only the quadrature moved.")
        import numpy as np
        Q = np.array(T["q"]); G = np.array(T["g2b_Ry"])
        for q in (8.0, 16.0, 32.0):
            i = int(np.argmin(abs(Q - q)))
            print(f"     tail: q = {Q[i]:7.3f}  g_2b q^4 = {G[i]*Q[i]**4:.6f}  vs 4/(3 pi^2) = {TAIL:.6f}"
                  f"   ratio {G[i]*Q[i]**4/TAIL:.4f}")
    else:
        print("\n  (run --table for the converged table)")
    print("\n  Nothing is repaired in any volume; nothing in recovered/ is touched.")
    print("=" * 108)


# ================================================================== selftest
def selftest():
    ok = bad = 0
    def check(name, cond, extra=""):
        nonlocal ok, bad
        print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"   [{extra}]" if extra else ""))
        ok, bad = ok + bool(cond), bad + (not cond)
    if importlib.util.find_spec("numpy") is None:
        print("  SKIP everything (numpy needed)"); return True
    import numpy as np
    print("\n  gate (1): the record's sealed golden, README-HANDOFF-32 gate (51)")
    m = _load_sox(GOLD_MESH)
    fix = g2b_fixed(m, GOLD_Q); rec = float(m.g2b(GOLD_Q))
    check("the record's fix reproduces g_2b(1.44881) = 0.0293843 at (80,80,64,128)",
          abs(fix / GOLD_G - 1) < 5e-5, f"{fix:.7f} ({(fix/GOLD_G-1)*100:+.4f} %)")
    check("the recovered text does not, and the shortfall is the fault the record names",
          -0.011 < rec / GOLD_G - 1 < -0.004, f"{rec:.7f} ({(rec/GOLD_G-1)*100:+.3f} %)")
    print("\n  gate (2): the ball autoconvolution, the record's own internal check on rho_q (unchanged)")
    P = np.array([0.3, 1.0, 1.7])
    rr = m.rho_q(3.0, P, np.zeros(3)); ex = (4 * np.pi / 3) * (1 - 3 * P / 4 + P ** 3 / 16)
    check("rho_q(q>2) is the unit-ball autoconvolution", float(np.max(abs(rr / ex - 1))) < 1e-3,
          f"max rel {float(np.max(abs(rr/ex-1))):.1e}")
    print("\n  gate (3): the analytic large-q limit, which the record does not state")
    m2 = _load_sox((160, 160, 64, 128))
    g16 = g2b_fixed(m2, 16.0)
    check("g_2b(q) q^4 -> 4/(3 pi^2) at q = 16 (fixes the prefactor 3/(16 pi^5) without E0B)",
          abs(g16 * 16.0 ** 4 / TAIL - 1) < 0.02, f"ratio {g16*16.0**4/TAIL:.4f}")
    print("\n  gate (4): G-S1 against the exactly known constant")
    if not os.path.exists(TABLE_JSON):
        print("  SKIP soxquad-table.json absent (run --table)")
    else:
        T = json.load(open(TABLE_JSON))
        check("int dq g_2b = E0B = 0.0241792 Ha within 0.05 % (the record's own gate read +0.062 %)",
              abs(T["int_g2b_Ha"] / E0B - 1) < 5e-4, f"{T['int_g2b_Ha']:.7f} ({(T['int_g2b_Ha']/E0B-1)*100:+.3f} %)")
        check("and it is closer to the constant than the record's own reading",
              abs(T["int_g2b_Ha"] / E0B - 1) < abs(GS1_RECORD / E0B - 1),
              f"{abs(T['int_g2b_Ha']/E0B-1)*100:.3f} % vs {abs(GS1_RECORD/E0B-1)*100:.3f} %")
        Q = np.array(T["q"]); G = np.array(T["g2b_Ry"])
        check("the table is on the pre-fix table's own q grid, so the quadrature is the only change",
              len(Q) == 130 and abs(Q[0] - 0.002) < 1e-9 and abs(Q[-1] - 120.0) < 1e-9, f"{len(Q)} q, {Q[0]}..{Q[-1]}")
        check("the table's own large-q tail carries the analytic coefficient",
              abs(G[-1] * Q[-1] ** 4 / TAIL - 1) < 0.05, f"ratio {G[-1]*Q[-1]**4/TAIL:.4f}")
    if os.path.exists(CONV_JSON):
        print("\n  the banked convergence study")
        C = json.load(open(CONV_JSON))
        if C.get("ladder"):
            fs = [x["g"] for x in C["ladder"]]; ns = [x["NZ"] for x in C["ladder"]]
            lim = richardson(fs, ns)
            check(f"the production mesh {PROD_MESH} is within 0.03 % of the h^2 limit",
                  abs(fs[0] / lim - 1) < 3e-4, f"{(fs[0]/lim-1)*100:+.4f} %")
            check("the record's own lens mesh (NZ = 80) carries the +0.06 % the record read on G-S1",
                  0.0003 < C["lens"][1]["g"][2] / lim - 1 < 0.0012,
                  f"{(C['lens'][1]['g'][2]/lim-1)*100:+.3f} %")
        if C.get("pmesh"):
            a, b = C["pmesh"][1]["g"][2], C["pmesh"][2]["g"][2]
            check("the P mesh is converged by the recovered (64, 128): doubling moves it under 0.02 %",
                  abs(b / a - 1) < 2e-4, f"{(b/a-1)*100:+.4f} %")
    print(f"\n  {ok} passed, {bad} failed")
    return bad == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--converge", action="store_true")
    ap.add_argument("--table", action="store_true")
    a = ap.parse_args()
    if a.selftest: sys.exit(0 if selftest() else 1)
    if a.converge: cmd_converge(); return
    if a.table: cmd_table(); return
    report()


if __name__ == "__main__":
    main()
