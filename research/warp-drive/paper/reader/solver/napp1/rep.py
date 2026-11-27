"""N-APP1: the printed representation of the certified approximant (computed tooling; the definitions are those of
proofs/P-APPC.md).  A case is a parameter: seed in {1, 2}, region D_A (u* = -2) or D* (u* = -11/10).

Chart:  xi = arsinh((u + 1)/a), a = 1/500.  Elements: n_xi x n_v boxes in (xi, v), x one element [-1, 1].
Element (i, j): box [m_i - h_i, m_i + h_i] x [m'_j - h'_j, m'_j + h'_j] (rational), t = (xi - m_i)/h_i,
sigma = (v - m'_j)/h'_j.  Partition of unity chi_i(xi) psi_j(v) from Phi(s) = e^{-1/s}/(e^{-1/s} + e^{-1/(1-s)}).
Fields:  F = F_seed + (v - 1/2)^4 sum_ij chi_i psi_j G^F_ij(t, sigma, x),  G = sum z 10^-p T_a(t) T_b(sigma) T_k(x),
F_seed = R_seed, W_seed (lem:tl5-seed) for R, W and 0 for m, n, s."""
from fractions import Fraction as Fr
import math, numpy as np

A_CH = Fr(1, 500)
FIELDS = ('R', 'm', 'n', 'W', 's')

# G0b section 6 targets (margin 10), mu at the M_w optimum; the printed target is f / 10 (S-APP 0.4 item 2)
CASES = {
    's1A': dict(seed=1, ustar=Fr(-2), nxi=2, nv=2, f=10 ** -16.5, mu=1e-3, L3=10.07, lam=1.0),
    's2A': dict(seed=2, ustar=Fr(-2), nxi=2, nv=2, f=10 ** -15.6, mu=1e-3, L3=8.06, lam=10 ** -0.5),
    's2D': dict(seed=2, ustar=Fr(-11, 10), nxi=2, nv=2, f=10 ** -19.1, mu=1e-3, L3=15.58, lam=10 ** -0.5),
    's1D': dict(seed=1, ustar=Fr(-11, 10), nxi=3, nv=2, f=10 ** -21.9, mu=1e-4, L3=18.37, lam=1.0),
}


def xi_of_u(u):
    return math.asinh((float(u) + 1) / float(A_CH))


def u_of_xi(xi):
    return -1 + float(A_CH) * np.sinh(xi)


def _round_dec(x, nd, mode):
    s = Fr(10) ** nd
    if mode == 'near':
        return Fr(round(x * float(s))) / s
    if mode == 'up':
        return Fr(math.ceil(x * float(s) - 1e-12)) / s
    return Fr(math.floor(x * float(s) + 1e-12)) / s


def layout(case, enlarge=True, clip=None):
    """element boxes and partition-of-unity parameters.  Returns dict with
    xi: list of (m, h) per xi-element, v: list of (m', h'), cxi, dxi (interior breakpoints, half-width of the
    transitions), cv, dv.  The use-interval of an element is the part of D where its partition function is
    positive; with enlarge, the box is the smallest 3-decimal box whose inner 90 % contains the use-interval.
    clip = (xi_lo, v_lo, v_hi) clips boxes to the data for the provisional source."""
    C = CASES[case]
    xlo, xhi = xi_of_u(-10), xi_of_u(C['ustar'])
    L = xhi - xlo
    n = C['nxi']
    cxi = [_round_dec(xlo + i * L / n, 2, 'near') for i in range(1, n)]
    dxi = _round_dec(0.05 * L / n, 3, 'near')                 # transition half-width: 5 % of an element
    cv = [Fr(1, 2) + Fr(3 * j, C['nv']) for j in range(1, C['nv'])]
    dv = Fr(3, 40 * C['nv'])                                  # 5 % of a v-element: 3/80 per side for two
    def boxes(lo, hi, cuts, d, nd):
        out = []
        ends = [lo] + [float(c) for c in cuts] + [hi]
        for i in range(len(ends) - 1):
            a = ends[i] - (float(d) if i > 0 else 0.0)
            b = ends[i + 1] + (float(d) if i < len(ends) - 2 else 0.0)
            m = _round_dec(0.5 * (a + b), nd, 'near')
            r = max(b - float(m), float(m) - a)
            h = _round_dec(r / 0.9 if enlarge else r, nd, 'up')
            out.append((m, h))
        return out
    xb = boxes(xlo, xhi, cxi, dxi, 3)
    vb = boxes(0.5, 3.5, cv, dv, 4)
    if clip is not None:
        xl, vl, vh = clip
        def cl(bx, lo, hi):
            out = []
            for (m, h) in bx:
                a, b = max(float(m - h), lo), min(float(m + h), hi)
                a, b = _round_dec(a, 3, 'down' if a == lo else 'near'), _round_dec(b, 3, 'up' if b == hi else 'near')
                out.append(((a + b) / 2, (b - a) / 2))
            return out
        xb = cl(xb, xl, 1e9); vb = cl(vb, vl, vh)
    return dict(xi=xb, v=vb, cxi=cxi, dxi=dxi, cv=cv, dv=dv, xlo=xlo, xhi=xhi)


# ----------------------------------------------------------------------------------- partition of unity (floats)
def Phi(s):
    s = np.asarray(s, float)
    out = np.where(s >= 1, 1.0, 0.0)
    inn = (s > 0) & (s < 1)
    si = np.where(inn, s, 0.5)
    a = np.exp(-1 / si); b = np.exp(-1 / (1 - si))
    return np.where(inn, a / (a + b), out)


def pou(y, cuts, d):
    """partition functions of the elements in one direction at points y (floats)"""
    n = len(cuts) + 1
    Ps = [Phi((y - float(c) + float(d)) / (2 * float(d))) for c in cuts]
    out = []
    for i in range(n):
        lo = Ps[i - 1] if i > 0 else 1.0
        hi = Ps[i] if i < n - 1 else 0.0
        out.append(lo - hi)
    return out


# --------------------------------------------------------------------------------------------- the seed (floats)
def seed_RW(U, V):
    """R_seed, W_seed by bisection + Newton on F(R) = e^{v-2u}(u+1)/(u-1), F(R) = e^{2R}(R-1)/(R+1) (u < -1)"""
    U = np.asarray(U, float); V = np.asarray(V, float)
    H = V - 2 * U + np.log((U + 1) / (U - 1))
    lo = np.full(U.shape, 1 + 1e-15); hi = np.full(U.shape, 80.0)
    for _ in range(120):
        mid = 0.5 * (lo + hi); g = 2 * mid + np.log((mid - 1) / (mid + 1))
        lo = np.where(g < H, mid, lo); hi = np.where(g < H, hi, mid)
    R = 0.5 * (lo + hi)
    for _ in range(3):
        g = 2 * R + np.log((R - 1) / (R + 1)); R = R - (g - H) / (2 * R * R / (R * R - 1))
    E2W = (R + 1) ** 2 * U ** 2 * np.exp(V - 2 * U - 2 * R) / (2 * R ** 2 * (U - 1) ** 2)
    return R, 0.5 * np.log(E2W)


# --------------------------------------------------------------------------------------------- printing and checks
def fmt(n):
    return ('−%d' % -n) if n < 0 else '%d' % n


def line_check(vals):
    return sum((m + 1) * v for m, v in enumerate(vals)) % 97


def block_sums(z):
    """S1 = sum z = 10^p G(1,1,1), S2 = 10^p G(-1,-1,-1), S0 = 10^p G(0,0,0) (exact integers)"""
    I, J, K = np.indices(z.shape)
    zo = z.astype(object)
    S1 = int(zo.sum())
    S2 = int((zo * ((-1) ** (I + J + K))).sum())
    ev = (I % 2 == 0) & (J % 2 == 0) & (K % 2 == 0)
    S0 = int((zo * np.where(ev, (-1) ** ((I + J + K) // 2), 0)).sum())
    return S1, S2, S0


def print_block(z, head, width=121, indent=4):
    """z: integer array (n_t+1, n_s+1, n_x+1) (object or int64).  Returns the lines of the block (header lines
    first).  Row (a, b) lists z_ab0 .. z_abK, K its last nonzero; rows with no nonzero entry are omitted."""
    lines = []; nrows = 0; nent = 0
    W = width - indent
    for a in range(z.shape[0]):
        for b in range(z.shape[1]):
            row = z[a, b]
            nz = np.nonzero(row)[0]
            if len(nz) == 0:
                continue
            row = [int(t) for t in row[:nz[-1] + 1]]
            nrows += 1; nent += len(row)
            cur = ('(%d,%d)' % (a, b)).ljust(8); vals = []
            for t in row:
                s = fmt(t)
                if len(cur) + 1 + len(s) + 4 > W and vals:
                    lines.append(cur + ' |%02d' % line_check(vals)); cur = '+'.ljust(8); vals = []
                cur += ' ' + s; vals.append(t)
            lines.append(cur + ' |%02d' % line_check(vals))
    S1, S2, S0 = block_sums(z)
    hdr = ['%s; rows %d; entries %d;' % (head, nrows, nent), 'S1 = %s,  S2 = %s,  S0 = %s' % (fmt(S1), fmt(S2), fmt(S0))]
    return [' ' * indent + h for h in hdr] + [' ' * indent + l for l in lines], nrows, nent


def read_block(lines, shape):
    """the reader's side: parse a printed block, verify every line check and the three block sums; returns z"""
    import re
    z = np.zeros(shape, dtype=object)
    hdr = lines[1].strip()
    S = [int(t.replace('−', '-')) for t in re.findall(r'S[120] = (\S+?),?\s', hdr + ' ')]
    cur = None; k = 0; bad = 0
    for l in lines[2:]:
        body, cc = l.rsplit('|', 1)
        lab = body[:len(body) - len(body.lstrip())] and body.strip()[:0]
        toks = body.split()
        if toks[0] == '+':
            vals = toks[1:]
        else:
            a, b = (int(q) for q in toks[0][1:-1].split(','))
            cur = (a, b); k = 0; vals = toks[1:]
        ints = [int(t.replace('−', '-')) for t in vals]
        if line_check(ints) != int(cc):
            bad += 1
        for t in ints:
            z[cur[0], cur[1], k] = t; k += 1
    ok = (bad == 0) and (list(block_sums(z)) == S)
    return z, ok, bad
