"""g1cells5.py -- CERTIFY-10L5 section 6b (D399): the two gauges of G1 compared on the cells both keep.

The null foliation is the same in both gauges (section 6b, D386), so a cell (u_i, v_j) is the same pair of null
hypersurfaces in dnsolve5's gauge (the record's) and in dnsolve5v's (the swapped one); only the angle x is dragged
differently. Each run keeps the cells its own cut allows, and the cuts differ: a cell is dropped when R < r_cut at any
node, and R at a node is not invariant (D391). So a comparison of the two gauges, each over its own kept cells, compares
two sets of cells as well as two gauges. This script separates the two:

  --uv SW_N SW_2N SW_4N RE_N RE_2N RE_4N [k ...]
      in (u, v), on nested grids N, 2N, 4N at one M (checks/g1uv5.py's measures): per v-band, max |F_2N - F_4N| and the
      ratio max |F_N - F_2N| / max |F_2N - F_4N| (about 4 for second order) for F = P, s, m in each gauge, on the cells
      all six runs keep, with each v-column's last k such rows dropped;
  --angle SW_16 SW_24 SW_32 RE_16 RE_24 RE_32 [k ...]
      in angle, at one (u, v) grid (checks/g1geom5.py's measures, fields at 65 Chebyshev-Lobatto points, the axes
      included): per v-band, M16-M24 and M24-M32 of P, s, m on the cells all six runs keep, with k rows dropped; then
      M24-M32 of m and P over all those cells (k = 0) in each gauge, and in the record's gauge over the cells only it
      keeps, with their count per band.
SW_* are dnsolve5v.py runs, RE_* dnsolve5.py runs (`--run`). Labels: computed (floating point, on saved runs).

    python3 checks/g1cells5.py --uv SW200 SW400 SW800 RE200 RE400 RE800 3 10 50
    python3 checks/g1cells5.py --angle SW16 SW24 SW32 RE16 RE24 RE32 10 40
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g1geom5 as GA   # noqa: E402
import g1uv5 as GU     # noqa: E402

GAUGES = ("swapped", "record")


def row(vals, fmt="%8.1e"):
    return " ".join(fmt % q for q in vals)


def uv(paths, ks):
    F, ok, v = {}, None, None
    for g, ps in zip(GAUGES, (paths[:3], paths[3:6])):
        ds = [np.load(p) for p in ps]
        assert np.allclose(ds[0]["u"], ds[1]["u"][::2]) and np.allclose(ds[0]["u"], ds[2]["u"][::4]), "u not nested"
        assert np.allclose(ds[0]["v"], ds[1]["v"][::2]) and np.allclose(ds[0]["v"], ds[2]["v"][::4]), "v not nested"
        out = [GU.fields(d, st) for d, st in zip(ds, (1, 2, 4))]
        F[g] = [o[0] for o in out]
        keep = ~(out[0][1] | out[1][1] | out[2][1])
        print("%-8s keeps %d coarse cells at all three grids" % (g, keep.sum()))
        ok = keep if ok is None else ok & keep
        v = ds[0]["v"]
    print("both keep:", int(ok.sum()), "\nv-bands:", GU.BANDS)
    for k in ks:
        sel = GU.interior(ok, k)
        for name in ("P", "s", "m"):
            for g in GAUGES:
                c, m, f = F[g]
                d1 = GU.band_max(np.abs(c[name] - m[name]).max(-1), sel, v)
                d2 = GU.band_max(np.abs(m[name] - f[name]).max(-1), sel, v)
                with np.errstate(divide="ignore", invalid="ignore"):
                    print("k=%-3d %s %-8s 2N-4N: %s" % (k, name, g, row(d2)))
                    print("%-21s ratio: %s" % ("", row(d1/d2, "%8.2f")))


def angle(paths, ks):
    F, keep, v = {}, {}, None
    for g, ps in zip(GAUGES, (paths[:3], paths[3:6])):
        ds = [np.load(p) for p in ps]
        F[g] = [GA.fields(d) for d in ds]
        keep[g] = ~(ds[0]["mask"] | ds[1]["mask"] | ds[2]["mask"])
        v = ds[0]["v"]
    ok = keep["swapped"] & keep["record"]
    only = keep["record"] & ~keep["swapped"]
    both_sw = (keep["swapped"] & ~keep["record"]).sum()
    print("kept at all three M: swapped %d, record %d; both %d; record only %d; swapped only %d"
          % (keep["swapped"].sum(), keep["record"].sum(), ok.sum(), only.sum(), both_sw))
    print("v-bands:", GA.BANDS)
    for k in ks:
        sel = GA.interior(ok, k)
        for name in ("P", "s", "m"):
            for g in GAUGES:
                a, b, c = F[g]
                d1 = GA.band_max(np.abs(a[name] - b[name]).max(-1), sel, v)
                d2 = GA.band_max(np.abs(b[name] - c[name]).max(-1), sel, v)
                print("k=%-3d %s %-8s M16-M24: %s" % (k, name, g, row(d1)))
                print("%-20s M24-M32: %s" % ("", row(d2)))
    for tag, sel, g in (("both keep, swapped", ok, "swapped"), ("both keep, record", ok, "record"),
                        ("record only, record", only, "record")):
        for name in ("m", "P"):
            b, c = F[g][1], F[g][2]
            d = GA.band_max(np.abs(b[name] - c[name]).max(-1), sel, v)
            print("%-20s %s M24-M32 (k = 0): %s" % (tag, name, row(d)))
    print("record-only cells per band:", [int((only & ((v >= lo) & (v < hi))[None, :]).sum()) for lo, hi in GA.BANDS])


def main():
    mode, rest = sys.argv[1], sys.argv[2:]
    paths, ks = rest[:6], [int(q) for q in rest[6:]] or [10]
    {"--uv": uv, "--angle": angle}[mode](paths, ks)


if __name__ == "__main__":
    main()
