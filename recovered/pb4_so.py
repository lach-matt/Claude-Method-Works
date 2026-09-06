"""pb4_so.py -- s48: scores PREDICTION-PT-SO (PS-1..PS-5).
First-order spin-orbit on the SAME instrument as pb4_terms.py (hfc2 SR HF, CORR=False) --
zeta is recomputed on the hfc2 CONVERGED potential and grid, NOT on the SR-pol TS field, so
no instruments are mixed.
    zeta_nl = (alpha^2/2) * INT P^2 (1/r)(dV/dr) dr,  alpha = 1/c,  c = 137.035999
    V(r)    = -Z/r + SUM_b Q_b Y0_b(r)/r      (central Hartree field from the converged P)
Lowest-J LS shift per open shell, summed shell-additively (approximation declared in the
prediction file):  A_so = +z/(2S) if N<2l+1 else -z/(2S);  J=|L-S| or L+S;
    E_SO = (A_so/2)[J(J+1)-L(L+1)-S(S+1)]
(S,L) come from diag_sum_terms -- COMPUTED by the diagonal-sum rule, not asserted.
usage: python3 pb4_so.py 59 64   -> appends pb4_so.jsonl, resumable.
"""
import sys, os, json, time, numpy as np
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
import hfc2 as H; H.CORR = False
from t7c_kernel import C0
from hfterm import radial
from nlterm import opens, diag_sum_terms
from pb4_terms import XE, CASES

OUT = "pb4_so.jsonl"
TS = "SPDFGHIKLMNO"


def zeta_all(Z, occ):
    """converged hfc2, then zeta for every open shell from its own P on the same grid."""
    h = H.HFC(Z, occ, c=C0); E, _, it, eps = h.run2()
    r, dr, P = h.r, h.dr, h.P
    Q = {(n, l): q for n, l, q in occ}
    V = -Z / r + sum(Q[b] * h.Yk(P[b], P[b], 0) / r for b in P)
    dV = np.gradient(V, r)
    out = {}
    for (n, l), q in Q.items():
        if l == 0 or not (1e-9 < q < 2 * (2 * l + 1) - 1e-9): continue
        u = P[(n, l)]; u = u / np.sqrt(np.sum(u * u * dr))
        out[(n, l)] = float((1.0 / C0 ** 2) / 2 * np.sum(u * u * dV / r * dr))
    return float(E), out, it, h


def e_so(Z, tail):
    occ = XE + list(tail)
    E, zt, it, h = zeta_all(Z, occ)
    op = opens(occ)
    openk = [(n, l) for n, l, q in op]
    Fk, Gk = radial(h, openk)
    tot = 0.0; detail = []
    for i, (n, l, q) in enumerate(op):
        N = int(round(q))
        if l == 0: continue
        z = zt.get((n, l), 0.0)
        if N == 1:
            S, L = 0.5, l                      # single electron: 2L term
        else:
            m, L, _ = diag_sum_terms(l, N, Fk[(i, i)])[0]
            S = (m - 1) / 2.0
        half = 2 * l + 1
        if N < half:   A, J = z / (2 * S), abs(L - S)
        elif N > half: A, J = -z / (2 * S), L + S
        else:          A, J = 0.0, S           # exactly half-filled: L=0, no first-order shift
        e = (A / 2) * (J * (J + 1) - L * (L + 1) - S * (S + 1))
        tot += e
        detail.append(dict(nl=f"{n}{'spdf'[l]}", N=N, term=f"{int(2*S+1)}{TS[int(L)]}",
                           J=J, zeta=round(z, 6), E_SO=round(e, 6)))
    return float(E), float(tot), detail, it


if __name__ == "__main__":
    done = {d['Z'] for d in map(json.loads, open(OUT))} if os.path.exists(OUT) else set()
    prev = {d['Z']: d for d in map(json.loads, open("pb4_terms.jsonl"))}
    for Z in map(int, sys.argv[1:]):
        if Z in done: print("SKIP", Z); continue
        c = CASES[Z]; t0 = time.time()
        EA, soA, dA, itA = e_so(Z, c['A'])
        EB, soB, dB, itB = e_so(Z, c['B'])
        p = prev[Z]; dSO = soA - soB
        o = dict(Z=Z, el=c['el'], Acfg=c['Alab'], Bcfg=c['Blab'],
                 E_SO_A=round(soA, 6), E_SO_B=round(soB, 6), dSO=round(dSO, 6),
                 dTOT=p['dTOT'], dTOT_SO=round(p['dTOT'] + dSO, 6),
                 dAVG=p['dAVG'], dTERM=p['dTERM'], detA=dA, detB=dB,
                 it=[itA, itB], sec=int(time.time() - t0))
        open(OUT, "a").write(json.dumps(o) + "\n"); print(json.dumps(o), flush=True)
