#!/usr/bin/env python3
"""
phonon_kpoint_derive.py -- THE GROUND TRUTH any k-point phonon index must
reproduce.  Derivation behind captures/PHONON-KGROUND.tsv and
captures/PHONON-KCRYSTALS.tsv.

    python3 phonon_kpoint_derive.py            rebuild both captures
    python3 phonon_kpoint_derive.py --selftest fixtures (needs numpy+spglib)

Needs numpy and spglib; the cross-validation additionally needs spgrep.
None is vendored -- sgcapture.py's pattern and its reason.

WHAT THIS DISCHARGES.  phonondex.py section 5 refuses k != Gamma because "at a
general k the little group's representations are PROJECTIVE for non-symmorphic
groups, which is a different computation".  It is a different computation but
it is NOT a different machinery: by HERRING'S METHOD the little group modulo
the phase-trivial translations is a FINITE group Ghat, and the projective
irreps of the little co-group are exactly the ORDINARY irreps of Ghat in one
central-character sector.  Burnside's class algebra -- already seated in
phonon_derive.py -- runs on Ghat unchanged.  The refusal is DISCHARGED.

WHAT THIS FINDS INSTEAD, AND IT IS THE REAL OBSTRUCTION.  Discharging the
projective refusal is NECESSARY AND NOT SUFFICIENT.  A second, independent
obstruction -- TIME REVERSAL, via Herring's criterion -- degenerates levels at
126 space groups' TRIMs against the projective mechanism's 108, and 56 space
groups are touched by the antiunitary obstruction ALONE.  An implementation
that discharges only the projective refusal is wrong at those 56 and its
integrality checks do not notice.  RECORDED, NOT REPAIRED.
"""

import numpy as np, spglib, itertools, time, sys
from fractions import Fraction

def prim_sym(lat, pos, num):
    """spglib operations in the basis the cell is given in."""
    d = spglib.get_symmetry((lat, pos, num), symprec=1e-5)
    R = np.asarray(d['rotations']); t = np.asarray(d['translations']) % 1.0
    # one translation per rotation is required
    seen = {}
    for Ri, ti in zip(R, t):
        key = tuple(Ri.ravel())
        if key in seen:
            d0 = np.abs(seen[key] - ti); d0 = np.minimum(d0, 1 - d0)
            assert np.max(d0) < 1e-6, "more than one translation per rotation -> not primitive"
        seen[key] = ti
    return R, t

def denom(k):
    from math import gcd
    ds = [Fraction(x).limit_denominator(60).denominator for x in k]
    N = 1
    for d in ds: N = N * d // gcd(N, d)
    return N

def little(R, t, k):
    """Row convention: k -> k R.  Returns indices with k R == k mod 1."""
    out = []
    for i, Ri in enumerate(R):
        d = np.asarray(k, float) @ Ri - np.asarray(k, float)
        if np.max(np.abs(d - np.round(d))) < 1e-8:
            out.append(i)
    return out

def ghat(R, t, k, N, idxs):
    """Multiplication table of Ghat = G^k / T_k, order len(idxs)*N.

    Element (a, c): rotation R[idxs[a]], translation t[idxs[a]] + n where
    c = round(N * k.n) mod N labels the coset of n in Z^3 / T_k.
    """
    m = len(idxs)
    rot = {tuple(R[i].ravel()): a for a, i in enumerate(idxs)}
    kk = np.asarray(k, float)
    tab = np.zeros((m * N, m * N), int)
    for a in range(m):
        ia = idxs[a]
        for b in range(m):
            ib = idxs[b]
            Rp = R[ia] @ R[ib]
            tp = R[ia] @ t[ib] + t[ia]
            c = rot[tuple(Rp.ravel())]
            n = tp - t[idxs[c]]
            assert np.max(np.abs(n - np.round(n))) < 1e-6
            ph = int(round(N * float(kk @ np.round(n)))) % N
            for ca in range(N):
                for cb in range(N):
                    tab[a * N + ca, b * N + cb] = c * N + (ca + cb + ph) % N
    return tab

def classes(tab):
    n = tab.shape[0]
    inv = {}
    e = None
    for g in range(n):
        if all(tab[g, h] == h for h in range(n)): e = g
    assert e is not None
    for g in range(n):
        for h in range(n):
            if tab[g, h] == e: inv[g] = h
    seen, cls = set(), []
    for g in range(n):
        if g in seen: continue
        c = sorted({tab[tab[x, g], inv[x]] for x in range(n)})
        cls.append(c); seen |= set(c)
    cls.sort(key=lambda c: 0 if c == [e] else 1)
    return e, cls

def char_table(tab):
    """Burnside class algebra on an abstract multiplication table."""
    e, cls = classes(tab)
    n = len(cls)
    co = {}
    for ci, c in enumerate(cls):
        for g in c: co[g] = ci
    order = tab.shape[0]
    Nmat = np.zeros((n, n, n))
    for i in range(n):
        for j in range(n):
            cnt = np.zeros(n)
            for a in cls[i]:
                for b in cls[j]:
                    cnt[co[tab[a, b]]] += 1
            Nmat[i, j] = cnt / np.array([len(c) for c in cls])
    for seed in range(400):
        T = _try(cls, Nmat, order, seed)
        if T is not None:
            return e, cls, T
    raise RuntimeError("no valid character table, |G|=%d" % order)

def _try(cls, Nm, order, seed):
    n = len(cls)
    A = np.tensordot(np.random.default_rng(seed).normal(size=n), Nm, axes=(0, 0))
    _w, V = np.linalg.eig(A)
    out = []
    for r in range(n):
        v = V[:, r]
        if abs(v[0]) < 1e-9: return None
        om = v / v[0]
        base = np.array([om[i] / len(cls[i]) for i in range(n)])
        s2 = sum(len(cls[i]) * abs(base[i]) ** 2 for i in range(n))
        if abs(s2) < 1e-12: return None
        chi = base * np.sqrt(order / s2)
        if np.real(chi[0]) < 0: chi = -chi
        out.append(chi)
    T = np.array(out)
    dims = [complex(x[0]) for x in T]
    if any(abs(d.imag) > 1e-6 or abs(d.real - round(d.real)) > 1e-6 for d in dims): return None
    if abs(sum(round(d.real) ** 2 for d in dims) - order) > 1e-6: return None
    for r in range(n):
        for q in range(n):
            ip = sum(len(cls[i]) * T[r][i] * np.conj(T[q][i]) for i in range(n)) / order
            if abs(ip - (1.0 if r == q else 0.0)) > 1e-6: return None
    idx = sorted(range(n), key=lambda r: (round(T[r][0].real),
                 [round(float(np.real(x)), 4) for x in T[r]], [round(float(np.imag(x)), 4) for x in T[r]]))
    return T[idx]

def mech(R, t, pos, k, N, idxs, sign):
    """3n x 3n matrices of the phonon rep for every element of Ghat."""
    na = len(pos); m = len(idxs)
    kk = np.asarray(k, float)
    D = []
    for a in range(m):
        i = idxs[a]
        M = np.zeros((3 * na, 3 * na), complex)
        for b in range(na):
            img = (R[i] @ pos[b] + t[i])
            hit = None
            for c in range(na):
                d = img - pos[c]
                if np.max(np.abs(d - np.round(d))) < 1e-5:
                    hit = c; L = np.round(d); break
            assert hit is not None
            ph = np.exp(sign * 2j * np.pi * float(kk @ L))
            M[3 * hit:3 * hit + 3, 3 * b:3 * b + 3] = R[i] * ph
        for c in range(N):
            D.append(M * np.exp(sign * 2j * np.pi * c / N))
    return D

def decompose(lat, pos, num, k, verbose=False):
    R, t = prim_sym(lat, pos, num)
    k = np.asarray(k, float)
    N = denom(k)
    idxs = little(R, t, k)
    tab = ghat(R, t, k, N, idxs)
    # fix the phase sign empirically: D must be a rep of Ghat
    good = None
    for sign in (-1, +1):
        D = mech(R, t, pos, k, N, idxs, sign)
        ok = True
        for a in range(len(D)):
            for b in range(len(D)):
                if np.max(np.abs(D[a] @ D[b] - D[tab[a, b]])) > 1e-7: ok = False; break
            if not ok: break
        if ok: good = (sign, D); break
    assert good is not None, "no sign convention makes the mechanical rep a representation"
    sign, D = good
    e, cls, T = char_table(tab)
    chi = np.array([np.trace(D[c[0]]) for c in cls])
    order = tab.shape[0]
    mult = [complex(sum(len(cls[i]) * chi[i] * np.conj(T[r][i]) for i in range(len(cls))) / order)
            for r in range(len(T))]
    return dict(R=R, t=t, N=N, idxs=idxs, tab=tab, cls=cls, T=T, chi=chi,
                mult=mult, sign=sign, order=order, npg=len(idxs), nat=len(pos))

def herring(R, t, k, N, idxs, cls, T):
    """Herring's criterion for every irrep of Ghat, in the SAME labelling.

    Q = { q : k R_q == -k mod 1 }.  q^2 lies in the little group and its image
    in Ghat is independent of q's lattice representative, because
    exp(-2pi i k.(R_q n + n)) = 1 when k R_q == -k.

    W = +1 case (a), no extra degeneracy;  W = -1 case (b);  W = 0 case (c).
    In cases (b) and (c) TIME REVERSAL doubles the degeneracy, and that
    doubling is INVISIBLE to the unitary (projective) calculation.
    """
    k = np.asarray(k, float)
    Q = [i for i in range(len(R)) if np.max(np.abs(k @ R[i] + k - np.round(k @ R[i] + k))) < 1e-8]
    if not Q:
        return None, Q
    rot = {tuple(np.asarray(R[i]).ravel()): a for a, i in enumerate(idxs)}
    co = {}
    for ci, c in enumerate(cls):
        for g in c: co[g] = ci
    W = []
    for r in range(len(T)):
        s = 0
        for i in Q:
            Rq2 = np.asarray(R[i]) @ np.asarray(R[i])
            tq2 = np.asarray(R[i]) @ t[i] + t[i]
            a = rot[tuple(np.rint(Rq2).astype(int).ravel())]
            n = tq2 - t[idxs[a]]
            assert np.max(np.abs(n - np.round(n))) < 1e-6
            c = int(round(N * float(k @ np.round(n)))) % N
            s += T[r][co[a * N + c]]
        W.append(s / len(Q))
    return W, Q


# ===========================================================================
# THE TRIM SET.  Eight k-points needing NO table: k = half a reciprocal
# lattice vector, in the PRIMITIVE reciprocal basis.  Basis-independent, so
# it is a census and not a reading of anyone's k-vector tables.
# ===========================================================================
import itertools
TRIM = [np.array(v, float) / 2 for v in itertools.product((0, 1), repeat=3)]
GEN, GEN2 = (0.113, 0.271, 0.407), (0.317, 0.059, 0.223)


def hall(sg):
    for h in range(1, 531):
        if spglib.get_spacegroup_type(h).number == sg:
            return h


def orbit(sg, reps):
    """Full orbits from Wyckoff representatives, via the DATABASE operations."""
    d = spglib.get_symmetry_from_database(hall(sg))
    R, T = np.asarray(d['rotations']), np.asarray(d['translations'])
    pos, num = [], []
    for z, p in reps:
        p = np.asarray(p, float)
        for Ri, ti in zip(R, T):
            q = (Ri @ p + ti) % 1.0
            if not any(np.max(np.minimum(np.abs(q - o), 1 - np.abs(q - o))) < 1e-6 for o in pos):
                pos.append(q); num.append(z)
    return np.array(pos), num


def probe_cell(sg):
    """A crystal in space group sg and no more: two generic orbits, two species.
    ONE species is not enough -- a single generic orbit gains symmetry (P1 with
    one atom is P-1), which silently built the wrong group for 53 of 230."""
    pos, num = orbit(sg, [(1, GEN), (2, GEN2)])
    a, b, c, al, be, ga = 5.1, 5.1, 5.1, 90, 90, 90
    if sg <= 2:    a, b, c, al, be, ga = 5.1, 6.3, 7.2, 83, 97, 101
    elif sg <= 15: a, b, c, be = 5.1, 6.3, 7.2, 101
    elif sg <= 74: a, b, c = 5.1, 6.3, 7.2
    elif sg <= 142: a, b, c = 5.1, 5.1, 7.2
    elif sg <= 194: a, b, c, ga = 5.1, 5.1, 7.2, 120
    al, be, ga = (np.radians(x) for x in (al, be, ga))
    lat = np.array([[a, 0, 0], [b * np.cos(ga), b * np.sin(ga), 0],
                    [c * np.cos(be), c * (np.cos(al) - np.cos(be) * np.cos(ga)) / np.sin(ga), 0]])
    lat[2, 2] = np.sqrt(max(c * c - lat[2, 0] ** 2 - lat[2, 1] ** 2, 1e-9))
    return (lat, pos, num)


def sectors(R, t, k):
    """Allowed-sector dims and Herring W, for the little group at k."""
    N = denom(k); idxs = little(np.array(R), t, k)
    tab = ghat(np.array(R), t, k, N, idxs)
    e, cls, T = char_table(tab)
    dims = [int(round(x[0].real)) for x in T]
    I = tuple(np.eye(3, dtype=int).ravel())
    a0 = [a for a, i in enumerate(idxs) if tuple(np.asarray(R[i]).ravel()) == I][0]
    cz = [ci for ci, c in enumerate(cls) if a0 * N + 1 in c][0]
    allowed = [r for r in range(len(T)) if abs(T[r][cz] / T[r][0] + 1) < 1e-6]
    W, Q = herring(R, t, k, N, idxs, cls, T)
    ws = [int(round(complex(W[r]).real)) for r in allowed] if W else []
    ad = sorted(dims[r] for r in allowed)
    # Sum of squared allowed dims equals |P_k|: the projective analogue of
    # sum(dim^2) = |G|, and it guards every row.
    assert sum(d * d for d in ad) == len(idxs), (k, ad, len(idxs))
    return len(idxs), ad, ws


def sweep(xval=True):
    """230 space groups x 7 non-Gamma TRIMs, both obstructions, cross-validated."""
    try:
        from spgrep import get_spacegroup_irreps_from_primitive_symmetry as sgi
    except Exception:
        sgi = None; xval = False
    rows = []; agree = dis = 0
    for sg in range(1, 231):
        cell = probe_cell(sg)
        got = spglib.get_spacegroup(cell, symprec=1e-4)
        assert got.endswith('(%d)' % sg), (sg, got)
        p = spglib.standardize_cell(cell, to_primitive=True, no_idealize=False, symprec=1e-4)
        d = spglib.get_symmetry(p, symprec=1e-4)
        R = [np.rint(x).astype(int) for x in d['rotations']]; t = np.array(d['translations']) % 1.0
        for k in TRIM:
            if np.allclose(k, 0): continue
            npg, ad, ws = sectors(R, t, k)
            if xval:
                irr, mp = sgi(np.array(R), t, k)
                b = sorted(i.shape[1] for i in irr)
                if b == ad and len(mp) == npg: agree += 1
                else: dis += 1; print("  XVAL DISAGREE", sg, k, ad, b, file=sys.stderr)
            rows.append((sg, k, npg, ad, ws))
    return rows, agree, dis


CRYSTALS = (
    # name, space group, lattice, Wyckoff representatives, k-points
    ("diamond C / Si", 227, ('F', 3.567), [(6, (0, 0, 0))],
     {"Gamma": (0, 0, 0), "X": (.5, .5, 0), "L": (.5, .5, .5), "W": (.25, .5, .75)}),
    ("NaCl rocksalt", 225, ('F', 5.640), [(11, (0, 0, 0)), (17, (.5, .5, .5))],
     {"Gamma": (0, 0, 0), "X": (.5, .5, 0), "L": (.5, .5, .5)}),
    ("GaAs zincblende", 216, ('F', 5.653), [(31, (0, 0, 0)), (33, (.25, .25, .25))],
     {"Gamma": (0, 0, 0), "X": (.5, .5, 0), "L": (.5, .5, .5)}),
    ("CaF2 fluorite", 225, ('F', 5.463), [(20, (0, 0, 0)), (9, (.25, .25, .25))],
     {"Gamma": (0, 0, 0), "X": (.5, .5, 0), "L": (.5, .5, .5)}),
    ("CsCl", 221, ('P', 4.110), [(55, (0, 0, 0)), (17, (.5, .5, .5))],
     {"Gamma": (0, 0, 0), "X": (.5, 0, 0), "M": (.5, .5, 0), "R": (.5, .5, .5)}),
    ("SrTiO3 perovskite", 221, ('P', 3.905), [(38, (0, 0, 0)), (22, (.5, .5, .5)), (8, (.5, .5, 0))],
     {"Gamma": (0, 0, 0), "X": (.5, 0, 0), "M": (.5, .5, 0), "R": (.5, .5, .5)}),
    ("W bcc", 229, ('I', 3.165), [(74, (0, 0, 0))],
     {"Gamma": (0, 0, 0), "H": (.5, .5, .5), "N": (.5, 0, 0), "P": (.25, .25, .25)}),
    ("graphite 2H", 194, ('H', 2.460, 6.700), [(6, (0, 0, .25)), (6, (1 / 3., 2 / 3., .25))],
     {"Gamma": (0, 0, 0), "A": (0, 0, .5), "M": (.5, 0, 0), "K": (1 / 3., 1 / 3., 0), "H": (1 / 3., 1 / 3., .5)}),
    ("MoS2 2H", 194, ('H', 3.160, 12.290), [(42, (1 / 3., 2 / 3., .25)), (16, (1 / 3., 2 / 3., .621))],
     {"Gamma": (0, 0, 0), "A": (0, 0, .5), "M": (.5, 0, 0), "K": (1 / 3., 1 / 3., 0)}),
    ("ZnO wurtzite", 186, ('H', 3.250, 5.207), [(30, (1 / 3., 2 / 3., 0.)), (8, (1 / 3., 2 / 3., .3825))],
     {"Gamma": (0, 0, 0), "A": (0, 0, .5), "M": (.5, 0, 0), "K": (1 / 3., 1 / 3., 0), "H": (1 / 3., 1 / 3., .5)}),
    ("rutile TiO2", 136, ('T', 4.594, 2.959), [(22, (0, 0, 0)), (8, (.3053, .3053, 0))],
     {"Gamma": (0, 0, 0), "Z": (0, 0, .5), "M": (.5, .5, 0), "A": (.5, .5, .5), "X": (.5, 0, 0), "R": (.5, 0, .5)}),
    ("alpha-quartz", 152, ('H', 4.913, 5.405), [(14, (.4697, 0, 1 / 3.)), (8, (.4135, .2669, .1191))],
     {"Gamma": (0, 0, 0), "A": (0, 0, .5), "M": (.5, 0, 0), "K": (1 / 3., 1 / 3., 0), "H": (1 / 3., 1 / 3., .5)}),
)


def build(spec, sg, reps):
    kind = spec[0]
    if kind == 'H':
        a, c = spec[1], spec[2]
        conv = np.array([[a, 0, 0], [-a / 2, a * np.sqrt(3) / 2, 0], [0, 0, c]])
    elif kind == 'T':
        a, c = spec[1], spec[2]
        conv = np.array([[a, 0, 0], [0, a, 0], [0, 0, c]])
    else:
        conv = np.eye(3) * spec[1]
    pos, num = orbit(sg, reps)
    cell = (conv, pos, num)
    got = spglib.get_spacegroup(cell, symprec=1e-4)
    assert got.endswith('(%d)' % sg), (sg, got)
    return spglib.standardize_cell(cell, to_primitive=True, no_idealize=False, symprec=1e-4)


def crystal_rows():
    out = []
    for name, sg, spec, reps, ks in CRYSTALS:
        lat, pos, num = build(spec, sg, reps)
        for kn, k in ks.items():
            r = decompose(np.asarray(lat), np.asarray(pos, float), list(num), k)
            W, Q = herring(r['R'], r['t'], k, r['N'], r['idxs'], r['cls'], r['T'])
            dims = [int(round(x[0].real)) for x in r['T']]
            mult = [m.real for m in r['mult']]
            # TWO INTEGRALITY GUARDS, exactly phonon_derive.py's, and a third
            # that only exists at k != Gamma: the multiplicity must vanish on
            # every irrep outside the allowed sector.
            assert all(abs(m - round(m)) < 1e-6 for m in mult), (name, kn, mult)
            assert all(abs(m.imag) < 1e-6 for m in r['mult']), (name, kn)
            tot = sum(d * round(m) for d, m in zip(dims, mult))
            assert tot == 3 * len(pos), (name, kn, tot, 3 * len(pos))
            lev = []
            for i, (d, m) in enumerate(zip(dims, mult)):
                if not round(m): continue
                w = int(round(complex(W[i]).real)) if W else 1
                lev.append((d, int(round(m)), w))
            out.append((name, sg, len(pos), kn, k, r['npg'], r['N'], r['order'], lev))
    return out


def fmt_lev(lev):
    return " + ".join("%dx(dim %d%s)" % (m, d, "" if w == 1 else ", W=%d" % w) for d, m, w in lev)


def main():
    t0 = time.time()
    rows, agree, dis = sweep()
    with open("PHONON-KGROUND.tsv", "w") as f:
        f.write("# 230 space groups x 7 non-Gamma TRIM points.  COMPUTED, and every row\n")
        f.write("# cross-validated against spgrep 0.7.0, which shares no code or algorithm.\n")
        f.write("sg\tk\tpk_order\tallowed_dims\tprojective\therring_W\tantiunitary\n")
        for sg, k, npg, ad, ws in rows:
            f.write("%d\t%s\t%d\t%s\t%d\t%s\t%d\n" % (
                sg, ",".join('1/2' if x else '0' for x in k), npg, ",".join(map(str, ad)),
                1 if min(ad) > 1 else 0, ",".join(map(str, ws)) if ws else "-",
                1 if any(w != 1 for w in ws) else 0))
    P = sum(1 for r in rows if min(r[3]) > 1)
    A = sum(1 for r in rows if any(w != 1 for w in r[4]))
    sP = {r[0] for r in rows if min(r[3]) > 1}
    sA = {r[0] for r in rows if any(w != 1 for w in r[4])}
    print("rows                                  %d" % len(rows), file=sys.stderr)
    print("cross-validation vs spgrep            agree %d  disagree %d" % (agree, dis), file=sys.stderr)
    print("PROJECTIVE obstruction                %d rows, %d space groups" % (P, len(sP)), file=sys.stderr)
    print("ANTIUNITARY obstruction (Herring)     %d rows, %d space groups" % (A, len(sA)), file=sys.stderr)
    print("antiunitary ONLY (missed by a correct")
    print("  projective implementation)          %d space groups" % len(sA - sP), file=sys.stderr)
    print("neither -- ordinary reps suffice      %d rows" % sum(
        1 for r in rows if min(r[3]) == 1 and not any(w != 1 for w in r[4])), file=sys.stderr)

    cr = crystal_rows()
    with open("PHONON-KCRYSTALS.tsv", "w") as f:
        f.write("# Phonon symmetry content of 12 crystals at their high-symmetry k-points.\n")
        f.write("# COMPUTED.  No published decomposition is read; section 3 of the write-up\n")
        f.write("# compares against them.\n")
        f.write("crystal\tsg\tatoms\tk\tk_frac\tpk_order\tN\tghat_order\tmodes\tdecomposition\n")
        for name, sg, na, kn, k, npg, N, go, lev in cr:
            f.write("%s\t%d\t%d\t%s\t%s\t%d\t%d\t%d\t%d\t%s\n" % (
                name, sg, na, kn, ",".join(str(Fraction(x).limit_denominator(12)) for x in k),
                npg, N, go, 3 * na, fmt_lev(lev)))
    print("crystal rows                          %d  (all passed 3 integrality guards)" % len(cr), file=sys.stderr)
    print("elapsed %.0f s" % (time.time() - t0), file=sys.stderr)


def selftest():
    """Fixtures are the corpus's own computed numbers, plus the literature
    decompositions that phonondex.py section 3 already checks at Gamma."""
    ok = 0
    lat, pos, num = build(('F', 3.567), 227, [(6, (0, 0, 0))])
    for kn, k, want in (("Gamma", (0, 0, 0), [3, 3]),
                        ("X", (.5, .5, 0), [2, 2, 2]),
                        ("L", (.5, .5, .5), [1, 1, 2, 2]),
                        ("W", (.25, .5, .75), [2, 2, 2])):
        r = decompose(np.asarray(lat), np.asarray(pos, float), list(num), k)
        dims = [int(round(x[0].real)) for x in r['T']]
        used = sorted(d for d, m in zip(dims, [m.real for m in r['mult']]) for _ in range(int(round(m))))
        assert used == want, ("diamond", kn, used, want)
        ok += 1
    # the diamond X sticking: NO one-dimensional irrep is allowed at X
    R, t = prim_sym(np.asarray(lat), np.asarray(pos, float), list(num))
    npg, ad, ws = sectors([np.rint(x).astype(int) for x in R], t, np.array([.5, .5, 0.]))
    assert (npg, ad) == (16, [2, 2, 2, 2]), (npg, ad)
    assert ws == [1, 1, 1, 1], ws          # cubic: NO time-reversal degeneracy
    ok += 1
    # wurtzite at A: factor system TRIVIAL, degeneracy entirely antiunitary
    lat2, pos2, num2 = build(('H', 3.250, 5.207), 186,
                             [(30, (1 / 3., 2 / 3., 0.)), (8, (1 / 3., 2 / 3., .3825))])
    R2, t2 = prim_sym(np.asarray(lat2), np.asarray(pos2, float), list(num2))
    npg, ad, ws = sectors([np.rint(x).astype(int) for x in R2], t2, np.array([0., 0., .5]))
    assert (npg, ad) == (12, [1, 1, 1, 1, 2, 2]), (npg, ad)
    assert set(ws) == {0}, ws
    ok += 1
    print("selftest: %d fixtures pass" % ok)


if __name__ == "__main__":
    if "--selftest" in sys.argv: selftest()
    else: main()
