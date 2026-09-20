#!/usr/bin/env python3
"""
phonon_kpoints_derive.py -- the derivation behind captures/PHONON-KPOINTS.tsv.

    python3 phonon_kpoints_derive.py            rebuild the capture
    python3 phonon_kpoints_derive.py --selftest fixtures (needs numpy+spglib)

Needs numpy and spglib, neither vendored.  It IMPORTS `K`, `hallmap` and
`primitive_ops` from `phonon_derive` rather than copying them -- the Gamma-point
derivation is the store of record for the primitive-basis transformation.

THIS IS THE SECOND OF TWO INDEPENDENT IMPLEMENTATIONS.  The first is
`kpoint_derive.py`, which writes `KPOINTS-HIGHSYM.tsv` and is what `kpointdex.py`
seats; this one is the cross-check, and the two share no code below
`phonon_derive`.  They are compared in `kpointdex.py` section 5a and NEVER
merged.  The comparison is the point: a figure both produce independently is
worth more than either alone, and the one place they still differ -- the
reported factor order at space groups 180 and 181 -- is recorded there as a
definition difference rather than smoothed away.

WHY THIS FILE EXISTS SEPARATELY FROM ITS CAPTURE, AND WHAT IT CORRECTS.  The
capture was first written by a scratchpad script that was never banked, so the
repository held the numbers and not the route to them.  Banking it surfaced the
bug below, which had been misdiagnosed three times.

    THE MULTIPLIER MUST BE A 2-COCYCLE, AND THE FIRST ONE WAS NOT.

An earlier `omega` took the reciprocal lattice vector as

    g = R1^{-T} k - k          (WRONG)

which is integral for R1 in the little co-group, so every integrality check it
met passed.  It is not a 2-cocycle.  Tested directly against the associativity
identity

    phi(a,b) + phi(ab,c)  ==  phi(b,c) + phi(a,bc)   (mod 1)

at space groups 199, 212 and 230 it deviates by EXACTLY 1/2, and the object
built from it is not a group: associativity and inverses both fail.  Eighteen
k-points in nine cubic non-symmorphic groups (198, 199, 205, 206, 212, 213, 214,
220, 230) therefore came out UNRESOLVED.

THREE DIAGNOSES WERE WRONG BEFORE THE FOURTH WAS RIGHT, and they are recorded
because each one looked reasonable:

  1. "Burnside's randomised eigenvector search does not converge."  WITHDRAWN.
     Reseeding did not help.
  2. "A real random combination cannot split a complex-conjugate eigenvalue
     pair."  WITHDRAWN.  A complex combination did not help either.
  3. "A deterministic Dixon-Schneider simultaneous diagonalisation is the
     remedy."  WITHDRAWN.  It was written, and it failed IDENTICALLY -- it
     recovered FEWER irreps than there were conjugacy classes, which is
     impossible for a finite group.  That impossibility is what pointed at the
     input rather than the algorithm: Burnside was correctly refusing a
     malformed group.

Four conventions were then tested against the cocycle identity:

    g = R1^{-T} k - k   cocycle: NO    worst deviation 0.5
    K = k - R1^T k      cocycle: YES   worst deviation 0
    K = R1^T k - k      cocycle: YES   worst deviation 0
    g = k - R1^{-T} k   cocycle: NO    worst deviation 0.5

This file uses `K1 = k - R1^T k`, which is also the convention `kpoint_derive.py`
arrived at independently.  Every central extension now tests as a valid GROUP,
and the sweep resolves ALL 870 members with sum(d^2) = |G_k| everywhere.

WHAT A ROW IS.  One isolated high-symmetry k-STAR of one space group:

    sg  system  pg_order  little_group  star  factor_order  n_small_reps
        max_dim  dims

`little_group` is |G_k| for the little co-group, `star` the number of arms,
`factor_order` the order of the image of the multiplier omega (see section 5a
for why that differs from kpoint_derive.py's `m` at sg 180 and 181), and `dims`
the small-representation dimensions, largest first.

WHAT THIS FILE DOES NOT CLAIM.  The 1/12 grid below is an ENUMERATION over a
mesh, not the grid-free Hermite-normal-form argument `kpoint_derive.py` runs.
It is converged -- 1/12 and 1/24 give the same stars -- but converged is not
proved, and that is exactly why the two implementations are kept apart.  The
proof lives in `kpoint_derive.py`; this file is the measurement that agrees
with it.
"""
import sys, os, time, collections, cmath
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from phonon_derive import K, hallmap, primitive_ops

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "PHONON-KPOINTS.tsv")

SYSTEMS = ((2, "triclinic"), (15, "monoclinic"), (74, "orthorhombic"),
           (142, "tetragonal"), (167, "trigonal"), (194, "hexagonal"),
           (230, "cubic"))


def system(sg):
    for lim, nm in SYSTEMS:
        if sg <= lim:
            return nm


def canon_star(Rt, k):
    """The star of k as a canonical sorted tuple, modulo a reciprocal vector."""
    S = []
    for M in Rt:
        q = M @ k
        q = q - np.rint(q)
        q = np.round(q, 6) % 1.0
        t = tuple(np.round(q, 6))
        if t not in S:
            S.append(t)
    return tuple(sorted(S))


def fixed_dim(Rt, idx):
    """Dimension of the subspace the stabiliser leaves free.  0 == isolated."""
    return 3 - np.linalg.matrix_rank(
        np.vstack([Rt[i] - np.eye(3) for i in idx]), tol=1e-8)


def omega(R, T, k, a, b):
    """omega(R1,R2) = exp(2 pi i K1 . t2),  K1 = k - R1^T k in Z^3.

    See the module docstring: the earlier g = R1^{-T} k - k is NOT a 2-cocycle.
    """
    K1 = np.rint(k - np.asarray(R[a], float).T @ k)
    return cmath.exp(2j * np.pi * float(np.dot(K1, T[b])))


def factor_order(R, T, k, idx, cap=24):
    """Order of the IMAGE of omega -- the lcm of the orders of its values."""
    n = 1
    for a in idx:
        for b in idx:
            w = omega(R, T, k, a, b)
            for m in range(1, cap + 1):
                if abs(w ** m - 1) < 1e-6:
                    n = n * m // np.gcd(n, m)
                    break
            else:
                raise ValueError("omega not a root of unity")
    return int(n)


def extension(R, T, k, idx, n):
    """Central extension by Z_n:  (R,c)(R',c') = (RR', c+c'+phi).

    Returns (elements, Cayley table).  Valid ONLY when omega is a 2-cocycle,
    which is the whole content of the correction above.
    """
    els = [(i, c) for i in idx for c in range(n)]
    pos = {e: j for j, e in enumerate(els)}
    mult = [[0] * len(els) for _ in els]
    for A, (a, ca) in enumerate(els):
        for B, (b, cb) in enumerate(els):
            j = [q for q in idx if K(R[q]) == K(R[a] @ R[b])][0]
            phi = (round(float(np.angle(omega(R, T, k, a, b))) / (2 * np.pi / n)) % n
                   if n > 1 else 0)
            mult[A][B] = pos[(j, (ca + cb + phi) % n)]
    return els, mult


def is_group(mult):
    """Direct axiom test.  This is what exposed the broken multiplier.

    The identity is FOUND, not assumed to be element 0: assuming it would let a
    table fail this test for the wrong reason.
    """
    n = len(mult)
    e = [i for i in range(n)
         if all(mult[i][j] == j and mult[j][i] == j for j in range(n))]
    if len(e) != 1:
        return False
    e = e[0]
    for i in range(n):
        if not any(mult[i][j] == e for j in range(n)):
            return False
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if mult[mult[a][b]][c] != mult[a][mult[b][c]]:
                    return False
    return True


def char_table_cayley(mult):
    """Burnside's class algebra over a Cayley table.  Returns (classes, table)."""
    n = len(mult)
    inv = [next(j for j in range(n) if mult[i][j] == 0) for i in range(n)]
    seen = set()
    cls = []
    for i in range(n):
        if i in seen:
            continue
        c = sorted({mult[mult[x][i]][inv[x]] for x in range(n)})
        cls.append(c)
        seen |= set(c)
    cls.sort(key=lambda c: 0 if 0 in c else 1)
    nc = len(cls)
    co = [0] * n
    for ci, c in enumerate(cls):
        for g in c:
            co[g] = ci
    N = np.zeros((nc, nc, nc))
    for i in range(nc):
        for j in range(nc):
            cnt = np.zeros(nc)
            for a in cls[i]:
                for b in cls[j]:
                    cnt[co[mult[a][b]]] += 1
            for kk in range(nc):
                N[i][j][kk] = cnt[kk] / len(cls[kk])
    for seed in range(60):
        # A COMPLEX random combination: a real one cannot split a
        # complex-conjugate pair of eigenvalues, which a character table with
        # complex entries presents.  This was NOT the fix for the eighteen --
        # see the module docstring -- but it is still the right combination.
        rng = np.random.default_rng(seed)
        A = np.tensordot(rng.normal(size=nc) + 1j * rng.normal(size=nc), N, axes=(0, 0))
        _w, V = np.linalg.eig(A)
        out = []
        ok = True
        for t in range(nc):
            v = V[:, t]
            if abs(v[0]) < 1e-9:
                ok = False
                break
            om = v / v[0]
            base = np.array([om[i] / len(cls[i]) for i in range(nc)])
            s = sum(len(cls[i]) * abs(base[i]) ** 2 for i in range(nc))
            if abs(s) < 1e-12:
                ok = False
                break
            chi = base * np.sqrt(n / s)
            if np.real(chi[0]) < 0:
                chi = -chi
            out.append(chi)
        if not ok:
            continue
        Tb = np.array(out)
        d = [complex(x[0]) for x in Tb]
        if any(abs(z.imag) > 1e-6 or abs(z.real - round(z.real)) > 1e-6 for z in d):
            continue
        if abs(sum(round(z.real) ** 2 for z in d) - n) > 1e-6:
            continue
        bad = False
        for r in range(nc):
            for q in range(nc):
                ip = sum(len(cls[i]) * Tb[r][i] * np.conj(Tb[q][i])
                         for i in range(nc)) / n
                if abs(ip - (1.0 if r == q else 0.0)) > 1e-6:
                    bad = True
                    break
            if bad:
                break
        if bad:
            continue
        return cls, Tb
    raise RuntimeError("no valid table |G|=%d" % n)


def small_rep_dims(R, T, k, idx):
    """Dimensions of the SMALL representations at k.

    Ordinary irreps of the central extension whose central element acts as the
    primitive n-th root; for n = 1 that is every irrep of the little co-group.
    """
    n = factor_order(R, T, k, idx)
    els, mult = extension(R, T, k, idx, n)
    cls, Tb = char_table_cayley(mult)
    if n == 1:
        return n, [int(round(float(np.real(x[0])))) for x in Tb]
    ident = [i for i in idx if K(R[i]) == K(np.eye(3))][0]
    z = els.index((ident, 1))
    cz = [c for c in range(len(cls)) if z in cls[c]][0]
    keep = []
    for r in range(len(Tb)):
        d = float(np.real(Tb[r][0]))
        if abs(complex(Tb[r][cz]) - d * cmath.exp(2j * np.pi / n)) < 1e-6:
            keep.append(r)
    return n, [int(round(float(np.real(Tb[r][0])))) for r in keep]


def stars_of(sg, HN, mesh=12):
    """Every isolated high-symmetry k-star of one space group.

    Returns (R, T, [(star, k, little-group indices), ...]) in the capture's own
    order: descending little-group order, then the star's canonical tuple.
    """
    P, R, T, nc = primitive_ops(sg, HN)
    R = [np.asarray(x, float) for x in R]
    T = [np.asarray(x, float) for x in T]
    Rt = [np.linalg.inv(x).T for x in R]
    g = np.arange(mesh) / float(mesh)
    seen = {}
    for x in g:
        for y in g:
            for z in g:
                k = np.array([x, y, z])
                st = canon_star(Rt, k)
                if st in seen:
                    continue
                idx = [i for i, M in enumerate(Rt)
                       if np.max(np.abs((M @ k - k) - np.rint(M @ k - k))) < 1e-6]
                if fixed_dim(Rt, idx) != 0:
                    continue
                seen[st] = (k, idx)
    order = sorted(seen.items(), key=lambda kv: (-len(kv[1][1]), kv[0]))
    return R, T, [(st, k, idx) for st, (k, idx) in order]


def sweep(mesh=12, verbose=True):
    HN = hallmap()
    rows = []
    bad = []
    t0 = time.time()
    for sg in range(1, 231):
        R, T, stars = stars_of(sg, HN, mesh)
        for st, k, idx in stars:
            try:
                n, dims = small_rep_dims(R, T, k, idx)
            except Exception:
                n = factor_order(R, T, k, idx)
                rows.append((sg, system(sg), len(R), len(idx), len(st), n,
                             0, 0, "UNRESOLVED"))
                bad.append((sg, len(idx), "UNRESOLVED"))
                continue
            if sum(d * d for d in dims) != len(idx):
                bad.append((sg, len(idx), "sum d^2 mismatch"))
                continue
            rows.append((sg, system(sg), len(R), len(idx), len(st), n,
                         len(dims), max(dims),
                         "+".join(str(d) for d in sorted(dims, reverse=True))))
        if verbose and sg % 40 == 0:
            print("  sg %d  %.0fs  %d rows  %d bad"
                  % (sg, time.time() - t0, len(rows), len(bad)), file=sys.stderr)
    if verbose:
        print("\nswept in %.1f s" % (time.time() - t0), file=sys.stderr)
        print("k-point types seated : %d" % len(rows), file=sys.stderr)
        print("failures             : %d %s"
              % (len(bad), collections.Counter(b[2] for b in bad)), file=sys.stderr)
    return rows, bad


HEADER = ("sg\tsystem\tpg_order\tlittle_group\tstar\tfactor_order"
          "\tn_small_reps\tmax_dim\tdims\n")


def render(rows):
    return HEADER + "".join("\t".join(str(x) for x in r) + "\n" for r in rows)


def main():
    rows, bad = sweep()
    text = render(rows)
    if "--check" in sys.argv:
        old = open(OUT).read()
        print("IDENTICAL" if old == text else "DIFFERS", file=sys.stderr)
        sys.exit(0 if old == text else 1)
    open(OUT, "w").write(text)
    print("wrote %s (%d rows)" % (os.path.basename(OUT), len(rows)), file=sys.stderr)


def selftest():
    """Fixtures on the corrected multiplier, on three of the nine cubic groups
    that the broken one could not resolve, and on the capture as it stands."""
    HN = hallmap()
    fails = []

    def chk(name, got, want):
        ok = got == want
        if not ok:
            fails.append(name)
        print("%-4s %-62s %s" % ("ok" if ok else "FAIL", name,
                                 "" if ok else "got %r want %r" % (got, want)))

    # 1 -- the cocycle identity, which is the whole correction.
    def cocycle_dev(sg):
        """(worst deviation of k - R^T k, worst deviation of R^-T k - k).

        Over EVERY isolated star of the group, not just the first: at Gamma both
        conventions are trivially exact, so a test that stops there sees nothing.
        The product and phase tables are built once per star -- sg230 has
        |G_k| = 48 and the identity is a triple loop over the little group.
        """
        R, T, stars = stars_of(sg, HN)
        wg = wb = 0.0
        for st, k, idx in stars:
            n = len(idx)
            key = {K(np.rint(R[i])): a for a, i in enumerate(idx)}
            prod = [[key[K(np.rint(R[idx[a]] @ R[idx[b]]))] for b in range(n)]
                    for a in range(n)]
            pg = np.zeros((n, n))
            pb = np.zeros((n, n))
            for a in range(n):
                gvec = np.rint(np.linalg.inv(np.asarray(R[idx[a]], float)).T @ k - k)
                for b in range(n):
                    pg[a][b] = float(np.angle(omega(R, T, k, idx[a], idx[b]))) / (2 * np.pi)
                    pb[a][b] = -float(np.dot(gvec, T[idx[b]]))
            for ph, which in ((pg, 0), (pb, 1)):
                for a in range(n):
                    for b in range(n):
                        ab = prod[a][b]
                        for c in range(n):
                            d = ph[a][b] + ph[ab][c] - ph[b][c] - ph[a][prod[b][c]]
                            d = abs(d - round(d))
                            if which == 0:
                                wg = max(wg, d)
                            else:
                                wb = max(wb, d)
        return round(wg, 6), round(wb, 6)

    for sg in (199, 212, 230):
        chk("sg%d: k - R^T k IS a cocycle, R^-T k - k deviates by 1/2" % sg,
            cocycle_dev(sg), (0.0, 0.5))

    # 2 -- every extension the corrected multiplier builds is a GROUP.
    for sg in (198, 205, 214, 220):
        R, T, stars = stars_of(sg, HN)
        ok = True
        for st, k, idx in stars:
            n = factor_order(R, T, k, idx)
            els, mult = extension(R, T, k, idx, n)
            if not is_group(mult):
                ok = False
        chk("sg%d: every central extension satisfies the group axioms" % sg,
            ok, True)

    # 3 -- the nine groups that went UNRESOLVED all resolve, with sum d^2 = |G_k|.
    for sg in (198, 199, 205, 206, 212, 213, 214, 220, 230):
        R, T, stars = stars_of(sg, HN)
        ok = True
        for st, k, idx in stars:
            n, dims = small_rep_dims(R, T, k, idx)
            if sum(d * d for d in dims) != len(idx):
                ok = False
        chk("sg%d: all stars resolve, sum d^2 = |G_k|" % sg, ok, True)

    # 4 -- the capture itself.
    L = [l.split("\t") for l in open(OUT).read().splitlines() if l.strip()]
    hdr, body = L[0], L[1:]
    chk("the capture is 870 rows", len(body), 870)
    chk("no row is UNRESOLVED", sum(1 for r in body if r[8] == "UNRESOLVED"), 0)
    chk("162 space groups carry an isolated k-star; 68 carry none",
        (len({int(r[0]) for r in body}), 230 - len({int(r[0]) for r in body})),
        (162, 68))
    chk("the factor orders present", dict(sorted(collections.Counter(
        int(r[5]) for r in body).items())), {1: 471, 2: 351, 3: 14, 4: 32, 6: 2})
    chk("sum d^2 = |G_k| on every row",
        all(sum(int(d) ** 2 for d in r[8].split("+")) == int(r[3]) for r in body),
        True)
    chk("the header", "\t".join(hdr) + "\n", HEADER)

    print("\n%d failure(s)" % len(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    main()
