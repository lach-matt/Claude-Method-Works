#!/usr/bin/env python3
"""
kpoint_derive.py -- the derivation behind captures/KPOINTS-HIGHSYM.tsv.

    python3 kpoint_derive.py          rebuild the capture

Needs numpy and spglib; z3 is OPTIONAL and adds one column (see `is_coboundary`).
Nothing is vendored and no table is read.

IT IMPORTS `primitive_ops`, `char_table` and `K` FROM `phonon_derive` RATHER THAN
COPYING THEM.  The Gamma-point derivation is the store of record for the
primitive-basis transformation and for Burnside's class-algebra method; this
file adds the reciprocal-space half and the PROJECTIVE representation theory
that k != Gamma needs.

METHOD, in the order the code runs it:

 1.  `recip_ops`   the point group acting on k is {(R^-1)^T : R in the
     primitive-basis rotations}.  Integral, because R is integral with
     det +-1, so k stays in fractional coordinates of the primitive
     RECIPROCAL basis and "modulo a reciprocal lattice vector" is `% 1`.

 2.  `candidates`  THE ISOLATED POINTS, GRID-FREE AND EXHAUSTIVE.  k is a
     0-dimensional stratum of the stabiliser stratification iff the stacked
     matrix [R - I : R in G_k] has rank 3.  Rank grows by at least one per
     row block, so SOME subset A of G_k with |A| <= 3 already has rank 3, and
     then k lies in the lattice L_A = {k : (R-I)k in Z^3 for all R in A},
     which contains Z^3 with finite index.  So sweeping every subset of the
     point group of size <= 3 with rank 3, and enumerating L_A / Z^3 exactly
     by Hermite normal form, yields a FINITE SUPERSET of every isolated
     point.  No grid, no truncation, no convergence question.

 3.  `little`, `factor_system`  the little group and its multiplier.  With
     D^k({R|t}) = exp(-2 pi i k.t) Gamma(R),

         Gamma(R1) Gamma(R2) = omega(R1,R2) Gamma(R1 R2),
         omega(R1,R2) = exp(2 pi i K1 . t2),   K1 = k - R1^T k in Z^3.

     K1 is integral exactly because R1 is in the little co-group.  omega is
     trivial iff every K1.t2 is an integer -- which is automatic when the
     group is symmorphic (all t = 0) or when no umklapp occurs (all K1 = 0).

 4.  `cover`, `table_from_mult`  THE PROJECTIVE OBSTRUCTION, DISCHARGED.  Let
     m be the order of the omega values.  The central extension

         (R1,j1)(R2,j2) = (R1 R2, j1 + j2 + w(R1,R2) mod m)

     is an ORDINARY finite group of order m|H|.  Burnside's class-algebra
     method -- the same one phonon_derive uses, generalised from 3x3 matrices
     to an abstract multiplication table -- gives its character table, and
     the irreps in which the central element (E,1) acts as exp(2 pi i / m)
     are exactly the omega-projective irreps of H.  So the small reps at any
     k of any space group are computed by ordinary character theory.

 5.  `is_coboundary`  whether the multiplier is trivial, decided rather than
     guessed.  omega = delta(mu) forces |mu| = 1 and mu(a)^|H| = prod_b
     omega(a,b), so mu is valued in the (m|H|)-th roots of unity and the
     question is a linear system over Z_{m|H|}, which z3 decides.

GUARDS.  Every row carries sum(d^2) = |H| over the selected sector, which is
the projective analogue of the check that caught five bugs at Gamma.  The
z3 verdict and the "do the projective dimensions differ from the ordinary
ones" test are computed independently and compared.
"""
import sys, math, time, itertools, collections
from fractions import Fraction as F
import numpy as np
import spglib

from phonon_derive import primitive_ops, hallmap, char_table, K

try:
    import z3
    HAVE_Z3 = True
except Exception:
    HAVE_Z3 = False


# --------------------------------------------------------------- reciprocal
def recip_ops(R):
    """direct primitive-basis rotations -> reciprocal primitive-basis rotations."""
    out = []
    for M in R:
        A = np.asarray(M, float)
        B = np.linalg.inv(A).T
        Bi = np.rint(B).astype(np.int64)
        if np.max(np.abs(B - Bi)) > 1e-8:
            raise RuntimeError("non-integral reciprocal rotation")
        out.append(Bi)
    return out


def point_group(R):
    seen = {}
    for M in recip_ops(R):
        seen[K(M)] = M
    return list(seen.values())


def inv3(A):
    det = (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
    C = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            m = [[A[r][c] for c in range(3) if c != j] for r in range(3) if r != i]
            C[j][i] = F(m[0][0]*m[1][1]-m[0][1]*m[1][0]) * ((-1)**(i+j)) / det
    return C


def hnf_cols(M):
    """column-style Hermite normal form of an integer 3 x N; same column lattice."""
    n = len(M)
    cols = [[int(M[i][j]) for i in range(n)] for j in range(len(M[0]))]
    c0 = 0
    for i in range(n):
        while True:
            nz = [j for j in range(c0, len(cols)) if cols[j][i] != 0]
            if len(nz) <= 1:
                break
            nz.sort(key=lambda j: abs(cols[j][i]))
            j0 = nz[0]
            for j in nz[1:]:
                q = cols[j][i] // cols[j0][i]
                for t in range(n):
                    cols[j][t] -= q * cols[j0][t]
        nz = [j for j in range(c0, len(cols)) if cols[j][i] != 0]
        if not nz:
            continue
        j0 = nz[0]
        if cols[j0][i] < 0:
            cols[j0] = [-x for x in cols[j0]]
        cols[c0], cols[j0] = cols[j0], cols[c0]
        c0 += 1
    H = [[0]*n for _ in range(n)]
    for j in range(min(c0, n)):
        for i in range(n):
            H[i][j] = cols[j][i]
    return H


def rank3(Rs):
    rows = []
    for R in Rs:
        rows.extend((np.asarray(R, np.int64) - np.eye(3, dtype=np.int64)).tolist())
    return int(np.linalg.matrix_rank(np.array(rows, float)))


def lattice_points(Rs):
    """{k mod 1 : (R-I)k in Z^3 for all R in Rs}.  Exact; Rs must have rank 3."""
    rows = []
    for R in Rs:
        rows.extend((np.asarray(R, np.int64) - np.eye(3, dtype=np.int64)).tolist())
    M = np.array(rows, dtype=np.int64).T
    H = np.array(hnf_cols(M), dtype=np.int64)
    d = [int(H[i][i]) for i in range(3)]
    if any(x == 0 for x in d):
        return set()
    HT = [[F(int(H[j][i])) for j in range(3)] for i in range(3)]
    iv = inv3(HT)
    out = set()
    for n0 in range(abs(d[0])):
        for n1 in range(abs(d[1])):
            for n2 in range(abs(d[2])):
                n = (n0, n1, n2)
                out.add(tuple((sum(iv[i][j]*n[j] for j in range(3))) % 1
                              for i in range(3)))
    return out


def candidates(PG):
    """EVERY k that is an isolated fixed point of some subgroup.  Grid-free."""
    n = len(PG)
    single = [i for i in range(n) if rank3([PG[i]]) == 3]
    cand = set()
    for i in single:
        cand |= lattice_points([PG[i]])
    low = [i for i in range(n) if i not in single]
    pairs = set()
    for a, b in itertools.combinations(low, 2):
        if rank3([PG[a], PG[b]]) == 3:
            pairs.add((a, b))
            cand |= lattice_points([PG[a], PG[b]])
    for a, b, c in itertools.combinations(low, 3):
        if (a, b) in pairs or (a, c) in pairs or (b, c) in pairs:
            continue
        if rank3([PG[a], PG[b], PG[c]]) == 3:
            cand |= lattice_points([PG[a], PG[b], PG[c]])
    return cand


def stab(PG, k):
    kk = [F(x) for x in k]
    out = []
    for i, R in enumerate(PG):
        q = [sum(int(R[r][c])*kk[c] for c in range(3)) for r in range(3)]
        if all((q[r]-kk[r]).denominator == 1 for r in range(3)):
            out.append(i)
    return tuple(out)


def star(PG, k):
    kk = [F(x) for x in k]
    return frozenset(tuple((sum(int(R[r][c])*kk[c] for c in range(3))) % 1
                           for r in range(3)) for R in PG)


# ------------------------------------------------- little group and multiplier
def little(k, R):
    kk = [F(x) for x in k]
    out = []
    for i in range(len(R)):
        RT = np.asarray(R[i], np.int64).T
        q = [sum(int(RT[r][c])*kk[c] for c in range(3)) for r in range(3)]
        if all((q[r]-kk[r]).denominator == 1 for r in range(3)):
            out.append(i)
    return out


def factor_system(k, R, T, idx):
    """omega(a,b) = exp(2 pi i w[a][b] / m),  w integral."""
    kk = [F(x) for x in k]
    n = len(idx)
    Kv = []
    for i in idx:
        RT = np.asarray(R[i], np.int64).T
        q = [sum(int(RT[r][c])*kk[c] for c in range(3)) for r in range(3)]
        Kv.append([int(kk[r]-q[r]) for r in range(3)])
    tt = [[F(x).limit_denominator(10**6) for x in T[j]] for j in idx]
    ph = [[sum(F(Kv[a][r])*tt[b][r] for r in range(3)) for b in range(n)]
          for a in range(n)]
    m = 1
    for row in ph:
        for x in row:
            m = m * x.denominator // math.gcd(m, x.denominator)
    return m, [[int((ph[a][b]*m) % m) for b in range(n)] for a in range(n)]


def prod_table(R, idx):
    key = {K(np.asarray(R[i], np.int64)): a for a, i in enumerate(idx)}
    n = len(idx)
    return [[key[K(np.asarray(R[idx[a]], np.int64) @ np.asarray(R[idx[b]], np.int64))]
             for b in range(n)] for a in range(n)]


def cover(pt, m, w, ident):
    """central extension by Z_m; element (a,j) is indexed a*m+j."""
    n = len(pt)
    N = n*m
    mul = [[0]*N for _ in range(N)]
    for a in range(n):
        for j in range(m):
            row = mul[a*m+j]
            for b in range(n):
                p = pt[a][b]*m
                wab = w[a][b]
                for l in range(m):
                    row[b*m+l] = p + ((j+l+wab) % m)
    return mul, ident*m, N


# ------------------------------------ Burnside on an abstract multiplication table
def _try(cls, N, order, seed):
    nc = len(cls)
    A = np.tensordot(np.random.default_rng(seed).normal(size=nc), N, axes=(0, 0))
    _w, V = np.linalg.eig(A)
    out = []
    for t in range(nc):
        v = V[:, t]
        if abs(v[0]) < 1e-9:
            return None
        om = v/v[0]
        base = np.array([om[i]/len(cls[i]) for i in range(nc)])
        s2 = sum(len(cls[i])*abs(base[i])**2 for i in range(nc))
        if abs(s2) < 1e-12:
            return None
        chi = base*np.sqrt(order/s2)
        if np.real(chi[0]) < 0:
            chi = -chi
        out.append(chi)
    T = np.array(out)
    dims = [complex(x[0]) for x in T]
    if any(abs(d.imag) > 1e-6 or abs(d.real-round(d.real)) > 1e-6 for d in dims):
        return None
    if abs(sum(round(d.real)**2 for d in dims) - order) > 1e-6:
        return None
    for r in range(nc):
        for q in range(nc):
            ip = sum(len(cls[i])*T[r][i]*np.conj(T[q][i]) for i in range(nc))/order
            if abs(ip - (1.0 if r == q else 0.0)) > 1e-6:
                return None
    return T


def table_from_mult(mul, e):
    """character table of a finite group given by its multiplication table."""
    n = len(mul)
    inv = [0]*n
    for a in range(n):
        for b in range(n):
            if mul[a][b] == e:
                inv[a] = b
                break
    seen, cls = set(), []
    for a in range(n):
        if a in seen:
            continue
        c = sorted({mul[mul[g][a]][inv[g]] for g in range(n)})
        cls.append(c)
        seen |= set(c)
    cls.sort(key=lambda c: 0 if c[0] == e else 1)
    nc = len(cls)
    co = [0]*n
    for ci, c in enumerate(cls):
        for g in c:
            co[g] = ci
    N = np.zeros((nc, nc, nc))
    for i in range(nc):
        for j in range(nc):
            cnt = np.zeros(nc)
            for a in cls[i]:
                ma = mul[a]
                for b in cls[j]:
                    cnt[co[ma[b]]] += 1
            for kk in range(nc):
                N[i][j][kk] = cnt[kk]/len(cls[kk])
    for seed in range(400):
        T = _try(cls, N, n, seed)
        if T is not None:
            return cls, T, co
    raise RuntimeError("no valid character table, |G|=%d" % n)


def small_reps(k, R, T):
    """(|H|, m, sorted small-rep dims, sum d^2).  The projective computation."""
    idx = little(k, R)
    m, w = factor_system(k, R, T, idx)
    pt = prod_table(R, idx)
    I = K(np.eye(3, dtype=np.int64))
    ident = [a for a, i in enumerate(idx) if K(np.asarray(R[i], np.int64)) == I][0]
    mul, e, N = cover(pt, m, w, ident)
    cls, Tab, co = table_from_mult(mul, e)
    z = ident*m + (1 % m)
    zeta = complex(math.cos(2*math.pi/m), math.sin(2*math.pi/m))
    sec = [r for r in range(len(Tab))
           if abs(Tab[r][co[z]] - zeta*Tab[r][co[e]]) < 1e-6]
    dims = sorted(int(round(float(np.real(Tab[r][co[e]])))) for r in sec)
    return len(idx), m, dims, sum(d*d for d in dims), idx, w, pt


def is_coboundary(m, w, pt):
    """decide omega = delta(mu).  mu is valued in mu_{m|H|}; z3 solves over Z_M."""
    if not HAVE_Z3:
        return None
    n = len(w)
    M = m*n
    s = z3.Solver()
    v = [z3.Int('v%d' % a) for a in range(n)]
    for a in range(n):
        s.add(v[a] >= 0, v[a] < M)
    for a in range(n):
        for b in range(n):
            s.add((v[a]+v[b]-v[pt[a][b]]-w[a][b]*n) % M == 0)
    return s.check() == z3.sat


# --------------------------------------------------------------------- sweep
def system(sg):
    for lim, nm in ((2, "triclinic"), (15, "monoclinic"), (74, "orthorhombic"),
                    (142, "tetragonal"), (167, "trigonal"), (194, "hexagonal"),
                    (230, "cubic")):
        if sg <= lim:
            return nm


def bravais(sg, sym):
    s = system(sg)
    c = sym[0]
    base = {"triclinic": "a", "monoclinic": "m", "orthorhombic": "o",
            "tetragonal": "t", "trigonal": "h", "hexagonal": "h",
            "cubic": "c"}[s]
    if c == "R":
        return "hR"
    cent = {"P": "P", "A": "S", "B": "S", "C": "S", "I": "I", "F": "F"}[c]
    if base == "h":
        return "hP"
    return base + cent


def fmt(k):
    return ",".join("%d/%d" % (F(x).numerator, F(x).denominator) for x in k)


def main():
    HN = hallmap()
    t0 = time.time()
    rows = []
    disagree = []
    polar = []
    for sg in range(1, 231):
        P, R, T, nc = primitive_ops(sg, HN)
        st = spglib.get_spacegroup_type(HN[sg])
        sym = st.international_short if hasattr(st, "international_short") else st["international_short"]
        pgs = st.pointgroup_international if hasattr(st, "pointgroup_international") else st["pointgroup_international"]
        PG = point_group(R)
        cand = candidates(PG)
        stars = {}
        for k in cand:
            stars.setdefault(star(PG, k), k)
        if not stars:
            polar.append((sg, pgs))
        for s, k in sorted(stars.items(),
                           key=lambda kv: (-len(stab(PG, kv[1])), fmt(kv[1]))):
            nH, m, dims, ss, idx, w, pt = small_reps(k, R, T)
            if ss != nH:
                raise RuntimeError("sum d^2 != |H| at sg %d k %s" % (sg, fmt(k)))
            _cls, Tab = char_table([np.asarray(R[i], float) for i in idx])
            odims = sorted(int(round(float(np.real(x[0])))) for x in Tab)
            stick = 0 if dims == odims else 1
            cb = is_coboundary(m, w, pt)
            if cb is not None and (cb == bool(stick)):
                disagree.append((sg, fmt(k)))
            rows.append((sg, system(sg), bravais(sg, sym), len(PG), fmt(k),
                         len(s), nH, m, "" if cb is None else int(not cb),
                         len(dims), "+".join(str(d) for d in dims), max(dims),
                         stick))
        if sg % 20 == 0:
            print("  sg %d  %.0fs  %d rows" % (sg, time.time()-t0, len(rows)),
                  file=sys.stderr)
    print("\nswept 230 space groups in %.1f s" % (time.time()-t0), file=sys.stderr)
    print("isolated k-stars          : %d" % len(rows), file=sys.stderr)
    print("space groups with none    : %d" % len(polar), file=sys.stderr)
    print("  their point groups      : %s"
          % sorted({p for _s, p in polar}), file=sys.stderr)
    print("z3 / dimension disagreements: %d" % len(disagree), file=sys.stderr)
    with open("KPOINTS-HIGHSYM.tsv", "w") as f:
        f.write("sg\tsystem\tbravais\tpg_order\tk\tstar\tlittle_order\tm"
                "\tnontrivial_multiplier\tn_smallreps\tdims\tmax_dim\tsticking\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r)+"\n")
    print("wrote KPOINTS-HIGHSYM.tsv", file=sys.stderr)




# ======================================================================
# THE ADDITIVITY MEASUREMENT.  Does the Gamma-point generating table
# survive to k != 0?  Two questions, and they have different answers.
#
#   (i)  do ORBIT contributions still ADD?  Yes, and it is a theorem: the
#        character of the mechanical representation is a sum over atoms
#        mapped to themselves, orbits are disjoint and invariant, so the
#        representation is block diagonal by orbit at EVERY k.  Verified
#        numerically here as well.
#
#   (ii) is an orbit's contribution a function of its SITE-SYMMETRY TYPE,
#        as it is at Gamma?  NO.  The phase exp(-2 pi i k . v) depends on
#        the site's POSITION through v = R x + t - x, not on its
#        stabiliser.  P-1's eight inversion centres -- ONE member in
#        phonondex, because at Gamma they contribute identically -- split
#        4/4 at k = (1/2,0,0).
# ======================================================================
def orbit_of(R, T, p):
    O = []
    for Ri, ti in zip(R, T):
        q = tuple((sum(int(np.asarray(Ri, np.int64)[r][c])*p[c] for c in range(3))
                   + F(ti[r]).limit_denominator(10**6)) % 1 for r in range(3))
        if q not in O:
            O.append(q)
    return O


def mech_decomp(k, R, T, O):
    """(dims, multiplicities) of ONE orbit's mechanical rep at k."""
    idx = little(k, R)
    m, w = factor_system(k, R, T, idx)
    pt = prod_table(R, idx)
    I = K(np.eye(3, dtype=np.int64))
    ident = [a for a, i in enumerate(idx) if K(np.asarray(R[i], np.int64)) == I][0]
    mul, e, N = cover(pt, m, w, ident)
    cls, Tab, co = table_from_mult(mul, e)
    z = ident*m + (1 % m)
    zeta = complex(math.cos(2*math.pi/m), math.sin(2*math.pi/m))
    sec = [r for r in range(len(Tab))
           if abs(Tab[r][co[z]] - zeta*Tab[r][co[e]]) < 1e-6]
    kk = [F(x) for x in k]
    chi = []
    for a, i in enumerate(idx):
        Ri = np.asarray(R[i], np.int64)
        ti = [F(x).limit_denominator(10**6) for x in T[i]]
        s = 0j
        for p in O:
            q = [sum(int(Ri[r][c])*p[c] for c in range(3)) + ti[r] for r in range(3)]
            v = [q[r]-p[r] for r in range(3)]
            if all(x.denominator == 1 for x in v):
                ph = -2*math.pi*float(sum(kk[r]*v[r] for r in range(3)))
                s += complex(math.cos(ph), math.sin(ph))
        ph2 = 2*math.pi*float(sum(kk[r]*ti[r] for r in range(3)))
        chi.append(s*complex(math.cos(ph2), math.sin(ph2))*float(np.trace(Ri)))
    dims, mult = [], []
    for r in sec:
        v = sum(chi[a]*np.conj(Tab[r][co[a*m+0]]) for a in range(len(idx)))/len(idx)
        v = complex(v)
        if abs(v.imag) > 1e-6 or abs(v.real-round(v.real)) > 1e-6:
            raise RuntimeError("non-integral multiplicity")
        dims.append(int(round(float(np.real(Tab[r][co[e]])))))
        mult.append(int(round(v.real)))
    return dims, mult


def additivity():
    HN = hallmap()
    out = []
    half = (F(0), F(1, 2))
    for sg in (2, 47, 123):
        P, R, T, nc = primitive_ops(sg, HN)
        PG = point_group(R)
        sites = [(a, b, c) for a in half for b in half for c in half]
        for k in ((F(0), F(0), F(0)), (F(1, 2), F(0), F(0))):
            for p in sites:
                O = orbit_of(R, T, p)
                S = [i for i in range(len(R))
                     if orbit_of(R, T, p) and
                     all((sum(int(np.asarray(R[i], np.int64)[r][c])*p[c]
                              for c in range(3))
                          + F(T[i][r]).limit_denominator(10**6) - p[r]) % 1 == 0
                         for r in range(3))]
                d, mu = mech_decomp(k, R, T, O)
                out.append((sg, ",".join("%d/%d" % (F(x).numerator, F(x).denominator)
                                         for x in p), len(S), len(O),
                            ",".join("%d/%d" % (F(x).numerator, F(x).denominator)
                                     for x in k),
                            "+".join(str(x) for x in d),
                            "+".join(str(x) for x in mu),
                            sum(a*b for a, b in zip(d, mu))))
        # (i) orbits ADD: total over two distinct orbits == sum of the two
        for k in ((F(1, 2), F(0), F(0)),):
            A = orbit_of(R, T, sites[0])
            B = orbit_of(R, T, sites[-1])
            if set(A) & set(B):
                continue
            dA, mA = mech_decomp(k, R, T, A)
            dB, mB = mech_decomp(k, R, T, B)
            dU, mU = mech_decomp(k, R, T, A+B)
            assert dA == dB == dU and [x+y for x, y in zip(mA, mB)] == mU, sg
    with open("KPOINTS-ADDITIVITY.tsv", "w") as f:
        f.write("sg\tsite\tsite_order\tmultiplicity\tk\tdims\tmult\tmodes\n")
        for r in out:
            f.write("\t".join(str(x) for x in r)+"\n")
    print("wrote KPOINTS-ADDITIVITY.tsv (%d rows)" % len(out), file=sys.stderr)
    return out


# ======================================================================
# THE CROSS-CHECK.  Setyawan & Curtarolo (2010), Comput. Mater. Sci. 49,
# 299 define the high-symmetry k-points of every Bravais lattice.  THEIR
# COORDINATES ARE USED ONLY TO CHECK AND NEVER TO BUILD -- they enter as
# CARTESIAN vectors in units of 2 pi / a, which is convention-free, and
# are pushed into whatever primitive reciprocal basis `hnf_basis` happens
# to have produced.  Nothing downstream reads them.
# ======================================================================
SETYAWAN = {
    225: [("Gamma", (0, 0, 0)), ("X", (0, 1, 0)),
          ("L", (F(1, 2), F(1, 2), F(1, 2))), ("W", (F(1, 2), 1, 0)),
          ("K", (F(3, 4), F(3, 4), 0)), ("U", (F(1, 4), 1, F(1, 4)))],
    229: [("Gamma", (0, 0, 0)), ("H", (0, 0, 1)),
          ("P", (F(1, 2), F(1, 2), F(1, 2))), ("N", (F(1, 2), F(1, 2), 0))],
    221: [("Gamma", (0, 0, 0)), ("X", (0, F(1, 2), 0)),
          ("M", (F(1, 2), F(1, 2), 0)), ("R", (F(1, 2), F(1, 2), F(1, 2)))],
}

HOLOHEDRAL = (("aP", 2, "P-1"), ("mP", 10, "P2/m"), ("mS", 12, "C2/m"),
              ("oP", 47, "Pmmm"), ("oS", 65, "Cmmm"), ("oF", 69, "Fmmm"),
              ("oI", 71, "Immm"), ("tP", 123, "P4/mmm"), ("tI", 139, "I4/mmm"),
              ("hR", 166, "R-3m"), ("hP", 191, "P6/mmm"), ("cP", 221, "Pm-3m"),
              ("cF", 225, "Fm-3m"), ("cI", 229, "Im-3m"))


def crosscheck():
    HN = hallmap()
    out = []
    for sg in sorted(SETYAWAN):
        P, R, T, nc = primitive_ops(sg, HN)
        PG = point_group(R)
        Pf = [[F(x).limit_denominator(10**6) for x in row] for row in P]
        A = inv3(Pf)
        AT = [[A[j][i] for j in range(3)] for i in range(3)]
        ATi = inv3(AT)
        mine = {}
        for k in candidates(PG):
            mine.setdefault(star(PG, k), k)
        seen = set()
        for nm, c in SETYAWAN[sg]:
            kp = tuple((sum(ATi[i][j]*F(c[j]) for j in range(3))) % 1
                       for i in range(3))
            s = star(PG, kp)
            H = stab(PG, kp)
            dim = 3 - rank3([PG[i] for i in H])
            verdict = ("FOUND" if s in mine else
                       "NOT-ISOLATED" if dim > 0 else "MISSED")
            if s in seen:
                verdict += " (same star as an earlier row)"
            seen.add(s)
            out.append((sg, nm,
                        ",".join("%d/%d" % (F(x).numerator, F(x).denominator)
                                 for x in c),
                        fmt(kp), len(s), len(H), dim, verdict))
        for s, k in mine.items():
            if s not in seen:
                out.append((sg, "-", "", fmt(k), len(s), len(stab(PG, k)), 0,
                            "EXTRA -- isolated but not in the table"))
    with open("KPOINTS-CHECK.tsv", "w") as f:
        f.write("sg\tname\tcartesian_2pi_over_a\tk_primitive\tstar\tlittle_order"
                "\tdim_fixed_space\tverdict\n")
        for r in out:
            f.write("\t".join(str(x) for x in r)+"\n")
    print("wrote KPOINTS-CHECK.tsv (%d rows)" % len(out), file=sys.stderr)
    return out


def gridscan(PG, n):
    """the GRID method: stabiliser types on a 1/n grid, grouped by conjugacy."""
    g = len(PG)
    A = np.array(PG, dtype=np.int64)
    idxK = {K(M): i for i, M in enumerate(PG)}
    invp = [idxK[K(np.rint(np.linalg.inv(np.asarray(M, float))).astype(np.int64))]
            for M in PG]
    conj = np.zeros((g, g), dtype=np.int64)
    for x in range(g):
        for s in range(g):
            conj[x][s] = idxK[K(A[x] @ A[s] @ A[invp[x]])]
    P = np.array([[a, b, c] for a in range(n) for b in range(n)
                  for c in range(n)], dtype=np.int64)
    fix = np.zeros((len(P), g), dtype=bool)
    for i in range(g):
        q = (P @ (A[i]-np.eye(3, dtype=np.int64)).T) % n
        fix[:, i] = np.all(q == 0, axis=1)
    sig = {}
    for j in range(len(P)):
        sig.setdefault(tuple(np.flatnonzero(fix[j]).tolist()), []).append(j)
    types, iso = set(), set()
    for s, js in sig.items():
        types.add(min(tuple(sorted(conj[x][list(s)].tolist())) for x in range(g)))
        if 3 - rank3([PG[i] for i in s]) == 0:
            for j in js:
                iso.add(star(PG, tuple(F(int(x), n) for x in P[j])))
    return types, iso, len(P)


def convergence():
    """the grid at 1/12 and 1/24 against the exact enumeration, all 14 lattices."""
    HN = hallmap()
    out = []
    for bl, sg, nm in HOLOHEDRAL:
        P, R, T, nc = primitive_ops(sg, HN)
        PG = point_group(R)
        ex = set()
        for k in candidates(PG):
            ex.add(star(PG, k))
        r = [gridscan(PG, n) for n in (12, 24)]
        out.append((bl, sg, nm, len(PG), len(r[0][0]), len(r[0][1]),
                    len(r[1][0]), len(r[1][1]), len(ex),
                    int(r[0][1] == ex), int(r[1][1] == ex)))
    with open("KPOINTS-GRID.tsv", "w") as f:
        f.write("bravais\tsg\tsymbol\tpg_order\ttypes12\tiso12\ttypes24\tiso24"
                "\texact_iso\tgrid12_exact\tgrid24_exact\n")
        for r in out:
            f.write("\t".join(str(x) for x in r)+"\n")
    print("wrote KPOINTS-GRID.tsv (%d rows)" % len(out), file=sys.stderr)
    return out


# ======================================================================
# THE MERGE THAT WAS MEASURED AND THEN REFUSED.  kpointdex.py section 5.
# Two k-stars are indistinguishable on symmetry content when some point-
# group element conjugates one little co-group onto the other AND the
# pulled-back multiplier is cohomologous to the original -- both decided,
# the second by z3 on the difference cocycle.  It merges 870 to 485.
# The index does NOT take the merge: at k != 0 the crystal momentum is the
# mode's own quantum number, and a merge would flatten it.
# ======================================================================
def symmetry_content_merge():
    HN = hallmap()
    total = 0
    for sg in range(1, 231):
        P, R, T, nc = primitive_ops(sg, HN)
        PG = point_group(R)
        idxK = {K(np.asarray(R[i], np.int64)): i for i in range(len(R))}
        items = []
        st = {}
        for k in candidates(PG):
            st.setdefault(star(PG, k), k)
        for s, k in st.items():
            idx = little(k, R)
            m, w = factor_system(k, R, T, idx)
            items.append((idx, m, w, prod_table(R, idx),
                          tuple(sorted(K(np.asarray(R[i], np.int64)) for i in idx))))
        reps = []
        for idx, m, w, pt, Hs in items:
            placed = False
            for idx2, m2, w2, pt2, H2 in reps:
                for g in range(len(R)):
                    Rg = np.asarray(R[g], np.int64)
                    Rgi = np.rint(np.linalg.inv(Rg)).astype(np.int64)
                    img = tuple(sorted(K(Rg @ np.asarray(R[idxK[h]], np.int64) @ Rgi)
                                       for h in Hs))
                    if img != H2:
                        continue
                    try:
                        sig = [[b for b in range(len(idx2))
                                if K(np.asarray(R[idx2[b]], np.int64)) ==
                                K(Rg @ np.asarray(R[idx[a]], np.int64) @ Rgi)][0]
                               for a in range(len(idx))]
                    except IndexError:
                        continue
                    M = m*m2//math.gcd(m, m2)
                    wd = [[(w[a][b]*(M//m) - w2[sig[a]][sig[b]]*(M//m2)) % M
                           for b in range(len(idx))] for a in range(len(idx))]
                    if is_coboundary(M, wd, pt):
                        placed = True
                        break
                if placed:
                    break
            if not placed:
                reps.append((idx, m, w, pt, Hs))
        total += len(reps)
    print("symmetry-content merge: 870 -> %d  (MEASURED, and REFUSED)" % total,
          file=sys.stderr)
    return total


if __name__ == "__main__":
    main()
    additivity()
    crosscheck()
    convergence()
    symmetry_content_merge()
