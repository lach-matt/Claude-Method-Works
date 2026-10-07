#!/usr/bin/env python3
"""static.py -- M's static planes with moving surfaces (M-RULINGS item 141).

M (item 141): "If planes are constantly in motion around each other, a stable throat cannot form. I suggest the planes
are static, but their surfaces contain their own movements from within their own contained dimensions / Imagine two
rubiks cubes solving so that their facing sides match".  This instrument asks what that configuration does to the
questions left open by positivity.py (is the energy positive?) and kderive.py (what holds position 2's plane?).

  S1  a static configuration exists at every separation: in the Lykken-Randall bulk (PRZ hep-th/0004028v2, READ, eqs.
      2.16-2.17) the tensions do not depend on the separation r, so no force moves the planes; r is still physical
      (the 4D Planck mass depends on it), so "static" is a real condition, not a choice of coordinates
  S2  the force law on our plane splits EXACTLY into a massless graviton and the radion:
        (1/(8 Mhat^2))(P2 - (2/3) P0) - (1/(24 ML^2)) P0  =  (1/(8 Mhat^2))(P2 - P0)  +  (1/C_r) P0
      (PRZ eq. 3.3, by their identity 3.4).  The radion term is the only source of gamma != 1: remove it and gamma = 1;
      keep it and gamma = 5/4 at the coinciding planes (multiplane.py M4)
  S3  how the planes are held matters: with kinetic coefficient C_r < 0, ANY restoring potential leaves a mode of
      negative energy (a massive ghost); only a constraint -- the separation not a variable at all -- removes it
  S4  under the static constraint the energy is positive in both senses the board can compute: the background keeps the
      null energy condition (positivity.py Q3) and the one remaining long-range mode, the graviton, has positive norm
  S5  the surfaces' movements cost nothing and change nothing the bulk sees, if they are reorganizations: E depends on
      the README's bit count N alone (exactE.py's defining relation), and a permutation of the README's states keeps
      its entropy, so Landauer's erasure cost is zero; a map that merges states (the control) costs at least kT ln2
  S6  matching: two surfaces whose N-bit arrangements match carry N bits of mutual information (H-PASSAGE-IS-N);
      arrangements that match by chance do so with probability 2^-N, so the match is made, not found
  S7  M's image, run: two Rubik's cubes face to face.  Face turns never move a centre (the frame is static, the content
      moves); they keep every colour's count (reorganization); each quarter turn has order 4 (reversible).  Cube A is
      the mirror image of cube B through the plane between them; if A makes the mirror of each of B's moves, their
      facing sides stay matched through any scramble.  Control: the same, unmirrored moves break the match.  And since
      centres never move, two cubes whose facing centres differ (a frame not shared) can never be matched by turning
Imports multiplane.py, positivity.py, exactE.py (by path); stdlib + sympy.  python3 static.py [--selftest]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import random
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
EXAMPLE_N = 2742570311524972


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


_C = {}


def owners():
    if not _C:
        _C["mp"] = _load(os.path.join(HERE, "multiplane.py"), "st_multiplane")
        _C["pos"] = _load(os.path.join(HERE, "positivity.py"), "st_positivity")
    return _C


# ---------------------------------------------------------------- S1-S4: the bulk

def s1():
    mp = owners()["mp"]
    d = mp.lr()
    return {"dtau1_dr": sp.diff(d["tau1"], mp.r), "dtau2_dr": sp.diff(d["tau2"], mp.r),
            "dMhat2_dr": sp.simplify(sp.diff(d["Mhat2"], mp.r)),
            "dMhat2_dr_equal_k": sp.simplify(sp.diff(d["Mhat2"], mp.r).subs(mp.kR, mp.kL))}


def s2(cr_scale=1):
    """The split of PRZ eq. 3.3.  cr_scale != 1 is the control: a wrong radion coefficient leaves a residue."""
    mp = owners()["mp"]
    d = mp.lr()
    P2, P0 = sp.symbols("P2 P0")
    prz = (P2 - sp.Rational(2, 3) * P0) / (8 * d["Mhat2"]) - P0 / (24 * d["ML2"])
    split = (P2 - P0) / (8 * d["Mhat2"]) + P0 / (cr_scale * d["Cr"])
    residue = sp.simplify(sp.expand(prz - split))
    graviton_only_c0 = sp.Integer(-1)                       # (P2 - P0): the massless graviton alone
    at = {mp.M: 1, mp.kL: 1, mp.kR: sp.Rational(3, 4), mp.r: 0}
    return {"residue": residue, "gamma_frozen": mp.gamma_from_c0(graviton_only_c0),
            "gamma_with_radion": sp.simplify(d["gamma"].subs(at)), "graviton_coeff_r0": sp.simplify(
                (1 / (8 * d["Mhat2"])).subs(at)), "Cr_r0": sp.simplify(d["Cr"].subs(at))}


def s3(Cr):
    """Energy of one mode with kinetic coefficient Cr and restoring potential m^2 >= 0: H = Cr/2 v^2 + m^2/2 phi^2.
    Returns whether H is non-negative for every state, for every m^2 >= 0, and H at (phi, v) = (0, 1)."""
    m2 = sp.Symbol("m2", nonnegative=True)
    phi, v = sp.symbols("phi v", real=True)
    Hm = sp.Rational(1, 2) * Cr * v**2 + sp.Rational(1, 2) * m2 * phi**2
    return {"H_at_v1": Hm.subs({phi: 0, v: 1}), "positive_for_all": bool(Cr >= 0)}


def s4():
    pos = owners()["pos"]
    q3 = pos.q3()
    lrs, ky = sp.Symbol("lambda_RS", positive=True), sp.Symbol("k_y", real=True)
    return {"S_total": q3["S_total"], "S_ok": sp.simplify(q3["S_total"] - lrs * ky**2) == 0,
            "graviton_coeff_r0": s2()["graviton_coeff_r0"]}


# ---------------------------------------------------------------- S5-S6: the surfaces

def entropy_bits(dist):
    return -sum(p * math.log2(p) for p in dist.values() if p > 0)


def push(dist, f):
    out = {}
    for s, p in dist.items():
        out[f(s)] = out.get(f(s), 0) + p
    return out


def s5(nbits=4, seed=141):
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "st_exactE")
    E_N = sp.sqrt(sp.Symbol("N", positive=True)) * sp.Float(str(ex.e_per_sqrt_bit()), 25)
    states = list(itertools.product((0, 1), repeat=nbits))
    uniform = {s: 1 / len(states) for s in states}
    rng = random.Random(seed)
    perm = states[:]
    rng.shuffle(perm)
    P = dict(zip(states, perm))
    after_perm = push(uniform, lambda s: P[s])
    erase = push(uniform, lambda s: (0,) + s[1:])           # control: reset the first bit
    return {"E_free_symbols": sorted(str(x) for x in E_N.free_symbols),
            "H_before": entropy_bits(uniform), "H_perm": entropy_bits(after_perm), "H_erase": entropy_bits(erase),
            "nbits": nbits}


def mutual_information(joint):
    pa, pb = {}, {}
    for (a, b), p in joint.items():
        pa[a] = pa.get(a, 0) + p
        pb[b] = pb.get(b, 0) + p
    return sum(p * math.log2(p / (pa[a] * pb[b])) for (a, b), p in joint.items() if p > 0)


def s6(nbits=5):
    states = list(itertools.product((0, 1), repeat=nbits))
    w = 1 / len(states)
    matched = {(s, tuple(reversed(s))): w for s in states}          # B is A's mirror image, sticker for sticker
    independent = {(a, b): w * w for a in states for b in states}
    return {"MI_matched": mutual_information(matched), "MI_independent": mutual_information(independent),
            "nbits": nbits, "log10_chance_example": -EXAMPLE_N * math.log10(2)}


# ---------------------------------------------------------------- S7: two Rubik's cubes

AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def solved(mirror=False):
    """Stickers as (position, normal) -> colour.  Colour = the name of the solved normal.  mirror=True builds the
    mirror image through x = 0 (positions and normals reflected, colours kept)."""
    cube = {}
    for p in itertools.product((-1, 0, 1), repeat=3):
        for ax in range(3):
            if p[ax] != 0:
                n = tuple(p[ax] if i == ax else 0 for i in range(3))
                col = ("+" if p[ax] > 0 else "-") + "xyz"[ax]
                if mirror:
                    p2, n2 = (-p[0], p[1], p[2]), (-n[0], n[1], n[2])
                    cube[(p2, n2)] = col
                else:
                    cube[(p, n)] = col
    return cube


def rot(v, ax, q):
    """Rotate integer vector v by q quarter turns (right-handed) about axis ax."""
    x, y, z = v
    for _ in range(q % 4):
        if ax == 0:
            y, z = -z, y
        elif ax == 1:
            z, x = -x, z
        else:
            x, y = -y, x
    return (x, y, z)


def turn(cube, ax, layer, q):
    out = {}
    for (p, n), c in cube.items():
        if p[ax] == layer:
            out[(rot(p, ax, q), rot(n, ax, q))] = c
        else:
            out[(p, n)] = c
    return out


def mirror_move(ax, layer, q):
    """The reflection x -> -x carries a turn about x to the opposite x-layer, same sense; a turn about y or z to the
    same layer, opposite sense.  Derived, then tested by the match it must keep."""
    return (0, -layer, q) if ax == 0 else (ax, layer, -q)


FACE_TURNS = [(ax, layer, q) for ax in range(3) for layer in (-1, 1) for q in (1, 2, 3)]


def centres(cube):
    return {k: c for k, c in cube.items() if sum(1 for t in k[0] if t != 0) == 1}


def counts(cube):
    out = {}
    for c in cube.values():
        out[c] = out.get(c, 0) + 1
    return out


def facing_match(A, B):
    """A sits to the left of B: A's +x face against B's -x face, sticker (1, y, z) against (-1, y, z)."""
    for (p, n), c in A.items():
        if n == (1, 0, 0):
            if B[((-1, p[1], p[2]), (-1, 0, 0))] != c:
                return False
    return True


def s7(nmoves=40, seed=141):
    rng = random.Random(seed)
    seq = [rng.choice(FACE_TURNS) for _ in range(nmoves)]
    B, A = solved(), solved(mirror=True)
    Bc, Ac = solved(), solved(mirror=True)                     # control: A copies B's moves unmirrored
    start_match = facing_match(A, B)
    still = True
    for mv in seq:
        B = turn(B, *mv)
        A = turn(A, *mirror_move(*mv))
        still = still and facing_match(A, B)
        Bc = turn(Bc, *mv)
        Ac = turn(Ac, *mv)
    base = solved()
    centres_fixed = all(centres(turn(base, *mv)) == centres(base) for mv in FACE_TURNS)
    slice_moves_centre = centres(turn(base, 0, 0, 1)) != centres(base)        # control: a middle slice
    counts_kept = counts(B) == counts(solved()) and counts(A) == counts(solved(mirror=True))
    order4 = all(turn(turn(turn(turn(base, ax, l, 1), ax, l, 1), ax, l, 1), ax, l, 1) == base
                 for ax in range(3) for l in (-1, 1))
    once = all(turn(base, ax, l, 1) != base for ax in range(3) for l in (-1, 1))
    scrambled = B != solved()
    # a frame not shared: A an unmirrored copy of B.  Its +x centre faces B's -x centre; centres never move under face
    # turns, so if those two differ no sequence of turns can ever match the facing sides
    copy = solved()
    unshared = copy[((1, 0, 0), (1, 0, 0))] != solved()[((-1, 0, 0), (-1, 0, 0))]
    return {"unshared_frame_blocks": unshared and centres_fixed, "start_match": start_match, "kept_match": still, "control_match": facing_match(Ac, Bc),
            "centres_fixed": centres_fixed, "slice_moves_centre": slice_moves_centre, "counts_kept": counts_kept,
            "order4": order4 and once, "scrambled": scrambled, "nmoves": nmoves}


# ----------------------------------------------------------------

def report():
    a, b, c_neg, c_pos, d, e, f, g = s1(), s2(), s3(-96), s3(96), s4(), s5(), s6(), s7()
    print("static.py -- M's static planes with moving surfaces (item 141)\n")
    print("S1 static exists at every separation: d(tau1)/dr = %s, d(tau2)/dr = %s; but d(Mhat^2)/dr = %s (zero only if "
          "k_R = k_L: %s) -- the separation is physical" % (a["dtau1_dr"], a["dtau2_dr"], a["dMhat2_dr"],
                                                           a["dMhat2_dr_equal_k"]))
    print("S2 PRZ eq. 3.3 = graviton (P2 - P0)/(8 Mhat^2) + radion P0/C_r: residue %s.  Radion frozen: gamma = %s; "
          "radion live at the coinciding planes: gamma = %s" % (b["residue"], b["gamma_frozen"], b["gamma_with_radion"]))
    print("S3 a mode held by a restoring potential: with C_r = -96 (the coinciding planes) the energy at rest position, "
          "unit speed, is %s for every m^2 -- a massive ghost; with C_r = +96 non-negative for all states: %s"
          % (c_neg["H_at_v1"], c_pos["positive_for_all"]))
    print("S4 under the static constraint: background null energy %s on the summed surface; graviton coefficient %s > 0"
          % (d["S_total"], d["graviton_coeff_r0"]))
    print("S5 E(N) depends on %s only; a permutation of %d bits keeps the entropy (%.3f -> %.3f bits: Landauer cost 0); "
          "erasing one bit (control) %.3f -> %.3f" % (e["E_free_symbols"], e["nbits"], e["H_before"], e["H_perm"],
                                                     e["H_before"], e["H_erase"]))
    print("S6 matched %d-bit surfaces share %.3f bits; independent ones %.3f; a chance match at the example README has "
          "probability 10^(%.4g)" % (f["nbits"], f["MI_matched"], f["MI_independent"], f["log10_chance_example"]))
    print("S7 Rubik's cubes face to face: matched at start %s; after a %d-move scramble with mirrored moves %s; with the "
          "same moves unmirrored %s.  Centres fixed under every face turn %s (a middle slice moves them: %s); colour "
          "counts kept %s; quarter turns of order 4 %s.  A frame not shared can never match: %s"
          % (g["start_match"], g["nmoves"], g["kept_match"], g["control_match"], g["centres_fixed"],
             g["slice_moves_centre"], g["counts_kept"], g["order4"], g["unshared_frame_blocks"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    a, b, bctl = s1(), s2(), s2(cr_scale=2)
    chk("S1: the tensions do not depend on the separation -- a static configuration exists at every r",
        a["dtau1_dr"] == 0 and a["dtau2_dr"] == 0)
    chk("S1 control: the 4D Planck mass does depend on r (unless k_R = k_L), so r is physical",
        a["dMhat2_dr"] != 0 and a["dMhat2_dr_equal_k"] == 0)
    chk("S2: PRZ eq. 3.3 splits exactly into a massless graviton and P0/C_r", b["residue"] == 0)
    chk("S2 control: with the radion coefficient doubled the split leaves a residue", bctl["residue"] != 0)
    chk("S2: radion frozen gives gamma = 1; live at the coinciding planes, 5/4",
        b["gamma_frozen"] == 1 and b["gamma_with_radion"] == sp.Rational(5, 4))
    neg, posi = s3(b["Cr_r0"]), s3(96)
    chk("S3: with the coinciding planes' C_r = %s a restoring potential leaves negative energy (a massive ghost)"
        % b["Cr_r0"], neg["H_at_v1"] < 0 and not neg["positive_for_all"])
    chk("S3 control: a mode with positive kinetic coefficient is non-negative for every state", posi["positive_for_all"])
    d = s4()
    chk("S4: under the static constraint the background keeps null energy and the graviton's norm is positive",
        d["S_ok"] and d["graviton_coeff_r0"] > 0)
    e = s5()
    chk("S5: E depends on N alone (no other free symbol)", e["E_free_symbols"] == ["N"])
    chk("S5: a permutation of the README's states keeps its entropy: Landauer cost zero",
        abs(e["H_perm"] - e["H_before"]) < 1e-12)
    chk("S5 control: erasing one bit lowers the entropy by one bit (cost kT ln2)",
        abs(e["H_before"] - e["H_erase"] - 1) < 1e-12)
    f = s6()
    chk("S6: matched surfaces carry exactly N bits of mutual information; independent ones none",
        abs(f["MI_matched"] - f["nbits"]) < 1e-12 and abs(f["MI_independent"]) < 1e-12)
    g = s7()
    chk("S7: mirrored moves keep the facing sides matched through a scramble", g["start_match"] and g["kept_match"]
        and g["scrambled"])
    chk("S7 control: the same moves unmirrored break the match", not g["control_match"])
    chk("S7: face turns never move a centre; a middle slice does (control)", g["centres_fixed"] and g["slice_moves_centre"])
    chk("S7: with a frame not shared (an unmirrored copy) the facing centres differ, and as centres never move, no "
        "sequence of turns can match the facing sides", g["unshared_frame_blocks"])
    chk("S7: colour counts kept, quarter turns of order 4 (reorganization, reversible)", g["counts_kept"] and g["order4"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
